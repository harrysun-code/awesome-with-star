# WebExtensions

> 来源：[fregante/Awesome-WebExtensions](https://github.com/fregante/Awesome-WebExtensions)

[![GitHub stars](https://img.shields.io/github/stars/fregante/Awesome-WebExtensions?style=flat)](https://github.com/fregante/Awesome-WebExtensions/stargazers)

# Awesome WebExtensions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome resources for WebExtensions development.

WebExtensions are a cross-browser system for developing browser add-ons. To a large extent the system is compatible with the extension API supported by Google Chrome. Extensions written for this browser will in most cases run in Firefox with just [a few changes](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Porting_a_Google_Chrome_extension).

Follow [@fregante](https://fregante.com) for more webext-related news.

## Contents

- [Getting started](#getting-started)
- [Community](#community)
- [Libraries and Frameworks](#libraries-and-frameworks)
- [Tools](#tools)
- [Testing](#testing)
- [Boilerplates](#boilerplates)
- [Sample Extensions](#sample-extensions)

## Getting started

- [Chrome Extensions documentation](https://developer.chrome.com/docs/extensions/reference) - Documentation for the original Chrome extension model.
- [Mozilla's WebExtensions documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) - MDN wiki for the WebExtensions API.
- [Browser support for WebExtensions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs) - Compatibility table for Chrome, Edge, Firefox, and Opera.
- [Safari Extensions documentation](https://developer.apple.com/safari/extensions/) - Developer documentation on building Safari extensions. Technically not WebExtensions, the API is completely different.
- [Opera API support](https://dev.opera.com/extensions/apis/) - Detailed WebExtensions support for Opera.
- [Browser Extension Standard](https://browserext.github.io/browserext/) - Standard for the API, supported by Mozilla, Opera and Microsoft.

## Community

- [Google Groups](https://groups.google.com/a/chromium.org/forum/#!forum/chromium-extensions) - Discussions.
- [Mozilla Discourse](https://discourse.mozilla.org/c/add-ons) - Discussions.
- [`#addons:mozilla.org`](https://matrix.to/#/#addons:mozilla.org) - Matrix channel by Mozilla.
- [`google-chrome-extension` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/google-chrome-extension) - Relevant questions.
- [`firefox-addon-webextensions` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/firefox-addon-webextensions) - Relevant questions.
- [`microsoft-edge-extension` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/microsoft-edge-extension) - Relevant questions.

## Libraries and Frameworks

Code meant become part of the extension.

- [webext-options-sync](https://github.com/fregante/webext-options-sync) [![GitHub stars](https://img.shields.io/github/stars/fregante/webext-options-sync?style=flat)](https://github.com/fregante/webext-options-sync/stargazers) - Helps you manage and autosave your extension's options.
- [webext-storage-cache](https://github.com/fregante/webext-storage-cache) [![GitHub stars](https://img.shields.io/github/stars/fregante/webext-storage-cache?style=flat)](https://github.com/fregante/webext-storage-cache/stargazers) - Map-like promised cache storage with expiration.
- [webext-dynamic-content-scripts](https://github.com/fregante/webext-dynamic-content-scripts) [![GitHub stars](https://img.shields.io/github/stars/fregante/webext-dynamic-content-scripts?style=flat)](https://github.com/fregante/webext-dynamic-content-scripts/stargazers) - Automatically inject your `content_scripts` on custom domains.
- [mozilla/webextension-polyfill](https://github.com/mozilla/webextension-polyfill) [![GitHub stars](https://img.shields.io/github/stars/mozilla/webextension-polyfill?style=flat)](https://github.com/mozilla/webextension-polyfill/stargazers) - Polyfill to support the standardized promise based API in the `browser` namespace.
- [@types/firefox-webext-browser](https://www.npmjs.com/package/@types/firefox-webext-browser) - Supplies TypeScript types for the `browser` namespace.
- [redux-webext](https://github.com/ivantsov/redux-webext) [![GitHub stars](https://img.shields.io/github/stars/ivantsov/redux-webext?style=flat)](https://github.com/ivantsov/redux-webext/stargazers) - Uses Redux for managing the state of your WebExtension.
- [ExtPay](https://github.com/Glench/ExtPay) [![GitHub stars](https://img.shields.io/github/stars/Glench/ExtPay?style=flat)](https://github.com/Glench/ExtPay/stargazers) - Take secure payments in extensions without needing to run a server backend.
- [inject-react-anywhere](https://github.com/OlegWock/inject-react-anywhere) [![GitHub stars](https://img.shields.io/github/stars/OlegWock/inject-react-anywhere?style=flat)](https://github.com/OlegWock/inject-react-anywhere/stargazers) - Inject React components into 3rd party sites with convenient API and styles isolation.
- [More…](https://github.com/fregante/webext-fun) [![GitHub stars](https://img.shields.io/github/stars/fregante/webext-fun?style=flat)](https://github.com/fregante/webext-fun/stargazers)

## Tools

Apps that help you manage your extensions.

- [Chrome Webstore Upload](https://github.com/fregante/chrome-webstore-upload-cli) [![GitHub stars](https://img.shields.io/github/stars/fregante/chrome-webstore-upload-cli?style=flat)](https://github.com/fregante/chrome-webstore-upload-cli/stargazers) - Upload the extension to the Chrome Web Store via cli (or on GitHub Actions, automatically).
- [mozilla/web-ext](https://github.com/mozilla/web-ext) [![GitHub stars](https://img.shields.io/github/stars/mozilla/web-ext?style=flat)](https://github.com/mozilla/web-ext/stargazers) - Command line tool to help build, run, and test WebExtensions.
- [chromepet](https://github.com/ZenHubIO/chromepet) [![GitHub stars](https://img.shields.io/github/stars/ZenHubIO/chromepet?style=flat)](https://github.com/ZenHubIO/chromepet/stargazers) - Get notified when your new version has been published.
- [chrome-ext-downloader](https://github.com/jiripospisil/chrome-ext-downloader) [![GitHub stars](https://img.shields.io/github/stars/jiripospisil/chrome-ext-downloader?style=flat)](https://github.com/jiripospisil/chrome-ext-downloader/stargazers) - Download any extension on Chrome Web Store to see how they do it.
- [chrome-store-api](https://github.com/acvetkov/chrome-store-api) [![GitHub stars](https://img.shields.io/github/stars/acvetkov/chrome-store-api?style=flat)](https://github.com/acvetkov/chrome-store-api/stargazers) - Chrome Web Store API wrapper.
- [Chrome extension source viewer](https://github.com/Rob--W/crxviewer) [![GitHub stars](https://img.shields.io/github/stars/Rob--W/crxviewer?style=flat)](https://github.com/Rob--W/crxviewer/stargazers) - WebExtension to view source code of extensions directly on the store.
- [@wext/shipit](https://github.com/LinusU/wext-shipit) [![GitHub stars](https://img.shields.io/github/stars/LinusU/wext-shipit?style=flat)](https://github.com/LinusU/wext-shipit/stargazers) - Tool to automatically publish to Chrome Web Store, Mozilla Addons and Opera Addons.
- [wext-manifest-loader](https://github.com/abhijithvijayan/wext-manifest-loader) [![GitHub stars](https://img.shields.io/github/stars/abhijithvijayan/wext-manifest-loader?style=flat)](https://github.com/abhijithvijayan/wext-manifest-loader/stargazers) - Webpack loader that lets you specify `manifest.json` properties to appear only in specific browsers.
- [webextension-manifest-loader](https://github.com/jsmnbom/webextension-manifest-loader) [![GitHub stars](https://img.shields.io/github/stars/jsmnbom/webextension-manifest-loader?style=flat)](https://github.com/jsmnbom/webextension-manifest-loader/stargazers) - Webpack loader that loads browser tailored manifest.json. It also imports all importable properties, allowing you to have 'manifest.json' as your only webpack entry point.
- [webpack-extension-reloader](https://github.com/rubenspgcavalcante/webpack-extension-reloader) [![GitHub stars](https://img.shields.io/github/stars/rubenspgcavalcante/webpack-extension-reloader?style=flat)](https://github.com/rubenspgcavalcante/webpack-extension-reloader/stargazers) - A Webpack plugin to automatically reload browser extensions during development.
- [webpack-target-webextension](https://github.com/awesome-webextension/webpack-target-webextension) [![GitHub stars](https://img.shields.io/github/stars/awesome-webextension/webpack-target-webextension?style=flat)](https://github.com/awesome-webextension/webpack-target-webextension/stargazers) - Adds code-splitting support to WebExtensions build with Webpack.
- [Extension.js](https://github.com/cezaraugusto/extension.js) [![GitHub stars](https://img.shields.io/github/stars/cezaraugusto/extension.js?style=flat)](https://github.com/cezaraugusto/extension.js/stargazers) - Plug-and-play, zero-config, cross-browser extension development tool.

## Testing

- [sinon-chrome](https://github.com/acvetkov/sinon-chrome) [![GitHub stars](https://img.shields.io/github/stars/acvetkov/sinon-chrome?style=flat)](https://github.com/acvetkov/sinon-chrome/stargazers) - Mocks the Chrome Extensions API for testing.
- [addons-linter](https://github.com/mozilla/addons-linter) [![GitHub stars](https://img.shields.io/github/stars/mozilla/addons-linter?style=flat)](https://github.com/mozilla/addons-linter/stargazers) - Validate an extension against Mozilla's guidelines.
- [webextensions-jsdom](https://github.com/stoically/webextensions-jsdom) [![GitHub stars](https://img.shields.io/github/stars/stoically/webextensions-jsdom?style=flat)](https://github.com/stoically/webextensions-jsdom/stargazers) - Load popup, sidebar and background with JSDOM based on the manifest.json.
- [webextensions-api-fake](https://github.com/stoically/webextensions-api-fake) [![GitHub stars](https://img.shields.io/github/stars/stoically/webextensions-api-fake?style=flat)](https://github.com/stoically/webextensions-api-fake/stargazers) - In-memory WebExtensions API Fake Implementation (includes TypeScript types).
- [webextensions-api-mock](https://github.com/stoically/webextensions-api-mock) [![GitHub stars](https://img.shields.io/github/stars/stoically/webextensions-api-mock?style=flat)](https://github.com/stoically/webextensions-api-mock/stargazers) - WebExtensions API as sinon stubs (includes TypeScript types).
- [webextensions-schema](https://github.com/stoically/webextensions-schema) [![GitHub stars](https://img.shields.io/github/stars/stoically/webextensions-schema?style=flat)](https://github.com/stoically/webextensions-schema/stargazers) - Programmatically consume the WebExtensions Schema JSON files.

## Boilerplates

- [browser-extension-template](https://github.com/fregante/browser-extension-template) [![GitHub stars](https://img.shields.io/github/stars/fregante/browser-extension-template?style=flat)](https://github.com/fregante/browser-extension-template/stargazers) - Barebones boilerplate with parcel, options handler and auto-publishing.
- [create-webextension](https://github.com/rpl/create-webextension) [![GitHub stars](https://img.shields.io/github/stars/rpl/create-webextension?style=flat)](https://github.com/rpl/create-webextension/stargazers) - Yarn WebExtension generator.
- [generator-web-extension](https://github.com/webextension-toolbox/generator-web-extension) [![GitHub stars](https://img.shields.io/github/stars/webextension-toolbox/generator-web-extension?style=flat)](https://github.com/webextension-toolbox/generator-web-extension/stargazers) - WebExtension generator that creates everything you need to get started with cross-browser web-extension development.
- [WXT](https://github.com/wxt-dev/wxt) [![GitHub stars](https://img.shields.io/github/stars/wxt-dev/wxt?style=flat)](https://github.com/wxt-dev/wxt/stargazers) - Next-gen framework for developing web extensions

## Sample Extensions

These are simple and modern WebExtensions repositories that could help you figure out where pieces go, including automatic deployment via GitHub Actions.

- [npmhub](https://github.com/npmhub/npmhub) [![GitHub stars](https://img.shields.io/github/stars/npmhub/npmhub?style=flat)](https://github.com/npmhub/npmhub/stargazers)
- [Hide Files on GitHub](https://github.com/sindresorhus/hide-files-on-github) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/hide-files-on-github?style=flat)](https://github.com/sindresorhus/hide-files-on-github/stargazers)
- [mdn/webextension-examples](https://github.com/mdn/webextensions-examples) [![GitHub stars](https://img.shields.io/github/stars/mdn/webextensions-examples?style=flat)](https://github.com/mdn/webextensions-examples/stargazers) - Various example extensions curated for the MDN documentation.
