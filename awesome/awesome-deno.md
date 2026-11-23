# Deno

> 来源：[denolib/awesome-deno](https://github.com/denolib/awesome-deno)

[![GitHub stars](https://img.shields.io/github/stars/denolib/awesome-deno?style=flat)](https://github.com/denolib/awesome-deno/stargazers)

# Awesome Deno [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="deno-logo.png" align="right" width="100">](https://deno.land)

Deno is a simple, modern and secure runtime for JavaScript and TypeScript that uses V8 and is built in Rust.

This list is a collection of the best Deno modules and resources.

## Contents

- [Docs](#docs)
  - [Official Docs](#official-docs)
  - [External Docs](#external-docs)
- [Modules](#modules)
  - [Automation](#automation)
  - [CLI utils](#cli-utils)
  - [Cloud APIs](#cloud-apis)
  - [Database](#database)
  - [Editor framework](#editor-framework)
  - [Frontend framework](#frontend-framework)
  - [Game engine](#game-engine)
  - [Logging](#logging)
  - [Mail](#mail)
  - [Markdown](#markdown)
  - [Static site generator](#static-site-generator)
  - [Social Platform APIs](#social-platform-apis)
  - [Template engine](#template-engine)
  - [Testing](#testing)
  - [Utils](#utils)
  - [Web framework](#web-framework)
  - [Web utils](#web-utils)
  - [Webview](#webview)
- [Registries](#registries)
- [Showcases](#showcases)
- [Tools](#tools)
- [Integrations](#integrations)
- [Articles](#articles)
- [Blogs/Newsletters](#blogsnewsletters)
- [Presentations](#presentations)
- [Resources](#resources)
  - [Books](#books)
- [Resources in Other Languages](#resources-in-other-languages)
  - [Chinese](#chinese)
  - [Hebrew](#hebrew)
  - [Indonesian](#indonesian)
  - [Italian](#italian)
  - [Japanese](#japanese)
  - [Russian](#russian)
  - [Spanish](#spanish)
  - [Darija (Arabe marocain)](#darija)
  - [Kurdish (Central)](#kurdish-central)

## Docs

### Official Docs

- [Deno API Reference](https://docs.deno.com/api)
- [Deno Manual](https://docs.deno.com)
- [Deno Standard Library](https://jsr.io/@std)
- [Official Site](https://deno.com)

### External Docs

- [V8 Docs for Deno](https://denolib.github.io/v8-docs/)

## Modules

### Automation
- [zuke](https://github.com/zuke-build/zuke) [![GitHub stars](https://img.shields.io/github/stars/zuke-build/zuke?style=flat)](https://github.com/zuke-build/zuke/stargazers) - Code-first, strongly-typed build automation system where builds are defined as TypeScript classes.

### CLI utils
- [cac](https://github.com/cacjs/cac) [![GitHub stars](https://img.shields.io/github/stars/cacjs/cac?style=flat)](https://github.com/cacjs/cac/stargazers) - Simple yet powerful framework for building command-line apps.
- [cli-spinner](https://github.com/ameerthehacker/deno-cli-spinners) [![GitHub stars](https://img.shields.io/github/stars/ameerthehacker/deno-cli-spinners?style=flat)](https://github.com/ameerthehacker/deno-cli-spinners/stargazers) - Show spinners in the terminal while running long tasks.
- [cliffy](https://github.com/c4spar/cliffy) [![GitHub stars](https://img.shields.io/github/stars/c4spar/cliffy?style=flat)](https://github.com/c4spar/cliffy/stargazers) - The complete solution for building interactive command-line tools.
- [clinfer](https://github.com/jersou/clinfer) [![GitHub stars](https://img.shields.io/github/stars/jersou/clinfer?style=flat)](https://github.com/jersou/clinfer/stargazers) - Automatically generate CLIs from JS objects, classes or ES modules.
- [commit-sage-cli](https://github.com/AhmedOsman101/commit-sage-cli) [![GitHub stars](https://img.shields.io/github/stars/AhmedOsman101/commit-sage-cli?style=flat)](https://github.com/AhmedOsman101/commit-sage-cli/stargazers) - Generates Conventional Commit messages with AI based on Git repository changes.
- [yargs](https://github.com/yargs/yargs) [![GitHub stars](https://img.shields.io/github/stars/yargs/yargs?style=flat)](https://github.com/yargs/yargs/stargazers) - The modern, pirate-themed successor to optimist.

### Cloud APIs
- [aws-api](https://aws-api.danopia.deno.net/) - From-scratch Typescript AWS API client built for Deno.
- [sigflint](https://github.com/bompus/sigflint) [![GitHub stars](https://img.shields.io/github/stars/bompus/sigflint?style=flat)](https://github.com/bompus/sigflint/stargazers) - AWS Signature Version 4 and SigV4a request signing with no dependencies, for use with `fetch`.

### Database
- [@iuioiua/redis](https://jsr.io/@iuioiua/redis) - Fast, lightweight Redis client built upon the Web Streams API.
- [deno_mongo](https://github.com/denodrivers/mongo) [![GitHub stars](https://img.shields.io/github/stars/denodrivers/mongo?style=flat)](https://github.com/denodrivers/mongo/stargazers) - MongoDB database driver.
- [kvdock](https://github.com/zisam-glitch/kvdock) [![GitHub stars](https://img.shields.io/github/stars/zisam-glitch/kvdock?style=flat)](https://github.com/zisam-glitch/kvdock/stargazers) - Zero-dependency key-value and multi-tier caching engine with native Deno KV support and single-flight stampede protection.
- [maxminddb](https://github.com/josh-hemphill/maxminddb-wasm) [![GitHub stars](https://img.shields.io/github/stars/josh-hemphill/maxminddb-wasm?style=flat)](https://github.com/josh-hemphill/maxminddb-wasm/stargazers) - A library that enables the usage of MaxmindDB geoIP database files
- [nessie](https://github.com/lmxrd/deno-nessie) [![GitHub stars](https://img.shields.io/github/stars/lmxrd/deno-nessie?style=flat)](https://github.com/lmxrd/deno-nessie/stargazers) - Create, migrate and rollback migrations for PostgreSQL, MySQL and SQLite.
- [postgres](https://github.com/denodrivers/postgres) [![GitHub stars](https://img.shields.io/github/stars/denodrivers/postgres?style=flat)](https://github.com/denodrivers/postgres/stargazers) - Driver for PostgreSQL database.
- [redis](https://github.com/denodrivers/redis) [![GitHub stars](https://img.shields.io/github/stars/denodrivers/redis?style=flat)](https://github.com/denodrivers/redis/stargazers) - An experimental implementation of redis client for deno.

### Editor framework

- [Denops](https://github.com/vim-denops/denops.vim) [![GitHub stars](https://img.shields.io/github/stars/vim-denops/denops.vim?style=flat)](https://github.com/vim-denops/denops.vim/stargazers) - 🐜 An ecosystem to write Vim/Neovim plugins with Deno.

### Frontend framework
- [fresh](https://github.com/freshframework/fresh) [![GitHub stars](https://img.shields.io/github/stars/freshframework/fresh?style=flat)](https://github.com/freshframework/fresh/stargazers) - The next-gen web framework.

### Game engine
- [caviar](https://github.com/load1n9/caviar) [![GitHub stars](https://img.shields.io/github/stars/load1n9/caviar?style=flat)](https://github.com/load1n9/caviar/stargazers) - ⚡ Blazing fast, modern, Game Engine powered by WebGPU for Deno and the browser
- [sdl2](https://github.com/littledivy/deno_sdl2) [![GitHub stars](https://img.shields.io/github/stars/littledivy/deno_sdl2?style=flat)](https://github.com/littledivy/deno_sdl2/stargazers) - SDL2 module for Deno

### Image
- [aigifmaker](https://github.com/hanshs474/aigifmaker-ts) [![GitHub stars](https://img.shields.io/github/stars/hanshs474/aigifmaker-ts?style=flat)](https://github.com/hanshs474/aigifmaker-ts/stargazers) - Turn text prompts into animated GIFs with the AI GIF Maker API.
- [ImageScript](https://github.com/imagescript/ImageScript) [![GitHub stars](https://img.shields.io/github/stars/imagescript/ImageScript?style=flat)](https://github.com/imagescript/ImageScript/stargazers) - Image processing in JavaScript, utilizing WebAssembly for performance.
- [kavel](https://github.com/hanshs474/kavel-ts) [![GitHub stars](https://img.shields.io/github/stars/hanshs474/kavel-ts?style=flat)](https://github.com/hanshs474/kavel-ts/stargazers) - Generate and edit images with AI without an API key or account.

### Logging
- [LogTape](https://github.com/dahlia/logtape) [![GitHub stars](https://img.shields.io/github/stars/dahlia/logtape?style=flat)](https://github.com/dahlia/logtape/stargazers) - Simple logging library with zero dependencies for Deno/Node.js/Bun/browsers.

### Mail
- [dmarc-rua](https://github.com/domaincanary/dmarc-rua) [![GitHub stars](https://img.shields.io/github/stars/domaincanary/dmarc-rua?style=flat)](https://github.com/domaincanary/dmarc-rua/stargazers) - Parse DMARC aggregate reports from XML, gzip, zip and report emails.

### Markdown
- [LiteMarkup](https://github.com/tuures/LiteMarkup) [![GitHub stars](https://img.shields.io/github/stars/tuures/LiteMarkup?style=flat)](https://github.com/tuures/LiteMarkup/stargazers) - AST-first parser. Under 3 KB gzipped, zero dependencies.

### Static site generator
- [lume](https://github.com/lumeland/lume) [![GitHub stars](https://img.shields.io/github/stars/lumeland/lume?style=flat)](https://github.com/lumeland/lume/stargazers) - A static site generator similar to Jekyll or Eleventy with support for multiple file formats.
- [zerho](https://github.com/glastor-core/zerho) [![GitHub stars](https://img.shields.io/github/stars/glastor-core/zerho?style=flat)](https://github.com/glastor-core/zerho/stargazers) - High-performance documentation engine for Deno 2 and Edge runtimes with interactive playground, OpenAPI explorer, and native llms.txt support.

### Social Platform APIs
- [Circe](https://github.com/sxnnyside-project/circe) [![GitHub stars](https://img.shields.io/github/stars/sxnnyside-project/circe?style=flat)](https://github.com/sxnnyside-project/circe/stargazers) - Inversion-of-control framework for discord.js bots with file-system routing, guards and Gateway or HTTP transport.
- [discordeno](https://github.com/discordeno/discordeno) [![GitHub stars](https://img.shields.io/github/stars/discordeno/discordeno?style=flat)](https://github.com/discordeno/discordeno/stargazers) - Discord API library for Deno
- [grammY](https://github.com/grammyjs/grammY) [![GitHub stars](https://img.shields.io/github/stars/grammyjs/grammY?style=flat)](https://github.com/grammyjs/grammY/stargazers) - Telegram Bot API framework for Deno.
- [MTKruto](https://github.com/MTKruto/MTKruto) [![GitHub stars](https://img.shields.io/github/stars/MTKruto/MTKruto?style=flat)](https://github.com/MTKruto/MTKruto/stargazers) - Deno-first, cross-runtime client library for Telegram's MTProto API.


### Template engine
- [eta](https://github.com/bgub/eta) [![GitHub stars](https://img.shields.io/github/stars/bgub/eta?style=flat)](https://github.com/bgub/eta/stargazers) - Fast, lightweight, and configurable embedded template engine.

### Testing
- [keploy](https://github.com/keploy/keploy) [![GitHub stars](https://img.shields.io/github/stars/keploy/keploy?style=flat)](https://github.com/keploy/keploy/stargazers) - Record real traffic to generate integration tests and mock Postgres, Redis, and fetch calls.
- [qunitx](https://github.com/izelnakri/qunitx) [![GitHub stars](https://img.shields.io/github/stars/izelnakri/qunitx?style=flat)](https://github.com/izelnakri/qunitx/stargazers) - Zero dependency, fully customizable, mature, universal test API that can run interchangably in node.js, Deno & browser, using default runtime test runners.
- [superdeno](https://github.com/cmorten/superdeno) [![GitHub stars](https://img.shields.io/github/stars/cmorten/superdeno?style=flat)](https://github.com/cmorten/superdeno/stargazers) - Super-agent driven library for testing Deno HTTP servers.
- [tepi](https://github.com/jupegarnica/tepi) [![GitHub stars](https://img.shields.io/github/stars/jupegarnica/tepi?style=flat)](https://github.com/jupegarnica/tepi/stargazers) - A .http Test Runner
- [unexpected](https://github.com/unexpectedjs/unexpected) [![GitHub stars](https://img.shields.io/github/stars/unexpectedjs/unexpected?style=flat)](https://github.com/unexpectedjs/unexpected/stargazers) - Extensible BDD assertion toolkit.

### Utils
- [computed_types](https://github.com/neuledge/computed-types) [![GitHub stars](https://img.shields.io/github/stars/neuledge/computed-types?style=flat)](https://github.com/neuledge/computed-types/stargazers) - Joi like validators for Typescript and Deno.
- [croner](https://github.com/Hexagon/croner) [![GitHub stars](https://img.shields.io/github/stars/Hexagon/croner?style=flat)](https://github.com/Hexagon/croner/stargazers) - Cron library with advanced scheduling features, well-documented API, and zero dependencies.
- [csv-pipe](https://github.com/martsinlabs/csv-pipe) [![GitHub stars](https://img.shields.io/github/stars/martsinlabs/csv-pipe?style=flat)](https://github.com/martsinlabs/csv-pipe/stargazers) - Typed, zero-dependency CSV parser and encoder for every runtime.
- [deno_kv_fs](https://github.com/hviana/deno_kv_fs) [![GitHub stars](https://img.shields.io/github/stars/hviana/deno_kv_fs?style=flat)](https://github.com/hviana/deno_kv_fs/stargazers) Deno KV file system, compatible with Deno deploy. Makes use of Web Streams API.
- [durationjs](https://github.com/retraigo/duration.js) [![GitHub stars](https://img.shields.io/github/stars/retraigo/duration.js?style=flat)](https://github.com/retraigo/duration.js/stargazers) - Get formatted time duration from a timestamp or a human-readable string.
- [envapt](https://github.com/materwelonDhruv/envapt) [![GitHub stars](https://img.shields.io/github/stars/materwelonDhruv/envapt?style=flat)](https://github.com/materwelonDhruv/envapt/stargazers) - Read environment variables as typed values with built-in converters, Standard Schema validation, and zero dependencies.
- [esm-itter](https://github.com/tillsanders/esm-itter) [![GitHub stars](https://img.shields.io/github/stars/tillsanders/esm-itter?style=flat)](https://github.com/tillsanders/esm-itter/stargazers) – A strongly typed fork of the popular EventEmitter3 with a focus on EcmaScript module syntax, TypeScript and modern tooling.
- [evt](https://github.com/garronej/evt) [![GitHub stars](https://img.shields.io/github/stars/garronej/evt?style=flat)](https://github.com/garronej/evt/stargazers) - Type safe replacement for EventEmitter.
- [fastest-validator](https://github.com/icebob/fastest-validator) [![GitHub stars](https://img.shields.io/github/stars/icebob/fastest-validator?style=flat)](https://github.com/icebob/fastest-validator/stargazers) - Schema validator for all javascript platforms
- [fortuna](https://github.com/retraigo/fortuna) [![GitHub stars](https://img.shields.io/github/stars/retraigo/fortuna?style=flat)](https://github.com/retraigo/fortuna/stargazers) - Weighted gacha system.
- [injecute](https://github.com/Masyaka/injecute) [![GitHub stars](https://img.shields.io/github/stars/Masyaka/injecute?style=flat)](https://github.com/Masyaka/injecute/stargazers) - Type-safe dependency injection container with explicit wiring and no decorators.
- [json-schema-for-llms](https://github.com/carmenaresearch/json-schema-for-llms) [![GitHub stars](https://img.shields.io/github/stars/carmenaresearch/json-schema-for-llms?style=flat)](https://github.com/carmenaresearch/json-schema-for-llms/stargazers) - Turn a JSON document too large for an LLM context window into a short JSON Schema with counts, ranges and example records.
- [optionals](https://github.com/OliverBrotchie/optionals) [![GitHub stars](https://img.shields.io/github/stars/OliverBrotchie/optionals?style=flat)](https://github.com/OliverBrotchie/optionals/stargazers) - Rust-like error handling and options with exhaustive pattern matching.
- [PLS](https://github.com/xorgram/pls) [![GitHub stars](https://img.shields.io/github/stars/xorgram/pls?style=flat)](https://github.com/xorgram/pls/stargazers) - Use 2 lines to persist localStorage in any database, including, but not limited to, MongoDB, PostgreSQL and Redis.
- [qrcode](https://github.com/denorg/qrcode) [![GitHub stars](https://img.shields.io/github/stars/denorg/qrcode?style=flat)](https://github.com/denorg/qrcode/stargazers) - QR code image generator for Deno.
- [rubico](https://github.com/a-synchronous/rubico) [![GitHub stars](https://img.shields.io/github/stars/a-synchronous/rubico?style=flat)](https://github.com/a-synchronous/rubico/stargazers) - 🏞 [a]synchronous function composition; it just works.
- [solc](https://github.com/deno-web3/solc) [![GitHub stars](https://img.shields.io/github/stars/deno-web3/solc?style=flat)](https://github.com/deno-web3/solc/stargazers) - 💎 Solidity bindings for Deno.
- [switcher4deno](https://github.com/switcherapi/switcher-client-deno) [![GitHub stars](https://img.shields.io/github/stars/switcherapi/switcher-client-deno?style=flat)](https://github.com/switcherapi/switcher-client-deno/stargazers) - Feature Flag Deno SDK client for Switcher-API.
- [wu-diff-js](https://github.com/bokuweb/wu-diff-js) [![GitHub stars](https://img.shields.io/github/stars/bokuweb/wu-diff-js?style=flat)](https://github.com/bokuweb/wu-diff-js/stargazers) - A diff library to compute differences between two slices using wu(the O(NP)) algorithm.

### Validation

- [is-kit](https://github.com/necoz-oss/is-kit) [![GitHub stars](https://img.shields.io/github/stars/necoz-oss/is-kit?style=flat)](https://github.com/necoz-oss/is-kit/stargazers) - Build small, composable type guards with natural TypeScript narrowing and zero dependencies.
- [zod](https://github.com/colinhacks/zod) [![GitHub stars](https://img.shields.io/github/stars/colinhacks/zod?style=flat)](https://github.com/colinhacks/zod/stargazers) - TypeScript-first schema validation with static type inference.

### Web framework
- [alosaur](https://github.com/alosaur/alosaur) [![GitHub stars](https://img.shields.io/github/stars/alosaur/alosaur?style=flat)](https://github.com/alosaur/alosaur/stargazers) - Alosaur - Deno web framework with many ES Decorators.
- [danet](https://github.com/Savory/Danet) [![GitHub stars](https://img.shields.io/github/stars/Savory/Danet?style=flat)](https://github.com/Savory/Danet/stargazers) - A Savory web framework for Deno heavily inspired by [Nest.js](https://nestjs.com).
- [drash](https://github.com/drashland/drash) [![GitHub stars](https://img.shields.io/github/stars/drashland/drash?style=flat)](https://github.com/drashland/drash/stargazers) - A REST microframework for Deno's HTTP server with zero dependencies.
- [faster](https://github.com/hviana/faster) [![GitHub stars](https://img.shields.io/github/stars/hviana/faster?style=flat)](https://github.com/hviana/faster/stargazers) - A fast and optimized middleware server with a set of useful middlwares.
- [faster_react](https://github.com/hviana/faster_react) [![GitHub stars](https://img.shields.io/github/stars/hviana/faster_react?style=flat)](https://github.com/hviana/faster_react/stargazers) - Full Stack web framework with React + Faster. Fully compatible with Deno Deploy.
- [hono](https://github.com/honojs/hono) [![GitHub stars](https://img.shields.io/github/stars/honojs/hono?style=flat)](https://github.com/honojs/hono/stargazers) - Ultrafast web framework for Cloudflare Workers, Deno, and Bun. Fast, but not only fast.
- [orpc](https://github.com/middleapi/orpc) [![GitHub stars](https://img.shields.io/github/stars/middleapi/orpc?style=flat)](https://github.com/middleapi/orpc/stargazers) - End-to-end typesafe APIs with RPC and OpenAPI support, without code generation.

### Web utils
- [forwarded](https://github.com/deno-libs/forwarded) [![GitHub stars](https://img.shields.io/github/stars/deno-libs/forwarded?style=flat)](https://github.com/deno-libs/forwarded/stargazers) - Deno port of `forwarded` library.
- [gql](https://github.com/deno-libs/gql) [![GitHub stars](https://img.shields.io/github/stars/deno-libs/gql?style=flat)](https://github.com/deno-libs/gql/stargazers) - Universal GraphQL HTTP middleware.
- [graphql-tag](https://github.com/deno-libs/graphql_tag) [![GitHub stars](https://img.shields.io/github/stars/deno-libs/graphql_tag?style=flat)](https://github.com/deno-libs/graphql_tag/stargazers) - GraphQL schema AST from template literal.
- [linkpeek](https://github.com/thegruber/linkpeek) [![GitHub stars](https://img.shields.io/github/stars/thegruber/linkpeek?style=flat)](https://github.com/thegruber/linkpeek/stargazers) - Extract Open Graph, Twitter Card and JSON-LD link-preview metadata from a URL.
- [rpc](https://github.com/deno-libs/rpc) [![GitHub stars](https://img.shields.io/github/stars/deno-libs/rpc?style=flat)](https://github.com/deno-libs/rpc/stargazers) - JSONRPC server implementation for Deno.

### Webview
- [webview](https://github.com/webview/webview_deno) [![GitHub stars](https://img.shields.io/github/stars/webview/webview_deno?style=flat)](https://github.com/webview/webview_deno/stargazers) - Deno bindings for webview, a tiny library for creating web-based desktop GUIs.

## Registries

- [deno.land/x/](https://deno.land/x/) - The official 3rd party module registry.

## Showcases

- [Chobble Tickets](https://github.com/chobbledotcom/tickets) [![GitHub stars](https://img.shields.io/github/stars/chobbledotcom/tickets?style=flat)](https://github.com/chobbledotcom/tickets/stargazers) - Open source ticket sales system with encrypted attendee data and Stripe, Square, or SumUp payments.
- [Deno Rest](https://github.com/Prolifode/deno_rest) [![GitHub stars](https://img.shields.io/github/stars/Prolifode/deno_rest?style=flat)](https://github.com/Prolifode/deno_rest/stargazers) - A Boilerplate for deno RESTful apis.
- [GitHub Profile Trophy](https://github.com/ryo-ma/github-profile-trophy) [![GitHub stars](https://img.shields.io/github/stars/ryo-ma/github-profile-trophy?style=flat)](https://github.com/ryo-ma/github-profile-trophy/stargazers) - 🏆 Add dynamically generated GitHub Trophy on your readme
- [globnotes](https://github.com/alexindigo/globnotes) [![GitHub stars](https://img.shields.io/github/stars/alexindigo/globnotes?style=flat)](https://github.com/alexindigo/globnotes/stargazers) - Self-hosted Markdown note-taking app for Obsidian vaults and nested folders, with full-text search and sandboxed plugins.
- [Medusa Edge API Gateway](https://github.com/glastor-core/medusa) [![GitHub stars](https://img.shields.io/github/stars/glastor-core/medusa?style=flat)](https://github.com/glastor-core/medusa/stargazers) - Resilient Edge API Gateway and caching proxy on Deno Deploy with circuit breaker, single-flight deduplication, and Deno KV.
- [ShopSavvy Deno Deploy](https://github.com/shopsavvy/deno-deploy-shopsavvy) [![GitHub stars](https://img.shields.io/github/stars/shopsavvy/deno-deploy-shopsavvy?style=flat)](https://github.com/shopsavvy/deno-deploy-shopsavvy/stargazers) - Deno Deploy router with Hono for product search, real-time pricing, and price history.
- [The Official Showcase](https://deno.com/showcase) - The official showcase of Deno.

## Tools

- [bare-devcontainer/templates](https://github.com/bare-devcontainer/templates/tree/main/src/deno) [![GitHub stars](https://img.shields.io/github/stars/bare-devcontainer/templates/tree/main/src/deno?style=flat)](https://github.com/bare-devcontainer/templates/tree/main/src/deno/stargazers) - Security-focused Deno dev container for JS/TS with hardened defaults and cached modules. The base image is available at [bare-devcontainer/images](https://github.com/bare-devcontainer/images/tree/main/src/deno) [![GitHub stars](https://img.shields.io/github/stars/bare-devcontainer/images/tree/main/src/deno?style=flat)](https://github.com/bare-devcontainer/images/tree/main/src/deno/stargazers).
- [clone](https://github.com/ekaragodin/clone) [![GitHub stars](https://img.shields.io/github/stars/ekaragodin/clone?style=flat)](https://github.com/ekaragodin/clone/stargazers) - A simple utility for the convenient clone.
- [CompatLab](https://github.com/siddiksawani/CompatLab) [![GitHub stars](https://img.shields.io/github/stars/siddiksawani/CompatLab?style=flat)](https://github.com/siddiksawani/CompatLab/stargazers) - Check npm package loading across pinned Deno, Node.js and Bun versions with shareable reports.
- [copilotz](https://github.com/copilotzhq/copilotz) [![GitHub stars](https://img.shields.io/github/stars/copilotzhq/copilotz?style=flat)](https://github.com/copilotzhq/copilotz/stargazers) - TypeScript runtime for apps used by people, the app's own agents and AI assistants over MCP, with one set of Actions, access rules and audit record for every caller.
- [denoify](https://github.com/garronej/denoify) [![GitHub stars](https://img.shields.io/github/stars/garronej/denoify?style=flat)](https://github.com/garronej/denoify/stargazers) - For NPM module authors that would like to support Deno but do not want to write and maintain a port.
- [denoliver](https://github.com/joakimunge/denoliver) [![GitHub stars](https://img.shields.io/github/stars/joakimunge/denoliver?style=flat)](https://github.com/joakimunge/denoliver/stargazers) - A simple, dependency free file server with live reload.
- [denomander](https://github.com/siokas/denomander) [![GitHub stars](https://img.shields.io/github/stars/siokas/denomander?style=flat)](https://github.com/siokas/denomander/stargazers) - Deno command-line interfaces inspired from commander.js.
- [denopkg](https://github.com/egoist-labs/denopkg.com) [![GitHub stars](https://img.shields.io/github/stars/egoist-labs/denopkg.com?style=flat)](https://github.com/egoist-labs/denopkg.com/stargazers) - An easier way to use code from GitHub in your Deno project.
- [deno_docker](https://github.com/denoland/deno_docker) [![GitHub stars](https://img.shields.io/github/stars/denoland/deno_docker?style=flat)](https://github.com/denoland/deno_docker/stargazers) - Latest dockerfiles and images for Deno - alpine, centos, debian, ubuntu.
- [dnt](https://github.com/denoland/dnt) [![GitHub stars](https://img.shields.io/github/stars/denoland/dnt?style=flat)](https://github.com/denoland/dnt/stargazers) - Deno to npm package build tool.
- dvm
  - [asdf-community/asdf-deno](https://github.com/asdf-community/asdf-deno) [![GitHub stars](https://img.shields.io/github/stars/asdf-community/asdf-deno?style=flat)](https://github.com/asdf-community/asdf-deno/stargazers) - Deno plugin for [asdf](https://asdf-vm.com/)
  - [justjavac/dvm](https://github.com/justjavac/dvm) [![GitHub stars](https://img.shields.io/github/stars/justjavac/dvm?style=flat)](https://github.com/justjavac/dvm/stargazers) - Deno Version Manager: manage multiple active Deno versions.
  - [ghosind/dvm](https://github.com/ghosind/dvm) [![GitHub stars](https://img.shields.io/github/stars/ghosind/dvm?style=flat)](https://github.com/ghosind/dvm/stargazers) - A lightweight Deno Version Manager for Linux/MacOS.
- [make-deno-edition](https://github.com/bevry/make-deno-edition) [![GitHub stars](https://img.shields.io/github/stars/bevry/make-deno-edition?style=flat)](https://github.com/bevry/make-deno-edition/stargazers) - Automatically makes package.json projects (such as npm packages and node.js modules) compatible with Deno.
- [nemesis](https://github.com/glastor-core/nemesis) [![GitHub stars](https://img.shields.io/github/stars/glastor-core/nemesis?style=flat)](https://github.com/glastor-core/nemesis/stargazers) - Automated DevSecOps auditing, repository hygiene, auto-fix, and compliance CLI built with Deno 2.
- [pup](https://github.com/Hexagon/pup) [![GitHub stars](https://img.shields.io/github/stars/Hexagon/pup?style=flat)](https://github.com/Hexagon/pup/stargazers) - Advanced process manager for Deno. With autorestart, fs watch, cron start, process telemetry, ipc, clustering, load balancer and more.
- [studio-pack-generator](https://github.com/jersou/studio-pack-generator) [![GitHub stars](https://img.shields.io/github/stars/jersou/studio-pack-generator?style=flat)](https://github.com/jersou/studio-pack-generator/stargazers) - Convert a folder or a RSS URL to Studio pack for Lunii device
- [vscode-deno](https://github.com/denoland/vscode_deno) [![GitHub stars](https://img.shields.io/github/stars/denoland/vscode_deno?style=flat)](https://github.com/denoland/vscode_deno/stargazers) - VS Code extension that provides Deno support using the `TypeScript Deno language service plugin`.

## Integrations

- [Netlify Edge Functions](https://docs.netlify.com/build/edge-functions/overview/) - Edge Functions connect the Netlify platform and workflow.
- [Slack Custom Functions](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-custom-functions/) - Build custom Run On Slack functions using Deno.
- [Smallweb](https://www.smallweb.run/) - A personal cloud contained in a single directory. You can customize the server behavior using Deno.
- [Supabase Edge Functions](https://supabase.com/docs/guides/functions) - Edge Functions are server-side TypeScript functions, distributed globally at the edge.
- [Astro](https://docs.astro.build/en/guides/deploy/deno/) - Deploy a server-side rendered Astro site to Deno Deploy.

## Blogs/Newsletters
- [Deno Blog](https://deno.com/blog) - The official blog of the Deno Company.
- [Deno News](https://deno.news) - A newsletter of Deno articles, news and cool projects.

## Articles

- [Develop with Deno and Visual Studio Code](https://medium.com/@kitsonk/develop-with-deno-and-visual-studio-code-225ce7c5b1ba)
- [First thoughts on Deno, the JavaScript/TypeScript run-time](https://43081j.com/2019/01/first-look-at-deno)
- [Getting started with Deno](https://dev.to/wuz/getting-started-with-deno-e1m)
- [What's Deno, and how is it different from Node.js?](https://dev.to/bnevilleoneill/what-s-deno-and-how-is-it-different-from-node-js-366g)
- [Write a small API using Deno](https://dev.to/kryz/write-a-small-api-using-deno-1cl0)
- [Deno on Cloud Run](https://medium.com/google-cloud/deno-on-cloud-run-89ae64d1664d)
- [Learn Deno: Chat app](https://aralroca.com/blog/learn-deno-chat-app)
- [From Node to Deno](https://dev.to/aralroca/from-node-to-deno-5gpn)
- [Create a simple Note-taking app with Deno](https://dev.to/jeferson_sb/create-a-simple-note-taking-app-with-deno-3k7g)
- [Building API's using Deno, Oak and MYSQL](https://codeforgeek.com/building-api-server-using-deno-and-mysql/)
- [Create your first News CLI app using Deno](https://medium.com/javascript-in-plain-english/creating-your-first-news-cli-app-using-deno-e1470398c627)
- [Continuous Integration with Deno](https://semaphoreci.com/blog/continuous-integration-with-deno)
- [The Hidden Superpower of Deno: xeval](https://stefanbuck.com/blog/hidden-superpower-deno-xeval)
- [Getting Started with Deno](https://sabe.io/tutorials/getting-started-with-deno)
- [How to deploy a Deno app using Docker](https://sabe.io/tutorials/how-to-deploy-deno-app-docker)

## Presentations

- [10 Things I Regret About Node.js - Ryan Dahl - JSConf EU 2018](https://www.youtube.com/watch?v=M3BM9TB-8yA)
  - [Slides](https://tinyclouds.org/jsconf2018.pdf)
- [JSDC 2018#A01 - Deno, A New Server-Side Runtime By Ryan Dahl](https://www.youtube.com/watch?v=FlTG0UXRAkE)
- [Ryan Dahl. Deno, a new way to JavaScript. JS Fest 2019 Spring](https://www.youtube.com/watch?v=z6JRlx5NC9E)
  - [Slides](https://www.slideshare.net/JSFestUA/js-fest-2019-ryan-dahl-deno-a-new-way-to-javascript)
- [Rafał Pocztarski — From Node.js to Deno - JavaScript/TypeScript runtime built with V8 and Rust [EN]](https://www.youtube.com/watch?v=Aib1OZLy0_c)
- [Ryan Dahl: A secure runtime for JavaScript and TypeScript | js.la April 2019](https://www.youtube.com/watch?v=RAmqgbv247s)
  - [Slides](https://docs.google.com/presentation/d/1CSQVTeH5tFzE4AZVXIpx9Xwew5YS-gxJZ03eRFtNeIc/edit)
- [Ryan Dahl: Deno, a new way to JavaScript - HolyJS 2019 Piter](https://www.youtube.com/watch?v=HjdJzNoT_qg)
  - [Slides](https://docs.google.com/presentation/d/1BjvZx5S8noVfFINptH4jfKfqh9jB9nXlFC0I3oIDtg4/edit)
- [Rafał Pocztarski - What is Deno? A new runtime for modern JavaScript and TypeScript backends for 2020s - Deno Warsaw](https://www.youtube.com/watch?v=aI5A9zvYSjk)
- [Michał Sabiniarz - How to contribute to Deno? - Deno Warsaw](https://www.youtube.com/watch?v=LAtjnKLbPpw)
- [Bartek Iwańczuk - Deno internals, how modern runtime is built - Deno Warsaw](https://www.youtube.com/watch?v=qt7fbmypAFk)
  - [Slides](https://docs.google.com/presentation/d/1LYNGpyjx9PemL-P__7hVC8mSqkX-jL8VQLMhCRehy00/edit?usp=sharing)
- [Ryan Dahl & Kitson Kelly: Deno is a New Way to JavaScript - TSConf 2019](https://www.youtube.com/watch?v=1gIiZfSbEAE)
- [Bert Belder - Deno - dotJS 2019](https://www.youtube.com/watch?v=puXyo1jGQys)
- [Kitson P. Kelly - Deno, and The Future of JavaScript Runtimes - CityJS Conf 2020](https://www.youtube.com/watch?v=2eRyZpX4qvI)
- [Matías Insaurralde - Deno: an experimental approach on V8 interoperability [EN subtitles] - NodeConf Argentina 2019](https://www.youtube.com/watch?v=N0BRE-0n2cU)
  - [Slides](https://speakerdeck.com/matiasinsaurralde/deno-an-experimental-approach-on-v8-interoperability)

## Resources

### Books
- [Modern Web Development with Deno](https://bpbonline.com/products/modern-web-development-with-deno)

## Resources in Other Languages

### Chinese

- [Deno 并不是下一代 Node.js](https://juejin.im/post/5b14a390e51d4506c1300bbc)
- [玩 Deno 遇到问题的解决方案](https://juejin.im/post/5b1245b3f265da6e4c6cf249)
- [让我们一起来学习别人学不动的 Deno](https://segmentfault.com/a/1190000015151287)
- [Design Mistakes in Node zh-CN](https://zhuanlan.zhihu.com/p/37637923)
- [Node之父ry：Node中的设计错误](https://mp.weixin.qq.com/s/7XAiYw18c8YZc-fXk0-wrw)
- [Node之父 - Deno，一个新的JS运行时](https://www.bilibili.com/video/av52038617)

### Hebrew

- [Deno intro in Hebrew (slides in English)](https://www.youtube.com/watch?v=9tJ_LkI6_qw)

### Indonesian

- [Berkenalan dengan Deno](https://medium.com/@redhajuanda/berkenalan-dengan-dengan-deno-c48cdf3aa31e)
- [Perkenalan Deno dan Instalasi](https://youtu.be/V_kpUTJSd9c)
- [Deno Land Indonesia Telegram group](https://t.me/deno_id)

### Italian

- [Deno - L'anagramma di Node](https://www.slideshare.net/FrancescoSciuti/deno-lanagramma-di-node)

### Japanese

- [Node.js における設計ミス By Ryan Dahl](https://yosuke-furukawa.hatenablog.com/entry/2018/06/07/080335)
- [mizchi/deno_code_reading.md](https://gist.github.com/mizchi/31e5628751330b624a0e8ada9e739b1e)
- [Design Mistakes in Node & Deno #kng5 / deno](https://speakerdeck.com/masashi/deno)
- [Dive into Deno：プロセス起動からTypeScriptが実行されるまで](https://blog.leko.jp/post/code-reading-of-deno-boot-process/)

### Russian

- [Telegram channel](https://t.me/denoland_ru)
- [Telegram chat](https://t.me/denoland)

### Spanish

- [Hola Deno! . 🦕](https://medium.com/javascript-espa%C3%B1ol/hola-deno-f31f9f6f2c84)
- [Así puedes crear tu primera API REST con Deno](https://medium.com/@mpampols/as%C3%AD-puedes-crear-tu-primera-api-rest-con-deno-a9094ee5c0b2)
- [Primeros pasos con Deno 🦕 El sucesor de NodeJS desarrollado con Rust y TypeScript](https://medium.com/@manurua/primeros-pasos-con-deno-el-nuevo-nodejs-desarrollado-con-rust-y-typescript-b9ac14f7d0c7)
- [Primer vistazo con deno](https://dev.to/buttercubz/first-look-with-deno-spanish-30dh)

### Darija

- [A first look at Deno | BlaBlaConf 2021 🇲🇦](https://www.youtube.com/watch?v=Y_etUvzAa4s)

### Kurdish (Central)

- [A short introduction to Deno](https://devs.krd/about-deno)
