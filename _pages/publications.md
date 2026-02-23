---
layout: page
permalink: /publications/
title: publications
description: Publications in reversed chronological order, generated from BibTeX via jekyll-scholar.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<div class="row text-center mb-4 stats-row">
  <div class="col-md-3 col-6">
    <h3 class="stats-number" style="color:var(--global-theme-color)">25+</h3>
    <p class="small text-muted">Publications</p>
  </div>
  <div class="col-md-3 col-6">
    <h3 class="stats-number" style="color:var(--global-theme-color)">10</h3>
    <p class="small text-muted">First-Author Papers</p>
  </div>
  <div class="col-md-3 col-6">
    <h3 class="stats-number" style="color:var(--global-theme-color)">13+</h3>
    <p class="small text-muted">Journals</p>
  </div>
  <div class="col-md-3 col-6">
    <h3 class="stats-number" style="color:var(--global-theme-color)">2018–2026</h3>
    <p class="small text-muted">Publication Span</p>
  </div>
</div>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
