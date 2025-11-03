---
title: Accuracy, Evidence, and Hallucination Control
status: draft
---

# Accuracy, Evidence, and Hallucination Control

Goal: make every statement traceable and every number reproducible. Use file‑scoped prompts, keep a simple claims log, and require “use code to calculate” for any numeric result.

What this covers
- Read–extract–cite workflow for quotes, paraphrases, and summaries
- A lightweight claims log you can audit
- Numeric results rubric (units, CI/SE, n, method) and guardrails
- Review gates and when to stop and read the primary source

Before you start
- In your project, add a simple `claims.md` at the root to track non‑obvious assertions and their sources.
- Use file‑scoped prompts so edits remain auditable (diffs in one file) and avoid stale chat memory.
- Prefer local processing for sensitive data; see `content/policies/data-governance.md`.

Read–extract–cite workflow
1) Identify the target passage(s) in your sources (PDFs, datasets, protocols).
2) Extract quotes verbatim where essential; otherwise paraphrase carefully.
3) Immediately add an inline citation (include page/section numbers for direct quotes, e.g., [@key, p. 12]) and, if relevant, a footnote pointing to `references/` or a claim in `claims.md`.
4) Summarize in your own words and note any uncertainty or missing evidence in `claims.md`.

File‑scoped prompt patterns
- “From `data/raw/paper1.pdf` and `paper2.pdf`, extract the definitions of [term]. Insert a 2–3 sentence paraphrase into `manuscript/sections/01-introduction.md` with citations, and add any non‑obvious claims to `claims.md` with source links. Keep edits file‑scoped and show diffs.”
- “Scan `manuscript/sections/` for quotations or paraphrases. Ensure each has a citation and, if non‑obvious, a footnote that points to `references/` or `claims.md`. List any gaps as TODOs in `claims.md`.”

Claims log (project‑level `claims.md`)
- Purpose: track non‑obvious assertions and their evidence.
- Suggested fields per claim: statement; source type (primary/secondary); location (page/figure/URL); status (unverified/verified/disputed); evidence note; date.
- Workflow: when drafting, add claims as unverified; during review, move to verified or disputed with notes.

Minimal claims.md (copy into your project)

| Statement | Source (primary/secondary) | Location (page/URL) | Status | Evidence note | Date |
|---|---|---|---|---|---|
| X increases Y in Z dataset | Primary | p. 5, Fig. 2 | unverified | Needs replication details | 2025‑11‑03 |

Numeric results: “use code to calculate”
- Require that any derived number comes from code with visible inputs and outputs.
- Save code in `analysis/scripts/` (or a Markdown notebook in `analysis/notebooks/`) and keep figures/tables under `analysis/figures/` and `analysis/tables/` before promoting paper‑ready assets into `manuscript/`.
- Set seeds for stochastic procedures; capture environments with lockfiles (e.g., `environment.yml`, `renv.lock`).

No‑code path: if you aren’t running code, mark derived numbers as TODOs in the manuscript and list them in `claims.md` for later verification.

Example pattern (low‑code, for review — not auto‑run)
```
# analysis/notebooks/01-summary.md

Use code to calculate; show code and outputs; explain in plain language.

```python
import pandas as pd
df = pd.read_csv('data/processed/example.csv')
summary = df['value'].describe()
print(summary.to_string())
```

Result (annotated):

```
count    120
mean      ...  # model prints the actual value here
std       ...
min       ...
25%       ...
50%       ...
75%       ...
max       ...
```

Explanation (plain language): Report N, mean, dispersion, and range. Include units and any relevant subgroup definitions.
```

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
- Writing in Markdown: `content/guide/core/writing-markdown.md`
- Analysis patterns: `content/guide/core/analysis.md`
- Managing sources: `content/guide/core/managing-sources.md`
- Project rules (AGENTS.md): `content/guide/core/project-rules.md`
- Data governance: `content/policies/data-governance.md`

What’s next
- Proceed to Managing Sources: `content/guide/core/managing-sources.md`

Change log
- 2025-11-03: Added page‑number requirement, no‑code numeric note, claims.md template, and privacy pointer.
- 2025-11-03: Removed internal repo reference; clarified reader-facing guidance for `claims.md` in user projects.
- 2025-11-03: First full draft with claims log, read–extract–cite, numeric rubric, and verification checklist.
