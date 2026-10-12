# Chrome DevTools

> 来源：[ChromeDevTools/awesome-chrome-devtools](https://github.com/ChromeDevTools/awesome-chrome-devtools)

[![GitHub stars](https://img.shields.io/github/stars/ChromeDevTools/awesome-chrome-devtools?style=flat)](https://github.com/ChromeDevTools/awesome-chrome-devtools/stargazers)

# Awesome Chrome DevTools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Awesome tooling and resources in the Chrome DevTools ecosystem

Tools, protocol drivers, trace viewers, and standalone frontends built around Chrome DevTools and the Chrome DevTools Protocol (CDP). Following the [Awesome Manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome/blob/main/awesome.md?style=flat)](https://github.com/sindresorhus/awesome/blob/main/awesome.md/stargazers), we keep this list focused on what's genuinely useful rather than indexing everything in the space.

## Contents

- [Learning](#learning)
- [Tracing & Profiling](#tracing--profiling)
- [Chrome DevTools Protocol](#chrome-devtools-protocol)
- [Using DevTools frontend with other platforms](#using-devtools-frontend-with-other-platforms)
- [DevTools Extensions](#devtools-extensions)
- [Alumni](#alumni)

---

## Learning
- [Dev Tips](https://umaar.com/dev-tips/) - Large collection of tips as animated gifs.
- [DevTools Tips](https://devtoolstips.org/) - Collection of illustrated tips as mini tutorials.
- [Web cheatcodes](https://codepo8.github.io/web-cheatcodes/) - Browser developer tools for non-developers.
- [Dear Console](https://codepo8.github.io/dearconsole) - A collection of snippets to use in the browser console.
- [Chrome Secret Menus](https://github.com/sparkyrider/chrome-secret-menus) [![GitHub stars](https://img.shields.io/github/stars/sparkyrider/chrome-secret-menus?style=flat)](https://github.com/sparkyrider/chrome-secret-menus/stargazers) - Guide to Chrome's internal `chrome://` pages and diagnostic tools.
- [Front-end Debugging Tools Handbook](https://github.com/lala-hakobyan/front-end-debugging-handbook) [![GitHub stars](https://img.shields.io/github/stars/lala-hakobyan/front-end-debugging-handbook?style=flat)](https://github.com/lala-hakobyan/front-end-debugging-handbook/stargazers) - Practical guide to front-end debugging across DevTools, framework extensions, and IDEs.

---

## Tracing & Profiling

DevTools Performance traces and V8 `.cpuprofile` logs are plain JSON under the hood, and a few standalone viewers do great things with them:

- [trace.cafe](https://trace.cafe/) - Share and view web performance traces directly in the DevTools Performance panel ([source](https://github.com/paulirish/trace.cafe) [![GitHub stars](https://img.shields.io/github/stars/paulirish/trace.cafe?style=flat)](https://github.com/paulirish/trace.cafe/stargazers)).
- [speedscope](https://github.com/jlfwong/speedscope) [![GitHub stars](https://img.shields.io/github/stars/jlfwong/speedscope?style=flat)](https://github.com/jlfwong/speedscope/stargazers) - Fast, interactive flamegraph viewer that imports Chrome `.cpuprofile` and timeline traces.
- [cpupro](https://github.com/discoveryjs/cpupro) [![GitHub stars](https://img.shields.io/github/stars/discoveryjs/cpupro?style=flat)](https://github.com/discoveryjs/cpupro/stargazers) - Deep V8/Chrome `.cpuprofile` analyzer with flamegraphs, call trees, and hot-spot diagnostics.
- [Perfetto](https://github.com/google/perfetto) [![GitHub stars](https://img.shields.io/github/stars/google/perfetto?style=flat)](https://github.com/google/perfetto/stargazers) - System profiling and trace analysis suite ([ui.perfetto.dev](https://ui.perfetto.dev/)) with Chromium trace support and SQL trace querying.

---

## Chrome DevTools Protocol

Pro-tip: flip on Chrome's built-in [Protocol Monitor](https://developer.chrome.com/docs/devtools/protocol-monitor) (`More tools > Protocol monitor`) to watch live CDP traffic and fire off raw commands right in the browser.

- [ChromeDevTools/devtools-protocol](https://github.com/chromedevtools/devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/chromedevtools/devtools-protocol?style=flat)](https://github.com/chromedevtools/devtools-protocol/stargazers) - **Canonical location of the protocol JSON**, TypeScript types, and issue tracker for protocol bugs.
- [DevTools Protocol API Docs](https://chromedevtools.github.io/devtools-protocol/) - Browsable UI for exploring the protocol's domains, methods, and events.

### Developing with the protocol
- [chrome-remote-interface Wiki](https://github.com/cyrus-and/chrome-remote-interface/wiki) - Handy recipes for common raw-CDP tasks.
- [Chrome Protocol Proxy](https://github.com/wendigo/chrome-protocol-proxy) [![GitHub stars](https://img.shields.io/github/stars/wendigo/chrome-protocol-proxy?style=flat)](https://github.com/wendigo/chrome-protocol-proxy/stargazers) - Proxy for inspecting and debugging CDP client traffic.

### The big two automation libraries
- [Puppeteer](https://github.com/puppeteer/puppeteer) [![GitHub stars](https://img.shields.io/github/stars/puppeteer/puppeteer?style=flat)](https://github.com/puppeteer/puppeteer/stargazers) - High-level Node.js API for controlling Chrome over CDP and WebDriver BiDi. See also [awesome-puppeteer](https://github.com/transitive-bullshit/awesome-puppeteer) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/awesome-puppeteer?style=flat)](https://github.com/transitive-bullshit/awesome-puppeteer/stargazers).
- [Playwright](https://github.com/microsoft/playwright) [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright?style=flat)](https://github.com/microsoft/playwright/stargazers) - Cross-browser automation for Chromium, Firefox, and WebKit across Node.js, Python, .NET, and Java. See also [awesome-playwright](https://github.com/mxschmitt/awesome-playwright) [![GitHub stars](https://img.shields.io/github/stars/mxschmitt/awesome-playwright?style=flat)](https://github.com/mxschmitt/awesome-playwright/stargazers).

### Libraries for driving the protocol (or a layer above)

- JavaScript/Node.js: [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) [![GitHub stars](https://img.shields.io/github/stars/cyrus-and/chrome-remote-interface?style=flat)](https://github.com/cyrus-and/chrome-remote-interface/stargazers) - Low-level CDP client
- Rust: [chromiumoxide](https://github.com/mattsse/chromiumoxide) [![GitHub stars](https://img.shields.io/github/stars/mattsse/chromiumoxide?style=flat)](https://github.com/mattsse/chromiumoxide/stargazers) - Async/tokio library with generated types
- Rust: [Rust Headless Chrome](https://github.com/rust-headless-chrome/rust-headless-chrome) [![GitHub stars](https://img.shields.io/github/stars/rust-headless-chrome/rust-headless-chrome?style=flat)](https://github.com/rust-headless-chrome/rust-headless-chrome/stargazers) - High-level headless Chrome client
- Java: [chrome-devtools-java-client](https://github.com/kklisura/chrome-devtools-java-client) [![GitHub stars](https://img.shields.io/github/stars/kklisura/chrome-devtools-java-client?style=flat)](https://github.com/kklisura/chrome-devtools-java-client/stargazers) - Low-level protocol client
- Java: [jvppeteer](https://github.com/fanyong920/jvppeteer) [![GitHub stars](https://img.shields.io/github/stars/fanyong920/jvppeteer?style=flat)](https://github.com/fanyong920/jvppeteer/stargazers) - Headless Chrome for Java
- Python: [Zendriver](https://github.com/cdpdriver/zendriver) [![GitHub stars](https://img.shields.io/github/stars/cdpdriver/zendriver?style=flat)](https://github.com/cdpdriver/zendriver/stargazers) - Async CDP browser automation
- Python: [PyCDP](https://github.com/hyperiongray/python-chrome-devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/hyperiongray/python-chrome-devtools-protocol?style=flat)](https://github.com/hyperiongray/python-chrome-devtools-protocol/stargazers) - Sans-IO wrappers (see also [Trio driver](https://github.com/hyperiongray/trio-chrome-devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/hyperiongray/trio-chrome-devtools-protocol?style=flat)](https://github.com/hyperiongray/trio-chrome-devtools-protocol/stargazers))
- Python: [ChromeController](https://github.com/fake-name/ChromeController) [![GitHub stars](https://img.shields.io/github/stars/fake-name/ChromeController?style=flat)](https://github.com/fake-name/ChromeController/stargazers) - High-level browser mgmt
- Go: [chromedp](https://github.com/chromedp/chromedp) [![GitHub stars](https://img.shields.io/github/stars/chromedp/chromedp?style=flat)](https://github.com/chromedp/chromedp/stargazers) - High-level actions and tasks
- Go: [Rod](https://github.com/go-rod/rod) [![GitHub stars](https://img.shields.io/github/stars/go-rod/rod?style=flat)](https://github.com/go-rod/rod/stargazers) - High-level automation and scraping
- Go: [cdp](https://github.com/mafredri/cdp) [![GitHub stars](https://img.shields.io/github/stars/mafredri/cdp?style=flat)](https://github.com/mafredri/cdp/stargazers) - Type-safe bindings for CDP
- C#/.NET: [Puppeteer Sharp](https://github.com/hardkoded/puppeteer-sharp) [![GitHub stars](https://img.shields.io/github/stars/hardkoded/puppeteer-sharp?style=flat)](https://github.com/hardkoded/puppeteer-sharp/stargazers) - Puppeteer port
- C#/.NET: [dotnet-chrome-protocol](https://github.com/seclerp/dotnet-chrome-protocol) [![GitHub stars](https://img.shields.io/github/stars/seclerp/dotnet-chrome-protocol?style=flat)](https://github.com/seclerp/dotnet-chrome-protocol/stargazers) - Runtime library and schema codegen
- Ruby: [Ferrum](https://github.com/rubycdp/ferrum) [![GitHub stars](https://img.shields.io/github/stars/rubycdp/ferrum?style=flat)](https://github.com/rubycdp/ferrum/stargazers) - High-level API to control Chrome
- Ruby: [Cuprite](https://github.com/rubycdp/cuprite) [![GitHub stars](https://img.shields.io/github/stars/rubycdp/cuprite?style=flat)](https://github.com/rubycdp/cuprite/stargazers) - Capybara driver
- Kotlin: [chrome-devtools-kotlin](https://github.com/joffrey-bion/chrome-devtools-kotlin) [![GitHub stars](https://img.shields.io/github/stars/joffrey-bion/chrome-devtools-kotlin?style=flat)](https://github.com/joffrey-bion/chrome-devtools-kotlin/stargazers) - Coroutine-based client library
- Kotlin: [kdriver](https://github.com/cdpdriver/kdriver) [![GitHub stars](https://img.shields.io/github/stars/cdpdriver/kdriver?style=flat)](https://github.com/cdpdriver/kdriver/stargazers) - High-level coroutine-based automation
- Clojure: [clj-chrome-devtools](https://github.com/tatut/clj-chrome-devtools) [![GitHub stars](https://img.shields.io/github/stars/tatut/clj-chrome-devtools?style=flat)](https://github.com/tatut/clj-chrome-devtools/stargazers) - Autogenerated CDP wrapper
- Clojure: [cuic](https://github.com/milankinen/cuic) [![GitHub stars](https://img.shields.io/github/stars/milankinen/cuic?style=flat)](https://github.com/milankinen/cuic/stargazers) - High-level UI test automation
- PHP: [chrome-devtools-protocol](https://github.com/jakubkulhan/chrome-devtools-protocol) [![GitHub stars](https://img.shields.io/github/stars/jakubkulhan/chrome-devtools-protocol?style=flat)](https://github.com/jakubkulhan/chrome-devtools-protocol/stargazers) - Client library

### Agentic Browser Automation

> We're *extremely* picky with this section. Everyone is wrapping a browser for agents right now—expect any PR adding another MCP server or agent CLI to be closed unless it has real traction and does something novel with CDP under the hood.

- [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) [![GitHub stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat)](https://github.com/ChromeDevTools/chrome-devtools-mcp/stargazers) - Official MCP server for Chrome DevTools, which also includes a [CLI](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/SKILL.md) [![GitHub stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/SKILL.md?style=flat)](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/skills/chrome-devtools-cli/SKILL.md/stargazers).
- [Webcmd](https://github.com/agentrhq/webcmd) [![GitHub stars](https://img.shields.io/github/stars/agentrhq/webcmd?style=flat)](https://github.com/agentrhq/webcmd/stargazers) - Compiles site navigation into deterministic per-site CLI commands for AI agents.
- [Lumen](https://github.com/omxyz/lumen) [![GitHub stars](https://img.shields.io/github/stars/omxyz/lumen?style=flat)](https://github.com/omxyz/lumen/stargazers) - Vision-first browser agent with self-healing deterministic replay over CDP.
- [bdg](https://github.com/szymdzum/browser-debugger-cli) [![GitHub stars](https://img.shields.io/github/stars/szymdzum/browser-debugger-cli?style=flat)](https://github.com/szymdzum/browser-debugger-cli/stargazers) - Persistent background CDP session exposing DOM, network, console, and raw protocol methods as shell commands.


### Browser Adapters
- [devtools-remote-debugger](https://github.com/Nice-PLQ/devtools-remote-debugger) [![GitHub stars](https://img.shields.io/github/stars/Nice-PLQ/devtools-remote-debugger?style=flat)](https://github.com/Nice-PLQ/devtools-remote-debugger/stargazers) - Debug a webpage remotely via a CDP agent implemented in client-side JS.
- [Inspect](https://inspect.dev/) - Use DevTools against iOS and Android browsers and WebViews. **(closed source)**


## Using DevTools frontend with other platforms

The DevTools UI is a web app speaking CDP over a WebSocket, so you can embed it or point it at Node, Ruby, mobile webviews, or custom runtimes (see `chrome://inspect` for built-in targets).

- [ChromeDevTools/devtools-frontend](https://github.com/ChromeDevTools/devtools-frontend) [![GitHub stars](https://img.shields.io/github/stars/ChromeDevTools/devtools-frontend?style=flat)](https://github.com/ChromeDevTools/devtools-frontend/stargazers) - Canonical source repo for the Chrome DevTools UI (published to npm as [chrome-devtools-frontend](https://www.npmjs.com/package/chrome-devtools-frontend)).
- [Chii](https://github.com/liriliri/chii) [![GitHub stars](https://img.shields.io/github/stars/liriliri/chii?style=flat)](https://github.com/liriliri/chii/stargazers) & [Eruda](https://github.com/liriliri/eruda) [![GitHub stars](https://img.shields.io/github/stars/liriliri/eruda?style=flat)](https://github.com/liriliri/eruda/stargazers) - Remote debugging server using the real `devtools-frontend` UI (`Chii`, a modern Weinre replacement) and in-page mobile DevTools console (`Eruda`).
- [vscode-js-debug](https://github.com/microsoft/vscode-js-debug) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode-js-debug?style=flat)](https://github.com/microsoft/vscode-js-debug/stargazers) - Official DAP-compliant JavaScript and Chrome CDP debugger powering VS Code.
- [VS Code - Elements for Microsoft Edge](https://github.com/microsoft/vscode-edge-devtools) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode-edge-devtools?style=flat)](https://github.com/microsoft/vscode-edge-devtools/stargazers) - Elements and Network panels embedded inside VS Code.
- [Debugging Node.js with Chrome DevTools](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27) - Guide on debugging and profiling Node.js with `node --inspect`.
- [ruby/debug](https://github.com/ruby/debug) [![GitHub stars](https://img.shields.io/github/stars/ruby/debug?style=flat)](https://github.com/ruby/debug/stargazers) - Ruby's official debugger, which supports connecting Chrome DevTools over CDP (`rdbg --open=chrome`).

---

## DevTools Extensions

- [React Developer Tools](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) - Inspect React component hierarchies, props, and profiler flamegraphs.
- [Vue.js Developer Tools](https://github.com/vuejs/devtools) [![GitHub stars](https://img.shields.io/github/stars/vuejs/devtools?style=flat)](https://github.com/vuejs/devtools/stargazers) - Inspect Vue.js components, state, and routing.
- [Angular DevTools](https://chromewebstore.google.com/detail/angular-devtools/ienfalfjdbdpebioblfackkekamfmbnh) - Component tree inspection and change-detection profiling for Angular.
- [Redux Devtools](https://chromewebstore.google.com/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd) - Time-travel debugging and action history for Redux.
- [Ember.js Inspector](https://chromewebstore.google.com/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi) - Inspect Ember.js objects, routes, and data.
- [Web Component DevTools](https://chromewebstore.google.com/detail/web-component-devtools/gdniinfdlmmmjpnhgnkmfpffipenjljo) - Inspect, modify, and observe custom elements and shadow DOM on the page.
- [Clockwork](https://chromewebstore.google.com/detail/clockwork/dmggabnehkmmfmdffgajcflpdjlnoemp?hl=en) - PHP application profiling and request inspection in DevTools.
- [RailsPanel](https://chromewebstore.google.com/detail/railspanel/gjpfobpafnhjhbajcjgccbbdofdckggg?hl=en-US) - Ruby on Rails request and SQL profiling panel.

## Alumni
Old projects, likely not maintained any longer… But still cool.

- [ndb](https://github.com/GoogleChromeLabs/ndb) [![GitHub stars](https://img.shields.io/github/stars/GoogleChromeLabs/ndb?style=flat)](https://github.com/GoogleChromeLabs/ndb/stargazers) - Improved Node.js debugging experience built on the DevTools frontend.
- [thetool](https://github.com/sfninja/thetool) [![GitHub stars](https://img.shields.io/github/stars/sfninja/thetool?style=flat)](https://github.com/sfninja/thetool/stargazers) - CPU, memory, coverage, and type profiling for Node.js.
- [Facebook Stetho](https://github.com/facebook/stetho) [![GitHub stars](https://img.shields.io/github/stars/facebook/stetho?style=flat)](https://github.com/facebook/stetho/stargazers) - Native Android debugging with Chrome DevTools.
- [PonyDebugger](https://github.com/square/PonyDebugger) [![GitHub stars](https://img.shields.io/github/stars/square/PonyDebugger?style=flat)](https://github.com/square/PonyDebugger/stargazers) - Remote network and Core Data debugging for iOS apps via Chrome DevTools.
- [betwixt](https://github.com/kdzwinel/betwixt) [![GitHub stars](https://img.shields.io/github/stars/kdzwinel/betwixt?style=flat)](https://github.com/kdzwinel/betwixt/stargazers) - System-level network proxy inspected through a standalone DevTools Network panel.
- [Dirac](https://github.com/binaryage/dirac) [![GitHub stars](https://img.shields.io/github/stars/binaryage/dirac?style=flat)](https://github.com/binaryage/dirac/stargazers) - ClojureScript debugging with a custom DevTools fork.
- [VS Code - Debugger for Chrome](https://github.com/Microsoft/vscode-chrome-debug/) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/vscode-chrome-debug/?style=flat)](https://github.com/Microsoft/vscode-chrome-debug//stargazers) - Original Chrome debugger for VS Code (superseded by built-in [vscode-js-debug](https://github.com/microsoft/vscode-js-debug) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode-js-debug?style=flat)](https://github.com/microsoft/vscode-js-debug/stargazers), which has a rich CDP/DAP implementation).
- [noice-json-rpc](https://github.com/nojvek/noice-json-rpc) [![GitHub stars](https://img.shields.io/github/stars/nojvek/noice-json-rpc?style=flat)](https://github.com/nojvek/noice-json-rpc/stargazers) - Proxy-based TypeScript/JS library exposing CDP domains directly as an API.
- [PuPHPeteer](https://github.com/rialto-php/puphpeteer) [![GitHub stars](https://img.shields.io/github/stars/rialto-php/puphpeteer?style=flat)](https://github.com/rialto-php/puphpeteer/stargazers) - PHP bridge to Node Puppeteer.
- [Insight](https://github.com/3Dparallax/insight/) [![GitHub stars](https://img.shields.io/github/stars/3Dparallax/insight/?style=flat)](https://github.com/3Dparallax/insight//stargazers) - WebGL debugging toolkit for Chrome DevTools.
- [Remote Debug Gateway](https://github.com/RemoteDebug/remotedebug-gateway) [![GitHub stars](https://img.shields.io/github/stars/RemoteDebug/remotedebug-gateway?style=flat)](https://github.com/RemoteDebug/remotedebug-gateway/stargazers) - Connect a debugging client to multiple browsers at once.
  - Multiuser DevTools: [DevTools Remote](https://github.com/auchenberg/devtools-remote) [![GitHub stars](https://img.shields.io/github/stars/auchenberg/devtools-remote?style=flat)](https://github.com/auchenberg/devtools-remote/stargazers) - Remotely debug someone else's browser.
- [DevTools Backend](https://github.com/christian-bromann/devtools-backend) [![GitHub stars](https://img.shields.io/github/stars/christian-bromann/devtools-backend?style=flat)](https://github.com/christian-bromann/devtools-backend/stargazers) - Standalone implementation of the Chrome DevTools backend to debug arbitrary web environments.
- Python CDP driver: [pychrome](https://github.com/fate0/pychrome) [![GitHub stars](https://img.shields.io/github/stars/fate0/pychrome?style=flat)](https://github.com/fate0/pychrome/stargazers) - Low-level CDP transport handler.
- [ios-webkit-debug-proxy](https://github.com/google/ios-webkit-debug-proxy) [![GitHub stars](https://img.shields.io/github/stars/google/ios-webkit-debug-proxy?style=flat)](https://github.com/google/ios-webkit-debug-proxy/stargazers) - Exposes Mobile Safari & UIWebView instances via CDP.
  - [Remote Debug iOS WebKit adapter](https://github.com/RemoteDebug/remotedebug-ios-webkit-adapter) [![GitHub stars](https://img.shields.io/github/stars/RemoteDebug/remotedebug-ios-webkit-adapter?style=flat)](https://github.com/RemoteDebug/remotedebug-ios-webkit-adapter/stargazers) - Builds on `ios-webkit-debug-proxy` and translates WebKit's Remote Debugging Protocol to CDP.
- [IE Diagnostics Adapter](https://github.com/Microsoft/IEDiagnosticsAdapter) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/IEDiagnosticsAdapter?style=flat)](https://github.com/Microsoft/IEDiagnosticsAdapter/stargazers) - Protocol adapter translating IE 11 to CDP.

