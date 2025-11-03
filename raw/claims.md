# Claims Catalog

_Last fact-check: 2025-11-03_

## ChatGPT - Using Cursor’s Agent for Scientific Research_ A Playbook.md

### Cursor 2.0 platform
- Cursor 2.0 introduced a multi-agent workspace with the Composer model (marketed as four times faster than comparable agents) and supports up to eight parallel agents in isolated worktrees or remote machines; the release also added an Agent Review pane for auditing changes in one view.[^cursor-changelog]
- The same release graduated the in-editor browser to GA (with DOM capture), defaulted macOS agent commands into sandboxed terminals, and delivered voice control, background Plan Mode, and shareable Team Commands.[^cursor-changelog]
- Cursor now prunes most manual @-context panels in favor of self-gathered context and advertises 99.9 % reliability with instant startup for cloud agents.[^cursor-changelog]

### Integrations & ecosystem
- Cursor ships with Composer but also lets you assign external models from Anthropic, OpenAI, Google, xAI, and others once you provide API keys, so you can mix-and-match per agent or plan.[^cursor-models]
- Cursor lets you configure your own API keys for providers like OpenAI, Anthropic, Google, Azure OpenAI, and AWS Bedrock; however, some features—most notably the Agent—are unavailable when using custom keys. As an alternative to routing through your own keys, you can leverage vendor IDE extensions (e.g., Claude Code or the OpenAI Codex VS Code extension) to use your provider subscriptions directly.[^cursor-api-keys][^claude-code-overview][^openai-codex][^cursor-agent-custom-key][^cursor-api-keys-models-actions][^reddit-byoak]
- Guidance: Using custom (BYO) API keys in Cursor is not recommended if you rely on advanced features; Agent Mode is disabled when custom keys are used. Instead, install and use the Claude Code and/or OpenAI Codex VS Code extensions inside Cursor to access your provider accounts without sacrificing agent capabilities.[^cursor-agent-custom-key][^cursor-api-keys-models-actions][^claude-code-overview][^openai-codex][^author-empirical-claude-codex-in-cursor]
- Empirical note (author-tested): The Claude Code and OpenAI Codex VS Code extensions work well inside Cursor on the author’s setup, so there is no need to switch to stock VS Code to use them; as with any extension, compatibility can depend on Cursor build, OS, and extension versions—verify on your environment.[^author-empirical-claude-codex-in-cursor]
- AGENTS.md emerged mid-2025—led by Sourcegraph’s Amp team with participation from OpenAI Codex, Google’s Jules, Cursor, Factory, and others—as a vendor-neutral project brief; GitHub already indexes 20 k+ public repositories with the file, so Cursor and peer tools ingest it alongside README.md.[^upsun-agents][^agents-md]
- Claude Code does not automatically read AGENTS.md; Anthropic instructs users to include `@AGENTS.md` inside CLAUDE.md to reuse the same rules across Cursor and Claude.[^claude-web-bestpractices]
- Cursor’s improved agent harness highlights quality gains for GPT-5 Codex, but OpenAI Codex itself is a separate product that spans a CLI, IDE extension, and web client rather than a built-in Cursor feature.[^cursor-changelog][^openai-codex]
- GPT-5-Codex became the default Codex model on 2025-09-23; it is available through ChatGPT-authenticated Codex clients and the Responses API for API-key users.[^openai-codex-upgrades]
- Codex CLI is distributed as a Homebrew cask (`brew install --cask codex` and `brew upgrade --cask codex`); Homebrew now recommends the cask while keeping the legacy formula deprecated but still present.[^openai-codex-cli][^brew-codex]

### MCP & skills
- The Model Context Protocol (MCP) is an open standard (co-authored by Anthropic) that lets agent clients—including Cursor, Claude Code, and Codex—talk to tool servers over JSON-RPC; both Anthropic and Cursor publish guides for configuring remote MCP servers.[^mcp-intro][^anthropic-mcp]
- The community-maintained `claude-scientific-skills` repository ships 70+ MCP skills for domains like bioinformatics and materials science; they run inside Claude products but can be proxied into Cursor by registering the MCP server or using the Claude Code extension.[^claude-skills-news][^claude-skills-repo]
- The K-Dense scientific skills README currently lists 26 database connectors and 64 scientific package integrations—covering sources like PubMed, PubChem, UniProt, and AlphaFold DB—for Claude or MCP-enabled clients.[^claude-skills-counts]
- A bundled `scientific-context-initialization` skill automatically creates or updates AGENTS.md so Claude is prompted to use installed skills before attempting a task.[^claude-skills-context]

### Workflow notes
- Cursor forum guidance recommends labelling @ references precisely (e.g., `@style-guide`, `@example`) rather than relying on `@codebase`, so the reranker retrieves the right context.[^cursor-forum-prompts]
- A NSF project-summary experiment shared on the Cursor forum combined @-referenced source files, supplemental rule files, and Claude’s thinking mode—yielding richer drafts but also more hallucinations—underscoring the need for manual review.[^cursor-forum-research]

### Documentation hygiene
- Upsun’s analysis stresses that AGENTS.md arose to unify tool instructions, yet high-quality README.md documentation remains essential for both humans and agentic assistants.[^upsun-agents]

## Google Docs Editors — Markdown support
- Google Docs, Slides, and Drawings can automatically convert Markdown formatting (e.g., headings, emphasis, lists, links) when “Automatically detect Markdown” is enabled in Preferences. This helps paste‑in Markdown render as styled text for collaborators in Google Docs.[^google-docs-markdown]
- Some Google Docs builds also include Edit menu commands “Paste from Markdown” and “Copy as Markdown,” which enable conversion to/from Markdown for easier round‑tripping. Availability can vary by account and rollout waves.[^google-docs-markdown]

## Claude - compass_artifact_wf-5b39e094-007e-4e5c-8bfa-8ee030b5c540_text_markdown.md
- Cursor markets Composer as a low-latency agentic model that completes most turns in under 30 seconds while staying tuned for code-wide reasoning; for specialised research tasks, benchmark Claude or GPT models alongside it.[^cursor-blog-2-0]
- Plan Mode lets one model draft a plan and another execute it (foreground or background), while Team Commands push centrally managed rules to teammates—so you no longer juggle local `.cursorrules` files.[^cursor-changelog]
- Multi-agent execution supports up to eight parallel agents on isolated worktrees or remote machines, enabling subtasks like literature search, synthesis, and visualisation without file conflicts.[^cursor-changelog]
- The integrated browser, sandboxed terminals, and voice mode give agents web access, safer command execution, and hands-free prompting from inside the editor.[^cursor-changelog]
- MCP adoption in Cursor and Claude Code enables shared toolchains, but Claude Code still requires CLAUDE.md/Skills configuration and does not yet read AGENTS.md automatically.[^mcp-intro][^claude-web-bestpractices]
- K-Dense AI’s Claude scientific skills bundle depends on a Claude runtime; you can expose it to Cursor via the Claude Code extension or by registering the MCP server in `~/.cursor/mcp.json`.[^claude-skills-news][^claude-skills-repo]
- Anthropic positions Claude Haiku 4.5 for speed, Sonnet 4.5 as the default generalist, and Opus 4.1 for complex reasoning; the VS Code extension brings these models into VS Code-based IDEs such as Cursor.[^anthropic-models-overview][^anthropic-haiku45][^anthropic-sonnet45][^anthropic-opus41][^claude-code-overview]

## Gemini - Cursor for Scientific Research Playbook.md
- The playbook frames Cursor as model-agnostic: Composer is fast for repo-scale reasoning, yet you can route tasks to GPT-4/5 or Claude 4.5 models depending on context length and reasoning style.[^cursor-models][^cursor-blog-2-0][^anthropic-models-overview][^openai-codex-upgrades]
- OpenAI Codex operates alongside Cursor rather than inside it, supplying a CLI, IDE extension (VS Code/Cursor/Windsurf), web workspace, cloud task orchestration, and an SDK for scripted workflows via GPT-5-Codex.[^openai-codex][^openai-codex-cli][^openai-codex-cloud][^openai-codex-sdk][^openai-codex-upgrades][^openai-codex-changelog]
- Claude Code competes in the same space with terminal-first workflows, approvals for file changes, MCP support, and Skills; installing Anthropic’s VS Code extension inside Cursor lets you swap between Composer and Claude experiences.[^claude-code-overview][^claude-skills-news]

## Grok - Playbook- Using Cursor for Scientific Research.md
- Use Composer by default and add OpenAI or Anthropic API keys only when tasks benefit from GPT-4/5 or Claude 4.5 models; install the Claude Code extension separately if you want Anthropic’s assistant inside Cursor.[^cursor-models][^claude-code-overview]
- Cursor 2.0’s agent workspace supports up to eight concurrent agents with sandboxed terminals and the native browser, plus Plan Mode, voice control, and shareable Team Commands.[^cursor-changelog]
- MCP lets Cursor, Claude Code, and Codex reuse the same external tool servers, so configure once and share across workflows.[^mcp-intro]
- Claude Code users should maintain CLAUDE.md with `@AGENTS.md` to keep instructions in sync across assistants.[^claude-web-bestpractices]
- The Agent Review pane consolidates per-run diffs so you can inspect changes before committing.[^cursor-changelog]

## Grok - skills.md
- The Claude scientific skills expansion details MCP-based skill packs that extend Claude with discipline-specific workflows; load them via Claude Desktop or the VS Code extension (which also runs inside Cursor).[^claude-skills-news][^claude-skills-repo][^claude-code-overview]
- Installing Claude Desktop or the Claude Code VS Code extension and authenticating with Anthropic is required before those skills can execute.[^claude-code-overview][^claude-skills-news]
- As of 2025-11-03 the K-Dense scientific skills catalog documents 26 database connectors, 64 scientific packages, 7 integrations, 2 helper utilities, and 122 documented workflows.[^claude-skills-counts]
- The repository’s connectors span data sources such as PubMed, bioRxiv, ChEMBL, GEO, UniProt, and AlphaFold DB, while package skills wrap tooling like RDKit, Scanpy, DeepChem, and BioPython.[^claude-skills-counts]
- Workflow-focused skills include literature review, hypothesis generation, and experiment design patterns, and integration skills target platforms like Benchling, DNAnexus, Opentrons, LabArchives, LatchBio, OMERO, and Protocols.io.[^claude-skills-counts]
- K-Dense also maintains the `claude-skills-mcp` bridge so Cursor’s Composer agents can reach those skills via MCP.[^claude-skills-mcp-repo]
- Additional community-maintained Claude Skills directories exist, such as VoltAgent’s `awesome-claude-skills` list and related curated collections.[^community-claude-skills]

[^cursor-changelog]: Cursor, “New Coding Model and Agent Interface (2.0 changelog),” https://cursor.com/changelog/2-0 (accessed 2025-11-03).
[^cursor-models]: Cursor Docs, “Models,” https://cursor.com/docs/models (accessed 2025-11-03).
[^upsun-agents]: Upsun Developer Blog, “AGENTS.md: Why your README matters more than AI configuration files,” https://devcenter.upsun.com/posts/why-your-readme-matters-more-than-ai-configuration-files/ (published 2025-08-12).
[^agents-md]: AGENTS.md specification, https://agents.md/ (accessed 2025-11-03).
[^claude-web-bestpractices]: Anthropic Docs, “Claude Code on the web – best practices,” https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web#best-practices (accessed 2025-11-03).
[^openai-codex]: OpenAI, “Codex,” https://openai.com/codex (accessed 2025-11-03).
[^openai-codex-upgrades]: OpenAI, “Introducing upgrades to Codex,” https://openai.com/index/introducing-upgrades-to-codex/ (updated 2025-09-23).
[^openai-codex-cli]: OpenAI Developers, “Codex CLI,” https://developers.openai.com/codex/cli (accessed 2025-11-03).
[^brew-codex]: Homebrew Formulae, “codex,” https://formulae.brew.sh/cask/codex (accessed 2025-11-03).
[^mcp-intro]: Model Context Protocol, “Introduction,” https://modelcontextprotocol.io/docs/getting-started/intro (accessed 2025-11-03).
[^anthropic-mcp]: Anthropic Support, “Getting started with custom connectors using remote MCP,” https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp (accessed 2025-11-03).
[^claude-skills-news]: Anthropic, “Introducing Agent Skills,” https://www.anthropic.com/news/skills (published 2025-10-16).
[^claude-skills-repo]: K-Dense AI, “claude-scientific-skills,” https://github.com/K-Dense-AI/claude-scientific-skills (accessed 2025-11-03).
[^claude-skills-counts]: K-Dense AI, “claude-scientific-skills – What’s Included,” https://github.com/K-Dense-AI/claude-scientific-skills#-whats-included (accessed 2025-11-03).
[^claude-skills-context]: K-Dense AI, “claude-scientific-skills – scientific-context-initialization,” https://github.com/K-Dense-AI/claude-scientific-skills#scientific-context-initialization (accessed 2025-11-03).
[^claude-skills-mcp-repo]: K-Dense AI, “claude-skills-mcp,” https://github.com/K-Dense-AI/claude-skills-mcp (accessed 2025-11-03).
[^community-claude-skills]: VoltAgent, “awesome-claude-skills,” https://github.com/VoltAgent/awesome-claude-skills (accessed 2025-11-03).
[^cursor-forum-prompts]: Cursor Community Forum, “Cursor prompt engineering best practices,” https://forum.cursor.com/t/cursor-prompt-engineering-best-practices/1592 (accessed 2025-11-03).
[^cursor-forum-research]: Cursor Community Forum, “Anyone use Cursor for academic research writing?,” https://forum.cursor.com/t/anyone-use-cursor-for-academic-research-writing/57393 (accessed 2025-11-03).
[^google-docs-markdown]: Google Docs Editors Help, “Use Markdown in Google Docs, Slides, & Drawings,” https://support.google.com/docs/answer/12014036?hl=en (accessed 2025-11-03).
[^cursor-blog-2-0]: Cursor, “Cursor 2.0: Agent-first coding,” https://cursor.com/blog/2-0 (accessed 2025-11-03).
[^anthropic-models-overview]: Anthropic Docs, “Models overview,” https://docs.anthropic.com/claude/docs/models-overview (accessed 2025-11-03).
[^anthropic-haiku45]: Anthropic, “Introducing Claude Haiku 4.5,” https://www.anthropic.com/news/claude-haiku-4-5 (published 2025-10-15).
[^anthropic-sonnet45]: Anthropic, “Introducing Claude Sonnet 4.5,” https://www.anthropic.com/news/claude-sonnet-4-5 (published 2025-09-29).
[^anthropic-opus41]: Anthropic, “Claude Opus 4.1,” https://www.anthropic.com/news/claude-opus-4-1 (published 2025-08-05).
[^claude-code-overview]: Anthropic Docs, “Claude Code overview,” https://docs.claude.com/en/docs/claude-code/overview (accessed 2025-11-03).
[^openai-codex-cloud]: OpenAI Developers, “Codex Cloud,” https://developers.openai.com/codex/cloud (accessed 2025-11-03).
[^openai-codex-sdk]: OpenAI Developers, “Codex SDK,” https://developers.openai.com/codex/sdk (accessed 2025-11-03).
[^openai-codex-changelog]: OpenAI Developers, “Codex changelog,” https://developers.openai.com/codex/changelog (accessed 2025-11-03).
[^cursor-api-keys]: Cursor Docs, “API keys,” https://cursor.com/docs/settings/api-keys (accessed 2025-11-03).
[^cursor-agent-custom-key]: Cursor Community Forum, “Cursor agent Mode with custom Claude API key,” https://forum.cursor.com/t/cursor-agent-mode-with-custom-claude-api-key/67062 (accessed 2025-11-03).
[^cursor-api-keys-models-actions]: Cursor Community Forum, “API Keys work on which models/actions? – #2,” https://forum.cursor.com/t/api-keys-work-on-which-models-actions/45041/2 (accessed 2025-11-03).
[^reddit-byoak]: Reddit, “Cursor effectively killed the ‘Bring Your Own API Key’ option,” https://old.reddit.com/r/cursor/comments/1mhp9jz/cursor_effectively_killed_the_bring_your_own_api/ (accessed 2025-11-03).
[^author-empirical-claude-codex-in-cursor]: Empirical verification by the repository author (2025-11-03) on macOS using Cursor 2.x (build unspecified). Claude Code and OpenAI Codex VS Code extensions were installed via Cursor’s Extensions pane, activated, and used for file‑scoped commands without observed issues. Note: extension support may vary by Cursor build, OS, and extension versions; please verify in your own setup.
