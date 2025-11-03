# The Researcher's Guide to Cursor: Transform Your AI IDE into a Scientific Research Powerhouse

Cursor isn't just for coders anymore. This revolutionary AI-powered editor can become your autonomous research assistant, managing literature reviews, writing reports, and organizing findings—all through natural language instructions and markdown files. **The key insight**: Cursor's agentic capabilities let you delegate entire research workflows with simple prompts like "research climate change impacts, analyze 20+ papers, and write findings to report.md with APA citations."

This playbook teaches semi-technical researchers how to harness Cursor's file system integration, Model Context Protocol servers, and scientific skills to automate research tasks without writing code. You'll learn to configure Cursor as a research workstation that autonomously searches databases, synthesizes literature, generates hypotheses, and produces publication-ready documents.

## Why Cursor for scientific research, not just coding

**Cursor 2.0** (released October 2025) represents a paradigm shift toward agent-first workflows where AI autonomously handles complex, multi-step tasks. Unlike traditional editors, Cursor treats AI agents as first-class collaborators with powerful capabilities specifically valuable for research:

**Agentic autonomy** means Cursor can work independently on research tasks. The Composer Agent executes complex workflows—searching databases, reading papers, extracting data, synthesizing findings—completing most tasks in under 30 seconds. With **Agent Mode** (Cmd/Ctrl + .), you can instruct Cursor to "conduct a systematic literature review on CRISPR applications" and it autonomously navigates the process, creates files, runs searches, and generates structured reports. Composer is tuned for code-aware reasoning and advertises 4× faster responses than similarly capable models, but for highly specialized scientific analysis you should still experiment with Claude or GPT variants to see which reasoning style fits.[^cursor-toolbelt] 

**Native markdown mastery** makes Cursor ideal for research documentation. All agent plans generate as markdown files with task lists and references.

**Plan Mode & Team Commands** let one model draft plans while another executes them, plus push shared rules to entire teams via the Cursor dashboard so you no longer maintain local `.cursorrules` files.[^cursor20][^cursor-team]

 The editor provides rich markdown rendering, supports mermaid diagrams, and enables AI-assisted prose writing. Research reports, literature reviews, and documentation live as markdown files that Cursor reads, edits, and organizes intelligently.

**Multi-agent parallel execution** allows running up to 8 agents simultaneously on different research subtasks. One agent searches PubMed while another queries arXiv, a third synthesizes findings, and a fourth generates visualizations—all without interference. Agents run in isolated git worktrees or remote sandboxes so they don’t clobber each other’s changes.[^cursor-multi]

**Integrated toolbelt** equips each agent with a native browser for testing and evidence capture plus sandboxed terminals that are GA on macOS, giving you safer automation for scripts and web verification without leaving the IDE.[^cursor-toolbelt]

**Voice-driven control** lets you speak to Cursor’s agents for hands-free prompting—a surprisingly useful option when you’re juggling lab equipment or reviewing PDFs away from the keyboard.[^cursor-voice]

**Deep context understanding** through codebase-wide semantic search means Cursor understands relationships between files, can reference multiple documents simultaneously using @ symbols, and maintains context across your entire research project. Reference previous reports, datasets, and notes effortlessly.

**Plan Mode** revolutionizes research project planning. The agent researches your existing files, asks clarifying questions, then generates detailed markdown plans with step-by-step approaches. You edit the plan, then execute—creating a collaborative research workflow where you guide strategy while AI handles execution.

## Understanding the technology stack

### Model Context Protocol: Your research database gateway

The **Model Context Protocol (MCP)** is the "USB-C port for AI"—an open standard introduced by Anthropic that lets different agent clients connect to the same external data sources and tools.[^mcp-overview] MCP is not unique to Cursor: the same protocol powers integrations in Claude Desktop, Claude Code CLI, OpenAI Codex, and any other client that implements the spec. Cursor 2.0 added first-class MCP support so you can bring those connectors into the IDE without rewriting them.

**For researchers**, MCP is transformative because one MCP server can serve multiple tools. Configure a server once (for example, PubMed search or Zotero syncing) and it becomes available whether you trigger it from Claude Code, Claude Desktop, or Cursor’s agents. Inside Cursor, you register MCP servers through `Settings > Context > MCP`, and the agent can then call them during a task.

**How it works**: MCP servers are lightweight processes that expose **Tools** (functions such as `search_papers`), **Resources** (data like PDFs), and **Prompts** (templated instructions) via JSON-RPC.[^mcp-protocol] Clients—including Cursor—invoke those endpoints over standard sockets. When you ask a Cursor agent to "find recent papers on transformer models" and include the PubMed MCP server in the configuration, Cursor relays the call to that server, receives the results, and incorporates them into the agent’s plan.

### AGENTS.md: Your project's research instructions

**AGENTS.md** is an open standard for guiding AI agents—think "README for AI." This simple markdown file at your project root provides context and instructions that help Cursor work effectively on your research.

**Why it matters**: Instead of explaining your research setup, data sources, and standards in every conversation, AGENTS.md stores these instructions permanently. Cursor reads the file automatically, understanding your project structure, citation requirements, data locations, and quality standards.

> **Claude Code tip:** Anthropic’s Claude Code doesn’t read `AGENTS.md` automatically. Create `CLAUDE.md` in the project and reference `@AGENTS.md` inside it to keep a single source of truth that both Cursor and Claude share.[^claude-agents]

### Skills system: Modular research expertise

**Claude Skills** are specialized knowledge packages that extend Cursor's capabilities. Each skill is a folder containing instructions, scripts, and resources focused on a specific research capability—like "statistical analysis" or "literature review."

**Progressive disclosure architecture** makes skills efficient. Cursor always loads skill names and descriptions (30-50 tokens each). When you make a research request, Cursor's AI autonomously identifies relevant skills, loads their detailed instructions, and accesses supporting files only as needed.

### K-Dense-AI Claude Skills: Ready-made research capabilities

The **K-Dense-AI/claude-scientific-skills** project ships 70+ ready-to-use Claude Skills for disciplines such as bioinformatics, cheminformatics, machine learning, materials science, and data analysis. These skills target Anthropic’s Claude ecosystem—Claude Desktop, Claude Code CLI, and the Claude Code VS Code extension—not Cursor’s native agents.[^claude-skills] To use them alongside Cursor you must launch the Claude Code extension (which runs inside Cursor because Cursor is VS Code-based) or operate Claude Desktop in parallel. Cursor’s own Composer agents do not currently load Skill bundles directly.

## Step-by-step setup guide

### Installing Cursor (15 minutes)

**System requirements**: Windows 10/11, macOS 10.15+, or Ubuntu 20.04+; 8GB RAM recommended; 2GB disk space; stable internet.

**For Windows**:
1. Visit cursor.com and download Windows installer
2. Run `CursorUserSetup-x64-0.48.1.exe`
3. Follow installation wizard, accept license
4. Launch from Start menu
5. Configure keyboard shortcuts (VS Code defaults recommended)

**For macOS**:
1. Download `Cursor.dmg` from cursor.com
2. Drag Cursor to Applications folder
3. If security warning: System Preferences > Security & Privacy > "Open Anyway"
4. Grant necessary permissions

**For Linux (Ubuntu/Debian)**:
```bash
# Download and make executable
wget -O cursor.AppImage "https://downloader.cursor.sh/linux/appImage/x64"
chmod +x cursor.AppImage

# Run directly or extract and install
./cursor.AppImage --no-sandbox
```

### Configuring AI models (10 minutes)

**Adding API keys**:
1. Get keys from platform.openai.com or console.anthropic.com
2. In Cursor: Settings (Cmd/Ctrl + ,) > Models
3. Enter OpenAI API Key and/or Anthropic API Key

**Model selection for research**:
- **Quick tasks**: Claude Haiku 4.5, GPT-4o mini (fast, economical)[^anthropic-models]
- **Standard research**: Claude Sonnet 4.5, GPT-4o (balanced)[^anthropic-models]
- **Complex reasoning**: Claude Opus 4.1, o1 (maximum capability)[^anthropic-models]

**Enable Privacy Mode** in Settings > Privacy to prevent data from training models.

[^anthropic-models]: Anthropic. (2025). *Models overview*. https://docs.anthropic.com/claude/docs/models-overview

[^claude-skills]: Anthropic. (2025). *Introducing Claude Skills*. https://www.anthropic.com/news/skills

[^claudecode]: Anthropic. (2025). *Claude Code overview*. https://docs.anthropic.com/claude/docs/claude-code-overview

[^mcp-skills]: K-Dense AI. (2025). *Claude scientific skills*. https://github.com/K-Dense-AI/claude-scientific-skills

[^mcp-overview]: Model Context Protocol. (2024). *Getting started*. https://modelcontextprotocol.io/docs/getting-started/intro

[^mcp-protocol]: Anthropic Support. (2025). *Custom connectors with remote MCP*. https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp

[^cursor-multi]: Cursor. (2025). *2.0 changelog – New coding model and agent interface*. https://cursor.com/changelog/2-0

[^cursor-toolbelt]: Cursor. (2025). *Introducing Cursor 2.0 and Composer*. https://cursor.com/blog/2-0

[^cursor-voice]: Cursor. (2025). *2.0 changelog – Voice mode*. https://cursor.com/changelog/2-0
[^cursor-team]: Cursor. (2025). *Team Commands*. https://cursor.com/docs/team/commands

[^claude-agents]: Anthropic. (2025). *Claude Code on the web – best practices*. https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web#best-practices

[^cursor-review]: Cursor. (2025). *2.0 changelog – Improved review workflow*. https://cursor.com/changelog/2-0

### Installing MCP servers for research (20 minutes)

**Quick setup (recommended)**:

1. Install Claude Desktop or the Claude Code CLI (Anthropic account required).  
2. If you want the experience inside Cursor, install the Claude Code VS Code extension and sign in.[^claudecode]  
3. Clone the K-Dense skills repo inside the location Claude Code watches (for example `~/Library/Application Support/Claude/skills/`).  
4. Enable the desired skills from the Claude Code palette (e.g., “Claude: Manage Skills”) or via `claude-code skills enable`.

**Optional MCP bridge (advanced)**: K-Dense additionally maintains an MCP server that wraps the same capabilities. You can register that server in `~/.cursor/mcp.json` so Cursor’s agents can call it through MCP, but the server still depends on a Claude runtime to execute skill actions.[^mcp-skills]

**Essential servers**:
- **ArXiv**: Preprints in physics, CS, math, biology
- **PubMed**: 35M+ biomedical citations
- **Semantic Scholar**: AI-powered search, citation analysis
- **K-Dense Skills**: 78 scientific capabilities

## Research workflow examples

### Literature review: Complete workflow

**Step 1: Define scope** (5 min) - Create AGENTS.md with research question, search strategy, inclusion/exclusion criteria, output requirements.

**Step 2: Search databases** (10 min active, 30 min execution):
```
"Conduct systematic literature search following AGENTS.md

Search PubMed, arXiv, and Semantic Scholar for '[your keywords]'
Apply filters from AGENTS.md
Download 40-60 papers after filtering
Create data/papers/ with PDFs
Generate papers_metadata.csv and search_report.md

Use ArXiv, PubMed, and Semantic Scholar MCP servers"
```

**Step 3: Extract data** (15 min active, 60 min execution):
```
"Systematic data extraction from @data/papers/

Extract for each paper:
- Citation (APA), research question, methodology, 
  sample size, key findings, limitations, relevance score

Create data/extraction_table.csv and 
data/paper_summaries/ with one .md per paper"
```

**Step 4: Synthesize** (20 min active, 90 min execution):
```
"Synthesize literature review from @data/extraction_table.csv

Identify major themes (minimum 3)
For each theme: which papers, consensus, contradictions, evidence quality
Identify research gaps

Create synthesis.md with:
- Introduction, Methods, Thematic Synthesis, 
  Research Gaps, Methodological Analysis, Conclusion
- Minimum 3000 words, ≥2 citations per claim
- Summary table of papers by theme"
```

**Step 5: Visualize** (10 min):
```
"Create publication-quality visualizations:
1. PRISMA flow diagram
2. Timeline plot (publications by year and methodology)
3. Methodology distribution pie chart

All 300 DPI, color-blind palette, proper captions"
```

**Time**: ~90 min active, 3-4 hours total vs. 2-3 weeks manually.

### Hypothesis generation workflow

**Step 1: Background** (15 min):
```
"Background research for hypothesis generation on [topic]

1. Ask the agent to use the built-in browser to gather recent reviews (2022-2024)
2. Read @data/observations/ for patterns
3. Search PubMed/Semantic Scholar for mechanisms and contradictions
4. Identify theoretical frameworks

Output to hypothesis_background.md"
```

**Step 2: Generate candidates** (20 min):
```
"Generate hypothesis candidates from @hypothesis_background.md

Apply frameworks: inductive, deductive, abductive
For each gap/contradiction: propose mechanisms, predictions, alternatives

Generate minimum 15 hypotheses specifying:
- Statement (If X, then Y, because Z)
- Type, variables, theoretical basis, novelty

Organize by: mechanistic, predictive, comparative"
```

**Step 3: Evaluate** (25 min):
```
"Evaluate @hypothesis_candidates.md on:
- Testability (methods, resources, ethics)
- Novelty (literature search)
- Theoretical strength
- Potential impact

Create hypothesis_evaluation_matrix.csv
Then hypothesis_top5.md with detailed justification and experimental approaches"
```

**Step 4: Design experiments** (20 min):
```
"Design experiments for @hypothesis_top5.md

For each: experimental design, methodology, analysis plan,
expected outcomes, feasibility assessment

Output to experimental_designs.md"
```

### Data analysis workflow

**Step 1: Quality check** (20 min):
```
"Data preparation for @data/raw/experiment_results.csv

1. Load, inspect data structure
2. Quality: missing data, duplicates, range checks
3. Outlier detection (IQR method)
4. Handle issues with justification

Save: data/processed/cleaned_data.csv,
data_dictionary.md, quality_report.md"
```

**Step 2: Exploratory analysis** (30 min):
```
"EDA for @data/processed/cleaned_data.csv

1. Descriptive statistics (all variables)
2. Distribution analysis with normality tests
3. Correlation matrix and heatmap
4. Group comparisons (boxplots, Levene's test)
5. Note patterns and insights

Generate results/eda_report.md and figures/eda/ 
All 300 DPI, color-blind palette"
```

**Step 3: Hypothesis testing** (40 min):
```
"Statistical analysis per @experiment_plan.md

1. Select appropriate test based on @results/eda_report.md
2. Conduct analysis with assumption checks
3. Report APA format: test(df) = value, p = .xxx, effect size, 95% CI
4. Post-hoc if needed with corrections
5. Create results visualization with error bars
6. Sensitivity analyses

Save: results/primary_analysis.md,
statistical_tables.md, figures/main_results.png"
```

**Step 4: Interpret** (30 min):
```
"Interpret @results/primary_analysis.md in context

1. Primary findings vs. hypothesis
2. Compare to literature
3. Alternative explanations
4. Mechanism analysis
5. Practical implications
6. Limitations (honest and specific)
7. Future directions

Generate results/interpretation.md"
```

### Report writing workflow

**Step 1: Organize content** (10 min):
```
"Organize materials for manuscript

Gather: literature review, methods protocols, 
analysis results, interpretation notes

Create content/ folder with:
- introduction_refs.md
- methods_notes.md  
- results_data.md
- discussion_points.md"
```

**Step 2: Write sections** (30 min active per section):
```
"Write Introduction section for manuscript

Sources: @content/introduction_refs.md, @AGENTS.md objectives

Structure: ~800 words
- Opening: establish importance of topic (2-3 sentences)
- Literature review: synthesize current knowledge (400 words)
- Gap identification: what's missing/contradictory (200 words)
- Study purpose: specific research questions (100 words)
- Hypotheses: clear predictions

Requirements:
- APA 7th edition citations, ≥2 per claim
- Academic tone, past tense for literature
- Create smooth transitions between paragraphs
- End with clear statement of contribution

Save to manuscript/1_introduction.md"
```

Repeat for Methods, Results, Discussion sections with appropriate specifications.

**Step 3: Integrate and polish** (20 min):
```
"Compile complete manuscript

Combine: @manuscript/1_introduction.md, 
@manuscript/2_methods.md, @manuscript/3_results.md,
@manuscript/4_discussion.md

Add:
- Title page (title, authors, affiliations)
- Abstract (150-250 words structured)
- Keywords (5-7 terms)
- References section (all cited sources, APA 7th)
- Figure/table captions

Proofread for:
- Consistent terminology
- Proper headings hierarchy
- Citation format uniformity
- Grammar and clarity

Save to manuscript/complete_draft.md"
```

## Best practices and tips

### Maximize efficiency with parallel agents

**Pattern**: Break large tasks into independent subtasks, run simultaneously.

**Example**:
```
"Launch 3 parallel research streams:

Agent 1: Search PubMed for papers on immune response
Agent 2: Search arXiv for computational models  
Agent 3: Search Semantic Scholar for review articles

Each creates separate output folder.
I'll synthesize when complete."
```

Use Plan Mode for tasks exceeding 2 hours—it breaks work into phases you can execute across sessions.

### Leverage @Codebase for project memory

When working across multiple sessions, use `@Codebase what did we conclude about X?` to search all project files. Cursor's semantic search finds relevant information even if exact keywords differ.

### Create reusable skills for repeated workflows

If you perform certain analyses regularly:
1. Create personal skill in `~/.claude/skills/`
2. Document exact procedures, standards, output formats
3. Every future project automatically inherits this expertise

### Use Notepads for persistent context

For ongoing projects, create a Notepad (View > Notepads) with:
- Research objectives
- Key findings so far  
- Decisions made and rationale
- Questions to investigate

Reference this notepad in prompts to maintain continuity across sessions.

### Prompt engineering for research

**Effective structure**:
1. **Context**: "I'm researching [topic]. We have [data/papers/findings]."
2. **Task**: "Conduct [specific analysis/review/synthesis]."
3. **Specifications**: "Requirements: [format, standards, constraints]."
4. **Output**: "Save to [location] with [structure]."

**Poor**: "Analyze this data"
**Better**: "Analyze @data/results.csv using t-test comparing groups A and B. Report with APA format statistics including effect size. Save to results/analysis.md"

### Verify critical information

For factual claims, especially in literature reviews:
- Cross-reference with multiple sources
- Check original papers, not just AI summaries
- Ask the agent to open sources with the browser tool and quote supporting evidence for each claim
- When in doubt, read the source yourself

### Review multi-file diffs before committing

Cursor 2.0 adds an **Agent Review** pane that aggregates every file the agent touched so you can audit changes without hopping around the tree.[^cursor-review] After an agent run, open the review to:

- Inspect a unified diff spanning all modified Markdown, data tables, and scripts
- Leave inline comments or mark items to revisit before merging
- Trigger follow-up commands (rerun tests, revert hunks) directly from the panel

Treat this as your pre-publication checklist: ensure citations survived, headings follow journal style, and any generated code still passes unit tests.

### Document AI assistance appropriately

For publications, include in Methods:
> "Data analysis was assisted by AI tools (Cursor IDE with Claude Sonnet 4.5) with manual verification of all statistical computations and interpretations. All citations reference original sources, not AI-generated summaries."

### Organize projects with clear structure

**Recommended hierarchy**:
```
research-project/
├── AGENTS.md                    # Project instructions
├── .cursor/
│   └── mcp.json                # Project-specific MCP servers
├── data/
│   ├── raw/                    # Original data (read-only)
│   ├── processed/              # Cleaned data
│   └── external/               # Third-party data
├── literature/
│   ├── papers/                 # PDFs
│   ├── notes/                  # Reading notes
│   └── synthesis.md            # Literature review
├── analysis/
│   ├── scripts/                # Analysis code
│   ├── results/                # Output files
│   └── figures/                # Visualizations
├── manuscript/
│   ├── drafts/                 # Writing iterations
│   ├── figures/                # Publication figures
│   └── supplements/            # Supplementary materials
└── README.md                   # Project overview
```

### Quality control checklist

Before finalizing any research output:

**For literature reviews**:
- [ ] All claims have ≥2 credible sources
- [ ] Citations properly formatted
- [ ] Contradictions acknowledged, not hidden
- [ ] Research gaps clearly identified
- [ ] Summary table includes all reviewed papers

**For data analysis**:
- [ ] Assumptions tested and reported
- [ ] Effect sizes included, not just p-values
- [ ] Outlier decisions justified
- [ ] Figures have clear labels and captions
- [ ] Results reproducible from raw data

**For manuscripts**:
- [ ] IMRAD structure followed
- [ ] All figures/tables referenced in text
- [ ] Methods detailed enough for replication
- [ ] Limitations honestly discussed
- [ ] All citations in reference list

## Troubleshooting common issues

### "MCP server not starting"

**Symptoms**: Tools don't appear in Cursor, MCP section shows errors.

**Solutions**:
1. **Check JSON syntax**: Use jsonlint.com to validate `mcp.json`
2. **Verify command paths**: Test commands in terminal first
   ```bash
   # Test if uv works
   uv --version
   ```
3. **Install missing dependencies**:
   ```bash
   # Install uv if missing
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
4. **Restart Cursor completely**: Quit (not just close window), relaunch
5. **Check logs**: Settings > MCP > View Server Logs

### "Cursor gives inaccurate citations"

**Problem**: AI hallucinates paper citations or gets details wrong.

**Prevention**:
- Always use MCP servers (ArXiv, PubMed, Semantic Scholar) for paper searches
- Verify citations against original sources
- Use Zotero MCP integration for reference management

**Fix**:
```
"Verify all citations in @manuscript/draft.md

For each citation:
1. Search actual paper via Semantic Scholar MCP
2. Confirm: authors, year, title, publication match
3. Flag any discrepancies
4. Provide corrected citation in APA format

Generate citation_verification_report.md"
```

### "Agent produces unexpected results"

**Symptoms**: Output doesn't match instructions, analysis is wrong.

**Diagnosis**:
1. **Check if AGENTS.md was read**: Ask "What are the project standards?" to verify
2. **Prompt too vague**: Add more specifications
3. **Context missing**: Use @ symbols to reference necessary files
4. **Wrong skill activated**: Explicitly name skill to use

**Improved prompting**:
```
Before: "Analyze the data"

After: "Analyze @data/experiment.csv using statistical-analysis skill

Follow standards in AGENTS.md:
- Significance: α = 0.05
- Report format: APA with effect sizes
- Visual output: 300 DPI, color-blind palette

Conduct independent samples t-test comparing 
groups on outcome variable.

Save results to results/analysis.md and 
figure to figures/main_plot.png"
```

### "Slow performance or timeouts"

**Causes**: Too many MCP servers, large context, complex operations.

**Solutions**:
1. **Limit active servers**: Disable unused servers in `mcp.json`
2. **Reduce context**: Reference specific files, not entire folders when possible
3. **Break large tasks**: Split into smaller sequential prompts
4. **Use faster models**: Claude Haiku 4.5 or GPT-4o mini for simple tasks
5. **Close unnecessary files**: Fewer open tabs = better performance

### "Skills not activating"

**Problem**: Cursor doesn't use installed skills.

**Check**:
1. Skills installed? Ask: "What skills are available?"
2. Restart Cursor after installing new skills
3. Skill description clear? Cursor selects based on descriptions
4. Explicitly name skill: "Use the statistical-analysis skill to..."

### "Results not reproducible"

**Issue**: Re-running analysis gives different results.

**Fixes**:
1. **Set random seeds**: Document in AGENTS.md, specify in prompts
2. **Version control data**: Keep raw data immutable
3. **Document environment**: Note software versions, packages
4. **Save complete workflows**: Export analysis steps to scripts

### "Rate limiting from APIs"

**Symptoms**: "Rate limit exceeded" errors from PubMed, Semantic Scholar.

**Solutions**:
1. **Get API keys**: Register for higher rate limits (free)
   - PubMed: ncbi.nlm.nih.gov/account
   - Semantic Scholar: email api@semanticscholar.org
2. **Add to mcp.json**: Include keys in `env` section
3. **Implement delays**: Add "wait 2 seconds between queries" to prompts
4. **Use caching**: MCP servers cache results—leverage this

## Resources and further learning

### Official documentation

**Cursor**:
- Website: cursor.com
- Documentation: docs.cursor.com
- Blog: cursor.com/blog
- Latest version: 0.48.1+ (as of November 2025)

**Model Context Protocol**:
- Specification: modelcontextprotocol.io
- Cursor integration: docs.cursor.com/context/model-context-protocol
- Anthropic announcement: anthropic.com/news/model-context-protocol

**AGENTS.md standard**:
- Official site: agents.md
- GitHub: github.com/openai/agents.md
- 20,000+ example repos

**Claude Skills**:
- Documentation: docs.claude.com/en/docs/agents-and-tools/agent-skills
- Anthropic blog: anthropic.com/news/skills
- Cookbook: github.com/anthropics/claude-cookbooks/tree/main/skills

**K-Dense-AI Claude Skills (requires Claude Desktop or Claude Code)**:
- GitHub: github.com/K-Dense-AI/claude-scientific-skills
- MCP bridge: github.com/K-Dense-AI/claude-skills-mcp
- K-Dense platform: k-dense.ai

### MCP server directories

**Find research-focused servers**:
- MCP Registry: mcpm.sh/registry
- Glama MCP Directory: glama.ai/mcp/servers
- Smithery: smithery.ai/servers
- Composio (100+ servers): mcp.composio.dev

**Recommended research servers**:
- ArXiv MCP: blazickjp/arxiv-mcp-server
- PubMed MCP: cyanheads/pubmed-mcp-server
- Semantic Scholar: JackKuo666/semanticscholar-MCP-Server
- Zotero MCP: 54yyyu/zotero-mcp
- Paper Search: openags/paper-search-mcp
- mcp.science collection (materials, computation, Jupyter)

### AI research tools ecosystem

**Complement Cursor with**:
- **Elicit**: AI research assistant, literature review automation (elicit.org)
- **Consensus**: Evidence-based answers from papers (consensus.app)
- **Research Rabbit**: Citation network visualization (researchrabbit.ai)
- **Semantic Scholar**: 200M+ papers with AI search (semanticscholar.org)
- **Connected Papers**: Visual literature mapping (connectedpapers.com)
- **Zotero**: Reference management with MCP integration (zotero.org)

### Learning resources

**Video tutorials**:
- Cursor official YouTube channel (cursor.com/youtube)
- K-Dense AI scientist demos (youtube.com/@KDenseAI)

**Written guides**:
- Cursor setup guides: docs.cursor.com/get-started
- MCP quickstart: modelcontextprotocol.io/quickstart
- Skills creation guide: github.com/anthropics/skills/tree/main/examples

**Community**:
- Cursor community forum: forum.cursor.com
- MCP GitHub discussions: github.com/modelcontextprotocol/discussions
- K-Dense GitHub issues: github.com/K-Dense-AI/claude-scientific-skills/issues

### Academic integrity guidelines

**Using AI in research**:
- Always disclose AI assistance in methods sections
- Verify all factual claims against original sources
- Never cite AI-generated content—cite the original papers
- Human researcher responsible for accuracy and interpretation
- Check institutional policies before publication

**Proper attribution example**:
> "Data extraction and preliminary synthesis were assisted by AI tools (Cursor IDE v0.48 with Claude Sonnet 4.5 and K-Dense-AI scientific skills) with comprehensive manual verification. All statistical analyses were validated by the research team. All citations reference original peer-reviewed sources accessed through PubMed and arXiv databases."

### Citation for this playbook

If referencing this guide in your work:

> "The Researcher's Guide to Cursor: Transform Your AI IDE into a Scientific Research Powerhouse." (2025). Retrieved from [source location].

### Getting help

**Technical issues**:
- Cursor support: [email protected]
- MCP questions: GitHub discussions at modelcontextprotocol
- K-Dense skills: GitHub issues at K-Dense-AI/claude-scientific-skills

**Research methodology questions**:
- Consult domain experts and advisors
- AI tools assist but don't replace expert judgment
- When uncertain, seek human guidance

---

## Conclusion: Your research, accelerated

Cursor transforms from a code editor into a comprehensive research workstation when configured with MCP servers and scientific skills. The combination of agentic autonomy, markdown-native workflows, and direct database access creates a uniquely powerful environment for scientific research.

**What you've learned**:
- Installing and configuring Cursor for research workflows
- Connecting to scientific databases via MCP servers
- Using AGENTS.md to standardize project instructions
- Leveraging skills for specialized research capabilities
- Creating effective prompts for research tasks
- Complete workflows for literature review, hypothesis generation, data analysis, and report writing

**Next steps**:
1. Install Cursor and complete basic setup (30 minutes)
2. Install Claude Code (or Claude Desktop) and enable the K-Dense scientific skills library (10 minutes)
3. Create your first research project with AGENTS.md (15 minutes)
4. Try one complete workflow from this playbook (2-3 hours)
5. Customize skills for your specific research needs (ongoing)

**The paradigm shift**: Instead of manually searching databases, reading papers, extracting data, running analyses, and writing reports—you orchestrate AI agents to handle these tasks while you focus on strategy, interpretation, and scientific insight. Research that took weeks now takes hours. But you remain the scientist, the critical thinker, the interpreter of meaning.

Cursor doesn't replace the researcher. It amplifies research capacity, eliminates tedious work, and accelerates the path from question to insight. Your expertise directs the process; AI handles execution.

Welcome to the future of scientific research. Start building.
