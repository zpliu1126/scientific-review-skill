# Methods extracted from Paper

Paper ID: `2023-Liang-Phased-siRNAs-Speciation`

Source basis: `mineru-parsed/Liang_2023_Science/full.md` and `content_list.json`. Supplementary Materials and Methods are referenced but not fully expanded in the MinerU text; needs manual PDF check.

## Method list

### Fine-scale genetic mapping and NIL construction

- Method name: Genetic mapping with near-isogenic lines
- Purpose: 将 YUP 定位到较小 genomic interval，并分离 YUP 与相邻 PELAN 的效应。
- Input material/data: M. parishii, M. cardinalis, BC/selfing populations, NILs.
- Output: 70-kb YUP candidate interval; Mpar yupC/C and Mlew yupC/C NILs.
- Key parameters: about 3000 BC3S1/BC3S2 individuals genotyped.
- Strengths: 高分辨率定位并结合表型重组材料。
- Limitations: marker-level details require supplementary manual check.
- Used in which result: Finding 1; Fig. 1I.

### Protein-coding candidate RNAi screen

- Method name: RNA interference of interval protein-coding genes
- Purpose: 测试 70-kb interval 中 8 个 protein-coding genes 是否影响 carotenoid pigmentation。
- Input material/data: candidate genes in YUP interval; M. lewisii transgenic/RNAi lines.
- Output: no carotenoid pigmentation phenotype for tested protein-coding genes.
- Key parameters: not reported in provided text.
- Strengths: 排除 obvious protein-coding candidates，推动寻找 noncoding gene。
- Limitations: RNAi knockdown efficiency not fully visible; negative evidence depends on knockdown quality.
- Used in which result: Finding 2; fig. S3.

### RNA-seq/transcript inspection and hairpin prediction

- Method name: Candidate noncoding transcript identification
- Purpose: 在 candidate interval 中寻找非编码转录本和潜在 hairpin。
- Input material/data: RNA sequencing reads mapped to YUP interval; genome sequence.
- Output: about 1.3-kb transcript; no conserved ORF; inverted repeat with about 250-bp arm; homology to CYP450 5' UTR/exon fragment.
- Key parameters: BLAST comparison to genome.
- Strengths: 将结构来源和 small RNA substrate 可能性连接起来。
- Limitations: exact transcript boundaries require manual check.
- Used in which result: Finding 2; fig. S4-S6.

### sRNA-seq and phasing analysis

- Method name: small RNA sequencing and phased siRNA analysis
- Purpose: 判断 YUP inverted repeat 是否产生 phased siRNAs。
- Input material/data: whole corolla sRNA libraries from wild-type M. lewisii, M. parishii, and Mpar yupC/C NIL.
- Output: 21-nt siRNAs, phasing score, YUP_siR1/siR-RCP2 identification.
- Key parameters: TPM and phasing score; phasing calculation cited in figure caption.
- Strengths: 直接显示 small RNA 产物和相位模式。
- Limitations: library preparation and computational thresholds need supplementary check.
- Used in which result: Finding 3; Fig. 2A.

### qRT-PCR of siRNA abundance

- Method name: qRT-PCR for YUP_siR1/siR-RCP2
- Purpose: 验证 siRNA 在不同物种、发育阶段和组织中的积累模式。
- Input material/data: corolla developmental stages, floral organs, leaves, transgenic lines.
- Output: relative abundance of YUP_siR1/siR-RCP2.
- Key parameters: three technical replicates for several panels; one-way ANOVA or Student's t test in figure captions.
- Strengths: 补充 sRNA-seq 的组织和发育分辨率。
- Limitations: normalization details not reported in main MinerU text.
- Used in which result: Findings 3, 4, 6, 8; Fig. 2-4.

### Transgenic YUP allele overexpression

- Method name: 35S-driven YUP allele overexpression
- Purpose: 测试 M. lewisii/M. parishii/M. cardinalis YUP alleles 是否能够改变 flower carotenoid phenotype。
- Input material/data: about 1.3-kb YUP transcripts from three species; Mpar DPKC/C NIL.
- Output: dark pink/no carotenoid phenotype for dominant alleles; no phenotypic change for M. cardinalis allele.
- Key parameters: 30, 35, and 41 independent lines reported for M. lewisii, M. parishii, and M. cardinalis constructs.
- Strengths: 强功能验证，包含 allele contrast 和较多独立转基因线。
- Limitations: constitutive promoter may not capture endogenous spatial regulation.
- Used in which result: Finding 4; Fig. 2D-G.

### Target validation by 5' RLM RACE

- Method name: RNA ligase-mediated 5' rapid amplification of cDNA ends
- Purpose: 验证 siR-RCP2 是否在预测位点切割 RCP2 transcripts。
- Input material/data: RCP2 transcripts from M. lewisii.
- Output: cleavage positions at predicted target site.
- Key parameters: clone proportions shown in Fig. 3A.
- Strengths: 直接支持 small RNA-guided transcript cleavage。
- Limitations: precise clone counts need figure manual check.
- Used in which result: Finding 5; Fig. 3A.

### Artificial siRNA overexpression

- Method name: 35S:amiR-RCP2 transgenic assay
- Purpose: 测试 siR-RCP2 本身是否足以抑制 carotenoid accumulation。
- Input material/data: artificial siR-RCP2 construct; orange-flowered Mpar DPKC/C NIL.
- Output: subset of transgenic lines shifted to dark pink/no carotenoid phenotype; increased siR-RCP2 abundance.
- Key parameters: 6 of 21 lines with phenotype; 17- to 43-fold siR-RCP2 increase in strong lines.
- Strengths: 将 YUP locus effect 缩小到特定 siRNA。
- Limitations: phenotype appears expression-dependent.
- Used in which result: Finding 6; Fig. 3B-D.

### RCP2-YFP and siRNA-resistant target-site reporter assay

- Method name: RCP2 translational repression reporter
- Purpose: 判断 siR-RCP2 是否除 transcript cleavage 外还抑制 RCP2 translation。
- Input material/data: 35S:RCP2-YFP and 35S:mRCP2-YFP constructs; silent mutations in siR-RCP2 target site.
- Output: petal lobe/filament YFP signal comparison; carotenoid accumulation patterns.
- Key parameters: at least three flowers per line for YFP signal confirmation in figure caption.
- Strengths: 靶位点突变使 translational repression 证据较强。
- Limitations: reporter transgene context differs from endogenous locus.
- Used in which result: Finding 7; Fig. 3E-H.

### Comparative genomics and synteny analysis

- Method name: Synteny and evolutionary origin analysis
- Purpose: 推断 YUP-SOLAR-PELAN superlocus 的起源时间和谱系限制性。
- Input material/data: chromosome-level and fragmentary Mimulus genome assemblies; additional species genome sequencing.
- Output: superlocus presence/absence across sections; estimated origin about 5 MYA.
- Key parameters: about 10 flanking genes upstream/downstream used in synteny figure.
- Strengths: 将功能 locus 放入 phylogenetic context。
- Limitations: fragmentary assemblies and manually linked contigs require manual check.
- Used in which result: Finding 8; Fig. 5.
