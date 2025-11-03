# Contributing

Thank you for your interest in improving the Cursor for Scientists playbook! We welcome contributions of all sizes—from typo fixes to new case studies.

## Ways to contribute

- **Discuss**: Open a GitHub Discussion to propose topics, ask questions, or share experiences.
- **Triage**: Help organize `raw/` notes into `content/` outlines.
- **Draft**: Write drafts under `content/` and promote to `docs/` when ready.
- **Review**: Comment on pull requests and improve the clarity or accuracy of existing material.

## Workflow

1. Fork the repository and create a feature branch.
2. If you are drafting new guidance, start from `content/` and promote it into `docs/` when it is ready for publication.
   - See “Promoting drafts to the site” below.
3. Follow the style guidelines in `docs/resources/style-guide.md` (coming soon).
4. Run `markdownlint` (or another linter) locally if you have it installed.
5. Submit a pull request that explains the intent of your change.

## Releases & Publishing

This site is published with GitHub Pages via a GitHub Actions workflow located at `.github/workflows/pages.yml`.

- What triggers a publish: any push to `main` that changes files under `docs/**`, `docs/_config.yml`, `assets/**`, `references/**`, or `ops/**`.
- Where it builds from: `docs/` (the reader-facing site). Drafts live under `content/` and are not published until promoted into `docs/`.
- Where it deploys: GitHub Pages environment for this repository. Pages sites are public, even when the repo is private.

### Cutting a release (semantic versioning)

1. Promote ready content from `content/` into `docs/` and ensure navigation and cross-links are correct.
2. Update `docs/_config.yml` and bump `version:` (e.g., `0.1.1`).
3. Update `docs/changelog.md` with a new entry for the version. Include the date (YYYY-MM-DD) and highlights.
4. Commit and push to `main`. Wait for the “Pages build and deployment” workflow to pass.
5. Tag the release and push tags:
   - `git tag -a vX.Y.Z -m "Release vX.Y.Z" && git push --tags`
6. Create a GitHub Release referencing `docs/changelog.md` and linking to the live site.

### Local preview (optional)

You can run Jekyll locally to preview the site:

```
gem install bundler jekyll
bundle init
bundle add jekyll just-the-docs jekyll-remote-theme
JEKYLL_ENV=development bundle exec jekyll serve --source docs --destination _site
```

Or use a containerized environment that runs Jekyll with the `docs/` source.

## Promoting drafts to the site

We keep in-progress work under `content/` and publish stable pages into `docs/`.

- Front matter requirements in `content/**` to be eligible for promotion:
  - `---` fenced YAML front matter
  - `title: ...`
  - `status: complete`
- Run a dry-run preview first:
  - `make promote-dry` (or `python3 ops/promote.py --dry-run`)
- Publish all eligible pages:
  - `make promote` (or `python3 ops/promote.py`)
- Publish only selected files:
  - `make promote-only FILES='content/guide/core/quick-start.md content/guide/core/accuracy.md'`

What the promoter does
- Copies eligible files to `docs/**` using path rules:
  - `content/guide/**` → `docs/guide/**`
  - `content/exercises/**` → `docs/getting-started/**`
  - `content/policies/**` → `docs/resources/**`
- Adjusts front matter for Jekyll navigation:
  - Ensures `layout: default`, removes `status`
  - Sets `grand_parent`/`parent` for Guide/Core/Plus/Pro; Getting Started; Resources
  - Assigns `nav_order` for core pages (Quick Start=10, Writing Markdown=20, Accuracy=30, Managing Sources=40, Analysis=50, Checklists=60, Project Rules=70, Endgame=80)
- Link tip: use `{{ '/path/' | relative_url }}` in Markdown links so they work under the project `baseurl`.

Note: do not modify files in `raw/` (except updating `raw/claims.md` per `AGENTS.md`).

## Commit conventions

- Use descriptive commit messages (e.g., `docs: add reproducible workflow outline`).
- Keep pull requests focused—small, incremental improvements are easier to review.

## Need help?

If you are unsure how to contribute, open an issue or discussion and tag a maintainer. We are happy to help you get started.
