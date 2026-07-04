# Chrome DevTools

> 来源：[ChromeDevTools/awesome-chrome-devtools](https://github.com/ChromeDevTools/awesome-chrome-devtools)

[![GitHub stars](https://img.shields.io/github/stars/ChromeDevTools/awesome-chrome-devtools?style=flat)](https://github.com/ChromeDevTools/awesome-chrome-devtools/stargazers)

# Awesome Chrome DevTools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Awesome tooling and resources in the Chrome DevTools ecosystem

## Contents

- [Learning](#learning)
- [DevTools tooling and ecosystem](#devtools-tooling-and-ecosystem)
- [Chrome DevTools Protocol](#chrome-devtools-protocol)
- [Using DevTools frontend with other platforms](#using-devtools-frontend-with-other-platforms)
- [Applications](#applications)
- [DevTools Extensions](#devtools-extensions)
- [Alumni](#alumni)

---

## Learning
- [Dev Tips](https://umaar.com/dev-tips/) - Large collection of tips as animated gifs.
- [DevTools Tips](https://devtoolstips.org/) - Collection of illustrated tips as mini tutorials.
- [Can I DevTools?](https://www.canidev.tools/) - Various workflows, documented. Also a weekly tips & tricks [newsletter](https://canidevtools.substack.com/).
- [Web cheatcodes](https://codepo8.github.io/web-cheatcodes/) - Browser developer tools for non-developers.
- [Dear Console](https://codepo8.github.io/dearconsole) - A collection of snippets to use in the browser console.
- [Chrome Secret Menus](https://github.com/sparkyrider/chrome-secret-menus) [![GitHub stars](https://img.shields.io/github/stars/sparkyrider/chrome-secret-menus?style=flat)](https://github.com/sparkyrider/chrome-secret-menus/stargazers) - Comprehensive guide to internal pages and diagnostic tools in Chrome.
- [Front-end Debugging Tools Handbook](https://github.com/lala-hakobyan/front-end-debugging-handbook) [![GitHub stars](https://img.shields.io/github/stars/lala-hakobyan/front-end-debugging-handbook?style=flat)](https://github.com/lala-hakobyan/front-end-debugging-handbook/stargazers) - Practical guide to mastering front-end debugging tools, from Chrome DevTools and framework extensions to AI-enhanced IDE debugging.

---

## DevTools tooling and ecosystem

### Object formatting
- [immutable-devtools](https://github.com/andrewdavey/immutable-devtools) [![GitHub stars](https://img.shields.io/github/stars/andrewdavey/immutable-devtools?style=flat)](https://github.com/andrewdavey/immutable-devtools/stargazers) - Custom formatter for Immutable-js values.

### Network Inspection
- [betwixt](https://github.com/kdzwinel/betwixt) [![GitHub stars](https://img.shields.io/github/stars/kdzwinel/betwixt?style=flat)](https://github.com/kdzwinel/betwixt/stargazers) - System level network proxy, providing inspection via Network panel.

### CPU profile
- [call-trace](https://github.com/brendankenny/call-trace) [![GitHub stars](https://img.shields.io/github/stars/brendankenny/call-trace?style=flat)](https://github.com/brendankenny/call-trace/stargazers) - Can instrument your JS with hooks, and then generate a `.cpuprofile`  of the of the complete (non-sampled) execution. View either time or call counts.
- [cpuprofilify](https://github.com/thlorenz/cpuprofilify) [![GitHub stars](https://img.shields.io/github/stars/thlorenz/cpuprofilify?style=flat)](https://github.com/thlorenz/cpuprofilify/stargazers) - Converts output of various profiling/sampling tools to the `.cpuprofile` format.
- [Wishbone Python framework](https://wishbone.readthedocs.io/en/latest/misc/profiling.html) - Profiling data can export as `.cpuprofile`.

### Multimedia
- [snapline](https://github.com/pmdartus/snapline) [![GitHub stars](https://img.shields.io/github/stars/pmdartus/snapline?style=flat)](https://github.com/pmdartus/snapline/stargazers) - Converts timeline screenshots to gif.

### Timeline, Tracing & Profiling
- [DevTools Timeline Viewer](https://chromedevtools.github.io/timeline-viewer/) - Share URLs of your timeline recordings.

### Chrome Debugger integration with Editors
- [VS Code - Debugger for Chrome](https://github.com/Microsoft/vscode-chrome-debug/) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/vscode-chrome-debug/?style=flat)](https://github.com/Microsoft/vscode-chrome-debug//stargazers) - Breakpoint debugging in VS Code.
- [VS Code - Elements for Microsoft Edge](https://github.com/microsoft/vscode-edge-devtools) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode-edge-devtools?style=flat)](https://github.com/microsoft/vscode-edge-devtools/stargazers) - Elements panel inside VS Code.
- [ChromeREPL](https://github.com/acarabott/ChromeREPL) [![GitHub stars](https://img.shields.io/github/stars/acarabott/ChromeREPL?style=flat)](https://github.com/acarabott/ChromeREPL/stargazers) - Within Sublime Text, use the Chrome console.
- [Sublime Web Inspector](http://sokolovstas.github.io/SublimeWebInspector/) - JavaScript Breakpoint debugging right in Sublime Text.
- [WebStorm/JetBrains Chrome Extension](https://www.jetbrains.com/help/webstorm/2017.1/configuring-javascript-debugger-and-jetbrains-chrome-extension.html) - The WebStorm IDE can debug JavaScript, view the DOM tree, and edit HTML, CSS and JS live.

---

## Chrome DevTools Protocol
- [ChromeDevTools/devtools-protocol](https://github.com/chromedevtools/devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/chromedevtools/devtools-protocol?style=flat)](https://github.com/chromedevtools/devtools-protocol/stargazers) - **Canonical location of the protocol JSON**. Issue tracker for protocol bugs. TypeScript types.
- [DevTools Protocol API Docs](https://chromedevtools.github.io/devtools-protocol/) - Easy browsable UI for exploring the protocol's domains, methods and events.

### Developing with the protocol
- [chrome-remote-interface Wiki](https://github.com/cyrus-and/chrome-remote-interface/wiki) - Many useful recipes.
- [Chrome Protocol Proxy](https://github.com/wendigo/chrome-protocol-proxy) [![GitHub stars](https://img.shields.io/github/stars/wendigo/chrome-protocol-proxy?style=flat)](https://github.com/wendigo/chrome-protocol-proxy/stargazers) - Tool for debugging clients using devtools protocol.

### The big two automation libraries
- [Puppeteer](https://github.com/GoogleChrome/puppeteer/) [![GitHub stars](https://img.shields.io/github/stars/GoogleChrome/puppeteer/?style=flat)](https://github.com/GoogleChrome/puppeteer//stargazers) - Node.js offering a high-level API to control headless Chrome over the DevTools Protocol. See also [awesome-puppeteer](https://github.com/transitive-bullshit/awesome-puppeteer) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/awesome-puppeteer?style=flat)](https://github.com/transitive-bullshit/awesome-puppeteer/stargazers).
- [Playwright](https://github.com/microsoft/playwright) [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright?style=flat)](https://github.com/microsoft/playwright/stargazers) - Library to automate Chromium, Firefox and WebKit with a single API. Available for Node.js, Python, .Net, Java. See also [awesome-playwright](https://github.com/mxschmitt/awesome-playwright) [![GitHub stars](https://img.shields.io/github/stars/mxschmitt/awesome-playwright?style=flat)](https://github.com/mxschmitt/awesome-playwright/stargazers).

### Libraries for driving the protocol (or a layer above)

- JavaScript/Node.js: [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) [![GitHub stars](https://img.shields.io/github/stars/cyrus-and/chrome-remote-interface?style=flat)](https://github.com/cyrus-and/chrome-remote-interface/stargazers)
- TypeScript/Node.js: [chrome-debugging-client](https://github.com/TracerBench/chrome-debugging-client) [![GitHub stars](https://img.shields.io/github/stars/TracerBench/chrome-debugging-client?style=flat)](https://github.com/TracerBench/chrome-debugging-client/stargazers)
- TypeScript/Node.js: [noice-json-rpc](https://www.npmjs.com/package/noice-json-rpc) - A proxy-based implementation to expose the CDP as its API.
- TypeScript/Node.js: [Taiko](https://github.com/getgauge/taiko/) [![GitHub stars](https://img.shields.io/github/stars/getgauge/taiko/?style=flat)](https://github.com/getgauge/taiko//stargazers)
- TypeScript/Node.js: [Lumen](https://github.com/omxyz/lumen) [![GitHub stars](https://img.shields.io/github/stars/omxyz/lumen?style=flat)](https://github.com/omxyz/lumen/stargazers) - Vision-first browser agent with self-healing deterministic replay over CDP.
- Rust: [Rust Headless Chrome](https://github.com/atroche/rust-headless-chrome/) [![GitHub stars](https://img.shields.io/github/stars/atroche/rust-headless-chrome/?style=flat)](https://github.com/atroche/rust-headless-chrome//stargazers)
- Java: [chrome-devtools-java-client](https://github.com/kklisura/chrome-devtools-java-client) [![GitHub stars](https://img.shields.io/github/stars/kklisura/chrome-devtools-java-client?style=flat)](https://github.com/kklisura/chrome-devtools-java-client/stargazers)
- Java: [jvppeteer](https://github.com/fanyong920/jvppeteer) [![GitHub stars](https://img.shields.io/github/stars/fanyong920/jvppeteer?style=flat)](https://github.com/fanyong920/jvppeteer/stargazers)  - Headless Chrome For Java 
- Python: [PyCDP](https://github.com/hyperiongray/python-chrome-devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/hyperiongray/python-chrome-devtools-protocol?style=flat)](https://github.com/hyperiongray/python-chrome-devtools-protocol/stargazers) - Pure-Python, sans-IO wrappers. See also the [Trio CDP driver](https://github.com/hyperiongray/trio-chrome-devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/hyperiongray/trio-chrome-devtools-protocol?style=flat)](https://github.com/hyperiongray/trio-chrome-devtools-protocol/stargazers)
- Python: [chromewhip](https://github.com/chuckus/chromewhip) [![GitHub stars](https://img.shields.io/github/stars/chuckus/chromewhip?style=flat)](https://github.com/chuckus/chromewhip/stargazers) - drop-in replacement for the `splash` service
- Python: [pyppeteer](https://github.com/pyppeteer/pyppeteer) [![GitHub stars](https://img.shields.io/github/stars/pyppeteer/pyppeteer?style=flat)](https://github.com/pyppeteer/pyppeteer/stargazers) - Puppeteer port
- Python: [ChromeController](https://github.com/fake-name/ChromeController) [![GitHub stars](https://img.shields.io/github/stars/fake-name/ChromeController?style=flat)](https://github.com/fake-name/ChromeController/stargazers) - high-level browser mgmt
- Go: [chromedp](https://github.com/chromedp/chromedp) [![GitHub stars](https://img.shields.io/github/stars/chromedp/chromedp?style=flat)](https://github.com/chromedp/chromedp/stargazers) - High-level actions and tasks for driving browsers
- Go: [cdp](https://github.com/mafredri/cdp) [![GitHub stars](https://img.shields.io/github/stars/mafredri/cdp?style=flat)](https://github.com/mafredri/cdp/stargazers)
- Go: [gcd](https://github.com/wirepair/gcd) [![GitHub stars](https://img.shields.io/github/stars/wirepair/gcd?style=flat)](https://github.com/wirepair/gcd/stargazers)
- Go: [godet](https://github.com/raff/godet) [![GitHub stars](https://img.shields.io/github/stars/raff/godet?style=flat)](https://github.com/raff/godet/stargazers)
- Go: [Rod](https://github.com/go-rod/rod) [![GitHub stars](https://img.shields.io/github/stars/go-rod/rod?style=flat)](https://github.com/go-rod/rod/stargazers)
- C#/.NET: [Puppeteer Sharp](https://github.com/hardkoded/puppeteer-sharp) [![GitHub stars](https://img.shields.io/github/stars/hardkoded/puppeteer-sharp?style=flat)](https://github.com/hardkoded/puppeteer-sharp/stargazers) - Puppeteer port
- C#/dotnet: [chrome-dev-tools](https://github.com/BaristaLabs/chrome-dev-tools) [![GitHub stars](https://img.shields.io/github/stars/BaristaLabs/chrome-dev-tools?style=flat)](https://github.com/BaristaLabs/chrome-dev-tools/stargazers) - Protocol wrapper generator that can be customized by editing handlebars templates. Includes .Net Core template.
- C#/.NET: [dotnet-chrome-protocol](https://github.com/seclerp/dotnet-chrome-protocol) [![GitHub stars](https://img.shields.io/github/stars/seclerp/dotnet-chrome-protocol?style=flat)](https://github.com/seclerp/dotnet-chrome-protocol/stargazers) - A runtime library and schema code generation tools for Chrome DevTools Protocol support in C#/.NET.
- Ruby: [Ferrum](https://github.com/route/ferrum) [![GitHub stars](https://img.shields.io/github/stars/route/ferrum?style=flat)](https://github.com/route/ferrum/stargazers) - high-level API to control Chrome in Ruby
- Ruby: [Cuprite](https://github.com/machinio/cuprite) [![GitHub stars](https://img.shields.io/github/stars/machinio/cuprite?style=flat)](https://github.com/machinio/cuprite/stargazers) - Capybara driver
- Kotlin: [chrome-reactive-kotlin](https://github.com/wendigo/chrome-reactive-kotlin) [![GitHub stars](https://img.shields.io/github/stars/wendigo/chrome-reactive-kotlin?style=flat)](https://github.com/wendigo/chrome-reactive-kotlin/stargazers) - reactive (rxjava 2.x), low-level client library in Kotlin
- Kotlin: [chrome-devtools-kotlin](https://github.com/joffrey-bion/chrome-devtools-kotlin) [![GitHub stars](https://img.shields.io/github/stars/joffrey-bion/chrome-devtools-kotlin?style=flat)](https://github.com/joffrey-bion/chrome-devtools-kotlin/stargazers) - A coroutine-based client library, providing low-level CDP primitives and high-level extensions.
- Clojure: [clj-chrome-devtools](https://github.com/tatut/clj-chrome-devtools) [![GitHub stars](https://img.shields.io/github/stars/tatut/clj-chrome-devtools?style=flat)](https://github.com/tatut/clj-chrome-devtools/stargazers) - The CDP wrapper API is autogenerated and will be updated when CDP protocol changes.
- Clojure: [cuic](https://github.com/milankinen/cuic) [![GitHub stars](https://img.shields.io/github/stars/milankinen/cuic?style=flat)](https://github.com/milankinen/cuic/stargazers) - Providing a high-level API for UI test automation over the DevTools Protocol.
- PHP: [chrome-devtools-protocol](https://github.com/jakubkulhan/chrome-devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/jakubkulhan/chrome-devtools-protocol?style=flat)](https://github.com/jakubkulhan/chrome-devtools-protocol/stargazers) - A PHP client library for the protocol.
- PHP: [PuPHPeteer](https://github.com/rialto-php/puphpeteer) [![GitHub stars](https://img.shields.io/github/stars/rialto-php/puphpeteer?style=flat)](https://github.com/rialto-php/puphpeteer/stargazers) - PHP bridge to node Puppeteer


### Browser Adapters
- [devtools-remote-debugger](https://github.com/Nice-PLQ/devtools-remote-debugger) [![GitHub stars](https://img.shields.io/github/stars/Nice-PLQ/devtools-remote-debugger?style=flat)](https://github.com/Nice-PLQ/devtools-remote-debugger/stargazers) - Use devtools against a webpage; a CDP agent implemeted in client-side JS.
- [Inspect](https://inspect.dev/) - Use devtools against iOS and Android, easily. Browser and Webviews. **(closed source)**


## Using DevTools frontend with other platforms

#### Android
- [Facebook Stetho](https://github.com/facebook/stetho) [![GitHub stars](https://img.shields.io/github/stars/facebook/stetho?style=flat)](https://github.com/facebook/stetho/stargazers) - Native Android debugging with Chrome DevTools.
- [j2v8-debugger](https://github.com/AlexTrotsenko/j2v8-debugger) [![GitHub stars](https://img.shields.io/github/stars/AlexTrotsenko/j2v8-debugger?style=flat)](https://github.com/AlexTrotsenko/j2v8-debugger/stargazers) - Debugging JavaScript running in [J2V8](https://github.com/eclipsesource/J2V8) [![GitHub stars](https://img.shields.io/github/stars/eclipsesource/J2V8?style=flat)](https://github.com/eclipsesource/J2V8/stargazers) with Chrome DevTools.

#### ClojureScript
- [Dirac](https://github.com/binaryage/dirac) [![GitHub stars](https://img.shields.io/github/stars/binaryage/dirac?style=flat)](https://github.com/binaryage/dirac/stargazers) - Debugging of ClojsureScript.

#### iOS
- [PonyDebugger](https://github.com/square/PonyDebugger) [![GitHub stars](https://img.shields.io/github/stars/square/PonyDebugger?style=flat)](https://github.com/square/PonyDebugger/stargazers) - Remote network and data debugging iOS apps with Chrome DevTools.

#### Node.js
- [ndb](https://github.com/GoogleChromeLabs/ndb) [![GitHub stars](https://img.shields.io/github/stars/GoogleChromeLabs/ndb?style=flat)](https://github.com/GoogleChromeLabs/ndb/stargazers) - An improved Node.js debugging experience with the DevTools Frontend.
- [Debugging Node.js with Chrome DevTools](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27) - Guide on using the full debugging and profiling support in Node v6.3+.
- [thetool](https://github.com/sfninja/thetool) [![GitHub stars](https://img.shields.io/github/stars/sfninja/thetool?style=flat)](https://github.com/sfninja/thetool/stargazers) - CPU, memory, coverage, type profiling with Node.
- [chrome-devtools-frontend](https://www.npmjs.com/package/chrome-devtools-frontend) - Mirror of the frontend that ships in Chrome.

#### Ruby
- [ruby/debug](https://github.com/ruby/debug) [![GitHub stars](https://img.shields.io/github/stars/ruby/debug?style=flat)](https://github.com/ruby/debug/stargazers) - Debugging functionality for Ruby.

---

## Applications

### Browsers
- [BrowserBox](https://github.com/BrowserBox/BrowserBox) [![GitHub stars](https://img.shields.io/github/stars/BrowserBox/BrowserBox?style=flat)](https://github.com/BrowserBox/BrowserBox/stargazers) - Embed Chrome in a web page, largely powered by DevTools and supporting multiuser browsing, remote DevTools, audio, and documents like `.docx`, `.pdf`, and more.
- [Puppetromium](https://github.com/dosyago/puppetromium) [![GitHub stars](https://img.shields.io/github/stars/dosyago/puppetromium?style=flat)](https://github.com/dosyago/puppetromium/stargazers) - A proof-of-concept web browser built with Puppeteer, written in Node.js, HTML and CSS, with 0% client-side JavaScript.

### Web Archivers and Indexers
- [dn](https://github.com/dosyago/dn) [![GitHub stars](https://img.shields.io/github/stars/dosyago/dn?style=flat)](https://github.com/dosyago/dn/stargazers) - Archive and index pages you browse for offline viewing and search, implemented using the `Fetch` domain's interceptions, and works with any Chromium-based browser.
  
---

## DevTools Extensions

### Workflow
- [Clockwork](https://chromewebstore.google.com/detail/clockwork/dmggabnehkmmfmdffgajcflpdjlnoemp?hl=en) - View PHP application profiling data.
- [RailsPanel](https://chromewebstore.google.com/detail/railspanel/gjpfobpafnhjhbajcjgccbbdofdckggg?hl=en-US) - View Ruby on Rails application profiling data.
- [React Developer Tools](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) - Inspect the React component hierarchies.
- [Ember.js Inspector](https://chromewebstore.google.com/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi) - Allows you to inspect Ember.js objects in your application.
- [Vue.js Developer Tools](https://github.com/vuejs/vue-devtools) [![GitHub stars](https://img.shields.io/github/stars/vuejs/vue-devtools?style=flat)](https://github.com/vuejs/vue-devtools/stargazers) - Inspect Vue.js components and manipulate their data.
- [Angular DevTools](https://chromewebstore.google.com/detail/angular-devtools/ienfalfjdbdpebioblfackkekamfmbnh) - Debugging and Profiling for Angular applications.
- [Backbone Debugger](https://chromewebstore.google.com/detail/backbone-debugger/bhljhndlimiafopmmhjlgfpnnchjjbhd) - Inspect a Backbone application's views, models, events, and routes.
- [Redux Devtools](https://chromewebstore.google.com/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd) - Inspect Redux with actions history, undo and replay.
- [Insight](https://github.com/3Dparallax/insight/) [![GitHub stars](https://img.shields.io/github/stars/3Dparallax/insight/?style=flat)](https://github.com/3Dparallax/insight//stargazers) - A WebGL debugging toolkit which enables more productive WebGL development and more efficient WebGL applications.
- [BEM devtools](https://github.com/escaton/bem-chrome-devtools) [![GitHub stars](https://img.shields.io/github/stars/escaton/bem-chrome-devtools?style=flat)](https://github.com/escaton/bem-chrome-devtools/stargazers) - Inspect BEM entities expressed in `i-bem` framework.
- [Web Component DevTools](https://chromewebstore.google.com/detail/web-component-devtools/gdniinfdlmmmjpnhgnkmfpffipenjljo) - Inspect, modify and observe Web Components on page.

### Themes
- [Material UI Theme](https://chromewebstore.google.com/detail/material-devtools-theme-c/jmefikbdhgocdjeejjnnepgnfkkbpgjo) - Provides various Material Design inspired themes.

### Performance
- [sloth](https://github.com/denar90/sloth) [![GitHub stars](https://img.shields.io/github/stars/denar90/sloth?style=flat)](https://github.com/denar90/sloth/stargazers) - Chrome extension allows to enable and save CPU and network throttling for selected tabs.
- [TracerBench](https://github.com/TracerBench/tracerbench) [![GitHub stars](https://img.shields.io/github/stars/TracerBench/tracerbench?style=flat)](https://github.com/TracerBench/tracerbench/stargazers) - A controlled performance benchmarking tool for web applications, providing clear, actionable and usable insights into performance deltas.

### Automation
- [Puppeteer IDE](https://github.com/gajananpp/puppeteer-ide-extension) [![GitHub stars](https://img.shields.io/github/stars/gajananpp/puppeteer-ide-extension?style=flat)](https://github.com/gajananpp/puppeteer-ide-extension/stargazers) - Standalone Puppeteer playground in browser's developer tools.
- [k6 browser](https://github.com/grafana/xk6-browser) [![GitHub stars](https://img.shields.io/github/stars/grafana/xk6-browser?style=flat)](https://github.com/grafana/xk6-browser/stargazers) - Browser automation and end-to-end web testing tool that interacts with browsers and collects frontend performance metrics.

## Alumni
Old projects, likely not maintained any longer… But still cool.

- [Remote Debug Gateway](https://github.com/RemoteDebug/remotedebug-gateway) [![GitHub stars](https://img.shields.io/github/stars/RemoteDebug/remotedebug-gateway?style=flat)](https://github.com/RemoteDebug/remotedebug-gateway/stargazers) - Allows you to connect a client to multiple browsers at once.  
   - Multiuser DevTools: [DevTools Remote](https://github.com/auchenberg/devtools-remote) [![GitHub stars](https://img.shields.io/github/stars/auchenberg/devtools-remote?style=flat)](https://github.com/auchenberg/devtools-remote/stargazers) - Remotely debug someone else's browser.
- [DevTools Backend](https://github.com/christian-bromann/devtools-backend) [![GitHub stars](https://img.shields.io/github/stars/christian-bromann/devtools-backend?style=flat)](https://github.com/christian-bromann/devtools-backend/stargazers) - Standalone implementation of the Chrome DevTools backend to debug arbitrary web environments.
- Python CDP driver: [pychrome](https://github.com/fate0/pychrome) [![GitHub stars](https://img.shields.io/github/stars/fate0/pychrome?style=flat)](https://github.com/fate0/pychrome/stargazers) - low level CDP transport handler
- [ios-webkit-debug-proxy](https://github.com/google/ios-webkit-debug-proxy) [![GitHub stars](https://img.shields.io/github/stars/google/ios-webkit-debug-proxy?style=flat)](https://github.com/google/ios-webkit-debug-proxy/stargazers) - Exposes Mobile Safari & UIWebView instances via the CDP.
  - [Remote Debug iOS WebKit adapter](https://github.com/RemoteDebug/remotedebug-ios-webkit-adapter) [![GitHub stars](https://img.shields.io/github/stars/RemoteDebug/remotedebug-ios-webkit-adapter?style=flat)](https://github.com/RemoteDebug/remotedebug-ios-webkit-adapter/stargazers) - Builts upon ios-webkit-debug-proxy and translates WebKit's Remote Debugging Protocol API to the CDP.
- [IE Diagnostics Adapter](https://github.com/Microsoft/IEDiagnosticsAdapter) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/IEDiagnosticsAdapter?style=flat)](https://github.com/Microsoft/IEDiagnosticsAdapter/stargazers) - Protocol adaptor for Microsoft IE 11 to CDP.
- [go-debugger-devtools](https://github.com/allada/go-debugger-devtools) [![GitHub stars](https://img.shields.io/github/stars/allada/go-debugger-devtools?style=flat)](https://github.com/allada/go-debugger-devtools/stargazers)
