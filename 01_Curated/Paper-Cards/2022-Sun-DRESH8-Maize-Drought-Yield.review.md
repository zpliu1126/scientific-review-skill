---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: The role of transposon inverted repeats in balancing drought tolerance and yield-related traits in maize
authors: Xiaopeng Sun; Yanli Xiang; Nannan Dou; Hui Zhang; Surui Pei; Arcadio Valdes Franco; Mitra Menon; Brandon Monier; Taylor Ferebee; Tao Liu; Sanyang Liu; Yuchi Gao; Jubin Wang; William Terzaghi; Jianbing Yan; Sarah Hearne; Lin Li; Feng Li; Mingqiu Dai
year: 2022
journal: Nature Biotechnology
doi: unknown
study_type: primary research; population multi-omics; functional genomics
field: maize stress biology; small RNA regulation; crop domestication
topics: [maize, drought tolerance, yield traits, TE-IR, DRESH8, siRNA, ZmMYBR38, eQTL]
source_basis: full.md + content_list.json
evidence_strength: high for DRESH8 functional validation; moderate-high for genome-wide TE-IR selection model
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Sun_2023_Nature Biotechnology_2
created: 2026-06-07
updated: 2026-06-07
---

# The role of transposon inverted repeats in balancing drought tolerance and yield-related traits in maize

## 1. Citation metadata

- Title: The role of transposon inverted repeats in balancing drought tolerance and yield-related traits in maize
- Authors: Xiaopeng Sun; Yanli Xiang; Nannan Dou; Hui Zhang; Surui Pei; Arcadio Valdes Franco; Mitra Menon; Brandon Monier; Taylor Ferebee; Tao Liu; Sanyang Liu; Yuchi Gao; Jubin Wang; William Terzaghi; Jianbing Yan; Sarah Hearne; Lin Li; Feng Li; Mingqiu Dai
- Year: 2022
- Journal: Nature Biotechnology
- DOI: unknown
- Article type: primary research

## 2. Source basis

本凝练基于 MinerU 解析目录 `mineru-parsed/Sun_2023_Nature Biotechnology_2`。同名目录 `mineru-parsed/Sun_2023_Nature Biotechnology` 更像 supplementary results/source，作为补充来源记录在索引备注中。Parser note: figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

本文通过 maize 多样性群体的 sRNAome/transcriptome eQTL、CRISPR 删除、转基因和演化扫描，提出 TE inverted repeat 产生的 siRNA 网络可在 drought tolerance 与 yield-related traits 之间形成遗传权衡。

## 4. Research question

本文试图回答：maize 中小 RNA 表达变异的遗传基础是什么，TE-derived inverted repeats 是否能通过 siRNA 调控网络影响干旱适应与产量性状的权衡，并在驯化中受到选择。

## 5. Study design

研究包括 338 个 maize inbred accessions 的 sRNAome profiling、197 个 accessions 的 transcriptome profiling，在 well-watered (WW) 和 drought-stressed (DS) 条件下比较表达。作者进一步进行 sRNA/mRNA eGWAS、coexpression network、DRESH8 locus cloning、PAV/LD/selection analyses、F2 drought assays、CRISPR-Cas9 deletion mutant、mRNA cleavage assays、ZmMYBR38 overexpression in maize and Arabidopsis，以及 genome-wide TE-IR/yield/stress association scans。

## 6. Key methods

- sRNA-seq and mRNA-seq under WW/DS conditions.
- eGWAS for sRNA traits, sRNA cluster traits and mRNA expression traits.
- seQTL/meQTL/sm-eQTL hotspot identification.
- DRESH8 PAV genotyping, LD analysis and selection scans.
- CRISPR-Cas9 DRESH8 deletion in B104.
- Drought survival assays in GWAS panel, F2 populations and edited lines.
- mRNA cleavage assays for DRESH8-derived siRNA targets.
- ZmMYBR38 overexpression in maize and Arabidopsis.
- Genome-wide TE-IR association with drought response, kernel length and yield-related genes.

## 7. Main findings with anchors

### Finding 1

- Source-reported content: Dataset comprised 338 sRNAomes and 197 transcriptomes; authors detected 12,476 drought-responsive sRNA traits and 21,757 drought-responsive sRNA cluster traits, plus 6,158 significant sRNA-gene coexpression pairs.
- Figure/table/section anchor if available: Results, "Expression variation and genetic control of sRNAs in maize drought response"; Fig. 1; Extended Data Fig. 1-2.
- Evidence type: population sRNA-seq/mRNA-seq.
- Limitation: coexpression does not prove regulatory causality.
- Confidence level: high.

### Finding 2

- Source-reported content: eGWAS identified seQTLs, seQTL hotspots and 4,722 sm-eQTLs; 56.1% of meQTL-regulated genes were controlled by sm-eQTLs, including genes involved in ABA signaling, osmotic stress, water deprivation and abiotic stress responses.
- Figure/table/section anchor if available: Fig. 1c-e; Supplementary Tables 9-15.
- Evidence type: expression GWAS and network integration.
- Limitation: population structure/statistical model details need manual PDF check.
- Confidence level: moderate-high.

### Finding 3

- Source-reported content: DRESH8 is a DS-specific super eQTL hotspot on chromosome 8; the most significant marker is a ~21.4-kb PAV in the third intron of ZmPP2C16, containing Gypsy TE arms forming an inverted repeat and associated with hundreds of drought-responsive sRNA traits.
- Figure/table/section anchor if available: Results, "Role and mechanism of DRESH8 in maize drought tolerance"; Fig. 2a-d; Extended Data Fig. 3.
- Evidence type: eQTL fine mapping, PAV/TE-IR structural analysis.
- Limitation: authors phrase initial causality as "might be causative" before validation.
- Confidence level: high after functional validation.

### Finding 4

- Source-reported content: Genotypes lacking DRESH8 showed higher drought survival; F2 populations supported this; CRISPR dDRESH8 B104 lines had higher survival rates (34.62% +/- 12.66%) than wild-type B104 (16.67% +/- 10.76%) after drought stress, and DRESH8-derived sRNAs were reduced in dDRESH8.
- Figure/table/section anchor if available: Fig. 2e-l.
- Evidence type: population association, segregating population, CRISPR deletion, sRNA-seq.
- Limitation: survival phenotype context and environmental replication require manual check.
- Confidence level: high.

### Finding 5

- Source-reported content: mRNA cleavage assays identified targets of DRESH8-derived sRNAs, including ZmMYBR38; overexpression of ZmMYBR38 in maize and Arabidopsis increased drought tolerance relative to wild type.
- Figure/table/section anchor if available: Fig. 2m-q; Extended Data Fig. 3g-i.
- Evidence type: target cleavage assay and transgenic functional validation.
- Limitation: not all DRESH8-derived targets have equivalent validation.
- Confidence level: high for ZmMYBR38.

### Finding 6

- Source-reported content: DRESH8 showed selection signals during maize domestication/spread; DRESH8 was not detected in tested teosinte accessions but was found in landraces and modern maize, with frequency patterns suggesting origin/spread from southern Mexico.
- Figure/table/section anchor if available: Fig. 3; Extended Data Fig. 4.
- Evidence type: population genetics and allele distribution.
- Limitation: historical selection interpretation is inferential.
- Confidence level: moderate-high.

### Finding 7

- Source-reported content: DRESH8 presence was associated with longer kernels under WW conditions, while DRESH8 absence favored drought survival; genome-wide TE-IR scans suggested many IR-linked loci show opposite effects on kernel length and survival rate.
- Figure/table/section anchor if available: DRESH8 yield/drought section; Extended Data Fig. 5-8.
- Evidence type: association plus edited-line phenotype and genome-wide scan.
- Limitation: yield trait effects need field/environment validation before breeding application.
- Confidence level: moderate-high.

## 8. Author conclusions

作者结论是：TE-IR-derived sRNA/gene regulatory networks are key molecular mechanisms underlying the tradeoff between crop environmental adaptation and yield-related traits。DRESH8-derived siRNAs cleave target mRNAs such as ZmMYBR38, thereby affecting drought tolerance, while TE-IR loci have undergone selection and expansion during maize domestication.

## 9. Reasonable inference

- DRESH8 absence may be useful for improving drought tolerance, but could carry yield-related tradeoffs depending on environment.
- TE-IR loci could indicate a broader class of small-RNA regulatory variants for crop improvement.
- The DRESH8-ZmMYBR38 result may suggest that TE insertions can become regulatory hubs rather than merely passive genome repeats.

## 10. Model synthesis

这篇文章的核心模型是：TE-derived inverted repeat 在特定环境下产生 sRNAs，这些 sRNAs 通过转录后切割或抑制目标基因，改变 stress tolerance 和 yield-related traits。DRESH8 是其中经过强验证的案例：presence 产生 DRESH8-derived siRNAs，靶向包括 ZmMYBR38 在内的 drought-positive regulators；deletion 减少这些 sRNAs 并提高 drought survival，但可能影响 kernel/yield traits。

## 11. Limitations and missing controls

- DOI not confirmed in provided MinerU text; recorded as unknown.
- `Sun_2023_Nature Biotechnology` appears to be supplementary material and should be manually matched to the main PDF.
- Many genome-wide TE-IR associations are statistical and require locus-by-locus functional validation.
- Breeding implications require multi-environment yield and drought trials.
- Figure/table anchor uncertain due MinerU structure; needs manual PDF check.

## 12. Reusable knowledge

- Concepts: TE inverted repeat; sRNA eQTL; sm-eQTL; drought-responsive sRNA; PAV; crop tradeoff; domestication selection.
- Methods: population sRNAome/transcriptome; eGWAS; CRISPR deletion; mRNA cleavage assay; transgenic overexpression; selection scan; TE-IR genome-wide association.
- Datasets: 338 maize sRNAomes; 197 maize transcriptomes; supplementary source in `mineru-parsed/Sun_2023_Nature Biotechnology`.
- Experimental designs: combine association genetics with edited-line validation to move from correlation to causality.
- Analytical frameworks: use environment-specific eQTL hotspots to nominate stress-regulatory sRNA loci.

## 13. Open questions

- DRESH8-derived siRNAs除了 ZmMYBR38 外，哪些 targets 对 yield-related traits 贡献最大？
- DRESH8 deletion 在多环境田间试验中是否能兼顾 drought tolerance 和 stable yield？
- TE-IR expansion during domestication 是主动选择结果还是 linked selection 的副产物？
- 其他作物中是否存在类似 TE-IR-derived sRNA tradeoff loci？
