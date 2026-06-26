# Common Lisp

[![GitHub stars](https://img.shields.io/github/stars/CodyReichert/awesome-cl?style=flat)](https://github.com/CodyReichert/awesome-cl/stargazers)

<div align="center">
  <a href="https://awesome-cl.com" target="_blank">
    <img src="https://raw.githubusercontent.com/CodyReichert/awesome-cl/refs/heads/master/alien.png">
  </a>
</div>

# Awesome Common Lisp [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Assertible status](https://assertible.com/apis/102e334d-f9a8-4565-9353-7572de775cae/status?api_token=8b55a286830323effb)](https://assertible.com/docs/guide/deployments)

A curated list of _awesome_ Common Lisp libraries.

All libraries listed here are available from [Quicklisp][16] unless
stated otherwise. The ones marked with a ⭐ are so widespread and
solid that they became community standards. You can't be wrong with
them. This is the case for Quicklisp, BordeauxThreads and
such. Libraries denoted with a 👍 are the ones we like and want to
promote here at the Awesome-cl list. They proved solid, they may solve
a problem better than a community standard but they aren't as
widespread, or not considered as stable. For example, we prefer
Spinneret over Cl-Who.

---

For a list of *software*, see the [lisp-screenshots.org](https://www.lisp-screenshots.org/) gallery and the
[awesome-cl-software](https://github.com/azzamsa/awesome-cl-software) [![GitHub stars](https://img.shields.io/github/stars/azzamsa/awesome-cl-software?style=flat)](https://github.com/azzamsa/awesome-cl-software/stargazers) list.

For examples of *companies* using CL in production, see [lisp-lang.org's success stories](http://lisp-lang.org/success/),
the [awesome-lisp-companies](https://github.com/azzamsa/awesome-lisp-companies/) [![GitHub stars](https://img.shields.io/github/stars/azzamsa/awesome-lisp-companies/?style=flat)](https://github.com/azzamsa/awesome-lisp-companies//stargazers) list,
but also [LispWorks' success stories](https://www.lispworks.com/success-stories/index.html)
and [Allegro's success stories](https://franz.com/success/).

---

Add something new! See the [contributing](#contributing) section for adding something to the
list.

This is released under the GNU Free Documentation License - its text
is provided in the LICENSE file. Preference is given to [free software][13] and
sellers who aren't evil for physical resources.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Artificial Intelligence (AI, LLMs)](#artificial-intelligence-ai-llms)
  - [Around the OpenAI API](#around-the-openai-api)
  - [MCP servers](#mcp-servers)
  - [Machine Learning](#machine-learning)
  - [Natural Language Processing](#natural-language-processing)
  - [Expert Systems](#expert-systems)
  - [Educational](#educational)
- [Audio](#audio)
- [Build Systems](#build-systems)
- [Compilers, code generators](#compilers-code-generators)
  - [APL](#apl)
  - [C, C++](#c-c)
- [Cryptography](#cryptography)
- [Cryptocurrencies](#cryptocurrencies)
- [Database](#database)
  - [ORMs](#orms)
  - [Persistent object databases](#persistent-object-databases)
  - [Graph databases](#graph-databases)
  - [Other DB wrappers](#other-db-wrappers)
  - [Migration tools](#migration-tools)
  - [To third parties](#to-third-parties)
  - [Tools](#tools)
- [Data Formats](#data-formats)
  - [CSV](#csv)
  - [JSON](#json)
  - [TOML](#toml)
  - [XML](#xml)
  - [YAML](#yaml)
- [Data Structures](#data-structures)
- [Docker images](#docker-images)
- [Foreign Function Interface, languages interop](#foreign-function-interface-languages-interop)
  - [C](#c)
  - [Clojure](#clojure)
  - [Erlang](#erlang)
  - [Java](#java)
  - [Objective-C](#objective-c)
  - [Python](#python)
  - [.Net Core](#net-core)
  - [Emacs Lisp](#emacs-lisp)
- [Game Development](#game-development)
- [Graphics](#graphics)
- [GUI](#gui)
  - [Web views](#web-views)
  - [Mobile](#mobile)
- [Implementations](#implementations)
- [Language libraries](#language-libraries)
  - [Lisp parsers](#lisp-parsers)
  - [Tree-sitter grammars](#tree-sitter-grammars)
- [Language extensions](#language-extensions)
  - [Pattern matching](#pattern-matching)
  - [Portability layers](#portability-layers)
  - [Changing the syntax](#changing-the-syntax)
  - [CLOS extensions](#clos-extensions)
  - [Function extensions](#function-extensions)
  - [Iteration](#iteration)
  - [Lambda shorthands](#lambda-shorthands)
  - [Non-deterministic, logic programming](#non-deterministic-logic-programming)
  - [Reactive programming](#reactive-programming)
  - [Contract programming](#contract-programming)
  - [Typing](#typing)
  - [Theorem provers](#theorem-provers)
- [Learning and Tutorials](#learning-and-tutorials)
  - [Online](#online)
  - [Beginner](#beginner)
  - [Intermediate](#intermediate)
  - [Advanced](#advanced)
  - [Coding platforms](#coding-platforms)
  - [Web Development](#web-development)
  - [Reference](#reference)
  - [Offline](#offline)
  - [Beginner](#beginner-1)
  - [Intermediate](#intermediate-1)
  - [Advanced](#advanced-1)
  - [Other books](#other-books)
  - [Community](#community)
  - [Showcase](#showcase)
- [Library Manager](#library-manager)
  - [Interfaces to other package managers](#interfaces-to-other-package-managers)
- [Network and Internet](#network-and-internet)
  - [HTTP clients](#http-clients)
  - [HTTP Servers](#http-servers)
    - [Hunchentoot plugins](#hunchentoot-plugins)
    - [Clack plugins](#clack-plugins)
  - [Web frameworks](#web-frameworks)
    - [Isomorphic web frameworks](#isomorphic-web-frameworks)
  - [Parsing html](#parsing-html)
  - [Querying HTML/DOM, web scraping](#querying-htmldom-web-scraping)
  - [HTML generators and templates](#html-generators-and-templates)
  - [URI and IP handling](#uri-and-ip-handling)
  - [Javascript](#javascript)
  - [Deployment](#deployment)
    - [Hosting platforms](#hosting-platforms)
  - [Monitoring](#monitoring)
  - [Websockets](#websockets)
  - [HTTPS](#https)
  - [Web development utilities](#web-development-utilities)
    - [Browser tests](#browser-tests)
    - [Form handling](#form-handling)
    - [User login and password management](#user-login-and-password-management)
    - [Web project skeletons and generators](#web-project-skeletons-and-generators)
  - [Others](#others)
    - [Email](#email)
    - [OpenAPI, OData, OpenRPC](#openapi-odata-openrpc)
    - [Static site generators](#static-site-generators)
    - [Third-party APIs](#third-party-apis)
- [Numerical and Scientific](#numerical-and-scientific)
  - [Matrix libraries](#matrix-libraries)
  - [Statistics](#statistics)
  - [Units](#units)
  - [Plotting](#plotting)
  - [Utils](#utils)
- [Parallelism and Concurrency](#parallelism-and-concurrency)
  - [Actors pattern](#actors-pattern)
  - [Event processing](#event-processing)
  - [Job processing](#job-processing)
- [Regular expressions and string parsing](#regular-expressions-and-string-parsing)
- [Scripting](#scripting)
  - [Running scripts](#running-scripts)
  - [Command-line options parsers](#command-line-options-parsers)
  - [Readline, ncurses and other graphical TUI helpers](#readline-ncurses-and-other-graphical-tui-helpers)
  - [Shells, shells interfaces](#shells-shells-interfaces)
  - [System administration](#system-administration)
  - [Updating executables](#updating-executables)
  - [Other scripting utilities](#other-scripting-utilities)
- [Text Editor Resources](#text-editor-resources)
  - [Emacs](#emacs)
  - [Vim & Neovim](#vim--neovim)
  - [Eclipse](#eclipse)
  - [Lem](#lem)
  - [LispWorks](#lispworks)
  - [Mine - single-download beginner friendly IDE for Common Lisp and Coalton](#mine---single-download-beginner-friendly-ide-for-common-lisp-and-coalton)
  - [Atom, Pulsar](#atom-pulsar)
  - [Sublime Text](#sublime-text)
  - [VSCode](#vscode)
  - [JetBrains](#jetbrains)
  - [Geany (experimental)](#geany-experimental)
  - [Notebooks](#notebooks)
  - [REPLs](#repls)
  - [Online editors](#online-editors)
- [Text and binary parsers](#text-and-binary-parsers)
- [Text Processing](#text-processing)
- [Tools](#tools-1)
- [Unit Testing](#unit-testing)
- [Utilities](#utilities)
  - [Caching (serialization)](#caching-serialization)
  - [Caching (memoization)](#caching-memoization)
  - [Compression / decompression](#compression--decompression)
  - [Configuration](#configuration)
  - [Date and time](#date-and-time)
  - [Data validation](#data-validation)
  - [Developer utilities](#developer-utilities)
  - [Documentation builders](#documentation-builders)
  - [Documentation lookup](#documentation-lookup)
  - [Files and directories](#files-and-directories)
  - [Git](#git)
  - [i18n](#i18n)
  - [Linting, code formatting](#linting-code-formatting)
  - [Literate programming](#literate-programming)
  - [Logging](#logging)
  - [Macro helpers](#macro-helpers)
  - [Markdown](#markdown)
  - [Package declarations](#package-declarations)
  - [PDF](#pdf)
  - [Project skeletons](#project-skeletons)
  - [Security](#security)
  - [System interface](#system-interface)
  - [Other](#other)
- [Contributing](#contributing)

<!-- markdown-toc end -->

Artificial Intelligence (AI, LLMs)
==================================

## Around the OpenAI API

* [openai-openapi-client](https://codeberg.org/kilianmh/openai-openapi-client) - semi-automatically generated Openapi client updated frequently from the [official Openapi specification](https://github.com/openai/openai-openapi/blob/master/openapi.yaml) [![GitHub stars](https://img.shields.io/github/stars/openai/openai-openapi/blob/master/openapi.yaml?style=flat)](https://github.com/openai/openai-openapi/blob/master/openapi.yaml/stargazers). AGPL-3.
  * available on Ultralisp.
* [cl-completions](https://github.com/atgreen/cl-completions) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-completions?style=flat)](https://github.com/atgreen/cl-completions/stargazers) - LLM completions.
  * makes it easy to create GPT functions in Common Lisp.
  * Ollama support.
* [cl-embeddings](https://github.com/atgreen/cl-embeddings) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-embeddings?style=flat)](https://github.com/atgreen/cl-embeddings/stargazers) - LLM embeddings.
* [cl-chroma](https://github.com/atgreen/cl-chroma) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-chroma?style=flat)](https://github.com/atgreen/cl-chroma/stargazers) - the vector DB interface.

demos: [cl-rag-example](https://github.com/atgreen/cl-rag-example) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-rag-example?style=flat)](https://github.com/atgreen/cl-rag-example/stargazers) and [cl-chat](https://github.com/atgreen/cl-chat) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-chat?style=flat)](https://github.com/atgreen/cl-chat/stargazers), a LLM chat library and web UI.

Work In Progress:

* [Caten](https://github.com/hikettei/Caten) [![GitHub stars](https://img.shields.io/github/stars/hikettei/Caten?style=flat)](https://github.com/hikettei/Caten/stargazers) -  Deep Learning Compiler based on Polyhedral Compiler and Light-weight IRs, and Optimizing Pattern Matcher, written in Common Lisp

## MCP servers

* [cl-MCP](https://github.com/cl-ai-project/cl-mcp) [![GitHub stars](https://img.shields.io/github/stars/cl-ai-project/cl-mcp?style=flat)](https://github.com/cl-ai-project/cl-mcp/stargazers) - MCP for Common Lisp.
  * provides a newline‑delimited JSON‑RPC 2.0 transport over stdio or TCP, a small protocol layer (initialize, ping, tools/list, tools/call), and a REPL tool that evaluates forms and returns the last value.
* [40ants-MCP](https://github.com/40ants/mcp) [![GitHub stars](https://img.shields.io/github/stars/40ants/mcp?style=flat)](https://github.com/40ants/mcp/stargazers) - a framework for building Model Context Protocol servers in Common Lisp.
* [mcp-lisp](https://github.com/jsulmont/mcp-lisp) [![GitHub stars](https://img.shields.io/github/stars/jsulmont/mcp-lisp?style=flat)](https://github.com/jsulmont/mcp-lisp/stargazers) - Common Lisp SDK for MCP (2025-11-25) with full conformance (44/44 checks) and limited A2A support. Supports stdio and SSE transports, tools, resources, prompts, structured errors, and access logging. [MIT][200].
* [Lisply MCP](https://github.com/gornskew/lisply-mcp) [![GitHub stars](https://img.shields.io/github/stars/gornskew/lisply-mcp?style=flat)](https://github.com/gornskew/lisply-mcp/stargazers) - a generic Node.js wrapper meant to work with pretty much any language backend which can support "eval" and http .
  * By default, it comes configured to work with an existing reference-implementation backend CL-based container image which it will pull and run on-demand.
* [cl-tron-mcp](https://github.com/Alba-Intelligence/cl-tron-mcp) [![GitHub stars](https://img.shields.io/github/stars/Alba-Intelligence/cl-tron-mcp?style=flat)](https://github.com/Alba-Intelligence/cl-tron-mcp/stargazers) - MCP wrap around the Slime Swank library. Provides discoverable access to Swank commands, including control of the Swank debugging sessions and code hot-reload. Currently 90+ tools. Tested on SBCL and ECL.

## Machine Learning

* [MGL](https://github.com/melisgl/mgl) [![GitHub stars](https://img.shields.io/github/stars/melisgl/mgl?style=flat)](https://github.com/melisgl/mgl/stargazers) - a machine learning library for backpropagation neural networks, boltzmann machines, gaussian processes and more. [MIT][200].
  * some parts originally contributed by Ravenpack International.
  * used by its [author](https://github.com/melisgl) [![GitHub stars](https://img.shields.io/github/stars/melisgl?style=flat)](https://github.com/melisgl/stargazers) to [win](https://github.com/melisgl/higgsml) [![GitHub stars](https://img.shields.io/github/stars/melisgl/higgsml?style=flat)](https://github.com/melisgl/higgsml/stargazers) the Higgs Boson Machine Learning Challenge.
  * more about the author: he also won the Google [AI Challenge](https://en.wikipedia.org/wiki/AI_Challenge) in 2010 using Common Lisp, but without MGL, as no machine learning was needed. A [related talk](https://www.youtube.com/watch?v=7sgERtZkycU) (59', 2013).
* [clml](https://github.com/mmaul/clml) [![GitHub stars](https://img.shields.io/github/stars/mmaul/clml?style=flat)](https://github.com/mmaul/clml/stargazers) - originally developed by Mathematicl Systems Inc., a Japanese company. With a [tutorial](https://mmaul.github.io/clml.tutorials//2015/08/08/CLML-Time-Series-Part-1.html). [LLGPL][8].
* [antik](https://www.common-lisp.net/project/antik/) -  a foundation for scientific and engineering computation in Common Lisp. GPL. Also [mgl-mat](https://github.com/melisgl/mgl-mat) [![GitHub stars](https://img.shields.io/github/stars/melisgl/mgl-mat?style=flat)](https://github.com/melisgl/mgl-mat/stargazers) and [LLA](https://github.com/tpapp/lla) [![GitHub stars](https://img.shields.io/github/stars/tpapp/lla?style=flat)](https://github.com/tpapp/lla/stargazers).

Credit: borretti.me's [State of CL Ecosystem 2015](http://borretti.me/article/common-lisp-sotu-2015#machine-learning).

* [llama.cl](https://github.com/snunez1/llama.cl) [![GitHub stars](https://img.shields.io/github/stars/snunez1/llama.cl?style=flat)](https://github.com/snunez1/llama.cl/stargazers) - implementation of Llama inference operations. MIT.
    * "Enables researchers and developers to explore LLM techniques within the Common Lisp ecosystem, leveraging the language's capabilities for interactive development and integration with symbolic AI systems."

## Natural Language Processing

* 🚀 [sparser](https://github.com/ddmcdonald/sparser) [![GitHub stars](https://img.shields.io/github/stars/ddmcdonald/sparser?style=flat)](https://github.com/ddmcdonald/sparser/stargazers) - A natural language understanding system for English. [Eclipse][209].
  * > a model-driven, rule-based language text analysis system for large volume, high-precision information extraction. At its heart, Sparser is a bottom-up, phrase-structure-based chart parser, optimized for semantic grammars and partial parsing.
* [cl-nlp](https://github.com/vseloved/cl-nlp) [![GitHub stars](https://img.shields.io/github/stars/vseloved/cl-nlp?style=flat)](https://github.com/vseloved/cl-nlp/stargazers) - Natural language processing toolset. [Apache2.0][89].
* [babel2](https://github.com/lucas8/Babel2/) [![GitHub stars](https://img.shields.io/github/stars/lucas8/Babel2/?style=flat)](https://github.com/lucas8/Babel2//stargazers) - A Fluid Construction Grammar implementation, computational framework, and unification-based grammar formalism [Apache2.0][89].

## Expert Systems

* [Lisa](https://github.com/youngde811/Lisa) [![GitHub stars](https://img.shields.io/github/stars/youngde811/Lisa?style=flat)](https://github.com/youngde811/Lisa/stargazers) - a production-quality, forward-chaining expert system shell featuring an optimized implementation of Charles Forgy's Rete algorithm, a highly efficient solution to the difficult many-to-many pattern matching problem. MIT.
* [WouldWork](https://github.com/davypough/wouldwork) [![GitHub stars](https://img.shields.io/github/stars/davypough/wouldwork?style=flat)](https://github.com/davypough/wouldwork/stargazers) - solve classical planning and constraint satisfaction problems without extensive programming experience. BSD_3Clause.

## Educational

* [PAIP-lisp](https://github.com/norvig/paip-lisp) [![GitHub stars](https://img.shields.io/github/stars/norvig/paip-lisp?style=flat)](https://github.com/norvig/paip-lisp/stargazers) - Lisp code for the textbook ["Paradigms of Artificial Intelligence Programming"](https://norvig.github.io/paip-lisp/#/).
* [AIMA-lisp](https://github.com/aimacode/aima-lisp) [![GitHub stars](https://img.shields.io/github/stars/aimacode/aima-lisp?style=flat)](https://github.com/aimacode/aima-lisp/stargazers) -  Common Lisp implementation of algorithms from Russell and Norvig's "Artificial Intelligence - A Modern Approach".
* the book [Reinforcement Learning: An Introduction](http://www.incompleteideas.net/book/the-book.html), by Richard S. Sutton and Andrew G. Barto, with code in Lisp.
  * the authors are the recipients of the [2024 ACM A.M. Turing Award](https://awards.acm.org/about/2024-turing) for developing the conceptual and algorithmic foundations of reinforcement learning.
* [microgpt](https://github.com/40ants/microgpt) [![GitHub stars](https://img.shields.io/github/stars/40ants/microgpt?style=flat)](https://github.com/40ants/microgpt/stargazers) - A Common Lisp port of @karpathy microgpt.py — the most atomicimplementation of a GPT with a hand-written scalar autograd engine.


Audio
=====

Music composition:

* [OpenMusic](https://github.com/openmusic-project/openmusic/) [![GitHub stars](https://img.shields.io/github/stars/openmusic-project/openmusic/?style=flat)](https://github.com/openmusic-project/openmusic//stargazers) visual programming / computer-aided composition environment. [GPL3][2]. Developped at [IRCAM](https://www.stms-lab.fr/team/representations-musicales/), France.
* [OM7](https://github.com/openmusic-project/om7) [![GitHub stars](https://img.shields.io/github/stars/openmusic-project/om7?style=flat)](https://github.com/openmusic-project/om7/stargazers) - a new implementation of the OpenMusic visual programming and computer-aided composition environment including a number of improvements on graphical interface, computational mode, and connection to external software libraries. [GPL3][2].
  * an extension: [rq](https://github.com/openmusic-project/RQ) [![GitHub stars](https://img.shields.io/github/stars/openmusic-project/RQ?style=flat)](https://github.com/openmusic-project/RQ/stargazers) - a library for rhythm transcription in OpenMusic (version 6.10 and later). [demo video](https://www.youtube.com/watch?v=XVEllB0TtVs). [GPL3][2].
* [Incudine](http://incudine.sourceforge.net/) -  Music/DSP programming environment for Common Lisp. Useful to design software synthesizers or sound plugins from scratch. It is also a compositional tool that allows to produce high quality sounds controllable at the sample level, defining and redefining the digital signal processors and the musical structures on-the-fly.
* [CLM](https://ccrma.stanford.edu/software/clm/) - Common Lisp Music is a music synthesis and signal processing package in the Music V family. It provides much the same functionality as Stk, Csound, SuperCollider, PD, CMix, cmusic, and Arctic — a collection of functions that create and manipulate sounds, aimed primarily at composers (in CLM's case anyway).
  * [common-tones](https://github.com/theraphonics/common-tones) [![GitHub stars](https://img.shields.io/github/stars/theraphonics/common-tones?style=flat)](https://github.com/theraphonics/common-tones/stargazers) - a fork of CLM5 with modern Lisp (ASDF, cffi…). [BSD_3Clause][15].
* [Slippery Chicken](https://github.com/mdedwards/slippery-chicken/) [![GitHub stars](https://img.shields.io/github/stars/mdedwards/slippery-chicken/?style=flat)](https://github.com/mdedwards/slippery-chicken//stargazers) - Algorithmic composition library which outputs Midi, Common Music Notation, pdf-score via Lilypond and sound via Common Lisp Music. [GPL3][2].
  * with documentation: https://michael-edwards.org/sc/
* [Common Music](https://github.com/ormf/cm) [![GitHub stars](https://img.shields.io/github/stars/ormf/cm?style=flat)](https://github.com/ormf/cm/stargazers) - the repository of an
  ancient version of Common Music (version 2.12.0), the presumably
  last version which ran on Common Lisp dating from around 2007-09,
  before work on Common Music shifted to (scheme-based) cm3.
  * note: old project but working.
  * [cm-incudine](https://github.com/ormf/cm-incudine) [![GitHub stars](https://img.shields.io/github/stars/ormf/cm-incudine?style=flat)](https://github.com/ormf/cm-incudine/stargazers) - extends Common Music 2 with realtime capabilities. GPL2.
* [cl-patterns](https://github.com/defaultxr/cl-patterns) [![GitHub stars](https://img.shields.io/github/stars/defaultxr/cl-patterns?style=flat)](https://github.com/defaultxr/cl-patterns/stargazers) - a system for composing music via Lisp code, heavily inspired by SuperCollider’s patterns system, with aims to implement much of it, but in a more robust, expressive, consistent, reflective, and lispy way. Audio output through SuperCollider, with preliminary support for Incudine, and MIDI through ALSA.
* [Music](https://github.com/MegaLoler/Music) [![GitHub stars](https://img.shields.io/github/stars/MegaLoler/Music?style=flat)](https://github.com/MegaLoler/Music/stargazers) - A framework for musical expression in Lisp with a focus on music theory (built from scratch, unrelated to Common Music).

Decoders, sound processing:

* [Harmony](https://shirakumo.github.io/harmony) - A real-time sound processing and playback system. [zlib][33].
  * "provides you with audio processing tools as well as an audio server to play back music, sfx, and so forth."
  * using [cl-mixed](https://github.com/Shirakumo/cl-mixed) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-mixed?style=flat)](https://github.com/Shirakumo/cl-mixed/stargazers) for the mixing and sound processing library.
* [easy-audio](https://github.com/shamazmazum/easy-audio) [![GitHub stars](https://img.shields.io/github/stars/shamazmazum/easy-audio?style=flat)](https://github.com/shamazmazum/easy-audio/stargazers) - a collection of audio decoders and metadata readers.

others:

* [scheduler](https://github.com/byulparan/scheduler) [![GitHub stars](https://img.shields.io/github/stars/byulparan/scheduler?style=flat)](https://github.com/byulparan/scheduler/stargazers) - The time based musical event scheduler for Common Lisp. [Apache2.0][89].
* [Common Music Notation](https://ccrma.stanford.edu/software/cmn/) - Common Music Notation (CMN) provides a package of functions to hierarchically describe a musical score. Public domain.
* [osc](https://github.com/zzkt/osc) [![GitHub stars](https://img.shields.io/github/stars/zzkt/osc?style=flat)](https://github.com/zzkt/osc/stargazers) - an implementation of the Open Sound Protocol. [LGPL2.1][11].

bindings and clients to other software and libraries:

* [cl-mpg123](https://github.com/Shirakumo/cl-mpg123) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-mpg123?style=flat)](https://github.com/Shirakumo/cl-mpg123/stargazers), [cl-opus](https://github.com/Shirakumo/cl-opus) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-opus?style=flat)](https://github.com/Shirakumo/cl-opus/stargazers) (OGG/Opus), [cl-vorbis](https://github.com/Shirakumo/cl-vorbis) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-vorbis?style=flat)](https://github.com/Shirakumo/cl-vorbis/stargazers) (OGG/Vorbis), [cl-SoLoud](https://github.com/Shirakumo/cl-soloud) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-soloud?style=flat)](https://github.com/Shirakumo/cl-soloud/stargazers), [cl-out123](https://github.com/Shirakumo/cl-out123) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-out123?style=flat)](https://github.com/Shirakumo/cl-out123/stargazers) (libout123), [cl-flac](https://github.com/Shirakumo/cl-flac) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/cl-flac?style=flat)](https://github.com/Shirakumo/cl-flac/stargazers)
* [csound](https://github.com/csound/csound) [![GitHub stars](https://img.shields.io/github/stars/csound/csound?style=flat)](https://github.com/csound/csound/stargazers) - A sound and music computing system. Includes CFFI and FFI interfaces for Common Lisp.
* [cl-collider](https://github.com/byulparan/cl-collider) [![GitHub stars](https://img.shields.io/github/stars/byulparan/cl-collider?style=flat)](https://github.com/byulparan/cl-collider/stargazers) - A [SuperCollider](http://supercollider.github.io/) client for CommonLisp. With a [tutorial](https://github.com/defaultxr/cl-collider-tutorial) [![GitHub stars](https://img.shields.io/github/stars/defaultxr/cl-collider-tutorial?style=flat)](https://github.com/defaultxr/cl-collider-tutorial/stargazers) and [live coding demos](https://www.youtube.com/watch?v=xzTH_ZqaFKI). Public domain.
* [cl-openal](https://github.com/zkat/cl-openal) [![GitHub stars](https://img.shields.io/github/stars/zkat/cl-openal?style=flat)](https://github.com/zkat/cl-openal/stargazers) - bindings for the OpenAL audio library. Public domain.

and more audio software targetting musicians on [awesome-cl-software#audio](https://github.com/CodyReichert/awesome-cl#audio) (Opus Modus, OpenMusic…).



Build Systems
=============

* ⭐[ASDF](https://common-lisp.net/project/asdf/) - Another System Definition Facility; a build system for Common Lisp. [Expat][14]. Quicklisp (see [library manager](#library-manager)) uses ASDF under the hood.
  * [known ASDF extensions](https://common-lisp.net/project/asdf/#extensions), such as `asdf-system-connections`, that lets you specify systems that are automatically loaded when two other systems are loaded, to connect them.
* [asdf-viz](https://github.com/guicho271828/asdf-viz) [![GitHub stars](https://img.shields.io/github/stars/guicho271828/asdf-viz?style=flat)](https://github.com/guicho271828/asdf-viz/stargazers) - a tool to visualize the library dependencies of ASDF systems, the call graph of a function and the class inheritances. [LLGPL][8].


See also:

* [modularize](https://codeberg.org/shinmera/modularize) -  A modularization framework for Common Lisp. [zlib][33].
  * provides a common interface to segregate major application components.
  * for instance, by adding module definition options you can introduce mechanisms to tie modules together in functionality, hook into each other and so on.
  * acts as a wrapper around `defpackage` and integrates into ASDF.
* [asdf-linguist](https://github.com/eudoxia0/asdf-linguist) [![GitHub stars](https://img.shields.io/github/stars/eudoxia0/asdf-linguist?style=flat)](https://github.com/eudoxia0/asdf-linguist/stargazers) - Extensions for ASDF for compiling various languages and running various preprocessing tools on files in your project. [Expat][14].
  * Sass, LESS, Myth, C, C++, Fortran, CSS/JS minifiers, ParensScript, Make, CMake, org-mode, pandoc, dot, diita…
  * currently archived and unmaintained.
* [asdf-dependency-traverser](https://codeberg.org/johnlorentzson/asdf-dependency-traverser/) - a small utility for traversing the dependency tree of an ASDF system. Zlib.


Compilers, code generators
==========================

APL
---

* [April](https://github.com/phantomics/april) [![GitHub stars](https://img.shields.io/github/stars/phantomics/april?style=flat)](https://github.com/phantomics/april/stargazers) - The APL programming language (a subset thereof) compiling to Common Lisp. Replace hundreds of lines of number-crunching code with a single line of APL. [Apache2][89].


C, C++
------

* [C-mera](https://github.com/kiselgra/c-mera) [![GitHub stars](https://img.shields.io/github/stars/kiselgra/c-mera?style=flat)](https://github.com/kiselgra/c-mera/stargazers) - a source-to-source compiler that utilizes Lisp's macro system for meta programming of C-like languages. [GPL3][2].
* [lispc](https://github.com/eratosthenesia/lispc) [![GitHub stars](https://img.shields.io/github/stars/eratosthenesia/lispc?style=flat)](https://github.com/eratosthenesia/lispc/stargazers) - a powerful "lispsy" macrolanguage for C. [MIT][200].
* [with-c-syntax](https://github.com/y2q-actionman/with-c-syntax) [![GitHub stars](https://img.shields.io/github/stars/y2q-actionman/with-c-syntax?style=flat)](https://github.com/y2q-actionman/with-c-syntax/stargazers) - a fun package which introduces the C language syntax into Common Lisp. (Yes, this package is not for practical coding, I think.) WTFPL Licence.
* [ecrepl](https://gitlab.common-lisp.net/ecl/ecrepl) - an interactive REPL for the C language. [BSD_2Clause][17].
* [Software-Evolution-Library](https://github.com/GrammaTech/sel) [![GitHub stars](https://img.shields.io/github/stars/GrammaTech/sel?style=flat)](https://github.com/GrammaTech/sel/stargazers) - The SEL enables the programmatic modification and evaluation of software (C/C++ support using Clang, compiled assembler, and linked ELF binaries). [GPL3][2].
* [vacietis](https://github.com/vsedach/Vacietis) [![GitHub stars](https://img.shields.io/github/stars/vsedach/Vacietis?style=flat)](https://github.com/vsedach/Vacietis/stargazers) -  C to Common Lisp compiler. [LGPL3][9].
* NEW as of 2025 [Cicili](https://github.com/saman-pasha/cicili/) [![GitHub stars](https://img.shields.io/github/stars/saman-pasha/cicili/?style=flat)](https://github.com/saman-pasha/cicili//stargazers) - C generator macro-driven language. GPL3.0.
  * "can use lisp libraries to produce compile time content like html, json, sql, ... for inside C generated code".

Cryptography
============

* ⭐ [Ironclad](https://github.com/sharplispers/ironclad) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/ironclad?style=flat)](https://github.com/sharplispers/ironclad/stargazers) - A library of crypto functions for Common Lisp. Not considered secure, but is still useful for the message digest functions. [Expat][14].
* [crypto-shortcuts](https://codeberg.org/shinmera/crypto-shortcuts) - Collection of common crypto shortcuts. [zlib][33].
* [cl-ssh-keys](https://github.com/dnaeon/cl-ssh-keys) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/cl-ssh-keys?style=flat)](https://github.com/dnaeon/cl-ssh-keys/stargazers) - Common Lisp system for generating and parsing of OpenSSH keys. [BSD_3Clause][15].
* [cl-bcrypt](https://github.com/dnaeon/cl-bcrypt) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/cl-bcrypt?style=flat)](https://github.com/dnaeon/cl-bcrypt/stargazers) - Common Lisp system for parsing and generating bcrypt password hashes. [BSD_3Clause][15].
* [gpgme](https://www.gnupg.org/download/index.en.html#gpgme) (GnuPG Made Easy) is the standard library to access GnuPG functions from programming languages. It provides an official Common Lisp system.
  * [gpgme lisp sources](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpgme.git;a=tree;f=lang/cl;h=05151bdf839e513f534a1b423d59332a2e46fd5d;hb=HEAD) (not in Quicklisp). GPL2.
* [cl-frugal-uuid](https://github.com/ak-coram/cl-frugal-uuid/) [![GitHub stars](https://img.shields.io/github/stars/ak-coram/cl-frugal-uuid/?style=flat)](https://github.com/ak-coram/cl-frugal-uuid//stargazers) -  Common Lisp UUID library with zero dependencies. [MIT][200].

Cryptocurrencies
================

* [bitcoin-core-rpc](https://codeberg.org/kilianmh/bitcoin-core-rpc/) - a (hopefully) complete Bitcoin Core RPC client. [AGPL-3.0+][agpl3]
* [bp](https://github.com/rodentrabies/bp) [![GitHub stars](https://img.shields.io/github/stars/rodentrabies/bp?style=flat)](https://github.com/rodentrabies/bp/stargazers) - Bitcoin Protocol components in Common Lisp. [MIT][200].
* [peercoin-blockchain-parser](https://github.com/glv2/peercoin-blockchain-parser) [![GitHub stars](https://img.shields.io/github/stars/glv2/peercoin-blockchain-parser?style=flat)](https://github.com/glv2/peercoin-blockchain-parser/stargazers) - parse the blockchain contained in a file and export some of its data to a text file, a SQL script or a database. It can also create a database using the RPC of a Peercoin daemon as source of data instead of a blockchain file. LGPL3. Not in Quicklisp.
* [peercoin-calculator](https://github.com/glv2/peercoin-calculator) [![GitHub stars](https://img.shields.io/github/stars/glv2/peercoin-calculator?style=flat)](https://github.com/glv2/peercoin-calculator/stargazers) - This program gives you the probability of generating a POS or POW block within 10 minutes, 24 hours, 31 days, 90 days and 1 year, as well as the reward that can be expected. GUI in Qt. [GPL3][2]. Not in Quicklisp.
* [peercoin-vote](https://github.com/glv2/peercoin-vote) [![GitHub stars](https://img.shields.io/github/stars/glv2/peercoin-vote?style=flat)](https://github.com/glv2/peercoin-vote/stargazers) -  A voting system based on data from the blockchain (addresses and balances). [GPL3][2]. Not in Quicklisp.
* [stacks-api](https://github.com/kilianmh/stacks-api) [![GitHub stars](https://img.shields.io/github/stars/kilianmh/stacks-api?style=flat)](https://github.com/kilianmh/stacks-api/stargazers) - a Stacks API client. [AGPL-3.0][89]

See also [legochain](https://github.com/defunkydrummer/legochain) [![GitHub stars](https://img.shields.io/github/stars/defunkydrummer/legochain?style=flat)](https://github.com/defunkydrummer/legochain/stargazers), a simple educational blockchain; [emotiq](https://github.com/emotiq/emotiq) [![GitHub stars](https://img.shields.io/github/stars/emotiq/emotiq?style=flat)](https://github.com/emotiq/emotiq/stargazers), a next-generation blockchain with an innovative natural-language approach to smart contracts built in Common Lisp (stopped).

Database
========

* ⭐ [postmodern](http://marijnhaverbeke.nl/postmodern/) - A library for interacting with PostgreSQL. [zlib][33].
* [cl-dbi](https://github.com/fukamachi/cl-dbi) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/cl-dbi?style=flat)](https://github.com/fukamachi/cl-dbi/stargazers) - A database-independent interface for Common Lisp. [LLGPL][8].
* [sxql](https://github.com/fukamachi/sxql) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/sxql?style=flat)](https://github.com/fukamachi/sxql/stargazers) - A DSL for generating SQL. [3-clause BSD][15].
  * NEW as of Oct, 2025: a [composable query builder](https://github.com/fukamachi/sxql/blob/master/COMPOSER.md) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/sxql/blob/master/COMPOSER.md?style=flat)](https://github.com/fukamachi/sxql/blob/master/COMPOSER.md/stargazers). Queries become first-class values that can be derived, combined, and reused without side effects.
* [cl-sqlite](https://github.com/dmitryvk/cl-sqlite) [![GitHub stars](https://img.shields.io/github/stars/dmitryvk/cl-sqlite?style=flat)](https://github.com/dmitryvk/cl-sqlite/stargazers) - Bindings for SQLite. Public domain.
* [cl-yesql](https://github.com/ruricolist/cl-yesql) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/cl-yesql?style=flat)](https://github.com/ruricolist/cl-yesql/stargazers) - SQL statements live in their own files, in SQL syntax, and are imported into Lisp as functions. You are not limited to the features a DSL supports. Based on Clojure's Yesql. [MIT][200].

See also:

* [endatabas](https://github.com/endatabas/endb) [![GitHub stars](https://img.shields.io/github/stars/endatabas/endb?style=flat)](https://github.com/endatabas/endb/stargazers) - Schemaless SQL document database with full history. [AGPL-3.0][89].
  - built in Common Lisp and Rust, in development.

ORMs
----

* 👍 [mito](https://github.com/fukamachi/mito) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/mito?style=flat)](https://github.com/fukamachi/mito/stargazers) - An ORM for Common Lisp with migrations, relationships and PostgreSQL support [BSD_3Clause][15].
  * [mitho-auth](https://github.com/fukamachi/mito-auth) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/mito-auth?style=flat)](https://github.com/fukamachi/mito-auth/stargazers), a mixin class for use authorization
  * [mito-attachment](https://github.com/fukamachi/mito-attachment) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/mito-attachment?style=flat)](https://github.com/fukamachi/mito-attachment/stargazers), a mixin class for file management outside of RDBMS.
  * works best coupled with SxQL and its Query Composer.
* [clsql](http://www.cliki.net/CLSQL) - An SQL database with a Common Lisp interface. [LLGPL][8].
  * [dbd-oracle](https://github.com/sergadin/dbd-oracle) [![GitHub stars](https://img.shields.io/github/stars/sergadin/dbd-oracle?style=flat)](https://github.com/sergadin/dbd-oracle/stargazers) - an Oracle database driver for CL-DBI. [LLGPL][8].
* [datafly](https://github.com/fukamachi/datafly) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/datafly?style=flat)](https://github.com/fukamachi/datafly/stargazers) - A lightweight database library. [3-clause BSD][15].

Persistent object databases
---------------------------

* bknr.datastore - a CLOS-based lisp-only database in RAM with transaction logging persistence. [Manual](https://www.common-lisp.net/project/bknr/html/documentation.html). [licence][208].
  * active and significant fork: [tdrhk/bknr-datastore](https://github.com/tdrhq/bknr-datastore) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/bknr-datastore?style=flat)](https://github.com/tdrhq/bknr-datastore/stargazers)
  * [original repository](https://github.com/hanshuebner/bknr-datastore) [![GitHub stars](https://img.shields.io/github/stars/hanshuebner/bknr-datastore?style=flat)](https://github.com/hanshuebner/bknr-datastore/stargazers)
  * see also this [good introductory blog post](https://ashok-khanna.medium.com/persistent-in-memory-data-storage-in-common-lisp-b-k-n-r-37f8ae76042f)
  * an example web application using bknr.datastore: [screenshotbot-oss](https://github.com/screenshotbot/screenshotbot-oss) [![GitHub stars](https://img.shields.io/github/stars/screenshotbot/screenshotbot-oss?style=flat)](https://github.com/screenshotbot/screenshotbot-oss/stargazers).
  * See also [bknr.cluster](https://github.com/tdrhq/bknr.cluster) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/bknr.cluster?style=flat)](https://github.com/tdrhq/bknr.cluster/stargazers), if you want a highly-available replicated version of bknr.datastore. [blog post](https://screenshotbot.io/blog/building-a-highly-available-web-service-without-a-database).
* [ubiquitous](https://codeberg.org/shinmera/ubiquitous) - A library providing easy-to-use persistent configuration storage. [zlib][33].
* [cl-prevalence](https://common-lisp.net/project/cl-prevalence/) - in-memory database system. Implementation of Object Prevalence, in which business objects are kept live in memory and transactions are journaled for system recovery. [github fork](https://github.com/40ants/cl-prevalence) [![GitHub stars](https://img.shields.io/github/stars/40ants/cl-prevalence?style=flat)](https://github.com/40ants/cl-prevalence/stargazers). [LLGPL][8].
  * See also [cl-prevalence-multimaster](https://github.com/40ants/cl-prevalence-multimaster) [![GitHub stars](https://img.shields.io/github/stars/40ants/cl-prevalence-multimaster?style=flat)](https://github.com/40ants/cl-prevalence-multimaster/stargazers), to syncronize multiple cl-prevalence systems state.

See also the [Caching (serialization)](#caching-serialization) section.

Graph databases
---------------

* [AllegroGraph](https://allegrograph.com/) - a high-performance, multi-model (document and graph), entity-event knowledge graph technology.
  * Proprietary, with a free version of a limit of 5 million RDF triples.
  * with a [hosted version](https://allegrograph.cloud/)
  * AllegroGraph 8.0 - "incorporates Large Language Model (LLM) components directly into SPARQL along with vector generation and vector storage for a comprehensive AI Knowledge Graph solution."
* [cl-agraph](https://github.com/vseloved/cl-agraph) [![GitHub stars](https://img.shields.io/github/stars/vseloved/cl-agraph?style=flat)](https://github.com/vseloved/cl-agraph/stargazers), a minimal client for AllegroGraph.
* [neo4cl](https://codeberg.org/Equill/neo4cl) - a library for interacting with Neo4J. Sends Cypher queries to a Neo4J server, and decodes the responses into something useful for processing in CL. [Apache2][89].
  * and maybe: [cl-neo4j](https://github.com/kraison/cl-neo4j) [![GitHub stars](https://img.shields.io/github/stars/kraison/cl-neo4j?style=flat)](https://github.com/kraison/cl-neo4j/stargazers) - a thin neo4j RESTFUL client interface.
* [vivace-graph](https://github.com/kraison/vivace-graph-v3) [![GitHub stars](https://img.shields.io/github/stars/kraison/vivace-graph-v3?style=flat)](https://github.com/kraison/vivace-graph-v3/stargazers) - graph database & Prolog implementation. Takes design inspiration from CouchDB, neo4j and AllegroGraph. It implements an ACID-compliant object graph model with user-defined indexes and map-reduce views. It also implements a master / slave replication scheme for redundancy and horizontal read scaling. Querying the graph is accomplished via a number of Lisp methods or via a Prolog-like query language. [MIT][200].
  * "I have used Vivace Graph as an online catalog for millions of products, as the back end for a complex, adaptable VoIP-based IVR, as well as data store for several complex big data analysis systems, and finally as the engine for two recommender systems." (issue #23)
  * "Why is vivace graph so fast? I have been comparing it with SQL-based approach and Neo4j, and vivace graph is much, much faster."
* [Ariadne](https://git.sr.ht/~hajovonta/ariadne) - A graph database in Common Lisp with full W3C SPARQL 1.1 and SHACL conformance, Gremlin-style traversal, RDF import/export, property graph support, inference rules, graph analytics, and Graphviz visualization.
  * *Built with LLMs*.

and also:

* [restagraph](https://github.com/JermellB/restagraph) [![GitHub stars](https://img.shields.io/github/stars/JermellB/restagraph?style=flat)](https://github.com/JermellB/restagraph/stargazers) - an app that dynamically generates REST APIs for a Neo4j database, using a schema defined within the database. [GPL3][2].

<!-- lost in translation: (it was slow anyways) -->
<!-- * [facts](https://github.com/cl-facts/facts) [![GitHub stars](https://img.shields.io/github/stars/cl-facts/facts?style=flat)](https://github.com/cl-facts/facts/stargazers) - an in-memory graph database with transactions and rollbacks, logging/replay and dumping/loading to/from disk. BSD-style license (ISC). -->


Other DB wrappers
-----------------

* [cl-memcached](https://github.com/quasi/cl-memcached) [![GitHub stars](https://img.shields.io/github/stars/quasi/cl-memcached?style=flat)](https://github.com/quasi/cl-memcached/stargazers) - Fast, thread-safe interface to the Memcached object caching system. [Expat][14].
* [cl-redis](https://github.com/vseloved/cl-redis) [![GitHub stars](https://img.shields.io/github/stars/vseloved/cl-redis?style=flat)](https://github.com/vseloved/cl-redis/stargazers) - Redis client. [Expat][14].
* [cl-disque](https://github.com/CodyReichert/cl-disque) [![GitHub stars](https://img.shields.io/github/stars/CodyReichert/cl-disque?style=flat)](https://github.com/CodyReichert/cl-disque/stargazers) - Disque client. [3-clause BSD][15].
* [cl-rethinkdb](https://github.com/orthecreedence/cl-rethinkdb) [![GitHub stars](https://img.shields.io/github/stars/orthecreedence/cl-rethinkdb?style=flat)](https://github.com/orthecreedence/cl-rethinkdb/stargazers) - RethinkDB client. [Expat][14].
* [cl-mango](https://github.com/cmoore/cl-mango/) [![GitHub stars](https://img.shields.io/github/stars/cmoore/cl-mango/?style=flat)](https://github.com/cmoore/cl-mango//stargazers) -  A minimalist CouchDB 2.x database client. BSD_3Clause.
  * See also [clouchdb](https://common-lisp.net/project/clouchdb/) - Library for interacting with CouchDB. [FreeBSD][39].
* [lmdb](https://github.com/melisgl/lmdb) [![GitHub stars](https://img.shields.io/github/stars/melisgl/lmdb?style=flat)](https://github.com/melisgl/lmdb/stargazers) - Bindings to [LMDB](http://www.lmdb.tech/doc/), the Lightning Memory-mapped Database, an ACID key-value database with MultiVersion Concurrency Control.
* [cl-ndbapi](https://github.com/datagraph/cl-ndbapi) [![GitHub stars](https://img.shields.io/github/stars/datagraph/cl-ndbapi?style=flat)](https://github.com/datagraph/cl-ndbapi/stargazers) - bindings to the C++ NDB API of [RonDB](https://www.rondb.com/), "the world's fastest key value store", by [Dydra](https://dydra.com/home). GPLv2.
* [cl-duckdb](https://github.com/ak-coram/cl-duckdb) [![GitHub stars](https://img.shields.io/github/stars/ak-coram/cl-duckdb?style=flat)](https://github.com/ak-coram/cl-duckdb/stargazers) -  Common Lisp CFFI wrapper around the DuckDB C API. [MIT][200].
* [cl-bunny](https://github.com/cl-rabbit/cl-bunny) [![GitHub stars](https://img.shields.io/github/stars/cl-rabbit/cl-bunny?style=flat)](https://github.com/cl-rabbit/cl-bunny/stargazers) -  Common Lisp RabbitMQ client based on IOLib. MIT.

Migration tools
---------------

(recall that Mito handles migrations)

* [cl-migratum](https://github.com/dnaeon/cl-migratum) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/cl-migratum?style=flat)](https://github.com/dnaeon/cl-migratum/stargazers) - a system which provides facilities for performing database schema migrations, designed to work with various databases. [BSD_3Clause][15].
* [postmodern-passenger-pigeon](https://github.com/fisxoj/postmodern-passenger-pigeon/) [![GitHub stars](https://img.shields.io/github/stars/fisxoj/postmodern-passenger-pigeon/?style=flat)](https://github.com/fisxoj/postmodern-passenger-pigeon//stargazers) - a migration manager for postmodern. No licence specified.


To third parties
----------------

* [dyna](https://github.com/Rudolph-Miller/dyna) [![GitHub stars](https://img.shields.io/github/stars/Rudolph-Miller/dyna?style=flat)](https://github.com/Rudolph-Miller/dyna/stargazers) - an AWS DynamoDB ORM. [MIT][200].
* [cl-influxdb](https://github.com/mmaul/cl-influxdb/) [![GitHub stars](https://img.shields.io/github/stars/mmaul/cl-influxdb/?style=flat)](https://github.com/mmaul/cl-influxdb//stargazers) - an interface to the Time Series Database InfluxDB. [MIT][200].
* [cl-remizmq](https://fossil.cyberia9.org/cl-remizmq/index) - ZeroMQ sockets, messages, timers, atomics, and proxies.
  * low-level and high-level APIs. Tested with libzmq 5.2.5, any v4.x and v5.x should work, v3.x may as well.
* [coalton-zmq](https://github.com/coalton-lang/coalton-zmq) [![GitHub stars](https://img.shields.io/github/stars/coalton-lang/coalton-zmq?style=flat)](https://github.com/coalton-lang/coalton-zmq/stargazers) - ZeroMQ interface for Coalton.
  - "It's complete enough to be useful for building apps that use ZeroMQ". Many of the official [ZeroMQ examples](https://github.com/coalton-lang/coalton-zmq/tree/main/zmq-examples) [![GitHub stars](https://img.shields.io/github/stars/coalton-lang/coalton-zmq/tree/main/zmq-examples?style=flat)](https://github.com/coalton-lang/coalton-zmq/tree/main/zmq-examples/stargazers) are implemented.

Tools
-----

* ⭐ [pgloader](https://github.com/dimitri/pgloader) [![GitHub stars](https://img.shields.io/github/stars/dimitri/pgloader?style=flat)](https://github.com/dimitri/pgloader/stargazers) - a data loading tool for PostgreSQL. [PostgreSQL Licence][205].
  * obligatory blog post: [Why is pgloader so much faster?](https://tapoueh.org/blog/2014/05/why-is-pgloader-so-much-faster/) (hint: it was re-written from Python to Common Lisp)

Data Formats
============

CSV
---

* ⭐ [cl-csv](https://github.com/AccelerationNet/cl-csv) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/cl-csv?style=flat)](https://github.com/AccelerationNet/cl-csv/stargazers) - A library for parsing CSV files. [3-clause BSD][15].
  * [documentation](https://github.com/AccelerationNet/cl-csv/blob/master/DOCUMENTATION.md) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/cl-csv/blob/master/DOCUMENTATION.md?style=flat)](https://github.com/AccelerationNet/cl-csv/blob/master/DOCUMENTATION.md/stargazers)
  * [example blog post](https://dev.to/vindarel/read-csv-files-in-common-lisp-cl-csv-data-table-3c9n).
* [cl-decimals](https://github.com/tlikonen/cl-decimals) [![GitHub stars](https://img.shields.io/github/stars/tlikonen/cl-decimals?style=flat)](https://github.com/tlikonen/cl-decimals/stargazers) - Decimal number parser and formatter. Public domain.
* [auto-text](https://github.com/defunkydrummer/auto-text) [![GitHub stars](https://img.shields.io/github/stars/defunkydrummer/auto-text?style=flat)](https://github.com/defunkydrummer/auto-text/stargazers) - automatic (encoding, end of line, column width, csv delimiter etc) detection for text files. [MIT][200]. See also [inquisitor](https://github.com/t-sin/inquisitor) [![GitHub stars](https://img.shields.io/github/stars/t-sin/inquisitor?style=flat)](https://github.com/t-sin/inquisitor/stargazers) for detection of asian and far eastern languages.
* [csv-validator](https://github.com/KoenvdBerg/csv-validator) [![GitHub stars](https://img.shields.io/github/stars/KoenvdBerg/csv-validator?style=flat)](https://github.com/KoenvdBerg/csv-validator/stargazers) - Validates tabular CSV data using predefined validations, inspired from its Python homologue "Great Expectations". [BSD_3Clause][15].

See also: cl-duckdb for fast parsing, [lisp-stat's data-frames `read-csv`](https://lisp-stat.dev/docs/manuals/data-frame/), [vellum-csv](https://github.com/sirherrbatka/vellum-csv/) [![GitHub stars](https://img.shields.io/github/stars/sirherrbatka/vellum-csv/?style=flat)](https://github.com/sirherrbatka/vellum-csv//stargazers) (data frames library), vellum-duckdb.

JSON
----

* 👍 [jzon](https://github.com/Zulu-Inuoe/jzon/) [![GitHub stars](https://img.shields.io/github/stars/Zulu-Inuoe/jzon/?style=flat)](https://github.com/Zulu-Inuoe/jzon//stargazers) - a correct, safe and fast JSON parser. [MIT][200].
  * jzon is the only CL JSON library which correctly declines all invalid inputs per the official JSON test suite and accepts all valid inputs per that suite.
  * it doesn't crash on invalid input (jsown), doesn't choke on large datasets (Jonathan), and more.
  * "I believe jzon to be the superior choice and hope for it to become the new, true de-facto library in the world of JSON-in-CL once and for all."
* [shasht](https://github.com/yitzchak/shasht) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/shasht?style=flat)](https://github.com/yitzchak/shasht/stargazers) -  Common Lisp JSON reading and writing for the Kzinti. [MIT][14].
  - "Shasht is one of the two new libraries that I particularly like and is already in quicklisp. It is fast, it handles null correctly, it encodes CLOS objects, structures and hash-tables. It can also do incremental encoding." Sabra Crolleton.
* [cl-json](https://github.com/sharplispers/cl-json) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/cl-json?style=flat)](https://github.com/sharplispers/cl-json/stargazers) - A highly customizable JSON encoder and decoder. [MIT][14].
  * "cl-json and yason are still the work horses if you need fine control, but speed is not their forte." @sabracrolleton
* [parcom/json](https://github.com/fosskers/parcom) [![GitHub stars](https://img.shields.io/github/stars/fosskers/parcom?style=flat)](https://github.com/fosskers/parcom/stargazers) - An extension to `parcom` for simple, fast, no-dependency JSON parsing.

See this [extensive comparison](https://sabracrolleton.github.io/json-review) of many more JSON libraries, as well as [these benchmarks](https://github.com/fosskers/parcom?tab=readme-ov-file#json-benchmarks).

JSON tools:

* [NJSON](https://github.com/atlas-engineer/njson) [![GitHub stars](https://img.shields.io/github/stars/atlas-engineer/njson?style=flat)](https://github.com/atlas-engineer/njson/stargazers) - Parser-agnostic JSON indexing (with JSON Pointer support), destructuring, and validation framework. [BSD][15].
* [json-mop](https://github.com/gschjetne/json-mop) [![GitHub stars](https://img.shields.io/github/stars/gschjetne/json-mop?style=flat)](https://github.com/gschjetne/json-mop/stargazers) - A metaclass for bridging CLOS and JSON objects. [MIT][200].
  * depends on YASON
  * for JSON libraries that don't do it natively (jzon, shasht and cl-json are able to *encode* CLOS objects to JSON out of the box, and cl-json has the ability to *decode* JSON objects into a "fluid-class" CLOS object.)
* [cl-json-pointer](https://github.com/y2q-actionman/cl-json-pointer) [![GitHub stars](https://img.shields.io/github/stars/y2q-actionman/cl-json-pointer?style=flat)](https://github.com/y2q-actionman/cl-json-pointer/stargazers) - A JSON Pointer implementation. [MIT][200].
* [cl-jwk](https://github.com/dnaeon/cl-jwk) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/cl-jwk?style=flat)](https://github.com/dnaeon/cl-jwk/stargazers) -  Common Lisp system for decoding public JSON Web Keys (JWK). BSD License.
* [JOSE](https://github.com/fukamachi/jose) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/jose?style=flat)](https://github.com/fukamachi/jose/stargazers) - A JSON Object Signing and Encryption (JOSE) implementation for Common Lisp. BSD_2Clause.
* [cl-jsonpath](https://git.sr.ht/~hajovonta/cl-jsonpath) - A JSONPath implementation for Common Lisp with 99% test compliance and complete real-world compatibility. MIT. With AI inside.
* [cl-json-utils](https://git.sr.ht/~q3cpma/cl-json-utils) - querying JSON, inspired by JSONPath by lisp-ier.
  * jsonpath: `$.store.book[*].author`, json-utils: `(query $ "store" "book" :wild "author")`

JSON online services:

* [pantry](https://github.com/dotemacs/pantry) [![GitHub stars](https://img.shields.io/github/stars/dotemacs/pantry?style=flat)](https://github.com/dotemacs/pantry/stargazers) - client library for the [Pantry JSON storage service](https://getpantry.cloud/). BSD.

and search for JSON RPC below.

TOML
----
* [parcom/toml](https://github.com/fosskers/parcom) [![GitHub stars](https://img.shields.io/github/stars/fosskers/parcom?style=flat)](https://github.com/fosskers/parcom/stargazers) - An extension to `parcom` for simple, no-dependency TOML parsing.
* [clop](https://github.com/sheepduke/clop) [![GitHub stars](https://img.shields.io/github/stars/sheepduke/clop?style=flat)](https://github.com/sheepduke/clop/stargazers) - A 1.0-compliant TOML parser.

XML
---

* [CXML](https://common-lisp.net/project/cxml/) - XML parser and serializer, with a range of extension libraries. [LLGPL][8].
  - 👍 has an incremental parser, allowing to parse big files.
  - see the [FXML](https://github.com/ruricolist/FXML) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/FXML?style=flat)](https://github.com/ruricolist/FXML/stargazers) fork, with fixes and new features. You should use it if your are parsing potentially ill-formed or malicious XML, or if you need to use Klacks with namespaces.
* [Plump][71] - A lenient XML parser. [zlib][33].
* [parcom/xml](https://github.com/fosskers/parcom) [![GitHub stars](https://img.shields.io/github/stars/fosskers/parcom?style=flat)](https://github.com/fosskers/parcom/stargazers) - An extension to `parcom` for simple, fast XML parsing.
* [xpath](https://github.com/sharplispers/xpath) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/xpath?style=flat)](https://github.com/sharplispers/xpath/stargazers) ([homepage](https://common-lisp.net/project/plexippus-xpath/atdoc/index.html) - Implementation of the XML Path Language (XPath) Version 1.0. [BSD_2Clause][17].
* [s-xml](http://cliki.net/S-XML) - A basic parser. [LLGPL][8].
* [xmls](https://github.com/rpgoldman/xmls) [![GitHub stars](https://img.shields.io/github/stars/rpgoldman/xmls?style=flat)](https://github.com/rpgoldman/xmls/stargazers) - A small, simple, non-validating XML parser. [3-clause BSD][15].
* [cl-feedparser](https://github.com/TBRSS/cl-feedparser) [![GitHub stars](https://img.shields.io/github/stars/TBRSS/cl-feedparser?style=flat)](https://github.com/TBRSS/cl-feedparser/stargazers) - A Common Lisp (RSS, Atom) feed parser. [LLGPL][8]
* [Buildnode](https://github.com/AccelerationNet/buildnode) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/buildnode?style=flat)](https://github.com/AccelerationNet/buildnode/stargazers) - A common lisp library to ease interaction with CXML-dom, such as building Excel spreadsheets. [BSD][15].

<!-- * [cl-xmlspan](https://github.com/rogpeppe/cl-xmlspam/) [![GitHub stars](https://img.shields.io/github/stars/rogpeppe/cl-xmlspam/?style=flat)](https://github.com/rogpeppe/cl-xmlspam//stargazers) - concise, regexp-like pattern matching on streaming XML. BSD_3-clause. -->
<!--   * "What do you do when you have a XML file that's larger than you want to fit in memory, and you want to extract some information from it? Writing code to deal with SAX events, or even using Klacks quickly becomes tedious. Cl-xmlspam is designed to make it easy to write code that mirrors the structure of the XML that it's parsing." -->

To read Excel files:

* [cl-excel](https://github.com/gwangjinkim/cl-excel) [![GitHub stars](https://img.shields.io/github/stars/gwangjinkim/cl-excel?style=flat)](https://github.com/gwangjinkim/cl-excel/stargazers) - a modern and powerful Common Lisp library for reading and writing Microsoft Excel .xlsx and LibreOffice .ods files. MIT.
  * "allow developers to handle complex spreadsheets with minimal code while maintaining memory efficiency for large datasets."
  * full writing support.
  * robust format detection.

YAML
----

* 👍 [cl-yaml](https://github.com/eudoxia0/cl-yaml.git) [![GitHub stars](https://img.shields.io/github/stars/eudoxia0/cl-yaml.git?style=flat)](https://github.com/eudoxia0/cl-yaml.git/stargazers) - a YAML parser and emitter built on top of libyaml. [MIT][200].
  * an active fork: [cl-RemiYaml](https://nanako.mooo.com/fossil/cl-remiyaml/index) with a few fixes. Not a drop-in replacement.
* [yamson](https://github.com/bohonghuang/yamson) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/yamson?style=flat)](https://github.com/bohonghuang/yamson/stargazers) - Fast YAML and JSON parsers for Common Lisp (not yet emitters). Apache2.0.

<!-- * [nyaml](https://github.com/jasom/nyaml) [![GitHub stars](https://img.shields.io/github/stars/jasom/nyaml?style=flat)](https://github.com/jasom/nyaml/stargazers) - A lisp native YAML parser. MIT. -->
  <!-- * *in our tests (2026), nyaml was slow (too orders of magnitude slower than cl-yaml* -->

Data Structures
===============

strings:

* 👍 [str](https://github.com/vindarel/cl-str) [![GitHub stars](https://img.shields.io/github/stars/vindarel/cl-str?style=flat)](https://github.com/vindarel/cl-str/stargazers) - a modern, simple and consistent string manipulation library. [MIT][200].
* [rope](https://github.com/garlic0x1/rope) [![GitHub stars](https://img.shields.io/github/stars/garlic0x1/rope?style=flat)](https://github.com/garlic0x1/rope/stargazers) -  Immutable Ropes for Common Lisp. MIT.
  - see also: ropes in Sycamore.

lists and sequences:

* [trivial-extensible-sequences](https://codeberg.org/shinmera/trivial-extensible-sequences) - Portability library for the extensible sequences protocol ([SBCL documentation](http://www.sbcl.org/manual/#Extensible-Sequences)). [zlib][33].
* [listopia](https://github.com/Dimercel/listopia) [![GitHub stars](https://img.shields.io/github/stars/Dimercel/listopia?style=flat)](https://github.com/Dimercel/listopia/stargazers) - a list manipulation library inspired by Haskell's Data.List. [LLGPL][8].
* [nonempty](https://github.com/fosskers/cl-nonempty) [![GitHub stars](https://img.shields.io/github/stars/fosskers/cl-nonempty?style=flat)](https://github.com/fosskers/cl-nonempty/stargazers) -  Non-empty collections for Common Lisp.  [LGPL3][9].
* also cl-containers, cl-data-structures, serapeum

(purely) functional data structures:

* 👍 [FSet](https://common-lisp.net/project/fset) - A functional, set-theoretic collections data structure library. [LLGPL][8].
  * defines four major types: seqs (sequences), maps (hash-tables), sets and bags (like sets, but they remember the number of times each member has been added to it).  Now includes JSON support in system FSet/Jzon.
* [sycamore](https://github.com/ndantam/sycamore) [![GitHub stars](https://img.shields.io/github/stars/ndantam/sycamore?style=flat)](https://github.com/ndantam/sycamore/stargazers) -  a fast, purely functional data structure library. [BSD_3Clause][15].
  - comparison: [FSet vs. Sycamore](https://scottlburson2.blogspot.com/2024/10/comparison-fset-vs-sycamore.html)
* [modf](https://github.com/smithzvk/modf) [![GitHub stars](https://img.shields.io/github/stars/smithzvk/modf?style=flat)](https://github.com/smithzvk/modf/stargazers) - a setf-like macro for functional programming.
* also cl-containers, cl-data-structures

hash-tables:

* Serapeum's hash-table functions: `dict` etc.
* [cl-hash-util](https://github.com/orthecreedence/cl-hash-util) [![GitHub stars](https://img.shields.io/github/stars/orthecreedence/cl-hash-util?style=flat)](https://github.com/orthecreedence/cl-hash-util/stargazers) - Hash-table creation, access, and manipulation utilities. [MIT][200].
* [hash-set](https://github.com/samebchase/hash-set/) [![GitHub stars](https://img.shields.io/github/stars/samebchase/hash-set/?style=flat)](https://github.com/samebchase/hash-set//stargazers) - a convenience library implementing hash sets on top of CL hash tables [The Unlicense][5]
* also cl-containers, cl-data-structures, serapeum

algorithms:

* [cl-competitive](https://github.com/privet-kitty/cl-competitive) [![GitHub stars](https://img.shields.io/github/stars/privet-kitty/cl-competitive?style=flat)](https://github.com/privet-kitty/cl-competitive/stargazers) - Common Lisp algorithms collection for competitive programming. Public domain, CCO or MIT.
* [cl-permutation](https://github.com/stylewarning/cl-permutation) [![GitHub stars](https://img.shields.io/github/stars/stylewarning/cl-permutation?style=flat)](https://github.com/stylewarning/cl-permutation/stargazers) -  Permutations and permutation groups in Common Lisp. [BSD_3Clause][15].

trees:

* [bst](https://codeberg.org/glv/bst) - Binary Search Tree. [GPL3][2].
* also cl-containers, cl-data-structures, serapeum

heaps:

* [pileup](http://nikodemus.github.io/pileup/) - a portable, performant, and thread-safe binary heap for Common Lisp. [MIT][200].

queues:

* [cl-freelock](https://github.com/ItsMeForLua/cl-freelock) [![GitHub stars](https://img.shields.io/github/stars/ItsMeForLua/cl-freelock?style=flat)](https://github.com/ItsMeForLua/cl-freelock/stargazers) - thread-safe, lock-free queues optimized for different use cases and hardware. The library offers three queue types, each designed for specific concurrency patterns and performance requirements.
  * On systems with many cores, cl-freelock demonstrates up to 3.2x performance improvements over competing libraries.


bigger collection libraries:

* [cl-data-structures](https://github.com/sirherrbatka/cl-data-structures) [![GitHub stars](https://img.shields.io/github/stars/sirherrbatka/cl-data-structures?style=flat)](https://github.com/sirherrbatka/cl-data-structures/stargazers) - a portable collection of data structures (mutable and immutable) and streaming algorithms (aggregations, group-by and so on, mainly dicts and sequences, with some statistical functions). [BSD][15].
  * sequences, sets, queues, dictionaries
* [cl-containers](https://github.com/hraban/cl-containers) [![GitHub stars](https://img.shields.io/github/stars/hraban/cl-containers?style=flat)](https://github.com/hraban/cl-containers/stargazers) - an extensive library of data structures and utilities - queues, trees, heaps, doubly-linked lists, sets, bags,... [MIT][200]
  * and a "standard interface so that they are simpler to use and so that changing design decisions becomes significantly easier".

Other data structures:

* [cl-ctrie](https://github.com/danlentz/cl-ctrie) [![GitHub stars](https://img.shields.io/github/stars/danlentz/cl-ctrie?style=flat)](https://github.com/danlentz/cl-ctrie/stargazers) -
lock-free, concurrent, key/value index with efficient memory-mapped persistence and fast transient storage models. [MIT][200].
* [bitfield](https://github.com/marcoheisig/bitfield) [![GitHub stars](https://img.shields.io/github/stars/marcoheisig/bitfield?style=flat)](https://github.com/marcoheisig/bitfield/stargazers) - Efficiently represent several finite sets or small integers as a single non-negative integer. [MIT][200].
* [bit-smasher](https://github.com/thephoeron/bit-smasher) [![GitHub stars](https://img.shields.io/github/stars/thephoeron/bit-smasher?style=flat)](https://github.com/thephoeron/bit-smasher/stargazers) -  Common Lisp library for handling bit vectors, bit vector arithmetic, and type conversions. [MIT][200].

Generic access of data structures:

* 👍 [access](https://github.com/AccelerationNet/access/) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/access/?style=flat)](https://github.com/AccelerationNet/access//stargazers) - Consistent and nested access to most common data structures. [BSD_3Clause][15].


See also:

* [Pretty printing tree data structures in Common Lisp](https://gist.github.com/WetHat/9682b8f70f0241c37cd5d732784d1577) (as a Jupyter notebook)


Docker images
=============

* [cl-docker-images](https://common-lisp.net/project/cl-docker-images/) - Docker images for ABCL, CCL, ECL, and SBCL on Windows (amd64) and Alpine and Debian (amd64, arm64, arm/v7) [BSD_2Clause][17].
* [base-lisp-image](https://github.com/40ants/base-lisp-image) [![GitHub stars](https://img.shields.io/github/stars/40ants/base-lisp-image?style=flat)](https://github.com/40ants/base-lisp-image/stargazers) - base
  Docker image for Common Lisp projects with SBCL or CCL and the latest
  ASDF, Qlot and Roswell.
* [40ants/setup-lisp](https://github.com/40ants/setup-lisp) [![GitHub stars](https://img.shields.io/github/stars/40ants/setup-lisp?style=flat)](https://github.com/40ants/setup-lisp/stargazers) -  GitHub Action to Setup Common Lisp tools.
  * updates ASDF, installs Qlot, installs Roswell
  * for multiple implementations
  * for Ubuntu, OSX and Windows.
  * Example use: [Trial's CI](https://github.com/Shirakumo/trial/blob/master/.github/workflows/examples.yml) [![GitHub stars](https://img.shields.io/github/stars/Shirakumo/trial/blob/master/.github/workflows/examples.yml?style=flat)](https://github.com/Shirakumo/trial/blob/master/.github/workflows/examples.yml/stargazers)
* [fukamachi/dockerfiles](https://github.com/fukamachi/dockerfiles) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/dockerfiles?style=flat)](https://github.com/fukamachi/dockerfiles/stargazers) - Dockerfiles for Common Lisp programming. Roswell, SBCL, CCL.
* [archlinux-cl](https://github.com/yitzchak/archlinux-cl) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/archlinux-cl?style=flat)](https://github.com/yitzchak/archlinux-cl/stargazers) - Docker Arch Linux image with Common Lisp implementations (7 to this day). MIT.
* [docker-lisp-gamedev](https://gitlab.com/lockie/docker-lisp-gamedev) - A Docker image containing tools necessary for Common Lisp game development and deployment. Comes in Linux and Windows variety. Thoroughly tested via CI.


Foreign Function Interface, languages interop
=============================================

## C ##

* ⭐ [CFFI](https://github.com/cffi/cffi) [![GitHub stars](https://img.shields.io/github/stars/cffi/cffi?style=flat)](https://github.com/cffi/cffi/stargazers) - Portable, easy-to-use C foreign function interface. [Expat][14].
  * [cffi-ops](https://github.com/bohonghuang/cffi-ops) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/cffi-ops?style=flat)](https://github.com/bohonghuang/cffi-ops/stargazers) - helps write concise CFFI-related code.
  * [cffi-objects](https://github.com/bohonghuang/cffi-object) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/cffi-object?style=flat)](https://github.com/bohonghuang/cffi-object/stargazers) - enables fast and convenient interoperation with foreign objects.
* 👍[cl-autowrap](https://github.com/rpav/cl-autowrap) [![GitHub stars](https://img.shields.io/github/stars/rpav/cl-autowrap?style=flat)](https://github.com/rpav/cl-autowrap/stargazers) - Automatically parses header files into CFFI definitions. [FreeBSD][39].
* [cl-bindgen](https://github.com/sdilts/cl-bindgen) [![GitHub stars](https://img.shields.io/github/stars/sdilts/cl-bindgen?style=flat)](https://github.com/sdilts/cl-bindgen/stargazers) - A command line tool and library for creating Common Lisp language bindings from C header files. [MIT][200].
* [cl-gobject-introspection](https://github.com/andy128k/cl-gobject-introspection) [![GitHub stars](https://img.shields.io/github/stars/andy128k/cl-gobject-introspection?style=flat)](https://github.com/andy128k/cl-gobject-introspection/stargazers) - [Gobject Introspection](https://gi.readthedocs.io/en/latest/) FFI. Automatic bindings to call into the C library. [BSD][15]. Generate a lisp interface with [gir2cl](https://github.com/kat-co/gir2cl) [![GitHub stars](https://img.shields.io/github/stars/kat-co/gir2cl?style=flat)](https://github.com/kat-co/gir2cl/stargazers). [LGPL3][9].
* [cl-cxx-jit](https://github.com/Islam0mar/CL-CXX-JIT) [![GitHub stars](https://img.shields.io/github/stars/Islam0mar/CL-CXX-JIT?style=flat)](https://github.com/Islam0mar/CL-CXX-JIT/stargazers) -  Common Lisp and C++ interoperation with JIT. [MIT][200].

## Clojure

* [ABCLJ](https://github.com/lsevero/abclj) [![GitHub stars](https://img.shields.io/github/stars/lsevero/abclj?style=flat)](https://github.com/lsevero/abclj/stargazers) - dead easy  Clojure to Common lisp interop. EPL-2.0.

In development:

* [Cloture](https://github.com/ruricolist/cloture) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/cloture?style=flat)](https://github.com/ruricolist/cloture/stargazers) - Clojure in Common Lisp.

> Cloture is in very early (pre-alpha) stages, but it has progressed far enough to load clojure.test, allowing the test suite to actually be written in Clojure.

See also those libraries:

* NEW! in 2025 [clj-coll](https://github.com/dtenny/clj-coll) [![GitHub stars](https://img.shields.io/github/stars/dtenny/clj-coll?style=flat)](https://github.com/dtenny/clj-coll/stargazers) -  Clojure collection and sequence APIs in Common Lisp, with optional Clojure collection syntax. [Eclipse][209].
  * provides immutable Cons, Queue, PersistentList, capabilities as well as Vector, Set, and Map analogues built on FSet (but accessed entirely via Clojure APIs).
  * optional read syntax so you can type `{:a 1 :b 2}`, `#{1 2 3}`, and `[1 2 3]`.
* [clj-con](https://github.com/dtenny/clj-con) [![GitHub stars](https://img.shields.io/github/stars/dtenny/clj-con?style=flat)](https://github.com/dtenny/clj-con/stargazers) - Clojure-style concurrency operations in Common Lisp. [MIT][200].
* [clj-re](https://github.com/dtenny/clj-re/) [![GitHub stars](https://img.shields.io/github/stars/dtenny/clj-re/?style=flat)](https://github.com/dtenny/clj-re//stargazers) - Clojure-style regular expression functions.
* [clj-arrows](https://github.com/dtenny/clj-arrows) [![GitHub stars](https://img.shields.io/github/stars/dtenny/clj-arrows?style=flat)](https://github.com/dtenny/clj-arrows/stargazers) -  Clojure-compatible threading/transformation/arrow macros for Common Lisp.
* [with-redefs](https://github.com/dtenny/with-redefs) [![GitHub stars](https://img.shields.io/github/stars/dtenny/with-redefs?style=flat)](https://github.com/dtenny/with-redefs/stargazers) - enables rebinding of global functions, inspired by Clojure's with-redefs.
* [cl-oju](https://github.com/eigenhombre/cl-oju/) [![GitHub stars](https://img.shields.io/github/stars/eigenhombre/cl-oju/?style=flat)](https://github.com/eigenhombre/cl-oju//stargazers) - a few idioms, mostly relating to sequences, that I miss when writing Common Lisp. [MIT][200].

## Erlang ##

* [CLERIC](https://github.com/flambard/CLERIC) [![GitHub stars](https://img.shields.io/github/stars/flambard/CLERIC?style=flat)](https://github.com/flambard/CLERIC/stargazers) - a Common Lisp Erlang Interface. An implementation of the Erlang distribution protocol, comparable with erl_interface and jinterface. [MIT][200].

## Java ##

(see also LispWorks and ABCL)

* [open-ldk](https://github.com/atgreen/openldk) [![GitHub stars](https://img.shields.io/github/stars/atgreen/openldk?style=flat)](https://github.com/atgreen/openldk/stargazers) - A Java JIT Compiler and Runtime in Common Lisp. [GPL3.0][89]. (Work In Progress)
  * "bridges the gap between Java and Common Lisp by incrementally translating Java bytecode into Lisp, which is then compiled into native machine code for execution. This unique approach allows Java classes to be seamlessly mapped to Common Lisp Object System (CLOS) classes, enabling effortless integration between Java and Common Lisp codebases."
  * "provides a practical solution for integrating Java libraries into a Lisp-based workflow without the need for an out-of-process Java runtime environment."

See also:

* [FOIL](https://github.com/jasom/foil/blob/master/docs/foil.md) [![GitHub stars](https://img.shields.io/github/stars/jasom/foil/blob/master/docs/foil.md?style=flat)](https://github.com/jasom/foil/blob/master/docs/foil.md/stargazers) - Rich Hickey's Foreign Object Interface for Lisp to access the JVM and the CLI/CLR.


## Objective-C ##

* [cl-nextstep](https://github.com/byulparan/cl-nextstep) [![GitHub stars](https://img.shields.io/github/stars/byulparan/cl-nextstep?style=flat)](https://github.com/byulparan/cl-nextstep/stargazers) -  Cocoa binding for Common Lisp on macOS.
* [objc-lisp-bridge](https://github.com/fiddlerwoaroof/objc-lisp-bridge) [![GitHub stars](https://img.shields.io/github/stars/fiddlerwoaroof/objc-lisp-bridge?style=flat)](https://github.com/fiddlerwoaroof/objc-lisp-bridge/stargazers) -  A portable reader and bridge for interacting with Objective-C and Cocoa. [MIT][200].
* [cocoas](https://codeberg.org/shinmera/cocoas) -  A toolkit library to help deal with CoreFoundation, Cocoa, and objc. zlib.

## Python ##

* [burgled-batteries](https://github.com/pinterface/burgled-batteries) [![GitHub stars](https://img.shields.io/github/stars/pinterface/burgled-batteries?style=flat)](https://github.com/pinterface/burgled-batteries/stargazers) - A bridge between Python and Common Lisp. The goal is that Lisp programs can use Python libraries. Not available on Quicklisp. [MIT][200].
* [cl4py](https://github.com/marcoheisig/cl4py) [![GitHub stars](https://img.shields.io/github/stars/marcoheisig/cl4py?style=flat)](https://github.com/marcoheisig/cl4py/stargazers) - The library cl4py (pronounce as clappy) allows Python programs to call Common Lisp libraries. [MIT][200].
* [py4cl](https://github.com/bendudson/py4cl) [![GitHub stars](https://img.shields.io/github/stars/bendudson/py4cl?style=flat)](https://github.com/bendudson/py4cl/stargazers) - A library that allows Common Lisp code to access Python libraries. It is basically the inverse of cl4py. [MIT][200].
  * its fork [py4cl2](https://github.com/digikar99/py4cl2) [![GitHub stars](https://img.shields.io/github/stars/digikar99/py4cl2?style=flat)](https://github.com/digikar99/py4cl2/stargazers), at first less stable, now more developped and faster.
  * [py4cl2-cffi](https://github.com/digikar99/py4cl2-cffi) [![GitHub stars](https://img.shields.io/github/stars/digikar99/py4cl2-cffi?style=flat)](https://github.com/digikar99/py4cl2-cffi/stargazers) - CFFI based alternative to py4cl2.
    * "When capable, the CFFI approach can be a 50 times faster than py4cl2."

See also [async-process](https://github.com/cxxxr/async-process/) [![GitHub stars](https://img.shields.io/github/stars/cxxxr/async-process/?style=flat)](https://github.com/cxxxr/async-process//stargazers).

* [cl-python](https://github.com/metawilm/cl-python) [![GitHub stars](https://img.shields.io/github/stars/metawilm/cl-python?style=flat)](https://github.com/metawilm/cl-python/stargazers) - an implementation of Python in Common Lisp. [LLGPL][8], not under active development.


## .Net Core

* [Bike](https://github.com/Lovesan/bike) [![GitHub stars](https://img.shields.io/github/stars/Lovesan/bike?style=flat)](https://github.com/Lovesan/bike/stargazers) - a cross-platform .Net Core interface. [MIT][200].

## Emacs Lisp

* [CEDAR](https://gitlab.com/sasanidas/cedar) - an advance interactive development environment aiming to be Emacs compatible with all the features that come with it. Stalled.
* [CLOCC's elisp.lisp](https://sourceforge.net/p/clocc/hg/ci/default/tree/src/cllib/elisp.lisp) - Emacs Lisp in Common Lisp.
  * implementation of the Emacs Lisp language as a Common Lisp package. [1999]
  * does not attempt to reimplement the library of functions provided in Emacs to manipulate buffers and other related objects, so it focuses on the "pure" Emacs Lisp language; but it was able to run the non-UI parts of the Emacs Calendar. (S. Monnier, M. Sperber)


Game Development
================

* [Trial](https://codeberg.org/shirakumo/trial) - Trial is an OpenGL game engine with a heavy focus on modularity. It is supposed to provide a large toolkit of useful bits and pieces from which you can create a game. Custom: [zlib][33] with a political clause added.
  * the [Kandria](https://kandria.com/) game is built with Trial.
* [claw-raylib](https://github.com/bohonghuang/claw-raylib) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/claw-raylib?style=flat)](https://github.com/bohonghuang/claw-raylib/stargazers) - Fully auto-generated Common Lisp bindings to Raylib and Raygui using claw and cffi-object. Apache 2.0.
* [raylib](https://github.com/fosskers/raylib/) [![GitHub stars](https://img.shields.io/github/stars/fosskers/raylib/?style=flat)](https://github.com/fosskers/raylib//stargazers) (2025) - Hand-written bindings to Raylib for improved performance and smaller dependency footprint. [MPL-2.0][211].
* [trivial-gamekit](https://github.com/borodust/trivial-gamekit) [![GitHub stars](https://img.shields.io/github/stars/borodust/trivial-gamekit?style=flat)](https://github.com/borodust/trivial-gamekit/stargazers) – With this small framework you would be able to make simple 2D games: draw basic geometric forms, images and text, play sounds and listen to mouse and keyboard input. [MIT][200].
* [Xelf](https://gitlab.com/dto/xelf/) - Extensible game library. Not available on Quicklisp. [GNU LGPL2.1][11].
* [eon](https://github.com/bohonghuang/eon) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/eon?style=flat)](https://github.com/bohonghuang/eon/stargazers) -  An easy-to-use but flexible game framework based on Raylib for Common Lisp. Apache2.0.

Utilities:

* [cl-gamepad](https://shirakumo.github.io/cl-gamepad) - Access to gamepads and joysticks on Windows, Mac OS, and Linux. [zlib][33].
* [cl-mpg123](https://shirakumo.github.io/cl-mpg123) and [cl-out123](https://shirakumo.github.io/cl-out123), bindings libraries for libmpg123 and libout123 respectively, giving you fast and easy to use mp3 decoding and cross-platform audio output. [zlib][33].

Chess:

* [Queen.lisp](https://github.com/mishoo/queen.lisp) [![GitHub stars](https://img.shields.io/github/stars/mishoo/queen.lisp?style=flat)](https://github.com/mishoo/queen.lisp/stargazers) - Chess Utilities For Common Lisp. MIT.
  * board generation (0x88 method), move generation, FEN/SAN/PGN parser and generator, basic evaluation engine.

Graphics
========

These are libraries for working with graphics, rather than making GUIs (i.e. widget toolkits), which have their own section.

* ⭐ [Sketch](https://github.com/vydd/sketch) [![GitHub stars](https://img.shields.io/github/stars/vydd/sketch?style=flat)](https://github.com/vydd/sketch/stargazers) - A CL framework for the creation of electronic art, graphics, and lots more. [MIT][200].
* [Vecto](http://www.xach.com/lisp/vecto/) - Simple vector drawing library. [FreeBSD][39].
* [cl-svg](https://github.com/wmannis/cl-svg) [![GitHub stars](https://img.shields.io/github/stars/wmannis/cl-svg?style=flat)](https://github.com/wmannis/cl-svg/stargazers) - A basic library for producing SVG files. [Expat][14].
* [trivial-svg](https://github.com/calsys456/trivial-svg) [![GitHub stars](https://img.shields.io/github/stars/calsys456/trivial-svg?style=flat)](https://github.com/calsys456/trivial-svg/stargazers) - render SVG images to PNG using Vecto and zpb-ttf. 0BSD.
* [dufy](https://github.com/privet-kitty/dufy) [![GitHub stars](https://img.shields.io/github/stars/privet-kitty/dufy?style=flat)](https://github.com/privet-kitty/dufy/stargazers) - exact color manipulation and conversion in various color models. [MIT][200].
* [opticl](https://github.com/slyrus/opticl) [![GitHub stars](https://img.shields.io/github/stars/slyrus/opticl?style=flat)](https://github.com/slyrus/opticl/stargazers) - a library for representing and processing images. [BSD_2Clause][17].
* [Varjo](https://github.com/cbaggers/varjo) [![GitHub stars](https://img.shields.io/github/stars/cbaggers/varjo?style=flat)](https://github.com/cbaggers/varjo/stargazers) - Lisp to GLSL translator. [BSD_2Clause][17].
* [zpng](http://www.xach.com/lisp/zpng/) - A library for creating PNG files. [FreeBSD][39].
* [pngload-fast](https://github.com/lisp-mirror/pngload) [![GitHub stars](https://img.shields.io/github/stars/lisp-mirror/pngload?style=flat)](https://github.com/lisp-mirror/pngload/stargazers) - A PNG (Portable Network Graphics) image format decoder in portable Common Lisp with an emphasis on speed. [MIT][200].
* [imago](https://github.com/tokenrove/imago) [![GitHub stars](https://img.shields.io/github/stars/tokenrove/imago?style=flat)](https://github.com/tokenrove/imago/stargazers) -  image manipulation library for Common Lisp.
  * supports images in png, pcx, portable bitmap (.pnm), Truevision TGA (.tga) and jpeg formats
  * allows for: resizing, rotation, emboss effect, inverting colors, adjusting contrast, manipulating color elements, composing pictures, drawing simple primitives…
  * is integrated with common-lisp-jupyter.

These are bindings:

* [glfw](https://github.com/shirakumo/glfw) [![GitHub stars](https://img.shields.io/github/stars/shirakumo/glfw?style=flat)](https://github.com/shirakumo/glfw/stargazers) - An up-to-date Common Lisp bindings library to the most recent GLFW OpenGL context management library.
* [cl-cairo2](https://github.com/rpav/cl-cairo2) [![GitHub stars](https://img.shields.io/github/stars/rpav/cl-cairo2?style=flat)](https://github.com/rpav/cl-cairo2/stargazers) - Cairo bindings. [Boost 1.0][54]
* [cl-gd](http://weitz.de/cl-gd/) - A library providing an interface to the GD graphics library. [FreeBSD][39].
* [cl-horde3d](https://github.com/anwyn/cl-horde3d/) [![GitHub stars](https://img.shields.io/github/stars/anwyn/cl-horde3d/?style=flat)](https://github.com/anwyn/cl-horde3d//stargazers) - FFI bindings to the Horde3D graphics library. Not available on Quicklisp. [EPL 1.0][59]
* [cl-jpeg](https://github.com/sharplispers/cl-jpeg) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/cl-jpeg?style=flat)](https://github.com/sharplispers/cl-jpeg/stargazers) - Baseline JPEG encoder and decoder library. [3-clause BSD][15].
* [cl-liballegro](https://github.com/resttime/cl-liballegro) [![GitHub stars](https://img.shields.io/github/stars/resttime/cl-liballegro?style=flat)](https://github.com/resttime/cl-liballegro/stargazers) - Interface and bindings to the Allegro 5 game programming library. [zlib][33].
* [cl-opengl](https://github.com/3b/cl-opengl) [![GitHub stars](https://img.shields.io/github/stars/3b/cl-opengl?style=flat)](https://github.com/3b/cl-opengl/stargazers) - CFFI bindings to OpenGL, GLU and GLUT APIs. [3-clause BSD][15].
* [cl-sdl2](https://github.com/lispgames/cl-sdl2) [![GitHub stars](https://img.shields.io/github/stars/lispgames/cl-sdl2?style=flat)](https://github.com/lispgames/cl-sdl2/stargazers) - Bindings for SDL2 using C2FFI. [Expat][14].
* [CLinch](https://github.com/BradWBeer/CLinch) [![GitHub stars](https://img.shields.io/github/stars/BradWBeer/CLinch?style=flat)](https://github.com/BradWBeer/CLinch/stargazers) - Common Lisp 2D/3D graphics engine for OpenGL. [FreeBSD][39].
* [donuts](https://github.com/tkych/donuts) [![GitHub stars](https://img.shields.io/github/stars/tkych/donuts?style=flat)](https://github.com/tkych/donuts/stargazers) - Graphviz interface for Common Lisp. [Expat][14].
* [lispbuilder-sdl](https://github.com/lispbuilder/lispbuilder) [![GitHub stars](https://img.shields.io/github/stars/lispbuilder/lispbuilder?style=flat)](https://github.com/lispbuilder/lispbuilder/stargazers) - A set of bindings for SDL. [Expat][14].
* [lisp-magick-wand](https://github.com/ruricolist/lisp-magick-wand) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/lisp-magick-wand?style=flat)](https://github.com/ruricolist/lisp-magick-wand/stargazers) - ImageMagick bindings. [BSD][15]. Not in Quicklisp.
* [okra](https://www.common-lisp.net/project/okra/manual.html) - CFFI bindings to Ogre. Not available on Quicklisp. [3-clause BSD][15].
* [cl-cuda](https://github.com/takagi/cl-cuda) [![GitHub stars](https://img.shields.io/github/stars/takagi/cl-cuda?style=flat)](https://github.com/takagi/cl-cuda/stargazers) - A library to use NVIDIA CUDA in Common Lisp programs. [LLGPL][8].

GUI
===

For an overview and a tutorial on GUI toolkits, see [the Cookbook/GUI](https://lispcookbook.github.io/cl-cookbook/gui.html).

* [LispWork's CAPI](http://www.lispworks.com/products/capi.html) - A portable GUI toolkit, with mobile runtime. Proprietary, but comes with a free version.
* [Allegro's Common Graphics](https://franz.com/products/allegro-common-lisp/acl_gui_tools.lhtml)- a library of functions for writing windowized GUIs for Windows, Mac and Linux. Proprietary with a free version.
  - since Allegro 10.1 (March, 2022), the IDE and the Common Graphics toolkit [runs in the browser](https://franz.com/ftp/pri/acl/cgjs/doc.html).
* 🆕 [cl-gtk4](https://github.com/bohonghuang/cl-gtk4) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/cl-gtk4?style=flat)](https://github.com/bohonghuang/cl-gtk4/stargazers) -  GTK4/Libadwaita/WebKit binding for Common Lisp. [LGPL3][9].
* [cl-cffi-gtk](https://github.com/crategus/cl-cffi-gtk) [![GitHub stars](https://img.shields.io/github/stars/crategus/cl-cffi-gtk?style=flat)](https://github.com/crategus/cl-cffi-gtk/stargazers) - Binding for GTK+3. [GNU LGPL2.1][11].
  - a tutorial: [Learn Common Lisp by Example: GTK GUI with SBCL](https://dev.to/goober99/learn-common-lisp-by-example-gtk-gui-with-sbcl-5e5c)
* [Qtools](https://codeberg.org/shinmera/qtools/) - A Qt toolkit, based on CommonQt. [zlib][33] Also [Qtools-ui](https://codeberg.org/shinmera/qtools-ui) (premade UI components), with [videos](https://www.youtube.com/watch?v=KwASFOhYta4&index=7&list=PLkDl6Irujx9Mh3BWdBmt4JtIrwYgihTWp).
* [CommonQt](https://github.com/commonqt/commonqt) [![GitHub stars](https://img.shields.io/github/stars/commonqt/commonqt?style=flat)](https://github.com/commonqt/commonqt/stargazers) - A Common Lisp binding for Qt4 via QtSmoke. [FreeBSD][39].
  * [CommonQt5](https://github.com/commonqt/commonqt5/) [![GitHub stars](https://img.shields.io/github/stars/commonqt/commonqt5/?style=flat)](https://github.com/commonqt/commonqt5//stargazers) - bindings for Qt5.
    * warn: currently difficult to install. Used in production© by SISCOG.
* ⭐ [ltk](http://www.peter-herth.de/ltk/) - A binding for the Tk toolkit. [LLGPL][8] or [GNU LGPL2.1][11].
  * [LTk Examples](https://peterlane.codeberg.page/ltk-examples/) - Provides LTk examples for the tkdocs tutorial.
  * [LTk Plotchart](https://peterlane.codeberg.page/ltk-plotchart/) - A wrapper around the tklib/plotchart library to work with LTk. This includes over 20 different chart types (xy-plots, gantt charts, 3d-bar charts etc...).
* [nodgui](https://codeberg.org/cage/nodgui) - Bindings for the Tk toolkit, based on Ltk, with syntax sugar and additional widgets. [LLGPL][8].
  * 🎨 supports [tk custom themes](https://wiki.tcl-lang.org/page/List+of+ttk+Themes), such as [ttkthemes](https://ttkthemes.readthedocs.io/en/latest/themes.html) and [Forest-ttk-theme](https://github.com/rdbende/Forest-ttk-theme) [![GitHub stars](https://img.shields.io/github/stars/rdbende/Forest-ttk-theme?style=flat)](https://github.com/rdbende/Forest-ttk-theme/stargazers).
  * supports an SDL frame as an alternative to the Tk canvas when fast rendering is needed. For 2D (pixel-based) and 3D rendering (using openGL).
* [IUP](https://github.com/lispnik/iup/) [![GitHub stars](https://img.shields.io/github/stars/lispnik/iup/?style=flat)](https://github.com/lispnik/iup//stargazers) - CFFI bindings to the [IUP](https://www.tecgraf.puc-rio.br/iup/) Portable User Interface library (pre-ALPHA).
  - IUP is cross-platform (Windows, macOS, GNU/Linux, with new Android, iOs, Cocoa and Web Assembly drivers), has many widgets, has a small api and is actively developed.
  - has a web view.
* 🆕 [Barium](https://tomscii.sig7.se/barium/) - an X widget toolkit, directly accessing the X client library and other platform libraries (OpenGL, Cairo). [MIT][200].
  * with menus, panes, tabs, dialogs, a file chooser, a flexible event loop…
  * not a wrapper of another toolkit. Allows incremental GUI development.
  * new as of April, 2025.

But that's not all.


* [CocoaInterface](https://github.com/plkrueger/CocoaInterface/) [![GitHub stars](https://img.shields.io/github/stars/plkrueger/CocoaInterface/?style=flat)](https://github.com/plkrueger/CocoaInterface//stargazers) -
Cocoa interface for Clozure Common Lisp. Build Cocoa user interface
windows dynamically using Lisp code and bypass the typical Xcode
processes. It has
[good documentation and a tutorial](https://github.com/plkrueger/CocoaInterface/blob/master/Documentation/UserInterfaceTutorial.pdf) [![GitHub stars](https://img.shields.io/github/stars/plkrueger/CocoaInterface/blob/master/Documentation/UserInterfaceTutorial.pdf?style=flat)](https://github.com/plkrueger/CocoaInterface/blob/master/Documentation/UserInterfaceTutorial.pdf/stargazers).
* [McCLIM](https://common-lisp.net/project/mcclim/) - An implementation of the Common Lisp Interface Manager, version II. [GNU LGPL2.1][11].
  * example project: a Lem editor CLIM interface: [discussion](https://github.com/lem-project/lem/discussions/1311#discussioncomment-10203860), [screenshot](https://framapiaf.org/@frescosecco@mastodon.social/112909105163460836).
  * [Anathema](https://codeberg.org/contrapunctus/anathema), a theme library for McCLIM applications. Unlicense.
    * *At time of reading (2026-05-18), it provides fonts and color changes. Doesn't change the rendering of widgets. Provides a Doom theme.*
  * [clim-modern](https://git.sr.ht/~hajovonta/clim-modern) - A theming library for McCLIM that replaces stock '90s Motif-style widgets with flat, modern-looking equivalents. Fully customizable via themes and per-widget style overrides. MIT. *Built with LLMs*.
* [cl-webkit](https://github.com/joachifm/cl-webkit) [![GitHub stars](https://img.shields.io/github/stars/joachifm/cl-webkit?style=flat)](https://github.com/joachifm/cl-webkit/stargazers) - A binding to WebKitGTK+. Also adds web browsing capabilities to an application, leveraging the full power of the WebKit browsing engine. [MIT][200].
* [ftw](https://github.com/fjames86/ftw) [![GitHub stars](https://img.shields.io/github/stars/fjames86/ftw?style=flat)](https://github.com/fjames86/ftw/stargazers) - A Win32 GUI library. [MIT][200].
* [eql, eql5, eql5-android](https://gitlab.com/eql) - Embedded Qt4 and Qt5 Lisp, embedded in ECL, embeddable in Qt. Port of EQL5 to the Android platform. [MIT][200].
  * [EQL5 on the Android store](https://play.google.com/store/apps/details?id=org.eql5.android.repl&pcampaignid=web_share)
* [bodge-nuklear](https://github.com/borodust/bodge-nuklear) [![GitHub stars](https://img.shields.io/github/stars/borodust/bodge-nuklear?style=flat)](https://github.com/borodust/bodge-nuklear/stargazers) - Wrapper over the [Nuklear](https://github.com/Immediate-Mode-UI/Nuklear) [![GitHub stars](https://img.shields.io/github/stars/Immediate-Mode-UI/Nuklear?style=flat)](https://github.com/Immediate-Mode-UI/Nuklear/stargazers) immediate mode GUI library. [MIT][200].
* [vk](https://github.com/JolifantoBambla/vk) [![GitHub stars](https://img.shields.io/github/stars/JolifantoBambla/vk?style=flat)](https://github.com/JolifantoBambla/vk/stargazers) -  Common Lisp/CFFI bindings for the Vulkan API. [MIT][200].
  * see also [cl-vulkan](https://github.com/awolven/cl-vulkan) [![GitHub stars](https://img.shields.io/github/stars/awolven/cl-vulkan?style=flat)](https://github.com/awolven/cl-vulkan/stargazers) - supports Vulkan 1.0 and 1.2, including compute pipelines. Vulkan 1.1 and 1.3 are coming soon©. MIT.
    * cl-vulkan currently supports SBCL and Clozure Common Lisp on Microsoft Windows, Linux and MacOS.

Other utilities:

* [file-select](https://codeberg.org/shinmera/file-select) -  A library to invoke the native system file dialog to select or create files. Zlib.

See also this [demo to use Java Swing from ABCL](https://github.com/defunkydrummer/abcl-jazz) [![GitHub stars](https://img.shields.io/github/stars/defunkydrummer/abcl-jazz?style=flat)](https://github.com/defunkydrummer/abcl-jazz/stargazers).

Web views
-----------

For Electron, see:

* [Electron-lisp-boilerplate](https://github.com/mikelevins/electron-lisp-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/mikelevins/electron-lisp-boilerplate?style=flat)](https://github.com/mikelevins/electron-lisp-boilerplate/stargazers) - a rudimentary boilerplate for building Electron apps that start a Lisp process.
* [ceramic](https://ceramic.github.io/) - a wrapper around simpler tools to create and build an Electron app for Common Lisp. It is currently broken and unmaintained, but some tools are workth having a look at.
* NOTE: the main idea in embedding a lisp web app in Electron is to start the lisp webserver as an async process from Electron's `main.js` file, and to point the Electron window to the localhost URL. That's it.

Read: [Three web views for Common Lisp](https://lisp-journey.gitlab.io/blog/three-web-views-for-common-lisp--cross-platform-guis/).

For other web views, see:

* [cl-webui](https://github.com/garlic0x1/cl-webui/) [![GitHub stars](https://img.shields.io/github/stars/garlic0x1/cl-webui/?style=flat)](https://github.com/garlic0x1/cl-webui//stargazers) - bindings for [webui](https://webui.me/), that allows to use any web browser or WebView as GUI.
* [clogframe](https://github.com/rabbibotton/clog/tree/main/clogframe) [![GitHub stars](https://img.shields.io/github/stars/rabbibotton/clog/tree/main/clogframe?style=flat)](https://github.com/rabbibotton/clog/tree/main/clogframe/stargazers) - an executable wrapper for webview.h, allowing to display any web application served by a Common Lisp server.
  * clogframe does *not* induce the use of the whole CLOG framework.


Mobile
------

* [LispWork's mobile runtime](http://www.lispworks.com/products/lw4mr.html) - Android and iOs.  Proprietary.
* [LQML](https://gitlab.com/eql/lqml) - a lightweight ECL binding to QML (both Qt5 and Qt6) derived from EQL5. LGPL and public domain.
* [sbcl-termux-build](https://github.com/bohonghuang/sbcl-termux-build/) [![GitHub stars](https://img.shields.io/github/stars/bohonghuang/sbcl-termux-build/?style=flat)](https://github.com/bohonghuang/sbcl-termux-build//stargazers) - Prebuilt SBCL binary for Android (Termux).

Also:

[hello-alien](https://github.com/Gleefre/hello-alien/) [![GitHub stars](https://img.shields.io/github/stars/Gleefre/hello-alien/?style=flat)](https://github.com/Gleefre/hello-alien//stargazers), SBCL built for an Android application.


Implementations
===============

* ⭐ [SBCL](http://www.sbcl.org/index.html) - Steel Bank Common Lisp. A fork of CMUCL; compiles to efficient machine code. [Standard compliance][13]. Public domain, with some parts under [Expat][14] and [3-clause BSD][15].
  * see also: [sbcl-librarian](https://github.com/quil-lang/sbcl-librarian) [![GitHub stars](https://img.shields.io/github/stars/quil-lang/sbcl-librarian?style=flat)](https://github.com/quil-lang/sbcl-librarian/stargazers) -  Dynamic library delivery tools for SBCL. Create shared libraries that can be called from C or Python. MIT. [Blog post](https://mstmetent.blogspot.com/2022/04/using-lisp-libraries-from-other.html). [Tutorial](https://lispcookbook.github.io/cl-cookbook/dynamic-libraries.html).
  * [SBCL-GOODIES](https://github.com/sionescu/sbcl-goodies) [![GitHub stars](https://img.shields.io/github/stars/sionescu/sbcl-goodies?style=flat)](https://github.com/sionescu/sbcl-goodies/stargazers) - Distributing binaries with Common Lisp and foreign libraries: libssl, libcrypto and libfixposix are statically baked in. [MIT][200].
  * [Nightly Windows builds of SBCL](https://github.com/olnw/sbcl-builds) [![GitHub stars](https://img.shields.io/github/stars/olnw/sbcl-builds?style=flat)](https://github.com/olnw/sbcl-builds/stargazers) -  Nightly builds of SBCL using MSYS2 UCRT64. See also [Roswell's SBCL MSI builds](https://github.com/roswell/sbcl_bin/releases/) [![GitHub stars](https://img.shields.io/github/stars/roswell/sbcl_bin/releases/?style=flat)](https://github.com/roswell/sbcl_bin/releases//stargazers).
  * [SBCL on Chocolatey for Windows](https://community.chocolatey.org/packages/sbcl) (unofficial)
  * [WIP, 2021] [Static Executables with SBCL](https://www.timmons.dev/posts/static-executables-with-sbcl-v2.html).
  * [SBCL Windows builds supporting Windows 7+](https://github.com/lockie/sbcl-w7) [![GitHub stars](https://img.shields.io/github/stars/lockie/sbcl-w7?style=flat)](https://github.com/lockie/sbcl-w7/stargazers), packaged into NSIS installer and updated monthly (unofficial)
  * *tip: to enhance the default terminal experience of SBCL, see also `icl` or `cl-repl` in the Editors section below.*
* ⭐ [CCL](https://ccl.clozure.com/) - Clozure Common Lisp; compiler-only implementation, generates native code.  [LLGPL][8].
* [ECL](https://common-lisp.net/project/ecl/) - Embeddable Common Lisp; compiles to C. [GNU LGPL2.1][11].
  * [cross compilation](https://ecl.common-lisp.dev/static/files/manual/current-manual/System-building.html#Cross-compilation)
    * [blog report: porting Maxima to iOS](https://li-yiyang.github.io/lisp/imaxima/).
  * WASM support in development ([NLNET grant in 2025](https://nlnet.nl/project/ECL/))
  * [eclweb](https://github.com/chee/eclweb) [![GitHub stars](https://img.shields.io/github/stars/chee/eclweb?style=flat)](https://github.com/chee/eclweb/stargazers) is [a proof-of-concept REPL inside a browser](https://repl.chee.party/) using Web Assembly (WASM).
* [ABCL](https://common-lisp.net/project/armedbear/) - Armed Bear Common Lisp; targets the JVM, compiles to bytecode. [Standard conformance][4]. [GNU GPL3][2] with [Classpath exception][3].
  * [abcl-memory-compiler](https://gitlab.com/cl-projects/abcl-memory-compiler) - a way to compile Java source code to create Java classes at runtime with ABCL. [Apache2][89].
  * [py4abcl](https://gitlab.com/cl-projects/py4abcl) - communicate with Python in ABCL.
* [CLASP](https://github.com/drmeister/clasp) [![GitHub stars](https://img.shields.io/github/stars/drmeister/clasp?style=flat)](https://github.com/drmeister/clasp/stargazers) - a new Common Lisp implementation that seamlessly interoperates with C++ libraries and programs using LLVM for compilation to native code. This allows Clasp to take advantage of a vast array of preexisting libraries and programs, such as out of the scientific computing ecosystem. [LGPL2.1][11] (and others).

Proprietary:

* [LispWorks](http://www.lispworks.com/) - an integrated cross-platform development tool for Common Lisp.
  * reputed features include: the CAPI cross-platform and native GUI toolkit, the LispWorks IDE, the mobile platforme runtime (iOs, Android), its Java interface, the tree shaker to build lighter binaries, its KnowledgeWorks system for "rule-based, object-oriented, logical, functional and database programming", and more.
  * has a free edition, with limitations (heap size limit, time limit).
* [Allegro CL](https://franz.com/products/allegro-common-lisp/) - provides the full ANSI Common Lisp standard with many extensions.
  * reputed features include: the AllegroCache object persistence database system, the KnowledgeGraph system, its concurrent garbage collector, its web-based IDE, and more.
  * has a free edition. It includes AllegroCache, with a size limit.
  * might be pricy. Licensed developers get access to much of the source code. Franz Inc. also publishes [open-source libraries](https://github.com/franzinc) [![GitHub stars](https://img.shields.io/github/stars/franzinc?style=flat)](https://github.com/franzinc/stargazers) (often tied to AllegroCL).

Other implementations, mainly for historical purposes:

* [CMUCL](http://www.cons.org/cmucl/) - An implementation from Carnegie Mellon University. Public domain. SBCL is a fork of CMUCL.
* [GNU CLISP](http://www.clisp.org/) - A GNU implementation; contains a compiler and an interpreter. [Standard conformance][6]. [GNU GPL3][2]. They develop [on Gitlab](https://gitlab.com/gnu-clisp/clisp).
  * compiles to bytecode, its default REPL is more user friendly than SBCL's (with symbol completion and readline integration).
  * however, it is not actively developed, it doesn't comply entirely to the ANSI standard, it is less performant than SBCL and it is lacking compatibility features.
* [Corman Lisp](https://github.com/sharplispers/cormanlisp) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/cormanlisp?style=flat)](https://github.com/sharplispers/cormanlisp/stargazers) - a Common Lisp development environment for Microsoft Windows running on Intel platforms. [MIT][200].

You can check the implementations' compatibility to common extensions here: [portability.cl](https://portability.cl).

See also:

* [cl-all](https://codeberg.org/shinmera/cl-all) - A script to run Lisp snippets in multiple implementations. This allows you to quickly compare implementation behaviour and differences. [zlib][33].

# Language libraries

## Lisp parsers

* [Eclector](https://github.com/s-expressionists/Eclector/) [![GitHub stars](https://img.shields.io/github/stars/s-expressionists/Eclector/?style=flat)](https://github.com/s-expressionists/Eclector//stargazers) - A portable Common Lisp reader that is highly customizable, can recover from errors and can return concrete syntax trees.
  * used in tools and libraries but still *under active development*
* [rewrite-cl](https://github.com/atgreen/rewrite-cl) [![GitHub stars](https://img.shields.io/github/stars/atgreen/rewrite-cl?style=flat)](https://github.com/atgreen/rewrite-cl/stargazers) - Read, modify, and write Common Lisp source code while preserving whitespace and comments. MIT. *Built with LLMs*.
* [cl-sourcery](https://sr.ht/~hajovonta/cl-sourcery/) - Intercepts all standard CL definition forms (defun, defmacro, defclass, defstruct, etc.) to capture and store the exact source as written — including whitespace, comments, and formatting. MIT. *Built with LLMs*.

See also:

* [breeze](https://github.com/fstamour/breeze/) [![GitHub stars](https://img.shields.io/github/stars/fstamour/breeze/?style=flat)](https://github.com/fstamour/breeze//stargazers) - experiments on workflows for Common Lisp. WIP.

## Tree-sitter grammars

* [tree-sitter-commonlisp](https://github.com/tree-sitter-grammars/tree-sitter-commonlisp) [![GitHub stars](https://img.shields.io/github/stars/tree-sitter-grammars/tree-sitter-commonlisp?style=flat)](https://github.com/tree-sitter-grammars/tree-sitter-commonlisp/stargazers) -  Common Lisp grammar for tree-sitter. MIT.
  * still Work In Progress.
* [tree-sitter-cl-syntax](https://codeberg.org/zshaftel/tree-sitter-cl-syntax) - another WIP grammar, ocused specifically on the syntax of the language.
  * with a grammar for `format` directives.

Language extensions
===================

* ⭐ [alexandria](https://common-lisp.net/project/alexandria/) - A general-purpose utility library. Public domain.
* 👍 [serapeum](https://github.com/ruricolist/serapeum/) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/serapeum/?style=flat)](https://github.com/ruricolist/serapeum//stargazers) - Another general-purpose utility library. [Expat][14].
* [rutils](https://github.com/vseloved/rutils) [![GitHub stars](https://img.shields.io/github/stars/vseloved/rutils?style=flat)](https://github.com/vseloved/rutils/stargazers) - radical yet reasonable syntactic utilities for Common Lisp. [MIT][200].
* [generic-cl](https://github.com/alex-gutev/generic-cl/) [![GitHub stars](https://img.shields.io/github/stars/alex-gutev/generic-cl/?style=flat)](https://github.com/alex-gutev/generic-cl//stargazers) - Generic function interface to standard Common Lisp functions (equality, comparison, arithmetic, objects, iterator, sequences,…). [MIT][200].
  * see also the more lightweight [equals](https://github.com/karlosz/equals/) [![GitHub stars](https://img.shields.io/github/stars/karlosz/equals/?style=flat)](https://github.com/karlosz/equals//stargazers) [MIT][200].
* [anaphora](https://common-lisp.net/project/anaphora/) - A collection of anaphoric macros. Public domain.
* [arrow-macros](https://github.com/hipeta/arrow-macros) [![GitHub stars](https://img.shields.io/github/stars/hipeta/arrow-macros?style=flat)](https://github.com/hipeta/arrow-macros/stargazers) - Clojure-like threading macros. [MIT][200].
* [hu.dwim.walker](https://github.com/hu-dwim/hu.dwim.walker) [![GitHub stars](https://img.shields.io/github/stars/hu-dwim/hu.dwim.walker?style=flat)](https://github.com/hu-dwim/hu.dwim.walker/stargazers) - a code walker and unwalker (aka AST parser and unparser). [BSD][15]. See also [this blog post](http://40ants.com/lisp-project-of-the-day/2020/04/0044-hu.dwim.walker.html).

Pattern matching
--------------------

* ⭐ [trivia](https://github.com/guicho271828/trivia/) [![GitHub stars](https://img.shields.io/github/stars/guicho271828/trivia/?style=flat)](https://github.com/guicho271828/trivia//stargazers) - Optimized pattern-matching library. [LLGPL][8].


Portability layers
------------------

A large list of portability layers is collected here: [portability.cl/](https://portability.cl/). Here are some of them:

* [trivial-arguments](https://codeberg.org/shinmera/trivial-arguments) - A portable library to retrieve the arguments list and argument types of a function. [zlib][33].
* [definitions](https://codeberg.org/shinmera/definitions) - a general definitions introspection library. It gives you the ability to retrieve definitions or bindings associated with designators such as symbols, packages, and names in general. [zlib][33].
* [DRef](https://github.com/melisgl/dref) [![GitHub stars](https://img.shields.io/github/stars/melisgl/dref?style=flat)](https://github.com/melisgl/dref/stargazers) - Another definition introspection library with extensive documentation, tests and an emphasis on extensibility. [MIT][200].
* [dissect](https://shinmera.github.io/dissect) - when a lot of projects use the “trivial-backtrace” system that just gives them a string with a backtrace, Dissect allows you to capture, step, and completely inspect the stack trace on a variety of Lisp implementations. Also very useful for logging and other situations where execution is automatically continued, but the information of the current stack is still useful to store somewhere. [zlib][33].

Changing the syntax
-------------------

* [cl-annot](https://github.com/m2ym/cl-annot) [![GitHub stars](https://img.shields.io/github/stars/m2ym/cl-annot?style=flat)](https://github.com/m2ym/cl-annot/stargazers) - Python-like annotations for Common Lisp. [LLGPL][8].
  * [cl-annot-revisit](https://github.com/y2q-actionman/cl-annot-revisit/) [![GitHub stars](https://img.shields.io/github/stars/y2q-actionman/cl-annot-revisit/?style=flat)](https://github.com/y2q-actionman/cl-annot-revisit//stargazers) -  re-implementation of cl-annot. WTFPL.
* [cl-reader](https://github.com/digikar99/reader) [![GitHub stars](https://img.shields.io/github/stars/digikar99/reader?style=flat)](https://github.com/digikar99/reader/stargazers) - A utility library intended at providing reader macros for lambdas, mapping, accessors, hash-tables and hash-sets. [MIT][200].
* [clamp](https://github.com/malisper/Clamp) [![GitHub stars](https://img.shields.io/github/stars/malisper/Clamp?style=flat)](https://github.com/malisper/Clamp/stargazers) - Arc language's brevity and conciseness to Common Lisp. [Artistic License 2.0][51].
  * also [arc-compat](https://github.com/g000001/arc-compat) [![GitHub stars](https://img.shields.io/github/stars/g000001/arc-compat?style=flat)](https://github.com/g000001/arc-compat/stargazers) -  Arc compatible package. Perl Foundation's Artistic Licence 2.0.

For strings:

* ⭐ [cl-interpol](https://github.com/edicl/cl-interpol/) [![GitHub stars](https://img.shields.io/github/stars/edicl/cl-interpol/?style=flat)](https://github.com/edicl/cl-interpol//stargazers) - A set of reader modifications to allow string interpolation. [BSD][15].
  * see also: [f-string](https://git.sr.ht/~dieggsy/f-string) for only string interpolation, with no dependencies. MIT.
* [mstrings](https://git.sr.ht/~shunter/mstrings) -  a reader macro to provide visually appealing multiline blocks. An M-string trims leading whitespace, concatenates lines together, etc. [BSD_3Clause][15].
* [pythonic-string-reader](https://github.com/smithzvk/pythonic-string-reader) [![GitHub stars](https://img.shields.io/github/stars/smithzvk/pythonic-string-reader?style=flat)](https://github.com/smithzvk/pythonic-string-reader/stargazers) - A simple and unobtrusive read table modification inspired by Python's three quote strings. [BSD_3Clause][15].
* [cl-heredoc](https://github.com/outergod/cl-heredoc) [![GitHub stars](https://img.shields.io/github/stars/outergod/cl-heredoc?style=flat)](https://github.com/outergod/cl-heredoc/stargazers) - a ["heredocs"](https://github.com/outergod/cl-heredoc) [![GitHub stars](https://img.shields.io/github/stars/outergod/cl-heredoc?style=flat)](https://github.com/outergod/cl-heredoc/stargazers) dispatcher. [GPL3][2]. Allows to write: `#>eof>Write whatever (you) "want", no matter what characters, until the magic end sequence has been reached.eof`

Experimental:

* [Moonli](https://gitlab.com/digikar/moonli) - a Julia/Python-ish syntax layer that transpiles to Common Lisp.
  * *experimental*. New as of 2025.

CLOS extensions
---------------

* ⭐ [closer-mop](https://github.com/pcostanza/closer-mop) [![GitHub stars](https://img.shields.io/github/stars/pcostanza/closer-mop?style=flat)](https://github.com/pcostanza/closer-mop/stargazers) - A compatibility layer that rectifies many absent or incorrect MOP features. [Expat][14].
* [specialization-store](https://github.com/markcox80/specialization-store/) [![GitHub stars](https://img.shields.io/github/stars/markcox80/specialization-store/?style=flat)](https://github.com/markcox80/specialization-store//stargazers) - generic functions based on types. Simplified BSD License variant.
* [filtered-functions](https://github.com/pcostanza/filtered-functions) [![GitHub stars](https://img.shields.io/github/stars/pcostanza/filtered-functions?style=flat)](https://github.com/pcostanza/filtered-functions/stargazers) - enable the use of arbitrary predicates for selecting and applying methods. [MIT][200].
* [inlined-generic-function](https://github.com/guicho271828/inlined-generic-function) [![GitHub stars](https://img.shields.io/github/stars/guicho271828/inlined-generic-function?style=flat)](https://github.com/guicho271828/inlined-generic-function/stargazers) -
Bringing the speed of Static Dispatch to CLOS. [LLGPL][8].
* [static-dispatch](https://github.com/alex-gutev/static-dispatch) [![GitHub stars](https://img.shields.io/github/stars/alex-gutev/static-dispatch?style=flat)](https://github.com/alex-gutev/static-dispatch/stargazers) - allows standard generic function dispatch to be performed statically (at compile time) rather than dynamically (runtime). This is similar to what is known as "overloading" in languages such as C++ and Java. [MIT][200].
* [dynamic-mixins](https://github.com/rpav/dynamic-mixins) [![GitHub stars](https://img.shields.io/github/stars/rpav/dynamic-mixins?style=flat)](https://github.com/rpav/dynamic-mixins/stargazers) - simple, dynamic class combination. [BSD_2Clause][17].
* [fast-generic-functions](https://github.com/marcoheisig/fast-generic-functions) [![GitHub stars](https://img.shields.io/github/stars/marcoheisig/fast-generic-functions?style=flat)](https://github.com/marcoheisig/fast-generic-functions/stargazers) - Seal your generic functions for an extra boost in performance. [MIT][200].
* [polymorphic functions](https://github.com/digikar99/polymorphic-functions) [![GitHub stars](https://img.shields.io/github/stars/digikar99/polymorphic-functions?style=flat)](https://github.com/digikar99/polymorphic-functions/stargazers) - A function type to dispatch on types instead of classes with partial support for dispatching on optional and keyword argument types. Still experimental (May, 2021). [MIT][200].
  - polymorphic-functions dispatch on the types of the arguments supplied to it. This helps dispatching on specialized arrays as well as user-defined types.
  - for differences with specialization-store and fast-generic-functions, see its README.

Writing terser defclass forms:

* [defclass-std](https://github.com/lisp-maintainers/defclass-std) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/defclass-std?style=flat)](https://github.com/lisp-maintainers/defclass-std/stargazers) - a shortcut macro to write DEFCLASS and PRINT-OBJECT forms quickly. [LLGPL][8].
* [nclasses](https://github.com/atlas-engineer/nclasses) [![GitHub stars](https://img.shields.io/github/stars/atlas-engineer/nclasses?style=flat)](https://github.com/atlas-engineer/nclasses/stargazers) - Syntactic sugar for class and generic function declarations. Features type inference, automatic accessors, inline initform syntax, automatic exports, and other conveniences. [BSD][15].

And also:

* [slot-extra-options](https://github.com/some-mthfka/slot-extra-options) [![GitHub stars](https://img.shields.io/github/stars/some-mthfka/slot-extra-options?style=flat)](https://github.com/some-mthfka/slot-extra-options/stargazers) - lets you build a metaclass which in turn lets you specify extra slot options in its classes. [LGPL3][9].

Function extensions
-------------------

* [cl-hooks](https://github.com/scymtym/architecture.hooks/) [![GitHub stars](https://img.shields.io/github/stars/scymtym/architecture.hooks/?style=flat)](https://github.com/scymtym/architecture.hooks//stargazers) - Hooks extension point mechanism (as known, e.g., from GNU Emacs). LGPL.
* [method-hooks](https://gitlab.com/Gnuxie/method-hooks) - When CLOS method combination allow only one hook per method, this library allows an arbitrary number of them. Mozilla Public Licence.
* [cl-advice](https://github.com/lisp-mirror/budden-tools/blob/213ab2b52a1b0c0b496efd30c3b5143f5c8e1ff2/cl-advice/README.md) [![GitHub stars](https://img.shields.io/github/stars/lisp-mirror/budden-tools/blob/213ab2b52a1b0c0b496efd30c3b5143f5c8e1ff2/cl-advice/README.md?style=flat)](https://github.com/lisp-mirror/budden-tools/blob/213ab2b52a1b0c0b496efd30c3b5143f5c8e1ff2/cl-advice/README.md/stargazers) - an attempt of portable layer advice library for SBCL, CCL, LispWorks and Allegro. Not in Quicklisp.
* [nhooks](https://github.com/atlas-engineer/nhooks) [![GitHub stars](https://img.shields.io/github/stars/atlas-engineer/nhooks?style=flat)](https://github.com/atlas-engineer/nhooks/stargazers) - an enhanced implementation of hooks (extension points) with crucial improvements.

Iteration
---------

* ⭐ [iterate](https://common-lisp.net/project/iterate/) - An iteration construct for Common Lisp which is extensible and Lispier. [MIT][200].
* [Khazern](https://github.com/s-expressionists/Khazern) [![GitHub stars](https://img.shields.io/github/stars/s-expressionists/Khazern?style=flat)](https://github.com/s-expressionists/Khazern/stargazers) - An implementation of CL:LOOP that can be used in any CL implementation without replacing the core CL:LOOP, is extensible and has a "batteries included" extension system with many useful iteration constructs.
* [for](https://shinmera.github.io/for/) - A concise, lispy and extensible iteration macro. It is extensible and sensible, and unlike iterate it does not require code-walking and is easier to extend. [zlib][33].
* [series](https://series.sourceforge.net/) - Functional style without any runtime penalty at all. [MIT][200].
* [trivial-do](https://github.com/yitzchak/trivial-do/) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/trivial-do/?style=flat)](https://github.com/yitzchak/trivial-do//stargazers) -  Additional dolist style macros for Common Lisp. [MIT][200].
* [doplus](https://github.com/alessiostalla/doplus) [![GitHub stars](https://img.shields.io/github/stars/alessiostalla/doplus?style=flat)](https://github.com/alessiostalla/doplus/stargazers) – another extensible iteration library, similar to :for.
* [cl-transducers](https://github.com/fosskers/cl-transducers/) [![GitHub stars](https://img.shields.io/github/stars/fosskers/cl-transducers/?style=flat)](https://github.com/fosskers/cl-transducers//stargazers) - Ergonomic, efficient data processing. [LGPL3][9].
  * "Transducers are an ergonomic and extremely memory-efficient way to process a data source. Here “data source” means simple collections like Lists or Vectors, but also potentially large files or generators of infinite data."
  * "It is, in general, the most complete implementation of the Transducer pattern."
  * a "modern" API with `map`, `filter`, `take`, `repeat`, `cycle`, `fold`…
* [snakes](https://github.com/BnMcGn/snakes) [![GitHub stars](https://img.shields.io/github/stars/BnMcGn/snakes?style=flat)](https://github.com/BnMcGn/snakes/stargazers) - Python style generators for Common Lisp. Includes a port of itertools. [Apache2][89].
* [picl](https://github.com/anlsh/picl) [![GitHub stars](https://img.shields.io/github/stars/anlsh/picl?style=flat)](https://github.com/anlsh/picl/stargazers) - An (almost) complete port of Python's itertools package, complete with laziness where applicable, and not relying on cl-cont. [MIT][200].
* [gtwiwtg](https://cicadas.surf/cgit/colin/gtwiwtg.git/about/) - A lazy sequences library. Similar to 'series' but not as complete. However it has a 'modern' API with stuff like `take`, `filter`, `for`, `fold`, etc. that is easy to use.
* [gmap](https://github.com/slburson/misc-extensions) [![GitHub stars](https://img.shields.io/github/stars/slburson/misc-extensions?style=flat)](https://github.com/slburson/misc-extensions/stargazers) - A concise and extensible iteration facility that has the advantage of integrating well with FSet (see the Data Structures section), as it was written by the same author. In Quicklisp as part of `misc-extensions`. Public domain.


Lambda shorthands
-----------------

* [fn](https://github.com/cbaggers/fn) [![GitHub stars](https://img.shields.io/github/stars/cbaggers/fn?style=flat)](https://github.com/cbaggers/fn/stargazers) - a couple of lambda shorthand macros. `(fn* (+ _ _))  -->  (lambda (_) (+ _ _))`. Public domain.
* [f-underscore](https://gitlab.common-lisp.net/bpm/f-underscore) - a tiny library of functional programming utils. `(f_ (+ _ _)) -> (lambda (_) (+ _ _))`. Public domain.
* [cl-punch](https://github.com/windymelt/cl-punch/) [![GitHub stars](https://img.shields.io/github/stars/windymelt/cl-punch/?style=flat)](https://github.com/windymelt/cl-punch//stargazers) - Scala-like anonymous lambda literals. `(mapcar ^(* 2 _) '(1 2 3 4 5))`. [MIT][200].


See also [Rutils](https://github.com/vseloved/rutils) [![GitHub stars](https://img.shields.io/github/stars/vseloved/rutils?style=flat)](https://github.com/vseloved/rutils/stargazers).


Non-deterministic, logic programming
------------------------------------

* [cl-prolog2](https://github.com/guicho271828/cl-prolog2) [![GitHub stars](https://img.shields.io/github/stars/guicho271828/cl-prolog2?style=flat)](https://github.com/guicho271828/cl-prolog2/stargazers) - Common Interface to ISO Prolog implementations from Common Lisp. [MIT][200].
* [Screamer](https://github.com/nikodemus/screamer) [![GitHub stars](https://img.shields.io/github/stars/nikodemus/screamer?style=flat)](https://github.com/nikodemus/screamer/stargazers) - augment Common
  Lisp with practically all of the functionality of both Prolog and
  constraint logic programming
  languages. [Blog post](https://chriskohlhepp.wordpress.com/reasoning-systems/specification-driven-programming-in-common-lisp/)
  solving Project Euler puzzles. [MIT][200].
* [Screamer+](https://github.com/yakovzaytsev/screamer-plus) [![GitHub stars](https://img.shields.io/github/stars/yakovzaytsev/screamer-plus?style=flat)](https://github.com/yakovzaytsev/screamer-plus/stargazers) - increasing the expressiveness of SCREAMER. [MIT][200].
* [AP5](https://ap5.com/) - allows users to program in a model of first order logic or a relational database. 1989, updated 2024. Public domain.
* [Temperance](https://github.com/sjl/temperance) [![GitHub stars](https://img.shields.io/github/stars/sjl/temperance?style=flat)](https://github.com/sjl/temperance/stargazers) - logic programming. [MIT][200]. A focus on performance, with General Game Playing in mind.

Reactive programming
--------------------

* [Cells](https://github.com/kennytilton/cells) [![GitHub stars](https://img.shields.io/github/stars/kennytilton/cells?style=flat)](https://github.com/kennytilton/cells/stargazers) - an implementation of the dataflow programming paradigm, reactive spreadsheet-like expressiveness for CLOS. Used to build an [algebra learning system](http://tiltontec.com/). With [documentation](https://github.com/stefano/cells-doc/) [![GitHub stars](https://img.shields.io/github/stars/stefano/cells-doc/?style=flat)](https://github.com/stefano/cells-doc//stargazers). Lisp LGPL.
* [lwcells](https://github.com/kchanqvq/lwcells) [![GitHub stars](https://img.shields.io/github/stars/kchanqvq/lwcells?style=flat)](https://github.com/kchanqvq/lwcells/stargazers) - Light Weight Cells.
  * LWCELLS is a dataflow extension to Common Lisp. It maintains a consistent state of cells according to functions specifying their relation. LWCELLS is designed to be simple, clean, compositional and flexible.
* NEW (2025) · [live-cells](https://github.com/alex-gutev/live-cells-cl/) [![GitHub stars](https://img.shields.io/github/stars/alex-gutev/live-cells-cl/?style=flat)](https://github.com/alex-gutev/live-cells-cl//stargazers) -  A reactive programming library for Lisp. BSD_3Clause.


Contract programming
--------------------

* [quid-pro-quo](https://github.com/sellout/quid-pro-quo) [![GitHub stars](https://img.shields.io/github/stars/sellout/quid-pro-quo?style=flat)](https://github.com/sellout/quid-pro-quo/stargazers) - a contract
  programming library in the style of Eiffel’s Design by Contract ™. Public domain.

Typing
------

* 👍 [Coalton](https://github.com/coalton-lang/coalton/) [![GitHub stars](https://img.shields.io/github/stars/coalton-lang/coalton/?style=flat)](https://github.com/coalton-lang/coalton//stargazers) - an efficient, statically typed functional programming language that supercharges Common Lisp. [MIT][200].
  * focuses on high-performance, built-in advanced mathematics, a numerical tower more powerful and extensible than Lisp's:
    * arbitrary precision floats, exact computable real arithmetic, transfinite numbers, [dual numbers](https://coalton-lang.github.io/reference/#coalton-library/math/dual-package) and [hyperdual numbers](https://coalton-lang.github.io/reference/#coalton-library/math/hyperdual-package),
  * [flime](https://github.com/fukamachi/flime) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/flime?style=flat)](https://github.com/fukamachi/flime/stargazers) - Real-time, project-wide Coalton compilation with isolated processes for LSP integration. [MIT][200].
  * [tokyo-tojo-json](https://github.com/tojoqk/tokyo.tojo.json) [![GitHub stars](https://img.shields.io/github/stars/tojoqk/tokyo.tojo.json?style=flat)](https://github.com/tojoqk/tokyo.tojo.json/stargazers) - a JSON parser implemented in Coalton.
  * [coalton-threads](https://github.com/garlic0x1/coalton-threads) [![GitHub stars](https://img.shields.io/github/stars/garlic0x1/coalton-threads?style=flat)](https://github.com/garlic0x1/coalton-threads/stargazers) - primitive thread and concurrency operations for Coalton.
  * [coalton-io](https://github.com/Jason94/coalton-io) [![GitHub stars](https://img.shields.io/github/stars/Jason94/coalton-io?style=flat)](https://github.com/Jason94/coalton-io/stargazers) - Functional IO interfaces. Includes terminal IO, file system IO, random variables, mutable variables, multithreading, and safely sharing state between threads.
  * [mine editor](https://coalton-lang.github.io/mine/) - an integrated development environment for Coalton and Common Lisp for Windows, macOS, and Linux.
  * [Lem editor mode for Coalton](https://lem-project.github.io/modes/coalton-lang/) - syntax highlighting, code completion, autodoc, interactive compilation commands (`coalton-compile-defun`, `C-c C-c`).
  * [Slime contrib for Coalton](https://github.com/slime/slime/pull/919) [![GitHub stars](https://img.shields.io/github/stars/slime/slime/pull/919?style=flat)](https://github.com/slime/slime/pull/919/stargazers) - shows type signatures. With a short demo video.
  * [Coalton.app playground](https://coalton.app/) - a web-based REPL for Coalton. [blog post announce](https://abacusnoir.com/2025/08/12/coalton-playground-type-safe-lisp-in-your-browser/).
  * [smelter](https://smelter.app/) - a zero setup Coalton (and CL) scripts runner, with some batteries (JSON, HTTP, filesystem, process utilities).
* 👍 [trivial-types](https://github.com/m2ym/trivial-types) [![GitHub stars](https://img.shields.io/github/stars/m2ym/trivial-types?style=flat)](https://github.com/m2ym/trivial-types/stargazers) - provides missing but important type definitions such as `proper-list`, `association-list`, `property-list` and `tuple`. [LLGPL][8].
* [defstar](https://bitbucket.org/eeeickythump/defstar/src/master/) - a collection of macros for easy inclusion of type declarations for arguments in lambda lists. [GNU GPL3][2]
* [algebraic-data-types](https://github.com/stylewarning/cl-algebraic-data-type) [![GitHub stars](https://img.shields.io/github/stars/stylewarning/cl-algebraic-data-type?style=flat)](https://github.com/stylewarning/cl-algebraic-data-type/stargazers) - defining algebraic data types in a similar spirit to Haskell or Standard ML, as well as for operating on them. [BSD_3Clause][15].

See also:

* [typo](https://github.com/marcoheisig/Typo/) [![GitHub stars](https://img.shields.io/github/stars/marcoheisig/Typo/?style=flat)](https://github.com/marcoheisig/Typo//stargazers) -  A portable type inference library for Common Lisp. [MIT][200].
* experimental: [PELTADOT](https://gitlab.com/digikar/peltadot/) - PELTADOT Extends Lisp’s Types And Dispatches Over Them.

Theorem provers
-------------------

* [ACL2](https://www.cs.utexas.edu/users/moore/acl2/) - a logic and programming language in which you can model computer systems, together with a tool to help you prove properties of those models.
  * used in the industry since the 1990s.
  * it supports a subset of the ANSI standard Common Lisp programming language.
  * "Companies that have used ACL2 regularly include AMD, Centaur Technology, IBM, Intel, Kestrel Institute, Motorola/Freescale, Oracle and Rockwell Collins." ([source](https://royalsocietypublishing.org/doi/10.1098/rsta.2015.0399))
  * [Proofpad](https://github.com/calebegg/proof-pad/) [![GitHub stars](https://img.shields.io/github/stars/calebegg/proof-pad/?style=flat)](https://github.com/calebegg/proof-pad//stargazers), an online IDE for ACL2.
  * [ACL2-kernel](https://github.com/tani/acl2-kernel) [![GitHub stars](https://img.shields.io/github/stars/tani/acl2-kernel?style=flat)](https://github.com/tani/acl2-kernel/stargazers), a Jupyter Kernel for ACL2.
  * [Proceedings of the 19th International Workshop on the ACL2 theorem prover and its applications, 2025 (PDF)](https://cgi.cse.unsw.edu.au/~eptcs/Published/ACL2in2025/Proceedings.pdf)
* NASA's [PVS](https://pvs.csl.sri.com/), the Prototype Verification System, and [NASAlib](https://github.com/nasa/pvslib) [![GitHub stars](https://img.shields.io/github/stars/nasa/pvslib?style=flat)](https://github.com/nasa/pvslib/stargazers), a collection of formal development libraries.
  * its 63 top-level libraries span the fields of: real analysis, limits, continuity, derivatives, integrals; complex integration; directed graphs; exact real arithmetic including trig functions; interval arithmetic and numerical approximations; linear algebra; 2-D, 3-D, 4-D, and n-dimensional vectors… and more.

Learning and Tutorials
=====================

## Online ##

Beginner
--------

* [Learn X in Y minutes - Where X = Common Lisp](https://learnxinyminutes.com/docs/common-lisp/) - Small Common Lisp tutorial covering the essentials.
* [Lisp Koans][201] - The project guides the learner progressively through many Common Lisp language features.
* [Practical Common Lisp][206] - A good introductory text to Common Lisp, with practical examples.
  * better read with [a Firefox add-on: Practical-cl beautified](https://github.com/vale981/practical-cl-beautified) [![GitHub stars](https://img.shields.io/github/stars/vale981/practical-cl-beautified?style=flat)](https://github.com/vale981/practical-cl-beautified/stargazers).
  * translated in [Chinese simplified](https://binghe.github.io/pcl-cn/)
* [Common LISP: A Gentle Introduction to Symbolic Computation](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/dst/www/LispBook/index.html) - A nice introduction into the language.
* [Successful Lisp](http://successful-lisp.blogspot.com/) - A good book for beginners with some programming background.
* [Lisp Quickstart](https://cs.gmu.edu/~sean/lisp/LispTutorial.html) - A good tutorial to get up and code Common Lisp quickly.
* [Casting SPELs in LISP](http://www.lisperati.com/casting.html) - A fun way to learn LISP while reading a comic book.
* 📹 [Common Lisp Programming: from novice to effective developer](https://www.udemy.com/course/common-lisp-programming/?referralCode=2F3D698BBC4326F94358) - A learning video series on the Udemy platform (*full content under paid access*). By an active lisper and community contributor (@vindarel). [Github home](https://github.com/vindarel/common-lisp-course-in-videos/) [![GitHub stars](https://img.shields.io/github/stars/vindarel/common-lisp-course-in-videos/?style=flat)](https://github.com/vindarel/common-lisp-course-in-videos//stargazers).
  > Thanks for supporting my work on Udemy. I can send a free link to students, just contact me.

Intermediate
------------

* [The Common Lisp Cookbook](https://lispcookbook.github.io/cl-cookbook/)
* [Lisp Tips](https://github.com/lisp-tips/lisp-tips/issues/) [![GitHub stars](https://img.shields.io/github/stars/lisp-tips/lisp-tips/issues/?style=flat)](https://github.com/lisp-tips/lisp-tips/issues//stargazers) - A blog with useful tips and tricks.
* [Lisp project of the day](http://40ants.com/lisp-project-of-the-day/) - A blog showcasing many Lisp libraries.
* A gentle introduction to Compile-Time Computing - [Part 1](https://medium.com/@MartinCracauer/a-gentle-introduction-to-compile-time-computing-part-1-d4d96099cea0), [Part 2](https://medium.com/@MartinCracauer/a-gentle-introduction-to-compile-time-computing-part-2-cb0a46f6cfe8), [Part 3 (Safely dealing with scientific units of variables at compile time)](https://medium.com/@MartinCracauer/a-gentle-introduction-to-compile-time-computing-part-3-scientific-units-8e41d8a727ca)
* [Static type checking in the programmable programming language](https://medium.com/@MartinCracauer/static-type-checking-in-the-programmable-programming-language-lisp-79bb79eb068a)
* [Loving Common Lisp, or the Savvy Programmer's Secret Weapon](https://leanpub.com/lovinglisp) - Quick introduction to Common Lisp with many examples. A particular focus is on how to use Large Language Models (LLMs).

Advanced
--------

* [Let Over Lambda][156] - A book on advanced macro techniques. The first six chapters are available online.
* [On Lisp](http://www.paulgraham.com/onlisp.html) - Paul Graham's amazing book on Lisp macros (and other interesting things).
* [Programming Algorithms in Lisp](https://link.springer.com/book/10.1007/978-1-4842-6428-7) - Updated version of "[Programming Algorithms](https://leanpub.com/progalgs)"; A comprehensive guide to writing efficient programs with data structures and algorithms in Lisp.

And a couple learning resources for SBCL internals:

* [SBCL internals](https://simonsafar.com/2020/sbcl/)
* [sbcl-wiki](https://github.com/guicho271828/sbcl-wiki/wiki) [![GitHub stars](https://img.shields.io/github/stars/guicho271828/sbcl-wiki/wiki?style=flat)](https://github.com/guicho271828/sbcl-wiki/wiki/stargazers) - an open wiki to document SBCL's internals.


Coding platforms
----------------

* [Codewars](https://docs.codewars.com/languages/commonlisp/) - a code training platform, with Common Lisp support (SBCL).

Web Development
--------

* [Section on Web Development in The Common Lisp Cookbook](https://lispcookbook.github.io/cl-cookbook/web.html) - An introductory tutorial covering web server setup, routing, weblocks, templating, error handling, packaging, hot reloading, database connection, and deployment, amongst other topics in the current lisp web development ecosystem.
* NEW [Web Apps in Lisp: Know-how](https://web-apps-in-lisp.github.io/) - tutorial and reference material to build interactive web apps in Common Lisp. CC-BY.

Reference
---------

* NEW! [CL CommunitySpec](https://cl-community-spec.github.io/pages/index.html) - a rendition of the Common Lisp ANSI Specification draft.
  * with an interactive search, syntax highlighting! And open-source.
* NEW! [novaspec](https://novaspec.org/) - a modern rendition of the CL ANSI draft.
  * not open-source?
* [Common Lisp Quick Reference](http://clqr.boundp.org/index.html) - A distilled, pocket-size version of the ANSI CL spec. Available for download as a PDF.
* [CLHS](http://www.lispworks.com/documentation/lw50/CLHS/Front/index.htm) - The Common Lisp HyperSpec; the ANSI CL standard, in hypertext form.
* [CLOS MOP specification](https://clos-mop.hexstreamsoft.com/) - A modern public domain online version of chapters 5 and 6 of The Art of the Metaobject Protocol
* [Common Lisp Standard Draft (pdf)](https://franz.com/support/documentation/cl-ansi-standard-draft-w-sidebar.pdf) - The standard draft of the Common Lisp specifications, in a well formatted PDF with a sidebar.
  * also [dpans2texi](https://github.com/mmontone/dpans2texi/releases/) [![GitHub stars](https://img.shields.io/github/stars/mmontone/dpans2texi/releases/?style=flat)](https://github.com/mmontone/dpans2texi/releases//stargazers) - the standard draft converted to Texinfo and published as a well formatted PDF.
  * which can be read online: https://mmontone.github.io/dpans2texi/
* [Common Lisp the Language](http://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html) - The original standard for Common Lisp before the ANSI spec.
  * [CLtL2, in PDF format](https://github.com/mmontone/cltl2-doc) [![GitHub stars](https://img.shields.io/github/stars/mmontone/cltl2-doc?style=flat)](https://github.com/mmontone/cltl2-doc/stargazers)
* [Minispec](https://lamberta.github.io/minispec/) - A friendlier, but less-complete, version of CLHS. Also contains documentation for some commonly-used CL libraries (such as Alexandria).
* [Simplified Common Lisp reference](http://jtra.cz/stuff/lisp/sclr/index.html) - The simplified version of CLHS.
* [CDR](https://cdr.common-lisp.dev/) - Common Lisp Document Repository. a repository of documents that are of interest to the Common Lisp community. The most important property of a CDR document is that it will never change: if you refer to it, you can be sure that your reference will always refer to exactly the same document.
  - the Common Lisp Document Repository is hosted at [Zenodo](https://zenodo.org/communities/cdr/).

## Offline ##

The CLHS is available offline via an [archive](ftp://ftp.lispworks.com/pub/software_tools/reference/HyperSpec-7-0.tar.gz) and as doc sets in [Dash](https://kapeli.com/dash), [Zeal](https://zealdocs.org/) and [Velocity](https://velocity.silverlakesoftware.com/).

Beginner
--------

* [Land of Lisp](http://landoflisp.com/) - A fun, game-oriented introduction to Common Lisp.
* [Practical Common Lisp][206] - A good introductory text to Common Lisp, with practical examples.

Intermediate
------------

* [ANSI Common Lisp](http://www.paulgraham.com/acl.html) - A thorough, practical covering of the entire language, with exercises. Not recommended as a starter text, due to [some caveats][20].
* [Common Lisp Recipes](http://weitz.de/cl-recipes/) - **Common Lisp Recipes** is a collection of solutions to problems and answers to questions you are likely to encounter when writing real-world applications in Common Lisp. Published in 2015.

Advanced
--------

* [Let Over Lambda][156] - A book on advanced macro techniques. All eight chapters are available in the print copy.
* [Object-Oriented Programming in Common Lisp: A Programmer's Guide to CLOS][21] - An old, but very thorough book on CLOS.
* [Paradigms of Artificial Intelligence Programming: Case Studies in Common Lisp][157] - A book on programming AI that covers some advanced Lisp.
  * with a web version: [https://norvig.github.io/paip-lisp/](https://norvig.github.io/paip-lisp/#/)
  * [PAIP-lisp](https://github.com/norvig/paip-lisp) [![GitHub stars](https://img.shields.io/github/stars/norvig/paip-lisp?style=flat)](https://github.com/norvig/paip-lisp/stargazers) -  Lisp code for the textbook "Paradigms of Artificial Intelligence Programming".
* [Norvig's Lisp style](https://www.cs.umd.edu/~nau/cmsc421/norvig-lisp-style.pdf)
  * and [lisp-lang.org's style guide](https://lisp-lang.org/style-guide/)

Other books
-----------

* [Building Problem Solvers](https://www.qrg.northwestern.edu/BPS/readme.html) ([PDF](https://www.qrg.northwestern.edu/BPS/BPS-Searchable.pdf)) by Ken Forbus and Johan de Kleer, made available for free by MIT Press - a  unique book among standard artificial intelligence texts in combining science and engineering, theory and craft to describe the construction of AI reasoning systems, and including code illustrating the ideas.

Community
---------

* [/r/Common_Lisp](https://www.reddit.com/r/Common_Lisp/) - subreddit about Common Lisp
* [/r/learnlisp](https://www.reddit.com/r/learnlisp/) - a subreddit to ask questions and get help about Lisp
* [common-lisp.net](https://common-lisp.net)
* [Lisp Discord Server](https://discord.gg/hhk46CE)
* [#commonlisp](https://irclog.tymoon.eu/libera/%23commonlisp) on Libera Chat - main Common Lisp IRC channel.
* [#lisp](https://irclog.tymoon.eu/libera/%23lisp) on Libera Chat - IRC channel for all Lisp dialects.
* #clschool on Libera Chat - IRC channel for learning Common Lisp.
* #lispcafe on Libera Chat - IRC channel for off-topic discussions.
* [Planet Lisp](http://planet.lisp.org/) - A meta blog that collects the contents of various Lisp-related blogs.
* [Lisp Jabber/XMPP channel](https://xmpp.link/#lisp@conference.a3.pm?join)
* [Matrix-for-lispers](https://web.matrix-for-lispers.net/) - a space for chatting about different lisp topics with support for persistency, markdown, screenshots.
  * NEW as of May, 2026.
  * the registration token is `lisp-spelt-without-caps`. Click on "explore" to see all the available rooms.

Showcase
--------

* [lisp-lang.org](https://lisp-lang.org/)
* 🔥 [lisp-screenshots.org](https://www.lisp-screenshots.org/)
* [awesome-lisp-companies](https://github.com/azzamsa/awesome-lisp-companies/) [![GitHub stars](https://img.shields.io/github/stars/azzamsa/awesome-lisp-companies/?style=flat)](https://github.com/azzamsa/awesome-lisp-companies//stargazers)
* [cl-software](https://github.com/azzamsa/awesome-cl-software) [![GitHub stars](https://img.shields.io/github/stars/azzamsa/awesome-cl-software?style=flat)](https://github.com/azzamsa/awesome-cl-software/stargazers)

Library Manager
===============

* ⭐ [Quicklisp][16] - A library manager containing many libraries, with easy depencency management. [Expat][14].
  * [ql-https](https://github.com/rudolfochrist/ql-https) [![GitHub stars](https://img.shields.io/github/stars/rudolfochrist/ql-https?style=flat)](https://github.com/rudolfochrist/ql-https/stargazers) - shell out to cURL and use HTTPS by default.
  * [Quicklisp bundles](https://quicklisp.org/beta/bundles.html) -  self-contained sets of systems that are exported from Quicklisp and loadable without involving Quicklisp.
* [ocicl](https://github.com/ocicl/ocicl) [![GitHub stars](https://img.shields.io/github/stars/ocicl/ocicl?style=flat)](https://github.com/ocicl/ocicl/stargazers) - A modern dependency management tool with novel features. [MIT][200].
  * project-local dependencies, code linting, project scaffolding, LLM-generated summaries of changes between package versions
  * securely distributed packages over TLS, all software packaged as OCI-compliant artifacts, and more.
* [Ultralisp](http://ultralisp.org/) - A Quicklisp distribution which updates every 5 minutes and to which one can add his project in one click. [BSD][15].
* [Roswell](https://github.com/roswell/roswell) [![GitHub stars](https://img.shields.io/github/stars/roswell/roswell?style=flat)](https://github.com/roswell/roswell/stargazers) - a Lisp implementation installer, script launcher and more. [MIT][200].
* [Qlot](https://github.com/fukamachi/qlot) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/qlot?style=flat)](https://github.com/fukamachi/qlot/stargazers) - A project-local library installer, similar to Bundler or Virtualenv. [Expat][14].
  * how to [use it from the Lisp REPL](https://github.com/svetlyak40wt/qlot-without-roswell) [![GitHub stars](https://img.shields.io/github/stars/svetlyak40wt/qlot-without-roswell?style=flat)](https://github.com/svetlyak40wt/qlot-without-roswell/stargazers) without Roswell.
* [vend](https://github.com/fosskers/vend) [![GitHub stars](https://img.shields.io/github/stars/fosskers/vend?style=flat)](https://github.com/fosskers/vend/stargazers) - Just vendor your dependencies! [MPL-2.0][211].

see also:

* [CLPM](https://www.clpm.dev) - A package manager for Common Lisp that strives to cleanly separate the package manager process itself from the client image that uses it. [BSD_2Clause][17].
  * CLPM comes as a pre-built binary, supports HTTPS by default, supports installing multiple package versions, supports versioned systems, and more.
* [trivial-system-loader](https://github.com/atgreen/trivial-system-loader) [![GitHub stars](https://img.shields.io/github/stars/atgreen/trivial-system-loader?style=flat)](https://github.com/atgreen/trivial-system-loader/stargazers) -  A system installation/loading abstraction for Common Lisp.
  * play nice with people using another library manager than Quicklisp: instead of hard-coding `(ql:quickload :mysystem)`, use `(tsl:load-system :mysystem)`. tsl:load-system will first try to use ocicl if available, then quicklisp, then plain asdf:load-system.
* [Quicksys](https://lisp.com.br/quicksys/) - install systems from multiple Quicklisp distributions. [MIT][200].
* [Quickutil](https://github.com/stylewarning/quickutil) [![GitHub stars](https://img.shields.io/github/stars/stylewarning/quickutil?style=flat)](https://github.com/stylewarning/quickutil/stargazers) - A utility manager, similar to Quicklisp, but for small utilities rather than whole libraries. [3-clause BSD][15].

might help:

* [redist](https://github.com/shirakumo/redist) [![GitHub stars](https://img.shields.io/github/stars/shirakumo/redist?style=flat)](https://github.com/shirakumo/redist/stargazers) - facilities to produce Quicklisp distributions.
* [quick-patch](https://github.com/tdrhq/quick-patch/) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/quick-patch/?style=flat)](https://github.com/tdrhq/quick-patch//stargazers) -  easily override quicklisp projects without using git submodules. [MPL-2.0][211].
* [print-licenses](https://github.com/vindarel/print-licenses) [![GitHub stars](https://img.shields.io/github/stars/vindarel/print-licenses?style=flat)](https://github.com/vindarel/print-licenses/stargazers) - print licenses used by a project and its dependencies. [MIT][200].
* [asdf-dependency-graph](https://github.com/digikar99/asdf-dependency-graph/) [![GitHub stars](https://img.shields.io/github/stars/digikar99/asdf-dependency-graph/?style=flat)](https://github.com/digikar99/asdf-dependency-graph//stargazers) - A minimal wrapper around `dot` to generate an image of the dependencies graph.

## Interfaces to other package managers

* [linux-packaging](https://gitlab.com/ralt/linux-packaging) - build .deb, .rpm or .pkg packages for your application with a single ASDF declaration. Uses fpm under the hood. [MIT][200].
* [qldeb](https://github.com/ralt/qldeb) [![GitHub stars](https://img.shields.io/github/stars/ralt/qldeb?style=flat)](https://github.com/ralt/qldeb/stargazers) -  Quicklisp systems to debian packages, along with [deb-packager](https://github.com/ralt/deb-packager) [![GitHub stars](https://img.shields.io/github/stars/ralt/deb-packager?style=flat)](https://github.com/ralt/deb-packager/stargazers) (simply create a debian package by defining an s-expression). Both [MIT][200].
* [ql-to-deb](https://github.com/dimitri/ql-to-deb) [![GitHub stars](https://img.shields.io/github/stars/dimitri/ql-to-deb?style=flat)](https://github.com/dimitri/ql-to-deb/stargazers) -  Update cl-* debian packages from Quicklisp releases. WTFPL.
* [dh-quicklisp-buildapp](https://github.com/ralt/dh-quicklisp-buildapp) [![GitHub stars](https://img.shields.io/github/stars/ralt/dh-quicklisp-buildapp?style=flat)](https://github.com/ralt/dh-quicklisp-buildapp/stargazers) - debhelper utility to let you compile your quicklisp-based Common Lisp code into a buildapp binary in a .deb with almost no effort. [MIT][200].
* [cl-brewer](https://github.com/can3p/cl-brewer) [![GitHub stars](https://img.shields.io/github/stars/can3p/cl-brewer?style=flat)](https://github.com/can3p/cl-brewer/stargazers) - Homebrew formula builder for (command line) common lisp applications. Public domain.
* [flatpack-common-lisp](https://gitlab.com/ralph-schleicher/flatpak-common-lisp) - A BuildStream project for building Flatpak based runtime environments for Common Lisp applications.
* [alien-works-delivery](https://github.com/borodust/alien-works-delivery) [![GitHub stars](https://img.shields.io/github/stars/borodust/alien-works-delivery?style=flat)](https://github.com/borodust/alien-works-delivery/stargazers) - WIP system for delivering Common Lisp applications as executable bundles. For now it only supports AppImage format for Linux and MSIX for Windows, but .APK for Android and later MacOSX and iOS bundle formats are planned too.
* [cl-nix-lite](https://github.com/hraban/cl-nix-lite) [![GitHub stars](https://img.shields.io/github/stars/hraban/cl-nix-lite?style=flat)](https://github.com/hraban/cl-nix-lite/stargazers) -  Common Lisp module for Nix, without Quicklisp. [AGPL-3.0][51]


See also:

- [asdf-sbcl](https://github.com/smashedtoatoms/asdf-sbcl) [![GitHub stars](https://img.shields.io/github/stars/smashedtoatoms/asdf-sbcl?style=flat)](https://github.com/smashedtoatoms/asdf-sbcl/stargazers), a plugin for the universal package manager.
- 📹 [this Youtube video](https://www.youtube.com/watch?v=lGS4sr6AzKw) (by 40ants, 2023) on how to use alien-works-delivery and linux-packaging.

Network and Internet
====================

See [Cliki](http://www.cliki.net/Web) for more.

HTTP clients
------------
* 👍 [Dexador](https://github.com/fukamachi/dexador) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/dexador?style=flat)](https://github.com/fukamachi/dexador/stargazers) - An HTTP client, that aims at replacing Drakma. [MIT][200].
* [Carrier](https://github.com/orthecreedence/carrier) [![GitHub stars](https://img.shields.io/github/stars/orthecreedence/carrier?style=flat)](https://github.com/orthecreedence/carrier/stargazers) - A lightweight, async HTTP client built on top of cl-async and fast-http. [MIT][200].
* [fast-http](https://github.com/fukamachi/fast-http) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/fast-http?style=flat)](https://github.com/fukamachi/fast-http/stargazers) - A fast HTTP request/response parser for Common Lisp. [MIT][200].
* [http2](https://github.com/zellerin/http2/) [![GitHub stars](https://img.shields.io/github/stars/zellerin/http2/?style=flat)](https://github.com/zellerin/http2//stargazers) -  HTTP/2 implementation in Common Lisp. [MIT][200].


HTTP Servers
------------

* ⭐ [Hunchentoot](http://weitz.de/hunchentoot/) - A web server. [2-clause BSD][207]
* 👍[Clack](https://github.com/fukamachi/clack) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/clack?style=flat)](https://github.com/fukamachi/clack/stargazers) - A web application environment inspired by Rack and WSGI. [LLGPL][8].  Provides a unified interface to a webserver of choice (default is Hunchentoot). With more [getting started guide](https://jasom.github.io/clack-tutorial/posts/getting-started-with-clack/).
* [wookie](https://github.com/orthecreedence/wookie) [![GitHub stars](https://img.shields.io/github/stars/orthecreedence/wookie?style=flat)](https://github.com/orthecreedence/wookie/stargazers) - Asynchronous HTTP server. [Expat][14].
* [woo](https://github.com/fukamachi/woo) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/woo?style=flat)](https://github.com/fukamachi/woo/stargazers) - A fast non-blocking HTTP server on top of libev. [MIT][200].

See also:

* [portableaserve](https://github.com/sharplispers/portableaserve) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/portableaserve?style=flat)](https://github.com/sharplispers/portableaserve/stargazers) - an attempt to provide the functionality of Franz.com's [AllegroServe web server](https://github.com/franzinc/aserve) [![GitHub stars](https://img.shields.io/github/stars/franzinc/aserve?style=flat)](https://github.com/franzinc/aserve/stargazers) (open-source but tied to AllegroCL) to other lisp implementations.
  * the system named `aserve` on Quicklisp.
  * AllegroServe is open-source: LGPL2.1.
  * it provides:
    * HTTP/1.1 compliant web server capable of serving static and dynamic pages.
    * SSL for client an server, web proxy, CGI, chunking, compress and inflate files on the fly,
    * A publish function that builds a page from static and dynamic data and handles caching of the result, with access rights.
  * Allegro's [Aserve documentation](https://github.com/franzinc/aserve/blob/master/doc/aserve.md) [![GitHub stars](https://img.shields.io/github/stars/franzinc/aserve/blob/master/doc/aserve.md?style=flat)](https://github.com/franzinc/aserve/blob/master/doc/aserve.md/stargazers)
  * ! not all AllegroServe tests pass on portableaserve.
  * [zaserve](https://github.com/gendl/aserve) [![GitHub stars](https://img.shields.io/github/stars/gendl/aserve?style=flat)](https://github.com/gendl/aserve/stargazers) - a portable fork of AllegroServe [LLGPL][8].
* [cl-http2-protocol](https://github.com/akamai/cl-http2-protocol) [![GitHub stars](https://img.shields.io/github/stars/akamai/cl-http2-protocol?style=flat)](https://github.com/akamai/cl-http2-protocol/stargazers) (*archived*) - a pure Common Lisp transport agnostic implementation of the HTTP/2 protocol at draft-14. [MIT][200].

### Hunchentoot plugins

* 👍 [easy-routes](https://github.com/mmontone/easy-routes) [![GitHub stars](https://img.shields.io/github/stars/mmontone/easy-routes?style=flat)](https://github.com/mmontone/easy-routes/stargazers) - a routes handling system on top of Hunchentoot. It supports dispatch based on HTTP method, arguments extraction from the url path, decorators, url generation from route name, etc. [MIT][200].
* [hunchentoot-cgi](https://github.com/slyrus/hunchentoot-cgi) [![GitHub stars](https://img.shields.io/github/stars/slyrus/hunchentoot-cgi?style=flat)](https://github.com/slyrus/hunchentoot-cgi/stargazers) - a library for executing CGI scripts from the hunchentoot webserver. [BSD][207].
* [hunchentoot-multi-acceptor](https://github.com/moderninterpreters/hunchentoot-multi-acceptor/) [![GitHub stars](https://img.shields.io/github/stars/moderninterpreters/hunchentoot-multi-acceptor/?style=flat)](https://github.com/moderninterpreters/hunchentoot-multi-acceptor//stargazers) - Route multiple domains (virtual hosts) on a single hunchentoot acceptor using a single port. [Apache2.0][89].
* [hunchentoot-errors](https://github.com/mmontone/hunchentoot-errors) [![GitHub stars](https://img.shields.io/github/stars/mmontone/hunchentoot-errors?style=flat)](https://github.com/mmontone/hunchentoot-errors/stargazers) - Augments Hunchentoot error pages and logs with request and session information. [MIT][200].
* [hunchentoot-stuck-connection-monitor](https://github.com/avodonosov/hunchentoot-stuck-connection-monitor/) [![GitHub stars](https://img.shields.io/github/stars/avodonosov/hunchentoot-stuck-connection-monitor/?style=flat)](https://github.com/avodonosov/hunchentoot-stuck-connection-monitor//stargazers) - Monitors hunchentoot connections and logs the connections stuck in the same state for a long time.
  - offers an option to shutdown the stuck connections sockets manually or automatically, thus unblocking the connection threads and preventing thread and socket leakage. [BSD_2Clause][17].

Making Hunchentoot faster:

* [cl-tbnl-gserver-tmgr](https://github.com/mdbergmann/cl-tbnl-gserver-tmgr) [![GitHub stars](https://img.shields.io/github/stars/mdbergmann/cl-tbnl-gserver-tmgr?style=flat)](https://github.com/mdbergmann/cl-tbnl-gserver-tmgr/stargazers) -  Hunchentoot Gserver-based taskmanager. cl-gserver is an actor-like message-passing library (see below in "Actors pattern"). Experimental.
* [hunchentoot-recycling-taskmaster](https://github.com/y2q-actionman/hunchentoot-recycling-taskmaster) [![GitHub stars](https://img.shields.io/github/stars/y2q-actionman/hunchentoot-recycling-taskmaster?style=flat)](https://github.com/y2q-actionman/hunchentoot-recycling-taskmaster/stargazers) - a taskmaster implementation for Hunchentoot, aiming to improve connection establishment efficiency through thread-pooling and flexible thread count adjustment. BSD_2Clause.

### Clack plugins

* [tiny-routes](https://github.com/jeko2000/tiny-routes) [![GitHub stars](https://img.shields.io/github/stars/jeko2000/tiny-routes?style=flat)](https://github.com/jeko2000/tiny-routes/stargazers) -  A tiny routing library for Common Lisp targeting Clack. [BSD_3Clause][15].
* [clack-errors](https://github.com/eudoxia0/clack-errors) [![GitHub stars](https://img.shields.io/github/stars/eudoxia0/clack-errors?style=flat)](https://github.com/eudoxia0/clack-errors/stargazers) - Error page middleware for Clack. Unmaintained. [LLGPL][8].
* [clath](https://github.com/BnMcGn/clath) [![GitHub stars](https://img.shields.io/github/stars/BnMcGn/clath?style=flat)](https://github.com/BnMcGn/clath/stargazers) - a single sign-on
  middleware for Clack. It allows basic login with OAuth1.0a, OAuth2
  and OpenID. At the time of writing, it supports authentication from
  Google, Twitter, LinkedIn, StackExchange, Reddit and Github. [Apache2.0][89].
* [clack-pretend](https://github.com/BnMcGn/clack-pretend) [![GitHub stars](https://img.shields.io/github/stars/BnMcGn/clack-pretend?style=flat)](https://github.com/BnMcGn/clack-pretend/stargazers) - a testing
  and debugging tool for clack. [Apache2.0][89].
* [hismetic](https://github.com/dertuxmalwieder/cl-hismetic) [![GitHub stars](https://img.shields.io/github/stars/dertuxmalwieder/cl-hismetic?style=flat)](https://github.com/dertuxmalwieder/cl-hismetic/stargazers) - Security for Clack-based web applications. [Expat][14].
* [live-reload](https://github.com/knobo/live-reload) [![GitHub stars](https://img.shields.io/github/stars/knobo/live-reload?style=flat)](https://github.com/knobo/live-reload/stargazers) - Live reload prototype for clack. [LLGPL][8].
* [clack-static-asset-middleware](https://github.com/fisxoj/clack-static-asset-middleware) [![GitHub stars](https://img.shields.io/github/stars/fisxoj/clack-static-asset-middleware?style=flat)](https://github.com/fisxoj/clack-static-asset-middleware/stargazers) - a cache-busting static asset middleware for the clack. [MIT][200].
* [lack-expression-cache](https://github.com/daninus14/lack-compression-cache) [![GitHub stars](https://img.shields.io/github/stars/daninus14/lack-compression-cache?style=flat)](https://github.com/daninus14/lack-compression-cache/stargazers) -  lack middleware for compressing and caching static resources. MIT.
* [lack-rerouter](https://github.com/daninus14/lack-rerouter) [![GitHub stars](https://img.shields.io/github/stars/daninus14/lack-rerouter?style=flat)](https://github.com/daninus14/lack-rerouter/stargazers) -  lack middleware to reroute URIs of requests. MIT.
* [clack-cors](https://40ants.com/clack-cors/) - A Clack middleware to set CORS related HTTP headers. — Unlicense.
* [clack-promotheus](https://40ants.com/clack-prometheus/) - Clack middleware to serve stats in Prometheus format. Unlicense.


Web frameworks
--------------

* [Caveman](https://github.com/fukamachi/caveman) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/caveman?style=flat)](https://github.com/fukamachi/caveman/stargazers) - A powerful web framework. [LLGPL][8].
  Example projects: [Quickdocs](https://github.com/quickdocs) [![GitHub stars](https://img.shields.io/github/stars/quickdocs?style=flat)](https://github.com/quickdocs/stargazers)
* [ningle](https://github.com/fukamachi/ningle) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/ningle?style=flat)](https://github.com/fukamachi/ningle/stargazers) - A super-micro web framework. [LLGPL][8].
  - [jingle](https://github.com/dnaeon/cl-jingle) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/cl-jingle?style=flat)](https://github.com/dnaeon/cl-jingle/stargazers) - based on ningle, adds  bells and whistles, such as middlewares.
    - includes an OpenAPI and Swagger UI demo.
* [radiance](https://codeberg.org/shirakumo/radiance) - A web application environment and framework . [zlib][33].

REST-focused frameworks:

* 👍 [Snooze](https://github.com/joaotavora/snooze) [![GitHub stars](https://img.shields.io/github/stars/joaotavora/snooze?style=flat)](https://github.com/joaotavora/snooze/stargazers) - A RESTful web framework. Web server agnostic. Currently has support for Hunchentoot and Clack. Routes are just functions and HTTP conditions are just Lisp conditions. [LLGPL][8].
* [cl-rest-server](https://github.com/mmontone/cl-rest-server) [![GitHub stars](https://img.shields.io/github/stars/mmontone/cl-rest-server?style=flat)](https://github.com/mmontone/cl-rest-server/stargazers) - a library for writing REST web APIs. Features validation with schemas, annotations for logging, caching, permissions or authentication, documentation via Swagger, etc. [MIT][200].

See OpenAPI, OData and other libraries below.

### Isomorphic web frameworks

* [CLOG](https://github.com/rabbibotton/clog) [![GitHub stars](https://img.shields.io/github/stars/rabbibotton/clog?style=flat)](https://github.com/rabbibotton/clog/stargazers) - The Common Lisp Omnificent GUI. Uses web technology to produce graphical user interfaces for applications locally or remotely. [BSD_3Clause][15].
  - CLOG is based on the ideas of GNOGA, a framework the author wrote for Ada and used in commercial production code since 2013.
* [Weblocks (Reblocks)](https://github.com/40ants/reblocks) [![GitHub stars](https://img.shields.io/github/stars/40ants/reblocks?style=flat)](https://github.com/40ants/reblocks/stargazers) - A widgets-based framework with a built-in ajax update mechanism that "solves the JavaScript problem". [LLGPL][8].
  - example code bases: [Ultralisp](https://github.com/ultralisp/ultralisp/) [![GitHub stars](https://img.shields.io/github/stars/ultralisp/ultralisp/?style=flat)](https://github.com/ultralisp/ultralisp//stargazers), [krasnodar](https://github.com/lct23/krasnodar) [![GitHub stars](https://img.shields.io/github/stars/lct23/krasnodar?style=flat)](https://github.com/lct23/krasnodar/stargazers), a dashboard made for a hackaton (2024) ([demo video](https://diode.zone/videos/watch/9e379a86-c530-4e9d-b8be-7437b1f7200b)).
* [Interactive SSR](https://github.com/interactive-ssr/client/blob/master/main.org/) [![GitHub stars](https://img.shields.io/github/stars/interactive-ssr/client/blob/master/main.org/?style=flat)](https://github.com/interactive-ssr/client/blob/master/main.org//stargazers) - ISSR allows you to make interactive web pages without writing client scripting. No knowledge about Javascript or DOM is necessary.
  - it is not unlike Phoenix LiveView or Hotwire.

CLOG-based frameworks:

- [mold-desktop](https://codeberg.org/mmontone/mold-desktop) - a programmable desktop.
- [WIP] [clog-moldable-inspector](https://codeberg.org/khinsen/clog-moldable-inspector) - A moldable Common Lisp object inspector based on CLOG. The inspector is thus shown in a Web browser.


Parsing html
---------------
* 👍 [Plump][71] - A lenient HTML/XML parser, tolerant on malformed markup. [zlib][33]. Best used with [lquery][72] and [clss](https://codeberg.org/shinmera/CLSS).
* [cl-html5-parser](https://github.com/rotatef/cl-html5-parser) [![GitHub stars](https://img.shields.io/github/stars/rotatef/cl-html5-parser?style=flat)](https://github.com/rotatef/cl-html5-parser/stargazers) -  HTML5 parser for Common Lisp. GPL3.0.
  * a port of the Python library html5lib.
  * compared to Plump: Plump is a mix of an XML and an HTML parser and breaks on some HTML rules, while cl-html5-parser is a fully compliant HTML parser.

Sanitizing HTML:

* [cl-sanitize-html](https://github.com/atgreen/cl-sanitize-html/) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-sanitize-html/?style=flat)](https://github.com/atgreen/cl-sanitize-html//stargazers) - OWASP-style HTML sanitization library for Common Lisp, designed for safely rendering untrusted HTML content (like HTML emails or user-generated content). MIT.
  - partly LLM. [reddit announce](https://old.reddit.com/r/Common_Lisp/comments/1q30bqh/atgreenclsanitizehtml_a_common_lisp_library_for/).
  - related: [trivial-sanitize](https://codeberg.org/cage/trivial-sanitize)


Querying HTML/DOM, web scraping
---------------------------------------

* 👍 [lquery][72] - A jQuery-like HTML/DOM manipulation library. [zlib][33].
* [scrapycl](https://40ants.com/scrapycl/) - web scraping framework for writing crawlers in Common Lisp. Unlicense.
  * relying on lquery.

See also the XML section below for xpath libraries and more.


HTML generators and templates
-----------------------------

* 👍 [spinneret](https://github.com/ruricolist/spinneret) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/spinneret?style=flat)](https://github.com/ruricolist/spinneret/stargazers) - Common Lisp HTML5 generator. [Expat][14].
* ⭐ [cl-who](http://weitz.de/cl-who/) - The venerable HTML generator. [FreeBSD][39].
* ⭐ [Djula](https://github.com/mmontone/djula) [![GitHub stars](https://img.shields.io/github/stars/mmontone/djula?style=flat)](https://github.com/mmontone/djula/stargazers) - A port of Django's template engine to Common Lisp. [Expat][14].
  - [cl-djula-tailwind](https://github.com/rajasegar/cl-djula-tailwind) [![GitHub stars](https://img.shields.io/github/stars/rajasegar/cl-djula-tailwind?style=flat)](https://github.com/rajasegar/cl-djula-tailwind/stargazers) - use TailwindCSS classe in your Djula templates without any JavaScript or Node.js tooling.
  - [djula-template-designer](https://github.com/mmontone/djula-template-designer) [![GitHub stars](https://img.shields.io/github/stars/mmontone/djula-template-designer?style=flat)](https://github.com/mmontone/djula-template-designer/stargazers) - a template designer tool.
* [TEN](https://github.com/mmontone/ten) [![GitHub stars](https://img.shields.io/github/stars/mmontone/ten?style=flat)](https://github.com/mmontone/ten/stargazers) - the completness of Djula with the full usability of Common Lisp code in templates. [MIT][200].
* [cl-closure-template](https://github.com/archimag/cl-closure-template) [![GitHub stars](https://img.shields.io/github/stars/archimag/cl-closure-template?style=flat)](https://github.com/archimag/cl-closure-template/stargazers) - Implementation of Google's Closure templates, where compiling a template creates a function that generates the result. [LLGPL][8].
* [hsx](https://github.com/skyizwhite/hsx/) [![GitHub stars](https://img.shields.io/github/stars/skyizwhite/hsx/?style=flat)](https://github.com/skyizwhite/hsx//stargazers) - An easily composable HTML5 generation library with the most simplistic syntax. [MIT][200].
* [clip](https://shinmera.github.io/clip) - An HTML template processor where the templates are written in HTML. [zlib][33].
* [lsx](https://github.com/fukamachi/lsx/) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/lsx/?style=flat)](https://github.com/fukamachi/lsx//stargazers) and [markup](https://github.com/moderninterpreters/markup) [![GitHub stars](https://img.shields.io/github/stars/moderninterpreters/markup?style=flat)](https://github.com/moderninterpreters/markup/stargazers) - Two JSX-like templating engines, where HTML tags are Common Lisp code. `markup` comes with an Emacs package.

URI and IP handling
-------------------

* [quri](https://github.com/fukamachi/quri) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/quri?style=flat)](https://github.com/fukamachi/quri/stargazers) - Another URI library for
  Common Lisp. Supports userinfo, IPv6 hostname, encoding/decoding
  utilities,… [BSD_3Clause][15].
* [cl-slug](https://github.com/lisp-maintainers/cl-slug) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/cl-slug?style=flat)](https://github.com/lisp-maintainers/cl-slug/stargazers) - a small library to make slugs, mainly for URIs, transform in CamelCase, remove accentuation and punctuation, for english and beyond. [LLGPL][8].
* [netaddr](https://github.com/ynadji/netaddr) [![GitHub stars](https://img.shields.io/github/stars/ynadji/netaddr?style=flat)](https://github.com/ynadji/netaddr/stargazers) -  A network address manipulation library for Common Lisp. MIT.
  * for manipulating IP addresses, subnets, ranges, and sets. It is inspired by its namesake library in Python, netaddr.

Javascript
----------

* ⭐ [Parenscript](https://common-lisp.net/project/parenscript/) - A translator from Common Lisp to Javascript. [3-clause BSD][15]. See [Trident-mode](https://github.com/johnmastro/trident-mode.el) [![GitHub stars](https://img.shields.io/github/stars/johnmastro/trident-mode.el?style=flat)](https://github.com/johnmastro/trident-mode.el/stargazers), an Emacs mode that provides live interaction with the browser.[unlicence][5].
  * [paren6](https://github.com/BnMcGn/paren6/) [![GitHub stars](https://img.shields.io/github/stars/BnMcGn/paren6/?style=flat)](https://github.com/BnMcGn/paren6//stargazers) - a set of ES6 macros for Parenscript.
  * [paren-async](https://github.com/Junker/paren-async) [![GitHub stars](https://img.shields.io/github/stars/Junker/paren-async?style=flat)](https://github.com/Junker/paren-async/stargazers) async/await for Parenscript.
  * [paren-jquery](https://github.com/Junker/paren-jquery) [![GitHub stars](https://img.shields.io/github/stars/Junker/paren-jquery?style=flat)](https://github.com/Junker/paren-jquery/stargazers) - Jquery-style macros for Parenscript. MIT.
  * example: [ParenScript + Mithril demo](https://mmontone.codeberg.page/lisp-pwa/#!/home) for Progressive Web Apps (PWA) [2025].
  * example: [Building a Freecell game with ParenScript and Preact](https://nickfa.ro/wiki/Building_with_Parenscript_and_Preact) [2024].
* [JSCL](https://github.com/jscl-project/jscl) [![GitHub stars](https://img.shields.io/github/stars/jscl-project/jscl?style=flat)](https://github.com/jscl-project/jscl/stargazers) - A CL-to-JS compiler designed to be self-hosting from day one. GPL3.0.
  * full support of `format`([pull request](https://github.com/jscl-project/jscl/pull/525) [![GitHub stars](https://img.shields.io/github/stars/jscl-project/jscl/pull/525?style=flat)](https://github.com/jscl-project/jscl/pull/525/stargazers))
  * supports `loop`([tests](https://github.com/jscl-project/jscl/tree/master/tests/loop) [![GitHub stars](https://img.shields.io/github/stars/jscl-project/jscl/tree/master/tests/loop?style=flat)](https://github.com/jscl-project/jscl/tree/master/tests/loop/stargazers)) and `CLOS`([tests](https://github.com/jscl-project/jscl/blob/master/tests/clos.lisp) [![GitHub stars](https://img.shields.io/github/stars/jscl-project/jscl/blob/master/tests/clos.lisp?style=flat)](https://github.com/jscl-project/jscl/blob/master/tests/clos.lisp/stargazers))
  * [live playground](https://jscl-project.github.io/)
  * 🔥 [live JupyterLite playground](https://wiki3-ai.github.io/jscl-kernel/) (Wasm powered Jupyter running in the browser). Project source: [jscl-kernel](https://github.com/wiki3-ai/jscl-kernel) [![GitHub stars](https://img.shields.io/github/stars/wiki3-ai/jscl-kernel?style=flat)](https://github.com/wiki3-ai/jscl-kernel/stargazers).
* [CL-JavaScript](http://marijnhaverbeke.nl/cl-javascript/) - A translator from Javascript to Common Lisp. Not available on Quicklisp. [Expat][14].
* [parse-js](http://marijnhaverbeke.nl/parse-js/) - A package for parsing ECMAScript 3. [zlib][33].
* [remote-js](https://github.com/ceramic/remote-js) [![GitHub stars](https://img.shields.io/github/stars/ceramic/remote-js?style=flat)](https://github.com/ceramic/remote-js/stargazers) - send JavaScript from Common Lisp to a browser. [MIT][200].
* [sigil](https://github.com/BnMcGn/sigil) [![GitHub stars](https://img.shields.io/github/stars/BnMcGn/sigil?style=flat)](https://github.com/BnMcGn/sigil/stargazers) - A Parenscript to Javascript command line compiler and REPL. [MIT][200].

In development:

* [Valtan](https://github.com/cxxxr/valtan) [![GitHub stars](https://img.shields.io/github/stars/cxxxr/valtan?style=flat)](https://github.com/cxxxr/valtan/stargazers) -  Common Lisp to JavaScript compiler.
* [JACL](https://tailrecursion.com/JACL/) - an experimental Lisp system for the Web browser platform to explore new techniques for developing large Single Page Applications with Lisp.
* [SLip](https://lisperator.net/slip/) - an aspiring Common Lisp environment in the browser.
  * Self-hosting compiler, TCO, CLOS, structures, conditions, loop and format, JavaScript "FFI", green threads…
  * in-browser development environment inspired by Emacs and Slime based on [Ymacs](https://lisperator.net/ymacs/).
  * [Live demo](https://lisperator.net/s/slip/)!


Utilities for **React**:

* [cl-react](https://github.com/helmutkian/cl-react) [![GitHub stars](https://img.shields.io/github/stars/helmutkian/cl-react?style=flat)](https://github.com/helmutkian/cl-react/stargazers) -  Common Lisp (Parenscript) utilities for building web apps in ReactJs. MIT.
* [Panic](https://github.com/michaeljforster/panic) [![GitHub stars](https://img.shields.io/github/stars/michaeljforster/panic?style=flat)](https://github.com/michaeljforster/panic/stargazers), a Parenscript library for React. Not in Quicklisp. [MIT][200]. Its [TodoMVC example](https://github.com/40ants/todomvc/blob/common-lisp-example/examples/common-lisp-react/src/app.lisp) [![GitHub stars](https://img.shields.io/github/stars/40ants/todomvc/blob/common-lisp-example/examples/common-lisp-react/src/app.lisp?style=flat)](https://github.com/40ants/todomvc/blob/common-lisp-example/examples/common-lisp-react/src/app.lisp/stargazers).
* [Parenscriptx](https://github.com/jasom/parenscriptx) [![GitHub stars](https://img.shields.io/github/stars/jasom/parenscriptx?style=flat)](https://github.com/jasom/parenscriptx/stargazers) -  Parenscript Macros to aid generating react code. [MIT][200].
* [jscl-react](https://github.com/nilesr/jscl-react) [![GitHub stars](https://img.shields.io/github/stars/nilesr/jscl-react?style=flat)](https://github.com/nilesr/jscl-react/stargazers) -  A web framework for writing react components in common lisp using jscl. No license specified.

SDK for **[Datastar](https://data-star.dev/)**:

- [datastar-cl](https://github.com/fsmunoz/datastar-cl) [![GitHub stars](https://img.shields.io/github/stars/fsmunoz/datastar-cl?style=flat)](https://github.com/fsmunoz/datastar-cl/stargazers) - Datastar Common Lisp SDK.
  - online demo: https://dataspice.interlaye.red/


See also:

* [trident-mode](https://github.com/johnmastro/trident-mode.el) [![GitHub stars](https://img.shields.io/github/stars/johnmastro/trident-mode.el?style=flat)](https://github.com/johnmastro/trident-mode.el/stargazers), an Emacs minor mode for live Parenscript interaction.


Deployment
----------

* 👍 [deploy](https://shinmera.github.io/deploy) - A toolkit for binary deployment of Lisp applications, with extra support for foreign shared libraries. [zlib][33].
* [common-lisp-heroku-example](https://github.com/fstamour/common-lisp-heroku-example) [![GitHub stars](https://img.shields.io/github/stars/fstamour/common-lisp-heroku-example?style=flat)](https://github.com/fstamour/common-lisp-heroku-example/stargazers) -  Example of Common Lisp server on Heroku using Docker.
* [cube](https://github.com/xh4/cube) [![GitHub stars](https://img.shields.io/github/stars/xh4/cube?style=flat)](https://github.com/xh4/cube/stargazers) - Kubernetes client library for Common LISP generated from the Swagger specification. [MIT][200].
* [s2i-lisp](https://github.com/container-lisp/s2i-lisp) [![GitHub stars](https://img.shields.io/github/stars/container-lisp/s2i-lisp?style=flat)](https://github.com/container-lisp/s2i-lisp/stargazers) - Source-to-Image builder image based on CentOS or alternatively RHEL7 for building Common LISP images for OpenShift (and also Docker). It features an up-to-date SBCL with Quicklisp installation, SLIME or SLY integration and allows customization via environment variables. [Apache2][89]
* [cl-aws-runtime-test](https://github.com/y2q-actionman/cl-aws-custom-runtime-test) [![GitHub stars](https://img.shields.io/github/stars/y2q-actionman/cl-aws-custom-runtime-test?style=flat)](https://github.com/y2q-actionman/cl-aws-custom-runtime-test/stargazers) - An example of using Common Lisp (SBCL) as a custom runtime on AWS lambda. WTFPL.
* [40ants/ci](https://github.com/40ants/ci/) [![GitHub stars](https://img.shields.io/github/stars/40ants/ci/?style=flat)](https://github.com/40ants/ci//stargazers) -  Highly opionated Github Actions workflow builder for Common Lisp projects.
  * with: a linter, lisp critic, tests runner, test matrix, doc building, caching…
* [make-common-lisp-program](https://github.com/melusina-org/make-common-lisp-program/) [![GitHub stars](https://img.shields.io/github/stars/melusina-org/make-common-lisp-program/?style=flat)](https://github.com/melusina-org/make-common-lisp-program//stargazers) -  GitHub action to build an executable Common Lisp program on Ubuntu, MacOS and Windows. MIT.

See also:

- [Cloud Init file for SBCL](https://git.sr.ht/%7Emarcuskammer/cloudinit/tree/main/item/sbcl-nginx.yml) - an init file for providers supporting the cloudinit format (DigitalOcean etc).

### Hosting platforms

We can host Common Lisp services on any server. These services offer
out of the box availability for CL:

- [Heliohost](https://www.heliohost.org/) for a free hosting solution.
- [Nearly Free Speech](https://www.nearlyfreespeech.net/) - 25+ programming languages, pay for what you use.
  - SBCL and GNU CLISP


Monitoring
----------

* [prometheus.cl](https://github.com/deadtrickster/prometheus.cl) [![GitHub stars](https://img.shields.io/github/stars/deadtrickster/prometheus.cl?style=flat)](https://github.com/deadtrickster/prometheus.cl/stargazers) - Prometheus.io client. Grafana dashboard for SBCL and Hunchentoot metrics (memory, threads, requests per second,…). [MIT][200].
  * [prometheus-g](https://github.com/40ants/prometheus-gc) [![GitHub stars](https://img.shields.io/github/stars/40ants/prometheus-gc?style=flat)](https://github.com/40ants/prometheus-gc/stargazers) - Extension for prometheus.cl which collects metrics about garbage collector state.
* [lisp-sentry](https://gitlab.com/lockie/lisp-sentry) - A full-featured Common Lisp client library for Sentry application monitoring software. MIT.
  * light in dependencies, provides Sentry with source code in stack traces, supports  file attachments, event breadcrumbs, automatically populated execution contexts, threads and user reports, GPU information.
  * supports only SBCL
* [cl-sentry-client](https://github.com/mmontone/cl-sentry-client) [![GitHub stars](https://img.shields.io/github/stars/mmontone/cl-sentry-client?style=flat)](https://github.com/mmontone/cl-sentry-client/stargazers) - a Sentry client for Common Lisp, the cloud-based error monitoring system. [MIT][200].
  * based on dexador for HTTP communication and swank for stack traces. It also features an async HTTP client via the simple-tasks library.
* [rollbar.lisp](https://github.com/adventuring/rollbar.lisp) [![GitHub stars](https://img.shields.io/github/stars/adventuring/rollbar.lisp?style=flat)](https://github.com/adventuring/rollbar.lisp/stargazers) - interface to [Rollbar.com](https://rollbar.com/), an error tracking software.


Websockets
----------

* 👍 [usocket](https://github.com/usocket/usocket) [![GitHub stars](https://img.shields.io/github/stars/usocket/usocket?style=flat)](https://github.com/usocket/usocket/stargazers) - A portable TCP and UDP socket interface. [Expat][14].
* [Portal](https://github.com/charJe/portal) [![GitHub stars](https://img.shields.io/github/stars/charJe/portal?style=flat)](https://github.com/charJe/portal/stargazers) - Portable websockets for Common Lisp, using usocket. [LLGPL][8].
* [clws](https://github.com/3b/clws) [![GitHub stars](https://img.shields.io/github/stars/3b/clws?style=flat)](https://github.com/3b/clws/stargazers) -  websockets server in CL, built on IOlib and libfixposix. MIT.
* [Hunchensocket](https://github.com/joaotavora/hunchensocket) [![GitHub stars](https://img.shields.io/github/stars/joaotavora/hunchensocket?style=flat)](https://github.com/joaotavora/hunchensocket/stargazers) -  RFC6455 compliant WebSockets for Common Lisp, as an extension to Hunchentoot. [MIT][200].
* [websocket-driver](https://github.com/fukamachi/websocket-driver) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/websocket-driver?style=flat)](https://github.com/fukamachi/websocket-driver/stargazers) - based on Clack.
* [iolib](https://github.com/sionescu/iolib) [![GitHub stars](https://img.shields.io/github/stars/sionescu/iolib?style=flat)](https://github.com/sionescu/iolib/stargazers) - I/O library. [Expat][14].
  * "IOlib is to be a better and more modern I/O library than the standard Common Lisp library. It contains: a socket library, a DNS resolver, an I/O multiplexer, a pathname library and file-system utilities."

*Editor's note: at the time of writing, it seems we don't have a full-featured websocket implementation for Common Lisp. We can however recommend Portal, and we invite you to double-check the current issues of Hunchensocket and websocket-driver.*

HTTPS
-----

- [pure-tls](https://github.com/atgreen/pure-tls) [![GitHub stars](https://img.shields.io/github/stars/atgreen/pure-tls?style=flat)](https://github.com/atgreen/pure-tls/stargazers) -  Pure Common Lisp TLS 1.3 implementation, HTTPS server with automatic Let's Encrypt certificate. MIT
  - warn: new code, partly done with LLMs.
  - read:
    - [Building a TLS 1.3 implementation in Common Lisp](https://atgreen.github.io/repl-yell/posts/pure-tls/)
    - [Automatic TLS Certificates for Common Lisp with pure-tls/acme](https://atgreen.github.io/repl-yell/posts/pure-tls-acme/)


Web development utilities
-------------------------

### Browser tests

* [cl-webdriver-client](https://github.com/copyleft/cl-webdriver-client/) [![GitHub stars](https://img.shields.io/github/stars/copyleft/cl-webdriver-client/?style=flat)](https://github.com/copyleft/cl-webdriver-client//stargazers) - a binding library to WebDriver (supports Selenium 4.0).

### Form handling

* 👍 [cl-forms](https://github.com/mmontone/cl-forms) [![GitHub stars](https://img.shields.io/github/stars/mmontone/cl-forms?style=flat)](https://github.com/mmontone/cl-forms/stargazers) -  Web forms handling library for Common lisp. [MIT][200].

### User login and password management

* [cl-authentic](https://github.com/charJe/cl-authentic) [![GitHub stars](https://img.shields.io/github/stars/charJe/cl-authentic?style=flat)](https://github.com/charJe/cl-authentic/stargazers) -  Password management for Common Lisp (web) applications. [LLGPL][8].
  - safe password storage: cleartext-free, using your choice of hash algorithm through ironclad, storage in an SQL database,
  - password reset mechanism with one-time tokens (suitable for mailing to users for confirmation),
  - user creation optionally with confirmation tokens (suitable for mailing to users),
* [mito-email-auth](https://github.com/40ants/mito-email-auth) [![GitHub stars](https://img.shields.io/github/stars/40ants/mito-email-auth?style=flat)](https://github.com/40ants/mito-email-auth/stargazers) - Helper to authenticate a website's users by sending them unique code by email.

* [cl-cas](https://github.com/fferrere/cl-cas) [![GitHub stars](https://img.shields.io/github/stars/fferrere/cl-cas?style=flat)](https://github.com/fferrere/cl-cas/stargazers) - A library to help [CAS authenticaton](https://en.wikipedia.org/wiki/Central_Authentication_Service) to Common Lisp web applications. Not in Quicklisp.
  * [cas-middleware](https://github.com/fferrere/cas-middleware) [![GitHub stars](https://img.shields.io/github/stars/fferrere/cas-middleware?style=flat)](https://github.com/fferrere/cas-middleware/stargazers) - CAS authenticaton middleware for Caveman.
  * [cas-demo](https://github.com/fferrere/cas-demo) [![GitHub stars](https://img.shields.io/github/stars/fferrere/cas-demo?style=flat)](https://github.com/fferrere/cas-demo/stargazers) - a demo project.

See also mito-auth and the Hunchentoot and Clack plugins above.

### Web project skeletons and generators

* [cl-cookieweb](https://github.com/vindarel/cl-cookieweb) [![GitHub stars](https://img.shields.io/github/stars/vindarel/cl-cookieweb?style=flat)](https://github.com/vindarel/cl-cookieweb/stargazers) - a  Cookiecutter template to start a web project. [BSD_3Clause][15]. Not in Quicklisp.
  * Provides a working toy web app with the Hunchentoot web server, easy-routes, Djula templates, styled with Bulma, based on SQLite, with migrations, an example table definition and a test suite using FiveAM.
* [make-like](https://github.com/container-lisp/make-like) [![GitHub stars](https://img.shields.io/github/stars/container-lisp/make-like?style=flat)](https://github.com/container-lisp/make-like/stargazers) - an application template builder for LIKE (Lisp In Kubernetes + Emacs) applications. [Apache2.0][51].
  * Makefile, podman support, GitHub Actions, Prometheus metrics support, TOML-style config.ini, easy-route preconfigured with health-check and more.
* [cl-webapp-seed](https://github.com/rajasegar/cl-webapp-seed) [![GitHub stars](https://img.shields.io/github/stars/rajasegar/cl-webapp-seed?style=flat)](https://github.com/rajasegar/cl-webapp-seed/stargazers) - a simple web application boilerplate. Uses Hunchentoot, cl-who, deploys easily to Heroku. [MIT][200].

Others
------

* [LASS](https://codeberg.org/shinmera/LASS) -  Lisp Augmented Style Sheets. Largely inspired by SASS. Zlib.
* [css-lite](https://github.com/paddymul/css-lite) [![GitHub stars](https://img.shields.io/github/stars/paddymul/css-lite?style=flat)](https://github.com/paddymul/css-lite/stargazers) - A CSS grammar. [Expat][14].
* [find-port](https://github.com/lisp-maintainers/find-port) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/find-port?style=flat)](https://github.com/lisp-maintainers/find-port/stargazers) -  Programmatically find open ports. [MIT][200].
* [cl-wget](https://github.com/cl-wget/cl-wget) [![GitHub stars](https://img.shields.io/github/stars/cl-wget/cl-wget?style=flat)](https://github.com/cl-wget/cl-wget/stargazers) - Makes retrieving large files or mirroring entire websites easy. [AGPL-3.0][51].
* [trivial-download](https://github.com/eudoxia0/trivial-download) [![GitHub stars](https://img.shields.io/github/stars/eudoxia0/trivial-download?style=flat)](https://github.com/eudoxia0/trivial-download/stargazers) - Download files.
  * currently archived and unmaintained. [MIT][200].
* [cl-cookie](https://github.com/fukamachi/cl-cookie) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/cl-cookie?style=flat)](https://github.com/fukamachi/cl-cookie/stargazers) HTTP Cookie (jar) manager: parse and write (set-)cookie headers, compare cookies, optional cookie attribute sanity check. [MIT][200]
* [dns-client](https://codeberg.org/Shinmera/dns-client) - DNS record client. See [documentation](https://shinmera.github.io/dns-client/). [zlib][33].
* [mobiledetect](https://github.com/Junker/mobiledetect) [![GitHub stars](https://img.shields.io/github/stars/Junker/mobiledetect?style=flat)](https://github.com/Junker/mobiledetect/stargazers) - System for detecting mobile devices (including tablets) in User-Agent strings. MIT.
* [random-ua](https://github.com/Junker/random-ua) [![GitHub stars](https://img.shields.io/github/stars/Junker/random-ua?style=flat)](https://github.com/Junker/random-ua/stargazers) - Random User-Agent generator for Common Lisp. BSD_2Clause.
* [cl-web-push](https://github.com/ryukinix/cl-web-push) [![GitHub stars](https://img.shields.io/github/stars/ryukinix/cl-web-push?style=flat)](https://github.com/ryukinix/cl-web-push/stargazers) - Web Push Notifications for Common Lisp applications.


### Email

* [trivial-imap](https://github.com/40ants/trivial-imap) [![GitHub stars](https://img.shields.io/github/stars/40ants/trivial-imap?style=flat)](https://github.com/40ants/trivial-imap/stargazers) - tries to make easy some common cases of working with IMAP servers, like reading emails from the server. A thin wrapper over post-office library (which is a fork of Franz's cl-imap). [BSD][15].
* [cl-smtp](https://gitlab.common-lisp.net/cl-smtp/cl-smtp) - CL-SMTP is a simple lisp smtp client.

Sending emails with a third-party provider:

* [sendgrid](https://github.com/vindarel/cl-sendgrid) [![GitHub stars](https://img.shields.io/github/stars/vindarel/cl-sendgrid?style=flat)](https://github.com/vindarel/cl-sendgrid/stargazers) - send emails with Sendgrid's API. [MIT][200].
* [mailgun](https://github.com/40ants/mailgun) [![GitHub stars](https://img.shields.io/github/stars/40ants/mailgun?style=flat)](https://github.com/40ants/mailgun/stargazers) - A thin wrapper to post HTML emails through mailgun.com. [unlicence][5].

Parsing email addresses:

* [parcom/email](https://github.com/fosskers/parcom/?tab=readme-ov-file#email-addresses) - types and parsers for RFC5322 email addresses. The implementation is RFC-compliant and particularly memory-efficient for well-behaved addresses.


### OpenAPI, OData, OpenRPC

* NEW! [openapi-generator](https://codeberg.org/kilianmh/openapi-generator) - OpenAPI client code generator. [AGPL-3.0][51].
  * Generation of OpenAPI ASDF/Quicklisp-loadable projects within one command,
  * Support for path, (arbitrary) query, (arbitrary) header, (json) content parameters,
  * Conversion of an OpenAPI spec into CLOS object -> explore API within inspector,
  * Conversion of OpenAPI-2.0 or YAML files to OpenAPI-3.0 JSON with swagger converter (network connection required),
  * etc.
* [apispec](https://github.com/cxxxr/apispec) [![GitHub stars](https://img.shields.io/github/stars/cxxxr/apispec?style=flat)](https://github.com/cxxxr/apispec/stargazers) -  A Common Lisp library for handling Web API requests and responses. [BSD_3Clause][15].
  - takes an OpenAPI3 yaml specification and allows to validate and parse HTTP request headers, parameters and bodies.
* [cl-odata-client](https://github.com/copyleft/cl-odata-client) [![GitHub stars](https://img.shields.io/github/stars/copyleft/cl-odata-client?style=flat)](https://github.com/copyleft/cl-odata-client/stargazers) - Common Lisp client library for accessing [OData services](https://www.odata.org). [MIT][200].
* [OpenRPC](https://github.com/40ants/openrpc) [![GitHub stars](https://img.shields.io/github/stars/40ants/openrpc?style=flat)](https://github.com/40ants/openrpc/stargazers) - OpenRPC implementation for Common Lisp. [BSD][15].
  - Automatic OpenRPC spec generation
  - Automatic JSON-RPC client building by OpenRPC spec. This includes creation of Common Lisp classes and methods for making RPC requests and returning native CL objects.
  - all JSON marshalling is done under the hood.
- [jsonrpc](https://github.com/cxxxr/jsonrpc) [![GitHub stars](https://img.shields.io/github/stars/cxxxr/jsonrpc?style=flat)](https://github.com/cxxxr/jsonrpc/stargazers) -  JSON-RPC 2.0 server/client for Common Lisp. [BSD][15].


### Static site generators

* [coleslaw](https://github.com/kingcons/coleslaw) [![GitHub stars](https://img.shields.io/github/stars/kingcons/coleslaw?style=flat)](https://github.com/kingcons/coleslaw/stargazers) and its
  [coleslaw-cli](https://github.com/40ants/coleslaw-cli) [![GitHub stars](https://img.shields.io/github/stars/40ants/coleslaw-cli?style=flat)](https://github.com/40ants/coleslaw-cli/stargazers) - Flexible
  Lisp Blogware similar to Frog, Jekyll, or Hakyll. [BSD][15].

### Third-party APIs

* [pirá](https://github.com/fukamachi/pira) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/pira?style=flat)](https://github.com/fukamachi/pira/stargazers) - Unofficial AWS SDK for Common Lisp.
  * "Pirá is a modern, unofficial AWS SDK for Common Lisp built on the Smithy protocol framework. It provides comprehensive coverage of AWS services through auto-generated client code from official AWS service models."
  * Supports 400+ AWS services
  * Multiple Protocols: REST-JSON, REST-XML, AWS Query, EC2 Query, and AWS JSON.
* [aws-sdk-lisp](https://github.com/pokepay/aws-sdk-lisp/) [![GitHub stars](https://img.shields.io/github/stars/pokepay/aws-sdk-lisp/?style=flat)](https://github.com/pokepay/aws-sdk-lisp//stargazers) - Provides interfaces for each AWS services as individual systems. [BSD_2Clause][17].
  * *intended to be replaced by Pirá*
  * incluse dozens of services: dsn, appstream, athena, cloudfront, codedeploy, cognito-*, directconnect, dynamodb, dms, elasticache, email, events, kinesis, machinelearning, monitoring, s3, sms, storagegateway, workspaces…
* [Aws-sign4](https://github.com/rotatef/aws-sign4) [![GitHub stars](https://img.shields.io/github/stars/rotatef/aws-sign4?style=flat)](https://github.com/rotatef/aws-sign4/stargazers) - Common Lisp library for Amazon Web Services signing version 4. [GNU GPL3][2].
* [zs3](https://github.com/xach/zs3) [![GitHub stars](https://img.shields.io/github/stars/xach/zs3?style=flat)](https://github.com/xach/zs3/stargazers) - A library for working with Amazon's Simple Storage
Service (S3) and CloudFront service. [BSD][15].
* [north](https://shinmera.github.io/north) - The successor to the South (Simple OaUTH) library, implementing the full oAuth 1.0a protocol, both client and server sides. Using North you can easily become an oAuth provider or consumer. [zlib][33].
* [Ciao](https://github.com/kjinho/ciao) [![GitHub stars](https://img.shields.io/github/stars/kjinho/ciao?style=flat)](https://github.com/kjinho/ciao/stargazers) - an easy-to-use Common Lisp OAuth 2.0 client library. It is a port of the Racket OAuth 2.0 Client to Common Lisp. [LGPL3][9].
* [cl-oauth2](https://sr.ht/~hajovonta/cl-oauth2/) - OAuth 2.0 and OpenID Connect client library for Common Lisp. Supports authorization code (with PKCE), client credentials, device authorization, token refresh, JWT verification (RS256/ES256/HS256), OIDC discovery, and token caching. MIT.
  * *built with LLMs*
* [tooter](https://codeberg.org/shinmera/tooter) - a client library implementing the full v1 REST API protocol for Mastodon. [zlib][33].
* [cl-irc](https://www.common-lisp.net/project/cl-irc/) - An IRC client library. [Expat][14].
* [cl-mediawiki](https://github.com/AccelerationNet/cl-mediawiki) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/cl-mediawiki?style=flat)](https://github.com/AccelerationNet/cl-mediawiki/stargazers) - a wrapper around the MediaWiki api. [MIT][200].
* [cl-openid](https://github.com/cl-openid/cl-openid) [![GitHub stars](https://img.shields.io/github/stars/cl-openid/cl-openid?style=flat)](https://github.com/cl-openid/cl-openid/stargazers) - An implementation of OpenID. [LLGPL][8].
* [cl-pushover](https://github.com/TeMPOraL/cl-pushover) [![GitHub stars](https://img.shields.io/github/stars/TeMPOraL/cl-pushover?style=flat)](https://github.com/TeMPOraL/cl-pushover/stargazers) -  Common Lisp bindings to Pushover. [MIT][200].
* [humbler](https://codeberg.org/shinmera/humbler) - A Tumblr API interface. [zlib][33].
* [multiposter](https://codeberg.org/shinmera/multiposter) - post to multiple services simultaneously. [zlib][33].
* [stripe](https://github.com/boogsbunny/stripe) [![GitHub stars](https://img.shields.io/github/stars/boogsbunny/stripe?style=flat)](https://github.com/boogsbunny/stripe/stargazers) - a client for the Stripe payment system. [MIT][200].
* [lisp-pay](https://github.com/K1D77A/lisp-pay) [![GitHub stars](https://img.shields.io/github/stars/K1D77A/lisp-pay?style=flat)](https://github.com/K1D77A/lisp-pay/stargazers) - Wrappers around various payment processors: Paypal, Stripe, Coinpayments and BTCPayServer. [MIT][200].
* [lunamech-matrix-api](https://github.com/K1D77A/lunamech-matrix-api) [![GitHub stars](https://img.shields.io/github/stars/K1D77A/lunamech-matrix-api?style=flat)](https://github.com/K1D77A/lunamech-matrix-api/stargazers) - A complete wrapper over the Client -> Server Matrix API. [MIT][200].
* [cl-telegram-bot](https://40ants.com/cl-telegram-bot/) - Telegram bot API. [MIT][200].
  * includes example bots such as a calculator, payment with invoices, an actor-based bot…
  * automatic API spec parser
  * [cl-telegram-bot-auto-api](https://github.com/aartaka/cl-telegram-bot-auto-api) [![GitHub stars](https://img.shields.io/github/stars/aartaka/cl-telegram-bot-auto-api?style=flat)](https://github.com/aartaka/cl-telegram-bot-auto-api/stargazers) - Alternative Telegram Bot API bindings, auto-generated from Telegram website. [3-clause BSD][15].


Numerical and Scientific
========================

* ⭐ [maxima](http://maxima.sourceforge.net/) - Computer Algebra System. [GNU GPL3][2].
  * [wxMaxima](https://wxmaxima-developers.github.io/wxmaxima/): a graphical frontend.
  * [Maxima on Jupyter](https://github.com/robert-dodier/maxima-jupyter) [![GitHub stars](https://img.shields.io/github/stars/robert-dodier/maxima-jupyter?style=flat)](https://github.com/robert-dodier/maxima-jupyter/stargazers)
  * [new, POC] [Maxima in the browser on WASM](https://maxima-on-wasm.pages.dev/), [sources](https://gitlab.com/spaghettisalat/maxima/-/tree/emscripten-port-deployed)
  * it can be used via [SageMath](https://www.sagemath.org/) and [KDE Cantor](https://apps.kde.org/cantor/).
  * it can be used within Emacs:
    * [maxima-mode](https://gitlab.com/sasanidas/maxima) ([screenshot](https://community.linuxmint.com/img/screenshots/maxima-emacs.png))
    * [maxima-interface](https://github.com/jmbr/maxima-interface) [![GitHub stars](https://img.shields.io/github/stars/jmbr/maxima-interface?style=flat)](https://github.com/jmbr/maxima-interface/stargazers) to ease the interface between Maxima and Common Lisp.
    * [symbol-cruncher](https://git.sr.ht/~jmbr/symbol-cruncher) - Computer algebra system for computations in differential geometry. Built on top of maxima-interface.
* [numcl](https://github.com/numcl/numcl) [![GitHub stars](https://img.shields.io/github/stars/numcl/numcl?style=flat)](https://github.com/numcl/numcl/stargazers) - Numpy clone in Common Lisp. [LGPL3][9].
* [numericals](https://github.com/digikar99/numericals) [![GitHub stars](https://img.shields.io/github/stars/digikar99/numericals?style=flat)](https://github.com/digikar99/numericals/stargazers) -  SIMD powered simple-math numerical operations on arrays for Common Lisp through CFFI [still experimental]. MIT.
  * documentation: https://digikar99.github.io/numericals/
* [dense-arrays](https://github.com/digikar99/dense-arrays) [![GitHub stars](https://img.shields.io/github/stars/digikar99/dense-arrays?style=flat)](https://github.com/digikar99/dense-arrays/stargazers) -  Numpy like array object for common lisp. MIT.
* [GSLL](https://common-lisp.net/project/gsll/) - GNU Scientific Library for Lisp; allows the use of the GSL from Common Lisp. [GNU LGPL2.1][11].
* [Xecto](https://github.com/pkhuong/Xecto) [![GitHub stars](https://img.shields.io/github/stars/pkhuong/Xecto?style=flat)](https://github.com/pkhuong/Xecto/stargazers) - A library for regular array parallelism. [3-clause BSD][15].
* [Petalisp](https://github.com/marcoheisig/Petalisp) [![GitHub stars](https://img.shields.io/github/stars/marcoheisig/Petalisp?style=flat)](https://github.com/marcoheisig/Petalisp/stargazers) - an attempt to
  generate high performance code for parallel computers by
  JIT-compiling array definitions. It works on a more
  fundamental level than NumPy, by providing even more powerful
  N-dimensional arrays, but just a few building blocks for working on
  them. [AGPL-3.0][agpl3].
* [cl-ana](https://github.com/ghollisjr/cl-ana) [![GitHub stars](https://img.shields.io/github/stars/ghollisjr/cl-ana?style=flat)](https://github.com/ghollisjr/cl-ana/stargazers) - Common Lisp data analysis library with emphasis on modularity and conceptual clarity. It aims to be a general purpose framework for analyzing small and large scale datasets, including binned data analysis and visualization. [GNU GPL3][2].
* [avm](https://github.com/takagi/avm) [![GitHub stars](https://img.shields.io/github/stars/takagi/avm?style=flat)](https://github.com/takagi/avm/stargazers) - Efficient and expressive arrayed vector math library with multi-threading and CUDA support. [MIT][200].
* [array-operations](https://github.com/bendudson/array-operations) [![GitHub stars](https://img.shields.io/github/stars/bendudson/array-operations?style=flat)](https://github.com/bendudson/array-operations/stargazers) - a collection of functions and macros for manipulating Common Lisp arrays and performing numerical calculations with them. [MIT][200].
* [cl-geometry](https://github.com/Ramarren/cl-geometry/) [![GitHub stars](https://img.shields.io/github/stars/Ramarren/cl-geometry/?style=flat)](https://github.com/Ramarren/cl-geometry//stargazers) - a system for two dimensional computational geometry for Common Lisp. [MIT][200].
* [Vellum](https://github.com/sirherrbatka/vellum) [![GitHub stars](https://img.shields.io/github/stars/sirherrbatka/vellum?style=flat)](https://github.com/sirherrbatka/vellum/stargazers) - Data Frames for Common Lisp. BSD_2Clause.
* [rtg-math](https://github.com/cbaggers/rtg-math/) [![GitHub stars](https://img.shields.io/github/stars/cbaggers/rtg-math/?style=flat)](https://github.com/cbaggers/rtg-math//stargazers) - a selection of the math routines most commonly needed for making realtime graphics in lisp (2, 3 and 4 component vectors, 3x3 and 4x4 matrices, quaternions, spherical and polar coordinates). BSD_2Clause.


Planning solvers:

* [linear-programming](https://neil-lindquist.github.io/linear-programming/) – a library for solving linear programming problems. [MIT][200].
* [shop3](https://github.com/shop-planner/shop3) [![GitHub stars](https://img.shields.io/github/stars/shop-planner/shop3?style=flat)](https://github.com/shop-planner/shop3/stargazers) - a Hierarchical Task Network (HTN) AI planner. Mozilla Public License.


NEW! If you have precise needs, blurry needs or simply questions, the repository [Common Lisp numsci call for needs](https://github.com/digikar99/common-lisp-numsci-call-for-needs) [![GitHub stars](https://img.shields.io/github/stars/digikar99/common-lisp-numsci-call-for-needs?style=flat)](https://github.com/digikar99/common-lisp-numsci-call-for-needs/stargazers) is a new place to discuss them.


Matrix libraries
----------------

* [LLA](https://github.com/Lisp-Stat/lla) [![GitHub stars](https://img.shields.io/github/stars/Lisp-Stat/lla?style=flat)](https://github.com/Lisp-Stat/lla/stargazers) -  Lisp Linear Algebra. MS-PL.
  * a high-level Common Lisp library built on on BLAS and LAPACK, but providing a more abstract interface with the purpose of freeing the user from low-level concerns and reducing the number of bugs in numerical code.
* [magicl](https://github.com/quil-lang/magicl) [![GitHub stars](https://img.shields.io/github/stars/quil-lang/magicl?style=flat)](https://github.com/quil-lang/magicl/stargazers) - Matrix Algebra proGrams In Common Lisp based on BLAS/LAPACK and Expokit, by Rigetti Computing. [BSD_3Clause][15].
* [lisp-matrix](https://github.com/blindglobe/lisp-matrix) [![GitHub stars](https://img.shields.io/github/stars/blindglobe/lisp-matrix?style=flat)](https://github.com/blindglobe/lisp-matrix/stargazers) - A matrix package. [FreeBSD][39].
* [3d-matrices](https://shinmera.github.io/3d-matrices) - A library implementing common matrix calculations, with an emphasis on 2x2,3x3, and 4x4 matrices as commonly used in graphics. It provides some numerical functions as well, but those are not the focus. The library is heavily optimised, so it is not made of pretty code. [zlib][33].
* [clem](https://github.com/slyrus/clem) [![GitHub stars](https://img.shields.io/github/stars/slyrus/clem?style=flat)](https://github.com/slyrus/clem/stargazers) - a matrix library. [BSD_2Clause][17].

Statistics
---------

* 👍 [lisp-stat](https://github.com/lisp-stat) [![GitHub stars](https://img.shields.io/github/stars/lisp-stat?style=flat)](https://github.com/lisp-stat/stargazers) - an environment for statistical computing, conceptually similar to R, that is also suitable for front-line production deployments. "It grew out of a desire to have an environment for rapidly prototyping analytical and A.I. solutions, and move directly to production environments with minimal friction."
  * https://lisp-stat.dev/
  * inspired by Luke Tierney's [XLisp-Stat](https://homepage.stat.uiowa.edu/~luke/xls/xlsinfo/) (a predecessor of R), ships a compatibility library for it, otherwise builds on other and newer libraries.

See also [common-lisp-stat](https://github.com/blindglobe/common-lisp-stat/) [![GitHub stars](https://img.shields.io/github/stars/blindglobe/common-lisp-stat/?style=flat)](https://github.com/blindglobe/common-lisp-stat//stargazers), Common Lisp statistics library. [FreeBSD][39], staling.

Units
-----

* [physical-quantities](https://github.com/mrossini-ethz/physical-quantities) [![GitHub stars](https://img.shields.io/github/stars/mrossini-ethz/physical-quantities?style=flat)](https://github.com/mrossini-ethz/physical-quantities/stargazers) - a library that provides a numeric type with optional unit and/or uncertainty for computations with automatic error propagation. GPL2

Plotting
--------

* lisp-stat's [plot (vega-lite)](https://github.com/Lisp-Stat/plot) [![GitHub stars](https://img.shields.io/github/stars/Lisp-Stat/plot?style=flat)](https://github.com/Lisp-Stat/plot/stargazers) - a Vega-lite DSL. MS-PL.
  * includes functions for text-based plotting that work in the REPL, and JavaScript visualisations that are rendered in a browser.
  * [emacs-vega-view](https://github.com/applied-science/emacs-vega-view?tab=readme-ov-file#common-lisp) - an Emacs plugin that allows to display a Vega plot from a lisp-stat expression in a buffer.
* [vgplot](https://github.com/volkers/vgplot) [![GitHub stars](https://img.shields.io/github/stars/volkers/vgplot?style=flat)](https://github.com/volkers/vgplot/stargazers) - an interface to the
  gnuplot plotting utility with the intention to resemble some of
  the plot commands of octave or matlab. [GPL3][2].
* [eazy-gnuplot](https://github.com/guicho271828/eazy-gnuplot) [![GitHub stars](https://img.shields.io/github/stars/guicho271828/eazy-gnuplot?style=flat)](https://github.com/guicho271828/eazy-gnuplot/stargazers) - a
  lispy, structure-less Gnuplot library. With its
  [cookbook](http://guicho271828.github.io/eazy-gnuplot/). [LLGPL][8]
* [kai](https://github.com/komi1230/kai) [![GitHub stars](https://img.shields.io/github/stars/komi1230/kai?style=flat)](https://github.com/komi1230/kai/stargazers) - A high-level plotter library for Common Lisp. A wrapper around the [Plotly](https://plotly.com/javascript/) JS library. [MIT][200].
* [ADW-Charting](https://common-lisp.net/project/adw-charting/) - A simple chart drawing library written completely in Common Lisp. Also includes a backend to Google's chart service. BSD-like.

cool but WIP:

* [plotly-user](https://github.com/ajberkley/plotly-user) [![GitHub stars](https://img.shields.io/github/stars/ajberkley/plotly-user?style=flat)](https://github.com/ajberkley/plotly-user/stargazers) -  Use plotly in your browser to explore data from a Common Lisp REPL. [BSD_3Clause][15].

Plotting with text:

* [cl-text-plot](https://github.com/moneylobster/cl-text-plot/) [![GitHub stars](https://img.shields.io/github/stars/moneylobster/cl-text-plot/?style=flat)](https://github.com/moneylobster/cl-text-plot//stargazers) -  Plot with text in Common Lisp. No licence specified.
* [cl-spark](https://github.com/tkych/cl-spark) [![GitHub stars](https://img.shields.io/github/stars/tkych/cl-spark?style=flat)](https://github.com/tkych/cl-spark/stargazers) - sparkline strings for the console: `(spark '(1 1 2 3 5 8))` => "▁▁▂▃▅▇". [MIT][200].

See also the chart facilities of IUP and ltk-plotchart (GUI section).

Utils
-----

* [cmu-infix](https://github.com/rigetti/cmu-infix) [![GitHub stars](https://img.shields.io/github/stars/rigetti/cmu-infix?style=flat)](https://github.com/rigetti/cmu-infix/stargazers) - A library for writing infix mathematical notation in Common Lisp. See also [polisher](https://github.com/mrcdr/polisher) [![GitHub stars](https://img.shields.io/github/stars/mrcdr/polisher?style=flat)](https://github.com/mrcdr/polisher/stargazers).


Parallelism and Concurrency
===========================

* ⭐ [BordeauxThreads](https://common-lisp.net/project/bordeaux-threads/) - Portable, shared-state concurrency. [Expat][14].
* ⭐ [lparallel](https://github.com/sharplispers/lparallel) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/lparallel?style=flat)](https://github.com/sharplispers/lparallel/stargazers) - A library for parallel programming. [3-clause BSD][15]. Originally on [lmj/lparallel](https://github.com/lmj/lparallel) [![GitHub stars](https://img.shields.io/github/stars/lmj/lparallel?style=flat)](https://github.com/lmj/lparallel/stargazers).
  - with [good documentation](https://sharplispers.github.io/lparallel/)
* [lfarm](https://github.com/lmj/lfarm) [![GitHub stars](https://img.shields.io/github/stars/lmj/lfarm?style=flat)](https://github.com/lmj/lfarm/stargazers) - distributing work across machines (on top of lparallel and usocket). [BSD_3Clause][15]
* [calispel](https://github.com/hawkir/calispel) [![GitHub stars](https://img.shields.io/github/stars/hawkir/calispel?style=flat)](https://github.com/hawkir/calispel/stargazers) - [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes)-like channels for common lisp. With blocking, optionally buffered channels and a "CSP select" statement. ISC-style.
  - "It is complete, flexible and easy to use. I would recommend Calispel over Lparallel and ChanL." @Ambrevar. [discussion](https://github.com/CodyReichert/awesome-cl/issues/290) [![GitHub stars](https://img.shields.io/github/stars/CodyReichert/awesome-cl/issues/290?style=flat)](https://github.com/CodyReichert/awesome-cl/issues/290/stargazers)
* [chanl](https://github.com/zkat/chanl) [![GitHub stars](https://img.shields.io/github/stars/zkat/chanl?style=flat)](https://github.com/zkat/chanl/stargazers) - Portable, channel-based concurrency. [Expat][14], with parts under [3-clause BSD][15].
* [cl-async](https://github.com/orthecreedence/cl-async) [![GitHub stars](https://img.shields.io/github/stars/orthecreedence/cl-async?style=flat)](https://github.com/orthecreedence/cl-async/stargazers) - A library for general-purpose, non-blocking programming. [Expat][14].
* [Moira](https://github.com/TBRSS/moira) [![GitHub stars](https://img.shields.io/github/stars/TBRSS/moira?style=flat)](https://github.com/TBRSS/moira/stargazers) -  Monitor and restart background threads. In-lisp process supervisor. [MIT][200].
* [trivial-monitored-thread](https://gitlab.com/ediethelm/trivial-monitored-thread) -
  a Common Lisp library offering a way of spawning threads and being
  informed when one any of them crash and die. [MIT][200].
* [cl-gearman](https://github.com/taksatou/cl-gearman) [![GitHub stars](https://img.shields.io/github/stars/taksatou/cl-gearman?style=flat)](https://github.com/taksatou/cl-gearman/stargazers) - a library for the [Gearman](https://github.com/gearman/gearmand/) [![GitHub stars](https://img.shields.io/github/stars/gearman/gearmand/?style=flat)](https://github.com/gearman/gearmand//stargazers) distributed job system. [LLGPL][8].
* [swank-crew](https://github.com/brown/swank-crew) [![GitHub stars](https://img.shields.io/github/stars/brown/swank-crew?style=flat)](https://github.com/brown/swank-crew/stargazers) - distributed computation framework implemented using Swank Client. [BSD_3Clause][15].
* [cl-coroutine](https://github.com/takagi/cl-coroutine) [![GitHub stars](https://img.shields.io/github/stars/takagi/cl-coroutine?style=flat)](https://github.com/takagi/cl-coroutine/stargazers) - a coroutine library. It uses the CL-CONT continuations library in its implementation. [MIT][200].
* [STMX](https://github.com/cosmos72/stmx) [![GitHub stars](https://img.shields.io/github/stars/cosmos72/stmx?style=flat)](https://github.com/cosmos72/stmx/stargazers) -  High performance Transactional Memory for Common Lisp. [LLGPL][8].
* [Blackbird](https://orthecreedence.github.io/blackbird/) - a Promise implementation for Common Lisp [MIT][200].
  * see also [promise](https://codeberg.org/Shinmera/promise) - a basic promise datastructure, with timeouts. ZLIB.
* [cl-cancel](https://github.com/atgreen/cl-cancel) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-cancel?style=flat)](https://github.com/atgreen/cl-cancel/stargazers) -  Cancellation propagation library for Common Lisp with deadlines and timeouts. MIT. *With LLM*.

See also:

* [cl-etcd](https://github.com/atgreen/cl-etcd) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-etcd?style=flat)](https://github.com/atgreen/cl-etcd/stargazers) - Run etcd as an asynchronous inferior process.  [etcd](https://etcd.io/) is a strongly consistent, distributed key-value store. [AGPL-3.0][agpl3].

Actors pattern
--------------

* 👍 [Sento](https://github.com/mdbergmann/cl-gserver) [![GitHub stars](https://img.shields.io/github/stars/mdbergmann/cl-gserver?style=flat)](https://github.com/mdbergmann/cl-gserver/stargazers) - Sento is a 'message passing' library/framework with actors similar to Erlang or Akka. It supports creating systems that should work reactive, require parallel computing and event based message handling. [Apache2][89].
  * has remoting support since 2026-03.

See also:

* [lisp-actors](https://github.com/dbmcclain/Lisp-Actors) [![GitHub stars](https://img.shields.io/github/stars/dbmcclain/Lisp-Actors?style=flat)](https://github.com/dbmcclain/Lisp-Actors/stargazers), an "ongoing investigation into the use of the Actor model in Common Lisp, which has had the benefit of real-world application".
  * it was part of the [Emotiq blockchain](https://github.com/emotiq/emotiq/blob/dev/src/test/blockchain-test.lisp) [![GitHub stars](https://img.shields.io/github/stars/emotiq/emotiq/blob/dev/src/test/blockchain-test.lisp?style=flat)](https://github.com/emotiq/emotiq/blob/dev/src/test/blockchain-test.lisp/stargazers) (a discontinued project)
  * does remoting, includes a threading abstraction layer library similar to Bordeaux-Threads.
  * ! it lacks unit tests.
* [Actors](https://github.com/aarvid/Actors) [![GitHub stars](https://img.shields.io/github/stars/aarvid/Actors?style=flat)](https://github.com/aarvid/Actors/stargazers) package for LispWorks ([announce](https://www.reddit.com/r/Common_Lisp/comments/77vsft/david_mcclains_actors_package_for_lispworks/)) [MIT][200].


Event processing
----------------

* [simple-tasks](https://codeberg.org/shinmera/simple-tasks) - A very simple task scheduling framework. [zlib][33].
  * saves the return values and the task environment in case of failure, so we can inspect it later.
* [deeds](https://codeberg.org/shinmera/deeds) - Deeds is an Extensible Event Delivery System. It allows for efficient event delivery to multiple handlers with a complex event filtering system. [zlib][33].
* [cl-flow](https://github.com/borodust/cl-flow/) [![GitHub stars](https://img.shields.io/github/stars/borodust/cl-flow/?style=flat)](https://github.com/borodust/cl-flow//stargazers) -  Data-flowish computation tree library for non-blocking concurrent Common Lisp. [MIT][200].
* [event-glue](https://github.com/orthecreedence/event-glue) [![GitHub stars](https://img.shields.io/github/stars/orthecreedence/event-glue?style=flat)](https://github.com/orthecreedence/event-glue/stargazers) - simple eventing abstraction. No dependencies. It can be used anywhere you need a generic event handling system. [MIT][200].
* [cl-nats](https://github.com/atgreen/cl-nats) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-nats?style=flat)](https://github.com/atgreen/cl-nats/stargazers) -  A full-featured NATS messaging client for Common Lisp. MIT. *With LLM*.
  * Pub/Sub, request/reply, TLS 1.3, auto-reconnect, cluster discovery, Keep-Alive, cancellation.


Job processing
--------------


* [SBCL's timers](http://www.sbcl.org/manual/#Timers), system-wide event schedulers.
* [psychiq](https://github.com/fukamachi/psychiq) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/psychiq?style=flat)](https://github.com/fukamachi/psychiq/stargazers) - redis-based background job processing for Common Lisp applications. Inspired by Ruby's Sidekiq and compatible with its web UI. [LLGPL][8].
* [cl-cron](https://github.com/lisp-maintainers/cl-cron) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/cl-cron?style=flat)](https://github.com/lisp-maintainers/cl-cron/stargazers) - A simple tool that provides cron like facilities. [GPL3][2].
* [clerk](https://github.com/tsikov/clerk) [![GitHub stars](https://img.shields.io/github/stars/tsikov/clerk?style=flat)](https://github.com/tsikov/clerk/stargazers) - run regular or one-time jobs at given intervals. [MIT][200].
  * maintained on [lisp-maintainers/clerk](https://github.com/lisp-maintainers/clerk) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/clerk?style=flat)](https://github.com/lisp-maintainers/clerk/stargazers)


Regular expressions and string parsing
===============================================

* ⭐ [cl-ppcre](http://weitz.de/cl-ppcre/) - Portable, Perl-compatible regular expressions. [FreeBSD][39].
* [one-more-re-nightmare](https://github.com/no-defun-allowed/one-more-re-nightmare) [![GitHub stars](https://img.shields.io/github/stars/no-defun-allowed/one-more-re-nightmare?style=flat)](https://github.com/no-defun-allowed/one-more-re-nightmare/stargazers) - a fast-ish regular expression compiler in Common Lisp. [BSD_2Clause][17].

See also:

* [rexxparse](https://github.com/dtenny/rexxparse) [![GitHub stars](https://img.shields.io/github/stars/dtenny/rexxparse?style=flat)](https://github.com/dtenny/rexxparse/stargazers) -  A string parsing tool inspired by the REXX PARSE construct. MIT.
* [pregexp](http://ds26gte.github.io/pregexp/index.html) -  Portable Regular Expressions for Scheme and Common Lisp.

See also clj-re above.


Scripting
=========

Running scripts
---------------

*Implementations can run files with `--load`, SBCL has `--script`,
but there is a start-up time specially when loading libraries. Can we
do better? We can always build a binary.*

* [ScriptL](https://github.com/rpav/ScriptL) [![GitHub stars](https://img.shields.io/github/stars/rpav/ScriptL?style=flat)](https://github.com/rpav/ScriptL/stargazers) - Shell scripting made Lisp-like! Or, live-coding remote function calls for the shell. Write a command in the REPL, and run it instantly in the shell. [LLGPL][8].
  * similar and maybe simpler: [lserver](https://notabug.org/quasus/lserver/)
* [CIEL](https://github.com/ciel-lang/CIEL/) [![GitHub stars](https://img.shields.io/github/stars/ciel-lang/CIEL/?style=flat)](https://github.com/ciel-lang/CIEL//stargazers) - CIEL Is an Extended Lisp is a collection of dozens of libraries useful for mundane tasks (HTTP, JSON, regexps…). [unclear licence]
  * It also comes as a binary that is able to run scripts from sources. Scripts that use the built-in libraries start fast without a compilation step.
  * *in beta as of 2024*
* [kiln](https://github.com/ruricolist/kiln) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/kiln?style=flat)](https://github.com/ruricolist/kiln/stargazers) - an infrastructure (managing a hidden multicall binary) to make Lisp scripting efficient and ergonomic. [MIT][200].
  * Kiln makes it practical to write very small scripts. Kiln scripts are fast and cheap to the point where it makes sense to expose even small pieces of Lisp functionality to the shell.


Command-line options parsers
----------------------------

* 👍 [Clingon](https://github.com/dnaeon/clingon) [![GitHub stars](https://img.shields.io/github/stars/dnaeon/clingon?style=flat)](https://github.com/dnaeon/clingon/stargazers) - a rich command-line options parser system.
  * it may have the richest feature set: subcommands, generation of bash completion, support for various kinds of options (integers, booleans, counter, enums…), extensible…
  * [clingon-scripter](https://git.sr.ht/~michal_atlas/clingon-scripter) - define flags as simple `defvar` declarations.
* [Adopt](https://github.com/sjl/adopt/) [![GitHub stars](https://img.shields.io/github/stars/sjl/adopt/?style=flat)](https://github.com/sjl/adopt//stargazers) - A Damn OPTion parsing library. [MIT][200].


Readline, ncurses and other graphical TUI helpers
-------------------------------------------------

* 🔥 [cl-tuition](https://github.com/atgreen/cl-tuition) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-tuition?style=flat)](https://github.com/atgreen/cl-tuition/stargazers) -  A Common Lisp library for building rich, responsive TUIs. MIT.
  * model-view-update Elm architecture, reusable widgets (text input, spinner, progress bar…), mouse support, layout helpers…
* [cl-readline](https://github.com/vindarel/cl-readline) [![GitHub stars](https://img.shields.io/github/stars/vindarel/cl-readline?style=flat)](https://github.com/vindarel/cl-readline/stargazers) - a set of
  functions to edit lines as they are typed in, to maintain a list of
  previously-entered command lines, to recall and reedit them and
  perform csh-like history expansion.  Emacs and vi editing
  modes. [GPL3][2].
* [cl-isocline](https://codeberg.org/digikar/cl-isocline/) - an alternative to libreadline, libedit and the likes.
  * in contrast to the contagious GPL-licensed libreadline, it is MIT licensed, pure C, portable across Unix, Windows, MacOS, supports multiline editing out of the box, and more.
  * contains `isocline-repl`, a feature-rich Common Lisp REPL with support for: multiline editing, history, syntax highlighting, basic debugging.
* [Linedit](https://common-lisp.net/project/linedit) - Readline-style
  library that provides customizable line-editing
  features. [MIT-style][210].
* [cl-charms](https://github.com/HiTECNOLOGYs/cl-charms) [![GitHub stars](https://img.shields.io/github/stars/HiTECNOLOGYs/cl-charms?style=flat)](https://github.com/HiTECNOLOGYs/cl-charms/stargazers) - an
  interface to `libcurses` in Common Lisp. It provides both a raw,
  low-level interface to libcurses via CFFI, and a more higher-level
  lispier interface. [MIT][200].
* [cl-termbox2](https://github.com/garlic0x1/cl-termbox2) [![GitHub stars](https://img.shields.io/github/stars/garlic0x1/cl-termbox2?style=flat)](https://github.com/garlic0x1/cl-termbox2/stargazers) - [Termbox2](https://github.com/termbox/termbox2) [![GitHub stars](https://img.shields.io/github/stars/termbox/termbox2?style=flat)](https://github.com/termbox/termbox2/stargazers) bindings.
  * "termbox2 is a terminal I/O library for creating TUIs. It is a slim alternative to the ubiquitous ncurses library. Unlike ncurses, it has a tighter API, and comes with built-in support for popular terminals if a terminfo db is not present on the system."
* [replic](https://github.com/vindarel/replic/) [![GitHub stars](https://img.shields.io/github/stars/vindarel/replic/?style=flat)](https://github.com/vindarel/replic//stargazers) - helpers to turn existing code into a readline application, with a focus on defining the completion of the commands' arguments. Also comes as a ready to use executable, that transforms a user's lispy init file into readline commands. [MIT][200].
* [cl-ansi-term](https://github.com/vindarel/cl-ansi-term) [![GitHub stars](https://img.shields.io/github/stars/vindarel/cl-ansi-term?style=flat)](https://github.com/vindarel/cl-ansi-term/stargazers) - print
  colorized text, horizontal lines, progress bars, (un)ordered lists
  and tables on ANSI-compliant terminals. [GPL3][2].
* [cl-progress-bar](https://github.com/sirherrbatka/cl-progress-bar/) [![GitHub stars](https://img.shields.io/github/stars/sirherrbatka/cl-progress-bar/?style=flat)](https://github.com/sirherrbatka/cl-progress-bar//stargazers) - progress bars, just like in Quicklisp ! [MIT][200].
  * and [progressons](https://github.com/vindarel/progressons) [![GitHub stars](https://img.shields.io/github/stars/vindarel/progressons?style=flat)](https://github.com/vindarel/progressons/stargazers), a progress bar on one line, for real an dumb terminals. MIT.
* [text-draw](https://codeberg.org/shinmera/text-draw) - Toolkit to draw graphics using pure Unicode text only: boxes, backgrounds, checkboxes and radio buttons, lines, arrows, tables, trees… zlib.
* [old-norse](https://github.com/nallen05/old-norse) [![GitHub stars](https://img.shields.io/github/stars/nallen05/old-norse?style=flat)](https://github.com/nallen05/old-norse/stargazers) - a low-latency, grid-based terminal graphics engine with an integrated event loop. MIT.
  * mouse support, 60fps rendering, deploy anywhere via SSH or TTYD.
* [uncursed](https://github.com/Plisp/uncursed) [![GitHub stars](https://img.shields.io/github/stars/Plisp/uncursed?style=flat)](https://github.com/Plisp/uncursed/stargazers) - cross-platform library for writing terminal interfaces with minimal dependencies. BSD_3Clause.
  * a higher-level buffered drawing abstraction and low-level utilities are provided.

Shells, shells interfaces
-------------------------

* [shcl](https://github.com/bradleyjensen/shcl) [![GitHub stars](https://img.shields.io/github/stars/bradleyjensen/shcl?style=flat)](https://github.com/bradleyjensen/shcl/stargazers) - a POSIX-like shell in Common Lisp. [Apache2.0][89].
* [unix-in-lisp](https://github.com/PuellaeMagicae/unix-in-lisp) [![GitHub stars](https://img.shields.io/github/stars/PuellaeMagicae/unix-in-lisp?style=flat)](https://github.com/PuellaeMagicae/unix-in-lisp/stargazers) -  Mount Unix system into Common Lisp image.
  * Unix concepts are directly/shallowly embedded into Lisp (Unix commands become Lisp macros, Unix file become Lisp variables, Unix streams become lazy Lisp sequences, etc).

Lisp utilities:

* [cmd](https://github.com/ruricolist/cmd) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/cmd?style=flat)](https://github.com/ruricolist/cmd/stargazers) - utility for running external programs. Protects against shell interpolation, built with multi-threaded programs in mind, Windows support. [MIT][200].
  * `uiop:run-program` (synchronous) and `uiop:launch-program` (async) are shipped with ASDF and available on all modern implementations. See the [CL Cookbook: running external programs](https://lispcookbook.github.io/cl-cookbook/os.html#running-external-programs).
* [Clesh](https://github.com/Neronus/Clesh) [![GitHub stars](https://img.shields.io/github/stars/Neronus/Clesh?style=flat)](https://github.com/Neronus/Clesh/stargazers) - extends Common Lisp to embed shell code in a manner similar to perl's backtick. [FreeBSD][39].

See also:

* [Lish](https://github.com/lisp-mirror/yew) [![GitHub stars](https://img.shields.io/github/stars/lisp-mirror/yew?style=flat)](https://github.com/lisp-mirror/yew/stargazers) - `lish` may someday be a lisp shell. [GPL3][2].
  * supports tab-completion of executables in the path and Lisp symbols, allows to write and to mix shell commands and Lisp code, has a tiny REPL and an interactive debugger, and more.
  * WARN: this is an old backup. The original repository is no more.


System administration
---------------------

Configuration tools not unlike Ansible, Chef or Puppet.

* [Consfigurator](https://spwhitton.name/tech/code/consfigurator/) - Lisp declarative configuration management system.  You can use it to configure hosts as root, deploy services as unprivileged users, build and deploy containers, produce disc images, operate on files and directories and more. [GPL3][2].
  * apache, apt, cmd, container, cron, disk, file, firewalld, git, hostname, lets-encrypt, locale, lxc, mount, network, os, package, periodic, postgres, reboot, service, ssh, sshd, systemd, timezone, user…
* [cl-unix-cybernetics](https://github.com/cl-unix-cybernetics/cl-unix-cybernetics) [![GitHub stars](https://img.shields.io/github/stars/cl-unix-cybernetics/cl-unix-cybernetics?style=flat)](https://github.com/cl-unix-cybernetics/cl-unix-cybernetics/stargazers) (previously Adams) - UNIX system administration in Common Lisp. [ISC][22].
  - You describe your systems (hosts) using resources having properties. The properties are then probed and synchronized using only /bin/sh on the remote host, and /usr/bin/ssh on the control host.
- [cl-ssh](https://github.com/jmeissen/cl-ssh) [![GitHub stars](https://img.shields.io/github/stars/jmeissen/cl-ssh?style=flat)](https://github.com/jmeissen/cl-ssh/stargazers) -  SSH v2 client implementation. MIT.
  * Core transport, authentication, and session execution work. Use at your own risk.
  * see also: [trivial-ssh](https://github.com/eudoxia0/trivial-ssh) [![GitHub stars](https://img.shields.io/github/stars/eudoxia0/trivial-ssh?style=flat)](https://github.com/eudoxia0/trivial-ssh/stargazers) (*bitrot as of 2026?*)

Updating executables
--------------------

* [cl-selfupdate](https://github.com/atgreen/cl-selfupdate) [![GitHub stars](https://img.shields.io/github/stars/atgreen/cl-selfupdate?style=flat)](https://github.com/atgreen/cl-selfupdate/stargazers) -  Self-update functionality for Common Lisp executables via GitHub/GitLab Releases. MIT.


Other scripting utilities
-------------------------

* [clawk](https://github.com/sharplispers/clawk) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/clawk?style=flat)](https://github.com/sharplispers/clawk/stargazers) - an AWK implementation embedded into Common Lisp, to search files for lines and perform specified actions on its fields. BSD-style.
* [lqn](https://github.com/inconvergent/lqn) [![GitHub stars](https://img.shields.io/github/stars/inconvergent/lqn?style=flat)](https://github.com/inconvergent/lqn/stargazers) -  query language and terminal utility for querying and transforming Lisp, JSON and other text files. written in Common Lisp. [MIT][200].

And also, stalled projects:

* [WCL](https://github.com/wadehennessey/wcl) [![GitHub stars](https://img.shields.io/github/stars/wadehennessey/wcl?style=flat)](https://github.com/wadehennessey/wcl/stargazers) [stalled] - allow hundreds of Lisp
applications to be realistically available at once, while allowing
several of them to run concurrently.  WCL accomplishes this by
providing Common Lisp as a Unix shared library that can be linked with
Lisp and C code to produce efficient applications.  For example, the
executable for a Lisp version of the canonical `Hello World!`
program requires only 20k bytes on 32 bit x86 Linux.  WCL also
supports a full development environment, including dynamic file
loading and debugging.  A modified version of GDB is used to debug WCL
programs, providing support for mixed language debugging.
    - a [paper](https://dl.acm.org/doi/abs/10.1145/141478.141560): "Delivering efficient Common Lisp applications under Unix".


Text Editor Resources
=====================

This contains plugins and other goodies for various text editors.

* [Parinfer](https://shaunlebron.github.io/parinfer/) - Parinfer is a way to edit lisp code that helps to keep both the indentation and the parenthesis balanced. It is easy to start with and yet it offers advanced features à la Paredit. It is available on many editors (Emacs, Vim, Neovim, Atom, Sublime Text, Visual Studio Code, LightTable, CodeMirror,…).

## Emacs ##

* ⭐ [Slime](https://github.com/slime/slime) [![GitHub stars](https://img.shields.io/github/stars/slime/slime?style=flat)](https://github.com/slime/slime/stargazers) - Superior Lisp Interaction Mode for Emacs; a full-blown environment for Common Lisp inside of Emacs. Public domain.
* [Sly](https://github.com/joaotavora/sly) [![GitHub stars](https://img.shields.io/github/stars/joaotavora/sly?style=flat)](https://github.com/joaotavora/sly/stargazers) - SLY is a fork of SLIME and contains multiple changes and new features, such as Sly stickers.
  * *no C-c C-y shortcut aka slime-call-defun equivalent!*

Starter kits:

* [Emacs4CL](https://github.com/susam/emacs4cl) [![GitHub stars](https://img.shields.io/github/stars/susam/emacs4cl?style=flat)](https://github.com/susam/emacs4cl/stargazers) - A tiny Emacs initialization file to quickly set up vanilla Emacs for Common Lisp programming. Comes with a line-by-line explanation of every line of code in the initialization file.
* [plain-common-lisp](https://github.com/pascalcombier/plain-common-lisp/) [![GitHub stars](https://img.shields.io/github/stars/pascalcombier/plain-common-lisp/?style=flat)](https://github.com/pascalcombier/plain-common-lisp//stargazers) -  A trivial way to get a native Common Lisp environment on Windows.
  * ships SBCL, Quicklisp, Emacs and Slime.
  * with example programs for a console program, accessing the Win32 API, displaying a GUI with IUP, running an OpenGL window.
* [cl-devel2](https://hub.docker.com/r/eshamster/cl-devel2/) - a Docker container for Common Lisp development environment. Ships SBCL, CCL, Roswell and Emacs 26 with Slime.
* [Portacle](https://shinmera.github.io/portacle/) - A portable and multiplatform Common Lisp environment: SBCL, Quicklisp, Emacs, Slime, Git.
  * *warm: Portacle is now un-maintained and ships an old Emacs.*
* [IDEmacs](https://codeberg.org/IDEmacs/IDEmacs) is an attempt at making Emacs beginner friendly.
    * it ships Sly for Common Lisp. With Emacs v29 or higher, you can try IDEmacs temporarily without messing with your .emacs configuration, thanks to the new `--init-directory` option.
* [lisp-stat's Docker image](https://lisp-stat.dev/blog/2026/03/09/getting-started/) comes with a ready-to-use Emacs.

Slime extensions:

* 👍 [slime-star](https://github.com/mmontone/slime-star) [![GitHub stars](https://img.shields.io/github/stars/mmontone/slime-star?style=flat)](https://github.com/mmontone/slime-star/stargazers) - a SLIME configuration with extensions pre-installed, with also some custom utilities and menus:
  - the Lisp system browser
  - [SLIME doc contrib](https://github.com/mmontone/slime-doc-contribs) [![GitHub stars](https://img.shields.io/github/stars/mmontone/slime-doc-contribs?style=flat)](https://github.com/mmontone/slime-doc-contribs/stargazers) - enhance the default help buffer.
  - [Quicklisp systems](https://github.com/mmontone/quicklisp-systems) [![GitHub stars](https://img.shields.io/github/stars/mmontone/quicklisp-systems?style=flat)](https://github.com/mmontone/quicklisp-systems/stargazers) - Search, browse and load Quicklisp systems from Emacs.
  - [Slime breakpoints](https://github.com/mmontone/slime-breakpoints) [![GitHub stars](https://img.shields.io/github/stars/mmontone/slime-breakpoints?style=flat)](https://github.com/mmontone/slime-breakpoints/stargazers)
  - [Slite](https://github.com/tdrhq/slite/) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/slite/?style=flat)](https://github.com/tdrhq/slite//stargazers) - a test runner for FiveAM.
  - [Quicklisp-apropos](https://github.com/mmontone/quicklisp-apropos) [![GitHub stars](https://img.shields.io/github/stars/mmontone/quicklisp-apropos?style=flat)](https://github.com/mmontone/quicklisp-apropos/stargazers) - Perform `apropos` queries across libraries in Quicklisp (full-text search on symbol names, classes, documentation…).
  - [slime-critic](https://github.com/mmontone/slime-critic) [![GitHub stars](https://img.shields.io/github/stars/mmontone/slime-critic?style=flat)](https://github.com/mmontone/slime-critic/stargazers) - the lisp critic gently critiques your code for bad patterns.

Sly extensions:

* [sly-overlay](https://git.sr.ht/~fosskers/sly-overlay) - an extension for Sly that enables the overlay of Common Lisp evaluation results directly into the buffer in the spirit of CIDER (Clojure), Eros (Emacs Lisp) and the Lem editor.
* [sly-mrepl-db](https://gitlab.com/akashadutchie/sly-mrepl-db) - from the debugger, evaluate expressions in a REPL with frame context (and not only in the minibuffer).

Tools:

- [Quicksearch](https://github.com/lisp-maintainers/quicksearch) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/quicksearch?style=flat)](https://github.com/lisp-maintainers/quicksearch/stargazers) - search for projects on GitHub, Quicklisp, Cliki and Bitbucket. MIT.

## Vim & Neovim ##

* [SLIMV](https://github.com/kovisoft/slimv) [![GitHub stars](https://img.shields.io/github/stars/kovisoft/slimv?style=flat)](https://github.com/kovisoft/slimv/stargazers) - Superior Lisp Interaction Mode for Vim; a full-blown environment for Common Lisp inside of Vim. No license specified.
* [Vlime](https://github.com/vlime/vlime) [![GitHub stars](https://img.shields.io/github/stars/vlime/vlime?style=flat)](https://github.com/vlime/vlime/stargazers) - VLIME: Vim plus Lisp Is Mostly Evil. A Common Lisp dev environment for Vim (and Neovim). [MIT][200].
* [quicklisp.nvim](https://gitlab.com/HiPhish/quicklisp.nvim) - A Quicklisp frontend for Neovim.
* [Slimv_box](https://github.com/justin2004/slimv_box) [![GitHub stars](https://img.shields.io/github/stars/justin2004/slimv_box?style=flat)](https://github.com/justin2004/slimv_box/stargazers) - slimv in a Docker container.


## Eclipse ##

* [Dandelion](https://github.com/Ragnaroek/dandelion) [![GitHub stars](https://img.shields.io/github/stars/Ragnaroek/dandelion?style=flat)](https://github.com/Ragnaroek/dandelion/stargazers) - a Common Lisp plugin for the Eclipse IDE.

## Lem ##

* [Lem](https://github.com/lem-project/lem) [![GitHub stars](https://img.shields.io/github/stars/lem-project/lem?style=flat)](https://github.com/lem-project/lem/stargazers) - a general-purpose development environment extensible in Common Lisp.[MIT][200].
  * ncurses and webview frontends.
  * built-in LSP client.
  * ready to use, Emacs-like, Slime-based editor tailored for Common Lisp out of the box.
  * website and documentation: [https://lem-project.github.io/](https://lem-project.github.io/)

* 🚀 [Rooms: Lem on the cloud](https://www.youtube.com/watch?v=IMN7feOQOak) (video presentation)
  * "Rooms is a product that runs Lem, a text editor created in Common Lisp, in the Cloud and can be used by multiple users."
  * NEW as of April, 2024.

## LispWorks

* [lw-plugins](https://github.com/apr3vau/lw-plugins) [![GitHub stars](https://img.shields.io/github/stars/apr3vau/lw-plugins?style=flat)](https://github.com/apr3vau/lw-plugins/stargazers) -  LispWorks Plugins by April & May. OBSD.
  * terminal integration, code folding, side tree, markdown highlighting, Nerd Fonts, fuzzy-matching, enhanced directory mode, expand region, pair editing, SVG rendering…
* [lw-rich-text](https://codeberg.org/fourier/lw-rich-text/) - LispWorks panes with support for HTML-like markup.

## Mine - single-download beginner friendly IDE for Common Lisp and Coalton

* [mine](https://coalton-lang.github.io/mine/) - an integrated development environment for Coalton and Common Lisp for Windows, macOS, and Linux.

## Atom, Pulsar ##

* [SLIMA](https://github.com/neil-lindquist/slima) [![GitHub stars](https://img.shields.io/github/stars/neil-lindquist/slima?style=flat)](https://github.com/neil-lindquist/slima/stargazers) allows you to
  interactively develop Common Lisp code, turning Atom (or now Pulsar) into a
  pretty good, and actively developped, Lisp IDE. [MIT][200].
  - *notice: at the time of writing, SLIMA is a bit lagging behind Slime and Swank's latest changes. It works for us with [Slime 2.27](https://github.com/slime/slime/releases/tag/v2.27) [![GitHub stars](https://img.shields.io/github/stars/slime/slime/releases/tag/v2.27?style=flat)](https://github.com/slime/slime/releases/tag/v2.27/stargazers). Tested on SBCL 2.5.8 and SBCL 2.1.11.debian.*

## Sublime Text ##

* [Sublime Text](http://www.sublimetext.com/3) (proprietary) has
  Common Lisp support with its SublimeREPL and
  [Slyblime](https://github.com/s-clerc/slyblime) [![GitHub stars](https://img.shields.io/github/stars/s-clerc/slyblime?style=flat)](https://github.com/s-clerc/slyblime/stargazers) packages. Slyblime
  is an implementation of SLY and it uses the same backend (SLYNK). It
  ships advanced features including a debugger with stack frame
  inspection.

## VSCode ##

* NEW as of May, 2026 · [OLIVE](https://github.com/kchanqvq/olive/) [![GitHub stars](https://img.shields.io/github/stars/kchanqvq/olive/?style=flat)](https://github.com/kchanqvq/olive//stargazers) - A Common Lisp extension for VSCode with REPL, debugger, go to definition, macro stepper. Based on Swank.
  * [announce and difference from Alive](https://old.reddit.com/r/lisp/comments/1tn3zff/new_cl_vscode_extension_olive/)
* [alive](https://github.com/nobody-famous/alive) [![GitHub stars](https://img.shields.io/github/stars/nobody-famous/alive?style=flat)](https://github.com/nobody-famous/alive/stargazers) -  Common Lisp Extension for VSCode. Public domain.
  * not based on Slime/Swank.
  * see the Cookbook: [using VSCode with Alive](https://lispcookbook.github.io/cl-cookbook/vscode-alive.html)
* [commonlisp-vscode](https://marketplace.visualstudio.com/items?itemName=ailisp.commonlisp-vscode) - an extension to support syntax highlight, auto completion, documentation on hover, go to definition, compile & load file, REPL. It is [On GitHub](https://github.com/ailisp/commonlisp-vscode/) [![GitHub stars](https://img.shields.io/github/stars/ailisp/commonlisp-vscode/?style=flat)](https://github.com/ailisp/commonlisp-vscode//stargazers).
* [strict-paredit-vscode](https://marketplace.visualstudio.com/items?itemName=ailisp.strict-paredit) - structural editing and navigation like Emacs.

## JetBrains

* [SLT](https://github.com/Enerccio/SLT) [![GitHub stars](https://img.shields.io/github/stars/Enerccio/SLT?style=flat)](https://github.com/Enerccio/SLT/stargazers) -  an IDE Plugin for Intellij/Jetbrains IDE lineup implementing support for Common Lisp via SBCL and Slime/Swank.
  - released in Jan, 2023. Experimental.
  - see [this fork](https://github.com/ivanbulanov/SLT/releases) [![GitHub stars](https://img.shields.io/github/stars/ivanbulanov/SLT/releases?style=flat)](https://github.com/ivanbulanov/SLT/releases/stargazers) that is updated to work on Intellij 2025.3.2.

## Geany (experimental) ##

* [Geany-lisp](https://github.com/jasom/geany-lisp) [![GitHub stars](https://img.shields.io/github/stars/jasom/geany-lisp?style=flat)](https://github.com/jasom/geany-lisp/stargazers) is an experimental lisp mode for the [Geany](https://geany.org/) editor.

## Notebooks ##

* [common-lisp-jupyter](https://github.com/yitzchak/common-lisp-jupyter) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/common-lisp-jupyter?style=flat)](https://github.com/yitzchak/common-lisp-jupyter/stargazers) - A Common Lisp kernel for Jupyter along with a library for building Jupyter kernels, based on Maxima-Jupyter by Robert Dodier which was based on cl-jupyter by Frederic Peschanski. [MIT][200].
  * [Cytoscape widget](https://github.com/yitzchak/cytoscape-clj) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/cytoscape-clj?style=flat)](https://github.com/yitzchak/cytoscape-clj/stargazers) -  Cytoscape.js widget for common-lisp-jupyter.
  * [Kekule widget](https://github.com/yitzchak/kekule-clj) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/kekule-clj?style=flat)](https://github.com/yitzchak/kekule-clj/stargazers) -  Kekule.js widget for common-lisp-jupyter.
  * [ngl widget](https://github.com/yitzchak/ngl-clj) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/ngl-clj?style=flat)](https://github.com/yitzchak/ngl-clj/stargazers) -  A ngl widget (protein viewer) for common-lisp-jupyter.
  * [sheet widget](https://github.com/yitzchak/sheet-clj) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/sheet-clj?style=flat)](https://github.com/yitzchak/sheet-clj/stargazers) -  Data grid widget for common-lisp-jupyter.
* [cl-jupyter](https://github.com/fredokun/cl-jupyter) [![GitHub stars](https://img.shields.io/github/stars/fredokun/cl-jupyter?style=flat)](https://github.com/fredokun/cl-jupyter/stargazers) - A Common Lisp kernel for Jupyter notebooks [custom licence](https://github.com/fredokun/cl-jupyter/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/fredokun/cl-jupyter/blob/master/LICENSE?style=flat)](https://github.com/fredokun/cl-jupyter/blob/master/LICENSE/stargazers).

## REPLs ##

* [icl](https://github.com/atgreen/icl) [![GitHub stars](https://img.shields.io/github/stars/atgreen/icl?style=flat)](https://github.com/atgreen/icl/stargazers) - an enhanced REPL for the terminal. MIT.
  * based on Slynk: shares many features with Slime.
  * interactive inspector
  * experimental `,explain` command that fires up Gemini or Claude CLI.
* [cl-repl](https://github.com/lisp-maintainers/cl-repl) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/cl-repl?style=flat)](https://github.com/lisp-maintainers/cl-repl/stargazers) - an ipython-like REPL. With completion, shell commands, magic commands, debugger, etc. [GPL3][2].
  * binary releases: simply download a binary (Ubuntu, OSX, Windows) and run it.
  * [colorthemes](https://github.com/koji-kojiro/lem-pygments-colorthemes) [![GitHub stars](https://img.shields.io/github/stars/koji-kojiro/lem-pygments-colorthemes?style=flat)](https://github.com/koji-kojiro/lem-pygments-colorthemes/stargazers).
  * compared to icl: has an interactive debugger, has a `!` shell shortcut, has an `%edit` command, has classic readline-based autocompletion (icl has a drop-down), not based on Slynk, can't connect to a running Lisp image.
* [cl-isocline](https://codeberg.org/digikar/cl-isocline/) - contains `isocline-repl`, a feature-rich Common Lisp REPL with support for: multiline editing, history, syntax highlighting, basic debugging.
* [magic-ed](https://github.com/sanel/magic-ed) [![GitHub stars](https://img.shields.io/github/stars/sanel/magic-ed?style=flat)](https://github.com/sanel/magic-ed/stargazers) - a tiny editing facility, where you can directly load, edit, manipulate and evaluate file or file content from the REPL, when going to a full IDE is too much. [MIT][200].

<!-- See also: -->

<!-- * [cl-web-editor](https://git.sr.ht/~hajovonta/cl-web-editor) - a simple in-browser editor that does on-the-fly form validation and instant REPL results. MIT. -->

## Online editors ##

* [Judge0 IDE](https://ide.judge0.com/?lUpj) is an online editor which supports Common Lisp (SBCL). [MIT][200].
* [Riju](https://riju.codes/commonlisp), a "fast online playground for every programming language", supports Common Lisp (SBCL).


Text and binary parsers
============================

* ⭐ [esrap](https://github.com/scymtym/esrap) [![GitHub stars](https://img.shields.io/github/stars/scymtym/esrap?style=flat)](https://github.com/scymtym/esrap/stargazers) - Parsing Grammar, Packrat parser, TDPL features and more. [Expat][14].
* [parseq](https://github.com/mrossini-ethz/parseq) [![GitHub stars](https://img.shields.io/github/stars/mrossini-ethz/parseq?style=flat)](https://github.com/mrossini-ethz/parseq/stargazers) - a library for parsing sequences such as strings and lists using Parsing Expression Grammars (PEGs). Inspired by Esrap. GPL2.
* [uclp](https://github.com/ravi-delia/uclp) [![GitHub stars](https://img.shields.io/github/stars/ravi-delia/uclp?style=flat)](https://github.com/ravi-delia/uclp/stargazers) -  An experimental implementation of parsing expression grammars (PEGs, a la Janet) in Common Lisp. MIT.
* [alexa](https://github.com/quil-lang/alexa) [![GitHub stars](https://img.shields.io/github/stars/quil-lang/alexa?style=flat)](https://github.com/quil-lang/alexa/stargazers) -  A Lexical Analyzer Generator. [BSD_3Clause][15].
  - ALEXA is a tool similar to lex or flex for generating lexical analyzers. Unlike tools like lex, however, ALEXA defines a domain-specific language within your Lisp program, so you don't need to invoke a separate tool.
* [cl-yacc](https://github.com/jech/cl-yacc) [![GitHub stars](https://img.shields.io/github/stars/jech/cl-yacc?style=flat)](https://github.com/jech/cl-yacc/stargazers) - a LALR(1) parser generator. [MIT][200].
* [cl-shlex](https://github.com/ruricolist/cl-shlex/) [![GitHub stars](https://img.shields.io/github/stars/ruricolist/cl-shlex/?style=flat)](https://github.com/ruricolist/cl-shlex//stargazers) - simple lexical analyzer for shell-like syntaxes. [MIT][200].
* [smug](https://github.com/drewc/smug) [![GitHub stars](https://img.shields.io/github/stars/drewc/smug?style=flat)](https://github.com/drewc/smug/stargazers) - parser combinators for Common Lisp. SMUG makes it simple to create quick extensible recursive descent parsers without funky syntax or impenetrable macrology. [MIT][200].
* [MaxPC](https://github.com/eugeneia/maxpc) [![GitHub stars](https://img.shields.io/github/stars/eugeneia/maxpc?style=flat)](https://github.com/eugeneia/maxpc/stargazers) - a simple and pragmatic library for writing parsers and lexers based on combinatory parsing.
  * MaxPC is capable of parsing deterministic, context-free languages, provides powerful tools for parse tree transformation and error handling, and can operate on sequences and streams.
  * excellent documentation.
* [parcom](https://github.com/fosskers/parcom) [![GitHub stars](https://img.shields.io/github/stars/fosskers/parcom?style=flat)](https://github.com/fosskers/parcom/stargazers) - Simple parser combinators for Common Lisp, in the style of Haskell’s `parsec` and Rust’s `nom`. [MPL-2.0][211].

See also:

* [lisp-binary](https://github.com/j3pic/lisp-binary) [![GitHub stars](https://img.shields.io/github/stars/j3pic/lisp-binary?style=flat)](https://github.com/j3pic/lisp-binary/stargazers) - A library to easily read and write complex binary formats. [GPL3][2].
* [texp](https://github.com/eugeneia/texp/) [![GitHub stars](https://img.shields.io/github/stars/eugeneia/texp/?style=flat)](https://github.com/eugeneia/texp//stargazers) - A DSL to generate TeX. [AGPL-3.0][agpl3].

Text Processing
===============

* [montezuma](https://github.com/sharplispers/montezuma/) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/montezuma/?style=flat)](https://github.com/sharplispers/montezuma//stargazers) -  Full-text indexing and search for Common Lisp. [Expat][14].
* [mk-string-metrics](https://github.com/cbaggers/mk-string-metrics) [![GitHub stars](https://img.shields.io/github/stars/cbaggers/mk-string-metrics?style=flat)](https://github.com/cbaggers/mk-string-metrics/stargazers) -
  Calculate various string metrics efficiently in Common Lisp
  (Damerau-Levenshtein, Hamming, Jaro, Jaro-Winkler, Levenshtein,
  etc). [MIT][200].
* [wiki-lang-detect](https://github.com/vseloved/wiki-lang-detect) [![GitHub stars](https://img.shields.io/github/stars/vseloved/wiki-lang-detect?style=flat)](https://github.com/vseloved/wiki-lang-detect/stargazers) -
Text language identification using Wikipedia data. No license specified.
* [cl-phonetic](https://github.com/bgutter/cl-phonetic) [![GitHub stars](https://img.shields.io/github/stars/bgutter/cl-phonetic?style=flat)](https://github.com/bgutter/cl-phonetic/stargazers) - Phonetic pattern matching library for Common Lisp (intended to replace the Sylvia library for Python). [MIT][200].
* [cl-string-generator](https://github.com/pokepay/cl-string-generator) [![GitHub stars](https://img.shields.io/github/stars/pokepay/cl-string-generator?style=flat)](https://github.com/pokepay/cl-string-generator/stargazers) -  Generate string from regular expression. [MIT][200].
* [trivial-sanitize](https://codeberg.org/cage/trivial-sanitize) -  clean html strings: `"<a>foo</a>"` → `"foo"`. [LLGPL][8].

See also:

* [Resolve](https://github.com/GrammaTech/resolve) [![GitHub stars](https://img.shields.io/github/stars/GrammaTech/resolve?style=flat)](https://github.com/GrammaTech/resolve/stargazers) - A software for AST-based diff calculation, display, and automated resolution. Written in C++ and CL, you'll find Lisp utilities.

Tools
=====

These are applications or bits of code that make development in Common Lisp easier without being Common Lisp libraries themselves.

* [quicksearch](https://github.com/tkych/quicksearch) [![GitHub stars](https://img.shields.io/github/stars/tkych/quicksearch?style=flat)](https://github.com/tkych/quicksearch/stargazers) - Look up online libraries from the REPL. [Expat][14].
* [lake](https://github.com/takagi/lake) [![GitHub stars](https://img.shields.io/github/stars/takagi/lake?style=flat)](https://github.com/takagi/lake/stargazers) - a GNU make like build utility. [MIT][200].


Unit Testing
============

* ⭐ [FiveAM](https://github.com/sionescu/fiveam) [![GitHub stars](https://img.shields.io/github/stars/sionescu/fiveam?style=flat)](https://github.com/sionescu/fiveam/stargazers) - Simple regression testing framework. [FreeBSD][39].
  * [FiveAM documentation](https://fiveam.common-lisp.dev/docs/index.html)
  * [fiveam-matchers](https://github.com/tdrhq/fiveam-matchers/) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/fiveam-matchers/?style=flat)](https://github.com/tdrhq/fiveam-matchers//stargazers) -  an extensible, composable matchers library for fiveam. [Apache2.0][89].
* [Parachute](https://codeberg.org/shinmera/parachute) - An extensible and cross-compatible testing framework. With test dependencies, conditions, fixtures and restarts. [zlib][33].
* [CLUnit2](https://codeberg.org/cage/clunit2/) - A unit testing library. [MIT][200].
* [Mockingbird](https://github.com/Chream/mockingbird) [![GitHub stars](https://img.shields.io/github/stars/Chream/mockingbird?style=flat)](https://github.com/Chream/mockingbird/stargazers) - A small
  stubbing and mocking library for Common Lisp. Can also check wether
  a stubbed function was called, how many times and with which
  arguments. [MIT][200].
* [cl-mock](https://github.com/Ferada/cl-mock) [![GitHub stars](https://img.shields.io/github/stars/Ferada/cl-mock?style=flat)](https://github.com/Ferada/cl-mock/stargazers) - Another mocking library. It has more features than Mockingbird, like pattern matching on the mocked call, etc.
* [Check-it](https://github.com/DalekBaldwin/check-it) [![GitHub stars](https://img.shields.io/github/stars/DalekBaldwin/check-it?style=flat)](https://github.com/DalekBaldwin/check-it/stargazers) - A QuickCheck-style randomized property-based testing. [LLGPL][8].
* [cl-coveralls](https://github.com/fukamachi/cl-coveralls) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/cl-coveralls?style=flat)](https://github.com/fukamachi/cl-coveralls/stargazers) - a helper
  library to post test coverage to Coveralls. See [SBCL's code coverage tool](http://www.sbcl.org/manual/index.html#sb_002dcover). [FreeBSD][39].
* [CheckL](https://github.com/rpav/CheckL/) [![GitHub stars](https://img.shields.io/github/stars/rpav/CheckL/?style=flat)](https://github.com/rpav/CheckL//stargazers) - Why write programs in Common Lisp but tests like Java? Meet CheckL!
  * a testing library that checks the current test value against the previous one and offers restarts.
* [Try](https://github.com/melisgl/try) [![GitHub stars](https://img.shields.io/github/stars/melisgl/try?style=flat)](https://github.com/melisgl/try/stargazers) - Try is an extensible test anti-framework with equal support for interactive and non-interactive workflows, as well as Emacs integration. [MIT][200].

See also:

* [testiere](https://cicadas.surf/cgit/colin/testiere.git/about/) - a testing utility where tests are included at the top of a `defun/t` form. They are run when you recompile your functions interactively. With mocking and stubbing support. [GPL3][2].
  * [testiere-mode](https://github.com/dotemacs/testiere-mode.el) [![GitHub stars](https://img.shields.io/github/stars/dotemacs/testiere-mode.el?style=flat)](https://github.com/dotemacs/testiere-mode.el/stargazers) for Emacs, to hide and show the `#+testiere` section.
* [cl-hamcrest](https://github.com/40ants/cl-hamcrest) [![GitHub stars](https://img.shields.io/github/stars/40ants/cl-hamcrest?style=flat)](https://github.com/40ants/cl-hamcrest/stargazers) -  a set of [Hamcrest](https://hamcrest.org/) matchers that can be combined to create flexible expressions of intent. Helps make your unittests more readable by using  assertions such as `has-plist-entries`, `has-slots`, `has-length`, `contains`, `contains-in-any-order`, `has-all`… [BSD_3Clause][15].

Editor utilities:

* [Slite](https://github.com/tdrhq/slite/) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/slite/?style=flat)](https://github.com/tdrhq/slite//stargazers) - a SLIme-based TEst runner for FiveAM Tests. [Apache2.0][89]
  - Slite interactively runs your Common Lisp tests (at the time of writing only FiveAM is supported). It allows you to see the summary of test failures, jump to test definitions, rerun tests with the debugger, all from inside Emacs.

CI utilities:

* [CI-utils](https://github.com/neil-lindquist/CI-Utils) [![GitHub stars](https://img.shields.io/github/stars/neil-lindquist/CI-Utils?style=flat)](https://github.com/neil-lindquist/CI-Utils/stargazers) (low activity) - a set of utilities and examples for working on continuous integration platforms, including a run script for the Fiveam test library.
  * helps run Fiveam tests with the right exit code.
  * integrated with Roswell.

For more: [Sabra Crolleton's extensive test frameworks comparison](https://sabracrolleton.github.io/testing-framework).


Utilities
=========

Caching (serialization)
-----------------------

* [cl-store](https://github.com/skypher/cl-store) [![GitHub stars](https://img.shields.io/github/stars/skypher/cl-store?style=flat)](https://github.com/skypher/cl-store/stargazers) - a portable serialization package which gives you the ability to store all common-lisp data types into streams. MIT.
  * Call `store object "file.bin")` to store a (possibly compound) lisp object to disk, and `restore` to get it back.
* [clache](https://github.com/html/clache) [![GitHub stars](https://img.shields.io/github/stars/html/clache?style=flat)](https://github.com/html/clache/stargazers) - General caching facility. Cache any Lisp object on disk or in memory.  [LLGPL][8].
  * built on cl-store
  * a cache can be persistent or have an expiration time.
  * exposes the store locations too.
* [conspack](https://github.com/conspack/cl-conspack) [![GitHub stars](https://img.shields.io/github/stars/conspack/cl-conspack?style=flat)](https://github.com/conspack/cl-conspack/stargazers) - binary serialization.
* [cl-naive-store](https://gitlab.com/naive-x/cl-naive-store) - a naive persisted, in memory (lazy loading), indexed, document store for Common Lisp. [MIT][200].
  - see [the introductory blog post](https://zaries.wordpress.com/2022/05/31/cl-naive-store/)
  - dare we add: used in production by the author's company (ASTN Group, see [awesome-lisp-companies](https://github.com/azzamsa/awesome-lisp-companies/) [![GitHub stars](https://img.shields.io/github/stars/azzamsa/awesome-lisp-companies/?style=flat)](https://github.com/azzamsa/awesome-lisp-companies//stargazers))
* 🚀 [cl-binary-store](https://github.com/ajberkley/cl-binary-store) [![GitHub stars](https://img.shields.io/github/stars/ajberkley/cl-binary-store?style=flat)](https://github.com/ajberkley/cl-binary-store/stargazers) -  A fast Common Lisp binary serializer/deserializer. BSD_3Clause. See [reddit announce](https://www.reddit.com/r/Common_Lisp/comments/1hz5879/new_binary_serializationdeserialization_library/) (2025).
  * "A super fast and customizable serializer/deserializer of Common Lisp objects to/from a very compact binary format. Equality of objects, circular references, and the full Common Lisp type system are supported. Specialized arrays (on SBCL) are stored/restore at lightning speed."

See also the [Persistent object databases](#persistent-object-databases) section.


Caching (memoization)
-----------------------

* [function-cache](https://github.com/AccelerationNet/function-cache) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/function-cache?style=flat)](https://github.com/AccelerationNet/function-cache/stargazers) -  A Common Lisp function caching / memoization library. [BSD][15].


Compression / decompression
---------------------------

* [chipz](https://github.com/froydnj/chipz) [![GitHub stars](https://img.shields.io/github/stars/froydnj/chipz?style=flat)](https://github.com/froydnj/chipz/stargazers) - A decompression library. [3-clause BSD][15].
* [Salza2](http://www.xach.com/lisp/salza2/) - A library for creating compressed data. [FreeBSD][39].
* [zippy](https://codeberg.org/shinmera/zippy) -  A ZIP archive format library based on 3bz. [zlib][33].
* [archive](https://github.com/froydnj/archive) [![GitHub stars](https://img.shields.io/github/stars/froydnj/archive?style=flat)](https://github.com/froydnj/archive/stargazers) - a library for reading and creating archive (tar, cpio) files. [BSD_3Clause][15]. A pure Common Lisp replacement for the `tar` program.
  * see its recent fork [cl-tar](https://common-lisp.net/project/cl-tar/) (2021). [Announce](https://www.timmons.dev/posts/new-project-cl-tar.html).
* [deoxybyte-gzip](https://github.com/keithj/deoxybyte-gzip) [![GitHub stars](https://img.shields.io/github/stars/keithj/deoxybyte-gzip?style=flat)](https://github.com/keithj/deoxybyte-gzip/stargazers) -  Common Lisp interface to zlib via CFFI. GPL3.
  * This system provides gzip and gunzip functions and a Gray-streams implementation, both built on a set of lower-level zlib functions.


Configuration
-------------

* 👍 [py-configparser](https://common-lisp.net/project/py-configparser/) - reads and writes Python's ConfigParser-like configuration files. [MIT][200].
* [envy](https://github.com/fukamachi/envy) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/envy?style=flat)](https://github.com/fukamachi/envy/stargazers) - Configuration switcher. [FreeBSD][39].
* [chameleon](https://github.com/sheepduke/chameleon/) [![GitHub stars](https://img.shields.io/github/stars/sheepduke/chameleon/?style=flat)](https://github.com/sheepduke/chameleon//stargazers) - a configuration management library shipped with profile support. [MIT][200].

Date and time
-------------

* ⭐ [local-time](https://codeberg.org/dlowe/local-time) - A development library for manipulating date and time information in a semi-standard manner. [3-clause BSD][15].
  * [local-time documentation](https://local-time.common-lisp.dev/), [github mirror](https://github.com/dlowe-net/local-time) [![GitHub stars](https://img.shields.io/github/stars/dlowe-net/local-time?style=flat)](https://github.com/dlowe-net/local-time/stargazers).
* [fuzzy-dates](https://codeberg.org/shinmera/fuzzy-dates) -  A library to fuzzily parse date and time strings. Zlib.
* [cl-date-time-parser](https://github.com/tkych/cl-date-time-parser) [![GitHub stars](https://img.shields.io/github/stars/tkych/cl-date-time-parser?style=flat)](https://github.com/tkych/cl-date-time-parser/stargazers) - Parse date-time-string, liberally. Hides the difference between date-time formats, and enables to manage date and time as the one date-time format. [MIT][200].
* [chronicity](https://github.com/chaitanyagupta/chronicity) [![GitHub stars](https://img.shields.io/github/stars/chaitanyagupta/chronicity?style=flat)](https://github.com/chaitanyagupta/chronicity/stargazers) - A natural language date and time parse, to parse strings like "3 days from now". [BSD_3Clause][15].
* [local-time-duration](https://github.com/enaeher/local-time-duration) [![GitHub stars](https://img.shields.io/github/stars/enaeher/local-time-duration?style=flat)](https://github.com/enaeher/local-time-duration/stargazers) -
Duration processing library built on top of local-time. [MIT][200].
  * see this fork: [humanize-duration](https://github.com/40ants/humanize-duration) [![GitHub stars](https://img.shields.io/github/stars/40ants/humanize-duration?style=flat)](https://github.com/40ants/humanize-duration/stargazers), that outputs only significant parts of a duration object. Has localization suport.
* [iso-8601-date](https://gitlab.com/DataLinkDroid/iso-8601-date) - Miscellaneous date routines in Common Lisp, based around the ISO 8601 string representation. [LLGPL][8].
* [calendar-times](https://github.com/copyleft/calendar-times) [![GitHub stars](https://img.shields.io/github/stars/copyleft/calendar-times?style=flat)](https://github.com/copyleft/calendar-times/stargazers) - a calendar time library implemented on top of the LOCAL-TIME library. It features zoned calendar times and calculations.
  * see also: [calendar-date](https://github.com/takagi/calendar-date) [![GitHub stars](https://img.shields.io/github/stars/takagi/calendar-date?style=flat)](https://github.com/takagi/calendar-date/stargazers) - a Gregorian calendar date library. [MIT][200].
* [periods](https://github.com/jwiegley/periods) [![GitHub stars](https://img.shields.io/github/stars/jwiegley/periods?style=flat)](https://github.com/jwiegley/periods/stargazers) - manipulating date/time objects at a higher level. With series-compatible data structure. [BSD_3Clause][15].
  * with [some documentation](https://lisp-maintainers.github.io/periods/)
* [stopclock](https://github.com/Gleefre/stopclock) [![GitHub stars](https://img.shields.io/github/stars/Gleefre/stopclock?style=flat)](https://github.com/Gleefre/stopclock/stargazers) - a library for measuring time using (stop)clocks. It allows you to create a clock, pause it, resume it and change its speed. [Apache2.0][89].

See also the book [Calendrical calculations](https://www.cambridge.org/us/academic/subjects/computer-science/computing-general-interest/calendrical-calculations-ultimate-edition-4th-edition?format=HB#resources), by Edward M. Reingold, Nachum Dershowitz, Cambridge Press. It provides Lisp sources.

Data validation
---------------

* [clavier](https://github.com/mmontone/clavier) [![GitHub stars](https://img.shields.io/github/stars/mmontone/clavier?style=flat)](https://github.com/mmontone/clavier/stargazers) - General purpose validation library for Common Lisp. [MIT][200].
* [ratify](https://codeberg.org/shinmera/ratify) - A collection of utilities to ratify, validate and parse inputs. [zlib][33].
* [json-schema](https://github.com/fisxoj/json-schema) [![GitHub stars](https://img.shields.io/github/stars/fisxoj/json-schema?style=flat)](https://github.com/fisxoj/json-schema/stargazers) - A library for validating data against schemas of drafts 4, 6, 7, and 2019-09 of the [JSON Schema](https://json-schema.org/) standard. [LLGPL][8].
* [sanity-clause](https://github.com/fisxoj/sanity-clause) [![GitHub stars](https://img.shields.io/github/stars/fisxoj/sanity-clause?style=flat)](https://github.com/fisxoj/sanity-clause/stargazers) - a data serialization/contract library for Common Lisp. Schemas can be property lists or class-based, allowing to check slots' types during `make-instance`. [LLGPL][8].
* [cl-semver](https://github.com/cldm/cl-semver) [![GitHub stars](https://img.shields.io/github/stars/cldm/cl-semver?style=flat)](https://github.com/cldm/cl-semver/stargazers) - Implementation of the [Semantic Versioning](https://semver.org) Specification. [MIT][200]

Developer utilities
-------------------

Common Lisp implementations have plenty of debugging tools. See: [Cookbook / debugging](https://lispcookbook.github.io/cl-cookbook/debugging.html). Those are additional utilities.


* [repl-utilities](https://github.com/m-n/repl-utilities) [![GitHub stars](https://img.shields.io/github/stars/m-n/repl-utilities?style=flat)](https://github.com/m-n/repl-utilities/stargazers) - Ease
common tasks at the REPL (print documentation, print external symbols,
call hooks when loading a package,…). [BSD_2Clause][17].
* [flight-recorder](https://github.com/vseloved/flight-recorder) [![GitHub stars](https://img.shields.io/github/stars/vseloved/flight-recorder?style=flat)](https://github.com/vseloved/flight-recorder/stargazers) - a robust REPL history facility.
* [tracer](https://github.com/TeMPOraL/tracer) [![GitHub stars](https://img.shields.io/github/stars/TeMPOraL/tracer?style=flat)](https://github.com/TeMPOraL/tracer/stargazers) - tracing profiler for Common Lisp, with output suitable for display in Chrome’s/Chromium’s Tracing Viewer. [MIT][200].
* [cl-flamegraph](https://github.com/40ants/cl-flamegraph) [![GitHub stars](https://img.shields.io/github/stars/40ants/cl-flamegraph?style=flat)](https://github.com/40ants/cl-flamegraph/stargazers) - A wrapper around SBCL's statistical profiler, to generate FlameGraph charts for Common Lisp programs. [BSD][15].
* [supertrace](https://github.com/fukamachi/supertrace) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/supertrace?style=flat)](https://github.com/fukamachi/supertrace/stargazers) - Superior Common Lisp `trace` functionality for debugging/profiling. Trace many functions at once, use before and after hooks. [BSD_2Clause][17].
* [printv](https://github.com/danlentz/printv) [![GitHub stars](https://img.shields.io/github/stars/danlentz/printv?style=flat)](https://github.com/danlentz/printv/stargazers) -  A batteries-included tracing and debug-logging macro. [Apache2][89].
* [journal](https://github.com/melisgl/journal) [![GitHub stars](https://img.shields.io/github/stars/melisgl/journal?style=flat)](https://github.com/melisgl/journal/stargazers) - a library for logging, tracing, record-and-replay testing and persistence. MIT.
* [brake](https://github.com/varjagg/brake) [![GitHub stars](https://img.shields.io/github/stars/varjagg/brake?style=flat)](https://github.com/varjagg/brake/stargazers) -  An extended breakpoint facility for Common Lisp. [MIT][200].
* [cl-codegraph](https://sr.ht/~hajovonta/cl-codegraph/) - Automatic Knowledge Graph of Common Lisp code via live image introspection.
  * Given a package loaded in the SBCL image, builds and maintains a
    graph of its symbols, class hierarchies, method
    specializations, call relationships, and metadata — all without
    parsing source code. Includes a live Emacs integration that shows
    code intelligence as you navigate and a web-based graph viewer.

and also:

* [GTFL](http://www.martin-loetzsch.de/gtfl/) - A graphical terminal for Lisp, meant for Lisp programmers who want to debug or visualize their own algorithms. A graphical trace in the browser. BSD-style.
* [trivial-benchmark](https://codeberg.org/shinmera/trivial-benchmark) - Tiny benchmarking library. [zlib][33].
  * a similar macro (`benchmark`) is part of [trivial-time](https://github.com/aartaka/trivial-time) [![GitHub stars](https://img.shields.io/github/stars/aartaka/trivial-time?style=flat)](https://github.com/aartaka/trivial-time/stargazers), providing support for more implementations (ABCL, Allegro, CCL, CLISP, ECL).
  * Indeed, most trivial-benchmark's metrics are only implemented on SBCL. On other implementations, it measures real and user-space time (and not bytes allocated (it does for ECL), system run-time or GC run-time).
* [glyphs](https://github.com/ahungry/glyphs/) [![GitHub stars](https://img.shields.io/github/stars/ahungry/glyphs/?style=flat)](https://github.com/ahungry/glyphs//stargazers) - A library for cutting down the verboseness of Common Lisp in places. [GNU GPL3][2].
* [Lisp REPL core dumper](https://gitlab.com/ambrevar/lisp-repl-core-dumper/) -
A portable wrapper to generate Lisp cores on demand to start REPL blazing fast.
It can preload provided systems to help build a collection of specialized
Lisp cores.


Documentation builders
----------------------

* [Staple](https://codeberg.org/shinmera/staple) - a tool to generate documentation pages using an HTML template. Uses the existing README, adds docstrings, crossreferences and links to the CLHS. [zlib][33].
* [mgl-pax](https://github.com/melisgl/mgl-pax) [![GitHub stars](https://img.shields.io/github/stars/melisgl/mgl-pax?style=flat)](https://github.com/melisgl/mgl-pax/stargazers) - Exploratory
programming environment and documentation generator. one may
accomplish similar effects as with Literate Programming, but
documentation is generated from code, not vice versa. Code is first,
code must look pretty, documentation is code. [MIT][200].
  - also PDF export
  - see this [40ants/doc](https://github.com/40ants/doc) [![GitHub stars](https://img.shields.io/github/stars/40ants/doc?style=flat)](https://github.com/40ants/doc/stargazers) fork: a lighter core system, a JavaScript search index, multiple format output, HTML themes, RSS and Atom feed for the Changelog and more.
* [sphinxcontrib-cldomain](https://sphinxcontrib-cldomain.russellsim.org/) -
  Extending Sphinx to cover Common Lisp. To build documentation with
  the same ease as sphinx would a Python project. [GPL3][2]
  - crossreferences, links to the CLHS, symbol index, search, and all Sphinx features.
* [Codex](https://github.com/CommonDoc/codex) [![GitHub stars](https://img.shields.io/github/stars/CommonDoc/codex?style=flat)](https://github.com/CommonDoc/codex/stargazers) - A beautiful documentation system for Common Lisp. [MIT][200].
* [QBook](https://github.com/mmontone/qbook) [![GitHub stars](https://img.shields.io/github/stars/mmontone/qbook?style=flat)](https://github.com/mmontone/qbook/stargazers) - generates HTML (or LaTeX) formatted code listings of Common Lisp source files. [BSD_3Clause][15].
  - all comments started with 4 `;` (";;;;") are interpreted as documentation. Enhance the documentation with headings and directives.
  - QBook acts as "a lightweight literate programming system, where Lisp code is not rendered inline, but in separate sections, and that makes the document more pleasant to navigate." @mmontone
* [Declt](https://github.com/didierverna/declt) [![GitHub stars](https://img.shields.io/github/stars/didierverna/declt?style=flat)](https://github.com/didierverna/declt/stargazers) - Reference manual generator for Common Lisp libraries. Builds a texinfo document that can be further processed into various formats, such as HTML or PDF. BSD.
* [cl-bibtex](https://github.com/mkoeppe/cl-bibtex) [![GitHub stars](https://img.shields.io/github/stars/mkoeppe/cl-bibtex?style=flat)](https://github.com/mkoeppe/cl-bibtex/stargazers) - A compatible re-implementation of the BibTeX program in Common Lisp, with a BST-to-CL compiler. [GNU LGPL2.1][11].
* [adp](https://github.com/HectareaGalbis/adp) [![GitHub stars](https://img.shields.io/github/stars/HectareaGalbis/adp?style=flat)](https://github.com/HectareaGalbis/adp/stargazers) -  Common Lisp documentation generator using Scribble files. [MIT][200].
* 🟢 [NEW in 2025] [HyperDoc](https://hyperdoc.khinsen.net/) - scientific publications that combine code, data, and computed results with explanatory text, and software documentation that is an integral part of a software system, rather than a pile of documents remaining outside of it.


An overview blog post with even more documentation generators: https://lisp-journey.gitlab.io/blog/overview-of-documentation-generators/ and a dedicated site with reviews and demos: https://cl-doc-systems.github.io/

You might also like: [literate programming systems](#literate-programming).

Documentation lookup
--------------------

`apropos` and `ppcre:regex-apropos` search in function names.

* [docbrowser](https://github.com/lokedhs/docbrowser) [![GitHub stars](https://img.shields.io/github/stars/lokedhs/docbrowser?style=flat)](https://github.com/lokedhs/docbrowser/stargazers) - a server that generates documentation for the loaded systems on the fly.
  - Its main page presents a list of all loaded systems in your Lisp image. Click on one system, and you get a page with three panes: functions, classes and variables. Click on a function to see its source, in context, with line numbers. Click on classes to see their slots and specializing functions.
* [cl-livedocs](https://github.com/mmontone/cl-livedocs) [![GitHub stars](https://img.shields.io/github/stars/mmontone/cl-livedocs?style=flat)](https://github.com/mmontone/cl-livedocs/stargazers) - similar and newer, based on Webinfo.
    * full text search is enabled by default.
* [cl-docsearch](https://github.com/digikar99/cl-docsearch) [![GitHub stars](https://img.shields.io/github/stars/digikar99/cl-docsearch?style=flat)](https://github.com/digikar99/cl-docsearch/stargazers) -  A tool to search documentation of lisp symbols in the current lisp image.
  * indexes and searches the documentation string too.
  * [docsearch-ollama](https://github.com/digikar99/cl-docsearch/blob/main/README-docsearch-ollama.md) [![GitHub stars](https://img.shields.io/github/stars/digikar99/cl-docsearch/blob/main/README-docsearch-ollama.md?style=flat)](https://github.com/digikar99/cl-docsearch/blob/main/README-docsearch-ollama.md/stargazers) provides Common Lisp documentation search functionality through Ollama. It computes and caches embeddings corresponding to symbol documentation, and looks up user queries by comparing the cosine similarity of the query embedding with symbol documentation embeddings.
    * we can do something like: `(query "How do I remove whitespace from the ends of a string?")`

mgl-pax (see above) also has a live documentation browser. [doc](https://melisgl.github.io/mgl-pax-world/mgl-pax-manual.html#MGL-PAX:@BROWSING-LIVE-DOCUMENTATION%20MGL-PAX:SECTION) and [demo video](https://www.youtube.com/watch?v=4bl8PS8OW94&list=PLxbqYr4DvjX68AEdLky4IiHG69VJu6f5s).


Files and directories
---------------------

* ⭐ [uiop](https://common-lisp.net/project/asdf/uiop.html) and its `pathname` package
  (replaces [cl-fad](http://weitz.de/cl-fad/)). uiop is part of ASDF3
  and as thus is shipped in many implementations. [MIT][200].
* [pathname-utils](https://codeberg.org/shinmera/pathname-utils) - A collection of utilities to help with pathname operations. [zlib][33].
  * [filesystem-utils](https://codeberg.org/shinmera/filesystem-utils) - deal with common problems with filesystems, such as listing files, probing file types, determining default directories, etc.
  * no dependencies, doesn't access the filesystem.
  * [file-attributes](https://codeberg.org/shinmera/file-attributes) -  access to common file attributes (uid, gid, permissions, ctime, mtime, atime).
* [filepaths](https://github.com/fosskers/filepaths) [![GitHub stars](https://img.shields.io/github/stars/fosskers/filepaths?style=flat)](https://github.com/fosskers/filepaths/stargazers) -  Modern and consistent filepath manipulation for Common Lisp. [LGPL3][9].
  * no dependencies, doesn't access the filesystem.
* [file-finder](https://github.com/lisp-maintainers/file-finder/) [![GitHub stars](https://img.shields.io/github/stars/lisp-maintainers/file-finder/?style=flat)](https://github.com/lisp-maintainers/file-finder//stargazers) - File-object finder Common Lisp library. Enable rapid file search, inspection and manipulation. [GPL3][2].
* [osicat](https://common-lisp.net/project/osicat/) - A lightweight operating system interface on POSIX-like systems, including Windows (directory iteration and deletion, file permissions, file-type identification, etc) [Expat][14].
  * note: Osicat isn't a pure Lisp library, it relies on compiling C code and this might make your deployment harder.
* [ppath](https://codeberg.org/fourier/ppath) - Common Lisp's implementation of the Python's os.path module. [BSD][15].
* [mmap](https://codeberg.org/shinmera/mmap) - Portable mmap file memory mapping utility library. [zlib][33].
* [nfiles](https://github.com/atlas-engineer/nfiles) [![GitHub stars](https://img.shields.io/github/stars/atlas-engineer/nfiles?style=flat)](https://github.com/atlas-engineer/nfiles/stargazers) - File persistence, watching, data synchronization, (per user profile) path resolution, and structured data retrieval. Has pre-defined classes for configuration files, remote fetched files, data files, Lisp-readable files and many others. [BSD][15].
* [trivial-glob](https://github.com/fukamachi/trivial-glob) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/trivial-glob?style=flat)](https://github.com/fukamachi/trivial-glob/stargazers) -  Shell-style glob pattern matching and filesystem globbing for Common Lisp. MIT.
  * `(glob "**/*.lisp")`

File watching libraries:

* [file-notify](https://codeberg.org/shinmera/file-notify) - a cross-platform library for file change detection. [zlib][33].

Git
---

* [cl-git](https://cl-git.russellsim.org/) - a CFFI interface to the libgit2 library. [LGPL3][9].
* [legit](https://shinmera.github.io/legit/) - an interface to the Git binary. [zlib][33].
* [git-api](https://codeberg.org/fourier/git-api) - Common Lisp library to access a git repository. It doesn't need git or libgit installed. [BSD][15].

See also the [Lem editor's Git interface](https://lem-project.github.io/usage/usage/#version-control-with-lemlegit-git-experimental)!

i18n
----

* [cl-i18n](https://codeberg.org/cage/cl-i18n) - an i18n library. Load translations from GNU gettext text or binary files or from its native format. Localisation helpers of plural forms. [LLGPL][8].
* [gettext](https://github.com/rotatef/gettext) [![GitHub stars](https://img.shields.io/github/stars/rotatef/gettext?style=flat)](https://github.com/rotatef/gettext/stargazers) -  a port of the gettext runtime to Common Lisp. [GPL3][2].
* [fluent](https://github.com/fosskers/fluent) [![GitHub stars](https://img.shields.io/github/stars/fosskers/fluent?style=flat)](https://github.com/fosskers/fluent/stargazers) - implementation of [Fluent](https://github.com/projectfluent/fluent/) [![GitHub stars](https://img.shields.io/github/stars/projectfluent/fluent/?style=flat)](https://github.com/projectfluent/fluent//stargazers), a modern localisation system. MPL-2.0.

See also:

* [translate](https://github.com/dkochmanski/translate) [![GitHub stars](https://img.shields.io/github/stars/dkochmanski/translate?style=flat)](https://github.com/dkochmanski/translate/stargazers) - seamless language localization. LLGPL.
* [enchant](https://github.com/tlikonen/cl-enchant) [![GitHub stars](https://img.shields.io/github/stars/tlikonen/cl-enchant?style=flat)](https://github.com/tlikonen/cl-enchant/stargazers) - bindings for the Enchant spell-checker library. Public domain.
* [oxenfurt](https://codeberg.org/shinmera/oxenfurt) - A  client library for the Oxford dictionary API. [zlib][33].
* [language-codes](https://shinmera.github.io/language-codes) - A database library for ISO language codes. [zlib][33]
* [system-locale](https://shinmera.github.io/system-locale) - A library to retrieve the user's preferred language, so that your application may choose a sensible default. [zlib][33].
* [multilang-documentation](https://shinmera.github.io/multilang-documentation) - Allows writing docstrings in multiple languages, for truly internationally documented libraries. [zlib][33].

Linting, code formatting
------------------------

* [sblint](https://github.com/fukamachi/sblint) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/sblint?style=flat)](https://github.com/fukamachi/sblint/stargazers) - a linter for Common Lisp source code using SBCL, suited for Reviewdog ([slides](http://www.slideshare.net/fukamachi/sblint)). [BSD_2Clause][17].
* [mallet](https://github.com/fukamachi/mallet) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/mallet?style=flat)](https://github.com/fukamachi/mallet/stargazers) -  A sensible Common Lisp linter that catches real mistakes, not style. MIT.
* [ocicl](https://github.com/ocicl/ocicl/) [![GitHub stars](https://img.shields.io/github/stars/ocicl/ocicl/?style=flat)](https://github.com/ocicl/ocicl//stargazers)'s built-in linter and auto-fix feature.
* [trivial-formatter](https://github.com/hyotang666/trivial-formatter) [![GitHub stars](https://img.shields.io/github/stars/hyotang666/trivial-formatter?style=flat)](https://github.com/hyotang666/trivial-formatter/stargazers) - code formatter for Common Lisp. [MIT][200].

and also:

* [lisp-format](https://github.com/eschulte/lisp-format) [![GitHub stars](https://img.shields.io/github/stars/eschulte/lisp-format?style=flat)](https://github.com/eschulte/lisp-format/stargazers) and [cl-indentify](https://github.com/yitzchak/cl-indentify) [![GitHub stars](https://img.shields.io/github/stars/yitzchak/cl-indentify?style=flat)](https://github.com/yitzchak/cl-indentify/stargazers).

Literate programming
--------------------

* [literate-lisp](https://github.com/jingtaozf/literate-lisp) [![GitHub stars](https://img.shields.io/github/stars/jingtaozf/literate-lisp?style=flat)](https://github.com/jingtaozf/literate-lisp/stargazers) -  Load Common Lisp code blocks from Emacs' Org files. [MIT][200].
* [erudite](https://github.com/mmontone/erudite) [![GitHub stars](https://img.shields.io/github/stars/mmontone/erudite?style=flat)](https://github.com/mmontone/erudite/stargazers) - Literate Programming System built with interactive development in mind. [MIT][200].
* [papyrus](https://github.com/tani/papyrus) [![GitHub stars](https://img.shields.io/github/stars/tani/papyrus?style=flat)](https://github.com/tani/papyrus/stargazers) - Papyrus makes your markdown executable with the reader macro of Common Lisp.[MIT][200]


Logging
-------

* ⭐ [log4cl](https://github.com/sharplispers/log4cl/) [![GitHub stars](https://img.shields.io/github/stars/sharplispers/log4cl/?style=flat)](https://github.com/sharplispers/log4cl//stargazers) - Logging framework modelled after Log4J. [Apache2.0][89]. Advanced integration with Slime.
  * [log4cl-json](https://github.com/40ants/log4cl-json) [![GitHub stars](https://img.shields.io/github/stars/40ants/log4cl-json?style=flat)](https://github.com/40ants/log4cl-json/stargazers) - JSON appender extension. [BSD][15].
* [verbose](https://shinmera.github.io/verbose) - A fast and highly configurable logging framework. [zlib][33].
* [a-cl-logger](https://github.com/AccelerationNet/a-cl-logger) [![GitHub stars](https://img.shields.io/github/stars/AccelerationNet/a-cl-logger?style=flat)](https://github.com/AccelerationNet/a-cl-logger/stargazers) - Logging library providing context sensitive logging of more than just strings to more than just local files or output streams. Features logstash support, json support, logger hierarchies, context sensitive logging, objects printed as an inspectable presentation,…

To third parties:

* [cl-fluent-logger](https://github.com/fukamachi/cl-fluent-logger) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/cl-fluent-logger?style=flat)](https://github.com/fukamachi/cl-fluent-logger/stargazers) - A Common Lisp structured logger for [Fluentd](https://www.fluentd.org/).

See also: [extensive comparison of logging libraries](https://sabracrolleton.github.io/logging-comparison).

Macro helpers
-------------

* [easy-macros](https://github.com/tdrhq/easy-macros/) [![GitHub stars](https://img.shields.io/github/stars/tdrhq/easy-macros/?style=flat)](https://github.com/tdrhq/easy-macros//stargazers) -  an easy way to write 90% of your macros. [Apache2.0][89].
* [trivial-with-current-source-from](https://github.com/scymtym/trivial-with-current-source-form/) [![GitHub stars](https://img.shields.io/github/stars/scymtym/trivial-with-current-source-form/?style=flat)](https://github.com/scymtym/trivial-with-current-source-form//stargazers) - Helps macro writers produce better errors for macro users. [GPL3][2].

Markdown
--------

* [3bmd](https://github.com/3b/3bmd) [![GitHub stars](https://img.shields.io/github/stars/3b/3bmd?style=flat)](https://github.com/3b/3bmd/stargazers) - a markdown -> html converter. [MIT][200].

Package declarations
-------------------------

* [cl-reexport](https://github.com/takagi/cl-reexport) [![GitHub stars](https://img.shields.io/github/stars/takagi/cl-reexport?style=flat)](https://github.com/takagi/cl-reexport/stargazers) - when you want to import and re-export many symbols at once and `:include` or `:exclude` some.

See also [uiop:define-package](https://common-lisp.net/project/asdf/uiop.html#UIOP_002fPACKAGE) and its `:reexport` clause (without include/exclude), `:recycle`, `mix`…

PDF
---

* [cl-typesetting](https://github.com/mbattyani/cl-typesetting) [![GitHub stars](https://img.shields.io/github/stars/mbattyani/cl-typesetting?style=flat)](https://github.com/mbattyani/cl-typesetting/stargazers) and [cl-pdf](https://github.com/mbattyani/cl-pdf) [![GitHub stars](https://img.shields.io/github/stars/mbattyani/cl-pdf?style=flat)](https://github.com/mbattyani/cl-pdf/stargazers) - cross-platform Common Lisp libraries for generating PDF files. [FreeBSD][39].
* [cl-pslib](https://codeberg.org/cage/cl-pslib) - a (thin) wrapper around the [pslib](http://pslib.sourceforge.net/) library for generating PostScript files. Also [cl-pslib-barcode](https://codeberg.org/cage/cl-pslib-barcode). [LLGPL][8].

Project skeletons
-----------------

* [cl-project](https://github.com/fukamachi/cl-project) [![GitHub stars](https://img.shields.io/github/stars/fukamachi/cl-project?style=flat)](https://github.com/fukamachi/cl-project/stargazers) - General modern project skeletons. [LLGPL][8].
* [cl-project-with-docs](https://github.com/40ants/cl-project-with-docs) [![GitHub stars](https://img.shields.io/github/stars/40ants/cl-project-with-docs?style=flat)](https://github.com/40ants/cl-project-with-docs/stargazers) - uses Sphinx and reStructured text to render nice and readable HTML documentation. [BSD][15].
* [cl-cookieproject](https://github.com/vindarel/cl-cookieproject) [![GitHub stars](https://img.shields.io/github/stars/vindarel/cl-cookieproject?style=flat)](https://github.com/vindarel/cl-cookieproject/stargazers) -  Generate a ready-to-use Common Lisp project. Not in Quicklisp. [BSD_3Clause][15].
  * test definitions, entry point to run from sources, build a binary, Roswell integration…
* [cookiecutter-lisp-game](https://github.com/lockie/cookiecutter-lisp-game) [![GitHub stars](https://img.shields.io/github/stars/lockie/cookiecutter-lisp-game?style=flat)](https://github.com/lockie/cookiecutter-lisp-game/stargazers) - An opinionated cookiecutter template for Common Lisp videogame projects. Allows to choose [backend middleware library](#graphics) between liballegro, raylib and SDL2. Contains CI scripts using [docker-lisp-gamedev](#docker-images) to automatically build binaries for Windows, MacOS and Linux.

Security
--------

* [cl-isolated](https://github.com/kanru/cl-isolated) [![GitHub stars](https://img.shields.io/github/stars/kanru/cl-isolated?style=flat)](https://github.com/kanru/cl-isolated/stargazers) - A restricted environment for Common Lisp code evaluation [AGPL-3.0][agpl3].
* [safe-read](https://github.com/phoe/safe-read) [![GitHub stars](https://img.shields.io/github/stars/phoe/safe-read?style=flat)](https://github.com/phoe/safe-read/stargazers) - a variant of READ secure against internbombing, excessive input and macro characters. [BSD_2Clause][17].
* [secret-values](https://github.com/rotatef/secret-values) [![GitHub stars](https://img.shields.io/github/stars/rotatef/secret-values?style=flat)](https://github.com/rotatef/secret-values/stargazers) -  A Common Lisp library to reduce the risk of accidentally revealing secret values such as passwords.
  * [privacy-output-stream](https://github.com/atgreen/privacy-output-stream) [![GitHub stars](https://img.shields.io/github/stars/atgreen/privacy-output-stream?style=flat)](https://github.com/atgreen/privacy-output-stream/stargazers) - an output stream that masks secret strings with `****`, based on secret-values. MIT.

To safely `read` data, see also `uiop:with-safe-io-syntax` and the
associated `safe-read-*` functions (they ensure we `read` with the
standard readtable and `#.` is inhibited to avoid read-time
evaluation).


System interface
--------------------

* [machine-state](https://codeberg.org/shinmera/machine-state/) -  Retrieve machine state information about CPU time, memory usage, thread processing time, etc.

Other
-----

This contains anything which doesn't fit into another category.

* [babel](https://github.com/cl-babel/babel) [![GitHub stars](https://img.shields.io/github/stars/cl-babel/babel?style=flat)](https://github.com/cl-babel/babel/stargazers) - A charset encoding/decoding library. [Expat][14].
* [fast-io](https://github.com/rpav/fast-io) [![GitHub stars](https://img.shields.io/github/stars/rpav/fast-io?style=flat)](https://github.com/rpav/fast-io/stargazers) - Fast octet-vector/stream I/O. [3-clause BSD][15].
* [named-readtables](https://github.com/melisgl/named-readtables) [![GitHub stars](https://img.shields.io/github/stars/melisgl/named-readtables?style=flat)](https://github.com/melisgl/named-readtables/stargazers) - Provides a readtable namespace, akin to package namespaces. [3-clause BSD][15].
* [simple-currency](https://github.com/a0-prw/simple-currency) [![GitHub stars](https://img.shields.io/github/stars/a0-prw/simple-currency?style=flat)](https://github.com/a0-prw/simple-currency/stargazers) - A currency conversion library using daily information published by the ECB. [FreeBSD][39].
* [trivial-garbage](https://github.com/trivial-garbage/trivial-garbage) [![GitHub stars](https://img.shields.io/github/stars/trivial-garbage/trivial-garbage?style=flat)](https://github.com/trivial-garbage/trivial-garbage/stargazers) - A portable finalizer, weak hash-table and weak pointer API. Public domain.
* [trivial-utf8](https://common-lisp.net/project/trivial-utf-8/) - A small library for doing UTF-8-based I/O. BSD.

Contributing
============
Your contributions are always welcome! Please submit a pull request or create
an issue to add a new framework, library or software to the list.

The rules we (try to) respect are the followings:

- by default, add a library to the end of its section.
- absolute de-facto libraries, like BordeauxThreads or Quicklisp,
  should be denoted with a ⭐ (Unicode code U+2B50).
- two libraries very similar in scope should be side by side, or in a
  section of their own.
- do some curation based on your experience and the state of the
  library's documentation. We do *not* aim at listing every existing
  CL library (see Cliki for that) nor to list every
  "popular" library (see Quicklisp stats).
- as such, the libraries we like best are marked with a 👍 (`1F44D`
  unicode character). See also the signs' explanation in the
  introduction.


[2]: http://www.gnu.org/copyleft/gpl.html
[3]: http://www.gnu.org/software/classpath/license.html
[4]: https://common-lisp.net/project/armedbear/faq.shtml#qa
[5]: http://unlicense.org/
[6]: http://www.gnu.org/software/clisp/impnotes.html
[8]: http://opensource.franz.com/preamble.html
[9]: https://www.gnu.org/licenses/lgpl-3.0.en.html
[11]: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
[13]: http://www.sbcl.org/manual/index.html#ANSI-Conformance
[14]: https://directory.fsf.org/wiki/License:Expat
[15]: https://directory.fsf.org/wiki/License:BSD_3Clause
[16]: https://www.quicklisp.org/beta/
[17]: https://directory.fsf.org/wiki/License:BSD_2Clause
[20]: http://www.cs.northwestern.edu/academics/courses/325/readings/graham/graham-notes.html
[21]: http://www.goodreads.com/book/show/1175730.Object_Oriented_Programming_in_Common_LISP
[22]: https://en.wikipedia.org/wiki/ISC_license
[33]: https://directory.fsf.org/wiki/License:Zlib
[39]: https://directory.fsf.org/wiki?title=License:FreeBSD
[47]: https://directory.fsf.org/wiki/License:CPLv1.0
[51]: https://directory.fsf.org/wiki/License:ArtisticLicense2.0
[54]: https://directory.fsf.org/wiki/License:Boost1.0
[59]: https://directory.fsf.org/wiki/License:EPLv1.0
[71]: https://codeberg.org/shinmera/plump
[72]: https://codeberg.org/shinmera/lquery
[89]: https://directory.fsf.org/wiki/License:Apache2.0
[156]: http://letoverlambda.com/
[157]: http://norvig.com/paip.html
[176]: https://github.com/gwkkwg/lift/blob/master/COPYING
[188]: https://github.com/triclops200/quickapp
[200]: https://opensource.org/licenses/MIT
[201]: https://github.com/google/lisp-koans
[205]: https://www.postgresql.org/about/licence/
[206]: http://www.gigamonkeys.com/book/
[207]: https://opensource.org/licenses/bsd-license.php
[208]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
[209]: http://www.eclipse.org/legal/epl-v10.html
[210]: https://common-lisp.net/project/linedit/license.html
[agpl3]: https://directory.fsf.org/wiki/License:AGPL-3.0
[211]: http://mozilla.org/MPL/2.0/
