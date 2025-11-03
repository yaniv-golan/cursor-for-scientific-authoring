---
title: Endgame: Journal‑Ready Output
status: draft
---

# Endgame: Journal‑Ready Output

Draft. Assemble, audit, package.

- Match author guidelines and templates
- Final citation audit; figure/table checks
- Reproducibility bundle (data/code/prompts/diffs)
- Preprint vs submission packaging

Google Docs collaboration (optional)
- If collaborators prefer Google Docs, you can paste your Markdown into Docs and enable Tools → Preferences → “Automatically detect Markdown” so headings, lists, emphasis, and links auto‑convert to formatted text.[^google-docs-markdown]
- Use this as a review copy; keep Markdown in your repo as the source of truth. When edits land in Docs, ask the agent to reconcile back into your Markdown files as diffs.
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

Change log
- 2025-11-03: Added Google Docs collaboration (Markdown auto‑convert) with limits and source‑of‑truth reminder.
- 2025-11-03: Added optional equation numbering guidance (LaTeX and pandoc-crossref paths).
