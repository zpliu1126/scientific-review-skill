# Cited Literature Mining Rules

## Purpose

The Cited Relevant Literature Mining Module identifies topic-relevant references cited by a full-text paper and turns them into traceable seed papers for the next literature discovery round. It is backward citation mining. It is not full-text evidence curation of the cited papers.

## When To Use

Use this module when:

- A user is doing single-paper PDF full-text close reading.
- The reading card should also list relevant cited papers.
- The user wants to recover classic or core papers missed by keyword search.
- The user wants seed papers for candidate_papers.csv, need_fulltext.md, evidence matrices, functional gene curation, regulatory network curation, or mechanism review writing.

## Source Sections To Inspect

Inspect at least:

- Introduction
- Results
- Discussion
- References

Methods may also be inspected when the topic depends on a specialized assay, dataset, mapping population, model organism, or analysis method. References-only matches are allowed, but they should be lower confidence unless the reference title clearly matches the topic.

## Relevance Inclusion Rules

Keep a cited paper if it satisfies at least one condition:

1. It is directly related to the current topic.
2. It reports a related functional gene.
3. It reports a related regulatory relationship.
4. It reports a related pathway, mechanism, or metabolic branch.
5. It reports a key experimental method or detection technology needed for the topic.
6. It reports evidence in the target species or an important model species.
7. It is important for the current paper's research design, candidate gene choice, or mechanism model.
8. It is a classic foundation paper in the field.
9. It is an original research paper that should be downloaded for later full-text verification.
10. It is a high-quality review useful for reference mining, while remaining review / background only.

## Exclusion Rules

Exclude:

- Generic statistics, software, sequencing-platform, database, or package citations unless the user explicitly needs methods literature.
- Broad background papers unrelated to the current topic.
- Vague citation strings whose title or source cannot be resolved, except as entries in need_reference_verification.md.
- References cited only for rhetorical background when they do not help discover evidence for the topic.
- Review papers that do not provide useful primary-study leads.

## Citation Context Requirement

Every retained cited paper must record citation context:

- cited section: Introduction / Methods / Results / Discussion / References only
- the sentence-level or paragraph-level reason the current paper cited it
- the topic relevance
- whether the current paper used it as background, method support, candidate-gene rationale, comparison, mechanism support, or review synthesis

Do not quote long passages. Paraphrase the context briefly.

## Paper Type And Evidence Role

Use these paper types:

- original research
- review
- method
- dataset/resource
- unknown

Use these evidence roles:

- background
- functional gene evidence
- regulatory relationship
- pathway mechanism
- phenotype evidence
- method reference
- dataset/resource
- review for reference mining

Review papers can be useful leads, but they must not be treated as primary experimental evidence.

## Priority Rules

- Priority A: strong topic relevance; likely original functional, mechanistic, regulatory, target-species, or classic evidence; must download full text.
- Priority B: relevant and likely useful; should download full text after Priority A.
- Priority C: background, conceptual, auxiliary, review-only, or lower direct relevance.
- Priority D: not worth processing now.

Priority is a discovery priority, not an evidence strength score.

## Metadata Rules

- Do not invent title, authors, year, journal, DOI, PMID, species, genes, methods, or conclusions.
- If metadata is incomplete, write `[需要核实]` or `unknown`.
- If reference parsing fails, add the citation string to need_reference_verification.md.
- If a DOI or PMID is missing from the current PDF but can be verified from a reliable source, mark the source of verification in notes. If not verified, keep `[需要核实]`.

## Deduplication Rules

Deduplicate by:

1. DOI
2. PMID
3. normalized title plus year

If two records may be the same paper but metadata conflicts, do not merge silently. Add the conflict to need_reference_verification.md.

If the same cited paper is cited by multiple current papers, keep one global record and append all source papers to `cited_by_current_paper`.

## Output Paths

Default output:

```text
literature-notes/cited-literature/
```

If the current workflow has a topic directory, write under:

```text
literature-notes/plant-gene-network-curation/{topic}/cited_references/
```

Expected structure:

```text
cited_references/
├── per_paper/
│   └── {paper_slug}_cited_relevant_literature.md
├── cited_reference_inventory.csv
├── cited_reference_inventory.md
├── cited_reference_priority_list.md
└── need_reference_verification.md
```

## Relationship To Literature Discovery

The global cited_reference_inventory.csv can seed the next literature discovery round.

Workflow chain:

```text
Full-text Paper Reading
-> Cited Relevant Literature Mining
-> cited_reference_inventory.csv
-> merge into candidate_papers.csv
-> update need_fulltext.md
-> next-round full-text evidence curation
```

When merging into candidate_papers.csv, label the source basis as `cited-reference lead` unless the cited paper metadata, abstract, or full text has been independently checked.

## Evidence Boundary

- Cited references are leads, not verified evidence.
- Do not add functional genes, regulatory edges, mechanisms, or phenotypes from cited references to formal evidence tables until their full texts are read.
- Do not turn the current paper's characterization of a cited paper into the cited paper's full conclusion.
- Keep original research and review/background references separate.

## Quality Check

After each full-text paper:

- A deep reading card was generated for the current paper.
- A cited relevant literature table was generated for the current paper.
- The full References section was not mechanically copied.
- Every retained cited paper has a relevance reason and citation context.
- Original research and review papers are distinguished.
- Cited references were not treated as verified full-text evidence.
- Missing DOI/PMID/year/journal/title fields are marked `[需要核实]` or `unknown`.
- Priority A/B cited papers were added to the global cited_reference_inventory.csv.
- The global inventory was checked against candidate_papers.csv and papers/ when available.
- need_reference_verification.md was updated for ambiguous or failed parses.
