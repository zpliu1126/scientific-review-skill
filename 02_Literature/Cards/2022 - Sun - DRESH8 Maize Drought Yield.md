---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: The role of transposon inverted repeats in balancing drought tolerance and yield-related traits in maize
authors: Xiaopeng Sun; Yanli Xiang; Nannan Dou; Hui Zhang; Surui Pei; Arcadio Valdes Franco; Mitra Menon; Brandon Monier; Taylor Ferebee; Tao Liu; Sanyang Liu; Yuchi Gao; Jubin Wang; William Terzaghi; Jianbing Yan; Sarah Hearne; Lin Li; Feng Li; Mingqiu Dai
year: 2022
journal: Nature Biotechnology
doi: unknown
field: maize stress biology; small RNA regulation; crop domestication
topics: 
  - maize
  - drought tolerance
  - yield traits
  - TE-IR
  - DRESH8
  - siRNA
  - ZmMYBR38
  - eQTL
study_type: primary research; population multi-omics; functional genomics
methods: 
  - Population sRNA-seq and mRNA-seq
  - sRNAome and transcriptome profiling under WW/DS
  - eGWAS and eQTL hotspot identification
  - expression GWAS for sRNA and mRNA traits
  - DRESH8 structural and population-genetic analysis
  - "PAV, LD, TE-IR and selection analyses"
  - CRISPR-Cas9 deletion of DRESH8
  - Genome editing deletion mutant
  - mRNA cleavage assay
  - DRESH8-derived siRNA target cleavage validation
  - Transgenic overexpression of ZmMYBR38
  - ZmMYBR38 overexpression in maize and Arabidopsis
  - Genome-wide TE-IR tradeoff scan
  - IR-associated trait and selection scan
  - sRNA-seq
  - mRNA-seq
  - regression
  - GO/KEGG enrichment
  - eGWAS
  - PAV analysis
  - LD analysis
  - TE annotation
  - CRISPR-Cas9 deletion
  - drought survival assay
  - transgenic overexpression
  - drought assay
  - nucleotide diversity
  - Fst
  - XP-CLR
  - allele frequency analysis
  - genome-wide TE-IR scan
  - trait association
  - edited-line phenotyping
data_types: 
  - cleavage products; transgene expression; survival/phenotype
  - kernel length; survival rate; IR-linked variants
  - population genotype data
  - sRNA and mRNA expression
  - sRNA expression; mRNA expression
  - sRNA traits; genotype variants
  - survival rate; sRNA expression
study_system: 
  - maize
  - maize B104 and dDRESH8 lines
  - maize and Arabidopsis
  - maize diversity panel
  - maize diversity panel under WW and DS
  - "teosinte, landraces, modern maize"
evidence_strength: high for DRESH8 functional validation; moderate-high for genome-wide TE-IR selection model
confidence_level: high; moderate-high; moderate
paper_id: 2022-Sun-DRESH8-Maize-Drought-Yield
mineru_dir: mineru-parsed/Sun_2023_Nature Biotechnology_2
curated_card: 01_Curated/Paper-Cards/2022-Sun-DRESH8-Maize-Drought-Yield.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2022-Sun-DRESH8-Maize-Drought-Yield.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# The role of transposon inverted repeats in balancing drought tolerance and yield-related traits in maize

> [!summary] 一句话结论
> 本文通过 maize 多样性群体的 sRNAome/transcriptome eQTL、CRISPR 删除、转基因和演化扫描，提出 TE inverted repeat 产生的 siRNA 网络可在 drought tolerance 与 yield-related traits 之间形成遗传权衡。

## 基本信息
- Authors: Xiaopeng Sun; Yanli Xiang; Nannan Dou; Hui Zhang; Surui Pei; Arcadio Valdes Franco; Mitra Menon; Brandon Monier; Taylor Ferebee; Tao Liu; Sanyang Liu; Yuchi Gao; Jubin Wang; William Terzaghi; Jianbing Yan; Sarah Hearne; Lin Li; Feng Li; Mingqiu Dai
- Year: 2022
- Journal: Nature Biotechnology
- DOI: unknown
- Study type: primary research; population multi-omics; functional genomics
- Source basis: 01_Curated/Paper-Cards/2022-Sun-DRESH8-Maize-Drought-Yield.review.md; 01_Curated/Claim-Evidence/2022-Sun-DRESH8-Maize-Drought-Yield.claims.tsv; 01_Curated/Method-Summaries/method-summary.2022-Sun-DRESH8-Maize-Drought-Yield.md

## 核心科学问题
本文试图回答：maize 中小 RNA 表达变异的遗传基础是什么，TE-derived inverted repeats 是否能通过 siRNA 调控网络影响干旱适应与产量性状的权衡，并在驯化中受到选择。

## 研究设计
研究包括 338 个 maize inbred accessions 的 sRNAome profiling、197 个 accessions 的 transcriptome profiling，在 well-watered (WW) 和 drought-stressed (DS) 条件下比较表达。作者进一步进行 sRNA/mRNA eGWAS、coexpression network、DRESH8 locus cloning、PAV/LD/selection analyses、F2 drought assays、CRISPR-Cas9 deletion mutant、mRNA cleavage assays、ZmMYBR38 overexpression in maize and Arabidopsis，以及 genome-wide TE-IR/yield/stress association scans。

## 主要发现

### Finding 1
> [!info] Source-reported content
> The dataset comprises 338 sRNAomes and 197 transcriptomes; 12,476 drought-responsive sRNA traits and 21,757 drought-responsive sRNA cluster traits were detected

- Evidence type: population multi-omics
- Method: sRNA-seq; mRNA-seq
- Data type: sRNA and mRNA expression
- Figure/table anchor: Fig. 1; Extended Data Fig. 1
- Confidence: high
- Limitation: sample handling details require methods check

### Finding 2
> [!info] Source-reported content
> Population-level regression uncovered 6,158 significant sRNA-gene coexpression pairs; 1,317 pairs showed negative coexpression; enriched genes included stress/stimulus GO terms and metabolic pathways

- Evidence type: coexpression evidence
- Method: regression; GO/KEGG enrichment
- Data type: sRNA expression; mRNA expression
- Figure/table anchor: Fig. 1; Extended Data Fig. 2
- Confidence: moderate-high
- Limitation: coexpression and target prediction do not prove regulation

### Finding 3
> [!info] Source-reported content
> DRESH8 on chromosome 8 was detected only under DS; a ~21.4-kb PAV in ZmPP2C16 intron contained Gypsy TE inverted-repeat arms and was associated with 542 drought-responsive sc-traits and 283 s-traits

- Evidence type: eQTL and structural variant evidence
- Method: eGWAS; PAV analysis; LD analysis; TE annotation
- Data type: sRNA traits; genotype variants
- Figure/table anchor: Fig. 2a-d; Extended Data Fig. 3
- Confidence: high
- Limitation: supplementary methods needed for full eQTL thresholds

### Finding 4
> [!info] Source-reported content
> B104 dDRESH8 CRISPR deletion lines had higher survival rates after drought stress than wild-type B104, and DRESH8-derived sRNAs were reduced in dDRESH8

- Evidence type: functional genetics
- Method: CRISPR-Cas9 deletion; drought survival assay; sRNA-seq
- Data type: survival rate; sRNA expression
- Figure/table anchor: Fig. 2i-l
- Confidence: high
- Limitation: environmental conditions and replicate details require manual PDF check

### Finding 5
> [!info] Source-reported content
> mRNA cleavage assays identified ZmMYBR38 as a target of DRESH8-derived sRNAs; ZmMYBR38 overexpression in maize and Arabidopsis increased drought tolerance

- Evidence type: target validation and transgenic evidence
- Method: mRNA cleavage assay; transgenic overexpression; drought assay
- Data type: cleavage products; transgene expression; survival/phenotype
- Figure/table anchor: Fig. 2m-q; Extended Data Fig. 3
- Confidence: high
- Limitation: other DRESH8 targets are less deeply validated

### Finding 6
> [!info] Source-reported content
> The paper reports lower nucleotide diversity around DRESH8 in maize than teosinte, Fst/XP-CLR selection signals, no DRESH8 in tested teosinte, and increasing frequency in landraces/modern maize

- Evidence type: population genetics evidence
- Method: nucleotide diversity; Fst; XP-CLR; allele frequency analysis
- Data type: population genotype data
- Figure/table anchor: Fig. 3; Extended Data Fig. 4
- Confidence: moderate-high
- Limitation: selection history is inferential

## 作者结论
作者结论是：TE-IR-derived sRNA/gene regulatory networks are key molecular mechanisms underlying the tradeoff between crop environmental adaptation and yield-related traits。DRESH8-derived siRNAs cleave target mRNAs such as ZmMYBR38, thereby affecting drought tolerance, while TE-IR loci have undergone selection and expansion during maize domestication.

## 谨慎推断
> [!caution] Reasonable inference
> - DRESH8 absence may be useful for improving drought tolerance, but could carry yield-related tradeoffs depending on environment.
> - TE-IR loci could indicate a broader class of small-RNA regulatory variants for crop improvement.
> - The DRESH8-ZmMYBR38 result may suggest that TE insertions can become regulatory hubs rather than merely passive genome repeats.

## 模型综合
> [!abstract] Model synthesis
> 这篇文章的核心模型是：TE-derived inverted repeat 在特定环境下产生 sRNAs，这些 sRNAs 通过转录后切割或抑制目标基因，改变 stress tolerance 和 yield-related traits。DRESH8 是其中经过强验证的案例：presence 产生 DRESH8-derived siRNAs，靶向包括 ZmMYBR38 在内的 drought-positive regulators；deletion 减少这些 sRNAs 并提高 drought survival，但可能影响 kernel/yield traits。

## 可复用知识

### Concepts
- [[TE inverted repeat]]
- [[sRNA eQTL]]
- [[sm-eQTL]]
- [[drought-responsive sRNA]]
- [[PAV]]
- [[crop tradeoff]]
- [[domestication selection]]

### Methods
- [[Population sRNA-seq and mRNA-seq]]
- [[sRNAome and transcriptome profiling under WW/DS]]
- [[eGWAS and eQTL hotspot identification]]
- [[expression GWAS for sRNA and mRNA traits]]
- [[DRESH8 structural and population-genetic analysis]]
- [[PAV, LD, TE-IR and selection analyses]]
- [[CRISPR-Cas9 deletion of DRESH8]]
- [[Genome editing deletion mutant]]
- [[mRNA cleavage assay]]
- [[DRESH8-derived siRNA target cleavage validation]]
- [[Transgenic overexpression of ZmMYBR38]]
- [[ZmMYBR38 overexpression in maize and Arabidopsis]]

### Datasets
- 338 maize sRNAomes
- 197 maize transcriptomes
- supplementary source in `mineru-parsed/Sun_2023_Nature Biotechnology`

### Analytical frameworks
- use environment-specific eQTL hotspots to nominate stress-regulatory sRNA loci

### Experimental designs
- combine association genetics with edited-line validation to move from correlation to causality

## 局限性
- DOI not confirmed in provided MinerU text; recorded as unknown.
- `Sun_2023_Nature Biotechnology` appears to be supplementary material and should be manually matched to the main PDF.
- Many genome-wide TE-IR associations are statistical and require locus-by-locus functional validation.
- Breeding implications require multi-environment yield and drought trials.
- Figure/table anchor uncertain due MinerU structure; needs manual PDF check.

## 开放问题
- DRESH8-derived siRNAs除了 ZmMYBR38 外，哪些 targets 对 yield-related traits 贡献最大？
- DRESH8 deletion 在多环境田间试验中是否能兼顾 drought tolerance 和 stable yield？
- TE-IR expansion during domestication 是主动选择结果还是 linked selection 的副产物？
- 其他作物中是否存在类似 TE-IR-derived sRNA tradeoff loci？

## 关联笔记
- Concepts: [[TE inverted repeat]], [[sRNA eQTL]], [[sm-eQTL]], [[drought-responsive sRNA]], [[PAV]], [[crop tradeoff]], [[domestication selection]]
- Methods: [[Population sRNA-seq and mRNA-seq]], [[sRNAome and transcriptome profiling under WW/DS]], [[eGWAS and eQTL hotspot identification]], [[expression GWAS for sRNA and mRNA traits]], [[DRESH8 structural and population-genetic analysis]], [[PAV, LD, TE-IR and selection analyses]], [[CRISPR-Cas9 deletion of DRESH8]], [[Genome editing deletion mutant]], [[mRNA cleavage assay]], [[DRESH8-derived siRNA target cleavage validation]], [[Transgenic overexpression of ZmMYBR38]], [[ZmMYBR38 overexpression in maize and Arabidopsis]]
- Evidence: [[2022-Sun-DRESH8-Maize-Drought-Yield claims]]
- Questions: [[2022-Sun-DRESH8-Maize-Drought-Yield open questions]]
