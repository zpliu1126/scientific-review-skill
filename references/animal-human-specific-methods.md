# Animal and Human Functional Gene Research Reference

## 1. Scope

This file supports interpretation and review writing for literature on animal functional gene research, human genetics, disease mechanisms, cell models, model organisms, clinical cohorts, iPSC systems, organoids, single-cell studies, and multi-omics research. It highlights methods and evidence issues that are more common or more specific in animal and human research than in plant research.

## 2. Core Differences from Plant Research

- Human research is constrained by ethics and cannot freely use genetic modification experiments in humans.
- Animal research can use model organisms, controlled breeding, transgenic lines, and conditional knockout systems.
- Human research often relies more heavily on cohorts, clinical samples, genetic statistics, and in vitro models.
- Cell line results cannot be treated as equivalent to in vivo tissue or organism-level results.
- Mouse or other model organism findings cannot be directly generalized to humans without supporting human evidence.
- Clinical relevance does not by itself prove causal mechanism.

## 3. Common Methods in Animal Research

- Cell line experiments: useful for controlled perturbation and mechanistic screening; limited by cell type, culture conditions, and transformation state.
- siRNA/shRNA knockdown: reduces gene expression; requires knockdown efficiency and off-target assessment.
- CRISPR cell lines: generate knockout, knock-in, or edited cellular models; require validation of genotype, clone effects, and off-target risk.
- Transgenic animals: test gene function in an organismal context through overexpression, reporter, knock-in, or engineered alleles.
- Whole-body knockout and conditional knockout: test gene function at the organism or tissue-specific level.
- Cre-LoxP system: enables spatial, temporal, or cell-type-specific recombination when appropriate Cre drivers are available.
- Disease model animals: model pathological processes, genetic disease, inflammation, cancer, metabolism, neurobiology, or infection.
- Histopathology: evaluates tissue architecture, lesions, inflammation, degeneration, fibrosis, or tumor changes.
- Immunohistochemistry and immunofluorescence: localize proteins, cell types, or tissue markers.
- Flow cytometry: quantifies cell populations, immune phenotypes, cell cycle, apoptosis, or reporter signals.
- Behavioral assays: measure animal behavior, cognition, motor function, anxiety-like behavior, social behavior, pain, or disease-related phenotypes.
- Pharmacological intervention experiments: test pathway involvement or therapeutic response; off-target effects and dosing must be considered.
- Organoid or primary cell models: preserve more physiological features than immortalized cell lines but remain simplified systems.

## 4. Common Methods in Human Research

- Case-control studies: compare affected and unaffected groups; sensitive to matching, confounding, and population structure.
- Cohort studies: follow participants over time; useful for risk, prognosis, and exposure-outcome relationships.
- GWAS: identifies genetic loci associated with traits or disease; loci are not automatically causal genes.
- WGS/WES: identifies genome-wide or exome variants; interpretation requires segregation, frequency, predicted impact, and functional evidence.
- eQTL, pQTL, and mQTL: link genetic variants to RNA, protein, or methylation variation; useful for regulatory inference.
- Mendelian randomization: uses genetic instruments to infer potential causality; depends on instrument validity and assumptions.
- Clinical sample transcriptomics: profiles disease-associated expression changes in patient tissues or blood.
- Single-cell transcriptomics: resolves cell states, cell types, and disease-associated cellular heterogeneity.
- Spatial transcriptomics: links expression patterns to tissue architecture and spatial context.
- Patient-derived cells: model patient-specific genetic or disease contexts in vitro.
- iPSC and differentiated models: enable human genetic background modeling and cell-type-specific differentiation.
- Organoids: model aspects of tissue organization, development, or disease in vitro.
- Biomarker analysis: evaluates diagnostic, prognostic, predictive, or pharmacodynamic markers.
- Drug sensitivity analysis: tests response to compounds in cells, organoids, ex vivo systems, or patient-derived models.

## 5. Evidence Hierarchy

Evidence strength generally increases through the following levels. Strength depends on design, replication, controls, model relevance, statistical rigor, and independent validation.

### expression association

Can support: association between gene expression and disease state, tissue type, cell state, treatment, or phenotype.

Cannot support: causal involvement of the gene in disease or physiology by itself.

### case-control association

Can support: association between a variant, expression pattern, biomarker, or phenotype and disease status.

Cannot support: causal mechanism without control for confounders, replication, and functional evidence.

### genetic association

Can support: statistical association between genetic variants and traits or disease, including GWAS, WGS/WES, or QTL-based evidence.

Cannot support: direct identification of the causal gene or mechanism without fine mapping, functional validation, or convergent evidence.

### cellular perturbation

Can support: evidence that gene knockdown, knockout, overexpression, editing, or drug treatment changes cellular phenotype.

Cannot support: organism-level or human disease conclusions without relevant tissue, in vivo, or clinical evidence.

### animal model evidence

Can support: gene function or disease mechanism in an organismal context.

Cannot support: direct human conclusions without evidence that the model captures relevant human biology.

### rescue experiment

Can support: stronger causal evidence when restoring gene function, pathway activity, or molecular state rescues phenotype.

Cannot support: full clinical relevance if rescue is limited to a simplified model or non-human system.

### mechanistic biochemical evidence

Can support: protein interaction, enzyme activity, binding, signaling, transcriptional regulation, or molecular mechanism.

Cannot support: physiological or clinical importance without phenotype and disease-context evidence.

### human cohort replication

Can support: robustness of association across independent human cohorts, populations, datasets, or clinical contexts.

Cannot support: mechanism by itself; replication strengthens association, not necessarily causality.

### clinical or therapeutic validation

Can support: clinical relevance, biomarker utility, therapeutic response, or intervention value in patient-related settings.

Cannot support: complete molecular mechanism unless paired with mechanistic and functional evidence.

## 6. Literature Interpretation Notes

- Correlation is not causation.
- Cell line results cannot directly represent tissues or whole organisms.
- Animal model findings cannot be directly generalized to humans.
- A GWAS locus is not the same as a causal disease gene.
- Drug treatment experiments require attention to off-target effects.
- siRNA/shRNA studies require validation of knockdown efficiency and off-target risk.
- CRISPR studies require attention to off-target effects, clone effects, and compensatory effects.
- Clinical samples require attention to age, sex, disease stage, treatment history, tissue source, batch effects, and other confounders.
- Single-cell results require attention to cell annotation, batch effects, sample size, and dissociation bias.
- iPSC and organoid models require attention to maturation state, differentiation efficiency, batch variation, and model fidelity.
- Biomarker associations require independent validation before diagnostic, prognostic, or predictive claims.

## 7. Review Writing Guidance

- First distinguish cellular evidence, animal evidence, and human evidence.
- Do not write cell experiment results as direct human mechanisms.
- Do not write animal model results as direct human conclusions.
- Use cautious language for clinical relevance, such as "is associated with", "may contribute to", "is consistent with", or "requires validation".
- Mark unsupported points as `[source needed]`; mark available but unchecked support as `[needs verification]`.
- Compare evidence across model systems and state where findings converge or diverge.
- Separate disease association, mechanistic evidence, and therapeutic validation.
- Reserve strong causal language for claims supported by perturbation, rescue, mechanism, and relevant in vivo or human evidence.
