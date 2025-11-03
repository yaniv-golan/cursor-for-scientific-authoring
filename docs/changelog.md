---
layout: default
title: Changelog
parent: Cursor for Scientists
nav_order: 45
---

# Changelog

All notable changes to this guide are documented here. We use semantic versioning. Tags are created as `vMAJOR.MINOR.PATCH`.

## [0.1.0] - Unreleased

- Initial public structure for the site under `docs/`.
- GitHub Pages CI via Actions (`.github/workflows/pages.yml`).
- Set canonical URL and base URL in `_config.yml`.
- Added About page with version and build date.

---

Release process:

- Merge changes to `main`.
- Tag a release: `git tag -a vX.Y.Z -m "Release vX.Y.Z" && git push --tags`.
- Create a GitHub Release linking to this changelog and summarizing highlights.

