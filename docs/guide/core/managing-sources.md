---
title: Managing Sources And Local Corpora
layout: default
grand_parent: Guide
parent: Core
nav_order: 40
---


# Managing Sources And Local Corpora

Who this is for: researchers organizing PDFs, notes, and datasets so agents stay grounded.

Keep agents grounded and reduce hallucinations by organizing sources, writing synthesis notes the agent can reliably use, and referencing files precisely with `@file` instead of ad‑hoc chat memory.[^cursor-forum-prompts]

Goals
- Organize PDFs, notes, and data artifacts so agents can retrieve the right context
- Create synthesis notes that summarize and cite reliably
- De‑duplicate sources and keep a single bibliographic source of truth in `references/`

Recommended folders (adapt to your project)
- `references/`: bibliographies (BibTeX `.bib` or CSL JSON), citation style files (`.csl`), and reference lists
- `sources/` or `data/external/`: PDFs and third‑party datasets (read‑only originals)
- `notes/`: human‑authored synthesis notes (Markdown)
- `claims.md`: a simple claims log for non‑obvious assertions and their sources (see Accuracy)

Synthesis notes the agent can trust
- Create a per‑topic or per‑paper note in `notes/` with: a 3–5 sentence summary, 2–3 key quotes (with page numbers), and a short “how this supports our argument” line.
- Use headings keyed to questions you’ll ask later (e.g., “Definition of [term]”, “Reported effect sizes”).
- Paraphrase carefully and always add an inline citation (and page numbers for quotes); log non‑obvious claims in `claims.md`.

Precise `@file` references
- Reference concrete files in prompts instead of generic `@codebase`. Label context precisely (e.g., `@notes/related-work.md`, `@references/library.bib`) so the reranker retrieves the right material.[^cursor-forum-prompts]
- Keep prompts file‑scoped when asking for edits; this produces clear, reviewable changes and prevents context drift.

Bibliography and citations
- Choose one library of record in `references/` (BibTeX or CSL JSON). Connect citations in your manuscript to this file; see Writing in Markdown for citation syntax and export.
- Include page/section numbers for direct quotes and figure/table citations.
- Run regular citation audits: scan for missing keys, unresolved references, and fabricated entries.

De‑duplication and source hygiene
- Normalize filenames with stable slugs (e.g., `smith2021-transformer-biology.pdf`); avoid spaces. You can ask the agent to propose these changes for you (see automation below).
- Deduplicate PDFs and references by DOI/URL. Keep exactly one copy of each source in read‑only storage, and reference it from notes/manuscript. Ask the agent to outline a dry‑run plan first before making any changes.

Automate with agents (simple & safe)
- Use this minimal prompt. It keeps things safe and simple—no special steps.

```text
Task: Normalize filenames and flag duplicates in sources/ safely.

Safety rules:
- Read-only first. Do not change anything until I reply exactly: CONFIRM APPLY
- Never delete. If needed, propose moving dupes to sources/_duplicates/
- Only touch sources/ and update links in notes/ if I confirm
- Do not edit manuscript/ or references/

Step 1 — Dry run (show only):
- Propose new slugs: list lines as "old → new" (e.g., Smith_2021_final.pdf → smith2021-transformer-biology.pdf)
- Flag duplicates by DOI/URL and by checksum; for uncertain matches, ask me a question
- Summarize counts: to-rename, likely-dupes, unknown
- List any risks or ambiguities in one short paragraph

Step 2 — On my explicit "CONFIRM APPLY":
- Rename/move files exactly as listed; create sources/_duplicates/ as needed
- Update only notes/ links that point to renamed files
- Print a plain text log of actions and an undo list (new → old)

If anything is unclear, stop and ask up to two clarifying questions before proceeding.
```

Advanced (optional) — structured review
- For larger teams or scripted reviews, you can ask for a structured checklist and a proposed change list to review before applying. Keep the same safety rules (no deletes; scope to `sources/` and `notes/`). Use only if your team prefers a reviewable artifact.
- Avoid dumping huge, uncurated corpora; prefer a curated set with high‑quality synthesis notes.

File‑scoped prompt patterns
- “From `sources/` PDFs `paper-a.pdf` and `paper-b.pdf`, extract definitions of [term] into `notes/definitions.md`. Add quotes with page numbers and a 2–3 sentence paraphrase. Update `claims.md` with any non‑obvious assertions.”
- “Scan `notes/` for duplicated claims/citations. Propose specific changes to merge overlaps; do not delete unique content. Keep edits file‑scoped and show a clear preview of changes.”

Optional — build a notes index (approval-gated)

```text
Task: Create or update notes/_index.md with a one-line summary for each curated source.

Safety rules:
- Read-only scan first. Do not write files until I reply exactly: CONFIRM APPLY
- Only write to: notes/_index.md
- Do not modify manuscript/**, references/**, sources/**

Steps:
1) Scan notes/** for per-paper or per-topic notes. Extract title, year (if present), and the first summary sentence.
2) Prepare a preview of notes/_index.md entries as lines: "slug — Title (Year): summary sentence".
3) Wait for my reply: CONFIRM APPLY before writing notes/_index.md
```

Cross‑links
- Quick Start: {{ site.baseurl }}{% link guide/core/quick-start.md %}
- Accuracy: {{ site.baseurl }}{% link guide/core/accuracy.md %}
- Writing in Markdown: {{ site.baseurl }}{% link guide/core/writing-markdown.md %}
- Analysis patterns: {{ site.baseurl }}{% link guide/core/analysis.md %}
- Project rules (AGENTS.md): {{ site.baseurl }}{% link guide/core/project-rules.md %}
- Data governance: {{ site.baseurl }}{% link resources/data-governance.md %}

What’s next
- Proceed to Data Governance and Privacy: {{ site.baseurl }}{% link resources/data-governance.md %}

Change log
- 2025-11-03: Added audience one‑liner.
- 2025-11-03: Marked complete; added an optional approval-gated prompt to build a notes index; kept file-scoped constraints and cross-links.
- 2025-11-03: Reworded to avoid jargon (YAML/diffs/patch/manifest) in Core; advanced option now describes a plain‑language structured review.
- 2025-11-03: Added agent automation (dry‑run manifest + patch) for slug normalization and dedup; clarified approval flow.
- 2025-11-03: First draft with folder recommendations, synthesis notes, precise `@file` usage, de‑dup hygiene, prompt patterns, and cross‑links.

[^cursor-forum-prompts]: Cursor Community Forum, “Cursor prompt engineering best practices,” https://forum.cursor.com/t/cursor-prompt-engineering-best-practices/1592 (accessed 2025-11-03).
