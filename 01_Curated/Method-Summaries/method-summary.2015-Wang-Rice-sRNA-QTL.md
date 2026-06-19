# Methods extracted from Paper

Paper ID: `2015-Wang-Rice-sRNA-QTL`

Source basis: `mineru-parsed/Wang_2015_eLife/full.md` and `content_list.json`.

## Method list

### IMF2 population sRNA profiling

- Method name: sRNA-seq in rice IMF2 population
- Purpose: Quantify sRNA abundance as molecular traits.
- Input material/data: 98 IMF2 hybrids, parents Zhenshan 97 and Minghui 63, F1; flag leaves.
- Output: 53,613,739 unique sRNAs and 165,797 s-traits.
- Key parameters: 18-26 nt reads; RPM >= 0.6 and expressed in more than 25 IMF2s for s-traits.
- Strengths: population-scale small RNA measurement.
- Limitations: single tissue/developmental stage.
- Used in which result: Findings 1-3.

### SNP-replaced genome mapping

- Method name: Parental SNP-replaced reference mapping
- Purpose: Improve mapping of sRNAs to parental genomes.
- Input material/data: sRNA reads and parental SNP-replaced reference genomes.
- Output: mapped sRNA categories and parental-specific sRNAs.
- Key parameters: unique location allowing no mismatch.
- Strengths: reduces mapping bias between parents.
- Limitations: repetitive sRNAs may be underrepresented.
- Used in which result: Finding 1.

### sQTL/scQTL mapping

- Method name: Composite interval mapping with R/qtl
- Purpose: Identify local and distant genetic loci controlling sRNA and sRNA cluster expression.
- Input material/data: s-traits, sc-traits, 1568-bin genotype map.
- Output: local-sQTLs, distant-sQTLs, scQTLs and hotspots.
- Key parameters: 1000 permutations; same map/parameters as e-trait QTL analysis.
- Strengths: quantitative genetics framework for sRNA abundance.
- Limitations: QTLs are associations until validated.
- Used in which result: Findings 2, 4, 5.

### Mother gene and expression correlation analysis

- Method name: sRNA-mother gene co-regulation analysis
- Purpose: Test whether sRNAs from the same gene and their mother genes are co-regulated.
- Input material/data: sRNA expression, mRNA expression, gene annotations.
- Output: correlation classes and co-regulation patterns.
- Key parameters: correlation thresholds around -0.3 and 0.3 reported for strong correlations.
- Strengths: separates sRNA regulation from precursor/mother gene regulation.
- Limitations: correlation cannot define mechanism.
- Used in which result: Finding 3.
