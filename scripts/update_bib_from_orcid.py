#!/usr/bin/env python3
"""
Fetch new publications from ORCID and append them to ``_bibliography/papers.bib``.

Pipeline:
  1. Read all DOIs and cite keys already present in papers.bib.
  2. Query ORCID Public API for the user's works -> list of DOIs.
  3. For each DOI not already in the file, fetch a BibTeX record from
     doi.org via content negotiation.
  4. Validate the record (real title, not a cover/errata, unique cite key,
     not a known-superseded preprint), normalise its formatting, add the
     al-folio side fields, and append.

Design choices that fix the previous duplicate-pollution bug:
  * DOIs are normalised before comparison: lower-cased, URL-prefix
    stripped, version suffix (``/v2``, ``/v3`` ...) stripped. Same paper
    on ChemRxiv as a v1 and v2 preprint cannot be added twice.
  * BibTeX entries without a non-empty title are rejected.
  * Entries whose title looks like a cover/errata/correction companion
    citation are rejected (the publisher mints a separate DOI for these
    that ORCID happily reports).
  * Cite-key collisions are resolved by renaming the new entry rather
    than emitting a duplicate.
  * Dry-run mode (``--dry-run``) prints the diff plan and writes nothing.
  * Each fetched record is reformatted to one field per line so the
    diff in version control stays human-readable.

Re-running the script is idempotent: if no new publications appear on
ORCID, papers.bib is left untouched.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ORCID_ID = "0000-0003-4977-5600"
BIB_FILE = Path(__file__).resolve().parent.parent / "_bibliography" / "papers.bib"
ORCID_API = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"

# Titles starting with any of these prefixes are companion citations
# (cover image, cover profile, errata, corrections, retractions, etc.)
# that share authorship with a paper but should not be listed separately.
SKIP_TITLE_PREFIXES = (
    "front cover",
    "back cover",
    "cover profile",
    "cover picture",
    "cover image",
    "frontispiece",
    "inside cover",
    "errata",
    "erratum",
    "correction",
    "corrigendum",
    "retraction",
    "withdrawn",
    "comment on",
    "reply to",
)

# Keys that look like the bot's old single-line auto-import format
# (e.g. ``Ajmera_2025``, ``Varghese_2022``). We re-key these ourselves.
AUTO_KEY_PATTERN = re.compile(r"^[A-Z][a-zA-Z]+_\d{4}$")


# ---------------------------------------------------------------------------
# DOI helpers
# ---------------------------------------------------------------------------


def normalise_doi(doi: str) -> str:
    """Canonicalise a DOI for set-membership comparison.

    Strips a URL prefix, lower-cases, and removes a trailing version suffix
    such as ``/v2``. Preprint v1 and v2 of the same paper collapse to the
    same key.
    """
    if not doi:
        return ""
    d = doi.strip()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d, flags=re.IGNORECASE)
    d = d.rstrip("/").lower()
    d = re.sub(r"/v\d+$", "", d)
    return d


def normalise_title(title: str) -> str:
    """Canonicalise a title for set-membership comparison.

    Lower-cases, strips punctuation, and collapses whitespace. This catches
    duplicates where ORCID has a separate DOI for a preprint version and a
    journal version of the same paper — they share a title even if their
    DOIs differ.
    """
    if not title:
        return ""
    t = title.lower()
    t = re.sub(r"[‐-―−\-]", " ", t)  # all dash variants
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def get_existing_state(
    bib_path: Path,
) -> tuple[set[str], set[str], set[str]]:
    """Return (DOIs, cite keys, normalised titles) already in the bib file."""
    dois: set[str] = set()
    keys: set[str] = set()
    titles: set[str] = set()
    if not bib_path.exists():
        return dois, keys, titles
    content = bib_path.read_text()
    for match in re.finditer(r"\bdoi\s*=\s*\{([^}]+)\}", content, re.IGNORECASE):
        dois.add(normalise_doi(match.group(1)))
    for match in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", content):
        keys.add(match.group(1).strip().lower())
    for match in re.finditer(
        r"\btitle\s*=\s*\{((?:[^{}]|\{[^{}]*\})+)\}",
        content,
        re.IGNORECASE | re.DOTALL,
    ):
        titles.add(normalise_title(match.group(1)))
    return dois, keys, titles


# ---------------------------------------------------------------------------
# ORCID + doi.org fetchers
# ---------------------------------------------------------------------------


def fetch_orcid_dois() -> list[str]:
    """Return DOIs for all of the user's ORCID works (one per work)."""
    req = urllib.request.Request(
        ORCID_API, headers={"Accept": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        print(f"Error fetching ORCID data: {e}", file=sys.stderr)
        return []

    dois: list[str] = []
    for group in data.get("group", []):
        for summary in group.get("work-summary", []):
            for eid in (
                summary.get("external-ids", {}).get("external-id", [])
            ):
                if eid.get("external-id-type") == "doi":
                    doi = eid.get("external-id-value", "").strip()
                    if doi:
                        dois.append(doi)
                        break  # one DOI per work is enough
    return dois


def fetch_bibtex(doi: str) -> str:
    """Return the BibTeX record for ``doi`` via doi.org content negotiation."""
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={"Accept": "application/x-bibtex"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode().strip()
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  warn: could not fetch BibTeX for {doi}: {e}", file=sys.stderr)
        return ""


# ---------------------------------------------------------------------------
# BibTeX parsing helpers
# ---------------------------------------------------------------------------


def parse_fields(bibtex: str) -> dict[str, str]:
    """Lift ``key = {value}`` fields out of a BibTeX entry into a dict.

    Naive but sufficient: doesn't handle quoted values or nested braces beyond
    one level — fine for entries minted by Crossref/DataCite via doi.org.
    """
    fields: dict[str, str] = {}
    # Greedy-but-balanced match for {...} including one level of nested braces.
    pattern = re.compile(
        r"(\b[a-zA-Z_][a-zA-Z0-9_-]*)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}",
        re.DOTALL,
    )
    for m in pattern.finditer(bibtex):
        fields[m.group(1).lower()] = m.group(2).strip()
    return fields


def parse_entry_type_and_key(bibtex: str) -> tuple[str, str]:
    """Return (entry_type, cite_key); empty strings if unparseable."""
    m = re.match(r"\s*@(\w+)\s*\{\s*([^,\s]+)\s*,", bibtex)
    if not m:
        return "", ""
    return m.group(1).lower(), m.group(2).strip()


def looks_like_companion_citation(title: str) -> bool:
    """True if title is a cover/errata/comment/etc. companion citation."""
    t = title.strip().lower()
    return any(t.startswith(p) for p in SKIP_TITLE_PREFIXES)


def make_cite_key(fields: dict[str, str], used_keys: set[str]) -> str:
    """Generate ``firstauthorYEARkeyword`` style key, unique within ``used_keys``.

    Mirrors the manual style of existing entries so the file stays uniform.
    """
    author_field = fields.get("author", "")
    first_author = ""
    if author_field:
        # "Last, First and Last, First and ..."
        first_chunk = author_field.split(" and ")[0]
        first_author = first_chunk.split(",")[0].strip()
    first_author = re.sub(r"[^A-Za-z]", "", first_author).lower() or "anon"

    year = fields.get("year", "").strip()
    year_match = re.search(r"\d{4}", year)
    year = year_match.group(0) if year_match else "nodate"

    title = fields.get("title", "")
    keyword = ""
    for word in re.findall(r"[A-Za-z]+", title):
        if len(word) >= 4 and word.lower() not in {
            "from", "with", "into", "this", "that", "these", "those",
            "based", "using", "study", "studies", "analysis",
        }:
            keyword = word.lower()
            break
    base = f"{first_author}{year}{keyword}"

    candidate = base
    suffix = 1
    while candidate.lower() in used_keys or not candidate:
        suffix += 1
        candidate = f"{base}{suffix}"
    return candidate


# ---------------------------------------------------------------------------
# BibTeX rewriting
# ---------------------------------------------------------------------------


# Field order matches the manual entries already in papers.bib.
PREFERRED_ORDER = [
    "abbr",
    "bibtex_show",
    "title",
    "author",
    "journal",
    "booktitle",
    "publisher",
    "school",
    "volume",
    "number",
    "pages",
    "year",
    "month",
    "doi",
    "url",
    "html",
    "preview",
    "code",
    "pdf",
    "supp",
    "dimensions",
    "altmetric",
    "selected",
    "award",
    "abstract",
]


def render_entry(
    entry_type: str, cite_key: str, fields: dict[str, str], doi: str
) -> str:
    """Render a multi-line BibTeX entry in the project's house style."""
    fields = dict(fields)  # copy
    fields["doi"] = doi  # always use the canonical DOI we fetched against
    fields.setdefault("html", f"https://doi.org/{doi}")
    fields.setdefault("bibtex_show", "true")
    fields.setdefault("dimensions", "true")
    fields.setdefault("altmetric", "true")

    ordered_keys = [k for k in PREFERRED_ORDER if k in fields]
    leftover = [k for k in fields if k not in ordered_keys]
    ordered_keys += sorted(leftover)

    pad = max(len(k) for k in ordered_keys)
    lines = [f"@{entry_type}{{{cite_key},"]
    for k in ordered_keys:
        v = fields[k].strip()
        if not v:
            continue
        # collapse internal whitespace for a one-line value
        v = re.sub(r"\s+", " ", v)
        lines.append(f"  {k.ljust(pad)} = {{{v}}},")
    # drop trailing comma on last field for stylistic parity
    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be added; don't modify papers.bib.",
    )
    args = parser.parse_args()

    print(f"ORCID:    {ORCID_ID}")
    print(f"BibFile:  {BIB_FILE}")
    existing_dois, existing_keys, existing_titles = get_existing_state(BIB_FILE)
    print(
        f"Existing: {len(existing_dois)} DOIs, {len(existing_keys)} cite keys, "
        f"{len(existing_titles)} titles"
    )

    orcid_dois = fetch_orcid_dois()
    print(f"ORCID:    {len(orcid_dois)} DOIs returned")

    # Filter to DOIs we don't already have (after normalisation).
    new_dois: list[str] = []
    seen_normalised: set[str] = set()
    for raw in orcid_dois:
        norm = normalise_doi(raw)
        if not norm:
            continue
        if norm in existing_dois or norm in seen_normalised:
            continue
        seen_normalised.add(norm)
        new_dois.append(raw)

    if not new_dois:
        print("No new publications to add — papers.bib already up to date.")
        return 0

    print(f"Candidates: {len(new_dois)} DOI(s) not yet in papers.bib")

    new_entries: list[str] = []
    used_keys = set(existing_keys)
    used_titles = set(existing_titles)
    skipped_no_title = 0
    skipped_companion = 0
    skipped_duplicate_title = 0
    skipped_fetch = 0

    for doi in new_dois:
        print(f"  fetching: {doi}")
        bibtex = fetch_bibtex(doi)
        if not bibtex or not bibtex.lstrip().startswith("@"):
            skipped_fetch += 1
            continue

        entry_type, original_key = parse_entry_type_and_key(bibtex)
        fields = parse_fields(bibtex)

        title = fields.get("title", "").strip()
        if not title:
            print(f"    skip (no title): {doi}")
            skipped_no_title += 1
            continue
        if looks_like_companion_citation(title):
            print(f"    skip (cover/errata): {title[:60]}")
            skipped_companion += 1
            continue
        title_key = normalise_title(title)
        if title_key in used_titles:
            print(f"    skip (title already present): {title[:60]}")
            skipped_duplicate_title += 1
            continue

        # Decide cite key. If the publisher gave us a clean one (e.g.
        # ``smith2020topology``) reuse it. If it's the
        # ``Capitalised_Year`` shape Crossref emits, regenerate it.
        if (
            original_key
            and original_key.lower() not in used_keys
            and not AUTO_KEY_PATTERN.match(original_key)
            and original_key.lower() != "year"
            and not original_key.isdigit()
        ):
            cite_key = original_key
        else:
            cite_key = make_cite_key(fields, used_keys)

        used_keys.add(cite_key.lower())
        used_titles.add(title_key)

        rendered = render_entry(entry_type or "article", cite_key, fields, doi)
        new_entries.append(rendered)

        time.sleep(1)  # be polite to doi.org

    print()
    print(
        f"Plan: add {len(new_entries)}, skip "
        f"{skipped_no_title} no-title, "
        f"{skipped_companion} companion citations, "
        f"{skipped_duplicate_title} duplicate titles, "
        f"{skipped_fetch} fetch failures."
    )

    if not new_entries:
        return 0

    if args.dry_run:
        print("\n--- DRY RUN: entries that would be added ---")
        for e in new_entries:
            print(e)
            print()
        return 0

    with BIB_FILE.open("a") as f:
        f.write("\n\n% === Auto-added from ORCID ===\n")
        for e in new_entries:
            f.write("\n")
            f.write(e)
            f.write("\n")
    print(f"Appended {len(new_entries)} entries to {BIB_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
