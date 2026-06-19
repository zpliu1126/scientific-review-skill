---
type: literature-note
source: mineru
curation: scientific-review-skill
status: curated
title: Dynamic roles of small RNAs and DNA methylation associated with heterosis in allotetraploid cotton (Gossypium hirsutum L.)
authors: Rasmieh Hamid; Feba Jacob; Zahra Ghorbanzadeh; Leila Jafari; Omran Alishah
year: 2023
journal: BMC Plant Biology
doi: 10.1186/s12870-023-04495-2
field: plant epigenomics; crop heterosis; cotton
topics: 
  - small RNA
  - DNA methylation
  - heterosis
  - cotton
  - transcriptomics
  - miRNA
  - siRNA
study_type: primary research; multi-omics association study
methods: 
  - Field and developmental-stage phenotyping
  - Field and growth trait phenotyping
  - RNA-seq differential expression analysis
  - mRNA transcriptome profiling and MPV-DEG analysis
  - Expression level dominance classification
  - ELD classification
  - SNP-based allele-specific expression and cis/trans regulation analysis
  - Allele-specific expression and cis/trans effect classification
  - Small RNA sequencing and siRNA cluster analysis
  - small RNA-seq and 24-nt siRNA cluster profiling
  - "miRNA identification, target prediction, and correlation"
  - known/novel miRNA profiling and target analysis
  - Whole-genome bisulfite sequencing and methylome integration
  - Bisulfite sequencing and DMR/methylation analysis
  - field phenotyping
  - MPV comparison
  - RNA-seq differential expression
  - GO/KEGG enrichment
  - genome resequencing
  - SNP-based allelic expression
  - cis/trans effect classification
  - small RNA-seq
  - siRNA cluster calling
  - genomic colocalization
  - bisulfite sequencing
  - TE expression analysis
  - miRNA identification
  - target prediction
  - expression correlation
  - integrated multi-omics interpretation
data_types: 
  - allelic mRNA expression
  - "integrated phenotype, transcriptome, small RNA, methylome"
  - mRNA expression
  - miRNA expression; predicted target mRNA expression
  - siRNA clusters; methylation; TE expression
  - small RNA reads; genome annotation; gene expression
  - yield and growth traits
study_system: 
  - Gossypium hirsutum Latif x Taban F1
  - Gossypium hirsutum hybrid and parents
evidence_strength: moderate; multi-omics observational evidence with phenotype association
confidence_level: moderate; high; moderate-high
paper_id: 2023-Hamid-Cotton-Heterosis
mineru_dir: mineru-parsed/Hamid_2023_BMC Plant Biology
curated_card: 01_Curated/Paper-Cards/2023-Hamid-Cotton-Heterosis.review.md
claim_evidence_table: 01_Curated/Claim-Evidence/2023-Hamid-Cotton-Heterosis.claims.tsv
created: 2026-06-07
updated: 2026-06-07
---

# Dynamic roles of small RNAs and DNA methylation associated with heterosis in allotetraploid cotton (Gossypium hirsutum L.)

> [!summary] 一句话结论
> 本文在陆地棉杂交种及亲本中整合表型、转录组、小 RNA 组和甲基化组数据，提出杂种优势与高亲表达偏向、24-nt siRNA、DNA 甲基化和 TE 表达变化之间存在关联。

## 基本信息
- Authors: Rasmieh Hamid; Feba Jacob; Zahra Ghorbanzadeh; Leila Jafari; Omran Alishah
- Year: 2023
- Journal: BMC Plant Biology
- DOI: 10.1186/s12870-023-04495-2
- Study type: primary research; multi-omics association study
- Source basis: 01_Curated/Paper-Cards/2023-Hamid-Cotton-Heterosis.review.md; 01_Curated/Claim-Evidence/2023-Hamid-Cotton-Heterosis.claims.tsv; 01_Curated/Method-Summaries/method-summary.2023-Hamid-Cotton-Heterosis.md

## 核心科学问题
本文试图回答：在异源四倍体棉花中，F1 杂种优势是否伴随基因表达重组、小 RNA 表达变化和 DNA 甲基化变化，以及这些组学变化是否与产量和生长优势相关。

## 研究设计
研究对象为陆地棉 `Gossypium hirsutum L.` 杂交组合：Latif 作为母本、Taban 作为父本，产生 F1 hybrid。作者先比较两年田间性状和 20、40、60 天发育阶段的生长参数，随后选择 squaring stage 相关样本进行下游多组学分析。
数据类型包括：
- 表型数据：铃数、纤维产量、总籽棉产量、鲜重/干重、shoot weight、shoot/root length。
- mRNA-seq：F1 与双亲在 match-head (MH)、square growth midpoint (SM)、1DPA ovule 的花芽/胚珠样本，三次生物学重复。
- small RNA-seq：27 个 sRNA-seq libraries，用于 miRNA 和 24-nt siRNA profiling。
- bisulfite sequencing：SM stage methylome profiling。
- genome resequencing：用于 parental allele discrimination 和 cis/trans regulatory analysis。
样本量、田间重复设计、完整统计模型和 qRT-PCR 验证细节在 provided text 中未完整报告；Methods S1 被提及但未在 MinerU `full.md` 中完整展开，需 manual PDF check。

## 主要发现

### Finding 1
> [!info] Source-reported content
> F1 from Latif x Taban had total seed cotton yield 16% higher than MPV, boll number about 20% higher than MPV, and at 40 days showed higher plant weight, shoot height, and root length than MPV

- Evidence type: phenotype comparison
- Method: field phenotyping; MPV comparison
- Data type: yield and growth traits
- Figure/table anchor: Fig. 1; Table S1; Fig. S1
- Confidence: high
- Limitation: complete field design and replicate details not fully visible in provided text

### Finding 2
> [!info] Source-reported content
> Most F1 genes were additive, but 697-1426 genes or 10-22% were non-additively expressed across stages; MH and SM had more upregulated than downregulated F1 MPV-DEGs

- Evidence type: transcriptomic evidence
- Method: RNA-seq differential expression
- Data type: mRNA expression
- Figure/table anchor: Fig. 2; Table S2/S3; Fig. S2-S5
- Confidence: moderate-high
- Limitation: differential expression does not establish causal contribution to heterosis

### Finding 3
> [!info] Source-reported content
> High-parental ELD accounted for 72% in MH, 78% in SM, and 58% in 1DPA; a subset overlapped MPV-DEGs

- Evidence type: transcriptomic evidence
- Method: ELD classification; GO/KEGG enrichment
- Data type: mRNA expression
- Figure/table anchor: Fig. 3
- Confidence: moderate
- Limitation: ELD is classified from expression profiles and not functionally perturbed

### Finding 4
> [!info] Source-reported content
> Parental genomes were resequenced, allelic SNPs were used to distinguish parental allele contributions, and the paper reports substantial allelic expression trans-regulation

- Evidence type: allele-specific expression evidence
- Method: genome resequencing; SNP-based allelic expression; cis/trans effect classification
- Data type: allelic mRNA expression
- Figure/table anchor: Fig. 4
- Confidence: moderate
- Limitation: full statistical details require methods/supplement manual check

### Finding 5
> [!info] Source-reported content
> More than 74.3% of 24-nt siRNA clusters colocalized with TEs; 2-kb flanking regions had more clusters than gene-coding regions; DE 24-nt siRNA clusters were associated with subsets of nonadditively expressed MPV-DEGs

- Evidence type: small RNA/genome annotation evidence
- Method: small RNA-seq; siRNA cluster calling; genomic colocalization
- Data type: small RNA reads; genome annotation; gene expression
- Figure/table anchor: Fig. 6
- Confidence: moderate
- Limitation: colocalization and differential expression do not prove direct regulation

### Finding 6
> [!info] Source-reported content
> The abstract and results report that transposable elements correlated with siRNA clusters in F1 had higher methylation levels but lower expression levels

- Evidence type: small RNA/methylome/transcriptome integration
- Method: small RNA-seq; bisulfite sequencing; TE expression analysis
- Data type: siRNA clusters; methylation; TE expression
- Figure/table anchor: Fig. 6 and methylome-related sections
- Confidence: moderate
- Limitation: correlation among siRNA, methylation, and expression is not direct causality

## 作者结论
作者明确认为，多组学数据提示表观遗传机制和基因表达模式变化可以为异源四倍体棉花杂种优势提供解释。作者还认为，F1 中高水平 24-nt siRNA、DNA 甲基化变化、TE 表达降低、miRNA 靶基因调控和高亲表达偏向共同构成可能影响 hybrid vigour 的机制框架。

## 谨慎推断
> [!caution] Reasonable inference
> - The observed high-parental ELD pattern may suggest that F1 preferentially retains or approximates higher parental expression states for some heterosis-related genes.
> - The association between increased 24-nt siRNA, TE methylation, and reduced TE expression is consistent with RdDM-linked TE repression in the hybrid.
> - miRNA repression in F1 could indicate altered post-transcriptional regulation of developmental and stress-related genes, but individual miRNA-target effects remain uncertain without validation details.

## 模型综合
> [!abstract] Model synthesis
> 这篇文章更像是一个“杂种优势的多组学关联图谱”，而不是单一因果因子的功能验证研究。其核心模型可以概括为：F1 通过基因表达的非加性重组和高亲表达偏向改变生长、能量和激素相关通路，同时 24-nt siRNA 和 DNA 甲基化变化可能限制 TE 活性并调节邻近基因表达。这一模型为后续功能验证提供候选通路、候选 miRNA/siRNA clusters 和候选表观遗传区域。

## 可复用知识

### Concepts
- [[heterosis]]
- [[MPV-DEGs]]
- [[additive/non-additive expression]]
- [[expression level dominance]]
- [[allele-specific expression]]
- [[cis/trans regulation]]
- [[RdDM]]
- [[24-nt siRNA clusters]]
- [[TE methylation]]

### Methods
- [[Field and developmental-stage phenotyping]]
- [[Field and growth trait phenotyping]]
- [[RNA-seq differential expression analysis]]
- [[mRNA transcriptome profiling and MPV-DEG analysis]]
- [[Expression level dominance classification]]
- [[ELD classification]]
- [[SNP-based allele-specific expression and cis/trans regulation analysis]]
- [[Allele-specific expression and cis/trans effect classification]]
- [[Small RNA sequencing and siRNA cluster analysis]]
- [[small RNA-seq and 24-nt siRNA cluster profiling]]
- [[miRNA identification, target prediction, and correlation]]
- [[known/novel miRNA profiling and target analysis]]

### Datasets
- cotton F1 hybrid and parental multi-omics data
- raw sequence data reported under BioProject PRJNA973929 in provided text

### Analytical frameworks
- integrate transcriptome
- small RNAome
- methylome
- TE annotation
- and phenotype to generate candidate heterosis mechanisms

### Experimental designs
- compare F1 against MPV and individual parents across developmental stages

## 局限性
- 没有在 provided text 中看到针对关键 siRNA/miRNA/DMR 的遗传扰动或反向验证，因此机制多为关联性。
- Methods S1 未在 MinerU `full.md` 中完整展开，样本处理、部分参数、qRT-PCR 验证细节需要 manual PDF check。
- Figure/table anchor uncertain，原因是 MinerU 输出中没有独立 `images/`/`tables/` 目录，图表与正文关系需人工核对。
- miRNA target 以预测和表达相关为主，不能直接等同于经实验证明的靶向关系。
- F1 是一个特定杂交组合，结论外推到其他 cotton hybrids 或其他作物需谨慎。

## 开放问题
- 哪些具体 24-nt siRNA clusters 或 DMRs 对产量/生长优势有可验证的因果贡献？
- high-parental ELD 是杂种优势的原因、结果，还是与其他调控层共同出现的标记？
- miRNA repression 在 F1 中是否通过已验证靶基因改变激素或防御通路？
- TE methylation/expression changes 是否直接影响邻近 protein-coding genes 的表达？
- 该模型在其他 cotton hybrids、不同环境或不同发育阶段中是否稳定？

## 关联笔记
- Concepts: [[heterosis]], [[MPV-DEGs]], [[additive/non-additive expression]], [[expression level dominance]], [[allele-specific expression]], [[cis/trans regulation]], [[RdDM]], [[24-nt siRNA clusters]], [[TE methylation]]
- Methods: [[Field and developmental-stage phenotyping]], [[Field and growth trait phenotyping]], [[RNA-seq differential expression analysis]], [[mRNA transcriptome profiling and MPV-DEG analysis]], [[Expression level dominance classification]], [[ELD classification]], [[SNP-based allele-specific expression and cis/trans regulation analysis]], [[Allele-specific expression and cis/trans effect classification]], [[Small RNA sequencing and siRNA cluster analysis]], [[small RNA-seq and 24-nt siRNA cluster profiling]], [[miRNA identification, target prediction, and correlation]], [[known/novel miRNA profiling and target analysis]]
- Evidence: [[2023-Hamid-Cotton-Heterosis claims]]
- Questions: [[2023-Hamid-Cotton-Heterosis open questions]]
