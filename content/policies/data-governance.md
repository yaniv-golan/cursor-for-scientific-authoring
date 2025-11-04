---
title: Data Governance and Privacy
status: complete
---

# Data Governance and Privacy

Purpose: protect sensitive information while keeping work auditable and reproducible. Favor a local‑first workflow, scope agent permissions narrowly, and require explicit approvals for any change that touches data, secrets, or the network.

Note: IDE agents typically transmit your prompts and selected file excerpts to the configured model provider for inference. Treat any text included in prompts/context as leaving your device unless your client explicitly guarantees local inference.

How Cursor handles data (links)
- Data Use & Privacy Overview: https://cursor.com/data-use
- Review (proposed changes before apply): https://cursor.com/docs/agent/review
- @ Symbols (scoping files in context): https://cursor.com/docs/context/symbols

What this covers
- What agents can access (local vs. cloud execution; model/vendor differences)
- Approval gates and auditable logs for commands and code
- Local‑first practices for sensitive data; when to use cloud resources
- Redaction, minimal sharing, and synthetic examples for demos

Key principles
- Local‑first by default: keep private data on your machine. Understand that prompts and selected file excerpts are sent to providers; include only what’s necessary. Use cloud calls only when necessary and approved under your policy, and prefer working on redacted or synthetic data when possible.
- Minimum necessary access: in prompts, state exactly which files or folders the agent may read or change. Prefer read‑only dry runs first.
- Approval gating: require a clear preview of changes and your explicit reply “CONFIRM APPLY” before any rename/move/install/execute.
- Separate secrets: never paste raw credentials. Store secrets in platform keychains or `.env` files that are never committed; reference them indirectly if needed.
- No unnecessary uploads: assume prompts and excerpts are transmitted to providers. Do not paste large chunks of sensitive text. Prefer the smallest necessary excerpt (e.g., ≤ 10 lines) and summarize where possible.
- Audit trail: keep plain‑text logs of agent actions and decisions inside `ops/` or `analysis/reports/`. Summarize data touchpoints and approvals.
- PII safety: avoid collecting unnecessary personal data. If present, document lawful basis and handling. Prefer de‑identified or aggregated outputs.
- License and terms: confirm license/usage rights for any third‑party data; record source, date, and license in a short metadata note.

Simple‑first prompt (safe by default)

```text
Task: Summarize methods from sources/ for the manuscript without exposing sensitive data.

Safety rules:
- Read-only. Do not write or rename any files.
- Scope reads to: sources/** and notes/**
- Minimize transmission: do not include full documents in prompts; if an excerpt is needed, show at most 5–10 lines and get approval first.
- If any uncertainty about sensitive content, stop and ask one question.

Steps:
1) List candidate files and propose the smallest necessary excerpts (quote count and line ranges only) for approval.
2) After approval, produce a 3–5 sentence methods summary and list which files informed it.
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
