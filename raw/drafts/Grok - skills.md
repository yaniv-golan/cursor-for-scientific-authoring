## Expanded Section: Claude Skills for Scientific Research

This expansion builds on the "Claude Skills for Science" in the playbook, providing more depth on integration, a fuller list of skills from key repositories, and additional resources. Claude Skills are modular packages (folders with prompts, code, and configs) that extend Claude's capabilities via MCP (Model Context Protocol). They allow the AI to access databases, run analyses, and follow scientific workflows without user coding. Inside Cursor you can load these skills either by configuring Claude models via MCP[^mcp-skills] or by installing Anthropic’s Claude Code extension,[^claudecode] then instructing: "Use the PubMed skill to search for studies on neural networks in biology; summarize in report.md with APA citations."

### Integration into Cursor
- **Setup Steps**:
  1. Install Claude Desktop or the Claude Code VS Code extension (the latter can run inside Cursor) and sign in with your Anthropic account.[^claudecode]
  2. Add the K-Dense skill pack to Claude’s skills directory (e.g., run `git clone https://github.com/K-Dense-AI/claude-scientific-skills` in Claude’s skills folder).
  3. Enable desired skills from the Claude palette (`Claude: Manage Skills`) or via `claude-code skills enable` in the CLI.
  4. Optional: register the `claude-skills-mcp` server so Cursor’s Composer agents can call into the same capabilities through MCP.
  5. When working inside Cursor, open the Claude Code side panel and issue prompts like: "Use the Literature Review skill to query bioRxiv on Y; summarize in findings.md."
- **Dependencies**: Requires access to Anthropic’s Claude platform. Some skills call external APIs (PubMed, arXiv) that may need environment variables or API keys configured in the Claude Code settings.
- **Best Practices**: Bring skills online one at a time and chain them deliberately (e.g., PubMed search → RDKit analysis). Keep prompts high level—the skill instructions handle the detailed execution.

### Skills from K-Dense-AI/claude-scientific-skills
This repo (updated as of Nov 2025) organizes ~100+ skills into bundles: Scientific Databases (26), Scientific Packages (59), Scientific Thinking (8), Scientific Integrations (6), and Scientific Context Initialization (1). Purpose: Turn Claude into an "AI Scientist" for domains like bioinformatics, chemistry, and physics.

#### Scientific Databases (Key Examples)
These connect to real-time APIs for data retrieval. Inputs: Queries (e.g., gene names); Outputs: Tables, JSON, or files.
- **PubMed**: Searches biomedical literature. Features: Abstract extraction, citation export. Example: "Query PubMed for immunotherapy reviews; list top 5 with abstracts."
- **bioRxiv**: Preprint searches. Features: Full-text, DOI parsing. Example: "Find CRISPR preprints from 2024."
- **ChEMBL**: Bioactivity data for molecules. Features: Activity filters (e.g., IC50). Example: "Find EGFR inhibitors with IC50 <50nM."
- **GEO**: Gene expression datasets. Features: Matrix loading, plotting. Example: "Load GSE123456 and summarize differential genes."
- **UniProt**: Protein annotations. Features: Functional sites. Example: "Retrieve EGFR (P00533) entry."
- Full list includes: AlphaFold DB, ClinVar, DrugBank, Ensembl, GWAS Catalog, KEGG, PDB, PubChem, Reactome, STRING, and more (26 total).

#### Scientific Packages (Key Examples)
Wrappers for Python libraries. Inputs: Data/files; Outputs: Results (e.g., plots, models).
- **RDKit**: Cheminformatics toolkit. Features: Molecule manipulation, descriptors. Example: "Compute SMILES for aspirin and predict solubility."
- **Scanpy**: Single-cell RNA-seq analysis. Features: Clustering, visualization. Example: "Cluster my AnnData file and plot UMAP."
- **DeepChem**: ML for drug discovery. Features: Property prediction. Example: "Predict toxicity for a SMILES list."
- **PyDESeq2**: Differential expression. Features: Normalization, stats. Example: "Analyze RNA-seq counts for condition A vs B."
- Other notables: BioPython (sequence analysis), scvi-tools (deep models for omics), Datamol (molecule wrangling), and 50+ more across bioinformatics, cheminformatics, etc.

#### Scientific Thinking (8 Skills)
Prompt-based for reasoning/workflows.
- **Literature Review**: Systematic searches/summaries. Example: "Review quantum computing in biology; cite 2+ sources."
- **Hypothesis Generation**: Brainstorms ideas from data. Example: "Generate hypotheses from GEO dataset."
- **Exploratory Data Analysis**: Summarizes datasets. Example: "EDA on my CSV; plot distributions."
- Others: Scientific Writing (IMRAD formatting), Peer Review Simulation, Statistical Analysis, Experiment Design, Reproducibility Checker.

#### Scientific Integrations (6 Skills)
Connects to lab tools.
- **Benchling**: Experiment management. Example: "Import sequence from Benchling."
- **Schrodinger**: Molecular modeling. Example: "Run docking simulation."
- Others: Jupyter (notebook export), Git (version control), Zotero (reference management), Overleaf (LaTeX reports).

#### Scientific Context Initialization (1 Skill)
Auto-creates/updates AGENTS.md with project rules, ensuring consistent use of skills.

### Other Claude Skills Projects for Science
Search revealed curated lists and specialized repos:
- **awesome-claude-skills** (ComposioHQ, VoltAgent, travisvn forks): Curated collections with science-focused skills like "Research Summarizer" (scrapes articles) and "Data Visualizer" (plots from CSVs). Install via GitHub; great for quick additions.
- **anthropics/skills**: Official Anthropic repo with foundational skills; includes "Scientific Query" for general research.
- **alirezarezvani/claude-skills**: Modular packs for domains like physics (e.g., simulation skills) and environmental science.
- **brunoasm/my_claude_skills**: Custom skills for task optimization, including "Prevent Hallucination" for fact-checked research.
- Community Tips (from Reddit): Users recommend "YouTube/Article Scraper" for lit reviews; test in Cursor for compatibility.

Expand your research workflows by running these Claude Skills through Claude Code (inside or alongside Cursor) and combining them with MCP servers for Composer when needed. Always verify outputs against original sources for accuracy.

[^claudecode]: Anthropic. (2025). *Claude Code overview* – terminal and VS Code workflows. https://docs.anthropic.com/claude/docs/claude-code-overview
[^mcp-skills]: Model Context Protocol. (2024). *Intro to MCP servers*. https://modelcontextprotocol.io/docs/getting-started/intro
