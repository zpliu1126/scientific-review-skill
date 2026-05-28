# Cited Relevant Literature Mining Prompt

Use this prompt after full-text reading of a PDF when the user wants the paper's relevant cited literature mined for the next discovery round. This is backward citation mining, not evidence curation of the cited papers.

```text
Run the Cited Relevant Literature Mining Module for the current full-text paper.

Inputs:
- Current paper full text:
- Current paper bibliographic metadata:
- Current topic or review question:
- Existing candidate_papers.csv, if available:
- Existing papers/ directory, if available:
- Output directory, if different from default:

Workflow:
1. Confirm the source basis is the current paper full text, extracted text, or verified full-text notes.
2. Define the current topic narrowly enough to screen cited references. If the topic is not explicit, infer it from the user's stated review goal and the current paper, and label it as inferred.
3. Read the Introduction, Results, Discussion, and References. Do not rely on the reference list alone.
4. Identify cited papers that match at least one relevance rule in references/cited-literature-mining-rules.md.
5. Exclude generic method, software, platform, database, or unrelated background references unless they are important to the user's topic.
6. For every retained cited paper, record the citation context from the current paper: section, what claim or method it supported, and why it is relevant.
7. Classify each retained cited paper as original research, review/background only, method reference, dataset/resource, or needs verification.
8. Assign Evidence role:
   - background
   - functional gene evidence
   - regulatory relationship
   - pathway mechanism
   - phenotype evidence
   - method reference
   - dataset/resource
   - review for reference mining
9. Assign Priority:
   - A: strong relevance; must download full text
   - B: relevant; should download full text
   - C: background or auxiliary
   - D: do not process now
10. Write the per-paper table using templates/cited-relevant-literature-table.md.
11. Update the global inventory using templates/cited-reference-inventory.md.
12. Deduplicate by DOI, PMID, or normalized title plus year. If the same cited paper is found from multiple source papers, merge it and append the source paper to cited_by_current_paper.
13. Compare with candidate_papers.csv and papers/ when available. Mark already_in_candidate_papers and already_in_papers_dir.
14. Add Priority A/B papers that still need full text to cited_reference_priority_list.md and, when appropriate, to need_fulltext.md in the literature discovery workflow.
15. Put incomplete, ambiguous, or failed reference parses in need_reference_verification.md.

Output:
- per_paper/{paper_slug}_cited_relevant_literature.md
- cited_reference_inventory.csv
- cited_reference_inventory.md
- cited_reference_priority_list.md
- need_reference_verification.md

Boundary rules:
- Do not mechanically copy the full References section.
- Do not treat cited papers as verified evidence until their full texts are read.
- Do not add genes, edges, pathways, mechanisms, or phenotypes from cited papers into formal evidence tables unless the cited paper has been read or independently verified.
- If DOI, PMID, year, journal, title, or citation context is incomplete, write [需要核实].
- Keep review papers clearly labeled as review / background only.
```

