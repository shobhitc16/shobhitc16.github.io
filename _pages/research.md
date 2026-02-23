---
layout: page
permalink: /research/
title: research
description: Discovering how protein scaffolds control enzyme catalysis — and translating these principles into enzyme engineering, machine learning tools, and sustainable chemistry.
nav: true
nav_order: 1
---

Enzymes achieve extraordinary catalytic efficiency through the precise organization of their protein scaffolds — arranging charges, dynamics, and electronic interactions to stabilize transition states and direct reaction outcomes. My research investigates the physical principles that underpin this control and translates them into strategies for discovering novel reactivity, predicting catalytic function, and engineering enzymes with tailored properties.

---

## Discovering Novel Reaction Mechanisms in Metalloenzymes

The foundation of my research program is the discovery and characterization of reaction mechanisms in metalloenzymes, with a focus on the non-heme iron and 2-oxoglutarate (2OG)-dependent enzyme superfamily. These enzymes catalyze a remarkable diversity of reactions — hydroxylation, demethylation, halogenation, desaturation — that are central to epigenetic regulation, DNA repair, and biosynthesis of signaling molecules.

Using **hybrid QM/MM** simulations at multiple levels of theory (DFT, DLPNO-CCSD(T)) embedded in explicit protein environments, combined with extensive **molecular dynamics** (500 ns–1 &mu;s), I have uncovered how coordination dynamics at the iron center, conformational motions, and long-range interactions collectively govern catalytic selectivity and efficiency. Notably, I predicted a novel bicarbonate intermediate in the ethylene-forming enzyme — a finding subsequently **validated through experimental characterization** (Copeland et al., _Science_ 2021, 373, 1489). My work on histone demethylases revealed that iron center rearrangement and substrate reorientation are essential catalytic steps, insights that have informed therapeutic targeting of epigenetic enzymes. I have also developed and validated **force field parameters** for metal centers in metalloenzymes, enabling accurate classical simulations of these challenging systems.

This mechanistic research extends to **drug discovery** through free energy perturbation (FEP) simulations characterizing inhibitor binding to &alpha;-synuclein aggregation targets in Parkinson's disease, demonstrating the translational potential of fundamental mechanistic understanding.

**Key publications:**

- _ACS Catal._ 2020, 10, 1195–1209 (Iron center rearrangement in histone demethylase PHF8)
- _ACS Catal._ 2021, 11, 1578–1592 (Ethylene-forming enzyme: novel pathway validated in _Science_)
- _Chem. Eur. J._ 2023, 29, e202203713 (Mechanistic bifurcation in isopenicillin N synthase)
- _JACS Au_ 2022, 2, 2326–2340 (QM/MM mechanism of isopenicillin N synthase)
- _ACS Central Science_ 2020, 6, 795–814 (Selectivity in DNA repair oxygenases)
- _Chem Catalysis_ 2023, 3, 100732 (Catalytic strategy of the FTO obesity enzyme)
- _Inorg. Chem._ 2024, 63, 10737–10755 (Second coordination sphere control in KDM2A)
- _ChemPhysChem_ 2021, 22, 1073–1081 (Molecular dynamics of lipoxygenase)

---

## Computational Method Development & Machine Learning

To move beyond case-by-case mechanistic studies, I develop computational methods and software tools that capture the physical basis of catalysis at scale. A central innovation is the mapping of **dynamic, three-dimensional electric fields** within enzyme active sites — quantifying the electrostatic preorganization that protein scaffolds impose on catalytic centers.

I developed protocols integrating molecular dynamics, topological analysis, unsupervised clustering, and QM/MM calculations into a unified pipeline for characterizing heterogeneous electric field landscapes. This program led to **PyCPET**, an open-source toolbox for computing 3D protein electric fields and their dynamics. Applying machine learning to these electric field fingerprints, I showed that ML models can **predict and classify enzymatic function with up to 84% accuracy** — distinguishing monooxygenases, peroxidases, and catalases from electrostatics alone, without reliance on sequence or structural features. These methods reveal that electrostatic signatures are not merely descriptors but the **physical basis of functional divergence** across enzyme families.

**Key publications:**

- _Chem. Rev._ 2025, 125, 3772–3813 (Comprehensive review: methods for local fields in enzymes)
- _J. Am. Chem. Soc._ 2024, 146, 28375–28383 (ML prediction of enzyme function from electric fields)
- _J. Am. Chem. Soc._ 2024, 146, 16670–16680 (Electric field evolution during directed evolution)
- _J. Chem. Theory Comput._ 2025, 21, 4299–4308 (PyCPET: open-source EF software)
- _Chemical Science_ 2023, 14, 8027–8046 (Review: second coordination sphere in metalloenzymes)
- _Phys. Chem. Chem. Phys._ 2023, 25, 13772–13783 (External electric field control of reactivity)

---

## Rational Enzyme Engineering & Design

Translating mechanistic and methodological insights into practical enzyme engineering is a central goal of my research. I have shown that the **second coordination sphere** — residues beyond the immediate active site — exerts powerful control over catalysis through modulation of electric field landscapes, correlated motions, and substrate positioning. By systematically mapping how mutations in this sphere alter electric field distributions, I provide a rational framework for engineering enzymes that goes beyond traditional active-site mutagenesis.

A key demonstration is my analysis of **directed evolution in protoglobin**, where I showed that laboratory evolution optimizes the enzyme's electric field to support non-native cyclopropanation catalysis — revealing that evolution operates on the electrostatic environment, not just on individual residues. Building on this, my long-term goal is **inverse enzyme design**: starting from a desired catalytic outcome, identifying the optimal electric field profile, and using ML to predict or generate protein scaffolds that produce that field. This approach, leveraging AlphaFold and diffusion models for scaffold screening, represents a shift from sequence-first to field-first engineering strategies.

This pillar also encompasses the design of **artificial metalloenzymes** for sustainable chemistry, including Re(I)-catalyzed CO<sub>2</sub> photoreduction in collaboration with experimental groups.

**Key publications:**

- _J. Am. Chem. Soc._ 2025, 147, 32225–32237 (Distinct EFs enable common function across enzyme families)
- _J. Am. Chem. Soc._ 2024, 146, 16670–16680 (Electric field optimization in directed evolution)
- _JACS Au_ 2022, 2, 2169–2186 (SCS and long-range interactions modulate catalysis in PHF8)
- _Chemical Science_ 2023, 14, 10997–11011 (From random to rational enzyme design)
- _ACS Central Science_ 2020, 6, 2160–2167 (SCS effects in lipoxygenase)
- _ChemRxiv_ 2026 (Artificial metalloenzyme for Re(I)-catalyzed CO<sub>2</sub> photoreduction)

---

## Quantum Computing & Sustainable Chemistry

At ETH Zurich, I am extending my research into emerging computational paradigms and applications in sustainability. As part of an **XPRIZE finalist team**, I develop high-performance pipelines for biological applications on quantum computers — bridging quantum chemistry with biological modeling to tackle problems intractable by classical methods.

I am also scaling **automated reaction network exploration** (Chemoton) by integrating QM/MM methods for complex enzyme catalysis, enabling systematic discovery of reaction pathways without human bias. In parallel, I collaborate on rational engineering of **cytochrome P450** metalloenzyme variants and contribute to a multi-group initiative elucidating the catalytic mechanism and electronic structure of **nitrogenase** — one of the most challenging problems in bioinorganic chemistry. These efforts connect fundamental enzymology to applications in sustainable chemical synthesis, green catalysis, and next-generation computational platforms.
