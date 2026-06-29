# D

[![GitHub stars](https://img.shields.io/github/stars/dlang-community/awesome-d?style=flat)](https://github.com/dlang-community/awesome-d/stargazers)

# Awesome D [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome D frameworks, libraries and software. Inspired by [awesome-python](https://github.com/vinta/awesome-python) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers).

Most documents and links are collected from the [D forum](https://forum.dlang.org), the [D wiki](https://wiki.dlang.org), and the [D package repository](https://code.dlang.org). Exploring GitHub is also helpful, as many libraries are hosted there. If you know of an interesting D project, please let us know via [GitHub issues](https://github.com/dlang-community/awesome-d/issues) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/awesome-d/issues?style=flat)](https://github.com/dlang-community/awesome-d/issues/stargazers) or by [editing this file](https://github.com/dlang-community/awesome-d/edit/master/README.md) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/awesome-d/edit/master/README.md?style=flat)](https://github.com/dlang-community/awesome-d/edit/master/README.md/stargazers).

## Contents

* Basic Information
	* [Official Website](#official-websites)
  		* [Status Page](#status-page)
	* [Getting Help](#getting-help)
	* [People](#people)
	* [Events](#events)
	* [Organizations](#organizations)
* Documents
	* [Books](#books)
	* [Tutorials](#tutorials)
	* [Blogs](#blogs)
	* [Articles](#articles)
* Language Related
	* [Package Management](#package-management)
	* [Compilers](#compilers)
	* [Alternative / WIP Compilers](#alternative--wip-compilers)
	* [Dev Tools](#dev-tools)
	* [Build Tools](#build-tools)
	* [IDEs & Editors](#ides--editors)
	* [Lexers, Parsers & Generators](#lexers-parsers--generators)
	* [Preprocessors](#preprocessors)
	* [Version Managers](#version-managers)
* Continuous Integration
	* [GitHub Actions](#github-actions)
	* [Testing Frameworks](#testing-frameworks)
* Languages
	* [Programming Languages](#programming-languages)
* OS
	* [Operating Systems](#operating-systems)
	* [Bare Metal / Kernel Development](#bare-metal--kernel-development)
* Common
	* [General Containers](#general-containers)
	* [Core Utilities](#core-utilities)
* Networking / Web
	* [Web Frameworks](#web-frameworks)
	* [Data Serialization](#data-serialization)
* Database
	* [Database Clients](#database-clients)
* CLI
	* [CLI Libraries](#cli-libraries)
	* [CLI Applications](#cli-applications)
* GUI
	* [GUI Libraries](#gui-libraries)
	* [GUI Applications](#gui-applications)
* Game Development
	* [Game Bindings](#game-bindings)
	* [Game Libraries](#game-libraries)
	* [Games](#games)
* Internationalization (i18n) / Globalization
	* [Internationalization](#internationalization)
* Image Processing
	* [Image Processing](#image-processing)
* Machine Learning
	* [Machine Learning](#machine-learning)
	* [Parallel Computing](#parallel-computing)
* Scientific
	* [Scientific](#scientific)
	* [Language Processing](#language-processing)
* Others
	* [Text Processing](#text-processing)
	* [Logging](#logging)
	* [Configuration](#configuration)
	* [BlogEngine](#blog-engine)
	* [Dependency Injection](#dependency-injection)
	* [Cryptography](#cryptography)
	* [Unmaintained](#unmaintained)

## Official Websites

*Official website URLs for D.*

* [dlang.org](https://dlang.org) - Official website for D.
* [wiki.dlang.org](https://wiki.dlang.org) - Official wiki for D.
* [blog.dlang.org](https://dlang.org/blog/) - Official blog for D.
* [forum.dlang.org](https://forum.dlang.org/) - Official forum for D. Many interesting discussions occurring on a daily basis.
* [code.dlang.org](https://code.dlang.org) - Official library registry for D.
* [GitHub organization](https://github.com/dlang) [![GitHub stars](https://img.shields.io/github/stars/dlang?style=flat)](https://github.com/dlang/stargazers) - Official GitHub organization for D. Repository for all official D tools & code.
* [Issue tracker](https://github.com/dlang) [![GitHub stars](https://img.shields.io/github/stars/dlang?style=flat)](https://github.com/dlang/stargazers) – Official issue tracker for D. Older reports can be found in the [archived tracker](https://issues.dlang.org/).
* [Language specification](https://dlang.org/spec/spec.html) - The D programming language specification.

### Status page

*Unofficial, run by the community.*

* [status.dlang.rocks](https://status.dlang.rocks) - Public infrastructure monitoring of services associated with or used by the D Language Foundation and its project contributors.

## Getting Help

*For when you're stuck.*

* [Official D Forum Learn Group](https://forum.dlang.org/group/learn) - Highest-traffic site for getting D questions answered.
* [D on Stack Overflow](https://stackoverflow.com/questions/tagged/d) - Less traffic than the forums but possibly easier to search.
* [D on Rosetta Code](https://rosettacode.org/wiki/Category:D) - Examples of how to do many basic things in D.
* [D on Discord](https://discord.com/invite/bMZk9Q4) - Another very active community for D discussions and questions.

## People

*The people that made D the language it is.*

* [Walter Bright](https://www.walterbright.com/) - Father of D. Walter Bright is the creator and first implementer of the D programming language and has implemented compilers for several other languages.
* [Andrei Alexandrescu, PhD](http://erdani.org/) - C++ guru. Author of *The D Programming Language* and *Modern C++ Design*. With Walter Bright, Andrei co-designed many important features of D and authored a large part of D's standard library. Andrei works as a trainer in advanced C++ programming and algorithms and is now actively evangelizing D in the organization.
* [Átila Neves](https://atilaoncode.blog/) - [Deputy Leader of D](https://dlang.org/blog/2019/10/15/my-vision-of-ds-future/).
* **YOU** - Please add your information if you've done something interesting in D. It is you, the awesome people that make D awesome.

## Events

* [DConf](https://dconf.org/) - The premier event where D luminaries exchange knowledge, insight, and inspiration on everything related to the D language and its ecosystem.
* [Beerconf](https://wiki.dlang.org/Beerconf) - A casual, monthly virtual meetup for D community members.

## Organizations

*Organizations that contribute to D projects.*

* [D Programming Language](https://github.com/dlang) [![GitHub stars](https://img.shields.io/github/stars/dlang?style=flat)](https://github.com/dlang/stargazers) - Official Organization, hosts DMD, Phobos and other official tools and libs.
* [LDC Developers](https://github.com/ldc-developers) [![GitHub stars](https://img.shields.io/github/stars/ldc-developers?style=flat)](https://github.com/ldc-developers/stargazers) - LDC releated projects.
* [DerelictOrg](https://github.com/DerelictOrg) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg?style=flat)](https://github.com/DerelictOrg/stargazers) - A GitHub organization hosting all Derelict bindings including OpenGL and other multimedia/game related library bindings. (OpenGL 3, Bgfx, ENet, SDL 2, GLFW 3，OpenGLES, Free Image, Assimp3, libtheora, libogg, libvorbis, SFML 2, libpq, PhysicsFS, Open Dynamics Engine, Lua, DevIL, OpenAL, ALURE).
* [DlangScience](https://github.com/DlangScience) [![GitHub stars](https://img.shields.io/github/stars/DlangScience?style=flat)](https://github.com/DlangScience/stargazers) - A focal point and first port of call for scientific libraries and tooling for D.
* [Circular Studios](https://github.com/Circular-Studios) [![GitHub stars](https://img.shields.io/github/stars/Circular-Studios?style=flat)](https://github.com/Circular-Studios/stargazers) - We are a group of game developers at Rochester Institute of Technology building games and game tech. Hosts [Dash](https://github.com/Circular-Studios/Dash) [![GitHub stars](https://img.shields.io/github/stars/Circular-Studios/Dash?style=flat)](https://github.com/Circular-Studios/Dash/stargazers), a 3D game engine written in D, and other related libs.
* [EMSI](https://github.com/economicmodeling) [![GitHub stars](https://img.shields.io/github/stars/economicmodeling?style=flat)](https://github.com/economicmodeling/stargazers) - A Career building company that uses D as their main language. Hosts their opensource projects.
* [infognition](http://www.infognition.com/company.html) - Infognition is a self-funded and self-sustained company specializing in video processing and compression technologies for end-users and developers. They provide several opensource video related applications & tools written in D, hosted on [bitbucket](https://bitbucket.org/infognition/workspace/repositories/). They are also porting their main product--[Video Enchanser](http://www.infognition.com/VideoEnhancer/) from C/C++ to D.
* [libmir](https://github.com/libmir) [![GitHub stars](https://img.shields.io/github/stars/libmir?style=flat)](https://github.com/libmir/stargazers) - D's numeric library development team
* [sociomantic labs](https://github.com/sociomantic-tsunami) [![GitHub stars](https://img.shields.io/github/stars/sociomantic-tsunami?style=flat)](https://github.com/sociomantic-tsunami/stargazers) - Berlin based company specializing in real-time bidding for online advertising. Main sponsor of the [annual D language conference](https://dconf.org/). Has open-sourced large parts of their codebase as part of the [tsunami](https://github.com/sociomantic-tsunami) [![GitHub stars](https://img.shields.io/github/stars/sociomantic-tsunami?style=flat)](https://github.com/sociomantic-tsunami/stargazers) organization.
* [Symmetry Investments](https://symmetryinvestments.com/) - Symmetry Investments LP is an investment management company with approximately US$4.7 billion in assets under management as of 31 December 2018. Main sponsor of the [Symmetry Autumn of Code](https://dlang.org/blog/symmetry-autumn-of-code/). Have sponsored the development of [excel-d](https://dlang.org/blog/2017/05/31/project-highlight-excel-d/), [dpp](https://github.com/atilaneves/dpp) [![GitHub stars](https://img.shields.io/github/stars/atilaneves/dpp?style=flat)](https://github.com/atilaneves/dpp/stargazers), [autowrap](https://github.com/symmetryinvestments/autowrap) [![GitHub stars](https://img.shields.io/github/stars/symmetryinvestments/autowrap?style=flat)](https://github.com/symmetryinvestments/autowrap/stargazers), [mir-algorithm](https://github.com/libmir/mir-algorithm) [![GitHub stars](https://img.shields.io/github/stars/libmir/mir-algorithm?style=flat)](https://github.com/libmir/mir-algorithm/stargazers), and various other projects.
* [HuntLabs](https://github.com/huntlabs) [![GitHub stars](https://img.shields.io/github/stars/huntlabs?style=flat)](https://github.com/huntlabs/stargazers) - A technology group using DLang. Have pure D language implementation of quickly develop server-side applications and build distributed system services.

## Books

*D related books.* You can find another list of books on the [Books](https://wiki.dlang.org/Books) D wiki page.

* [TDPL](https://www.amazon.com/The-Programming-Language-Andrei-Alexandrescu/dp/0321635361/) - *The D Programming Language* by Andrei Alexandrescu.
* [Programming in D](https://ddili.org/ders/d.en/index.html) - A very detailed book about programming in D by Ali Çehreli covering many areas of the language. Has a free online version and is suitable for beginners.
* [D Cookbook](https://www.packtpub.com/en-us/product/d-cookbook-9781783287215) - A recipe-packed reference guide filled with practical tasks that are concisely explained to develop and broaden the user's abilities with the D programming language. by Adam D. Ruppe. Here is an interesting [review of the book](https://www.cppstories.com/2014/08/review-of-d-cookbook/).
* [Learning D](https://www.packtpub.com/en-us/product/learning-d-9781783552481) - This book is intended for those with some background in a C-family language who want to learn how to apply their knowledge and experience to D. (...) This book will help you get up to speed with the language and avoid common pitfalls that arise when translating C-family experience to D.
* [D Web Development](https://www.packtpub.com/en-us/product/d-web-development-9781785288890) - Whether you are new to the world of D, or already have developed applications in D, or if you want to leverage the power of D for web development, then this book is ideal for you.

## Tutorials

*D related tutorials.*

* [The Dlang Tour](https://tour.dlang.org/) - An interactive tutorial for D, inspired by Golang Tour.
* [Programming in Dlang](https://www.youtube.com/watch?v=HS7X9ERdjM4&list=PLvv0ScY6vfd9Fso-3cB4CGnSlW0E4btJV&ab_channel=MikeShah) - An introductory video series about programming in D.
* [Pragmatic D tutorial](https://qznc.github.io/d-tut/index.html) - This is a pragmatic introduction to the D Programming Language. by Andreas Zwinkau.
* [D Template Tutorial](https://github.com/PhilippeSigaud/D-templates-tutorial) [![GitHub stars](https://img.shields.io/github/stars/PhilippeSigaud/D-templates-tutorial?style=flat)](https://github.com/PhilippeSigaud/D-templates-tutorial/stargazers) - A tutorial dedicated to D Templates. Very good explanation about templates. Has pdf version. by Philippe Sigaud.
* [Component programming with ranges](https://wiki.dlang.org/Component_programming_with_ranges) - A detailed blog post about how to do component programming in a idiomatic D way with ranges, with a full working example.
* [Functional image processing in D](https://blog.cy.md/2014/03/21/functional-image-processing-in-d/) - A very interesting tutorial about writing an image processing lib in D. Shows the power of D's templates/CTFE/Ranges/UFCS for functional style programming.
* [OpenGL tutorials](https://github.com/drewet/opengl-tutorials) [![GitHub stars](https://img.shields.io/github/stars/drewet/opengl-tutorials?style=flat)](https://github.com/drewet/opengl-tutorials/stargazers) - OpenGL tutorials in D.
* [Creating a simple JSON serialiser in D](https://bradley.chatha.dev/BlogPost/JsonSerialiser/0) - D metaprogramming tutorial series
* [Let's learn D programming Game Dev!](https://www.youtube.com/watch?v=j-Zm1zgSxMQ&list=PLgM-lc_kSqFQPF0UXgmFZpZalqcrSofe-&ab_channel=KiRill) - A video series on learning game development with D from Ki Rill. [His channel](https://www.youtube.com/@rillki-dev/) also posts other videos related to D programming.
* [DLang YouTube Tutorials from Mike Shah](https://www.youtube.com/playlist?list=PLvv0ScY6vfd9Fso-3cB4CGnSlW0E4btJV) - Series of tutorials covering basic to advanced features of the D programming language and standard library.

## Blogs

*D related blogs.*

* [blog.dlang.org](https://dlang.org/blog/) - Official blog.
* [/r/d_language on Reddit](https://www.reddit.com/r/d_language/) - A feed of news and blog posts about D.
* [This week in D](https://dpldocs.info/this-week-in-d/Blog.html) - A weekly overview of activity in the D community and brief advice columns to help you get the most out of the D Programming Language.
* [Planet D](http://planet.dsource.org) - A repository of co-authored D-specific blogs maintained by Vladimir Panteleev.
* [D Idioms](https://p0nce.github.io/d-idioms/) - A great blog for many useful idioms with D programming.
* [GTK-D coding](https://web.archive.org/web/20241201013031/https://gtkdcoding.com/) - Simple examples of how to use GtkD to build GUI applications.
* [Tasty D](https://tastyminerals.github.io/tasty-blog/) - A blog about learning the D programming language and various D language trivia.

## Articles

*D related Articles.*

* [Origins of the D programming language](https://dl.acm.org/doi/pdf/10.1145/3386323) - By Walter Bright, Andrei Alexandrescu, Michael Parker. The history and development of D language.
* [Purity in D](https://klickverbot.at/blog/2012/05/purity-in-d/) - An article that explains the design principles behind D's purity feature.
* [Hidden treasures in the D standard library](https://web.archive.org/web/20171119072212/http://nomad.so/2014/08/hidden-treasure-in-the-d-standard-library/) - An article talking about several useful functions and templates in Phobos.
* [D is for Data Science](https://tech.nextroll.com/blog/data/2014/11/17/d-is-for-data-science.html) - A great post about how D is suitable for data science, particularly, replacing the role of python scripts for fast prototyping.
* [D Functional Garden](https://garden.dlang.io/)

## Package Management

*Libraries for package and dependency management.*

* [code.dlang.org](https://code.dlang.org/) - Official D library repository. Backed by dub.
* [dub](https://github.com/dlang/dub) [![GitHub stars](https://img.shields.io/github/stars/dlang/dub?style=flat)](https://github.com/dlang/dub/stargazers) - Official package and build management system for D.

## Compilers

*Official compilers for the D language.*

* [DMD](https://github.com/dlang/dmd) [![GitHub stars](https://img.shields.io/github/stars/dlang/dmd?style=flat)](https://github.com/dlang/dmd/stargazers) - The reference compiler for the D programming language. Stable, builds insanely fast, very good for learning and rapid prototyping/development. Currently the frontend is implemented in D, and shared between dmd, ldc and gdc, the backend is implemented in C++.
* [LDC](https://github.com/ldc-developers/ldc) [![GitHub stars](https://img.shields.io/github/stars/ldc-developers/ldc?style=flat)](https://github.com/ldc-developers/ldc/stargazers) - The LLVM-based D compiler. Uses the DMD frontend and LLVM backend. Builds slower than dmd, but generates more optimized code than DMD. It supports all the target platforms of LLVM.
* [GDC](https://github.com/D-Programming-GDC/GDC) [![GitHub stars](https://img.shields.io/github/stars/D-Programming-GDC/GDC?style=flat)](https://github.com/D-Programming-GDC/GDC/stargazers) - GNU D Compiler. Use DMD frontend and GCC backend. Currently targets the most platforms due to the use of GCC. Generated code runs faster than DMD in most cases, on par with LDC. In the process of integration with the official GCC toolchain.

## Alternative / WIP Compilers

*These compilers may differ from or be incompatible with the official set of tools.*

* [SDC](https://github.com/snazzy-d/SDC) [![GitHub stars](https://img.shields.io/github/stars/snazzy-d/SDC?style=flat)](https://github.com/snazzy-d/SDC/stargazers) - The Snazzy D Compiler. Written in D. Grows Smarter every day.
* [OpenD](https://opendlang.org/index.html) - A fork of the D language focused on practical and incremental improvements.

## Dev Tools

*Tools for more productive D development.*

* [D-Scanner](https://github.com/dlang-community/D-Scanner) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/D-Scanner?style=flat)](https://github.com/dlang-community/D-Scanner/stargazers) - Swiss-army knife for D source code (linting, static analysis, D code parsing, etc.)
* [dfmt](https://github.com/dlang-community/dfmt) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/dfmt?style=flat)](https://github.com/dlang-community/dfmt/stargazers) - formatter for D source code

## Build Tools

*Manage projects and compile software from source code.*

* [dub](https://github.com/dlang/dub) [![GitHub stars](https://img.shields.io/github/stars/dlang/dub?style=flat)](https://github.com/dlang/dub/stargazers) - De facto official package and build management system for D. Will be included officially soon.
* [scons-d](https://scons.org/) - Scons has built-in support for building D projects, thanks to Russel Winder.
* [premake](https://github.com/premake/premake-dlang) [![GitHub stars](https://img.shields.io/github/stars/premake/premake-dlang?style=flat)](https://github.com/premake/premake-dlang/stargazers) - Premake has built-in support for D projects
* [reggae](https://github.com/atilaneves/reggae) [![GitHub stars](https://img.shields.io/github/stars/atilaneves/reggae?style=flat)](https://github.com/atilaneves/reggae/stargazers) - meta build system in D
* [Makefile](https://github.com/bioinfornatics/MakefileForD) [![GitHub stars](https://img.shields.io/github/stars/bioinfornatics/MakefileForD?style=flat)](https://github.com/bioinfornatics/MakefileForD/stargazers) - Makefile template for D projects
* [cmake-d](https://github.com/dcarp/cmake-d) [![GitHub stars](https://img.shields.io/github/stars/dcarp/cmake-d?style=flat)](https://github.com/dcarp/cmake-d/stargazers) - CMake D Projects
* [cook2](https://github.com/gecko0307/Cook2) [![GitHub stars](https://img.shields.io/github/stars/gecko0307/Cook2?style=flat)](https://github.com/gecko0307/Cook2/stargazers) - Fast incremental build tool intended for projects in D
* [button](https://jasonwhite.io/button/) - A universal build system to build your software at the push of a button.
* [wild](https://github.com/Vild/Wild) [![GitHub stars](https://img.shields.io/github/stars/Vild/Wild?style=flat)](https://github.com/Vild/Wild/stargazers) - Wild build system, used to build the [PowerNex](https://github.com/PowerNex/PowerNex) [![GitHub stars](https://img.shields.io/github/stars/PowerNex/PowerNex?style=flat)](https://github.com/PowerNex/PowerNex/stargazers) kernel
* [XMake](https://xmake.io) - XMake is a crossplatform build system, that incorporated the D language and also has support for DUB repositories.
* [wox](https://github.com/redthing1/wox) [![GitHub stars](https://img.shields.io/github/stars/redthing1/wox?style=flat)](https://github.com/redthing1/wox/stargazers) - A highly flexible recipe build system inspired by Make

## IDEs & Editors

*Integrated Development Environment.*

* [Visual D](https://github.com/dlang/visuald) [![GitHub stars](https://img.shields.io/github/stars/dlang/visuald?style=flat)](https://github.com/dlang/visuald/stargazers) - Visual Studio extension for the D programming language.
* [IntelliJ D Language](https://intellij-dlanguage.github.io/) - Support for the D programming language within IntelliJ IDEA.
* [Dexed](https://gitlab.com/basile.b/dexed) - IDE for the D programming language, its compilers, tools and libraries.
* [Dutyl](https://github.com/idanarye/vim-dutyl) [![GitHub stars](https://img.shields.io/github/stars/idanarye/vim-dutyl?style=flat)](https://github.com/idanarye/vim-dutyl/stargazers) - Vim plugin that integrates various D development tools
* [code-d](https://marketplace.visualstudio.com/items?itemName=webfreak.code-d) <sup>\[[open-vsx](https://open-vsx.org/extension/webfreak/code-d)\]</sup> - Visual Studio Code extension using serve-d
* [ide-d](https://packages.pulsar-edit.dev/packages/ide-d) - Pulsar (fork of Atom) extension for D using serve-d
* [DCD](https://github.com/dlang-community/DCD) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/DCD?style=flat)](https://github.com/dlang-community/DCD/stargazers) - Independent auto-complete program for the D programming language. Could be used with editors like vim, emacs, sublime text, textadept, and zeus. See [editors support](https://github.com/dlang-community/DCD/wiki/IDEs-and-Editors-with-DCD-support) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/DCD/wiki/IDEs-and-Editors-with-DCD-support?style=flat)](https://github.com/dlang-community/DCD/wiki/IDEs-and-Editors-with-DCD-support/stargazers).
* [serve-d](https://github.com/Pure-D/serve-d) [![GitHub stars](https://img.shields.io/github/stars/Pure-D/serve-d?style=flat)](https://github.com/Pure-D/serve-d/stargazers) - Language Server Protocol (LSP) implementation for D. Adds modern IDE features to any editor with LSP support (VSCode, Atom, Vim/Neovim and others)

## Lexers, Parsers & Generators

* [libdparse](https://github.com/dlang-community/libdparse) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/libdparse?style=flat)](https://github.com/dlang-community/libdparse/stargazers) - A D language lexer and parser, (possibly) future standard D parser/lexer.
* [Martin Nowak's Lexer](https://github.com/MartinNowak/lexer) [![GitHub stars](https://img.shields.io/github/stars/MartinNowak/lexer?style=flat)](https://github.com/MartinNowak/lexer/stargazers) - A lexer generator.
* [Mono-D's DParser](https://github.com/aBothe/D_Parser) [![GitHub stars](https://img.shields.io/github/stars/aBothe/D_Parser?style=flat)](https://github.com/aBothe/D_Parser/stargazers) - A D parser written in C# and used in Mono-D.
* [Pegged](https://github.com/dlang-community/Pegged) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/Pegged?style=flat)](https://github.com/dlang-community/Pegged/stargazers) - A Parsing Expression Grammar (PEG) module written in D.
* [Goldie](https://bitbucket.org/Abscissa/goldie/wiki/Home) - Goldie Parsing System.
* [ctpg](https://github.com/youxkei/ctpg) [![GitHub stars](https://img.shields.io/github/stars/youxkei/ctpg?style=flat)](https://github.com/youxkei/ctpg/stargazers) - Compile-Time Parser (with converter) Generator written in D.
* [dunnart](https://github.com/pwil3058/dunnart) [![GitHub stars](https://img.shields.io/github/stars/pwil3058/dunnart?style=flat)](https://github.com/pwil3058/dunnart/stargazers) - LALR(1) Parser Generator written in D.

## Preprocesors

* [warp](https://github.com/facebookarchive/warp) [![GitHub stars](https://img.shields.io/github/stars/facebookarchive/warp?style=flat)](https://github.com/facebookarchive/warp/stargazers) - A fast preprocessor for C and C++ used in Facebook infrastructure. Written by Walter Bright.

## Version Managers

* [dvm](https://github.com/jacob-carlborg/dvm) [![GitHub stars](https://img.shields.io/github/stars/jacob-carlborg/dvm?style=flat)](https://github.com/jacob-carlborg/dvm/stargazers) - A small tool to install and manage DMD (self-hosting) compiler.
* [ldcup](https://github.com/kassane/ldcup) [![GitHub stars](https://img.shields.io/github/stars/kassane/ldcup?style=flat)](https://github.com/kassane/ldcup/stargazers) - A small tool to install and manage LDC2 (LLVM backend) compiler.


## GitHub Actions

* [setup-dlang](https://github.com/dlang-community/setup-dlang) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/setup-dlang?style=flat)](https://github.com/dlang-community/setup-dlang/stargazers) - Install D compilers & DUB inside GitHub Actions
* [dub-upgrade](https://github.com/WebFreak001/dub-upgrade) [![GitHub stars](https://img.shields.io/github/stars/WebFreak001/dub-upgrade?style=flat)](https://github.com/WebFreak001/dub-upgrade/stargazers) - Run `dub upgrade` trying to repeat on network failure and using package cache on GitHub Actions

## Testing Frameworks

* [unit-threaded](https://github.com/atilaneves/unit-threaded) [![GitHub stars](https://img.shields.io/github/stars/atilaneves/unit-threaded?style=flat)](https://github.com/atilaneves/unit-threaded/stargazers) - Multi-threaded unit test framework
* [silly](https://gitlab.com/AntonMeep/silly) - Better test runner for the D programming language. No nonsense.
* [fluent-asserts](https://github.com/gedaiu/fluent-asserts) [![GitHub stars](https://img.shields.io/github/stars/gedaiu/fluent-asserts?style=flat)](https://github.com/gedaiu/fluent-asserts/stargazers) - Fluent assertion framework with expressive syntax and detailed error messages.

## Programming Languages

*Programming languages written in D.*

* [higgs](https://github.com/higgsjs/Higgs) [![GitHub stars](https://img.shields.io/github/stars/higgsjs/Higgs?style=flat)](https://github.com/higgsjs/Higgs/stargazers) - Higgs JavaScript Virtual Machine, implemented in D.
* [brainfuck-d](https://codeberg.org/GuineaPigUuhh/brainfuck-d) - Brainfuck interpreter, compiler and REPL written in D.
* [arsd.script](https://github.com/adamdruppe/arsd/blob/master/script.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/script.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/script.d/stargazers) - A small script interpreter that builds on *arsd.jsvar* to be easily embedded inside and to have easy two-way interop with the host D program.

## Operating Systems

*Operating systems written in D.*

* [PowerNex](https://github.com/PowerNex/PowerNex) [![GitHub stars](https://img.shields.io/github/stars/PowerNex/PowerNex?style=flat)](https://github.com/PowerNex/PowerNex/stargazers) - A kernel written in D
* [SerpentOS](https://gitlab.com/serpent-os) - Snek factory
* [Trinix](https://github.com/Rikarin/Trinix) [![GitHub stars](https://img.shields.io/github/stars/Rikarin/Trinix?style=flat)](https://github.com/Rikarin/Trinix/stargazers) - Hybrid operating system for x64 PC written in D
* [XOmB](https://github.com/xomboverlord/xomb) [![GitHub stars](https://img.shields.io/github/stars/xomboverlord/xomb?style=flat)](https://github.com/xomboverlord/xomb/stargazers) - An exokernel operating system written in D

## Bare Metal / Kernel Development

* [D Bare bones](https://wiki.osdev.org/D_Bare_Bones) - kernel hello world in D (using GDC compiler)
* [D barebone with ldc2](https://wiki.osdev.org/D_barebone_with_ldc2) - another kernel hello world in D (using LDC compiler)
* [XOmB bare bones](https://web.archive.org/web/20161214232759/http://wiki.xomb.org/index.php?title=XOmB_Bare_Bones) - an exokernel operating system written in D. [Main page](https://web.archive.org/web/20161201061242/http://wiki.xomb.org/index.php?title=Main_Page), [github](https://github.com/xomboverlord/xomb/tree/unborn) [![GitHub stars](https://img.shields.io/github/stars/xomboverlord/xomb/tree/unborn?style=flat)](https://github.com/xomboverlord/xomb/tree/unborn/stargazers).
* [Bare Metal ARM Cortex-M GDC Cross Compiler](https://wiki.dlang.org/Bare_Metal_ARM_Cortex-M_GDC_Cross_Compiler) - building a bare metal ARM Cortex-M (arm-none-eabi) GDC cross compiler for a Linux host.

## General Containers

*Data structures and container libraries.*

* [EMSI containers](https://github.com/dlang-community/containers) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/containers?style=flat)](https://github.com/dlang-community/containers/stargazers) - Containers that do not use the GC
* [memutils](https://github.com/etcimon/memutils) [![GitHub stars](https://img.shields.io/github/stars/etcimon/memutils?style=flat)](https://github.com/etcimon/memutils/stargazers) - Overhead allocators, allocator-aware containers and lifetime management for D objects
* [dlib.container](https://github.com/gecko0307/dlib) [![GitHub stars](https://img.shields.io/github/stars/gecko0307/dlib?style=flat)](https://github.com/gecko0307/dlib/stargazers) - generic data structures (GC-free dynamic and associative arrays and more)
* [std.rcstring](https://github.com/burner/std.rcstring) [![GitHub stars](https://img.shields.io/github/stars/burner/std.rcstring?style=flat)](https://github.com/burner/std.rcstring/stargazers) - A reference counted string implementation for D's build in string construct

## Core Utilities

*General-purpose utility libraries.*

* [NuMem](https://github.com/Inochi2D/numem) [![GitHub stars](https://img.shields.io/github/stars/Inochi2D/numem?style=flat)](https://github.com/Inochi2D/numem/stargazers) - No-GC memory management utilities for DLang.
* [NuLib](https://github.com/Inochi2D/nulib) [![GitHub stars](https://img.shields.io/github/stars/Inochi2D/nulib?style=flat)](https://github.com/Inochi2D/nulib/stargazers) - D "standard" library built ontop of numem.
* [Joka](https://github.com/Kapendev/joka) [![GitHub stars](https://img.shields.io/github/stars/Kapendev/joka?style=flat)](https://github.com/Kapendev/joka/stargazers) - A nogc utility library.

## Web Frameworks

*Networking libraries.*

* [dlang-requests](https://github.com/ikod/dlang-requests) [![GitHub stars](https://img.shields.io/github/stars/ikod/dlang-requests?style=flat)](https://github.com/ikod/dlang-requests/stargazers) - HTTP client library inspired by python-requests
* [Handy-Httpd](https://github.com/andrewlalis/handy-httpd) [![GitHub stars](https://img.shields.io/github/stars/andrewlalis/handy-httpd?style=flat)](https://github.com/andrewlalis/handy-httpd/stargazers) - A simple, lightweight, and well-documented HTTP server that lets you bootstrap ideas and have something up and running in minutes.
* [serverino](https://github.com/trikko/serverino) [![GitHub stars](https://img.shields.io/github/stars/trikko/serverino?style=flat)](https://github.com/trikko/serverino/stargazers) - Small and ready-to-go http server, in D
* [libasync](https://github.com/etcimon/libasync) [![GitHub stars](https://img.shields.io/github/stars/etcimon/libasync?style=flat)](https://github.com/etcimon/libasync/stargazers) - Cross-platform event loop library of asynchronous objects
* [libhttp2](https://github.com/etcimon/libhttp2) [![GitHub stars](https://img.shields.io/github/stars/etcimon/libhttp2?style=flat)](https://github.com/etcimon/libhttp2/stargazers) - HTTP/2 library in D, translated from nghttp2

*Full stack web frameworks.*

* [vibe.d](https://vibed.org/) - Asynchronous I/O Web Framework that doesn’t get in your way, written in D.
* [arsd](https://github.com/adamdruppe/arsd) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd?style=flat)](https://github.com/adamdruppe/arsd/stargazers) - Adam D. Ruppe's web framework. (See `arsd/cgi.d` for the CGI/FastCGI/SCGI/webserver component.)
* [cmsed](https://github.com/rikkimax/Cmsed) [![GitHub stars](https://img.shields.io/github/stars/rikkimax/Cmsed?style=flat)](https://github.com/rikkimax/Cmsed/stargazers) - A component library for Vibe that functions as a CMS.

*RPC libraries.*

* [Apache Thrift](https://code.dlang.org/packages/apache-thrift) - A lightweight, language-independent, featureful RPC framework. Thrift provides clean abstractions for data transport, data serialization, code generation, and application level processing. [Apache Thrift Page](https://thrift.apache.org/)
* [Hprose](https://github.com/hprose/hprose-d) [![GitHub stars](https://img.shields.io/github/stars/hprose/hprose-d?style=flat)](https://github.com/hprose/hprose-d/stargazers) - A very newbility RPC Library for D, and it support 25+ languages now.

*Static Site Generator.*

* [DSSG](https://github.com/kambrium/dssg) [![GitHub stars](https://img.shields.io/github/stars/kambrium/dssg?style=flat)](https://github.com/kambrium/dssg/stargazers) - A static site generator with a different approach.

## Data Serialization

*JSON, XML, protobuf and other data serialization libraries.*

* [cerealed](https://github.com/atilaneves/cerealed) [![GitHub stars](https://img.shields.io/github/stars/atilaneves/cerealed?style=flat)](https://github.com/atilaneves/cerealed/stargazers) - Serialisation library for D
* [dproto](https://github.com/msoucy/dproto) [![GitHub stars](https://img.shields.io/github/stars/msoucy/dproto?style=flat)](https://github.com/msoucy/dproto/stargazers) - Google Protocol Buffer support in D.

*JSON libraries.*

* [vibe.data.json](https://vibed.org/api/vibe.data.json/) - JSON functions in Vibe.d. Currently the best implementation I used.
* [fast.json](https://github.com/etcimon/fast) [![GitHub stars](https://img.shields.io/github/stars/etcimon/fast?style=flat)](https://github.com/etcimon/fast/stargazers) - A library for D that aims to provide the fastest possible implementation of some every day routines.
* [std.json](https://dlang.org/phobos/std_json.html) - D's standard library JSON module. Needs refinement.
* [painlessjson](https://github.com/BlackEdder/painlessjson) [![GitHub stars](https://img.shields.io/github/stars/BlackEdder/painlessjson?style=flat)](https://github.com/BlackEdder/painlessjson/stargazers) - Convert between D types and std.json.
* [std.data.json](https://github.com/dlang-community/std_data_json) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/std_data_json?style=flat)](https://github.com/dlang-community/std_data_json/stargazers) - Phobos candidate for JSON serialization (based on Vibed)
* [asdf](https://github.com/libmir/asdf) [![GitHub stars](https://img.shields.io/github/stars/libmir/asdf?style=flat)](https://github.com/libmir/asdf/stargazers) - Cache oriented string based JSON representation for fast read & writes and serialisation.

*XML libraries.*

* [orange](https://github.com/jacob-carlborg/orange) [![GitHub stars](https://img.shields.io/github/stars/jacob-carlborg/orange?style=flat)](https://github.com/jacob-carlborg/orange/stargazers) - General purpose serializer (currently only supports XML)
* [std.experimental.xml](https://github.com/lodo1995/experimental.xml) [![GitHub stars](https://img.shields.io/github/stars/lodo1995/experimental.xml?style=flat)](https://github.com/lodo1995/experimental.xml/stargazers) - Phobos candidate for a XML serialization
* arsd [dom.d](https://github.com/adamdruppe/arsd/blob/master/dom.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/dom.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/dom.d/stargazers) - an xml/html DOM based on what Javascript provides in browsers
* [newxml](https://github.com/ZILtoid1991/newxml) [![GitHub stars](https://img.shields.io/github/stars/ZILtoid1991/newxml?style=flat)](https://github.com/ZILtoid1991/newxml/stargazers) - Successor of std.experimental.xml. DOM compatible, and also has a SAX parser.

## Database Clients

*Clients and bindings to C clients for relational and nosql databases.*

* [vibe.d](https://github.com/vibe-d/vibe.d) [![GitHub stars](https://img.shields.io/github/stars/vibe-d/vibe.d?style=flat)](https://github.com/vibe-d/vibe.d/stargazers) - Vibe.d has internal support for Redis and MongoDB, which are very stable. Soon, the database drivers will be separated into independent projects.
* [arsd](https://github.com/adamdruppe/arsd) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd?style=flat)](https://github.com/adamdruppe/arsd/stargazers) - Adam D. Ruppe's library; in addition to a Web backend, it also has support for database access with database.d, sqlite.d, mysql.d and postgres.d.
* [hibernated](https://github.com/buggins/hibernated) [![GitHub stars](https://img.shields.io/github/stars/buggins/hibernated?style=flat)](https://github.com/buggins/hibernated/stargazers) - HibernateD is an ORM for D (similar to [Hibernate](https://hibernate.org/)).
* [mysql-native](https://github.com/mysql-d/mysql-native) [![GitHub stars](https://img.shields.io/github/stars/mysql-d/mysql-native?style=flat)](https://github.com/mysql-d/mysql-native/stargazers) - A MySQL client implemented in native D.
* [ddb](https://github.com/pszturmaj/ddb) [![GitHub stars](https://img.shields.io/github/stars/pszturmaj/ddb?style=flat)](https://github.com/pszturmaj/ddb/stargazers) - Database access for D2. Currently only supports PostgreSQL.
* [ddbc](https://github.com/buggins/ddbc) [![GitHub stars](https://img.shields.io/github/stars/buggins/ddbc?style=flat)](https://github.com/buggins/ddbc/stargazers) - DDBC is a DB Connector for D language (similar to JDBC). HibernateD (see below) uses ddbc for database abstraction.
* [dvorm](https://github.com/rikkimax/Dvorm) [![GitHub stars](https://img.shields.io/github/stars/rikkimax/Dvorm?style=flat)](https://github.com/rikkimax/Dvorm/stargazers) - An ORM for D with Vibe support. Works with vibe.d and mysql-d, giving it the ability to access MongoDB and MySQL.
* [Tiny Redis](http://adilbaig.github.io/Tiny-Redis/) - Redis driver for D. Fast, Simple, Stable. Has no dependencies.
* [libpb](https://github.com/Hax-io/libpb) [![GitHub stars](https://img.shields.io/github/stars/Hax-io/libpb?style=flat)](https://github.com/Hax-io/libpb/stargazers) - Interact with a PocketBase database

## CLI Libraries

* [terminal.d](https://github.com/adamdruppe/arsd/blob/master/terminal.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/terminal.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/terminal.d/stargazers) - Part of Adam Ruppe's [arsd](https://github.com/adamdruppe/arsd) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd?style=flat)](https://github.com/adamdruppe/arsd/stargazers) library supporting cursor and color manipulation on the console.
* [commandr](https://github.com/robik/commandr) [![GitHub stars](https://img.shields.io/github/stars/robik/commandr?style=flat)](https://github.com/robik/commandr/stargazers) - A modern, powerful command line argument parser.
* [argsd](https://github.com/burner/argsd) [![GitHub stars](https://img.shields.io/github/stars/burner/argsd?style=flat)](https://github.com/burner/argsd/stargazers) - A command line and config file parser for DLang
* [luneta](https://github.com/fbeline/luneta) [![GitHub stars](https://img.shields.io/github/stars/fbeline/luneta?style=flat)](https://github.com/fbeline/luneta/stargazers) - A command-line fuzzy finder.
* [argparse](https://code.dlang.org/packages/argparse) - Flexible parser of command line arguments.
* [gogga](https://github.com/deavmi/gogga) [![GitHub stars](https://img.shields.io/github/stars/deavmi/gogga?style=flat)](https://github.com/deavmi/gogga/stargazers) - simple easy-to-use colorful logger for command-line applications
* [scriptlike](https://github.com/Abscissa/scriptlike) [![GitHub stars](https://img.shields.io/github/stars/Abscissa/scriptlike?style=flat)](https://github.com/Abscissa/scriptlike/stargazers) - Utility library to aid writing script-like programs in D.
* [d-colorize](https://code.dlang.org/packages/colorize) - A port of the ruby library [colorize](https://github.com/fazibear/colorize) [![GitHub stars](https://img.shields.io/github/stars/fazibear/colorize?style=flat)](https://github.com/fazibear/colorize/stargazers). It add some methods to set color, background color and text effect on console easier using ANSI escape sequences.
* [dexpect](https://github.com/grogancolin/dexpect/) [![GitHub stars](https://img.shields.io/github/stars/grogancolin/dexpect/?style=flat)](https://github.com/grogancolin/dexpect//stargazers) - A D implementation of the expect framework. Handy for bash emulation.
* [Argon](https://github.com/markuslaker/Argon) [![GitHub stars](https://img.shields.io/github/stars/markuslaker/Argon?style=flat)](https://github.com/markuslaker/Argon/stargazers) - A processor for command-line arguments, an alternative to Getopt, written in D.

## CLI Applications

* [Literate](https://github.com/zyedidia/Literate) [![GitHub stars](https://img.shields.io/github/stars/zyedidia/Literate?style=flat)](https://github.com/zyedidia/Literate/stargazers) - A literate programming tool for any language.
* [onedrive](https://github.com/abraunegg/onedrive) [![GitHub stars](https://img.shields.io/github/stars/abraunegg/onedrive?style=flat)](https://github.com/abraunegg/onedrive/stargazers) - #1 Free OneDrive Client for Linux.
* [tshare](https://github.com/trikko/tshare) [![GitHub stars](https://img.shields.io/github/stars/trikko/tshare?style=flat)](https://github.com/trikko/tshare/stargazers) - Fast file sharing from cli, using transfer.sh.
* [todod](https://github.com/BlackEdder/todod) [![GitHub stars](https://img.shields.io/github/stars/BlackEdder/todod?style=flat)](https://github.com/BlackEdder/todod/stargazers) - Todod is a command line based todo list manager. It also has support for shell interaction based on [linenoise](https://github.com/antirez/linenoise) [![GitHub stars](https://img.shields.io/github/stars/antirez/linenoise?style=flat)](https://github.com/antirez/linenoise/stargazers).
* [Soulfind](https://github.com/soulfind-dev/soulfind) [![GitHub stars](https://img.shields.io/github/stars/soulfind-dev/soulfind?style=flat)](https://github.com/soulfind-dev/soulfind/stargazers) - Soulseek server implementation in D.

## GUI Libraries

*Libraries for working with graphical user interface applications.*

* [giD](https://github.com/Kymorphia/gid) [![GitHub stars](https://img.shields.io/github/stars/Kymorphia/gid?style=flat)](https://github.com/Kymorphia/gid/stargazers) - GObject Introspection D Package Repository.
* [Fluid](https://git.samerion.com/Samerion/Fluid) - A declarative cross-platform user interface library for D.
* [minigui](https://arsd-official.dpldocs.info/arsd.minigui.html) - A smallish GUI widget library, aiming to be on par with at least HTML4 forms and a few other expected gui components. It's part of the [arsd libraries](https://github.com/adamdruppe/arsd/blob/master/minigui.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/minigui.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/minigui.d/stargazers).
* [DLangUI](https://github.com/buggins/dlangui) [![GitHub stars](https://img.shields.io/github/stars/buggins/dlangui?style=flat)](https://github.com/buggins/dlangui/stargazers) - Cross Platform GUI for D programming language. My personal favorite, because it is written in D(not a binding), and is cross platform. DLangUI also has a good showcase in the IDE [DLangIDE](https://github.com/buggins/dlangide) [![GitHub stars](https://img.shields.io/github/stars/buggins/dlangide?style=flat)](https://github.com/buggins/dlangide/stargazers).
* [microui-d](https://github.com/Kapendev/microui-d) [![GitHub stars](https://img.shields.io/github/stars/Kapendev/microui-d?style=flat)](https://github.com/Kapendev/microui-d/stargazers) - A tiny immediate-mode UI library.
* [GtkD](https://github.com/gtkd-developers/GtkD) [![GitHub stars](https://img.shields.io/github/stars/gtkd-developers/GtkD?style=flat)](https://github.com/gtkd-developers/GtkD/stargazers) - GtkD is a D binding and OO wrapper of GTK+. GtkD is actively maintained and is currently the most stable GUI lib for D.
* [tkD](https://github.com/nomad-software/tkd) [![GitHub stars](https://img.shields.io/github/stars/nomad-software/tkd?style=flat)](https://github.com/nomad-software/tkd/stargazers) - GUI toolkit for the D programming language based on Tcl/Tk.
* [dqml](https://github.com/filcuc/dqml) [![GitHub stars](https://img.shields.io/github/stars/filcuc/dqml?style=flat)](https://github.com/filcuc/dqml/stargazers) - Qt Qml bindings for the D programming language.
* [Sciter-Dport](https://github.com/sciter-sdk/Sciter-Dport) [![GitHub stars](https://img.shields.io/github/stars/sciter-sdk/Sciter-Dport?style=flat)](https://github.com/sciter-sdk/Sciter-Dport/stargazers) - D bindings for the [Sciter](https://sciter.com) - crossplatform HTML/CSS/script desktop UI toolkit.

*Note*: You can also find a list of GUI libs on [wiki.dlang.org](https://wiki.dlang.org/Libraries_and_Frameworks#GUI_Libraries), but not all of the libraries are actively maintained now.

## GUI Applications

* [tilix](https://github.com/gnunn1/tilix) [![GitHub stars](https://img.shields.io/github/stars/gnunn1/tilix?style=flat)](https://github.com/gnunn1/tilix/stargazers) - A tiling terminal emulator for Linux using GTK+ 3.
* [Inochi Creator](https://github.com/Inochi2D/inochi-creator) [![GitHub stars](https://img.shields.io/github/stars/Inochi2D/inochi-creator?style=flat)](https://github.com/Inochi2D/inochi-creator/stargazers) - Inochi2D Rigging Application.
* [Inochi Session](https://github.com/Inochi2D/inochi-session) [![GitHub stars](https://img.shields.io/github/stars/Inochi2D/inochi-session?style=flat)](https://github.com/Inochi2D/inochi-session/stargazers) - Application that allows streaming with Inochi2D puppets.

## Game Bindings

*Bindings to game development related libraries in C, C++, and other languages.*

* [raylib-d](https://github.com/schveiguy/raylib-d) [![GitHub stars](https://img.shields.io/github/stars/schveiguy/raylib-d?style=flat)](https://github.com/schveiguy/raylib-d/stargazers) - D bindings for raylib.
* [sokol-d](https://github.com/floooh/sokol-d) [![GitHub stars](https://img.shields.io/github/stars/floooh/sokol-d?style=flat)](https://github.com/floooh/sokol-d/stargazers) - D bindings for the sokol headers.
* [DAllegro5](https://github.com/SiegeLord/DAllegro5) [![GitHub stars](https://img.shields.io/github/stars/SiegeLord/DAllegro5?style=flat)](https://github.com/SiegeLord/DAllegro5/stargazers) - D binding/wrapper to Allegro 5, a modern game programming library.
* [DSFML](https://github.com/Jebbs/DSFML) [![GitHub stars](https://img.shields.io/github/stars/Jebbs/DSFML?style=flat)](https://github.com/Jebbs/DSFML/stargazers) - A static binding of SFML in a way that makes sense for D.
* [Godot-D](https://github.com/godot-d/godot-d) [![GitHub stars](https://img.shields.io/github/stars/godot-d/godot-d?style=flat)](https://github.com/godot-d/godot-d/stargazers) - D language bindings for the Godot Engine's GDNative API.
* [BindBC](https://github.com/BindBC) [![GitHub stars](https://img.shields.io/github/stars/BindBC?style=flat)](https://github.com/BindBC/stargazers) - Bindings compatible with `-betterC` and `@nogc`, using [bindbc-loader](https://github.com/BindBC/bindbc-loader) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-loader?style=flat)](https://github.com/BindBC/bindbc-loader/stargazers).
	* [OpenGL](https://github.com/BindBC/bindbc-opengl) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-opengl?style=flat)](https://github.com/BindBC/bindbc-opengl/stargazers) - Graphics API
	* [GLFW 3](https://github.com/BindBC/bindbc-glfw) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-glfw?style=flat)](https://github.com/BindBC/bindbc-glfw/stargazers) - Window/Input library
	* [SDL 2](https://github.com/BindBC/bindbc-sdl) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-sdl?style=flat)](https://github.com/BindBC/bindbc-sdl/stargazers) - Multimedia library
	* [SDL2_gfx](https://github.com/aferust/bindbc-sdlgfx) [![GitHub stars](https://img.shields.io/github/stars/aferust/bindbc-sdlgfx?style=flat)](https://github.com/aferust/bindbc-sdlgfx/stargazers) - Drawing primitives for SDL2
	* [SFML 2](https://github.com/BindBC/bindbc-sfml) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-sfml?style=flat)](https://github.com/BindBC/bindbc-sfml/stargazers) - Multimedia library
	* [Imgui](https://github.com/Inochi2D/i2d-imgui) [![GitHub stars](https://img.shields.io/github/stars/Inochi2D/i2d-imgui?style=flat)](https://github.com/Inochi2D/i2d-imgui/stargazers) - Immediate mode GUI
	* [Nuklear](https://github.com/Timu5/bindbc-nuklear) [![GitHub stars](https://img.shields.io/github/stars/Timu5/bindbc-nuklear?style=flat)](https://github.com/Timu5/bindbc-nuklear/stargazers) - Immediate mode GUI
	* [raylib3](https://github.com/o3o/bindbc-raylib3) [![GitHub stars](https://img.shields.io/github/stars/o3o/bindbc-raylib3?style=flat)](https://github.com/o3o/bindbc-raylib3/stargazers) - Game library
	* [bgfx](https://github.com/GoaLitiuM/bindbc-bgfx) [![GitHub stars](https://img.shields.io/github/stars/GoaLitiuM/bindbc-bgfx?style=flat)](https://github.com/GoaLitiuM/bindbc-bgfx/stargazers) - Cross-Platform renderer
	* [WebGPU](https://github.com/DLangGamedev/bindbc-wgpu) [![GitHub stars](https://img.shields.io/github/stars/DLangGamedev/bindbc-wgpu?style=flat)](https://github.com/DLangGamedev/bindbc-wgpu/stargazers) - Modern GPU API
	* [Zstandard](https://github.com/ZILtoid1991/bindbc-zstandard) [![GitHub stars](https://img.shields.io/github/stars/ZILtoid1991/bindbc-zstandard?style=flat)](https://github.com/ZILtoid1991/bindbc-zstandard/stargazers) - Fast compression
	* [nanomsg-next-gen](https://github.com/darkridder/bindbc-nng) [![GitHub stars](https://img.shields.io/github/stars/darkridder/bindbc-nng?style=flat)](https://github.com/darkridder/bindbc-nng/stargazers) - Messaging library
	* [OpenAL](https://github.com/BindBC/bindbc-openal) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-openal?style=flat)](https://github.com/BindBC/bindbc-openal/stargazers) - Audio library
	* [SoLoud](https://github.com/DLangGamedev/bindbc-soloud) [![GitHub stars](https://img.shields.io/github/stars/DLangGamedev/bindbc-soloud?style=flat)](https://github.com/DLangGamedev/bindbc-soloud/stargazers) - Audio library
	* [KiWi](https://github.com/aferust/bindbc-kiwi) [![GitHub stars](https://img.shields.io/github/stars/aferust/bindbc-kiwi?style=flat)](https://github.com/aferust/bindbc-kiwi/stargazers) - UI widget toolkit
	* [NanoVG](https://github.com/aferust/bindbc-nanovg) [![GitHub stars](https://img.shields.io/github/stars/aferust/bindbc-nanovg?style=flat)](https://github.com/aferust/bindbc-nanovg/stargazers) - Vector graphics
	* [Blend2D](https://github.com/kdmult/bindbc-blend2d) [![GitHub stars](https://img.shields.io/github/stars/kdmult/bindbc-blend2d?style=flat)](https://github.com/kdmult/bindbc-blend2d/stargazers) - Vector graphics
	* [Lua](https://github.com/BindBC/bindbc-lua) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-lua?style=flat)](https://github.com/BindBC/bindbc-lua/stargazers) - Scripting language
	* [JoyShockLibrary](https://github.com/ZILtoid1991/bindbc-JSL) [![GitHub stars](https://img.shields.io/github/stars/ZILtoid1991/bindbc-JSL?style=flat)](https://github.com/ZILtoid1991/bindbc-JSL/stargazers) - Gamepad/Gyro input
	* [Newton Dynamics](https://github.com/DLangGamedev/bindbc-newton) [![GitHub stars](https://img.shields.io/github/stars/DLangGamedev/bindbc-newton?style=flat)](https://github.com/DLangGamedev/bindbc-newton/stargazers) - Physics library
	* [FreeImage](https://github.com/BindBC/bindbc-freeimage) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-freeimage?style=flat)](https://github.com/BindBC/bindbc-freeimage/stargazers) - Image loading
	* [FreeType](https://github.com/BindBC/bindbc-freetype) [![GitHub stars](https://img.shields.io/github/stars/BindBC/bindbc-freetype?style=flat)](https://github.com/BindBC/bindbc-freetype/stargazers) - Font rendering
	* [HarfBuzz](https://github.com/DlangGraphicsWG/bindbc-harfbuzz) [![GitHub stars](https://img.shields.io/github/stars/DlangGraphicsWG/bindbc-harfbuzz?style=flat)](https://github.com/DlangGraphicsWG/bindbc-harfbuzz/stargazers) - Text shaping
* [DerelictOrg](https://github.com/DerelictOrg) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg?style=flat)](https://github.com/DerelictOrg/stargazers) - Bindings, now largely outdated. BindBC is its modern successor.
	* [OpenGLES](https://github.com/DerelictOrg/DerelictGLES) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictGLES?style=flat)](https://github.com/DerelictOrg/DerelictGLES/stargazers) - Graphics API
	* [ENet](https://github.com/DerelictOrg/DerelictENet) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictENet?style=flat)](https://github.com/DerelictOrg/DerelictENet/stargazers) - Networking library
	* [libtheora](https://github.com/DerelictOrg/DerelictTheora) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictTheora?style=flat)](https://github.com/DerelictOrg/DerelictTheora/stargazers) - Video codec
	* [libogg](https://github.com/DerelictOrg/DerelictOgg) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictOgg?style=flat)](https://github.com/DerelictOrg/DerelictOgg/stargazers) - Audio codec
	* [libvorbis](https://github.com/DerelictOrg/DerelictVorbis) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictVorbis?style=flat)](https://github.com/DerelictOrg/DerelictVorbis/stargazers) - Audio codec
	* [libpq](https://github.com/DerelictOrg/DerelictPQ) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictPQ?style=flat)](https://github.com/DerelictOrg/DerelictPQ/stargazers) - PostgreSQL library
	* [PhysicsFS](https://github.com/DerelictOrg/DerelictPHYSFS) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictPHYSFS?style=flat)](https://github.com/DerelictOrg/DerelictPHYSFS/stargazers) - Virtual file system
	* [Open Dynamics Engine (ODE)](https://github.com/DerelictOrg/DerelictODE) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictODE?style=flat)](https://github.com/DerelictOrg/DerelictODE/stargazers) - Physics library
	* [ALURE](https://github.com/DerelictOrg/DerelictALURE) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictALURE?style=flat)](https://github.com/DerelictOrg/DerelictALURE/stargazers) - Audio library
	* [DevIL](https://github.com/DerelictOrg/DerelictIL) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictIL?style=flat)](https://github.com/DerelictOrg/DerelictIL/stargazers) - Image library

## Game Libraries

*D libraries for game development.*

* [InMath](https://github.com/Inochi2D/inmath) [![GitHub stars](https://img.shields.io/github/stars/Inochi2D/inmath?style=flat)](https://github.com/Inochi2D/inmath/stargazers) - Games math library for D.
* [godot-math](https://github.com/AuburnSounds/godot-math) [![GitHub stars](https://img.shields.io/github/stars/AuburnSounds/godot-math?style=flat)](https://github.com/AuburnSounds/godot-math/stargazers) - A D port of Godot's linear algebra with unchanged semantics.
* [text-mode](https://github.com/AuburnSounds/text-mode) [![GitHub stars](https://img.shields.io/github/stars/AuburnSounds/text-mode?style=flat)](https://github.com/AuburnSounds/text-mode/stargazers) - Virtual text mode with 8x8 Unicode font and markup language.

*Libraries for 2D-related projects.*

* [gfm](https://github.com/drug007/gfm7) [![GitHub stars](https://img.shields.io/github/stars/drug007/gfm7?style=flat)](https://github.com/drug007/gfm7/stargazers) - D gamedev toolkit.
* [Parin](https://github.com/Kapendev/parin) [![GitHub stars](https://img.shields.io/github/stars/Kapendev/parin?style=flat)](https://github.com/Kapendev/parin/stargazers) - A delightfully simple 2D game engine.
* [PixelPerfectEngine](https://github.com/ZILtoid1991/pixelperfectengine) [![GitHub stars](https://img.shields.io/github/stars/ZILtoid1991/pixelperfectengine?style=flat)](https://github.com/ZILtoid1991/pixelperfectengine/stargazers) - 2D graphics engine written in D.
* [HipremeEngine](https://github.com/MrcSnm/HipremeEngine) [![GitHub stars](https://img.shields.io/github/stars/MrcSnm/HipremeEngine?style=flat)](https://github.com/MrcSnm/HipremeEngine/stargazers) - Cross Platform D-Lang Game Engine with scripting support.
* [PixmapPresenter](https://github.com/adamdruppe/arsd/blob/master/pixmappresenter.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/pixmappresenter.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/pixmappresenter.d/stargazers) - High-level display library for blitting fully-rendered frames to the screen (→ software-rendering, retro graphics).

*Libraries for 2D/3D-related projects.*

* [rengfx](https://github.com/bmchtech/rengfx) [![GitHub stars](https://img.shields.io/github/stars/bmchtech/rengfx?style=flat)](https://github.com/bmchtech/rengfx/stargazers) - lightweight, expressive, extensible 2D/3D game engine.

*Libraries for 3D-related projects.*

* [Dagon](https://github.com/gecko0307/dagon) [![GitHub stars](https://img.shields.io/github/stars/gecko0307/dagon?style=flat)](https://github.com/gecko0307/dagon/stargazers) - 3D game engine for D. See: <https://gecko0307.github.io/dagon/>
* [Voxelman](https://github.com/MrSmith33/voxelman) [![GitHub stars](https://img.shields.io/github/stars/MrSmith33/voxelman?style=flat)](https://github.com/MrSmith33/voxelman/stargazers) - Plugin-based client-server voxel game engine written in D language.

## Games

*Games made with D.*

* [Spacecraft](https://github.com/Ingrater/Spacecraft) [![GitHub stars](https://img.shields.io/github/stars/Ingrater/Spacecraft?style=flat)](https://github.com/Ingrater/Spacecraft/stargazers) - A 3d multiplayer deathmatch space game written in D 2.0.
* [Dtanks](https://github.com/kingsleyh/dtanks) [![GitHub stars](https://img.shields.io/github/stars/kingsleyh/dtanks?style=flat)](https://github.com/kingsleyh/dtanks/stargazers) - Robot Tank Battle Game.
* [Electronvolt (formerly Atrium)](https://github.com/gecko0307/electronvolt) [![GitHub stars](https://img.shields.io/github/stars/gecko0307/electronvolt?style=flat)](https://github.com/gecko0307/electronvolt/stargazers) - FPS game with physics based puzzles using OpenGL.
* [Backgammony](https://github.com/jonathanballs/backgammony) [![GitHub stars](https://img.shields.io/github/stars/jonathanballs/backgammony?style=flat)](https://github.com/jonathanballs/backgammony/stargazers) - A Backgammon GUI for Linux built with Gtk.
* [Worms Within](https://kapendev.itch.io/worms-within) - A bite-sized escape room game.
* [Clean & Haunted](https://kapendev.itch.io/clean-haunted) - Clean a spooky haunted house.
* [Runani](https://kapendev.itch.io/runani) - An endless runner game where you help cute animals.
* [A Short Metamorphosis](https://kapendev.itch.io/a-short-metamorphosis) - A cute visual novel about looking at an egg.
* [Would you still save the world with me if I were a worm?](https://0xeab.itch.io/would-you-still-save-the-world-with-me-if-i-were-a-worm) - Help your wormy partner find the exit of each of the 20 puzzles to eventually save the world that has fallen into a wormhole.

## Internationalization

* [bindbc-icu](https://github.com/shoo/bindbc-icu) [![GitHub stars](https://img.shields.io/github/stars/shoo/bindbc-icu?style=flat)](https://github.com/shoo/bindbc-icu/stargazers) - bindbc bindings for the unicode ICU library.

## Image Processing

* [ArmageddonEngine](https://github.com/CyberShadow/ae/tree/master/utils/graphics) [![GitHub stars](https://img.shields.io/github/stars/CyberShadow/ae/tree/master/utils/graphics?style=flat)](https://github.com/CyberShadow/ae/tree/master/utils/graphics/stargazers) - Vladimir Panteleev's ae library has a package for image processing in functional style, which is described in the article [Functional Image Processing in D](https://blog.cy.md/2014/03/21/functional-image-processing-in-d/).
* [dlib.image](https://github.com/gecko0307/dlib) [![GitHub stars](https://img.shields.io/github/stars/gecko0307/dlib?style=flat)](https://github.com/gecko0307/dlib/stargazers) - image processing (8 and 16 bits per channel, floating point operations, filtering, FFT, HDRI, graphics formats support including JPEG and PNG)
* [color.d](https://github.com/adamdruppe/arsd/blob/master/color.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/color.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/color.d/stargazers) + [bmp.d](https://github.com/adamdruppe/arsd/blob/master/bmp.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/bmp.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/bmp.d/stargazers), [jpg.d](https://github.com/adamdruppe/arsd/blob/master/jpg.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/jpg.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/jpg.d/stargazers), [png.d](https://github.com/adamdruppe/arsd/blob/master/png.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/png.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/png.d/stargazers) - basic color struct, HSL functions and reading and writing image files
* [opencvd](https://github.com/aferust/opencvd) [![GitHub stars](https://img.shields.io/github/stars/aferust/opencvd?style=flat)](https://github.com/aferust/opencvd/stargazers) - Unofficial OpenCV binding for D
* [PixmapPaint](https://github.com/adamdruppe/arsd/blob/master/pixmappaint.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/pixmappaint.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/pixmappaint.d/stargazers) - Pixmap image manipulation library for software-rendering purposes.

## Machine Learning

* [vectorflow](https://github.com/Netflix/vectorflow) [![GitHub stars](https://img.shields.io/github/stars/Netflix/vectorflow?style=flat)](https://github.com/Netflix/vectorflow/stargazers) - Nexflix's opensource deep learning framework.
* [bindbc-onnxruntime](https://github.com/lempiji/bindbc-onnxruntime) [![GitHub stars](https://img.shields.io/github/stars/lempiji/bindbc-onnxruntime?style=flat)](https://github.com/lempiji/bindbc-onnxruntime/stargazers) - bindbc bindings to Microsoft's cross-platform, high performance ML inferencing and training accelerator
* [grain2](https://github.com/ShigekiKarita/grain2) [![GitHub stars](https://img.shields.io/github/stars/ShigekiKarita/grain2?style=flat)](https://github.com/ShigekiKarita/grain2/stargazers) - Autograd and GPGPU library for dynamic neural networks in D
* [tfd](https://github.com/ShigekiKarita/tfd) [![GitHub stars](https://img.shields.io/github/stars/ShigekiKarita/tfd?style=flat)](https://github.com/ShigekiKarita/tfd/stargazers) - Tensorflow wrapper for D

## Parallel Computing

* [DCompute](https://github.com/libmir/dcompute) [![GitHub stars](https://img.shields.io/github/stars/libmir/dcompute?style=flat)](https://github.com/libmir/dcompute/stargazers) - [GPGPU with Native D for OpenCL and CUDA](https://dlang.org/blog/2017/07/17/dcompute-gpgpu-with-native-d-for-opencl-and-cuda/)
* [DerelictCUDA](https://github.com/DerelictOrg/DerelictCUDA) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictCUDA?style=flat)](https://github.com/DerelictOrg/DerelictCUDA/stargazers) - Dynamic bindings to the CUDA library for the D Programming Language.
* [DerelictCL](https://github.com/DerelictOrg/DerelictCL) [![GitHub stars](https://img.shields.io/github/stars/DerelictOrg/DerelictCL?style=flat)](https://github.com/DerelictOrg/DerelictCL/stargazers) - Dynamic bindings to the OpenCL library for the D Programming Language.

## Scientific

*Scientific programming.*

* [scid](https://github.com/DlangScience/scid) [![GitHub stars](https://img.shields.io/github/stars/DlangScience/scid?style=flat)](https://github.com/DlangScience/scid/stargazers) - Scientific library for the D programming language
* [dstats](https://github.com/DlangScience/dstats) [![GitHub stars](https://img.shields.io/github/stars/DlangScience/dstats?style=flat)](https://github.com/DlangScience/dstats/stargazers) - A statistics library for D.
* [mir](https://github.com/libmir/mir) [![GitHub stars](https://img.shields.io/github/stars/libmir/mir?style=flat)](https://github.com/libmir/mir/stargazers) - Sandbox for some mir packages: sparse tensors, Hoffman and others.
* [mir-algorithm](https://github.com/libmir/mir) [![GitHub stars](https://img.shields.io/github/stars/libmir/mir?style=flat)](https://github.com/libmir/mir/stargazers) - N-dimensional arrays (matrixes, tensors), algorithms, general purpose library.
* [mir-random](https://github.com/libmir/mir-random) [![GitHub stars](https://img.shields.io/github/stars/libmir/mir-random?style=flat)](https://github.com/libmir/mir-random/stargazers) - Advanced Random Number Generators.

### Language Processing

* [bindbc-mecab](https://github.com/lempiji/bindbc-mecab) [![GitHub stars](https://img.shields.io/github/stars/lempiji/bindbc-mecab?style=flat)](https://github.com/lempiji/bindbc-mecab/stargazers) - bindbc MeCab binding (Part-of-Speech and Morphological Analyzer for Japanese)

## Text Processing

* [hunt-markdown](https://github.com/huntlabs/hunt-markdown) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-markdown?style=flat)](https://github.com/huntlabs/hunt-markdown/stargazers) - A markdown parsing and rendering library for D programming language. Support commonMark.
* [eBay's TSV utilities](https://github.com/eBay/tsv-utils/) [![GitHub stars](https://img.shields.io/github/stars/eBay/tsv-utils/?style=flat)](https://github.com/eBay/tsv-utils//stargazers) - Filtering, statistics, sampling, joins and other operations on TSV files. Very fast, especially good for large datasets.

## Logging

*Print with care.*

* [dlog](https://github.com/deavmi/dlog) [![GitHub stars](https://img.shields.io/github/stars/deavmi/dlog?style=flat)](https://github.com/deavmi/dlog/stargazers) - extensible logging framework with message transformation support and custom loggers and contexts
* [std.experimenatal.logger](https://dlang.org/phobos/std_experimental_logger.html) - Phobos's upcoming standard logging facility.
* [dlogg](https://github.com/NCrashed/dlogg) [![GitHub stars](https://img.shields.io/github/stars/NCrashed/dlogg?style=flat)](https://github.com/NCrashed/dlogg/stargazers) - Logging for concurrent applications and daemons with lazy and delayed logging, logrotate support.

## Configuration

*Parsing configuration files.*

* [sdlang](https://github.com/dlang-community/SDLang-D) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/SDLang-D?style=flat)](https://github.com/dlang-community/SDLang-D/stargazers) - An SDL (Simple Declarative Language) library for D.
* [D:YAML](https://github.com/dlang-community/D-YAML) [![GitHub stars](https://img.shields.io/github/stars/dlang-community/D-YAML?style=flat)](https://github.com/dlang-community/D-YAML/stargazers) - YAML parser and emitter for the D programming language.
* [inifile-D](https://github.com/burner/inifiled) [![GitHub stars](https://img.shields.io/github/stars/burner/inifiled?style=flat)](https://github.com/burner/inifiled/stargazers) - A compile time ini file parser and writer generator for D
* [arsd.ini](https://github.com/adamdruppe/arsd/blob/master/ini.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/ini.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/ini.d/stargazers) - A configurable INI parser with support for multiple “dialects” of the format.

## Blog Engine

*Hosting blogs yourself.*

* [mood](https://github.com/mihails-strasuns/mood) [![GitHub stars](https://img.shields.io/github/stars/mihails-strasuns/mood?style=flat)](https://github.com/mihails-strasuns/mood/stargazers) - simple vibe.d based blog engine
* [adrdox](https://github.com/adamdruppe/adrdox) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/adrdox?style=flat)](https://github.com/adamdruppe/adrdox/stargazers) - A documentation generator that can also be used for blogging. (Used by the *This Week in ARSD* blog.)

## Dependency Injection

*Apply inversion of control.*

* [Poodinis](https://github.com/mbierlee/poodinis) [![GitHub stars](https://img.shields.io/github/stars/mbierlee/poodinis?style=flat)](https://github.com/mbierlee/poodinis/stargazers) - A dependency injection framework for D with support for autowiring.
* [arsd.di](https://github.com/adamdruppe/arsd/blob/master/di.d) [![GitHub stars](https://img.shields.io/github/stars/adamdruppe/arsd/blob/master/di.d?style=flat)](https://github.com/adamdruppe/arsd/blob/master/di.d/stargazers) - A single-file lightweight dependency injection framework.

## Cryptography

* [Botan](https://github.com/etcimon/botan) [![GitHub stars](https://img.shields.io/github/stars/etcimon/botan?style=flat)](https://github.com/etcimon/botan/stargazers) - Block & stream ciphers, public key crypto, hashing, KDF, MAC, PKCS, TLS, ASN.1, BER/DER, etc.
* [OpenSSL](https://github.com/D-Programming-Deimos/openssl) [![GitHub stars](https://img.shields.io/github/stars/D-Programming-Deimos/openssl?style=flat)](https://github.com/D-Programming-Deimos/openssl/stargazers) - D version of the C headers for OpenSSL.
* [Crypto](https://github.com/shove70/crypto) [![GitHub stars](https://img.shields.io/github/stars/shove70/crypto?style=flat)](https://github.com/shove70/crypto/stargazers) - A D Library of encryption, decryption, encode, hash, and message digital signatures.

## Unmaintained

*Old or archived projects saved for reference.*

* [dunit](https://github.com/nomad-software/dunit) [![GitHub stars](https://img.shields.io/github/stars/nomad-software/dunit?style=flat)](https://github.com/nomad-software/dunit/stargazers) - Advanced unit testing & mocking toolkit
* [hunt](https://github.com/huntlabs/hunt) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt?style=flat)](https://github.com/huntlabs/hunt/stargazers) - A refined core library for D programming language. The module has concurrency / collection / event / io / logging / text / serialize and more.
* [hunt-time](https://github.com/huntlabs/hunt-time) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-time?style=flat)](https://github.com/huntlabs/hunt-time/stargazers) - A time library and similar to Joda-time and Java.time api.
* [hunt-validation](https://github.com/huntlabs/hunt-validation) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-validation?style=flat)](https://github.com/huntlabs/hunt-validation/stargazers) - A data validation library for DLang based on hunt library.
* [collie](https://github.com/huntlabs/collie) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/collie?style=flat)](https://github.com/huntlabs/collie/stargazers) - An asynchronous event-driven network framework written in dlang, like netty framework in D.
* [hunt-net](https://github.com/huntlabs/hunt-net) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-net?style=flat)](https://github.com/huntlabs/hunt-net/stargazers) - High-performance network library for D programming language, event-driven asynchonous implemention(IOCP / kqueue / epoll).
* [hunt-http](https://github.com/huntlabs/hunt-http) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-http?style=flat)](https://github.com/huntlabs/hunt-http/stargazers) - HTTP/1 and HTTP/2 protocol library for D.
* [Hunt Framework](https://github.com/huntlabs/hunt-framework/) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-framework/?style=flat)](https://github.com/huntlabs/hunt-framework//stargazers) - Hunt is a high-level D Programming Language Web framework that encourages rapid development and clean, pragmatic design. It lets you build high-performance Web applications quickly and easily.
* [grpc](https://github.com/huntlabs/grpc-dlang) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/grpc-dlang?style=flat)](https://github.com/huntlabs/grpc-dlang/stargazers) - Grpc for D programming language, hunt-http library based.
* [kissrpc](https://github.com/huntlabs/kissrpc) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/kissrpc?style=flat)](https://github.com/huntlabs/kissrpc/stargazers) - Fast and light, flatbuffers based rpc framework.
* [hunt-gossip](https://github.com/huntlabs/hunt-gossip) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-gossip?style=flat)](https://github.com/huntlabs/hunt-gossip/stargazers) - A Apache V2 gossip protocol implementation for D programming language.
* [hunt-cache](https://github.com/huntlabs/hunt-cache) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-cache?style=flat)](https://github.com/huntlabs/hunt-cache/stargazers) - D language universal cache library, using radix, redis and memcached.
* [flatbuffers](https://github.com/huntlabs/flatbuffers) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/flatbuffers?style=flat)](https://github.com/huntlabs/flatbuffers/stargazers) - D Programming Language implementation of the google flatbuffers library.
* [hunt-entity](https://github.com/huntlabs/hunt-entity) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-entity?style=flat)](https://github.com/huntlabs/hunt-entity/stargazers) - Hunt entity is an object-relational mapping tool for the D programming language. Referring to the design idea of JPA, support PostgreSQL / MySQL / SQLite.
* [hunt-database](https://github.com/huntlabs/hunt-database) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-database?style=flat)](https://github.com/huntlabs/hunt-database/stargazers) - Hunt database abstraction layer for D programing language, support PostgreSQL / MySQL / SQLite.
* [hunt-console](https://github.com/huntlabs/hunt-console) [![GitHub stars](https://img.shields.io/github/stars/huntlabs/hunt-console?style=flat)](https://github.com/huntlabs/hunt-console/stargazers) - Hunt console creation easier to create powerful command-line applications.
* [DWT](https://github.com/d-widget-toolkit/dwt) [![GitHub stars](https://img.shields.io/github/stars/d-widget-toolkit/dwt?style=flat)](https://github.com/d-widget-toolkit/dwt/stargazers) - A library for creating cross-platform GUI applications. GWT is a port of the Java SWT library to D. DWT was promoted as a semi-standard GUI library for D, but unfortunately didn't catch up popularity yet.
* [LibUI](https://github.com/Extrawurst/DerelictLibui) [![GitHub stars](https://img.shields.io/github/stars/Extrawurst/DerelictLibui?style=flat)](https://github.com/Extrawurst/DerelictLibui/stargazers) - Dynamic Binding for [libui](https://github.com/andlabs/libui) [![GitHub stars](https://img.shields.io/github/stars/andlabs/libui?style=flat)](https://github.com/andlabs/libui/stargazers)
