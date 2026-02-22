---
layout: page
permalink: /research/
title: research
description: Research areas spanning computational chemistry, enzyme design, machine learning, and quantum computing.
nav: true
nav_order: 1
---

My research integrates computational chemistry, machine learning, and emerging quantum computing methods to understand and engineer enzyme catalysis.

---

## Enzyme Electric Fields, Machine Learning & Rational Design

A unifying theme of my work is the role of **electric fields** in enzyme catalysis. I developed computational frameworks that map time-resolved, three-dimensional electric field landscapes within enzyme active sites — revealing how protein scaffolds modulate electrostatics along reaction coordinates. I showed that these electrostatic signatures are not merely descriptors but the **physical basis** of functional divergence: machine learning models trained on electric field fingerprints can predict and classify enzymatic function with up to 84% accuracy, distinguishing monooxygenases, peroxidases, and catalases from electrostatics alone. By systematically mapping how **second coordination sphere** mutations alter electric field landscapes, I provide a rational framework for enzyme engineering that goes beyond traditional active-site approaches. This program led to the development of **PyCPET**, an open-source toolbox for computing heterogeneous 3D protein electric fields and their dynamics.

**Key publications:**

- _Chem. Rev._ 2025 (Comprehensive review: electric fields in enzymes)
- _J. Am. Chem. Soc._ 2024, 146, 28375–28383 (ML prediction of enzyme function from electric fields)
- _J. Am. Chem. Soc._ 2024, 146, 16670–16680 (Electric field evolution in protoglobin directed evolution)
- _J. Chem. Theory Comput._ 2025, 21, 4299–4308 (PyCPET software)
- _Chemical Science_ 2023, 14, 8027–8046 (Review: second coordination sphere in metalloenzymes)
- _ACS Central Science_ 2020, 6, 2160–2167 (SCS effects in lipoxygenase)

---

## Metalloenzyme Mechanisms & Multiscale Simulations

I employ **hybrid QM/MM** simulations — treating the catalytic core with high-level quantum methods (DFT, DLPNO-CCSD(T)) while embedding it in a classically treated protein environment — to elucidate detailed reaction mechanisms of metalloenzymes. These studies have revealed how protein structure controls reaction energetics and selectivity in non-heme iron enzymes, including novel pathways later validated experimentally (_Science_). Complementing this, I use extensive **classical molecular dynamics** simulations (500 ns–1 &mu;s) to characterize conformational dynamics, correlated motions, and allosteric communication pathways that underpin catalysis. I have also developed and validated force field parameters for metal centers in metalloenzymes, proteins, and nucleic acids.

**Key publications:**

- _JACS Au_ 2022, 2, 2169–2186 (SCS and long-range interactions in histone demethylase)
- _JACS Au_ 2022, 2, 2326–2340 (QM/MM mechanism of isopenicillin N synthase)
- _Chem. Eur. J._ 2023, 29, e202203713 (Bifurcation in IPNS mechanism)
- _ACS Catal._ 2020, 10, 1195–1209 (Iron center rearrangement in PHF8)
- _ChemPhysChem_ 2021, 22, 1073–1081 (MD analysis of lipoxygenase dynamics)
- _J. Phys. Chem. B_ 2020, 124, 8149–8159 (Protein dynamics in metalloenzymes)

---

## Drug Discovery, Artificial Metalloenzymes & Sustainability

In collaboration with experimental groups, I apply advanced **free energy perturbation** (FEP) simulations and large-scale DFT calculations to drug discovery, including characterizing the binding of inhibitors targeting &alpha;-synuclein aggregation in Parkinson's disease. In a separate effort, I contribute to designing **artificial metalloenzymes** for sustainable chemistry, including Re(I)-catalyzed CO<sub>2</sub> photoreduction. These projects extend my electrostatics and enzyme engineering expertise toward therapeutic and sustainability applications.

---

## Quantum Computing & Automated Reaction Networks

At ETH Zurich, I am part of an **X-prize finalist team** developing high-performance pipelines for biological applications on quantum computers — bridging quantum chemistry with biological modeling. I am also scaling **Chemoton's** automated reaction network exploration by integrating QM/MM for complex enzyme catalysis, collaborating on rational engineering of **P450** metalloenzyme variants, and contributing to a multi-group initiative elucidating the catalytic mechanism and electronic structure of **Nitrogenase**.
