# Using Cursor to Author Scientific Papers — Reference TOC

> Scope: This is the guide’s reference Table of Contents. It outlines an incremental path: start with vanilla Cursor and Markdown, then add Git, MCP skills, and optional IDE integrations. It recommends a project layout for data work (distinct from this repository’s layout).

## Start Here (Overview)
- Who it’s for (non‑coders first) and what to expect
- No‑code by default; low‑code analysis optional later
- Copy the minimal project starter; short AGENTS.md rules
- Pointers to Quick Start and the First‑Hour exercise

## Why Cursor For Papers
- File-first workflow vs. chat memory
- Precise, auditable edits (diffs, rollbacks)
- Working in Markdown as the source of truth
- Use local files for long-term context across sessions
- What Cursor is not (and when to use other tools)
- Decision: When to use Cursor vs ChatGPT web vs Claude Code vs Codex
- Decision: Local agent vs cloud agent (data sensitivity, approvals)

## Day‑0 Prerequisites (Before Quick Start)
- Cursor installed; sign-in complete
- Provider plan ready (OpenAI/Anthropic/etc.) if using external models
- Storage location chosen for your paper project (local folder)
- Optional installs for advanced paths: Git; Python or R; Pandoc; LaTeX
- Goal: a first IMRaD stub and one figure within 30–60 minutes
- Project starter: copy a minimal template folder and AGENTS.md

## Data Governance and Privacy
- Understand what data agents can access (local vs cloud operations)
- Use file‑scoped prompts; avoid pasting sensitive data into chat
- Approvals: review commands/code before execution; keep logs
- Prefer local processing for sensitive data; verify provider policies

## Core

### Quick Start (Vanilla Cursor)
- Create a paper workspace and minimal layout (not this repo’s layout)
- Configure available models in Cursor (Composer)
- Default path is no‑code; optional low‑code analysis later
- Copy the minimal project template and a minimal AGENTS.md
- Draft a paper outline in Markdown
- Make safe edits with inline diffs and file-scoped prompts
- Save checkpoints without Git (local history, snapshots)
- First‑hour guided exercise: outline IMRaD from 3 PDFs, generate one table and one figure from a CSV, run a citation audit, and export

### Writing In Markdown For Science
- IMRaD scaffolding and section templates
- Figures, tables, equations, and callouts
- Inline citations, footnotes, and reference lists
- Connect Markdown citations to a `.bib` file (Zotero/Mendeley) and a CSL style; keep `references/` as the bibliographic source of truth
- Manage a `references/` folder and citation styles
- Export options (Markdown → journal formats via Pandoc/LaTeX)
- Citation tooling decision: BibTeX vs CSL JSON vs Zotero export

### Accuracy, Evidence, and Hallucination Control
- Grounded, file-scoped prompts; avoid ad‑hoc chat memory
- Read–extract–cite workflow (quotes, paraphrases, summaries)
- Track a simple claims log in `claims.md`
- Verification checklists before merging agent edits
- For any numeric result, explicitly add: “use code to calculate” and require the model to show code and outputs
- When to stop and manually read the primary source
- Numeric results rubric (units, CI/SE, sample size, method)

### Managing Sources And Local Corpora
- Organize PDFs, notes, and data artifacts
- Create synthesis notes the agent can reliably use
- Prevent context drift: `@file` references vs. ad‑hoc chat
- De-duplication and source hygiene

### Agent‑Written Code with Minimal Coding
- What you can do in Cursor without prior programming
- Prompt patterns to generate and run analysis code safely
  - “Use code to calculate”; “show code and outputs”; “explain each step in plain language”
- Loading data (CSV/TSV, Excel) and basic cleaning
- Descriptive statistics, comparisons, and simple modeling
- Plotting and visualization (figures saved to `analysis/figures/`)
- Saving results as Markdown tables and embedding in the manuscript
- Reproducibility guardrails (inputs, scripts, parameters, random seeds)
- Install environment: Python or R runtime; approve executions consciously
- Dependency lockfiles: `environment.yml` (conda/mamba) or `renv.lock` (R)
- Recommended project layout for data work:

```
project/
  AGENTS.md
  claims.md
  manuscript/
    sections/          # 01-intro.md, 02-methods.md, ...
    figures/           # paper-ready images
    tables/            # paper-ready tables (CSV/MD)
  data/
    raw/               # original, read-only
    external/          # third-party data
    interim/           # cleaned subsets / features
    processed/         # analysis-ready datasets
  analysis/
    notebooks/         # Markdown notebooks (with code blocks)
    scripts/           # generated Python/R scripts
    reports/           # auto-generated MD/HTML summaries
    figures/           # exploratory plots
    tables/            # exploratory tables
  references/
```

### Project Rules With AGENTS.md
- Capture norms, tone, and acceptance criteria in `AGENTS.md`
- File‑constrained tasks and safe‑edit patterns
- Reuse rules across tools (e.g., reference `@AGENTS.md` from `CLAUDE.md`; Claude Code does not auto-read `AGENTS.md`)
- Examples: reproducibility, citation, and style policies

## Plus

### Versioning With Git (Inside Cursor)
- Initialize Git, stage granular changes, write useful commit messages
- Inspect diffs, revert, and bisect mistakes
- Sync (push/pull) and lightweight collaboration
- Automate pre-commit checks (spelling, links, style) for Markdown

### Exploratory Branching For Alternates (Optional)
- Branching strategies for competing hypotheses/frames
- Isolate risky rewrites; merge back with review
- Use branches as preregistration or proto-registrations
- Archive abandoned directions without losing work

## Pro

### MCP and Scientific Skills
- What MCP is and when to use it
- Register MCP servers in Cursor for domain tasks
- Examples: literature, bio/chem/materials databases; analysis skills
- Guardrails for tool output, attribution, and citations
- Mini‑lab: install and verify a skill; record provenance

### Integrations: Claude Code & OpenAI Codex
- When to use vendor IDE extensions alongside Cursor
- Leverage Claude Code skills via the extension
- Use the OpenAI Codex VS Code extension for complementary tasks
- Built‑in models vs. extensions: using custom API keys in Cursor can disable some features (e.g., Agent); extensions let you use provider subscriptions and skills directly
- Extensions often work in Cursor; verify extension support for your build
- Composer agent vs vendor extensions: clarify capability boundaries
- Stay file‑first and avoid fragmented context

### Multi-Agent Workflows (Optional)
- Planning vs. executing agents; keep edits isolated
- Parallel tasks that won’t trample files
- Up to eight concurrent agents; isolation via worktrees/remote
- Agent Review pane, Plan Mode, and integrated browser as accelerants (optional)
- Review and reconcile agent outputs; add strict review gates

### Endgame: Journal‑Ready Output
- Target author guidelines and templates
- Final citation audit and figure/table checks
- Reproducibility bundle (data/code/prompts/diffs)
- Preprint vs. submission packaging

### Checklists And Prompt Patterns
- Day‑0 setup checklist (workspace, rules, sources)
- Section drafting checklist (Intro/Methods/Results/Discussion)
- Verification and citation checklist
- Data analysis prompt patterns (generate → run → verify → summarize)
- One‑page “red team your draft” checklist

### Case Studies And Recipes
- Rapid literature review → structured related work
- Methods transcription → reproducible Markdown
- Results narrative from tables/figures without overclaiming
- Domain-specific mini-guides

### Troubleshooting And Safety
- Common pitfalls (fabricated citations, stale context, over‑refactoring)
- Privacy, data handling, and sensitive information
- Performance tuning (chunking, file splits, indexing)
- When to escalate to manual review or SMEs
