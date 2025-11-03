---
title: First‑Hour Guided Exercise
layout: default
parent: Getting Started
---


# First‑Hour Guided Exercise

Objective: in 60 minutes, create an IMRaD outline, one table, and a shareable export—entirely with file‑scoped prompts and auditable diffs. A figure is optional in the no‑code track.

Success criteria
- `manuscript/sections/00-outline.md` exists with IMRaD headings and citations.
- One Markdown table at `manuscript/tables/example.md` with a caption.
- Optional: one figure saved (no‑code: manual; low‑code: generated) with a caption.
- `claims.md` updated with any non‑obvious assertions to verify.
- A shareable export (Markdown recommended). PDF/DOCX export comes later.

Before you start (5 minutes)
- Open your paper workspace (a local folder you created—see example layout in `content/guide/core/quick-start.md`).
- Ensure Cursor is signed in and a model is selected in Composer.
- Create a minimal `AGENTS.md` that captures citation and accuracy rules (see `content/guide/core/project-rules.md`).

Part A — IMRaD outline from 3 PDFs (15–20 minutes)
1) Place three relevant PDFs under `data/raw/`.
2) Prompt (file‑scoped) to create `manuscript/sections/00-outline.md`:
   ```text
   Read the three PDFs in data/raw/. Extract the research
   questions, datasets, methods, and key findings. Draft an IMRaD
   outline in manuscript/sections/00-outline.md. Use footnotes for
   non-obvious claims and point them to references/ or entries in
   claims.md. Keep edits file-scoped and show a clear preview of
   changes.
   ```
3) Check that quotes/paraphrases have citations. Add gaps to
   `claims.md` for follow‑up (see `content/guide/core/accuracy.md`).

Part B — One table (10–15 minutes)
Choose your path:
- No‑code (default)
  1) Add a small CSV at `data/processed/example.csv`.
  2) Prompt (file‑scoped):
     ```text
     Read data/processed/example.csv and convert the first N rows and
     relevant columns into a clean Markdown table saved at
     manuscript/tables/example.md. Do not compute derived statistics
     yet—leave TODOs for Analysis. Add a short caption.
     ```
- Low‑code (optional)
  1) Add a small CSV at `data/processed/example.csv`.
  2) Prompt (file‑scoped):
     ```text
     Create analysis/notebooks/01-table.md that loads
     data/processed/example.csv, computes summary statistics, and
     writes a paper‑ready Markdown table to
     manuscript/tables/example.md. Use code to calculate; show code and
     outputs; explain the result in plain language. Save code in
     analysis/scripts/01-table.py (or .R).
     ```
     See content/guide/core/analysis.md.

Part C — Optional figure (10–15 minutes)
Choose your path:
- No‑code (default)
  1) Prompt (file‑scoped):
     ```text
     Write step‑by‑step instructions for making a
     [scatter/bar/line] chart from data/processed/example.csv in
     Numbers/Excel/Sheets (which columns, chart type, labels, units).
     Provide the figure caption text. I’ll create the chart manually
     and save as manuscript/figures/example.png.
     ```
- Low‑code (optional)
  1) Prompt (file‑scoped):
     ```text
     Create analysis/notebooks/02-figure.md that loads
     data/processed/example.csv and generates a figure saved to
     analysis/figures/example.png. Include code and the resulting plot
     preview; describe the figure in plain language. Save code in
     analysis/scripts/02-figure.py (or .R). If randomness is used, set
     a fixed seed.
     ```

Part D — Citation audit and export (10 minutes)
1) Audit citations (file‑scoped):
   ```text
   Scan manuscript/sections/ for quotations or paraphrases. Ensure
   each has a citation and a footnote that points to references/ or
   claims.md. Flag missing sources and list them in claims.md. Do not
   invent citations.
   ```
   See `content/guide/core/accuracy.md`.
2) Export a shareable draft:
   - Share Markdown directly for now (recommended in the first hour).
   - PDF/DOCX export (with bibliography and CSL) is covered in `content/guide/core/writing-markdown.md`.

Optional (advanced, file‑scoped agent prompt — review before running)
- Agents typically propose safe commands, but it’s good practice to review them first. If unsure, ask the agent to explain each step in plain language before approving.
```text
Check whether pandoc is installed. If not, propose safe install steps
for my OS without executing. Then draft a command to export the merged
manuscript to DOCX/PDF with --citeproc, my references/library.bib, and
references/style.csl. Show the exact command, explain each flag, and
wait for my approval before running.
```

Reproducibility and safety guardrails
- File‑scoped prompts; avoid ad‑hoc chat memory.
- No‑code path: restrict to transcription; mark derived calculations as TODOs for Analysis.
- Low‑code path: “use code to calculate”; show code and outputs; explain in plain language (`content/guide/core/analysis.md`).
- Set seeds for stochastic steps; save exact scripts under `analysis/scripts/`.
- Capture environments as lockfiles where applicable (e.g., `environment.yml`, `renv.lock`).
- Prefer local processing for sensitive data; see `content/policies/data-governance.md`.
- Track non‑obvious assertions in `claims.md` and cite accordingly.

Validation checklist
- Outline file present with citations; no obvious uncited paraphrases.
- Table file renders correctly in Markdown; caption is present and specific.
- If created, figure is saved and captioned; units and axes labeled.
- `claims.md` contains follow‑ups for any missing sources.
- If you chose to export, the file opens cleanly and includes citations formatted by your CSL.

Cross‑links
- Quick Start: `content/guide/core/quick-start.md`
- Writing in Markdown: `content/guide/core/writing-markdown.md`
- Accuracy and claims: `content/guide/core/accuracy.md`
- Analysis patterns: `content/guide/core/analysis.md`
- Data governance: `content/policies/data-governance.md`

What’s next
- Proceed to Writing in Markdown: `content/guide/core/writing-markdown.md`

Change log
- 2025-11-03: Marked complete after refinement; tightened guardrails and cross-links.
- 2025-11-03: Deferred PDF/DOCX export to Writing in Markdown; removed shell example; added optional agent prompt.
- 2025-11-03: Added success and validation criteria; Pandoc example; env lockfile note.
- 2025-11-03: First full draft added; step‑by‑step tasks, guardrails, cross‑links.
- 2025-11-03: Removed early provider/API-key details and repo-layout note.
