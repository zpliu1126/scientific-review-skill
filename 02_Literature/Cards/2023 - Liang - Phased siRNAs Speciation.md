---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: "Taxon-specific, phased siRNAs underlie a speciation locus in monkeyflowers"
authors: Mei Liang; Wenjie Chen; Amy M. LaFountain; Yuanlong Liu; Foen Peng; Rui Xia; H. D. Bradshaw; Yao-Wu Yuan
year: 2023
journal: Science
doi: 10.1126/science.adf1323
field: plant evolutionary genetics; small RNA biology; floral pigmentation
topics: 
  - phased siRNA
  - speciation
  - Mimulus
  - YUP
  - RCP2
  - carotenoid pigmentation
  - pollination syndrome
study_type: primary research; functional genetics; evolutionary genomics
methods: 
  - Fine-scale genetic mapping and NIL construction
  - Genetic mapping with near-isogenic lines
  - Protein-coding candidate RNAi screen
  - RNA interference of interval protein-coding genes
  - RNA-seq/transcript inspection and hairpin prediction
  - Candidate noncoding transcript identification
  - sRNA-seq and phasing analysis
  - small RNA sequencing and phased siRNA analysis
  - qRT-PCR of siRNA abundance
  - qRT-PCR for YUP_siR1/siR-RCP2
  - Transgenic YUP allele overexpression
  - 35S-driven YUP allele overexpression
  - Target validation by 5' RLM RACE
  - RNA ligase-mediated 5' rapid amplification of cDNA ends
  - Artificial siRNA overexpression
  - "35S:amiR-RCP2 transgenic assay"
  - RCP2-YFP and siRNA-resistant target-site reporter assay
  - RCP2 translational repression reporter
  - Comparative genomics and synteny analysis
  - Synteny and evolutionary origin analysis
  - NIL construction
  - backcrossing/selfing
  - genotyping
  - RNA interference
  - RNA-seq
  - BLAST
  - hairpin prediction
  - sRNA-seq
  - phasing analysis
  - CaMV 35S-driven transgenic overexpression
  - target prediction
  - 5' RLM RACE
  - qRT-PCR
  - YFP fusion reporter
  - silent target-site mutation
  - confocal microscopy
  - mutant crosses
  - overexpression
  - synteny analysis
  - genome sequencing
  - phylogenetic timing
  - transgenic overexpression
data_types: 
  - genome assemblies; flower phenotype
  - pigment phenotype; siRNA abundance
  - pigmentation phenotype
  - segregating genotypes and flower pigment phenotypes
  - small RNA sequence; RCP2 transcript cleavage
  - transcript and protein reporter signal
  - transcript reads; small RNA reads
study_system: 
  - Mimulus lewisii
  - Mimulus lewisii and NILs
  - Mimulus lewisii; Mimulus parishii; Mpar yupC/C NIL
  - Mimulus parishii transgenics
  - Mimulus parishii; Mimulus cardinalis; NILs
  - Mimulus species
  - Mpar DPKC/C NIL
  - Mpar DPKC/C NIL background
evidence_strength: high for YUP-RCP2 functional mechanism; moderate-high for evolutionary/speciation interpretation
confidence_level: high; moderate-high
paper_id: 2023-Liang-Phased-siRNAs-Speciation
mineru_dir: mineru-parsed/Liang_2023_Science
curated_card: 01_Curated/Paper-Cards/2023-Liang-Phased-siRNAs-Speciation.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2023-Liang-Phased-siRNAs-Speciation.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# Taxon-specific, phased siRNAs underlie a speciation locus in monkeyflowers

> [!summary] 一句话结论
> 本文证明 Mimulus 的物种分化位点 YUP 是一个产生 phased siRNA 的非编码基因，其中 siR-RCP2 靶向并抑制 RCP2，从而改变花瓣类胡萝卜素沉积并影响传粉者介导的物种分化。

## 基本信息
- Authors: Mei Liang; Wenjie Chen; Amy M. LaFountain; Yuanlong Liu; Foen Peng; Rui Xia; H. D. Bradshaw; Yao-Wu Yuan
- Year: 2023
- Journal: Science
- DOI: 10.1126/science.adf1323
- Study type: primary research; functional genetics; evolutionary genomics
- Source basis: 01_Curated/Paper-Cards/2023-Liang-Phased-siRNAs-Speciation.review.md; 01_Curated/Claim-Evidence/2023-Liang-Phased-siRNAs-Speciation.claims.tsv; 01_Curated/Method-Summaries/method-summary.2023-Liang-Phased-siRNAs-Speciation.md

## 核心科学问题
本文试图回答：Mimulus 中控制花色、传粉者偏好和生殖隔离的 YUP 位点究竟是什么分子实体，以及 taxon-specific small RNA locus 是否能作为功能性演化创新参与表型分化和物种形成。

## 研究设计
研究系统为 Mimulus lewisii complex，包括 bumble bee-pollinated `M. lewisii`、self-pollinated `M. parishii`、hummingbird-pollinated `M. cardinalis` 及多个 near-isogenic lines (NILs) 和转基因材料。作者通过 `M. parishii` 与 `M. cardinalis` 遗传背景进行精细定位，将 YUP 缩小到 70-kb interval；随后用 RNA-seq/sRNA-seq、qRT-PCR、转基因过表达、人工 siRNA、5' RLM RACE、RCP2-YFP reporter、siR-RCP2-resistant RCP2、遗传杂交和 synteny/evolutionary analysis 解析分子机制和演化来源。

## 主要发现

### Finding 1
> [!info] Source-reported content
> Genotyping about 3000 BC3S1 and BC3S2 individuals delimited YUP to a 70-kb interval and produced refined NILs with petal lobe carotenoid accumulation

- Evidence type: genetic mapping
- Method: NIL construction; backcrossing/selfing; genotyping
- Data type: segregating genotypes and flower pigment phenotypes
- Figure/table anchor: Fig. 1I; fig. S2
- Confidence: high
- Limitation: supplementary marker details require manual PDF check

### Finding 2
> [!info] Source-reported content
> RNA interference experiments of eight protein-coding genes in the 70-kb interval in M. lewisii produced no phenotypic changes in carotenoid pigmentation

- Evidence type: functional screen
- Method: RNA interference
- Data type: pigmentation phenotype
- Figure/table anchor: fig. S3
- Confidence: moderate-high
- Limitation: knockdown efficiency and full RNAi details not visible in provided text

### Finding 3
> [!info] Source-reported content
> RNA-seq revealed an about 1.3-kb transcript with no conserved ORF and an inverted repeat; sRNA-seq showed abundant 21-nt siRNAs in a phased pattern in M. lewisii and M. parishii

- Evidence type: transcript and small RNA evidence
- Method: RNA-seq; BLAST; hairpin prediction; sRNA-seq; phasing analysis
- Data type: transcript reads; small RNA reads
- Figure/table anchor: Fig. 2A; figs. S4-S6
- Confidence: high
- Limitation: phasing calculation details require supplementary method check

### Finding 4
> [!info] Source-reported content
> All 30 M. lewisii YUP overexpression lines and all 35 M. parishii YUP overexpression lines showed dark pink flowers with no carotenoid accumulation; 41 M. cardinalis allele lines showed no phenotypic change

- Evidence type: transgenic functional validation
- Method: CaMV 35S-driven transgenic overexpression
- Data type: pigment phenotype; siRNA abundance
- Figure/table anchor: Fig. 2D-G; figs. S7-S8
- Confidence: high
- Limitation: 35S overexpression may differ from endogenous expression

### Finding 5
> [!info] Source-reported content
> Three YUP_siR1 forms were predicted to target RCP2; 5' RLM RACE confirmed RCP2 transcript cleavage at the predicted target site

- Evidence type: target validation
- Method: target prediction; 5' RLM RACE
- Data type: small RNA sequence; RCP2 transcript cleavage
- Figure/table anchor: Fig. 3A; fig. S9A
- Confidence: high
- Limitation: RACE clone counts should be manually checked in figure

### Finding 6
> [!info] Source-reported content
> Six of 21 35S:amiR-RCP2 lines displayed dark pink flowers without carotenoid accumulation and strong lines showed 17- to 43-fold siR-RCP2 increase

- Evidence type: transgenic perturbation
- Method: artificial siRNA overexpression; qRT-PCR
- Data type: pigment phenotype; siRNA abundance
- Figure/table anchor: Fig. 3B-D; fig. S8D
- Confidence: high
- Limitation: not all transgenic lines showed phenotype; likely expression-dependent

## 作者结论
作者明确结论是：YUP 是一个 taxon-restricted noncoding gene，可产生 phased siRNAs；其中 siR-RCP2 通过 transcript cleavage 和 translational inhibition 抑制 RCP2；YUP-SOLAR-PELAN superlocus 自约 5 million years ago 起源后，参与后代 Mimulus 物种的花色多样化、传粉模式适应和物种形成。

## 谨慎推断
> [!caution] Reasonable inference
> - The YUP case may suggest that taxon-restricted regulatory small RNA loci can be major-effect loci in adaptive floral traits.
> - The presence of YUP, SOLAR, and PELAN in a linked superlocus is consistent with coordinated selection on flower-color traits, but direct historical selection is not experimentally demonstrated.
> - The disrupted phased pattern in M. cardinalis could indicate that loss or alteration of specific phased siRNA output contributed to red-flower evolution.

## 模型综合
> [!abstract] Model synthesis
> 本文把 small RNA 从“调控层背景因素”提升为“物种分化位点本体”：YUP 不是编码色素酶或转录因子的经典基因，而是由基因片段倒置重复形成的非编码 phased siRNA 产生位点。它通过 siR-RCP2 抑制 RCP2，从而控制类胡萝卜素在花瓣中的空间沉积；RCP1 又在 nectar guide 区域压制 YUP，使局部黄色信号保留。这个 RCP1-YUP-RCP2 轴把发育调控、small RNA 靶向和传粉者选择连接成一个可验证的演化机制。

## 可复用知识

### Concepts
- [[taxon-restricted regulatory sRNA]]
- [[phased siRNA]]
- [[noncoding speciation locus]]
- [[floral carotenoid patterning]]
- [[pollinator-mediated reproductive isolation]]
- [[superlocus]]

### Methods
- [[Fine-scale genetic mapping and NIL construction]]
- [[Genetic mapping with near-isogenic lines]]
- [[Protein-coding candidate RNAi screen]]
- [[RNA interference of interval protein-coding genes]]
- [[RNA-seq/transcript inspection and hairpin prediction]]
- [[Candidate noncoding transcript identification]]
- [[sRNA-seq and phasing analysis]]
- [[small RNA sequencing and phased siRNA analysis]]
- [[qRT-PCR of siRNA abundance]]
- [[qRT-PCR for YUP_siR1/siR-RCP2]]
- [[Transgenic YUP allele overexpression]]
- [[35S-driven YUP allele overexpression]]

### Datasets
- sRNA sequencing and whole-genome sequencing deposited under BioProject PRJNA882815 and PRJNA882787
- according to provided text

### Analytical frameworks
- infer evolutionary origin of a regulatory locus by combining synteny
- phylogeny
- functional transgenics
- and phenotype history

### Experimental designs
- allele-specific transgenic rescue/overexpression
- target-site mutation to separate transcript abundance from translation repression

## 局限性
- Supplementary Materials and Methods are referenced but not fully present in MinerU `full.md`; needs manual PDF check.
- Figure/table anchor uncertain because separate MinerU `images/`/`tables/` directories are absent.
- Pollinator-mediated speciation background partly依赖 prior studies cited in the paper；本凝练没有把被引文献当作已独立验证证据。
- YUP overexpression in distant Mimulus species说明系统对 YUP action 有 predisposition，但不能单独证明祖先状态下自然表达模式。
- RCP1 对 YUP 的调控在 provided text 中由表达互补、突变体和过表达支持；直接 DNA binding 或顺式元件证据未见报告。

## 开放问题
- YUP 的 phased siRNA biogenesis 是否确由 DCL4 或其他 Dicer-like protein 介导？
- RCP1 是否直接结合 YUP regulatory region，还是通过间接调控降低 YUP/siR-RCP2？
- YUP-SOLAR-PELAN superlocus 的形成过程涉及哪些结构变异机制？
- 在自然群体中，YUP phased pattern 的变异是否与传粉者偏好和适合度直接关联？
- 其他植物类群中是否也存在类似“非编码 small RNA speciation locus”？

## 关联笔记
- Concepts: [[taxon-restricted regulatory sRNA]], [[phased siRNA]], [[noncoding speciation locus]], [[floral carotenoid patterning]], [[pollinator-mediated reproductive isolation]], [[superlocus]]
- Methods: [[Fine-scale genetic mapping and NIL construction]], [[Genetic mapping with near-isogenic lines]], [[Protein-coding candidate RNAi screen]], [[RNA interference of interval protein-coding genes]], [[RNA-seq/transcript inspection and hairpin prediction]], [[Candidate noncoding transcript identification]], [[sRNA-seq and phasing analysis]], [[small RNA sequencing and phased siRNA analysis]], [[qRT-PCR of siRNA abundance]], [[qRT-PCR for YUP_siR1/siR-RCP2]], [[Transgenic YUP allele overexpression]], [[35S-driven YUP allele overexpression]]
- Evidence: [[2023-Liang-Phased-siRNAs-Speciation claims]]
- Questions: [[2023-Liang-Phased-siRNAs-Speciation open questions]]
