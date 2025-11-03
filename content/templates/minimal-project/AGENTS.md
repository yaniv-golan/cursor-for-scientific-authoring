# Project Agent Rules (Paper Title)

Scope: Entire `minimal-project` folder when used as a standalone project.

How we work
- File-first edits only. Make the smallest safe change and show diffs.
- Keep edits to the target file(s) unless explicitly asked to touch others.
- Prefer file-scoped prompts; avoid ad-hoc chat memory.

Accuracy & citations
- Ground non-obvious claims in cited sources. Add footnotes and entries in `references/` and log key claims in `claims.md` (quote, paraphrase, source, DOI/URL).
- Do not invent citations. Flag gaps instead of guessing.
- For any derived number: use code to calculate; include code and outputs. Save scripts in `analysis/scripts/` and results in `manuscript/tables/` and `manuscript/figures/`.

Privacy & safety
- Do not send local files or data to external services unless explicitly approved.
- Ask before executing commands or installing packages.

Acceptance checklist (before finishing)
- Edits are file-scoped with diffs.
- Sources cited; `claims.md` updated for non-obvious statements.
- Numbers are reproducible (code + outputs saved).
- Paths and filenames are consistent with this layout.
- List next actions or open questions at the end of the file.
