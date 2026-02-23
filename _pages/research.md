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

The foundation of my research is uncovering the physical principles by which protein scaffolds control catalytic outcomes — and discovering **previously unknown chemistry** hidden within enzyme active sites. I combine **hybrid QM/MM simulations** at multiple levels of theory (DFT, DLPNO-CCSD(T)), extensive **molecular dynamics** (500 ns–1 &mu;s), **dynamic 3D electric field mapping**, and **automated reaction network exploration** to reveal how electrostatics, conformational dynamics, correlated motions, and long-range interactions collectively govern enzymatic selectivity, efficiency, and the potential for novel reactivity.

**Novel reaction mechanisms and catalytic discovery.** A major focus is the non-heme iron and 2-oxoglutarate (2OG)-dependent enzyme superfamily — catalysts of hydroxylation, demethylation, halogenation, and desaturation reactions central to epigenetic regulation, DNA repair, and biosynthesis. I have uncovered how coordination dynamics at the iron center, substrate reorientation, and second coordination sphere interactions drive catalytic diversity. Notably, I predicted a novel bicarbonate intermediate in the ethylene-forming enzyme — a finding subsequently **validated through experimental characterization** (Copeland et al., _Science_ 2021, 373, 1489). I also discovered **catalytic bifurcation** pathways where a single enzyme active site can steer reactions toward entirely different products depending on the dynamic electric field environment.

**Conformational dynamics and allosteric control.** Using microsecond-scale MD simulations, I characterize **conformational landscapes, correlated motions, and allosteric communication pathways** that modulate catalysis. These studies reveal how long-range protein dynamics — far from the active site — influence reaction outcomes, providing the dynamic context in which electric fields operate. I have also developed and validated **force field parameters** for metal centers in metalloenzymes, enabling accurate classical simulations of these challenging systems.

**Dynamic 3D electric field mapping.** A central innovation is the mapping of **dynamic, three-dimensional electric fields** within enzyme active sites — quantifying the electrostatic preorganization that protein scaffolds impose on catalytic centers. These fields, intrinsically tied to protein conformational fluctuations, serve as quantitative descriptors of catalytic potential. I have shown that dynamic EF components, while dormant under native conditions, can harbor latent compatibility with **non-native catalytic functions** — providing a physical basis for how enzymes can be evolved toward new chemistry.

**Automated reaction network exploration.** Beyond case-by-case studies, I integrate QM/MM methods with systematic search algorithms (**Chemoton**) to explore reaction networks without human bias — enabling the discovery of **undiscovered enzyme chemistry** at scale. This approach systematically maps the space of possible reactions an enzyme can catalyze, identifying pathways that would be missed by hypothesis-driven investigations alone.

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

To translate fundamental understanding into predictive power and practical enzyme design, I develop **computational methods**, **open-source software**, and **machine learning** approaches that bridge mechanistic insight with engineering.

**Machine learning for enzyme function prediction.** Applying ML to electric field fingerprints, I showed that models can predict and classify enzymatic function with up to **84% accuracy** — distinguishing monooxygenases, peroxidases, and catalases from electrostatics alone, without reliance on sequence or structural features. These methods reveal that electrostatic signatures are the **physical basis of functional divergence** across enzyme families, opening a new avenue for computational enzyme classification. By identifying enzymes with multi-reactive electric fields — fields that support alternative reaction pathways not dominant under native conditions — ML enables the **prediction of evolutionary starting points** for developing new reactivity.

**Open-source software for electric field analysis.** This program led to the development of **PyCPET**, an open-source toolbox for computing heterogeneous 3D protein electric fields and their dynamics. PyCPET integrates molecular dynamics, topological analysis, unsupervised clustering, and QM/MM calculations into a unified pipeline, making electric field analysis accessible to the broader enzyme science community.

**Rational enzyme design through second coordination sphere engineering.** I have shown that the **second coordination sphere** — residues beyond the immediate active site — exerts powerful control over catalysis through modulation of electric field landscapes, correlated motions, and substrate positioning. A key demonstration is my analysis of **directed evolution in protoglobin**, where I showed that laboratory evolution optimizes the enzyme's electric field to support non-native cyclopropanation catalysis — revealing that evolution operates on the electrostatic environment, not just on individual residues.

**Inverse enzyme design.** Building on these insights, my long-term goal is **inverse enzyme design**: starting from a desired catalytic outcome, identifying the optimal electric field profile, and using ML with protein structure prediction (AlphaFold, diffusion models) to generate scaffolds that produce that field. This shifts the paradigm from sequence-first to **field-first** design strategies, providing a scalable framework for engineering enzymes with new-to-nature functions.

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

My fundamental and methodological research converges on applications with direct societal relevance, spanning **quantum computing for biology**, **drug discovery**, **artificial metalloenzyme design**, and **sustainable catalysis**.

**Quantum computing for biological applications.** At ETH Zurich, as part of an **XPRIZE finalist team**, I develop high-performance pipelines for biological applications on quantum computers — bridging quantum chemistry with biological modeling to tackle problems intractable by classical methods, such as accurate treatment of strongly correlated metal centers in metalloenzymes.

**Sustainable catalysis and green chemistry.** I collaborate on rational engineering of **cytochrome P450** metalloenzyme variants for selective chemical transformations and contribute to a multi-group initiative elucidating the catalytic mechanism and electronic structure of **nitrogenase** — one of the most challenging problems in bioinorganic chemistry, with direct implications for sustainable nitrogen fixation. I also contribute to the design of **artificial metalloenzymes** for CO<sub>2</sub> capture and conversion, including Re(I)-catalyzed CO<sub>2</sub> photoreduction — demonstrating how electric field and mechanistic insights can be extended from natural enzymes to engineered catalysts for green chemistry.

**Drug discovery and therapeutic applications.** I apply **free energy perturbation** (FEP) simulations and large-scale DFT calculations to characterize inhibitor binding to &alpha;-synuclein aggregation targets in Parkinson's disease, translating fundamental mechanistic understanding into therapeutic impact.

**Key publications:**

- _ChemRxiv_ 2026 (Artificial metalloenzyme for Re(I)-catalyzed CO<sub>2</sub> photoreduction)
