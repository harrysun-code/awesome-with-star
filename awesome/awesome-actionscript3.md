# ActionScript 3

[![GitHub stars](https://img.shields.io/github/stars/robinrodricks/awesome-actionscript3?style=flat)](https://github.com/robinrodricks/awesome-actionscript3/stargazers)

[<img src="https://rawgit.com/hgupta9/awesome-actionscript3/master/AS3_AIR.png" align="right" width="150">](https://www.adobe.com/products/air.html)

# Awesome ActionScript 3 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome libraries and components for ActionScript 3 and Adobe AIR.

[Adobe AIR](https://en.wikipedia.org/wiki/Adobe_AIR) provides a single set of APIs to build cross-platform desktop/mobile applications and games. [ActionScript 3](https://en.wikipedia.org/wiki/ActionScript) is the programming language for AIR. Powerful native functionality such as file system, SQLite, sensors are included by default. To add missing functionality, you can build ANEs (Air Native Extensions) coded in the native language (eg VC++ for Windows, Java for Android, Swift/Objective-C for iOS). To build mobile apps/games with GPU-rendered graphics, use the [Starling](https://gamua.com/starling/) framework and optionally the [Feathers UI](https://feathersui.com/). Adobe AIR is very popular in the mobile gaming space.

Contributions welcome. To add a useful project simply create an [Issue](https://github.com/hgupta9/awesome-actionscript3/issues) [![GitHub stars](https://img.shields.io/github/stars/hgupta9/awesome-actionscript3/issues?style=flat)](https://github.com/hgupta9/awesome-actionscript3/issues/stargazers).

## Contents

* [Development Tools](#development-tools)
* [Frameworks](#frameworks)
* [User Interface](#user-interface)
* [Multimedia](#multimedia)
* [Database](#database)
* [File Formats](#file-formats)
* [Networking](#networking)
* [Utilities](#utilities)
* [Runtimes](#runtimes)
* [AIR Native Extensions](#air-native-extensions)
	

## Development Tools
*This section includes commercial tools as well as free/open source tools.*

#### Code Editors
* [FlashDevelop](http://flashdevelop.org/) - Premiere free & open-source IDE for AS3 & AIR, with code completion, debugging, and more.
* [Powerflasher FDT](http://fdt.powerflasher.com/) - Commercial IDE built on the Eclipse platform for development of Adobe Flash/AIR content.
* [Adobe Flash Builder](https://www.adobe.com/products/flash-builder.html) - Commercial IDE for building applications on the Flex framework (with advanced debugging tools).
* [Moonshine IDE](http://moonshine-ide.com/) - Moonshine is a free and open source middleweight IDE built with ActionScript 3 for ActionScript 3, Apache Flex®, Apache FlexJS® and Feathers development with Cloud and Desktop support.
* [IntelliJ IDEA](https://www.jetbrains.com/help/idea/building-actionscript-and-flex-applications.html) - Commercial IDE that supports many different languages including AS3.
* [Visual Studio Code](https://as3mxml.com/) - An AS3 & MXML language extension for Visual Studio Code. Runs on Windows, macOS, and Linux.

#### Live Debuggers
* [Adobe Scout](https://www.adobe.com/products/scout.html) - Advanced visual profiling and debugging tool for AIR apps & games (supports Stage3D).
* [De-Monster Debugger](https://github.com/MrTact/monsterdebugger) [![GitHub stars](https://img.shields.io/github/stars/MrTact/monsterdebugger?style=flat)](https://github.com/MrTact/monsterdebugger/stargazers) - Advanced tool to debug graphics and data from a live AIR application.
* [De-Monster Debugger (Starling)](https://github.com/joshtynjala/monsterdebugger-client-starling) [![GitHub stars](https://img.shields.io/github/stars/joshtynjala/monsterdebugger-client-starling?style=flat)](https://github.com/joshtynjala/monsterdebugger-client-starling/stargazers) - Fork of De-Monster Debugger with support for Starling Framework.

#### Asset Creators
* [Adobe Animate CC](https://www.adobe.com/products/animate.html) - Premiere vector graphics and animation toolset for vector/spritesheet creation.
* [TILED Map Editor](http://www.mapeditor.org/) - Flexible tile map editor compatible with various AS3 game engines.
* [FlashMovieClipConverter](https://github.com/zenrobin/FlashMovieClipConverter) [![GitHub stars](https://img.shields.io/github/stars/zenrobin/FlashMovieClipConverter?style=flat)](https://github.com/zenrobin/FlashMovieClipConverter/stargazers) - Converts a Flash MovieClip to a Starling IAnimatable Sprite.

#### SWF Obfuscators
* [secureSWF](http://www.kindi.com/) - Commercial AS3/AIR obfuscator with renaming, asset encryption and automatic code optimization.
* [irrFuscator](http://www.ambiera.com/irrfuscator/) - Commercial AS3 obfuscator for Flash and Flex SWF files.

#### SWF Inspectors
* [SWFWire](https://github.com/magicalhobo/SWFWire) [![GitHub stars](https://img.shields.io/github/stars/magicalhobo/SWFWire?style=flat)](https://github.com/magicalhobo/SWFWire/stargazers) - Advanced SWF Decompiler, Inspector and Debugger Tools ([website](http://www.swfwire.com/)).
* [Velocity9](https://github.com/velocity9/Inspector) [![GitHub stars](https://img.shields.io/github/stars/velocity9/Inspector?style=flat)](https://github.com/velocity9/Inspector/stargazers) - Basic SWF Inspector.

#### SWF Decompilers
* [AS3Sorcerer](http://www.as3sorcerer.com/) - Premiere AS3 decompiler with 99% decompilation accuracy (supports SWF/SWC, Alchemy opcodes).
* [Sothink Decompiler](http://www.sothink.com/product/flashdecompiler/) - Advanced decompiler for AS2/AS3 (supports asset extraction and conversion of SWF to FLA/Flex).

#### ANE Dev Tools
* [FreSharp](https://github.com/tuarua/FreSharp) [![GitHub stars](https://img.shields.io/github/stars/tuarua/FreSharp?style=flat)](https://github.com/tuarua/FreSharp/stargazers) - Build ANEs using C# with this C# wrapper for FlashRuntimeExtensions .
* [Swift-IOS-ANE](https://github.com/tuarua/Swift-IOS-ANE) [![GitHub stars](https://img.shields.io/github/stars/tuarua/Swift-IOS-ANE?style=flat)](https://github.com/tuarua/Swift-IOS-ANE/stargazers) - ANE starter kit written in Swift 3 for iOS 10 .

## Frameworks
#### MVC Frameworks

* [PureMVC](https://github.com/PureMVC/puremvc-as3-standard-framework) [![GitHub stars](https://img.shields.io/github/stars/PureMVC/puremvc-as3-standard-framework?style=flat)](https://github.com/PureMVC/puremvc-as3-standard-framework/stargazers) - Industry-standard MVC framework for Flash ([multicore](https://github.com/PureMVC/puremvc-as3-multicore-framework) [![GitHub stars](https://img.shields.io/github/stars/PureMVC/puremvc-as3-multicore-framework?style=flat)](https://github.com/PureMVC/puremvc-as3-multicore-framework/stargazers)).
* [Robotlegs](https://github.com/robotlegs/robotlegs-framework) [![GitHub stars](https://img.shields.io/github/stars/robotlegs/robotlegs-framework?style=flat)](https://github.com/robotlegs/robotlegs-framework/stargazers) - Dependency injection, module/view/command management framework for Flash.
* [Hummingbird](https://github.com/flashapi/hummingbird) [![GitHub stars](https://img.shields.io/github/stars/flashapi/hummingbird?style=flat)](https://github.com/flashapi/hummingbird/stargazers) - Build and deploy robust MVC applications for AS3, Mobile and the Starling Framework.
* [Apollo](https://github.com/LaurentZuijdwijk/Apollo) [![GitHub stars](https://img.shields.io/github/stars/LaurentZuijdwijk/Apollo?style=flat)](https://github.com/LaurentZuijdwijk/Apollo/stargazers) - Dependency injection and messaging framework, which can be used as the basis for MVC projects.
* [Somacore](https://github.com/soundstep/somacore_framework) [![GitHub stars](https://img.shields.io/github/stars/soundstep/somacore_framework?style=flat)](https://github.com/soundstep/somacore_framework/stargazers) - Lightweight event-based AS3 MVC framework.
* [Kote](https://github.com/whitered/Kote) [![GitHub stars](https://img.shields.io/github/stars/whitered/Kote?style=flat)](https://github.com/whitered/Kote/stargazers) - Fast and lightweight MVC framework that brings together the best of PureMVC and as3-signals.
* [StarlingMVC](https://github.com/CreativeBottle/starlingMVC) [![GitHub stars](https://img.shields.io/github/stars/CreativeBottle/starlingMVC?style=flat)](https://github.com/CreativeBottle/starlingMVC/stargazers) - IOC Framework for Starling based games.

#### UI Frameworks

* [Starling](https://gamua.com/starling/) - High-performance 2D graphics engine built on Stage3D. API identical to Flash API. ([github](https://github.com/Gamua/Starling-Framework) [![GitHub stars](https://img.shields.io/github/stars/Gamua/Starling-Framework?style=flat)](https://github.com/Gamua/Starling-Framework/stargazers), [help](http://wiki.starling-framework.org/start)).
* [Feathers UI](https://feathersui.com/) - User interface components for Starling Framework ([github](https://github.com/BowlerHatLLC/feathers) [![GitHub stars](https://img.shields.io/github/stars/BowlerHatLLC/feathers?style=flat)](https://github.com/BowlerHatLLC/feathers/stargazers), [help](https://feathersui.com/help/index.html)).
* [Flow](https://github.com/artman/Flow) [![GitHub stars](https://img.shields.io/github/stars/artman/Flow?style=flat)](https://github.com/artman/Flow/stargazers) - Layout, effects, data binding and remoting framework to be used instead of Flex.
* [AS3Commons UI](https://github.com/AS3Commons/as3commons-ui) [![GitHub stars](https://img.shields.io/github/stars/AS3Commons/as3commons-ui?style=flat)](https://github.com/AS3Commons/as3commons-ui/stargazers) - Layouting, focus and keyboard management framework.
* [Swiz](https://github.com/swiz/swiz-framework) [![GitHub stars](https://img.shields.io/github/stars/swiz/swiz-framework?style=flat)](https://github.com/swiz/swiz-framework/stargazers) - Brutally simple micro-architecture for creating RIAs with AS3 and Adobe Flex.
* [Hiddenwood](https://github.com/raweden/Project-Hiddenwood) [![GitHub stars](https://img.shields.io/github/stars/raweden/Project-Hiddenwood?style=flat)](https://github.com/raweden/Project-Hiddenwood/stargazers) - User interface library developed for a web app project, written in AS3 and in a MVC pattern.
* [Elastic-Lists](https://github.com/MoritzStefaner/Elastic-Lists) [![GitHub stars](https://img.shields.io/github/stars/MoritzStefaner/Elastic-Lists?style=flat)](https://github.com/MoritzStefaner/Elastic-Lists/stargazers) - Fluid and powerful interface for facet browsing.
* [Apache Flex®](https://flex.apache.org/) - The Apache Flex® SDK is the evolution of the popular Adobe Flex SDK. The Apache Flex® SDK is an application development framework for easily building Flash-based applications for mobile devices, web browsers, and desktop platforms.
* [Apache Royale®](http://royale.apache.org/) - The Apache Royale® project is developing a next-generation of the Apache Flex® SDK. Royale has the goal of allowing applications developed in MXML and ActionScript to not only run in the Flash/AIR runtimes, but also to run natively in the browser without Flash, on mobile devices as a PhoneGap/Cordova application, and in embedded JS environments such as Chromium Embedded Framework. Royale has the potential to allow your MXML and ActionScript code to run in even more places than Flash currently does.

#### Game Frameworks

* [CitrusEngine](http://citrusengine.com/) - Professional-grade game engine built built on Starling & Away3D.
* [StarlingPunk](https://github.com/asaia/StarlingPunk) [![GitHub stars](https://img.shields.io/github/stars/asaia/StarlingPunk?style=flat)](https://github.com/asaia/StarlingPunk/stargazers) - Framework built on Starling to add structure and organization to your game projects.
* [FlashPunk](https://github.com/useflashpunk/FlashPunk) [![GitHub stars](https://img.shields.io/github/stars/useflashpunk/FlashPunk?style=flat)](https://github.com/useflashpunk/FlashPunk/stargazers) - Framework to build 2D games. Provides graphics, events, inputs, animation, etc.
* [Flixel](https://github.com/AdamAtomic/flixel) [![GitHub stars](https://img.shields.io/github/stars/AdamAtomic/flixel?style=flat)](https://github.com/AdamAtomic/flixel/stargazers) - Useful base classes that you can extend to make your own game objects.
* [Tetragon](https://github.com/NothingInteractive/tetragon) [![GitHub stars](https://img.shields.io/github/stars/NothingInteractive/tetragon?style=flat)](https://github.com/NothingInteractive/tetragon/stargazers) - Cross-platform framework to build any kind of game. Provides resource management, debugging facilities, multi-locale support, layered extendability, a game-oriented data structure, and more.
* [Pixelizer](https://github.com/johanp/Pixelizer) [![GitHub stars](https://img.shields.io/github/stars/johanp/Pixelizer?style=flat)](https://github.com/johanp/Pixelizer/stargazers) - Component based game engine to build 2D games. Provides rendering, animation, input, etc.
* [AS3isolib](https://github.com/as3isolib/as3isolib.v1) [![GitHub stars](https://img.shields.io/github/stars/as3isolib/as3isolib.v1?style=flat)](https://github.com/as3isolib/as3isolib.v1/stargazers) - Isometric Library developed to assist in creating isometrically projected games.
* [IsoHill](https://github.com/jadbox/IsoHill-Game-Engine) [![GitHub stars](https://img.shields.io/github/stars/jadbox/IsoHill-Game-Engine?style=flat)](https://github.com/jadbox/IsoHill-Game-Engine/stargazers) - GPU-based Isometric engine built on Starling, with TILED map parser, layers, etc ([website](http://www.isohill.com/)).
* [YCanvas](https://github.com/jozefchutka/YCanvas) [![GitHub stars](https://img.shields.io/github/stars/jozefchutka/YCanvas?style=flat)](https://github.com/jozefchutka/YCanvas/stargazers) - High-performance 2D tile renderer and world map renderer.
* [ND2D](https://github.com/lrrrs/nd2d) [![GitHub stars](https://img.shields.io/github/stars/lrrrs/nd2d?style=flat)](https://github.com/lrrrs/nd2d/stargazers) - GPU-accelerated 2D game engine using Stage3D ([ND2Dx](https://github.com/NoRabbit/ND2Dx) [![GitHub stars](https://img.shields.io/github/stars/NoRabbit/ND2Dx?style=flat)](https://github.com/NoRabbit/ND2Dx/stargazers)).
* [Nexus](https://github.com/tversteeg/Nexus) [![GitHub stars](https://img.shields.io/github/stars/tversteeg/Nexus?style=flat)](https://github.com/tversteeg/Nexus/stargazers) - GPU-accelerated 2D game engine using Stage3D.

#### 3D Frameworks

* [AwayBuilder](http://awaytools.com/awaybuilder/) - Visual workflow tool to import, optimise and bake 3D assets from a variety of sources.
* [Away3D](https://github.com/away3d/away3d-core-fp11) [![GitHub stars](https://img.shields.io/github/stars/away3d/away3d-core-fp11?style=flat)](https://github.com/away3d/away3d-core-fp11/stargazers) - Open-source GPU-accelerated 3D engine for Flash Player 11+ ([examples](https://github.com/away3d/away3d-examples-fp11) [![GitHub stars](https://img.shields.io/github/stars/away3d/away3d-examples-fp11?style=flat)](https://github.com/away3d/away3d-examples-fp11/stargazers)).
* [Away3D OpenFL](https://github.com/away3d/away3d-core-openfl) [![GitHub stars](https://img.shields.io/github/stars/away3d/away3d-core-openfl?style=flat)](https://github.com/away3d/away3d-core-openfl/stargazers) - Away3D for Neko, HTML5 and native CPP. ([examples](https://github.com/away3d/away3d-examples-openfl) [![GitHub stars](https://img.shields.io/github/stars/away3d/away3d-examples-openfl?style=flat)](https://github.com/away3d/away3d-examples-openfl/stargazers)).
* [AwayPhysics FP11](https://github.com/away3d/awayphysics-core-fp11) [![GitHub stars](https://img.shields.io/github/stars/away3d/awayphysics-core-fp11?style=flat)](https://github.com/away3d/awayphysics-core-fp11/stargazers) - Away Physics - 3D physics library for the Away3D FP 11 ([examples](https://github.com/away3d/awayphysics-examples-fp11) [![GitHub stars](https://img.shields.io/github/stars/away3d/awayphysics-examples-fp11?style=flat)](https://github.com/away3d/awayphysics-examples-fp11/stargazers)).
* [Alternativa3D](https://github.com/AlternativaPlatform/Alternativa3D) [![GitHub stars](https://img.shields.io/github/stars/AlternativaPlatform/Alternativa3D?style=flat)](https://github.com/AlternativaPlatform/Alternativa3D/stargazers) - Alternativa3D GPU accelerated 3D engine ([examples](https://github.com/AlternativaPlatform/Alternativa3DExamples) [![GitHub stars](https://img.shields.io/github/stars/AlternativaPlatform/Alternativa3DExamples?style=flat)](https://github.com/AlternativaPlatform/Alternativa3DExamples/stargazers)).
* [Flare3D](http://flare3d.com/) - Commercial 3D platform with high-performance engine and Level-editor IDE.
* [Zen3D](https://github.com/hgupta9/Zen3D) [![GitHub stars](https://img.shields.io/github/stars/hgupta9/Zen3D?style=flat)](https://github.com/hgupta9/Zen3D/stargazers) - High-performance 3D engine for Adobe Flash & AIR (GPU based).

#### Animation

* [GreenSock GSAP](https://greensock.com/gsap-as) - The industry-standard animation library for Flash (TweenLite, TweenMax) ([github](https://github.com/greensock/GreenSock-AS3) [![GitHub stars](https://img.shields.io/github/stars/greensock/GreenSock-AS3?style=flat)](https://github.com/greensock/GreenSock-AS3/stargazers)).
* [GTween](http://gskinner.com/libraries/gtween/) - Small but robust library for programmatic tweening, animation, and transitions.
* [DragonBones](http://dragonbones.github.io/) - High-speed skeletal animation using Starling, and tools to export animations from Flash Pro.
* [FlashEff2](http://www.flasheff.com/) - Premiere programmatic animation library with 100+ transitions and text effects.
* [FlashEffNano](http://www.flasheffnano.com/) - FlashEff transition library optimized for mobile devices, with 20+ transitions in 750 styles.
* [StarlingGAFPlayer](https://github.com/zenrobin/StarlingGAFPlayer) [![GitHub stars](https://img.shields.io/github/stars/zenrobin/StarlingGAFPlayer?style=flat)](https://github.com/zenrobin/StarlingGAFPlayer/stargazers) - Play back GAF animations using Starling (animations authored in Flash Pro).

#### Signals

* [AS3-signals](https://github.com/robertpenner/as3-signals) [![GitHub stars](https://img.shields.io/github/stars/robertpenner/as3-signals?style=flat)](https://github.com/robertpenner/as3-signals/stargazers) - New approach for AS3 events inspired by C# events and signals/slots in Qt.
* [react-as3](https://github.com/tconkling/react-as3) [![GitHub stars](https://img.shields.io/github/stars/tconkling/react-as3?style=flat)](https://github.com/tconkling/react-as3/stargazers) - Signals/slots and functional reactive programming library.
* [Signaller](https://github.com/whitered/Signaller) [![GitHub stars](https://img.shields.io/github/stars/whitered/Signaller?style=flat)](https://github.com/whitered/Signaller/stargazers) - Signals implementation with restricted rights for dispatching.
* [Fa-as3](https://github.com/fabrikagency/fa-as3) [![GitHub stars](https://img.shields.io/github/stars/fabrikagency/fa-as3?style=flat)](https://github.com/fabrikagency/fa-as3/stargazers) - Write less, do more framework, modeled like jQuery.

#### Functional

* [AS3FP](https://github.com/jadbox/AS3FP) [![GitHub stars](https://img.shields.io/github/stars/jadbox/AS3FP?style=flat)](https://github.com/jadbox/AS3FP/stargazers) - Collection of functional idioms based on Haskell and Coffeescript.
* [Raix](https://github.com/richardszalay/raix) [![GitHub stars](https://img.shields.io/github/stars/richardszalay/raix?style=flat)](https://github.com/richardszalay/raix/stargazers) - Reactive And Interactive eXtensions simplifies working with interactive data (arrays) or reactive data (events).
* [Fxp-as3](https://github.com/j3k0/fxp-as3) [![GitHub stars](https://img.shields.io/github/stars/j3k0/fxp-as3?style=flat)](https://github.com/j3k0/fxp-as3/stargazers) - Functional library inspired by the "mostly adequate guide".

#### Unit Testing

* [AS3unit](https://github.com/Hoten/as3unit) [![GitHub stars](https://img.shields.io/github/stars/Hoten/as3unit?style=flat)](https://github.com/Hoten/as3unit/stargazers) - Unit testing framework for ActionScript 3.
* [hamcrest-as3](https://github.com/drewbourne/hamcrest-as3) [![GitHub stars](https://img.shields.io/github/stars/drewbourne/hamcrest-as3?style=flat)](https://github.com/drewbourne/hamcrest-as3/stargazers) - Matcher objects allowing 'match' rules to be defined declaratively.
* [expect.as](https://github.com/krzysztof-o/expect.as) [![GitHub stars](https://img.shields.io/github/stars/krzysztof-o/expect.as?style=flat)](https://github.com/krzysztof-o/expect.as/stargazers) - BDD-style assertion library for ActionScript 3.
* [AS3spec](https://github.com/f1337/as3spec) [![GitHub stars](https://img.shields.io/github/stars/f1337/as3spec?style=flat)](https://github.com/f1337/as3spec/stargazers) - Tiny BDD framework for AS3, inspired by Bacon and RSpec.
* [Flexunit](https://github.com/flexunit/flexunit) [![GitHub stars](https://img.shields.io/github/stars/flexunit/flexunit?style=flat)](https://github.com/flexunit/flexunit/stargazers) - FlexUnit project for Actionscript 3 and Flex projects.
* [ASunit](https://github.com/patternpark/asunit) [![GitHub stars](https://img.shields.io/github/stars/patternpark/asunit?style=flat)](https://github.com/patternpark/asunit/stargazers) - The only unit test framework that supports Flash Players 6, 7, 8, 9 and 10.
* [RobotEyes](https://github.com/Stray/RobotEyes) [![GitHub stars](https://img.shields.io/github/stars/Stray/RobotEyes?style=flat)](https://github.com/Stray/RobotEyes/stargazers) - End-to-end testing for TDD. Hybrid of WindowLicker and Drew Bourne's Mockolate.

## User Interface
#### UI Components

* [MinimalComps](https://github.com/minimalcomps/minimalcomps) [![GitHub stars](https://img.shields.io/github/stars/minimalcomps/minimalcomps?style=flat)](https://github.com/minimalcomps/minimalcomps/stargazers) - Minimal ActionScript 3.0 UI Components for Flash.
* [MadComponents](https://github.com/danfreeman/MadComponents) [![GitHub stars](https://img.shields.io/github/stars/danfreeman/MadComponents?style=flat)](https://github.com/danfreeman/MadComponents/stargazers) - Popular Mobile UI Framework for AS3 / AIR.
* [AsWing](https://github.com/dreamsxin/AsWing) [![GitHub stars](https://img.shields.io/github/stars/dreamsxin/AsWing?style=flat)](https://github.com/dreamsxin/AsWing/stargazers) - Open Source Flash ActionScript GUI framework.
* [GPUI](https://github.com/inspirit/GPUI) [![GitHub stars](https://img.shields.io/github/stars/inspirit/GPUI?style=flat)](https://github.com/inspirit/GPUI/stargazers) - Tiny GUI Library based on Stage3D (GPU).
* [Falcon](https://github.com/HendrixString/Falcon) [![GitHub stars](https://img.shields.io/github/stars/HendrixString/Falcon?style=flat)](https://github.com/HendrixString/Falcon/stargazers) - responsive/flexible mobile ui controls for Feathers.
* [Flex-maps](https://github.com/igorcosta/flex-maps) [![GitHub stars](https://img.shields.io/github/stars/igorcosta/flex-maps?style=flat)](https://github.com/igorcosta/flex-maps/stargazers) - Definitive solution for maps in Apache Flex.
* [FlexBook](https://github.com/blvz/FlexBook) [![GitHub stars](https://img.shields.io/github/stars/blvz/FlexBook?style=flat)](https://github.com/blvz/FlexBook/stargazers) - Awesome Page Flip component for Flex.
* [Flex-Android-Material-Skins](https://github.com/quick6black/flex-Android-Material-Skins) [![GitHub stars](https://img.shields.io/github/stars/quick6black/flex-Android-Material-Skins?style=flat)](https://github.com/quick6black/flex-Android-Material-Skins/stargazers) - Android Material Design skins for Flex Mobile components.

#### Starling Components

* [TabbedApplication](https://github.com/pol2095/Feathers-Extension-Tabbed-Application) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-Tabbed-Application?style=flat)](https://github.com/pol2095/Feathers-Extension-Tabbed-Application/stargazers) - View-based navigation model with swipe to navigate tabs.
* [DataGrid](https://github.com/pol2095/Feathers-Extension-DataGrid) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-DataGrid?style=flat)](https://github.com/pol2095/Feathers-Extension-DataGrid/stargazers) - Displays a datagrid with column headings and smooth scrolling.
* [DataTree](https://github.com/pol2095/Feathers-Extension-Tree) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-Tree?style=flat)](https://github.com/pol2095/Feathers-Extension-Tree/stargazers) - Displays hierarchical data arranged as an expandable tree.
* [Canvas](https://github.com/pol2095/Feathers-Extension-Canvas) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-Canvas?style=flat)](https://github.com/pol2095/Feathers-Extension-Canvas/stargazers) - Supports basic vector drawing functionality.
* [CircleProgress](https://github.com/pol2095/Feathers-Extension-CircleProgress) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-CircleProgress?style=flat)](https://github.com/pol2095/Feathers-Extension-CircleProgress/stargazers) - Displays progress using a radial progressbar.
* [ZoomableControl](https://github.com/pol2095/Feathers-Extension-ZoomableControl) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-ZoomableControl?style=flat)](https://github.com/pol2095/Feathers-Extension-ZoomableControl/stargazers) - Allows a pinch to zoom using the multitouch inputs.
* [Toaster](https://github.com/pol2095/Feathers-Extension-Toaster) [![GitHub stars](https://img.shields.io/github/stars/pol2095/Feathers-Extension-Toaster?style=flat)](https://github.com/pol2095/Feathers-Extension-Toaster/stargazers) - Simple feedback about an operation in a small popup. .
* [Google Maps](https://github.com/ZwickTheGreat/feathers-maps) [![GitHub stars](https://img.shields.io/github/stars/ZwickTheGreat/feathers-maps?style=flat)](https://github.com/ZwickTheGreat/feathers-maps/stargazers) - Google Maps for Starling, optimized for mobile devices.

#### Layout

* [Adobe TLF](https://github.com/apache/flex-tlf) [![GitHub stars](https://img.shields.io/github/stars/apache/flex-tlf?style=flat)](https://github.com/apache/flex-tlf/stargazers) - Adobe/Apache Flex Text Layout Framework (TLF).
* [TinyTLF](https://github.com/joelhooks/tinytlf) [![GitHub stars](https://img.shields.io/github/stars/joelhooks/tinytlf?style=flat)](https://github.com/joelhooks/tinytlf/stargazers) - Versatile text layout framework built on top of the Flash Text Engine for Flash/Flex.
* [TransformManager](https://greensock.com/TransformManager) - By Greensock. Interactive scaling/rotating/moving of DisplayObjects.
* [TransformTool](https://github.com/senocular/TransformTool) [![GitHub stars](https://img.shields.io/github/stars/senocular/TransformTool?style=flat)](https://github.com/senocular/TransformTool/stargazers) - Free Transform Tool (AS, JS) for manipulating objects in 2D space.
* [Argilla-Mosaic](https://github.com/folletto/Argilla-Mosaic) [![GitHub stars](https://img.shields.io/github/stars/folletto/Argilla-Mosaic?style=flat)](https://github.com/folletto/Argilla-Mosaic/stargazers) - Dynamic layout library.
* [xrope](https://github.com/evan-liu/xrope) [![GitHub stars](https://img.shields.io/github/stars/evan-liu/xrope?style=flat)](https://github.com/evan-liu/xrope/stargazers) - Simple layout library for native AS3 display objects.
* [miglayout-as](https://github.com/develar/miglayout-as) [![GitHub stars](https://img.shields.io/github/stars/develar/miglayout-as?style=flat)](https://github.com/develar/miglayout-as/stargazers) - Port of MigLayout, a superbly versatile Flash/Flex/FlashCocoa (SWT/Swing/JavaFX) layout manager.

#### Multi Touch

* [TUIO Client](https://github.com/lagerkoller/tuio-as3) [![GitHub stars](https://img.shields.io/github/stars/lagerkoller/tuio-as3?style=flat)](https://github.com/lagerkoller/tuio-as3/stargazers) - Common framework for multi-touch hardware, supporting TUIO/FLC and TUIO/TCP ([web](http://www.tuio.org/?flash)).
* [Gestouch](https://github.com/fljot/Gestouch) [![GitHub stars](https://img.shields.io/github/stars/fljot/Gestouch?style=flat)](https://github.com/fljot/Gestouch/stargazers) - Multitouch gesture recognition library for building better Natural User Interfaces.
* [Gestures.IO](https://github.com/GesturesIO/gesturesio-as3) [![GitHub stars](https://img.shields.io/github/stars/GesturesIO/gesturesio-as3?style=flat)](https://github.com/GesturesIO/gesturesio-as3/stargazers) - Simplifies the way you create gesture-based Natural Interactions.
* [TouchScript](https://github.com/TouchScript/TouchScript.as3) [![GitHub stars](https://img.shields.io/github/stars/TouchScript/TouchScript.as3?style=flat)](https://github.com/TouchScript/TouchScript.as3/stargazers) - Multitouch framework that makes handling complex gesture interactions on large touch surfaces easier.

#### Game Controllers

* [AS3dpad](https://github.com/duckleg/as3dpad) [![GitHub stars](https://img.shields.io/github/stars/duckleg/as3dpad?style=flat)](https://github.com/duckleg/as3dpad/stargazers) - A virtual touchscreen gamepad designed for Adobe AIR Mobile (Android/iOS).
* [Gamepad](https://github.com/iainlobb/Gamepad) [![GitHub stars](https://img.shields.io/github/stars/iainlobb/Gamepad?style=flat)](https://github.com/iainlobb/Gamepad/stargazers) - Simulates an analog joystick input using the keyboard.
* [Advanced_Joystick](https://github.com/justjoeyuk/Advanced_Joystick) [![GitHub stars](https://img.shields.io/github/stars/justjoeyuk/Advanced_Joystick?style=flat)](https://github.com/justjoeyuk/Advanced_Joystick/stargazers) - Joystick for the Starling Framework, designed for Adobe AIR Mobile.
* [AS3-Controller-Input](https://github.com/arkeus/as3-controller-input) [![GitHub stars](https://img.shields.io/github/stars/arkeus/as3-controller-input?style=flat)](https://github.com/arkeus/as3-controller-input/stargazers) - Interact with Ouya and Xbox360 game controllers from Adobe AIR.

## Multimedia

#### Augmented Reality

* [FLARToolKit](https://github.com/Saqoosha/FLARToolKit) [![GitHub stars](https://img.shields.io/github/stars/Saqoosha/FLARToolKit?style=flat)](https://github.com/Saqoosha/FLARToolKit/stargazers) - AS3 port of the industry standard ARToolkit library, for Flash Player 11. ([website](http://www.libspark.org/wiki/saqoosha/FLARToolKit/en)).
* [FLAREmulator](https://github.com/theflashbum/FLAREmulator) [![GitHub stars](https://img.shields.io/github/stars/theflashbum/FLAREmulator?style=flat)](https://github.com/theflashbum/FLAREmulator/stargazers) - Test AR demos to see what works and what doesn't with or without a webcam.
* [FLARManager](http://words.transmote.com/wp/flarmanager/) - Lightweight framework for building augmented reality apps, using FLARToolkit/flare.tracker/flare.NFT.
* [NyARToolkitAS3](https://github.com/nyatla/NyARToolkitAS3) [![GitHub stars](https://img.shields.io/github/stars/nyatla/NyARToolkitAS3?style=flat)](https://github.com/nyatla/NyARToolkitAS3/stargazers) - NyARToolkit AS3 edition. Marker based Augmented reality library.
* [EZFLAR](https://github.com/tcha-tcho/EZFLAR) [![GitHub stars](https://img.shields.io/github/stars/tcha-tcho/EZFLAR?style=flat)](https://github.com/tcha-tcho/EZFLAR/stargazers) - A little wrapper to ease the way AR works.
* [IN2AR](https://github.com/inspirit/IN2ARSDKExamples) [![GitHub stars](https://img.shields.io/github/stars/inspirit/IN2ARSDKExamples?style=flat)](https://github.com/inspirit/IN2ARSDKExamples/stargazers) - SDK for IN2AR cross-platform Augmented Reality Engine.

#### Data Visualization

* [Axiis](https://github.com/hgupta9/AxiisCharts) [![GitHub stars](https://img.shields.io/github/stars/hgupta9/AxiisCharts?style=flat)](https://github.com/hgupta9/AxiisCharts/stargazers) - Data visualization framework with line, bar, wedge, column, cluster, area, smith and treemap charts.
* [Open Flash Charts](https://sourceforge.net/projects/openflashchart/) - Line charts, Area charts, Bar charts, Pie charts, Scatter charts.
* [Flare](https://github.com/prefuse/Flare) [![GitHub stars](https://img.shields.io/github/stars/prefuse/Flare?style=flat)](https://github.com/prefuse/Flare/stargazers) - charts and graphs, supports data management, visual encoding, animation, and interaction techniques.
* [clearmaps](https://github.com/sunlightlabs/clearmaps) [![GitHub stars](https://img.shields.io/github/stars/sunlightlabs/clearmaps?style=flat)](https://github.com/sunlightlabs/clearmaps/stargazers) - Mapping framework for data visualization.
* [redada](https://github.com/geraldo/redada) [![GitHub stars](https://img.shields.io/github/stars/geraldo/redada?style=flat)](https://github.com/geraldo/redada/stargazers) - Interactive visualization of weighted graphs using GraphML files.
* [Flextreemap](https://github.com/joshtynjala/flextreemap) [![GitHub stars](https://img.shields.io/github/stars/joshtynjala/flextreemap?style=flat)](https://github.com/joshtynjala/flextreemap/stargazers) - TreeMap data visualization component for Adobe Flex.
* [GraphVisualizer](https://github.com/armisael/GraphVisualizer) [![GitHub stars](https://img.shields.io/github/stars/armisael/GraphVisualizer?style=flat)](https://github.com/armisael/GraphVisualizer/stargazers) - A Flex 3 + ActionScript 3 web software to draw dynamic graphcs.
* [Weave](https://github.com/WeaveTeam/Weave) [![GitHub stars](https://img.shields.io/github/stars/WeaveTeam/Weave?style=flat)](https://github.com/WeaveTeam/Weave/stargazers) - Web-based Analysis and Visualization Environment.
* [Social-grid](https://github.com/Instrument/social-grid) [![GitHub stars](https://img.shields.io/github/stars/Instrument/social-grid?style=flat)](https://github.com/Instrument/social-grid/stargazers) - Abstract Grid Visualization for Social Media.

#### Camera

* [CameraDetection](https://github.com/cataclysmicrewind/CameraDetection) [![GitHub stars](https://img.shields.io/github/stars/cataclysmicrewind/CameraDetection?style=flat)](https://github.com/cataclysmicrewind/CameraDetection/stargazers) - Camera detection.
* [Fluocam](https://github.com/Fluocode/Fluocam) [![GitHub stars](https://img.shields.io/github/stars/Fluocode/Fluocam?style=flat)](https://github.com/Fluocode/Fluocam/stargazers) - Virtual camera for Starling applications.
* [WebcamRecorder](https://github.com/Stupeflix/WebcamRecorder) [![GitHub stars](https://img.shields.io/github/stars/Stupeflix/WebcamRecorder?style=flat)](https://github.com/Stupeflix/WebcamRecorder/stargazers) - Chromeless video/audio/still image recording from webcams.
* [FlashyWrappers](https://github.com/rainbowcreatures/FlashyWrappers) [![GitHub stars](https://img.shields.io/github/stars/rainbowcreatures/FlashyWrappers?style=flat)](https://github.com/rainbowcreatures/FlashyWrappers/stargazers) - Recording video from AIR apps on Windows/Android/iOS/OSX.

#### Image

* [Scale9Image](https://github.com/Tibus/Scale9Image) [![GitHub stars](https://img.shields.io/github/stars/Tibus/Scale9Image?style=flat)](https://github.com/Tibus/Scale9Image/stargazers) - Optimized scale9Grid image for starling.
* [ASImageLib](https://github.com/terrynoya/ASImageLib) [![GitHub stars](https://img.shields.io/github/stars/terrynoya/ASImageLib?style=flat)](https://github.com/terrynoya/ASImageLib/stargazers) - BMP/PNG decoder for actionscript.
* [Async-Image-Encoders](https://github.com/LeeBurrows/Async-Image-Encoders) [![GitHub stars](https://img.shields.io/github/stars/LeeBurrows/Async-Image-Encoders?style=flat)](https://github.com/LeeBurrows/Async-Image-Encoders/stargazers) - Asynchronously encode BitmapData objects into image file format.
* [Flip-Planes-AS3](https://github.com/jamesflorentino/Flip-Planes-AS3) [![GitHub stars](https://img.shields.io/github/stars/jamesflorentino/Flip-Planes-AS3?style=flat)](https://github.com/jamesflorentino/Flip-Planes-AS3/stargazers) - Photo slideshow effects.
* [AS3-transitions-lib](https://github.com/foo123/as3-transitions-lib) [![GitHub stars](https://img.shields.io/github/stars/foo123/as3-transitions-lib?style=flat)](https://github.com/foo123/as3-transitions-lib/stargazers) - Image Transitions Library.
* [Inspirit Image](https://github.com/hgupta9/InspiritImage) [![GitHub stars](https://img.shields.io/github/stars/hgupta9/InspiritImage?style=flat)](https://github.com/hgupta9/InspiritImage/stargazers) - FFT, SURF, edge detection, fluid solver, etc.
* [Inspirit GPUImage](https://github.com/inspirit/GPUImage) [![GitHub stars](https://img.shields.io/github/stars/inspirit/GPUImage?style=flat)](https://github.com/inspirit/GPUImage/stargazers) - Framework for GPU-based image processing.
* [AS3potrace](https://github.com/PowerflasherBR/as3potrace) [![GitHub stars](https://img.shields.io/github/stars/PowerflasherBR/as3potrace?style=flat)](https://github.com/PowerflasherBR/as3potrace/stargazers) - POTrace implementation, to trace bitmap images to vector.
* [ATF-Encoder](https://github.com/plepers/ATF-Encoder) [![GitHub stars](https://img.shields.io/github/stars/plepers/ATF-Encoder?style=flat)](https://github.com/plepers/ATF-Encoder/stargazers) - Encode/decode ATF (Adobe Texture Format) files in pure AS3.
* [AS3-klt](https://github.com/motemen/as3-klt) [![GitHub stars](https://img.shields.io/github/stars/motemen/as3-klt?style=flat)](https://github.com/motemen/as3-klt/stargazers) - Kanade-Lucas-Tomasi feature tracker implementation.
* [BlurHash](https://github.com/roipeker/as3-blurhash) [![GitHub stars](https://img.shields.io/github/stars/roipeker/as3-blurhash?style=flat)](https://github.com/roipeker/as3-blurhash/stargazers) - A BlurHash encoder/decoder implementation in ActionScript 3.0..

#### Font

* [Firetype](https://github.com/MaxDidIt/firetype) [![GitHub stars](https://img.shields.io/github/stars/MaxDidIt/firetype?style=flat)](https://github.com/MaxDidIt/firetype/stargazers) - Parse OpenType fonts and render them using Stage3D.
* [BMFontRenderer](https://github.com/bengarney/BMFontRenderer) [![GitHub stars](https://img.shields.io/github/stars/bengarney/BMFontRenderer?style=flat)](https://github.com/bengarney/BMFontRenderer/stargazers) - AS3 renderer for bitmap font data in the BMFont format.
* [HanFont](https://github.com/kyoji2/HanFont) [![GitHub stars](https://img.shields.io/github/stars/kyoji2/HanFont?style=flat)](https://github.com/kyoji2/HanFont/stargazers) - AIR app for Chinese Font Embeding in ActionScript.
* [Ficon.as](https://github.com/dv/Ficon.as) [![GitHub stars](https://img.shields.io/github/stars/dv/Ficon.as?style=flat)](https://github.com/dv/Ficon.as/stargazers) - Library to easily include icon fonts.

#### Particle

* [Flint](https://github.com/richardlord/Flint) [![GitHub stars](https://img.shields.io/github/stars/richardlord/Flint?style=flat)](https://github.com/richardlord/Flint/stargazers) - Particle Engine for Flash and Flex.
* [Desuade Partigen](http://desuade.com/partigen) - Desuade Partigen particle generation system ([github](https://github.com/andrewfitz/desuade) [![GitHub stars](https://img.shields.io/github/stars/andrewfitz/desuade?style=flat)](https://github.com/andrewfitz/desuade/stargazers)).
* [Angulex](https://github.com/cosmindolha/ParticleDesigner) [![GitHub stars](https://img.shields.io/github/stars/cosmindolha/ParticleDesigner?style=flat)](https://github.com/cosmindolha/ParticleDesigner/stargazers) - Particle Designer for the Starling framework (ActionScript 3).
* [SAP](https://github.com/gonchar/SAP) [![GitHub stars](https://img.shields.io/github/stars/gonchar/SAP?style=flat)](https://github.com/gonchar/SAP/stargazers) - Particle System for Starling.
* [Starling-Particles](https://github.com/Gamua/Starling-Extension-Particle-System) [![GitHub stars](https://img.shields.io/github/stars/Gamua/Starling-Extension-Particle-System?style=flat)](https://github.com/Gamua/Starling-Extension-Particle-System/stargazers) - Particle system for the Starling framework, compatible with the "Particle Designer" from 71squared.com.
* [MotionParticleSprite](https://github.com/bjeld/motionparticlesprite) [![GitHub stars](https://img.shields.io/github/stars/bjeld/motionparticlesprite?style=flat)](https://github.com/bjeld/motionparticlesprite/stargazers) - Design motion paths in Flash Pro and use it to guide Starling particles.

#### Panorama Viewer

* [Pantaloons](https://github.com/EyeSee360/Pantaloons) [![GitHub stars](https://img.shields.io/github/stars/EyeSee360/Pantaloons?style=flat)](https://github.com/EyeSee360/Pantaloons/stargazers) - Panoramic viewing in Flash Player.
* [SaladoPlayer](https://github.com/mstandio/SaladoPlayer) [![GitHub stars](https://img.shields.io/github/stars/mstandio/SaladoPlayer?style=flat)](https://github.com/mstandio/SaladoPlayer/stargazers) - Panorama viewer.
* [PanoramicViewer](https://github.com/BrianMehrman/PanoramicViewer) [![GitHub stars](https://img.shields.io/github/stars/BrianMehrman/PanoramicViewer?style=flat)](https://github.com/BrianMehrman/PanoramicViewer/stargazers) - 3D Panoramic Viewer.
* [Sphere_panorama](https://github.com/suzumura-ss/flash_sphere_panorama) [![GitHub stars](https://img.shields.io/github/stars/suzumura-ss/flash_sphere_panorama?style=flat)](https://github.com/suzumura-ss/flash_sphere_panorama/stargazers) - Panorama player with equirectangular texture written in AS3 (Alternativa3D).
* [CuTy](https://github.com/fieldOfView/CuTy) [![GitHub stars](https://img.shields.io/github/stars/fieldOfView/CuTy?style=flat)](https://github.com/fieldOfView/CuTy/stargazers) - QTVR Panorama viewer based on Flash 10.

#### QR Code

* [Zxing AS3](https://github.com/zxing/zxing/tree/c1df162b95e07928afbd4830798cc1408af1ac67/actionscript) [![GitHub stars](https://img.shields.io/github/stars/zxing/zxing/tree/c1df162b95e07928afbd4830798cc1408af1ac67/actionscript?style=flat)](https://github.com/zxing/zxing/tree/c1df162b95e07928afbd4830798cc1408af1ac67/actionscript/stargazers) - QR code detection and generation ([docs](https://zxing.github.io/zxing/)).
* [AS3-qrcode-encoder](https://github.com/jbpin/as3-qrcode-encoder) [![GitHub stars](https://img.shields.io/github/stars/jbpin/as3-qrcode-encoder?style=flat)](https://github.com/jbpin/as3-qrcode-encoder/stargazers) - QR code encoder in as3.
* [qrcode-as](https://github.com/yanbe/qrcode-as) [![GitHub stars](https://img.shields.io/github/stars/yanbe/qrcode-as?style=flat)](https://github.com/yanbe/qrcode-as/stargazers) - QR Code reader which supports webcam on Windows, Mac and Linux.

#### Sound

* [SoundAS](https://github.com/treefortress/SoundAS) [![GitHub stars](https://img.shields.io/github/stars/treefortress/SoundAS?style=flat)](https://github.com/treefortress/SoundAS/stargazers) - Modern & lightweight sound manager for AS3.
* [Standingwave3](https://github.com/maxl0rd/standingwave3) [![GitHub stars](https://img.shields.io/github/stars/maxl0rd/standingwave3?style=flat)](https://github.com/maxl0rd/standingwave3/stargazers) - Dynamic audio library.
* [Standingwave3-addons](https://github.com/charlesclements/standingwave3-addons) [![GitHub stars](https://img.shields.io/github/stars/charlesclements/standingwave3-addons?style=flat)](https://github.com/charlesclements/standingwave3-addons/stargazers) - Addons for SW3.
* [Soundtouch-as3](https://github.com/also/soundtouch-as3) [![GitHub stars](https://img.shields.io/github/stars/also/soundtouch-as3?style=flat)](https://github.com/also/soundtouch-as3/stargazers) - AS3 Port of the SoundTouch Sound Processing Library.
* [SeiON](https://github.com/cardin/SeiON) [![GitHub stars](https://img.shields.io/github/stars/cardin/SeiON?style=flat)](https://github.com/cardin/SeiON/stargazers) - Sound Management Library.
* [AS3-Sound-Manager](https://github.com/GrupoW/as3-Sound-Manager) [![GitHub stars](https://img.shields.io/github/stars/GrupoW/as3-Sound-Manager?style=flat)](https://github.com/GrupoW/as3-Sound-Manager/stargazers)- Upgraded version of the Sound Manager Class from Matt Przybylski.
* [AS3sfxr](https://github.com/SFBTom/as3sfxr) [![GitHub stars](https://img.shields.io/github/stars/SFBTom/as3sfxr?style=flat)](https://github.com/SFBTom/as3sfxr/stargazers) - Port of sfxr from C++ to AS3, using the new sound and file capabilities of Flash Player 10.
* [AS3-audio](https://github.com/singuerinc/as3-audio) [![GitHub stars](https://img.shields.io/github/stars/singuerinc/as3-audio?style=flat)](https://github.com/singuerinc/as3-audio/stargazers) - Audio Management in Actionscript.
* [SiON](https://github.com/keim/SiON) [![GitHub stars](https://img.shields.io/github/stars/keim/SiON?style=flat)](https://github.com/keim/SiON/stargazers) - Flash Software Synthesizer.
* [FlashWavRecorder](https://github.com/michalstocki/FlashWavRecorder) [![GitHub stars](https://img.shields.io/github/stars/michalstocki/FlashWavRecorder?style=flat)](https://github.com/michalstocki/FlashWavRecorder/stargazers) - Recording audio and saving as a WAV.
* [Local-recorder](https://github.com/pauln/local-audio-recorder) [![GitHub stars](https://img.shields.io/github/stars/pauln/local-audio-recorder?style=flat)](https://github.com/pauln/local-audio-recorder/stargazers) - Local audio recorder (no streaming server required).  Currently requires Flash Player 10.1 or above.
* [Jukebox](https://github.com/AlwynW/Jukebox) [![GitHub stars](https://img.shields.io/github/stars/AlwynW/Jukebox?style=flat)](https://github.com/AlwynW/Jukebox/stargazers) - Music manager for Actionscript 3 projects.
* [Flod](https://github.com/photonstorm/Flod) [![GitHub stars](https://img.shields.io/github/stars/photonstorm/Flod?style=flat)](https://github.com/photonstorm/Flod/stargazers) - Amiga SoundTracker (MOD) and FastTracker (XM) Replay Library.

#### Video Player

* [Flowplayer](https://github.com/flowplayer/flash) [![GitHub stars](https://img.shields.io/github/stars/flowplayer/flash?style=flat)](https://github.com/flowplayer/flash/stargazers) - Flowplayer Flash, the video player for the Web.
* [Goplayer](https://github.com/dbrock/goplayer) [![GitHub stars](https://img.shields.io/github/stars/dbrock/goplayer?style=flat)](https://github.com/dbrock/goplayer/stargazers) - Modern open-source video player written in ActionScript 3.
* [OSFlashVideoPlayer](https://github.com/FlashJunior/OSFlashVideoPlayer) [![GitHub stars](https://img.shields.io/github/stars/FlashJunior/OSFlashVideoPlayer?style=flat)](https://github.com/FlashJunior/OSFlashVideoPlayer/stargazers) - Open source flash video player.
* [F4player](https://github.com/gokercebeci/f4player) [![GitHub stars](https://img.shields.io/github/stars/gokercebeci/f4player?style=flat)](https://github.com/gokercebeci/f4player/stargazers) - Open Source AS3 Flash Video Player.
* [dashas](https://github.com/castlabs/dashas) [![GitHub stars](https://img.shields.io/github/stars/castlabs/dashas?style=flat)](https://github.com/castlabs/dashas/stargazers) - MPEG-DASH player written in ActionScript.
* [hlsplayer](https://github.com/erlyvideo/hlsplayer) [![GitHub stars](https://img.shields.io/github/stars/erlyvideo/hlsplayer?style=flat)](https://github.com/erlyvideo/hlsplayer/stargazers) - HLS player for OSMF flash framework.
* [vgaplayer](https://github.com/euske/vgaplayer) [![GitHub stars](https://img.shields.io/github/stars/euske/vgaplayer?style=flat)](https://github.com/euske/vgaplayer/stargazers) - Open source player for Adobe Flash Media Server streams (RTMP).

## Database

#### SQLite
* [AS3Query](https://github.com/kemsky/as3Query) [![GitHub stars](https://img.shields.io/github/stars/kemsky/as3Query?style=flat)](https://github.com/kemsky/as3Query/stargazers) - Another SQLite ORM and query DSL for ActionScript.
* [AIRdb](https://github.com/dkeskar/airdb) [![GitHub stars](https://img.shields.io/github/stars/dkeskar/airdb?style=flat)](https://github.com/dkeskar/airdb/stargazers) - AIR ORM for using client-side SQLite within AIR and Flex apps. Supports ActiveRecord style models, migrations and associations.
* [Flexine](https://github.com/riadvice/Flexine) [![GitHub stars](https://img.shields.io/github/stars/riadvice/Flexine?style=flat)](https://github.com/riadvice/Flexine/stargazers) - SQLite ORM for AIR.
* [AIR-sqlite](https://github.com/probertson/air-sqlite) [![GitHub stars](https://img.shields.io/github/stars/probertson/air-sqlite?style=flat)](https://github.com/probertson/air-sqlite/stargazers) - Utilities for working with SQLite databases in AIR.

#### MongoDB
* [MongoAS3](https://github.com/s9tpepper/MongoAS3) [![GitHub stars](https://img.shields.io/github/stars/s9tpepper/MongoAS3?style=flat)](https://github.com/s9tpepper/MongoAS3/stargazers) - MongoDB driver.
* [ActionMongo](https://github.com/RIAlizer/ActionMongo) [![GitHub stars](https://img.shields.io/github/stars/RIAlizer/ActionMongo?style=flat)](https://github.com/RIAlizer/ActionMongo/stargazers) - MongoDB driver.

#### CouchDB
* [AS3couchdb](https://github.com/bustardcelly/as3couchdb) [![GitHub stars](https://img.shields.io/github/stars/bustardcelly/as3couchdb?style=flat)](https://github.com/bustardcelly/as3couchdb/stargazers) - Client-side API for interacting with a CouchDB instance.
* [Soup](https://github.com/dima/soup) [![GitHub stars](https://img.shields.io/github/stars/dima/soup?style=flat)](https://github.com/dima/soup/stargazers) - Mixing CouchDB, Sinatra, AIR and RestfulX to create an offline/online ready app with undo/redo capabilities.

#### MySQL
* [AS3mysql](https://github.com/hgupta9/as3mysql) [![GitHub stars](https://img.shields.io/github/stars/hgupta9/as3mysql?style=flat)](https://github.com/hgupta9/as3mysql/stargazers) - Driver for the MySQL open source database.

#### PostgreSQL
* [Pegasus](https://github.com/uhoh-itsmaciek/pegasus) [![GitHub stars](https://img.shields.io/github/stars/uhoh-itsmaciek/pegasus?style=flat)](https://github.com/uhoh-itsmaciek/pegasus/stargazers) - Driver for the PostgreSQL open source database.

#### DynamoDB
* [AWS-dynamodb](https://github.com/ferf/aws-dynamodb-actionscript) [![GitHub stars](https://img.shields.io/github/stars/ferf/aws-dynamodb-actionscript?style=flat)](https://github.com/ferf/aws-dynamodb-actionscript/stargazers) - Driver for accessing Amazon's AWS DynamoDB.

#### Redis
* [AS3redis](https://github.com/zhangq0355/as3redis) [![GitHub stars](https://img.shields.io/github/stars/zhangq0355/as3redis?style=flat)](https://github.com/zhangq0355/as3redis/stargazers) - Driver for Redis.

## File Formats

#### Archives

* [FZip](https://github.com/claus/fzip) [![GitHub stars](https://img.shields.io/github/stars/claus/fzip?style=flat)](https://github.com/claus/fzip/stargazers) - Mature library to load, modify and create standard ZIP archives.
* [ASZip](https://code.google.com/archive/p/aszip/) - Generate ZIP archives from AS3.
* [Untar-Worker](https://github.com/mesmotronic/as3-worker-untar) [![GitHub stars](https://img.shields.io/github/stars/mesmotronic/as3-worker-untar?style=flat)](https://github.com/mesmotronic/as3-worker-untar/stargazers) - TAR extraction using AS3 Workers (background threads).

#### 3D Formats

* [AsCollada](https://github.com/timknip/ascollada) [![GitHub stars](https://img.shields.io/github/stars/timknip/ascollada?style=flat)](https://github.com/timknip/ascollada/stargazers) - Parse COLLADA 3D model files ([fork](https://github.com/david-gregory/ascollada) [![GitHub stars](https://img.shields.io/github/stars/david-gregory/ascollada?style=flat)](https://github.com/david-gregory/ascollada/stargazers)).
* [AsBlender](https://github.com/timknip/asblender) [![GitHub stars](https://img.shields.io/github/stars/timknip/asblender?style=flat)](https://github.com/timknip/asblender/stargazers) - Parse Blender .BLEND files.
* [AS3-bvh-parser](https://github.com/rkn14/as3-bvh-parser) [![GitHub stars](https://img.shields.io/github/stars/rkn14/as3-bvh-parser?style=flat)](https://github.com/rkn14/as3-bvh-parser/stargazers) - Parse BVH files.
* [EasyAGAL](https://github.com/Barliesque/EasyAGAL) [![GitHub stars](https://img.shields.io/github/stars/Barliesque/EasyAGAL?style=flat)](https://github.com/Barliesque/EasyAGAL/stargazers) - Simplifies development of AGAL shaders with code completion, code hinting,  macros, etc.

#### CSV

* [CSV4AS3](https://github.com/lizardon/CSV4AS3) [![GitHub stars](https://img.shields.io/github/stars/lizardon/CSV4AS3?style=flat)](https://github.com/lizardon/CSV4AS3/stargazers) - CSV library ported from Apache Commons CSV.
* [Csvlib](https://github.com/51systems/csvlib) [![GitHub stars](https://img.shields.io/github/stars/51systems/csvlib?style=flat)](https://github.com/51systems/csvlib/stargazers) - CSV parser.

#### CSS

* [AS3csslib](https://github.com/heyfrench/as3csslib) [![GitHub stars](https://img.shields.io/github/stars/heyfrench/as3csslib?style=flat)](https://github.com/heyfrench/as3csslib/stargazers) - CSS3 parser, selector and style engine for ActionScript 3.0.
* [Fcss](https://github.com/theflashbum/fcss) [![GitHub stars](https://img.shields.io/github/stars/theflashbum/fcss?style=flat)](https://github.com/theflashbum/fcss/stargazers) - Flash Cascading StyleSheet Library.
* [Stylekit-as3](https://github.com/videojuicer/stylekit-as3) [![GitHub stars](https://img.shields.io/github/stars/videojuicer/stylekit-as3?style=flat)](https://github.com/videojuicer/stylekit-as3/stargazers) -  Skinnable user interfaces using CSS3.
* [Sass4as](https://github.com/jeremyruppel/sass4as) [![GitHub stars](https://img.shields.io/github/stars/jeremyruppel/sass4as?style=flat)](https://github.com/jeremyruppel/sass4as/stargazers) - Syntactically Awesome Stylesheets for ActionScript 3.
* [Jakute-CSS](https://github.com/kakenbok/Jakute-Styling-Engine) [![GitHub stars](https://img.shields.io/github/stars/kakenbok/Jakute-Styling-Engine?style=flat)](https://github.com/kakenbok/Jakute-Styling-Engine/stargazers) - Jakute is a CSS framework for ActionScript/Flash.
* [CSS.as](https://gist.github.com/trxcllnt/1161266) - Single-file CSS parser, part of TinyTLF project.

#### BSON

* [ActionBSON](https://github.com/fminzoni/ActionBSON) [![GitHub stars](https://img.shields.io/github/stars/fminzoni/ActionBSON?style=flat)](https://github.com/fminzoni/ActionBSON/stargazers) - BSON data encoder/decoder.
* [MongoAS3](https://github.com/s9tpepper/MongoAS3) [![GitHub stars](https://img.shields.io/github/stars/s9tpepper/MongoAS3?style=flat)](https://github.com/s9tpepper/MongoAS3/stargazers) - MongoDB Driver which includes BSON I/O.

#### EXIF

* [AS3-exif-lib](https://github.com/unstoppable/actionscript-exif-reading-lib) [![GitHub stars](https://img.shields.io/github/stars/unstoppable/actionscript-exif-reading-lib?style=flat)](https://github.com/unstoppable/actionscript-exif-reading-lib/stargazers) - Parse JPEG EXIF data.
* [Exif-as3](https://github.com/bashi/exif-as3) [![GitHub stars](https://img.shields.io/github/stars/bashi/exif-as3?style=flat)](https://github.com/bashi/exif-as3/stargazers) - Parse JPEG EXIF data.

#### FXG

* [Fxg-as3-lib](https://github.com/pixelami/fxg-as3-lib) [![GitHub stars](https://img.shields.io/github/stars/pixelami/fxg-as3-lib?style=flat)](https://github.com/pixelami/fxg-as3-lib/stargazers) - Pure AS3 FXG rendering library (both runtime rendering and mxml supported).
* [Fxg2as3](https://github.com/ZackPierce/fxg2as3) [![GitHub stars](https://img.shields.io/github/stars/ZackPierce/fxg2as3?style=flat)](https://github.com/ZackPierce/fxg2as3/stargazers) - Converting FXG markup into executable Actionscript 3 code.

#### GIF

* [AS3gif](https://github.com/audreyt/as3gif) [![GitHub stars](https://img.shields.io/github/stars/audreyt/as3gif?style=flat)](https://github.com/audreyt/as3gif/stargazers) - Play and encode Animated GIFs.
* [GIF Player](https://github.com/theturtle32/Flash-Animated-GIF-Library) [![GitHub stars](https://img.shields.io/github/stars/theturtle32/Flash-Animated-GIF-Library?style=flat)](https://github.com/theturtle32/Flash-Animated-GIF-Library/stargazers) - Play Animated GIFs in Flash.
* [Async-gif-decoder](https://github.com/honzabrecka/async-gif-decoder) [![GitHub stars](https://img.shields.io/github/stars/honzabrecka/async-gif-decoder?style=flat)](https://github.com/honzabrecka/async-gif-decoder/stargazers) - Asynchronous GIF decoder & player.

#### ICAL

* [AS3iCAL](https://github.com/nicolai86/as3.iCal) [![GitHub stars](https://img.shields.io/github/stars/nicolai86/as3.iCal?style=flat)](https://github.com/nicolai86/as3.iCal/stargazers) - iCal parser based on the RFC2445 specification.

#### JSON

* [Actionjson](https://github.com/mherkender/actionjson) [![GitHub stars](https://img.shields.io/github/stars/mherkender/actionjson?style=flat)](https://github.com/mherkender/actionjson/stargazers) - Faster, more advanced ActionScript 3 JSON library.
* [Jameson](https://github.com/mattupstate/jameson) [![GitHub stars](https://img.shields.io/github/stars/mattupstate/jameson?style=flat)](https://github.com/mattupstate/jameson/stargazers) - JSON Document Object Mapper.
* [Serialkiller](https://github.com/benbjohnson/serialkiller) [![GitHub stars](https://img.shields.io/github/stars/benbjohnson/serialkiller?style=flat)](https://github.com/benbjohnson/serialkiller/stargazers) - JSON & XML serialization library.
* [JsonMapper](https://github.com/kemsky/JsonMapper) [![GitHub stars](https://img.shields.io/github/stars/kemsky/JsonMapper?style=flat)](https://github.com/kemsky/JsonMapper/stargazers) - Typed JSON parser.
* [JSONTools](https://github.com/s9tpepper/JSONTools) [![GitHub stars](https://img.shields.io/github/stars/s9tpepper/JSONTools?style=flat)](https://github.com/s9tpepper/JSONTools/stargazers) - JSON errors, the speed of the JSWoof JSON library, and E4X style queries dubbed E4J.

#### Markdown

* [Showdown.as](https://gist.github.com/cstrahan/648771) - Port of showdown.js.
* [Actiondown](https://github.com/bbeaumont/Actiondown) [![GitHub stars](https://img.shields.io/github/stars/bbeaumont/Actiondown?style=flat)](https://github.com/bbeaumont/Actiondown/stargazers) - Port of Javascript Showdown.
* [Markdownlib](https://github.com/Corsaair/markdownlib) [![GitHub stars](https://img.shields.io/github/stars/Corsaair/markdownlib?style=flat)](https://github.com/Corsaair/markdownlib/stargazers) - Implementation of Markdown.

#### MP3

* [AS3id3lib](https://github.com/devxoul/as3id3lib) [![GitHub stars](https://img.shields.io/github/stars/devxoul/as3id3lib?style=flat)](https://github.com/devxoul/as3id3lib/stargazers) - Parse MP3 ID3 data.
* [AS3Icy](https://github.com/claus/as3icy) [![GitHub stars](https://img.shields.io/github/stars/claus/as3icy?style=flat)](https://github.com/claus/as3icy/stargazers) - Decode and play live MP3 streams from Shoutcast, Icecast and Limewire.

#### PDF

* [AlivePDF](https://code.google.com/archive/p/alivepdf/) - Client side PDF generation ([github](https://github.com/riadvice/alivepdf) [![GitHub stars](https://img.shields.io/github/stars/riadvice/alivepdf?style=flat)](https://github.com/riadvice/alivepdf/stargazers)).
* [PurePDF](https://github.com/sephiroth74/purePDF) [![GitHub stars](https://img.shields.io/github/stars/sephiroth74/purePDF?style=flat)](https://github.com/sephiroth74/purePDF/stargazers) - Complete PDF library, port of Java iText.
* [HalcyonPDF](https://github.com/systemed/halcyon_pdf) [![GitHub stars](https://img.shields.io/github/stars/systemed/halcyon_pdf?style=flat)](https://github.com/systemed/halcyon_pdf/stargazers) - OpenStreetMap PDF renderer.
* [PDFCase](https://github.com/dickclaus/pdfcase) [![GitHub stars](https://img.shields.io/github/stars/dickclaus/pdfcase?style=flat)](https://github.com/dickclaus/pdfcase/stargazers) - PDF Library.
* [PDFView](https://github.com/jankapunkt/PDFView) [![GitHub stars](https://img.shields.io/github/stars/jankapunkt/PDFView?style=flat)](https://github.com/jankapunkt/PDFView/stargazers) - PDF viewer built from scratch.

#### PSD

* [AS3-psd-parser](https://github.com/warrenseine/as3-psd-parser) [![GitHub stars](https://img.shields.io/github/stars/warrenseine/as3-psd-parser?style=flat)](https://github.com/warrenseine/as3-psd-parser/stargazers) - Parse Photoshop PSD files and render as BitmapData objects.

#### SWF

* [AS3swf](https://github.com/claus/as3swf) [![GitHub stars](https://img.shields.io/github/stars/claus/as3swf?style=flat)](https://github.com/claus/as3swf/stargazers) - Low level library to parse, create, modify and publish SWF files.
* [AS3abc](https://github.com/imcj/as3abc) [![GitHub stars](https://img.shields.io/github/stars/imcj/as3abc?style=flat)](https://github.com/imcj/as3abc/stargazers) - Low level library to parse, create, modify and publish ABC (Actionscript Block Code) files.
* [SWFWire](https://github.com/magicalhobo/SWFWire) [![GitHub stars](https://img.shields.io/github/stars/magicalhobo/SWFWire?style=flat)](https://github.com/magicalhobo/SWFWire/stargazers) - SWF Decompiler and Inspector Tools.
* [Abc-abstraction](https://github.com/krilnon/abc-abstraction) [![GitHub stars](https://img.shields.io/github/stars/krilnon/abc-abstraction?style=flat)](https://github.com/krilnon/abc-abstraction/stargazers) - Allows ABC to be analyzed, manipulated, packaged back into an SWF, and run.

#### SVG

* [AS3SVGRenderer](https://github.com/LucasLorentz/AS3SVGRenderer) [![GitHub stars](https://img.shields.io/github/stars/LucasLorentz/AS3SVGRenderer?style=flat)](https://github.com/LucasLorentz/AS3SVGRenderer/stargazers) - SVG Renderer for Flash Player.
* [SVGParser](https://github.com/millermedeiros/SVGParser) [![GitHub stars](https://img.shields.io/github/stars/millermedeiros/SVGParser?style=flat)](https://github.com/millermedeiros/SVGParser/stargazers) - SVG parser and renderer to FIVe3D and HTML5 canvas.

#### XML

* [XMLSerializer](https://github.com/vapesolius/XMLSerializer) [![GitHub stars](https://img.shields.io/github/stars/vapesolius/XMLSerializer?style=flat)](https://github.com/vapesolius/XMLSerializer/stargazers) - Library which allows data serialisation from ActionScript to XML and from XML to ActionScript.
* [DynamicXMLParser](https://github.com/lmgerhard/DynamicXMLParser) [![GitHub stars](https://img.shields.io/github/stars/lmgerhard/DynamicXMLParser?style=flat)](https://github.com/lmgerhard/DynamicXMLParser/stargazers) - Dynamic parse xml content into predefined data classes (actionscript 3).
* [Nudge](https://github.com/pluglimited/Nudge) [![GitHub stars](https://img.shields.io/github/stars/pluglimited/Nudge?style=flat)](https://github.com/pluglimited/Nudge/stargazers) - Framework to serialize/deserialize objects as XML.
* [AStream](https://github.com/kokorin/AStream) [![GitHub stars](https://img.shields.io/github/stars/kokorin/AStream?style=flat)](https://github.com/kokorin/AStream/stargazers) - XML to Object (and vice versa) mapping library written in AS3. Compatible with XStream.

#### XLSX

* [AS3-xlsx-reader](https://github.com/childoftv/as3-xlsx-reader) [![GitHub stars](https://img.shields.io/github/stars/childoftv/as3-xlsx-reader?style=flat)](https://github.com/childoftv/as3-xlsx-reader/stargazers) - Parse Open XML Excel (.XLSX) or Open Office spreadsheets.


## Networking
#### Data Loader

* [GreenSock LoaderMax](https://github.com/greensock/GreenSock-AS3) [![GitHub stars](https://img.shields.io/github/stars/greensock/GreenSock-AS3?style=flat)](https://github.com/greensock/GreenSock-AS3/stargazers) - Provides an easy and powerful way to load assets at runtime.
* [BulkLoader](https://github.com/arthur-debert/BulkLoader) [![GitHub stars](https://img.shields.io/github/stars/arthur-debert/BulkLoader?style=flat)](https://github.com/arthur-debert/BulkLoader/stargazers) - Bulk asset loading library for Actionscript.
* [AssetLoader](https://github.com/Matan/AssetLoader) [![GitHub stars](https://img.shields.io/github/stars/Matan/AssetLoader?style=flat)](https://github.com/Matan/AssetLoader/stargazers) - Multi-file/asset loader for AS3 built on AS3Signals.

#### Hardware

* [AS3midilib](https://github.com/heyfrench/as3midilib) [![GitHub stars](https://img.shields.io/github/stars/heyfrench/as3midilib?style=flat)](https://github.com/heyfrench/as3midilib/stargazers) - Work with MIDI files and MIDI input/output devices.
* [AS3glue](https://code.google.com/archive/p/as3glue/) - Communication for Arduino boards.
* [AS3-arduino](https://github.com/quetwo/as3-arduino-connector) [![GitHub stars](https://img.shields.io/github/stars/quetwo/as3-arduino-connector?style=flat)](https://github.com/quetwo/as3-arduino-connector/stargazers) - Connecting Arduino Prototyping board to Adobe AIR.
* [AIRkinect](https://github.com/AS3NUI/airkinect-2-core) [![GitHub stars](https://img.shields.io/github/stars/AS3NUI/airkinect-2-core?style=flat)](https://github.com/AS3NUI/airkinect-2-core/stargazers) - ANE for integrating with Microsoft Kinect. ([examples](https://github.com/AS3NUI/airkinect-2-examples) [![GitHub stars](https://img.shields.io/github/stars/AS3NUI/airkinect-2-examples?style=flat)](https://github.com/AS3NUI/airkinect-2-examples/stargazers)).
* [KinectGate](https://github.com/cleoag/KinectGate) [![GitHub stars](https://img.shields.io/github/stars/cleoag/KinectGate?style=flat)](https://github.com/cleoag/KinectGate/stargazers) - KinectSDK to AS3 socket gate.
* [Kinect-Gestures](https://github.com/tonybeltramelli/Air-Kinect-Gesture-Lib) [![GitHub stars](https://img.shields.io/github/stars/tonybeltramelli/Air-Kinect-Gesture-Lib?style=flat)](https://github.com/tonybeltramelli/Air-Kinect-Gesture-Lib/stargazers) - AIR Kinect Gesture Library.
* [OpenTSPS](https://github.com/labatrockwell/openTSPS) [![GitHub stars](https://img.shields.io/github/stars/labatrockwell/openTSPS?style=flat)](https://github.com/labatrockwell/openTSPS/stargazers) - TSPS is a cross platform Toolkit for Sensing People in Spaces. It performs openCV operations on live video (Kinect, web camera, etc) and sends it to clients as JSON (via WebSockets), OSC, TUIO, or TCP.
* [LeapMotionAS3](https://github.com/logotype/LeapMotionAS3) [![GitHub stars](https://img.shields.io/github/stars/logotype/LeapMotionAS3?style=flat)](https://github.com/logotype/LeapMotionAS3/stargazers) - Integrate with the LeapMotion sensor (provides Gestures, Image, Skeleton/Bone @ 210 FPS).

#### Servers

* [AIRhttp](https://github.com/leopoldodonnell/airhttp) [![GitHub stars](https://img.shields.io/github/stars/leopoldodonnell/airhttp?style=flat)](https://github.com/leopoldodonnell/airhttp/stargazers) - HTTP Server for Adobe AIR.
* [AIR-Server](https://github.com/wouterverweirder/AIR-Server) [![GitHub stars](https://img.shields.io/github/stars/wouterverweirder/AIR-Server?style=flat)](https://github.com/wouterverweirder/AIR-Server/stargazers) - Socket Server library for Adobe AIR.

#### OAuth

* [Actionscript-oauth2](https://github.com/charlesbihis/actionscript-oauth2) [![GitHub stars](https://img.shields.io/github/stars/charlesbihis/actionscript-oauth2?style=flat)](https://github.com/charlesbihis/actionscript-oauth2/stargazers) - Interfacing with OAuth 2.0 services.
* [oauth-flex](https://github.com/oauth-io/oauth-flex) [![GitHub stars](https://img.shields.io/github/stars/oauth-io/oauth-flex?style=flat)](https://github.com/oauth-io/oauth-flex/stargazers) - OAuth.io plugin for Apache Flex/ActionScript.
* [oauth-as3](https://github.com/mlepicki/oauth-as3) [![GitHub stars](https://img.shields.io/github/stars/mlepicki/oauth-as3?style=flat)](https://github.com/mlepicki/oauth-as3/stargazers) - Mavenized, RSL version of oauth-as3 library - OAuth for ActionScript 3.

#### HTTP

* [Hendrix-HTTP](https://github.com/HendrixString/Hendrix-HttP-AiR) [![GitHub stars](https://img.shields.io/github/stars/HendrixString/Hendrix-HttP-AiR?style=flat)](https://github.com/HendrixString/Hendrix-HttP-AiR/stargazers) - Lightweight HTTP library for ActionScript 3 (as3) inspired by Square's OkHttp.
* [HTTPForm](https://github.com/dv/HTTPForm) [![GitHub stars](https://img.shields.io/github/stars/dv/HTTPForm?style=flat)](https://github.com/dv/HTTPForm/stargazers) - Emulate a multipart/form-data HTML form submission request, including file upload.
* [AS3httpclient](https://github.com/abdul/as3httpclient) [![GitHub stars](https://img.shields.io/github/stars/abdul/as3httpclient?style=flat)](https://github.com/abdul/as3httpclient/stargazers) - HTTP client implementation.
* [AS3httpclient](https://github.com/gabriel/as3httpclient) [![GitHub stars](https://img.shields.io/github/stars/gabriel/as3httpclient?style=flat)](https://github.com/gabriel/as3httpclient/stargazers) - HTTP client implementation.
* [Amazon Web Services](https://github.com/satoshi7/ActionScript-API-for-AWS-Amazon-Web-Services-) [![GitHub stars](https://img.shields.io/github/stars/satoshi7/ActionScript-API-for-AWS-Amazon-Web-Services-?style=flat)](https://github.com/satoshi7/ActionScript-API-for-AWS-Amazon-Web-Services-/stargazers) - AS3 API for AWS.

#### P2P

* [P2Plocal](https://github.com/palkan/as3_p2plocal) [![GitHub stars](https://img.shields.io/github/stars/palkan/as3_p2plocal?style=flat)](https://github.com/palkan/as3_p2plocal/stargazers) - Local RTMFP connections.
* [Android-Flash-P2P](https://github.com/beautifycode/Android-Flash-P2P) [![GitHub stars](https://img.shields.io/github/stars/beautifycode/Android-Flash-P2P?style=flat)](https://github.com/beautifycode/Android-Flash-P2P/stargazers) - P2P Communication between a Client.swf and an Android Device with AIR.
* [NetGrouper](https://github.com/walpolea/NetGrouper) [![GitHub stars](https://img.shields.io/github/stars/walpolea/NetGrouper?style=flat)](https://github.com/walpolea/NetGrouper/stargazers) - Wrapper for NetGroup and RTMFP Multicasting abilities to create quick P2P multiplayer games over local networks or Adobe Cirrus.
* [HydraP2P](https://github.com/devboy/HydraP2P) [![GitHub stars](https://img.shields.io/github/stars/devboy/HydraP2P?style=flat)](https://github.com/devboy/HydraP2P/stargazers) - Simplifies the peer-to-peer API introduced in Flash Player 10.1.
* [GroupP2P](https://github.com/oohazard/GroupP2P) [![GitHub stars](https://img.shields.io/github/stars/oohazard/GroupP2P?style=flat)](https://github.com/oohazard/GroupP2P/stargazers) - P2P-based netgroup.
* [HLS-P2P](https://github.com/lava-tech/hls-p2p) [![GitHub stars](https://img.shields.io/github/stars/lava-tech/hls-p2p?style=flat)](https://github.com/lava-tech/hls-p2p/stargazers) - Flash OSMF based hybrid cdn&p2p hls solution.
* [P2Pmessaging](https://github.com/dreamsocket/actionscript-p2p_messaging) [![GitHub stars](https://img.shields.io/github/stars/dreamsocket/actionscript-p2p_messaging?style=flat)](https://github.com/dreamsocket/actionscript-p2p_messaging/stargazers) - Simple messaging framework for doing P2P in Flash.
* [ArcusNode](https://github.com/OpenRTMFP/ArcusNode) [![GitHub stars](https://img.shields.io/github/stars/OpenRTMFP/ArcusNode?style=flat)](https://github.com/OpenRTMFP/ArcusNode/stargazers) - RTMFP Rendevouz Service For Peer Assisted Networking With Adobe Flash on Node JS.

#### Sockets

* [AS3WebSocket](https://github.com/theturtle32/AS3WebSocket) [![GitHub stars](https://img.shields.io/github/stars/theturtle32/AS3WebSocket?style=flat)](https://github.com/theturtle32/AS3WebSocket/stargazers) - WebSocket client implementation for the final WebSocket Draft RFC6455.
* [SmartSocket](https://github.com/XaeroDegreaz/SmartSocket) [![GitHub stars](https://img.shields.io/github/stars/XaeroDegreaz/SmartSocket?style=flat)](https://github.com/XaeroDegreaz/SmartSocket/stargazers) - SmartSocket is a Java and PHP socket server engine, to make creating multi-user applications quick and painless.
* [FlashSocket.IO](https://github.com/simb/FlashSocket.IO) [![GitHub stars](https://img.shields.io/github/stars/simb/FlashSocket.IO?style=flat)](https://github.com/simb/FlashSocket.IO/stargazers) - Clients connect to Socket.IO servers from AS3/AIR clients.
* [Socket.io](https://github.com/ascorbic/socket-io-actionscript) [![GitHub stars](https://img.shields.io/github/stars/ascorbic/socket-io-actionscript?style=flat)](https://github.com/ascorbic/socket-io-actionscript/stargazers) - Socket.IO Actionscript 3 client.
* [AMFsocket](https://github.com/chadrem/amf_socket) [![GitHub stars](https://img.shields.io/github/stars/chadrem/amf_socket?style=flat)](https://github.com/chadrem/amf_socket/stargazers) - Bi-directional RPC library for high performance network communication.
* [Sockpuppet](https://github.com/rjungemann/sockpuppet) [![GitHub stars](https://img.shields.io/github/stars/rjungemann/sockpuppet?style=flat)](https://github.com/rjungemann/sockpuppet/stargazers) - Complete Ruby/ActionScript socket client/server with AMF.
* [Socket.io-flash](https://github.com/sinnus/socket.io-flash) [![GitHub stars](https://img.shields.io/github/stars/sinnus/socket.io-flash?style=flat)](https://github.com/sinnus/socket.io-flash/stargazers) - Communication to Socket.IO v.0.8+ servers.
* [ws-flash-client](https://github.com/youurayy/ws-flash-client) [![GitHub stars](https://img.shields.io/github/stars/youurayy/ws-flash-client?style=flat)](https://github.com/youurayy/ws-flash-client/stargazers) - Reliable minimalistic WebSocket client (uses Adobe Flash where native WebSocket is not available).

#### Protocols

* [GIT](https://github.com/nexussays/git-as3) [![GitHub stars](https://img.shields.io/github/stars/nexussays/git-as3?style=flat)](https://github.com/nexussays/git-as3/stargazers) - Client-side implementation of Git.
* [AIRplay](https://github.com/mikkoh/AS3-Airplay) [![GitHub stars](https://img.shields.io/github/stars/mikkoh/AS3-Airplay?style=flat)](https://github.com/mikkoh/AS3-Airplay/stargazers) - Client-side implementation of Apple's Airplay.
* [TeaTime](https://github.com/aemoncannon/croqodile) [![GitHub stars](https://img.shields.io/github/stars/aemoncannon/croqodile?style=flat)](https://github.com/aemoncannon/croqodile/stargazers) - AS3/Erlang implementation of the Croquet project's TeaTime protocol.
* [XMPP](https://github.com/lyokato/as3xmppclient) [![GitHub stars](https://img.shields.io/github/stars/lyokato/as3xmppclient?style=flat)](https://github.com/lyokato/as3xmppclient/stargazers) - Client-side implementation of XMPP library.
* [XMPP](https://github.com/bluef/kuching) [![GitHub stars](https://img.shields.io/github/stars/bluef/kuching?style=flat)](https://github.com/bluef/kuching/stargazers) - Lightweight implementation of XMPP library.
* [AMQP](https://github.com/0x6e6562/as3-amqp) [![GitHub stars](https://img.shields.io/github/stars/0x6e6562/as3-amqp?style=flat)](https://github.com/0x6e6562/as3-amqp/stargazers) - Client-side implementation of the 0-8 version of AMQP.
* [NTP](https://github.com/charlespalen/AS3-NTP-Implementation) [![GitHub stars](https://img.shields.io/github/stars/charlespalen/AS3-NTP-Implementation?style=flat)](https://github.com/charlespalen/AS3-NTP-Implementation/stargazers) - Client-side implementation of NTP Client (Network Time Protocol).
* [FUDI](https://github.com/matthiasbreuer/FUDI-as3) [![GitHub stars](https://img.shields.io/github/stars/matthiasbreuer/FUDI-as3?style=flat)](https://github.com/matthiasbreuer/FUDI-as3/stargazers) - Client-side implementation of the Puredata FUDI protocol.
* [BDD Cucumber](https://github.com/flashquartermaster/Cuke4AS3) [![GitHub stars](https://img.shields.io/github/stars/flashquartermaster/Cuke4AS3?style=flat)](https://github.com/flashquartermaster/Cuke4AS3/stargazers) - A BDD Cucumber wire protocol implementation for Flash ActionScript.

#### Email

* [AIRXMail](https://github.com/hgupta9/AirXMail) [![GitHub stars](https://img.shields.io/github/stars/hgupta9/AirXMail?style=flat)](https://github.com/hgupta9/AirXMail/stargazers) - Complete client-side email library supporting SMTP, POP3 and IMAP4.
* [AS3Mailer](https://github.com/Matan/AS3Mailer) [![GitHub stars](https://img.shields.io/github/stars/Matan/AS3Mailer?style=flat)](https://github.com/Matan/AS3Mailer/stargazers) - Sends email using server script or invokes a mailto.

## Utilities

#### Artificial Intelligence

* [FiniteStateMachine](https://github.com/pzUH/FiniteStateMachine) [![GitHub stars](https://img.shields.io/github/stars/pzUH/FiniteStateMachine?style=flat)](https://github.com/pzUH/FiniteStateMachine/stargazers) - Finite State Machine for AI bot/agent.
* [N-GramPredictor](https://github.com/pzUH/N-GramPredictor) [![GitHub stars](https://img.shields.io/github/stars/pzUH/N-GramPredictor?style=flat)](https://github.com/pzUH/N-GramPredictor/stargazers) - n-Gram predictor for AI bot/agent.
* [Naive-BayesPredictor](https://github.com/pzUH/Naive-BayesPredictor) [![GitHub stars](https://img.shields.io/github/stars/pzUH/Naive-BayesPredictor?style=flat)](https://github.com/pzUH/Naive-BayesPredictor/stargazers) - Naive-Bayes predictor for AI bot/agent.
* [HierarchicalStateMachine](https://github.com/pzUH/HierarchicalStateMachine) [![GitHub stars](https://img.shields.io/github/stars/pzUH/HierarchicalStateMachine?style=flat)](https://github.com/pzUH/HierarchicalStateMachine/stargazers) - Hierarchical State Machine for AI bot/agent.
* [Godmode-as3](https://github.com/tconkling/godmode-as3) [![GitHub stars](https://img.shields.io/github/stars/tconkling/godmode-as3?style=flat)](https://github.com/tconkling/godmode-as3/stargazers) - Behavior tree implementation (artificial intelligence).
* [DecisionTree](https://github.com/pzUH/DecisionTree) [![GitHub stars](https://img.shields.io/github/stars/pzUH/DecisionTree?style=flat)](https://github.com/pzUH/DecisionTree/stargazers) - Binary decision tree for AI bot/agent.
* [FuzzyStateMachine](https://github.com/pzUH/FuzzyStateMachine) [![GitHub stars](https://img.shields.io/github/stars/pzUH/FuzzyStateMachine?style=flat)](https://github.com/pzUH/FuzzyStateMachine/stargazers) - Fuzzy State Machine (FuSM) for AI bot/agent.
* [SmartKid](https://github.com/skyfeiyun/SmartKid) [![GitHub stars](https://img.shields.io/github/stars/skyfeiyun/SmartKid?style=flat)](https://github.com/skyfeiyun/SmartKid/stargazers) - Powerful AI engine for 2D & 3D games.

#### Async

* [EasyAS-Worker](https://github.com/myflashlab/easyAS-Worker) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/easyAS-Worker?style=flat)](https://github.com/myflashlab/easyAS-Worker/stargazers) - Simplified wrapper for AIR Workers.
* [Worker-from-class](https://github.com/bortsen/worker-from-class) [![GitHub stars](https://img.shields.io/github/stars/bortsen/worker-from-class?style=flat)](https://github.com/bortsen/worker-from-class/stargazers) - Create Workers from Class definitions.

#### Crypto

* [BlooddyCrypto](https://github.com/blooddy/blooddy_crypto) [![GitHub stars](https://img.shields.io/github/stars/blooddy/blooddy_crypto?style=flat)](https://github.com/blooddy/blooddy_crypto/stargazers) - High-performance library for processing binary data. This library contains MD5, SHA-1, SHA-2, Base64, CRC32, JSON, PNG/JPEG encoders.
* [AS3Crypto](https://github.com/timkurvers/as3-crypto) [![GitHub stars](https://img.shields.io/github/stars/timkurvers/as3-crypto?style=flat)](https://github.com/timkurvers/as3-crypto/stargazers) - Fork of Henri Torgemane's excellent cryptography library ([patched](https://github.com/lyokato/as3crypto_patched) [![GitHub stars](https://img.shields.io/github/stars/lyokato/as3crypto_patched?style=flat)](https://github.com/lyokato/as3crypto_patched/stargazers)).
* [AS3corelib](https://github.com/mikechambers/as3corelib) [![GitHub stars](https://img.shields.io/github/stars/mikechambers/as3corelib?style=flat)](https://github.com/mikechambers/as3corelib/stargazers) -  MD5 and SHA1 hashing, Image encoders, and JSON serialization.
* [ASCrypt](https://github.com/Meychi/ASCrypt) [![GitHub stars](https://img.shields.io/github/stars/Meychi/ASCrypt?style=flat)](https://github.com/Meychi/ASCrypt/stargazers) - Crypto library with a similar API for multiple languages.
* [Nexuslib](https://github.com/nexussays/nexuslib-as3) [![GitHub stars](https://img.shields.io/github/stars/nexussays/nexuslib-as3?style=flat)](https://github.com/nexussays/nexuslib-as3/stargazers) - Reflection, serialization, seeded random number generation, cryptography, networking, and more.
* [Hashlib](https://github.com/Corsaair/hashlib) [![GitHub stars](https://img.shields.io/github/stars/Corsaair/hashlib?style=flat)](https://github.com/Corsaair/hashlib/stargazers) - Over 30 different hashing functions.
* [XXTEA-AS3](https://github.com/xxtea/xxtea-as3) [![GitHub stars](https://img.shields.io/github/stars/xxtea/xxtea-as3?style=flat)](https://github.com/xxtea/xxtea-as3/stargazers) - XXTEA encryption algorithm library for ActionScript 3.
* [Gibberish-AES](https://github.com/NordMike/gibberish-aes-as3) [![GitHub stars](https://img.shields.io/github/stars/NordMike/gibberish-aes-as3?style=flat)](https://github.com/NordMike/gibberish-aes-as3/stargazers) - A fully OpenSSL compliant ActionScript 3 library for AES encryption.

#### Data	

 * [AS3Commons Collections](https://github.com/AS3Commons/as3commons-collections) [![GitHub stars](https://img.shields.io/github/stars/AS3Commons/as3commons-collections?style=flat)](https://github.com/AS3Commons/as3commons-collections/stargazers) - Sophisticated and high-performance collections & iterators for AS3.
 
#### Geometry

* [AS3geometry](https://github.com/alecmce/as3geometry) [![GitHub stars](https://img.shields.io/github/stars/alecmce/as3geometry?style=flat)](https://github.com/alecmce/as3geometry/stargazers) - Primitives, Polygons, Intersections, etc.
* [AS3GeomAlgo](https://github.com/azrafe7/as3GeomAlgo) [![GitHub stars](https://img.shields.io/github/stars/azrafe7/as3GeomAlgo?style=flat)](https://github.com/azrafe7/as3GeomAlgo/stargazers) - Collection of geometry algorithms. Port of hxGeomAlgo.
* [Coral](https://github.com/richardlord/Coral) [![GitHub stars](https://img.shields.io/github/stars/richardlord/Coral?style=flat)](https://github.com/richardlord/Coral/stargazers) - High-performance classes for 3D mathematics (Point, Vector, Matrix, Quaternion).
* [Csg.as](https://github.com/timknip/csg.as) [![GitHub stars](https://img.shields.io/github/stars/timknip/csg.as?style=flat)](https://github.com/timknip/csg.as/stargazers) - Constructive Solid Geometry on 3D meshes.
* [PathUtils](https://github.com/alinakipoglu/Actionscript-PathUtils) [![GitHub stars](https://img.shields.io/github/stars/alinakipoglu/Actionscript-PathUtils?style=flat)](https://github.com/alinakipoglu/Actionscript-PathUtils/stargazers) - Working with quadratic, bezier and line sequences.
* [Hilbert](https://github.com/nodename/Hilbert) [![GitHub stars](https://img.shields.io/github/stars/nodename/Hilbert?style=flat)](https://github.com/nodename/Hilbert/stargazers) - Port of Hilbert curve from cortesi/scurve.
* [AS3AStar](https://github.com/tomnewton/AS3AStar) [![GitHub stars](https://img.shields.io/github/stars/tomnewton/AS3AStar?style=flat)](https://github.com/tomnewton/AS3AStar/stargazers) - Fast A-Star pathfinding algorithm.
* [A-star_pathfinder](https://github.com/kevhiggins/a-star_pathfinder) [![GitHub stars](https://img.shields.io/github/stars/kevhiggins/a-star_pathfinder?style=flat)](https://github.com/kevhiggins/a-star_pathfinder/stargazers) - A-Star pathfinding interface for tile based maps.
* [As3Pathfinder](https://github.com/azakhary/As3Pathfinder) [![GitHub stars](https://img.shields.io/github/stars/azakhary/As3Pathfinder?style=flat)](https://github.com/azakhary/As3Pathfinder/stargazers) - Grid Path finding Library written using Dijkstra's algorithm.

#### Math

* [AS3Units](https://github.com/erussell/AS3Units) [![GitHub stars](https://img.shields.io/github/stars/erussell/AS3Units?style=flat)](https://github.com/erussell/AS3Units/stargazers) - Port of NGUnits. Parsing, formatting, and converting between units of measure.
* [AS3LinAlg](https://github.com/inspirit/AS3LinAlg) [![GitHub stars](https://img.shields.io/github/stars/inspirit/AS3LinAlg?style=flat)](https://github.com/inspirit/AS3LinAlg/stargazers) - Linear Algebra library (Jacobi SVD, Eigen Vectors/Values, Cholesky LU, etc).
* [Performance Primitives](https://github.com/martinkallman/performance-as3) [![GitHub stars](https://img.shields.io/github/stars/martinkallman/performance-as3?style=flat)](https://github.com/martinkallman/performance-as3/stargazers) - High-performance math modeled on the Intel Performance Primitives.
* [Zexpression](https://github.com/Xorcerer/zexpression) [![GitHub stars](https://img.shields.io/github/stars/Xorcerer/zexpression?style=flat)](https://github.com/Xorcerer/zexpression/stargazers) - Parse and evalate math expressions with functions and variables.
* [FlexibleMatrix](https://github.com/Lukx/FlexibleMatrix) [![GitHub stars](https://img.shields.io/github/stars/Lukx/FlexibleMatrix?style=flat)](https://github.com/Lukx/FlexibleMatrix/stargazers) - A multi purpose Matrix class.
* [AS3eval](http://eval.hurlant.com/) - Packages the Tamarin ESC compiler to work within Flash Player. ([alternate](https://github.com/SimonRichardson/as3-eval) [![GitHub stars](https://img.shields.io/github/stars/SimonRichardson/as3-eval?style=flat)](https://github.com/SimonRichardson/as3-eval/stargazers)).
* [FlashFormulaEditor](https://github.com/zasdfgbnm/FlashFormulaEditor) [![GitHub stars](https://img.shields.io/github/stars/zasdfgbnm/FlashFormulaEditor?style=flat)](https://github.com/zasdfgbnm/FlashFormulaEditor/stargazers) - Formula editor made in Adobe Flex.

#### Text

* [Linkify-as3](https://github.com/CodeCatalyst/linkify-as3) [![GitHub stars](https://img.shields.io/github/stars/CodeCatalyst/linkify-as3?style=flat)](https://github.com/CodeCatalyst/linkify-as3/stargazers) - Convert URLs, e-mail addresses, phone numbers, into clickable links.
* [AS3hyphenation](https://github.com/gka/as3hyphenation) [![GitHub stars](https://img.shields.io/github/stars/gka/as3hyphenation?style=flat)](https://github.com/gka/as3hyphenation/stargazers) - Port of the Javascript text hyphenation library Hyphenator.js.

## Runtimes

#### Emulators

* [NES Emulator](https://github.com/nesbox/emulator) [![GitHub stars](https://img.shields.io/github/stars/nesbox/emulator?style=flat)](https://github.com/nesbox/emulator/stargazers) - Emulator of NES, Super Nintendo, Sega Mega Drive, GameBoy video consoles.
* [Commodore 64 Emulator](https://github.com/claus/fc64) [![GitHub stars](https://img.shields.io/github/stars/claus/fc64?style=flat)](https://github.com/claus/fc64/stargazers) - A low level Commodore 64 emulator written in Actionscript 3.
* [8080 Emulator](https://github.com/ozipi/As3_SpaceInvaders_Emulator) [![GitHub stars](https://img.shields.io/github/stars/ozipi/As3_SpaceInvaders_Emulator?style=flat)](https://github.com/ozipi/As3_SpaceInvaders_Emulator/stargazers) - An actionscript 3 space invaders emulator based on the intel 8080 processor.
* [8-bit VM](https://github.com/OutOfTheVoid/AS3-8-bit-VM) [![GitHub stars](https://img.shields.io/github/stars/OutOfTheVoid/AS3-8-bit-VM?style=flat)](https://github.com/OutOfTheVoid/AS3-8-bit-VM/stargazers) - An eight bit virtual machine written in actionscript.

#### Interpreters

* [JS](https://github.com/theturtle32/RhinoAS3) [![GitHub stars](https://img.shields.io/github/stars/theturtle32/RhinoAS3?style=flat)](https://github.com/theturtle32/RhinoAS3/stargazers) - RhinoJS, Port of Mozilla's Rhino JavaScript interpreter.
* [Simple JS](https://github.com/sixsided/Simplified-JavaScript-Interpreter) [![GitHub stars](https://img.shields.io/github/stars/sixsided/Simplified-JavaScript-Interpreter?style=flat)](https://github.com/sixsided/Simplified-JavaScript-Interpreter/stargazers) - AS3-based Javascript interpreter.
* [MIL](https://github.com/ser1zw/MIL) [![GitHub stars](https://img.shields.io/github/stars/ser1zw/MIL?style=flat)](https://github.com/ser1zw/MIL/stargazers) - A MIL language VM and interpreter written in ActionScript.
* [TALES](https://github.com/oaubert/tales4as) [![GitHub stars](https://img.shields.io/github/stars/oaubert/tales4as?style=flat)](https://github.com/oaubert/tales4as/stargazers) - TALES interpreter for ActionScript.
* [Scheme](https://github.com/hrundik/fScheme) [![GitHub stars](https://img.shields.io/github/stars/hrundik/fScheme?style=flat)](https://github.com/hrundik/fScheme/stargazers) - Scheme interpreter in ActionScript.
* [Lisp](https://github.com/rzubek/as_lisp) [![GitHub stars](https://img.shields.io/github/stars/rzubek/as_lisp?style=flat)](https://github.com/rzubek/as_lisp/stargazers) - Lisp dialect written in Actionscript, with compiler and bytecode interpreter.
* [Lisp Compiler](https://github.com/aemoncannon/las3r) [![GitHub stars](https://img.shields.io/github/stars/aemoncannon/las3r?style=flat)](https://github.com/aemoncannon/las3r/stargazers) - A lisp compiler for the AVM2.
* [CannonML](https://github.com/abiyasa/cannonml_as3) [![GitHub stars](https://img.shields.io/github/stars/abiyasa/cannonml_as3?style=flat)](https://github.com/abiyasa/cannonml_as3/stargazers) - keim's CannonML (shmup scripting language) interpreter.

## AIR Native Extensions

#### Audio ANE
* [SongPicker](https://github.com/richpixel/SongPickerANE) [![GitHub stars](https://img.shields.io/github/stars/richpixel/SongPickerANE?style=flat)](https://github.com/richpixel/SongPickerANE/stargazers) - A song picker/player ANE for iOS and Android.
* [SilentSwitch](https://github.com/StickSports/ANE-Silent-Switch) [![GitHub stars](https://img.shields.io/github/stars/StickSports/ANE-Silent-Switch?style=flat)](https://github.com/StickSports/ANE-Silent-Switch/stargazers) - ANE for iOS to mute sounds if the hardware silent switch is on.
* [VolumePro](https://github.com/myflashlab/VolumePro-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/VolumePro-ANE?style=flat)](https://github.com/myflashlab/VolumePro-ANE/stargazers) - Control native music stream volume and you can listen to the volume changes.
* [SystemVolume](https://github.com/nweber/SystemVolumeNativeExtension) [![GitHub stars](https://img.shields.io/github/stars/nweber/SystemVolumeNativeExtension?style=flat)](https://github.com/nweber/SystemVolumeNativeExtension/stargazers) - Interact with the system volume for iOS and Android devices.

#### Multimedia ANE
* [WebView (Tuarua)](https://github.com/tuarua/WebViewANE) [![GitHub stars](https://img.shields.io/github/stars/tuarua/WebViewANE?style=flat)](https://github.com/tuarua/WebViewANE/stargazers) - Modern WebView for OSX 10.10+, Windows Desktop, iOS 9.0+ and Android 21+. Uses CEF (Chromium Embedded Framework) on Windows, WKWebView on iOS/OSX, and WebView on Android.
* [WebView (FlashLab)](https://github.com/myflashlab/webView-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/webView-ANE?style=flat)](https://github.com/myflashlab/webView-ANE/stargazers) - Replacement for StageWebView, allows calling Javascript functions from AIR.
* [AVANE](https://github.com/tuarua/AVANE) [![GitHub stars](https://img.shields.io/github/stars/tuarua/AVANE?style=flat)](https://github.com/tuarua/AVANE/stargazers) - For building video encoding applications using FFmpeg.
* [PDF](https://github.com/myflashlab/PDF-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/PDF-ANE?style=flat)](https://github.com/myflashlab/PDF-ANE/stargazers) - Lets you open PDF files from your AIR mobile apps. Supported on Android and iOS.
* [VideoPlayer](https://github.com/myflashlab/videoPlayer-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/videoPlayer-ANE?style=flat)](https://github.com/myflashlab/videoPlayer-ANE/stargazers) - Play video files in Android or iOS native video player.
* [SurfaceVideoPlayer](https://github.com/myflashlab/surfaceVideoPlayer-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/surfaceVideoPlayer-ANE?style=flat)](https://github.com/myflashlab/surfaceVideoPlayer-ANE/stargazers) - SurfacePlayer ANE helps you play video files inside your air mobile projects.
* [Speech](https://github.com/myflashlab/speech-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/speech-ANE?style=flat)](https://github.com/myflashlab/speech-ANE/stargazers) - Convert strings to voice files and vice versa fully in the background.
* [MyAR](https://github.com/myflashlab/AR-ANE-Samples) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/AR-ANE-Samples?style=flat)](https://github.com/myflashlab/AR-ANE-Samples/stargazers) - AR ANE supporting Android and iOS 64-bit based on Metaio's SDK.
* [QR-zbar](https://github.com/saumitrabhave/qr-zbar-ane) [![GitHub stars](https://img.shields.io/github/stars/saumitrabhave/qr-zbar-ane?style=flat)](https://github.com/saumitrabhave/qr-zbar-ane/stargazers) - ANE for QR Code Reader.
* [Barcode](https://github.com/myflashlab/barcode-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/barcode-ANE?style=flat)](https://github.com/myflashlab/barcode-ANE/stargazers) - Scan almost any barcode type with this super fast barcode scanner ANE.
* [Bullet](https://github.com/mziwisky/bullet-ane) [![GitHub stars](https://img.shields.io/github/stars/mziwisky/bullet-ane?style=flat)](https://github.com/mziwisky/bullet-ane/stargazers) - Bullet physics simulation library.

#### File System ANE
* [FileChooser](https://github.com/myflashlab/fileChooser-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/fileChooser-ANE?style=flat)](https://github.com/myflashlab/fileChooser-ANE/stargazers) - Enable users to select a file from the device filesystem.
* [ZipManager](https://github.com/myflashlab/zipManager-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/zipManager-ANE?style=flat)](https://github.com/myflashlab/zipManager-ANE/stargazers) - Zip or unzip large zip archives super fast using native process on Android and iOS.
* [Spotlight](https://github.com/myflashlab/Spotlight-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/Spotlight-ANE?style=flat)](https://github.com/myflashlab/Spotlight-ANE/stargazers) - Integrate with iOS 9 Spotlight Search, to index search items and user generated content.

#### Networking ANE
* [Firebase](https://github.com/myflashlab/Firebase-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/Firebase-ANE?style=flat)](https://github.com/myflashlab/Firebase-ANE/stargazers) - API for Google Firebase on Android and iOS with 100% identical ActionScript API.
* [DownloadManager](https://github.com/myflashlab/downloadManager-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/downloadManager-ANE?style=flat)](https://github.com/myflashlab/downloadManager-ANE/stargazers) - Download large data files with pause/resume support.
* [BitTorrent](https://github.com/tuarua/BitTorrentANE) [![GitHub stars](https://img.shields.io/github/stars/tuarua/BitTorrentANE?style=flat)](https://github.com/tuarua/BitTorrentANE/stargazers) - For building BitTorrent enabled applications.

#### Hardware ANE
* [Bluetooth](https://github.com/myflashlab/bluetooth-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/bluetooth-ANE?style=flat)](https://github.com/myflashlab/bluetooth-ANE/stargazers) - Scan for other devices, connect to and pair with them and transfer data between them.
* [GPS](https://github.com/myflashlab/GPS-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/GPS-ANE?style=flat)](https://github.com/myflashlab/GPS-ANE/stargazers) - Get current device GPS location as fast as possible by automatically checking the best available provider.
* [GoogleVR](https://github.com/myflashlab/GoogleVR-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/GoogleVR-ANE?style=flat)](https://github.com/myflashlab/GoogleVR-ANE/stargazers) - Google Virtual Reality SDK available to AIR developers.
* [Joystick-ANE](https://github.com/StackAndHeap/joystick-ane) [![GitHub stars](https://img.shields.io/github/stars/StackAndHeap/joystick-ane?style=flat)](https://github.com/StackAndHeap/joystick-ane/stargazers) - ANE Joystick Library.
* [AIRControl](https://github.com/AlexanderOMara/AIRControl) [![GitHub stars](https://img.shields.io/github/stars/AlexanderOMara/AIRControl?style=flat)](https://github.com/AlexanderOMara/AIRControl/stargazers) - Adobe AIR Game Controller ANE.
* [AIROUYAController](https://github.com/gaslightgames/AIROUYAController) [![GitHub stars](https://img.shields.io/github/stars/gaslightgames/AIROUYAController?style=flat)](https://github.com/gaslightgames/AIROUYAController/stargazers) - ANE for the OUYA Controller.
* [AIRKinectv2](https://github.com/Tastenkunst/AIRKinectv2) [![GitHub stars](https://img.shields.io/github/stars/Tastenkunst/AIRKinectv2?style=flat)](https://github.com/Tastenkunst/AIRKinectv2/stargazers) - ANE for Microsoft Kinect v2 for Windows SDK.
* [Serial/MIDI/DMX](https://github.com/benkuper/AIR-NativeExtensions) [![GitHub stars](https://img.shields.io/github/stars/benkuper/AIR-NativeExtensions?style=flat)](https://github.com/benkuper/AIR-NativeExtensions/stargazers) - AIRBonjour, NativeSerial, NativeDMXController, NativeMIDI, VirtualMIDI, ExtendedMouse.
* [LeapMotionAS3](https://github.com/logotype/LeapMotionAS3) [![GitHub stars](https://img.shields.io/github/stars/logotype/LeapMotionAS3?style=flat)](https://github.com/logotype/LeapMotionAS3/stargazers) - ANE for LeapMotion sensor (provides Gestures, Image, Skeleton/Bone @ 210 FPS).

#### System ANE
* [TaskbarProgress](https://github.com/tuarua/TaskbarProgressANE) [![GitHub stars](https://img.shields.io/github/stars/tuarua/TaskbarProgressANE?style=flat)](https://github.com/tuarua/TaskbarProgressANE/stargazers) - Display taskbar progress on OSX & Windows 7/8/10 .
* [DesktopToast](https://github.com/tuarua/DesktopToastANE) [![GitHub stars](https://img.shields.io/github/stars/tuarua/DesktopToastANE?style=flat)](https://github.com/tuarua/DesktopToastANE/stargazers) - Display interactive toast notifications in Windows 8/10 and OSX.
* [AlarmManager](https://github.com/myflashlab/alarmManager-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/alarmManager-ANE?style=flat)](https://github.com/myflashlab/alarmManager-ANE/stargazers) - Run a scheduled task even if your AIR app is closed.
* [InAppPayments](https://github.com/myflashlab/inAppPayments-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/inAppPayments-ANE?style=flat)](https://github.com/myflashlab/inAppPayments-ANE/stargazers) - Identical in-app-billing and in-app-purchase ANE for Android and iOS.
* [PermissionCheck](https://github.com/myflashlab/PermissionCheck-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/PermissionCheck-ANE?style=flat)](https://github.com/myflashlab/PermissionCheck-ANE/stargazers) - Check and request for permissions in your Adobe Air app.
* [RateMe](https://github.com/myflashlab/RateMe-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/RateMe-ANE?style=flat)](https://github.com/myflashlab/RateMe-ANE/stargazers) - Ask your users to rate your app in the most efficient way.
* [Statusbar](https://github.com/myflashlab/Statusbar-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/Statusbar-ANE?style=flat)](https://github.com/myflashlab/Statusbar-ANE/stargazers) - Control the Statusbar in your AIR apps in runtime.
* [Badge](https://github.com/myflashlab/Badge-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/Badge-ANE?style=flat)](https://github.com/myflashlab/Badge-ANE/stargazers) - Control the iOS badge value.
* [WinDebug](http://www.henke37.cjb.net/windebug/) - Windows ANE to control applications, windows, memory, breakpoints, metadata, registry, etc.
* [Can-Open-URL](https://github.com/StickSports/ANE-Can-Open-URL) [![GitHub stars](https://img.shields.io/github/stars/StickSports/ANE-Can-Open-URL?style=flat)](https://github.com/StickSports/ANE-Can-Open-URL/stargazers) - ANE for iOS to detect whether an app is installed to handle a specific URL scheme.

#### Social ANE
* [Facebook](https://github.com/myflashlab/facebook-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/facebook-ANE?style=flat)](https://github.com/myflashlab/facebook-ANE/stargazers) - Integrate Facebook SDK into your AIR apps.
* [GCM](https://github.com/myflashlab/GCM-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/GCM-ANE?style=flat)](https://github.com/myflashlab/GCM-ANE/stargazers) - Use Google Cloud messaging on Android and iOS. .
* [Baidu](https://github.com/lilili87222/baidu-ane-for-ios-and-android) [![GitHub stars](https://img.shields.io/github/stars/lilili87222/baidu-ane-for-ios-and-android?style=flat)](https://github.com/lilili87222/baidu-ane-for-ios-and-android/stargazers) - Baidu ANE for for iOS and Android.

#### Analytics ANE
* [Admob](https://github.com/myflashlab/Admob-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/Admob-ANE?style=flat)](https://github.com/myflashlab/Admob-ANE/stargazers) - Admob ANE.
* [GameServices](https://github.com/myflashlab/GameServices-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/GameServices-ANE?style=flat)](https://github.com/myflashlab/GameServices-ANE/stargazers) - Google Game Services for Android+iOS.
* [MoPub](https://github.com/StickSports/MoPub-ANE) [![GitHub stars](https://img.shields.io/github/stars/StickSports/MoPub-ANE?style=flat)](https://github.com/StickSports/MoPub-ANE/stargazers) - ANE for MoPub advertising.
* [UMAnalytics](https://github.com/ColerYu/ANE-UMAnalytics) [![GitHub stars](https://img.shields.io/github/stars/ColerYu/ANE-UMAnalytics?style=flat)](https://github.com/ColerYu/ANE-UMAnalytics/stargazers) - ANE for UMAnalytics SDK (iOS and Android).
* [Localytics](https://github.com/randori/ANE-Localytics) [![GitHub stars](https://img.shields.io/github/stars/randori/ANE-Localytics?style=flat)](https://github.com/randori/ANE-Localytics/stargazers) - Localytics analytics for mobile Adobe AIR applications (iOS & Android).
* [Testflight](https://github.com/jlopez/ane-testflight) [![GitHub stars](https://img.shields.io/github/stars/jlopez/ane-testflight?style=flat)](https://github.com/jlopez/ane-testflight/stargazers) - Apple TestFlight ANE.
* [HockeyApp](https://github.com/airext/hockeyapp) [![GitHub stars](https://img.shields.io/github/stars/airext/hockeyapp?style=flat)](https://github.com/airext/hockeyapp/stargazers) - ANE for the Hockeyapp testing & distribute platform.
* [Chartboost](https://github.com/ChartBoost/air) [![GitHub stars](https://img.shields.io/github/stars/ChartBoost/air?style=flat)](https://github.com/ChartBoost/air/stargazers) - ANE for the Chartboost SDK with compile scripts.
* [Devtodev](https://github.com/devtodev-analytics/air-sdk) [![GitHub stars](https://img.shields.io/github/stars/devtodev-analytics/air-sdk?style=flat)](https://github.com/devtodev-analytics/air-sdk/stargazers) - A full-cycle analytics solution for game developers.
