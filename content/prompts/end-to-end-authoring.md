# Prompt: End‑to‑End Guide Authoring Orchestrator (Restartable)

You are assisting as a file‑first authoring agent. Generate and refine the guide section‑by‑section, keeping the whole work aligned and consistent across runs. This prompt is restartable: if interrupted, run it again to resume from the last incomplete section without losing work.

Required context to load via @file:
- @AGENTS.md
- @content/reference-toc.md
- @raw/claims.md
- Draft targets live under `content/guide/…` (Core/Plus/Pro), with additional pages in `content/policies/` and `content/exercises/`.

Ground rules (from AGENTS.md + house style):
- File‑first edits only; prefer `@file` context over chat memory.
- Treat `raw/claims.md` as the fact‑checked source of truth. Only include non‑obvious claims that are supported there or add them to `raw/claims.md` first (with sources or clearly labeled empirical notes).
- Do not change `raw/` except `raw/claims.md` when adding vetted claims.
- This repository’s layout (docs/content/raw) is for the guide only; do not present it as a research project template. Use the example project layout shown in the TOC for guidance only.
- For any numeric outputs or analysis examples, require: “use code to calculate”, show code and outputs; explain in plain language.
- Keep tone instructional, friendly, concise, appropriate for researchers (some non‑programmers).

Section planning and mapping (use this canonical mapping):
- Overview → content/guide/index.md
- Core → content/guide/core/
  - Quick Start → quick-start.md
  - Writing In Markdown → writing-markdown.md
  - Accuracy → accuracy.md
  - Managing Sources → managing-sources.md
  - Agent‑Written Code (analysis) → analysis.md
  - Project Rules (AGENTS.md) → project-rules.md
  - Endgame → endgame.md
  - Checklists → checklists.md
- Plus → content/guide/plus/
  - Git → git.md
  - Branching → branching.md
- Pro → content/guide/pro/
  - MCP → mcp.md
  - Integrations → integrations.md
  - Multi‑agent → multi-agent.md
- Policies → content/policies/data-governance.md
- Exercises → content/exercises/first-hour.md

Progress ledger (for restartability):
- Maintain YAML at `ops/authoring-progress.yml` with entries:
  - id: slug (e.g., core/quick-start)
  - path: file path
  - status: pending | in_progress | draft | complete
  - updated: ISO datetime
  - notes: short summary of last change
- Also add lightweight YAML front matter to each content file with `status` (draft/complete) where safe; otherwise, infer status from file presence and length.

Algorithm per run:
1) Load @content/reference-toc.md and compute the ordered list as Overview → Core → Plus → Pro, inserting Policies (Data Governance) just before Analysis, and Exercises in Core after Quick Start.
2) Read `ops/authoring-progress.yml` if present; otherwise, initialize it from the mapping above.
3) For each section in order, find the first item with status not `complete`:
   - Set status to `in_progress` in the ledger; write back to `ops/authoring-progress.yml`.
   - Read any existing draft file; preserve good content and improve incrementally (do not wipe).
   - Draft or refine the section so it aligns with:
     - Claims in @raw/claims.md (cite non‑obvious items with footnotes that mirror the sources listed there).
     - Structure and terminology established in previously completed sections.
     - Cross‑links to sibling sections using repo‑relative paths.
     - TOC guidance (don’t introduce Git/MCP too early; keep the on‑ramp simple).
     - “Use code to calculate” pattern for any example numbers or plots.
     - Reproducibility guardrails (seeds, lockfiles) where relevant.
   - End each section with a short “What’s next” that points to the next TOC item.
   - Update or add YAML front matter `status: draft` (or `complete` if mature).
   - Set status to `draft` (or `complete`) in the ledger with a one‑line summary.
4) Output a concise run report summarizing: completed/updated section, links, and next target.
5) On subsequent runs, repeat from step (1). If everything is complete, suggest final publishing to `docs/` with appropriate front matter.

Definition of Done per section:
- Aligns with the TOC and previously written sections; consistent terminology.
- Non‑obvious claims cite sources; any new claims are first added to @raw/claims.md.
- Includes cross‑links to related sections and references.
- Incorporates accuracy guardrails and the “use code to calculate” instruction where applicable.
- Ends with a “What’s next” pointer.

Initial targets for Core (first passes expected within 30–60 minutes total):
- Quick Start: Day‑0 prerequisites, first‑hour exercise (IMRaD from 3 PDFs; one table and optional figure; citation audit; export), file‑scoped prompts only, no‑code by default with optional low‑code later.
- Writing In Markdown: IMRaD scaffolds, citations, BibTeX/CSL JSON, Pandoc export.
- Accuracy: claims log, read–extract–cite, numeric rubric.
- Data Governance (Policies): approvals, local‑first guidance, privacy notes.
- Analysis: environment setup, seeds, lockfiles, “use code to calculate,” save figures/tables.

Operational notes:
- Never modify `docs/` from this drafting loop. Publishing is a separate step.
- Keep diffs small and focused; include a short change log at the bottom of each file during drafting.
- If a section depends on facts not yet in @raw/claims.md, pause and add them there first (with sources or empirical note), then continue.

Run now: pick the next incomplete section from the ledger (or initialize it), then draft/refine it according to the above. After writing, update `ops/authoring-progress.yml`, and print a brief run report with the next section queued.
