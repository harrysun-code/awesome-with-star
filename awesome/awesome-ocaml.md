# OCaml

[![GitHub stars](https://img.shields.io/github/stars/ocaml-community/awesome-ocaml?style=flat)](https://github.com/ocaml-community/awesome-ocaml/stargazers)

Awesome OCaml
=============

<img src="colour-logo.png" width="70%" />

> _**Everything you'll ever need on the road to mastering OCaml.**_

A curated list of references to awesome OCaml tools, frameworks, libraries, and articles. Additionally, there is a collection of freely available [**books**](https://github.com/rizo/awesome-ocaml/tree/master/books) [![GitHub stars](https://img.shields.io/github/stars/rizo/awesome-ocaml/tree/master/books?style=flat)](https://github.com/rizo/awesome-ocaml/tree/master/books/stargazers), [**papers**](https://github.com/rizo/awesome-ocaml/tree/master/papers) [![GitHub stars](https://img.shields.io/github/stars/rizo/awesome-ocaml/tree/master/papers?style=flat)](https://github.com/rizo/awesome-ocaml/tree/master/papers/stargazers), and [**presentations**](https://github.com/rizo/awesome-ocaml/tree/master/presentations) [![GitHub stars](https://img.shields.io/github/stars/rizo/awesome-ocaml/tree/master/presentations?style=flat)](https://github.com/rizo/awesome-ocaml/tree/master/presentations/stargazers).

If you're looking for comprehensive community-driven content about OCaml, visit 📚[OCamlverse](https://ocamlverse.github.io/)!

For a quick introduction to the modern OCaml development workflow, consult the [**Up and Running with OCaml**](https://ocaml.org/learn/tutorials/up_and_running.html) tutorial.

Your favorite package is not listed? Fork and [create a Pull Request](https://github.com/rizo/awesome-ocaml/edit/master/README.md) [![GitHub stars](https://img.shields.io/github/stars/rizo/awesome-ocaml/edit/master/README.md?style=flat)](https://github.com/rizo/awesome-ocaml/edit/master/README.md/stargazers) to add it!

## Contents

- [Community](#community)
- [Algorithms and Data Structures](#algorithms-and-data-structures)
- [Application Libraries](#application-libraries)
- [Benchmarking](#benchmarking)
- [Blogs](#blogs)
- [Books](#books)
- [Videos](#videos)
- [Code Analysis and Linters](#code-analysis-and-linters)
- [Compilers and Compiler Tools](#compilers-and-compiler-tools)
- [Concurrency](#concurrency)
- [Databases](#databases)
- [Datetime](#datetime)
- [Developer Tools](#developer-tools)
- [Exercises and Short Examples](#exercises-and-short-examples)
- [Formal Software Verification](#formal-software-verification)
- [General](#general)
- [Graphics](#graphics)
- [Internationalization](#internationalization)
- [User Interface](#user-interface)
- [Language-related](#language-related)
- [Large Source Code Examples](#large-source-code-examples)
- [Logging](#logging)
- [Machine Learning](#machine-learning)
- [Messaging](#messaging)
- [Metaprogramming](#metaprogramming)
- [Metrics](#metrics)
- [Mobile Applications](#mobile-applications)
- [Networking](#networking)
- [Online Courses](#online-courses)
- [Package Management](#package-management)
- [Parallelism](#parallelism)
- [Project Starter Templates](#project-starter-templates)
- [Printers helpers](#printers-helpers)
- [Questions](#questions)
- [Regular Expressions](#regular-expressions)
- [Science and Technical Computing](#science-and-technical-computing)
- [Security and Cryptography](#security-and-cryptography)
- [Semantic Technology](#semantic-technology)
- [Serialization](#serialization)
- [System Programming](#system-programming)
- [Testing](#testing)
- [Utilities](#utilities)
- [Web Development](#web-development)

* * *


## Community

- [Official OCaml Website](https://ocaml.org/)
- [OCaml Discourse Web Forum](https://discuss.ocaml.org/)
- [OCaml Discord Chat](https://discord.gg/ZBgYuvR)
- [Official OCaml Mailing List](https://inbox.ocaml.org/caml-list/)
- [OCaml Planet](https://ocaml.org/community/planet/)
- [OCaml SubReddit](https://www.reddit.com/r/ocaml/)


## Algorithms and Data Structures

- [Comparing a Machine Learning Algorithm Implemented in F# and OCaml](https://philtomson.github.io/blog/2014-05-29-comparing-a-machine-learning-algorithm-implemented-in-f-sharp-and-ocaml/)
- [OCamlgraph](https://github.com/backtracking/ocamlgraph) [![GitHub stars](https://img.shields.io/github/stars/backtracking/ocamlgraph?style=flat)](https://github.com/backtracking/ocamlgraph/stargazers) – A generic graph library for OCaml.
- [ods](https://github.com/owainlewis/ods) [![GitHub stars](https://img.shields.io/github/stars/owainlewis/ods?style=flat)](https://github.com/owainlewis/ods/stargazers) – A large collection of data structures and algorithms for OCaml.
- [combine](https://github.com/backtracking/combine) [![GitHub stars](https://img.shields.io/github/stars/backtracking/combine?style=flat)](https://github.com/backtracking/combine/stargazers) – OCaml library for combinatorics <https://www.lri.fr/~filliatr/combine/>.
- [Decompress](https://github.com/mirage/decompress) [![GitHub stars](https://img.shields.io/github/stars/mirage/decompress?style=flat)](https://github.com/mirage/decompress/stargazers) - A pure OCaml implementation of Zlib.
- [Ke](https://github.com/mirage/ke) [![GitHub stars](https://img.shields.io/github/stars/mirage/ke?style=flat)](https://github.com/mirage/ke/stargazers) - Fast implementation of queue (FIFO) in OCaml.
- [Duff](https://github.com/mirage/duff) [![GitHub stars](https://img.shields.io/github/stars/mirage/duff?style=flat)](https://github.com/mirage/duff/stargazers) - Implementation of Rabin's fingerprint and delta compression by P. MacDonald in OCaml (same as [libXdiff](http://www.xmailserver.org/xdiff-lib.html)
- [ORaft](https://github.com/komamitsu/oraft) [![GitHub stars](https://img.shields.io/github/stars/komamitsu/oraft?style=flat)](https://github.com/komamitsu/oraft/stargazers) - Library of [Raft consensus algorithm](https://raft.github.io/raft.pdf) implemented in OCaml
- [ODiff](https://github.com/dmtrKovalenko/odiff) [![GitHub stars](https://img.shields.io/github/stars/dmtrKovalenko/odiff?style=flat)](https://github.com/dmtrKovalenko/odiff/stargazers) – Library of [YIQ NTSC transmission image difference alghoritm](http://www.progmat.uaem.mx:8080/artVol2Num2/Articulo3Vol2Num2.pdf) implemented in OCaml and ReasonML.

## Application Libraries

- [Batteries Included](https://github.com/ocaml-batteries-team/batteries-included) [![GitHub stars](https://img.shields.io/github/stars/ocaml-batteries-team/batteries-included?style=flat)](https://github.com/ocaml-batteries-team/batteries-included/stargazers) – A community-maintained foundation library for your OCaml projects.
- [Cmdliner](https://github.com/dbuenzli/cmdliner) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/cmdliner?style=flat)](https://github.com/dbuenzli/cmdliner/stargazers) – Declarative definition of command line interfaces for OCaml.
- [Core](https://github.com/janestreet/core) [![GitHub stars](https://img.shields.io/github/stars/janestreet/core?style=flat)](https://github.com/janestreet/core/stargazers) – Jane Street Capital's full-fledged standard library overlay. A portable subset of Core is also available: [Core_kernel](https://github.com/janestreet/core_kernel) [![GitHub stars](https://img.shields.io/github/stars/janestreet/core_kernel?style=flat)](https://github.com/janestreet/core_kernel/stargazers).
- [Base](https://github.com/janestreet/base) [![GitHub stars](https://img.shields.io/github/stars/janestreet/base?style=flat)](https://github.com/janestreet/base/stargazers) - Jane Street Capital's dependency-free, quick-compiling, fully-portable across any environment that can run OCaml code standard library.
- [React](http://erratique.ch/software/react) – React is an OCaml module for functional reactive programming (FRP). It provides support for programs with time-varying values, declarative events, and signals.
- [Minicli](https://github.com/UnixJunkie/minicli) [![GitHub stars](https://img.shields.io/github/stars/UnixJunkie/minicli?style=flat)](https://github.com/UnixJunkie/minicli/stargazers) – Minimalist library for command-line parsing.
- [easy-format](https://github.com/mjambon/easy-format) [![GitHub stars](https://img.shields.io/github/stars/mjambon/easy-format?style=flat)](https://github.com/mjambon/easy-format/stargazers) – Pretty-printing library for OCaml.
- [ocaml-rpc](https://github.com/mirage/ocaml-rpc) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-rpc?style=flat)](https://github.com/mirage/ocaml-rpc/stargazers) – Light library to deal with RPCs in OCaml.
- [ocaml-containers](https://github.com/c-cube/ocaml-containers) [![GitHub stars](https://img.shields.io/github/stars/c-cube/ocaml-containers?style=flat)](https://github.com/c-cube/ocaml-containers/stargazers) – A lightweight, modular standard library extension, string library, and interfaces to various libraries (bigarrays, Unix, etc.) BSD license.


## Benchmarking

- [core_bench](https://github.com/janestreet/core_bench) [![GitHub stars](https://img.shields.io/github/stars/janestreet/core_bench?style=flat)](https://github.com/janestreet/core_bench/stargazers) – Micro-benchmarking library for OCaml by Jane Street.
  - [Getting Started with Core_bench](https://github.com/janestreet/core_bench/wiki/Getting-Started-with-Core_bench) [![GitHub stars](https://img.shields.io/github/stars/janestreet/core_bench/wiki/Getting-Started-with-Core_bench?style=flat)](https://github.com/janestreet/core_bench/wiki/Getting-Started-with-Core_bench/stargazers)
- [benchmark](https://github.com/Chris00/ocaml-benchmark) [![GitHub stars](https://img.shields.io/github/stars/Chris00/ocaml-benchmark?style=flat)](https://github.com/Chris00/ocaml-benchmark/stargazers) – Benchmarking functions for measuring the run-time of functions using latency or throughput.


## Blogs

- [Gagallium](http://gallium.inria.fr/blog/)
- [Type OCaml – Many things about OCaml](http://typeocaml.com/)
- [OCaml Platform](https://opam.ocaml.org/blog/)
- [Drup's Thingies](https://drup.github.io/)
- [Thomas Letan’s articles about OCaml](https://soap.coffee/~lthms/tags/ocaml.html)

## Books

- [More OCaml: Algorithms, Methods, and Diversions](https://www.amazon.com/More-OCaml-Algorithms-Methods-Diversions/dp/0957671113/) – In More OCaml, John Whitington takes a meandering tour of functional programming with OCaml, introducing various language features and describing some classic algorithms. The book ends with a large-scale example dealing with the production of PDF files. There are questions for each chapter, along with worked-out answers and hints.
- [How to Think Like a (Functional) Programmer](http://www.greenteapress.com/thinkocaml/index.html) by Allen Downey and Nicholas Monje – How to Think Like a Computer Scientist is an introductory programming textbook based on the OCaml language. It is a modified version of Think Python by Allen Downey. It is intended for newcomers to programming and also those who know some programming but want to learn programming in the function-oriented paradigm, or those who simply want to learn OCaml.
- [OCaml from the Very Beginning](http://ocaml-book.com/) by J. Whitington - OCaml from the Very Beginning will appeal both to new programmers and experienced programmers eager to explore functional languages such as OCaml.
- [Pearls of Functional Algorithm Design](https://www.amazon.co.uk/Pearls-Functional-Algorithm-Design-Richard/dp/0521513383) by Richard Bird - It summarizes 30 hard algorithmic problems in the function programming world. Although it is for Haskell, the algorithm problems are very interesting, and trying to solve them in OCaml also helps the thinking of functional programming. Partial solutions in OCaml are [here](https://github.com/MassD/pearls) [![GitHub stars](https://img.shields.io/github/stars/MassD/pearls?style=flat)](https://github.com/MassD/pearls/stargazers).
- [Real World OCaml](https://realworldocaml.org/) by Y. Minsky, A. Madhavapeddy, and J. Hickey - Functional Programming for the masses.
- [Unix System Programming in OCaml](https://ocaml.github.io/ocamlunix/) by X. Leroy and D. Rémy – Introduction to Unix Systems Programming, with an emphasis on communications between processes.
- [Using, Understanding, and Unraveling OCaml](https://caml.inria.fr/pub/docs/u3-ocaml) – This book describes both the OCaml language and the theoretical grounds behind its powerful type system.
- [Purely Functional Data Structures](https://www.amazon.co.uk/Purely-Functional-Structures-Chris-Okasaki/dp/0521631246/ref=sr_1_1?ie=UTF8&qid=1406279836&sr=8-1&keywords=functional+data+structures) - This is the first or only book focus on various data structures in FP world. A must-read one.
- [OCaml for Scientists](http://www.ffconsultancy.com/products/ocaml_for_scientists/) - by Jon Harrop.
- [OCaml Programming: Correct + Efficient + Beautiful](https://cs3110.github.io/textbook) - Textbook on Functional Programming and Data Structures in OCaml - by Michael R. Clarkson et al.

## Videos

 - [OCaml Programming: Correct + Efficient + Beautiful](https://www.youtube.com/playlist?list=PLre5AT9JnKShBOPeuiD9b-I4XROIJhkIU) - List of 200 bite-sized videos recorded by Michael R. Clarkson. It can be watched independently of the textbook titled the same and listed above in the [Books section](#books).

## Code Analysis and Linters

- [Mascot](http://mascot.x9c.fr/) - Mascot is a style-checker for OCaml sources.
- [pfff](https://github.com/returntocorp/pfff) [![GitHub stars](https://img.shields.io/github/stars/returntocorp/pfff?style=flat)](https://github.com/returntocorp/pfff/stargazers) – pfff is a set of tools and APIs to perform some static analysis, dynamic analysis, code visualizations, code navigations, or style-preserving source-to-source transformations such as refactorings on source code.
- [Infer](https://github.com/facebook/infer) [![GitHub stars](https://img.shields.io/github/stars/facebook/infer?style=flat)](https://github.com/facebook/infer/stargazers) - Infer is a static analyzer for Java, C and Objective-C
- [Frama-C](http://frama-c.com) - Frama-C is a static analysis and formal proof framework for C and C++.
- [flow](https://github.com/facebook/flow) [![GitHub stars](https://img.shields.io/github/stars/facebook/flow?style=flat)](https://github.com/facebook/flow/stargazers) - flow is a static type checker for JavaScript.
- [SLAyer](https://github.com/Microsoft/SLAyer) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/SLAyer?style=flat)](https://github.com/Microsoft/SLAyer/stargazers) - SLAyer is an automatic formal verification tool that uses separation logic to verify memory safety of C programs.
- [MemCAD](https://github.com/Antique-team/memcad) [![GitHub stars](https://img.shields.io/github/stars/Antique-team/memcad?style=flat)](https://github.com/Antique-team/memcad/stargazers) - MemCAD is an abstract interpreter for shape analysis. MemCAD can verify C programs manipulating complex data structures.
- [Camelot](https://github.com/upenn-cis1xx/camelot) [![GitHub stars](https://img.shields.io/github/stars/upenn-cis1xx/camelot?style=flat)](https://github.com/upenn-cis1xx/camelot/stargazers) - Camelot is a modular and fully configurable OCaml linter and stylechecker.
- [coq-of-ocaml](https://github.com/formal-land/coq-of-ocaml) [![GitHub stars](https://img.shields.io/github/stars/formal-land/coq-of-ocaml?style=flat)](https://github.com/formal-land/coq-of-ocaml/stargazers) - Translator from OCaml to Coq to formally verify OCaml code.
- [MOPSA](https://gitlab.com/mopsa/mopsa-analyzer) - MOPSA is a generic framework for building sound static analyzers based on the theory of abstract interpretation.


## Program analysis
- [BAP](https://github.com/BinaryAnalysisPlatform/bap) [![GitHub stars](https://img.shields.io/github/stars/BinaryAnalysisPlatform/bap?style=flat)](https://github.com/BinaryAnalysisPlatform/bap/stargazers) - BAP is a reverse engineering and program analysis platform that targets binary programs.
- [BinCat](https://github.com/airbus-seclab/bincat) [![GitHub stars](https://img.shields.io/github/stars/airbus-seclab/bincat?style=flat)](https://github.com/airbus-seclab/bincat/stargazers) - BinCat is a binary code static analysis toolkit.
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) [![GitHub stars](https://img.shields.io/github/stars/fkie-cad/cwe_checker?style=flat)](https://github.com/fkie-cad/cwe_checker/stargazers) - cwe_checker finds vulnerable patterns in binary executables.
- [Owi](https://github.com/OCamlPro/owi) [![GitHub stars](https://img.shields.io/github/stars/OCamlPro/owi?style=flat)](https://github.com/OCamlPro/owi/stargazers) - Owi is a toolchain for working with WebAssembly (Wasm) in OCaml, featuring a powerful, parallel symbolic execution engine for Wasm. It also provides frontends for compiling and analyzing C and Rust programs.
- [Smt.ml](https://github.com/formalsec/smtml) [![GitHub stars](https://img.shields.io/github/stars/formalsec/smtml?style=flat)](https://github.com/formalsec/smtml/stargazers) - Smt.ml is a frontend OCaml library that interfaces with multiple SMT solvers, enabling seamless integration of solvers like Z3, cvc5, Colibri2, Bitwuzla, and Alt-Ergo within OCaml programs.

## Compilers and Compiler Tools

- **Languages and Compilers**:
  - [Caramel](https://caramel.run/) - Caramel is a functional language for building type-safe, scalable, and maintainable applications.
  - [cDuce](http://www.cduce.org/) - cDuce is a modern XML-oriented functional language with innovative features.
  - [Compcert C Compiler](http://compcert.inria.fr/) - It is a C Compiler supporting most of the ISO C90 and C99 / ANSI C  features.
  - [Eff Programming Language](http://www.eff-lang.org/) - Eff is a functional language with handlers of not only exceptions, but also of other computational effects such as state or I/O.
  - [Hack Programming Language](https://hacklang.org/)
  - [Haxe Programming Language](https://haxe.org/)
  - [Neko Programming Language](https://nekovm.org/) - Originally the compiler was written in OCaml.
  - [Mazeppa](https://github.com/mazeppa-dev/mazeppa) [![GitHub stars](https://img.shields.io/github/stars/mazeppa-dev/mazeppa?style=flat)](https://github.com/mazeppa-dev/mazeppa/stargazers) - A modern supercompiler for call-by-value functional languages.
  - [Mezzo Programming Language](https://protz.github.io/mezzo/) - Mezzo is a programming language in the ML tradition, which places strong emphasis on the control of aliasing and access to mutable memory.
  - [OCaml-Java](http://www.ocamljava.org/) - OCaml to Java bytecode compiler.
  - [Opa Programming Language](http://opalang.org/)
  - [Rhine](https://github.com/artagnon/rhine-ml) [![GitHub stars](https://img.shields.io/github/stars/artagnon/rhine-ml?style=flat)](https://github.com/artagnon/rhine-ml/stargazers) – A Lisp on LLVM written in OCaml.
  - [Rust Programming Language](https://www.rust-lang.org/) - Originally written in OCaml before bootstrapping.
  - [Quick C-- Target Language](http://www.cminusminus.org/) - It is now a dead project. [Github Repo](https://github.com/nrnrnr/qc--) [![GitHub stars](https://img.shields.io/github/stars/nrnrnr/qc--?style=flat)](https://github.com/nrnrnr/qc--/stargazers). [Alternative website](http://www.cs.tufts.edu/~nr/c--/qc--.html).
  - [tis-interpreter](https://github.com/TrustInSoft/tis-interpreter) [![GitHub stars](https://img.shields.io/github/stars/TrustInSoft/tis-interpreter?style=flat)](https://github.com/TrustInSoft/tis-interpreter/stargazers) - An interpreter for finding subtle bugs in programs written in standard C

  - [Reason](http://facebook.github.io/reason/) - Friendly syntax & toolchain for OCaml by Facebook.
  - [RaML](http://raml.co/index.html) - Resource Aware ML (RaML) is a tool that automatically and statically computes resource-use bounds for OCaml programs.
  - [Liquid ML](https://github.com/benfaerber/liquid-ml) [![GitHub stars](https://img.shields.io/github/stars/benfaerber/liquid-ml?style=flat)](https://github.com/benfaerber/liquid-ml/stargazers) - Shopify's Liquid Templating language for OCaml.

- **Parser and Lexer Generators**:
  - [Opal](https://github.com/pyrocat101/opal) [![GitHub stars](https://img.shields.io/github/stars/pyrocat101/opal?style=flat)](https://github.com/pyrocat101/opal/stargazers) – Self-contained monadic parser combinators for OCaml.
  - [Sedlex](https://github.com/ocaml-community/sedlex) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/sedlex?style=flat)](https://github.com/ocaml-community/sedlex/stargazers) is a modern, encoding-agnostic (read: Unicode-supporting) lexer generator (the ppx-based successor to [ulex](http://www.cduce.org/download.html#side).)
  - [Menhir](http://gallium.inria.fr/~fpottier/menhir/) – Menhir is a LR(1) parser generator for OCaml.
    - See [ocaml-parsing](https://github.com/smolkaj/ocaml-parsing) [![GitHub stars](https://img.shields.io/github/stars/smolkaj/ocaml-parsing?style=flat)](https://github.com/smolkaj/ocaml-parsing/stargazers) for a clearer example of using Menhir and Sedlex to produce a useful parser,
    - ... and [Obelisk](https://github.com/Lelio-Brun/Obelisk) [![GitHub stars](https://img.shields.io/github/stars/Lelio-Brun/Obelisk?style=flat)](https://github.com/Lelio-Brun/Obelisk/stargazers), a neat project to produce readable LaTeX, HTML, or plain-text EBNF-style documentation for your grammar.
  - [ocamllex/ocamlyacc](http://caml.inria.fr/pub/docs/manual-ocaml-4.01/lexyacc.html) – lex and yacc implementation for OCaml.
  - [Angstrom](https://github.com/inhabitedtype/angstrom) [![GitHub stars](https://img.shields.io/github/stars/inhabitedtype/angstrom?style=flat)](https://github.com/inhabitedtype/angstrom/stargazers) - Parser combinators built for speed and memory efficiency
- **Articles**:
  - [Kaleidoscope: Implementing a Language with LLVM in Objective Caml¶](http://llvm.org/docs/tutorial/OCamlLangImpl1.html)


## Concurrency
Before OCaml 5.0, there were two libraries for concurrent programming: _Lwt_ and _Async_. They provide very similar functionality but make radically different decisions with regards to error handling and internal implementation details (see the links below for more details). [Real World OCaml](https://realworldocaml.org/) uses Async, but a version of the [code examples translated to Lwt](https://github.com/dkim/rwo-lwt) [![GitHub stars](https://img.shields.io/github/stars/dkim/rwo-lwt?style=flat)](https://github.com/dkim/rwo-lwt/stargazers) is also available.

With the introduction of [Effect Handlers](https://ocaml.org/manual/effects.html) in OCaml 5.0, a bunch of other libraries have been created for concurrent programming, replacing the monadic approaches of LWT and Async with direct-style ones.

- **Libraries**:
  - [Eio](https://github.com/ocaml-multicore/eio) [![GitHub stars](https://img.shields.io/github/stars/ocaml-multicore/eio?style=flat)](https://github.com/ocaml-multicore/eio/stargazers) — effects-based direct-style IO for multicore OCaml.
  - [Miou](https://github.com/robur-coop/miou) [![GitHub stars](https://img.shields.io/github/stars/robur-coop/miou?style=flat)](https://github.com/robur-coop/miou/stargazers) — a simple scheduler for OCaml 5.
  - [Lwt](http://ocsigen.org/lwt/) — A cooperative threads library for OCaml.
  - [Async](https://opensource.janestreet.com/async/) — A monadic concurrence library to go with the Core library.
- **Articles**:
  - [The blog post that introduced Async](https://blog.janestreet.com/announcing-async/)
  - [A user gives up on Async](http://rgrinberg.com/posts/abandoning-async/)
  - [Cooperative Concurrency in OCaml: A Core.Std.Async Example](http://philtomson.github.io/blog/2014/07/09/core-dot-async-example/).

## Databases

- **Bindings**
  - [Dbm](https://forge.ocamlcore.org/projects/camldbm/) — A binding to the NDBM/GDBM Unix "databases".
  - [Mongo.ml](https://massd.github.io/mongo/) – An OCaml driver for Mongodb
  - [PG'OCaml](http://pgocaml.forge.ocamlcore.org/) — A type-safe interface to PostgreSQL in pure OCaml.
    - [ppx_pgsql](https://github.com/tizoc/ppx_pgsql) [![GitHub stars](https://img.shields.io/github/stars/tizoc/ppx_pgsql?style=flat)](https://github.com/tizoc/ppx_pgsql/stargazers) – A syntax extension for embedded SQL queries using PG'OCaml.
  - [PostgreSQL-OCaml](https://mmottl.github.io/postgresql-ocaml/) — An interface to PostgreSQL through the C API (`libpq`).
  - [SQLite3](https://github.com/mmottl/sqlite3-ocaml) [![GitHub stars](https://img.shields.io/github/stars/mmottl/sqlite3-ocaml?style=flat)](https://github.com/mmottl/sqlite3-ocaml/stargazers) — OCaml bindings to the SQLite3 database.
  - [Sqlite3EZ](https://mlin.github.io/ocaml-sqlite3EZ/) — Thin wrapper for SQLite3 with a simplified interface.
  - [ocaml-redis](https://github.com/0xffea/ocaml-redis) [![GitHub stars](https://img.shields.io/github/stars/0xffea/ocaml-redis?style=flat)](https://github.com/0xffea/ocaml-redis/stargazers) – Redis bindings for OCaml.
  - [mariadb](https://github.com/ocaml-community/ocaml-mariadb) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/ocaml-mariadb?style=flat)](https://github.com/ocaml-community/ocaml-mariadb/stargazers) - Bindings to MariaDB/MySQL, supporting the nonblocking API
  - [pgx](https://github.com/arenadotio/pgx) [![GitHub stars](https://img.shields.io/github/stars/arenadotio/pgx?style=flat)](https://github.com/arenadotio/pgx/stargazers) – A pure OCaml PostgreSQL client library.
  - [mysql_protocol](https://github.com/slegrand45/mysql_protocol) [![GitHub stars](https://img.shields.io/github/stars/slegrand45/mysql_protocol?style=flat)](https://github.com/slegrand45/mysql_protocol/stargazers) – Implementation of MySQL Protocol with the Bitstring library.
- **New Implementations**
  - [Irmin](https://github.com/mirage/irmin) [![GitHub stars](https://img.shields.io/github/stars/mirage/irmin?style=flat)](https://github.com/mirage/irmin/stargazers) — A distributed database that follows the same design principles as Git.
  - [Obigstore](http://obigstore.forge.ocamlcore.org/) — A database with BigTable-like data model atop LevelDB.
  - [RunOrg](https://github.com/RunOrg/RunOrg) [![GitHub stars](https://img.shields.io/github/stars/RunOrg/RunOrg?style=flat)](https://github.com/RunOrg/RunOrg/stargazers) - It is a WIP database server written in OCaml.
  - [dokeysto](https://github.com/UnixJunkie/dokeysto) [![GitHub stars](https://img.shields.io/github/stars/UnixJunkie/dokeysto?style=flat)](https://github.com/UnixJunkie/dokeysto/stargazers) - dumb OCaml key-value store, string keys and string
  values. Optional on-the-fly LZ4 compression of values or tokyocabinet backend.
- **Overlays**
  - [Sequoia](https://github.com/andrenth/sequoia) [![GitHub stars](https://img.shields.io/github/stars/andrenth/sequoia?style=flat)](https://github.com/andrenth/sequoia/stargazers) - Sequoia is a type-safe query builder for MySQL/MariaDB and PostgreSQL
  - [Macaque](https://github.com/ocsigen/macaque) [![GitHub stars](https://img.shields.io/github/stars/ocsigen/macaque?style=flat)](https://github.com/ocsigen/macaque/stargazers) — Macaque is a library for safe and flexible database queries using comprehensions on top of PG'OCaml.
  - [ORM](https://github.com/mirage/orm) [![GitHub stars](https://img.shields.io/github/stars/mirage/orm?style=flat)](https://github.com/mirage/orm/stargazers) — ORM for SQLite.
  - [Caqti](https://github.com/paurkedal/ocaml-caqti) [![GitHub stars](https://img.shields.io/github/stars/paurkedal/ocaml-caqti?style=flat)](https://github.com/paurkedal/ocaml-caqti/stargazers) - Cooperative-threaded access to relational data
  - [Caqti setence preparation, ppx_rapper](https://github.com/roddyyaga/ppx_rapper) [![GitHub stars](https://img.shields.io/github/stars/roddyyaga/ppx_rapper?style=flat)](https://github.com/roddyyaga/ppx_rapper/stargazers)
- **Articles**:
  - [Implementing the Binary Memcached Protocol with Ocaml and Bitstring](https://andreas.github.io/2014/08/22/implementing-the-binary-memcached-protocol-with-ocaml-and-bitstring/)
  - [Interfacing OCaml and PostgreSQL with Caqti](https://medium.com/@bobbypriambodo/interfacing-ocaml-and-postgresql-with-caqti-a92515bdaa11)
  - [Finally, Type-Safe, Extensible and Efficient Language Integrated Query](https://www.cs.tsukuba.ac.jp/~kam/papers/pepm2016a.pdf) by Oleg and Co. 
    The proposed approach is to describe SQL queries in type-safe manner and optimize them (using term rewriting or normalization-by evaluation) before sending to database engine. It potentially could optimize O(n^2) queries to O(n) ones.


## Datetime

- [ISO8601](https://github.com/sagotch/ISO8601.ml) [![GitHub stars](https://img.shields.io/github/stars/sagotch/ISO8601.ml?style=flat)](https://github.com/sagotch/ISO8601.ml/stargazers)
- [calendar](http://calendar.forge.ocamlcore.org/)
- [odate](https://github.com/hhugo/odate) [![GitHub stars](https://img.shields.io/github/stars/hhugo/odate?style=flat)](https://github.com/hhugo/odate/stargazers)
- [ptime](http://erratique.ch/software/ptime)


## Developer Tools

- [Try OCaml](https://try.ocamlpro.com/) – Try OCaml in your web browser.
- [learn-ocaml](https://github.com/ocaml-sf/learn-ocaml) [![GitHub stars](https://img.shields.io/github/stars/ocaml-sf/learn-ocaml?style=flat)](https://github.com/ocaml-sf/learn-ocaml/stargazers). Web app (written in OCaml) underlying the learn-ocaml-corpus. Can be customized to serve lectures (with Markdown slides), playgrounds (with a toplevel prelude), and interactive exercises (with OCaml tests). MIT License.
- [learn-ocaml.el](https://github.com/pfitaxel/learn-ocaml.el) [![GitHub stars](https://img.shields.io/github/stars/pfitaxel/learn-ocaml.el?style=flat)](https://github.com/pfitaxel/learn-ocaml.el/stargazers). Minor mode for Emacs that can display exercise topics and grade exercise solutions, after logging to a Learn-OCaml instance. MIT License.
- [BetterOCaml](https://betterocaml.ml) – An efficient, intuitive, and cross-platform web IDE with your OCaml code interpreted and running in your browser!
- [codingground](https://www.tutorialspoint.com/compile_ocaml_online.php) – Compile and execute OCaml code online.
- [OCaml: Learn & Code iOS app](https://apps.apple.com/app/ocaml-learn-code/id1547506826) - Learn and execute OCaml code from your iPhone/iPad/Mac.
- [Jupyter](https://github.com/akabe/ocaml-jupyter) [![GitHub stars](https://img.shields.io/github/stars/akabe/ocaml-jupyter?style=flat)](https://github.com/akabe/ocaml-jupyter/stargazers) – An OCaml kernel for the Jupyter notebook.
- [utop](https://github.com/ocaml-community/utop) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/utop?style=flat)](https://github.com/ocaml-community/utop/stargazers) – Universal toplevel for OCaml with support for multiline edition, history, real-time and context-sensitive completion, colors, and more.
- [ocamlformat](https://github.com/ocaml-ppx/ocamlformat) [![GitHub stars](https://img.shields.io/github/stars/ocaml-ppx/ocamlformat?style=flat)](https://github.com/ocaml-ppx/ocamlformat/stargazers) - A command-line tool to format OCaml code.
- [ocamlbrowser](http://caml.inria.fr/pub/docs/manual-ocaml/browser.html) – A source and compiled interface browser, written using LablTk. Included in the standard distribution for ocaml <= 4.01 and with labltk for ocaml >= 4.02.
- [ghim](https://github.com/samoht/ghim) [![GitHub stars](https://img.shields.io/github/stars/samoht/ghim?style=flat)](https://github.com/samoht/ghim/stargazers) – A command-line tool to manage Github Issues.
- [OCaml Yeoman Generator](https://github.com/mabrasil/generator-ocaml) [![GitHub stars](https://img.shields.io/github/stars/mabrasil/generator-ocaml?style=flat)](https://github.com/mabrasil/generator-ocaml/stargazers) – Yeoman generator to scaffold OCaml modules.
- [puml2xml](https://github.com/khalidbelk/puml2xml) [![GitHub stars](https://img.shields.io/github/stars/khalidbelk/puml2xml?style=flat)](https://github.com/khalidbelk/puml2xml/stargazers) – A PlantUML (**.puml**) to XML (**.xmi**) converter.

- **Foreign Function Interface**:
  - [ctypes](https://github.com/ocamllabs/ocaml-ctypes) [![GitHub stars](https://img.shields.io/github/stars/ocamllabs/ocaml-ctypes?style=flat)](https://github.com/ocamllabs/ocaml-ctypes/stargazers) – Library for binding to C libraries using pure OCaml.
  - [ocaml-main-program-in-c](https://github.com/johnwhitington/ocaml-main-program-in-c) [![GitHub stars](https://img.shields.io/github/stars/johnwhitington/ocaml-main-program-in-c?style=flat)](https://github.com/johnwhitington/ocaml-main-program-in-c/stargazers) – Example build system for making mixed C/Ocaml binaries where the main program is in C.
  - [Modular foreign function bindings](http://openmirage.org/blog/modular-foreign-function-bindings)
  - [Py.ml](https://github.com/thierry-martinez/pyml) [![GitHub stars](https://img.shields.io/github/stars/thierry-martinez/pyml?style=flat)](https://github.com/thierry-martinez/pyml/stargazers) - OCaml bindings for Python.
- **Editor Integration**:
  - [ocaml-lsp](https://github.com/ocaml/ocaml-lsp) [![GitHub stars](https://img.shields.io/github/stars/ocaml/ocaml-lsp?style=flat)](https://github.com/ocaml/ocaml-lsp/stargazers) - An LSP language server for OCaml that integrates with any editor that understands LSP like [VSCode](https://github.com/microsoft/vscode) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode?style=flat)](https://github.com/microsoft/vscode/stargazers), Vim and Emacs.
  - [merlin](https://github.com/ocaml/merlin) [![GitHub stars](https://img.shields.io/github/stars/ocaml/merlin?style=flat)](https://github.com/ocaml/merlin/stargazers) – Context sensitive completion for OCaml in Vim and Emacs.
  - [tuareg](https://github.com/ocaml/tuareg) [![GitHub stars](https://img.shields.io/github/stars/ocaml/tuareg?style=flat)](https://github.com/ocaml/tuareg/stargazers) - OCaml mode for Emacs that can run the toplevel and the debugger within Emacs.
  - [opam-switch-mode](https://github.com/ProofGeneral/opam-switch-mode) [![GitHub stars](https://img.shields.io/github/stars/ProofGeneral/opam-switch-mode?style=flat)](https://github.com/ProofGeneral/opam-switch-mode/stargazers) - Minor mode for Emacs that extends Tuareg and Merlin with menus to change or reset the opam switch in the ambient Emacs session.
  - [merlin-eldoc](https://github.com/Khady/merlin-eldoc) [![GitHub stars](https://img.shields.io/github/stars/Khady/merlin-eldoc?style=flat)](https://github.com/Khady/merlin-eldoc/stargazers) – Emacs package to provide merlin's features through eldoc.
  - [vscode-ocaml](https://github.com/hackwaly/vscode-ocaml) [![GitHub stars](https://img.shields.io/github/stars/hackwaly/vscode-ocaml?style=flat)](https://github.com/hackwaly/vscode-ocaml/stargazers) – extension that provides OCaml language support for [VSCode](https://github.com/microsoft/vscode) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode?style=flat)](https://github.com/microsoft/vscode/stargazers)
  - [OCaml Debugger](https://github.com/hackwaly/ocamlearlybird) [![GitHub stars](https://img.shields.io/github/stars/hackwaly/ocamlearlybird?style=flat)](https://github.com/hackwaly/ocamlearlybird/stargazers) – extension that provides OCaml Debugger for [VSCode](https://github.com/microsoft/vscode) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode?style=flat)](https://github.com/microsoft/vscode/stargazers)
  - [Sublime better ocaml](https://github.com/whitequark/sublime-better-ocaml) [![GitHub stars](https://img.shields.io/github/stars/whitequark/sublime-better-ocaml?style=flat)](https://github.com/whitequark/sublime-better-ocaml/stargazers) – Better OCaml mode for Sublime Text.
    - [Sublime text package](https://github.com/def-lkb/sublime-text-merlin) [![GitHub stars](https://img.shields.io/github/stars/def-lkb/sublime-text-merlin?style=flat)](https://github.com/def-lkb/sublime-text-merlin/stargazers)
  - [ocp-index](http://www.typerex.org/ocp-index.html) – Easy access to the interface information of installed OCaml libraries. Provides standalone tools like `ocp-browser` and `ocp-grep`.
    - [ocp-browser](http://www.typerex.org/ocp-index.html#ocp-browser) – Small ncurses-based API and documentation browser.
    - [ocp-index-top](https://github.com/reynir/ocp-index-top) [![GitHub stars](https://img.shields.io/github/stars/reynir/ocp-index-top?style=flat)](https://github.com/reynir/ocp-index-top/stargazers) – Toplevel directive for looking up documentation using ocp-index.
    - [Sublime text package](https://sublime.wbond.net/packages/OCaml%20Autocompletion)
  - [ocp-indent](http://www.typerex.org/ocp-indent.html) – Indentation tool for OCaml, to be used from editors like Emacs and Vim.
    - [Vim plugin](https://github.com/def-lkb/ocp-indent-vim) [![GitHub stars](https://img.shields.io/github/stars/def-lkb/ocp-indent-vim?style=flat)](https://github.com/def-lkb/ocp-indent-vim/stargazers).
- **Code coverage**:
  - [Bisect_ppx](https://github.com/aantron/bisect_ppx) [![GitHub stars](https://img.shields.io/github/stars/aantron/bisect_ppx?style=flat)](https://github.com/aantron/bisect_ppx/stargazers)


## Exercises and Short Examples

- [99 problems](https://ocaml.org/learn/tutorials/99problems.html). 99% of the solutions are [here](https://github.com/MassD/99) [![GitHub stars](https://img.shields.io/github/stars/MassD/99?style=flat)](https://github.com/MassD/99/stargazers).
- [learn-ocaml-corpus](https://ocaml-sf.org/learn-ocaml-public/#activity=exercises). Corpus of beginner-to-advanced online exercises (including those from the OCaml MOOC) with automatic grading tests.
- [Rosetta Code](http://rosettacode.org/wiki/Category:OCaml)
- [OCaml at Exercism](http://exercism.io/languages/ocaml) – Exercism is your place to engage in thoughtful conversations about code. Explore simplicity, idiomatic language features, and expressive, readable code. [Solutions](https://github.com/exercism/xocaml) [![GitHub stars](https://img.shields.io/github/stars/exercism/xocaml?style=flat)](https://github.com/exercism/xocaml/stargazers).
- [Programming Language Examples Alike Cookbook](http://pleac.sourceforge.net/pleac_ocaml/index.html) - The OCaml section of the book is a free reference for solving common programming problems using OCaml.

## Formal Software Verification

- [Coq](https://coq.inria.fr/) – Coq is a formal proof management system. It provides a formal language to write mathematical definitions, executable algorithms, and theorems, together with an environment for semi-interactive development of machine-checked proofs.
- [Why3](http://why3.lri.fr/) – Why3 is a platform for deductive program verification. It provides a rich language for specification and programming, called WhyML, and relies on external theorem provers, both automated and interactive, to discharge verification conditions.
- [Alt-Ergo](http://alt-ergo.lri.fr/) – Alt-Ergo is an open-source SMT solver dedicated to the proof of mathematical formulas generated in the context of program verification.


## General

- [Functional Programming with OCaml](https://haifengl.wordpress.com/2014/06/17/ocaml-introduction/)
- [Python to OCaml: retrospective](http://roscidus.com/blog/blog/2014/06/06/python-to-ocaml-retrospective/)
- [OCaml for the Masses](http://queue.acm.org/detail.cfm?id=2038036)
- [Why We Use OCaml](https://espertech.wordpress.com/2014/07/15/why-we-use-ocaml)
- [Xen – OCaml Coding Considerations](http://wiki.xen.org/wiki/OCaml_Coding_Considerations)
- [Monads are a class of hard drugs](http://lambda-diode.com/programming/monads-are-a-class-of-hard-drugs)
- [Beginner's guide to OCaml](http://blog.nullspace.io/beginners-guide-to-ocaml-beginners-guides.html)
- [Why OCaml, why now?](http://spyder.wordpress.com/2014/03/16/why-ocaml-why-now/)
- [A blog about game development in OCaml](http://cranialburnout.blogspot.ca/)
- [(Functional) Alternatives to inheritance](http://ocamltutorials.blogspot.se/2013/06/alternatives-to-subtyping.html)
- [camlPDF](https://github.com/johnwhitington/camlpdf) [![GitHub stars](https://img.shields.io/github/stars/johnwhitington/camlpdf?style=flat)](https://github.com/johnwhitington/camlpdf/stargazers) – OCaml library for reading, writing and modifying PDF files.
- [slacko](https://github.com/Leonidas-from-XIV/slacko) [![GitHub stars](https://img.shields.io/github/stars/Leonidas-from-XIV/slacko?style=flat)](https://github.com/Leonidas-from-XIV/slacko/stargazers) – A neat interface for Slack in OCaml.
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/ocaml/) - Where X=OCaml.


## Graphics

- **2D**
  - [archimedes](http://archimedes.forge.ocamlcore.org/) — 2D plotting library.
  - [cairo2](https://github.com/Chris00/ocaml-cairo) [![GitHub stars](https://img.shields.io/github/stars/Chris00/ocaml-cairo?style=flat)](https://github.com/Chris00/ocaml-cairo/stargazers) — Binding to Cairo, a 2D Vector Graphics Library. Integrates well with lablgtk.
  - [Vg](https://github.com/dbuenzli/vg) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/vg?style=flat)](https://github.com/dbuenzli/vg/stargazers) – Declarative 2D vector graphics for OCaml.
- **3D**
  - [glMLite](https://github.com/fccm/glMLite) [![GitHub stars](https://img.shields.io/github/stars/fccm/glMLite?style=flat)](https://github.com/fccm/glMLite/stargazers) — OpenGL bindings for OCaml. Provides an (experimental) functional API. ([homepage](http://decapode314.free.fr/ocaml/GL/))
  - [lablgl](https://forge.ocamlcore.org/projects/lablgl/) — Interface to OpenGL. Integrates well with lablgtk.
  - [tgls](http://erratique.ch/software/tgls) — Thin bindings OpenGL 3.{2,3},4.{0,1,2,3,4} and OpenGL ES {2,3}.


## Internationalization

- [Camomile](https://github.com/yoriyuki/Camomile/) [![GitHub stars](https://img.shields.io/github/stars/yoriyuki/Camomile/?style=flat)](https://github.com/yoriyuki/Camomile//stargazers) — A Unicode library for OCaml.
- [ocaml-m17n](https://github.com/whitequark/ocaml-m17n) [![GitHub stars](https://img.shields.io/github/stars/whitequark/ocaml-m17n?style=flat)](https://github.com/whitequark/ocaml-m17n/stargazers) — Multilingualization for OCaml source code. Allows using Unicode identifiers in OCaml source code.
- [Uucd](https://github.com/dbuenzli/uucd) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/uucd?style=flat)](https://github.com/dbuenzli/uucd/stargazers) — Unicode character database decoder for OCaml.
- [Uucp](https://github.com/dbuenzli/uucp) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/uucp?style=flat)](https://github.com/dbuenzli/uucp/stargazers) — Unicode character properties for OCaml.
- [Uunf](https://github.com/dbuenzli/uunf) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/uunf?style=flat)](https://github.com/dbuenzli/uunf/stargazers) — Unicode text normalization for OCaml.
- [Uuseg](https://github.com/dbuenzli/uuseg) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/uuseg?style=flat)](https://github.com/dbuenzli/uuseg/stargazers) — Unicode text segmentation for OCaml.
- [Uutf](https://github.com/dbuenzli/uutf) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/uutf?style=flat)](https://github.com/dbuenzli/uutf/stargazers) — Non-blocking streaming Unicode codec for OCaml.


## User Interface

- [lablgtk](https://garrigue.github.io/lablgtk/) — GTK2 and GTK3 bindings for OCaml with various higher-level facilities to define GUIs.
- [lablqml](https://github.com/Kakadu/lablqml) [![GitHub stars](https://img.shields.io/github/stars/Kakadu/lablqml?style=flat)](https://github.com/Kakadu/lablqml/stargazers) – QML Qt5 bindings for OCaml.
- [labltk](https://forge.ocamlcore.org/projects/labltk/) — Interface to the Tcl/Tk GUI framework. In the standard distribution for ocaml <= 4.01.
- [TSDL](http://erratique.ch/software/tsdl) – Tsdl is an OCaml module providing thin bindings to the cross-platform SDL library.
- [Lambda-Term](https://github.com/ocaml-community/lambda-term) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/lambda-term?style=flat)](https://github.com/ocaml-community/lambda-term/stargazers) – Lambda-Term is a cross-platform library for manipulating the terminal. It provides an abstraction for keys, mouse events, and colors, as well as a set of widgets to write curses-like applications.
- [Notty](https://github.com/ocaml-community/notty-community) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/notty-community?style=flat)](https://github.com/ocaml-community/notty-community/stargazers) - Notty is a declarative terminal library for OCaml, structured around the notion of composable images.
- [ocaml-linenoise](https://github.com/ocaml-community/ocaml-linenoise) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/ocaml-linenoise?style=flat)](https://github.com/ocaml-community/ocaml-linenoise/stargazers) - Self-contained OCaml bindings to linenoise; easy high-level readline functionality in OCaml.


## Language-related

- [Higher-Rank Polymorphism in OCaml](http://devmusings.legiasoft.com/blog/2008/05/23/higher-rank_polymorphism_in_ocaml)
- [mikmatch](https://github.com/mjambon/mikmatch) [![GitHub stars](https://img.shields.io/github/stars/mjambon/mikmatch?style=flat)](https://github.com/mjambon/mikmatch/stargazers) – OCaml pattern-matching extended with regexps
- [Inlined records in constructors](https://www.lexifi.com/ocaml/inlined-records-constructors/)
- [Algebraic Data Types](https://espertech.wordpress.com/2014/07/30/algebraic-data-types/)
- [XEN – OCaml Best Practices for Developers](http://wiki.xen.org/wiki/OCaml_Best_Practices_for_Developers)
- [OCaml Style Guide (by Jane Street)](https://opensource.janestreet.com/standards/) - See also: [[1]](https://www.seas.upenn.edu/~cis500/cis500-f06/resources/programming_style.html), [[2]](http://www.cs.cornell.edu/Courses/cs312/2001sp/style.html), [[3]](https://www.seas.upenn.edu/~cis120/20fa/ocaml_style/).
- [A safe but strange way of modifying OCaml compiler](https://camlspotter.blogspot.com/2012/09/a-safe-but-strange-way-of-modifying.html)
- [Fiddling with the OCaml Type System](https://technotroph.wordpress.com/2013/10/25/fiddling-with-the-ocaml-type-system/)


## Large Source Code Examples

- [Base](https://github.com/janestreet/base) [![GitHub stars](https://img.shields.io/github/stars/janestreet/base?style=flat)](https://github.com/janestreet/base/stargazers) - Standard library for OCaml
- [cil](https://github.com/cil-project/cil) [![GitHub stars](https://img.shields.io/github/stars/cil-project/cil?style=flat)](https://github.com/cil-project/cil/stargazers) - C Intermediate Language
- [coq](https://github.com/coq/coq) [![GitHub stars](https://img.shields.io/github/stars/coq/coq?style=flat)](https://github.com/coq/coq/stargazers) - formal proof management system
- [frama-c](https://git.frama-c.com/pub/frama-c) - platform dedicated to the analysis of source code written in C
- [libguestfs](https://github.com/libguestfs/libguestfs) [![GitHub stars](https://img.shields.io/github/stars/libguestfs/libguestfs?style=flat)](https://github.com/libguestfs/libguestfs/stargazers) - library and tools for accessing and modifying virtual machine disk images
- [Liquidsoap](https://github.com/savonet/liquidsoap) [![GitHub stars](https://img.shields.io/github/stars/savonet/liquidsoap?style=flat)](https://github.com/savonet/liquidsoap/stargazers) - a swiss-army knife for multimedia streaming, notably used for netradios and webtvs
- [mirage](https://github.com/mirage/mirage) [![GitHub stars](https://img.shields.io/github/stars/mirage/mirage?style=flat)](https://github.com/mirage/mirage/stargazers) -  library operating system that constructs unikernels for secure, high-performance network applications across a variety of cloud computing and mobile platforms
- [MLDonkey](https://github.com/ygrek/mldonkey) [![GitHub stars](https://img.shields.io/github/stars/ygrek/mldonkey?style=flat)](https://github.com/ygrek/mldonkey/stargazers) - cross-platform multi-network peer-to-peer daemon
- [Oni2](https://github.com/onivim/oni2) [![GitHub stars](https://img.shields.io/github/stars/onivim/oni2?style=flat)](https://github.com/onivim/oni2/stargazers) - Native, lightweight modal code editor.
- [pfff](https://github.com/returntocorp/pfff) [![GitHub stars](https://img.shields.io/github/stars/returntocorp/pfff?style=flat)](https://github.com/returntocorp/pfff/stargazers) - an OCaml API to write static analysis, dynamic analysis, code visualizations, code navigations, or style-preserving source-to-source transformations such as refactorings on source code.
- [Tezos](https://gitlab.com/tezos/tezos) - a self-upgradable Proof of Stake blockchain
- [WHY3](https://gitlab.inria.fr/why3/why3) - platform for deductive program verification
- [xen-api](https://github.com/xapi-project/xen-api) [![GitHub stars](https://img.shields.io/github/stars/xapi-project/xen-api?style=flat)](https://github.com/xapi-project/xen-api/stargazers) - management stack that configures and controls Xen-enabled hosts and resource pools, and co-ordinates resources within the pool.

## Logging

- [dolog](https://github.com/UnixJunkie/dolog) [![GitHub stars](https://img.shields.io/github/stars/UnixJunkie/dolog?style=flat)](https://github.com/UnixJunkie/dolog/stargazers) – A dumb OCaml logger.
- [Volt](https://github.com/codinuum/volt) [![GitHub stars](https://img.shields.io/github/stars/codinuum/volt?style=flat)](https://github.com/codinuum/volt/stargazers) – A variant of the Bolt OCaml logging tool.
- [Logs](http://erratique.ch/software/logs) - Logs provides a logging infrastructure for OCaml.

## Machine Learning

- **Libraries**
	- [Ocaml-sklearn](https://github.com/lehy/ocaml-sklearn) [![GitHub stars](https://img.shields.io/github/stars/lehy/ocaml-sklearn?style=flat)](https://github.com/lehy/ocaml-sklearn/stargazers) scikit-learn for OCaml.
	- [Owl](https://ocaml.xyz/) - Scientific library with neural networks, algorithmic differentiation and ONNX support.
	- [Object detection convolutional neural network with OCaml (based on Owl)](https://github.com/owlbarn/owl_mask_rcnn) [![GitHub stars](https://img.shields.io/github/stars/owlbarn/owl_mask_rcnn?style=flat)](https://github.com/owlbarn/owl_mask_rcnn/stargazers).
	- [PyTorch bindings](https://github.com/LaurentMazare/ocaml-torch) [![GitHub stars](https://img.shields.io/github/stars/LaurentMazare/ocaml-torch?style=flat)](https://github.com/LaurentMazare/ocaml-torch/stargazers) - OCaml bindings for PyTorch.
  	- [Ocaml-NN](https://github.com/ck090/ocaml-nn/tree/main) [![GitHub stars](https://img.shields.io/github/stars/ck090/ocaml-nn/tree/main?style=flat)](https://github.com/ck090/ocaml-nn/tree/main/stargazers) - Fully functional monadic implementation of a Neural Network (FCNNs) in OCaml
- **Articles**
	- [Deep Learning with OCaml (PyTorch bindings)](https://blog.janestreet.com/deep-learning-experiments-in-ocaml/).
	- [Transfer Learning with OCaml (PyTorch bindings)](https://blog.janestreet.com/of-pythons-and-camels/).
	- [Reinforcement Learning with OCaml (PyTorch bindings)](https://blog.janestreet.com/playing-atari-games-with-ocaml-and-deep-rl/).

## Messaging

- [ocaml-zmq](https://github.com/issuu/ocaml-zmq) [![GitHub stars](https://img.shields.io/github/stars/issuu/ocaml-zmq?style=flat)](https://github.com/issuu/ocaml-zmq/stargazers) – ZeroMQ bindings for OCaml with Async and Lwt wrappers.
- [onanomsg](https://github.com/rgrinberg/onanomsg) [![GitHub stars](https://img.shields.io/github/stars/rgrinberg/onanomsg?style=flat)](https://github.com/rgrinberg/onanomsg/stargazers) – nanomsg bindings for OCaml.
- [Kafka](https://github.com/didier-wenzek/ocaml-kafka) [![GitHub stars](https://img.shields.io/github/stars/didier-wenzek/ocaml-kafka?style=flat)](https://github.com/didier-wenzek/ocaml-kafka/stargazers) – OCaml bindings for Apache Kafka.
- [AMQP](https://github.com/andersfugmann/amqp-client) [![GitHub stars](https://img.shields.io/github/stars/andersfugmann/amqp-client?style=flat)](https://github.com/andersfugmann/amqp-client/stargazers) – AMQP client library for Async and Lwt.
- [MPI](https://github.com/xavierleroy/ocamlmpi) [![GitHub stars](https://img.shields.io/github/stars/xavierleroy/ocamlmpi?style=flat)](https://github.com/xavierleroy/ocamlmpi/stargazers) – Message Passing Interface bindings for OCaml.
- [MQTT](https://github.com/j0sh/ocaml-mqtt) [![GitHub stars](https://img.shields.io/github/stars/j0sh/ocaml-mqtt?style=flat)](https://github.com/j0sh/ocaml-mqtt/stargazers) – OCaml implementation of the MQTT pubsub protocol.
- [capnp-ocaml](https://github.com/capnproto/capnp-ocaml) [![GitHub stars](https://img.shields.io/github/stars/capnproto/capnp-ocaml?style=flat)](https://github.com/capnproto/capnp-ocaml/stargazers) – OCaml code generator plugin for the Cap'n Proto serialization framework.

## Metaprogramming

- **Articles**:
  - [A Guide to Extension Points in OCaml](http://whitequark.org/blog/2014/04/16/a-guide-to-extension-points-in-ocaml/)
  - [Extension Points, or how OCaml is becoming more like Lisp](https://blogs.janestreet.com/extension-points-or-how-ocaml-is-becoming-more-like-lisp)
  - [Syntax extensions without Camlp4: let's do it!](https://www.lexifi.com/ocaml/syntax-extensions-without-camlp4-lets-do-it/)
  - [Reading Camlp4 – Ambassador to the Computers](https://ambassadortothecomputers.blogspot.com/p/reading-camlp4.html)
- **Syntax Extensions**:
  - [ppx_import](https://github.com/ocaml-ppx/ppx_import) [![GitHub stars](https://img.shields.io/github/stars/ocaml-ppx/ppx_import?style=flat)](https://github.com/ocaml-ppx/ppx_import/stargazers) – Import is a syntax extension that allows to pull in types or signatures from other compiled interface files.
  - [ppx_string_interpolate](https://github.com/sheijk/ppx_string_interpolate) [![GitHub stars](https://img.shields.io/github/stars/sheijk/ppx_string_interpolate?style=flat)](https://github.com/sheijk/ppx_string_interpolate/stargazers) – A simple ppx filter to support string interpolation like `[%str "value of foo is $(foo)"]`.
  - [ppx_monad](https://github.com/rizo/ppx_monad) [![GitHub stars](https://img.shields.io/github/stars/rizo/ppx_monad?style=flat)](https://github.com/rizo/ppx_monad/stargazers) – Monad syntax extension for OCaml.
  - [ppx_deriving_yojson](https://github.com/whitequark/ppx_deriving_yojson) [![GitHub stars](https://img.shields.io/github/stars/whitequark/ppx_deriving_yojson?style=flat)](https://github.com/whitequark/ppx_deriving_yojson/stargazers) – A Yojson codec generator for OCaml.
- **Tools and Language Extensions**:
  - [MetaOCaml](http://okmij.org/ftp/ML/MetaOCaml.html) – an OCaml dialect for multi-stage programming.
  - [Fan](http://bobzhang.github.io/fan/) – Fan is a compile-time metaprogramming system for OCaml, originally inspired from Camlp4. It's a combination of OCaml and Lispy Macros. It shares the same concrete syntax with OCaml.
  - [camlp5](https://camlp5.github.io/) - Camlp5 is a preprocessor-pretty-printer of OCaml.
  - [camlp4](http://caml.inria.fr/pub/docs/manual-camlp4/manual002.html) - Camlp4 is part of the standard OCaml distribution and is different from Camlp5.

## Metrics

- [prometheus](https://github.com/mirage/prometheus) [![GitHub stars](https://img.shields.io/github/stars/mirage/prometheus?style=flat)](https://github.com/mirage/prometheus/stargazers) – OCaml client library for Prometheus monitoring.

## Mobile Applications

- **Articles**:
  - [OCaml on iOS 7 Released](http://psellos.com/2014/08/2014.08.ocamlxarm-402.html)
  - [OCaml + Cordova = more secured, typed and hybrid mobile applications](https://dannywillems.github.io/2016/07/14/ocaml-cordova-secured-typed-hybrid-mobile-applications.html)
- **Bindings**:
  - [Cordova plugins](https://github.com/dannywillems/ocaml-cordova-plugin-list) [![GitHub stars](https://img.shields.io/github/stars/dannywillems/ocaml-cordova-plugin-list?style=flat)](https://github.com/dannywillems/ocaml-cordova-plugin-list/stargazers) – List of bindings to Cordova plugins. Get access to native device components like accelerometer, SMS, geolocation, etc in OCaml.


## Networking

- **HTTP Tools**:
  - [ocaml-cohttp](https://github.com/mirage/ocaml-cohttp) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-cohttp?style=flat)](https://github.com/mirage/ocaml-cohttp/stargazers) – Very lightweight HTTP server using Lwt or Async.
  - [ocurl](https://github.com/ygrek/ocurl) [![GitHub stars](https://img.shields.io/github/stars/ygrek/ocurl?style=flat)](https://github.com/ygrek/ocurl/stargazers) – OCaml bindings to libcurl.
  - [httpaf](https://github.com/inhabitedtype/httpaf) [![GitHub stars](https://img.shields.io/github/stars/inhabitedtype/httpaf?style=flat)](https://github.com/inhabitedtype/httpaf/stargazers) – A high performance, memory efficient, and scalable web server written in OCaml.
  - [piaf](https://github.com/anmonteiro/piaf) [![GitHub stars](https://img.shields.io/github/stars/anmonteiro/piaf?style=flat)](https://github.com/anmonteiro/piaf/stargazers) - Client/server library for HTTP/1.X / HTTP/2 written entirely in OCaml.
- [ocaml-dns](https://github.com/mirage/ocaml-dns) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-dns?style=flat)](https://github.com/mirage/ocaml-dns/stargazers) – A pure OCaml implementation of the DNS protocol.
- [fluent-logger](https://github.com/fluent/fluent-logger-ocaml) [![GitHub stars](https://img.shields.io/github/stars/fluent/fluent-logger-ocaml?style=flat)](https://github.com/fluent/fluent-logger-ocaml/stargazers) – Fluentd logger for OCaml.
- [charrua-unix](https://github.com/haesbaert/charrua-unix) [![GitHub stars](https://img.shields.io/github/stars/haesbaert/charrua-unix?style=flat)](https://github.com/haesbaert/charrua-unix/stargazers) - charrua-unix is a Unix DHCP daemon based on [charrua-core](https://github.com/haesbaert/charrua-core) [![GitHub stars](https://img.shields.io/github/stars/haesbaert/charrua-core?style=flat)](https://github.com/haesbaert/charrua-core/stargazers).


## Online Courses

- [OCaml MOOC: Introduction to Functional Programming in OCaml](https://www.fun-mooc.fr/en/courses/introduction-functional-programming-ocaml/) - Videos available in [this playlist](https://www.youtube.com/playlist?list=PLTBEN441uEY36t5CCrJkdTSv588d3nWN5) of the [OCaml Software Foundation](https://ocaml-sf.org/) YouTube channel.
- [Cornell University – Data Structures and Functional Programming](http://www.cs.cornell.edu/Courses/cs3110/2014fa/course_info.php).
- [Princeton University - Functional programming in OCaml](http://www.cs.princeton.edu/~dpw/courses/cos326-12/).
- [University of Illinois](https://courses.engr.illinois.edu/cs421/fa2014/) - Course that uses OCaml to teach functional programming and programming language design


## Package Management
- **Distribution**:
  - [OPAM](http://opam.ocamlpro.com/) – A flexible Git-friendly package manager with multiple compiler support.
  - [ocamlfind](http://projects.camlcity.org/projects/findlib.html) — Local OCaml library manager. Used by most of the OCaml ecosystem.
  - [OCaml for Windows](https://fdopen.github.io/opam-repository-mingw) - opam repository and experimental build for Windows (deprecated since 2021).
  - [Diskuv OCaml](https://github.com/diskuv/dkml-installer-ocaml#readme) - Diskuv OCaml distribution for Windows.
  - [makorel](https://github.com/sagotch/makorel) [![GitHub stars](https://img.shields.io/github/stars/sagotch/makorel?style=flat)](https://github.com/sagotch/makorel/stargazers) – Release OPAM packages easily.
  - [esy](https://github.com/esy/esy) [![GitHub stars](https://img.shields.io/github/stars/esy/esy?style=flat)](https://github.com/esy/esy/stargazers) - package.json workflow for native development with Reason/OCaml.

- **Build Tools**:
  - [dune](https://github.com/ocaml/dune) [![GitHub stars](https://img.shields.io/github/stars/ocaml/dune?style=flat)](https://github.com/ocaml/dune/stargazers) – A composable and opinionated build system for OCaml (former jbuilder)
  - [Oasis](http://oasis.forge.ocamlcore.org/) - A tool to integrate a configure, build and install system in your OCaml project. It helps to create standard entry points in your build system and allows external tools to analyse your project easily.
    - [oasis2opam](https://github.com/ocaml/oasis2opam) [![GitHub stars](https://img.shields.io/github/stars/ocaml/oasis2opam?style=flat)](https://github.com/ocaml/oasis2opam/stargazers) — Tool to convert OASIS metadata to OPAM package descriptions.
  - [obuild](https://github.com/ocaml-obuild/obuild) [![GitHub stars](https://img.shields.io/github/stars/ocaml-obuild/obuild?style=flat)](https://github.com/ocaml-obuild/obuild/stargazers) – Simple package build system for ocaml.
  - [ocaml-makefile](https://github.com/mmottl/ocaml-makefile) [![GitHub stars](https://img.shields.io/github/stars/mmottl/ocaml-makefile?style=flat)](https://github.com/mmottl/ocaml-makefile/stargazers) — Easy to use Makefile for small to medium-sized OCaml-projects.
  - [topkg](https://github.com/dbuenzli/topkg) [![GitHub stars](https://img.shields.io/github/stars/dbuenzli/topkg?style=flat)](https://github.com/dbuenzli/topkg/stargazers) — OPAM-aware packaging system using ocamlbuild.
  - [Bazel](https://github.com/jin/rules_ocaml) [![GitHub stars](https://img.shields.io/github/stars/jin/rules_ocaml?style=flat)](https://github.com/jin/rules_ocaml/stargazers) - OCaml rules for [Bazel](https://bazel.build/), Google's multi-language and platform build tool.

## Parallelism

(_Note: Sorted from the easier to use to the more flexible._)

- **Libraries**:
  - [Parmap](http://rdicosmo.github.io/parmap/) — Provides easy-to-use parallel map and fold functions.
  - [ForkWork](https://github.com/mlin/forkwork) [![GitHub stars](https://img.shields.io/github/stars/mlin/forkwork?style=flat)](https://github.com/mlin/forkwork/stargazers) — A simple library for forking child processes to perform work on multiple cores.
  - [Functory](http://functory.lri.fr/About.html) — A distributed computing library which facilitates distributed execution of parallelizable computations in a seamless fashion.
  - [Rpc.Parallel](https://github.com/janestreet/rpc_parallel) [![GitHub stars](https://img.shields.io/github/stars/janestreet/rpc_parallel?style=flat)](https://github.com/janestreet/rpc_parallel/stargazers) — A library for spawning processes on a cluster of machines, and passing typed messages between them.
  - [Ocamlnet](http://projects.camlcity.org/projects/ocamlnet.html) — An enhanced system platform library. Contains the `netmulticore` library to compute tasks on as many cores of the machine as needed.
  - [Nproc](https://github.com/MyLifeLabs/nproc) [![GitHub stars](https://img.shields.io/github/stars/MyLifeLabs/nproc?style=flat)](https://github.com/MyLifeLabs/nproc/stargazers) – Process pool implementation for OCaml.
  - [Parany](https://github.com/UnixJunkie/parany) [![GitHub stars](https://img.shields.io/github/stars/UnixJunkie/parany?style=flat)](https://github.com/UnixJunkie/parany/stargazers) – Parallelize computation over independent items, even if there is an infinite number of them.
  - [Sklml](http://sklml.inria.fr) – Functional parallel skeleton compiler and programming system for OCaml programs.
  - [SPOC](https://github.com/mathiasbourgoin/SPOC) [![GitHub stars](https://img.shields.io/github/stars/mathiasbourgoin/SPOC?style=flat)](https://github.com/mathiasbourgoin/SPOC/stargazers) - Libraries and syntax extensions to offload intensive computations to parallel accelerators (multicore CPUs, GPUs and other accelerators compatible with GPGPU frameworks).

- **Articles**:
  - [What is the state of OCaml's parallelization abilities?](https://stackoverflow.com/questions/6588500/what-is-the-state-of-ocamls-parallelization-abilities)
  - [Parallel programming in multicore OCaml](https://github.com/ocaml-multicore/parallel-programming-in-multicore-ocaml) [![GitHub stars](https://img.shields.io/github/stars/ocaml-multicore/parallel-programming-in-multicore-ocaml?style=flat)](https://github.com/ocaml-multicore/parallel-programming-in-multicore-ocaml/stargazers)
  - [Parallelism programming](https://v2.ocaml.org/releases/5.0/htmlman/parallelism.html) from the officiel OCaml manual 
  - [Awesome multicore OCaml](https://github.com/ocaml-multicore/awesome-multicore-ocaml) [![GitHub stars](https://img.shields.io/github/stars/ocaml-multicore/awesome-multicore-ocaml?style=flat)](https://github.com/ocaml-multicore/awesome-multicore-ocaml/stargazers). A compilation of resources

## Printers helpers

- Reason's native [**Console.log**](https://github.com/reasonml/reason-native/tree/master/src/console#consoleloganything)
- [**Dum**](https://github.com/mjambon/dum#readme)
- [**Inspect**](https://github.com/krohrer/caml-inspect#readme)
- [**ppx_deriving** ](https://github.com/ocaml-ppx/ppx_deriving#usage)’s `[@@deriving show]`.
- [**refl** ](https://github.com/thierry-martinez/refl#basic-usage), a ppx_deriving-like.
- [**lrt** ](https://github.com/LexiFi/lrt#getting-started), another ppx_deriving-like.
- [**tpf** ](https://github.com/pqwy/tpf#readme), again a ppx_deriving-like.
- [**typerep** ](https://github.com/janestreet/typerep) [![GitHub stars](https://img.shields.io/github/stars/janestreet/typerep?style=flat)](https://github.com/janestreet/typerep/stargazers), probably a ppx_deriving-like with ppx_typerep_conv.
- [**repr**](https://mirage.github.io/repr/repr/Repr/index.html#val-pp_json), which appears to have the user build the type representation manually from combinators in addition to also having the user pass it where needed.
- [**data-encoding**](https://gitlab.com/nomadic-labs/data-encoding/-/blob/master/src/tutorial.md#how-to-build-an-encoding), also fully manual.
- [**cmon** ](https://github.com/let-def/cmon#documentation), fully manual.
- [**dyn** ](https://github.com/ocaml/dune/blob/4b95cd3d1b3a62e69a9a9db2bc4af2f9fd2e56d8/otherlibs/dyn/dyn.mli) [![GitHub stars](https://img.shields.io/github/stars/ocaml/dune/blob/4b95cd3d1b3a62e69a9a9db2bc4af2f9fd2e56d8/otherlibs/dyn/dyn.mli?style=flat)](https://github.com/ocaml/dune/blob/4b95cd3d1b3a62e69a9a9db2bc4af2f9fd2e56d8/otherlibs/dyn/dyn.mli/stargazers) in Dune. It appears to also be fully manual.
- [**Genprint** ](https://github.com/progman1/genprintlib#readme)
- [**OCaml@p** ](https://github.com/tsubame-sp/ocaml_at_p#readme)


## Project Starter Templates

- [drom](https://github.com/OCamlPro/drom/) [![GitHub stars](https://img.shields.io/github/stars/OCamlPro/drom/?style=flat)](https://github.com/OCamlPro/drom//stargazers) - The drom tool is a wrapper over opam/dune in an attempt to provide a cargo-like user experience.
- [spin](https://github.com/tmattio/spin) [![GitHub stars](https://img.shields.io/github/stars/tmattio/spin?style=flat)](https://github.com/tmattio/spin/stargazers) - Reason and Ocaml project generator
- [modern-ocaml](https://github.com/Khady/modern-ocaml) [![GitHub stars](https://img.shields.io/github/stars/Khady/modern-ocaml?style=flat)](https://github.com/Khady/modern-ocaml/stargazers) - Template for an ocaml project with modern tooling

## Questions

- [OCaml polymorphism example other than template function?](https://stackoverflow.com/questions/14440531/ocaml-polymorphism-example-other-than-template-function)
- [OCaml - polymorphic print and type losing](https://stackoverflow.com/questions/7442449/ocaml-polymorphic-print-and-type-losing)


# Science and Technical Computing

- [biocaml](https://github.com/biocaml/biocaml) [![GitHub stars](https://img.shields.io/github/stars/biocaml/biocaml?style=flat)](https://github.com/biocaml/biocaml/stargazers) – OCaml Bioinformatics Library <http://biocaml.org>.
- [bistro](https://github.com/pveber/bistro) [![GitHub stars](https://img.shields.io/github/stars/pveber/bistro?style=flat)](https://github.com/pveber/bistro/stargazers) – OCaml library for building bioinformatics pipelines.
- [lacaml](https://mmottl.github.io/lacaml/) - OCaml bindings for BLAS/LAPACK (high-performance linear algebra Fortran libraries).
- [obandit](http://freux.fr/oss/obandit.html) - OCaml library for multi-armed bandits.
- [onumerical](https://github.com/cheshire/onumerical) [![GitHub stars](https://img.shields.io/github/stars/cheshire/onumerical?style=flat)](https://github.com/cheshire/onumerical/stargazers) – Numerical library for OCaml.
- [oml](https://github.com/hammerlab/oml) [![GitHub stars](https://img.shields.io/github/stars/hammerlab/oml?style=flat)](https://github.com/hammerlab/oml/stargazers) - OCaml library for general numerical work.
- [ocephes](https://github.com/rleonid/ocephes) [![GitHub stars](https://img.shields.io/github/stars/rleonid/ocephes?style=flat)](https://github.com/rleonid/ocephes/stargazers) - Bindings to frequently used `C` special functions library.
- [slap](https://github.com/akabe/slap) [![GitHub stars](https://img.shields.io/github/stars/akabe/slap?style=flat)](https://github.com/akabe/slap/stargazers) - A linear algebra library in OCaml with type-based static size checking for matrix operations.
- [tensorflow-ocaml](https://github.com/LaurentMazare/tensorflow-ocaml) [![GitHub stars](https://img.shields.io/github/stars/LaurentMazare/tensorflow-ocaml?style=flat)](https://github.com/LaurentMazare/tensorflow-ocaml/stargazers) – OCaml bindings for TensorFlow.
- [owl](https://github.com/owlbarn/owl) [![GitHub stars](https://img.shields.io/github/stars/owlbarn/owl?style=flat)](https://github.com/owlbarn/owl/stargazers) - OCaml numerical library: dense and sparse matrix, linear algebra, regressions, maths and stats functions.
- [WHIZARD](https://whizard.hepforge.org/) - A system designed for the efficient calculation of multi-particle scattering cross sections and simulated event samples.


## Regular Expressions

- [Re](https://github.com/ocaml/ocaml-re) [![GitHub stars](https://img.shields.io/github/stars/ocaml/ocaml-re?style=flat)](https://github.com/ocaml/ocaml-re/stargazers) – a pure OCaml regular expressions library with combinators, supporting several formats (glob, posix, str, etc.).
- [ocaml-pcre](https://github.com/mmottl/pcre-ocaml) [![GitHub stars](https://img.shields.io/github/stars/mmottl/pcre-ocaml?style=flat)](https://github.com/mmottl/pcre-ocaml/stargazers) – bindings to the PCRE library (perl-compatible regular expressions)
- [Humane-re](https://github.com/rgrinberg/humane-re) [![GitHub stars](https://img.shields.io/github/stars/rgrinberg/humane-re?style=flat)](https://github.com/rgrinberg/humane-re/stargazers) – Humane-re attempts to provide an easy interface for 90% of your regex needs. Courtesy of ocaml-re.
- [Tyre](https://github.com/Drup/tyre) [![GitHub stars](https://img.shields.io/github/stars/Drup/tyre?style=flat)](https://github.com/Drup/tyre/stargazers) - Tyre is a set of combinators to build type-safe regular expressions, allowing automatic extraction and modification of matched groups.


## Security and Cryptography

- [ocaml-tls](https://github.com/mirleft/ocaml-tls) [![GitHub stars](https://img.shields.io/github/stars/mirleft/ocaml-tls?style=flat)](https://github.com/mirleft/ocaml-tls/stargazers) – TLS in pure OCaml.
- [Digestif](https://github.com/mirage/digestif) [![GitHub stars](https://img.shields.io/github/stars/mirage/digestif?style=flat)](https://github.com/mirage/digestif/stargazers) - Hash algorithms (like SHA* or BLAKE2*) in OCaml and C.
- [cryptokit](https://github.com/xavierleroy/cryptokit) [![GitHub stars](https://img.shields.io/github/stars/xavierleroy/cryptokit?style=flat)](https://github.com/xavierleroy/cryptokit/stargazers) – The Cryptokit library for OCaml provides a variety of cryptographic primitives that can be used to implement cryptographic protocols in security-sensitive applications.
- [nocoiner](https://github.com/marcoonroad/nocoiner) [![GitHub stars](https://img.shields.io/github/stars/marcoonroad/nocoiner?style=flat)](https://github.com/marcoonroad/nocoiner/stargazers) - A Commitment scheme library for Multi-party computations such as online auctions and gambling.
- [nocrypto](https://github.com/mirleft/ocaml-nocrypto) [![GitHub stars](https://img.shields.io/github/stars/mirleft/ocaml-nocrypto?style=flat)](https://github.com/mirleft/ocaml-nocrypto/stargazers) – A small cryptographic library behind the ocaml-tls project. It is built to be straightforward to use, adhere to functional programming principles, and able to run in a Xen-based unikernel.

> Note: The differences between `nocrypto` and `cryptokit` cryptographic libraries are described in the following blog post: [OCaml-TLS: building the nocrypto library core](https://mirage.io/blog/introducing-nocrypto).


## Semantic Technology

- [OCaml-RDF](https://framagit.org/zoggy/ocaml-rdf) – OCaml library to manipulate RDF graphs and execute Sparql queries.


## Serialization

- [atdgen](https://github.com/ahrefs/atd) [![GitHub stars](https://img.shields.io/github/stars/ahrefs/atd?style=flat)](https://github.com/ahrefs/atd/stargazers) — A serialization compiler for multiple languages (OCaml, Java, Python, Scala, Typescript) with a Binou or JSON format
- [bencode](https://github.com/rgrinberg/bencode) [![GitHub stars](https://img.shields.io/github/stars/rgrinberg/bencode?style=flat)](https://github.com/rgrinberg/bencode/stargazers) — Bencode (.torrent file format) reader/writer.
- [biniou](https://github.com/mjambon/biniou) [![GitHub stars](https://img.shields.io/github/stars/mjambon/biniou?style=flat)](https://github.com/mjambon/biniou/stargazers) – Extensible binary data format, like JSON but faster.
- [cbor](https://github.com/ygrek/ocaml-cbor) [![GitHub stars](https://img.shields.io/github/stars/ygrek/ocaml-cbor?style=flat)](https://github.com/ygrek/ocaml-cbor/stargazers) —  OCaml native [CBOR](https://cbor.io/) decoder/encoder.
- [jsonm](http://erratique.ch/software/jsonm) — Non-blocking streaming JSON codec for OCaml.
- [xmlm](http://erratique.ch/software/xmlm) — A streaming codec to decode and encode the XML data format.
- [yojson](https://github.com/ocaml-community/yojson) [![GitHub stars](https://img.shields.io/github/stars/ocaml-community/yojson?style=flat)](https://github.com/ocaml-community/yojson/stargazers) — An optimized parsing and printing library for the JSON format.
- [sexplib](https://github.com/janestreet/sexplib) [![GitHub stars](https://img.shields.io/github/stars/janestreet/sexplib?style=flat)](https://github.com/janestreet/sexplib/stargazers) – A S-expression parser and printer


## System Programming

- [Mirage OS](https://github.com/mirage/mirage) [![GitHub stars](https://img.shields.io/github/stars/mirage/mirage?style=flat)](https://github.com/mirage/mirage/stargazers) – Mirage is a programming framework for constructing secure, high-performance network applications across a variety of cloud computing and mobile platforms.
- [ocaml-fat](https://github.com/mirage/ocaml-fat) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-fat?style=flat)](https://github.com/mirage/ocaml-fat/stargazers) – Read and write FAT-format filesystems from OCaml.
- [ocaml-git](https://github.com/mirage/ocaml-git) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-git?style=flat)](https://github.com/mirage/ocaml-git/stargazers) – Pure OCaml low-level git bindings.
- [ocaml-vchan](https://github.com/mirage/ocaml-vchan) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-vchan?style=flat)](https://github.com/mirage/ocaml-vchan/stargazers) – Pure OCaml implementation of the "vchan" shared-memory communication protocol.

- **Embedded systems**
  - [OMicroB](https://github.com/stevenvar/omicrob) [![GitHub stars](https://img.shields.io/github/stars/stevenvar/omicrob?style=flat)](https://github.com/stevenvar/omicrob/stargazers) - A virtual machine designed to run OCaml bytecode on AVR (Arduino for instance) micro-controlers.
  - [OCaPIC](http://www.algo-prog.info/ocapic/web/index.php?id=OCAPIC:OCAPIC) - An OCaml virtual machine for PIC18 micro-controlers.
  - [ocaml-esp32](https://github.com/sadiqj/ocaml-esp32) [![GitHub stars](https://img.shields.io/github/stars/sadiqj/ocaml-esp32?style=flat)](https://github.com/sadiqj/ocaml-esp32/stargazers) - A compiler for ESP32 SoC.


## Testing

- [Alcotest](https://github.com/mirage/alcotest) [![GitHub stars](https://img.shields.io/github/stars/mirage/alcotest?style=flat)](https://github.com/mirage/alcotest/stargazers) – A lightweight and colourful test framework.
- [OUnit](http://ounit.forge.ocamlcore.org/) – OUnit is a unit test framework for OCaml. It allows one to easily create unit-tests for OCaml code. It is based on HUnit, a unit testing framework for Haskell.
- [QCheck](https://github.com/c-cube/qcheck) [![GitHub stars](https://img.shields.io/github/stars/c-cube/qcheck?style=flat)](https://github.com/c-cube/qcheck/stargazers) — QCheck is a property testing library inspired from Haskell's QuickCheck
- [iTeML](https://github.com/vincent-hugot/iTeML) [![GitHub stars](https://img.shields.io/github/stars/vincent-hugot/iTeML?style=flat)](https://github.com/vincent-hugot/iTeML/stargazers) (formerly known as [qtest](http://batteries.vhugot.com/qtest/))  — supports inline pragma's to generate tests.
- [Kaputt](http://kaputt.x9c.fr/) —  comprehensive testing framework.
- [Pa_test](https://ocaml.janestreet.com/ocaml-core/111.28.00/doc/pa_test) —  General inline testing macro's.
- [TestSimple](https://github.com/hcarty/ocaml-testsimple) [![GitHub stars](https://img.shields.io/github/stars/hcarty/ocaml-testsimple?style=flat)](https://github.com/hcarty/ocaml-testsimple/stargazers) - A lightweight unit testing framework compatible with the [Test Anything Protocol](https://testanything.org/).
- [expect-test](https://github.com/janestreet/ppx_expect) [![GitHub stars](https://img.shields.io/github/stars/janestreet/ppx_expect?style=flat)](https://github.com/janestreet/ppx_expect/stargazers) — A framework for writing tests in OCaml, similar to [Cram](https://bitheap.org/cram/), developed by [JaneStreet](https://blog.janestreet.com/testing-with-expectations/). 


## Utilities

- [ocaml-cuid](https://github.com/marcoonroad/ocaml-cuid) [![GitHub stars](https://img.shields.io/github/stars/marcoonroad/ocaml-cuid?style=flat)](https://github.com/marcoonroad/ocaml-cuid/stargazers) - Collision-resistant IDs for server scalability & database performance.
- [Validate](https://github.com/Axot017/validate) [![GitHub stars](https://img.shields.io/github/stars/Axot017/validate?style=flat)](https://github.com/Axot017/validate/stargazers) - PPX deriver designed to streamline the process of validating records.
- [Uuidm](https://erratique.ch/software/uuidm) - Uuidm is an OCaml module implementing 128-bit universally unique identifiers version 3, 5 (name based with MD5, SHA-1 hashing) and 4 (random based) according to RFC 4122.
- [sqids-ocaml](https://github.com/sqids/sqids-ocaml) [![GitHub stars](https://img.shields.io/github/stars/sqids/sqids-ocaml?style=flat)](https://github.com/sqids/sqids-ocaml/stargazers) - Official OCaml port of Sqids. Generate short unique IDs from numbers.


## Web Development

- **Frameworks**:
  - [Opium](https://github.com/rgrinberg/opium) [![GitHub stars](https://img.shields.io/github/stars/rgrinberg/opium?style=flat)](https://github.com/rgrinberg/opium/stargazers) – Sinatra like web toolkit for OCaml.
  - [Ocsigen Eliom](http://ocsigen.org/eliom/) – Eliom is a full-featured multi-tier framework, for developing multi-platform Web and mobile apps as 100% OCaml distributed applications. It can also be used for more traditional Web or mobile apps: Web sites, single page applications, REST API, etc.
  - [Dream](https://camlworks.github.io/dream/) - Tidy Web framework for OCaml and ReasonML
  - [webmachine](https://github.com/inhabitedtype/ocaml-webmachine) [![GitHub stars](https://img.shields.io/github/stars/inhabitedtype/ocaml-webmachine?style=flat)](https://github.com/inhabitedtype/ocaml-webmachine/stargazers) – A REST toolkit for OCaml. OCaml webmachine is a layer on top of cohttp that implements a state-machine-based HTTP request processor. It's particularly well-suited for writing RESTful APIs. As the name suggests, this is an OCaml port of the webmachine project.
  - [incr_dom](https://github.com/janestreet/incr_dom) [![GitHub stars](https://img.shields.io/github/stars/janestreet/incr_dom?style=flat)](https://github.com/janestreet/incr_dom/stargazers) - A library for building dynamic webapps, using Js_of_ocaml
  - [fmlib_browser](https://hbr.github.io/fmlib/odoc/fmlib_browser/doc_overview.html) - a library which helps to write web applications which run in the browser in a pure functional style.
  - [ocaml-vdom](https://github.com/LexiFi/ocaml-vdom) [![GitHub stars](https://img.shields.io/github/stars/LexiFi/ocaml-vdom?style=flat)](https://github.com/LexiFi/ocaml-vdom/stargazers) - Elm architecture and (V)DOM for OCaml

- **Tools**:
  - [COW](https://github.com/mirage/ocaml-cow) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-cow?style=flat)](https://github.com/mirage/ocaml-cow/stargazers) – Caml on the Web (COW) is a set of parsers and syntax extensions to let you manipulate HTML, CSS, XML, JSON and Markdown directly from OCaml code.
  - [Ocamlnet](http://projects.camlcity.org/projects/ocamlnet.html)
    has many relevant web libraries —
    [Nethtml](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Nethtml.html)
    html parser,
    [Netasn1](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Netasn1.html)
    for ASN.1 parsing,
    [Netencoding](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Netencoding.html)
    for Base64, Quoted Printable, URL encoding and HTML escaping,
    [Netmime](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Netmime.html)
    for MIME processing, etc. See the [list of
    modules](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/index.html)
    in Ocamlnet's manual.
  - [tyxml](http://ocsigen.org/tyxml) — Library to build valid (according to the W3C spec) Html and Svg trees.
  - [js_of_ocaml](http://ocsigen.org/js_of_ocaml) – Js_of_ocaml is a compiler of OCaml bytecode to Javascript. It makes it possible to run Ocaml programs in a Web browser.
    - [commonjs_of_ocaml](https://github.com/AngryLawyer/commonjs_of_ocaml) [![GitHub stars](https://img.shields.io/github/stars/AngryLawyer/commonjs_of_ocaml?style=flat)](https://github.com/AngryLawyer/commonjs_of_ocaml/stargazers) - Easily import and export CommonJS modules from a js_of_ocaml project.
  - [ReScript](https://rescript-lang.org/) - ReScript is a robustly typed language that compiles to efficient and human-readable JavaScript.
  - [ocaml-uri](https://github.com/mirage/ocaml-uri) [![GitHub stars](https://img.shields.io/github/stars/mirage/ocaml-uri?style=flat)](https://github.com/mirage/ocaml-uri/stargazers) – RFC3986 URI parsing library.
  - [Goji](https://github.com/klakplok/goji) [![GitHub stars](https://img.shields.io/github/stars/klakplok/goji?style=flat)](https://github.com/klakplok/goji/stargazers) – An OCaml bindings generator for JavaScript libraries.
  - [Syndic](https://github.com/Cumulus/Syndic) [![GitHub stars](https://img.shields.io/github/stars/Cumulus/Syndic?style=flat)](https://github.com/Cumulus/Syndic/stargazers) – RSS and Atom feed parsing
  - [ocaml-mustache](https://github.com/rgrinberg/ocaml-mustache) [![GitHub stars](https://img.shields.io/github/stars/rgrinberg/ocaml-mustache?style=flat)](https://github.com/rgrinberg/ocaml-mustache/stargazers) – mustache.js logic-less templates in OCaml.
  - [atdjs](https://github.com/barko/atdjs) [![GitHub stars](https://img.shields.io/github/stars/barko/atdjs?style=flat)](https://github.com/barko/atdjs/stargazers) – atd code generator (serialization) for OCaml/js_of_ocaml.
  - [jingoo](https://github.com/tategakibunko/jingoo) [![GitHub stars](https://img.shields.io/github/stars/tategakibunko/jingoo?style=flat)](https://github.com/tategakibunko/jingoo/stargazers) – OCaml template engine almost compatible with jinja2.
  - [dispatch](https://github.com/inhabitedtype/ocaml-dispatch) [![GitHub stars](https://img.shields.io/github/stars/inhabitedtype/ocaml-dispatch?style=flat)](https://github.com/inhabitedtype/ocaml-dispatch/stargazers) – Path-based dispatching for client- and server-side applications.
  - [Lambda Soup](https://github.com/aantron/lambda-soup) [![GitHub stars](https://img.shields.io/github/stars/aantron/lambda-soup?style=flat)](https://github.com/aantron/lambda-soup/stargazers) - Functional HTML scraping and manipulation with CSS selectors, à la Python's Beautiful Soup.
  - [Markup.ml](https://github.com/aantron/markup.ml) [![GitHub stars](https://img.shields.io/github/stars/aantron/markup.ml?style=flat)](https://github.com/aantron/markup.ml/stargazers) - Error-recovering streaming HTML5 and XML parsers, serializers.
  - [gen_js_api](https://github.com/LexiFi/gen_js_api) [![GitHub stars](https://img.shields.io/github/stars/LexiFi/gen_js_api?style=flat)](https://github.com/LexiFi/gen_js_api/stargazers) - gen_js_api aims at simplifying the creation of OCaml bindings for Javascript libraries.
  - [routes](https://github.com/anuragsoni/routes) [![GitHub stars](https://img.shields.io/github/stars/anuragsoni/routes?style=flat)](https://github.com/anuragsoni/routes/stargazers) - Typed routes for OCaml/ReasonML web applications.

- **Open Source Projects**:
  - [Cumulus](https://github.com/Cumulus/Cumulus) [![GitHub stars](https://img.shields.io/github/stars/Cumulus/Cumulus?style=flat)](https://github.com/Cumulus/Cumulus/stargazers) – Hacker news like website with the OCaml framework Ocsigen

* * *

_Inspired by awesome projects line. Discover [more awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers) :sparkles:._
