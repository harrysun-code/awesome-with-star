# choo

[![GitHub stars](https://img.shields.io/github/stars/choojs/awesome-choo?style=flat)](https://github.com/choojs/awesome-choo/stargazers)

# Awesome choo [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) <div align="right">:steam_locomotive::train::train::train::train::train:</div>

> [choo](https://choo.io/) is a `4kb` framework for creating
> sturdy frontend applications

## Contents

- [Official resources](#official-resources)
- [Dependencies](#dependencies)
- [Demos](#demos)
- [Community](#community)
- [Plugins and addons](#plugins-and-addons)
- [Elements](#elements)
- [CLI Templates](#cli-templates)
- [Resources](#resources)
- [Projects using choo](#projects-using-choo)

### Official resources

- [Docs](https://github.com/yoshuawuyts/choo/blob/master/README.md) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo/blob/master/README.md?style=flat)](https://github.com/yoshuawuyts/choo/blob/master/README.md/stargazers)
- [Handbook](https://github.com/yoshuawuyts/choo-handbook) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo-handbook?style=flat)](https://github.com/yoshuawuyts/choo-handbook/stargazers)
- [Repo](https://github.com/yoshuawuyts/choo) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo?style=flat)](https://github.com/yoshuawuyts/choo/stargazers)
- [Website](https://choo.io/)
- [Twitter thread](https://twitter.com/yoshuawuyts/status/730087077803528193)

### Dependencies
`choo` is a modular framework. These are the dependencies it glues together
under the hood:

- [bel](https://github.com/shama/bel) [![GitHub stars](https://img.shields.io/github/stars/shama/bel?style=flat)](https://github.com/shama/bel/stargazers) - Create composable DOM elements using
  template strings.
- [hyperx](https://github.com/substack/hyperx) [![GitHub stars](https://img.shields.io/github/stars/substack/hyperx?style=flat)](https://github.com/substack/hyperx/stargazers) - Convert template strings to
  library backends.
- [nanomorph](https://github.com/choojs/nanomorph) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanomorph?style=flat)](https://github.com/choojs/nanomorph/stargazers) - Hyper fast diffing algorithm for real DOM nodes.
- [nanoraf](https://github.com/yoshuawuyts/nanoraf) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/nanoraf?style=flat)](https://github.com/yoshuawuyts/nanoraf/stargazers) - Only call RAF when needed.
- [nanorouter](https://github.com/choojs/nanorouter) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanorouter?style=flat)](https://github.com/choojs/nanorouter/stargazers) - Smol frontend router.
- [nanobus](https://github.com/choojs/nanobus) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanobus?style=flat)](https://github.com/choojs/nanobus/stargazers) - Tiny message bus.
- [nanolocation](https://github.com/choojs/nanolocation) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanolocation?style=flat)](https://github.com/choojs/nanolocation/stargazers) - Small window.location library.
- [nanohref](https://github.com/choojs/nanohref) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanohref?style=flat)](https://github.com/choojs/nanohref/stargazers) - Tiny href click handler library.
- [nanoquery](https://github.com/choojs/nanoquery) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanoquery?style=flat)](https://github.com/choojs/nanoquery/stargazers) - Tiny querystring module.
- [nanotiming](https://github.com/choojs/nanotiming) [![GitHub stars](https://img.shields.io/github/stars/choojs/nanotiming?style=flat)](https://github.com/choojs/nanotiming/stargazers) - Small timing library.

### Demos

- [Input example](http://requirebin.com/?gist=e589473373b3100a6ace29f7bbee3186) - ([repo](https://github.com/yoshuawuyts/choo/tree/master/examples/title) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo/tree/master/examples/title?style=flat)](https://github.com/yoshuawuyts/choo/tree/master/examples/title/stargazers))
- [HTTP effects](https://hyperdev.com/#!/project/fork-fang)
- [Mailbox routing](https://github.com/yoshuawuyts/choo/tree/master/examples/mailbox) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo/tree/master/examples/mailbox?style=flat)](https://github.com/yoshuawuyts/choo/tree/master/examples/mailbox/stargazers)
- [TodoMVC](http://shuheikagawa.com/todomvc-choo) - ([repo](https://github.com/shuhei/todomvc-choo) [![GitHub stars](https://img.shields.io/github/stars/shuhei/todomvc-choo?style=flat)](https://github.com/shuhei/todomvc-choo/stargazers))
- [choo-firebase](https://choo-firebase-2ec21.firebaseapp.com) - ([repo](https://github.com/mw222rs/choo-firebase) [![GitHub stars](https://img.shields.io/github/stars/mw222rs/choo-firebase?style=flat)](https://github.com/mw222rs/choo-firebase/stargazers))
- [Grow](https://grow.static.land) - ([repo](https://github.com/sethvincent/grow) [![GitHub stars](https://img.shields.io/github/stars/sethvincent/grow?style=flat)](https://github.com/sethvincent/grow/stargazers))
- [Chatbot](http://chootbot.herokuapp.com) - ([repo](https://github.com/plaey/chatbot) [![GitHub stars](https://img.shields.io/github/stars/plaey/chatbot?style=flat)](https://github.com/plaey/chatbot/stargazers))
- [chat-random](https://github.com/akiva/chat-random) [![GitHub stars](https://img.shields.io/github/stars/akiva/chat-random?style=flat)](https://github.com/akiva/chat-random/stargazers)
- [choo-leaflet-demo](https://github.com/timwis/choo-leaflet-demo) [![GitHub stars](https://img.shields.io/github/stars/timwis/choo-leaflet-demo?style=flat)](https://github.com/timwis/choo-leaflet-demo/stargazers)
- [choo-scriber](https://zhouhansen.github.io/choo-scriber) - ([repo](https://github.com/ZhouHansen/choo-scriber) [![GitHub stars](https://img.shields.io/github/stars/ZhouHansen/choo-scriber?style=flat)](https://github.com/ZhouHansen/choo-scriber/stargazers))

### Community

- [Freenode](https://webchat.freenode.net/?channels=choo)

### Plugins and addons

- [choo-location-electron](https://github.com/bcomnes/choo-location-electron) [![GitHub stars](https://img.shields.io/github/stars/bcomnes/choo-location-electron?style=flat)](https://github.com/bcomnes/choo-location-electron/stargazers) - Fix `choo`'s router in electron.
- [choo-log](https://github.com/yoshuawuyts/choo-log) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo-log?style=flat)](https://github.com/yoshuawuyts/choo-log/stargazers) - Development logger for choo.
- [choo-test](https://github.com/mantoni/choo-test) [![GitHub stars](https://img.shields.io/github/stars/mantoni/choo-test?style=flat)](https://github.com/mantoni/choo-test/stargazers) - Easy choo app unit testing.
- [choo-persist](https://github.com/yoshuawuyts/choo-persist/) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo-persist/?style=flat)](https://github.com/yoshuawuyts/choo-persist//stargazers) - Synchronize choo state with LocalStorage.
- [choo-promise](https://github.com/rahatarmanahmed/choo-promise) [![GitHub stars](https://img.shields.io/github/stars/rahatarmanahmed/choo-promise?style=flat)](https://github.com/rahatarmanahmed/choo-promise/stargazers) - Use promises in effects and subscriptions.
- [choo-pull](https://github.com/yoshuawuyts/choo-pull) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo-pull?style=flat)](https://github.com/yoshuawuyts/choo-pull/stargazers) - Wrap handlers to use pull-stream in a choo plugin.
- [choo-redirect](https://github.com/yoshuawuyts/choo-redirect) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo-redirect?style=flat)](https://github.com/yoshuawuyts/choo-redirect/stargazers) - Redirect a view to another view.
- [choo-model](https://github.com/yoshuawuyts/choo-model) [![GitHub stars](https://img.shields.io/github/stars/yoshuawuyts/choo-model?style=flat)](https://github.com/yoshuawuyts/choo-model/stargazers) - Experimental state management lib for choo.
- [choo-resume](https://github.com/bengourley/choo-resume) [![GitHub stars](https://img.shields.io/github/stars/bengourley/choo-resume?style=flat)](https://github.com/bengourley/choo-resume/stargazers) - choo-resume + hot-rld = hot app reload in choo.
- [choo-detached](https://github.com/graforlock/choo-detached) [![GitHub stars](https://img.shields.io/github/stars/graforlock/choo-detached?style=flat)](https://github.com/graforlock/choo-detached/stargazers) - Use `choo` as a mountable, simple stand-alone component (no routing).
- [choo-service-worker](https://github.com/choojs/choo-service-worker) [![GitHub stars](https://img.shields.io/github/stars/choojs/choo-service-worker?style=flat)](https://github.com/choojs/choo-service-worker/stargazers) - Service worker loader for `choo`.
- [choo-websocket](https://github.com/YerkoPalma/choo-websocket) [![GitHub stars](https://img.shields.io/github/stars/YerkoPalma/choo-websocket?style=flat)](https://github.com/YerkoPalma/choo-websocket/stargazers) - Small wraper around WebSocket browser API, for `choo` apps.
- [choo-store](https://github.com/ungoldman/choo-store) [![GitHub stars](https://img.shields.io/github/stars/ungoldman/choo-store?style=flat)](https://github.com/ungoldman/choo-store/stargazers) - Lightweight state structure for choo apps.

### Elements

- [dom-notifications](https://github.com/finnp/dom-notifications) [![GitHub stars](https://img.shields.io/github/stars/finnp/dom-notifications?style=flat)](https://github.com/finnp/dom-notifications/stargazers) - Atom-inspired notifications component.
- [choodown](https://github.com/trainyard/choodown) [![GitHub stars](https://img.shields.io/github/stars/trainyard/choodown?style=flat)](https://github.com/trainyard/choodown/stargazers) - A simple markdown component for choo.
- [choo-md-editor](https://github.com/dbtek/choo-md-editor) [![GitHub stars](https://img.shields.io/github/stars/dbtek/choo-md-editor?style=flat)](https://github.com/dbtek/choo-md-editor/stargazers) - Lightweight markdown editor that can be used inside Choo app or as a standalone library.
- [choo-chartist](https://github.com/rexmortus/choo-chartist) [![GitHub stars](https://img.shields.io/github/stars/rexmortus/choo-chartist?style=flat)](https://github.com/rexmortus/choo-chartist/stargazers) - A little component for using [Chartist](https://gionkunz.github.io/chartist-js/) with the choo framework.

### CLI Templates

Templates for [choo-cli](https://github.com/trainyard/choo-cli) [![GitHub stars](https://img.shields.io/github/stars/trainyard/choo-cli?style=flat)](https://github.com/trainyard/choo-cli/stargazers)

- [trainyard/template-basic](https://github.com/trainyard/template-basic) [![GitHub stars](https://img.shields.io/github/stars/trainyard/template-basic?style=flat)](https://github.com/trainyard/template-basic/stargazers)
- [haroenv/template-webpack](https://github.com/haroenv/template-webpack) [![GitHub stars](https://img.shields.io/github/stars/haroenv/template-webpack?style=flat)](https://github.com/haroenv/template-webpack/stargazers)
- [simonwjackson/atomic-choo](https://github.com/simonwjackson/atomic-choo) [![GitHub stars](https://img.shields.io/github/stars/simonwjackson/atomic-choo?style=flat)](https://github.com/simonwjackson/atomic-choo/stargazers) - An opinionated project seed to get started developing with electron, webpack and choo.

Other CLI templates
- [graforlock/choo-bandwagon](https://github.com/graforlock/choo-bandwagon) [![GitHub stars](https://img.shields.io/github/stars/graforlock/choo-bandwagon?style=flat)](https://github.com/graforlock/choo-bandwagon/stargazers)

### Resources
> :movie_camera: : videos
> :computer: : tutorials
> :book: : articles

- :computer: [Your first choo app](https://yoshuawuyts.gitbooks.io/choo/content/02_your_first_app.html)
- :movie_camera: [TCBY community live hangout](https://www.youtube.com/watch?v=a97Mw2z1SAI)
- :book: [A better frontend experience](https://medium.com/@yoshuawuyts/a-better-frontend-experience-7b0498c85658)
- :book: [Composition in CycleJS, choo, React and Angular2](http://blog.krawaller.se/posts/composition-in-cyclejs-choo-react-and-angular2)
- :book: [Stupidly smart components in choo](http://blog.krawaller.se/posts/stupidly-smart-components-in-choo)

### Projects using choo

- [boxcar](https://github.com/toddself/boxcar) [![GitHub stars](https://img.shields.io/github/stars/toddself/boxcar?style=flat)](https://github.com/toddself/boxcar/stargazers) - A choo-based grid/spreadsheet editor.
- [choo-sortable](https://github.com/willkessler/choo-sortable) [![GitHub stars](https://img.shields.io/github/stars/willkessler/choo-sortable?style=flat)](https://github.com/willkessler/choo-sortable/stargazers) - Building sortable code with choo.
- [hacker-choo](https://github.com/mw222rs/hacker-choo) [![GitHub stars](https://img.shields.io/github/stars/mw222rs/hacker-choo?style=flat)](https://github.com/mw222rs/hacker-choo/stargazers) - Hacker Typer clone written in choo.
- [footprint-rechoo](https://github.com/npeihl/footprint-rechoo) [![GitHub stars](https://img.shields.io/github/stars/npeihl/footprint-rechoo?style=flat)](https://github.com/npeihl/footprint-rechoo/stargazers) - A choo rewrite of [footprint-review](http://github.com/sjcgis/footprint-review).
- [minidocs](https://github.com/freeman-lab/minidocs) [![GitHub stars](https://img.shields.io/github/stars/freeman-lab/minidocs?style=flat)](https://github.com/freeman-lab/minidocs/stargazers) – A documentation site generator built with choo.
- [dataface](https://github.com/timwis/dataface) [![GitHub stars](https://img.shields.io/github/stars/timwis/dataface?style=flat)](https://github.com/timwis/dataface/stargazers) - Desktop application to manage databases.
- [BlankUp](https://github.com/HoverBaum/BlankUp-Electron) [![GitHub stars](https://img.shields.io/github/stars/HoverBaum/BlankUp-Electron?style=flat)](https://github.com/HoverBaum/BlankUp-Electron/stargazers) - Multiplatform markdown editor.
- [hackernews-choo](https://github.com/kvnneff/hackernews-choo) [![GitHub stars](https://img.shields.io/github/stars/kvnneff/hackernews-choo?style=flat)](https://github.com/kvnneff/hackernews-choo/stargazers) - A Hacker News reader built with choo.
- [tic-tac-choo](https://github.com/YerkoPalma/tic-tac-toe) [![GitHub stars](https://img.shields.io/github/stars/YerkoPalma/tic-tac-toe?style=flat)](https://github.com/YerkoPalma/tic-tac-toe/stargazers) - Progressive tic tac toe game, made with choo.
- [enviar](https://github.com/timwis/enviar) [![GitHub stars](https://img.shields.io/github/stars/timwis/enviar?style=flat)](https://github.com/timwis/enviar/stargazers) - Chat interface for SMS / text messages.
- [kaktus](https://github.com/kaktus/kaktus) [![GitHub stars](https://img.shields.io/github/stars/kaktus/kaktus?style=flat)](https://github.com/kaktus/kaktus/stargazers) - A new minimalistic web browser, built on `choo` and IndexedDB.
- [civicdr.org](https://github.com/CiviCDR/civicdr.org) [![GitHub stars](https://img.shields.io/github/stars/CiviCDR/civicdr.org?style=flat)](https://github.com/CiviCDR/civicdr.org/stargazers) - Website for [CiviCDR](https://civicdr.org/).
- [nekocafe](https://github.com/notenoughneon/nekocafe) [![GitHub stars](https://img.shields.io/github/stars/notenoughneon/nekocafe?style=flat)](https://github.com/notenoughneon/nekocafe/stargazers) - Web chat room :cat: :speech_balloon:.
- [Robotopia](https://github.com/robotopia-x/robotopia) [![GitHub stars](https://img.shields.io/github/stars/robotopia-x/robotopia?style=flat)](https://github.com/robotopia-x/robotopia/stargazers) - Introducing kids to coding with tiny virtual robots!
- [busca](https://github.com/afk-mcz/busca) [![GitHub stars](https://img.shields.io/github/stars/afk-mcz/busca?style=flat)](https://github.com/afk-mcz/busca/stargazers) - A small web-extension to search the current tab on reddit.
- [choo-ban](https://github.com/luizbaldi/choo-ban) [![GitHub stars](https://img.shields.io/github/stars/luizbaldi/choo-ban?style=flat)](https://github.com/luizbaldi/choo-ban/stargazers) - Simple kanban to manage board tasks, built with `choo`.
- [boowa](https://github.com/boowajs/boowa) [![GitHub stars](https://img.shields.io/github/stars/boowajs/boowa?style=flat)](https://github.com/boowajs/boowa/stargazers) - A fun blog generator, built with `choo`.
- [hyperamp](https://github.com/hypermodules/hyperamp) [![GitHub stars](https://img.shields.io/github/stars/hypermodules/hyperamp?style=flat)](https://github.com/hypermodules/hyperamp/stargazers) - Humble music player.

### License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Yerko Palma](https://github.com/YerkoPalma) [![GitHub stars](https://img.shields.io/github/stars/YerkoPalma?style=flat)](https://github.com/YerkoPalma/stargazers) has waived all copyright and related or neighboring rights to this work.
