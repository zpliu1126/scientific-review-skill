# Plant Functional Gene Network Curation Prompt

```text
Use scientific-review-skill to run the Plant Trait and Stress Functional Gene Network Curation Workflow.

Goal:
Curate plant genes and regulatory relationships for a specified trait, stress response, or biological topic, then build a traceable preliminary functional gene network with Cytoscape-ready node and edge tables.

Required inputs:
- Topic: nitrogen response, nitrogen use efficiency, drought stress, salt stress, cold stress, heat stress, phosphate starvation, ABA response, disease resistance, root architecture, flowering time, fiber development, yield traits, seed development, hormone signaling, or another plant trait/stress response.
- Species priority: Arabidopsis, rice, maize, wheat, cotton, soybean, tomato, or user-specified species.
- Evidence scope:
  - functional validation only
  - include candidate genes
  - include omics associations
  - include homolog-inferred genes
  - include regulatory network edges
- Input sources:
  - papers/
  - literature-notes/
  - user-provided gene list
  - user-provided DEG/WGCNA/GWAS/QTL table
  - public database notes, including gget-style gene, ortholog, sequence, or annotation outputs
  - SRA/GEO dataset notes or accession-linked paper notes
  - manually curated seed papers

Default output directory:
literature-notes/plant-gene-network-curation/

Required outputs:
- topic_scope.md
- plant_functional_gene_inventory.csv
- plant_functional_gene_inventory.md
- plant_regulatory_edge_table.csv
- plant_regulatory_edge_table.md
- network_nodes_for_cytoscape.csv
- network_edges_for_cytoscape.csv
- network_model.md
- gene_cards/
- need_verification.md

Workflow:
0. Run literature discovery when needed.
   - If the user only provides a topic or has not collected PDFs/full text, first use prompts/plant-literature-discovery.md.
   - Generate search_strategy.md, candidate_papers.csv, candidate_papers.md, fulltext_priority_list.md, and need_fulltext.md under literature-notes/plant-gene-network-curation/literature_discovery/.
   - Do not treat candidate paper metadata or abstracts as full-text evidence.
   - Enter full-text evidence curation only after PDFs, extracted text, or verified full-text notes are available.

0.5. Run PDF structure parsing when PDFs are available.
   - Use prompts/pdf-structure-parsing.md before extracting genes, functional evidence, regulatory edges, cited-reference leads, figure/table evidence, or methods details from PDFs.
   - Write topic workflow outputs to literature-notes/plant-gene-network-curation/{topic}/pdf_structure/.
   - Check parsing_manifest.csv before curation.
   - Preserve parser_used, parser_status, fallback_used, parser confidence, and section uncertainty in downstream evidence cards.
   - If Introduction is not stable, write [Introduction 标题未稳定识别，正文结构需人工复核] and continue as section-uncertain full-text reading when full text is available.

1. Define scope.
   - Record topic, species priority, input sources, evidence scope, inclusion/exclusion criteria, and source basis.
   - State whether evidence is based on full text, abstract, user notes, database notes, or omics tables.

2. Curate gene inventory.
   - Extract genes related to the topic.
   - Classify each gene as functionally validated gene, candidate gene, stress/trait-responsive gene, homolog-inferred gene, or database-annotated gene.
   - Assign one evidence level using references/plant-functional-gene-evidence-levels.md.
   - Every gene must have a source paper, database note, or user-provided source. Missing source means the gene must be placed in need_verification.md, not treated as curated evidence.

3. Curate regulatory and functional edges.
   - Extract regulatory, genetic, pathway, co-expression, homolog-inferred, and literature-inferred relationships.
   - Assign directness using references/plant-regulatory-edge-evidence-rules.md.
   - Every edge must have a source paper or source note.
   - Edges without a source must not enter the formal network edge table; put them in need_verification.md.

4. Build gene cards.
   - Generate one Gene Evidence Card for each important gene.
   - Separate source-reported function, experimental evidence, evidence level, mechanism, review use, unsupported claims, and verification needs.

5. Build preliminary network model.
   - Organize genes into modules such as signal perception, transcriptional regulation, transport, metabolism, hormone crosstalk, ROS/stress signaling, root/shoot development, yield/agronomic traits, and species-specific modules.
   - Separate high-confidence edges, medium-confidence edges, and candidate edges.
   - Write a Chinese text network model.
   - Generate a Mermaid network diagram using only sourced edges, with evidence level labels.

6. Export Cytoscape tables.
   - Generate network_nodes_for_cytoscape.csv using the required node fields.
   - Generate network_edges_for_cytoscape.csv using the required edge fields.

Evidence and wording rules:
- Do not write DEG, WGCNA, GO/KEGG, co-expression, selection signal, or qRT-PCR evidence as functional validation.
- Do not write co-expression as direct regulation.
- Do not write homolog inference as validated function in the target species.
- Treat database annotations, ortholog lookups, SRA/GEO metadata, and accession-linked notes as source leads unless primary experimental evidence is available.
- Do not treat review-article statements as primary experimental evidence unless the original paper has been checked.
- Do not invent DOI, PMID, gene ID, species, experiment, figure/table/page, regulatory relationship, or conclusion.
- Use unknown, [需要核实], or [source needed] for missing information.
- Distinguish Source-reported content, Reasonable inference, and Model synthesis in the final outputs.

Final quality check:
0. Does every PDF used for full-text curation have parser_used, fallback_used, text-layer status, structure_report, and explicit section statuses?
1. Does every gene have a source?
2. Does every edge have a source?
3. Were DEG, WGCNA, GO/KEGG, and co-expression kept below functional validation?
4. Were co-expression edges kept separate from direct regulatory edges?
5. Were homolog-inferred claims kept separate from target-species validation?
6. Were review-derived claims marked as secondary evidence unless primary sources were checked?
7. Does every formal edge include source paper and evidence support?
8. Does every high-confidence edge have experimental evidence?
9. Are missing DOI/PMID/figure/table/page values marked as [需要核实] or unknown?
10. Are Source-reported content, Reasonable inference, and Model synthesis clearly separated?

Chat response after saving files:
Return only the saved paths, one-sentence summary, and Evidence Check status unless the user requests the full content in chat.
```
