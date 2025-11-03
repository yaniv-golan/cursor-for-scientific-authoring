---
title: "Endgame: Journal‑Ready Output"
layout: default
grand_parent: Guide
parent: Core
nav_order: 80
---


# Endgame: Journal‑Ready Output

Draft. Assemble, audit, package.

- Match author guidelines and templates
- Final citation audit; figure/table checks
- Reproducibility bundle (data/code/prompts/change previews)
- Preprint vs submission packaging

Google Docs collaboration (optional)
- If collaborators prefer Google Docs, you can paste your Markdown into Docs and enable Tools → Preferences → “Automatically detect Markdown” so headings, lists, emphasis, and links auto‑convert to formatted text.[^google-docs-markdown]
- Use this as a review copy; keep Markdown in your repo as the source of truth. When edits land in Docs, ask the agent to reconcile back into your Markdown files with a clear preview of changes.
- Limits: code blocks and math may not convert; for equations, prefer the PDF/LaTeX export path or keep math in Markdown and summarize in Docs.

Equation numbering (optional)
- Choose one path based on your export target.
- PDF (LaTeX engine): use raw LaTeX with labels and references.
  - Example: `\begin{equation}\label{eq:ols} 
    \hat{\beta}=(X^\top X)^{-1}X^\top y
    \end{equation}` and cite with `\eqref{eq:ols}`.
  - Requires exporting to PDF with a LaTeX engine (e.g., `xelatex`).
- Cross‑format (DOCX/HTML) via pandoc‑crossref (advanced):
  - Label: `$$ y = mx + b $$ {#eq:line}` and reference with `@eq:line`.
  - Requires the `pandoc-crossref` filter; propose it as optional and approval‑gated in agent prompts. Verify availability before use.

Notes
- Keep Core drafts simple; add numbering only if a venue requires it.
- Prefer review‑first prompts: ask the agent to propose commands/installs and wait for your approval before executing anything.

Assemble the manuscript
- Conform to the target journal’s section order, word/figure limits, and template. Keep Markdown as the source of truth; regenerate exports rather than editing exported files.
- Ensure headings, callouts, figures, and tables follow the patterns in [Writing in Markdown]({{ site.baseurl }}{% link guide/core/writing-markdown.md %}).
- Verify internal links resolve and paths are consistent. If you changed filenames, reconcile cross-references with a clear preview of changes.

Citations and references
- Re-run a citation audit. Confirm every in-text citation appears in `references/` and vice versa. Spot-check a few references against originals. See [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %}).
- Keep a minimal `references/` source (BibTeX or CSL JSON) and a single CSL style checked into the project. Avoid manual edits in exported DOCX reference lists; regenerate from Markdown.

Figures and tables
- Save submission-quality figures in `manuscript/figures/` and tables (CSV or Markdown) in `manuscript/tables/`. Confirm filenames and captions match citations in text.
- Check resolution, dimensions, and color requirements for the venue. Prefer vector (PDF/SVG) where allowed.

Reproducibility bundle
- Include inputs, scripts, and environment files from [Analysis]({{ site.baseurl }}{% link guide/core/analysis.md %}). Pin dependencies (e.g., `environment.yml`, `requirements.txt`, or `renv.lock`) and note any random seeds.
- Add a short `README.md` explaining how to re-run key analyses and where outputs are saved.
- Include a summary of major agent edits or merges with a clear preview of changes for traceability.

Exports (Pandoc examples)
- Ensure the output folder exists:
  ```bash
  mkdir -p dist
  ```
- DOCX (journal template):
  ```bash
  pandoc manuscript/sections/*.md \
    --from gfm --to docx \
    --csl references/style.csl \
    --bibliography references/library.bib \
    --reference-doc ops/templates/journal.docx \
    --output dist/paper.docx
  ```
- PDF (LaTeX engine):
  ```bash
  pandoc manuscript/sections/*.md \
    --from gfm --to pdf --pdf-engine=xelatex \
    --csl references/style.csl \
    --bibliography references/library.bib \
    --output dist/paper.pdf
  ```
- HTML (preprint site or lab page):
  ```bash
  pandoc manuscript/sections/*.md \
    --from gfm --to html5 \
    --csl references/style.csl \
    --bibliography references/library.bib \
    --css ops/templates/article.css \
    --output dist/paper.html
  ```

Final packaging prompt (copy/paste)
```text
Task: Prepare final submission and preprint packages from Markdown sources.

Safety rules:
- File-scoped changes only in manuscript/, references/, analysis/, and dist/.
- Propose any commands or installs first; wait for explicit approval.
- Do not move/rename files unless approved. No external uploads.

Steps:
1) Validate citations against references/library.bib; list any mismatches.
2) Verify figures/tables exist and are referenced; report any missing captions.
3) Propose pandoc commands for DOCX, PDF, and HTML. Use existing templates.
4) Assemble a reproducibility bundle (README, scripts, environment files).
5) Show a preview of changes (creates/edits) before applying.

Approval gate: Reply exactly CONFIRM APPLY to run commands and write outputs.

Files allowed to change:
- dist/** (new exports)
- analysis/reports/** (auto summaries)
- manuscript/figures/**, manuscript/tables/** (if re-saved)
- references/** (no destructive changes; add missing CSL/Bib)
```

What’s next
- Continue to [Checklists]({{ site.baseurl }}{% link guide/core/checklists.md %}) to run final verification before publishing.

Change log
- 2025-11-03: Added Google Docs collaboration (Markdown auto‑convert) with limits and source‑of‑truth reminder.
- 2025-11-03: Added optional equation numbering guidance (LaTeX and pandoc-crossref paths).
- 2025-11-03: Added exports (Pandoc), reproducibility bundle, a packaging prompt, and What’s next; marked page complete.

[^google-docs-markdown]: Google Docs Editors Help, “Use Markdown in Google Docs, Slides, & Drawings,” https://support.google.com/docs/answer/12014036?hl=en (accessed 2025-11-03).
