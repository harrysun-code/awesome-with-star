# Uno Platform

> 来源：[MartinZikmund/awesome-uno-platform](https://github.com/MartinZikmund/awesome-uno-platform)

[![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/awesome-uno-platform?style=flat)](https://github.com/MartinZikmund/awesome-uno-platform/stargazers)

<div align="center">
	<img width="160" src="media/logo.png" alt="Uno Platform">
	<h1>Awesome Uno Platform</h1>
	<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
</div>

[Uno Platform](https://platform.uno/) is an open-source UI Platform for building single-codebase .NET applications for Windows, iOS, Android, WebAssembly, macOS, and Linux.

This is a list of **awesome resources** for users of Uno Platform. **If you find the list helpful, please make sure to ⭐ star it!**

## Contents

- [General](#general)
- [Community](#community)
- [Repositories](#repositories)
- [Tools](#tools)
  - [IDE and Design](#ide-and-design)
  - [AI](#ai)
  - [Build and Deployment](#build-and-deployment)
  - [Testing](#testing)
- [Libraries](#libraries)
  - [Toolkits](#toolkits)
  - [Controls](#controls)
  - [Graphics](#graphics)
  - [Media](#media)
  - [MVVM](#mvvm)
  - [Dependency Injection](#dependency-injection)
  - [Integrations](#integrations)
  - [Compatibility](#compatibility)
- [Samples](#samples)
- [Live apps](#live-apps)
- [Open-source apps](#open-source-apps)
- [Games](#games)
- [Case Studies](#case-studies)
- [Blogs](#blogs)
- [Articles](#articles)
- [Courses and Tutorials](#courses-and-tutorials)
- [Live coding](#live-coding)
- [Talks](#talks)
- [Videos](#videos)
- [Podcasts](#podcasts)
- [Books](#books)

## General

- [Uno Platform Website](https://platform.uno/platforms/) - Supported platforms, features and product overview.
- [Uno Platform Documentation](https://platform.uno/docs/articles/intro.html) - Guides, tutorials and API reference.
- [Live Wizard](https://new.platform.uno/) - Browser-based wizard that configures a new project and generates the matching `dotnet new` command.
- [Get Started Guide](https://platform.uno/docs/articles/get-started.html) - Environment setup for each OS, IDE and AI agent, leading into the first-app tutorials.

## Community

- [Discord](https://platform.uno/discord) - Official chat server for questions, help and announcements.
- [GitHub Discussions](https://github.com/unoplatform/uno/discussions) - Q&A, ideas and show-and-tell forum on the main repository.
- [Stack Overflow](https://stackoverflow.com/questions/tagged/uno-platform) - Q&A tag for framework and tooling questions.
- [X (Twitter)](https://x.com/UnoPlatform) - Official account for release news and community highlights.
- [LinkedIn](https://www.linkedin.com/company/uno-platform/) - Official company page with product and release updates.
- [r/unoplatform](https://www.reddit.com/r/unoplatform/) - Official subreddit for news, tutorials and questions.
- [Uno Platform Newsletter](https://platform.uno/newsletter-sign-up/) - Email newsletter with release news, blog posts, tutorials and Uno Tech Bites videos.

## Repositories

- [Uno Platform](https://github.com/unoplatform/uno) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno?style=flat)](https://github.com/unoplatform/uno/stargazers) - Main repository of Uno Platform, including the full API surface of UWP/WinUI, the best place to submit issues and contribute.
- [Uno Themes](https://github.com/unoplatform/Uno.Themes) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Themes?style=flat)](https://github.com/unoplatform/Uno.Themes/stargazers) - Material and Cupertino theme library for Uno Platform apps. In addition, includes advanced controls based on Android/iOS developer guidelines.
- [Uno Toolkit](https://github.com/unoplatform/uno.toolkit.ui) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.toolkit.ui?style=flat)](https://github.com/unoplatform/uno.toolkit.ui/stargazers) - Multiplatform-first UI component library to speed up application development. Also provides Material and Cupertino styles for the included components.
- [Uno Gallery](https://github.com/unoplatform/Uno.Gallery) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Gallery?style=flat)](https://github.com/unoplatform/Uno.Gallery/stargazers) - Controls and API gallery app. Includes live examples of most built-in controls and features along with easy to use code snippets.
- [Uno Samples](https://github.com/unoplatform/Uno.Samples) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Samples?style=flat)](https://github.com/unoplatform/Uno.Samples/stargazers) - A growing collection of code samples and snippets.
- [Uno Core](https://github.com/unoplatform/Uno.Core) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Core?style=flat)](https://github.com/unoplatform/Uno.Core/stargazers) - Provides a set of reusable utilities and helpers. Used by the main Uno Platform repository.
- [Uno UI Test](https://github.com/unoplatform/Uno.UITest) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.UITest?style=flat)](https://github.com/unoplatform/Uno.UITest/stargazers) - Xamarin.UITest-style UI testing, using Selenium for WebAssembly and Xamarin.UITest for Android and iOS.

## Tools

### IDE and Design

- [Uno Platform Extension for Visual Studio](https://marketplace.visualstudio.com/items?itemName=unoplatform.uno-platform-addin-2022) - Project templates, Hot Reload and Hot Design tooling for Visual Studio 2022 and 2026.
- [Uno Platform Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=unoplatform.vscode) - Adds a range of productivity boosters to Visual Studio Code, including XAML IntelliSense, Hot Reload, and mobile target debugging support.
- [Uno Platform for Figma](https://www.figma.com/community/plugin/1045528009520465828/uno-platform-figma-to-c-or-xaml) - Figma plugin that generates responsive XAML or C# Markup from high-fidelity designs.
- [Uno Material Toolkit](https://www.figma.com/community/file/1110792522046146058/Uno-Platform-Material-Toolkit) - Figma file to use with the Figma plugin.
- [Uno Platform Studio](https://platform.uno/studio/) - Productivity suite bundling Hot Reload, Hot Design, design-to-code, MCP servers and an AI agent, usable from any IDE or OS.
- [Hot Design](https://platform.uno/hot-design/) - Agentic visual designer that turns the running app into an editable design surface, from Visual Studio, VS Code or Rider.
- [Hot Reload](https://platform.uno/hot-reload/) - Applies XAML and C# changes to the running app on every target without rebuilding, free in the Community tier.
- [Uno Platform Plugin for JetBrains Rider](https://plugins.jetbrains.com/plugin/24653-uno-platform) - Rider plugin adding project templates, Hot Reload and Hot Design support.
- [DevToolsUno](https://github.com/wieslawsoltes/DevToolsUno) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/DevToolsUno?style=flat)](https://github.com/wieslawsoltes/DevToolsUno/stargazers) - In-app diagnostics for inspecting the live visual tree, bindings, resources, styles, events and memory.
- [XAML Styler](https://github.com/Xavalon/XamlStyler) [![GitHub stars](https://img.shields.io/github/stars/Xavalon/XamlStyler?style=flat)](https://github.com/Xavalon/XamlStyler/stargazers) - XAML formatter for Visual Studio, Rider and the command line, used to enforce markup style in the official repositories.

### AI

- [Uno Platform MCP](https://platform.uno/mcp/) - Free remote MCP server that grounds AI agents in the current documentation and API references.
- [Uno App MCP](https://platform.uno/docs/articles/features/using-the-uno-mcps.html#app-mcp-local) - Local MCP server that lets AI agents inspect and drive a running app through its visual tree, properties, clicks, typing and screenshots.
- [Uno Platform Studio Agent Plugin](https://github.com/unoplatform/studio) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/studio?style=flat)](https://github.com/unoplatform/studio/stargazers) - Agent plugin with an app-building agent, topic skills (MVUX, navigation, Toolkit, themes, testing) and Hot Reload hooks for Claude Code, GitHub Copilot and Codex.
- [Uno Platform Studio App](https://studio.platform.uno/) - Browser-based AI app builder (Pro) that generates a project from a prompt, previews it live and exports it to your IDE.
- [dotnet-agentic-engineering (dna)](https://github.com/VincentH-Net/dotnet-agentic-engineering) [![GitHub stars](https://img.shields.io/github/stars/VincentH-Net/dotnet-agentic-engineering?style=flat)](https://github.com/VincentH-Net/dotnet-agentic-engineering/stargazers) - Agent directives, skills and tooling that detect a repo's stack (MVUX or MVVM, C# Markup, design system, SDK version) and install a matching skill set.
- [Uno Platform Skills](https://github.com/noknowscode/UnoPlatformSkills) [![GitHub stars](https://img.shields.io/github/stars/noknowscode/UnoPlatformSkills?style=flat)](https://github.com/noknowscode/UnoPlatformSkills/stargazers) - Claude Code skills covering MVUX, navigation, Toolkit, Material theming, C# Markup, WebAssembly and WPF migration.
- [Uno DevServer CLI](https://www.nuget.org/packages/Uno.DevServer) - Dev Server CLI that registers the MCPs with AI agents, diagnoses the environment and drives a running app from scripts or CI.

### Build and Deployment

- [Uno.Check](https://github.com/unoplatform/uno.check) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.check?style=flat)](https://github.com/unoplatform/uno.check/stargazers) - CLI that checks and installs the SDKs, workloads and tooling needed for each target platform.
- [Uno.Templates and Uno.Sdk](https://github.com/unoplatform/uno.templates) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.templates?style=flat)](https://github.com/unoplatform/uno.templates/stargazers) - The `dotnet new` app and library templates plus the single-project MSBuild SDK they build on.
- [Uno.Wasm.Bootstrap](https://github.com/unoplatform/Uno.Wasm.Bootstrap) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Wasm.Bootstrap?style=flat)](https://github.com/unoplatform/Uno.Wasm.Bootstrap/stargazers) - MSBuild package that builds and hosts .NET code in the browser via WebAssembly, with AOT and PWA support.
- [Uno.XamlMerge.Task](https://github.com/unoplatform/uno.xamlmerge.task) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.xamlmerge.task?style=flat)](https://github.com/unoplatform/uno.xamlmerge.task/stargazers) - MSBuild task that merges a control library's resource dictionaries into a single file for faster resource lookup.
- [DependencyPropertyGenerator](https://github.com/HavenDV/DependencyPropertyGenerator) [![GitHub stars](https://img.shields.io/github/stars/HavenDV/DependencyPropertyGenerator?style=flat)](https://github.com/HavenDV/DependencyPropertyGenerator/stargazers) - Source generator for dependency properties, routed events and weak events, with automatic Uno detection.
- [Velopack](https://github.com/velopack/velopack) [![GitHub stars](https://img.shields.io/github/stars/velopack/velopack?style=flat)](https://github.com/velopack/velopack/stargazers) - Installer and auto-update framework for desktop apps, with an official Uno sample and setup guide.
- [Uno.Resizetizer](https://github.com/unoplatform/uno.resizetizer) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.resizetizer?style=flat)](https://github.com/unoplatform/uno.resizetizer/stargazers) - Build-time generation of app icons, splash screens and scaled images from SVG or PNG sources.

### Testing

- [Uno.UI.RuntimeTests.Engine](https://github.com/unoplatform/uno.ui.runtimetests.engine) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.ui.runtimetests.engine?style=flat)](https://github.com/unoplatform/uno.ui.runtimetests.engine/stargazers) - In-app MSTest runner for UI tests on devices, desktop and the browser, with NUnit reports and CI sharding.

## Libraries

### Toolkits

- [Uno Extensions](https://github.com/unoplatform/uno.extensions) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.extensions?style=flat)](https://github.com/unoplatform/uno.extensions/stargazers) - NuGet packages for navigation, DI, configuration, HTTP, localization and the MVUX reactive pattern.
- [Telerik UI for Uno](https://github.com/unoplatform/Uno.Telerik.UI-For-UWP) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Telerik.UI-For-UWP?style=flat)](https://github.com/unoplatform/Uno.Telerik.UI-For-UWP/stargazers) - Community port of the open-source Telerik UI for UWP controls.
- [MZikmund Toolkit](https://github.com/MartinZikmund/mzikmund-toolkit) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/mzikmund-toolkit?style=flat)](https://github.com/MartinZikmund/mzikmund-toolkit/stargazers) - Reusable app services such as preferences storage and a ContentDialog coordinator, with a gallery sample app, by Martin Zikmund.
- [Windows Community Toolkit](https://github.com/CommunityToolkit/Windows) [![GitHub stars](https://img.shields.io/github/stars/CommunityToolkit/Windows?style=flat)](https://github.com/CommunityToolkit/Windows/stargazers) - Microsoft-backed collection of WinUI controls, helpers and extensions that ships builds for every target.
- [dt (搬运工)](https://github.com/Daoting/dt) [![GitHub stars](https://img.shields.io/github/stars/Daoting/dt?style=flat)](https://github.com/Daoting/dt/stargazers) - Chinese-language framework for rapid line-of-business apps, with reusable client controls and backend microservices.
- [Infragistics Ultimate UI for Uno Platform](https://github.com/Infragistics/uno-samples) [![GitHub stars](https://img.shields.io/github/stars/Infragistics/uno-samples?style=flat)](https://github.com/Infragistics/uno-samples/stargazers) - Commercial (beta) charts, data grid, geographic maps, gauges and dashboard components, with a samples browser.
- [Flowery.Uno](https://github.com/tobitege/Flowery.Uno) [![GitHub stars](https://img.shields.io/github/stars/tobitege/Flowery.Uno?style=flat)](https://github.com/tobitege/Flowery.Uno/stargazers) - Over 100 DaisyUI-inspired themed controls, localized in 12 languages.
- [CherylUI.Uno](https://github.com/kikipoulet/CherylUI.Uno) [![GitHub stars](https://img.shields.io/github/stars/kikipoulet/CherylUI.Uno?style=flat)](https://github.com/kikipoulet/CherylUI.Uno/stargazers) - Mobile-styled controls and styles ported from the CherylUI library.
- [Uno.Fonts](https://github.com/unoplatform/uno.fonts) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.fonts?style=flat)](https://github.com/unoplatform/uno.fonts/stargazers) - Font packages with Fluent and MDL2 icon fonts as drop-in Segoe replacements, plus Roboto, Open Sans and Inter.

### Controls

- [Uno Monaco Editor](https://github.com/unoplatform/uno.monaco.editor) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.monaco.editor?style=flat)](https://github.com/unoplatform/uno.monaco.editor/stargazers) - Monaco (VS Code) code editor control with language providers, diff view and two-way text binding for WebAssembly and desktop.
- [Uno ColorCode](https://github.com/unoplatform/Uno.ColorCode-Universal) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.ColorCode-Universal?style=flat)](https://github.com/unoplatform/Uno.ColorCode-Universal/stargazers) - Syntax highlighting library that renders source code into a RichTextBlock or HTML.
- [LiveCharts2](https://github.com/Live-Charts/LiveCharts2) [![GitHub stars](https://img.shields.io/github/stars/Live-Charts/LiveCharts2?style=flat)](https://github.com/Live-Charts/LiveCharts2/stargazers) - Interactive, animated charts, maps and gauges drawn with SkiaSharp.
- [ScottPlot](https://github.com/ScottPlot/ScottPlot) [![GitHub stars](https://img.shields.io/github/stars/ScottPlot/ScottPlot?style=flat)](https://github.com/ScottPlot/ScottPlot/stargazers) - Interactive plotting library built for large scientific and high-density datasets.
- [Mapsui](https://github.com/Mapsui/Mapsui) [![GitHub stars](https://img.shields.io/github/stars/Mapsui/Mapsui?style=flat)](https://github.com/Mapsui/Mapsui/stargazers) - Map component with tile layers, vector data and touch interaction.
- [WinUI.TableView](https://github.com/w-ahmad/WinUI.TableView) [![GitHub stars](https://img.shields.io/github/stars/w-ahmad/WinUI.TableView?style=flat)](https://github.com/w-ahmad/WinUI.TableView/stargazers) - Lightweight, fast DataGrid control with Excel-like column filtering, sorting, editing and export.
- [WinUI.Dock](https://github.com/qian-o/WinUI.Dock) [![GitHub stars](https://img.shields.io/github/stars/qian-o/WinUI.Dock?style=flat)](https://github.com/qian-o/WinUI.Dock/stargazers) - Visual Studio-style docking controls, with limited floating-window support.
- [UnoDock](https://github.com/wieslawsoltes/UnoDock) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/UnoDock?style=flat)](https://github.com/wieslawsoltes/UnoDock/stargazers) - IDE-style docking with documents, tool windows, auto-hide, floating windows and themes.
- [RibbonSpace](https://github.com/wieslawsoltes/RibbonSpace) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/RibbonSpace?style=flat)](https://github.com/wieslawsoltes/RibbonSpace/stargazers) - Office-style ribbon with adaptive layouts, contextual tabs, backstage, Quick Access Toolbar and KeyTips.
- [UnoEdit](https://github.com/lextudio/UnoEdit) [![GitHub stars](https://img.shields.io/github/stars/lextudio/UnoEdit?style=flat)](https://github.com/lextudio/UnoEdit/stargazers) - Code editor control with syntax highlighting, ported from AvalonEdit.
- [ScreenKeyboard](https://github.com/wieslawsoltes/ScreenKeyboardControl) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/ScreenKeyboardControl?style=flat)](https://github.com/wieslawsoltes/ScreenKeyboardControl/stargazers) - Themable on-screen keyboard with glide typing, gestures, emoji and 90+ layouts.
- [UnoKeyboard](https://github.com/mcNets/UnoKeyboard) [![GitHub stars](https://img.shields.io/github/stars/mcNets/UnoKeyboard?style=flat)](https://github.com/mcNets/UnoKeyboard/stargazers) - On-screen virtual keyboard for touch-screen desktop, Windows and WebAssembly apps.
- [Broadside](https://github.com/michaelstonis/Broadside) [![GitHub stars](https://img.shields.io/github/stars/michaelstonis/Broadside?style=flat)](https://github.com/michaelstonis/Broadside/stargazers) - Fully managed PDF library for reading, writing, editing and rendering, with an embeddable viewer.
- [CSharpMath](https://github.com/verybadcat/CSharpMath) [![GitHub stars](https://img.shields.io/github/stars/verybadcat/CSharpMath?style=flat)](https://github.com/verybadcat/CSharpMath/stargazers) - LaTeX math typesetting and rendering, ported from iosMath.
- [Pysar](https://github.com/MriyaLab/Pysar) [![GitHub stars](https://img.shields.io/github/stars/MriyaLab/Pysar?style=flat)](https://github.com/MriyaLab/Pysar/stargazers) - Report engine for paginated documents with an in-app report view, PDF export, printing and sharing.
- [FluentIcons](https://github.com/davidxuang/FluentIcons) [![GitHub stars](https://img.shields.io/github/stars/davidxuang/FluentIcons?style=flat)](https://github.com/davidxuang/FluentIcons/stargazers) - Fluent UI System Icons as icon controls, icon sources and markup extensions.
- [DesktopFlyouts](https://github.com/0x5bfa/DesktopFlyouts) [![GitHub stars](https://img.shields.io/github/stars/0x5bfa/DesktopFlyouts?style=flat)](https://github.com/0x5bfa/DesktopFlyouts/stargazers) - Desktop flyouts shown from tray icons or programmatically, including on Linux with X11.

### Graphics

- [SkiaSharp](https://github.com/mono/SkiaSharp) [![GitHub stars](https://img.shields.io/github/stars/mono/SkiaSharp?style=flat)](https://github.com/mono/SkiaSharp/stargazers) - Cross-platform 2D graphics API based on Google's Skia, with XAML canvas views.
- [Svg.Skia](https://github.com/wieslawsoltes/Svg.Skia) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/Svg.Skia?style=flat)](https://github.com/wieslawsoltes/Svg.Skia/stargazers) - SVG rendering library with animated SVG controls and inline SVG authoring in XAML.
- [ProGPU](https://github.com/wieslawsoltes/ProGPU) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/ProGPU?style=flat)](https://github.com/wieslawsoltes/ProGPU/stargazers) - WebGPU-based rendering, composition, vector and text engine with an embeddable host control.
- [Zenith.NET](https://github.com/qian-o/Zenith.NET) [![GitHub stars](https://img.shields.io/github/stars/qian-o/Zenith.NET?style=flat)](https://github.com/qian-o/Zenith.NET/stargazers) - GPU graphics and compute abstraction over DirectX 12, Metal and Vulkan, with a rendering view control.
- [Ab4d.SharpEngine](https://www.ab4d.com/SharpEngine.aspx) - Commercial cross-platform 3D rendering engine built on Vulkan, free for non-commercial open-source projects.
- [SKCanvasElement](https://platform.uno/docs/articles/controls/SKCanvasElement.html) - Hardware-accelerated SkiaSharp drawing hosted directly in the XAML visual tree.
- [GLCanvasElement](https://platform.uno/docs/articles/controls/GLCanvasElement.html) - OpenGL rendering through Silk.NET inside the XAML visual tree, with WebGL on WebAssembly.
- [Lottie Animations](https://platform.uno/docs/articles/features/Lottie.html) - Built-in Lottie playback through AnimatedVisualPlayer, rendered with Skottie or a managed engine.

### Media

- [VisioForge Media Framework](https://www.visioforge.com/) - Commercial SDKs for video capture, playback, editing and streaming, including a cross-platform video view control.
- [LibVLCSharp](https://github.com/videolan/libvlcsharp) [![GitHub stars](https://img.shields.io/github/stars/videolan/libvlcsharp?style=flat)](https://github.com/videolan/libvlcsharp/stargazers) - VLC-based media playback bindings with a MediaPlayerElement control for Windows, Android and iOS.

### MVVM

- [MVx.Observable](https://www.nuget.org/packages/MVx.Observable/) - A (mostly) unopinionated, light-weight alternative to ReactiveUI provided as a library _not a framework_.
- [Prism](https://prismlibrary.com/) - Framework for building loosely coupled, modular, maintainable, and testable XAML applications.
- [Microsoft MVVM Toolkit](https://learn.microsoft.com/dotnet/communitytoolkit/mvvm/) - Modern, fast, and modular MVVM library.
- [Microsoft.UI.Reactor for Uno](https://github.com/unoplatform/Uno.microsoft-ui-reactor) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.microsoft-ui-reactor?style=flat)](https://github.com/unoplatform/Uno.microsoft-ui-reactor/stargazers) - Experimental port of Microsoft's React-style framework for building UI from C# components and hooks without XAML.
- [XAML Behaviors for Uno](https://github.com/unoplatform/Uno.XamlBehaviors) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.XamlBehaviors?style=flat)](https://github.com/unoplatform/Uno.XamlBehaviors/stargazers) - Port of XAML Behaviors with triggers, actions and InvokeCommandAction for non-Windows targets.
- [ReactiveUI.Uno](https://github.com/reactiveui/ReactiveUI.Uno) [![GitHub stars](https://img.shields.io/github/stars/reactiveui/ReactiveUI.Uno?style=flat)](https://github.com/reactiveui/ReactiveUI.Uno/stargazers) - ReactiveUI integration with view bases, activation, routing, bindings and schedulers.
- [R3](https://github.com/Cysharp/R3) [![GitHub stars](https://img.shields.io/github/stars/Cysharp/R3?style=flat)](https://github.com/Cysharp/R3/stargazers) - Modern reimplementation of Reactive Extensions, with an extension package for dispatcher-timer and rendering-frame providers.
- [Singulink UI Toolkit](https://github.com/Singulink/Singulink.UI) [![GitHub stars](https://img.shields.io/github/stars/Singulink/Singulink.UI?style=flat)](https://github.com/Singulink/Singulink.UI/stargazers) - Strongly typed, deep-linkable MVVM navigation plus a task runner, XAML helpers and trimmed Fluent icon packs.
- [Chinook.DynamicMvvm](https://github.com/nventive/Chinook.DynamicMvvm) [![GitHub stars](https://img.shields.io/github/stars/nventive/Chinook.DynamicMvvm?style=flat)](https://github.com/nventive/Chinook.DynamicMvvm/stargazers) - Declarative and extensible ViewModels, properties and commands, by nventive.
- [Chinook.Navigation](https://github.com/nventive/Chinook.Navigation) [![GitHub stars](https://img.shields.io/github/stars/nventive/Chinook.Navigation?style=flat)](https://github.com/nventive/Chinook.Navigation/stargazers) - ViewModel-first stack, sections and modal navigation, by nventive.
- [Shiny Mediator](https://github.com/shinyorg/mediator) [![GitHub stars](https://img.shields.io/github/stars/shinyorg/mediator?style=flat)](https://github.com/shinyorg/mediator/stargazers) - Mediator pattern library with app middleware for caching, offline, resilience and main-thread dispatch.

### Dependency Injection

- [Pure.DI](https://github.com/DevTeam/Pure.DI) [![GitHub stars](https://img.shields.io/github/stars/DevTeam/Pure.DI?style=flat)](https://github.com/DevTeam/Pure.DI/stargazers) - Generates dependency injection object graphs at compile time without requiring a runtime container by [Nikolay Pianikov](https://github.com/NikolayPianikov) [![GitHub stars](https://img.shields.io/github/stars/NikolayPianikov?style=flat)](https://github.com/NikolayPianikov/stargazers).

### Integrations

- [Uno.AdMob](https://github.com/MartinZikmund/Uno.AdMob) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/Uno.AdMob?style=flat)](https://github.com/MartinZikmund/Uno.AdMob/stargazers) - Google AdMob banner, interstitial, rewarded and app open ads with UMP consent on Android and iOS.
- [Uno.RevenueCat](https://github.com/MartinZikmund/Uno.RevenueCat) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/Uno.RevenueCat?style=flat)](https://github.com/MartinZikmund/Uno.RevenueCat/stargazers) - RevenueCat in-app purchases and subscriptions for Android and iOS.
- [Uno.SQLitePCLRaw.Wasm](https://github.com/unoplatform/Uno.SQLitePCLRaw.Wasm) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.SQLitePCLRaw.Wasm?style=flat)](https://github.com/unoplatform/Uno.SQLitePCLRaw.Wasm/stargazers) - SQLitePCLRaw provider that brings SQLite, sqlite-net and EF Core to WebAssembly apps.
- [Shiny](https://github.com/shinyorg/shiny) [![GitHub stars](https://img.shields.io/github/stars/shinyorg/shiny?style=flat)](https://github.com/shinyorg/shiny/stargazers) - Device and background services such as jobs, Bluetooth LE, push notifications, geofencing and GPS.
- [32feet.NET](https://github.com/inthehand/32feet) [![GitHub stars](https://img.shields.io/github/stars/inthehand/32feet?style=flat)](https://github.com/inthehand/32feet/stargazers) - Bluetooth Classic, Bluetooth LE and NFC library with an API modeled on Web Bluetooth.
- [Datasync Community Toolkit](https://github.com/CommunityToolkit/Datasync) [![GitHub stars](https://img.shields.io/github/stars/CommunityToolkit/Datasync?style=flat)](https://github.com/CommunityToolkit/Datasync/stargazers) - Offline-capable data synchronization between client apps and an ASP.NET Core backend.

### Compatibility

- [SignalR](https://learn.microsoft.com/aspnet/core/signalr/introduction) - [Cross-Platform Real-Time Communication with Uno & SignalR](https://ian.bebbs.co.uk/posts/UnoChat) - Integration example for the SignalR framework.
- [Elmish.Uno](https://github.com/xperiandri/Elmish.Uno) [![GitHub stars](https://img.shields.io/github/stars/xperiandri/Elmish.Uno?style=flat)](https://github.com/xperiandri/Elmish.Uno/stargazers) - Half-Elmish framework for apps written in F#.
- [C# Markup](https://platform.uno/docs/articles/external/uno.extensions/doc/Learn/Markup/Overview.html) - Fluent C# API for declaring UI, including bindings, styles and resources, as an alternative to XAML.
- [.NET MAUI Embedding](https://platform.uno/docs/articles/external/uno.extensions/doc/Learn/Maui/MauiOverview.html) - Hosts .NET MAUI controls, including third-party vendor suites, inside apps on iOS, Android, macOS and Windows.
- [C# Markup 2](https://github.com/VincentH-Net/CSharpForMarkup) [![GitHub stars](https://img.shields.io/github/stars/VincentH-Net/CSharpForMarkup?style=flat)](https://github.com/VincentH-Net/CSharpForMarkup/stargazers) - Concise, declarative C# UI markup with Uno Toolkit, Navigation and MVUX support and `dotnet new` templates.
- [Majorsilence.Forms](https://github.com/majorsilence/Majorsilence.Forms) [![GitHub stars](https://img.shields.io/github/stars/majorsilence/Majorsilence.Forms?style=flat)](https://github.com/majorsilence/Majorsilence.Forms/stargazers) - Cross-platform Windows Forms API that runs WinForms-style apps on desktop, mobile and WebAssembly.

## Samples

- [Wayfarer](https://github.com/MartinZikmund/Wayfarer) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/Wayfarer?style=flat)](https://github.com/MartinZikmund/Wayfarer/stargazers) - Travel journal sample showcasing LinedFlowLayout, RichEditBox, Composition animations, multi-window and tvOS support.
- [Fun with SkiaSharp](https://github.com/MartinZikmund/fun-with-skiasharp) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/fun-with-skiasharp?style=flat)](https://github.com/MartinZikmund/fun-with-skiasharp/stargazers) - Nineteen SkiaSharp visual demos and minigames from the SkiaSharp 4 launch event, with a live WebAssembly gallery.
- [Uno App Template](https://github.com/MartinZikmund/uno-app-template) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/uno-app-template?style=flat)](https://github.com/MartinZikmund/uno-app-template/stargazers) - Opinionated app template with MVVM, DI, navigation, localization, versioning and multi-store release pipelines.
- [Uno Chefs](https://github.com/unoplatform/uno.chefs) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uno.chefs?style=flat)](https://github.com/unoplatform/uno.chefs/stargazers) - Official recipe reference app demonstrating MVUX, navigation, Material theming and Toolkit controls.
- [League of Legends Client](https://github.com/JamesnetGroup/leagueoflegends-uno) [![GitHub stars](https://img.shields.io/github/stars/JamesnetGroup/leagueoflegends-uno?style=flat)](https://github.com/JamesnetGroup/leagueoflegends-uno/stargazers) - Recreation of the League of Legends client UI showing custom controls and a modular architecture for large XAML apps.
- [nventive Uno Application Template](https://github.com/nventive/UnoApplicationTemplate) [![GitHub stars](https://img.shields.io/github/stars/nventive/UnoApplicationTemplate?style=flat)](https://github.com/nventive/UnoApplicationTemplate/stargazers) - Production-grade dotnet new mobile app template with MVVM, dependency injection, logging and built-in diagnostic tools.
- [DevTKSS Uno Sample Apps](https://github.com/DevTKSS/DevTKSS.Uno.SampleApps) [![GitHub stars](https://img.shields.io/github/stars/DevTKSS/DevTKSS.Uno.SampleApps?style=flat)](https://github.com/DevTKSS/DevTKSS.Uno.SampleApps/stargazers) - Bilingual German and English sample apps and step-by-step tutorials covering MVUX, navigation and other Uno.Extensions features.

## Live apps

- [Uno Playground](https://playground.platform.uno) - Experiment with C# and XAML right from the browser.
- [Uno Calculator](https://calculator.platform.uno/) - WebAssembly port of the Windows Calculator app.
- [NuGet.info](https://nuget.info/) - Modernized version of NuGet Package Explorer application.
- [Windows Community Toolkit Gallery](https://toolkitlabs.dev/) - Live gallery of Windows Community Toolkit controls and helpers, including experimental Labs components.
- [Unexpected APIs in Uno Platform](https://unexpectedapis.uno/) - Demo app including various UI and non-UI APIs that you can use in Uno Platform.
- [Uno Gallery](https://gallery.platform.uno/) - Browser version of the control and theme gallery with live samples and code snippets.
- [Uno Space](https://wieslawsoltes.github.io/UnoSpace/) - Seventeen local-first desktop-class apps, from a word processor and spreadsheet to PDF, CAD and Git tools, running in the browser.
- [Fluent Stopwatch](https://fluentstopwatch.uno/) - Stopwatch with multiple timers, laps and history, by Martin Zikmund.
- [XAML-MAN](https://martinzikmund.github.io/XamlMan/) - Arcade-accurate Pac-Man clone rendered entirely in XAML, by Martin Zikmund.
- [UnoDOOM](https://happy-tree-0e73b8e10.3.azurestaticapps.net/) - Playable cross-platform DOOM port based on ManagedDoom, with a bundled Freedoom WAD, by Martin Zikmund.
- [Roslyn Quoter](https://roslynquoter-wasm.platform.uno/) - Shows the Roslyn SyntaxFactory API calls that construct any given C# program.
- [SQLite + Entity Framework Core in WebAssembly](https://sqliteefcore-wasm.platform.uno/) - In-browser C# editor that compiles code with Roslyn and runs Entity Framework Core against SQLite.

## Open-source apps

- [UADO](https://github.com/unoplatform/uado) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/uado?style=flat)](https://github.com/unoplatform/uado/stargazers) - Azure DevOps backlog viewer.
- [Uno Playground](https://github.com/unoplatform/Uno.Playground) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Playground?style=flat)](https://github.com/unoplatform/Uno.Playground/stargazers) - Source code of the in-browser playground, with UI samples.
- [Uno Calculator](https://github.com/unoplatform/calculator) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/calculator?style=flat)](https://github.com/unoplatform/calculator/stargazers) - Port of the open-source Windows Calculator to C# for iOS, macOS, Android, WebAssembly and Linux.
- [NuGet Package Explorer](https://github.com/NuGetPackageExplorer/NuGetPackageExplorer/tree/main/Uno) [![GitHub stars](https://img.shields.io/github/stars/NuGetPackageExplorer/NuGetPackageExplorer/tree/main/Uno?style=flat)](https://github.com/NuGetPackageExplorer/NuGetPackageExplorer/tree/main/Uno/stargazers) - Source code of the Uno Platform version of NuGet Package Explorer.
- [Ch9](https://github.com/unoplatform/Uno.Ch9) [![GitHub stars](https://img.shields.io/github/stars/unoplatform/Uno.Ch9?style=flat)](https://github.com/unoplatform/Uno.Ch9/stargazers) - Channel 9 browser app.
- [CODuo](https://github.com/ibebbs/CODuo) [![GitHub stars](https://img.shields.io/github/stars/ibebbs/CODuo?style=flat)](https://github.com/ibebbs/CODuo/stargazers) - Visualizing the environmental impact of current and forecast energy generation in the UK. Designed for use on both single and dual-screen devices.
- [Eppie](https://github.com/Eppie-io/Eppie-App) [![GitHub stars](https://img.shields.io/github/stars/Eppie-io/Eppie-App?style=flat)](https://github.com/Eppie-io/Eppie-App/stargazers) - Encrypted peer-to-peer email client that also works with regular IMAP/SMTP accounts.
- [Daily Plants](https://github.com/MartinZikmund/daily-plants) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/daily-plants?style=flat)](https://github.com/MartinZikmund/daily-plants/stargazers) - Private checklist for Dr. Greger's Daily Dozen and Twenty-One Tweaks, with streaks, statistics and 21 languages.
- [Fluent Stopwatch](https://github.com/MartinZikmund/stopwatch) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/stopwatch?style=flat)](https://github.com/MartinZikmund/stopwatch/stargazers) - Stopwatch with multiple timers, laps and history, also usable in the browser.
- [MZikmund.dev](https://github.com/MartinZikmund/mzikmund) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/mzikmund?style=flat)](https://github.com/MartinZikmund/mzikmund/stargazers) - Personal website and blog platform with an ASP.NET Core backend and a cross-platform reader and admin app.
- [Uno Cockpit](https://github.com/MartinZikmund/UnoCockpit) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/UnoCockpit?style=flat)](https://github.com/MartinZikmund/UnoCockpit/stargazers) - WebAssembly dashboard for in-car browsers with a trip HUD, gamepad arcade game, photo booth and sensor lab.
- [Sefirah](https://github.com/shrimqy/Sefirah) [![GitHub stars](https://img.shields.io/github/stars/shrimqy/Sefirah?style=flat)](https://github.com/shrimqy/Sefirah/stargazers) - Phone Link alternative that syncs clipboard, notifications, files and media between Android and the desktop.
- [2fast](https://github.com/2fast-team/2fast) [![GitHub stars](https://img.shields.io/github/stars/2fast-team/2fast?style=flat)](https://github.com/2fast-team/2fast/stargazers) - Two-factor TOTP authenticator for Windows, Android, iOS, Linux and macOS.
- [SecureFolderFS](https://github.com/securefolderfs-community/SecureFolderFS) [![GitHub stars](https://img.shields.io/github/stars/securefolderfs-community/SecureFolderFS?style=flat)](https://github.com/securefolderfs-community/SecureFolderFS/stargazers) - File encryption app that protects folders as vaults with on-the-fly encryption.
- [Strix Music](https://github.com/Arlodotexe/strix-music) [![GitHub stars](https://img.shields.io/github/stars/Arlodotexe/strix-music?style=flat)](https://github.com/Arlodotexe/strix-music/stargazers) - Alpha-stage music player and SDK that merges multiple music sources into a single reskinnable library.
- [Azure Key Vault Explorer](https://github.com/cricketthomas/AzureKeyVaultExplorer) [![GitHub stars](https://img.shields.io/github/stars/cricketthomas/AzureKeyVaultExplorer?style=flat)](https://github.com/cricketthomas/AzureKeyVaultExplorer/stargazers) - Desktop app for finding, filtering and reading secrets, keys and certificates across Azure Key Vaults.
- [asERP](https://github.com/andrich-software/asERP) [![GitHub stars](https://img.shields.io/github/stars/andrich-software/asERP?style=flat)](https://github.com/andrich-software/asERP/stargazers) - Self-hosted retail ERP toolkit with a REST API and cross-platform desktop, web and mobile clients.
- [Emerald](https://github.com/RiversideValley/Emerald) [![GitHub stars](https://img.shields.io/github/stars/RiversideValley/Emerald?style=flat)](https://github.com/RiversideValley/Emerald/stargazers) - Minecraft launcher for Windows, macOS and Linux with multi-instance profiles.
- [StoryCAD](https://github.com/storybuilder-org/StoryCAD) [![GitHub stars](https://img.shields.io/github/stars/storybuilder-org/StoryCAD?style=flat)](https://github.com/storybuilder-org/StoryCAD/stargazers) - Free outlining tool that helps fiction writers plan characters, plots and settings.
- [Scrubbler 2](https://github.com/Scrubbler-Dev/Scrubbler-2) [![GitHub stars](https://img.shields.io/github/stars/Scrubbler-Dev/Scrubbler-2?style=flat)](https://github.com/Scrubbler-Dev/Scrubbler-2/stargazers) - Plugin-based manual scrobbler for listens that a player or service failed to submit.
- [Sentry Desktop Crash Reporter](https://github.com/getsentry/sentry-desktop-crash-reporter) [![GitHub stars](https://img.shields.io/github/stars/getsentry/sentry-desktop-crash-reporter?style=flat)](https://github.com/getsentry/sentry-desktop-crash-reporter/stargazers) - Sentry's cross-platform crash reporter that asks users for feedback and consent before submitting a report.
- [Celbridge](https://github.com/celbridge-org/celbridge) [![GitHub stars](https://img.shields.io/github/stars/celbridge-org/celbridge?style=flat)](https://github.com/celbridge-org/celbridge/stargazers) - Workbench for building HTML-based tools for game dev teams, with Python scripting and spreadsheet support.
- [SubZero Framework Edition](https://github.com/TekuSP/SubZeroFramework) [![GitHub stars](https://img.shields.io/github/stars/TekuSP/SubZeroFramework?style=flat)](https://github.com/TekuSP/SubZeroFramework/stargazers) - Fan control and thermal telemetry app for Framework laptops on Windows and Linux.
- [DotUninstall](https://github.com/lextudio/DotUninstall) [![GitHub stars](https://img.shields.io/github/stars/lextudio/DotUninstall?style=flat)](https://github.com/lextudio/DotUninstall/stargazers) - Graphical front end for the dotnet-core-uninstall tool that removes old .NET SDKs and runtimes on Windows and macOS.
- [Matroska Batch Flow](https://github.com/TimGels/Matroska-Batch-Flow) [![GitHub stars](https://img.shields.io/github/stars/TimGels/Matroska-Batch-Flow?style=flat)](https://github.com/TimGels/Matroska-Batch-Flow/stargazers) - Batch editor for Matroska (MKV) container and track properties across many files.
- [Recurrents](https://github.com/morning4coffe-dev/recurrents) [![GitHub stars](https://img.shields.io/github/stars/morning4coffe-dev/recurrents?style=flat)](https://github.com/morning4coffe-dev/recurrents/stargazers) - Subscription tracker with payment reminders and spending overview.
- [Pāli Practice](https://github.com/DhammaBytes/PaliPractice) [![GitHub stars](https://img.shields.io/github/stars/DhammaBytes/PaliPractice?style=flat)](https://github.com/DhammaBytes/PaliPractice/stargazers) - Flashcard app that uses spaced repetition to drill Pāli noun declensions and verb conjugations.
- [Elapsed](https://github.com/hackclub/elapsed) [![GitHub stars](https://img.shields.io/github/stars/hackclub/elapsed?style=flat)](https://github.com/hackclub/elapsed/stargazers) - Desktop and mobile client for Hack Club's Lapse timelapse programme, with a companion CLI.
- [PixlPunkt](https://github.com/ChadRoesler/PixlPunkt) [![GitHub stars](https://img.shields.io/github/stars/ChadRoesler/PixlPunkt?style=flat)](https://github.com/ChadRoesler/PixlPunkt/stargazers) - Pixel art editor with animation and a plugin SDK, with builds for Windows, macOS and Linux.
- [HouzLinc](https://github.com/Lakeside-Apps/HouzLinc) [![GitHub stars](https://img.shields.io/github/stars/Lakeside-Apps/HouzLinc?style=flat)](https://github.com/Lakeside-Apps/HouzLinc/stargazers) - Local-network configuration app for Insteon home automation devices and scenes.
- [RoMi](https://github.com/DrHardReset/RoMi) [![GitHub stars](https://img.shields.io/github/stars/DrHardReset/RoMi?style=flat)](https://github.com/DrHardReset/RoMi/stargazers) - Calculator for the SysEx MIDI messages that remote-control Roland keyboards and synthesizers.
- [Daily Reflection](https://github.com/kazo0/DailyReflection) [![GitHub stars](https://img.shields.io/github/stars/kazo0/DailyReflection?style=flat)](https://github.com/kazo0/DailyReflection/stargazers) - Reader for the A.A. Daily Reflections, migrated in place from Xamarin.Forms and live on Google Play and the App Store.
- [TextSpace](https://github.com/wieslawsoltes/TextSpace) [![GitHub stars](https://img.shields.io/github/stars/wieslawsoltes/TextSpace?style=flat)](https://github.com/wieslawsoltes/TextSpace/stargazers) - Local-first word processor with paginated editing, a ribbon and DOCX/PDF export, running on desktop and in the browser.
- [Salmon Egg](https://github.com/salmonloop/salmon-egg) [![GitHub stars](https://img.shields.io/github/stars/salmonloop/salmon-egg?style=flat)](https://github.com/salmonloop/salmon-egg/stargazers) - Desktop client for AI agents over the Agent Client Protocol, with session history, tool-call review and terminal workflows.

## Games

- [XAML-MAN](https://github.com/MartinZikmund/XamlMan) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/XamlMan?style=flat)](https://github.com/MartinZikmund/XamlMan/stargazers) - Faithful Pac-Man clone with arcade-accurate ghost AI, drawn entirely with XAML shapes and playable in the browser.
- [UnoDOOM](https://github.com/MartinZikmund/UnoDoom) [![GitHub stars](https://img.shields.io/github/stars/MartinZikmund/UnoDoom?style=flat)](https://github.com/MartinZikmund/UnoDoom/stargazers) - DOOM port built on ManagedDoom with touch, keyboard and gamepad controls, playable in the browser.
- [Astro Odyssey](https://github.com/asadullah-refat-89/astro-odyssey-uno-platform) [![GitHub stars](https://img.shields.io/github/stars/asadullah-refat-89/astro-odyssey-uno-platform?style=flat)](https://github.com/asadullah-refat-89/astro-odyssey-uno-platform/stargazers) - Browser space shooter where you destroy meteors and enemies and battle level bosses.

## Case Studies

- [Case Studies](https://platform.uno/case-studies/) - Official success stories from companies such as Toyota, Kahua, Air Canada, TradeZero and Microsoft.
- [Toyota Migrates Mobile App to Uno Platform](https://platform.uno/blog/toyota-migrates-mobile-app-to-uno-platform/) - How Toyota moved its North American plant line-of-business apps off Xamarin.Forms.
- [Windows Community Toolkit - How Microsoft Uses Uno Platform to Ship Fast](https://platform.uno/blog/windows-community-toolkit-how-microsoft-uses-uno-platform-to-ship-fast/) - Guest post by Michael Hawker on how the Windows Community Toolkit ships WinUI 2, WinUI 3 and WebAssembly from one codebase.
- [Sentry Chooses Uno Platform](https://platform.uno/blog/sentry-chooses-uno-platform-a-success-story/) - How Sentry built its open-source desktop crash reporter for Windows, macOS and Linux.

## Blogs

- [Official Uno Platform blog](https://platform.uno/blog/) - Lists latest release notes, tutorials, and articles by Uno Platform maintainers as well as external contributors.
- [Jerome Laban's blog](https://jaylee.org/) - Blog of the CTO of Uno Platform.
- [Martin Zikmund blog](https://mzikmund.dev/blog/categories/uno-platform) - Posts on WebAssembly, device APIs, sample apps and fun projects like DOOM, by Martin Zikmund.
- [Nick's .NET Travels](https://nicksnettravels.builttoroam.com/tag/uno/) - Uno Platform blog posts by Nick Randolph.
- [IObservable\<Opinion\>](https://ian.bebbs.co.uk/tags/uno-platform) - Uno Platform blog posts by Ian Bebbington.
- [InfoQ Uno Platform News](https://www.infoq.com/uno-platform/) - Independent release-by-release news coverage, mostly by Almir Vuk and Edin Kapić.
- [Steve Bilogan's Blog](https://kazo0.dev/) - Toolkit Tuesdays, Uno Tidbits and AI agent posts by Uno Toolkit maintainer Steve Bilogan.
- [lindexi's Blog (ZH)](https://www.cnblogs.com/lindexi/tag/UNO/) - Chinese posts on WPF migration, Linux desktop quirks (UOS, Kylin, X11) and framework internals by lindexi.

## Articles

- [WPF and Legacy App Migration Guides](https://platform.uno/blog/article_tags/migration/) - Official article series on migrating WPF and Xamarin.Forms apps, covering scoping, XAML mapping, triggers, resources, testing and incremental adoption.
- [How Uno Platform Uses .NET, MCP, and AI to Build High Quality Apps](https://devblogs.microsoft.com/dotnet/how-uno-platform-uses-dotnet-mcp-ai-to-build-high-quality-apps/) - Tour of the docs and app MCP servers, agent skills and Studio, by Sam Basu on the .NET Blog.

## Courses and Tutorials

- [Counter App Tutorial](https://platform.uno/docs/articles/getting-started/counterapp/get-started-counter.html) - Step-by-step first app in XAML or C# Markup with MVVM or MVUX, plus a Hot Design variant.
- [SimpleCalc Workshop](https://platform.uno/docs/articles/external/workshops/simple-calc/README.html) - Hands-on workshop building a calculator with XAML or C# Markup, MVVM or MVUX and runtime theme switching.
- [TubePlayer Workshop](https://platform.uno/docs/articles/external/workshops/tube-player/README.html) - Multi-module workshop building a YouTube search and playback app with C# Markup, MVUX, navigation and optional Figma import.
- [Uno Platform From Start to Finish](https://www.devforge.com/courses/uno-from-start-to-finish/) - Paid 66-lesson video course covering setup, MVUX, Uno Toolkit, Hot Design, Figma to code and MCPs. By Tim Corey.

## Live coding

- [Jerome Laban's Twitch](https://www.twitch.tv/jeromelaban) - Weekly Uno Platform live coding sessions (Tuesdays).
- [Martin Zikmund's Twitch](https://www.twitch.tv/martinzikmund) - Mostly Uno Platform-themed live coding sessions.
- [Martin Zikmund's Live Coding Archive](https://www.youtube.com/playlist?list=PLC0wF4Qw6SDNu61eMpdGCw-c5RR2Tk2R6) - Recorded streams porting WinUI APIs into the framework, plus walkthroughs on contributing to it.
- [Uno Platform Live Coding Archive](https://www.youtube.com/playlist?list=PLl_OlDcUya9pRqt9A0vpyi89Vl-uq3nSb) - Recordings of CTO Jérôme Laban's weekly streams debugging and building the framework.

## Talks

- [Introduction to open source Uno Platform](https://youtu.be/vRzTr8XYau0) - Introductory talk by Jérôme Laban about Uno Platform and what it offers.
- [Uno Platform - Your Apps Everywhere](https://youtu.be/dX69x-D6COI) - Overview of the Uno Platform ecosystem by Martin Zikmund at NDC Porto 2022.
- [Building Multi-Platform Applications with the Uno Platform](https://youtu.be/0zvzfCGO0gI) - Introduction to creating apps for multiple platforms and form factors, all while reusing your existing XAML and C# skills by Nick Randolph.
- [Разработка кросс-платформенных приложений с Uno Platform и Elmish-подходом на F# (RU)](https://www.youtube.com/watch?v=ApNGATu9RSo) - Introduction to Uno, Blend and Elmish.
- [Uno Platform - Your Apps Everywhere (NDC London 2023)](https://www.youtube.com/watch?v=BTgp9VyZSs8) - Overview of the ecosystem by Martin Zikmund at NDC London 2023.
- [How We Build an Open-Source Cross-Platform Framework in .NET](https://www.youtube.com/watch?v=ns9EiKLlxsQ) - Engineering behind the framework, from source generators and the custom MSBuild SDK to CI and C++ porting, by Martin Zikmund at Monkey Conf 2024.
- [UnoConf](https://www.youtube.com/playlist?list=PLl_OlDcUya9rp-ZbLkFHWtp2-9V-xGYFu) - Recordings from the 2019 to 2021 developer conferences, including Miguel de Icaza's keynote and sessions on Extensions, styling, testing and WPF migration.
- [Announcing Uno Platform Studio and Hot Design](https://www.youtube.com/watch?v=sJPyieyt1Rc) - Launch of Studio and the Hot Design runtime visual designer, by Jérôme Laban and Nick Randolph at .NET Conf 2024.
- [Uno Platform. Now with AI](https://www.youtube.com/watch?v=g4A_3ZCwwWg) - Generating full-stack apps with AI on top of Hot Design, by Jérôme Laban at .NET Conf 2025.
- [Best Practices for Cross-Platform .NET 8 Applications](https://www.youtube.com/watch?v=yVYhZsu7gso) - Bootstrapping a well-architected app with Extensions for navigation and localization and the MVUX reactive pattern, at .NET Conf 2023.
- [Build Modern .NET Apps with Uno Platform, AI, and Visual Tools](https://www.youtube.com/watch?v=t_cKjNtB2aU) - Hot Design, AI agents grounded by the docs and app MCP servers, and SkiaSharp rendering, by Sam Basu at Microsoft Build 2026.
- [Write Uno Time, Run Everywhere with the Uno Platform](https://www.youtube.com/watch?v=vyR38vxo4ug) - Getting started from machine setup to a contacts app backed by an existing REST API, by Joseph Guadagno at NDC London 2025.
- [Let's Build a .NET YouTube Player! For Which Platform? All of Them!](https://www.youtube.com/watch?v=Vfzdr0TRYCs) - Building a YouTube player from its original Figma designs with Toolkit and Material, by Steve Bilogan at Copenhagen Developers Festival 2024.
- [Figma Meets .NET Developers](https://www.youtube.com/watch?v=lxo5TTK1Bfw) - Smoothing the designer-developer handoff by exporting Figma designs straight into the app, by Nick Randolph at NDC Sydney 2024.
- [.NET Apps Everywhere](https://www.youtube.com/watch?v=inD_3SD0G80) - Under-the-hood tour of how a single codebase renders on every platform, by Steve Bilogan at JetBrains .NET Days Online 2025.
- [Build Beautiful .NET Apps Faster with Uno Platform](https://www.youtube.com/watch?v=u8Fkb7pjqwQ) - Building cross-platform apps in C# with full UI control, device APIs, Hot Reload and Figma integration, by Martin Zikmund at the BASTA! conference.
- [Design, Build and Publish Cross-Platform .NET Applications with Uno Platform](https://www.youtube.com/watch?v=gUubBX9xhdA) - Workshop from project creation to publishing, covering the Figma plugin, Hot Reload and Hot Design, by Nick Randolph at Indy .NET Consortium 2025.
- [Migrating WPF Apps to Web](https://www.youtube.com/watch?v=doomI2bEBno) - Architecture and implementation considerations for moving WPF apps to the web, by Daren May at UnoConf 2021.
- [Martin Zikmund's Talks](https://www.youtube.com/playlist?list=PLC0wF4Qw6SDMCHrbo9PlNC4OrJ_rV5i1U) - Recordings of Martin Zikmund's Uno talks at NDC, Visual Studio Toolbox, .NET Oxford and other events.
- [Building Linux Desktop Apps with .NET and Uno Platform](https://www.youtube.com/watch?v=OxyJYF2HgBM) - James Montemagno and Jérôme Laban build, debug and deploy Linux desktop apps from VS Code on Ubuntu.
- [Uno Platform - Now With AI! (Visual Studio Toolbox)](https://www.youtube.com/watch?v=xGJ0U_E9LC8) - Sam Basu and Jérôme Laban demo MCP-driven development, Hot Design and the Hot Design agent on Visual Studio Toolbox.

## Videos

- [Uno Platform's YouTube](https://www.youtube.com/@unoplatform) - Official YouTube channel of Uno Platform, includes new release highlights, live sessions, and tutorials.
- [Uno Tech Bites](https://www.youtube.com/playlist?list=PLl_OlDcUya9rP_fDcFrHWV3DuP7KhQKRA) - Uno Platform development learnings in bite-sized lessons.
- [Martin Zikmund's YouTube](https://www.youtube.com/@mzikmund) - Various Uno Platform-related videos and tutorials.
- [Definitive Guide to Uno Platform Contributions](https://www.youtube.com/watch?v=GIboa7CZXaw) - Two-hour walkthrough of setting up, building, debugging and contributing to the framework repository by Martin Zikmund.
- [Get Started with AI-Assisted Development](https://www.youtube.com/playlist?list=PLl_OlDcUya9rizyD8smQFO45G1Q-meutb) - Official series on agent-driven development with Claude Code, Copilot CLI, Codex, Cursor, Antigravity, MCPs and Studio.
- [Intro to Uno Platform - Full Cross-Platform C# Development](https://www.youtube.com/watch?v=Cm2FRfiAzSU) - In-depth introduction to building and deploying a single-project cross-platform app, by Tim Corey.
- [Uno Platform Webinars](https://www.youtube.com/playlist?list=PLl_OlDcUya9qeKZEF3HCFdqXuys0-RwIp) - Release webinars, product launch streams and AMA sessions from the core team.
- [VectoArt's Uno Platform Tutorials](https://www.youtube.com/playlist?list=PLqT49gV-eqe6t-sdQpW0BaJIpo8Zxuiwz) - Community tutorials on Figma-to-XAML apps, animations and the Hot Design agent, by VectoArt.

## Podcasts

- [The Modern .NET Show: One UI to Rule Them All](https://dotnetcore.show/season-6/s06e18-uno-platform-one-ui-to-rule-them-all-with-martin-zikmund/) - Martin Zikmund on WinUI everywhere, Linux support and designer-developer tooling, with Jamie Taylor in 2024.
- [.NET Rocks! 1984: Uno and .NET 10 with Sam Basu and Jérôme Laban](https://www.dotnetrocks.com/details/1984) - Jérôme Laban and Sam Basu on .NET 10, the MAUI collaboration, WebAssembly and MCP-based AI tooling.
- [.NET Rocks! 1938: Uno Hot Design with Francois Tanguay and Sasha Krsmanovic](https://www.dotnetrocks.com/details/1938) - Co-founders Francois Tanguay and Sasha Krsmanovic on Hot Design and how the framework has evolved.
- [.NET Rocks! 1882: Uno Platform Update with Nick Randolph](https://www.dotnetrocks.com/details/1882) - Nick Randolph on the Figma plugin, design-to-code workflow and CI integration.
- [.NET Rocks! 1552: Open Sourcing Uno with Francois Tanguay and Jérôme Laban](https://www.dotnetrocks.com/details/1552) - Francois Tanguay and Jérôme Laban on open-sourcing the UWP-based framework in 2018.
- [Hanselminutes 820: Multi-Platform Apps with Uno Platform's Jérôme Laban](https://hanselminutes.com/820/multi-platform-apps-with-uno-platforms-jrme-laban) - Jérôme Laban on the importance and flexibility of write-once-run-everywhere, with Scott Hanselman.
- [Software Engineering Radio 508: Jérôme Laban on Cross-Platform UI](https://se-radio.net/2022/04/episode-508-jerome-laban-on-cross-platform-ui/) - Jérôme Laban on native fidelity versus consistent design, rendering approaches and platform differences in cross-platform UI.
- [The Unhandled Exception Podcast 74: The Uno Platform and Hot Design with Jérôme Laban](https://unhandledexceptionpodcast.com/posts/0074-unoplatformandhotdesign/) - Jérôme Laban on the framework and its Hot Design visual designer, with Dan Clarke.
- [Betatalks the Podcast 92: The Uno Platform: Unlocking Cross-Platform Potential with Martin Zikmund](https://www.buzzsprout.com/1622272/episodes/15826598-92-the-uno-platform-unlocking-cross-platform-potential-with-martin-zikmund) - Martin Zikmund on cross-platform development, contributing to the framework and how it compares with alternatives.
- [Blue Blazes S04E01: Uno Platform featuring Sam Basu](https://www.youtube.com/watch?v=rqm_54Y8h8U) - Sam Basu on native and Skia rendering paths and how the framework compares with MAUI, React Native and Flutter, with Jonathan Tower.

## Books

- [Getting Started with the Uno Platform and WinUI 3 (2022/09)](https://link.springer.com/book/10.1007/978-1-4842-8248-9) - Hands-on building of cross-platform desktop, mobile, and web applications that can run anywhere. By Skye Hoefling.
- [Creating Cross-Platform C# Applications with Uno Platform (2021/08)](https://www.packtpub.com/en-us/product/creating-cross-platform-c-applications-with-uno-platform-9781801078498) - Build apps with C# and XAML that run on Windows, macOS, iOS, Android, and WebAssembly. By Matt Lacey and Marcel Alexander Wagner.
- [Uno Platform Succinctly](https://www.syncfusion.com/succinctly-free-ebooks/uno-platform-succinctly) - Free introductory ebook by Ed Freitas, published by Syncfusion.
## Contributing

Your contributions are welcome! Please read the [contribution guidelines](contributing.md) before creating a pull request.
