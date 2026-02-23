---
layout: page
permalink: /research/
title: research
description: Understanding enzyme catalysis, predicting and engineering enzyme function, and applying frontier methods toward sustainable chemistry and human health.
nav: true
nav_order: 1
---

Enzymes achieve extraordinary catalytic efficiency through the precise organization of their protein scaffolds — arranging charges, dynamics, and electronic interactions to stabilize transition states and direct reaction outcomes. My research investigates the physical principles that underpin this control and translates them into strategies for discovering novel reactivity, predicting catalytic function, and designing enzymes with tailored properties.

This program is organized around three interconnected questions: _Why_ do enzymes catalyze specific reactions with such precision? _How_ can we predict and engineer catalytic function? And _what for_ — how can these insights drive real-world applications in health, energy, and sustainability?

---

## Understanding Enzyme Catalysis

_Why do enzymes catalyze specific reactions with extraordinary selectivity?_

The foundation of my research is uncovering the physical principles by which protein scaffolds control catalytic outcomes. I combine **hybrid QM/MM** simulations at multiple levels of theory (DFT, DLPNO-CCSD(T)), extensive **molecular dynamics** (500 ns–1 &mu;s), and **electric field analysis** to reveal how electrostatics, conformational dynamics, correlated motions, and long-range interactions collectively govern enzymatic selectivity and efficiency.

A major focus is the non-heme iron and 2-oxoglutarate (2OG)-dependent enzyme superfamily — catalysts of hydroxylation, demethylation, halogenation, and desaturation reactions central to epigenetic regulation, DNA repair, and biosynthesis. In these systems, I have uncovered how coordination dynamics at the iron center, substrate reorientation, and second coordination sphere interactions drive catalytic diversity. Notably, I predicted a novel bicarbonate intermediate in the ethylene-forming enzyme — a finding subsequently **validated through experimental characterization** (Copeland et al., _Science_ 2021, 373, 1489). I have also developed and validated **force field parameters** for metal centers in metalloenzymes, enabling accurate classical simulations of these challenging systems.

A central innovation is the mapping of **dynamic, three-dimensional electric fields** within enzyme active sites — quantifying the electrostatic preorganization that protein scaffolds impose on catalytic centers. These fields, intrinsically tied to protein conformational dynamics, serve as quantitative descriptors of catalytic potential. Complementing this, I characterize **conformational landscapes, correlated motions, and allosteric communication pathways** that modulate catalysis, providing the dynamic context in which electric fields operate.

Beyond case-by-case studies, I pursue **automated reaction network exploration** — integrating QM/MM methods with systematic search algorithms (Chemoton) to discover reaction pathways without human bias, enabling scalable catalytic discovery across enzyme families.

**Key publications:**

- _ACS Catal._ 2020, 10, 1195–1209 (Iron center rearrangement in histone demethylase PHF8)
- _ACS Catal._ 2021, 11, 1578–1592 (Ethylene-forming enzyme: novel pathway validated in _Science_)
- _Chem. Eur. J._ 2023, 29, e202203713 (Mechanistic bifurcation in isopenicillin N synthase)
- _JACS Au_ 2022, 2, 2326–2340 (QM/MM mechanism of isopenicillin N synthase)
- _JACS Au_ 2022, 2, 2169–2186 (Correlated motions and SCS modulation in histone demethylase)
- _ACS Central Science_ 2020, 6, 795–814 (Selectivity in DNA repair oxygenases)
- _Chem Catalysis_ 2023, 3, 100732 (Catalytic strategy of the FTO obesity enzyme)
- _Inorg. Chem._ 2024, 63, 10737–10755 (Second coordination sphere control in KDM2A)
- _Phys. Chem. Chem. Phys._ 2023, 25, 13772–13783 (External electric field control of reactivity)
- _ChemPhysChem_ 2021, 22, 1073–1081 (Molecular dynamics of lipoxygenase)
- _Chem. Eur. J._ 2019, 25, 5422–5426 (Conformational dynamics in KDM7 demethylases)

---

## Predicting & Engineering Enzyme Function

_How can we predict catalytic function and design enzymes with new capabilities?_

To translate fundamental understanding into predictive power and practical enzyme design, I develop computational methods, software tools, and machine learning approaches that bridge mechanistic insight with engineering.

A cornerstone is **PyCPET**, an open-source toolbox for computing heterogeneous 3D protein electric fields and their dynamics. Applying **machine learning** to electric field fingerprints, I showed that ML models can predict and classify enzymatic function with up to **84% accuracy** — distinguishing monooxygenases, peroxidases, and catalases from electrostatics alone, without reliance on sequence or structural features. These methods reveal that electrostatic signatures are the **physical basis of functional divergence** across enzyme families, opening a new avenue for computational enzyme classification and design.

On the design front, I have shown that the **second coordination sphere** — residues beyond the immediate active site — exerts powerful control over catalysis through modulation of electric field landscapes. A key demonstration is my analysis of **directed evolution in protoglobin**, where I showed that laboratory evolution optimizes the enzyme's electric field to support non-native cyclopropanation catalysis — revealing that evolution operates on the electrostatic environment, not just on individual residues. Building on this, my long-term goal is **inverse enzyme design**: starting from a desired catalytic outcome, identifying the optimal electric field profile, and using ML with protein structure prediction (AlphaFold, diffusion models) to generate scaffolds that produce that field. This shifts the paradigm from sequence-first to **field-first** design strategies.

**Key publications:**

- _Chem. Rev._ 2025, 125, 3772–3813 (Comprehensive review: methods for local fields in enzymes)
- _J. Am. Chem. Soc._ 2025, 147, 32225–32237 (Distinct EFs enable common function across enzyme families)
- _J. Am. Chem. Soc._ 2024, 146, 28375–28383 (ML prediction of enzyme function from electric fields)
- _J. Am. Chem. Soc._ 2024, 146, 16670–16680 (Electric field optimization in directed evolution)
- _J. Chem. Theory Comput._ 2025, 21, 4299–4308 (PyCPET: open-source EF software)
- _Chemical Science_ 2023, 14, 10997–11011 (From random to rational enzyme design)
- _Chemical Science_ 2023, 14, 8027–8046 (Review: second coordination sphere in metalloenzymes)
- _ACS Central Science_ 2020, 6, 2160–2167 (SCS effects in lipoxygenase)

---

## Frontier Applications

_What for — how can these insights drive real-world impact in health, energy, and sustainability?_

My fundamental and methodological research converges on applications with direct societal relevance, spanning **quantum computing for biology**, **drug discovery**, **artificial metalloenzymes**, and **sustainable catalysis**.

At ETH Zurich, as part of an **XPRIZE finalist team**, I develop high-performance pipelines for biological applications on quantum computers — bridging quantum chemistry with biological modeling to tackle problems intractable by classical methods. I collaborate on rational engineering of **cytochrome P450** metalloenzyme variants for selective chemical transformations and contribute to a multi-group initiative elucidating the catalytic mechanism and electronic structure of **nitrogenase** — one of the most challenging problems in bioinorganic chemistry, with direct implications for sustainable nitrogen fixation.

In parallel, I apply **free energy perturbation** (FEP) simulations to drug discovery, characterizing inhibitor binding to &alpha;-synuclein aggregation targets in Parkinson's disease. I also contribute to the design of **artificial metalloenzymes** for sustainable chemistry, including Re(I)-catalyzed CO<sub>2</sub> photoreduction — demonstrating how electric field and mechanistic insights can be extended from natural enzymes to engineered catalysts for green chemistry.

**Key publications:**

- _ChemRxiv_ 2026 (Artificial metalloenzyme for Re(I)-catalyzed CO<sub>2</sub> photoreduction)
