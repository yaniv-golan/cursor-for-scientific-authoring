---
title: Workflows
status: complete
---

# Workflows

Practical, repeatable patterns you can run in Cursor with file‑scoped prompts. Each workflow lists inputs, steps, and a review checklist.

How to use these
- Start from a small set of files (PDFs, CSVs) and a clear goal.
- Ask file‑scoped prompts; review the clear preview of changes before approving.
- Keep a short `claims.md` for non‑obvious statements; use code to calculate for numbers.

Examples
- Rapid literature review → structured related work  
  Inputs: 3–6 PDFs. Output: a draft related‑work section with citations and footnotes.  
  See: [Managing Sources]({{ site.baseurl }}{% link guide/core/managing-sources.md %})
- Methods transcription → reproducible Markdown  
  Inputs: 1–2 PDFs with methods. Output: a methods section with quotes, paraphrases, and citations.  
  See: [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %})
- Results narrative from tables/figures  
  Inputs: one CSV, one figure. Output: a results paragraph with units and uncertainty.  
  See: [Analysis]({{ site.baseurl }}{% link guide/core/analysis.md %})

Review checklist
- Edits are file‑scoped with a clear preview of changes.
- Non‑obvious claims are cited; `claims.md` updated with key statements.
- Any numbers were computed with code and outputs saved.
- Internal links use `{{ site.baseurl }}{% link ... %}` tags.

What’s next
- Explore [Case Studies]({{ site.baseurl }}{% link case-studies/index.md %}) for real examples and lessons learned.

Change log
- 2025‑11‑04: First version with three exemplar workflows and links.

