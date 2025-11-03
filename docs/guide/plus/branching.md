---
title: Exploratory Branching For Alternates (Optional)
layout: default
grand_parent: Guide
parent: Plus
---


# Exploratory Branching For Alternates (Optional)

Use short‑lived branches to try risky rewrites, alternate framings, or new analyses without destabilizing `main`. Keep commits small and reviewable.

When to branch
- Major reframes or structure edits (e.g., rewrite Introduction)
- Competing analysis approaches or figures
- Collaborative experiments where a reviewer needs a clear preview of changes

Naming conventions
- `experiment/<topic>` for content experiments (e.g., `experiment/intro-alt`)
- `analysis/<task>` for data/figures (e.g., `analysis/forest-plot`)
- Include date or initials if helpful: `experiment/discussion-2025-11-03`

Create and switch
```bash
# from up-to-date main
git checkout -b experiment/intro-alt
# or, with newer Git
git switch -c experiment/intro-alt
```

Work in small commits
```bash
git status
git add manuscript/sections/01-introduction.md
git commit -m "feat(intro): reframe problem statement; add two citations"
git add manuscript/figures/alt-schematic.svg
git commit -m "feat(figure): add alternate schematic; update caption"
```

Review and merge
- Sync `main` first: `git checkout main && git pull --ff-only`
- Prefer simple fast‑forward merges. Open a small review (PR) or ask the agent to summarize a preview of changes. Merge back when approved:
  ```bash
  git checkout main
  git merge --ff-only experiment/intro-alt
  git branch -d experiment/intro-alt
  ```
- Optional (advanced): Update the branch with the latest `main` before review. If you’re comfortable: `git checkout experiment/intro-alt && git rebase main`. If unsure, skip and let the merge step surface conflicts.

If conflicts arise
- Pause and review conflicted files with a clear preview of changes.
- Resolve, then continue: for merges, `git add <files> && git commit`; for rebases, `git add <files> && git rebase --continue`.
- If unsure, ask for help or abort the rebase: `git rebase --abort`.

Approval‑gated branching prompt (copy/paste)
```text
Task: Create an experiment branch, save focused commits, and merge back
after review.

Safety rules:
- Only run Git commands; do not modify file contents.
- Propose the exact commands first; wait for my reply exactly: CONFIRM APPLY.
- Use fast-forward merges only; if conflicts appear, stop and ask.

Steps:
1) Show current branch and status; suggest a branch name
2) Propose staged commits by topic with messages
3) Propose merge steps (ff-only) and branch deletion after merge
4) On CONFIRM APPLY, run commands and print resulting commit/merge IDs
```

Tips
- Keep branches short‑lived and focused on one idea.
- Lean on the [Git]({{ site.baseurl }}{% link guide/plus/git.md %}) basics for staging and safe undo.
- Use the [Checklists]({{ site.baseurl }}{% link guide/core/checklists.md %}) during review.

What’s next
- Continue to [MCP]({{ site.baseurl }}{% link guide/pro/mcp.md %}) to connect tool‑based skills once your Git basics feel comfortable.

Change log (drafting)
- 2025-11-03: Added front matter, branching workflow, commands, approval‑gated prompt, and internal links; marked page complete.
