# Browserify

> 来源：[browserify/awesome-browserify](https://github.com/browserify/awesome-browserify)

[![GitHub stars](https://img.shields.io/github/stars/browserify/awesome-browserify?style=flat)](https://github.com/browserify/awesome-browserify/stargazers)

<div align="center"><img src="browserify.png" alt="Browserify!"></div>

# Awesome Browserify [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> :crystal_ball: A curated list of awesome [Browserify](https://github.com/substack/node-browserify) [![GitHub stars](https://img.shields.io/github/stars/substack/node-browserify?style=flat)](https://github.com/substack/node-browserify/stargazers) resources, libraries, and tools.

Please help improve this list by [contributing](contributing.md)!

## Contents

- [About](#about)
- [Official Resources](#official-resources)
- [Community Resources](#community-resources)
- [Tutorials](#tutorials)
- [Articles](#articles)
- [Demos](#demos)
- [Videos](#videos)
- [Tools](#tools)
  - [Development Servers](#development-servers)
  - [Plugins](#plugins)
  - [Watchers](#watchers)
  - [CSS Bundlers](#css-bundlers)
  - [Transforms](#transforms)
  - [Node in the Browser](#node-in-the-browser)
  - [Production Tools](#production-tools)

## About

Browserify lets you `require('modules')` in the browser by bundling up all of your dependencies.

You can use a node-style `require()` to organize your browser code and load modules installed by npm. Browserify will recursively analyze all the `require()` calls in your app in order to build a bundle you can serve up to the browser in a single `<script>` tag.

## Official Resources

- [Docs](https://github.com/substack/node-browserify#usage) [![GitHub stars](https://img.shields.io/github/stars/substack/node-browserify?style=flat)](https://github.com/substack/node-browserify/stargazers)
- [Handbook](https://github.com/substack/browserify-handbook) [![GitHub stars](https://img.shields.io/github/stars/substack/browserify-handbook?style=flat)](https://github.com/substack/browserify-handbook/stargazers)
- [Repo](https://github.com/substack/node-browserify) [![GitHub stars](https://img.shields.io/github/stars/substack/node-browserify?style=flat)](https://github.com/substack/node-browserify/stargazers)
- [Website](http://browserify.org/)

## Community Resources

- [IRC](http://webchat.freenode.net/?channels=browserify)
- [Twitter](http://twitter.com/browserify)
- [StackOverflow](http://stackoverflow.com/questions/tagged/browserify)

## Tutorials

- [Hello World with Browserify](http://browserify.org/#middle-section)
- [Browserify Adventure](https://github.com/workshopper/browserify-adventure) [![GitHub stars](https://img.shields.io/github/stars/workshopper/browserify-adventure?style=flat)](https://github.com/workshopper/browserify-adventure/stargazers)
- [A Gentle Browserify Walkthrough](https://ponyfoo.com/articles/a-gentle-browserify-walkthrough)
- [Browserify guide](http://zhaoda.net/2015/10/16/browserify-guide/) (Chinese)

## Articles

- [Introduction to Browserify](https://writingjavascript.org/posts/introduction-to-browserify)
- [Using npm on the client side](http://dontkry.com/posts/code/using-npm-on-the-client-side.html)
- [How Browserify Works](http://benclinkinbeard.com/posts/how-browserify-works/)
- [Gulp + Browserify: The Everything Post](https://www.viget.com/articles/gulp-browserify-starter-faq)
- [Browserify vs Component](http://www.forbeslindesay.co.uk/post/44144487088/browserify-vs-component)
- [Browserify for Webpack users](https://gist.github.com/substack/68f8d502be42d5cd4942)
- [Browserify vs. Webpack](https://mattdesl.svbtle.com/browserify-vs-webpack)

## Demos

- [Canvas Splitter](http://requirebin.com/?gist=maxogden/9576799) by [hughsk](http://github.com/hughsk)
- [Infinite 2D Cave Generator](http://requirebin.com/?gist=maxogden/9557700) by [hughsk](http://github.com/hughsk)
- [2D Velocity Control](http://requirebin.com/?gist=maxogden/9557776) by [sethvincent](http://github.com/sethvincent)

## Videos

- [James Halliday (substack) - LXJS 2013 - Modularidade para todos](https://www.youtube.com/watch?v=DCQNm6yiZh0)
- [Getting Started with Browserify](https://www.youtube.com/watch?v=CTAa8IcQh1U) by [shama](https://github.com/shama/) [![GitHub stars](https://img.shields.io/github/stars/shama/?style=flat)](https://github.com/shama//stargazers)
- [Transform your Bundles with Browserify](https://www.youtube.com/watch?v=Uk2bgp8OLT8) by [shama](https://github.com/shama/) [![GitHub stars](https://img.shields.io/github/stars/shama/?style=flat)](https://github.com/shama//stargazers)

## Tools

### Development Servers

- [budo](https://github.com/mattdesl/budo) [![GitHub stars](https://img.shields.io/github/stars/mattdesl/budo?style=flat)](https://github.com/mattdesl/budo/stargazers) - Dev server for rapid prototyping.
- [beefy](https://github.com/chrisdickinson/beefy) [![GitHub stars](https://img.shields.io/github/stars/chrisdickinson/beefy?style=flat)](https://github.com/chrisdickinson/beefy/stargazers) - Local development server that aims to make using browserify fast and fun.
- [wzrd](https://github.com/maxogden/wzrd) [![GitHub stars](https://img.shields.io/github/stars/maxogden/wzrd?style=flat)](https://github.com/maxogden/wzrd/stargazers) - Super minimal browserify development server.

### Plugins

- [browserify-hmr](https://github.com/AgentME/browserify-hmr) [![GitHub stars](https://img.shields.io/github/stars/AgentME/browserify-hmr?style=flat)](https://github.com/AgentME/browserify-hmr/stargazers) - Hot Module Replacement plugin for Browserify.

### Watchers

- [watchify](https://github.com/substack/watchify) [![GitHub stars](https://img.shields.io/github/stars/substack/watchify?style=flat)](https://github.com/substack/watchify/stargazers) - Watch mode for browserify builds.
- [persistify](https://github.com/royriojas/persistify) [![GitHub stars](https://img.shields.io/github/stars/royriojas/persistify?style=flat)](https://github.com/royriojas/persistify/stargazers) - Wrapper around `browserify` to make incremental builds.

### CSS bundlers

- [sheetify](https://github.com/stackcss/sheetify) [![GitHub stars](https://img.shields.io/github/stars/stackcss/sheetify?style=flat)](https://github.com/stackcss/sheetify/stargazers) - Modular CSS bundler for browserify.
- [parcelify](https://github.com/rotundasoftware/parcelify) [![GitHub stars](https://img.shields.io/github/stars/rotundasoftware/parcelify?style=flat)](https://github.com/rotundasoftware/parcelify/stargazers) - Add css to your npm modules consumed with browserify.
- [css-modulesify](https://github.com/css-modules/css-modulesify) [![GitHub stars](https://img.shields.io/github/stars/css-modules/css-modulesify?style=flat)](https://github.com/css-modules/css-modulesify/stargazers) - Browserify plugin to load CSS Modules.

### Transforms

- [babelify](https://github.com/babel/babelify) [![GitHub stars](https://img.shields.io/github/stars/babel/babelify?style=flat)](https://github.com/babel/babelify/stargazers) - Browserify transform for babel.
- [aliasify](https://github.com/benbria/aliasify) [![GitHub stars](https://img.shields.io/github/stars/benbria/aliasify?style=flat)](https://github.com/benbria/aliasify/stargazers) - Remap require calls at build time.
- [brfs](https://github.com/substack/brfs) [![GitHub stars](https://img.shields.io/github/stars/substack/brfs?style=flat)](https://github.com/substack/brfs/stargazers) - `fs.readFileSync()` and `fs.readFile()` static asset browserify transform.

### Node in the Browser

- [crypto-browserify](https://github.com/crypto-browserify/crypto-browserify) [![GitHub stars](https://img.shields.io/github/stars/crypto-browserify/crypto-browserify?style=flat)](https://github.com/crypto-browserify/crypto-browserify/stargazers) - Port of node's `crypto` module to the browser.
- [stream-browserify](https://github.com/substack/stream-browserify) [![GitHub stars](https://img.shields.io/github/stars/substack/stream-browserify?style=flat)](https://github.com/substack/stream-browserify/stargazers) - The `stream` module from node core, for browsers!
- [buffer](https://github.com/feross/buffer) [![GitHub stars](https://img.shields.io/github/stars/feross/buffer?style=flat)](https://github.com/feross/buffer/stargazers) - The `buffer` module from node.js, for the browser.
- [requirebin](http://requirebin.com/) - Write browser JavaScript programs using modules from NPM.

### Production Tools

- [wzrd.in](https://wzrd.in/) - Browserify CDN. Browserify-as-a-Service!
- [bankai](https://github.com/yoshuawuyts/bankai) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/bankai?style=flat)](https://github.com/yoshuawuyts/bankai/stargazers) - DIY asset server. Serves HTML, CSS and JS as streams.

## Contributing

Contributions welcome! Please read the [contributing guidelines](contributing.md) before getting started.

## License

The [browserify logo](browserify.png) is by [substack](https://github.com/substack) [![GitHub stars](https://img.shields.io/github/stars/substack?style=flat)](https://github.com/substack/stargazers).

All other content is released to the public domain under [CC0-1.0](https://spdx.org/licenses/CC0-1.0.html).

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
