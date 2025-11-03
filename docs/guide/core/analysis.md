---
title: Agent‑Written Code with Minimal Coding
layout: default
grand_parent: Guide
parent: Core
nav_order: 50
---


# Agent‑Written Code with Minimal Coding

Who this is for: researchers who want to generate and run small analyses with agent help, without deep programming knowledge.

Goal: run small, auditable analyses with agent‑generated code while keeping results reproducible. Require “use code to calculate,” show code and outputs, and save artifacts predictably.

What you need
- A local runtime (Python or R). Approve executions consciously.
- A project layout with `analysis/`, `manuscript/`, `data/`, and `references/` (see Quick Start). Keep paper‑ready assets under `manuscript/` and exploratory outputs under `analysis/`.
- A dependency lockfile: `environment.yml` (conda/mamba) or `renv.lock` (R). Pin exact versions.

If you’re new to this
- You do not need to know what a lockfile, `environment.yml`, or `renv` is to get started. Use the simple‑first prompt below; the agent will propose any setup and wait for your explicit approval.
- You can skip installs at first. When ready, approve a minimal setup the agent proposes (with a clear preview).

Reproducibility guardrails
- Always compute numbers from code (“use code to calculate”). Show the code and printed outputs; add a one‑sentence plain‑language explanation.
- Set random seeds and record parameters. Save scripts in `analysis/scripts/` or use Markdown notebooks in `analysis/notebooks/`.
- Save figures to `analysis/figures/` and tables to `analysis/tables/`. Promote finalized assets into `manuscript/figures/` and `manuscript/tables/`.
- Keep inputs immutable: treat `data/raw/` as read‑only; write derived datasets to `data/processed/`.

Simple‑first prompt (safe; propose before applying)

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
1) Print a preview of files to be written (paths only).
2) Draft a Markdown notebook at analysis/notebooks/example.md with:
   - Code blocks to load CSV, compute summary stats, and plot
   - Printed outputs for all numbers
   - One‑sentence plain‑language explanation
3) On my CONFIRM APPLY, write the notebook and save the plot to
   analysis/figures/example.png and a table to
   analysis/tables/example.md
```

Python example (in‑notebook code)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.read_csv('data/processed/example.csv')
summary = df['value'].describe()
print(summary.to_string())

plt.figure(figsize=(5,3))
df['value'].hist(bins=20)
plt.xlabel('value')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('analysis/figures/example.png', dpi=150)

# Save a small Markdown table
table = summary.reset_index()
table.columns = ['metric', 'value']
table.to_csv('analysis/tables/example.csv', index=False)
print('Saved figure to analysis/figures/example.png and table to analysis/tables/example.csv')
```

R example (in‑notebook code)

```r
set.seed(42)
df <- read.csv('data/processed/example.csv')
summary_vals <- summary(df$value)
print(summary_vals)

png('analysis/figures/example.png', width=800, height=480)
hist(df$value, breaks=20, xlab='value', main='Histogram')
dev.off()

write.csv(data.frame(metric=names(summary_vals), value=as.numeric(summary_vals)),
          'analysis/tables/example.csv', row.names=FALSE)
cat('Saved figure to analysis/figures/example.png and table to analysis/tables/example.csv\n')
```

Lockfiles and environments
- Python: propose an `environment.yml` with pinned versions (e.g., `python=3.11`, `pandas=2.2.*`, `matplotlib=3.9.*`). Keep it minimal.
- R: prefer `renv` to snapshot exact package versions; store `renv.lock` in the repo.
- On installs, require a dry‑run preview of packages and versions before applying.

Plain‑language definitions
- Lockfile: a small text file that records the exact versions of the packages you used so results can be reproduced later.
- `environment.yml`: Conda’s configuration file that lists Python and packages to install; the tool reads it to create the environment.
- `renv`: an R package that freezes your R package versions into `renv.lock` so collaborators can recreate the same setup.

Optional — validation pass (approval‑gated)

```text
Task: Validate that all numbers and figures in manuscript/ come from
code.

Safety rules:
- Read-only scan of manuscript/** and analysis/**
- Propose changes only; wait for my reply exactly: CONFIRM APPLY

Steps:
1) List every number in manuscript/ that lacks a code reference.
2) For each, propose a minimal code block and exact input path to
   reproduce it.
3) Prepare a preview of file-scoped edits to insert code references or
   TODOs.
```

Cross‑links
- Data governance: `content/policies/data-governance.md`
- Accuracy: `content/guide/core/accuracy.md`
- Managing Sources: `content/guide/core/managing-sources.md`
- Writing in Markdown: `content/guide/core/writing-markdown.md`
- Project rules (AGENTS.md): `content/guide/core/project-rules.md`

What’s next
- Proceed to Project Rules with AGENTS.md: `content/guide/core/project-rules.md`

Change log
- 2025-11-03: Added audience one‑liner and beginner guidance.
- 2025-11-03: First complete draft with prompts, Python/R examples, lockfile guidance, seeds, and save locations; added cross‑links and next step.
