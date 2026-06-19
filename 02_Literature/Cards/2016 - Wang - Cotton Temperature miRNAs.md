---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: Small RNA-mediated responses to low- and high-temperature stresses in cotton
authors: Qiongshan Wang; Nian Liu; Xiyan Yang; Lili Tu; Xianlong Zhang
year: 2016
journal: Scientific Reports
doi: 10.1038/srep35558
field: cotton stress biology; miRNA regulation
topics: 
  - cotton
  - temperature stress
  - miRNA
  - degradome
  - small RNA
  - stress response
study_type: primary research; stress small RNA profiling
methods: 
  - Temperature stress treatment and physiological assays
  - Cotton seedling temperature treatments
  - small RNA sequencing
  - sRNA library construction and Illumina sequencing
  - miRNA identification
  - miRBase homology and Mireap novel miRNA prediction
  - Degradome sequencing and target analysis
  - degradome/PARE target identification
  - qRT-PCR and enrichment analysis
  - qRT-PCR validation plus GO/KEGG enrichment
  - temperature treatment
  - physiological assays
  - small RNA library sequencing
  - miRBase homology
  - Mireap hairpin prediction
  - sRNA-seq expression comparison
  - log2 ratio threshold
  - degradome sequencing
  - PAREsnip
  - GO/KEGG enrichment
data_types: 
  - degradome tags and target annotations
  - miRNA expression
  - read size distribution
  - sRNA sequences
  - stress phenotypes and metabolite/oxidative markers
study_system: 
  - Gossypium hirsutum cv. YZ1 seedlings
  - "cotton leaves under EL, NL, CK, NH, EH"
  - cotton leaves under temperature treatments
  - cotton seedlings under 4/12/25/35/42 deg C
evidence_strength: moderate; profiling plus degradome target evidence
confidence_level: high; moderate; moderate-high for known; moderate for novel
paper_id: 2016-Wang-Cotton-Temperature-miRNAs
mineru_dir: mineru-parsed/Wang_2016_Scientific Reports
curated_card: 01_Curated/Paper-Cards/2016-Wang-Cotton-Temperature-miRNAs.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2016-Wang-Cotton-Temperature-miRNAs.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# Small RNA-mediated responses to low- and high-temperature stresses in cotton

> [!summary] 一句话结论
> 本文在 cotton seedlings 的低温和高温处理中构建 small RNA/degradome 图谱，识别温度胁迫响应 miRNAs 及其可能靶基因网络。

## 基本信息
- Authors: Qiongshan Wang; Nian Liu; Xiyan Yang; Lili Tu; Xianlong Zhang
- Year: 2016
- Journal: Scientific Reports
- DOI: 10.1038/srep35558
- Study type: primary research; stress small RNA profiling
- Source basis: 01_Curated/Paper-Cards/2016-Wang-Cotton-Temperature-miRNAs.review.md; 01_Curated/Claim-Evidence/2016-Wang-Cotton-Temperature-miRNAs.claims.tsv; 01_Curated/Method-Summaries/method-summary.2016-Wang-Cotton-Temperature-miRNAs.md

## 核心科学问题
本文要回答：Gossypium hirsutum 在 4/12/35/42 deg C 温度胁迫下有哪些 known/novel miRNAs 发生表达变化，以及这些 miRNAs 的 degradome-supported targets 涉及哪些 stress-response pathways。

## 研究设计
二叶期 `G. hirsutum cv. YZ1` seedlings 分别处理 4 deg C、12 deg C、25 deg C、35 deg C、42 deg C for 8 h。作者测定 H2O2、proline、MDA、soluble sugar 等生理指标；构建五个 sRNA libraries 和五个 degradome libraries，并进行 miRNA identification、differential expression、target prediction/validation、GO/KEGG enrichment 和 qRT-PCR。

## 主要发现

### Finding 1
> [!info] Source-reported content
> Seedlings treated at 4, 12 and 42 deg C showed strong wilting; physiological parameters including H2O2, proline, MDA and soluble sugar were generally higher in treatments than control, especially 4 deg C

- Evidence type: phenotype/physiology evidence
- Method: temperature treatment; physiological assays
- Data type: stress phenotypes and metabolite/oxidative markers
- Figure/table anchor: Fig. 1
- Confidence: high
- Limitation: 8 h seedling treatment only

### Finding 2
> [!info] Source-reported content
> Five sRNA libraries generated about 11.8 million clean reads each; 24-nt reads were the most abundant at 41.6-46.6%, followed by 21-nt reads

- Evidence type: sRNA-seq evidence
- Method: small RNA library sequencing
- Data type: read size distribution
- Figure/table anchor: Table 1; Fig. 2
- Confidence: high
- Limitation: leaf tissue only

### Finding 3
> [!info] Source-reported content
> 319 known miRNAs from 144 families and 800 novel miRNAs were identified

- Evidence type: miRNA annotation evidence
- Method: miRBase homology; Mireap hairpin prediction
- Data type: sRNA sequences
- Figure/table anchor: Known and novel miRNA sections; supplementary tables
- Confidence: moderate-high for known; moderate for novel
- Limitation: novel miRNAs need independent validation

### Finding 4
> [!info] Source-reported content
> 63 known miRNAs and 105 novel miRNAs were differentially expressed; high-temperature stress had more differential miRNAs and most miRNAs were downregulated under high temperature

- Evidence type: differential expression evidence
- Method: sRNA-seq expression comparison; log2 ratio threshold
- Data type: miRNA expression
- Figure/table anchor: Fig. 4; Fig. S4-S6; Table S4
- Confidence: moderate
- Limitation: full statistical model not clear in provided text

### Finding 5
> [!info] Source-reported content
> The abstract reports targets analyzed by degradome sequencing and enriched in response to hormone stimulus, oxidation-reduction, photosynthesis, plant-pathogen interaction and plant hormone signal transduction

- Evidence type: target/enrichment evidence
- Method: degradome sequencing; PAREsnip; GO/KEGG enrichment
- Data type: degradome tags and target annotations
- Figure/table anchor: Abstract; Methods target/enrichment sections
- Confidence: moderate
- Limitation: pathway enrichment does not prove stress tolerance function

## 作者结论
作者认为 cotton low/high temperature stresses trigger miRNA expression changes, and the identified miRNA-target network provides insight into molecular mechanisms of cotton temperature-stress responses.

## 谨慎推断
> [!caution] Reasonable inference
> - Temperature-responsive miRNAs may coordinate hormone, redox and photosynthesis-related responses.
> - High-temperature stress appears to cause stronger miRNA expression reprogramming than mild/normal high temperature in this dataset.

## 模型综合
> [!abstract] Model synthesis
> 该研究是 cotton temperature stress miRNA atlas：先确认温度处理造成生理胁迫，再用 sRNA-seq 识别 known/novel miRNAs，并用 degradome 给出靶基因切割证据，最后通过富集分析把 miRNA changes 连接到 stress-response pathways。

## 可复用知识

### Concepts
- [[temperature-responsive miRNA]]
- [[degradome-supported target]]
- [[cotton stress physiology]]

### Methods
- [[Temperature stress treatment and physiological assays]]
- [[Cotton seedling temperature treatments]]
- [[small RNA sequencing]]
- [[sRNA library construction and Illumina sequencing]]
- [[miRNA identification]]
- [[miRBase homology and Mireap novel miRNA prediction]]
- [[Degradome sequencing and target analysis]]
- [[degradome/PARE target identification]]
- [[qRT-PCR and enrichment analysis]]
- [[qRT-PCR validation plus GO/KEGG enrichment]]
- [[temperature treatment]]
- [[physiological assays]]

### Datasets
- unknown

### Analytical frameworks
- unknown

### Experimental designs
- compare extreme/normal low/high temperatures with 25 deg C control

## 局限性
- 未见 miRNA overexpression/knockdown 功能验证。
- novel miRNAs 和 targets 需要独立实验验证。
- 仅 8 h seedling leaf treatments，不能直接外推到 fiber yield。
- figure/table anchor uncertain; needs manual PDF check.

## 开放问题
- 哪些 temperature-responsive miRNAs 具有直接提升 cold/heat tolerance 的功能？
- degradome-supported targets 中哪些是关键调控节点？
- seedling leaf miRNA response 是否与 cotton fiber quality/yield under temperature stress 相关？

## 关联笔记
- Concepts: [[temperature-responsive miRNA]], [[degradome-supported target]], [[cotton stress physiology]]
- Methods: [[Temperature stress treatment and physiological assays]], [[Cotton seedling temperature treatments]], [[small RNA sequencing]], [[sRNA library construction and Illumina sequencing]], [[miRNA identification]], [[miRBase homology and Mireap novel miRNA prediction]], [[Degradome sequencing and target analysis]], [[degradome/PARE target identification]], [[qRT-PCR and enrichment analysis]], [[qRT-PCR validation plus GO/KEGG enrichment]], [[temperature treatment]], [[physiological assays]]
- Evidence: [[2016-Wang-Cotton-Temperature-miRNAs claims]]
- Questions: [[2016-Wang-Cotton-Temperature-miRNAs open questions]]
