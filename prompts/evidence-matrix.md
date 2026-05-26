# Evidence Matrix Prompt

```text
Compare the provided life science papers using scientific-review-skill. Apply the general review evidence rules. For plant, crop, population genomics, evolutionary genomics, comparative genomics, transcriptomics, animal, human, or biomedical papers, apply the relevant domain-specific reference.

Create an evidence matrix with columns:
- Citation
- Source basis
- Study type
- Biological system
- Intervention/exposure/condition
- Data type
- Analysis method
- Key methods
- Main findings
- Source-reported content
- Reasonable inference
- Model synthesis
- Validation evidence
- Causality level
- Strengths
- Limitations
- Relevance to the review question
- Confidence level

After the matrix, summarize:
1. Areas of convergence.
2. Areas of disagreement.
3. Methodological differences that may explain disagreement.
4. Evidence gaps.
5. Claims that still need citations.

Rules:
- Do not force a consensus.
- Do not add papers that were not provided or verified.
- Mark unsupported claims as [source needed].
- Do not treat DEG, GO/KEGG enrichment, WGCNA, qRT-PCR/qPCR expression validation, selection scans, synteny, cell-line perturbation, animal models, or clinical association as stronger evidence than they are.
```
