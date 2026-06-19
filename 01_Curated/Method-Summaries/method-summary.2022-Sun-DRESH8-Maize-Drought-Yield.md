# Methods extracted from Paper

Paper ID: `2022-Sun-DRESH8-Maize-Drought-Yield`

Source basis: `mineru-parsed/Sun_2023_Nature Biotechnology_2/full.md`, `content_list.json`, and supplementary parsed source `mineru-parsed/Sun_2023_Nature Biotechnology`.

## Method list

### Population sRNA-seq and mRNA-seq

- Method name: sRNAome and transcriptome profiling under WW/DS
- Purpose: 构建 maize drought response 的 small RNA and mRNA expression landscape。
- Input material/data: 338 maize accessions for sRNAome; 197 accessions for transcriptome; WW and DS conditions.
- Output: drought-responsive s-traits, sc-traits, gene expression traits.
- Key parameters: exact library filters in supplementary source; 676 sRNA-seq libraries and 394 mRNA-seq libraries reported in supplementary parsed text.
- Strengths: population-scale expression resource.
- Limitations: batch/environment details require manual PDF check.
- Used in which result: Findings 1-2.

### eGWAS and eQTL hotspot identification

- Method name: expression GWAS for sRNA and mRNA traits
- Purpose: 定位控制 sRNA/mRNA expression variation 的 genetic loci。
- Input material/data: SNP/PAV genotypes; sRNA and mRNA expression traits.
- Output: seQTLs, meQTLs, sm-eQTLs, seQTL hotspots including DRESH8.
- Key parameters: Bonferroni-adjusted thresholds reported in text for s-traits and sc-traits.
- Strengths: links regulatory expression traits to genetic variants.
- Limitations: association results require functional validation.
- Used in which result: Findings 2-3.

### DRESH8 structural and population-genetic analysis

- Method name: PAV, LD, TE-IR and selection analyses
- Purpose: 解析 DRESH8 结构变异、TE inverted repeat 来源和驯化选择信号。
- Input material/data: DRESH8 locus sequences from teosinte, landraces, modern maize.
- Output: PAV status, LD with significant SNPs, nucleotide diversity, Fst/XP-CLR signals, allele frequency map.
- Key parameters: DRESH8 ~21.4 kb; Gypsy TE arms ~8 kb each.
- Strengths: connects molecular structure to domestication/spread.
- Limitations: historical inference cannot be experimentally replayed.
- Used in which result: Findings 3 and 6.

### CRISPR-Cas9 deletion of DRESH8

- Method name: Genome editing deletion mutant
- Purpose: 测试 DRESH8 对 sRNA expression and drought tolerance 的因果作用。
- Input material/data: maize B104; dDRESH8 edited lines.
- Output: DRESH8-derived sRNA reduction; drought survival phenotype.
- Key parameters: dDRESH8 survival 34.62% +/- 12.66%; B104 survival 16.67% +/- 10.76% reported.
- Strengths: strong locus-level causal evidence.
- Limitations: edited-line background and field robustness require further validation.
- Used in which result: Finding 4.

### mRNA cleavage assay

- Method name: DRESH8-derived siRNA target cleavage validation
- Purpose: 识别 DRESH8-derived siRNAs 的 downstream mRNA targets。
- Input material/data: predicted targets including ZmMYBR38.
- Output: cleavage evidence for target transcripts.
- Key parameters: not fully expanded in provided text.
- Strengths: supports post-transcriptional regulatory mechanism.
- Limitations: exact assay format and clone counts need manual PDF check.
- Used in which result: Finding 5.

### Transgenic overexpression of ZmMYBR38

- Method name: ZmMYBR38 overexpression in maize and Arabidopsis
- Purpose: 测试 ZmMYBR38 对 drought tolerance 的功能。
- Input material/data: transgenic maize and Arabidopsis plants overexpressing ZmMYBR38.
- Output: drought tolerance phenotype relative to wild-type controls.
- Key parameters: Extended Data notes multiple replicates for Arabidopsis; exact maize sample sizes need manual check.
- Strengths: cross-species functional support.
- Limitations: overexpression may not reflect endogenous regulation level.
- Used in which result: Finding 5.

### Genome-wide TE-IR tradeoff scan

- Method name: IR-associated trait and selection scan
- Purpose: 评估 TE-IR loci 是否广泛关联 drought response and yield-related traits。
- Input material/data: genome-wide IR annotations, SNPs near IRs, kernel length/survival/yield-associated genes.
- Output: IR-linked opposite effects on survival and kernel length; enrichment of yield-related genes.
- Key parameters: Extended Data Fig. 8 reports most IR-adjacent SNPs associated with both traits had opposite effects.
- Strengths: expands DRESH8 from case study to genome-wide hypothesis.
- Limitations: most loci remain statistical associations.
- Used in which result: Finding 7.
