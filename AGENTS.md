# Cursor for Scientists – AGENTS.md

## Project context
- We are authoring a public guide that teaches researchers how to use Cursor (and related coding agents) to author scientific papers end-to-end.
- Secondary coverage (e.g., reports, workflows) may appear, but the primary focus is papers.
- The finished, reader-facing content lives in `docs/` (GitHub Pages). Drafts stay in `content/`. Source material remains in `raw/`.
- Everything is written in Markdown; prefer lightweight structure (headings, tables, callouts) that is easy to edit by humans.

> [!IMPORTANT]
> Scope and layout: This repository’s structure (`docs/`, `content/`, `raw/`) exists solely to produce this guide. It is NOT the layout recommended by the guide for authoring scientific papers with Cursor. The guide will include its own project-structure recommendations and templates for research workflows.

## What the agent should do
- Draft or edit Markdown documents that explain processes, checklists, and best practices for scientific work aided by coding agents.
- Summarize and synthesize the vetted notes in `raw/`, turning them into coherent guidance while keeping attributions.
- Maintain clear navigation and cross-links so readers can connect workflows, case studies, and resources.

## Process & Layout (for agents)
- Draft in `content/`; publish in `docs/`; fact-check claims in `raw/claims.md`.
- Do not modify files under `raw/` except to update `raw/claims.md` with sourced or clearly labeled empirical notes.
- Treat `raw/drafts/` as inspiration only; align guidance with `raw/claims.md`.
- Follow the reference TOC at `content/reference-toc.md:1` when planning structure and cross-links.
- Keep this repository’s layout (docs/content/raw) as production for the guide only; do not present it as a template for research projects.
- Prefer file-scoped prompts and grounded edits over free-form chat. Show diffs for substantial changes.

### Prompt formatting for docs (copy/paste friendly)
- Present any long prompt examples inside fenced code blocks using triple backticks and a neutral language tag like `text` for clean copy/paste.
- Avoid triple quotes ("""). They are not a Markdown standard and are easier to miscopy. Prefer fenced blocks instead.
- Keep prompts plain and self-contained: start with a single-line Task, then Safety rules, then Steps. Avoid internal Markdown formatting inside the prompt text.
- Include explicit approval gating for any changes (e.g., require the user to reply exactly `CONFIRM APPLY` before renames/moves/installs).
- Use a simple-first prompt by default; list any structured/advanced workflow (e.g., review checklist, proposed change list) as optional.
- Prefer file-scoped constraints in prompts (what files/paths may be changed). Ask clarifying questions before proceeding if anything is ambiguous.

## Tool-specific ingestion notes
- Cursor: reference `@AGENTS.md` and `@content/reference-toc.md` in prompts so the agent loads rules and structure.
- Claude Code: create and maintain `CLAUDE.md` that includes `@AGENTS.md`; Claude Code does not auto-read `AGENTS.md`.
- Codex and other IDE assistants: explicitly include `@AGENTS.md` (and, when relevant, `@content/reference-toc.md`) in prompts to pin rules and site structure.

## Quality guardrails
- Cite sources for non-obvious claims using Markdown footnotes or reference lists. Capture bibliographic details in `references/` when possible.
- Flag any uncertainty or missing evidence rather than speculating.
- Keep tone instructional, concise, and appropriate for researchers who may not be software engineers.
- Prefer plain language over developer jargon in reader-facing content. If a technical term is necessary, define it briefly or use a clearer substitute (e.g., say “preview of changes” instead of “diff,” “checklist” instead of “manifest”). Default to a simple-first prompt, with any advanced or team workflows marked as optional.
- Avoid modifying files under `raw/`; add new work in `content/` or `docs/` as appropriate.
- Treat `raw/claims.md` as the fact-checked source of truth—align new guidance with the claims it records or update the catalogue first if new evidence emerges.
- Do not present this repository’s layout as a template for research projects; it is a production layout for the guide only.

## Publishing & Versioning (for agents)

- Publishing is automated via GitHub Actions (`.github/workflows/pages.yml`). Any push to `main` that changes `docs/**`, `docs/_config.yml`, `assets/**`, `references/**`, or `ops/**` will build and deploy the site to GitHub Pages.
- Only promote stable, reader-ready material into `docs/`. Keep drafts in `content/` until vetted against `raw/claims.md`.
- Canonical URLs are set in `docs/_config.yml` (`url` and `baseurl`). Do not change them unless the repo name or user/org changes.

### Release checklist

1. Ensure new or updated pages in `docs/` have correct front matter (layout, title, parent, nav_order) and cross-links.
2. Bump `docs/_config.yml: version` (semantic version, e.g., `0.2.0`).
3. Update `docs/changelog.md` with the new version and date.
4. Commit and push to `main`; verify the Pages workflow succeeds.
5. Tag and push: `git tag -a vX.Y.Z -m "Release vX.Y.Z" && git push --tags`.
6. Create a GitHub Release summarizing changes and linking to the live site.

Notes:
- Pages uses the artifact-based deployment (`actions/deploy-pages`); do not create or push to a `gh-pages` branch.
- Pages sites are public. If the repository is private, ensure the account plan allows Pages, and be aware the published site is visible publicly.
- Rollback: revert the offending commit or create a corrective commit and push to `main`; the next deployment will overwrite the site.
