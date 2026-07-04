# Redux

> 来源：[brillout/awesome-redux](https://github.com/brillout/awesome-redux)

[![GitHub stars](https://img.shields.io/github/stars/brillout/awesome-redux?style=flat)](https://github.com/brillout/awesome-redux/stargazers)

# Redux Libraries & Learning Material [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://rawgit.com/brillout/awesome-redux/master/redux-logo.svg" align="right" width="110">](http://redux.js.org/)

> Redux is a state container for JavaScript apps.

 - Official website: [`devarchy.com/redux`](https://devarchy.com/redux)
 - Use devarchy to add a library to the catalog
 
 <br/>

#### Contents
- [Code Architecture](#code-architecture)
- [Utilities](#utilities)
- [Code Style](#code-style)
- [Dev tools / Inspection tools](#dev-tools--inspection-tools)
- [React Integration](#react-integration)
- [Other Integrations](#other-integrations)
- [Boilerplate](#boilerplate)
- [Miscellaneous](#miscellaneous)
- [Learning Material](#learning-material)
- [Community](#community)

<br/>

## Code Architecture

*Aims to improve the overall structure of the source code. Makes reasoning about the code easier.*

 - [redux-schema](https://github.com/ddsol/redux-schema) [![GitHub stars](https://img.shields.io/github/stars/ddsol/redux-schema?style=flat)](https://github.com/ddsol/redux-schema/stargazers) - Automatic actions, reducers and validation for Redux.
 - [redux-tcomb](https://github.com/gcanti/redux-tcomb) [![GitHub stars](https://img.shields.io/github/stars/gcanti/redux-tcomb?style=flat)](https://github.com/gcanti/redux-tcomb/stargazers) - Immutable and type-checked state and actions for Redux.
 - [redux-action-tree](https://github.com/cerebral/redux-action-tree) [![GitHub stars](https://img.shields.io/github/stars/cerebral/redux-action-tree?style=flat)](https://github.com/cerebral/redux-action-tree/stargazers) - The Cerebral signals running with Redux.
 - [redux-elm](https://github.com/salsita/redux-elm) [![GitHub stars](https://img.shields.io/github/stars/salsita/redux-elm?style=flat)](https://github.com/salsita/redux-elm/stargazers) - The Elm Architecture in JavaScript.


## Utilities

 - [redux-orm](https://github.com/tommikaikkonen/redux-orm) [![GitHub stars](https://img.shields.io/github/stars/tommikaikkonen/redux-orm?style=flat)](https://github.com/tommikaikkonen/redux-orm/stargazers) - Small, simple and immutable ORM to manage relational data in your Redux store.
 - [redux-api-middleware](https://github.com/agraboso/redux-api-middleware) [![GitHub stars](https://img.shields.io/github/stars/agraboso/redux-api-middleware?style=flat)](https://github.com/agraboso/redux-api-middleware/stargazers) - Redux middleware for calling an API.
 - [redux-ignore](https://github.com/omnidan/redux-ignore) [![GitHub stars](https://img.shields.io/github/stars/omnidan/redux-ignore?style=flat)](https://github.com/omnidan/redux-ignore/stargazers) - Higher-order reducer to ignore Redux actions.
 - [redux-modifiers](https://github.com/calvinfroedge/redux-modifiers) [![GitHub stars](https://img.shields.io/github/stars/calvinfroedge/redux-modifiers?style=flat)](https://github.com/calvinfroedge/redux-modifiers/stargazers) - Collection of generic functions for writing Redux reducers to operate on various data structures.
 - [rereduce](https://github.com/slorber/rereduce) [![GitHub stars](https://img.shields.io/github/stars/slorber/rereduce?style=flat)](https://github.com/slorber/rereduce/stargazers) - Reducer library for Redux.
 - [redux-search](https://github.com/treasure-data/redux-search) [![GitHub stars](https://img.shields.io/github/stars/treasure-data/redux-search?style=flat)](https://github.com/treasure-data/redux-search/stargazers) - Redux bindings for client-side search.
 - [redux-logger](https://github.com/evgenyrodionov/redux-logger) [![GitHub stars](https://img.shields.io/github/stars/evgenyrodionov/redux-logger?style=flat)](https://github.com/evgenyrodionov/redux-logger/stargazers) - Logger middleware for Redux.
 - [redux-immutable](https://github.com/gajus/redux-immutable) [![GitHub stars](https://img.shields.io/github/stars/gajus/redux-immutable?style=flat)](https://github.com/gajus/redux-immutable/stargazers) - Redux-immutable is used to create an equivalent function of Redux combineReducers that works with Immutable.js state.
 - [reselect](https://github.com/reactjs/reselect) [![GitHub stars](https://img.shields.io/github/stars/reactjs/reselect?style=flat)](https://github.com/reactjs/reselect/stargazers) - Selector library for Redux.
 - [redux-requests](https://github.com/idolize/redux-requests) [![GitHub stars](https://img.shields.io/github/stars/idolize/redux-requests?style=flat)](https://github.com/idolize/redux-requests/stargazers) - Manages in-flight requests with a Redux reducer to avoid issuing duplicate requests.
 - [redux-undo](https://github.com/omnidan/redux-undo) [![GitHub stars](https://img.shields.io/github/stars/omnidan/redux-undo?style=flat)](https://github.com/omnidan/redux-undo/stargazers) - Higher order reducer to add undo/redo functionality to Redux state containers.
 - [redux-bug-reporter](https://github.com/dtschust/redux-bug-reporter) [![GitHub stars](https://img.shields.io/github/stars/dtschust/redux-bug-reporter?style=flat)](https://github.com/dtschust/redux-bug-reporter/stargazers) - Bug reporter and bug playback tool for Redux.
 - [redux-transducers](https://github.com/acdlite/redux-transducers) [![GitHub stars](https://img.shields.io/github/stars/acdlite/redux-transducers?style=flat)](https://github.com/acdlite/redux-transducers/stargazers) - Transducer utilities for Redux.


### Store Persistence

 - [redux-storage](https://github.com/michaelcontento/redux-storage) [![GitHub stars](https://img.shields.io/github/stars/michaelcontento/redux-storage?style=flat)](https://github.com/michaelcontento/redux-storage/stargazers) - Persistence layer for Redux with flexible backends.
 - [redux-persist](https://github.com/rt2zz/redux-persist) [![GitHub stars](https://img.shields.io/github/stars/rt2zz/redux-persist?style=flat)](https://github.com/rt2zz/redux-persist/stargazers) - Persist and rehydrate a Redux store.


### Side Effects

*Side Effects / Asynchronous Actions*

 - [redux-saga](https://github.com/yelouafi/redux-saga) [![GitHub stars](https://img.shields.io/github/stars/yelouafi/redux-saga?style=flat)](https://github.com/yelouafi/redux-saga/stargazers) - Alternative side effect model for Redux apps.
 - [redux-promise-middleware](https://github.com/pburtchaell/redux-promise-middleware) [![GitHub stars](https://img.shields.io/github/stars/pburtchaell/redux-promise-middleware?style=flat)](https://github.com/pburtchaell/redux-promise-middleware/stargazers) - Redux middleware for resolving and rejecting promises with conditional optimistic updates.
 - [redux-effects](https://github.com/redux-effects/redux-effects) [![GitHub stars](https://img.shields.io/github/stars/redux-effects/redux-effects?style=flat)](https://github.com/redux-effects/redux-effects/stargazers) - You write pure functions, redux-effects handles the rest.
 - [redux-thunk](https://github.com/gaearon/redux-thunk) [![GitHub stars](https://img.shields.io/github/stars/gaearon/redux-thunk?style=flat)](https://github.com/gaearon/redux-thunk/stargazers) - Thunk middleware for Redux.
 - [redux-connect](https://github.com/makeomatic/redux-connect) [![GitHub stars](https://img.shields.io/github/stars/makeomatic/redux-connect?style=flat)](https://github.com/makeomatic/redux-connect/stargazers) - Provides decorator for resolving async props in react-router, extremely useful for handling server-side rendering in React.
 - [redux-loop](https://github.com/redux-loop/redux-loop) [![GitHub stars](https://img.shields.io/github/stars/redux-loop/redux-loop?style=flat)](https://github.com/redux-loop/redux-loop/stargazers) - Port of elm-effects and the Elm Architecture to Redux that allows you to sequence your effects naturally and purely by returning them from your reducers.
 - [redux-side-effects](https://github.com/salsita/redux-side-effects) [![GitHub stars](https://img.shields.io/github/stars/salsita/redux-side-effects?style=flat)](https://github.com/salsita/redux-side-effects/stargazers) - Redux toolset for keeping all the side effects inside your reducers while maintaining their purity.
 - [redux-logic](https://github.com/jeffbski/redux-logic) [![GitHub stars](https://img.shields.io/github/stars/jeffbski/redux-logic?style=flat)](https://github.com/jeffbski/redux-logic/stargazers) - Redux middleware for organizing business logic and action side effects.
 - [redux-observable](https://github.com/redux-observable/redux-observable) [![GitHub stars](https://img.shields.io/github/stars/redux-observable/redux-observable?style=flat)](https://github.com/redux-observable/redux-observable/stargazers) - RxJS middleware for action side effects in Redux using &quot;Epics&quot;.
 - [redux-ship](https://github.com/clarus/redux-ship) [![GitHub stars](https://img.shields.io/github/stars/clarus/redux-ship?style=flat)](https://github.com/clarus/redux-ship/stargazers) - Composable, testable and typable side effects.


## Code Style

*Aims to make parts of the source code easier to read/write.*

 - [redux-act](https://github.com/pauldijou/redux-act) [![GitHub stars](https://img.shields.io/github/stars/pauldijou/redux-act?style=flat)](https://github.com/pauldijou/redux-act/stargazers) - Opinionated lib to create actions and reducers for Redux.
 - [redux-crud](https://github.com/Versent/redux-crud) [![GitHub stars](https://img.shields.io/github/stars/Versent/redux-crud?style=flat)](https://github.com/Versent/redux-crud/stargazers) - Set of standard actions and reducers for Redux CRUD Applications.


## Dev tools / Inspection tools

 - [redux-devtools-inspector](https://github.com/alexkuz/redux-devtools-inspector) [![GitHub stars](https://img.shields.io/github/stars/alexkuz/redux-devtools-inspector?style=flat)](https://github.com/alexkuz/redux-devtools-inspector/stargazers) - Another Redux DevTools Monitor.
 - [redux-diff-logger](https://github.com/fcomb/redux-diff-logger) [![GitHub stars](https://img.shields.io/github/stars/fcomb/redux-diff-logger?style=flat)](https://github.com/fcomb/redux-diff-logger/stargazers) - Diff logger between states for Redux.
 - [redux-devtools-chart-monitor](https://github.com/romseguy/redux-devtools-chart-monitor) [![GitHub stars](https://img.shields.io/github/stars/romseguy/redux-devtools-chart-monitor?style=flat)](https://github.com/romseguy/redux-devtools-chart-monitor/stargazers) - Chart monitor for Redux DevTools.
 - [redux-devtools](https://github.com/gaearon/redux-devtools) [![GitHub stars](https://img.shields.io/github/stars/gaearon/redux-devtools?style=flat)](https://github.com/gaearon/redux-devtools/stargazers) - DevTools for Redux with hot reloading, action replay, and customizable UI.
 - [redux-devtools-dispatch](https://github.com/YoruNoHikage/redux-devtools-dispatch) [![GitHub stars](https://img.shields.io/github/stars/YoruNoHikage/redux-devtools-dispatch?style=flat)](https://github.com/YoruNoHikage/redux-devtools-dispatch/stargazers) - Dispatch your actions manually to test if your app Reacts well.
 - [redux-devtools-dock-monitor](https://github.com/gaearon/redux-devtools-dock-monitor) [![GitHub stars](https://img.shields.io/github/stars/gaearon/redux-devtools-dock-monitor?style=flat)](https://github.com/gaearon/redux-devtools-dock-monitor/stargazers) - Resizable and movable dock for Redux DevTools monitors.
 - [redux-devtools-filterable-log-monitor](https://github.com/bvaughn/redux-devtools-filterable-log-monitor) [![GitHub stars](https://img.shields.io/github/stars/bvaughn/redux-devtools-filterable-log-monitor?style=flat)](https://github.com/bvaughn/redux-devtools-filterable-log-monitor/stargazers) - Filterable tree view monitor for Redux DevTools.
 - [redux-devtools-log-monitor](https://github.com/gaearon/redux-devtools-log-monitor) [![GitHub stars](https://img.shields.io/github/stars/gaearon/redux-devtools-log-monitor?style=flat)](https://github.com/gaearon/redux-devtools-log-monitor/stargazers) - The default monitor for Redux DevTools with a tree view.
 - [remote-redux-devtools](https://github.com/zalmoxisus/remote-redux-devtools) [![GitHub stars](https://img.shields.io/github/stars/zalmoxisus/remote-redux-devtools?style=flat)](https://github.com/zalmoxisus/remote-redux-devtools/stargazers) - Redux DevTools remotely.


## React Integration

 - [redux-test-recorder](https://github.com/conorhastings/redux-test-recorder) [![GitHub stars](https://img.shields.io/github/stars/conorhastings/redux-test-recorder?style=flat)](https://github.com/conorhastings/redux-test-recorder/stargazers) - Redux middleware to automatically generate tests for reducers through ui interaction.
 - [react-redux](https://github.com/reactjs/react-redux) [![GitHub stars](https://img.shields.io/github/stars/reactjs/react-redux?style=flat)](https://github.com/reactjs/react-redux/stargazers) - Official React bindings for Redux.
 - [react-easy-universal](https://github.com/keystonejs/react-easy-universal) [![GitHub stars](https://img.shields.io/github/stars/keystonejs/react-easy-universal?style=flat)](https://github.com/keystonejs/react-easy-universal/stargazers) - Universal Routing &amp; Rendering with React &amp; Redux was too hard. Now it&#39;s easy.
 - [redux-form-material-ui](https://github.com/erikras/redux-form-material-ui) [![GitHub stars](https://img.shields.io/github/stars/erikras/redux-form-material-ui?style=flat)](https://github.com/erikras/redux-form-material-ui/stargazers) - Set of wrapper components to facilitate using Material UI with Redux Form.


### Routing

 - [redux-async-connect](https://github.com/Rezonans/redux-async-connect) [![GitHub stars](https://img.shields.io/github/stars/Rezonans/redux-async-connect?style=flat)](https://github.com/Rezonans/redux-async-connect/stargazers) - It allows you to request async data, store them in Redux state and connect them to your React component.
 - [redux-tiny-router](https://github.com/Agamennon/redux-tiny-router) [![GitHub stars](https://img.shields.io/github/stars/Agamennon/redux-tiny-router?style=flat)](https://github.com/Agamennon/redux-tiny-router/stargazers) - Router made for Redux and made for universal apps. Stop using the router as a controller, it's just state.
 - [redux-router](https://github.com/acdlite/redux-router) [![GitHub stars](https://img.shields.io/github/stars/acdlite/redux-router?style=flat)](https://github.com/acdlite/redux-router/stargazers) - Redux bindings for React Router &ndash; keep your router state inside your Redux store.
 - [react-router-redux](https://github.com/reactjs/react-router-redux) [![GitHub stars](https://img.shields.io/github/stars/reactjs/react-router-redux?style=flat)](https://github.com/reactjs/react-router-redux/stargazers) - Ruthlessly simple bindings to keep react-router and Redux in sync.
 - [ground-control](https://github.com/raisemarketplace/ground-control) [![GitHub stars](https://img.shields.io/github/stars/raisemarketplace/ground-control?style=flat)](https://github.com/raisemarketplace/ground-control/stargazers) - Scalable reducer management &amp; powerful data fetching for React Router &amp; Redux.


### Forms

 - [redux-form](https://github.com/erikras/redux-form) [![GitHub stars](https://img.shields.io/github/stars/erikras/redux-form?style=flat)](https://github.com/erikras/redux-form/stargazers) - Higher Order Component using react-redux to keep form state in a Redux store.
 - [react-redux-form](https://github.com/davidkpiano/react-redux-form) [![GitHub stars](https://img.shields.io/github/stars/davidkpiano/react-redux-form?style=flat)](https://github.com/davidkpiano/react-redux-form/stargazers) - Create forms easily in React with Redux.


### Component State

 - [redux-react-local](https://github.com/threepointone/redux-react-local) [![GitHub stars](https://img.shields.io/github/stars/threepointone/redux-react-local?style=flat)](https://github.com/threepointone/redux-react-local/stargazers) - Local component state via Redux.
 - [redux-ui](https://github.com/tonyhb/redux-ui) [![GitHub stars](https://img.shields.io/github/stars/tonyhb/redux-ui?style=flat)](https://github.com/tonyhb/redux-ui/stargazers) - Easy UI state management for React Redux.


## Other Integrations


### Flux

 - [redux-actions](https://github.com/acdlite/redux-actions) [![GitHub stars](https://img.shields.io/github/stars/acdlite/redux-actions?style=flat)](https://github.com/acdlite/redux-actions/stargazers) - Flux Standard Action utilities for Redux.
 - [redux-promise](https://github.com/acdlite/redux-promise) [![GitHub stars](https://img.shields.io/github/stars/acdlite/redux-promise?style=flat)](https://github.com/acdlite/redux-promise/stargazers) - FSA-compliant promise middleware for Redux.


### Backbone

 - [backbone-redux](https://github.com/redbooth/backbone-redux) [![GitHub stars](https://img.shields.io/github/stars/redbooth/backbone-redux?style=flat)](https://github.com/redbooth/backbone-redux/stargazers) - Easy way to keep your backbone collections and Redux store in sync.


### Falcor

 - [redux-falcor](https://github.com/ekosz/redux-falcor) [![GitHub stars](https://img.shields.io/github/stars/ekosz/redux-falcor?style=flat)](https://github.com/ekosz/redux-falcor/stargazers) - Connect your Redux front-end to your falcor back-end.


### RxJS

 - [redux-observable](https://github.com/redux-observable/redux-observable) [![GitHub stars](https://img.shields.io/github/stars/redux-observable/redux-observable?style=flat)](https://github.com/redux-observable/redux-observable/stargazers) - RxJS middleware for action side effects in Redux using &quot;Epics&quot;.
 - [rx-redux](https://github.com/jas-chen/rx-redux) [![GitHub stars](https://img.shields.io/github/stars/jas-chen/rx-redux?style=flat)](https://github.com/jas-chen/rx-redux/stargazers) - Reimplementation of Redux using RxJS.
 - [redux-rx](https://github.com/acdlite/redux-rx) [![GitHub stars](https://img.shields.io/github/stars/acdlite/redux-rx?style=flat)](https://github.com/acdlite/redux-rx/stargazers) - RxJS utilities for Redux.
 - [redurx](https://github.com/shiftyp/redurx) [![GitHub stars](https://img.shields.io/github/stars/shiftyp/redurx?style=flat)](https://github.com/shiftyp/redurx/stargazers) - Redux&#39;ish Functional State Management using RxJS.


### Electron

 - [redux-electron-store](https://github.com/samiskin/redux-electron-store) [![GitHub stars](https://img.shields.io/github/stars/samiskin/redux-electron-store?style=flat)](https://github.com/samiskin/redux-electron-store/stargazers) - Redux store enhancer that allows automatic synchronization between electron processes.


### Deku

 - [deku-redux](https://github.com/troch/deku-redux) [![GitHub stars](https://img.shields.io/github/stars/troch/deku-redux?style=flat)](https://github.com/troch/deku-redux/stargazers) - Bindings for Redux in deku &lt; v2.


### Other

 - [redux-rollbar-middleware](https://github.com/netguru/redux-rollbar-middleware) [![GitHub stars](https://img.shields.io/github/stars/netguru/redux-rollbar-middleware?style=flat)](https://github.com/netguru/redux-rollbar-middleware/stargazers) - Redux middleware that wraps exceptions in actions and sends them to Rollbar with current state.
 - [kasia](https://github.com/outlandishideas/kasia) [![GitHub stars](https://img.shields.io/github/stars/outlandishideas/kasia?style=flat)](https://github.com/outlandishideas/kasia/stargazers) - React Redux toolset for the WordPress API.


## Boilerplate

*Boilerplates /  Scaffolds / Starter Kits / Generators / Stack Ensembles*

 - [redux-cli](https://github.com/SpencerCDixon/redux-cli) [![GitHub stars](https://img.shields.io/github/stars/SpencerCDixon/redux-cli?style=flat)](https://github.com/SpencerCDixon/redux-cli/stargazers) - Opinionated CLI for building Redux/React apps quicker.
 - [reactuate](https://github.com/reactuate/reactuate) [![GitHub stars](https://img.shields.io/github/stars/reactuate/reactuate?style=flat)](https://github.com/reactuate/reactuate/stargazers) - React/Redux stack (not a boilerplate kit).
 - [react-chrome-extension-boilerplate](https://github.com/jhen0409/react-chrome-extension-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/jhen0409/react-chrome-extension-boilerplate?style=flat)](https://github.com/jhen0409/react-chrome-extension-boilerplate/stargazers) - Boilerplate for Chrome Extension React.js project.
 - [universal-redux](https://github.com/bdefore/universal-redux) [![GitHub stars](https://img.shields.io/github/stars/bdefore/universal-redux?style=flat)](https://github.com/bdefore/universal-redux/stargazers) - Npm package that lets you jump right into coding React and Redux with universal (isomorphic) rendering. Only manage Express setups or Webpack configurations if you want to.
 - [generator-react-aspnet-boilerplate](https://github.com/pauldotknopf/react-aspnet-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/pauldotknopf/react-aspnet-boilerplate?style=flat)](https://github.com/pauldotknopf/react-aspnet-boilerplate/stargazers) - Starting point for building isomorphic React applications with ASP.NET Core 1, leveraging existing techniques.
 - [generator-redux](https://github.com/banderson/generator-redux) [![GitHub stars](https://img.shields.io/github/stars/banderson/generator-redux?style=flat)](https://github.com/banderson/generator-redux/stargazers) - CLI tools for Redux: next-gen functional Flux/React with devtools.
 - [generator-react-webpack-redux](https://github.com/stylesuxx/generator-react-webpack-redux) [![GitHub stars](https://img.shields.io/github/stars/stylesuxx/generator-react-webpack-redux?style=flat)](https://github.com/stylesuxx/generator-react-webpack-redux/stargazers) - React Webpack Generator including Redux support.
 - [socrates](https://github.com/matthewmueller/socrates) [![GitHub stars](https://img.shields.io/github/stars/matthewmueller/socrates?style=flat)](https://github.com/matthewmueller/socrates/stargazers) - Small (8kb), batteries-included Redux store to reduce boilerplate and promote good habits.


## Miscellaneous

 - [redux-core](https://github.com/jas-chen/redux-core) [![GitHub stars](https://img.shields.io/github/stars/jas-chen/redux-core?style=flat)](https://github.com/jas-chen/redux-core/stargazers) - Minimal Redux.


## Learning Material

 - **Redux's concepts**

    [Redux official documentation](http://redux.js.org/) does a great job at explaining Redux's core principles.

 - **Why immutable data structures**

    The [guide on performance](https://facebook.github.io/react/docs/advanced-performance.html) of React's official documentation explains well what immutable data structures are and why they play an important role.

 - **Side Effects**

    [Redux Loop's readme](https://github.com/redux-loop/redux-loop) [![GitHub stars](https://img.shields.io/github/stars/redux-loop/redux-loop?style=flat)](https://github.com/redux-loop/redux-loop/stargazers) gives a good insight on Side Effects in the context of Redux.

Reading the aforementioned material will get you a good start for writing apps with Redux.
If you are curious for more, check out following resources.

 - **Functional Programming - Basics**

    This [post](http://jaysoo.ca/2016/01/13/functional-programming-little-ideas/) goes over basic concepts of functional programming while building a YouTube instant search demo app.

 - **Reactive Programming**

    This [introduction to Reactive Programming](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) explains Reactive Programming with clarity.

 - **Functional Programming - Going beyond**

    Well written [article](https://medium.com/@chetcorcos/functional-programming-for-javascript-people-1915d8775504) that talks about interesting computer science concepts implemented in functional languages and how these apply to JavaScript.

 - **Monads**

    Curious about monads? Wikipedia gives a good [overview on monads](https://en.wikipedia.org/wiki/Monad_(functional_programming)) and [this article](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html) explains monads in more details with graphics and simple examples.


## Community

- [Reddit](https://www.reddit.com/r/reduxjs/)
- [Stack Overflow](http://stackoverflow.com/questions/tagged/redux)
- [Discord](https://discord.gg/0ZcbPKXt5bZ6au5t)
- [Slack](http://slack.redux.io/)
- [Gitter](https://gitter.im/reactjs/redux)
- [`#rackt` on freenode](https://webchat.freenode.net/)

