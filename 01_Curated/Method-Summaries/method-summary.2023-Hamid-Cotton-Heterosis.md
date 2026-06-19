# Methods extracted from Paper

Paper ID: `2023-Hamid-Cotton-Heterosis`

Source basis: `mineru-parsed/Hamid_2023_BMC Plant Biology/full.md` and `content_list.json`. Methods S1 is referenced but not fully available in the MinerU text; needs manual PDF check.

## Method list

### Field and developmental-stage phenotyping

- Method name: Field and growth trait phenotyping
- Purpose: 判断 Latif x Taban F1 是否表现产量和生长杂种优势，并选择后续组学分析阶段。
- Input material/data: F1 hybrid, maternal Latif, paternal Taban; yield and growth traits at 20, 40, and 60 days.
- Output: seed cotton yield, boll number, fresh/dry weight, shoot weight, shoot/root length, MPV comparison.
- Key parameters: MPV comparison; significance noted as P < 0.01 for Fig. 1 caption.
- Strengths: 先以实际表型确定杂种优势，再进入组学分析。
- Limitations: 田间重复、环境、完整统计模型在 provided text 中未完整展开。
- Used in which result: Finding 1; Fig. 1; Table S1; Fig. S1.

### RNA-seq differential expression analysis

- Method name: mRNA transcriptome profiling and MPV-DEG analysis
- Purpose: 比较 F1 与 MPV/双亲之间的表达差异，识别 additive 和 non-additive expression。
- Input material/data: flower bud samples at MH, SM, and 1DPA ovule; three biological replicates; 62-84 million reads per library reported.
- Output: expressed genes, MPV-DEGs, M-F DEGs, additive/non-additive expression classes.
- Key parameters: high-quality read mapping to G. hirsutum reference genome; |log2 FC| threshold and P/FDR thresholds reported in text for some comparisons.
- Strengths: 多阶段、多重复转录组设计。
- Limitations: 不能单独证明表达变化导致杂种优势。
- Used in which result: Finding 2; Fig. 2; Table S2/S3; Fig. S2-S5.

### Expression level dominance classification

- Method name: ELD classification
- Purpose: 判断 F1 表达水平是否接近某一亲本，特别是 high-parental ELD。
- Input material/data: F1 and parental RNA-seq expression values.
- Output: ELD-F, ELD-M, high-parental ELD, low-parental ELD, overlap with MPV-DEGs.
- Key parameters: 12 expression classes referenced from prior classification framework.
- Strengths: 可把杂交后表达模式与亲本表达差异联系起来。
- Limitations: 分类本身是描述性/关联性，不是功能验证。
- Used in which result: Finding 3; Fig. 3.

### SNP-based allele-specific expression and cis/trans regulation analysis

- Method name: Allele-specific expression and cis/trans effect classification
- Purpose: 区分 F1 中两个亲本等位基因表达贡献，并分析 cis/trans regulation。
- Input material/data: parental genome resequencing, exonic SNPs, F1 transcriptome reads.
- Output: parental allele expression estimates, cis/trans effect categories.
- Key parameters: parental genomes resequenced; transcripts containing allelic SNPs in genome and transcriptome used for read mapping and comparison.
- Strengths: 提供 F1 等位基因层面的表达调控信息。
- Limitations: SNP calling、read assignment 和统计细节需 manual PDF check。
- Used in which result: Finding 4; Fig. 4.

### Small RNA sequencing and siRNA cluster analysis

- Method name: small RNA-seq and 24-nt siRNA cluster profiling
- Purpose: 识别 F1 和双亲中 small RNA size classes、24-nt siRNA clusters 及其基因组分布。
- Input material/data: 27 sRNA-seq libraries; small RNA reads from hybrid and parents.
- Output: 21-nt/24-nt sRNA profiles, 24-nt siRNA clusters, TE/gene/flanking-region colocalization.
- Key parameters: 24-nt clusters; genomic windows/regions including TEs and 2-kb flanking regions.
- Strengths: 与 TE 和基因附近区域整合，适合研究 RdDM 相关候选机制。
- Limitations: cluster 与表达或甲基化的关联不能直接证明因果。
- Used in which result: Finding 5; Fig. 6.

### miRNA identification, target prediction, and correlation

- Method name: known/novel miRNA profiling and target analysis
- Purpose: 分析 F1 中 miRNA 的非加性表达及其潜在靶基因功能。
- Input material/data: small RNA reads; predicted target genes; matched gene expression profiles.
- Output: known miRNAs, novel miRNAs, predicted targets, miRNA-target expression correlation.
- Key parameters: P <= 0.01 and FDR <= 0.05 reported for non-additive expression; Pearson negative correlation reported for known miRNA-target expression.
- Strengths: 将 miRNA 表达与潜在调控功能连接。
- Limitations: target prediction 不是靶向验证；需降解组、reporter 或 genetic perturbation 支持。
- Used in which result: Finding 7; miRNA results section.

### Whole-genome bisulfite sequencing and methylome integration

- Method name: Bisulfite sequencing and DMR/methylation analysis
- Purpose: 分析 F1 与双亲在 CG/CHG/CHH context 中的甲基化差异，并与 ASE、TE、siRNA、gene expression 关联。
- Input material/data: SM-stage DNA methylome libraries; genome reference.
- Output: methylation profiles, DMRs, allele-specific methylation associations, TE methylation associations.
- Key parameters: 1641 million clean reads, average 150 bp; 82.25% uniquely mapped; >10-fold coverage; >99% conversion efficiency; replicate Pearson 0.92-0.96 reported.
- Strengths: 覆盖度和转换效率信息较完整，适合和 small RNA/transcriptome 整合。
- Limitations: 甲基化与表达关联仍需功能扰动验证。
- Used in which result: methylome-related findings; abstract and conclusion.
