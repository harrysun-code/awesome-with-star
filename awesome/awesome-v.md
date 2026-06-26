# V

[![GitHub stars](https://img.shields.io/github/stars/vlang/awesome-v?style=flat)](https://github.com/vlang/awesome-v/stargazers)

<!--lint disable no-dead-urls-->

<p align="center"><img src="media/awesome-v-logo.svg" width="400"/></p>

# Awesome V [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome V frameworks, libraries, software and resources.

[V](https://vlang.io/) is a simple, fast, safe, compiled language for developing maintainable software.

## Contents

- [Applications](#applications)
	- [Build Systems](#build-systems)
	- [Command-line](#command-line)
	- [Editors](#editors)
	- [Games](#games)
	- [Graphics](#graphics)
	- [Interpreters/Compilers](#interpreterscompilers)
	- [Operating systems/Kernels](#operating-systemskernels)
	- [Package managers](#package-managers)
	- [Project management](#project-management)
	- [Serialization](#serialization)
	- [Utilities](#utilities)
	- [Web](#web)
- [Libraries](#libraries)
	- [Audio](#audio)
	- [Automation](#automation)
	- [Command line interface (CLI) / Terminal / Shell](#command-line-interface-cli--terminal--shell)
	- [Database clients](#database-clients)
	- [Discord](#discord)
	- [Eventing](#eventing)
	- [File handling](#file-handling)
	- [Game development](#game-development)
	- [Graphics](#graphics-1)
	- [Interoperability](#interoperability)
	- [IRC](#irc)
	- [Networking](#networking)
	- [Operating system](#operating-system)
	- [Scientific computing](#scientific-computing)
	- [Serial Communications](#serial-communications)
	- [Telecommunications](#telecommunications)
	- [Telegram](#telegram)
	- [Text processing](#text-processing)
	- [User Interface toolkits](#user-interface-toolkits)
	- [Utility](#utility)
	- [Web](#web-1)
- [Other](#other)
	- [Articles](#articles)
	- [Books](#books)
	- [Communities](#communities)
	- [Editor plugins](#editor-plugins)
	- [Forums](#forums)
	- [GitHub Actions](#github-actions)
	- [GitHub templates](#github-templates)
	- [IDEs with V](#ides-with-v)
	- [Online IDEs with V](#online-ides-with-v)
	- [Operating Systems & OS Development Examples](#operating-systems--os-development-examples)
	- [Patterns](#patterns)
	- [Programming contests](#programming-contests)
	- [Syntax highlighting](#syntax-highlighting)
	- [Tutorials](#tutorials)
	- [Videos](#videos)

## Applications

### Build Systems

- [clockwork](https://github.com/emmathemartian/clockwork) [![GitHub stars](https://img.shields.io/github/stars/emmathemartian/clockwork?style=flat)](https://github.com/emmathemartian/clockwork/stargazers) - A language-agnostic build tool wrote in V.
- [vab](https://github.com/vlang/vab) [![GitHub stars](https://img.shields.io/github/stars/vlang/vab?style=flat)](https://github.com/vlang/vab/stargazers) - The official V tool to build and package applications for Android.
- [vab-sdl](https://github.com/larpon/vab-sdl) [![GitHub stars](https://img.shields.io/github/stars/larpon/vab-sdl?style=flat)](https://github.com/larpon/vab-sdl/stargazers) - Standalone and extra command for `vab` to build and package
SDL2 and SDL3 based applications importing `vlang/sdl`.

### Command-line

- [amdim](https://github.com/tailsmails/amdim) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/amdim?style=flat)](https://github.com/tailsmails/amdim/stargazers) - Make your screen dimmer than 0%.
- [crepl](https://github.com/l1mey112/crepl) [![GitHub stars](https://img.shields.io/github/stars/l1mey112/crepl?style=flat)](https://github.com/l1mey112/crepl/stargazers) - Compile and execute C code on the fly as you type it.
- [dnshammer](https://github.com/tailsmails/dnshammer) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/dnshammer?style=flat)](https://github.com/tailsmails/dnshammer/stargazers) - A covert communication channel that encodes data into DNS cache timing differences.
- [envelop](https://github.com/tailsmails/envelop) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/envelop?style=flat)](https://github.com/tailsmails/envelop/stargazers) - Generates background HTTP HEAD requests to obfuscate real web traffic.
- [fastgit](https://github.com/tailsmails/fastgit) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/fastgit?style=flat)](https://github.com/tailsmails/fastgit/stargazers) - A command-line tool written in V, designed to automate and simplify uploading, syncing, and modifying GitHub repositories.
- [fdup](https://github.com/gechandesu/fdup) [![GitHub stars](https://img.shields.io/github/stars/gechandesu/fdup?style=flat)](https://github.com/gechandesu/fdup/stargazers) - Find and remove duplicate files.
- [github-releases](https://github.com/Dracks/repo-download-asset) [![GitHub stars](https://img.shields.io/github/stars/Dracks/repo-download-asset?style=flat)](https://github.com/Dracks/repo-download-asset/stargazers) - Cli tool to keep track of applications released as GitHub Release (or assets in workflow) and download them.
- [HN-top](https://github.com/BafS/hn-top) [![GitHub stars](https://img.shields.io/github/stars/BafS/hn-top?style=flat)](https://github.com/BafS/hn-top/stargazers) - A simple command to list most recent news from hacker-news.
- [httest](https://github.com/gechandesu/httest) [![GitHub stars](https://img.shields.io/github/stars/gechandesu/httest?style=flat)](https://github.com/gechandesu/httest/stargazers) - A CGI-enabled HTTP test server for mocking backends, inspecting requests and simulating latency and failures.
- [klonol](https://github.com/hungrybluedev/klonol) [![GitHub stars](https://img.shields.io/github/stars/hungrybluedev/klonol?style=flat)](https://github.com/hungrybluedev/klonol/stargazers) - CLI tool to help you "clone all" Git repositories belonging to you. Works with GitHub and Gitea.
- [lagger](https://github.com/tailsmails/lagger) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/lagger?style=flat)](https://github.com/tailsmails/lagger/stargazers) - A dynamic network latency and packet loss simulation proxy designed to emulate real-world network degradation at the application layer.
- [lsv](https://github.com/mike-ward/lsv) [![GitHub stars](https://img.shields.io/github/stars/mike-ward/lsv?style=flat)](https://github.com/mike-ward/lsv/stargazers) - `ls` file lister in the spirit of exa, eza, lsd, pls, natls, ls-go and others.
- [minimax-v](https://github.com/whiter001/minimax-v) [![GitHub stars](https://img.shields.io/github/stars/whiter001/minimax-v?style=flat)](https://github.com/whiter001/minimax-v/stargazers) - Local AI Agent runtime implemented in the V language.
- [mushroomtek](https://github.com/tailsmails/mushroomtek) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/mushroomtek?style=flat)](https://github.com/tailsmails/mushroomtek/stargazers) - Don't worry about the grid, you are just a radius (Anti-IMSI catcher/Anti-Triangulation...).
- [musicc](https://github.com/tailsmails/musicc) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/musicc?style=flat)](https://github.com/tailsmails/musicc/stargazers) - A lightweight, high-performance command-line music compiler.
- [netprint](https://github.com/tailsmails/netprint) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/netprint?style=flat)](https://github.com/tailsmails/netprint/stargazers) - A low-level network telemetry and anomaly detection tool designed to identify environmental changes and traffic interception.
- [newfolder](https://github.com/tailsmails/newfolder) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/newfolder?style=flat)](https://github.com/tailsmails/newfolder/stargazers) - A lightweight, high-performance command-line steganography, file obfuscation, and secure metadata-destruction workstation written in V.
- [pfjson](https://github.com/fleximus/pfjson) [![GitHub stars](https://img.shields.io/github/stars/fleximus/pfjson?style=flat)](https://github.com/fleximus/pfjson/stargazers) - A CLI tool to convert OpenBSD Packet Filter configuration files (`pf.conf`) to JSON and vice versa.
- [PhoneSnatchProof](https://github.com/tailsmails/PhoneSnatchProof) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/PhoneSnatchProof?style=flat)](https://github.com/tailsmails/PhoneSnatchProof/stargazers) - An FS that encrypts your app data and keeps them on RAM (with a backup).
- [portctl](https://github.com/apoprotsky/portctl) [![GitHub stars](https://img.shields.io/github/stars/apoprotsky/portctl?style=flat)](https://github.com/apoprotsky/portctl/stargazers) - CLI tool to manage Docker Swarm resources using Portainer API.
- [runner](https://github.com/Naheel-Azawy/runner) [![GitHub stars](https://img.shields.io/github/stars/Naheel-Azawy/runner?style=flat)](https://github.com/Naheel-Azawy/runner/stargazers) - A tool that automates running/compiling code written in various programming languages.
- [salty](https://github.com/tailsmails/salty) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/salty?style=flat)](https://github.com/tailsmails/salty/stargazers) - A lightweight command-line utility written in V for secure data encryption, deep compression, and steganographic-like format obfuscation.
- [sockslender](https://github.com/tailsmails/sockslender) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/sockslender?style=flat)](https://github.com/tailsmails/sockslender/stargazers) - A lightweight, blazing-fast SOCKS5 proxy failover tool written in V.
- [stripshot](https://github.com/tailsmails/stripshot) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/stripshot?style=flat)](https://github.com/tailsmails/stripshot/stargazers) - Strips device/OS fingerprints from screenshots.
- [symlinker](https://github.com/serkonda7/symlinker) [![GitHub stars](https://img.shields.io/github/stars/serkonda7/symlinker?style=flat)](https://github.com/serkonda7/symlinker/stargazers) - A small Linux tool to manage symlinks.
- [timingless](https://github.com/tailsmails/timingless) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/timingless?style=flat)](https://github.com/tailsmails/timingless/stargazers) - A SOCKS5 proxy that sits between your applications and Tor, enforcing constant bandwidth to defeat traffic timing analysis.
- [v-terminal-apps](https://github.com/cogrow4/V-Terminal-Apps) [![GitHub stars](https://img.shields.io/github/stars/cogrow4/V-Terminal-Apps?style=flat)](https://github.com/cogrow4/V-Terminal-Apps/stargazers) - A collection of high-quality terminal applications written in V, including job planner, calculator, notes, file browser, quiz game, budget tracker, P2P chat (WIP), and Pomodoro timer.
- [v_llama_cpp](https://github.com/sakana-ctf/v_llama_cpp) [![GitHub stars](https://img.shields.io/github/stars/sakana-ctf/v_llama_cpp?style=flat)](https://github.com/sakana-ctf/v_llama_cpp/stargazers) - Lightweight V wrapper for Llama.cpp, enabling efficient LLM execution.
- [vast](https://github.com/lydiandy/vast) [![GitHub stars](https://img.shields.io/github/stars/lydiandy/vast?style=flat)](https://github.com/lydiandy/vast/stargazers) - A simple tool for vlang, generate v source file to AST json file.
- [vcli](https://github.com/changhz/vcli) [![GitHub stars](https://img.shields.io/github/stars/changhz/vcli?style=flat)](https://github.com/changhz/vcli/stargazers) - A CLI tool to generate folder structure according to the [guideline](https://blog.vlang.io/the-complete-beginners-guide-to-cli-apps-in-v/)
- [verve](https://github.com/MohammadMD1383/verve) [![GitHub stars](https://img.shields.io/github/stars/MohammadMD1383/verve?style=flat)](https://github.com/MohammadMD1383/verve/stargazers) - Simple and fast static file server.
- [vfc](https://github.com/Ict00/vfc) [![GitHub stars](https://img.shields.io/github/stars/Ict00/vfc?style=flat)](https://github.com/Ict00/vfc/stargazers) - A simple TUI file manager, made with V.
- [vfetch](https://github.com/carlosqsilva/vfetch) [![GitHub stars](https://img.shields.io/github/stars/carlosqsilva/vfetch?style=flat)](https://github.com/carlosqsilva/vfetch/stargazers) - A macOS system information fetch written in V.
- [vgoogle](https://github.com/changhz/vgoogle) [![GitHub stars](https://img.shields.io/github/stars/changhz/vgoogle?style=flat)](https://github.com/changhz/vgoogle/stargazers) - Make google search on the terminal.
- [vin](https://github.com/DeoDorqnt387/vin) [![GitHub stars](https://img.shields.io/github/stars/DeoDorqnt387/vin?style=flat)](https://github.com/DeoDorqnt387/vin/stargazers) - A Basic Command Line Interface for V.
- [vindex](https://github.com/wenxuanjun/vindex) [![GitHub stars](https://img.shields.io/github/stars/wenxuanjun/vindex?style=flat)](https://github.com/wenxuanjun/vindex/stargazers) - A simple file list server generating json strings, compatible with nginx's autoindex module.
- [vinit](https://github.com/pranavbaburaj/vinit) [![GitHub stars](https://img.shields.io/github/stars/pranavbaburaj/vinit?style=flat)](https://github.com/pranavbaburaj/vinit/stargazers) - A tool to generate v projects.
- [vLogQL](https://github.com/lmangani/vLogQL) [![GitHub stars](https://img.shields.io/github/stars/lmangani/vLogQL?style=flat)](https://github.com/lmangani/vLogQL/stargazers) - A tiny command-line utility to query LogQL APIs.
- [vlsh](https://github.com/vlshcc/vlsh) [![GitHub stars](https://img.shields.io/github/stars/vlshcc/vlsh?style=flat)](https://github.com/vlshcc/vlsh/stargazers) - *nix Shell written in V (pipes, plugins, mux mode, etc).
- [vqrcode](https://github.com/carlosqsilva/vqrcode) [![GitHub stars](https://img.shields.io/github/stars/carlosqsilva/vqrcode?style=flat)](https://github.com/carlosqsilva/vqrcode/stargazers) - CLI for creating QR Codes.
- [vspect](https://github.com/zakuro9715/vspect) [![GitHub stars](https://img.shields.io/github/stars/zakuro9715/vspect?style=flat)](https://github.com/zakuro9715/vspect/stargazers) - A tool to inspect vlang source file. ( Archived )
- [vsqlite](https://github.com/quaesitor-scientiam/vsqlite) [![GitHub stars](https://img.shields.io/github/stars/quaesitor-scientiam/vsqlite?style=flat)](https://github.com/quaesitor-scientiam/vsqlite/stargazers) - SQLite CLI and module replacement written in pure V.
- [vzcc](https://github.com/malisipi/vzcc) [![GitHub stars](https://img.shields.io/github/stars/malisipi/vzcc?style=flat)](https://github.com/malisipi/vzcc/stargazers) - A CLI cross-compiling tool based on Zig CC for V.
- [zilch](https://github.com/mike-ward/zilch) [![GitHub stars](https://img.shields.io/github/stars/mike-ward/zilch?style=flat)](https://github.com/mike-ward/zilch/stargazers) - An entertaining and amusing simulation of an installer.

### Editors

- [lilly](https://github.com/tauraamui/lilly) [![GitHub stars](https://img.shields.io/github/stars/tauraamui/lilly?style=flat)](https://github.com/tauraamui/lilly/stargazers) - TUI editor and VIM/Neovim alternative.
- [polygon-editor](https://github.com/ArtemkaKun/polygon-editor) [![GitHub stars](https://img.shields.io/github/stars/ArtemkaKun/polygon-editor?style=flat)](https://github.com/ArtemkaKun/polygon-editor/stargazers) - A tool to create and edit 2D polygons with sprite lookup, created in V.
- [text_editor](https://github.com/vlang/v/blob/master/examples/term.ui/text_editor.v) [![GitHub stars](https://img.shields.io/github/stars/vlang/v/blob/master/examples/term.ui/text_editor.v?style=flat)](https://github.com/vlang/v/blob/master/examples/term.ui/text_editor.v/stargazers) - Small text editor from the official V examples.
- [ved](https://github.com/vlang/ved) [![GitHub stars](https://img.shields.io/github/stars/vlang/ved?style=flat)](https://github.com/vlang/ved/stargazers) - 1 MB text editor written in V with hardware accelerated text rendering. Compiles in <1s.
- [vee](https://github.com/Larpon/vee) [![GitHub stars](https://img.shields.io/github/stars/Larpon/vee?style=flat)](https://github.com/Larpon/vee/stargazers) - V Editor Engine. A V module providing the guts of a text editor. Comes with a [TUI editor example](https://github.com/Larpon/vee/blob/master/examples/tuieditor/) [![GitHub stars](https://img.shields.io/github/stars/Larpon/vee/blob/master/examples/tuieditor/?style=flat)](https://github.com/Larpon/vee/blob/master/examples/tuieditor//stargazers).
- [volt](https://github.com/Volt-Editor-Team/volt) [![GitHub stars](https://img.shields.io/github/stars/Volt-Editor-Team/volt?style=flat)](https://github.com/Volt-Editor-Team/volt/stargazers) - Aims to be a fully featured text editor written entirely in Vlang.
- [vPDF](https://github.com/vlang/pdf) [![GitHub stars](https://img.shields.io/github/stars/vlang/pdf?style=flat)](https://github.com/vlang/pdf/stargazers) - A module to simplify PDF file creation using the V programming language.
- [vro](https://github.com/undivisible/vro) [![GitHub stars](https://img.shields.io/github/stars/undivisible/vro?style=flat)](https://github.com/undivisible/vro/stargazers) - <0.5MB micro-inspired basic text editor. Compatible with Micro's YAML syntax highlighting.

### Games

- [2048](https://github.com/wenxuanjun/2048) [![GitHub stars](https://img.shields.io/github/stars/wenxuanjun/2048?style=flat)](https://github.com/wenxuanjun/2048/stargazers) - A 2048 game with several types of traditional AI integrated.
- [Boundstone](https://github.com/organization/boundstone) [![GitHub stars](https://img.shields.io/github/stars/organization/boundstone?style=flat)](https://github.com/organization/boundstone/stargazers) - High Performance / Fast Compilation / Lightweight Minecraft: Bedrock Edition Server.
- [flappylearning-v](https://github.com/vlang/v/tree/master/examples/flappylearning) [![GitHub stars](https://img.shields.io/github/stars/vlang/v/tree/master/examples/flappylearning?style=flat)](https://github.com/vlang/v/tree/master/examples/flappylearning/stargazers) - A simple flappy learning demo in v.
- [Kurarin](https://github.com/FireRedz/kurarin) [![GitHub stars](https://img.shields.io/github/stars/FireRedz/kurarin?style=flat)](https://github.com/FireRedz/kurarin/stargazers) - osu! beatmap visualizer made in V. [Example video](https://p153.p0.n0.cdn.getcloudapp.com/items/6quvQjb5/ce3ea737-eb29-4b8c-a5f3-65a804a2f56f.mp4).
- [minesweeper](https://github.com/ali-furkan/minesweeper-v) [![GitHub stars](https://img.shields.io/github/stars/ali-furkan/minesweeper-v?style=flat)](https://github.com/ali-furkan/minesweeper-v/stargazers) - A simple Minesweeper game written in vlang.
- [Puzzle Vibes](https://github.com/Larpon/puzzle_vibes) [![GitHub stars](https://img.shields.io/github/stars/Larpon/puzzle_vibes?style=flat)](https://github.com/Larpon/puzzle_vibes/stargazers) - A jigsaw-like puzzle game written in V using `shy`.
- [vchess](https://github.com/hedgeg0d/vchess) [![GitHub stars](https://img.shields.io/github/stars/hedgeg0d/vchess?style=flat)](https://github.com/hedgeg0d/vchess/stargazers) - Chess game written in V programming language.
- [v-pong](https://github.com/thebigsmileXD/v-pong) [![GitHub stars](https://img.shields.io/github/stars/thebigsmileXD/v-pong?style=flat)](https://github.com/thebigsmileXD/v-pong/stargazers) - A classic paddle game brought back to life through the power of V.

### Graphics

- [mpv-v](https://github.com/xjunko/mpv-v) [![GitHub stars](https://img.shields.io/github/stars/xjunko/mpv-v?style=flat)](https://github.com/xjunko/mpv-v/stargazers) - World's Simplest Video Player.
- [vpaint](https://github.com/pisaiah/vpaint) [![GitHub stars](https://img.shields.io/github/stars/pisaiah/vpaint?style=flat)](https://github.com/pisaiah/vpaint/stargazers) - MS-Paint alternative written in V.
- [vRayTracer](https://github.com/ali-raheem/vraytracer) [![GitHub stars](https://img.shields.io/github/stars/ali-raheem/vraytracer?style=flat)](https://github.com/ali-raheem/vraytracer/stargazers) - A simple ray tracer written in V.

### Interpreters/Compilers

- [Aixt](https://github.com/fermarsan/aixt) [![GitHub stars](https://img.shields.io/github/stars/fermarsan/aixt?style=flat)](https://github.com/fermarsan/aixt/stargazers) - Programming framework for microcontrollers based on a V-based language and written in V. 
- [cotowali](https://github.com/cotowali/cotowali) [![GitHub stars](https://img.shields.io/github/stars/cotowali/cotowali?style=flat)](https://github.com/cotowali/cotowali/stargazers) - A statically typed scripting language that transpiles into POSIX sh.
- [monkey_v](https://github.com/Delta456/monkey_v) [![GitHub stars](https://img.shields.io/github/stars/Delta456/monkey_v?style=flat)](https://github.com/Delta456/monkey_v/stargazers) - Implementation of [Thorsten Ball's Monkey Language](https://interpreterbook.com/) in V.
- [papyrus-compiler](https://github.com/russo-2025/papyrus-compiler) [![GitHub stars](https://img.shields.io/github/stars/russo-2025/papyrus-compiler?style=flat)](https://github.com/russo-2025/papyrus-compiler/stargazers) - Open-source compiler for Bethesda's Papyrus scripting language (Skyrim SE/AE).
- [stas](https://github.com/l1mey112/stas/tree/0.1.0-v-compiler) [![GitHub stars](https://img.shields.io/github/stars/l1mey112/stas/tree/0.1.0-v-compiler?style=flat)](https://github.com/l1mey112/stas/tree/0.1.0-v-compiler/stargazers) - A stack based compiled programming language. The bootstrap compiler is written in V.
- [v](https://github.com/vlang/v) [![GitHub stars](https://img.shields.io/github/stars/vlang/v?style=flat)](https://github.com/vlang/v/stargazers) - The language V itself. Simple, fast, safe, compiled language for developing maintainable software.
- [vas](https://github.com/v420v/vas) [![GitHub stars](https://img.shields.io/github/stars/v420v/vas?style=flat)](https://github.com/v420v/vas/stargazers) - A simple x86-64 assembler written in V.
- [vbf](https://github.com/vpervenditti/vbf) [![GitHub stars](https://img.shields.io/github/stars/vpervenditti/vbf?style=flat)](https://github.com/vpervenditti/vbf/stargazers) - A brainfuck interpreter/compiler.
- [vfuck](https://github.com/ShayokhShorfuddin/VFuck) [![GitHub stars](https://img.shields.io/github/stars/ShayokhShorfuddin/VFuck?style=flat)](https://github.com/ShayokhShorfuddin/VFuck/stargazers) - A brainfuck interpreter written in V.
- [vcc](https://github.com/lemoncmd/vcc) [![GitHub stars](https://img.shields.io/github/stars/lemoncmd/vcc?style=flat)](https://github.com/lemoncmd/vcc/stargazers) - A C compiler written in V.
- [Vork](https://github.com/Itay2805/Vork) [![GitHub stars](https://img.shields.io/github/stars/Itay2805/Vork?style=flat)](https://github.com/Itay2805/Vork/stargazers) - Alternative V compiler/interpreter written in Python.

### Operating systems/Kernels

- [Vinix](https://github.com/vlang/vinix) [![GitHub stars](https://img.shields.io/github/stars/vlang/vinix?style=flat)](https://github.com/vlang/vinix/stargazers) - Small and simple OS in V. Runs bash.
- [V-Unikernel](https://github.com/vlang/unikernel) [![GitHub stars](https://img.shields.io/github/stars/vlang/unikernel?style=flat)](https://github.com/vlang/unikernel/stargazers) - A unikernel is a computer program statically linked with the operating system code on which it depends.

### Package managers

- [vpm](https://github.com/vlang/vpm) [![GitHub stars](https://img.shields.io/github/stars/vlang/vpm?style=flat)](https://github.com/vlang/vpm/stargazers) - The V language package management tool written in V.

### Project management

- [Lenra template](https://github.com/lenra-io/template-v) [![GitHub stars](https://img.shields.io/github/stars/lenra-io/template-v?style=flat)](https://github.com/lenra-io/template-v/stargazers) - The Lenra template to write V app for Lenra platform.
- [vset](https://github.com/mulh8377/vset) [![GitHub stars](https://img.shields.io/github/stars/mulh8377/vset?style=flat)](https://github.com/mulh8377/vset/stargazers) - A project setup and configuration tool for V projects.

### Serialization

- [ini-v](https://github.com/ldedev/ini-v) [![GitHub stars](https://img.shields.io/github/stars/ldedev/ini-v?style=flat)](https://github.com/ldedev/ini-v/stargazers) - Simple and practical module for manipulating ini/cfg file.
- [maple](https://github.com/emmathemartian/maple) [![GitHub stars](https://img.shields.io/github/stars/emmathemartian/maple?style=flat)](https://github.com/emmathemartian/maple/stargazers) - A very simple key-value config format wrote in V.
- [v-toxml](https://github.com/radare/v-toxml) [![GitHub stars](https://img.shields.io/github/stars/radare/v-toxml?style=flat)](https://github.com/radare/v-toxml/stargazers) - XML Serialization library for V.
- [vgura](https://github.com/gura-conf/vgura) [![GitHub stars](https://img.shields.io/github/stars/gura-conf/vgura?style=flat)](https://github.com/gura-conf/vgura/stargazers) - Official Gura parser for V.
- [vlang-yaml](https://github.com/jdonnerstag/vlang-yaml) [![GitHub stars](https://img.shields.io/github/stars/jdonnerstag/vlang-yaml?style=flat)](https://github.com/jdonnerstag/vlang-yaml/stargazers) - A V-native YAML reader, incl. YAML-to-JSON converter.
- [vproto](https://github.com/emily33901/vproto) [![GitHub stars](https://img.shields.io/github/stars/emily33901/vproto?style=flat)](https://github.com/emily33901/vproto/stargazers) - Protobuf compiler and runtime in V.

### Utilities

- [boj-server](https://github.com/hyperpolymath/boj-server) [![GitHub stars](https://img.shields.io/github/stars/hyperpolymath/boj-server?style=flat)](https://github.com/hyperpolymath/boj-server/stargazers) - Unified developer tool server using V for the network adapter layer. Exposes REST (port 7700), gRPC (7701), and GraphQL (7702) from a single V codebase. 18 capability cartridges loaded via Zig FFI with Idris2-verified interfaces.
- [emoji-mart-desktop](https://github.com/ttytm/emoji-mart-desktop) [![GitHub stars](https://img.shields.io/github/stars/ttytm/emoji-mart-desktop?style=flat)](https://github.com/ttytm/emoji-mart-desktop/stargazers) - An emoji picker created with V, webview and SvelteKit.
- [qptorrent](https://github.com/qptorrent/qptorrent) [![GitHub stars](https://img.shields.io/github/stars/qptorrent/qptorrent?style=flat)](https://github.com/qptorrent/qptorrent/stargazers) - A minimal GUI/CLI BitTorrent client written in V + vlang/gui.
- [raur](https://github.com/Matejsdevelopment/raur) [![GitHub stars](https://img.shields.io/github/stars/Matejsdevelopment/raur?style=flat)](https://github.com/Matejsdevelopment/raur/stargazers) - Simple Arch User Repository (AUR) helper coded in Vlang.
- [unix-emulators-win](https://github.com/Ddiidev/unix-emulators-win) [![GitHub stars](https://img.shields.io/github/stars/Ddiidev/unix-emulators-win?style=flat)](https://github.com/Ddiidev/unix-emulators-win/stargazers) - Collection of 16 UNIX utilities rewritten in V for Windows.
- [v-nodejs-addon](https://github.com/fanlia/v-nodejs-addon) [![GitHub stars](https://img.shields.io/github/stars/fanlia/v-nodejs-addon?style=flat)](https://github.com/fanlia/v-nodejs-addon/stargazers) - An demo of how to create a Node.js addon with V.

### Web

- [Gitly](https://github.com/vlang/gitly) [![GitHub stars](https://img.shields.io/github/stars/vlang/gitly?style=flat)](https://github.com/vlang/gitly/stargazers) - A light and fast SCM alternative to GitHub/GitLab written in V.
- [gitval](https://github.com/davlgd/gitval) [![GitHub stars](https://img.shields.io/github/stars/davlgd/gitval?style=flat)](https://github.com/davlgd/gitval/stargazers) - A static site generator for Git repositories, written in V.
- [Heroku Buildpack for V](https://github.com/zztkm/heroku-buildpack-v) [![GitHub stars](https://img.shields.io/github/stars/zztkm/heroku-buildpack-v?style=flat)](https://github.com/zztkm/heroku-buildpack-v/stargazers) - Deploy V apps on Heroku.
- [highlighter](https://codeberg.org/tamer/highlighter) - Inject syntax highlighting into HTML files at build time, or via the CLI tool.
- [Mantis](https://github.com/khalyomede/mantis) [![GitHub stars](https://img.shields.io/github/stars/khalyomede/mantis?style=flat)](https://github.com/khalyomede/mantis/stargazers) - A web framework written in V.
- [Mustela](https://github.com/filipos800/mustela) [![GitHub stars](https://img.shields.io/github/stars/filipos800/mustela?style=flat)](https://github.com/filipos800/mustela/stargazers) - Ultra-high-performance static site generator (SSG) engineered for speed (>9,000 pages/sec) and total data sovereignty.
- [rr-dl](https://github.com/dy-tea/rr-dl) [![GitHub stars](https://img.shields.io/github/stars/dy-tea/rr-dl?style=flat)](https://github.com/dy-tea/rr-dl/stargazers) - Royal-Road Novel downloader.
- [Tiniest Veb Server](https://github.com/davlgd/tVeb) [![GitHub stars](https://img.shields.io/github/stars/davlgd/tVeb?style=flat)](https://github.com/davlgd/tVeb/stargazers) - A < 1MB static hosting web server written in V, based on `veb`. 🍃
- [v-admin-skeleton](https://github.com/xiusin/v-system-skeleton) [![GitHub stars](https://img.shields.io/github/stars/xiusin/v-system-skeleton?style=flat)](https://github.com/xiusin/v-system-skeleton/stargazers) - Backend skeleton written in V.
- [v-vite starter](https://github.com/v-vite/starter) [![GitHub stars](https://img.shields.io/github/stars/v-vite/starter?style=flat)](https://github.com/v-vite/starter/stargazers) - A starter kit for Veb applications, preconfigured with Vite.js.
- [vblog](https://github.com/scurty-labs/vblog) [![GitHub stars](https://img.shields.io/github/stars/scurty-labs/vblog?style=flat)](https://github.com/scurty-labs/vblog/stargazers) - A simple, fast and responsive blogging system.
- [Vebview.JS](https://github.com/malisipi/Vebview.JS) [![GitHub stars](https://img.shields.io/github/stars/malisipi/Vebview.JS?style=flat)](https://github.com/malisipi/Vebview.JS/stargazers) - Electron/Neutralino.JS alternative written in V.
- [Verne](https://github.com/davlgd/Verne) [![GitHub stars](https://img.shields.io/github/stars/davlgd/Verne?style=flat)](https://github.com/davlgd/Verne/stargazers) - The other static site generator named after a famous French author.
- [vico_bot](https://github.com/KArjmand/vico_bot) [![GitHub stars](https://img.shields.io/github/stars/KArjmand/vico_bot?style=flat)](https://github.com/KArjmand/vico_bot/stargazers) - Lightweight self-hosted AI chatbot with persistent memory and tool calling.
- [Vieter](https://github.com/ChewingBever/vieter) [![GitHub stars](https://img.shields.io/github/stars/ChewingBever/vieter?style=flat)](https://github.com/ChewingBever/vieter/stargazers) - Arch Linux repository server & package build system, written in V.
- [Vlang Benchmarks Visualization](https://github.com/ArtemkaKun/VlangBenchmarksVisualization) [![GitHub stars](https://img.shields.io/github/stars/ArtemkaKun/VlangBenchmarksVisualization?style=flat)](https://github.com/ArtemkaKun/VlangBenchmarksVisualization/stargazers) - Fancy statistics and plots for *[Is V still fast?](https://fast.vlang.io/)*.
- [vorum](https://github.com/vlang/vorum) [![GitHub stars](https://img.shields.io/github/stars/vlang/vorum?style=flat)](https://github.com/vlang/vorum/stargazers) - Open-source blogging/forum software written in V.
- [vss](https://github.com/vssio/vss) [![GitHub stars](https://img.shields.io/github/stars/vssio/vss?style=flat)](https://github.com/vssio/vss/stargazers) - Easy-to-use static site generator.
- [VTik](https://github.com/Sharqo78/VTik) [![GitHub stars](https://img.shields.io/github/stars/Sharqo78/VTik?style=flat)](https://github.com/Sharqo78/VTik/stargazers) - TikTok and Twitter video downloader app (CLI / Telegram Bot).

## Libraries

### Audio

- [miniaudio](https://github.com/larpon/miniaudio) [![GitHub stars](https://img.shields.io/github/stars/larpon/miniaudio?style=flat)](https://github.com/larpon/miniaudio/stargazers) - Bindings for the excellent miniaudio C audio library.
- [vave](https://github.com/thecodrr/vave) [![GitHub stars](https://img.shields.io/github/stars/thecodrr/vave?style=flat)](https://github.com/thecodrr/vave/stargazers) - A crazy simple library for reading/writing WAV files in V. 🌊
- [vspeech](https://github.com/thecodrr/vspeech) [![GitHub stars](https://img.shields.io/github/stars/thecodrr/vspeech?style=flat)](https://github.com/thecodrr/vspeech/stargazers) - Complete V bindings for Mozilla's DeepSpeech TensorFlow based Speech-to-Text library. 📢📜

### Automation

- [v-webdriver](https://github.com/quaesitor-scientiam/v-webdriver) [![GitHub stars](https://img.shields.io/github/stars/quaesitor-scientiam/v-webdriver?style=flat)](https://github.com/quaesitor-scientiam/v-webdriver/stargazers) - A V language implementation of the W3C WebDriver protocol for browser automation.
- [vrobot](https://github.com/eioo/vrobot) [![GitHub stars](https://img.shields.io/github/stars/eioo/vrobot?style=flat)](https://github.com/eioo/vrobot/stargazers) - Desktop automation for V. Only supports Windows.

### Command line interface (CLI) / Terminal / Shell

- [bartender](https://github.com/tobealive/bartender) [![GitHub stars](https://img.shields.io/github/stars/tobealive/bartender?style=flat)](https://github.com/tobealive/bartender/stargazers) - Customizable progress indicators for V terminal applications.
- [boxx](https://github.com/thecodrr/boxx) [![GitHub stars](https://img.shields.io/github/stars/thecodrr/boxx?style=flat)](https://github.com/thecodrr/boxx/stargazers) - Create highly customizable terminal boxes that also look great! 📦
- [lol](https://github.com/0xLeif/lol) [![GitHub stars](https://img.shields.io/github/stars/0xLeif/lol?style=flat)](https://github.com/0xLeif/lol/stargazers) - V version of lolcat (text/character rainbowizer).
- [progressbar](https://github.com/Waqar144/progressbar) [![GitHub stars](https://img.shields.io/github/stars/Waqar144/progressbar?style=flat)](https://github.com/Waqar144/progressbar/stargazers) - An easy to use V library for creating progress bars in cli.
- [spinners](https://github.com/rhygg/spinners) [![GitHub stars](https://img.shields.io/github/stars/rhygg/spinners?style=flat)](https://github.com/rhygg/spinners/stargazers) - Create spinners in your terminal!
- [termtable](https://github.com/serkonda7/termtable) [![GitHub stars](https://img.shields.io/github/stars/serkonda7/termtable?style=flat)](https://github.com/serkonda7/termtable/stargazers) - V Terminal Tables: Simple and highly customizable library to display tables in the terminal.
- [vargs](https://github.com/nedpals/vargs) [![GitHub stars](https://img.shields.io/github/stars/nedpals/vargs?style=flat)](https://github.com/nedpals/vargs/stargazers) - V library for parsing arguments from argv-like arrays. ( Archived )
- [vesseract](https://github.com/barrack-obama/vesseract) [![GitHub stars](https://img.shields.io/github/stars/barrack-obama/vesseract?style=flat)](https://github.com/barrack-obama/vesseract/stargazers) - V wrapper for Tesseract-OCR (optical character recognition).

### Database clients
<!-- lint disable awesome-spell-check -->
- [firebird](https://github.com/einar-hjortdal/firebird) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/firebird?style=flat)](https://github.com/einar-hjortdal/firebird/stargazers) - Client for Firebird SQL.
- [mongodb](https://github.com/vlang/mongo) [![GitHub stars](https://img.shields.io/github/stars/vlang/mongo?style=flat)](https://github.com/vlang/mongo/stargazers) - A MongoDB driver for V.
- [redict](https://github.com/einar-hjortdal/redict) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/redict?style=flat)](https://github.com/einar-hjortdal/redict/stargazers) - Client for Redict, a LGPL-3.0-only fork of Redis (compatible with Redis <=7.2.4).
- [redis](https://github.com/patrickpissurno/vredis) [![GitHub stars](https://img.shields.io/github/stars/patrickpissurno/vredis?style=flat)](https://github.com/patrickpissurno/vredis/stargazers) - A Redis client for V, written in V.
- [vduckdb](https://github.com/rodabt/vduckdb) [![GitHub stars](https://img.shields.io/github/stars/rodabt/vduckdb?style=flat)](https://github.com/rodabt/vduckdb/stargazers) - A DuckDB client wrapper for V.
- [vmemcached](https://github.com/blacktrub/vmemcached) [![GitHub stars](https://img.shields.io/github/stars/blacktrub/vmemcached?style=flat)](https://github.com/blacktrub/vmemcached/stargazers) - Memcached client for V, written in V.
- [vredis](https://github.com/xiusin/vredis) [![GitHub stars](https://img.shields.io/github/stars/xiusin/vredis?style=flat)](https://github.com/xiusin/vredis/stargazers) - A simple, user-friendly, and comprehensive Redis client.
- [vsql](https://github.com/lydiandy/vsql) [![GitHub stars](https://img.shields.io/github/stars/lydiandy/vsql?style=flat)](https://github.com/lydiandy/vsql/stargazers) - A sql query builder for V.

### Discord

- [discord.v](https://github.com/Terisback/discord.v) [![GitHub stars](https://img.shields.io/github/stars/Terisback/discord.v?style=flat)](https://github.com/Terisback/discord.v/stargazers) - User-friendly Discord bot library.
- [discordwebhook](https://github.com/ysdragon/discordwebhook) [![GitHub stars](https://img.shields.io/github/stars/ysdragon/discordwebhook?style=flat)](https://github.com/ysdragon/discordwebhook/stargazers) - Super simple interface to send discord messages through webhooks.
- [kitten](https://github.com/geniushq/kitten) [![GitHub stars](https://img.shields.io/github/stars/geniushq/kitten?style=flat)](https://github.com/geniushq/kitten/stargazers) - Simple Discord API library for writing bots.
- [viscord](https://github.com/vlang/viscord) [![GitHub stars](https://img.shields.io/github/stars/vlang/viscord?style=flat)](https://github.com/vlang/viscord/stargazers) - Pretty basic library for connecting to the Discord gateway.
- [vord](https://github.com/9xN/vord) [![GitHub stars](https://img.shields.io/github/stars/9xN/vord?style=flat)](https://github.com/9xN/vord/stargazers) - Library for interacting with user account endpoints and gateway (Self-bots, custom clients, etc).

### Eventing

- [eventbus](https://github.com/vlang/v/tree/master/vlib/eventbus) [![GitHub stars](https://img.shields.io/github/stars/vlang/v/tree/master/vlib/eventbus?style=flat)](https://github.com/vlang/v/tree/master/vlib/eventbus/stargazers) - A simple event bus system for V.

### File handling

- [v-mime](https://github.com/nedpals/v-mime) [![GitHub stars](https://img.shields.io/github/stars/nedpals/v-mime?style=flat)](https://github.com/nedpals/v-mime/stargazers) - MIME detection library for V.
- [vmon](https://github.com/Larpon/vmon) [![GitHub stars](https://img.shields.io/github/stars/Larpon/vmon?style=flat)](https://github.com/Larpon/vmon/stargazers) - Asynchronously watch for file changes in a directory. The module is essentially a V wrapper for `septag/dmon`. It works for Windows, macOS and Linux.

### Game development

- [chipmunk2d](https://github.com/larpon/chipmunk2d) [![GitHub stars](https://img.shields.io/github/stars/larpon/chipmunk2d?style=flat)](https://github.com/larpon/chipmunk2d/stargazers) - V wrapper of the Chipmunk2D physics library.
- [engine](https://github.com/LouisSchmieder/engine) [![GitHub stars](https://img.shields.io/github/stars/LouisSchmieder/engine?style=flat)](https://github.com/LouisSchmieder/engine/stargazers) - WIP Vulkan in V.
- [raylib.v](https://github.com/irishgreencitrus/raylib.v) [![GitHub stars](https://img.shields.io/github/stars/irishgreencitrus/raylib.v?style=flat)](https://github.com/irishgreencitrus/raylib.v/stargazers) - Updated V bindings for [raylib](https://www.raylib.com) with plans for complete cross-platform support.
- [sdl2test](https://github.com/nsauzede/sdl2test) [![GitHub stars](https://img.shields.io/github/stars/nsauzede/sdl2test?style=flat)](https://github.com/nsauzede/sdl2test/stargazers) - Exhaustive suite of tests and examples for SDL2 with V.
- [shy](https://github.com/Larpon/shy) [![GitHub stars](https://img.shields.io/github/stars/Larpon/shy?style=flat)](https://github.com/Larpon/shy/stargazers) - A foundation that helps you being creative in V.
- [V_ecs](https://github.com/mohamedLT/V_ecs) [![GitHub stars](https://img.shields.io/github/stars/mohamedLT/V_ecs?style=flat)](https://github.com/mohamedLT/V_ecs/stargazers) - ECS library made in V inspired by Bevy ECS.
- [vraylib](https://github.com/mohamedLT/vraylib) [![GitHub stars](https://img.shields.io/github/stars/mohamedLT/vraylib?style=flat)](https://github.com/mohamedLT/vraylib/stargazers) - A V wrapper for the awesome raylib library.
- [vraylib](https://github.com/MajorHard/vraylib) [![GitHub stars](https://img.shields.io/github/stars/MajorHard/vraylib?style=flat)](https://github.com/MajorHard/vraylib/stargazers) - V wrapper (bindings) for raylib, the C game development framework.
- [wren](https://github.com/larpon/wren) [![GitHub stars](https://img.shields.io/github/stars/larpon/wren?style=flat)](https://github.com/larpon/wren/stargazers) - V wrapper around the excellent Wren scripting language.

### Graphics

- [sdl](https://github.com/vlang/sdl) [![GitHub stars](https://img.shields.io/github/stars/vlang/sdl?style=flat)](https://github.com/vlang/sdl/stargazers) - Official SDL2 & SDL3 bindings for V.
- [sgldraw](https://github.com/larpon/sgldraw) [![GitHub stars](https://img.shields.io/github/stars/larpon/sgldraw?style=flat)](https://github.com/larpon/sgldraw/stargazers) - An experimental real-time vector render V module based on `sokol.sgl`.
- [svgg](https://github.com/Avocadocs/svgg) [![GitHub stars](https://img.shields.io/github/stars/Avocadocs/svgg?style=flat)](https://github.com/Avocadocs/svgg/stargazers) - V module to load and resterize svg file into `gg.Image` object.
- [V Earcut](https://github.com/Larpon/earcut) [![GitHub stars](https://img.shields.io/github/stars/Larpon/earcut?style=flat)](https://github.com/Larpon/earcut/stargazers) - fast (real-time) polygon triangulation library based on [mapbox/Earcut](https://github.com/mapbox/earcut) [![GitHub stars](https://img.shields.io/github/stars/mapbox/earcut?style=flat)](https://github.com/mapbox/earcut/stargazers) to handle holes, twisted polygons, degeneracies and self-intersections.
- [V_sokol_gp](https://github.com/mohamedLT/V_sokol_gp) [![GitHub stars](https://img.shields.io/github/stars/mohamedLT/V_sokol_gp?style=flat)](https://github.com/mohamedLT/V_sokol_gp/stargazers) - A V wrapper for the sokol_gp library for easy and fast 2d graphics.
- [vglyph](https://github.com/vlang/vglyph) [![GitHub stars](https://img.shields.io/github/stars/vlang/vglyph?style=flat)](https://github.com/vlang/vglyph/stargazers) - High-performance text rendering engine for the V programming language, built on Pango, FreeType, and Sokol.
- [viup](https://github.com/kjlaw89/viup) [![GitHub stars](https://img.shields.io/github/stars/kjlaw89/viup?style=flat)](https://github.com/kjlaw89/viup/stargazers) - V wrapper for the C-based cross-platform UI library, IUP.
- [vsdl](https://github.com/kjlaw89/vsdl) [![GitHub stars](https://img.shields.io/github/stars/kjlaw89/vsdl?style=flat)](https://github.com/kjlaw89/vsdl/stargazers) - V wrapper for the C-based SDL library.
- [vsdl2](https://github.com/nsauzede/vsdl2) [![GitHub stars](https://img.shields.io/github/stars/nsauzede/vsdl2?style=flat)](https://github.com/nsauzede/vsdl2/stargazers) - A libSDL2 wrapper.
- [vsl.vcl](https://github.com/vlang/vsl/tree/master/vcl#readme) - VCL is a high level way of writing programs with OpenCL using V. These are highly opinionated OpenCL bindings for V. It tries to make GPU computing easy, with some sugar abstraction, V's concurrency and channels.
- [vbmp](https://github.com/dy-tea/vbmp) [![GitHub stars](https://img.shields.io/github/stars/dy-tea/vbmp?style=flat)](https://github.com/dy-tea/vbmp/stargazers) - Read and write bitmap files.
- [voronoi](https://github.com/larpon/voronoi) [![GitHub stars](https://img.shields.io/github/stars/larpon/voronoi?style=flat)](https://github.com/larpon/voronoi/stargazers) - V wrapper of [JCash/voronoi](https://github.com/JCash/voronoi) [![GitHub stars](https://img.shields.io/github/stars/JCash/voronoi?style=flat)](https://github.com/JCash/voronoi/stargazers).
- [vqoi](https://github.com/Le0Developer/vqoi) [![GitHub stars](https://img.shields.io/github/stars/Le0Developer/vqoi?style=flat)](https://github.com/Le0Developer/vqoi/stargazers) - V: QOI - The "Quite OK Image" format for fast, lossless image compression.

### Interoperability

- [jni](https://github.com/larpon/jni) [![GitHub stars](https://img.shields.io/github/stars/larpon/jni?style=flat)](https://github.com/larpon/jni/stargazers) - V wrapper around the C Java Native Interface (Desktop + Android).
- [vjsx](https://github.com/guweigang/vjsx) [![GitHub stars](https://img.shields.io/github/stars/guweigang/vjsx?style=flat)](https://github.com/guweigang/vjsx/stargazers) - V bindings to quickjs javascript engine. Run JS in V.
- [vphp](https://github.com/guweigang/vphp) [![GitHub stars](https://img.shields.io/github/stars/guweigang/vphp?style=flat)](https://github.com/guweigang/vphp/stargazers) - Vlang library for building PHP extensions natively in Vlang.

### IRC

- [vitric](https://github.com/m-242/vitric) [![GitHub stars](https://img.shields.io/github/stars/m-242/vitric?style=flat)](https://github.com/m-242/vitric/stargazers) - A transparent IRC library.

### Networking

- [netaddr](https://github.com/gechandesu/netaddr) [![GitHub stars](https://img.shields.io/github/stars/gechandesu/netaddr?style=flat)](https://github.com/gechandesu/netaddr/stargazers) - IPv4, IPv6 and MAC (EUI-48, EUI-64) addresses manipulation library.
- [netio](https://github.com/gechandesu/netio) [![GitHub stars](https://img.shields.io/github/stars/gechandesu/netio?style=flat)](https://github.com/gechandesu/netio/stargazers) - Low-level networking library for V that gives more control over sockets.
- [v-grpc](https://github.com/hyperpolymath/v-grpc) [![GitHub stars](https://img.shields.io/github/stars/hyperpolymath/v-grpc?style=flat)](https://github.com/hyperpolymath/v-grpc/stargazers) - gRPC and Protobuf support for V with Idris2 ABI proofs and Zig FFI.
- [vibe](https://github.com/tobealive/vibe) [![GitHub stars](https://img.shields.io/github/stars/tobealive/vibe?style=flat)](https://github.com/tobealive/vibe/stargazers) - Request library that wraps libcurl to enable fast and reliable requests while providing a higher-level API.
- [vmq](https://github.com/jordan-bonecutter/vmq) [![GitHub stars](https://img.shields.io/github/stars/jordan-bonecutter/vmq?style=flat)](https://github.com/jordan-bonecutter/vmq/stargazers) -  V wrapper For [ZMQ](https://zeromq.org/) (aka ZeroMQ, ØMQ, 0MQ: a high-performance asynchronous messaging library).

### Operating system

- [clipboard](https://github.com/vlang/v/tree/master/vlib/clipboard) [![GitHub stars](https://img.shields.io/github/stars/vlang/v/tree/master/vlib/clipboard?style=flat)](https://github.com/vlang/v/tree/master/vlib/clipboard/stargazers) - V module for interacting with the OS clipboard. Fully cross-platform.
- [mmap](https://github.com/jdonnerstag/vlang-mmap) [![GitHub stars](https://img.shields.io/github/stars/jdonnerstag/vlang-mmap?style=flat)](https://github.com/jdonnerstag/vlang-mmap/stargazers) - Provide native V-lang support for memory-mapping on Linux and Windows.
- [vlipboard](https://github.com/asvvvad/vlipboard) [![GitHub stars](https://img.shields.io/github/stars/asvvvad/vlipboard?style=flat)](https://github.com/asvvvad/vlipboard/stargazers) - An easy to use wrapper of clipboard with Wayland and Termux support.
- [winreg](https://github.com/ldedev/WindowsRegistry) [![GitHub stars](https://img.shields.io/github/stars/ldedev/WindowsRegistry?style=flat)](https://github.com/ldedev/WindowsRegistry/stargazers) - MS Windows Registry API. (WIP)

### Scientific computing

- [vplot](https://github.com/erdetn/vplot) [![GitHub stars](https://img.shields.io/github/stars/erdetn/vplot?style=flat)](https://github.com/erdetn/vplot/stargazers) - V wrapper for GNU Plot (`gnuplot_i`).
- [vsl](https://github.com/vlang/vsl) [![GitHub stars](https://img.shields.io/github/stars/vlang/vsl?style=flat)](https://github.com/vlang/vsl/stargazers) - A Scientific Library with a great variety of different modules. Although most modules offer pure-V definitions, it also provides modules that wrap known C libraries among other backends that allow high performance computing as an alternative. Also provides opinionated wrappers for OpenBLAS, LAPACKE, MPI, OpenCL among other libraries.
- [vstats](https://github.com/rodabt/vstats) [![GitHub stars](https://img.shields.io/github/stars/rodabt/vstats?style=flat)](https://github.com/rodabt/vstats/stargazers) - A dependency-free Linear Algebra, Statistics, and Machine Learning library written from scratch in V.
- [vtl](https://github.com/vlang/vtl) [![GitHub stars](https://img.shields.io/github/stars/vlang/vtl?style=flat)](https://github.com/vlang/vtl/stargazers) - The V Tensor Library is a numerical computing library supporting n-dimensional data structure, backed by VSL.
- [NeuralNetworks-V-Module](https://github.com/Eliyaan/NeuralNetworks-V-Module) [![GitHub stars](https://img.shields.io/github/stars/Eliyaan/NeuralNetworks-V-Module?style=flat)](https://github.com/Eliyaan/NeuralNetworks-V-Module/stargazers) - This is a V module to create neural networks.

### Serial Communications

- [vi2c](https://github.com/erdetn/vi2c) [![GitHub stars](https://img.shields.io/github/stars/erdetn/vi2c?style=flat)](https://github.com/erdetn/vi2c/stargazers) - A tiny (wrapper) library for I2C serial communication for Linux written in V.
- [vserialport](https://github.com/erdetn/vserialport) [![GitHub stars](https://img.shields.io/github/stars/erdetn/vserialport?style=flat)](https://github.com/erdetn/vserialport/stargazers) - V wrapper for [libserialport](https://sigrok.org/wiki/Libserialport).
- [vserialx](https://github.com/erdetn/vserialx) [![GitHub stars](https://img.shields.io/github/stars/erdetn/vserialx?style=flat)](https://github.com/erdetn/vserialx/stargazers) - A tiny (wrapper) serial communication library for Linux written in V.

### Telecommunications

- [vagi](https://github.com/Ouri028/vagi) [![GitHub stars](https://img.shields.io/github/stars/Ouri028/vagi?style=flat)](https://github.com/Ouri028/vagi/stargazers) - Asterisk FastAGI library in V.

### Telegram

- [velegram](https://github.com/tailsmails/velegram) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/velegram?style=flat)](https://github.com/tailsmails/velegram/stargazers) - A V language wrapper for TDLib (Telegram Database Library).
- [vgram](https://github.com/dariotarantini/vgram) [![GitHub stars](https://img.shields.io/github/stars/dariotarantini/vgram?style=flat)](https://github.com/dariotarantini/vgram/stargazers) - Telegram bot library.

### Text processing


- [ascii_robot](https://github.com/Delta456/ascii_robot) [![GitHub stars](https://img.shields.io/github/stars/Delta456/ascii_robot?style=flat)](https://github.com/Delta456/ascii_robot/stargazers) - ASCII Robot generator written in V.
- [chalk](https://github.com/etienne-napoleone/chalk) [![GitHub stars](https://img.shields.io/github/stars/etienne-napoleone/chalk?style=flat)](https://github.com/etienne-napoleone/chalk/stargazers) - Colorize strings in the terminal.
- [cjson](https://github.com/lydiandy/cjson) [![GitHub stars](https://img.shields.io/github/stars/lydiandy/cjson?style=flat)](https://github.com/lydiandy/cjson/stargazers) - Wrap cJSON for vlang.
- [crayon](https://github.com/thecodrr/crayon) [![GitHub stars](https://img.shields.io/github/stars/thecodrr/crayon?style=flat)](https://github.com/thecodrr/crayon/stargazers) - Paint your terminal output like Picasso. 🖍️🎨
- [iconv](https://github.com/fanlia/iconv) [![GitHub stars](https://img.shields.io/github/stars/fanlia/iconv?style=flat)](https://github.com/fanlia/iconv/stargazers) - Wrap iconv for vlang.
- [pcre2](https://github.com/srackham/pcre2) [![GitHub stars](https://img.shields.io/github/stars/srackham/pcre2?style=flat)](https://github.com/srackham/pcre2/stargazers) - Library for processing PCRE regular expressions.
- [read_xlsx_v](https://github.com/fanlia/read_xlsx_v) [![GitHub stars](https://img.shields.io/github/stars/fanlia/read_xlsx_v?style=flat)](https://github.com/fanlia/read_xlsx_v/stargazers) - Read xlsx using vlang.
- [Rosie-RPL](https://github.com/jdonnerstag/vlang-rosie) [![GitHub stars](https://img.shields.io/github/stars/jdonnerstag/vlang-rosie?style=flat)](https://github.com/jdonnerstag/vlang-rosie/stargazers) - A Rosie Pattern Language (RPL) implementation.
- [slugify](https://github.com/einar-hjortdal/slugify) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/slugify?style=flat)](https://github.com/einar-hjortdal/slugify/stargazers) - Transform Unicode strings to url-friendly human-readable ASCII slugs.
- [text-processing](https://github.com/ArtemkaKun/text-processing) [![GitHub stars](https://img.shields.io/github/stars/ArtemkaKun/text-processing?style=flat)](https://github.com/ArtemkaKun/text-processing/stargazers) - V text processing library, that contains common tools to manipulate text data.
- [v-regex](https://github.com/spytheman/v-regex) [![GitHub stars](https://img.shields.io/github/stars/spytheman/v-regex?style=flat)](https://github.com/spytheman/v-regex/stargazers) - A simple regex library for V.
- [vsoup](https://github.com/marcalc/vsoup) [![GitHub stars](https://img.shields.io/github/stars/marcalc/vsoup?style=flat)](https://github.com/marcalc/vsoup/stargazers) - A fast, JSoup-inspired HTML5 parser and DOM manipulation library for V, powered by Lexbor.
- [vxml](https://github.com/i582/vxml) [![GitHub stars](https://img.shields.io/github/stars/i582/vxml?style=flat)](https://github.com/i582/vxml/stargazers) - Pure V library for parsing XML to a DOM.
- [whisker](https://github.com/hungrybluedev/whisker) [![GitHub stars](https://img.shields.io/github/stars/hungrybluedev/whisker?style=flat)](https://github.com/hungrybluedev/whisker/stargazers) - Fast, robust template engine for V inspired by mustache.
- [xlsx](https://github.com/hungrybluedev/xlsx) [![GitHub stars](https://img.shields.io/github/stars/hungrybluedev/xlsx?style=flat)](https://github.com/hungrybluedev/xlsx/stargazers) - V library for reading and writing Microsoft Excel files.
- [lexical_uuid](https://github.com/einar-hjortdal/lexical_uuid) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/lexical_uuid?style=flat)](https://github.com/einar-hjortdal/lexical_uuid/stargazers) - Lexicographically-sortable universally unique identifiers.

### User Interface toolkits

- [bobatea](https://github.com/tauraamui/bobatea) [![GitHub stars](https://img.shields.io/github/stars/tauraamui/bobatea?style=flat)](https://github.com/tauraamui/bobatea/stargazers) - TUI framework inspired by Bubble Tea.
- [iUI](https://github.com/isaiahpatton/ui) [![GitHub stars](https://img.shields.io/github/stars/isaiahpatton/ui?style=flat)](https://github.com/isaiahpatton/ui/stargazers) - Isaiah's cross-platform GUI library for V. Inspired by the syntax of Java's Swing.
- [mui](https://github.com/malisipi/mui) [![GitHub stars](https://img.shields.io/github/stars/malisipi/mui?style=flat)](https://github.com/malisipi/mui/stargazers) - A Cross-Platform UI library for Windows, Linux, Android and Web.
- [V UI](https://github.com/vlang/ui) [![GitHub stars](https://img.shields.io/github/stars/vlang/ui?style=flat)](https://github.com/vlang/ui/stargazers) - Integrated cross platform UI toolkit for Windows, macOS, Linux, Android, iOS and the web.
- [vgtk3](https://github.com/vgtk/vgtk3) [![GitHub stars](https://img.shields.io/github/stars/vgtk/vgtk3?style=flat)](https://github.com/vgtk/vgtk3/stargazers) - A wrapper for GTK3 in V.
- [vig](https://github.com/nsauzede/vig) [![GitHub stars](https://img.shields.io/github/stars/nsauzede/vig?style=flat)](https://github.com/nsauzede/vig/stargazers) - Bindings for [Dear ImGui](https://github.com/ocornut/imgui) [![GitHub stars](https://img.shields.io/github/stars/ocornut/imgui?style=flat)](https://github.com/ocornut/imgui/stargazers) GUI toolkit.
- [vnk](https://github.com/nsauzede/vnk) [![GitHub stars](https://img.shields.io/github/stars/nsauzede/vnk?style=flat)](https://github.com/nsauzede/vnk/stargazers) - Bindings for [Nuklear](https://github.com/vurtun/nuklear) [![GitHub stars](https://img.shields.io/github/stars/vurtun/nuklear?style=flat)](https://github.com/vurtun/nuklear/stargazers) GUI toolkit.
- [V-WebUI](https://github.com/webui-dev/v-webui) [![GitHub stars](https://img.shields.io/github/stars/webui-dev/v-webui?style=flat)](https://github.com/webui-dev/v-webui/stargazers) - A wrapper for WebUI. A lightweight library that allows you to use any web browser as a GUI, with V in the backend and HTML5 in the frontend.
- [webview](https://github.com/ttytm/webview) [![GitHub stars](https://img.shields.io/github/stars/ttytm/webview?style=flat)](https://github.com/ttytm/webview/stargazers) - Bindings for webview. A tiny library to build modern cross-platform GUI applications. It allows to combine V with modern web technologies to design a graphical user interface.

### Utility

- [dialog](https://github.com/ttytm/dialog) [![GitHub stars](https://img.shields.io/github/stars/ttytm/dialog?style=flat)](https://github.com/ttytm/dialog/stargazers) - A cross-platform utility library to open system dialogs - open files, message boxes, color-pickers etc.
- [dotenv](https://github.com/einar-hjortdal/dotenv) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/dotenv?style=flat)](https://github.com/einar-hjortdal/dotenv/stargazers) - Loads environment variables from a .env file for development purposes.
- [json2v](https://github.com/ldedev/Json2V) [![GitHub stars](https://img.shields.io/github/stars/ldedev/Json2V?style=flat)](https://github.com/ldedev/Json2V/stargazers) - Convert a json to a struct in Vlang.
- [objc](https://github.com/magic003/objc) [![GitHub stars](https://img.shields.io/github/stars/magic003/objc?style=flat)](https://github.com/magic003/objc/stargazers) - V bindings to Objective-C runtime.
- [range](https://github.com/Delta456/range) [![GitHub stars](https://img.shields.io/github/stars/Delta456/range?style=flat)](https://github.com/Delta456/range/stargazers) - Functionality of Python's range() in V.
- [ssh-config](https://github.com/walkingdevel/ssh-config) [![GitHub stars](https://img.shields.io/github/stars/walkingdevel/ssh-config?style=flat)](https://github.com/walkingdevel/ssh-config/stargazers) - A V library for parsing SSH config files.
- [structlog](https://github.com/gechandesu/structlog) [![GitHub stars](https://img.shields.io/github/stars/gechandesu/structlog?style=flat)](https://github.com/gechandesu/structlog/stargazers) - Structured logs library for V.
- [V-crypto](https://github.com/bstnbuck/V-crypto) [![GitHub stars](https://img.shields.io/github/stars/bstnbuck/V-crypto?style=flat)](https://github.com/bstnbuck/V-crypto/stargazers) - Implementation of additional cryptographic algorithms.
- [vaker](https://github.com/ChAoSUnItY/vaker) [![GitHub stars](https://img.shields.io/github/stars/ChAoSUnItY/vaker?style=flat)](https://github.com/ChAoSUnItY/vaker/stargazers) - A light-weight compile-time-generated data faker written in V.
- [vanadium](https://github.com/tailsmails/vanadium) [![GitHub stars](https://img.shields.io/github/stars/tailsmails/vanadium?style=flat)](https://github.com/tailsmails/vanadium/stargazers) - Ada-level runtime safety for the V programming language.
- [vdotenv](https://github.com/zztkm/vdotenv) [![GitHub stars](https://img.shields.io/github/stars/zztkm/vdotenv?style=flat)](https://github.com/zztkm/vdotenv/stargazers) - Support for .env files which loads environment variables.
- [vhs](https://github.com/KevinDaSilvaS/vhs) [![GitHub stars](https://img.shields.io/github/stars/KevinDaSilvaS/vhs?style=flat)](https://github.com/KevinDaSilvaS/vhs/stargazers) - Haskell prelude list functions(zip, zipwith, head, etc) implemented in V.
- [VInstall](https://github.com/malisipi/VInstall) [![GitHub stars](https://img.shields.io/github/stars/malisipi/VInstall?style=flat)](https://github.com/malisipi/VInstall/stargazers) - A cross-platform installer creator.
- [votp](https://github.com/OdaiGH/votp) [![GitHub stars](https://img.shields.io/github/stars/OdaiGH/votp?style=flat)](https://github.com/OdaiGH/votp/stargazers) - TOTP and HOTP implementation in v.

### Web

- [blobly](https://github.com/einar-hjortdal/blobly) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/blobly?style=flat)](https://github.com/einar-hjortdal/blobly/stargazers) - Central file server.
- [jsonrpcv](https://github.com/Te4nick/jsonrpcv) [![GitHub stars](https://img.shields.io/github/stars/Te4nick/jsonrpcv?style=flat)](https://github.com/Te4nick/jsonrpcv/stargazers) - JSON-RPC 2.0 client+server implementation in pure V.
- [pico.v](https://github.com/S-YOU/pico.v) [![GitHub stars](https://img.shields.io/github/stars/S-YOU/pico.v?style=flat)](https://github.com/S-YOU/pico.v/stargazers) - A web server in V based on picoev and picohttpparser.
- [sessions](https://github.com/einar-hjortdal/sessions) [![GitHub stars](https://img.shields.io/github/stars/einar-hjortdal/sessions?style=flat)](https://github.com/einar-hjortdal/sessions/stargazers) - Web-framework-agnostic sessions library.
- [v-graphql](https://github.com/hyperpolymath/v-graphql) [![GitHub stars](https://img.shields.io/github/stars/hyperpolymath/v-graphql?style=flat)](https://github.com/hyperpolymath/v-graphql/stargazers) - GraphQL server implementation with schema generation, Idris2 ABI proofs, and Zig FFI.
- [v-jsonrpc](https://github.com/nedpals/v-jsonrpc) [![GitHub stars](https://img.shields.io/github/stars/nedpals/v-jsonrpc?style=flat)](https://github.com/nedpals/v-jsonrpc/stargazers) - Basic JSON-RPC 2.0-compliant server written on V.
- [v-rest](https://github.com/hyperpolymath/v-rest) [![GitHub stars](https://img.shields.io/github/stars/hyperpolymath/v-rest?style=flat)](https://github.com/hyperpolymath/v-rest/stargazers) - REST API server framework with Idris2 ABI proofs and Zig FFI.
- [v-tiktok](https://github.com/walkingdevel/v-tiktok) [![GitHub stars](https://img.shields.io/github/stars/walkingdevel/v-tiktok?style=flat)](https://github.com/walkingdevel/v-tiktok/stargazers) - A V library for downloading TikTok videos.
- [validate](https://github.com/endeveit/v-validate) [![GitHub stars](https://img.shields.io/github/stars/endeveit/v-validate?style=flat)](https://github.com/endeveit/v-validate/stargazers) - A simple library to validate strings in V.
- [valval](https://github.com/taojy123/valval) [![GitHub stars](https://img.shields.io/github/stars/taojy123/valval?style=flat)](https://github.com/taojy123/valval/stargazers) - Web framework written in V, improved by vweb.
- [vcurrency](https://github.com/mehtaarn000/vcurrency) [![GitHub stars](https://img.shields.io/github/stars/mehtaarn000/vcurrency?style=flat)](https://github.com/mehtaarn000/vcurrency/stargazers) - API wrapper (written in V) for [https://api.exchangeratesapi.io](https://api.exchangeratesapi.io).
- [veb](https://github.com/vlang/v/tree/master/vlib/veb) [![GitHub stars](https://img.shields.io/github/stars/vlang/v/tree/master/vlib/veb?style=flat)](https://github.com/vlang/v/tree/master/vlib/veb/stargazers) - V's built-in web framework.
- [vest](https://github.com/alexferl/vest) [![GitHub stars](https://img.shields.io/github/stars/alexferl/vest?style=flat)](https://github.com/alexferl/vest/stargazers) - A REST client in V.
- [vex](https://github.com/nedpals/vex) [![GitHub stars](https://img.shields.io/github/stars/nedpals/vex?style=flat)](https://github.com/nedpals/vex/stargazers) - Web framework written on V inspired by Express and Sinatra.
- [vigest](https://github.com/withs/vigest) [![GitHub stars](https://img.shields.io/github/stars/withs/vigest?style=flat)](https://github.com/withs/vigest/stargazers) - Simple client for digest authentication (written in V).
- [vite.v](https://github.com/siguici/vite.v) [![GitHub stars](https://img.shields.io/github/stars/siguici/vite.v?style=flat)](https://github.com/siguici/vite.v/stargazers) - Seamless [Vite.js](https://vite.dev) integration for Veb applications.
- [vxbloauth](https://github.com/WolvesFortress/vxbl-oauth) [![GitHub stars](https://img.shields.io/github/stars/WolvesFortress/vxbl-oauth?style=flat)](https://github.com/WolvesFortress/vxbl-oauth/stargazers) - A minimalistic Xbox Live authenticator for vweb.
- [west](https://github.com/Dracks/West) [![GitHub stars](https://img.shields.io/github/stars/Dracks/West?style=flat)](https://github.com/Dracks/West/stargazers) - A wrapper of vweb to work in a similar way as nestjs works with modules and dependency injection.

## Other

### Articles

- [An introduction to V](https://simonknott.de/articles/VLang.html)

### Books

- [Getting Started with V Programming - Navule Pavan Kumar Rao - Packt 2021 Dec](https://www.amazon.com/Getting-Started-Programming-end-end-ebook/dp/B09FKK3JL7/ref=sr_1_1?keywords=Getting+started+with+V+programming&qid=1639480830&sr=8-1) - Introductory book on V.

### Communities

- [V Community](https://github.com/v-community) [![GitHub stars](https://img.shields.io/github/stars/v-community?style=flat)](https://github.com/v-community/stargazers)

### Editor plugins

- [tree-sitter-v](https://github.com/undivisible/tree-sitter-v) [![GitHub stars](https://img.shields.io/github/stars/undivisible/tree-sitter-v?style=flat)](https://github.com/undivisible/tree-sitter-v/stargazers) - Tree-sitter grammar for V language. Maintained fork with modern API, crates.io package, 244 node types.

#### Atom

- [language-v](https://github.com/Cutlery-Drawer/language-v) [![GitHub stars](https://img.shields.io/github/stars/Cutlery-Drawer/language-v?style=flat)](https://github.com/Cutlery-Drawer/language-v/stargazers) - V language support for Atom (port of vscode-vlang).

#### Emacs

- [v-mode](https://github.com/damon-kwok/v-mode) [![GitHub stars](https://img.shields.io/github/stars/damon-kwok/v-mode?style=flat)](https://github.com/damon-kwok/v-mode/stargazers) - Emacs major mode for the V programming language.
- [vlang-mode.el](https://github.com/Naheel-Azawy/vlang-mode.el) [![GitHub stars](https://img.shields.io/github/stars/Naheel-Azawy/vlang-mode.el?style=flat)](https://github.com/Naheel-Azawy/vlang-mode.el/stargazers) - Emacs major mode for the V programming language.

#### Pulsar

- [language-v](https://packages.pulsar-edit.dev/packages/language-v) - V language support for Atom (port of vscode-vlang) (migrated from atom.io)

#### Sublime Text 3

- [sublime-v](https://github.com/onerbs/sublime-v) [![GitHub stars](https://img.shields.io/github/stars/onerbs/sublime-v?style=flat)](https://github.com/onerbs/sublime-v/stargazers) - Fully-featured Sublime Text 3 package for the V Programming Language.
- [vlang-sublime](https://github.com/oversoul/vlang-sublime) [![GitHub stars](https://img.shields.io/github/stars/oversoul/vlang-sublime?style=flat)](https://github.com/oversoul/vlang-sublime/stargazers) - Sublime Text 3 Support for the Vlang Programming Language.

#### VS Code

- [vscode-vlang](https://github.com/vlang/vscode-vlang) [![GitHub stars](https://img.shields.io/github/stars/vlang/vscode-vlang?style=flat)](https://github.com/vlang/vscode-vlang/stargazers) - V Language extension for Visual Studio Code.
- [v-analyzer](https://github.com/vlang/v-analyzer) [![GitHub stars](https://img.shields.io/github/stars/vlang/v-analyzer?style=flat)](https://github.com/vlang/v-analyzer/stargazers) - Bring IDE features for the V programming language to VS Code.

#### Vim

- [v-vim](https://github.com/ollykel/v-vim) [![GitHub stars](https://img.shields.io/github/stars/ollykel/v-vim?style=flat)](https://github.com/ollykel/v-vim/stargazers) - Support for V syntax highlighting in Vim.
- [vim-v](https://github.com/cheap-glitch/vim-v) [![GitHub stars](https://img.shields.io/github/stars/cheap-glitch/vim-v?style=flat)](https://github.com/cheap-glitch/vim-v/stargazers) - Quality syntax highlighting for the V programming language.
- [vim-vtools](https://github.com/zakuro9715/vim-vtools) [![GitHub stars](https://img.shields.io/github/stars/zakuro9715/vim-vtools?style=flat)](https://github.com/zakuro9715/vim-vtools/stargazers) - V tools for Vim, including auto formatting.

### Forums

- [r/vlang](https://www.reddit.com/r/vlang)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/vlang)

### GitHub Actions

- [action-create-v-docs](https://github.com/marketplace/actions/create-documentation-for-v-modules) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/create-documentation-for-v-modules?style=flat)](https://github.com/marketplace/actions/create-documentation-for-v-modules/stargazers) - GitHub action to create documentation for V modules.
- [setup-v](https://github.com/marketplace/actions/setup-vlang) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/setup-vlang?style=flat)](https://github.com/marketplace/actions/setup-vlang/stargazers) - GitHub action to install and use V in your workflow.

### GitHub templates

- [v-project-basement](https://github.com/ArtemkaKun/v-project-basement) [![GitHub stars](https://img.shields.io/github/stars/ArtemkaKun/v-project-basement?style=flat)](https://github.com/ArtemkaKun/v-project-basement/stargazers) - A basement for every V project, that contains universal minimum GitHub CI scripts and issue templates for a V project.

### IDEs with V

- [Vide](https://github.com/IsaiahPatton/Vide) [![GitHub stars](https://img.shields.io/github/stars/IsaiahPatton/Vide?style=flat)](https://github.com/IsaiahPatton/Vide/stargazers)

### Online IDEs with V

- [V Playground](https://play.vlang.io)
- [V Playground (old)](https://v-wasm.now.sh/)
- [VOSCA V Playground](https://play.vosca.dev)

### Operating Systems & OS Development Examples

- [limine-v-template](https://github.com/plos-clan/limine-v-template) [![GitHub stars](https://img.shields.io/github/stars/plos-clan/limine-v-template?style=flat)](https://github.com/plos-clan/limine-v-template/stargazers) - A simple template for building a Limine-compliant kernel in V.
- [Simple Linux kernel module example](https://github.com/spytheman/simple_kernel_module_in_v) [![GitHub stars](https://img.shields.io/github/stars/spytheman/simple_kernel_module_in_v?style=flat)](https://github.com/spytheman/simple_kernel_module_in_v/stargazers) - Demonstration & test of writing a very simple Linux kernel module, using V.
- [v-limine](https://github.com/wenxuanjun/v-limine) [![GitHub stars](https://img.shields.io/github/stars/wenxuanjun/v-limine?style=flat)](https://github.com/wenxuanjun/v-limine/stargazers) - A V library for handling Limine boot protocol structures.

### Patterns

- [MVU.v](https://github.com/ArtemkaKun/MVU.v) [![GitHub stars](https://img.shields.io/github/stars/ArtemkaKun/MVU.v?style=flat)](https://github.com/ArtemkaKun/MVU.v/stargazers) - MVU pattern (The Elm Architecture) implemented in V programming language.

### Programming contests

- [Advent of Code 2019](https://github.com/mvlootman/aoc2019) [![GitHub stars](https://img.shields.io/github/stars/mvlootman/aoc2019?style=flat)](https://github.com/mvlootman/aoc2019/stargazers) - Solution of Advent of Code 2019 in V.
- [Advent of Code 2022](https://github.com/vlang/adventofcode) [![GitHub stars](https://img.shields.io/github/stars/vlang/adventofcode?style=flat)](https://github.com/vlang/adventofcode/stargazers) - Solution of Advent of Code 2022 in V.
- [Rosetta Code in V](https://rosettacode.org/wiki/Category:V_(Vlang)) - Solutions for Rosetta Code in V.
- [SoloLearn Coding Challenges](https://github.com/Serkonda/v-sololearn-coding-challenges) [![GitHub stars](https://img.shields.io/github/stars/Serkonda/v-sololearn-coding-challenges?style=flat)](https://github.com/Serkonda/v-sololearn-coding-challenges/stargazers) - Implementation of the SoloLearn coding challenges in V.

### Syntax highlighting

- [kate-syntax-highlight-v](https://github.com/Larpon/kate-syntax-highlight-v) [![GitHub stars](https://img.shields.io/github/stars/Larpon/kate-syntax-highlight-v?style=flat)](https://github.com/Larpon/kate-syntax-highlight-v/stargazers) - V syntax highlighting for [Kate](https://kate-editor.org/).
- [scite-v-support](https://github.com/sunnylcw/scite-v-support) [![GitHub stars](https://img.shields.io/github/stars/sunnylcw/scite-v-support?style=flat)](https://github.com/sunnylcw/scite-v-support/stargazers) - V syntax highlighting for [SciTE](https://www.scintilla.org/SciTE.html).

### Tutorials

- [Learn V in Y Minutes](https://github.com/v-community/learn_v_in_y_minutes) [![GitHub stars](https://img.shields.io/github/stars/v-community/learn_v_in_y_minutes?style=flat)](https://github.com/v-community/learn_v_in_y_minutes/stargazers)
- [V by Example](https://github.com/v-community/v_by_example) [![GitHub stars](https://img.shields.io/github/stars/v-community/v_by_example?style=flat)](https://github.com/v-community/v_by_example/stargazers) - V book as [GitBook](https://v-community.gitbook.io/v-by-example/).
- [V for Node Devs](https://github.com/Thigidu/vlang-for-nodejs-developers) [![GitHub stars](https://img.shields.io/github/stars/Thigidu/vlang-for-nodejs-developers?style=flat)](https://github.com/Thigidu/vlang-for-nodejs-developers/stargazers) - Vlang for node js developers.
- [V learning notes](https://github.com/lydiandy/vlang_note) [![GitHub stars](https://img.shields.io/github/stars/lydiandy/vlang_note?style=flat)](https://github.com/lydiandy/vlang_note/stargazers) - Personal learning notes in Chinese.
- [VOSCA Blog Tutorials](https://blog.vosca.dev/categories/tutorials/) - Tutorial category on VOSCA blog.

### Videos

- [The V Programming Language](https://www.youtube.com/channel/UCLZIElNyubHOvbfudT7KS1A)
- [V Programming Tutorials](https://www.youtube.com/watch?v=BVCuZ7z7GMY&list=PLEPMhdsq-gNpFr40A-ZnX-Hu9l-Sp5Oc_)
