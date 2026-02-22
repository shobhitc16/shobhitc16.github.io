#!/usr/bin/env python3
"""
Fetch new publications from ORCID and append to papers.bib.

Queries the ORCID Public API for works, extracts DOIs,
fetches BibTeX via doi.org content negotiation, and appends
new entries to _bibliography/papers.bib.

Preserves manually curated fields (selected, abbr, preview, etc.)
by only appending entries whose DOI is not already in the file.
"""

import json
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ORCID_ID = "0000-0003-4977-5600"
BIB_FILE = Path(__file__).parent.parent / "_bibliography" / "papers.bib"
ORCID_API = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"


def get_existing_dois(bib_path: Path) -> set:
    """Extract all DOIs already present in the bib file."""
    dois = set()
    if not bib_path.exists():
        return dois
    content = bib_path.read_text()
    for match in re.finditer(r"doi\s*=\s*\{([^}]+)\}", content, re.IGNORECASE):
        dois.add(match.group(1).strip().lower())
    return dois


def fetch_orcid_dois() -> list:
    """Fetch all DOIs from ORCID works."""
    req = urllib.request.Request(
        ORCID_API,
        headers={"Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        print(f"Error fetching ORCID data: {e}", file=sys.stderr)
        return []

    dois = []
    for group in data.get("group", []):
        for summary in group.get("work-summary", []):
            ext_ids = summary.get("external-ids", {}).get("external-id", [])
            for eid in ext_ids:
                if eid.get("external-id-type") == "doi":
                    doi = eid.get("external-id-value", "").strip()
                    if doi:
                        dois.append(doi)
                        break  # one DOI per work is enough
    return dois


def fetch_bibtex(doi: str) -> str:
    """Fetch BibTeX entry from doi.org content negotiation."""
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={"Accept": "application/x-bibtex"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode().strip()
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  Warning: Could not fetch BibTeX for {doi}: {e}", file=sys.stderr)
        return ""


def add_alfolio_fields(bibtex: str, doi: str) -> str:
    """Add al-folio-specific fields to a BibTeX entry."""
    # Add bibtex_show, dimensions, altmetric if not present
    additions = []
    if "bibtex_show" not in bibtex:
        additions.append("  bibtex_show   = {true},")
    if "dimensions" not in bibtex:
        additions.append("  dimensions    = {true},")
    if "altmetric" not in bibtex:
        additions.append("  altmetric     = {true},")
    if "html" not in bibtex:
        additions.append(f"  html          = {{https://doi.org/{doi}}},")

    if additions:
        # Insert before the closing brace
        lines = bibtex.rstrip().rstrip("}").rstrip()
        if not lines.endswith(","):
            lines += ","
        bibtex = lines + "\n" + "\n".join(additions) + "\n}"

    return bibtex


def main():
    print(f"Fetching publications from ORCID: {ORCID_ID}")
    existing_dois = get_existing_dois(BIB_FILE)
    print(f"Found {len(existing_dois)} existing DOIs in {BIB_FILE}")

    orcid_dois = fetch_orcid_dois()
    print(f"Found {len(orcid_dois)} DOIs from ORCID")

    new_dois = [d for d in orcid_dois if d.lower() not in existing_dois]
    if not new_dois:
        print("No new publications to add.")
        return

    print(f"Found {len(new_dois)} new publications to fetch:")
    new_entries = []
    for doi in new_dois:
        print(f"  Fetching: {doi}")
        bibtex = fetch_bibtex(doi)
        if bibtex and bibtex.startswith("@"):
            bibtex = add_alfolio_fields(bibtex, doi)
            new_entries.append(f"% DOI: {doi}\n{bibtex}")
        time.sleep(1)  # Be polite to doi.org

    if new_entries:
        with open(BIB_FILE, "a") as f:
            f.write("\n\n% === Auto-added from ORCID ===\n\n")
            f.write("\n\n".join(new_entries))
            f.write("\n")
        print(f"Added {len(new_entries)} new entries to {BIB_FILE}")
    else:
        print("No valid BibTeX entries fetched.")


if __name__ == "__main__":
    main()
