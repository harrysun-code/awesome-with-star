# Copilot Agents

[![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/stargazers)

<!--lint disable remark-lint:awesome-list-item-->

#

<!-- [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) -->
<div align="center">
  <img src="./.refs/imgs/awesome-github-copilot.svg" alt="Awesome Copilot Agents" height="300">
</div>

<h4 align="center">✨ A curated list of awesome GitHub instructions, prompt, skills, MCPs and custom agent markdown files for enhancing your GitHub Copilot AI experience.</h4>

<!--lint enable remark-lint:awesome-badge-->

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge-flat2.svg" alt="Awesome">
  </a>
</p>

<hr>

<p align="center">
 <a href="CONTRIBUTING.md">📖 Contribution Guide</a>
</p>
<br>

## Contents

- [Why Copilot Agents](#why-copilot-agents)
- [Instructions](#instructions)
  - [Boilerplates & Templates](#boilerplates--templates)
  - [Language & Stack](#language--stack)
  - [Framework / Library](#framework--library)
  - [Tools](#tools)
  - [Workflows](#workflows)
- [Prompts](#prompts)
  - [AI Development Tasks](#ai-development-tasks)
- [Custom Agents](#custom-agents)
  - [AI Development Mode](#ai-development-mode)
- [Agent Skills](#agent-skills)
- [MCPs](#mcps)
- [How to Use](#how-to-use)

## Why Copilot Agents

Customized instructions, prompts, agent skills, agent MCPs and custom agents help guide GitHub Copilot by providing contextual details about your repository such as the type of workflow your team follows, tools and other project specific details such as coding style, frameworks used or project specific rules.

**Tip**: Learn more about customizing GitHub Copilot in VS Code in the [VS Code documentation](https://code.visualstudio.com/docs/copilot/customization/overview).

## Instructions

Instructions provides Copilot with repository-specific context, such as coding standards, frameworks, or workflows, to improve code suggestions.

### Boilerplates & Templates

#### Templates

- [General Language](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-language.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-language.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-language.instructions.md/stargazers) - Standard language template to build instruction files.

#### Boilerplate

- [Standard IaC Tools Boilerplate](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-iac-tools.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-iac-tools.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-iac-tools.instructions.md/stargazers) - Standard tool boilerplate for infrastructure-as-code tools.

### Language & Stack

#### C

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/c/c.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/c/c.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/c/c.instructions.md/stargazers) - System libraries, CLI tools, and embedded applications with POSIX/GNU libc.

#### C-Sharp

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/csharp/csharp.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/csharp/csharp.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/csharp/csharp.instructions.md/stargazers) - .NET applications with modern C# patterns and best practices.

#### C++

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/cplusplus/cplusplus.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/cplusplus/cplusplus.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/cplusplus/cplusplus.instructions.md/stargazers) - Modern C++ development with STL, RAII, and performance optimization.

#### Go

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/go/go.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/go/go.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/go/go.instructions.md/stargazers) - Go for microservices, CLI tools, and concurrent applications.

#### Java

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/java/java.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/java/java.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/java/java.instructions.md/stargazers) - Enterprise Java development with Spring framework and modern patterns.

#### JavaScript

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/javascript/javascript.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/javascript/javascript.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/javascript/javascript.instructions.md/stargazers) - Modern JavaScript with ES6+, Node.js, and browser development.

#### Kotlin

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/kotlin/kotlin.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/kotlin/kotlin.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/kotlin/kotlin.instructions.md/stargazers) - Kotlin for Android development and multi-platform projects.

#### Lua

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/lua/lua.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/lua/lua.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/lua/lua.instructions.md/stargazers) - Lua scripting for embedded systems, game development, and automation.

#### Python

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/python/python.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/python/python.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/python/python.instructions.md/stargazers) - Python development for web applications, data science, and automation.

#### Rust

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/rust/rust.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/rust/rust.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/rust/rust.instructions.md/stargazers) - Systems programming with Rust's ownership model and memory safety.

#### Swift

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/swift/swift.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/swift/swift.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/swift/swift.instructions.md/stargazers) - iOS and macOS development with Swift and SwiftUI.

#### TypeScript

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/typescript/typescript.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/typescript/typescript.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/typescript/typescript.instructions.md/stargazers) - TypeScript development for web and Node.js applications.

### Framework / Library

#### Cobra CLI (Go)

- [Charmbracelet Bubbles CLI](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/cobra-cli-go/charmbracelet-cli.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/cobra-cli-go/charmbracelet-cli.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/cobra-cli-go/charmbracelet-cli.instructions.md/stargazers) - Interactive terminal applications with Charm's Bubble Tea framework and Golang Cobra CLI.

#### Node.js (TypeScript)

- [Azure Function App](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/azure-function-app.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/azure-function-app.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/azure-function-app.instructions.md/stargazers) - Azure Function Apps using TypeScript Node.js.
- [Express API](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/express-api.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/express-api.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/express-api.instructions.md/stargazers) - REST API development with Express.js and TypeScript Node.js.

### Tools

#### Content Management Systems (CMS)

##### Drupal

- [Standard Focus for Drupal 11](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/cms/drupal/drupal-11.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/cms/drupal/drupal-11.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/cms/drupal/drupal-11.instructions.md/stargazers) - Drupal 11 module and theme development.

#### Infra as Code (IaC)

##### Terraform

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/terraform.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/terraform.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/terraform.instructions.md/stargazers) - Standard Terraform instructions.
- [Atmos](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/atmos-terraform.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/atmos-terraform.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/atmos-terraform.instructions.md/stargazers) - Terraform workflow orchestration with Atmos framework.

### Workflows

#### AI Development Instructions

A comprehensive workflow for AI-assisted development featuring structured approaches to planning, task generation, and execution.

- [PRD Creation](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/prd-creation.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/prd-creation.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/prd-creation.instructions.md/stargazers) - Create detailed Product Requirements Documents.
- [Task Generation](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-generation.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-generation.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-generation.instructions.md/stargazers) - Break PRDs into actionable development tasks.
- [Task Execution](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-execution.instructions.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-execution.instructions.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-execution.instructions.md/stargazers) - Systematic task execution with proper testing and Git practices.

## Prompts

Prompts are reusable tasks or workflow instructions that help guide Copilot to perform specific actions or generate certain outputs.

### AI Development Tasks

A comprehensive workflow for AI-assisted development featuring structured approaches to planning, task generation, and execution.

- [PRD Creation Prompt](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/prd-creation.prompt.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/prd-creation.prompt.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/prd-creation.prompt.md/stargazers) - Create detailed Product Requirements Documents using prompt tasks.
- [Task Generation Prompt](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-generation.prompt.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-generation.prompt.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-generation.prompt.md/stargazers) - Break PRDs into actionable development tasks using prompt tasks.
- [Task Execution Prompt](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-execution.prompt.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-execution.prompt.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-execution.prompt.md/stargazers) - Systematic task execution with proper testing and Git practices using prompt tasks.

## Custom Agents

[Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) let you set up different AI personas in VS Code for specific dev roles (like security reviewer, planner, or architect), each with its own instructions, tools, and behavior. You can also use handoffs to move between these specialized agents in a guided workflow (e.g., planning → implementation → review) with relevant context carried over.

The built-in available custom agents are:

- Agent
- Ask
- Edit
- Plan
- AIAgentExpert
- Configure Custom Agents (create your own)

### AI Development Mode

- [Architect](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/architect.agent.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/architect.agent.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/architect.agent.md/stargazers) - Design and plan software systems.
- [Clean Code](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/clean-code.agent.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/clean-code.agent.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/clean-code.agent.md/stargazers) - Write clean, readable, and maintainable code using clean code best practices.
- [Debugger](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/debugger.agent.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/debugger.agent.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/debugger.agent.md/stargazers) - Debug your application code to find a fix.
- [PRD Creation](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/prd-creation.agent.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/prd-creation.agent.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/prd-creation.agent.md/stargazers) - Build Product Requirements Document (PRD).

## Agent Skills

Agent Skills are portable, [open standard](https://agentskills.io/home), version-controlled folders of instructions, scripts, and resources that agents can discover and load on demand to do tasks more accurately and efficiently. They let agents gain domain expertise, new capabilities, and repeatable workflows—while making those same skills reusable across different compatible agent products and teams.

### General

- [Calculator](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/calculator/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/calculator/SKILL.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/calculator/SKILL.md/stargazers) - Performs arbitrary-precision arithmetic calculations including addition, subtraction, multiplication, division, and exponents.
- [Jira CLI](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/jira-cli/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/jira-cli/SKILL.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/jira-cli/SKILL.md/stargazers) - Interact with Jira from the command line to create, list, view, edit, and transition issues, manage sprints and epics, and perform common Jira workflows.
- [Skill Creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/anthropics/skills/blob/main/skills/skill-creator/SKILL.md?style=flat)](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md/stargazers) - Create new skills, modify and improve existing skills, and measure skill performance.

### Documents

- [docx](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/docx/README.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/docx/README.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/docx/README.md/stargazers) - Document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction.
- [pdf](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pdf/README.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pdf/README.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pdf/README.md/stargazers) - PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms.
- [pptx](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pptx/README.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pptx/README.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pptx/README.md/stargazers) - Presentation creation, editing, and analysis.
- [xlsx](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/xlsx/README.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/xlsx/README.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/xlsx/README.md/stargazers) - Spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization.

### Cloud

- [Az CLI](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/az-cli/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/az-cli/SKILL.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/az-cli/SKILL.md/stargazers) - Azure CLI documentation to execute or ask about Azure CLI commands.
- [Azure Prices](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/azure-prices/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/azure-prices/SKILL.md?style=flat)](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/azure-prices/SKILL.md/stargazers) - Look up and compare Azure service pricing using the Azure Retail Prices API.

### Development

- [Playwright CLI](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md?style=flat)](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md/stargazers) - Automate browser interactions, test web pages and work with Playwright tests.
- [Frontend Design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/anthropics/skills/blob/main/skills/frontend-design/SKILL.md?style=flat)](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md/stargazers) - Create distinctive, production-grade frontend interfaces with high design quality.
- [Webapp Testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md?style=flat)](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md/stargazers) - Toolkit for interacting with and testing local web applications using Playwright.

## MCPs

MCPs (Model Context Protocol servers) give agents a standardized way to connect to external tools, APIs, data sources, and local capabilities. They extend what an agent can do beyond plain chat by exposing actions such as reading files, browsing the web, querying cloud platforms, or interacting with development tooling through a common protocol.

This section highlights useful MCP servers you can add to your Copilot setup to expand agent capabilities for research, development, automation, and cloud workflows.

### General MCPs

- [Knowledge Graph Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/servers/tree/main/src/memory?style=flat)](https://github.com/modelcontextprotocol/servers/tree/main/src/memory/stargazers) - Create a local knowledge graph for your agent to remember information across different chat sessions.
- [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/servers/tree/main/src/filesystem?style=flat)](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem/stargazers) - Read and write files in batch operations, search file contents, list files, and validate file paths.
- [Fetch](https://github.com/modelcontextprotocol/servers/blob/main/src/fetch) [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/servers/blob/main/src/fetch?style=flat)](https://github.com/modelcontextprotocol/servers/blob/main/src/fetch/stargazers) - Automate web browsing for agents to retrieve and process content from web pages, converting HTML to markdown for easier consumption.
- [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/servers/tree/main/src/sequentialthinking?style=flat)](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking/stargazers) - Break down complex problems into structured steps.
- [GitHub](https://github.com/github/github-mcp-server) [![GitHub stars](https://img.shields.io/github/stars/github/github-mcp-server?style=flat)](https://github.com/github/github-mcp-server/stargazers) - Allow your agent access to repository and workflow management.
- [Time](https://github.com/modelcontextprotocol/servers/blob/main/src/time) [![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/servers/blob/main/src/time?style=flat)](https://github.com/modelcontextprotocol/servers/blob/main/src/time/stargazers) - Enables agents to get current time information and perform timezone conversions using IANA timezone names, with automatic system timezone detection.

### Development MCPs

- [Playwright](https://github.com/microsoft/playwright-mcp) [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=flat)](https://github.com/microsoft/playwright-mcp/stargazers) - Playwright MCP to automate browser interactions, test web pages and work with Playwright tests.
- [Context7](https://github.com/upstash/context7) [![GitHub stars](https://img.shields.io/github/stars/upstash/context7?style=flat)](https://github.com/upstash/context7/stargazers) - Inject version-specific code documentation in your agent session to provide the correct API docs for code generation.

### Cloud MCPs

- [Azure MCP](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md) [![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md?style=flat)](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md/stargazers) - Azure MCP Server supercharges your agents with Azure context across different Azure services.
- [AWS Documentation](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server) [![GitHub stars](https://img.shields.io/github/stars/awslabs/mcp/tree/main/src/aws-documentation-mcp-server?style=flat)](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server/stargazers) - Agent tools to access AWS documentation, search for content, and get recommendations.
- [gcloud](https://github.com/googleapis/gcloud-mcp) [![GitHub stars](https://img.shields.io/github/stars/googleapis/gcloud-mcp?style=flat)](https://github.com/googleapis/gcloud-mcp/stargazers) - Agent tools to interact with the Google Cloud environment using the gcloud CLI.
- [KubeStellar Console](https://github.com/kubestellar/console) [![GitHub stars](https://img.shields.io/github/stars/kubestellar/console?style=flat)](https://github.com/kubestellar/console/stargazers) - MCP server bridging AI agents to multi-cluster Kubernetes environments for cluster management, pod inspection, and real-time observability.

## How to Use

### Setup Copilot in VSCode

1. Hover over the Copilot icon in the Status Bar and select Set up Copilot.
2. Select **Sign in** to sign in to your GitHub account or **Use Copilot** if you're already signed in.

**Tip**: Read more about setting up [VS Code Copilot](https://code.visualstudio.com/docs/copilot/setup).

### Setup Instructions

1. Create instruction files using the latest naming conventions:
    1. Workspace instructions (place `*.instructions.md` files in `.github/instructions/` directory).
    2. Workspace prompts (place `*.prompt.md` files in `.github/prompts/` directory).
    3. Workspace custom agents (place `*.agent.md` files in `.github/agents` directory).
    4. Workspace custom skills (skills are stored in directories with a `SKILL.md` file that defines the skill's behavior).
    5. Workspace single instruction (place `copilot-instructions.md` in `.github` directory).

#### File Types

##### Instruction Files

`.instructions.md` - Contextual instructions that apply to specific files or file types.

##### Prompt Files

`.prompt.md` - Reusable prompts for specific tasks or workflows.

##### Custom Agent Files

`.agent.md` - Predefined AI personas behavior in VS Code for specific dev roles.

##### Custom Agent Skills

`SKILLS.md` - Portable, version-controlled folders of instructions, scripts, and resources that agents can discover and load on demand.

##### Formatting

Use YAML front matter to specify metadata like `applyTo`, `mode`, and `description`.

## Contributing

All contributions are welcome! If you would like to share instruction files (`.instructions.md`), prompt files (`.prompt.md`), skills (`SKILL.md` in a skill folder) or custom agents (`.agent.md`), see the [contribution guide](CONTRIBUTING.md) for details.
