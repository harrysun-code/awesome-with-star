# Lua

> 来源：[LewisJEllis/awesome-lua](https://github.com/LewisJEllis/awesome-lua)

[![GitHub stars](https://img.shields.io/github/stars/LewisJEllis/awesome-lua?style=flat)](https://github.com/LewisJEllis/awesome-lua/stargazers)

# Awesome Lua [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of quality Lua [packages](#packages) and [resources](#resources).

Inspired by the lists [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers), [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers), and [awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome-nodejs?style=flat)](https://github.com/sindresorhus/awesome-nodejs/stargazers).


## Packages
- [Implementations, Interpreters, and Bindings](#implementations-interpreters-and-bindings)
- [Package Managers](#package-managers)
- [Build Tools and Standalone Makers](#build-tools-and-standalone-makers)
- [Debugging and Profiling](#debugging-and-profiling)
- [IDEs and Plugins](#ides-and-plugins)
- [Utility Belts](#utility-belts)
- [Game Engines](#game-engines)
- [Game Development](#game-development)
- [Logging](#logging)
- [Web/Networking Platforms](#webnetworking-platforms)
- [OpenResty](#openresty)
- [Command-line Utilities](#command-line-utilities)
- [Concurrency and Multithreading](#concurrency-and-multithreading)
- [Templating](#templating)
- [Documentation](#documentation)
- [Object-oriented Programming](#object-oriented-programming)
- [File system and OS](#file-system-and-os)
- [Time and Date](#time-and-date)
- [Image Manipulation](#image-manipulation)
- [Digital Signal Processing](#digital-signal-processing)
- [Hardware and Embedded Systems](###hardware-and-embedded-systems)
- [Math and Scientific Computing](#math-and-scientific-computing)
- [Parsing and Serialization](#parsing-and-serialization)
- [Humanize](#humanize)
- [Compression](#compression)
- [Cryptography](#cryptography)
- [Network](#network)
- [Data Stores](#data-stores)
- [Message Brokers](#message-brokers)
- [Testing](#testing)
- [Foreign Function Interfaces](#foreign-function-interfaces)
- [Analysis Tools and ASTs](#analysis-tools-and-asts)
- [Experimental, etc](#experimental-etc)
- [Scriptable by Lua](#scriptable-by-lua)
- [Miscellaneous](#miscellaneous)


## Resources
- [Community](#community)
- [References](#references)
- [Style Guides](#style-guides)
- [Tutorials](#tutorials)
- [Articles](#articles)
- [Talks & Slides](#talks--slides)
- [Books](#books)
- [Other Lists](#other-lists)


### Implementations, Interpreters, and Bindings
- [Lua](http://www.lua.org/download.html) - Lua's original ANSI C interpreter.
  - [Lua Repo](https://github.com/lua/lua) [![GitHub stars](https://img.shields.io/github/stars/lua/lua?style=flat)](https://github.com/lua/lua/stargazers) - The official Lua repo, as seen by the Lua team, mirrored to GitHub.
- [LuaJIT](http://luajit.org/luajit.html) - High-performance Just-In-Time compiler for Lua.
- [LLVM-Lua](https://github.com/neopallium/llvm-lua) [![GitHub stars](https://img.shields.io/github/stars/neopallium/llvm-lua?style=flat)](https://github.com/neopallium/llvm-lua/stargazers) - Compiles Lua to LLVM.
- [lua.vm.js](https://github.com/daurnimator/lua.vm.js) [![GitHub stars](https://img.shields.io/github/stars/daurnimator/lua.vm.js?style=flat)](https://github.com/daurnimator/lua.vm.js/stargazers) - Lua VM on the web; a direct port of the C interpreter via LLVM, emscripten, and asm.js.
- [Moonshine](https://github.com/gamesys/moonshine) [![GitHub stars](https://img.shields.io/github/stars/gamesys/moonshine?style=flat)](https://github.com/gamesys/moonshine/stargazers) - A Lua VM implemented in JavaScript. Slower than lua.vm.js, but with better docs, examples, and JS interfacing.
- [Fengari](https://fengari.io/) - The Lua VM rewritten in Javascript with seamless JS and DOM interoperability.
- [MoonSharp](https://github.com/xanathar/moonsharp) [![GitHub stars](https://img.shields.io/github/stars/xanathar/moonsharp?style=flat)](https://github.com/xanathar/moonsharp/stargazers) - A Lua interpreter written entirely in C# for the .NET, Mono and Unity platforms.
- [UniLua](https://github.com/xebecnan/UniLua) [![GitHub stars](https://img.shields.io/github/stars/xebecnan/UniLua?style=flat)](https://github.com/xebecnan/UniLua/stargazers) - A pure C# implementation of Lua 5.2, focused on compatibility with the Unity game engine.
- [lupa](https://github.com/scoder/lupa) [![GitHub stars](https://img.shields.io/github/stars/scoder/lupa?style=flat)](https://github.com/scoder/lupa/stargazers) - Python bindings to LuaJIT2.
- [golua](https://github.com/aarzilli/golua) [![GitHub stars](https://img.shields.io/github/stars/aarzilli/golua?style=flat)](https://github.com/aarzilli/golua/stargazers) - Golang bindings to the Lua C API.
- [GopherLua](https://github.com/yuin/gopher-lua) [![GitHub stars](https://img.shields.io/github/stars/yuin/gopher-lua?style=flat)](https://github.com/yuin/gopher-lua/stargazers) - Lua 5.1 VM and compiler implemented in Go with Go APIs.
- [LuaBridge](https://github.com/vinniefalco/LuaBridge) [![GitHub stars](https://img.shields.io/github/stars/vinniefalco/LuaBridge?style=flat)](https://github.com/vinniefalco/LuaBridge/stargazers) - A lightweight library for mapping data, functions, and classes back and forth between C++ and Lua.

Note: From LuaJIT to Lua to lua.vm.js to Moonshine, a basic benchmark sees performance drop by roughly a factor of 6 with each hop.


### Package Managers
- [LuaRocks](https://luarocks.org/) - De-facto tool for installing Lua modules as packages called "rocks", plus public rock repository and website.  Much like npm or pip.


### Build Tools and Standalone Makers
- [Lake](https://github.com/stevedonovan/Lake) [![GitHub stars](https://img.shields.io/github/stars/stevedonovan/Lake?style=flat)](https://github.com/stevedonovan/Lake/stargazers) - A build engine written in Lua, similar to Ruby's rake.
- [Luabuild](https://github.com/stevedonovan/luabuild) [![GitHub stars](https://img.shields.io/github/stars/stevedonovan/luabuild?style=flat)](https://github.com/stevedonovan/luabuild/stargazers) - Highly customizable Lua 5.2 build system.
- [luastatic](https://github.com/ers35/luastatic) [![GitHub stars](https://img.shields.io/github/stars/ers35/luastatic?style=flat)](https://github.com/ers35/luastatic/stargazers) - Simple tool for turning Lua programs into standalone executables.
- [omnia](https://github.com/tongson/omnia) [![GitHub stars](https://img.shields.io/github/stars/tongson/omnia?style=flat)](https://github.com/tongson/omnia/stargazers) - A batteries-included creator of standalone executables, built on top of luastatic.


### Debugging and Profiling
- [ProFi](https://gist.github.com/perky/2838755) - Simple profiler that works with LuaJIT and produces a report file.
- [luatrace](https://github.com/geoffleyland/luatrace) [![GitHub stars](https://img.shields.io/github/stars/geoffleyland/luatrace?style=flat)](https://github.com/geoffleyland/luatrace/stargazers) - Toolset for tracing/analyzing/profiling script execution and generating detailed reports.
- [StackTracePlus](https://github.com/ignacio/StackTracePlus) [![GitHub stars](https://img.shields.io/github/stars/ignacio/StackTracePlus?style=flat)](https://github.com/ignacio/StackTracePlus/stargazers) - Drop-in upgrade to Lua's stack traces which adds local context and improves readability.
- [MobDebug](https://github.com/pkulchenko/MobDebug) [![GitHub stars](https://img.shields.io/github/stars/pkulchenko/MobDebug?style=flat)](https://github.com/pkulchenko/MobDebug/stargazers) - Powerful remote debugger with breakpoints and stack inspection. Used by ZeroBraneStudio.
- [lovebird](https://github.com/rxi/lovebird) [![GitHub stars](https://img.shields.io/github/stars/rxi/lovebird?style=flat)](https://github.com/rxi/lovebird/stargazers) - Browser-based debug console. Originally made for LÖVE, but works in any project with LuaSocket support.


### IDEs and Plugins
- [Lua Development Tools](https://eclipse.org/ldt/) - Eclipse plugin which provides code completion, debugging, and more. Built on Metalua.
- [Lua for IDEA](https://bitbucket.org/sylvanaar2/lua-for-idea/wiki/Home) - IntelliJ IDEA plugin which, among other things, provides code completion, smart highlighting, and experimental debugging.
- [ZeroBraneStudio](https://studio.zerobrane.com/) - Lightweight, customizable, cross-platform Lua-dedicated IDE with code completion and analysis, written in Lua. Has broad debugging support for numerous Lua engines.
- [BabeLua](https://archive.codeplex.com/?p=babelua) - Lua editor/debugger extension for VS2012-13 with highlighting, auto-completion, linting, and formatting capabilities.
- [lua-mode](https://github.com/immerrr/lua-mode) [![GitHub stars](https://img.shields.io/github/stars/immerrr/lua-mode?style=flat)](https://github.com/immerrr/lua-mode/stargazers) - Emacs major mode for editing Lua.
- [vscode-lua](https://github.com/trixnz/vscode-lua) [![GitHub stars](https://img.shields.io/github/stars/trixnz/vscode-lua?style=flat)](https://github.com/trixnz/vscode-lua/stargazers) - VSCode intellisense and linting.


### Utility Belts
- [Lua Fun](https://github.com/luafun/luafun) [![GitHub stars](https://img.shields.io/github/stars/luafun/luafun?style=flat)](https://github.com/luafun/luafun/stargazers) - High-performance functional programming library designed for LuaJIT.
- [Moses](https://github.com/Yonaba/Moses) [![GitHub stars](https://img.shields.io/github/stars/Yonaba/Moses?style=flat)](https://github.com/Yonaba/Moses/stargazers) - Functional programming utility belt, inspired by Underscore.js.
- [Penlight](https://github.com/stevedonovan/Penlight) [![GitHub stars](https://img.shields.io/github/stars/stevedonovan/Penlight?style=flat)](https://github.com/stevedonovan/Penlight/stargazers) - Broad, heavyweight utility library, inspired by Python's standard libs. Provides the batteries that Lua doesn't.
- [lua-stdlib](https://github.com/lua-stdlib/lua-stdlib) [![GitHub stars](https://img.shields.io/github/stars/lua-stdlib/lua-stdlib?style=flat)](https://github.com/lua-stdlib/lua-stdlib/stargazers) - Middle-weight standard library extension; adds some useful data structures, utility functions, and basic functional stuff.
- [Microlight](https://github.com/stevedonovan/Microlight) [![GitHub stars](https://img.shields.io/github/stars/stevedonovan/Microlight?style=flat)](https://github.com/stevedonovan/Microlight/stargazers) - A little library of useful Lua functions; the 'extra light' version of Penlight.
- [compat53](https://luarocks.org/modules/siffiejoe/compat53) - Compatibility module providing Lua-5.3-style APIs for Lua 5.2 and 5.1.
- [RxLua](https://github.com/bjornbytes/RxLua) [![GitHub stars](https://img.shields.io/github/stars/bjornbytes/RxLua?style=flat)](https://github.com/bjornbytes/RxLua/stargazers) - Reactive Extensions, Observables, etc.


### Game Engines
- [LÖVE 2D](http://love2d.org/) - Desktop game development platform. Cross-platform, feature-complete, well-adopted.
- [Corona SDK](https://coronalabs.com/) - Development platform for iOS and Android. Proprietary, but used by numerous top games and apps, totaling over 150 million downloads.
- [MOAI](http://getmoai.com/) - Open source, cross-platform, mobile game development framework. Minimalist C++ engine powered by Lua scripting.
- [Drystal](https://drystal.github.io/) - Open source, games can run on Linux or on any platform with a recent web browser.
- [Amulet](http://www.amulet.xyz/) - Open source, audio/visual toolkit suitable for small games and experimentation. It runs on Windows, Mac, Linux, HTML5 and iOS.
- [LÖVR](https://lovr.org) - 3D framework for creating virtual reality experiences, inspired by LÖVE 2D.


### Game Development
- Corona
  - [Coronium](https://develephant.github.io/coronium-core-docs/) - Simple cloud platform supporting analytics, data objects, user management, and more.
- LÖVE
  - [awesome-love2d](https://github.com/love2d-community/awesome-love2d) [![GitHub stars](https://img.shields.io/github/stars/love2d-community/awesome-love2d?style=flat)](https://github.com/love2d-community/awesome-love2d/stargazers) - A list like this one, but focused on game dev and the LÖVE platform.
  - [lurker](https://github.com/rxi/lurker) [![GitHub stars](https://img.shields.io/github/stars/rxi/lurker?style=flat)](https://github.com/rxi/lurker/stargazers) - Shortens the iteration cycle by auto-swapping changed Lua files in a running LÖVE project.
  - [HUMP](http://vrld.github.io/hump/) - A set of lightweight helpers for LÖVE; a game-oriented utility belt.
- MOAI
  - [moaifiddle](https://moaifiddle.com) - Edit and share short scripts for the MOAI game engine and run them in the browser using WebGL.
- [Jumper](https://github.com/Yonaba/Jumper) [![GitHub stars](https://img.shields.io/github/stars/Yonaba/Jumper?style=flat)](https://github.com/Yonaba/Jumper/stargazers) - Fast, lightweight, and easy-to-use pathfinding library for grid-based games.
- [lume](https://github.com/rxi/lume/) [![GitHub stars](https://img.shields.io/github/stars/rxi/lume/?style=flat)](https://github.com/rxi/lume//stargazers) - Utility belt library geared toward game development.
- [NoobHub](https://github.com/Overtorment/NoobHub) [![GitHub stars](https://img.shields.io/github/stars/Overtorment/NoobHub?style=flat)](https://github.com/Overtorment/NoobHub/stargazers) - Network multiplayer for Corona, LÖVE, and more, following a simple pub-sub model.
- Collision detection
  - [bump.lua](https://github.com/kikito/bump.lua) [![GitHub stars](https://img.shields.io/github/stars/kikito/bump.lua?style=flat)](https://github.com/kikito/bump.lua/stargazers) - Minimal rectangle-based collision detection which handles tunnelling and basic collision resolution.
  - [HardonCollider](http://vrld.github.io/HardonCollider/) - Detect collisions between arbitrarily positioned and rotated shapes of any type.
- Tweening
  - [flux](https://github.com/rxi/flux) [![GitHub stars](https://img.shields.io/github/stars/rxi/flux?style=flat)](https://github.com/rxi/flux/stargazers) - A fast, lightweight tweening library for Lua with easing functions and the ability to group tweens together.
  - [tween.lua](https://github.com/kikito/tween.lua) [![GitHub stars](https://img.shields.io/github/stars/kikito/tween.lua?style=flat)](https://github.com/kikito/tween.lua/stargazers) - Small library for tweening, with several easing functions.
- Examples
  - [termtris](https://github.com/tylerneylon/termtris) [![GitHub stars](https://img.shields.io/github/stars/tylerneylon/termtris?style=flat)](https://github.com/tylerneylon/termtris/stargazers) - A tetris clone, written in literate style with "an emphasis on learn-from-ability".
  - [PacPac](https://github.com/tylerneylon/pacpac) [![GitHub stars](https://img.shields.io/github/stars/tylerneylon/pacpac?style=flat)](https://github.com/tylerneylon/pacpac/stargazers) - A Pac-man clone, made with LÖVE.
  - [Mari0](https://github.com/Stabyourself/mari0) [![GitHub stars](https://img.shields.io/github/stars/Stabyourself/mari0?style=flat)](https://github.com/Stabyourself/mari0/stargazers) - Fusion of Mario and Portal, made with LÖVE. See also its [wikipedia entry](https://en.wikipedia.org/wiki/Mari0).
  - [Journey to the Center of Hawkthorne](https://github.com/hawkthorne/hawkthorne-journey) [![GitHub stars](https://img.shields.io/github/stars/hawkthorne/hawkthorne-journey?style=flat)](https://github.com/hawkthorne/hawkthorne-journey/stargazers) - 2D platformer based on Community's [Digital Estate Planning](https://en.wikipedia.org/wiki/Digital_Estate_Planning) episode, made with LÖVE.


### Logging
- [lua-log](https://github.com/moteus/lua-log) [![GitHub stars](https://img.shields.io/github/stars/moteus/lua-log?style=flat)](https://github.com/moteus/lua-log/stargazers) - Asynchronous logging library with pluggable writers for file system, network, ZeroMQ, and more.
- [LuaLogging](https://github.com/Neopallium/lualogging) [![GitHub stars](https://img.shields.io/github/stars/Neopallium/lualogging?style=flat)](https://github.com/Neopallium/lualogging/stargazers) - Log4j-inspired logging library supporting various appenders.
- [luasyslog](https://luarocks.org/modules/luarocks/luasyslog) - Log to syslog, based on LuaLogging.


### Web/Networking Platforms
- [OpenResty](http://openresty.org/en/) - A fast and scalable web application platform created by extending Nginx with Lua. Today's de-facto Lua web platform, used heavily by Cloudflare, Taobao, Tencent, and others.
- [turbo](https://turbo.readthedocs.io/en/latest/) - Event-driven, non-blocking, LuaJIT-based networking suite and framework, inspired by Tornado.
- [Kepler Project](https://github.com/keplerproject) [![GitHub stars](https://img.shields.io/github/stars/keplerproject?style=flat)](https://github.com/keplerproject/stargazers) - A collection of web-oriented projects using a common set of standards and components.
- [Pegasus.lua](https://github.com/EvandroLG/pegasus.lua) [![GitHub stars](https://img.shields.io/github/stars/EvandroLG/pegasus.lua?style=flat)](https://github.com/EvandroLG/pegasus.lua/stargazers) - Pegasus.lua is a http server to work with web applications written in Lua language.


### OpenResty
- [awesome-resty](https://github.com/bungle/awesome-resty) [![GitHub stars](https://img.shields.io/github/stars/bungle/awesome-resty?style=flat)](https://github.com/bungle/awesome-resty/stargazers) - A list like this one, but focused on OpenResty.
- Core platform
  - [ngx_lua](https://www.nginx.com/resources/wiki/modules/lua/) - The core piece of OpenResty. Embeds Lua in Nginx and exposes, among other things, the cosocket API for non-blocking sockets (compatible with LuaSocket's API).
  - [OpenResty GitHub Organization](https://github.com/openresty) [![GitHub stars](https://img.shields.io/github/stars/openresty?style=flat)](https://github.com/openresty/stargazers) - Home of the repositories for ngx_lua, ngx_openresty, and many related modules.
- Third-party modules
  - [lua-resty-http](https://github.com/pintsized/lua-resty-http) [![GitHub stars](https://img.shields.io/github/stars/pintsized/lua-resty-http?style=flat)](https://github.com/pintsized/lua-resty-http/stargazers) - Lua HTTP client driver, built on the cosocket API.
- Frameworks & tools
  - [Lapis](http://leafo.net/lapis/) - Full-stack framework for Lua and OpenResty. Like the Django or Rails of Lua. Supports Moonscript.
  - [ledge](https://github.com/pintsized/ledge) [![GitHub stars](https://img.shields.io/github/stars/pintsized/ledge?style=flat)](https://github.com/pintsized/ledge/stargazers) - Lua module providing scriptable, RFC-compliant HTTP cache functionality.
  - [Sailor](https://github.com/sailorproject/sailor) [![GitHub stars](https://img.shields.io/github/stars/sailorproject/sailor?style=flat)](https://github.com/sailorproject/sailor/stargazers) — An MVC web framework compatible with OpenResty, Apache and other webservers.
  - [Kong](https://github.com/Kong/kong) [![GitHub stars](https://img.shields.io/github/stars/Kong/kong?style=flat)](https://github.com/Kong/kong/stargazers) - Microservice & API Management Layer.

Search this page for 'OpenResty' to find related packages under other categories (data stores in particular).


### Command-line Utilities
- [ansicolors](https://github.com/kikito/ansicolors.lua) [![GitHub stars](https://img.shields.io/github/stars/kikito/ansicolors.lua?style=flat)](https://github.com/kikito/ansicolors.lua/stargazers) - Simple function for printing to the console in color.
- [cliargs](https://github.com/amireh/lua_cliargs) [![GitHub stars](https://img.shields.io/github/stars/amireh/lua_cliargs?style=flat)](https://github.com/amireh/lua_cliargs/stargazers) - A simple command-line argument parsing module.
- [lua-term](https://github.com/hoelzro/lua-term) [![GitHub stars](https://img.shields.io/github/stars/hoelzro/lua-term?style=flat)](https://github.com/hoelzro/lua-term/stargazers) - Terminal operations and manipulations.
- [argparse](https://github.com/mpeterv/argparse) [![GitHub stars](https://img.shields.io/github/stars/mpeterv/argparse?style=flat)](https://github.com/mpeterv/argparse/stargazers) - A feature-rich command line parser inspired by argparse for Python.

### Concurrency and Multithreading
- Coroutine-based multitasking:
  - [Lumen](https://github.com/xopxe/Lumen) [![GitHub stars](https://img.shields.io/github/stars/xopxe/Lumen?style=flat)](https://github.com/xopxe/Lumen/stargazers) - Simple concurrent task scheduling.
  - [ConcurrentLua](https://github.com/lefcha/concurrentlua) [![GitHub stars](https://img.shields.io/github/stars/lefcha/concurrentlua?style=flat)](https://github.com/lefcha/concurrentlua/stargazers) - Implements an Erlang-style message-passing concurrency model.
  - [cqueues](http://25thandclement.com/~william/projects/cqueues.html) - Library for managing sockets, signals, and threads based on an event loop with coroutines.
- Multithreading:
  - [llthreads](https://github.com/Neopallium/lua-llthreads) [![GitHub stars](https://img.shields.io/github/stars/Neopallium/lua-llthreads?style=flat)](https://github.com/Neopallium/lua-llthreads/stargazers) - A simple wrapper for low-level pthreads & WIN32 threads.
  - [llthreads2](https://github.com/moteus/lua-llthreads2) [![GitHub stars](https://img.shields.io/github/stars/moteus/lua-llthreads2?style=flat)](https://github.com/moteus/lua-llthreads2/stargazers) - Newer rewrite of llthreads.
  - [lanes](https://github.com/LuaLanes/lanes) [![GitHub stars](https://img.shields.io/github/stars/LuaLanes/lanes?style=flat)](https://github.com/LuaLanes/lanes/stargazers) - Library implementing a message passing model with one OS thread per Lua thread.
  - [luaproc](https://github.com/askyrme/luaproc) [![GitHub stars](https://img.shields.io/github/stars/askyrme/luaproc?style=flat)](https://github.com/askyrme/luaproc/stargazers) - Message-passing model which allows multiple threads per OS thread and easily generalizes across a network. See also [the paper](http://www.inf.puc-rio.br/~roberto/docs/ry08-05.pdf) where it originated.

For more on the differences (particularly between `lanes` and `luaproc`), see this [comparison](http://www.luteus.biz/Download/LoriotPro_Doc/LUA/LUA_For_Windows/lanes/comparison.html) of options; somewhat dated, but covers how each one works and the significant differences.


### Templating
- [lustache](http://olivinelabs.com/lustache/) - Mustache template implementation.
- [etlua](https://github.com/leafo/etlua) [![GitHub stars](https://img.shields.io/github/stars/leafo/etlua?style=flat)](https://github.com/leafo/etlua/stargazers) - Embedded Lua templates, ERB-style.
- [lua-resty-template](https://github.com/bungle/lua-resty-template) [![GitHub stars](https://img.shields.io/github/stars/bungle/lua-resty-template?style=flat)](https://github.com/bungle/lua-resty-template/stargazers) - Lua-oriented template engine for OpenResty, somewhat Jinja-like.


### Documentation
- [LDoc](http://stevedonovan.github.io/ldoc/) - Documentation generator which modernizes and extends [LuaDoc](http://keplerproject.github.io/luadoc/).
- [Locco](http://rgieseke.github.io/locco/) - Lua port of [Docco](http://ashkenas.com/docco/), the "quick-and-dirty, hundred-line-long, literate-programming-style documentation generator".
- [docroc](https://github.com/bjornbytes/docroc) [![GitHub stars](https://img.shields.io/github/stars/bjornbytes/docroc?style=flat)](https://github.com/bjornbytes/docroc/stargazers) - Parse comments into a Lua table to generate documentation.


### Object-oriented Programming
- [30log](https://github.com/Yonaba/30log) [![GitHub stars](https://img.shields.io/github/stars/Yonaba/30log?style=flat)](https://github.com/Yonaba/30log/stargazers) - Minimalist OOP library with basic classes, inheritance, and mixins in 30 lines.
- [middleclass](https://github.com/kikito/middleclass) [![GitHub stars](https://img.shields.io/github/stars/kikito/middleclass?style=flat)](https://github.com/kikito/middleclass/stargazers) - Simple but robust OOP library with inheritance, methods, metamethods, class variables and mixins.


### File system and OS
- [LuaFileSystem](http://keplerproject.github.io/luafilesystem/) - Extends and complements Lua's built-in set of file system functions.
- [luaposix](https://github.com/luaposix/luaposix) [![GitHub stars](https://img.shields.io/github/stars/luaposix/luaposix?style=flat)](https://github.com/luaposix/luaposix/stargazers) - Bindings for POSIX APIs, including curses.
- [lunix](http://25thandclement.com/~william/projects/lunix.html) - Bindings to common Unix system APIs, striving for thread-safety.
- [lua-path](https://github.com/moteus/lua-path) [![GitHub stars](https://img.shields.io/github/stars/moteus/lua-path?style=flat)](https://github.com/moteus/lua-path/stargazers) - File system path manipulation library.


### Time and Date
- [LuaDate](https://github.com/Tieske/date) [![GitHub stars](https://img.shields.io/github/stars/Tieske/date?style=flat)](https://github.com/Tieske/date/stargazers) - Date and time module with parsing, formatting, addition/subtraction, localization, and ISO 8601 support.
- [cron.lua](https://github.com/kikito/cron.lua) [![GitHub stars](https://img.shields.io/github/stars/kikito/cron.lua?style=flat)](https://github.com/kikito/cron.lua/stargazers) - Time-related functions for Lua, inspired by JavaScript's setTimeout and setInterval.
- [luatx](https://github.com/daurnimator/luatz) [![GitHub stars](https://img.shields.io/github/stars/daurnimator/luatz?style=flat)](https://github.com/daurnimator/luatz/stargazers) - Time, date, and timezone library.


### Image Manipulation
- [magick](https://github.com/leafo/magick) [![GitHub stars](https://img.shields.io/github/stars/leafo/magick?style=flat)](https://github.com/leafo/magick/stargazers) - Lua bindings to ImageMagick for LuaJIT using FFI.


### Digital Signal Processing
- [LuaFFT](https://github.com/h4rm/luafft) [![GitHub stars](https://img.shields.io/github/stars/h4rm/luafft?style=flat)](https://github.com/h4rm/luafft/stargazers) - An easy to use Fast Fourier Transformation package in pure Lua.
- [Worp](http://worp.zevv.nl/about.html) - Sound/music/DSP engine written for LuaJIT.


### Hardware and Embedded Systems
- [eLua](http://www.eluaproject.net/) - Lua, extended with optimizations and specific features for efficient and portable embedded software development.


### Math and Scientific Computing
- [SciLua](http://scilua.org/) - Numerical/scientific computing framework built on LuaJIT, with an interface to R.
- [Torch7](http://torch.ch/) - Scientific computing framework with wide support for machine learning algorithms, used by Facebook, Google, and more.
- [lhf's Lua Tools](http://webserver2.tecgraf.puc-rio.br/~lhf/ftp/lua/) - Assorted libraries and tools, many math- or data-related.


### Parsing and Serialization
- JSON
  - [lua-cjson](https://github.com/mpx/lua-cjson/) [![GitHub stars](https://img.shields.io/github/stars/mpx/lua-cjson/?style=flat)](https://github.com/mpx/lua-cjson//stargazers) - Blazing fast JSON encoding/decoding implemented in C and exposed to Lua.
  - [luajson](https://github.com/harningt/luajson) [![GitHub stars](https://img.shields.io/github/stars/harningt/luajson?style=flat)](https://github.com/harningt/luajson/stargazers) - JSON encoder/decoder implemented in Lua on top of LPeg.
  - [dkjson](http://dkolf.de/src/dkjson-lua.fsl/home) - JSON encoder/decoder implemented in pure Lua.
  - [json.lua](https://github.com/rxi/json.lua) [![GitHub stars](https://img.shields.io/github/stars/rxi/json.lua?style=flat)](https://github.com/rxi/json.lua/stargazers) - A fast and tiny JSON library in pure Lua.
- XML
  - [LuaExpat](https://matthewwild.co.uk/projects/luaexpat/) - SAX XML parser via binding to the Expat library.
  - [SLAXML](https://github.com/Phrogz/SLAXML) [![GitHub stars](https://img.shields.io/github/stars/Phrogz/SLAXML?style=flat)](https://github.com/Phrogz/SLAXML/stargazers) - Pure Lua SAX-like streaming XML parser.
- MessagePack
  - [lua-MessagePack](https://github.com/fperrad/lua-MessagePack) [![GitHub stars](https://img.shields.io/github/stars/fperrad/lua-MessagePack?style=flat)](https://github.com/fperrad/lua-MessagePack/stargazers) - Pure Lua implementation of MessagePack.
  - [lua-cmsgpack](https://github.com/antirez/lua-cmsgpack) [![GitHub stars](https://img.shields.io/github/stars/antirez/lua-cmsgpack?style=flat)](https://github.com/antirez/lua-cmsgpack/stargazers) - A MessagePack C implementation with Lua bindings, as used by Redis.=
- LPeg
  - [LPeg](http://www.inf.puc-rio.br/~roberto/lpeg/) - A pattern-matching library for Lua, based on Parsing Expression Grammars.
  - [lpeg_patterns](https://github.com/daurnimator/lpeg_patterns) [![GitHub stars](https://img.shields.io/github/stars/daurnimator/lpeg_patterns?style=flat)](https://github.com/daurnimator/lpeg_patterns/stargazers) - A collection of LPeg patterns.
  - [LuLPeg](https://github.com/pygy/LuLPeg) [![GitHub stars](https://img.shields.io/github/stars/pygy/LuLPeg?style=flat)](https://github.com/pygy/LuLPeg/stargazers) - A pure Lua implementation of LPeg v0.12.
  - [LPegLJ](https://github.com/sacek/LPegLJ) [![GitHub stars](https://img.shields.io/github/stars/sacek/LPegLJ?style=flat)](https://github.com/sacek/LPegLJ/stargazers) - A pure LuaJIT implementation of LPeg v1.0.
  - [LPegLabel](https://github.com/sqmedeiros/lpeglabel) [![GitHub stars](https://img.shields.io/github/stars/sqmedeiros/lpeglabel?style=flat)](https://github.com/sqmedeiros/lpeglabel/stargazers) - An extension of LPeg adding support for labeled failures.
- [lyaml](https://github.com/gvvaughan/lyaml) [![GitHub stars](https://img.shields.io/github/stars/gvvaughan/lyaml?style=flat)](https://github.com/gvvaughan/lyaml/stargazers) - YAML encoding/decoding via binding to LibYAML.
- [lunamark](https://github.com/jgm/lunamark) [![GitHub stars](https://img.shields.io/github/stars/jgm/lunamark?style=flat)](https://github.com/jgm/lunamark/stargazers) - Converts Markdown to other textual formats including HTML and LaTeX. Uses LPeg for fast parsing.
- [LXSH](https://github.com/xolox/lua-lxsh) [![GitHub stars](https://img.shields.io/github/stars/xolox/lua-lxsh?style=flat)](https://github.com/xolox/lua-lxsh/stargazers) - A collection of lexers and syntax highlighters written with LPeg.
- [lua-pb](https://github.com/Neopallium/lua-pb) [![GitHub stars](https://img.shields.io/github/stars/Neopallium/lua-pb?style=flat)](https://github.com/Neopallium/lua-pb/stargazers) - Protocol Buffers implementation.


### Humanize
- [i18n.lua](https://github.com/kikito/i18n.lua) [![GitHub stars](https://img.shields.io/github/stars/kikito/i18n.lua?style=flat)](https://github.com/kikito/i18n.lua/stargazers) - Internationalization library with locales, formatting, and pluralization.
- [inspect.lua](https://github.com/kikito/inspect.lua) [![GitHub stars](https://img.shields.io/github/stars/kikito/inspect.lua?style=flat)](https://github.com/kikito/inspect.lua/stargazers) - Human-readable representation of Lua tables.
- [serpent](https://github.com/pkulchenko/serpent) [![GitHub stars](https://img.shields.io/github/stars/pkulchenko/serpent?style=flat)](https://github.com/pkulchenko/serpent/stargazers) - Serializer and pretty printer.
- [Ser](https://github.com/gvx/Ser) [![GitHub stars](https://img.shields.io/github/stars/gvx/Ser?style=flat)](https://github.com/gvx/Ser/stargazers) - Dead simple serializer with good performance.
- [say](https://github.com/Olivine-Labs/say) [![GitHub stars](https://img.shields.io/github/stars/Olivine-Labs/say?style=flat)](https://github.com/Olivine-Labs/say/stargazers) - Simple string key-value store for i18n.


### Compression
- [lua-zlib](https://github.com/brimworks/lua-zlib) [![GitHub stars](https://img.shields.io/github/stars/brimworks/lua-zlib?style=flat)](https://github.com/brimworks/lua-zlib/stargazers) - Simple streaming interface to zlib for gzip/gunzip.
- [lua-zip](https://github.com/brimworks/lua-zip) [![GitHub stars](https://img.shields.io/github/stars/brimworks/lua-zip?style=flat)](https://github.com/brimworks/lua-zip/stargazers) - Lua binding to libzip. Reads and writes zip files.


### Cryptography
- [LuaCrypto](https://github.com/mkottman/luacrypto) [![GitHub stars](https://img.shields.io/github/stars/mkottman/luacrypto?style=flat)](https://github.com/mkottman/luacrypto/stargazers) - Lua bindings to OpenSSL.
- [lua-lockbox](https://github.com/somesocks/lua-lockbox) [![GitHub stars](https://img.shields.io/github/stars/somesocks/lua-lockbox?style=flat)](https://github.com/somesocks/lua-lockbox/stargazers) - A collection of cryptographic primitives written in pure Lua.
- [luatweetnacl](https://github.com/philanc/luatweetnacl) [![GitHub stars](https://img.shields.io/github/stars/philanc/luatweetnacl?style=flat)](https://github.com/philanc/luatweetnacl/stargazers) - Bindings to tweetnacl, modern high-security cryptographic library.
- [luaossl](https://github.com/wahern/luaossl) [![GitHub stars](https://img.shields.io/github/stars/wahern/luaossl?style=flat)](https://github.com/wahern/luaossl/stargazers) - "Most comprehensive OpenSSL module in the Lua universe" - used by lapis, kong, and lua-http.


### Network
- [LuaSocket](https://github.com/diegonehab/luasocket) [![GitHub stars](https://img.shields.io/github/stars/diegonehab/luasocket?style=flat)](https://github.com/diegonehab/luasocket/stargazers) - Networking extension which provides a socket API for TCP and UDP, and implements HTTP, FTP, and SMTP.
- [lua-websockets](https://github.com/lipp/lua-websockets) [![GitHub stars](https://img.shields.io/github/stars/lipp/lua-websockets?style=flat)](https://github.com/lipp/lua-websockets/stargazers) - WebSocket client and server modules. Webserver-agnostic, implemented in Lua on top of LuaSocket.
- [lua-cURLv3](https://github.com/Lua-cURL/Lua-cURLv3) [![GitHub stars](https://img.shields.io/github/stars/Lua-cURL/Lua-cURLv3?style=flat)](https://github.com/Lua-cURL/Lua-cURLv3/stargazers) - Lua binding to libcurl.
- [lua-http](https://github.com/daurnimator/lua-http) [![GitHub stars](https://img.shields.io/github/stars/daurnimator/lua-http?style=flat)](https://github.com/daurnimator/lua-http/stargazers) - Asynchronous HTTP and WebSocket library with client and server APIs, TLS, and HTTP/2; based on cqueues.


### Data Stores
- [LuaSQL](http://keplerproject.github.io/luasql/) - Simple interface for connecting to ODBC, ADO, Oracle, MySQL, SQLite and PostgreSQL.
- [pgmoon](https://github.com/leafo/pgmoon) [![GitHub stars](https://img.shields.io/github/stars/leafo/pgmoon?style=flat)](https://github.com/leafo/pgmoon/stargazers) - Lua PostgreSQL driver for OpenResty, LuaSocket, and cqueues.
- [lua-resty-mysql](https://github.com/openresty/lua-resty-mysql) [![GitHub stars](https://img.shields.io/github/stars/openresty/lua-resty-mysql?style=flat)](https://github.com/openresty/lua-resty-mysql/stargazers) - Lua MySQL driver for OpenResty.
- [lua-resty-cassandra](https://github.com/jbochi/lua-resty-cassandra) [![GitHub stars](https://img.shields.io/github/stars/jbochi/lua-resty-cassandra?style=flat)](https://github.com/jbochi/lua-resty-cassandra/stargazers) - Lua Cassandra client driver for OpenResty and others.
- Redis
  - [redis-lua](https://github.com/nrk/redis-lua) [![GitHub stars](https://img.shields.io/github/stars/nrk/redis-lua?style=flat)](https://github.com/nrk/redis-lua/stargazers) - Pure Lua client library for Redis.
  - [lua-resty-redis](https://github.com/openresty/lua-resty-redis) [![GitHub stars](https://img.shields.io/github/stars/openresty/lua-resty-redis?style=flat)](https://github.com/openresty/lua-resty-redis/stargazers) - Lua Redis client driver for OpenResty.
  - [lredis](https://github.com/daurnimator/lredis) [![GitHub stars](https://img.shields.io/github/stars/daurnimator/lredis?style=flat)](https://github.com/daurnimator/lredis/stargazers) - Asynchronous Redis client with pipelining and Pub/Sub support; based on cqueues.


### Message Brokers
- [lua-zmq](https://github.com/Neopallium/lua-zmq) [![GitHub stars](https://img.shields.io/github/stars/Neopallium/lua-zmq?style=flat)](https://github.com/Neopallium/lua-zmq/stargazers) - Lua bindings to ZeroMQ.
- [lzmq](https://github.com/zeromq/lzmq) [![GitHub stars](https://img.shields.io/github/stars/zeromq/lzmq?style=flat)](https://github.com/zeromq/lzmq/stargazers) - A newer Lua binding to ZeroMQ.
- [lua-resty-kafka](https://github.com/doujiang24/lua-resty-kafka) [![GitHub stars](https://img.shields.io/github/stars/doujiang24/lua-resty-kafka?style=flat)](https://github.com/doujiang24/lua-resty-kafka/stargazers) - Kafka client driver based on OpenResty cosockets.
- [lua-resty-rabbitmqstomp](https://github.com/wingify/lua-resty-rabbitmqstomp) [![GitHub stars](https://img.shields.io/github/stars/wingify/lua-resty-rabbitmqstomp?style=flat)](https://github.com/wingify/lua-resty-rabbitmqstomp/stargazers) - RabbitMQ client library based on OpenResty cosockets.


### Testing
- [busted](http://olivinelabs.com/busted/) - BDD-style unit testing framework with great docs and Moonscript support.
- [telescope](https://github.com/norman/telescope) [![GitHub stars](https://img.shields.io/github/stars/norman/telescope?style=flat)](https://github.com/norman/telescope/stargazers) - Flexible and highly customizable testing library.
- [luassert](https://github.com/Olivine-Labs/luassert) [![GitHub stars](https://img.shields.io/github/stars/Olivine-Labs/luassert?style=flat)](https://github.com/Olivine-Labs/luassert/stargazers) - Assertion library extending Lua's built-in assertions.
- [lust](https://github.com/bjornbytes/lust) [![GitHub stars](https://img.shields.io/github/stars/bjornbytes/lust?style=flat)](https://github.com/bjornbytes/lust/stargazers) - Minimal test framework.


### Foreign Function Interfaces
- [LuaJIT FFI](http://luajit.org/ext_ffi.html) - LuaJIT's mechanism for calling external C functions and using C data structures from pure Lua code.
- [luaffi](https://github.com/jmckaskill/luaffi) [![GitHub stars](https://img.shields.io/github/stars/jmckaskill/luaffi?style=flat)](https://github.com/jmckaskill/luaffi/stargazers) - Standalone FFI library, compatible with the LuaJIT FFI interface.


### Analysis Tools and ASTs
- [luadec51](https://github.com/sztupy/luadec51) [![GitHub stars](https://img.shields.io/github/stars/sztupy/luadec51?style=flat)](https://github.com/sztupy/luadec51/stargazers) - Lua Decompiler for Lua version 5.1.
- [luacov](http://keplerproject.github.io/luacov/) - Simple coverage analyzer, used by busted and telescope for checking test coverage.
  - [luacov-coveralls](https://github.com/moteus/luacov-coveralls) [![GitHub stars](https://img.shields.io/github/stars/moteus/luacov-coveralls?style=flat)](https://github.com/moteus/luacov-coveralls/stargazers) - LuaCov reporter for coveralls.io.
- [luacheck](https://github.com/mpeterv/luacheck) [![GitHub stars](https://img.shields.io/github/stars/mpeterv/luacheck?style=flat)](https://github.com/mpeterv/luacheck/stargazers) - Simple static analyzer which detects accidental globals and undefined or shadowed locals.
- [Metalua](https://github.com/fab13n/metalua) [![GitHub stars](https://img.shields.io/github/stars/fab13n/metalua?style=flat)](https://github.com/fab13n/metalua/stargazers) - Pure Lua parser and compiler, used for generating ASTs. A number of other tools make use of the Metalua parser in this way.
- [LuaInspect](https://github.com/davidm/lua-inspect) [![GitHub stars](https://img.shields.io/github/stars/davidm/lua-inspect?style=flat)](https://github.com/davidm/lua-inspect/stargazers) - Lua's most powerful code analysis and linting tool, built on Metalua. Used by ZeroBraneStudio, among others.
- [LuaMinify](https://github.com/stravant/LuaMinify) [![GitHub stars](https://img.shields.io/github/stars/stravant/LuaMinify?style=flat)](https://github.com/stravant/LuaMinify/stargazers) - Minifier which also brings its own static analysis tools, lexer, and parser.
- [Typed Lua](https://github.com/andremm/typedlua) [![GitHub stars](https://img.shields.io/github/stars/andremm/typedlua?style=flat)](https://github.com/andremm/typedlua/stargazers) - A typed superset of Lua that compiles to plain Lua.
- [lua-parser](https://github.com/andremm/lua-parser) [![GitHub stars](https://img.shields.io/github/stars/andremm/lua-parser?style=flat)](https://github.com/andremm/lua-parser/stargazers) - A Lua 5.3 parser written using LPegLabel, with improved error messages.


### Experimental, etc
- [punchdrunk.js](https://github.com/TannerRogalsky/punchdrunk) [![GitHub stars](https://img.shields.io/github/stars/TannerRogalsky/punchdrunk?style=flat)](https://github.com/TannerRogalsky/punchdrunk/stargazers) - Moonshine + LÖVE API reimplementation = run LÖVE games in the browser.
- [luvit](https://github.com/luvit/luvit) [![GitHub stars](https://img.shields.io/github/stars/luvit/luvit?style=flat)](https://github.com/luvit/luvit/stargazers) - Node.js's underlying architecture (libUV) with Lua on top instead of JavaScript.
- [graphql-lua](https://github.com/bjornbytes/graphql-lua) [![GitHub stars](https://img.shields.io/github/stars/bjornbytes/graphql-lua?style=flat)](https://github.com/bjornbytes/graphql-lua/stargazers) - Lua implementation of [GraphQL](http://graphql.org/).


### Scriptable by Lua
- [luakit](https://luakit.github.io/luakit/) - Fast, small, webkit based browser framework extensible by Lua.
- [Hammerspoon](http://www.hammerspoon.org) - A powerful, extensible OS X automation tool. A community-maintained fork of [Mjolnir](http://www.mjolnir.io/).
- [kpie](https://github.com/skx/kpie) [![GitHub stars](https://img.shields.io/github/stars/skx/kpie?style=flat)](https://github.com/skx/kpie/stargazers) - A scripting utility to juggle windows.
- [lumail](https://lumail.org/) - A console-based mail client, with extensive scripting capabilities.
- [AwesomeWM](https://awesomewm.org/) - A highly configurable and extensible window manager for X, scripted and configured by Lua.
- [Textadept](https://foicica.com/textadept/) - Extremely lightweight, customizable, cross-platform editor, written (mostly) in (and scripted by) Lua.
- [KoReader](https://github.com/koreader/koreader) [![GitHub stars](https://img.shields.io/github/stars/koreader/koreader?style=flat)](https://github.com/koreader/koreader/stargazers) - An ebook reader application supports PDF, DJVU, EPUB, FB2 and much more, running on Kindle, Kobo, PocketBook and Android devices.


### Miscellaneous
- [MoonScript](http://moonscript.org/) - Moonscript is a dynamic scripting language that compiles to Lua. It reduces verbosity and provides a rich set of features like comprehensions and classes. Its author calls it 'CoffeeScript for Lua'.
- [sitegen](http://leafo.net/sitegen/) - A static site generator which uses MoonScript and supports HTML and Markdown, page grouping, and plugins.


## Resources

### Community
- [lua-l](http://www.lua.org/lua-l.html) - The official Lua mailing list, and one of the focal points of the Lua community.
- [Lua.Space](http://lua.space/) - The Lua community blog.
- [Lua Users Foundation](https://github.com/lua-users-foundation) [![GitHub stars](https://img.shields.io/github/stars/lua-users-foundation?style=flat)](https://github.com/lua-users-foundation/stargazers) - An association of individuals with the mission of supporting and promoting Lua and its community and ecosystems.
- [lua-users.org](http://lua-users.org/) - A site for and by users of Lua, featuring an IRC channel, a web archive of lua-l, and a large wiki.
- Conferences/Meetups
  - [Lua Workshop](https://www.lua.org/community.html#workshop) - Annual 2-day meeting of the Lua community, in rotating locations.
  - [Lua Conf](http://luaconf.com/) - Annual 1-day Lua conference in Brazil.
  - [FOSDEM](https://fosdem.org/) - Annual 2-day gathering of F/OSS developers in Brussels which sometimes has a "Lua devroom".


### References
- [Reference Manual](http://www.lua.org/manual/5.3/) - The official definition of the Lua language.
- [lua-users wiki](http://lua-users.org/wiki/) - A large community-maintained collection of Lua information and resources, supplementing the official website.
- [Lua Unofficial FAQ](http://www.luafaq.org/) - Answers all sorts of Lua-related questions, including many of the form 'How to ___?'.


### Glossaries
- [Lua 5.3 Glossary](https://rawgit.com/dlaurie/lua-notes/master/glossary.html) - A glossary of some essential Lua terms.


### Style Guides
- [Lua-users style guide](http://lua-users.org/wiki/LuaStyleGuide) - A general, high-level style guide; unopinionated, easily agreed on.
- [Olivine style guide](https://github.com/Olivine-Labs/lua-style-guide) [![GitHub stars](https://img.shields.io/github/stars/Olivine-Labs/lua-style-guide?style=flat)](https://github.com/Olivine-Labs/lua-style-guide/stargazers) - A more opinionated and specific, and therefore more rigorous, guide.


### Tutorials
- [Lua Crash Course](http://www.coppeliarobotics.com/helpFiles/en/luaCrashCourse.htm) - Short crash course readover, or reference for when you forget the basics.
- [Learn Lua in 15 Minutes](http://tylerneylon.com/a/learn-lua/) - A well-commented example file which covers the basics.
- [Learning Lua from JS](http://phrogz.net/lua/LearningLua_FromJS.html) - An overview of the similarities and differences between Lua and JS; a great start for JavaScript folks looking to pick up Lua.
- [lua-users tutorial](http://lua-users.org/wiki/LuaTutorial) - In-depth collection of tutorials aimed at newcomers.
- [Lua Missions](https://github.com/kikito/lua_missions) [![GitHub stars](https://img.shields.io/github/stars/kikito/lua_missions?style=flat)](https://github.com/kikito/lua_missions/stargazers) - A series of 'Missions' to work through which are designed to teach aspects of Lua along the way.
- [Creating an Image Server](http://leafo.net/posts/creating_an_image_server.html) - Walks through setting up and using OpenResty to build a simple image processing server; a great starting point for playing with OpenResty.


### Articles
- [Embedding Lua in C](https://debian-administration.org/article/264/Embedding_a_scripting_language_inside_your_C/C_code) - An introductory walkthrough of embedding Lua in a C program. A bit dated, but still a great walkthrough.
- [Lua: Good, bad, and ugly parts](http://notebook.kulchenko.com/programming/lua-good-different-bad-and-ugly-parts) - A thorough summary of the good, different, bad, and ugly aspects of Lua, including many subtle quirks, by the author of ZeroBraneStudio.
- [Lua states, libraries, coroutines and memory](http://www.thijsschreijer.nl/blog/?p=693) - Diagrams and explains some more advanced concepts of the Lua VM, particularly when interfacing with C.


### Talks & Slides
- [Roberto's Talks](http://www.inf.puc-rio.br/~roberto/talks/index.html) - History of talks given by Lua's chief architect, with slides for each.
- [Lua Workshop Talks](http://www.lua.org/wshop14.html#abstracts) - High-quality talks are given at each ~annual Lua Workshop, and a history of them is online, slides included.


### Books
- [Programming in Lua](http://www.lua.org/pil/) - The authoritative intro to all aspects of Lua programming, written by Lua's chief architect. Three editions released; first edition available online.
- [Lua Quick Reference](https://foicica.com/lua/) - A quick reference on how to program in and embed Lua 5.1 through 5.3, by the creator of Textadept.
- [Programming Gems](http://www.lua.org/gems/) - A collection of articles covering existing wisdom and practices on programming well in Lua, in a broad variety of use cases.
- [Lua Programming](https://en.wikibooks.org/wiki/Lua_Programming) - A shorter overview of the language, up to date for Lua 5.2, and available online.


### Other Lists
- [awesome-resty](https://github.com/bungle/awesome-resty) [![GitHub stars](https://img.shields.io/github/stars/bungle/awesome-resty?style=flat)](https://github.com/bungle/awesome-resty/stargazers) - A list like this one, but focused on OpenResty.
- [awesome-love2d](https://github.com/love2d-community/awesome-love2d) [![GitHub stars](https://img.shields.io/github/stars/love2d-community/awesome-love2d?style=flat)](https://github.com/love2d-community/awesome-love2d/stargazers) - A list like this one, but focused on game dev and the LÖVE platform.
- [Where Lua is Used](https://sites.google.com/site/marbux/home/where-lua-is-used) - A comprehensive list of stand-alone programs written in or extensible using Lua.


## Contribute

Contributions welcome and wanted! Read the [contribution guidelines](contributing.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Lewis Ellis has waived all copyright and related or neighboring rights to this work.
