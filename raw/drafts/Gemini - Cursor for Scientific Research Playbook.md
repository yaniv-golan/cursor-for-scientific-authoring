

# **The Agentic Researcher: A Playbook for Scientific Inquiry in Cursor**

## **Part I: The AI-Powered Research Environment: Foundations**

This section establishes the foundational philosophy of this playbook: transitioning the perception of Cursor from a tool for writing code to a comprehensive, integrated environment for managing and executing scientific research. The central organizing principle introduced is a markdown-first workflow, where human-readable documents serve as the primary interface for directing a powerful, agentic AI collaborator.

### **Chapter 1: Introduction: Cursor as a Research Hub, Not Just a Code Editor**

While Cursor is marketed as the "best way to code with AI," its true potential for the scientific community lies beyond software development.1 For researchers, graduate students, and academics, Cursor can be transformed into an integrated research environment—a digital laboratory where ideas are formulated, literature is synthesized, experiments are planned, and manuscripts are drafted. This reframing moves the focus from coding productivity to the acceleration of the entire research lifecycle. Testimonials from students at institutions like the University of Pennsylvania and Harvard University underscore this shift; they use Cursor not just for programming, but to "clean datasets, debug pipelines, and write complex queries," which saves hours each week and allows them to "focus on my research".2

#### **The Agentic Shift**

The paradigm shift offered by modern AI tools is the move from simple assistance to agentic collaboration. Traditional AI tools function as sophisticated autocompletes or targeted editors. An agent, by contrast, is a system that can understand a high-level goal, create a multi-step plan to achieve it, execute that plan, and even correct itself along the way.3 This capability is what allows an AI in Cursor to "independently research libraries, best practices, and implementation strategies," acting less like a tool and more like a research assistant who is "always on call".2

This introduces what has been described as an "autonomy slider".1 At one end of the slider, the AI offers simple, inline suggestions. At the other, the user can "let it rip with the full autonomy agentic version".1 The objective of this playbook is to provide the mental models and practical workflows necessary to confidently operate at the high-autonomy end of this slider, transforming the AI into a partner capable of tackling complex research tasks.

Cursor 2.0 makes that slider tangible: you can spin up to eight agents in parallel, give them dedicated git worktrees, let them browse the web natively, run sandboxed terminals, or even talk to them via voice mode—all inside a unified agent sidebar.[38][39] A revamped Agent Review view collects every file they touch so you can audit multi-file diffs without leaving the workflow. Treat these upgrades as core research infrastructure, not optional extras.

#### **Markdown as the Command Center**

For the semi-technical researcher, the primary interface for controlling this powerful agent is not complex code, but rather simple, well-structured markdown files. This markdown-first approach is the cornerstone of the agentic research workflow. It is a methodology for translating abstract research goals into concrete, actionable plans that the AI can understand and execute. By structuring a project around a series of interconnected markdown documents, the researcher creates a persistent, context-rich environment. This is akin to the software development best practice of creating a Product Requirements Document (PRD), which serves as a "North Star" to guide development and ensure alignment between the human and the AI on the end goal.5 In this paradigm, markdown is not merely for documentation; it is the command and control center for the entire research project.

### **Chapter 2: The Markdown-First Workflow: Your Digital Lab Notebook**

Adopting a markdown-first workflow means establishing a clear, organized structure for a research project from its inception. This structure serves as a digital lab notebook, providing a coherent and navigable framework that both the researcher and the AI agent can understand. This proactive organization is critical; an AI agent's effectiveness is directly tied to the clarity and structure of the information it is given.7

#### **Structuring Your Research Project**

A well-organized project directory provides the scaffolding for agentic work. Before writing the first prompt, the researcher should establish a folder structure containing a set of core markdown files. This initial setup mirrors the best practice in complex software projects of drafting a comprehensive plan before writing any code, as it ensures all subsequent actions are aligned with a clear, documented objective.5

A recommended directory structure for a typical scientific research project might look as follows:

* project\_root/  
  * AGENTS.md (The AI's core instruction manual, detailed in Part II)  
  * README.md (A human-readable project overview)  
  * data/ (For raw and processed datasets)  
  * docs/  
    * PROJECT\_PLAN.md (The strategic blueprint for the research)  
    * LITERATURE\_REVIEW.md (For synthesizing existing knowledge)  
    * EXPERIMENTS.md (A log of experimental designs and results)  
    * DATA\_ANALYSIS\_PLAN.md (The statistical methodology)  
  * outputs/  
    * figures/ (For generated plots and visualizations)  
    * MANUSCRIPT\_DRAFT.md (The final written output)

Each markdown file serves a distinct purpose:

* **PROJECT\_PLAN.md**: This is the most critical document, acting as the project's "North Star".5 It should contain the research question, core hypotheses, a high-level overview of the methodology, and the defined success criteria or expected outcomes.  
* **LITERATURE\_REVIEW.md**: This file becomes the repository for all synthesized information from existing research. The agent will be instructed to populate and reference this file when summarizing papers, identifying knowledge gaps, and contextualizing new findings.  
* **EXPERIMENTS.md**: For empirical research, this file serves as a detailed log. It can be used to outline experimental protocols, list parameters, and record observations, creating a reproducible record of the work performed.  
* **DATA\_ANALYSIS\_PLAN.md**: This document specifies the statistical methods and visualization strategies that will be used. Instructing the agent to follow this plan ensures consistency and methodological rigor.  
* **MANUSCRIPT\_DRAFT.md**: This is the destination for the final synthesized output, where the agent will assemble the structured information from other documents into a coherent narrative.

#### **The Power of @ and \#: Creating a Dynamic Knowledge Base**

Cursor's true power for non-coders is unlocked through its context-aware commands, primarily the @ and \# symbols. These commands are the mechanisms that transform a collection of static markdown files into a dynamic, interconnected knowledge base that the AI agent can traverse, query, and synthesize.

* **@ for Files and Context**: The @ symbol allows the user to reference specific files or even the entire project workspace within a prompt.1 For example, a prompt can instruct the agent to "Summarize the key themes in @docs/LITERATURE\_REVIEW.md" or "Based on the methodology in @docs/PROJECT\_PLAN.md, suggest a title for the study." This provides the AI with precise, targeted context without requiring the user to manually copy and paste large blocks of text.9  
* **\# for Symbols (Less relevant for non-coding)**: The \# symbol is typically used to reference specific functions or classes within code files. While less central to a purely markdown-based workflow, it can be useful for researchers working with data analysis scripts to quickly reference specific parts of their code.

The ability to reference files with @ is the fundamental building block of the agentic research workflow. A researcher's knowledge is often distributed across numerous notes, drafts, and data files. Without an effective linking mechanism, the AI's understanding is confined to the file currently open in the editor or the limited text that can be pasted into a chat window. This approach is inefficient and leads to a constant loss of context, forcing the researcher to repeat instructions and background information in every prompt.6

The @ command solves this problem. It enables the researcher to orchestrate complex, cross-document tasks with simple, natural language. A single prompt can now become a sophisticated instruction for knowledge synthesis:

"Read the approved methodology in @docs/PROJECT\_PLAN.md and the statistical approach in @docs/DATA\_ANALYSIS\_PLAN.md. Then, review the collected summaries in @docs/LITERATURE\_REVIEW.md and propose three novel hypotheses that extend the current research. Write these hypotheses in a new section within @docs/EXPERIMENTS.md."

This command sequence elevates the AI from a mere text generator to a genuine knowledge synthesizer. It operates across the project's entire documented "brain," understanding the relationships between the plan, the literature, and the proposed experiments. This is the first practical step toward harnessing the full potential of agentic AI for scientific inquiry.

## **Part II: Directing the Agent: From Simple Prompts to Persistent Protocols**

Moving beyond basic interactions requires establishing a system of persistent instructions that guide the AI agent's behavior consistently across all tasks. This section details how to create a "lab manual" for the AI using the AGENTS.md file. This approach ensures that the agent's outputs adhere to the rigorous standards of scientific research, maintaining a consistent persona, style, and methodological approach throughout the project's lifecycle.

### **Chapter 3: AGENTS.md: Crafting the "Lab Manual" for Your AI**

The AGENTS.md file is an emerging open standard designed to provide clear, machine-readable instructions to AI agents.10 It functions as a "README for machines," offering a single, predictable location for project-specific guidelines that might otherwise be scattered across disparate documents or forgotten in long chat histories.12

#### **The Role of AGENTS.md in Cursor**

Cursor provides direct support for an AGENTS.md file placed in the root directory of a project.9 It serves as a user-friendly and powerful alternative to the more complex .cursor/rules system, which uses a specialized .mdc file format.14 For the semi-technical researcher, the simplicity of a standard markdown file makes AGENTS.md the ideal method for configuring the AI's behavior. When pairing Cursor with Anthropic's Claude Code extension, remember that Claude does not ingest `AGENTS.md` automatically—create `CLAUDE.md` and reference `@AGENTS.md` so both assistants share the same rules.[43]

The core purpose of this file is to provide persistent, reusable context to the large language model.14 LLMs are inherently stateless; they do not retain memory between interactions unless context is explicitly provided again. This can lead to "context drift," a phenomenon where the AI gradually forgets initial instructions over the course of a long and complex task.15 The AGENTS.md file mitigates this by ensuring that a core set of instructions is included at the start of the model's context for every major task. This gives the AI consistent guidance, ensuring it adheres to the project's specific methodological standards, writing style, and analytical principles.12

#### **Syntax and Structure**

The beauty of AGENTS.md lies in its simplicity. It is a plain markdown file without any complex schema or required tooling.12 The structure is intuitive and relies on standard markdown conventions that are easily readable by both humans and machines:

* **Top-Level Headings (\#, \#\#)**: These are used to define distinct categories of instructions. For a research project, these headings act as semantic cues that organize the agent's "knowledge" into logical domains, such as \#\# Persona and Communication Style or \#\# Data Interpretation Guidelines.13  
* **Bullet Points (-)**: Under each heading, specific rules and directives are listed as bullet points. This format is easily parsed by the AI. Commands or specific terms can be enclosed in backticks (\`) to ensure they are interpreted literally.11

This straightforward structure allows a researcher to build a comprehensive set of operating procedures for their AI assistant with minimal technical overhead.

### **Chapter 4: A Template for Scientific Inquiry: Building a Research-Specific AGENTS.md**

To make these concepts practical, this chapter provides a detailed, annotated AGENTS.md template specifically tailored for a scientific research project. This template is designed to be a starting point that a researcher can adapt to their specific field and project requirements. It is the practical centerpiece of this playbook, transforming abstract principles into a concrete tool.

The AGENTS.md file, when properly constructed, functions as a practical implementation of a **Meta-level Control Policy** for the research agent. Academic research explores the concept of theoretical "meta-controllers" that operate at a high level to guide an LLM's behavior, deciding on macro-actions and enforcing constraints to ensure alignment with a user's goals.17 The AGENTS.md file serves precisely this function within the Cursor environment. It does not dictate the exact content of the AI's output line-by-line. Instead, it establishes the overarching rules, principles, and objectives that govern the agent's decision-making process. When a researcher issues a high-level command like "Analyze these findings," the agent's execution of that command is constrained and shaped by the policies defined in AGENTS.md. By carefully crafting this file, the researcher is not merely prompting; they are programming the agent's long-term behavior and aligning its operation with the rigorous standards of scientific inquiry.

#### **Annotated AGENTS.md Template for Scientific Research**

# **AGENTS.md: Research Protocol for Project \[Project Name\]**

## **Project Overview**

* **Research Goal:** To conduct a systematic review of the literature on the efficacy of for treating.  
* **Primary Hypothesis:** is significantly more effective than the current standard of care, with fewer side effects.  
* **Key Objectives:**  
  1. Identify all relevant peer-reviewed studies published between 2015 and 2025\.  
  2. Synthesize findings regarding efficacy, patient outcomes, and reported adverse events.  
  3. Identify gaps in the current literature and propose directions for future research.

## **Persona and Communication Style**

* You are a meticulous and critical research assistant with expertise in.  
* Your communication style must be formal, objective, and strictly evidence-based.  
* Avoid speculative language, hyperbole, and first-person pronouns ("I think," "I believe").  
* All claims, summaries, and conclusions must be directly supported by the provided source material or cited literature.  
* When asked for an opinion or suggestion, frame it as a logical possibility based on the available data (e.g., "The data suggest a possible correlation...").

## **Literature Search and Synthesis Protocol**

* **Search Strategy:** When conducting literature searches, use the following keywords: \`\`. Prioritize searches on PubMed, Google Scholar, and Scopus.  
* **Inclusion Criteria:** Include only peer-reviewed, English-language articles, randomized controlled trials (RCTs), and meta-analyses.  
* **Exclusion Criteria:** Exclude case studies, opinion pieces, editorials, and studies with a sample size smaller than N=50.  
* **Extraction Protocol:** For each included paper, extract the following information into a structured format:  
  * Full Citation (APA 7th Edition)  
  * Hypothesis/Research Question  
  * Methodology (including sample size, duration, and measures)  
  * Key Findings (with relevant statistics, e.g., p-values, effect sizes)  
  * Stated Limitations  
* **Synthesis Approach:** When synthesizing findings, group studies thematically. Explicitly note areas of scientific consensus, points of controversy, and inconsistencies in the results.

## **Data Interpretation Guidelines**

* When summarizing statistical results, always report the specific statistical test used, the degrees of freedom, the test statistic value, the p-value, and the effect size (e.g., Cohen's d, odds ratio).  
* Acknowledge the limitations of any dataset or study design you are analyzing.  
* When creating data visualizations, prioritize clarity, accuracy, and reproducibility. All axes must be clearly labeled with units.  
* Adhere to the visualization best practices outlined in the scientific-visualization skill, especially regarding colorblind-friendly palettes.

## **Manuscript and Citation Style**

* All written output intended for the manuscript must conform to the **APA 7th Edition** style guide.  
* Use in-text parenthetical citations, for example: (Author, Year).  
* Maintain a running bibliography in a separate references.md file.  
* All figures and tables must have numbered captions that clearly describe their content.  
* Figures should be generated using colorblind-friendly palettes and exported as high-resolution (300 DPI) PDF or TIFF files, following the guidelines from the scientific-visualization skill.19

By establishing this detailed "lab manual" at the outset of a project, the researcher creates a reliable and consistent AI collaborator. This file becomes a living document; as the project evolves, the researcher can instruct the agent to update its own rules, progressively refining its performance and ensuring its outputs remain aligned with the project's goals.20

## **Part III: Augmenting Your Agent with Specialist Tools and Knowledge**

An AI agent's effectiveness is determined by the quality of its underlying model and the tools it can access. This section focuses on extending the agent's native capabilities by making strategic choices about its "brain" (the LLM) and connecting it to external data sources, specialized tools, and pre-packaged domain expertise through Model Context Protocol (MCP) servers and Claude Skills.

### **Chapter 5: Choosing Your Assistant's "Brain": OpenAI vs. Claude Models**

Cursor 2.0 is model-agnostic and agent-first. Its proprietary Composer model ships as the default, trained with codebase-wide semantic search and touted as four times faster than similarly capable models, while still letting you pull in OpenAI GPT-4/5 or Anthropic Claude models when they’re a better fit.1 21 Experiment across models: Composer handles repo-wide reasoning quickly, but Claude’s long context or GPT-5 Codex’s analytic harness may outperform it on certain scientific syntheses. Anthropic currently positions Claude Haiku 4.5, Claude Sonnet 4.5, and Claude Opus 4.1 as its production Claude models, and those same models power both the Claude Code assistant and the Claude API.[\[40\]](https://docs.anthropic.com/claude/docs/models-overview)

OpenAI Codex is a parallel product, not a Cursor feature—it offers a Rust-based CLI, a web cloud IDE with managed sandboxes, extensions for VS Code/Cursor/Windsurf, Slack and GitHub integrations, and an Agents SDK so teams can script GPT-5-Codex workflows.[\[45\]](https://developers.openai.com/codex/cloud)[\[46\]](https://developers.openai.com/codex/ide)[\[47\]](https://developers.openai.com/codex/sdk) Codex jobs require a paid ChatGPT plan and can run multiple tasks in parallel in the cloud while adhering to the same `AGENTS.md` configuration style via MCP.[\[37\]](https://openai.com/codex/)[\[48\]](https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers) Treat it as a cooperating agent that you can invoke inside Cursor when you need Codex’s hosted environment or GitHub/RFC review features.

Claude Code occupies the same competitive space: a terminal-first agent with integrations for VS Code, JetBrains, GitHub Actions, and its own Skills system for repeatable workflows. It never commits files without your approval, can orchestrate multi-file edits, and supports MCP just like Cursor.[\[41\]](https://docs.anthropic.com/claude/docs/claude-code-overview)[\[49\]](https://www.anthropic.com/news/skills) Running the Claude Code extension inside Cursor simply embeds that experience alongside Composer—you’re switching between two agent platforms, not using Claude as a “model inside Cursor.”

#### **Comparative Strengths for Research Tasks**

While direct, peer-reviewed comparisons of these models for scientific research tasks are still emerging, valuable inferences can be drawn from their performance in complex coding and reasoning scenarios.

* **Anthropic's Claude Models (Opus, Sonnet):** These models are frequently lauded for their strong reasoning capabilities, large context windows, and proficiency in handling complex, multi-step instructions. In comparative tests, Claude models have demonstrated a robust ability to understand and refactor large codebases, suggesting a strong aptitude for tasks that require deep contextual understanding and logical consistency.21 This makes them particularly well-suited for structured research tasks such as drafting a detailed methodology, performing a systematic analysis based on strict criteria, or synthesizing complex information from multiple sources.  
* **OpenAI's GPT Models:** OpenAI's models are renowned for their vast general knowledge, creativity, and fluency in generating human-like text.23 These strengths are highly valuable in the exploratory phases of research. GPT models can excel at brainstorming novel hypotheses, drafting compelling introductions for manuscripts, and summarizing dense academic prose in more accessible language.  
* **Google's Gemini Models:** Gemini models are noted for their speed and efficiency, especially in "flash" variants. They offer a good balance of performance and cost, making them a solid choice for iterative, lower-stakes tasks like reformatting text, generating lists, or performing quick checks.21

#### **Pricing and Usage Implications**

For a researcher, who is often working within the constraints of a grant or university budget, the economic implications of model selection are critical. Cursor operates on a usage-based system where different models consume "requests" from a monthly allowance at different rates.21 High-performance models like Claude Opus are more "expensive" per request than more efficient models like Gemini. For example, a Pro plan might offer 225 Claude Sonnet 4.5 requests but 550 Gemini requests for the same price.21

This economic reality necessitates a strategic approach to model selection. An agentic task that involves multiple steps and tool calls could rapidly deplete a monthly budget if a premium model is used for every sub-task. Therefore, the researcher must become adept at matching the model to the task's complexity and importance.

The following table provides a framework for making these strategic decisions.

**Table 1: Comparison of Primary LLMs in Cursor for Research Tasks**

| Model Name | Primary Strength | Best Suited For | Relative Usage Cost |
| :---- | :---- | :---- | :---- |
| **Claude 4 Opus** | Sophisticated, multi-step reasoning; large context understanding | Drafting detailed analysis plans; synthesizing complex literature reviews; ensuring logical consistency in arguments. | High |
| **Claude Sonnet 4.5** | Balanced performance and reasoning; strong instruction following | Executing structured protocols from AGENTS.md; drafting manuscript sections; data interpretation. | Medium-High |
| **GPT-5** | Creativity; broad knowledge base; fluent prose generation | Brainstorming research questions and hypotheses; generating initial drafts; explaining complex topics simply. | High |
| **Gemini 2.5 Pro** | Speed and efficiency; multimodal capabilities | Quick summarization; reformatting text and citations; generating boilerplate content; analyzing figures. | Medium |

### **Chapter 6: Model Context Protocol (MCP): Connecting Your Digital Lab to the World**

Scientific research is not conducted in a vacuum; it requires constant interaction with external data sources, from online publication databases to local experimental results. The **Model Context Protocol (MCP)** is the technology that enables this interaction. MCP is an open standard that functions like a "USB-C port for AI," allowing Cursor's agent to securely connect with a vast ecosystem of external tools, APIs, and data sources without needing custom-written integrations for each one.24 An MCP server acts as a standardized bridge, exposing the capabilities of an external service (like a database or a web scraper) in a way the AI can understand and use.26

#### **A Non-Coder's Guide to Using MCP Servers**

For the researcher, the key is not to build these servers, but to leverage the growing library of pre-built ones. Directories like Cursor's official MCP list, mcpservers.org, and Smithery.ai host numerous open-source servers that can be installed with minimal technical effort.27

The installation process is designed to be accessible to a semi-technical user. Here is a generalized, step-by-step walkthrough for adding a pre-built MCP server:

1. **Find an MCP Server:** Browse a directory like the([https://cursor.com/docs/context/mcp/directory](https://cursor.com/docs/context/mcp/directory)) and identify a server relevant to a research task. A powerful example is **Firecrawl**, a server designed for web scraping and data extraction.30  
2. **Obtain the Configuration:** The directory will typically provide a one-click "Add to Cursor" button or a JSON configuration snippet. For a command-line tool like Firecrawl, the configuration might look like this, often requiring an API key from the service's website 31:  
   JSON  
   {  
     "mcpServers": {  
       "firecrawl": {  
         "command": "npx",  
         "args": \["-y", "@firecrawl/mcp-server"\],  
         "env": { "FIRECRAWL\_API\_KEY": "YOUR\_API\_KEY\_HERE" }  
       }  
     }  
   }

3. **Add the Server in Cursor:**  
   * Navigate to Cursor's settings (the gear icon).  
   * Find the section for "Tools & Integrations" or "MCP".32  
   * Click "Add New MCP Server".  
   * Paste the JSON configuration into the appropriate fields. If it's a simple command, you can often just paste it directly.28  
4. **Restart and Verify:** Fully restart the Cursor application. After restarting, return to the MCP settings page to confirm that the new tool (e.g., "firecrawl") appears in the list of available tools.  
5. **Use the Tool in Chat:** Once installed, the agent can be instructed to use the tool by name. For example: *"Use Firecrawl to scrape the abstracts from the top 10 search results on PubMed for 'CRISPR gene editing review'."* The agent will automatically recognize the tool, formulate the correct command, and execute the web scrape.31

The following table highlights several MCP servers that are particularly valuable for a scientific research workflow.

**Table 2: Recommended MCP Servers for Scientific Researchers**

| MCP Server Name | Function | Research Use Case Example |
| :---- | :---- | :---- |
| **Firecrawl** | Web Scraping & Data Extraction | Automatically gather abstracts, articles, or data from online databases like PubMed, Google Scholar, or specific journal websites.31 |
| **Filesystem** | Local File Access & Manipulation | Allow the agent to read data from local CSV files, analyze log files from experiments, or organize output files into directories.\[34\] |
| **Database Connectors (e.g., PostgreSQL, DuckDB)** | Direct Database Querying | Connect directly to a lab's database to query experimental results, analyze patient data, or check inventory without manual exporting.\[35, 36\] |
| **Google / Brave Search** | Real-time Web Search | Augment the agent's knowledge with up-to-the-minute information, find recent news articles, or look up definitions of emerging technical terms.\[34\] |
| **Figma** | Design File Interaction | For research involving UI/UX or data visualization, allow the agent to inspect design mockups or extract style guidelines to ensure consistency in figures.\[35, 37\] |

### **Chapter 7: Claude Skills: Embedding Domain Expertise into Your AI**

While MCP servers connect the agent to external *tools*, **Claude Skills** embed specialized *knowledge and workflows* directly into the agent itself. A Skill is a self-contained folder of instructions, reference documents, and even executable scripts that provides Claude with a repeatable, expert-level capability for a specific domain.38 Skills are more powerful than simple prompts because they create a persistent, structured knowledge base that the agent can consult on demand, complete with best practices and concrete examples.40

#### **Case Study: The K-Dense-AI/claude-scientific-skills Repository**

The K-Dense-AI/claude-scientific-skills repository on GitHub is a landmark project for the scientific community, representing a comprehensive, open-source collection of Claude Skills tailored for scientific research.41 These skills run on Anthropic’s platforms (Claude Desktop, Claude Code CLI, or the Claude Code VS Code extension) and can be accessed inside Cursor only when the Claude Code extension is active. They provide ready-to-use capabilities across domains including bioinformatics, cheminformatics, data analysis, and materials science, giving Claude agents deep procedural knowledge without bespoke scripting.41 This repository serves as a powerful case study in how domain experts can collaborate to build and share specialized expertise for AI agents, saving individual researchers countless hours of development and prompt engineering.

#### **Installing and Activating the Scientific Skills**

The skills from this repository can be integrated into a compatible client like Cursor (when using Claude models) or the Claude Code CLI. The process typically involves adding the GitHub repository as a "plugin marketplace" and then installing the desired skill packages.41

A crucial component of this repository is the scientific-context-initialization skill. This is a powerful meta-skill that solves the "activation energy" problem of using a large toolkit. An agent may have access to dozens of specialized skills, but it will not use them unless it knows they exist and are relevant to the current task. The scientific-context-initialization skill automates this by creating or updating an AGENTS.md file in the user's project. This file contains a simple but powerful directive: "Before attempting any scientific task, always search for and use existing skills".41 This instruction bootstraps the entire scientific toolkit, ensuring the agent defaults to using the curated, expert-level workflows instead of relying solely on its general knowledge.

#### **Dissecting a Skill: scientific-visualization**

To understand how Skills provide such detailed guidance, it is instructive to analyze the structure of a SKILL.md file. The scientific-visualization skill, for example, is a masterclass in encoding expert knowledge for an AI.19 Its SKILL.md file contains:

* **Overview and When to Use:** A clear description of the skill's purpose—creating journal-ready plots—and a checklist of scenarios where it should be activated, such as "Preparing figures for journal submission (Nature, Science, Cell, PLOS, etc.)" or "Ensuring figures are colorblind-friendly".19  
* **Core Principles and Best Practices:** Detailed, instructional sections on fundamental concepts like resolution, file formats (vector vs. raster), colorblind-safe palettes (recommending the Okabe-Ito palette), typography standards, and journal-specific dimensions.19  
* **Common Tasks with Code Examples:** A series of practical, hands-on guides for tasks like "Create a Publication-Ready Line Plot" or "Create a Multi-Panel Figure." Each guide includes complete, commented Python code snippets using libraries like Matplotlib and Seaborn, demonstrating best practices in action.19  
* **Resources:** Links to other files within the skill's folder, such as references/publication\_guidelines.md and assets/nature.mplstyle, which provide even more granular detail and reusable assets.19  
* **Final Checklist:** A pre-submission checklist for the user (and agent) to verify that a figure meets all publication standards.19

This highly structured format provides the agent with a comprehensive operational manual, enabling it to produce outputs that adhere to the highest standards of scientific communication. The following table provides an overview of the main packages within the K-Dense-AI collection.

**Table 3: Overview of the claude-scientific-skills Collection**

| Skill Package | Description | Example Capabilities |
| :---- | :---- | :---- |
| **scientific-databases** | Provides tools and instructions for querying over 25 specialized scientific databases. | Querying gene information from Ensembl and NCBI Gene; screening compound libraries from PubChem; searching clinical trials on ClinicalTrials.gov.41 |
| **scientific-packages** | Contains skills for working with 57 specialized Python packages for scientific computing. | Processing genomic sequences with BioPython; analyzing single-cell RNA-seq data with Scanpy; predicting molecular properties with RDKit.41 |
| **scientific-thinking** | Includes skills for higher-level research tasks like analysis, visualization, and document processing. | Generating publication-quality visualizations; brainstorming novel hypotheses; manipulating DOCX, PDF, and PPTX files for reports and presentations.\[19, 41, 43\] |
| **scientific-integrations** | Focuses on skills for lab automation and integration with external research platforms. | Interfacing with laboratory information management systems (LIMS); automating data collection from scientific instruments.41 |

## **Part IV: The Agentic Workflow in Practice: A Complete Research Simulation**

This capstone section integrates all the concepts from the preceding parts into a single, cohesive, end-to-end narrative. It simulates a realistic scientific project, demonstrating how a researcher can orchestrate a complex, knowledge-intensive workflow using markdown files as the primary interface to direct the AI agent. This walkthrough will showcase the hierarchical control flow of an agentic research process, where the human acts as the strategic director, markdown files serve as the operational plan, AGENTS.md provides the governing policy, and MCPs and Skills function as the specialized tools for execution.

### **Chapter 8: From Hypothesis to First Draft: An End-to-End Walkthrough**

The chosen scenario is a common yet demanding task in academic research: **conducting a systematic review on a specific topic**. This task is ideal because it is heavily reliant on knowledge synthesis, critical analysis, and structured writing, making it a perfect application for a non-coding, agentic workflow.

**Scenario:** A researcher aims to conduct a systematic review on "The efficacy of mindfulness-based interventions (MBIs) for reducing anxiety in university students."

#### **Phase 1: Ideation and Scoping (The PROJECT\_PLAN.md)**

The project begins not with a literature search, but with a planning session to define the scope and methodology. The researcher creates a blank file, docs/PROJECT\_PLAN.md, and uses the AI as a thought partner.

* **Researcher's Action:** The researcher initiates the process with a high-level prompt, invoking a specialized skill for ideation.**Prompt:** "I am starting a new project in docs/PROJECT\_PLAN.md. The goal is to conduct a systematic review on mindfulness-based interventions for anxiety in university students. Using the scientific-brainstorming skill, act as a research ideation partner. Help me refine my research question, define specific inclusion and exclusion criteria for the studies, and outline a comprehensive search strategy. Structure this plan with clear headings in the PROJECT\_PLAN.md file."  
* **Agent's Execution:**  
  1. The agent, guided by the scientific-brainstorming skill 43, will not simply provide an answer. Instead, it will engage in a collaborative dialogue, asking probing questions like: "What specific types of MBIs should we include (e.g., MBSR, MBCT, meditation apps)?" or "What outcome measures for anxiety are most relevant (e.g., GAD-7, STAI)?"  
  2. Through this dialogue, the researcher and the agent collaboratively populate PROJECT\_PLAN.md with a detailed and rigorous protocol.

#### **Phase 2: Information Gathering (Using MCPs)**

With a clear plan, the researcher moves to the data collection phase. This is where external tools become essential. The researcher has already installed and configured the **Firecrawl MCP server** to give the agent web-scraping capabilities.

* **Researcher's Action:** The researcher issues a command that references the plan and directs the external tool.**Prompt:** "Execute the search strategy outlined in @docs/PROJECT\_PLAN.md. Use the Firecrawl tool to search PubMed and Google Scholar with the defined keywords. Scrape the full abstracts of the top 50 most relevant papers published since 2018\. For each abstract, extract the title, authors, year, and the abstract text itself. Save this information in a structured markdown format to a new file named docs/collected\_abstracts.md."  
* **Agent's Execution:**  
  1. The agent parses the prompt and identifies the need to use the Firecrawl MCP server.31  
  2. It reads @docs/PROJECT\_PLAN.md to retrieve the exact search terms and database targets.  
  3. It formulates and sends the appropriate commands to the Firecrawl server, which executes the searches and scrapes the data.  
  4. The agent receives the structured data back from the server and formats it as instructed, creating the docs/collected\_abstracts.md file.

#### **Phase 3: Synthesis and Analysis (Governed by AGENTS.md)**

This phase is the core of the intellectual work, where the raw information is filtered, analyzed, and synthesized. The quality and consistency of this work are governed by the policies established in the project's AGENTS.md file.

* **Researcher's Action:** The prompt for this phase is deceptively simple, as the complexity is handled by the pre-defined protocols.**Prompt:** "Read @docs/collected\_abstracts.md. Applying the inclusion and exclusion criteria from @docs/PROJECT\_PLAN.md, filter the collected studies. For all included studies, perform the extraction protocol as defined in AGENTS.md. Synthesize the key findings into thematic categories and write this synthesis in @docs/LITERATURE\_REVIEW.md."  
* **Agent's Execution:**  
  1. The agent's behavior is now heavily constrained by its "lab manual." It first reads the AGENTS.md file to load its core instructions.  
  2. It then reads the criteria from @docs/PROJECT\_PLAN.md and the abstracts from @docs/collected\_abstracts.md.  
  3. It systematically evaluates each abstract against the criteria, discarding those that do not fit.  
  4. For the remaining studies, it follows the Extraction Protocol from AGENTS.md—pulling out the hypothesis, methods, findings, and limitations for each one.  
  5. Finally, it performs the synthesis, grouping findings thematically (e.g., "Impact on Trait Anxiety," "Efficacy of App-Based MBIs," "Reported Adverse Events") and writing the summary in @docs/LITERATURE\_REVIEW.md.

#### **Phase 4: Manuscript Assembly (Putting It All Together)**

The final phase involves transforming the synthesized knowledge into a coherent narrative for publication. The agent's role shifts from analyst to writer, again guided by the project's established standards.

* **Researcher's Action:** The researcher directs the agent to begin drafting the manuscript.**Prompt:** "Using the synthesized findings in @docs/LITERATURE\_REVIEW.md and the project outline in @docs/PROJECT\_PLAN.md, write the first draft of the 'Introduction' and 'Discussion' sections in outputs/MANUSCRIPT\_DRAFT.md. Adhere strictly to the APA 7th Edition style guide and the formal, objective tone defined in AGENTS.md. Ensure all claims are supported by in-text citations."  
* **Agent's Execution:**  
  1. The agent consults AGENTS.md to set its persona and writing style (formal, objective, APA 7th).  
  2. It uses @docs/PROJECT\_PLAN.md to structure the introduction, outlining the problem and the review's objectives.  
  3. It draws heavily from the thematic synthesis in @docs/LITERATURE\_REVIEW.md to build the body of the text.  
  4. For the discussion section, it synthesizes the findings, discusses implications, and, referencing its protocol, identifies the limitations of the reviewed studies and suggests future research directions.  
  5. Throughout the process, it automatically formats citations and the overall document according to the APA 7th style guide.

This end-to-end simulation reveals the power of the agentic workflow. The researcher manages a complex, multi-stage project through a series of high-level, natural language commands. The intricate details of execution, analysis, and formatting are delegated to the AI, which operates consistently and reliably according to a set of human-defined, machine-readable protocols.

## **Part V: Conclusion and Best Practices**

The transition to an agentic research workflow represents a significant evolution in the role of the scientist. It shifts the focus from the rote mechanics of information processing to the higher-order tasks of strategic planning, critical evaluation, and creative insight. This final section distills the key lessons from this playbook into a set of guiding principles and provides a quick-reference guide to help solidify these new practices.

### **Chapter 9: Principles for Effective Human-AI Research Collaboration**

Mastering the agentic workflow is not about finding the perfect prompt; it is about adopting a new mindset for collaborating with an AI partner. The following principles are essential for a successful and productive human-AI research team.

* **Be the Architect, Not the Bricklayer:** The researcher's primary role is to design the system that enables high-quality research. This means focusing on creating a well-structured project directory, crafting a detailed PROJECT\_PLAN.md, and meticulously defining the agent's operating procedures in AGENTS.md. The AI becomes the "bricklayer," executing the architectural blueprint that the researcher has designed. The human's value is in the strategic oversight, not the manual execution.  
* **Garbage In, Garbage Out (Clarity is Paramount):** The quality of the AI's output is a direct reflection of the quality of the instructions it receives. Vague or ambiguous prompts will lead to generic and often incorrect results.6 The success of the entire workflow hinges on the clarity, detail, and specificity of the instructions provided in the markdown files, especially the AGENTS.md protocol.5 Investing time upfront to create a detailed plan and a robust set of rules will yield significantly better outcomes.  
* **Trust but Verify (The Human Remains in the Loop):** While the AI agent is a powerful collaborator, it is not an infallible oracle. It can misinterpret instructions, generate factually incorrect information ("hallucinate"), or miss subtle nuances in the data.8 The researcher's critical judgment remains the most important tool in the laboratory. Every output from the agent—from a literature summary to a statistical analysis—must be reviewed and validated by the human expert. The goal is to augment human intellect, not replace it.2  
* **Inspect the Agent Review Pane:** After each automated run, open Cursor’s Agent Review view to audit a unified diff of every file the agent touched, leave inline comments, and trigger follow-up fixes before merging changes.[38][39]  
* **Iterate and Refine (The Agent's Education is Ongoing):** The AGENTS.md file should be treated as a living document, not a static configuration file. As the project progresses, the researcher will identify areas where the agent's performance can be improved. Instead of correcting the same mistakes repeatedly in chat, the researcher should update the agent's core instructions. This iterative refinement process effectively "trains" the agent on the specific preferences and standards of the project, making it a progressively more effective and intelligent partner over time.20

### **Chapter 10: Playbook Quick-Reference**

This section provides a concise, one-page summary of the key steps and tools covered in this playbook, designed for quick reference during a research project.

#### **The Agentic Research Workflow Checklist**

1. **\[ \] Project Setup:**  
   * Create the core project directory structure (data/, docs/, outputs/).  
   * Create initial blank markdown files: PROJECT\_PLAN.md, LITERATURE\_REVIEW.md, etc.  
2. **\[ \] Define the Protocol (AGENTS.md):**  
   * Create an AGENTS.md file in the project root.  
   * Define the core sections: Project Overview, Persona, Literature Protocol, Data Guidelines, and Manuscript Style.  
3. **\[ \] Augment the Agent (Tools & Skills):**  
   * Select the appropriate primary LLM (e.g., Claude for reasoning, GPT for brainstorming) for the day's tasks.  
   * Install necessary MCP Servers for external data access (e.g., Firecrawl for web scraping).  
   * Install relevant Claude Skills via Claude Desktop or the Claude Code extension (e.g., claude-scientific-skills) and ensure the scientific-context-initialization skill is active before invoking them inside Cursor.  
4. **\[ \] Execute in Phases (Markdown-First):**  
   * **Phase 1 (Plan):** Use the agent as a thought partner to populate PROJECT\_PLAN.md.  
   * **Phase 2 (Gather):** Direct the agent to use MCPs to collect data, referencing the plan (@docs/PROJECT\_PLAN.md).  
   * **Phase 3 (Synthesize):** Instruct the agent to analyze the collected data according to the rules in AGENTS.md.  
   * **Phase 4 (Draft):** Command the agent to assemble the final manuscript, referencing all relevant documents.  
5. **\[ \] Review and Iterate:**  
   * Critically review all AI-generated output for accuracy and quality.  
   * Update AGENTS.md with new learnings and corrections to improve future performance.

#### **Essential Commands and AGENTS.md Sections**

* **Key Command:** @filename.md \- The most important command for providing file-specific context to the agent.  
* **Essential AGENTS.md Sections:**  
  * \#\# Persona and Communication Style: Sets the tone and voice.  
  * \#\# Literature Search and Synthesis Protocol: Defines rules for evidence gathering.  
  * \#\# Data Interpretation Guidelines: Enforces methodological rigor.  
  * \#\# Manuscript and Citation Style: Ensures outputs are publication-ready.

#### **Recommended Starter Kit**

* **Recommended LLM for General Research:** Claude Sonnet 4.5 (strong balance of reasoning and cost).  
* **Essential MCP Servers:** Firecrawl (web), Filesystem (local), a relevant database connector.  
* **Essential Claude Skills:** When running Claude via Desktop or the Claude Code extension, enable the K-Dense-AI/claude-scientific-skills repository—give special attention to the scientific-thinking package for writing and analysis.

#### **Works cited**

1. Cursor: The best way to code with AI, accessed November 2, 2025, [https://cursor.com/](https://cursor.com/)  
2. Students · Cursor, accessed November 2, 2025, [https://cursor.com/students](https://cursor.com/students)  
3. Cursor 2.0 and Composer: how a multi-agent rethink surprised AI coding \- CometAPI, accessed November 2, 2025, [https://www.cometapi.com/cursor-2-0-what-changed-and-why-it-matters/](https://www.cometapi.com/cursor-2-0-what-changed-and-why-it-matters/)  
4. Agentic workflow for feature creation \- Cursor \- Community Forum, accessed November 2, 2025, [https://forum.cursor.com/t/agentic-workflow-for-feature-creation/51649](https://forum.cursor.com/t/agentic-workflow-for-feature-creation/51649)  
5. Mastering Cursor IDE: 10 Best Practices (Building a Daily Task Manager App) \- Medium, accessed November 2, 2025, [https://medium.com/@roberto.g.infante/mastering-cursor-ide-10-best-practices-building-a-daily-task-manager-app-0b26524411c1](https://medium.com/@roberto.g.infante/mastering-cursor-ide-10-best-practices-building-a-daily-task-manager-app-0b26524411c1)  
6. How I'm Using Agentic Coding with Claude and Cursor in Real-World Projects, accessed November 2, 2025, [https://ed-wentworth.medium.com/how-im-using-agentic-coding-with-claude-and-cursor-in-real-world-projects-b4b6694c132d](https://ed-wentworth.medium.com/how-im-using-agentic-coding-with-claude-and-cursor-in-real-world-projects-b4b6694c132d)  
7. Cursor 2.0 Workflow Tips: Shortcuts for Faster Coding \- skywork ai, accessed November 2, 2025, [https://skywork.ai/blog/vibecoding/cursor-2-0-workflow-tips/](https://skywork.ai/blog/vibecoding/cursor-2-0-workflow-tips/)  
8. My New Favorite IDE: Cursor \- Mensur Duraković, accessed November 2, 2025, [https://www.mensurdurakovic.com/my-new-favorite-ide-cursor/](https://www.mensurdurakovic.com/my-new-favorite-ide-cursor/)  
9. Using Agent in CLI | Cursor Docs, accessed November 2, 2025, [https://cursor.com/docs/cli/using](https://cursor.com/docs/cli/using)  
10. What is AGENTS.md and Why Should You Care? \- DEV Community, accessed November 2, 2025, [https://dev.to/proflead/what-is-agentsmd-and-why-should-you-care-3bg4](https://dev.to/proflead/what-is-agentsmd-and-why-should-you-care-3bg4)  
11. AGENTS.md, accessed November 2, 2025, [https://agents.md/](https://agents.md/)  
12. Agents.md: The README for Your AI Coding Agents \- Research AIMultiple, accessed November 2, 2025, [https://research.aimultiple.com/agents-md/](https://research.aimultiple.com/agents-md/)  
13. Agents.md: A Comprehensive Guide to Agentic AI Collaboration | by DhanushKumar, accessed November 2, 2025, [https://ai.plainenglish.io/agents-md-a-comprehensive-guide-to-agentic-ai-collaboration-571df0e78ccc](https://ai.plainenglish.io/agents-md-a-comprehensive-guide-to-agentic-ai-collaboration-571df0e78ccc)  
14. Rules | Cursor Docs, accessed November 2, 2025, [https://cursor.com/docs/context/rules](https://cursor.com/docs/context/rules)  
15. Agentic Project Management \- My AI workflow : r/cursor \- Reddit, accessed November 2, 2025, [https://www.reddit.com/r/cursor/comments/1l2p2y6/agentic\_project\_management\_my\_ai\_workflow/](https://www.reddit.com/r/cursor/comments/1l2p2y6/agentic_project_management_my_ai_workflow/)  
16. Introduction to Agents.md | genai-research – Weights & Biases \- Wandb, accessed November 2, 2025, [https://wandb.ai/wandb\_fc/genai-research/reports/Introduction-to-Agents-md--VmlldzoxNDEwNDI2Ng](https://wandb.ai/wandb_fc/genai-research/reports/Introduction-to-Agents-md--VmlldzoxNDEwNDI2Ng)  
17. Conversational Planning for Personal Plans, accessed November 2, 2025, [https://arxiv.org/pdf/2502.19500?](https://arxiv.org/pdf/2502.19500)  
18. (PDF) Curriculum-Based Meta-Learning for LLM Alignment: Dynamic Control of Imitation and Exploration Phases \- ResearchGate, accessed November 2, 2025, [https://www.researchgate.net/publication/394511683\_Curriculum-Based\_Meta-Learning\_for\_LLM\_Alignment\_Dynamic\_Control\_of\_Imitation\_and\_Exploration\_Phases](https://www.researchgate.net/publication/394511683_Curriculum-Based_Meta-Learning_for_LLM_Alignment_Dynamic_Control_of_Imitation_and_Exploration_Phases)  
19. raw.githubusercontent.com, accessed November 2, 2025, [https://raw.githubusercontent.com/K-Dense-AI/claude-scientific-skills/main/scientific-thinking/scientific-visualization/SKILL.md](https://raw.githubusercontent.com/K-Dense-AI/claude-scientific-skills/main/scientific-thinking/scientific-visualization/SKILL.md)  
20. How to teach your coding agent with AGENTS.md \- Eric J. Ma's Personal Site \- Eric Ma, accessed November 2, 2025, [https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/)  
21. Cursor vs Claude Code: Ultimate Comparison Guide \- Builder.io, accessed November 2, 2025, [https://www.builder.io/blog/cursor-vs-claude-code](https://www.builder.io/blog/cursor-vs-claude-code)  
22. Claude Code vs Cursor: Deep Comparison for Dev Teams \[2025\] \- Qodo, accessed November 2, 2025, [https://www.qodo.ai/blog/claude-code-vs-cursor/](https://www.qodo.ai/blog/claude-code-vs-cursor/)  
23. Testing AI coding agents (2025): Cursor vs. Claude, OpenAI, and ..., accessed November 2, 2025, [https://render.com/blog/ai-coding-agents-benchmark](https://render.com/blog/ai-coding-agents-benchmark)  
24. Model Context Protocol (MCP) Explained With Examples \- AltexSoft, accessed November 2, 2025, [https://www.altexsoft.com/blog/model-context-protocol/](https://www.altexsoft.com/blog/model-context-protocol/)  
25. What is Model Context Protocol (MCP): Explained \- Composio, accessed November 2, 2025, [https://composio.dev/blog/what-is-model-context-protocol-mcp-explained](https://composio.dev/blog/what-is-model-context-protocol-mcp-explained)  
26. Bringing AI to Your Data: Integrating Cursor with Snowflake MCP Server, accessed November 2, 2025, [https://medium.com/snowflake/bringing-ai-to-your-data-integrating-cursor-with-snowflake-mcp-server-f428c5b6fcd1](https://medium.com/snowflake/bringing-ai-to-your-data-integrating-cursor-with-snowflake-mcp-server-f428c5b6fcd1)  
27. Model Context Protocol (MCP) | Cursor Docs, accessed November 2, 2025, [https://cursor.com/docs/context/mcp](https://cursor.com/docs/context/mcp)  
28. How to Get started with Cursor AI and MCP: A Comprehensive Tutorial \- Apidog, accessed November 2, 2025, [https://apidog.com/blog/cursor-ai-mcp/](https://apidog.com/blog/cursor-ai-mcp/)  
29. Awesome MCP Servers, accessed November 2, 2025, [https://mcpservers.org/](https://mcpservers.org/)  
30. 10 Best MCP Servers to Boost Cursor Productivity \- Clockwise, accessed November 2, 2025, [https://www.getclockwise.com/blog/best-cursor-mcp-servers](https://www.getclockwise.com/blog/best-cursor-mcp-servers)  
31. 15 Best MCP Servers You Can Add to Cursor For 10x Productivity \- Firecrawl, accessed November 2, 2025, [https://www.firecrawl.dev/blog/best-mcp-servers-for-cursor](https://www.firecrawl.dev/blog/best-mcp-servers-for-cursor)  
32. Cursor Meets MCP: Elasticsearch \+ Jupyter in One Workflow, accessed November 2, 2025, [https://medium.com/@CyberRaya/cursor-meets-mcp-elasticsearch-jupyter-in-one-workflow-755f5b795361](https://medium.com/@CyberRaya/cursor-meets-mcp-elasticsearch-jupyter-in-one-workflow-755f5b795361)  
33. MCP in Cursor AI. In this article we will add tools to… | by Lovelyn David | Medium, accessed November 2, 2025, [https://medium.com/@lovelyndavid/mcp-in-cursor-ai-02e3d96eb593](https://medium.com/@lovelyndavid/mcp-in-cursor-ai-02e3d96eb593)  
34. anthropics/skills: Public repository for Skills \- GitHub, accessed November 2, 2025, [https://github.com/anthropics/skills](https://github.com/anthropics/skills)  
35. A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows \- GitHub, accessed November 2, 2025, [https://github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)  
36. I've been tracking what people are building with Claude Skills since launch \- here's the wildest stuff I've found (with links) : r/ClaudeAI \- Reddit, accessed November 2, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1o9ph4u/ive\_been\_tracking\_what\_people\_are\_building\_with/](https://www.reddit.com/r/ClaudeAI/comments/1o9ph4u/ive_been_tracking_what_people_are_building_with/)  
37. K-Dense-AI/claude-scientific-skills \- GitHub, accessed November 2, 2025, [https://github.com/K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)  
38. ai-scientist · GitHub Topics, accessed November 2, 2025, [https://github.com/topics/ai-scientist](https://github.com/topics/ai-scientist)  
39. raw.githubusercontent.com, accessed November 2, 2025, [https://raw.githubusercontent.com/K-Dense-AI/claude-scientific-skills/main/scientific-thinking/scientific-brainstorming/SKILL.md](https://raw.githubusercontent.com/K-Dense-AI/claude-scientific-skills/main/scientific-thinking/scientific-brainstorming/SKILL.md)  
40. Models overview \- Claude Docs, accessed November 2, 2025, [https://docs.anthropic.com/claude/docs/models-overview](https://docs.anthropic.com/claude/docs/models-overview)
43. Claude Code on the web – best practices, accessed November 2, 2025, https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web#best-practices
45. Codex cloud – managed sandboxes and parallel tasks. OpenAI Developers (2025). https://developers.openai.com/codex/cloud  
46. Codex IDE extension surfaces. OpenAI Developers (2025). https://developers.openai.com/codex/ide  
47. Codex Agents SDK (TypeScript). OpenAI Developers (2025). https://developers.openai.com/codex/sdk  
48. Codex configuration – MCP servers. OpenAI Codex GitHub (2025). https://github.com/openai/codex/blob/main/docs/config.md#mcp_servers  
49. Introducing Claude Skills. Anthropic News (2025). https://www.anthropic.com/news/skills  
