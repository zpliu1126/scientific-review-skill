# Cited Reference Inventory Template

Use this template for the global cited-reference outputs under:

```text
cited_references/
```

or, when no topic directory exists:

```text
literature-notes/cited-literature/
```

## cited_reference_inventory.csv

CSV header:

```csv
cited_id,cited_title,authors,year,journal,DOI,PMID,cited_by_current_paper,current_paper_DOI,topic,relevance_reason,evidence_role,priority,full_text_status,already_in_candidate_papers,already_in_papers_dir,need_fulltext,need_verification_notes
```

Rules:

- Use one row per unique cited paper.
- Deduplicate by DOI first, PMID second, then normalized title plus year.
- If the same cited paper is cited by multiple source papers, merge rows and append all source papers in `cited_by_current_paper`.
- `full_text_status` vocabulary: not collected / in papers dir / read as full text / user notes only / abstract only / unknown.
- `already_in_candidate_papers`, `already_in_papers_dir`, and `need_fulltext` use yes / no / unknown.
- Missing DOI, PMID, year, journal, or title must be written as `[需要核实]` or `unknown`.

## cited_reference_inventory.md

| cited_id | Cited title | Authors | Year | Journal | DOI | PMID | Cited by current paper | Current paper DOI | Topic | Relevance reason | Evidence role | Priority | Full text status | In candidate papers | In papers dir | Need full text | Verification notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CR-0001 | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | background / functional gene evidence / regulatory relationship / pathway mechanism / phenotype evidence / method reference / dataset/resource / review for reference mining | A / B / C / D | unknown | unknown | unknown | yes / maybe / no | Mark original research / review / method / dataset/resource / unknown here when needed. |

## cited_reference_priority_list.md

Use this file to queue cited references for full-text acquisition.

### Priority A: Download and Read First

| Rank | cited_id | Title | Authors | Year | Evidence role | Why Priority A | DOI/PMID | Already in papers dir | Need full text | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
|  | CR-0001 | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | unknown | yes |  |

### Priority B: Download After Priority A

| Rank | cited_id | Title | Authors | Year | Evidence role | Why Priority B | DOI/PMID | Already in papers dir | Need full text | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
|  | CR-0002 | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | [需要核实] | unknown | yes / maybe |  |

## need_reference_verification.md

Use this file for failed parses, incomplete metadata, ambiguous references, uncertain duplicate matches, or unclear citation context.

| Source paper | Citation string | Problem | Current best guess | Action needed |
|---|---|---|---|---|
| [需要核实] | [需要核实] | missing title / ambiguous year / DOI missing / PMID missing / unclear journal / uncertain relevance / duplicate conflict | [需要核实] | verify metadata before adding to candidate papers or evidence tables |

## Merge Into candidate_papers.csv

When the user asks to merge cited-reference leads into the literature discovery workflow:

1. Import Priority A/B rows with `need_fulltext = yes` or `maybe`.
2. Map `relevance_reason` to the candidate-paper `Notes` or `Evidence signal` field.
3. Preserve `source basis` as `cited-reference lead` unless metadata or abstract has been independently checked.
4. Do not upgrade cited-reference leads to abstract-level or full-text evidence without checking the cited paper.
5. Keep cited_id in notes or an auxiliary column when possible so the lead remains traceable.
