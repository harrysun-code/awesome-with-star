# Master CSS

> 来源：[master-co/awesome-master-css](https://github.com/master-co/awesome-master-css)

[![GitHub stars](https://img.shields.io/github/stars/master-co/awesome-master-css?style=flat)](https://github.com/master-co/awesome-master-css/stargazers)

# Awesome Master CSS [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<a href="https://css.master.co"><picture><source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/33840671/205240887-0e354830-f0d4-4eb6-b604-9f7b8112c92c.svg"><source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/33840671/205238744-7355106d-d454-4b3d-a40a-7b19e34ddb9d.svg"><img alt="Master CSS" src="https://user-images.githubusercontent.com/33840671/205238744-7355106d-d454-4b3d-a40a-7b19e34ddb9d.svg" height="60" width="350" align="right"></picture></a>

> A curated list of resources for Master CSS, a markup-driven CSS orchestration language for developers and AI agents.

Master CSS turns the classes in your markup into the CSS your pages use, driven by CSS-first theme tokens. It can generate static CSS at build time, render it on the server, or run in the browser, with editor, lint and AI tooling that understand your design system.

## Contents

- [Official Resources](#official-resources)
- [Learning](#learning)
- [Framework Integrations](#framework-integrations)
- [Tools](#tools)
- [Editor Support](#editor-support)
- [AI Coding](#ai-coding)
- [Examples](#examples)
- [Articles](#articles)
- [Related Libraries](#related-libraries)
- [Community](#community)

## Official Resources

- [Website](https://css.master.co) - Homepage and documentation.
- [Repository](https://github.com/master-co/css) [![GitHub stars](https://img.shields.io/github/stars/master-co/css?style=flat)](https://github.com/master-co/css/stargazers) - Source code of the language, compiler, integrations and tooling.
- [Releases](https://github.com/master-co/css/releases) - Version history and release notes.
- [`@master/css`](https://www.npmjs.com/package/@master/css) - The core package on npm.
- [Master CSS 2.0 Film](https://youtu.be/lQLEHN-AiBw) - Launch film for Master CSS 2.0.

## Learning

- [Introduction](https://css.master.co/guide/introduction) - What Master CSS is and how it works.
- [Installation](https://css.master.co/guide/installation) - Add Master CSS to a new or existing project.
- [Syntax Tutorial](https://css.master.co/guide/syntax-tutorial) - Read and write Master CSS classes step by step.
- [Reference](https://css.master.co/reference) - Every utility, token, directive and selector the preset supports.
- [Migration](https://css.master.co/guide/migration) - Move from Tailwind CSS, Bootstrap, Sass, CSS-in-JS, Material UI, shadcn/ui or plain CSS one route at a time.
- [Benchmarks](https://css.master.co/benchmarks) - How much delivered CSS a page uses, generated CSS compared for the same UI, and build and runtime costs.
- [`llms.txt`](https://css.master.co/llms.txt) - The documentation as plain text for language models.

## Framework Integrations

- [Astro](https://css.master.co/guide/installation/astro) - `@master/css-astro` integration.
- [Next.js](https://css.master.co/guide/installation/nextjs) - `@master/css-next` integration for the App Router, with pre-rendered and request-time pages.
- [Nuxt](https://css.master.co/guide/installation/nuxtjs) - `@master/css-nuxt` module with static, browser or Nitro response rendering.
- [SvelteKit](https://css.master.co/guide/installation/svelte) - `@master/css-svelte` integration, installed with `npx sv add @master/css-svelte-addon`.
- [Vite](https://css.master.co/guide/installation/vite) - `@master/css-vite` plugin for Vite, React, Vue, React Router and TanStack Start.
- [Webpack](https://css.master.co/guide/installation/webpack) - `@master/css-webpack` plugin for Webpack, Rspack and Rsbuild.
- [Angular](https://css.master.co/guide/installation/angular) - CLI-generated CSS, or the optional browser runtime.
- [Lit](https://css.master.co/guide/installation/lit) - Style shadow roots with static CSS or a runtime that follows the component lifecycle.
- [Storybook](https://css.master.co/guide/installation/storybook) - Load application styles into the Storybook preview with the Vite builder.
- [Server-Rendered Apps](https://css.master.co/guide/installation/server-rendered) - Build with Vite and load the CSS from PHP, Laravel, Rails, WordPress, Shopify, ASP.NET Core, Blazor or Express templates.

## Tools

- [`create-css`](https://www.npmjs.com/package/@master/create-css) - Add Master CSS to an existing project with `npm create @master/css`.
- [`@master/css-cli`](https://www.npmjs.com/package/@master/css-cli) - Scan sources and generate static CSS from the command line.
- [`@master/css-runtime`](https://www.npmjs.com/package/@master/css-runtime) - Generate CSS in the browser as classes appear.
- [`@master/css-server`](https://www.npmjs.com/package/@master/css-server) - Render the CSS for server-generated HTML.
- [ESLint Plugin](https://css.master.co/guide/code-linting) - Sort classes and report invalid, non-canonical or conflicting classes with `@master/eslint-plugin-css`.

## Editor Support

- [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=masterco.master-css-vscode) - Official extension with completion, hover previews, syntax highlighting, color tools and diagnostics.
- [Language Server](https://github.com/master-co/css/tree/main/packages/language-server) [![GitHub stars](https://img.shields.io/github/stars/master-co/css/tree/main/packages/language-server?style=flat)](https://github.com/master-co/css/tree/main/packages/language-server/stargazers) - `@master/css-language-server` for editors that speak the Language Server Protocol.
- [Language Service Guide](https://css.master.co/guide/language-service) - Set up and tune editor support for your project.

## AI Coding

- [AI Coding Guide](https://css.master.co/guide/ai-coding) - Work with coding agents and verify what they change.
- [MCP Server](https://github.com/master-co/css/tree/main/packages/mcp) [![GitHub stars](https://img.shields.io/github/stars/master-co/css/tree/main/packages/mcp?style=flat)](https://github.com/master-co/css/tree/main/packages/mcp/stargazers) - `@master/css-mcp` lets agents inspect classes, render CSS, lint, preview fixes and read design system contracts.
- [Agent Skill](https://github.com/master-co/css/tree/main/skills/master-css) [![GitHub stars](https://img.shields.io/github/stars/master-co/css/tree/main/skills/master-css?style=flat)](https://github.com/master-co/css/tree/main/skills/master-css/stargazers) - Teach coding agents Master CSS with `npx skills add master-co/css --skill master-css`.

## Examples

- [Starter Projects](https://github.com/master-co/css/tree/main/examples) [![GitHub stars](https://img.shields.io/github/stars/master-co/css/tree/main/examples?style=flat)](https://github.com/master-co/css/tree/main/examples/stargazers) - Minimal setups for Angular, Astro, Laravel, Lit, Next.js, Nuxt, React, Svelte, Vite, Webpack, the CDN and more.

## Articles

- [Master CSS 2.0](https://master.co/blog/master-css-v2) - Expressive classes, CSS-defined tokens, and tools that understand your design system.
- [Master CSS with Next.js: When to Use Progressive Rendering](https://master.co/blog/master-css-next) - Pre-rendered HTML, later classes in the browser, and the boundary for dynamic SSR.
- [Master CSS with Vite: Choose When to Generate CSS](https://master.co/blog/bootstrapping-master-css-with-vite) - Follow one app through source scanning, emitted HTML and the connected DOM.

## Related Libraries

- [Styled](https://github.com/master-co/styled) [![GitHub stars](https://img.shields.io/github/stars/master-co/styled?style=flat)](https://github.com/master-co/styled/stargazers) - Create reusable styled elements in one line for React and Vue.

## Community

- [GitHub Discussions](https://github.com/master-co/css/discussions) - Ask questions, discuss ideas and share your work. English and Chinese are welcome.
- [GitHub Issues](https://github.com/master-co/css/issues) - Report reproducible bugs.
- [Discord](https://discord.com/invite/sZNKpAAAw6) - Chat with the community.
- [X](https://twitter.com/mastercorg) - News and announcements.

<p align="center">
  <br/>
  <br/>
  <br/>
  <sub>Contributions welcome! Read the <a href="./contributing.md">contribution guidelines</a> first.</sub>
</p>
