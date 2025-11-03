# Playbook: Using Cursor for Scientific Research

This concise guide helps non-coders use Cursor 2.0—an agent-first research workspace powered by the in-house Composer model—for scientific work. Focus: Orchestrate Cursor’s autonomous agents (up to eight in parallel) to run literature reviews, synthesize findings, and update Markdown deliverables with instructions like: "Research topic X, write findings to report.md with 2+ citations per claim in APA format."

## 1. Setup Basics
- **Install Cursor**: Download from cursor.com; sign up with email/GitHub. The 2.0 interface opens to an Agent Home where Composer plans work, with the editor and file explorer still available for review.
- **Project Setup**: Create a folder per topic; use .md files for reports (simple formatted text).
- **AI Integrations**:
  - Composer (built-in) is the default low-latency agent for coding and research tasks.
  - Add OpenAI or Anthropic API keys only if you need GPT-4/5 or Claude models alongside Composer; install the Claude Code extension separately if you want Anthropic’s terminal/VS Code assistant inside Cursor.[^claudecode]
  - Switch models per agent when you want varied perspectives (e.g., Composer for fast iteration, Claude Sonnet 4.5 for long-context synthesis).

## 2. Key Features & Integrations
- **Agent Workspace & Composer**: 2.0 centers the workflow on Composer, Cursor’s native model, and supports up to eight concurrent agents with sandboxed terminals and the native browser.[^cursor20]
- **Plan Mode, Voice, Team Commands**: Draft plans with one model, build with another (even in the background), issue instructions by voice, and push shared Team Commands instead of maintaining local `.cursorrules`.[^cursor20][^cursor-team]
- **MCP (Model Context Protocol)**: Anthropic’s open standard for connecting agent clients (Claude Code, Claude Desktop, OpenAI Codex, Cursor) to the same external tools. Configure servers once via Cursor’s MCP settings or the Claude Code extension and reuse them across workflows.[^mcp]
- **Claude Skills for Science**: Install the Claude Code extension (or Claude Desktop) and enable the K-Dense-AI/claude-scientific-skills library there; the skills run inside Anthropic’s agents and can operate alongside Cursor when the extension is open. Examples: Literature Review (PubMed searches), Hypothesis Generation, Data Analysis. Prompt Claude Code: "Use Literature Review skill to query bioRxiv on Y; summarize in findings.md."
- **AGENTS.md**: Create this file in project root for guidelines (e.g., citation rules, workflows). Structure:
  ```
  # AGENTS.md
  ## Guidelines
  - Cite 2+ reputable sources per claim (APA with links).
  - Use skills: Literature Review, etc.
  ## Workflow
  1. Research. 2. Summarize. 3. Write to file.md.
  ```
  Reference in instructions: "Follow AGENTS.md: Research Z to report.md."
  - If you run Claude Code alongside Cursor, add `CLAUDE.md` with `@AGENTS.md` inside so both assistants reference the same rules.[^claude-agents]

## 3. Research Workflow Steps
1. **Define Task**: In Chat/Composer: "Research impacts of AI on drug discovery using the Claude Code extension with scientific skills enabled."
2. **Instruct Output**: "Write summary to overview.md with pros/cons; cite 2+ PubMed sources in APA."
3. **Enforce Quality**: Add: "Every claim needs 2+ citations; use IMRAD structure."
4. **Iterate**: Review file, then: "Add ethics section with recent studies."
5. **Advanced Chaining**: "Generate hypotheses from overview.md using Hypothesis skill, then analyze."

## 4. Best Practices
- Be specific in instructions (file names, formats) for better results.
- Start small; organize folders (e.g., /reports).
- Use parallel agents when tasks can run independently (e.g., one gathers papers while another drafts syntheses).[^cursor20]
- Trust Cursor’s automatic context gathering; use `@file.md` when you need to pin a specific source for the agent.
- Open the Agent Review pane after each run to inspect a unified diff of every modified file before committing.[^cursor20]
- Switch models for perspectives; backup .md files.
- Privacy: Avoid sensitive data.
- Sources: Cursor forums, GitHub for more skills/workflows.

[^mcp]: Model Context Protocol. (2024). *Getting started*. https://modelcontextprotocol.io/docs/getting-started/intro
[^claudecode]: Anthropic. (2025). *Claude Code overview* – terminal and VS Code workflows. https://docs.anthropic.com/claude/docs/claude-code-overview
[^claude-agents]: Anthropic. (2025). *Claude Code on the web – best practices*. https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web#best-practices

[^cursor20]: Cursor. (2025, Oct 29). *New coding model and agent interface* (2.0 changelog). https://cursor.com/changelog/2-0
[^cursor-team]: Cursor. (2025). *Team Commands*. https://cursor.com/docs/team/commands
