# Go

[![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go?style=flat)](https://github.com/avelino/awesome-go/stargazers)

# Awesome Go

<a href="https://awesome-go.com/"><img align="right" src="https://github.com/avelino/awesome-go/raw/main/tmpl/assets/logo.png" alt="awesome-go" title="awesome-go" /></a>

[![Build Status](https://github.com/avelino/awesome-go/actions/workflows/tests.yaml/badge.svg?branch=main) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go/actions/workflows/tests.yaml/badge.svg?branch=main?style=flat)](https://github.com/avelino/awesome-go/actions/workflows/tests.yaml/badge.svg?branch=main/stargazers)](https://github.com/avelino/awesome-go/actions/workflows/tests.yaml?query=branch%3Amain)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Slack Widget](https://img.shields.io/badge/join-us%20on%20slack-gray.svg?longCache=true&logo=slack&colorB=red)](https://gophers.slack.com/messages/awesome)
[![Netlify Status](https://api.netlify.com/api/v1/badges/83a6dcbe-0da6-433e-b586-f68109286bd5/deploy-status)](https://app.netlify.com/sites/awesome-go/deploys)
[![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/avelino/awesome-go/)
[![Last Commit](https://img.shields.io/github/last-commit/avelino/awesome-go)](https://github.com/avelino/awesome-go/commits/main)

We use the _[Golang Bridge](https://github.com/gobridge/about-us/blob/master/README.md) [![GitHub stars](https://img.shields.io/github/stars/gobridge/about-us/blob/master/README.md?style=flat)](https://github.com/gobridge/about-us/blob/master/README.md/stargazers)_ community Slack for instant communication, follow the [form here to join](https://invite.slack.golangbridge.org/).

<a href="https://www.producthunt.com/posts/awesome-go?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-awesome-go" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=291535&theme=light" alt="awesome-go - Curated list awesome Go frameworks, libraries and software | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

**Sponsorships:**

_Special thanks to_

<div align="center">
<table cellpadding="5">
<tbody align="center">
<tr>
<td colspan="2">
<a href="https://bit.ly/awesome-go-digitalocean">
<img src="https://avelino.run/sponsors/do_logo_horizontal_blue-210.png" width="200" alt="Digital Ocean">
</a>
</td>
</tr>
</tbody>
</table>
</div>

**Awesome Go has no monthly fee**_, but we have employees who **work hard** to keep it running. With money raised, we can repay the effort of each person involved! You can see how we calculate our billing and distribution as it is open to the entire community. Want to be a supporter of the project click [here](mailto:avelinorun+oss@gmail.com?subject=awesome-go%3A%20project%20support)._

> A curated list of awesome Go frameworks, libraries, and software. Inspired by [awesome-python](https://github.com/vinta/awesome-python) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers).

**Contributing:**

Please take a quick gander at the [contribution guidelines](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go/blob/main/CONTRIBUTING.md?style=flat)](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md/stargazers) first. Thanks to all [contributors](https://github.com/avelino/awesome-go/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go/graphs/contributors?style=flat)](https://github.com/avelino/awesome-go/graphs/contributors/stargazers); you rock!

> _If you see a package or project here that is no longer maintained or is not a good fit, please submit a pull request to improve this file. Thank you!_

## Contents

<details>
<summary>Expand contents</summary>

- [Awesome Go](#awesome-go)
  - [Contents](#contents)
  - [Actor Model](#actor-model)
  - [Artificial Intelligence](#artificial-intelligence)
  - [Audio and Music](#audio-and-music)
  - [Authentication and Authorization](#authentication-and-authorization)
  - [Blockchain](#blockchain)
  - [Bot Building](#bot-building)
  - [Build Automation](#build-automation)
  - [Command Line](#command-line)
    - [Advanced Console UIs](#advanced-console-uis)
    - [Standard CLI](#standard-cli)
  - [Configuration](#configuration)
  - [Continuous Integration](#continuous-integration)
  - [CSS Preprocessors](#css-preprocessors)
  - [Data Integration Frameworks](#data-integration-frameworks)
  - [Data Structures and Algorithms](#data-structures-and-algorithms)
    - [Bit-packing and Compression](#bit-packing-and-compression)
    - [Bit Sets](#bit-sets)
    - [Bloom and Cuckoo Filters](#bloom-and-cuckoo-filters)
    - [Data Structure and Algorithm Collections](#data-structure-and-algorithm-collections)
    - [Iterators](#iterators)
    - [Maps](#maps)
    - [Miscellaneous Data Structures and Algorithms](#miscellaneous-data-structures-and-algorithms)
    - [Nullable Types](#nullable-types)
    - [Queues](#queues)
    - [Sets](#sets)
    - [Text Analysis](#text-analysis)
    - [Trees](#trees)
    - [Pipes](#pipes)
  - [Database](#database)
    - [Caches](#caches)
    - [Databases Implemented in Go](#databases-implemented-in-go)
    - [Database Schema Migration](#database-schema-migration)
    - [Database Tools](#database-tools)
    - [SQL Query Builders](#sql-query-builders)
  - [Database Drivers](#database-drivers)
    - [Interfaces to Multiple Backends](#interfaces-to-multiple-backends)
    - [Relational Database Drivers](#relational-database-drivers)
    - [NoSQL Database Drivers](#nosql-database-drivers)
    - [Search and Analytic Databases](#search-and-analytic-databases)
  - [Date and Time](#date-and-time)
  - [Distributed Systems](#distributed-systems)
  - [Dynamic DNS](#dynamic-dns)
  - [Email](#email)
  - [Embeddable Scripting Languages](#embeddable-scripting-languages)
  - [Error Handling](#error-handling)
  - [File Handling](#file-handling)
  - [Financial](#financial)
  - [Forms](#forms)
  - [Functional](#functional)
  - [Game Development](#game-development)
  - [Generators](#generators)
  - [Geographic](#geographic)
  - [Go Compilers](#go-compilers)
  - [Goroutines](#goroutines)
  - [GUI](#gui)
  - [Hardware](#hardware)
  - [Images](#images)
  - [IoT (Internet of Things)](#iot-internet-of-things)
  - [Job Scheduler](#job-scheduler)
  - [JSON](#json)
  - [Logging](#logging)
  - [Machine Learning](#machine-learning)
  - [Messaging](#messaging)
  - [Microsoft Office](#microsoft-office)
    - [Microsoft Excel](#microsoft-excel)
    - [Microsoft Word](#microsoft-word)
  - [Miscellaneous](#miscellaneous)
    - [Dependency Injection](#dependency-injection)
    - [Project Layout](#project-layout)
    - [Strings](#strings)
    - [Uncategorized](#uncategorized)
  - [Natural Language Processing](#natural-language-processing)
    - [Language Detection](#language-detection)
    - [Morphological Analyzers](#morphological-analyzers)
    - [Slugifiers](#slugifiers)
    - [Tokenizers](#tokenizers)
    - [Translation](#translation)
    - [Transliteration](#transliteration)
  - [Networking](#networking)
    - [HTTP Clients](#http-clients)
  - [OpenGL](#opengl)
  - [ORM](#orm)
  - [Package Management](#package-management)
  - [Performance](#performance)
  - [Query Language](#query-language)
  - [Reflection](#reflection)
  - [Resource Embedding](#resource-embedding)
  - [Science and Data Analysis](#science-and-data-analysis)
  - [Security](#security)
  - [Serialization](#serialization)
  - [Server Applications](#server-applications)
  - [Stream Processing](#stream-processing)
  - [Template Engines](#template-engines)
  - [Testing](#testing)
    - [Testing Frameworks](#testing-frameworks)
    - [Mock](#mock)
    - [Fuzzing and delta-debugging/reducing/shrinking](#fuzzing-and-delta-debuggingreducingshrinking)
    - [Selenium and browser control tools](#selenium-and-browser-control-tools)
    - [Fail injection](#fail-injection)
  - [Text Processing](#text-processing)
    - [Formatters](#formatters)
    - [Markup Languages](#markup-languages)
    - [Parsers/Encoders/Decoders](#parsersencodersdecoders)
    - [Regular Expressions](#regular-expressions)
    - [Sanitation](#sanitation)
    - [Scrapers](#scrapers)
    - [RSS](#rss)
    - [Utility/Miscellaneous](#utilitymiscellaneous)
  - [Third-party APIs](#third-party-apis)
  - [Utilities](#utilities)
  - [UUID](#uuid)
  - [Validation](#validation)
  - [Version Control](#version-control)
  - [Video](#video)
  - [Web Frameworks](#web-frameworks)
    - [Middlewares](#middlewares)
      - [Actual middlewares](#actual-middlewares)
      - [Libraries for creating HTTP middlewares](#libraries-for-creating-http-middlewares)
    - [Routers](#routers)
  - [WebAssembly](#webassembly)
  - [Webhooks Server](#webhooks-server)
  - [Windows](#windows)
  - [Workflow Frameworks](#workflow-frameworks)
  - [XML](#xml)
  - [Zero Trust](#zero-trust)
  - [Code Analysis](#code-analysis)
  - [Editor Plugins](#editor-plugins)
  - [Go Generate Tools](#go-generate-tools)
  - [Go Tools](#go-tools)
  - [Software Packages](#software-packages)
    - [DevOps Tools](#devops-tools)
    - [Other Software](#other-software)
- [Resources](#resources)
  - [Benchmarks](#benchmarks)
  - [Conferences](#conferences)
  - [E-Books](#e-books)
    - [E-books for purchase](#e-books-for-purchase)
    - [Free e-books](#free-e-books)
  - [Gophers](#gophers)
  - [Meetups](#meetups)
  - [Style Guides](#style-guides)
  - [Social Media](#social-media)
    - [Twitter](#twitter)
    - [Reddit](#reddit)
  - [Websites](#websites)
    - [Tutorials](#tutorials)
    - [Guided Learning](#guided-learning)
  - [Contribution](#contribution)
  - [License](#license)

**[⬆ back to top](#contents)**



</details>

## Actor Model

_Libraries for building actor-based programs._

- [asyncmachine-go/pkg/machine](https://github.com/pancsta/asyncmachine-go/tree/main/pkg/machine) [![GitHub stars](https://img.shields.io/github/stars/pancsta/asyncmachine-go/tree/main/pkg/machine?style=flat)](https://github.com/pancsta/asyncmachine-go/tree/main/pkg/machine/stargazers) - Graph control flow library (AOP, actor, state-machine).
- [Ergo](https://github.com/ergo-services/ergo) [![GitHub stars](https://img.shields.io/github/stars/ergo-services/ergo?style=flat)](https://github.com/ergo-services/ergo/stargazers) - An actor-based Framework with network transparency for creating event-driven architecture in Golang. Inspired by Erlang.
- [Goakt](https://github.com/Tochemey/goakt) [![GitHub stars](https://img.shields.io/github/stars/Tochemey/goakt?style=flat)](https://github.com/Tochemey/goakt/stargazers) - Fast and Distributed Actor framework using protocol buffers as message for Golang.
- [Hollywood](https://github.com/anthdm/hollywood) [![GitHub stars](https://img.shields.io/github/stars/anthdm/hollywood?style=flat)](https://github.com/anthdm/hollywood/stargazers) - Blazingly fast and light-weight Actor engine written in Golang.
- [ProtoActor](https://github.com/asynkron/protoactor-go) [![GitHub stars](https://img.shields.io/github/stars/asynkron/protoactor-go?style=flat)](https://github.com/asynkron/protoactor-go/stargazers) - Distributed actors for Go, C#, and Java/Kotlin.

**[⬆ back to top](#contents)**

## Artificial Intelligence

_Libraries for building programs that leverage AI._

- [AegisFlow](https://github.com/saivedant169/AegisFlow) [![GitHub stars](https://img.shields.io/github/stars/saivedant169/AegisFlow?style=flat)](https://github.com/saivedant169/AegisFlow/stargazers) - AI gateway for routing, securing, and monitoring LLM traffic across 10+ providers. OpenAI-compatible API, WASM policy plugins, canary rollouts, real-time dashboard.
- [Aetheris](https://github.com/Colin4k1024/Aetheris) [![GitHub stars](https://img.shields.io/github/stars/Colin4k1024/Aetheris?style=flat)](https://github.com/Colin4k1024/Aetheris/stargazers) - AI Agent execution runtime with event sourcing, checkpoint recovery, and At-Most-Once execution guarantee. Written in Go.
- [agent-sdk-go](https://github.com/agenticenv/agent-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/agenticenv/agent-sdk-go?style=flat)](https://github.com/agenticenv/agent-sdk-go/stargazers) - Go SDK for building durable AI agents on Temporal with support for tools, MCP, human approvals, and sub-agent delegation.
- [ai](https://github.com/joakimcarlsson/ai) [![GitHub stars](https://img.shields.io/github/stars/joakimcarlsson/ai?style=flat)](https://github.com/joakimcarlsson/ai/stargazers) - A Go toolkit for building AI agents and applications across multiple providers with unified LLM, embeddings, tool calling, and MCP integration.
- [chromem-go](https://github.com/philippgille/chromem-go) [![GitHub stars](https://img.shields.io/github/stars/philippgille/chromem-go?style=flat)](https://github.com/philippgille/chromem-go/stargazers) - Embeddable vector database for Go with Chroma-like interface and zero third-party dependencies. In-memory with optional persistence.
- [dakera-go](https://github.com/dakera-ai/dakera-go) [![GitHub stars](https://img.shields.io/github/stars/dakera-ai/dakera-go?style=flat)](https://github.com/dakera-ai/dakera-go/stargazers) - Official Go client SDK for the Dakera self-hosted agent memory server, providing typed interfaces for memory store/recall, session management, namespace operations, and decay configuration.
- [fun](https://gitlab.com/tozd/go/fun) - The simplest but powerful way to use large language models (LLMs) in Go.
- [goai](https://github.com/zendev-sh/goai) [![GitHub stars](https://img.shields.io/github/stars/zendev-sh/goai?style=flat)](https://github.com/zendev-sh/goai/stargazers) - Go SDK for building AI applications. One SDK, 20+ providers. Inspired by Vercel AI SDK.
- [hotplex](https://github.com/hrygo/hotplex) [![GitHub stars](https://img.shields.io/github/stars/hrygo/hotplex?style=flat)](https://github.com/hrygo/hotplex/stargazers) - AI Agent runtime engine with long-lived sessions for Claude Code, OpenCode, pi-mono and other CLI AI tools. Provides full-duplex streaming, multi-platform integrations, and secure sandbox.
- [langchaingo](https://github.com/tmc/langchaingo) [![GitHub stars](https://img.shields.io/github/stars/tmc/langchaingo?style=flat)](https://github.com/tmc/langchaingo/stargazers) - LangChainGo is a framework for developing applications powered by language models.
- [langgraphgo](https://github.com/smallnest/langgraphgo) [![GitHub stars](https://img.shields.io/github/stars/smallnest/langgraphgo?style=flat)](https://github.com/smallnest/langgraphgo/stargazers) - A Go library for building stateful, multi-actor applications with LLMs, built on the concept of LangGraph，with a lot of builtin Agent architectures.
- [LocalAI](https://github.com/mudler/LocalAI) [![GitHub stars](https://img.shields.io/github/stars/mudler/LocalAI?style=flat)](https://github.com/mudler/LocalAI/stargazers) - Open Source OpenAI alternative, self-host AI models.
- [localaik](https://github.com/harshaneel/localaik) [![GitHub stars](https://img.shields.io/github/stars/harshaneel/localaik?style=flat)](https://github.com/harshaneel/localaik/stargazers) - LocalStack-style local emulation of OpenAI and Gemini APIs; single Docker container, llama.cpp + Gemma 3 backend.
- [mcp-go](https://github.com/mark3labs/mcp-go) [![GitHub stars](https://img.shields.io/github/stars/mark3labs/mcp-go?style=flat)](https://github.com/mark3labs/mcp-go/stargazers) - Go implementation of the Model Context Protocol for building MCP servers and clients in Go.
- [Ollama](https://github.com/jmorganca/ollama) [![GitHub stars](https://img.shields.io/github/stars/jmorganca/ollama?style=flat)](https://github.com/jmorganca/ollama/stargazers) - Run large language models locally.
- [OllamaFarm](https://github.com/presbrey/ollamafarm) [![GitHub stars](https://img.shields.io/github/stars/presbrey/ollamafarm?style=flat)](https://github.com/presbrey/ollamafarm/stargazers) - Manage, load-balance, and failover packs of Ollamas.
- [otellix](https://github.com/oluwajubelo1/otellix) [![GitHub stars](https://img.shields.io/github/stars/oluwajubelo1/otellix?style=flat)](https://github.com/oluwajubelo1/otellix/stargazers) - OpenTelemetry-native LLM observability and budget guardrails for cost-constrained production environments.
- [routex](https://github.com/Ad3bay0c/routex) [![GitHub stars](https://img.shields.io/github/stars/Ad3bay0c/routex?style=flat)](https://github.com/Ad3bay0c/routex/stargazers) - YAML-driven multi-agent AI runtime for Go with Erlang-style supervision, MCP tool server support, and a CLI.
- [trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) [![GitHub stars](https://img.shields.io/github/stars/trpc-group/trpc-agent-go?style=flat)](https://github.com/trpc-group/trpc-agent-go/stargazers) - Framework for building LLM-based multi-agent systems.
- [web-researcher-mcp](https://github.com/zoharbabin/web-researcher-mcp) [![GitHub stars](https://img.shields.io/github/stars/zoharbabin/web-researcher-mcp?style=flat)](https://github.com/zoharbabin/web-researcher-mcp/stargazers) - MCP server providing AI assistants with web search, content extraction, and multi-source research capabilities. Single binary, 5 search providers with circuit-breaker failover, 4-tier scraping pipeline.
- [zenflow](https://github.com/zendev-sh/zenflow) [![GitHub stars](https://img.shields.io/github/stars/zendev-sh/zenflow?style=flat)](https://github.com/zendev-sh/zenflow/stargazers) - Multi-agent orchestration & workflow engine. Declarative YAML workflows, LLM coordinator with hub-and-spoke mailboxes, race-safe delivery. One YAML file, one Go binary. Runs on any goai-supported provider.

**[⬆ back to top](#contents)**

## Audio and Music

_Libraries for manipulating audio and music._

- [beep](https://github.com/gopxl/beep) [![GitHub stars](https://img.shields.io/github/stars/gopxl/beep?style=flat)](https://github.com/gopxl/beep/stargazers) - A simple library for playback and audio manipulation.
- [flac](https://github.com/mewkiz/flac) [![GitHub stars](https://img.shields.io/github/stars/mewkiz/flac?style=flat)](https://github.com/mewkiz/flac/stargazers) - Native Go FLAC encoder/decoder with support for FLAC streams.
- [gaad](https://github.com/Comcast/gaad) [![GitHub stars](https://img.shields.io/github/stars/Comcast/gaad?style=flat)](https://github.com/Comcast/gaad/stargazers) - Native Go AAC bitstream parser.
- [go-mpris](https://github.com/leberKleber/go-mpris) [![GitHub stars](https://img.shields.io/github/stars/leberKleber/go-mpris?style=flat)](https://github.com/leberKleber/go-mpris/stargazers) - Client for mpris dbus interfaces.
- [GoAudio](https://github.com/DylanMeeus/GoAudio) [![GitHub stars](https://img.shields.io/github/stars/DylanMeeus/GoAudio?style=flat)](https://github.com/DylanMeeus/GoAudio/stargazers) - Native Go Audio Processing Library.
- [gosamplerate](https://github.com/dh1tw/gosamplerate) [![GitHub stars](https://img.shields.io/github/stars/dh1tw/gosamplerate?style=flat)](https://github.com/dh1tw/gosamplerate/stargazers) - libsamplerate bindings for go.
- [id3v2](https://github.com/bogem/id3v2) [![GitHub stars](https://img.shields.io/github/stars/bogem/id3v2?style=flat)](https://github.com/bogem/id3v2/stargazers) - ID3 decoding and encoding library for Go.
- [malgo](https://github.com/gen2brain/malgo) [![GitHub stars](https://img.shields.io/github/stars/gen2brain/malgo?style=flat)](https://github.com/gen2brain/malgo/stargazers) - Mini audio library.
- [minimp3](https://github.com/tosone/minimp3) [![GitHub stars](https://img.shields.io/github/stars/tosone/minimp3?style=flat)](https://github.com/tosone/minimp3/stargazers) - Lightweight MP3 decoder library.
- [music-theory](https://github.com/go-music-theory/music-theory) [![GitHub stars](https://img.shields.io/github/stars/go-music-theory/music-theory?style=flat)](https://github.com/go-music-theory/music-theory/stargazers) - Music theory models in Go.
- [Oto](https://github.com/hajimehoshi/oto) [![GitHub stars](https://img.shields.io/github/stars/hajimehoshi/oto?style=flat)](https://github.com/hajimehoshi/oto/stargazers) - A low-level library to play sound on multiple platforms.
- [PortAudio](https://github.com/gordonklaus/portaudio) [![GitHub stars](https://img.shields.io/github/stars/gordonklaus/portaudio?style=flat)](https://github.com/gordonklaus/portaudio/stargazers) - Go bindings for the PortAudio audio I/O library.
-[voxrai-ai](https://github.com/Voxray-AI/Voxray) [![GitHub stars](https://img.shields.io/github/stars/Voxray-AI/Voxray?style=flat)](https://github.com/Voxray-AI/Voxray/stargazers) - AI voice agents with a JSON configuration,  STT → LLM → TTS pipelines over WebSocket and WebRTC 

**[⬆ back to top](#contents)**

## Authentication and Authorization

_Libraries for implementing authentication and authorization._

- [authboss](https://github.com/volatiletech/authboss) [![GitHub stars](https://img.shields.io/github/stars/volatiletech/authboss?style=flat)](https://github.com/volatiletech/authboss/stargazers) - Modular authentication system for the web. It tries to remove as much boilerplate and "hard things" as possible so that each time you start a new web project in Go, you can plug it in, configure it, and start building your app without having to build an authentication system each time.
- [authgate](https://github.com/go-authgate/authgate) [![GitHub stars](https://img.shields.io/github/stars/go-authgate/authgate?style=flat)](https://github.com/go-authgate/authgate/stargazers) - A lightweight OAuth 2.0 Authorization Server supporting Device Authorization Grant ([RFC 8628](https://datatracker.ietf.org/doc/html/rfc8628)), Authorization Code Flow with PKCE ([RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) + [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)), and Client Credentials Grant for machine-to-machine authentication.
- [branca](https://github.com/essentialkaos/branca) [![GitHub stars](https://img.shields.io/github/stars/essentialkaos/branca?style=flat)](https://github.com/essentialkaos/branca/stargazers) - branca token [specification implementation](https://github.com/tuupola/branca-spec) [![GitHub stars](https://img.shields.io/github/stars/tuupola/branca-spec?style=flat)](https://github.com/tuupola/branca-spec/stargazers) for Golang 1.15+.
- [casbin](https://github.com/hsluoyz/casbin) [![GitHub stars](https://img.shields.io/github/stars/hsluoyz/casbin?style=flat)](https://github.com/hsluoyz/casbin/stargazers) - Authorization library that supports access control models like ACL, RBAC, and ABAC.
- [cookiestxt](https://github.com/mengzhuo/cookiestxt) [![GitHub stars](https://img.shields.io/github/stars/mengzhuo/cookiestxt?style=flat)](https://github.com/mengzhuo/cookiestxt/stargazers) - provides a parser of cookies.txt file format.
- [go-githubauth](https://github.com/jferrl/go-githubauth) [![GitHub stars](https://img.shields.io/github/stars/jferrl/go-githubauth?style=flat)](https://github.com/jferrl/go-githubauth/stargazers) - Utilities for GitHub authentication: generate and use GitHub application and installation tokens.
- [go-guardian](https://github.com/shaj13/go-guardian) [![GitHub stars](https://img.shields.io/github/stars/shaj13/go-guardian?style=flat)](https://github.com/shaj13/go-guardian/stargazers) - Go-Guardian is a golang library that provides a simple, clean, and idiomatic way to create powerful modern API and web authentication that supports LDAP, Basic, Bearer token, and Certificate based authentication.
- [go-iam](https://github.com/melvinodsa/go-iam) [![GitHub stars](https://img.shields.io/github/stars/melvinodsa/go-iam?style=flat)](https://github.com/melvinodsa/go-iam/stargazers) - Developer-first Identity and Access Management system with a simple UI.
- [go-jose](https://github.com/go-jose/go-jose) [![GitHub stars](https://img.shields.io/github/stars/go-jose/go-jose?style=flat)](https://github.com/go-jose/go-jose/stargazers) - Fairly complete implementation of the JOSE working group's JSON Web Token, JSON Web Signatures, and JSON Web Encryption specs.
- [go-jwt](https://github.com/deatil/go-jwt) [![GitHub stars](https://img.shields.io/github/stars/deatil/go-jwt?style=flat)](https://github.com/deatil/go-jwt/stargazers) - A JWT (JSON Web Token) library for Go.
- [go-jwt](https://github.com/pardnchiu/go-jwt) [![GitHub stars](https://img.shields.io/github/stars/pardnchiu/go-jwt?style=flat)](https://github.com/pardnchiu/go-jwt/stargazers) - JWT authentication package providing access tokens and refresh tokens with fingerprinting, Redis storage, and automatic refresh capabilities.
- [goiabada](https://github.com/leodip/goiabada) [![GitHub stars](https://img.shields.io/github/stars/leodip/goiabada?style=flat)](https://github.com/leodip/goiabada/stargazers) - An open-source authentication and authorization server supporting OAuth2 and OpenID Connect.
- [gologin](https://github.com/dghubble/gologin) [![GitHub stars](https://img.shields.io/github/stars/dghubble/gologin?style=flat)](https://github.com/dghubble/gologin/stargazers) - chainable handlers for login with OAuth1 and OAuth2 authentication providers.
- [gorbac](https://github.com/mikespook/gorbac) [![GitHub stars](https://img.shields.io/github/stars/mikespook/gorbac?style=flat)](https://github.com/mikespook/gorbac/stargazers) - provides a lightweight role-based access control (RBAC) implementation in Golang.
- [gosession](https://github.com/Kwynto/gosession) [![GitHub stars](https://img.shields.io/github/stars/Kwynto/gosession?style=flat)](https://github.com/Kwynto/gosession/stargazers) - This is quick session for net/http in GoLang. This package is perhaps the best implementation of the session mechanism, or at least it tries to become one.
- [goth](https://github.com/markbates/goth) [![GitHub stars](https://img.shields.io/github/stars/markbates/goth?style=flat)](https://github.com/markbates/goth/stargazers) - provides a simple, clean, and idiomatic way to use OAuth and OAuth2. Handles multiple providers out of the box.
- [jeff](https://github.com/abraithwaite/jeff) [![GitHub stars](https://img.shields.io/github/stars/abraithwaite/jeff?style=flat)](https://github.com/abraithwaite/jeff/stargazers) - Simple, flexible, secure, and idiomatic web session management with pluggable backends.
- [jwt](https://github.com/pascaldekloe/jwt) [![GitHub stars](https://img.shields.io/github/stars/pascaldekloe/jwt?style=flat)](https://github.com/pascaldekloe/jwt/stargazers) - Lightweight JSON Web Token (JWT) library.
- [jwt](https://github.com/cristalhq/jwt) [![GitHub stars](https://img.shields.io/github/stars/cristalhq/jwt?style=flat)](https://github.com/cristalhq/jwt/stargazers) - Safe, simple, and fast JSON Web Tokens for Go.
- [jwt-auth](https://github.com/adam-hanna/jwt-auth) [![GitHub stars](https://img.shields.io/github/stars/adam-hanna/jwt-auth?style=flat)](https://github.com/adam-hanna/jwt-auth/stargazers) - JWT middleware for Golang http servers with many configuration options.
- [jwt-go](https://github.com/golang-jwt/jwt) [![GitHub stars](https://img.shields.io/github/stars/golang-jwt/jwt?style=flat)](https://github.com/golang-jwt/jwt/stargazers) - A full featured implementation of JSON Web Tokens (JWT). This library supports the parsing and verification as well as the generation and signing of JWTs.
- [jwx](https://github.com/lestrrat-go/jwx) [![GitHub stars](https://img.shields.io/github/stars/lestrrat-go/jwx?style=flat)](https://github.com/lestrrat-go/jwx/stargazers) - Go module implementing various JWx (JWA/JWE/JWK/JWS/JWT, otherwise known as JOSE) technologies.
- [keto](https://github.com/ory/keto) [![GitHub stars](https://img.shields.io/github/stars/ory/keto?style=flat)](https://github.com/ory/keto/stargazers) - Open Source (Go) implementation of "Zanzibar: Google's Consistent, Global Authorization System". Ships gRPC, REST APIs, newSQL, and an easy and granular permission language. Supports ACL, RBAC, and other access models.
- [loginsrv](https://github.com/tarent/loginsrv) [![GitHub stars](https://img.shields.io/github/stars/tarent/loginsrv?style=flat)](https://github.com/tarent/loginsrv/stargazers) - JWT login microservice with pluggable backends such as OAuth2 (Github), htpasswd, osiam.
- [oauth2](https://github.com/golang/oauth2) [![GitHub stars](https://img.shields.io/github/stars/golang/oauth2?style=flat)](https://github.com/golang/oauth2/stargazers) - Successor of goauth2. Generic OAuth 2.0 package that comes with JWT, Google APIs, Compute Engine, and App Engine support.
- [oidc](https://github.com/zitadel/oidc) [![GitHub stars](https://img.shields.io/github/stars/zitadel/oidc?style=flat)](https://github.com/zitadel/oidc/stargazers) - Easy to use OpenID Connect client and server library written for Go and certified by the OpenID Foundation.
- [openfga](https://github.com/openfga/openfga) [![GitHub stars](https://img.shields.io/github/stars/openfga/openfga?style=flat)](https://github.com/openfga/openfga/stargazers) - Implementation of fine-grained authorization based on the "Zanzibar: Google's Consistent, Global Authorization System" paper. Backed by [CNCF](https://www.cncf.io/).
- [osin](https://github.com/openshift/osin) [![GitHub stars](https://img.shields.io/github/stars/openshift/osin?style=flat)](https://github.com/openshift/osin/stargazers) - Golang OAuth2 server library.
- [otpgen](https://github.com/grijul/otpgen) [![GitHub stars](https://img.shields.io/github/stars/grijul/otpgen?style=flat)](https://github.com/grijul/otpgen/stargazers) - Library to generate TOTP/HOTP codes.
- [otpgo](https://github.com/jltorresm/otpgo) [![GitHub stars](https://img.shields.io/github/stars/jltorresm/otpgo?style=flat)](https://github.com/jltorresm/otpgo/stargazers) - Time-Based One-Time Password (TOTP) and HMAC-Based One-Time Password (HOTP) library for Go.
- [paseto](https://github.com/o1egl/paseto) [![GitHub stars](https://img.shields.io/github/stars/o1egl/paseto?style=flat)](https://github.com/o1egl/paseto/stargazers) - Golang implementation of Platform-Agnostic Security Tokens (PASETO).
- [permissions](https://github.com/xyproto/permissions) [![GitHub stars](https://img.shields.io/github/stars/xyproto/permissions?style=flat)](https://github.com/xyproto/permissions/stargazers) - Library for keeping track of users, login states, and permissions. Uses secure cookies and bcrypt.
- [scope](https://github.com/SonicRoshan/scope) [![GitHub stars](https://img.shields.io/github/stars/SonicRoshan/scope?style=flat)](https://github.com/SonicRoshan/scope/stargazers) - Easily Manage OAuth2 Scopes In Go.
- [scs](https://github.com/alexedwards/scs) [![GitHub stars](https://img.shields.io/github/stars/alexedwards/scs?style=flat)](https://github.com/alexedwards/scs/stargazers) - Session Manager for HTTP servers.
- [securecookie](https://github.com/chmike/securecookie) [![GitHub stars](https://img.shields.io/github/stars/chmike/securecookie?style=flat)](https://github.com/chmike/securecookie/stargazers) - Efficient secure cookie encoding/decoding.
- [session](https://github.com/icza/session) [![GitHub stars](https://img.shields.io/github/stars/icza/session?style=flat)](https://github.com/icza/session/stargazers) - Go session management for web servers (including support for Google App Engine - GAE).
- [sessions](https://github.com/adam-hanna/sessions) [![GitHub stars](https://img.shields.io/github/stars/adam-hanna/sessions?style=flat)](https://github.com/adam-hanna/sessions/stargazers) - Dead simple, highly performant, highly customizable sessions service for go http servers.
- [sessionup](https://github.com/swithek/sessionup) [![GitHub stars](https://img.shields.io/github/stars/swithek/sessionup?style=flat)](https://github.com/swithek/sessionup/stargazers) - Simple, yet effective HTTP session management and identification package.
- [sjwt](https://github.com/brianvoe/sjwt) [![GitHub stars](https://img.shields.io/github/stars/brianvoe/sjwt?style=flat)](https://github.com/brianvoe/sjwt/stargazers) - Simple jwt generator and parser.
- [spicedb](https://github.com/authzed/spicedb) [![GitHub stars](https://img.shields.io/github/stars/authzed/spicedb?style=flat)](https://github.com/authzed/spicedb/stargazers) - A Zanzibar-inspired database that enables fine-grained authorization.
- [x509proxy](https://github.com/vkuznet/x509proxy) [![GitHub stars](https://img.shields.io/github/stars/vkuznet/x509proxy?style=flat)](https://github.com/vkuznet/x509proxy/stargazers) - Library to handle X509 proxy certificates.

**[⬆ back to top](#contents)**

## Blockchain

_Tools for building blockchains._

- [cometbft](https://github.com/cometbft/cometbft) [![GitHub stars](https://img.shields.io/github/stars/cometbft/cometbft?style=flat)](https://github.com/cometbft/cometbft/stargazers) - A distributed, Byzantine fault-tolerant, deterministic state machine replication engine. It is a fork of Tendermint Core and implements the Tendermint consensus algorithm.
- [cosmos-sdk](https://github.com/cosmos/cosmos-sdk) [![GitHub stars](https://img.shields.io/github/stars/cosmos/cosmos-sdk?style=flat)](https://github.com/cosmos/cosmos-sdk/stargazers) - A Framework for Building Public Blockchains in the Cosmos Ecosystem.
- [gno](https://github.com/gnolang/gno) [![GitHub stars](https://img.shields.io/github/stars/gnolang/gno?style=flat)](https://github.com/gnolang/gno/stargazers) - A comprehensive smart contract suite built with Golang and Gnolang, a deterministic, purpose-built Go variant for blockchains.
- [go-ethereum](https://github.com/ethereum/go-ethereum) [![GitHub stars](https://img.shields.io/github/stars/ethereum/go-ethereum?style=flat)](https://github.com/ethereum/go-ethereum/stargazers) - Official Go implementation of the Ethereum protocol.
- [gosemble](https://github.com/LimeChain/gosemble) [![GitHub stars](https://img.shields.io/github/stars/LimeChain/gosemble?style=flat)](https://github.com/LimeChain/gosemble/stargazers) - A Go-based framework for building Polkadot/Substrate-compatible runtimes.
- [gossamer](https://github.com/ChainSafe/gossamer) [![GitHub stars](https://img.shields.io/github/stars/ChainSafe/gossamer?style=flat)](https://github.com/ChainSafe/gossamer/stargazers) - A Go implementation of the Polkadot Host.
- [kubo](https://github.com/ipfs/kubo) [![GitHub stars](https://img.shields.io/github/stars/ipfs/kubo?style=flat)](https://github.com/ipfs/kubo/stargazers) - An IPFS implementation in Go. It provides content-addressable storage which can be used for decentralized storage in DApps. It is based on the IPFS protocol.
- [lnd](https://github.com/lightningnetwork/lnd) [![GitHub stars](https://img.shields.io/github/stars/lightningnetwork/lnd?style=flat)](https://github.com/lightningnetwork/lnd/stargazers) - A complete implementation of a Lightning Network node.
- [nview](https://github.com/blinklabs-io/nview) [![GitHub stars](https://img.shields.io/github/stars/blinklabs-io/nview?style=flat)](https://github.com/blinklabs-io/nview/stargazers) - Local monitoring tool for a Cardano Node. It's a TUI (terminal user interface) designed to fit most screens.
- [solana-go](https://github.com/gagliardetto/solana-go) [![GitHub stars](https://img.shields.io/github/stars/gagliardetto/solana-go?style=flat)](https://github.com/gagliardetto/solana-go/stargazers) - Go library to interface with Solana JSON RPC and WebSocket interfaces.
- [tendermint](https://github.com/tendermint/tendermint) [![GitHub stars](https://img.shields.io/github/stars/tendermint/tendermint?style=flat)](https://github.com/tendermint/tendermint/stargazers) - High-performance middleware for transforming a state machine written in any programming language into a Byzantine Fault Tolerant replicated state machine using the Tendermint consensus and blockchain protocols.
- [tronlib](https://github.com/kslamph/tronlib) [![GitHub stars](https://img.shields.io/github/stars/kslamph/tronlib?style=flat)](https://github.com/kslamph/tronlib/stargazers) - A comprehensive, production-ready Go SDK for interacting with the TRON blockchain with TRC20 token support.

**[⬆ back to top](#contents)**

## Bot Building

_Libraries for building and working with bots._

- [arikawa](https://github.com/diamondburned/arikawa) [![GitHub stars](https://img.shields.io/github/stars/diamondburned/arikawa?style=flat)](https://github.com/diamondburned/arikawa/stargazers) - A library and framework for the Discord API.
- [bot](https://github.com/go-telegram/bot) [![GitHub stars](https://img.shields.io/github/stars/go-telegram/bot?style=flat)](https://github.com/go-telegram/bot/stargazers) - Zero-dependencies Telegram Bot library with additional UI components.
- [echotron](https://github.com/NicoNex/echotron) [![GitHub stars](https://img.shields.io/github/stars/NicoNex/echotron?style=flat)](https://github.com/NicoNex/echotron/stargazers) - An elegant and concurrent library for Telegram Bots in Go.
- [go-joe](https://joe-bot.net) - A general-purpose bot library inspired by Hubot but written in Go.
- [go-sarah](https://github.com/oklahomer/go-sarah) [![GitHub stars](https://img.shields.io/github/stars/oklahomer/go-sarah?style=flat)](https://github.com/oklahomer/go-sarah/stargazers) - Framework to build a bot for desired chat services including LINE, Slack, Gitter, and more.
- [go-tg](https://github.com/mr-linch/go-tg) [![GitHub stars](https://img.shields.io/github/stars/mr-linch/go-tg?style=flat)](https://github.com/mr-linch/go-tg/stargazers) - Generated from official docs Go client library for accessing Telegram Bot API, with batteries for building complex bots included.
- [go-twitch-irc](https://github.com/gempir/go-twitch-irc) [![GitHub stars](https://img.shields.io/github/stars/gempir/go-twitch-irc?style=flat)](https://github.com/gempir/go-twitch-irc/stargazers) - Library to write bots for twitch.tv chat
- [micha](https://github.com/onrik/micha) [![GitHub stars](https://img.shields.io/github/stars/onrik/micha?style=flat)](https://github.com/onrik/micha/stargazers) - Go Library for Telegram bot api.
- [slack-bot](https://github.com/innogames/slack-bot) [![GitHub stars](https://img.shields.io/github/stars/innogames/slack-bot?style=flat)](https://github.com/innogames/slack-bot/stargazers) - Ready to use Slack Bot for lazy developers: Custom commands, Jenkins, Jira, Bitbucket, Github...
- [slacker](https://github.com/slack-io/slacker) [![GitHub stars](https://img.shields.io/github/stars/slack-io/slacker?style=flat)](https://github.com/slack-io/slacker/stargazers) - Easy to use framework to create Slack bots.
- [telebot](https://github.com/tucnak/telebot) [![GitHub stars](https://img.shields.io/github/stars/tucnak/telebot?style=flat)](https://github.com/tucnak/telebot/stargazers) - Telegram bot framework is written in Go.
- [telego](https://github.com/mymmrac/telego) [![GitHub stars](https://img.shields.io/github/stars/mymmrac/telego?style=flat)](https://github.com/mymmrac/telego/stargazers) - Telegram Bot API library for Golang with full one-to-one API implementation.
- [telegram-bot-api](https://github.com/go-telegram-bot-api/telegram-bot-api) [![GitHub stars](https://img.shields.io/github/stars/go-telegram-bot-api/telegram-bot-api?style=flat)](https://github.com/go-telegram-bot-api/telegram-bot-api/stargazers) - Simple and clean Telegram bot client.
- [TG](https://github.com/enetx/tg) [![GitHub stars](https://img.shields.io/github/stars/enetx/tg?style=flat)](https://github.com/enetx/tg/stargazers) - Telegram Bot Framework for Go.
- [wayback](https://github.com/wabarc/wayback) [![GitHub stars](https://img.shields.io/github/stars/wabarc/wayback?style=flat)](https://github.com/wabarc/wayback/stargazers) - A bot for Telegram, Mastodon, Slack, and other messaging platforms archives webpages.
- [ymsdk](https://github.com/rekurt/ymsdk) [![GitHub stars](https://img.shields.io/github/stars/rekurt/ymsdk?style=flat)](https://github.com/rekurt/ymsdk/stargazers) - Go SDK for Yandex Messenger Bot API with type-safe models, automatic retry, and rate-limit handling.
   - [Wisp](https://github.com/wisp-trading/wisp) [![GitHub stars](https://img.shields.io/github/stars/wisp-trading/wisp?style=flat)](https://github.com/wisp-trading/wisp/stargazers) - Event-driven trading framework for Go. Spot, perpetual futures, prediction markets. Multi-exchange (Bybit, Hyperliquid, Polymarket).

**[⬆ back to top](#contents)**

## Build Automation

_Libraries and tools help with build automation._

- [1build](https://github.com/gopinath-langote/1build) [![GitHub stars](https://img.shields.io/github/stars/gopinath-langote/1build?style=flat)](https://github.com/gopinath-langote/1build/stargazers) - Command line tool to frictionlessly manage project-specific commands.
- [air](https://github.com/cosmtrek/air) [![GitHub stars](https://img.shields.io/github/stars/cosmtrek/air?style=flat)](https://github.com/cosmtrek/air/stargazers) - Air - Live reload for Go apps.
- [anko](https://github.com/GuilhermeCaruso/anko) [![GitHub stars](https://img.shields.io/github/stars/GuilhermeCaruso/anko?style=flat)](https://github.com/GuilhermeCaruso/anko/stargazers) - Simple application watcher for multiple programming languages.
- [gaper](https://github.com/maxclaus/gaper) [![GitHub stars](https://img.shields.io/github/stars/maxclaus/gaper?style=flat)](https://github.com/maxclaus/gaper/stargazers) - Builds and restarts a Go project when it crashes or some watched file changes.
- [gilbert](https://go-gilbert.github.io) - Build system and task runner for Go projects.
- [gob](https://github.com/kcmvp/gob) [![GitHub stars](https://img.shields.io/github/stars/kcmvp/gob?style=flat)](https://github.com/kcmvp/gob/stargazers) - [Gradle](https://docs.gradle.org/)/[Maven](https://maven.apache.org/) like build tool for Go projects.
- [goyek](https://github.com/goyek/goyek) [![GitHub stars](https://img.shields.io/github/stars/goyek/goyek?style=flat)](https://github.com/goyek/goyek/stargazers) - Create build pipelines in Go.
- [mage](https://github.com/magefile/mage) [![GitHub stars](https://img.shields.io/github/stars/magefile/mage?style=flat)](https://github.com/magefile/mage/stargazers) - Mage is a make/rake-like build tool using Go.
- [mmake](https://github.com/tj/mmake) [![GitHub stars](https://img.shields.io/github/stars/tj/mmake?style=flat)](https://github.com/tj/mmake/stargazers) - Modern Make.
- [realize](https://github.com/tockins/realize) [![GitHub stars](https://img.shields.io/github/stars/tockins/realize?style=flat)](https://github.com/tockins/realize/stargazers) - Go build a system with file watchers and live to reload. Run, build and watch file changes with custom paths.
- [rex](https://github.com/rexrun-dev/rex) [![GitHub stars](https://img.shields.io/github/stars/rexrun-dev/rex?style=flat)](https://github.com/rexrun-dev/rex/stargazers) - Zero-config universal project runner. Detects your stack (Go, Node, Python, Rust, PHP, Zig, Elixir) and runs the right command.
- [Task](https://github.com/go-task/task) [![GitHub stars](https://img.shields.io/github/stars/go-task/task?style=flat)](https://github.com/go-task/task/stargazers) - simple "Make" alternative.
- [taskctl](https://github.com/taskctl/taskctl) [![GitHub stars](https://img.shields.io/github/stars/taskctl/taskctl?style=flat)](https://github.com/taskctl/taskctl/stargazers) - Concurrent task runner.
- [xc](https://github.com/joerdav/xc) [![GitHub stars](https://img.shields.io/github/stars/joerdav/xc?style=flat)](https://github.com/joerdav/xc/stargazers) - Task runner with README.md defined tasks, executable markdown.

**[⬆ back to top](#contents)**

## Command Line

### Advanced Console UIs

_Libraries for building Console Applications and Console User Interfaces._

- [asciigraph](https://github.com/guptarohit/asciigraph) [![GitHub stars](https://img.shields.io/github/stars/guptarohit/asciigraph?style=flat)](https://github.com/guptarohit/asciigraph/stargazers) - Go package to make lightweight ASCII line graph ╭┈╯ in command line apps with no other dependencies.
- [aurora](https://github.com/logrusorgru/aurora) [![GitHub stars](https://img.shields.io/github/stars/logrusorgru/aurora?style=flat)](https://github.com/logrusorgru/aurora/stargazers) - ANSI terminal colors that support fmt.Printf/Sprintf.
- [box-cli-maker](https://github.com/box-cli-maker/box-cli-maker) [![GitHub stars](https://img.shields.io/github/stars/box-cli-maker/box-cli-maker?style=flat)](https://github.com/box-cli-maker/box-cli-maker/stargazers) - Render highly customizable boxes in the terminal.
- [bubble-table](https://github.com/Evertras/bubble-table) [![GitHub stars](https://img.shields.io/github/stars/Evertras/bubble-table?style=flat)](https://github.com/Evertras/bubble-table/stargazers) - An interactive table component for bubbletea.
- [bubbles](https://github.com/charmbracelet/bubbles) [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/bubbles?style=flat)](https://github.com/charmbracelet/bubbles/stargazers) - TUI components for bubbletea.
- [bubbletea](https://github.com/charmbracelet/bubbletea) [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/bubbletea?style=flat)](https://github.com/charmbracelet/bubbletea/stargazers) - Go framework to build terminal apps, based on The Elm Architecture.
- [chroma16](https://github.com/arceus-7/chroma16) [![GitHub stars](https://img.shields.io/github/stars/arceus-7/chroma16?style=flat)](https://github.com/arceus-7/chroma16/stargazers) - Generate a harmonious 16-color terminal palette from a single seed color or string.
- [crab-config-files-templating](https://github.com/alfiankan/crab-config-files-templating) [![GitHub stars](https://img.shields.io/github/stars/alfiankan/crab-config-files-templating?style=flat)](https://github.com/alfiankan/crab-config-files-templating/stargazers) - Dynamic configuration file templating tool for kubernetes manifest or general configuration files.
- [ctc](https://github.com/wzshiming/ctc) [![GitHub stars](https://img.shields.io/github/stars/wzshiming/ctc?style=flat)](https://github.com/wzshiming/ctc/stargazers) - The non-invasive cross-platform terminal color library does not need to modify the Print method.
- [fx](https://github.com/antonmedv/fx) [![GitHub stars](https://img.shields.io/github/stars/antonmedv/fx?style=flat)](https://github.com/antonmedv/fx/stargazers) - Terminal JSON viewer & processor.
- [go-ataman](https://github.com/workanator/go-ataman) [![GitHub stars](https://img.shields.io/github/stars/workanator/go-ataman?style=flat)](https://github.com/workanator/go-ataman/stargazers) - Go library for rendering ANSI colored text templates in terminals.
- [go-colorable](https://github.com/mattn/go-colorable) [![GitHub stars](https://img.shields.io/github/stars/mattn/go-colorable?style=flat)](https://github.com/mattn/go-colorable/stargazers) - Colorable writer for windows.
- [go-colortext](https://github.com/daviddengcn/go-colortext) [![GitHub stars](https://img.shields.io/github/stars/daviddengcn/go-colortext?style=flat)](https://github.com/daviddengcn/go-colortext/stargazers) - Go library for color output in terminals.
- [go-isatty](https://github.com/mattn/go-isatty) [![GitHub stars](https://img.shields.io/github/stars/mattn/go-isatty?style=flat)](https://github.com/mattn/go-isatty/stargazers) - isatty for golang.
- [go-palette](https://github.com/abusomani/go-palette) [![GitHub stars](https://img.shields.io/github/stars/abusomani/go-palette?style=flat)](https://github.com/abusomani/go-palette/stargazers) - Go library that provides elegant and convenient style definitions using ANSI colors. Fully compatible & wraps the [fmt library](https://pkg.go.dev/fmt) for nice terminal layouts.
- [go-prompt](https://github.com/c-bata/go-prompt) [![GitHub stars](https://img.shields.io/github/stars/c-bata/go-prompt?style=flat)](https://github.com/c-bata/go-prompt/stargazers) - Library for building a powerful interactive prompt, inspired by [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) [![GitHub stars](https://img.shields.io/github/stars/jonathanslenders/python-prompt-toolkit?style=flat)](https://github.com/jonathanslenders/python-prompt-toolkit/stargazers).
- [go-tui](https://github.com/grindlemire/go-tui) [![GitHub stars](https://img.shields.io/github/stars/grindlemire/go-tui?style=flat)](https://github.com/grindlemire/go-tui/stargazers) - A declarative terminal UI framework with templ-like templates, flexbox layout, and a language server for editor support.
- [gocui](https://github.com/jroimartin/gocui) [![GitHub stars](https://img.shields.io/github/stars/jroimartin/gocui?style=flat)](https://github.com/jroimartin/gocui/stargazers) - Minimalist Go library aimed at creating Console User Interfaces.
- [gommon/color](https://github.com/labstack/gommon/tree/master/color) [![GitHub stars](https://img.shields.io/github/stars/labstack/gommon/tree/master/color?style=flat)](https://github.com/labstack/gommon/tree/master/color/stargazers) - Style terminal text.
- [gookit/color](https://github.com/gookit/color) [![GitHub stars](https://img.shields.io/github/stars/gookit/color?style=flat)](https://github.com/gookit/color/stargazers) - Terminal color rendering tool library, support 16 colors, 256 colors, RGB color rendering output, compatible with Windows.
- [goscaf](https://github.com/iyashjayesh/goscaf) [![GitHub stars](https://img.shields.io/github/stars/iyashjayesh/goscaf?style=flat)](https://github.com/iyashjayesh/goscaf/stargazers) - goscaf generates opinionated, production-quality Go project boilerplate via an interactive CLI. Stop copy-pasting skeleton code between projects.
- [lazyenv](https://github.com/lazynop/lazyenv) [![GitHub stars](https://img.shields.io/github/stars/lazynop/lazyenv?style=flat)](https://github.com/lazynop/lazyenv/stargazers) - TUI for browsing, comparing, and editing .env files.
- [lipgloss](https://github.com/charmbracelet/lipgloss) [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/lipgloss?style=flat)](https://github.com/charmbracelet/lipgloss/stargazers) - Declaratively define styles for color, format and layout in the terminal.
- [loom](https://github.com/loom-go/loom) [![GitHub stars](https://img.shields.io/github/stars/loom-go/loom?style=flat)](https://github.com/loom-go/loom/stargazers) - Signal-based reactive components framework for building TUIs.
- [marker](https://github.com/cyucelen/marker) [![GitHub stars](https://img.shields.io/github/stars/cyucelen/marker?style=flat)](https://github.com/cyucelen/marker/stargazers) - Easiest way to match and mark strings for colorful terminal outputs.
- [mpb](https://github.com/vbauerster/mpb) [![GitHub stars](https://img.shields.io/github/stars/vbauerster/mpb?style=flat)](https://github.com/vbauerster/mpb/stargazers) - Multi progress bar for terminal applications.
- [phoenix](https://github.com/phoenix-tui/phoenix) [![GitHub stars](https://img.shields.io/github/stars/phoenix-tui/phoenix?style=flat)](https://github.com/phoenix-tui/phoenix/stargazers) - High-performance TUI framework with Elm-inspired architecture, perfect Unicode rendering, and zero-allocation event system.
- [progressbar](https://github.com/schollz/progressbar) [![GitHub stars](https://img.shields.io/github/stars/schollz/progressbar?style=flat)](https://github.com/schollz/progressbar/stargazers) - Basic thread-safe progress bar that works in every OS.
- [pterm](https://github.com/pterm/pterm) [![GitHub stars](https://img.shields.io/github/stars/pterm/pterm?style=flat)](https://github.com/pterm/pterm/stargazers) - A library to beautify console output on every platform with many combinable components.
- [simpletable](https://github.com/alexeyco/simpletable) [![GitHub stars](https://img.shields.io/github/stars/alexeyco/simpletable?style=flat)](https://github.com/alexeyco/simpletable/stargazers) - Simple tables in a terminal with Go.
- [spinner](https://github.com/briandowns/spinner) [![GitHub stars](https://img.shields.io/github/stars/briandowns/spinner?style=flat)](https://github.com/briandowns/spinner/stargazers) - Go package to easily provide a terminal spinner with options.
- [tabby](https://github.com/cheynewallace/tabby) [![GitHub stars](https://img.shields.io/github/stars/cheynewallace/tabby?style=flat)](https://github.com/cheynewallace/tabby/stargazers) - A tiny library for super simple Golang tables.
- [table](https://github.com/tomlazar/table) [![GitHub stars](https://img.shields.io/github/stars/tomlazar/table?style=flat)](https://github.com/tomlazar/table/stargazers) - Small library for terminal color based tables.
- [termbox-go](https://github.com/nsf/termbox-go) [![GitHub stars](https://img.shields.io/github/stars/nsf/termbox-go?style=flat)](https://github.com/nsf/termbox-go/stargazers) - Termbox is a library for creating cross-platform text-based interfaces.
- [termdash](https://github.com/mum4k/termdash) [![GitHub stars](https://img.shields.io/github/stars/mum4k/termdash?style=flat)](https://github.com/mum4k/termdash/stargazers) - Go terminal dashboard based on **termbox-go** and inspired by [termui](https://github.com/gizak/termui) [![GitHub stars](https://img.shields.io/github/stars/gizak/termui?style=flat)](https://github.com/gizak/termui/stargazers).
- [termenv](https://github.com/muesli/termenv) [![GitHub stars](https://img.shields.io/github/stars/muesli/termenv?style=flat)](https://github.com/muesli/termenv/stargazers) - Advanced ANSI style & color support for your terminal applications.
- [termui](https://github.com/gizak/termui) [![GitHub stars](https://img.shields.io/github/stars/gizak/termui?style=flat)](https://github.com/gizak/termui/stargazers) - Go terminal dashboard based on **termbox-go** and inspired by [blessed-contrib](https://github.com/yaronn/blessed-contrib) [![GitHub stars](https://img.shields.io/github/stars/yaronn/blessed-contrib?style=flat)](https://github.com/yaronn/blessed-contrib/stargazers).
- [uilive](https://github.com/gosuri/uilive) [![GitHub stars](https://img.shields.io/github/stars/gosuri/uilive?style=flat)](https://github.com/gosuri/uilive/stargazers) - Library for updating terminal output in real time.
- [uiprogress](https://github.com/gosuri/uiprogress) [![GitHub stars](https://img.shields.io/github/stars/gosuri/uiprogress?style=flat)](https://github.com/gosuri/uiprogress/stargazers) - Flexible library to render progress bars in terminal applications.
- [uitable](https://github.com/gosuri/uitable) [![GitHub stars](https://img.shields.io/github/stars/gosuri/uitable?style=flat)](https://github.com/gosuri/uitable/stargazers) - Library to improve readability in terminal apps using tabular data.
- [vhs](https://github.com/charmbracelet/vhs) [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/vhs?style=flat)](https://github.com/charmbracelet/vhs/stargazers) - Your CLI home video recorder - generate terminal GIFs from code for documentation and tutorials.
- [yacspin](https://github.com/theckman/yacspin) [![GitHub stars](https://img.shields.io/github/stars/theckman/yacspin?style=flat)](https://github.com/theckman/yacspin/stargazers) - Yet Another CLi Spinner package, for working with terminal spinners.

**[⬆ back to top](#contents)**

### Standard CLI

_Libraries for building standard or basic Command Line applications._

- [acmd](https://github.com/cristalhq/acmd) [![GitHub stars](https://img.shields.io/github/stars/cristalhq/acmd?style=flat)](https://github.com/cristalhq/acmd/stargazers) - Simple, useful, and opinionated CLI package in Go.
- [argparse](https://github.com/akamensky/argparse) [![GitHub stars](https://img.shields.io/github/stars/akamensky/argparse?style=flat)](https://github.com/akamensky/argparse/stargazers) - Command line argument parser inspired by Python's argparse module.
- [argv](https://github.com/cosiner/argv) [![GitHub stars](https://img.shields.io/github/stars/cosiner/argv?style=flat)](https://github.com/cosiner/argv/stargazers) - Go library to split command line string as arguments array using the bash syntax.
- [boa](https://github.com/GiGurra/boa) [![GitHub stars](https://img.shields.io/github/stars/GiGurra/boa?style=flat)](https://github.com/GiGurra/boa/stargazers) - Declarative flags, env vars, validation, and config files from struct tags. Built on cobra.
- [carapace](https://github.com/rsteube/carapace) [![GitHub stars](https://img.shields.io/github/stars/rsteube/carapace?style=flat)](https://github.com/rsteube/carapace/stargazers) - Command argument completion generator for spf13/cobra.
- [carapace-bin](https://github.com/rsteube/carapace-bin) [![GitHub stars](https://img.shields.io/github/stars/rsteube/carapace-bin?style=flat)](https://github.com/rsteube/carapace-bin/stargazers) - Multi-shell multi-command argument completer.
- [carapace-spec](https://github.com/rsteube/carapace-spec) [![GitHub stars](https://img.shields.io/github/stars/rsteube/carapace-spec?style=flat)](https://github.com/rsteube/carapace-spec/stargazers) - Define simple completions using a spec file.
- [climax](https://github.com/tucnak/climax) [![GitHub stars](https://img.shields.io/github/stars/tucnak/climax?style=flat)](https://github.com/tucnak/climax/stargazers) - Alternative CLI with "human face", in spirit of Go command.
- [clîr](https://github.com/leaanthony/clir) [![GitHub stars](https://img.shields.io/github/stars/leaanthony/clir?style=flat)](https://github.com/leaanthony/clir/stargazers) - A Simple and Clear CLI library. Dependency free.
- [cmd](https://github.com/posener/cmd) [![GitHub stars](https://img.shields.io/github/stars/posener/cmd?style=flat)](https://github.com/posener/cmd/stargazers) - Extends the standard `flag` package to support sub commands and more in idiomatic way.
- [cmdr](https://github.com/hedzr/cmdr) [![GitHub stars](https://img.shields.io/github/stars/hedzr/cmdr?style=flat)](https://github.com/hedzr/cmdr/stargazers) - A POSIX/GNU style, getopt-like command-line UI Go library.
- [cobra](https://github.com/spf13/cobra) [![GitHub stars](https://img.shields.io/github/stars/spf13/cobra?style=flat)](https://github.com/spf13/cobra/stargazers) - Commander for modern Go CLI interactions.
- [command-chain](https://github.com/rainu/go-command-chain) [![GitHub stars](https://img.shields.io/github/stars/rainu/go-command-chain?style=flat)](https://github.com/rainu/go-command-chain/stargazers) - A go library for configure and run command chains - such as pipelining in unix shells.
- [commandeer](https://github.com/jaffee/commandeer) [![GitHub stars](https://img.shields.io/github/stars/jaffee/commandeer?style=flat)](https://github.com/jaffee/commandeer/stargazers) - Dev-friendly CLI apps: sets up flags, defaults, and usage based on struct fields and tags.
- [complete](https://github.com/posener/complete) [![GitHub stars](https://img.shields.io/github/stars/posener/complete?style=flat)](https://github.com/posener/complete/stargazers) - Write bash completions in Go + Go command bash completion.
- [console](https://github.com/reeflective/console) [![GitHub stars](https://img.shields.io/github/stars/reeflective/console?style=flat)](https://github.com/reeflective/console/stargazers) Closed-loop application library for Cobra commands, with oh-my-posh prompts, and more.
- [Dnote](https://github.com/dnote/dnote) [![GitHub stars](https://img.shields.io/github/stars/dnote/dnote?style=flat)](https://github.com/dnote/dnote/stargazers) - A simple command line notebook with multi-device sync.
- [elvish](https://github.com/elves/elvish) [![GitHub stars](https://img.shields.io/github/stars/elves/elvish?style=flat)](https://github.com/elves/elvish/stargazers) - An expressive programming language and a versatile interactive shell.
- [env](https://github.com/codingconcepts/env) [![GitHub stars](https://img.shields.io/github/stars/codingconcepts/env?style=flat)](https://github.com/codingconcepts/env/stargazers) - Tag-based environment configuration for structs.
- [flaggy](https://github.com/integrii/flaggy) [![GitHub stars](https://img.shields.io/github/stars/integrii/flaggy?style=flat)](https://github.com/integrii/flaggy/stargazers) - A robust and idiomatic flags package with excellent subcommand support.
- [flagvar](https://github.com/sgreben/flagvar) [![GitHub stars](https://img.shields.io/github/stars/sgreben/flagvar?style=flat)](https://github.com/sgreben/flagvar/stargazers) - A collection of flag argument types for Go's standard `flag` package.
- [flash-flags](https://github.com/agilira/flash-flags) [![GitHub stars](https://img.shields.io/github/stars/agilira/flash-flags?style=flat)](https://github.com/agilira/flash-flags/stargazers) - Ultra-fast, zero-dependency, POSIX-compliant flag parsing library that can be used as drop-in stdlib replacement with security hardening.
- [getopt](https://github.com/jon-codes/getopt) [![GitHub stars](https://img.shields.io/github/stars/jon-codes/getopt?style=flat)](https://github.com/jon-codes/getopt/stargazers) - An accurate Go `getopt`, validated against the GNU libc implementation.
- [go-arg](https://github.com/alexflint/go-arg) [![GitHub stars](https://img.shields.io/github/stars/alexflint/go-arg?style=flat)](https://github.com/alexflint/go-arg/stargazers) - Struct-based argument parsing in Go.
- [go-flags](https://github.com/jessevdk/go-flags) [![GitHub stars](https://img.shields.io/github/stars/jessevdk/go-flags?style=flat)](https://github.com/jessevdk/go-flags/stargazers) - go command line option parser.
- [go-getoptions](https://github.com/DavidGamba/go-getoptions) [![GitHub stars](https://img.shields.io/github/stars/DavidGamba/go-getoptions?style=flat)](https://github.com/DavidGamba/go-getoptions/stargazers) - Go option parser inspired by the flexibility of Perl’s GetOpt::Long.
- [go-readline-ny](https://github.com/nyaosorg/go-readline-ny) [![GitHub stars](https://img.shields.io/github/stars/nyaosorg/go-readline-ny?style=flat)](https://github.com/nyaosorg/go-readline-ny/stargazers) - A customizable line-editing library with Emacs keybindings, Unicode support, completion, and syntax highlighting. Used in NYAGOS shell.
- [gocmd](https://github.com/devfacet/gocmd) [![GitHub stars](https://img.shields.io/github/stars/devfacet/gocmd?style=flat)](https://github.com/devfacet/gocmd/stargazers) - Go library for building command line applications.
- [goopt](https://github.com/napalu/goopt) [![GitHub stars](https://img.shields.io/github/stars/napalu/goopt?style=flat)](https://github.com/napalu/goopt/stargazers) - A declarative, struct-tag based CLI framework for Go, with a broad feature set such as hierarchical commands/flags, i18n, shell completion, and validation.
- [hashicorp/cli](https://github.com/hashicorp/cli) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/cli?style=flat)](https://github.com/hashicorp/cli/stargazers) - Go library for implementing command-line interfaces.
- [hiboot cli](https://github.com/hidevopsio/hiboot/tree/master/pkg/app/cli) [![GitHub stars](https://img.shields.io/github/stars/hidevopsio/hiboot/tree/master/pkg/app/cli?style=flat)](https://github.com/hidevopsio/hiboot/tree/master/pkg/app/cli/stargazers) - cli application framework with auto configuration and dependency injection.
- [job](https://github.com/liujianping/job) [![GitHub stars](https://img.shields.io/github/stars/liujianping/job?style=flat)](https://github.com/liujianping/job/stargazers) - JOB, make your short-term command as a long-term job.
- [kingpin](https://github.com/alecthomas/kingpin) [![GitHub stars](https://img.shields.io/github/stars/alecthomas/kingpin?style=flat)](https://github.com/alecthomas/kingpin/stargazers) - Command line and flag parser supporting sub commands (superseded by `kong`; see below).
- [liner](https://github.com/peterh/liner) [![GitHub stars](https://img.shields.io/github/stars/peterh/liner?style=flat)](https://github.com/peterh/liner/stargazers) - Go readline-like library for command-line interfaces.
- [mcli](https://github.com/jxskiss/mcli) [![GitHub stars](https://img.shields.io/github/stars/jxskiss/mcli?style=flat)](https://github.com/jxskiss/mcli/stargazers) - A minimal but very powerful cli library for Go.
- [memsh](https://github.com/amjadjibon/memsh) [![GitHub stars](https://img.shields.io/github/stars/amjadjibon/memsh?style=flat)](https://github.com/amjadjibon/memsh/stargazers) - Virtual bash shell in Go: executes shell commands against an in-memory filesystem (afero), with WASM plugin support and an embeddable HTTP server.
- [mkideal/cli](https://github.com/mkideal/cli) [![GitHub stars](https://img.shields.io/github/stars/mkideal/cli?style=flat)](https://github.com/mkideal/cli/stargazers) - Feature-rich and easy to use command-line package based on golang struct tags.
- [mow.cli](https://github.com/jawher/mow.cli) [![GitHub stars](https://img.shields.io/github/stars/jawher/mow.cli?style=flat)](https://github.com/jawher/mow.cli/stargazers) - Go library for building CLI applications with sophisticated flag and argument parsing and validation.
- [neuron-cli](https://github.com/steevin/neuron-cli) [![GitHub stars](https://img.shields.io/github/stars/steevin/neuron-cli?style=flat)](https://github.com/steevin/neuron-cli/stargazers) - A local-first, Obsidian-compatible terminal knowledge manager.
- [ops](https://github.com/nanovms/ops) [![GitHub stars](https://img.shields.io/github/stars/nanovms/ops?style=flat)](https://github.com/nanovms/ops/stargazers) - Unikernel Builder/Orchestrator.
- [orpheus](https://github.com/agilira/orpheus) [![GitHub stars](https://img.shields.io/github/stars/agilira/orpheus?style=flat)](https://github.com/agilira/orpheus/stargazers) - CLI framework with security hardening, plugin storage system, and production observability features.
- [pflag](https://github.com/spf13/pflag) [![GitHub stars](https://img.shields.io/github/stars/spf13/pflag?style=flat)](https://github.com/spf13/pflag/stargazers) - Drop-in replacement for Go's flag package, implementing POSIX/GNU-style --flags.
- [readline](https://github.com/reeflective/readline) [![GitHub stars](https://img.shields.io/github/stars/reeflective/readline?style=flat)](https://github.com/reeflective/readline/stargazers) - Shell library with modern and easy to use UI features.
- [sflags](https://github.com/octago/sflags) [![GitHub stars](https://img.shields.io/github/stars/octago/sflags?style=flat)](https://github.com/octago/sflags/stargazers) - Struct based flags generator for flag, urfave/cli, pflag, cobra, kingpin, and other libraries.
- [structcli](https://github.com/leodido/structcli) [![GitHub stars](https://img.shields.io/github/stars/leodido/structcli?style=flat)](https://github.com/leodido/structcli/stargazers) - Eliminate Cobra boilerplate: build powerful, feature-rich CLIs declaratively from Go structs.
- [strumt](https://github.com/antham/strumt) [![GitHub stars](https://img.shields.io/github/stars/antham/strumt?style=flat)](https://github.com/antham/strumt/stargazers) - Library to create prompt chain.
- [subcmd](https://github.com/bobg/subcmd) [![GitHub stars](https://img.shields.io/github/stars/bobg/subcmd?style=flat)](https://github.com/bobg/subcmd/stargazers) - Another approach to parsing and running subcommands. Works alongside the standard `flag` package.
- [teris-io/cli](https://github.com/teris-io/cli) [![GitHub stars](https://img.shields.io/github/stars/teris-io/cli?style=flat)](https://github.com/teris-io/cli/stargazers) - Simple and complete API for building command line interfaces in Go.
- [urfave/cli](https://github.com/urfave/cli) [![GitHub stars](https://img.shields.io/github/stars/urfave/cli?style=flat)](https://github.com/urfave/cli/stargazers) - Simple, fast, and fun package for building command line apps in Go (formerly codegangsta/cli).
- [version](https://github.com/mszostok/version) [![GitHub stars](https://img.shields.io/github/stars/mszostok/version?style=flat)](https://github.com/mszostok/version/stargazers) - Collects and displays CLI version information in multiple formats along with upgrade notice.
- [wlog](https://github.com/dixonwille/wlog) [![GitHub stars](https://img.shields.io/github/stars/dixonwille/wlog?style=flat)](https://github.com/dixonwille/wlog/stargazers) - Simple logging interface that supports cross-platform color and concurrency.
- [wmenu](https://github.com/dixonwille/wmenu) [![GitHub stars](https://img.shields.io/github/stars/dixonwille/wmenu?style=flat)](https://github.com/dixonwille/wmenu/stargazers) - Easy to use menu structure for cli applications that prompt users to make choices.

**[⬆ back to top](#contents)**

## Configuration

_Libraries for configuration parsing._

- [aconfig](https://github.com/cristalhq/aconfig) [![GitHub stars](https://img.shields.io/github/stars/cristalhq/aconfig?style=flat)](https://github.com/cristalhq/aconfig/stargazers) - Simple, useful and opinionated config loader.
- [argus](https://github.com/agilira/argus) [![GitHub stars](https://img.shields.io/github/stars/agilira/argus?style=flat)](https://github.com/agilira/argus/stargazers) - File watching and configuration management with MPSC ring buffer, adaptive batching strategies, and universal format parsing (JSON, YAML, TOML, INI, HCL, Properties).
- [azureappconfiguration](https://github.com/Azure/AppConfiguration-GoProvider) [![GitHub stars](https://img.shields.io/github/stars/Azure/AppConfiguration-GoProvider?style=flat)](https://github.com/Azure/AppConfiguration-GoProvider/stargazers) - The configuration provider for consuming data in Azure App Configuration from Go applications.
- [bcl](https://github.com/wkhere/bcl) [![GitHub stars](https://img.shields.io/github/stars/wkhere/bcl?style=flat)](https://github.com/wkhere/bcl/stargazers) - BCL is a configuration language similar to HCL.
- [cleanenv](https://github.com/ilyakaznacheev/cleanenv) [![GitHub stars](https://img.shields.io/github/stars/ilyakaznacheev/cleanenv?style=flat)](https://github.com/ilyakaznacheev/cleanenv/stargazers) - Minimalistic configuration reader (from files, ENV, and wherever you want).
- [config](https://github.com/JeremyLoy/config) [![GitHub stars](https://img.shields.io/github/stars/JeremyLoy/config?style=flat)](https://github.com/JeremyLoy/config/stargazers) - Cloud native application configuration. Bind ENV to structs in only two lines.
- [config](https://github.com/num30/config) [![GitHub stars](https://img.shields.io/github/stars/num30/config?style=flat)](https://github.com/num30/config/stargazers) - configure your app using file, environment variables, or flags in two lines of code.
- [config](https://github.com/andreiavrammsd/config) [![GitHub stars](https://img.shields.io/github/stars/andreiavrammsd/config?style=flat)](https://github.com/andreiavrammsd/config/stargazers) - Struct-based configuration loader with a dedicated config file parser, supporting env vars, flags, defaults, and validation.
- [configuration](https://github.com/BoRuDar/configuration) [![GitHub stars](https://img.shields.io/github/stars/BoRuDar/configuration?style=flat)](https://github.com/BoRuDar/configuration/stargazers) - Library for initializing configuration structs from env variables, files, flags and 'default' tag.
- [configuro](https://github.com/sherifabdlnaby/configuro) [![GitHub stars](https://img.shields.io/github/stars/sherifabdlnaby/configuro?style=flat)](https://github.com/sherifabdlnaby/configuro/stargazers) - opinionated configuration loading & validation framework from ENV and Files focused towards 12-Factor compliant applications.
- [confiq](https://github.com/greencoda/confiq) [![GitHub stars](https://img.shields.io/github/stars/greencoda/confiq?style=flat)](https://github.com/greencoda/confiq/stargazers) - Structured data format to config struct decoder library for Go - supporting multiple data formats.
- [confita](https://github.com/heetch/confita) [![GitHub stars](https://img.shields.io/github/stars/heetch/confita?style=flat)](https://github.com/heetch/confita/stargazers) - Load configuration in cascade from multiple backends into a struct.
- [conflate](https://github.com/the4thamigo-uk/conflate) [![GitHub stars](https://img.shields.io/github/stars/the4thamigo-uk/conflate?style=flat)](https://github.com/the4thamigo-uk/conflate/stargazers) - Library/tool to merge multiple JSON/YAML/TOML files from arbitrary URLs, validation against a JSON schema, and application of default values defined in the schema.
- [enflag](https://github.com/atelpis/enflag) [![GitHub stars](https://img.shields.io/github/stars/atelpis/enflag?style=flat)](https://github.com/atelpis/enflag/stargazers) - Container-oriented, zero-dependency configuration library that unifies Env variable and Flag parsing. Uses generics for type safety, without reflection or struct tags.
- [env](https://github.com/caarlos0/env) [![GitHub stars](https://img.shields.io/github/stars/caarlos0/env?style=flat)](https://github.com/caarlos0/env/stargazers) - Parse environment variables to Go structs (with defaults).
- [env](https://github.com/junk1tm/env) [![GitHub stars](https://img.shields.io/github/stars/junk1tm/env?style=flat)](https://github.com/junk1tm/env/stargazers) - A lightweight package for loading environment variables into structs.
- [env](https://github.com/syntaqx/env) [![GitHub stars](https://img.shields.io/github/stars/syntaqx/env?style=flat)](https://github.com/syntaqx/env/stargazers) - An environment utility package with support for unmarshaling into structs.
- [envconfig](https://github.com/vrischmann/envconfig) [![GitHub stars](https://img.shields.io/github/stars/vrischmann/envconfig?style=flat)](https://github.com/vrischmann/envconfig/stargazers) - Read your configuration from environment variables.
- [envh](https://github.com/antham/envh) [![GitHub stars](https://img.shields.io/github/stars/antham/envh?style=flat)](https://github.com/antham/envh/stargazers) - Helpers to manage environment variables.
- [envyaml](https://github.com/yuseferi/envyaml) [![GitHub stars](https://img.shields.io/github/stars/yuseferi/envyaml?style=flat)](https://github.com/yuseferi/envyaml/stargazers) - Yaml with environment variables reader. it helps to have secrets as environment variable but load them configs as structured Yaml.
- [fig](https://github.com/kkyr/fig) [![GitHub stars](https://img.shields.io/github/stars/kkyr/fig?style=flat)](https://github.com/kkyr/fig/stargazers) - Tiny library for reading configuration from a file and from environment variables (with validation & defaults).
- [genv](https://github.com/sakirsensoy/genv) [![GitHub stars](https://img.shields.io/github/stars/sakirsensoy/genv?style=flat)](https://github.com/sakirsensoy/genv/stargazers) - Read environment variables easily with dotenv support.
- [go-array](https://github.com/deatil/go-array) [![GitHub stars](https://img.shields.io/github/stars/deatil/go-array?style=flat)](https://github.com/deatil/go-array/stargazers) - A Go package that read or set data from map, slice or json.
- [go-aws-ssm](https://github.com/PaddleHQ/go-aws-ssm) [![GitHub stars](https://img.shields.io/github/stars/PaddleHQ/go-aws-ssm?style=flat)](https://github.com/PaddleHQ/go-aws-ssm/stargazers) - Go package that fetches parameters from AWS System Manager - Parameter Store.
- [go-cfg](https://github.com/dsbasko/go-cfg) [![GitHub stars](https://img.shields.io/github/stars/dsbasko/go-cfg?style=flat)](https://github.com/dsbasko/go-cfg/stargazers) - The library provides a unified way to read configuration data into a structure from various sources, such as env, flags, and configuration files (.json, .yaml, .toml, .env).
- [go-conf](https://github.com/ThomasObenaus/go-conf) [![GitHub stars](https://img.shields.io/github/stars/ThomasObenaus/go-conf?style=flat)](https://github.com/ThomasObenaus/go-conf/stargazers) - Simple library for application configuration based on annotated structs. It supports reading the configuration from environment variables, config files and command line parameters.
- [go-config](https://github.com/MordaTeam/go-config) [![GitHub stars](https://img.shields.io/github/stars/MordaTeam/go-config?style=flat)](https://github.com/MordaTeam/go-config/stargazers) - Simple and convenient library for working with app configurations.
- [go-external-config](https://github.com/go-external-config/go) [![GitHub stars](https://img.shields.io/github/stars/go-external-config/go?style=flat)](https://github.com/go-external-config/go/stargazers) - Spring-inspired configuration management library for Go.
- [go-external-config/aws](https://github.com/go-external-config/aws) [![GitHub stars](https://img.shields.io/github/stars/go-external-config/aws?style=flat)](https://github.com/go-external-config/aws/stargazers) - AWS property source support for go-external-config.
- [go-external-config/consul](https://github.com/go-external-config/consul) [![GitHub stars](https://img.shields.io/github/stars/go-external-config/consul?style=flat)](https://github.com/go-external-config/consul/stargazers) - Consul property source support for go-external-config.
- [go-external-config/vault](https://github.com/go-external-config/vault) [![GitHub stars](https://img.shields.io/github/stars/go-external-config/vault?style=flat)](https://github.com/go-external-config/vault/stargazers) - Vault property source support for go-external-config.
- [go-ini](https://github.com/subpop/go-ini) [![GitHub stars](https://img.shields.io/github/stars/subpop/go-ini?style=flat)](https://github.com/subpop/go-ini/stargazers) - A Go package that marshals and unmarshals INI-files.
- [go-ssm-config](https://github.com/ianlopshire/go-ssm-config) [![GitHub stars](https://img.shields.io/github/stars/ianlopshire/go-ssm-config?style=flat)](https://github.com/ianlopshire/go-ssm-config/stargazers) - Go utility for loading configuration parameters from AWS SSM (Parameter Store).
- [go-up](https://github.com/ufoscout/go-up) [![GitHub stars](https://img.shields.io/github/stars/ufoscout/go-up?style=flat)](https://github.com/ufoscout/go-up/stargazers) - A simple configuration library with recursive placeholders resolution and no magic.
- [GoCfg](https://github.com/Jagerente/gocfg) [![GitHub stars](https://img.shields.io/github/stars/Jagerente/gocfg?style=flat)](https://github.com/Jagerente/gocfg/stargazers) - Config manager with Struct Tags based contracts, custom value providers, parsers, and documentation generation. Customizable yet simple.
- [goconfig](https://github.com/fulldump/goconfig) [![GitHub stars](https://img.shields.io/github/stars/fulldump/goconfig?style=flat)](https://github.com/fulldump/goconfig/stargazers) - Populate Go structs from flags, environment variables, config.json and defaults with deterministic precedence. No extra dependencies.
- [godotenv](https://github.com/joho/godotenv) [![GitHub stars](https://img.shields.io/github/stars/joho/godotenv?style=flat)](https://github.com/joho/godotenv/stargazers) - Go port of Ruby's dotenv library (Loads environment variables from `.env`).
- [GoLobby/Config](https://github.com/golobby/config) [![GitHub stars](https://img.shields.io/github/stars/golobby/config?style=flat)](https://github.com/golobby/config/stargazers) - GoLobby Config is a lightweight yet powerful configuration manager for the Go programming language.
- [gone/jconf](https://github.com/One-com/gone/tree/master/jconf) [![GitHub stars](https://img.shields.io/github/stars/One-com/gone/tree/master/jconf?style=flat)](https://github.com/One-com/gone/tree/master/jconf/stargazers) - Modular JSON configuration. Keep your config structs along with the code they configure and delegate parsing to submodules without sacrificing full config serialization.
- [gonfig](https://github.com/milad-abbasi/gonfig) [![GitHub stars](https://img.shields.io/github/stars/milad-abbasi/gonfig?style=flat)](https://github.com/milad-abbasi/gonfig/stargazers) - Tag-based configuration parser which loads values from different providers into typesafe struct.
- [gookit/config](https://github.com/gookit/config) [![GitHub stars](https://img.shields.io/github/stars/gookit/config?style=flat)](https://github.com/gookit/config/stargazers) - application config manage(load,get,set). support JSON, YAML, TOML, INI, HCL. multi file load, data override merge.
- [harvester](https://github.com/beatlabs/harvester) [![GitHub stars](https://img.shields.io/github/stars/beatlabs/harvester?style=flat)](https://github.com/beatlabs/harvester/stargazers) - Harvester, a easy to use static and dynamic configuration package supporting seeding, env vars and Consul integration.
- [hedzr/store](https://github.com/hedzr/store) [![GitHub stars](https://img.shields.io/github/stars/hedzr/store?style=flat)](https://github.com/hedzr/store/stargazers) - Extensible, high-performance configuration management library, optimized for hierarchical data.
- [hjson](https://github.com/hjson/hjson-go) [![GitHub stars](https://img.shields.io/github/stars/hjson/hjson-go?style=flat)](https://github.com/hjson/hjson-go/stargazers) - Human JSON, a configuration file format for humans. Relaxed syntax, fewer mistakes, more comments.
- [hocon](https://github.com/gurkankaymak/hocon) [![GitHub stars](https://img.shields.io/github/stars/gurkankaymak/hocon?style=flat)](https://github.com/gurkankaymak/hocon/stargazers) - Configuration library for working with the HOCON(a human-friendly JSON superset) format, supports features like environment variables, referencing other values, comments and multiple files.
- [ini](https://github.com/go-ini/ini) [![GitHub stars](https://img.shields.io/github/stars/go-ini/ini?style=flat)](https://github.com/go-ini/ini/stargazers) - Go package to read and write INI files.
- [ini](https://github.com/wlevene/ini) [![GitHub stars](https://img.shields.io/github/stars/wlevene/ini?style=flat)](https://github.com/wlevene/ini/stargazers) - INI Parser & Write Library, Unmarshal to Struct, Marshal to Json, Write File, watch file.
- [kelseyhightower/envconfig](https://github.com/kelseyhightower/envconfig) [![GitHub stars](https://img.shields.io/github/stars/kelseyhightower/envconfig?style=flat)](https://github.com/kelseyhightower/envconfig/stargazers) - Go library for managing configuration data from environment variables.
- [koanf](https://github.com/knadh/koanf) [![GitHub stars](https://img.shields.io/github/stars/knadh/koanf?style=flat)](https://github.com/knadh/koanf/stargazers) - Light weight, extensible library for reading config in Go applications. Built in support for JSON, TOML, YAML, env, command line.
- [konf](https://github.com/nil-go/konf) [![GitHub stars](https://img.shields.io/github/stars/nil-go/konf?style=flat)](https://github.com/nil-go/konf/stargazers) - The simplest API for reading/watching config from file, env, flag and clouds (e.g. AWS, Azure, GCP).
- [konfig](https://github.com/lalamove/konfig) [![GitHub stars](https://img.shields.io/github/stars/lalamove/konfig?style=flat)](https://github.com/lalamove/konfig/stargazers) - Composable, observable and performant config handling for Go for the distributed processing era.
- [kong](https://github.com/alecthomas/kong) [![GitHub stars](https://img.shields.io/github/stars/alecthomas/kong?style=flat)](https://github.com/alecthomas/kong/stargazers) - Command-line parser with support for arbitrarily complex command-line structures and additional sources of configuration such as YAML, JSON, TOML, etc (successor to `kingpin`).
- [nasermirzaei89/env](https://github.com/nasermirzaei89/env) [![GitHub stars](https://img.shields.io/github/stars/nasermirzaei89/env?style=flat)](https://github.com/nasermirzaei89/env/stargazers) - Simple useful package for read environment variables.
- [nfigure](https://github.com/muir/nfigure) [![GitHub stars](https://img.shields.io/github/stars/muir/nfigure?style=flat)](https://github.com/muir/nfigure/stargazers) - Per-library struct-tag based configuration from command lines (Posix & Go-style); environment, JSON, YAML
- [onion](https://github.com/goraz/onion) [![GitHub stars](https://img.shields.io/github/stars/goraz/onion?style=flat)](https://github.com/goraz/onion/stargazers) - Layer based configuration for Go, Supports JSON, TOML, YAML, properties, etcd, env, and encryption using PGP.
- [piper](https://github.com/Yiling-J/piper) [![GitHub stars](https://img.shields.io/github/stars/Yiling-J/piper?style=flat)](https://github.com/Yiling-J/piper/stargazers) - Viper wrapper with config inheritance and key generation.
- [sonic](https://github.com/bytedance/sonic) [![GitHub stars](https://img.shields.io/github/stars/bytedance/sonic?style=flat)](https://github.com/bytedance/sonic/stargazers) - A blazingly fast JSON serializing & deserializing library.
- [swap](https://github.com/oblq/swap) [![GitHub stars](https://img.shields.io/github/stars/oblq/swap?style=flat)](https://github.com/oblq/swap/stargazers) - Instantiate/configure structs recursively, based on build environment. (YAML, TOML, JSON and env).
- [typenv](https://github.com/diegomarangoni/typenv) [![GitHub stars](https://img.shields.io/github/stars/diegomarangoni/typenv?style=flat)](https://github.com/diegomarangoni/typenv/stargazers) - Minimalistic, zero dependency, typed environment variables library.
- [uConfig](https://github.com/omeid/uconfig) [![GitHub stars](https://img.shields.io/github/stars/omeid/uconfig?style=flat)](https://github.com/omeid/uconfig/stargazers) - Lightweight, zero-dependency, and extendable configuration management.
- [viper](https://github.com/spf13/viper) [![GitHub stars](https://img.shields.io/github/stars/spf13/viper?style=flat)](https://github.com/spf13/viper/stargazers) - Go configuration with fangs.
- [xdg](https://github.com/adrg/xdg) [![GitHub stars](https://img.shields.io/github/stars/adrg/xdg?style=flat)](https://github.com/adrg/xdg/stargazers) - Go implementation of the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) and [XDG user directories](https://wiki.archlinux.org/index.php/XDG_user_directories).
- [yamagiconf](https://github.com/romshark/yamagiconf) [![GitHub stars](https://img.shields.io/github/stars/romshark/yamagiconf?style=flat)](https://github.com/romshark/yamagiconf/stargazers) - The "safe subset" of YAML for Go configs.
- [zerocfg](https://github.com/chaindead/zerocfg) [![GitHub stars](https://img.shields.io/github/stars/chaindead/zerocfg?style=flat)](https://github.com/chaindead/zerocfg/stargazers) - Zero-effort, concise configuration management that avoids boilerplate and repetitive code, supports multiple sources with priority overrides.

**[⬆ back to top](#contents)**

## Continuous Integration

_Tools for help with continuous integration._

- [abstruse](https://github.com/bleenco/abstruse) [![GitHub stars](https://img.shields.io/github/stars/bleenco/abstruse?style=flat)](https://github.com/bleenco/abstruse/stargazers) - Abstruse is a distributed CI platform.
- [Bencher](https://bencher.dev/) - A suite of continuous benchmarking tools designed to catch performance regressions in CI.
- [CDS](https://github.com/ovh/cds) [![GitHub stars](https://img.shields.io/github/stars/ovh/cds?style=flat)](https://github.com/ovh/cds/stargazers) - Enterprise-Grade CI/CD and DevOps Automation Open Source Platform.
- [dot](https://github.com/opnlabs/dot) [![GitHub stars](https://img.shields.io/github/stars/opnlabs/dot?style=flat)](https://github.com/opnlabs/dot/stargazers) - A minimal, local first continuous integration system that uses Docker to run jobs concurrently in stages.
- [drone](https://github.com/drone/drone) [![GitHub stars](https://img.shields.io/github/stars/drone/drone?style=flat)](https://github.com/drone/drone/stargazers) - Drone is a Continuous Integration platform built on Docker, written in Go.
- [go-beautiful-html-coverage](https://github.com/gha-common/go-beautiful-html-coverage) [![GitHub stars](https://img.shields.io/github/stars/gha-common/go-beautiful-html-coverage?style=flat)](https://github.com/gha-common/go-beautiful-html-coverage/stargazers) - A GitHub Action to track code coverage in your pull requests, with a beautiful HTML preview, for free.
- [go-fuzz-action](https://github.com/jidicula/go-fuzz-action) [![GitHub stars](https://img.shields.io/github/stars/jidicula/go-fuzz-action?style=flat)](https://github.com/jidicula/go-fuzz-action/stargazers) - Use Go 1.18's built-in fuzz testing in GitHub Actions.
- [go-semver-release](https://github.com/s0ders/go-semver-release) [![GitHub stars](https://img.shields.io/github/stars/s0ders/go-semver-release?style=flat)](https://github.com/s0ders/go-semver-release/stargazers) - Automate the semantic versioning of Git repositories.
- [go-test-coverage](https://github.com/marketplace/actions/go-test-coverage) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/go-test-coverage?style=flat)](https://github.com/marketplace/actions/go-test-coverage/stargazers) - A GitHub Action which reports issues when test coverage is below set threshold.
- [gomason](https://github.com/nikogura/gomason) [![GitHub stars](https://img.shields.io/github/stars/nikogura/gomason?style=flat)](https://github.com/nikogura/gomason/stargazers) - Test, Build, Sign, and Publish your go binaries from a clean workspace.
- [gotestfmt](https://github.com/GoTestTools/gotestfmt) [![GitHub stars](https://img.shields.io/github/stars/GoTestTools/gotestfmt?style=flat)](https://github.com/GoTestTools/gotestfmt/stargazers) - go test output for humans.
- [goveralls](https://github.com/mattn/goveralls) [![GitHub stars](https://img.shields.io/github/stars/mattn/goveralls?style=flat)](https://github.com/mattn/goveralls/stargazers) - Go integration for Coveralls.io continuous code coverage tracking system.
- [muffet](https://github.com/raviqqe/muffet) [![GitHub stars](https://img.shields.io/github/stars/raviqqe/muffet?style=flat)](https://github.com/raviqqe/muffet/stargazers) - Fast website link checker in Go, see [alternatives](https://github.com/lycheeverse/lychee#features).
- [overalls](https://github.com/go-playground/overalls) [![GitHub stars](https://img.shields.io/github/stars/go-playground/overalls?style=flat)](https://github.com/go-playground/overalls/stargazers) - Multi-Package go project coverprofile for tools like goveralls.
- [PikoCI](https://github.com/pikoci/pikoci) [![GitHub stars](https://img.shields.io/github/stars/pikoci/pikoci?style=flat)](https://github.com/pikoci/pikoci/stargazers) - Self-hosted CI/CD inspired by Concourse. Single binary, any database, any queue. HCL pipelines, pluggable resource types and runners.
- [roveralls](https://github.com/LawrenceWoodman/roveralls) [![GitHub stars](https://img.shields.io/github/stars/LawrenceWoodman/roveralls?style=flat)](https://github.com/LawrenceWoodman/roveralls/stargazers) - Recursive coverage testing tool.
- [woodpecker](https://github.com/woodpecker-ci/woodpecker) [![GitHub stars](https://img.shields.io/github/stars/woodpecker-ci/woodpecker?style=flat)](https://github.com/woodpecker-ci/woodpecker/stargazers) - Woodpecker is a community fork of the Drone CI system.

**[⬆ back to top](#contents)**

## CSS Preprocessors

_Libraries for preprocessing CSS files._

- [go-css](https://github.com/napsy/go-css) [![GitHub stars](https://img.shields.io/github/stars/napsy/go-css?style=flat)](https://github.com/napsy/go-css/stargazers) - A very simple CSS parser, written in Go.
- [go-libsass](https://github.com/wellington/go-libsass) [![GitHub stars](https://img.shields.io/github/stars/wellington/go-libsass?style=flat)](https://github.com/wellington/go-libsass/stargazers) - Go wrapper to the 100% Sass compatible libsass project.

**[⬆ back to top](#contents)**

## Data Integration Frameworks

_Frameworks for performing ELT / ETL_

- [Benthos](https://github.com/benthosdev/benthos) [![GitHub stars](https://img.shields.io/github/stars/benthosdev/benthos?style=flat)](https://github.com/benthosdev/benthos/stargazers) - A message streaming bridge between a range of protocols.
- [CloudQuery](http://github.com/cloudquery/cloudquery) - A high-performance ELT data integration framework with pluggable architecture.
- [confluence2md](https://github.com/gkoos/confluence2md) [![GitHub stars](https://img.shields.io/github/stars/gkoos/confluence2md?style=flat)](https://github.com/gkoos/confluence2md/stargazers) - Confluence to Markdown crawler and converter.
- [omniparser](https://github.com/jf-tech/omniparser) [![GitHub stars](https://img.shields.io/github/stars/jf-tech/omniparser?style=flat)](https://github.com/jf-tech/omniparser/stargazers) - A versatile ETL library that parses text input (CSV/txt/JSON/XML/EDI/X12/EDIFACT/etc) in streaming fashion and transforms data into JSON output using data-driven schema.

**[⬆ back to top](#contents)**

## Data Structures and Algorithms

### Bit-packing and Compression

- [bingo](https://github.com/iancmcc/bingo) [![GitHub stars](https://img.shields.io/github/stars/iancmcc/bingo?style=flat)](https://github.com/iancmcc/bingo/stargazers) - Fast, zero-allocation, lexicographical-order-preserving packing of native types to bytes.
- [binpacker](https://github.com/zhuangsirui/binpacker) [![GitHub stars](https://img.shields.io/github/stars/zhuangsirui/binpacker?style=flat)](https://github.com/zhuangsirui/binpacker/stargazers) - Binary packer and unpacker helps user build custom binary stream.
- [bit](https://github.com/yourbasic/bit) [![GitHub stars](https://img.shields.io/github/stars/yourbasic/bit?style=flat)](https://github.com/yourbasic/bit/stargazers) - Golang set data structure with bonus bit-twiddling functions.
- [crunch](https://github.com/superwhiskers/crunch) [![GitHub stars](https://img.shields.io/github/stars/superwhiskers/crunch?style=flat)](https://github.com/superwhiskers/crunch/stargazers) - Go package implementing buffers for handling various datatypes easily.
- [go-ef](https://github.com/amallia/go-ef) [![GitHub stars](https://img.shields.io/github/stars/amallia/go-ef?style=flat)](https://github.com/amallia/go-ef/stargazers) - A Go implementation of the Elias-Fano encoding.
- [roaring](https://github.com/RoaringBitmap/roaring) [![GitHub stars](https://img.shields.io/github/stars/RoaringBitmap/roaring?style=flat)](https://github.com/RoaringBitmap/roaring/stargazers) - Go package implementing compressed bitsets.

### Bit Sets

- [bitmap](https://github.com/kelindar/bitmap) [![GitHub stars](https://img.shields.io/github/stars/kelindar/bitmap?style=flat)](https://github.com/kelindar/bitmap/stargazers) - Dense, zero-allocation, SIMD-enabled bitmap/bitset in Go.
- [bitset](https://github.com/bits-and-blooms/bitset) [![GitHub stars](https://img.shields.io/github/stars/bits-and-blooms/bitset?style=flat)](https://github.com/bits-and-blooms/bitset/stargazers) - Go package implementing bitsets.

### Bloom and Cuckoo Filters

- [bloom](https://github.com/bits-and-blooms/bloom) [![GitHub stars](https://img.shields.io/github/stars/bits-and-blooms/bloom?style=flat)](https://github.com/bits-and-blooms/bloom/stargazers) - Go package implementing Bloom filters.
- [bloom](https://github.com/zhenjl/bloom) [![GitHub stars](https://img.shields.io/github/stars/zhenjl/bloom?style=flat)](https://github.com/zhenjl/bloom/stargazers) - Bloom filters implemented in Go.
- [bloom](https://github.com/yourbasic/bloom) [![GitHub stars](https://img.shields.io/github/stars/yourbasic/bloom?style=flat)](https://github.com/yourbasic/bloom/stargazers) - Golang Bloom filter implementation.
- [bloomfilter](https://github.com/OldPanda/bloomfilter) [![GitHub stars](https://img.shields.io/github/stars/OldPanda/bloomfilter?style=flat)](https://github.com/OldPanda/bloomfilter/stargazers) - Yet another Bloomfilter implementation in Go, compatible with Java's Guava library.
- [boomfilters](https://github.com/tylertreat/BoomFilters) [![GitHub stars](https://img.shields.io/github/stars/tylertreat/BoomFilters?style=flat)](https://github.com/tylertreat/BoomFilters/stargazers) - Probabilistic data structures for processing continuous, unbounded streams.
- [cuckoo-filter](https://github.com/linvon/cuckoo-filter) [![GitHub stars](https://img.shields.io/github/stars/linvon/cuckoo-filter?style=flat)](https://github.com/linvon/cuckoo-filter/stargazers) - Cuckoo filter: a comprehensive cuckoo filter, which is configurable and space optimized compared with other implements, and all features mentioned in original paper are available.
- [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) [![GitHub stars](https://img.shields.io/github/stars/seiflotfy/cuckoofilter?style=flat)](https://github.com/seiflotfy/cuckoofilter/stargazers) - Cuckoo filter: a good alternative to a counting bloom filter implemented in Go.
- [ribbonGo](https://github.com/RibbonFilter/ribbonGo) [![GitHub stars](https://img.shields.io/github/stars/RibbonFilter/ribbonGo?style=flat)](https://github.com/RibbonFilter/ribbonGo/stargazers) - First pure Go implementation of Ribbon filters (practically smaller than Bloom and Xor) for space-efficient approximate set membership queries.
- [ring](https://github.com/TheTannerRyan/ring) [![GitHub stars](https://img.shields.io/github/stars/TheTannerRyan/ring?style=flat)](https://github.com/TheTannerRyan/ring/stargazers) - Go implementation of a high performance, thread safe bloom filter.

### Data Structure and Algorithm Collections

- [algorithms](https://github.com/shady831213/algorithms) [![GitHub stars](https://img.shields.io/github/stars/shady831213/algorithms?style=flat)](https://github.com/shady831213/algorithms/stargazers) - Algorithms and data structures.CLRS study.
- [go-datastructures](https://github.com/Workiva/go-datastructures) [![GitHub stars](https://img.shields.io/github/stars/Workiva/go-datastructures?style=flat)](https://github.com/Workiva/go-datastructures/stargazers) - Collection of useful, performant, and thread-safe data structures.
- [gods](https://github.com/emirpasic/gods) [![GitHub stars](https://img.shields.io/github/stars/emirpasic/gods?style=flat)](https://github.com/emirpasic/gods/stargazers) - Go Data Structures. Containers, Sets, Lists, Stacks, Maps, BidiMaps, Trees, HashSet etc.
- [gostl](https://github.com/liyue201/gostl) [![GitHub stars](https://img.shields.io/github/stars/liyue201/gostl?style=flat)](https://github.com/liyue201/gostl/stargazers) - Data structure and algorithm library for go, designed to provide functions similar to C++ STL.

### Iterators

- [gloop](https://github.com/alvii147/gloop) [![GitHub stars](https://img.shields.io/github/stars/alvii147/gloop?style=flat)](https://github.com/alvii147/gloop/stargazers) - Convenient looping using Go's range-over-func feature.
- [goterator](https://github.com/yaa110/goterator) [![GitHub stars](https://img.shields.io/github/stars/yaa110/goterator?style=flat)](https://github.com/yaa110/goterator/stargazers) - Iterator implementation to provide map and reduce functionalities.
- [iter](https://github.com/disksing/iter) [![GitHub stars](https://img.shields.io/github/stars/disksing/iter?style=flat)](https://github.com/disksing/iter/stargazers) - Go implementation of C++ STL iterators and algorithms.

### Maps

See also [Database](#database) for more complex key-value stores, and [Trees](#trees) for
additional ordered map implementations.

- [cmap](https://github.com/lrita/cmap) [![GitHub stars](https://img.shields.io/github/stars/lrita/cmap?style=flat)](https://github.com/lrita/cmap/stargazers) - a thread-safe concurrent map for go, support using `interface{}` as key and auto scale up shards.
- [concurrent-swiss-map](https://github.com/mhmtszr/concurrent-swiss-map) [![GitHub stars](https://img.shields.io/github/stars/mhmtszr/concurrent-swiss-map?style=flat)](https://github.com/mhmtszr/concurrent-swiss-map/stargazers) - A high-performance, thread-safe generic concurrent hash map implementation with Swiss Map.
- [dict](https://github.com/srfrog/dict) [![GitHub stars](https://img.shields.io/github/stars/srfrog/dict?style=flat)](https://github.com/srfrog/dict/stargazers) - Python-like dictionaries (dict) for Go.
- [go-shelve](https://github.com/lucmq/go-shelve) [![GitHub stars](https://img.shields.io/github/stars/lucmq/go-shelve?style=flat)](https://github.com/lucmq/go-shelve/stargazers) - A persistent, map-like object for the Go programming language. Supports multiple embedded key-value stores.
- [goradd/maps](https://github.com/goradd/maps) [![GitHub stars](https://img.shields.io/github/stars/goradd/maps?style=flat)](https://github.com/goradd/maps/stargazers) - Go 1.18+ generic map interface for maps; safe maps; ordered maps; ordered, safe maps; etc.
- [hmap](https://github.com/lyonnee/hmap) [![GitHub stars](https://img.shields.io/github/stars/lyonnee/hmap?style=flat)](https://github.com/lyonnee/hmap/stargazers) - HMap is a concurrent and secure, generic support Map implementation designed to provide an easy-to-use API.

### Miscellaneous Data Structures and Algorithms

- [combo](https://github.com/bobg/combo) [![GitHub stars](https://img.shields.io/github/stars/bobg/combo?style=flat)](https://github.com/bobg/combo/stargazers) - Combinatorial operations including permutations, combinations, and combinations-with-replacement.
- [concurrent-writer](https://github.com/free/concurrent-writer) [![GitHub stars](https://img.shields.io/github/stars/free/concurrent-writer?style=flat)](https://github.com/free/concurrent-writer/stargazers) - Highly concurrent drop-in replacement for `bufio.Writer`.
- [count-min-log](https://github.com/seiflotfy/count-min-log) [![GitHub stars](https://img.shields.io/github/stars/seiflotfy/count-min-log?style=flat)](https://github.com/seiflotfy/count-min-log/stargazers) - Go implementation Count-Min-Log sketch: Approximately counting with approximate counters (Like Count-Min sketch but using less memory).
- [FSM](https://github.com/enetx/fsm) [![GitHub stars](https://img.shields.io/github/stars/enetx/fsm?style=flat)](https://github.com/enetx/fsm/stargazers) - FSM for Go.
- [fsm](https://github.com/cocoonspace/fsm) [![GitHub stars](https://img.shields.io/github/stars/cocoonspace/fsm?style=flat)](https://github.com/cocoonspace/fsm/stargazers) - Finite-State Machine package.
- [genfuncs](https://github.com/nwillc/genfuncs) [![GitHub stars](https://img.shields.io/github/stars/nwillc/genfuncs?style=flat)](https://github.com/nwillc/genfuncs/stargazers) - Go 1.18+ generics package inspired by Kotlin's Sequence and Map.
- [go-generics](https://github.com/bobg/go-generics) [![GitHub stars](https://img.shields.io/github/stars/bobg/go-generics?style=flat)](https://github.com/bobg/go-generics/stargazers) - Generic slice, map, set, iterator, and goroutine utilities.
- [go-geoindex](https://github.com/hailocab/go-geoindex) [![GitHub stars](https://img.shields.io/github/stars/hailocab/go-geoindex?style=flat)](https://github.com/hailocab/go-geoindex/stargazers) - In-memory geo index.
- [go-rampart](https://github.com/francesconi/go-rampart) [![GitHub stars](https://img.shields.io/github/stars/francesconi/go-rampart?style=flat)](https://github.com/francesconi/go-rampart/stargazers) - Determine how intervals relate to each other.
- [go-rquad](https://github.com/aurelien-rainone/go-rquad) [![GitHub stars](https://img.shields.io/github/stars/aurelien-rainone/go-rquad?style=flat)](https://github.com/aurelien-rainone/go-rquad/stargazers) - Region quadtrees with efficient point location and neighbour finding.
- [go-tuple](https://github.com/barweiss/go-tuple) [![GitHub stars](https://img.shields.io/github/stars/barweiss/go-tuple?style=flat)](https://github.com/barweiss/go-tuple/stargazers) - Generic tuple implementation for Go 1.18+.
- [go18ds](https://github.com/daichi-m/go18ds) [![GitHub stars](https://img.shields.io/github/stars/daichi-m/go18ds?style=flat)](https://github.com/daichi-m/go18ds/stargazers) - Go Data Structures using Go 1.18 generics.
- [gofal](https://github.com/xxjwxc/gofal) [![GitHub stars](https://img.shields.io/github/stars/xxjwxc/gofal?style=flat)](https://github.com/xxjwxc/gofal/stargazers) - fractional api for Go.
- [gogu](https://github.com/esimov/gogu) [![GitHub stars](https://img.shields.io/github/stars/esimov/gogu?style=flat)](https://github.com/esimov/gogu/stargazers) - A comprehensive, reusable and efficient concurrent-safe generics utility functions and data structures library.
- [gota](https://github.com/kniren/gota) [![GitHub stars](https://img.shields.io/github/stars/kniren/gota?style=flat)](https://github.com/kniren/gota/stargazers) - Implementation of dataframes, series, and data wrangling methods for Go.
- [hide](https://github.com/emvi/hide) [![GitHub stars](https://img.shields.io/github/stars/emvi/hide?style=flat)](https://github.com/emvi/hide/stargazers) - ID type with marshalling to/from hash to prevent sending IDs to clients.
- [hyperloglog](https://github.com/axiomhq/hyperloglog) [![GitHub stars](https://img.shields.io/github/stars/axiomhq/hyperloglog?style=flat)](https://github.com/axiomhq/hyperloglog/stargazers) - HyperLogLog implementation with Sparse, LogLog-Beta bias correction and TailCut space reduction.
- [quadtree](https://github.com/s0rg/quadtree) [![GitHub stars](https://img.shields.io/github/stars/s0rg/quadtree?style=flat)](https://github.com/s0rg/quadtree/stargazers) - Generic, zero-alloc, 100%-test covered quadtree.
- [slices](https://github.com/twharmon/slices) [![GitHub stars](https://img.shields.io/github/stars/twharmon/slices?style=flat)](https://github.com/twharmon/slices/stargazers) - Pure, generic functions for slices.

### Nullable Types

- [nan](https://github.com/kak-tus/nan) [![GitHub stars](https://img.shields.io/github/stars/kak-tus/nan?style=flat)](https://github.com/kak-tus/nan/stargazers) - Zero allocation Nullable structures in one library with handy conversion functions, marshallers and unmarshallers.
- [null](https://github.com/emvi/null) [![GitHub stars](https://img.shields.io/github/stars/emvi/null?style=flat)](https://github.com/emvi/null/stargazers) - Nullable Go types that can be marshalled/unmarshalled to/from JSON.
- [typ](https://github.com/gurukami/typ) [![GitHub stars](https://img.shields.io/github/stars/gurukami/typ?style=flat)](https://github.com/gurukami/typ/stargazers) - Null Types, Safe primitive type conversion and fetching value from complex structures.

### Queues

- [deheap](https://github.com/aalpar/deheap) [![GitHub stars](https://img.shields.io/github/stars/aalpar/deheap?style=flat)](https://github.com/aalpar/deheap/stargazers) - Doubly-ended heap (min-max heap) with O(log n) access to both minimum and maximum elements.
- [deque](https://github.com/edwingeng/deque) [![GitHub stars](https://img.shields.io/github/stars/edwingeng/deque?style=flat)](https://github.com/edwingeng/deque/stargazers) - A highly optimized double-ended queue.
- [deque](https://github.com/gammazero/deque) [![GitHub stars](https://img.shields.io/github/stars/gammazero/deque?style=flat)](https://github.com/gammazero/deque/stargazers) - Fast ring-buffer deque (double-ended queue).
- [dqueue](https://github.com/vodolaz095/dqueue) [![GitHub stars](https://img.shields.io/github/stars/vodolaz095/dqueue?style=flat)](https://github.com/vodolaz095/dqueue/stargazers) - Simple, in memory, zero dependency and battle tested, thread-safe deferred queue.
- [goconcurrentqueue](https://github.com/enriquebris/goconcurrentqueue) [![GitHub stars](https://img.shields.io/github/stars/enriquebris/goconcurrentqueue?style=flat)](https://github.com/enriquebris/goconcurrentqueue/stargazers) - Concurrent FIFO queue.
- [hatchet](https://github.com/hatchet-dev/hatchet) [![GitHub stars](https://img.shields.io/github/stars/hatchet-dev/hatchet?style=flat)](https://github.com/hatchet-dev/hatchet/stargazers) - Distributed, Fault-tolerant task queue.
- [list](https://github.com/koss-null/list) [![GitHub stars](https://img.shields.io/github/stars/koss-null/list?style=flat)](https://github.com/koss-null/list/stargazers) - A generic, thread-safe doubly linked list with full iterator support and an intrusive singly linked list for embedded use; a feature-rich replacement for container/list.
- [memlog](https://github.com/embano1/memlog) [![GitHub stars](https://img.shields.io/github/stars/embano1/memlog?style=flat)](https://github.com/embano1/memlog/stargazers) - An easy to use, lightweight, thread-safe and append-only in-memory data structure inspired by Apache Kafka.
- [queue](https://github.com/adrianbrad/queue) [![GitHub stars](https://img.shields.io/github/stars/adrianbrad/queue?style=flat)](https://github.com/adrianbrad/queue/stargazers) - Multiple thread-safe, generic queue implementations for Go.

### Sets

- [dsu](https://github.com/ihebu/dsu) [![GitHub stars](https://img.shields.io/github/stars/ihebu/dsu?style=flat)](https://github.com/ihebu/dsu/stargazers) - Disjoint Set data structure implementation in Go.
- [golang-set](https://github.com/deckarep/golang-set) [![GitHub stars](https://img.shields.io/github/stars/deckarep/golang-set?style=flat)](https://github.com/deckarep/golang-set/stargazers) - Thread-Safe and Non-Thread-Safe high-performance sets for Go.
- [goset](https://github.com/zoumo/goset) [![GitHub stars](https://img.shields.io/github/stars/zoumo/goset?style=flat)](https://github.com/zoumo/goset/stargazers) - A useful Set collection implementation for Go.
- [set](https://github.com/StudioSol/set) [![GitHub stars](https://img.shields.io/github/stars/StudioSol/set?style=flat)](https://github.com/StudioSol/set/stargazers) - Simple set data structure implementation in Go using LinkedHashMap.

### Text Analysis

- [bleve](https://github.com/blevesearch/bleve) [![GitHub stars](https://img.shields.io/github/stars/blevesearch/bleve?style=flat)](https://github.com/blevesearch/bleve/stargazers) - Modern text indexing library for go.
- [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) [![GitHub stars](https://img.shields.io/github/stars/plar/go-adaptive-radix-tree?style=flat)](https://github.com/plar/go-adaptive-radix-tree/stargazers) - Go implementation of Adaptive Radix Tree.
- [go-edlib](https://github.com/hbollon/go-edlib) [![GitHub stars](https://img.shields.io/github/stars/hbollon/go-edlib?style=flat)](https://github.com/hbollon/go-edlib/stargazers) - Go string comparison and edit distance algorithms library (Levenshtein, LCS, Hamming, Damerau levenshtein, Jaro-Winkler, etc.) compatible with Unicode.
- [levenshtein](https://github.com/agext/levenshtein) [![GitHub stars](https://img.shields.io/github/stars/agext/levenshtein?style=flat)](https://github.com/agext/levenshtein/stargazers) - Levenshtein distance and similarity metrics with customizable edit costs and Winkler-like bonus for common prefix.
- [levenshtein](https://github.com/agnivade/levenshtein) [![GitHub stars](https://img.shields.io/github/stars/agnivade/levenshtein?style=flat)](https://github.com/agnivade/levenshtein/stargazers) - Implementation to calculate levenshtein distance in Go.
- [mspm](https://github.com/BlackRabbitt/mspm) [![GitHub stars](https://img.shields.io/github/stars/BlackRabbitt/mspm?style=flat)](https://github.com/BlackRabbitt/mspm/stargazers) - Multi-String Pattern Matching Algorithm for information retrieval.
- [parsefields](https://github.com/MonaxGT/parsefields) [![GitHub stars](https://img.shields.io/github/stars/MonaxGT/parsefields?style=flat)](https://github.com/MonaxGT/parsefields/stargazers) - Tools for parse JSON-like logs for collecting unique fields and events.
- [ptrie](https://github.com/viant/ptrie) [![GitHub stars](https://img.shields.io/github/stars/viant/ptrie?style=flat)](https://github.com/viant/ptrie/stargazers) - An implementation of prefix tree.
- [radixtree](https://github.com/gammazero/radixtree) [![GitHub stars](https://img.shields.io/github/stars/gammazero/radixtree?style=flat)](https://github.com/gammazero/radixtree/stargazers) - Adaptive radix tree (prefix-tree or compact-trie).
- [trie](https://github.com/derekparker/trie) [![GitHub stars](https://img.shields.io/github/stars/derekparker/trie?style=flat)](https://github.com/derekparker/trie/stargazers) - Trie implementation in Go.

### Trees

- [graphlib](https://github.com/aio-arch/graphlib) [![GitHub stars](https://img.shields.io/github/stars/aio-arch/graphlib?style=flat)](https://github.com/aio-arch/graphlib/stargazers) - Topological sort lib,Sorting and pruning of DAG graphs.
- [hashsplit](http://github.com/bobg/hashsplit) - Split byte streams into chunks, and arrange chunks into trees, with boundaries determined by content, not position.
- [merkle](https://github.com/bobg/merkle) [![GitHub stars](https://img.shields.io/github/stars/bobg/merkle?style=flat)](https://github.com/bobg/merkle/stargazers) - Space-efficient computation of Merkle root hashes and inclusion proofs.
- [skiplist](https://github.com/MauriceGit/skiplist) [![GitHub stars](https://img.shields.io/github/stars/MauriceGit/skiplist?style=flat)](https://github.com/MauriceGit/skiplist/stargazers) - Very fast Go Skiplist implementation.
- [skiplist](https://github.com/gansidui/skiplist) [![GitHub stars](https://img.shields.io/github/stars/gansidui/skiplist?style=flat)](https://github.com/gansidui/skiplist/stargazers) - Skiplist implementation in Go.
- [treemap](https://github.com/igrmk/treemap) [![GitHub stars](https://img.shields.io/github/stars/igrmk/treemap?style=flat)](https://github.com/igrmk/treemap/stargazers) - Generic key-sorted map using a red-black tree under the hood.

### Pipes

- [ordered-concurrently](https://github.com/tejzpr/ordered-concurrently) [![GitHub stars](https://img.shields.io/github/stars/tejzpr/ordered-concurrently?style=flat)](https://github.com/tejzpr/ordered-concurrently/stargazers) - Go module that processes work concurrently and returns output in a channel in the order of input.
- [parapipe](https://github.com/nazar256/parapipe) [![GitHub stars](https://img.shields.io/github/stars/nazar256/parapipe?style=flat)](https://github.com/nazar256/parapipe/stargazers) - FIFO Pipeline which parallels execution on each stage while maintaining the order of messages and results.
- [pipeline](https://github.com/hyfather/pipeline) [![GitHub stars](https://img.shields.io/github/stars/hyfather/pipeline?style=flat)](https://github.com/hyfather/pipeline/stargazers) - An implementation of pipelines with fan-in and fan-out.
- [pipelines](https://github.com/nxdir-s/pipelines) [![GitHub stars](https://img.shields.io/github/stars/nxdir-s/pipelines?style=flat)](https://github.com/nxdir-s/pipelines/stargazers) - Generic pipeline functions for concurrent processing.

**[⬆ back to top](#contents)**

## Database

### Caches

_Data stores with expiring records, in-memory distributed data stores, or in-memory subsets of file-based databases._

- [bcache](https://github.com/iwanbk/bcache) [![GitHub stars](https://img.shields.io/github/stars/iwanbk/bcache?style=flat)](https://github.com/iwanbk/bcache/stargazers) - Eventually consistent distributed in-memory cache Go library.
- [BigCache](https://github.com/allegro/bigcache) [![GitHub stars](https://img.shields.io/github/stars/allegro/bigcache?style=flat)](https://github.com/allegro/bigcache/stargazers) - Efficient key/value cache for gigabytes of data.
- [cache2go](https://github.com/muesli/cache2go) [![GitHub stars](https://img.shields.io/github/stars/muesli/cache2go?style=flat)](https://github.com/muesli/cache2go/stargazers) - In-memory key:value cache which supports automatic invalidation based on timeouts.
- [cachego](https://github.com/faabiosr/cachego) [![GitHub stars](https://img.shields.io/github/stars/faabiosr/cachego?style=flat)](https://github.com/faabiosr/cachego/stargazers) - Golang Cache component for multiple drivers.
- [clusteredBigCache](https://github.com/oaStuff/clusteredBigCache) [![GitHub stars](https://img.shields.io/github/stars/oaStuff/clusteredBigCache?style=flat)](https://github.com/oaStuff/clusteredBigCache/stargazers) - BigCache with clustering support and individual item expiration.
- [coherence-go-client](https://github.com/oracle/coherence-go-client) [![GitHub stars](https://img.shields.io/github/stars/oracle/coherence-go-client?style=flat)](https://github.com/oracle/coherence-go-client/stargazers) - Full implementation of Oracle Coherence cache API for Go applications using gRPC as network transport.
- [couchcache](https://github.com/codingsince1985/couchcache) [![GitHub stars](https://img.shields.io/github/stars/codingsince1985/couchcache?style=flat)](https://github.com/codingsince1985/couchcache/stargazers) - RESTful caching micro-service backed by Couchbase server.
- [EchoVault](https://github.com/EchoVault/EchoVault) [![GitHub stars](https://img.shields.io/github/stars/EchoVault/EchoVault?style=flat)](https://github.com/EchoVault/EchoVault/stargazers) - Embeddable Distributed in-memory data store compatible with Redis clients.
- [fastcache](https://github.com/VictoriaMetrics/fastcache) [![GitHub stars](https://img.shields.io/github/stars/VictoriaMetrics/fastcache?style=flat)](https://github.com/VictoriaMetrics/fastcache/stargazers) - fast thread-safe inmemory cache for big number of entries. Minimizes GC overhead.
- [GCache](https://github.com/bluele/gcache) [![GitHub stars](https://img.shields.io/github/stars/bluele/gcache?style=flat)](https://github.com/bluele/gcache/stargazers) - Cache library with support for expirable Cache, LFU, LRU and ARC.
- [gdcache](https://github.com/ulovecode/gdcache) [![GitHub stars](https://img.shields.io/github/stars/ulovecode/gdcache?style=flat)](https://github.com/ulovecode/gdcache/stargazers) - A pure non-intrusive cache library implemented by golang, you can use it to implement your own distributed cache.
- [go-cache](https://github.com/viney-shih/go-cache) [![GitHub stars](https://img.shields.io/github/stars/viney-shih/go-cache?style=flat)](https://github.com/viney-shih/go-cache/stargazers) - A flexible multi-layer Go caching library to deal with in-memory and shared cache by adopting Cache-Aside pattern.
- [go-freelru](https://github.com/elastic/go-freelru) [![GitHub stars](https://img.shields.io/github/stars/elastic/go-freelru?style=flat)](https://github.com/elastic/go-freelru/stargazers) A GC-less, fast and generic LRU hashmap library with optional locking, sharding, eviction and expiration.
- [go-gcache](https://github.com/szyhf/go-gcache) [![GitHub stars](https://img.shields.io/github/stars/szyhf/go-gcache?style=flat)](https://github.com/szyhf/go-gcache/stargazers) - The generic version of `GCache`, cache support for expirable Cache, LFU, LRU and ARC.
- [go-mcache](https://github.com/OrlovEvgeny/go-mcache) [![GitHub stars](https://img.shields.io/github/stars/OrlovEvgeny/go-mcache?style=flat)](https://github.com/OrlovEvgeny/go-mcache/stargazers) - Fast in-memory key:value store/cache library. Pointer caches.
- [gocache](https://github.com/eko/gocache) [![GitHub stars](https://img.shields.io/github/stars/eko/gocache?style=flat)](https://github.com/eko/gocache/stargazers) - A complete Go cache library with multiple stores (memory, memcache, redis, ...), chainable, loadable, metrics cache and more.
- [gocache](https://github.com/yuseferi/gocache) [![GitHub stars](https://img.shields.io/github/stars/yuseferi/gocache?style=flat)](https://github.com/yuseferi/gocache/stargazers) - A data race free Go ache library with high performance and auto pruge functionality
- [groupcache](https://github.com/golang/groupcache) [![GitHub stars](https://img.shields.io/github/stars/golang/groupcache?style=flat)](https://github.com/golang/groupcache/stargazers) - Groupcache is a caching and cache-filling library, intended as a replacement for memcached in many cases.
- [icache](https://github.com/mdaliyan/icache) [![GitHub stars](https://img.shields.io/github/stars/mdaliyan/icache?style=flat)](https://github.com/mdaliyan/icache/stargazers) - A High Performance, Generic, thread-safe, zero-dependency cache package.
- [imcache](https://github.com/erni27/imcache) [![GitHub stars](https://img.shields.io/github/stars/erni27/imcache?style=flat)](https://github.com/erni27/imcache/stargazers) - A generic in-memory cache Go library. It supports expiration, sliding expiration, max entries limit, eviction callbacks and sharding.
- [jetcache-go](https://github.com/mgtv-tech/jetcache-go) [![GitHub stars](https://img.shields.io/github/stars/mgtv-tech/jetcache-go?style=flat)](https://github.com/mgtv-tech/jetcache-go/stargazers) - Unified Go cache library supporting multi-level caching.
- [nscache](https://github.com/no-src/nscache) [![GitHub stars](https://img.shields.io/github/stars/no-src/nscache?style=flat)](https://github.com/no-src/nscache/stargazers) - A Go caching framework that supports multiple data source drivers.
- [otter](https://github.com/maypok86/otter) [![GitHub stars](https://img.shields.io/github/stars/maypok86/otter?style=flat)](https://github.com/maypok86/otter/stargazers) - A high performance lockless cache for Go. Many times faster than Ristretto and friends.
- [pocache](https://github.com/naughtygopher/pocache) [![GitHub stars](https://img.shields.io/github/stars/naughtygopher/pocache?style=flat)](https://github.com/naughtygopher/pocache/stargazers) - Pocache is a minimal cache package which focuses on a preemptive optimistic caching strategy.
- [ristretto](https://github.com/dgraph-io/ristretto) [![GitHub stars](https://img.shields.io/github/stars/dgraph-io/ristretto?style=flat)](https://github.com/dgraph-io/ristretto/stargazers) - A high performance memory-bound Go cache.
- [sturdyc](https://github.com/viccon/sturdyc) [![GitHub stars](https://img.shields.io/github/stars/viccon/sturdyc?style=flat)](https://github.com/viccon/sturdyc/stargazers) - A caching library with advanced concurrency features designed to make I/O heavy applications robust and highly performant.
- [theine](https://github.com/Yiling-J/theine-go) [![GitHub stars](https://img.shields.io/github/stars/Yiling-J/theine-go?style=flat)](https://github.com/Yiling-J/theine-go/stargazers) - High performance, near optimal in-memory cache with proactive TTL expiration and generics.
- [timedmap](https://github.com/zekroTJA/timedmap) [![GitHub stars](https://img.shields.io/github/stars/zekroTJA/timedmap?style=flat)](https://github.com/zekroTJA/timedmap/stargazers) - Map with expiring key-value pairs.
- [ttlcache](https://github.com/jellydator/ttlcache) [![GitHub stars](https://img.shields.io/github/stars/jellydator/ttlcache?style=flat)](https://github.com/jellydator/ttlcache/stargazers) - An in-memory cache with item expiration and generics.
- [ttlcache](https://github.com/cheshir/ttlcache) [![GitHub stars](https://img.shields.io/github/stars/cheshir/ttlcache?style=flat)](https://github.com/cheshir/ttlcache/stargazers) - In-memory key value storage with TTL for each record.

### Databases Implemented in Go

- [badger](https://github.com/dgraph-io/badger) [![GitHub stars](https://img.shields.io/github/stars/dgraph-io/badger?style=flat)](https://github.com/dgraph-io/badger/stargazers) - Fast key-value store in Go.
- [bbolt](https://github.com/etcd-io/bbolt) [![GitHub stars](https://img.shields.io/github/stars/etcd-io/bbolt?style=flat)](https://github.com/etcd-io/bbolt/stargazers) - An embedded key/value database for Go.
- [Bitcask](https://git.mills.io/prologic/bitcask) - Bitcask is an embeddable, persistent and fast key-value (KV) database written in pure Go with predictable read/write performance, low latency and high throughput thanks to the bitcask on-disk layout (LSM+WAL).
- [buntdb](https://github.com/tidwall/buntdb) [![GitHub stars](https://img.shields.io/github/stars/tidwall/buntdb?style=flat)](https://github.com/tidwall/buntdb/stargazers) - Fast, embeddable, in-memory key/value database for Go with custom indexing and spatial support.
- [clover](https://github.com/ostafen/clover) [![GitHub stars](https://img.shields.io/github/stars/ostafen/clover?style=flat)](https://github.com/ostafen/clover/stargazers) - A lightweight document-oriented NoSQL database written in pure Golang.
- [cockroach](https://github.com/cockroachdb/cockroach) [![GitHub stars](https://img.shields.io/github/stars/cockroachdb/cockroach?style=flat)](https://github.com/cockroachdb/cockroach/stargazers) - Scalable, Geo-Replicated, Transactional Datastore.
- [Coffer](https://github.com/claygod/coffer) [![GitHub stars](https://img.shields.io/github/stars/claygod/coffer?style=flat)](https://github.com/claygod/coffer/stargazers) - Simple ACID key-value database that supports transactions.
- [column](https://github.com/kelindar/column) [![GitHub stars](https://img.shields.io/github/stars/kelindar/column?style=flat)](https://github.com/kelindar/column/stargazers) - High-performance, columnar, embeddable in-memory store with bitmap indexing and transactions.
- [CovenantSQL](https://github.com/CovenantSQL/CovenantSQL) [![GitHub stars](https://img.shields.io/github/stars/CovenantSQL/CovenantSQL?style=flat)](https://github.com/CovenantSQL/CovenantSQL/stargazers) - CovenantSQL is a SQL database on blockchain.
- [Databunker](https://github.com/paranoidguy/databunker) [![GitHub stars](https://img.shields.io/github/stars/paranoidguy/databunker?style=flat)](https://github.com/paranoidguy/databunker/stargazers) - Personally identifiable information (PII) storage service built to comply with GDPR and CCPA.
- [dgraph](https://github.com/dgraph-io/dgraph) [![GitHub stars](https://img.shields.io/github/stars/dgraph-io/dgraph?style=flat)](https://github.com/dgraph-io/dgraph/stargazers) - Scalable, Distributed, Low Latency, High Throughput Graph Database.
- [DiceDB](https://github.com/DiceDB/dice) [![GitHub stars](https://img.shields.io/github/stars/DiceDB/dice?style=flat)](https://github.com/DiceDB/dice/stargazers) - An open-source, fast, reactive, in-memory database optimized for modern hardware. Higher throughput and lower median latencies, making it ideal for modern workloads.
- [diskv](https://github.com/peterbourgon/diskv) [![GitHub stars](https://img.shields.io/github/stars/peterbourgon/diskv?style=flat)](https://github.com/peterbourgon/diskv/stargazers) - Home-grown disk-backed key-value store.
- [dolt](https://github.com/dolthub/dolt) [![GitHub stars](https://img.shields.io/github/stars/dolthub/dolt?style=flat)](https://github.com/dolthub/dolt/stargazers) - Dolt – It's Git for Data.
- [eliasdb](https://github.com/krotik/eliasdb) [![GitHub stars](https://img.shields.io/github/stars/krotik/eliasdb?style=flat)](https://github.com/krotik/eliasdb/stargazers) - Dependency-free, transactional graph database with REST API, phrase search and SQL-like query language.
- [go-sqlite](https://github.com/glebarez/go-sqlite) [![GitHub stars](https://img.shields.io/github/stars/glebarez/go-sqlite?style=flat)](https://github.com/glebarez/go-sqlite/stargazers) – A Pure Golang implemented SQLite driver without CGO.
- [godis](https://github.com/hdt3213/godis) [![GitHub stars](https://img.shields.io/github/stars/hdt3213/godis?style=flat)](https://github.com/hdt3213/godis/stargazers) - A Golang implemented high-performance Redis server and cluster.
- [goleveldb](https://github.com/syndtr/goleveldb) [![GitHub stars](https://img.shields.io/github/stars/syndtr/goleveldb?style=flat)](https://github.com/syndtr/goleveldb/stargazers) - Implementation of the [LevelDB](https://github.com/google/leveldb) [![GitHub stars](https://img.shields.io/github/stars/google/leveldb?style=flat)](https://github.com/google/leveldb/stargazers) key/value database in Go.
- [hare](https://github.com/jameycribbs/hare) [![GitHub stars](https://img.shields.io/github/stars/jameycribbs/hare?style=flat)](https://github.com/jameycribbs/hare/stargazers) - A simple database management system that stores each table as a text file of line-delimited JSON.
- [immudb](https://github.com/codenotary/immudb) [![GitHub stars](https://img.shields.io/github/stars/codenotary/immudb?style=flat)](https://github.com/codenotary/immudb/stargazers) - immudb is a lightweight, high-speed immutable database for systems and applications written in Go.
- [influxdb](https://github.com/influxdb/influxdb) [![GitHub stars](https://img.shields.io/github/stars/influxdb/influxdb?style=flat)](https://github.com/influxdb/influxdb/stargazers) - Scalable datastore for metrics, events, and real-time analytics.
- [ledisdb](https://github.com/siddontang/ledisdb) [![GitHub stars](https://img.shields.io/github/stars/siddontang/ledisdb?style=flat)](https://github.com/siddontang/ledisdb/stargazers) - Ledisdb is a high performance NoSQL like Redis based on LevelDB.
- [levigo](https://github.com/jmhodges/levigo) [![GitHub stars](https://img.shields.io/github/stars/jmhodges/levigo?style=flat)](https://github.com/jmhodges/levigo/stargazers) - Levigo is a Go wrapper for LevelDB.
- [libradb](https://github.com/amit-davidson/LibraDB) [![GitHub stars](https://img.shields.io/github/stars/amit-davidson/LibraDB?style=flat)](https://github.com/amit-davidson/LibraDB/stargazers) - LibraDB is a simple database with less than 1000 lines of code for learning.
- [LinDB](https://github.com/lindb/lindb) [![GitHub stars](https://img.shields.io/github/stars/lindb/lindb?style=flat)](https://github.com/lindb/lindb/stargazers) - LinDB is a scalable, high performance, high availability distributed time series database.
- [lotusdb](https://github.com/flower-corp/lotusdb) [![GitHub stars](https://img.shields.io/github/stars/flower-corp/lotusdb?style=flat)](https://github.com/flower-corp/lotusdb/stargazers) - Fast k/v database compatible with lsm and b+tree.
- [lynxdb](https://github.com/lynxbase/lynxdb) [![GitHub stars](https://img.shields.io/github/stars/lynxbase/lynxdb?style=flat)](https://github.com/lynxbase/lynxdb/stargazers) - Lightweight columnar log analytics database with a pipe-style query language inspired by SPL.
- [Milvus](https://github.com/milvus-io/milvus) [![GitHub stars](https://img.shields.io/github/stars/milvus-io/milvus?style=flat)](https://github.com/milvus-io/milvus/stargazers) - Milvus is a vector database for embedding management, analytics and search.
- [minisql](https://github.com/RichardKnop/minisql) [![GitHub stars](https://img.shields.io/github/stars/RichardKnop/minisql?style=flat)](https://github.com/RichardKnop/minisql/stargazers) - Embedded single file SQL database.
- [moss](https://github.com/couchbase/moss) [![GitHub stars](https://img.shields.io/github/stars/couchbase/moss?style=flat)](https://github.com/couchbase/moss/stargazers) - Moss is a simple LSM key-value storage engine written in 100% Go.
- [nanotdb](https://github.com/aymanhs/nanotdb) [![GitHub stars](https://img.shields.io/github/stars/aymanhs/nanotdb?style=flat)](https://github.com/aymanhs/nanotdb/stargazers) - A lightweight, zero-dependency, append-only Time-Series Database and Dashboard optimized for low-power hardware.
- [NoKV](https://github.com/feichai0017/NoKV) [![GitHub stars](https://img.shields.io/github/stars/feichai0017/NoKV?style=flat)](https://github.com/feichai0017/NoKV/stargazers) - Native metadata service for distributed filesystems, object storage, and AI dataset workloads.
- [NornicDB](https://github.com/orneryd/NornicDB) [![GitHub stars](https://img.shields.io/github/stars/orneryd/NornicDB?style=flat)](https://github.com/orneryd/NornicDB/stargazers) - High performance graph + vector database (Neo4j and qDrant compatible), focused on low latency graph-rag retreival for AI systems. 
- [nutsdb](https://github.com/xujiajun/nutsdb) [![GitHub stars](https://img.shields.io/github/stars/xujiajun/nutsdb?style=flat)](https://github.com/xujiajun/nutsdb/stargazers) - Nutsdb is a simple, fast, embeddable, persistent key/value store written in pure Go. It supports fully serializable transactions and many data structures such as list, set, sorted set.
- [objectbox-go](https://github.com/objectbox/objectbox-go) [![GitHub stars](https://img.shields.io/github/stars/objectbox/objectbox-go?style=flat)](https://github.com/objectbox/objectbox-go/stargazers) - High-performance embedded Object Database (NoSQL) with Go API.
- [pebble](https://github.com/cockroachdb/pebble) [![GitHub stars](https://img.shields.io/github/stars/cockroachdb/pebble?style=flat)](https://github.com/cockroachdb/pebble/stargazers) - RocksDB/LevelDB inspired key-value database in Go.
- [piladb](https://github.com/fern4lvarez/piladb) [![GitHub stars](https://img.shields.io/github/stars/fern4lvarez/piladb?style=flat)](https://github.com/fern4lvarez/piladb/stargazers) - Lightweight RESTful database engine based on stack data structures.
- [pogreb](https://github.com/akrylysov/pogreb) [![GitHub stars](https://img.shields.io/github/stars/akrylysov/pogreb?style=flat)](https://github.com/akrylysov/pogreb/stargazers) - Embedded key-value store for read-heavy workloads.
- [prometheus](https://github.com/prometheus/prometheus) [![GitHub stars](https://img.shields.io/github/stars/prometheus/prometheus?style=flat)](https://github.com/prometheus/prometheus/stargazers) - Monitoring system and time series database.
- [pudge](https://github.com/recoilme/pudge) [![GitHub stars](https://img.shields.io/github/stars/recoilme/pudge?style=flat)](https://github.com/recoilme/pudge/stargazers) - Fast and simple key/value store written using Go's standard library.
- [redka](https://github.com/nalgeon/redka) [![GitHub stars](https://img.shields.io/github/stars/nalgeon/redka?style=flat)](https://github.com/nalgeon/redka/stargazers) - Redis re-implemented with SQLite.
- [rosedb](https://github.com/roseduan/rosedb) [![GitHub stars](https://img.shields.io/github/stars/roseduan/rosedb?style=flat)](https://github.com/roseduan/rosedb/stargazers) - An embedded k-v database based on LSM+WAL, supports string, list, hash, set, zset.
- [rotom](https://github.com/xgzlucario/rotom) [![GitHub stars](https://img.shields.io/github/stars/xgzlucario/rotom?style=flat)](https://github.com/xgzlucario/rotom/stargazers) - A tiny Redis server built with Golang, compatible with RESP protocols.
- [rqlite](https://github.com/rqlite/rqlite) [![GitHub stars](https://img.shields.io/github/stars/rqlite/rqlite?style=flat)](https://github.com/rqlite/rqlite/stargazers) - The lightweight, distributed, relational database built on SQLite.
- [tempdb](https://github.com/rafaeljesus/tempdb) [![GitHub stars](https://img.shields.io/github/stars/rafaeljesus/tempdb?style=flat)](https://github.com/rafaeljesus/tempdb/stargazers) - Key-value store for temporary items.
- [tidb](https://github.com/pingcap/tidb) [![GitHub stars](https://img.shields.io/github/stars/pingcap/tidb?style=flat)](https://github.com/pingcap/tidb/stargazers) - TiDB is a distributed SQL database. Inspired by the design of Google F1.
- [tiedot](https://github.com/HouzuoGuo/tiedot) [![GitHub stars](https://img.shields.io/github/stars/HouzuoGuo/tiedot?style=flat)](https://github.com/HouzuoGuo/tiedot/stargazers) - Your NoSQL database powered by Golang.
- [unitdb](https://github.com/unit-io/unitdb) [![GitHub stars](https://img.shields.io/github/stars/unit-io/unitdb?style=flat)](https://github.com/unit-io/unitdb/stargazers) - Fast timeseries database for IoT, realtime messaging applications. Access unitdb with pubsub over tcp or websocket using github.com/unit-io/unitd application.
- [Vasto](https://github.com/chrislusf/vasto) [![GitHub stars](https://img.shields.io/github/stars/chrislusf/vasto?style=flat)](https://github.com/chrislusf/vasto/stargazers) - A distributed high-performance key-value store. On Disk. Eventual consistent. HA. Able to grow or shrink without service interruption.
- [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) [![GitHub stars](https://img.shields.io/github/stars/VictoriaMetrics/VictoriaMetrics?style=flat)](https://github.com/VictoriaMetrics/VictoriaMetrics/stargazers) - fast, resource-effective and scalable open source time series database. May be used as long-term remote storage for Prometheus. Supports PromQL.
- 
### Database Schema Migration

- [atlas](https://github.com/ariga/atlas) [![GitHub stars](https://img.shields.io/github/stars/ariga/atlas?style=flat)](https://github.com/ariga/atlas/stargazers) - A Database Toolkit. A CLI designed to help companies better work with their data.
- [avro](https://github.com/khezen/avro) [![GitHub stars](https://img.shields.io/github/stars/khezen/avro?style=flat)](https://github.com/khezen/avro/stargazers) - Discover SQL schemas and convert them to AVRO schemas. Query SQL records into AVRO bytes.
- [bytebase](https://github.com/bytebase/bytebase) [![GitHub stars](https://img.shields.io/github/stars/bytebase/bytebase?style=flat)](https://github.com/bytebase/bytebase/stargazers) - Safe database schema change and version control for DevOps teams.
- [darwin](https://github.com/GuiaBolso/darwin) [![GitHub stars](https://img.shields.io/github/stars/GuiaBolso/darwin?style=flat)](https://github.com/GuiaBolso/darwin/stargazers) - Database schema evolution library for Go.
- [dbmate](https://github.com/amacneil/dbmate) [![GitHub stars](https://img.shields.io/github/stars/amacneil/dbmate?style=flat)](https://github.com/amacneil/dbmate/stargazers) - A lightweight, framework-agnostic database migration tool.
- [go-fixtures](https://github.com/RichardKnop/go-fixtures) [![GitHub stars](https://img.shields.io/github/stars/RichardKnop/go-fixtures?style=flat)](https://github.com/RichardKnop/go-fixtures/stargazers) - Django style fixtures for Golang's excellent built-in database/sql library.
- [go-pg-migrate](https://github.com/lawzava/go-pg-migrate) [![GitHub stars](https://img.shields.io/github/stars/lawzava/go-pg-migrate?style=flat)](https://github.com/lawzava/go-pg-migrate/stargazers) - CLI-friendly package for go-pg migrations management.
- [go-pg-migrations](https://github.com/robinjoseph08/go-pg-migrations) [![GitHub stars](https://img.shields.io/github/stars/robinjoseph08/go-pg-migrations?style=flat)](https://github.com/robinjoseph08/go-pg-migrations/stargazers) - A Go package to help write migrations with go-pg/pg.
- [goavro](https://github.com/linkedin/goavro) [![GitHub stars](https://img.shields.io/github/stars/linkedin/goavro?style=flat)](https://github.com/linkedin/goavro/stargazers) - A Go package that encodes and decodes Avro data.
- [godfish](https://github.com/rafaelespinoza/godfish) [![GitHub stars](https://img.shields.io/github/stars/rafaelespinoza/godfish?style=flat)](https://github.com/rafaelespinoza/godfish/stargazers) - Database migration manager, works with native query language. Support for cassandra, mysql, postgres, sqlite3.
- [goose](https://github.com/pressly/goose) [![GitHub stars](https://img.shields.io/github/stars/pressly/goose?style=flat)](https://github.com/pressly/goose/stargazers) - Database migration tool. You can manage your database's evolution by creating incremental SQL or Go scripts.
- [gorm-seeder](https://github.com/Kachit/gorm-seeder) [![GitHub stars](https://img.shields.io/github/stars/Kachit/gorm-seeder?style=flat)](https://github.com/Kachit/gorm-seeder/stargazers) - Simple database seeder for Gorm ORM.
- [gormigrate](https://github.com/go-gormigrate/gormigrate) [![GitHub stars](https://img.shields.io/github/stars/go-gormigrate/gormigrate?style=flat)](https://github.com/go-gormigrate/gormigrate/stargazers) - Database schema migration helper for Gorm ORM.
- [libschema](https://github.com/muir/libschema) [![GitHub stars](https://img.shields.io/github/stars/muir/libschema?style=flat)](https://github.com/muir/libschema/stargazers) - Define your migrations separately in each library. Migrations for open source libraries. MySQL & PostgreSQL.
- [migrate](https://github.com/golang-migrate/migrate) [![GitHub stars](https://img.shields.io/github/stars/golang-migrate/migrate?style=flat)](https://github.com/golang-migrate/migrate/stargazers) - Database migrations. CLI and Golang library.
- [migrator](https://github.com/lopezator/migrator) [![GitHub stars](https://img.shields.io/github/stars/lopezator/migrator?style=flat)](https://github.com/lopezator/migrator/stargazers) - Dead simple Go database migration library.
- [migrator](https://github.com/larapulse/migrator) [![GitHub stars](https://img.shields.io/github/stars/larapulse/migrator?style=flat)](https://github.com/larapulse/migrator/stargazers) - MySQL database migrator designed to run migrations to your features and manage database schema update with intuitive go code.
- [schema](https://github.com/adlio/schema) [![GitHub stars](https://img.shields.io/github/stars/adlio/schema?style=flat)](https://github.com/adlio/schema/stargazers) - Library to embed schema migrations for database/sql-compatible databases inside your Go binaries.
- [skeema](https://github.com/skeema/skeema) [![GitHub stars](https://img.shields.io/github/stars/skeema/skeema?style=flat)](https://github.com/skeema/skeema/stargazers) - Pure-SQL schema management system for MySQL, with support for sharding and external online schema change tools.
- [soda](https://github.com/gobuffalo/pop/tree/master/soda) [![GitHub stars](https://img.shields.io/github/stars/gobuffalo/pop/tree/master/soda?style=flat)](https://github.com/gobuffalo/pop/tree/master/soda/stargazers) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.
- [sql-migrate](https://github.com/rubenv/sql-migrate) [![GitHub stars](https://img.shields.io/github/stars/rubenv/sql-migrate?style=flat)](https://github.com/rubenv/sql-migrate/stargazers) - Database migration tool. Allows embedding migrations into the application using go-bindata.
- [sqlize](https://github.com/sunary/sqlize) [![GitHub stars](https://img.shields.io/github/stars/sunary/sqlize?style=flat)](https://github.com/sunary/sqlize/stargazers) - Database migration generator. Allows generate sql migration from model and existing sql by differ them.

### Database Tools

- [chproxy](https://github.com/Vertamedia/chproxy) [![GitHub stars](https://img.shields.io/github/stars/Vertamedia/chproxy?style=flat)](https://github.com/Vertamedia/chproxy/stargazers) - HTTP proxy for ClickHouse database.
- [clickhouse-bulk](https://github.com/nikepan/clickhouse-bulk) [![GitHub stars](https://img.shields.io/github/stars/nikepan/clickhouse-bulk?style=flat)](https://github.com/nikepan/clickhouse-bulk/stargazers) - Collects small inserts and sends big requests to ClickHouse servers.
- [database-gateway](https://github.com/kazhuravlev/database-gateway) [![GitHub stars](https://img.shields.io/github/stars/kazhuravlev/database-gateway?style=flat)](https://github.com/kazhuravlev/database-gateway/stargazers) - Running SQL in production with ACLs, logs, and shared links.
- [dbbench](https://github.com/sj14/dbbench) [![GitHub stars](https://img.shields.io/github/stars/sj14/dbbench?style=flat)](https://github.com/sj14/dbbench/stargazers) - Database benchmarking tool with support for several databases and scripts.
- [dg](https://github.com/codingconcepts/dg) [![GitHub stars](https://img.shields.io/github/stars/codingconcepts/dg?style=flat)](https://github.com/codingconcepts/dg/stargazers) - A fast data generator that produces CSV files from generated relational data.
- [gatewayd](https://github.com/gatewayd-io/gatewayd) [![GitHub stars](https://img.shields.io/github/stars/gatewayd-io/gatewayd?style=flat)](https://github.com/gatewayd-io/gatewayd/stargazers) - Cloud-native database gateway and framework for building data-driven applications. Like API gateways, for databases.
- [go-mysql](https://github.com/siddontang/go-mysql) [![GitHub stars](https://img.shields.io/github/stars/siddontang/go-mysql?style=flat)](https://github.com/siddontang/go-mysql/stargazers) - Go toolset to handle MySQL protocol and replication.
- [go-postgres-s3-backup](https://github.com/nicobistolfi/go-postgres-s3-backup) [![GitHub stars](https://img.shields.io/github/stars/nicobistolfi/go-postgres-s3-backup?style=flat)](https://github.com/nicobistolfi/go-postgres-s3-backup/stargazers) - Serverless PostgreSQL backups to S3 using AWS Lambda, with daily, monthly, and yearly rotation.
- [gorm-multitenancy](https://github.com/bartventer/gorm-multitenancy) [![GitHub stars](https://img.shields.io/github/stars/bartventer/gorm-multitenancy?style=flat)](https://github.com/bartventer/gorm-multitenancy/stargazers) - Multi-tenancy support for GORM managed databases.
- [GoSQLX](https://github.com/ajitpratap0/GoSQLX) [![GitHub stars](https://img.shields.io/github/stars/ajitpratap0/GoSQLX?style=flat)](https://github.com/ajitpratap0/GoSQLX/stargazers) - High-performance SQL parser, formatter, linter, and security scanner with multi-dialect support and WASM playground.
- [hasql](https://golang.yandex/hasql) - Library for accessing multi-host SQL database installations.
- [octillery](https://github.com/knocknote/octillery) [![GitHub stars](https://img.shields.io/github/stars/knocknote/octillery?style=flat)](https://github.com/knocknote/octillery/stargazers) - Go package for sharding databases ( Supports every ORM or raw SQL ).
- [onedump](https://github.com/liweiyi88/onedump) [![GitHub stars](https://img.shields.io/github/stars/liweiyi88/onedump?style=flat)](https://github.com/liweiyi88/onedump/stargazers) - Database backup from different drivers to different destinations with one command and configuration.
- [pg_timetable](https://github.com/cybertec-postgresql/pg_timetable) [![GitHub stars](https://img.shields.io/github/stars/cybertec-postgresql/pg_timetable?style=flat)](https://github.com/cybertec-postgresql/pg_timetable/stargazers) - Advanced scheduling for PostgreSQL.
- [pgrwl](https://github.com/pgrwl/pgrwl) [![GitHub stars](https://img.shields.io/github/stars/pgrwl/pgrwl?style=flat)](https://github.com/pgrwl/pgrwl/stargazers) - Cloud-native continuous backup for PostgreSQL.
- [pgweb](https://github.com/sosedoff/pgweb) [![GitHub stars](https://img.shields.io/github/stars/sosedoff/pgweb?style=flat)](https://github.com/sosedoff/pgweb/stargazers) - Web-based PostgreSQL database browser.
- [pgxcli](https://github.com/Balaji01-4D/pgxcli) [![GitHub stars](https://img.shields.io/github/stars/Balaji01-4D/pgxcli?style=flat)](https://github.com/Balaji01-4D/pgxcli/stargazers) - PostgreSQL CLI client written in Go, inspired by pgcli.
- [prep](https://github.com/hexdigest/prep) [![GitHub stars](https://img.shields.io/github/stars/hexdigest/prep?style=flat)](https://github.com/hexdigest/prep/stargazers) - Use prepared SQL statements without changing your code.
- [pREST](https://github.com/prest/prest) [![GitHub stars](https://img.shields.io/github/stars/prest/prest?style=flat)](https://github.com/prest/prest/stargazers) - Simplify and accelerate development, ⚡ instant, realtime, high-performance on any Postgres application, existing or new.
- [rdb](https://github.com/HDT3213/rdb) [![GitHub stars](https://img.shields.io/github/stars/HDT3213/rdb?style=flat)](https://github.com/HDT3213/rdb/stargazers) - Redis RDB file parser for secondary development and memory analysis.
- [rwdb](https://github.com/andizzle/rwdb) [![GitHub stars](https://img.shields.io/github/stars/andizzle/rwdb?style=flat)](https://github.com/andizzle/rwdb/stargazers) - rwdb provides read replica capability for multiple database servers setup.
- [vitess](https://github.com/youtube/vitess) [![GitHub stars](https://img.shields.io/github/stars/youtube/vitess?style=flat)](https://github.com/youtube/vitess/stargazers) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.
- [wescale](https://github.com/wesql/wescale) [![GitHub stars](https://img.shields.io/github/stars/wesql/wescale?style=flat)](https://github.com/wesql/wescale/stargazers) - WeScale is a database proxy designed to enhance the scalability, performance, security, and resilience of your applications.

### SQL Query Builders

_Libraries for building and using SQL._

- [bqb](https://github.com/nullism/bqb) [![GitHub stars](https://img.shields.io/github/stars/nullism/bqb?style=flat)](https://github.com/nullism/bqb/stargazers) - Lightweight and easy to learn query builder.
- [buildsqlx](https://github.com/arthurkushman/buildsqlx) [![GitHub stars](https://img.shields.io/github/stars/arthurkushman/buildsqlx?style=flat)](https://github.com/arthurkushman/buildsqlx/stargazers) - Go database query builder library for PostgreSQL.
- [builq](https://github.com/cristalhq/builq) [![GitHub stars](https://img.shields.io/github/stars/cristalhq/builq?style=flat)](https://github.com/cristalhq/builq/stargazers) - Easily build SQL queries in Go.
- [dbq](https://github.com/rocketlaunchr/dbq) [![GitHub stars](https://img.shields.io/github/stars/rocketlaunchr/dbq?style=flat)](https://github.com/rocketlaunchr/dbq/stargazers) - Zero boilerplate database operations for Go.
- [Dotsql](https://github.com/gchaincl/dotsql) [![GitHub stars](https://img.shields.io/github/stars/gchaincl/dotsql?style=flat)](https://github.com/gchaincl/dotsql/stargazers) - Go library that helps you keep sql files in one place and use them with ease.
- [gendry](https://github.com/didi/gendry) [![GitHub stars](https://img.shields.io/github/stars/didi/gendry?style=flat)](https://github.com/didi/gendry/stargazers) - Non-invasive SQL builder and powerful data binder.
- [godbal](https://github.com/xujiajun/godbal) [![GitHub stars](https://img.shields.io/github/stars/xujiajun/godbal?style=flat)](https://github.com/xujiajun/godbal/stargazers) - Database Abstraction Layer (dbal) for go. Support SQL builder and get result easily.
- [goqu](https://github.com/doug-martin/goqu) [![GitHub stars](https://img.shields.io/github/stars/doug-martin/goqu?style=flat)](https://github.com/doug-martin/goqu/stargazers) - Idiomatic SQL builder and query library.
- [gosql](https://github.com/twharmon/gosql) [![GitHub stars](https://img.shields.io/github/stars/twharmon/gosql?style=flat)](https://github.com/twharmon/gosql/stargazers) - SQL Query builder with better null values support.
- [Hotcoal](https://github.com/motrboat/hotcoal) [![GitHub stars](https://img.shields.io/github/stars/motrboat/hotcoal?style=flat)](https://github.com/motrboat/hotcoal/stargazers) - Secure your handcrafted SQL against injection.
- [igor](https://github.com/galeone/igor) [![GitHub stars](https://img.shields.io/github/stars/galeone/igor?style=flat)](https://github.com/galeone/igor/stargazers) - Abstraction layer for PostgreSQL that supports advanced functionality and uses gorm-like syntax.
- [jet](https://github.com/go-jet/jet) [![GitHub stars](https://img.shields.io/github/stars/go-jet/jet?style=flat)](https://github.com/go-jet/jet/stargazers) - Framework for writing type-safe SQL queries in Go, with ability to easily convert database query result into desired arbitrary object structure.
- [obreron](https://github.com/profe-ajedrez/obreron) [![GitHub stars](https://img.shields.io/github/stars/profe-ajedrez/obreron?style=flat)](https://github.com/profe-ajedrez/obreron/stargazers) - Fast and cheap SQL builder which does only one thing, SQL building.
- [ormlite](https://github.com/pupizoid/ormlite) [![GitHub stars](https://img.shields.io/github/stars/pupizoid/ormlite?style=flat)](https://github.com/pupizoid/ormlite/stargazers) - Lightweight package containing some ORM-like features and helpers for sqlite databases.
- [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) [![GitHub stars](https://img.shields.io/github/stars/go-ozzo/ozzo-dbx?style=flat)](https://github.com/go-ozzo/ozzo-dbx/stargazers) - Powerful data retrieval methods as well as DB-agnostic query building capabilities.
- [patcher](https://github.com/Jacobbrewer1/patcher) [![GitHub stars](https://img.shields.io/github/stars/Jacobbrewer1/patcher?style=flat)](https://github.com/Jacobbrewer1/patcher/stargazers) - Powerful SQL Query builder that automatically generates SQL queries from structs.
- [qrafter](https://github.com/SennovE/qrafter) [![GitHub stars](https://img.shields.io/github/stars/SennovE/qrafter?style=flat)](https://github.com/SennovE/qrafter/stargazers) - Type-safe SQL query builder with dialect-aware rendering, schema introspection, and migration generation.
- [qry](https://github.com/HnH/qry) [![GitHub stars](https://img.shields.io/github/stars/HnH/qry?style=flat)](https://github.com/HnH/qry/stargazers) - Tool that generates constants from files with raw SQL queries.
- [relica](https://github.com/coregx/relica) [![GitHub stars](https://img.shields.io/github/stars/coregx/relica?style=flat)](https://github.com/coregx/relica/stargazers) - Type-safe database query builder with zero production dependencies, LRU statement cache, batch operations, and support for JOINs, subqueries, CTEs, and window functions.
- [sg](https://github.com/go-the-way/sg) [![GitHub stars](https://img.shields.io/github/stars/go-the-way/sg?style=flat)](https://github.com/go-the-way/sg/stargazers) - A SQL Gen for generating standard SQLs(supports: CRUD) written in Go.
- [sq](https://github.com/bokwoon95/go-structured-query) [![GitHub stars](https://img.shields.io/github/stars/bokwoon95/go-structured-query?style=flat)](https://github.com/bokwoon95/go-structured-query/stargazers) - Type-safe SQL builder and struct mapper for Go.
- [sqlc](https://github.com/kyleconroy/sqlc) [![GitHub stars](https://img.shields.io/github/stars/kyleconroy/sqlc?style=flat)](https://github.com/kyleconroy/sqlc/stargazers) - Generate type-safe code from SQL.
- [sqlf](https://github.com/leporo/sqlf) [![GitHub stars](https://img.shields.io/github/stars/leporo/sqlf?style=flat)](https://github.com/leporo/sqlf/stargazers) - Fast SQL query builder.
- [sqlh](https://github.com/kirill-scherba/sqlh) [![GitHub stars](https://img.shields.io/github/stars/kirill-scherba/sqlh?style=flat)](https://github.com/kirill-scherba/sqlh/stargazers) - Zero-boilerplate SQL helper with struct tags and Go generics (CRUD, UPSERT, JOIN, benchmarks).
- [sqlingo](https://github.com/lqs/sqlingo) [![GitHub stars](https://img.shields.io/github/stars/lqs/sqlingo?style=flat)](https://github.com/lqs/sqlingo/stargazers) - A lightweight DSL to build SQL in Go.
- [sqrl](https://github.com/elgris/sqrl) [![GitHub stars](https://img.shields.io/github/stars/elgris/sqrl?style=flat)](https://github.com/elgris/sqrl/stargazers) - SQL query builder, fork of Squirrel with improved performance.
- [Squalus](https://gitlab.com/qosenergy/squalus) - Thin layer over the Go SQL package that makes it easier to perform queries.
- [Squirrel](https://github.com/Masterminds/squirrel) [![GitHub stars](https://img.shields.io/github/stars/Masterminds/squirrel?style=flat)](https://github.com/Masterminds/squirrel/stargazers) - Go library that helps you build SQL queries.
- [xo](https://github.com/knq/xo) [![GitHub stars](https://img.shields.io/github/stars/knq/xo?style=flat)](https://github.com/knq/xo/stargazers) - Generate idiomatic Go code for databases based on existing schema definitions or custom queries supporting PostgreSQL, MySQL, SQLite, Oracle, and Microsoft SQL Server.

**[⬆ back to top](#contents)**

## Database Drivers

### Interfaces to Multiple Backends

- [cayley](https://github.com/google/cayley) [![GitHub stars](https://img.shields.io/github/stars/google/cayley?style=flat)](https://github.com/google/cayley/stargazers) - Graph database with support for multiple backends.
- [dsc](https://github.com/viant/dsc) [![GitHub stars](https://img.shields.io/github/stars/viant/dsc?style=flat)](https://github.com/viant/dsc/stargazers) - Datastore connectivity for SQL, NoSQL, structured files.
- [dynamo](https://github.com/fogfish/dynamo) [![GitHub stars](https://img.shields.io/github/stars/fogfish/dynamo?style=flat)](https://github.com/fogfish/dynamo/stargazers) - A simple key-value abstraction to store algebraic and linked-data data types at AWS storage services: AWS DynamoDB and AWS S3.
- [go-transaction-manager](https://github.com/avito-tech/go-transaction-manager) [![GitHub stars](https://img.shields.io/github/stars/avito-tech/go-transaction-manager?style=flat)](https://github.com/avito-tech/go-transaction-manager/stargazers) - Transaction manager with multiple adapters (sql, sqlx, gorm, mongo, ...) controls transaction boundaries.
- [gokv](https://github.com/philippgille/gokv) [![GitHub stars](https://img.shields.io/github/stars/philippgille/gokv?style=flat)](https://github.com/philippgille/gokv/stargazers) - Simple key-value store abstraction and implementations for Go (Redis, Consul, etcd, bbolt, BadgerDB, LevelDB, Memcached, DynamoDB, S3, PostgreSQL, MongoDB, CockroachDB and many more).
- [transactor](https://github.com/metalfm/transactor) [![GitHub stars](https://img.shields.io/github/stars/metalfm/transactor?style=flat)](https://github.com/metalfm/transactor/stargazers) - Type-safe transaction boundary abstraction with adapters for database/sql, sqlx, and pgx.

### Relational Database Drivers

- [avatica](https://github.com/apache/calcite-avatica-go) [![GitHub stars](https://img.shields.io/github/stars/apache/calcite-avatica-go?style=flat)](https://github.com/apache/calcite-avatica-go/stargazers) - Apache Avatica/Phoenix SQL driver for database/sql.
- [bgc](https://github.com/viant/bgc) [![GitHub stars](https://img.shields.io/github/stars/viant/bgc?style=flat)](https://github.com/viant/bgc/stargazers) - Datastore Connectivity for BigQuery for go.
- [firebirdsql](https://github.com/nakagami/firebirdsql) [![GitHub stars](https://img.shields.io/github/stars/nakagami/firebirdsql?style=flat)](https://github.com/nakagami/firebirdsql/stargazers) - Firebird RDBMS SQL driver for Go.
- [go-adodb](https://github.com/mattn/go-adodb) [![GitHub stars](https://img.shields.io/github/stars/mattn/go-adodb?style=flat)](https://github.com/mattn/go-adodb/stargazers) - Microsoft ActiveX Object DataBase driver for go that uses database/sql.
- [go-mssqldb](https://github.com/denisenkom/go-mssqldb) [![GitHub stars](https://img.shields.io/github/stars/denisenkom/go-mssqldb?style=flat)](https://github.com/denisenkom/go-mssqldb/stargazers) - Microsoft MSSQL driver for Go.
- [go-oci8](https://github.com/mattn/go-oci8) [![GitHub stars](https://img.shields.io/github/stars/mattn/go-oci8?style=flat)](https://github.com/mattn/go-oci8/stargazers) - Oracle driver for go that uses database/sql.
- [go-rqlite](https://github.com/rqlite/gorqlite) [![GitHub stars](https://img.shields.io/github/stars/rqlite/gorqlite?style=flat)](https://github.com/rqlite/gorqlite/stargazers) - A Go client for rqlite, providing easy-to-use abstractions for working with the rqlite API.
- [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) [![GitHub stars](https://img.shields.io/github/stars/go-sql-driver/mysql?style=flat)](https://github.com/go-sql-driver/mysql/stargazers) - MySQL driver for Go.
- [go-sqlite3](https://github.com/mattn/go-sqlite3) [![GitHub stars](https://img.shields.io/github/stars/mattn/go-sqlite3?style=flat)](https://github.com/mattn/go-sqlite3/stargazers) - SQLite3 driver for go that uses database/sql.
- [go-sqlite3](https://github.com/ncruces/go-sqlite3) [![GitHub stars](https://img.shields.io/github/stars/ncruces/go-sqlite3?style=flat)](https://github.com/ncruces/go-sqlite3/stargazers) - This Go module is compatible with the database/sql driver. It allows embedding SQLite into your application, provides direct access to its C API, supports SQLite VFS, and also includes a GORM driver.
- [godror](https://github.com/godror/godror) [![GitHub stars](https://img.shields.io/github/stars/godror/godror?style=flat)](https://github.com/godror/godror/stargazers) - Oracle driver for Go, using the ODPI-C driver.
- [gofreetds](https://github.com/minus5/gofreetds) [![GitHub stars](https://img.shields.io/github/stars/minus5/gofreetds?style=flat)](https://github.com/minus5/gofreetds/stargazers) - Microsoft MSSQL driver. Go wrapper over [FreeTDS](https://www.freetds.org).
- [KSQL](https://github.com/VinGarcia/ksql) [![GitHub stars](https://img.shields.io/github/stars/VinGarcia/ksql?style=flat)](https://github.com/VinGarcia/ksql/stargazers) - A Simple and Powerful Golang SQL Library.
- [pgx](https://github.com/jackc/pgx) [![GitHub stars](https://img.shields.io/github/stars/jackc/pgx?style=flat)](https://github.com/jackc/pgx/stargazers) - PostgreSQL driver supporting features beyond those exposed by database/sql.
- [pig](https://github.com/alexeyco/pig) [![GitHub stars](https://img.shields.io/github/stars/alexeyco/pig?style=flat)](https://github.com/alexeyco/pig/stargazers) - Simple [pgx](https://github.com/jackc/pgx) [![GitHub stars](https://img.shields.io/github/stars/jackc/pgx?style=flat)](https://github.com/jackc/pgx/stargazers) wrapper to execute and [scan](https://github.com/georgysavva/scany) [![GitHub stars](https://img.shields.io/github/stars/georgysavva/scany?style=flat)](https://github.com/georgysavva/scany/stargazers) query results easily.
- [pq](https://github.com/lib/pq) [![GitHub stars](https://img.shields.io/github/stars/lib/pq?style=flat)](https://github.com/lib/pq/stargazers) - Pure Go Postgres driver for database/sql.
- [Sqinn-Go](https://github.com/cvilsmeier/sqinn-go) [![GitHub stars](https://img.shields.io/github/stars/cvilsmeier/sqinn-go?style=flat)](https://github.com/cvilsmeier/sqinn-go/stargazers) - SQLite with pure Go.
- [sqlhooks](https://github.com/qustavo/sqlhooks) [![GitHub stars](https://img.shields.io/github/stars/qustavo/sqlhooks?style=flat)](https://github.com/qustavo/sqlhooks/stargazers) - Attach hooks to any database/sql driver.
- [sqlite](https://pkg.go.dev/modernc.org/sqlite) - Package sqlite is a sql/database driver using a CGo-free port of the C SQLite3 library.
- [surrealdb.go](https://github.com/surrealdb/surrealdb.go) [![GitHub stars](https://img.shields.io/github/stars/surrealdb/surrealdb.go?style=flat)](https://github.com/surrealdb/surrealdb.go/stargazers) - SurrealDB Driver for Go.
- [ydb-go-sdk](https://github.com/ydb-platform/ydb-go-sdk) [![GitHub stars](https://img.shields.io/github/stars/ydb-platform/ydb-go-sdk?style=flat)](https://github.com/ydb-platform/ydb-go-sdk/stargazers) - native and database/sql driver YDB (Yandex Database).

### NoSQL Database Drivers

- [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) [![GitHub stars](https://img.shields.io/github/stars/aerospike/aerospike-client-go?style=flat)](https://github.com/aerospike/aerospike-client-go/stargazers) - Aerospike client in Go language.
- [arangolite](https://github.com/solher/arangolite) [![GitHub stars](https://img.shields.io/github/stars/solher/arangolite?style=flat)](https://github.com/solher/arangolite/stargazers) - Lightweight golang driver for ArangoDB.
- [asc](https://github.com/viant/asc) [![GitHub stars](https://img.shields.io/github/stars/viant/asc?style=flat)](https://github.com/viant/asc/stargazers) - Datastore Connectivity for Aerospike for go.
- [forestdb](https://github.com/couchbase/goforestdb) [![GitHub stars](https://img.shields.io/github/stars/couchbase/goforestdb?style=flat)](https://github.com/couchbase/goforestdb/stargazers) - Go bindings for ForestDB.
- [go-couchbase](https://github.com/couchbase/go-couchbase) [![GitHub stars](https://img.shields.io/github/stars/couchbase/go-couchbase?style=flat)](https://github.com/couchbase/go-couchbase/stargazers) - Couchbase client in Go.
- [go-mongox](https://github.com/chenmingyong0423/go-mongox) [![GitHub stars](https://img.shields.io/github/stars/chenmingyong0423/go-mongox?style=flat)](https://github.com/chenmingyong0423/go-mongox/stargazers) - A Go Mongo library based on the official driver, featuring streamlined document operations, generic binding of structs to collections, built-in CRUD, aggregation, automated field updates, struct validation, hooks, and plugin-based programming.
- [go-pilosa](https://github.com/pilosa/go-pilosa) [![GitHub stars](https://img.shields.io/github/stars/pilosa/go-pilosa?style=flat)](https://github.com/pilosa/go-pilosa/stargazers) - Go client library for Pilosa.
- [go-rejson](https://github.com/nitishm/go-rejson) [![GitHub stars](https://img.shields.io/github/stars/nitishm/go-rejson?style=flat)](https://github.com/nitishm/go-rejson/stargazers) - Golang client for redislabs' ReJSON module using Redigo golang client. Store and manipulate structs as JSON objects in redis with ease.
- [gocb](https://github.com/couchbase/gocb) [![GitHub stars](https://img.shields.io/github/stars/couchbase/gocb?style=flat)](https://github.com/couchbase/gocb/stargazers) - Official Couchbase Go SDK.
- [gocosmos](https://github.com/btnguyen2k/gocosmos) [![GitHub stars](https://img.shields.io/github/stars/btnguyen2k/gocosmos?style=flat)](https://github.com/btnguyen2k/gocosmos/stargazers) - REST client and standard `database/sql` driver for Azure Cosmos DB.
- [gocql](https://gocql.github.io) - Go language driver for Apache Cassandra.
- [godis](https://github.com/piaohao/godis) [![GitHub stars](https://img.shields.io/github/stars/piaohao/godis?style=flat)](https://github.com/piaohao/godis/stargazers) - redis client implement by golang, inspired by jedis.
- [godscache](https://github.com/defcronyke/godscache) [![GitHub stars](https://img.shields.io/github/stars/defcronyke/godscache?style=flat)](https://github.com/defcronyke/godscache/stargazers) - A wrapper for the Google Cloud Platform Go Datastore package that adds caching using memcached.
- [gomemcache](https://github.com/bradfitz/gomemcache/) [![GitHub stars](https://img.shields.io/github/stars/bradfitz/gomemcache/?style=flat)](https://github.com/bradfitz/gomemcache//stargazers) - memcache client library for the Go programming language.
- [gomemcached](https://github.com/aliexpressru/gomemcached) [![GitHub stars](https://img.shields.io/github/stars/aliexpressru/gomemcached?style=flat)](https://github.com/aliexpressru/gomemcached/stargazers) - A binary Memcached client for Go with support for sharding using consistent hashing, along with SASL.
- [gorethink](https://github.com/dancannon/gorethink) [![GitHub stars](https://img.shields.io/github/stars/dancannon/gorethink?style=flat)](https://github.com/dancannon/gorethink/stargazers) - Go language driver for RethinkDB.
- [goriak](https://github.com/zegl/goriak) [![GitHub stars](https://img.shields.io/github/stars/zegl/goriak?style=flat)](https://github.com/zegl/goriak/stargazers) - Go language driver for Riak KV.
- [Kivik](https://github.com/go-kivik/kivik) [![GitHub stars](https://img.shields.io/github/stars/go-kivik/kivik?style=flat)](https://github.com/go-kivik/kivik/stargazers) - Kivik provides a common Go and GopherJS client library for CouchDB, PouchDB, and similar databases.
- [mgm](https://github.com/kamva/mgm) [![GitHub stars](https://img.shields.io/github/stars/kamva/mgm?style=flat)](https://github.com/kamva/mgm/stargazers) - MongoDB model-based ODM for Go (based on official MongoDB driver).
- [mgo](https://github.com/globalsign/mgo) [![GitHub stars](https://img.shields.io/github/stars/globalsign/mgo?style=flat)](https://github.com/globalsign/mgo/stargazers) - (unmaintained) MongoDB driver for the Go language that implements a rich and well tested selection of features under a very simple API following standard Go idioms.
- [mongo-go-driver](https://github.com/mongodb/mongo-go-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-go-driver?style=flat)](https://github.com/mongodb/mongo-go-driver/stargazers) - Official MongoDB driver for the Go language.
- [neo4j](https://github.com/cihangir/neo4j) [![GitHub stars](https://img.shields.io/github/stars/cihangir/neo4j?style=flat)](https://github.com/cihangir/neo4j/stargazers) - Neo4j Rest API Bindings for Golang.
- [neoism](https://github.com/jmcvetta/neoism) [![GitHub stars](https://img.shields.io/github/stars/jmcvetta/neoism?style=flat)](https://github.com/jmcvetta/neoism/stargazers) - Neo4j client for Golang.
- [qmgo](https://github.com/qiniu/qmgo) [![GitHub stars](https://img.shields.io/github/stars/qiniu/qmgo?style=flat)](https://github.com/qiniu/qmgo/stargazers) - The MongoDB driver for Go. It‘s based on official MongoDB driver but easier to use like Mgo.
- [redeo](https://github.com/bsm/redeo) [![GitHub stars](https://img.shields.io/github/stars/bsm/redeo?style=flat)](https://github.com/bsm/redeo/stargazers) - Redis-protocol compatible TCP servers/services.
- [redigo](https://github.com/gomodule/redigo) [![GitHub stars](https://img.shields.io/github/stars/gomodule/redigo?style=flat)](https://github.com/gomodule/redigo/stargazers) - Redigo is a Go client for the Redis database.
- [redis](https://github.com/redis/go-redis) [![GitHub stars](https://img.shields.io/github/stars/redis/go-redis?style=flat)](https://github.com/redis/go-redis/stargazers) - Redis client for Golang.
- [rueidis](http://github.com/rueian/rueidis) - Fast Redis RESP3 client with auto pipelining and server-assisted client side caching.
- [xredis](https://github.com/shomali11/xredis) [![GitHub stars](https://img.shields.io/github/stars/shomali11/xredis?style=flat)](https://github.com/shomali11/xredis/stargazers) - Typesafe, customizable, clean & easy to use Redis client.

### Search and Analytic Databases

- [clickhouse-go](https://github.com/ClickHouse/clickhouse-go/) [![GitHub stars](https://img.shields.io/github/stars/ClickHouse/clickhouse-go/?style=flat)](https://github.com/ClickHouse/clickhouse-go//stargazers) - ClickHouse SQL client for Go with a `database/sql` compatibility.
- [effdsl](https://github.com/sdqri/effdsl) [![GitHub stars](https://img.shields.io/github/stars/sdqri/effdsl?style=flat)](https://github.com/sdqri/effdsl/stargazers) - Elasticsearch query builder for Go.
- [elastic](https://github.com/olivere/elastic) [![GitHub stars](https://img.shields.io/github/stars/olivere/elastic?style=flat)](https://github.com/olivere/elastic/stargazers) - Elasticsearch client for Go.
- [elasticsql](https://github.com/cch123/elasticsql) [![GitHub stars](https://img.shields.io/github/stars/cch123/elasticsql?style=flat)](https://github.com/cch123/elasticsql/stargazers) - Convert sql to elasticsearch dsl in Go.
- [elastigo](https://github.com/mattbaird/elastigo) [![GitHub stars](https://img.shields.io/github/stars/mattbaird/elastigo?style=flat)](https://github.com/mattbaird/elastigo/stargazers) - Elasticsearch client library.
- [go-elasticsearch](https://github.com/elastic/go-elasticsearch) [![GitHub stars](https://img.shields.io/github/stars/elastic/go-elasticsearch?style=flat)](https://github.com/elastic/go-elasticsearch/stargazers) - Official Elasticsearch client for Go.
- [goes](https://github.com/OwnLocal/goes) [![GitHub stars](https://img.shields.io/github/stars/OwnLocal/goes?style=flat)](https://github.com/OwnLocal/goes/stargazers) - Library to interact with Elasticsearch.
- [skizze](https://github.com/skizzehq/skizze) [![GitHub stars](https://img.shields.io/github/stars/skizzehq/skizze?style=flat)](https://github.com/skizzehq/skizze/stargazers) - A probabilistic data structure service and storage.
- [zoekt](https://github.com/sourcegraph/zoekt) [![GitHub stars](https://img.shields.io/github/stars/sourcegraph/zoekt?style=flat)](https://github.com/sourcegraph/zoekt/stargazers) - Fast trigram based code search.

**[⬆ back to top](#contents)**

## Date and Time

_Libraries for working with dates and times._

- [approx](https://github.com/goschtalt/approx) [![GitHub stars](https://img.shields.io/github/stars/goschtalt/approx?style=flat)](https://github.com/goschtalt/approx/stargazers) - A Duration extension supporting parsing/printing durations in days, weeks and years.
- [carbon](https://github.com/dromara/carbon) [![GitHub stars](https://img.shields.io/github/stars/dromara/carbon?style=flat)](https://github.com/dromara/carbon/stargazers) - A simple, semantic and developer-friendly time package for golang.
- [carbon](https://github.com/uniplaces/carbon) [![GitHub stars](https://img.shields.io/github/stars/uniplaces/carbon?style=flat)](https://github.com/uniplaces/carbon/stargazers) - Simple Time extension with a lot of util methods, ported from PHP Carbon library.
- [cronrange](https://github.com/1set/cronrange) [![GitHub stars](https://img.shields.io/github/stars/1set/cronrange?style=flat)](https://github.com/1set/cronrange/stargazers) - Parses Cron-style time range expressions, checks if the given time is within any ranges.
- [date](https://github.com/rickb777/date) [![GitHub stars](https://img.shields.io/github/stars/rickb777/date?style=flat)](https://github.com/rickb777/date/stargazers) - Augments Time for working with dates, date ranges, time spans, periods, and time-of-day.
- [dateparse](https://github.com/araddon/dateparse) [![GitHub stars](https://img.shields.io/github/stars/araddon/dateparse?style=flat)](https://github.com/araddon/dateparse/stargazers) - Parse date's without knowing format in advance.
- [durafmt](https://github.com/hako/durafmt) [![GitHub stars](https://img.shields.io/github/stars/hako/durafmt?style=flat)](https://github.com/hako/durafmt/stargazers) - Time duration formatting library for Go.
- [feiertage](https://github.com/wlbr/feiertage) [![GitHub stars](https://img.shields.io/github/stars/wlbr/feiertage?style=flat)](https://github.com/wlbr/feiertage/stargazers) - Set of functions to calculate public holidays in Germany, incl. specialization on the states of Germany (Bundesländer). Things like Easter, Pentecost, Thanksgiving...
- [go-anytime](https://github.com/ijt/go-anytime) [![GitHub stars](https://img.shields.io/github/stars/ijt/go-anytime?style=flat)](https://github.com/ijt/go-anytime/stargazers) - Parse dates/times like "next dec 22nd at 3pm" and ranges like "from today until next thursday" without knowing the format in advance.
- [go-date-fns](https://github.com/chmenegatti/go-date-fns) [![GitHub stars](https://img.shields.io/github/stars/chmenegatti/go-date-fns?style=flat)](https://github.com/chmenegatti/go-date-fns/stargazers) - A comprehensive date utility library for Go, inspired by date-fns, with 140+ pure and immutable functions.
- [go-datebin](https://github.com/deatil/go-datebin) [![GitHub stars](https://img.shields.io/github/stars/deatil/go-datebin?style=flat)](https://github.com/deatil/go-datebin/stargazers) - A simple datetime parse pkg.
- [go-faketime](https://github.com/harkaitz/go-faketime) [![GitHub stars](https://img.shields.io/github/stars/harkaitz/go-faketime?style=flat)](https://github.com/harkaitz/go-faketime/stargazers) - A simple `time.Now()` that honors the faketime(1) utility.
- [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) [![GitHub stars](https://img.shields.io/github/stars/yaa110/go-persian-calendar?style=flat)](https://github.com/yaa110/go-persian-calendar/stargazers) - The implementation of the Persian (Solar Hijri) Calendar in Go (golang).
- [go-str2duration](https://github.com/xhit/go-str2duration) [![GitHub stars](https://img.shields.io/github/stars/xhit/go-str2duration?style=flat)](https://github.com/xhit/go-str2duration/stargazers) - Convert string to duration. Support time.Duration returned string and more.
- [go-sunrise](https://github.com/nathan-osman/go-sunrise) [![GitHub stars](https://img.shields.io/github/stars/nathan-osman/go-sunrise?style=flat)](https://github.com/nathan-osman/go-sunrise/stargazers) - Calculate the sunrise and sunset times for a given location.
- [go-week](https://github.com/stoewer/go-week) [![GitHub stars](https://img.shields.io/github/stars/stoewer/go-week?style=flat)](https://github.com/stoewer/go-week/stargazers) - An efficient package to work with ISO8601 week dates.
- [gostradamus](https://github.com/bykof/gostradamus) [![GitHub stars](https://img.shields.io/github/stars/bykof/gostradamus?style=flat)](https://github.com/bykof/gostradamus/stargazers) - A Go package for working with dates.
- [iso8601](https://github.com/relvacode/iso8601) [![GitHub stars](https://img.shields.io/github/stars/relvacode/iso8601?style=flat)](https://github.com/relvacode/iso8601/stargazers) - Efficiently parse ISO8601 date-times without regex.
- [kair](https://github.com/GuilhermeCaruso/kair) [![GitHub stars](https://img.shields.io/github/stars/GuilhermeCaruso/kair?style=flat)](https://github.com/GuilhermeCaruso/kair/stargazers) - Date and Time - Golang Formatting Library.
- [now](https://github.com/jinzhu/now) [![GitHub stars](https://img.shields.io/github/stars/jinzhu/now?style=flat)](https://github.com/jinzhu/now/stargazers) - Now is a time toolkit for golang.
- [strftime](https://github.com/awoodbeck/strftime) [![GitHub stars](https://img.shields.io/github/stars/awoodbeck/strftime?style=flat)](https://github.com/awoodbeck/strftime/stargazers) - C99-compatible strftime formatter.
- [timespan](https://github.com/SaidinWoT/timespan) [![GitHub stars](https://img.shields.io/github/stars/SaidinWoT/timespan?style=flat)](https://github.com/SaidinWoT/timespan/stargazers) - For interacting with intervals of time, defined as a start time and a duration.
- [timeutil](https://github.com/leekchan/timeutil) [![GitHub stars](https://img.shields.io/github/stars/leekchan/timeutil?style=flat)](https://github.com/leekchan/timeutil/stargazers) - Useful extensions (Timedelta, Strftime, ...) to the golang's time package.
- [tuesday](https://github.com/osteele/tuesday) [![GitHub stars](https://img.shields.io/github/stars/osteele/tuesday?style=flat)](https://github.com/osteele/tuesday/stargazers) - Ruby-compatible Strftime function.

**[⬆ back to top](#contents)**

## Distributed Systems

_Packages that help with building Distributed Systems._

- [arpc](https://github.com/lesismal/arpc) [![GitHub stars](https://img.shields.io/github/stars/lesismal/arpc?style=flat)](https://github.com/lesismal/arpc/stargazers) - More effective network communication, support two-way-calling, notify, broadcast.
- [bedrock](https://github.com/z5labs/bedrock) [![GitHub stars](https://img.shields.io/github/stars/z5labs/bedrock?style=flat)](https://github.com/z5labs/bedrock/stargazers) - Provides a minimal, modular and composable foundation for quickly developing services and more use case specific frameworks in Go.
- [capillaries](https://github.com/capillariesio/capillaries) [![GitHub stars](https://img.shields.io/github/stars/capillariesio/capillaries?style=flat)](https://github.com/capillariesio/capillaries/stargazers) - distributed batch data processing framework.
- [circuit](https://github.com/schigh/circuit) [![GitHub stars](https://img.shields.io/github/stars/schigh/circuit?style=flat)](https://github.com/schigh/circuit/stargazers) - Circuit breaker with gradual recovery via probabilistic throttling.
- [cmd-stream-go](https://github.com/cmd-stream/cmd-stream-go) [![GitHub stars](https://img.shields.io/github/stars/cmd-stream/cmd-stream-go?style=flat)](https://github.com/cmd-stream/cmd-stream-go/stargazers) - High-performance distributed command pattern library for Go.
- [committer](https://github.com/vadiminshakov/committer) [![GitHub stars](https://img.shields.io/github/stars/vadiminshakov/committer?style=flat)](https://github.com/vadiminshakov/committer/stargazers) - A distributed transactions management system (2PC/3PC implementation).
- [consistent](https://github.com/buraksezer/consistent) [![GitHub stars](https://img.shields.io/github/stars/buraksezer/consistent?style=flat)](https://github.com/buraksezer/consistent/stargazers) - Consistent hashing with bounded loads.
- [consistenthash](https://github.com/mbrostami/consistenthash) [![GitHub stars](https://img.shields.io/github/stars/mbrostami/consistenthash?style=flat)](https://github.com/mbrostami/consistenthash/stargazers) - Consistent hashing with configurable replicas.
- [dht](https://github.com/anacrolix/dht) [![GitHub stars](https://img.shields.io/github/stars/anacrolix/dht?style=flat)](https://github.com/anacrolix/dht/stargazers) - BitTorrent Kademlia DHT implementation.
- [digota](https://github.com/digota/digota) [![GitHub stars](https://img.shields.io/github/stars/digota/digota?style=flat)](https://github.com/digota/digota/stargazers) - grpc ecommerce microservice.
- [dot](https://github.com/dotchain/dot/) [![GitHub stars](https://img.shields.io/github/stars/dotchain/dot/?style=flat)](https://github.com/dotchain/dot//stargazers) - distributed sync using operational transformation/OT.
- [doublejump](https://github.com/edwingeng/doublejump) [![GitHub stars](https://img.shields.io/github/stars/edwingeng/doublejump?style=flat)](https://github.com/edwingeng/doublejump/stargazers) - A revamped Google's jump consistent hash.
- [dragonboat](https://github.com/lni/dragonboat) [![GitHub stars](https://img.shields.io/github/stars/lni/dragonboat?style=flat)](https://github.com/lni/dragonboat/stargazers) - A feature complete and high performance multi-group Raft library in Go.
- [Dragonfly](https://github.com/dragonflyoss/Dragonfly2) [![GitHub stars](https://img.shields.io/github/stars/dragonflyoss/Dragonfly2?style=flat)](https://github.com/dragonflyoss/Dragonfly2/stargazers) - Provide efficient, stable and secure file distribution and image acceleration based on p2p technology to be the best practice and standard solution in cloud native architectures.
- [drmaa](https://github.com/dgruber/drmaa) [![GitHub stars](https://img.shields.io/github/stars/dgruber/drmaa?style=flat)](https://github.com/dgruber/drmaa/stargazers) - Job submission library for cluster schedulers based on the DRMAA standard.
- [dynamolock](https://cirello.io/dynamolock) - DynamoDB-backed distributed locking implementation.
- [dynatomic](https://github.com/tylfin/dynatomic) [![GitHub stars](https://img.shields.io/github/stars/tylfin/dynatomic?style=flat)](https://github.com/tylfin/dynatomic/stargazers) - A library for using DynamoDB as an atomic counter.
- [emitter-io](https://github.com/emitter-io/emitter) [![GitHub stars](https://img.shields.io/github/stars/emitter-io/emitter?style=flat)](https://github.com/emitter-io/emitter/stargazers) - High performance, distributed, secure and low latency publish-subscribe platform built with MQTT, Websockets and love.
- [evans](https://github.com/ktr0731/evans) [![GitHub stars](https://img.shields.io/github/stars/ktr0731/evans?style=flat)](https://github.com/ktr0731/evans/stargazers) - Evans: more expressive universal gRPC client.
- [failured](https://github.com/andy2046/failured) [![GitHub stars](https://img.shields.io/github/stars/andy2046/failured?style=flat)](https://github.com/andy2046/failured/stargazers) - adaptive accrual failure detector for distributed systems.
- [flowgraph](https://github.com/vectaport/flowgraph) [![GitHub stars](https://img.shields.io/github/stars/vectaport/flowgraph?style=flat)](https://github.com/vectaport/flowgraph/stargazers) - flow-based programming package.
- [gleam](https://github.com/chrislusf/gleam) [![GitHub stars](https://img.shields.io/github/stars/chrislusf/gleam?style=flat)](https://github.com/chrislusf/gleam/stargazers) - Fast and scalable distributed map/reduce system written in pure Go and Luajit, combining Go's high concurrency with Luajit's high performance, runs standalone or distributed.
- [glow](https://github.com/chrislusf/glow) [![GitHub stars](https://img.shields.io/github/stars/chrislusf/glow?style=flat)](https://github.com/chrislusf/glow/stargazers) - Easy-to-Use scalable distributed big data processing, Map-Reduce, DAG execution, all in pure Go.
- [gmsec](https://github.com/gmsec/micro) [![GitHub stars](https://img.shields.io/github/stars/gmsec/micro?style=flat)](https://github.com/gmsec/micro/stargazers) - A Go distributed systems development framework.
- [go-doudou](https://github.com/unionj-cloud/go-doudou) [![GitHub stars](https://img.shields.io/github/stars/unionj-cloud/go-doudou?style=flat)](https://github.com/unionj-cloud/go-doudou/stargazers) - A gossip protocol and OpenAPI 3.0 spec based decentralized microservice framework. Built-in go-doudou cli focusing on low-code and rapid dev can power up your productivity.
- [go-eagle](https://github.com/go-eagle/eagle) [![GitHub stars](https://img.shields.io/github/stars/go-eagle/eagle?style=flat)](https://github.com/go-eagle/eagle/stargazers) - A Go framework for the API or Microservice with handy scaffolding tools.
- [go-jump](https://github.com/dgryski/go-jump) [![GitHub stars](https://img.shields.io/github/stars/dgryski/go-jump?style=flat)](https://github.com/dgryski/go-jump/stargazers) - Port of Google's "Jump" Consistent Hash function.
- [go-kit](https://github.com/go-kit/kit) [![GitHub stars](https://img.shields.io/github/stars/go-kit/kit?style=flat)](https://github.com/go-kit/kit/stargazers) - Microservice toolkit with support for service discovery, load balancing, pluggable transports, request tracking, etc.
- [go-micro](https://github.com/micro/go-micro) [![GitHub stars](https://img.shields.io/github/stars/micro/go-micro?style=flat)](https://github.com/micro/go-micro/stargazers) - A distributed systems development framework.
- [go-mysql-lock](https://github.com/sanketplus/go-mysql-lock) [![GitHub stars](https://img.shields.io/github/stars/sanketplus/go-mysql-lock?style=flat)](https://github.com/sanketplus/go-mysql-lock/stargazers) - MySQL based distributed lock.
- [go-pdu](https://github.com/pdupub/go-pdu) [![GitHub stars](https://img.shields.io/github/stars/pdupub/go-pdu?style=flat)](https://github.com/pdupub/go-pdu/stargazers) - A decentralized identity-based social network.
- [go-sundheit](https://github.com/AppsFlyer/go-sundheit) [![GitHub stars](https://img.shields.io/github/stars/AppsFlyer/go-sundheit?style=flat)](https://github.com/AppsFlyer/go-sundheit/stargazers) - A library built to provide support for defining async service health checks for golang services.
- [go-zero](https://github.com/tal-tech/go-zero) [![GitHub stars](https://img.shields.io/github/stars/tal-tech/go-zero?style=flat)](https://github.com/tal-tech/go-zero/stargazers) - A web and rpc framework. It's born to ensure the stability of the busy sites with resilient design. Builtin goctl greatly improves the development productivity.
- [gorpc](https://github.com/valyala/gorpc) [![GitHub stars](https://img.shields.io/github/stars/valyala/gorpc?style=flat)](https://github.com/valyala/gorpc/stargazers) - Simple, fast and scalable RPC library for high load.
- [grpc-go](https://github.com/grpc/grpc-go) [![GitHub stars](https://img.shields.io/github/stars/grpc/grpc-go?style=flat)](https://github.com/grpc/grpc-go/stargazers) - The Go language implementation of gRPC. HTTP/2 based RPC.
- [health](https://github.com/schigh/health) [![GitHub stars](https://img.shields.io/github/stars/schigh/health?style=flat)](https://github.com/schigh/health/stargazers) - Health checker for Go services with Kubernetes probe support.
- [hprose](https://github.com/hprose/hprose-golang) [![GitHub stars](https://img.shields.io/github/stars/hprose/hprose-golang?style=flat)](https://github.com/hprose/hprose-golang/stargazers) - Very newbility RPC Library, support 25+ languages now.
- [jsonrpc](https://github.com/osamingo/jsonrpc) [![GitHub stars](https://img.shields.io/github/stars/osamingo/jsonrpc?style=flat)](https://github.com/osamingo/jsonrpc/stargazers) - The jsonrpc package helps implement of JSON-RPC 2.0.
- [jsonrpc](https://github.com/ybbus/jsonrpc) [![GitHub stars](https://img.shields.io/github/stars/ybbus/jsonrpc?style=flat)](https://github.com/ybbus/jsonrpc/stargazers) - JSON-RPC 2.0 HTTP client implementation.
- [K8gb](https://github.com/k8gb-io/k8gb) [![GitHub stars](https://img.shields.io/github/stars/k8gb-io/k8gb?style=flat)](https://github.com/k8gb-io/k8gb/stargazers) - A cloud native Kubernetes Global Balancer.
- [Kitex](https://github.com/cloudwego/kitex) [![GitHub stars](https://img.shields.io/github/stars/cloudwego/kitex?style=flat)](https://github.com/cloudwego/kitex/stargazers) - A high-performance and strong-extensibility Golang RPC framework that helps developers build microservices. If the performance and extensibility are the main concerns when you develop microservices, Kitex can be a good choice.
- [Kratos](https://github.com/go-kratos/kratos) [![GitHub stars](https://img.shields.io/github/stars/go-kratos/kratos?style=flat)](https://github.com/go-kratos/kratos/stargazers) - A modular-designed and easy-to-use microservices framework in Go.
- [liftbridge](https://github.com/liftbridge-io/liftbridge) [![GitHub stars](https://img.shields.io/github/stars/liftbridge-io/liftbridge?style=flat)](https://github.com/liftbridge-io/liftbridge/stargazers) - Lightweight, fault-tolerant message streams for NATS.
- [lock](https://github.com/ubgo/lock) [![GitHub stars](https://img.shields.io/github/stars/ubgo/lock?style=flat)](https://github.com/ubgo/lock/stargazers) - Distributed lock family with one Go interface and five backends (filelock, flock, Redis, Postgres, etcd) — fencing tokens, semaphore mode, and observability hooks across all backends.
- [lura](https://github.com/luraproject/lura) [![GitHub stars](https://img.shields.io/github/stars/luraproject/lura?style=flat)](https://github.com/luraproject/lura/stargazers) - Ultra performant API Gateway framework with middlewares.
- [mochi mqtt](https://github.com/mochi-co/mqtt) [![GitHub stars](https://img.shields.io/github/stars/mochi-co/mqtt?style=flat)](https://github.com/mochi-co/mqtt/stargazers) - Fully spec compliant, embeddable high-performance MQTT v5/v3 broker for IoT, smarthome, and pubsub.
- [NATS](https://github.com/nats-io/nats-server) [![GitHub stars](https://img.shields.io/github/stars/nats-io/nats-server?style=flat)](https://github.com/nats-io/nats-server/stargazers) - NATS is a simple, secure, and performant communications system for digital systems, services, and devices.
- [opentelemetry-go-auto-instrumentation](https://github.com/alibaba/opentelemetry-go-auto-instrumentation) [![GitHub stars](https://img.shields.io/github/stars/alibaba/opentelemetry-go-auto-instrumentation?style=flat)](https://github.com/alibaba/opentelemetry-go-auto-instrumentation/stargazers) - OpenTelemetry Compile-Time Instrumentation for Golang.
- [oras](https://github.com/oras-project/oras) [![GitHub stars](https://img.shields.io/github/stars/oras-project/oras?style=flat)](https://github.com/oras-project/oras/stargazers) - CLI and library for OCI Artifacts in container registries.
- [outbox](https://github.com/oagudo/outbox) [![GitHub stars](https://img.shields.io/github/stars/oagudo/outbox?style=flat)](https://github.com/oagudo/outbox/stargazers) - Lightweight library for the transactional outbox pattern in Go, not tied to any specific relational database or broker.
- [outboxer](https://github.com/italolelis/outboxer) [![GitHub stars](https://img.shields.io/github/stars/italolelis/outboxer?style=flat)](https://github.com/italolelis/outboxer/stargazers) - Outboxer is a go library that implements the outbox pattern.
- [pglock](https://cirello.io/pglock) - PostgreSQL-backed distributed locking implementation.
- [pjrpc](https://gitlab.com/pjrpc/pjrpc) - Golang JSON-RPC Server-Client with Protobuf spec.
- [raft](https://github.com/hashicorp/raft) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/raft?style=flat)](https://github.com/hashicorp/raft/stargazers) - Golang implementation of the Raft consensus protocol, by HashiCorp.
- [raft](https://github.com/etcd-io/raft) [![GitHub stars](https://img.shields.io/github/stars/etcd-io/raft?style=flat)](https://github.com/etcd-io/raft/stargazers) - Go implementation of the Raft consensus protocol, by CoreOS.
- [rain](https://github.com/cenkalti/rain) [![GitHub stars](https://img.shields.io/github/stars/cenkalti/rain?style=flat)](https://github.com/cenkalti/rain/stargazers) - BitTorrent client and library.
- [redis-lock](https://github.com/bsm/redislock) [![GitHub stars](https://img.shields.io/github/stars/bsm/redislock?style=flat)](https://github.com/bsm/redislock/stargazers) - Simplified distributed locking implementation using Redis.
- [resgate](https://resgate.io/) - Realtime API Gateway for building REST, real time, and RPC APIs, where all clients are synchronized seamlessly.
- [rpcplatform](https://github.com/nexcode/rpcplatform) [![GitHub stars](https://img.shields.io/github/stars/nexcode/rpcplatform?style=flat)](https://github.com/nexcode/rpcplatform/stargazers) - Framework for microservices with service discovery, load balancing, and related features.
- [rpcx](https://github.com/smallnest/rpcx) [![GitHub stars](https://img.shields.io/github/stars/smallnest/rpcx?style=flat)](https://github.com/smallnest/rpcx/stargazers) - Distributed pluggable RPC service framework like alibaba Dubbo.
- [Semaphore](https://github.com/jexia/semaphore) [![GitHub stars](https://img.shields.io/github/stars/jexia/semaphore?style=flat)](https://github.com/jexia/semaphore/stargazers) - A straightforward (micro) service orchestrator.
- [sleuth](https://github.com/ursiform/sleuth) [![GitHub stars](https://img.shields.io/github/stars/ursiform/sleuth?style=flat)](https://github.com/ursiform/sleuth/stargazers) - Library for master-less p2p auto-discovery and RPC between HTTP services (using [ZeroMQ](https://github.com/zeromq/libzmq) [![GitHub stars](https://img.shields.io/github/stars/zeromq/libzmq?style=flat)](https://github.com/zeromq/libzmq/stargazers)).
- [sponge](https://github.com/zhufuyi/sponge) [![GitHub stars](https://img.shields.io/github/stars/zhufuyi/sponge?style=flat)](https://github.com/zhufuyi/sponge/stargazers) - A distributed development framework that integrates automatic code generation, gin and grpc frameworks, base development frameworks.
- [Tarmac](https://github.com/tarmac-project/tarmac) [![GitHub stars](https://img.shields.io/github/stars/tarmac-project/tarmac?style=flat)](https://github.com/tarmac-project/tarmac/stargazers) - Framework for writing functions, microservices, or monoliths with WebAssembly
- [Temporal](https://github.com/temporalio/sdk-go) [![GitHub stars](https://img.shields.io/github/stars/temporalio/sdk-go?style=flat)](https://github.com/temporalio/sdk-go/stargazers) - Durable execution system for making code fault-tolerant and simple.
- [torrent](https://github.com/anacrolix/torrent) [![GitHub stars](https://img.shields.io/github/stars/anacrolix/torrent?style=flat)](https://github.com/anacrolix/torrent/stargazers) - BitTorrent client package.
- [trpc-go](https://github.com/trpc-group/trpc-go) [![GitHub stars](https://img.shields.io/github/stars/trpc-group/trpc-go?style=flat)](https://github.com/trpc-group/trpc-go/stargazers) - The Go language implementation of tRPC, which is a pluggable, high-performance RPC framework.

**[⬆ back to top](#contents)**

## Dynamic DNS

_Tools for updating dynamic DNS records._

- [DDNS](https://github.com/skibish/ddns) [![GitHub stars](https://img.shields.io/github/stars/skibish/ddns?style=flat)](https://github.com/skibish/ddns/stargazers) - Personal DDNS client with Digital Ocean Networking DNS as backend.
- [dyndns](https://gitlab.com/alcastle/dyndns) - Background Go process to regularly and automatically check your IP Address and make updates to (one or many) Dynamic DNS records for Google domains whenever your address changes.
- [GoDNS](https://github.com/timothyye/godns) [![GitHub stars](https://img.shields.io/github/stars/timothyye/godns?style=flat)](https://github.com/timothyye/godns/stargazers) - A dynamic DNS client tool, supports DNSPod & HE.net, written in Go.

**[⬆ back to top](#contents)**

## Email

_Libraries and tools that implement email creation and sending._

- [chasquid](https://blitiri.com.ar/p/chasquid) - SMTP server written in Go.
- [douceur](https://github.com/aymerick/douceur) [![GitHub stars](https://img.shields.io/github/stars/aymerick/douceur?style=flat)](https://github.com/aymerick/douceur/stargazers) - CSS inliner for your HTML emails.
- [email](https://github.com/jordan-wright/email) [![GitHub stars](https://img.shields.io/github/stars/jordan-wright/email?style=flat)](https://github.com/jordan-wright/email/stargazers) - A robust and flexible email library for Go.
- [email-verifier](https://github.com/AfterShip/email-verifier) [![GitHub stars](https://img.shields.io/github/stars/AfterShip/email-verifier?style=flat)](https://github.com/AfterShip/email-verifier/stargazers) - A Go library for email verification without sending any emails.
- [go-dkim](https://github.com/toorop/go-dkim) [![GitHub stars](https://img.shields.io/github/stars/toorop/go-dkim?style=flat)](https://github.com/toorop/go-dkim/stargazers) - DKIM library, to sign & verify email.
- [go-email-normalizer](https://github.com/dimuska139/go-email-normalizer) [![GitHub stars](https://img.shields.io/github/stars/dimuska139/go-email-normalizer?style=flat)](https://github.com/dimuska139/go-email-normalizer/stargazers) - Golang library for providing a canonical representation of email address.
- [go-imap](https://github.com/BrianLeishman/go-imap) [![GitHub stars](https://img.shields.io/github/stars/BrianLeishman/go-imap?style=flat)](https://github.com/BrianLeishman/go-imap/stargazers) - Batteries-included IMAP client with auto-reconnect, OAuth2, IDLE support, and built-in MIME parsing.
- [go-imap](https://github.com/emersion/go-imap) [![GitHub stars](https://img.shields.io/github/stars/emersion/go-imap?style=flat)](https://github.com/emersion/go-imap/stargazers) - IMAP library for clients and servers.
- [go-mail](https://github.com/wneessen/go-mail) [![GitHub stars](https://img.shields.io/github/stars/wneessen/go-mail?style=flat)](https://github.com/wneessen/go-mail/stargazers) - A simple Go library for sending mails in Go.
- [go-message](https://github.com/emersion/go-message) [![GitHub stars](https://img.shields.io/github/stars/emersion/go-message?style=flat)](https://github.com/emersion/go-message/stargazers) - Streaming library for the Internet Message Format and mail messages.
- [go-premailer](https://github.com/vanng822/go-premailer) [![GitHub stars](https://img.shields.io/github/stars/vanng822/go-premailer?style=flat)](https://github.com/vanng822/go-premailer/stargazers) - Inline styling for HTML mail in Go.
- [go-simple-mail](https://github.com/xhit/go-simple-mail) [![GitHub stars](https://img.shields.io/github/stars/xhit/go-simple-mail?style=flat)](https://github.com/xhit/go-simple-mail/stargazers) - Very simple package to send emails with SMTP Keep Alive and two timeouts: Connect and Send.
- [Hectane](https://github.com/hectane/hectane) [![GitHub stars](https://img.shields.io/github/stars/hectane/hectane?style=flat)](https://github.com/hectane/hectane/stargazers) - Lightweight SMTP client providing an HTTP API.
- [hermes](https://github.com/matcornic/hermes) [![GitHub stars](https://img.shields.io/github/stars/matcornic/hermes?style=flat)](https://github.com/matcornic/hermes/stargazers) - Golang package that generates clean, responsive HTML e-mails.
- [Maddy](https://github.com/foxcpp/maddy) [![GitHub stars](https://img.shields.io/github/stars/foxcpp/maddy?style=flat)](https://github.com/foxcpp/maddy/stargazers) - All-in-one (SMTP, IMAP, DKIM, DMARC, MTA-STS, DANE) email server
- [mailchain](https://github.com/mailchain/mailchain) [![GitHub stars](https://img.shields.io/github/stars/mailchain/mailchain?style=flat)](https://github.com/mailchain/mailchain/stargazers) - Send encrypted emails to blockchain addresses written in Go.
- [mailgun-go](https://github.com/mailgun/mailgun-go) [![GitHub stars](https://img.shields.io/github/stars/mailgun/mailgun-go?style=flat)](https://github.com/mailgun/mailgun-go/stargazers) - Go library for sending mail with the Mailgun API.
- [MailHog](https://github.com/mailhog/MailHog) [![GitHub stars](https://img.shields.io/github/stars/mailhog/MailHog?style=flat)](https://github.com/mailhog/MailHog/stargazers) - Email and SMTP testing with web and API interface.
- [Mailpit](https://github.com/axllent/mailpit) [![GitHub stars](https://img.shields.io/github/stars/axllent/mailpit?style=flat)](https://github.com/axllent/mailpit/stargazers) - Email and SMTP testing tool for developers.
- [mailx](https://github.com/valord577/mailx) [![GitHub stars](https://img.shields.io/github/stars/valord577/mailx?style=flat)](https://github.com/valord577/mailx/stargazers) - Mailx is a library that makes it easier to send email via SMTP. It is an enhancement of the golang standard library `net/smtp`.
- [mox](https://github.com/mjl-/mox) [![GitHub stars](https://img.shields.io/github/stars/mjl-/mox?style=flat)](https://github.com/mjl-/mox/stargazers) - Modern full-featured secure mail server for low-maintenance, self-hosted email.
- [SendGrid](https://github.com/sendgrid/sendgrid-go) [![GitHub stars](https://img.shields.io/github/stars/sendgrid/sendgrid-go?style=flat)](https://github.com/sendgrid/sendgrid-go/stargazers) - SendGrid's Go library for sending email.
- [smtp](https://github.com/mailhog/smtp) [![GitHub stars](https://img.shields.io/github/stars/mailhog/smtp?style=flat)](https://github.com/mailhog/smtp/stargazers) - SMTP server protocol state machine.
- [smtpmock](https://github.com/mocktools/go-smtp-mock) [![GitHub stars](https://img.shields.io/github/stars/mocktools/go-smtp-mock?style=flat)](https://github.com/mocktools/go-smtp-mock/stargazers) - Lightweight configurable multithreaded fake SMTP server. Mimic any SMTP behaviour for your test environment.
- [tickstem/verify](https://github.com/tickstem/verify) [![GitHub stars](https://img.shields.io/github/stars/tickstem/verify?style=flat)](https://github.com/tickstem/verify/stargazers) - Validate email addresses before they hit your database: syntax, MX lookup, disposable domains, and role-based inboxes.
- [truemail-go](https://github.com/truemail-rb/truemail-go) [![GitHub stars](https://img.shields.io/github/stars/truemail-rb/truemail-go?style=flat)](https://github.com/truemail-rb/truemail-go/stargazers) - Configurable Golang email validator/verifier. Verify email via Regex, DNS, SMTP and even more.

**[⬆ back to top](#contents)**

## Embeddable Scripting Languages

_Embedding other languages inside your go code._

- [anko](https://github.com/mattn/anko) [![GitHub stars](https://img.shields.io/github/stars/mattn/anko?style=flat)](https://github.com/mattn/anko/stargazers) - Scriptable interpreter written in Go.
- [binder](https://github.com/alexeyco/binder) [![GitHub stars](https://img.shields.io/github/stars/alexeyco/binder?style=flat)](https://github.com/alexeyco/binder/stargazers) - Go to Lua binding library, based on [gopher-lua](https://github.com/yuin/gopher-lua) [![GitHub stars](https://img.shields.io/github/stars/yuin/gopher-lua?style=flat)](https://github.com/yuin/gopher-lua/stargazers).
- [cel-go](https://github.com/google/cel-go) [![GitHub stars](https://img.shields.io/github/stars/google/cel-go?style=flat)](https://github.com/google/cel-go/stargazers) - Fast, portable, non-Turing complete expression evaluation with gradual typing.
- [ecal](https://github.com/krotik/ecal) [![GitHub stars](https://img.shields.io/github/stars/krotik/ecal?style=flat)](https://github.com/krotik/ecal/stargazers) - A simple embeddable scripting language which supports concurrent event processing.
- [expr](https://github.com/antonmedv/expr) [![GitHub stars](https://img.shields.io/github/stars/antonmedv/expr?style=flat)](https://github.com/antonmedv/expr/stargazers) - Expression evaluation engine for Go: fast, non-Turing complete, dynamic typing, static typing.
- [FrankenPHP](https://github.com/dunglas/frankenphp) [![GitHub stars](https://img.shields.io/github/stars/dunglas/frankenphp?style=flat)](https://github.com/dunglas/frankenphp/stargazers) - PHP embedded in Go, with a `net/http` handler.
- [gentee](https://github.com/gentee/gentee) [![GitHub stars](https://img.shields.io/github/stars/gentee/gentee?style=flat)](https://github.com/gentee/gentee/stargazers) - Embeddable scripting programming language.
- [gisp](https://github.com/jcla1/gisp) [![GitHub stars](https://img.shields.io/github/stars/jcla1/gisp?style=flat)](https://github.com/jcla1/gisp/stargazers) - Simple LISP in Go.
- [go-lua](https://github.com/Shopify/go-lua) [![GitHub stars](https://img.shields.io/github/stars/Shopify/go-lua?style=flat)](https://github.com/Shopify/go-lua/stargazers) - Port of the Lua 5.2 VM to pure Go.
- [go-lua](https://github.com/speedata/go-lua) [![GitHub stars](https://img.shields.io/github/stars/speedata/go-lua?style=flat)](https://github.com/speedata/go-lua/stargazers) - Lua 5.4 VM implemented in pure Go.
- [go-php](https://github.com/deuill/go-php) [![GitHub stars](https://img.shields.io/github/stars/deuill/go-php?style=flat)](https://github.com/deuill/go-php/stargazers) - PHP bindings for Go.
- [goal](https://codeberg.org/anaseto/goal) - An embeddable scripting array language.
- [goja](https://github.com/dop251/goja) [![GitHub stars](https://img.shields.io/github/stars/dop251/goja?style=flat)](https://github.com/dop251/goja/stargazers) - ECMAScript 5.1(+) implementation in Go.
- [golua](https://github.com/aarzilli/golua) [![GitHub stars](https://img.shields.io/github/stars/aarzilli/golua?style=flat)](https://github.com/aarzilli/golua/stargazers) - Go bindings for Lua C API.
- [gopher-lua](https://github.com/yuin/gopher-lua) [![GitHub stars](https://img.shields.io/github/stars/yuin/gopher-lua?style=flat)](https://github.com/yuin/gopher-lua/stargazers) - Lua 5.1 VM and compiler written in Go.
- [gval](https://github.com/PaesslerAG/gval) [![GitHub stars](https://img.shields.io/github/stars/PaesslerAG/gval?style=flat)](https://github.com/PaesslerAG/gval/stargazers) - A highly customizable expression language written in Go.
- [metacall](https://github.com/metacall/core) [![GitHub stars](https://img.shields.io/github/stars/metacall/core?style=flat)](https://github.com/metacall/core/stargazers) - Cross-platform Polyglot Runtime which supports NodeJS, JavaScript, TypeScript, Python, Ruby, C#, WebAssembly, Java, Cobol and more.
- [ngaro](https://github.com/db47h/ngaro) [![GitHub stars](https://img.shields.io/github/stars/db47h/ngaro?style=flat)](https://github.com/db47h/ngaro/stargazers) - Embeddable Ngaro VM implementation enabling scripting in Retro.
- [prolog](https://github.com/ichiban/prolog) [![GitHub stars](https://img.shields.io/github/stars/ichiban/prolog?style=flat)](https://github.com/ichiban/prolog/stargazers) - Embeddable Prolog.
- [purl](https://github.com/ian-kent/purl) [![GitHub stars](https://img.shields.io/github/stars/ian-kent/purl?style=flat)](https://github.com/ian-kent/purl/stargazers) - Perl 5.18.2 embedded in Go.
- [starlark-go](https://github.com/google/starlark-go) [![GitHub stars](https://img.shields.io/github/stars/google/starlark-go?style=flat)](https://github.com/google/starlark-go/stargazers) - Go implementation of Starlark: Python-like language with deterministic evaluation and hermetic execution.
- [starlet](https://github.com/1set/starlet) [![GitHub stars](https://img.shields.io/github/stars/1set/starlet?style=flat)](https://github.com/1set/starlet/stargazers) - Go wrapper for [starlark-go](https://github.com/google/starlark-go) [![GitHub stars](https://img.shields.io/github/stars/google/starlark-go?style=flat)](https://github.com/google/starlark-go/stargazers) that simplifies script execution, offers data conversion, and useful Starlark libraries and extensions.
- [tengo](https://github.com/d5/tengo) [![GitHub stars](https://img.shields.io/github/stars/d5/tengo?style=flat)](https://github.com/d5/tengo/stargazers) - Bytecode compiled script language for Go.
- [Wa/凹语言](https://github.com/wa-lang/wa) [![GitHub stars](https://img.shields.io/github/stars/wa-lang/wa?style=flat)](https://github.com/wa-lang/wa/stargazers) - The Wa Programming Language embedded in Go.

**[⬆ back to top](#contents)**

## Error Handling

_Libraries for handling errors._

- [emperror](https://github.com/emperror/emperror) [![GitHub stars](https://img.shields.io/github/stars/emperror/emperror?style=flat)](https://github.com/emperror/emperror/stargazers) - Error handling tools and best practices for Go libraries and applications.
- [eris](https://github.com/rotisserie/eris) [![GitHub stars](https://img.shields.io/github/stars/rotisserie/eris?style=flat)](https://github.com/rotisserie/eris/stargazers) - A better way to handle, trace, and log errors in Go. Compatible with the standard error library and github.com/pkg/errors.
- [errlog](https://github.com/snwfdhmp/errlog) [![GitHub stars](https://img.shields.io/github/stars/snwfdhmp/errlog?style=flat)](https://github.com/snwfdhmp/errlog/stargazers) - Hackable package that determines responsible source code for an error (and some other fast-debugging features). Pluggable to any logger in-place.
- [errors](https://github.com/emperror/errors) [![GitHub stars](https://img.shields.io/github/stars/emperror/errors?style=flat)](https://github.com/emperror/errors/stargazers) - Drop-in replacement for the standard library errors package and github.com/pkg/errors. Provides various error handling primitives.
- [errors](https://github.com/neuronlabs/errors) [![GitHub stars](https://img.shields.io/github/stars/neuronlabs/errors?style=flat)](https://github.com/neuronlabs/errors/stargazers) - Simple golang error handling with classification primitives.
- [errors](https://github.com/PumpkinSeed/errors) [![GitHub stars](https://img.shields.io/github/stars/PumpkinSeed/errors?style=flat)](https://github.com/PumpkinSeed/errors/stargazers) - The most simple error wrapper with awesome performance and minimal memory overhead.
- [errors](https://gitlab.com/tozd/go/errors) - Providing errors with a stack trace and optional structured details. Compatible with github.com/pkg/errors API but does not use it internally.
- [errors](https://github.com/naughtygopher/errors) [![GitHub stars](https://img.shields.io/github/stars/naughtygopher/errors?style=flat)](https://github.com/naughtygopher/errors/stargazers) - Drop-in replacement for builtin Go errors. This is a minimal error handling package with custom error types, user friendly messages, Unwrap & Is. With very easy to use and straightforward helper functions.
- [errors](https://github.com/cockroachdb/errors) [![GitHub stars](https://img.shields.io/github/stars/cockroachdb/errors?style=flat)](https://github.com/cockroachdb/errors/stargazers) - Go error library with error portability over the network.
- [errorx](https://github.com/joomcode/errorx) [![GitHub stars](https://img.shields.io/github/stars/joomcode/errorx?style=flat)](https://github.com/joomcode/errorx/stargazers) - A feature rich error package with stack traces, composition of errors and more.
- [exception](https://github.com/rbrahul/exception) [![GitHub stars](https://img.shields.io/github/stars/rbrahul/exception?style=flat)](https://github.com/rbrahul/exception/stargazers) - A simple utility package for exception handling with try-catch in Golang.
- [Falcon](https://github.com/SonicRoshan/falcon) [![GitHub stars](https://img.shields.io/github/stars/SonicRoshan/falcon?style=flat)](https://github.com/SonicRoshan/falcon/stargazers) - A Simple Yet Highly Powerful Package For Error Handling.
- [Fault](https://github.com/Southclaws/fault) [![GitHub stars](https://img.shields.io/github/stars/Southclaws/fault?style=flat)](https://github.com/Southclaws/fault/stargazers) - An ergonomic mechanism for wrapping errors in order to facilitate structured metadata and context for error values.
- [go-errr](https://github.com/go-errr/go) [![GitHub stars](https://img.shields.io/github/stars/go-errr/go?style=flat)](https://github.com/go-errr/go/stargazers) - Error handling library with Catch/Recover semantics, wrapped error chains, and stack traces for Go.
- [go-multierror](https://github.com/hashicorp/go-multierror) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/go-multierror?style=flat)](https://github.com/hashicorp/go-multierror/stargazers) - Go (golang) package for representing a list of errors as a single error.
- [metaerr](https://github.com/quantumcycle/metaerr) [![GitHub stars](https://img.shields.io/github/stars/quantumcycle/metaerr?style=flat)](https://github.com/quantumcycle/metaerr/stargazers) - A library to create your custom error builders producing structured errors with metadata from different sources and optional stacktraces.
- [multierr](https://github.com/uber-go/multierr) [![GitHub stars](https://img.shields.io/github/stars/uber-go/multierr?style=flat)](https://github.com/uber-go/multierr/stargazers) - Package for representing a list of errors as a single error.
- [oops](https://github.com/samber/oops) [![GitHub stars](https://img.shields.io/github/stars/samber/oops?style=flat)](https://github.com/samber/oops/stargazers) - Error handling with context, stack trace and source fragments.
- [tracerr](https://github.com/ztrue/tracerr) [![GitHub stars](https://img.shields.io/github/stars/ztrue/tracerr?style=flat)](https://github.com/ztrue/tracerr/stargazers) - Golang errors with stack trace and source fragments.

**[⬆ back to top](#contents)**

## File Handling

_Libraries for handling files and file systems._

- [afero](https://github.com/spf13/afero) [![GitHub stars](https://img.shields.io/github/stars/spf13/afero?style=flat)](https://github.com/spf13/afero/stargazers) - FileSystem Abstraction System for Go.
- [afs](https://github.com/viant/afs) [![GitHub stars](https://img.shields.io/github/stars/viant/afs?style=flat)](https://github.com/viant/afs/stargazers) - Abstract File Storage (mem, scp, zip, tar, cloud: s3, gs) for Go.
- [baraka](https://github.com/xis/baraka) [![GitHub stars](https://img.shields.io/github/stars/xis/baraka?style=flat)](https://github.com/xis/baraka/stargazers) - A library to process http file uploads easily.
- [checksum](https://github.com/codingsince1985/checksum) [![GitHub stars](https://img.shields.io/github/stars/codingsince1985/checksum?style=flat)](https://github.com/codingsince1985/checksum/stargazers) - Compute message digest, like MD5, SHA256, SHA1, CRC or BLAKE2s, for large files.
- [copy](https://github.com/otiai10/copy) [![GitHub stars](https://img.shields.io/github/stars/otiai10/copy?style=flat)](https://github.com/otiai10/copy/stargazers) - Copy directory recursively.
- [fastwalk](https://github.com/charlievieth/fastwalk) [![GitHub stars](https://img.shields.io/github/stars/charlievieth/fastwalk?style=flat)](https://github.com/charlievieth/fastwalk/stargazers) - Fast parallel directory traversal library (used by [fzf](https://github.com/junegunn/fzf) [![GitHub stars](https://img.shields.io/github/stars/junegunn/fzf?style=flat)](https://github.com/junegunn/fzf/stargazers)).
- [flop](https://github.com/homedepot/flop) [![GitHub stars](https://img.shields.io/github/stars/homedepot/flop?style=flat)](https://github.com/homedepot/flop/stargazers) - File operations library which aims to mirror feature parity with [GNU cp](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html).
- [gdu](https://github.com/dundee/gdu) [![GitHub stars](https://img.shields.io/github/stars/dundee/gdu?style=flat)](https://github.com/dundee/gdu/stargazers) - Disk usage analyzer with console interface.
- [go-csv-tag](https://github.com/artonge/go-csv-tag) [![GitHub stars](https://img.shields.io/github/stars/artonge/go-csv-tag?style=flat)](https://github.com/artonge/go-csv-tag/stargazers) - Load csv file using tag.
- [go-decent-copy](https://github.com/hugocarreira/go-decent-copy) [![GitHub stars](https://img.shields.io/github/stars/hugocarreira/go-decent-copy?style=flat)](https://github.com/hugocarreira/go-decent-copy/stargazers) - Copy files for humans.
- [go-exiftool](https://github.com/barasher/go-exiftool) [![GitHub stars](https://img.shields.io/github/stars/barasher/go-exiftool?style=flat)](https://github.com/barasher/go-exiftool/stargazers) - Go bindings for ExifTool, the well-known library used to extract as much metadata as possible (EXIF, IPTC, ...) from files (pictures, PDF, office, ...).
- [go-gtfs](https://github.com/artonge/go-gtfs) [![GitHub stars](https://img.shields.io/github/stars/artonge/go-gtfs?style=flat)](https://github.com/artonge/go-gtfs/stargazers) - Load gtfs files in go.
- [go-wkhtmltopdf](https://github.com/SebastiaanKlippert/go-wkhtmltopdf) [![GitHub stars](https://img.shields.io/github/stars/SebastiaanKlippert/go-wkhtmltopdf?style=flat)](https://github.com/SebastiaanKlippert/go-wkhtmltopdf/stargazers) - A package to convert an HTML template to a PDF file.
- [gofs](https://github.com/no-src/gofs) [![GitHub stars](https://img.shields.io/github/stars/no-src/gofs?style=flat)](https://github.com/no-src/gofs/stargazers) - A cross-platform real-time file synchronization tool out of the box.
- [gulter](https://github.com/adelowo/gulter) [![GitHub stars](https://img.shields.io/github/stars/adelowo/gulter?style=flat)](https://github.com/adelowo/gulter/stargazers) - A simple HTTP middleware to automatically handle all your file upload needs
- [gut/yos](https://github.com/1set/gut) [![GitHub stars](https://img.shields.io/github/stars/1set/gut?style=flat)](https://github.com/1set/gut/stargazers) - Simple and reliable package for file operations like copy/move/diff/list on files, directories and symbolic links.
- [gxpdf](https://github.com/coregx/gxpdf) [![GitHub stars](https://img.shields.io/github/stars/coregx/gxpdf?style=flat)](https://github.com/coregx/gxpdf/stargazers) - Modern full-lifecycle PDF library for Go — parse, extract tables, generate, and sign documents with zero CGO dependencies.
- [higgs](https://github.com/dastoori/higgs) [![GitHub stars](https://img.shields.io/github/stars/dastoori/higgs?style=flat)](https://github.com/dastoori/higgs/stargazers) - A tiny cross-platform Go library to hide/unhide files and directories.
- [iso9660](https://github.com/kdomanski/iso9660) [![GitHub stars](https://img.shields.io/github/stars/kdomanski/iso9660?style=flat)](https://github.com/kdomanski/iso9660/stargazers) - A package for reading and creating ISO9660 disk images
- [notify](https://github.com/rjeczalik/notify) [![GitHub stars](https://img.shields.io/github/stars/rjeczalik/notify?style=flat)](https://github.com/rjeczalik/notify/stargazers) - File system event notification library with simple API, similar to os/signal.
- [opc](https://github.com/qmuntal/opc) [![GitHub stars](https://img.shields.io/github/stars/qmuntal/opc?style=flat)](https://github.com/qmuntal/opc/stargazers) - Load Open Packaging Conventions (OPC) files for Go.
- [parquet](https://github.com/parsyl/parquet) [![GitHub stars](https://img.shields.io/github/stars/parsyl/parquet?style=flat)](https://github.com/parsyl/parquet/stargazers) - Read and write [parquet](https://parquet.apache.org) files.
- [pathtype](https://github.com/jonchun/pathtype) [![GitHub stars](https://img.shields.io/github/stars/jonchun/pathtype?style=flat)](https://github.com/jonchun/pathtype/stargazers) - Treat paths as their own type instead of using strings.
- [pdfcpu](https://github.com/pdfcpu/pdfcpu) [![GitHub stars](https://img.shields.io/github/stars/pdfcpu/pdfcpu?style=flat)](https://github.com/pdfcpu/pdfcpu/stargazers) - PDF processor.
- [skywalker](https://github.com/dixonwille/skywalker) [![GitHub stars](https://img.shields.io/github/stars/dixonwille/skywalker?style=flat)](https://github.com/dixonwille/skywalker/stargazers) - Package to allow one to concurrently go through a filesystem with ease.
- [todotxt](https://github.com/1set/todotxt) [![GitHub stars](https://img.shields.io/github/stars/1set/todotxt?style=flat)](https://github.com/1set/todotxt/stargazers) - Go library for Gina Trapani's [_todo.txt_](http://todotxt.org/) files, supports parsing and manipulating of task lists in the [_todo.txt_ format](https://github.com/todotxt/todo.txt) [![GitHub stars](https://img.shields.io/github/stars/todotxt/todo.txt?style=flat)](https://github.com/todotxt/todo.txt/stargazers).
- [vfs](https://github.com/C2FO/vfs) [![GitHub stars](https://img.shields.io/github/stars/C2FO/vfs?style=flat)](https://github.com/C2FO/vfs/stargazers) - A pluggable, extensible, and opinionated set of filesystem functionality for Go across a number of filesystem types such as os, S3, and GCS.

**[⬆ back to top](#contents)**

## Financial

_Packages for accounting and finance._

- [accounting](https://github.com/leekchan/accounting) [![GitHub stars](https://img.shields.io/github/stars/leekchan/accounting?style=flat)](https://github.com/leekchan/accounting/stargazers) - money and currency formatting for golang.
- [ach](https://github.com/moov-io/ach) [![GitHub stars](https://img.shields.io/github/stars/moov-io/ach?style=flat)](https://github.com/moov-io/ach/stargazers) - A reader, writer, and validator for Automated Clearing House (ACH) files.
- [bbgo](https://github.com/c9s/bbgo) [![GitHub stars](https://img.shields.io/github/stars/c9s/bbgo?style=flat)](https://github.com/c9s/bbgo/stargazers) - A crypto trading bot framework written in Go. Including common crypto exchange API, standard indicators, back-testing and many built-in strategies.
- [currency](https://github.com/bojanz/currency) [![GitHub stars](https://img.shields.io/github/stars/bojanz/currency?style=flat)](https://github.com/bojanz/currency/stargazers) - Handles currency amounts, provides currency information and formatting.
- [currency](https://github.com/naughtygopher/currency) [![GitHub stars](https://img.shields.io/github/stars/naughtygopher/currency?style=flat)](https://github.com/naughtygopher/currency/stargazers) - High performant & accurate currency computation package.
- [dec128](https://github.com/jokruger/dec128) [![GitHub stars](https://img.shields.io/github/stars/jokruger/dec128?style=flat)](https://github.com/jokruger/dec128/stargazers) - High performance 128-bit fixed-point decimal numbers.
- [decimal](https://github.com/shopspring/decimal) [![GitHub stars](https://img.shields.io/github/stars/shopspring/decimal?style=flat)](https://github.com/shopspring/decimal/stargazers) - Arbitrary-precision fixed-point decimal numbers.
- [decimal](https://github.com/aytechnet/decimal) [![GitHub stars](https://img.shields.io/github/stars/aytechnet/decimal?style=flat)](https://github.com/aytechnet/decimal/stargazers) - High performance 64-bit decimal partially compatible with [shopspring/decimal](https://github.com/shopspring/decimal) [![GitHub stars](https://img.shields.io/github/stars/shopspring/decimal?style=flat)](https://github.com/shopspring/decimal/stargazers) and int64, including Weight and Length.
- [decimal](https://github.com/govalues/decimal) [![GitHub stars](https://img.shields.io/github/stars/govalues/decimal?style=flat)](https://github.com/govalues/decimal/stargazers) - Immutable decimal numbers with panic-free arithmetic.
- [fpdecimal](https://github.com/nikolaydubina/fpdecimal) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/fpdecimal?style=flat)](https://github.com/nikolaydubina/fpdecimal/stargazers) - Fast and precise serialization and arithmetic for small fixed-point decimals
- [fpmoney](https://github.com/nikolaydubina/fpmoney) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/fpmoney?style=flat)](https://github.com/nikolaydubina/fpmoney/stargazers) - Fast and simple ISO4217 fixed-point decimal money.
- [go-finance](https://github.com/alpeb/go-finance) [![GitHub stars](https://img.shields.io/github/stars/alpeb/go-finance?style=flat)](https://github.com/alpeb/go-finance/stargazers) - Library of financial functions for time value of money (annuities), cash flow, interest rate conversions, bonds and depreciation calculations.
- [go-finance](https://github.com/pieterclaerhout/go-finance) [![GitHub stars](https://img.shields.io/github/stars/pieterclaerhout/go-finance?style=flat)](https://github.com/pieterclaerhout/go-finance/stargazers) - Module to fetch exchange rates, check VAT numbers via VIES and check IBAN bank account numbers.
- [go-money](https://github.com/rhymond/go-money) [![GitHub stars](https://img.shields.io/github/stars/rhymond/go-money?style=flat)](https://github.com/rhymond/go-money/stargazers) - Implementation of Fowler's Money pattern.
- [go-nowpayments](https://github.com/matm/go-nowpayments) [![GitHub stars](https://img.shields.io/github/stars/matm/go-nowpayments?style=flat)](https://github.com/matm/go-nowpayments/stargazers) - Library for the crypto NOWPayments API.
- [gobl](https://github.com/invopop/gobl) [![GitHub stars](https://img.shields.io/github/stars/invopop/gobl?style=flat)](https://github.com/invopop/gobl/stargazers) - Invoice and billing document framework. JSON Schema based. Automates tax calculations and validation, with tooling to convert into global formats.
- [indicator](https://github.com/cinar/indicator) [![GitHub stars](https://img.shields.io/github/stars/cinar/indicator?style=flat)](https://github.com/cinar/indicator/stargazers) - Technical analysis library providing financial indicators, strategies, and backtesting framework.
- [ledger](https://github.com/formancehq/ledger) [![GitHub stars](https://img.shields.io/github/stars/formancehq/ledger?style=flat)](https://github.com/formancehq/ledger/stargazers) - A programmable financial ledger that provides a foundation for money-moving applications.
- [money](https://github.com/govalues/money) [![GitHub stars](https://img.shields.io/github/stars/govalues/money?style=flat)](https://github.com/govalues/money/stargazers) - Immutable monetary amounts and exchange rates with panic-free arithmetic.
- [ofxgo](https://github.com/aclindsa/ofxgo) [![GitHub stars](https://img.shields.io/github/stars/aclindsa/ofxgo?style=flat)](https://github.com/aclindsa/ofxgo/stargazers) - Query OFX servers and/or parse the responses (with example command-line client).
- [orderbook](https://github.com/i25959341/orderbook) [![GitHub stars](https://img.shields.io/github/stars/i25959341/orderbook?style=flat)](https://github.com/i25959341/orderbook/stargazers) - Matching Engine for Limit Order Book in Golang.
- [payme](https://github.com/jovandeginste/payme) [![GitHub stars](https://img.shields.io/github/stars/jovandeginste/payme?style=flat)](https://github.com/jovandeginste/payme/stargazers) - QR code generator (ASCII & PNG) for SEPA payments.
- [paystack-sdk-go](https://github.com/samaasi/paystack-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/samaasi/paystack-sdk-go?style=flat)](https://github.com/samaasi/paystack-sdk-go/stargazers) - A comprehensive, zero-dependency, and fully typed Go SDK for the Paystack API.
- [swift](https://code.pfad.fr/swift/) - Offline validity check of IBAN (International Bank Account Number) and retrieval of BIC (for some countries).
- [techan](https://github.com/sdcoffey/techan) [![GitHub stars](https://img.shields.io/github/stars/sdcoffey/techan?style=flat)](https://github.com/sdcoffey/techan/stargazers) - Technical analysis library with advanced market analysis and trading strategies.
- [ticker](https://github.com/achannarasappa/ticker) [![GitHub stars](https://img.shields.io/github/stars/achannarasappa/ticker?style=flat)](https://github.com/achannarasappa/ticker/stargazers) - Terminal stock watcher and stock position tracker.
- [transaction](https://github.com/claygod/transaction) [![GitHub stars](https://img.shields.io/github/stars/claygod/transaction?style=flat)](https://github.com/claygod/transaction/stargazers) - Embedded transactional database of accounts, running in multithreaded mode.
- [udecimal](https://github.com/quagmt/udecimal) [![GitHub stars](https://img.shields.io/github/stars/quagmt/udecimal?style=flat)](https://github.com/quagmt/udecimal/stargazers) - High performance, high precision, zero allocation fixed-point decimal library for financial applications.
- [vat](https://github.com/dannyvankooten/vat) [![GitHub stars](https://img.shields.io/github/stars/dannyvankooten/vat?style=flat)](https://github.com/dannyvankooten/vat/stargazers) - VAT number validation & EU VAT rates.

**[⬆ back to top](#contents)**

## Forms

_Libraries for working with forms._

- [bind](https://github.com/robfig/bind) [![GitHub stars](https://img.shields.io/github/stars/robfig/bind?style=flat)](https://github.com/robfig/bind/stargazers) - Bind form data to any Go values.
- [checker](https://github.com/cinar/checker) [![GitHub stars](https://img.shields.io/github/stars/cinar/checker?style=flat)](https://github.com/cinar/checker/stargazers) - Checker helps validating user input through rules defined in struct tags or directly through functions.
- [conform](https://github.com/leebenson/conform) [![GitHub stars](https://img.shields.io/github/stars/leebenson/conform?style=flat)](https://github.com/leebenson/conform/stargazers) - Keeps user input in check. Trims, sanitizes & scrubs data based on struct tags.
- [form](https://github.com/go-playground/form) [![GitHub stars](https://img.shields.io/github/stars/go-playground/form?style=flat)](https://github.com/go-playground/form/stargazers) - Decodes url.Values into Go value(s) and Encodes Go value(s) into url.Values. Dual Array and Full map support.
- [formam](https://github.com/monoculum/formam) [![GitHub stars](https://img.shields.io/github/stars/monoculum/formam?style=flat)](https://github.com/monoculum/formam/stargazers) - decode form's values into a struct.
- [forms](https://github.com/albrow/forms) [![GitHub stars](https://img.shields.io/github/stars/albrow/forms?style=flat)](https://github.com/albrow/forms/stargazers) - Framework-agnostic library for parsing and validating form/JSON data which supports multipart forms and files.
- [gbind](https://github.com/bdjimmy/gbind) [![GitHub stars](https://img.shields.io/github/stars/bdjimmy/gbind?style=flat)](https://github.com/bdjimmy/gbind/stargazers) - Bind data to any Go value. Can use built-in and custom expression binding capabilities; supports data validation
- [gorilla/csrf](https://github.com/gorilla/csrf) [![GitHub stars](https://img.shields.io/github/stars/gorilla/csrf?style=flat)](https://github.com/gorilla/csrf/stargazers) - CSRF protection for Go web applications & services.
- [httpin](https://github.com/ggicci/httpin) [![GitHub stars](https://img.shields.io/github/stars/ggicci/httpin?style=flat)](https://github.com/ggicci/httpin/stargazers) - Decode an HTTP request into a custom struct, including querystring, forms, HTTP headers, etc.
- [nosurf](https://github.com/justinas/nosurf) [![GitHub stars](https://img.shields.io/github/stars/justinas/nosurf?style=flat)](https://github.com/justinas/nosurf/stargazers) - CSRF protection middleware for Go.
- [qs](https://github.com/sonh/qs) [![GitHub stars](https://img.shields.io/github/stars/sonh/qs?style=flat)](https://github.com/sonh/qs/stargazers) - Go module for encoding structs into URL query parameters.
- [queryparam](https://github.com/tomwright/queryparam) [![GitHub stars](https://img.shields.io/github/stars/tomwright/queryparam?style=flat)](https://github.com/tomwright/queryparam/stargazers) - Decode `url.Values` into usable struct values of standard or custom types.
- [roamer](https://github.com/slipros/roamer) [![GitHub stars](https://img.shields.io/github/stars/slipros/roamer?style=flat)](https://github.com/slipros/roamer/stargazers) - Eliminates boilerplate code for parsing HTTP requests by binding cookies, headers, query params, path params, body to structs and more by using simple tags.

**[⬆ back to top](#contents)**

## Functional

_Packages to support functional programming in Go._

- [fp-go](https://github.com/repeale/fp-go) [![GitHub stars](https://img.shields.io/github/stars/repeale/fp-go?style=flat)](https://github.com/repeale/fp-go/stargazers) - Collection of Functional Programming helpers powered by Golang 1.18+ generics.
- [fpGo](https://github.com/TeaEntityLab/fpGo) [![GitHub stars](https://img.shields.io/github/stars/TeaEntityLab/fpGo?style=flat)](https://github.com/TeaEntityLab/fpGo/stargazers) - Monad, Functional Programming features for Golang.
- [fuego](https://github.com/seborama/fuego) [![GitHub stars](https://img.shields.io/github/stars/seborama/fuego?style=flat)](https://github.com/seborama/fuego/stargazers) - Functional Experiment in Go.
- [FuncFrog](https://github.com/koss-null/FuncFrog) [![GitHub stars](https://img.shields.io/github/stars/koss-null/FuncFrog?style=flat)](https://github.com/koss-null/FuncFrog/stargazers) - Functional helpers library providing Map, Filter, Reduce and other stream operations on generic slices Go1.18+ with lazy evaluation and error handling mechanisms.
- [g](https://github.com/enetx/g) [![GitHub stars](https://img.shields.io/github/stars/enetx/g?style=flat)](https://github.com/enetx/g/stargazers) - Functional programming framework for Go.
- [go-functional](https://github.com/BooleanCat/go-functional) [![GitHub stars](https://img.shields.io/github/stars/BooleanCat/go-functional?style=flat)](https://github.com/BooleanCat/go-functional/stargazers) - Functional programming in Go using generics
- [go-underscore](https://github.com/tobyhede/go-underscore) [![GitHub stars](https://img.shields.io/github/stars/tobyhede/go-underscore?style=flat)](https://github.com/tobyhede/go-underscore/stargazers) - Useful collection of helpfully functional Go collection utilities.
- [gofp](https://github.com/rbrahul/gofp) [![GitHub stars](https://img.shields.io/github/stars/rbrahul/gofp?style=flat)](https://github.com/rbrahul/gofp/stargazers) - A lodash like powerful utility library for Golang.
- [mo](https://github.com/samber/mo) [![GitHub stars](https://img.shields.io/github/stars/samber/mo?style=flat)](https://github.com/samber/mo/stargazers) - Monads and popular FP abstractions, based on Go 1.18+ Generics (Option, Result, Either...).
- [underscore](https://github.com/rjNemo/underscore) [![GitHub stars](https://img.shields.io/github/stars/rjNemo/underscore?style=flat)](https://github.com/rjNemo/underscore/stargazers) - Functional programming helpers for Go 1.18 and beyond.
- [valor](https://github.com/phelmkamp/valor) [![GitHub stars](https://img.shields.io/github/stars/phelmkamp/valor?style=flat)](https://github.com/phelmkamp/valor/stargazers) - Generic option and result types that optionally contain a value.

**[⬆ back to top](#contents)**

## Game Development

_Awesome game development libraries._

- [Ark](https://github.com/mlange-42/ark) [![GitHub stars](https://img.shields.io/github/stars/mlange-42/ark?style=flat)](https://github.com/mlange-42/ark/stargazers) - Archetype-based Entity Component System (ECS) for Go.
- [Ebitengine](https://github.com/hajimehoshi/ebiten) [![GitHub stars](https://img.shields.io/github/stars/hajimehoshi/ebiten?style=flat)](https://github.com/hajimehoshi/ebiten/stargazers) - dead simple 2D game engine in Go.
- [ecs](https://github.com/andygeiss/ecs) [![GitHub stars](https://img.shields.io/github/stars/andygeiss/ecs?style=flat)](https://github.com/andygeiss/ecs/stargazers) - Build your own Game-Engine based on the Entity Component System concept in Golang.
- [engo](https://github.com/EngoEngine/engo) [![GitHub stars](https://img.shields.io/github/stars/EngoEngine/engo?style=flat)](https://github.com/EngoEngine/engo/stargazers) - Engo is an open-source 2D game engine written in Go. It follows the Entity-Component-System paradigm.
- [fantasyname](https://github.com/s0rg/fantasyname) [![GitHub stars](https://img.shields.io/github/stars/s0rg/fantasyname?style=flat)](https://github.com/s0rg/fantasyname/stargazers) - Fantasy names generator.
- [g3n](https://github.com/g3n/engine) [![GitHub stars](https://img.shields.io/github/stars/g3n/engine?style=flat)](https://github.com/g3n/engine/stargazers) - Go 3D Game Engine.
- [go-astar](https://github.com/beefsack/go-astar) [![GitHub stars](https://img.shields.io/github/stars/beefsack/go-astar?style=flat)](https://github.com/beefsack/go-astar/stargazers) - Go implementation of the A\* path finding algorithm.
- [go-sdl2](https://github.com/veandco/go-sdl2) [![GitHub stars](https://img.shields.io/github/stars/veandco/go-sdl2?style=flat)](https://github.com/veandco/go-sdl2/stargazers) - Go bindings for the [Simple DirectMedia Layer](https://www.libsdl.org/).
- [go3d](https://github.com/ungerik/go3d) [![GitHub stars](https://img.shields.io/github/stars/ungerik/go3d?style=flat)](https://github.com/ungerik/go3d/stargazers) - Performance oriented 2D/3D math package for Go.
- [gogpu](https://github.com/gogpu/gogpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu/gogpu?style=flat)](https://github.com/gogpu/gogpu/stargazers) - GPU application framework with windowing, input, and rendering built on WebGPU — reduces 480+ lines of GPU code to ~20, zero CGO (GoGPU ecosystem: [gg](https://github.com/gogpu/gg) [![GitHub stars](https://img.shields.io/github/stars/gogpu/gg?style=flat)](https://github.com/gogpu/gg/stargazers), [ui](https://github.com/gogpu/ui) [![GitHub stars](https://img.shields.io/github/stars/gogpu/ui?style=flat)](https://github.com/gogpu/ui/stargazers), [wgpu](https://github.com/gogpu/wgpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu/wgpu?style=flat)](https://github.com/gogpu/wgpu/stargazers), [naga](https://github.com/gogpu/naga) [![GitHub stars](https://img.shields.io/github/stars/gogpu/naga?style=flat)](https://github.com/gogpu/naga/stargazers)).
- [gogpu/wgpu](https://github.com/gogpu/wgpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu/wgpu?style=flat)](https://github.com/gogpu/wgpu/stargazers) - Pure Go WebGPU implementation with Vulkan, DX12, and Metal backends, zero CGO (part of [GoGPU](https://github.com/gogpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu?style=flat)](https://github.com/gogpu/stargazers) ecosystem).
- [GOKe](https://github.com/kjkrol/goke) [![GitHub stars](https://img.shields.io/github/stars/kjkrol/goke?style=flat)](https://github.com/kjkrol/goke/stargazers) - Data-Oriented (DOD), archetype-based ECS engine utilizing an L1 cache-aligned chunked SoA layout for predictable, stepless memory growth and zero-allocation execution paths.
- [gonet](https://github.com/xtaci/gonet) [![GitHub stars](https://img.shields.io/github/stars/xtaci/gonet?style=flat)](https://github.com/xtaci/gonet/stargazers) - Game server skeleton implemented with golang.
- [goworld](https://github.com/xiaonanln/goworld) [![GitHub stars](https://img.shields.io/github/stars/xiaonanln/goworld?style=flat)](https://github.com/xiaonanln/goworld/stargazers) - Scalable game server engine, featuring space-entity framework and hot-swapping.
- [grid](https://github.com/s0rg/grid) [![GitHub stars](https://img.shields.io/github/stars/s0rg/grid?style=flat)](https://github.com/s0rg/grid/stargazers) - Generic 2D grid with ray-casting, shadow-casting and path finding.
- [Leaf](https://github.com/name5566/leaf) [![GitHub stars](https://img.shields.io/github/stars/name5566/leaf?style=flat)](https://github.com/name5566/leaf/stargazers) - Lightweight game server framework.
- [nano](https://github.com/lonng/nano) [![GitHub stars](https://img.shields.io/github/stars/lonng/nano?style=flat)](https://github.com/lonng/nano/stargazers) - Lightweight, facility, high performance golang based game server framework.
- [Oak](https://github.com/oakmound/oak) [![GitHub stars](https://img.shields.io/github/stars/oakmound/oak?style=flat)](https://github.com/oakmound/oak/stargazers) - Pure Go game engine.
- [Pi](https://github.com/elgopher/pi) [![GitHub stars](https://img.shields.io/github/stars/elgopher/pi?style=flat)](https://github.com/elgopher/pi/stargazers) - Game engine for creating retro games for modern computers. Inspired by Pico-8 and powered by Ebitengine.
- [Pitaya](https://github.com/topfreegames/pitaya) [![GitHub stars](https://img.shields.io/github/stars/topfreegames/pitaya?style=flat)](https://github.com/topfreegames/pitaya/stargazers) - Scalable game server framework with clustering support and client libraries for iOS, Android, Unity and others through the C SDK.
- [Pixel](https://github.com/gopxl/pixel) [![GitHub stars](https://img.shields.io/github/stars/gopxl/pixel?style=flat)](https://github.com/gopxl/pixel/stargazers) - Hand-crafted 2D game library in Go.
- [prototype](https://github.com/gonutz/prototype) [![GitHub stars](https://img.shields.io/github/stars/gonutz/prototype?style=flat)](https://github.com/gonutz/prototype/stargazers) - Cross-platform (Windows/Linux/Mac) library for creating desktop games using a minimal API.
- [raylib-go](https://github.com/gen2brain/raylib-go) [![GitHub stars](https://img.shields.io/github/stars/gen2brain/raylib-go?style=flat)](https://github.com/gen2brain/raylib-go/stargazers) - Go bindings for [raylib](https://www.raylib.com/), a simple and easy-to-use library to learn videogames programming.
- [termloop](https://github.com/JoelOtter/termloop) [![GitHub stars](https://img.shields.io/github/stars/JoelOtter/termloop?style=flat)](https://github.com/JoelOtter/termloop/stargazers) - Terminal-based game engine for Go, built on top of Termbox.
- [tile](https://github.com/kelindar/tile) [![GitHub stars](https://img.shields.io/github/stars/kelindar/tile?style=flat)](https://github.com/kelindar/tile/stargazers) - Data-oriented and cache-friendly 2D Grid library (TileMap), includes pathfinding, observers and import/export.

**[⬆ back to top](#contents)**

## Generators

_Tools that generate Go code._

- [convergen](https://github.com/reedom/convergen) [![GitHub stars](https://img.shields.io/github/stars/reedom/convergen?style=flat)](https://github.com/reedom/convergen/stargazers) - Feature rich type-to-type copy code generator.
- [copygen](https://github.com/switchupcb/copygen) [![GitHub stars](https://img.shields.io/github/stars/switchupcb/copygen?style=flat)](https://github.com/switchupcb/copygen/stargazers) - Generate any code based on Go types, including type-to-type converters (copy code) without reflection by default.
- [generis](https://github.com/senselogic/GENERIS) [![GitHub stars](https://img.shields.io/github/stars/senselogic/GENERIS?style=flat)](https://github.com/senselogic/GENERIS/stargazers) - Code generation tool providing generics, free-form macros, conditional compilation and HTML templating.
- [go-apispec](https://github.com/antst/go-apispec) [![GitHub stars](https://img.shields.io/github/stars/antst/go-apispec?style=flat)](https://github.com/antst/go-apispec/stargazers) - Generate OpenAPI 3.1 specs from Go source code via static analysis with automatic framework detection.
- [go-enum](https://github.com/abice/go-enum) [![GitHub stars](https://img.shields.io/github/stars/abice/go-enum?style=flat)](https://github.com/abice/go-enum/stargazers) - Code generation for enums from code comments.
- [go-enum-encoding](https://github.com/nikolaydubina/go-enum-encoding) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/go-enum-encoding?style=flat)](https://github.com/nikolaydubina/go-enum-encoding/stargazers) - Code generation for enum encoding from code comments.
- [go-linq](https://github.com/ahmetalpbalkan/go-linq) [![GitHub stars](https://img.shields.io/github/stars/ahmetalpbalkan/go-linq?style=flat)](https://github.com/ahmetalpbalkan/go-linq/stargazers) - .NET LINQ-like query methods for Go.
- [goderive](https://github.com/awalterschulze/goderive) [![GitHub stars](https://img.shields.io/github/stars/awalterschulze/goderive?style=flat)](https://github.com/awalterschulze/goderive/stargazers) - Derives functions from input types
- [goverter](https://github.com/jmattheis/goverter) [![GitHub stars](https://img.shields.io/github/stars/jmattheis/goverter?style=flat)](https://github.com/jmattheis/goverter/stargazers) - Generate converters by defining an interface.
- [GoWrap](https://github.com/hexdigest/gowrap) [![GitHub stars](https://img.shields.io/github/stars/hexdigest/gowrap?style=flat)](https://github.com/hexdigest/gowrap/stargazers) - Generate decorators for Go interfaces using simple templates.
- [interfaces](https://github.com/rjeczalik/interfaces) [![GitHub stars](https://img.shields.io/github/stars/rjeczalik/interfaces?style=flat)](https://github.com/rjeczalik/interfaces/stargazers) - Command line tool for generating interface definitions.
- [jennifer](https://github.com/dave/jennifer) [![GitHub stars](https://img.shields.io/github/stars/dave/jennifer?style=flat)](https://github.com/dave/jennifer/stargazers) - Generate arbitrary Go code without templates.
- [oapi-codegen](https://github.com/deepmap/oapi-codegen) [![GitHub stars](https://img.shields.io/github/stars/deepmap/oapi-codegen?style=flat)](https://github.com/deepmap/oapi-codegen/stargazers) - This package contains a set of utilities for generating Go boilerplate code for services based on OpenAPI 3.0 API definitions.
- [protoc-gen-httpgo](https://github.com/MUlt1mate/protoc-gen-httpgo) [![GitHub stars](https://img.shields.io/github/stars/MUlt1mate/protoc-gen-httpgo?style=flat)](https://github.com/MUlt1mate/protoc-gen-httpgo/stargazers) - Generate HTTP server and client from protobuf.
- [typeregistry](https://github.com/xiaoxin01/typeregistry) [![GitHub stars](https://img.shields.io/github/stars/xiaoxin01/typeregistry?style=flat)](https://github.com/xiaoxin01/typeregistry/stargazers) - A library to create type dynamically.

**[⬆ back to top](#contents)**

## Geographic

_Geographic tools and servers_

- [borders](https://github.com/kpfaulkner/borders) [![GitHub stars](https://img.shields.io/github/stars/kpfaulkner/borders?style=flat)](https://github.com/kpfaulkner/borders/stargazers) - Detects image borders and converts to GeoJSON for GIS operations.
- [geoos](https://github.com/spatial-go/geoos) [![GitHub stars](https://img.shields.io/github/stars/spatial-go/geoos?style=flat)](https://github.com/spatial-go/geoos/stargazers) - A library provides spatial data and geometric algorithms.
- [geoserver](https://github.com/hishamkaram/geoserver) [![GitHub stars](https://img.shields.io/github/stars/hishamkaram/geoserver?style=flat)](https://github.com/hishamkaram/geoserver/stargazers) - geoserver Is a Go Package For Manipulating a GeoServer Instance via the GeoServer REST API.
- [gismanager](https://github.com/hishamkaram/gismanager) [![GitHub stars](https://img.shields.io/github/stars/hishamkaram/gismanager?style=flat)](https://github.com/hishamkaram/gismanager/stargazers) - Publish Your GIS Data(Vector Data) to PostGIS and Geoserver.
- [godal](https://github.com/airbusgeo/godal) [![GitHub stars](https://img.shields.io/github/stars/airbusgeo/godal?style=flat)](https://github.com/airbusgeo/godal/stargazers) - Go wrapper for GDAL.
- [H3](https://github.com/uber/h3-go) [![GitHub stars](https://img.shields.io/github/stars/uber/h3-go?style=flat)](https://github.com/uber/h3-go/stargazers) - Go bindings for H3, a hierarchical hexagonal geospatial indexing system.
- [H3 GeoJSON](https://github.com/mmadfox/go-geojson2h3) [![GitHub stars](https://img.shields.io/github/stars/mmadfox/go-geojson2h3?style=flat)](https://github.com/mmadfox/go-geojson2h3/stargazers) - Conversion utilities between H3 indexes and GeoJSON.
- [H3GeoDist](https://github.com/mmadfox/go-h3geo-dist) [![GitHub stars](https://img.shields.io/github/stars/mmadfox/go-h3geo-dist?style=flat)](https://github.com/mmadfox/go-h3geo-dist/stargazers) - Distribution of Uber H3geo cells by virtual nodes.
- [mbtileserver](https://github.com/consbio/mbtileserver) [![GitHub stars](https://img.shields.io/github/stars/consbio/mbtileserver?style=flat)](https://github.com/consbio/mbtileserver/stargazers) - A simple Go-based server for map tiles stored in mbtiles format.
- [osm](https://github.com/paulmach/osm) [![GitHub stars](https://img.shields.io/github/stars/paulmach/osm?style=flat)](https://github.com/paulmach/osm/stargazers) - Library for reading, writing and working with OpenStreetMap data and APIs.
- [pbf](https://github.com/maguro/pbf) [![GitHub stars](https://img.shields.io/github/stars/maguro/pbf?style=flat)](https://github.com/maguro/pbf/stargazers) - OpenStreetMap PBF golang encoder/decoder.
- [S2 geojson](https://github.com/pantrif/s2-geojson) [![GitHub stars](https://img.shields.io/github/stars/pantrif/s2-geojson?style=flat)](https://github.com/pantrif/s2-geojson/stargazers) - Convert geojson to s2 cells & demonstrating some S2 geometry features on map.
- [S2 geometry](https://github.com/golang/geo) [![GitHub stars](https://img.shields.io/github/stars/golang/geo?style=flat)](https://github.com/golang/geo/stargazers) - S2 geometry library in Go.
- [simplefeatures](https://github.com/peterstace/simplefeatures) [![GitHub stars](https://img.shields.io/github/stars/peterstace/simplefeatures?style=flat)](https://github.com/peterstace/simplefeatures/stargazers) - simplesfeatures is a 2D geometry library that provides Go types that model geometries, as well as algorithms that operate on them.
- [Tile38](https://github.com/tidwall/tile38) [![GitHub stars](https://img.shields.io/github/stars/tidwall/tile38?style=flat)](https://github.com/tidwall/tile38/stargazers) - Geolocation DB with spatial index and realtime geofencing.
- [Web-Mercator-Projection](https://github.com/jorelosorio/web-mercator-projection) [![GitHub stars](https://img.shields.io/github/stars/jorelosorio/web-mercator-projection?style=flat)](https://github.com/jorelosorio/web-mercator-projection/stargazers) A project to easily use and convert LonLat, Point and Tile to display info, markers, etc, in a map using the Web Mercator Projection.
- [WGS84](https://github.com/wroge/wgs84) [![GitHub stars](https://img.shields.io/github/stars/wroge/wgs84?style=flat)](https://github.com/wroge/wgs84/stargazers) - Library for Coordinate Conversion and Transformation (ETRS89, OSGB36, NAD83, RGF93, Web Mercator, UTM).

**[⬆ back to top](#contents)**

## Go Compilers

_Tools for compiling Go to other languages and vice-versa._

- [bunster](https://github.com/yassinebenaid/bunster) [![GitHub stars](https://img.shields.io/github/stars/yassinebenaid/bunster?style=flat)](https://github.com/yassinebenaid/bunster/stargazers) - Compile shell scripts to Go.
- [c4go](https://github.com/Konstantin8105/c4go) [![GitHub stars](https://img.shields.io/github/stars/Konstantin8105/c4go?style=flat)](https://github.com/Konstantin8105/c4go/stargazers) - Transpile C code to Go code.
- [cxgo](https://github.com/gotranspile/cxgo) [![GitHub stars](https://img.shields.io/github/stars/gotranspile/cxgo?style=flat)](https://github.com/gotranspile/cxgo/stargazers) - Transpile C code to Go code.
- [esp32](https://github.com/andygeiss/esp32-transpiler) [![GitHub stars](https://img.shields.io/github/stars/andygeiss/esp32-transpiler?style=flat)](https://github.com/andygeiss/esp32-transpiler/stargazers) - Transpile Go into Arduino code.
- [f4go](https://github.com/Konstantin8105/f4go) [![GitHub stars](https://img.shields.io/github/stars/Konstantin8105/f4go?style=flat)](https://github.com/Konstantin8105/f4go/stargazers) - Transpile FORTRAN 77 code to Go code.
- [go2hx](https://github.com/go2hx/go2hx) [![GitHub stars](https://img.shields.io/github/stars/go2hx/go2hx?style=flat)](https://github.com/go2hx/go2hx/stargazers) - Compiler from Go to Haxe to Javascript/C++/Java/C#.
- [gopherjs](https://github.com/gopherjs/gopherjs) [![GitHub stars](https://img.shields.io/github/stars/gopherjs/gopherjs?style=flat)](https://github.com/gopherjs/gopherjs/stargazers) - Compiler from Go to JavaScript.

**[⬆ back to top](#contents)**

## Goroutines

_Tools for managing and working with Goroutines._

- [anchor](https://github.com/kyuff/anchor) [![GitHub stars](https://img.shields.io/github/stars/kyuff/anchor?style=flat)](https://github.com/kyuff/anchor/stargazers) - Library to manage component lifecycle in microservice architectures.
- [ants](https://github.com/panjf2000/ants) [![GitHub stars](https://img.shields.io/github/stars/panjf2000/ants?style=flat)](https://github.com/panjf2000/ants/stargazers) - A high-performance and low-cost goroutine pool in Go.
- [artifex](https://github.com/borderstech/artifex) [![GitHub stars](https://img.shields.io/github/stars/borderstech/artifex?style=flat)](https://github.com/borderstech/artifex/stargazers) - Simple in-memory job queue for Golang using worker-based dispatching.
- [async](https://github.com/yaitoo/async) [![GitHub stars](https://img.shields.io/github/stars/yaitoo/async?style=flat)](https://github.com/yaitoo/async/stargazers) - An asynchronous task package with async/await style for Go.
- [async](https://github.com/reugn/async) [![GitHub stars](https://img.shields.io/github/stars/reugn/async?style=flat)](https://github.com/reugn/async/stargazers) - An alternative sync library for Go (Future, Promise, Locks).
- [async](https://github.com/studiosol/async) [![GitHub stars](https://img.shields.io/github/stars/studiosol/async?style=flat)](https://github.com/studiosol/async/stargazers) - A safe way to execute functions asynchronously, recovering them in case of panic.
- [async-job](https://github.com/lab210-dev/async-job) [![GitHub stars](https://img.shields.io/github/stars/lab210-dev/async-job?style=flat)](https://github.com/lab210-dev/async-job/stargazers) - AsyncJob is an asynchronous queue job manager with light code, clear and speed.
- [autopool](https://github.com/AshvinBambhaniya/autopool) [![GitHub stars](https://img.shields.io/github/stars/AshvinBambhaniya/autopool?style=flat)](https://github.com/AshvinBambhaniya/autopool/stargazers) - Zero-config, auto-scaling worker pool for Go with priority-aware scheduling.
- [breaker](https://github.com/kamilsk/breaker) [![GitHub stars](https://img.shields.io/github/stars/kamilsk/breaker?style=flat)](https://github.com/kamilsk/breaker/stargazers) - Flexible mechanism to make execution flow interruptible.
- [channelify](https://github.com/ddelizia/channelify) [![GitHub stars](https://img.shields.io/github/stars/ddelizia/channelify?style=flat)](https://github.com/ddelizia/channelify/stargazers) - Transform your function to return channels for easy and powerful parallel processing.
- [conc](https://github.com/sourcegraph/conc) [![GitHub stars](https://img.shields.io/github/stars/sourcegraph/conc?style=flat)](https://github.com/sourcegraph/conc/stargazers) - `conc` is your toolbelt for structured concurrency in go, making common tasks easier and safer.
- [concurrency-limiter](https://github.com/vivek-ng/concurrency-limiter) [![GitHub stars](https://img.shields.io/github/stars/vivek-ng/concurrency-limiter?style=flat)](https://github.com/vivek-ng/concurrency-limiter/stargazers) - Concurrency limiter with support for timeouts, dynamic priority and context cancellation of goroutines.
- [conexec](https://github.com/ITcathyh/conexec) [![GitHub stars](https://img.shields.io/github/stars/ITcathyh/conexec?style=flat)](https://github.com/ITcathyh/conexec/stargazers) - A concurrent toolkit to help execute funcs concurrently in an efficient and safe way. It supports specifying the overall timeout to avoid blocking and uses goroutine pool to improve efficiency.
- [cyclicbarrier](https://github.com/marusama/cyclicbarrier) [![GitHub stars](https://img.shields.io/github/stars/marusama/cyclicbarrier?style=flat)](https://github.com/marusama/cyclicbarrier/stargazers) - CyclicBarrier for golang.
- [execpool](https://github.com/hexdigest/execpool) [![GitHub stars](https://img.shields.io/github/stars/hexdigest/execpool?style=flat)](https://github.com/hexdigest/execpool/stargazers) - A pool built around exec.Cmd that spins up a given number of processes in advance and attaches stdin and stdout to them when needed. Very similar to FastCGI or Apache Prefork MPM but works for any command.
- [flowmatic](https://github.com/carlmjohnson/flowmatic) [![GitHub stars](https://img.shields.io/github/stars/carlmjohnson/flowmatic?style=flat)](https://github.com/carlmjohnson/flowmatic/stargazers) - Structured concurrency made easy.
- [go-accumulator](https://github.com/nar10z/go-accumulator) [![GitHub stars](https://img.shields.io/github/stars/nar10z/go-accumulator?style=flat)](https://github.com/nar10z/go-accumulator/stargazers) - Solution for accumulation of events and their subsequent processing.
- [go-actor](https://github.com/vladopajic/go-actor) [![GitHub stars](https://img.shields.io/github/stars/vladopajic/go-actor?style=flat)](https://github.com/vladopajic/go-actor/stargazers) - A tiny library for writing concurrent programs using actor model.
- [go-floc](https://github.com/workanator/go-floc) [![GitHub stars](https://img.shields.io/github/stars/workanator/go-floc?style=flat)](https://github.com/workanator/go-floc/stargazers) - Orchestrate goroutines with ease.
- [go-flow](https://github.com/kamildrazkiewicz/go-flow) [![GitHub stars](https://img.shields.io/github/stars/kamildrazkiewicz/go-flow?style=flat)](https://github.com/kamildrazkiewicz/go-flow/stargazers) - Control goroutines execution order.
- [go-tools/multithreading](https://github.com/nikhilsaraf/go-tools) [![GitHub stars](https://img.shields.io/github/stars/nikhilsaraf/go-tools?style=flat)](https://github.com/nikhilsaraf/go-tools/stargazers) - Manage a pool of goroutines using this lightweight library with a simple API.
- [go-trylock](https://github.com/subchen/go-trylock) [![GitHub stars](https://img.shields.io/github/stars/subchen/go-trylock?style=flat)](https://github.com/subchen/go-trylock/stargazers) - TryLock support on read-write lock for Golang.
- [go-waitgroup](https://github.com/pieterclaerhout/go-waitgroup) [![GitHub stars](https://img.shields.io/github/stars/pieterclaerhout/go-waitgroup?style=flat)](https://github.com/pieterclaerhout/go-waitgroup/stargazers) - Like `sync.WaitGroup` with error handling and concurrency control.
- [go-workerpool](https://github.com/zenthangplus/go-workerpool) [![GitHub stars](https://img.shields.io/github/stars/zenthangplus/go-workerpool?style=flat)](https://github.com/zenthangplus/go-workerpool/stargazers) - Inspired from Java Thread Pool, Go WorkerPool aims to control heavy Go Routines.
- [goccm](https://github.com/zenthangplus/goccm) [![GitHub stars](https://img.shields.io/github/stars/zenthangplus/goccm?style=flat)](https://github.com/zenthangplus/goccm/stargazers) - Go Concurrency Manager package limits the number of goroutines that allowed to run concurrently.
- [gohive](https://github.com/loveleshsharma/gohive) [![GitHub stars](https://img.shields.io/github/stars/loveleshsharma/gohive?style=flat)](https://github.com/loveleshsharma/gohive/stargazers) - A highly performant and easy to use Goroutine pool for Go.
- [gollback](https://github.com/vardius/gollback) [![GitHub stars](https://img.shields.io/github/stars/vardius/gollback?style=flat)](https://github.com/vardius/gollback/stargazers) - asynchronous simple function utilities, for managing execution of closures and callbacks.
- [gowl](https://github.com/hamed-yousefi/gowl) [![GitHub stars](https://img.shields.io/github/stars/hamed-yousefi/gowl?style=flat)](https://github.com/hamed-yousefi/gowl/stargazers) - Gowl is a process management and process monitoring tool at once. An infinite worker pool gives you the ability to control the pool and processes and monitor their status.
- [goworker](https://github.com/benmanns/goworker) [![GitHub stars](https://img.shields.io/github/stars/benmanns/goworker?style=flat)](https://github.com/benmanns/goworker/stargazers) - goworker is a Go-based background worker.
- [gowp](https://github.com/xxjwxc/gowp) [![GitHub stars](https://img.shields.io/github/stars/xxjwxc/gowp?style=flat)](https://github.com/xxjwxc/gowp/stargazers) - gowp is concurrency limiting goroutine pool.
- [gpool](https://github.com/Sherifabdlnaby/gpool) [![GitHub stars](https://img.shields.io/github/stars/Sherifabdlnaby/gpool?style=flat)](https://github.com/Sherifabdlnaby/gpool/stargazers) - manages a resizeable pool of context-aware goroutines to bound concurrency.
- [grpool](https://github.com/ivpusic/grpool) [![GitHub stars](https://img.shields.io/github/stars/ivpusic/grpool?style=flat)](https://github.com/ivpusic/grpool/stargazers) - Lightweight Goroutine pool.
- [hands](https://github.com/duanckham/hands) [![GitHub stars](https://img.shields.io/github/stars/duanckham/hands?style=flat)](https://github.com/duanckham/hands/stargazers) - A process controller used to control the execution and return strategies of multiple goroutines.
- [Hunch](https://github.com/AaronJan/Hunch) [![GitHub stars](https://img.shields.io/github/stars/AaronJan/Hunch?style=flat)](https://github.com/AaronJan/Hunch/stargazers) - Hunch provides functions like: `All`, `First`, `Retry`, `Waterfall` etc., that makes asynchronous flow control more intuitive.
- [kyoo](https://github.com/dirkaholic/kyoo) [![GitHub stars](https://img.shields.io/github/stars/dirkaholic/kyoo?style=flat)](https://github.com/dirkaholic/kyoo/stargazers) - Provides an unlimited job queue and concurrent worker pools.
- [neilotoole/errgroup](https://github.com/neilotoole/errgroup) [![GitHub stars](https://img.shields.io/github/stars/neilotoole/errgroup?style=flat)](https://github.com/neilotoole/errgroup/stargazers) - Drop-in alternative to `sync/errgroup`, limited to a pool of N worker goroutines.
- [nursery](https://github.com/arunsworld/nursery) [![GitHub stars](https://img.shields.io/github/stars/arunsworld/nursery?style=flat)](https://github.com/arunsworld/nursery/stargazers) - Structured concurrency in Go.
- [oversight](https://pkg.go.dev/cirello.io/oversight) - Oversight is a complete implementation of the Erlang supervision trees.
- [parallel-fn](https://github.com/rafaeljesus/parallel-fn) [![GitHub stars](https://img.shields.io/github/stars/rafaeljesus/parallel-fn?style=flat)](https://github.com/rafaeljesus/parallel-fn/stargazers) - Run functions in parallel.
- [pond](https://github.com/alitto/pond) [![GitHub stars](https://img.shields.io/github/stars/alitto/pond?style=flat)](https://github.com/alitto/pond/stargazers) - Minimalistic and High-performance goroutine worker pool written in Go.
- [pool](https://github.com/go-playground/pool) [![GitHub stars](https://img.shields.io/github/stars/go-playground/pool?style=flat)](https://github.com/go-playground/pool/stargazers) - Limited consumer goroutine or unlimited goroutine pool for easier goroutine handling and cancellation.
- [rill](https://github.com/destel/rill) [![GitHub stars](https://img.shields.io/github/stars/destel/rill?style=flat)](https://github.com/destel/rill/stargazers) - Go toolkit for clean, composable, channel-based concurrency.
- [routine](https://github.com/timandy/routine) [![GitHub stars](https://img.shields.io/github/stars/timandy/routine?style=flat)](https://github.com/timandy/routine/stargazers) - `routine` is a `ThreadLocal` for go library. It encapsulates and provides some easy-to-use, non-competitive, high-performance `goroutine` context access interfaces, which can help you access coroutine context information more gracefully.
- [routine](https://github.com/x-mod/routine) [![GitHub stars](https://img.shields.io/github/stars/x-mod/routine?style=flat)](https://github.com/x-mod/routine/stargazers) - go routine control with context, support: Main, Go, Pool and some useful Executors.
- [semaphore](https://github.com/kamilsk/semaphore) [![GitHub stars](https://img.shields.io/github/stars/kamilsk/semaphore?style=flat)](https://github.com/kamilsk/semaphore/stargazers) - Semaphore pattern implementation with timeout of lock/unlock operations based on channel and context.
- [semaphore](https://github.com/marusama/semaphore) [![GitHub stars](https://img.shields.io/github/stars/marusama/semaphore?style=flat)](https://github.com/marusama/semaphore/stargazers) - Fast resizable semaphore implementation based on CAS (faster than channel-based semaphore implementations).
- [stl](https://github.com/ssgreg/stl) [![GitHub stars](https://img.shields.io/github/stars/ssgreg/stl?style=flat)](https://github.com/ssgreg/stl/stargazers) - Software transactional locks based on Software Transactional Memory (STM) concurrency control mechanism.
- [threadpool](https://github.com/shettyh/threadpool) [![GitHub stars](https://img.shields.io/github/stars/shettyh/threadpool?style=flat)](https://github.com/shettyh/threadpool/stargazers) - Golang threadpool implementation.
- [tunny](https://github.com/Jeffail/tunny) [![GitHub stars](https://img.shields.io/github/stars/Jeffail/tunny?style=flat)](https://github.com/Jeffail/tunny/stargazers) - Goroutine pool for golang.
- [worker-pool](https://github.com/vardius/worker-pool) [![GitHub stars](https://img.shields.io/github/stars/vardius/worker-pool?style=flat)](https://github.com/vardius/worker-pool/stargazers) - goworker is a Go simple async worker pool.
- [workerpool](https://github.com/gammazero/workerpool) [![GitHub stars](https://img.shields.io/github/stars/gammazero/workerpool?style=flat)](https://github.com/gammazero/workerpool/stargazers) - Goroutine pool that limits the concurrency of task execution, not the number of tasks queued.

**[⬆ back to top](#contents)**

## GUI

_Libraries for building GUI Applications._

_Toolkits_

- [app](https://github.com/murlokswarm/app) [![GitHub stars](https://img.shields.io/github/stars/murlokswarm/app?style=flat)](https://github.com/murlokswarm/app/stargazers) - Package to create apps with GO, HTML and CSS. Supports: MacOS, Windows in progress.
- [cimgui-go](https://github.com/AllenDang/cimgui-go) [![GitHub stars](https://img.shields.io/github/stars/AllenDang/cimgui-go?style=flat)](https://github.com/AllenDang/cimgui-go/stargazers) - Auto generated Go wrapper for [Dear ImGui](https://github.com/ocornut/imgui) [![GitHub stars](https://img.shields.io/github/stars/ocornut/imgui?style=flat)](https://github.com/ocornut/imgui/stargazers) via [cimgui](https://github.com/cimgui/cimgui) [![GitHub stars](https://img.shields.io/github/stars/cimgui/cimgui?style=flat)](https://github.com/cimgui/cimgui/stargazers).
- [Cogent Core](https://github.com/cogentcore/core) [![GitHub stars](https://img.shields.io/github/stars/cogentcore/core?style=flat)](https://github.com/cogentcore/core/stargazers) - A framework for building 2D and 3D apps that run on macOS, Windows, Linux, iOS, Android, and the web.
- [DarwinKit](https://github.com/progrium/darwinkit) [![GitHub stars](https://img.shields.io/github/stars/progrium/darwinkit?style=flat)](https://github.com/progrium/darwinkit/stargazers) - Build native macOS applications using Go.
- [energy](https://github.com/energye/energy) [![GitHub stars](https://img.shields.io/github/stars/energye/energy?style=flat)](https://github.com/energye/energy/stargazers) - Cross-platform based on LCL(Native System UI Control Library) and CEF(Chromium Embedded Framework) (Windows/ macOS / Linux)
- [fyne](https://github.com/fyne-io/fyne) [![GitHub stars](https://img.shields.io/github/stars/fyne-io/fyne?style=flat)](https://github.com/fyne-io/fyne/stargazers) - Cross platform native GUIs designed for Go based on Material Design. Supports: Linux, macOS, Windows, BSD, iOS and Android.
- [gio](https://gioui.org) - Gio is a library for writing cross-platform immediate mode GUI-s in Go. Gio supports all the major platforms: Linux, macOS, Windows, Android, iOS, FreeBSD, OpenBSD and WebAssembly.
- [go-gtk](https://mattn.github.io/go-gtk/) - Go bindings for GTK.
- [go-sciter](https://github.com/sciter-sdk/go-sciter) [![GitHub stars](https://img.shields.io/github/stars/sciter-sdk/go-sciter?style=flat)](https://github.com/sciter-sdk/go-sciter/stargazers) - Go bindings for Sciter: the Embeddable HTML/CSS/script engine for modern desktop UI development. Cross platform.
- [Goey](https://bitbucket.org/rj/goey/src/master/) - Cross platform UI toolkit aggregator for Windows / Linux / Mac. GTK, Cocoa, Windows API
- [gogpu/ui](https://github.com/gogpu/ui) [![GitHub stars](https://img.shields.io/github/stars/gogpu/ui?style=flat)](https://github.com/gogpu/ui/stargazers) - GPU-accelerated GUI toolkit with 22 widgets, 3 design systems (Material, Fluent, Cupertino), reactive signals, and zero CGO (part of [GoGPU](https://github.com/gogpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu?style=flat)](https://github.com/gogpu/stargazers) ecosystem).
- [goradd/html5tag](https://github.com/goradd/html5tag) [![GitHub stars](https://img.shields.io/github/stars/goradd/html5tag?style=flat)](https://github.com/goradd/html5tag/stargazers) - Library for outputting HTML5 tags.
- [gotk3](https://github.com/gotk3/gotk3) [![GitHub stars](https://img.shields.io/github/stars/gotk3/gotk3?style=flat)](https://github.com/gotk3/gotk3/stargazers) - Go bindings for GTK3.
- [gowd](https://github.com/dtylman/gowd) [![GitHub stars](https://img.shields.io/github/stars/dtylman/gowd?style=flat)](https://github.com/dtylman/gowd/stargazers) - Rapid and simple desktop UI development with GO, HTML, CSS and NW.js. Cross platform.
- [proton](https://github.com/CzaxStudio/proton) [![GitHub stars](https://img.shields.io/github/stars/CzaxStudio/proton?style=flat)](https://github.com/CzaxStudio/proton/stargazers) - Pure Go immediate-mode GUI framework built on Gio with zero Cgo dependencies.
- [qt](https://github.com/therecipe/qt) [![GitHub stars](https://img.shields.io/github/stars/therecipe/qt?style=flat)](https://github.com/therecipe/qt/stargazers) - Qt binding for Go (support for Windows / macOS / Linux / Android / iOS / Sailfish OS / Raspberry Pi).
- [Spot](https://github.com/roblillack/spot) [![GitHub stars](https://img.shields.io/github/stars/roblillack/spot?style=flat)](https://github.com/roblillack/spot/stargazers) - Reactive, cross-platform desktop GUI toolkit.
- [ui](https://github.com/andlabs/ui) [![GitHub stars](https://img.shields.io/github/stars/andlabs/ui?style=flat)](https://github.com/andlabs/ui/stargazers) - Platform-native GUI library for Go. Cross platform.
- [unison](https://github.com/richardwilkes/unison) [![GitHub stars](https://img.shields.io/github/stars/richardwilkes/unison?style=flat)](https://github.com/richardwilkes/unison/stargazers) - A unified graphical user experience toolkit for Go desktop applications. macOS, Windows, and Linux are supported.
- [Wails](https://wails.io) - Mac, Windows, Linux desktop apps with HTML UI using built-in OS HTML renderer.
- [walk](https://github.com/lxn/walk) [![GitHub stars](https://img.shields.io/github/stars/lxn/walk?style=flat)](https://github.com/lxn/walk/stargazers) - Windows application library kit for Go.
- [webview](https://github.com/zserge/webview) [![GitHub stars](https://img.shields.io/github/stars/zserge/webview?style=flat)](https://github.com/zserge/webview/stargazers) - Cross-platform webview window with simple two-way JavaScript bindings (Windows / macOS / Linux).

_Interaction_

- [AppIndicator Go](https://github.com/gopherlibs/appindicator) [![GitHub stars](https://img.shields.io/github/stars/gopherlibs/appindicator?style=flat)](https://github.com/gopherlibs/appindicator/stargazers) - Go bindings for libappindicator3 C library.
- [gogpu/systray](https://github.com/gogpu/systray) [![GitHub stars](https://img.shields.io/github/stars/gogpu/systray?style=flat)](https://github.com/gogpu/systray/stargazers) - Pure Go system tray library for Windows, macOS, and Linux with zero CGO (part of [GoGPU](https://github.com/gogpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu?style=flat)](https://github.com/gogpu/stargazers) ecosystem).
- [gosx-notifier](https://github.com/deckarep/gosx-notifier) [![GitHub stars](https://img.shields.io/github/stars/deckarep/gosx-notifier?style=flat)](https://github.com/deckarep/gosx-notifier/stargazers) - OSX Desktop Notifications library for Go.
- [mac-activity-tracker](https://github.com/prashantgupta24/activity-tracker) [![GitHub stars](https://img.shields.io/github/stars/prashantgupta24/activity-tracker?style=flat)](https://github.com/prashantgupta24/activity-tracker/stargazers) - OSX library to notify about any (pluggable) activity on your machine.
- [mac-sleep-notifier](https://github.com/prashantgupta24/mac-sleep-notifier) [![GitHub stars](https://img.shields.io/github/stars/prashantgupta24/mac-sleep-notifier?style=flat)](https://github.com/prashantgupta24/mac-sleep-notifier/stargazers) - OSX Sleep/Wake notifications in golang.
- [robotgo](https://github.com/go-vgo/robotgo) [![GitHub stars](https://img.shields.io/github/stars/go-vgo/robotgo?style=flat)](https://github.com/go-vgo/robotgo/stargazers) - Go Native cross-platform GUI system automation. Control the mouse, keyboard and other.
- [systray](https://github.com/getlantern/systray) [![GitHub stars](https://img.shields.io/github/stars/getlantern/systray?style=flat)](https://github.com/getlantern/systray/stargazers) - Cross platform Go library to place an icon and menu in the notification area.
- [trayhost](https://github.com/shurcooL/trayhost) [![GitHub stars](https://img.shields.io/github/stars/shurcooL/trayhost?style=flat)](https://github.com/shurcooL/trayhost/stargazers) - Cross-platform Go library to place an icon in the host operating system's taskbar.
- [zenity](https://github.com/ncruces/zenity) [![GitHub stars](https://img.shields.io/github/stars/ncruces/zenity?style=flat)](https://github.com/ncruces/zenity/stargazers) - Cross-platform Go library and CLI to create simple dialogs that interact graphically with the user.

**[⬆ back to top](#contents)**

## Hardware

_Libraries, tools, and tutorials for interacting with hardware._

- [arduino-cli](https://github.com/arduino/arduino-cli) [![GitHub stars](https://img.shields.io/github/stars/arduino/arduino-cli?style=flat)](https://github.com/arduino/arduino-cli/stargazers) - Official Arduino CLI and library. Can run standalone, or be incorporated into larger Go projects.
- [emgo](https://github.com/ziutek/emgo) [![GitHub stars](https://img.shields.io/github/stars/ziutek/emgo?style=flat)](https://github.com/ziutek/emgo/stargazers) - Go-like language for programming embedded systems (e.g. STM32 MCU).
- [ghw](https://github.com/jaypipes/ghw) [![GitHub stars](https://img.shields.io/github/stars/jaypipes/ghw?style=flat)](https://github.com/jaypipes/ghw/stargazers) - Golang hardware discovery/inspection library.
- [go-osc](https://github.com/hypebeast/go-osc) [![GitHub stars](https://img.shields.io/github/stars/hypebeast/go-osc?style=flat)](https://github.com/hypebeast/go-osc/stargazers) - Open Sound Control (OSC) bindings for Go.
- [go-rpio](https://github.com/stianeikeland/go-rpio) [![GitHub stars](https://img.shields.io/github/stars/stianeikeland/go-rpio?style=flat)](https://github.com/stianeikeland/go-rpio/stargazers) - GPIO for Go, doesn't require cgo.
- [goroslib](https://github.com/aler9/goroslib) [![GitHub stars](https://img.shields.io/github/stars/aler9/goroslib?style=flat)](https://github.com/aler9/goroslib/stargazers) - Robot Operating System (ROS) library for Go.
- [joystick](https://github.com/0xcafed00d/joystick) [![GitHub stars](https://img.shields.io/github/stars/0xcafed00d/joystick?style=flat)](https://github.com/0xcafed00d/joystick/stargazers) - a polled API to read the state of an attached joystick.
- [moody](https://github.com/dinakars777/moody) [![GitHub stars](https://img.shields.io/github/stars/dinakars777/moody?style=flat)](https://github.com/dinakars777/moody/stargazers) - Hardware event personality daemon for macOS. Monitors USB, charger, lid, and other hardware events and responds with customizable personalities.
- [sysinfo](https://github.com/zcalusic/sysinfo) [![GitHub stars](https://img.shields.io/github/stars/zcalusic/sysinfo?style=flat)](https://github.com/zcalusic/sysinfo/stargazers) - A pure Go library providing Linux OS / kernel / hardware system information.

**[⬆ back to top](#contents)**

## Images

_Libraries for manipulating images._

- [bild](https://github.com/anthonynsimon/bild) [![GitHub stars](https://img.shields.io/github/stars/anthonynsimon/bild?style=flat)](https://github.com/anthonynsimon/bild/stargazers) - Collection of image processing algorithms in pure Go.
- [bimg](https://github.com/h2non/bimg) [![GitHub stars](https://img.shields.io/github/stars/h2non/bimg?style=flat)](https://github.com/h2non/bimg/stargazers) - Small package for fast and efficient image processing using libvips.
- [cameron](https://github.com/aofei/cameron) [![GitHub stars](https://img.shields.io/github/stars/aofei/cameron?style=flat)](https://github.com/aofei/cameron/stargazers) - An avatar generator for Go.
- [canvas](https://github.com/tdewolff/canvas) [![GitHub stars](https://img.shields.io/github/stars/tdewolff/canvas?style=flat)](https://github.com/tdewolff/canvas/stargazers) - Vector graphics to PDF, SVG or rasterized image.
- [color-extractor](https://github.com/marekm4/color-extractor) [![GitHub stars](https://img.shields.io/github/stars/marekm4/color-extractor?style=flat)](https://github.com/marekm4/color-extractor/stargazers) - Dominant color extractor with no external dependencies.
- [darkroom](https://github.com/gojek/darkroom) [![GitHub stars](https://img.shields.io/github/stars/gojek/darkroom?style=flat)](https://github.com/gojek/darkroom/stargazers) - An image proxy with changeable storage backends and image processing engines with focus on speed and resiliency.
- [geopattern](https://github.com/pravj/geopattern) [![GitHub stars](https://img.shields.io/github/stars/pravj/geopattern?style=flat)](https://github.com/pravj/geopattern/stargazers) - Create beautiful generative image patterns from a string.
- [gg](https://github.com/fogleman/gg) [![GitHub stars](https://img.shields.io/github/stars/fogleman/gg?style=flat)](https://github.com/fogleman/gg/stargazers) - 2D rendering in pure Go.
- [gift](https://github.com/disintegration/gift) [![GitHub stars](https://img.shields.io/github/stars/disintegration/gift?style=flat)](https://github.com/disintegration/gift/stargazers) - Package of image processing filters.
- [gltf](https://github.com/qmuntal/gltf) [![GitHub stars](https://img.shields.io/github/stars/qmuntal/gltf?style=flat)](https://github.com/qmuntal/gltf/stargazers) - Efficient and robust glTF 2.0 reader, writer and validator.
- [go-cairo](https://github.com/ungerik/go-cairo) [![GitHub stars](https://img.shields.io/github/stars/ungerik/go-cairo?style=flat)](https://github.com/ungerik/go-cairo/stargazers) - Go binding for the cairo graphics library.
- [go-gd](https://github.com/bolknote/go-gd) [![GitHub stars](https://img.shields.io/github/stars/bolknote/go-gd?style=flat)](https://github.com/bolknote/go-gd/stargazers) - Go binding for GD library.
- [go-nude](https://github.com/koyachi/go-nude) [![GitHub stars](https://img.shields.io/github/stars/koyachi/go-nude?style=flat)](https://github.com/koyachi/go-nude/stargazers) - Nudity detection with Go.
- [go-qrcode](https://github.com/yeqown/go-qrcode) [![GitHub stars](https://img.shields.io/github/stars/yeqown/go-qrcode?style=flat)](https://github.com/yeqown/go-qrcode/stargazers) - Generate QR codes with personalized styles, allowing adjustments to color, block size, shape, and icons.
- [go-webcolors](https://github.com/jyotiska/go-webcolors) [![GitHub stars](https://img.shields.io/github/stars/jyotiska/go-webcolors?style=flat)](https://github.com/jyotiska/go-webcolors/stargazers) - Port of webcolors library from Python to Go.
- [go-webp](https://github.com/kolesa-team/go-webp) [![GitHub stars](https://img.shields.io/github/stars/kolesa-team/go-webp?style=flat)](https://github.com/kolesa-team/go-webp/stargazers) - Library for encode and decode webp pictures, using libwebp.
- [gocv](https://github.com/hybridgroup/gocv) [![GitHub stars](https://img.shields.io/github/stars/hybridgroup/gocv?style=flat)](https://github.com/hybridgroup/gocv/stargazers) - Go package for computer vision using OpenCV 3.3+.
- [gogpu/gg](https://github.com/gogpu/gg) [![GitHub stars](https://img.shields.io/github/stars/gogpu/gg?style=flat)](https://github.com/gogpu/gg/stargazers) - GPU-accelerated 2D rendering with Canvas-like API, zero CGO (part of [GoGPU](https://github.com/gogpu) [![GitHub stars](https://img.shields.io/github/stars/gogpu?style=flat)](https://github.com/gogpu/stargazers) pure Go graphics ecosystem).
- [goimagehash](https://github.com/corona10/goimagehash) [![GitHub stars](https://img.shields.io/github/stars/corona10/goimagehash?style=flat)](https://github.com/corona10/goimagehash/stargazers) - Go Perceptual image hashing package.
- [goimghdr](https://github.com/corona10/goimghdr) [![GitHub stars](https://img.shields.io/github/stars/corona10/goimghdr?style=flat)](https://github.com/corona10/goimghdr/stargazers) - The imghdr module determines the type of image contained in a file for Go.
- [govatar](https://github.com/o1egl/govatar) [![GitHub stars](https://img.shields.io/github/stars/o1egl/govatar?style=flat)](https://github.com/o1egl/govatar/stargazers) - Library and CMD tool for generating funny avatars.
- [govips](https://github.com/davidbyttow/govips) [![GitHub stars](https://img.shields.io/github/stars/davidbyttow/govips?style=flat)](https://github.com/davidbyttow/govips/stargazers) - A lightning fast image processing and resizing library for Go.
- [gowitness](https://github.com/sensepost/gowitness) [![GitHub stars](https://img.shields.io/github/stars/sensepost/gowitness?style=flat)](https://github.com/sensepost/gowitness/stargazers) - Screenshoting webpages using go and headless chrome on command line.
- [gridder](https://github.com/shomali11/gridder) [![GitHub stars](https://img.shields.io/github/stars/shomali11/gridder?style=flat)](https://github.com/shomali11/gridder/stargazers) - A Grid based 2D Graphics library.
- [image2ascii](https://github.com/qeesung/image2ascii) [![GitHub stars](https://img.shields.io/github/stars/qeesung/image2ascii?style=flat)](https://github.com/qeesung/image2ascii/stargazers) - Convert image to ASCII.
- [imagick](https://github.com/gographics/imagick) [![GitHub stars](https://img.shields.io/github/stars/gographics/imagick?style=flat)](https://github.com/gographics/imagick/stargazers) - Go binding to ImageMagick's MagickWand C API.
- [imaginary](https://github.com/h2non/imaginary) [![GitHub stars](https://img.shields.io/github/stars/h2non/imaginary?style=flat)](https://github.com/h2non/imaginary/stargazers) - Fast and simple HTTP microservice for image resizing.
- [imaging](https://github.com/disintegration/imaging) [![GitHub stars](https://img.shields.io/github/stars/disintegration/imaging?style=flat)](https://github.com/disintegration/imaging/stargazers) - Simple Go image processing package.
- [imagor](https://github.com/cshum/imagor) [![GitHub stars](https://img.shields.io/github/stars/cshum/imagor?style=flat)](https://github.com/cshum/imagor/stargazers) - Fast, secure image processing server and Go library, using libvips.
- [img](https://github.com/hawx/img) [![GitHub stars](https://img.shields.io/github/stars/hawx/img?style=flat)](https://github.com/hawx/img/stargazers) - Selection of image manipulation tools.
- [ln](https://github.com/fogleman/ln) [![GitHub stars](https://img.shields.io/github/stars/fogleman/ln?style=flat)](https://github.com/fogleman/ln/stargazers) - 3D line art rendering in Go.
- [mergi](https://github.com/noelyahan/mergi) [![GitHub stars](https://img.shields.io/github/stars/noelyahan/mergi?style=flat)](https://github.com/noelyahan/mergi/stargazers) - Tool & Go library for image manipulation (Merge, Crop, Resize, Watermark, Animate).
- [mort](https://github.com/aldor007/mort) [![GitHub stars](https://img.shields.io/github/stars/aldor007/mort?style=flat)](https://github.com/aldor007/mort/stargazers) - Storage and image processing server written in Go.
- [mpo](https://github.com/donatj/mpo) [![GitHub stars](https://img.shields.io/github/stars/donatj/mpo?style=flat)](https://github.com/donatj/mpo/stargazers) - Decoder and conversion tool for MPO 3D Photos.
- [nativewebp](https://github.com/HugoSmits86/nativewebp) [![GitHub stars](https://img.shields.io/github/stars/HugoSmits86/nativewebp?style=flat)](https://github.com/HugoSmits86/nativewebp/stargazers) - Go native WebP encoder with zero external dependencies.
- [picfit](https://github.com/thoas/picfit) [![GitHub stars](https://img.shields.io/github/stars/thoas/picfit?style=flat)](https://github.com/thoas/picfit/stargazers) - An image resizing server written in Go.
- [pt](https://github.com/fogleman/pt) [![GitHub stars](https://img.shields.io/github/stars/fogleman/pt?style=flat)](https://github.com/fogleman/pt/stargazers) - Path tracing engine written in Go.
- [scout](https://github.com/jonoton/scout) [![GitHub stars](https://img.shields.io/github/stars/jonoton/scout?style=flat)](https://github.com/jonoton/scout/stargazers) - Scout is a standalone open source software solution for DIY video security.
- [smartcrop](https://github.com/muesli/smartcrop) [![GitHub stars](https://img.shields.io/github/stars/muesli/smartcrop?style=flat)](https://github.com/muesli/smartcrop/stargazers) - Finds good crops for arbitrary images and crop sizes.
- [steganography](https://github.com/auyer/steganography) [![GitHub stars](https://img.shields.io/github/stars/auyer/steganography?style=flat)](https://github.com/auyer/steganography/stargazers) - Pure Go Library for LSB steganography.
- [stegify](https://github.com/DimitarPetrov/stegify) [![GitHub stars](https://img.shields.io/github/stars/DimitarPetrov/stegify?style=flat)](https://github.com/DimitarPetrov/stegify/stargazers) - Go tool for LSB steganography, capable of hiding any file within an image.
- [svgo](https://github.com/ajstarks/svgo) [![GitHub stars](https://img.shields.io/github/stars/ajstarks/svgo?style=flat)](https://github.com/ajstarks/svgo/stargazers) - Go Language Library for SVG generation.
- [transformimgs](https://github.com/Pixboost/transformimgs) [![GitHub stars](https://img.shields.io/github/stars/Pixboost/transformimgs?style=flat)](https://github.com/Pixboost/transformimgs/stargazers) - Transformimgs resizes and optimises images for Web using next-generation formats.
- [webp-server](https://github.com/mehdipourfar/webp-server) [![GitHub stars](https://img.shields.io/github/stars/mehdipourfar/webp-server?style=flat)](https://github.com/mehdipourfar/webp-server/stargazers) - Simple and minimal image server capable of storing, resizing, converting and caching images.

**[⬆ back to top](#contents)**

## IoT (Internet of Things)

_Libraries for programming devices of the IoT._

- [connectordb](https://github.com/connectordb/connectordb) [![GitHub stars](https://img.shields.io/github/stars/connectordb/connectordb?style=flat)](https://github.com/connectordb/connectordb/stargazers) - Open-Source Platform for Quantified Self & IoT.
- [devices](https://github.com/goiot/devices) [![GitHub stars](https://img.shields.io/github/stars/goiot/devices?style=flat)](https://github.com/goiot/devices/stargazers) - Suite of libraries for IoT devices, experimental for x/exp/io.
- [ekuiper](https://github.com/lf-edge/ekuiper) [![GitHub stars](https://img.shields.io/github/stars/lf-edge/ekuiper?style=flat)](https://github.com/lf-edge/ekuiper/stargazers) - Lightweight data stream processing engine for IoT edge.
- [eywa](https://github.com/xcodersun/eywa) [![GitHub stars](https://img.shields.io/github/stars/xcodersun/eywa?style=flat)](https://github.com/xcodersun/eywa/stargazers) - Project Eywa is essentially a connection manager that keeps track of connected devices.
- [flogo](https://github.com/tibcosoftware/flogo) [![GitHub stars](https://img.shields.io/github/stars/tibcosoftware/flogo?style=flat)](https://github.com/tibcosoftware/flogo/stargazers) - Project Flogo is an Open Source Framework for IoT Edge Apps & Integration.
- [gatt](https://github.com/paypal/gatt) [![GitHub stars](https://img.shields.io/github/stars/paypal/gatt?style=flat)](https://github.com/paypal/gatt/stargazers) - Gatt is a Go package for building Bluetooth Low Energy peripherals.
- [gobot](https://github.com/hybridgroup/gobot/) [![GitHub stars](https://img.shields.io/github/stars/hybridgroup/gobot/?style=flat)](https://github.com/hybridgroup/gobot//stargazers) - Gobot is a framework for robotics, physical computing, and the Internet of Things.
- [huego](https://github.com/amimof/huego) [![GitHub stars](https://img.shields.io/github/stars/amimof/huego?style=flat)](https://github.com/amimof/huego/stargazers) - An extensive Philips Hue client library for Go.
- [iot](https://github.com/vaelen/iot/) [![GitHub stars](https://img.shields.io/github/stars/vaelen/iot/?style=flat)](https://github.com/vaelen/iot//stargazers) - IoT is a simple framework for implementing a Google IoT Core device.
- [periph](https://periph.io/) - Peripherals I/O to interface with low-level board facilities.
- [rulego](https://github.com/rulego/rulego) [![GitHub stars](https://img.shields.io/github/stars/rulego/rulego?style=flat)](https://github.com/rulego/rulego/stargazers) - RuleGo is a lightweight, high-performance, embedded, orchestrable component-based rule engine for IoT edge.
- [sensorbee](https://github.com/sensorbee/sensorbee) [![GitHub stars](https://img.shields.io/github/stars/sensorbee/sensorbee?style=flat)](https://github.com/sensorbee/sensorbee/stargazers) - Lightweight stream processing engine for IoT.
- [shifu](https://github.com/Edgenesis/shifu) [![GitHub stars](https://img.shields.io/github/stars/Edgenesis/shifu?style=flat)](https://github.com/Edgenesis/shifu/stargazers) - Kubernetes native IoT development framework.
- [smart-home](https://github.com/e154/smart-home) [![GitHub stars](https://img.shields.io/github/stars/e154/smart-home?style=flat)](https://github.com/e154/smart-home/stargazers) - Software package for IoT automation.

**[⬆ back to top](#contents)**

## Job Scheduler

_Libraries for scheduling jobs._

- [cdule](https://github.com/deepaksinghvi/cdule) [![GitHub stars](https://img.shields.io/github/stars/deepaksinghvi/cdule?style=flat)](https://github.com/deepaksinghvi/cdule/stargazers) - Job scheduler library with database support
- [cheek](https://github.com/bart6114/cheek) [![GitHub stars](https://img.shields.io/github/stars/bart6114/cheek?style=flat)](https://github.com/bart6114/cheek/stargazers) - A simple crontab like scheduler that aims to offer a KISS approach to job scheduling.
- [clockwerk](https://github.com/onatm/clockwerk) [![GitHub stars](https://img.shields.io/github/stars/onatm/clockwerk?style=flat)](https://github.com/onatm/clockwerk/stargazers) - Go package to schedule periodic jobs using a simple, fluent syntax.
- [cronticker](https://github.com/krayzpipes/cronticker) [![GitHub stars](https://img.shields.io/github/stars/krayzpipes/cronticker?style=flat)](https://github.com/krayzpipes/cronticker/stargazers) - A ticker implementation to support cron schedules.
- [go-cron](https://github.com/rk/go-cron) [![GitHub stars](https://img.shields.io/github/stars/rk/go-cron?style=flat)](https://github.com/rk/go-cron/stargazers) - Simple Cron library for go that can execute closures or functions at varying intervals, from once a second to once a year on a specific date and time. Primarily for web applications and long running daemons.
- [go-cron](https://github.com/netresearch/go-cron) [![GitHub stars](https://img.shields.io/github/stars/netresearch/go-cron?style=flat)](https://github.com/netresearch/go-cron/stargazers) - Cron job scheduler with runtime schedule updates, per-entry context, resilience middleware (retry, circuit breaker, rate limiting), and observability hooks; successor to robfig/cron.
- [go-job](https://github.com/cybergarage/go-job) [![GitHub stars](https://img.shields.io/github/stars/cybergarage/go-job?style=flat)](https://github.com/cybergarage/go-job/stargazers) - A flexible and extensible job scheduling and execution library for Go.
- [go-quartz](https://github.com/reugn/go-quartz) [![GitHub stars](https://img.shields.io/github/stars/reugn/go-quartz?style=flat)](https://github.com/reugn/go-quartz/stargazers) - Simple, zero-dependency scheduling library for Go.
- [go-scheduler](https://github.com/pardnchiu/go-scheduler) [![GitHub stars](https://img.shields.io/github/stars/pardnchiu/go-scheduler?style=flat)](https://github.com/pardnchiu/go-scheduler/stargazers) - Job scheduler supporting standard cron expressions, custom descriptors, intervals, and task dependencies.
- [gocron](https://github.com/go-co-op/gocron) [![GitHub stars](https://img.shields.io/github/stars/go-co-op/gocron?style=flat)](https://github.com/go-co-op/gocron/stargazers) - Easy and fluent Go job scheduling. This is an actively maintained fork of [jasonlvhit/gocron](https://github.com/jasonlvhit/gocron) [![GitHub stars](https://img.shields.io/github/stars/jasonlvhit/gocron?style=flat)](https://github.com/jasonlvhit/gocron/stargazers).
- [goflow](https://github.com/fieldryand/goflow) [![GitHub stars](https://img.shields.io/github/stars/fieldryand/goflow?style=flat)](https://github.com/fieldryand/goflow/stargazers) - A simple but powerful DAG scheduler and dashboard.
- [gron](https://github.com/roylee0704/gron) [![GitHub stars](https://img.shields.io/github/stars/roylee0704/gron?style=flat)](https://github.com/roylee0704/gron/stargazers) - Define time-based tasks using a simple Go API and Gron’s scheduler will run them accordingly.
- [gronx](https://github.com/adhocore/gronx) [![GitHub stars](https://img.shields.io/github/stars/adhocore/gronx?style=flat)](https://github.com/adhocore/gronx/stargazers) - Cron expression parser, task runner and daemon consuming crontab like task list.
- [JobRunner](https://github.com/bamzi/jobrunner) [![GitHub stars](https://img.shields.io/github/stars/bamzi/jobrunner?style=flat)](https://github.com/bamzi/jobrunner/stargazers) - Smart and featureful cron job scheduler with job queuing and live monitoring built in.
- [leprechaun](https://github.com/kilgaloon/leprechaun) [![GitHub stars](https://img.shields.io/github/stars/kilgaloon/leprechaun?style=flat)](https://github.com/kilgaloon/leprechaun/stargazers) - Job scheduler that supports webhooks, crons and classic scheduling.
- [ofelia](https://github.com/netresearch/ofelia) [![GitHub stars](https://img.shields.io/github/stars/netresearch/ofelia?style=flat)](https://github.com/netresearch/ofelia/stargazers) - Docker job scheduler (crontab for Docker); fork of mcuadros/ofelia that adds a web UI, job dependencies, retries, and job persistence.
- [pending](https://github.com/kahoon/pending) [![GitHub stars](https://img.shields.io/github/stars/kahoon/pending?style=flat)](https://github.com/kahoon/pending/stargazers) - ID-based debounced task scheduler for deferred tasks with cancellation, graceful shutdown, and optional concurrency limits.
- [sched](https://github.com/romshark/sched) [![GitHub stars](https://img.shields.io/github/stars/romshark/sched?style=flat)](https://github.com/romshark/sched/stargazers) - A job scheduler with the ability to fast-forward time.
- [scheduler](https://github.com/carlescere/scheduler) [![GitHub stars](https://img.shields.io/github/stars/carlescere/scheduler?style=flat)](https://github.com/carlescere/scheduler/stargazers) - Cronjobs scheduling made easy.
- [scheduler](https://github.com/yuseferi/scheduler) [![GitHub stars](https://img.shields.io/github/stars/yuseferi/scheduler?style=flat)](https://github.com/yuseferi/scheduler/stargazers) - Go-native distributed job scheduler with delayed tasks, batched Redis coordination, retries, lease-based recovery, and versioned queue partitioning.
- [tasks](https://github.com/madflojo/tasks) [![GitHub stars](https://img.shields.io/github/stars/madflojo/tasks?style=flat)](https://github.com/madflojo/tasks/stargazers) - An easy to use in-process scheduler for recurring tasks in Go.
- [tickstem/cron](https://github.com/tickstem/cron) [![GitHub stars](https://img.shields.io/github/stars/tickstem/cron?style=flat)](https://github.com/tickstem/cron/stargazers) - Go client for scheduling HTTP cron jobs, with execution history, failure alerts, and tsk-local for testing handlers without live credentials.
- [tickstem/heartbeat](https://github.com/tickstem/heartbeat) [![GitHub stars](https://img.shields.io/github/stars/tickstem/heartbeat?style=flat)](https://github.com/tickstem/heartbeat/stargazers) - Go client for dead-man's switch heartbeat monitoring: ping a URL after each job run and get alerted by email if pings stop arriving.

**[⬆ back to top](#contents)**

## JSON

_Libraries for working with JSON._

- [ajson](https://github.com/spyzhov/ajson) [![GitHub stars](https://img.shields.io/github/stars/spyzhov/ajson?style=flat)](https://github.com/spyzhov/ajson/stargazers) - Abstract JSON for golang with JSONPath support.
- [ask](https://github.com/simonnilsson/ask) [![GitHub stars](https://img.shields.io/github/stars/simonnilsson/ask?style=flat)](https://github.com/simonnilsson/ask/stargazers) - Easy access to nested values in maps and slices. Works in combination with encoding/json and other packages that "Unmarshal" arbitrary data into Go data-types.
- [dynjson](https://github.com/cocoonspace/dynjson) [![GitHub stars](https://img.shields.io/github/stars/cocoonspace/dynjson?style=flat)](https://github.com/cocoonspace/dynjson/stargazers) - Client-customizable JSON formats for dynamic APIs.
- [ej](https://github.com/lucassscaravelli/ej) [![GitHub stars](https://img.shields.io/github/stars/lucassscaravelli/ej?style=flat)](https://github.com/lucassscaravelli/ej/stargazers) - Write and read JSON from different sources succinctly.
- [epoch](https://github.com/vtopc/epoch) [![GitHub stars](https://img.shields.io/github/stars/vtopc/epoch?style=flat)](https://github.com/vtopc/epoch/stargazers) - Contains primitives for marshaling/unmarshalling Unix timestamp/epoch to/from build-in time.Time type in JSON.
- [fastjson](https://github.com/valyala/fastjson) [![GitHub stars](https://img.shields.io/github/stars/valyala/fastjson?style=flat)](https://github.com/valyala/fastjson/stargazers) - Fast JSON parser and validator for Go. No custom structs, no code generation, no reflection.
- [gabs](https://github.com/Jeffail/gabs) [![GitHub stars](https://img.shields.io/github/stars/Jeffail/gabs?style=flat)](https://github.com/Jeffail/gabs/stargazers) - For parsing, creating and editing unknown or dynamic JSON in Go.
- [gjo](https://github.com/skanehira/gjo) [![GitHub stars](https://img.shields.io/github/stars/skanehira/gjo?style=flat)](https://github.com/skanehira/gjo/stargazers) - Small utility to create JSON objects.
- [GJSON](https://github.com/tidwall/gjson) [![GitHub stars](https://img.shields.io/github/stars/tidwall/gjson?style=flat)](https://github.com/tidwall/gjson/stargazers) - Get a JSON value with one line of code.
- [go-jsonerror](https://github.com/ddymko/go-jsonerror) [![GitHub stars](https://img.shields.io/github/stars/ddymko/go-jsonerror?style=flat)](https://github.com/ddymko/go-jsonerror/stargazers) - Go-JsonError is meant to allow us to easily create json response errors that follow the JsonApi spec.
- [go-respond](https://github.com/nicklaw5/go-respond) [![GitHub stars](https://img.shields.io/github/stars/nicklaw5/go-respond?style=flat)](https://github.com/nicklaw5/go-respond/stargazers) - Go package for handling common HTTP JSON responses.
- [gojmapr](https://github.com/limiu82214/gojmapr) [![GitHub stars](https://img.shields.io/github/stars/limiu82214/gojmapr?style=flat)](https://github.com/limiu82214/gojmapr/stargazers) - Get simple struct from complex json by json path.
- [gojq](https://github.com/elgs/gojq) [![GitHub stars](https://img.shields.io/github/stars/elgs/gojq?style=flat)](https://github.com/elgs/gojq/stargazers) - JSON query in Golang.
- [gojson](https://github.com/ChimeraCoder/gojson) [![GitHub stars](https://img.shields.io/github/stars/ChimeraCoder/gojson?style=flat)](https://github.com/ChimeraCoder/gojson/stargazers) - Automatically generate Go (golang) struct definitions from example JSON.
- [htmljson](https://github.com/nikolaydubina/htmljson) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/htmljson?style=flat)](https://github.com/nikolaydubina/htmljson/stargazers) - Rich rendering of JSON as HTML in Go.
- [JayDiff](https://github.com/yazgazan/jaydiff) [![GitHub stars](https://img.shields.io/github/stars/yazgazan/jaydiff?style=flat)](https://github.com/yazgazan/jaydiff/stargazers) - JSON diff utility written in Go.
- [jettison](https://github.com/wI2L/jettison) [![GitHub stars](https://img.shields.io/github/stars/wI2L/jettison?style=flat)](https://github.com/wI2L/jettison/stargazers) - Fast and flexible JSON encoder for Go.
- [jscan](https://github.com/romshark/jscan) [![GitHub stars](https://img.shields.io/github/stars/romshark/jscan?style=flat)](https://github.com/romshark/jscan/stargazers) - High performance zero-allocation JSON iterator.
- [JSON-to-Go](https://mholt.github.io/json-to-go/) - Convert JSON to Go struct.
- [JSON-to-Proto](https://json-to-proto.github.io/) - Convert JSON to Protobuf online.
- [json2go](https://github.com/m-zajac/json2go) [![GitHub stars](https://img.shields.io/github/stars/m-zajac/json2go?style=flat)](https://github.com/m-zajac/json2go/stargazers) - Advanced JSON to Go struct conversion. Provides package that can parse multiple JSON documents and create struct to fit them all.
- [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) [![GitHub stars](https://img.shields.io/github/stars/AmuzaTkts/jsonapi-errors?style=flat)](https://github.com/AmuzaTkts/jsonapi-errors/stargazers) - Go bindings based on the JSON API errors reference.
- [jsoncolor](https://github.com/neilotoole/jsoncolor) [![GitHub stars](https://img.shields.io/github/stars/neilotoole/jsoncolor?style=flat)](https://github.com/neilotoole/jsoncolor/stargazers) - Drop-in replacement for `encoding/json` that outputs colorized JSON.
- [jsondiff](https://github.com/wI2L/jsondiff) [![GitHub stars](https://img.shields.io/github/stars/wI2L/jsondiff?style=flat)](https://github.com/wI2L/jsondiff/stargazers) - JSON diff library for Go based on RFC6902 (JSON Patch).
- [jsonf](https://github.com/miolini/jsonf) [![GitHub stars](https://img.shields.io/github/stars/miolini/jsonf?style=flat)](https://github.com/miolini/jsonf/stargazers) - Console tool for highlighted formatting and struct query fetching JSON.
- [jsongo](https://github.com/ricardolonga/jsongo) [![GitHub stars](https://img.shields.io/github/stars/ricardolonga/jsongo?style=flat)](https://github.com/ricardolonga/jsongo/stargazers) - Fluent API to make it easier to create Json objects.
- [jsonhal](https://github.com/RichardKnop/jsonhal) [![GitHub stars](https://img.shields.io/github/stars/RichardKnop/jsonhal?style=flat)](https://github.com/RichardKnop/jsonhal/stargazers) - Simple Go package to make custom structs marshal into HAL compatible JSON responses.
- [jsonhandlers](https://github.com/abusomani/jsonhandlers) [![GitHub stars](https://img.shields.io/github/stars/abusomani/jsonhandlers?style=flat)](https://github.com/abusomani/jsonhandlers/stargazers) - JSON library to expose simple handlers that lets you easily read and write json from various sources.
- [jsonic](https://github.com/sinhashubham95/jsonic) [![GitHub stars](https://img.shields.io/github/stars/sinhashubham95/jsonic?style=flat)](https://github.com/sinhashubham95/jsonic/stargazers) - Utilities to handle and query JSON without defining structs in a type safe manner.
- [jsonvalue](https://github.com/Andrew-M-C/go.jsonvalue) [![GitHub stars](https://img.shields.io/github/stars/Andrew-M-C/go.jsonvalue?style=flat)](https://github.com/Andrew-M-C/go.jsonvalue/stargazers) - A fast and convenient library for unstructured JSON data, replacing `encoding/json`.
- [jzon](https://github.com/zerosnake0/jzon) [![GitHub stars](https://img.shields.io/github/stars/zerosnake0/jzon?style=flat)](https://github.com/zerosnake0/jzon/stargazers) - JSON library with standard compatible API/behavior.
- [kazaam](https://github.com/Qntfy/kazaam) [![GitHub stars](https://img.shields.io/github/stars/Qntfy/kazaam?style=flat)](https://github.com/Qntfy/kazaam/stargazers) - API for arbitrary transformation of JSON documents.
- [mapslice-json](https://github.com/mickep76/mapslice-json) [![GitHub stars](https://img.shields.io/github/stars/mickep76/mapslice-json?style=flat)](https://github.com/mickep76/mapslice-json/stargazers) - Go MapSlice for ordered marshal/ unmarshal of maps in JSON.
- [marshmallow](https://github.com/PerimeterX/marshmallow) [![GitHub stars](https://img.shields.io/github/stars/PerimeterX/marshmallow?style=flat)](https://github.com/PerimeterX/marshmallow/stargazers) - Performant JSON unmarshalling for flexible use cases.
- [mp](https://github.com/sanbornm/mp) [![GitHub stars](https://img.shields.io/github/stars/sanbornm/mp?style=flat)](https://github.com/sanbornm/mp/stargazers) - Simple cli email parser. It currently takes stdin and outputs JSON.
- [OjG](https://github.com/ohler55/ojg) [![GitHub stars](https://img.shields.io/github/stars/ohler55/ojg?style=flat)](https://github.com/ohler55/ojg/stargazers) - Optimized JSON for Go is a high performance parser with a variety of additional JSON tools including JSONPath.
- [omg.jsonparser](https://github.com/dedalqq/omg.jsonparser) [![GitHub stars](https://img.shields.io/github/stars/dedalqq/omg.jsonparser?style=flat)](https://github.com/dedalqq/omg.jsonparser/stargazers) - Simple JSON parser with validation by condition via golang struct fields tags.
- [SJSON](https://github.com/tidwall/sjson) [![GitHub stars](https://img.shields.io/github/stars/tidwall/sjson?style=flat)](https://github.com/tidwall/sjson/stargazers) - Set a JSON value with one line of code.  
- [ujson](https://github.com/olvrng/ujson) [![GitHub stars](https://img.shields.io/github/stars/olvrng/ujson?style=flat)](https://github.com/olvrng/ujson/stargazers) - Fast and minimal JSON parser and transformer that works on unstructured JSON.
- [vjson](https://github.com/miladibra10/vjson) [![GitHub stars](https://img.shields.io/github/stars/miladibra10/vjson?style=flat)](https://github.com/miladibra10/vjson/stargazers) - Go package for validating JSON objects with declaring a JSON schema with fluent API.

**[⬆ back to top](#contents)**

## Logging

_Libraries for generating and working with log files._

- [caarlos0/log](https://github.com/caarlos0/log) [![GitHub stars](https://img.shields.io/github/stars/caarlos0/log?style=flat)](https://github.com/caarlos0/log/stargazers) - Colorful CLI logger.
- [distillog](https://github.com/amoghe/distillog) [![GitHub stars](https://img.shields.io/github/stars/amoghe/distillog?style=flat)](https://github.com/amoghe/distillog/stargazers) - distilled levelled logging (think of it as stdlib + log levels).
- [glg](https://github.com/kpango/glg) [![GitHub stars](https://img.shields.io/github/stars/kpango/glg?style=flat)](https://github.com/kpango/glg/stargazers) - glg is simple and fast leveled logging library for Go.
- [glo](https://github.com/lajosbencz/glo) [![GitHub stars](https://img.shields.io/github/stars/lajosbencz/glo?style=flat)](https://github.com/lajosbencz/glo/stargazers) - PHP Monolog inspired logging facility with identical severity levels.
- [glog](https://github.com/golang/glog) [![GitHub stars](https://img.shields.io/github/stars/golang/glog?style=flat)](https://github.com/golang/glog/stargazers) - Leveled execution logs for Go.
- [go-cronowriter](https://github.com/utahta/go-cronowriter) [![GitHub stars](https://img.shields.io/github/stars/utahta/go-cronowriter?style=flat)](https://github.com/utahta/go-cronowriter/stargazers) - Simple writer that rotate log files automatically based on current date and time, like cronolog.
- [go-log](https://github.com/pieterclaerhout/go-log) [![GitHub stars](https://img.shields.io/github/stars/pieterclaerhout/go-log?style=flat)](https://github.com/pieterclaerhout/go-log/stargazers) - A logging library with stack traces, object dumping and optional timestamps.
- [go-log](https://github.com/subchen/go-log) [![GitHub stars](https://img.shields.io/github/stars/subchen/go-log?style=flat)](https://github.com/subchen/go-log/stargazers) - Simple and configurable Logging in Go, with level, formatters and writers.
- [go-log](https://github.com/siddontang/go-log) [![GitHub stars](https://img.shields.io/github/stars/siddontang/go-log?style=flat)](https://github.com/siddontang/go-log/stargazers) - Log lib supports level and multi handlers.
- [go-log](https://github.com/ian-kent/go-log) [![GitHub stars](https://img.shields.io/github/stars/ian-kent/go-log?style=flat)](https://github.com/ian-kent/go-log/stargazers) - Log4j implementation in Go.
- [go-logger](https://github.com/apsdehal/go-logger) [![GitHub stars](https://img.shields.io/github/stars/apsdehal/go-logger?style=flat)](https://github.com/apsdehal/go-logger/stargazers) - Simple logger of Go Programs, with level handlers.
- [GoLogX](https://github.com/AyoubTadlaoui/GoLogX) [![GitHub stars](https://img.shields.io/github/stars/AyoubTadlaoui/GoLogX?style=flat)](https://github.com/AyoubTadlaoui/GoLogX/stargazers) - Append-only, hash-chained, optionally Ed25519-signed slog handler with offline verification of tampering.
- [gone/log](https://github.com/One-com/gone/tree/master/log) [![GitHub stars](https://img.shields.io/github/stars/One-com/gone/tree/master/log?style=flat)](https://github.com/One-com/gone/tree/master/log/stargazers) - Fast, extendable, full-featured, std-lib source compatible log library.
- [httpretty](https://github.com/henvic/httpretty) [![GitHub stars](https://img.shields.io/github/stars/henvic/httpretty?style=flat)](https://github.com/henvic/httpretty/stargazers) - Pretty-prints your regular HTTP requests on your terminal for debugging (similar to http.DumpRequest).
- [journald](https://github.com/ssgreg/journald) [![GitHub stars](https://img.shields.io/github/stars/ssgreg/journald?style=flat)](https://github.com/ssgreg/journald/stargazers) - Go implementation of systemd Journal's native API for logging.
- [kemba](https://github.com/clok/kemba) [![GitHub stars](https://img.shields.io/github/stars/clok/kemba?style=flat)](https://github.com/clok/kemba/stargazers) - A tiny debug logging tool inspired by [debug](https://github.com/visionmedia/debug) [![GitHub stars](https://img.shields.io/github/stars/visionmedia/debug?style=flat)](https://github.com/visionmedia/debug/stargazers), great for CLI tools and applications.
- [lazyjournal](https://github.com/Lifailon/lazyjournal) [![GitHub stars](https://img.shields.io/github/stars/Lifailon/lazyjournal?style=flat)](https://github.com/Lifailon/lazyjournal/stargazers) - A TUI for reading and filtering logs from journalctl, file system, Docker and Podman containers, as well Kubernetes pods.
- [log](https://github.com/aerogo/log) [![GitHub stars](https://img.shields.io/github/stars/aerogo/log?style=flat)](https://github.com/aerogo/log/stargazers) - An O(1) logging system that allows you to connect one log to multiple writers (e.g. stdout, a file and a TCP connection).
- [log](https://github.com/apex/log) [![GitHub stars](https://img.shields.io/github/stars/apex/log?style=flat)](https://github.com/apex/log/stargazers) - Structured logging package for Go.
- [log](https://github.com/go-playground/log) [![GitHub stars](https://img.shields.io/github/stars/go-playground/log?style=flat)](https://github.com/go-playground/log/stargazers) - Simple, configurable and scalable Structured Logging for Go.
- [log](https://github.com/teris-io/log) [![GitHub stars](https://img.shields.io/github/stars/teris-io/log?style=flat)](https://github.com/teris-io/log/stargazers) - Structured log interface for Go cleanly separates logging facade from its implementation.
- [log](https://github.com/heartwilltell/log) [![GitHub stars](https://img.shields.io/github/stars/heartwilltell/log?style=flat)](https://github.com/heartwilltell/log/stargazers) - Simple leveled logging wrapper around standard log package.
- [log](https://github.com/no-src/log) [![GitHub stars](https://img.shields.io/github/stars/no-src/log?style=flat)](https://github.com/no-src/log/stargazers) - A simple logging framework out of the box.
- [log15](https://github.com/inconshreveable/log15) [![GitHub stars](https://img.shields.io/github/stars/inconshreveable/log15?style=flat)](https://github.com/inconshreveable/log15/stargazers) - Simple, powerful logging for Go.
- [logdump](https://github.com/ewwwwwqm/logdump) [![GitHub stars](https://img.shields.io/github/stars/ewwwwwqm/logdump?style=flat)](https://github.com/ewwwwwqm/logdump/stargazers) - Package for multi-level logging.
- [logex](https://github.com/chzyer/logex) [![GitHub stars](https://img.shields.io/github/stars/chzyer/logex?style=flat)](https://github.com/chzyer/logex/stargazers) - Golang log lib, supports tracking and level, wrap by standard log lib.
- [logger](https://github.com/azer/logger) [![GitHub stars](https://img.shields.io/github/stars/azer/logger?style=flat)](https://github.com/azer/logger/stargazers) - Minimalistic logging library for Go.
- [logo](https://github.com/mbndr/logo) [![GitHub stars](https://img.shields.io/github/stars/mbndr/logo?style=flat)](https://github.com/mbndr/logo/stargazers) - Golang logger to different configurable writers.
- [logrus](https://github.com/Sirupsen/logrus) [![GitHub stars](https://img.shields.io/github/stars/Sirupsen/logrus?style=flat)](https://github.com/Sirupsen/logrus/stargazers) - Structured logger for Go.
- [logrusiowriter](https://github.com/cabify/logrusiowriter) [![GitHub stars](https://img.shields.io/github/stars/cabify/logrusiowriter?style=flat)](https://github.com/cabify/logrusiowriter/stargazers) - `io.Writer` implementation using [logrus](https://github.com/sirupsen/logrus) [![GitHub stars](https://img.shields.io/github/stars/sirupsen/logrus?style=flat)](https://github.com/sirupsen/logrus/stargazers) logger.
- [logrusly](https://github.com/sebest/logrusly) [![GitHub stars](https://img.shields.io/github/stars/sebest/logrusly?style=flat)](https://github.com/sebest/logrusly/stargazers) - [logrus](https://github.com/sirupsen/logrus) [![GitHub stars](https://img.shields.io/github/stars/sirupsen/logrus?style=flat)](https://github.com/sirupsen/logrus/stargazers) plug-in to send errors to a [Loggly](https://www.loggly.com/).
- [logutils](https://github.com/hashicorp/logutils) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/logutils?style=flat)](https://github.com/hashicorp/logutils/stargazers) - Utilities for slightly better logging in Go (Golang) extending the standard logger.
- [logxi](https://github.com/mgutz/logxi) [![GitHub stars](https://img.shields.io/github/stars/mgutz/logxi?style=flat)](https://github.com/mgutz/logxi/stargazers) - 12-factor app logger that is fast and makes you happy.
- [lumberjack](https://github.com/natefinch/lumberjack) [![GitHub stars](https://img.shields.io/github/stars/natefinch/lumberjack?style=flat)](https://github.com/natefinch/lumberjack/stargazers) - Simple rolling logger, implements io.WriteCloser.
- [mlog](https://github.com/jbrodriguez/mlog) [![GitHub stars](https://img.shields.io/github/stars/jbrodriguez/mlog?style=flat)](https://github.com/jbrodriguez/mlog/stargazers) - Simple logging module for go, with 5 levels, an optional rotating logfile feature and stdout/stderr output.
- [noodlog](https://github.com/gyozatech/noodlog) [![GitHub stars](https://img.shields.io/github/stars/gyozatech/noodlog?style=flat)](https://github.com/gyozatech/noodlog/stargazers) - Parametrized JSON logging library which lets you obfuscate sensitive data and marshal any kind of content. No more printed pointers instead of values, nor escape chars for the JSON strings.
- [onelog](https://github.com/francoispqt/onelog) [![GitHub stars](https://img.shields.io/github/stars/francoispqt/onelog?style=flat)](https://github.com/francoispqt/onelog/stargazers) - Onelog is a dead simple but very efficient JSON logger. It is the fastest JSON logger out there in all scenarios. Also, it is one of the logger with the lowest allocation.
- [ozzo-log](https://github.com/go-ozzo/ozzo-log) [![GitHub stars](https://img.shields.io/github/stars/go-ozzo/ozzo-log?style=flat)](https://github.com/go-ozzo/ozzo-log/stargazers) - High performance logging supporting log severity, categorization, and filtering. Can send filtered log messages to various targets (e.g. console, network, mail).
- [phuslu/log](https://github.com/phuslu/log) [![GitHub stars](https://img.shields.io/github/stars/phuslu/log?style=flat)](https://github.com/phuslu/log/stargazers) - High performance structured logging.
- [pp](https://github.com/k0kubun/pp) [![GitHub stars](https://img.shields.io/github/stars/k0kubun/pp?style=flat)](https://github.com/k0kubun/pp/stargazers) - Colored pretty printer for Go language.
- [rollingwriter](https://github.com/arthurkiller/rollingWriter) [![GitHub stars](https://img.shields.io/github/stars/arthurkiller/rollingWriter?style=flat)](https://github.com/arthurkiller/rollingWriter/stargazers) - RollingWriter is an auto-rotate `io.Writer` implementation with multi policies to provide log file rotation.
- [seelog](https://github.com/cihub/seelog) [![GitHub stars](https://img.shields.io/github/stars/cihub/seelog?style=flat)](https://github.com/cihub/seelog/stargazers) - Logging functionality with flexible dispatching, filtering, and formatting.
- [sentry-go](https://github.com/getsentry/sentry-go) [![GitHub stars](https://img.shields.io/github/stars/getsentry/sentry-go?style=flat)](https://github.com/getsentry/sentry-go/stargazers) - Sentry SDK for Go. Helps monitor and track errors with real-time alerts and performance monitoring.
- [slf4g](https://github.com/echocat/slf4g) [![GitHub stars](https://img.shields.io/github/stars/echocat/slf4g?style=flat)](https://github.com/echocat/slf4g/stargazers) - Simple Logging Facade for Golang: Simple structured logging; but powerful, extendable and customizable, with huge amount of learnings from decades of past logging frameworks.
- [slog](https://github.com/gookit/slog) [![GitHub stars](https://img.shields.io/github/stars/gookit/slog?style=flat)](https://github.com/gookit/slog/stargazers) - Lightweight, configurable, extensible logger for Go.
- [slog-formatter](https://github.com/samber/slog-formatter) [![GitHub stars](https://img.shields.io/github/stars/samber/slog-formatter?style=flat)](https://github.com/samber/slog-formatter/stargazers) - Common formatters for slog and helpers to build your own.
- [slog-multi](https://github.com/samber/slog-multi) [![GitHub stars](https://img.shields.io/github/stars/samber/slog-multi?style=flat)](https://github.com/samber/slog-multi/stargazers) - Chain of slog.Handler (pipeline, fanout...).
- [slogor](https://gitlab.com/greyxor/slogor) - A colorful slog handler.
- [spew](https://github.com/davecgh/go-spew) [![GitHub stars](https://img.shields.io/github/stars/davecgh/go-spew?style=flat)](https://github.com/davecgh/go-spew/stargazers) - Implements a deep pretty printer for Go data structures to aid in debugging.
- [sqldb-logger](https://github.com/simukti/sqldb-logger) [![GitHub stars](https://img.shields.io/github/stars/simukti/sqldb-logger?style=flat)](https://github.com/simukti/sqldb-logger/stargazers) - A logger for Go SQL database driver without modify existing \*sql.DB stdlib usage.
- [stdlog](https://github.com/alexcesaro/log) [![GitHub stars](https://img.shields.io/github/stars/alexcesaro/log?style=flat)](https://github.com/alexcesaro/log/stargazers) - Stdlog is an object-oriented library providing leveled logging. It is very useful for cron jobs.
- [structy/log](https://github.com/structy/log) [![GitHub stars](https://img.shields.io/github/stars/structy/log?style=flat)](https://github.com/structy/log/stargazers) - A simple to use log system, minimalist but with features for debugging and differentiation of messages.
- [tail](https://github.com/hpcloud/tail) [![GitHub stars](https://img.shields.io/github/stars/hpcloud/tail?style=flat)](https://github.com/hpcloud/tail/stargazers) - Go package striving to emulate the features of the BSD tail program.
- [timberjack](https://github.com/DeRuina/timberjack) [![GitHub stars](https://img.shields.io/github/stars/DeRuina/timberjack?style=flat)](https://github.com/DeRuina/timberjack/stargazers) - Rolling logger with size-based, time-based, and scheduled clock-based rotation, supporting compression and cleanup.
- [tint](https://github.com/lmittmann/tint) [![GitHub stars](https://img.shields.io/github/stars/lmittmann/tint?style=flat)](https://github.com/lmittmann/tint/stargazers) - A slog.Handler that writes tinted logs.
- [xlog](https://github.com/xfxdev/xlog) [![GitHub stars](https://img.shields.io/github/stars/xfxdev/xlog?style=flat)](https://github.com/xfxdev/xlog/stargazers) - Plugin architecture and flexible log system for Go, with level ctrl, multiple log target and custom log format.
- [xlog](https://github.com/rs/xlog) [![GitHub stars](https://img.shields.io/github/stars/rs/xlog?style=flat)](https://github.com/rs/xlog/stargazers) - Structured logger for `net/context` aware HTTP handlers with flexible dispatching.
- [xylog](https://github.com/xybor-x/xylog) [![GitHub stars](https://img.shields.io/github/stars/xybor-x/xylog?style=flat)](https://github.com/xybor-x/xylog/stargazers) - Leveled and structured logging, dynamic fields, high performance, zone management, simple configuration, and readable syntax.
- [yell](https://github.com/jfcg/yell) [![GitHub stars](https://img.shields.io/github/stars/jfcg/yell?style=flat)](https://github.com/jfcg/yell/stargazers) - Yet another minimalistic logging library.
- [zap](https://github.com/uber-go/zap) [![GitHub stars](https://img.shields.io/github/stars/uber-go/zap?style=flat)](https://github.com/uber-go/zap/stargazers) - Fast, structured, leveled logging in Go.
- [zax](https://github.com/yuseferi/zax) [![GitHub stars](https://img.shields.io/github/stars/yuseferi/zax?style=flat)](https://github.com/yuseferi/zax/stargazers) - Integrate Context with Zap logger, which leads to more flexibility in Go logging.
- [zerolog](https://github.com/rs/zerolog) [![GitHub stars](https://img.shields.io/github/stars/rs/zerolog?style=flat)](https://github.com/rs/zerolog/stargazers) - Zero-allocation JSON logger.
- [zkits-logger](https://github.com/edoger/zkits-logger) [![GitHub stars](https://img.shields.io/github/stars/edoger/zkits-logger?style=flat)](https://github.com/edoger/zkits-logger/stargazers) - A powerful zero-dependency JSON logger.
- [zl](https://github.com/nkmr-jp/zl) [![GitHub stars](https://img.shields.io/github/stars/nkmr-jp/zl?style=flat)](https://github.com/nkmr-jp/zl/stargazers) - High Developer Experience, zap based logger. It offers rich functionality but is easy to configure.

**[⬆ back to top](#contents)**

## Machine Learning

_Libraries for Machine Learning._

- [Anneal](https://github.com/georgebuilds/anneal) [![GitHub stars](https://img.shields.io/github/stars/georgebuilds/anneal?style=flat)](https://github.com/georgebuilds/anneal/stargazers) - Machine learning compiler in Go, a from-scratch tinygrad port with a WebGPU backend.
- [bayesian](https://github.com/jbrukh/bayesian) [![GitHub stars](https://img.shields.io/github/stars/jbrukh/bayesian?style=flat)](https://github.com/jbrukh/bayesian/stargazers) - Naive Bayesian Classification for Golang.
- [born](https://github.com/born-ml/born) [![GitHub stars](https://img.shields.io/github/stars/born-ml/born?style=flat)](https://github.com/born-ml/born/stargazers) - Deep learning framework inspired by Burn (Rust), with autograd, type-safe tensors, and zero-CGO GPU acceleration.
- [catboost-cgo](https://github.com/mirecl/catboost-cgo) [![GitHub stars](https://img.shields.io/github/stars/mirecl/catboost-cgo?style=flat)](https://github.com/mirecl/catboost-cgo/stargazers) - Fast, scalable, high performance Gradient Boosting on Decision Trees library. Golang using Cgo for blazing fast inference CatBoost Model.
- [CloudForest](https://github.com/ryanbressler/CloudForest) [![GitHub stars](https://img.shields.io/github/stars/ryanbressler/CloudForest?style=flat)](https://github.com/ryanbressler/CloudForest/stargazers) - Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go.
- [datatrax](https://github.com/rbmuller/datatrax) [![GitHub stars](https://img.shields.io/github/stars/rbmuller/datatrax?style=flat)](https://github.com/rbmuller/datatrax/stargazers) - Data engineering and classic ML toolkit with batch processing, type coercion, and 7 algorithms in pure Go with zero dependencies.
- [ddt](https://github.com/sgrodriguez/ddt) [![GitHub stars](https://img.shields.io/github/stars/sgrodriguez/ddt?style=flat)](https://github.com/sgrodriguez/ddt/stargazers) - Dynamic decision tree, create trees defining customizable rules.
- [eaopt](https://github.com/MaxHalford/eaopt) [![GitHub stars](https://img.shields.io/github/stars/MaxHalford/eaopt?style=flat)](https://github.com/MaxHalford/eaopt/stargazers) - An evolutionary optimization library.
- [evoli](https://github.com/khezen/evoli) [![GitHub stars](https://img.shields.io/github/stars/khezen/evoli?style=flat)](https://github.com/khezen/evoli/stargazers) - Genetic Algorithm and Particle Swarm Optimization library.
- [fonet](https://github.com/Fontinalis/fonet) [![GitHub stars](https://img.shields.io/github/stars/Fontinalis/fonet?style=flat)](https://github.com/Fontinalis/fonet/stargazers) - A Deep Neural Network library written in Go.
- [go-cluster](https://github.com/e-XpertSolutions/go-cluster) [![GitHub stars](https://img.shields.io/github/stars/e-XpertSolutions/go-cluster?style=flat)](https://github.com/e-XpertSolutions/go-cluster/stargazers) - Go implementation of the k-modes and k-prototypes clustering algorithms.
- [go-deep](https://github.com/patrikeh/go-deep) [![GitHub stars](https://img.shields.io/github/stars/patrikeh/go-deep?style=flat)](https://github.com/patrikeh/go-deep/stargazers) - A feature-rich neural network library in Go.
- [go-fann](https://github.com/white-pony/go-fann) [![GitHub stars](https://img.shields.io/github/stars/white-pony/go-fann?style=flat)](https://github.com/white-pony/go-fann/stargazers) - Go bindings for Fast Artificial Neural Networks(FANN) library.
- [go-galib](https://github.com/thoj/go-galib) [![GitHub stars](https://img.shields.io/github/stars/thoj/go-galib?style=flat)](https://github.com/thoj/go-galib/stargazers) - Genetic Algorithms library written in Go / golang.
- [go-pr](https://github.com/daviddengcn/go-pr) [![GitHub stars](https://img.shields.io/github/stars/daviddengcn/go-pr?style=flat)](https://github.com/daviddengcn/go-pr/stargazers) - Pattern recognition package in Go lang.
- [gobrain](https://github.com/goml/gobrain) [![GitHub stars](https://img.shields.io/github/stars/goml/gobrain?style=flat)](https://github.com/goml/gobrain/stargazers) - Neural Networks written in go.
- [godist](https://github.com/e-dard/godist) [![GitHub stars](https://img.shields.io/github/stars/e-dard/godist?style=flat)](https://github.com/e-dard/godist/stargazers) - Various probability distributions, and associated methods.
- [goga](https://github.com/tomcraven/goga) [![GitHub stars](https://img.shields.io/github/stars/tomcraven/goga?style=flat)](https://github.com/tomcraven/goga/stargazers) - Genetic algorithm library for Go.
- [GoLearn](https://github.com/sjwhitworth/golearn) [![GitHub stars](https://img.shields.io/github/stars/sjwhitworth/golearn?style=flat)](https://github.com/sjwhitworth/golearn/stargazers) - General Machine Learning library for Go.
- [GoMind](https://github.com/surenderthakran/gomind) [![GitHub stars](https://img.shields.io/github/stars/surenderthakran/gomind?style=flat)](https://github.com/surenderthakran/gomind/stargazers) - A simplistic Neural Network Library in Go.
- [goml](https://github.com/cdipaolo/goml) [![GitHub stars](https://img.shields.io/github/stars/cdipaolo/goml?style=flat)](https://github.com/cdipaolo/goml/stargazers) - On-line Machine Learning in Go.
- [GoMLX](https://github.com/gomlx/gomlx) [![GitHub stars](https://img.shields.io/github/stars/gomlx/gomlx?style=flat)](https://github.com/gomlx/gomlx/stargazers) - An accelerated Machine Learning framework for Go.
- [gonet](https://github.com/dathoangnd/gonet) [![GitHub stars](https://img.shields.io/github/stars/dathoangnd/gonet?style=flat)](https://github.com/dathoangnd/gonet/stargazers) - Neural Network for Go.
- [Goptuna](https://github.com/c-bata/goptuna) [![GitHub stars](https://img.shields.io/github/stars/c-bata/goptuna?style=flat)](https://github.com/c-bata/goptuna/stargazers) - Bayesian optimization framework for black-box functions written in Go. Everything will be optimized.
- [goRecommend](https://github.com/timkaye11/goRecommend) [![GitHub stars](https://img.shields.io/github/stars/timkaye11/goRecommend?style=flat)](https://github.com/timkaye11/goRecommend/stargazers) - Recommendation Algorithms library written in Go.
- [gorgonia](https://github.com/gorgonia/gorgonia) [![GitHub stars](https://img.shields.io/github/stars/gorgonia/gorgonia?style=flat)](https://github.com/gorgonia/gorgonia/stargazers) - graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms.
- [gorse](https://github.com/zhenghaoz/gorse) [![GitHub stars](https://img.shields.io/github/stars/zhenghaoz/gorse?style=flat)](https://github.com/zhenghaoz/gorse/stargazers) - An offline recommender system backend based on collaborative filtering written in Go.
- [goscore](https://github.com/asafschers/goscore) [![GitHub stars](https://img.shields.io/github/stars/asafschers/goscore?style=flat)](https://github.com/asafschers/goscore/stargazers) - Go Scoring API for PMML.
- [gosseract](https://github.com/otiai10/gosseract) [![GitHub stars](https://img.shields.io/github/stars/otiai10/gosseract?style=flat)](https://github.com/otiai10/gosseract/stargazers) - Go package for OCR (Optical Character Recognition), by using Tesseract C++ library.
- [hugot](https://github.com/knights-analytics/hugot) [![GitHub stars](https://img.shields.io/github/stars/knights-analytics/hugot?style=flat)](https://github.com/knights-analytics/hugot/stargazers) - Huggingface transformer pipelines for golang with onnxruntime.
- [libsvm](https://github.com/datastream/libsvm) [![GitHub stars](https://img.shields.io/github/stars/datastream/libsvm?style=flat)](https://github.com/datastream/libsvm/stargazers) - libsvm golang version derived work based on LIBSVM 3.14.
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) [![GitHub stars](https://img.shields.io/github/stars/BayesWitnesses/m2cgen?style=flat)](https://github.com/BayesWitnesses/m2cgen/stargazers) - A CLI tool to transpile trained classic ML models into a native Go code with zero dependencies, written in Python with Go language support.
- [neural-go](https://github.com/schuyler/neural-go) [![GitHub stars](https://img.shields.io/github/stars/schuyler/neural-go?style=flat)](https://github.com/schuyler/neural-go/stargazers) - Multilayer perceptron network implemented in Go, with training via backpropagation.
- [ocrserver](https://github.com/otiai10/ocrserver) [![GitHub stars](https://img.shields.io/github/stars/otiai10/ocrserver?style=flat)](https://github.com/otiai10/ocrserver/stargazers) - A simple OCR API server, seriously easy to be deployed by Docker and Heroku.
- [onnx-go](https://github.com/owulveryck/onnx-go) [![GitHub stars](https://img.shields.io/github/stars/owulveryck/onnx-go?style=flat)](https://github.com/owulveryck/onnx-go/stargazers) - Go Interface to Open Neural Network Exchange (ONNX).
- [probab](https://github.com/ThePaw/probab) [![GitHub stars](https://img.shields.io/github/stars/ThePaw/probab?style=flat)](https://github.com/ThePaw/probab/stargazers) - Probability distribution functions. Bayesian inference. Written in pure Go.
- [randomforest](https://github.com/malaschitz/randomForest) [![GitHub stars](https://img.shields.io/github/stars/malaschitz/randomForest?style=flat)](https://github.com/malaschitz/randomForest/stargazers) - Easy to use Random Forest library for Go.
- [regommend](https://github.com/muesli/regommend) [![GitHub stars](https://img.shields.io/github/stars/muesli/regommend?style=flat)](https://github.com/muesli/regommend/stargazers) - Recommendation & collaborative filtering engine.
- [shield](https://github.com/eaigner/shield) [![GitHub stars](https://img.shields.io/github/stars/eaigner/shield?style=flat)](https://github.com/eaigner/shield/stargazers) - Bayesian text classifier with flexible tokenizers and storage backends for Go.
- [tfgo](https://github.com/galeone/tfgo) [![GitHub stars](https://img.shields.io/github/stars/galeone/tfgo?style=flat)](https://github.com/galeone/tfgo/stargazers) - Easy to use Tensorflow bindings: simplifies the usage of the official Tensorflow Go bindings. Define computational graphs in Go, load and execute models trained in Python.
- [Varis](https://github.com/Xamber/Varis) [![GitHub stars](https://img.shields.io/github/stars/Xamber/Varis?style=flat)](https://github.com/Xamber/Varis/stargazers) - Golang Neural Network.

**[⬆ back to top](#contents)**

## Messaging

_Libraries that implement messaging systems._

- [ami](https://github.com/kak-tus/ami) [![GitHub stars](https://img.shields.io/github/stars/kak-tus/ami?style=flat)](https://github.com/kak-tus/ami/stargazers) - Go client to reliable queues based on Redis Cluster Streams.
- [amqp](https://github.com/rabbitmq/amqp091-go) [![GitHub stars](https://img.shields.io/github/stars/rabbitmq/amqp091-go?style=flat)](https://github.com/rabbitmq/amqp091-go/stargazers) - Go RabbitMQ Client Library.
- [APNs2](https://github.com/sideshow/apns2) [![GitHub stars](https://img.shields.io/github/stars/sideshow/apns2?style=flat)](https://github.com/sideshow/apns2/stargazers) - HTTP/2 Apple Push Notification provider for Go - Send push notifications to iOS, tvOS, Safari and OSX apps.
- [Asynq](https://github.com/hibiken/asynq) [![GitHub stars](https://img.shields.io/github/stars/hibiken/asynq?style=flat)](https://github.com/hibiken/asynq/stargazers) - A simple, reliable, and efficient distributed task queue for Go built on top of Redis.
- [backlite](https://github.com/mikestefanello/backlite) [![GitHub stars](https://img.shields.io/github/stars/mikestefanello/backlite?style=flat)](https://github.com/mikestefanello/backlite/stargazers) - Type-safe, persistent, embedded task queues and background job runner w/ SQLite.
- [Beaver](https://github.com/Clivern/Beaver) [![GitHub stars](https://img.shields.io/github/stars/Clivern/Beaver?style=flat)](https://github.com/Clivern/Beaver/stargazers) - A real time messaging server to build a scalable in-app notifications, multiplayer games, chat apps in web and mobile apps.
- [broker](https://github.com/qvcloud/broker) [![GitHub stars](https://img.shields.io/github/stars/qvcloud/broker?style=flat)](https://github.com/qvcloud/broker/stargazers) - Production-grade messaging abstraction with a unified API for various brokers and built-in OpenTelemetry integration.
- [Bus](https://github.com/mustafaturan/bus) [![GitHub stars](https://img.shields.io/github/stars/mustafaturan/bus?style=flat)](https://github.com/mustafaturan/bus/stargazers) - Minimalist message bus implementation for internal communication.
- [Centrifugo](https://github.com/centrifugal/centrifugo) [![GitHub stars](https://img.shields.io/github/stars/centrifugal/centrifugo?style=flat)](https://github.com/centrifugal/centrifugo/stargazers) - Real-time messaging (Websockets or SockJS) server in Go.
- [Chanify](https://github.com/chanify/chanify) [![GitHub stars](https://img.shields.io/github/stars/chanify/chanify?style=flat)](https://github.com/chanify/chanify/stargazers) - A push notification server send message to your iOS devices.
- [Commander](https://github.com/jeroenrinzema/commander) [![GitHub stars](https://img.shields.io/github/stars/jeroenrinzema/commander?style=flat)](https://github.com/jeroenrinzema/commander/stargazers) - A high-level event driven consumer/producer supporting various "dialects" such as Apache Kafka.
- [Confluent Kafka Golang Client](https://github.com/confluentinc/confluent-kafka-go) [![GitHub stars](https://img.shields.io/github/stars/confluentinc/confluent-kafka-go?style=flat)](https://github.com/confluentinc/confluent-kafka-go/stargazers) - confluent-kafka-go is Confluent's Golang client for Apache Kafka and the Confluent Platform.
- [dbus](https://github.com/godbus/dbus) [![GitHub stars](https://img.shields.io/github/stars/godbus/dbus?style=flat)](https://github.com/godbus/dbus/stargazers) - Native Go bindings for D-Bus.
- [drone-line](https://github.com/appleboy/drone-line) [![GitHub stars](https://img.shields.io/github/stars/appleboy/drone-line?style=flat)](https://github.com/appleboy/drone-line/stargazers) - Sending [Line](https://at.line.me/en) notifications using a binary, docker or Drone CI.
- [emitter](https://github.com/olebedev/emitter) [![GitHub stars](https://img.shields.io/github/stars/olebedev/emitter?style=flat)](https://github.com/olebedev/emitter/stargazers) - Emits events using Go way, with wildcard, predicates, cancellation possibilities and many other good wins.
- [event](https://github.com/agoalofalife/event) [![GitHub stars](https://img.shields.io/github/stars/agoalofalife/event?style=flat)](https://github.com/agoalofalife/event/stargazers) - Implementation of the pattern observer.
- [EventBus](https://github.com/asaskevich/EventBus) [![GitHub stars](https://img.shields.io/github/stars/asaskevich/EventBus?style=flat)](https://github.com/asaskevich/EventBus/stargazers) - The lightweight event bus with async compatibility.
- [gaurun-client](https://github.com/osamingo/gaurun-client) [![GitHub stars](https://img.shields.io/github/stars/osamingo/gaurun-client?style=flat)](https://github.com/osamingo/gaurun-client/stargazers) - Gaurun Client written in Go.
- [Glue](https://github.com/desertbit/glue) [![GitHub stars](https://img.shields.io/github/stars/desertbit/glue?style=flat)](https://github.com/desertbit/glue/stargazers) - Robust Go and Javascript Socket Library (Alternative to Socket.io).
- [go-eventbus](https://github.com/stanipetrosyan/go-eventbus) [![GitHub stars](https://img.shields.io/github/stars/stanipetrosyan/go-eventbus?style=flat)](https://github.com/stanipetrosyan/go-eventbus/stargazers) - Simple Event Bus package for Go.
- [Go-MediatR](https://github.com/mehdihadeli/Go-MediatR) [![GitHub stars](https://img.shields.io/github/stars/mehdihadeli/Go-MediatR?style=flat)](https://github.com/mehdihadeli/Go-MediatR/stargazers) - A library for handling mediator patterns and simplified CQRS patterns within an event-driven architecture, inspired by csharp MediatR library.
- [go-mq](https://github.com/cheshir/go-mq) [![GitHub stars](https://img.shields.io/github/stars/cheshir/go-mq?style=flat)](https://github.com/cheshir/go-mq/stargazers) - RabbitMQ client with declarative configuration.
- [go-notify](https://github.com/TheCreeper/go-notify) [![GitHub stars](https://img.shields.io/github/stars/TheCreeper/go-notify?style=flat)](https://github.com/TheCreeper/go-notify/stargazers) - Native implementation of the freedesktop notification spec.
- [go-nsq](https://github.com/nsqio/go-nsq) [![GitHub stars](https://img.shields.io/github/stars/nsqio/go-nsq?style=flat)](https://github.com/nsqio/go-nsq/stargazers) - the official Go package for NSQ.
- [go-res](https://github.com/jirenius/go-res) [![GitHub stars](https://img.shields.io/github/stars/jirenius/go-res?style=flat)](https://github.com/jirenius/go-res/stargazers) - Package for building REST/real-time services where clients are synchronized seamlessly, using NATS and Resgate.
- [go-vitotrol](https://github.com/maxatome/go-vitotrol) [![GitHub stars](https://img.shields.io/github/stars/maxatome/go-vitotrol?style=flat)](https://github.com/maxatome/go-vitotrol/stargazers) - Client library to Viessmann Vitotrol web service.
- [GoEventBus](https://github.com/Raezil/GoEventBus) [![GitHub stars](https://img.shields.io/github/stars/Raezil/GoEventBus?style=flat)](https://github.com/Raezil/GoEventBus/stargazers) - A blazing‑fast, in‑memory, lock‑free event bus library
- [Gollum](https://github.com/trivago/gollum) [![GitHub stars](https://img.shields.io/github/stars/trivago/gollum?style=flat)](https://github.com/trivago/gollum/stargazers) - A n:m multiplexer that gathers messages from different sources and broadcasts them to a set of destinations.
- [golongpoll](https://github.com/jcuga/golongpoll) [![GitHub stars](https://img.shields.io/github/stars/jcuga/golongpoll?style=flat)](https://github.com/jcuga/golongpoll/stargazers) - HTTP longpoll server library that makes web pub-sub simple.
- [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) [![GitHub stars](https://img.shields.io/github/stars/Terry-Mao/gopush-cluster?style=flat)](https://github.com/Terry-Mao/gopush-cluster/stargazers) - gopush-cluster is a go push server cluster.
- [gorush](https://github.com/appleboy/gorush) [![GitHub stars](https://img.shields.io/github/stars/appleboy/gorush?style=flat)](https://github.com/appleboy/gorush/stargazers) - Push notification server using [APNs2](https://github.com/sideshow/apns2) [![GitHub stars](https://img.shields.io/github/stars/sideshow/apns2?style=flat)](https://github.com/sideshow/apns2/stargazers) and google [GCM](https://github.com/google/go-gcm) [![GitHub stars](https://img.shields.io/github/stars/google/go-gcm?style=flat)](https://github.com/google/go-gcm/stargazers).
- [gosd](https://github.com/alexsniffin/gosd) [![GitHub stars](https://img.shields.io/github/stars/alexsniffin/gosd?style=flat)](https://github.com/alexsniffin/gosd/stargazers) - A library for scheduling when to dispatch a message to a channel.
- [guble](https://github.com/smancke/guble) [![GitHub stars](https://img.shields.io/github/stars/smancke/guble?style=flat)](https://github.com/smancke/guble/stargazers) - Messaging server using push notifications (Google Firebase Cloud Messaging, Apple Push Notification services, SMS) as well as websockets, a REST API, featuring distributed operation and message-persistence.
- [hare](https://github.com/leozz37/hare) [![GitHub stars](https://img.shields.io/github/stars/leozz37/hare?style=flat)](https://github.com/leozz37/hare/stargazers) - A user friendly library for sending messages and listening to TCP sockets.
- [hub](https://github.com/leandro-lugaresi/hub) [![GitHub stars](https://img.shields.io/github/stars/leandro-lugaresi/hub?style=flat)](https://github.com/leandro-lugaresi/hub/stargazers) - A Message/Event Hub for Go applications, using publish/subscribe pattern with support for alias like rabbitMQ exchanges.
- [hypermatch](https://github.com/SchwarzIT/hypermatch) [![GitHub stars](https://img.shields.io/github/stars/SchwarzIT/hypermatch?style=flat)](https://github.com/SchwarzIT/hypermatch/stargazers) - A very fast and efficient Go library for matching events to a large set of rules
- [jazz](https://github.com/socifi/jazz) [![GitHub stars](https://img.shields.io/github/stars/socifi/jazz?style=flat)](https://github.com/socifi/jazz/stargazers) - A simple RabbitMQ abstraction layer for queue administration and publishing and consuming of messages.
- [machinery](https://github.com/RichardKnop/machinery) [![GitHub stars](https://img.shields.io/github/stars/RichardKnop/machinery?style=flat)](https://github.com/RichardKnop/machinery/stargazers) - Asynchronous task queue/job queue based on distributed message passing.
- [mangos](https://github.com/nanomsg/mangos) [![GitHub stars](https://img.shields.io/github/stars/nanomsg/mangos?style=flat)](https://github.com/nanomsg/mangos/stargazers) - Pure go implementation of the Nanomsg ("Scalability Protocols") with transport interoperability.
- [melody](https://github.com/olahol/melody) [![GitHub stars](https://img.shields.io/github/stars/olahol/melody?style=flat)](https://github.com/olahol/melody/stargazers) - Minimalist framework for dealing with websocket sessions, includes broadcasting and automatic ping/pong handling.
- [Mercure](https://github.com/dunglas/mercure) [![GitHub stars](https://img.shields.io/github/stars/dunglas/mercure?style=flat)](https://github.com/dunglas/mercure/stargazers) - Server and library to dispatch server-sent updates using the Mercure protocol (built on top of Server-Sent Events).
- [messagebus](https://github.com/vardius/message-bus) [![GitHub stars](https://img.shields.io/github/stars/vardius/message-bus?style=flat)](https://github.com/vardius/message-bus/stargazers) - messagebus is a Go simple async message bus, perfect for using as event bus when doing event sourcing, CQRS, DDD.
- [NATS Go Client](https://github.com/nats-io/nats.go) [![GitHub stars](https://img.shields.io/github/stars/nats-io/nats.go?style=flat)](https://github.com/nats-io/nats.go/stargazers) - Go client for the NATS
  messaging system.
- [nsq-event-bus](https://github.com/rafaeljesus/nsq-event-bus) [![GitHub stars](https://img.shields.io/github/stars/rafaeljesus/nsq-event-bus?style=flat)](https://github.com/rafaeljesus/nsq-event-bus/stargazers) - A tiny wrapper around NSQ topic and channel.
- [oplog](https://github.com/dailymotion/oplog) [![GitHub stars](https://img.shields.io/github/stars/dailymotion/oplog?style=flat)](https://github.com/dailymotion/oplog/stargazers) - Generic oplog/replication system for REST APIs.
- [pubsub](https://github.com/tuxychandru/pubsub) [![GitHub stars](https://img.shields.io/github/stars/tuxychandru/pubsub?style=flat)](https://github.com/tuxychandru/pubsub/stargazers) - Simple pubsub package for go.
- [Quamina](https://github.com/timbray/quamina) [![GitHub stars](https://img.shields.io/github/stars/timbray/quamina?style=flat)](https://github.com/timbray/quamina/stargazers) - Fast pattern-matching for filtering messages and events.
- [rabbitroutine](https://github.com/furdarius/rabbitroutine) [![GitHub stars](https://img.shields.io/github/stars/furdarius/rabbitroutine?style=flat)](https://github.com/furdarius/rabbitroutine/stargazers) - Lightweight library that handles RabbitMQ auto-reconnect and publishing retries. The library takes into account the need to re-declare entities in RabbitMQ after reconnection.
- [rabbus](https://github.com/rafaeljesus/rabbus) [![GitHub stars](https://img.shields.io/github/stars/rafaeljesus/rabbus?style=flat)](https://github.com/rafaeljesus/rabbus/stargazers) - A tiny wrapper over amqp exchanges and queues.
- [rabtap](https://github.com/jandelgado/rabtap) [![GitHub stars](https://img.shields.io/github/stars/jandelgado/rabtap?style=flat)](https://github.com/jandelgado/rabtap/stargazers) - RabbitMQ swiss army knife cli app.
- [RapidMQ](https://github.com/sybrexsys/RapidMQ) [![GitHub stars](https://img.shields.io/github/stars/sybrexsys/RapidMQ?style=flat)](https://github.com/sybrexsys/RapidMQ/stargazers) - RapidMQ is a lightweight and reliable library for managing of the local messages queue.
- [Ratus](https://github.com/hyperonym/ratus) [![GitHub stars](https://img.shields.io/github/stars/hyperonym/ratus?style=flat)](https://github.com/hyperonym/ratus/stargazers) - Ratus is a RESTful asynchronous task queue server.
- [redisqueue](https://github.com/robinjoseph08/redisqueue) [![GitHub stars](https://img.shields.io/github/stars/robinjoseph08/redisqueue?style=flat)](https://github.com/robinjoseph08/redisqueue/stargazers) - redisqueue provides a producer and consumer of a queue that uses Redis streams.
- [rmqconn](https://github.com/sbabiv/rmqconn) [![GitHub stars](https://img.shields.io/github/stars/sbabiv/rmqconn?style=flat)](https://github.com/sbabiv/rmqconn/stargazers) - RabbitMQ Reconnection. Wrapper over amqp.Connection and amqp.Dial. Allowing to do a reconnection when the connection is broken before forcing the call to the Close () method to be closed.
- [sarama](https://github.com/Shopify/sarama) [![GitHub stars](https://img.shields.io/github/stars/Shopify/sarama?style=flat)](https://github.com/Shopify/sarama/stargazers) - Go library for Apache Kafka.
- [Uniqush-Push](https://github.com/uniqush/uniqush-push) [![GitHub stars](https://img.shields.io/github/stars/uniqush/uniqush-push?style=flat)](https://github.com/uniqush/uniqush-push/stargazers) - Redis backed unified push service for server-side notifications to mobile devices.
- [varmq](https://github.com/goptics/varmq) [![GitHub stars](https://img.shields.io/github/stars/goptics/varmq?style=flat)](https://github.com/goptics/varmq/stargazers) - A storage-agnostic message queue and worker pool for concurrent Go programs.
- [Watermill](https://github.com/ThreeDotsLabs/watermill) [![GitHub stars](https://img.shields.io/github/stars/ThreeDotsLabs/watermill?style=flat)](https://github.com/ThreeDotsLabs/watermill/stargazers) - Working efficiently with message streams. Building event driven applications, enabling event sourcing, RPC over messages, sagas. Can use conventional pub/sub implementations like Kafka or RabbitMQ, but also HTTP or MySQL binlog.
- [zmq4](https://github.com/pebbe/zmq4) [![GitHub stars](https://img.shields.io/github/stars/pebbe/zmq4?style=flat)](https://github.com/pebbe/zmq4/stargazers) - Go interface to ZeroMQ version 4. Also available for [version 3](https://github.com/pebbe/zmq3) [![GitHub stars](https://img.shields.io/github/stars/pebbe/zmq3?style=flat)](https://github.com/pebbe/zmq3/stargazers) and [version 2](https://github.com/pebbe/zmq2) [![GitHub stars](https://img.shields.io/github/stars/pebbe/zmq2?style=flat)](https://github.com/pebbe/zmq2/stargazers).

**[⬆ back to top](#contents)**

## Microsoft Office

- [unioffice](https://github.com/unidoc/unioffice) [![GitHub stars](https://img.shields.io/github/stars/unidoc/unioffice?style=flat)](https://github.com/unidoc/unioffice/stargazers) - Pure go library for creating and processing Office Word (.docx), Excel (.xlsx) and Powerpoint (.pptx) documents.

### Microsoft Excel

_Libraries for working with Microsoft Excel._

- [cellwalker](https://github.com/chonla/cellwalker) [![GitHub stars](https://img.shields.io/github/stars/chonla/cellwalker?style=flat)](https://github.com/chonla/cellwalker/stargazers) - Virtually traverse Excel cell by cell's name.
- [excelize](https://github.com/xuri/excelize) [![GitHub stars](https://img.shields.io/github/stars/xuri/excelize?style=flat)](https://github.com/xuri/excelize/stargazers) - Golang library for reading and writing Microsoft Excel&trade; (XLSX) files.
- [exl](https://github.com/go-the-way/exl) [![GitHub stars](https://img.shields.io/github/stars/go-the-way/exl?style=flat)](https://github.com/go-the-way/exl/stargazers) - Excel binding to struct written in Go.(Only supports Go1.18+)
- [go-excel](https://github.com/szyhf/go-excel) [![GitHub stars](https://img.shields.io/github/stars/szyhf/go-excel?style=flat)](https://github.com/szyhf/go-excel/stargazers) - A simple and light reader to read a relate-db-like excel as a table.
- [xlsx](https://github.com/tealeg/xlsx) [![GitHub stars](https://img.shields.io/github/stars/tealeg/xlsx?style=flat)](https://github.com/tealeg/xlsx/stargazers) - Library to simplify reading the XML format used by recent version of Microsoft Excel in Go programs.
- [xlsx](https://github.com/plandem/xlsx) [![GitHub stars](https://img.shields.io/github/stars/plandem/xlsx?style=flat)](https://github.com/plandem/xlsx/stargazers) - Fast and safe way to read/update your existing Microsoft Excel files in Go programs.

### Microsoft Word

_Libraries for working with Microsoft Word._

- [godocx](https://github.com/gomutex/godocx) [![GitHub stars](https://img.shields.io/github/stars/gomutex/godocx?style=flat)](https://github.com/gomutex/godocx/stargazers) - Library for reading and writing Microsoft Word (Docx) files.

**[⬆ back to top](#contents)**

## Miscellaneous

### Dependency Injection

_Libraries for working with dependency injection._

- [alice](https://github.com/magic003/alice) [![GitHub stars](https://img.shields.io/github/stars/magic003/alice?style=flat)](https://github.com/magic003/alice/stargazers) - Additive dependency injection container for Golang.
- [autowire](https://github.com/tiendc/autowire) [![GitHub stars](https://img.shields.io/github/stars/tiendc/autowire?style=flat)](https://github.com/tiendc/autowire/stargazers) - Dependency injection using Generics and reflection.
- [boot-go](http://github.com/boot-go/boot) - Component-based development with dependency injection using reflections for Go developers.
- [componego](https://github.com/componego/componego) [![GitHub stars](https://img.shields.io/github/stars/componego/componego?style=flat)](https://github.com/componego/componego/stargazers) - A dependency injection framework based on components, allowing dynamic dependency replacement without duplicating code in tests.
- [cosban/di](https://gitlab.com/cosban/di) - A code generation based dependency injection wiring tool.
- [di](https://github.com/goava/di) [![GitHub stars](https://img.shields.io/github/stars/goava/di?style=flat)](https://github.com/goava/di/stargazers) - A dependency injection container for go programming language.
- [dig](https://github.com/uber-go/dig) [![GitHub stars](https://img.shields.io/github/stars/uber-go/dig?style=flat)](https://github.com/uber-go/dig/stargazers) - A reflection based dependency injection toolkit for Go.
- [dingo](https://github.com/i-love-flamingo/dingo) [![GitHub stars](https://img.shields.io/github/stars/i-love-flamingo/dingo?style=flat)](https://github.com/i-love-flamingo/dingo/stargazers) - A dependency injection toolkit for Go, based on Guice.
- [do](https://github.com/samber/do) [![GitHub stars](https://img.shields.io/github/stars/samber/do?style=flat)](https://github.com/samber/do/stargazers) - A dependency injection framework based on Generics.
- [fx](https://github.com/uber-go/fx) [![GitHub stars](https://img.shields.io/github/stars/uber-go/fx?style=flat)](https://github.com/uber-go/fx/stargazers) - A dependency injection based application framework for Go (built on top of dig).
- [go-beans](https://github.com/go-beans/go) [![GitHub stars](https://img.shields.io/github/stars/go-beans/go?style=flat)](https://github.com/go-beans/go/stargazers) - Spring-inspired dependency injection and application lifecycle framework for Go.
- [Go-Spring](https://github.com/go-spring/spring-core) [![GitHub stars](https://img.shields.io/github/stars/go-spring/spring-core?style=flat)](https://github.com/go-spring/spring-core/stargazers) - A high-performance Go framework inspired by Spring Boot, offering DI, auto-configuration, and lifecycle management while maintaining Go's simplicity and efficiency.
- [gocontainer](https://github.com/vardius/gocontainer) [![GitHub stars](https://img.shields.io/github/stars/vardius/gocontainer?style=flat)](https://github.com/vardius/gocontainer/stargazers) - Simple Dependency Injection Container.
- [godi](https://github.com/junioryono/godi) [![GitHub stars](https://img.shields.io/github/stars/junioryono/godi?style=flat)](https://github.com/junioryono/godi/stargazers) - Microsoft-style dependency injection for Go with scoped lifetimes and generics.
- [goioc/di](https://github.com/goioc/di) [![GitHub stars](https://img.shields.io/github/stars/goioc/di?style=flat)](https://github.com/goioc/di/stargazers) - Spring-inspired Dependency Injection Container.
- [GoLobby/Container](https://github.com/golobby/container) [![GitHub stars](https://img.shields.io/github/stars/golobby/container?style=flat)](https://github.com/golobby/container/stargazers) - GoLobby Container is a lightweight yet powerful IoC dependency injection container for the Go programming language.
- [gontainer](https://github.com/NVIDIA/gontainer) [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/gontainer?style=flat)](https://github.com/NVIDIA/gontainer/stargazers) - A dependency injection service container for Go projects.
- [gontainer/gontainer](https://github.com/gontainer/gontainer) [![GitHub stars](https://img.shields.io/github/stars/gontainer/gontainer?style=flat)](https://github.com/gontainer/gontainer/stargazers) - A YAML-based Dependency Injection container for GO. It supports dependencies' scopes, and auto-detection of circular dependencies. Gontainer is concurrent-safe.
- [HnH/di](https://github.com/HnH/di) [![GitHub stars](https://img.shields.io/github/stars/HnH/di?style=flat)](https://github.com/HnH/di/stargazers) - DI container library that is focused on clean API and flexibility.
- [kinit](https://github.com/go-kata/kinit) [![GitHub stars](https://img.shields.io/github/stars/go-kata/kinit?style=flat)](https://github.com/go-kata/kinit/stargazers) - Customizable dependency injection container with the global mode, cascade initialization and panic-safe finalization.
- [kod](https://github.com/go-kod/kod) [![GitHub stars](https://img.shields.io/github/stars/go-kod/kod?style=flat)](https://github.com/go-kod/kod/stargazers) - A generics based dependency injection framework for Go.
- [linker](https://github.com/logrange/linker) [![GitHub stars](https://img.shields.io/github/stars/logrange/linker?style=flat)](https://github.com/logrange/linker/stargazers) - A reflection based dependency injection and inversion of control library with components lifecycle support.
- [nject](https://github.com/muir/nject) [![GitHub stars](https://img.shields.io/github/stars/muir/nject?style=flat)](https://github.com/muir/nject/stargazers) - A type safe, reflective framework for libraries, tests, http endpoints, and service startup.
- [ore](https://github.com/firasdarwish/ore) [![GitHub stars](https://img.shields.io/github/stars/firasdarwish/ore?style=flat)](https://github.com/firasdarwish/ore/stargazers) - Lightweight, generic & simple dependency injection (DI) container.
- [parsley](https://github.com/matzefriedrich/parsley) [![GitHub stars](https://img.shields.io/github/stars/matzefriedrich/parsley?style=flat)](https://github.com/matzefriedrich/parsley/stargazers) - A flexible and modular reflection-based DI library with advanced features like scoped contexts and proxy generation, designed for large-scale Go applications.
- [wire](https://github.com/Fs02/wire) [![GitHub stars](https://img.shields.io/github/stars/Fs02/wire?style=flat)](https://github.com/Fs02/wire/stargazers) - Strict Runtime Dependency Injection for Golang.

**[⬆ back to top](#contents)**

### Project Layout

_**Unofficial** set of patterns for structuring projects._

- [ardanlabs/service](https://github.com/ardanlabs/service) [![GitHub stars](https://img.shields.io/github/stars/ardanlabs/service?style=flat)](https://github.com/ardanlabs/service/stargazers) - A [starter kit](https://github.com/ardanlabs/service/wiki) [![GitHub stars](https://img.shields.io/github/stars/ardanlabs/service/wiki?style=flat)](https://github.com/ardanlabs/service/wiki/stargazers) for building production grade scalable web service applications.
- [cookiecutter-golang](https://github.com/lacion/cookiecutter-golang) [![GitHub stars](https://img.shields.io/github/stars/lacion/cookiecutter-golang?style=flat)](https://github.com/lacion/cookiecutter-golang/stargazers) - A Go application boilerplate template for quick starting projects following production best practices.
- [go-blueprint](https://github.com/Melkeydev/go-blueprint) [![GitHub stars](https://img.shields.io/github/stars/Melkeydev/go-blueprint?style=flat)](https://github.com/Melkeydev/go-blueprint/stargazers) - Allows users to spin up a quick Go project using a popular framework.
- [go-module](https://github.com/octomation/go-module) [![GitHub stars](https://img.shields.io/github/stars/octomation/go-module?style=flat)](https://github.com/octomation/go-module/stargazers) - Template for a typical module written on Go.
- [go-rest-api-boilerplate](https://github.com/vahiiiid/go-rest-api-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/vahiiiid/go-rest-api-boilerplate?style=flat)](https://github.com/vahiiiid/go-rest-api-boilerplate/stargazers) - AI-friendly, production-ready Go REST API boilerplate with clean architecture, JWT authentication, RBAC, PostgreSQL, Docker hot-reload, and Swagger documentation.
- [go-sample](https://github.com/zitryss/go-sample) [![GitHub stars](https://img.shields.io/github/stars/zitryss/go-sample?style=flat)](https://github.com/zitryss/go-sample/stargazers) - A sample layout for Go application projects with the real code.
- [go-starter](https://github.com/allaboutapps/go-starter) [![GitHub stars](https://img.shields.io/github/stars/allaboutapps/go-starter?style=flat)](https://github.com/allaboutapps/go-starter/stargazers) - An opinionated production-ready RESTful JSON backend template, highly integrated with VSCode DevContainers.
- [go-todo-backend](https://github.com/Fs02/go-todo-backend) [![GitHub stars](https://img.shields.io/github/stars/Fs02/go-todo-backend?style=flat)](https://github.com/Fs02/go-todo-backend/stargazers) - Go Todo Backend example using modular project layout for product microservice.
- [goapp](https://github.com/naughtygopher/goapp) [![GitHub stars](https://img.shields.io/github/stars/naughtygopher/goapp?style=flat)](https://github.com/naughtygopher/goapp/stargazers) - An opinionated guideline to structure & develop a Go web application/service.
- [gobase](https://github.com/wajox/gobase) [![GitHub stars](https://img.shields.io/github/stars/wajox/gobase?style=flat)](https://github.com/wajox/gobase/stargazers) - A simple skeleton for golang application with basic setup for real golang application.
- [golang-standards/project-layout](https://github.com/golang-standards/project-layout) [![GitHub stars](https://img.shields.io/github/stars/golang-standards/project-layout?style=flat)](https://github.com/golang-standards/project-layout/stargazers) - Set of common historical and emerging project layout patterns in the Go ecosystem. Note: despite the org-name they do not represent official golang standards, see [this issue](https://github.com/golang-standards/project-layout/issues/117) [![GitHub stars](https://img.shields.io/github/stars/golang-standards/project-layout/issues/117?style=flat)](https://github.com/golang-standards/project-layout/issues/117/stargazers) for more information. Nonetheless, some may find the layout useful.
- [golang-templates/seed](https://github.com/golang-templates/seed) [![GitHub stars](https://img.shields.io/github/stars/golang-templates/seed?style=flat)](https://github.com/golang-templates/seed/stargazers) - Go application GitHub repository template.
- [goxygen](https://github.com/shpota/goxygen) [![GitHub stars](https://img.shields.io/github/stars/shpota/goxygen?style=flat)](https://github.com/shpota/goxygen/stargazers) - Generate a modern Web project with Go and Angular, React, or Vue in seconds.
- [insidieux/inizio](https://github.com/insidieux/inizio) [![GitHub stars](https://img.shields.io/github/stars/insidieux/inizio?style=flat)](https://github.com/insidieux/inizio/stargazers) - Golang project layout generator with plugins.
- [kickstart.go](https://github.com/raeperd/kickstart.go) [![GitHub stars](https://img.shields.io/github/stars/raeperd/kickstart.go?style=flat)](https://github.com/raeperd/kickstart.go/stargazers) - Minimalistic single-file Go HTTP server template without third-party dependencies.
- [modern-go-application](https://github.com/sagikazarmark/modern-go-application) [![GitHub stars](https://img.shields.io/github/stars/sagikazarmark/modern-go-application?style=flat)](https://github.com/sagikazarmark/modern-go-application/stargazers) - Go application boilerplate and example applying modern practices.
- [nunu](https://github.com/go-nunu/nunu) [![GitHub stars](https://img.shields.io/github/stars/go-nunu/nunu?style=flat)](https://github.com/go-nunu/nunu/stargazers) - Nunu is a scaffolding tool for building Go applications.
- [pagoda](https://github.com/mikestefanello/pagoda) [![GitHub stars](https://img.shields.io/github/stars/mikestefanello/pagoda?style=flat)](https://github.com/mikestefanello/pagoda/stargazers) - Rapid, easy full-stack web development starter kit built in Go.
- [scaffold](https://github.com/catchplay/scaffold) [![GitHub stars](https://img.shields.io/github/stars/catchplay/scaffold?style=flat)](https://github.com/catchplay/scaffold/stargazers) - Scaffold generates a starter Go project layout. Lets you focus on business logic implemented.
- [wangyoucao577/go-project-layout](https://github.com/wangyoucao577/go-project-layout) [![GitHub stars](https://img.shields.io/github/stars/wangyoucao577/go-project-layout?style=flat)](https://github.com/wangyoucao577/go-project-layout/stargazers) - Set of practices and discussions on how to structure Go project layout.

**[⬆ back to top](#contents)**

### Strings

_Libraries for working with strings._

- [bexp](https://github.com/happy-sdk/happy/tree/main/pkg/strings/bexp) [![GitHub stars](https://img.shields.io/github/stars/happy-sdk/happy/tree/main/pkg/strings/bexp?style=flat)](https://github.com/happy-sdk/happy/tree/main/pkg/strings/bexp/stargazers) - Go implementation of Brace Expansion mechanism to generate arbitrary strings.
- [caps](https://github.com/chanced/caps) [![GitHub stars](https://img.shields.io/github/stars/chanced/caps?style=flat)](https://github.com/chanced/caps/stargazers) - A case conversion library.
- [go-formatter](https://gitlab.com/tymonx/go-formatter) - Implements **replacement fields** surrounded by curly braces `{}` format strings.
- [gobeam/Stringy](https://github.com/gobeam/Stringy) [![GitHub stars](https://img.shields.io/github/stars/gobeam/Stringy?style=flat)](https://github.com/gobeam/Stringy/stargazers) - String manipulation library to convert string to camel case, snake case, kebab case / slugify etc.
- [str](https://github.com/schigh/str) [![GitHub stars](https://img.shields.io/github/stars/schigh/str?style=flat)](https://github.com/schigh/str/stargazers) - Pipeline-first string toolkit for composing transformations.
- [strcase](https://github.com/charlievieth/strcase) [![GitHub stars](https://img.shields.io/github/stars/charlievieth/strcase?style=flat)](https://github.com/charlievieth/strcase/stargazers) - Case-insensitive implementation of the standard library's strings/bytes packages.
- [stringFormatter](https://github.com/Wissance/stringFormatter) [![GitHub stars](https://img.shields.io/github/stars/Wissance/stringFormatter?style=flat)](https://github.com/Wissance/stringFormatter/stargazers) - String formatting like in Python or C# manner with the additional text formatting features.
- [strutil](https://github.com/ozgio/strutil) [![GitHub stars](https://img.shields.io/github/stars/ozgio/strutil?style=flat)](https://github.com/ozgio/strutil/stargazers) - String utilities.
- [sttr](https://github.com/abhimanyu003/sttr) [![GitHub stars](https://img.shields.io/github/stars/abhimanyu003/sttr?style=flat)](https://github.com/abhimanyu003/sttr/stargazers) - cross-platform, cli app to perform various operations on string.
- [xstrings](https://github.com/huandu/xstrings) [![GitHub stars](https://img.shields.io/github/stars/huandu/xstrings?style=flat)](https://github.com/huandu/xstrings/stargazers) - Collection of useful string functions ported from other languages.

**[⬆ back to top](#contents)**

### Uncategorized

_These libraries were placed here because none of the other categories seemed to fit._

- [anagent](https://github.com/mudler/anagent) [![GitHub stars](https://img.shields.io/github/stars/mudler/anagent?style=flat)](https://github.com/mudler/anagent/stargazers) - Minimalistic, pluggable Golang evloop/timer handler with dependency-injection.
- [antch](https://github.com/antchfx/antch) [![GitHub stars](https://img.shields.io/github/stars/antchfx/antch?style=flat)](https://github.com/antchfx/antch/stargazers) - A fast, powerful and extensible web crawling & scraping framework.
- [archives](https://github.com/mholt/archives) [![GitHub stars](https://img.shields.io/github/stars/mholt/archives?style=flat)](https://github.com/mholt/archives/stargazers) - a cross-platform, multi-format Go library for working with archives and compression formats with a unified API and as virtual file systems compatible with io/fs.
- [autoflags](https://github.com/artyom/autoflags) [![GitHub stars](https://img.shields.io/github/stars/artyom/autoflags?style=flat)](https://github.com/artyom/autoflags/stargazers) - Go package to automatically define command line flags from struct fields.
- [avgRating](https://github.com/kirillDanshin/avgRating) [![GitHub stars](https://img.shields.io/github/stars/kirillDanshin/avgRating?style=flat)](https://github.com/kirillDanshin/avgRating/stargazers) - Calculate average score and rating based on Wilson Score Equation.
- [banner](https://github.com/dimiro1/banner) [![GitHub stars](https://img.shields.io/github/stars/dimiro1/banner?style=flat)](https://github.com/dimiro1/banner/stargazers) - Add beautiful banners into your Go applications.
- [base64Captcha](https://github.com/mojocn/base64Captcha) [![GitHub stars](https://img.shields.io/github/stars/mojocn/base64Captcha?style=flat)](https://github.com/mojocn/base64Captcha/stargazers) - Base64captch supports digit, number, alphabet, arithmetic, audio and digit-alphabet captcha.
- [basexx](https://github.com/bobg/basexx) [![GitHub stars](https://img.shields.io/github/stars/bobg/basexx?style=flat)](https://github.com/bobg/basexx/stargazers) - Convert to, from, and between digit strings in various number bases.
- [battery](https://github.com/distatus/battery) [![GitHub stars](https://img.shields.io/github/stars/distatus/battery?style=flat)](https://github.com/distatus/battery/stargazers) - Cross-platform, normalized battery information library.
- [bitio](https://github.com/icza/bitio) [![GitHub stars](https://img.shields.io/github/stars/icza/bitio?style=flat)](https://github.com/icza/bitio/stargazers) - Highly optimized bit-level Reader and Writer for Go.
- [browscap_go](https://github.com/digitalcrab/browscap_go) [![GitHub stars](https://img.shields.io/github/stars/digitalcrab/browscap_go?style=flat)](https://github.com/digitalcrab/browscap_go/stargazers) - GoLang Library for [Browser Capabilities Project](https://browscap.org/).
- [captcha](https://github.com/steambap/captcha) [![GitHub stars](https://img.shields.io/github/stars/steambap/captcha?style=flat)](https://github.com/steambap/captcha/stargazers) - Package captcha provides an easy to use, unopinionated API for captcha generation.
- [common](https://github.com/kubeservice-stack/common) [![GitHub stars](https://img.shields.io/github/stars/kubeservice-stack/common?style=flat)](https://github.com/kubeservice-stack/common/stargazers) - A library for server framework.
- [conv](https://github.com/cstockton/go-conv) [![GitHub stars](https://img.shields.io/github/stars/cstockton/go-conv?style=flat)](https://github.com/cstockton/go-conv/stargazers) - Package conv provides fast and intuitive conversions across Go types.
- [datacounter](https://github.com/miolini/datacounter) [![GitHub stars](https://img.shields.io/github/stars/miolini/datacounter?style=flat)](https://github.com/miolini/datacounter/stargazers) - Go counters for readers/writer/http.ResponseWriter.
- [fake-useragent](https://github.com/lib4u/fake-useragent) [![GitHub stars](https://img.shields.io/github/stars/lib4u/fake-useragent?style=flat)](https://github.com/lib4u/fake-useragent/stargazers) - Up-to-date simple useragent faker with real world database in Golang
- [faker](https://github.com/pioz/faker) [![GitHub stars](https://img.shields.io/github/stars/pioz/faker?style=flat)](https://github.com/pioz/faker/stargazers) - Random fake data and struct generator for Go.
- [ffmt](https://github.com/go-ffmt/ffmt) [![GitHub stars](https://img.shields.io/github/stars/go-ffmt/ffmt?style=flat)](https://github.com/go-ffmt/ffmt/stargazers) - Beautify data display for Humans.
- [gatus](https://github.com/TwinProduction/gatus) [![GitHub stars](https://img.shields.io/github/stars/TwinProduction/gatus?style=flat)](https://github.com/TwinProduction/gatus/stargazers) - Automated service health dashboard.
- [go-commandbus](https://github.com/lana/go-commandbus) [![GitHub stars](https://img.shields.io/github/stars/lana/go-commandbus?style=flat)](https://github.com/lana/go-commandbus/stargazers) - A slight and pluggable command-bus for Go.
- [go-commons-pool](https://github.com/jolestar/go-commons-pool) [![GitHub stars](https://img.shields.io/github/stars/jolestar/go-commons-pool?style=flat)](https://github.com/jolestar/go-commons-pool/stargazers) - Generic object pool for Golang.
- [go-openapi](https://github.com/go-openapi) [![GitHub stars](https://img.shields.io/github/stars/go-openapi?style=flat)](https://github.com/go-openapi/stargazers) - Collection of packages to parse and utilize open-api schemas.
- [go-resiliency](https://github.com/eapache/go-resiliency) [![GitHub stars](https://img.shields.io/github/stars/eapache/go-resiliency?style=flat)](https://github.com/eapache/go-resiliency/stargazers) - Resiliency patterns for golang.
- [go-unarr](https://github.com/gen2brain/go-unarr) [![GitHub stars](https://img.shields.io/github/stars/gen2brain/go-unarr?style=flat)](https://github.com/gen2brain/go-unarr/stargazers) - Decompression library for RAR, TAR, ZIP and 7z archives.
- [gofakeit](https://github.com/brianvoe/gofakeit) [![GitHub stars](https://img.shields.io/github/stars/brianvoe/gofakeit?style=flat)](https://github.com/brianvoe/gofakeit/stargazers) - Random data generator written in go.
- [goffi](https://github.com/go-webgpu/goffi) [![GitHub stars](https://img.shields.io/github/stars/go-webgpu/goffi?style=flat)](https://github.com/go-webgpu/goffi/stargazers) - Pure Go FFI with libffi-style typed call interface and structured error handling for calling C libraries without CGO.
- [gommit](https://github.com/antham/gommit) [![GitHub stars](https://img.shields.io/github/stars/antham/gommit?style=flat)](https://github.com/antham/gommit/stargazers) - Analyze git commit messages to ensure they follow defined patterns.
- [gopsutil](https://github.com/shirou/gopsutil) [![GitHub stars](https://img.shields.io/github/stars/shirou/gopsutil?style=flat)](https://github.com/shirou/gopsutil/stargazers) - Cross-platform library for retrieving process and system utilization(CPU, Memory, Disks, etc).
- [gosh](https://github.com/osamingo/gosh) [![GitHub stars](https://img.shields.io/github/stars/osamingo/gosh?style=flat)](https://github.com/osamingo/gosh/stargazers) - Provide Go Statistics Handler, Struct, Measure Method.
- [gosms](https://github.com/haxpax/gosms) [![GitHub stars](https://img.shields.io/github/stars/haxpax/gosms?style=flat)](https://github.com/haxpax/gosms/stargazers) - Your own local SMS gateway in Go that can be used to send SMS.
- [gotoprom](https://github.com/cabify/gotoprom) [![GitHub stars](https://img.shields.io/github/stars/cabify/gotoprom?style=flat)](https://github.com/cabify/gotoprom/stargazers) - Type-safe metrics builder wrapper library for the official Prometheus client.
- [gountries](https://github.com/pariz/gountries) [![GitHub stars](https://img.shields.io/github/stars/pariz/gountries?style=flat)](https://github.com/pariz/gountries/stargazers) - Package that exposes country and subdivision data.
- [gtree](https://github.com/ddddddO/gtree) [![GitHub stars](https://img.shields.io/github/stars/ddddddO/gtree?style=flat)](https://github.com/ddddddO/gtree/stargazers) - Provide CLI, Package and Web for tree output and directories creation from Markdown or programmatically.
- [health](https://github.com/alexliesenfeld/health) [![GitHub stars](https://img.shields.io/github/stars/alexliesenfeld/health?style=flat)](https://github.com/alexliesenfeld/health/stargazers) - A simple and flexible health check library for Go.
- [health](https://github.com/dimiro1/health) [![GitHub stars](https://img.shields.io/github/stars/dimiro1/health?style=flat)](https://github.com/dimiro1/health/stargazers) - Easy to use, extensible health check library.
- [healthcheck](https://github.com/etherlabsio/healthcheck) [![GitHub stars](https://img.shields.io/github/stars/etherlabsio/healthcheck?style=flat)](https://github.com/etherlabsio/healthcheck/stargazers) - An opinionated and concurrent health-check HTTP handler for RESTful services.
- [hostutils](https://github.com/Wing924/hostutils) [![GitHub stars](https://img.shields.io/github/stars/Wing924/hostutils?style=flat)](https://github.com/Wing924/hostutils/stargazers) - A golang library for packing and unpacking FQDNs list.
- [indigo](https://github.com/osamingo/indigo) [![GitHub stars](https://img.shields.io/github/stars/osamingo/indigo?style=flat)](https://github.com/osamingo/indigo/stargazers) - Distributed unique ID generator of using Sonyflake and encoded by Base58.
- [lk](https://github.com/hyperboloide/lk) [![GitHub stars](https://img.shields.io/github/stars/hyperboloide/lk?style=flat)](https://github.com/hyperboloide/lk/stargazers) - A simple licensing library for golang.
- [llvm](https://github.com/llir/llvm) [![GitHub stars](https://img.shields.io/github/stars/llir/llvm?style=flat)](https://github.com/llir/llvm/stargazers) - Library for interacting with LLVM IR in pure Go.
- [metrics](https://github.com/pascaldekloe/metrics) [![GitHub stars](https://img.shields.io/github/stars/pascaldekloe/metrics?style=flat)](https://github.com/pascaldekloe/metrics/stargazers) - Library for metrics instrumentation and Prometheus exposition.
- [morse](https://github.com/alwindoss/morse) [![GitHub stars](https://img.shields.io/github/stars/alwindoss/morse?style=flat)](https://github.com/alwindoss/morse/stargazers) - Library to convert to and from morse code.
- [numa](https://github.com/lrita/numa) [![GitHub stars](https://img.shields.io/github/stars/lrita/numa?style=flat)](https://github.com/lrita/numa/stargazers) - NUMA is a utility library, which is written in go. It help us to write some NUMA-AWARED code.
- [pdfgen](https://github.com/hyperboloide/pdfgen) [![GitHub stars](https://img.shields.io/github/stars/hyperboloide/pdfgen?style=flat)](https://github.com/hyperboloide/pdfgen/stargazers) - HTTP service to generate PDF from Json requests.
- [persian](https://github.com/mavihq/persian) [![GitHub stars](https://img.shields.io/github/stars/mavihq/persian?style=flat)](https://github.com/mavihq/persian/stargazers) - Some utilities for Persian language in go.
- [purego](https://github.com/ebitengine/purego) [![GitHub stars](https://img.shields.io/github/stars/ebitengine/purego?style=flat)](https://github.com/ebitengine/purego/stargazers) - A library for calling C functions from Go without Cgo.
- [sandid](https://github.com/aofei/sandid) [![GitHub stars](https://img.shields.io/github/stars/aofei/sandid?style=flat)](https://github.com/aofei/sandid/stargazers) - Every grain of sand on earth has its own ID.
- [shellwords](https://github.com/Wing924/shellwords) [![GitHub stars](https://img.shields.io/github/stars/Wing924/shellwords?style=flat)](https://github.com/Wing924/shellwords/stargazers) - A Golang library to manipulate strings according to the word parsing rules of the UNIX Bourne shell.
- [shortid](https://github.com/teris-io/shortid) [![GitHub stars](https://img.shields.io/github/stars/teris-io/shortid?style=flat)](https://github.com/teris-io/shortid/stargazers) - Distributed generation of super short, unique, non-sequential, URL friendly IDs.
- [shoutrrr](https://github.com/containrrr/shoutrrr) [![GitHub stars](https://img.shields.io/github/stars/containrrr/shoutrrr?style=flat)](https://github.com/containrrr/shoutrrr/stargazers) - Notification library providing easy access to various messaging services like slack, mattermost, gotify and smtp among others.
- [sitemap-format](https://github.com/mingard/sitemap-format) [![GitHub stars](https://img.shields.io/github/stars/mingard/sitemap-format?style=flat)](https://github.com/mingard/sitemap-format/stargazers) - A simple sitemap generator, with a little syntactic sugar.
- [stateless](https://github.com/qmuntal/stateless) [![GitHub stars](https://img.shields.io/github/stars/qmuntal/stateless?style=flat)](https://github.com/qmuntal/stateless/stargazers) - A fluent library for creating state machines.
- [stats](https://github.com/go-playground/stats) [![GitHub stars](https://img.shields.io/github/stars/go-playground/stats?style=flat)](https://github.com/go-playground/stats/stargazers) - Monitors Go MemStats + System stats such as Memory, Swap and CPU and sends via UDP anywhere you want for logging etc...
- [turtle](https://github.com/hackebrot/turtle) [![GitHub stars](https://img.shields.io/github/stars/hackebrot/turtle?style=flat)](https://github.com/hackebrot/turtle/stargazers) - Emojis for Go.
- [url-shortener](https://github.com/pantrif/url-shortener) [![GitHub stars](https://img.shields.io/github/stars/pantrif/url-shortener?style=flat)](https://github.com/pantrif/url-shortener/stargazers) - A modern, powerful, and robust URL shortener microservice with mysql support.
- [VarHandler](https://github.com/azr/generators/tree/master/varhandler) [![GitHub stars](https://img.shields.io/github/stars/azr/generators/tree/master/varhandler?style=flat)](https://github.com/azr/generators/tree/master/varhandler/stargazers) - Generate boilerplate http input and output handling.
- [varint](https://github.com/chmike/varint) [![GitHub stars](https://img.shields.io/github/stars/chmike/varint?style=flat)](https://github.com/chmike/varint/stargazers) - A faster varying length integer encoder/decoder than the one provided in the standard library.
- [xdg](https://github.com/rkoesters/xdg) [![GitHub stars](https://img.shields.io/github/stars/rkoesters/xdg?style=flat)](https://github.com/rkoesters/xdg/stargazers) - FreeDesktop.org (xdg) Specs implemented in Go.
- [xkg](https://github.com/go-xkg/xkg) [![GitHub stars](https://img.shields.io/github/stars/go-xkg/xkg?style=flat)](https://github.com/go-xkg/xkg/stargazers) - X Keyboard Grabber.
- [xz](https://github.com/ulikunitz/xz) [![GitHub stars](https://img.shields.io/github/stars/ulikunitz/xz?style=flat)](https://github.com/ulikunitz/xz/stargazers) - Pure golang package for reading and writing xz-compressed files.
**[⬆ back to top](#contents)**

## Natural Language Processing

_Libraries for working with human languages._

See also [Text Processing](#text-processing) and [Text Analysis](#text-analysis).

### Language Detection

- [detectlanguage](https://github.com/detectlanguage/detectlanguage-go) [![GitHub stars](https://img.shields.io/github/stars/detectlanguage/detectlanguage-go?style=flat)](https://github.com/detectlanguage/detectlanguage-go/stargazers) - Language Detection API Go Client. Supports batch requests, short phrase or single word language detection.
- [getlang](https://github.com/rylans/getlang) [![GitHub stars](https://img.shields.io/github/stars/rylans/getlang?style=flat)](https://github.com/rylans/getlang/stargazers) - Fast natural language detection package.
- [guesslanguage](https://github.com/endeveit/guesslanguage) [![GitHub stars](https://img.shields.io/github/stars/endeveit/guesslanguage?style=flat)](https://github.com/endeveit/guesslanguage/stargazers) - Functions to determine the natural language of a unicode text.
- [lingua-go](https://github.com/pemistahl/lingua-go) [![GitHub stars](https://img.shields.io/github/stars/pemistahl/lingua-go?style=flat)](https://github.com/pemistahl/lingua-go/stargazers) - An accurate natural language detection library, suitable for long and short text alike. Supports detecting multiple languages in mixed-language text.
- [whatlanggo](https://github.com/abadojack/whatlanggo) [![GitHub stars](https://img.shields.io/github/stars/abadojack/whatlanggo?style=flat)](https://github.com/abadojack/whatlanggo/stargazers) - Natural language detection package for Go. Supports 84 languages and 24 scripts (writing systems e.g. Latin, Cyrillic, etc).

### Morphological Analyzers

- [go-propisyu](https://github.com/rekurt/go-propisyu) [![GitHub stars](https://img.shields.io/github/stars/rekurt/go-propisyu?style=flat)](https://github.com/rekurt/go-propisyu/stargazers) - Convert numbers to Russian words with correct grammatical gender and noun declension.
- [go-stem](https://github.com/agonopol/go-stem) [![GitHub stars](https://img.shields.io/github/stars/agonopol/go-stem?style=flat)](https://github.com/agonopol/go-stem/stargazers) - Implementation of the porter stemming algorithm.
- [go2vec](https://github.com/danieldk/go2vec) [![GitHub stars](https://img.shields.io/github/stars/danieldk/go2vec?style=flat)](https://github.com/danieldk/go2vec/stargazers) - Reader and utility functions for word2vec embeddings.
- [golibstemmer](https://github.com/rjohnsondev/golibstemmer) [![GitHub stars](https://img.shields.io/github/stars/rjohnsondev/golibstemmer?style=flat)](https://github.com/rjohnsondev/golibstemmer/stargazers) - Go bindings for the snowball libstemmer library including porter 2.
- [gosentiwordnet](https://github.com/dinopuguh/gosentiwordnet) [![GitHub stars](https://img.shields.io/github/stars/dinopuguh/gosentiwordnet?style=flat)](https://github.com/dinopuguh/gosentiwordnet/stargazers) - Sentiment analyzer using sentiwordnet lexicon in Go.
- [govader](https://github.com/jonreiter/govader) [![GitHub stars](https://img.shields.io/github/stars/jonreiter/govader?style=flat)](https://github.com/jonreiter/govader/stargazers) - Go implementation of [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) [![GitHub stars](https://img.shields.io/github/stars/cjhutto/vaderSentiment?style=flat)](https://github.com/cjhutto/vaderSentiment/stargazers).
- [govader-backend](https://github.com/PIMPfiction/govader_backend) [![GitHub stars](https://img.shields.io/github/stars/PIMPfiction/govader_backend?style=flat)](https://github.com/PIMPfiction/govader_backend/stargazers) - Microservice implementation of [GoVader](https://github.com/jonreiter/govader) [![GitHub stars](https://img.shields.io/github/stars/jonreiter/govader?style=flat)](https://github.com/jonreiter/govader/stargazers).
- [kagome](https://github.com/ikawaha/kagome) [![GitHub stars](https://img.shields.io/github/stars/ikawaha/kagome?style=flat)](https://github.com/ikawaha/kagome/stargazers) - JP morphological analyzer written in pure Go.
- [libtextcat](https://github.com/goodsign/libtextcat) [![GitHub stars](https://img.shields.io/github/stars/goodsign/libtextcat?style=flat)](https://github.com/goodsign/libtextcat/stargazers) - Cgo binding for libtextcat C library. Guaranteed compatibility with version 2.2.
- [nlp](https://github.com/james-bowman/nlp) [![GitHub stars](https://img.shields.io/github/stars/james-bowman/nlp?style=flat)](https://github.com/james-bowman/nlp/stargazers) - Go Natural Language Processing library supporting LSA (Latent Semantic Analysis).
- [paicehusk](https://github.com/rookii/paicehusk) [![GitHub stars](https://img.shields.io/github/stars/rookii/paicehusk?style=flat)](https://github.com/rookii/paicehusk/stargazers) - Golang implementation of the Paice/Husk Stemming Algorithm.
- [porter](https://github.com/a2800276/porter) [![GitHub stars](https://img.shields.io/github/stars/a2800276/porter?style=flat)](https://github.com/a2800276/porter/stargazers) - This is a fairly straightforward port of Martin Porter's C implementation of the Porter stemming algorithm.
- [porter2](https://github.com/zhenjl/porter2) [![GitHub stars](https://img.shields.io/github/stars/zhenjl/porter2?style=flat)](https://github.com/zhenjl/porter2/stargazers) - Really fast Porter 2 stemmer.
- [RAKE.go](https://github.com/afjoseph/RAKE.Go) [![GitHub stars](https://img.shields.io/github/stars/afjoseph/RAKE.Go?style=flat)](https://github.com/afjoseph/RAKE.Go/stargazers) - Go port of the Rapid Automatic Keyword Extraction Algorithm (RAKE).
- [snowball](https://github.com/goodsign/snowball) [![GitHub stars](https://img.shields.io/github/stars/goodsign/snowball?style=flat)](https://github.com/goodsign/snowball/stargazers) - Snowball stemmer port (cgo wrapper) for Go. Provides word stem extraction functionality [Snowball native](http://snowball.tartarus.org/).
- [spaGO](https://github.com/nlpodyssey/spago) [![GitHub stars](https://img.shields.io/github/stars/nlpodyssey/spago?style=flat)](https://github.com/nlpodyssey/spago/stargazers) - Self-contained Machine Learning and Natural Language Processing library in Go.
- [spelling-corrector](https://github.com/jorelosorio/spellingcorrector) [![GitHub stars](https://img.shields.io/github/stars/jorelosorio/spellingcorrector?style=flat)](https://github.com/jorelosorio/spellingcorrector/stargazers) - A spelling corrector for the Spanish language or create your own.

### Slugifiers

- [go-slugify](https://github.com/mozillazg/go-slugify) [![GitHub stars](https://img.shields.io/github/stars/mozillazg/go-slugify?style=flat)](https://github.com/mozillazg/go-slugify/stargazers) - Make pretty slug with multiple languages support.
- [slug](https://github.com/gosimple/slug) [![GitHub stars](https://img.shields.io/github/stars/gosimple/slug?style=flat)](https://github.com/gosimple/slug/stargazers) - URL-friendly slugify with multiple languages support.
- [Slugify](https://github.com/avelino/slugify) [![GitHub stars](https://img.shields.io/github/stars/avelino/slugify?style=flat)](https://github.com/avelino/slugify/stargazers) - Go slugify application that handles string.

### Tokenizers

- [gojieba](https://github.com/yanyiwu/gojieba) [![GitHub stars](https://img.shields.io/github/stars/yanyiwu/gojieba?style=flat)](https://github.com/yanyiwu/gojieba/stargazers) - This is a Go implementation of [jieba](https://github.com/fxsjy/jieba) [![GitHub stars](https://img.shields.io/github/stars/fxsjy/jieba?style=flat)](https://github.com/fxsjy/jieba/stargazers) which a Chinese word splitting algorithm.
- [gotokenizer](https://github.com/xujiajun/gotokenizer) [![GitHub stars](https://img.shields.io/github/stars/xujiajun/gotokenizer?style=flat)](https://github.com/xujiajun/gotokenizer/stargazers) - A tokenizer based on the dictionary and Bigram language models for Golang. (Now only support chinese segmentation)
- [gse](https://github.com/go-ego/gse) [![GitHub stars](https://img.shields.io/github/stars/go-ego/gse?style=flat)](https://github.com/go-ego/gse/stargazers) - Go efficient text segmentation; support english, chinese, japanese and other.
- [MMSEGO](https://github.com/awsong/MMSEGO) [![GitHub stars](https://img.shields.io/github/stars/awsong/MMSEGO?style=flat)](https://github.com/awsong/MMSEGO/stargazers) - This is a GO implementation of [MMSEG](http://technology.chtsai.org/mmseg/) which a Chinese word splitting algorithm.
- [segment](https://github.com/blevesearch/segment) [![GitHub stars](https://img.shields.io/github/stars/blevesearch/segment?style=flat)](https://github.com/blevesearch/segment/stargazers) - Go library for performing Unicode Text Segmentation as described in [Unicode Standard Annex #29](https://www.unicode.org/reports/tr29/)
- [sentences](https://github.com/neurosnap/sentences) [![GitHub stars](https://img.shields.io/github/stars/neurosnap/sentences?style=flat)](https://github.com/neurosnap/sentences/stargazers) - Sentence tokenizer: converts text into a list of sentences.
- [shamoji](https://github.com/osamingo/shamoji) [![GitHub stars](https://img.shields.io/github/stars/osamingo/shamoji?style=flat)](https://github.com/osamingo/shamoji/stargazers) - The shamoji is word filtering package written in Go.
- [stemmer](https://github.com/dchest/stemmer) [![GitHub stars](https://img.shields.io/github/stars/dchest/stemmer?style=flat)](https://github.com/dchest/stemmer/stargazers) - Stemmer packages for Go programming language. Includes English and German stemmers.
- [textcat](https://github.com/pebbe/textcat) [![GitHub stars](https://img.shields.io/github/stars/pebbe/textcat?style=flat)](https://github.com/pebbe/textcat/stargazers) - Go package for n-gram based text categorization, with support for utf-8 and raw text.

### Translation

- [ctxi18n](https://github.com/invopop/ctxi18n/) [![GitHub stars](https://img.shields.io/github/stars/invopop/ctxi18n/?style=flat)](https://github.com/invopop/ctxi18n//stargazers) - Context aware i18n with a short and consise API, pluralization, interpolation, and `fs.FS` support. YAML locale definitions are based on [Rails i18n](https://guides.rubyonrails.org/i18n.html).
- [go-i18n](https://github.com/nicksnyder/go-i18n/) [![GitHub stars](https://img.shields.io/github/stars/nicksnyder/go-i18n/?style=flat)](https://github.com/nicksnyder/go-i18n//stargazers) - Package and an accompanying tool to work with localized text.
- [go-mystem](https://github.com/dveselov/mystem) [![GitHub stars](https://img.shields.io/github/stars/dveselov/mystem?style=flat)](https://github.com/dveselov/mystem/stargazers) - CGo bindings to Yandex.Mystem - russian morphology analyzer.
- [go-pinyin](https://github.com/mozillazg/go-pinyin) [![GitHub stars](https://img.shields.io/github/stars/mozillazg/go-pinyin?style=flat)](https://github.com/mozillazg/go-pinyin/stargazers) - CN Hanzi to Hanyu Pinyin converter.
- [go-words](https://github.com/saleh-rahimzadeh/go-words) [![GitHub stars](https://img.shields.io/github/stars/saleh-rahimzadeh/go-words?style=flat)](https://github.com/saleh-rahimzadeh/go-words/stargazers) - A words table and text resource library for Golang projects.
- [gotext](https://github.com/leonelquinteros/gotext) [![GitHub stars](https://img.shields.io/github/stars/leonelquinteros/gotext?style=flat)](https://github.com/leonelquinteros/gotext/stargazers) - GNU gettext utilities for Go.
- [iuliia-go](https://github.com/mehanizm/iuliia-go) [![GitHub stars](https://img.shields.io/github/stars/mehanizm/iuliia-go?style=flat)](https://github.com/mehanizm/iuliia-go/stargazers) - Transliterate Cyrillic → Latin in every possible way.
- [spreak](https://github.com/vorlif/spreak) [![GitHub stars](https://img.shields.io/github/stars/vorlif/spreak?style=flat)](https://github.com/vorlif/spreak/stargazers) - Flexible translation and humanization library for Go, based on the concepts behind gettext.
- [t](https://github.com/youthlin/t) [![GitHub stars](https://img.shields.io/github/stars/youthlin/t?style=flat)](https://github.com/youthlin/t/stargazers) - Another i18n pkg for golang, which follows GNU gettext style and supports .po/.mo files: `t.T (gettext)`, `t.N (ngettext)`, etc. And it contains a cmd tool [xtemplate](https://github.com/youthlin/t/blob/main/cmd/xtemplate) [![GitHub stars](https://img.shields.io/github/stars/youthlin/t/blob/main/cmd/xtemplate?style=flat)](https://github.com/youthlin/t/blob/main/cmd/xtemplate/stargazers), which can extract messages as a pot file from text/html template.

### Transliteration

- [enca](https://github.com/endeveit/enca) [![GitHub stars](https://img.shields.io/github/stars/endeveit/enca?style=flat)](https://github.com/endeveit/enca/stargazers) - Minimal cgo bindings for [libenca](https://cihar.com/software/enca/), which detects character encodings.
- [go-unidecode](https://github.com/mozillazg/go-unidecode) [![GitHub stars](https://img.shields.io/github/stars/mozillazg/go-unidecode?style=flat)](https://github.com/mozillazg/go-unidecode/stargazers) - ASCII transliterations of Unicode text.
- [gounidecode](https://github.com/fiam/gounidecode) [![GitHub stars](https://img.shields.io/github/stars/fiam/gounidecode?style=flat)](https://github.com/fiam/gounidecode/stargazers) - Unicode transliterator (also known as unidecode) for Go.
- [transliterator](https://github.com/alexsergivan/transliterator) [![GitHub stars](https://img.shields.io/github/stars/alexsergivan/transliterator?style=flat)](https://github.com/alexsergivan/transliterator/stargazers) - Provides one-way string transliteration with supporting of language-specific transliteration rules.

**[⬆ back to top](#contents)**

## Networking

_Libraries for working with various layers of the network._

- [arp](https://github.com/mdlayher/arp) [![GitHub stars](https://img.shields.io/github/stars/mdlayher/arp?style=flat)](https://github.com/mdlayher/arp/stargazers) - Package arp implements the ARP protocol, as described in RFC 826.
- [bart](https://github.com/gaissmai/bart) [![GitHub stars](https://img.shields.io/github/stars/gaissmai/bart?style=flat)](https://github.com/gaissmai/bart/stargazers) - Package bart provides a Balanced-Routing-Table (BART) for very fast IP to CIDR lookups and more.
- [buffstreams](https://github.com/stabbycutyou/buffstreams) [![GitHub stars](https://img.shields.io/github/stars/stabbycutyou/buffstreams?style=flat)](https://github.com/stabbycutyou/buffstreams/stargazers) - Streaming protocolbuffer data over TCP made easy.
- [canopus](https://github.com/zubairhamed/canopus) [![GitHub stars](https://img.shields.io/github/stars/zubairhamed/canopus?style=flat)](https://github.com/zubairhamed/canopus/stargazers) - CoAP Client/Server implementation (RFC 7252).
- [cdns](https://github.com/junevm/cdns) [![GitHub stars](https://img.shields.io/github/stars/junevm/cdns?style=flat)](https://github.com/junevm/cdns/stargazers) - Change DNS servers effortlessly via terminal.
- [cidranger](https://github.com/yl2chen/cidranger) [![GitHub stars](https://img.shields.io/github/stars/yl2chen/cidranger?style=flat)](https://github.com/yl2chen/cidranger/stargazers) - Fast IP to CIDR lookup for Go.
- [cloudflared](https://github.com/cloudflare/cloudflared) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/cloudflared?style=flat)](https://github.com/cloudflare/cloudflared/stargazers) - Cloudflare Tunnel client (formerly Argo Tunnel).
- [dhcp6](https://github.com/mdlayher/dhcp6) [![GitHub stars](https://img.shields.io/github/stars/mdlayher/dhcp6?style=flat)](https://github.com/mdlayher/dhcp6/stargazers) - Package dhcp6 implements a DHCPv6 server, as described in RFC 3315.
- [dns](https://github.com/miekg/dns) [![GitHub stars](https://img.shields.io/github/stars/miekg/dns?style=flat)](https://github.com/miekg/dns/stargazers) - Go library for working with DNS.
- [dnsmonster](https://github.com/mosajjal/dnsmonster) [![GitHub stars](https://img.shields.io/github/stars/mosajjal/dnsmonster?style=flat)](https://github.com/mosajjal/dnsmonster/stargazers) - Passive DNS Capture/Monitoring Framework.
- [easytcp](https://github.com/DarthPestilane/easytcp) [![GitHub stars](https://img.shields.io/github/stars/DarthPestilane/easytcp?style=flat)](https://github.com/DarthPestilane/easytcp/stargazers) - A light-weight TCP framework written in Go (Golang), built with message router. EasyTCP helps you build a TCP server easily fast and less painful.
- [ether](https://github.com/songgao/ether) [![GitHub stars](https://img.shields.io/github/stars/songgao/ether?style=flat)](https://github.com/songgao/ether/stargazers) - Cross-platform Go package for sending and receiving ethernet frames.
- [ethernet](https://github.com/mdlayher/ethernet) [![GitHub stars](https://img.shields.io/github/stars/mdlayher/ethernet?style=flat)](https://github.com/mdlayher/ethernet/stargazers) - Package ethernet implements marshaling and unmarshalling of IEEE 802.3 Ethernet II frames and IEEE 802.1Q VLAN tags.
- [event](https://github.com/cheng-zhongliang/event) [![GitHub stars](https://img.shields.io/github/stars/cheng-zhongliang/event?style=flat)](https://github.com/cheng-zhongliang/event/stargazers) - Simple I/O event notification library written in Golang.
- [fasthttp](https://github.com/valyala/fasthttp) [![GitHub stars](https://img.shields.io/github/stars/valyala/fasthttp?style=flat)](https://github.com/valyala/fasthttp/stargazers) - Package fasthttp is a fast HTTP implementation for Go, up to 10 times faster than net/http.
- [fibersse](https://github.com/vinod-morya/fibersse) [![GitHub stars](https://img.shields.io/github/stars/vinod-morya/fibersse?style=flat)](https://github.com/vinod-morya/fibersse/stargazers) - Production-grade Server-Sent Events (SSE) for Fiber v3 with event coalescing, priority lanes, topic wildcards, adaptive throttling, and built-in auth.
- [fortio](https://github.com/fortio/fortio) [![GitHub stars](https://img.shields.io/github/stars/fortio/fortio?style=flat)](https://github.com/fortio/fortio/stargazers) - Load testing library and command line tool, advanced echo server and web UI. Allows to specify a set query-per-second load and record latency histograms and other useful stats and graph them. Tcp, Http, gRPC.
- [ftp](https://github.com/jlaffaye/ftp) [![GitHub stars](https://img.shields.io/github/stars/jlaffaye/ftp?style=flat)](https://github.com/jlaffaye/ftp/stargazers) - Package ftp implements a FTP client as described in [RFC 959](https://tools.ietf.org/html/rfc959).
- [ftpserverlib](https://github.com/fclairamb/ftpserverlib) [![GitHub stars](https://img.shields.io/github/stars/fclairamb/ftpserverlib?style=flat)](https://github.com/fclairamb/ftpserverlib/stargazers) - Fully featured FTP server library.
- [fullproxy](https://github.com/shoriwe/fullproxy) [![GitHub stars](https://img.shields.io/github/stars/shoriwe/fullproxy?style=flat)](https://github.com/shoriwe/fullproxy/stargazers) - A fully featured scriptable and daemon configurable proxy and pivoting toolkit with SOCKS5, HTTP, raw ports and reverse proxy protocols.
- [fwdctl](https://github.com/alegrey91/fwdctl) [![GitHub stars](https://img.shields.io/github/stars/alegrey91/fwdctl?style=flat)](https://github.com/alegrey91/fwdctl/stargazers) - A simple and intuitive CLI to manage IPTables forwards in your Linux server.
- [gaio](https://github.com/xtaci/gaio) [![GitHub stars](https://img.shields.io/github/stars/xtaci/gaio?style=flat)](https://github.com/xtaci/gaio/stargazers) - High performance async-io networking for Golang in proactor mode.
- [gev](https://github.com/Allenxuxu/gev) [![GitHub stars](https://img.shields.io/github/stars/Allenxuxu/gev?style=flat)](https://github.com/Allenxuxu/gev/stargazers) - gev is a lightweight, fast non-blocking TCP network library based on Reactor mode.
- [gldap](https://github.com/jimlambrt/gldap) [![GitHub stars](https://img.shields.io/github/stars/jimlambrt/gldap?style=flat)](https://github.com/jimlambrt/gldap/stargazers) - gldap provides an ldap server implementation and you provide handlers for its ldap operations.
- [gmqtt](https://github.com/DrmagicE/gmqtt) [![GitHub stars](https://img.shields.io/github/stars/DrmagicE/gmqtt?style=flat)](https://github.com/DrmagicE/gmqtt/stargazers) - Gmqtt is a flexible, high-performance MQTT broker library that fully implements the MQTT protocol V3.1.1.
- [gnet](https://github.com/panjf2000/gnet) [![GitHub stars](https://img.shields.io/github/stars/panjf2000/gnet?style=flat)](https://github.com/panjf2000/gnet/stargazers) - `gnet` is a high-performance, lightweight, non-blocking, event-driven networking framework written in pure Go.
- [gnet](https://github.com/fish-tennis/gnet) [![GitHub stars](https://img.shields.io/github/stars/fish-tennis/gnet?style=flat)](https://github.com/fish-tennis/gnet/stargazers) - `gnet` is a high-performance networking framework,especially for game servers.
- [gNxI](https://github.com/google/gnxi) [![GitHub stars](https://img.shields.io/github/stars/google/gnxi?style=flat)](https://github.com/google/gnxi/stargazers) - A collection of tools for Network Management that use the gNMI and gNOI protocols.
- [go-getter](https://github.com/hashicorp/go-getter) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/go-getter?style=flat)](https://github.com/hashicorp/go-getter/stargazers) - Go library for downloading files or directories from various sources using a URL.
- [go-multiproxy](https://github.com/presbrey/go-multiproxy) [![GitHub stars](https://img.shields.io/github/stars/presbrey/go-multiproxy?style=flat)](https://github.com/presbrey/go-multiproxy/stargazers) - Library for making HTTP requests through a pool of proxies offering fault tolerance, load balancing, automatic retries, cookie management, and more, via http.Get/Post replacement or http.Client RoundTripper drop-in
- [go-pcaplite](https://github.com/alexcfv/go-pcaplite) [![GitHub stars](https://img.shields.io/github/stars/alexcfv/go-pcaplite?style=flat)](https://github.com/alexcfv/go-pcaplite/stargazers) - Lightweight live packet capture library with HTTPS SNI extraction.
- [go-powerdns](https://github.com/joeig/go-powerdns) [![GitHub stars](https://img.shields.io/github/stars/joeig/go-powerdns?style=flat)](https://github.com/joeig/go-powerdns/stargazers) - PowerDNS API bindings for Golang.
- [go-sse](https://github.com/lampctl/go-sse) [![GitHub stars](https://img.shields.io/github/stars/lampctl/go-sse?style=flat)](https://github.com/lampctl/go-sse/stargazers) - Go client and server implementation of HTML server-sent events.
- [go-stun](https://github.com/ccding/go-stun) [![GitHub stars](https://img.shields.io/github/stars/ccding/go-stun?style=flat)](https://github.com/ccding/go-stun/stargazers) - Go implementation of the STUN client (RFC 3489 and RFC 5389).
- [gobgp](https://github.com/osrg/gobgp) [![GitHub stars](https://img.shields.io/github/stars/osrg/gobgp?style=flat)](https://github.com/osrg/gobgp/stargazers) - BGP implemented in the Go Programming Language.
- [gopacket](https://github.com/google/gopacket) [![GitHub stars](https://img.shields.io/github/stars/google/gopacket?style=flat)](https://github.com/google/gopacket/stargazers) - Go library for packet processing with libpcap bindings.
- [gopcap](https://github.com/akrennmair/gopcap) [![GitHub stars](https://img.shields.io/github/stars/akrennmair/gopcap?style=flat)](https://github.com/akrennmair/gopcap/stargazers) - Go wrapper for libpcap.
- [GoProxy](https://github.com/elazarl/goproxy) [![GitHub stars](https://img.shields.io/github/stars/elazarl/goproxy?style=flat)](https://github.com/elazarl/goproxy/stargazers) - A library to create a customized HTTP/HTTPS proxy server using Go.
- [goshark](https://github.com/sunwxg/goshark) [![GitHub stars](https://img.shields.io/github/stars/sunwxg/goshark?style=flat)](https://github.com/sunwxg/goshark/stargazers) - Package goshark use tshark to decode IP packet and create data struct to analyse packet.
- [gosnmp](https://github.com/soniah/gosnmp) [![GitHub stars](https://img.shields.io/github/stars/soniah/gosnmp?style=flat)](https://github.com/soniah/gosnmp/stargazers) - Native Go library for performing SNMP actions.
- [gotcp](https://github.com/gansidui/gotcp) [![GitHub stars](https://img.shields.io/github/stars/gansidui/gotcp?style=flat)](https://github.com/gansidui/gotcp/stargazers) - Go package for quickly writing tcp applications.
- [grab](https://github.com/cavaliercoder/grab) [![GitHub stars](https://img.shields.io/github/stars/cavaliercoder/grab?style=flat)](https://github.com/cavaliercoder/grab/stargazers) - Go package for managing file downloads.
- [graval](https://github.com/koofr/graval) [![GitHub stars](https://img.shields.io/github/stars/koofr/graval?style=flat)](https://github.com/koofr/graval/stargazers) - Experimental FTP server framework.
- [gws](https://github.com/lxzan/gws) [![GitHub stars](https://img.shields.io/github/stars/lxzan/gws?style=flat)](https://github.com/lxzan/gws/stargazers) - High-Performance WebSocket Server & Client With AsyncIO Supporting .
- [HTTPLab](https://github.com/gchaincl/httplab) [![GitHub stars](https://img.shields.io/github/stars/gchaincl/httplab?style=flat)](https://github.com/gchaincl/httplab/stargazers) - HTTPLabs let you inspect HTTP requests and forge responses.
- [httpproxy](https://github.com/wzshiming/httpproxy) [![GitHub stars](https://img.shields.io/github/stars/wzshiming/httpproxy?style=flat)](https://github.com/wzshiming/httpproxy/stargazers) - HTTP proxy handler and dialer.
- [iplib](https://github.com/c-robinson/iplib) [![GitHub stars](https://img.shields.io/github/stars/c-robinson/iplib?style=flat)](https://github.com/c-robinson/iplib/stargazers) - Library for working with IP addresses (net.IP, net.IPNet), inspired by python [ipaddress](https://docs.python.org/3/library/ipaddress.html) and ruby [ipaddr](https://ruby-doc.org/stdlib-2.5.1/libdoc/ipaddr/rdoc/IPAddr.html)
- [jazigo](https://github.com/udhos/jazigo) [![GitHub stars](https://img.shields.io/github/stars/udhos/jazigo?style=flat)](https://github.com/udhos/jazigo/stargazers) - Jazigo is a tool written in Go for retrieving configuration for multiple network devices.
- [kcp-go](https://github.com/xtaci/kcp-go) [![GitHub stars](https://img.shields.io/github/stars/xtaci/kcp-go?style=flat)](https://github.com/xtaci/kcp-go/stargazers) - KCP - Fast and Reliable ARQ Protocol.
- [lhttp](https://github.com/fanux/lhttp) [![GitHub stars](https://img.shields.io/github/stars/fanux/lhttp?style=flat)](https://github.com/fanux/lhttp/stargazers) - Powerful websocket framework, build your IM server more easily.
- [linkio](https://github.com/ian-kent/linkio) [![GitHub stars](https://img.shields.io/github/stars/ian-kent/linkio?style=flat)](https://github.com/ian-kent/linkio/stargazers) - Network link speed simulation for Reader/Writer interfaces.
- [llb](https://github.com/kirillDanshin/llb) [![GitHub stars](https://img.shields.io/github/stars/kirillDanshin/llb?style=flat)](https://github.com/kirillDanshin/llb/stargazers) - It's a very simple but quick backend for proxy servers. Can be useful for fast redirection to predefined domain with zero memory allocation and fast response.
- [macwifi](https://github.com/jaisonerick/macwifi) [![GitHub stars](https://img.shields.io/github/stars/jaisonerick/macwifi?style=flat)](https://github.com/jaisonerick/macwifi/stargazers) - Wi-Fi scanning and Keychain password retrieval for macOS 13+.
- [mdns](https://github.com/hashicorp/mdns) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/mdns?style=flat)](https://github.com/hashicorp/mdns/stargazers) - Simple mDNS (Multicast DNS) client/server library in Golang.
- [mqttPaho](https://eclipse.org/paho/clients/golang/) - The Paho Go Client provides an MQTT client library for connection to MQTT brokers via TCP, TLS or WebSockets.
- [natiu-mqtt](https://github.com/soypat/natiu-mqtt) [![GitHub stars](https://img.shields.io/github/stars/soypat/natiu-mqtt?style=flat)](https://github.com/soypat/natiu-mqtt/stargazers) - A dead-simple, non-allocating, low level implementation of MQTT well suited for embedded systems.
- [nbio](https://github.com/lesismal/nbio) [![GitHub stars](https://img.shields.io/github/stars/lesismal/nbio?style=flat)](https://github.com/lesismal/nbio/stargazers) - Pure Go 1000k+ connections solution, support tls/http1.x/websocket and basically compatible with net/http, with high-performance and low memory cost, non-blocking, event-driven, easy-to-use.
- [net](https://golang.org/x/net) - This repository holds supplementary Go networking libraries.
- [netpoll](https://github.com/cloudwego/netpoll) [![GitHub stars](https://img.shields.io/github/stars/cloudwego/netpoll?style=flat)](https://github.com/cloudwego/netpoll/stargazers) - A high-performance non-blocking I/O networking framework, which focused on RPC scenarios, developed by ByteDance.
- [NFF-Go](https://github.com/intel-go/nff-go) [![GitHub stars](https://img.shields.io/github/stars/intel-go/nff-go?style=flat)](https://github.com/intel-go/nff-go/stargazers) - Framework for rapid development of performant network functions for cloud and bare-metal (former YANFF).
- [nodepass](https://github.com/NodePassProject/nodepass) [![GitHub stars](https://img.shields.io/github/stars/NodePassProject/nodepass?style=flat)](https://github.com/NodePassProject/nodepass/stargazers) - A secure, efficient TCP/UDP tunneling solution that delivers fast, reliable access across network restrictions using pre-established TCP/QUIC/WebSocket or HTTP/2 connections.
- [peerdiscovery](https://github.com/schollz/peerdiscovery) [![GitHub stars](https://img.shields.io/github/stars/schollz/peerdiscovery?style=flat)](https://github.com/schollz/peerdiscovery/stargazers) - Pure Go library for cross-platform local peer discovery using UDP multicast.
- [portproxy](https://github.com/aybabtme/portproxy) [![GitHub stars](https://img.shields.io/github/stars/aybabtme/portproxy?style=flat)](https://github.com/aybabtme/portproxy/stargazers) - Simple TCP proxy which adds CORS support to API's which don't support it.
- [psql-wire](https://github.com/jeroenrinzema/psql-wire) [![GitHub stars](https://img.shields.io/github/stars/jeroenrinzema/psql-wire?style=flat)](https://github.com/jeroenrinzema/psql-wire/stargazers) - PostgreSQL server wire protocol. Build your own server and start serving connections..
- [publicip](https://github.com/polera/publicip) [![GitHub stars](https://img.shields.io/github/stars/polera/publicip?style=flat)](https://github.com/polera/publicip/stargazers) - Package publicip returns your public facing IPv4 address (internet egress).
- [quic-go](https://github.com/lucas-clemente/quic-go) [![GitHub stars](https://img.shields.io/github/stars/lucas-clemente/quic-go?style=flat)](https://github.com/lucas-clemente/quic-go/stargazers) - An implementation of the QUIC protocol in pure Go.
- [sdns](https://github.com/semihalev/sdns) [![GitHub stars](https://img.shields.io/github/stars/semihalev/sdns?style=flat)](https://github.com/semihalev/sdns/stargazers) - A high-performance, recursive DNS resolver server with DNSSEC support, focused on preserving privacy.
- [sftp](https://github.com/pkg/sftp) [![GitHub stars](https://img.shields.io/github/stars/pkg/sftp?style=flat)](https://github.com/pkg/sftp/stargazers) - Package sftp implements the SSH File Transfer Protocol as described in <https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt>.
- [ssh](https://github.com/gliderlabs/ssh) [![GitHub stars](https://img.shields.io/github/stars/gliderlabs/ssh?style=flat)](https://github.com/gliderlabs/ssh/stargazers) - Higher-level API for building SSH servers (wraps crypto/ssh).
- [sslb](https://github.com/eduardonunesp/sslb) [![GitHub stars](https://img.shields.io/github/stars/eduardonunesp/sslb?style=flat)](https://github.com/eduardonunesp/sslb/stargazers) - It's a Super Simples Load Balancer, just a little project to achieve some kind of performance.
- [stun](https://github.com/go-rtc/stun) [![GitHub stars](https://img.shields.io/github/stars/go-rtc/stun?style=flat)](https://github.com/go-rtc/stun/stargazers) - Go implementation of RFC 5389 STUN protocol.
- [tcpack](https://github.com/lim-yoona/tcpack) [![GitHub stars](https://img.shields.io/github/stars/lim-yoona/tcpack?style=flat)](https://github.com/lim-yoona/tcpack/stargazers) - tcpack is an application protocol based on TCP to Pack and Unpack bytes stream in go program.
- [tspool](https://github.com/two/tspool) [![GitHub stars](https://img.shields.io/github/stars/two/tspool?style=flat)](https://github.com/two/tspool/stargazers) - A TCP Library use worker pool to improve performance and protect your server.
- [tun2socks](https://github.com/xjasonlyu/tun2socks) [![GitHub stars](https://img.shields.io/github/stars/xjasonlyu/tun2socks?style=flat)](https://github.com/xjasonlyu/tun2socks/stargazers) - A pure go implementation of tun2socks powered by [gVisor](https://gvisor.dev/) TCP/IP stack.
- [utp](https://github.com/anacrolix/utp) [![GitHub stars](https://img.shields.io/github/stars/anacrolix/utp?style=flat)](https://github.com/anacrolix/utp/stargazers) - Go uTP micro transport protocol implementation.
- [vssh](https://github.com/yahoo/vssh) [![GitHub stars](https://img.shields.io/github/stars/yahoo/vssh?style=flat)](https://github.com/yahoo/vssh/stargazers) - Go library for building network and server automation over SSH protocol.
- [water](https://github.com/songgao/water) [![GitHub stars](https://img.shields.io/github/stars/songgao/water?style=flat)](https://github.com/songgao/water/stargazers) - Simple TUN/TAP library.
- [webrtc](https://github.com/pions/webrtc) [![GitHub stars](https://img.shields.io/github/stars/pions/webrtc?style=flat)](https://github.com/pions/webrtc/stargazers) - A pure Go implementation of the WebRTC API.
- [winrm](https://github.com/masterzen/winrm) [![GitHub stars](https://img.shields.io/github/stars/masterzen/winrm?style=flat)](https://github.com/masterzen/winrm/stargazers) - Go WinRM client to remotely execute commands on Windows machines.
- [xtcp](https://github.com/xfxdev/xtcp) [![GitHub stars](https://img.shields.io/github/stars/xfxdev/xtcp?style=flat)](https://github.com/xfxdev/xtcp/stargazers) - TCP Server Framework with simultaneous full duplex communication, graceful shutdown, and custom protocol.

**[⬆ back to top](#contents)**

### HTTP Clients

_Libraries for making HTTP requests._

- [axios4go](https://github.com/rezmoss/axios4go) [![GitHub stars](https://img.shields.io/github/stars/rezmoss/axios4go?style=flat)](https://github.com/rezmoss/axios4go/stargazers) - A Go HTTP client library inspired by Axios, providing a simple and intuitive API for making HTTP requests.
- [azuretls-client](https://github.com/Noooste/azuretls-client) [![GitHub stars](https://img.shields.io/github/stars/Noooste/azuretls-client?style=flat)](https://github.com/Noooste/azuretls-client/stargazers) - An easy-to-use HTTP client 100% in Go to spoof TLS/JA3 and HTTP2 fingerprint.
- [fast-shot](https://github.com/opus-domini/fast-shot) [![GitHub stars](https://img.shields.io/github/stars/opus-domini/fast-shot?style=flat)](https://github.com/opus-domini/fast-shot/stargazers) - Hit your API targets with rapid-fire precision using Go's fastest and simple HTTP Client.
- [gentleman](https://github.com/h2non/gentleman) [![GitHub stars](https://img.shields.io/github/stars/h2non/gentleman?style=flat)](https://github.com/h2non/gentleman/stargazers) - Full-featured plugin-driven HTTP client library.
- [go-cleanhttp](https://github.com/hashicorp/go-cleanhttp) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/go-cleanhttp?style=flat)](https://github.com/hashicorp/go-cleanhttp/stargazers) - Get easily stdlib HTTP client, which does not share any state with other clients.
- [go-http-client](https://github.com/bozd4g/go-http-client) [![GitHub stars](https://img.shields.io/github/stars/bozd4g/go-http-client?style=flat)](https://github.com/bozd4g/go-http-client/stargazers) - Make http calls simply and easily.
- [go-ipmux](https://github.com/optimus-hft/go-ipmux) [![GitHub stars](https://img.shields.io/github/stars/optimus-hft/go-ipmux?style=flat)](https://github.com/optimus-hft/go-ipmux/stargazers) - A library for Multiplexing HTTP requests based on multiple Source IPs.
- [go-otelroundtripper](https://github.com/NdoleStudio/go-otelroundtripper) [![GitHub stars](https://img.shields.io/github/stars/NdoleStudio/go-otelroundtripper?style=flat)](https://github.com/NdoleStudio/go-otelroundtripper/stargazers) - Go http.RoundTripper that emits open telemetry metrics for HTTP requests.
- [go-req](https://github.com/wenerme/go-req) [![GitHub stars](https://img.shields.io/github/stars/wenerme/go-req?style=flat)](https://github.com/wenerme/go-req/stargazers) - Declarative golang HTTP client.
- [go-retryablehttp](https://github.com/hashicorp/go-retryablehttp) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/go-retryablehttp?style=flat)](https://github.com/hashicorp/go-retryablehttp/stargazers) - Retryable HTTP client in Go.
- [go-zoox/fetch](https://github.com/go-zoox/fetch) [![GitHub stars](https://img.shields.io/github/stars/go-zoox/fetch?style=flat)](https://github.com/go-zoox/fetch/stargazers) - A Powerful, Lightweight, Easy Http Client, inspired by Web Fetch API.
- [Grequest](https://github.com/lib4u/grequest) [![GitHub stars](https://img.shields.io/github/stars/lib4u/grequest?style=flat)](https://github.com/lib4u/grequest/stargazers)  - Simple and lightweight golang package for http requests. based on powerful net/http
- [grequests](https://github.com/levigross/grequests) [![GitHub stars](https://img.shields.io/github/stars/levigross/grequests?style=flat)](https://github.com/levigross/grequests/stargazers) - A Go "clone" of the great and famous Requests library.
- [hedge](https://github.com/bhope/hedge) [![GitHub stars](https://img.shields.io/github/stars/bhope/hedge?style=flat)](https://github.com/bhope/hedge/stargazers) - Adaptive hedged requests for Go. Cuts p99 latency with zero configuration, based on Google's "The Tail at Scale" paper.
- [heimdall](https://github.com/gojektech/heimdall) [![GitHub stars](https://img.shields.io/github/stars/gojektech/heimdall?style=flat)](https://github.com/gojektech/heimdall/stargazers) - An enhanced http client with retry and hystrix capabilities.
- [httpretry](https://github.com/ybbus/httpretry) [![GitHub stars](https://img.shields.io/github/stars/ybbus/httpretry?style=flat)](https://github.com/ybbus/httpretry/stargazers) - Enriches the default go HTTP client with retry functionality.
- [pester](https://github.com/sethgrid/pester) [![GitHub stars](https://img.shields.io/github/stars/sethgrid/pester?style=flat)](https://github.com/sethgrid/pester/stargazers) - Go HTTP client calls with retries, backoff, and concurrency.
- [req](https://github.com/imroc/req) [![GitHub stars](https://img.shields.io/github/stars/imroc/req?style=flat)](https://github.com/imroc/req/stargazers) - Simple Go HTTP client with Black Magic (Less code and More efficiency).
- [request](https://github.com/monaco-io/request) [![GitHub stars](https://img.shields.io/github/stars/monaco-io/request?style=flat)](https://github.com/monaco-io/request/stargazers) - HTTP client for golang. If you have experience about axios or requests, you will love it. No 3rd dependency.
- [requests](https://github.com/carlmjohnson/requests) [![GitHub stars](https://img.shields.io/github/stars/carlmjohnson/requests?style=flat)](https://github.com/carlmjohnson/requests/stargazers) - HTTP requests for Gophers. Uses context.Context and doesn't hide the underlying net/http.Client, making it compatible with standard Go APIs. Also includes testing tools.
- [resty](https://github.com/go-resty/resty) [![GitHub stars](https://img.shields.io/github/stars/go-resty/resty?style=flat)](https://github.com/go-resty/resty/stargazers) - Simple HTTP and REST client for Go inspired by Ruby rest-client.
- [rq](https://github.com/ddo/rq) [![GitHub stars](https://img.shields.io/github/stars/ddo/rq?style=flat)](https://github.com/ddo/rq/stargazers) - A nicer interface for golang stdlib HTTP client.
- [sling](https://github.com/dghubble/sling) [![GitHub stars](https://img.shields.io/github/stars/dghubble/sling?style=flat)](https://github.com/dghubble/sling/stargazers) - Sling is a Go HTTP client library for creating and sending API requests.
- [surf](https://github.com/enetx/surf) [![GitHub stars](https://img.shields.io/github/stars/enetx/surf?style=flat)](https://github.com/enetx/surf/stargazers) - Advanced HTTP client with HTTP/1.1, HTTP/2, HTTP/3 (QUIC), SOCKS5 proxy support and browser-grade TLS fingerprinting.
- [tls-client](https://github.com/bogdanfinn/tls-client) [![GitHub stars](https://img.shields.io/github/stars/bogdanfinn/tls-client?style=flat)](https://github.com/bogdanfinn/tls-client/stargazers) - net/http.Client like HTTP Client with options to select specific client TLS Fingerprints to use for requests.

**[⬆ back to top](#contents)**

## OpenGL

_Libraries for using OpenGL in Go._

- [gl](https://github.com/go-gl/gl) [![GitHub stars](https://img.shields.io/github/stars/go-gl/gl?style=flat)](https://github.com/go-gl/gl/stargazers) - Go bindings for OpenGL (generated via glow).
- [glfw](https://github.com/go-gl/glfw) [![GitHub stars](https://img.shields.io/github/stars/go-gl/glfw?style=flat)](https://github.com/go-gl/glfw/stargazers) - Go bindings for GLFW 3.
- [go-glmatrix](https://github.com/technohippy/go-glmatrix) [![GitHub stars](https://img.shields.io/github/stars/technohippy/go-glmatrix?style=flat)](https://github.com/technohippy/go-glmatrix/stargazers) - Go port of [glMatrix](https://glmatrix.net/) library.
- [goxjs/gl](https://github.com/goxjs/gl) [![GitHub stars](https://img.shields.io/github/stars/goxjs/gl?style=flat)](https://github.com/goxjs/gl/stargazers) - Go cross-platform OpenGL bindings (OS X, Linux, Windows, browsers, iOS, Android).
- [goxjs/glfw](https://github.com/goxjs/glfw) [![GitHub stars](https://img.shields.io/github/stars/goxjs/glfw?style=flat)](https://github.com/goxjs/glfw/stargazers) - Go cross-platform glfw library for creating an OpenGL context and receiving events.
- [mathgl](https://github.com/go-gl/mathgl) [![GitHub stars](https://img.shields.io/github/stars/go-gl/mathgl?style=flat)](https://github.com/go-gl/mathgl/stargazers) - Pure Go math package specialized for 3D math, with inspiration from GLM.

**[⬆ back to top](#contents)**

## ORM

_Libraries that implement Object-Relational Mapping or datamapping techniques._

- [bob](https://github.com/stephenafamo/bob) [![GitHub stars](https://img.shields.io/github/stars/stephenafamo/bob?style=flat)](https://github.com/stephenafamo/bob/stargazers) - SQL query builder and ORM/Factory generator for Go. Successor of SQLBoiler.
- [bun](https://github.com/uptrace/bun) [![GitHub stars](https://img.shields.io/github/stars/uptrace/bun?style=flat)](https://github.com/uptrace/bun/stargazers) - SQL-first Golang ORM. Successor of go-pg.
- [cacheme](https://github.com/Yiling-J/cacheme-go) [![GitHub stars](https://img.shields.io/github/stars/Yiling-J/cacheme-go?style=flat)](https://github.com/Yiling-J/cacheme-go/stargazers) - Schema based, typed Redis caching/memoize framework for Go.
- [CQL](https://github.com/FrancoLiberali/cql) [![GitHub stars](https://img.shields.io/github/stars/FrancoLiberali/cql?style=flat)](https://github.com/FrancoLiberali/cql/stargazers) - Built on top of GORM, adds compile-time verified queries based on auto-generated code.
- [ent](https://github.com/facebook/ent) [![GitHub stars](https://img.shields.io/github/stars/facebook/ent?style=flat)](https://github.com/facebook/ent/stargazers) - An entity framework for Go. Simple, yet powerful ORM for modeling and querying data.
- [go-dbw](https://github.com/hashicorp/go-dbw) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/go-dbw?style=flat)](https://github.com/hashicorp/go-dbw/stargazers) - A simple package that encapsulates database operations.
- [go-firestorm](https://github.com/jschoedt/go-firestorm) [![GitHub stars](https://img.shields.io/github/stars/jschoedt/go-firestorm?style=flat)](https://github.com/jschoedt/go-firestorm/stargazers) - A simple ORM for Google/Firebase Cloud Firestore.
- [go-sql](https://github.com/rushteam/gosql) [![GitHub stars](https://img.shields.io/github/stars/rushteam/gosql?style=flat)](https://github.com/rushteam/gosql/stargazers) - A easy ORM for mysql.
- [go-sqlbuilder](https://github.com/huandu/go-sqlbuilder) [![GitHub stars](https://img.shields.io/github/stars/huandu/go-sqlbuilder?style=flat)](https://github.com/huandu/go-sqlbuilder/stargazers) - A flexible and powerful SQL string builder library plus a zero-config ORM.
- [go-store](https://github.com/gosuri/go-store) [![GitHub stars](https://img.shields.io/github/stars/gosuri/go-store?style=flat)](https://github.com/gosuri/go-store/stargazers) - Simple and fast Redis backed key-value store library for Go.
- [golobby/orm](https://github.com/golobby/orm) [![GitHub stars](https://img.shields.io/github/stars/golobby/orm?style=flat)](https://github.com/golobby/orm/stargazers) - Simple, fast, type-safe, generic orm for developer happiness.
- [GORM](https://github.com/go-gorm/gorm) [![GitHub stars](https://img.shields.io/github/stars/go-gorm/gorm?style=flat)](https://github.com/go-gorm/gorm/stargazers) - The fantastic ORM library for Golang, aims to be developer friendly.
- [gormt](https://github.com/xxjwxc/gormt) [![GitHub stars](https://img.shields.io/github/stars/xxjwxc/gormt?style=flat)](https://github.com/xxjwxc/gormt/stargazers) - Mysql database to golang gorm struct.
- [gorp](https://github.com/go-gorp/gorp) [![GitHub stars](https://img.shields.io/github/stars/go-gorp/gorp?style=flat)](https://github.com/go-gorp/gorp/stargazers) - Go Relational Persistence, ORM-ish library for Go.
- [grimoire](https://github.com/Fs02/grimoire) [![GitHub stars](https://img.shields.io/github/stars/Fs02/grimoire?style=flat)](https://github.com/Fs02/grimoire/stargazers) - Grimoire is a database access layer and validation for golang. (Support: MySQL, PostgreSQL and SQLite3).
- [lore](https://github.com/abrahambotros/lore) [![GitHub stars](https://img.shields.io/github/stars/abrahambotros/lore?style=flat)](https://github.com/abrahambotros/lore/stargazers) - Simple and lightweight pseudo-ORM/pseudo-struct-mapping environment for Go.
- [marlow](https://github.com/marlow/marlow) [![GitHub stars](https://img.shields.io/github/stars/marlow/marlow?style=flat)](https://github.com/marlow/marlow/stargazers) - Generated ORM from project structs for compile time safety assurances.
- [pop/soda](https://github.com/gobuffalo/pop) [![GitHub stars](https://img.shields.io/github/stars/gobuffalo/pop?style=flat)](https://github.com/gobuffalo/pop/stargazers) - Database migration, creation, ORM, etc... for MySQL, PostgreSQL, and SQLite.
- [Prisma](https://github.com/prisma/prisma-client-go) [![GitHub stars](https://img.shields.io/github/stars/prisma/prisma-client-go?style=flat)](https://github.com/prisma/prisma-client-go/stargazers) - Prisma Client Go, Typesafe database access for Go.
- [reform](https://github.com/go-reform/reform) [![GitHub stars](https://img.shields.io/github/stars/go-reform/reform?style=flat)](https://github.com/go-reform/reform/stargazers) - Better ORM for Go, based on non-empty interfaces and code generation.
- [rel](https://github.com/go-rel/rel) [![GitHub stars](https://img.shields.io/github/stars/go-rel/rel?style=flat)](https://github.com/go-rel/rel/stargazers) - Modern Database Access Layer for Golang - Testable, Extendable and Crafted Into a Clean and Elegant API.
- [SQLBoiler](https://github.com/volatiletech/sqlboiler) [![GitHub stars](https://img.shields.io/github/stars/volatiletech/sqlboiler?style=flat)](https://github.com/volatiletech/sqlboiler/stargazers) - ORM generator. Generate a featureful and blazing-fast ORM tailored to your database schema.
- [upper.io/db](https://github.com/upper/db) [![GitHub stars](https://img.shields.io/github/stars/upper/db?style=flat)](https://github.com/upper/db/stargazers) - Single interface for interacting with different data sources through the use of adapters that wrap mature database drivers.
- [XORM](https://gitea.com/xorm/xorm) - Simple and powerful ORM for Go. (Support: MySQL, MyMysql, PostgreSQL, Tidb, SQLite3, MsSql and Oracle).
- [Zoom](https://github.com/albrow/zoom) [![GitHub stars](https://img.shields.io/github/stars/albrow/zoom?style=flat)](https://github.com/albrow/zoom/stargazers) - Blazing-fast datastore and querying engine built on Redis.

**[⬆ back to top](#contents)**

## Package Management

_Official tooling for dependency and package management_

- [go modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) - Modules are the unit of source code interchange and versioning. The go command has direct support for working with modules, including recording and resolving dependencies on other modules.

_Unofficial libraries for package and dependency management._

- [gup](https://github.com/nao1215/gup) [![GitHub stars](https://img.shields.io/github/stars/nao1215/gup?style=flat)](https://github.com/nao1215/gup/stargazers) - Update binaries installed by "go install".
- [modup](https://github.com/chaindead/modup) [![GitHub stars](https://img.shields.io/github/stars/chaindead/modup?style=flat)](https://github.com/chaindead/modup/stargazers) - Terminal UI for Go dependency updates with outdated module detection and selective upgrading.
- [syft](https://github.com/anchore/syft) [![GitHub stars](https://img.shields.io/github/stars/anchore/syft?style=flat)](https://github.com/anchore/syft/stargazers) - A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems.

**[⬆ back to top](#contents)**

## Performance

- [ebpf-go](https://github.com/cilium/ebpf) [![GitHub stars](https://img.shields.io/github/stars/cilium/ebpf?style=flat)](https://github.com/cilium/ebpf/stargazers) - Provides utilities for loading, compiling, and debugging eBPF programs.
- [go-instrument](https://github.com/nikolaydubina/go-instrument) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/go-instrument?style=flat)](https://github.com/nikolaydubina/go-instrument/stargazers) - Automatically add spans to all methods and functions.
- [go-perfstat](https://github.com/go-perfstat/go) [![GitHub stars](https://img.shields.io/github/stars/go-perfstat/go?style=flat)](https://github.com/go-perfstat/go/stargazers) - Lightweight performance statistics and execution time aggregation for Go.
- [jaeger](https://github.com/jaegertracing/jaeger) [![GitHub stars](https://img.shields.io/github/stars/jaegertracing/jaeger?style=flat)](https://github.com/jaegertracing/jaeger/stargazers) - A distributed tracing system.
- [mm-go](https://github.com/joetifa2003/mm-go) [![GitHub stars](https://img.shields.io/github/stars/joetifa2003/mm-go?style=flat)](https://github.com/joetifa2003/mm-go/stargazers) - Generic manual memory management for golang.
- [otelinji](https://github.com/hedhyw/otelinji) [![GitHub stars](https://img.shields.io/github/stars/hedhyw/otelinji?style=flat)](https://github.com/hedhyw/otelinji/stargazers) - OpenTelemetry auto-instrumentation tool for adding spans to functions.
- [pixie](https://github.com/pixie-labs/pixie) [![GitHub stars](https://img.shields.io/github/stars/pixie-labs/pixie?style=flat)](https://github.com/pixie-labs/pixie/stargazers) - No instrumentation tracing for Golang applications via eBPF.
- [profile](https://github.com/pkg/profile) [![GitHub stars](https://img.shields.io/github/stars/pkg/profile?style=flat)](https://github.com/pkg/profile/stargazers) - Simple profiling support package for Go.
- [statsviz](https://github.com/arl/statsviz) [![GitHub stars](https://img.shields.io/github/stars/arl/statsviz?style=flat)](https://github.com/arl/statsviz/stargazers) - Live visualization of your Go application runtime statistics.
- [tracer](https://github.com/kamilsk/tracer) [![GitHub stars](https://img.shields.io/github/stars/kamilsk/tracer?style=flat)](https://github.com/kamilsk/tracer/stargazers) - Simple, lightweight tracing.

**[⬆ back to top](#contents)**

## Query Language

- [api-fu](https://github.com/ccbrown/api-fu) [![GitHub stars](https://img.shields.io/github/stars/ccbrown/api-fu?style=flat)](https://github.com/ccbrown/api-fu/stargazers) - Comprehensive GraphQL implementation.
- [dasel](https://github.com/tomwright/dasel) [![GitHub stars](https://img.shields.io/github/stars/tomwright/dasel?style=flat)](https://github.com/tomwright/dasel/stargazers) - Query and update data structures using selectors from the command line. Comparable to jq/yq but supports JSON, YAML, TOML and XML with zero runtime dependencies.
- [gojsonq](https://github.com/thedevsaddam/gojsonq) [![GitHub stars](https://img.shields.io/github/stars/thedevsaddam/gojsonq?style=flat)](https://github.com/thedevsaddam/gojsonq/stargazers) - A simple Go package to Query over JSON Data.
- [goven](https://github.com/SeldonIO/goven) [![GitHub stars](https://img.shields.io/github/stars/SeldonIO/goven?style=flat)](https://github.com/SeldonIO/goven/stargazers) - A drop-in query language for any database schema.
- [gqlgen](https://github.com/99designs/gqlgen) [![GitHub stars](https://img.shields.io/github/stars/99designs/gqlgen?style=flat)](https://github.com/99designs/gqlgen/stargazers) - go generate based graphql server library.
- [grapher](https://github.com/reaganiwadha/grapher) [![GitHub stars](https://img.shields.io/github/stars/reaganiwadha/grapher?style=flat)](https://github.com/reaganiwadha/grapher/stargazers) - A GraphQL field builder utilizing Go generics with extra utilities and features.
- [graphql](https://github.com/neelance/graphql-go) [![GitHub stars](https://img.shields.io/github/stars/neelance/graphql-go?style=flat)](https://github.com/neelance/graphql-go/stargazers) - GraphQL server with a focus on ease of use.
- [graphql-go](https://github.com/graphql-go/graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-go/graphql?style=flat)](https://github.com/graphql-go/graphql/stargazers) - Implementation of GraphQL for Go.
- [gws](https://github.com/Zaba505/gws) [![GitHub stars](https://img.shields.io/github/stars/Zaba505/gws?style=flat)](https://github.com/Zaba505/gws/stargazers) - Apollos' "GraphQL over Websocket" client and server implementation.
- [jsonpath](https://github.com/AsaiYusuke/jsonpath) [![GitHub stars](https://img.shields.io/github/stars/AsaiYusuke/jsonpath?style=flat)](https://github.com/AsaiYusuke/jsonpath/stargazers) - A query library for retrieving part of JSON based on JSONPath syntax.
- [jsonql](https://github.com/elgs/jsonql) [![GitHub stars](https://img.shields.io/github/stars/elgs/jsonql?style=flat)](https://github.com/elgs/jsonql/stargazers) - JSON query expression library in Golang.
- [jsonslice](https://github.com/bhmj/jsonslice) [![GitHub stars](https://img.shields.io/github/stars/bhmj/jsonslice?style=flat)](https://github.com/bhmj/jsonslice/stargazers) - Jsonpath queries with advanced filters.
- [mql](https://github.com/hashicorp/mql) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/mql?style=flat)](https://github.com/hashicorp/mql/stargazers) - Model Query Language (mql) is a query language for your database models.
- [play](https://github.com/paololazzari/play) [![GitHub stars](https://img.shields.io/github/stars/paololazzari/play?style=flat)](https://github.com/paololazzari/play/stargazers) - A TUI playground to experiment with your favorite programs, such as grep, sed, awk, jq and yq.
- [rql](https://github.com/a8m/rql) [![GitHub stars](https://img.shields.io/github/stars/a8m/rql?style=flat)](https://github.com/a8m/rql/stargazers) - Resource Query Language for REST API.
- [rqp](https://github.com/timsolov/rest-query-parser) [![GitHub stars](https://img.shields.io/github/stars/timsolov/rest-query-parser?style=flat)](https://github.com/timsolov/rest-query-parser/stargazers) - Query Parser for REST API. Filtering, validations, both `AND`, `OR` operations are supported directly in the query.
- [straf](https://github.com/SonicRoshan/straf) [![GitHub stars](https://img.shields.io/github/stars/SonicRoshan/straf?style=flat)](https://github.com/SonicRoshan/straf/stargazers) - Easily Convert Golang structs to GraphQL objects.

**[⬆ back to top](#contents)**

## Reflection

- [copy](https://github.com/gotidy/copy) [![GitHub stars](https://img.shields.io/github/stars/gotidy/copy?style=flat)](https://github.com/gotidy/copy/stargazers) - Package for fast copying structs of different types.
- [Deepcopier](https://github.com/ulule/deepcopier) [![GitHub stars](https://img.shields.io/github/stars/ulule/deepcopier?style=flat)](https://github.com/ulule/deepcopier/stargazers) - Simple struct copying for Go.
- [go-deepcopy](https://github.com/tiendc/go-deepcopy) [![GitHub stars](https://img.shields.io/github/stars/tiendc/go-deepcopy?style=flat)](https://github.com/tiendc/go-deepcopy/stargazers) - Fast deep copy library.
- [goenum](https://github.com/lvyahui8/goenum) [![GitHub stars](https://img.shields.io/github/stars/lvyahui8/goenum?style=flat)](https://github.com/lvyahui8/goenum/stargazers) - A common enumeration struct based on generics and reflection that allows you to quickly define enumerations and use a set of useful default methods.
- [gotype](https://github.com/wzshiming/gotype) [![GitHub stars](https://img.shields.io/github/stars/wzshiming/gotype?style=flat)](https://github.com/wzshiming/gotype/stargazers) - Golang source code parsing, usage like reflect package.
- [gpath](https://github.com/tenntenn/gpath) [![GitHub stars](https://img.shields.io/github/stars/tenntenn/gpath?style=flat)](https://github.com/tenntenn/gpath/stargazers) - Library to simplify access struct fields with Go's expression in reflection.
- [objwalker](https://github.com/rekby/objwalker) [![GitHub stars](https://img.shields.io/github/stars/rekby/objwalker?style=flat)](https://github.com/rekby/objwalker/stargazers) - Walk by go objects with reflection.
- [reflectpro](https://github.com/gontainer/reflectpro) [![GitHub stars](https://img.shields.io/github/stars/gontainer/reflectpro?style=flat)](https://github.com/gontainer/reflectpro/stargazers) - Callers, copiers, getters and setters for go.
- [reflectutils](https://github.com/muir/reflectutils) [![GitHub stars](https://img.shields.io/github/stars/muir/reflectutils?style=flat)](https://github.com/muir/reflectutils/stargazers) - Helpers for working with reflection: struct tag parsing; recursive walking; fill value from string.

**[⬆ back to top](#contents)**

## Resource Embedding

- [debme](https://github.com/leaanthony/debme) [![GitHub stars](https://img.shields.io/github/stars/leaanthony/debme?style=flat)](https://github.com/leaanthony/debme/stargazers) - Create an `embed.FS` from an existing `embed.FS` subdirectory.
- [embed](https://pkg.go.dev/embed) - Package embed provides access to files embedded in the running Go program.
- [rebed](https://github.com/soypat/rebed) [![GitHub stars](https://img.shields.io/github/stars/soypat/rebed?style=flat)](https://github.com/soypat/rebed/stargazers) - Recreate folder structures and files from Go 1.16's `embed.FS` type
- [vfsgen](https://github.com/shurcooL/vfsgen) [![GitHub stars](https://img.shields.io/github/stars/shurcooL/vfsgen?style=flat)](https://github.com/shurcooL/vfsgen/stargazers) - Generates a vfsdata.go file that statically implements the given virtual filesystem.

**[⬆ back to top](#contents)**

## Science and Data Analysis

_Libraries for scientific computing and data analyzing._

- [bradleyterry](https://github.com/seanhagen/bradleyterry) [![GitHub stars](https://img.shields.io/github/stars/seanhagen/bradleyterry?style=flat)](https://github.com/seanhagen/bradleyterry/stargazers) - Provides a Bradley-Terry Model for pairwise comparisons.
- [calendarheatmap](https://github.com/nikolaydubina/calendarheatmap) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/calendarheatmap?style=flat)](https://github.com/nikolaydubina/calendarheatmap/stargazers) - Calendar heatmap in plain Go inspired by Github contribution activity.
- [chart](https://github.com/vdobler/chart) [![GitHub stars](https://img.shields.io/github/stars/vdobler/chart?style=flat)](https://github.com/vdobler/chart/stargazers) - Simple Chart Plotting library for Go. Supports many graphs types.
- [dataframe-go](https://github.com/rocketlaunchr/dataframe-go) [![GitHub stars](https://img.shields.io/github/stars/rocketlaunchr/dataframe-go?style=flat)](https://github.com/rocketlaunchr/dataframe-go/stargazers) - Dataframes for machine-learning and statistics (similar to pandas).
- [decimal](https://github.com/db47h/decimal) [![GitHub stars](https://img.shields.io/github/stars/db47h/decimal?style=flat)](https://github.com/db47h/decimal/stargazers) - Package decimal implements arbitrary-precision decimal floating-point arithmetic.
- [entitydebs](https://github.com/ndabAP/entitydebs) [![GitHub stars](https://img.shields.io/github/stars/ndabAP/entitydebs?style=flat)](https://github.com/ndabAP/entitydebs/stargazers) - A social science tool to programmatically analyze entities in non-fictional texts with a built-in dependency parser.
- [evaler](https://github.com/soniah/evaler) [![GitHub stars](https://img.shields.io/github/stars/soniah/evaler?style=flat)](https://github.com/soniah/evaler/stargazers) - Simple floating point arithmetic expression evaluator.
- [ewma](https://github.com/VividCortex/ewma) [![GitHub stars](https://img.shields.io/github/stars/VividCortex/ewma?style=flat)](https://github.com/VividCortex/ewma/stargazers) - Exponentially-weighted moving averages.
- [geom](https://github.com/skelterjohn/geom) [![GitHub stars](https://img.shields.io/github/stars/skelterjohn/geom?style=flat)](https://github.com/skelterjohn/geom/stargazers) - 2D geometry for golang.
- [go-dsp](https://github.com/mjibson/go-dsp) [![GitHub stars](https://img.shields.io/github/stars/mjibson/go-dsp?style=flat)](https://github.com/mjibson/go-dsp/stargazers) - Digital Signal Processing for Go.
- [go-estimate](https://github.com/milosgajdos/go-estimate) [![GitHub stars](https://img.shields.io/github/stars/milosgajdos/go-estimate?style=flat)](https://github.com/milosgajdos/go-estimate/stargazers) - State estimation and filtering algorithms in Go.
- [go-gt](https://github.com/ThePaw/go-gt) [![GitHub stars](https://img.shields.io/github/stars/ThePaw/go-gt?style=flat)](https://github.com/ThePaw/go-gt/stargazers) - Graph theory algorithms written in "Go" language.
- [go-hep](https://github.com/go-hep/hep) [![GitHub stars](https://img.shields.io/github/stars/go-hep/hep?style=flat)](https://github.com/go-hep/hep/stargazers) - A set of libraries and tools for performing High Energy Physics analyses with ease.
- [godesim](https://github.com/soypat/godesim) [![GitHub stars](https://img.shields.io/github/stars/soypat/godesim?style=flat)](https://github.com/soypat/godesim/stargazers) - Extended/multivariable ODE solver framework for event-based simulations with simple API.
- [goent](https://github.com/kzahedi/goent) [![GitHub stars](https://img.shields.io/github/stars/kzahedi/goent?style=flat)](https://github.com/kzahedi/goent/stargazers) - GO Implementation of Entropy Measures.
- [gograph](https://github.com/hmdsefi/gograph) [![GitHub stars](https://img.shields.io/github/stars/hmdsefi/gograph?style=flat)](https://github.com/hmdsefi/gograph/stargazers) - A golang generic graph library that provides mathematical graph-theory and algorithms.
- [gonum](https://github.com/gonum/gonum) [![GitHub stars](https://img.shields.io/github/stars/gonum/gonum?style=flat)](https://github.com/gonum/gonum/stargazers) - Gonum is a set of numeric libraries for the Go programming language. It contains libraries for matrices, statistics, optimization, and more.
- [gonum/plot](https://github.com/gonum/plot) [![GitHub stars](https://img.shields.io/github/stars/gonum/plot?style=flat)](https://github.com/gonum/plot/stargazers) - gonum/plot provides an API for building and drawing plots in Go.
- [goraph](https://github.com/gyuho/goraph) [![GitHub stars](https://img.shields.io/github/stars/gyuho/goraph?style=flat)](https://github.com/gyuho/goraph/stargazers) - Pure Go graph theory library(data structure, algorithm visualization).
- [gosl](https://github.com/cpmech/gosl) [![GitHub stars](https://img.shields.io/github/stars/cpmech/gosl?style=flat)](https://github.com/cpmech/gosl/stargazers) - Go scientific library for linear algebra, FFT, geometry, NURBS, numerical methods, probabilities, optimisation, differential equations, and more.
- [GoStats](https://github.com/OGFris/GoStats) [![GitHub stars](https://img.shields.io/github/stars/OGFris/GoStats?style=flat)](https://github.com/OGFris/GoStats/stargazers) - GoStats is an Open Source GoLang library for math statistics mostly used in Machine Learning domains, it covers most of the Statistical measures functions.
- [graph](https://github.com/yourbasic/graph) [![GitHub stars](https://img.shields.io/github/stars/yourbasic/graph?style=flat)](https://github.com/yourbasic/graph/stargazers) - Library of basic graph algorithms.
- [hdf5](https://github.com/scigolib/hdf5) [![GitHub stars](https://img.shields.io/github/stars/scigolib/hdf5?style=flat)](https://github.com/scigolib/hdf5/stargazers) - Pure Go implementation of the HDF5 file format for scientific data storage and exchange.
- [insyra](https://github.com/HazelnutParadise/insyra) [![GitHub stars](https://img.shields.io/github/stars/HazelnutParadise/insyra?style=flat)](https://github.com/HazelnutParadise/insyra/stargazers) - Data analysis library with statistics, visualization, Parquet support, and Python integration.
- [jsonl-graph](https://github.com/nikolaydubina/jsonl-graph) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/jsonl-graph?style=flat)](https://github.com/nikolaydubina/jsonl-graph/stargazers) - Tool to manipulate JSONL graphs with graphviz support.
- [matlab](https://github.com/scigolib/matlab) [![GitHub stars](https://img.shields.io/github/stars/scigolib/matlab?style=flat)](https://github.com/scigolib/matlab/stargazers) - Pure Go library for reading and writing MATLAB .mat files (v5-v7.3) without CGO.
- [MatProInterface.go](https://github.com/MatProGo-dev/MatProInterface.go) [![GitHub stars](https://img.shields.io/github/stars/MatProGo-dev/MatProInterface.go?style=flat)](https://github.com/MatProGo-dev/MatProInterface.go/stargazers) - MatProInterface.go is an open source package for defining mathematical programs (e.g., convex optimization problems) in Go.
- [matrix](https://github.com/Arceus-7/matrix) [![GitHub stars](https://img.shields.io/github/stars/Arceus-7/matrix?style=flat)](https://github.com/Arceus-7/matrix/stargazers) - A clean, generic, zero-dependency matrix math package for Go with support for arithmetic, decompositions, and linear system solving.
- [ode](https://github.com/ChristopherRabotin/ode) [![GitHub stars](https://img.shields.io/github/stars/ChristopherRabotin/ode?style=flat)](https://github.com/ChristopherRabotin/ode/stargazers) - Ordinary differential equation (ODE) solver which supports extended states and channel-based iteration stop conditions.
- [orb](https://github.com/paulmach/orb) [![GitHub stars](https://img.shields.io/github/stars/paulmach/orb?style=flat)](https://github.com/paulmach/orb/stargazers) - 2D geometry types with clipping, GeoJSON and Mapbox Vector Tile support.
- [pagerank](https://github.com/alixaxel/pagerank) [![GitHub stars](https://img.shields.io/github/stars/alixaxel/pagerank?style=flat)](https://github.com/alixaxel/pagerank/stargazers) - Weighted PageRank algorithm implemented in Go.
- [piecewiselinear](https://github.com/sgreben/piecewiselinear) [![GitHub stars](https://img.shields.io/github/stars/sgreben/piecewiselinear?style=flat)](https://github.com/sgreben/piecewiselinear/stargazers) - Tiny linear interpolation library.
- [PiHex](https://github.com/claygod/PiHex) [![GitHub stars](https://img.shields.io/github/stars/claygod/PiHex?style=flat)](https://github.com/claygod/PiHex/stargazers) - Implementation of the "Bailey-Borwein-Plouffe" algorithm for the hexadecimal number Pi.
- [Poly](https://github.com/bebop/poly) [![GitHub stars](https://img.shields.io/github/stars/bebop/poly?style=flat)](https://github.com/bebop/poly/stargazers) - A Go package for engineering organisms.
- [rootfinding](https://github.com/khezen/rootfinding) [![GitHub stars](https://img.shields.io/github/stars/khezen/rootfinding?style=flat)](https://github.com/khezen/rootfinding/stargazers) - root-finding algorithms library for finding roots of quadratic functions.
- [sparse](https://github.com/james-bowman/sparse) [![GitHub stars](https://img.shields.io/github/stars/james-bowman/sparse?style=flat)](https://github.com/james-bowman/sparse/stargazers) - Go Sparse matrix formats for linear algebra supporting scientific and machine learning applications, compatible with gonum matrix libraries.
- [stats](https://github.com/montanaflynn/stats) [![GitHub stars](https://img.shields.io/github/stars/montanaflynn/stats?style=flat)](https://github.com/montanaflynn/stats/stargazers) - Statistics package with common functions missing from the Golang standard library.
- [streamtools](https://github.com/nytlabs/streamtools) [![GitHub stars](https://img.shields.io/github/stars/nytlabs/streamtools?style=flat)](https://github.com/nytlabs/streamtools/stargazers) - general purpose, graphical tool for dealing with streams of data.
- [taxonkit](https://github.com/shenwei356/taxonkit) [![GitHub stars](https://img.shields.io/github/stars/shenwei356/taxonkit?style=flat)](https://github.com/shenwei356/taxonkit/stargazers) - A practical and efficient NCBI taxonomy toolkit; supports querying lineage, reformatting, filtering, and creating custom taxdump files.
- [TextRank](https://github.com/DavidBelicza/TextRank) [![GitHub stars](https://img.shields.io/github/stars/DavidBelicza/TextRank?style=flat)](https://github.com/DavidBelicza/TextRank/stargazers) - TextRank implementation in Golang with extendable features (summarization, weighting, phrase extraction) and multithreading (goroutine) support.
- [topk](https://github.com/keilerkonzept/topk) [![GitHub stars](https://img.shields.io/github/stars/keilerkonzept/topk?style=flat)](https://github.com/keilerkonzept/topk/stargazers) - Sliding-window and regular top-K sketches, based on the HeavyKeeper algorithm.
- [triangolatte](https://github.com/tchayen/triangolatte) [![GitHub stars](https://img.shields.io/github/stars/tchayen/triangolatte?style=flat)](https://github.com/tchayen/triangolatte/stargazers) - 2D triangulation library. Allows translating lines and polygons (both based on points) to the language of GPUs.

**[⬆ back to top](#contents)**

## Security

_Libraries that are used to help make your application more secure._

- [acmetool](https://github.com/hlandau/acme) [![GitHub stars](https://img.shields.io/github/stars/hlandau/acme?style=flat)](https://github.com/hlandau/acme/stargazers) - ACME (Let's Encrypt) client tool with automatic renewal.
- [acopw-go](https://sr.ht/~jamesponddotco/acopw-go/) - Small cryptographically secure password generator package for Go.
- [acra](https://github.com/cossacklabs/acra) [![GitHub stars](https://img.shields.io/github/stars/cossacklabs/acra?style=flat)](https://github.com/cossacklabs/acra/stargazers) - Network encryption proxy to protect database-based applications from data leaks: strong selective encryption, SQL injections prevention, intrusion detection system.
- [aes-ctr-drbg](https://github.com/sixafter/aes-ctr-drbg) [![GitHub stars](https://img.shields.io/github/stars/sixafter/aes-ctr-drbg?style=flat)](https://github.com/sixafter/aes-ctr-drbg/stargazers) - A Deterministic Random Bit Generator based on AES in Counter mode (AES-CTR-DRBG) as specified in NIST SP 800-90A.
- [age](https://github.com/FiloSottile/age) [![GitHub stars](https://img.shields.io/github/stars/FiloSottile/age?style=flat)](https://github.com/FiloSottile/age/stargazers) - A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability.
- [argon2-hashing](https://github.com/andskur/argon2-hashing) [![GitHub stars](https://img.shields.io/github/stars/andskur/argon2-hashing?style=flat)](https://github.com/andskur/argon2-hashing/stargazers) - light wrapper around Go's argon2 package that closely mirrors with Go's standard library Bcrypt and simple-scrypt package.
- [autocert](https://pkg.go.dev/golang.org/x/crypto/acme/autocert) - Auto provision Let's Encrypt certificates and start a TLS server.
- [BadActor](https://github.com/jaredfolkins/badactor) [![GitHub stars](https://img.shields.io/github/stars/jaredfolkins/badactor?style=flat)](https://github.com/jaredfolkins/badactor/stargazers) - In-memory, application-driven jailer built in the spirit of fail2ban.
- [beelzebub](https://github.com/mariocandela/beelzebub) [![GitHub stars](https://img.shields.io/github/stars/mariocandela/beelzebub?style=flat)](https://github.com/mariocandela/beelzebub/stargazers) - A secure low code honeypot framework, leveraging AI for System Virtualization.
- [booster](https://github.com/anatol/booster) [![GitHub stars](https://img.shields.io/github/stars/anatol/booster?style=flat)](https://github.com/anatol/booster/stargazers) - Fast initramfs generator with full-disk encryption support.
- [Cameradar](https://github.com/Ullaakut/cameradar) [![GitHub stars](https://img.shields.io/github/stars/Ullaakut/cameradar?style=flat)](https://github.com/Ullaakut/cameradar/stargazers) - Tool and library to remotely hack RTSP streams from surveillance cameras.
- [canery](https://github.com/rluders/canery) [![GitHub stars](https://img.shields.io/github/stars/rluders/canery?style=flat)](https://github.com/rluders/canery/stargazers) - Minimal, stateless authorization engine with a pluggable evaluation model.
- [certificates](https://github.com/mvmaasakkers/certificates) [![GitHub stars](https://img.shields.io/github/stars/mvmaasakkers/certificates?style=flat)](https://github.com/mvmaasakkers/certificates/stargazers) - An opinionated tool for generating tls certificates.
- [CertMagic](https://github.com/caddyserver/certmagic) [![GitHub stars](https://img.shields.io/github/stars/caddyserver/certmagic?style=flat)](https://github.com/caddyserver/certmagic/stargazers) - Mature, robust, and powerful ACME client integration for fully-managed TLS certificate issuance and renewal.
- [Coraza](https://github.com/corazawaf/coraza) [![GitHub stars](https://img.shields.io/github/stars/corazawaf/coraza?style=flat)](https://github.com/corazawaf/coraza/stargazers) - Enterprise-ready, modsecurity and OWASP CRS compatible WAF library.
- [dongle](https://github.com/golang-module/dongle) [![GitHub stars](https://img.shields.io/github/stars/golang-module/dongle?style=flat)](https://github.com/golang-module/dongle/stargazers) - A simple, semantic and developer-friendly golang package for encoding&decoding and encryption&decryption.
- [dotlock](https://github.com/ahmadraza100/dotlock) [![GitHub stars](https://img.shields.io/github/stars/ahmadraza100/dotlock?style=flat)](https://github.com/ahmadraza100/dotlock/stargazers) - Encrypted .env vault manager with interactive TUI for managing secrets across multiple environments and profiles.
- [encid](https://github.com/bobg/encid) [![GitHub stars](https://img.shields.io/github/stars/bobg/encid?style=flat)](https://github.com/bobg/encid/stargazers) - Encode and decode encrypted integer IDs.
- [entpassgen](https://github.com/andreimerlescu/entpassgen) [![GitHub stars](https://img.shields.io/github/stars/andreimerlescu/entpassgen?style=flat)](https://github.com/andreimerlescu/entpassgen/stargazers) - Entropy Password Generator with extensive command line arguments to generate random strings securely including digits, passwords, and passwords built using obscure dictionary words mixed with symbols and digits.
- [firewalld-rest](https://github.com/prashantgupta24/firewalld-rest) [![GitHub stars](https://img.shields.io/github/stars/prashantgupta24/firewalld-rest?style=flat)](https://github.com/prashantgupta24/firewalld-rest/stargazers) - A rest application to dynamically update firewalld rules on a linux server.
- [fort](https://github.com/djadmin/fort) [![GitHub stars](https://img.shields.io/github/stars/djadmin/fort?style=flat)](https://github.com/djadmin/fort/stargazers) - Audits macOS security settings across 16 checks, reports a score, and fixes issues where it safely can. Single binary, installable via Homebrew.
- [go-generate-password](https://github.com/m1/go-generate-password) [![GitHub stars](https://img.shields.io/github/stars/m1/go-generate-password?style=flat)](https://github.com/m1/go-generate-password/stargazers) - Password generator that can be used on the cli or as a library.
- [go-htpasswd](https://github.com/tg123/go-htpasswd) [![GitHub stars](https://img.shields.io/github/stars/tg123/go-htpasswd?style=flat)](https://github.com/tg123/go-htpasswd/stargazers) - Apache htpasswd Parser for Go.
- [go-password-validator](https://github.com/lane-c-wagner/go-password-validator) [![GitHub stars](https://img.shields.io/github/stars/lane-c-wagner/go-password-validator?style=flat)](https://github.com/lane-c-wagner/go-password-validator/stargazers) - Password validator based on raw cryptographic entropy values.
- [go-peer](https://github.com/number571/go-peer) [![GitHub stars](https://img.shields.io/github/stars/number571/go-peer?style=flat)](https://github.com/number571/go-peer/stargazers) - A software library for creating secure and anonymous decentralized systems.
- [go-yara](https://github.com/hillu/go-yara) [![GitHub stars](https://img.shields.io/github/stars/hillu/go-yara?style=flat)](https://github.com/hillu/go-yara/stargazers) - Go Bindings for [YARA](https://github.com/plusvic/yara) [![GitHub stars](https://img.shields.io/github/stars/plusvic/yara?style=flat)](https://github.com/plusvic/yara/stargazers), the "pattern matching swiss knife for malware researchers (and everyone else)".
- [goArgonPass](https://github.com/dwin/goArgonPass) [![GitHub stars](https://img.shields.io/github/stars/dwin/goArgonPass?style=flat)](https://github.com/dwin/goArgonPass/stargazers) - Argon2 password hash and verification designed to be compatible with existing Python and PHP implementations.
- [goSecretBoxPassword](https://github.com/dwin/goSecretBoxPassword) [![GitHub stars](https://img.shields.io/github/stars/dwin/goSecretBoxPassword?style=flat)](https://github.com/dwin/goSecretBoxPassword/stargazers) - A probably paranoid package for securely hashing and encrypting passwords.
- [gost-crypto](https://github.com/rekurt/gost-crypto) [![GitHub stars](https://img.shields.io/github/stars/rekurt/gost-crypto?style=flat)](https://github.com/rekurt/gost-crypto/stargazers) - Go library for Russian GOST cryptographic standards (digital signatures, Streebog hash, Kuznechik cipher, MGM AEAD) backed by OpenSSL gost-engine.
- [gspy](https://github.com/Mutasem-mk4/gspy) [![GitHub stars](https://img.shields.io/github/stars/Mutasem-mk4/gspy?style=flat)](https://github.com/Mutasem-mk4/gspy/stargazers) - Forensic goroutine-to-syscall inspector for live Go processes.
- [Interpol](https://github.com/avahidi/interpol) [![GitHub stars](https://img.shields.io/github/stars/avahidi/interpol?style=flat)](https://github.com/avahidi/interpol/stargazers) - Rule-based data generator for fuzzing and penetration testing.
- [leakhound](https://github.com/nilpoona/leakhound) [![GitHub stars](https://img.shields.io/github/stars/nilpoona/leakhound?style=flat)](https://github.com/nilpoona/leakhound/stargazers) - Static analysis tool to detect accidental logging of sensitive struct fields, preventing data leaks in logs.
- [lego](https://github.com/go-acme/lego) [![GitHub stars](https://img.shields.io/github/stars/go-acme/lego?style=flat)](https://github.com/go-acme/lego/stargazers) - Pure Go ACME client library and CLI tool (for use with Let's Encrypt).
- [luks.go](https://github.com/anatol/luks.go) [![GitHub stars](https://img.shields.io/github/stars/anatol/luks.go?style=flat)](https://github.com/anatol/luks.go/stargazers) - Pure Golang library to manage LUKS partitions.
- [memguard](https://github.com/awnumar/memguard) [![GitHub stars](https://img.shields.io/github/stars/awnumar/memguard?style=flat)](https://github.com/awnumar/memguard/stargazers) - A pure Go library for handling sensitive values in memory.
- [multikey](https://github.com/adrianosela/multikey) [![GitHub stars](https://img.shields.io/github/stars/adrianosela/multikey?style=flat)](https://github.com/adrianosela/multikey/stargazers) - An n-out-of-N keys encryption/decryption framework based on Shamir's Secret Sharing algorithm.
- [nacl](https://github.com/kevinburke/nacl) [![GitHub stars](https://img.shields.io/github/stars/kevinburke/nacl?style=flat)](https://github.com/kevinburke/nacl/stargazers) - Go implementation of the NaCL set of API's.
- [optimus-go](https://github.com/pjebs/optimus-go) [![GitHub stars](https://img.shields.io/github/stars/pjebs/optimus-go?style=flat)](https://github.com/pjebs/optimus-go/stargazers) - ID hashing and Obfuscation using Knuth's Algorithm.
- [passlib](https://github.com/hlandau/passlib) [![GitHub stars](https://img.shields.io/github/stars/hlandau/passlib?style=flat)](https://github.com/hlandau/passlib/stargazers) - Futureproof password hashing library.
- [passwap](https://github.com/zitadel/passwap) [![GitHub stars](https://img.shields.io/github/stars/zitadel/passwap?style=flat)](https://github.com/zitadel/passwap/stargazers) - Provides a unified implementation between different password hashing algorithms
- [pii-shield](https://github.com/pii-shield/pii-shield) [![GitHub stars](https://img.shields.io/github/stars/pii-shield/pii-shield?style=flat)](https://github.com/pii-shield/pii-shield/stargazers) - Zero-code log sanitization sidecar for Kubernetes that redacts PII from logs.
- [pm](https://github.com/nicola-strappazzon/password-manager) [![GitHub stars](https://img.shields.io/github/stars/nicola-strappazzon/password-manager?style=flat)](https://github.com/nicola-strappazzon/password-manager/stargazers) - Unix-style password manager written in Go to save your data with OpenPGP encryption.
- [procscope](https://github.com/Mutasem-mk4/procscope) [![GitHub stars](https://img.shields.io/github/stars/Mutasem-mk4/procscope?style=flat)](https://github.com/Mutasem-mk4/procscope/stargazers) - Process-scoped runtime investigator using eBPF to trace process lifecycle, file activity, and network connections.
- [qrand](https://github.com/bitfield/qrand) [![GitHub stars](https://img.shields.io/github/stars/bitfield/qrand?style=flat)](https://github.com/bitfield/qrand/stargazers) - Client for the ANU Quantum Numbers (AQN) API, providing quantum-mechanically secure random data.
- [Razify](https://github.com/Hossiy21/razify) [![GitHub stars](https://img.shields.io/github/stars/Hossiy21/razify?style=flat)](https://github.com/Hossiy21/razify/stargazers) - CLI to scan, validate and audit .env files for leaked secrets and environment drift.
- [redact](https://github.com/alesr/redact) [![GitHub stars](https://img.shields.io/github/stars/alesr/redact?style=flat)](https://github.com/alesr/redact/stargazers) - Redact sensitive information from slog-based logs using a configurable pipeline.
- [SafeDep/vet](https://github.com/safedep/vet) [![GitHub stars](https://img.shields.io/github/stars/safedep/vet?style=flat)](https://github.com/safedep/vet/stargazers) - Protect against malicious open source packages.
- [secret](https://github.com/rsjethani/secret) [![GitHub stars](https://img.shields.io/github/stars/rsjethani/secret?style=flat)](https://github.com/rsjethani/secret/stargazers) - Prevent your secrets from leaking into logs, std\* etc.
- [secure](https://github.com/unrolled/secure) [![GitHub stars](https://img.shields.io/github/stars/unrolled/secure?style=flat)](https://github.com/unrolled/secure/stargazers) - HTTP middleware for Go that facilitates some quick security wins.
- [secureio](https://github.com/xaionaro-go/secureio) [![GitHub stars](https://img.shields.io/github/stars/xaionaro-go/secureio?style=flat)](https://github.com/xaionaro-go/secureio/stargazers) - An keyexchanging+authenticating+encrypting wrapper and multiplexer for `io.ReadWriteCloser` based on XChaCha20-poly1305, ECDH and ED25519.
- [simple-scrypt](https://github.com/elithrar/simple-scrypt) [![GitHub stars](https://img.shields.io/github/stars/elithrar/simple-scrypt?style=flat)](https://github.com/elithrar/simple-scrypt/stargazers) - Scrypt package with a simple, obvious API and automatic cost calibration built-in.
- [ssh-vault](https://github.com/ssh-vault/ssh-vault) [![GitHub stars](https://img.shields.io/github/stars/ssh-vault/ssh-vault?style=flat)](https://github.com/ssh-vault/ssh-vault/stargazers) - encrypt/decrypt using ssh keys.
- [sslmgr](https://github.com/adrianosela/sslmgr) [![GitHub stars](https://img.shields.io/github/stars/adrianosela/sslmgr?style=flat)](https://github.com/adrianosela/sslmgr/stargazers) - SSL certificates made easy with a high level wrapper around acme/autocert.
- [teler-waf](https://github.com/kitabisa/teler-waf) [![GitHub stars](https://img.shields.io/github/stars/kitabisa/teler-waf?style=flat)](https://github.com/kitabisa/teler-waf/stargazers) - teler-waf is a Go HTTP middleware that provide teler IDS functionality to protect against web-based attacks and improve the security of Go-based web applications. It is highly configurable and easy to integrate into existing Go applications.
- [themis](https://github.com/cossacklabs/themis) [![GitHub stars](https://img.shields.io/github/stars/cossacklabs/themis?style=flat)](https://github.com/cossacklabs/themis/stargazers) - high-level cryptographic library for solving typical data security tasks (secure data storage, secure messaging, zero-knowledge proof authentication), available for 14 languages, best fit for multi-platform apps.
- [urusai](https://github.com/calpa/urusai) [![GitHub stars](https://img.shields.io/github/stars/calpa/urusai?style=flat)](https://github.com/calpa/urusai/stargazers) - Urusai ("noisy" in Japanese) is a Go implementation of a random HTTP/DNS traffic noise generator that helps protect privacy by creating digital smokescreens while browsing.
- [veil](https://github.com/getveil/veil) [![GitHub stars](https://img.shields.io/github/stars/getveil/veil?style=flat)](https://github.com/getveil/veil/stargazers) - Local HTTPS proxy that hides API credentials from AI coding agents. OS keychain integration, format-aware placeholders, SQLite audit log.


**[⬆ back to top](#contents)**

## Serialization

_Libraries and tools for binary serialization._

- [bambam](https://github.com/glycerine/bambam) [![GitHub stars](https://img.shields.io/github/stars/glycerine/bambam?style=flat)](https://github.com/glycerine/bambam/stargazers) - generator for Cap'n Proto schemas from go.
- [bel](https://github.com/32leaves/bel) [![GitHub stars](https://img.shields.io/github/stars/32leaves/bel?style=flat)](https://github.com/32leaves/bel/stargazers) - Generate TypeScript interfaces from Go structs/interfaces. Useful for JSON RPC.
- [binstruct](https://github.com/ghostiam/binstruct) [![GitHub stars](https://img.shields.io/github/stars/ghostiam/binstruct?style=flat)](https://github.com/ghostiam/binstruct/stargazers) - Golang binary decoder for mapping data into the structure.
- [cbor](https://github.com/fxamacker/cbor) [![GitHub stars](https://img.shields.io/github/stars/fxamacker/cbor?style=flat)](https://github.com/fxamacker/cbor/stargazers) - Small, safe, and easy CBOR encoding and decoding library.
- [colfer](https://github.com/pascaldekloe/colfer) [![GitHub stars](https://img.shields.io/github/stars/pascaldekloe/colfer?style=flat)](https://github.com/pascaldekloe/colfer/stargazers) - Code generation for the Colfer binary format.
- [csvutil](https://github.com/jszwec/csvutil) [![GitHub stars](https://img.shields.io/github/stars/jszwec/csvutil?style=flat)](https://github.com/jszwec/csvutil/stargazers) - High Performance, idiomatic CSV record encoding and decoding to native Go structures.
- [elastic](https://github.com/epiclabs-io/elastic) [![GitHub stars](https://img.shields.io/github/stars/epiclabs-io/elastic?style=flat)](https://github.com/epiclabs-io/elastic/stargazers) - Convert slices, maps or any other unknown value across different types at run-time, no matter what.
- [fixedwidth](https://github.com/huydang284/fixedwidth) [![GitHub stars](https://img.shields.io/github/stars/huydang284/fixedwidth?style=flat)](https://github.com/huydang284/fixedwidth/stargazers) - Fixed-width text formatting (UTF-8 supported).
- [fwencoder](https://github.com/o1egl/fwencoder) [![GitHub stars](https://img.shields.io/github/stars/o1egl/fwencoder?style=flat)](https://github.com/o1egl/fwencoder/stargazers) - Fixed width file parser (encoding and decoding library) for Go.
- [go-capnproto](https://github.com/glycerine/go-capnproto) [![GitHub stars](https://img.shields.io/github/stars/glycerine/go-capnproto?style=flat)](https://github.com/glycerine/go-capnproto/stargazers) - Cap'n Proto library and parser for go.
- [go-codec](https://github.com/ugorji/go) [![GitHub stars](https://img.shields.io/github/stars/ugorji/go?style=flat)](https://github.com/ugorji/go/stargazers) - High Performance, feature-Rich, idiomatic encode, decode and rpc library for msgpack, cbor and json, with runtime-based OR code-generation support.
- [go-csvlib](https://github.com/tiendc/go-csvlib) [![GitHub stars](https://img.shields.io/github/stars/tiendc/go-csvlib?style=flat)](https://github.com/tiendc/go-csvlib/stargazers) - High level and rich functionalities CSV serialization/deserialization library.
- [goprotobuf](https://github.com/golang/protobuf) [![GitHub stars](https://img.shields.io/github/stars/golang/protobuf?style=flat)](https://github.com/golang/protobuf/stargazers) - Go support, in the form of a library and protocol compiler plugin, for Google's protocol buffers.
- [gotiny](https://github.com/raszia/gotiny) [![GitHub stars](https://img.shields.io/github/stars/raszia/gotiny?style=flat)](https://github.com/raszia/gotiny/stargazers) - Efficient Go serialization library, gotiny is almost as fast as serialization libraries that generate code.
- [jsoniter](https://github.com/json-iterator/go) [![GitHub stars](https://img.shields.io/github/stars/json-iterator/go?style=flat)](https://github.com/json-iterator/go/stargazers) - High-performance 100% compatible drop-in replacement of "encoding/json".
- [mus-go](https://github.com/mus-format/mus-go) [![GitHub stars](https://img.shields.io/github/stars/mus-format/mus-go?style=flat)](https://github.com/mus-format/mus-go/stargazers) - MUS format serializer for Go.
- [php_session_decoder](https://github.com/yvasiyarov/php_session_decoder) [![GitHub stars](https://img.shields.io/github/stars/yvasiyarov/php_session_decoder?style=flat)](https://github.com/yvasiyarov/php_session_decoder/stargazers) - GoLang library for working with PHP session format and PHP Serialize/Unserialize functions.
- [pletter](https://github.com/vimeda/pletter) [![GitHub stars](https://img.shields.io/github/stars/vimeda/pletter?style=flat)](https://github.com/vimeda/pletter/stargazers) - A standard way to wrap a proto message for message brokers.
- [proto](https://github.com/emicklei/proto) [![GitHub stars](https://img.shields.io/github/stars/emicklei/proto?style=flat)](https://github.com/emicklei/proto/stargazers) - Parser and writer for Google ProtocolBuffers .proto files.
- [structomap](https://github.com/tuvistavie/structomap) [![GitHub stars](https://img.shields.io/github/stars/tuvistavie/structomap?style=flat)](https://github.com/tuvistavie/structomap/stargazers) - Library to easily and dynamically generate maps from static structures.
- [unitpacking](https://github.com/recolude/unitpacking) [![GitHub stars](https://img.shields.io/github/stars/recolude/unitpacking?style=flat)](https://github.com/recolude/unitpacking/stargazers) - Library to pack unit vectors into as fewest bytes as possible.

**[⬆ back to top](#contents)**

## Server Applications

- [algernon](https://github.com/xyproto/algernon) [![GitHub stars](https://img.shields.io/github/stars/xyproto/algernon?style=flat)](https://github.com/xyproto/algernon/stargazers) - HTTP/2 web server with built-in support for Lua, Markdown, GCSS and Amber.
- [Caddy](https://github.com/caddyserver/caddy) [![GitHub stars](https://img.shields.io/github/stars/caddyserver/caddy?style=flat)](https://github.com/caddyserver/caddy/stargazers) - Caddy is an alternative, HTTP/2 web server that's easy to configure and use.
- [consul](https://www.consul.io/) - Consul is a tool for service discovery, monitoring and configuration.
- [cortex-tenant](https://github.com/blind-oracle/cortex-tenant) [![GitHub stars](https://img.shields.io/github/stars/blind-oracle/cortex-tenant?style=flat)](https://github.com/blind-oracle/cortex-tenant/stargazers) - Prometheus remote write proxy that adds add Cortex tenant ID header based on metric labels.
- [devd](https://github.com/cortesi/devd) [![GitHub stars](https://img.shields.io/github/stars/cortesi/devd?style=flat)](https://github.com/cortesi/devd/stargazers) - Local webserver for developers.
- [discovery](https://github.com/Bilibili/discovery) [![GitHub stars](https://img.shields.io/github/stars/Bilibili/discovery?style=flat)](https://github.com/Bilibili/discovery/stargazers) - A registry for resilient mid-tier load balancing and failover.
- [dudeldu](https://github.com/krotik/dudeldu) [![GitHub stars](https://img.shields.io/github/stars/krotik/dudeldu?style=flat)](https://github.com/krotik/dudeldu/stargazers) - A simple SHOUTcast server.
- [Easegress](https://github.com/megaease/easegress) [![GitHub stars](https://img.shields.io/github/stars/megaease/easegress?style=flat)](https://github.com/megaease/easegress/stargazers) - A cloud native high availability/performance traffic orchestration system with observability and extensibility.
- [Engity's Bifröst](https://bifroest.engity.org/) - Highly customizable SSH server with several ways to authorize a user how to execute its session (local or in containers).
- [etcd](https://github.com/etcd-io/etcd) [![GitHub stars](https://img.shields.io/github/stars/etcd-io/etcd?style=flat)](https://github.com/etcd-io/etcd/stargazers) - Highly-available key value store for shared configuration and service discovery.
- [Euterpe](https://github.com/ironsmile/euterpe) [![GitHub stars](https://img.shields.io/github/stars/ironsmile/euterpe?style=flat)](https://github.com/ironsmile/euterpe/stargazers) - Self-hosted music streaming server with built-in web UI and REST API.
- [Fider](https://github.com/getfider/fider) [![GitHub stars](https://img.shields.io/github/stars/getfider/fider?style=flat)](https://github.com/getfider/fider/stargazers) - Fider is an open platform to collect and organize customer feedback.
- [Flagr](https://github.com/checkr/flagr) [![GitHub stars](https://img.shields.io/github/stars/checkr/flagr?style=flat)](https://github.com/checkr/flagr/stargazers) - Flagr is an open-source feature flagging and A/B testing service.
- [flipt](https://github.com/markphelps/flipt) [![GitHub stars](https://img.shields.io/github/stars/markphelps/flipt?style=flat)](https://github.com/markphelps/flipt/stargazers) - A self contained feature flag solution written in Go and Vue.js
- [go-feature-flag](https://github.com/thomaspoignant/go-feature-flag) [![GitHub stars](https://img.shields.io/github/stars/thomaspoignant/go-feature-flag?style=flat)](https://github.com/thomaspoignant/go-feature-flag/stargazers) - A simple, complete and lightweight self-hosted feature flag solution 100% Open Source.
- [go-proxy-cache](https://github.com/fabiocicerchia/go-proxy-cache) [![GitHub stars](https://img.shields.io/github/stars/fabiocicerchia/go-proxy-cache?style=flat)](https://github.com/fabiocicerchia/go-proxy-cache/stargazers) - Simple Reverse Proxy with Caching, written in Go, using Redis.
- [gondola](https://github.com/bmf-san/gondola) [![GitHub stars](https://img.shields.io/github/stars/bmf-san/gondola?style=flat)](https://github.com/bmf-san/gondola/stargazers) - A YAML based golang reverse proxy.
- [goshs](https://github.com/patrickhener/goshs) [![GitHub stars](https://img.shields.io/github/stars/patrickhener/goshs?style=flat)](https://github.com/patrickhener/goshs/stargazers) - SimpleHTTPServer replacement with file upload/download, WebDAV, SFTP, SMB, TLS, authentication, and share links.
- [Kono](https://github.com/starwalkn/kono) [![GitHub stars](https://img.shields.io/github/stars/starwalkn/kono?style=flat)](https://github.com/starwalkn/kono/stargazers) - lightweight extendable API Gateway in Go - parallel fan-out, flexible aggregation, and zero configuration magic.
- [lets-proxy2](https://github.com/rekby/lets-proxy2) [![GitHub stars](https://img.shields.io/github/stars/rekby/lets-proxy2?style=flat)](https://github.com/rekby/lets-proxy2/stargazers) - Reverse proxy for handle https with issue certificates in fly from lets-encrypt.
- [minio](https://github.com/pgsty/minio) [![GitHub stars](https://img.shields.io/github/stars/pgsty/minio?style=flat)](https://github.com/pgsty/minio/stargazers) - Community Maintained Fork of minio (Object Storage Service).
- [Moxy](https://github.com/sinhashubham95/moxy) [![GitHub stars](https://img.shields.io/github/stars/sinhashubham95/moxy?style=flat)](https://github.com/sinhashubham95/moxy/stargazers) - Moxy is a simple mocker and proxy application server, you can create mock endpoints as well as proxy requests in case no mock exists for the endpoint.
- [nginx-prometheus](https://github.com/blind-oracle/nginx-prometheus) [![GitHub stars](https://img.shields.io/github/stars/blind-oracle/nginx-prometheus?style=flat)](https://github.com/blind-oracle/nginx-prometheus/stargazers) - Nginx log parser and exporter to Prometheus.
- [nsq](https://nsq.io/) - A realtime distributed messaging platform.
- [OpenRun](https://github.com/openrundev/openrun) [![GitHub stars](https://img.shields.io/github/stars/openrundev/openrun?style=flat)](https://github.com/openrundev/openrun/stargazers) - Open-source alternative to Google Cloud Run and AWS App Runner. Easily deploy internal tools across a team.
- [pocketbase](https://github.com/pocketbase/pocketbase) [![GitHub stars](https://img.shields.io/github/stars/pocketbase/pocketbase?style=flat)](https://github.com/pocketbase/pocketbase/stargazers) - PocketBase is a realtime backend in 1 file consisting of embedded database (SQLite) with realtime subscriptions, built-in auth management and much more.
- [protoxy](https://github.com/camgraff/protoxy) [![GitHub stars](https://img.shields.io/github/stars/camgraff/protoxy?style=flat)](https://github.com/camgraff/protoxy/stargazers) - A proxy server that converts JSON request bodies to Protocol Buffers.
- [psql-streamer](https://github.com/blind-oracle/psql-streamer) [![GitHub stars](https://img.shields.io/github/stars/blind-oracle/psql-streamer?style=flat)](https://github.com/blind-oracle/psql-streamer/stargazers) - Stream database events from PostgreSQL to Kafka.
- [riemann-relay](https://github.com/blind-oracle/riemann-relay) [![GitHub stars](https://img.shields.io/github/stars/blind-oracle/riemann-relay?style=flat)](https://github.com/blind-oracle/riemann-relay/stargazers) - Relay to load-balance Riemann events and/or convert them to Carbon.
- [RoadRunner](https://github.com/spiral/roadrunner) [![GitHub stars](https://img.shields.io/github/stars/spiral/roadrunner?style=flat)](https://github.com/spiral/roadrunner/stargazers) - High-performance PHP application server, load-balancer and process manager.
- [SFTPGo](https://github.com/drakkan/sftpgo) [![GitHub stars](https://img.shields.io/github/stars/drakkan/sftpgo?style=flat)](https://github.com/drakkan/sftpgo/stargazers) - Fully featured and highly configurable SFTP server with optional FTP/S and WebDAV support. It can serve local filesystem and Cloud Storage backends such as S3 and Google Cloud Storage.
- [Trickster](https://github.com/tricksterproxy/trickster) [![GitHub stars](https://img.shields.io/github/stars/tricksterproxy/trickster?style=flat)](https://github.com/tricksterproxy/trickster/stargazers) - HTTP reverse proxy cache and time series accelerator.
- [wd-41](https://github.com/baalimago/wd-41) [![GitHub stars](https://img.shields.io/github/stars/baalimago/wd-41?style=flat)](https://github.com/baalimago/wd-41/stargazers) - A (w)eb (d)evelopment server with automatic live-reload on file changes.
- [Wish](https://github.com/charmbracelet/wish) [![GitHub stars](https://img.shields.io/github/stars/charmbracelet/wish?style=flat)](https://github.com/charmbracelet/wish/stargazers) - Make SSH apps, just like that!

**[⬆ back to top](#contents)**

## Stream Processing

_Libraries and tools for stream processing and reactive programming._

- [go-etl](https://github.com/Breeze0806/go-etl) [![GitHub stars](https://img.shields.io/github/stars/Breeze0806/go-etl?style=flat)](https://github.com/Breeze0806/go-etl/stargazers) - A lightweight toolkit for data source extraction, transformation, and loading (ETL).
- [go-streams](https://github.com/reugn/go-streams) [![GitHub stars](https://img.shields.io/github/stars/reugn/go-streams?style=flat)](https://github.com/reugn/go-streams/stargazers) - Go stream processing library.
- [goio](https://github.com/primetalk/goio) [![GitHub stars](https://img.shields.io/github/stars/primetalk/goio?style=flat)](https://github.com/primetalk/goio/stargazers) - An implementation of IO, Stream, Fiber for Golang, inspired by awesome Scala libraries cats and fs2.
- [gostream](https://github.com/mariomac/gostream) [![GitHub stars](https://img.shields.io/github/stars/mariomac/gostream?style=flat)](https://github.com/mariomac/gostream/stargazers) - Type-safe stream processing library inspired by the Java Streams API.
- [machine](https://github.com/whitaker-io/machine) [![GitHub stars](https://img.shields.io/github/stars/whitaker-io/machine?style=flat)](https://github.com/whitaker-io/machine/stargazers) - Go library for writing and generating stream workers with built in metrics and traceability.
- [nibbler](https://github.com/naughtygopher/nibbler) [![GitHub stars](https://img.shields.io/github/stars/naughtygopher/nibbler?style=flat)](https://github.com/naughtygopher/nibbler/stargazers) - A lightweight package for micro batch processing.
- [ro](https://github.com/samber/ro) [![GitHub stars](https://img.shields.io/github/stars/samber/ro?style=flat)](https://github.com/samber/ro/stargazers) - Reactive Programming: declarative and composable API for event-driven applications.
- [signals](https://github.com/coregx/signals) [![GitHub stars](https://img.shields.io/github/stars/coregx/signals?style=flat)](https://github.com/coregx/signals/stargazers) - Type-safe reactive state management inspired by Angular Signals with computed values, effects, and dependency tracking.
- [stream](https://github.com/youthlin/stream) [![GitHub stars](https://img.shields.io/github/stars/youthlin/stream?style=flat)](https://github.com/youthlin/stream/stargazers) - Go Stream, like Java 8 Stream: Filter/Map/FlatMap/Peek/Sorted/ForEach/Reduce...
- [StreamSQL](https://github.com/rulego/streamsql) [![GitHub stars](https://img.shields.io/github/stars/rulego/streamsql?style=flat)](https://github.com/rulego/streamsql/stargazers) - A lightweight streaming SQL engine for real-time data processing.

**[⬆ back to top](#contents)**

## Template Engines

_Libraries and tools for templating and lexing._

- [bagme](https://github.com/boxesandglue/bagme) [![GitHub stars](https://img.shields.io/github/stars/boxesandglue/bagme?style=flat)](https://github.com/boxesandglue/bagme/stargazers) - HTML/CSS to PDF rendering with TeX-quality typesetting in pure Go.
- [ego](https://github.com/benbjohnson/ego) [![GitHub stars](https://img.shields.io/github/stars/benbjohnson/ego?style=flat)](https://github.com/benbjohnson/ego/stargazers) - Lightweight templating language that lets you write templates in Go. Templates are translated into Go and compiled.
- [fasttemplate](https://github.com/valyala/fasttemplate) [![GitHub stars](https://img.shields.io/github/stars/valyala/fasttemplate?style=flat)](https://github.com/valyala/fasttemplate/stargazers) - Simple and fast template engine. Substitutes template placeholders up to 10x faster than [text/template](https://golang.org/pkg/text/template/).
- [gomponents](https://www.gomponents.com) - HTML 5 components in pure Go, that look something like this: `func(name string) g.Node { return Div(Class("headline"), g.Textf("Hi %v!", name)) }`.
- [got](https://github.com/goradd/got) [![GitHub stars](https://img.shields.io/github/stars/goradd/got?style=flat)](https://github.com/goradd/got/stargazers) - A Go code generator inspired by Hero and Fasttemplate. Has include files, custom tag definitions, injected Go code, language translation, and more.
- [goview](https://github.com/foolin/goview) [![GitHub stars](https://img.shields.io/github/stars/foolin/goview?style=flat)](https://github.com/foolin/goview/stargazers) - Goview is a lightweight, minimalist and idiomatic template library based on golang html/template for building Go web application.
- [gox](https://github.com/doors-dev/gox) [![GitHub stars](https://img.shields.io/github/stars/doors-dev/gox?style=flat)](https://github.com/doors-dev/gox/stargazers) - HTML templates as first-class Go expressions, with seamless editor support.
- [htmgo](https://htmgo.dev) - build simple and scalable systems with go + htmx
- [jet](https://github.com/CloudyKit/jet) [![GitHub stars](https://img.shields.io/github/stars/CloudyKit/jet?style=flat)](https://github.com/CloudyKit/jet/stargazers) - Jet template engine.
- [liquid](https://github.com/osteele/liquid) [![GitHub stars](https://img.shields.io/github/stars/osteele/liquid?style=flat)](https://github.com/osteele/liquid/stargazers) - Go implementation of Shopify Liquid templates.
- [maroto](https://github.com/johnfercher/maroto) [![GitHub stars](https://img.shields.io/github/stars/johnfercher/maroto?style=flat)](https://github.com/johnfercher/maroto/stargazers) - A maroto way to create PDFs. Maroto is inspired in Bootstrap and uses gofpdf. Fast and simple.
- [pongo2](https://github.com/flosch/pongo2) [![GitHub stars](https://img.shields.io/github/stars/flosch/pongo2?style=flat)](https://github.com/flosch/pongo2/stargazers) - Django-like template-engine for Go.
- [quicktemplate](https://github.com/valyala/quicktemplate) [![GitHub stars](https://img.shields.io/github/stars/valyala/quicktemplate?style=flat)](https://github.com/valyala/quicktemplate/stargazers) - Fast, powerful, yet easy to use template engine. Converts templates into Go code and then compiles it.
- [Razor](https://github.com/sipin/gorazor) [![GitHub stars](https://img.shields.io/github/stars/sipin/gorazor?style=flat)](https://github.com/sipin/gorazor/stargazers) - Razor view engine for Golang.
- [Soy](https://github.com/robfig/soy) [![GitHub stars](https://img.shields.io/github/stars/robfig/soy?style=flat)](https://github.com/robfig/soy/stargazers) - Closure templates (aka Soy templates) for Go, following the [official spec](https://developers.google.com/closure/templates/).
- [sprout](https://github.com/go-sprout/sprout) [![GitHub stars](https://img.shields.io/github/stars/go-sprout/sprout?style=flat)](https://github.com/go-sprout/sprout/stargazers) - Useful template functions for Go templates.
- [tbd](https://github.com/lucasepe/tbd) [![GitHub stars](https://img.shields.io/github/stars/lucasepe/tbd?style=flat)](https://github.com/lucasepe/tbd/stargazers) - A really simple way to create text templates with placeholders - exposes extra builtin Git repo metadata.
- [templ](https://github.com/a-h/templ) [![GitHub stars](https://img.shields.io/github/stars/a-h/templ?style=flat)](https://github.com/a-h/templ/stargazers) - A HTML templating language that has great developer tooling.
- [templator](https://github.com/alesr/templator) [![GitHub stars](https://img.shields.io/github/stars/alesr/templator?style=flat)](https://github.com/alesr/templator/stargazers) - A type-safe HTML template rendering engine for Go.

**[⬆ back to top](#contents)**

## Testing

_Libraries for testing codebases and generating test data._

### Testing Frameworks

- [apitest](https://apitest.dev) - Simple and extensible behavioural testing library for REST based services or HTTP handlers that supports mocking external http calls and rendering of sequence diagrams.
- [arch-go](https://github.com/arch-go/arch-go) [![GitHub stars](https://img.shields.io/github/stars/arch-go/arch-go?style=flat)](https://github.com/arch-go/arch-go/stargazers) - Architecture testing tool for Go projects.
- [assay](https://github.com/tushariitr-19/assay) [![GitHub stars](https://img.shields.io/github/stars/tushariitr-19/assay?style=flat)](https://github.com/tushariitr-19/assay/stargazers) - Framework-agnostic evaluation library for testing Go agents and MCP servers with deterministic checks, CI-ready exit codes, and zero-code YAML-based testing.
- [assert](https://github.com/go-playground/assert) [![GitHub stars](https://img.shields.io/github/stars/go-playground/assert?style=flat)](https://github.com/go-playground/assert/stargazers) - Basic Assertion Library used along side native go testing, with building blocks for custom assertions.
- [baloo](https://github.com/h2non/baloo) [![GitHub stars](https://img.shields.io/github/stars/h2non/baloo?style=flat)](https://github.com/h2non/baloo/stargazers) - Expressive and versatile end-to-end HTTP API testing made easy.
- [be](https://github.com/carlmjohnson/be) [![GitHub stars](https://img.shields.io/github/stars/carlmjohnson/be?style=flat)](https://github.com/carlmjohnson/be/stargazers) - The minimalist generic test assertion library.
- [biff](https://github.com/fulldump/biff) [![GitHub stars](https://img.shields.io/github/stars/fulldump/biff?style=flat)](https://github.com/fulldump/biff/stargazers) - Bifurcation testing framework, BDD compatible.
- [charlatan](https://github.com/percolate/charlatan) [![GitHub stars](https://img.shields.io/github/stars/percolate/charlatan?style=flat)](https://github.com/percolate/charlatan/stargazers) - Tool to generate fake interface implementations for tests.
- [commander](https://github.com/SimonBaeumer/commander) [![GitHub stars](https://img.shields.io/github/stars/SimonBaeumer/commander?style=flat)](https://github.com/SimonBaeumer/commander/stargazers) - Tool for testing cli applications on windows, linux and osx.
- [cupaloy](https://github.com/bradleyjkemp/cupaloy) [![GitHub stars](https://img.shields.io/github/stars/bradleyjkemp/cupaloy?style=flat)](https://github.com/bradleyjkemp/cupaloy/stargazers) - Simple snapshot testing addon for your test framework.
- [dbcleaner](https://github.com/khaiql/dbcleaner) [![GitHub stars](https://img.shields.io/github/stars/khaiql/dbcleaner?style=flat)](https://github.com/khaiql/dbcleaner/stargazers) - Clean database for testing purpose, inspired by `database_cleaner` in Ruby.
- [dft](https://github.com/abecodes/dft) [![GitHub stars](https://img.shields.io/github/stars/abecodes/dft?style=flat)](https://github.com/abecodes/dft/stargazers) - Lightweight, zero dependency docker containers for testing (or more).
- [dsunit](https://github.com/viant/dsunit) [![GitHub stars](https://img.shields.io/github/stars/viant/dsunit?style=flat)](https://github.com/viant/dsunit/stargazers) - Datastore testing for SQL, NoSQL, structured files.
- [embedded-postgres](https://github.com/fergusstrange/embedded-postgres) [![GitHub stars](https://img.shields.io/github/stars/fergusstrange/embedded-postgres?style=flat)](https://github.com/fergusstrange/embedded-postgres/stargazers) - Run a real Postgres database locally on Linux, OSX or Windows as part of another Go application or test.
- [endly](https://github.com/viant/endly) [![GitHub stars](https://img.shields.io/github/stars/viant/endly?style=flat)](https://github.com/viant/endly/stargazers) - Declarative end to end functional testing.
- [envite](https://github.com/PerimeterX/envite) [![GitHub stars](https://img.shields.io/github/stars/PerimeterX/envite?style=flat)](https://github.com/PerimeterX/envite/stargazers) - Dev and testing environment management framework.
- [fixenv](https://github.com/rekby/fixenv) [![GitHub stars](https://img.shields.io/github/stars/rekby/fixenv?style=flat)](https://github.com/rekby/fixenv/stargazers) - Fixture manage engine, inspired by pytest fixtures.
- [flute](https://github.com/suzuki-shunsuke/flute) [![GitHub stars](https://img.shields.io/github/stars/suzuki-shunsuke/flute?style=flat)](https://github.com/suzuki-shunsuke/flute/stargazers) - HTTP client testing framework.
- [frisby](https://github.com/verdverm/frisby) [![GitHub stars](https://img.shields.io/github/stars/verdverm/frisby?style=flat)](https://github.com/verdverm/frisby/stargazers) - REST API testing framework.
- [gherkingen](https://github.com/hedhyw/gherkingen) [![GitHub stars](https://img.shields.io/github/stars/hedhyw/gherkingen?style=flat)](https://github.com/hedhyw/gherkingen/stargazers) - BDD boilerplate generator and framework.
- [ginkgo](https://onsi.github.io/ginkgo/) - BDD Testing Framework for Go.
- [gnomock](https://github.com/orlangure/gnomock) [![GitHub stars](https://img.shields.io/github/stars/orlangure/gnomock?style=flat)](https://github.com/orlangure/gnomock/stargazers) - integration testing with real dependencies (database, cache, even Kubernetes or AWS) running in Docker, without mocks.
- [go-carpet](https://github.com/msoap/go-carpet) [![GitHub stars](https://img.shields.io/github/stars/msoap/go-carpet?style=flat)](https://github.com/msoap/go-carpet/stargazers) - Tool for viewing test coverage in terminal.
- [go-cmp](https://github.com/google/go-cmp) [![GitHub stars](https://img.shields.io/github/stars/google/go-cmp?style=flat)](https://github.com/google/go-cmp/stargazers) - Package for comparing Go values in tests.
- [go-hit](https://github.com/Eun/go-hit) [![GitHub stars](https://img.shields.io/github/stars/Eun/go-hit?style=flat)](https://github.com/Eun/go-hit/stargazers) - Hit is an http integration test framework written in golang.
- [go-httpbin](https://github.com/mccutchen/go-httpbin) [![GitHub stars](https://img.shields.io/github/stars/mccutchen/go-httpbin?style=flat)](https://github.com/mccutchen/go-httpbin/stargazers) - HTTP testing and debugging tool with various endpoints for client testing.
- [go-mutesting](https://github.com/jonbaldie/go-mutesting) [![GitHub stars](https://img.shields.io/github/stars/jonbaldie/go-mutesting?style=flat)](https://github.com/jonbaldie/go-mutesting/stargazers) - Mutation testing for Go with CI quality gates, coverage-aware MSI, baseline tracking, and git-diff filtering.
- [go-mysql-test-container](https://github.com/arikama/go-mysql-test-container) [![GitHub stars](https://img.shields.io/github/stars/arikama/go-mysql-test-container?style=flat)](https://github.com/arikama/go-mysql-test-container/stargazers) - Golang MySQL testcontainer to help with MySQL integration testing.
- [go-snaps](http://github.com/gkampitakis/go-snaps) - Jest-like snapshot testing in Golang.
- [go-test-coverage](https://github.com/vladopajic/go-test-coverage) [![GitHub stars](https://img.shields.io/github/stars/vladopajic/go-test-coverage?style=flat)](https://github.com/vladopajic/go-test-coverage/stargazers) - Tool that reports coverage of files below set threshold.
- [go-testdeep](https://github.com/maxatome/go-testdeep) [![GitHub stars](https://img.shields.io/github/stars/maxatome/go-testdeep?style=flat)](https://github.com/maxatome/go-testdeep/stargazers) - Extremely flexible golang deep comparison, extends the go testing package.
- [go-testing](https://github.com/tkrop/go-testing) [![GitHub stars](https://img.shields.io/github/stars/tkrop/go-testing?style=flat)](https://github.com/tkrop/go-testing/stargazers) - Go testing extension, that allows a simple setup of strongly isolated unit, component, and integration test providing advanced mock support extending gomock and gock.
- [go-testpredicate](https://github.com/maargenton/go-testpredicate) [![GitHub stars](https://img.shields.io/github/stars/maargenton/go-testpredicate?style=flat)](https://github.com/maargenton/go-testpredicate/stargazers) - Test predicate style assertions library with extensive diagnostics output.
- [go-vcr](https://github.com/dnaeon/go-vcr) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/go-vcr?style=flat)](https://github.com/dnaeon/go-vcr/stargazers) - Record and replay your HTTP interactions for fast, deterministic and accurate tests.
- [goblin](https://github.com/franela/goblin) [![GitHub stars](https://img.shields.io/github/stars/franela/goblin?style=flat)](https://github.com/franela/goblin/stargazers) - Mocha like testing framework of Go.
- [goc](https://github.com/qiniu/goc) [![GitHub stars](https://img.shields.io/github/stars/qiniu/goc?style=flat)](https://github.com/qiniu/goc/stargazers) - Goc is a comprehensive coverage testing system for The Go Programming Language.
- [gocheck](https://labix.org/gocheck) - More advanced testing framework alternative to gotest.
- [GoConvey](https://github.com/smartystreets/goconvey/) [![GitHub stars](https://img.shields.io/github/stars/smartystreets/goconvey/?style=flat)](https://github.com/smartystreets/goconvey//stargazers) - BDD-style framework with web UI and live reload.
- [gocrest](https://github.com/corbym/gocrest) [![GitHub stars](https://img.shields.io/github/stars/corbym/gocrest?style=flat)](https://github.com/corbym/gocrest/stargazers) - Composable hamcrest-like matchers for Go assertions.
- [godog](https://github.com/cucumber/godog) [![GitHub stars](https://img.shields.io/github/stars/cucumber/godog?style=flat)](https://github.com/cucumber/godog/stargazers) - Cucumber BDD framework for Go.
- [gofight](https://github.com/appleboy/gofight) [![GitHub stars](https://img.shields.io/github/stars/appleboy/gofight?style=flat)](https://github.com/appleboy/gofight/stargazers) - API Handler Testing for Golang Router framework.
- [gogiven](https://github.com/corbym/gogiven) [![GitHub stars](https://img.shields.io/github/stars/corbym/gogiven?style=flat)](https://github.com/corbym/gogiven/stargazers) - YATSPEC-like BDD testing framework for Go.
- [gomatch](https://github.com/jfilipczyk/gomatch) [![GitHub stars](https://img.shields.io/github/stars/jfilipczyk/gomatch?style=flat)](https://github.com/jfilipczyk/gomatch/stargazers) - library created for testing JSON against patterns.
- [gomega](https://onsi.github.io/gomega/) - Rspec like matcher/assertion library.
- [gospecify](https://github.com/stesla/gospecify) [![GitHub stars](https://img.shields.io/github/stars/stesla/gospecify?style=flat)](https://github.com/stesla/gospecify/stargazers) - This provides a BDD syntax for testing your Go code. It should be familiar to anybody who has used libraries such as rspec.
- [gosuite](https://github.com/pavlo/gosuite) [![GitHub stars](https://img.shields.io/github/stars/pavlo/gosuite?style=flat)](https://github.com/pavlo/gosuite/stargazers) - Brings lightweight test suites with setup/teardown facilities to `testing` by leveraging Go1.7's Subtests.
- [got](https://github.com/ysmood/got) [![GitHub stars](https://img.shields.io/github/stars/ysmood/got?style=flat)](https://github.com/ysmood/got/stargazers) - An enjoyable golang test framework.
- [gotest.tools](https://github.com/gotestyourself/gotest.tools) [![GitHub stars](https://img.shields.io/github/stars/gotestyourself/gotest.tools?style=flat)](https://github.com/gotestyourself/gotest.tools/stargazers) - A collection of packages to augment the go testing package and support common patterns.
- [Hamcrest](https://github.com/rdrdr/hamcrest) [![GitHub stars](https://img.shields.io/github/stars/rdrdr/hamcrest?style=flat)](https://github.com/rdrdr/hamcrest/stargazers) - fluent framework for declarative Matcher objects that, when applied to input values, produce self-describing results.
- [httper](https://github.com/gustofarbi/httper) [![GitHub stars](https://img.shields.io/github/stars/gustofarbi/httper?style=flat)](https://github.com/gustofarbi/httper/stargazers) - CLI runner for JetBrains .http files with scripting, assertions, gRPC, and load testing.
- [httpexpect](https://github.com/gavv/httpexpect) [![GitHub stars](https://img.shields.io/github/stars/gavv/httpexpect?style=flat)](https://github.com/gavv/httpexpect/stargazers) - Concise, declarative, and easy to use end-to-end HTTP and REST API testing.
- [is](https://github.com/matryer/is) [![GitHub stars](https://img.shields.io/github/stars/matryer/is?style=flat)](https://github.com/matryer/is/stargazers) - Professional lightweight testing mini-framework for Go.
- [jsonassert](https://github.com/kinbiko/jsonassert) [![GitHub stars](https://img.shields.io/github/stars/kinbiko/jsonassert?style=flat)](https://github.com/kinbiko/jsonassert/stargazers) - Package for verifying that your JSON payloads are serialized correctly.
- [keploy](https://github.com/keploy/keploy) [![GitHub stars](https://img.shields.io/github/stars/keploy/keploy?style=flat)](https://github.com/keploy/keploy/stargazers) - Generate Testcase and Data Mocks from API calls automatically.
- [omg.testingtools](https://github.com/dedalqq/omg.testingtools) [![GitHub stars](https://img.shields.io/github/stars/dedalqq/omg.testingtools?style=flat)](https://github.com/dedalqq/omg.testingtools/stargazers) - The simple library for change a values of private fields for testing.
- [restit](https://github.com/yookoala/restit) [![GitHub stars](https://img.shields.io/github/stars/yookoala/restit?style=flat)](https://github.com/yookoala/restit/stargazers) - Go micro framework to help writing RESTful API integration test.
- [schema](https://github.com/jgroeneveld/schema) [![GitHub stars](https://img.shields.io/github/stars/jgroeneveld/schema?style=flat)](https://github.com/jgroeneveld/schema/stargazers) - Quick and easy expression matching for JSON schemas used in requests and responses.
- [should](https://github.com/Kairum-Labs/should) [![GitHub stars](https://img.shields.io/github/stars/Kairum-Labs/should?style=flat)](https://github.com/Kairum-Labs/should/stargazers) - Testing library with zero dependencies, detailed struct diffs and human-readable error messages.
- [stop-and-go](https://github.com/elgohr/stop-and-go) [![GitHub stars](https://img.shields.io/github/stars/elgohr/stop-and-go?style=flat)](https://github.com/elgohr/stop-and-go/stargazers) - Testing helper for concurrency.
- [testcase](https://github.com/adamluzsi/testcase) [![GitHub stars](https://img.shields.io/github/stars/adamluzsi/testcase?style=flat)](https://github.com/adamluzsi/testcase/stargazers) - Idiomatic testing framework for Behavior Driven Development.
- [testcerts](https://github.com/madflojo/testcerts) [![GitHub stars](https://img.shields.io/github/stars/madflojo/testcerts?style=flat)](https://github.com/madflojo/testcerts/stargazers) - Dynamically generate self-signed certificates and certificate authorities within your test functions.
- [testcontainers-go](https://github.com/testcontainers/testcontainers-go) [![GitHub stars](https://img.shields.io/github/stars/testcontainers/testcontainers-go?style=flat)](https://github.com/testcontainers/testcontainers-go/stargazers) - A Go package that makes it simple to create and clean up container-based dependencies for automated integration/smoke tests. The clean, easy-to-use API enables developers to programmatically define containers that should be run as part of a test and clean up those resources when the test is done.
- [testfixtures](https://github.com/go-testfixtures/testfixtures) [![GitHub stars](https://img.shields.io/github/stars/go-testfixtures/testfixtures?style=flat)](https://github.com/go-testfixtures/testfixtures/stargazers) - A helper for Rails' like test fixtures to test database applications.
- [Testify](https://github.com/stretchr/testify) [![GitHub stars](https://img.shields.io/github/stars/stretchr/testify?style=flat)](https://github.com/stretchr/testify/stargazers) - Sacred extension to the standard go testing package.
- [Testo](https://github.com/ozontech/testo) [![GitHub stars](https://img.shields.io/github/stars/ozontech/testo?style=flat)](https://github.com/ozontech/testo/stargazers) - Plugin-based testing framework with suites, parallel tests, hooks and parametrization. Inspired by Pytest.
- [testsql](https://github.com/zhulongcheng/testsql) [![GitHub stars](https://img.shields.io/github/stars/zhulongcheng/testsql?style=flat)](https://github.com/zhulongcheng/testsql/stargazers) - Generate test data from SQL files before testing and clear it after finished.
- [testza](https://github.com/MarvinJWendt/testza) [![GitHub stars](https://img.shields.io/github/stars/MarvinJWendt/testza?style=flat)](https://github.com/MarvinJWendt/testza/stargazers) - Full-featured test framework with nice colorized output.
- [tparse](https://github.com/mfridman/tparse) [![GitHub stars](https://img.shields.io/github/stars/mfridman/tparse?style=flat)](https://github.com/mfridman/tparse/stargazers) - CLI tool for summarizing go test output. Pipe friendly. Compatible with go test flags.
- [trial](https://github.com/jgroeneveld/trial) [![GitHub stars](https://img.shields.io/github/stars/jgroeneveld/trial?style=flat)](https://github.com/jgroeneveld/trial/stargazers) - Quick and easy extendable assertions without introducing much boilerplate.
- [Tt](https://github.com/vcaesar/tt) [![GitHub stars](https://img.shields.io/github/stars/vcaesar/tt?style=flat)](https://github.com/vcaesar/tt/stargazers) - Simple and colorful test tools.
- [wstest](https://github.com/posener/wstest) [![GitHub stars](https://img.shields.io/github/stars/posener/wstest?style=flat)](https://github.com/posener/wstest/stargazers) - Websocket client for unit-testing a websocket http.Handler.

### Mock

- [counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) [![GitHub stars](https://img.shields.io/github/stars/maxbrunsfeld/counterfeiter?style=flat)](https://github.com/maxbrunsfeld/counterfeiter/stargazers) - Tool for generating self-contained mock objects.
- [genmock](https://gitlab.com/so_literate/genmock) - Go mocking system with code generator for building calls of the interface methods.
- [go-localstack](https://github.com/elgohr/go-localstack) [![GitHub stars](https://img.shields.io/github/stars/elgohr/go-localstack?style=flat)](https://github.com/elgohr/go-localstack/stargazers) - Tool for using localstack in AWS testing.
- [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) [![GitHub stars](https://img.shields.io/github/stars/DATA-DOG/go-sqlmock?style=flat)](https://github.com/DATA-DOG/go-sqlmock/stargazers) - Mock SQL driver for testing database interactions.
- [go-txdb](https://github.com/DATA-DOG/go-txdb) [![GitHub stars](https://img.shields.io/github/stars/DATA-DOG/go-txdb?style=flat)](https://github.com/DATA-DOG/go-txdb/stargazers) - Single transaction based database driver mainly for testing purposes.
- [gomock](https://github.com/uber-go/mock) [![GitHub stars](https://img.shields.io/github/stars/uber-go/mock?style=flat)](https://github.com/uber-go/mock/stargazers) - Mocking framework for the Go programming language.
- [gomock](https://github.com/vibridi/gomock) [![GitHub stars](https://img.shields.io/github/stars/vibridi/gomock?style=flat)](https://github.com/vibridi/gomock/stargazers) - CLI tool to generate typed and framework-agnostic interface mocks, with support for generics.
- [govcr](https://github.com/seborama/govcr) [![GitHub stars](https://img.shields.io/github/stars/seborama/govcr?style=flat)](https://github.com/seborama/govcr/stargazers) - HTTP mock for Golang: record and replay HTTP interactions for offline testing.
- [hoverfly](https://github.com/SpectoLabs/hoverfly) [![GitHub stars](https://img.shields.io/github/stars/SpectoLabs/hoverfly?style=flat)](https://github.com/SpectoLabs/hoverfly/stargazers) - HTTP(S) proxy for recording and simulating REST/SOAP APIs with extensible middleware and easy-to-use CLI.
- [httpmock](https://github.com/jarcoal/httpmock) [![GitHub stars](https://img.shields.io/github/stars/jarcoal/httpmock?style=flat)](https://github.com/jarcoal/httpmock/stargazers) - Easy mocking of HTTP responses from external resources.
- [minimock](https://github.com/gojuno/minimock) [![GitHub stars](https://img.shields.io/github/stars/gojuno/minimock?style=flat)](https://github.com/gojuno/minimock/stargazers) - Mock generator for Go interfaces.
- [mockery](https://github.com/vektra/mockery) [![GitHub stars](https://img.shields.io/github/stars/vektra/mockery?style=flat)](https://github.com/vektra/mockery/stargazers) - Tool to generate Go interfaces.
- [mockfs](https://github.com/balinomad/go-mockfs) [![GitHub stars](https://img.shields.io/github/stars/balinomad/go-mockfs?style=flat)](https://github.com/balinomad/go-mockfs/stargazers) - Mock filesystem for Go testing with error injection and latency simulation, built on `testing/fstest.MapFS`.
- [mockhttp](https://github.com/tv42/mockhttp) [![GitHub stars](https://img.shields.io/github/stars/tv42/mockhttp?style=flat)](https://github.com/tv42/mockhttp/stargazers) - Mock object for Go http.ResponseWriter.
- [mooncake](https://github.com/GuilhermeCaruso/mooncake) [![GitHub stars](https://img.shields.io/github/stars/GuilhermeCaruso/mooncake?style=flat)](https://github.com/GuilhermeCaruso/mooncake/stargazers) - A simple way to generate mocks for multiple purposes.
- [moq](https://github.com/matryer/moq) [![GitHub stars](https://img.shields.io/github/stars/matryer/moq?style=flat)](https://github.com/matryer/moq/stargazers) - Utility that generates a struct from any interface. The struct can be used in test code as a mock of the interface.
- [moxie](https://lesiw.io/moxie) - Generate mock methods on embedded structs.
- [pgxmock](https://github.com/pashagolub/pgxmock) [![GitHub stars](https://img.shields.io/github/stars/pashagolub/pgxmock?style=flat)](https://github.com/pashagolub/pgxmock/stargazers) - A mock library implementing [pgx - PostgreSQL Driver and Toolkit](https://github.com/jackc/pgx/) [![GitHub stars](https://img.shields.io/github/stars/jackc/pgx/?style=flat)](https://github.com/jackc/pgx//stargazers).
- [timex](https://github.com/cabify/timex) [![GitHub stars](https://img.shields.io/github/stars/cabify/timex?style=flat)](https://github.com/cabify/timex/stargazers) - A test-friendly replacement for the native `time` package.
- [xgo](https://github.com/xhd2015/xgo) [![GitHub stars](https://img.shields.io/github/stars/xhd2015/xgo?style=flat)](https://github.com/xhd2015/xgo/stargazers) - A general pureposed function mocking library.

### Fuzzing and delta-debugging/reducing/shrinking

- [go-fuzz](https://github.com/dvyukov/go-fuzz) [![GitHub stars](https://img.shields.io/github/stars/dvyukov/go-fuzz?style=flat)](https://github.com/dvyukov/go-fuzz/stargazers) - Randomized testing system.
- [Tavor](https://github.com/zimmski/tavor) [![GitHub stars](https://img.shields.io/github/stars/zimmski/tavor?style=flat)](https://github.com/zimmski/tavor/stargazers) - Generic fuzzing and delta-debugging framework.

### Selenium and browser control tools

- [bonk](https://github.com/joakimcarlsson/bonk) [![GitHub stars](https://img.shields.io/github/stars/joakimcarlsson/bonk?style=flat)](https://github.com/joakimcarlsson/bonk/stargazers) - Fast, stealth-first browser automation library using Chrome DevTools Protocol over WebSocket with no external dependencies.
- [cdp](https://github.com/mafredri/cdp) [![GitHub stars](https://img.shields.io/github/stars/mafredri/cdp?style=flat)](https://github.com/mafredri/cdp/stargazers) - Type-safe bindings for the Chrome Debugging Protocol that can be used with browsers or other debug targets that implement it.
- [chromedp](https://github.com/knq/chromedp) [![GitHub stars](https://img.shields.io/github/stars/knq/chromedp?style=flat)](https://github.com/knq/chromedp/stargazers) - a way to drive/test Chrome, Safari, Edge, Android Webviews, and other browsers supporting the Chrome Debugging Protocol.
- [playwright-go](https://github.com/mxschmitt/playwright-go) [![GitHub stars](https://img.shields.io/github/stars/mxschmitt/playwright-go?style=flat)](https://github.com/mxschmitt/playwright-go/stargazers) - browser automation library to control Chromium, Firefox and WebKit with a single API.
- [rod](https://github.com/go-rod/rod) [![GitHub stars](https://img.shields.io/github/stars/go-rod/rod?style=flat)](https://github.com/go-rod/rod/stargazers) - A Devtools driver to make web automation and scraping easy.
- [selenosis](https://github.com/alcounit/selenosis) [![GitHub stars](https://img.shields.io/github/stars/alcounit/selenosis?style=flat)](https://github.com/alcounit/selenosis/stargazers) - Stateless Kubernetes-native hub that routes Selenium, Playwright, and MCP sessions to on-demand browser pods via custom resources.

### Fail injection

- [failpoint](https://github.com/pingcap/failpoint) [![GitHub stars](https://img.shields.io/github/stars/pingcap/failpoint?style=flat)](https://github.com/pingcap/failpoint/stargazers) - An implementation of [failpoints](https://www.freebsd.org/cgi/man.cgi?query=fail) for Golang.

**[⬆ back to top](#contents)**

## Text Processing

_Libraries for parsing and manipulating texts._

See also [Natural Language Processing](#natural-language-processing) and [Text Analysis](#text-analysis).

### Formatters

- [address](https://github.com/bojanz/address) [![GitHub stars](https://img.shields.io/github/stars/bojanz/address?style=flat)](https://github.com/bojanz/address/stargazers) - Handles address representation, validation and formatting.
- [align](https://github.com/Guitarbum722/align) [![GitHub stars](https://img.shields.io/github/stars/Guitarbum722/align?style=flat)](https://github.com/Guitarbum722/align/stargazers) - A general purpose application that aligns text.
- [bytes](https://github.com/labstack/gommon/tree/master/bytes) [![GitHub stars](https://img.shields.io/github/stars/labstack/gommon/tree/master/bytes?style=flat)](https://github.com/labstack/gommon/tree/master/bytes/stargazers) - Formats and parses numeric byte values (10K, 2M, 3G, etc.).
- [go-fixedwidth](https://github.com/ianlopshire/go-fixedwidth) [![GitHub stars](https://img.shields.io/github/stars/ianlopshire/go-fixedwidth?style=flat)](https://github.com/ianlopshire/go-fixedwidth/stargazers) - Fixed-width text formatting (encoder/decoder with reflection).
- [go-humanize](https://github.com/dustin/go-humanize) [![GitHub stars](https://img.shields.io/github/stars/dustin/go-humanize?style=flat)](https://github.com/dustin/go-humanize/stargazers) - Formatters for time, numbers, and memory size to human readable format.
- [gotabulate](https://github.com/bndr/gotabulate) [![GitHub stars](https://img.shields.io/github/stars/bndr/gotabulate?style=flat)](https://github.com/bndr/gotabulate/stargazers) - Easily pretty-print your tabular data with Go.
- [sq](https://github.com/neilotoole/sq) [![GitHub stars](https://img.shields.io/github/stars/neilotoole/sq?style=flat)](https://github.com/neilotoole/sq/stargazers) - Convert data from SQL databases or document formats like CSV or Excel into formats such as JSON, Excel, CSV, HTML, Markdown, XML, and YAML.
- [textwrap](https://github.com/isbm/textwrap) [![GitHub stars](https://img.shields.io/github/stars/isbm/textwrap?style=flat)](https://github.com/isbm/textwrap/stargazers) - Wraps text at end of lines. Implementation of `textwrap` module from Python.

### Markup Languages

- [bafi](https://github.com/mmalcek/bafi) [![GitHub stars](https://img.shields.io/github/stars/mmalcek/bafi?style=flat)](https://github.com/mmalcek/bafi/stargazers) - Universal JSON, BSON, YAML, XML translator to ANY format using templates.
- [bbConvert](https://github.com/CalebQ42/bbConvert) [![GitHub stars](https://img.shields.io/github/stars/CalebQ42/bbConvert?style=flat)](https://github.com/CalebQ42/bbConvert/stargazers) - Converts bbCode to HTML that allows you to add support for custom bbCode tags.
- [blackfriday](https://github.com/russross/blackfriday) [![GitHub stars](https://img.shields.io/github/stars/russross/blackfriday?style=flat)](https://github.com/russross/blackfriday/stargazers) - Markdown processor in Go.
- [go-output-format](https://github.com/drewstinnett/go-output-format) [![GitHub stars](https://img.shields.io/github/stars/drewstinnett/go-output-format?style=flat)](https://github.com/drewstinnett/go-output-format/stargazers) - Output go structures into multiple formats (YAML/JSON/etc) in your command line app.
- [go-toml](https://github.com/pelletier/go-toml) [![GitHub stars](https://img.shields.io/github/stars/pelletier/go-toml?style=flat)](https://github.com/pelletier/go-toml/stargazers) - Go library for the TOML format with query support and handy cli tools.
- [goldmark](https://github.com/yuin/goldmark) [![GitHub stars](https://img.shields.io/github/stars/yuin/goldmark?style=flat)](https://github.com/yuin/goldmark/stargazers) - A Markdown parser written in Go. Easy to extend, standard (CommonMark) compliant, well structured.
- [goq](https://github.com/andrewstuart/goq) [![GitHub stars](https://img.shields.io/github/stars/andrewstuart/goq?style=flat)](https://github.com/andrewstuart/goq/stargazers) - Declarative unmarshalling of HTML using struct tags with jQuery syntax (uses GoQuery).
- [html-to-markdown](https://github.com/JohannesKaufmann/html-to-markdown) [![GitHub stars](https://img.shields.io/github/stars/JohannesKaufmann/html-to-markdown?style=flat)](https://github.com/JohannesKaufmann/html-to-markdown/stargazers) - Convert HTML to Markdown. Even works with entire websites and can be extended through rules.
- [htmlquery](https://github.com/antchfx/htmlquery) [![GitHub stars](https://img.shields.io/github/stars/antchfx/htmlquery?style=flat)](https://github.com/antchfx/htmlquery/stargazers) - An XPath query package for HTML, lets you extract data or evaluate from HTML documents by an XPath expression.
- [htmlyaml](https://github.com/nikolaydubina/htmlyaml) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/htmlyaml?style=flat)](https://github.com/nikolaydubina/htmlyaml/stargazers) - Rich rendering of YAML as HTML in Go.
- [htree](https://github.com/bobg/htree) [![GitHub stars](https://img.shields.io/github/stars/bobg/htree?style=flat)](https://github.com/bobg/htree/stargazers) - Traverse, navigate, filter, and otherwise process trees of [html.Node](https://pkg.go.dev/golang.org/x/net/html#Node) objects.
- [mdsmith](https://github.com/jeduden/mdsmith) [![GitHub stars](https://img.shields.io/github/stars/jeduden/mdsmith?style=flat)](https://github.com/jeduden/mdsmith/stargazers) - fast, auto-fixing Markdown linter and formatter. Checks style, readability, structure, and cross-file integrity.
- [mxj](https://github.com/clbanning/mxj) [![GitHub stars](https://img.shields.io/github/stars/clbanning/mxj?style=flat)](https://github.com/clbanning/mxj/stargazers) - Encode / decode XML as JSON or map[string]interface{}; extract values with dot-notation paths and wildcards. Replaces x2j and j2x packages.
- [picoloom](https://github.com/alnah/picoloom) [![GitHub stars](https://img.shields.io/github/stars/alnah/picoloom?style=flat)](https://github.com/alnah/picoloom/stargazers) - Markdown-to-PDF converter with CLI and Go library APIs.
- [toml](https://github.com/BurntSushi/toml) [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/toml?style=flat)](https://github.com/BurntSushi/toml/stargazers) - TOML configuration format (encoder/decoder with reflection).

### Parsers/Encoders/Decoders

- [allot](https://github.com/sbstjn/allot) [![GitHub stars](https://img.shields.io/github/stars/sbstjn/allot?style=flat)](https://github.com/sbstjn/allot/stargazers) - Placeholder and wildcard text parsing for CLI tools and bots.
- [codetree](https://github.com/aerogo/codetree) [![GitHub stars](https://img.shields.io/github/stars/aerogo/codetree?style=flat)](https://github.com/aerogo/codetree/stargazers) - Parses indented code (python, pixy, scarlet, etc.) and returns a tree structure.
- [commonregex](https://github.com/mingrammer/commonregex) [![GitHub stars](https://img.shields.io/github/stars/mingrammer/commonregex?style=flat)](https://github.com/mingrammer/commonregex/stargazers) - A collection of common regular expressions for Go.
- [did](https://github.com/ockam-network/did) [![GitHub stars](https://img.shields.io/github/stars/ockam-network/did?style=flat)](https://github.com/ockam-network/did/stargazers) - DID (Decentralized Identifiers) Parser and Stringer in Go.
- [doi](https://github.com/hscells/doi) [![GitHub stars](https://img.shields.io/github/stars/hscells/doi?style=flat)](https://github.com/hscells/doi/stargazers) - Document object identifier (doi) parser in Go.
- [editorconfig-core-go](https://github.com/editorconfig/editorconfig-core-go) [![GitHub stars](https://img.shields.io/github/stars/editorconfig/editorconfig-core-go?style=flat)](https://github.com/editorconfig/editorconfig-core-go/stargazers) - Editorconfig file parser and manipulator for Go.
- [go-fasttld](https://github.com/elliotwutingfeng/go-fasttld) [![GitHub stars](https://img.shields.io/github/stars/elliotwutingfeng/go-fasttld?style=flat)](https://github.com/elliotwutingfeng/go-fasttld/stargazers) - High performance effective top level domains (eTLD) extraction module.
- [go-nmea](https://github.com/adrianmo/go-nmea) [![GitHub stars](https://img.shields.io/github/stars/adrianmo/go-nmea?style=flat)](https://github.com/adrianmo/go-nmea/stargazers) - NMEA parser library for the Go language.
- [go-querystring](https://github.com/google/go-querystring) [![GitHub stars](https://img.shields.io/github/stars/google/go-querystring?style=flat)](https://github.com/google/go-querystring/stargazers) - Go library for encoding structs into URL query parameters.
- [go-vcard](https://github.com/emersion/go-vcard) [![GitHub stars](https://img.shields.io/github/stars/emersion/go-vcard?style=flat)](https://github.com/emersion/go-vcard/stargazers) - Parse and format vCard.
- [godump](https://github.com/yassinebenaid/godump) [![GitHub stars](https://img.shields.io/github/stars/yassinebenaid/godump?style=flat)](https://github.com/yassinebenaid/godump/stargazers) - Pretty print any GO variable with ease, an alternative to Go's `fmt.Printf("%#v")`.
- [godump (goforj)](https://github.com/goforj/godump) [![GitHub stars](https://img.shields.io/github/stars/goforj/godump?style=flat)](https://github.com/goforj/godump/stargazers) - Pretty-print Go structs with Laravel/Symfony-style dumps, full type info, colorized CLI output, cycle detection, and private field access.
- [gofeed](https://github.com/mmcdole/gofeed) [![GitHub stars](https://img.shields.io/github/stars/mmcdole/gofeed?style=flat)](https://github.com/mmcdole/gofeed/stargazers) - Parse RSS and Atom feeds in Go.
- [gographviz](https://github.com/awalterschulze/gographviz) [![GitHub stars](https://img.shields.io/github/stars/awalterschulze/gographviz?style=flat)](https://github.com/awalterschulze/gographviz/stargazers) - Parses the Graphviz DOT language.
- [gonameparts](https://github.com/polera/gonameparts) [![GitHub stars](https://img.shields.io/github/stars/polera/gonameparts?style=flat)](https://github.com/polera/gonameparts/stargazers) - Parses human names into individual name parts.
- [ltsv](https://github.com/Wing924/ltsv) [![GitHub stars](https://img.shields.io/github/stars/Wing924/ltsv?style=flat)](https://github.com/Wing924/ltsv/stargazers) - High performance [LTSV (Labeled Tab Separated Value)](http://ltsv.org/) reader for Go.
- [normalize](https://github.com/avito-tech/normalize) [![GitHub stars](https://img.shields.io/github/stars/avito-tech/normalize?style=flat)](https://github.com/avito-tech/normalize/stargazers) - Sanitize, normalize and compare fuzzy text.
- [parseargs-go](https://github.com/nproc/parseargs-go) [![GitHub stars](https://img.shields.io/github/stars/nproc/parseargs-go?style=flat)](https://github.com/nproc/parseargs-go/stargazers) - string argument parser that understands quotes and backslashes.
- [prattle](https://github.com/askeladdk/prattle) [![GitHub stars](https://img.shields.io/github/stars/askeladdk/prattle?style=flat)](https://github.com/askeladdk/prattle/stargazers) - Scan and parse LL(1) grammars simply and efficiently.
- [sh](https://github.com/mvdan/sh) [![GitHub stars](https://img.shields.io/github/stars/mvdan/sh?style=flat)](https://github.com/mvdan/sh/stargazers) - Shell parser and formatter.
- [tokenizer](https://github.com/bzick/tokenizer) [![GitHub stars](https://img.shields.io/github/stars/bzick/tokenizer?style=flat)](https://github.com/bzick/tokenizer/stargazers) - Parse any string, slice or infinite buffer to any tokens.
- [vdf](https://github.com/andygrunwald/vdf) [![GitHub stars](https://img.shields.io/github/stars/andygrunwald/vdf?style=flat)](https://github.com/andygrunwald/vdf/stargazers) - A Lexer and Parser for Valves Data Format (known as vdf) written in Go.
- [when](https://github.com/olebedev/when) [![GitHub stars](https://img.shields.io/github/stars/olebedev/when?style=flat)](https://github.com/olebedev/when/stargazers) - Natural EN and RU language date/time parser with pluggable rules.
- [xj2go](https://github.com/stackerzzq/xj2go) [![GitHub stars](https://img.shields.io/github/stars/stackerzzq/xj2go?style=flat)](https://github.com/stackerzzq/xj2go/stargazers) - Convert xml or json to go struct.

### Regular Expressions

- [coregex](https://github.com/coregx/coregex) [![GitHub stars](https://img.shields.io/github/stars/coregx/coregex?style=flat)](https://github.com/coregx/coregex/stargazers) - Production regex engine with Rust regex-crate architecture: multi-engine DFA/NFA, SIMD prefilters, drop-in stdlib replacement.
- [genex](https://github.com/alixaxel/genex) [![GitHub stars](https://img.shields.io/github/stars/alixaxel/genex?style=flat)](https://github.com/alixaxel/genex/stargazers) - Count and expand Regular Expressions into all matching Strings.
- [go-wildcard](https://github.com/IGLOU-EU/go-wildcard) [![GitHub stars](https://img.shields.io/github/stars/IGLOU-EU/go-wildcard?style=flat)](https://github.com/IGLOU-EU/go-wildcard/stargazers) - Simple and lightweight wildcard pattern matching.
- [goregen](https://github.com/zach-klippenstein/goregen) [![GitHub stars](https://img.shields.io/github/stars/zach-klippenstein/goregen?style=flat)](https://github.com/zach-klippenstein/goregen/stargazers) - Library for generating random strings from regular expressions.
- [regroup](https://github.com/oriser/regroup) [![GitHub stars](https://img.shields.io/github/stars/oriser/regroup?style=flat)](https://github.com/oriser/regroup/stargazers) - Match regex expression named groups into go struct using struct tags and automatic parsing.
- [rex](https://github.com/hedhyw/rex) [![GitHub stars](https://img.shields.io/github/stars/hedhyw/rex?style=flat)](https://github.com/hedhyw/rex/stargazers) - Regular expressions builder.

### Sanitation

- [bluemonday](https://github.com/microcosm-cc/bluemonday) [![GitHub stars](https://img.shields.io/github/stars/microcosm-cc/bluemonday?style=flat)](https://github.com/microcosm-cc/bluemonday/stargazers) - HTML Sanitizer.
- [gofuckyourself](https://github.com/JoshuaDoes/gofuckyourself) [![GitHub stars](https://img.shields.io/github/stars/JoshuaDoes/gofuckyourself?style=flat)](https://github.com/JoshuaDoes/gofuckyourself/stargazers) - A sanitization-based swear filter for Go.

### Scrapers

- [colly](https://github.com/asciimoo/colly) [![GitHub stars](https://img.shields.io/github/stars/asciimoo/colly?style=flat)](https://github.com/asciimoo/colly/stargazers) - Fast and Elegant Scraping Framework for Gophers.
- [dataflowkit](https://github.com/slotix/dataflowkit) [![GitHub stars](https://img.shields.io/github/stars/slotix/dataflowkit?style=flat)](https://github.com/slotix/dataflowkit/stargazers) - Web scraping Framework to turn websites into structured data.
- [go-recipe](https://github.com/kkyr/go-recipe) [![GitHub stars](https://img.shields.io/github/stars/kkyr/go-recipe?style=flat)](https://github.com/kkyr/go-recipe/stargazers) - A package for scraping recipes from websites.
- [go-sitemap-parser](https://github.com/aafeher/go-sitemap-parser) [![GitHub stars](https://img.shields.io/github/stars/aafeher/go-sitemap-parser?style=flat)](https://github.com/aafeher/go-sitemap-parser/stargazers) - Go language library for parsing Sitemaps.
- [GoQuery](https://github.com/PuerkitoBio/goquery) [![GitHub stars](https://img.shields.io/github/stars/PuerkitoBio/goquery?style=flat)](https://github.com/PuerkitoBio/goquery/stargazers) - GoQuery brings a syntax and a set of features similar to jQuery to the Go language.
- [pagser](https://github.com/foolin/pagser) [![GitHub stars](https://img.shields.io/github/stars/foolin/pagser?style=flat)](https://github.com/foolin/pagser/stargazers) - Pagser is a simple, extensible, configurable parse and deserialize html page to struct based on goquery and struct tags for golang crawler.
- [Tagify](https://github.com/zoomio/tagify) [![GitHub stars](https://img.shields.io/github/stars/zoomio/tagify?style=flat)](https://github.com/zoomio/tagify/stargazers) - Produces a set of tags from given source.
- [walker](https://github.com/cyucelen/walker) [![GitHub stars](https://img.shields.io/github/stars/cyucelen/walker?style=flat)](https://github.com/cyucelen/walker/stargazers) - Seamlessly fetch paginated data from any source. Simple and high performance API scraping included.
- [xurls](https://github.com/mvdan/xurls) [![GitHub stars](https://img.shields.io/github/stars/mvdan/xurls?style=flat)](https://github.com/mvdan/xurls/stargazers) - Extract urls from text.

### RSS

- [podcast](https://github.com/eduncan911/podcast) [![GitHub stars](https://img.shields.io/github/stars/eduncan911/podcast?style=flat)](https://github.com/eduncan911/podcast/stargazers) - iTunes Compliant and RSS 2.0 Podcast Generator in Golang

### Utility/Miscellaneous

- [ahocorasick](https://github.com/coregx/ahocorasick) [![GitHub stars](https://img.shields.io/github/stars/coregx/ahocorasick?style=flat)](https://github.com/coregx/ahocorasick/stargazers) - High-performance Aho-Corasick multi-pattern string matching with DFA compilation and SIMD prefilter, up to 7 GB/s throughput (part of [coregx](https://github.com/coregx) [![GitHub stars](https://img.shields.io/github/stars/coregx?style=flat)](https://github.com/coregx/stargazers) ecosystem).
- [go-runewidth](https://github.com/mattn/go-runewidth) [![GitHub stars](https://img.shields.io/github/stars/mattn/go-runewidth?style=flat)](https://github.com/mattn/go-runewidth/stargazers) - Functions to get fixed width of the character or string.
- [kace](https://github.com/codemodus/kace) [![GitHub stars](https://img.shields.io/github/stars/codemodus/kace?style=flat)](https://github.com/codemodus/kace/stargazers) - Common case conversions covering common initialisms.
- [lancet](https://github.com/duke-git/lancet) [![GitHub stars](https://img.shields.io/github/stars/duke-git/lancet?style=flat)](https://github.com/duke-git/lancet/stargazers) - A comprehensive, Lodash-like utility library for Go
- [petrovich](https://github.com/striker2000/petrovich) [![GitHub stars](https://img.shields.io/github/stars/striker2000/petrovich?style=flat)](https://github.com/striker2000/petrovich/stargazers) - Petrovich is the library which inflects Russian names to given grammatical case.
- [radix](https://github.com/yourbasic/radix) [![GitHub stars](https://img.shields.io/github/stars/yourbasic/radix?style=flat)](https://github.com/yourbasic/radix/stargazers) - Fast string sorting algorithm.
- [TySug](https://github.com/Dynom/TySug) [![GitHub stars](https://img.shields.io/github/stars/Dynom/TySug?style=flat)](https://github.com/Dynom/TySug/stargazers) - Alternative suggestions with respect to keyboard layouts.
- [uniwidth](https://github.com/unilibs/uniwidth) [![GitHub stars](https://img.shields.io/github/stars/unilibs/uniwidth?style=flat)](https://github.com/unilibs/uniwidth/stargazers) - High-performance Unicode character width calculation with SWAR optimization, O(1) lookup tables, and ZWJ emoji support.
- [w2vgrep](https://github.com/arunsupe/semantic-grep) [![GitHub stars](https://img.shields.io/github/stars/arunsupe/semantic-grep?style=flat)](https://github.com/arunsupe/semantic-grep/stargazers) - A semantic grep tool using word embeddings to find semantically similar matches. For example, searching for "death" will find "dead", "killing", "murder".

**[⬆ back to top](#contents)**

## Third-party APIs

_Libraries for accessing third party APIs._

- [airtable](https://github.com/mehanizm/airtable) [![GitHub stars](https://img.shields.io/github/stars/mehanizm/airtable?style=flat)](https://github.com/mehanizm/airtable/stargazers) - Go client library for the [Airtable API](https://airtable.com/api).
- [anaconda](https://github.com/ChimeraCoder/anaconda) [![GitHub stars](https://img.shields.io/github/stars/ChimeraCoder/anaconda?style=flat)](https://github.com/ChimeraCoder/anaconda/stargazers) - Go client library for the Twitter 1.1 API.
- [appstore-sdk-go](https://github.com/Kachit/appstore-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/Kachit/appstore-sdk-go?style=flat)](https://github.com/Kachit/appstore-sdk-go/stargazers) - Unofficial Golang SDK for AppStore Connect API.
- [aws-encryption-sdk-go](https://github.com/chainifynet/aws-encryption-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/chainifynet/aws-encryption-sdk-go?style=flat)](https://github.com/chainifynet/aws-encryption-sdk-go/stargazers) - Unofficial Go SDK implementation of the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/index.html).
- [aws-sdk-go](https://github.com/aws/aws-sdk-go-v2) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-go-v2?style=flat)](https://github.com/aws/aws-sdk-go-v2/stargazers) - The official AWS SDK for the Go programming language.
- [bqwriter](https://github.com/OTA-Insight/bqwriter) [![GitHub stars](https://img.shields.io/github/stars/OTA-Insight/bqwriter?style=flat)](https://github.com/OTA-Insight/bqwriter/stargazers) - High Level Go Library to write data into [Google BigQuery](https://cloud.google.com/bigquery) at a high throughout.
- [brewerydb](https://github.com/naegelejd/brewerydb) [![GitHub stars](https://img.shields.io/github/stars/naegelejd/brewerydb?style=flat)](https://github.com/naegelejd/brewerydb/stargazers) - Go library for accessing the BreweryDB API.
- [cachet](https://github.com/andygrunwald/cachet) [![GitHub stars](https://img.shields.io/github/stars/andygrunwald/cachet?style=flat)](https://github.com/andygrunwald/cachet/stargazers) - Go client library for [Cachet (open source status page system)](https://cachethq.io/).
- [circleci](https://github.com/jszwedko/go-circleci) [![GitHub stars](https://img.shields.io/github/stars/jszwedko/go-circleci?style=flat)](https://github.com/jszwedko/go-circleci/stargazers) - Go client library for interacting with CircleCI's API.
- [codeship-go](https://github.com/codeship/codeship-go) [![GitHub stars](https://img.shields.io/github/stars/codeship/codeship-go?style=flat)](https://github.com/codeship/codeship-go/stargazers) - Go client library for interacting with Codeship's API v2.
- [coinpaprika-go](https://github.com/coinpaprika/coinpaprika-api-go-client) [![GitHub stars](https://img.shields.io/github/stars/coinpaprika/coinpaprika-api-go-client?style=flat)](https://github.com/coinpaprika/coinpaprika-api-go-client/stargazers) - Go client library for interacting with Coinpaprika's API.
- [colony-sdk-go](https://github.com/TheColonyCC/colony-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/TheColonyCC/colony-sdk-go?style=flat)](https://github.com/TheColonyCC/colony-sdk-go/stargazers) - Go client library for [The Colony](https://thecolony.cc) — a public social network whose users are AI agents.
- [device-check-go](https://github.com/rinchsan/device-check-go) [![GitHub stars](https://img.shields.io/github/stars/rinchsan/device-check-go?style=flat)](https://github.com/rinchsan/device-check-go/stargazers) - Go client library for interacting with [iOS DeviceCheck API](https://developer.apple.com/documentation/devicecheck) v1.
- [discordgo](https://github.com/bwmarrin/discordgo) [![GitHub stars](https://img.shields.io/github/stars/bwmarrin/discordgo?style=flat)](https://github.com/bwmarrin/discordgo/stargazers) - Go bindings for the Discord Chat API.
- [disgo](https://github.com/switchupcb/disgo) [![GitHub stars](https://img.shields.io/github/stars/switchupcb/disgo?style=flat)](https://github.com/switchupcb/disgo/stargazers) - Go API Wrapper for the Discord API.
- [dusupay-sdk-go](https://github.com/Kachit/dusupay-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/Kachit/dusupay-sdk-go?style=flat)](https://github.com/Kachit/dusupay-sdk-go/stargazers) - Unofficial Dusupay payment gateway API Client for Go
- [ethrpc](https://github.com/onrik/ethrpc) [![GitHub stars](https://img.shields.io/github/stars/onrik/ethrpc?style=flat)](https://github.com/onrik/ethrpc/stargazers) - Go bindings for Ethereum JSON RPC API.
- [facebook](https://github.com/huandu/facebook) [![GitHub stars](https://img.shields.io/github/stars/huandu/facebook?style=flat)](https://github.com/huandu/facebook/stargazers) - Go Library that supports the Facebook Graph API.
- [fasapay-sdk-go](https://github.com/Kachit/fasapay-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/Kachit/fasapay-sdk-go?style=flat)](https://github.com/Kachit/fasapay-sdk-go/stargazers) - Unofficial Fasapay payment gateway XML API Client for Golang.
- [fcm](https://github.com/maddevsio/fcm) [![GitHub stars](https://img.shields.io/github/stars/maddevsio/fcm?style=flat)](https://github.com/maddevsio/fcm/stargazers) - Go library for Firebase Cloud Messaging.
- [gads](https://github.com/emiddleton/gads) [![GitHub stars](https://img.shields.io/github/stars/emiddleton/gads?style=flat)](https://github.com/emiddleton/gads/stargazers) - Google Adwords Unofficial API.
- [gcm](https://github.com/Aorioli/gcm) [![GitHub stars](https://img.shields.io/github/stars/Aorioli/gcm?style=flat)](https://github.com/Aorioli/gcm/stargazers) - Go library for Google Cloud Messaging.
- [geo-golang](https://github.com/codingsince1985/geo-golang) [![GitHub stars](https://img.shields.io/github/stars/codingsince1985/geo-golang?style=flat)](https://github.com/codingsince1985/geo-golang/stargazers) - Go Library to access [Google Maps](https://developers.google.com/maps/documentation/geocoding/intro), [MapQuest](https://developer.mapquest.com/documentation/api/geocoding/), [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/), [OpenCage](https://opencagedata.com/api), [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx), [Mapbox](https://www.mapbox.com/developers/api/geocoding/), and [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Nominatim) geocoding / reverse geocoding APIs.
- [github](https://github.com/google/go-github) [![GitHub stars](https://img.shields.io/github/stars/google/go-github?style=flat)](https://github.com/google/go-github/stargazers) - Go library for accessing the GitHub REST API v3.
- [githubql](https://github.com/shurcooL/githubql) [![GitHub stars](https://img.shields.io/github/stars/shurcooL/githubql?style=flat)](https://github.com/shurcooL/githubql/stargazers) - Go library for accessing the GitHub GraphQL API v4.
- [go-atlassian](https://github.com/ctreminiom/go-atlassian) [![GitHub stars](https://img.shields.io/github/stars/ctreminiom/go-atlassian?style=flat)](https://github.com/ctreminiom/go-atlassian/stargazers) - Go library for accessing the [Atlassian Cloud](https://www.atlassian.com/enterprise/cloud) services (Jira, Jira Service Management, Jira Agile, Confluence, Admin Cloud)
- [go-aws-news](https://github.com/circa10a/go-aws-news) [![GitHub stars](https://img.shields.io/github/stars/circa10a/go-aws-news?style=flat)](https://github.com/circa10a/go-aws-news/stargazers) - Go application and library to fetch what's new from AWS.
- [go-chronos](https://github.com/axelspringer/go-chronos) [![GitHub stars](https://img.shields.io/github/stars/axelspringer/go-chronos?style=flat)](https://github.com/axelspringer/go-chronos/stargazers) - Go library for interacting with the [Chronos](https://mesos.github.io/chronos/) Job Scheduler
- [go-gerrit](https://github.com/andygrunwald/go-gerrit) [![GitHub stars](https://img.shields.io/github/stars/andygrunwald/go-gerrit?style=flat)](https://github.com/andygrunwald/go-gerrit/stargazers) - Go client library for [Gerrit Code Review](https://www.gerritcodereview.com/).
- [go-hacknews](https://github.com/PaulRosset/go-hacknews) [![GitHub stars](https://img.shields.io/github/stars/PaulRosset/go-hacknews?style=flat)](https://github.com/PaulRosset/go-hacknews/stargazers) - Tiny Go client for HackerNews API.
- [go-here](https://github.com/abdullahselek/go-here) [![GitHub stars](https://img.shields.io/github/stars/abdullahselek/go-here?style=flat)](https://github.com/abdullahselek/go-here/stargazers) - Go client library around the HERE location based APIs.
- [go-hibp](https://github.com/wneessen/go-hibp) [![GitHub stars](https://img.shields.io/github/stars/wneessen/go-hibp?style=flat)](https://github.com/wneessen/go-hibp/stargazers) - Simple Go binding to the "Have I Been Pwned" APIs.
- [go-imgur](https://github.com/koffeinsource/go-imgur) [![GitHub stars](https://img.shields.io/github/stars/koffeinsource/go-imgur?style=flat)](https://github.com/koffeinsource/go-imgur/stargazers) - Go client library for [imgur](https://imgur.com)
- [go-jira](https://github.com/andygrunwald/go-jira) [![GitHub stars](https://img.shields.io/github/stars/andygrunwald/go-jira?style=flat)](https://github.com/andygrunwald/go-jira/stargazers) - Go client library for [Atlassian JIRA](https://www.atlassian.com/software/jira)
- [go-lark](https://github.com/go-lark/lark) [![GitHub stars](https://img.shields.io/github/stars/go-lark/lark?style=flat)](https://github.com/go-lark/lark/stargazers) - An easy-to-use unofficial SDK for [Feishu](https://open.feishu.cn/) and [Lark](https://open.larksuite.com/) Open Platform.
- [go-marathon](https://github.com/gambol99/go-marathon) [![GitHub stars](https://img.shields.io/github/stars/gambol99/go-marathon?style=flat)](https://github.com/gambol99/go-marathon/stargazers) - Go library for interacting with Mesosphere's Marathon PAAS.
- [go-myanimelist](https://github.com/nstratos/go-myanimelist) [![GitHub stars](https://img.shields.io/github/stars/nstratos/go-myanimelist?style=flat)](https://github.com/nstratos/go-myanimelist/stargazers) - Go client library for accessing the [MyAnimeList API](https://myanimelist.net/apiconfig/references/api/v2).
- [go-openai](https://github.com/sashabaranov/go-openai) [![GitHub stars](https://img.shields.io/github/stars/sashabaranov/go-openai?style=flat)](https://github.com/sashabaranov/go-openai/stargazers) - OpenAI ChatGPT, DALL·E, Whisper API library for Go.
- [go-openproject](https://github.com/manuelbcd/go-openproject) [![GitHub stars](https://img.shields.io/github/stars/manuelbcd/go-openproject?style=flat)](https://github.com/manuelbcd/go-openproject/stargazers) - Go client library for interacting with [OpenProject](https://docs.openproject.org/api/) API.
- [go-postman-collection](https://github.com/rbretecher/go-postman-collection) [![GitHub stars](https://img.shields.io/github/stars/rbretecher/go-postman-collection?style=flat)](https://github.com/rbretecher/go-postman-collection/stargazers) - Go module to work with [Postman Collections](https://learning.getpostman.com/docs/postman/collections/creating-collections/) (compatible with Insomnia).
- [go-redoc](https://github.com/mvrilo/go-redoc) [![GitHub stars](https://img.shields.io/github/stars/mvrilo/go-redoc?style=flat)](https://github.com/mvrilo/go-redoc/stargazers) - Embedded OpenAPI/Swagger documentation ui for Go using [ReDoc](https://redocly.com/).
- [go-restcountries](https://github.com/chriscross0/go-restcountries) [![GitHub stars](https://img.shields.io/github/stars/chriscross0/go-restcountries?style=flat)](https://github.com/chriscross0/go-restcountries/stargazers) - Go library for the [REST Countries API](https://countrylayer.com/).
- [go-salesforce](https://github.com/k-capehart/go-salesforce) [![GitHub stars](https://img.shields.io/github/stars/k-capehart/go-salesforce?style=flat)](https://github.com/k-capehart/go-salesforce/stargazers) - Go client library for interacting with the [Salesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm).
- [go-sophos](https://github.com/esurdam/go-sophos) [![GitHub stars](https://img.shields.io/github/stars/esurdam/go-sophos?style=flat)](https://github.com/esurdam/go-sophos/stargazers) - Go client library for the [Sophos UTM REST API](https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en) with zero dependencies.
- [go-swagger-ui](https://github.com/esurdam/go-swagger-ui) [![GitHub stars](https://img.shields.io/github/stars/esurdam/go-swagger-ui?style=flat)](https://github.com/esurdam/go-swagger-ui/stargazers) - Go library containing precompiled [Swagger UI](https://swagger.io/tools/swagger-ui/) for serving swagger json.
- [go-telegraph](https://gitlab.com/toby3d/telegraph) - Telegraph publishing platform API client.
- [go-trending](https://github.com/andygrunwald/go-trending) [![GitHub stars](https://img.shields.io/github/stars/andygrunwald/go-trending?style=flat)](https://github.com/andygrunwald/go-trending/stargazers) - Go library for accessing [trending repositories](https://github.com/trending) [![GitHub stars](https://img.shields.io/github/stars/trending?style=flat)](https://github.com/trending/stargazers) and [developers](https://github.com/trending/developers) [![GitHub stars](https://img.shields.io/github/stars/trending/developers?style=flat)](https://github.com/trending/developers/stargazers) at Github.
- [go-unsplash](https://github.com/hbagdi/go-unsplash) [![GitHub stars](https://img.shields.io/github/stars/hbagdi/go-unsplash?style=flat)](https://github.com/hbagdi/go-unsplash/stargazers) - Go client library for the [Unsplash.com](https://unsplash.com) API.
- [go-xkcd](https://github.com/nishanths/go-xkcd) [![GitHub stars](https://img.shields.io/github/stars/nishanths/go-xkcd?style=flat)](https://github.com/nishanths/go-xkcd/stargazers) - Go client for the xkcd API.
- [go-yapla](https://gitlab.com/adrienK/go-yapla) - Go client library for the Yapla v2.0 API.
- [goagi](https://github.com/staskobzar/goagi) [![GitHub stars](https://img.shields.io/github/stars/staskobzar/goagi?style=flat)](https://github.com/staskobzar/goagi/stargazers) - Go library to build Asterisk PBX agi/fastagi applications.
- [goami2](https://github.com/staskobzar/goami2) [![GitHub stars](https://img.shields.io/github/stars/staskobzar/goami2?style=flat)](https://github.com/staskobzar/goami2/stargazers) - AMI v2 library for Asterisk PBX.
- [GoFreeDB](https://github.com/FreeLeh/GoFreeDB) [![GitHub stars](https://img.shields.io/github/stars/FreeLeh/GoFreeDB?style=flat)](https://github.com/FreeLeh/GoFreeDB/stargazers) - Golang library providing common and simple database abstractions on top of Google Sheets.
- [gogtrends](https://github.com/groovili/gogtrends) [![GitHub stars](https://img.shields.io/github/stars/groovili/gogtrends?style=flat)](https://github.com/groovili/gogtrends/stargazers) - Google Trends Unofficial API.
- [golang-tmdb](https://github.com/cyruzin/golang-tmdb) [![GitHub stars](https://img.shields.io/github/stars/cyruzin/golang-tmdb?style=flat)](https://github.com/cyruzin/golang-tmdb/stargazers) - Golang wrapper for The Movie Database API v3.
- [golyrics](https://github.com/mamal72/golyrics) [![GitHub stars](https://img.shields.io/github/stars/mamal72/golyrics?style=flat)](https://github.com/mamal72/golyrics/stargazers) - Golyrics is a Go library to fetch music lyrics data from the Wikia website.
- [gomalshare](https://github.com/MonaxGT/gomalshare) [![GitHub stars](https://img.shields.io/github/stars/MonaxGT/gomalshare?style=flat)](https://github.com/MonaxGT/gomalshare/stargazers) - Go library MalShare API [malshare.com](https://www.malshare.com/)
- [GoMusicBrainz](https://github.com/michiwend/gomusicbrainz) [![GitHub stars](https://img.shields.io/github/stars/michiwend/gomusicbrainz?style=flat)](https://github.com/michiwend/gomusicbrainz/stargazers) - Go MusicBrainz WS2 client library.
- [google](https://github.com/google/google-api-go-client) [![GitHub stars](https://img.shields.io/github/stars/google/google-api-go-client?style=flat)](https://github.com/google/google-api-go-client/stargazers) - Auto-generated Google APIs for Go.
- [google-analytics](https://github.com/chonthu/go-google-analytics) [![GitHub stars](https://img.shields.io/github/stars/chonthu/go-google-analytics?style=flat)](https://github.com/chonthu/go-google-analytics/stargazers) - Simple wrapper for easy google analytics reporting.
- [google-cloud](https://github.com/GoogleCloudPlatform/gcloud-golang) [![GitHub stars](https://img.shields.io/github/stars/GoogleCloudPlatform/gcloud-golang?style=flat)](https://github.com/GoogleCloudPlatform/gcloud-golang/stargazers) - Google Cloud APIs Go Client Library.
- [gopaapi5](https://github.com/utekaravinash/gopaapi5) [![GitHub stars](https://img.shields.io/github/stars/utekaravinash/gopaapi5?style=flat)](https://github.com/utekaravinash/gopaapi5/stargazers) - Go Client Library for [Amazon Product Advertising API 5.0](https://webservices.amazon.com/paapi5/documentation/).
- [gopensky](https://github.com/navidys/gopensky) [![GitHub stars](https://img.shields.io/github/stars/navidys/gopensky?style=flat)](https://github.com/navidys/gopensky/stargazers) - Go client implementation for [OpenSKY Network](https://opensky-network.org/) live's API (airspace ADS-B and Mode S data).
- [gosip](https://github.com/koltyakov/gosip) [![GitHub stars](https://img.shields.io/github/stars/koltyakov/gosip?style=flat)](https://github.com/koltyakov/gosip/stargazers) - Client library for SharePoint.
- [gostorm](https://github.com/jsgilmore/gostorm) [![GitHub stars](https://img.shields.io/github/stars/jsgilmore/gostorm?style=flat)](https://github.com/jsgilmore/gostorm/stargazers) - GoStorm is a Go library that implements the communications protocol required to write Storm spouts and Bolts in Go that communicate with the Storm shells.
- [hipchat](https://github.com/andybons/hipchat) [![GitHub stars](https://img.shields.io/github/stars/andybons/hipchat?style=flat)](https://github.com/andybons/hipchat/stargazers) - This project implements a golang client library for the Hipchat API.
- [hipchat (xmpp)](https://github.com/daneharrigan/hipchat) [![GitHub stars](https://img.shields.io/github/stars/daneharrigan/hipchat?style=flat)](https://github.com/daneharrigan/hipchat/stargazers) - A golang package to communicate with HipChat over XMPP.
- [igdb](https://github.com/Henry-Sarabia/igdb) [![GitHub stars](https://img.shields.io/github/stars/Henry-Sarabia/igdb?style=flat)](https://github.com/Henry-Sarabia/igdb/stargazers) - Go client for the [Internet Game Database API](https://api.igdb.com/).
- [ip2location-io-go](https://github.com/ip2location/ip2location-io-go) [![GitHub stars](https://img.shields.io/github/stars/ip2location/ip2location-io-go?style=flat)](https://github.com/ip2location/ip2location-io-go/stargazers) - Go wrapper for the IP2Location.io API [IP2Location.io](https://www.ip2location.io/).
- [jokeapi-go](https://github.com/icelain/jokeapi) [![GitHub stars](https://img.shields.io/github/stars/icelain/jokeapi?style=flat)](https://github.com/icelain/jokeapi/stargazers) - Go client for [JokeAPI](https://sv443.net/jokeapi/v2/).
- [lark](https://github.com/chyroc/lark) [![GitHub stars](https://img.shields.io/github/stars/chyroc/lark?style=flat)](https://github.com/chyroc/lark/stargazers) - [Feishu](https://open.feishu.cn/)/[Lark](https://open.larksuite.com/) Open API Go SDK, Support ALL Open API and Event Callback.
- [lastpass-go](https://github.com/ansd/lastpass-go) [![GitHub stars](https://img.shields.io/github/stars/ansd/lastpass-go?style=flat)](https://github.com/ansd/lastpass-go/stargazers) - Go client library for the [LastPass](https://www.lastpass.com/) API.
- [libgoffi](https://github.com/clevabit/libgoffi) [![GitHub stars](https://img.shields.io/github/stars/clevabit/libgoffi?style=flat)](https://github.com/clevabit/libgoffi/stargazers) - Library adapter toolbox for native [libffi](https://sourceware.org/libffi/) integration
- [libopenapi](https://github.com/pb33f/libopenapi) [![GitHub stars](https://img.shields.io/github/stars/pb33f/libopenapi?style=flat)](https://github.com/pb33f/libopenapi/stargazers) - Parse, validate, and work with OpenAPI, Swagger, Overlays, and Arazzo specifications.
- [Medium](https://github.com/Medium/medium-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/Medium/medium-sdk-go?style=flat)](https://github.com/Medium/medium-sdk-go/stargazers) - Golang SDK for Medium's OAuth2 API.
- [megos](https://github.com/andygrunwald/megos) [![GitHub stars](https://img.shields.io/github/stars/andygrunwald/megos?style=flat)](https://github.com/andygrunwald/megos/stargazers) - Client library for accessing an [Apache Mesos](https://mesos.apache.org/) cluster.
- [minio-go](https://github.com/minio/minio-go) [![GitHub stars](https://img.shields.io/github/stars/minio/minio-go?style=flat)](https://github.com/minio/minio-go/stargazers) - Minio Go Library for Amazon S3 compatible cloud storage.
- [mixpanel](https://github.com/dukex/mixpanel) [![GitHub stars](https://img.shields.io/github/stars/dukex/mixpanel?style=flat)](https://github.com/dukex/mixpanel/stargazers) - Mixpanel is a library for tracking events and sending Mixpanel profile updates to Mixpanel from your go applications.
- [newsapi-go](https://github.com/jellydator/newsapi-go) [![GitHub stars](https://img.shields.io/github/stars/jellydator/newsapi-go?style=flat)](https://github.com/jellydator/newsapi-go/stargazers) - Go client for [NewsAPI](https://newsapi.org/).
- [openaigo](https://github.com/otiai10/openaigo) [![GitHub stars](https://img.shields.io/github/stars/otiai10/openaigo?style=flat)](https://github.com/otiai10/openaigo/stargazers) - OpenAI GPT3/GPT3.5 ChatGPT API client library for Go.
- [patreon-go](https://github.com/mxpv/patreon-go) [![GitHub stars](https://img.shields.io/github/stars/mxpv/patreon-go?style=flat)](https://github.com/mxpv/patreon-go/stargazers) - Go library for Patreon API.
- [paypal](https://github.com/logpacker/PayPal-Go-SDK) [![GitHub stars](https://img.shields.io/github/stars/logpacker/PayPal-Go-SDK?style=flat)](https://github.com/logpacker/PayPal-Go-SDK/stargazers) - Wrapper for PayPal payment API.
- [playlyfe](https://github.com/playlyfe/playlyfe-go-sdk) [![GitHub stars](https://img.shields.io/github/stars/playlyfe/playlyfe-go-sdk?style=flat)](https://github.com/playlyfe/playlyfe-go-sdk/stargazers) - The Playlyfe Rest API Go SDK.
- [pushover](https://github.com/gregdel/pushover) [![GitHub stars](https://img.shields.io/github/stars/gregdel/pushover?style=flat)](https://github.com/gregdel/pushover/stargazers) - Go wrapper for the Pushover API.
- [rawg-sdk-go](https://github.com/dimuska139/rawg-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/dimuska139/rawg-sdk-go?style=flat)](https://github.com/dimuska139/rawg-sdk-go/stargazers) - Go library for the [RAWG Video Games Database](https://rawg.io/) API
- [shopify](https://github.com/rapito/go-shopify) [![GitHub stars](https://img.shields.io/github/stars/rapito/go-shopify?style=flat)](https://github.com/rapito/go-shopify/stargazers) - Go Library to make CRUD request to the Shopify API.
- [simples3](https://github.com/rhnvrm/simples3) [![GitHub stars](https://img.shields.io/github/stars/rhnvrm/simples3?style=flat)](https://github.com/rhnvrm/simples3/stargazers) - Simple no frills AWS S3 Library using REST with V4 Signing written in Go.
- [slack](https://github.com/slack-go/slack) [![GitHub stars](https://img.shields.io/github/stars/slack-go/slack?style=flat)](https://github.com/slack-go/slack/stargazers) - Slack API in Go.
- [smite](https://github.com/sergiotapia/smitego) [![GitHub stars](https://img.shields.io/github/stars/sergiotapia/smitego?style=flat)](https://github.com/sergiotapia/smitego/stargazers) - Go package to wraps access to the Smite game API.
- [spec](https://github.com/oaswrap/spec) [![GitHub stars](https://img.shields.io/github/stars/oaswrap/spec?style=flat)](https://github.com/oaswrap/spec/stargazers) - Lightweight OpenAPI 3.x builder supporting static generation and popular frameworks like chi, echo, gin, fiber, mux and more.
- [spotify](https://github.com/rapito/go-spotify) [![GitHub stars](https://img.shields.io/github/stars/rapito/go-spotify?style=flat)](https://github.com/rapito/go-spotify/stargazers) - Go Library to access Spotify WEB API.
- [steam](https://github.com/sostronk/go-steam) [![GitHub stars](https://img.shields.io/github/stars/sostronk/go-steam?style=flat)](https://github.com/sostronk/go-steam/stargazers) - Go Library to interact with Steam game servers.
- [stripe](https://github.com/stripe/stripe-go) [![GitHub stars](https://img.shields.io/github/stars/stripe/stripe-go?style=flat)](https://github.com/stripe/stripe-go/stargazers) - Go client for the Stripe API.
- [swag](https://github.com/zc2638/swag) [![GitHub stars](https://img.shields.io/github/stars/zc2638/swag?style=flat)](https://github.com/zc2638/swag/stargazers) - No comments, simple go wrapper to create swagger 2.0 compatible APIs. Support most routing frameworks, such as built-in, gin, chi, mux, echo, httprouter, fasthttp and more.
- [textbelt](https://github.com/dietsche/textbelt) [![GitHub stars](https://img.shields.io/github/stars/dietsche/textbelt?style=flat)](https://github.com/dietsche/textbelt/stargazers) - Go client for the textbelt.com txt messaging API.
- [threads-go](https://github.com/tirthpatell/threads-go) [![GitHub stars](https://img.shields.io/github/stars/tirthpatell/threads-go?style=flat)](https://github.com/tirthpatell/threads-go/stargazers) - Go client library for the Meta Threads API with OAuth 2.0, rate limiting, and type-safe error handling.
- [Trello](https://github.com/adlio/trello) [![GitHub stars](https://img.shields.io/github/stars/adlio/trello?style=flat)](https://github.com/adlio/trello/stargazers) - Go wrapper for the Trello API.
- [TripAdvisor](https://github.com/mrbenosborne/tripadvisor-golang) [![GitHub stars](https://img.shields.io/github/stars/mrbenosborne/tripadvisor-golang?style=flat)](https://github.com/mrbenosborne/tripadvisor-golang/stargazers) - Go wrapper for the TripAdvisor API.
- [tumblr](https://github.com/mattcunningham/gumblr) [![GitHub stars](https://img.shields.io/github/stars/mattcunningham/gumblr?style=flat)](https://github.com/mattcunningham/gumblr/stargazers) - Go wrapper for the Tumblr v2 API.
- [uptimerobot](https://github.com/bitfield/uptimerobot) [![GitHub stars](https://img.shields.io/github/stars/bitfield/uptimerobot?style=flat)](https://github.com/bitfield/uptimerobot/stargazers) - Go wrapper and command-line client for the Uptime Robot v2 API.
- [vl-go](https://github.com/verifid/vl-go) [![GitHub stars](https://img.shields.io/github/stars/verifid/vl-go?style=flat)](https://github.com/verifid/vl-go/stargazers) - Go client library around the VerifID identity verification layer API.
- [webhooks](https://github.com/go-playground/webhooks) [![GitHub stars](https://img.shields.io/github/stars/go-playground/webhooks?style=flat)](https://github.com/go-playground/webhooks/stargazers) - Webhook receiver for GitHub and Bitbucket.
- [wit-go](https://github.com/wit-ai/wit-go) [![GitHub stars](https://img.shields.io/github/stars/wit-ai/wit-go?style=flat)](https://github.com/wit-ai/wit-go/stargazers) - Go client for wit.ai HTTP API.
- [ynab](https://github.com/brunomvsouza/ynab.go) [![GitHub stars](https://img.shields.io/github/stars/brunomvsouza/ynab.go?style=flat)](https://github.com/brunomvsouza/ynab.go/stargazers) - Go wrapper for the YNAB API.
- [zooz](https://github.com/gojuno/go-zooz) [![GitHub stars](https://img.shields.io/github/stars/gojuno/go-zooz?style=flat)](https://github.com/gojuno/go-zooz/stargazers) - Go client for the Zooz API.

**[⬆ back to top](#contents)**

## Utilities

_General utilities and tools to make your life easier._

- [abstract](https://github.com/maxbolgarin/abstract) [![GitHub stars](https://img.shields.io/github/stars/maxbolgarin/abstract?style=flat)](https://github.com/maxbolgarin/abstract/stargazers) - Abstractions and utilities to get rid of boilerplate code in business logic.
- [apm](https://github.com/topfreegames/apm) [![GitHub stars](https://img.shields.io/github/stars/topfreegames/apm?style=flat)](https://github.com/topfreegames/apm/stargazers) - Process manager for Golang applications with an HTTP API.
- [backscanner](https://github.com/icza/backscanner) [![GitHub stars](https://img.shields.io/github/stars/icza/backscanner?style=flat)](https://github.com/icza/backscanner/stargazers) - A scanner similar to bufio.Scanner, but it reads and returns lines in reverse order, starting at a given position and going backward.
- [bed](https://github.com/itchyny/bed) [![GitHub stars](https://img.shields.io/github/stars/itchyny/bed?style=flat)](https://github.com/itchyny/bed/stargazers) - A Vim-like binary editor written in Go.
- [blank](https://github.com/Henry-Sarabia/blank) [![GitHub stars](https://img.shields.io/github/stars/Henry-Sarabia/blank?style=flat)](https://github.com/Henry-Sarabia/blank/stargazers) - Verify or remove blanks and whitespace from strings.
- [bleep](https://github.com/sinhashubham95/bleep) [![GitHub stars](https://img.shields.io/github/stars/sinhashubham95/bleep?style=flat)](https://github.com/sinhashubham95/bleep/stargazers) - Perform any number of actions on any set of OS signals in Go.
- [boilr](https://github.com/tmrts/boilr) [![GitHub stars](https://img.shields.io/github/stars/tmrts/boilr?style=flat)](https://github.com/tmrts/boilr/stargazers) - Blazingly fast CLI tool for creating projects from boilerplate templates.
- [boring](https://github.com/alebeck/boring) [![GitHub stars](https://img.shields.io/github/stars/alebeck/boring?style=flat)](https://github.com/alebeck/boring/stargazers) - Simple command-line SSH tunnel manager.
- [changie](https://github.com/miniscruff/changie) [![GitHub stars](https://img.shields.io/github/stars/miniscruff/changie?style=flat)](https://github.com/miniscruff/changie/stargazers) - Automated changelog tool for preparing releases with lots of customization options.
- [chyle](https://github.com/antham/chyle) [![GitHub stars](https://img.shields.io/github/stars/antham/chyle?style=flat)](https://github.com/antham/chyle/stargazers) - Changelog generator using a git repository with multiple configuration possibilities.
- [circuit](https://github.com/cep21/circuit) [![GitHub stars](https://img.shields.io/github/stars/cep21/circuit?style=flat)](https://github.com/cep21/circuit/stargazers) - An efficient and feature complete Hystrix like Go implementation of the circuit breaker pattern.
- [circuitbreaker](https://github.com/rubyist/circuitbreaker) [![GitHub stars](https://img.shields.io/github/stars/rubyist/circuitbreaker?style=flat)](https://github.com/rubyist/circuitbreaker/stargazers) - Circuit Breakers in Go.
- [clipboard](https://github.com/golang-design/clipboard) [![GitHub stars](https://img.shields.io/github/stars/golang-design/clipboard?style=flat)](https://github.com/golang-design/clipboard/stargazers) - 📋 cross-platform clipboard package in Go.
- [clockwork](https://github.com/jonboulle/clockwork) [![GitHub stars](https://img.shields.io/github/stars/jonboulle/clockwork?style=flat)](https://github.com/jonboulle/clockwork/stargazers) - A simple fake clock for golang.
- [cmd](https://github.com/SimonBaeumer/cmd) [![GitHub stars](https://img.shields.io/github/stars/SimonBaeumer/cmd?style=flat)](https://github.com/SimonBaeumer/cmd/stargazers) - Library for executing shell commands on osx, windows and linux.
- [config-file-validator](https://github.com/Boeing/config-file-validator) [![GitHub stars](https://img.shields.io/github/stars/Boeing/config-file-validator?style=flat)](https://github.com/Boeing/config-file-validator/stargazers) - Cross Platform tool to validate configuration files.
- [contem](https://github.com/maxbolgarin/contem) [![GitHub stars](https://img.shields.io/github/stars/maxbolgarin/contem?style=flat)](https://github.com/maxbolgarin/contem/stargazers) - Drop-in context.Context replacement for graceful shutdown Go applications.
- [cookie](https://github.com/syntaqx/cookie) [![GitHub stars](https://img.shields.io/github/stars/syntaqx/cookie?style=flat)](https://github.com/syntaqx/cookie/stargazers) - Cookie struct parsing and helper package.
- [copy-pasta](https://github.com/jutkko/copy-pasta) [![GitHub stars](https://img.shields.io/github/stars/jutkko/copy-pasta?style=flat)](https://github.com/jutkko/copy-pasta/stargazers) - Universal multi-workstation clipboard that uses S3 like backend for the storage.
- [countries](https://github.com/biter777/countries) [![GitHub stars](https://img.shields.io/github/stars/biter777/countries?style=flat)](https://github.com/biter777/countries/stargazers) - Full implementation of ISO-3166-1, ISO-4217, ITU-T E.164, Unicode CLDR and IANA ccTLD standards.
- [countries](https://github.com/pioz/countries) [![GitHub stars](https://img.shields.io/github/stars/pioz/countries?style=flat)](https://github.com/pioz/countries/stargazers) - All you need when you are working with countries in Go.
- [create-go-app](https://github.com/create-go-app/cli) [![GitHub stars](https://img.shields.io/github/stars/create-go-app/cli?style=flat)](https://github.com/create-go-app/cli/stargazers) - A powerful CLI for create a new production-ready project with backend (Golang), frontend (JavaScript, TypeScript) & deploy automation (Ansible, Docker) by running one command.
- [cryptgo](https://github.com/Gituser143/cryptgo) [![GitHub stars](https://img.shields.io/github/stars/Gituser143/cryptgo?style=flat)](https://github.com/Gituser143/cryptgo/stargazers) - Crytpgo is a TUI based application written purely in Go to monitor and observe cryptocurrency prices in real time!
- [ctop](https://github.com/bcicen/ctop) [![GitHub stars](https://img.shields.io/github/stars/bcicen/ctop?style=flat)](https://github.com/bcicen/ctop/stargazers) - [Top-like](https://ctop.sh) interface (e.g. htop) for container metrics.
- [ctxutil](https://github.com/posener/ctxutil) [![GitHub stars](https://img.shields.io/github/stars/posener/ctxutil?style=flat)](https://github.com/posener/ctxutil/stargazers) - A collection of utility functions for contexts.
- [cvt](https://github.com/shockerli/cvt) [![GitHub stars](https://img.shields.io/github/stars/shockerli/cvt?style=flat)](https://github.com/shockerli/cvt/stargazers) - Easy and safe convert any value to another type.
- [dbt](https://github.com/nikogura/dbt) [![GitHub stars](https://img.shields.io/github/stars/nikogura/dbt?style=flat)](https://github.com/nikogura/dbt/stargazers) - A framework for running self-updating signed binaries from a central, trusted repository.
- [Death](https://github.com/vrecan/death) [![GitHub stars](https://img.shields.io/github/stars/vrecan/death?style=flat)](https://github.com/vrecan/death/stargazers) - Managing go application shutdown with signals.
- [debounce](https://github.com/floatdrop/debounce) [![GitHub stars](https://img.shields.io/github/stars/floatdrop/debounce?style=flat)](https://github.com/floatdrop/debounce/stargazers) - A zero-allocation debouncer written in Go.
- [delve](https://github.com/derekparker/delve) [![GitHub stars](https://img.shields.io/github/stars/derekparker/delve?style=flat)](https://github.com/derekparker/delve/stargazers) - Go debugger.
- [dive](https://github.com/wagoodman/dive) [![GitHub stars](https://img.shields.io/github/stars/wagoodman/dive?style=flat)](https://github.com/wagoodman/dive/stargazers) - A tool for exploring each layer in a Docker image.
- [dlog](https://github.com/kirillDanshin/dlog) [![GitHub stars](https://img.shields.io/github/stars/kirillDanshin/dlog?style=flat)](https://github.com/kirillDanshin/dlog/stargazers) - Compile-time controlled logger to make your release smaller without removing debug calls.
- [EaseProbe](https://github.com/megaease/easeprobe) [![GitHub stars](https://img.shields.io/github/stars/megaease/easeprobe?style=flat)](https://github.com/megaease/easeprobe/stargazers) - A simple, standalone, and lightWeight tool that can do health/status checking daemon, support HTTP/TCP/SSH/Shell/Client/... probes, and Slack/Discord/Telegram/SMS... notification.
- [equalizer](https://github.com/reugn/equalizer) [![GitHub stars](https://img.shields.io/github/stars/reugn/equalizer?style=flat)](https://github.com/reugn/equalizer/stargazers) - Quota manager and rate limiter collection for Go.
- [ergo](https://github.com/cristianoliveira/ergo) [![GitHub stars](https://img.shields.io/github/stars/cristianoliveira/ergo?style=flat)](https://github.com/cristianoliveira/ergo/stargazers) - The management of multiple local services running over different ports made easy.
- [evaluator](https://github.com/nullne/evaluator) [![GitHub stars](https://img.shields.io/github/stars/nullne/evaluator?style=flat)](https://github.com/nullne/evaluator/stargazers) - Evaluate an expression dynamically based on s-expression. It's simple and easy to extend.
- [Failsafe-go](https://github.com/failsafe-go/failsafe-go) [![GitHub stars](https://img.shields.io/github/stars/failsafe-go/failsafe-go?style=flat)](https://github.com/failsafe-go/failsafe-go/stargazers) - Fault tolerance and resilience patterns for Go.
- [filetype](https://github.com/h2non/filetype) [![GitHub stars](https://img.shields.io/github/stars/h2non/filetype?style=flat)](https://github.com/h2non/filetype/stargazers) - Small package to infer the file type checking the magic numbers signature.
- [filler](https://github.com/yaronsumel/filler) [![GitHub stars](https://img.shields.io/github/stars/yaronsumel/filler?style=flat)](https://github.com/yaronsumel/filler/stargazers) - small utility to fill structs using "fill" tag.
- [filter](https://github.com/gookit/filter) [![GitHub stars](https://img.shields.io/github/stars/gookit/filter?style=flat)](https://github.com/gookit/filter/stargazers) - provide filtering, sanitizing, and conversion of Go data.
- [fzf](https://github.com/junegunn/fzf) [![GitHub stars](https://img.shields.io/github/stars/junegunn/fzf?style=flat)](https://github.com/junegunn/fzf/stargazers) - Command-line fuzzy finder written in Go.
- [generate](https://github.com/go-playground/generate) [![GitHub stars](https://img.shields.io/github/stars/go-playground/generate?style=flat)](https://github.com/go-playground/generate/stargazers) - runs go generate recursively on a specified path or environment variable and can filter by regex.
- [gh-image](https://github.com/drogers0/gh-image) [![GitHub stars](https://img.shields.io/github/stars/drogers0/gh-image?style=flat)](https://github.com/drogers0/gh-image/stargazers) - A gh CLI extension that uploads images to GitHub issues, PRs, and READMEs from the command line, producing user-attachments URLs that respect repository visibility.
- [ghokin](https://github.com/antham/ghokin) [![GitHub stars](https://img.shields.io/github/stars/antham/ghokin?style=flat)](https://github.com/antham/ghokin/stargazers) - Parallelized formatter with no external dependencies for gherkin (cucumber, behat...).
- [git-time-metric](https://github.com/git-time-metric/gtm) [![GitHub stars](https://img.shields.io/github/stars/git-time-metric/gtm?style=flat)](https://github.com/git-time-metric/gtm/stargazers) - Simple, seamless, lightweight time tracking for Git.
- [git-tools](https://github.com/kazhuravlev/git-tools) [![GitHub stars](https://img.shields.io/github/stars/kazhuravlev/git-tools?style=flat)](https://github.com/kazhuravlev/git-tools/stargazers) - Tool to help manage git tags.
- [gitbatch](https://github.com/isacikgoz/gitbatch) [![GitHub stars](https://img.shields.io/github/stars/isacikgoz/gitbatch?style=flat)](https://github.com/isacikgoz/gitbatch/stargazers) - manage your git repositories in one place.
- [gitcs](https://github.com/knbr13/gitcs/) [![GitHub stars](https://img.shields.io/github/stars/knbr13/gitcs/?style=flat)](https://github.com/knbr13/gitcs//stargazers) - Git Commits Visualizer, CLI tool to visualize your Git commits on your local machine.
- [go-actuator](https://github.com/sinhashubham95/go-actuator) [![GitHub stars](https://img.shields.io/github/stars/sinhashubham95/go-actuator?style=flat)](https://github.com/sinhashubham95/go-actuator/stargazers) - Production ready features for Go based web frameworks.
- [go-astitodo](https://github.com/asticode/go-astitodo) [![GitHub stars](https://img.shields.io/github/stars/asticode/go-astitodo?style=flat)](https://github.com/asticode/go-astitodo/stargazers) - Parse TODOs in your GO code.
- [go-bind-plugin](https://github.com/wendigo/go-bind-plugin) [![GitHub stars](https://img.shields.io/github/stars/wendigo/go-bind-plugin?style=flat)](https://github.com/wendigo/go-bind-plugin/stargazers) - go:generate tool for wrapping symbols exported by golang plugins (1.8 only).
- [go-bsdiff](https://github.com/gabstv/go-bsdiff) [![GitHub stars](https://img.shields.io/github/stars/gabstv/go-bsdiff?style=flat)](https://github.com/gabstv/go-bsdiff/stargazers) - Pure Go bsdiff and bspatch libraries and CLI tools.
- [go-clip](https://github.com/prashantgupta24/go-clip) [![GitHub stars](https://img.shields.io/github/stars/prashantgupta24/go-clip?style=flat)](https://github.com/prashantgupta24/go-clip/stargazers) - A minimalistic clipboard manager for Mac.
- [Go-Constant](https://github.com/sajjadrabiee/go-constant) [![GitHub stars](https://img.shields.io/github/stars/sajjadrabiee/go-constant?style=flat)](https://github.com/sajjadrabiee/go-constant/stargazers) - Generic typed constant sets with safe string parsing for Go's missing enum type.
- [go-convert](https://github.com/Eun/go-convert) [![GitHub stars](https://img.shields.io/github/stars/Eun/go-convert?style=flat)](https://github.com/Eun/go-convert/stargazers) - Package go-convert enables you to convert a value into another type.
- [go-countries](https://github.com/mikekonan/go-countries) [![GitHub stars](https://img.shields.io/github/stars/mikekonan/go-countries?style=flat)](https://github.com/mikekonan/go-countries/stargazers) - Lightweight lookup over ISO-3166 codes.
- [go-dry](https://github.com/ungerik/go-dry) [![GitHub stars](https://img.shields.io/github/stars/ungerik/go-dry?style=flat)](https://github.com/ungerik/go-dry/stargazers) - DRY (don't repeat yourself) package for Go.
- [go-events](https://github.com/deatil/go-events) [![GitHub stars](https://img.shields.io/github/stars/deatil/go-events?style=flat)](https://github.com/deatil/go-events/stargazers) - A go event and event'subscribe package, like wordpress hook functions.
- [go-funk](https://github.com/thoas/go-funk) [![GitHub stars](https://img.shields.io/github/stars/thoas/go-funk?style=flat)](https://github.com/thoas/go-funk/stargazers) - Modern Go utility library which provides helpers (map, find, contains, filter, chunk, reverse, ...).
- [go-health](https://github.com/Talento90/go-health) [![GitHub stars](https://img.shields.io/github/stars/Talento90/go-health?style=flat)](https://github.com/Talento90/go-health/stargazers) - Health package simplifies the way you add health check to your services.
- [go-httpheader](https://github.com/mozillazg/go-httpheader) [![GitHub stars](https://img.shields.io/github/stars/mozillazg/go-httpheader?style=flat)](https://github.com/mozillazg/go-httpheader/stargazers) - Go library for encoding structs into Header fields.
- [go-lambda-cleanup](https://github.com/karl-cardenas-coding/go-lambda-cleanup) [![GitHub stars](https://img.shields.io/github/stars/karl-cardenas-coding/go-lambda-cleanup?style=flat)](https://github.com/karl-cardenas-coding/go-lambda-cleanup/stargazers) - A CLI for removing unused or previous versions of AWS Lambdas.
- [go-lock](https://github.com/viney-shih/go-lock) [![GitHub stars](https://img.shields.io/github/stars/viney-shih/go-lock?style=flat)](https://github.com/viney-shih/go-lock/stargazers) - go-lock is a lock library implementing read-write mutex and read-write trylock without starvation.
- [go-pattern-match](https://github.com/PhakornKiong/go-pattern-match) [![GitHub stars](https://img.shields.io/github/stars/PhakornKiong/go-pattern-match?style=flat)](https://github.com/PhakornKiong/go-pattern-match/stargazers) - A Pattern matching library inspired by ts-pattern.
- [go-pkg](https://github.com/chenquan/go-pkg) [![GitHub stars](https://img.shields.io/github/stars/chenquan/go-pkg?style=flat)](https://github.com/chenquan/go-pkg/stargazers) - A go toolkit.
- [go-problemdetails](https://github.com/mvmaasakkers/go-problemdetails) [![GitHub stars](https://img.shields.io/github/stars/mvmaasakkers/go-problemdetails?style=flat)](https://github.com/mvmaasakkers/go-problemdetails/stargazers) - Go package for working with Problem Details.
- [go-qr](https://github.com/piglig/go-qr) [![GitHub stars](https://img.shields.io/github/stars/piglig/go-qr?style=flat)](https://github.com/piglig/go-qr/stargazers) - A native, high-quality and minimalistic QR code generator.
- [go-rate](https://github.com/beefsack/go-rate) [![GitHub stars](https://img.shields.io/github/stars/beefsack/go-rate?style=flat)](https://github.com/beefsack/go-rate/stargazers) - Timed rate limiter for Go.
- [go-safecast](https://github.com/ccoVeille/go-safecast) [![GitHub stars](https://img.shields.io/github/stars/ccoVeille/go-safecast?style=flat)](https://github.com/ccoVeille/go-safecast/stargazers) - Safe number type conversion library that prevents integer overflow and underflow (addresses gosec G115 and CWE-190).
- [go-sitemap-generator](https://github.com/ikeikeikeike/go-sitemap-generator) [![GitHub stars](https://img.shields.io/github/stars/ikeikeikeike/go-sitemap-generator?style=flat)](https://github.com/ikeikeikeike/go-sitemap-generator/stargazers) - XML Sitemap generator written in Go.
- [go-snk](https://github.com/SharkByteSoftware/go-snk) [![GitHub stars](https://img.shields.io/github/stars/SharkByteSoftware/go-snk?style=flat)](https://github.com/SharkByteSoftware/go-snk/stargazers) - Type-safe generic helpers for slices, maps, strings, errors, JSON, HTTP, and containers, organized as small independently adoptable packages.
- [go-trigger](https://github.com/sadlil/go-trigger) [![GitHub stars](https://img.shields.io/github/stars/sadlil/go-trigger?style=flat)](https://github.com/sadlil/go-trigger/stargazers) - Go-lang global event triggerer, Register Events with an id and trigger the event from anywhere from your project.
- [go-tripper](https://github.com/rajnandan1/go-tripper) [![GitHub stars](https://img.shields.io/github/stars/rajnandan1/go-tripper?style=flat)](https://github.com/rajnandan1/go-tripper/stargazers) - Tripper is a circuit breaker package for Go that allows you to circuit and control the status of circuits.
- [go-type](https://github.com/mikekonan/go-types) [![GitHub stars](https://img.shields.io/github/stars/mikekonan/go-types?style=flat)](https://github.com/mikekonan/go-types/stargazers) - Library providing Go types for store/validation and transfer of ISO-4217, ISO-3166, and other types.
- [goback](https://github.com/carlescere/goback) [![GitHub stars](https://img.shields.io/github/stars/carlescere/goback?style=flat)](https://github.com/carlescere/goback/stargazers) - Go simple exponential backoff package.
- [goctx](https://github.com/zerosnake0/goctx) [![GitHub stars](https://img.shields.io/github/stars/zerosnake0/goctx?style=flat)](https://github.com/zerosnake0/goctx/stargazers) - Get your context value with high performance.
- [godaemon](https://github.com/VividCortex/godaemon) [![GitHub stars](https://img.shields.io/github/stars/VividCortex/godaemon?style=flat)](https://github.com/VividCortex/godaemon/stargazers) - Utility to write daemons.
- [godoclive](https://github.com/syst3mctl/godoclive) [![GitHub stars](https://img.shields.io/github/stars/syst3mctl/godoclive?style=flat)](https://github.com/syst3mctl/godoclive/stargazers) - Generates interactive API documentation from Go HTTP handlers using static analysis of chi, gin, and net/http routers.
- [godropbox](https://github.com/dropbox/godropbox) [![GitHub stars](https://img.shields.io/github/stars/dropbox/godropbox?style=flat)](https://github.com/dropbox/godropbox/stargazers) - Common libraries for writing Go services/applications from Dropbox.
- [gofn](https://github.com/tiendc/gofn) [![GitHub stars](https://img.shields.io/github/stars/tiendc/gofn?style=flat)](https://github.com/tiendc/gofn/stargazers) - High performance utility functions written using Generics for Go 1.18+.
- [golarm](https://github.com/msempere/golarm) [![GitHub stars](https://img.shields.io/github/stars/msempere/golarm?style=flat)](https://github.com/msempere/golarm/stargazers) - Fire alarms with system events.
- [golog](https://github.com/mlimaloureiro/golog) [![GitHub stars](https://img.shields.io/github/stars/mlimaloureiro/golog?style=flat)](https://github.com/mlimaloureiro/golog/stargazers) - Easy and lightweight CLI tool to time track your tasks.
- [gopencils](https://github.com/bndr/gopencils) [![GitHub stars](https://img.shields.io/github/stars/bndr/gopencils?style=flat)](https://github.com/bndr/gopencils/stargazers) - Small and simple package to easily consume REST APIs.
- [goplaceholder](https://github.com/michiwend/goplaceholder) [![GitHub stars](https://img.shields.io/github/stars/michiwend/goplaceholder?style=flat)](https://github.com/michiwend/goplaceholder/stargazers) - a small golang lib to generate placeholder images.
- [goreadability](https://github.com/philipjkim/goreadability) [![GitHub stars](https://img.shields.io/github/stars/philipjkim/goreadability?style=flat)](https://github.com/philipjkim/goreadability/stargazers) - Webpage summary extractor using Facebook Open Graph and arc90's readability.
- [goreleaser](https://github.com/goreleaser/goreleaser) [![GitHub stars](https://img.shields.io/github/stars/goreleaser/goreleaser?style=flat)](https://github.com/goreleaser/goreleaser/stargazers) - Deliver Go binaries as fast and easily as possible.
- [goreporter](https://github.com/wgliang/goreporter) [![GitHub stars](https://img.shields.io/github/stars/wgliang/goreporter?style=flat)](https://github.com/wgliang/goreporter/stargazers) - Golang tool that does static analysis, unit testing, code review and generate code quality report.
- [goseaweedfs](https://github.com/linxGnu/goseaweedfs) [![GitHub stars](https://img.shields.io/github/stars/linxGnu/goseaweedfs?style=flat)](https://github.com/linxGnu/goseaweedfs/stargazers) - SeaweedFS client library with almost full features.
- [gostrutils](https://github.com/ik5/gostrutils) [![GitHub stars](https://img.shields.io/github/stars/ik5/gostrutils?style=flat)](https://github.com/ik5/gostrutils/stargazers) - Collections of string manipulation and conversion functions.
- [gotenv](https://github.com/subosito/gotenv) [![GitHub stars](https://img.shields.io/github/stars/subosito/gotenv?style=flat)](https://github.com/subosito/gotenv/stargazers) - Load environment variables from `.env` or any `io.Reader` in Go.
- [goval](https://github.com/maja42/goval) [![GitHub stars](https://img.shields.io/github/stars/maja42/goval?style=flat)](https://github.com/maja42/goval/stargazers) - Evaluate arbitrary expressions in Go.
- [graterm](https://github.com/skovtunenko/graterm) [![GitHub stars](https://img.shields.io/github/stars/skovtunenko/graterm?style=flat)](https://github.com/skovtunenko/graterm/stargazers) - Provides primitives to perform ordered (sequential/concurrent) GRAceful TERMination (aka shutdown) in Go application.
- [grofer](https://github.com/pesos/grofer) [![GitHub stars](https://img.shields.io/github/stars/pesos/grofer?style=flat)](https://github.com/pesos/grofer/stargazers) - A system and resource monitoring tool written in Golang!
- [gubrak](https://github.com/novalagung/gubrak) [![GitHub stars](https://img.shields.io/github/stars/novalagung/gubrak?style=flat)](https://github.com/novalagung/gubrak/stargazers) - Golang utility library with syntactic sugar. It's like lodash, but for golang.
- [handy](https://github.com/miguelpragier/handy) [![GitHub stars](https://img.shields.io/github/stars/miguelpragier/handy?style=flat)](https://github.com/miguelpragier/handy/stargazers) - Many utilities and helpers like string handlers/formatters and validators.
- [healthcheck](https://github.com/kazhuravlev/healthcheck) [![GitHub stars](https://img.shields.io/github/stars/kazhuravlev/healthcheck?style=flat)](https://github.com/kazhuravlev/healthcheck/stargazers) - A simple yet powerful readiness test for Kubernetes.
- [hostctl](https://github.com/guumaster/hostctl) [![GitHub stars](https://img.shields.io/github/stars/guumaster/hostctl?style=flat)](https://github.com/guumaster/hostctl/stargazers) - A CLI tool to manage /etc/hosts with easy commands.
- [htcat](https://github.com/htcat/htcat) [![GitHub stars](https://img.shields.io/github/stars/htcat/htcat?style=flat)](https://github.com/htcat/htcat/stargazers) - Parallel and Pipelined HTTP GET Utility.
- [hub](https://github.com/github/hub) [![GitHub stars](https://img.shields.io/github/stars/github/hub?style=flat)](https://github.com/github/hub/stargazers) - wrap git commands with additional functionality to interact with github from the terminal.
- [immortal](https://github.com/immortal/immortal) [![GitHub stars](https://img.shields.io/github/stars/immortal/immortal?style=flat)](https://github.com/immortal/immortal/stargazers) - \*nix cross-platform (OS agnostic) supervisor.
- [jet](https://github.com/NicoNex/jet) [![GitHub stars](https://img.shields.io/github/stars/NicoNex/jet?style=flat)](https://github.com/NicoNex/jet/stargazers) - Just Edit Text: a fast and powerful tool for finding and replacing file content and names using regular expressions.
- [jsend](https://github.com/clevergo/jsend) [![GitHub stars](https://img.shields.io/github/stars/clevergo/jsend?style=flat)](https://github.com/clevergo/jsend/stargazers) - JSend's implementation written in Go.
- [json-log-viewer](https://github.com/hedhyw/json-log-viewer) [![GitHub stars](https://img.shields.io/github/stars/hedhyw/json-log-viewer?style=flat)](https://github.com/hedhyw/json-log-viewer/stargazers) - Interactive viewer for JSON logs.
- [jump](https://github.com/gsamokovarov/jump) [![GitHub stars](https://img.shields.io/github/stars/gsamokovarov/jump?style=flat)](https://github.com/gsamokovarov/jump/stargazers) - Jump helps you navigate faster by learning your habits.
- [just](https://github.com/kazhuravlev/just) [![GitHub stars](https://img.shields.io/github/stars/kazhuravlev/just?style=flat)](https://github.com/kazhuravlev/just/stargazers) - Just a collection of useful functions for working with generic data structures.
- [koazee](https://github.com/wesovilabs/koazee) [![GitHub stars](https://img.shields.io/github/stars/wesovilabs/koazee?style=flat)](https://github.com/wesovilabs/koazee/stargazers) - Library inspired in Lazy evaluation and functional programming that takes the hassle out of working with arrays.
- [lang](https://github.com/maxbolgarin/lang) [![GitHub stars](https://img.shields.io/github/stars/maxbolgarin/lang?style=flat)](https://github.com/maxbolgarin/lang/stargazers) - Generic one-liners to work with variables, slices and maps without boilerplate code.
- [lets-go](https://github.com/aplescia-chwy/lets-go) [![GitHub stars](https://img.shields.io/github/stars/aplescia-chwy/lets-go?style=flat)](https://github.com/aplescia-chwy/lets-go/stargazers) - Go module that provides common utilities for Cloud Native REST API development. Also contains AWS Specific utilities.
- [limiters](https://github.com/mennanov/limiters) [![GitHub stars](https://img.shields.io/github/stars/mennanov/limiters?style=flat)](https://github.com/mennanov/limiters/stargazers) - Rate limiters for distributed applications in Golang with configurable back-ends and distributed locks.
- [lo](https://github.com/samber/lo) [![GitHub stars](https://img.shields.io/github/stars/samber/lo?style=flat)](https://github.com/samber/lo/stargazers) - A Lodash like Go library based on Go 1.18+ Generics (map, filter, contains, find...)
- [loncha](https://github.com/kazu/loncha) [![GitHub stars](https://img.shields.io/github/stars/kazu/loncha?style=flat)](https://github.com/kazu/loncha/stargazers) - A high-performance slice Utilities.
- [lrserver](https://github.com/jaschaephraim/lrserver) [![GitHub stars](https://img.shields.io/github/stars/jaschaephraim/lrserver?style=flat)](https://github.com/jaschaephraim/lrserver/stargazers) - LiveReload server for Go.
- [mani](https://github.com/alajmo/mani) [![GitHub stars](https://img.shields.io/github/stars/alajmo/mani?style=flat)](https://github.com/alajmo/mani/stargazers) - CLI tool to help you manage multiple repositories.
- [mc](https://github.com/minio/mc) [![GitHub stars](https://img.shields.io/github/stars/minio/mc?style=flat)](https://github.com/minio/mc/stargazers) - Minio Client provides minimal tools to work with Amazon S3 compatible cloud storage and filesystems.
- [mergo](https://github.com/imdario/mergo) [![GitHub stars](https://img.shields.io/github/stars/imdario/mergo?style=flat)](https://github.com/imdario/mergo/stargazers) - Helper to merge structs and maps in Golang. Useful for configuration default values, avoiding messy if-statements.
- [mimemagic](https://github.com/zRedShift/mimemagic) [![GitHub stars](https://img.shields.io/github/stars/zRedShift/mimemagic?style=flat)](https://github.com/zRedShift/mimemagic/stargazers) - Pure Go ultra performant MIME sniffing library/utility.
- [mimetype](https://github.com/gabriel-vasile/mimetype) [![GitHub stars](https://img.shields.io/github/stars/gabriel-vasile/mimetype?style=flat)](https://github.com/gabriel-vasile/mimetype/stargazers) - Package for MIME type detection based on magic numbers.
- [minify](https://github.com/tdewolff/minify) [![GitHub stars](https://img.shields.io/github/stars/tdewolff/minify?style=flat)](https://github.com/tdewolff/minify/stargazers) - Fast minifiers for HTML, CSS, JS, XML, JSON and SVG file formats.
- [minquery](https://github.com/icza/minquery) [![GitHub stars](https://img.shields.io/github/stars/icza/minquery?style=flat)](https://github.com/icza/minquery/stargazers) - MongoDB / mgo.v2 query that supports efficient pagination (cursors to continue listing documents where we left off).
- [moldova](https://github.com/StabbyCutyou/moldova) [![GitHub stars](https://img.shields.io/github/stars/StabbyCutyou/moldova?style=flat)](https://github.com/StabbyCutyou/moldova/stargazers) - Utility for generating random data based on an input template.
- [mole](https://github.com/davrodpin/mole) [![GitHub stars](https://img.shields.io/github/stars/davrodpin/mole?style=flat)](https://github.com/davrodpin/mole/stargazers) - cli app to easily create ssh tunnels.
- [mongo-go-pagination](https://github.com/gobeam/mongo-go-pagination) [![GitHub stars](https://img.shields.io/github/stars/gobeam/mongo-go-pagination?style=flat)](https://github.com/gobeam/mongo-go-pagination/stargazers) - Mongodb Pagination for official mongodb/mongo-go-driver package which supports both normal queries and Aggregation pipelines.
- [mssqlx](https://github.com/linxGnu/mssqlx) [![GitHub stars](https://img.shields.io/github/stars/linxGnu/mssqlx?style=flat)](https://github.com/linxGnu/mssqlx/stargazers) - Database client library, proxy for any master slave, master master structures. Lightweight and auto balancing in mind.
- [multitick](https://github.com/VividCortex/multitick) [![GitHub stars](https://img.shields.io/github/stars/VividCortex/multitick?style=flat)](https://github.com/VividCortex/multitick/stargazers) - Multiplexor for aligned tickers.
- [netbug](https://github.com/e-dard/netbug) [![GitHub stars](https://img.shields.io/github/stars/e-dard/netbug?style=flat)](https://github.com/e-dard/netbug/stargazers) - Easy remote profiling of your services.
- [nfdump](https://github.com/chrispassas/nfdump) [![GitHub stars](https://img.shields.io/github/stars/chrispassas/nfdump?style=flat)](https://github.com/chrispassas/nfdump/stargazers) - Read nfdump netflow files.
- [nostromo](https://github.com/pokanop/nostromo) [![GitHub stars](https://img.shields.io/github/stars/pokanop/nostromo?style=flat)](https://github.com/pokanop/nostromo/stargazers) - CLI for building powerful aliases.
- [okrun](https://github.com/xta/okrun) [![GitHub stars](https://img.shields.io/github/stars/xta/okrun?style=flat)](https://github.com/xta/okrun/stargazers) - go run error steamroller.
- [olaf](https://github.com/btnguyen2k/olaf) [![GitHub stars](https://img.shields.io/github/stars/btnguyen2k/olaf?style=flat)](https://github.com/btnguyen2k/olaf/stargazers) - Twitter Snowflake implemented in Go.
- [onecache](https://github.com/adelowo/onecache) [![GitHub stars](https://img.shields.io/github/stars/adelowo/onecache?style=flat)](https://github.com/adelowo/onecache/stargazers) - Caching library with support for multiple backend stores (Redis, Memcached, filesystem etc).
- [optional](https://github.com/kazhuravlev/optional) [![GitHub stars](https://img.shields.io/github/stars/kazhuravlev/optional?style=flat)](https://github.com/kazhuravlev/optional/stargazers) - Optional struct fields and vars.
- [panicparse](https://github.com/maruel/panicparse) [![GitHub stars](https://img.shields.io/github/stars/maruel/panicparse?style=flat)](https://github.com/maruel/panicparse/stargazers) - Groups similar goroutines and colorizes stack dump.
- [pattern-match](https://github.com/alexpantyukhin/go-pattern-match) [![GitHub stars](https://img.shields.io/github/stars/alexpantyukhin/go-pattern-match?style=flat)](https://github.com/alexpantyukhin/go-pattern-match/stargazers) - Pattern matching library.
- [peco](https://github.com/peco/peco) [![GitHub stars](https://img.shields.io/github/stars/peco/peco?style=flat)](https://github.com/peco/peco/stargazers) - Simplistic interactive filtering tool.
- [pgo](https://github.com/arthurkushman/pgo) [![GitHub stars](https://img.shields.io/github/stars/arthurkushman/pgo?style=flat)](https://github.com/arthurkushman/pgo/stargazers) - Convenient functions for PHP community.
- [pm](https://github.com/VividCortex/pm) [![GitHub stars](https://img.shields.io/github/stars/VividCortex/pm?style=flat)](https://github.com/VividCortex/pm/stargazers) - Process (i.e. goroutine) manager with an HTTP API.
- [pointer](https://github.com/xorcare/pointer) [![GitHub stars](https://img.shields.io/github/stars/xorcare/pointer?style=flat)](https://github.com/xorcare/pointer/stargazers) - Package pointer contains helper routines for simplifying the creation of optional fields of basic type.
- [ptr](https://github.com/gotidy/ptr) [![GitHub stars](https://img.shields.io/github/stars/gotidy/ptr?style=flat)](https://github.com/gotidy/ptr/stargazers) - Package that provide functions for simplified creation of pointers from constants of basic types.
- [rate](https://github.com/webriots/rate) [![GitHub stars](https://img.shields.io/github/stars/webriots/rate?style=flat)](https://github.com/webriots/rate/stargazers) - High-performance rate limiting library with token bucket and AIMD strategies.
- [rclient](https://github.com/zpatrick/rclient) [![GitHub stars](https://img.shields.io/github/stars/zpatrick/rclient?style=flat)](https://github.com/zpatrick/rclient/stargazers) - Readable, flexible, simple-to-use client for REST APIs.
- [release](https://github.com/tomodian/release) [![GitHub stars](https://img.shields.io/github/stars/tomodian/release?style=flat)](https://github.com/tomodian/release/stargazers) - CLI for Keep-a-changelog formatted changelogs.
- [relimpact](https://github.com/hashmap-kz/relimpact) [![GitHub stars](https://img.shields.io/github/stars/hashmap-kz/relimpact?style=flat)](https://github.com/hashmap-kz/relimpact/stargazers) - Fast API compatibility reports for Go projects.
- [remote-touchpad](https://github.com/Unrud/remote-touchpad) [![GitHub stars](https://img.shields.io/github/stars/Unrud/remote-touchpad?style=flat)](https://github.com/Unrud/remote-touchpad/stargazers) - Control mouse and keyboard from a smartphone.
- [repeat](https://github.com/ssgreg/repeat) [![GitHub stars](https://img.shields.io/github/stars/ssgreg/repeat?style=flat)](https://github.com/ssgreg/repeat/stargazers) - Go implementation of different backoff strategies useful for retrying operations and heartbeating.
- [request](https://github.com/mozillazg/request) [![GitHub stars](https://img.shields.io/github/stars/mozillazg/request?style=flat)](https://github.com/mozillazg/request/stargazers) - Go HTTP Requests for Humans™.
- [rerun](https://github.com/ivpusic/rerun) [![GitHub stars](https://img.shields.io/github/stars/ivpusic/rerun?style=flat)](https://github.com/ivpusic/rerun/stargazers) - Recompiling and rerunning go apps when source changes.
- [rest-go](https://github.com/edermanoel94/rest-go) [![GitHub stars](https://img.shields.io/github/stars/edermanoel94/rest-go?style=flat)](https://github.com/edermanoel94/rest-go/stargazers) - A package that provide many helpful methods for working with rest api.
- [retro](https://github.com/goioc/retro) [![GitHub stars](https://img.shields.io/github/stars/goioc/retro?style=flat)](https://github.com/goioc/retro/stargazers) - Handy retry-on-error library with extensive flexibility (backoff strategies, caps, etc).
- [retry](https://github.com/kamilsk/retry) [![GitHub stars](https://img.shields.io/github/stars/kamilsk/retry?style=flat)](https://github.com/kamilsk/retry/stargazers) - The most advanced functional mechanism to perform actions repetitively until successful.
- [retry](https://github.com/percolate/retry) [![GitHub stars](https://img.shields.io/github/stars/percolate/retry?style=flat)](https://github.com/percolate/retry/stargazers) - A simple but highly configurable retry package for Go.
- [retry](https://github.com/thedevsaddam/retry) [![GitHub stars](https://img.shields.io/github/stars/thedevsaddam/retry?style=flat)](https://github.com/thedevsaddam/retry/stargazers) - Simple and easy retry mechanism package for Go.
- [retry](https://github.com/shafreeck/retry) [![GitHub stars](https://img.shields.io/github/stars/shafreeck/retry?style=flat)](https://github.com/shafreeck/retry/stargazers) - A pretty simple library to ensure your work to be done.
- [retry-go](https://github.com/avast/retry-go) [![GitHub stars](https://img.shields.io/github/stars/avast/retry-go?style=flat)](https://github.com/avast/retry-go/stargazers) - Simple library for retry mechanism.
- [retry-go](https://github.com/rafaeljesus/retry-go) [![GitHub stars](https://img.shields.io/github/stars/rafaeljesus/retry-go?style=flat)](https://github.com/rafaeljesus/retry-go/stargazers) - Retrying made simple and easy for golang.
- [robustly](https://github.com/VividCortex/robustly) [![GitHub stars](https://img.shields.io/github/stars/VividCortex/robustly?style=flat)](https://github.com/VividCortex/robustly/stargazers) - Runs functions resiliently, catching and restarting panics.
- [rospo](https://github.com/ferama/rospo) [![GitHub stars](https://img.shields.io/github/stars/ferama/rospo?style=flat)](https://github.com/ferama/rospo/stargazers) - Simple and reliable ssh tunnels with embedded ssh server in Golang.
- [scan](https://github.com/blockloop/scan) [![GitHub stars](https://img.shields.io/github/stars/blockloop/scan?style=flat)](https://github.com/blockloop/scan/stargazers) - Scan golang `sql.Rows` directly to structs, slices, or primitive types.
- [scan](https://github.com/wroge/scan) [![GitHub stars](https://img.shields.io/github/stars/wroge/scan?style=flat)](https://github.com/wroge/scan/stargazers) - Scan sql rows into any type powered by generics.
- [scany](https://github.com/georgysavva/scany) [![GitHub stars](https://img.shields.io/github/stars/georgysavva/scany?style=flat)](https://github.com/georgysavva/scany/stargazers) - Library for scanning data from a database into Go structs and more.
- [serve](https://github.com/syntaqx/serve) [![GitHub stars](https://img.shields.io/github/stars/syntaqx/serve?style=flat)](https://github.com/syntaqx/serve/stargazers) - A static http server anywhere you need.
- [sesh](https://github.com/joshmedeski/sesh) [![GitHub stars](https://img.shields.io/github/stars/joshmedeski/sesh?style=flat)](https://github.com/joshmedeski/sesh/stargazers) - Sesh is a CLI that helps you create and manage tmux sessions quickly and easily using zoxide.
- [set](https://github.com/nofeaturesonlybugs/set) [![GitHub stars](https://img.shields.io/github/stars/nofeaturesonlybugs/set?style=flat)](https://github.com/nofeaturesonlybugs/set/stargazers) - Performant and flexible struct mapping and loose type conversion.
- [shutdown](https://github.com/ztrue/shutdown) [![GitHub stars](https://img.shields.io/github/stars/ztrue/shutdown?style=flat)](https://github.com/ztrue/shutdown/stargazers) - App shutdown hooks for `os.Signal` handling.
- [silk](https://github.com/chrispassas/silk) [![GitHub stars](https://img.shields.io/github/stars/chrispassas/silk?style=flat)](https://github.com/chrispassas/silk/stargazers) - Read silk netflow files.
- [slice](https://github.com/psampaz/slice) [![GitHub stars](https://img.shields.io/github/stars/psampaz/slice?style=flat)](https://github.com/psampaz/slice/stargazers) - Type-safe functions for common Go slice operations.
- [sliceconv](https://github.com/Henry-Sarabia/sliceconv) [![GitHub stars](https://img.shields.io/github/stars/Henry-Sarabia/sliceconv?style=flat)](https://github.com/Henry-Sarabia/sliceconv/stargazers) - Slice conversion between primitive types.
- [slicer](https://github.com/leaanthony/slicer) [![GitHub stars](https://img.shields.io/github/stars/leaanthony/slicer?style=flat)](https://github.com/leaanthony/slicer/stargazers) - Makes working with slices easier.
- [sorty](https://github.com/jfcg/sorty) [![GitHub stars](https://img.shields.io/github/stars/jfcg/sorty?style=flat)](https://github.com/jfcg/sorty/stargazers) - Fast Concurrent / Parallel Sorting.
- [sqlex](https://github.com/go-sqlex/sqlex) [![GitHub stars](https://img.shields.io/github/stars/go-sqlex/sqlex?style=flat)](https://github.com/go-sqlex/sqlex/stargazers) - Drop-in modernization of jmoiron/sqlx with fixed SQL lexer bugs, automatic IN-clause expansion, pluggable hooks, and unified DB/Tx/Conn interfaces.
- [sqlx](https://github.com/jmoiron/sqlx) [![GitHub stars](https://img.shields.io/github/stars/jmoiron/sqlx?style=flat)](https://github.com/jmoiron/sqlx/stargazers) - provides a set of extensions on top of the excellent built-in database/sql package.
- [sqlz](https://github.com/rfberaldo/sqlz) [![GitHub stars](https://img.shields.io/github/stars/rfberaldo/sqlz?style=flat)](https://github.com/rfberaldo/sqlz/stargazers) - Extension for the database/sql package, adding named queries, struct scanning, and batch operations.
- [sshman](https://github.com/shoobyban/sshman) [![GitHub stars](https://img.shields.io/github/stars/shoobyban/sshman?style=flat)](https://github.com/shoobyban/sshman/stargazers) - SSH Manager for authorized_keys files on multiple remote servers.
- [stacktower](https://github.com/stacktower-io/stacktower) [![GitHub stars](https://img.shields.io/github/stars/stacktower-io/stacktower?style=flat)](https://github.com/stacktower-io/stacktower/stargazers) - Visualize dependency graphs as physical tower structures, inspired by XKCD #2347.
- [statiks](https://github.com/janiltonmaciel/statiks) [![GitHub stars](https://img.shields.io/github/stars/janiltonmaciel/statiks?style=flat)](https://github.com/janiltonmaciel/statiks/stargazers) - Fast, zero-configuration, static HTTP filer server.
- [Storm](https://github.com/asdine/storm) [![GitHub stars](https://img.shields.io/github/stars/asdine/storm?style=flat)](https://github.com/asdine/storm/stargazers) - Simple and powerful toolkit for BoltDB.
- [structs](https://github.com/PumpkinSeed/structs) [![GitHub stars](https://img.shields.io/github/stars/PumpkinSeed/structs?style=flat)](https://github.com/PumpkinSeed/structs/stargazers) - Implement simple functions to manipulate structs.
- [throttle](https://github.com/yudppp/throttle) [![GitHub stars](https://img.shields.io/github/stars/yudppp/throttle?style=flat)](https://github.com/yudppp/throttle/stargazers) - Throttle is an object that will perform exactly one action per duration.
- [tik](https://github.com/andy2046/tik) [![GitHub stars](https://img.shields.io/github/stars/andy2046/tik?style=flat)](https://github.com/andy2046/tik/stargazers) - Simple and easy timing wheel package for Go.
- [tome](https://github.com/cyruzin/tome) [![GitHub stars](https://img.shields.io/github/stars/cyruzin/tome?style=flat)](https://github.com/cyruzin/tome/stargazers) - Tome was designed to paginate simple RESTful APIs.
- [toolbox](https://github.com/viant/toolbox) [![GitHub stars](https://img.shields.io/github/stars/viant/toolbox?style=flat)](https://github.com/viant/toolbox/stargazers) - Slice, map, multimap, struct, function, data conversion utilities. Service router, macro evaluator, tokenizer.
- [UNIS](https://github.com/esemplastic/unis) [![GitHub stars](https://img.shields.io/github/stars/esemplastic/unis?style=flat)](https://github.com/esemplastic/unis/stargazers) - Common Architecture™ for String Utilities in Go.
- [upterm](https://github.com/owenthereal/upterm) [![GitHub stars](https://img.shields.io/github/stars/owenthereal/upterm?style=flat)](https://github.com/owenthereal/upterm/stargazers) - A tool for developers to share terminal/tmux sessions securely over the web. It’s perfect for remote pair programming, accessing computers behind NATs/firewalls, remote debugging, and more.
- [usql](https://github.com/knq/usql) [![GitHub stars](https://img.shields.io/github/stars/knq/usql?style=flat)](https://github.com/knq/usql/stargazers) - usql is a universal command-line interface for SQL databases.
- [util](https://github.com/shomali11/util) [![GitHub stars](https://img.shields.io/github/stars/shomali11/util?style=flat)](https://github.com/shomali11/util/stargazers) - Collection of useful utility functions. (strings, concurrency, manipulations, ...).
- [watchhttp](https://github.com/nikolaydubina/watchhttp) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/watchhttp?style=flat)](https://github.com/nikolaydubina/watchhttp/stargazers) - Run command periodically and expose latest STDOUT or its rich delta as HTTP endpoint.
- [wifiqr](https://github.com/reugn/wifiqr) [![GitHub stars](https://img.shields.io/github/stars/reugn/wifiqr?style=flat)](https://github.com/reugn/wifiqr/stargazers) - Wi-Fi QR Code Generator.
- [wuzz](https://github.com/asciimoo/wuzz) [![GitHub stars](https://img.shields.io/github/stars/asciimoo/wuzz?style=flat)](https://github.com/asciimoo/wuzz/stargazers) - Interactive cli tool for HTTP inspection.
- [xferspdy](https://github.com/monmohan/xferspdy) [![GitHub stars](https://img.shields.io/github/stars/monmohan/xferspdy?style=flat)](https://github.com/monmohan/xferspdy/stargazers) - Xferspdy provides binary diff and patch library in golang.
- [xpool](https://github.com/peczenyj/xpool) [![GitHub stars](https://img.shields.io/github/stars/peczenyj/xpool?style=flat)](https://github.com/peczenyj/xpool/stargazers) - Yet another golang type safe object pool using generics.
- [yogo](https://github.com/antham/yogo) [![GitHub stars](https://img.shields.io/github/stars/antham/yogo?style=flat)](https://github.com/antham/yogo/stargazers) - Check yopmail mails from command line.

**[⬆ back to top](#contents)**

## UUID

_Libraries for working with UUIDs._

- [fastuuid](https://github.com/rekby/fastuuid) [![GitHub stars](https://img.shields.io/github/stars/rekby/fastuuid?style=flat)](https://github.com/rekby/fastuuid/stargazers) - Fast generate UUIDv4 as string or bytes.
- [goid](https://github.com/jakehl/goid) [![GitHub stars](https://img.shields.io/github/stars/jakehl/goid?style=flat)](https://github.com/jakehl/goid/stargazers) - Generate and Parse RFC4122 compliant V4 UUIDs.
- [gouid](https://github.com/twharmon/gouid) [![GitHub stars](https://img.shields.io/github/stars/twharmon/gouid?style=flat)](https://github.com/twharmon/gouid/stargazers) - Generate cryptographically secure random string IDs with just one allocation.
- [guid](https://github.com/sdrapkin/guid) [![GitHub stars](https://img.shields.io/github/stars/sdrapkin/guid?style=flat)](https://github.com/sdrapkin/guid/stargazers) - Fast cryptographically safe Guid generator for Go (~10x faster than `uuid`).
- [nanoid](https://github.com/aidarkhanov/nanoid) [![GitHub stars](https://img.shields.io/github/stars/aidarkhanov/nanoid?style=flat)](https://github.com/aidarkhanov/nanoid/stargazers) - A tiny and efficient Go unique string ID generator.
- [sno](https://github.com/muyo/sno) [![GitHub stars](https://img.shields.io/github/stars/muyo/sno?style=flat)](https://github.com/muyo/sno/stargazers) - Compact, sortable and fast unique IDs with embedded metadata.
- [ulid](https://github.com/oklog/ulid) [![GitHub stars](https://img.shields.io/github/stars/oklog/ulid?style=flat)](https://github.com/oklog/ulid/stargazers) - Go implementation of ULID (Universally Unique Lexicographically Sortable Identifier).
- [uniq](https://gitlab.com/skilstak/code/go/uniq) - No hassle safe, fast unique identifiers with commands.
- [uuid](https://github.com/agext/uuid) [![GitHub stars](https://img.shields.io/github/stars/agext/uuid?style=flat)](https://github.com/agext/uuid/stargazers) - Generate, encode, and decode UUIDs v1 with fast or cryptographic-quality random node identifier.
- [uuid](https://github.com/gofrs/uuid) [![GitHub stars](https://img.shields.io/github/stars/gofrs/uuid?style=flat)](https://github.com/gofrs/uuid/stargazers) - Implementation of Universally Unique Identifier (UUID). Supports both creation and parsing of UUIDs. Actively maintained fork of satori uuid.
- [uuid](https://github.com/google/uuid) [![GitHub stars](https://img.shields.io/github/stars/google/uuid?style=flat)](https://github.com/google/uuid/stargazers) - Go package for UUIDs based on RFC 4122 and DCE 1.1: Authentication and Security Services.
- [uuidcheck](https://github.com/ashwingopalsamy/uuidcheck) [![GitHub stars](https://img.shields.io/github/stars/ashwingopalsamy/uuidcheck?style=flat)](https://github.com/ashwingopalsamy/uuidcheck/stargazers) - A tiny, dependency-free Go library that validates UUIDs against standard RFC 4122 formatting, converts UUIDv7() into UTC timestamps.
- [wuid](https://github.com/edwingeng/wuid) [![GitHub stars](https://img.shields.io/github/stars/edwingeng/wuid?style=flat)](https://github.com/edwingeng/wuid/stargazers) - An extremely fast globally unique number generator.
- [xid](https://github.com/rs/xid) [![GitHub stars](https://img.shields.io/github/stars/rs/xid?style=flat)](https://github.com/rs/xid/stargazers) - Xid is a globally unique id generator library, ready to be safely used directly in your server code.

**[⬆ back to top](#contents)**

## Validation

_Libraries for validation._

- [checkdigit](https://github.com/osamingo/checkdigit) [![GitHub stars](https://img.shields.io/github/stars/osamingo/checkdigit?style=flat)](https://github.com/osamingo/checkdigit/stargazers) - Provide check digit algorithms (Luhn, Verhoeff, Damm) and calculators (ISBN, EAN, JAN, UPC, etc.).
- [go-validator](https://github.com/tiendc/go-validator) [![GitHub stars](https://img.shields.io/github/stars/tiendc/go-validator?style=flat)](https://github.com/tiendc/go-validator/stargazers) - Validation library using Generics.
- [gody](https://github.com/guiferpa/gody) [![GitHub stars](https://img.shields.io/github/stars/guiferpa/gody?style=flat)](https://github.com/guiferpa/gody/stargazers) - :balloon: A lightweight struct validator for Go.
- [govalid](https://github.com/twharmon/govalid) [![GitHub stars](https://img.shields.io/github/stars/twharmon/govalid?style=flat)](https://github.com/twharmon/govalid/stargazers) - Fast, tag-based validation for structs.
- [govalidator](https://github.com/asaskevich/govalidator) [![GitHub stars](https://img.shields.io/github/stars/asaskevich/govalidator?style=flat)](https://github.com/asaskevich/govalidator/stargazers) - Validators and sanitizers for strings, numerics, slices and structs.
- [govalidator](https://github.com/thedevsaddam/govalidator) [![GitHub stars](https://img.shields.io/github/stars/thedevsaddam/govalidator?style=flat)](https://github.com/thedevsaddam/govalidator/stargazers) - Validate Golang request data with simple rules. Highly inspired by Laravel's request validation.
- [govy](https://github.com/nobl9/govy) [![GitHub stars](https://img.shields.io/github/stars/nobl9/govy?style=flat)](https://github.com/nobl9/govy/stargazers) - strongly-typed validation rules over functional interface, powered by generics and reflection free with heavy focus on crafting clear and information-rich error messages.
- [hvalid](https://github.com/lyonnee/hvalid) [![GitHub stars](https://img.shields.io/github/stars/lyonnee/hvalid?style=flat)](https://github.com/lyonnee/hvalid/stargazers) hvalid is a lightweight validation library written in Go language. It provides a custom validator interface and a series of common validation functions to help developers quickly implement data validation.
- [jio](https://github.com/faceair/jio) [![GitHub stars](https://img.shields.io/github/stars/faceair/jio?style=flat)](https://github.com/faceair/jio/stargazers) - jio is a json schema validator similar to [joi](https://github.com/hapijs/joi) [![GitHub stars](https://img.shields.io/github/stars/hapijs/joi?style=flat)](https://github.com/hapijs/joi/stargazers).
- [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) [![GitHub stars](https://img.shields.io/github/stars/go-ozzo/ozzo-validation?style=flat)](https://github.com/go-ozzo/ozzo-validation/stargazers) - Supports validation of various data types (structs, strings, maps, slices, etc.) with configurable and extensible validation rules specified in usual code constructs instead of struct tags.
- [validate](https://github.com/gookit/validate) [![GitHub stars](https://img.shields.io/github/stars/gookit/validate?style=flat)](https://github.com/gookit/validate/stargazers) - Go package for data validation and filtering. support validate Map, Struct, Request(Form, JSON, url.Values, Uploaded Files) data and more features.
- [validate](https://github.com/gobuffalo/validate) [![GitHub stars](https://img.shields.io/github/stars/gobuffalo/validate?style=flat)](https://github.com/gobuffalo/validate/stargazers) - This package provides a framework for writing validations for Go applications.
- [validator](https://github.com/go-playground/validator) [![GitHub stars](https://img.shields.io/github/stars/go-playground/validator?style=flat)](https://github.com/go-playground/validator/stargazers) - Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving.
- [Validator](https://github.com/go-the-way/validator) [![GitHub stars](https://img.shields.io/github/stars/go-the-way/validator?style=flat)](https://github.com/go-the-way/validator/stargazers) - A lightweight model validator written in Go.Contains VFs:Min, Max, MinLength, MaxLength, Length, Enum, Regex.
- [valix](https://github.com/marrow16/valix) [![GitHub stars](https://img.shields.io/github/stars/marrow16/valix?style=flat)](https://github.com/marrow16/valix/stargazers) Go package for validating requests
- [Zog](https://github.com/Oudwins/zog) [![GitHub stars](https://img.shields.io/github/stars/Oudwins/zog?style=flat)](https://github.com/Oudwins/zog/stargazers) - A [Zod](https://github.com/colinhacks/zod) [![GitHub stars](https://img.shields.io/github/stars/colinhacks/zod?style=flat)](https://github.com/colinhacks/zod/stargazers) inspired schema builder for runtime value parsing and validation.
  **[⬆ back to top](#contents)**

## Version Control

_Libraries for version control._

- [cli](https://gitlab.com/gitlab-org/cli) - An open-source GitLab command line tool bringing GitLab's cool features to your command line.
- [froggit-go](https://github.com/jfrog/froggit-go) [![GitHub stars](https://img.shields.io/github/stars/jfrog/froggit-go?style=flat)](https://github.com/jfrog/froggit-go/stargazers) - Froggit-Go is a Go library, allowing to perform actions on VCS providers.
- [ggc](https://github.com/bmf-san/ggc) [![GitHub stars](https://img.shields.io/github/stars/bmf-san/ggc?style=flat)](https://github.com/bmf-san/ggc/stargazers) - A Git CLI tool with both traditional command-line and interactive incremental-search UI, workflow support, and configurable keybindings.
- [git-courer](https://github.com/Alejandro-M-P/git-courer) [![GitHub stars](https://img.shields.io/github/stars/Alejandro-M-P/git-courer?style=flat)](https://github.com/Alejandro-M-P/git-courer/stargazers) - Local MCP server for Git operations using Ollama to save tokens and prevent secret leakage.
- [git2go](https://github.com/libgit2/git2go) [![GitHub stars](https://img.shields.io/github/stars/libgit2/git2go?style=flat)](https://github.com/libgit2/git2go/stargazers) - Go bindings for libgit2.
- [githooks](https://github.com/gabyx/githooks) [![GitHub stars](https://img.shields.io/github/stars/gabyx/githooks?style=flat)](https://github.com/gabyx/githooks/stargazers) - Per-repo and shared Git hooks with version control and auto update.
- [gitty](https://github.com/Omibranch/gitty) [![GitHub stars](https://img.shields.io/github/stars/Omibranch/gitty?style=flat)](https://github.com/Omibranch/gitty/stargazers) - Single-binary Git/GitHub CLI that replaces add→commit→push with one command; human-readable syntax, no external dependencies.
- [go-git](https://github.com/go-git/go-git) [![GitHub stars](https://img.shields.io/github/stars/go-git/go-git?style=flat)](https://github.com/go-git/go-git/stargazers) - highly extensible Git implementation in pure Go.
- [go-vcs](https://github.com/sourcegraph/go-vcs) [![GitHub stars](https://img.shields.io/github/stars/sourcegraph/go-vcs?style=flat)](https://github.com/sourcegraph/go-vcs/stargazers) - manipulate and inspect VCS repositories in Go.
- [hercules](https://github.com/src-d/hercules) [![GitHub stars](https://img.shields.io/github/stars/src-d/hercules?style=flat)](https://github.com/src-d/hercules/stargazers) - gaining advanced insights from Git repository history.
- [hgo](https://github.com/beyang/hgo) [![GitHub stars](https://img.shields.io/github/stars/beyang/hgo?style=flat)](https://github.com/beyang/hgo/stargazers) - Hgo is a collection of Go packages providing read-access to local Mercurial repositories.

**[⬆ back to top](#contents)**

## Video

_Libraries for manipulating video._

- [gmf](https://github.com/3d0c/gmf) [![GitHub stars](https://img.shields.io/github/stars/3d0c/gmf?style=flat)](https://github.com/3d0c/gmf/stargazers) - Go bindings for FFmpeg av\* libraries.
- [go-astiav](https://github.com/asticode/go-astiav) [![GitHub stars](https://img.shields.io/github/stars/asticode/go-astiav?style=flat)](https://github.com/asticode/go-astiav/stargazers) - Better C bindings for ffmpeg in GO.
- [go-astisub](https://github.com/asticode/go-astisub) [![GitHub stars](https://img.shields.io/github/stars/asticode/go-astisub?style=flat)](https://github.com/asticode/go-astisub/stargazers) - Manipulate subtitles in GO (.srt, .stl, .ttml, .webvtt, .ssa/.ass, teletext, .smi, etc.).
- [go-astits](https://github.com/asticode/go-astits) [![GitHub stars](https://img.shields.io/github/stars/asticode/go-astits?style=flat)](https://github.com/asticode/go-astits/stargazers) - Parse and demux MPEG Transport Streams (.ts) natively in GO.
- [go-mpd](https://github.com/unki2aut/go-mpd) [![GitHub stars](https://img.shields.io/github/stars/unki2aut/go-mpd?style=flat)](https://github.com/unki2aut/go-mpd/stargazers) - Parser and generator library for MPEG-DASH manifest files.
- [goav](https://github.com/giorgisio/goav) [![GitHub stars](https://img.shields.io/github/stars/giorgisio/goav?style=flat)](https://github.com/giorgisio/goav/stargazers) - Comprehensive Go bindings for FFmpeg.
- [gortsplib](https://github.com/aler9/gortsplib) [![GitHub stars](https://img.shields.io/github/stars/aler9/gortsplib?style=flat)](https://github.com/aler9/gortsplib/stargazers) - Pure Go RTSP server and client library.
- [hls-m3u8](https://github.com/Eyevinn/hls-m3u8) [![GitHub stars](https://img.shields.io/github/stars/Eyevinn/hls-m3u8?style=flat)](https://github.com/Eyevinn/hls-m3u8/stargazers) - Parser and generator for HLS (M3U8) playlists; kept up to date with the spec.
- [libvlc-go](https://github.com/adrg/libvlc-go) [![GitHub stars](https://img.shields.io/github/stars/adrg/libvlc-go?style=flat)](https://github.com/adrg/libvlc-go/stargazers) - Go bindings for libvlc 2.X/3.X/4.X (used by the VLC media player).
- [manifestor](https://github.com/alanzng/manifestor) [![GitHub stars](https://img.shields.io/github/stars/alanzng/manifestor?style=flat)](https://github.com/alanzng/manifestor/stargazers) - Zero-dependency library for parsing, filtering, transforming, and building HLS and DASH manifests.
- [mp4ff](https://github.com/Eyevinn/mp4ff) [![GitHub stars](https://img.shields.io/github/stars/Eyevinn/mp4ff?style=flat)](https://github.com/Eyevinn/mp4ff/stargazers) - Library and tools for working with MP4 files containing video, audio, subtitles, or metadata.
- [v4l](https://github.com/korandiz/v4l) [![GitHub stars](https://img.shields.io/github/stars/korandiz/v4l?style=flat)](https://github.com/korandiz/v4l/stargazers) - Video capture library for Linux, written in Go.

**[⬆ back to top](#contents)**

## Web Frameworks

_Full stack web frameworks._

- [Atreugo](https://github.com/savsgio/atreugo) [![GitHub stars](https://img.shields.io/github/stars/savsgio/atreugo?style=flat)](https://github.com/savsgio/atreugo/stargazers) - High performance and extensible micro web framework with zero memory allocations in hot paths.
- [Barf](https://github.com/opensaucerer/barf) [![GitHub stars](https://img.shields.io/github/stars/opensaucerer/barf?style=flat)](https://github.com/opensaucerer/barf/stargazers) - Basically, A Remarkable Framework for building JSON-based web APIs. It is entirely unobtrusive and re-invents no wheel. It is crafted such that getting started is easy and quick while being flexible enough for more complex use cases.
- [Beego](https://github.com/beego/beego) [![GitHub stars](https://img.shields.io/github/stars/beego/beego?style=flat)](https://github.com/beego/beego/stargazers) - beego is an open-source, high-performance web framework for the Go programming language.
- [Confetti Framework](https://confetti-framework.github.io/docs/) - Confetti is a Go web application framework with an expressive, elegant syntax. Confetti combines the elegance of Laravel and the simplicity of Go.
- [Don](https://github.com/abemedia/go-don) [![GitHub stars](https://img.shields.io/github/stars/abemedia/go-don?style=flat)](https://github.com/abemedia/go-don/stargazers) - A highly performant and simple to use API framework.
- [doors](https://github.com/doors-dev/doors) [![GitHub stars](https://img.shields.io/github/stars/doors-dev/doors?style=flat)](https://github.com/doors-dev/doors/stargazers) - Server-driven framework for building stateful, reactive web applications entirely in Go.
- [Echo](https://github.com/labstack/echo) [![GitHub stars](https://img.shields.io/github/stars/labstack/echo?style=flat)](https://github.com/labstack/echo/stargazers) - High performance, minimalist Go web framework.
- [Fastschema](https://github.com/fastschema/fastschema) [![GitHub stars](https://img.shields.io/github/stars/fastschema/fastschema?style=flat)](https://github.com/fastschema/fastschema/stargazers) - A flexible Go web framework and Headless CMS.
- [Fiber](https://github.com/gofiber/fiber) [![GitHub stars](https://img.shields.io/github/stars/gofiber/fiber?style=flat)](https://github.com/gofiber/fiber/stargazers) - An Express.js inspired web framework build on Fasthttp.
- [Flamingo](https://github.com/i-love-flamingo/flamingo) [![GitHub stars](https://img.shields.io/github/stars/i-love-flamingo/flamingo?style=flat)](https://github.com/i-love-flamingo/flamingo/stargazers) - Framework for pluggable web projects. Including a concept for modules and offering features for DI, Configareas, i18n, template engines, graphql, observability, security, events, routing & reverse routing etc.
- [Flamingo Commerce](https://github.com/i-love-flamingo/flamingo-commerce) [![GitHub stars](https://img.shields.io/github/stars/i-love-flamingo/flamingo-commerce?style=flat)](https://github.com/i-love-flamingo/flamingo-commerce/stargazers) - Providing e-commerce features using clean architecture like DDD and ports and adapters, that you can use to build flexible e-commerce applications.
- [Fuego](https://github.com/go-fuego/fuego) [![GitHub stars](https://img.shields.io/github/stars/go-fuego/fuego?style=flat)](https://github.com/go-fuego/fuego/stargazers) - The framework for busy Go developers! Web framework generating OpenAPI 3 spec from source code.
- [Gin](https://github.com/gin-gonic/gin) [![GitHub stars](https://img.shields.io/github/stars/gin-gonic/gin?style=flat)](https://github.com/gin-gonic/gin/stargazers) - Gin is a web framework written in Go! It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity.
- [Ginrpc](https://github.com/xxjwxc/ginrpc) [![GitHub stars](https://img.shields.io/github/stars/xxjwxc/ginrpc?style=flat)](https://github.com/xxjwxc/ginrpc/stargazers) - Gin parameter automatic binding tool,gin rpc tools.
- [go-api-boot](https://github.com/SaiNageswarS/go-api-boot) [![GitHub stars](https://img.shields.io/github/stars/SaiNageswarS/go-api-boot?style=flat)](https://github.com/SaiNageswarS/go-api-boot/stargazers) - A gRpc-first micro-service framework. Features include ODM support for Mongo, cloud resource support (AWS/Azure/Google), and a fluent dependency injection which is customized for gRpc. Additionally, grpc-web is supported directly, enabling browser access to all gRpc APIs without a proxy.
- [Goa](https://github.com/goadesign/goa) [![GitHub stars](https://img.shields.io/github/stars/goadesign/goa?style=flat)](https://github.com/goadesign/goa/stargazers) - Goa provides a holistic approach for developing remote APIs and microservices in Go.
- [GoFr](https://github.com/gofr-dev/gofr) [![GitHub stars](https://img.shields.io/github/stars/gofr-dev/gofr?style=flat)](https://github.com/gofr-dev/gofr/stargazers) - Gofr is an opinionated microservice development framework.
- [GoFrame](https://github.com/gogf/gf) [![GitHub stars](https://img.shields.io/github/stars/gogf/gf?style=flat)](https://github.com/gogf/gf/stargazers) - GoFrame is a modular, powerful, high-performance and enterprise-class application development framework of Golang.
- [Gone](https://github.com/gone-io/gone) [![GitHub stars](https://img.shields.io/github/stars/gone-io/gone?style=flat)](https://github.com/gone-io/gone/stargazers) - A lightweight dependency injection and web framework inspired by Spring.
- [goravel](https://github.com/goravel/goravel) [![GitHub stars](https://img.shields.io/github/stars/goravel/goravel?style=flat)](https://github.com/goravel/goravel/stargazers) - A Laravel-inspired web framework with ORM, authentication, queue, task scheduling, and more built-in features.
- [Goyave](https://github.com/go-goyave/goyave) [![GitHub stars](https://img.shields.io/github/stars/go-goyave/goyave?style=flat)](https://github.com/go-goyave/goyave/stargazers) - Feature-complete REST API framework aimed at clean code and fast development, with powerful built-in functionalities.
- [Hertz](https://github.com/cloudwego/hertz) [![GitHub stars](https://img.shields.io/github/stars/cloudwego/hertz?style=flat)](https://github.com/cloudwego/hertz/stargazers) - A high-performance and strong-extensibility Go HTTP framework that helps developers build microservices.
- [hiboot](https://github.com/hidevopsio/hiboot) [![GitHub stars](https://img.shields.io/github/stars/hidevopsio/hiboot?style=flat)](https://github.com/hidevopsio/hiboot/stargazers) - hiboot is a high performance web application framework with auto configuration and dependency injection support.
- [httpsuite](https://github.com/rluders/httpsuite) [![GitHub stars](https://img.shields.io/github/stars/rluders/httpsuite?style=flat)](https://github.com/rluders/httpsuite/stargazers) - HTTP request parsing and RFC 9457 problem responses for Go, with a stdlib-only core and optional validation.
- [Huma](https://github.com/danielgtaylor/huma/) [![GitHub stars](https://img.shields.io/github/stars/danielgtaylor/huma/?style=flat)](https://github.com/danielgtaylor/huma//stargazers) - Framework for modern REST/GraphQL APIs with built-in OpenAPI 3, generated documentation, and a CLI.
- [iWF](https://github.com/indeedeng/iwf) [![GitHub stars](https://img.shields.io/github/stars/indeedeng/iwf?style=flat)](https://github.com/indeedeng/iwf/stargazers) - iWF is an all-in-one platform for developing long-running business processes. It offers a convenient abstraction for utilizing databases, ElasticSearch, message queues, durable timers, and more, with a clean, simple, and user-friendly interface.
- [Lit](https://github.com/jvcoutinho/lit) [![GitHub stars](https://img.shields.io/github/stars/jvcoutinho/lit?style=flat)](https://github.com/jvcoutinho/lit/stargazers) - Highly performant declarative web framework for Golang, aiming for simplicity and quality of life.
- [Microservice](https://github.com/claygod/microservice) [![GitHub stars](https://img.shields.io/github/stars/claygod/microservice?style=flat)](https://github.com/claygod/microservice/stargazers) - The framework for the creation of microservices, written in Golang.
- [NotNet](https://github.com/nottechdm/notnet) [![GitHub stars](https://img.shields.io/github/stars/nottechdm/notnet?style=flat)](https://github.com/nottechdm/notnet/stargazers) - A lightweight Go framework for building fast, ergonomic RESTful APIs with middleware and flexible routing.
- [patron](https://github.com/beatlabs/patron) [![GitHub stars](https://img.shields.io/github/stars/beatlabs/patron?style=flat)](https://github.com/beatlabs/patron/stargazers) - Patron is a microservice framework following best cloud practices with a focus on productivity.
- [Pnutmux](https://gitlab.com/fruitygo/pnutmux) - Pnutmux is a powerful Go web framework that uses regex for matching and handling HTTP requests. It offers features such as CORS handling, structured logging, URL parameters extraction, middlewares, and concurrency limiting.
- [Revel](https://github.com/revel/revel) [![GitHub stars](https://img.shields.io/github/stars/revel/revel?style=flat)](https://github.com/revel/revel/stargazers) - High-productivity web framework for the Go language.
- [rk-boot](https://github.com/rookie-ninja/rk-boot) [![GitHub stars](https://img.shields.io/github/stars/rookie-ninja/rk-boot?style=flat)](https://github.com/rookie-ninja/rk-boot/stargazers) - A bootstrapper library for building enterprise go microservice with Gin and gRPC quickly and easily.
- [Ronykit](https://github.com/clubpay/ronykit) [![GitHub stars](https://img.shields.io/github/stars/clubpay/ronykit?style=flat)](https://github.com/clubpay/ronykit/stargazers) - Web framework with pluggable architecture and very performant.
- [rux](https://github.com/gookit/rux) [![GitHub stars](https://img.shields.io/github/stars/gookit/rux?style=flat)](https://github.com/gookit/rux/stargazers) - Simple and fast web framework for build golang HTTP applications.
- [templui](https://github.com/axzilla/templui) [![GitHub stars](https://img.shields.io/github/stars/axzilla/templui?style=flat)](https://github.com/axzilla/templui/stargazers) - Modern UI Components for Go & Templ.
- [togo](https://github.com/togo-framework/togo) [![GitHub stars](https://img.shields.io/github/stars/togo-framework/togo?style=flat)](https://github.com/togo-framework/togo/stargazers) - Full-stack framework that ships your Go backend and React frontend as a single binary; a Laravel-artisan-grade CLI.
- [uAdmin](https://github.com/uadmin/uadmin) [![GitHub stars](https://img.shields.io/github/stars/uadmin/uadmin?style=flat)](https://github.com/uadmin/uadmin/stargazers) - Fully featured web framework for Golang, inspired by Django.
- [WebGo](https://github.com/naughtygopher/webgo) [![GitHub stars](https://img.shields.io/github/stars/naughtygopher/webgo?style=flat)](https://github.com/naughtygopher/webgo/stargazers) - A micro-framework to build web apps with handler chaining, middleware, and context injection. With standard library-compliant HTTP handlers (i.e., `http.HandlerFunc`)..
- [Xun](https://github.com/yaitoo/xun) [![GitHub stars](https://img.shields.io/github/stars/yaitoo/xun?style=flat)](https://github.com/yaitoo/xun/stargazers) - Web framework built on Go's built-in html/template and net/http package’s router. It is designed to be lightweight, fast, and easy to use while providing a simple and intuitive API for building web applications with advanced features such as middleware, routing, and template rendering.
- [Yokai](https://github.com/ankorstore/yokai) [![GitHub stars](https://img.shields.io/github/stars/ankorstore/yokai?style=flat)](https://github.com/ankorstore/yokai/stargazers) - Simple, modular, and observable Go framework for backend applications.

**[⬆ back to top](#contents)**

### Middlewares

#### Actual middlewares

- [client-timing](https://github.com/posener/client-timing) [![GitHub stars](https://img.shields.io/github/stars/posener/client-timing?style=flat)](https://github.com/posener/client-timing/stargazers) - An HTTP client for Server-Timing header.
- [CORS](https://github.com/rs/cors) [![GitHub stars](https://img.shields.io/github/stars/rs/cors?style=flat)](https://github.com/rs/cors/stargazers) - Easily add CORS capabilities to your API.
- [echo-middleware](https://github.com/faabiosr/echo-middleware) [![GitHub stars](https://img.shields.io/github/stars/faabiosr/echo-middleware?style=flat)](https://github.com/faabiosr/echo-middleware/stargazers) - Middleware for Echo framework with logging and metrics.
- [formjson](https://github.com/rs/formjson) [![GitHub stars](https://img.shields.io/github/stars/rs/formjson?style=flat)](https://github.com/rs/formjson/stargazers) - Transparently handle JSON input as a standard form POST.
- [go-fault](https://github.com/github/go-fault) [![GitHub stars](https://img.shields.io/github/stars/github/go-fault?style=flat)](https://github.com/github/go-fault/stargazers) - Fault injection middleware for Go.
- [Limiter](https://github.com/ulule/limiter) [![GitHub stars](https://img.shields.io/github/stars/ulule/limiter?style=flat)](https://github.com/ulule/limiter/stargazers) - Dead simple rate limit middleware for Go.
- [ln-paywall](https://github.com/philippgille/ln-paywall) [![GitHub stars](https://img.shields.io/github/stars/philippgille/ln-paywall?style=flat)](https://github.com/philippgille/ln-paywall/stargazers) - Go middleware for monetizing APIs on a per-request basis with the Lightning Network (Bitcoin).
- [mid](https://github.com/bobg/mid) [![GitHub stars](https://img.shields.io/github/stars/bobg/mid?style=flat)](https://github.com/bobg/mid/stargazers) - Miscellaneous HTTP middleware features: idiomatic error return from handlers; receive/respond with JSON data; request tracing; and more.
- [rk-gin](https://github.com/rookie-ninja/rk-gin) [![GitHub stars](https://img.shields.io/github/stars/rookie-ninja/rk-gin?style=flat)](https://github.com/rookie-ninja/rk-gin/stargazers) - Middleware for Gin framework with logging, metrics, auth, tracing etc.
- [rk-grpc](https://github.com/rookie-ninja/rk-grpc) [![GitHub stars](https://img.shields.io/github/stars/rookie-ninja/rk-grpc?style=flat)](https://github.com/rookie-ninja/rk-grpc/stargazers) - Middleware for gRPC with logging, metrics, auth, tracing etc.
- [Tollbooth](https://github.com/didip/tollbooth) [![GitHub stars](https://img.shields.io/github/stars/didip/tollbooth?style=flat)](https://github.com/didip/tollbooth/stargazers) - Rate limit HTTP request handler.
- [XFF](https://github.com/sebest/xff) [![GitHub stars](https://img.shields.io/github/stars/sebest/xff?style=flat)](https://github.com/sebest/xff/stargazers) - Handle `X-Forwarded-For` header and friends.

#### Libraries for creating HTTP middlewares

- [alice](https://github.com/justinas/alice) [![GitHub stars](https://img.shields.io/github/stars/justinas/alice?style=flat)](https://github.com/justinas/alice/stargazers) - Painless middleware chaining for Go.
- [catena](https://github.com/codemodus/catena) [![GitHub stars](https://img.shields.io/github/stars/codemodus/catena?style=flat)](https://github.com/codemodus/catena/stargazers) - http.Handler wrapper catenation (same API as "chain").
- [chain](https://github.com/codemodus/chain) [![GitHub stars](https://img.shields.io/github/stars/codemodus/chain?style=flat)](https://github.com/codemodus/chain/stargazers) - Handler wrapper chaining with scoped data (net/context-based "middleware").
- [gores](https://github.com/alioygur/gores) [![GitHub stars](https://img.shields.io/github/stars/alioygur/gores?style=flat)](https://github.com/alioygur/gores/stargazers) - Go package that handles HTML, JSON, XML and etc. responses. Useful for RESTful APIs.
- [interpose](https://github.com/carbocation/interpose) [![GitHub stars](https://img.shields.io/github/stars/carbocation/interpose?style=flat)](https://github.com/carbocation/interpose/stargazers) - Minimalist net/http middleware for golang.
- [mediary](https://github.com/HereMobilityDevelopers/mediary) [![GitHub stars](https://img.shields.io/github/stars/HereMobilityDevelopers/mediary?style=flat)](https://github.com/HereMobilityDevelopers/mediary/stargazers) - add interceptors to `http.Client` to allow dumping/shaping/tracing/... of requests/responses.
- [muxchain](https://github.com/stephens2424/muxchain) [![GitHub stars](https://img.shields.io/github/stars/stephens2424/muxchain?style=flat)](https://github.com/stephens2424/muxchain/stargazers) - Lightweight middleware for net/http.
- [negroni](https://github.com/urfave/negroni) [![GitHub stars](https://img.shields.io/github/stars/urfave/negroni?style=flat)](https://github.com/urfave/negroni/stargazers) - Idiomatic HTTP middleware for Golang.
- [render](https://github.com/unrolled/render) [![GitHub stars](https://img.shields.io/github/stars/unrolled/render?style=flat)](https://github.com/unrolled/render/stargazers) - Go package for easily rendering JSON, XML, and HTML template responses.
- [renderer](https://github.com/thedevsaddam/renderer) [![GitHub stars](https://img.shields.io/github/stars/thedevsaddam/renderer?style=flat)](https://github.com/thedevsaddam/renderer/stargazers) - Simple, lightweight and faster response (JSON, JSONP, XML, YAML, HTML, File) rendering package for Go.
- [stats](https://github.com/thoas/stats) [![GitHub stars](https://img.shields.io/github/stars/thoas/stats?style=flat)](https://github.com/thoas/stats/stargazers) - Go middleware that stores various information about your web application.

**[⬆ back to top](#contents)**

### Routers

- [alien](https://github.com/gernest/alien) [![GitHub stars](https://img.shields.io/github/stars/gernest/alien?style=flat)](https://github.com/gernest/alien/stargazers) - Lightweight and fast http router from outer space.
- [bellt](https://github.com/GuilhermeCaruso/bellt) [![GitHub stars](https://img.shields.io/github/stars/GuilhermeCaruso/bellt?style=flat)](https://github.com/GuilhermeCaruso/bellt/stargazers) - A simple Go HTTP router.
- [Bone](https://github.com/go-zoo/bone) [![GitHub stars](https://img.shields.io/github/stars/go-zoo/bone?style=flat)](https://github.com/go-zoo/bone/stargazers) - Lightning Fast HTTP Multiplexer.
- [Bxog](https://github.com/claygod/Bxog) [![GitHub stars](https://img.shields.io/github/stars/claygod/Bxog?style=flat)](https://github.com/claygod/Bxog/stargazers) - Simple and fast HTTP router for Go. It works with routes of varying difficulty, length and nesting. And he knows how to create a URL from the received parameters.
- [chi](https://github.com/go-chi/chi) [![GitHub stars](https://img.shields.io/github/stars/go-chi/chi?style=flat)](https://github.com/go-chi/chi/stargazers) - Small, fast and expressive HTTP router built on net/context.
- [fasthttprouter](https://github.com/buaazp/fasthttprouter) [![GitHub stars](https://img.shields.io/github/stars/buaazp/fasthttprouter?style=flat)](https://github.com/buaazp/fasthttprouter/stargazers) - High performance router forked from `httprouter`. The first router fit for `fasthttp`.
- [FastRouter](https://github.com/razonyang/fastrouter) [![GitHub stars](https://img.shields.io/github/stars/razonyang/fastrouter?style=flat)](https://github.com/razonyang/fastrouter/stargazers) - a fast, flexible HTTP router written in Go.
- [Fox](https://github.com/fox-toolkit/fox) [![GitHub stars](https://img.shields.io/github/stars/fox-toolkit/fox?style=flat)](https://github.com/fox-toolkit/fox/stargazers) - A high-performance HTTP router for building reverse proxies and API gateways, with first-class support for mutating routes at runtime.
- [fursy](https://github.com/coregx/fursy) [![GitHub stars](https://img.shields.io/github/stars/coregx/fursy?style=flat)](https://github.com/coregx/fursy/stargazers) - HTTP router with type-safe generic handlers, automatic OpenAPI 3.1 generation from code, and RFC 9457 error responses.
- [goblin](https://github.com/bmf-san/goblin) [![GitHub stars](https://img.shields.io/github/stars/bmf-san/goblin?style=flat)](https://github.com/bmf-san/goblin/stargazers) - A golang http router based on trie tree.
- [gocraft/web](https://github.com/gocraft/web) [![GitHub stars](https://img.shields.io/github/stars/gocraft/web?style=flat)](https://github.com/gocraft/web/stargazers) - Mux and middleware package in Go.
- [Goji](https://github.com/goji/goji) [![GitHub stars](https://img.shields.io/github/stars/goji/goji?style=flat)](https://github.com/goji/goji/stargazers) - Goji is a minimalistic and flexible HTTP request multiplexer with support for `net/context`.
- [GoLobby/Router](https://github.com/golobby/router) [![GitHub stars](https://img.shields.io/github/stars/golobby/router?style=flat)](https://github.com/golobby/router/stargazers) - GoLobby Router is a lightweight yet powerful HTTP router for the Go programming language.
- [goroute](https://github.com/goroute/route) [![GitHub stars](https://img.shields.io/github/stars/goroute/route?style=flat)](https://github.com/goroute/route/stargazers) - Simple yet powerful HTTP request multiplexer.
- [GoRouter](https://github.com/vardius/gorouter) [![GitHub stars](https://img.shields.io/github/stars/vardius/gorouter?style=flat)](https://github.com/vardius/gorouter/stargazers) - GoRouter is a Server/API micro framework, HTTP request router, multiplexer, mux that provides request router with middleware supporting `net/context`.
- [gowww/router](https://github.com/gowww/router) [![GitHub stars](https://img.shields.io/github/stars/gowww/router?style=flat)](https://github.com/gowww/router/stargazers) - Lightning fast HTTP router fully compatible with the net/http.Handler interface.
- [httprouter](https://github.com/julienschmidt/httprouter) [![GitHub stars](https://img.shields.io/github/stars/julienschmidt/httprouter?style=flat)](https://github.com/julienschmidt/httprouter/stargazers) - High performance router. Use this and the standard http handlers to form a very high performance web framework.
- [httptreemux](https://github.com/dimfeld/httptreemux) [![GitHub stars](https://img.shields.io/github/stars/dimfeld/httptreemux?style=flat)](https://github.com/dimfeld/httptreemux/stargazers) - High-speed, flexible tree-based HTTP router for Go. Inspiration from httprouter.
- [lars](https://github.com/go-playground/lars) [![GitHub stars](https://img.shields.io/github/stars/go-playground/lars?style=flat)](https://github.com/go-playground/lars/stargazers) - Is a lightweight, fast and extensible zero allocation HTTP router for Go used to create customizable frameworks.
- [mux](https://github.com/gorilla/mux) [![GitHub stars](https://img.shields.io/github/stars/gorilla/mux?style=flat)](https://github.com/gorilla/mux/stargazers) - Powerful URL router and dispatcher for golang.
- [nchi](https://github.com/muir/nchi) [![GitHub stars](https://img.shields.io/github/stars/muir/nchi?style=flat)](https://github.com/muir/nchi/stargazers) - chi-like router built on httprouter with dependency injection based middleware wrappers
- [ngamux](https://github.com/ngamux/ngamux) [![GitHub stars](https://img.shields.io/github/stars/ngamux/ngamux?style=flat)](https://github.com/ngamux/ngamux/stargazers) - Simple HTTP router for Go.
- [ozzo-routing](https://github.com/go-ozzo/ozzo-routing) [![GitHub stars](https://img.shields.io/github/stars/go-ozzo/ozzo-routing?style=flat)](https://github.com/go-ozzo/ozzo-routing/stargazers) - An extremely fast Go (golang) HTTP router that supports regular expression route matching. Comes with full support for building RESTful APIs.
- [pure](https://github.com/go-playground/pure) [![GitHub stars](https://img.shields.io/github/stars/go-playground/pure?style=flat)](https://github.com/go-playground/pure/stargazers) - Is a lightweight HTTP router that sticks to the std "net/http" implementation.
- [Siesta](https://github.com/VividCortex/siesta) [![GitHub stars](https://img.shields.io/github/stars/VividCortex/siesta?style=flat)](https://github.com/VividCortex/siesta/stargazers) - Composable framework to write middleware and handlers.
- [vestigo](https://github.com/husobee/vestigo) [![GitHub stars](https://img.shields.io/github/stars/husobee/vestigo?style=flat)](https://github.com/husobee/vestigo/stargazers) - Performant, stand-alone, HTTP compliant URL Router for go web applications.
- [violetear](https://github.com/nbari/violetear) [![GitHub stars](https://img.shields.io/github/stars/nbari/violetear?style=flat)](https://github.com/nbari/violetear/stargazers) - Go HTTP router.
- [xmux](https://github.com/rs/xmux) [![GitHub stars](https://img.shields.io/github/stars/rs/xmux?style=flat)](https://github.com/rs/xmux/stargazers) - High performance muxer based on `httprouter` with `net/context` support.
- [xujiajun/gorouter](https://github.com/xujiajun/gorouter) [![GitHub stars](https://img.shields.io/github/stars/xujiajun/gorouter?style=flat)](https://github.com/xujiajun/gorouter/stargazers) - A simple and fast HTTP router for Go.

**[⬆ back to top](#contents)**

## WebAssembly

- [dom](https://github.com/dennwc/dom) [![GitHub stars](https://img.shields.io/github/stars/dennwc/dom?style=flat)](https://github.com/dennwc/dom/stargazers) - DOM library.
- [Extism Go SDK](https://github.com/extism/go-sdk) [![GitHub stars](https://img.shields.io/github/stars/extism/go-sdk?style=flat)](https://github.com/extism/go-sdk/stargazers) - Universal, cross-language WebAssembly framework for building plug-in systems and polyglot apps.
- [go-canvas](https://github.com/markfarnan/go-canvas) [![GitHub stars](https://img.shields.io/github/stars/markfarnan/go-canvas?style=flat)](https://github.com/markfarnan/go-canvas/stargazers) - Library to use HTML5 Canvas, with all drawing within go code.
- [tinygo](https://github.com/tinygo-org/tinygo) [![GitHub stars](https://img.shields.io/github/stars/tinygo-org/tinygo?style=flat)](https://github.com/tinygo-org/tinygo/stargazers) - Go compiler for small places. Microcontrollers, WebAssembly, and command-line tools. Based on LLVM.
- [vert](https://github.com/norunners/vert) [![GitHub stars](https://img.shields.io/github/stars/norunners/vert?style=flat)](https://github.com/norunners/vert/stargazers) - Interop between Go and JS values.
- [wasmbrowsertest](https://github.com/agnivade/wasmbrowsertest) [![GitHub stars](https://img.shields.io/github/stars/agnivade/wasmbrowsertest?style=flat)](https://github.com/agnivade/wasmbrowsertest/stargazers) - Run Go WASM tests in your browser.
- [webapi](https://github.com/gowebapi/webapi) [![GitHub stars](https://img.shields.io/github/stars/gowebapi/webapi?style=flat)](https://github.com/gowebapi/webapi/stargazers) - Bindings for DOM and HTML generated from WebIDL.

**[⬆ back to top](#contents)**

## Webhooks Server

- [HookRun](https://github.com/bluvenr/hookrun) [![GitHub stars](https://img.shields.io/github/stars/bluvenr/hookrun?style=flat)](https://github.com/bluvenr/hookrun/stargazers) - Lightweight webhook action engine (~3MB single binary, zero deps) that executes commands and scripts from YAML rules with token/HMAC/IP auth and hot reload.
- [webhook](https://github.com/adnanh/webhook) [![GitHub stars](https://img.shields.io/github/stars/adnanh/webhook?style=flat)](https://github.com/adnanh/webhook/stargazers) - Tool which allows user to create HTTP endpoints (hooks) that execute commands on the server.
- [webhooked](https://github.com/42Atomys/webhooked) [![GitHub stars](https://img.shields.io/github/stars/42Atomys/webhooked?style=flat)](https://github.com/42Atomys/webhooked/stargazers) - A webhook receiver on steroids: handle, secure, format and store a Webhook payload has never been easier.
- [WebhookX](https://github.com/webhookx-io/webhookx) [![GitHub stars](https://img.shields.io/github/stars/webhookx-io/webhookx?style=flat)](https://github.com/webhookx-io/webhookx/stargazers) - A webhooks gateway for message receiving, processing, and reliable delivering.

**[⬆ back to top](#contents)**

## Windows

- [d3d9](https://github.com/gonutz/d3d9) [![GitHub stars](https://img.shields.io/github/stars/gonutz/d3d9?style=flat)](https://github.com/gonutz/d3d9/stargazers) - Go bindings for Direct3D9.
- [go-ole](https://github.com/go-ole/go-ole) [![GitHub stars](https://img.shields.io/github/stars/go-ole/go-ole?style=flat)](https://github.com/go-ole/go-ole/stargazers) - Win32 OLE implementation for golang.
- [gosddl](https://github.com/MonaxGT/gosddl) [![GitHub stars](https://img.shields.io/github/stars/MonaxGT/gosddl?style=flat)](https://github.com/MonaxGT/gosddl/stargazers) - Converter from SDDL-string to user-friendly JSON. SDDL consist of four part: Owner, Primary Group, DACL, SACL.
- [windowsupdate](https://github.com/ceshihao/windowsupdate) [![GitHub stars](https://img.shields.io/github/stars/ceshihao/windowsupdate?style=flat)](https://github.com/ceshihao/windowsupdate/stargazers) - A Golang binding for Windows Update Agent API using go-ole.

**[⬆ back to top](#contents)**

## Workflow Frameworks

_Libraries for creating Workflows._

- [Cadence-client](https://github.com/uber-go/cadence-client) [![GitHub stars](https://img.shields.io/github/stars/uber-go/cadence-client?style=flat)](https://github.com/uber-go/cadence-client/stargazers) - A framework for authoring workflows and activities running on top of the Cadence orchestration engine made by Uber.
- [Dagu](https://github.com/dagu-go/dagu) [![GitHub stars](https://img.shields.io/github/stars/dagu-go/dagu?style=flat)](https://github.com/dagu-go/dagu/stargazers) - No-code workflow executor. it executes DAGs defined in a simple YAML format.
- [Flowbaker](https://github.com/flowbaker/flowbaker) [![GitHub stars](https://img.shields.io/github/stars/flowbaker/flowbaker?style=flat)](https://github.com/flowbaker/flowbaker/stargazers) - Self-hosted execution engine for building, connecting, and automating no-code workflows.
- [go-dag](https://github.com/rhosocial/go-dag) [![GitHub stars](https://img.shields.io/github/stars/rhosocial/go-dag?style=flat)](https://github.com/rhosocial/go-dag/stargazers) - A framework developed in Go that manages the execution of workflows described by directed acyclic graphs.
- [go-taskflow](https://github.com/noneback/go-taskflow) [![GitHub stars](https://img.shields.io/github/stars/noneback/go-taskflow?style=flat)](https://github.com/noneback/go-taskflow/stargazers) - A taskflow-like General-purpose Task-parallel Programming Framework with integrated visualizer and profiler.
- [workflow](https://github.com/luno/workflow) [![GitHub stars](https://img.shields.io/github/stars/luno/workflow?style=flat)](https://github.com/luno/workflow/stargazers) - A tech stack agnostic Event Driven Workflow framework.

**[⬆ back to top](#contents)**

## XML

_Libraries and tools for manipulating XML._

- [XML-Comp](https://github.com/xml-comp/xml-comp) [![GitHub stars](https://img.shields.io/github/stars/xml-comp/xml-comp?style=flat)](https://github.com/xml-comp/xml-comp/stargazers) - Simple command line XML comparer that generates diffs of folders, files and tags.
- [xml2map](https://github.com/sbabiv/xml2map) [![GitHub stars](https://img.shields.io/github/stars/sbabiv/xml2map?style=flat)](https://github.com/sbabiv/xml2map/stargazers) - XML to MAP converter written Golang.
- [xmlquery](https://github.com/antchfx/xmlquery) [![GitHub stars](https://img.shields.io/github/stars/antchfx/xmlquery?style=flat)](https://github.com/antchfx/xmlquery/stargazers) - xmlquery is Golang XPath package for XML query.
- [xmlwriter](https://github.com/shabbyrobe/xmlwriter) [![GitHub stars](https://img.shields.io/github/stars/shabbyrobe/xmlwriter?style=flat)](https://github.com/shabbyrobe/xmlwriter/stargazers) - Procedural XML generation API based on libxml2's xmlwriter module.
- [xpath](https://github.com/antchfx/xpath) [![GitHub stars](https://img.shields.io/github/stars/antchfx/xpath?style=flat)](https://github.com/antchfx/xpath/stargazers) - XPath package for Go.
- [zek](https://github.com/miku/zek) [![GitHub stars](https://img.shields.io/github/stars/miku/zek?style=flat)](https://github.com/miku/zek/stargazers) - Generate a Go struct from XML.

## Zero Trust

_Libraries and tools to implement Zero Trust architectures._

- [Cosign](https://github.com/sigstore/cosign) [![GitHub stars](https://img.shields.io/github/stars/sigstore/cosign?style=flat)](https://github.com/sigstore/cosign/stargazers) - Container Signing, Verification and Storage in an OCI registry.
- [in-toto](https://github.com/in-toto/in-toto-golang) [![GitHub stars](https://img.shields.io/github/stars/in-toto/in-toto-golang?style=flat)](https://github.com/in-toto/in-toto-golang/stargazers) - Go implementation of the in-toto (provides a framework to protect the integrity of the software supply chain) python reference implementation.
- [OpenZiti](https://github.com/openziti/ziti) [![GitHub stars](https://img.shields.io/github/stars/openziti/ziti?style=flat)](https://github.com/openziti/ziti/stargazers) - A full, open source zero trust overlay network. Including numerous SDKs for numerous languages such as [golang](https://github.com/openziti/sdk-golang) [![GitHub stars](https://img.shields.io/github/stars/openziti/sdk-golang?style=flat)](https://github.com/openziti/sdk-golang/stargazers) allowing you to embed zero trust principles directly into your applications. The [OpenZiti Test Kitchen](https://github.com/openziti-test-kitchen) [![GitHub stars](https://img.shields.io/github/stars/openziti-test-kitchen?style=flat)](https://github.com/openziti-test-kitchen/stargazers) has numerous examples to draw inspiration from including a [zero trust ssh client - zssh](https://github.com/openziti-test-kitchen/zssh) [![GitHub stars](https://img.shields.io/github/stars/openziti-test-kitchen/zssh?style=flat)](https://github.com/openziti-test-kitchen/zssh/stargazers)
- [Spiffe-Vault](https://github.com/philips-labs/spiffe-vault) [![GitHub stars](https://img.shields.io/github/stars/philips-labs/spiffe-vault?style=flat)](https://github.com/philips-labs/spiffe-vault/stargazers) - Utilizes Spiffe JWT authentication with Hashicorp Vault for secretless authentication.
- [Spire](https://github.com/spiffe/spire) [![GitHub stars](https://img.shields.io/github/stars/spiffe/spire?style=flat)](https://github.com/spiffe/spire/stargazers) - SPIRE (the SPIFFE Runtime Environment) is a toolchain of APIs for establishing trust between software systems across a wide variety of hosting platforms.

## Code Analysis

_Source code analysis tools, also known as Static Application Security Testing (SAST) Tools._

- [apicompat](https://github.com/bradleyfalzon/apicompat) [![GitHub stars](https://img.shields.io/github/stars/bradleyfalzon/apicompat?style=flat)](https://github.com/bradleyfalzon/apicompat/stargazers) - Checks recent changes to a Go project for backwards incompatible changes.
- [asty](https://github.com/asty-org/asty) [![GitHub stars](https://img.shields.io/github/stars/asty-org/asty?style=flat)](https://github.com/asty-org/asty/stargazers) - Converts golang AST to JSON and JSON to AST.
- [blanket](https://gitlab.com/verygoodsoftwarenotvirus/blanket) - blanket is a tool that helps you catch functions which don't have direct unit tests in your Go packages.
- [ChainJacking](https://github.com/Checkmarx/chainjacking) [![GitHub stars](https://img.shields.io/github/stars/Checkmarx/chainjacking?style=flat)](https://github.com/Checkmarx/chainjacking/stargazers) - Find which of your Go lang direct GitHub dependencies is susceptible to ChainJacking attack.
- [Chronos](https://github.com/amit-davidson/Chronos) [![GitHub stars](https://img.shields.io/github/stars/amit-davidson/Chronos?style=flat)](https://github.com/amit-davidson/Chronos/stargazers) - Detects race conditions statically
- [dupl](https://github.com/mibk/dupl) [![GitHub stars](https://img.shields.io/github/stars/mibk/dupl?style=flat)](https://github.com/mibk/dupl/stargazers) - Tool for code clone detection.
- [errcheck](https://github.com/kisielk/errcheck) [![GitHub stars](https://img.shields.io/github/stars/kisielk/errcheck?style=flat)](https://github.com/kisielk/errcheck/stargazers) - Errcheck is a program for checking for unchecked errors in Go programs.
- [fatcontext](https://github.com/Crocmagnon/fatcontext) [![GitHub stars](https://img.shields.io/github/stars/Crocmagnon/fatcontext?style=flat)](https://github.com/Crocmagnon/fatcontext/stargazers) - Fatcontext detects nested contexts in loops or function literals.
- [go-checkstyle](https://github.com/qiniu/checkstyle) [![GitHub stars](https://img.shields.io/github/stars/qiniu/checkstyle?style=flat)](https://github.com/qiniu/checkstyle/stargazers) - checkstyle is a style check tool like java checkstyle. This tool inspired by java checkstyle, golint. The style referred to some points in Go Code Review Comments.
- [go-cleanarch](https://github.com/roblaszczak/go-cleanarch) [![GitHub stars](https://img.shields.io/github/stars/roblaszczak/go-cleanarch?style=flat)](https://github.com/roblaszczak/go-cleanarch/stargazers) - go-cleanarch was created to validate Clean Architecture rules, like a The Dependency Rule and interaction between packages in your Go projects.
- [go-critic](https://github.com/go-critic/go-critic) [![GitHub stars](https://img.shields.io/github/stars/go-critic/go-critic?style=flat)](https://github.com/go-critic/go-critic/stargazers) - source code linter that brings checks that are currently not implemented in other linters.
- [go-mod-outdated](https://github.com/psampaz/go-mod-outdated) [![GitHub stars](https://img.shields.io/github/stars/psampaz/go-mod-outdated?style=flat)](https://github.com/psampaz/go-mod-outdated/stargazers) - An easy way to find outdated dependencies of your Go projects.
- [goast-viewer](https://github.com/yuroyoro/goast-viewer) [![GitHub stars](https://img.shields.io/github/stars/yuroyoro/goast-viewer?style=flat)](https://github.com/yuroyoro/goast-viewer/stargazers) - Web based Golang AST visualizer.
- [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) - Tool to fix (add, remove) your Go imports automatically.
- [golang-ifood-sdk](https://github.com/arxdsilva/golang-ifood-sdk) [![GitHub stars](https://img.shields.io/github/stars/arxdsilva/golang-ifood-sdk?style=flat)](https://github.com/arxdsilva/golang-ifood-sdk/stargazers) - iFood API SDK.
- [golangci-lint](https://github.com/golangci/golangci-lint) [![GitHub stars](https://img.shields.io/github/stars/golangci/golangci-lint?style=flat)](https://github.com/golangci/golangci-lint/stargazers) – A fast Go linters runner. It runs linters in parallel, uses caching, supports `yaml` config, has integrations with all major IDE and has dozens of linters included.
- [golines](https://github.com/segmentio/golines) [![GitHub stars](https://img.shields.io/github/stars/segmentio/golines?style=flat)](https://github.com/segmentio/golines/stargazers) - Formatter that automatically shortens long lines in Go code.
- [gomarklint](https://github.com/shinagawa-web/gomarklint) [![GitHub stars](https://img.shields.io/github/stars/shinagawa-web/gomarklint?style=flat)](https://github.com/shinagawa-web/gomarklint/stargazers) - Markdown linter with built-in HTTP link validation, single binary, no Node.js required.
- [GoPlantUML](https://github.com/jfeliu007/goplantuml) [![GitHub stars](https://img.shields.io/github/stars/jfeliu007/goplantuml?style=flat)](https://github.com/jfeliu007/goplantuml/stargazers) - Library and CLI that generates text plantump class diagram containing information about structures and interfaces with the relationship among them.
- [goreturns](https://github.com/sqs/goreturns) [![GitHub stars](https://img.shields.io/github/stars/sqs/goreturns?style=flat)](https://github.com/sqs/goreturns/stargazers) - Adds zero-value return statements to match the func return types.
- [gostatus](https://github.com/shurcooL/gostatus) [![GitHub stars](https://img.shields.io/github/stars/shurcooL/gostatus?style=flat)](https://github.com/shurcooL/gostatus/stargazers) - Command line tool, shows the status of repositories that contain Go packages.
- [lint](https://github.com/surullabs/lint) [![GitHub stars](https://img.shields.io/github/stars/surullabs/lint?style=flat)](https://github.com/surullabs/lint/stargazers) - Run linters as part of go test.
- [php-parser](https://github.com/z7zmey/php-parser) [![GitHub stars](https://img.shields.io/github/stars/z7zmey/php-parser?style=flat)](https://github.com/z7zmey/php-parser/stargazers) - A Parser for PHP written in Go.
- [revive](https://github.com/mgechev/revive) [![GitHub stars](https://img.shields.io/github/stars/mgechev/revive?style=flat)](https://github.com/mgechev/revive/stargazers) – ~6x faster, stricter, configurable, extensible, and beautiful drop-in replacement for `golint`.
- [staticcheck](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck) [![GitHub stars](https://img.shields.io/github/stars/dominikh/go-tools/tree/master/cmd/staticcheck?style=flat)](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck/stargazers) - staticcheck is `go vet` on steroids, applying a ton of static analysis checks you might be used to from tools like ReSharper for C#.
- [structalign](https://github.com/peczenyj/structalign) [![GitHub stars](https://img.shields.io/github/stars/peczenyj/structalign?style=flat)](https://github.com/peczenyj/structalign/stargazers) - Shows how a struct's fields could be reordered to use less memory, printing a diff instead of rewriting files.
- [stto](https://github.com/mainak55512/stto) [![GitHub stars](https://img.shields.io/github/stars/mainak55512/stto?style=flat)](https://github.com/mainak55512/stto/stargazers) - A light-weight superfast line of code counter written in pure Go.
- [testifylint](https://github.com/Antonboom/testifylint) [![GitHub stars](https://img.shields.io/github/stars/Antonboom/testifylint?style=flat)](https://github.com/Antonboom/testifylint/stargazers) – A linter that checks usage of [github.com/stretchr/testify](https://github.com/stretchr/testify) [![GitHub stars](https://img.shields.io/github/stars/stretchr/testify?style=flat)](https://github.com/stretchr/testify/stargazers).
- [tickgit](https://github.com/augmentable-dev/tickgit) [![GitHub stars](https://img.shields.io/github/stars/augmentable-dev/tickgit?style=flat)](https://github.com/augmentable-dev/tickgit/stargazers) - CLI and go package for surfacing code comment TODOs (in any language) and applying a `git blame`to identify the author.
- [todocheck](https://github.com/preslavmihaylov/todocheck) [![GitHub stars](https://img.shields.io/github/stars/preslavmihaylov/todocheck?style=flat)](https://github.com/preslavmihaylov/todocheck/stargazers) - Static code analyser which links TODO comments in code with issues in your issue tracker.
- [unconvert](https://github.com/mdempsky/unconvert) [![GitHub stars](https://img.shields.io/github/stars/mdempsky/unconvert?style=flat)](https://github.com/mdempsky/unconvert/stargazers) - Remove unnecessary type conversions from Go source.
- [usestdlibvars](https://github.com/sashamelentyev/usestdlibvars) [![GitHub stars](https://img.shields.io/github/stars/sashamelentyev/usestdlibvars?style=flat)](https://github.com/sashamelentyev/usestdlibvars/stargazers) - A linter that detect the possibility to use variables/constants from the Go standard library.
- [vacuum](https://github.com/daveshanley/vacuum) [![GitHub stars](https://img.shields.io/github/stars/daveshanley/vacuum?style=flat)](https://github.com/daveshanley/vacuum/stargazers) - An ultra-super-fast, lightweight OpenAPI linter and quality checking tool.
- [validate](https://github.com/mccoyst/validate) [![GitHub stars](https://img.shields.io/github/stars/mccoyst/validate?style=flat)](https://github.com/mccoyst/validate/stargazers) - Automatically validates struct fields with tags.
- [wrapcheck](https://github.com/tomarrell/wrapcheck) [![GitHub stars](https://img.shields.io/github/stars/tomarrell/wrapcheck?style=flat)](https://github.com/tomarrell/wrapcheck/stargazers) - A linter to check that errors from external packages are wrapped.

**[⬆ back to top](#contents)**

## Editor Plugins

_Plugin for text editors and IDEs._

- [coc-go language server extension for Vim/Neovim](https://github.com/josa42/coc-go) [![GitHub stars](https://img.shields.io/github/stars/josa42/coc-go?style=flat)](https://github.com/josa42/coc-go/stargazers) - This plugin adds [gopls](https://github.com/golang/tools/blob/master/gopls/README.md) [![GitHub stars](https://img.shields.io/github/stars/golang/tools/blob/master/gopls/README.md?style=flat)](https://github.com/golang/tools/blob/master/gopls/README.md/stargazers) features to Vim/Neovim.
- [Go Doc](https://github.com/msyrus/vscode-go-doc) [![GitHub stars](https://img.shields.io/github/stars/msyrus/vscode-go-doc?style=flat)](https://github.com/msyrus/vscode-go-doc/stargazers) - A Visual Studio Code extension for showing definition in output and generating go doc.
- [Go plugin for JetBrains IDEs](https://plugins.jetbrains.com/plugin/9568-go) - Go plugin for JetBrains IDEs.
- [go-mode](https://github.com/dominikh/go-mode.el) [![GitHub stars](https://img.shields.io/github/stars/dominikh/go-mode.el?style=flat)](https://github.com/dominikh/go-mode.el/stargazers) - Go mode for GNU/Emacs.
- [gocode](https://github.com/nsf/gocode) [![GitHub stars](https://img.shields.io/github/stars/nsf/gocode?style=flat)](https://github.com/nsf/gocode/stargazers) - Autocompletion daemon for the Go programming language.
- [goimports-reviser](https://github.com/incu6us/goimports-reviser) [![GitHub stars](https://img.shields.io/github/stars/incu6us/goimports-reviser?style=flat)](https://github.com/incu6us/goimports-reviser/stargazers) - Formatting tool for imports.
- [goprofiling](https://marketplace.visualstudio.com/items?itemName=MaxMedia.go-prof) - This extension adds benchmark profiling support for the Go language to VS Code.
- [GoSublime](https://github.com/DisposaBoy/GoSublime) [![GitHub stars](https://img.shields.io/github/stars/DisposaBoy/GoSublime?style=flat)](https://github.com/DisposaBoy/GoSublime/stargazers) - Golang plugin collection for the text editor SublimeText 3 providing code completion and other IDE-like features.
- [gounit-vim](https://github.com/hexdigest/gounit-vim) [![GitHub stars](https://img.shields.io/github/stars/hexdigest/gounit-vim?style=flat)](https://github.com/hexdigest/gounit-vim/stargazers) - Vim plugin for generating Go tests based on the function's or method's signature.
- [vim-compiler-go](https://github.com/rjohnsondev/vim-compiler-go) [![GitHub stars](https://img.shields.io/github/stars/rjohnsondev/vim-compiler-go?style=flat)](https://github.com/rjohnsondev/vim-compiler-go/stargazers) - Vim plugin to highlight syntax errors on save.
- [vim-go](https://github.com/fatih/vim-go) [![GitHub stars](https://img.shields.io/github/stars/fatih/vim-go?style=flat)](https://github.com/fatih/vim-go/stargazers) - Go development plugin for Vim.
- [vscode-go](https://github.com/golang/vscode-go) [![GitHub stars](https://img.shields.io/github/stars/golang/vscode-go?style=flat)](https://github.com/golang/vscode-go/stargazers) - Extension for Visual Studio Code (VS Code) which provides support for the Go language.
- [Watch](https://github.com/eaburns/Watch) [![GitHub stars](https://img.shields.io/github/stars/eaburns/Watch?style=flat)](https://github.com/eaburns/Watch/stargazers) - Runs a command in an acme win on file changes.

**[⬆ back to top](#contents)**

## Go Generate Tools

- [envdoc](https://github.com/g4s8/envdoc) [![GitHub stars](https://img.shields.io/github/stars/g4s8/envdoc?style=flat)](https://github.com/g4s8/envdoc/stargazers) - generate documentation for environment variables from Go source files.
- [generic](https://github.com/usk81/generic) [![GitHub stars](https://img.shields.io/github/stars/usk81/generic?style=flat)](https://github.com/usk81/generic/stargazers) - flexible data type for Go.
- [gocontracts](https://github.com/Parquery/gocontracts) [![GitHub stars](https://img.shields.io/github/stars/Parquery/gocontracts?style=flat)](https://github.com/Parquery/gocontracts/stargazers) - brings design-by-contract to Go by synchronizing the code with the documentation.
- [godal](https://github.com/mafulong/godal) [![GitHub stars](https://img.shields.io/github/stars/mafulong/godal?style=flat)](https://github.com/mafulong/godal/stargazers) - Generate orm models corresponding to golang by specifying sql ddl file, which can be used by gorm.
- [gonerics](https://github.com/bouk/gonerics) [![GitHub stars](https://img.shields.io/github/stars/bouk/gonerics?style=flat)](https://github.com/bouk/gonerics/stargazers) - Idiomatic Generics in Go.
- [gotests](https://github.com/cweill/gotests) [![GitHub stars](https://img.shields.io/github/stars/cweill/gotests?style=flat)](https://github.com/cweill/gotests/stargazers) - Generate Go tests from your source code.
- [gounit](https://github.com/hexdigest/gounit) [![GitHub stars](https://img.shields.io/github/stars/hexdigest/gounit?style=flat)](https://github.com/hexdigest/gounit/stargazers) - Generate Go tests using your own templates.
- [hasgo](https://github.com/DylanMeeus/hasgo) [![GitHub stars](https://img.shields.io/github/stars/DylanMeeus/hasgo?style=flat)](https://github.com/DylanMeeus/hasgo/stargazers) - Generate Haskell inspired functions for your slices.
- [options-gen](https://github.com/kazhuravlev/options-gen) [![GitHub stars](https://img.shields.io/github/stars/kazhuravlev/options-gen?style=flat)](https://github.com/kazhuravlev/options-gen/stargazers) - Functional options described by Dave Cheney's post "Functional options for friendly APIs".
- [re2dfa](https://gitlab.com/opennota/re2dfa) - Transform regular expressions into finite state machines and output Go source code.
- [sqlgen](https://github.com/anqiansong/sqlgen) [![GitHub stars](https://img.shields.io/github/stars/anqiansong/sqlgen?style=flat)](https://github.com/anqiansong/sqlgen/stargazers) - Generate gorm, xorm, sqlx, bun, sql code from SQL file or DSN.
- [TOML-to-Go](https://xuri.me/toml-to-go) - Translates TOML into a Go type in the browser instantly.
- [xgen](https://github.com/xuri/xgen) [![GitHub stars](https://img.shields.io/github/stars/xuri/xgen?style=flat)](https://github.com/xuri/xgen/stargazers) - XSD (XML Schema Definition) parser and Go/C/Java/Rust/TypeScript code generator.

**[⬆ back to top](#contents)**

## Go Tools

- [decouple](https://github.com/bobg/decouple) [![GitHub stars](https://img.shields.io/github/stars/bobg/decouple?style=flat)](https://github.com/bobg/decouple/stargazers) - Find “overspecified” function parameters that could be generalized with interface types.
- [docs](https://github.com/go-oas/docs) [![GitHub stars](https://img.shields.io/github/stars/go-oas/docs?style=flat)](https://github.com/go-oas/docs/stargazers) - Automatically generate RESTful API documentation for GO projects - aligned with Open API Specification standard.
- [go-callvis](https://github.com/TrueFurby/go-callvis) [![GitHub stars](https://img.shields.io/github/stars/TrueFurby/go-callvis?style=flat)](https://github.com/TrueFurby/go-callvis/stargazers) - Visualize call graph of your Go program using dot format.
- [go-size-analyzer](https://github.com/Zxilly/go-size-analyzer) [![GitHub stars](https://img.shields.io/github/stars/Zxilly/go-size-analyzer?style=flat)](https://github.com/Zxilly/go-size-analyzer/stargazers) - Analyze and visualize the size of dependencies in compiled Golang binaries, providing insight into their impact on the final build.
- [go-swagger](https://github.com/go-swagger/go-swagger) [![GitHub stars](https://img.shields.io/github/stars/go-swagger/go-swagger?style=flat)](https://github.com/go-swagger/go-swagger/stargazers) - Swagger 2.0 implementation for go. Swagger is a simple yet powerful representation of your RESTful API.
- [go-template-playground](https://bartventer.github.io/go-template-playground/) - An interactive environment to create and test Go templates.
- [godbg](https://github.com/tylerwince/godbg) [![GitHub stars](https://img.shields.io/github/stars/tylerwince/godbg?style=flat)](https://github.com/tylerwince/godbg/stargazers) - Implementation of Rusts `dbg!` macro for quick and easy debugging during development.
- [gomodrun](https://github.com/dustinblackman/gomodrun/) [![GitHub stars](https://img.shields.io/github/stars/dustinblackman/gomodrun/?style=flat)](https://github.com/dustinblackman/gomodrun//stargazers) - Go tool that executes and caches binaries included in go.mod files.
- [gotemplate.io](https://gotemplate.io/) - Online tool to preview `text/template` templates live.
- [gotestdox](https://github.com/bitfield/gotestdox) [![GitHub stars](https://img.shields.io/github/stars/bitfield/gotestdox?style=flat)](https://github.com/bitfield/gotestdox/stargazers) - Show Go test results as readable sentences.
- [gothanks](https://github.com/psampaz/gothanks) [![GitHub stars](https://img.shields.io/github/stars/psampaz/gothanks?style=flat)](https://github.com/psampaz/gothanks/stargazers) - GoThanks automatically stars your go.mod github dependencies, sending this way some love to their maintainers.
- [gotutor](https://github.com/ahmedakef/gotutor) [![GitHub stars](https://img.shields.io/github/stars/ahmedakef/gotutor?style=flat)](https://github.com/ahmedakef/gotutor/stargazers) - Online Go Debugger & Visualizer.
- [govisual](https://github.com/doganarif/govisual) [![GitHub stars](https://img.shields.io/github/stars/doganarif/govisual?style=flat)](https://github.com/doganarif/govisual/stargazers) - Zero-config, pure-Go HTTP request visualizer & debugger for local Go web development.
- [igo](https://github.com/rocketlaunchr/igo) [![GitHub stars](https://img.shields.io/github/stars/rocketlaunchr/igo?style=flat)](https://github.com/rocketlaunchr/igo/stargazers) - An igo to go transpiler (new language features for Go language!)
- [lensm](https://github.com/loov/lensm) [![GitHub stars](https://img.shields.io/github/stars/loov/lensm?style=flat)](https://github.com/loov/lensm/stargazers) - Go assembly and source viewer.
- [modver](https://github.com/bobg/modver) [![GitHub stars](https://img.shields.io/github/stars/bobg/modver?style=flat)](https://github.com/bobg/modver/stargazers) - Compare two versions of a Go module to check the version-number change required (major, minor, or patchlevel), according to [semver](https://semver.org/) rules.
- [MoniGO](https://github.com/iyashjayesh/monigo) [![GitHub stars](https://img.shields.io/github/stars/iyashjayesh/monigo?style=flat)](https://github.com/iyashjayesh/monigo/stargazers) - A performance monitoring library for Go applications. It provides real-time insights into application performance! 🚀
- [OctoLinker](https://github.com/OctoLinker/browser-extension) [![GitHub stars](https://img.shields.io/github/stars/OctoLinker/browser-extension?style=flat)](https://github.com/OctoLinker/browser-extension/stargazers) - Navigate through go files efficiently with the OctoLinker browser extension for GitHub.
- [richgo](https://github.com/kyoh86/richgo) [![GitHub stars](https://img.shields.io/github/stars/kyoh86/richgo?style=flat)](https://github.com/kyoh86/richgo/stargazers) - Enrich `go test` outputs with text decorations.
- [roumon](https://github.com/becheran/roumon) [![GitHub stars](https://img.shields.io/github/stars/becheran/roumon?style=flat)](https://github.com/becheran/roumon/stargazers) - Monitor current state of all active goroutines via a command line interface.
- [rts](https://github.com/galeone/rts) [![GitHub stars](https://img.shields.io/github/stars/galeone/rts?style=flat)](https://github.com/galeone/rts/stargazers) - RTS: response to struct. Generates Go structs from server responses.
- [textra](https://github.com/ravsii/textra) [![GitHub stars](https://img.shields.io/github/stars/ravsii/textra?style=flat)](https://github.com/ravsii/textra/stargazers) - Extract Go struct field names, types and tags for filtering and exporting.
- [typex](https://github.com/dtgorski/typex) [![GitHub stars](https://img.shields.io/github/stars/dtgorski/typex?style=flat)](https://github.com/dtgorski/typex/stargazers) - Examine Go types and their transitive dependencies, alternatively export results as TypeScript value objects (or types) declaration.

**[⬆ back to top](#contents)**

## Software Packages

_Software written in Go._

**[⬆ back to top](#contents)**

### DevOps Tools

- [abbreviate](https://github.com/dnnrly/abbreviate) [![GitHub stars](https://img.shields.io/github/stars/dnnrly/abbreviate?style=flat)](https://github.com/dnnrly/abbreviate/stargazers) - abbreviate is a tool turning long strings in to shorter ones with configurable separators, for example to embed branch names in to deployment stack IDs.
- [alaz](https://github.com/ddosify/alaz) [![GitHub stars](https://img.shields.io/github/stars/ddosify/alaz?style=flat)](https://github.com/ddosify/alaz/stargazers) - Effortless, Low-Overhead, eBPF-based Kubernetes Monitoring.
- [aptly](https://github.com/aptly-dev/aptly) [![GitHub stars](https://img.shields.io/github/stars/aptly-dev/aptly?style=flat)](https://github.com/aptly-dev/aptly/stargazers) - aptly is a Debian repository management tool.
- [aurora](https://github.com/xuri/aurora) [![GitHub stars](https://img.shields.io/github/stars/xuri/aurora?style=flat)](https://github.com/xuri/aurora/stargazers) - Cross-platform web-based Beanstalkd queue server console.
- [aws-doctor](https://github.com/elC0mpa/aws-doctor) [![GitHub stars](https://img.shields.io/github/stars/elC0mpa/aws-doctor?style=flat)](https://github.com/elC0mpa/aws-doctor/stargazers) - Diagnose AWS costs, detect idle resources, and optimize cloud spending directly from your terminal 🩺 ☁️.
- [awsenv](https://github.com/soniah/awsenv) [![GitHub stars](https://img.shields.io/github/stars/soniah/awsenv?style=flat)](https://github.com/soniah/awsenv/stargazers) - Small binary that loads Amazon (AWS) environment variables for a profile.
- [Balerter](https://github.com/balerter/balerter) [![GitHub stars](https://img.shields.io/github/stars/balerter/balerter?style=flat)](https://github.com/balerter/balerter/stargazers) - A self-hosted script-based alerting manager.
- [Blast](https://github.com/dave/blast) [![GitHub stars](https://img.shields.io/github/stars/dave/blast?style=flat)](https://github.com/dave/blast/stargazers) - A simple tool for API load testing and batch jobs.
- [bombardier](https://github.com/codesenberg/bombardier) [![GitHub stars](https://img.shields.io/github/stars/codesenberg/bombardier?style=flat)](https://github.com/codesenberg/bombardier/stargazers) - Fast cross-platform HTTP benchmarking tool.
- [cassowary](https://github.com/rogerwelin/cassowary) [![GitHub stars](https://img.shields.io/github/stars/rogerwelin/cassowary?style=flat)](https://github.com/rogerwelin/cassowary/stargazers) - Modern cross-platform HTTP load-testing tool written in Go.
- [chaosmonkey](https://github.com/Netflix/chaosmonkey) [![GitHub stars](https://img.shields.io/github/stars/Netflix/chaosmonkey?style=flat)](https://github.com/Netflix/chaosmonkey/stargazers) - A resiliency tool that helps applications tolerate random instance failures.
- [colima](https://github.com/abiosoft/colima) [![GitHub stars](https://img.shields.io/github/stars/abiosoft/colima?style=flat)](https://github.com/abiosoft/colima/stargazers) - Container runtimes on macOS (and Linux) with minimal setup.
- [Ddosify](https://github.com/ddosify/ddosify) [![GitHub stars](https://img.shields.io/github/stars/ddosify/ddosify?style=flat)](https://github.com/ddosify/ddosify/stargazers) - High-performance load testing tool, written in Golang.
- [decompose](https://github.com/s0rg/decompose) [![GitHub stars](https://img.shields.io/github/stars/s0rg/decompose?style=flat)](https://github.com/s0rg/decompose/stargazers) - tool to generate and process Docker containers connections graphs.
- [Den](https://github.com/us/den) [![GitHub stars](https://img.shields.io/github/stars/us/den?style=flat)](https://github.com/us/den/stargazers) - Self-hosted sandbox runtime for AI agents. Open-source E2B alternative.
- [DepCharge](https://github.com/centerorbit/depcharge) [![GitHub stars](https://img.shields.io/github/stars/centerorbit/depcharge?style=flat)](https://github.com/centerorbit/depcharge/stargazers) - Helps orchestrating the execution of commands across the many dependencies in larger projects.
- [dish](https://github.com/thevxn/dish) [![GitHub stars](https://img.shields.io/github/stars/thevxn/dish?style=flat)](https://github.com/thevxn/dish/stargazers) - A lightweight, remotely configurable monitoring service.
- [Docker](https://www.docker.com/) - Open platform for distributed applications for developers and sysadmins.
- [docker-go-mingw](https://github.com/x1unix/docker-go-mingw) [![GitHub stars](https://img.shields.io/github/stars/x1unix/docker-go-mingw?style=flat)](https://github.com/x1unix/docker-go-mingw/stargazers) - Docker image for building Go binaries for Windows with MinGW toolchain.
- [docker-volume-backup](https://github.com/offen/docker-volume-backup) [![GitHub stars](https://img.shields.io/github/stars/offen/docker-volume-backup?style=flat)](https://github.com/offen/docker-volume-backup/stargazers) - Backup Docker volumes locally or to any S3, WebDAV, Azure Blob Storage, Dropbox or SSH compatible storage.
- [Dockerfile-Generator](https://github.com/ozankasikci/dockerfile-generator) [![GitHub stars](https://img.shields.io/github/stars/ozankasikci/dockerfile-generator?style=flat)](https://github.com/ozankasikci/dockerfile-generator/stargazers) - A go library and an executable that produces valid Dockerfiles using various input channels.
- [dogo](https://github.com/liudng/dogo) [![GitHub stars](https://img.shields.io/github/stars/liudng/dogo?style=flat)](https://github.com/liudng/dogo/stargazers) - Monitoring changes in the source file and automatically compile and run (restart).
- [drone-jenkins](https://github.com/appleboy/drone-jenkins) [![GitHub stars](https://img.shields.io/github/stars/appleboy/drone-jenkins?style=flat)](https://github.com/appleboy/drone-jenkins/stargazers) - Trigger downstream Jenkins jobs using a binary, docker or Drone CI.
- [drone-scp](https://github.com/appleboy/drone-scp) [![GitHub stars](https://img.shields.io/github/stars/appleboy/drone-scp?style=flat)](https://github.com/appleboy/drone-scp/stargazers) - Copy files and artifacts via SSH using a binary, docker or Drone CI.
- [Dropship](https://github.com/chrismckenzie/dropship) [![GitHub stars](https://img.shields.io/github/stars/chrismckenzie/dropship?style=flat)](https://github.com/chrismckenzie/dropship/stargazers) - Tool for deploying code via cdn.
- [easyssh-proxy](https://github.com/appleboy/easyssh-proxy) [![GitHub stars](https://img.shields.io/github/stars/appleboy/easyssh-proxy?style=flat)](https://github.com/appleboy/easyssh-proxy/stargazers) - Golang package for easy remote execution through SSH and SCP downloading via `ProxyCommand`.
- [fac](https://github.com/mkchoi212/fac) [![GitHub stars](https://img.shields.io/github/stars/mkchoi212/fac?style=flat)](https://github.com/mkchoi212/fac/stargazers) - Command-line user interface to fix git merge conflicts.
- [Flannel](https://github.com/flannel-io/flannel) [![GitHub stars](https://img.shields.io/github/stars/flannel-io/flannel?style=flat)](https://github.com/flannel-io/flannel/stargazers) - Flannel is a network fabric for containers, designed for Kubernetes.
- [Fleet device management](https://github.com/fleetdm/fleet) [![GitHub stars](https://img.shields.io/github/stars/fleetdm/fleet?style=flat)](https://github.com/fleetdm/fleet/stargazers) - Lightweight, programmable telemetry for servers and workstations.
- [gaia](https://github.com/gaia-pipeline/gaia) [![GitHub stars](https://img.shields.io/github/stars/gaia-pipeline/gaia?style=flat)](https://github.com/gaia-pipeline/gaia/stargazers) - Build powerful pipelines in any programming language.
- [ghorg](https://github.com/gabrie30/ghorg) [![GitHub stars](https://img.shields.io/github/stars/gabrie30/ghorg?style=flat)](https://github.com/gabrie30/ghorg/stargazers) - Quickly clone an entire org/users repositories into one directory - Supports GitHub, GitLab, Gitea, and Bitbucket.
- [Gitea](https://github.com/go-gitea/gitea) [![GitHub stars](https://img.shields.io/github/stars/go-gitea/gitea?style=flat)](https://github.com/go-gitea/gitea/stargazers) - Fork of Gogs, entirely community driven.
- [gitea-github-migrator](https://git.jonasfranz.software/JonasFranzDEV/gitea-github-migrator) - Migrate all your GitHub repositories, issues, milestones and labels to your Gitea instance.
- [go-furnace](https://github.com/go-furnace/go-furnace) [![GitHub stars](https://img.shields.io/github/stars/go-furnace/go-furnace?style=flat)](https://github.com/go-furnace/go-furnace/stargazers) - Hosting solution written in Go. Deploy your Application with ease on AWS, GCP or DigitalOcean.
- [go-rocket-update](https://github.com/mouuff/go-rocket-update) [![GitHub stars](https://img.shields.io/github/stars/mouuff/go-rocket-update?style=flat)](https://github.com/mouuff/go-rocket-update/stargazers) - A simple way to make self updating Go applications - Supports Github and Gitlab.
- [go-selfupdate](https://github.com/sanbornm/go-selfupdate) [![GitHub stars](https://img.shields.io/github/stars/sanbornm/go-selfupdate?style=flat)](https://github.com/sanbornm/go-selfupdate/stargazers) - Enable your Go applications to self update.
- [gobrew](https://github.com/cryptojuice/gobrew) [![GitHub stars](https://img.shields.io/github/stars/cryptojuice/gobrew?style=flat)](https://github.com/cryptojuice/gobrew/stargazers) - gobrew lets you easily switch between multiple versions of go.
- [gobrew](https://github.com/kevincobain2000/gobrew) [![GitHub stars](https://img.shields.io/github/stars/kevincobain2000/gobrew?style=flat)](https://github.com/kevincobain2000/gobrew/stargazers) - Go version manager. Super simple tool to install and manage Go versions. Install go without root. Gobrew doesn't require shell rehash.
- [godbg](https://github.com/sirnewton01/godbg) [![GitHub stars](https://img.shields.io/github/stars/sirnewton01/godbg?style=flat)](https://github.com/sirnewton01/godbg/stargazers) - Web-based gdb front-end application.
- [Gogs](https://gogs.io/) - A Self Hosted Git Service in the Go Programming Language.
- [goma-gateway](https://github.com/jkaninda/goma-gateway) [![GitHub stars](https://img.shields.io/github/stars/jkaninda/goma-gateway?style=flat)](https://github.com/jkaninda/goma-gateway/stargazers) - A Lightweight API Gateway and Reverse Proxy with declarative config, robust middleware, and support for REST, GraphQL, TCP, UDP, and gRPC.
- [gonative](https://github.com/inconshreveable/gonative) [![GitHub stars](https://img.shields.io/github/stars/inconshreveable/gonative?style=flat)](https://github.com/inconshreveable/gonative/stargazers) - Tool which creates a build of Go that can cross compile to all platforms while still using the Cgo-enabled versions of the stdlib packages.
- [govvv](https://github.com/ahmetalpbalkan/govvv) [![GitHub stars](https://img.shields.io/github/stars/ahmetalpbalkan/govvv?style=flat)](https://github.com/ahmetalpbalkan/govvv/stargazers) - “go build” wrapper to easily add version information into Go binaries.
- [grapes](https://github.com/yaronsumel/grapes) [![GitHub stars](https://img.shields.io/github/stars/yaronsumel/grapes?style=flat)](https://github.com/yaronsumel/grapes/stargazers) - Lightweight tool designed to distribute commands over ssh with ease.
- [GVM](https://github.com/moovweb/gvm) [![GitHub stars](https://img.shields.io/github/stars/moovweb/gvm?style=flat)](https://github.com/moovweb/gvm/stargazers) - GVM provides an interface to manage Go versions.
- [Hey](https://github.com/rakyll/hey) [![GitHub stars](https://img.shields.io/github/stars/rakyll/hey?style=flat)](https://github.com/rakyll/hey/stargazers) - Hey is a tiny program that sends some load to a web application.
- [httpref](https://github.com/dnnrly/httpref) [![GitHub stars](https://img.shields.io/github/stars/dnnrly/httpref?style=flat)](https://github.com/dnnrly/httpref/stargazers) - httpref is a handy CLI reference for HTTP methods, status codes, headers, and TCP and UDP ports.
- [jcli](https://github.com/jenkins-zh/jenkins-cli) [![GitHub stars](https://img.shields.io/github/stars/jenkins-zh/jenkins-cli?style=flat)](https://github.com/jenkins-zh/jenkins-cli/stargazers) - Jenkins CLI allows you manage your Jenkins as an easy way.
- [k0s](https://github.com/k0sproject/k0s) [![GitHub stars](https://img.shields.io/github/stars/k0sproject/k0s?style=flat)](https://github.com/k0sproject/k0s/stargazers) - Zero Friction Kubernetes distribution.
- [k3d](https://github.com/k3d-io/k3d) [![GitHub stars](https://img.shields.io/github/stars/k3d-io/k3d?style=flat)](https://github.com/k3d-io/k3d/stargazers) - Little helper to run CNCF's k3s in Docker.
- [k3s](https://github.com/k3s-io/k3s) [![GitHub stars](https://img.shields.io/github/stars/k3s-io/k3s?style=flat)](https://github.com/k3s-io/k3s/stargazers) - Lightweight Kubernetes.
- [k6](https://github.com/grafana/k6) [![GitHub stars](https://img.shields.io/github/stars/grafana/k6?style=flat)](https://github.com/grafana/k6/stargazers) - A modern load testing tool, using Go and JavaScript.
- [k9s](https://github.com/derailed/k9s) [![GitHub stars](https://img.shields.io/github/stars/derailed/k9s?style=flat)](https://github.com/derailed/k9s/stargazers) - Kubernetes CLI to manage your clusters in style.
- [kala](https://github.com/ajvb/kala) [![GitHub stars](https://img.shields.io/github/stars/ajvb/kala?style=flat)](https://github.com/ajvb/kala/stargazers) - Simplistic, modern, and performant job scheduler.
- [kcli](https://github.com/cswank/kcli) [![GitHub stars](https://img.shields.io/github/stars/cswank/kcli?style=flat)](https://github.com/cswank/kcli/stargazers) - Command line tool for inspecting kafka topics/partitions/messages.
- [kepfi](https://github.com/Knuspii/kepfi) [![GitHub stars](https://img.shields.io/github/stars/Knuspii/kepfi?style=flat)](https://github.com/Knuspii/kepfi/stargazers) - A smart alternative to rm with a recovery bin and storage tracking.
- [kind](https://github.com/kubernetes-sigs/kind) [![GitHub stars](https://img.shields.io/github/stars/kubernetes-sigs/kind?style=flat)](https://github.com/kubernetes-sigs/kind/stargazers) - Kubernetes IN Docker - local clusters for testing Kubernetes.
- [ko](https://github.com/google/ko) [![GitHub stars](https://img.shields.io/github/stars/google/ko?style=flat)](https://github.com/google/ko/stargazers) - Command line tool for building and deploying Go applications on Kubernetes
- [kool](https://github.com/kool-dev/kool) [![GitHub stars](https://img.shields.io/github/stars/kool-dev/kool?style=flat)](https://github.com/kool-dev/kool/stargazers) - Command line tool for managing Docker environments as an easy way.
- [kubeblocks](https://github.com/apecloud/kubeblocks) [![GitHub stars](https://img.shields.io/github/stars/apecloud/kubeblocks?style=flat)](https://github.com/apecloud/kubeblocks/stargazers) - KubeBlocks is an open-source control plane that runs and manages databases, message queues and other data infrastructure on K8s.
- [kubefwd](https://github.com/txn2/kubefwd) [![GitHub stars](https://img.shields.io/github/stars/txn2/kubefwd?style=flat)](https://github.com/txn2/kubefwd/stargazers) - Bulk Kubernetes port forwarding with unique IPs per service for local development.
- [kubernetes](https://github.com/kubernetes/kubernetes) [![GitHub stars](https://img.shields.io/github/stars/kubernetes/kubernetes?style=flat)](https://github.com/kubernetes/kubernetes/stargazers) - Container Cluster Manager from Google.
- [kubeshark](https://github.com/kubeshark/kubeshark) [![GitHub stars](https://img.shields.io/github/stars/kubeshark/kubeshark?style=flat)](https://github.com/kubeshark/kubeshark/stargazers) - API traffic analyzer for Kubernetes, inspired by Wireshark, purposely built for Kubernetes.
- [KubeVela](https://github.com/kubevela/kubevela) [![GitHub stars](https://img.shields.io/github/stars/kubevela/kubevela?style=flat)](https://github.com/kubevela/kubevela/stargazers) - Cloud native application delivery.
- [KubeVPN](https://github.com/kubenetworks/kubevpn) [![GitHub stars](https://img.shields.io/github/stars/kubenetworks/kubevpn?style=flat)](https://github.com/kubenetworks/kubevpn/stargazers) - KubeVPN offers a Cloud-Native Dev Environment that seamlessly connects to your Kubernetes cluster network.
- [KusionStack](https://github.com/KusionStack/kusion) [![GitHub stars](https://img.shields.io/github/stars/KusionStack/kusion?style=flat)](https://github.com/KusionStack/kusion/stargazers) - A unified programmable configuration techstack to deliver modern app in 'platform as code' and 'infra as code' approach.
- [kwatch](https://github.com/abahmed/kwatch) [![GitHub stars](https://img.shields.io/github/stars/abahmed/kwatch?style=flat)](https://github.com/abahmed/kwatch/stargazers) - Monitor & detect crashes in your Kubernetes(K8s) cluster instantly.
- [lstags](https://github.com/ivanilves/lstags) [![GitHub stars](https://img.shields.io/github/stars/ivanilves/lstags?style=flat)](https://github.com/ivanilves/lstags/stargazers) - Tool and API to sync Docker images across different registries.
- [lwc](https://github.com/timdp/lwc) [![GitHub stars](https://img.shields.io/github/stars/timdp/lwc?style=flat)](https://github.com/timdp/lwc/stargazers) - A live-updating version of the UNIX wc command.
- [manssh](https://github.com/xwjdsh/manssh) [![GitHub stars](https://img.shields.io/github/stars/xwjdsh/manssh?style=flat)](https://github.com/xwjdsh/manssh/stargazers) - manssh is a command line tool for managing your ssh alias config easily.
- [Mantil](https://github.com/mantil-io/mantil) [![GitHub stars](https://img.shields.io/github/stars/mantil-io/mantil?style=flat)](https://github.com/mantil-io/mantil/stargazers) - Go specific framework for building serverless applications on AWS that enables you to focus on pure Go code while Mantil takes care of the infrastructure.
- [minikube](https://github.com/kubernetes/minikube) [![GitHub stars](https://img.shields.io/github/stars/kubernetes/minikube?style=flat)](https://github.com/kubernetes/minikube/stargazers) - Run Kubernetes locally.
- [Moby](https://github.com/moby/moby) [![GitHub stars](https://img.shields.io/github/stars/moby/moby?style=flat)](https://github.com/moby/moby/stargazers) - Collaborative project for the container ecosystem to assemble container-based systems.
- [Mora](https://github.com/emicklei/mora) [![GitHub stars](https://img.shields.io/github/stars/emicklei/mora?style=flat)](https://github.com/emicklei/mora/stargazers) - REST server for accessing MongoDB documents and meta data.
- [ostent](https://github.com/ostrost/ostent) [![GitHub stars](https://img.shields.io/github/stars/ostrost/ostent?style=flat)](https://github.com/ostrost/ostent/stargazers) - collects and displays system metrics and optionally relays to Graphite and/or InfluxDB.
- [Packer](https://github.com/mitchellh/packer) [![GitHub stars](https://img.shields.io/github/stars/mitchellh/packer?style=flat)](https://github.com/mitchellh/packer/stargazers) - Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
- [Pewpew](https://github.com/bengadbois/pewpew) [![GitHub stars](https://img.shields.io/github/stars/bengadbois/pewpew?style=flat)](https://github.com/bengadbois/pewpew/stargazers) - Flexible HTTP command line stress tester.
- [pingtower](https://github.com/crleonard/pingtower) [![GitHub stars](https://img.shields.io/github/stars/crleonard/pingtower?style=flat)](https://github.com/crleonard/pingtower/stargazers) - Lightweight self-hosted uptime monitor for websites and APIs.
- [PipeCD](https://github.com/pipe-cd/pipecd) [![GitHub stars](https://img.shields.io/github/stars/pipe-cd/pipecd?style=flat)](https://github.com/pipe-cd/pipecd/stargazers) - A GitOps-style continuous delivery platform that provides consistent deployment and operations experience for any applications.
- [podinfo](https://github.com/stefanprodan/podinfo) [![GitHub stars](https://img.shields.io/github/stars/stefanprodan/podinfo?style=flat)](https://github.com/stefanprodan/podinfo/stargazers) - Podinfo is a tiny web application made with Go that showcases best practices of running microservices in Kubernetes. Podinfo is used by CNCF projects like Flux and Flagger for end-to-end testing and workshops.
- [podman-tui](https://github.com/containers/podman-tui) [![GitHub stars](https://img.shields.io/github/stars/containers/podman-tui?style=flat)](https://github.com/containers/podman-tui/stargazers) - Terminal UI for Podman management.
- [Pomerium](https://github.com/pomerium/pomerium) [![GitHub stars](https://img.shields.io/github/stars/pomerium/pomerium?style=flat)](https://github.com/pomerium/pomerium/stargazers) - Pomerium is an identity-aware access proxy.
- [Rodent](https://github.com/alouche/rodent) [![GitHub stars](https://img.shields.io/github/stars/alouche/rodent?style=flat)](https://github.com/alouche/rodent/stargazers) - Rodent helps you manage Go versions, projects and track dependencies.
- [s3-proxy](https://github.com/oxyno-zeta/s3-proxy) [![GitHub stars](https://img.shields.io/github/stars/oxyno-zeta/s3-proxy?style=flat)](https://github.com/oxyno-zeta/s3-proxy/stargazers) - S3 Proxy with GET, PUT and DELETE methods and authentication (OpenID Connect and Basic Auth).
- [s3gof3r](https://github.com/rlmcpherson/s3gof3r) [![GitHub stars](https://img.shields.io/github/stars/rlmcpherson/s3gof3r?style=flat)](https://github.com/rlmcpherson/s3gof3r/stargazers) - Small utility/library optimized for high speed transfer of large objects into and out of Amazon S3.
- [s5cmd](https://github.com/peak/s5cmd) [![GitHub stars](https://img.shields.io/github/stars/peak/s5cmd?style=flat)](https://github.com/peak/s5cmd/stargazers) - Blazing fast S3 and local filesystem execution tool.
- [Scaleway-cli](https://github.com/scaleway/scaleway-cli) [![GitHub stars](https://img.shields.io/github/stars/scaleway/scaleway-cli?style=flat)](https://github.com/scaleway/scaleway-cli/stargazers) - Manage BareMetal Servers from Command Line (as easily as with Docker).
- [script](https://github.com/bitfield/script) [![GitHub stars](https://img.shields.io/github/stars/bitfield/script?style=flat)](https://github.com/bitfield/script/stargazers) - Making it easy to write shell-like scripts in Go for DevOps and system administration tasks.
- [sg](https://github.com/ChristopherRabotin/sg) [![GitHub stars](https://img.shields.io/github/stars/ChristopherRabotin/sg?style=flat)](https://github.com/ChristopherRabotin/sg/stargazers) - Benchmarks a set of HTTP endpoints (like ab), with possibility to use the response code and data between each call for specific server stress based on its previous response.
- [sigma](https://github.com/go-sigma/sigma) [![GitHub stars](https://img.shields.io/github/stars/go-sigma/sigma?style=flat)](https://github.com/go-sigma/sigma/stargazers) - OCI-native container image registry, support OCI-native artifact, scan artifact, image build etc.
- [skm](https://github.com/TimothyYe/skm) [![GitHub stars](https://img.shields.io/github/stars/TimothyYe/skm?style=flat)](https://github.com/TimothyYe/skm/stargazers) - SKM is a simple and powerful SSH Keys Manager, it helps you to manage your multiple SSH keys easily!
- [StatusOK](https://github.com/sanathp/statusok) [![GitHub stars](https://img.shields.io/github/stars/sanathp/statusok?style=flat)](https://github.com/sanathp/statusok/stargazers) - Monitor your Website and REST APIs.Get Notified through Slack, E-mail when your server is down or response time is more than expected.
- [tau](https://github.com/taubyte/tau) [![GitHub stars](https://img.shields.io/github/stars/taubyte/tau?style=flat)](https://github.com/taubyte/tau/stargazers) - Easily build Cloud Computing Platforms with features like Serverless WebAssembly Functions, Frontend Hosting, CI/CD, Object Storage, K/V Database, and Pub-Sub Messaging.
- [terraform-provider-openapi](https://github.com/dikhan/terraform-provider-openapi) [![GitHub stars](https://img.shields.io/github/stars/dikhan/terraform-provider-openapi?style=flat)](https://github.com/dikhan/terraform-provider-openapi/stargazers) - Terraform provider plugin that dynamically configures itself at runtime based on an OpenAPI document (formerly known as swagger file) containing the definitions of the APIs exposed.
- [tf-profile](https://github.com/datarootsio/tf-profile) [![GitHub stars](https://img.shields.io/github/stars/datarootsio/tf-profile?style=flat)](https://github.com/datarootsio/tf-profile/stargazers) - Profiler for Terraform runs. Generate global stats, resource-level stats or visualizations.
- [tickstem/uptime](https://github.com/tickstem/uptime) [![GitHub stars](https://img.shields.io/github/stars/tickstem/uptime?style=flat)](https://github.com/tickstem/uptime/stargazers) - Go client for HTTP uptime monitoring with SSL expiry alerts and configurable response assertions.
- [tlm](https://github.com/yusufcanb/tlm) [![GitHub stars](https://img.shields.io/github/stars/yusufcanb/tlm?style=flat)](https://github.com/yusufcanb/tlm/stargazers) - Local cli copilot, powered by CodeLLaMa
- [traefik](https://github.com/containous/traefik) [![GitHub stars](https://img.shields.io/github/stars/containous/traefik?style=flat)](https://github.com/containous/traefik/stargazers) - Reverse proxy and load balancer with support for multiple backends.
- [trubka](https://github.com/xitonix/trubka) [![GitHub stars](https://img.shields.io/github/stars/xitonix/trubka?style=flat)](https://github.com/xitonix/trubka/stargazers) - A CLI tool to manage and troubleshoot Apache Kafka clusters with the ability of generically publishing/consuming protocol buffer and plain text events to/from Kafka.
- [Updatecli](https://github.com/updatecli/updatecli) [![GitHub stars](https://img.shields.io/github/stars/updatecli/updatecli?style=flat)](https://github.com/updatecli/updatecli/stargazers) - A universal declarative update policy engine.
- [uTask](https://github.com/ovh/utask) [![GitHub stars](https://img.shields.io/github/stars/ovh/utask?style=flat)](https://github.com/ovh/utask/stargazers) - Automation engine that models and executes business processes declared in yaml.
- [Vegeta](https://github.com/tsenart/vegeta) [![GitHub stars](https://img.shields.io/github/stars/tsenart/vegeta?style=flat)](https://github.com/tsenart/vegeta/stargazers) - HTTP load testing tool and library. It's over 9000!
- [wait-for](https://github.com/dnnrly/wait-for) [![GitHub stars](https://img.shields.io/github/stars/dnnrly/wait-for?style=flat)](https://github.com/dnnrly/wait-for/stargazers) - Wait for something to happen (from the command line) before continuing. Easy orchestration of Docker services and other things.
- [Wide](https://wide.b3log.org/login) - Web-based IDE for Teams using Golang.
- [winrm-cli](https://github.com/masterzen/winrm-cli) [![GitHub stars](https://img.shields.io/github/stars/masterzen/winrm-cli?style=flat)](https://github.com/masterzen/winrm-cli/stargazers) - Cli tool to remotely execute commands on Windows machines.
- [zerohand](https://github.com/nilpoona/zerohand) [![GitHub stars](https://img.shields.io/github/stars/nilpoona/zerohand?style=flat)](https://github.com/nilpoona/zerohand/stargazers) - A simple and efficient load testing tool for Web APIs.

**[⬆ back to top](#contents)**

### Other Software

- [Backrest](https://github.com/garethgeorge/backrest) [![GitHub stars](https://img.shields.io/github/stars/garethgeorge/backrest?style=flat)](https://github.com/garethgeorge/backrest/stargazers) - Web-based UI and orchestrator for restic backup.
- [Better Go Playground](https://goplay.tools) - Go playground with syntax highlight, code completion and other features.
- [blocky](https://github.com/0xERR0R/blocky) [![GitHub stars](https://img.shields.io/github/stars/0xERR0R/blocky?style=flat)](https://github.com/0xERR0R/blocky/stargazers) - Fast and lightweight DNS proxy as ad-blocker for local network with many features.
- [bluetuith](https://github.com/bluetuith-org/bluetuith) [![GitHub stars](https://img.shields.io/github/stars/bluetuith-org/bluetuith?style=flat)](https://github.com/bluetuith-org/bluetuith/stargazers) - TUI Bluetooth manager for Linux.
- [borg](https://github.com/crufter/borg) [![GitHub stars](https://img.shields.io/github/stars/crufter/borg?style=flat)](https://github.com/crufter/borg/stargazers) - Terminal based search engine for bash snippets.
- [boxed](https://github.com/tejo/boxed) [![GitHub stars](https://img.shields.io/github/stars/tejo/boxed?style=flat)](https://github.com/tejo/boxed/stargazers) - Dropbox based blog engine.
- [Chapar](https://github.com/chapar-rest/chapar) [![GitHub stars](https://img.shields.io/github/stars/chapar-rest/chapar?style=flat)](https://github.com/chapar-rest/chapar/stargazers) - Chapar is a a cross-platform Postman alternative built with go, aims to help developers to test their api endpoints. it support http and grpc protocols.
- [Cherry](https://github.com/rafael-santiago/cherry) [![GitHub stars](https://img.shields.io/github/stars/rafael-santiago/cherry?style=flat)](https://github.com/rafael-santiago/cherry/stargazers) - Tiny webchat server in Go.
- [Circuit](https://github.com/gocircuit/circuit) [![GitHub stars](https://img.shields.io/github/stars/gocircuit/circuit?style=flat)](https://github.com/gocircuit/circuit/stargazers) - Circuit is a programmable platform-as-a-service (PaaS) and/or Infrastructure-as-a-Service (IaaS), for management, discovery, synchronization and orchestration of services and hosts comprising cloud applications.
- [Comcast](https://github.com/tylertreat/Comcast) [![GitHub stars](https://img.shields.io/github/stars/tylertreat/Comcast?style=flat)](https://github.com/tylertreat/Comcast/stargazers) - Simulate bad network connections.
- [confd](https://github.com/kelseyhightower/confd) [![GitHub stars](https://img.shields.io/github/stars/kelseyhightower/confd?style=flat)](https://github.com/kelseyhightower/confd/stargazers) - Manage local application configuration files using templates and data from etcd or consul.
- [crawley](https://github.com/s0rg/crawley) [![GitHub stars](https://img.shields.io/github/stars/s0rg/crawley?style=flat)](https://github.com/s0rg/crawley/stargazers) - Web scraper/crawler for cli.
- [croc](https://github.com/schollz/croc) [![GitHub stars](https://img.shields.io/github/stars/schollz/croc?style=flat)](https://github.com/schollz/croc/stargazers) - Easily and securely send files or folders from one computer to another.
- [CrunchyCleaner](https://github.com/Knuspii/CrunchyCleaner) [![GitHub stars](https://img.shields.io/github/stars/Knuspii/CrunchyCleaner?style=flat)](https://github.com/Knuspii/CrunchyCleaner/stargazers) - A lightweight, software cache cleanup tool for Windows & Linux.
- [Documize](https://github.com/documize/community) [![GitHub stars](https://img.shields.io/github/stars/documize/community?style=flat)](https://github.com/documize/community/stargazers) - Modern wiki software that integrates data from SaaS tools.
- [dp](https://github.com/scryinfo/dp) [![GitHub stars](https://img.shields.io/github/stars/scryinfo/dp?style=flat)](https://github.com/scryinfo/dp/stargazers) - Through SDK for data exchange with blockchain, developers can get easy access to DAPP development.
- [drive](https://github.com/odeke-em/drive) [![GitHub stars](https://img.shields.io/github/stars/odeke-em/drive?style=flat)](https://github.com/odeke-em/drive/stargazers) - Google Drive client for the commandline.
- [Duplicacy](https://github.com/gilbertchen/duplicacy) [![GitHub stars](https://img.shields.io/github/stars/gilbertchen/duplicacy?style=flat)](https://github.com/gilbertchen/duplicacy/stargazers) - A cross-platform network and cloud backup tool based on the idea of lock-free deduplication.
- [fjira](https://github.com/mk-5/fjira) [![GitHub stars](https://img.shields.io/github/stars/mk-5/fjira?style=flat)](https://github.com/mk-5/fjira/stargazers) - A fuzzy-search based terminal UI application for Attlasian Jira
- [Gebug](https://github.com/moshebe/gebug) [![GitHub stars](https://img.shields.io/github/stars/moshebe/gebug?style=flat)](https://github.com/moshebe/gebug/stargazers) - A tool that makes debugging of Dockerized Go applications super easy by enabling Debugger and Hot-Reload features, seamlessly.
- [gfile](https://github.com/Antonito/gfile) [![GitHub stars](https://img.shields.io/github/stars/Antonito/gfile?style=flat)](https://github.com/Antonito/gfile/stargazers) - Securely transfer files between two computers, without any third party, over WebRTC.
- [Go Package Store](https://github.com/shurcooL/Go-Package-Store) [![GitHub stars](https://img.shields.io/github/stars/shurcooL/Go-Package-Store?style=flat)](https://github.com/shurcooL/Go-Package-Store/stargazers) - App that displays updates for the Go packages in your GOPATH.
- [go-peerflix](https://github.com/Sioro-Neoku/go-peerflix) [![GitHub stars](https://img.shields.io/github/stars/Sioro-Neoku/go-peerflix?style=flat)](https://github.com/Sioro-Neoku/go-peerflix/stargazers) - Video streaming torrent client.
- [goblin](https://goblin.run) - Cloud builder for CLI's written in go lang
- [GoBoy](https://github.com/Humpheh/goboy) [![GitHub stars](https://img.shields.io/github/stars/Humpheh/goboy?style=flat)](https://github.com/Humpheh/goboy/stargazers) - Nintendo Game Boy Color emulator written in Go.
- [gocc](https://github.com/goccmack/gocc) [![GitHub stars](https://img.shields.io/github/stars/goccmack/gocc?style=flat)](https://github.com/goccmack/gocc/stargazers) - Gocc is a compiler kit for Go written in Go.
- [GoDocTooltip](https://github.com/diankong/GoDocTooltip) [![GitHub stars](https://img.shields.io/github/stars/diankong/GoDocTooltip?style=flat)](https://github.com/diankong/GoDocTooltip/stargazers) - Chrome extension for Go Doc sites, which shows function description as tooltip at function list.
- [Gokapi](https://github.com/Forceu/gokapi) [![GitHub stars](https://img.shields.io/github/stars/Forceu/gokapi?style=flat)](https://github.com/Forceu/gokapi/stargazers) - Lightweight server to share files, which expire after a set amount of downloads or days. Similar to Firefox Send, but without public upload.
- [GoLand](https://jetbrains.com/go) - Full featured cross-platform Go IDE.
- [GoNB](https://github.com/janpfeifer/gonb) [![GitHub stars](https://img.shields.io/github/stars/janpfeifer/gonb?style=flat)](https://github.com/janpfeifer/gonb/stargazers) - Interactive Go programming with Jupyter Notebooks (also works in VSCode, Binder and Google's Colab).
- [GooseForum](https://github.com/leancodebox/GooseForum) [![GitHub stars](https://img.shields.io/github/stars/leancodebox/GooseForum?style=flat)](https://github.com/leancodebox/GooseForum/stargazers) - Self-hosted forum platform built with Go, Vue, and Tailwind CSS.
- [Gor](https://github.com/buger/gor) [![GitHub stars](https://img.shields.io/github/stars/buger/gor?style=flat)](https://github.com/buger/gor/stargazers) - Http traffic replication tool, for replaying traffic from production to stage/dev environments in real-time.
- [Guora](https://github.com/meloalright/guora) [![GitHub stars](https://img.shields.io/github/stars/meloalright/guora?style=flat)](https://github.com/meloalright/guora/stargazers) - A self-hosted Quora like web application written in Go.
- [hoofli](https://github.com/dnnrly/hoofli) [![GitHub stars](https://img.shields.io/github/stars/dnnrly/hoofli?style=flat)](https://github.com/dnnrly/hoofli/stargazers) - Generate PlantUML diagrams from Chrome or Firefox network inspections.
- [hotswap](https://github.com/edwingeng/hotswap) [![GitHub stars](https://img.shields.io/github/stars/edwingeng/hotswap?style=flat)](https://github.com/edwingeng/hotswap/stargazers) - A complete solution to reload your go code without restarting your server, interrupting or blocking any ongoing procedure.
- [hugo](https://gohugo.io/) - Fast and Modern Static Website Engine.
- [ide](https://github.com/thestrukture/ide) [![GitHub stars](https://img.shields.io/github/stars/thestrukture/ide?style=flat)](https://github.com/thestrukture/ide/stargazers) - Browser accessible IDE. Designed for Go with Go.
- [joincap](https://github.com/assafmo/joincap) [![GitHub stars](https://img.shields.io/github/stars/assafmo/joincap?style=flat)](https://github.com/assafmo/joincap/stargazers) - Command-line utility for merging multiple pcap files together.
- [JuiceFS](https://github.com/juicedata/juicefs) [![GitHub stars](https://img.shields.io/github/stars/juicedata/juicefs?style=flat)](https://github.com/juicedata/juicefs/stargazers) - Distributed POSIX file system built on top of Redis and AWS S3.
- [Juju](https://jujucharms.com/) - Cloud-agnostic service deployment and orchestration - supports EC2, Azure, Openstack, MAAS and more.
- [Layli](https://layli.app) - Draw pretty layout diagrams as code.
- [Leaps](https://github.com/jeffail/leaps) [![GitHub stars](https://img.shields.io/github/stars/jeffail/leaps?style=flat)](https://github.com/jeffail/leaps/stargazers) - Pair programming service using Operational Transforms.
- [lgo](https://github.com/yunabe/lgo) [![GitHub stars](https://img.shields.io/github/stars/yunabe/lgo?style=flat)](https://github.com/yunabe/lgo/stargazers) - Interactive Go programming with Jupyter. It supports code completion, code inspection and 100% Go compatibility.
- [limetext](https://limetext.github.io) - Lime Text is a powerful and elegant text editor primarily developed in Go that aims to be a Free and open-source software successor to Sublime Text.
- [LiteIDE](https://github.com/visualfc/liteide) [![GitHub stars](https://img.shields.io/github/stars/visualfc/liteide?style=flat)](https://github.com/visualfc/liteide/stargazers) - LiteIDE is a simple, open source, cross-platform Go IDE.
- [mac-cleanup-go](https://github.com/2ykwang/mac-cleanup-go) [![GitHub stars](https://img.shields.io/github/stars/2ykwang/mac-cleanup-go?style=flat)](https://github.com/2ykwang/mac-cleanup-go/stargazers) - Preview-first TUI for cleaning macOS caches, logs, and temporary files.
- [mdv](https://github.com/Allra-Fintech/mdv) [![GitHub stars](https://img.shields.io/github/stars/Allra-Fintech/mdv?style=flat)](https://github.com/Allra-Fintech/mdv/stargazers) - CLI tool that renders Markdown files in the browser with live reload, GFM, syntax highlighting, Mermaid diagrams, and PDF export.
- [mockingjay](https://github.com/quii/mockingjay-server) [![GitHub stars](https://img.shields.io/github/stars/quii/mockingjay-server?style=flat)](https://github.com/quii/mockingjay-server/stargazers) - Fake HTTP servers and consumer driven contracts from one configuration file. You can also make the server randomly misbehave to help do more realistic performance tests.
- [myLG](https://github.com/mehrdadrad/mylg) [![GitHub stars](https://img.shields.io/github/stars/mehrdadrad/mylg?style=flat)](https://github.com/mehrdadrad/mylg/stargazers) - Command Line Network Diagnostic tool written in Go.
- [naclpipe](https://github.com/unix4fun/naclpipe) [![GitHub stars](https://img.shields.io/github/stars/unix4fun/naclpipe?style=flat)](https://github.com/unix4fun/naclpipe/stargazers) - Simple NaCL EC25519 based crypto pipe tool written in Go.
- [Neo-cowsay](https://github.com/Code-Hex/Neo-cowsay) [![GitHub stars](https://img.shields.io/github/stars/Code-Hex/Neo-cowsay?style=flat)](https://github.com/Code-Hex/Neo-cowsay/stargazers) - 🐮 cowsay is reborn. for a New Era.
- [nes](https://github.com/fogleman/nes) [![GitHub stars](https://img.shields.io/github/stars/fogleman/nes?style=flat)](https://github.com/fogleman/nes/stargazers) - Nintendo Entertainment System (NES) emulator written in Go.
- [onWatch](https://github.com/onllm-dev/onWatch) [![GitHub stars](https://img.shields.io/github/stars/onllm-dev/onWatch?style=flat)](https://github.com/onllm-dev/onWatch/stargazers) - Monitor AI API quotas across providers locally with historical tracking, alerts, and a web dashboard to avoid surprise throttling and budget overruns.
- [Orbit](https://github.com/gulien/orbit) [![GitHub stars](https://img.shields.io/github/stars/gulien/orbit?style=flat)](https://github.com/gulien/orbit/stargazers) - A simple tool for running commands and generating files from templates.
- [peg](https://github.com/pointlander/peg) [![GitHub stars](https://img.shields.io/github/stars/pointlander/peg?style=flat)](https://github.com/pointlander/peg/stargazers) - Peg, Parsing Expression Grammar, is an implementation of a Packrat parser generator.
- [Plik](https://github.com/root-gg/plik) [![GitHub stars](https://img.shields.io/github/stars/root-gg/plik?style=flat)](https://github.com/root-gg/plik/stargazers) - Plik is a temporary file upload system (Wetransfer like) in Go.
- [portal](https://github.com/SpatiumPortae/portal) [![GitHub stars](https://img.shields.io/github/stars/SpatiumPortae/portal?style=flat)](https://github.com/SpatiumPortae/portal/stargazers) - Portal is a quick and easy command-line file transfer utility from any computer to another.
- [restic](https://github.com/restic/restic) [![GitHub stars](https://img.shields.io/github/stars/restic/restic?style=flat)](https://github.com/restic/restic/stargazers) - De-duplicating backup program.
- [sake](https://github.com/alajmo/sake) [![GitHub stars](https://img.shields.io/github/stars/alajmo/sake?style=flat)](https://github.com/alajmo/sake/stargazers) - sake is a command runner for local and remote hosts.
- [scc](https://github.com/boyter/scc) [![GitHub stars](https://img.shields.io/github/stars/boyter/scc?style=flat)](https://github.com/boyter/scc/stargazers) - Sloc Cloc and Code, a very fast accurate code counter with complexity calculations and COCOMO estimates.
- [Seaweed File System](https://github.com/chrislusf/seaweedfs) [![GitHub stars](https://img.shields.io/github/stars/chrislusf/seaweedfs?style=flat)](https://github.com/chrislusf/seaweedfs/stargazers) - Fast, Simple and Scalable Distributed File System with O(1) disk seek.
- [shell2http](https://github.com/msoap/shell2http) [![GitHub stars](https://img.shields.io/github/stars/msoap/shell2http?style=flat)](https://github.com/msoap/shell2http/stargazers) - Executing shell commands via http server (for prototyping or remote control).
- [Snitch](https://github.com/lucasgomide/snitch) [![GitHub stars](https://img.shields.io/github/stars/lucasgomide/snitch?style=flat)](https://github.com/lucasgomide/snitch/stargazers) - Simple way to notify your team and many tools when someone has deployed any application via Tsuru.
- [sonic](https://github.com/go-sonic/sonic) [![GitHub stars](https://img.shields.io/github/stars/go-sonic/sonic?style=flat)](https://github.com/go-sonic/sonic/stargazers) - Sonic is a Go Blogging Platform. Simple and Powerful.
- [Stack Up](https://github.com/pressly/sup) [![GitHub stars](https://img.shields.io/github/stars/pressly/sup?style=flat)](https://github.com/pressly/sup/stargazers) - Stack Up, a super simple deployment tool - just Unix - think of it like 'make' for a network of servers.
- [stew](https://github.com/marwanhawari/stew) [![GitHub stars](https://img.shields.io/github/stars/marwanhawari/stew?style=flat)](https://github.com/marwanhawari/stew/stargazers) - An independent package manager for compiled binaries.
- [syncthing](https://syncthing.net/) - Open, decentralized file synchronization tool and protocol.
- [tcpdog](https://github.com/mehrdadrad/tcpdog) [![GitHub stars](https://img.shields.io/github/stars/mehrdadrad/tcpdog?style=flat)](https://github.com/mehrdadrad/tcpdog/stargazers) - eBPF based TCP observability.
- [tinycare-tui](https://github.com/DMcP89/tinycare-tui) [![GitHub stars](https://img.shields.io/github/stars/DMcP89/tinycare-tui?style=flat)](https://github.com/DMcP89/tinycare-tui/stargazers) - Small terminal app that shows git commits from the last 24 hours and week, current weather, some self care advice, a joke, and you current todo list tasks.
- [tldx](https://github.com/brandonyoungdev/tldx) [![GitHub stars](https://img.shields.io/github/stars/brandonyoungdev/tldx?style=flat)](https://github.com/brandonyoungdev/tldx/stargazers) - Bulk domain availability checker using RDAP, DNS, and WHOIS fallback with keyword permutation generation.
- [toxiproxy](https://github.com/shopify/toxiproxy) [![GitHub stars](https://img.shields.io/github/stars/shopify/toxiproxy?style=flat)](https://github.com/shopify/toxiproxy/stargazers) - Proxy to simulate network and system conditions for automated tests.
- [tsuru](https://tsuru.io/) - Extensible and open source Platform as a Service software.
- [vaku](https://github.com/lingrino/vaku) [![GitHub stars](https://img.shields.io/github/stars/lingrino/vaku?style=flat)](https://github.com/lingrino/vaku/stargazers) - CLI & API for folder-based functions in Vault like copy, move, and search.
- [vFlow](https://github.com/VerizonDigital/vflow) [![GitHub stars](https://img.shields.io/github/stars/VerizonDigital/vflow?style=flat)](https://github.com/VerizonDigital/vflow/stargazers) - High-performance, scalable and reliable IPFIX, sFlow and Netflow collector.
- [Wave Terminal](https://waveterm.dev) - Wave is an open-source, AI-native terminal built for seamless developer workflows with inline rendering, a modern UI, and persistent sessions.
- [wellington](https://github.com/wellington/wellington) [![GitHub stars](https://img.shields.io/github/stars/wellington/wellington?style=flat)](https://github.com/wellington/wellington/stargazers) - Sass project management tool, extends the language with sprite functions (like Compass).
- [woke](https://github.com/get-woke/woke) [![GitHub stars](https://img.shields.io/github/stars/get-woke/woke?style=flat)](https://github.com/get-woke/woke/stargazers) - Detect non-inclusive language in your source code.
- [yai](https://github.com/ekkinox/yai) [![GitHub stars](https://img.shields.io/github/stars/ekkinox/yai?style=flat)](https://github.com/ekkinox/yai/stargazers) - AI powered terminal assistant.
- [zs](https://git.mills.io/prologic/zs) - an extremely minimal static site generator.

**[⬆ back to top](#contents)**

# Resources

_Where to discover new Go libraries._

**[⬆ back to top](#contents)**

## Benchmarks

- [autobench](https://github.com/davecheney/autobench) [![GitHub stars](https://img.shields.io/github/stars/davecheney/autobench?style=flat)](https://github.com/davecheney/autobench/stargazers) - Framework to compare the performance between different Go versions.
- [go-benchmark-app](https://github.com/mrLSD/go-benchmark-app) [![GitHub stars](https://img.shields.io/github/stars/mrLSD/go-benchmark-app?style=flat)](https://github.com/mrLSD/go-benchmark-app/stargazers) - Powerful HTTP-benchmark tool mixed with Аb, Wrk, Siege tools. Gathering statistics and various parameters for benchmarks and comparison results.
- [go-benchmarks](https://github.com/tylertreat/go-benchmarks) [![GitHub stars](https://img.shields.io/github/stars/tylertreat/go-benchmarks?style=flat)](https://github.com/tylertreat/go-benchmarks/stargazers) - Few miscellaneous Go microbenchmarks. Compare some language features to alternative approaches.
- [go-http-routing-benchmark](https://github.com/julienschmidt/go-http-routing-benchmark) [![GitHub stars](https://img.shields.io/github/stars/julienschmidt/go-http-routing-benchmark?style=flat)](https://github.com/julienschmidt/go-http-routing-benchmark/stargazers) - Go HTTP request router benchmark and comparison.
- [go-json-benchmark](https://github.com/zerosnake0/go-json-benchmark) [![GitHub stars](https://img.shields.io/github/stars/zerosnake0/go-json-benchmark?style=flat)](https://github.com/zerosnake0/go-json-benchmark/stargazers) - Go JSON benchmark.
- [go-ml-benchmarks](https://github.com/nikolaydubina/go-ml-benchmarks) [![GitHub stars](https://img.shields.io/github/stars/nikolaydubina/go-ml-benchmarks?style=flat)](https://github.com/nikolaydubina/go-ml-benchmarks/stargazers) - benchmarks for machine learning inference in Go.
- [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) [![GitHub stars](https://img.shields.io/github/stars/smallnest/go-web-framework-benchmark?style=flat)](https://github.com/smallnest/go-web-framework-benchmark/stargazers) - Go web framework benchmark.
- [go_serialization_benchmarks](https://github.com/alecthomas/go_serialization_benchmarks) [![GitHub stars](https://img.shields.io/github/stars/alecthomas/go_serialization_benchmarks?style=flat)](https://github.com/alecthomas/go_serialization_benchmarks/stargazers) - Benchmarks of Go serialization methods.
- [gocostmodel](https://github.com/PuerkitoBio/gocostmodel) [![GitHub stars](https://img.shields.io/github/stars/PuerkitoBio/gocostmodel?style=flat)](https://github.com/PuerkitoBio/gocostmodel/stargazers) - Benchmarks of common basic operations for the Go language.
- [golang-benchmarks](https://github.com/SimonWaldherr/golang-benchmarks) [![GitHub stars](https://img.shields.io/github/stars/SimonWaldherr/golang-benchmarks?style=flat)](https://github.com/SimonWaldherr/golang-benchmarks/stargazers) - a collection of golang benchmarks.
- [gospeed](https://github.com/feyeleanor/GoSpeed) [![GitHub stars](https://img.shields.io/github/stars/feyeleanor/GoSpeed?style=flat)](https://github.com/feyeleanor/GoSpeed/stargazers) - Go micro-benchmarks for calculating the speed of language constructs.
- [kvbench](https://github.com/jimrobinson/kvbench) [![GitHub stars](https://img.shields.io/github/stars/jimrobinson/kvbench?style=flat)](https://github.com/jimrobinson/kvbench/stargazers) - Key/Value database benchmark.
- [skynet](https://github.com/atemerev/skynet) [![GitHub stars](https://img.shields.io/github/stars/atemerev/skynet?style=flat)](https://github.com/atemerev/skynet/stargazers) - Skynet 1M threads microbenchmark.
- [speedtest-resize](https://github.com/fawick/speedtest-resize) [![GitHub stars](https://img.shields.io/github/stars/fawick/speedtest-resize?style=flat)](https://github.com/fawick/speedtest-resize/stargazers) - Compare various Image resize algorithms for the Go language.
- [vizb](https://github.com/goptics/vizb) [![GitHub stars](https://img.shields.io/github/stars/goptics/vizb?style=flat)](https://github.com/goptics/vizb/stargazers) - A CLI tool to visualize Go benchmark data in 4D.

**[⬆ back to top](#contents)**

## Conferences

- [GoCon](https://gocon.connpass.com/) - Tokyo, Japan.
- [GoDays](https://www.godays.io/) - Berlin, Germany.
- [GoLab](https://golab.io/) - Florence, Italy.
- [GopherCon](https://www.gophercon.com/) - Varied Locations Each Year, USA.
- [GopherCon Africa](https://gophercon.africa/) - Nairobi, Kenya.
- [GopherCon Australia](https://gophercon.com.au/) - Sydney, Australia.
- [GopherCon Brazil](https://gopherconbr.org) - Florianópolis, Brazil.
- [GopherCon China](https://gophercon.com.cn) - Shanghai, China.
- [GopherCon Europe](https://gophercon.eu/) - Berlin, Germany.
- [GopherCon India](https://gopherconindia.org/) - Pune, India.
- [GopherCon Israel](https://www.gophercon.org.il/) - Tel Aviv, Israel.
- [GopherCon Russia](https://www.gophercon-russia.ru) - Moscow, Russia.
- [GopherCon Singapore](https://gophercon.sg) - Mapletree Business City, Singapore.
- [GopherCon UK](https://www.gophercon.co.uk/) - London, UK.
- [GopherCon Vietnam](https://gophercon.vn/) - Ho Chi Minh City, Vietnam.
- [GoWest Conference](https://www.gowestconf.com/) - Lehi, USA.

**[⬆ back to top](#contents)**

## E-Books

### E-books for purchase

- [100 Go Mistakes: How to Avoid Them](https://www.manning.com/books/100-go-mistakes-how-to-avoid-them)
- [Black Hat Go](https://nostarch.com/blackhatgo) - Go programming for hackers and pentesters.
- [Build an Orchestrator in Go](https://www.manning.com/books/build-an-orchestrator-in-go)
- [Continuous Delivery in Go](https://www.manning.com/books/continuous-delivery-in-go) - This practical guide to continuous delivery shows you how to rapidly establish an automated pipeline that will improve your testing, code quality, and final product.
- [Creative DIY Microcontroller Project With TinyGo and WebAssembly](https://www.packtpub.com/product/creative-diy-microcontroller-projects-with-tinygo-and-webassembly/9781800560208) - An introduction into the TinyGo compiler with projects involving Arduino and WebAssembly.
- [Effective Go: Elegant, efficient, and testable code](https://www.manning.com/books/effective-go) - Unlock Go’s unique perspective on program design, and start writing simple, maintainable, and testable Go code.
- [For the Love of Go](https://bitfieldconsulting.com/books/love) - An introductory book for Go beginners.
- [Go in Practice, Second Edition](https://www.manning.com/books/go-in-practice-second-edition) - Your practical guide on the ins-and-outs of Go development, covering the standard library and the most important tools from Go’s powerful ecosystem.
- [Know Go: Generics](https://bitfieldconsulting.com/books/generics) - A guide to understanding and using generics in Go.
- [Lets-Go](https://lets-go.alexedwards.net) - A step-by-step guide to creating fast, secure and maintanable web applications with Go.
- [Lets-Go-Further](https://lets-go-further.alexedwards.net) - Advanced patterns for building APIs and web applications in Go.
- [The Power of Go: Tests](https://bitfieldconsulting.com/books/tests) - A guide to testing in Go.
- [The Power of Go: Tools](https://bitfieldconsulting.com/books/tools) - A guide to writing command-line tools in Go.
- [Writing A Compiler In Go](https://compilerbook.com)
- [Writing An Interpreter In Go](https://interpreterbook.com) - Book that introduces dozens of techniques for writing idiomatic, expressive, and efficient Go code that avoids common pitfalls.

### Free e-books

- [A Go Developer's Notebook](https://leanpub.com/GoNotebook/read)
- [An Introduction to Programming in Go](http://www.golang-book.com/)
- [Build a blockchain from scratch in Go with gRPC](https://github.com/volodymyrprokopyuk/go-blockchain) [![GitHub stars](https://img.shields.io/github/stars/volodymyrprokopyuk/go-blockchain?style=flat)](https://github.com/volodymyrprokopyuk/go-blockchain/stargazers) - The foundational and practical guide for effectively learning and progressively building a blockchain from scratch in Go with gRPC.
- [Build Web Application with Golang](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/)
- [Building Web Apps With Go](https://codegangsta.gitbooks.io/building-web-apps-with-go/content/)
- [Go 101](https://go101.org) - A book focusing on Go syntax/semantics and all kinds of details.
- [Go AST Book (Chinese)](https://github.com/chai2010/go-ast-book) [![GitHub stars](https://img.shields.io/github/stars/chai2010/go-ast-book?style=flat)](https://github.com/chai2010/go-ast-book/stargazers) - A book focusing on Go `go/*` packages.
- [Go Faster](https://leanpub.com/gofaster) - This book seeks to shorten your learning curve and help you become a proficient Go programmer, faster.
- [Go Succinctly](https://github.com/thedevsir/gosuccinctly) [![GitHub stars](https://img.shields.io/github/stars/thedevsir/gosuccinctly?style=flat)](https://github.com/thedevsir/gosuccinctly/stargazers) - in Persian.
- [Go with the domain](https://threedots.tech/go-with-the-domain/) - A book showing how to apply DDD, Clean Architecture, and CQRS by practical refactoring.
- [GoBooks](https://github.com/dariubs/GoBooks) [![GitHub stars](https://img.shields.io/github/stars/dariubs/GoBooks?style=flat)](https://github.com/dariubs/GoBooks/stargazers) - A curated list of Go books.
- [How To Code in Go eBook](https://www.digitalocean.com/community/books/how-to-code-in-go-ebook) - A 600 page introduction to Go aimed at first time developers.
- [Learning Go](https://www.miek.nl/downloads/Go/Learning-Go-latest.pdf)
- [Network Programming With Go](https://jan.newmarch.name/golang/)
- [Practical Go Lessons](https://www.practical-go-lessons.com/)
- [Spaceship Go A Journey to the Standard Library](https://blasrodri.github.io/spaceship-go-gh-pages/)
- [The Go Programming Language](https://www.gopl.io/)
- [The Golang Standard Library by Example (Chinese)](https://github.com/polaris1119/The-Golang-Standard-Library-by-Example) [![GitHub stars](https://img.shields.io/github/stars/polaris1119/The-Golang-Standard-Library-by-Example?style=flat)](https://github.com/polaris1119/The-Golang-Standard-Library-by-Example/stargazers)
- [The Little Go Book](https://github.com/karlseguin/the-little-go-book) [![GitHub stars](https://img.shields.io/github/stars/karlseguin/the-little-go-book?style=flat)](https://github.com/karlseguin/the-little-go-book/stargazers)
- [Web Application with Go the Anti-Textbook](https://github.com/thewhitetulip/web-dev-golang-anti-textbook/) [![GitHub stars](https://img.shields.io/github/stars/thewhitetulip/web-dev-golang-anti-textbook/?style=flat)](https://github.com/thewhitetulip/web-dev-golang-anti-textbook//stargazers)

**[⬆ back to top](#contents)**

## Gophers

- [Free Gophers Pack](https://github.com/MariaLetta/free-gophers-pack) [![GitHub stars](https://img.shields.io/github/stars/MariaLetta/free-gophers-pack?style=flat)](https://github.com/MariaLetta/free-gophers-pack/stargazers) - Gopher graphics pack by Maria Letta with illustrations and emotional characters in vector and raster.
- [Go-gopher-Vector](https://github.com/keygx/Go-gopher-Vector) [![GitHub stars](https://img.shields.io/github/stars/keygx/Go-gopher-Vector?style=flat)](https://github.com/keygx/Go-gopher-Vector/stargazers) - Go gopher Vector Data [.ai, .svg].
- [gopher-logos](https://github.com/GolangUA/gopher-logos) [![GitHub stars](https://img.shields.io/github/stars/GolangUA/gopher-logos?style=flat)](https://github.com/GolangUA/gopher-logos/stargazers) - adorable gopher logos.
- [gopher-stickers](https://github.com/tenntenn/gopher-stickers) [![GitHub stars](https://img.shields.io/github/stars/tenntenn/gopher-stickers?style=flat)](https://github.com/tenntenn/gopher-stickers/stargazers)
- [gophericons](https://github.com/shalakhin/gophericons) [![GitHub stars](https://img.shields.io/github/stars/shalakhin/gophericons?style=flat)](https://github.com/shalakhin/gophericons/stargazers)
- [gopherize.me](https://github.com/matryer/gopherize.me) [![GitHub stars](https://img.shields.io/github/stars/matryer/gopherize.me?style=flat)](https://github.com/matryer/gopherize.me/stargazers) - Gopherize yourself.
- [gophers](https://github.com/ashleymcnamara/gophers) [![GitHub stars](https://img.shields.io/github/stars/ashleymcnamara/gophers?style=flat)](https://github.com/ashleymcnamara/gophers/stargazers) - Gopher artworks by Ashley McNamara.
- [gophers](https://github.com/egonelbre/gophers) [![GitHub stars](https://img.shields.io/github/stars/egonelbre/gophers?style=flat)](https://github.com/egonelbre/gophers/stargazers) - Free gophers.
- [gophers](https://github.com/rogeralsing/gophers) [![GitHub stars](https://img.shields.io/github/stars/rogeralsing/gophers?style=flat)](https://github.com/rogeralsing/gophers/stargazers) - random gopher graphics.
- [gophers](https://github.com/sillecelik/go-gopher) [![GitHub stars](https://img.shields.io/github/stars/sillecelik/go-gopher?style=flat)](https://github.com/sillecelik/go-gopher/stargazers) - Gopher amigurumi toy pattern.
- [gophers](https://github.com/scraly/gophers) [![GitHub stars](https://img.shields.io/github/stars/scraly/gophers?style=flat)](https://github.com/scraly/gophers/stargazers) - Gophers by Aurélie Vache.

**[⬆ back to top](#contents)**

## Meetups

- [Basel Go Meetup](https://www.meetup.com/Basel-Go-Meetup/)
- [Belfast Gophers](https://www.meetup.com/Belfast-Gophers/)
- [Belgrade Golang Meetup](https://www.meetup.com/golang-serbia/)
- [Berlin Golang](https://www.meetup.com/golang-users-berlin/)
- [Brisbane Gophers](https://www.meetup.com/Brisbane-Golang-Meetup/)
- [Bärner Go Meetup - Berne, Switzerland](https://www.meetup.com/berner-go-meetup/)
- [Go Ireland - Dublin](https://www.meetup.com/goireland/)
- [Go Language NYC](https://www.meetup.com/golanguagenewyork/)
- [Go London User Group](https://www.meetup.com/Go-London-User-Group/)
- [Go Remote Meetup](https://www.meetup.com/Go-Remote-Meetup/)
- [Go Toronto](https://www.meetup.com/go-toronto/)
- [Go User Group Atlanta](https://www.meetup.com/Go-Users-Group-Atlanta/)
- [GoBandung](https://www.meetup.com/GoBandung/)
- [GoBridge, San Francisco, CA](https://www.meetup.com/gobridge/)
- [GoCracow - Krakow, Poland](https://www.meetup.com/GoCracow/)
- [GoJakarta](https://www.meetup.com/GoJakarta/)
- [Golang Amsterdam](https://www.meetup.com/golang-amsterdam/)
- [Golang Argentina](https://www.meetup.com/Golang-Argentina/)
- [Golang Athens](https://www.meetup.com/Athens-Gophers/)
- [Golang Baltimore, MD](https://www.meetup.com/BaltimoreGolang/)
- [Golang Bangalore](https://www.meetup.com/Golang-Bangalore/)
- [Golang Belo Horizonte - Brazil](https://www.meetup.com/go-belo-horizonte/)
- [Golang Boston](https://www.meetup.com/bostongo/)
- [Golang Bulgaria](https://www.meetup.com/Golang-Bulgaria/)
- [Golang Cardiff, UK](https://www.meetup.com/Cardiff-Go-Meetup/)
- [Golang Copenhagen](https://www.meetup.com/Go-Cph/)
- [Golang Curitiba - Brazil](https://www.meetup.com/GolangCWB/)
- [Golang DC, Arlington, VA](https://www.meetup.com/Golang-DC/)
- [Golang Dorset, UK](https://www.meetup.com/golang-dorset/)
- [Golang Estonia](https://www.meetup.com/Golang-Estonia/)
- [Golang Gurgaon, India](https://www.meetup.com/Gurgaon-Go-Meetup/)
- [Golang Hamburg - Germany](https://www.meetup.com/Go-User-Group-Hamburg/)
- [Golang Israel](https://www.meetup.com/Go-Israel/)
- [Golang Kathmandu](https://www.meetup.com/Golang-Kathmandu/)
- [Golang Lima - Peru](https://www.meetup.com/Golang-Peru/)
- [Golang Lyon](https://www.meetup.com/Golang-Lyon/)
- [Golang Marseille](https://www.meetup.com/fr-FR/Golang-Marseille/)
- [Golang Melbourne](https://www.meetup.com/golang-mel/)
- [Golang Milano](https://www.meetup.com/golang-milano/)
- [Golang North East](https://www.meetup.com/en-AU/Golang-North-East/)
- [Golang Paris](https://www.meetup.com/Golang-Paris/)
- [Golang Poland](https://www.meetup.com/Golang-Poland/)
- [Golang Pune](https://www.meetup.com/Golang-Pune/)
- [Golang Roma](https://www.meetup.com/golangroma/)
- [Golang Rotterdam](https://www.meetup.com/golang-rotterdam/)
- [Golang Singapore](https://www.meetup.com/golangsg/)
- [Golang Stockholm](https://www.meetup.com/Go-Stockholm/)
- [Golang Sydney, AU](https://www.meetup.com/golang-syd/)
- [Golang São Paulo - Brazil](https://www.meetup.com/golangbr/)
- [Golang Taipei](https://www.meetup.com/golang-taipei-meetup/)
- [Golang Thessaloniki](https://www.meetup.com/thessaloniki-golang-meetup/)
- [Golang Torino](https://www.meetup.com/golang-torino/)
- [Golang Turkey](https://kommunity.com/goturkiye)
- [Golang Vancouver, BC](https://www.meetup.com/golangvan/)
- [Golang Vienna, Austria](https://www.meetup.com/viennago/)
- [Golang Москва](https://www.meetup.com/Golang-Moscow/)
- [GoSF - San Francisco, CA](https://www.meetup.com/golangsf)
- [Istanbul Golang](https://www.meetup.com/Istanbul-Golang/)
- [Lagos Gophers](https://www.meetup.com/GolangNigeria/)
- [Nairobi Gophers](https://www.meetup.com/nairobi-gophers/)
- [Seattle Go Programmers](https://www.meetup.com/golang/)
- [Ukrainian Golang User Groups](https://www.meetup.com/uagolang/)
- [Utah Go User Group](https://www.meetup.com/utahgophers/)
- [Women Who Go - San Francisco, CA](https://www.meetup.com/Women-Who-Go/)
- [Zürich Gophers - Zurich, Switzerland](https://www.meetup.com/zurich-gophers/)

_Add the group of your city/country here (send **PR**)_

**[⬆ back to top](#contents)**

## Style Guides

- [CockroachDB](https://github.com/cockroachdb/cockroach/blob/master/docs/style.md) [![GitHub stars](https://img.shields.io/github/stars/cockroachdb/cockroach/blob/master/docs/style.md?style=flat)](https://github.com/cockroachdb/cockroach/blob/master/docs/style.md/stargazers)
- [enra/go-styleguide](https://codeberg.org/enra/go-styleguide)
- [GitLab](https://docs.gitlab.com/ee/development/go_guide/)
- [Google](https://google.github.io/styleguide/go/)
- [Hyperledger](https://github.com/hyperledger/fabric/blob/release-1.4/docs/source/style-guides/go-style.rst) [![GitHub stars](https://img.shields.io/github/stars/hyperledger/fabric/blob/release-1.4/docs/source/style-guides/go-style.rst?style=flat)](https://github.com/hyperledger/fabric/blob/release-1.4/docs/source/style-guides/go-style.rst/stargazers)
- [Thanos](https://thanos.io/tip/contributing/coding-style-guide.md/)
- [Trybe](https://github.com/betrybe/playbook-go/blob/main/README_EN.md) [![GitHub stars](https://img.shields.io/github/stars/betrybe/playbook-go/blob/main/README_EN.md?style=flat)](https://github.com/betrybe/playbook-go/blob/main/README_EN.md/stargazers)
- [Uber](https://github.com/uber-go/guide/blob/master/style.md) [![GitHub stars](https://img.shields.io/github/stars/uber-go/guide/blob/master/style.md?style=flat)](https://github.com/uber-go/guide/blob/master/style.md/stargazers)

**[⬆ back to top](#contents)**

## Social Media

### Twitter

- [@GoDiscussions](https://twitter.com/GoDiscussions)
- [@golang](https://twitter.com/golang)
- [@golang_news](https://twitter.com/golang_news)
- [@golangch](https://twitter.com/golangch)
- [@golangweekly](https://twitter.com/golangweekly)

**[⬆ back to top](#contents)**

### Reddit

- [r/golang](https://www.reddit.com/r/golang/)

**[⬆ back to top](#contents)**

## Websites

- [Awesome Go @LibHunt](https://go.libhunt.com) - Your go-to Go Toolbox.
- [Awesome Golang Workshops](https://github.com/amit-davidson/awesome-golang-workshops) [![GitHub stars](https://img.shields.io/github/stars/amit-davidson/awesome-golang-workshops?style=flat)](https://github.com/amit-davidson/awesome-golang-workshops/stargazers) - A curated list of awesome golang workshops.
- [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) [![GitHub stars](https://img.shields.io/github/stars/lukasz-madon/awesome-remote-job?style=flat)](https://github.com/lukasz-madon/awesome-remote-job/stargazers) - Curated list of awesome remote jobs. A lot of them are looking for Go hackers.
- [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers) - List of other amazingly awesome lists.
- [awesome-go-extra](https://github.com/xwjdsh/awesome-go-extra) [![GitHub stars](https://img.shields.io/github/stars/xwjdsh/awesome-go-extra?style=flat)](https://github.com/xwjdsh/awesome-go-extra/stargazers) - Parse awesome-go README file and generate a new README file with repo info.
- [Code with Mukesh](https://codewithmukesh.com/categories/golang) - Software Engineer and Blogs @ codewithmukesh.com.
- [Coding Mystery](https://codingmystery.com) - Solve exciting escape-room-inspired programming challenges using Go.
- [CodinGame](https://www.codingame.com/) - Learn Go by solving interactive tasks using small games as practical examples.
- [Go Blog](https://blog.golang.org) - The official Go blog.
- [Go Code Club](https://www.youtube.com/watch?v=nvoIPQYdx9g&list=PLEcwzBXTPUE_YQR7R0BRtHBYJ0LN3Y0i3) - A group of Gophers read and discuss a different Go project every week.
- [Go Community on Hashnode](https://hashnode.com/n/go) - Community of Gophers on Hashnode.
- [Go Forum](https://forum.golangbridge.org) - Forum to discuss Go.
- [Go Projects](https://github.com/golang/go/wiki/Projects) [![GitHub stars](https://img.shields.io/github/stars/golang/go/wiki/Projects?style=flat)](https://github.com/golang/go/wiki/Projects/stargazers) - List of projects on the Go community wiki.
- [Go Proverbs](https://go-proverbs.github.io/) - Go Proverbs by Rob Pike.
- [Go Report Card](https://goreportcard.com) - A report card for your Go package.
- [go.dev](https://go.dev/) - A hub for Go developers.
- [gocryforhelp](https://github.com/ninedraft/gocryforhelp) [![GitHub stars](https://img.shields.io/github/stars/ninedraft/gocryforhelp?style=flat)](https://github.com/ninedraft/gocryforhelp/stargazers) - Collection of Go projects that needs help. Good place to start your open-source way in Go.
- [Golang Developer Jobs](https://golangjob.xyz) - Developer Jobs exclusively for Golang related Roles.
- [Golang News](https://golangnews.com) - Links and news about Go programming.
- [Golang Nugget](https://golangnugget.com) - A weekly roundup of the best Go content, delivered to your inbox every Monday.
- [Golang Weekly](https://discu.eu/weekly/golang/) - Each monday projects, tutorials and articles about Go.
- [golang-nuts](https://groups.google.com/forum/#!forum/golang-nuts) - Go mailing list.
- [Gopher Community Chat](https://invite.slack.golangbridge.org) - Join Our New Slack Community For Gophers ([Understand how it came](https://blog.gopheracademy.com/gophers-slack-community/)).
- [Gophercises](https://gophercises.com/) - Free coding exercises for budding gophers.
- [json2go](https://m-zajac.github.io/json2go) - Advanced JSON to Go struct conversion - online tool.
- [justforfunc](https://www.youtube.com/c/justforfunc) - Youtube channel dedicated to Go programming language tips and tricks, hosted by Francesc Campoy [@francesc](https://twitter.com/francesc).
- [Learn Go Programming](https://blog.learngoprogramming.com) - Learn Go concepts with illustrations.
- [Libs.tech](https://libs.tech/go) – Awesome Go libraries and hidden gems
- [Made with Golang](https://madewithgolang.com/?ref=awesome-go)
- [pkg.go.dev](https://pkg.go.dev/) - Documentation for open source Go packages.
- [studygolang](https://studygolang.com) - The community of studygolang in China.
- [Trending Go repositories on GitHub today](https://github.com/trending?l=go) [![GitHub stars](https://img.shields.io/github/stars/trending?l=go?style=flat)](https://github.com/trending?l=go/stargazers) - Good place to find new Go libraries.
- [TutorialEdge - Golang](https://tutorialedge.net/course/golang/)

**[⬆ back to top](#contents)**

### Tutorials

- [50 Shades of Go](https://golang50shades.github.io/) - Traps, Gotchas, and Common Mistakes for New Golang Devs.
- [A Comprehensive Guide to Structured Logging in Go](https://betterstack.com/community/guides/logging/logging-in-go/) - Delve deep into the world of structured logging in Go with a specific focus on recently accepted slog proposal which aims to bring high performance structured logging with levels to the standard library.
- [A Guide to Golang E-Commerce](https://snipcart.com/blog/golang-ecommerce-ponzu-cms-demo?utm_term=golang-ecommerce-ponzu-cms-demo) - Building a Golang site for e-commerce (demo included).
- [A Tour of Go](https://tour.golang.org/) - Interactive tour of Go.
- [Build a Database in 1000 lines of code](https://link.medium.com/O9YQlx89Htb) - Build a NoSQL Database From Zero in 1000 Lines of Code.
- [Build web application with Golang](https://github.com/astaxie/build-web-application-with-golang) [![GitHub stars](https://img.shields.io/github/stars/astaxie/build-web-application-with-golang?style=flat)](https://github.com/astaxie/build-web-application-with-golang/stargazers) - Golang ebook intro how to build a web app with golang.
- [Building and Testing a REST API in Go with Gorilla Mux and PostgreSQL](https://semaphoreci.com/community/tutorials/building-and-testing-a-rest-api-in-go-with-gorilla-mux-and-postgresql) - We’ll write an API with the help of the powerful Gorilla Mux.
- [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin) - Get familiar with Gin and find out how it can help you reduce boilerplate code and build a request handling pipeline.
- [Caching Slow Database Queries](https://medium.com/@rocketlaunchr.cloud/caching-slow-database-queries-1085d308a0c9) - How to cache slow database queries.
- [Canceling MySQL](https://medium.com/@rocketlaunchr.cloud/canceling-mysql-in-go-827ed8f83b30) - How to cancel MySQL queries.
- [CodeCrafters Golang Track](https://app.codecrafters.io/tracks/go) - Achieve mastery in advanced Go by building your own Redis, Docker, Git, and SQLite. Featuring goroutines, systems programming, file I/O, and more.
- [Design Patterns in Go](https://github.com/shubhamzanwar/design-patterns) [![GitHub stars](https://img.shields.io/github/stars/shubhamzanwar/design-patterns?style=flat)](https://github.com/shubhamzanwar/design-patterns/stargazers) - Collection of programming design patterns implemented in Go.
- [Games With Go](https://www.youtube.com/watch?v=9D4yH7e_ea8&list=PLDZujg-VgQlZUy1iCqBbe5faZLMkA3g2x) - A video series teaching programming and game development.
- [Go By Example](https://gobyexample.com/) - Hands-on introduction to Go using annotated example programs.
- [Go Cheat Sheet](https://github.com/a8m/go-lang-cheat-sheet) [![GitHub stars](https://img.shields.io/github/stars/a8m/go-lang-cheat-sheet?style=flat)](https://github.com/a8m/go-lang-cheat-sheet/stargazers) - Go's reference card.
- [Go database/sql tutorial](http://go-database-sql.org/) - Introduction to database/sql.
- [Go in 7 days](https://github.com/harrytran103/7_days_of_go) [![GitHub stars](https://img.shields.io/github/stars/harrytran103/7_days_of_go?style=flat)](https://github.com/harrytran103/7_days_of_go/stargazers) - Learn everything about Go in 7 days (from a Nodejs developer).
- [Go Language Tutorial](https://www.javatpoint.com/go-tutorial) - Learn Go language Tutorial.
- [Go Tutorial](https://www.tutorialspoint.com/go/index.htm) - Learn Go programming.
- [Go WebAssembly Tutorial - Building a Simple Calculator](https://tutorialedge.net/golang/go-webassembly-tutorial/)
- [go-clean-template](https://github.com/evrone/go-clean-template) [![GitHub stars](https://img.shields.io/github/stars/evrone/go-clean-template?style=flat)](https://github.com/evrone/go-clean-template/stargazers) - Clean Architecture template for Golang services.
- [go-patterns](https://github.com/tmrts/go-patterns) [![GitHub stars](https://img.shields.io/github/stars/tmrts/go-patterns?style=flat)](https://github.com/tmrts/go-patterns/stargazers) - Curated list of Go design patterns, recipes and idioms.
- [Golang for Node.js Developers](https://github.com/miguelmota/golang-for-nodejs-developers) [![GitHub stars](https://img.shields.io/github/stars/miguelmota/golang-for-nodejs-developers?style=flat)](https://github.com/miguelmota/golang-for-nodejs-developers/stargazers) - Examples of Golang compared to Node.js for learning.
- [Golang Tutorial Guide](https://www.freecodecamp.org/news/golang-tutorial-list-free-courses-learn-go-programming-language/) - A List of Free Courses to Learn the Go Programming Language.
- [golang-examples](https://github.com/SimonWaldherr/golang-examples) [![GitHub stars](https://img.shields.io/github/stars/SimonWaldherr/golang-examples?style=flat)](https://github.com/SimonWaldherr/golang-examples/stargazers) - Many examples to learn Golang.
- [Golangbot](https://golangbot.com/learn-golang-series/) - Tutorials to get started with programming in Go.
- [GopherCoding](https://gophercoding.com/) - Collection of code snippets and tutorials to help tackle every day issues.
- [GopherSnippets](https://gophersnippets.com/) - Code snippets with tests and testable examples for the Go programming language.
- [Gosamples](https://gosamples.dev/) - Collection of code snippets that let you solve everyday code problems.
- [GraphQL with Go](https://hasura.io/learn/graphql/backend-stack/languages/go/) - Learn how to create a Go GraphQL server and client with code generation. Also includes creating REST endpoints.
- [Hackr.io](https://hackr.io/tutorials/learn-golang) - Learn Go from the best online golang tutorials submitted & voted by the golang programming community.
- [Hex Monscape](https://github.com/Haraj-backend/hex-monscape) [![GitHub stars](https://img.shields.io/github/stars/Haraj-backend/hex-monscape?style=flat)](https://github.com/Haraj-backend/hex-monscape/stargazers) - Getting started guidelines in writing maintainable code using Hexagonal Architecture.
- [How to Benchmark: dbq vs sqlx vs GORM](https://medium.com/@rocketlaunchr.cloud/how-to-benchmark-dbq-vs-sqlx-vs-gorm-e814caacecb5) - Learn how to benchmark in Go. As a case-study, we will benchmark dbq, sqlx and GORM.
- [How To Deploy a Go Web Application with Docker](https://semaphoreci.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker) - Learn how to use Docker for Go development and how to build production Docker images.
- [How to Implement Role-Based Access Control (RBAC) Authorization in Golang](https://www.permit.io/blog/role-based-access-control-rbac-authorization-in-golang) - A guide to implementing Role-Based Access Control (RBAC) in Golang, including code examples, covering various methods to secure app endpoints with role-based authorization.
- [How to Use Godog for Behavior-driven Development in Go](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go) - Get started with Godog - a Behavior-driven development framework for building and testing Go applications.
- [Learn Go with 1000+ Exercises](https://github.com/inancgumus/learngo) [![GitHub stars](https://img.shields.io/github/stars/inancgumus/learngo?style=flat)](https://github.com/inancgumus/learngo/stargazers) - Learn Go with thousands of examples, exercises, and quizzes.
- [Learn Go with TDD](https://github.com/quii/learn-go-with-tests) [![GitHub stars](https://img.shields.io/github/stars/quii/learn-go-with-tests?style=flat)](https://github.com/quii/learn-go-with-tests/stargazers) - Learn Go with test-driven development.
- [Learning Go by examples](https://dev.to/aurelievache/learning-go-by-examples-introduction-448n) - Series of articles in order to learn Golang language by concrete applications as example.
- [Microservices with Go](https://www.youtube.com/playlist?list=PLmD8u-IFdreyh6EUfevBcbiuCKzFk0EW_) - Dive deep into building microservices using Go, including gRPC.
- [package main](https://www.youtube.com/packagemain) - YouTube channel about Programming in Go.
- [Programming with Google Go](https://www.coursera.org/specializations/google-golang) - Coursera Specialization to learn about Go from scratch.
- [Scaling Go Applications](https://betterstack.com/community/guides/scaling-go/) - Everything about building, deploying and scaling Go applications in production.
- [The world’s easiest introduction to WebAssembly with Golang](https://medium.com/@martinolsansky/webassembly-with-golang-is-fun-b243c0e34f02)
- [Understanding Go in a visual way](https://dev.to/aurelievache/series/26234) - Learn Go visually
- [W3basic Go Tutorials](https://www.w3basic.com/golang/) - W3Basic provides an in-depth tutorial and well-organized content to learn Golang programming.
- [Your basic Go](https://yourbasic.org/golang) - Huge collection of tutorials and how to's.

**[⬆ back to top](#contents)**

### Guided Learning

- [The Go Developer Roadmap](https://roadmap.sh/golang) - A visual roadmap that new Go developers can follow through to help them learn Go.
- [The Go Interview Practice](https://github.com/RezaSi/go-interview-practice) [![GitHub stars](https://img.shields.io/github/stars/RezaSi/go-interview-practice?style=flat)](https://github.com/RezaSi/go-interview-practice/stargazers) - A GitHub repository offering coding challenges for Go technical interview preparation.
- [The Go Learning Path](https://tutorialedge.net/paths/golang/) - A guided learning path containing a mix of free and premium resources.
- [The Go Skill Tree](https://labex.io/skilltrees/go) - A structured learning path that combines both free and premium resources.

**[⬆ back to top](#contents)**

## Contribution

We welcome contributions! Please refer to our [CONTRIBUTING.md](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go/blob/main/CONTRIBUTING.md?style=flat)](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md/stargazers) for guidelines.

## License

This project is licensed under the [MIT License](https://github.com/avelino/awesome-go/blob/main/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go/blob/main/LICENSE?style=flat)](https://github.com/avelino/awesome-go/blob/main/LICENSE/stargazers) - see the LICENSE file for details.
