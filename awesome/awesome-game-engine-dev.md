# Game Engine Development

[![GitHub stars](https://img.shields.io/github/stars/stevinz/awesome-game-engine-dev?style=flat)](https://github.com/stevinz/awesome-game-engine-dev/stargazers)

<!--lint ignore no-dead-urls-->

<div align="center">
    <a href="https://github.com/stevinz/awesome-game-engine-dev"><img width="1100" src="aged-title.png" alt="Awesome Game Engine Dev Logo"/></a>
</div>

# Awesome Game Engine Development [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome#readme)

Curated list of resources related to the development of game engines (tools that improve and speed up game creation). Specifically toward the development of high-level, fully featured game engines (e.g., Godot / Unity).

This includes things typically not found in low-level game engines, app / game frameworks, or graphics libraries (e.g., MonoGame / SDL). Most importantly of which would be a visual scene editor, but also capabilities like scripting, physics, asset management, special effects, monetization, etc.

<br />

## Contents

- [Game Engines](#game-engines)
    - [Awesome Collections](#awesome-collections)
    - [Popular](#popular)
    - [AAA](#aaa)
    - [Commercial](#commercial)
    - [Specialty](#specialty)
- [Learning](#learning)
    - [Computer Graphics](#computer-graphics)
    - [Engine Development](#engine-development)
    - [Game Development](#game-development)
    - [Graphical User Interface](#graphical-user-interface)
    - [Programming](#programming)
- [Libraries](#libraries)
    - [BASIC](#basic)
    - [C](#c)
    - [C++](#c-1)
    - [C#](#c-2)
    - [Dart](#dart)
    - [F#](#f)
    - [Go](#go)
    - [Haxe](#haxe)
    - [Lua](#lua)
    - [Java](#java)
    - [JavaScript](#javascript)
    - [Kotlin](#kotlin)
    - [Pascal](#pascal)
    - [Python](#python)
    - [Ruby](#ruby)
    - [Rust](#rust)
    - [Zig](#zig)
- [Open Source Games](#open-source-games)
    - [Awesome Collections](#awesome-collections-1)
    - [C](#c-3)
    - [C++](#c-4)
    - [Java](#java-1)
- [Specialty Topics](#specialty-topics)
    - [Asset Pipeline / Formats](#asset-pipeline--formats)
    - [Color Manipulation](#color-manipulation)
    - [Enemies / Pathfinding](#enemies--pathfinding)
    - [Entity Component Systems](#entity-component-systems)
    - [Fluid / Smoke](#fluid--smoke)
    - [Geometry](#geometry)
    - [Hair](#hair)
    - [Lighting / Shadows](#lighting--shadows)
    - [Network](#network)
    - [Particles](#particles)
    - [Physics](#physics)
    - [Rendering](#rendering)
    - [Scripting](#scripting)
    - [Shaders](#shaders)
    - [Signed Distance Fields](#signed-distance-fields)
    - [Tiling](#tiling)
    - [Transparency](#transparency)
- [Tools / Software](#tools--software)
    - [Awesome Collections](#awesome-collections-2)
    - [Animation Software](#animation-software)
    - [Audio Tools](#audio-tools)
    - [Color / Palettes](#color--palettes)
    - [Debugging / Profiling](#debugging--profiling)
    - [Image Editors](#image-editors)
    - [Level Editors](#level-editors)
    - [Materials / Textures](#materials--textures)
    - [Modeling Tools](#modeling-tools)
    - [Particle Tools](#particle-tools)
    - [Pixel Art](#pixel-art)
    - [Tilemap Editors](#tilemap-editors)
    - [Vector Editors](#vector-editors)
    - [Voxel](#voxel)
- [Video Game Assets](#video-game-assets)
    - [Audio Assets](#audio-assets)
    - [Graphic Assets](#graphic-assets)
    - [Material Assets](#material-assets)
    - [Model Assets](#model-assets)
- [Archive](#archive)
- [Legend](#legend)

<br />
<br />

## Game Engines
_Production ready game engines to tinker with, explore, learn and inspire._

### Awesome Collections
- 📚 [Awesome Game Engines](https://github.com/ChessMax/awesome-game-engines) [![GitHub stars](https://img.shields.io/github/stars/ChessMax/awesome-game-engines?style=flat)](https://github.com/ChessMax/awesome-game-engines/stargazers) - List of game engines.
- 📚 [Cool Engines](https://github.com/JohnClarking/CoolEngines) [![GitHub stars](https://img.shields.io/github/stars/JohnClarking/CoolEngines?style=flat)](https://github.com/JohnClarking/CoolEngines/stargazers) - List of open source graphic & game engines.
- 📚 [Fantasy Consoles](https://github.com/paladin-t/fantasy) [![GitHub stars](https://img.shields.io/github/stars/paladin-t/fantasy?style=flat)](https://github.com/paladin-t/fantasy/stargazers) - List of available fantasy consoles/computers.
- 📚 [Wikipedia: List of Game Engines](https://en.wikipedia.org/wiki/List_of_game_engines) - Game engines along with their platforms and licenses.

### Popular
- 🎉 [Godot](https://github.com/godotengine/godot) [![GitHub stars](https://img.shields.io/github/stars/godotengine/godot?style=flat)](https://github.com/godotengine/godot/stargazers) 🔥 - Feature-packed, open source engine. Excellent! [[Awesome](https://github.com/godotengine/awesome-godot) [![GitHub stars](https://img.shields.io/github/stars/godotengine/awesome-godot?style=flat)](https://github.com/godotengine/awesome-godot/stargazers) | [Website](https://godotengine.org)]
- 💸 [Unity](https://unity.com) - Biggest name in game engines, industry standard. [[Awesome](https://github.com/RyanNielson/awesome-unity) [![GitHub stars](https://img.shields.io/github/stars/RyanNielson/awesome-unity?style=flat)](https://github.com/RyanNielson/awesome-unity/stargazers)]
- 💸 [Unreal Engine](https://www.unrealengine.com) - AAA quality, insane feature set, photoreal visuals. [[Awesome](https://github.com/insthync/awesome-ue4) [![GitHub stars](https://img.shields.io/github/stars/insthync/awesome-ue4?style=flat)](https://github.com/insthync/awesome-ue4/stargazers)]

### AAA
- 🎉 [Amazon Lumberyard](https://github.com/aws/lumberyard) [![GitHub stars](https://img.shields.io/github/stars/aws/lumberyard?style=flat)](https://github.com/aws/lumberyard/stargazers) - AAA engine integrated with _AWS_ and _Twitch_. Forked from _CRYENGINE_.
- 💰 [C4 Engine](http://c4engine.com) - Modern console engine.
- 💸 [CRYENGINE](https://www.cryengine.com) - Powerful real-time game development platform by _Crytek_.
- 🆓 [Evergine](https://evergine.com) - High-quality 3D and 2D solutions. Formerly _Wave Engine_. [[Samples](https://github.com/EvergineTeam/Samples) [![GitHub stars](https://img.shields.io/github/stars/EvergineTeam/Samples?style=flat)](https://github.com/EvergineTeam/Samples/stargazers)]
- 💸 [Flax Engine](https://github.com/FlaxEngine/FlaxEngine) [![GitHub stars](https://img.shields.io/github/stars/FlaxEngine/FlaxEngine?style=flat)](https://github.com/FlaxEngine/FlaxEngine/stargazers) - Modern 3D game engine written in C++ and C#.
- 💰 [Gamebryo](http://www.gamebryo.com) - Complete toolset, flexible workflow, rapid prototyping.
- 🎉 [O3DE](https://github.com/o3de/o3de/) [![GitHub stars](https://img.shields.io/github/stars/o3de/o3de/?style=flat)](https://github.com/o3de/o3de//stargazers) - Multi-platform AAA engine. Cinema-quality 3D. Successor to _Lumberyard_.
- 💸 [Unigine](https://unigine.com) - Real-time 3D engine. Photorealistic graphics, large virtual worlds, C++ and C# API.

### Commercial
- 💰 [AppGameKit](https://www.appgamekit.com/studio) - Easy and quick game making by _TheGameCreators_.
- 💸 [Buildbox](https://www.buildbox.com) - Create 3D & 2D video games without coding.
- 💰 [Cave Engine](https://uniday.studio/cave/) - Fast and easy Python game engine for 3D.
- 💸 [Construct](https://www.construct.net/) - Drag and drop game builder. [[Awesome](https://github.com/ConstructCommunity/awesome-construct) [![GitHub stars](https://img.shields.io/github/stars/ConstructCommunity/awesome-construct?style=flat)](https://github.com/ConstructCommunity/awesome-construct/stargazers)]
- 💰 [Corgi Engine](https://corgi-engine.moremountains.com/) - 2D/2.5D platformer engine built on top of _Unity_.
- 🎉 [Defold](https://github.com/defold/defold) [![GitHub stars](https://img.shields.io/github/stars/defold/defold?style=flat)](https://github.com/defold/defold/stargazers) - Open sourced game engine by _King_. [[Website](https://defold.com)]
- 💸 [Felgo](https://felgo.com/games) - Build cross-platform 2D games in days, built with _Qt_.
- 💰 [GameGuru](https://www.game-guru.com/) - Game builder, 3D, no coding required by _TheGameCreators_.
- 💸 [GameMaker](https://www.yoyogames.com/en/gamemaker) - Popular 2D game development environment by _YoYo Games_.
- 💸 [GameSalad](https://gamesalad.com) - Sophisticated visual programming interface.
- 💸 [Luxe](https://luxeengine.com/) - 2D first engine, with a 2D/3D renderer.
- 💸 [MANU](https://manu-vgm.itch.io/) - Unique animation system helps you create games without coding.
- 💸 [NeoAxis](https://github.com/NeoAxis/NeoAxisEngine) [![GitHub stars](https://img.shields.io/github/stars/NeoAxis/NeoAxisEngine?style=flat)](https://github.com/NeoAxis/NeoAxisEngine/stargazers) - Versatile real-time platform for making games and apps.
- 💰 [Phaser Editor 2D](https://phasereditor2d.com) - Commercial, web-based editor for _Phaser_. [[GitHub](https://github.com/PhaserEditor2D/PhaserEditor2D-v3) [![GitHub stars](https://img.shields.io/github/stars/PhaserEditor2D/PhaserEditor2D-v3?style=flat)](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/stargazers)]
- 💸 [PlayCanvas](https://playcanvas.com) - Popular (_Flappy Bird_) WebGL game engine. [[Awesome](https://github.com/playcanvas/awesome-playcanvas) [![GitHub stars](https://img.shields.io/github/stars/playcanvas/awesome-playcanvas?style=flat)](https://github.com/playcanvas/awesome-playcanvas/stargazers) | [GitHub](https://github.com/playcanvas/engine) [![GitHub stars](https://img.shields.io/github/stars/playcanvas/engine?style=flat)](https://github.com/playcanvas/engine/stargazers)]
- 💸 [Roblox](https://www.roblox.com/create) - Create immersive 3D experiences with Lua scripting.
- 💸 [Simulation Starter Kit](https://benmorris.itch.io/plugin-based-scene-editor) - Create interactive 3D apps across a range of platforms.
- 💸 [Stencyl](https://github.com/Stencyl/stencyl-engine) [![GitHub stars](https://img.shields.io/github/stars/Stencyl/stencyl-engine?style=flat)](https://github.com/Stencyl/stencyl-engine/stargazers) - Quick and easy game making with visual scripting.
- 💸 [Titan Engine](https://esenthel.com/) - Cross-platform engine, started in 2000. Formerly _Esenthel Engine_.

### Specialty
- 💰 [3dSen](https://geod.itch.io/3dnes) - Emulator that lets you play _NES_ games in 3D. [[Website](http://www.geodstudio.net)]
- 🎉 [Adventure Game Studio](https://github.com/adventuregamestudio/ags) [![GitHub stars](https://img.shields.io/github/stars/adventuregamestudio/ags?style=flat)](https://github.com/adventuregamestudio/ags/stargazers) - Open source engine for point-and-click adventure games. [[Website](https://www.adventuregamestudio.co.uk/)]
- 💸 [DopeFish](https://lemontoast-games.itch.io/dopefish) - _Doom_ / _Heretic_ map loading system for _GameMaker_.
- 🎉 [GB Studio](https://github.com/chrismaltby/gb-studio) [![GitHub stars](https://img.shields.io/github/stars/chrismaltby/gb-studio?style=flat)](https://github.com/chrismaltby/gb-studio/stargazers) - Retro adventure game creator for _Game Boy_.
- 🔒 [HARFANG 3D](https://github.com/harfang3d/harfang3d) [![GitHub stars](https://img.shields.io/github/stars/harfang3d/harfang3d?style=flat)](https://github.com/harfang3d/harfang3d/stargazers) - 3D visualization library for industry professionals, usable in C++, Python, Lua, Go.
- 💰 [Platforming Engine](https://robvansaaze.itch.io/platforming-engine) - Everything you need to create your own platformer in _GameMaker_.
- 🎉 [Ren'Py](https://github.com/renpy/renpy) [![GitHub stars](https://img.shields.io/github/stars/renpy/renpy?style=flat)](https://github.com/renpy/renpy/stargazers) - Visual novel engine. [[Website](https://www.renpy.org/)]
- 💰 [RPG in a Box](https://www.rpginabox.com) - Turn your stories and ideas into games, built with _Godot_.
- 💰 [RPG Maker](https://www.rpgmakerweb.com) - Create an original role-playing game without any specialized knowledge.
- 🔒 [Twine](https://github.com/klembot/twinejs) [![GitHub stars](https://img.shields.io/github/stars/klembot/twinejs?style=flat)](https://github.com/klembot/twinejs/stargazers) - Tool for telling interactive, nonlinear stories.
- 💸 [Unbound](https://www.unbound.io/) - SDF‑powered game engine. Intuitively sculpt & script 3D games.

<br />
<br />

## Learning
_Info on topics necessary for designing and developing game engines._

### Computer Graphics
- Awesome Collections
    - 📚 [Awesome Demoscene](https://github.com/psykon/awesome-demoscene) [![GitHub stars](https://img.shields.io/github/stars/psykon/awesome-demoscene?style=flat)](https://github.com/psykon/awesome-demoscene/stargazers) - Underground computer art culture exploring computer graphics and sound.
    - 📚 [Awesome Graphics Libraries](https://github.com/jslee02/awesome-graphics-libraries) [![GitHub stars](https://img.shields.io/github/stars/jslee02/awesome-graphics-libraries?style=flat)](https://github.com/jslee02/awesome-graphics-libraries/stargazers) - Curated list of 3D graphics libraries and resources.
- Blog Articles
    - 📚 [Comparison of Modern Graphics APIs](https://web.archive.org/web/20260203162531/https://alain.xyz/blog/comparison-of-modern-graphics-apis) - Modern graphics APIs vs older APIs.
    - 📚 [GPU Performance for Game Artists](http://www.fragmentbuffer.com/gpu-performance-for-game-artists/) - Common art-related performance issues.
- Books
    - 📚 [GPU Gems](https://developer.nvidia.com/gpugems/gpugems/contributors) - Programming techniques, tips, and tricks for real-time graphics.
    - 📚 [GPU Gems 2](https://developer.nvidia.com/gpugems/gpugems2/copyright) - Programming techniques for high-performance graphics.
    - 📚 [GPU Gems 3](https://developer.nvidia.com/gpugems/gpugems3/contributors) - Collection of state-of-the-art GPU programming examples hosted by _NVIDIA_.
    - 📚 [Interactive Computer Graphics](https://www.cs.unm.edu/~angel/) - Top-down approach to computer graphics.
    - 📚 [Physically-Based Rendering](https://www.pbrt.org) - From the Academy Award winning authority on PBR.
- Education Portals
    - 📚 [Game Art Tricks](http://simonschreibt.de/game-art-tricks/) - Articles exploring different graphics techniques.
    - 📚 [Graphics Codex](https://graphicscodex.com/) - Essential digital reference and learning resource for computer graphics.
    - 📚 [Lighthouse3d.com](http://www.lighthouse3d.com/tutorials/) - Collection of tutorials on OpenGL, GLSL and other graphics topics.
    - 📚 [Paper Bug](https://www.jeremyong.com/paperbug/) - Indexed compendium of graphics programming papers.
    - 📚 [Scratchapixel](https://www.scratchapixel.com) - In depth coverage of computer graphics topics.
- Graphics API: DirectX
    - 🌎 [DirectX](https://learn.microsoft.com/en-us/windows/win32/directx) - _Microsoft_ API used to create 2D/3D games and apps. [[Blog](https://devblogs.microsoft.com/directx/) | [Samples](https://github.com/microsoft/DirectX-Graphics-Samples) [![GitHub stars](https://img.shields.io/github/stars/microsoft/DirectX-Graphics-Samples?style=flat)](https://github.com/microsoft/DirectX-Graphics-Samples/stargazers)]
    - 📚 [DirectXTutorial.com](http://www.directxtutorial.com/default.aspx) - Older resource with lots of tutorials on DirectX versions 9 & 11.
- Graphics API: Glide
    - 📚 [Glide](https://en.wikipedia.org/wiki/Glide_(API)) - Developed by _3dfx Interactive_ for their _Voodoo Graphics_ in the 1990's.
    - 🌎 [Glide Open Source Project](https://glide.sourceforge.net/) - Glide open source project.
- Graphics API: Mantle
    - 📚 [Mantle](https://en.wikipedia.org/wiki/Mantle_(API)) - Developed by _AMD_ as an alternative to Direct3D and OpenGL.
- Graphics API: Metal
    - 🌎 [Metal](https://developer.apple.com/metal/) - API for developing 3D apps on _Apple_ platforms. [[Samples](https://developer.apple.com/metal/sample-code/)]
    - 📚 [Metal Tutorial](https://www.raywenderlich.com/7475-metal-tutorial-getting-started) - Learn how to get started with Metal at _RayWenderlich.com_.
- Graphics API: OpenGL
    - 📚 [Learn OpenGL](https://learnopengl.com) 🔥 - Incredible! In depth tutorials for modern graphics programming.
    - 🌎 [Mesa 3D](https://www.mesa3d.org/) - Open source implementations of OpenGL.
    - 🌎 [OpenGL](https://www.opengl.org/) - The industry's foundation for high-performance graphics.
    - 📚 [OpenGL Tutorial](https://www.opengl-tutorial.org) - Collection of OpenGL tutorials with source code examples.
- Graphics API: Vulkan
    - 🌎 [Vulkan](https://www.vulkan.org) - Modern, cross-platform graphics API. [[Samples](https://github.com/khronosGroup/Vulkan-samples) [![GitHub stars](https://img.shields.io/github/stars/khronosGroup/Vulkan-samples?style=flat)](https://github.com/khronosGroup/Vulkan-samples/stargazers)]
    - 📚 [Vulkan Tutorial](https://github.com/Overv/VulkanTutorial) [![GitHub stars](https://img.shields.io/github/stars/Overv/VulkanTutorial?style=flat)](https://github.com/Overv/VulkanTutorial/stargazers) - Teaches the basics of using Vulkan graphics and compute API.
- Graphics API: WebGL
    - 🌎 [WebGL](https://www.khronos.org/webgl/) - Open web standard 3D graphics API. [[GitHub](https://github.com/KhronosGroup/WebGL) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/WebGL?style=flat)](https://github.com/KhronosGroup/WebGL/stargazers)]
    - 📚 [WebGL Fundamentals](https://webglfundamentals.org) 🔥 - Full understanding of what WebGL really is and how it works.
    - 📚 [WebGL 2 Fundamentals](https://webgl2fundamentals.org) - Updated to use the WebGL2 standard.
    - 📚 [WebGL 2 Samples](https://github.com/WebGLSamples/WebGL2Samples) [![GitHub stars](https://img.shields.io/github/stars/WebGLSamples/WebGL2Samples?style=flat)](https://github.com/WebGLSamples/WebGL2Samples/stargazers) - Short and easy to understand samples demonstrating WebGL 2 features.
    - 📚 [WebGL Tutorial](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial) - How to use the canvas element to draw WebGL graphics.
- Graphics API: WebGPU
    - 📚 [Learn WebGPU](https://eliemichel.github.io/LearnWebGPU/) - WebGPU graphics API walk-through.
    - 🌎 [WebGPU](https://github.com/gpuweb/gpuweb/wiki/Implementation-Status) [![GitHub stars](https://img.shields.io/github/stars/gpuweb/gpuweb/wiki/Implementation-Status?style=flat)](https://github.com/gpuweb/gpuweb/wiki/Implementation-Status/stargazers) - Next generation web 3D graphics API. [[GitHub](https://github.com/gpuweb/gpuweb) [![GitHub stars](https://img.shields.io/github/stars/gpuweb/gpuweb?style=flat)](https://github.com/gpuweb/gpuweb/stargazers)]
    - 🌎 [WebGPU Demos](https://webkit.org/demos/webgpu/) - Collection of simple WebGPU examples by _Apple_.
    - 📚 [WebGPU Fundamentals](https://webgpufundamentals.org/) - Set of articles to help learn WebGPU.
- Pipeline: GPGPU
    - 🌎 [CUDA](https://developer.nvidia.com/cuda-zone) - Developed by _NVIDIA_ for parallel computing and programming.
    - 📚 [DirectCompute](https://en.wikipedia.org/wiki/DirectCompute) - Developed by _Microsoft_ for using compute shaders with DirectX 10 & 11.
    - 🌎 [OpenCL](https://www.khronos.org/opencl/) - For writing programs that execute across CPUs, GPUs, and other processors.
- Platform: XNA
    - 📚 [RB Whitaker's Wiki](http://rbwhitaker.wikidot.com/) - Tutorials on C#, MonoGame, XNA, and more.
    - 📚 [Riemer's MonoGame Tutorials](https://github.com/SimonDarksideJ/XNAGameStudio/wiki/RiemersArchiveOverview) [![GitHub stars](https://img.shields.io/github/stars/SimonDarksideJ/XNAGameStudio/wiki/RiemersArchiveOverview?style=flat)](https://github.com/SimonDarksideJ/XNAGameStudio/wiki/RiemersArchiveOverview/stargazers) - Everything you need to start programming with MonoGame.
    - 📚 [XNA Game Studio Archive](https://github.com/SimonDarksideJ/XNAGameStudio) [![GitHub stars](https://img.shields.io/github/stars/SimonDarksideJ/XNAGameStudio?style=flat)](https://github.com/SimonDarksideJ/XNAGameStudio/stargazers) 🔥 - Required visit for [MonoGame](https://en.wikipedia.org/wiki/MonoGame) / [FNA](https://fna-xna.github.io/) / [XNA](https://en.wikipedia.org/wiki/Microsoft_XNA) developers.

### Engine Development
- Blog Articles
    - 📚 [How to Become a Game Engine Developer](https://www.haroldserrano.com/blog/how-to-become-a-game-engine-developer) - Starting point on game engine development.
- Books
    - 📚 [Data-Oriented Design](https://www.dataorienteddesign.com/dodbook/) - Practical methodology that reduces complexity, improves performance.
    - 📚 [Game Engine Architecture](https://www.gameenginebook.com) - Theory and practice of game engine development.
    - 📚 [Game Engine Black Book: DOOM](https://fabiensanglard.net/gebbdoom/) - History, engineering, and development of the _Doom_ engine.
- Commercial Studios Research Divisions
    - 🌎 [Activision Research](https://research.activision.com/) - Blog posts, articles and presentations from research within _Activision_.
    - 🌎 [EA Technology](https://www.ea.com/technology/research) - Research on game tech including info on the _Frostbite_ engine.
    - 🌎 [tri-Ace Research](https://research.tri-ace.com/) - Publications from the Research and Development Department at _tri-Ace Inc_.
    - 🌎 [Ubisoft Technology](https://www.ubisoft.com/en-us/company/how-we-make-games/technology) - Learn about in-house tech including the _Anvil_ and _Snowdrop_ engines.
- Education Portals
    - 📚 [3D Game Engine Programming](https://www.3dgep.com) - Articles on graphics, physics, AI, I/O and more.

### Game Development
- Awesome Collections
    - 📚 [Awesome Gamedev](https://github.com/Calinou/awesome-gamedev) [![GitHub stars](https://img.shields.io/github/stars/Calinou/awesome-gamedev?style=flat)](https://github.com/Calinou/awesome-gamedev/stargazers) - Collection of free resources for making games.
    - 📚 [GameDev-Resources](https://github.com/Kavex/GameDev-Resources) [![GitHub stars](https://img.shields.io/github/stars/Kavex/GameDev-Resources?style=flat)](https://github.com/Kavex/GameDev-Resources/stargazers) - Wonderful list of game development resources.
    - 📚 [Magic Tools](https://github.com/ellisonleao/magictools) [![GitHub stars](https://img.shields.io/github/stars/ellisonleao/magictools?style=flat)](https://github.com/ellisonleao/magictools/stargazers) - List of game development resources to make magic happen.
    - 🌎 [Web Game Dev](https://www.webgamedev.com) - Resources on techniques and tools around JavaScript game development.
- Books
    - 📚 [Art of Game Design](https://www.amazon.com/Art-Game-Design-Book-Lenses/dp/0123694965) - Teaches game design in an accessible manner.
    - 📚 [Game Programming Patterns](https://gameprogrammingpatterns.com) - Patterns found in games that make code easier to understand.
- Developer Portals
    - 🌎 [Game Developer](https://www.gamedeveloper.com) - Industry blogs, events, jobs, updates and more. Formerly _Gamasutra_.
    - 🌎 [GameDev.net](https://www.gamedev.net/) - Game dev forums, tutorials, blogs, projects, portfolios, and news.
    - 🌎 [GameFromScratch.com](https://gamefromscratch.com) - Game dev news, tutorials and much more.
    - 🌎 [itch.io](https://itch.io) - Game dev resources and platform to showcase / promote / buy & sell games.
- Education Portals
    - 🌎 [Lazy Foo' Tutorials](https://lazyfoo.net/tutorials/SDL/) - Beginning game programming with SDL.

### Graphical User Interface
- 📚 [List of Widget Toolkits](https://en.wikipedia.org/wiki/List_of_widget_toolkits) - Gui frameworks across all platforms and languages.

### Programming
- 📚 [Big-O Cheat Sheet](https://www.bigocheatsheet.com) - Big-O complexities of algorithms used in computer science.
- 🌎 [Deadlock Empire](https://deadlockempire.github.io/#menu) - Interactive tutorial to master threads and concurrency.
- 📚 [Every Programmer Should Know](https://github.com/mtdvio/every-programmer-should-know) [![GitHub stars](https://img.shields.io/github/stars/mtdvio/every-programmer-should-know?style=flat)](https://github.com/mtdvio/every-programmer-should-know/stargazers) - Technical things every developer should know.
- 📚 [Games of Coding](https://github.com/michelpereira/awesome-games-of-coding) [![GitHub stars](https://img.shields.io/github/stars/michelpereira/awesome-games-of-coding?style=flat)](https://github.com/michelpereira/awesome-games-of-coding/stargazers) - Games that teach you a programming language.
- 🌎 [Geeks for Geeks](https://www.geeksforgeeks.org) - Tutorials, articles, courses, coding competitions, jobs and more.
- 📚 [Learn to Program](https://github.com/karlhorky/learn-to-program) [![GitHub stars](https://img.shields.io/github/stars/karlhorky/learn-to-program?style=flat)](https://github.com/karlhorky/learn-to-program/stargazers) - Educational resources to learn to program.
- 📚 [TIOBE Index](https://www.tiobe.com/tiobe-index/) - Popularity of programming languages, updated monthly.

<br />
<br />

## Libraries
_Language specific game engine development libraries / frameworks / code._

### BASIC
- 📚 [Awesome Basic](https://github.com/JohnBlood/awesome-basic) [![GitHub stars](https://img.shields.io/github/stars/JohnBlood/awesome-basic?style=flat)](https://github.com/JohnBlood/awesome-basic/stargazers) - List of awesome BASIC dialects, IDEs, and tutorials.
- BASIC: App Framework
    - 💰 [Basic for Qt](https://www.q7basic.org/index.html) - BASIC language and environment built with _Qt_. Formerly _Q7Basic_.
    - 🎉 [QB64](https://github.com/QB64Team/qb64) [![GitHub stars](https://img.shields.io/github/stars/QB64Team/qb64?style=flat)](https://github.com/QB64Team/qb64/stargazers) - Modern BASIC+OpenGL language, retains _QBasic_ / _QB4.5_ compatibility.
    - 📚 [Visual Basic](https://learn.microsoft.com/en-us/dotnet/visual-basic/) - Object-oriented language for Windows by _Microsoft_.
- BASIC: Game Framework
    - 🎉 [Dark Basic](https://github.com/TheGameCreators/Dark-Basic-Pro) [![GitHub stars](https://img.shields.io/github/stars/TheGameCreators/Dark-Basic-Pro?style=flat)](https://github.com/TheGameCreators/Dark-Basic-Pro/stargazers) - BASIC programming language for creating apps and games. [[Website](https://www.thegamecreators.com/product/dark-basic-pro-open-source)]

### C
- 📚 [Awesome C](https://github.com/oz123/awesome-c) [![GitHub stars](https://img.shields.io/github/stars/oz123/awesome-c?style=flat)](https://github.com/oz123/awesome-c/stargazers) - List of awesome C frameworks, libraries, resources and other shiny things.
- 📚 [Learn C Programming](https://www.programiz.com/c-programming) - Excellent tutorials that will guide you to learn C programming.
- C: App Framework
    - 🎉 [Allegro](https://github.com/liballeg/allegro5) [![GitHub stars](https://img.shields.io/github/stars/liballeg/allegro5?style=flat)](https://github.com/liballeg/allegro5/stargazers) - Cross-platform library aimed at video game and multimedia apps.
    - 🎉 [glfw](https://github.com/glfw/glfw) [![GitHub stars](https://img.shields.io/github/stars/glfw/glfw?style=flat)](https://github.com/glfw/glfw/stargazers) - Cross-platform API for windowing, graphics contexts, input and events.
    - 🎉 [MiniFB](https://github.com/emoon/minifb) [![GitHub stars](https://img.shields.io/github/stars/emoon/minifb?style=flat)](https://github.com/emoon/minifb/stargazers) - Creates a cross-platform frame buffer for drawing pixels.
    - 🎉 [SDL](https://github.com/libsdl-org/SDL) [![GitHub stars](https://img.shields.io/github/stars/libsdl-org/SDL?style=flat)](https://github.com/libsdl-org/SDL/stargazers) 🔥 - Low-level access to audio, keyboard, mouse, joystick, and graphics hardware.
    - 🎉 [Sokol](https://github.com/floooh/sokol) [![GitHub stars](https://img.shields.io/github/stars/floooh/sokol?style=flat)](https://github.com/floooh/sokol/stargazers) 🔥 - Single-file libraries for graphics, windowing, file handling, audio and more.
- C: Audio
    - ⭐ [Miniaudio](https://github.com/mackron/miniaudio) [![GitHub stars](https://img.shields.io/github/stars/mackron/miniaudio?style=flat)](https://github.com/mackron/miniaudio/stargazers) - Single-file audio playback and capture library.
    - 🎉 [SDL_mixer](https://github.com/libsdl-org/SDL_mixer) [![GitHub stars](https://img.shields.io/github/stars/libsdl-org/SDL_mixer?style=flat)](https://github.com/libsdl-org/SDL_mixer/stargazers) - Audio mixer that supports various file formats for SDL.
    - 🎉 [SoLoud](https://github.com/jarikomppa/soloud) [![GitHub stars](https://img.shields.io/github/stars/jarikomppa/soloud?style=flat)](https://github.com/jarikomppa/soloud/stargazers) 🔥 - Free, easy, portable audio engine for games.
- C: Cross-Platform
    - 🎉 [Cosmopolitan](https://github.com/jart/cosmopolitan) [![GitHub stars](https://img.shields.io/github/stars/jart/cosmopolitan?style=flat)](https://github.com/jart/cosmopolitan/stargazers) - Build-once run-anywhere C library.
- C: Entity Component System
    - 🎉 [Flecs](https://github.com/SanderMertens/flecs) [![GitHub stars](https://img.shields.io/github/stars/SanderMertens/flecs?style=flat)](https://github.com/SanderMertens/flecs/stargazers) - Fast and lightweight entity component system in C99.
- C: File Formats
    - 🎉 [Assimp](https://github.com/assimp/assimp) [![GitHub stars](https://img.shields.io/github/stars/assimp/assimp?style=flat)](https://github.com/assimp/assimp/stargazers) - Open Asset Importer Library. Loads 40+ 3D file formats.
    - 🎉 [cgltf](https://github.com/jkuhlmann/cgltf) [![GitHub stars](https://img.shields.io/github/stars/jkuhlmann/cgltf?style=flat)](https://github.com/jkuhlmann/cgltf/stargazers) - Single-file glTF 2.0 loader and writer in C99.
    - ⭐ [dr_libs](https://github.com/mackron/dr_libs) [![GitHub stars](https://img.shields.io/github/stars/mackron/dr_libs?style=flat)](https://github.com/mackron/dr_libs/stargazers) - Single-file audio decoding libraries.
    - 🎉 [Libspng](https://github.com/randy408/libspng) [![GitHub stars](https://img.shields.io/github/stars/randy408/libspng?style=flat)](https://github.com/randy408/libspng/stargazers) - Simple, modern libpng alternative.
    - 🎉 [Miniz](https://github.com/richgel999/miniz) [![GitHub stars](https://img.shields.io/github/stars/richgel999/miniz?style=flat)](https://github.com/richgel999/miniz/stargazers) - Single-file drop-in replacement for zlib's most used APIs (_libpng_ and _libzip_).
    - 🎉 [OBJ GL Loader v2](https://github.com/karolek471/objgl) [![GitHub stars](https://img.shields.io/github/stars/karolek471/objgl?style=flat)](https://github.com/karolek471/objgl/stargazers) - Quite fast wavefront OBJ loader for OpenGL.
    - 🎉 [PL_MPEG](https://github.com/phoboslab/pl_mpeg) [![GitHub stars](https://img.shields.io/github/stars/phoboslab/pl_mpeg?style=flat)](https://github.com/phoboslab/pl_mpeg/stargazers) - Single-file library for decoding MPEG1 Video and MP2 Audio.
    - 🎉 [QOI](https://github.com/phoboslab/qoi) [![GitHub stars](https://img.shields.io/github/stars/phoboslab/qoi?style=flat)](https://github.com/phoboslab/qoi/stargazers) - The “Quite OK Image Format” for fast, lossless image compression.
    - ⭐ [stb_vorbis](https://github.com/nothings/stb/blob/master/stb_vorbis.c) [![GitHub stars](https://img.shields.io/github/stars/nothings/stb/blob/master/stb_vorbis.c?style=flat)](https://github.com/nothings/stb/blob/master/stb_vorbis.c/stargazers) - Ogg Vorbis audio decoder.
- C: File System
    - 🎉 [HexEmbed](https://github.com/codeplea/hexembed) [![GitHub stars](https://img.shields.io/github/stars/codeplea/hexembed?style=flat)](https://github.com/codeplea/hexembed/stargazers) - Small utility to help embed files in C/C++ programs in an easy, cross-platform way.
    - ⭐ [Incbin](https://github.com/graphitemaster/incbin) [![GitHub stars](https://img.shields.io/github/stars/graphitemaster/incbin?style=flat)](https://github.com/graphitemaster/incbin/stargazers) - Include binary and text files in your C/C++ apps with ease.
    - 🎉 [PhysicsFS](https://github.com/icculus/physfs) [![GitHub stars](https://img.shields.io/github/stars/icculus/physfs?style=flat)](https://github.com/icculus/physfs/stargazers) - Portable, flexible file I/O abstraction. Provides access to various archives.
    - ⭐ [Where Am I](https://github.com/gpakosz/whereami) [![GitHub stars](https://img.shields.io/github/stars/gpakosz/whereami?style=flat)](https://github.com/gpakosz/whereami/stargazers) - Locates the current path on the local file system.
- C: Fonts
    - 🎉 [Font Stash](https://github.com/memononen/fontstash) [![GitHub stars](https://img.shields.io/github/stars/memononen/fontstash?style=flat)](https://github.com/memononen/fontstash/stargazers) - Lightweight library that uses stb_truetype to render fonts to a texture atlas.
    - 🎉 [IconFontCppHeaders](https://github.com/juliettef/IconFontCppHeaders) [![GitHub stars](https://img.shields.io/github/stars/juliettef/IconFontCppHeaders?style=flat)](https://github.com/juliettef/IconFontCppHeaders/stargazers) - C/C++ headers and C# classes for icon fonts.
    - ⭐ [stb_truetype](https://github.com/nothings/stb/blob/master/stb_truetype.h) [![GitHub stars](https://img.shields.io/github/stars/nothings/stb/blob/master/stb_truetype.h?style=flat)](https://github.com/nothings/stb/blob/master/stb_truetype.h/stargazers) - Single-header file library that processes TrueType font files.
    - 🎉 [Vertext](https://github.com/kevinmkchin/vertext) [![GitHub stars](https://img.shields.io/github/stars/kevinmkchin/vertext?style=flat)](https://github.com/kevinmkchin/vertext/stargazers) - Generates vertices for rendering text, requires stb_truetype.
- C: Game Engine w/Editor
    - ⭐ [AVA](https://github.com/r-lyeh/AVA) [![GitHub stars](https://img.shields.io/github/stars/r-lyeh/AVA?style=flat)](https://github.com/r-lyeh/AVA/stargazers) - Tiny, minimalistic 3D game engine.
    - 🎉 [TIC-80](https://github.com/nesbox/TIC-80) [![GitHub stars](https://img.shields.io/github/stars/nesbox/TIC-80?style=flat)](https://github.com/nesbox/TIC-80/stargazers) - Virtual computer for making & sharing tiny games. [[Website](https://tic80.com/)]
- C: Game Framework
    - 🎉 [CGL](https://github.com/Jaysmito101/cgl) [![GitHub stars](https://img.shields.io/github/stars/Jaysmito101/cgl?style=flat)](https://github.com/Jaysmito101/cgl/stargazers) - Single-header file, lots of graphics & utility functions.
    - 🎉 [DOME](https://github.com/domeengine/dome) [![GitHub stars](https://img.shields.io/github/stars/domeengine/dome?style=flat)](https://github.com/domeengine/dome/stargazers) - Melds SDL2 and the Wren scripting language. [[Website](https://domeengine.com/)]
    - 🎉 [Entrypoint](https://github.com/jimon/entrypoint) [![GitHub stars](https://img.shields.io/github/stars/jimon/entrypoint?style=flat)](https://github.com/jimon/entrypoint/stargazers) - Lightweight entry point for games.
    - ⭐ [FWK](https://github.com/r-lyeh/FWK) [![GitHub stars](https://img.shields.io/github/stars/r-lyeh/FWK?style=flat)](https://github.com/r-lyeh/FWK/stargazers) - 3D game framework.
    - 🎉 [Gunslinger](https://github.com/MrFrenik/gunslinger) [![GitHub stars](https://img.shields.io/github/stars/MrFrenik/gunslinger?style=flat)](https://github.com/MrFrenik/gunslinger/stargazers) - Header-only C99 framework for multimedia apps.
    - 🎉 [RayLib](https://github.com/raysan5/raylib) [![GitHub stars](https://img.shields.io/github/stars/raysan5/raylib?style=flat)](https://github.com/raysan5/raylib/stargazers) 🔥 - Simple and easy-to-use library to enjoy 2D/3D videogame programming.
- C: Geometry
    - 🎉 [Blob](https://github.com/BlockoS/blob) [![GitHub stars](https://img.shields.io/github/stars/BlockoS/blob?style=flat)](https://github.com/BlockoS/blob/stargazers) - Single-header implementation of a contour tracing algorithm.
    - 🎉 [Marching Squares](https://github.com/prideout/par/blob/master/par_msquares.h) [![GitHub stars](https://img.shields.io/github/stars/prideout/par/blob/master/par_msquares.h?style=flat)](https://github.com/prideout/par/blob/master/par_msquares.h/stargazers) - Convert images into triangles. [[Info](https://prideout.net/marching-squares)]
    - 🎉 [Octasphere](https://github.com/prideout/par/blob/master/par_octasphere.h) [![GitHub stars](https://img.shields.io/github/stars/prideout/par/blob/master/par_octasphere.h?style=flat)](https://github.com/prideout/par/blob/master/par_octasphere.h/stargazers) - Generates triangle meshes for spheres, boxes, and capsules. [[Info](https://prideout.net/blog/octasphere/)]
    - 🎉 [Par_Shapes](https://github.com/prideout/par/blob/master/par_shapes.h) [![GitHub stars](https://img.shields.io/github/stars/prideout/par/blob/master/par_shapes.h?style=flat)](https://github.com/prideout/par/blob/master/par_shapes.h/stargazers) - Triangle meshes including solids, spheres and more. [[Info](https://prideout.net/shapes)]
    - 🎉 [Par_Streamlines](https://github.com/prideout/par/blob/master/par_streamlines.h) [![GitHub stars](https://img.shields.io/github/stars/prideout/par/blob/master/par_streamlines.h?style=flat)](https://github.com/prideout/par/blob/master/par_streamlines.h/stargazers) - Triangulating thick lines, béziers, streamlines. [[Demo](https://github.com/prideout/streamlines_demo) [![GitHub stars](https://img.shields.io/github/stars/prideout/streamlines_demo?style=flat)](https://github.com/prideout/streamlines_demo/stargazers) | [Info](https://prideout.net/blog/par_streamlines/)]
- C: Graphics - 2D
    - 🎉 [NanoVG](https://github.com/memononen/nanovg) [![GitHub stars](https://img.shields.io/github/stars/memononen/nanovg?style=flat)](https://github.com/memononen/nanovg/stargazers) - OpenGL-based 2D vector drawing library for UI and visualizations.
    - 🎉 [Tilengine](https://github.com/megamarc/Tilengine) [![GitHub stars](https://img.shields.io/github/stars/megamarc/Tilengine?style=flat)](https://github.com/megamarc/Tilengine/stargazers) - 2D graphics with raster effects for retro style game development.
- C: Graphics - 3D
    - 🎉 [Sokol Gfx](https://github.com/floooh/sokol/blob/master/sokol_gfx.h) [![GitHub stars](https://img.shields.io/github/stars/floooh/sokol/blob/master/sokol_gfx.h?style=flat)](https://github.com/floooh/sokol/blob/master/sokol_gfx.h/stargazers) - Cross-platform, single-file graphics. [[Examples](https://floooh.github.io/sokol-html5/)]
    - 🎉 [Sokol Graphics Painter](https://github.com/edubart/sokol_gp) [![GitHub stars](https://img.shields.io/github/stars/edubart/sokol_gp?style=flat)](https://github.com/edubart/sokol_gp/stargazers) - 2D graphics painter implemented with _Sokol_.
    - 🎉 [wgpu-native](https://github.com/gfx-rs/wgpu-native) [![GitHub stars](https://img.shields.io/github/stars/gfx-rs/wgpu-native?style=flat)](https://github.com/gfx-rs/wgpu-native/stargazers) - Native WebGPU implementation based on _wgpu-core_.
- C: Gui
    - 🎉 [cImgui](https://github.com/cimgui/cimgui) [![GitHub stars](https://img.shields.io/github/stars/cimgui/cimgui?style=flat)](https://github.com/cimgui/cimgui/stargazers) - Thin C wrapper generated for Dear ImGui.
    - 🎉 [lvgl](https://github.com/lvgl/lvgl) [![GitHub stars](https://img.shields.io/github/stars/lvgl/lvgl?style=flat)](https://github.com/lvgl/lvgl/stargazers) 🔥 - Embedded gui library, many widgets and advanced visual effects.
    - 🎉 [NAppGUI](https://github.com/frang75/nappgui_src) [![GitHub stars](https://img.shields.io/github/stars/frang75/nappgui_src?style=flat)](https://github.com/frang75/nappgui_src/stargazers) - Professional, well documented SDK to build desktop apps.
    - 🎉 [Native File Dialog](https://github.com/mlabbe/nativefiledialog) [![GitHub stars](https://img.shields.io/github/stars/mlabbe/nativefiledialog?style=flat)](https://github.com/mlabbe/nativefiledialog/stargazers) - Portably invoke native file open / save dialogs.
    - 🎉 [Nuklear](https://github.com/Immediate-Mode-UI/Nuklear) [![GitHub stars](https://img.shields.io/github/stars/Immediate-Mode-UI/Nuklear?style=flat)](https://github.com/Immediate-Mode-UI/Nuklear/stargazers) - Single-header immediate mode cross-platform gui library.
- C: Input
    - 🎉 [libGamepad](https://github.com/mtwilliams/libgamepad) [![GitHub stars](https://img.shields.io/github/stars/mtwilliams/libgamepad?style=flat)](https://github.com/mtwilliams/libgamepad/stargazers) - Cross-platform library for gamepad input.
    - 🎉 [Sokol Gamepad](https://github.com/floooh/sokol/pull/393/commits/26a9da9dafd4adb22a1ace0de0d2569da31ae427) [![GitHub stars](https://img.shields.io/github/stars/floooh/sokol/pull/393/commits/26a9da9dafd4adb22a1ace0de0d2569da31ae427?style=flat)](https://github.com/floooh/sokol/pull/393/commits/26a9da9dafd4adb22a1ace0de0d2569da31ae427/stargazers) - Branch with addon support for gamepads in _Sokol_.
- C: Layout
    - 🎉 [Clay](https://github.com/nicbarker/clay) [![GitHub stars](https://img.shields.io/github/stars/nicbarker/clay?style=flat)](https://github.com/nicbarker/clay/stargazers) - High performance 2D UI layout library.
- C: Libraries
    - ⭐ [Cute Headers](https://github.com/RandyGaul/cute_headers) [![GitHub stars](https://img.shields.io/github/stars/RandyGaul/cute_headers?style=flat)](https://github.com/RandyGaul/cute_headers/stargazers) - Single-file libraries primarily used for games, by [Randy Gaul](https://github.com/RandyGaul) [![GitHub stars](https://img.shields.io/github/stars/RandyGaul?style=flat)](https://github.com/RandyGaul/stargazers).
    - ⭐ [Libs](https://github.com/mattiasgustavsson/libs) [![GitHub stars](https://img.shields.io/github/stars/mattiasgustavsson/libs?style=flat)](https://github.com/mattiasgustavsson/libs/stargazers) - Single-file public domain libraries for C/C++, by [Mattias Gustavsson](https://github.com/mattiasgustavsson) [![GitHub stars](https://img.shields.io/github/stars/mattiasgustavsson?style=flat)](https://github.com/mattiasgustavsson/stargazers).
    - ⭐ [Pico Headers](https://github.com/empyreanx/pico_headers) [![GitHub stars](https://img.shields.io/github/stars/empyreanx/pico_headers?style=flat)](https://github.com/empyreanx/pico_headers/stargazers) - Single-file, cross-platform libraries for game development.
    - 📚 [Single-file Libs](https://github.com/nothings/single_file_libs) [![GitHub stars](https://img.shields.io/github/stars/nothings/single_file_libs?style=flat)](https://github.com/nothings/single_file_libs/stargazers) - Amazing collection of single-file C/C++ libraries compiled from many authors.
    - ⭐ [stb](https://github.com/nothings/stb) [![GitHub stars](https://img.shields.io/github/stars/nothings/stb?style=flat)](https://github.com/nothings/stb/stargazers) 🔥 - Single-file public domain libraries for C/C++, by [Sean Barrett](https://github.com/nothings) [![GitHub stars](https://img.shields.io/github/stars/nothings?style=flat)](https://github.com/nothings/stargazers).
- C: Lighting
    - ⭐ [Light Mapper](https://github.com/ands/lightmapper) [![GitHub stars](https://img.shields.io/github/stars/ands/lightmapper?style=flat)](https://github.com/ands/lightmapper/stargazers) - Single-file library for lightmap baking by using your existing OpenGL renderer.
- C: Math
    - 🎉 [Cglm](https://github.com/recp/cglm) [![GitHub stars](https://img.shields.io/github/stars/recp/cglm?style=flat)](https://github.com/recp/cglm/stargazers) - Highly optimized OpenGL math.
    - ⭐ [Handmade Math](https://github.com/HandmadeMath/Handmade-Math) [![GitHub stars](https://img.shields.io/github/stars/HandmadeMath/Handmade-Math?style=flat)](https://github.com/HandmadeMath/Handmade-Math/stargazers) 🔥 - Simple, public domain math library for games and computer graphics.
    - 🎉 [Kazmath](https://github.com/Kazade/kazmath) [![GitHub stars](https://img.shields.io/github/stars/Kazade/kazmath?style=flat)](https://github.com/Kazade/kazmath/stargazers) - Math library targeted at games.
    - 🎉 [Raymath](https://github.com/raysan5/raylib/blob/master/src/raymath.h) [![GitHub stars](https://img.shields.io/github/stars/raysan5/raylib/blob/master/src/raymath.h?style=flat)](https://github.com/raysan5/raylib/blob/master/src/raymath.h/stargazers) - Math library included in the _RayLib_ game framework.
- C: Network
    - 🎉 [ENet](https://github.com/zpl-c/enet) [![GitHub stars](https://img.shields.io/github/stars/zpl-c/enet?style=flat)](https://github.com/zpl-c/enet/stargazers) - Simple, lightweight and reliable UDP networking library.
    - 🎉 [librg](https://github.com/zpl-c/librg) [![GitHub stars](https://img.shields.io/github/stars/zpl-c/librg?style=flat)](https://github.com/zpl-c/librg/stargazers) - Middleware between networking / file-streaming libraries and app logic.
    - 🎉 [netcode](https://github.com/mas-bandwidth/netcode) [![GitHub stars](https://img.shields.io/github/stars/mas-bandwidth/netcode?style=flat)](https://github.com/mas-bandwidth/netcode/stargazers) - Secure client/server protocol for multiplayer games built on top of UDP.
- C: Physics
    - 🎉 [Chipmunk](https://github.com/slembcke/Chipmunk2D) [![GitHub stars](https://img.shields.io/github/stars/slembcke/Chipmunk2D?style=flat)](https://github.com/slembcke/Chipmunk2D/stargazers) - Fast, lightweight 2D game physics library.
- C: Scripting
    - 🎉 [Duktape](https://github.com/svaarala/duktape) [![GitHub stars](https://img.shields.io/github/stars/svaarala/duktape?style=flat)](https://github.com/svaarala/duktape/stargazers) - Embeddable JavaScript engine with a focus on portability and compact footprint.
    - 🎉 [JerryScript](https://github.com/jerryscript-project/jerryscript) [![GitHub stars](https://img.shields.io/github/stars/jerryscript-project/jerryscript?style=flat)](https://github.com/jerryscript-project/jerryscript/stargazers) - Ultra-lightweight JavaScript engine for the Internet of Things.
    - 🎉 [Lua](https://github.com/lua/lua) [![GitHub stars](https://img.shields.io/github/stars/lua/lua?style=flat)](https://github.com/lua/lua/stargazers) - Powerful, efficient, lightweight, embeddable scripting language.
    - 🎉 [QuickJS](https://github.com/bellard/quickjs) [![GitHub stars](https://img.shields.io/github/stars/bellard/quickjs?style=flat)](https://github.com/bellard/quickjs/stargazers) - Small and embeddable JavaScript engine.

### C++
- 📚 [Awesome C++](https://github.com/fffaraz/awesome-cpp) [![GitHub stars](https://img.shields.io/github/stars/fffaraz/awesome-cpp?style=flat)](https://github.com/fffaraz/awesome-cpp/stargazers) - List of awesome C++ frameworks, libraries, and resources.
- 📚 [Awesome C++ Game Dev](https://github.com/Caerind/AwesomeCppGameDev) [![GitHub stars](https://img.shields.io/github/stars/Caerind/AwesomeCppGameDev?style=flat)](https://github.com/Caerind/AwesomeCppGameDev/stargazers) - List of awesome C++ things for Game Development.
- 📚 [Awesome Hpp](https://github.com/p-ranav/awesome-hpp) [![GitHub stars](https://img.shields.io/github/stars/p-ranav/awesome-hpp?style=flat)](https://github.com/p-ranav/awesome-hpp/stargazers) - List of awesome header-only C++ libraries.
- 🌎 [C++ Papyrus](https://caiorss.github.io/C-Cpp-Notes/index.html) - Basic to advanced topics with modern C++ examples.
- 🌎 [cppreference.com](https://en.cppreference.com/w/cpp) - Online reference for C, C++, and the STL.
- 📚 [Learn C++](https://www.learncpp.com) 🔥 - Walks you through all the steps to write, compile, and debug C++.
- 📚 [Modern Cpp Features](https://github.com/AnthonyCalandra/modern-cpp-features) [![GitHub stars](https://img.shields.io/github/stars/AnthonyCalandra/modern-cpp-features?style=flat)](https://github.com/AnthonyCalandra/modern-cpp-features/stargazers) - Cheatsheet of modern C++ language and library features.
- C++: App Framework
    - 🎉 [Cinder](https://github.com/cinder/Cinder) [![GitHub stars](https://img.shields.io/github/stars/cinder/Cinder?style=flat)](https://github.com/cinder/Cinder/stargazers) - App / graphics library for macOS, Windows, Linux, iOS. [[Website](https://libcinder.org)]
    - 🎉 [Cross Window](https://github.com/alaingalvan/CrossWindow) [![GitHub stars](https://img.shields.io/github/stars/alaingalvan/CrossWindow?style=flat)](https://github.com/alaingalvan/CrossWindow/stargazers) - Platform library for managing windows and other OS tasks.
    - 🎉 [SFML](https://github.com/SFML/SFML) [![GitHub stars](https://img.shields.io/github/stars/SFML/SFML?style=flat)](https://github.com/SFML/SFML/stargazers) 🔥 - Cross-platform access to windowing, graphics, audio and networking.
- C++: Animation
    - 🎉 [Ozz-Animation](https://github.com/guillaumeblanc/ozz-animation) [![GitHub stars](https://img.shields.io/github/stars/guillaumeblanc/ozz-animation?style=flat)](https://github.com/guillaumeblanc/ozz-animation/stargazers) - Skeletal animation library and toolset.
    - 🎉 [Tweeny](https://github.com/mobius3/tweeny) [![GitHub stars](https://img.shields.io/github/stars/mobius3/tweeny?style=flat)](https://github.com/mobius3/tweeny/stargazers) - Inbetweening library for complex animations for games / apps.
- C++: Audio
    - 🎉 [Amplitude Audio SDK](https://github.com/SparkyStudios/AmplitudeAudioSDK) [![GitHub stars](https://img.shields.io/github/stars/SparkyStudios/AmplitudeAudioSDK?style=flat)](https://github.com/SparkyStudios/AmplitudeAudioSDK/stargazers) - Cross-platform audio engine designed for the needs of games.
    - 💰 [irrKlang](https://www.ambiera.com/irrklang/) - High level 2D/3D sound engine and audio library.
    - 💰 [Juce](https://github.com/juce-framework/JUCE) [![GitHub stars](https://img.shields.io/github/stars/juce-framework/JUCE?style=flat)](https://github.com/juce-framework/JUCE/stargazers) - The leading framework for multi-platform audio apps.
    - 🔒 [OpenAL Soft](https://github.com/kcat/openal-soft) [![GitHub stars](https://img.shields.io/github/stars/kcat/openal-soft?style=flat)](https://github.com/kcat/openal-soft/stargazers) - Software implementation of the _OpenAL_ 3D audio API.
    - 🎉 [PortAudio](https://github.com/PortAudio/portaudio) [![GitHub stars](https://img.shields.io/github/stars/PortAudio/portaudio?style=flat)](https://github.com/PortAudio/portaudio/stargazers) - Cross-platform audio library.
    - 🎉 [Steam Audio](https://github.com/ValveSoftware/steam-audio) [![GitHub stars](https://img.shields.io/github/stars/ValveSoftware/steam-audio?style=flat)](https://github.com/ValveSoftware/steam-audio/stargazers) - Cross-platform spatial audio SDK for games and VR.
- C++: Cross-Platform
    - 🌎 [emscripten](https://github.com/emscripten-core/emscripten) [![GitHub stars](https://img.shields.io/github/stars/emscripten-core/emscripten?style=flat)](https://github.com/emscripten-core/emscripten/stargazers) - The C/C++ to JavaScript (as WebAssembly) compiler. [[Website](https://emscripten.org/)]
- C++: Entity Component System
    - 🎉 [EntityX](https://github.com/alecthomas/entityx) [![GitHub stars](https://img.shields.io/github/stars/alecthomas/entityx?style=flat)](https://github.com/alecthomas/entityx/stargazers) - Fast, type-safe C++ entity component system.
    - 🎉 [Entt](https://github.com/skypjack/entt) [![GitHub stars](https://img.shields.io/github/stars/skypjack/entt?style=flat)](https://github.com/skypjack/entt/stargazers) - Gaming meets modern C++, a fast and reliable entity component system.
- C++: Fonts
    - 🎉 [HarfBuzz](https://github.com/harfbuzz/harfbuzz) [![GitHub stars](https://img.shields.io/github/stars/harfbuzz/harfbuzz?style=flat)](https://github.com/harfbuzz/harfbuzz/stargazers) - Text shaping library. Formatted and positioned glyph output.
    - 🎉 [msdfgen](https://github.com/Chlumsky/msdfgen) [![GitHub stars](https://img.shields.io/github/stars/Chlumsky/msdfgen?style=flat)](https://github.com/Chlumsky/msdfgen/stargazers) - Multi-channel signed distance field generator.
    - 💰 [Slug](http://sluglibrary.com) - High-quality, resolution-independent text and vector graphics for 3D apps.
    - 🎉 [slughorn](https://github.com/AlphaPixel/slughorn) [![GitHub stars](https://img.shields.io/github/stars/AlphaPixel/slughorn?style=flat)](https://github.com/AlphaPixel/slughorn/stargazers) - Library for shoehorning the _Slug_ text/graphics GPU rendering library into projects.
- C++: File Formats
    - ⭐ [Jpeg-Compressor](https://github.com/richgel999/jpeg-compressor) [![GitHub stars](https://img.shields.io/github/stars/richgel999/jpeg-compressor?style=flat)](https://github.com/richgel999/jpeg-compressor/stargazers) - Single-file library that writes baseline JPEG compressed images.
    - 🎉 [TinyDNG](https://github.com/syoyo/tinydng) [![GitHub stars](https://img.shields.io/github/stars/syoyo/tinydng?style=flat)](https://github.com/syoyo/tinydng/stargazers) - Header-only DNG / TIFF loader and writer.
    - 🎉 [TinyEXR](https://github.com/syoyo/tinyexr) [![GitHub stars](https://img.shields.io/github/stars/syoyo/tinyexr?style=flat)](https://github.com/syoyo/tinyexr/stargazers) - Tiny OpenEXR image loader / saver library.
    - 🎉 [TinyGLTF](https://github.com/syoyo/tinygltf) [![GitHub stars](https://img.shields.io/github/stars/syoyo/tinygltf?style=flat)](https://github.com/syoyo/tinygltf/stargazers) - Header-only C++11 tiny glTF 2.0 library.
    - 🎉 [TinyOBJLoader](https://github.com/tinyobjloader/tinyobjloader) [![GitHub stars](https://img.shields.io/github/stars/tinyobjloader/tinyobjloader?style=flat)](https://github.com/tinyobjloader/tinyobjloader/stargazers) - Tiny but powerful single-file wavefront obj loader.
- C++: File System
    - 🎉 [Imgui-Filebrowser](https://github.com/AirGuanZ/imgui-filebrowser) [![GitHub stars](https://img.shields.io/github/stars/AirGuanZ/imgui-filebrowser?style=flat)](https://github.com/AirGuanZ/imgui-filebrowser/stargazers) - Header-only file browser implementation for _Dear ImGui_ in C++17.
- C++: Game Engine w/Editor
    - 🎉 [AnKi 3D Engine](https://github.com/godlikepanos/anki-3d-engine) [![GitHub stars](https://img.shields.io/github/stars/godlikepanos/anki-3d-engine?style=flat)](https://github.com/godlikepanos/anki-3d-engine/stargazers) - Vulkan backend, modern renderer, scripting, physics and more.
    - 🔒 [Crown Engine](https://github.com/crownengine/crown) [![GitHub stars](https://img.shields.io/github/stars/crownengine/crown?style=flat)](https://github.com/crownengine/crown/stargazers) - Data-driven 3D and 2D game engine.
    - 🎉 [Crystal Engine](https://github.com/neelmewada/CrystalEngine) [![GitHub stars](https://img.shields.io/github/stars/neelmewada/CrystalEngine?style=flat)](https://github.com/neelmewada/CrystalEngine/stargazers) - Vulkan backend with PBR and styled GUI (_CrystalWidgets_).
    - 🎉 [Doriax](https://github.com/doriaxengine/doriax) [![GitHub stars](https://img.shields.io/github/stars/doriaxengine/doriax?style=flat)](https://github.com/doriaxengine/doriax/stargazers) - Cross-platform for 2D/3D projects. Formerly _Supernova_.
    - 🎉 [Drop Creator](https://github.com/scidian/drop) [![GitHub stars](https://img.shields.io/github/stars/scidian/drop?style=flat)](https://github.com/scidian/drop/stargazers) - No code, 2.5D game engine built with _Qt_, OpenGL and _Chipmunk Physics_.
    - 🔒 [Enigma](https://github.com/enigma-dev/enigma-dev) [![GitHub stars](https://img.shields.io/github/stars/enigma-dev/enigma-dev?style=flat)](https://github.com/enigma-dev/enigma-dev/stargazers) - GameMaker compatible 2D engine.
    - 🎉 [Esoterica Engine](https://github.com/BobbyAnguelov/Esoterica) [![GitHub stars](https://img.shields.io/github/stars/BobbyAnguelov/Esoterica?style=flat)](https://github.com/BobbyAnguelov/Esoterica/stargazers) - High-performance game engine with editor and AAA quality animation graph.
    - 🎉 [ezEngine](https://github.com/ezEngine/ezEngine) [![GitHub stars](https://img.shields.io/github/stars/ezEngine/ezEngine?style=flat)](https://github.com/ezEngine/ezEngine/stargazers) - Game engine in active development.
    - 🎉 [FIFE](https://github.com/fifengine/fifengine) [![GitHub stars](https://img.shields.io/github/stars/fifengine/fifengine?style=flat)](https://github.com/fifengine/fifengine/stargazers) - Multi-platform isometric game engine.
    - 🎉 [G3D Innovation Engine](https://sourceforge.net/p/g3d/code/HEAD/tree/) - Used for R&D throughout academia and industry. [[Website](https://casual-effects.com/g3d/www/index.html)].
    - 🎉 [Irrlicht](https://sourceforge.net/projects/irrlicht/) - Cross-platform 3D engine worked on for over 2 decades. [[Website](https://irrlicht.sourceforge.io/)]
    - 🎉 [Limon Engine](https://github.com/enginmanap/limonEngine) [![GitHub stars](https://img.shields.io/github/stars/enginmanap/limonEngine?style=flat)](https://github.com/enginmanap/limonEngine/stargazers) - 3D FPS game engine with full dynamic lighting and shadows.
    - 🎉 [Lina Engine](https://github.com/inanevin/LinaEngine) [![GitHub stars](https://img.shields.io/github/stars/inanevin/LinaEngine?style=flat)](https://github.com/inanevin/LinaEngine/stargazers) - Modular game engine, aimed to develop 3D desktop games.
    - 🎉 [Lumos](https://github.com/jmorton06/Lumos) [![GitHub stars](https://img.shields.io/github/stars/jmorton06/Lumos?style=flat)](https://github.com/jmorton06/Lumos/stargazers) - Cross-platform 2D/3D game engine, supports both OpenGL and Vulkan.
    - 🎉 [Lumix Engine](https://github.com/nem0/LumixEngine) [![GitHub stars](https://img.shields.io/github/stars/nem0/LumixEngine?style=flat)](https://github.com/nem0/LumixEngine/stargazers) - 3D game engine with _Dear ImGui_ based editor.
    - 🎉 [MxEngine](https://github.com/asc-community/MxEngine) [![GitHub stars](https://img.shields.io/github/stars/asc-community/MxEngine?style=flat)](https://github.com/asc-community/MxEngine/stargazers) - Modern-C++ general-purpose 3D game engine.
    - 🔒 [neoGFX](https://github.com/i42output/neogfx) [![GitHub stars](https://img.shields.io/github/stars/i42output/neogfx?style=flat)](https://github.com/i42output/neogfx/stargazers) - Cross-platform app and game engine.
    - 🎉 [ÖbEngine](https://github.com/ObEngine/ObEngine) [![GitHub stars](https://img.shields.io/github/stars/ObEngine/ObEngine?style=flat)](https://github.com/ObEngine/ObEngine/stargazers) - 2D engine with Lua scripting built with _SFML_.
    - 🎉 [Overload](https://github.com/adriengivry/Overload) [![GitHub stars](https://img.shields.io/github/stars/adriengivry/Overload?style=flat)](https://github.com/adriengivry/Overload/stargazers) - Well documented 3D game engine inspired by industry standards.
    - 🎉 [Razix Engine](https://github.com/Pikachuxxxx/Razix) [![GitHub stars](https://img.shields.io/github/stars/Pikachuxxxx/Razix?style=flat)](https://github.com/Pikachuxxxx/Razix/stargazers) - High-performance research engine for production pipeline.
    - 🎉 [Rootex](https://github.com/sdslabs/rootex) [![GitHub stars](https://img.shields.io/github/stars/sdslabs/rootex?style=flat)](https://github.com/sdslabs/rootex/stargazers) - Advanced C++ 3D game engine powering an in-production game.
    - 🎉 [Skylicht](https://github.com/skylicht-lab/skylicht-engine) [![GitHub stars](https://img.shields.io/github/stars/skylicht-lab/skylicht-engine?style=flat)](https://github.com/skylicht-lab/skylicht-engine/stargazers) - Upgraded features including audio, physics and particles. Built on _Irrlicht_.
    - 🎉 [Spartan Engine](https://github.com/PanosK92/SpartanEngine) [![GitHub stars](https://img.shields.io/github/stars/PanosK92/SpartanEngine?style=flat)](https://github.com/PanosK92/SpartanEngine/stargazers) - Emphasis on quality and performance.
    - 🎉 [Torque 3D](https://github.com/GarageGames/Torque3D) [![GitHub stars](https://img.shields.io/github/stars/GarageGames/Torque3D?style=flat)](https://github.com/GarageGames/Torque3D/stargazers) - High-performance 3D engine built on _The Forge_.
    - 🔒 [UPBGE](https://github.com/UPBGE/upbge) [![GitHub stars](https://img.shields.io/github/stars/UPBGE/upbge?style=flat)](https://github.com/UPBGE/upbge/stargazers) - Blender Game Engine, originally forked from _Blender_.
- C++: Game Framework
    - 🎉 [Acid](https://github.com/EQMG/Acid) [![GitHub stars](https://img.shields.io/github/stars/EQMG/Acid?style=flat)](https://github.com/EQMG/Acid/stargazers) - Modern C++17 and structured to be fast, simple, and modular.
    - 🎉 [blah](https://github.com/NoelFB/blah) [![GitHub stars](https://img.shields.io/github/stars/NoelFB/blah?style=flat)](https://github.com/NoelFB/blah/stargazers) - Small 2D game framework.
    - 🎉 [Cocos2d-x](https://github.com/cocos2d/cocos2d-x) [![GitHub stars](https://img.shields.io/github/stars/cocos2d/cocos2d-x?style=flat)](https://github.com/cocos2d/cocos2d-x/stargazers) - Widely used in indie game dev community.
    - 🎉 [Cute Framework](https://github.com/RandyGaul/cute_framework) [![GitHub stars](https://img.shields.io/github/stars/RandyGaul/cute_framework?style=flat)](https://github.com/RandyGaul/cute_framework/stargazers) - Simple and consise framework for making 2D games.
    - 🔒 [Fireworks Engine](https://github.com/Pikachuxxxx/Fireworks-Engine) [![GitHub stars](https://img.shields.io/github/stars/Pikachuxxxx/Fireworks-Engine?style=flat)](https://github.com/Pikachuxxxx/Fireworks-Engine/stargazers) - Lightweight OpenGL framework for quick prototyping.
    - 🎉 [Halley](https://github.com/amzeratul/halley) [![GitHub stars](https://img.shields.io/github/stars/amzeratul/halley?style=flat)](https://github.com/amzeratul/halley/stargazers) - Modern C++17. Used for _Wargroove_, a strategy game on desktop and consoles.
    - 🎉 [is::Engine](https://github.com/Is-Daouda/is-Engine) [![GitHub stars](https://img.shields.io/github/stars/Is-Daouda/is-Engine?style=flat)](https://github.com/Is-Daouda/is-Engine/stargazers) - 2D framework built on _SDL2_ and _SFML_.
    - 🎉 [JNGL](https://github.com/jhasse/jngl) [![GitHub stars](https://img.shields.io/github/stars/jhasse/jngl?style=flat)](https://github.com/jhasse/jngl/stargazers) - 2D framework. Develop anywhere, deploy everywhere.
    - 🔒 [KlayGE](https://github.com/gongminmin/KlayGE) [![GitHub stars](https://img.shields.io/github/stars/gongminmin/KlayGE?style=flat)](https://github.com/gongminmin/KlayGE/stargazers) - Cross-platform game framework with plugin-based architecture.
    - 🎉 [Koala Engine](https://github.com/phisko/kengine) [![GitHub stars](https://img.shields.io/github/stars/phisko/kengine?style=flat)](https://github.com/phisko/kengine/stargazers) - Framework with an ECS architecture, aka _Kengine_.
    - 🎉 [Lumino](https://github.com/LuminoEngine/Lumino) [![GitHub stars](https://img.shields.io/github/stars/LuminoEngine/Lumino?style=flat)](https://github.com/LuminoEngine/Lumino/stargazers) - Framework for building real-time graphics apps.
    - 🎉 [Nazara Engine](https://github.com/NazaraEngine/NazaraEngine) [![GitHub stars](https://img.shields.io/github/stars/NazaraEngine/NazaraEngine?style=flat)](https://github.com/NazaraEngine/NazaraEngine/stargazers) - Custom shaders, ECS, 2D/3D, networking and more.
    - 🎉 [nCine](https://github.com/nCine/nCine) [![GitHub stars](https://img.shields.io/github/stars/nCine/nCine?style=flat)](https://github.com/nCine/nCine/stargazers) - Cross-platform 2D game framework.
    - 🎉 [Octave](https://github.com/mholtkamp/octave) [![GitHub stars](https://img.shields.io/github/stars/mholtkamp/octave?style=flat)](https://github.com/mholtkamp/octave/stargazers) - 3D game engine for GameCube, Wii, 3DS, and more.
    - 🎉 [ORX](https://github.com/orx/orx) [![GitHub stars](https://img.shields.io/github/stars/orx/orx?style=flat)](https://github.com/orx/orx/stargazers) - 2.5D data-driven game development framework.
    - 🎉 [Oryol](https://github.com/floooh/oryol) [![GitHub stars](https://img.shields.io/github/stars/floooh/oryol?style=flat)](https://github.com/floooh/oryol/stargazers) - Small, 3D, portable and extensible coding framework.
    - ⭐ [Ouzel](https://github.com/elnormous/ouzel) [![GitHub stars](https://img.shields.io/github/stars/elnormous/ouzel?style=flat)](https://github.com/elnormous/ouzel/stargazers) - Public domain, targeted for development of 2D games.
    - 🎉 [Polycode](https://github.com/ivansafrin/Polycode) [![GitHub stars](https://img.shields.io/github/stars/ivansafrin/Polycode?style=flat)](https://github.com/ivansafrin/Polycode/stargazers) - Cross-platform engine for creative code.
    - 🎉 [Solar2D](https://github.com/coronalabs/corona) [![GitHub stars](https://img.shields.io/github/stars/coronalabs/corona?style=flat)](https://github.com/coronalabs/corona/stargazers) - Focus on ease of iterations and usage. Formerly _Corona_.
    - 🎉 [Thunder](https://github.com/thunder-engine/thunder) [![GitHub stars](https://img.shields.io/github/stars/thunder-engine/thunder?style=flat)](https://github.com/thunder-engine/thunder/stargazers) - Cross-platform 2D/3D with module architecture.
    - 🎉 [Two](https://github.com/hugoam/two) [![GitHub stars](https://img.shields.io/github/stars/hugoam/two?style=flat)](https://github.com/hugoam/two/stargazers) - Toolkit for rapid development of live graphical apps and games.
    - 🎉 [Urho3D](https://github.com/urho3d/Urho3D) [![GitHub stars](https://img.shields.io/github/stars/urho3d/Urho3D?style=flat)](https://github.com/urho3d/Urho3D/stargazers) - Cross-platform 2D/3D game framework.
    - 💸 [Valve Source SDK](https://github.com/ValveSoftware/source-sdk-2013) [![GitHub stars](https://img.shields.io/github/stars/ValveSoftware/source-sdk-2013?style=flat)](https://github.com/ValveSoftware/source-sdk-2013/stargazers) - The 2013 edition of the Source SDK by _[Valve Software](https://www.valvesoftware.com/)_. [[Info](https://en.wikipedia.org/wiki/Source_(game_engine)) | [Wiki](https://developer.valvesoftware.com/wiki/Source_SDK_2013)]
- C++: Geometry
    - 🎉 [CinoLib](https://github.com/mlivesu/cinolib) [![GitHub stars](https://img.shields.io/github/stars/mlivesu/cinolib?style=flat)](https://github.com/mlivesu/cinolib/stargazers) - Header-only library for processing polygonal and polyhedral meshes.
    - 🎉 [Delabella](https://github.com/msokalski/delabella) [![GitHub stars](https://img.shields.io/github/stars/msokalski/delabella?style=flat)](https://github.com/msokalski/delabella/stargazers) - Super stable 2D delaunay triangulation.
    - 🎉 [Delaunator-Cpp](https://github.com/soerendd/delaunator-cpp) [![GitHub stars](https://img.shields.io/github/stars/soerendd/delaunator-cpp?style=flat)](https://github.com/soerendd/delaunator-cpp/stargazers) - Really fast library for Delaunay triangulation of 2D points.
    - 🔒 [Easy3D](https://github.com/LiangliangNan/Easy3D) [![GitHub stars](https://img.shields.io/github/stars/LiangliangNan/Easy3D?style=flat)](https://github.com/LiangliangNan/Easy3D/stargazers) - Easy-to-use library for 3D modeling, geometry processing, and rendering.
    - 🎉 [Extrude](https://github.com/stevinz/extrude) [![GitHub stars](https://img.shields.io/github/stars/stevinz/extrude?style=flat)](https://github.com/stevinz/extrude/stargazers) - Converts 2D images into 3D extruded meshes.
    - 🔒 [Generator](https://github.com/ilmola/generator) [![GitHub stars](https://img.shields.io/github/stars/ilmola/generator?style=flat)](https://github.com/ilmola/generator/stargazers) - Procedural geometry generation library for C++11.
    - 🎉 [Geometric Tools](https://www.geometrictools.com/index.html) - Mathematics, geometry, graphics, image analysis and physics in C++14.
    - 🎉 [GeometronLib](https://github.com/LukasBanana/GeometronLib) [![GitHub stars](https://img.shields.io/github/stars/LukasBanana/GeometronLib?style=flat)](https://github.com/LukasBanana/GeometronLib/stargazers) - Meshes for 3D shapes (cube, sphere, etc.) and ray / geometry intersection.
    - 🔒 [Libigl](https://github.com/libigl/libigl) [![GitHub stars](https://img.shields.io/github/stars/libigl/libigl?style=flat)](https://github.com/libigl/libigl/stargazers) - Simple geometry processing library.
    - 🎉 [MeshOptimizer](https://github.com/zeux/meshoptimizer) [![GitHub stars](https://img.shields.io/github/stars/zeux/meshoptimizer?style=flat)](https://github.com/zeux/meshoptimizer/stargazers) - Mesh optimization library that makes meshes smaller and faster to render.
    - 🎉 [Polygon Mesh Processing Library](https://github.com/pmp-library/pmp-library) [![GitHub stars](https://img.shields.io/github/stars/pmp-library/pmp-library?style=flat)](https://github.com/pmp-library/pmp-library/stargazers) - Processing / visualizing polygon surface meshes.
    - 🎉 [PolyPartition](https://github.com/ivanfratric/polypartition) [![GitHub stars](https://img.shields.io/github/stars/ivanfratric/polypartition?style=flat)](https://github.com/ivanfratric/polypartition/stargazers) - 2D polygon partitioning and triangulation.
    - ⭐ [RamerDouglasPeucker](https://gist.github.com/TimSC/0813573d77734bcb6f2cd2cf6cc7aa51) - Reduces number of points along a 2D line.
    - 🎉 [Recast & Detour](https://github.com/recastnavigation/recastnavigation) [![GitHub stars](https://img.shields.io/github/stars/recastnavigation/recastnavigation?style=flat)](https://github.com/recastnavigation/recastnavigation/stargazers) - Navigation-mesh toolset for games.
    - 🎉 [Seam-aware Decimater](https://github.com/songrun/SeamAwareDecimater) [![GitHub stars](https://img.shields.io/github/stars/songrun/SeamAwareDecimater?style=flat)](https://github.com/songrun/SeamAwareDecimater/stargazers) - Simplifies mesh while preserving UVs.
    - 🎉 [Spheres](https://github.com/caosdoar/spheres) [![GitHub stars](https://img.shields.io/github/stars/caosdoar/spheres?style=flat)](https://github.com/caosdoar/spheres/stargazers) - Four methods to create a sphere mesh.
    - 🔒 [Trimesh2](https://gfx.cs.princeton.edu/proj/trimesh2/) - Utilities for input, output, and manipulation of 3D triangle meshes.
    - 🎉 [V-HACD](https://github.com/kmammou/v-hacd) [![GitHub stars](https://img.shields.io/github/stars/kmammou/v-hacd?style=flat)](https://github.com/kmammou/v-hacd/stargazers) - Decomposes a 3D surface into a set of "near" convex parts.
- C++: Graphics - 2D
    - 🎉 [Blend2D](https://github.com/blend2d/blend2d) [![GitHub stars](https://img.shields.io/github/stars/blend2d/blend2d?style=flat)](https://github.com/blend2d/blend2d/stargazers) - High-performance 2D vector graphics engine. [[Website](https://blend2d.com/)]
    - 🎉 [C++ Bitmap Library](https://github.com/ArashPartow/bitmap) [![GitHub stars](https://img.shields.io/github/stars/ArashPartow/bitmap?style=flat)](https://github.com/ArashPartow/bitmap/stargazers) - Featured bitmap loading and manipulation library.
    - 🎉 [QNanoPainter](https://github.com/QUItCoding/qnanopainter) [![GitHub stars](https://img.shields.io/github/stars/QUItCoding/qnanopainter?style=flat)](https://github.com/QUItCoding/qnanopainter/stargazers) - OpenGL accelerated vector drawing library for _Qt_, powered by _NanoVG_.
    - 🎉 [Skia](https://github.com/google/skia) [![GitHub stars](https://img.shields.io/github/stars/google/skia?style=flat)](https://github.com/google/skia/stargazers) - Complete 2D graphics library used in Chrome by _Google_. [[Website](https://skia.org)]
    - 🎉 [vg-renderer](https://github.com/jdryg/vg-renderer) [![GitHub stars](https://img.shields.io/github/stars/jdryg/vg-renderer?style=flat)](https://github.com/jdryg/vg-renderer/stargazers) - 2D vector graphics renderer for _Bgfx_, based on ideas from _NanoVG_.
- C++: Graphics - 3D
    - 🎉 [Bgfx](https://github.com/bkaradzic/bgfx) [![GitHub stars](https://img.shields.io/github/stars/bkaradzic/bgfx?style=flat)](https://github.com/bkaradzic/bgfx/stargazers) - Cross-platform, graphics API agnostic, rendering library.
    - 🎉 [Dawn](https://dawn.googlesource.com/dawn) - Underlying engine that powers WebGPU in _Chromium_. [[GitHub](https://github.com/google/dawn) [![GitHub stars](https://img.shields.io/github/stars/google/dawn?style=flat)](https://github.com/google/dawn/stargazers)]
    - 🎉 [Diligent Engine](https://github.com/DiligentGraphics/DiligentEngine) [![GitHub stars](https://img.shields.io/github/stars/DiligentGraphics/DiligentEngine?style=flat)](https://github.com/DiligentGraphics/DiligentEngine/stargazers) - Modern cross-platform graphics API abstraction library.
    - 🎉 [Ember](https://github.com/strah19/Ember) [![GitHub stars](https://img.shields.io/github/stars/strah19/Ember?style=flat)](https://github.com/strah19/Ember/stargazers) - Graphics framework using SDL2 and OpenGL.
    - 🎉 [Filament](https://github.com/google/filament) [![GitHub stars](https://img.shields.io/github/stars/google/filament?style=flat)](https://github.com/google/filament/stargazers) - Mobile-first, real-time physically-based renderer by _Google_.
    - 🎉 [Forge](https://github.com/ConfettiFX/The-Forge) [![GitHub stars](https://img.shields.io/github/stars/ConfettiFX/The-Forge?style=flat)](https://github.com/ConfettiFX/The-Forge/stargazers) 🔥 - Cross-platform rendering framework supporting all major platforms and consoles.
    - 🎉 [Horde3D](https://github.com/horde3d/Horde3D) [![GitHub stars](https://img.shields.io/github/stars/horde3d/Horde3D?style=flat)](https://github.com/horde3d/Horde3D/stargazers) - 3D rendering and animation engine.
    - 🎉 [Intermediate Graphics Library (IGL)](https://github.com/facebook/igl) [![GitHub stars](https://img.shields.io/github/stars/facebook/igl?style=flat)](https://github.com/facebook/igl/stargazers) - Cross-platform abstraction layer by _Facebook_.
    - 🎉 [LLGL](https://github.com/LukasBanana/LLGL) [![GitHub stars](https://img.shields.io/github/stars/LukasBanana/LLGL?style=flat)](https://github.com/LukasBanana/LLGL/stargazers) - Thin abstraction layer for OpenGL, Direct3D, Vulkan, and Metal.
    - 🎉 [Magnum Engine](https://github.com/mosra/magnum) [![GitHub stars](https://img.shields.io/github/stars/mosra/magnum?style=flat)](https://github.com/mosra/magnum/stargazers) - Modular C++11 graphics middleware for games and apps.
    - 🎉 [NVRHI](https://github.com/NVIDIA-RTX/NVRHI) [![GitHub stars](https://img.shields.io/github/stars/NVIDIA-RTX/NVRHI?style=flat)](https://github.com/NVIDIA-RTX/NVRHI/stargazers) - _NVIDIA_ abstraction layer over multiple graphics APIs.
    - 🎉 [Ogre](https://github.com/OGRECave/ogre) [![GitHub stars](https://img.shields.io/github/stars/OGRECave/ogre?style=flat)](https://github.com/OGRECave/ogre/stargazers) - Scene-oriented, flexible 3D engine.
    - 🎉 [OSRE](https://github.com/kimkulling/osre) [![GitHub stars](https://img.shields.io/github/stars/kimkulling/osre?style=flat)](https://github.com/kimkulling/osre/stargazers) - Just another "Open Source Render Engine".
    - 🔒 [StratusGFX](https://github.com/KTStephano/StratusGFX) [![GitHub stars](https://img.shields.io/github/stars/KTStephano/StratusGFX?style=flat)](https://github.com/KTStephano/StratusGFX/stargazers) - Realtime 3D rendering engine implementing modern graphics techniques.
    - 🎉 [Threepp](https://github.com/markaren/threepp) [![GitHub stars](https://img.shields.io/github/stars/markaren/threepp?style=flat)](https://github.com/markaren/threepp/stargazers) - Cross-platform C++17 port of the popular 3D JavaScript library _Three.js_ (r129).
    - 🎉 [Tungsten](https://github.com/tunabrain/tungsten) [![GitHub stars](https://img.shields.io/github/stars/tunabrain/tungsten?style=flat)](https://github.com/tunabrain/tungsten/stargazers) - High-performance physically-based renderer in C++11.
    - 🎉 [Wicked Engine](https://github.com/turanszkij/WickedEngine) [![GitHub stars](https://img.shields.io/github/stars/turanszkij/WickedEngine?style=flat)](https://github.com/turanszkij/WickedEngine/stargazers) - Engine focusing on performance & modern rendering techniques.
- C++: Gui
    - 🎉 [Crazy Eddie's GUI](https://github.com/cegui/cegui) [![GitHub stars](https://img.shields.io/github/stars/cegui/cegui?style=flat)](https://github.com/cegui/cegui/stargazers) - Versatile, multi-platform gui library.
    - 🎉 [Dear ImGui](https://github.com/ocornut/imgui) [![GitHub stars](https://img.shields.io/github/stars/ocornut/imgui?style=flat)](https://github.com/ocornut/imgui/stargazers) 🔥 - Bloat-free immediate mode gui library. Ported to many other languages.
    - 🔒 [FLTK](https://github.com/fltk/fltk) [![GitHub stars](https://img.shields.io/github/stars/fltk/fltk?style=flat)](https://github.com/fltk/fltk/stargazers) - Fast Light Toolkit, cross-platform gui. [[Website](https://www.fltk.org/)]
    - 🔒 [GTK](https://github.com/gnome/gtk) [![GitHub stars](https://img.shields.io/github/stars/gnome/gtk?style=flat)](https://github.com/gnome/gtk/stargazers) - GIMP Toolkit, a multi-platform toolkit for creating guis.
    - 🎉 [GuiLite](https://github.com/idea4good/GuiLite) [![GitHub stars](https://img.shields.io/github/stars/idea4good/GuiLite?style=flat)](https://github.com/idea4good/GuiLite/stargazers) - Header-only, cross-platform gui library.
    - 📚 [List of C++ UI Libraries](https://philippegroarke.com/posts/2018/c++_ui_solutions/) - List of C++ gui libraries, with pictures and descriptions.
    - 🎉 [Litehtml](https://github.com/litehtml/litehtml) [![GitHub stars](https://img.shields.io/github/stars/litehtml/litehtml?style=flat)](https://github.com/litehtml/litehtml/stargazers) - Lightweight HTML / CSS rendering engine.
    - 🎉 [Nana](https://github.com/cnjinhao/nana) [![GitHub stars](https://img.shields.io/github/stars/cnjinhao/nana?style=flat)](https://github.com/cnjinhao/nana/stargazers) - Cross-platform gui library in modern C++.
    - ⭐ [Portable File Dialogs](https://github.com/samhocevar/portable-file-dialogs) [![GitHub stars](https://img.shields.io/github/stars/samhocevar/portable-file-dialogs?style=flat)](https://github.com/samhocevar/portable-file-dialogs/stargazers) - Single-header C++11 native dialogs on Windows, macOS, and Linux.
    - 🔒 [Qt](https://github.com/qt) [![GitHub stars](https://img.shields.io/github/stars/qt?style=flat)](https://github.com/qt/stargazers) - Industry standard gui library. [[Awesome](https://github.com/mikeroyal/Qt-Guide) [![GitHub stars](https://img.shields.io/github/stars/mikeroyal/Qt-Guide?style=flat)](https://github.com/mikeroyal/Qt-Guide/stargazers) | [Website](https://www.qt.io)]
    - ⭐ [RmlUi](https://github.com/mikke89/RmlUi) [![GitHub stars](https://img.shields.io/github/stars/mikke89/RmlUi?style=flat)](https://github.com/mikke89/RmlUi/stargazers) - Turns HTML / CSS source files into vertices and draw commands. [[Docs](https://mikke89.github.io/RmlUiDoc/)]
    - ⭐ [Turbo Badger](https://github.com/fruxo/turbobadger) [![GitHub stars](https://img.shields.io/github/stars/fruxo/turbobadger?style=flat)](https://github.com/fruxo/turbobadger/stargazers) - Gui library for hardware accelerated apps & games. [[Oryol Example](https://floooh.github.io/oryol-samples/wasm/TurboBadgerDemo.html)]
    - 🔒 [Wt](https://github.com/emweb/wt) [![GitHub stars](https://img.shields.io/github/stars/emweb/wt?style=flat)](https://github.com/emweb/wt/stargazers) - Web gui library in modern C++. [[Website](https://www.webtoolkit.eu/wt)]
    - 🔒 [wxWidgets](https://github.com/wxWidgets/wxWidgets) [![GitHub stars](https://img.shields.io/github/stars/wxWidgets/wxWidgets?style=flat)](https://github.com/wxWidgets/wxWidgets/stargazers) - Cross-platform gui using native controls. [[Website](https://wxwidgets.org)]
- C++: Input
    - 🎉 [Gainput](https://github.com/jkuhlmann/gainput) [![GitHub stars](https://img.shields.io/github/stars/jkuhlmann/gainput?style=flat)](https://github.com/jkuhlmann/gainput/stargazers) - Easy to use input library.
    - 🎉 [OIS](https://github.com/wgois/OIS) [![GitHub stars](https://img.shields.io/github/stars/wgois/OIS?style=flat)](https://github.com/wgois/OIS/stargazers) - Object-oriented input system. Compatiable with many operating systems.
    - 🎉 [Oryol Input](https://github.com/floooh/oryol/tree/043683dcb3181beb64ae1c85ea76e4a4eb71c124/code/Modules/Input) [![GitHub stars](https://img.shields.io/github/stars/floooh/oryol/tree/043683dcb3181beb64ae1c85ea76e4a4eb71c124/code/Modules/Input?style=flat)](https://github.com/floooh/oryol/tree/043683dcb3181beb64ae1c85ea76e4a4eb71c124/code/Modules/Input/stargazers) - Input module from the _Oryol_ game framework.
- C++: Layout
    - 🎉 [Yoga](https://github.com/facebook/yoga) [![GitHub stars](https://img.shields.io/github/stars/facebook/yoga?style=flat)](https://github.com/facebook/yoga/stargazers) - Cross-platform [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) layout engine by _Facebook_. [[Website](https://yogalayout.com/)]
- C++: Libraries
    - 🎉 [Boost Libraries](https://github.com/boostorg) [![GitHub stars](https://img.shields.io/github/stars/boostorg?style=flat)](https://github.com/boostorg/stargazers) - Wide range of C++ libraries, many end up as part of the STL. [[Website](https://www.boost.org)]
    - 🎉 [cyCodeBase](https://github.com/cemyuksel/cyCodeBase) [![GitHub stars](https://img.shields.io/github/stars/cemyuksel/cyCodeBase?style=flat)](https://github.com/cemyuksel/cyCodeBase/stargazers) - Compact foundation library with math, geometry, image & graphics utilities.
    - 📚 [Gamedev Libraries](https://github.com/raizam/gamedev_libraries) [![GitHub stars](https://img.shields.io/github/stars/raizam/gamedev_libraries?style=flat)](https://github.com/raizam/gamedev_libraries/stargazers) - Collection of open source C/C++ libraries for game development.
    - 📚 [Inqlude](https://inqlude.org) - List of libraries for developers of _Qt_-based apps.
    - 📚 [List of Open Source C++ Libraries](https://en.cppreference.com/w/cpp/links/libs) - Comprehensive list of open source C++ libraries.
    - 📚 [NVIDIA GameWorks](https://github.com/NVIDIAGameWorks) [![GitHub stars](https://img.shields.io/github/stars/NVIDIAGameWorks?style=flat)](https://github.com/NVIDIAGameWorks/stargazers) - _NVIDIA_ technologies for game & app developers.
- C++: Lighting
    - 🎉 [Thekla Atlas](https://github.com/Thekla/thekla_atlas) [![GitHub stars](https://img.shields.io/github/stars/Thekla/thekla_atlas?style=flat)](https://github.com/Thekla/thekla_atlas/stargazers) - Atlas generation tool.
    - 🎉 [UVAtlas](https://github.com/Microsoft/UVAtlas) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/UVAtlas?style=flat)](https://github.com/Microsoft/UVAtlas/stargazers) - DirectX library for creating and packing texture atlases.
- C++: Math
    - 🎉 [OpenGL Mathematics](https://github.com/g-truc/glm) [![GitHub stars](https://img.shields.io/github/stars/g-truc/glm?style=flat)](https://github.com/g-truc/glm/stargazers) - Header-only math library for graphics software.
- C++: Network
    - 🎉 [Cpp-HttpLib](https://github.com/yhirose/cpp-httplib) [![GitHub stars](https://img.shields.io/github/stars/yhirose/cpp-httplib?style=flat)](https://github.com/yhirose/cpp-httplib/stargazers) - Single-header file HTTP server and client library in C++11.
    - 🎉 [GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) [![GitHub stars](https://img.shields.io/github/stars/ValveSoftware/GameNetworkingSockets?style=flat)](https://github.com/ValveSoftware/GameNetworkingSockets/stargazers) - Messages over UDP, P2P networking, encryption.
    - 🎉 [yojimbo](https://github.com/mas-bandwidth/yojimbo) [![GitHub stars](https://img.shields.io/github/stars/mas-bandwidth/yojimbo?style=flat)](https://github.com/mas-bandwidth/yojimbo/stargazers) - Network library for client/server games.
- C++: Physics
    - 🎉 [Box2D](https://github.com/erincatto/box2d) [![GitHub stars](https://img.shields.io/github/stars/erincatto/box2d?style=flat)](https://github.com/erincatto/box2d/stargazers) - Battle tested 2D physics for games. [[Docs](https://box2d.org/documentation/) | [Fixed Time-Step](https://www.unagames.com/blog/daniele/2010/06/fixed-time-step-implementation-box2d) | [Tutorials](http://www.iforce2d.net/b2dtut/introduction)]
    - 🎉 [Bullet Physics](https://github.com/bulletphysics/bullet3) [![GitHub stars](https://img.shields.io/github/stars/bulletphysics/bullet3?style=flat)](https://github.com/bulletphysics/bullet3/stargazers) - Popular 3D physics libary.
    - 🎉 [Chrono](https://github.com/projectchrono/chrono) [![GitHub stars](https://img.shields.io/github/stars/projectchrono/chrono?style=flat)](https://github.com/projectchrono/chrono/stargazers) - High-performance multiphysics and multibody dynamics simulations. [[Gallery](https://projectchrono.org/gallery/)]
    - 🎉 [Edyn](https://github.com/xissburg/edyn) [![GitHub stars](https://img.shields.io/github/stars/xissburg/edyn?style=flat)](https://github.com/xissburg/edyn/stargazers) - Multi-threaded, networked physics engine. Supports large dynamic worlds. [[Testbed](https://github.com/xissburg/edyn-testbed) [![GitHub stars](https://img.shields.io/github/stars/xissburg/edyn-testbed?style=flat)](https://github.com/xissburg/edyn-testbed/stargazers)]
    - 🎉 [Jolt Physics](https://github.com/jrouwe/JoltPhysics) [![GitHub stars](https://img.shields.io/github/stars/jrouwe/JoltPhysics?style=flat)](https://github.com/jrouwe/JoltPhysics/stargazers) - Multi-core friendly rigid body 3D physics and collision detection.
    - 🎉 [Liquid Fun](https://github.com/google/liquidfun) [![GitHub stars](https://img.shields.io/github/stars/google/liquidfun?style=flat)](https://github.com/google/liquidfun/stargazers) - Extension of _Box2D_, adds particle-based fluid and soft bodies. [[Demos](http://google.github.io/liquidfun/)]
    - 🎉 [Newton Dynamics](https://github.com/MADEAPPS/newton-dynamics/) [![GitHub stars](https://img.shields.io/github/stars/MADEAPPS/newton-dynamics/?style=flat)](https://github.com/MADEAPPS/newton-dynamics//stargazers) - Real-time simulation of 3D environments.
    - 🎉 [ODE](https://bitbucket.org/odedevs/ode/src/master/) - Open Dynamics Engine, 3D rigid body physics. [[Wikipedia](https://en.wikipedia.org/wiki/Open_Dynamics_Engine)]
    - 🎉 [Qu3e](https://github.com/RandyGaul/qu3e) [![GitHub stars](https://img.shields.io/github/stars/RandyGaul/qu3e?style=flat)](https://github.com/RandyGaul/qu3e/stargazers) - Fast 3D physics engine, created to be used in games.
    - 🎉 [ReactPhysics3D](https://github.com/DanielChappuis/reactphysics3d) [![GitHub stars](https://img.shields.io/github/stars/DanielChappuis/reactphysics3d?style=flat)](https://github.com/DanielChappuis/reactphysics3d/stargazers) - 3D physics engine.
    - 🎉 [Slingshot](https://github.com/Slingshot-Physics/slingshot-community) [![GitHub stars](https://img.shields.io/github/stars/Slingshot-Physics/slingshot-community?style=flat)](https://github.com/Slingshot-Physics/slingshot-community/stargazers) - Constraint-based physics engine for 3D rigid body dynamics.
- C++: Reflection
    - 🎉 [Boost.PFR](https://github.com/boostorg/pfr) [![GitHub stars](https://img.shields.io/github/stars/boostorg/pfr?style=flat)](https://github.com/boostorg/pfr/stargazers) - Basic reflection C++14 library, part of the Boost Libraries.
    - 🎉 [Magic Enum](https://github.com/Neargye/magic_enum) [![GitHub stars](https://img.shields.io/github/stars/Neargye/magic_enum?style=flat)](https://github.com/Neargye/magic_enum/stargazers) - Header-only C++17, provides static reflection for enums.
    - 🎉 [Meta](https://github.com/skypjack/meta) [![GitHub stars](https://img.shields.io/github/stars/skypjack/meta?style=flat)](https://github.com/skypjack/meta/stargazers) - Header-only, non-intrusive and macro-free runtime reflection system in C++17.
    - 🎉 [Nameof](https://github.com/Neargye/nameof) [![GitHub stars](https://img.shields.io/github/stars/Neargye/nameof?style=flat)](https://github.com/Neargye/nameof/stargazers) - Header-only C++17, provides nameof macros to obtain name of a variable.
    - 🎉 [Ponder](https://github.com/billyquith/ponder) [![GitHub stars](https://img.shields.io/github/stars/billyquith/ponder?style=flat)](https://github.com/billyquith/ponder/stargazers) - Expose C++17 classes and objects so they can used as data.
    - 🎉 [Reflect](https://github.com/stevinz/reflect) [![GitHub stars](https://img.shields.io/github/stars/stevinz/reflect?style=flat)](https://github.com/stevinz/reflect/stargazers) - Small, flexible, single-header library for runtime reflection and meta data in C++11.
    - 🎉 [RTTR](https://github.com/rttrorg/rttr) [![GitHub stars](https://img.shields.io/github/stars/rttrorg/rttr?style=flat)](https://github.com/rttrorg/rttr/stargazers) - Reflection for C++11.
- C++: Scripting
    - 🎉 [AngelScript](http://www.angelcode.com/angelscript/) - Cross-platform scripting library, follows the widely known syntax of C/C++.
    - 🔒 [ArkScript](https://github.com/ArkScript-lang/Ark) [![GitHub stars](https://img.shields.io/github/stars/ArkScript-lang/Ark?style=flat)](https://github.com/ArkScript-lang/Ark/stargazers) - Small, fast, functional and scripting language.
    - 🎉 [ChaiScript](https://github.com/ChaiScript/ChaiScript) [![GitHub stars](https://img.shields.io/github/stars/ChaiScript/ChaiScript?style=flat)](https://github.com/ChaiScript/ChaiScript/stargazers) - Embedded scripting language designed from to directly target C++17.
    - 🎉 [GameMonkey Script](https://github.com/publicrepo/gmscript) [![GitHub stars](https://img.shields.io/github/stars/publicrepo/gmscript?style=flat)](https://github.com/publicrepo/gmscript/stargazers) - Embedded scripting language for apps, tools and games.
    - 🎉 [v8](https://github.com/v8/v8) [![GitHub stars](https://img.shields.io/github/stars/v8/v8?style=flat)](https://github.com/v8/v8/stargazers) - High-performance JavaScript and WebAssembly engine by _Google_.
- C++: Serialization
    - 🎉 [Cap'n Proto](https://github.com/capnproto/capnproto) [![GitHub stars](https://img.shields.io/github/stars/capnproto/capnproto?style=flat)](https://github.com/capnproto/capnproto/stargazers) - Fast data interchange format and capability-based RPC system.
    - 🎉 [Cereal](https://github.com/USCiLab/cereal) [![GitHub stars](https://img.shields.io/github/stars/USCiLab/cereal?style=flat)](https://github.com/USCiLab/cereal/stargazers) - Header-only C++11 serialization library.
    - 🎉 [Cista++](https://github.com/felixguendling/cista) [![GitHub stars](https://img.shields.io/github/stars/felixguendling/cista?style=flat)](https://github.com/felixguendling/cista/stargazers) - Simple, high-performance serialization & reflection library.
    - 🎉 [FlatBuffers](https://github.com/google/flatbuffers) [![GitHub stars](https://img.shields.io/github/stars/google/flatbuffers?style=flat)](https://github.com/google/flatbuffers/stargazers) - Efficient cross-platform serialization library by _Google_.
    - 🎉 [JSON for Modern C++](https://github.com/nlohmann/json) [![GitHub stars](https://img.shields.io/github/stars/nlohmann/json?style=flat)](https://github.com/nlohmann/json/stargazers) - JSON support for Modern C++.
    - 🎉 [Protobuf](https://github.com/protocolbuffers/protobuf) [![GitHub stars](https://img.shields.io/github/stars/protocolbuffers/protobuf?style=flat)](https://github.com/protocolbuffers/protobuf/stargazers) - Protocol Buffers, for platform-neutral serialized data by _Google_.
    - 🎉 [RapidJSON](https://github.com/Tencent/rapidjson/) [![GitHub stars](https://img.shields.io/github/stars/Tencent/rapidjson/?style=flat)](https://github.com/Tencent/rapidjson//stargazers) - Fast JSON parser / generator.
- C++: Terrain
    - 🎉 [Terra Forge 3D](https://github.com/Jaysmito101/TerraForge3D) [![GitHub stars](https://img.shields.io/github/stars/Jaysmito101/TerraForge3D?style=flat)](https://github.com/Jaysmito101/TerraForge3D/stargazers) - Procedural 3D terrain generation and texturing tool.
- C++: Utility
    - 🎉 [Any-Lite](https://github.com/martinmoene/any-lite) [![GitHub stars](https://img.shields.io/github/stars/martinmoene/any-lite?style=flat)](https://github.com/martinmoene/any-lite/stargazers) - Header-only 'any' type for C++98 and above.
    - 🎉 [EASTL](https://github.com/electronicarts/EASTL/) [![GitHub stars](https://img.shields.io/github/stars/electronicarts/EASTL/?style=flat)](https://github.com/electronicarts/EASTL//stargazers) - Electronic Arts STL replacement, emphasis on performance.
    - 🎉 [faker-cxx](https://github.com/cieslarmichal/faker-cxx) [![GitHub stars](https://img.shields.io/github/stars/cieslarmichal/faker-cxx?style=flat)](https://github.com/cieslarmichal/faker-cxx/stargazers) - C++20 Faker library for generating fake (but realistic) data for testing and development.
    - 🎉 [Parallel Hashmap](https://github.com/greg7mdp/parallel-hashmap) [![GitHub stars](https://img.shields.io/github/stars/greg7mdp/parallel-hashmap?style=flat)](https://github.com/greg7mdp/parallel-hashmap/stargazers) - Header-only, fast and memory-friendly hashmap and binary tree containers.
    - 🎉 [Spdlog](https://github.com/gabime/spdlog) [![GitHub stars](https://img.shields.io/github/stars/gabime/spdlog?style=flat)](https://github.com/gabime/spdlog/stargazers) - Fast logging library.
    - 🎉 [Tiny-Process-Library](https://gitlab.com/eidheim/tiny-process-library) - Making it simple to create and stop new processes.
    - 🎉 [TinyXML-2](https://github.com/leethomason/tinyxml2) [![GitHub stars](https://img.shields.io/github/stars/leethomason/tinyxml2?style=flat)](https://github.com/leethomason/tinyxml2/stargazers) - XML parser that can be easily integrated into other programs.
- C++: Visual Programming / Nodes
    - 🎉 [NodeEditor](https://github.com/paceholder/nodeeditor) [![GitHub stars](https://img.shields.io/github/stars/paceholder/nodeeditor?style=flat)](https://github.com/paceholder/nodeeditor/stargazers) - Graph-controlled data processing, built with _Qt_.
    - 🎉 [QuickQanava](https://github.com/cneben/QuickQanava) [![GitHub stars](https://img.shields.io/github/stars/cneben/QuickQanava?style=flat)](https://github.com/cneben/QuickQanava/stargazers) - Display graphs and relational content in a _QtQuick_-based app, in C++14.
    - 🎉 [Visual Script Engine](https://github.com/kovacsv/VisualScriptEngine) [![GitHub stars](https://img.shields.io/github/stars/kovacsv/VisualScriptEngine?style=flat)](https://github.com/kovacsv/VisualScriptEngine/stargazers) - Visual scripting engine designed for embedding.

### C#
- 📚 [Awesome C-Sharp](https://github.com/uhub/awesome-c-sharp) [![GitHub stars](https://img.shields.io/github/stars/uhub/awesome-c-sharp?style=flat)](https://github.com/uhub/awesome-c-sharp/stargazers) - List of awesome C-Sharp frameworks, libraries and software.
- 📚 [Awesome .NET](https://github.com/quozd/awesome-dotnet) [![GitHub stars](https://img.shields.io/github/stars/quozd/awesome-dotnet?style=flat)](https://github.com/quozd/awesome-dotnet/stargazers) - Collection of awesome .NET libraries, tools, frameworks and software.
- 📚 [Dot Net Perls](https://www.dotnetperls.com) - Reference for the C# language.
- C#: App Framework
    - 🎉 [ATF](https://github.com/SonyWWS/ATF) [![GitHub stars](https://img.shields.io/github/stars/SonyWWS/ATF?style=flat)](https://github.com/SonyWWS/ATF/stargazers) - Components for making tools on Windows, started in 2005.
- C#: Audio
    - 🎉 [NAudio](https://github.com/naudio/NAudio) [![GitHub stars](https://img.shields.io/github/stars/naudio/NAudio?style=flat)](https://github.com/naudio/NAudio/stargazers) - Audio and MIDI library for .NET.
- C#: Cross-Platform
    - 🌎 [Blazor](https://github.com/dotnet/aspnetcore/blob/main/src/Components/README.md) [![GitHub stars](https://img.shields.io/github/stars/dotnet/aspnetcore/blob/main/src/Components/README.md?style=flat)](https://github.com/dotnet/aspnetcore/blob/main/src/Components/README.md/stargazers) - C# to JavaScript (as WebAssembly) technology by _Microsoft_. [[Website]((https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor))]
    - 🎉 [Mono](https://github.com/mono/mono) [![GitHub stars](https://img.shields.io/github/stars/mono/mono?style=flat)](https://github.com/mono/mono/stargazers) - Open source implementation of _Microsoft_'s .NET Framework.
- C#: Entity Component System
    - 🎉 [Arch](https://github.com/genaray/Arch) [![GitHub stars](https://img.shields.io/github/stars/genaray/Arch?style=flat)](https://github.com/genaray/Arch/stargazers) - High-performance ECS with optional multithreading.
    - 🎉 [DefaultEcs](https://github.com/Doraku/DefaultEcs) [![GitHub stars](https://img.shields.io/github/stars/Doraku/DefaultEcs?style=flat)](https://github.com/Doraku/DefaultEcs/stargazers) - ECS framework designed for game development.
    - 🎉 [friflo ECS](https://github.com/friflo/Friflo.Engine.ECS) [![GitHub stars](https://img.shields.io/github/stars/friflo/Friflo.Engine.ECS?style=flat)](https://github.com/friflo/Friflo.Engine.ECS/stargazers) - High-performance C# ECS.
    - 🎉 [LeoECS](https://github.com/Leopotam/ecs) [![GitHub stars](https://img.shields.io/github/stars/Leopotam/ecs?style=flat)](https://github.com/Leopotam/ecs/stargazers) - ECS framework powered by C# with optional integration to _Unity_.
- C#: Game Engine w/Editor
    - 🎉 [Duality](https://github.com/AdamsLair/duality) [![GitHub stars](https://img.shields.io/github/stars/AdamsLair/duality?style=flat)](https://github.com/AdamsLair/duality/stargazers) - Modular 2D engine, editor built with _OpenTK_.
    - 🎉 [Flat Red Ball](https://github.com/vchelaru/FlatRedBall) [![GitHub stars](https://img.shields.io/github/stars/vchelaru/FlatRedBall?style=flat)](https://github.com/vchelaru/FlatRedBall/stargazers) - 2D game engine & design tools, built with _MonoGame_. [[Website](https://flatredball.com/)]
    - 🎉 [Murder](https://github.com/isadorasophia/murder) [![GitHub stars](https://img.shields.io/github/stars/isadorasophia/murder?style=flat)](https://github.com/isadorasophia/murder/stargazers) - Pixel-art, ECS game engine built on _MonoGame_. [[Docs](https://isadorasophia.com/murder/)]
    - 🎉 [Prowl](https://github.com/ProwlEngine/Prowl) [![GitHub stars](https://img.shields.io/github/stars/ProwlEngine/Prowl?style=flat)](https://github.com/ProwlEngine/Prowl/stargazers) - 3D game engine inspired by _Unity_.
    - 🎉 [Stride](https://github.com/stride3d/stride) [![GitHub stars](https://img.shields.io/github/stars/stride3d/stride?style=flat)](https://github.com/stride3d/stride/stargazers) - Game engine for realistic rendering and VR. Formerly _Xenko_. [[Website](https://www.stride3d.net/)]
    - 💸 [Unity](https://store.unity.com/) - Biggest name in game engines, industry standard.
- C#: Game Framework
    - 🎉 [FNA](https://github.com/FNA-XNA/FNA) [![GitHub stars](https://img.shields.io/github/stars/FNA-XNA/FNA?style=flat)](https://github.com/FNA-XNA/FNA/stargazers) - Reimplementation of the Microsoft XNA Game Studio 4.0 libraries.
    - 🎉 [Monofoxe](https://github.com/Martenfur/Monofoxe) [![GitHub stars](https://img.shields.io/github/stars/Martenfur/Monofoxe?style=flat)](https://github.com/Martenfur/Monofoxe/stargazers) - Game engine designed to simplify working with _MonoGame_.
    - 🎉 [MonoGame](https://github.com/MonoGame/MonoGame) [![GitHub stars](https://img.shields.io/github/stars/MonoGame/MonoGame?style=flat)](https://github.com/MonoGame/MonoGame/stargazers) 🔥 - Framework for creating cross-platform games. [[Website](https://www.monogame.net/)]
    - 🎉 [Nez](https://github.com/prime31/Nez) [![GitHub stars](https://img.shields.io/github/stars/prime31/Nez?style=flat)](https://github.com/prime31/Nez/stargazers) - Feature-rich 2D framework built on _MonoGame_.
    - 🎉 [Protogame](https://github.com/RedpointGames/Protogame) [![GitHub stars](https://img.shields.io/github/stars/RedpointGames/Protogame?style=flat)](https://github.com/RedpointGames/Protogame/stargazers) - Cross-platform 2D/3D game engine built on _MonoGame_.
- C#: Geometry
    - 🎉 [DotRecast](https://github.com/ikpil/DotRecast) [![GitHub stars](https://img.shields.io/github/stars/ikpil/DotRecast?style=flat)](https://github.com/ikpil/DotRecast/stargazers) - A port of _Recast & Detour_, navigation mesh toolset for games, Unity3D, servers, C#.
- C#: Graphics - 2D
    - 🎉 [ImageSharp](https://github.com/SixLabors/ImageSharp) [![GitHub stars](https://img.shields.io/github/stars/SixLabors/ImageSharp?style=flat)](https://github.com/SixLabors/ImageSharp/stargazers) - Modern, cross-platform, 2D graphics library for .NET.
- C#: Graphics - 3D
    - 🎉 [OpenTK](https://github.com/opentk/opentk) [![GitHub stars](https://img.shields.io/github/stars/opentk/opentk?style=flat)](https://github.com/opentk/opentk/stargazers) - Open Toolkit, C# bindings for OpenGL. [[LearnOpenTK](https://github.com/opentk/LearnOpenTK) [![GitHub stars](https://img.shields.io/github/stars/opentk/LearnOpenTK?style=flat)](https://github.com/opentk/LearnOpenTK/stargazers)]
    - 🎉 [Veldrid](https://github.com/mellinoe/veldrid) [![GitHub stars](https://img.shields.io/github/stars/mellinoe/veldrid?style=flat)](https://github.com/mellinoe/veldrid/stargazers) - Cross-platform, graphics API-agnostic rendering and compute library for .NET.
- C#: Gui
    - 🎉 [Apos.Gui](https://github.com/Apostolique/Apos.Gui) [![GitHub stars](https://img.shields.io/github/stars/Apostolique/Apos.Gui?style=flat)](https://github.com/Apostolique/Apos.Gui/stargazers) - UI library for _MonoGame_.
    - 🎉 [Avalonia](https://github.com/AvaloniaUI/Avalonia) [![GitHub stars](https://img.shields.io/github/stars/AvaloniaUI/Avalonia?style=flat)](https://github.com/AvaloniaUI/Avalonia/stargazers) - Cross-platform gui framework for .NET. [[Website](https://avaloniaui.net/)]
    - 🎉 [GeonBit.UI](https://github.com/RonenNess/GeonBit.UI) [![GitHub stars](https://img.shields.io/github/stars/RonenNess/GeonBit.UI?style=flat)](https://github.com/RonenNess/GeonBit.UI/stargazers) - Gui for _MonoGame_ projects.
    - 🎉 [MGUI](https://github.com/Videogamers0/MGUI) [![GitHub stars](https://img.shields.io/github/stars/Videogamers0/MGUI?style=flat)](https://github.com/Videogamers0/MGUI/stargazers) - UI framework for the _MonoGame_ game framework.
    - 🎉 [MonoGame.Forms](https://github.com/BlizzCrafter/MonoGame.Forms) [![GitHub stars](https://img.shields.io/github/stars/BlizzCrafter/MonoGame.Forms?style=flat)](https://github.com/BlizzCrafter/MonoGame.Forms/stargazers) - _MonoGame_ render window for Windows Forms.
    - 🎉 [Myra](https://github.com/rds1983/Myra) [![GitHub stars](https://img.shields.io/github/stars/rds1983/Myra?style=flat)](https://github.com/rds1983/Myra/stargazers) - Gui library for _MonoGame_, _FNA_, and _Stride_.
    - 🎉 [Squid](https://github.com/Roderik11/Squid) [![GitHub stars](https://img.shields.io/github/stars/Roderik11/Squid?style=flat)](https://github.com/Roderik11/Squid/stargazers) - C# Realtime GUI System.
    - 🎉 [Uno](https://github.com/unoplatform/uno) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno?style=flat)](https://github.com/unoplatform/uno/stargazers) - Mobile, desktop and WebAssembly gui library. [[Website](https://platform.uno/)]
    - 🎉 [VellumUI](https://github.com/notgiven688/vellum) [![GitHub stars](https://img.shields.io/github/stars/notgiven688/vellum?style=flat)](https://github.com/notgiven688/vellum/stargazers) - Lightweight immediate-mode GUI library with font rendering.
- C#: Layout
    - 🎉 [Gum](https://github.com/vchelaru/Gum) [![GitHub stars](https://img.shields.io/github/stars/vchelaru/Gum?style=flat)](https://github.com/vchelaru/Gum/stargazers) - Flexible layout tool for creating UI on any platform.
- C#: Physics
    - 🎉 [Aether Physics](https://github.com/tainicom/Aether.Physics2D) [![GitHub stars](https://img.shields.io/github/stars/tainicom/Aether.Physics2D?style=flat)](https://github.com/tainicom/Aether.Physics2D/stargazers) - 2D physics library with continuous collision detection.
    - 🎉 [Box2D.NET](https://github.com/ikpil/Box2D.NET) [![GitHub stars](https://img.shields.io/github/stars/ikpil/Box2D.NET?style=flat)](https://github.com/ikpil/Box2D.NET/stargazers) - A port of Box2D. 2D physics engine for games, .NET C#, Unity3D, servers.
    - 🎉 [Jitter Physics 2](https://github.com/notgiven688/jitterphysics2) [![GitHub stars](https://img.shields.io/github/stars/notgiven688/jitterphysics2?style=flat)](https://github.com/notgiven688/jitterphysics2/stargazers) - Fast, simple, and dependency-free physics engine.
    - 🎉 [Velcro Physics](https://github.com/Genbox/VelcroPhysics) [![GitHub stars](https://img.shields.io/github/stars/Genbox/VelcroPhysics?style=flat)](https://github.com/Genbox/VelcroPhysics/stargazers) - C# port of Box2D. Formerly _Farseer Physics_.
- C#: Utility
    - 🎉 [Facepunch.Steamworks](https://github.com/Facepunch/Facepunch.Steamworks) [![GitHub stars](https://img.shields.io/github/stars/Facepunch/Facepunch.Steamworks?style=flat)](https://github.com/Facepunch/Facepunch.Steamworks/stargazers) - Steamworks implementation.
    - 🎉 [Monogame.Extended](https://github.com/MonoGame-Extended/Monogame-Extended) [![GitHub stars](https://img.shields.io/github/stars/MonoGame-Extended/Monogame-Extended?style=flat)](https://github.com/MonoGame-Extended/Monogame-Extended/stargazers) - Extensions to make _MonoGame_ more awesome.

### Dart
- 📚 [Awesome Dart](https://github.com/yissachar/awesome-dart) [![GitHub stars](https://img.shields.io/github/stars/yissachar/awesome-dart?style=flat)](https://github.com/yissachar/awesome-dart/stargazers) - Curated list of awesome Dart frameworks, libraries, and software.
- 🌎 [Dart](https://dart.dev) - Client-optimized language for fast apps on any platform. [[GitHub](https://github.com/dart-lang/) [![GitHub stars](https://img.shields.io/github/stars/dart-lang/?style=flat)](https://github.com/dart-lang//stargazers)]
- Dart: App Framework
    - 🎉 [Flutter](https://flutter.dev) - Open source app framework by _Google_. [[Awesome](https://github.com/Solido/awesome-flutter) [![GitHub stars](https://img.shields.io/github/stars/Solido/awesome-flutter?style=flat)](https://github.com/Solido/awesome-flutter/stargazers) | [GitHub](https://github.com/flutter) [![GitHub stars](https://img.shields.io/github/stars/flutter?style=flat)](https://github.com/flutter/stargazers)]
- Dart: File Formats
    - 🎉 [image](https://github.com/brendan-duncan/image) [![GitHub stars](https://img.shields.io/github/stars/brendan-duncan/image?style=flat)](https://github.com/brendan-duncan/image/stargazers) - Library for decoding / encoding image formats and image processing.
- Dart: Game Framework
    - 🎉 [Flame](https://github.com/flame-engine/flame) [![GitHub stars](https://img.shields.io/github/stars/flame-engine/flame?style=flat)](https://github.com/flame-engine/flame/stargazers) - Minimalist _Flutter_ based 2D game engine. [[Awesome](https://github.com/flame-engine/awesome-flame) [![GitHub stars](https://img.shields.io/github/stars/flame-engine/awesome-flame?style=flat)](https://github.com/flame-engine/awesome-flame/stargazers) | [Examples](https://examples.flame-engine.org/) | [Website](https://flame-engine.org/)]

### F#
- 📚 [Awesome F#](https://github.com/fsprojects/awesome-fsharp) [![GitHub stars](https://img.shields.io/github/stars/fsprojects/awesome-fsharp?style=flat)](https://github.com/fsprojects/awesome-fsharp/stargazers) - Curated list of frameworks, libraries, software and resources.
- 🌎 [F#](https://fsharp.org) - Functional-first language for .NET, prioritizing expressive code and parallelism.
- F#: Audio
    - 🔒 [FSound](https://github.com/albertp007/FSound) [![GitHub stars](https://img.shields.io/github/stars/albertp007/FSound?style=flat)](https://github.com/albertp007/FSound/stargazers) - Sound processing library.
- F#: Entity Component System
    - 🎉 [Garnet](https://github.com/bcarruthers/garnet) [![GitHub stars](https://img.shields.io/github/stars/bcarruthers/garnet?style=flat)](https://github.com/bcarruthers/garnet/stargazers) - Game composition library with ECS and actor-like messaging features.
- F#: Game Engine w/Editor
    - 🎉 [Nu Game Engine](https://github.com/bryanedds/Nu) [![GitHub stars](https://img.shields.io/github/stars/bryanedds/Nu?style=flat)](https://github.com/bryanedds/Nu/stargazers) - Cross-platform game engine built in the functional style.
- F#: Gui
    - 🎉 [Fabulous](https://github.com/fabulous-dev/Fabulous) [![GitHub stars](https://img.shields.io/github/stars/fabulous-dev/Fabulous?style=flat)](https://github.com/fabulous-dev/Fabulous/stargazers) - Declarative UI framework for cross-platform apps.

### Go
- 📚 [Awesome Go](https://github.com/avelino/awesome-go) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go?style=flat)](https://github.com/avelino/awesome-go/stargazers) - Awesome Go frameworks, libraries and software.
- 🌎 [Go](https://go.dev/) - Statically typed, compiled programming language designed at _Google_. [[GitHub](https://github.com/golang) [![GitHub stars](https://img.shields.io/github/stars/golang?style=flat)](https://github.com/golang/stargazers)]
- Go: Audio
    - 🎉 [Beep](https://github.com/faiface/beep) [![GitHub stars](https://img.shields.io/github/stars/faiface/beep?style=flat)](https://github.com/faiface/beep/stargazers) - Playback and audio-processing.
- Go: Game Engine w/Editor
    - 🎉 [G3N](https://github.com/g3n/engine) [![GitHub stars](https://img.shields.io/github/stars/g3n/engine?style=flat)](https://github.com/g3n/engine/stargazers) - OpenGL 3D game engine.
- Go: Game Framework
    - 🎉 [Ebitengine](https://github.com/hajimehoshi/ebiten) [![GitHub stars](https://img.shields.io/github/stars/hajimehoshi/ebiten?style=flat)](https://github.com/hajimehoshi/ebiten/stargazers) - Dead simple 2D game library.
    - 🎉 [Engo](https://github.com/EngoEngine/engo) [![GitHub stars](https://img.shields.io/github/stars/EngoEngine/engo?style=flat)](https://github.com/EngoEngine/engo/stargazers) - A 2D game framework.
    - 🎉 [Pixel](https://github.com/faiface/pixel) [![GitHub stars](https://img.shields.io/github/stars/faiface/pixel?style=flat)](https://github.com/faiface/pixel/stargazers) - Hand-crafted 2D game library. [[Examples](https://github.com/faiface/pixel-examples) [![GitHub stars](https://img.shields.io/github/stars/faiface/pixel-examples?style=flat)](https://github.com/faiface/pixel-examples/stargazers)]
- Go: Geometry
    - 🎉 [3D Mesh Simplification](https://github.com/fogleman/simplify) [![GitHub stars](https://img.shields.io/github/stars/fogleman/simplify?style=flat)](https://github.com/fogleman/simplify/stargazers) - 3D mesh simplification.
- Go: Graphics
    - 🎉 [ln](https://github.com/fogleman/ln) [![GitHub stars](https://img.shields.io/github/stars/fogleman/ln?style=flat)](https://github.com/fogleman/ln/stargazers) - The 3D Line Art Engine, a vector-based 3D renderer. [[Docs](https://pkg.go.dev/github.com/fogleman/ln/ln)]

### Haxe
- 📚 [Awesome Haxe](https://github.com/nadako/awesome-haxe) [![GitHub stars](https://img.shields.io/github/stars/nadako/awesome-haxe?style=flat)](https://github.com/nadako/awesome-haxe/stargazers) - Awesome curated list of useful Haxe links.
- 📚 [Awesome Haxe Game Dev](https://github.com/Dvergar/awesome-haxe-gamedev) [![GitHub stars](https://img.shields.io/github/stars/Dvergar/awesome-haxe-gamedev?style=flat)](https://github.com/Dvergar/awesome-haxe-gamedev/stargazers) - Awesome list of game dev resources for Haxe.
- 🌎 [Haxe](https://haxe.org) - Produce cross-platform native code. [[GitHub](https://github.com/HaxeFoundation/haxe) [![GitHub stars](https://img.shields.io/github/stars/HaxeFoundation/haxe?style=flat)](https://github.com/HaxeFoundation/haxe/stargazers)]
- 📚 [Haxe Blog: Game Engine](https://kircode.com/post/how-i-wrote-my-own-3d-game-engine-and-shipped-a-game-with-it-in-20-months) - "How I wrote my own 3D game engine and shipped a game in 20 months".
- 📚 [Haxe Blog: OpenFL](https://www.gamedeveloper.com/programming/flash-is-dead-long-live-openfl-) - "Flash is dead, long live OpenFL".
- Haxe: Animation
    - 🎉 [Actuate](https://github.com/jgranick/actuate) [![GitHub stars](https://img.shields.io/github/stars/jgranick/actuate?style=flat)](https://github.com/jgranick/actuate/stargazers) - Flexible, fast tween library.
    - 🎉 [DragonBones](https://github.com/openfl/dragonbones) [![GitHub stars](https://img.shields.io/github/stars/openfl/dragonbones?style=flat)](https://github.com/openfl/dragonbones/stargazers) - Runtime support for _DragonBones_ skeletal animation.
    - 🎉 [Spine-Hx](https://github.com/jeremyfa/spine-hx) [![GitHub stars](https://img.shields.io/github/stars/jeremyfa/spine-hx?style=flat)](https://github.com/jeremyfa/spine-hx/stargazers) - _Spine_ runtime for Haxe.
- Haxe: App Framework
    - 🎉 [Lime](https://github.com/haxelime/lime) [![GitHub stars](https://img.shields.io/github/stars/haxelime/lime?style=flat)](https://github.com/haxelime/lime/stargazers) - Flexible, lightweight layer for Haxe cross-platform developers.
    - 🎉 [nme](https://github.com/haxenme/nme) [![GitHub stars](https://img.shields.io/github/stars/haxenme/nme?style=flat)](https://github.com/haxenme/nme/stargazers) - Cross-platform native backend for Haxe projects.
- Haxe: Cross-Platform
    - 🎉 [HashLink](https://github.com/HaxeFoundation/hashlink/) [![GitHub stars](https://img.shields.io/github/stars/HaxeFoundation/hashlink/?style=flat)](https://github.com/HaxeFoundation/hashlink//stargazers) - Virtual machine for Haxe.
- Haxe: Entity Component System
    - 🎉 [Ecx](https://github.com/eliasku/ecx) [![GitHub stars](https://img.shields.io/github/stars/eliasku/ecx?style=flat)](https://github.com/eliasku/ecx/stargazers) - Entity component system framework for Haxe.
    - 🎉 [GASM](https://github.com/HacksawStudios/GASM) [![GitHub stars](https://img.shields.io/github/stars/HacksawStudios/GASM?style=flat)](https://github.com/HacksawStudios/GASM/stargazers) - Framework agnostic entity component system for Haxe.
- Haxe: Game Engine w/Editor
    - 🎉 [Armory](https://github.com/armory3d/armory) [![GitHub stars](https://img.shields.io/github/stars/armory3d/armory?style=flat)](https://github.com/armory3d/armory/stargazers) - 3D game engine with full _Blender_ integration.
    - 🎉 [Away3D](https://github.com/openfl/away3d) [![GitHub stars](https://img.shields.io/github/stars/openfl/away3d?style=flat)](https://github.com/openfl/away3d/stargazers) - Real-time 3D engine for OpenFL. [[Website](http://away3d.com)]
    - 🎉 [Flixel-Studio](https://github.com/Dovyski/flixel-studio) [![GitHub stars](https://img.shields.io/github/stars/Dovyski/flixel-studio?style=flat)](https://github.com/Dovyski/flixel-studio/stargazers) - Embeddable, in-game editor for _HaxeFlixel_.
    - 🎉 [Hide](https://github.com/heapsio/hide) [![GitHub stars](https://img.shields.io/github/stars/heapsio/hide?style=flat)](https://github.com/heapsio/hide/stargazers) - Extensible IDE for the _Heaps_ 3D graphic engine.
    - 🎉 [LDtk](https://github.com/deepnight/ldtk) [![GitHub stars](https://img.shields.io/github/stars/deepnight/ldtk?style=flat)](https://github.com/deepnight/ldtk/stargazers) 🔥 - Modern, lightweight and efficient 2D level editor. [[Website](https://ldtk.io)]
    - 🎉 [Starling](https://github.com/openfl/starling) [![GitHub stars](https://img.shields.io/github/stars/openfl/starling?style=flat)](https://github.com/openfl/starling/stargazers) - Popular (_Angry Birds_) 2D game engine built on _OpenFL_. [[Editor](http://starlingbuilder.github.io) | [Website](https://gamua.com/starling/)]
- Haxe: Game Framework
    - 🎉 [Ceramic](https://github.com/ceramic-engine/ceramic) [![GitHub stars](https://img.shields.io/github/stars/ceramic-engine/ceramic?style=flat)](https://github.com/ceramic-engine/ceramic/stargazers) - Cross-platform 2D framework. [[Examples](https://ceramic-engine.com/examples/)]
    - 🎉 [Citrus](https://github.com/DaVikingCode/Citrus-Engine) [![GitHub stars](https://img.shields.io/github/stars/DaVikingCode/Citrus-Engine?style=flat)](https://github.com/DaVikingCode/Citrus-Engine/stargazers) - ActionScript 3 based 2D/3D framework. [[Website](http://citrusengine.com/)]
    - 🎉 [Clay](https://github.com/clay2d/clay) [![GitHub stars](https://img.shields.io/github/stars/clay2d/clay?style=flat)](https://github.com/clay2d/clay/stargazers) - Cross-platform 2D game framework.
    - 🎉 [gameBase](https://github.com/deepnight/gameBase) [![GitHub stars](https://img.shields.io/github/stars/deepnight/gameBase?style=flat)](https://github.com/deepnight/gameBase/stargazers) - Base structure for Haxe games, using _Heaps_ graphics framework. [[Tutorial](https://deepnight.net/tutorial/using-my-gamebase-to-create-a-heaps-game/)]
    - 🎉 [HaxeFlixel](https://github.com/HaxeFlixel/flixel) [![GitHub stars](https://img.shields.io/github/stars/HaxeFlixel/flixel?style=flat)](https://github.com/HaxeFlixel/flixel/stargazers) - Cross-platform 2D game framework powered by _OpenFL_. [[Website](https://haxeflixel.com/)]
    - 🎉 [OpenFL](https://github.com/openfl/openfl) [![GitHub stars](https://img.shields.io/github/stars/openfl/openfl?style=flat)](https://github.com/openfl/openfl/stargazers) - Open source implementation of the [Adobe Flash](https://en.wikipedia.org/wiki/Adobe_Flash) API. [[Website](https://www.openfl.org/)]
- Haxe: Graphics
    - 🎉 [Heaps](https://github.com/HeapsIO/heaps) [![GitHub stars](https://img.shields.io/github/stars/HeapsIO/heaps?style=flat)](https://github.com/HeapsIO/heaps/stargazers) 🔥 - Cross-platform 2D/3D engine (by creators of Haxe). [[Website](https://heaps.io)]
    - 🎉 [Kha](https://github.com/Kode/Kha) [![GitHub stars](https://img.shields.io/github/stars/Kode/Kha?style=flat)](https://github.com/Kode/Kha/stargazers) - Ultra-portable, high-performance multimedia framework.
    - 🎉 [Sparkler](https://github.com/AndreiRudenko/sparkler) [![GitHub stars](https://img.shields.io/github/stars/AndreiRudenko/sparkler?style=flat)](https://github.com/AndreiRudenko/sparkler/stargazers) - Modular macro-powered particle system.
- Haxe: Gui
    - 🎉 [HaxeUI](https://github.com/haxeui/haxeui-core) [![GitHub stars](https://img.shields.io/github/stars/haxeui/haxeui-core?style=flat)](https://github.com/haxeui/haxeui-core/stargazers) - Cross-platform set of styleable gui components.
    - 🎉 [Zui](https://github.com/armory3d/zui) [![GitHub stars](https://img.shields.io/github/stars/armory3d/zui?style=flat)](https://github.com/armory3d/zui/stargazers) - Immediate mode user interface, used in _ArmorPaint_.
- Haxe: Libraries
    - 📚 [HaxeLibs](https://lib.haxe.org/all) - List of every library uploaded to the Haxe website.
    - 📚 [HaxeTink](https://github.com/haxetink) [![GitHub stars](https://img.shields.io/github/stars/haxetink?style=flat)](https://github.com/haxetink/stargazers) - Various addon libraries for Haxe.
    - 🌎 [Snowkit](https://github.com/snowkit) [![GitHub stars](https://img.shields.io/github/stars/snowkit?style=flat)](https://github.com/snowkit/stargazers) - Collective of Haxe developers.
- Haxe: Physics
    - 🎉 [Haxe Bullet](https://github.com/armory3d/haxebullet) [![GitHub stars](https://img.shields.io/github/stars/armory3d/haxebullet?style=flat)](https://github.com/armory3d/haxebullet/stargazers) - _Bullet 3D_ physics bindings for Haxe.
    - 🎉 [HeapsIO/bullet](https://github.com/HeapsIO/bullet) [![GitHub stars](https://img.shields.io/github/stars/HeapsIO/bullet?style=flat)](https://github.com/HeapsIO/bullet/stargazers) - _Bullet 3D_ physics for _Heaps_ (Haxe's native low-level game framework).
    - 🎉 [Jelly Physics](https://github.com/michaelapfelbeck/jellyPhysics) [![GitHub stars](https://img.shields.io/github/stars/michaelapfelbeck/jellyPhysics?style=flat)](https://github.com/michaelapfelbeck/jellyPhysics/stargazers) - Soft body 2D physics engine.
    - 🎉 [Nape](https://github.com/HaxeFlixel/nape-haxe4) [![GitHub stars](https://img.shields.io/github/stars/HaxeFlixel/nape-haxe4?style=flat)](https://github.com/HaxeFlixel/nape-haxe4/stargazers) - Fast, friendly 2D rigid body physics engine. [[Demos](https://joecreates.github.io/napephys/)]
- Haxe: Serialization / Storage
    - 🎉 [CastleDB](https://github.com/ncannasse/castle) [![GitHub stars](https://img.shields.io/github/stars/ncannasse/castle?style=flat)](https://github.com/ncannasse/castle/stargazers) - Structured database with a local web service to edit it.
    - 🎉 [Format](https://github.com/HaxeFoundation/format) [![GitHub stars](https://img.shields.io/github/stars/HaxeFoundation/format?style=flat)](https://github.com/HaxeFoundation/format/stargazers) - Various files formats support for Haxe.
    - 🎉 [HxBit](https://github.com/HeapsIO/hxbit) [![GitHub stars](https://img.shields.io/github/stars/HeapsIO/hxbit?style=flat)](https://github.com/HeapsIO/hxbit/stargazers) - Binary serialization and network synchronization library.
- Haxe: Utility
    - 🎉 [hexMachina](https://github.com/DoclerLabs/hexCore) [![GitHub stars](https://img.shields.io/github/stars/DoclerLabs/hexCore?style=flat)](https://github.com/DoclerLabs/hexCore/stargazers) - Powerful modular MVC framework. [[Website](http://hexmachina.org/)]
    - 🎉 [HxColorToolkit](https://github.com/andyli/hxColorToolkit) [![GitHub stars](https://img.shields.io/github/stars/andyli/hxColorToolkit?style=flat)](https://github.com/andyli/hxColorToolkit/stargazers) - Library for color conversion and color scheme generation.
    - 🎉 [HxMath](https://github.com/tbrosman/hxmath) [![GitHub stars](https://img.shields.io/github/stars/tbrosman/hxmath?style=flat)](https://github.com/tbrosman/hxmath/stargazers) - Game-oriented math library for the Haxe language.
    - 🎉 [SteamWrap](https://github.com/larsiusprime/SteamWrap) [![GitHub stars](https://img.shields.io/github/stars/larsiusprime/SteamWrap?style=flat)](https://github.com/larsiusprime/SteamWrap/stargazers) - Haxe native extension for the Steam API.
- Haxe: Visual Programming / Nodes
    - 🎉 [Haxe-Blockly](https://github.com/nickmain/haxe-blockly) [![GitHub stars](https://img.shields.io/github/stars/nickmain/haxe-blockly?style=flat)](https://github.com/nickmain/haxe-blockly/stargazers) - Haxe wrapper for [Blockly](https://developers.google.com/blockly)

### Lua
- 📚 [Awesome Lua](https://github.com/LewisJEllis/awesome-lua) [![GitHub stars](https://img.shields.io/github/stars/LewisJEllis/awesome-lua?style=flat)](https://github.com/LewisJEllis/awesome-lua/stargazers) - Awesome Lua packages and resources.
- Lua: Game Framework
    - 🎉 [3DreamEngine](https://github.com/3dreamengine/3DreamEngine) [![GitHub stars](https://img.shields.io/github/stars/3dreamengine/3DreamEngine?style=flat)](https://github.com/3dreamengine/3DreamEngine/stargazers) - 3D engine on top of _LÖVE_.
    - 🎉 [Gideros](https://github.com/gideros/gideros) [![GitHub stars](https://img.shields.io/github/stars/gideros/gideros?style=flat)](https://github.com/gideros/gideros/stargazers) - 2D/3D cross-platform games with Lua. [[Website](http://giderosmobile.com/)]
    - 🎉 [INSTEAD](https://github.com/instead-hub/instead) [![GitHub stars](https://img.shields.io/github/stars/instead-hub/instead?style=flat)](https://github.com/instead-hub/instead/stargazers) - Simple Text Adventure Interpreter.
    - 🎉 [LÖVE](https://github.com/love2d/love) [![GitHub stars](https://img.shields.io/github/stars/love2d/love?style=flat)](https://github.com/love2d/love/stargazers) - 2D framework for writing game code with Lua. [[Awesome](https://github.com/love2d-community/awesome-love2d) [![GitHub stars](https://img.shields.io/github/stars/love2d-community/awesome-love2d?style=flat)](https://github.com/love2d-community/awesome-love2d/stargazers) | [Website](https://love2d.org)]
    - 🎉 [Vectarine](https://github.com/vanyle/vectarine) [![GitHub stars](https://img.shields.io/github/stars/vanyle/vectarine?style=flat)](https://github.com/vanyle/vectarine/stargazers) - A cross-platform game engine for fast prototyping with Lua and Luau [[Website](http://vectarine.surge.sh/)]

### Java
- 📚 [Awesome Java](https://github.com/akullpp/awesome-java) [![GitHub stars](https://img.shields.io/github/stars/akullpp/awesome-java?style=flat)](https://github.com/akullpp/awesome-java/stargazers) - Awesome frameworks, libraries and software for Java.
- 🌎 [Java](https://dev.java) - General-purpose language, runs on [Java virtual machines](https://en.wikipedia.org/wiki/Java_virtual_machine). [[GitHub](https://github.com/openjdk) [![GitHub stars](https://img.shields.io/github/stars/openjdk?style=flat)](https://github.com/openjdk/stargazers)]
- 📚 [Learn Java](https://dev.java/learn/) - Official docs and tutorials.
- 📚 [OpenGL & GLSL Tutorials](https://github.com/mattdesl/lwjgl-basics/wiki) [![GitHub stars](https://img.shields.io/github/stars/mattdesl/lwjgl-basics/wiki?style=flat)](https://github.com/mattdesl/lwjgl-basics/wiki/stargazers) - OpenGL / GLSL tutorials for _LWJGL_ and _libGDX_.
- Java: Game Framework
    - 🎉 [jMonkeyEngine](https://github.com/jMonkeyEngine/jmonkeyengine) [![GitHub stars](https://img.shields.io/github/stars/jMonkeyEngine/jmonkeyengine?style=flat)](https://github.com/jMonkeyEngine/jmonkeyengine/stargazers) - Modern 3D game development suite.
    - 🎉 [libGDX](https://github.com/libgdx/libgdx) [![GitHub stars](https://img.shields.io/github/stars/libgdx/libgdx?style=flat)](https://github.com/libgdx/libgdx/stargazers) - Game framework built on, and adds to _LWJGL_. [[Awesome](https://github.com/rafaskb/awesome-libgdx) [![GitHub stars](https://img.shields.io/github/stars/rafaskb/awesome-libgdx?style=flat)](https://github.com/rafaskb/awesome-libgdx/stargazers) | [Website](https://libgdx.com/)]
    - 🎉 [LWJGL](https://github.com/LWJGL/lwjgl3) [![GitHub stars](https://img.shields.io/github/stars/LWJGL/lwjgl3?style=flat)](https://github.com/LWJGL/lwjgl3/stargazers) - Graphics, audio, parallel computing, XR and more. [[Website](https://www.lwjgl.org/)]
- Java: Gui
    - 🎉 [VisUI](https://github.com/kotcrab/vis-ui) [![GitHub stars](https://img.shields.io/github/stars/kotcrab/vis-ui?style=flat)](https://github.com/kotcrab/vis-ui/stargazers) - A _libGDX_ UI toolkit.

### JavaScript
- 📚 [Awesome JavaScript](https://github.com/sorrycc/awesome-javascript) [![GitHub stars](https://img.shields.io/github/stars/sorrycc/awesome-javascript?style=flat)](https://github.com/sorrycc/awesome-javascript/stargazers) - Collection of browser-side JavaScript libraries and resources.
- 📚 [Eloquent JavaScript](https://eloquentjavascript.net) - Modern JavaScript programming, with examples.
- 🌎 [MDN](https://developer.mozilla.org/en-US/) - Mozilla Developer Network, excellent learning resource.
- 🌎 [W3 Schools](https://www.w3schools.com/default.asp) - Learn to code with the world's largest web developer site.
- JavaScript: Animation
    - 🎉 [Animate.css](https://github.com/animate-css/animate.css) [![GitHub stars](https://img.shields.io/github/stars/animate-css/animate.css?style=flat)](https://github.com/animate-css/animate.css/stargazers) - Ready-to-use, pure CSS animations. [[Examples](https://animate.style/)]
    - 🎉 [D3.js](https://github.com/d3/d3) [![GitHub stars](https://img.shields.io/github/stars/d3/d3?style=flat)](https://github.com/d3/d3/stargazers) - Data-Driven Documents. Bring data to life with SVG, canvas and HTML. [[Examples](https://observablehq.com/@d3/gallery) | [Website](https://d3js.org)]
    - 💸 [GreenSock](https://github.com/greensock/GSAP) [![GitHub stars](https://img.shields.io/github/stars/greensock/GSAP?style=flat)](https://github.com/greensock/GSAP/stargazers) - Robust animation toolset. [[Website](https://greensock.com)]
    - 🎉 [Ossos](https://github.com/sketchpunklabs/ossos) [![GitHub stars](https://img.shields.io/github/stars/sketchpunklabs/ossos?style=flat)](https://github.com/sketchpunklabs/ossos/stargazers) - Web-based character animation system.
    - 🎉 [React-Spring](https://github.com/pmndrs/react-spring) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/react-spring?style=flat)](https://github.com/pmndrs/react-spring/stargazers) - Spring physics based React animation library.
    - 🎉 [Scene.js](https://github.com/daybrush/scenejs) [![GitHub stars](https://img.shields.io/github/stars/daybrush/scenejs?style=flat)](https://github.com/daybrush/scenejs/stargazers) - JavaScript & CSS timeline-based animation library.
    - 🎉 [Theatre](https://github.com/theatre-js/theatre) [![GitHub stars](https://img.shields.io/github/stars/theatre-js/theatre?style=flat)](https://github.com/theatre-js/theatre/stargazers) - Motion design editor for the web.
    - 🎉 [Tween.js](https://github.com/tweenjs/tween.js) [![GitHub stars](https://img.shields.io/github/stars/tweenjs/tween.js?style=flat)](https://github.com/tweenjs/tween.js/stargazers) - Tweening engine for easy animations using Robert Penner's equations.
    - 🎉 [TweenJS](https://github.com/CreateJS/TweenJS) [![GitHub stars](https://img.shields.io/github/stars/CreateJS/TweenJS?style=flat)](https://github.com/CreateJS/TweenJS/stargazers) - Tweening / animation library, part of the _CreateJS_ suite.
- JavaScript: Audio
    - 🎉 [Howler.js](https://github.com/goldfire/howler.js) [![GitHub stars](https://img.shields.io/github/stars/goldfire/howler.js?style=flat)](https://github.com/goldfire/howler.js/stargazers) - Audio made easy and reliable across all platforms.
    - 🎉 [PixiJS Sound](https://github.com/pixijs/sound) [![GitHub stars](https://img.shields.io/github/stars/pixijs/sound?style=flat)](https://github.com/pixijs/sound/stargazers) - Audio library with filters, built on _PixiJS_. [[Examples](https://pixijs.io/sound/examples/)]
    - 🎉 [SoundJS](https://github.com/CreateJS/SoundJS) [![GitHub stars](https://img.shields.io/github/stars/CreateJS/SoundJS?style=flat)](https://github.com/CreateJS/SoundJS/stargazers) - Simple API and powerful features, part of the _CreateJS_ suite.
    - 🎉 [Sonant-X](https://github.com/nicolas-van/sonant-x) [![GitHub stars](https://img.shields.io/github/stars/nicolas-van/sonant-x?style=flat)](https://github.com/nicolas-van/sonant-x/stargazers) - Small JavaScript synthesizer library. [[Online Composer](https://nicolas-van.github.io/sonant-x-live/)]
    - 🎉 [SpessaSynth](https://github.com/spessasus/SpessaSynth) [![GitHub stars](https://img.shields.io/github/stars/spessasus/SpessaSynth?style=flat)](https://github.com/spessasus/SpessaSynth/stargazers) - MIDI player and synthesizer.
    - 🎉 [Tone.js](https://github.com/Tonejs/Tone.js) [![GitHub stars](https://img.shields.io/github/stars/Tonejs/Tone.js?style=flat)](https://github.com/Tonejs/Tone.js/stargazers) - WebAudio framework for creating interactive music in the browser.
    - 🎉 [tuna](https://github.com/Theodeus/tuna) [![GitHub stars](https://img.shields.io/github/stars/Theodeus/tuna?style=flat)](https://github.com/Theodeus/tuna/stargazers) - Audio effects library for the WebAudio API.
    - 🎉 [Waveform Playlist](https://github.com/naomiaro/waveform-playlist) [![GitHub stars](https://img.shields.io/github/stars/naomiaro/waveform-playlist?style=flat)](https://github.com/naomiaro/waveform-playlist/stargazers) - Multitrack web audio editor and player with canvas waveform preview.
- JavaScript: Color
    - 🎉 [Chroma.js](https://github.com/gka/chroma.js) [![GitHub stars](https://img.shields.io/github/stars/gka/chroma.js?style=flat)](https://github.com/gka/chroma.js/stargazers) - Library for all kinds of color manipulations.
- JavaScript: Cross-Platform
    - 🎉 [Apache Cordova](https://cordova.apache.org) - Mobile apps (iOS / Android) with with JavaScript, HTML, and CSS.
    - 🎉 [Capacitor](https://github.com/ionic-team/capacitor) [![GitHub stars](https://img.shields.io/github/stars/ionic-team/capacitor?style=flat)](https://github.com/ionic-team/capacitor/stargazers) - Run web apps natively on iOS, Android, Web, and more. [[Website](https://capacitorjs.com/)]
    - 🎉 [Electron](https://github.com/electron/electron) [![GitHub stars](https://img.shields.io/github/stars/electron/electron?style=flat)](https://github.com/electron/electron/stargazers) - Cross-platform desktop apps with JavaScript, HTML, and CSS. [[Website](https://www.electronjs.org/)]
    - 📚 [Electron Alternatives](https://github.com/sudhakar3697/electron-alternatives) [![GitHub stars](https://img.shields.io/github/stars/sudhakar3697/electron-alternatives?style=flat)](https://github.com/sudhakar3697/electron-alternatives/stargazers) - Cross-platform gui app development options.
    - 🎉 [Ejecta](https://github.com/phoboslab/Ejecta) [![GitHub stars](https://img.shields.io/github/stars/phoboslab/Ejecta?style=flat)](https://github.com/phoboslab/Ejecta/stargazers) - JavaScript canvas & audio implementation for iOS. App store compatible.
    - 🎉 [NW.js](https://github.com/nwjs/nw.js) [![GitHub stars](https://img.shields.io/github/stars/nwjs/nw.js?style=flat)](https://github.com/nwjs/nw.js/stargazers) - Desktop apps with JavaScript. Formerly _Node-Webkit_. [[Website](https://nwjs.io)]
    - 🎉 [nx.js](https://github.com/TooTallNate/nx.js/) [![GitHub stars](https://img.shields.io/github/stars/TooTallNate/nx.js/?style=flat)](https://github.com/TooTallNate/nx.js//stargazers) - JavaScript runtime for Nintendo Switch homebrew applications.
    - 📚 [Progressive Web Apps](https://web.dev/progressive-web-apps/) - Using web tech in a way that feels like platform-specific apps.
    - 🎉 [React Native](https://github.com/facebook/react-native) [![GitHub stars](https://img.shields.io/github/stars/facebook/react-native?style=flat)](https://github.com/facebook/react-native/stargazers) - Framework for building native apps using React. [[Website](https://reactnative.dev/)]
    - 🎉 [Tauri](https://github.com/tauri-apps/tauri) [![GitHub stars](https://img.shields.io/github/stars/tauri-apps/tauri?style=flat)](https://github.com/tauri-apps/tauri/stargazers) - Smaller, faster, and more secure desktop applications. [[Website](https://tauri.app/)]
    - 💸 [Ultralight](https://ultralig.ht/) - Supports modern HTML5, CSS, and JavaScript. Based on _WebKit_.
    - 🎉 [WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) - Microsoft Edge control allows you to embed web in native apps. [[Docs](https://learn.microsoft.com/en-us/microsoft-edge/webview2/)]
    - 🎉 [Window.js](https://github.com/windowjs/windowjs) [![GitHub stars](https://img.shields.io/github/stars/windowjs/windowjs?style=flat)](https://github.com/windowjs/windowjs/stargazers) - JavaScript runtime for desktop graphics programming. [[Docs](https://windowjs.org/)]
- JavaScript: Docking
    - 🎉 [Dock Spawn TS](https://github.com/node-projects/dock-spawn-ts) [![GitHub stars](https://img.shields.io/github/stars/node-projects/dock-spawn-ts?style=flat)](https://github.com/node-projects/dock-spawn-ts/stargazers) - Maintained, TypeScript version of [Dock Spawn](https://github.com/coderespawn/dock-spawn) [![GitHub stars](https://img.shields.io/github/stars/coderespawn/dock-spawn?style=flat)](https://github.com/coderespawn/dock-spawn/stargazers), a JavaScript docking framework.
    - 🎉 [FlexLayout](https://github.com/caplin/FlexLayout) [![GitHub stars](https://img.shields.io/github/stars/caplin/FlexLayout?style=flat)](https://github.com/caplin/FlexLayout/stargazers) - Multi-tab layout manager.
    - 🎉 [Golden Layout](https://github.com/golden-layout/golden-layout) [![GitHub stars](https://img.shields.io/github/stars/golden-layout/golden-layout?style=flat)](https://github.com/golden-layout/golden-layout/stargazers) - Multi-window layout manager for web apps.
    - 🎉 [PhosphorJS](https://github.com/phosphorjs/phosphor) [![GitHub stars](https://img.shields.io/github/stars/phosphorjs/phosphor?style=flat)](https://github.com/phosphorjs/phosphor/stargazers) - High-performance, pluggable, desktop-style web apps.
    - 🎉 [React Mosaic](https://github.com/nomcopter/react-mosaic) [![GitHub stars](https://img.shields.io/github/stars/nomcopter/react-mosaic?style=flat)](https://github.com/nomcopter/react-mosaic/stargazers) - React tiling window manager.
    - 🎉 [RC-Dock](https://github.com/ticlo/rc-dock) [![GitHub stars](https://img.shields.io/github/stars/ticlo/rc-dock?style=flat)](https://github.com/ticlo/rc-dock/stargazers) - Dock layout component for React.
    - 🎉 [wcDocker](https://github.com/WebCabin/wcDocker) [![GitHub stars](https://img.shields.io/github/stars/WebCabin/wcDocker?style=flat)](https://github.com/WebCabin/wcDocker/stargazers) - Window layout system with a responsive and interactive design.
- JavaScript: Entity Component System
    - 🎉 [Becsy](https://github.com/LastOliveGames/becsy) [![GitHub stars](https://img.shields.io/github/stars/LastOliveGames/becsy?style=flat)](https://github.com/LastOliveGames/becsy/stargazers) - Multithreaded ECS for TypeScript and JavaScript.
    - 🔒 [bitECS](https://github.com/NateTheGreatt/bitECS) [![GitHub stars](https://img.shields.io/github/stars/NateTheGreatt/bitECS?style=flat)](https://github.com/NateTheGreatt/bitECS/stargazers) - Functional, minimal, data-oriented, ultra-high performance ECS library.
    - 🎉 [Ecsy](https://github.com/ecsyjs/ecsy) [![GitHub stars](https://img.shields.io/github/stars/ecsyjs/ecsy?style=flat)](https://github.com/ecsyjs/ecsy/stargazers) - Experimental ECS aiming to be lightweight, easy to use.
    - 🎉 [Miniplex](https://github.com/hmans/miniplex) [![GitHub stars](https://img.shields.io/github/stars/hmans/miniplex?style=flat)](https://github.com/hmans/miniplex/stargazers) - Entity management system for games.
- JavaScript: File Formats
    - 🎉 [JSMpeg](https://github.com/phoboslab/jsmpeg) [![GitHub stars](https://img.shields.io/github/stars/phoboslab/jsmpeg?style=flat)](https://github.com/phoboslab/jsmpeg/stargazers) - MPEG1 Video Decoder in JavaScript.
- JavaScript: Framework
    - 🎉 [Alpine](https://github.com/alpinejs/alpine) [![GitHub stars](https://img.shields.io/github/stars/alpinejs/alpine?style=flat)](https://github.com/alpinejs/alpine/stargazers) - Rugged, minimal framework for composing JavaScript behavior in your markup.
    - 🎉 [Angular](https://github.com/angular/angular) [![GitHub stars](https://img.shields.io/github/stars/angular/angular?style=flat)](https://github.com/angular/angular/stargazers) - The modern web developer's platform.
    - 🎉 [Aurelia](https://github.com/aurelia/framework) [![GitHub stars](https://img.shields.io/github/stars/aurelia/framework?style=flat)](https://github.com/aurelia/framework/stargazers) - Modern, front-end framework for browser, mobile, and desktop apps.
    - 🎉 [Ember](https://github.com/emberjs/ember.js) [![GitHub stars](https://img.shields.io/github/stars/emberjs/ember.js?style=flat)](https://github.com/emberjs/ember.js/stargazers) - Framework for ambitious web developers.
    - 🎉 [Preact](https://github.com/preactjs/preact) [![GitHub stars](https://img.shields.io/github/stars/preactjs/preact?style=flat)](https://github.com/preactjs/preact/stargazers) - Fast 3kB React alternative with the same modern API.
    - 🎉 [React](https://github.com/facebook/react/) [![GitHub stars](https://img.shields.io/github/stars/facebook/react/?style=flat)](https://github.com/facebook/react//stargazers) - Declarative, efficient, and flexible JavaScript library for building user interfaces.
    - 🎉 [Svelte](https://github.com/sveltejs/svelte) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/svelte?style=flat)](https://github.com/sveltejs/svelte/stargazers) - Takes your declarative components and converts them into efficient JavaScript.
    - 🎉 [Vue](https://github.com/vuejs/vue) [![GitHub stars](https://img.shields.io/github/stars/vuejs/vue?style=flat)](https://github.com/vuejs/vue/stargazers) - Progressive JavaScript framework for building UI on the web.
- JavaScript: Game Engines
    - 📚 [JavaScript Game Engines](https://github.com/collections/javascript-game-engines) [![GitHub stars](https://img.shields.io/github/stars/collections/javascript-game-engines?style=flat)](https://github.com/collections/javascript-game-engines/stargazers) - GitHub Collection of JavaScript / HTML5 game engines.
    - 📚 [JavaScript Wiki: Game Engines](https://github.com/bebraw/jswiki/wiki/Game-Engines) [![GitHub stars](https://img.shields.io/github/stars/bebraw/jswiki/wiki/Game-Engines?style=flat)](https://github.com/bebraw/jswiki/wiki/Game-Engines/stargazers) - JavaScript / HTML5 game engines and frameworks.
- JavaScript: Game Engine w/Editor
    - 🎉 [A-Frame](https://github.com/aframevr/aframe/) [![GitHub stars](https://img.shields.io/github/stars/aframevr/aframe/?style=flat)](https://github.com/aframevr/aframe//stargazers) - Web framework for building VR experiences. [[Website](https://aframe.io)]
    - 🎉 [Cocos Creator](https://github.com/cocos-creator/engine) [![GitHub stars](https://img.shields.io/github/stars/cocos-creator/engine?style=flat)](https://github.com/cocos-creator/engine/stargazers) - Cross-Platform 2D/3D game creation. [[Website](https://www.cocos.com/en/creator)]
    - 🎉 [ct.js](https://github.com/ct-js/ct-js) [![GitHub stars](https://img.shields.io/github/stars/ct-js/ct-js?style=flat)](https://github.com/ct-js/ct-js/stargazers) - Desktop 2D game engine, built on _PixiJS_.
    - 🎉 [Egret](https://github.com/egret-labs/egret-core) [![GitHub stars](https://img.shields.io/github/stars/egret-labs/egret-core?style=flat)](https://github.com/egret-labs/egret-core/stargazers) - Mobile game engine. [[Editor](https://github.com/egret-labs/egret-ui-editor-opensource) [![GitHub stars](https://img.shields.io/github/stars/egret-labs/egret-ui-editor-opensource?style=flat)](https://github.com/egret-labs/egret-ui-editor-opensource/stargazers)]
    - 🎉 [GDevelop](https://github.com/4ian/GDevelop) [![GitHub stars](https://img.shields.io/github/stars/4ian/GDevelop?style=flat)](https://github.com/4ian/GDevelop/stargazers) - Full-featured 2D game development. [[Website](https://gdevelop.io/)]
    - 🎉 [Impact](https://github.com/phoboslab/impact) [![GitHub stars](https://img.shields.io/github/stars/phoboslab/impact?style=flat)](https://github.com/phoboslab/impact/stargazers) - Game engine for desktop and mobile browsers. [[2D Level Editor](https://impactjs.com/documentation/weltmeister)]
    - 🔒 [Infinite Reality Engine](https://github.com/ir-engine/ir-engine) [![GitHub stars](https://img.shields.io/github/stars/ir-engine/ir-engine?style=flat)](https://github.com/ir-engine/ir-engine/stargazers) - 3D toolkit for the social spatial web. Formerly _Ethereal Engine_.
    - 🎉 [Isogenic](https://github.com/irrelon/ige) [![GitHub stars](https://img.shields.io/github/stars/irrelon/ige?style=flat)](https://github.com/irrelon/ige/stargazers) - Engine with advanced multiplayer, based on _Valve_'s multiplayer system.
    - 🎉 [melonJS](https://github.com/melonjs/melonJS) [![GitHub stars](https://img.shields.io/github/stars/melonjs/melonJS?style=flat)](https://github.com/melonjs/melonJS/stargazers) - Modern 2D game engine, level editing with [Tiled](https://doc.mapeditor.org/en/stable/). [[Website](https://melonjs.org)]
    - 🎉 [microStudio](https://github.com/pmgl/microstudio/) [![GitHub stars](https://img.shields.io/github/stars/pmgl/microstudio/?style=flat)](https://github.com/pmgl/microstudio//stargazers) - Online game engine. Learn and practice programming.
    - 🎉 [Pixelbox.js](https://github.com/cstoquer/pixelbox) [![GitHub stars](https://img.shields.io/github/stars/cstoquer/pixelbox?style=flat)](https://github.com/cstoquer/pixelbox/stargazers) - Sandbox to fast-prototype 2D tile-based games. [[Download](https://pixwlk.itch.io/pixelbox)]
    - 🎉 [QICI Engine](https://github.com/qiciengine/qiciengine) [![GitHub stars](https://img.shields.io/github/stars/qiciengine/qiciengine?style=flat)](https://github.com/qiciengine/qiciengine/stargazers) - Toolset for making games.
    - 🎉 [Superpowers](https://github.com/superpowers) [![GitHub stars](https://img.shields.io/github/stars/superpowers?style=flat)](https://github.com/superpowers/stargazers) - Both 2D & 3D game making for indies.
    - 🎉 [Taro](https://github.com/moddio/taro) [![GitHub stars](https://img.shields.io/github/stars/moddio/taro?style=flat)](https://github.com/moddio/taro/stargazers) - Multiplayer engine with _Box2D_ physics, aka _Moddio_. [[Website](https://www.modd.io)]
- JavaScript: Game Framework
    - 🎉 [Crafty](https://github.com/craftyjs/Crafty) [![GitHub stars](https://img.shields.io/github/stars/craftyjs/Crafty?style=flat)](https://github.com/craftyjs/Crafty/stargazers) - Create 2D games in a structured way.
    - 🎉 [Excalibur](https://github.com/excaliburjs/Excalibur) [![GitHub stars](https://img.shields.io/github/stars/excaliburjs/Excalibur?style=flat)](https://github.com/excaliburjs/Excalibur/stargazers) - Friendly TypeScript 2D game engine for the web.
    - 🎉 [Galacean](https://github.com/galacean/engine) [![GitHub stars](https://img.shields.io/github/stars/galacean/engine?style=flat)](https://github.com/galacean/engine/stargazers) - Web/Mobile-first engine built on WebGL and glTF.
    - 🎉 [Kaboom](https://github.com/replit/kaboom) [![GitHub stars](https://img.shields.io/github/stars/replit/kaboom?style=flat)](https://github.com/replit/kaboom/stargazers) - Simple 2D framework.
    - 🎉 [LittleJS](https://github.com/KilledByAPixel/LittleJS) [![GitHub stars](https://img.shields.io/github/stars/KilledByAPixel/LittleJS?style=flat)](https://github.com/KilledByAPixel/LittleJS/stargazers) - Lightweight 2D framework with WebGL rendering.
    - 🎉 [Meep](https://github.com/Usnul/meep) [![GitHub stars](https://img.shields.io/github/stars/Usnul/meep?style=flat)](https://github.com/Usnul/meep/stargazers) - ECS game framework.
    - 🎉 [Oasis](https://github.com/ant-galaxy/oasis-engine) [![GitHub stars](https://img.shields.io/github/stars/ant-galaxy/oasis-engine?style=flat)](https://github.com/ant-galaxy/oasis-engine/stargazers) - WebGL framework by _AntGroup_. 2D/3D, animation, physics.
    - 🎉 [Phaser](https://github.com/photonstorm/phaser) [![GitHub stars](https://img.shields.io/github/stars/photonstorm/phaser?style=flat)](https://github.com/photonstorm/phaser/stargazers) - Fast 2D game framework. [[Website](https://phaser.io)]
    - 🎉 [Turbulenz](https://github.com/turbulenz/turbulenz_engine) [![GitHub stars](https://img.shields.io/github/stars/turbulenz/turbulenz_engine?style=flat)](https://github.com/turbulenz/turbulenz_engine/stargazers) - Modular 2D/3D game framework for browsers, desktops and mobile.
    - 🎉 [WhitestormJS](https://github.com/WhitestormJS/whs.js) [![GitHub stars](https://img.shields.io/github/stars/WhitestormJS/whs.js?style=flat)](https://github.com/WhitestormJS/whs.js/stargazers) - Framework for 3D apps / games, built on _Three.js_.
- JavaScript: Geometry
    - 🎉 [Convexhull.js](https://github.com/indy256/convexhull-js) [![GitHub stars](https://img.shields.io/github/stars/indy256/convexhull-js?style=flat)](https://github.com/indy256/convexhull-js/stargazers) - High-performance JavaScript 2D convex hull library.
    - 🎉 [Delaunator](https://github.com/mapbox/delaunator) [![GitHub stars](https://img.shields.io/github/stars/mapbox/delaunator?style=flat)](https://github.com/mapbox/delaunator/stargazers) - Incredibly fast JavaScript library for Delaunay triangulation of 2D points.
    - 🎉 [Earcut](https://github.com/mapbox/earcut) [![GitHub stars](https://img.shields.io/github/stars/mapbox/earcut?style=flat)](https://github.com/mapbox/earcut/stargazers) - The fastest and smallest JavaScript polygon triangulation library for your WebGL apps.
    - 🎉 [Poly-Decomp.js](https://github.com/schteppe/poly-decomp.js) [![GitHub stars](https://img.shields.io/github/stars/schteppe/poly-decomp.js?style=flat)](https://github.com/schteppe/poly-decomp.js/stargazers) - Decompose 2D polygons into convex pieces.
- JavaScript: Graphics - 2D
    - 🎉 [CanvasKit](https://github.com/google/skia/tree/main/modules/canvaskit) [![GitHub stars](https://img.shields.io/github/stars/google/skia/tree/main/modules/canvaskit?style=flat)](https://github.com/google/skia/tree/main/modules/canvaskit/stargazers) - WebAssembly build of _Google_'s 2D graphics library, Skia. [[Samples](https://skia.org/docs/user/modules/canvaskit/)]
    - 🎉 [EaselJS](https://github.com/CreateJS/EaselJS) [![GitHub stars](https://img.shields.io/github/stars/CreateJS/EaselJS?style=flat)](https://github.com/CreateJS/EaselJS/stargazers) - Makes working with the canvas element easy, part of [CreateJS](https://createjs.com/).
    - 🎉 [Escher.js](https://github.com/tentone/escher.js) [![GitHub stars](https://img.shields.io/github/stars/tentone/escher.js?style=flat)](https://github.com/tentone/escher.js/stargazers) - Interactive 2D graphics canvas framework.
    - 🎉 [Fabric.js](https://github.com/fabricjs/fabric.js) [![GitHub stars](https://img.shields.io/github/stars/fabricjs/fabric.js?style=flat)](https://github.com/fabricjs/fabric.js/stargazers) - Powerful and simple JavaScript canvas library.
    - 🎉 [Konva](https://github.com/konvajs/konva) [![GitHub stars](https://img.shields.io/github/stars/konvajs/konva?style=flat)](https://github.com/konvajs/konva/stargazers) - Canvas interactivity framework for desktop and mobile apps.
    - 🎉 [p5.js](https://github.com/processing/p5.js) [![GitHub stars](https://img.shields.io/github/stars/processing/p5.js?style=flat)](https://github.com/processing/p5.js/stargazers) - Library for creative coding. [[Website](https://p5js.org)]
    - 🎉 [Paper.js](https://github.com/paperjs/paper.js) [![GitHub stars](https://img.shields.io/github/stars/paperjs/paper.js?style=flat)](https://github.com/paperjs/paper.js/stargazers) - The swiss army knife of vector graphics. [[Examples](http://paperjs.org/)]
    - 🎉 [Pencil.js](https://github.com/pencil-js/pencil.js) [![GitHub stars](https://img.shields.io/github/stars/pencil-js/pencil.js?style=flat)](https://github.com/pencil-js/pencil.js/stargazers) - Modular interactive 2D drawing library. [[Examples](https://pencil.js.org/)]
    - 🎉 [PixiJS](https://github.com/pixijs/pixijs) [![GitHub stars](https://img.shields.io/github/stars/pixijs/pixijs?style=flat)](https://github.com/pixijs/pixijs/stargazers) 🔥 - Fast, lightweight 2D library. [[Awesome](https://github.com/cursedcoder/awesome-pixijs) [![GitHub stars](https://img.shields.io/github/stars/cursedcoder/awesome-pixijs?style=flat)](https://github.com/cursedcoder/awesome-pixijs/stargazers) | [Editor](https://github.com/Megabyteceer/thing-editor) [![GitHub stars](https://img.shields.io/github/stars/Megabyteceer/thing-editor?style=flat)](https://github.com/Megabyteceer/thing-editor/stargazers) | [Essentials](https://github.com/ShukantPal/pixi-essentials) [![GitHub stars](https://img.shields.io/github/stars/ShukantPal/pixi-essentials?style=flat)](https://github.com/ShukantPal/pixi-essentials/stargazers) | [Website](https://pixijs.com/)]
    - 🎉 [Pts](https://github.com/williamngan/pts) [![GitHub stars](https://img.shields.io/github/stars/williamngan/pts?style=flat)](https://github.com/williamngan/pts/stargazers) - Library for visualization and creative coding. [[Examples](https://ptsjs.org)]
    - 🎉 [Scrawl-canvas](https://github.com/KaliedaRik/Scrawl-canvas) [![GitHub stars](https://img.shields.io/github/stars/KaliedaRik/Scrawl-canvas?style=flat)](https://github.com/KaliedaRik/Scrawl-canvas/stargazers) - Library for working with the canvas element.
    - 🎉 [Stage.js](https://github.com/piqnt/stage.js) [![GitHub stars](https://img.shields.io/github/stars/piqnt/stage.js?style=flat)](https://github.com/piqnt/stage.js/stargazers) - 2D rendering engine for game development. [[Examples](https://piqnt.com/stage.js/)]
    - 🎉 [Two.js](https://github.com/jonobr1/two.js) [![GitHub stars](https://img.shields.io/github/stars/jonobr1/two.js?style=flat)](https://github.com/jonobr1/two.js/stargazers) - Renderer agnostic 2D drawing API for the web.
    - 🎉 [ZIM](https://github.com/danzen/zimjs) [![GitHub stars](https://img.shields.io/github/stars/danzen/zimjs?style=flat)](https://github.com/danzen/zimjs/stargazers) - Creative canvas framework. [[Website](https://zimjs.com/)]
- JavaScript: Graphics - 3D
    - 🎉 [Babylon.js](https://github.com/BabylonJS/Babylon.js) [![GitHub stars](https://img.shields.io/github/stars/BabylonJS/Babylon.js?style=flat)](https://github.com/BabylonJS/Babylon.js/stargazers) 🔥 - Powerful web rendering engine. [[Extensions](https://github.com/BabylonJS/Extensions) [![GitHub stars](https://img.shields.io/github/stars/BabylonJS/Extensions?style=flat)](https://github.com/BabylonJS/Extensions/stargazers) | [Website](https://www.babylonjs.com/)]
    - 🎉 [ClayGL](https://github.com/pissang/claygl) [![GitHub stars](https://img.shields.io/github/stars/pissang/claygl?style=flat)](https://github.com/pissang/claygl/stargazers) - WebGL library for scalable Web3D applications.
    - 🎉 [CopperLicht](https://ambiera.com/copperlicht/) - A 3D library for WebGL. [[CopperCube Editor](https://ambiera.com/coppercube/index.html)]
    - 🎉 [Filament for Web](https://github.com/google/filament/tree/main/web/filament-js) [![GitHub stars](https://img.shields.io/github/stars/google/filament/tree/main/web/filament-js?style=flat)](https://github.com/google/filament/tree/main/web/filament-js/stargazers) - WebAssembly build of Google's 3D graphics library, _Filament_.
    - 🎉 [Four](https://github.com/CodyJasonBennett/four) [![GitHub stars](https://img.shields.io/github/stars/CodyJasonBennett/four?style=flat)](https://github.com/CodyJasonBennett/four/stargazers) - Minimal three.js alternative.
    - 🎉 [Hilo3d](https://github.com/hiloteam/Hilo3d) [![GitHub stars](https://img.shields.io/github/stars/hiloteam/Hilo3d?style=flat)](https://github.com/hiloteam/Hilo3d/stargazers) - WebGL 3D rendering engine by _Alibaba_.
    - 🎉 [Litescene.js](https://github.com/jagenjo/litescene.js) [![GitHub stars](https://img.shields.io/github/stars/jagenjo/litescene.js?style=flat)](https://github.com/jagenjo/litescene.js/stargazers) - WebGL 3D engine library, used by WebGLStudio.
    - 🎉 [LUME](https://github.com/lume/lume) [![GitHub stars](https://img.shields.io/github/stars/lume/lume?style=flat)](https://github.com/lume/lume/stargazers) - Simplifies the creation of interactive 2D/3D experiences.
    - ⭐ [OGL](https://github.com/oframe/ogl) [![GitHub stars](https://img.shields.io/github/stars/oframe/ogl?style=flat)](https://github.com/oframe/ogl/stargazers) 🔥 - Fast, powerful, minimal WebGL library. [[Examples](https://oframe.github.io/ogl/examples)]
    - 🎉 [PicoGL.js](https://github.com/tsherif/picogl.js) [![GitHub stars](https://img.shields.io/github/stars/tsherif/picogl.js?style=flat)](https://github.com/tsherif/picogl.js/stargazers) - Minimal WebGL 2 rendering library. [[Examples](https://tsherif.github.io/picogl.js/)]
    - 🎉 [Pixi3D](https://github.com/jnsmalm/pixi3d) [![GitHub stars](https://img.shields.io/github/stars/jnsmalm/pixi3d?style=flat)](https://github.com/jnsmalm/pixi3d/stargazers) - 3D renderer for _PixiJS_, seamless integration with 2D apps. [[Examples](https://pixi3d.org/)]
    - 🎉 [RedGL](https://github.com/redcamel/RedGL2) [![GitHub stars](https://img.shields.io/github/stars/redcamel/RedGL2?style=flat)](https://github.com/redcamel/RedGL2/stargazers) - JavaScript 3D WebGL library.
    - 🎉 [Regl](https://github.com/regl-project/regl) [![GitHub stars](https://img.shields.io/github/stars/regl-project/regl?style=flat)](https://github.com/regl-project/regl/stargazers) - Fast functional WebGL.
    - 🎉 [SwissGL](https://github.com/google/swissgl) [![GitHub stars](https://img.shields.io/github/stars/google/swissgl?style=flat)](https://github.com/google/swissgl/stargazers) - Minimalistic wrapper on top of WebGL2.
    - 🎉 [ThingJS](https://github.com/uinosoft/t3d.js) [![GitHub stars](https://img.shields.io/github/stars/uinosoft/t3d.js?style=flat)](https://github.com/uinosoft/t3d.js/stargazers) - Lightweight, extendable 3D library, aka _t3d_.
    - 🎉 [Three.js](https://github.com/mrdoob/three.js/) [![GitHub stars](https://img.shields.io/github/stars/mrdoob/three.js/?style=flat)](https://github.com/mrdoob/three.js//stargazers) 🔥 - General-purpose 3D library. [[Awesome](https://github.com/0xAxiome/awesome-threejs) [![GitHub stars](https://img.shields.io/github/stars/0xAxiome/awesome-threejs?style=flat)](https://github.com/0xAxiome/awesome-threejs/stargazers) | [Docs](https://threejs.org) | [Editor](https://threejs.org/editor/) | [Examples](https://threejs.org/examples/)]
    - 🎉 [TWGL](https://github.com/greggman/twgl.js) [![GitHub stars](https://img.shields.io/github/stars/greggman/twgl.js?style=flat)](https://github.com/greggman/twgl.js/stargazers) - Tiny WebGL helper Library. [[Examples](http://twgljs.org/)]
    - 📚 [WebGL Frameworks](https://en.wikipedia.org/wiki/List_of_WebGL_frameworks) - List of WebGL frameworks on Wikipedia.
    - 📚 [WebGL / WebGPU Frameworks](https://gist.github.com/76878ba6903cf15789b712464875cfdc) -  List of WebGL and WebGPU frameworks and libraries.
    - 🎉 [x3dom](https://github.com/x3dom/x3dom) [![GitHub stars](https://img.shields.io/github/stars/x3dom/x3dom?style=flat)](https://github.com/x3dom/x3dom/stargazers) - Integrate 3D content seamlessly into your webpage.
- JavaScript: Graphics - Three.js
    - 📚 [Discover Three.js](https://discoverthreejs.com) - Create stunning 3D web apps using Three.js.
    - 🌎 [SBcode Three.js Tutorials](https://sbcode.net/threejs/) - Fantastic examples with code and explanations of topics.
    - 🎉 [Sketch Three.js](https://github.com/ykob/sketch-threejs) [![GitHub stars](https://img.shields.io/github/stars/ykob/sketch-threejs?style=flat)](https://github.com/ykob/sketch-threejs/stargazers) - Interactive sketches made with Three.js.
    - 🎉 [Sketchbook](https://github.com/swift502/Sketchbook) [![GitHub stars](https://img.shields.io/github/stars/swift502/Sketchbook?style=flat)](https://github.com/swift502/Sketchbook/stargazers) - 3D playground built on Three.js and Cannon.js.
    - 🌎 [Stemkoski Three.js Examples](http://stemkoski.github.io/Three.js/) - Excellent set of instructive examples.
    - 📚 [Three.js Bookshelf](https://discourse.threejs.org/t/three-js-bookshelf/2468) - Nice collection of resources.
    - 📚 [Three.js Discourse Examples](https://hofk.de/main/discourse.threejs/) - Yearly collection of all examples posted on the Three.js forum.
    - 💰 [Three.js Journey](https://threejs-journey.com/) - Course teaching WebGL from beginner to advanced.
    - 📚 [Three.js Manual](https://threejs.org/manual/#en/fundamentals) - Fantastic articles and explanations. Formerly _ThreeJsFundamentals_.
    - 📚 [THREEx](https://github.com/jeromeetienne/threex) [![GitHub stars](https://img.shields.io/github/stars/jeromeetienne/threex?style=flat)](https://github.com/jeromeetienne/threex/stargazers) - Nice collection of open source game extensions.
- JavaScript: Graphics - Three.js - Addon
    - 🎉 [Custom Shader Material](https://github.com/FarazzShaikh/THREE-CustomShaderMaterial) [![GitHub stars](https://img.shields.io/github/stars/FarazzShaikh/THREE-CustomShaderMaterial?style=flat)](https://github.com/FarazzShaikh/THREE-CustomShaderMaterial/stargazers) - Extend Three.js materials with your own shaders.
    - 🎉 [irregular-grid](https://github.com/sketchpunklabs/irregular_grid) [![GitHub stars](https://img.shields.io/github/stars/sketchpunklabs/irregular_grid?style=flat)](https://github.com/sketchpunklabs/irregular_grid/stargazers) - Examples of generating and using irregular grids. [[Demos](https://sketchpunklabs.github.io/irregular_grid/)]
    - 🎉 [Lamina](https://github.com/pmndrs/lamina) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/lamina?style=flat)](https://github.com/pmndrs/lamina/stargazers) - Extensible, layered shader material for Three.js.
    - ❓ [screen-space-reflections](https://github.com/0beqz/screen-space-reflections) [![GitHub stars](https://img.shields.io/github/stars/0beqz/screen-space-reflections?style=flat)](https://github.com/0beqz/screen-space-reflections/stargazers) - Screen space reflections in Three.js.
    - 🎉 [three-billboard-reflection](https://github.com/0beqz/three-billboard-reflection) [![GitHub stars](https://img.shields.io/github/stars/0beqz/three-billboard-reflection?style=flat)](https://github.com/0beqz/three-billboard-reflection/stargazers) - Performant plane reflections in Three.js.
    - 🎉 [three-mesh-bvh](https://github.com/gkjohnson/three-mesh-bvh) [![GitHub stars](https://img.shields.io/github/stars/gkjohnson/three-mesh-bvh?style=flat)](https://github.com/gkjohnson/three-mesh-bvh/stargazers) - Speed up raycasting and enable spatial queries on Meshes.
    - 🎉 [three-mesh-ui](https://github.com/felixmariotto/three-mesh-ui) [![GitHub stars](https://img.shields.io/github/stars/felixmariotto/three-mesh-ui?style=flat)](https://github.com/felixmariotto/three-mesh-ui/stargazers) - VR user interfaces for Three.js.
    - 🎉 [three-nebula](https://github.com/creativelifeform/three-nebula) [![GitHub stars](https://img.shields.io/github/stars/creativelifeform/three-nebula?style=flat)](https://github.com/creativelifeform/three-nebula/stargazers) - WebGL particle system for Three.js. [[Examples](https://three-nebula.org/examples/custom-renderer)]
    - 🎉 [three-projected-material](https://github.com/marcofugaro/three-projected-material) [![GitHub stars](https://img.shields.io/github/stars/marcofugaro/three-projected-material?style=flat)](https://github.com/marcofugaro/three-projected-material/stargazers) - Texture projection in Three.js.
    - 🎉 [three.ik](https://github.com/jsantell/THREE.IK) [![GitHub stars](https://img.shields.io/github/stars/jsantell/THREE.IK?style=flat)](https://github.com/jsantell/THREE.IK/stargazers) - Inverse kinematics for Three.js.
    - 🎉 [Troika JS - Derived Material](https://github.com/protectwise/troika/blob/master/packages/troika-three-utils/src/DerivedMaterial.js) [![GitHub stars](https://img.shields.io/github/stars/protectwise/troika/blob/master/packages/troika-three-utils/src/DerivedMaterial.js?style=flat)](https://github.com/protectwise/troika/blob/master/packages/troika-three-utils/src/DerivedMaterial.js/stargazers) - Extend existing Three.js materials. [[Docs](https://protectwise.github.io/troika/troika-three-utils/createDerivedMaterial/)]
    - 🎉 [voxelizer](https://github.com/andstor/voxelizer) [![GitHub stars](https://img.shields.io/github/stars/andstor/voxelizer?style=flat)](https://github.com/andstor/voxelizer/stargazers) - Voxelization of 3D models.
- JavaScript: Graphics - Three.js - React
    - 🎉 [drei](https://github.com/pmndrs/drei) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/drei?style=flat)](https://github.com/pmndrs/drei/stargazers) - Useful helpers for react-three-fiber.
    - 🎉 [gltfjsx](https://github.com/pmndrs/gltfjsx) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/gltfjsx?style=flat)](https://github.com/pmndrs/gltfjsx/stargazers) - Turns GLTFs into JSX components.
    - 🎉 [react-three-fiber](https://github.com/pmndrs/react-three-fiber) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/react-three-fiber?style=flat)](https://github.com/pmndrs/react-three-fiber/stargazers) - React renderer for Three.js.
- JavaScript: Graphics - Three.js - Svelte
    - 🎉 [Threlte](https://github.com/threlte/threlte) [![GitHub stars](https://img.shields.io/github/stars/threlte/threlte?style=flat)](https://github.com/threlte/threlte/stargazers) - 3D framework and ecosystem for Svelte and Three.js. [[Website](https://threlte.xyz/)]
- JavaScript: Gui
    - 🎉 [Bootstrap](https://github.com/twbs/bootstrap) [![GitHub stars](https://img.shields.io/github/stars/twbs/bootstrap?style=flat)](https://github.com/twbs/bootstrap/stargazers) - Popular. Develop responsive, mobile first projects. [[Website](https://getbootstrap.com/)]
    - 🎉 [dat.GUI](https://github.com/dataarts/dat.gui) [![GitHub stars](https://img.shields.io/github/stars/dataarts/dat.gui?style=flat)](https://github.com/dataarts/dat.gui/stargazers) - Lightweight gui for changing variables in JavaScript.
    - 🎉 [Dojo](https://github.com/dojo/widgets) [![GitHub stars](https://img.shields.io/github/stars/dojo/widgets?style=flat)](https://github.com/dojo/widgets/stargazers) - Gui widgets for web apps.
    - 🎉 [Guify](https://github.com/colejd/guify) [![GitHub stars](https://img.shields.io/github/stars/colejd/guify?style=flat)](https://github.com/colejd/guify/stargazers) - Simple gui for changing JavaScript variables. [[Demo](https://jons.website/projects/guify/)]
    - 🎉 [GuiGui](https://github.com/superguigui/guigui) [![GitHub stars](https://img.shields.io/github/stars/superguigui/guigui?style=flat)](https://github.com/superguigui/guigui/stargazers) - Gui for tweaking stuff in JavaScript. [[Demo](https://superguigui.github.io/guigui/)]
    - 🎉 [Inferno](https://github.com/infernojs/inferno) [![GitHub stars](https://img.shields.io/github/stars/infernojs/inferno?style=flat)](https://github.com/infernojs/inferno/stargazers) - React-like library for building high-performance user interfaces.
    - 🎉 [jQuery UI](https://github.com/jquery/jquery-ui) [![GitHub stars](https://img.shields.io/github/stars/jquery/jquery-ui?style=flat)](https://github.com/jquery/jquery-ui/stargazers) - The official gui library for jQuery.
    - 🎉 [Leva](https://github.com/pmndrs/leva) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/leva?style=flat)](https://github.com/pmndrs/leva/stargazers) - React-first components gui.
    - 🎉 [Magic Circle](https://github.com/dpwoert/magic-circle) [![GitHub stars](https://img.shields.io/github/stars/dpwoert/magic-circle?style=flat)](https://github.com/dpwoert/magic-circle/stargazers) - Multi-functional gui. Inspired by _dat.GUI_, _Unity_ and _Framer_.
    - 🎉 [PCUI](https://github.com/playcanvas/pcui) [![GitHub stars](https://img.shields.io/github/stars/playcanvas/pcui?style=flat)](https://github.com/playcanvas/pcui/stargazers) - UI component library for the web by _PlayCanvas_.
    - 🎉 [Tweakpane](https://github.com/cocopon/tweakpane) [![GitHub stars](https://img.shields.io/github/stars/cocopon/tweakpane?style=flat)](https://github.com/cocopon/tweakpane/stargazers) - Compact gui for fine-tuning values.
    - 🎉 [uil](https://github.com/lo-th/uil) [![GitHub stars](https://img.shields.io/github/stars/lo-th/uil?style=flat)](https://github.com/lo-th/uil/stargazers) - Simple JavaScript gui.
    - 🎉 [w2ui](https://github.com/vitmalina/w2ui) [![GitHub stars](https://img.shields.io/github/stars/vitmalina/w2ui?style=flat)](https://github.com/vitmalina/w2ui/stargazers) - Gui widgets for modern web apps.
    - 🎉 [Zebkit](https://github.com/barmalei/zebkit) [![GitHub stars](https://img.shields.io/github/stars/barmalei/zebkit?style=flat)](https://github.com/barmalei/zebkit/stargazers) - Canvas rendered UI component libary.
- JavaScript: Input
    - 🎉 [Joycon.js](https://github.com/barhatsor/joycon.js) [![GitHub stars](https://img.shields.io/github/stars/barhatsor/joycon.js?style=flat)](https://github.com/barhatsor/joycon.js/stargazers) - JavaScript controller functionality.
    - ❓ [Mesekai](https://github.com/Neleac/Mesekai) [![GitHub stars](https://img.shields.io/github/stars/Neleac/Mesekai?style=flat)](https://github.com/Neleac/Mesekai/stargazers) - Real-time motion tracking.
    - 🎉 [use-gesture](https://github.com/pmndrs/use-gesture) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/use-gesture?style=flat)](https://github.com/pmndrs/use-gesture/stargazers) - Utility for mouse / touch gestures in React and JavaScript.
    - 🔒 [WebAR.rocks.faceDepth](https://github.com/WebAR-rocks/WebAR.rocks.faceDepth) [![GitHub stars](https://img.shields.io/github/stars/WebAR-rocks/WebAR.rocks.faceDepth?style=flat)](https://github.com/WebAR-rocks/WebAR.rocks.faceDepth/stargazers) - Insert your face from your camera into a 3D scene.
- JavaScript: Layout
    - 📚 [Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) - Comprehensive guide to CSS flexbox layout.
    - 📚 [Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) - Comprehensive guide to CSS grid.
- JavaScript: Networking
    - 🎉 [Socket.io](https://github.com/socketio/socket.io) [![GitHub stars](https://img.shields.io/github/stars/socketio/socket.io?style=flat)](https://github.com/socketio/socket.io/stargazers) - Enables real-time bidirectional event-based communication.
    - 🎉 [WebRTC](https://webrtc.org/) - Supports video, voice, and generic data to be sent between peers.
- JavaScript: Physics
    - 🎉 [Ammo.js](https://github.com/kripken/ammo.js) [![GitHub stars](https://img.shields.io/github/stars/kripken/ammo.js?style=flat)](https://github.com/kripken/ammo.js/stargazers) - _Bullet 3D_ Physics engine ported as WebAssembly.
    - 🎉 [Box2d.js](https://github.com/kripken/box2d.js/) [![GitHub stars](https://img.shields.io/github/stars/kripken/box2d.js/?style=flat)](https://github.com/kripken/box2d.js//stargazers) - Box2D to ported as WebAssembly.
    - 🎉 [Cannon-es](https://github.com/pmndrs/cannon-es) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/cannon-es?style=flat)](https://github.com/pmndrs/cannon-es/stargazers) - Maintained fork of [Cannon.js](https://github.com/schteppe/cannon.js) [![GitHub stars](https://img.shields.io/github/stars/schteppe/cannon.js?style=flat)](https://github.com/schteppe/cannon.js/stargazers) 3D physics engine. [[Demos](https://pmndrs.github.io/cannon-es/)]
    - 🎉 [Goblin Physics](https://github.com/chandlerprall/GoblinPhysics) [![GitHub stars](https://img.shields.io/github/stars/chandlerprall/GoblinPhysics?style=flat)](https://github.com/chandlerprall/GoblinPhysics/stargazers) - 3D physics engine written from the ground up in JavaScript. [[Demos](http://www.goblinphysics.com/)]
    - 🎉 [JoltPhysics.js](https://github.com/jrouwe/JoltPhysics.js) [![GitHub stars](https://img.shields.io/github/stars/jrouwe/JoltPhysics.js?style=flat)](https://github.com/jrouwe/JoltPhysics.js/stargazers) - Port of _Jolt Physics_ to JavaScript (as WebAssembly). [[Demos](https://jrouwe.github.io/JoltPhysics.js/)]
    - 🎉 [Matter.js](https://github.com/liabru/matter-js) [![GitHub stars](https://img.shields.io/github/stars/liabru/matter-js?style=flat)](https://github.com/liabru/matter-js/stargazers) - Featured 2D physics engine for the web. [[Demos](https://brm.io/matter-js/)]
    - 🎉 [Oimo.js](https://github.com/lo-th/Oimo.js) [![GitHub stars](https://img.shields.io/github/stars/lo-th/Oimo.js?style=flat)](https://github.com/lo-th/Oimo.js/stargazers) - Lightweight 3D physics engine. [[Demos](http://lo-th.github.io/Oimo.js)]
    - 🎉 [p2.js](https://github.com/schteppe/p2.js) [![GitHub stars](https://img.shields.io/github/stars/schteppe/p2.js?style=flat)](https://github.com/schteppe/p2.js/stargazers) - 2D rigid body physics, by the creator of Cannon.js.
    - 🎉 [Particulate.js](https://github.com/jpweeks/particulate-js) [![GitHub stars](https://img.shields.io/github/stars/jpweeks/particulate-js?style=flat)](https://github.com/jpweeks/particulate-js/stargazers) - Particle physics library designed to be simple, fast and stable.
    - 🎉 [Planck.js](https://github.com/shakiba/planck.js) [![GitHub stars](https://img.shields.io/github/stars/shakiba/planck.js?style=flat)](https://github.com/shakiba/planck.js/stargazers) - JavaScript rewrite of the _Box2D_ physics engine. [[Demos](https://piqnt.com/planck.js/)]
    - 🎉 [Physijs](https://github.com/chandlerprall/Physijs) [![GitHub stars](https://img.shields.io/github/stars/chandlerprall/Physijs?style=flat)](https://github.com/chandlerprall/Physijs/stargazers) - Physics plugin for Three.js
    - 🎉 [Rapier](https://rapier.rs/docs/user_guides/javascript/getting_started_js) - Rust 2D/3D physics libary focused on performance, ported as WebAssembly.
    - 🎉 [Verly.js](https://github.com/anuraghazra/Verly.js) [![GitHub stars](https://img.shields.io/github/stars/anuraghazra/Verly.js?style=flat)](https://github.com/anuraghazra/Verly.js/stargazers) - Easy to integrate verlet physics engine. [[Demos](https://anuraghazra.dev/Verly.js/)]
- JavaScript: Utility
    - 🎉 [Clipboard.js](https://github.com/zenorocha/clipboard.js) [![GitHub stars](https://img.shields.io/github/stars/zenorocha/clipboard.js?style=flat)](https://github.com/zenorocha/clipboard.js/stargazers) - Small, modern copy to clipboard.
    - 🎉 [Day.js](https://github.com/iamkun/dayjs) [![GitHub stars](https://img.shields.io/github/stars/iamkun/dayjs?style=flat)](https://github.com/iamkun/dayjs/stargazers) - Fast 2kB alternative to [Moment.js](https://github.com/moment/moment) [![GitHub stars](https://img.shields.io/github/stars/moment/moment?style=flat)](https://github.com/moment/moment/stargazers) with the same modern API.
    - 🎉 [i18next](https://github.com/i18next/i18next) [![GitHub stars](https://img.shields.io/github/stars/i18next/i18next?style=flat)](https://github.com/i18next/i18next/stargazers) - Popular internationalization framework.
    - 🎉 [jQuery](https://github.com/jquery/jquery) [![GitHub stars](https://img.shields.io/github/stars/jquery/jquery?style=flat)](https://github.com/jquery/jquery/stargazers) - Fast and feature-rich JavaScript library. [[Website](https://jquery.com)]
    - 🎉 [PreloadJS](https://github.com/CreateJS/PreloadJS) [![GitHub stars](https://img.shields.io/github/stars/CreateJS/PreloadJS?style=flat)](https://github.com/CreateJS/PreloadJS/stargazers) - Preloading assets w/progress events.
    - 🎉 [Struct Vec](https://github.com/moomoolive/struct-vec) [![GitHub stars](https://img.shields.io/github/stars/moomoolive/struct-vec?style=flat)](https://github.com/moomoolive/struct-vec/stargazers) - JavaScript array-like containers for multithreading.
- JavaScript: Timeline
    - 🎉 [Frame.js](https://github.com/mrdoob/frame.js/) [![GitHub stars](https://img.shields.io/github/stars/mrdoob/frame.js/?style=flat)](https://github.com/mrdoob/frame.js//stargazers) - JavaScript sequence editor.
    - 🎉 [Neo](https://github.com/lo-th/neo) [![GitHub stars](https://img.shields.io/github/stars/lo-th/neo?style=flat)](https://github.com/lo-th/neo/stargazers) - Timeline for JavaScript. [[Demo](http://lo-th.github.io/neo/)]
- JavaScript: Video
    - 💸 [Remotion](https://github.com/remotion-dev/remotion) [![GitHub stars](https://img.shields.io/github/stars/remotion-dev/remotion?style=flat)](https://github.com/remotion-dev/remotion/stargazers) - Create videos programmatically in React. [[Website](https://www.remotion.dev/)]
- JavaScript: Visual Programming / Nodes
    - 🎉 [Butterfly](https://github.com/alibaba/butterfly) [![GitHub stars](https://img.shields.io/github/stars/alibaba/butterfly?style=flat)](https://github.com/alibaba/butterfly/stargazers) - Diagramming library concentrated on flow and field layout by _Alibaba_.
    - 🎉 [Drawflow](https://github.com/jerosoler/Drawflow) [![GitHub stars](https://img.shields.io/github/stars/jerosoler/Drawflow?style=flat)](https://github.com/jerosoler/Drawflow/stargazers) - Simple JavaScript flow library. [[Demo](https://jerosoler.github.io/Drawflow/)]
    - 🎉 [Flow](https://github.com/sunag/flow) [![GitHub stars](https://img.shields.io/github/stars/sunag/flow?style=flat)](https://github.com/sunag/flow/stargazers) - Node-graph library.
    - 🎉 [Litegraph.js](https://github.com/jagenjo/litegraph.js) [![GitHub stars](https://img.shields.io/github/stars/jagenjo/litegraph.js?style=flat)](https://github.com/jagenjo/litegraph.js/stargazers) - Create graphs in the browser similar to _Unreal Blueprints_. [[Demo](https://tamats.com/projects/litegraph/editor/)]
    - 🎉 [Node-RED](https://github.com/node-red/node-red) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red?style=flat)](https://github.com/node-red/node-red/stargazers) - Low-code programming for event-driven applications.
    - 🎉 [Nodl](https://github.com/emilwidlund/nodl) [![GitHub stars](https://img.shields.io/github/stars/emilwidlund/nodl?style=flat)](https://github.com/emilwidlund/nodl/stargazers) - Framework for computational node graphs.
    - 🎉 [Rete.js](https://github.com/retejs/rete) [![GitHub stars](https://img.shields.io/github/stars/retejs/rete?style=flat)](https://github.com/retejs/rete/stargazers) - Framework for visual programming and node editors. [[Demo](https://rete.js.org/#/examples/basic)]

### Kotlin
- 📚 [Awesome Kotlin](https://github.com/KotlinBy/awesome-kotlin) [![GitHub stars](https://img.shields.io/github/stars/KotlinBy/awesome-kotlin?style=flat)](https://github.com/KotlinBy/awesome-kotlin/stargazers) - List of awesome Kotlin related stuff.
- 🌎 [Kotlin](https://kotlinlang.org/) - General-purpose language, interoperates with Java. [[GitHub](https://github.com/JetBrains/kotlin) [![GitHub stars](https://img.shields.io/github/stars/JetBrains/kotlin?style=flat)](https://github.com/JetBrains/kotlin/stargazers)]
- Kotlin: Game Engine w/Editor
    - 🎉 [KorGE](https://github.com/korlibs/korge) [![GitHub stars](https://img.shields.io/github/stars/korlibs/korge?style=flat)](https://github.com/korlibs/korge/stargazers) - Multi-platform 2D game engine for Kotlin. [[Website](https://korge.org/)]
- Kotlin: Game Framework
    - 🎉 [FXGL](https://github.com/AlmasB/FXGL) [![GitHub stars](https://img.shields.io/github/stars/AlmasB/FXGL?style=flat)](https://github.com/AlmasB/FXGL/stargazers) - Game library for 2D, experimental 3D.
    - 🎉 [Kool](https://github.com/fabmax/kool) [![GitHub stars](https://img.shields.io/github/stars/fabmax/kool?style=flat)](https://github.com/fabmax/kool/stargazers) - Multi-platform 3D Vulkan / OpenGL graphics engine. [[Examples](https://fabmax.github.io/kool/kool-js/)]
    - 🎉 [KTX](https://github.com/libktx/ktx) [![GitHub stars](https://img.shields.io/github/stars/libktx/ktx?style=flat)](https://github.com/libktx/ktx/stargazers) - Kotlin extensions for the _libGDX_ game framework.

### Pascal
- 📚 [Awesome Pascal](https://github.com/Fr0sT-Brutal/awesome-pascal) [![GitHub stars](https://img.shields.io/github/stars/Fr0sT-Brutal/awesome-pascal?style=flat)](https://github.com/Fr0sT-Brutal/awesome-pascal/stargazers) - Curated list of Delphi / Pascal resources.
- 📚 [Delphi](https://en.wikipedia.org/wiki/Delphi_(software)) - Pascal dialect and popular IDE with cross-platform support.
- 🌎 [Free Pascal](https://www.freepascal.org/) - Mature, open source Pascal compiler.
- 📚 [Pascal Tutorials](https://www.tutorialspoint.com/pascal/index.htm) - Simple and easy Pascal tutorials.
- Pascal: Game Engine w/Editor
    - 🎉 [Castle](https://github.com/castle-engine/castle-engine) [![GitHub stars](https://img.shields.io/github/stars/castle-engine/castle-engine?style=flat)](https://github.com/castle-engine/castle-engine/stargazers) - Cross-platform 2D/3D game engine and editor. [[Website](https://castle-engine.io/)]
- Pascal: Game Framework
    - 🎉 [Apus](https://github.com/Cooler2/ApusGameEngine) [![GitHub stars](https://img.shields.io/github/stars/Cooler2/ApusGameEngine?style=flat)](https://github.com/Cooler2/ApusGameEngine/stargazers) - Cross-platform library for making 2D games.
- Pascal: Physics
    - 🎉 [Kraft](https://github.com/BeRo1985/kraft) [![GitHub stars](https://img.shields.io/github/stars/BeRo1985/kraft?style=flat)](https://github.com/BeRo1985/kraft/stargazers) - Object Pascal 3D physics engine.

### Python
- 📚 [Awesome Python](https://github.com/vinta/awesome-python) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers) - List of awesome Python frameworks, libraries, software and more.
- 🌎 [Python.org](https://www.python.org) - Programming language that lets you work quickly. [[Docs](https://www.python.org/doc/)]
- Python: App Framework
    - 🎉 [Pyglet](https://github.com/pyglet/pyglet) [![GitHub stars](https://img.shields.io/github/stars/pyglet/pyglet?style=flat)](https://github.com/pyglet/pyglet/stargazers) - Windowing and multimedia library intended for game development.
- Python: Cross-Platform
    - 💸 [Anvil](https://anvil.works) - Full stack web apps with nothing but Python.
    - 🎉 [Brython](https://github.com/brython-dev/brython) [![GitHub stars](https://img.shields.io/github/stars/brython-dev/brython?style=flat)](https://github.com/brython-dev/brython/stargazers) - Python 3 running in the browser.
- Python: Game Engine w/Editor
    - 💰 [Cave Engine](https://uniday.studio/) - Fast and easy Python game engine for 3D.
    - 🎉 [ursina](https://github.com/pokepetter/ursina) [![GitHub stars](https://img.shields.io/github/stars/pokepetter/ursina?style=flat)](https://github.com/pokepetter/ursina/stargazers) - Game engine powered by Python and _Panda3D_.
- Python: Game Framework
    - 🎉 [Arcade](https://github.com/pythonarcade/arcade) [![GitHub stars](https://img.shields.io/github/stars/pythonarcade/arcade?style=flat)](https://github.com/pythonarcade/arcade/stargazers) - Easy to use library for creating 2D arcade games.
    - 🎉 [Panda3D](https://github.com/panda3d/panda3d) [![GitHub stars](https://img.shields.io/github/stars/panda3d/panda3d?style=flat)](https://github.com/panda3d/panda3d/stargazers) - Powerful, mature game engine developed by _Disney_ and _Carnegie Mellon_. [[Website](https://www.panda3d.org)]
    - 🔒 [Pygame](https://github.com/pygame/pygame) [![GitHub stars](https://img.shields.io/github/stars/pygame/pygame?style=flat)](https://github.com/pygame/pygame/stargazers) - Game & multimedia app framework, built on _SDL_.
    - 🎉 [Pygcurse](https://github.com/asweigart/pygcurse) [![GitHub stars](https://img.shields.io/github/stars/asweigart/pygcurse?style=flat)](https://github.com/asweigart/pygcurse/stargazers) - [Curses-like](https://en.wikipedia.org/wiki/Curses_%28programming_library%29) library for text adventures / roguelikes. [[Website](http://inventwithpython.com/pygcurse/)]
- Python: Gui
    - 🎉 [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) [![GitHub stars](https://img.shields.io/github/stars/TomSchimansky/CustomTkinter?style=flat)](https://github.com/TomSchimansky/CustomTkinter/stargazers) - Modern, customizable UI-library based on _Tkinter_.
    - 🎉 [Kivy](https://github.com/kivy/kivy) [![GitHub stars](https://img.shields.io/github/stars/kivy/kivy?style=flat)](https://github.com/kivy/kivy/stargazers) - Cross-platform gui framework. [[Website](https://kivy.org/)]
    - 🎉 [NiceGUI](https://github.com/zauberzeug/nicegui/) [![GitHub stars](https://img.shields.io/github/stars/zauberzeug/nicegui/?style=flat)](https://github.com/zauberzeug/nicegui//stargazers) - Create web-based user interfaces with Python.
    - 🔒 [PySide](https://doc.qt.io/qtforpython-6/) - Official Python bindings for _Qt_.
    - 💸 [PyQt](https://riverbankcomputing.com/software/pyqt/intro) - Python bindings for _Qt_.
    - 📚 [tkinter](https://docs.python.org/3/library/tkinter.html) - Standard Python interface to the Tcl/Tk GUI toolkit.

### Ruby
- 📚 [Awesome Ruby](https://github.com/markets/awesome-ruby) [![GitHub stars](https://img.shields.io/github/stars/markets/awesome-ruby?style=flat)](https://github.com/markets/awesome-ruby/stargazers) - Collection of awesome Ruby libraries, tools, frameworks and software.
- 🌎 [Ruby](https://www.ruby-lang.org/en/) - Dynamic programming language, focused on simplicity / productivity. [[GitHub](https://github.com/ruby/ruby) [![GitHub stars](https://img.shields.io/github/stars/ruby/ruby?style=flat)](https://github.com/ruby/ruby/stargazers)]
- Ruby: Framework
    - 🎉 [Ruby on Rails](https://github.com/rails/rails) [![GitHub stars](https://img.shields.io/github/stars/rails/rails?style=flat)](https://github.com/rails/rails/stargazers) - Web app framework. [[Website](https://rubyonrails.org)]
- Ruby: Game Framework
    - 🎉 [Ruby 2D](https://github.com/ruby2d/ruby2d) [![GitHub stars](https://img.shields.io/github/stars/ruby2d/ruby2d?style=flat)](https://github.com/ruby2d/ruby2d/stargazers) - Make cross-platform 2D apps.
- Ruby: Graphics - 3D
    - 🎉 [Mittsu](https://github.com/danini-the-panini/mittsu) [![GitHub stars](https://img.shields.io/github/stars/danini-the-panini/mittsu?style=flat)](https://github.com/danini-the-panini/mittsu/stargazers) - 3D graphics library based heavily on _Three.js_.
- Ruby: Gui
    - 🎉 [Glimmer](https://github.com/andyobtiva/glimmer) [![GitHub stars](https://img.shields.io/github/stars/andyobtiva/glimmer?style=flat)](https://github.com/andyobtiva/glimmer/stargazers) - Gui library and DSL (domain specific language) framework.
    - 🎉 [Shoes](https://github.com/shoes/shoes4) [![GitHub stars](https://img.shields.io/github/stars/shoes/shoes4?style=flat)](https://github.com/shoes/shoes4/stargazers) - Cross-platform gui library. [[Website](http://shoesrb.com/)]

### Rust
- 📚 [Awesome Rust](https://github.com/rust-unofficial/awesome-rust) [![GitHub stars](https://img.shields.io/github/stars/rust-unofficial/awesome-rust?style=flat)](https://github.com/rust-unofficial/awesome-rust/stargazers) - Curated list of Rust code and resources.
- 🌎 [Rust](https://www.rust-lang.org) - Empowering everyone to build quality software. [[Docs](https://www.rust-lang.org/learn) | [GitHub](https://github.com/rust-lang) [![GitHub stars](https://img.shields.io/github/stars/rust-lang?style=flat)](https://github.com/rust-lang/stargazers)]
- Rust: App Framework
    - 🎉 [Makepad](https://github.com/makepad/makepad) [![GitHub stars](https://img.shields.io/github/stars/makepad/makepad?style=flat)](https://github.com/makepad/makepad/stargazers) - Software development platform and native-rendering gui framework. [[Editor](https://makepad.dev/)]
    - 🎉 [Tao](https://github.com/tauri-apps/tao) [![GitHub stars](https://img.shields.io/github/stars/tauri-apps/tao?style=flat)](https://github.com/tauri-apps/tao/stargazers) - Cross-platform windowing. [[Docs](https://docs.rs/tao/latest/tao/)]
- Rust: Audio
    - 🎉 [Kira](https://github.com/tesselode/kira) [![GitHub stars](https://img.shields.io/github/stars/tesselode/kira?style=flat)](https://github.com/tesselode/kira/stargazers) - Create expressive audio for games.
- Rust: Game Engine w/Editor
    - 🎉 [Fyrox](https://github.com/FyroxEngine/Fyrox) [![GitHub stars](https://img.shields.io/github/stars/FyroxEngine/Fyrox?style=flat)](https://github.com/FyroxEngine/Fyrox/stargazers) - 2D/3D game engine with editor. Formerly _Rg3d_. [[Website](https://fyrox.rs/)]
- Rust: Game Framework
    - 🎉 [Ambient](https://github.com/AmbientRun/Ambient) [![GitHub stars](https://img.shields.io/github/stars/AmbientRun/Ambient?style=flat)](https://github.com/AmbientRun/Ambient/stargazers) - Multiplayer game engine.
    - 🎉 [Amethyst](https://github.com/amethyst/amethyst) [![GitHub stars](https://img.shields.io/github/stars/amethyst/amethyst?style=flat)](https://github.com/amethyst/amethyst/stargazers) - Data-driven 2D/3D game engine aiming to be fast and configurable.
    - 🎉 [Bevy](https://github.com/bevyengine/bevy) [![GitHub stars](https://img.shields.io/github/stars/bevyengine/bevy?style=flat)](https://github.com/bevyengine/bevy/stargazers) 🔥 - Refreshingly simple data-driven 2D/3D game engine. [[Website](https://bevyengine.org)]
    - 🎉 [Macroquad](https://github.com/not-fl3/macroquad) [![GitHub stars](https://img.shields.io/github/stars/not-fl3/macroquad?style=flat)](https://github.com/not-fl3/macroquad/stargazers) - Easy to use game library, heavily inspired by _RayLib_.
- Rust: Graphics - 3D
    - 🎉 [Ash](https://github.com/ash-rs/ash) [![GitHub stars](https://img.shields.io/github/stars/ash-rs/ash?style=flat)](https://github.com/ash-rs/ash/stargazers) - Vulkan bindgins for Rust.
    - 🎉 [Glium](https://github.com/glium/glium) [![GitHub stars](https://img.shields.io/github/stars/glium/glium?style=flat)](https://github.com/glium/glium/stargazers) - Safe wrapper arount the OpenGL API.
    - 🎉 [Kiss3D](https://github.com/sebcrozet/kiss3d) [![GitHub stars](https://img.shields.io/github/stars/sebcrozet/kiss3d?style=flat)](https://github.com/sebcrozet/kiss3d/stargazers) - Keep it simple, stupid 3D graphics engine.
    - 🎉 [Miniquad](https://github.com/not-fl3/miniquad) [![GitHub stars](https://img.shields.io/github/stars/not-fl3/miniquad?style=flat)](https://github.com/not-fl3/miniquad/stargazers) - Cross-platform rendering.
    - 🎉 [Vulkano](https://github.com/vulkano-rs/vulkano) [![GitHub stars](https://img.shields.io/github/stars/vulkano-rs/vulkano?style=flat)](https://github.com/vulkano-rs/vulkano/stargazers) - Safe and rich wrapper around the Vulkan API.
    - 🎉 [wgpu](https://github.com/gfx-rs/wgpu) [![GitHub stars](https://img.shields.io/github/stars/gfx-rs/wgpu?style=flat)](https://github.com/gfx-rs/wgpu/stargazers) - Cross-platform graphics API, powers WebGPU in _Firefox_.
- Rust: Gui
    - 🔒 [Azul](https://github.com/fschutt/azul) [![GitHub stars](https://img.shields.io/github/stars/fschutt/azul?style=flat)](https://github.com/fschutt/azul/stargazers) - Desktop gui framework.
    - 🎉 [Dioxus](https://github.com/dioxuslabs/dioxus) [![GitHub stars](https://img.shields.io/github/stars/dioxuslabs/dioxus?style=flat)](https://github.com/dioxuslabs/dioxus/stargazers) - Cross-platform, React-like gui library.
    - 🎉 [Druid](https://github.com/linebender/druid) [![GitHub stars](https://img.shields.io/github/stars/linebender/druid?style=flat)](https://github.com/linebender/druid/stargazers) - Data-first gui design toolkit.
    - 🎉 [egui](https://github.com/emilk/egui) [![GitHub stars](https://img.shields.io/github/stars/emilk/egui?style=flat)](https://github.com/emilk/egui/stargazers) - Easy to use immediate mode gui. Runs on web and native. [[Demo](https://www.egui.rs/)]
    - 🔒 [Slint](https://github.com/slint-ui/slint) [![GitHub stars](https://img.shields.io/github/stars/slint-ui/slint?style=flat)](https://github.com/slint-ui/slint/stargazers) - Gui toolkit for embedded / desktop. Formerly _SixtyFPS_. [[Website](https://slint-ui.com/)]
- Rust: Physics
    - 🎉 [Rapier](https://github.com/dimforge/rapier) [![GitHub stars](https://img.shields.io/github/stars/dimforge/rapier?style=flat)](https://github.com/dimforge/rapier/stargazers) - 2D/3D physics engines focused on performance. [[Docs](https://rapier.rs)]

### Zig
- 📚 [Awesome Zig](https://github.com/nrdmn/awesome-zig) [![GitHub stars](https://img.shields.io/github/stars/nrdmn/awesome-zig?style=flat)](https://github.com/nrdmn/awesome-zig/stargazers) - Curated list of Zig code and resources.
- 🌎 [Zig](https://ziglang.org/) - General-purpose language and toolchain. [[Docs](https://ziglang.org/documentation/master/) | [GitHub](https://github.com/michal-z/zig) [![GitHub stars](https://img.shields.io/github/stars/michal-z/zig?style=flat)](https://github.com/michal-z/zig/stargazers)]
- 📚 [Ziglings](https://github.com/ratfactor/ziglings) [![GitHub stars](https://img.shields.io/github/stars/ratfactor/ziglings?style=flat)](https://github.com/ratfactor/ziglings/stargazers) - Learn the Zig programming language by fixing tiny broken programs.
- Zig: App Framework
    - 🎉 [Upaya](https://github.com/prime31/zig-upaya) [![GitHub stars](https://img.shields.io/github/stars/prime31/zig-upaya?style=flat)](https://github.com/prime31/zig-upaya/stargazers) - Framework for creating game tools and helper apps.
- Zig: File System
    - 🎉 [Known Folders](https://github.com/ziglibs/known-folders) [![GitHub stars](https://img.shields.io/github/stars/ziglibs/known-folders?style=flat)](https://github.com/ziglibs/known-folders/stargazers) - Provides access to well-known folders across several operating systems.
- Zig: Game Engine w/Editor
    - 🎉 [Mach](https://github.com/hexops/mach) [![GitHub stars](https://img.shields.io/github/stars/hexops/mach?style=flat)](https://github.com/hexops/mach/stargazers) - Game engine & graphics toolkit. [[Examples](https://machengine.org/gpu/)]
- Zig: Game Framework
    - 🎉 [Zig-Gamedev Project](https://github.com/michal-z/zig-gamedev) [![GitHub stars](https://img.shields.io/github/stars/michal-z/zig-gamedev?style=flat)](https://github.com/michal-z/zig-gamedev/stargazers) - Sample apps and libraries using DirectX 12.
- Zig: Graphics - 2D
    - 🎉 [Mini Pixel](https://github.com/fabioarnold/MiniPixel) [![GitHub stars](https://img.shields.io/github/stars/fabioarnold/MiniPixel?style=flat)](https://github.com/fabioarnold/MiniPixel/stargazers) - Tiny pixel art editor. [[Download](https://fabioarnold.itch.io/mini-pixel)]
    - 🔒 [Pixi](https://github.com/foxnne/pixi) [![GitHub stars](https://img.shields.io/github/stars/foxnne/pixi?style=flat)](https://github.com/foxnne/pixi/stargazers) - Pixel art editor.
- Zig: Scripting
    - 🎉 [Cyber](https://github.com/fubark/cyber) [![GitHub stars](https://img.shields.io/github/stars/fubark/cyber?style=flat)](https://github.com/fubark/cyber/stargazers) - Fast, efficient, and concurrent scripting language.

<br />
<br />

## Open Source Games
_Successful open source video games to pick apart and gain knowledge._

### Awesome Collections
- 📚 [Open Source Games](https://github.com/michelpereira/awesome-open-source-games) [![GitHub stars](https://img.shields.io/github/stars/michelpereira/awesome-open-source-games?style=flat)](https://github.com/michelpereira/awesome-open-source-games/stargazers) - Collection of games that have the source code available on _GitHub_.
- 📚 [Quake Engines](https://quakeengines.github.io/) - List of repositories of _idTech_ engines, it's derivatives and sourceports.

### C
- 🔒 [Doom](https://github.com/id-Software/DOOM) [![GitHub stars](https://img.shields.io/github/stars/id-Software/DOOM?style=flat)](https://github.com/id-Software/DOOM/stargazers) - The original 1993 3D masterpiece by _id Software_.
- 🔒 [Gish](https://github.com/blinry/gish) [![GitHub stars](https://img.shields.io/github/stars/blinry/gish?style=flat)](https://github.com/blinry/gish/stargazers) - Open Source version of the award-winning physics platformer. [[Steam](https://store.steampowered.com/app/9500/Gish/)]
- 💸 [Handmade Hero](https://handmadehero.org/) - Videos on making a game from start to finish, source code for $15.
- 🔒 [Wolfenstein 3D](https://github.com/id-Software/wolf3d) [![GitHub stars](https://img.shields.io/github/stars/id-Software/wolf3d?style=flat)](https://github.com/id-Software/wolf3d/stargazers) - The original open source release of _Wolfenstein 3D_.

### C++
- 🔒 [Doom 3](https://github.com/id-Software/DOOM-3) [![GitHub stars](https://img.shields.io/github/stars/id-Software/DOOM-3?style=flat)](https://github.com/id-Software/DOOM-3/stargazers) - _Doom 3_ GPL source release.
- 🔒 [Dungeon Crawl: Stone Soup](https://github.com/crawl/crawl) [![GitHub stars](https://img.shields.io/github/stars/crawl/crawl?style=flat)](https://github.com/crawl/crawl/stargazers) - Classic roguelike adventure. [[Play](https://crawl.develz.org/)]
- 🎉 [Etheral Legends](https://github.com/Soverance/EtherealLegends) [![GitHub stars](https://img.shields.io/github/stars/Soverance/EtherealLegends?style=flat)](https://github.com/Soverance/EtherealLegends/stargazers) - Indie Action RPG built with _Unreal Engine 4_. [[Steam](https://store.steampowered.com/app/428980/Ethereal_Legends/)]
- 🔒 [GemRB](https://github.com/gemrb/gemrb) [![GitHub stars](https://img.shields.io/github/stars/gemrb/gemrb?style=flat)](https://github.com/gemrb/gemrb/stargazers) - Open source implementation of _Bioware_'s Infinity Engine.
- 🔒 [NetHack](https://github.com/NetHack/NetHack) [![GitHub stars](https://img.shields.io/github/stars/NetHack/NetHack?style=flat)](https://github.com/NetHack/NetHack/stargazers) - Official _NetHack_ git repository.
- 🎉 [OpenLara](https://github.com/XProger/OpenLara) [![GitHub stars](https://img.shields.io/github/stars/XProger/OpenLara?style=flat)](https://github.com/XProger/OpenLara/stargazers) - Classic _Tomb Raider_ open source engine. [[Play](http://xproger.info/projects/OpenLara/)]
- 🎉 [TeeWorlds](https://github.com/teeworlds/teeworlds) [![GitHub stars](https://img.shields.io/github/stars/teeworlds/teeworlds?style=flat)](https://github.com/teeworlds/teeworlds/stargazers) - Retro multiplayer shooter. [[Website](https://teeworlds.com/)]
- 🔒 [zDoom](https://github.com/ZDoom/gzdoom) [![GitHub stars](https://img.shields.io/github/stars/ZDoom/gzdoom?style=flat)](https://github.com/ZDoom/gzdoom/stargazers) - Modern, feature centric port for all Doom engine games.

### Java
- 🔒 [Pixel Dungeon](https://github.com/watabou/pixel-dungeon) [![GitHub stars](https://img.shields.io/github/stars/watabou/pixel-dungeon?style=flat)](https://github.com/watabou/pixel-dungeon/stargazers) - Traditional roguelike game with pixel-art graphics and simple interface.

<br />
<br />

## Specialty Topics
_Exploring specialty game engine / game development topics and features._

### Asset Pipeline / Formats
- 📚 [glTF](https://www.khronos.org/gltf/) - Runtime 3D asset delivery format for scenes, meshes, materials, animations, data.
- 🎉 [KTX-Software](https://github.com/KhronosGroup/KTX-Software) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/KTX-Software?style=flat)](https://github.com/KhronosGroup/KTX-Software/stargazers) - _Khronos_ texture container tools and library for KTX/KTX2 workflow.
- 🎉 [MikkTSpace](https://github.com/mmikk/MikkTSpace) [![GitHub stars](https://img.shields.io/github/stars/mmikk/MikkTSpace?style=flat)](https://github.com/mmikk/MikkTSpace/stargazers) - Standard for tangent space used in baking tools to produce normal maps.

### Color Manipulation
- 📚 [How to Choose Colors Procedurally](http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/) - Procedural palettes and how to generate them.
- 📚 [Red, Yellow, and Blue](https://daveeddy.com/2014/07/01/red-yellow-and-blue/) - Convert colors from the paint color wheel to RGB space. [[Source](https://github.com/bahamas10/ryb) [![GitHub stars](https://img.shields.io/github/stars/bahamas10/ryb?style=flat)](https://github.com/bahamas10/ryb/stargazers)]

### Enemies / Pathfinding
- 📚 [Intro to AI](https://www.raywenderlich.com/2808-introduction-to-ai-programming-for-games) - Intro to Enemy AI Programming for Games at RayWenderlich.com.
- 📚 [Beginner's Guide to Game AI](https://www.gamedev.net/tutorials/programming/artificial-intelligence/the-total-beginners-guide-to-game-ai-r4942/) - Intro to concepts used in Enemy AI for games.

### Entity Component Systems
- 📚 [A Simple Entity Component System](https://austinmorlan.com/posts/entity_component_system/) - Basis for an ECS in C++.
- 📚 [Evolve Your Hierarchy](https://cowboyprogramming.com/2007/01/05/evolve-your-heirachy/) - Overview of ECSs and why to use them, at [Cowboy Programming](https://cowboyprogramming.com).
- 📚 [Intro to Component-Based Architecture in Games](https://www.raywenderlich.com/2806-introduction-to-component-based-architecture-in-games) - Component-based architecture.
- 📚 [Nomad Game Engine](https://savas.ca/nomad) - Articles building an ECS from the ground up in C++. [[Source](https://github.com/taurheim/NomadECS) [![GitHub stars](https://img.shields.io/github/stars/taurheim/NomadECS?style=flat)](https://github.com/taurheim/NomadECS/stargazers)]
- 📚 [What's an Entity System](http://entity-systems.wikidot.com) - Overview of ECSs, how they are used in game development.

### Fluid / Smoke
- 📚 [Fluid Simulation on the GPU](https://developer.nvidia.com/gpugems/gpugems/part-vi-beyond-triangles/chapter-38-fast-fluid-dynamics-simulation-gpu) - GPU Gems Chapter 38 - Fast, stable fluid simulation on the GPU.
- 🔒 [Fluids-2D](https://github.com/mharrys/fluids-2d) [![GitHub stars](https://img.shields.io/github/stars/mharrys/fluids-2d?style=flat)](https://github.com/mharrys/fluids-2d/stargazers) - Real-time fluid dynamics on the GPU with the help of WebGL and Three.js.
- 🔒 [GPU Fluid Experiments](http://haxiomic.github.io/GPU-Fluid-Experiments/html5/) - Cross-platform GPU fluid simulation. [[Source](https://github.com/haxiomic/GPU-Fluid-Experiments) [![GitHub stars](https://img.shields.io/github/stars/haxiomic/GPU-Fluid-Experiments?style=flat)](https://github.com/haxiomic/GPU-Fluid-Experiments/stargazers)]
- 🎉 [WebGL Fluid Simulation](https://paveldogreat.github.io/WebGL-Fluid-Simulation/) - Play with fluids in your browser (even on mobile). [[Source](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) [![GitHub stars](https://img.shields.io/github/stars/PavelDoGreat/WebGL-Fluid-Simulation?style=flat)](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation/stargazers)]

### Geometry
- CSG (Constructive Solid Geometry)
    - 📚 [Constructive Solid Geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry) - Technique using boolean operations to combine primitive objects.
    - 🎉 [csg.js](https://github.com/evanw/csg.js/) [![GitHub stars](https://img.shields.io/github/stars/evanw/csg.js/?style=flat)](https://github.com/evanw/csg.js//stargazers) - JavaScript library implementing CSG. [[Examples](https://evanw.github.io/csg.js/)]
    - 🎉 [three-bvh-csg](https://github.com/gkjohnson/three-bvh-csg) [![GitHub stars](https://img.shields.io/github/stars/gkjohnson/three-bvh-csg?style=flat)](https://github.com/gkjohnson/three-bvh-csg/stargazers) - Fast and dynamic CSG on top of three-mesh-bvh.
    - 🎉 [three-csgmesh](https://github.com/manthrax/THREE-CSGMesh) [![GitHub stars](https://img.shields.io/github/stars/manthrax/THREE-CSGMesh?style=flat)](https://github.com/manthrax/THREE-CSGMesh/stargazers) - Conversion of the csg.js library for use with Three.js.
- Meshes
    - 📚 [Geometry, Surfaces, Curves, Polyhedra](https://paulbourke.net/geometry/) - Geometry topics including meshes, shapes, textures.
    - 📚 [Mesh Transforms](https://ciechanow.ski/mesh-transforms/) - _Apple_'s private API for manipulation of UIView meshes. [[Source](https://github.com/olegtyshcneko/CAMeshTransform) [![GitHub stars](https://img.shields.io/github/stars/olegtyshcneko/CAMeshTransform?style=flat)](https://github.com/olegtyshcneko/CAMeshTransform/stargazers)]
- Smoothing
    - 📚 [Laplacian Smoothing](http://rodolphe-vaillant.fr/entry/70/laplacian-smoothing-c-code-to-smooth-a-mesh) - Draft notes with C++ code for laplacian smoothing of meshes.
    - 📚 [Subdivision at Matt's Webcorner](http://graphics.stanford.edu/~mdfisher/subdivision.html) - Smoothing with subdivision surfaces.
    - 📚 [Subdivision Surfaces](http://www.holmes3d.net/graphics/subdivision/) - Explanations of different schemes used in subdivision surfaces.

### Hair
- 📚 [Fuzzy Meshes](https://medium.com/@Zadvorsky/fuzzy-meshes-4c7fd3910d6f) - Simulating fur with cones and gravity. [[Source](https://github.com/zadvorsky/three-fuzzy-mesh) [![GitHub stars](https://img.shields.io/github/stars/zadvorsky/three-fuzzy-mesh?style=flat)](https://github.com/zadvorsky/three-fuzzy-mesh/stargazers)]

### Lighting / Shadows
- Gamma
    - 📚 [What Every Coder Should Know About Gamma](https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/) - Light emission vs perceptual brightness.
- Lighting 2D
    - 📚 [Gleaner Heights: 2D Lighting](http://gleanerheights.blogspot.com/2017/05/lighting-in-2d-games-shader-glsl.html?m=1) - Simple intro to 2D lighting in a game with GLSL.
- Lighting 3D
    - 📚 [Basic Lighting](https://learnopengl.com/Lighting/Basic-Lighting) - 3D lighting article by _LearnOpenGL_.
    - 📚 [Forward Rendering vs. Deferred Rendering](https://gamedevelopment.tutsplus.com/articles/forward-rendering-vs-deferred-rendering--gamedev-12342) - Techniques for handling many lights.
    - 📚 [Forward+ Rendering / Tiled Forward Shading](https://www.3dgep.com/forward-plus/) - Forward rendering with tiled light culling.
- Shadows 2D
    - 📚 [2D Pixel Perfect Shadows](https://github.com/mattdesl/lwjgl-basics/wiki/2D-Pixel-Perfect-Shadows) [![GitHub stars](https://img.shields.io/github/stars/mattdesl/lwjgl-basics/wiki/2D-Pixel-Perfect-Shadows?style=flat)](https://github.com/mattdesl/lwjgl-basics/wiki/2D-Pixel-Perfect-Shadows/stargazers) - An approach to 2D pixel-perfect lights / shadows using shaders.
    - 📚 [2D Visibility](https://www.redblobgames.com/articles/visibility/) - Excellent interactive tutorial on 2D visibility.
    - 📚 [Fast 2D shadows in Unity](https://www.gamedeveloper.com/programming/fast-2d-shadows-in-unity-using-1d-shadow-mapping) - Adapting 3D rendering techniques to achieve fast 2D shadows.
    - 📚 [Sight & Light](https://ncase.me/sight-and-light/) - How to create 2D visibility / shadow effects for your game. [[Source](https://github.com/ncase/sight-and-light) [![GitHub stars](https://img.shields.io/github/stars/ncase/sight-and-light?style=flat)](https://github.com/ncase/sight-and-light/stargazers)]
    - 📚 [Symmetric Shadowcasting](https://www.albertford.com/shadowcasting/) - Common technique for calculating field of view.
- Shadows 3D
    - 📚 [Efficient Soft-Edged Shadows](https://developer.nvidia.com/gpugems/gpugems2/part-ii-shading-lighting-and-shadows/chapter-17-efficient-soft-edged-shadows-using) - GPU Gems 2 Chapter 17.
    - 📚 [Screen Space Shadows](https://panoskarabelas.com/posts/screen_space_shadows/) - Great exploration of screen space shadows.
    - 📚 [Shadow Mapping](https://en.m.wikipedia.org/wiki/Shadow_mapping) - Shadow mapping and the techniques used to acheive it.
- Volumetric
    - 🌎 [Threex Volumetric Spotlight](http://jeromeetienne.github.io/threex.volumetricspotlight/examples/basic.html) - Great example of volumetric lighting with Three.js. [[Source](https://github.com/jeromeetienne/threex.volumetricspotlight) [![GitHub stars](https://img.shields.io/github/stars/jeromeetienne/threex.volumetricspotlight?style=flat)](https://github.com/jeromeetienne/threex.volumetricspotlight/stargazers)]

### Network
- 📚 [Source Multiplayer Networking](https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking) - _Valve_'s Source Engine multiplayer system.

### Particles
- 📚 [Particles](https://learnopengl.com/In-Practice/2D-Game/Particles) - Article by _LearnOpenGL_.
- 📚 [Soft Particles](https://keaukraine.medium.com/implementing-soft-particles-in-webgl-and-opengl-es-b968d61133b0) - Implementing soft particles in WebGL.

### Physics
- 📚 [Fix Your Timestep!](https://gafferongames.com/post/fix_your_timestep/) 🔥 - How to keep physics stable with variable fps.
- 📚 [Game Physics from Scratch](https://brm.io/game-physics-for-beginners/) - Starting resource for game physics.
- 📚 [Intro to Physics](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics) - Part I: Intro to Rigid Body Dynamics.
- 📚 [Open Source Physics Engines](https://www.tapirgames.com/blog/open-source-physics-engines) - List of open source physics engines.
- Platformer
    - 📚 [2D Physics Games](https://www.gamedeveloper.com/design/how-to-create-2d-physics-games-with-box2d-library) - Using Box2D for water, ropes, gravity, lines, vehicles, etc.
    - 📚 [Basic 2D Platformer Physics](https://gamedevelopment.tutsplus.com/series/basic-2d-platformer-physics--cms-998) - How to create a physics system for a platformer.
- Ropes / Chains
    - 📚 [Draw SVG rope using JavaScript](https://muffinman.io/blog/draw-svg-rope-using-javascript/) - SVG path vector rope drawing.
    - 📚 [Ropes in Contraption Maker](https://www.gamedeveloper.com/design/ropes-in-contraption-maker) - Implementing the physics of ropes in _Contraption Maker_.
    - 🌎 [Matter.js: Chains](https://brm.io/matter-js/demo/#chains) - Chains demo using _Matter.js_. [[Source](https://github.com/liabru/matter-js/blob/master/examples/chains.js) [![GitHub stars](https://img.shields.io/github/stars/liabru/matter-js/blob/master/examples/chains.js?style=flat)](https://github.com/liabru/matter-js/blob/master/examples/chains.js/stargazers)]
- Soft Body
    - 📚 [Blob Physics](https://cowboyprogramming.com/2007/01/05/blob-physics/) - Using verlet physics to simulate 2D blobs.
    - 🌎 [Oryol: Bullet Cloth](https://floooh.github.io/oryol-samples/wasm/BulletPhysicsCloth.html) - _Bullet 3D_ physics cloth using the _Oryol_ game framework. [[Source](https://github.com/floooh/oryol-samples/blob/master/src/BulletPhysicsCloth/BulletPhysicsCloth.cc) [![GitHub stars](https://img.shields.io/github/stars/floooh/oryol-samples/blob/master/src/BulletPhysicsCloth/BulletPhysicsCloth.cc?style=flat)](https://github.com/floooh/oryol-samples/blob/master/src/BulletPhysicsCloth/BulletPhysicsCloth.cc/stargazers)]
    - 🌎 [Three.js: Ammo Volume](https://threejs.org/examples/?q=physics#physics_ammo_volume) - 3D soft body volumes using _Ammo.js_ and _Three.js_. [[Source](https://github.com/mrdoob/three.js/blob/master/examples/physics_ammo_volume.html) [![GitHub stars](https://img.shields.io/github/stars/mrdoob/three.js/blob/master/examples/physics_ammo_volume.html?style=flat)](https://github.com/mrdoob/three.js/blob/master/examples/physics_ammo_volume.html/stargazers)]
- Verlet Physics
    - 📚 [Making a Verlet Physics Engine](https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Fbetterprogramming.pub%2Fmaking-a-verlet-physics-engine-in-javascript-1dff066d7bc5) - Under the hood of a 2D physics engine in JavaScript.
- Water / Buoyancy
    - 📚 [2D Water](https://prime31.github.io/water2d-part1/) - Modeling 2D water with springs.

### Rendering
- 📚 [GPU Driven Rendering](https://vkguide.dev/docs/gpudriven/gpu_driven_engines/) - Calculating rendering on the GPU in compute shaders.
- 📚 [Model Batching](https://webglfundamentals.org/webgl/lessons/webgl-qna-drawing-many-different-models-in-a-single-draw-call.html) - Drawing many different models in a single draw call.

### Scripting
- 📚 [Adding Languages to Game Engines](https://www.gamedeveloper.com/programming/adding-languages-to-game-engines) - Story of adding scripting to a game.
- 📚 [Implementing a Scripting Engine](https://www.flipcode.com/archives/Implementing_A_Scripting_Engine-Part_1_Overview.shtml) - Writting a scripting engine from scratch.
- 📚 [Embedded Scripting Languages](https://caiorss.github.io/C-Cpp-Notes/embedded_scripting_languages.html) - Scripting languages and engines available as libraries.
- 📚 [List of Embedded Scripting Languages](https://github.com/dbohdan/embedded-scripting-languages) [![GitHub stars](https://img.shields.io/github/stars/dbohdan/embedded-scripting-languages?style=flat)](https://github.com/dbohdan/embedded-scripting-languages/stargazers) - Scripting languages to use in your app / game.
- 📚 [Scriptorium](https://github.com/r-lyeh-archived/scriptorium) [![GitHub stars](https://img.shields.io/github/stars/r-lyeh-archived/scriptorium?style=flat)](https://github.com/r-lyeh-archived/scriptorium/stargazers) - Game scripting languages benchmarked.

### Shaders
- 📚 [3D Game Shaders For Beginners](https://lettier.github.io/3d-game-shaders-for-beginners/index.html) 🔥 - Shaders to improve your games. [[Source](https://github.com/lettier/3d-game-shaders-for-beginners) [![GitHub stars](https://img.shields.io/github/stars/lettier/3d-game-shaders-for-beginners?style=flat)](https://github.com/lettier/3d-game-shaders-for-beginners/stargazers)]
- 📚 [Book of Shaders](https://thebookofshaders.com) 🔥 - Step-by-step guide through [Fragment Shaders](https://www.khronos.org/opengl/wiki/Fragment_Shader). [[Source](https://github.com/patriciogonzalezvivo/thebookofshaders) [![GitHub stars](https://img.shields.io/github/stars/patriciogonzalezvivo/thebookofshaders?style=flat)](https://github.com/patriciogonzalezvivo/thebookofshaders/stargazers)]
- 🎉 [CrossShader](https://github.com/alaingalvan/CrossShader) [![GitHub stars](https://img.shields.io/github/stars/alaingalvan/CrossShader?style=flat)](https://github.com/alaingalvan/CrossShader/stargazers) - Cross-compiling shaders between GLSL, HLSL, Metal, and more.
- 🌎 [Geeks3D Shader Library](https://www.geeks3d.com/shader-library/) - Postprocessing, lighting, utlities and many more.
- 📚 [Review of Shader Languages](https://web.archive.org/web/20260201143258/https://alain.xyz/blog/a-review-of-shader-languages) - Differences between HLSL, GLSL, MSL, and WGSL.
- 📚 [Ronja Tutorials](https://www.ronja-tutorials.com/) - Tutorials covering many shader techniques.
- 🌎 [Shader Park](https://github.com/shader-park/shader-park-core) [![GitHub stars](https://img.shields.io/github/stars/shader-park/shader-park-core?style=flat)](https://github.com/shader-park/shader-park-core/stargazers) - Shader programming in JavaScript.
- 🌎 [SHADERed](https://github.com/dfranx/SHADERed) [![GitHub stars](https://img.shields.io/github/stars/dfranx/SHADERed?style=flat)](https://github.com/dfranx/SHADERed/stargazers) - Shader IDE, written in C++.
- 🌎 [Shadertoy](https://www.shadertoy.com) - Build and share shaders online.
- Bloom
    - 📚 [LearnOpenGL Tutorial](https://learnopengl.com/Advanced-Lighting/Bloom) - Techniques used for bloom lighting, presented in OpenGL.
    - 🌎 [Three.js: Bloom Example](https://threejs.org/examples/?q=bloom#webgl_postprocessing_unreal_bloom) - WebGL bloom postprocessing using _Three.js_. [[Source](https://github.com/mrdoob/three.js/blob/master/examples/webgl_postprocessing_unreal_bloom.html) [![GitHub stars](https://img.shields.io/github/stars/mrdoob/three.js/blob/master/examples/webgl_postprocessing_unreal_bloom.html?style=flat)](https://github.com/mrdoob/three.js/blob/master/examples/webgl_postprocessing_unreal_bloom.html/stargazers)]
    - 📚 [Unity Tutorial](https://catlikecoding.com/unity/tutorials/advanced-rendering/bloom/) - How to add support for a bloom effect.
- Dithering
    - 📚 [Dithering on the GPU](http://alex-charlton.com/posts/Dithering_on_the_GPU/) - Ordered dithering in glsl using 8x8 Bayer Dithering.
- Fire
    - 📚 [Fire Shader in GLSL](https://clockworkchilli.com/blog/8_a_fire_shader_in_glsl_for_your_webgl_games) - Fire intro shader using noise textures and masking.
    - 🌎 [Simplex 3D Noise](https://www.shadertoy.com/view/MllfDn) - Simplex noise fire simulation shader at ShaderToy.
- Lines
    - 📚 [Drawing Lines](https://mattdesl.svbtle.com/drawing-lines-is-hard) - Techniques for 2D/3D line rendering.
- Noise
    - 📚 [Book of Shaders: Noise](https://thebookofshaders.com/11/) - Excellent GLSL noise article by Book of Shaders.
    - 📚 [Color Banding](https://shader-tutorial.dev/advanced/color-banding-dithering/) - Using noise / dithering to improve drawing gradients.
    - 🎉 [Psrdnoise](https://github.com/stegu/psrdnoise/) [![GitHub stars](https://img.shields.io/github/stars/stegu/psrdnoise/?style=flat)](https://github.com/stegu/psrdnoise//stargazers) - Tiling simplex flow noise in 2D/3D.
    - 📚 [Understanding Perlin Noise](http://adrianb.io/2014/08/09/perlinnoise.html) - Analysis of Perlin Noise, written in C#. [[Source](https://gist.github.com/Flafla2/f0260a861be0ebdeef76)]
    - 🎉 [WebGL Noise](https://github.com/stegu/webgl-noise/) [![GitHub stars](https://img.shields.io/github/stars/stegu/webgl-noise/?style=flat)](https://github.com/stegu/webgl-noise//stargazers) - Maintained branch of the original _Ashima Arts_ 2D, 3D and 4D noise functions.
- Outlines
    - 🌎 [Fast Solid 2D Outline](https://www.shadertoy.com/view/XdV3Dc) - Drawing an outline on the alpha channel of a 2D image.
    - 📚 [Let it glow!](http://blogs.love2d.org/content/let-it-glow-dynamically-adding-outlines-characters) - Article with shader code on dynamically adding outlines to characters.
    - 🎉 [Outline Shader](https://www.reddit.com/r/godot/comments/8g067a/the_perfect_outline_shader_atleast_close/) - Nice outline shader. [[Source](https://github.com/steincodes/godot-shader-tutorials) [![GitHub stars](https://img.shields.io/github/stars/steincodes/godot-shader-tutorials?style=flat)](https://github.com/steincodes/godot-shader-tutorials/stargazers)]
    - 📚 [Outlines w/Surface IDs](https://omar-shehata.medium.com/better-outline-rendering-using-surface-ids-with-webgl-e13cdab1fd94) - Technique combining depth, normals and surface IDs. [[Source](https://github.com/OmarShehata/webgl-outlines) [![GitHub stars](https://img.shields.io/github/stars/OmarShehata/webgl-outlines?style=flat)](https://github.com/OmarShehata/webgl-outlines/stargazers)]
    - 📚 [Sketchy Outling](https://lettier.github.io/3d-game-shaders-for-beginners/outlining.html) - Article on producing a sketchy outline look.
- Pixelation
    - 📚 [Pixel Art Shaders](https://alaingalvan.tumblr.com/post/79829067408/glsl-pixel-art-shaders) - Useful GLSL postprocessing shaders for pixel art games.
    - 🌎 [Three.js: Pixelation Example](https://threejs.org/examples/?q=pixel#webgl_postprocessing_pixel) - WebGL pixelation postprocessing using _Three.js_. [[Source](https://github.com/mrdoob/three.js/blob/master/examples/webgl_postprocessing_pixel.html) [![GitHub stars](https://img.shields.io/github/stars/mrdoob/three.js/blob/master/examples/webgl_postprocessing_pixel.html?style=flat)](https://github.com/mrdoob/three.js/blob/master/examples/webgl_postprocessing_pixel.html/stargazers)]
- Postprocessing
    - 📚 [Image Editor Effects](https://github.com/alaingalvan/image-editor-effects) [![GitHub stars](https://img.shields.io/github/stars/alaingalvan/image-editor-effects?style=flat)](https://github.com/alaingalvan/image-editor-effects/stargazers) - WebGL image filters / effects shaders.
- Upscaling
    - 📚 [How do I perform an xBR or hqx filter in XNA?](https://gamedev.stackexchange.com/questions/87275/how-do-i-perform-an-xbr-or-hqx-filter-in-xna/87821#87821) - Upscaling shader code.
    - 📚 [hqx](https://en.wikipedia.org/wiki/Hqx) - Wikipedia article about the hqx pixel art upscaling algorithm developed by Maxim Stepin.
- Water / Refraction
    - 📚 [2D Water Shader](https://rotatingcanvas.com/fragment-shader-to-simulate-water-surface-in-libgdx/) - GLSL fragment shader to simulate 2D water surface in _libGDX_.
- Wireframe
    - 📚 [Flat and Wireframe Shading](https://catlikecoding.com/unity/tutorials/advanced-rendering/flat-and-wireframe-shading/) - Flat shading / wireframes using Barycentric Coordinates.

### Signed Distance Fields
- 📚 [2D SDFs](https://iquilezles.org/articles/distfunctions2d/) - Signed distance functions for basic 2D primitives.
- 📚 [3D SDFs](https://iquilezles.org/articles/distfunctions/) - Signed distance functions for basic 3D primitives.
- 📚 [CSG w/SDFs](https://jasmcole.com/2019/10/03/signed-distance-fields/) - Using circular SDFs to build 3D objects with CSG. [[Source](https://github.com/jasmcole/Blog/tree/master/CSG) [![GitHub stars](https://img.shields.io/github/stars/jasmcole/Blog/tree/master/CSG?style=flat)](https://github.com/jasmcole/Blog/tree/master/CSG/stargazers)]
- 📚 [Basic 2D SDFs](https://www.ronja-tutorials.com/post/034-2d-sdf-basics/) - Basics of rendering 2D shapes with SDFs in shaders.
- 📚 [Bezier Strokes](https://vladjuckov.github.io/beziers-sdf/) - Blog post on rendering bezier strokes with SDFs.
- 📚 [Signed Distance Field Resources](https://github.com/CedricGuillemet/SDF) [![GitHub stars](https://img.shields.io/github/stars/CedricGuillemet/SDF?style=flat)](https://github.com/CedricGuillemet/SDF/stargazers) - Tutorials, papers, software, demos, discussions, etc.
- 🎉 [SDF Mesh Generation](https://github.com/fogleman/sdf) [![GitHub stars](https://img.shields.io/github/stars/fogleman/sdf?style=flat)](https://github.com/fogleman/sdf/stargazers) - Python API to generate 3D meshes with SDFs.

### Tiling
- 📚 [Auto-Tile](https://gamedevelopment.tutsplus.com/tutorials/how-to-use-tile-bitmasking-to-auto-tile-your-level-layouts--cms-25673) - How to use tile bitmasking to auto-tile your level layouts.
- 📚 [List of Eucliden Uniform Tilings](https://en.wikipedia.org/wiki/List_of_Euclidean_uniform_tilings) - Wikipedia article on uniform tiling, space-filling polygons.
- 📚 [Space-Filling Polyhedron](https://mathworld.wolfram.com/Space-FillingPolyhedron.html) - [Polyhedra](https://en.wikipedia.org/wiki/Category:Space-filling_polyhedra), 3D polygons that fill space. [[5 Space-Filling Polyhedra](https://www.steelpillow.com/polyhedra/five_sf/five.html)]

### Transparency
- 📚 [Depth Peeling](https://developer.download.nvidia.com/assets/gamedev/docs/OrderIndependentTransparency.pdf) - Method for order-independent transparency.
- 📚 [Intro to Order-Independent Transparency](https://learnopengl.com/Guest-Articles/2020/OIT/Introduction) - Article by _LearnOpenGL_.
- 📚 [Weighted, Blended](http://casual-effects.blogspot.com/2015/03/implemented-weighted-blended-order.html) - Method for order-independent transparency.

<br />
<br />

## Tools / Software
_Software to help with game engine / video game development._

### Awesome Collections
- 🌎 [Itch.io Tools](https://itch.io/tools) - Huge collection of game dev tools on _Itch.io_.
- 📚 [Tiny Tools](https://tinytools.directory/) - Tools that might be useful in building your game.

### Animation Software
- 💸 [Cascadeur](https://cascadeur.com) - 3D animation software for physics-based character animation.
- 🆓 [DragonBones](https://dragonbones.github.io/en/index.html) - Open source 2D game skeletal animation solution. [[Source](https://github.com/DragonBones/) [![GitHub stars](https://img.shields.io/github/stars/DragonBones/?style=flat)](https://github.com/DragonBones//stargazers)]
- 💸 [Mixamo](https://www.mixamo.com/#/) - Animate 3D characters for games, films and more. By _Adobe_.
- 💸 [Spine](http://esotericsoftware.com/) - 2D animation for games.

### Audio Tools
- Music
    - 🆓 [Ardour](https://ardour.org) - Record, edit, and mix. [[Source](https://github.com/Ardour/ardour) [![GitHub stars](https://img.shields.io/github/stars/Ardour/ardour?style=flat)](https://github.com/Ardour/ardour/stargazers)]
    - 🆓 [Audacity](https://www.audacityteam.org) - Multi-track audio editor and recorder. [[Source](https://github.com/audacity/audacity) [![GitHub stars](https://img.shields.io/github/stars/audacity/audacity?style=flat)](https://github.com/audacity/audacity/stargazers)]
    - 🆓 [Bosca Ceoil](https://boscaceoil.net) - Easy to use tool for creating music.
    - 🆓 [Cakewalk](https://www.bandlab.com/products/cakewalk) - Complete music production package.
    - 🆓 [FamiStudio](https://famistudio.org) - Music editor targeted at chiptune artists and NES homebrewers. [[Source](https://github.com/BleuBleu/FamiStudio) [![GitHub stars](https://img.shields.io/github/stars/BleuBleu/FamiStudio?style=flat)](https://github.com/BleuBleu/FamiStudio/stargazers)]
    - 💸 [fmod](https://www.fmod.com) - Popular (_Hades_, _Celeste_, _Untitled Goose Game_) audio software for games.
    - 💸 [KiraStudio](https://kirastudio.org/) - Lightweight music studio built for clarity, automation, and sound creation.
    - 🆓 [LMMS](https://lmms.io) 🔥 - Cross-platform music production software. [[Source](https://github.com/lmms/lmms) [![GitHub stars](https://img.shields.io/github/stars/lmms/lmms?style=flat)](https://github.com/lmms/lmms/stargazers)]
    - 🆓 [Sound Box](https://gitlab.com/mbitsnbites/soundbox) - Compose synthetic music in your browser, good for small demos.
    - 🆓 [ZzFXM](https://keithclark.github.io/ZzFXM/tracker/) - Music generator for use in tiny JavaScript apps. [[Source](https://github.com/keithclark/ZzFXM) [![GitHub stars](https://img.shields.io/github/stars/keithclark/ZzFXM?style=flat)](https://github.com/keithclark/ZzFXM/stargazers)]
- Sound Effects
    - 🆓 [Bfxr](https://www.bfxr.net) - Classic. For making simple sound effects for games. [[Source](https://github.com/increpare/bfxr) [![GitHub stars](https://img.shields.io/github/stars/increpare/bfxr?style=flat)](https://github.com/increpare/bfxr/stargazers)]
    - 🆓 [ChipTone](https://sfbgames.itch.io/chiptone) - Tool for generating sound effects.
    - 💸 [sfxia](https://rxi.itch.io/sfxia) - Tiny sound generator.
    - 🆓 [ZzFX](https://killedbyapixel.github.io/ZzFX/) - Tiny JavaScript sound FX system / Zuper Zmall Zound Zynth. [[Source](https://github.com/KilledByAPixel/ZzFX) [![GitHub stars](https://img.shields.io/github/stars/KilledByAPixel/ZzFX?style=flat)](https://github.com/KilledByAPixel/ZzFX/stargazers)]

### Color / Palettes
- 🌎 [Colormind](http://colormind.io) - Color scheme generator, can learn color styles from photographs, art, etc.
- 🌎 [COLOURlovers](https://www.colourlovers.com) - Share colors, palettes and patterns.
- 🌎 [Coolors](https://coolors.co) - Fast color palette generator.
- 🌎 [Huemint](https://huemint.com) - Uses machine learning to generate colors for graphic design.
- 🌎 [Lospec](https://lospec.com/palette-list) - Database of palettes for pixel art.
- 🌎 [Paletton](https://paletton.com) - Explore complementary colors on the color wheel.

### Debugging / Profiling
- 🆓 [Nsight](https://developer.nvidia.com/nsight-graphics) - Debug, profile, and export frames built with Direct3D, Vulkan, OpenGL, OpenXR.
- 🆓 [PIX](https://learn.microsoft.com/en-us/windows/win32/direct3dtools/pix/articles/general/pix-overview) - Debugging and profiling for game developers using Direct3D 12.
- 🎉 [RenderDoc](https://github.com/baldurk/renderdoc) [![GitHub stars](https://img.shields.io/github/stars/baldurk/renderdoc?style=flat)](https://github.com/baldurk/renderdoc/stargazers) - Stand-alone graphics debugging tool.
- 🎉 [Tracy Profiler](https://github.com/wolfpld/tracy) [![GitHub stars](https://img.shields.io/github/stars/wolfpld/tracy?style=flat)](https://github.com/wolfpld/tracy/stargazers) - Frame profiler.

### Image Editors
- 🆓 [GIMP](https://www.gimp.org) - GNU Image Manipulation Program, open source image editor. [[Source](https://github.com/GNOME/gimp) [![GitHub stars](https://img.shields.io/github/stars/GNOME/gimp?style=flat)](https://github.com/GNOME/gimp/stargazers)]
- 🆓 [Photopea](https://www.photopea.com) - Capable online photo editor.

### Level Editors
- 💰 [Crocotile 3D](https://prominent.itch.io/crocotile3d) - Tool for creating 3D scenes with 2D tiles.
- 🆓 [Radiant](https://icculus.org/gtkradiant/) - Cross-platform level editor for [idTech](https://en.wikipedia.org/wiki/Id_Tech) games. [[Source](https://github.com/TTimo/GtkRadiant) [![GitHub stars](https://img.shields.io/github/stars/TTimo/GtkRadiant?style=flat)](https://github.com/TTimo/GtkRadiant/stargazers)]
- 🆓 [TrenchBroom](https://trenchbroom.github.io) - Level editor for _Quake-Engine_ games. [[Source](https://github.com/TrenchBroom/TrenchBroom) [![GitHub stars](https://img.shields.io/github/stars/TrenchBroom/TrenchBroom?style=flat)](https://github.com/TrenchBroom/TrenchBroom/stargazers)]

### Materials / Textures
- 💰 [Filter Forge](https://www.filterforge.com) - Photo effects, realistic textures, and visual editor.
- 🆓 [JSplacement](https://windmillart.net/?p=jsplacement) - Cross-platform pseudo-random displacement map generator.
- 🆓 [Material Maker](https://www.materialmaker.org) - Procedural [physically-based rendering](https://en.wikipedia.org/wiki/Physically_based_rendering) material maker. [[Source](https://github.com/RodZill4/material-maker) [![GitHub stars](https://img.shields.io/github/stars/RodZill4/material-maker?style=flat)](https://github.com/RodZill4/material-maker/stargazers)]
- 🆓 [Materialize](http://boundingboxsoftware.com/materialize/) - Tool for creating materials from images to be used in games. [[Source](https://github.com/BoundingBoxSoftware/Materialize) [![GitHub stars](https://img.shields.io/github/stars/BoundingBoxSoftware/Materialize?style=flat)](https://github.com/BoundingBoxSoftware/Materialize/stargazers)]
- 💸 [PixPlant](https://www.pixplant.com/index.php) - Tool to allow simple creation of tiling 3D materials.
- 🆓 [SPARTAN](https://pnjeffries.itch.io/spartan-procjam-edition) - Generate a wide variety of different background types that are tileable.
- 🆓 [TexaTool](https://kronbits.itch.io/texatool) - Online tool to generate tileable textures by moving sliders.
- 🆓 [Texgen.js](https://texgenjs.org) - JavaScript texture generator tool. [[Source](https://github.com/mrdoob/texgen.js) [![GitHub stars](https://img.shields.io/github/stars/mrdoob/texgen.js?style=flat)](https://github.com/mrdoob/texgen.js/stargazers)]

### Modeling Tools
- 💰 [3DS Max](https://www.autodesk.com/products/3ds-max/) - Classic software for 3D modeling and rendering.
- 🆓 [ArmorPaint](https://armorpaint.org) - Physically-based texture painting, drop in your 3D models and paint. [[Source](https://github.com/armory3d/armortools) [![GitHub stars](https://img.shields.io/github/stars/armory3d/armortools?style=flat)](https://github.com/armory3d/armortools/stargazers)]
- 💰 [Asset Forge](https://assetforge.io) - Create 3D models and 2D sprites using building blocks.
- 🆓 [Blender](https://www.blender.org) 🔥 - Standard for open source 3D modeling. [[Source](https://github.com/blender/blender) [![GitHub stars](https://img.shields.io/github/stars/blender/blender?style=flat)](https://github.com/blender/blender/stargazers)]
- 🆓 [Meshroom](https://alicevision.org/#meshroom) - 3D reconstruction, built with the [AliceVision](https://github.com/alicevision/AliceVision) [![GitHub stars](https://img.shields.io/github/stars/alicevision/AliceVision?style=flat)](https://github.com/alicevision/AliceVision/stargazers) framework. [[Source](https://github.com/alicevision/meshroom) [![GitHub stars](https://img.shields.io/github/stars/alicevision/meshroom?style=flat)](https://github.com/alicevision/meshroom/stargazers)]
- 💸 [ZBrush](https://www.maxon.net/en/zbrush) - Simple and easy to use 3D sculpting tool.

### Particle Tools
- 💸 [Particle Designer](https://www.71squared.com/particledesigner) - Powerful particle effects editor designed for macOS.
- 💸 [TimelineFX](https://www.rigzsoft.co.uk) - Create amazing particle effects for your games, apps and webpages.

### Pixel Art
- 💸 [Aseprite](https://www.aseprite.org) - Animated sprite editor and pixel art tool. [[Source](https://github.com/aseprite/aseprite) [![GitHub stars](https://img.shields.io/github/stars/aseprite/aseprite?style=flat)](https://github.com/aseprite/aseprite/stargazers)]
- 💰 [Ditherdragon](https://winterveil.itch.io/ditherdragon) - Resample art, sketches and images into pixel-art.
- 💰 [Fluid FX](https://codemanu.itch.io/fluid-fx) - Uses fluid simulation to achieve animations like explosions, blood, smoke, etc.
- 💰 [Juice FX](https://codemanu.itch.io/juicefx) - Add style to your sprites and animations with ease.
- 🆓 [Piskel](https://www.piskelapp.com) - Online editor for animated sprites & pixel art. [[Source](https://github.com/piskelapp/piskel) [![GitHub stars](https://img.shields.io/github/stars/piskelapp/piskel?style=flat)](https://github.com/piskelapp/piskel/stargazers)]
- 💰 [PixaTool](https://kronbits.itch.io/pixatool) - Create pixel art by converting your images, sprites or videos.
- 💰 [Pixel FX](https://codemanu.itch.io/particle-fx-designer) - Create pixel art particle effects and render them to sprite sheets.
- 🎉 [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) [![GitHub stars](https://img.shields.io/github/stars/Orama-Interactive/Pixelorama?style=flat)](https://github.com/Orama-Interactive/Pixelorama/stargazers) - Open source pixel art multitool. [[Web Version](https://orama-interactive.itch.io/pixelorama)]
- 💰 [Smear FX](https://codemanu.itch.io/smear-fx) - Make your 2D animations juicy by adding some smearing to them.
- 💰 [Sprite Illuminator](https://www.codeandweb.com/spriteilluminator) - Create stunning light effects with 2D sprites in your game engine.
- 💰 [Texture Packer](https://www.codeandweb.com/texturepacker) - Create sprite sheets and optimize your game graphics.

### Tilemap Editors
- 🎉 [Ogmo Editor](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE) [![GitHub stars](https://img.shields.io/github/stars/Ogmo-Editor-3/OgmoEditor3-CE?style=flat)](https://github.com/Ogmo-Editor-3/OgmoEditor3-CE/stargazers) - Free, open source, project oriented tile map editor.
- 🆓 [Sprite Fusion](https://www.spritefusion.com/) - Free, web-based 2D tilemap editor with export to Unity, Godot, and more.
- 🆓 [Tiled](https://www.mapeditor.org) - General-purpose tile map editor for all tile-based games. [[Source](https://github.com/mapeditor/tiled) [![GitHub stars](https://img.shields.io/github/stars/mapeditor/tiled?style=flat)](https://github.com/mapeditor/tiled/stargazers)]

### Vector Editors
- 🆓 [Inkscape](https://inkscape.org) - Cross-platform, open source vector graphics editor. [[Source](https://github.com/inkscape/inkscape) [![GitHub stars](https://img.shields.io/github/stars/inkscape/inkscape?style=flat)](https://github.com/inkscape/inkscape/stargazers)]
- 🆓 [Krita](https://krita.org/en/) - Professional quality, open source painting. [[Source](https://github.com/KDE/krita) [![GitHub stars](https://img.shields.io/github/stars/KDE/krita?style=flat)](https://github.com/KDE/krita/stargazers)]
- 💰 [Vec Maker](https://kronbits.itch.io/vecmaker) - Easy to use vector design.

### Voxel
- 💰 [Ken Shape](https://tools.kenney.nl/kenshape/) - Draw in 2D, set the depth for each pixel and generate 3D models!
- 🎉 [IsoVoxel](https://github.com/tommyettinger/IsoVoxel) [![GitHub stars](https://img.shields.io/github/stars/tommyettinger/IsoVoxel?style=flat)](https://github.com/tommyettinger/IsoVoxel/stargazers) - Generates isometric pixel art from _MagicaVoxel_ .vox files.
- 🆓 [MagicaVoxel](https://ephtracy.github.io) - Lightweight voxel art editor.
- 💰 [Qubicle](http://minddesk.com/) - Popular (_Crossy Road_, _Pacman 256_) voxel editor, easy creation of 3D models.

<br />
<br />

## Video Game Assets
_Resources to help bring video games and game engines alive._

### Audio Assets
- Music
    - 🆓 [BandLab Sounds](https://www.bandlab.com/sounds/home) - High-quality loops and packs used for music creation.
    - 💸 [Bensound](https://www.bensound.com/royalty-free-music) - Original music tracks, free with attribution. Perfect for games.
    - 💸 [Incompetech](https://incompetech.com/wordpress/) - Nice collection of game tracks. Buy or attribution required.
    - 💸 [Melody Loops](https://www.melodyloops.com/music/free/) - Nice mix of free and affordable music loops.
    - 💸 [Soundimage](https://soundimage.org/looping-music/) - Looping music tracks for videogames. Buy or attribution required.
- Sound Effects
    - 🆓 [Freesound](https://freesound.org/browse/) - Community-based archive of free sound effects.
    - 💸 [Free Sound Effects](https://www.freesoundeffects.com/) - Large collection of sound effects.
    - 💰 [Soundsnap](https://www.soundsnap.com) - Subscription-based professional sound effects library.

### Graphic Assets
- 💸 [Flaticon](https://www.flaticon.com) - Quality vector icons and stickers.
- 💸 [Freepik](https://www.freepik.com) - Illustrations, photos, icons and presentation templates.
- 🆓 [Kenny](https://www.kenney.nl/assets) 🔥 - 2D/3D CC0 1.0 game graphics and other assets.
- 🆓 [Open Game Art](https://opengameart.org) - Portal for free / public domain game art online.
- 🆓 [Top Free Game Assets](https://itch.io/game-assets/free) - Top free game assets listed on _Itch.io_.

### Material Assets
- 🆓 [AmbientCG](https://ambientcg.com) - Public domain materials for physically-based rendering.
- 🆓 [Pmndrs Materials](https://github.com/pmndrs/market-assets/tree/main/files/materials) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/market-assets/tree/main/files/materials?style=flat)](https://github.com/pmndrs/market-assets/tree/main/files/materials/stargazers) - Collection of public domain materials.

### Model Assets
- 🆓 [Pmndrs Market](https://github.com/pmndrs/market) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/market?style=flat)](https://github.com/pmndrs/market/stargazers) - Collection of public domain models.
- 🆓 [Poly Pizza](https://poly.pizza) - Build something beautiful with thousands of free low poly models.
- 🆓 [Quaternius](https://quaternius.com) - Collection of CC0 1.0 3D models.
- 📚 [Retro3DGraphicsCollection](https://github.com/Miziziziz/Retro3DGraphicsCollection) [![GitHub stars](https://img.shields.io/github/stars/Miziziziz/Retro3DGraphicsCollection?style=flat)](https://github.com/Miziziziz/Retro3DGraphicsCollection/stargazers) - No attribution, retro (_PS1_ style) 3D graphics assets.
- 💸 [Sketchfab](https://sketchfab.com) - Huge library of 3D assets.

<br />
<br />

## Archive

_Dead links that have been removed are kept in the [Archive](ARCHIVE.md)._

<br />

## Legend

_The meaning behind the emoji._

- Open Source Software
    - ⭐ - [Public Domain License](https://en.wikipedia.org/wiki/Public-domain-equivalent_license) ([CC0](https://creativecommons.org/publicdomain/zero/1.0/), [BOLA](https://blitiri.com.ar/p/bola/), [WTFPL](https://en.wikipedia.org/wiki/WTFPL), [Unlicense](https://en.wikipedia.org/wiki/Unlicense), etc.)
    - 🎉 - [Permissive License](https://en.wikipedia.org/wiki/Permissive_software_license) ([MIT/Expat](https://en.wikipedia.org/wiki/MIT_License), [BSD](https://en.wikipedia.org/wiki/BSD_licenses), [ZLIB/LIBPNG](https://en.wikipedia.org/wiki/Zlib_License), [ISC](https://en.wikipedia.org/wiki/ISC_license), [Apache](https://en.wikipedia.org/wiki/Apache_License), [Boost](https://www.boost.org/users/license.html) etc.)
    - 🔒 - [Copyleft License](https://en.wikipedia.org/wiki/Copyleft) ([CC](https://en.wikipedia.org/wiki/Creative_Commons_license), [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License), [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), [MPL](https://en.wikipedia.org/wiki/Mozilla_Public_License), etc.)
    - ❓ - Unknown License
- Asset / Service / Tool
    - 🆓 - Free
    - 💰 - Paid
    - 💸 - Partially Free
- Other
    - 📚 - Article, Blog, Collection, List, Tutorial(s)
    - 🔥 - Hot! Amazing Resource!
    - 🌎 - Website

<br />

## Contributing

_See [Contribution Guide](CONTRIBUTING.md)._

<br />
