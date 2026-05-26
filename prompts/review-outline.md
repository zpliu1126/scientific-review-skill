# Review Outline Prompt

```text
Build a scientific review outline for the topic below using scientific-review-skill.

Save-output mode:
If the user asks to "save to file", "保存到文件", "写入 notes", "生成文献卡片文件", or equivalent, save the full outline as a Markdown file. Use literature-notes/ as the recommended default directory. Use a concise descriptive Markdown filename and use unknown for missing metadata rather than inventing it. After saving, respond in chat only with the saved path, a brief summary, and Evidence Check status.

Topic:
[insert topic]

Available sources:
[insert papers, abstracts, notes, or matrix]

Output:
- Proposed title
- Scope and boundaries
- Central thesis, labeled as draft if inferential
- Section-by-section outline
- For each section:
  - Purpose
  - Core claims
  - Supporting sources already available
  - Sources still needed
  - Controversies or uncertainties
  - Domain-specific variables if relevant, such as species, cultivar, tissue, stress treatment, population, cohort, model system, omics platform, validation evidence, and functional evidence level
  - Suggested figures/tables

Rules:
- Organize by scientific claims, mechanisms, and evidence gaps, not only by paper chronology.
- Separate source-reported content, reasonable inference, and model synthesis.
- Do not invent references.
- For omics-heavy reviews, distinguish expression association, pathway enrichment, co-expression, qRT-PCR/qPCR validation, population/comparative genomic evidence, and functional validation.
- For animal or human reviews, distinguish cellular evidence, animal model evidence, human cohort evidence, and clinical or therapeutic validation.
- Save-output mode does not weaken citation integrity, source tracing, evidence tiering, or missing-information labels.
```
