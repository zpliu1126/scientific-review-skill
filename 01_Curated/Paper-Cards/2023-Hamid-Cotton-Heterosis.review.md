---
type: curated-paper-card
source: mineru
curation_skill: scientific-review-skill
title: Dynamic roles of small RNAs and DNA methylation associated with heterosis in allotetraploid cotton (Gossypium hirsutum L.)
authors: Rasmieh Hamid; Feba Jacob; Zahra Ghorbanzadeh; Leila Jafari; Omran Alishah
year: 2023
journal: BMC Plant Biology
doi: 10.1186/s12870-023-04495-2
study_type: primary research; multi-omics association study
field: plant epigenomics; crop heterosis; cotton
topics: [small RNA, DNA methylation, heterosis, cotton, transcriptomics, miRNA, siRNA]
source_basis: full.md + content_list.json
evidence_strength: moderate; multi-omics observational evidence with phenotype association
curation_status: curated; needs manual PDF check
mineru_dir: mineru-parsed/Hamid_2023_BMC Plant Biology
created: 2026-06-07
updated: 2026-06-07
---

# Dynamic roles of small RNAs and DNA methylation associated with heterosis in allotetraploid cotton (Gossypium hirsutum L.)

## 1. Citation metadata

- Title: Dynamic roles of small RNAs and DNA methylation associated with heterosis in allotetraploid cotton (Gossypium hirsutum L.)
- Authors: Rasmieh Hamid; Feba Jacob; Zahra Ghorbanzadeh; Leila Jafari; Omran Alishah
- Year: 2023
- Journal: BMC Plant Biology
- DOI: 10.1186/s12870-023-04495-2
- Article type: primary research

## 2. Source basis

本凝练基于 MinerU 解析目录 `mineru-parsed/Hamid_2023_BMC Plant Biology`：

- `full.md`
- `content_list.json`
- `meta.json`
- Parser note: standardized output directory does not contain separate `images/` or `tables/` folders, although `full.md` includes image links, figure captions, and some extracted table-like blocks; figure/table anchor uncertain; needs manual PDF check.

## 3. One-sentence takeaway

本文在陆地棉杂交种及亲本中整合表型、转录组、小 RNA 组和甲基化组数据，提出杂种优势与高亲表达偏向、24-nt siRNA、DNA 甲基化和 TE 表达变化之间存在关联。

## 4. Research question

本文试图回答：在异源四倍体棉花中，F1 杂种优势是否伴随基因表达重组、小 RNA 表达变化和 DNA 甲基化变化，以及这些组学变化是否与产量和生长优势相关。

## 5. Study design

研究对象为陆地棉 `Gossypium hirsutum L.` 杂交组合：Latif 作为母本、Taban 作为父本，产生 F1 hybrid。作者先比较两年田间性状和 20、40、60 天发育阶段的生长参数，随后选择 squaring stage 相关样本进行下游多组学分析。

数据类型包括：

- 表型数据：铃数、纤维产量、总籽棉产量、鲜重/干重、shoot weight、shoot/root length。
- mRNA-seq：F1 与双亲在 match-head (MH)、square growth midpoint (SM)、1DPA ovule 的花芽/胚珠样本，三次生物学重复。
- small RNA-seq：27 个 sRNA-seq libraries，用于 miRNA 和 24-nt siRNA profiling。
- bisulfite sequencing：SM stage methylome profiling。
- genome resequencing：用于 parental allele discrimination 和 cis/trans regulatory analysis。

样本量、田间重复设计、完整统计模型和 qRT-PCR 验证细节在 provided text 中未完整报告；Methods S1 被提及但未在 MinerU `full.md` 中完整展开，需 manual PDF check。

## 6. Key methods

- Field and growth trait phenotyping: 用于判定 F1 相对 mid-parent value (MPV) 的杂种优势。
- RNA-seq differential expression analysis: 比较 F1 与 MPV、双亲间表达差异，并识别 additive/non-additive expression。
- Expression level dominance (ELD) classification: 将 F1 表达与亲本表达水平比较，识别 high-parental ELD 和 low-parental ELD。
- SNP-based allele-specific expression and cis/trans effect analysis: 使用亲本重测序和转录组 SNP 区分 F1 中亲本等位基因贡献。
- small RNA sequencing: 识别 21-nt/24-nt small RNAs、24-nt siRNA clusters、known/novel miRNAs。
- miRNA target prediction and expression correlation: 预测 miRNA targets，并报告 miRNA 与 target expression 的负相关。
- Whole-genome bisulfite sequencing: 分析 CG/CHG/CHH methylation、DMRs、allele-specific methylation。
- TE/gene-flanking-region integration: 比较 24-nt siRNA clusters、TE methylation、TE expression 和基因表达关系。

## 7. Main findings with anchors

### Finding 1

- Source-reported content: F1 hybrid 由 Latif x Taban 产生，总籽棉产量比 MPV 高 16%，铃数约比 MPV 高 20%；40 天时 F1 的 plant weight、shoot height、root length 分别比 MPV 高 36.7%、18.33%、22.38%。
- Figure/table/section anchor if available: Results, "F1 hybrid shows significant morphological heterosis"; Table S1; Fig. 1a-d; Fig. S1.
- Evidence type: field/growth phenotype comparison.
- Limitation: complete field design and replicate information not fully visible in provided text.
- Confidence level: high for source-reported phenotype values; moderate for generalization beyond this hybrid.

### Finding 2

- Source-reported content: RNA-seq showed most genes in F1 were additive, but 10-22% genes showed non-additive expression; MH and SM stages had more upregulated than downregulated F1 MPV-DEGs; parental DEGs overlapped substantially with F1 MPV-DEGs.
- Figure/table/section anchor if available: Results, "F1 hybrid have more actively expressed genes than its parents"; Fig. 2; Table S2/S3; Fig. S2-S5.
- Evidence type: transcriptome differential expression.
- Limitation: DEGs are associations with hybrid phenotype, not direct causal tests.
- Confidence level: moderate to high for expression pattern; moderate for mechanistic interpretation.

### Finding 3

- Source-reported content: Among ELD genes, high-parental ELD accounted for 72% (MH), 78% (SM), and 58% (1DPA), and a subset overlapped F1 MPV-DEGs; authors state these findings imply high-parental ELD plus nonadditive mechanisms may contribute to heterosis.
- Figure/table/section anchor if available: Results, "Importance of high-parental expression level dominance in hybrid performance"; Fig. 3.
- Evidence type: expression classification and GO/KEGG enrichment.
- Limitation: ELD contribution is inferential and not genetically perturbed.
- Confidence level: moderate.

### Finding 4

- Source-reported content: 24-nt siRNA clusters were broadly detected across chromosomes, more than 74.3% colocalized with TEs, and 2-kb flanking regions contained more clusters than gene-coding regions. F1-associated TEs correlated with siRNA clusters had higher methylation and lower expression.
- Figure/table/section anchor if available: Results, small RNA profiling and genomic distribution; Fig. 6; supplementary figures/tables referenced in text.
- Evidence type: small RNA-seq, TE annotation, methylome/expression integration.
- Limitation: correlation among siRNA, methylation, and TE expression does not prove causal silencing.
- Confidence level: moderate.

### Finding 5

- Source-reported content: Authors identified 105 known miRNAs from 65 families; 83 known miRNAs from 38 families were non-additively expressed. Novel miRNAs were more often downregulated than upregulated in F1, and predicted targets included developmental, stress, hormone, and transcription factor related genes. A negative Pearson correlation was reported between known miRNAs and target gene expression.
- Figure/table/section anchor if available: Results, "MiRNAs are non-additively repressed more in the F1 hybrid".
- Evidence type: small RNA-seq, target prediction, expression correlation.
- Limitation: target prediction and expression correlation require experimental validation to support direct regulatory interactions.
- Confidence level: moderate for miRNA expression; low to moderate for individual target regulation.

## 8. Author conclusions

作者明确认为，多组学数据提示表观遗传机制和基因表达模式变化可以为异源四倍体棉花杂种优势提供解释。作者还认为，F1 中高水平 24-nt siRNA、DNA 甲基化变化、TE 表达降低、miRNA 靶基因调控和高亲表达偏向共同构成可能影响 hybrid vigour 的机制框架。

## 9. Reasonable inference

- The observed high-parental ELD pattern may suggest that F1 preferentially retains or approximates higher parental expression states for some heterosis-related genes.
- The association between increased 24-nt siRNA, TE methylation, and reduced TE expression is consistent with RdDM-linked TE repression in the hybrid.
- miRNA repression in F1 could indicate altered post-transcriptional regulation of developmental and stress-related genes, but individual miRNA-target effects remain uncertain without validation details.

## 10. Model synthesis

这篇文章更像是一个“杂种优势的多组学关联图谱”，而不是单一因果因子的功能验证研究。其核心模型可以概括为：F1 通过基因表达的非加性重组和高亲表达偏向改变生长、能量和激素相关通路，同时 24-nt siRNA 和 DNA 甲基化变化可能限制 TE 活性并调节邻近基因表达。这一模型为后续功能验证提供候选通路、候选 miRNA/siRNA clusters 和候选表观遗传区域。

## 11. Limitations and missing controls

- 没有在 provided text 中看到针对关键 siRNA/miRNA/DMR 的遗传扰动或反向验证，因此机制多为关联性。
- Methods S1 未在 MinerU `full.md` 中完整展开，样本处理、部分参数、qRT-PCR 验证细节需要 manual PDF check。
- Figure/table anchor uncertain，原因是 MinerU 输出中没有独立 `images/`/`tables/` 目录，图表与正文关系需人工核对。
- miRNA target 以预测和表达相关为主，不能直接等同于经实验证明的靶向关系。
- F1 是一个特定杂交组合，结论外推到其他 cotton hybrids 或其他作物需谨慎。

## 12. Reusable knowledge

- Concepts: heterosis; MPV-DEGs; additive/non-additive expression; expression level dominance; allele-specific expression; cis/trans regulation; RdDM; 24-nt siRNA clusters; TE methylation.
- Methods: multi-stage phenotyping; RNA-seq differential expression; ELD classification; SNP-based allele-specific expression; small RNA-seq; miRNA discovery; bisulfite sequencing; DMR analysis; TE/sRNA/methylation integration.
- Datasets: cotton F1 hybrid and parental multi-omics data; raw sequence data reported under BioProject PRJNA973929 in provided text.
- Experimental designs: compare F1 against MPV and individual parents across developmental stages.
- Analytical frameworks: integrate transcriptome, small RNAome, methylome, TE annotation, and phenotype to generate candidate heterosis mechanisms.

## 13. Open questions

- 哪些具体 24-nt siRNA clusters 或 DMRs 对产量/生长优势有可验证的因果贡献？
- high-parental ELD 是杂种优势的原因、结果，还是与其他调控层共同出现的标记？
- miRNA repression 在 F1 中是否通过已验证靶基因改变激素或防御通路？
- TE methylation/expression changes 是否直接影响邻近 protein-coding genes 的表达？
- 该模型在其他 cotton hybrids、不同环境或不同发育阶段中是否稳定？
