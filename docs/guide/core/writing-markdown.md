---
title: Writing In Markdown For Science
layout: default
grand_parent: Guide
parent: Core
nav_order: 20
---


# Writing In Markdown For Science

Who this is for: researchers who want clean, citable Markdown manuscripts without wrestling tools.

Goal: make Markdown your single source of truth for the manuscript, with clear structure (IMRaD), managed citations, and predictable exports—without surprising installs.

What this covers
- IMRaD scaffolding and section templates
- Figures, tables, equations, and callouts
- Citations with BibTeX or CSL JSON under `references/`
- Safe, review‑first export to DOCX/PDF via Pandoc (optional)

Before you start
- Use the minimal project layout from Quick Start: {{ site.baseurl }}{% link guide/core/quick-start.md %}.  
  [Download the starter project (zip)]({{ site.baseurl }}/assets/downloads/minimal-project.zip)
- Keep this repo’s layout (docs/content/raw) out of your paper project; it’s for this guide only.

IMRaD scaffolding
- Start from an outline file like `manuscript/sections/00-outline.md` (see a template in the starter project zip above).
- Use one Markdown file per section (e.g., `01-introduction.md`, `02-methods.md`, `03-results.md`, `04-discussion.md`).
- Prefer file‑scoped prompts when drafting or refining sections so edits remain auditable.

Example section skeleton
```
# Introduction

Problem and context. Cite prior work briefly [@smith2020]. State contributions.

## Related Work

Summarize strands; quote sparingly with citations.

# Methods

Describe data, procedures, and measures. For any numbers, use code to calculate and include code/outputs in an analysis notebook; summarize here.

# Results

Embed figures from `manuscript/figures/` and tables from `manuscript/tables/`. Interpret without overclaiming.

# Discussion

Limitations, implications, and future work.
```

Figures and tables
- Save paper‑ready figures to `manuscript/figures/` and tables to `manuscript/tables/`.
- Embed an image: `![Caption with units](../figures/figure-01.png)`.
- Include a Markdown table file via copy/paste or link; keep captions specific and informative.
- For numeric results that require computing, follow the pattern in {{ site.baseurl }}{% link guide/core/analysis.md %}: use code to calculate; show code and outputs; explain in plain language.

Agent help with figures and tables (friendly shortcuts)
- Tables (no‑code):
  ```text
  Read data/processed/example.csv and generate a clean Markdown table
  with columns [A, C, E]. Save to
  manuscript/tables/example.md and add a specific caption. Do not
  compute derived statistics.
  ```
- Tables (low‑code):
  ```text
  Create analysis/notebooks/01-table.md to load
  data/processed/example.csv, compute summary stats, and write a
  paper-ready table to manuscript/tables/example.md. Use code to
  calculate; show code and outputs. Save code in
  analysis/scripts/01-table.py (or .R).
  ```
- Figures (no‑code):
  ```text
  Write step-by-step instructions for making a [scatter/bar/line]
  chart from data/processed/example.csv in Numbers/Excel/Sheets,
  including which columns, labels, units, and a caption. I will save
  the output to manuscript/figures/example.png.
  ```
- Figures (low‑code):
  ```text
  Create analysis/notebooks/02-figure.md that loads
  data/processed/example.csv and saves a figure to
  analysis/figures/example.png. Explain what the figure shows in plain
  language. Save code under analysis/scripts/02-figure.py (or .R). Set
  a random seed if randomness is used.
  ```

Equations and callouts
- Inline math with `$...$` and display math with `$$...$$` (if your export route supports LaTeX math).
- Use callouts sparingly to highlight constraints or decisions.
 - Equation numbering is optional and covered later in Endgame.

Math basics (optional)
- Inline example: “The mean is `$\mu$` and the variance is `$\sigma^2$`.”
- Display example:

```
$$
\hat{\beta} = (X^\top X)^{-1} X^\top y
$$
```

Tips
- Do not wrap math in backticks; use `$`/`$$` delimiters.
- To show a literal dollar sign in text, escape it as `\$`.
- Export: PDF requires a LaTeX engine (see Export). For DOCX, preview to confirm equations render correctly; if not, prefer PDF or simplify the math.

Agent help with math (friendly shortcuts)
- You don’t need to memorize LaTeX. Ask the agent to draft or fix math for you.
- Try one of these file‑scoped prompts:
  ```text
  From this English description, write both inline and display math
  and explain symbols briefly: beta hat equals (X transpose X)
  inverse, times X transpose y.
  ```
  ```text
  Convert this equation into LaTeX, then check syntax and suggest a
  clearer layout: y = m x + b.
  ```
  ```text
  Review this LaTeX for mistakes and consistency. If anything is
  ambiguous, ask me questions: $$ y = mx + b $$.
  ```
- If your environment supports images (some models or extensions do), you can attach a screenshot of an equation and ask: “Transcribe this into Markdown/LaTeX. If any symbols are unclear, list assumptions and alternatives.” Verify image support in your setup first.

Citations and references
- Store bibliographic data in `references/` as either BibTeX (`library.bib`) or CSL JSON (`library.json`). Keep `references/` as the bibliographic source of truth.
- Cite with Pandoc syntax: `[@key]` for parenthetical, `@key` for narrative, and `[-@key]` to suppress author.
- Add page numbers with `[@key, p. 12]`.
- Maintain a simple `claims.md` log at your project root for non‑obvious assertions and verify them; see {{ site.baseurl }}{% link guide/core/accuracy.md %}.

<details>
<summary><strong>Export (review‑first, optional)</strong></summary>
- Share Markdown during early drafting (recommended). When you need DOCX/PDF:
  - Ensure you have a `.bib` or `.json` file under `references/` and a journal style CSL (e.g., `references/style.csl`).
  - If Pandoc is available, you can export with `--citeproc` to format citations.
  - Prefer asking the agent to propose commands and wait for approval rather than running installs automatically.

What is Pandoc? (for non‑programmers)
- Pandoc is a document converter. It takes your Markdown and produces formats like DOCX and PDF, while handling citations and reference styles via CSL.
- For PDF, Pandoc commonly uses a LaTeX engine (e.g., `xelatex`). DOCX usually works without extra tooling.
- You don’t need Pandoc to start writing—share Markdown during early drafts and add export tooling only when needed.

Google Docs bridge (Markdown support)
- If you collaborate in Google Docs, you can enable “Automatically detect Markdown” in Tools → Preferences. Pasting or typing common Markdown (headings, lists, emphasis, links) will auto‑convert to formatted text. Not all elements convert (e.g., code blocks or math), so review the result.[^google-docs-markdown]
- Some Docs builds also add Edit → “Paste from Markdown” and “Copy as Markdown.” If available, these commands make round‑tripping between Docs and your Markdown files easier. Availability can vary by account/rollout.
- Workflow: draft in Markdown → paste into Docs for comments (auto‑convert or Paste from Markdown) → when ready, use “Copy as Markdown” in Docs and ask the agent to reconcile the changes back into your Markdown files with a clear preview of changes.

Agent‑assisted export (review first)
- Agents generally propose safe commands, but review proposed actions like you would review suggested edits before running them—especially on machines with important data.
- If anything is unclear, ask the agent to explain each step in plain language before you approve.
- Suggested file‑scoped prompt:
  ```text
  Check whether pandoc is available. If not, propose OS-specific
  install steps without executing. Draft a command to export
  manuscript/sections/*.md to DOCX (and optionally PDF) with
  --citeproc, using references/library.bib (or library.json) and
  references/style.csl. Show the exact command, explain each flag, and
  wait for my approval before running.
  ```

Example commands (for review and manual execution)
- DOCX (adjust paths/styles):
```
pandoc manuscript/sections/*.md \
  --from gfm --to docx \
  --citeproc \
  --bibliography references/library.bib \
  --csl references/style.csl \
  -o export/draft.docx
```
- PDF requires a LaTeX engine (e.g., `xelatex`). If you have one installed:
```
pandoc manuscript/sections/*.md \
  --from gfm --to pdf \
  --pdf-engine xelatex \
  --citeproc \
  --bibliography references/library.bib \
  --csl references/style.csl \
  -o export/draft.pdf
```

Reproducibility guardrails

</details>
- Keep analysis code separate (under `analysis/`) and save generated figures/tables deterministically.
- Record seeds for any stochastic steps; save exact scripts under `analysis/scripts/`.
- Capture environments with lockfiles (small files that record exact package versions) where applicable (`environment.yml`, `renv.lock`).

Cross‑links
- [Quick Start]({{ site.baseurl }}{% link guide/core/quick-start.md %})
- [Accuracy and claims]({{ site.baseurl }}{% link guide/core/accuracy.md %})
- [Managing sources]({{ site.baseurl }}{% link guide/core/managing-sources.md %})
- [Analysis patterns]({{ site.baseurl }}{% link guide/core/analysis.md %})
- [Data governance]({{ site.baseurl }}{% link resources/data-governance.md %})
- [First‑hour exercise]({{ site.baseurl }}{% link getting-started/first-hour.md %})

What’s next
- [Proceed to Accuracy →]({{ site.baseurl }}{% link guide/core/accuracy.md %})

Change log
- 2025-11-03: Added audience one‑liner; fixed front matter formatting.
- 2025-11-03: Standardized long prompt examples to fenced code blocks for easy copy/paste.
- 2025-11-03: Marked complete; added in-file footnote for Google Docs Markdown support and tightened export/math notes.
- 2025-11-03: Expanded Google Docs bridge with “Paste from Markdown” / “Copy as Markdown” and a round‑trip workflow.
- 2025-11-03: Added Google Docs bridge note with Markdown support and source citation.
- 2025-11-03: Added agent help with math prompts and image-transcription option (environment-dependent).
- 2025-11-03: Added "Math basics" with examples, tips, and export notes for non-experts.
- 2025-11-03: First substantial draft: IMRaD scaffolds, citations, safe export prompts, reproducibility guardrails, and cross‑links.

[^google-docs-markdown]: Google Docs Editors Help, “Use Markdown in Google Docs, Slides, & Drawings,” https://support.google.com/docs/answer/12014036?hl=en (accessed 2025-11-03).
