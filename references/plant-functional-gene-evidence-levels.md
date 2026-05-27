# Plant Functional Gene Evidence Levels

Use these levels when curating plant functional genes for trait, stress, developmental, hormone, omics, population-genomic, comparative-genomic, or molecular-breeding topics. Assign the strongest level that is directly supported by the available source. Do not upgrade a claim using inference alone.

## Level 1: Direct Regulatory or Mechanistic Evidence

Includes:
- ChIP-qPCR / ChIP-seq / DAP-seq.
- EMSA.
- Y1H.
- Dual-luciferase assay.
- Promoter activity assay.
- Protein-DNA or protein-protein interaction.
- Perturbation of a regulator plus target response.
- Functional phenotype supporting the mechanism.

Can support:
- Direct or mechanism-level claims when the assay, species, condition, and target are clear.
- Regulatory edges such as binds promoter of, trans-activates, represses, interacts with, or directly regulates.

Cannot support:
- Field or breeding value without agronomic validation.
- Universal conservation across species without cross-species evidence.
- Complete pathway causality if only one mechanistic link was tested.

## Level 2: Functional Genetic Evidence

Includes:
- Mutant.
- Overexpression.
- CRISPR / genome editing.
- Complementation.
- Transgenic validation.
- Clear trait or stress phenotype.

Can support:
- Functional involvement of a gene in the reported trait, stress, tissue, species, and genetic background.
- Stronger functional claims than expression or association evidence.

Cannot support:
- Direct regulation of a target gene unless direct regulatory assays are present.
- Exclusion of off-target, background, or expression-level artifacts without proper controls.
- Breeding value without field or population validation.

## Level 3: Genetic Mapping Plus Expression Evidence

Includes:
- GWAS.
- QTL.
- Fine mapping.
- Haplotype analysis.
- Allele validation.
- Expression or physiological support.

Can support:
- Candidate causal loci or alleles when mapping and expression/physiology evidence converge.
- Natural-variation or breeding-candidate claims with cautious wording.

Cannot support:
- Definitive gene function without perturbation or complementation.
- Direct regulatory edges without regulatory assays.
- Causal gene claims if the mapped interval contains unresolved candidates.

## Level 4: Omics Association Evidence

Includes:
- RNA-seq DEG.
- Proteomics.
- Metabolomics.
- WGCNA.
- Co-expression.
- Time-series network inference.
- GO/KEGG enrichment.

Can support:
- Treatment-responsive, trait-associated, module-associated, or pathway-associated candidate genes.
- Prioritization for future validation.

Cannot support:
- Functional validation.
- Direct regulation or causality.
- Mechanism proof without perturbation, biochemical, or genetic validation.

## Level 5: Weak or Indirect Evidence

Includes:
- Homolog inference.
- Database annotation.
- Review mention.
- Keyword match only.

Can support:
- Candidate inclusion, background context, and hypothesis generation.
- Cross-species leads when orthology is clearly stated and source-traceable.

Cannot support:
- Target-species functional validation.
- Direct mechanism, regulatory edge, or breeding application.
- Primary evidence claims when the only source is a review or database summary.

## Assignment Rules

- Use the lowest defensible level when evidence is ambiguous.
- Mark missing methods, figures, gene IDs, DOI/PMID, and experimental details as `[需要核实]`.
- If a gene has multiple evidence types, record all evidence types but assign the highest source-supported level.
- Do not combine two weak evidence types into a strong functional claim.
- Keep source-reported content, reasonable inference, and model synthesis separate.
