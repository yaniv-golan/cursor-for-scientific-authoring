---
title: Multi‑agent Workflows (Optional)
layout: default
grand_parent: Guide
parent: Pro
---


# Multi‑agent Workflows (Optional)

Coordinate multiple agents to parallelize work while preserving safety. Keep scope small, isolate edits, and require review before merge.

Patterns
- Planner → Executors: one agent proposes a plan; others execute file‑scoped tasks.
- Isolation: use Git branches or worktrees per agent to avoid conflicts.
- Batching: limit concurrency to what you can review (e.g., 2–3 tasks at a time).

Safety gates
- All edits must present a clear preview of changes; no direct writes without approval.
- Require citations for non‑obvious claims; see [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %}).
- Use [Checklists]({{ site.baseurl }}{% link guide/core/checklists.md %}) before merging outputs.

Coordinator prompt (copy/paste)
```text
Task: Coordinate 2–3 focused agent tasks on separate branches, then reconcile.

Safety rules:
- File‑scoped prompts only; show previews of changes.
- Propose branches, commands, and file lists; wait for CONFIRM APPLY.
- Stop on conflicts; request human review.

Steps:
1) Propose branches and task assignments (e.g., citations pass, figure polish)
2) For each, list files to change and the review checklist to apply
3) On CONFIRM APPLY, create branches and kick off tasks
4) Summarize outputs and open review; do not merge without approval
```

Reconciling outputs
- Summarize differences across branches; highlight conflicts.
- Prefer fast‑forward merges; if conflicts arise, pause and review.

What’s next
- Revisit [Endgame]({{ site.baseurl }}{% link guide/core/endgame.md %}) to package outputs once multi‑agent tasks are reconciled.

Change log (drafting)
- 2025-11-03: Added front matter, patterns, safety gates, coordinator prompt, and cross-links; marked page complete.
