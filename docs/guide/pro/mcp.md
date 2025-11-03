---
title: MCP And Scientific Skills (Advanced)
layout: default
grand_parent: Guide
parent: Pro
---


# MCP And Scientific Skills (Advanced)

Use the Model Context Protocol (MCP) to connect domain tools—literature search, bio/chem/materials databases, and specialized analysis skills—into your IDE agent. Start with Core workflows; add MCP only when a tool unblocks real work.

When to use MCP
- You need searchable databases (e.g., PubMed, UniProt) or structured APIs.
- You want repeatable tool access (e.g., the same query across branches).
- Your IDE agent supports MCP connections and tool permissioning.

Basics (what MCP is)
- MCP is an open standard for tool servers that agent clients can call. It exposes tools over JSON‑RPC; clients like Cursor, Claude Code, and Codex can register servers and invoke tools.[^mcp-intro][^anthropic-mcp]

Guardrails
- Cite sources surfaced by tools; do not treat tool outputs as claims without verification. See [Accuracy]({{ site.baseurl }}{% link guide/core/accuracy.md %}).
- Log non‑obvious assertions in your project’s `claims.md` with provenance.
- Keep credentials out of the repo; use env files or your OS keychain.

Configure a server (approval‑gated)
```text
Task: Configure a literature MCP server and run a test query.

Safety rules:
- Propose exact file edits and commands; wait for my reply exactly: CONFIRM APPLY.
- Only edit: ops/mcp/** and .env (if needed). Do not touch manuscript/.
- Do not send local files to remote servers.

Steps:
1) Propose a minimal config block for an MCP server (name, host, auth)
2) Show the command to register it with the IDE agent
3) Propose a test call (e.g., PubMed search), with expected fields
4) On CONFIRM APPLY, write config, run the test, and save results to analysis/reports/mcp-test.json
```

Example minimal config (illustrative)
```toml
# ops/mcp/literature.toml
[server]
name = "literature"
url = "https://example-mcp.org/jsonrpc"

[auth]
method = "token"
env = "MCP_LIT_TOKEN"
```

Verify and record
- Save a short `analysis/reports/mcp-test.md` summarizing the query, parameters, result count, and 2–3 example records with citations.
- Add any new claims to `claims.md` with sources.

Troubleshooting
- Connection errors: check URL, auth token, and network allow‑lists.
- Schema mismatches: inspect the tool’s JSON schema; adjust parameters.
- Rate limits: add backoff and keep test queries small.

What’s next
- Continue to [Integrations]({{ site.baseurl }}{% link guide/pro/integrations.md %}) for IDE extensions and provider‑specific tooling.

Change log (drafting)
- 2025-11-03: Added front matter, overview, guardrails, approval‑gated setup prompt, and links; added citations.

[^mcp-intro]: Model Context Protocol, “Introduction,” https://modelcontextprotocol.io/docs/getting-started/intro (accessed 2025-11-03).
[^anthropic-mcp]: Anthropic Support, “Getting started with custom connectors using remote MCP,” https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp (accessed 2025-11-03).
