# Review Paragraph Prompt

```text
Draft review paragraphs using scientific-review-skill.

Input:
- Review section:
- Intended claim:
- Available sources:
- Preferred citation style:
- Target audience:

Output:
1. Draft paragraph.
2. Claim-to-source map.
3. Source-reported content used.
4. Reasonable inference used, if any.
5. Model synthesis used, if any.
6. Unsupported statements that need sources.

Rules:
- Every factual claim must trace to an available source or be marked [source needed].
- Do not invent citations.
- Use cautious language for mechanism, causality, or translational implications unless directly supported.
- Do not turn DEG, GO/KEGG, WGCNA, qRT-PCR/qPCR, population/comparative genomics, cell-line perturbation, animal model, or clinical association evidence into causal claims without appropriate validation.
```
