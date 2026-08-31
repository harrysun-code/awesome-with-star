# React Native

> 来源：[jondot/awesome-react-native](https://github.com/jondot/awesome-react-native)

[![GitHub stars](https://img.shields.io/github/stars/jondot/awesome-react-native?style=flat)](https://github.com/jondot/awesome-react-native/stargazers)

<br/>

<p align="center">
    <img alt="awesome react native" src="arn.svg" width="480" />
</p>

<p align="center">
  <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
</p>

Awesome React Native is a curated list of the best libraries, tools, and learning resources for building React Native apps today. Every entry is checked for maintenance and relevance — if it's here, it works with modern React Native. PRs are welcome, see [contributing](CONTRIBUTING.md).

## Contents

- [Getting Started](#getting-started)
- [AI-Assisted Development](#ai-assisted-development)
  - [Agents & Skills](#agents--skills)
  - [MCP Servers](#mcp-servers)
  - [On-Device AI](#on-device-ai)
  - [AI App Builders](#ai-app-builders)
- [Components](#components)
  - [UI](#ui)
  - [Lists](#lists)
  - [Navigation](#navigation)
  - [Sheets, Menus & Toasts](#sheets-menus--toasts)
  - [Forms & Keyboard](#forms--keyboard)
  - [Text & Rich Content](#text--rich-content)
  - [Image & Camera](#image--camera)
  - [Video & Audio](#video--audio)
  - [Maps & Location](#maps--location)
  - [Charts](#charts)
  - [Animation & Gestures](#animation--gestures)
  - [Styling & Design Systems](#styling--design-systems)
  - [Internationalization](#internationalization)
  - [System & Device](#system--device)
  - [Notifications](#notifications)
  - [Web & WebViews](#web--webviews)
  - [Other Platforms](#other-platforms)
- [Data](#data)
  - [State Management](#state-management)
  - [Storage & Databases](#storage--databases)
  - [Networking](#networking)
- [Services & Integrations](#services--integrations)
- [Payments & Monetization](#payments--monetization)
- [Development Tools](#development-tools)
  - [Tooling & IDE](#tooling--ide)
  - [Debugging](#debugging)
  - [Testing](#testing)
  - [Builds, Deployment & OTA Updates](#builds-deployment--ota-updates)
  - [Building Libraries](#building-libraries)
- [Starters & Boilerplates](#starters--boilerplates)
- [Open Source Apps](#open-source-apps)
- [Learning](#learning)
- [Staying Up to Date](#staying-up-to-date)

## Getting Started

- [React Native](https://reactnative.dev) - Official documentation, including environment setup, guides, and API reference.
- [Expo](https://expo.dev) - The recommended framework for building React Native apps: file-based routing, native modules, builds, and updates out of the box.
- [React Native Directory](https://reactnative.directory) - Searchable, filterable directory of React Native libraries with maintenance and New Architecture compatibility signals.
- [Upgrade Helper](https://github.com/react-native-community/upgrade-helper) [![GitHub stars](https://img.shields.io/github/stars/react-native-community/upgrade-helper?style=flat)](https://github.com/react-native-community/upgrade-helper/stargazers) - Web tool that shows the exact diff between two React Native versions for painless upgrades.
- [rn-diff-purge](https://github.com/react-native-community/rn-diff-purge) [![GitHub stars](https://img.shields.io/github/stars/react-native-community/rn-diff-purge?style=flat)](https://github.com/react-native-community/rn-diff-purge/stargazers) - The raw version-to-version diffs powering Upgrade Helper.
- [Expo Examples](https://github.com/expo/examples) [![GitHub stars](https://img.shields.io/github/stars/expo/examples?style=flat)](https://github.com/expo/examples/stargazers) - Example projects demonstrating Expo APIs and integrations.

## AI-Assisted Development

Tools for building React Native apps with AI agents, and for putting AI inside your apps.

### Agents & Skills

- [Expo AI Agents Guide](https://docs.expo.dev/agents/) - Expo's official documentation for AI-native development: agent setup, llms.txt, and best practices.
- [Claude Code + Expo](https://docs.expo.dev/agents/claude/) - Official guide for building, debugging, and deploying Expo apps with Claude Code.
- [Expo Skills](https://github.com/expo/skills) [![GitHub stars](https://img.shields.io/github/stars/expo/skills?style=flat)](https://github.com/expo/skills/stargazers) - Agent skills that give coding agents Expo-specific knowledge and best practices.
- [Agent Skills](https://github.com/anthropics/skills) [![GitHub stars](https://img.shields.io/github/stars/anthropics/skills?style=flat)](https://github.com/anthropics/skills/stargazers) - Anthropic's public repository of agent skills, usable with Claude Code and other agents.

### MCP Servers

- [Expo MCP](https://docs.expo.dev/mcp/) - Expo-hosted MCP server: EAS logs, documentation search, and deployment workflows from any MCP-capable agent.
- [mobile-mcp](https://github.com/mobile-next/mobile-mcp) [![GitHub stars](https://img.shields.io/github/stars/mobile-next/mobile-mcp?style=flat)](https://github.com/mobile-next/mobile-mcp/stargazers) - MCP server for mobile automation on iOS, Android, emulators, simulators, and real devices.
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) [![GitHub stars](https://img.shields.io/github/stars/joshuayoes/ios-simulator-mcp?style=flat)](https://github.com/joshuayoes/ios-simulator-mcp/stargazers) - MCP server for driving the iOS simulator: interact with UI, take screenshots, inspect the view hierarchy.
- [Maestro](https://maestro.dev) - E2E testing framework with a built-in MCP server, letting agents run flows and control devices.

### On-Device AI

- [react-native-executorch](https://github.com/software-mansion/react-native-executorch) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/react-native-executorch?style=flat)](https://github.com/software-mansion/react-native-executorch/stargazers) - Declarative on-device AI inference powered by ExecuTorch, from Software Mansion.
- [llama.rn](https://github.com/mybigday/llama.rn) [![GitHub stars](https://img.shields.io/github/stars/mybigday/llama.rn?style=flat)](https://github.com/mybigday/llama.rn/stargazers) - React Native binding of llama.cpp for running LLMs on device.
- [react-native-fast-tflite](https://github.com/mrousavy/react-native-fast-tflite) [![GitHub stars](https://img.shields.io/github/stars/mrousavy/react-native-fast-tflite?style=flat)](https://github.com/mrousavy/react-native-fast-tflite/stargazers) - High-performance TensorFlow Lite inference with GPU acceleration.
- [AI SDK](https://github.com/vercel/ai) [![GitHub stars](https://img.shields.io/github/stars/vercel/ai?style=flat)](https://github.com/vercel/ai/stargazers) - The AI toolkit for TypeScript; works in Expo and React Native apps for chat, streaming, and tool use.

### AI App Builders

- [a0.dev](https://a0.dev) - Generates complete React Native apps from a prompt and ships them to the app stores.
- [Rork](https://rork.com) - AI app builder that generates Expo/React Native projects compiling to native iOS, Android, and web.

## Components

### UI

- [react-native-paper](https://github.com/callstack/react-native-paper) [![GitHub stars](https://img.shields.io/github/stars/callstack/react-native-paper?style=flat)](https://github.com/callstack/react-native-paper/stargazers) - Material Design components for Android and iOS.
- [React Native Elements](https://github.com/react-native-elements/react-native-elements) [![GitHub stars](https://img.shields.io/github/stars/react-native-elements/react-native-elements?style=flat)](https://github.com/react-native-elements/react-native-elements/stargazers) - Cross-platform UI toolkit with themed, composable components.
- [Tamagui](https://github.com/tamagui/tamagui) [![GitHub stars](https://img.shields.io/github/stars/tamagui/tamagui?style=flat)](https://github.com/tamagui/tamagui/stargazers) - Universal UI kit and style system with an optimizing compiler, 100% parity between React Native and web.
- [gluestack-ui](https://github.com/gluestack/gluestack-ui) [![GitHub stars](https://img.shields.io/github/stars/gluestack/gluestack-ui?style=flat)](https://github.com/gluestack/gluestack-ui/stargazers) - Copy-paste components and patterns built on Tailwind-style utility classes.
- [react-native-ui-kitten](https://github.com/akveo/react-native-ui-kitten) [![GitHub stars](https://img.shields.io/github/stars/akveo/react-native-ui-kitten?style=flat)](https://github.com/akveo/react-native-ui-kitten/stargazers) - UI library based on the Eva Design System with theming support.
- [NativeBase](https://github.com/GeekyAnts/NativeBase) [![GitHub stars](https://img.shields.io/github/stars/GeekyAnts/NativeBase?style=flat)](https://github.com/GeekyAnts/NativeBase/stargazers) - Mobile-first, accessible component library for React Native and web.
- [Shoutem UI](https://github.com/shoutem/ui) [![GitHub stars](https://img.shields.io/github/stars/shoutem/ui?style=flat)](https://github.com/shoutem/ui/stargazers) - Customizable set of styled components for React Native.
- [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons) [![GitHub stars](https://img.shields.io/github/stars/oblador/react-native-vector-icons?style=flat)](https://github.com/oblador/react-native-vector-icons/stargazers) - Customizable icon sets with support for styling and image sources.
- [lottie-react-native](https://github.com/lottie-react-native/lottie-react-native) [![GitHub stars](https://img.shields.io/github/stars/lottie-react-native/lottie-react-native?style=flat)](https://github.com/lottie-react-native/lottie-react-native/stargazers) - Render After Effects animations natively.
- [react-native-svg](https://github.com/software-mansion/react-native-svg) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/react-native-svg?style=flat)](https://github.com/software-mansion/react-native-svg/stargazers) - SVG rendering for React Native and web.
- [react-native-svg-transformer](https://github.com/kristerkari/react-native-svg-transformer) [![GitHub stars](https://img.shields.io/github/stars/kristerkari/react-native-svg-transformer?style=flat)](https://github.com/kristerkari/react-native-svg-transformer/stargazers) - Import SVG files as components, like on the web.
- [react-native-modal](https://github.com/react-native-modal/react-native-modal) [![GitHub stars](https://img.shields.io/github/stars/react-native-modal/react-native-modal?style=flat)](https://github.com/react-native-modal/react-native-modal/stargazers) - Enhanced, animated, customizable modal.
- [react-native-blur](https://github.com/margelo/react-native-blur) [![GitHub stars](https://img.shields.io/github/stars/margelo/react-native-blur?style=flat)](https://github.com/margelo/react-native-blur/stargazers) - Native blur view component.
- [react-native-blurhash](https://github.com/mrousavy/react-native-blurhash) [![GitHub stars](https://img.shields.io/github/stars/mrousavy/react-native-blurhash?style=flat)](https://github.com/mrousavy/react-native-blurhash/stargazers) - Colorful blurry placeholders while content loads.
- [react-native-calendars](https://github.com/wix/react-native-calendars) [![GitHub stars](https://img.shields.io/github/stars/wix/react-native-calendars?style=flat)](https://github.com/wix/react-native-calendars/stargazers) - Feature-rich calendar components.
- [react-native-date-picker](https://github.com/henninghall/react-native-date-picker) [![GitHub stars](https://img.shields.io/github/stars/henninghall/react-native-date-picker?style=flat)](https://github.com/henninghall/react-native-date-picker/stargazers) - Native date and time picker for Android and iOS.
- [react-native-reanimated-carousel](https://github.com/dohooo/react-native-reanimated-carousel) [![GitHub stars](https://img.shields.io/github/stars/dohooo/react-native-reanimated-carousel?style=flat)](https://github.com/dohooo/react-native-reanimated-carousel/stargazers) - Swiper/carousel built entirely on Reanimated, the successor to snap-carousel.
- [react-native-pager-view](https://github.com/callstack/react-native-pager-view) [![GitHub stars](https://img.shields.io/github/stars/callstack/react-native-pager-view?style=flat)](https://github.com/callstack/react-native-pager-view/stargazers) - Native ViewPager and UIPageViewController wrapper.
- [react-native-copilot](https://github.com/mohebifar/react-native-copilot) [![GitHub stars](https://img.shields.io/github/stars/mohebifar/react-native-copilot?style=flat)](https://github.com/mohebifar/react-native-copilot/stargazers) - Step-by-step walkthrough tooltips for onboarding.
- [react-native-super-grid](https://github.com/saleel/react-native-super-grid) [![GitHub stars](https://img.shields.io/github/stars/saleel/react-native-super-grid?style=flat)](https://github.com/saleel/react-native-super-grid/stargazers) - Responsive grid view.
- [react-native-circular-progress](https://github.com/bartgryszko/react-native-circular-progress) [![GitHub stars](https://img.shields.io/github/stars/bartgryszko/react-native-circular-progress?style=flat)](https://github.com/bartgryszko/react-native-circular-progress/stargazers) - Animated circular progress indicators.
- [react-native-progress-steps](https://github.com/colbymillerdev/react-native-progress-steps) [![GitHub stars](https://img.shields.io/github/stars/colbymillerdev/react-native-progress-steps?style=flat)](https://github.com/colbymillerdev/react-native-progress-steps/stargazers) - Customizable progress stepper.
- [react-native-confirmation-code-field](https://github.com/retyui/react-native-confirmation-code-field) [![GitHub stars](https://img.shields.io/github/stars/retyui/react-native-confirmation-code-field?style=flat)](https://github.com/retyui/react-native-confirmation-code-field/stargazers) - OTP/confirmation code input for iOS, Android, and web.
- [react-native-qrcode-svg](https://github.com/Expensify/react-native-qrcode-svg) [![GitHub stars](https://img.shields.io/github/stars/Expensify/react-native-qrcode-svg?style=flat)](https://github.com/Expensify/react-native-qrcode-svg/stargazers) - QR code generator based on react-native-svg.
- [react-native-country-picker-modal](https://github.com/xcarpentier/react-native-country-picker-modal) [![GitHub stars](https://img.shields.io/github/stars/xcarpentier/react-native-country-picker-modal?style=flat)](https://github.com/xcarpentier/react-native-country-picker-modal/stargazers) - Country picker with flags, search, and localization.
- [react-native-hole-view](https://github.com/ibitcy/react-native-hole-view) [![GitHub stars](https://img.shields.io/github/stars/ibitcy/react-native-hole-view?style=flat)](https://github.com/ibitcy/react-native-hole-view/stargazers) - Cut touch-through holes anywhere, perfect for onboarding highlights.

### Lists

- [FlashList](https://github.com/Shopify/flash-list) [![GitHub stars](https://img.shields.io/github/stars/Shopify/flash-list?style=flat)](https://github.com/Shopify/flash-list/stargazers) - Shopify's fast and performant list, a drop-in replacement for FlatList.
- [Legend List](https://github.com/LegendApp/legend-list) [![GitHub stars](https://img.shields.io/github/stars/LegendApp/legend-list?style=flat)](https://github.com/LegendApp/legend-list/stargazers) - High-performance list in pure JS, built for the New Architecture.
- [recyclerlistview](https://github.com/Flipkart/recyclerlistview) [![GitHub stars](https://img.shields.io/github/stars/Flipkart/recyclerlistview?style=flat)](https://github.com/Flipkart/recyclerlistview/stargazers) - The recycling listview that pioneered high-performance lists in React Native.

### Navigation

- [React Navigation](https://github.com/react-navigation/react-navigation) [![GitHub stars](https://img.shields.io/github/stars/react-navigation/react-navigation?style=flat)](https://github.com/react-navigation/react-navigation/stargazers) - The standard routing and navigation library for React Native.
- [Expo Router](https://docs.expo.dev/router/introduction/) - File-based routing for universal React Native apps, built on React Navigation.
- [react-native-navigation](https://github.com/wix/react-native-navigation) [![GitHub stars](https://img.shields.io/github/stars/wix/react-native-navigation?style=flat)](https://github.com/wix/react-native-navigation/stargazers) - Wix's fully native navigation solution.
- [react-native-screens](https://github.com/software-mansion/react-native-screens) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/react-native-screens?style=flat)](https://github.com/software-mansion/react-native-screens/stargazers) - Native navigation primitives that back React Navigation's native stack.
- [react-native-bottom-tabs](https://github.com/callstack/react-native-bottom-tabs) [![GitHub stars](https://img.shields.io/github/stars/callstack/react-native-bottom-tabs?style=flat)](https://github.com/callstack/react-native-bottom-tabs/stargazers) - Truly native bottom tab bars (SwiftUI and Material) for React Native.

### Sheets, Menus & Toasts

- [react-native-bottom-sheet](https://github.com/gorhom/react-native-bottom-sheet) [![GitHub stars](https://img.shields.io/github/stars/gorhom/react-native-bottom-sheet?style=flat)](https://github.com/gorhom/react-native-bottom-sheet/stargazers) - Performant, interactive bottom sheet with configurable gestures.
- [react-native-true-sheet](https://github.com/lodev09/react-native-true-sheet) [![GitHub stars](https://img.shields.io/github/stars/lodev09/react-native-true-sheet?style=flat)](https://github.com/lodev09/react-native-true-sheet/stargazers) - The true native bottom sheet experience.
- [react-native-actions-sheet](https://github.com/ammarahm-ed/react-native-actions-sheet) [![GitHub stars](https://img.shields.io/github/stars/ammarahm-ed/react-native-actions-sheet?style=flat)](https://github.com/ammarahm-ed/react-native-actions-sheet/stargazers) - Cross-platform ActionSheet with a flexible API.
- [Zeego](https://github.com/nandorojo/zeego) [![GitHub stars](https://img.shields.io/github/stars/nandorojo/zeego?style=flat)](https://github.com/nandorojo/zeego/stargazers) - Menus for React Native done right — truly native dropdown and context menus.
- [Burnt](https://github.com/nandorojo/burnt) [![GitHub stars](https://img.shields.io/github/stars/nandorojo/burnt?style=flat)](https://github.com/nandorojo/burnt/stargazers) - Native toasts and alerts for iOS and Android.
- [react-native-root-toast](https://github.com/magicismight/react-native-root-toast) [![GitHub stars](https://img.shields.io/github/stars/magicismight/react-native-root-toast?style=flat)](https://github.com/magicismight/react-native-root-toast/stargazers) - Pure JavaScript toast solution.
- [react-native-flash-message](https://github.com/lucasferreira/react-native-flash-message) [![GitHub stars](https://img.shields.io/github/stars/lucasferreira/react-native-flash-message?style=flat)](https://github.com/lucasferreira/react-native-flash-message/stargazers) - Flashbar and top-notification alerts.
- [react-native-notifier](https://github.com/seniv/react-native-notifier) [![GitHub stars](https://img.shields.io/github/stars/seniv/react-native-notifier?style=flat)](https://github.com/seniv/react-native-notifier/stargazers) - Fast and simple in-app notifications.
- [react-native-popup-menu](https://github.com/instea/react-native-popup-menu) [![GitHub stars](https://img.shields.io/github/stars/instea/react-native-popup-menu?style=flat)](https://github.com/instea/react-native-popup-menu/stargazers) - Extensible popup menu component.

### Forms & Keyboard

- [React Hook Form](https://github.com/react-hook-form/react-hook-form) [![GitHub stars](https://img.shields.io/github/stars/react-hook-form/react-hook-form?style=flat)](https://github.com/react-hook-form/react-hook-form/stargazers) - Performant form state management and validation for React and React Native.
- [Formik](https://github.com/jaredpalmer/formik) [![GitHub stars](https://img.shields.io/github/stars/jaredpalmer/formik?style=flat)](https://github.com/jaredpalmer/formik/stargazers) - Build forms without the tears.
- [react-native-keyboard-controller](https://github.com/kirillzyusko/react-native-keyboard-controller) [![GitHub stars](https://img.shields.io/github/stars/kirillzyusko/react-native-keyboard-controller?style=flat)](https://github.com/kirillzyusko/react-native-keyboard-controller/stargazers) - Keyboard manager that works identically on iOS and Android.
- [react-native-picker-select](https://github.com/lawnstarter/react-native-picker-select) [![GitHub stars](https://img.shields.io/github/stars/lawnstarter/react-native-picker-select?style=flat)](https://github.com/lawnstarter/react-native-picker-select/stargazers) - Picker emulating the native select interface.
- [react-native-autocomplete-input](https://github.com/byteburgers/react-native-autocomplete-input) [![GitHub stars](https://img.shields.io/github/stars/byteburgers/react-native-autocomplete-input?style=flat)](https://github.com/byteburgers/react-native-autocomplete-input/stargazers) - Pure JavaScript autocomplete input.
- [react-native-masked-text](https://github.com/bhrott/react-native-masked-text) [![GitHub stars](https://img.shields.io/github/stars/bhrott/react-native-masked-text?style=flat)](https://github.com/bhrott/react-native-masked-text/stargazers) - Masked text and input components.
- [react-native-credit-card-input](https://github.com/sbycrosz/react-native-credit-card-input) [![GitHub stars](https://img.shields.io/github/stars/sbycrosz/react-native-credit-card-input?style=flat)](https://github.com/sbycrosz/react-native-credit-card-input/stargazers) - Cross-platform credit card input.
- [react-native-multiple-select](https://github.com/toystars/react-native-multiple-select) [![GitHub stars](https://img.shields.io/github/stars/toystars/react-native-multiple-select?style=flat)](https://github.com/toystars/react-native-multiple-select/stargazers) - Simple multi-select component.

### Text & Rich Content

- [react-native-live-markdown](https://github.com/Expensify/react-native-live-markdown) [![GitHub stars](https://img.shields.io/github/stars/Expensify/react-native-live-markdown?style=flat)](https://github.com/Expensify/react-native-live-markdown/stargazers) - Drop-in TextInput replacement with live Markdown formatting, by Expensify.
- [react-native-markdown-display](https://github.com/iamacup/react-native-markdown-display) [![GitHub stars](https://img.shields.io/github/stars/iamacup/react-native-markdown-display?style=flat)](https://github.com/iamacup/react-native-markdown-display/stargazers) - 100% CommonMark-compatible Markdown renderer.
- [react-native-hyperlink](https://github.com/obipawan/react-native-hyperlink) [![GitHub stars](https://img.shields.io/github/stars/obipawan/react-native-hyperlink?style=flat)](https://github.com/obipawan/react-native-hyperlink/stargazers) - Make URLs, emails, and fuzzy links clickable.
- [react-native-html-to-pdf](https://github.com/christopherdro/react-native-html-to-pdf) [![GitHub stars](https://img.shields.io/github/stars/christopherdro/react-native-html-to-pdf?style=flat)](https://github.com/christopherdro/react-native-html-to-pdf/stargazers) - Convert HTML strings to PDF documents.
- [react-native-responsive-fontsize](https://github.com/heyman333/react-native-responsive-fontsize) [![GitHub stars](https://img.shields.io/github/stars/heyman333/react-native-responsive-fontsize?style=flat)](https://github.com/heyman333/react-native-responsive-fontsize/stargazers) - Responsive font sizes based on device screen size.

### Image & Camera

- [react-native-vision-camera](https://github.com/mrousavy/react-native-vision-camera) [![GitHub stars](https://img.shields.io/github/stars/mrousavy/react-native-vision-camera?style=flat)](https://github.com/mrousavy/react-native-vision-camera/stargazers) - Powerful, high-performance camera library with frame processors.
- [expo-image](https://docs.expo.dev/versions/latest/sdk/image/) - Fast, modern image component with caching and blurhash support.
- [react-native-image-picker](https://github.com/react-native-image-picker/react-native-image-picker) [![GitHub stars](https://img.shields.io/github/stars/react-native-image-picker/react-native-image-picker?style=flat)](https://github.com/react-native-image-picker/react-native-image-picker/stargazers) - Native UI for selecting photos and videos.
- [react-native-image-crop-picker](https://github.com/ivpusic/react-native-image-crop-picker) [![GitHub stars](https://img.shields.io/github/stars/ivpusic/react-native-image-crop-picker?style=flat)](https://github.com/ivpusic/react-native-image-crop-picker/stargazers) - Image picker with camera, cropping, and compression.
- [react-native-camera-kit](https://github.com/teslamotors/react-native-camera-kit) [![GitHub stars](https://img.shields.io/github/stars/teslamotors/react-native-camera-kit?style=flat)](https://github.com/teslamotors/react-native-camera-kit/stargazers) - High-performance camera library with barcode scanning, by Tesla.
- [react-native-image-resizer](https://github.com/bamlab/react-native-image-resizer) [![GitHub stars](https://img.shields.io/github/stars/bamlab/react-native-image-resizer?style=flat)](https://github.com/bamlab/react-native-image-resizer/stargazers) - Resize local images natively.

### Video & Audio

- [react-native-video](https://github.com/TheWidlarzGroup/react-native-video) [![GitHub stars](https://img.shields.io/github/stars/TheWidlarzGroup/react-native-video?style=flat)](https://github.com/TheWidlarzGroup/react-native-video/stargazers) - The Video component for React Native.
- [expo-video](https://docs.expo.dev/versions/latest/sdk/video/) - Modern video playback built for Expo and the New Architecture.
- [react-native-track-player](https://github.com/doublesymmetry/react-native-track-player) [![GitHub stars](https://img.shields.io/github/stars/doublesymmetry/react-native-track-player?style=flat)](https://github.com/doublesymmetry/react-native-track-player/stargazers) - Full-featured audio player: background playback, Android Auto, CarPlay, lock-screen controls.
- [react-native-audio-api](https://github.com/software-mansion/react-native-audio-api) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/react-native-audio-api?style=flat)](https://github.com/software-mansion/react-native-audio-api/stargazers) - High-performance audio engine implementing the Web Audio API.
- [react-native-sound](https://github.com/zmxv/react-native-sound) [![GitHub stars](https://img.shields.io/github/stars/zmxv/react-native-sound?style=flat)](https://github.com/zmxv/react-native-sound/stargazers) - Play sound clips natively.
- [react-native-webrtc](https://github.com/react-native-webrtc/react-native-webrtc) [![GitHub stars](https://img.shields.io/github/stars/react-native-webrtc/react-native-webrtc?style=flat)](https://github.com/react-native-webrtc/react-native-webrtc/stargazers) - WebRTC for React Native.

### Maps & Location

- [react-native-maps](https://github.com/react-native-maps/react-native-maps) [![GitHub stars](https://img.shields.io/github/stars/react-native-maps/react-native-maps?style=flat)](https://github.com/react-native-maps/react-native-maps/stargazers) - MapView components for iOS and Android.
- [rnmapbox/maps](https://github.com/rnmapbox/maps) [![GitHub stars](https://img.shields.io/github/stars/rnmapbox/maps?style=flat)](https://github.com/rnmapbox/maps/stargazers) - Mapbox maps for custom map experiences.
- [react-native-background-geolocation](https://github.com/transistorsoft/react-native-background-geolocation) [![GitHub stars](https://img.shields.io/github/stars/transistorsoft/react-native-background-geolocation?style=flat)](https://github.com/transistorsoft/react-native-background-geolocation/stargazers) - Battery-conscious background location with motion detection.
- [react-native-map-link](https://github.com/tschoffelen/react-native-map-link) [![GitHub stars](https://img.shields.io/github/stars/tschoffelen/react-native-map-link?style=flat)](https://github.com/tschoffelen/react-native-map-link/stargazers) - Open the user's preferred maps app.
- [react-native-google-places-autocomplete](https://github.com/FaridSafi/react-native-google-places-autocomplete) [![GitHub stars](https://img.shields.io/github/stars/FaridSafi/react-native-google-places-autocomplete?style=flat)](https://github.com/FaridSafi/react-native-google-places-autocomplete/stargazers) - Customizable Google Places autocomplete.

### Charts

- [victory-native-xl](https://github.com/FormidableLabs/victory-native-xl) [![GitHub stars](https://img.shields.io/github/stars/FormidableLabs/victory-native-xl?style=flat)](https://github.com/FormidableLabs/victory-native-xl/stargazers) - Charting built on Skia and Reanimated with a focus on performance.
- [react-native-graph](https://github.com/margelo/react-native-graph) [![GitHub stars](https://img.shields.io/github/stars/margelo/react-native-graph?style=flat)](https://github.com/margelo/react-native-graph/stargazers) - Beautiful, high-performance line graphs built with Skia.
- [react-native-gifted-charts](https://github.com/Abhinandan-Kushwaha/react-native-gifted-charts) [![GitHub stars](https://img.shields.io/github/stars/Abhinandan-Kushwaha/react-native-gifted-charts?style=flat)](https://github.com/Abhinandan-Kushwaha/react-native-gifted-charts/stargazers) - Bar, line, area, pie, donut, and stacked charts.

### Animation & Gestures

- [react-native-reanimated](https://github.com/software-mansion/react-native-reanimated) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/react-native-reanimated?style=flat)](https://github.com/software-mansion/react-native-reanimated/stargazers) - The standard for performant animations, running on the UI thread.
- [react-native-gesture-handler](https://github.com/software-mansion/react-native-gesture-handler) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/react-native-gesture-handler?style=flat)](https://github.com/software-mansion/react-native-gesture-handler/stargazers) - Declarative, native-driven gesture system.
- [react-native-skia](https://github.com/Shopify/react-native-skia) [![GitHub stars](https://img.shields.io/github/stars/Shopify/react-native-skia?style=flat)](https://github.com/Shopify/react-native-skia/stargazers) - High-performance 2D graphics with the Skia rendering engine.
- [Moti](https://github.com/nandorojo/moti) [![GitHub stars](https://img.shields.io/github/stars/nandorojo/moti?style=flat)](https://github.com/nandorojo/moti/stargazers) - Universal animation library powered by Reanimated, with a Framer Motion-like API.
- [react-native-animatable](https://github.com/oblador/react-native-animatable) [![GitHub stars](https://img.shields.io/github/stars/oblador/react-native-animatable?style=flat)](https://github.com/oblador/react-native-animatable/stargazers) - Declarative transitions and standard animations.
- [TypeGPU](https://github.com/software-mansion/TypeGPU) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/TypeGPU?style=flat)](https://github.com/software-mansion/TypeGPU/stargazers) - Type-safe WebGPU toolkit for advanced GPU work.

### Styling & Design Systems

- [NativeWind](https://github.com/nativewind/nativewind) [![GitHub stars](https://img.shields.io/github/stars/nativewind/nativewind?style=flat)](https://github.com/nativewind/nativewind/stargazers) - Tailwind CSS for React Native.
- [Unistyles](https://github.com/jpudysz/react-native-unistyles) [![GitHub stars](https://img.shields.io/github/stars/jpudysz/react-native-unistyles?style=flat)](https://github.com/jpudysz/react-native-unistyles/stargazers) - C++-powered StyleSheet superset with themes and breakpoints, built for the New Architecture.
- [styled-components](https://github.com/styled-components/styled-components) [![GitHub stars](https://img.shields.io/github/stars/styled-components/styled-components?style=flat)](https://github.com/styled-components/styled-components/stargazers) - CSS-in-JS styling that also targets React Native.
- [Emotion](https://github.com/emotion-js/emotion) [![GitHub stars](https://img.shields.io/github/stars/emotion-js/emotion?style=flat)](https://github.com/emotion-js/emotion/stargazers) - High-performance CSS-in-JS style composition.
- [react-native-typography](https://github.com/hectahertz/react-native-typography) [![GitHub stars](https://img.shields.io/github/stars/hectahertz/react-native-typography?style=flat)](https://github.com/hectahertz/react-native-typography/stargazers) - Pixel-perfect, native-looking typographic styles.
- [Stacks](https://github.com/grapp-dev/stacks) [![GitHub stars](https://img.shields.io/github/stars/grapp-dev/stacks?style=flat)](https://github.com/grapp-dev/stacks/stargazers) - Layout primitives for building consistent UIs.
- [react-native-edge-to-edge](https://github.com/zoontek/react-native-edge-to-edge) [![GitHub stars](https://img.shields.io/github/stars/zoontek/react-native-edge-to-edge?style=flat)](https://github.com/zoontek/react-native-edge-to-edge/stargazers) - Effortless edge-to-edge display on Android.
- [react-native-safe-area-context](https://github.com/AppAndFlow/react-native-safe-area-context) [![GitHub stars](https://img.shields.io/github/stars/AppAndFlow/react-native-safe-area-context?style=flat)](https://github.com/AppAndFlow/react-native-safe-area-context/stargazers) - Flexible safe area inset handling.

### Internationalization

- [react-native-localize](https://github.com/zoontek/react-native-localize) [![GitHub stars](https://img.shields.io/github/stars/zoontek/react-native-localize?style=flat)](https://github.com/zoontek/react-native-localize/stargazers) - Toolbox for app localization: locales, timezones, currencies.

### System & Device

- [react-native-device-info](https://github.com/react-native-device-info/react-native-device-info) [![GitHub stars](https://img.shields.io/github/stars/react-native-device-info/react-native-device-info?style=flat)](https://github.com/react-native-device-info/react-native-device-info/stargazers) - Device information for iOS and Android.
- [react-native-permissions](https://github.com/zoontek/react-native-permissions) [![GitHub stars](https://img.shields.io/github/stars/zoontek/react-native-permissions?style=flat)](https://github.com/zoontek/react-native-permissions/stargazers) - Unified permissions API.
- [react-native-keychain](https://github.com/oblador/react-native-keychain) [![GitHub stars](https://img.shields.io/github/stars/oblador/react-native-keychain?style=flat)](https://github.com/oblador/react-native-keychain/stargazers) - Secure keychain and keystore access.
- [react-native-config](https://github.com/react-native-config/react-native-config) [![GitHub stars](https://img.shields.io/github/stars/react-native-config/react-native-config?style=flat)](https://github.com/react-native-config/react-native-config/stargazers) - Expose environment config to your JS and native code.
- [react-native-contacts](https://github.com/morenoh149/react-native-contacts) [![GitHub stars](https://img.shields.io/github/stars/morenoh149/react-native-contacts?style=flat)](https://github.com/morenoh149/react-native-contacts/stargazers) - Native contacts access.
- [react-native-calendar-events](https://github.com/wmcmahan/react-native-calendar-events) [![GitHub stars](https://img.shields.io/github/stars/wmcmahan/react-native-calendar-events?style=flat)](https://github.com/wmcmahan/react-native-calendar-events/stargazers) - Calendar event access for iOS and Android.
- [react-native-share](https://github.com/react-native-share/react-native-share) [![GitHub stars](https://img.shields.io/github/stars/react-native-share/react-native-share?style=flat)](https://github.com/react-native-share/react-native-share/stargazers) - Native share sheet and social sharing.
- [react-native-haptic-feedback](https://github.com/mkuczera/react-native-haptic-feedback) [![GitHub stars](https://img.shields.io/github/stars/mkuczera/react-native-haptic-feedback?style=flat)](https://github.com/mkuczera/react-native-haptic-feedback/stargazers) - Haptics that feel right, including Core Haptics patterns.
- [react-native-sensors](https://github.com/react-native-sensors/react-native-sensors) [![GitHub stars](https://img.shields.io/github/stars/react-native-sensors/react-native-sensors?style=flat)](https://github.com/react-native-sensors/react-native-sensors/stargazers) - Developer-friendly access to device sensors.
- [react-native-background-fetch](https://github.com/transistorsoft/react-native-background-fetch) [![GitHub stars](https://img.shields.io/github/stars/transistorsoft/react-native-background-fetch?style=flat)](https://github.com/transistorsoft/react-native-background-fetch/stargazers) - Periodic background callbacks on iOS and Android.
- [react-native-background-downloader](https://github.com/kesha-antonov/react-native-background-downloader) [![GitHub stars](https://img.shields.io/github/stars/kesha-antonov/react-native-background-downloader?style=flat)](https://github.com/kesha-antonov/react-native-background-downloader/stargazers) - Download and upload large files, even when the app is backgrounded.
- [document-picker](https://github.com/react-native-documents/document-picker) [![GitHub stars](https://img.shields.io/github/stars/react-native-documents/document-picker?style=flat)](https://github.com/react-native-documents/document-picker/stargazers) - Document picker and viewer.
- [expo-quick-actions](https://github.com/EvanBacon/expo-quick-actions) [![GitHub stars](https://img.shields.io/github/stars/EvanBacon/expo-quick-actions?style=flat)](https://github.com/EvanBacon/expo-quick-actions/stargazers) - Home screen quick actions and custom app icons.
- [react-native-ssl-pinning](https://github.com/MaxToyberman/react-native-ssl-pinning) [![GitHub stars](https://img.shields.io/github/stars/MaxToyberman/react-native-ssl-pinning?style=flat)](https://github.com/MaxToyberman/react-native-ssl-pinning/stargazers) - SSL pinning and cookie handling.

### Notifications

- [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) - Push and local notifications for Expo apps.
- [react-native-firebase](https://github.com/invertase/react-native-firebase) [![GitHub stars](https://img.shields.io/github/stars/invertase/react-native-firebase?style=flat)](https://github.com/invertase/react-native-firebase/stargazers) - Includes FCM messaging alongside the full Firebase suite.
- [react-native-notifications](https://github.com/wix/react-native-notifications) [![GitHub stars](https://img.shields.io/github/stars/wix/react-native-notifications?style=flat)](https://github.com/wix/react-native-notifications/stargazers) - Wix's notification handling library.
- [react-native-onesignal](https://github.com/OneSignal/react-native-onesignal) [![GitHub stars](https://img.shields.io/github/stars/OneSignal/react-native-onesignal?style=flat)](https://github.com/OneSignal/react-native-onesignal/stargazers) - OneSignal push notification SDK.

### Web & WebViews

- [react-native-webview](https://github.com/react-native-webview/react-native-webview) [![GitHub stars](https://img.shields.io/github/stars/react-native-webview/react-native-webview?style=flat)](https://github.com/react-native-webview/react-native-webview/stargazers) - The community WebView component.
- [react-native-inappbrowser](https://github.com/proyecto26/react-native-inappbrowser) [![GitHub stars](https://img.shields.io/github/stars/proyecto26/react-native-inappbrowser?style=flat)](https://github.com/proyecto26/react-native-inappbrowser/stargazers) - In-app browser using Chrome Custom Tabs and SFSafariViewController.
- [react-native-web](https://github.com/necolas/react-native-web) [![GitHub stars](https://img.shields.io/github/stars/necolas/react-native-web?style=flat)](https://github.com/necolas/react-native-web/stargazers) - Run React Native components and APIs on the web.
- [Solito](https://github.com/nandorojo/solito) [![GitHub stars](https://img.shields.io/github/stars/nandorojo/solito?style=flat)](https://github.com/nandorojo/solito/stargazers) - React Native + Next.js, unified navigation for universal apps.

### Other Platforms

- [react-native-windows](https://github.com/microsoft/react-native-windows) [![GitHub stars](https://img.shields.io/github/stars/microsoft/react-native-windows?style=flat)](https://github.com/microsoft/react-native-windows/stargazers) - Build native Windows apps with React.
- [react-native-macos](https://github.com/microsoft/react-native-macos) [![GitHub stars](https://img.shields.io/github/stars/microsoft/react-native-macos?style=flat)](https://github.com/microsoft/react-native-macos/stargazers) - Build native macOS apps with React.

## Data

### State Management

- [Zustand](https://github.com/pmndrs/zustand) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/zustand?style=flat)](https://github.com/pmndrs/zustand/stargazers) - Bear necessities for state management.
- [Jotai](https://github.com/pmndrs/jotai) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/jotai?style=flat)](https://github.com/pmndrs/jotai/stargazers) - Primitive and flexible atomic state.
- [Redux Toolkit](https://github.com/reduxjs/redux-toolkit) [![GitHub stars](https://img.shields.io/github/stars/reduxjs/redux-toolkit?style=flat)](https://github.com/reduxjs/redux-toolkit/stargazers) - The official, batteries-included Redux toolset.
- [Legend State](https://github.com/LegendApp/legend-state) [![GitHub stars](https://img.shields.io/github/stars/LegendApp/legend-state?style=flat)](https://github.com/LegendApp/legend-state/stargazers) - Super fast state with fine-grained reactivity and built-in sync.

### Storage & Databases

- [react-native-mmkv](https://github.com/mrousavy/react-native-mmkv) [![GitHub stars](https://img.shields.io/github/stars/mrousavy/react-native-mmkv?style=flat)](https://github.com/mrousavy/react-native-mmkv/stargazers) - The fastest key/value storage for React Native, ~30x faster than AsyncStorage.
- [AsyncStorage](https://github.com/react-native-async-storage/async-storage) [![GitHub stars](https://img.shields.io/github/stars/react-native-async-storage/async-storage?style=flat)](https://github.com/react-native-async-storage/async-storage/stargazers) - Simple, asynchronous, persistent key-value storage.
- [op-sqlite](https://github.com/OP-Engineering/op-sqlite) [![GitHub stars](https://img.shields.io/github/stars/OP-Engineering/op-sqlite?style=flat)](https://github.com/OP-Engineering/op-sqlite/stargazers) - The fastest SQLite library for React Native.
- [expo-sqlite](https://docs.expo.dev/versions/latest/sdk/sqlite/) - SQLite database access in Expo, with support for Drizzle ORM.
- [Drizzle ORM](https://github.com/drizzle-team/drizzle-orm) [![GitHub stars](https://img.shields.io/github/stars/drizzle-team/drizzle-orm?style=flat)](https://github.com/drizzle-team/drizzle-orm/stargazers) - TypeScript ORM with first-class Expo/React Native SQLite support.
- [WatermelonDB](https://github.com/Nozbe/WatermelonDB) [![GitHub stars](https://img.shields.io/github/stars/Nozbe/WatermelonDB?style=flat)](https://github.com/Nozbe/WatermelonDB/stargazers) - Reactive and asynchronous database for powerful apps that scale.
- [RxDB](https://github.com/pubkey/rxdb) [![GitHub stars](https://img.shields.io/github/stars/pubkey/rxdb?style=flat)](https://github.com/pubkey/rxdb/stargazers) - Local-first, reactive database that replicates with your backend.
- [Realm](https://github.com/realm/realm-js) [![GitHub stars](https://img.shields.io/github/stars/realm/realm-js?style=flat)](https://github.com/realm/realm-js/stargazers) - Mobile object database, an alternative to SQLite.

### Networking

- [TanStack Query](https://github.com/TanStack/query) [![GitHub stars](https://img.shields.io/github/stars/TanStack/query?style=flat)](https://github.com/TanStack/query/stargazers) - Powerful async state management and data fetching.
- [apisauce](https://github.com/infinitered/apisauce) [![GitHub stars](https://img.shields.io/github/stars/infinitered/apisauce?style=flat)](https://github.com/infinitered/apisauce/stargazers) - Axios with standardized errors and request/response transforms.
- [react-native-netinfo](https://github.com/react-native-netinfo/react-native-netinfo) [![GitHub stars](https://img.shields.io/github/stars/react-native-netinfo/react-native-netinfo?style=flat)](https://github.com/react-native-netinfo/react-native-netinfo/stargazers) - Network state and connectivity info.
- [react-native-network-logger](https://github.com/alexbrazier/react-native-network-logger) [![GitHub stars](https://img.shields.io/github/stars/alexbrazier/react-native-network-logger?style=flat)](https://github.com/alexbrazier/react-native-network-logger/stargazers) - In-app HTTP request monitor.
- [react-native-quick-crypto](https://github.com/margelo/react-native-quick-crypto) [![GitHub stars](https://img.shields.io/github/stars/margelo/react-native-quick-crypto?style=flat)](https://github.com/margelo/react-native-quick-crypto/stargazers) - Fast native implementation of Node's crypto module.

## Services & Integrations

- [react-native-firebase](https://github.com/invertase/react-native-firebase) [![GitHub stars](https://img.shields.io/github/stars/invertase/react-native-firebase?style=flat)](https://github.com/invertase/react-native-firebase/stargazers) - Well-tested, feature-rich modular Firebase implementation.
- [sentry-react-native](https://github.com/getsentry/sentry-react-native) [![GitHub stars](https://img.shields.io/github/stars/getsentry/sentry-react-native?style=flat)](https://github.com/getsentry/sentry-react-native/stargazers) - Official Sentry SDK for crash reporting and performance monitoring.
- [react-native-app-auth](https://github.com/FormidableLabs/react-native-app-auth) [![GitHub stars](https://img.shields.io/github/stars/FormidableLabs/react-native-app-auth?style=flat)](https://github.com/FormidableLabs/react-native-app-auth/stargazers) - PKCE-compliant OAuth2 client based on AppAuth.
- [google-signin](https://github.com/react-native-google-signin/google-signin) [![GitHub stars](https://img.shields.io/github/stars/react-native-google-signin/google-signin?style=flat)](https://github.com/react-native-google-signin/google-signin/stargazers) - Google Sign-In for React Native.

## Payments & Monetization

- [stripe-react-native](https://github.com/stripe/stripe-react-native) [![GitHub stars](https://img.shields.io/github/stars/stripe/stripe-react-native?style=flat)](https://github.com/stripe/stripe-react-native/stargazers) - Official Stripe SDK for payments in React Native.
- [react-native-purchases](https://github.com/RevenueCat/react-native-purchases) [![GitHub stars](https://img.shields.io/github/stars/RevenueCat/react-native-purchases?style=flat)](https://github.com/RevenueCat/react-native-purchases/stargazers) - RevenueCat SDK for in-app purchases and subscriptions.

## Development Tools

### Tooling & IDE

- [Radon IDE](https://github.com/software-mansion/radon-ide) [![GitHub stars](https://img.shields.io/github/stars/software-mansion/radon-ide?style=flat)](https://github.com/software-mansion/radon-ide/stargazers) - VSCode/Cursor extension that turns your editor into a full-featured React Native IDE with an embedded simulator.
- [EAS CLI](https://github.com/expo/eas-cli) [![GitHub stars](https://img.shields.io/github/stars/expo/eas-cli?style=flat)](https://github.com/expo/eas-cli/stargazers) - Build, submit, and update iOS and Android apps from the command line.
- [react-native-rename](https://github.com/junedomingo/react-native-rename) [![GitHub stars](https://img.shields.io/github/stars/junedomingo/react-native-rename?style=flat)](https://github.com/junedomingo/react-native-rename/stargazers) - Rename a React Native app with one command.
- [react-native-bundle-visualizer](https://github.com/callstack/react-native-bundle-visualizer) [![GitHub stars](https://img.shields.io/github/stars/callstack/react-native-bundle-visualizer?style=flat)](https://github.com/callstack/react-native-bundle-visualizer/stargazers) - See which packages inflate your bundle size.
- [Re.Pack](https://github.com/callstack/repack) [![GitHub stars](https://img.shields.io/github/stars/callstack/repack?style=flat)](https://github.com/callstack/repack/stargazers) - Webpack/Rspack-based toolkit with code splitting and Module Federation for React Native.

### Debugging

- [Reactotron](https://github.com/infinitered/reactotron) [![GitHub stars](https://img.shields.io/github/stars/infinitered/reactotron?style=flat)](https://github.com/infinitered/reactotron/stargazers) - Desktop app for inspecting React Native apps: state, API requests, performance.
- [Buoy](https://github.com/Buoy-gg/buoy) [![GitHub stars](https://img.shields.io/github/stars/Buoy-gg/buoy?style=flat)](https://github.com/Buoy-gg/buoy/stargazers) - Devtools that live in your app — and answer to your AI agent.

### Testing

- [Maestro](https://github.com/mobile-dev-inc/Maestro) [![GitHub stars](https://img.shields.io/github/stars/mobile-dev-inc/Maestro?style=flat)](https://github.com/mobile-dev-inc/Maestro/stargazers) - Painless declarative E2E automation for mobile.
- [Detox](https://github.com/wix/Detox) [![GitHub stars](https://img.shields.io/github/stars/wix/Detox?style=flat)](https://github.com/wix/Detox/stargazers) - Gray-box end-to-end testing and automation framework.
- [React Native Testing Library](https://github.com/callstack/react-native-testing-library) [![GitHub stars](https://img.shields.io/github/stars/callstack/react-native-testing-library?style=flat)](https://github.com/callstack/react-native-testing-library/stargazers) - Testing utilities that encourage good practices.
- [Loki](https://github.com/oblador/loki) [![GitHub stars](https://img.shields.io/github/stars/oblador/loki?style=flat)](https://github.com/oblador/loki/stargazers) - Visual regression testing for Storybook.

### Builds, Deployment & OTA Updates

- [EAS](https://expo.dev/eas) - Expo Application Services: cloud builds, app store submission, and OTA updates.
- [hot-updater](https://github.com/gronxb/hot-updater) [![GitHub stars](https://img.shields.io/github/stars/gronxb/hot-updater?style=flat)](https://github.com/gronxb/hot-updater/stargazers) - Self-hostable OTA update solution, a CodePush alternative.
- [Fastlane](https://fastlane.tools) - Automate building, screenshots, and releasing for iOS and Android.

### Building Libraries

- [create-react-native-library](https://github.com/callstack/react-native-builder-bob) [![GitHub stars](https://img.shields.io/github/stars/callstack/react-native-builder-bob?style=flat)](https://github.com/callstack/react-native-builder-bob/stargazers) - Scaffold and build React Native libraries for distribution.
- [Nitro Modules](https://github.com/mrousavy/nitro) [![GitHub stars](https://img.shields.io/github/stars/mrousavy/nitro?style=flat)](https://github.com/mrousavy/nitro/stargazers) - Insanely fast native C++, Swift, or Kotlin modules with statically compiled bindings.

## Starters & Boilerplates

- [Ignite](https://github.com/infinitered/ignite) [![GitHub stars](https://img.shields.io/github/stars/infinitered/ignite?style=flat)](https://github.com/infinitered/ignite/stargazers) - Infinite Red's battle-tested boilerplate with CLI and generators.
- [react-native-boilerplate](https://github.com/thecodingmachine/react-native-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/thecodingmachine/react-native-boilerplate?style=flat)](https://github.com/thecodingmachine/react-native-boilerplate/stargazers) - TheCodingMachine's template for solid, scalable applications.
- [Expo Templates](https://docs.expo.dev/more/create-expo/) - Official Expo templates, from blank to tabs to full navigation setups.

## Open Source Apps

Production apps you can learn from.

- [Bluesky](https://github.com/bluesky-social/social-app) [![GitHub stars](https://img.shields.io/github/stars/bluesky-social/social-app?style=flat)](https://github.com/bluesky-social/social-app/stargazers) - The Bluesky social app for web, iOS, and Android.
- [Expensify](https://github.com/Expensify/App) [![GitHub stars](https://img.shields.io/github/stars/Expensify/App?style=flat)](https://github.com/Expensify/App/stargazers) - New Expensify: financial collaboration, chat-centered.
- [Joplin](https://github.com/laurent22/joplin) [![GitHub stars](https://img.shields.io/github/stars/laurent22/joplin?style=flat)](https://github.com/laurent22/joplin/stargazers) - Privacy-focused note-taking app with sync, on every platform.
- [Mattermost](https://github.com/mattermost/mattermost-mobile) [![GitHub stars](https://img.shields.io/github/stars/mattermost/mattermost-mobile?style=flat)](https://github.com/mattermost/mattermost-mobile/stargazers) - Mattermost's mobile apps.
- [Rocket.Chat](https://github.com/RocketChat/Rocket.Chat.ReactNative) [![GitHub stars](https://img.shields.io/github/stars/RocketChat/Rocket.Chat.ReactNative?style=flat)](https://github.com/RocketChat/Rocket.Chat.ReactNative/stargazers) - Rocket.Chat's mobile client.
- [Artsy](https://github.com/artsy/eigen) [![GitHub stars](https://img.shields.io/github/stars/artsy/eigen?style=flat)](https://github.com/artsy/eigen/stargazers) - The art world in your pocket.
- [YouTrack Mobile](https://github.com/JetBrains/youtrack-mobile) [![GitHub stars](https://img.shields.io/github/stars/JetBrains/youtrack-mobile?style=flat)](https://github.com/JetBrains/youtrack-mobile/stargazers) - JetBrains' YouTrack client for iOS and Android.

## Learning

- [React Native Docs](https://reactnative.dev/docs/getting-started) - The official guides, always the right place to start.
- [Expo Tutorial](https://docs.expo.dev/tutorial/introduction/) - Official hands-on tutorial building a universal app.
- [React Native Express](https://www.reactnative.express) - Guided walkthrough of the React Native ecosystem.
- [Start React Native](https://start-react-native.dev) - William Candillon's in-depth course on gestures and animations.
- [Can it be done in React Native?](https://www.youtube.com/@wcandillon) - William Candillon's YouTube series rebuilding famous UIs.

## Staying Up to Date

- [This Week In React](https://thisweekinreact.com) - Weekly newsletter covering React and React Native.
- [React Native Newsletter](https://reactnativenewsletter.com) - Occasional newsletter of React Native news and articles.
- [React Native Radio](https://reactnativeradio.com) - The long-running React Native podcast, by Infinite Red.
- [Chain React](https://chainreactconf.com) - The US React Native conference, Portland, OR.
- [App.js Conf](https://appjs.co) - Expo and React Native conference, Kraków, Poland.
- [React Universe Conf](https://www.reactuniverseconf.com) - Callstack's conference (formerly React Native EU), Wrocław, Poland.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first: entries should be actively maintained, work with current React Native, and be genuinely useful to most developers.

Many thanks to everyone on the [contributor list](https://github.com/jondot/awesome-react-native/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/jondot/awesome-react-native/graphs/contributors?style=flat)](https://github.com/jondot/awesome-react-native/graphs/contributors/stargazers) :)
