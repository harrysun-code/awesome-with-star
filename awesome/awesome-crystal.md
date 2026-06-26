# Crystal

[![GitHub stars](https://img.shields.io/github/stars/veelenga/awesome-crystal?style=flat)](https://github.com/veelenga/awesome-crystal/stargazers)

[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

<p align="center"><img src="logo/logotype_horizontal.jpg" alt="awesome-crystal"></p>

# Awesome Crystal
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome Crystal code and resources. Inspired by [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) and [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers).
The goal is to have projects mostly stable and useful for the community.

Search shards at [shards.info](https://shards.info) for more.

Contributions are welcome. Please take a quick look at the [contribution guidelines](https://github.com/veelenga/awesome-crystal/blob/master/.github/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/veelenga/awesome-crystal/blob/master/.github/CONTRIBUTING.md?style=flat)](https://github.com/veelenga/awesome-crystal/blob/master/.github/CONTRIBUTING.md/stargazers) first.

* [Awesome Crystal](#awesome-crystal)
  * [Algorithms and Data structures](#algorithms-and-data-structures)
  * [Blockchain](#blockchain)
  * [C Bindings](#c-bindings)
  * [Caching](#caching)
  * [CLI Builders](#cli-builders)
  * [CLI Utils](#cli-utils)
  * [Code Analysis and Metrics](#code-analysis-and-metrics)
  * [Compression](#compression)
  * [Configuration](#configuration)
  * [Converters](#converters)
  * [Cryptography](#cryptography)
  * [Data Formats](#data-formats)
  * [Data Generators](#data-generators)
  * [Database Drivers/Clients](#database-driversclients)
  * [Database Tools](#database-tools)
  * [Debugging](#debugging)
  * [Dependency Injection](#dependency-injection)
  * [Email](#email)
  * [Environment Management](#environment-management)
  * [Examples and funny stuff](#examples-and-funny-stuff)
  * [Framework Components](#framework-components)
  * [Game Development](#game-development)
  * [GUI Development](#gui-development)
  * [HTML Builders](#html-builders)
  * [HTML/XML parsing](#htmlxml-parsing)
  * [HTTP](#http)
  * [Image Processing](#image-processing)
  * [Implementations/Compilers](#implementationscompilers)
  * [Internationalization](#internationalization)
  * [Logging and monitoring](#logging-and-monitoring)
  * [Machine Learning](#machine-learning)
  * [Markdown/Text Processors](#markdowntext-processors)
  * [Misc](#misc)
  * [Network Protocols](#network-protocols)
  * [Networking](#networking)
  * [ORM/ODM Extensions](#ormodm-extensions)
  * [Package Management](#package-management)
  * [Processes and Threads](#processes-and-threads)
  * [Project Generators](#project-generators)
  * [Queues and Messaging](#queues-and-messaging)
  * [Routing](#routing)
  * [Scheduling](#scheduling)
  * [Science and Data analysis](#science-and-data-analysis)
  * [Search](#search)
  * [Security](#security)
  * [Serverless Computing](#serverless-computing)
  * [System](#system)
  * [Task management](#task-management)
  * [Template Engine](#template-engine)
  * [Testing](#testing)
  * [Third-party APIs](#third-party-apis)
  * [Validation](#validation)
  * [Web Frameworks](#web-frameworks)
* [Community](#community)
  * [Unofficial](#unofficial)
* [Resources](#resources)
  * [Official Documentation Translations](#official-documentation-translations)
* [Services and Apps](#services-and-apps)
* [Tools](#tools)
  * [DevOps](#devops)
  * [Editor Plugins](#editor-plugins)
  * [LSP Language Server Protocol Implementations](#lsp-language-server-protocol-implementations)
  * [Shell Plugins](#shell-plugins)

## Algorithms and Data structures
 * [bisect](https://github.com/spider-gazelle/bisect) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/bisect?style=flat)](https://github.com/spider-gazelle/bisect/stargazers) - Inserting values into a sorted array
 * [blurhash.cr](https://github.com/Sija/blurhash.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/blurhash.cr?style=flat)](https://github.com/Sija/blurhash.cr/stargazers) - [BlurHash](https://github.com/woltapp/blurhash) [![GitHub stars](https://img.shields.io/github/stars/woltapp/blurhash?style=flat)](https://github.com/woltapp/blurhash/stargazers) implementation
 * [crie](https://github.com/c910335/crie) [![GitHub stars](https://img.shields.io/github/stars/c910335/crie?style=flat)](https://github.com/c910335/crie/stargazers) - Compile-time Trie
 * [CrOTP](https://github.com/philnash/crotp) [![GitHub stars](https://img.shields.io/github/stars/philnash/crotp?style=flat)](https://github.com/philnash/crotp/stargazers) - HOTP and TOTP implementation for two factor authentication
 * [crystal-linked-list](https://github.com/abvdasker/crystal-linked-list) [![GitHub stars](https://img.shields.io/github/stars/abvdasker/crystal-linked-list?style=flat)](https://github.com/abvdasker/crystal-linked-list/stargazers) - Implementation of Linked List
 * [crystaledge](https://github.com/unn4m3d/crystaledge) [![GitHub stars](https://img.shields.io/github/stars/unn4m3d/crystaledge?style=flat)](https://github.com/unn4m3d/crystaledge/stargazers) - A pure Vector Math library
 * [crystalg](https://github.com/tobyapi/crystalg) [![GitHub stars](https://img.shields.io/github/stars/tobyapi/crystalg?style=flat)](https://github.com/tobyapi/crystalg/stargazers) - A Generic Algorithm Library
 * [crystalline](https://github.com/jtomschroeder/crystalline) [![GitHub stars](https://img.shields.io/github/stars/jtomschroeder/crystalline?style=flat)](https://github.com/jtomschroeder/crystalline/stargazers) - A collection of containers and algorithms
 * [csuuid](https://github.com/wyhaines/csuuid.cr) [![GitHub stars](https://img.shields.io/github/stars/wyhaines/csuuid.cr?style=flat)](https://github.com/wyhaines/csuuid.cr/stargazers) - A Chronologically Sortable UUID
 * [edits.cr](https://github.com/tcrouch/edits.cr) [![GitHub stars](https://img.shields.io/github/stars/tcrouch/edits.cr?style=flat)](https://github.com/tcrouch/edits.cr/stargazers) - Collection of edit distance algorithms
 * [fzy](https://github.com/hugopl/fzy) [![GitHub stars](https://img.shields.io/github/stars/hugopl/fzy?style=flat)](https://github.com/hugopl/fzy/stargazers) - A Crystal port of awesome Fzy project fuzzy finder algorithm
 * [Goban](https://github.com/soya-daizu/goban) [![GitHub stars](https://img.shields.io/github/stars/soya-daizu/goban?style=flat)](https://github.com/soya-daizu/goban/stargazers) - A fast and efficient QR Code implementation
 * [graphlb](https://github.com/mettuaditya/graphlb) [![GitHub stars](https://img.shields.io/github/stars/mettuaditya/graphlb?style=flat)](https://github.com/mettuaditya/graphlb/stargazers) - Collection of graph datastructure and algorithms
 * [haversine](https://github.com/geocrystal/haversine) [![GitHub stars](https://img.shields.io/github/stars/geocrystal/haversine?style=flat)](https://github.com/geocrystal/haversine/stargazers) - An Implementation of the Haversine formula
 * [HKDF](https://github.com/spider-gazelle/HKDF) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/HKDF?style=flat)](https://github.com/spider-gazelle/HKDF/stargazers) - HMAC-based Extract-and-Expand Key Derivation Function [rfc5869](https://www.rfc-editor.org/rfc/rfc5869)
 * [kd_tree](https://github.com/geocrystal/kd_tree) [![GitHub stars](https://img.shields.io/github/stars/geocrystal/kd_tree?style=flat)](https://github.com/geocrystal/kd_tree/stargazers) - An implementation of "K-Dimensional Tree" and "N-Nearest Neighbors"
 * [ksuid.cr](https://github.com/Sija/ksuid.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/ksuid.cr?style=flat)](https://github.com/Sija/ksuid.cr/stargazers) - K-Sortable Globally Unique IDs
 * [markov](https://github.com/mccallofthewild/markov) [![GitHub stars](https://img.shields.io/github/stars/mccallofthewild/markov?style=flat)](https://github.com/mccallofthewild/markov/stargazers) - Build Markov Chains and run Markov Processes
 * [multiset.cr](https://github.com/tcrouch/multiset.cr) [![GitHub stars](https://img.shields.io/github/stars/tcrouch/multiset.cr?style=flat)](https://github.com/tcrouch/multiset.cr/stargazers) - Implementation of a multiset
 * [named_information](https://github.com/spider-gazelle/named_information) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/named_information?style=flat)](https://github.com/spider-gazelle/named_information/stargazers) - Naming Things with Hashes [rfc6920](https://datatracker.ietf.org/doc/html/rfc6920)
 * [qr-code](https://github.com/spider-gazelle/qr-code) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/qr-code?style=flat)](https://github.com/spider-gazelle/qr-code/stargazers) - QR Code generator
 * [radix](https://github.com/luislavena/radix) [![GitHub stars](https://img.shields.io/github/stars/luislavena/radix?style=flat)](https://github.com/luislavena/radix/stargazers) - Radix Tree implementation
 * [s2_cells](https://github.com/spider-gazelle/s2_cells) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/s2_cells?style=flat)](https://github.com/spider-gazelle/s2_cells/stargazers) - [S2 Geometry](https://s2geometry.io/devguide/s2cell_hierarchy.html) for spatial indexing
 * [secure-remote-password](https://github.com/spider-gazelle/secure-remote-password) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/secure-remote-password?style=flat)](https://github.com/spider-gazelle/secure-remote-password/stargazers) - SRP-6a protocol for authentication over an insecure network
 * [SPAKE2+](https://github.com/spider-gazelle/SPAKE2_plus) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/SPAKE2_plus?style=flat)](https://github.com/spider-gazelle/SPAKE2_plus/stargazers) - Password Authenticated Key Exchange (PAKE) protocol, comparable to SRP-6a
 * [splay_tree_map](https://github.com/wyhaines/splay_tree_map.cr) [![GitHub stars](https://img.shields.io/github/stars/wyhaines/splay_tree_map.cr?style=flat)](https://github.com/wyhaines/splay_tree_map.cr/stargazers) - Splay Tree implementation that conforms to the Hash ducktype
 * [verhoeff](https://github.com/spider-gazelle/verhoeff) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/verhoeff?style=flat)](https://github.com/spider-gazelle/verhoeff/stargazers) - Implementation of the Verhoeff checksum algorithm

## Blockchain
 * [Axentro](https://github.com/Axentro/Axentro) [![GitHub stars](https://img.shields.io/github/stars/Axentro/Axentro?style=flat)](https://github.com/Axentro/Axentro/stargazers) - A custom blockchain platform
 * [Cocol](https://github.com/cocol-project/cocol) [![GitHub stars](https://img.shields.io/github/stars/cocol-project/cocol?style=flat)](https://github.com/cocol-project/cocol/stargazers) - A minimal blockchain testbed
 * [secp256k1.cr](https://github.com/q9f/secp256k1.cr) [![GitHub stars](https://img.shields.io/github/stars/q9f/secp256k1.cr?style=flat)](https://github.com/q9f/secp256k1.cr/stargazers) - Elliptic curve used in the public-private-key cryptography

## C bindings
 * [augeas.cr](https://github.com/fernandes/augeas.cr) [![GitHub stars](https://img.shields.io/github/stars/fernandes/augeas.cr?style=flat)](https://github.com/fernandes/augeas.cr/stargazers) - Bindings for [Augeas](https://augeas.net/)
 * [clang.cr](https://github.com/crystal-lang/clang.cr) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/clang.cr?style=flat)](https://github.com/crystal-lang/clang.cr/stargazers) - Libclang bindings
 * [crt.cr](https://github.com/maiha/crt.cr) [![GitHub stars](https://img.shields.io/github/stars/maiha/crt.cr?style=flat)](https://github.com/maiha/crt.cr/stargazers) - Bindings for libncursesw and crt
 * [crystal-gsl](https://github.com/konovod/crystal-gsl) [![GitHub stars](https://img.shields.io/github/stars/konovod/crystal-gsl?style=flat)](https://github.com/konovod/crystal-gsl/stargazers) - Bindings for [GNU Scientific Library](https://www.gnu.org/software/gsl/)
 * [crystal-hunspell](https://github.com/mamantoha/crystal-hunspell) [![GitHub stars](https://img.shields.io/github/stars/mamantoha/crystal-hunspell?style=flat)](https://github.com/mamantoha/crystal-hunspell/stargazers) - Bindings for [Hunspell](https://hunspell.github.io/)
 * [duktape.cr](https://github.com/jessedoyle/duktape.cr) [![GitHub stars](https://img.shields.io/github/stars/jessedoyle/duktape.cr?style=flat)](https://github.com/jessedoyle/duktape.cr/stargazers) - Bindings for the [Duktape](https://github.com/svaarala/duktape) [![GitHub stars](https://img.shields.io/github/stars/svaarala/duktape?style=flat)](https://github.com/svaarala/duktape/stargazers) javascript engine
 * [fftw.cr](https://github.com/firejox/fftw.cr) [![GitHub stars](https://img.shields.io/github/stars/firejox/fftw.cr?style=flat)](https://github.com/firejox/fftw.cr/stargazers) - Bindings for [FFTW](https://fftw.org/) library
 * [gphoto2.cr](https://github.com/Sija/gphoto2.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/gphoto2.cr?style=flat)](https://github.com/Sija/gphoto2.cr/stargazers) - Bindings for the [libgphoto2](http://www.gphoto.org/) library
 * [gpio.cr](https://github.com/spider-gazelle/gpio.cr) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/gpio.cr?style=flat)](https://github.com/spider-gazelle/gpio.cr/stargazers) - Bindings for the gpiod library (general purpose IO control and feedback)
 * [icu.cr](https://github.com/olbat/icu.cr) [![GitHub stars](https://img.shields.io/github/stars/olbat/icu.cr?style=flat)](https://github.com/olbat/icu.cr/stargazers) - Bindings for the [ICU](http://site.icu-project.org/) library
 * [libnotify.cr](https://github.com/splattael/libnotify.cr) [![GitHub stars](https://img.shields.io/github/stars/splattael/libnotify.cr?style=flat)](https://github.com/splattael/libnotify.cr/stargazers) - Bindings for Libnotify
 * [nlopt.cr](https://github.com/konovod/nlopt.cr) [![GitHub stars](https://img.shields.io/github/stars/konovod/nlopt.cr?style=flat)](https://github.com/konovod/nlopt.cr/stargazers) - Bindings for [NLOpt](https://nlopt.readthedocs.io/en/latest/)
 * [pcap.cr](https://github.com/maiha/pcap.cr) [![GitHub stars](https://img.shields.io/github/stars/maiha/pcap.cr?style=flat)](https://github.com/maiha/pcap.cr/stargazers) - Bindings for libpcap
 * [pledge.cr](https://github.com/chris-huxtable/pledge.cr) [![GitHub stars](https://img.shields.io/github/stars/chris-huxtable/pledge.cr?style=flat)](https://github.com/chris-huxtable/pledge.cr/stargazers) - Bindings for OpenBSD's `pledge(2)`
 * [ssh2.cr](https://github.com/spider-gazelle/ssh2.cr) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/ssh2.cr?style=flat)](https://github.com/spider-gazelle/ssh2.cr/stargazers) - Bindings for libssh2 library
 * [syslog.cr](https://github.com/chris-huxtable/syslog.cr) [![GitHub stars](https://img.shields.io/github/stars/chris-huxtable/syslog.cr?style=flat)](https://github.com/chris-huxtable/syslog.cr/stargazers) - Bindings for `syslog`
 * [v4l2.cr](https://github.com/spider-gazelle/v4l2.cr) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/v4l2.cr?style=flat)](https://github.com/spider-gazelle/v4l2.cr/stargazers) - Bindings for [Video4Linux2](https://en.wikipedia.org/wiki/Video4Linux)
 * [wasmer-crystal](https://github.com/naqvis/wasmer-crystal) [![GitHub stars](https://img.shields.io/github/stars/naqvis/wasmer-crystal?style=flat)](https://github.com/naqvis/wasmer-crystal/stargazers) - Bindings for the `wasmer` WebAssembly runtime
 * [win32cr](https://github.com/mjblack/win32cr) [![GitHub stars](https://img.shields.io/github/stars/mjblack/win32cr?style=flat)](https://github.com/mjblack/win32cr/stargazers) - Bindings for Win32 API
 * [x_do.cr](https://github.com/woodruffw/x_do.cr) [![GitHub stars](https://img.shields.io/github/stars/woodruffw/x_do.cr?style=flat)](https://github.com/woodruffw/x_do.cr/stargazers) - Bindings for libxdo ([`xdotool`](https://github.com/jordansissel/xdotool) [![GitHub stars](https://img.shields.io/github/stars/jordansissel/xdotool?style=flat)](https://github.com/jordansissel/xdotool/stargazers))

## Caching
 * [apt-larder](https://github.com/jbox-web/apt-larder) [![GitHub stars](https://img.shields.io/github/stars/jbox-web/apt-larder?style=flat)](https://github.com/jbox-web/apt-larder/stargazers) - An HTTP caching proxy for APT package repositories
 * [cache](https://github.com/crystal-cache/cache) [![GitHub stars](https://img.shields.io/github/stars/crystal-cache/cache?style=flat)](https://github.com/crystal-cache/cache/stargazers) - A key/value store where pairs can expire after a specified interval
 * [crystal-memcached](https://github.com/comandeo/crystal-memcached) [![GitHub stars](https://img.shields.io/github/stars/comandeo/crystal-memcached?style=flat)](https://github.com/comandeo/crystal-memcached/stargazers) - Implementation of a memcached client

## CLI Builders
 * [admiral](https://github.com/jwaldrip/admiral.cr) [![GitHub stars](https://img.shields.io/github/stars/jwaldrip/admiral.cr?style=flat)](https://github.com/jwaldrip/admiral.cr/stargazers) - A robust DSL for writing command line interfaces
 * [Athena Console](https://github.com/athena-framework/console) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/console?style=flat)](https://github.com/athena-framework/console/stargazers) - Allows for the creation of CLI based commands
 * [clicr](https://github.com/j8r/clicr) [![GitHub stars](https://img.shields.io/github/stars/j8r/clicr?style=flat)](https://github.com/j8r/clicr/stargazers) -  A simple declarative command line interface builder
 * [clim](https://github.com/at-grandpa/clim) [![GitHub stars](https://img.shields.io/github/stars/at-grandpa/clim?style=flat)](https://github.com/at-grandpa/clim/stargazers) - Slim command line interface builder
 * [Cling](https://github.com/devnote-dev/cling) [![GitHub stars](https://img.shields.io/github/stars/devnote-dev/cling?style=flat)](https://github.com/devnote-dev/cling/stargazers) - A modular, non-macro-based command line interface library
 * [commander](https://github.com/mrrooijen/commander) [![GitHub stars](https://img.shields.io/github/stars/mrrooijen/commander?style=flat)](https://github.com/mrrooijen/commander/stargazers) - Command-line interface builder
 * [Keimeno](https://github.com/robacarp/keimeno) [![GitHub stars](https://img.shields.io/github/stars/robacarp/keimeno?style=flat)](https://github.com/robacarp/keimeno/stargazers) -  A lightweight text user interface library in Crystal
 * [OptionParser](https://crystal-lang.org/api/OptionParser.html) - command-line options processing (Crystal stdlib)
 * [Phreak](https://github.com/shinzlet/phreak) [![GitHub stars](https://img.shields.io/github/stars/shinzlet/phreak?style=flat)](https://github.com/shinzlet/phreak/stargazers) - A highly flexible Crystal CLI builder in the style of OptionParser

## CLI Utils
 * [climate](https://github.com/Sija/climate.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/climate.cr?style=flat)](https://github.com/Sija/climate.cr/stargazers) - Tiny tool to make your CLI output 🌈  coloured
 * [coin](https://github.com/caian-org/coin) [![GitHub stars](https://img.shields.io/github/stars/caian-org/coin?style=flat)](https://github.com/caian-org/coin/stargazers) - Command-line application that performs currency conversion via the [Fixer API](https://fixer.io)
 * [cride](https://github.com/j8r/cride) [![GitHub stars](https://img.shields.io/github/stars/j8r/cride?style=flat)](https://github.com/j8r/cride/stargazers) - A light CLI text editor/IDE
 * [git-repository](https://github.com/place-labs/git-repository) [![GitHub stars](https://img.shields.io/github/stars/place-labs/git-repository?style=flat)](https://github.com/place-labs/git-repository/stargazers) - A git cli wrapper querying and cloning remote repositories with minimal data transfer
 * [hetzner-k3s](https://github.com/vitobotta/hetzner-k3s) [![GitHub stars](https://img.shields.io/github/stars/vitobotta/hetzner-k3s?style=flat)](https://github.com/vitobotta/hetzner-k3s/stargazers) - A CLI tool to quickly create and manage Kubernetes clusters in Hetzner Cloud
 * [lff](https://github.com/mkdika/lff-cr) [![GitHub stars](https://img.shields.io/github/stars/mkdika/lff-cr?style=flat)](https://github.com/mkdika/lff-cr/stargazers) - Simple and straightforward large files finder utility in command line
 * [meet](https://github.com/ryanprior/meet) [![GitHub stars](https://img.shields.io/github/stars/ryanprior/meet?style=flat)](https://github.com/ryanprior/meet/stargazers) - Start a jitsi meeting quickly from the comfort of your command line
 * [oq](https://github.com/Blacksmoke16/oq) [![GitHub stars](https://img.shields.io/github/stars/Blacksmoke16/oq?style=flat)](https://github.com/Blacksmoke16/oq/stargazers) - A performant, and portable jq wrapper to facilitate the consumption and output of formats other than JSON; using [jq](https://github.com/stedolan/jq) [![GitHub stars](https://img.shields.io/github/stars/stedolan/jq?style=flat)](https://github.com/stedolan/jq/stargazers) filters to transform the data
 * [progress_bar.cr](https://github.com/TPei/progress_bar.cr) [![GitHub stars](https://img.shields.io/github/stars/TPei/progress_bar.cr?style=flat)](https://github.com/TPei/progress_bar.cr/stargazers) - A simple and customizable progress bar
 * [tablo](https://github.com/hutou/tablo) [![GitHub stars](https://img.shields.io/github/stars/hutou/tablo?style=flat)](https://github.com/hutou/tablo/stargazers) - A flexible terminal table generator
 * [tallboy](https://github.com/epoch/tallboy) [![GitHub stars](https://img.shields.io/github/stars/epoch/tallboy?style=flat)](https://github.com/epoch/tallboy/stargazers) - Generate ASCII character tables with support for spanning cells over multiple columns

## Code Analysis and Metrics
 * [ameba](https://github.com/crystal-ameba/ameba) [![GitHub stars](https://img.shields.io/github/stars/crystal-ameba/ameba?style=flat)](https://github.com/crystal-ameba/ameba/stargazers) - A static code analysis tool
 * [cruml](https://github.com/tamdaz/cruml) [![GitHub stars](https://img.shields.io/github/stars/tamdaz/cruml?style=flat)](https://github.com/tamdaz/cruml/stargazers) - A tool that provides an UML class diagram generator for any Crystal projects
 * [linguist.cr](https://github.com/microgit-com/linguist.cr) [![GitHub stars](https://img.shields.io/github/stars/microgit-com/linguist.cr?style=flat)](https://github.com/microgit-com/linguist.cr/stargazers) - Using multiple ways to find programming language used in files, based on Github's Linguist

## Compression
 * [Crystar](https://github.com/naqvis/crystar) [![GitHub stars](https://img.shields.io/github/stars/naqvis/crystar?style=flat)](https://github.com/naqvis/crystar/stargazers) - Readers and writers of Tar archive format
 * [Gzip](https://crystal-lang.org/api/Compress/Gzip.html) - readers and writers of gzip format (Crystal stdlib)
 * [polylines.cr](https://github.com/BuonOmo/polylines.cr) [![GitHub stars](https://img.shields.io/github/stars/BuonOmo/polylines.cr?style=flat)](https://github.com/BuonOmo/polylines.cr/stargazers) — compression of series of coordinates
 * [snappy](https://github.com/naqvis/snappy) [![GitHub stars](https://img.shields.io/github/stars/naqvis/snappy?style=flat)](https://github.com/naqvis/snappy/stargazers) -  Snappy compression format reader/writer for Crystal
 * [Zip](https://crystal-lang.org/api/Compress/Zip.html) - readers and writers of zip format (Crystal stdlib)
 * [Zlib](https://crystal-lang.org/api/Compress/Zlib.html) - readers and writers of zlib format (Crystal stdlib)
 * [zstd.cr](https://github.com/didactic-drunk/zstd.cr) [![GitHub stars](https://img.shields.io/github/stars/didactic-drunk/zstd.cr?style=flat)](https://github.com/didactic-drunk/zstd.cr/stargazers) - Bindings for [Zstandard](https://github.com/facebook/zstd) [![GitHub stars](https://img.shields.io/github/stars/facebook/zstd?style=flat)](https://github.com/facebook/zstd/stargazers) compression library

## Configuration
 * [cr-dotenv](https://github.com/gdotdesign/cr-dotenv) [![GitHub stars](https://img.shields.io/github/stars/gdotdesign/cr-dotenv?style=flat)](https://github.com/gdotdesign/cr-dotenv/stargazers) - Loads .env file
 * [Envy](https://github.com/grottopress/envy) [![GitHub stars](https://img.shields.io/github/stars/grottopress/envy?style=flat)](https://github.com/grottopress/envy/stargazers) - Load environment variables from YAML
 * [envyable](https://github.com/philnash/envyable.cr) [![GitHub stars](https://img.shields.io/github/stars/philnash/envyable.cr?style=flat)](https://github.com/philnash/envyable.cr/stargazers) -  A simple YAML to ENV config loader
 * [habitat](https://github.com/luckyframework/habitat) [![GitHub stars](https://img.shields.io/github/stars/luckyframework/habitat?style=flat)](https://github.com/luckyframework/habitat/stargazers) - Type safe configuration for your classes and modules
 * [totem](https://github.com/icyleaf/totem) [![GitHub stars](https://img.shields.io/github/stars/icyleaf/totem?style=flat)](https://github.com/icyleaf/totem/stargazers) - Load and parse a configuration in JSON, YAML, dotenv formats

## Converters
 * [base62.cr](https://github.com/Sija/base62.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/base62.cr?style=flat)](https://github.com/Sija/base62.cr/stargazers) - Base62 encoder/decoder, well suited for url-shortening
 * [crunits](https://github.com/spider-gazelle/crunits) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/crunits?style=flat)](https://github.com/spider-gazelle/crunits/stargazers) - Tool for converting units of measure (miles to kilometers, celsius to fahrenheit etc)
 * [money](https://github.com/crystal-money/money) [![GitHub stars](https://img.shields.io/github/stars/crystal-money/money?style=flat)](https://github.com/crystal-money/money/stargazers) - Handling money and currency conversion with ease (almost complete port of [RubyMoney](https://github.com/RubyMoney/money) [![GitHub stars](https://img.shields.io/github/stars/RubyMoney/money?style=flat)](https://github.com/RubyMoney/money/stargazers))
 * [sass.cr](https://github.com/straight-shoota/sass.cr) [![GitHub stars](https://img.shields.io/github/stars/straight-shoota/sass.cr?style=flat)](https://github.com/straight-shoota/sass.cr/stargazers) - Compile SASS/SCSS to CSS ([libsass](https://github.com/sass/libsass/) [![GitHub stars](https://img.shields.io/github/stars/sass/libsass/?style=flat)](https://github.com/sass/libsass//stargazers) binding)
 * [tssc.cr](https://github.com/Sija/tssc.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/tssc.cr?style=flat)](https://github.com/Sija/tssc.cr/stargazers) - `Time::Span` String Converter (incl. JSON & YAML support)

## Cryptography
 * [cmac](https://github.com/spider-gazelle/cmac) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/cmac?style=flat)](https://github.com/spider-gazelle/cmac/stargazers) - Crystal implementation of Cipher-based Message Authentication Code (CMAC)
 * [ed25519](https://github.com/spider-gazelle/ed25519) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/ed25519?style=flat)](https://github.com/spider-gazelle/ed25519/stargazers) - the Ed25519 elliptic curve public-key signature system
described in [RFC 8032]
 * [monocypher.cr](https://github.com/konovod/monocypher.cr) [![GitHub stars](https://img.shields.io/github/stars/konovod/monocypher.cr?style=flat)](https://github.com/konovod/monocypher.cr/stargazers) - Crystal wrapper for the Monocypher crypto library
 * [sodium.cr](https://github.com/didactic-drunk/sodium.cr) [![GitHub stars](https://img.shields.io/github/stars/didactic-drunk/sodium.cr?style=flat)](https://github.com/didactic-drunk/sodium.cr/stargazers) - Crystal wrapper for the libsodium crypto API

## Data Formats
 * [BinData](https://github.com/spider-gazelle/bindata) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/bindata?style=flat)](https://github.com/spider-gazelle/bindata/stargazers) - Binary data parser helper with an [ASN.1](https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One) parser
 * [config.cr](https://github.com/chris-huxtable/config.cr) [![GitHub stars](https://img.shields.io/github/stars/chris-huxtable/config.cr?style=flat)](https://github.com/chris-huxtable/config.cr/stargazers) - Easy to use configuration format parser
 * [crinder](https://github.com/c910335/crinder) [![GitHub stars](https://img.shields.io/github/stars/c910335/crinder?style=flat)](https://github.com/c910335/crinder/stargazers) - Class based json renderer
 * [Crystalizer](https://github.com/j8r/crystalizer) [![GitHub stars](https://img.shields.io/github/stars/j8r/crystalizer?style=flat)](https://github.com/j8r/crystalizer/stargazers) - (De)serialize any Crystal object; supporting JSON, YAML, and Byte formats out of the box
 * [CSV](https://crystal-lang.org/api/CSV.html) - parsing and generating for comma-separated values (Crystal stdlib)
 * [front_matter.cr](https://github.com/chris-huxtable/front_matter.cr) [![GitHub stars](https://img.shields.io/github/stars/chris-huxtable/front_matter.cr?style=flat)](https://github.com/chris-huxtable/front_matter.cr/stargazers) - Separates a files front matter from its content
 * [geoip2.cr](https://github.com/delef/geoip2.cr) [![GitHub stars](https://img.shields.io/github/stars/delef/geoip2.cr?style=flat)](https://github.com/delef/geoip2.cr/stargazers) - GeoIP2 reader
 * [HAR](https://github.com/NeuraLegion/har) [![GitHub stars](https://img.shields.io/github/stars/NeuraLegion/har?style=flat)](https://github.com/NeuraLegion/har/stargazers) - HAR (HTTP Archive) parser
 * [INI](https://crystal-lang.org/api/INI.html) - INI file parser (Crystal stdlib)
 * [jmespath.cr](https://github.com/qequ/jmespath.cr) [![GitHub stars](https://img.shields.io/github/stars/qequ/jmespath.cr?style=flat)](https://github.com/qequ/jmespath.cr/stargazers) - Crystal implementation of JMESPath, a query language for JSON
 * [JSON](https://crystal-lang.org/api/JSON.html) - parsing and generating JSON documents (Crystal stdlib)
 * [json-schema](https://github.com/spider-gazelle/json-schema) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/json-schema?style=flat)](https://github.com/spider-gazelle/json-schema/stargazers) - convert JSON serializable classes into a [JSON Schema](https://json-schema.org/) representation
 * [JSON::OnSteroids](https://github.com/anykeyh/json_on_steroids) [![GitHub stars](https://img.shields.io/github/stars/anykeyh/json_on_steroids?style=flat)](https://github.com/anykeyh/json_on_steroids/stargazers) - handle and mutate JSON document easily
 * [maxminddb.cr](https://github.com/delef/maxminddb.cr) [![GitHub stars](https://img.shields.io/github/stars/delef/maxminddb.cr?style=flat)](https://github.com/delef/maxminddb.cr/stargazers) - MaxMindDB reader
 * [toml.cr](https://github.com/crystal-community/toml.cr) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/toml.cr?style=flat)](https://github.com/crystal-community/toml.cr/stargazers) - TOML parser
 * [toon-crystal](https://github.com/mamantoha/toon-crystal) [![GitHub stars](https://img.shields.io/github/stars/mamantoha/toon-crystal?style=flat)](https://github.com/mamantoha/toon-crystal/stargazers) - TOON (Token-Oriented Object Notation) parser
 * [XML](https://crystal-lang.org/api/XML.html) - parsing and generating XML documents (Crystal stdlib)
 * [YAML](https://crystal-lang.org/api/YAML.html) - parsing and generating YAML documents (Crystal stdlib)

## Data Generators
 * [faker](https://github.com/askn/faker) [![GitHub stars](https://img.shields.io/github/stars/askn/faker?style=flat)](https://github.com/askn/faker/stargazers) - A library for generating fake data
 * [hashids.cr](https://github.com/splattael/hashids.cr) [![GitHub stars](https://img.shields.io/github/stars/splattael/hashids.cr?style=flat)](https://github.com/splattael/hashids.cr/stargazers) - A library to generate YouTube-like ids from one or many numbers
 * [prime](https://github.com/wontruefree/prime) [![GitHub stars](https://img.shields.io/github/stars/wontruefree/prime?style=flat)](https://github.com/wontruefree/prime/stargazers) - A prime number generator

## Database Drivers/Clients
 * [couchdb.cr](https://github.com/TechMagister/couchdb.cr) [![GitHub stars](https://img.shields.io/github/stars/TechMagister/couchdb.cr?style=flat)](https://github.com/TechMagister/couchdb.cr/stargazers) - CouchDB client
 * [cryomongo](https://github.com/elbywan/cryomongo) [![GitHub stars](https://img.shields.io/github/stars/elbywan/cryomongo?style=flat)](https://github.com/elbywan/cryomongo/stargazers) - MongoDB driver
 * [crystal-db](https://github.com/crystal-lang/crystal-db) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/crystal-db?style=flat)](https://github.com/crystal-lang/crystal-db/stargazers) - Common db api
 * [crystal-ldap](https://github.com/spider-gazelle/crystal-ldap) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/crystal-ldap?style=flat)](https://github.com/spider-gazelle/crystal-ldap/stargazers) - LDAP client
 * [crystal-mysql](https://github.com/crystal-lang/crystal-mysql) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/crystal-mysql?style=flat)](https://github.com/crystal-lang/crystal-mysql/stargazers) - MySQL connector for Crystal
 * [crystal-pg](https://github.com/will/crystal-pg) [![GitHub stars](https://img.shields.io/github/stars/will/crystal-pg?style=flat)](https://github.com/will/crystal-pg/stargazers) - A Postgres driver
 * [crystal-redis](https://github.com/stefanwille/crystal-redis) [![GitHub stars](https://img.shields.io/github/stars/stefanwille/crystal-redis?style=flat)](https://github.com/stefanwille/crystal-redis/stargazers) - Full featured Redis client
 * [crystal-rethinkdb](https://github.com/kingsleyh/crystal-rethinkdb) [![GitHub stars](https://img.shields.io/github/stars/kingsleyh/crystal-rethinkdb?style=flat)](https://github.com/kingsleyh/crystal-rethinkdb/stargazers) - Driver for RethinkDB / RebirthDB
 * [crystal-sqlite3](https://github.com/crystal-lang/crystal-sqlite3) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/crystal-sqlite3?style=flat)](https://github.com/crystal-lang/crystal-sqlite3/stargazers) - SQLite3 bindings
 * [leveldb](https://github.com/crystal-community/leveldb) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/leveldb?style=flat)](https://github.com/crystal-community/leveldb/stargazers) - Crystal bindings for LevelDB
 * [rocksdb.cr](https://github.com/maiha/rocksdb.cr) [![GitHub stars](https://img.shields.io/github/stars/maiha/rocksdb.cr?style=flat)](https://github.com/maiha/rocksdb.cr/stargazers) - RocksDB client
 * [surrealdb.cr](https://github.com/yorci/surrealdb.cr) [![GitHub stars](https://img.shields.io/github/stars/yorci/surrealdb.cr?style=flat)](https://github.com/yorci/surrealdb.cr/stargazers) - Unoffical SurrealDB HTTP & Websocket Client

## Database Tools
 * [migrate](https://github.com/vladfaust/migrate.cr) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/migrate.cr?style=flat)](https://github.com/vladfaust/migrate.cr/stargazers) - A simpler database migration tool with transactions

## Debugging
* [backtracer.cr](https://github.com/Sija/backtracer.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/backtracer.cr?style=flat)](https://github.com/Sija/backtracer.cr/stargazers) - Shard aiming to assist with parsing backtraces into a structured form
* [debug.cr](https://github.com/Sija/debug.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/debug.cr?style=flat)](https://github.com/Sija/debug.cr/stargazers) - `debug!(…)` macro for `pp`-style debugging

## Dependency Injection
 * [Athena Dependency Injection](https://github.com/athena-framework/dependency-injection) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/dependency-injection?style=flat)](https://github.com/athena-framework/dependency-injection/stargazers) - Robust dependency injection service container framework
 * [Crystal-DI](https://github.com/funk-yourself/crystal-di) [![GitHub stars](https://img.shields.io/github/stars/funk-yourself/crystal-di?style=flat)](https://github.com/funk-yourself/crystal-di/stargazers) - Lightweight DI Container
 * [HardWire](https://github.com/jerometwell/hardwire) [![GitHub stars](https://img.shields.io/github/stars/jerometwell/hardwire?style=flat)](https://github.com/jerometwell/hardwire/stargazers) - A compile-time non-intrusive dependency injection system
 * [syringe](https://github.com/Bonemind/syringe) [![GitHub stars](https://img.shields.io/github/stars/Bonemind/syringe?style=flat)](https://github.com/Bonemind/syringe/stargazers) - A simple and basic dependency injection shard for crystal

## Email
 * [carbon](https://github.com/luckyframework/carbon) [![GitHub stars](https://img.shields.io/github/stars/luckyframework/carbon?style=flat)](https://github.com/luckyframework/carbon/stargazers) - Fun, testable, and adapter-based email library
 * [crystal-email](https://github.com/arcage/crystal-email) [![GitHub stars](https://img.shields.io/github/stars/arcage/crystal-email?style=flat)](https://github.com/arcage/crystal-email/stargazers) - Simple e-mail sending library
 * [CrystalEmail](https://git.sceptique.eu/Sceptique/CrystalEmail) - A RFC compliant Email validator
 * [sendgrid.cr](https://github.com/dlanileonardo/sendgrid.cr) [![GitHub stars](https://img.shields.io/github/stars/dlanileonardo/sendgrid.cr?style=flat)](https://github.com/dlanileonardo/sendgrid.cr/stargazers) - Simple Sendgrid Client

## Environment Management
 * [asdf-crystal](https://github.com/marciogm/asdf-crystal) [![GitHub stars](https://img.shields.io/github/stars/marciogm/asdf-crystal?style=flat)](https://github.com/marciogm/asdf-crystal/stargazers) - Plugin for asdf version manager
 * [crenv](https://github.com/crenv/crenv) [![GitHub stars](https://img.shields.io/github/stars/crenv/crenv?style=flat)](https://github.com/crenv/crenv/stargazers) - Crystal version manager
 * [rcm.cr](https://github.com/maiha/rcm.cr) [![GitHub stars](https://img.shields.io/github/stars/maiha/rcm.cr?style=flat)](https://github.com/maiha/rcm.cr/stargazers) - Redis Cluster Manager
 * [vfox-crystal](https://github.com/yanecc/vfox-crystal) [![GitHub stars](https://img.shields.io/github/stars/yanecc/vfox-crystal?style=flat)](https://github.com/yanecc/vfox-crystal/stargazers) - Plugin for vfox version manager

## Examples and funny stuff
 * [blackjack-cr](https://github.com/gdonald/blackjack-cr) [![GitHub stars](https://img.shields.io/github/stars/gdonald/blackjack-cr?style=flat)](https://github.com/gdonald/blackjack-cr/stargazers) - Console Blackjack
 * [crystal-patterns](https://github.com/crystal-community/crystal-patterns) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/crystal-patterns?style=flat)](https://github.com/crystal-community/crystal-patterns/stargazers) - Examples of GOF patters
 * [crystalworld](https://github.com/vladfaust/crystalworld) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/crystalworld?style=flat)](https://github.com/vladfaust/crystalworld/stargazers) - [realworld.io](https://realworld.io) back-end API implementation
 * [exercism-crystal](https://github.com/exercism/crystal) [![GitHub stars](https://img.shields.io/github/stars/exercism/crystal?style=flat)](https://github.com/exercism/crystal/stargazers) - Exercism exercises
 * [try.cr](https://github.com/maiha/try.cr) [![GitHub stars](https://img.shields.io/github/stars/maiha/try.cr?style=flat)](https://github.com/maiha/try.cr/stargazers) - Try monad

## Framework Components
 * [Athena Event Dispatcher](https://github.com/athena-framework/event-dispatcher) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/event-dispatcher?style=flat)](https://github.com/athena-framework/event-dispatcher/stargazers) - A Mediator and Observer pattern event library
 * [Athena Negotiation](https://github.com/athena-framework/negotiation) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/negotiation?style=flat)](https://github.com/athena-framework/negotiation/stargazers) - Framework agnostic content negotiation library
 * [device_detector](https://github.com/creadone/device_detector) [![GitHub stars](https://img.shields.io/github/stars/creadone/device_detector?style=flat)](https://github.com/creadone/device_detector/stargazers) - Shard for detect device by user agent string
 * [Exception Page](https://github.com/crystal-loot/exception_page) [![GitHub stars](https://img.shields.io/github/stars/crystal-loot/exception_page?style=flat)](https://github.com/crystal-loot/exception_page/stargazers) - An exceptional exception page for Crystal web libraries and frameworks
 * [graphql](https://github.com/graphql-crystal/graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-crystal/graphql?style=flat)](https://github.com/graphql-crystal/graphql/stargazers) - Type-safe [GraphQL](http://graphql.org) server implementation
 * [graphql-crystal](https://github.com/ziprandom/graphql-crystal) [![GitHub stars](https://img.shields.io/github/stars/ziprandom/graphql-crystal?style=flat)](https://github.com/ziprandom/graphql-crystal/stargazers) - [GraphQL](http://graphql.org) implementation
 * [kemal-session](https://github.com/kemalcr/kemal-session) [![GitHub stars](https://img.shields.io/github/stars/kemalcr/kemal-session?style=flat)](https://github.com/kemalcr/kemal-session/stargazers) - Session handler for Kemal
 * [mochi](https://github.com/awcrotwell/mochi) [![GitHub stars](https://img.shields.io/github/stars/awcrotwell/mochi?style=flat)](https://github.com/awcrotwell/mochi/stargazers) - Authentication shard inspired by Devise supporting: Authenticable, Confirmable, Invitable & more
 * [motion.cr](https://github.com/awcrotwell/motion.cr) [![GitHub stars](https://img.shields.io/github/stars/awcrotwell/motion.cr?style=flat)](https://github.com/awcrotwell/motion.cr/stargazers) - Object oriented frontend library for Amber
 * [multi-auth](https://github.com/msa7/multi_auth) [![GitHub stars](https://img.shields.io/github/stars/msa7/multi_auth?style=flat)](https://github.com/msa7/multi_auth/stargazers) - Standardized multi-provider OAuth2 authentication (inspired by omniauth)
 * [praetorian](https://github.com/ilanusse/praetorian) [![GitHub stars](https://img.shields.io/github/stars/ilanusse/praetorian?style=flat)](https://github.com/ilanusse/praetorian/stargazers) - Minimalist authorization library inspired by Pundit
 * [Shield](https://github.com/grottopress/shield) [![GitHub stars](https://img.shields.io/github/stars/grottopress/shield?style=flat)](https://github.com/grottopress/shield/stargazers) - Comprehensive security for *Lucky* framework
 * [shrine.cr](https://github.com/jetrockets/shrine.cr) [![GitHub stars](https://img.shields.io/github/stars/jetrockets/shrine.cr?style=flat)](https://github.com/jetrockets/shrine.cr/stargazers) - File Attachment toolkit for Crystal applications. Heavily inspired by Shrine for Ruby
 * [tourmaline](https://github.com/protoncr/tourmaline) [![GitHub stars](https://img.shields.io/github/stars/protoncr/tourmaline?style=flat)](https://github.com/protoncr/tourmaline/stargazers) - Telegram bot framework with an API loosely based on [telegraf.js](https://telegraf.js.org/)

## Game Development
 * [CrSFML](https://github.com/oprypin/crsfml) [![GitHub stars](https://img.shields.io/github/stars/oprypin/crsfml?style=flat)](https://github.com/oprypin/crsfml/stargazers) - Bindings to [SFML](https://www.sfml-dev.org/) multimedia/game library
 * [crystal-chipmunk](https://github.com/oprypin/crystal-chipmunk) [![GitHub stars](https://img.shields.io/github/stars/oprypin/crystal-chipmunk?style=flat)](https://github.com/oprypin/crystal-chipmunk/stargazers) - Bindings to [Chipmunk](http://chipmunk-physics.net/), a fast and lightweight 2D game physics library
 * [crystal-imgui-sfml](https://github.com/oprypin/crystal-imgui-sfml) [![GitHub stars](https://img.shields.io/github/stars/oprypin/crystal-imgui-sfml?style=flat)](https://github.com/oprypin/crystal-imgui-sfml/stargazers) - Bindings to integrate [Dear ImGui](https://github.com/ocornut/imgui) [![GitHub stars](https://img.shields.io/github/stars/ocornut/imgui?style=flat)](https://github.com/ocornut/imgui/stargazers) into an [SFML](https://www.sfml-dev.org/) project
 * [entitas.cr](https://github.com/spoved/entitas.cr) [![GitHub stars](https://img.shields.io/github/stars/spoved/entitas.cr?style=flat)](https://github.com/spoved/entitas.cr/stargazers) - A Entity Component System Framework for Crystal
 * [MyECS](https://github.com/konovod/myecs) [![GitHub stars](https://img.shields.io/github/stars/konovod/myecs?style=flat)](https://github.com/konovod/myecs/stargazers) - A Sparse Entity Component System Framework for Crystal
 * [Raylib-cr](https://github.com/sol-vin/raylib-cr) [![GitHub stars](https://img.shields.io/github/stars/sol-vin/raylib-cr?style=flat)](https://github.com/sol-vin/raylib-cr/stargazers) - Direct bindings to [Raylib](https://raylib.com), which supports Linux, Windows, and Mac
 * [SDL-Crystal-Bindings](https://github.com/Hadeweka/SDL-Crystal-Bindings) [![GitHub stars](https://img.shields.io/github/stars/Hadeweka/SDL-Crystal-Bindings?style=flat)](https://github.com/Hadeweka/SDL-Crystal-Bindings/stargazers) - Direct (unsafe) bindings to [SDL2](https://www.libsdl.org/), intended for writing own game libraries

## GUI Development
 * [CrymbleUI](https://github.com/wolfgang371/crymbleui) [![GitHub stars](https://img.shields.io/github/stars/wolfgang371/crymbleui?style=flat)](https://github.com/wolfgang371/crymbleui/stargazers) - A nice and fast GUI framework for Crystal. Declarative DSL, Reactive State, Performant, Rich Widget Set including VirtualMatrix and RecursiveGrid
 * [crystal-imgui](https://github.com/oprypin/crystal-imgui) [![GitHub stars](https://img.shields.io/github/stars/oprypin/crystal-imgui?style=flat)](https://github.com/oprypin/crystal-imgui/stargazers) - Bindings to [Dear ImGui](https://github.com/ocornut/imgui) [![GitHub stars](https://img.shields.io/github/stars/ocornut/imgui?style=flat)](https://github.com/ocornut/imgui/stargazers), an immediate-mode graphical UI library
 * [GTK4.cr](https://github.com/hugopl/gtk4.cr) [![GitHub stars](https://img.shields.io/github/stars/hugopl/gtk4.cr?style=flat)](https://github.com/hugopl/gtk4.cr/stargazers) - Bindings for [GTK4](https://docs.gtk.org/gtk4/overview.html) with Crystalized API
 * [Iu](https://github.com/grkek/iu) [![GitHub stars](https://img.shields.io/github/stars/grkek/iu?style=flat)](https://github.com/grkek/iu/stargazers) - UI framework based on the [Fusion/libui.cr](https://github.com/Fusion/libui.cr) [![GitHub stars](https://img.shields.io/github/stars/Fusion/libui.cr?style=flat)](https://github.com/Fusion/libui.cr/stargazers) library, with custom elements and modified bindings from [hedron-crystal/hedron](https://github.com/hedron-crystal/hedron) [![GitHub stars](https://img.shields.io/github/stars/hedron-crystal/hedron?style=flat)](https://github.com/hedron-crystal/hedron/stargazers)
 * [Ultimate GTK4 Crystal Guide](https://ultimate-gtk4-crystal-guide.geopjr.dev/) - Learn how to create premium GTK4 apps in Crystal

## HTML Builders
 * [blueprint](https://github.com/gunbolt/blueprint) [![GitHub stars](https://img.shields.io/github/stars/gunbolt/blueprint?style=flat)](https://github.com/gunbolt/blueprint/stargazers) - Write reusable and testable HTML templates in plain Crystal
 * [form_builder.cr](https://github.com/westonganger/form_builder.cr) [![GitHub stars](https://img.shields.io/github/stars/westonganger/form_builder.cr?style=flat)](https://github.com/westonganger/form_builder.cr/stargazers) - Dead simple HTML form builder for Crystal with built-in support for many popular UI libraries such as Bootstrap
 * [to_html](https://github.com/sbsoftware/to_html.cr) [![GitHub stars](https://img.shields.io/github/stars/sbsoftware/to_html.cr?style=flat)](https://github.com/sbsoftware/to_html.cr/stargazers) - The fastest HTML builder engine for Crystal
 * [Water](https://github.com/shootingfly/water) [![GitHub stars](https://img.shields.io/github/stars/shootingfly/water?style=flat)](https://github.com/shootingfly/water/stargazers) - A library for writing HTML in plain Crystal

## HTML/XML Parsing
 * [docx_cr_converter](https://github.com/aristotelesbr/docx_cr_converter) [![GitHub stars](https://img.shields.io/github/stars/aristotelesbr/docx_cr_converter?style=flat)](https://github.com/aristotelesbr/docx_cr_converter/stargazers) - parse DOCX Word
 * [lexbor](https://github.com/kostya/lexbor) [![GitHub stars](https://img.shields.io/github/stars/kostya/lexbor?style=flat)](https://github.com/kostya/lexbor/stargazers) - Fast HTML5 Parser that includes CSS selectors

## HTTP
 * [Cable](https://github.com/cable-cr/cable) [![GitHub stars](https://img.shields.io/github/stars/cable-cr/cable?style=flat)](https://github.com/cable-cr/cable/stargazers) - An ActionCable "port" to Crystal, framework agnostic, 100% compatible with the ActionCable JS Client
 * [cossack](https://github.com/crystal-community/cossack) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/cossack?style=flat)](https://github.com/crystal-community/cossack/stargazers) - Simple flexible HTTP client
 * [crest](https://github.com/mamantoha/crest) [![GitHub stars](https://img.shields.io/github/stars/mamantoha/crest?style=flat)](https://github.com/mamantoha/crest/stargazers) - Simple HTTP and REST client, inspired by the Ruby's RestClient gem
 * [crul](https://github.com/porras/crul) [![GitHub stars](https://img.shields.io/github/stars/porras/crul?style=flat)](https://github.com/porras/crul/stargazers) - Command line HTTP client
 * [cryload](https://github.com/sdogruyol/cryload) [![GitHub stars](https://img.shields.io/github/stars/sdogruyol/cryload?style=flat)](https://github.com/sdogruyol/cryload/stargazers) - cryload is a powerful, fast, and practical HTTP benchmarking tool for stress testing APIs and web services
 * [digest-auth](https://github.com/spider-gazelle/digest-auth) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/digest-auth?style=flat)](https://github.com/spider-gazelle/digest-auth/stargazers) - Digest authentication
 * [halite](https://github.com/icyleaf/halite) [![GitHub stars](https://img.shields.io/github/stars/icyleaf/halite?style=flat)](https://github.com/icyleaf/halite/stargazers) - Crystal HTTP Requests with a chainable REST API, built-in sessions and loggers
 * [http-multiserver.cr](https://github.com/vladfaust/http-multiserver.cr) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/http-multiserver.cr?style=flat)](https://github.com/vladfaust/http-multiserver.cr/stargazers) - Mounting multiple servers via routes (a.k.a. URL mapping)
 * [http-params-serializable](https://github.com/vladfaust/http-params-serializable) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/http-params-serializable?style=flat)](https://github.com/vladfaust/http-params-serializable/stargazers) - HTTP params (de)serialization, applicable to URL queries and URL-encoded forms
 * [http-protection](https://github.com/rogeriozambon/http-protection) [![GitHub stars](https://img.shields.io/github/stars/rogeriozambon/http-protection?style=flat)](https://github.com/rogeriozambon/http-protection/stargazers) - Protection against typical web attacks
 * [http2](https://github.com/ysbaddaden/http2) [![GitHub stars](https://img.shields.io/github/stars/ysbaddaden/http2?style=flat)](https://github.com/ysbaddaden/http2/stargazers) - HTTP/2 Protocol Implementation
 * [HTTP::Client](https://crystal-lang.org/api/HTTP/Client.html) - HTTP client (Crystal stdlib)
 * [HTTP::Server](https://crystal-lang.org/api/HTTP/Server.html) - HTTP server (Crystal stdlib)
 * [HTTP::WebSocket](https://crystal-lang.org/api/HTTP/WebSocket.html) - HTTP WebSocket client (Crystal stdlib)
 * [link-header](https://github.com/spider-gazelle/link-header) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/link-header?style=flat)](https://github.com/spider-gazelle/link-header/stargazers) - HTTP Link Header Parser
 * [ntlm](https://github.com/spider-gazelle/ntlm) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/ntlm?style=flat)](https://github.com/spider-gazelle/ntlm/stargazers) - NTLM authentication
 * [proxy-fetcher.cr](https://github.com/nbulaj/proxy-fetcher.cr) [![GitHub stars](https://img.shields.io/github/stars/nbulaj/proxy-fetcher.cr?style=flat)](https://github.com/nbulaj/proxy-fetcher.cr/stargazers) - Proxy lists fetching & validating library
 * [sse.cr](https://github.com/y2k2mt/sse.cr) [![GitHub stars](https://img.shields.io/github/stars/y2k2mt/sse.cr?style=flat)](https://github.com/y2k2mt/sse.cr/stargazers) - [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html) client

## Image processing
 * [celestine](https://github.com/celestinecr/celestine) [![GitHub stars](https://img.shields.io/github/stars/celestinecr/celestine?style=flat)](https://github.com/celestinecr/celestine/stargazers) - Create SVG images using a DSL
 * [ffmpeg](https://github.com/spider-gazelle/ffmpeg) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/ffmpeg?style=flat)](https://github.com/spider-gazelle/ffmpeg/stargazers) - FFmpeg bindings that works with StumpyPNG to extract frames
 * [Pluto](https://github.com/phenopolis/pluto) [![GitHub stars](https://img.shields.io/github/stars/phenopolis/pluto?style=flat)](https://github.com/phenopolis/pluto/stargazers) - A fast and convenient image processing library
 * [stumpy_png](https://github.com/stumpycr/stumpy_png) [![GitHub stars](https://img.shields.io/github/stars/stumpycr/stumpy_png?style=flat)](https://github.com/stumpycr/stumpy_png/stargazers) - Read and write PNG images

## Implementations/Compilers
 * [charly](https://github.com/charly-lang) [![GitHub stars](https://img.shields.io/github/stars/charly-lang?style=flat)](https://github.com/charly-lang/stargazers) - Charly Programming Language
 * [cltk](https://github.com/ziprandom/cltk) [![GitHub stars](https://img.shields.io/github/stars/ziprandom/cltk?style=flat)](https://github.com/ziprandom/cltk/stargazers) - A crystal port of the Ruby Language Toolkit
 * [crisp](https://github.com/rhysd/Crisp) [![GitHub stars](https://img.shields.io/github/stars/rhysd/Crisp?style=flat)](https://github.com/rhysd/Crisp/stargazers) - Lisp dialect implemented with Crystal
 * [GiavaScript](https://github.com/memburg/GiavaScript) [![GitHub stars](https://img.shields.io/github/stars/memburg/GiavaScript?style=flat)](https://github.com/memburg/GiavaScript/stargazers) - Open-source, cross-platform JavaScript runtime
 * [LinCAS-lang](https://github.com/LinCAS-lang) [![GitHub stars](https://img.shields.io/github/stars/LinCAS-lang?style=flat)](https://github.com/LinCAS-lang/stargazers) - A programming language for scientific computation
 * [mint-lang](https://github.com/mint-lang/mint) [![GitHub stars](https://img.shields.io/github/stars/mint-lang/mint?style=flat)](https://github.com/mint-lang/mint/stargazers) - A refreshing programming language for the front-end web
 * [myst-lang](https://github.com/myst-lang/) [![GitHub stars](https://img.shields.io/github/stars/myst-lang/?style=flat)](https://github.com/myst-lang//stargazers) - A practical, dynamic language designed to be written and understood as easily and efficiently as possible
 * [novika](https://github.com/novika-lang/novika) [![GitHub stars](https://img.shields.io/github/stars/novika-lang/novika?style=flat)](https://github.com/novika-lang/novika/stargazers) - A free-form, moldable, interpreted programming language
 * [runic-lang](https://github.com/runic-lang) [![GitHub stars](https://img.shields.io/github/stars/runic-lang?style=flat)](https://github.com/runic-lang/stargazers) - In-design toy language

## Internationalization

 * [crystal-i18n](https://github.com/crystal-i18n/i18n) [![GitHub stars](https://img.shields.io/github/stars/crystal-i18n/i18n?style=flat)](https://github.com/crystal-i18n/i18n/stargazers) - An internationalization library inspired by Ruby-I18n
 * [i18n.cr](https://github.com/vladfaust/i18n.cr) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/i18n.cr?style=flat)](https://github.com/vladfaust/i18n.cr/stargazers) - Internationalization shard
 * [Lens](https://github.com/syeopite/lens) [![GitHub stars](https://img.shields.io/github/stars/syeopite/lens?style=flat)](https://github.com/syeopite/lens/stargazers) - A multiformat internationalization (i18n) shard for Crystal. Supports Gettext, Ruby YAML, etc.
 * [Rosetta](https://github.com/wout/rosetta) [![GitHub stars](https://img.shields.io/github/stars/wout/rosetta?style=flat)](https://github.com/wout/rosetta/stargazers) - A blazing fast internationalization (i18n) library with compile-time key lookup supporting YAML and JSON formats

## Logging and monitoring
 * [crafana](https://github.com/spoved/crafana.cr) [![GitHub stars](https://img.shields.io/github/stars/spoved/crafana.cr?style=flat)](https://github.com/spoved/crafana.cr/stargazers) - A [Grafana](https://grafana.com/) library to help autogenerate dashboards
 * [fiber_metrics.cr](https://github.com/didactic-drunk/fiber_metrics.cr) [![GitHub stars](https://img.shields.io/github/stars/didactic-drunk/fiber_metrics.cr?style=flat)](https://github.com/didactic-drunk/fiber_metrics.cr/stargazers) - Track run time, wait time, or memory allocations per `Fiber`, method or block
 * [Log](https://crystal-lang.org/api/Log.html) - logging utility (Crystal stdlib)
 * [statsd.cr](https://github.com/miketheman/statsd.cr) [![GitHub stars](https://img.shields.io/github/stars/miketheman/statsd.cr?style=flat)](https://github.com/miketheman/statsd.cr/stargazers) - [Statsd](https://github.com/etsy/statsd) [![GitHub stars](https://img.shields.io/github/stars/etsy/statsd?style=flat)](https://github.com/etsy/statsd/stargazers) client library

## Machine Learning
 * [ai4cr](https://github.com/drhuffman12/ai4cr) [![GitHub stars](https://img.shields.io/github/stars/drhuffman12/ai4cr?style=flat)](https://github.com/drhuffman12/ai4cr/stargazers) - Artificial Intelligence (based on https://github.com/SergioFierens/ai4r)
 * [Cadmium](https://github.com/cadmiumcr/cadmium) [![GitHub stars](https://img.shields.io/github/stars/cadmiumcr/cadmium?style=flat)](https://github.com/cadmiumcr/cadmium/stargazers) - NLP library based heavily on [natural](https://github.com/NaturalNode/natural) [![GitHub stars](https://img.shields.io/github/stars/NaturalNode/natural?style=flat)](https://github.com/NaturalNode/natural/stargazers)
 * [crystal-fann](https://github.com/NeuraLegion/crystal-fann) [![GitHub stars](https://img.shields.io/github/stars/NeuraLegion/crystal-fann?style=flat)](https://github.com/NeuraLegion/crystal-fann/stargazers) - FANN (Fast Artifical Neural Network) binding
 * [mxnet.cr](https://github.com/toddsundsted/mxnet.cr) [![GitHub stars](https://img.shields.io/github/stars/toddsundsted/mxnet.cr?style=flat)](https://github.com/toddsundsted/mxnet.cr/stargazers) - Bindings for [MXNet](https://mxnet.incubator.apache.org/)
 * [shainet](https://github.com/NeuraLegion/shainet) [![GitHub stars](https://img.shields.io/github/stars/NeuraLegion/shainet?style=flat)](https://github.com/NeuraLegion/shainet/stargazers) - SHAInet (Neural Network in pure crystal)

## Markdown/Text Processors
 * [cr-cmark-gfm](https://github.com/amauryt/cr-cmark-gfm) [![GitHub stars](https://img.shields.io/github/stars/amauryt/cr-cmark-gfm?style=flat)](https://github.com/amauryt/cr-cmark-gfm/stargazers) -  Crystal C bindings for cmark-gfm to work with Commonmark and Github Flavored Markdown
 * [markd](https://github.com/icyleaf/markd) [![GitHub stars](https://img.shields.io/github/stars/icyleaf/markd?style=flat)](https://github.com/icyleaf/markd/stargazers) - Yet another markdown parser built for speed, Compliant to CommonMark specification

## Misc
 * [aasm.cr](https://github.com/veelenga/aasm.cr) [![GitHub stars](https://img.shields.io/github/stars/veelenga/aasm.cr?style=flat)](https://github.com/veelenga/aasm.cr/stargazers) - Easy to use finite state machine for Crystal classes
 * [any_hash.cr](https://github.com/Sija/any_hash.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/any_hash.cr?style=flat)](https://github.com/Sija/any_hash.cr/stargazers) - Recursive Hash with better JSON::Any included
 * [anyolite](https://github.com/Anyolite/anyolite) [![GitHub stars](https://img.shields.io/github/stars/Anyolite/anyolite?style=flat)](https://github.com/Anyolite/anyolite/stargazers) - Full mruby interpreter with simple bindings, allowing for easy scripting support in projects
 * [burocracia.cr](https://github.com/vinibrsl/burocracia.cr) [![GitHub stars](https://img.shields.io/github/stars/vinibrsl/burocracia.cr?style=flat)](https://github.com/vinibrsl/burocracia.cr/stargazers) - burocracia.cr the dependecyless shard to validate, generate and format Brazilian burocracias such as CPF, CNPJ and CEP
 * [callbacks](https://github.com/vladfaust/callbacks.cr) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/callbacks.cr?style=flat)](https://github.com/vladfaust/callbacks.cr/stargazers) - Expressive callbacks module
 * [circuit_breaker](https://github.com/TPei/circuit_breaker) [![GitHub stars](https://img.shields.io/github/stars/TPei/circuit_breaker?style=flat)](https://github.com/TPei/circuit_breaker/stargazers) - Implementation of the circuit breaker pattern
 * [cpf_cnpj](https://codeberg.org/gunbolt/cpf_cnpj) - Provide utilities for validating and formatting CPF and CNPJ identifiers
 * [CrSignals](https://github.com/firejox/CrSignals) [![GitHub stars](https://img.shields.io/github/stars/firejox/CrSignals?style=flat)](https://github.com/firejox/CrSignals/stargazers) - Signals/slots notification library
 * [crystal-binary_parser](https://github.com/DanSnow/crystal-binary_parser) [![GitHub stars](https://img.shields.io/github/stars/DanSnow/crystal-binary_parser?style=flat)](https://github.com/DanSnow/crystal-binary_parser/stargazers) - Binary parser
 * [crystal-web-framework-stars](https://github.com/isaced/crystal-web-framework-stars) [![GitHub stars](https://img.shields.io/github/stars/isaced/crystal-web-framework-stars?style=flat)](https://github.com/isaced/crystal-web-framework-stars/stargazers) - Web frameworks for Crystal, most starred on Github
 * [crz](https://github.com/dhruvrajvanshi/crz) [![GitHub stars](https://img.shields.io/github/stars/dhruvrajvanshi/crz?style=flat)](https://github.com/dhruvrajvanshi/crz/stargazers) - Functional programming library
 * [defined](https://github.com/wyhaines/defined.cr) [![GitHub stars](https://img.shields.io/github/stars/wyhaines/defined.cr?style=flat)](https://github.com/wyhaines/defined.cr/stargazers) - macros for conditional compilation based on constant definitions, version requirements, or environment variable settings
 * [emoji.cr](https://github.com/veelenga/emoji.cr) [![GitHub stars](https://img.shields.io/github/stars/veelenga/emoji.cr?style=flat)](https://github.com/veelenga/emoji.cr/stargazers) - Emoji library
 * [gphoto2-web.cr](https://github.com/Sija/gphoto2-web.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/gphoto2-web.cr?style=flat)](https://github.com/Sija/gphoto2-web.cr/stargazers) - Web API for libgphoto2
 * [immutable](https://github.com/lucaong/immutable) [![GitHub stars](https://img.shields.io/github/stars/lucaong/immutable?style=flat)](https://github.com/lucaong/immutable/stargazers) - Implementation of thread-safe, persistent, immutable collections
 * [iterm2](https://github.com/toddsundsted/iterm2) [![GitHub stars](https://img.shields.io/github/stars/toddsundsted/iterm2?style=flat)](https://github.com/toddsundsted/iterm2/stargazers) - Display images within the terminal using the ITerm2 Inline Images Protocol
 * [lua.cr](https://github.com/veelenga/lua.cr) [![GitHub stars](https://img.shields.io/github/stars/veelenga/lua.cr?style=flat)](https://github.com/veelenga/lua.cr/stargazers) - Bindings to liblua and a wrapper around it
 * [luajit.cr](https://github.com/mdwagner/luajit.cr) [![GitHub stars](https://img.shields.io/github/stars/mdwagner/luajit.cr?style=flat)](https://github.com/mdwagner/luajit.cr/stargazers) - LuaJIT bindings for Crystal
 * [monads](https://github.com/alex-lairan/monads) [![GitHub stars](https://img.shields.io/github/stars/alex-lairan/monads?style=flat)](https://github.com/alex-lairan/monads/stargazers) - Monad implementation
 * [observable](https://github.com/TPei/observable) [![GitHub stars](https://img.shields.io/github/stars/TPei/observable?style=flat)](https://github.com/TPei/observable/stargazers) - Implementation of the observer pattern
 * [pinger](https://github.com/spider-gazelle/pinger) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/pinger?style=flat)](https://github.com/spider-gazelle/pinger/stargazers) - Ping IP addresses and DNS entries without requiring sudo
 * [port_midi](https://github.com/jimm/crystal_port_midi) [![GitHub stars](https://img.shields.io/github/stars/jimm/crystal_port_midi?style=flat)](https://github.com/jimm/crystal_port_midi/stargazers) - Crystal C bindings for the PortMIDI cross-platform MIDI I/O library
 * [retriable.cr](https://github.com/Sija/retriable.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/retriable.cr?style=flat)](https://github.com/Sija/retriable.cr/stargazers) - Simple DSL to retry failed code blocks
 * [sentry](https://github.com/crystal-china/sentry) [![GitHub stars](https://img.shields.io/github/stars/crystal-china/sentry?style=flat)](https://github.com/crystal-china/sentry/stargazers) - Build/Runs your crystal application, watches files, and rebuilds/restarts app on file changes.
 * [serf-handler.cr](https://github.com/wyhaines/serf-handler.cr) [![GitHub stars](https://img.shields.io/github/stars/wyhaines/serf-handler.cr?style=flat)](https://github.com/wyhaines/serf-handler.cr/stargazers) - Framework for building Serf handlers, with a suite of useful builtin capabilities
 * [simple_retry](https://github.com/spider-gazelle/simple_retry) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/simple_retry?style=flat)](https://github.com/spider-gazelle/simple_retry/stargazers) - Simple tool for retrying failed code blocks
 * [sslscan.cr](https://github.com/NeuraLegion/sslscan.cr) [![GitHub stars](https://img.shields.io/github/stars/NeuraLegion/sslscan.cr?style=flat)](https://github.com/NeuraLegion/sslscan.cr/stargazers) - Crystal shard wrapping the rbsec/sslscan utility
 * [version_tools](https://github.com/anicholson/crystal-version-tools) [![GitHub stars](https://img.shields.io/github/stars/anicholson/crystal-version-tools?style=flat)](https://github.com/anicholson/crystal-version-tools/stargazers) - Version-dependent behaviour, specified at compile-time
 * [wafalyzer](https://github.com/NeuraLegion/wafalyzer) [![GitHub stars](https://img.shields.io/github/stars/NeuraLegion/wafalyzer?style=flat)](https://github.com/NeuraLegion/wafalyzer/stargazers) - Web Application Firewall (WAF) Detector - shard + cli
 * [zaru_crystal](https://github.com/szTheory/zaru_crystal) [![GitHub stars](https://img.shields.io/github/stars/szTheory/zaru_crystal?style=flat)](https://github.com/szTheory/zaru_crystal/stargazers) - Filename sanitization

## Network Protocols
 * [amqp-client.cr](https://github.com/cloudamqp/amqp-client.cr) [![GitHub stars](https://img.shields.io/github/stars/cloudamqp/amqp-client.cr?style=flat)](https://github.com/cloudamqp/amqp-client.cr/stargazers) - AMQP 0-9.1, a messaging protocol, implemented by eg. RabbitMQ
 * [connect-proxy](https://github.com/spider-gazelle/connect-proxy) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/connect-proxy?style=flat)](https://github.com/spider-gazelle/connect-proxy/stargazers) - Connect method style of HTTP tunnelling / HTTP proxy
 * [cr-xmpp](https://github.com/naqvis/cr-xmpp) [![GitHub stars](https://img.shields.io/github/stars/naqvis/cr-xmpp?style=flat)](https://github.com/naqvis/cr-xmpp/stargazers) - XMPP/Jabber Library
 * [Crirc](https://github.com/Meoowww/Crirc) [![GitHub stars](https://img.shields.io/github/stars/Meoowww/Crirc?style=flat)](https://github.com/Meoowww/Crirc/stargazers) - IRC protocol implementation (Client, Server, Bots)
 * [crystal-bacnet](https://github.com/spider-gazelle/crystal-bacnet) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/crystal-bacnet?style=flat)](https://github.com/spider-gazelle/crystal-bacnet/stargazers) - BACnet protocol implementation with BACnet/IP client
 * [crystal-json-socket](https://github.com/foi/crystal-json-socket) [![GitHub stars](https://img.shields.io/github/stars/foi/crystal-json-socket?style=flat)](https://github.com/foi/crystal-json-socket/stargazers) - JSON-socket client & server implementation. Inspired by and compatible with [node-json-socket](https://github.com/sebastianseilund/node-json-socket/) [![GitHub stars](https://img.shields.io/github/stars/sebastianseilund/node-json-socket/?style=flat)](https://github.com/sebastianseilund/node-json-socket//stargazers) and [ruby-json-socket](https://github.com/foi/ruby-json-socket) [![GitHub stars](https://img.shields.io/github/stars/foi/ruby-json-socket?style=flat)](https://github.com/foi/ruby-json-socket/stargazers)
 * [crystal-mqtt](https://github.com/spider-gazelle/crystal-mqtt) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/crystal-mqtt?style=flat)](https://github.com/spider-gazelle/crystal-mqtt/stargazers) - A MQTT client
 * [crystal-snmp](https://github.com/spider-gazelle/crystal-snmp) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/crystal-snmp?style=flat)](https://github.com/spider-gazelle/crystal-snmp/stargazers) - An SNMP implementation with version 1, 2c and 3 support
 * [dns](https://github.com/spider-gazelle/dns) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/dns?style=flat)](https://github.com/spider-gazelle/dns/stargazers) - DNS protocol implementation and resolver
 * [fast_irc.cr](https://github.com/RX14/fast_irc.cr) [![GitHub stars](https://img.shields.io/github/stars/RX14/fast_irc.cr?style=flat)](https://github.com/RX14/fast_irc.cr/stargazers) - Fast IRC parser/generator
 * [jwt](https://github.com/crystal-community/jwt) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/jwt?style=flat)](https://github.com/crystal-community/jwt/stargazers) - Implementation of JWT (JSON Web Token)
 * [knx](https://github.com/spider-gazelle/knx) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/knx?style=flat)](https://github.com/spider-gazelle/knx/stargazers) - KNX protocol implementation supporting multicast, unicast and TCP/IP tunnelling
 * [Matter](https://github.com/Crystal-Matter/matter) [![GitHub stars](https://img.shields.io/github/stars/Crystal-Matter/matter?style=flat)](https://github.com/Crystal-Matter/matter/stargazers) - Matter protocol for smart home and Internet of things (IoT) devices
 * [mDNS](https://github.com/spider-gazelle/mdns) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/mdns?style=flat)](https://github.com/spider-gazelle/mdns/stargazers) - DNS Service Discovery and multicast DNS
 * [mqtt-client.cr](https://github.com/84codes/mqtt-client.cr) [![GitHub stars](https://img.shields.io/github/stars/84codes/mqtt-client.cr?style=flat)](https://github.com/84codes/mqtt-client.cr/stargazers) - A fast and lightweight MQTT client
 * [msgpack-crystal](https://github.com/crystal-community/msgpack-crystal) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/msgpack-crystal?style=flat)](https://github.com/crystal-community/msgpack-crystal/stargazers) - MessagePack library
 * [OAuth](https://crystal-lang.org/api/OAuth.html) - OAuth consumer (Crystal stdlib)
 * [OAuth2](https://crystal-lang.org/api/OAuth2.html) - OAuth2 client (Crystal stdlib)
 * [OpenSSL](https://crystal-lang.org/api/OpenSSL.html) - bindings to libssl (Crystal stdlib)
 * [simple_rpc](https://github.com/kostya/simple_rpc) [![GitHub stars](https://img.shields.io/github/stars/kostya/simple_rpc?style=flat)](https://github.com/kostya/simple_rpc/stargazers) - RPC Server and Client for Crystal. Implements msgpack-rpc protocol
 * [stomp](https://github.com/spider-gazelle/stomp) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/stomp?style=flat)](https://github.com/spider-gazelle/stomp/stargazers) - STOMP protocol
 * [telnet.cr](https://github.com/spider-gazelle/telnet.cr) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/telnet.cr?style=flat)](https://github.com/spider-gazelle/telnet.cr/stargazers) - Telnet protocol
 * [transfer_more](https://git.sceptique.eu/Sceptique/transfer_more) - Clone of transfer.sh to uploads files

## Networking
 * [ipaddress.cr](https://github.com/Sija/ipaddress.cr) [![GitHub stars](https://img.shields.io/github/stars/Sija/ipaddress.cr?style=flat)](https://github.com/Sija/ipaddress.cr/stargazers) - Library to handle IPv4 and IPv6 addresses
 * [mac-address](https://github.com/automatico/mac-address) [![GitHub stars](https://img.shields.io/github/stars/automatico/mac-address?style=flat)](https://github.com/automatico/mac-address/stargazers) - Library for working with MAC addresses

## ORM/ODM Extensions
 * [avram](https://github.com/luckyframework/avram) [![GitHub stars](https://img.shields.io/github/stars/luckyframework/avram?style=flat)](https://github.com/luckyframework/avram/stargazers) - A database wrapper for reading, writing, and migrating Postgres databases
 * [clear](https://github.com/anykeyh/clear) [![GitHub stars](https://img.shields.io/github/stars/anykeyh/clear?style=flat)](https://github.com/anykeyh/clear/stargazers) - ORM specialized to PostgreSQL only but with advanced features
 * [crecto](https://github.com/Crecto/crecto) [![GitHub stars](https://img.shields.io/github/stars/Crecto/crecto?style=flat)](https://github.com/Crecto/crecto/stargazers) - Database wrapper, based on Ecto
 * [granite](https://github.com/amberframework/granite) [![GitHub stars](https://img.shields.io/github/stars/amberframework/granite?style=flat)](https://github.com/amberframework/granite/stargazers) - ORM for Postgres, Mysql, Sqlite
 * [jennifer.cr](https://github.com/imdrasil/jennifer.cr) [![GitHub stars](https://img.shields.io/github/stars/imdrasil/jennifer.cr?style=flat)](https://github.com/imdrasil/jennifer.cr/stargazers) - Active Record pattern implementation with flexible query chainable builder and migration system
 * [lustra](https://github.com/crystal-garage/lustra) [![GitHub stars](https://img.shields.io/github/stars/crystal-garage/lustra?style=flat)](https://github.com/crystal-garage/lustra/stargazers) - Advanced PostgreSQL ORM with ActiveRecord pattern, full-text search, geometry types, and more
 * [rethinkdb-orm](https://github.com/spider-gazelle/rethinkdb-orm) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/rethinkdb-orm?style=flat)](https://github.com/spider-gazelle/rethinkdb-orm/stargazers) - ORM for RethinkDB / RebirthDB

## Package Management
 * [shards](https://github.com/crystal-lang/shards) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/shards?style=flat)](https://github.com/crystal-lang/shards/stargazers) - Dependency manager for the Crystal

## Processes and Threads
 * [await_async](https://github.com/anykeyh/await_async) [![GitHub stars](https://img.shields.io/github/stars/anykeyh/await_async?style=flat)](https://github.com/anykeyh/await_async/stargazers) - Add keywords await & async in Crystal Lang
 * [concurrent.cr](https://github.com/didactic-drunk/concurrent.cr) [![GitHub stars](https://img.shields.io/github/stars/didactic-drunk/concurrent.cr?style=flat)](https://github.com/didactic-drunk/concurrent.cr/stargazers) - Simplified concurrency using streams/pipelines, waitgroups, semaphores, smores and more
 * [neph](https://github.com/tbrand/neph) [![GitHub stars](https://img.shields.io/github/stars/tbrand/neph?style=flat)](https://github.com/tbrand/neph/stargazers) - A modern command line job processor that can execute jobs concurrently
 * [promise](https://github.com/spider-gazelle/promise) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/promise?style=flat)](https://github.com/spider-gazelle/promise/stargazers) - A Promise implementation with type inference
 * [werk](https://github.com/marghidanu/werk) [![GitHub stars](https://img.shields.io/github/stars/marghidanu/werk?style=flat)](https://github.com/marghidanu/werk/stargazers) - Dead simple task runner with concurrent support, ideal for local CI

## Project Generators
 * [crygen](https://github.com/tamdaz/crygen) [![GitHub stars](https://img.shields.io/github/stars/tamdaz/crygen?style=flat)](https://github.com/tamdaz/crygen/stargazers) - A library that allows to generate the Crystal code
 * [crystal_lib](https://github.com/crystal-lang/crystal_lib) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/crystal_lib?style=flat)](https://github.com/crystal-lang/crystal_lib/stargazers) - Automatic binding generator for native libraries
 * [fez](https://github.com/jwoertink/fez) [![GitHub stars](https://img.shields.io/github/stars/jwoertink/fez?style=flat)](https://github.com/jwoertink/fez/stargazers) - A Kemal application generator
 * [libgen](https://github.com/olbat/libgen) [![GitHub stars](https://img.shields.io/github/stars/olbat/libgen?style=flat)](https://github.com/olbat/libgen/stargazers) - Automatic bindings generator configured using JSON/YAML files

## Queues and Messaging
 * [crafka](https://github.com/BT-OpenSource/crafka) [![GitHub stars](https://img.shields.io/github/stars/BT-OpenSource/crafka?style=flat)](https://github.com/BT-OpenSource/crafka/stargazers) - Apache Kafka library utilizing `librdkafka`
 * [mosquito](https://github.com/mosquito-cr/mosquito/) [![GitHub stars](https://img.shields.io/github/stars/mosquito-cr/mosquito/?style=flat)](https://github.com/mosquito-cr/mosquito//stargazers) - Redis backed periodic and ad hoc job processing
 * [NATS.io](https://github.com/nats-io/nats.cr) [![GitHub stars](https://img.shields.io/github/stars/nats-io/nats.cr?style=flat)](https://github.com/nats-io/nats.cr/stargazers) - NATS client
 * [sidekiq.cr](https://github.com/mperham/sidekiq.cr) [![GitHub stars](https://img.shields.io/github/stars/mperham/sidekiq.cr?style=flat)](https://github.com/mperham/sidekiq.cr/stargazers) - Simple, efficient job processing

## Routing
 * [orion](https://github.com/obsidian/orion) [![GitHub stars](https://img.shields.io/github/stars/obsidian/orion?style=flat)](https://github.com/obsidian/orion/stargazers) - A minimal, rails-esque routing library
 * [router.cr](https://github.com/tbrand/router.cr) [![GitHub stars](https://img.shields.io/github/stars/tbrand/router.cr?style=flat)](https://github.com/tbrand/router.cr/stargazers) - Minimum but powerful http router for HTTP::Server

## Scheduling
 * [crystime](https://gitlab.com/crystallabs/crystime) - Advanced time, calendar, schedule, and remind library
 * [schedule.cr](https://github.com/hugoabonizio/schedule.cr) [![GitHub stars](https://img.shields.io/github/stars/hugoabonizio/schedule.cr?style=flat)](https://github.com/hugoabonizio/schedule.cr/stargazers) - Run periodic tasks
 * [tasker](https://github.com/spider-gazelle/tasker) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/tasker?style=flat)](https://github.com/spider-gazelle/tasker/stargazers) - A high precision scheduler including timezone aware cron jobs

## Science and Data analysis
 * [alea](https://github.com/nin93/alea) [![GitHub stars](https://img.shields.io/github/stars/nin93/alea?style=flat)](https://github.com/nin93/alea/stargazers) - Repeatable sampling, CDF and other utilities to work with probability distributions
 * [ishi](https://github.com/toddsundsted/ishi) [![GitHub stars](https://img.shields.io/github/stars/toddsundsted/ishi?style=flat)](https://github.com/toddsundsted/ishi/stargazers) - Graph plotting package with a small API and sensible defaults powered by gnuplot
 * [linalg](https://github.com/konovod/linalg) [![GitHub stars](https://img.shields.io/github/stars/konovod/linalg?style=flat)](https://github.com/konovod/linalg/stargazers) - Linear algebra library inspired by MATLAB and SciPy.linalg
 * [num.cr](https://github.com/crystal-data/num.cr) [![GitHub stars](https://img.shields.io/github/stars/crystal-data/num.cr?style=flat)](https://github.com/crystal-data/num.cr/stargazers) - Numerical computing library supporting N-Dimensional data
 * [predict.cr](https://github.com/RX14/predict.cr) [![GitHub stars](https://img.shields.io/github/stars/RX14/predict.cr?style=flat)](https://github.com/RX14/predict.cr/stargazers) - Satellite prediction library using the sgp4 model
 * [quartz](https://github.com/RomainFranceschini/quartz) [![GitHub stars](https://img.shields.io/github/stars/RomainFranceschini/quartz?style=flat)](https://github.com/RomainFranceschini/quartz/stargazers) - Modeling and simulation framework

## Search
 * [hermes](https://github.com/imdrasil/hermes.cr) [![GitHub stars](https://img.shields.io/github/stars/imdrasil/hermes.cr?style=flat)](https://github.com/imdrasil/hermes.cr/stargazers) - Data Mapper pattern implementation for ElastiSearch

## Security
 * [cyclonedx-cr](https://github.com/hahwul/cyclonedx-cr) [![GitHub stars](https://img.shields.io/github/stars/hahwul/cyclonedx-cr?style=flat)](https://github.com/hahwul/cyclonedx-cr/stargazers) - CycloneDX SBOM(Software Bill of Materials) generator for Crystal projects
 * [OWASP Noir](https://github.com/owasp-noir/noir) [![GitHub stars](https://img.shields.io/github/stars/owasp-noir/noir?style=flat)](https://github.com/owasp-noir/noir/stargazers) - Attack surface detector that identifies endpoints by static analysis
 * [XSSMaze](https://github.com/hahwul/xssmaze) [![GitHub stars](https://img.shields.io/github/stars/hahwul/xssmaze?style=flat)](https://github.com/hahwul/xssmaze/stargazers) - XSSMaze is a web service that tests security tools using diverse XSS cases

## Serverless Computing
 * [crystal_openfaas](https://github.com/TPei/crystal_openfaas/) [![GitHub stars](https://img.shields.io/github/stars/TPei/crystal_openfaas/?style=flat)](https://github.com/TPei/crystal_openfaas//stargazers) - Template to enable crystal as first class citizens in OpenFaaS
 * [secrets-env](https://github.com/spider-gazelle/secrets-env) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/secrets-env?style=flat)](https://github.com/spider-gazelle/secrets-env/stargazers) - Extends ENV module to read values injected by docker / kubernetes secrets and other orchestration tools

## System
 * [baked_file_system](https://github.com/schovi/baked_file_system) [![GitHub stars](https://img.shields.io/github/stars/schovi/baked_file_system?style=flat)](https://github.com/schovi/baked_file_system/stargazers) - Virtual file system implementation
 * [hardware](https://github.com/crystal-community/hardware) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/hardware?style=flat)](https://github.com/crystal-community/hardware/stargazers) - Get CPU, Memory and Network informations of the running OS and its processes

## Task management
 * [cake](https://github.com/axvm/cake) [![GitHub stars](https://img.shields.io/github/stars/axvm/cake?style=flat)](https://github.com/axvm/cake/stargazers) - Production-ready Make-like utility tool
 * [sam](https://github.com/imdrasil/sam.cr) [![GitHub stars](https://img.shields.io/github/stars/imdrasil/sam.cr?style=flat)](https://github.com/imdrasil/sam.cr/stargazers) - Another one Rake-like task manager with namespacing and arguments system

## Template Engine
 * [crinja](https://github.com/straight-shoota/crinja) [![GitHub stars](https://img.shields.io/github/stars/straight-shoota/crinja?style=flat)](https://github.com/straight-shoota/crinja/stargazers) - An implementation of the [Jinja2 template engine](http://jinja.pocoo.org/)
 * [crustache](https://github.com/MakeNowJust/crustache) [![GitHub stars](https://img.shields.io/github/stars/MakeNowJust/crustache?style=flat)](https://github.com/MakeNowJust/crustache/stargazers) - [{{Mustache}}](https://mustache.github.io) for Crystal
 * [ECR (Embedded Crystal)](https://crystal-lang.org/api/ECR.html) - compile time template language which uses plain crystal expressions (Crystal stdlib)
 * [Jbuilder](https://github.com/shootingfly/jbuilder) [![GitHub stars](https://img.shields.io/github/stars/shootingfly/jbuilder?style=flat)](https://github.com/shootingfly/jbuilder/stargazers) - Generate JSON objects with a Builder-style DSL, inspired by jbuilder
 * [Kilt](https://github.com/jeromegn/kilt) [![GitHub stars](https://img.shields.io/github/stars/jeromegn/kilt?style=flat)](https://github.com/jeromegn/kilt/stargazers) - Abstraction layer for template engines
 * [Slang](https://github.com/jeromegn/slang) [![GitHub stars](https://img.shields.io/github/stars/jeromegn/slang?style=flat)](https://github.com/jeromegn/slang/stargazers) - Lightweight, terse, templating language inspired by Ruby's Slim
 * [teeplate](https://github.com/mosop/teeplate) [![GitHub stars](https://img.shields.io/github/stars/mosop/teeplate?style=flat)](https://github.com/mosop/teeplate/stargazers) - A library for rendering multiple template files

## Testing
 * [Athena Spec](https://github.com/athena-framework/spec) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/spec?style=flat)](https://github.com/athena-framework/spec/stargazers) - Common/helpful [Spec](https://crystal-lang.org/api/Spec.html) compliant testing utilities
 * [crotest](https://github.com/emancu/crotest) [![GitHub stars](https://img.shields.io/github/stars/emancu/crotest?style=flat)](https://github.com/emancu/crotest/stargazers) - A tiny and simple test framework
 * [crytic](https://github.com/hanneskaeufler/crytic) [![GitHub stars](https://img.shields.io/github/stars/hanneskaeufler/crytic?style=flat)](https://github.com/hanneskaeufler/crytic/stargazers) - Mutation testing framework
 * [hashr](https://github.com/crystal-china/hashr) [![GitHub stars](https://img.shields.io/github/stars/crystal-china/hashr?style=flat)](https://github.com/crystal-china/hashr/stargazers) - A tiny class makes test on JSON response easier
 * [LuckyFlow](https://github.com/luckyframework/lucky_flow) [![GitHub stars](https://img.shields.io/github/stars/luckyframework/lucky_flow?style=flat)](https://github.com/luckyframework/lucky_flow/stargazers) - Automated browser tests similar to Capybara
 * [mass-spec](https://github.com/c910335/mass-spec) [![GitHub stars](https://img.shields.io/github/stars/c910335/mass-spec?style=flat)](https://github.com/c910335/mass-spec/stargazers) - Web API testing library
 * [microtest](https://github.com/Ragmaanir/microtest) [![GitHub stars](https://img.shields.io/github/stars/Ragmaanir/microtest?style=flat)](https://github.com/Ragmaanir/microtest/stargazers) - Small opinionated testing library focusing on power asserts
 * [minitest.cr](https://github.com/ysbaddaden/minitest.cr) [![GitHub stars](https://img.shields.io/github/stars/ysbaddaden/minitest.cr?style=flat)](https://github.com/ysbaddaden/minitest.cr/stargazers) - Library for unit tests and assertions
 * [mocks.cr](https://github.com/waterlink/mocks.cr) [![GitHub stars](https://img.shields.io/github/stars/waterlink/mocks.cr?style=flat)](https://github.com/waterlink/mocks.cr/stargazers) - Mocking library for Crystal
 * [selenium.cr](https://github.com/crystal-loot/selenium.cr) [![GitHub stars](https://img.shields.io/github/stars/crystal-loot/selenium.cr?style=flat)](https://github.com/crystal-loot/selenium.cr/stargazers) - Selenium client for interacting with web pages for browser automation
 * [Spec](https://crystal-lang.org/api/Spec.html) - spec framework (Crystal stdlib)
 * [spectator](https://gitlab.com/arctic-fox/spectator) - Feature rich spec framework that uses the modern expect syntax
 * [timecop.cr](https://github.com/crystal-community/timecop.cr) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/timecop.cr?style=flat)](https://github.com/crystal-community/timecop.cr/stargazers) - Library for mocking with `Time.now`. Inspired by the [timecop ruby gem](https://github.com/travisjeffery/timecop) [![GitHub stars](https://img.shields.io/github/stars/travisjeffery/timecop?style=flat)](https://github.com/travisjeffery/timecop/stargazers)
 * [vcr](https://github.com/spoved/vcr.cr) [![GitHub stars](https://img.shields.io/github/stars/spoved/vcr.cr?style=flat)](https://github.com/spoved/vcr.cr/stargazers) - A HTTP capture and replay implementation for crystal
 * [webdriver_pump](https://github.com/bwilczek/webdriver_pump) [![GitHub stars](https://img.shields.io/github/stars/bwilczek/webdriver_pump?style=flat)](https://github.com/bwilczek/webdriver_pump/stargazers) - Page Object library. Inspired by Ruby's [WatirPump](https://github.com/bwilczek/watir_pump) [![GitHub stars](https://img.shields.io/github/stars/bwilczek/watir_pump?style=flat)](https://github.com/bwilczek/watir_pump/stargazers)
 * [webmock.cr](https://github.com/manastech/webmock.cr) [![GitHub stars](https://img.shields.io/github/stars/manastech/webmock.cr?style=flat)](https://github.com/manastech/webmock.cr/stargazers) - Library for stubbing `HTTP::Client` requests

## Third-party APIs
 * [amazonite](https://github.com/rjnienaber/amazonite) [![GitHub stars](https://img.shields.io/github/stars/rjnienaber/amazonite?style=flat)](https://github.com/rjnienaber/amazonite/stargazers) - An unofficial SDK supporting popular AWS APIs
 * [aws-signer.cr](https://github.com/beanieboi/aws-signer.cr) [![GitHub stars](https://img.shields.io/github/stars/beanieboi/aws-signer.cr?style=flat)](https://github.com/beanieboi/aws-signer.cr/stargazers) - This library signs your HTTP requests using AWS v4
 * [awscr-s3](https://github.com/taylorfinnell/awscr-s3) [![GitHub stars](https://img.shields.io/github/stars/taylorfinnell/awscr-s3?style=flat)](https://github.com/taylorfinnell/awscr-s3/stargazers) - AWS S3 interface
 * [awscr-signer](https://github.com/taylorfinnell/awscr-signer) [![GitHub stars](https://img.shields.io/github/stars/taylorfinnell/awscr-signer?style=flat)](https://github.com/taylorfinnell/awscr-signer/stargazers) - Sign HTTP::Request objects and generate presigned post forms
 * [crystal-consul](https://github.com/rogerwelin/crystal-consul) [![GitHub stars](https://img.shields.io/github/stars/rogerwelin/crystal-consul?style=flat)](https://github.com/rogerwelin/crystal-consul/stargazers) - Consul API client
 * [crystal-darksky](https://github.com/sb89/crystal-darksky) [![GitHub stars](https://img.shields.io/github/stars/sb89/crystal-darksky?style=flat)](https://github.com/sb89/crystal-darksky/stargazers) - Wrapper for the [Dark Sky](https://darksky.net) API
 * [crystal-swapi](https://github.com/sb89/crystal-swapi) [![GitHub stars](https://img.shields.io/github/stars/sb89/crystal-swapi?style=flat)](https://github.com/sb89/crystal-swapi/stargazers) - Star Wars API (SWAPI) wrapper
 * [crystal_slack](https://github.com/manastech/crystal_slack) [![GitHub stars](https://img.shields.io/github/stars/manastech/crystal_slack?style=flat)](https://github.com/manastech/crystal_slack/stargazers) - A tool that parses Slack slash commands or send incoming web hooks
 * [GDAX](https://github.com/mccallofthewild/gdax) [![GitHub stars](https://img.shields.io/github/stars/mccallofthewild/gdax?style=flat)](https://github.com/mccallofthewild/gdax/stargazers) - GDAX REST and WebSocket API Wrapper with request signing
 * [gitlab.cr](https://github.com/icyleaf/gitlab.cr) [![GitHub stars](https://img.shields.io/github/stars/icyleaf/gitlab.cr?style=flat)](https://github.com/icyleaf/gitlab.cr/stargazers) - GitLab API wrapper
 * [google](https://github.com/PlaceOS/google) [![GitHub stars](https://img.shields.io/github/stars/PlaceOS/google?style=flat)](https://github.com/PlaceOS/google/stargazers) - Google API wrapper
 * [host_meta](https://github.com/toddsundsted/host_meta) [![GitHub stars](https://img.shields.io/github/stars/toddsundsted/host_meta?style=flat)](https://github.com/toddsundsted/host_meta/stargazers) - A Web Host Metadata (https://tools.ietf.org/html/rfc6415) client
 * [kube-client.cr](https://github.com/spoved/kube-client.cr) [![GitHub stars](https://img.shields.io/github/stars/spoved/kube-client.cr?style=flat)](https://github.com/spoved/kube-client.cr/stargazers) - Kubernetes API Client
 * [mixpanel-crystal](https://github.com/petoem/mixpanel-crystal) [![GitHub stars](https://img.shields.io/github/stars/petoem/mixpanel-crystal?style=flat)](https://github.com/petoem/mixpanel-crystal/stargazers) - A library for sending events to Mixpanel
 * [mollie.cr](https://github.com/wout/mollie.cr) [![GitHub stars](https://img.shields.io/github/stars/wout/mollie.cr?style=flat)](https://github.com/wout/mollie.cr/stargazers) - [Mollie](https://www.mollie.com/en/) Payments API wrapper (Creditcard, PayPal, Apple Pay, Sofort, Klarna, ...)
 * [office365](https://github.com/PlaceOS/office365) [![GitHub stars](https://img.shields.io/github/stars/PlaceOS/office365?style=flat)](https://github.com/PlaceOS/office365/stargazers) - Microsoft Graph API wrapper
 * [pinboard.cr](https://github.com/oz/pinboard.cr) [![GitHub stars](https://img.shields.io/github/stars/oz/pinboard.cr?style=flat)](https://github.com/oz/pinboard.cr/stargazers) - [Pinboard](https://pinboard.in) API
 * [raven.cr](https://github.com/sija/raven.cr) [![GitHub stars](https://img.shields.io/github/stars/sija/raven.cr?style=flat)](https://github.com/sija/raven.cr/stargazers) - Raven is a client for [Sentry](https://github.com/getsentry/sentry) [![GitHub stars](https://img.shields.io/github/stars/getsentry/sentry?style=flat)](https://github.com/getsentry/sentry/stargazers)
 * [stripe.cr](https://github.com/confact/stripe.cr) [![GitHub stars](https://img.shields.io/github/stars/confact/stripe.cr?style=flat)](https://github.com/confact/stripe.cr/stargazers) - Stripe api wrapper
 * [tmdb.cr](https://github.com/mmacia/tmdb.cr) [![GitHub stars](https://img.shields.io/github/stars/mmacia/tmdb.cr?style=flat)](https://github.com/mmacia/tmdb.cr/stargazers) - The Movie DB (TMDb) api wrapper
 * [twitter-crystal](https://github.com/sferik/twitter-crystal) [![GitHub stars](https://img.shields.io/github/stars/sferik/twitter-crystal?style=flat)](https://github.com/sferik/twitter-crystal/stargazers) - A library to access the Twitter API
 * [web_finger](https://github.com/toddsundsted/web_finger) [![GitHub stars](https://img.shields.io/github/stars/toddsundsted/web_finger?style=flat)](https://github.com/toddsundsted/web_finger/stargazers) - A WebFinger (https://tools.ietf.org/html/rfc7033) client
 * [ynab.cr](https://github.com/jaredsmithse/ynab.cr) [![GitHub stars](https://img.shields.io/github/stars/jaredsmithse/ynab.cr?style=flat)](https://github.com/jaredsmithse/ynab.cr/stargazers) - A library to interact with your YNAB data

## Validation
 * [accord](https://github.com/neovintage/accord) [![GitHub stars](https://img.shields.io/github/stars/neovintage/accord?style=flat)](https://github.com/neovintage/accord/stargazers) - Shareable validation library for Crystal Objects
 * [Athena Validator](https://github.com/athena-framework/validator) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/validator?style=flat)](https://github.com/athena-framework/validator/stargazers) - Robust & flexible validation framework
 * [validations](https://github.com/vladfaust/validations.cr) [![GitHub stars](https://img.shields.io/github/stars/vladfaust/validations.cr?style=flat)](https://github.com/vladfaust/validations.cr/stargazers) - Validations mixin
 * [validator](https://github.com/Nicolab/crystal-validator) [![GitHub stars](https://img.shields.io/github/stars/Nicolab/crystal-validator?style=flat)](https://github.com/Nicolab/crystal-validator/stargazers) - Data check and validation

## Web Frameworks
 * [amber](https://github.com/amberframework/amber) [![GitHub stars](https://img.shields.io/github/stars/amberframework/amber?style=flat)](https://github.com/amberframework/amber/stargazers) - Open source efficient and cohesive web application framework
 * [Athena](https://github.com/athena-framework/athena) [![GitHub stars](https://img.shields.io/github/stars/athena-framework/athena?style=flat)](https://github.com/athena-framework/athena/stargazers) - A web framework comprised of reusable, independent components
 * [grip](https://github.com/grip-framework/grip) [![GitHub stars](https://img.shields.io/github/stars/grip-framework/grip?style=flat)](https://github.com/grip-framework/grip/stargazers) - The microframework for writing powerful web applications
 * [kemal](https://github.com/kemalcr/kemal) [![GitHub stars](https://img.shields.io/github/stars/kemalcr/kemal?style=flat)](https://github.com/kemalcr/kemal/stargazers) - Lightning Fast, Super Simple web framework. Inspired by Sinatra
 * [lucky](https://github.com/luckyframework/lucky) [![GitHub stars](https://img.shields.io/github/stars/luckyframework/lucky?style=flat)](https://github.com/luckyframework/lucky/stargazers) - Catch bugs early, forget about most performance issues, and spend more time on code instead of debugging and writing tests
 * [marten](https://github.com/martenframework/marten) [![GitHub stars](https://img.shields.io/github/stars/martenframework/marten?style=flat)](https://github.com/martenframework/marten/stargazers) - A web framework that makes building web applications easy, productive, and fun
 * [runcobo](https://github.com/runcobo/runcobo) [![GitHub stars](https://img.shields.io/github/stars/runcobo/runcobo?style=flat)](https://github.com/runcobo/runcobo/stargazers) - An api framework with simple, intuitive and consistent DSL, using jbuilder to render json
 * [Shivneri](https://github.com/ujjwalguptaofficial/shivneri) [![GitHub stars](https://img.shields.io/github/stars/ujjwalguptaofficial/shivneri?style=flat)](https://github.com/ujjwalguptaofficial/shivneri/stargazers) - Component based MVC web framework for crystal targeting good code structures, modularity & performance
 * [spider-gazelle](https://github.com/spider-gazelle/spider-gazelle) [![GitHub stars](https://img.shields.io/github/stars/spider-gazelle/spider-gazelle?style=flat)](https://github.com/spider-gazelle/spider-gazelle/stargazers) - A Rails esque web framework with a focus on speed and extensibility

# Community
 * [Crystal Forum](https://forum.crystal-lang.org/)
 * [Crystal newsletter](https://crystal-lang.org/#newsletter)
 * [Gitter](https://gitter.im/crystal-lang/crystal)
 * [IRC](ircs://irc.libera.chat:6697#crystal-lang) - #crystal-lang on Libera
 * [Reddit](https://www.reddit.com/r/crystal_programming/)
 * [Stackoverflow](https://stackoverflow.com/tags/crystal-lang/info)

## Unofficial
 * [Crystal Programming Discord Server](https://discord.gg/YS7YvQy) - Unofficial Discord server dedicated to the Crystal Programming Language
 * [Portuguese-speaking Telegram Group](https://t.me/crystalbrasil) - Bem vindos ao Crystal Brasil!
 * [Russian-speaking Telegram Group](https://t.me/crystal_ru) - Добро пожаловать, товарищ!

# Resources
 * [Crystal for Rubyists](http://www.crystalforrubyists.com/) - Free book to bootstrap your Crystal journey
 * [Crystal Shards for Ruby Gems](https://github.com/crystal-lang/crystal/wiki/Crystal-Shards-for-Ruby-Gems) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang/crystal/wiki/Crystal-Shards-for-Ruby-Gems?style=flat)](https://github.com/crystal-lang/crystal/wiki/Crystal-Shards-for-Ruby-Gems/stargazers) - A list of Ruby Gems and their Crystal Shards equivalents
 * [crystal-koans](https://github.com/ilmanzo/crystal-koans) [![GitHub stars](https://img.shields.io/github/stars/ilmanzo/crystal-koans?style=flat)](https://github.com/ilmanzo/crystal-koans/stargazers) - Learn Crystal by writing unit tests
 * [crystal-lang.org](https://crystal-lang.org) - Official language site
 * [devdocs.io](https://devdocs.io/crystal/) - API Documentation Browser with Crystal support
 * [Learn X in Y minutes](https://learnxinyminutes.com/docs/crystal/) - Quick tutorial on Crystal
 * [Programming Crystal](https://pragprog.com/book/crystal/programming-crystal) - PragProg book to start your Crystal journey
 * [Usability of Programming Languages](https://gergelyk.github.io/prog-lang-usability/) - Comparison of Python, Rust, Crystal

## Official Documentation Translations
 * [br.crystal-lang.org](http://br.crystal-lang.org/) - Brazilian
 * [ja.crystal-lang.org](http://ja.crystal-lang.org/) - Japanese
 * [kr.crystal-lang.org](https://kr.crystal-lang.org/) - Korean
 * [ru.crystal-lang.org](http://ru.crystal-lang.org/) - Russian
 * [tw.crystal-lang.org](http://tw.crystal-lang.org/) - Chinese Traditional

# Services and Apps
 * [carc.in](https://carc.in/) - A web service that runs your code and displays the result
 * [Crank](https://github.com/arktisklada/crank) [![GitHub stars](https://img.shields.io/github/stars/arktisklada/crank?style=flat)](https://github.com/arktisklada/crank/stargazers) - A Procfile-based application manager (like Foreman)
 * [cry](https://github.com/elorest/cry) [![GitHub stars](https://img.shields.io/github/stars/elorest/cry?style=flat)](https://github.com/elorest/cry/stargazers) - Ability to execute crystal code in a fashion similar to Ruby's pry edit
 * [DeBot](https://github.com/jhass/DeBot) [![GitHub stars](https://img.shields.io/github/stars/jhass/DeBot?style=flat)](https://github.com/jhass/DeBot/stargazers) - IRC bot written in Crystal
 * [icr](https://github.com/crystal-community/icr) [![GitHub stars](https://img.shields.io/github/stars/crystal-community/icr?style=flat)](https://github.com/crystal-community/icr/stargazers) - Interactive console for Crystal (like IRB for Ruby)
 * [Invidious](https://github.com/iv-org/invidious) [![GitHub stars](https://img.shields.io/github/stars/iv-org/invidious?style=flat)](https://github.com/iv-org/invidious/stargazers) - Invidious is an alternative front-end to YouTube
 * [mpngin](https://github.com/thewalkingtoast/mpngin) [![GitHub stars](https://img.shields.io/github/stars/thewalkingtoast/mpngin?style=flat)](https://github.com/thewalkingtoast/mpngin/stargazers) - A URL shortener with simple stats
 * [procodile](https://github.com/crystal-china/procodile) [![GitHub stars](https://img.shields.io/github/stars/crystal-china/procodile?style=flat)](https://github.com/crystal-china/procodile/stargazers) - Run processes in the background (and foreground) on Mac & Linux from a Procfile (for production and/or development environments)
 * [quicktype](https://quicktype.io/) - Generate models and serializers from JSON, JSON Schema, GraphQL, and TypeScript
 * [shards.info](http://shards.info/) - Web service that lists all repositories on GitHub that have Crystal code in them. The sources are available on [GitHub](https://github.com/mamantoha/shards-info) [![GitHub stars](https://img.shields.io/github/stars/mamantoha/shards-info?style=flat)](https://github.com/mamantoha/shards-info/stargazers)

# Tools
 * [ast_helper](https://github.com/bcardiff/crystal-ast-helper) [![GitHub stars](https://img.shields.io/github/stars/bcardiff/crystal-ast-helper?style=flat)](https://github.com/bcardiff/crystal-ast-helper/stargazers) - Helper tool to debug parser and formatter
 * [crystal-base](https://github.com/ruivieira/crystal-base) [![GitHub stars](https://img.shields.io/github/stars/ruivieira/crystal-base?style=flat)](https://github.com/ruivieira/crystal-base/stargazers) - CentOS base docker image for Crystal development
 * [crystal-dash-docset](https://github.com/Sija/crystal-dash-docset) [![GitHub stars](https://img.shields.io/github/stars/Sija/crystal-dash-docset?style=flat)](https://github.com/Sija/crystal-dash-docset/stargazers) - [Dash](https://kapeli.com/dash) docset generator
 * [port_ruby_to_crystal](https://github.com/crystal-china/port_ruby_to_crystal) [![GitHub stars](https://img.shields.io/github/stars/crystal-china/port_ruby_to_crystal?style=flat)](https://github.com/crystal-china/port_ruby_to_crystal/stargazers) - A regex replace ruby script for port ruby code to crystal easier, reduce friction
 * [public_suffix](https://github.com/toddsundsted/public_suffix) [![GitHub stars](https://img.shields.io/github/stars/toddsundsted/public_suffix?style=flat)](https://github.com/toddsundsted/public_suffix/stargazers) - A small library designed to make the Public Suffix List (https://publicsuffix.org/) easier to use

## DevOps
 * [ansible-crystal](https://github.com/CorbanR/ansible-crystal) [![GitHub stars](https://img.shields.io/github/stars/CorbanR/ansible-crystal?style=flat)](https://github.com/CorbanR/ansible-crystal/stargazers) - Ansible playbook for installing crystal
 * [DPPM](https://github.com/DFabric/dppm) [![GitHub stars](https://img.shields.io/github/stars/DFabric/dppm?style=flat)](https://github.com/DFabric/dppm/stargazers) - An easy, universal way to install and manage applications as packages (mostly Linux)

## Editor Plugins
 * Acme:
   * [acmecrystal](https://github.com/ilanpillemer/acmecrystal) [![GitHub stars](https://img.shields.io/github/stars/ilanpillemer/acmecrystal?style=flat)](https://github.com/ilanpillemer/acmecrystal/stargazers) - Reformats crystal code in acme
 * Atom
   * [crystal-tools](https://atom.io/packages/crystal-tools) - Enables built in tools in Crystal compiler
   * [language-crystal-actual](https://atom.io/packages/language-crystal-actual) - Crystal language support in Atom
 * Emacs
   * [crystal-mode](https://melpa.org/#/crystal-mode) - Crystal language support for Emacs ([crystal-lang-tools/emacs-crystal-mode](https://github.com/crystal-lang-tools/emacs-crystal-mode) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang-tools/emacs-crystal-mode?style=flat)](https://github.com/crystal-lang-tools/emacs-crystal-mode/stargazers))
 * Geany
   * [geany-crystal](https://github.com/crystal-lang-tools/geany-crystal) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang-tools/geany-crystal?style=flat)](https://github.com/crystal-lang-tools/geany-crystal/stargazers) - Crystal support for the [Geany editor](https://www.geany.org/)
 * IntelliJ IDEA
   * [intellij-crystal-lang](https://github.com/asedunov/intellij-crystal-lang) [![GitHub stars](https://img.shields.io/github/stars/asedunov/intellij-crystal-lang?style=flat)](https://github.com/asedunov/intellij-crystal-lang/stargazers) - Crystal support for the JetBrains IDEs
 * Lite-XL
   * [lite-plugin-crystal](https://github.com/Tamnac/lite-plugin-crystal) [![GitHub stars](https://img.shields.io/github/stars/Tamnac/lite-plugin-crystal?style=flat)](https://github.com/Tamnac/lite-plugin-crystal/stargazers) - Crystal support for the [Lite-XL](https://lite-xl.com/en/) editor
 * Spacemacs
   * [crystal-spacemacs-layer](https://github.com/juanedi/crystal-spacemacs-layer) [![GitHub stars](https://img.shields.io/github/stars/juanedi/crystal-spacemacs-layer?style=flat)](https://github.com/juanedi/crystal-spacemacs-layer/stargazers) - Spacemacs contribution layer for Crystal
 * Sublime
   * [sublime-crystal](https://github.com/crystal-lang-tools/sublime-crystal) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang-tools/sublime-crystal?style=flat)](https://github.com/crystal-lang-tools/sublime-crystal/stargazers) - Crystal syntax highlighting for sublime Text
 * TextMate
   * [Crystal.tmbundle](https://github.com/crystal-lang-tools/Crystal.tmbundle) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang-tools/Crystal.tmbundle?style=flat)](https://github.com/crystal-lang-tools/Crystal.tmbundle/stargazers) - Crystal syntax highlighting, compile, format command, snippets
 * Vim
   * [vim-crystal](https://github.com/vim-crystal/vim-crystal) [![GitHub stars](https://img.shields.io/github/stars/vim-crystal/vim-crystal?style=flat)](https://github.com/vim-crystal/vim-crystal/stargazers) - Vim filetype support for Crystal
   * [vim-slang](https://github.com/elorest/vim-slang) [![GitHub stars](https://img.shields.io/github/stars/elorest/vim-slang?style=flat)](https://github.com/elorest/vim-slang/stargazers) - Vim filetype support for Slang Templating Engine
 * Visual Studio Code
   * [vscode-crystal-lang](https://github.com/crystal-lang-tools/vscode-crystal-lang) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang-tools/vscode-crystal-lang?style=flat)](https://github.com/crystal-lang-tools/vscode-crystal-lang/stargazers) - Formatter, linter and syntax highlighting for `cr` and `ecr` files

## LSP Language Server Protocol Implementations
 * [crystalline](https://github.com/elbywan/crystalline) [![GitHub stars](https://img.shields.io/github/stars/elbywan/crystalline?style=flat)](https://github.com/elbywan/crystalline/stargazers) - Crystalline is an implementation of the Language Server Protocol written in and for the Crystal Language
 * [scry](https://github.com/crystal-lang-tools/scry) [![GitHub stars](https://img.shields.io/github/stars/crystal-lang-tools/scry?style=flat)](https://github.com/crystal-lang-tools/scry/stargazers) - Code analysis server for Crystal implementing the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)

## Shell plugins
 * [crun](https://github.com/Val/crun) [![GitHub stars](https://img.shields.io/github/stars/Val/crun?style=flat)](https://github.com/Val/crun/stargazers) - Crystal Run : shebang wrapper for Crystal
 * [crystal-zsh](https://github.com/veelenga/crystal-zsh) [![GitHub stars](https://img.shields.io/github/stars/veelenga/crystal-zsh?style=flat)](https://github.com/veelenga/crystal-zsh/stargazers) - .oh-my-zsh plugin
