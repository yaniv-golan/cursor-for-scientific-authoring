---
layout: default
title: Style Guide
parent: Resources
nav_order: 10
---

# Style Guide

Define tone, terminology, and formatting conventions so pages read consistently and help non‑coders move fast without confusion.

## Voice and tone
- Plain, instructional, and concise. Prefer short sentences and verbs that prompt action.
- Default to “simple‑first.” Put advanced paths behind an “Optional” or “Advanced” label.
- Avoid developer jargon on reader pages. Explain necessary terms in one line.
- Use present tense and active voice (e.g., “Review and approve the preview of changes”).

## Terminology (use these forms)
- file‑scoped prompt — preferred term; explains the safety constraint.
- clear preview of changes — preferred over diff/patch.
- Starter Pack — the downloadable minimal template (.zip).
- claims log (`claims.md`) — the minimal list of non‑obvious statements and sources.
- use code to calculate — exact phrase for numeric reproducibility.
- local‑first — when discussing privacy; clarify exceptions with links.

## Capitalization
- Page titles: Title Case (e.g., “Writing In Markdown For Science”).
- Sections and callouts: Sentence case unless a proper noun.
- Product names: Cursor, GitHub, Google Docs.

## Jargon to avoid (use substitutes)
- diff/patch → say “clear preview of changes”.
- manifest → say “proposed change list”.
- repo layout → say “this guide’s folder structure” or “your paper folder”.
- pipeline/CI → say “automated export checks” (only in Plus/Pro).
- LLM/context window → say “model” and “what the agent can read”.
- CRUD/mutate → say “add”, “edit”, “rename”, “delete”.

## Style rules
- Links: use internal link tags `[Text]({{ site.baseurl }}{% link path.md %})` so URLs survive renames.
- Prompts: fenced code blocks with language `text`. Keep self‑contained with Task, Safety rules, Steps.
- Numbers: “use code to calculate”, show code and outputs, one‑sentence plain‑language explanation.
- Sources: cite non‑obvious claims; keep `claims.md` up to date.
- Privacy: add a brief note and link to Cursor’s Data Use and Review pages when relevant.

## Examples
- Preferred: “Type `@` to reference files, then select the exact file.”
- Preferred: “Open Quick Start and unzip the Starter Pack.”
- Avoid: “Copy `content/templates/...` into your repo.”
- Avoid: “Review the diff and apply the patch.” → “Review the clear preview of changes and approve.”

## Page checklist
- Audience and goal in the first two lines.
- One main path, optional advanced path clearly labeled.
- Cross‑links to Core pages where relevant.
- No repo‑internal paths on reader pages; use actions and links instead.
