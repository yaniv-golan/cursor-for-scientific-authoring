---
title: Versioning With Git (Inside Cursor)
layout: default
grand_parent: Guide
parent: Plus
---


# Versioning With Git (Inside Cursor)

Track changes, review clear previews of changes, and share your work. Start simple: initialize a repo, save small commits, and only later add remotes and checks.

What you’ll learn
- Initialize a Git repo in your paper project
- Stage small, file-scoped edits and write useful commit messages
- Review a preview of changes and undo safely
- Connect a remote, push/pull, and collaborate lightly

Prerequisites
- A local project folder following the minimal layout (see [Quick Start]({{ site.baseurl }}{% link guide/core/quick-start.md %})).
- Git installed (`git --version`). No GitHub account required unless you plan to sync.

Initialize a repository (local only)
```bash
cd /path/to/your/paper
git init
git add AGENTS.md claims.md manuscript references analysis data .gitignore
git commit -m "chore: initialize project with minimal layout"
```

Stage and commit small changes
- Keep commits focused on a single idea (e.g., “add Methods outline” or “add figure and caption”).
- Review a preview of changes before committing:
  ```bash
  git status
  git diff        # unstaged changes
  git add path/to/file.md
  git diff --staged
  git commit -m "feat: add Results outline with two subsections"
  ```

Undo safely
- Unstage but keep edits: `git restore --staged path/to/file.md`
- Discard local edits in a file (careful): `git checkout -- path/to/file.md`
- Revert the last commit (creates a new commit): `git revert HEAD`

Connect a remote (optional)
```bash
# Create an empty repo on your hosting provider (e.g., GitHub) first
git remote add origin git@github.com:USER/REPO.git
git branch -M main
git push -u origin main
```
Pull and push changes
```bash
git pull --ff-only
git push
```

.gitignore for papers (minimal)
```text
.DS_Store
dist/
analysis/figures/
analysis/tables/
data/interim/
data/processed/
*.aux
*.log
```

Pre-commit checks (optional)
- Add lightweight checks for Markdown links or front matter. Keep them optional and approval‑gated in prompts.

Approval‑gated Git prompt (copy/paste)
```text
Task: Save my recent manuscript edits with small, focused commits.

Safety rules:
- Only run Git commands; do not modify files.
- Propose the exact commands first; wait for my reply exactly: CONFIRM APPLY.
- If any command would overwrite or discard changes, ask before proceeding.

Steps:
1) Show a preview of changes (git status; git diff summary)
2) Propose staged commits grouped by topic with commit messages
3) On CONFIRM APPLY, run the commands and show the new commit IDs
```

Collaboration tips
- Keep Markdown as the source of truth; regenerate exports instead of editing DOCX/PDF manually.
- Review changes in Cursor’s preview-of-changes view before committing.
- Use small pull requests for peer review; copy the checklist from [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %}).

What’s next
- Continue to [Branching]({{ site.baseurl }}{% link guide/plus/branching.md %}) to explore safe branches for experiments and reviews.

Change log (drafting)
- 2025-11-03: Added front matter, minimal workflows, .gitignore, approval-gated prompt, and internal links; marked page complete.
