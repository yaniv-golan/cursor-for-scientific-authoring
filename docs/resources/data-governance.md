---
title: Data Governance and Privacy
layout: default
parent: Resources
---


# Data Governance and Privacy

Purpose: protect sensitive information while keeping work auditable and reproducible. Favor a local‑first workflow, scope agent permissions narrowly, and require explicit approvals for any change that touches data, secrets, or the network.

What this covers
- What agents can access (local vs. cloud execution; model/vendor differences)
- Approval gates and auditable logs for commands and code
- Local‑first practices for sensitive data; when to use cloud resources
- Redaction, minimal sharing, and synthetic examples for demos

Key principles
- Local‑first by default: keep private data on your machine; bring the model to the data when possible. Use cloud only when needed and acceptable under policy.
- Minimum necessary access: in prompts, state exactly which files or folders the agent may read or change. Prefer read‑only dry runs first.
- Approval gating: require a clear preview of changes and your explicit reply “CONFIRM APPLY” before any rename/move/install/execute.
- Separate secrets: never paste raw credentials. Store secrets in platform keychains or `.env` files that are never committed; reference them indirectly if needed.
- No blind uploads: do not paste large excerpts of private documents into chat. Use file‑scoped prompts with `@file` references and keep content local.
- Audit trail: keep plain‑text logs of agent actions and decisions inside `ops/` or `analysis/reports/`. Summarize data touchpoints and approvals.
- PII safety: avoid collecting unnecessary personal data. If present, document lawful basis and handling. Prefer de‑identified or aggregated outputs.
- License and terms: confirm license/usage rights for any third‑party data; record source, date, and license in a short metadata note.

Simple‑first prompt (safe by default)

```text
Task: Summarize methods from sources/ for the manuscript without exposing sensitive data.

Safety rules:
- Read-only. Do not write or rename any files.
- Scope reads to: sources/** and notes/**
- Do not send any file contents to external services; work locally.
- If any uncertainty about sensitive content, stop and ask one question.

Steps:
1) Read only filenames and short excerpts necessary to draft a 3–5 sentence methods summary.
2) Output the summary into this chat and list which files informed it.
3) Propose file-scoped edits as a preview for manuscript/sections/02-methods.md. Wait for my reply: CONFIRM APPLY before any write.
```

Approval‑gated prompt (edits + installs)

```text
Task: Set up a minimal local analysis runtime and compute a summary table from data/processed/metrics.csv.

Safety rules:
- Propose changes first; do not apply until I reply exactly: CONFIRM APPLY
- Only modify: analysis/** and environment.yml
- Do not touch: data/raw/**, references/**, manuscript/**
- For any number, use code to calculate; show code and outputs; explain in plain language.

Steps:
1) Dry run: print a preview diff of files to add/change (paths only) and the conda packages with pinned versions.
2) On CONFIRM APPLY: write environment.yml, create analysis/notebooks/metrics.md with code, outputs, and one-sentence explanation.
3) Save figures to analysis/figures/ and tables to analysis/tables/; do not overwrite existing files.
4) Print an action log and an undo list.
```

Handling sensitive sources
- Redact: when showing examples, replace sensitive strings (names, IDs, addresses) with safe placeholders; keep an unredacted copy locally.
- Use synthetic samples: generate small, representative dummy data for demos and prompts. Keep real data offline.
- Network awareness: if using cloud‑executed agents or remote tools, assume data could leave your machine. Verify provider policies and disable network where required.

Operational checklists
- Before starting: confirm data location, access controls, licenses, and whether cloud use is permitted.
- During work: keep scopes narrow in prompts; run dry‑runs first; review previews carefully; require “CONFIRM APPLY”.
- Before sharing: scrub PII, remove secrets, and re‑run citation and claims audits.

Cross‑links
- [Quick Start]({{ site.baseurl }}{% link guide/core/quick-start.md %})
- [Managing Sources]({{ site.baseurl }}{% link guide/core/managing-sources.md %})
- [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %})
- [Analysis]({{ site.baseurl }}{% link guide/core/analysis.md %})
- [Project Rules]({{ site.baseurl }}{% link guide/core/project-rules.md %})

What’s next
- Proceed to [Analysis]({{ site.baseurl }}{% link guide/core/analysis.md %})

Change log
- 2025-11-03: First complete draft with local‑first guidance, approval gating, safe prompt patterns, and cross‑links.
