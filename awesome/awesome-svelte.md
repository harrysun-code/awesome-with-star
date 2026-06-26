# Svelte

[![GitHub stars](https://img.shields.io/github/stars/TheComputerM/awesome-svelte?style=flat)](https://github.com/TheComputerM/awesome-svelte/stargazers)

<p align="center">
  <br>
  <img width="200" src="./awesome-svelte.svg" alt="awesome-svelte logo">
  <br>
  <br>
</p>

# Awesome Svelte [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> ⚡ A curated list of awesome Svelte resources

[Svelte](https://svelte.dev/) is a new way to build web applications. It's a compiler that takes your declarative components and converts them into efficient JavaScript

Contributions welcome. Add links through pull requests or create an issue to start a discussion.

## Contents

- [Awesome Svelte](#awesome-svelte-)
  - [Contents](#contents)
  - [Resources](#resources)
    - [Official Resources](#official-resources)
    - [Community](#community)
    - [Conferences](#conferences)
    - [Podcasts](#podcasts)
    - [YouTube Channels](#youtube-channels)
    - [Tutorials](#tutorials)
    - [Studies](#studies)
  - [Integrations](#integrations)
    - [Preprocessing](#preprocessing)
    - [Mobile](#mobile)
  - [State Libraries](#state-libraries)
  - [UI Libraries](#ui-libraries)
  - [UI Components](#ui-components)
    - [Table](#table)
    - [Notification](#notification)
    - [Grid](#grid)
    - [Icons](#icons)
    - [Calendar](#calendar)
    - [Maps](#maps)
    - [Charts](#charts)
    - [Miscellaneous](#miscellaneous)
  - [Scaffold](#scaffold)
  - [Utilities](#utilities)
    - [Animations](#animations)
    - [Drag \& Drop](#drag--drop)
    - [Forms](#forms)
      - [Form Components](#form-components)
    - [HTTP Requests](#http-requests)
    - [Sound \& Video](#sound--video)
    - [WebGL](#webgl)
    - [PWA](#pwa)
    - [Portal](#portal)
    - [Fonts](#fonts)
    - [Internationalization](#internationalization)
  - [Routers](#routers)
  - [Frameworks](#frameworks)
  - [Dev Tools](#dev-tools)
    - [Lint](#lint)
    - [Test](#test)
    - [Editors](#editors)
      - [Visual Studio Code](#visual-studio-code)
      - [Sublime Text](#sublime-text)
      - [Vim](#vim)
      - [JetBrains](#jetbrains)
  - [Application Examples](#application-examples)
    - [Desktop](#desktop)

## Resources

### Official Resources

- [Official Guide](https://svelte.dev/tutorial)
- [API Reference](https://svelte.dev/docs)
- [GitHub Repo](https://github.com/sveltejs/svelte) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/svelte?style=flat)](https://github.com/sveltejs/svelte/stargazers)
- [Changelog](https://github.com/sveltejs/svelte/blob/master/packages/svelte/CHANGELOG.md) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/svelte/blob/master/packages/svelte/CHANGELOG.md?style=flat)](https://github.com/sveltejs/svelte/blob/master/packages/svelte/CHANGELOG.md/stargazers)

### Community

- ~~[Twitter](https://twitter.com/sveltejs)~~
- [Bluesky](https://bsky.app/profile/svelte.dev)
- [Discord](https://svelte.dev/chat)
- [Reddit](https://www.reddit.com/r/sveltejs/)
- [Japan Discord](https://discord.com/invite/YTXq3ZtBbx) - Svelte 日本.

### Conferences

- [Svelte Summit](https://sveltesummit.com/)

### Podcasts

- [Svelte Radio](https://www.svelteradio.com/)

### YouTube Channels

- [Svelte Society](https://www.youtube.com/channel/UCZSr5B0l07JXK2FIeWA0-jw)
- [Svelte Mastery](https://www.youtube.com/channel/UCg6SQd5jnWo5Y70rZD9SQFA)
- [Joy of Code](https://www.youtube.com/@JoyofCodeDev)

### Tutorials

- [Getting Started with Svelte 5: A Guide for React Developers](https://www.edistys.dev/blog/getting-started-with-svelte-5-a-guide-for-react-developers) - Edistys
- [Svelte 5 Basics - Complete Svelte 5 Course for Beginners](https://www.youtube.com/watch?v=8DQailPy3q8) - Syntax (YouTube)
- [TutorialSearch](https://tutorialsearch.io/?q=svelte) - Free cross-platform search engine indexing 50,000+ tutorials from Udemy, Skillshare, Pluralsight, and other major learning platforms across 45+ categories.

### Studies

_Studies and research on the Svelte framework._

- [SvelteScaling](https://svelte-scaling.acmion.com/) - Does Svelte Scale? _(pre-v5)_
- [Will it Scale?](https://github.com/halfnelson/svelte-it-will-scale) [![GitHub stars](https://img.shields.io/github/stars/halfnelson/svelte-it-will-scale?style=flat)](https://github.com/halfnelson/svelte-it-will-scale/stargazers) - Finding Svelte's inflection point. _(pre-v5)_

## Integrations

### Preprocessing

- [svelte-preprocess](https://github.com/sveltejs/svelte-preprocess) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/svelte-preprocess?style=flat)](https://github.com/sveltejs/svelte-preprocess/stargazers) - A preprocessor for PostCSS, SCSS, Less, Stylus, Coffeescript, TypeScript, Pug and much more.
- [MDSveX](https://github.com/pngwn/MDsveX) [![GitHub stars](https://img.shields.io/github/stars/pngwn/MDsveX?style=flat)](https://github.com/pngwn/MDsveX/stargazers) - Preprocessor for MDX markdown.
- [svelte-switch-case](https://github.com/l-portet/svelte-switch-case) [![GitHub stars](https://img.shields.io/github/stars/l-portet/svelte-switch-case?style=flat)](https://github.com/l-portet/svelte-switch-case/stargazers) - Switch case syntax for Svelte.
- [svelte-preprocess-less](https://github.com/ls-age/svelte-preprocess-less) [![GitHub stars](https://img.shields.io/github/stars/ls-age/svelte-preprocess-less?style=flat)](https://github.com/ls-age/svelte-preprocess-less/stargazers) - Preprocessor for less.
- [modular-css](https://github.com/tivac/modular-css/tree/main/packages/svelte) [![GitHub stars](https://img.shields.io/github/stars/tivac/modular-css/tree/main/packages/svelte?style=flat)](https://github.com/tivac/modular-css/tree/main/packages/svelte/stargazers) - Preprocessor support for modular-css.
- [svelte-preprocess-sass](https://github.com/ls-age/svelte-preprocess-sass) [![GitHub stars](https://img.shields.io/github/stars/ls-age/svelte-preprocess-sass?style=flat)](https://github.com/ls-age/svelte-preprocess-sass/stargazers) - Preprocessor for sass.
- [svelte-preprocess-markdown](https://github.com/AlexxNB/svelte-preprocess-markdown) [![GitHub stars](https://img.shields.io/github/stars/AlexxNB/svelte-preprocess-markdown?style=flat)](https://github.com/AlexxNB/svelte-preprocess-markdown/stargazers) - Write Svelte components in markdown syntax.
- [@nvl/sveltex](https://github.com/nvlang/sveltex) [![GitHub stars](https://img.shields.io/github/stars/nvlang/sveltex?style=flat)](https://github.com/nvlang/sveltex/stargazers) - Svelte + Markdown + LaTeX.

### Mobile

_UI frameworks for mobile._

- [Svelte Native](https://svelte-native.technology/) - Svelte controlling native components via Nativescript.
- [Framework7](https://framework7.io/svelte/) - Full featured HTML framework for building iOS & Android apps.
- [Capacitor](https://capacitorjs.com/solution/svelte) - Build native mobile apps with web technology and Svelte.

## State Libraries

- [svelte-asyncable](https://github.com/sveltetools/svelte-asyncable) [![GitHub stars](https://img.shields.io/github/stars/sveltetools/svelte-asyncable?style=flat)](https://github.com/sveltetools/svelte-asyncable/stargazers) - The Svelte store contract with support for asynchronous values.
- [exome](https://github.com/Marcisbee/exome) [![GitHub stars](https://img.shields.io/github/stars/Marcisbee/exome?style=flat)](https://github.com/Marcisbee/exome/stargazers) - Simple proxy based state manager for deeply nested states.
- [tanstack-store](https://tanstack.com/store/latest/docs/framework/svelte/quick-start) - Framework agnostic type-safe store w/ reactive framework adapters.
-

## UI Libraries

- [lomer-ui](https://ui.lomer.dev) - A dead-simple CLI tool to instantly kickstart your components.
- [shadcn-svelte](https://www.shadcn-svelte.com/) - Beautifully designed components that you can copy and paste into your apps.
- [SvelteUI](https://svelteui.dev/) - all inclusive Svelte library - Components, Actions, Utilities, Animations.
- [Flowbite Svelte](https://flowbite-svelte.com/) - Open-source Svelte UI components built with Tailwind CSS and Flowbite.
- [Skeleton](https://www.skeleton.dev/docs/get-started) - Skeleton uses Tailwind utility classes and design system to easily create theme-able user interfaces.
- [Sveltestrap](https://github.com/sveltestrap/sveltestrap) [![GitHub stars](https://img.shields.io/github/stars/sveltestrap/sveltestrap?style=flat)](https://github.com/sveltestrap/sveltestrap/stargazers) - Bootstrap 4 & 5 components.
- [carbon-components-svelte](https://github.com/IBM/carbon-components-svelte) [![GitHub stars](https://img.shields.io/github/stars/IBM/carbon-components-svelte?style=flat)](https://github.com/IBM/carbon-components-svelte/stargazers) - Svelte implementation of the IBM Carbon Design System.
- [Svelte Material UI](https://github.com/hperrin/svelte-material-ui) [![GitHub stars](https://img.shields.io/github/stars/hperrin/svelte-material-ui?style=flat)](https://github.com/hperrin/svelte-material-ui/stargazers) - Material UI Components.
- [Melt UI](https://github.com/melt-ui/melt-ui) [![GitHub stars](https://img.shields.io/github/stars/melt-ui/melt-ui?style=flat)](https://github.com/melt-ui/melt-ui/stargazers) - A collection of accessible, reusable, and composable headless component builders and utilities.
- [attractions](https://github.com/illright/attractions) [![GitHub stars](https://img.shields.io/github/stars/illright/attractions?style=flat)](https://github.com/illright/attractions/stargazers) - A pretty cool and modern UI kit. _(pre-v5)_
- [ionic-svelte](https://github.com/Tommertom/svelte-ionic-app) [![GitHub stars](https://img.shields.io/github/stars/Tommertom/svelte-ionic-app?style=flat)](https://github.com/Tommertom/svelte-ionic-app/stargazers) - Svelte integration with Ionic's UI for mobile app development, including many starters.
- [YeSvelte](https://www.yesvelte.com/) - YeSvelte is flexible Svelte UI component library built on top of Bootstrap css.
- [Svelte UX](https://github.com/techniq/svelte-ux) [![GitHub stars](https://img.shields.io/github/stars/techniq/svelte-ux?style=flat)](https://github.com/techniq/svelte-ux/stargazers) - Large collection of components, actions, stores, and utilities to build highly interactive applications
- [STDF](https://stdf.design) - Mobile web component library based on Svelte and Tailwind.
- [M3 Svelte](https://github.com/KTibow/m3-svelte) [![GitHub stars](https://img.shields.io/github/stars/KTibow/m3-svelte?style=flat)](https://github.com/KTibow/m3-svelte/stargazers) - Robust component library implementing Material Design 3
- [AgnosUI](https://amadeusitgroup.github.io/AgnosUI/latest/) - Highly configurable headless framework agnostic component library
- [daisyUI](https://daisyui.com/) - The most popular component library for Tailwind CSS - `daisyUI` adds component class names to Tailwind CSS so you can make beautiful websites faster than ever.
- [Smelte](https://github.com/matyunya/smelte) [![GitHub stars](https://img.shields.io/github/stars/matyunya/smelte?style=flat)](https://github.com/matyunya/smelte/stargazers) - UI framework with material components built with Tailwind CSS. _(pre-v5)_
- [SVAR Core for Svelte](https://github.com/svar-widgets/core) [![GitHub stars](https://img.shields.io/github/stars/svar-widgets/core?style=flat)](https://github.com/svar-widgets/core/stargazers) - A collection of 20+ Svelte UI components for building fast-performing, interactive and responsive web apps.
- [AgnosticUI](https://github.com/agnosticui/agnosticui) [![GitHub stars](https://img.shields.io/github/stars/agnosticui/agnosticui?style=flat)](https://github.com/agnosticui/agnosticui/stargazers) - Accessible Svelte Component Primitives (that also work with React, Vue 3, and Angular).
- [Svelte Animations](https://animation-svelte.vercel.app) - Consist of Svelte Magic UI, Svelte Aceternity UI, Svelte Luxe Components over 200+ Free Animation Components & 2 Templates
- [Svelte Marketing Blocks](https://sv-blocks.vercel.app) - A powerful library of 100+ marketing and UI blocks built using Shadcn Svelte, Tailwind CSS v4, and Svelte 5.
- [Quaff](https://quaff.dev) - An extensive UI framework featuring modern and elegant components following Material Design 3 principles.
- [retroui-svelte](https://retroui-svelte.netlify.app) - A retro-styled component library for Svelte built on top of shadcn-svelte, offering 40+ customizable UI components for funky and playful interfaces.
- [svelte-audio-ui](https://svelte-audio-ui.vercel.app) - A set of accessible and composable Audio UI components. Built on top of shadcn-svelte, inspired by audio-ui, it's designed for you to copy, paste, and own.
- [AgentsKit](https://github.com/AgentsKit-io/agentskit) [![GitHub stars](https://img.shields.io/github/stars/AgentsKit-io/agentskit?style=flat)](https://github.com/AgentsKit-io/agentskit/stargazers) - Headless chat and agent components plus a store for building AI apps in Svelte, with a framework-agnostic core supporting streaming, tools, memory and RAG.

## UI Components

### Table

_Tables and data grids._

- [@vincjo/datatables](https://github.com/vincjo/datatables) [![GitHub stars](https://img.shields.io/github/stars/vincjo/datatables?style=flat)](https://github.com/vincjo/datatables/stargazers) - A toolkit for creating datatable components with Svelte.
- [svelte-table](https://github.com/dasDaniel/svelte-table) [![GitHub stars](https://img.shields.io/github/stars/dasDaniel/svelte-table?style=flat)](https://github.com/dasDaniel/svelte-table/stargazers) - A table implementation that allows sorting and filtering.
- [svelte-generic-crud-table](https://github.com/ivosdc/svelte-generic-crud-table) [![GitHub stars](https://img.shields.io/github/stars/ivosdc/svelte-generic-crud-table?style=flat)](https://github.com/ivosdc/svelte-generic-crud-table/stargazers) - Agnostic web-component for object-arrays with CRUD functionality. Sort and resize columns. Multiple tables per page.
- [svelte-generic-table-pager](https://github.com/ivosdc/svelte-generic-table-pager) [![GitHub stars](https://img.shields.io/github/stars/ivosdc/svelte-generic-table-pager?style=flat)](https://github.com/ivosdc/svelte-generic-table-pager/stargazers) - Svelte-generic-crud-table with paginator.
- [powertable](https://github.com/muonw/powertable) [![GitHub stars](https://img.shields.io/github/stars/muonw/powertable?style=flat)](https://github.com/muonw/powertable/stargazers) - PowerTable is a JavaScript component that turns JSON data into an interactive HTML table. This facilitates manual inspection, sorting, filtering, searching, and editing of the data.
- [svelte-pivottable](https://github.com/jjagielka/svelte-pivottable) [![GitHub stars](https://img.shields.io/github/stars/jjagielka/svelte-pivottable?style=flat)](https://github.com/jjagielka/svelte-pivottable/stargazers) - Svelte-based pivot table library with drag'n'drop functionality.
- [SVAR DataGrid](https://github.com/svar-widgets/grid) [![GitHub stars](https://img.shields.io/github/stars/svar-widgets/grid?style=flat)](https://github.com/svar-widgets/grid/stargazers) - A Svelte datagrid with in-cell editing, sorting, context menu, collapsible and frozen columns, tree data view, paging and virtual scrolling.
- [svelte-datagrid](https://github.com/revolist/svelte-datagrid) [![GitHub stars](https://img.shields.io/github/stars/revolist/svelte-datagrid?style=flat)](https://github.com/revolist/svelte-datagrid/stargazers) - Powerful data grid library based on [revogrid](https://rv-grid.com) with best features from Excel.
- [@wjfe/dataview](https://github.com/WJSoftware/wjfe-dataview) [![GitHub stars](https://img.shields.io/github/stars/WJSoftware/wjfe-dataview?style=flat)](https://github.com/WJSoftware/wjfe-dataview/stargazers) - Table for data visualization purposes with advanced features like column pinning, and the only component in the world that does cross-table column position synchronization for master-child scenarios.

### Notification

_Toaster / snackbar - Notify the user with a modeless temporary little popup._

- [svelte-notifications](https://github.com/beyonk-adventures/svelte-notifications) [![GitHub stars](https://img.shields.io/github/stars/beyonk-adventures/svelte-notifications?style=flat)](https://github.com/beyonk-adventures/svelte-notifications/stargazers) - Toast notifications component that can be used in any JS application.
- [svelte-favicon-badge](https://github.com/kevmodrome/svelte-favicon-badge) [![GitHub stars](https://img.shields.io/github/stars/kevmodrome/svelte-favicon-badge?style=flat)](https://github.com/kevmodrome/svelte-favicon-badge/stargazers) - A custom component that adds a favicon and a badge that you can use to show for example number of unread messages, etc.
- [@zerodevx/svelte-toast](https://github.com/zerodevx/svelte-toast) [![GitHub stars](https://img.shields.io/github/stars/zerodevx/svelte-toast?style=flat)](https://github.com/zerodevx/svelte-toast/stargazers) - Simple elegant toast notifications.
- [svelte-french-toast](https://github.com/kbrgl/svelte-french-toast) [![GitHub stars](https://img.shields.io/github/stars/kbrgl/svelte-french-toast?style=flat)](https://github.com/kbrgl/svelte-french-toast/stargazers) - Buttery smooth toast notifications for Svelte, inspired by React Hot Toast. Lightweight, customizable, and beautiful by default.
- [svelte-sonner](https://github.com/wobsoriano/svelte-sonner) [![GitHub stars](https://img.shields.io/github/stars/wobsoriano/svelte-sonner?style=flat)](https://github.com/wobsoriano/svelte-sonner/stargazers) - An opinionated toast component for Svelte.

### Grid

- [svelte-grid-responsive](https://github.com/andrelmlins/svelte-grid-responsive) [![GitHub stars](https://img.shields.io/github/stars/andrelmlins/svelte-grid-responsive?style=flat)](https://github.com/andrelmlins/svelte-grid-responsive/stargazers) - Bootstrap-inspired responsive grid system.
- [svelte-flex](https://github.com/himynameisdave/svelte-flex) [![GitHub stars](https://img.shields.io/github/stars/himynameisdave/svelte-flex?style=flat)](https://github.com/himynameisdave/svelte-flex/stargazers) - A simple and reusable flexbox component for Svelte.

### Icons

- [unplugin-icons](https://github.com/unplugin/unplugin-icons) [![GitHub stars](https://img.shields.io/github/stars/unplugin/unplugin-icons?style=flat)](https://github.com/unplugin/unplugin-icons/stargazers) - Access thousands of icons as components on-demand universally.
- [svelte-fa](https://github.com/Cweili/svelte-fa) [![GitHub stars](https://img.shields.io/github/stars/Cweili/svelte-fa?style=flat)](https://github.com/Cweili/svelte-fa/stargazers) - Tiny FontAwesome 5 and 6 component.
- [svelte-awesome](https://github.com/RobBrazier/svelte-awesome) [![GitHub stars](https://img.shields.io/github/stars/RobBrazier/svelte-awesome?style=flat)](https://github.com/RobBrazier/svelte-awesome/stargazers) - Awesome SVG icon component, built with Font Awesome icons.
- [steeze-ui/icons](https://github.com/steeze-ui/icons) [![GitHub stars](https://img.shields.io/github/stars/steeze-ui/icons?style=flat)](https://github.com/steeze-ui/icons/stargazers) - Effortless Icon Packs & Components for Svelte, React, Vue and more.
- [svelte-icons](https://github.com/AnxiousDarkly/svelte-icons) [![GitHub stars](https://img.shields.io/github/stars/AnxiousDarkly/svelte-icons?style=flat)](https://github.com/AnxiousDarkly/svelte-icons/stargazers) - Icon components.
- [svelte-heroicons](https://github.com/krowten/svelte-heroicons) [![GitHub stars](https://img.shields.io/github/stars/krowten/svelte-heroicons?style=flat)](https://github.com/krowten/svelte-heroicons/stargazers) - Icons, crafted by the creators of Tailwind CSS.
- [svelte-icomoon](https://github.com/aykutkardas/svelte-icomoon) [![GitHub stars](https://img.shields.io/github/stars/aykutkardas/svelte-icomoon?style=flat)](https://github.com/aykutkardas/svelte-icomoon/stargazers) - It makes it very simple to use SVG icons in your Svelte projects.
- [svelte-unicons](https://github.com/devShamim/svelte-unicons) [![GitHub stars](https://img.shields.io/github/stars/devShamim/svelte-unicons?style=flat)](https://github.com/devShamim/svelte-unicons/stargazers) - Unicons svg icons for Svelte based on @iconscout/unicons.
- [@thesvg/svelte](https://github.com/glincker/thesvg) [![GitHub stars](https://img.shields.io/github/stars/glincker/thesvg?style=flat)](https://github.com/glincker/thesvg/stargazers) - 5,600+ SVG brand and cloud icon components for Svelte. AWS, Azure, GCP, and 4,000+ brand logos.
- [lucide-svelte](https://github.com/lucide-icons/lucide) [![GitHub stars](https://img.shields.io/github/stars/lucide-icons/lucide?style=flat)](https://github.com/lucide-icons/lucide/stargazers) - Implementation of the lucide icon library for svelte applications.
- [svelte-icons-pack](https://github.com/leshak/svelte-icons-pack) [![GitHub stars](https://img.shields.io/github/stars/leshak/svelte-icons-pack?style=flat)](https://github.com/leshak/svelte-icons-pack/stargazers) - Based on <https://github.com/react-icons/react-icons>.
- [svesome](https://github.com/pouchlabs/svesome) [![GitHub stars](https://img.shields.io/github/stars/pouchlabs/svesome?style=flat)](https://github.com/pouchlabs/svesome/stargazers) - A fontawesome v6 icons wrapper for svelte its awesome.
- [hugeicons](https://github.com/hugeicons/svelte) [![GitHub stars](https://img.shields.io/github/stars/hugeicons/svelte?style=flat)](https://github.com/hugeicons/svelte/stargazers) - Beautiful, production-ready icon package for Svelte with complete icon coverage.
- [moving icons](https://github.com/jis3r/icons) [![GitHub stars](https://img.shields.io/github/stars/jis3r/icons?style=flat)](https://github.com/jis3r/icons/stargazers) - A collection of beautifully crafted, animated Lucide icons.

### Calendar

_Display non-editable events in a calendar._

- [svelte-fullcalendar](https://github.com/YogliB/svelte-fullcalendar) [![GitHub stars](https://img.shields.io/github/stars/YogliB/svelte-fullcalendar?style=flat)](https://github.com/YogliB/svelte-fullcalendar/stargazers) - A component wrapper around FullCalendar.
- [svelte-calendar](https://github.com/6eDesign/svelte-calendar) [![GitHub stars](https://img.shields.io/github/stars/6eDesign/svelte-calendar?style=flat)](https://github.com/6eDesign/svelte-calendar/stargazers) - A lightweight datepicker with neat animations and a unique UX.
- [date-picker-svelte](https://github.com/probablykasper/date-picker-svelte) [![GitHub stars](https://img.shields.io/github/stars/probablykasper/date-picker-svelte?style=flat)](https://github.com/probablykasper/date-picker-svelte/stargazers) - A date and time picker for Svelte with clean UX.
- [@schedule-x/svelte](https://github.com/schedule-x/schedule-x) [![GitHub stars](https://img.shields.io/github/stars/schedule-x/schedule-x?style=flat)](https://github.com/schedule-x/schedule-x/stargazers) - A material design event calendar library.

### Maps

- [svelte-googlemaps](https://github.com/beyonk-adventures/svelte-googlemaps) [![GitHub stars](https://img.shields.io/github/stars/beyonk-adventures/svelte-googlemaps?style=flat)](https://github.com/beyonk-adventures/svelte-googlemaps/stargazers) - Google Maps component.
- [svelte-mapbox](https://github.com/beyonk-adventures/svelte-mapbox) [![GitHub stars](https://img.shields.io/github/stars/beyonk-adventures/svelte-mapbox?style=flat)](https://github.com/beyonk-adventures/svelte-mapbox/stargazers) - MapBox map and autocomplete components.
- [leaflet-svelte](https://github.com/anoram/leaflet-svelte) [![GitHub stars](https://img.shields.io/github/stars/anoram/leaflet-svelte?style=flat)](https://github.com/anoram/leaflet-svelte/stargazers) - Svelte wrapper for Leaflet.
- [esri-svelte](https://github.com/gavinr-maps/esri-svelte-example) [![GitHub stars](https://img.shields.io/github/stars/gavinr-maps/esri-svelte-example?style=flat)](https://github.com/gavinr-maps/esri-svelte-example/stargazers) - Web application that shows how to use the ArcGIS API for JavaScript with Svelte.
- [svelte-maplibre](https://github.com/dimfeld/svelte-maplibre) [![GitHub stars](https://img.shields.io/github/stars/dimfeld/svelte-maplibre?style=flat)](https://github.com/dimfeld/svelte-maplibre/stargazers) - Svelte bindings for the MapLibre mapping library.

### Charts

- [svelte-frappe-charts](https://github.com/himynameisdave/svelte-frappe-charts) [![GitHub stars](https://img.shields.io/github/stars/himynameisdave/svelte-frappe-charts?style=flat)](https://github.com/himynameisdave/svelte-frappe-charts/stargazers) - Svelte bindings for frappe-charts.
- [Layer Cake](https://github.com/mhkeller/layercake) [![GitHub stars](https://img.shields.io/github/stars/mhkeller/layercake?style=flat)](https://github.com/mhkeller/layercake/stargazers) - A framework for mostly-reusable graphics with svelte
- [LayerChart](https://github.com/techniq/layerchart) [![GitHub stars](https://img.shields.io/github/stars/techniq/layerchart?style=flat)](https://github.com/techniq/layerchart/stargazers) - Large collection of composable Svelte components to build a wide range of visualizations, built upon Layer Cake
- [SVAR Gantt Chart](https://github.com/svar-widgets/gantt) [![GitHub stars](https://img.shields.io/github/stars/svar-widgets/gantt?style=flat)](https://github.com/svar-widgets/gantt/stargazers) - An interactive, customizable Gantt chart component written in Svelte

### Graphs

- [svelte-flow](https://svelteflow.dev) - A customizable Svelte component for building node-based editors and interactive diagrams by the creators of React Flow

### Miscellaneous

- [number-flow](https://github.com/barvian/number-flow) [![GitHub stars](https://img.shields.io/github/stars/barvian/number-flow?style=flat)](https://github.com/barvian/number-flow/stargazers) - A component to transition, format, and localize numbers.
- [Svelte Tweakpane UI](https://kitschpatrol.com/svelte-tweakpane-ui) - UI elements from [Tweakpane](https://tweakpane.github.io/docs/) wrapped in a collection of idiomatic Svelte components.
- [svelte-tree-viewer](https://github.com/kpulkit29/svelte-tree-viewer) [![GitHub stars](https://img.shields.io/github/stars/kpulkit29/svelte-tree-viewer?style=flat)](https://github.com/kpulkit29/svelte-tree-viewer/stargazers) - A lightweight component to render tree views.
- [svelte-copyright](https://github.com/himynameisdave/svelte-copyright) [![GitHub stars](https://img.shields.io/github/stars/himynameisdave/svelte-copyright?style=flat)](https://github.com/himynameisdave/svelte-copyright/stargazers) - A Svelte component to format and display a copyright notice.
- [svelte-splitpanes](https://github.com/orefalo/svelte-splitpanes) [![GitHub stars](https://img.shields.io/github/stars/orefalo/svelte-splitpanes?style=flat)](https://github.com/orefalo/svelte-splitpanes/stargazers) - Full featured resizeable views panels.
- [mathjax-svelte](https://github.com/WoolDoughnut310/mathjax-svelte) [![GitHub stars](https://img.shields.io/github/stars/WoolDoughnut310/mathjax-svelte?style=flat)](https://github.com/WoolDoughnut310/mathjax-svelte/stargazers) - A Svelte component for MathJax.
- [svelte-stepper](https://github.com/efstajas/svelte-stepper) [![GitHub stars](https://img.shields.io/github/stars/efstajas/svelte-stepper?style=flat)](https://github.com/efstajas/svelte-stepper/stargazers) - A Svelte component for building animated step flows.
- [css-3d-progress](https://github.com/rofixro/css-3d-progress) [![GitHub stars](https://img.shields.io/github/stars/rofixro/css-3d-progress?style=flat)](https://github.com/rofixro/css-3d-progress/stargazers) - A 3D Progress Bar component
- [svelte-speedometer](https://github.com/palerdot/svelte-speedometer) [![GitHub stars](https://img.shields.io/github/stars/palerdot/svelte-speedometer?style=flat)](https://github.com/palerdot/svelte-speedometer/stargazers) - Svelte component for showing speedometer like gauge using d3.
- [embedz](https://github.com/embedz/embedz) [![GitHub stars](https://img.shields.io/github/stars/embedz/embedz?style=flat)](https://github.com/embedz/embedz/stargazers) - Easy, dependency free embeds for Svelte and Vue.
- [EmbedPDF](https://www.embedpdf.com/docs/svelte/introduction) - A modular, high-performance PDF viewer and editor built for Svelte, powered by PDFium. Fully extensible with plugins for annotations, redaction, thumbnails, and more.
- [Edra](https://edra.tsuzat.com) - Best Rich Text Editor, made for Svelte Developers with Tiptap.
- [svelte-streamdown](https://github.com/beynar/svelte-streamdown) [![GitHub stars](https://img.shields.io/github/stars/beynar/svelte-streamdown?style=flat)](https://github.com/beynar/svelte-streamdown/stargazers) - Port of [streamdown](https://streamdown.ai/). An all in one markdown renderer optimized for streaming with built in styles, math, mermaid, code highlighting support and more.
- [svelte-bash](https://github.com/YusufCeng1z/svelte-bash) [![GitHub stars](https://img.shields.io/github/stars/YusufCeng1z/svelte-bash?style=flat)](https://github.com/YusufCeng1z/svelte-bash/stargazers) - A customizable terminal-style component for Svelte 5.

## Scaffold

_Templates / boilerplate / starter kits / stack ensemble / Yeoman generator._

- [create-vite](https://github.com/vitejs/vite/tree/main/packages/create-vite#readme) - Generates scaffold for a vite + svelte app.
- [create-svelte](https://github.com/sveltejs/kit/tree/master/packages/create-svelte#readme) - A CLI for creating a new SvelteKit project.
- [saasstarter](https://github.com/CriticalMoments/CMSaasStarter) [![GitHub stars](https://img.shields.io/github/stars/CriticalMoments/CMSaasStarter?style=flat)](https://github.com/CriticalMoments/CMSaasStarter/stargazers) - A open source, fast, and free to host Svelte SaaS template.
- [svelte-pwa-template](https://github.com/tretapey/svelte-pwa) [![GitHub stars](https://img.shields.io/github/stars/tretapey/svelte-pwa?style=flat)](https://github.com/tretapey/svelte-pwa/stargazers) - A starter template for PWAs based in the official Template. _(pre-v5)_
- [vite-svelte-docker-template](https://github.com/bavragor/vite-svelte-docker-template) [![GitHub stars](https://img.shields.io/github/stars/bavragor/vite-svelte-docker-template?style=flat)](https://github.com/bavragor/vite-svelte-docker-template/stargazers) - Template for Svelte + Docker + Vite + Vitest.
- [svelte-docs-starter](https://github.com/code-gio/svelte-docs-starter) [![GitHub stars](https://img.shields.io/github/stars/code-gio/svelte-docs-starter?style=flat)](https://github.com/code-gio/svelte-docs-starter/stargazers) - A modern documentation template built with Svelte 5, MDSvex, and Tailwind CSS.
- [template-svelte](https://github.com/phaserjs/template-svelte) [![GitHub stars](https://img.shields.io/github/stars/phaserjs/template-svelte?style=flat)](https://github.com/phaserjs/template-svelte/stargazers) - An official quickstart template with Phaser.
- [generic-app-template](https://github.com/GantonL/templates/tree/main/sveltekit-shadcn-v5) [![GitHub stars](https://img.shields.io/github/stars/GantonL/templates/tree/main/sveltekit-shadcn-v5?style=flat)](https://github.com/GantonL/templates/tree/main/sveltekit-shadcn-v5/stargazers) - A open-source modern full-stack web application template built with SvelteKit + shadcn-svelte. Supports i18n, theming, cookie managment, SEO management, static content with mdsvex, a shell component and more.

## Utilities

### Animations

- [AutoAnimate](https://auto-animate.formkit.com/) - A zero-config, drop-in animation utility that adds smooth transitions to your Svelte app.
- [svelte-typewriter](https://github.com/henriquehbr/svelte-typewriter) [![GitHub stars](https://img.shields.io/github/stars/henriquehbr/svelte-typewriter?style=flat)](https://github.com/henriquehbr/svelte-typewriter/stargazers) - A simple and reusable typewriter effect for your Svelte applications.
- [moving-icons](https://github.com/jis3r/icons) [![GitHub stars](https://img.shields.io/github/stars/jis3r/icons?style=flat)](https://github.com/jis3r/icons/stargazers) - beautifully crafted, moving icons. for svelte. 🧡
- [ssgoi](https://github.com/meursyphus/ssgoi) [![GitHub stars](https://img.shields.io/github/stars/meursyphus/ssgoi?style=flat)](https://github.com/meursyphus/ssgoi/stargazers) - Native app-like page transitions with spring physics, 60fps on mobile, SSR-ready, and all modern browser support.

### Drag & Drop

- [neodrag](https://github.com/PuruVJ/neodrag) [![GitHub stars](https://img.shields.io/github/stars/PuruVJ/neodrag?style=flat)](https://github.com/PuruVJ/neodrag/stargazers) - One Draggable to rule them all 💍.
- sveltednd(https://github.com/thisuxhq/sveltednd) - A lightweight, flexible drag and drop library for Svelte 5 applications.

### Forms

- [Superforms](https://superforms.rocks) - SvelteKit library for handling server and client validation, and client-side display of forms.
- [Formsnap](https://www.formsnap.dev/) - High level Svelte components for forms, built on top of Superforms and Zod.
- [felte](https://felte.dev/) - Extensible form library, with built-in Yup, Zod, Vest, and Superstruct validation.
- [vest](https://github.com/ealush/vest) [![GitHub stars](https://img.shields.io/github/stars/ealush/vest?style=flat)](https://github.com/ealush/vest/stargazers) - 🦺 Declarative form validation framework inspired by unit testing.
- [svelte-formly](https://github.com/arabdevelop/svelte-formly) [![GitHub stars](https://img.shields.io/github/stars/arabdevelop/svelte-formly?style=flat)](https://github.com/arabdevelop/svelte-formly/stargazers) - A good solution to generate and control a dynamic forms using core and custom rules with customize styles. _(pre-v5)_
- [svelte-form-builder](https://github.com/pragmatic-engineering/svelte-form-builder-community) [![GitHub stars](https://img.shields.io/github/stars/pragmatic-engineering/svelte-form-builder-community?style=flat)](https://github.com/pragmatic-engineering/svelte-form-builder-community/stargazers) - A No-code Drag n Drop Form Builder built for Svelte.
- [Svelte Form Builder](https://svelte-form-builder.vercel.app) - Create forms with Shadcn Svelte, Superforms and ZOD | Valibot Schema within minutes.
- [Formisch](https://formisch.dev/svelte/guides/introduction/) - A form library for Svelte with focus on performance, type safety and bundle size.

#### Form Components

_Individual form components._

- [svelte-checkbox](https://github.com/HosseinShabani/svelte-checkbox) [![GitHub stars](https://img.shields.io/github/stars/HosseinShabani/svelte-checkbox?style=flat)](https://github.com/HosseinShabani/svelte-checkbox/stargazers) - A checkbox component (cool animation, customizable). _(pre-v5)_
- [svelte-toggle](https://github.com/beyonk-adventures/svelte-toggle) [![GitHub stars](https://img.shields.io/github/stars/beyonk-adventures/svelte-toggle?style=flat)](https://github.com/beyonk-adventures/svelte-toggle/stargazers) - Basic toggle component with styling. _(pre-v5)_

### HTTP Requests

- [sswr](https://github.com/ConsoleTVs/sswr) [![GitHub stars](https://img.shields.io/github/stars/ConsoleTVs/sswr?style=flat)](https://github.com/ConsoleTVs/sswr/stargazers) - Svelte stale while revalidate (SWR) data fetching strategy.
- [svelte-query](https://sveltequery.vercel.app/) - Fetch, cache and update data in your Svelte applications all without touching any "global state".
- [tanstack-svelte-query](https://tanstack.com/query/latest/docs/svelte/overview) - Framework agnostic type-safe query and mutation library for Svelte.

### Sound & Video

- [svelte-sound](https://github.com/Rajaniraiyn/svelte-sound) [![GitHub stars](https://img.shields.io/github/stars/Rajaniraiyn/svelte-sound?style=flat)](https://github.com/Rajaniraiyn/svelte-sound/stargazers) - Svelte Actions to play interaction sounds on target DOM events.

### WebGL

- [svelthree](https://github.com/vatro/svelthree) [![GitHub stars](https://img.shields.io/github/stars/vatro/svelthree?style=flat)](https://github.com/vatro/svelthree/stargazers) - Component library for declarative construction of reactive and reusable three.js scene graphs.
- [threlte](https://threlte.xyz) - Threlte is a renderer and component library for using Three.js in a declarative and state-driven way in Svelte apps.

### PWA

- [SvelteKit-Adapter-Versioned-Worker](https://github.com/hedgehog125/SvelteKit-Adapter-Versioned-Worker) [![GitHub stars](https://img.shields.io/github/stars/hedgehog125/SvelteKit-Adapter-Versioned-Worker?style=flat)](https://github.com/hedgehog125/SvelteKit-Adapter-Versioned-Worker/stargazers) - An easy-to-use service worker build plugin where you don't need to worry about cache durations.

### Portal

- [svelte-portal](https://github.com/romkor/svelte-portal) [![GitHub stars](https://img.shields.io/github/stars/romkor/svelte-portal?style=flat)](https://github.com/romkor/svelte-portal/stargazers) - Component for rendering outside the DOM of parent component.
- [svelte-teleport](https://github.com/nasso/svelte-teleport) [![GitHub stars](https://img.shields.io/github/stars/nasso/svelte-teleport?style=flat)](https://github.com/nasso/svelte-teleport/stargazers) - A component to teleport elements across the DOM.

### Fonts

- [svelte-web-fonts/google](https://github.com/svelte-web-fonts/google) [![GitHub stars](https://img.shields.io/github/stars/svelte-web-fonts/google?style=flat)](https://github.com/svelte-web-fonts/google/stargazers) - Tiny component for easily loading Fonts via the Google Fonts API including autocompletion.

### Internationalization

- [svelte-fluent](https://github.com/nubolab-ffwd/svelte-fluent) [![GitHub stars](https://img.shields.io/github/stars/nubolab-ffwd/svelte-fluent?style=flat)](https://github.com/nubolab-ffwd/svelte-fluent/stargazers) - Components for easy integration of [Fluent](https://projectfluent.org/) localization.
- [svelte-i18n](https://github.com/kaisermann/svelte-i18n) [![GitHub stars](https://img.shields.io/github/stars/kaisermann/svelte-i18n?style=flat)](https://github.com/kaisermann/svelte-i18n/stargazers) - Internationalization library for Svelte.
- [VoerkaI18n](https://zhangfisher.github.io/voerka-i18n/) - Internationalization solution for `Javascript/Typescript/Vue/React/Solidjs/SvelteJs/ReactNative`
- [sveltekit-i18n](https://github.com/jarda-svoboda/sveltekit-i18n) [![GitHub stars](https://img.shields.io/github/stars/jarda-svoboda/sveltekit-i18n?style=flat)](https://github.com/jarda-svoboda/sveltekit-i18n/stargazers) - For integrating [i18n](https://www.npmjs.com/package/i18n) style localization in SvelteKit.
- [@tolgee/svelte](https://github.com/tolgee/tolgee-js/tree/main/packages/svelte) [![GitHub stars](https://img.shields.io/github/stars/tolgee/tolgee-js/tree/main/packages/svelte?style=flat)](https://github.com/tolgee/tolgee-js/tree/main/packages/svelte/stargazers) - Web-based localization tool enabling users to translate directly in the Svelte app they develop.
- [@i18n-pro/svelte](https://github.com/i18n-pro/svelte) [![GitHub stars](https://img.shields.io/github/stars/i18n-pro/svelte?style=flat)](https://github.com/i18n-pro/svelte/stargazers) - Lightweight, simple, flexible, automatic translation internationalization tool for Svelte.
- [ParaglideJS](https://inlang.com/m/dxnzrydw/library-inlang-paraglideJsAdapterSvelteKit) - Tiny, typesafe i18n library with translated links out of the box.
- [wuchale](https://github.com/K1DV5/wuchale) [![GitHub stars](https://img.shields.io/github/stars/K1DV5/wuchale?style=flat)](https://github.com/K1DV5/wuchale/stargazers) - Internationalization library that lets you just write your code, no function calls or other ceremonies needed.

## Routers

_For Single Page Applications (SPAs) and more._

- [svelte-router-spa](https://github.com/jorgegorka/svelte-router) [![GitHub stars](https://img.shields.io/github/stars/jorgegorka/svelte-router?style=flat)](https://github.com/jorgegorka/svelte-router/stargazers) - Router adds routing to your Single Page Applications (SPA). Includes localisation, guards and nested layouts.
- [svelte-routing](https://github.com/EmilTholin/svelte-routing) [![GitHub stars](https://img.shields.io/github/stars/EmilTholin/svelte-routing?style=flat)](https://github.com/EmilTholin/svelte-routing/stargazers) - A declarative Svelte routing library with SSR support.
- [tinro](https://github.com/AlexxNB/tinro) [![GitHub stars](https://img.shields.io/github/stars/AlexxNB/tinro?style=flat)](https://github.com/AlexxNB/tinro/stargazers) - A tiny, dependency free and highly declarative router.
- [svelte-spa-router](https://github.com/ItalyPaleAle/svelte-spa-router) [![GitHub stars](https://img.shields.io/github/stars/ItalyPaleAle/svelte-spa-router?style=flat)](https://github.com/ItalyPaleAle/svelte-spa-router/stargazers) - Optimized for Single Page Applications (SPA) with hash based routing and support for parameters.
- [svelte-client-router](https://github.com/arthurgermano/svelte-client-router) [![GitHub stars](https://img.shields.io/github/stars/arthurgermano/svelte-client-router?style=flat)](https://github.com/arthurgermano/svelte-client-router/stargazers) - Svelte Client Router is everything you need and think when routing SPA's.
- [@danielsharkov/svelte-router](https://github.com/DanielSharkov/svelte-router) [![GitHub stars](https://img.shields.io/github/stars/DanielSharkov/svelte-router?style=flat)](https://github.com/DanielSharkov/svelte-router/stargazers) - A simple & easy to use SPA router, developed with page transitions in mind.
- [@shaun/svelterouter](https://github.com/shaunlee/svelterouter) [![GitHub stars](https://img.shields.io/github/stars/shaunlee/svelterouter?style=flat)](https://github.com/shaunlee/svelterouter/stargazers) - Another vue-router inspired Svelte router.
- [Elegua](https://github.com/howesteve/elegua) [![GitHub stars](https://img.shields.io/github/stars/howesteve/elegua?style=flat)](https://github.com/howesteve/elegua/stargazers) - Small (< 180LoC), fast, easy, full featured SPA router
- [svelte5-router](https://github.com/mateothegreat/svelte5-router) [![GitHub stars](https://img.shields.io/github/stars/mateothegreat/svelte5-router?style=flat)](https://github.com/mateothegreat/svelte5-router/stargazers) - First Svelte 5 SPA router with nesting, hooks, and more.. Use components, snippets, or both!
- [@wjfe/n-savant](https://github.com/WJSoftware/wjfe-n-savant) [![GitHub stars](https://img.shields.io/github/stars/WJSoftware/wjfe-n-savant?style=flat)](https://github.com/WJSoftware/wjfe-n-savant/stargazers) - Fast, reactive router with always-on path and hash routing, and the router that invented multi-hash routing.
- [sv-router](https://github.com/colinlienard/sv-router) [![GitHub stars](https://img.shields.io/github/stars/colinlienard/sv-router?style=flat)](https://github.com/colinlienard/sv-router/stargazers) - Type-safe SPA router with file-based or code-based routing.

## Frameworks

- [SvelteKit](https://svelte.dev/docs/kit/introduction) - The fastest way to build Svelte apps.
- [Routify](https://routify.dev/) - Routes for Svelte, automated by your file structure.
- [Elder.js](https://github.com/elderjs/elderjs) [![GitHub stars](https://img.shields.io/github/stars/elderjs/elderjs?style=flat)](https://github.com/elderjs/elderjs/stargazers) - Opinionated static site generator and web framework for Svelte built with SEO in mind. _(pre-v5)_
- [JungleJS](https://www.junglejs.org/) - The Jamstack framework for Svelte with GraphQL. _(pre-v5)_
- [svelte-document](https://github.com/mblouka/svelte-document) [![GitHub stars](https://img.shields.io/github/stars/mblouka/svelte-document?style=flat)](https://github.com/mblouka/svelte-document/stargazers) - Create documents (PDFs), resumes, or presentations entirely in Svelte.

## Dev Tools

- [Frontman](https://github.com/frontman-ai/frontman) [![GitHub stars](https://img.shields.io/github/stars/frontman-ai/frontman?style=flat)](https://github.com/frontman-ai/frontman/stargazers) - Open-source AI coding agent that lives in your browser with click-to-edit and hot reload for Svelte apps.

### Adapters

- [JesterKit EXE](https://github.com/Hugo-Dz/exe) [![GitHub stars](https://img.shields.io/github/stars/Hugo-Dz/exe?style=flat)](https://github.com/Hugo-Dz/exe/stargazers) - An adapter to distribute your SvelteKit web app as a single executable binary with zero runtime dependencies. Unlike static builds, it preserves all Kit features like SSR, API endpoints, server hooks, etc.

### Lint

_Lint and format your code._

- [prettier-plugin-svelte](https://github.com/sveltejs/prettier-plugin-svelte) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/prettier-plugin-svelte?style=flat)](https://github.com/sveltejs/prettier-plugin-svelte/stargazers) - Format your components using prettier.
- [svelte-check](https://www.npmjs.com/package/svelte-check) - Check your code.
- [eslint-plugin-svelte](https://github.com/sveltejs/eslint-plugin-svelte) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/eslint-plugin-svelte?style=flat)](https://github.com/sveltejs/eslint-plugin-svelte/stargazers) - An ESLint plugin for Svelte using AST.

### Test

- [svelte-jester](https://github.com/mihar-22/svelte-jester) [![GitHub stars](https://img.shields.io/github/stars/mihar-22/svelte-jester?style=flat)](https://github.com/mihar-22/svelte-jester/stargazers) - A Jest transformer to compile your components before importing them into tests.
- [@testing-library/svelte](https://github.com/testing-library/svelte-testing-library) [![GitHub stars](https://img.shields.io/github/stars/testing-library/svelte-testing-library?style=flat)](https://github.com/testing-library/svelte-testing-library/stargazers) - Simple and complete Svelte DOM testing utilities that encourage good testing practices.
- [jest-transform-svelte](https://github.com/rspieker/jest-transform-svelte) [![GitHub stars](https://img.shields.io/github/stars/rspieker/jest-transform-svelte?style=flat)](https://github.com/rspieker/jest-transform-svelte/stargazers) - Jest Transformer for Svelte components.

### Editors

_Text editor plugins._

#### Visual Studio Code

- [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) - Provides syntax highlighting and rich intellisense for your components.
- [Svelte 3 Snippets](https://marketplace.visualstudio.com/items?itemName=fivethree.vscode-svelte-snippets) - Svelte 3 Snippets for VS Code.

#### Sublime Text

- [Svelte](https://packagecontrol.io/packages/Svelte) - Syntax highlighting and support for Sublime Text.

#### Vim

- [vim-svelte-plugin](https://github.com/leafOfTree/vim-svelte-plugin) [![GitHub stars](https://img.shields.io/github/stars/leafOfTree/vim-svelte-plugin?style=flat)](https://github.com/leafOfTree/vim-svelte-plugin/stargazers) - Syntax highlighting and support for Vim.
- [coc-svelte](https://github.com/coc-extensions/coc-svelte) [![GitHub stars](https://img.shields.io/github/stars/coc-extensions/coc-svelte?style=flat)](https://github.com/coc-extensions/coc-svelte/stargazers) - Syntax highlighting and support for (Neo)Vim.

#### JetBrains

- [Svelte](https://plugins.jetbrains.com/plugin/12375-svelte) - Syntax highlighting and support for JetBrains.

## Application Examples

### Desktop

- [Oxide-Lab](https://github.com/FerrisMind/oxide-lab) [![GitHub stars](https://img.shields.io/github/stars/FerrisMind/oxide-lab?style=flat)](https://github.com/FerrisMind/oxide-lab/stargazers) - Privacy-focused local LLM chat application built with Svelte 5 frontend and Rust backend using the `candle` ML framework.
- [Zephyr](https://github.com/Prismo-Studio/Zephyr) [![GitHub stars](https://img.shields.io/github/stars/Prismo-Studio/Zephyr?style=flat)](https://github.com/Prismo-Studio/Zephyr/stargazers) - Open-source mod manager for PC games with built-in Archipelago multiworld randomizer support, built with Svelte 5 and Tauri 2.
