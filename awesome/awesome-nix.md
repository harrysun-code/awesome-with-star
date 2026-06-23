# Nix

[![GitHub stars](https://img.shields.io/github/stars/nix-community/awesome-nix?style=flat)](https://github.com/nix-community/awesome-nix/stargazers)

# Awesome Nix [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<a href="https://nixos.org">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NixOS/nixos-artwork/master/logo/nixos.svg">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NixOS/nixos-artwork/master/logo/nixos-white.png">
    <img src="https://raw.githubusercontent.com/NixOS/nixos-artwork/master/logo/nixos.svg" align="right" width="250" alt="NixOS logo">
  </picture>
</a>

A curated list of the best resources in the Nix community.

<br>

[Nix](https://github.com/nixos/nix) [![GitHub stars](https://img.shields.io/github/stars/nixos/nix?style=flat)](https://github.com/nixos/nix/stargazers) is a powerful package manager for Linux and other Unix systems that makes package management reliable and reproducible.

*Please read the [contribution guidelines](CONTRIBUTING.md) before contributing.*

## Contents

* [Resources](#resources)
    * [Learning](#learning)
    * [Discovery](#discovery)
* [Installation Media](#installation-media)
* [Channel History](#channel-history)
* [Deployment Tools](#deployment-tools)
* [Virtualisation](#virtualisation)
* [Command-Line Tools](#command-line-tools)
* [Development](#development)
* [DevOps](#devops)
* [Programming Languages](#programming-languages)
    * [Arduino](#arduino)
    * [Clojure](#clojure)
    * [Crystal](#crystal)
    * [Elm](#elm)
    * [Gleam](#gleam)
    * [Haskell](#haskell)
    * [Haxe](#haxe)
    * [Julia](#julia)
    * [Lean](#lean)
    * [Node.js](#nodejs)
    * [OCaml](#ocaml)
    * [PHP](#php)
    * [PureScript](#purescript)
    * [Python](#python)
    * [Ruby](#ruby)
    * [Rust](#rust)
    * [Scala](#scala)
    * [Zig](#zig)
* [NixOS Modules](#nixos-modules)
* [NixOS Configuration Editors](#nixos-configuration-editors)
* [Overlays](#overlays)
* [Distributions](#distributions)
* [Community](#community)

## Resources

### Learning

* [Building a Rust service with Nix](https://fasterthanli.me/series/building-a-rust-service-with-nix) - An in-depth blog series about creating a Rust application with Nix.
* [Explainix](https://zaynetro.com/explainix) - Explain Nix syntax visually.
* [How to Learn Nix](https://ianthehenry.com/posts/how-to-learn-nix/) - It's like a Let's Play, but for obscure software documentation.
* [Nix - A One Pager](https://code.tvl.fyi/about/nix/nix-1p) - A one page introduction to the Nix language.
* [nix-book](https://saylesss88.github.io) - A comprehensive guide to NixOS
  hardening and configuration.
* [Nix from First Principles: Flake Edition](https://tonyfinn.com/blog/nix-from-first-principles-flake-edition/) - A modern crash-course to using Nix features, Flakes, and developing with Nix.
* [Nix in 100 Seconds](https://www.youtube.com/watch?v=FJVFXsNzYZQ) - A YouTube video from Fireship presenting Nix in 100 seconds.
* [Nix Notes](https://github.com/noteed/nix-notes) [![GitHub stars](https://img.shields.io/github/stars/noteed/nix-notes?style=flat)](https://github.com/noteed/nix-notes/stargazers) - A collection of short notes about Nix, each contributing to the same virtual machine image.
* [Nix Pills](https://nixos.org/guides/nix-pills/) - The best way to learn, with examples.
* [Nix Shorts](https://github.com/alper/nix-shorts) [![GitHub stars](https://img.shields.io/github/stars/alper/nix-shorts?style=flat)](https://github.com/alper/nix-shorts/stargazers) - A collection of short notes about how to use Nix, updated for Nix Flakes.
* [Nix Starter Config](https://github.com/Misterio77/nix-starter-configs) [![GitHub stars](https://img.shields.io/github/stars/Misterio77/nix-starter-configs?style=flat)](https://github.com/Misterio77/nix-starter-configs/stargazers) - A few simple Nix Flake templates for getting started with NixOS + home-manager.
* [nix.dev](https://nix.dev/) - An opinionated guide for developers about getting things done using the Nix ecosystem.
* [NixOS & Flakes Book](https://github.com/ryan4yin/nixos-and-flakes-book) [![GitHub stars](https://img.shields.io/github/stars/ryan4yin/nixos-and-flakes-book?style=flat)](https://github.com/ryan4yin/nixos-and-flakes-book/stargazers) - An unofficial and opinionated NixOS & Flakes book for beginners.
* [NixOS Asia Tutorial Series](https://nixos.asia/en/tutorial) - A series of high-level tutorials on using Nix Flakes, NixOS, home-manager, etc.
* [NixOS in Production](https://leanpub.com/nixos-in-production) - Free (pay-what-you-want) book in pdf format.
* [Official Nix manual](https://nix.dev/manual/nix/stable/) - Latest stable version of the official Nix manual, best used as reference guide. Receives updates when available.
* [Official NixOS manual](https://nixos.org/manual/nixos/stable/) - Latest stable version of the official NixOS manual, mix of tutorial and reference guide. Receives updates when available.
* [Official Nixpkgs manual](https://nixos.org/manual/nixpkgs/stable/) - Latest stable version of the official Nixpkgs reference manual. Receives updates when available.
* [Tour of Nix](https://nixcloud.io/tour/) - An online interactive tutorial on Nix language constructs.
* [Wombat's Book of Nix](https://mhwombat.codeberg.page/nix-book/) - A book-length introduction to Nix and flakes.
* [Zero to Nix](https://zero-to-nix.com/) - A flake-centric guide to Nix and its concepts created by Determinate Systems to quickly onboard beginners.

### Discovery

* [Home Manager Option Search](https://home-manager-options.extranix.com/) - Search through all 2000+ Home Manager options and read how to use them.
<!-- * [Hound](https://search.nix.gsc.io) - Handily search across all or selected Nix-related repositories. -->
* [Nix Package Versions](https://lazamar.co.uk/nix-versions/) - Find all versions of a package that were available in a channel and the revision you can download it from.
* [nix-search-tv](https://github.com/3timeslazy/nix-search-tv) [![GitHub stars](https://img.shields.io/github/stars/3timeslazy/nix-search-tv?style=flat)](https://github.com/3timeslazy/nix-search-tv/stargazers) - CLI fuzzy finder for packages and options from Nixpkgs, Home Manager, and more.
* [Noogle](https://noogle.dev/) - Nix API search engine allowing to search functions based on their types and other attributes.
* [NüschtOS Search](https://github.com/NuschtOS/search) [![GitHub stars](https://img.shields.io/github/stars/NuschtOS/search?style=flat)](https://github.com/NuschtOS/search/stargazers) - Simple and fast static-page NixOS option search.
* [Searchix](https://searchix.ovh/) - Search Nix packages and options from NixOS, Darwin and Home Manager.

## Installation Media

* [nix-installer-scripts](https://github.com/dnkmmr69420/nix-installer-scripts) [![GitHub stars](https://img.shields.io/github/stars/dnkmmr69420/nix-installer-scripts?style=flat)](https://github.com/dnkmmr69420/nix-installer-scripts/stargazers) - Runs the official installer but does some tweaking as well such as adding fcontext for selinux and installing nix outside of the default profile so you don't accidently uninstall it.
* [nix-installer](https://github.com/DeterminateSystems/nix-installer) [![GitHub stars](https://img.shields.io/github/stars/DeterminateSystems/nix-installer?style=flat)](https://github.com/DeterminateSystems/nix-installer/stargazers) - Opinionated alternative to the official Nix install scripts.
* [nixos-anywhere](https://github.com/nix-community/nixos-anywhere) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nixos-anywhere?style=flat)](https://github.com/nix-community/nixos-anywhere/stargazers) - Install NixOS everywhere via SSH.
* [nixos-generators](https://github.com/nix-community/nixos-generators) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nixos-generators?style=flat)](https://github.com/nix-community/nixos-generators/stargazers) -  Take a NixOS config and build multiple different images types including VirtualBox VMs, Azure images, and installation ISOs.
* [nixos-infect](https://github.com/elitak/nixos-infect) [![GitHub stars](https://img.shields.io/github/stars/elitak/nixos-infect?style=flat)](https://github.com/elitak/nixos-infect/stargazers) - Replace a running non-NixOS Linux host with NixOS.
* [nixos-up](https://github.com/samuela/nixos-up) [![GitHub stars](https://img.shields.io/github/stars/samuela/nixos-up?style=flat)](https://github.com/samuela/nixos-up/stargazers) - Super easy NixOS installer that can be used from the installation ISO.

## Channel History

* [`npc`](https://github.com/samestep/npc) [![GitHub stars](https://img.shields.io/github/stars/samestep/npc?style=flat)](https://github.com/samestep/npc/stargazers) - CLI to view and bisect Nixpkgs channel history.
* [Nix Infra Status](https://status.nixos.org) - Get the age and current Git commit of each Nix channel.
* [Nix Review Tools Reports](https://malob.github.io/nix-review-tools-reports/) - Reports showing problematic dependencies (dependencies causing the most failed builds) for major Hydra jobsets.
<!-- * [Nixpkgs Bot](https://git.maralorn.de/nixos-config/tree/packages/nixpkgs-bot) - A Matrix bot to track when a Nixpkgs pull request reaches a relevant branch. -->
* [nixpkgs PR tracker](https://nixpk.gs/pr-tracker.html) - A tracker for whether a PR has made it into a channel yet.

## Deployment Tools

* [bento](https://github.com/rapenne-s/bento/) [![GitHub stars](https://img.shields.io/github/stars/rapenne-s/bento/?style=flat)](https://github.com/rapenne-s/bento//stargazers) - A KISS deployment tool to keep your NixOS fleet (servers & workstations) up to date.
* [Clan](https://clan.lol) - A peer-to-peer deployment tool with inbuilt support for secrets and a module system to manage distributed networks.
* [Colmena](https://github.com/zhaofengli/colmena) [![GitHub stars](https://img.shields.io/github/stars/zhaofengli/colmena?style=flat)](https://github.com/zhaofengli/colmena/stargazers) - A simple, stateless NixOS deployment tool modeled after NixOps and morph.
* [comin](https://github.com/nlewo/comin) [![GitHub stars](https://img.shields.io/github/stars/nlewo/comin?style=flat)](https://github.com/nlewo/comin/stargazers) - A deployment tool to continuously pull from Git repositories.
* [deploy-rs](https://github.com/serokell/deploy-rs) [![GitHub stars](https://img.shields.io/github/stars/serokell/deploy-rs?style=flat)](https://github.com/serokell/deploy-rs/stargazers) - A simple multi-profile Nix-flake deploy tool.
* [krops](https://cgit.krebsco.de/krops/about/) - A lightweight toolkit to deploy NixOS systems, remotely or locally.
* [KubeNix](https://github.com/hall/kubenix) [![GitHub stars](https://img.shields.io/github/stars/hall/kubenix?style=flat)](https://github.com/hall/kubenix/stargazers) - A Kubernetes resource builder using Nix.
* [KuberNix](https://github.com/saschagrunert/kubernix) [![GitHub stars](https://img.shields.io/github/stars/saschagrunert/kubernix?style=flat)](https://github.com/saschagrunert/kubernix/stargazers) - Single-dependency Kubernetes clusters via Nix packages.
* [morph](https://github.com/DBCDK/morph) [![GitHub stars](https://img.shields.io/github/stars/DBCDK/morph?style=flat)](https://github.com/DBCDK/morph/stargazers) - A tool for managing existing NixOS hosts.
* [Nixery](https://github.com/tazjin/nixery) [![GitHub stars](https://img.shields.io/github/stars/tazjin/nixery?style=flat)](https://github.com/tazjin/nixery/stargazers) - A Docker-compatible container registry which builds images ad-hoc via Nix.
* [Nixinate](https://github.com/MatthewCroughan/nixinate) [![GitHub stars](https://img.shields.io/github/stars/MatthewCroughan/nixinate?style=flat)](https://github.com/MatthewCroughan/nixinate/stargazers) - A Nix flake library to provide app outputs for managing existing NixOS hosts over SSH.
* [Nixlets](https://gitlab.com/TECHNOFAB/nixlets) - Like Helm but using only Nix, uses Kubenix under the hood.
* [NixOps](https://github.com/NixOS/nixops) [![GitHub stars](https://img.shields.io/github/stars/NixOS/nixops?style=flat)](https://github.com/NixOS/nixops/stargazers) - The official Nix deployment tool, compatible with AWS, Hetzner, and more.
* [pushnix](https://github.com/arnarg/pushnix) [![GitHub stars](https://img.shields.io/github/stars/arnarg/pushnix?style=flat)](https://github.com/arnarg/pushnix/stargazers) - Simple cli utility that pushes NixOS configuration and triggers a rebuild using ssh.
* [terraform-nixos](https://github.com/nix-community/terraform-nixos) [![GitHub stars](https://img.shields.io/github/stars/nix-community/terraform-nixos?style=flat)](https://github.com/nix-community/terraform-nixos/stargazers) - A set of Terraform modules designed to deploy NixOS.
* [terranix](https://terranix.org) - Use Nix and the NixOS module system to write your Terraform code.

## Virtualisation

* [extra-container](https://github.com/erikarvstedt/extra-container) [![GitHub stars](https://img.shields.io/github/stars/erikarvstedt/extra-container?style=flat)](https://github.com/erikarvstedt/extra-container/stargazers) - Run declarative NixOS containers from the command line.
* [microvm](https://github.com/microvm-nix/microvm.nix) [![GitHub stars](https://img.shields.io/github/stars/microvm-nix/microvm.nix?style=flat)](https://github.com/microvm-nix/microvm.nix/stargazers) - NixOS-based MicroVMs.
* [nixos-shell](https://github.com/Mic92/nixos-shell) [![GitHub stars](https://img.shields.io/github/stars/Mic92/nixos-shell?style=flat)](https://github.com/Mic92/nixos-shell/stargazers) - Simple headless VM configuration using Nix (similar to Vagrant).

## Command-Line Tools

* [alejandra](https://github.com/kamadorueda/alejandra) [![GitHub stars](https://img.shields.io/github/stars/kamadorueda/alejandra?style=flat)](https://github.com/kamadorueda/alejandra/stargazers) - An opinionated Nix code formatter optimized for speed and consistency.
* [angrr](https://github.com/linyinfeng/angrr) [![GitHub stars](https://img.shields.io/github/stars/linyinfeng/angrr?style=flat)](https://github.com/linyinfeng/angrr/stargazers) - Auto Nix GC Roots Retention. This tool simply deletes auto GC roots based on the modified time of their symbolic link target.
* [comma](https://github.com/nix-community/comma) [![GitHub stars](https://img.shields.io/github/stars/nix-community/comma?style=flat)](https://github.com/nix-community/comma/stargazers) - Quickly run any binary; wraps together `nix run` and `nix-index`.
* [deadnix](https://github.com/astro/deadnix) [![GitHub stars](https://img.shields.io/github/stars/astro/deadnix?style=flat)](https://github.com/astro/deadnix/stargazers) - Scan Nix files for dead code.
* [devenv](https://github.com/cachix/devenv) [![GitHub stars](https://img.shields.io/github/stars/cachix/devenv?style=flat)](https://github.com/cachix/devenv/stargazers) - A Nix-based tool for creating developer shell environments quickly and reproducibly.
* [dix](https://github.com/faukah/dix) [![GitHub stars](https://img.shields.io/github/stars/faukah/dix?style=flat)](https://github.com/faukah/dix/stargazers) - Diff Nix; a super-fast tool to diff Nix related things.
* [manix](https://github.com/mlvzk/manix) [![GitHub stars](https://img.shields.io/github/stars/mlvzk/manix?style=flat)](https://github.com/mlvzk/manix/stargazers) - Find configuration options and function documentation for Nixpkgs, NixOS, and Home Manager.
* [nh](https://github.com/nix-community/nh) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nh?style=flat)](https://github.com/nix-community/nh/stargazers) - Better output for `nix`, `nixos-rebuild`, `home-manager` and nix-darwin CLI leveraging `dix` and `nix-output-monitor`.
* [nix-alien](https://github.com/thiagokokada/nix-alien) [![GitHub stars](https://img.shields.io/github/stars/thiagokokada/nix-alien?style=flat)](https://github.com/thiagokokada/nix-alien/stargazers) - Run unpatched binaries on Nix/NixOS easily.
* [nix-diff](https://github.com/Gabriella439/nix-diff) [![GitHub stars](https://img.shields.io/github/stars/Gabriella439/nix-diff?style=flat)](https://github.com/Gabriella439/nix-diff/stargazers) - A tool to explain why two Nix derivations differ.
* [nix-du](https://github.com/symphorien/nix-du) [![GitHub stars](https://img.shields.io/github/stars/symphorien/nix-du?style=flat)](https://github.com/symphorien/nix-du/stargazers) - Visualise which gc-roots to delete to free some space in your Nix store.
* [nix-index](https://github.com/nix-community/nix-index) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nix-index?style=flat)](https://github.com/nix-community/nix-index/stargazers) - Quickly locate Nix packages with specific files.
* [nix-init](https://github.com/nix-community/nix-init) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nix-init?style=flat)](https://github.com/nix-community/nix-init/stargazers) - Generate Nix packages from URLs with hash prefetching, dependency inference, license detection, and more.
* [nix-melt](https://github.com/nix-community/nix-melt) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nix-melt?style=flat)](https://github.com/nix-community/nix-melt/stargazers) - A ranger-like flake.lock viewer.
* [nix-output-monitor](https://github.com/maralorn/nix-output-monitor) [![GitHub stars](https://img.shields.io/github/stars/maralorn/nix-output-monitor?style=flat)](https://github.com/maralorn/nix-output-monitor/stargazers) - A tool to produce useful graphs and statistics when building derivations.
* [nix-prefetch](https://github.com/msteen/nix-prefetch) [![GitHub stars](https://img.shields.io/github/stars/msteen/nix-prefetch?style=flat)](https://github.com/msteen/nix-prefetch/stargazers) - A universal tool for updating source checksums.
* [nix-tree](https://github.com/utdemir/nix-tree) [![GitHub stars](https://img.shields.io/github/stars/utdemir/nix-tree?style=flat)](https://github.com/utdemir/nix-tree/stargazers) - Interactively browse the dependency graph of Nix derivations.
* [nixfmt](https://github.com/NixOS/nixfmt) [![GitHub stars](https://img.shields.io/github/stars/NixOS/nixfmt?style=flat)](https://github.com/NixOS/nixfmt/stargazers) - A formatter for Nix code, intended to easily apply a uniform style.
* [nixos-cli](https://github.com/nix-community/nixos-cli) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nixos-cli?style=flat)](https://github.com/nix-community/nixos-cli/stargazers) - Configurable all-in-one CLI for common NixOS tools with an emphasis on improved user experience.
* [nixpkgs-hammering](https://github.com/jtojnar/nixpkgs-hammering) [![GitHub stars](https://img.shields.io/github/stars/jtojnar/nixpkgs-hammering?style=flat)](https://github.com/jtojnar/nixpkgs-hammering/stargazers) - An opinionated linter for Nixpkgs package expressions.
* [nurl](https://github.com/nix-community/nurl) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nurl?style=flat)](https://github.com/nix-community/nurl/stargazers) - Generate Nix fetcher calls from repository URLs.
* [nvd](https://git.sr.ht/~khumba/nvd) - Diff package versions between two store paths; it's especially useful for comparing NixOS generations on rebuild.
* [optnix](https://git.sr.ht/~watersucks/optnix) - A terminal-based options searcher for Nix module systems.
* [statix](https://github.com/oppiliappan/statix) [![GitHub stars](https://img.shields.io/github/stars/oppiliappan/statix?style=flat)](https://github.com/oppiliappan/statix/stargazers) - A linter/fixer to check for and fix antipatterns in Nix code.

## Development

* [Arion](https://github.com/hercules-ci/arion) [![GitHub stars](https://img.shields.io/github/stars/hercules-ci/arion?style=flat)](https://github.com/hercules-ci/arion/stargazers) - Run `docker-compose` with help from Nix/NixOS.
* [attic](https://github.com/zhaofengli/attic) [![GitHub stars](https://img.shields.io/github/stars/zhaofengli/attic?style=flat)](https://github.com/zhaofengli/attic/stargazers) - Multi-tenant Nix Binary Cache.
* [cached-nix-shell](https://github.com/xzfc/cached-nix-shell) [![GitHub stars](https://img.shields.io/github/stars/xzfc/cached-nix-shell?style=flat)](https://github.com/xzfc/cached-nix-shell/stargazers) - A `nix-shell` replacement that uses caching to open subsequent shells quickly.
* [Cachix](https://www.cachix.org) - Hosted binary cache service; free for open-source projects.
* [compose2nix](https://github.com/aksiksi/compose2nix) [![GitHub stars](https://img.shields.io/github/stars/aksiksi/compose2nix?style=flat)](https://github.com/aksiksi/compose2nix/stargazers) - Generate a NixOS config from a Docker Compose project.
* [Conflake](https://ratson.github.io/conflake/) - A batteries included, autoload files, convention-based configuration framework for `flake.nix`.
* [Devbox](https://github.com/jetify-com/devbox) [![GitHub stars](https://img.shields.io/github/stars/jetify-com/devbox?style=flat)](https://github.com/jetify-com/devbox/stargazers) - Instant, portable, and predictable development environments.
* [devshell](https://github.com/numtide/devshell) [![GitHub stars](https://img.shields.io/github/stars/numtide/devshell?style=flat)](https://github.com/numtide/devshell/stargazers) - `mkShell` with extra bits and a toml config option to be able to onboard non-nix users.
* [dream2nix](https://github.com/nix-community/dream2nix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/dream2nix?style=flat)](https://github.com/nix-community/dream2nix/stargazers) - A framework for automatically converting packages from other build systems to Nix.
* [flake-utils-plus](https://github.com/gytis-ivaskevicius/flake-utils-plus) [![GitHub stars](https://img.shields.io/github/stars/gytis-ivaskevicius/flake-utils-plus?style=flat)](https://github.com/gytis-ivaskevicius/flake-utils-plus/stargazers) - A lightweight Nix library flake for painless NixOS flake configuration.
* [flake-utils](https://github.com/numtide/flake-utils) [![GitHub stars](https://img.shields.io/github/stars/numtide/flake-utils?style=flat)](https://github.com/numtide/flake-utils/stargazers) - Pure Nix flake utility functions to help with writing flakes.
* [flake.parts](https://github.com/hercules-ci/flake-parts) [![GitHub stars](https://img.shields.io/github/stars/hercules-ci/flake-parts?style=flat)](https://github.com/hercules-ci/flake-parts/stargazers) - Minimal Nix modules framework for Flakes: split your flakes into modules and get things done with community modules.
* [flakelight](https://github.com/nix-community/flakelight) [![GitHub stars](https://img.shields.io/github/stars/nix-community/flakelight?style=flat)](https://github.com/nix-community/flakelight/stargazers) - A modular flake framework aiming to minimize boilerplate.
* [flox](https://github.com/flox/flox) [![GitHub stars](https://img.shields.io/github/stars/flox/flox?style=flat)](https://github.com/flox/flox/stargazers) - Manage and share development environments, package projects, and publish artifacts anywhere.
* [gitignore.nix](https://github.com/hercules-ci/gitignore.nix) [![GitHub stars](https://img.shields.io/github/stars/hercules-ci/gitignore.nix?style=flat)](https://github.com/hercules-ci/gitignore.nix/stargazers) - The most feature-complete and easy-to-use `.gitignore` integration.
* [haumea](https://github.com/nix-community/haumea) [![GitHub stars](https://img.shields.io/github/stars/nix-community/haumea?style=flat)](https://github.com/nix-community/haumea/stargazers) - Filesystem-based module system for the Nix language similar to traditional programming languages, with support for file hierarchy and visibility.
* [lorri](https://github.com/nix-community/lorri/) [![GitHub stars](https://img.shields.io/github/stars/nix-community/lorri/?style=flat)](https://github.com/nix-community/lorri//stargazers) - A much better `nix-shell` for development that augments direnv.
* [make-shell](https://github.com/nicknovitski/make-shell) [![GitHub stars](https://img.shields.io/github/stars/nicknovitski/make-shell?style=flat)](https://github.com/nicknovitski/make-shell/stargazers) - `mkShell` meets modules, a modular almost-drop-in replacement for `pkgs.mkShell` function.
* [MCP-NixOS](https://github.com/utensils/mcp-nixos) [![GitHub stars](https://img.shields.io/github/stars/utensils/mcp-nixos?style=flat)](https://github.com/utensils/mcp-nixos/stargazers) - An MCP server that provides AI assistants with accurate information about NixOS packages, options, Home Manager, and nix-darwin configurations.
* [namaka](https://github.com/nix-community/namaka) [![GitHub stars](https://img.shields.io/github/stars/nix-community/namaka?style=flat)](https://github.com/nix-community/namaka/stargazers) - Snapshot testing for Nix based on haumea.
* [nil](https://github.com/oxalica/nil) [![GitHub stars](https://img.shields.io/github/stars/oxalica/nil?style=flat)](https://github.com/oxalica/nil/stargazers) - NIx Language server, an incremental analysis assistent for writing in Nix.
* [niv](https://github.com/nmattia/niv/) [![GitHub stars](https://img.shields.io/github/stars/nmattia/niv/?style=flat)](https://github.com/nmattia/niv//stargazers) - Easy dependency management for Nix projects with package pinning.
* [nix2container](https://github.com/nlewo/nix2container) [![GitHub stars](https://img.shields.io/github/stars/nlewo/nix2container?style=flat)](https://github.com/nlewo/nix2container/stargazers) - An efficient container building workflow with Nix.
* [nix-direnv](https://github.com/nix-community/nix-direnv) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nix-direnv?style=flat)](https://github.com/nix-community/nix-direnv/stargazers) - A fast loader and flake-compliant configuration for the direnv environment auto-loader.
* [nix-health](https://github.com/juspay/nix-health) [![GitHub stars](https://img.shields.io/github/stars/juspay/nix-health?style=flat)](https://github.com/juspay/nix-health/stargazers) - A program to check the health of your Nix install. Furthermore, individual projects can configure their own health checks in their `flake.nix`.
* [nix-oci](https://github.com/Dauliac/nix-oci) [![GitHub stars](https://img.shields.io/github/stars/Dauliac/nix-oci?style=flat)](https://github.com/Dauliac/nix-oci/stargazers) - A flake-parts module for building minimal, reproducible OCI containers using nix2container.
* [nix-update](https://github.com/Mic92/nix-update) [![GitHub stars](https://img.shields.io/github/stars/Mic92/nix-update?style=flat)](https://github.com/Mic92/nix-update/stargazers) - Update versions/source hashes of nix packages.
* [nixd](https://github.com/nix-community/nixd) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nixd?style=flat)](https://github.com/nix-community/nixd/stargazers) - Nix language server, based on Nix libraries.
* [nixpkgs-review](https://github.com/Mic92/nixpkgs-review) [![GitHub stars](https://img.shields.io/github/stars/Mic92/nixpkgs-review?style=flat)](https://github.com/Mic92/nixpkgs-review/stargazers) - The best tool to verify that a pull-request in Nixpkgs is building properly.
* [Nixtest](https://gitlab.com/TECHNOFAB/nixtest) - Testing framework for Nix, with snapshot and unit test support, JUnit generation etc.
* [npins](https://github.com/andir/npins) [![GitHub stars](https://img.shields.io/github/stars/andir/npins?style=flat)](https://github.com/andir/npins/stargazers) - A simple tool for handling different types of dependencies in a Nix project. It is inspired by and comparable to Niv.
* [pog](https://github.com/jpetrucciani/pog) [![GitHub stars](https://img.shields.io/github/stars/jpetrucciani/pog?style=flat)](https://github.com/jpetrucciani/pog/stargazers) - A new, powerful way to do bash scripts. Pog is a powerful Nix library that transforms the way developers create command-line interfaces (CLIs).
* [pre-commit-hooks.nix](https://github.com/cachix/git-hooks.nix) [![GitHub stars](https://img.shields.io/github/stars/cachix/git-hooks.nix?style=flat)](https://github.com/cachix/git-hooks.nix/stargazers) - Run linters/formatters at commit time and on your CI.
* [rnix-lsp](https://github.com/nix-community/rnix-lsp) [![GitHub stars](https://img.shields.io/github/stars/nix-community/rnix-lsp?style=flat)](https://github.com/nix-community/rnix-lsp/stargazers) - A syntax-checking language server for Nix.
* [robotnix](https://github.com/nix-community/robotnix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/robotnix?style=flat)](https://github.com/nix-community/robotnix/stargazers) - A declarative and reproducible build system for Android (AOSP) images.
* [services-flake](https://github.com/juspay/services-flake) [![GitHub stars](https://img.shields.io/github/stars/juspay/services-flake?style=flat)](https://github.com/juspay/services-flake/stargazers) - A NixOS-like service configuration framework for Nix flakes.
* [Snowfall Lib](https://github.com/snowfallorg/lib) [![GitHub stars](https://img.shields.io/github/stars/snowfallorg/lib?style=flat)](https://github.com/snowfallorg/lib/stargazers) - A library that makes it easy to manage your Nix flake by imposing an opinionated file structure.
* [templates](https://github.com/nix-community/templates) [![GitHub stars](https://img.shields.io/github/stars/nix-community/templates?style=flat)](https://github.com/nix-community/templates/stargazers) - Project templates for many languages using Nix flakes.
* [treefmt-nix](https://github.com/numtide/treefmt-nix) [![GitHub stars](https://img.shields.io/github/stars/numtide/treefmt-nix?style=flat)](https://github.com/numtide/treefmt-nix/stargazers) - A formatter that allows formatting all your project files with a single command, all via a single `.nix` file.

## DevOps

* [Nix GitLab CI](https://gitlab.com/TECHNOFAB/nix-gitlab-ci) - Define GitLab CI pipelines in pure Nix with full access to all Nix packages (incl. caching).
* [nixidy](https://github.com/arnarg/nixidy) [![GitHub stars](https://img.shields.io/github/stars/arnarg/nixidy?style=flat)](https://github.com/arnarg/nixidy/stargazers) - Kubernetes GitOps with Nix and Argo CD.
* [Standard](https://github.com/divnix/std) [![GitHub stars](https://img.shields.io/github/stars/divnix/std?style=flat)](https://github.com/divnix/std/stargazers) - An opinionated Nix Flakes framework to keep Nix code in large projects organized, accompanied by a friendly CLI/TUI optized for DevOps scenarios.

## Programming Languages

### Arduino

* [nixduino](https://github.com/boredom101/nixduino) [![GitHub stars](https://img.shields.io/github/stars/boredom101/nixduino?style=flat)](https://github.com/boredom101/nixduino/stargazers) - Nix-based tool to help build Arduino sketches.

### Clojure

* [clj-nix](https://github.com/jlesquembre/clj-nix) [![GitHub stars](https://img.shields.io/github/stars/jlesquembre/clj-nix?style=flat)](https://github.com/jlesquembre/clj-nix/stargazers) - Nix helper functions for Clojure projects.

### Crystal

* [crystal2nix](https://github.com/nix-community/crystal2nix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/crystal2nix?style=flat)](https://github.com/nix-community/crystal2nix/stargazers) - Convert `shard.lock` into Nix expressions.

### Elm

* [elm2nix](https://github.com/cachix/elm2nix) [![GitHub stars](https://img.shields.io/github/stars/cachix/elm2nix?style=flat)](https://github.com/cachix/elm2nix/stargazers) - Convert `elm.json` into Nix expressions.

### Gleam

* [nix-gleam](https://github.com/arnarg/nix-gleam) [![GitHub stars](https://img.shields.io/github/stars/arnarg/nix-gleam?style=flat)](https://github.com/arnarg/nix-gleam/stargazers) - Generic Nix builder for Gleam applications.

### Haskell

* [cabal2nix](https://github.com/NixOS/cabal2nix) [![GitHub stars](https://img.shields.io/github/stars/NixOS/cabal2nix?style=flat)](https://github.com/NixOS/cabal2nix/stargazers) - Converts a Cabal file into a Nix build expression.
* [haskell-flake](https://github.com/srid/haskell-flake) [![GitHub stars](https://img.shields.io/github/stars/srid/haskell-flake?style=flat)](https://github.com/srid/haskell-flake/stargazers) - A `flake-parts` Nix module for Haskell development.
* [haskell.nix](https://github.com/input-output-hk/haskell.nix) [![GitHub stars](https://img.shields.io/github/stars/input-output-hk/haskell.nix?style=flat)](https://github.com/input-output-hk/haskell.nix/stargazers) - Alternative Haskell Infrastructure for Nixpkgs.
* [nix-haskell-mode](https://github.com/matthewbauer/nix-haskell-mode) [![GitHub stars](https://img.shields.io/github/stars/matthewbauer/nix-haskell-mode?style=flat)](https://github.com/matthewbauer/nix-haskell-mode/stargazers) - Automatic Haskell setup in Emacs.
* [nixkell](https://github.com/pwm/nixkell) [![GitHub stars](https://img.shields.io/github/stars/pwm/nixkell?style=flat)](https://github.com/pwm/nixkell/stargazers) - A Haskell project template using Nix and direnv.

### Haxe
* [haxix](https://github.com/MadMcCrow/haxix) [![GitHub stars](https://img.shields.io/github/stars/MadMcCrow/haxix?style=flat)](https://github.com/MadMcCrow/haxix/stargazers) - Nix flake to build haxe/Heaps.io projects.
* [kebab](https://github.com/bwkam/kebab) [![GitHub stars](https://img.shields.io/github/stars/bwkam/kebab?style=flat)](https://github.com/bwkam/kebab/stargazers) - Haxe packages for Nix.

### Julia

* [Manifest2Nix.jl](https://codeberg.org/aniva/Manifest2Nix.jl) - A Nix library for creating reproducible Julia builds and experiments via precompilation.

### Lean

* [lean4-nix](https://github.com/lenianiva/lean4-nix) [![GitHub stars](https://img.shields.io/github/stars/lenianiva/lean4-nix?style=flat)](https://github.com/lenianiva/lean4-nix/stargazers) -  Nix flake build for Lean 4, and `lake2nix`.

### Node.js

* [Napalm](https://github.com/nix-community/napalm) [![GitHub stars](https://img.shields.io/github/stars/nix-community/napalm?style=flat)](https://github.com/nix-community/napalm/stargazers) - Support for building npm packages in Nix with a lightweight npm registry.
* [node2nix](https://github.com/svanderburg/node2nix) [![GitHub stars](https://img.shields.io/github/stars/svanderburg/node2nix?style=flat)](https://github.com/svanderburg/node2nix/stargazers) - Generate Nix expression from a `package.json` (or `package-lock.json`) (to be stored as files).
* [npmlock2nix](https://github.com/nix-community/npmlock2nix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/npmlock2nix?style=flat)](https://github.com/nix-community/npmlock2nix/stargazers) - Generate Nix expressions from a `package-lock.json` (in-memory), primarily for web projects.

### OCaml

* [opam2nix](https://github.com/timbertson/opam2nix) [![GitHub stars](https://img.shields.io/github/stars/timbertson/opam2nix?style=flat)](https://github.com/timbertson/opam2nix/stargazers) - Generate Nix expressions from opam packages.

### PHP

* [composer-plugin-nixify](https://github.com/stephank/composer-plugin-nixify) [![GitHub stars](https://img.shields.io/github/stars/stephank/composer-plugin-nixify?style=flat)](https://github.com/stephank/composer-plugin-nixify/stargazers) - Composer plugin to help with Nix packaging.
* [composer2nix](https://github.com/svanderburg/composer2nix) [![GitHub stars](https://img.shields.io/github/stars/svanderburg/composer2nix?style=flat)](https://github.com/svanderburg/composer2nix/stargazers) - Generate Nix expressions to build composer packages.
* [composition-c4](https://github.com/fossar/composition-c4) [![GitHub stars](https://img.shields.io/github/stars/fossar/composition-c4?style=flat)](https://github.com/fossar/composition-c4/stargazers) - Support for building composer packages from a `composer.lock` (using IFD).
* [nix-phps](https://github.com/fossar/nix-phps) [![GitHub stars](https://img.shields.io/github/stars/fossar/nix-phps?style=flat)](https://github.com/fossar/nix-phps/stargazers) - Flake containing old and unmaintained PHP versions (intended for CI use).
* [nix-shell](https://github.com/loophp/nix-shell/) [![GitHub stars](https://img.shields.io/github/stars/loophp/nix-shell/?style=flat)](https://github.com/loophp/nix-shell//stargazers) - Nix shells for PHP development.

### PureScript

* [Easy PureScript Nix](https://github.com/justinwoo/easy-purescript-nix) [![GitHub stars](https://img.shields.io/github/stars/justinwoo/easy-purescript-nix?style=flat)](https://github.com/justinwoo/easy-purescript-nix/stargazers) - A project to easily use PureScript and other tools with Nix.
* [purs-nix](https://github.com/purs-nix/purs-nix) [![GitHub stars](https://img.shields.io/github/stars/purs-nix/purs-nix?style=flat)](https://github.com/purs-nix/purs-nix/stargazers) - CLI and library combo designed for managing PureScript projects using Nix. It provides a Nix API that can be used within your projects, as well as a command-line interface for managing your development process.

### Python

* [poetry2nix](https://github.com/nix-community/poetry2nix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/poetry2nix?style=flat)](https://github.com/nix-community/poetry2nix/stargazers) - Build Python packages directly from [Poetry's](https://python-poetry.org/) `poetry.lock`. No conversion step needed.
* [uv2nix](https://github.com/pyproject-nix/uv2nix) [![GitHub stars](https://img.shields.io/github/stars/pyproject-nix/uv2nix?style=flat)](https://github.com/pyproject-nix/uv2nix/stargazers) - Convert [`uv` workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) into pure Nix derivations.

### Ruby

* [Bundix](https://github.com/nix-community/bundix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/bundix?style=flat)](https://github.com/nix-community/bundix/stargazers) - Generates a Nix expression for your Bundler-managed application.
* [ruby-nix](https://github.com/inscapist/ruby-nix) [![GitHub stars](https://img.shields.io/github/stars/inscapist/ruby-nix?style=flat)](https://github.com/inscapist/ruby-nix/stargazers) - Generates reproducible ruby/bundler app environment with Nix.

### Rust

* [cargo2nix](https://github.com/cargo2nix/cargo2nix) [![GitHub stars](https://img.shields.io/github/stars/cargo2nix/cargo2nix?style=flat)](https://github.com/cargo2nix/cargo2nix/stargazers) - Granular caching, development shell, Nix & Rust integration.
* [crane](https://github.com/ipetkov/crane) [![GitHub stars](https://img.shields.io/github/stars/ipetkov/crane?style=flat)](https://github.com/ipetkov/crane/stargazers) - A Nix library for building Cargo projects with incremental artifact caching.
* [fenix](https://github.com/nix-community/fenix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/fenix?style=flat)](https://github.com/nix-community/fenix/stargazers) - Rust toolchains and Rust analyzer nightly for nix.
* [naersk](https://github.com/nix-community/naersk) [![GitHub stars](https://img.shields.io/github/stars/nix-community/naersk?style=flat)](https://github.com/nix-community/naersk/stargazers) - Build Rust packages directly from `Cargo.lock`. No conversion step needed.
* [nix-cargo-integration](https://github.com/90-008/nix-cargo-integration) [![GitHub stars](https://img.shields.io/github/stars/90-008/nix-cargo-integration?style=flat)](https://github.com/90-008/nix-cargo-integration/stargazers) - A library that allows easy and effortless integration for Cargo projects.
* [nixpkgs-mozilla](https://github.com/mozilla/nixpkgs-mozilla) [![GitHub stars](https://img.shields.io/github/stars/mozilla/nixpkgs-mozilla?style=flat)](https://github.com/mozilla/nixpkgs-mozilla/stargazers) - Mozilla's overlay with Rust toolchains and Firefox.
* [rust-nix-templater](https://github.com/90-008/rust-nix-templater) [![GitHub stars](https://img.shields.io/github/stars/90-008/rust-nix-templater?style=flat)](https://github.com/90-008/rust-nix-templater/stargazers) - Generates Nix build and development files for Rust projects.
* [rust-overlay](https://github.com/oxalica/rust-overlay) [![GitHub stars](https://img.shields.io/github/stars/oxalica/rust-overlay?style=flat)](https://github.com/oxalica/rust-overlay/stargazers) - Pure and reproducible nix overlay of binary distributed Rust toolchains.

### Scala

* [sbt-derivation](https://github.com/zaninime/sbt-derivation) [![GitHub stars](https://img.shields.io/github/stars/zaninime/sbt-derivation?style=flat)](https://github.com/zaninime/sbt-derivation/stargazers) - mkDerivation for sbt, similar to buildGoModule.

### Zig

* [zig2nix](https://github.com/Cloudef/zig2nix) [![GitHub stars](https://img.shields.io/github/stars/Cloudef/zig2nix?style=flat)](https://github.com/Cloudef/zig2nix/stargazers) - Flake for packaging, building and running Zig projects.
* [zon2nix](https://github.com/nix-community/zon2nix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/zon2nix?style=flat)](https://github.com/nix-community/zon2nix/stargazers) - Convert the dependencies in `build.zig.zon` to a Nix expression.

## NixOS Modules

* [base16.nix](https://github.com/SenchoPens/base16.nix) [![GitHub stars](https://img.shields.io/github/stars/SenchoPens/base16.nix?style=flat)](https://github.com/SenchoPens/base16.nix/stargazers) - Flake way to theme programs in [base16](https://github.com/chriskempson/base16) [![GitHub stars](https://img.shields.io/github/stars/chriskempson/base16?style=flat)](https://github.com/chriskempson/base16/stargazers) colorschemes, mustache template support included.
* [Home Manager](https://github.com/nix-community/home-manager) [![GitHub stars](https://img.shields.io/github/stars/nix-community/home-manager?style=flat)](https://github.com/nix-community/home-manager/stargazers) - Manage your user configuration just like NixOS.
* [impermanence](https://github.com/nix-community/impermanence) [![GitHub stars](https://img.shields.io/github/stars/nix-community/impermanence?style=flat)](https://github.com/nix-community/impermanence/stargazers) - Lets you choose what files and directories you want to keep between reboots.
* [musnix](https://github.com/musnix/musnix) [![GitHub stars](https://img.shields.io/github/stars/musnix/musnix?style=flat)](https://github.com/musnix/musnix/stargazers) - Do real-time audio work in NixOS.
* [nix-bitcoin](https://github.com/fort-nix/nix-bitcoin) [![GitHub stars](https://img.shields.io/github/stars/fort-nix/nix-bitcoin?style=flat)](https://github.com/fort-nix/nix-bitcoin/stargazers) - Modules and packages for Bitcoin nodes with higher-layer protocols with an emphasis on security.
* [nix-darwin](https://github.com/nix-darwin/nix-darwin) [![GitHub stars](https://img.shields.io/github/stars/nix-darwin/nix-darwin?style=flat)](https://github.com/nix-darwin/nix-darwin/stargazers) - Manage macOS configuration just like on NixOS.
* [nix-mineral](https://github.com/cynicsketch/nix-mineral) [![GitHub stars](https://img.shields.io/github/stars/cynicsketch/nix-mineral?style=flat)](https://github.com/cynicsketch/nix-mineral/stargazers) - Conveniently and reasonably harden NixOS.
* [nix-topology](https://github.com/oddlama/nix-topology) [![GitHub stars](https://img.shields.io/github/stars/oddlama/nix-topology?style=flat)](https://github.com/oddlama/nix-topology/stargazers) - Generate infrastructure and network diagrams directly from your NixOS configuration.
* [NixOS hardware](https://github.com/NixOS/nixos-hardware) [![GitHub stars](https://img.shields.io/github/stars/NixOS/nixos-hardware?style=flat)](https://github.com/NixOS/nixos-hardware/stargazers) - NixOS profiles to optimize settings for different hardware.
* [NixOS-WSL](https://github.com/nix-community/NixOS-WSL) [![GitHub stars](https://img.shields.io/github/stars/nix-community/NixOS-WSL?style=flat)](https://github.com/nix-community/NixOS-WSL/stargazers) - Modules for running NixOS on the Windows Subsystem for Linux.
* [NixVim](https://github.com/nix-community/nixvim) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nixvim?style=flat)](https://github.com/nix-community/nixvim/stargazers) - A Neovim distribution built with Nix modules and Nixpkgs.
* [Self Host Blocks](https://github.com/ibizaman/selfhostblocks) [![GitHub stars](https://img.shields.io/github/stars/ibizaman/selfhostblocks?style=flat)](https://github.com/ibizaman/selfhostblocks/stargazers) - Modular server management based on NixOS modules and focused on best practices.
* [Simple Nixos Mailserver](https://gitlab.com/simple-nixos-mailserver/nixos-mailserver) - A complete mailserver, managed with NixOS modules.
* [Stylix](https://github.com/nix-community/stylix) [![GitHub stars](https://img.shields.io/github/stars/nix-community/stylix?style=flat)](https://github.com/nix-community/stylix/stargazers) - System-wide colorscheming and typography for NixOS.

## NixOS Configuration Editors

### Desktop apps

* [Nix Software Center](https://github.com/snowfallorg/nix-software-center) [![GitHub stars](https://img.shields.io/github/stars/snowfallorg/nix-software-center?style=flat)](https://github.com/snowfallorg/nix-software-center/stargazers) - Install and manage Nix packages. Desktop app in Rust and GTK.
* [NixOS Configuration Editor](https://github.com/snowfallorg/nixos-conf-editor) [![GitHub stars](https://img.shields.io/github/stars/snowfallorg/nixos-conf-editor?style=flat)](https://github.com/snowfallorg/nixos-conf-editor/stargazers) - Graphical editor for NixOS configuration. Desktop app in Rust and GTK.

### Webinterface

* [MyNixOS](https://mynixos.com/) - Graphical editor for Nix flakes. Create and manage configurations and modules for NixOS and Nix home-manager. Rather a Nix generator than a Nix editor, because it does not allow to import Nix files.

## Overlays

* [awesome-nix-hpc](https://github.com/freuk/awesome-nix-hpc) [![GitHub stars](https://img.shields.io/github/stars/freuk/awesome-nix-hpc?style=flat)](https://github.com/freuk/awesome-nix-hpc/stargazers) - High Performance Computing package sets.
* [neovim-nightly-overlay](https://github.com/nix-community/neovim-nightly-overlay) [![GitHub stars](https://img.shields.io/github/stars/nix-community/neovim-nightly-overlay?style=flat)](https://github.com/nix-community/neovim-nightly-overlay/stargazers) - Daily bumped Neovim nightly package.
* [nixpkgs-firefox-darwin](https://github.com/bandithedoge/nixpkgs-firefox-darwin) [![GitHub stars](https://img.shields.io/github/stars/bandithedoge/nixpkgs-firefox-darwin?style=flat)](https://github.com/bandithedoge/nixpkgs-firefox-darwin/stargazers) - Automatically updated Firefox binary packages for macOS.
* [nixpkgs-wayland](https://github.com/nix-community/nixpkgs-wayland) [![GitHub stars](https://img.shields.io/github/stars/nix-community/nixpkgs-wayland?style=flat)](https://github.com/nix-community/nixpkgs-wayland/stargazers) - Bleeding-edge Wayland packages.
* [NUR](https://github.com/nix-community/NUR/) [![GitHub stars](https://img.shields.io/github/stars/nix-community/NUR/?style=flat)](https://github.com/nix-community/NUR//stargazers) - Nix User Repositories. The mother of all overlays, allowing access to user repositories and installing packages via attributes.
* [System Manager](https://github.com/numtide/system-manager) [![GitHub stars](https://img.shields.io/github/stars/numtide/system-manager?style=flat)](https://github.com/numtide/system-manager/stargazers) - A non-NixOS Linux system configuration tool built on Nix.
* [zig-overlay](https://github.com/mitchellh/zig-overlay) [![GitHub stars](https://img.shields.io/github/stars/mitchellh/zig-overlay?style=flat)](https://github.com/mitchellh/zig-overlay/stargazers) - A Nix flake packaging the Zig compiler. The flake mirrors the binaries built officially by Zig and does not build them from source.

## Distributions

* [nixbsd](https://github.com/nixos-bsd/nixbsd) [![GitHub stars](https://img.shields.io/github/stars/nixos-bsd/nixbsd?style=flat)](https://github.com/nixos-bsd/nixbsd/stargazers) - A NixOS fork with a FreeBSD kernel.
* [NixNG](https://github.com/nix-community/NixNG) [![GitHub stars](https://img.shields.io/github/stars/nix-community/NixNG?style=flat)](https://github.com/nix-community/NixNG/stargazers) - A GNU/Linux distribution similar to NixOS, defining difference is a focus on containers and lightweightness.
* [SnowflakeOS](https://snowflakeos.org/) - A NixOS-based Linux distribution focused on beginner friendliness and ease of use.

## Community

* [#nix:nixos.org](https://matrix.to/#/#nix:nixos.org)
* [#nixos on Libera.Chat](https://web.libera.chat/?nick=Guest?#nixos)
* [Discord - Nix/Nixos (Unofficial)](https://discord.com/invite/BMUCQx6)
* [Discourse](https://discourse.nixos.org/) - The best place to get help and discuss Nix-related topics.
* [NixCon](https://nixcon.org/) - The annual community conference for contributors and users of Nix and NixOS.
* [Wiki (Official)](https://wiki.nixos.org/wiki/Main_Page)
* [Wiki (Unofficial)](https://nixos.wiki/wiki/Main_Page)
