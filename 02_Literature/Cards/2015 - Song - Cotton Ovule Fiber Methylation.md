---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: Dynamic Roles for Small RNAs and DNA Methylation during Ovule and Fiber Development in Allotetraploid Cotton
authors: Qingxin Song; Xueying Guan; Z. Jeffrey Chen
year: 2015
journal: PLOS Genetics
doi: 10.1371/journal.pgen.1005724
field: cotton fiber development; plant epigenomics; small RNA biology
topics: 
  - cotton
  - fiber development
  - ovule
  - CHH methylation
  - RdDM
  - CMT2
  - small RNA
  - homoeolog expression bias
study_type: primary research; multi-omics developmental epigenomics
methods: 
  - Plant material and developmental sampling
  - Cotton tissue sampling
  - MethylC-seq / whole-genome bisulfite sequencing
  - MethylC-seq library construction and methylcytosine calling
  - CHH DMR identification
  - 100-bp sliding-window CHH DMR calling
  - Bisulfite validation of selected DMRs
  - cloned-fragment bisulfite sequencing validation
  - small RNA-seq
  - small RNA sequencing and abundance analysis
  - RNA-seq and gene/TE expression analysis
  - mRNA-seq differential expression
  - Homoeolog identification and methylation-expression comparison
  - A/D homoeolog identification and bias analysis
  - qRT-PCR of methylation pathway genes
  - qRT-PCR expression profiling
  - In vitro ovule culture and 5-aza-dC treatment
  - DNA methylation inhibitor perturbation
  - MethylC-seq
  - bisulfite sequencing
  - sRNA-seq
  - genomic distribution analysis
  - 100-bp sliding-window DMR calling
  - cloned-fragment bisulfite validation
  - RNA-seq
  - enrichment analysis
  - TE annotation
  - qRT-PCR
  - in vitro ovule culture
  - 5-aza-dC treatment
  - SEM/phenotyping
  - blastp
  - MCScanX
  - expression-bias analysis
data_types: 
  - CHH DMRs; siRNA density; gene/TE density
  - CHH methylation regions
  - TE expression; CHH DMRs
  - fiber number/length; ovule size
  - gene expression; CHH DMRs; siRNA abundance
  - gene-body methylation; homoeolog expression
  - methylation pathway gene expression
  - small RNA size distribution
  - whole-genome methylation
study_system: 
  - Gossypium hirsutum TM-1
  - Gossypium hirsutum TM-1 cultured ovules
  - "Gossypium hirsutum TM-1 leaves, ovules, fibers"
evidence_strength: moderate-high; genome-wide multi-omics plus methylation inhibitor perturbation
confidence_level: high; moderate-high; moderate
paper_id: 2015-Song-Cotton-Ovule-Fiber-Methylation
mineru_dir: mineru-parsed/Song_2015_PLOS Genetics
curated_card: 01_Curated/Paper-Cards/2015-Song-Cotton-Ovule-Fiber-Methylation.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2015-Song-Cotton-Ovule-Fiber-Methylation.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# Dynamic Roles for Small RNAs and DNA Methylation during Ovule and Fiber Development in Allotetraploid Cotton

> [!summary] 一句话结论
> 本文在异源四倍体棉花中显示 ovule 和 fiber 具有不同 CHH methylation 模式：ovule 近基因 CHH 与 24-nt siRNA/RdDM 和基因激活相关，fiber 异染色质 CHH 与 TE 抑制、CMT2/H1 状态和纤维发育相关。

## 基本信息
- Authors: Qingxin Song; Xueying Guan; Z. Jeffrey Chen
- Year: 2015
- Journal: PLOS Genetics
- DOI: 10.1371/journal.pgen.1005724
- Study type: primary research; multi-omics developmental epigenomics
- Source basis: 01_Curated/Paper-Cards/2015-Song-Cotton-Ovule-Fiber-Methylation.review.md; 01_Curated/Claim-Evidence/2015-Song-Cotton-Ovule-Fiber-Methylation.claims.tsv; 01_Curated/Method-Summaries/method-summary.2015-Song-Cotton-Ovule-Fiber-Methylation.md

## 核心科学问题
本文试图回答：DNA methylation、small RNAs 和 homoeolog expression bias 如何参与棉花 ovule epidermal cell 到 rapidly elongating fiber cell 的发育转变。

## 研究设计
研究材料为 allotetraploid cotton `Gossypium hirsutum L. acc. TM-1`。作者对 leaves、0 DPA ovules、14 DPA fibers，以及 14 DPA ovules 进行 MethylC-seq；对 leaves、0 DPA ovules、14 DPA fibers 进行 small RNA-seq；并结合 RNA-seq 分析 gene/TE expression。功能扰动部分使用 in vitro cultured ovules，加入 DNA methyltransferase inhibitor 5-aza-2'-deoxycytidine (5-aza-dC) 观察 fiber initiation/elongation。

## 主要发现

### Finding 1
> [!info] Source-reported content
> The paper reports CHH methylation levels much higher in fibers (~14%) than ovules (~8.1%) and leaves (~7.8%), while CG and CHG levels were similar among tissues

- Evidence type: methylome evidence
- Method: MethylC-seq; bisulfite sequencing
- Data type: whole-genome methylation
- Figure/table anchor: Fig. 1A; S1 Table
- Confidence: high
- Limitation: 14 DPA ovule has one replicate in provided text

### Finding 2
> [!info] Source-reported content
> The paper reports small RNA-seq data with three replicates showing 24-nt siRNAs were much higher in fibers and ovules than leaves

- Evidence type: small RNA evidence
- Method: small RNA-seq
- Data type: small RNA size distribution
- Figure/table anchor: Fig. 1B
- Confidence: high
- Limitation: does not alone prove siRNAs cause all CHH methylation changes

### Finding 3
> [!info] Source-reported content
> OL CHH hypermethylation correlated with gene-rich/euchromatic regions and siRNAs; FO CHH hypermethylation was enriched in TE- and repeat-rich heterochromatic regions

- Evidence type: methylome/genome annotation evidence
- Method: MethylC-seq; sRNA-seq; genomic distribution analysis
- Data type: CHH DMRs; siRNA density; gene/TE density
- Figure/table anchor: Fig. 1C-G; Fig. 2
- Confidence: high for distribution; moderate for pathway inference
- Limitation: genomic correlation does not prove enzyme causality

### Finding 4
> [!info] Source-reported content
> 39,668 OL CHH-hyper DMRs and 124,681 FO CHH-hyper DMRs were identified; a subset was validated by bisulfite sequencing of cloned genomic fragments

- Evidence type: DMR evidence
- Method: 100-bp sliding-window DMR calling; cloned-fragment bisulfite validation
- Data type: CHH methylation regions
- Figure/table anchor: Fig. 2; S2 Table; S3 Fig
- Confidence: high
- Limitation: validation subset details require manual PDF check

### Finding 5
> [!info] Source-reported content
> Up-regulated genes in ovule were enriched among genes overlapping OL CHH-hyper DMRs in upstream 1-kb sequences; ovule-preferred gene promoters had higher siRNA levels in ovules than leaves

- Evidence type: methylome/transcriptome/sRNA integration
- Method: MethylC-seq; RNA-seq; sRNA-seq; enrichment analysis
- Data type: gene expression; CHH DMRs; siRNA abundance
- Figure/table anchor: Fig. 3
- Confidence: moderate-high
- Limitation: directionality between methylation and expression remains unresolved

### Finding 6
> [!info] Source-reported content
> FO CHH-hyper DMRs were enriched in TEs and correlated with TE density; more TEs were expressed in fibers than ovules or leaves; authors suggest CHH hypermethylation in fibers may serve as feedback to repress TEs

- Evidence type: methylome/RNA-seq integration
- Method: MethylC-seq; RNA-seq; TE annotation
- Data type: TE expression; CHH DMRs
- Figure/table anchor: Fig. 4C-E; S1D Fig
- Confidence: moderate-high for association; moderate for feedback model
- Limitation: time order and direct repression are not established

## 作者结论
作者明确提出：ovule 中 promoter/flanking CHH hypermethylation 与 siRNAs/RdDM 和 ovule-preferred gene activation 相关；fiber 中额外 heterochromatic CHH hypermethylation 可能通过 CMT2/DDM1/H1 相关机制抑制 TEs 和 nearby genes；DNA methylation 还影响 homoeolog expression bias 和 fiber development。作者将这些过程概括为调控 gene and TE expression 的 double-lock feedback mechanism。

## 谨慎推断
> [!caution] Reasonable inference
> - The contrast between OL and FO CHH DMRs may suggest that the same methylation context can serve different developmental roles depending on genomic location.
> - The 5-aza-dC phenotype is consistent with DNA methylation being required for normal cotton fiber initiation/elongation, but it does not identify which methylation pathway is causal.
> - The anti-correlation between CHG/CHH gene-body methylation and homoeolog expression could indicate an epigenetic layer contributing to subgenome expression bias.

## 模型综合
> [!abstract] Model synthesis
> 本文可被整合为“发育阶段分区 CHH methylation 模型”：在 ovule 阶段，近基因短 TE/启动子区域的 24-nt siRNA 和 CHH methylation 与活跃基因表达相伴；进入 fiber elongation 后，异染色质/TE 区域出现额外 CHH methylation，可能作为 TE 活化后的反馈沉默机制，同时影响附近基因和部分 homoeolog expression bias。

## 可复用知识

### Concepts
- [[CHH methylation]]
- [[RdDM-dependent promoter methylation]]
- [[CMT2/DDM1-related heterochromatic methylation]]
- [[CHH methylation island]]
- [[homoeolog expression bias]]
- [[TE feedback silencing]]

### Methods
- [[Plant material and developmental sampling]]
- [[Cotton tissue sampling]]
- [[MethylC-seq / whole-genome bisulfite sequencing]]
- [[MethylC-seq library construction and methylcytosine calling]]
- [[CHH DMR identification]]
- [[100-bp sliding-window CHH DMR calling]]
- [[Bisulfite validation of selected DMRs]]
- [[cloned-fragment bisulfite sequencing validation]]
- [[small RNA-seq]]
- [[small RNA sequencing and abundance analysis]]
- [[RNA-seq and gene/TE expression analysis]]
- [[mRNA-seq differential expression]]

### Datasets
- GEO accession GSE61774

### Analytical frameworks
- integrate methylation context
- genomic compartment
- siRNA density
- TE proximity and gene expression

### Experimental designs
- compare leaf -> ovule and ovule -> fiber transitions separately to distinguish organogenesis and cell elongation effects

## 局限性
- 5-aza-dC 是广谱 DNA methylation inhibitor，作者也说明不能排除 growth inhibition side effects。
- GhCMT2/H1 机制主要由表达模式和已知通路推断，缺少 cotton CMT2/H1 loss-of-function 或 rescue 证据。
- DMR 与 gene/TE expression 多为相关性，不能全部解释为直接因果。
- Figure/table anchor uncertain；MinerU 输出没有独立 `images/`/`tables/` 目录。
- 14 DPA ovule replicate 信息在 provided text 中显示为 one replicate，需要 manual PDF check。

## 开放问题
- GhCMT2、GhDDM1 或 HISTONE H1 的遗传扰动是否能直接重现或解除 fiber CHH hypermethylation？
- ovule promoter CHH methylation 是由 gene expression 引发，还是促进 gene activation？
- fiber 中 TE transcription 和 CHH hypermethylation 的时间先后关系是什么？
- 哪些具体 fiber-related genes 受邻近 DMRs 直接调控？
- homoeolog gene-body CHG/CHH methylation 是否可被选择并稳定影响 cotton fiber traits？

## 关联笔记
- Concepts: [[CHH methylation]], [[RdDM-dependent promoter methylation]], [[CMT2/DDM1-related heterochromatic methylation]], [[CHH methylation island]], [[homoeolog expression bias]], [[TE feedback silencing]]
- Methods: [[Plant material and developmental sampling]], [[Cotton tissue sampling]], [[MethylC-seq / whole-genome bisulfite sequencing]], [[MethylC-seq library construction and methylcytosine calling]], [[CHH DMR identification]], [[100-bp sliding-window CHH DMR calling]], [[Bisulfite validation of selected DMRs]], [[cloned-fragment bisulfite sequencing validation]], [[small RNA-seq]], [[small RNA sequencing and abundance analysis]], [[RNA-seq and gene/TE expression analysis]], [[mRNA-seq differential expression]]
- Evidence: [[2015-Song-Cotton-Ovule-Fiber-Methylation claims]]
- Questions: [[2015-Song-Cotton-Ovule-Fiber-Methylation open questions]]
