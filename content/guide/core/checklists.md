---
title: Checklists And Prompt Patterns
status: complete
---

# Checklists And Prompt Patterns

Use these print‑friendly lists during drafting and review. Keep them close to your manuscript.

Day‑0 setup checklist
- Cursor installed and signed in; a model selected in Composer
- Create a local project folder using the minimal layout (see Quick Start)
- Add `AGENTS.md` with scope, safety rules, and acceptance criteria
- Create `claims.md` at project root for non‑obvious assertions
- Set up `references/` with `library.bib` (or `library.json`) and a CSL style
- Create empty folders: `manuscript/sections/`, `manuscript/figures/`, `manuscript/tables/`
- Optional (low‑code later): install Python or R; plan for `environment.yml` or `renv.lock`

Section drafting checklist (IMRaD)
- Start from `manuscript/sections/00-outline.md`; one file per section
- File‑scoped prompts only; request a clear preview of changes before applying
- Introduce claims in your own words; add citations immediately
- For direct quotes, include page or section numbers (e.g., [@key, p. 12])
- Add non‑obvious statements to `claims.md` with source and status
- Keep figures/tables referenced but store assets under `manuscript/`

Verification and citation checklist
- No fabricated citations; all citations resolve to keys in `references/`
- Direct quotes include page/section numbers; paraphrases are faithful
- `claims.md` lists non‑obvious assertions with status (unverified/verified)
- Numbers that require computation are marked TODO or backed by code
- Figures/tables have captions (units, context) and correct paths
- A second pass (self or peer) reviews citations and recomputes numbers

Data analysis prompt patterns (generate → run → verify → summarize)
- Simple‑first (approval‑gated):
  ```text
  Task: Compute descriptive statistics and one plot from
  data/processed/example.csv.

  Safety rules:
  - Propose changes first; do not write files until I reply exactly:
    CONFIRM APPLY
  - Only create or modify: analysis/notebooks/**, analysis/figures/**,
    analysis/tables/**
  - Do not touch: data/raw/**, manuscript/**, references/**
  - Use code to calculate; show code and outputs; explain in plain
    language.

  Steps:
  1) Print a preview of files to be written (paths only)
  2) Draft analysis/notebooks/example.md with code, printed outputs,
     and one‑sentence explanation
  3) On CONFIRM APPLY, write the notebook and save outputs
     deterministically
  ```

One‑page “red team your draft” list
- Are any claims too strong for the cited evidence? Tone them down or add sources
- Could a reader reproduce each number? Link to code or add TODOs
- Are units, sample sizes, and uncertainty reported where needed?
- Any ambiguous method steps? Add a short clarification or a methods note
- Any sensitive data? Remove, redact, or move to a safer path; prefer local processing
- Would a skeptical reviewer find missing citations? Add them now

Cross‑links
- [Quick Start]({{ site.baseurl }}{% link guide/core/quick-start.md %})
- [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %})
- [Writing in Markdown]({{ site.baseurl }}{% link guide/core/writing-markdown.md %})
- [Analysis]({{ site.baseurl }}{% link guide/core/analysis.md %})
- [Data Governance]({{ site.baseurl }}{% link policies/data-governance.md %})
