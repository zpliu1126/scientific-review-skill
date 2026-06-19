---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: "RNA-directed DNA methylation: an epigenetic pathway of increasing complexity"
authors: Marjori A. Matzke; Rebecca A. Mosher
year: 2014
journal: Nature Reviews Genetics
doi: 10.1038/nrg3683
field: plant epigenetics; small RNA biology
topics: 
  - RdDM
  - RNA-directed DNA methylation
  - Pol IV
  - Pol V
  - siRNA
  - AGO4
  - DRM2
  - Arabidopsis
study_type: review
methods: 
  - Review synthesis of RdDM literature
  - Narrative review and pathway synthesis
  - RdDM-defective mutant analysis
  - Mutant-based pathway component identification
  - Small RNA sequencing
  - sRNA-seq
  - Genome-wide DNA methylation profiling
  - methylome profiling at single-nucleotide resolution
  - ChIP-seq and chromatin feature mapping
  - Chromatin immunoprecipitation followed by sequencing
  - Protein interaction and biochemical assays
  - Protein interaction/biochemical characterization
  - literature synthesis
  - literature synthesis of genetic and biochemical studies
  - mutant-study synthesis
  - chromatin recruitment studies
  - ChIP-seq/protein interaction studies
  - genome-wide methylation and chromatin-study synthesis
data_types: 
  - 24-nt siRNA abundance
  - chromatin marks; Pol IV targeting
  - diverse biological process evidence
  - genomic methylation and chromatin features
  - pathway model
  - review synthesis
  - scaffold transcripts; chromatin occupancy
study_system: 
  - Arabidopsis thaliana
  - Arabidopsis thaliana-focused
  - plants
  - plants; mainly Arabidopsis
evidence_strength: review-level evidence
confidence_level: moderate-high; high; high for outline; moderate for unresolved steps
paper_id: 2014-Matzke-RNA-directed-DNA-Methylation
mineru_dir: mineru-parsed/Matzke_2014_Nature Reviews Genetics
curated_card: 01_Curated/Paper-Cards/2014-Matzke-RNA-directed-DNA-Methylation.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2014-Matzke-RNA-directed-DNA-Methylation.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# RNA-directed DNA methylation: an epigenetic pathway of increasing complexity

> [!summary] 一句话结论
> 这篇综述系统概括了植物 RdDM 的 canonical pathway、Pol IV/Pol V 专化转录机制、辅助因子、染色质互作以及非 canonical 变体，是构建植物 small RNA-表观遗传知识框架的基础综述。

## 基本信息
- Authors: Marjori A. Matzke; Rebecca A. Mosher
- Year: 2014
- Journal: Nature Reviews Genetics
- DOI: 10.1038/nrg3683
- Study type: review
- Source basis: 01_Curated/Paper-Cards/2014-Matzke-RNA-directed-DNA-Methylation.review.md; 01_Curated/Claim-Evidence/2014-Matzke-RNA-directed-DNA-Methylation.claims.tsv; 01_Curated/Method-Summaries/method-summary.2014-Matzke-RNA-directed-DNA-Methylation.md

## 核心科学问题
本文综述的问题是：植物 RNA-directed DNA methylation 如何通过 small RNAs、Pol IV/Pol V、AGO proteins 和 DNA methyltransferases 建立转录沉默，以及这一通路在转座子、基因调控、胁迫、防御和繁殖中的作用边界是什么。

## 研究设计
这是 review article，不是单篇原始实验研究。文章主要基于 Arabidopsis thaliana 文献，同时在适当位置纳入其他植物研究。文中整合了遗传学、生化、ChIP-seq、methylome、small RNA sequencing 和突变体研究，但这些证据来自被综述文献；本卡不把综述观点当作原始实验结果。

## 主要发现

### Finding 1
> [!info] Source-reported content
> The abstract states that RNA-directed DNA methylation is the major small RNA-mediated epigenetic pathway in plants

- Evidence type: review-level evidence
- Method: literature synthesis
- Data type: review synthesis
- Figure/table anchor: Abstract
- Confidence: high
- Limitation: review article; not primary experimental evidence

### Finding 2
> [!info] Source-reported content
> The review describes Pol IV transcripts copied by RDR2, processed by DCL3 into 24-nt siRNAs, loaded onto AGO4, paired with Pol V scaffold transcripts, and recruiting methyltransferase activity for CG/CHG/CHH methylation

- Evidence type: review-level mechanistic synthesis
- Method: literature synthesis of genetic and biochemical studies
- Data type: pathway model
- Figure/table anchor: Fig. 1; Table 1; Canonical RdDM pathway mechanisms
- Confidence: high for outline; moderate for unresolved steps
- Limitation: Pol IV/Pol V templates and some accessory functions remain incompletely understood

### Finding 3
> [!info] Source-reported content
> The review states that analyses of Pol IV-defective mutants show Pol IV is responsible for producing precursors of more than 90% of 24-nt siRNAs that guide canonical RdDM

- Evidence type: review-level evidence
- Method: mutant-study synthesis
- Data type: 24-nt siRNA abundance
- Figure/table anchor: Table 1; Pol IV-dependent siRNA biogenesis
- Confidence: high
- Limitation: underlying primary studies must be checked for exact experimental details

### Finding 4
> [!info] Source-reported content
> The review states that SHH1 binds H3K9me and unmethylated H3K4 through a tandem Tudor-like fold and recruits Pol IV to a subset of genomic targets

- Evidence type: review-level evidence
- Method: literature synthesis; chromatin recruitment studies
- Data type: chromatin marks; Pol IV targeting
- Figure/table anchor: Fig. 1; Table 1
- Confidence: moderate-high
- Limitation: Pol IV recruitment is explicitly not fully understood

### Finding 5
> [!info] Source-reported content
> The review states that Pol V transcripts are thought to provide scaffold RNAs that interact with siRNAs and recruit other silencing factors

- Evidence type: review-level evidence
- Method: literature synthesis; ChIP-seq/protein interaction studies
- Data type: scaffold transcripts; chromatin occupancy
- Figure/table anchor: Fig. 1; Pol V-mediated de novo methylation
- Confidence: moderate-high
- Limitation: Pol V occupancy alone is not sufficient for RdDM at all sites

### Finding 6
> [!info] Source-reported content
> The review states Pol V-mediated RdDM acts at many sites with preference for euchromatic small/young intergenic transposons and genes containing repeats; pericentromeric heterochromatin mostly relies on DDM1, MET1, CMT2 and CMT3

- Evidence type: review-level evidence
- Method: genome-wide methylation and chromatin-study synthesis
- Data type: genomic methylation and chromatin features
- Figure/table anchor: Pol V-mediated de novo methylation; Interplay with chromatin features
- Confidence: moderate-high
- Limitation: target preference may vary by locus and species

## 作者结论
作者认为 RdDM 是植物中主要的 small RNA-mediated epigenetic pathway，且其复杂度不断增加：除了 canonical Pol IV/Pol V-dependent pathway，还存在 recruitment factors、chromatin feedback、non-canonical variations 和多个生物学过程中的功能联系。作者同时强调，Pol IV/Pol V 的体内模板、辅助因子功能和靶向机制仍有许多未解问题。

## 谨慎推断
> [!caution] Reasonable inference
> - This review may suggest that plant small RNA biology cannot be separated from chromatin state, because siRNA biogenesis and DNA methylation targeting are coupled to histone marks, polymerase recruitment and repeat architecture.
> - The emphasis on Pol IV/Pol V specialization is consistent with a plant-specific expansion of transcriptional machinery for epigenetic regulation.
> - Because many examples are Arabidopsis-centered, extrapolation to all crops should be made cautiously.

## 模型综合
> [!abstract] Model synthesis
> 可以把本文的核心模型概括为“双转录系统 RdDM”：Pol IV 侧负责生成 24-nt siRNA 信息，Pol V 侧在目标位点提供 scaffold transcript 和染色质平台，两者通过 AGO4-bound siRNA 的序列互补连接，最终招募 DRM2 建立 de novo DNA methylation。染色质标记、DNA methylation、转座子状态和辅助蛋白共同决定 RdDM 的靶向和稳定性。

## 可复用知识

### Concepts
- [[RdDM]]
- [[transcriptional gene silencing]]
- [[de novo methylation]]
- [[scaffold RNA]]
- [[siRNA effector complex]]
- [[chromatin feedback loop]]

### Methods
- [[Review synthesis of RdDM literature]]
- [[Narrative review and pathway synthesis]]
- [[RdDM-defective mutant analysis]]
- [[Mutant-based pathway component identification]]
- [[Small RNA sequencing]]
- [[sRNA-seq]]
- [[Genome-wide DNA methylation profiling]]
- [[methylome profiling at single-nucleotide resolution]]
- [[ChIP-seq and chromatin feature mapping]]
- [[Chromatin immunoprecipitation followed by sequencing]]
- [[Protein interaction and biochemical assays]]
- [[Protein interaction/biochemical characterization]]

### Datasets
- unknown

### Analytical frameworks
- distinguish canonical RdDM
- non-canonical RdDM
- and siRNA-independent heterochromatic methylation pathways

### Experimental designs
- unknown

## 局限性
- 这是综述文章，所有事实性机制陈述属于 review-level evidence，不能等同于本文作者新做的实验结果。
- MinerU 对 Fig. 1 flowchart 的结构化抽取明显失真，需 manual PDF check。
- 文章发表于 2014，后续 RdDM 领域可能已有更新；本凝练只代表 provided text。
- 对许多通路成员的功能，作者本身也标注为 only partially understood 或 recruitment not fully understood。
- 不同 biological roles 的证据强弱不一，需要回读原始研究才能进入正式证据矩阵。

## 开放问题
- Pol IV 和 Pol V 的真实 in vivo templates 是什么？
- 不同 genomic targets 如何选择 Pol IV/Pol V-dependent RdDM、RDR6-dependent non-canonical RdDM 或 DDM1/CMT/MET1 体系？
- RdDM 在 pathogen defence、stress response 和 reproduction 中哪些作用是直接因果，哪些只是伴随性甲基化变化？
- 作物和非 Arabidopsis 植物中的 RdDM component 是否有同样功能和靶向偏好？
- RdDM 产生的甲基化变化在自然群体和杂交后代中如何遗传和选择？

## 关联笔记
- Concepts: [[RdDM]], [[transcriptional gene silencing]], [[de novo methylation]], [[scaffold RNA]], [[siRNA effector complex]], [[chromatin feedback loop]]
- Methods: [[Review synthesis of RdDM literature]], [[Narrative review and pathway synthesis]], [[RdDM-defective mutant analysis]], [[Mutant-based pathway component identification]], [[Small RNA sequencing]], [[sRNA-seq]], [[Genome-wide DNA methylation profiling]], [[methylome profiling at single-nucleotide resolution]], [[ChIP-seq and chromatin feature mapping]], [[Chromatin immunoprecipitation followed by sequencing]], [[Protein interaction and biochemical assays]], [[Protein interaction/biochemical characterization]]
- Evidence: [[2014-Matzke-RNA-directed-DNA-Methylation claims]]
- Questions: [[2014-Matzke-RNA-directed-DNA-Methylation open questions]]
