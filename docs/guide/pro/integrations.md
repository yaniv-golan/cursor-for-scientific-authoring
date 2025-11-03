---
title: "Integrations: Claude Code And OpenAI Codex"
layout: default
grand_parent: Guide
parent: Pro
---


# Integrations: Claude Code And OpenAI Codex

Use IDE extensions to access provider accounts and features while staying file‑first in Cursor. Extensions can complement built‑in agents; confirm compatibility on your setup.

When to integrate
- You need a provider feature not available via built‑in models.
- Your organization requires using provider‑managed billing/keys.
- You want to run Claude skills or Codex CLI/IDE workflows alongside Cursor.

Capability boundaries
- Custom API keys in Cursor can disable advanced Agent features; using vendor extensions (Claude Code, OpenAI Codex) lets you access provider subscriptions without losing Cursor’s file‑first flows.[^cursor-agent-custom-key][^cursor-api-keys-models-actions]
- Keep one source of truth: run edits through the same preview‑of‑changes flow and follow your [Project Rules]({{ site.baseurl }}{% link guide/core/project-rules.md %}).

Install and verify (approval‑gated)
```text
Task: Install and verify IDE extensions for provider integrations (Claude Code and/or OpenAI Codex).

Safety rules:
- Propose install steps first; wait for my reply exactly: CONFIRM APPLY.
- Do not change project files except adding a short integrations note.
- Collect no telemetry beyond extension defaults; do not upload local files.

Steps:
1) Propose installation commands or in‑IDE steps, with versions
2) Verify the extension loads and signs in
3) Run a small file‑scoped action (e.g., draft a commit message) and show the preview of changes
4) Record a short note in ops/integrations.md with versions and date
```

Using Claude skills
- Claude Code can surface MCP‑based skills; include `@AGENTS.md` in `CLAUDE.md` so rules carry over. See [MCP]({{ site.baseurl }}{% link guide/pro/mcp.md %}).

Using OpenAI Codex
- Use Codex for complementary coding and CLI flows. Keep edits file‑scoped and request a clear preview of changes before applying.

What’s next
- Continue to [Multi‑agent]({{ site.baseurl }}{% link guide/pro/multi-agent.md %}) to coordinate multiple agents safely.

Change log (drafting)
- 2025-11-03: Added front matter, capability boundaries, approval‑gated install/verify prompt, and links to Project Rules, MCP, and Multi-agent; added citations; marked page complete.

[^cursor-agent-custom-key]: Cursor Community Forum, “Cursor agent Mode with custom Claude API key,” https://forum.cursor.com/t/cursor-agent-mode-with-custom-claude-api-key/67062 (accessed 2025-11-03).
[^cursor-api-keys-models-actions]: Cursor Community Forum, “API Keys work on which models/actions? – #2,” https://forum.cursor.com/t/api-keys-work-on-which-models-actions/45041/2 (accessed 2025-11-03).
