# F#

[![GitHub stars](https://img.shields.io/github/stars/fsprojects/awesome-fsharp?style=flat)](https://github.com/fsprojects/awesome-fsharp/stargazers)

# Awesome F# [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <img src="https://fsharp.org/img/logo/fsharp.svg" width="48" height="48" align="right"/>

F# is a programming language with focus on immutability, type inference, first-class functions, powerful data types and pattern matching, targeting .NET and other platforms.

This is a curated list of awesome F# frameworks, libraries, software and resources.

## Contents
- [Main Language-Related Repositories](#main-language-related-repositories)
- [F# Wrappers for Popular .NET Libraries](#f-wrappers-for-popular-net-libraries)
- [Actor Frameworks](#actor-frameworks)
- [Build Tools](#build-tools)
- [Cloud](#cloud)
- [Code Analysis](#code-analysis)
- [Code Generation](#code-generation)
- [Compilers for Other Platforms](#compilers-for-other-platforms)
- [Concurrent, Asynchronous, and Parallel Programming](#concurrent-asynchronous-and-parallel-programming)
- [Configuration](#configuration)
- [Data Science](#data-science)
- [Development Tools](#development-tools)
  - [IDE](#ide)
  - [Editor Plugins](#editor-plugins)
  - [Performance Analysis](#performance-analysis)
- [General Purpose Libraries](#general-purpose-libraries)
- [Game Development](#game-development)
- [GUI](#gui)
- [HTTP Clients](#http-clients)
- [Logging](#logging)
- [Package Management](#package-management)
- [Parsing](#parsing)
- [Serialization](#serialization)
- [Simulation](#simulation)
- [Static Site Generators](#static-site-generators)
- [Testing](#testing)
- [Type Providers](#type-providers)
  - [Creating Type Providers](#creating-type-providers)
- [Visualization](#visualization)
- [Web Frameworks](#web-frameworks)
- [.NET Core Templates](#net-core-templates)
- [Resources](#resources)
  - [Blogs](#blogs)
  - [Books](#books)
  - [Cheatsheets](#cheatsheets)
  - [Community](#community)
  - [Other Lists](#other-lists)
  - [Websites](#websites)
  - [Videos](#videos)
  - [Courses](#courses)

## Main Language-Related Repositories

- [F# main repository](https://github.com/dotnet/fsharp) [![GitHub stars](https://img.shields.io/github/stars/dotnet/fsharp?style=flat)](https://github.com/dotnet/fsharp/stargazers)
- [F# projects](https://github.com/fsprojects) [![GitHub stars](https://img.shields.io/github/stars/fsprojects?style=flat)](https://github.com/fsprojects/stargazers)
- [F# suggestions](https://github.com/fsharp/fslang-suggestions) [![GitHub stars](https://img.shields.io/github/stars/fsharp/fslang-suggestions?style=flat)](https://github.com/fsharp/fslang-suggestions/stargazers)
- [F# RFCs](https://github.com/fsharp/fslang-design) [![GitHub stars](https://img.shields.io/github/stars/fsharp/fslang-design?style=flat)](https://github.com/fsharp/fslang-design/stargazers)

## F# Wrappers for Popular .NET Libraries
Looking to have a more enjoyable experience when consuming a popular .NET library? Here is a quick table.

<!-- The following table includes some entries that are duplicated in the list below. This is by design. -->  
<!--lint disable double-link -->
|.NET Library                                                                                                                     |F# Wrapper                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[ASP.NET Core Blazor](https://github.com/dotnet/aspnetcore/tree/main/src/Components) [![GitHub stars](https://img.shields.io/github/stars/dotnet/aspnetcore/tree/main/src/Components?style=flat)](https://github.com/dotnet/aspnetcore/tree/main/src/Components/stargazers)                                             |[Bolero](https://github.com/fsbolero/Bolero) [![GitHub stars](https://img.shields.io/github/stars/fsbolero/Bolero?style=flat)](https://github.com/fsbolero/Bolero/stargazers)                                                                                                                              |
|[ASP.NET Core](https://github.com/dotnet/aspnetcore) [![GitHub stars](https://img.shields.io/github/stars/dotnet/aspnetcore?style=flat)](https://github.com/dotnet/aspnetcore/stargazers)                                                                             |[Giraffe](https://github.com/giraffe-fsharp/Giraffe) [![GitHub stars](https://img.shields.io/github/stars/giraffe-fsharp/Giraffe?style=flat)](https://github.com/giraffe-fsharp/Giraffe/stargazers) (+ optionally [Saturn](https://github.com/SaturnFramework/Saturn) [![GitHub stars](https://img.shields.io/github/stars/SaturnFramework/Saturn?style=flat)](https://github.com/SaturnFramework/Saturn/stargazers))<br/>[Oxpecker](https://github.com/Lanayx/Oxpecker) [![GitHub stars](https://img.shields.io/github/stars/Lanayx/Oxpecker?style=flat)](https://github.com/Lanayx/Oxpecker/stargazers)|
|[Avalonia](https://github.com/AvaloniaUI/Avalonia) [![GitHub stars](https://img.shields.io/github/stars/AvaloniaUI/Avalonia?style=flat)](https://github.com/AvaloniaUI/Avalonia/stargazers)                                                                               |[Avalonia.FuncUI](https://github.com/fsprojects/Avalonia.FuncUI) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/Avalonia.FuncUI?style=flat)](https://github.com/fsprojects/Avalonia.FuncUI/stargazers)                                                                                                          |
|[MAUI](https://github.com/dotnet/maui) [![GitHub stars](https://img.shields.io/github/stars/dotnet/maui?style=flat)](https://github.com/dotnet/maui/stargazers)/[Xamarin.Forms](https://github.com/xamarin/Xamarin.Forms) [![GitHub stars](https://img.shields.io/github/stars/xamarin/Xamarin.Forms?style=flat)](https://github.com/xamarin/Xamarin.Forms/stargazers)                                 |[Fabulous](https://github.com/fabulous-dev/Fabulous) [![GitHub stars](https://img.shields.io/github/stars/fabulous-dev/Fabulous?style=flat)](https://github.com/fabulous-dev/Fabulous/stargazers)                                                                                                                      |
|[MSTest](https://github.com/microsoft/testfx) [![GitHub stars](https://img.shields.io/github/stars/microsoft/testfx?style=flat)](https://github.com/microsoft/testfx/stargazers)/[NUnit](https://github.com/nunit/nunit) [![GitHub stars](https://img.shields.io/github/stars/nunit/nunit?style=flat)](https://github.com/nunit/nunit/stargazers)/[xUnit.net](https://github.com/xunit/xunit) [![GitHub stars](https://img.shields.io/github/stars/xunit/xunit?style=flat)](https://github.com/xunit/xunit/stargazers)|[FsUnit](https://github.com/fsprojects/FsUnit) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FsUnit?style=flat)](https://github.com/fsprojects/FsUnit/stargazers)                                                                                                                            |
|[System.Text.Json](https://github.com/dotnet/runtime/tree/main/src/libraries/System.Text.Json) [![GitHub stars](https://img.shields.io/github/stars/dotnet/runtime/tree/main/src/libraries/System.Text.Json?style=flat)](https://github.com/dotnet/runtime/tree/main/src/libraries/System.Text.Json/stargazers)                                   |[FSharp.SystemTextJson](https://github.com/Tarmil/FSharp.SystemTextJson) [![GitHub stars](https://img.shields.io/github/stars/Tarmil/FSharp.SystemTextJson?style=flat)](https://github.com/Tarmil/FSharp.SystemTextJson/stargazers)                                                                                                  |
|[WPF](https://github.com/dotnet/wpf) [![GitHub stars](https://img.shields.io/github/stars/dotnet/wpf?style=flat)](https://github.com/dotnet/wpf/stargazers)                                                                                             |[Elmish.WPF](https://github.com/elmish/Elmish.WPF) [![GitHub stars](https://img.shields.io/github/stars/elmish/Elmish.WPF?style=flat)](https://github.com/elmish/Elmish.WPF/stargazers)                                                                                                                        |

<!--lint enable double-link -->

## Actor Frameworks

- [Akka.NET](https://github.com/akkadotnet/akka.net) [![GitHub stars](https://img.shields.io/github/stars/akkadotnet/akka.net?style=flat)](https://github.com/akkadotnet/akka.net/stargazers) - Community-driven port of the popular Java/Scala framework Akka to .NET.
- [Akkling](https://github.com/Horusiath/Akkling) [![GitHub stars](https://img.shields.io/github/stars/Horusiath/Akkling?style=flat)](https://github.com/Horusiath/Akkling/stargazers) - F# typed API for Akka.NET.
- [Orleankka](https://github.com/OrleansContrib/Orleankka) [![GitHub stars](https://img.shields.io/github/stars/OrleansContrib/Orleankka?style=flat)](https://github.com/OrleansContrib/Orleankka/stargazers) - Functional extension for Microsoft Orleans framework.
- [Orleans](https://github.com/dotnet/orleans) [![GitHub stars](https://img.shields.io/github/stars/dotnet/orleans?style=flat)](https://github.com/dotnet/orleans/stargazers) - Distributed virtual actor model.
- [Proto.actor](https://github.com/AsynkronIT/protoactor-dotnet) [![GitHub stars](https://img.shields.io/github/stars/AsynkronIT/protoactor-dotnet?style=flat)](https://github.com/AsynkronIT/protoactor-dotnet/stargazers) - Cross-platform actor framework for .NET, Go, Java and Kotlin.

## Build Tools

- [FAKE](https://github.com/fsharp/FAKE) [![GitHub stars](https://img.shields.io/github/stars/fsharp/FAKE?style=flat)](https://github.com/fsharp/FAKE/stargazers) - "F# Make" is a cross platform build automation system.
- [Xake](https://github.com/OlegZee/Xake) [![GitHub stars](https://img.shields.io/github/stars/OlegZee/Xake?style=flat)](https://github.com/OlegZee/Xake/stargazers) - Another Make utility implementation on F#, fully declarative with no-brain parallelism, inspired by Shake.

## Cloud

- [Chia](https://github.com/DanpowerGruppe/Chia) [![GitHub stars](https://img.shields.io/github/stars/DanpowerGruppe/Chia?style=flat)](https://github.com/DanpowerGruppe/Chia/stargazers) - An F# library which contains HelperFunctions for reporting, logging and Azure cloud operations.
- [Farmer](https://github.com/CompositionalIT/farmer) [![GitHub stars](https://img.shields.io/github/stars/CompositionalIT/farmer?style=flat)](https://github.com/CompositionalIT/farmer/stargazers) - Repeatable Azure deployments with ARM templates made easy.
- [FsFirestore](https://github.com/mrbandler/FsFirestore) [![GitHub stars](https://img.shields.io/github/stars/mrbandler/FsFirestore?style=flat)](https://github.com/mrbandler/FsFirestore/stargazers) - Functional F# library to access Firestore database hosted on Google Cloud Platform (GCP) or Firebase.
- [Pulumi.FSharp.Extensions](https://github.com/UnoSD/Pulumi.FSharp.Extensions) [![GitHub stars](https://img.shields.io/github/stars/UnoSD/Pulumi.FSharp.Extensions?style=flat)](https://github.com/UnoSD/Pulumi.FSharp.Extensions/stargazers) - F# computational expressions to reduce boilerplate in Pulumi code.

## Code Analysis
- [Ionide FSharp.Analyzers.SDK](https://github.com/ionide/FSharp.Analyzers.SDK) [![GitHub stars](https://img.shields.io/github/stars/ionide/FSharp.Analyzers.SDK?style=flat)](https://github.com/ionide/FSharp.Analyzers.SDK/stargazers) - Library for building custom analyzers for F# / FSharp.Analyzers.Cli.

## Code Generation

- [Hawaii](https://github.com/Zaid-Ajaj/Hawaii) [![GitHub stars](https://img.shields.io/github/stars/Zaid-Ajaj/Hawaii?style=flat)](https://github.com/Zaid-Ajaj/Hawaii/stargazers) - A dotnet CLI tool to generate type-safe F# clients from OpenAPI/Swagger services.
- [Myriad](https://github.com/MoiraeSoftware/myriad) [![GitHub stars](https://img.shields.io/github/stars/MoiraeSoftware/myriad?style=flat)](https://github.com/MoiraeSoftware/myriad/stargazers) - A pre-compilation code generator.

## Compilers for Other Platforms

- [Fable](https://github.com/fable-compiler/Fable) [![GitHub stars](https://img.shields.io/github/stars/fable-compiler/Fable?style=flat)](https://github.com/fable-compiler/Fable/stargazers) - F# to JavaScript compiler.
- [Fez](https://github.com/kjnilsson/fez) [![GitHub stars](https://img.shields.io/github/stars/kjnilsson/fez?style=flat)](https://github.com/kjnilsson/fez/stargazers) - F# to Erlang compiler.
- [FunScript](https://github.com/ZachBray/FunScript) [![GitHub stars](https://img.shields.io/github/stars/ZachBray/FunScript?style=flat)](https://github.com/ZachBray/FunScript/stargazers) - F# to JavaScript compiler with JQuery etc. mappings through a TypeScript type provider.
- [Juniper](https://github.com/calebh/Juniper) [![GitHub stars](https://img.shields.io/github/stars/calebh/Juniper?style=flat)](https://github.com/calebh/Juniper/stargazers) - Functional Reactive Programming for the Arduino and other microcontrollers.

## Concurrent, Asynchronous, and Parallel Programming

- [FIO](https://github.com/iyyel/fio) [![GitHub stars](https://img.shields.io/github/stars/iyyel/fio?style=flat)](https://github.com/iyyel/fio/stargazers) - A type-safe, highly concurrent and asynchronous library for F# based on pure functional programming.
- [FSharp.Control.AsyncSeq](https://github.com/fsprojects/FSharp.Control.AsyncSeq) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Control.AsyncSeq?style=flat)](https://github.com/fsprojects/FSharp.Control.AsyncSeq/stargazers) - Asynchronous sequence support, integration with `IAsyncEnumerable`.
- [FSharp.Control.FusionTasks](https://github.com/kekyo/FSharp.Control.FusionTasks) [![GitHub stars](https://img.shields.io/github/stars/kekyo/FSharp.Control.FusionTasks?style=flat)](https://github.com/kekyo/FSharp.Control.FusionTasks/stargazers) - F# Async workflow <--> .NET Task/ValueTask easy seamless interoperability library.
- [FSharpx.Async](https://github.com/fsprojects/FSharpx.Async) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharpx.Async?style=flat)](https://github.com/fsprojects/FSharpx.Async/stargazers) - Collection of asynchronous programming utilities for F#.
- [Hopac](https://github.com/Hopac/Hopac) [![GitHub stars](https://img.shields.io/github/stars/Hopac/Hopac?style=flat)](https://github.com/Hopac/Hopac/stargazers) - Concurrent ML style concurrent programming library for F#.
- [IcedTasks](https://github.com/TheAngryByrd/IcedTasks) [![GitHub stars](https://img.shields.io/github/stars/TheAngryByrd/IcedTasks?style=flat)](https://github.com/TheAngryByrd/IcedTasks/stargazers) - Cold tasks, cancellable tasks, and extensions for the `async` workflow.
- [Ply](https://github.com/crowded/ply) [![GitHub stars](https://img.shields.io/github/stars/crowded/ply?style=flat)](https://github.com/crowded/ply/stargazers) - High performance System.Threading.(Value)Task computation expressions for F#.
- [Reaction.AsyncRx](https://github.com/dbrattli/Reaction) [![GitHub stars](https://img.shields.io/github/stars/dbrattli/Reaction?style=flat)](https://github.com/dbrattli/Reaction/stargazers) - An implementation of Async Observables in F# for .NET and Fable.
- [TaskBuilder.fs](https://github.com/rspeele/TaskBuilder.fs) [![GitHub stars](https://img.shields.io/github/stars/rspeele/TaskBuilder.fs?style=flat)](https://github.com/rspeele/TaskBuilder.fs/stargazers) - F# computation expression builder for System.Threading.Tasks.

## Configuration

- [Argu](https://github.com/fsprojects/Argu) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/Argu?style=flat)](https://github.com/fsprojects/Argu/stargazers) - Declarative CLI argument/XML configuration parser for F# applications.
- [FsConfig](https://github.com/demystifyfp/FsConfig) [![GitHub stars](https://img.shields.io/github/stars/demystifyfp/FsConfig?style=flat)](https://github.com/demystifyfp/FsConfig/stargazers) - F# library for reading configuration data from environment variables and AppSettings with type safety.
- [Skid](https://github.com/Meyhem/Skid) [![GitHub stars](https://img.shields.io/github/stars/Meyhem/Skid?style=flat)](https://github.com/Meyhem/Skid/stargazers) - Simple, single-file portable CLI utility for configuration templating.
- [docopt.fs](https://github.com/docopt/docopt.fs/) [![GitHub stars](https://img.shields.io/github/stars/docopt/docopt.fs/?style=flat)](https://github.com/docopt/docopt.fs//stargazers) - Command line arguments parser, F# port of [docopt](https://github.com/docopt/docopt) [![GitHub stars](https://img.shields.io/github/stars/docopt/docopt?style=flat)](https://github.com/docopt/docopt/stargazers).

## Data Science

- [Deedle](https://github.com/BlueMountainCapital/Deedle) [![GitHub stars](https://img.shields.io/github/stars/BlueMountainCapital/Deedle?style=flat)](https://github.com/BlueMountainCapital/Deedle/stargazers) - Exploratory data library for .NET.
- [DiffSharp](https://github.com/DiffSharp/DiffSharp) [![GitHub stars](https://img.shields.io/github/stars/DiffSharp/DiffSharp?style=flat)](https://github.com/DiffSharp/DiffSharp/stargazers) - Functional automatic differentiation (AD) library.
- [FsLab](https://github.com/fslaborg/FsLab) [![GitHub stars](https://img.shields.io/github/stars/fslaborg/FsLab?style=flat)](https://github.com/fslaborg/FsLab/stargazers) - A collection of libraries for data-science. It provides a rapid development environment that lets you write advanced analysis with few lines of production-quality code.
- [IfSharp](https://github.com/fsprojects/IfSharp) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/IfSharp?style=flat)](https://github.com/fsprojects/IfSharp/stargazers) - F# for Jupyter Notebooks.
- [Math.NET Numerics](https://github.com/mathnet/mathnet-numerics) [![GitHub stars](https://img.shields.io/github/stars/mathnet/mathnet-numerics?style=flat)](https://github.com/mathnet/mathnet-numerics/stargazers) - Methods and algorithms for numerical computations in science, engineering and every day use. F# specific bindings available.
- [Math.NET Symbolics](https://github.com/mathnet/mathnet-symbolics/) [![GitHub stars](https://img.shields.io/github/stars/mathnet/mathnet-symbolics/?style=flat)](https://github.com/mathnet/mathnet-symbolics//stargazers) - A basic open source computer algebra library for .NET, Silverlight and Mono written entirely in F#.
- [SIMDArray](https://github.com/jackmott/SIMDArray) [![GitHub stars](https://img.shields.io/github/stars/jackmott/SIMDArray?style=flat)](https://github.com/jackmott/SIMDArray/stargazers) - SIMD enhanced Array extensions for faster computation.
- [Synapses](https://github.com/mrdimosthenis/Synapses) [![GitHub stars](https://img.shields.io/github/stars/mrdimosthenis/Synapses?style=flat)](https://github.com/mrdimosthenis/Synapses/stargazers) - Neural network library in F#.
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) [![GitHub stars](https://img.shields.io/github/stars/BayesWitnesses/m2cgen?style=flat)](https://github.com/BayesWitnesses/m2cgen/stargazers) - A CLI tool to transpile trained classic ML models into a native F# code with zero dependencies.

## Development Tools

### IDE

- [F# Playground](https://github.com/Seng-Jik/FSharpPlayground) [![GitHub stars](https://img.shields.io/github/stars/Seng-Jik/FSharpPlayground?style=flat)](https://github.com/Seng-Jik/FSharpPlayground/stargazers) - Minimal playground for F#.
- [JetBrains Rider](https://www.jetbrains.com/rider) - Cross-platform .NET IDE with F# support (Proprietary, free for non-commercial use).
- [MonoDevelop](http://www.monodevelop.com/) - Cross-platform IDE mostly aimed at Mono/.NET developers.
- [Visual Studio](https://www.visualstudio.com/) - IDE from Microsoft with first class F# support (Windows only, Proprietary).

### Editor Plugins

- [Emacs F# mode](https://github.com/fsharp/emacs-fsharp-mode) [![GitHub stars](https://img.shields.io/github/stars/fsharp/emacs-fsharp-mode?style=flat)](https://github.com/fsharp/emacs-fsharp-mode/stargazers) - F# support in Emacs (including Intellisense and Interactive mode).
- [FSharpFar](https://github.com/nightroman/FarNet) [![GitHub stars](https://img.shields.io/github/stars/nightroman/FarNet?style=flat)](https://github.com/nightroman/FarNet/stargazers) - F# support for Far Manager.
- [FSharpLint](https://github.com/fsprojects/FSharpLint) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharpLint?style=flat)](https://github.com/fsprojects/FSharpLint/stargazers) - F# code linter.
- [Fantomas](https://github.com/fsprojects/fantomas) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/fantomas?style=flat)](https://github.com/fsprojects/fantomas/stargazers) - F# code formatter.
- [Ionide](http://ionide.io/) - Atom Editor and Visual Studio Code package suite for cross platform F# development.
- [Vim F#](https://github.com/fsharp/vim-fsharp) [![GitHub stars](https://img.shields.io/github/stars/fsharp/vim-fsharp?style=flat)](https://github.com/fsharp/vim-fsharp/stargazers) - F# support for Vim.
- [VimSpeak](https://github.com/AshleyF/VimSpeak) [![GitHub stars](https://img.shields.io/github/stars/AshleyF/VimSpeak?style=flat)](https://github.com/AshleyF/VimSpeak/stargazers) - A tool to control Vim with your voice using speech recognition.
- [fsharp-notebook](https://github.com/pablofrommars/fsharp-notebook) [![GitHub stars](https://img.shields.io/github/stars/pablofrommars/fsharp-notebook?style=flat)](https://github.com/pablofrommars/fsharp-notebook/stargazers) - Data science notebook for F# Interactive.
- [neofsharp.vim](https://github.com/adelarsq/neofsharp.vim) [![GitHub stars](https://img.shields.io/github/stars/adelarsq/neofsharp.vim?style=flat)](https://github.com/adelarsq/neofsharp.vim/stargazers) - Basic F# support for (Neo)Vim.

### Performance Analysis

- [fasm](https://github.com/d-edge/fasm) [![GitHub stars](https://img.shields.io/github/stars/d-edge/fasm?style=flat)](https://github.com/d-edge/fasm/stargazers) - F# JIT disassembler, as a dotnet tool.

## General Purpose Libraries

- [Aether](https://github.com/xyncro/aether) [![GitHub stars](https://img.shields.io/github/stars/xyncro/aether?style=flat)](https://github.com/xyncro/aether/stargazers) - Optics library for F#, similar to the Haskell Data.Lens package.
- [Chessie](https://github.com/fsprojects/Chessie) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/Chessie?style=flat)](https://github.com/fsprojects/Chessie/stargazers) - Railway-oriented programming.
- [Donald](https://github.com/pimbrouwers/Donald) [![GitHub stars](https://img.shields.io/github/stars/pimbrouwers/Donald?style=flat)](https://github.com/pimbrouwers/Donald/stargazers) - A simple F# interface for ADO.NET.
- [DustyTables](https://github.com/Zaid-Ajaj/DustyTables) [![GitHub stars](https://img.shields.io/github/stars/Zaid-Ajaj/DustyTables?style=flat)](https://github.com/Zaid-Ajaj/DustyTables/stargazers) - Thin F# API for SqlClient for easy data access to ms sql server with functional seasoning on top.
- [ExtCore](https://github.com/jack-pappas/ExtCore) [![GitHub stars](https://img.shields.io/github/stars/jack-pappas/ExtCore?style=flat)](https://github.com/jack-pappas/ExtCore/stargazers) - Extended core library for F#.
- [FSharp.CosmosDb](https://github.com/aaronpowell/fsharp.cosmosdb) [![GitHub stars](https://img.shields.io/github/stars/aaronpowell/fsharp.cosmosdb?style=flat)](https://github.com/aaronpowell/fsharp.cosmosdb/stargazers) - An F# wrapper around the CosmosDB SDK, making it more functional-friendly.
- [FSharp.HashCollections](https://github.com/mvkara/fsharp-hashcollections) [![GitHub stars](https://img.shields.io/github/stars/mvkara/fsharp-hashcollections?style=flat)](https://github.com/mvkara/fsharp-hashcollections/stargazers) - Fast hash-based immutable map and set.
- [FSharpLu](https://github.com/Microsoft/fsharplu) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/fsharplu?style=flat)](https://github.com/Microsoft/fsharplu/stargazers) - Lightweight utilities for string manipulations, logging, collection data structures, file operations, text processing, security, async, parsing, diagnostics, configuration files and Json serialization.
- [FSharpPlus](https://github.com/gmpl/FSharpPlus) [![GitHub stars](https://img.shields.io/github/stars/gmpl/FSharpPlus?style=flat)](https://github.com/gmpl/FSharpPlus/stargazers) - Extensions for F#.
- [FSharpx.Extras](https://github.com/fsprojects/FSharpx.Extras) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharpx.Extras?style=flat)](https://github.com/fsprojects/FSharpx.Extras/stargazers) - A collection of libraries and tools for use with F#.
- [Fli](https://github.com/CaptnCodr/Fli) [![GitHub stars](https://img.shields.io/github/stars/CaptnCodr/Fli?style=flat)](https://github.com/CaptnCodr/Fli/stargazers) - Computational expression to run system processes and manage their output. 
- [Fling](https://github.com/cmeeren/Fling) [![GitHub stars](https://img.shields.io/github/stars/cmeeren/Fling?style=flat)](https://github.com/cmeeren/Fling/stargazers) - Significantly reduces boilerplate needed to efficiently save/load complex domain entities to/from multiple tables.
- [FsToolkit.ErrorHandling](https://github.com/demystifyfp/FsToolkit.ErrorHandling) [![GitHub stars](https://img.shields.io/github/stars/demystifyfp/FsToolkit.ErrorHandling?style=flat)](https://github.com/demystifyfp/FsToolkit.ErrorHandling/stargazers) - Clear, simple and powerful error handling with railway-oriented programming. Inspired by Chessie.
- [Fumble](https://github.com/tforkmann/Fumble) [![GitHub stars](https://img.shields.io/github/stars/tforkmann/Fumble?style=flat)](https://github.com/tforkmann/Fumble/stargazers) - Thin F# API for SQLite for easy data access to SQLite database with functional seasoning on top.
- [LiteDB.FSharp](https://github.com/Zaid-Ajaj/LiteDB.FSharp) [![GitHub stars](https://img.shields.io/github/stars/Zaid-Ajaj/LiteDB.FSharp?style=flat)](https://github.com/Zaid-Ajaj/LiteDB.FSharp/stargazers) - F# Support for [LiteDB](https://github.com/mbdavid/LiteDB) [![GitHub stars](https://img.shields.io/github/stars/mbdavid/LiteDB?style=flat)](https://github.com/mbdavid/LiteDB/stargazers), an embedded single file database for .NET.
- [Npgsql.FSharp](https://github.com/Zaid-Ajaj/Npgsql.FSharp) [![GitHub stars](https://img.shields.io/github/stars/Zaid-Ajaj/Npgsql.FSharp?style=flat)](https://github.com/Zaid-Ajaj/Npgsql.FSharp/stargazers) - Thin F# wrapper around [Npgsql](https://github.com/npgsql/npgsql) [![GitHub stars](https://img.shields.io/github/stars/npgsql/npgsql?style=flat)](https://github.com/npgsql/npgsql/stargazers), the PostgreSQL database driver.
- [SqlHydra](https://github.com/JordanMarr/SqlHydra) [![GitHub stars](https://img.shields.io/github/stars/JordanMarr/SqlHydra?style=flat)](https://github.com/JordanMarr/SqlHydra/stargazers) - Suite of NuGet packages for working with databases in F# including query expressions and code generation tools (for generating strongly typed F# DTO record types based on your database tables). Supports MySQL, PostgreSQL, Oracle, SQL Server, and SQLite.
- [TypeShape](https://github.com/eiriktsarpalis/TypeShape) [![GitHub stars](https://img.shields.io/github/stars/eiriktsarpalis/TypeShape?style=flat)](https://github.com/eiriktsarpalis/TypeShape/stargazers) - Small, extensible F# library for practical generic programming.
- [Validus](https://github.com/pimbrouwers/Validus) [![GitHub stars](https://img.shields.io/github/stars/pimbrouwers/Validus?style=flat)](https://github.com/pimbrouwers/Validus/stargazers) - A composable validation library for F#, with built-in validators for most primitive types and easily extended through custom validators.
- [Vp.FSharp.Sql](https://github.com/veepee-oss/Vp.FSharp.Sql) [![GitHub stars](https://img.shields.io/github/stars/veepee-oss/Vp.FSharp.Sql?style=flat)](https://github.com/veepee-oss/Vp.FSharp.Sql/stargazers) - Generic F# ADO provider wrapper (SqlServer, PostgreSQL, SQLite).

## Game Development

- [FsUnity](https://github.com/FsUnity) [![GitHub stars](https://img.shields.io/github/stars/FsUnity?style=flat)](https://github.com/FsUnity/stargazers) - F# libraries, tools, and plugins for the Unity game engine.
- [Garnet](https://github.com/bcarruthers/garnet) [![GitHub stars](https://img.shields.io/github/stars/bcarruthers/garnet?style=flat)](https://github.com/bcarruthers/garnet/stargazers) - Lightweight game composition library for F# with entity-component-system (ECS) and actor-like messaging features.
- [Godot](https://www.lkokemohr.de/fsharp_godot.html) - Tutorial how to use F# with Godot. 
- [Nu Game Engine](https://github.com/bryanedds/Nu) [![GitHub stars](https://img.shields.io/github/stars/bryanedds/Nu?style=flat)](https://github.com/bryanedds/Nu/stargazers) - Cross-platform F# 2D game engine built in the functional style. Uses SDL2 and Farseer Physics.

## GUI
<!--lint disable double-link -->
- [Avalonia.FuncUI](https://github.com/fsprojects/Avalonia.FuncUI) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/Avalonia.FuncUI?style=flat)](https://github.com/fsprojects/Avalonia.FuncUI/stargazers) - Develop cross-platform MVU GUI Applications using F# and Avalonia.
- [Elmish.WPF](https://github.com/elmish/Elmish.WPF) [![GitHub stars](https://img.shields.io/github/stars/elmish/Elmish.WPF?style=flat)](https://github.com/elmish/Elmish.WPF/stargazers) - Elmish (or MVU) approach to WPF programming.
- [Epoxy](https://github.com/kekyo/epoxy) [![GitHub stars](https://img.shields.io/github/stars/kekyo/epoxy?style=flat)](https://github.com/kekyo/epoxy/stargazers) - An independent flexible XAML MVVM library for .NET.
- [Fabulous](https://github.com/fabulous-dev/Fabulous) [![GitHub stars](https://img.shields.io/github/stars/fabulous-dev/Fabulous?style=flat)](https://github.com/fabulous-dev/Fabulous/stargazers) - F# functional app development, using declarative dynamic UI.
<!--lint enable double-link -->

## HTTP Clients

- [FsHttp](https://github.com/ronaldschlenker/FsHttp) [![GitHub stars](https://img.shields.io/github/stars/ronaldschlenker/FsHttp?style=flat)](https://github.com/ronaldschlenker/FsHttp/stargazers) - A convenient library for consuming HTTP/REST endpoints via F#.
- [Http.fs](https://github.com/haf/Http.fs) [![GitHub stars](https://img.shields.io/github/stars/haf/Http.fs?style=flat)](https://github.com/haf/Http.fs/stargazers) - A simple, functional HTTP client library for F#.
- [Oryx](https://github.com/cognitedata/oryx) [![GitHub stars](https://img.shields.io/github/stars/cognitedata/oryx?style=flat)](https://github.com/cognitedata/oryx/stargazers) - A high performance .NET cross-platform functional HTTP request handler library for writing HTTP clients and orchestrating web requests.

## Logging

- [FsLibLog](https://github.com/TheAngryByrd/FsLibLog) [![GitHub stars](https://img.shields.io/github/stars/TheAngryByrd/FsLibLog?style=flat)](https://github.com/TheAngryByrd/FsLibLog/stargazers) - A single file you can copy and paste or add through Paket GitHub dependencies to provide your F# library with a logging abstraction.
- [Logary](https://github.com/logary/logary/) [![GitHub stars](https://img.shields.io/github/stars/logary/logary/?style=flat)](https://github.com/logary/logary//stargazers) - High performance, multi-target logging, metric, tracing and health-check library for mono and .NET.

## Package Management

- [NuGet](https://www.nuget.org/) - The package manager for the Microsoft development platform including .NET.
- [Paket](https://github.com/fsprojects/Paket) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/Paket?style=flat)](https://github.com/fsprojects/Paket/stargazers) - Dependency manager for .NET with support for NuGet packages and Git repositories.

## Parsing

- [FParsec](https://github.com/stephan-tolksdorf/fparsec) [![GitHub stars](https://img.shields.io/github/stars/stephan-tolksdorf/fparsec?style=flat)](https://github.com/stephan-tolksdorf/fparsec/stargazers) - The parser combinator library for F#.
- [FsAttoparsec](https://github.com/haf/FsAttoparsec) [![GitHub stars](https://img.shields.io/github/stars/haf/FsAttoparsec?style=flat)](https://github.com/haf/FsAttoparsec/stargazers) - Port of Bryan O'Sullivan's attoparsec from Haskell to F#.
- [XParsec](https://github.com/corsis/XParsec) [![GitHub stars](https://img.shields.io/github/stars/corsis/XParsec?style=flat)](https://github.com/corsis/XParsec/stargazers) - Extensible, type-and-source-polymorphic, non-linear applicative parser combinator library for F# 3.0 and 4.0.

## Serialization
<!--lint disable double-link -->
- [FSharp.Json](https://github.com/vsapronov/FSharp.Json) [![GitHub stars](https://img.shields.io/github/stars/vsapronov/FSharp.Json?style=flat)](https://github.com/vsapronov/FSharp.Json/stargazers) - Reflection-based serialization library.
- [FSharp.SystemTextJson](https://github.com/Tarmil/FSharp.SystemTextJson) [![GitHub stars](https://img.shields.io/github/stars/Tarmil/FSharp.SystemTextJson?style=flat)](https://github.com/Tarmil/FSharp.SystemTextJson/stargazers) - System.Text.Json extensions for F# types.
- [Fleece](https://github.com/mausch/Fleece) [![GitHub stars](https://img.shields.io/github/stars/mausch/Fleece?style=flat)](https://github.com/mausch/Fleece/stargazers) - JSON mapper for F#. It simplifies mapping from a Json library's JsonValue onto your types, and mapping from your types onto JsonValue.
- [FsCodec](https://github.com/jet/FsCodec) [![GitHub stars](https://img.shields.io/github/stars/jet/FsCodec?style=flat)](https://github.com/jet/FsCodec/stargazers) - F# Event-Union Contract Encoding with versioning tolerant converters.
- [FsPickler](https://github.com/mbraceproject/FsPickler) [![GitHub stars](https://img.shields.io/github/stars/mbraceproject/FsPickler?style=flat)](https://github.com/mbraceproject/FsPickler/stargazers) - Fast, multi-format messaging serializer for .NET.
- [Legivel](https://github.com/fjoppe/Legivel) [![GitHub stars](https://img.shields.io/github/stars/fjoppe/Legivel?style=flat)](https://github.com/fjoppe/Legivel/stargazers) - F# Yaml 1.2 parser.
- [Thoth.Json](https://thoth-org.github.io/Thoth.Json/) - JSON encoder/decoder library inspired by Elm.
<!--lint enable double-link -->

## Simulation
 
- [F# RISC-V Instruction Set formal specification](https://github.com/mrLSD/riscv-fs) [![GitHub stars](https://img.shields.io/github/stars/mrLSD/riscv-fs?style=flat)](https://github.com/mrLSD/riscv-fs/stargazers) - RISC-V CPU formal ISA Specification. RISC-V CPU simulator with ELF files execution.

## Static Site Generators

- [SkunkHTML](https://github.com/mg0x7BE/skunk-html) [![GitHub stars](https://img.shields.io/github/stars/mg0x7BE/skunk-html?style=flat)](https://github.com/mg0x7BE/skunk-html/stargazers) - Markdown blog with GitHub Pages.

## Testing
<!--lint disable double-link -->
- [Expecto](https://github.com/haf/expecto) [![GitHub stars](https://img.shields.io/github/stars/haf/expecto?style=flat)](https://github.com/haf/expecto/stargazers) - Smooth testing framework for F# with tests-as-values and parallelism by default.
- [Faqt](https://github.com/cmeeren/Faqt) [![GitHub stars](https://img.shields.io/github/stars/cmeeren/Faqt?style=flat)](https://github.com/cmeeren/Faqt/stargazers) - Fantastic fluent assertions for your F# tests and domain code.
- [FsCheck](https://github.com/fscheck/FsCheck) [![GitHub stars](https://img.shields.io/github/stars/fscheck/FsCheck?style=flat)](https://github.com/fscheck/FsCheck/stargazers) - Random testing for .NET.
- [FsUnit](https://github.com/fsprojects/FsUnit) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FsUnit?style=flat)](https://github.com/fsprojects/FsUnit/stargazers) - Makes unit-testing with F# more enjoyable. It adds a special syntax to your favorite .NET testing framework.
- [NBomber](https://github.com/PragmaticFlow/NBomber) [![GitHub stars](https://img.shields.io/github/stars/PragmaticFlow/NBomber?style=flat)](https://github.com/PragmaticFlow/NBomber/stargazers) - Simple load testing framework for Pull and Push scenarios.
- [Persimmon](https://github.com/persimmon-projects/Persimmon) [![GitHub stars](https://img.shields.io/github/stars/persimmon-projects/Persimmon?style=flat)](https://github.com/persimmon-projects/Persimmon/stargazers) - Unit test framework for F# using computation expressions.
- [altcover](https://github.com/SteveGilham/altcover) [![GitHub stars](https://img.shields.io/github/stars/SteveGilham/altcover?style=flat)](https://github.com/SteveGilham/altcover/stargazers) - Cross-platform coverage gathering and processing tool set for .NET/.NET core and Mono.
- [canopy](https://github.com/lefthandedgoat/canopy) [![GitHub stars](https://img.shields.io/github/stars/lefthandedgoat/canopy?style=flat)](https://github.com/lefthandedgoat/canopy/stargazers) - F# web automation and testing framework.
- [fsharp-hedgehog](https://github.com/hedgehogqa/fsharp-hedgehog) [![GitHub stars](https://img.shields.io/github/stars/hedgehogqa/fsharp-hedgehog?style=flat)](https://github.com/hedgehogqa/fsharp-hedgehog/stargazers) - Property-based testing system for F#.
- [unquote](https://github.com/swensensoftware/unquote) [![GitHub stars](https://img.shields.io/github/stars/swensensoftware/unquote?style=flat)](https://github.com/swensensoftware/unquote/stargazers) - Write F# unit test assertions as quoted expressions.
- [xUnit.net](https://xunit.net/) - Free, open source, community-focused unit testing tool for the .NET Framework.
<!--lint enable double-link -->

## Type Providers

- [AzureStorageTypeProvider](https://github.com/fsprojects/AzureStorageTypeProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/AzureStorageTypeProvider?style=flat)](https://github.com/fsprojects/AzureStorageTypeProvider/stargazers) - F# Azure type provider which can be used to explore Blob, Table and Queue Azure Storage assets and easily apply CRUD operations on them.
- [DynamicsCRMProvider](https://github.com/fsprojects/DynamicsCRMProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/DynamicsCRMProvider?style=flat)](https://github.com/fsprojects/DynamicsCRMProvider/stargazers) - Type provider for Microsoft Dynamics CRM 2011.
- [EasyBuild.FileSystemProvider](https://github.com/easybuild-org/EasyBuild.FileSystemProvider) [![GitHub stars](https://img.shields.io/github/stars/easybuild-org/EasyBuild.FileSystemProvider?style=flat)](https://github.com/easybuild-org/EasyBuild.FileSystemProvider/stargazers) - Type provider to provide a typed representation of files and directories based on your project structure or a virtual file system.
- [ExcelProvider](https://github.com/fsprojects/ExcelProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/ExcelProvider?style=flat)](https://github.com/fsprojects/ExcelProvider/stargazers) - Excel type provider.
- [FSharp.Configuration](https://github.com/fsprojects/FSharp.Configuration) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Configuration?style=flat)](https://github.com/fsprojects/FSharp.Configuration/stargazers) - The project contains type providers for the configuration of .NET projects. Handles AppSettings, ResX, Yaml and Ini files.
- [FSharp.Data.Npgsql](https://github.com/demetrixbio/FSharp.Data.Npgsql) [![GitHub stars](https://img.shields.io/github/stars/demetrixbio/FSharp.Data.Npgsql?style=flat)](https://github.com/demetrixbio/FSharp.Data.Npgsql/stargazers) - F# type providers library on a top of well-known Npgsql ADO.NET client library.
- [FSharp.Data.SqlClient](https://github.com/fsprojects/FSharp.Data.SqlClient) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Data.SqlClient?style=flat)](https://github.com/fsprojects/FSharp.Data.SqlClient/stargazers) - F# type provider for statically typed access to T-SQL command parameters and result set.
- [FSharp.Data.Tdms](https://github.com/mettekou/FSharp.Data.Tdms) [![GitHub stars](https://img.shields.io/github/stars/mettekou/FSharp.Data.Tdms?style=flat)](https://github.com/mettekou/FSharp.Data.Tdms/stargazers) - TDMS support for F#.
- [FSharp.Data.Toolbox](https://github.com/fsprojects/FSharp.Data.Toolbox) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Data.Toolbox?style=flat)](https://github.com/fsprojects/FSharp.Data.Toolbox/stargazers) - Library for various data access APIs based on FSharp.Data. The library currently includes the Twitter type provider for access to Twitter users and feeds, and SAS type provider to read SAS dataset files.
- [FSharp.Data.TypeProviders](https://github.com/fsprojects/FSharp.Data.TypeProviders) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Data.TypeProviders?style=flat)](https://github.com/fsprojects/FSharp.Data.TypeProviders/stargazers) - Library that contains type providers for `.edmx` files, `.dbml` files, WSDL services, OData services, and SQL databases.
- [FSharp.Data](https://github.com/fsharp/FSharp.Data) [![GitHub stars](https://img.shields.io/github/stars/fsharp/FSharp.Data?style=flat)](https://github.com/fsharp/FSharp.Data/stargazers) - Data science library that contains type providers for CSV, HTML, JSON, XML, and WorldBank data.
- [FSharp.Management](https://github.com/fsprojects/FSharp.Management) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Management?style=flat)](https://github.com/fsprojects/FSharp.Management/stargazers) - The project contains various type providers for the management of the machine. Handles file system, registry,  Windows Management Instrumentation, PowerShell and SystemTimeZones.
- [FSharp.Text.RegexProvider](https://github.com/fsprojects/FSharp.Text.RegexProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.Text.RegexProvider?style=flat)](https://github.com/fsprojects/FSharp.Text.RegexProvider/stargazers) - Type provider for regular expressions.
- [Facil](https://github.com/cmeeren/Facil) [![GitHub stars](https://img.shields.io/github/stars/cmeeren/Facil?style=flat)](https://github.com/cmeeren/Facil/stargazers) - Generates F# data access source code from SQL queries and stored procedures.
- [FsXaml](https://github.com/fsprojects/FsXaml) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FsXaml?style=flat)](https://github.com/fsprojects/FsXaml/stargazers) - F# Tools for working with XAML Projects.
- [FsYaml](https://github.com/bleis-tift/FsYaml) [![GitHub stars](https://img.shields.io/github/stars/bleis-tift/FsYaml?style=flat)](https://github.com/bleis-tift/FsYaml/stargazers) - Typed Yaml library for F#.
- [GraphProvider](https://github.com/fsprojects/GraphProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/GraphProvider?style=flat)](https://github.com/fsprojects/GraphProvider/stargazers) - `.dgml` state machine type provider.
- [MatDataProvider](https://github.com/fsprojects/matprovider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/matprovider?style=flat)](https://github.com/fsprojects/matprovider/stargazers) - Erased type provider for `.mat` files (binary MATLAB format files).
- [R Type Provider](https://github.com/BlueMountainCapital/FSharpRProvider) [![GitHub stars](https://img.shields.io/github/stars/BlueMountainCapital/FSharpRProvider?style=flat)](https://github.com/BlueMountainCapital/FSharpRProvider/stargazers) - Type provider to interop with R.
- [Rezoom.SQL](https://github.com/rspeele/Rezoom.SQL) [![GitHub stars](https://img.shields.io/github/stars/rspeele/Rezoom.SQL?style=flat)](https://github.com/rspeele/Rezoom.SQL/stargazers) - Statically typed SQL for F#.
- [S3Provider](https://github.com/fsprojects/S3Provider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/S3Provider?style=flat)](https://github.com/fsprojects/S3Provider/stargazers) - Experimental type provider for Amazon S3.
- [SQLProvider](https://github.com/fsprojects/SQLProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/SQLProvider?style=flat)](https://github.com/fsprojects/SQLProvider/stargazers) - General F# SQL database erasing type provider, supporting LINQ queries, schema exploration, individuals, CRUD operations and much more besides.
- [SwaggerProvider](https://github.com/fsprojects/SwaggerProvider) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/SwaggerProvider?style=flat)](https://github.com/fsprojects/SwaggerProvider/stargazers) - Generative type provider for Swagger.

### Creating Type Providers

- [FSharp.TypeProviders.StarterPack](https://github.com/fsprojects/FSharp.TypeProviders.StarterPack) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/FSharp.TypeProviders.StarterPack?style=flat)](https://github.com/fsprojects/FSharp.TypeProviders.StarterPack/stargazers) - The ProvidedTypes SDK for creating F# type providers.

## Visualization

- [FSharp.Charting](https://github.com/fslaborg/FSharp.Charting) [![GitHub stars](https://img.shields.io/github/stars/fslaborg/FSharp.Charting?style=flat)](https://github.com/fslaborg/FSharp.Charting/stargazers) - Charting library suitable for interactive F# scripting.
- [GG.Net](https://github.com/pablofrommars/GGNet) [![GitHub stars](https://img.shields.io/github/stars/pablofrommars/GGNet?style=flat)](https://github.com/pablofrommars/GGNet/stargazers) - Visualization library for data scientists.
- [Plotly.NET](https://github.com/plotly/Plotly.NET) [![GitHub stars](https://img.shields.io/github/stars/plotly/Plotly.NET?style=flat)](https://github.com/plotly/Plotly.NET/stargazers) - A Plotly-based general purpose plotting library for F#.
- [SharpVG](https://github.com/ChrisNikkel/SharpVG) [![GitHub stars](https://img.shields.io/github/stars/ChrisNikkel/SharpVG?style=flat)](https://github.com/ChrisNikkel/SharpVG/stargazers) - Create SVG vector graphics in F#.
- [XPlot](https://github.com/fslaborg/XPlot) [![GitHub stars](https://img.shields.io/github/stars/fslaborg/XPlot?style=flat)](https://github.com/fslaborg/XPlot/stargazers) - A plotting library for the F# programming language.

## Web Frameworks
<!--lint disable double-link -->
- [Bolero](https://github.com/fsbolero/Bolero/) [![GitHub stars](https://img.shields.io/github/stars/fsbolero/Bolero/?style=flat)](https://github.com/fsbolero/Bolero//stargazers) - F# in WebAssembly, develop SPAs with the full power of F# and .NET Blazor.
- [Falco](https://github.com/pimbrouwers/Falco/) [![GitHub stars](https://img.shields.io/github/stars/pimbrouwers/Falco/?style=flat)](https://github.com/pimbrouwers/Falco//stargazers) - A functional-first toolkit for building brilliant ASP.NET Core applications using F#.
- [Felicity](https://github.com/cmeeren/Felicity) [![GitHub stars](https://img.shields.io/github/stars/cmeeren/Felicity?style=flat)](https://github.com/cmeeren/Felicity/stargazers) - Boilerplate-free, idiomatic JSON:API for your beautiful, idiomatic F# domain model.
- [Feliz](https://github.com/Zaid-Ajaj/Feliz) [![GitHub stars](https://img.shields.io/github/stars/Zaid-Ajaj/Feliz?style=flat)](https://github.com/Zaid-Ajaj/Feliz/stargazers) - A fresh retake of the React API in Fable and a collection of high-quality components to build React applications in F#.
- [Genit](https://github.com/lefthandedgoat/genit) [![GitHub stars](https://img.shields.io/github/stars/lefthandedgoat/genit?style=flat)](https://github.com/lefthandedgoat/genit/stargazers) - Cross-platform website generator and server using F#, Suave and PostgreSQL or MS SQL Server.
- [Giraffe](https://github.com/giraffe-fsharp/Giraffe) [![GitHub stars](https://img.shields.io/github/stars/giraffe-fsharp/Giraffe?style=flat)](https://github.com/giraffe-fsharp/Giraffe/stargazers) - Native functional ASP.NET Core web framework for F# developers.
- [Oxpecker](https://github.com/Lanayx/Oxpecker) [![GitHub stars](https://img.shields.io/github/stars/Lanayx/Oxpecker?style=flat)](https://github.com/Lanayx/Oxpecker/stargazers) - ASP.NET Core based F# framework + supporting tools (ViewEngine, Htmx, OpenApi).
- [Saturn](https://github.com/SaturnFramework/Saturn) [![GitHub stars](https://img.shields.io/github/stars/SaturnFramework/Saturn?style=flat)](https://github.com/SaturnFramework/Saturn/stargazers) - Opinionated, web development framework for F# which implements the server-side, functional MVC pattern.
- [Suave](https://github.com/SuaveIO/suave) [![GitHub stars](https://img.shields.io/github/stars/SuaveIO/suave?style=flat)](https://github.com/SuaveIO/suave/stargazers) - A simple web development F# library providing a lightweight web server and a set of combinators to manipulate route flow and task composition.
- [WebSharper](https://github.com/intellifactory/websharper) [![GitHub stars](https://img.shields.io/github/stars/intellifactory/websharper?style=flat)](https://github.com/intellifactory/websharper/stargazers) - F#-based web programming platform including a compiler from F# code to JavaScript.
<!--lint enable double-link -->

## .NET Core Templates
<!--lint disable awesome-list-item-->
- [ASP.NET Core WebAPI F# Template](https://github.com/MNie/FSharpNetCoreWebApiTemplate) [![GitHub stars](https://img.shields.io/github/stars/MNie/FSharpNetCoreWebApiTemplate?style=flat)](https://github.com/MNie/FSharpNetCoreWebApiTemplate/stargazers) - `dotnet new -i WebAPI.FSharp.Template::*`
- [Expecto Template](https://github.com/MNie/Expecto.Template) [![GitHub stars](https://img.shields.io/github/stars/MNie/Expecto.Template?style=flat)](https://github.com/MNie/Expecto.Template/stargazers) - `dotnet new -i Expecto.Template::*`
- [Fable, F# |> Babel](http://fable.io) - `dotnet new -i Fable.Template::*`
- [Fable-elmish](https://github.com/fable-compiler/fable-elmish) [![GitHub stars](https://img.shields.io/github/stars/fable-compiler/fable-elmish?style=flat)](https://github.com/fable-compiler/fable-elmish/stargazers) - `dotnet new -i Fable.Template.Elmish.React::*`
- [Giraffe Template](https://github.com/giraffe-fsharp/giraffe-template) [![GitHub stars](https://img.shields.io/github/stars/giraffe-fsharp/giraffe-template?style=flat)](https://github.com/giraffe-fsharp/giraffe-template/stargazers) - `dotnet new -i "giraffe-template::*"`
- [MiniScaffold](https://github.com/TheAngryByrd/MiniScaffold) [![GitHub stars](https://img.shields.io/github/stars/TheAngryByrd/MiniScaffold?style=flat)](https://github.com/TheAngryByrd/MiniScaffold/stargazers) - F# Template for creating and publishing libraries targeting .NET Full (net45) and Core (netstandard1.6), `dotnet new -i MiniScaffold::*`
- [NancyFx Template](https://github.com/MNie/NancyFxCore) [![GitHub stars](https://img.shields.io/github/stars/MNie/NancyFxCore?style=flat)](https://github.com/MNie/NancyFxCore/stargazers) - `dotnet new -i NancyFx.Core.Template::*`
- [SAFE Stack Template](https://github.com/SAFE-Stack/SAFE-template) [![GitHub stars](https://img.shields.io/github/stars/SAFE-Stack/SAFE-template?style=flat)](https://github.com/SAFE-Stack/SAFE-template/stargazers) - `dotnet new -i SAFE.Template::*`
<!--lint enable awesome-list-item-->

## Resources

### Blogs

- [.NET Blog (F# tag)](https://devblogs.microsoft.com/dotnet/tag/f/) - News and discussions about F# from the .NET team.
- [Codesuji](https://codesuji.com) - A community member blog, focusing on functional aspects on F#.
- [Krzysztof Cieslak](https://kcieslak.io/) - A blog of the Ionide maintainer. 
- [Mark Seemann](https://blog.ploeh.dk/) - A blog discussing various aspects of software design.
- [Sergey Tihon (F# Weekly)](https://sergeytihon.com/) - Weekly newsletter collected across the ecosystem.
- [Tomas Petricek](http://tomasp.net/blog/) - A well-known community member working on a diverse set of topics.

### Books

- [Domain Modeling Made Functional by Scott Wlaschin](https://pragprog.com/titles/swdddf/domain-modeling-made-functional/) - Tackle software complexity with domain-driven design and F#.
- [F# in Action by Isaac Abraham](https://www.manning.com/books/f-sharp-in-action) - A practical guide in software development in F#.

### Cheatsheets

- [F# Snips](https://fssnip.net/) - Share your snippets of F# code.
- [F# cheatsheet](https://fsprojects.github.io/fsharp-cheatsheet/) - Quick reference for the main language features.
- [F# tour](https://docs.microsoft.com/en-us/dotnet/articles/fsharp/tour) - Official language tour from Microsoft.
- [Guide for C# devs to learn F#](https://github.com/knocte/2fsharp/blob/master/csharp2fsharp.md) [![GitHub stars](https://img.shields.io/github/stars/knocte/2fsharp/blob/master/csharp2fsharp.md?style=flat)](https://github.com/knocte/2fsharp/blob/master/csharp2fsharp.md/stargazers) - A 30-minute F# tutorial for C# programmers, with back-to-back code snippets.
- [Guide for Python devs to learn F#](https://github.com/knocte/2fsharp/blob/master/python2fsharp.md) [![GitHub stars](https://img.shields.io/github/stars/knocte/2fsharp/blob/master/python2fsharp.md?style=flat)](https://github.com/knocte/2fsharp/blob/master/python2fsharp.md/stargazers) - A 30-minute F# tutorial for Python programmers, with back-to-back code snippets.
- [Guide for Rust devs to learn F#](https://github.com/Dhghomon/rust-fsharp) [![GitHub stars](https://img.shields.io/github/stars/Dhghomon/rust-fsharp?style=flat)](https://github.com/Dhghomon/rust-fsharp/stargazers) - Informal manual for users of Rust and F# to read through to learn about the other language. 
- [Learn F# in Y minutes](https://learnxinyminutes.com/docs/fsharp) - A guide recommended to quickly start programming in F#.

### Community

- [Amplifying F#](https://amplifyingfsharp.io)
- [F# on BlueSky](https://bsky.app/hashtag/fsharp)
- [F# on Discord](https://discord.com/invite/fsharp-196693847965696000)
- [F# on Discourse](https://forums.fsharp.org/)
- [F# on Reddit](https://www.reddit.com/r/fsharp/)
- [F# on Telegram](https://t.me/fsharp_chat)
- [F# on Twitter](https://x.com/hashtag/fsharp)

### Other Lists

- [Awesome .NET!](https://github.com/quozd/awesome-dotnet) [![GitHub stars](https://img.shields.io/github/stars/quozd/awesome-dotnet?style=flat)](https://github.com/quozd/awesome-dotnet/stargazers) - Collection of awesome .NET libraries, tools, frameworks and software.
- [Companies using F#](https://github.com/fsprojects/fsharp-companies) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/fsharp-companies?style=flat)](https://github.com/fsprojects/fsharp-companies/stargazers) - Community curated list of companies that use F# (maybe useful if you're looking for a job?)
- [F# Community Projects](http://fsharp.org/community/projects/) - Everything produced by the F# community. 
- [Fable Resources](https://fable.io/resources.html) - A curated list of useful Fable-related tutorials, libraries and software.

### Websites

- [Community for F#](http://c4fsharp.net/) - Links to dojos and recordings of community presentations.
- [Decompiler.com](https://www.decompiler.com/) - Online C#/VB/F# decompiler.
- [DotNetFiddle](https://dotnetfiddle.net/) - Online REPL.
- [F# Software Foundation](http://fsharp.org/) - Main website.
- [F# for Fun and Profit](https://fsharpforfunandprofit.com/) - Reference tutorials.
- [SharpLab](https://sharplab.io/) - C#/VB/F# compiler playground.
- [Try F#](https://try.fsharp.org/) - Online tutorials, currently without execution of code due to Silverlight dependency.
- [cs2fs](https://jindraivanek.gitlab.io/cs2fs-online) - Transform C# code to F# code.
- [fantomas-tools](https://fsprojects.github.io/fantomas-tools) - A set of Fantomas related tools like AST viewer and online bug reporter.

### Videos

- [Amplifying F# YouTube Channel](https://www.youtube.com/@amplifyingfsharp)
- [F# Online YouTube Channel](https://www.youtube.com/@fonline6018)
- [Austin F# Meetup Group Recorded Presentations](http://usergroup.tv/videos/category/group/austin-f-meetup)
- [F# Chats on performance](https://www.youtube.com/watch?v=EIBRoNEpg6c&list=PLqWncHdBPoD4O1sr2Q3W9gAuJ30s09U2r)
- [Fast Dictionary in F#](https://www.youtube.com/watch?v=KMR2y1vcO-s&list=PLqWncHdBPoD4-d_VSZ0MB0IBKQY0rwYLd)
- [Intro to F#](https://www.youtube.com/watch?v=1ioGr701c5Q&list=PLqWncHdBPoD4YEWoXQlRj1tiTc96HZxH8)
- [Topological Sort](https://www.youtube.com/playlist?list=PLqWncHdBPoD5hEK31CcfmTHP-7icw2Xd0)

### Courses

- [Write yourself a scheme in 48 hours using F#](https://write-yourself-a-scheme.pangwa.com/)
