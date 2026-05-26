# Plant and Omics Evidence Rules

Use this reference when interpreting plant science, crop science, stress physiology, molecular biology, transcriptomics, metabolomics, proteomics, or multi-omics papers.

## Core Principle

Omics results generate evidence and hypotheses. They do not automatically prove gene function, pathway mechanism, or causal regulation.

## RNA-seq and DEG

- RNA-seq supports expression differences under the reported conditions.
- Differentially expressed genes are candidates, not validated causal genes.
- Report species, cultivar/ecotype, tissue, developmental stage, treatment, time point, replicate design, sequencing approach, and threshold when available.
- Do not invent DEG counts, fold change thresholds, adjusted p values, or gene IDs.

## GO, KEGG, and GSEA

- GO/KEGG/GSEA enrichment supports functional clues at the gene-set or pathway level.
- Enrichment does not prove pathway activation, metabolite change, or mechanism.
- Distinguish annotation-based inference from measured physiology, metabolomics, enzyme activity, or functional assays.

## WGCNA and Co-Expression

- WGCNA supports correlation between modules, traits, treatments, or expression patterns.
- Hub genes are priority candidates, not proven regulators.
- Avoid causal language unless supported by perturbation, binding, genetic, or rescue evidence.

## qRT-PCR/qPCR

- qRT-PCR/qPCR can validate expression trends for selected genes.
- qRT-PCR/qPCR does not validate gene function by itself.
- Check whether qRT-PCR/qPCR uses independent samples, appropriate reference genes, and consistent treatment conditions when reported.

## Functional Validation

Evidence for stronger functional claims may include:

- Mutant phenotypes.
- Overexpression, knockdown, VIGS, RNAi, CRISPR, or complementation.
- Rescue experiments.
- Promoter-reporter or localization assays.
- Yeast one-hybrid, EMSA, ChIP-qPCR, dual-luciferase, protein interaction, or binding assays.
- Physiological measurements under stress, such as survival, biomass, chlorophyll, photosynthesis, ROS, MDA, proline, ion content, water-use efficiency, or yield traits.

## Recommended Claim Language

- DEG only: "is differentially expressed under..."
- DEG plus enrichment: "is associated with..." or "may participate in..."
- Co-expression: "is correlated with..." or "is a candidate hub gene for..."
- qRT-PCR/qPCR validation: "expression trends were validated for selected genes..."
- Functional validation: "contributes to..." only when perturbation and phenotype evidence support the claim.
