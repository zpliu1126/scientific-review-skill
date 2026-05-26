# Scientific Review Skill

Scientific Review Skill helps an AI agent read life science literature, compare evidence across papers, and draft review materials without fabricating citations or blurring source-reported content, reasonable inference, and model synthesis. It is a general life science review skill with domain-specific support for plant and crop science, population and evolutionary genomics, molecular biology, omics studies, animal models, human genetics, and biomedical evidence.

## What It Supports

- Single-paper close reading
- Multi-paper evidence matrices
- Review outlines organized by scientific claims
- Review paragraph drafting with citation traceability
- Explicit separation of source-reported content, reasonable inference, and model synthesis
- General review scoping, evidence grouping, controversy synthesis, and gap analysis
- Plant and omics evidence interpretation, including RNA-seq, DEG, GO/KEGG, WGCNA, qRT-PCR/qPCR, population genomics, comparative genomics, and functional validation boundaries
- Animal and human evidence interpretation, including cell models, animal models, cohorts, iPSC, organoids, and clinical validation boundaries

## Core Safety Rules

- Never invent references, DOI, PMID, author names, journal names, years, figures, species, cultivars, treatments, methods, statistics, results, pathways, or conclusions.
- Mark missing support as `[source needed]`; mark unverified but available support as `[needs verification]`.
- Distinguish source-reported content, reasonable inference, and model synthesis.
- State whether the analysis is based on full text, abstract, metadata, user notes, or searched sources.
- Preserve uncertainty, limitations, conflicting findings, and evidence quality.

## Directory Structure

```text
scientific-review-skill/
├── SKILL.md
├── README.md
├── agents/
├── assets/
├── prompts/
├── scripts/
├── templates/
├── examples/
└── references/
```

`assets/` and `scripts/` are reserved for future reusable assets and deterministic validators. They are intentionally unused in the current version.

## Suggested Use

Ask the agent to use this skill when working with life science papers, plant science, crop science, molecular biology, genetics, population genomics, evolutionary genomics, comparative genomics, stress physiology, transcriptomics, omics studies, animal or human functional genetics, candidate genes, functional validation, or review writing.

Example:

```text
Use scientific-review-skill to create an evidence matrix for these five papers on drought-responsive transcription factors in rice transcriptome studies.
```

## Important Limitation

This skill improves evidence handling and writing structure. It does not replace expert scientific review, clinical judgment, statistical review, or verification against original full-text sources.
