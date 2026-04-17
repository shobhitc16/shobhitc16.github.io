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
    <h3 class="stats-number" style="color:var(--global-theme-color)">761+</h3>
    <p class="small text-muted">Total Citations</p>
  </div>
  <div class="col-md-3 col-6">
    <h3 class="stats-number" style="color:var(--global-theme-color)">18</h3>
    <p class="small text-muted">h-index</p>
  </div>
  <div class="col-md-3 col-6">
    <h3 class="stats-number" style="color:var(--global-theme-color)">21</h3>
    <p class="small text-muted">i10-index</p>
  </div>
</div>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
