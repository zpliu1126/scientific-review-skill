---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: Genetic basis of sRNA quantitative variation analyzed using an experimental population derived from an elite rice hybrid
authors: Jia Wang; Wen Yao; Dan Zhu; Weibo Xie; Qifa Zhang
year: 2015
journal: eLife
doi: 10.7554/eLife.03913
field: rice genomics; small RNA genetics
topics: 
  - rice
  - sRNA
  - sQTL
  - scQTL
  - IMF2
  - small RNA biogenesis
study_type: primary research; sRNA quantitative genetics
methods: 
  - IMF2 population sRNA profiling
  - sRNA-seq in rice IMF2 population
  - SNP-replaced genome mapping
  - Parental SNP-replaced reference mapping
  - sQTL/scQTL mapping
  - Composite interval mapping with R/qtl
  - Mother gene and expression correlation analysis
  - sRNA-mother gene co-regulation analysis
  - sRNA-seq
  - read filtering
  - parental SNP-replaced mapping
  - R/qtl CIM
  - ultrahigh-density bin map
  - correlation analysis
  - eQTL/sQTL comparison
  - QTL hotspot analysis
  - candidate gene annotation
  - QTL additive/dominance effect analysis
data_types: 
  - sQTL hotspots; sRNA length classes
  - sRNA and mRNA expression
  - sRNA expression traits
  - sRNA expression traits and genotypes
  - sRNA reads
study_system: 
  - rice IMF2 population
  - rice Zhenshan97/Minghui63-derived IMF2 flag leaves
evidence_strength: high for population sRNA-QTL mapping; moderate for candidate biogenesis-gene interpretation
confidence_level: moderate-high; moderate; high
paper_id: 2015-Wang-Rice-sRNA-QTL
mineru_dir: mineru-parsed/Wang_2015_eLife
curated_card: 01_Curated/Paper-Cards/2015-Wang-Rice-sRNA-QTL.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2015-Wang-Rice-sRNA-QTL.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# Genetic basis of sRNA quantitative variation analyzed using an experimental population derived from an elite rice hybrid

> [!summary] 一句话结论
> 本文用 elite rice hybrid 来源的 immortalized F2 群体把 sRNA abundance 当作数量性状，系统定位了 sQTL/scQTL，显示植物 sRNA 水平具有广泛遗传控制且常与 mother gene expression 不同步。

## 基本信息
- Authors: Jia Wang; Wen Yao; Dan Zhu; Weibo Xie; Qifa Zhang
- Year: 2015
- Journal: eLife
- DOI: 10.7554/eLife.03913
- Study type: primary research; sRNA quantitative genetics
- Source basis: 01_Curated/Paper-Cards/2015-Wang-Rice-sRNA-QTL.review.md; 01_Curated/Claim-Evidence/2015-Wang-Rice-sRNA-QTL.claims.tsv; 01_Curated/Method-Summaries/method-summary.2015-Wang-Rice-sRNA-QTL.md

## 核心科学问题
本文要回答：rice 个体间 sRNA abundance 的定量差异由哪些遗传位点控制，sRNA 与其来源基因/cluster 是否共同调控，以及 sRNA biogenesis genes 是否解释特定长度类别的 sRNA variation。

## 研究设计
材料为 Zhenshan 97 x Minghui 63 RILs 构建的 98 个 IMF2 hybrids、亲本和 F1。作者从 flag leaf full expansion day 取样，构建 104 个 sRNA libraries，并结合 mRNA-seq、WGBS 和 ultrahigh-density bin map 进行 QTL 分析。

## 主要发现

### Finding 1
> [!info] Source-reported content
> 104 libraries yielded 53,613,739 unique sRNAs and 165,797 sRNA expression traits; 24-nt sRNAs were most numerous

- Evidence type: sRNA-seq profiling
- Method: sRNA-seq; read filtering; parental SNP-replaced mapping
- Data type: sRNA reads
- Figure/table anchor: Table 1; Fig. 1
- Confidence: high
- Limitation: flag leaf only

### Finding 2
> [!info] Source-reported content
> 66,649 s-traits mapped 40,049 local-sQTLs and 30,809 distant-sQTLs; 22,263 scQTLs were recovered for 20,249 sc-traits

- Evidence type: QTL evidence
- Method: R/qtl CIM; ultrahigh-density bin map
- Data type: sRNA expression traits and genotypes
- Figure/table anchor: Abstract; QTL sections
- Confidence: moderate-high
- Limitation: QTL intervals require validation for causal variants

### Finding 3
> [!info] Source-reported content
> The abstract states that genetic co-regulation was observed for a portion of sRNAs, but most sRNAs and mother genes showed little co-regulation

- Evidence type: expression/QTL comparison
- Method: correlation analysis; eQTL/sQTL comparison
- Data type: sRNA and mRNA expression
- Figure/table anchor: Fig. 2 and related sections
- Confidence: moderate-high
- Limitation: does not define causal basis of decoupling

### Finding 4
> [!info] Source-reported content
> Some sRNA biogenesis genes were located in distant-sQTL hotspots and corresponded with specific length classes of sRNAs

- Evidence type: QTL hotspot/candidate evidence
- Method: QTL hotspot analysis; candidate gene annotation
- Data type: sQTL hotspots; sRNA length classes
- Figure/table anchor: Discussion; hotspot sections
- Confidence: moderate
- Limitation: candidate genes not functionally validated in provided text

### Finding 5
> [!info] Source-reported content
> The discussion reports heterozygotes often had lower sRNA levels than parental means or lower homozygotes, and negative-dominance sQTLs were mostly distant-sQTLs

- Evidence type: genetic effect evidence
- Method: QTL additive/dominance effect analysis
- Data type: sRNA expression traits
- Figure/table anchor: Discussion
- Confidence: moderate
- Limitation: link to hybrid performance unresolved

## 作者结论
作者认为 rice sRNA abundance 具有大规模遗传控制；sRNAs 与 mother genes 的调控常可分离；部分 distant-sQTL hotspots 可能反映 sRNA biogenesis/function machinery 对特定 sRNA 长度类别的调节。

## 谨慎推断
> [!caution] Reasonable inference
> - The sQTL framework may suggest that small RNA abundance can be treated as a molecular quantitative trait, similar to mRNA eQTL.
> - Distant-sQTL hotspots could indicate trans-acting regulators, but specific causal variants need validation.

## 模型综合
> [!abstract] Model synthesis
> 本文提供了“sRNA quantitative genetics”框架：从单条 sRNA、sRNA cluster、mother gene expression 和 genetic bin effects 四个层面，把 sRNA variation 拆成 local genetic control、distant/trans control 和 cluster-level co-regulation。

## 可复用知识

### Concepts
- [[s-trait]]
- [[sQTL]]
- [[sc-trait]]
- [[scQTL]]
- [[local/distant QTL]]
- [[negative dominance]]

### Methods
- [[IMF2 population sRNA profiling]]
- [[sRNA-seq in rice IMF2 population]]
- [[SNP-replaced genome mapping]]
- [[Parental SNP-replaced reference mapping]]
- [[sQTL/scQTL mapping]]
- [[Composite interval mapping with R/qtl]]
- [[Mother gene and expression correlation analysis]]
- [[sRNA-mother gene co-regulation analysis]]
- [[sRNA-seq]]
- [[read filtering]]
- [[parental SNP-replaced mapping]]
- [[R/qtl CIM]]

### Datasets
- unknown

### Analytical frameworks
- unknown

### Experimental designs
- unknown

## 局限性
- 主要组织是 flag leaf，不能代表所有 rice tissues。
- QTL/candidate gene associations mostly lack functional perturbation.
- Relationship between negative dominance of sRNA levels and hybrid performance remains unresolved.
- figure/table anchor uncertain; needs manual PDF check.

## 开放问题
- 哪些 distant-sQTL hotspots 的 candidate genes 真正控制 sRNA biogenesis？
- sRNA negative dominance 与 rice hybrid vigor 是否有关？
- 不同 tissue 和 stress 条件下 sQTL landscape 是否稳定？

## 关联笔记
- Concepts: [[s-trait]], [[sQTL]], [[sc-trait]], [[scQTL]], [[local/distant QTL]], [[negative dominance]]
- Methods: [[IMF2 population sRNA profiling]], [[sRNA-seq in rice IMF2 population]], [[SNP-replaced genome mapping]], [[Parental SNP-replaced reference mapping]], [[sQTL/scQTL mapping]], [[Composite interval mapping with R/qtl]], [[Mother gene and expression correlation analysis]], [[sRNA-mother gene co-regulation analysis]], [[sRNA-seq]], [[read filtering]], [[parental SNP-replaced mapping]], [[R/qtl CIM]]
- Evidence: [[2015-Wang-Rice-sRNA-QTL claims]]
- Questions: [[2015-Wang-Rice-sRNA-QTL open questions]]
