---
title: Accuracy, Evidence, and Hallucination Control
status: complete
---

# Accuracy, Evidence, and Hallucination Control

Who this is for: anyone drafting scientific text who needs traceable statements and reproducible numbers.

Goal: make every statement traceable and every number reproducible. Use file‑scoped prompts, keep a simple claims log, and require “use code to calculate” for any numeric result.

What this covers
- Read–extract–cite workflow for quotes, paraphrases, and summaries
- A lightweight claims log you can audit
- Numeric results rubric (units, CI/SE, n, method) and guardrails
- Review gates and when to stop and read the primary source

Before you start
- In your project, add a simple `claims.md` at the root to track non‑obvious assertions and their sources.
- Use file‑scoped prompts so edits remain auditable (with a clear preview of changes in one file) and avoid stale chat memory.
- Prefer local processing for sensitive data; see [Data Governance]({{ site.baseurl }}{% link policies/data-governance.md %}).

Read–extract–cite workflow
1) Identify the target passage(s) in your sources (PDFs, datasets, protocols).
2) Extract quotes verbatim where essential; otherwise paraphrase carefully.
3) Immediately add an inline citation (include page/section numbers for direct quotes, e.g., [@key, p. 12]) and, if relevant, a footnote pointing to `references/` or a claim in `claims.md`.
4) Summarize in your own words and note any uncertainty or missing evidence in `claims.md`.

File‑scoped prompt patterns
- Use these copy/paste prompts:

  ```text
  From data/raw/paper1.pdf and data/raw/paper2.pdf, extract the
  definitions of [term]. Insert a 2–3 sentence paraphrase into
  manuscript/sections/01-introduction.md with citations, and add any
  non-obvious claims to claims.md with source links. Keep edits
  file-scoped and show a clear preview of changes.
  ```

  ```text
  Scan manuscript/sections/ for quotations or paraphrases. Ensure each
  has a citation and, if non-obvious, a footnote that points to
  references/ or claims.md. List any gaps as TODOs in claims.md.
  ```

Optional (advanced) — audit citations and numbers

```text
Task: Audit citations and numeric results for accuracy and
reproducibility.

Safety rules:
- Make file-scoped edits only to: manuscript/sections/** and claims.md
- Do not modify: references/**, manuscript/figures/**,
  manuscript/tables/**, analysis/**
- For any derived number, use code to calculate; show code and
  outputs; explain in plain language.
- Propose changes first as a preview; do not apply until I reply
  exactly: CONFIRM APPLY

Steps:
1) Scan manuscript/sections/** for quotes and paraphrases. Add missing
   citations, including page/section numbers for direct quotes.
2) Identify non-obvious statements. Add them to claims.md with source,
   location, and status=unverified. Do not duplicate existing claims.
3) Find all derived numbers. For each, draft a minimal code snippet
   that reproduces it. Include the exact input file paths. Place
   suggested code under analysis/notebooks/ as Markdown code blocks
   (do not write files yet).
4) Prepare a clear preview of changes for each touched file showing
   only minimal insertions/deletions.
5) Wait for my reply: CONFIRM APPLY before making any file edits.
```

Claims log (project‑level `claims.md`)
- Purpose: track non‑obvious assertions and their evidence.
- Suggested fields per claim: statement; source type (primary/secondary); location (page/figure/URL); status (unverified/verified/disputed); evidence note; date.
- Workflow: when drafting, add claims as unverified; during review, move to verified or disputed with notes.
- Format options:
  - Recommended (simplest): a bullet list you can edit quickly.
  - Optional: a small Markdown table (good for scanning) or a CSV if you prefer spreadsheets.

Minimal claims.md — bullet list template (recommended)

- [ ] Statement: X increases Y in Z dataset
  - Source: Primary
  - Location: p. 5, Fig. 2
  - Status: unverified
  - Evidence: Needs replication details
  - Date: 2025‑11‑03

Optional — table template (for scanning)

| Statement | Source | Location | Status | Evidence | Date |
|---|---|---|---|---|---|
| X increases Y in Z dataset | Primary | p. 5, Fig. 2 | unverified | Needs replication details | 2025‑11‑03 |

Numeric results: “use code to calculate”
- Require that any derived number comes from code with visible inputs and outputs.
- Save code in `analysis/scripts/` (or a Markdown notebook in `analysis/notebooks/`) and keep figures/tables under `analysis/figures/` and `analysis/tables/` before promoting paper‑ready assets into `manuscript/`.
- Set seeds for stochastic procedures; capture environments with lockfiles (small files that record exact package versions, e.g., `environment.yml`, `renv.lock`).
 - Always show the code and printed outputs, and add a one‑sentence plain‑language explanation of what the numbers mean.

No‑code path: if you aren’t running code, mark derived numbers as TODOs in the manuscript and list them in `claims.md` for later verification.

Example pattern (low‑code, for review — not auto‑run)
Notebook structure (inside your file): include these three parts — code; printed output; a one‑sentence plain‑language explanation.

```python
import pandas as pd
df = pd.read_csv('data/processed/example.csv')
summary = df['value'].describe()
print(summary.to_string())
```

Result (example output):

```
count    120
mean      ...  # real numbers appear when you run it
std       ...
min       ...
25%       ...
50%       ...
75%       ...
max       ...
```

Example explanation sentence (plain language)
- “Among 120 participants (treatment group), the average reaction time was 512 ms (SD 98), ranging from 320 to 780 ms.”

Numeric results rubric (add to your reviews)
- Units: every number carries explicit units.
- n: state sample size and any exclusions.
- Method: specify how it was computed (test/model, parameters, seed).
- Uncertainty: include CI/SE/SD with method and level (e.g., 95% CI).
- Reproducibility: link to the exact script or notebook and inputs.

Verification checklist
- Citations present for all quotes and paraphrases; no fabricated references.
- Direct quotes include page/section numbers.
- Non‑obvious claims logged in `claims.md` with sources/status.
- Derived numbers come from code blocks with visible outputs.
- Figures/tables saved deterministically with captions (units, context).
- Peer review gate: a second pass verifies citations and recomputes numbers.

When to stop and read the primary source
- If claims conflict across sources or an agent’s paraphrase seems strong, pause and read the original carefully.
- For critical claims (central to results/interpretation), verify directly from the primary source and update `claims.md`.

Cross‑links
- [Quick Start]({{ site.baseurl }}{% link guide/core/quick-start.md %})
- [First‑Hour exercise]({{ site.baseurl }}{% link getting-started/first-hour.md %})
- [Writing in Markdown]({{ site.baseurl }}{% link guide/core/writing-markdown.md %})
- [Analysis]({{ site.baseurl }}{% link guide/core/analysis.md %})
- [Managing Sources]({{ site.baseurl }}{% link guide/core/managing-sources.md %})
- [Project Rules]({{ site.baseurl }}{% link guide/core/project-rules.md %})
- [Data Governance]({{ site.baseurl }}{% link policies/data-governance.md %})

What’s next
- Proceed to [Managing Sources]({{ site.baseurl }}{% link guide/core/managing-sources.md %})

Change log
- 2025-11-03: Added audience one‑liner.
- 2025-11-03: Marked complete; added an optional advanced audit prompt with approval gating and file-scoped constraints.
- 2025-11-03: Standardized prompt patterns to fenced code blocks for easy copy/paste.
- 2025-11-03: Emphasized “show code and outputs” and added cross-links to Quick Start and First‑Hour.
- 2025-11-03: Switched default claims.md template to a simple bullet list; kept table as optional.
- 2025-11-03: Clarified example; moved explanation outside code block and added a concrete example sentence.
- 2025-11-03: Added page‑number requirement, no‑code numeric note, claims.md template, and privacy pointer.
- 2025-11-03: Removed internal repo reference; clarified reader-facing guidance for `claims.md` in user projects.
- 2025-11-03: First full draft with claims log, read–extract–cite, numeric rubric, and verification checklist.
