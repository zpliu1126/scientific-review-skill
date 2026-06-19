# Methods extracted from Paper

Paper ID: `2015-Song-Cotton-Ovule-Fiber-Methylation`

Source basis: `mineru-parsed/Song_2015_PLOS Genetics/full.md` and `content_list.json`.

## Method list

### Plant material and developmental sampling

- Method name: Cotton tissue sampling
- Purpose: 比较 leaf、ovule 和 fiber 发育阶段的 methylome/transcriptome/sRNAome。
- Input material/data: Gossypium hirsutum L. acc. TM-1; leaves; ovules at 0 DPA; fibers at 14 DPA; ovules at 14 DPA.
- Output: tissue-specific samples for sequencing.
- Key parameters: MethylC-seq used two biological replicates for leaves/0 DPA ovules/14 DPA fibers and one replicate for 14 DPA ovules as reported in Results.
- Strengths: 直接覆盖 ovule-to-fiber developmental transition.
- Limitations: 14 DPA ovule replication requires manual check.
- Used in which result: Findings 1-9.

### MethylC-seq / whole-genome bisulfite sequencing

- Method name: MethylC-seq library construction and methylcytosine calling
- Purpose: 测定 CG/CHG/CHH methylation patterns。
- Input material/data: genomic DNA from cotton tissues.
- Output: methylated cytosines, methylation levels, DMRs.
- Key parameters: bisulfite conversion >99%; cytosines covered by at least three reads used for analysis; Bismarck alignment; binomial test P < 1e-5 for methylcytosines.
- Strengths: genome-wide base-resolution methylation profiling.
- Limitations: repetitive allopolyploid genome may complicate unique mapping.
- Used in which result: Findings 1-4, 8.

### CHH DMR identification

- Method name: 100-bp sliding-window CHH DMR calling
- Purpose: 识别 ovule-leaf and fiber-ovule CHH hypermethylated regions。
- Input material/data: CHH methylation calls across tissues.
- Output: OL CHH-hyper DMRs and FO CHH-hyper DMRs.
- Key parameters: windows with at least eight CHH cytosines covered by at least three reads; ANOVA P < 0.05; methylation difference cutoff >0.1 between compared samples; cutoff 0.05 for ovule/fiber comparison in OL DMRs.
- Strengths: explicit window and coverage criteria.
- Limitations: window size and cutoffs can affect DMR boundaries.
- Used in which result: Findings 3-6.

### Bisulfite validation of selected DMRs

- Method name: cloned-fragment bisulfite sequencing validation
- Purpose: 验证 genome-wide DMR calls。
- Input material/data: selected DMR genomic fragments.
- Output: targeted methylation validation.
- Key parameters: not fully reported in provided text.
- Strengths: provides orthogonal support for DMR calls.
- Limitations: validation subset size and loci require manual PDF check.
- Used in which result: Finding 3; S3 Fig.

### small RNA-seq

- Method name: small RNA sequencing and abundance analysis
- Purpose: 分析 24-nt siRNA abundance and distribution relative to genes/TEs/DMRs。
- Input material/data: leaves, 0 DPA ovules, 14 DPA fibers with three replicates.
- Output: small RNA size profiles; siRNA density; promoter/TE siRNA levels.
- Key parameters: mapped to TM-1 genome; detailed filters not fully summarized in provided text.
- Strengths: supports RdDM-related interpretation of CHH methylation.
- Limitations: siRNA abundance is correlative without RdDM mutant perturbation.
- Used in which result: Findings 1, 2, 4, 5.

### RNA-seq and gene/TE expression analysis

- Method name: mRNA-seq differential expression
- Purpose: 关联 DMRs with gene expression and TE expression。
- Input material/data: RNA-seq reads from cotton tissues.
- Output: DEGs, TE expression, expression quartiles, homoeolog expression bias.
- Key parameters: TopHat mapping; Cufflinks quantification; DEGs identified by fold-change >2 and ANOVA P < 0.01.
- Strengths: integrates methylation with expression.
- Limitations: transcriptome association does not prove methylation causality.
- Used in which result: Findings 4-6, 9.

### Homoeolog identification and methylation-expression comparison

- Method name: A/D homoeolog identification and bias analysis
- Purpose: 分析 A and D subgenome homoeolog methylation differences and expression bias。
- Input material/data: A and D homoeolog protein sequences and gene expression/methylation data.
- Output: homoeolog pairs with differential methylation and expression differences.
- Key parameters: blastp E-value < 1e-10; MCScanX score >2000 and E-value < 1e-10; expression fold-change >2; methylation cutoffs shown in Fig. 5 caption.
- Strengths: useful for allopolyploid subgenome regulation.
- Limitations: correlation only; homoeolog mapping can be sensitive to genome annotation.
- Used in which result: Finding 9; Fig. 5.

### qRT-PCR of methylation pathway genes

- Method name: qRT-PCR expression profiling
- Purpose: 检测 GhCMT2, GhMET1, GhCMT3, RdDM genes and HISTONE H1 in tissues。
- Input material/data: RNA from leaf, ovule, fiber.
- Output: relative expression of DNA methylation-related genes.
- Key parameters: cotton HISTONE H3 used as internal control; ANOVA P < 0.05 in figure caption.
- Strengths: pathway-gene expression support for methylation interpretation.
- Limitations: indirect evidence; not equivalent to enzyme activity or genetic perturbation.
- Used in which result: Finding 7; Fig. 4F.

### In vitro ovule culture and 5-aza-dC treatment

- Method name: DNA methylation inhibitor perturbation
- Purpose: 测试 DNA methylation inhibition 对 cotton fiber development 的影响。
- Input material/data: ovules removed from flower buds at -3 or 0 DPA.
- Output: fiber cell number/length, ovule size, SEM/phenotypic images.
- Key parameters: Beasley-Ting liquid medium with 5 uM IAA and 0.5 uM GA3 at 30 deg C for 4-14 days in dark; 5-aza-dC at 10 mg/L.
- Strengths: direct perturbation of methylation status during fiber development.
- Limitations: 5-aza-dC may have growth-inhibition side effects and is not pathway-specific.
- Used in which result: Finding 8; Fig. 4G-I.
