# Methods extracted from Paper

Paper ID: `2016-Wang-Cotton-Temperature-miRNAs`

Source basis: `mineru-parsed/Wang_2016_Scientific Reports/full.md` and `content_list.json`.

## Method list

### Temperature stress treatment and physiological assays

- Method name: Cotton seedling temperature treatments
- Purpose: Establish low/high temperature stress conditions.
- Input material/data: two-leaf-stage G. hirsutum cv. YZ1 seedlings.
- Output: wilting phenotype; H2O2, proline, MDA, soluble sugar measurements.
- Key parameters: 4, 12, 25, 35 and 42 deg C for 8 h.
- Strengths: confirms stress physiology before sequencing.
- Limitations: short-term seedling assay only.
- Used in which result: Finding 1.

### small RNA sequencing

- Method name: sRNA library construction and Illumina sequencing
- Purpose: Identify and quantify cotton small RNAs under temperature stress.
- Input material/data: leaf total RNA from five temperature treatments, duplicated samples.
- Output: clean reads, size distribution, known/novel miRNAs.
- Key parameters: small RNAs purified from 10 ug total RNA; five pooled libraries; 18-24/28 nt reads used depending on analysis.
- Strengths: broad miRNA discovery.
- Limitations: pooled library wording and replicate handling need manual check.
- Used in which result: Findings 2-4.

### miRNA identification

- Method name: miRBase homology and Mireap novel miRNA prediction
- Purpose: Identify conserved and novel miRNAs.
- Input material/data: cleaned sRNA reads; G. hirsutum AD genome.
- Output: 319 known miRNAs and 800 novel miRNAs.
- Key parameters: <=2 mismatches to miRBase 21.0; hairpin precursor criteria for novel miRNAs.
- Strengths: combines conserved and species-specific candidates.
- Limitations: computational novel miRNAs require validation.
- Used in which result: Finding 3.

### Degradome sequencing and target analysis

- Method name: degradome/PARE target identification
- Purpose: Identify miRNA-cleaved target mRNAs.
- Input material/data: five degradome libraries from cotton leaves.
- Output: miRNA-target pairs and cleavage categories.
- Key parameters: no mismatches allowed at mature miRNA positions 10 and 11; PAREsnip P < 0.05; target categories 0-4.
- Strengths: stronger than prediction-only target lists.
- Limitations: cleavage evidence does not prove stress phenotype contribution.
- Used in which result: Finding 5.

### qRT-PCR and enrichment analysis

- Method name: qRT-PCR validation plus GO/KEGG enrichment
- Purpose: Validate selected expression patterns and infer pathway context.
- Input material/data: selected miRNAs/targets; target gene annotations.
- Output: relative expression and enriched functional categories.
- Key parameters: UBQ7 internal control; three biological replicates; GO FDR <0.05; KEGG P <0.05.
- Strengths: supports sequencing and functional interpretation.
- Limitations: enrichment is pathway-level inference.
- Used in which result: Findings 4-5.
