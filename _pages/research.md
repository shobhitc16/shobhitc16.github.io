---
layout: page
permalink: /research/
title: Research
description: Understanding enzyme catalysis, predicting and engineering enzyme function, and applying frontier methods toward sustainable chemistry and human health.
nav: true
nav_order: 1
---

Enzymes achieve extraordinary catalytic efficiency through the precise organization of their protein scaffolds — arranging charges, dynamics, and electronic interactions to stabilize transition states and direct reaction outcomes. My research investigates the physical principles that underpin this control and translates them into strategies for discovering novel reactivity, predicting catalytic function, and designing enzymes with tailored properties.

This program is organized around three interconnected questions: _Why_ do enzymes catalyze specific reactions with such precision? _How_ can we predict and engineer catalytic function? And _what for_ — how can these insights drive real-world applications in health, energy, and sustainability?

<div class="row mt-3 mb-4">
  <div class="col-md-4 mb-3">
    <a href="#understanding-enzyme-catalysis" class="text-decoration-none">
      <div class="card research-pillar h-100 border-0 shadow-sm text-center p-4">
        <div class="pillar-icon-wrapper">
          <i class="fas fa-atom fa-2x" style="color:var(--global-theme-color)"></i>
        </div>
        <h5 class="mt-3 mb-2">Understanding Catalysis</h5>
        <p class="small text-muted mb-0">Why do enzymes catalyze with such extraordinary precision and selectivity?</p>
      </div>
    </a>
  </div>
  <div class="col-md-4 mb-3">
    <a href="#predicting--engineering-enzyme-function" class="text-decoration-none">
      <div class="card research-pillar h-100 border-0 shadow-sm text-center p-4">
        <div class="pillar-icon-wrapper">
          <i class="fas fa-brain fa-2x" style="color:var(--global-theme-color)"></i>
        </div>
        <h5 class="mt-3 mb-2">Predicting & Engineering</h5>
        <p class="small text-muted mb-0">How can we predict catalytic function and design enzymes with new capabilities?</p>
      </div>
    </a>
  </div>
  <div class="col-md-4 mb-3">
    <a href="#frontier-applications" class="text-decoration-none">
      <div class="card research-pillar h-100 border-0 shadow-sm text-center p-4">
        <div class="pillar-icon-wrapper">
          <i class="fas fa-rocket fa-2x" style="color:var(--global-theme-color)"></i>
        </div>
        <h5 class="mt-3 mb-2">Frontier Applications</h5>
        <p class="small text-muted mb-0">Quantum computing, drug discovery, and sustainable catalysis for real-world impact.</p>
      </div>
    </a>
  </div>
</div>

---

## <i class="fas fa-atom"></i> Understanding Enzyme Catalysis

_Why do enzymes catalyze specific reactions with extraordinary selectivity?_

<div class="row mb-3">
<div class="col-md-8" markdown="1">

I investigate the physical principles by which protein scaffolds control catalytic outcomes using **hybrid QM/MM simulations** (DFT, DLPNO-CCSD(T)), **microsecond-scale molecular dynamics**, **dynamic 3D electric field mapping**, and **automated reaction network exploration**. A central focus has been the **non-heme iron/2OG enzyme superfamily** — where I have uncovered how coordination dynamics, substrate reorientation, and second coordination sphere interactions drive catalytic diversity, including predicting a **novel bicarbonate intermediate** validated in _Science_ (2021). I have mapped **three-dimensional electric fields** within active sites as quantitative descriptors of catalytic potential, revealing latent compatibility with **non-native functions** — a physical basis for evolving new chemistry. Using microsecond MD, I characterized **allosteric communication pathways** and **correlated motions** that modulate catalysis far from the active site, and developed validated **force field parameters** for metalloenzyme simulations. Currently at ETH Zürich, I am integrating QM/MM with **Chemoton** to explore reaction networks without human bias — discovering undiscovered enzyme chemistry at scale.

</div>
<div class="col-md-4">
<img src="/assets/img/publication_preview/chaturvedi2020acscatal.jpg" class="img-fluid rounded shadow-sm" alt="PHF8 mechanism — iron center rearrangement">
</div>
</div>

<div class="alert signature-result" style="border-left:4px solid var(--global-theme-color); background:rgba(var(--global-theme-color-rgb, 0, 123, 255),0.05);">
  <i class="fas fa-star" style="color:var(--global-theme-color)"></i> <strong>Signature Result:</strong> Predicted a novel bicarbonate intermediate in the ethylene-forming enzyme — subsequently validated by experimental characterization published in <em>Science</em> (2021, 373, 1489).
</div>

<details class="pub-list" markdown="1">
<summary><strong>Key publications</strong></summary>

- _ACS Catal._ 2020, 10, 1195–1209 (Iron center rearrangement in histone demethylase PHF8)
- _ACS Catal._ 2021, 11, 1578–1592 (Ethylene-forming enzyme: novel pathway validated in _Science_)
- _JACS Au_ 2022, 2, 2169–2186 (Second coordination sphere modulation in histone demethylase)
- _ACS Central Science_ 2020, 6, 795–814 (Selectivity in DNA repair oxygenases)
- _Chem. Eur. J._ 2023, 29, e202300138 (Protein environment controls dioxygen binding in non-heme iron enzymes)
- _Chem Catalysis_ 2023, 3, 100732 (Catalytic strategy of the FTO obesity enzyme)
- _Inorg. Chem._ 2024, 63, 10737–10755 (Second coordination sphere control in KDM2A)
- _Phys. Chem. Chem. Phys._ 2023, 25, 13772–13783 (External electric field control of reactivity)
- _Chem. Sci._ 2020, 11, 9950–9961 (Substrate dynamics and correlated motions in KDM4A)
- _Chem. Eur. J._ 2019, 25, 5422–5426 (Conformational dynamics in KDM7 demethylases)

</details>

---

## <i class="fas fa-brain"></i> Predicting & Engineering Enzyme Function

_How can we predict catalytic function and design enzymes with new capabilities?_

<div class="row mb-3">
<div class="col-md-8" markdown="1">

I develop computational methods, **open-source software**, and **machine learning** approaches that translate mechanistic understanding into predictive power and enzyme design. Applying ML to **electric field fingerprints**, I showed that models can classify enzymatic function with up to **84% accuracy** — revealing electrostatic signatures as the **physical basis of functional divergence** across enzyme families and enabling the **prediction of evolutionary starting points** for new reactivity. This work led to **PyCPET**, an open-source toolbox for computing heterogeneous 3D protein electric fields, integrating MD, topological analysis, and QM/MM into a unified pipeline. I demonstrated that **directed evolution optimizes the enzyme's electric field** — not just individual residues — in protoglobin's non-native cyclopropanation activity, establishing the second coordination sphere as a powerful lever for rational design. My long-term vision is **inverse enzyme design**: starting from a desired catalytic outcome, identifying the optimal electric field, and using ML with **AlphaFold/diffusion models** to generate scaffolds that produce that field — shifting from sequence-first to **field-first** design.

</div>
<div class="col-md-4">
<img src="/assets/img/publication_preview/chaturvedi2023chemsci.gif" class="img-fluid rounded shadow-sm" alt="Rational enzyme design — electric field guided">
</div>
</div>

<details class="pub-list" markdown="1">
<summary><strong>Key publications</strong></summary>

- _Chem. Rev._ 2025, 125, 3772–3813 (Comprehensive review: methods for local fields in enzymes)
- _J. Am. Chem. Soc._ 2025, 147, 32225–32237 (Distinct EFs enable common function across enzyme families)
- _J. Am. Chem. Soc._ 2024, 146, 28375–28383 (ML prediction of enzyme function from electric fields)
- _J. Am. Chem. Soc._ 2024, 146, 16670–16680 (Electric field optimization in directed evolution)
- _J. Chem. Theory Comput._ 2025, 21, 4299–4308 (PyCPET: open-source EF software)
- _Chemical Science_ 2023, 14, 10997–11011 (From random to rational enzyme design)

</details>

---

## <i class="fas fa-rocket"></i> Frontier Applications

_What for — how can these insights drive real-world impact?_

<div class="row mb-3">
<div class="col-md-8" markdown="1">

At ETH Zürich, as part of an **XPRIZE finalist team**, I am developing high-performance pipelines for **biological applications on quantum computers** — tackling strongly correlated metal centers intractable by classical methods. I apply electric field-guided and second coordination sphere engineering to **heme and non-heme metalloenzymes**, including **cytochrome P450** variants for selective transformations and the catalytic mechanism of **nitrogenase** for sustainable nitrogen fixation. I also contribute to **artificial metalloenzyme design** for CO<sub>2</sub> capture and conversion, extending mechanistic insights to engineered catalysts for green chemistry. In drug discovery, I apply **free energy perturbation** simulations to characterize inhibitor binding to &alpha;-synuclein aggregation targets in **Parkinson's disease**.

</div>
<div class="col-md-4">
<img src="/assets/img/publication_preview/chaturvedi2023pccp.gif" class="img-fluid rounded shadow-sm" alt="Electric field control of reactivity">
</div>
</div>

<details class="pub-list" markdown="1">
<summary><strong>Recent outputs &amp; ongoing collaborations</strong></summary>

- _ChemRxiv_ 2025 (Artificial metalloenzyme for Re(I)-catalyzed CO<sub>2</sub> photoreduction; with Yang group, UC Irvine, and Rovis group, Columbia)
- Cytochrome P450 engineering for selective C–H functionalisation _(ongoing; with Ward group, University of Basel)_
- Quantum-computing pipelines for biological metal centers _(ongoing; XPRIZE finalist team, ETH Zürich)_
- Nitrogenase catalytic mechanism _(ongoing; NITRO-GENESE consortium)_

</details>
