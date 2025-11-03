---
title: Project Rules With AGENTS.md
layout: default
grand_parent: Guide
parent: Core
nav_order: 70
---


# Project Rules With AGENTS.md

Purpose: capture norms, scope, and acceptance criteria so agents work safely and consistently on your paper. Keep it short and human‑readable.

What to include
- Scope: which files/folders agents may read or change by default
- Safe‑edit patterns: file‑scoped edits; smallest safe change; clear preview of changes
- Accuracy rules: cite non‑obvious claims; keep a `claims.md` log; “use code to calculate” for numbers and show code/outputs
- Privacy: ask before executing commands or installs; avoid sending local files to external services without approval
- Acceptance checklist: criteria to finish a task (citations present, numbers reproducible, paths consistent, next steps listed)

Minimal example (copy/paste into your project’s `AGENTS.md`)

```text
# Project Agent Rules (Paper Title)

Scope: All files in this project.

How we work
- File‑first edits only. Make the smallest safe change and show a clear preview of changes.
- Keep edits in the target file(s) unless asked otherwise.

Accuracy & citations
- Ground non‑obvious claims in cited sources. Add footnotes and entries in `references/` and log key claims in `claims.md`.
- Do not invent citations.
- If you compute any number, use code to calculate and include the code and outputs. Save scripts in `analysis/scripts/` and tables/figures in `manuscript/tables/` and `manuscript/figures/`.

Privacy & safety
- Do not send local files or data to external services unless explicitly approved.
- Ask before executing commands or installing packages.

Acceptance checklist
- Edits are file‑scoped with a clear preview of changes; citations present; numbers reproducible; paths consistent; next steps listed.
```

Reuse across tools
- Claude Code does not auto‑read `AGENTS.md`. Reference it from `CLAUDE.md` (see repository `CLAUDE.md`) to reuse the same rules.
- Keep the same rules if you use other IDE assistants; include `@AGENTS.md` and, when relevant, `@content/reference-toc.md` in prompts so tools load the site structure.

Where to start
- A sample `AGENTS.md` also appears in [Quick Start]({{ site.baseurl }}{% link guide/core/quick-start.md %})
- Keep `AGENTS.md` minimal; evolve it as your team converges on conventions.
