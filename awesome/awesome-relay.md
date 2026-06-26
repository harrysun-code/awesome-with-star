# Relay

[![GitHub stars](https://img.shields.io/github/stars/expede/awesome-relay?style=flat)](https://github.com/expede/awesome-relay/stargazers)

# Awesome Relay [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
Awesome resources for [Relay](https://github.com/facebook/relay) [![GitHub stars](https://img.shields.io/github/stars/facebook/relay?style=flat)](https://github.com/facebook/relay/stargazers), based on the [Awesome](https://github.com/sindresorhus/awesome/) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome/?style=flat)](https://github.com/sindresorhus/awesome//stargazers) project

# Table of Contents
- [Learning Resources](#learning-resources)
  - [Documentation](#documentation)
  - [FAQs](#faqs)
  - [Tutorials](#tutorials)
  - [Overviews](#overviews)
  - [Example Implementations](#example-implementations)
  - [Lists of Lists](#lists-of-lists)
- [Ecosystem](#ecosystem)
  - [Libraries & Packages](#libraries--packages)
  - [Tooling](#tooling)
  - [Starter Kits](#starter-kits)
- [Relay-Specific Server Support](#relay-specific-server-support)
  - [Go](#go)
  - [JavaScript](#javascript)
  - [Python](#python)
  - [Ruby](#ruby)
    - [Rails](#rails)
  - [Scala](#scala)
- [Testing](#testing)

# Learning Resources
## Documentation
- [Official Docs](https://facebook.github.io/relay/docs/getting-started.html#content) - Official Relay documentation.

## FAQs
- [Unofficial Relay FAQ](https://gist.github.com/wincent/598fa75e22bdfa44cf47) - Common questions answered! Relay resources are scarce at the moment, so this is very helpful if you get stuck.

## Tutorials
- [Getting Started with Relay](https://auth0.com/blog/2015/10/06/getting-started-with-relay/) - One of the few detailed walk throughs of hand-on Relay.
- [Relay 101: Building A Hacker News Client](https://medium.com/@clayallsopp/relay-101-building-a-hacker-news-client-bb8b2bdc76e6#.1i64q1pf9) - A complete workable example.
  - [Relay 102: Mutations](https://medium.com/@clayallsopp/relay-102-mutations-d8b471a4730e#.i9vuv3vxl) - A follow up to "Relay 101" concentrating on mutations.
- [Facebook Relay talk - Lunch and Learn session](https://www.youtube.com/watch?v=sP3n-nht0Xo) - Walkthrough of building a simple app, and demonstration of [GraphiQL](https://github.com/graphql/graphiql) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphiql?style=flat)](https://github.com/graphql/graphiql/stargazers).
- [A Beginner's Guide to Relay Mutations](http://blog.pathgather.com/blog/a-beginners-guide-to-relay-mutations) - Mutations in depth.
- [Learn Relay](https://learnrelay.org/) - Shows you how to make a Pokemon-themed CRUD app, providing a personal, cloud-based GraphQL backend so you can focus on the client-side code. 

## Overviews
- [React Data Fetching with Relay](http://www.sitepoint.com/react-data-fetching-with-relay/) - Clear conceptual overview of Relay's moving parts and magic.
- [Joseph Savona - Relay: An Application Framework For React](https://www.youtube.com/watch?v=IrgHurBjQbg) - Conceptual overview of Relay from the Facebook team.
- [F8 2015 - React Native & Relay: Bringing Modern Web Techniques to Mobile](https://www.youtube.com/watch?v=X6YbAKiLCLU) - Overview of Relay, some about the philosophy.
- [Relay - Daniel Dembach - Hamburg React.js Meetup](https://www.youtube.com/watch?v=dvWTxy1eY6s) - A good general overview of Relay, some discussion of alternatives. Common questions are covered in Q&A at the end.
- [Facebook Relay talk - Lunch and Learn session](https://www.youtube.com/watch?v=sP3n-nht0Xo) - Walkthrough of building a simple app, and demonstration of [GraphiQL](https://github.com/graphql/graphiql) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphiql?style=flat)](https://github.com/graphql/graphiql/stargazers).
- [React with Relay and GraphQL with Andrew Smith](https://www.youtube.com/watch?v=Cfna8gwt9h8) - High level overview of Relay and GraphQL, with some useful discussion from the audience. Some discussion of other front-end frameworks, as well.
- [Relay for Visual Learners](http://sgwilym.github.io/relay-visual-learners/) - Very clear set of diagrams laying out how the different parts of Relay relate to each other.
- [Relay: Seamless Syncing For React](http://www.slideshare.net/BrooklynZelenka/relay-seamless-syncing-for-react-vanjs) - An overview of what Relay is, and some discussion of experience using it in production.
- Cartoon Intro to Facebook's Relay - An overview of how Relay works, complete with illustrations.
  - [Part 1: Saying what data you need with GraphQL](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-1-3ec1a127bca5)
  - [Part 2: Fetching data from the server](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-2-d4a2435aee59)
  - [Part 3: Syncing changes back up to the server](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-3-9d8fcf8db670)
  - [Part 4: How it all fits together](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-4-aef7d819a8ed)
 
## Example Implementations
- [Relay TODO MVC](https://github.com/taion/relay-todomvc) [![GitHub stars](https://img.shields.io/github/stars/taion/relay-todomvc?style=flat)](https://github.com/taion/relay-todomvc/stargazers) - The classic TODO example app, written with Relay.
- [`relay-chat`](https://github.com/transedward/relay-chat) [![GitHub stars](https://img.shields.io/github/stars/transedward/relay-chat?style=flat)](https://github.com/transedward/relay-chat/stargazers) - Relay with routing and pagination.
- [`koa-graphql-relay-example`](https://github.com/chentsulin/koa-graphql-relay-example) [![GitHub stars](https://img.shields.io/github/stars/chentsulin/koa-graphql-relay-example?style=flat)](https://github.com/chentsulin/koa-graphql-relay-example/stargazers) - "TODO" app with [`koa-graphql`](https://github.com/chentsulin/koa-graphql) [![GitHub stars](https://img.shields.io/github/stars/chentsulin/koa-graphql?style=flat)](https://github.com/chentsulin/koa-graphql/stargazers) and `relay`.
- [`todomvc-relay-go`](https://github.com/sogko/todomvc-relay-go) [![GitHub stars](https://img.shields.io/github/stars/sogko/todomvc-relay-go?style=flat)](https://github.com/sogko/todomvc-relay-go/stargazers) - Relay TodoMVC app, driven by a Golang GraphQL backend.

## Lists of Lists
- [Relay and GraphQL Introduction Materials](https://quip.com/oLxzA1gTsJsE)

# Ecosystem
## Libraries & Packages
- [`graphql-relay-js`](https://github.com/graphql/graphql-relay-js) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphql-relay-js?style=flat)](https://github.com/graphql/graphql-relay-js/stargazers) - Simplifies creating a JS GraphQL server for `react-relay`.
- [Babel Relay Plugin](https://www.npmjs.com/package/babel-relay-plugin) - Use Relay the latest ES6+ syntax.
- [`react-router-relay`](https://github.com/relay-tools/react-router-relay) [![GitHub stars](https://img.shields.io/github/stars/relay-tools/react-router-relay?style=flat)](https://github.com/relay-tools/react-router-relay/stargazers) - `react-router` bindings for Relay. Greatly simplifies many local state UI uses cases.
  - [Relay and Routing](https://medium.com/@cpojer/relay-and-routing-36b5439bad9#.h91614i65) - A well-articulated walk through of `react-router-relay`, and the problems that it solves.
  - [`relay-nested-routes`](https://www.npmjs.com/package/relay-nested-routes) - Generate nested routes that reflect nested data. Helpful for managing deep data.
  - [`isomorphic-relay-router`](https://github.com/denvned/isomorphic-relay-router) [![GitHub stars](https://img.shields.io/github/stars/denvned/isomorphic-relay-router?style=flat)](https://github.com/denvned/isomorphic-relay-router/stargazers) - Server side rendering support for `react-router-relay`.
- [`relay-decorator`](https://github.com/4Catalyzer/relay-decorators) [![GitHub stars](https://img.shields.io/github/stars/4Catalyzer/relay-decorators?style=flat)](https://github.com/4Catalyzer/relay-decorators/stargazers) - Simply syntax for Relay containers with ES7 decorators (`@` syntax)
- [`recompose-relay`](https://www.npmjs.com/package/recompose-relay) - Ease composition of Relay containers by currying and providing the component after the container.
- [`relay-local-schema`](https://github.com/relay-tools/relay-local-schema) [![GitHub stars](https://img.shields.io/github/stars/relay-tools/relay-local-schema?style=flat)](https://github.com/relay-tools/relay-local-schema/stargazers) - Use a local schema; no need for a remote GraphQL server.
- [`react-native-relay`](https://github.com/lenaten/react-native-relay) [![GitHub stars](https://img.shields.io/github/stars/lenaten/react-native-relay?style=flat)](https://github.com/lenaten/react-native-relay/stargazers) - Use Relay with React Native.
  - May be supported [out of the box](https://github.com/facebook/relay/issues/26) [![GitHub stars](https://img.shields.io/github/stars/facebook/relay/issues/26?style=flat)](https://github.com/facebook/relay/issues/26/stargazers) in the future.
- [`relay-sink`](https://github.com/acdlite/relay-sink) [![GitHub stars](https://img.shields.io/github/stars/acdlite/relay-sink?style=flat)](https://github.com/acdlite/relay-sink/stargazers) - Use Relay to fetch and store data outside of a React component.
- [`babel-plugin-flow-relay-query`](https://github.com/guymers/babel-plugin-flow-relay-query) [![GitHub stars](https://img.shields.io/github/stars/guymers/babel-plugin-flow-relay-query?style=flat)](https://github.com/guymers/babel-plugin-flow-relay-query/stargazers) - Convert [Flow](http://flowtype.org) types into Relay fragments.
- [`sequelize-relay`](https://github.com/MattMcFarland/sequelize-relay) [![GitHub stars](https://img.shields.io/github/stars/MattMcFarland/sequelize-relay?style=flat)](https://github.com/MattMcFarland/sequelize-relay/stargazers) - Make Relay compatible with [`sequelize`](https://github.com/sequelize/sequelize) [![GitHub stars](https://img.shields.io/github/stars/sequelize/sequelize?style=flat)](https://github.com/sequelize/sequelize/stargazers).
- [`relay-mongodb-connection`](https://github.com/mikberg/relay-mongodb-connection) [![GitHub stars](https://img.shields.io/github/stars/mikberg/relay-mongodb-connection?style=flat)](https://github.com/mikberg/relay-mongodb-connection/stargazers) - Create Relay connections from MongoDB cursors.
- [`relay-composite-network-layer`](https://github.com/eyston/relay-composite-network-layer) [![GitHub stars](https://img.shields.io/github/stars/eyston/relay-composite-network-layer?style=flat)](https://github.com/eyston/relay-composite-network-layer/stargazers) - Compose your Relay Network Layer of many different Network Layers each with their own schema.
- [`react-relay-network-layer`](https://github.com/nodkz/react-relay-network-layer) [![GitHub stars](https://img.shields.io/github/stars/nodkz/react-relay-network-layer?style=flat)](https://github.com/nodkz/react-relay-network-layer/stargazers) - A Network Layer that adds support for query-batching and middlewares. It additionally provides some useful middlewares such as for auth, for logging, etc.

## Tooling
- [GraphiQL](https://github.com/graphql/graphiql) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphiql?style=flat)](https://github.com/graphql/graphiql/stargazers) - A library to introspect GraphQL, test queries and mutations.
  - [GraphiQL App](https://github.com/skevy/graphiql-app) [![GitHub stars](https://img.shields.io/github/stars/skevy/graphiql-app?style=flat)](https://github.com/skevy/graphiql-app/stargazers) - A standalone app for viewing GraphQL, introspection docs, and testing queries/mutations. Invaluable for debugging your Relay app.
- [`relay-local-schema`](https://github.com/relay-tools/relay-local-schema) [![GitHub stars](https://img.shields.io/github/stars/relay-tools/relay-local-schema?style=flat)](https://github.com/relay-tools/relay-local-schema/stargazers) - Use a local schema; no need for a remote GraphQL server.
- [Babel Relay Plugin](https://www.npmjs.com/package/babel-relay-plugin) - Use Relay the latest ES6+ syntax.

## Starter Kits
- [Relay Skeleton](https://github.com/fortruce/relay-skeleton) [![GitHub stars](https://img.shields.io/github/stars/fortruce/relay-skeleton?style=flat)](https://github.com/fortruce/relay-skeleton/stargazers) - Relay project skeleton.
- [Relay Starter Kit](https://github.com/relayjs/relay-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/relayjs/relay-starter-kit?style=flat)](https://github.com/relayjs/relay-starter-kit/stargazers) - An app that it already set up with a basic setup. Just clone and tweak to suit your needs!
- [Node.js API Starter Kit](https://github.com/kriasoft/nodejs-api-starter) [![GitHub stars](https://img.shields.io/github/stars/kriasoft/nodejs-api-starter?style=flat)](https://github.com/kriasoft/nodejs-api-starter/stargazers) - Boilerplate and tooling for building data APIs with Node.js, GraphQL and Relay
- [Simple Relay Starter](https://github.com/mhart/simple-relay-starter) [![GitHub stars](https://img.shields.io/github/stars/mhart/simple-relay-starter?style=flat)](https://github.com/mhart/simple-relay-starter/stargazers) - A Browserify version of the [Relay Starter Kit](https://github.com/relayjs/relay-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/relayjs/relay-starter-kit?style=flat)](https://github.com/relayjs/relay-starter-kit/stargazers).
- [UniversalRelayBoilerplate](https://github.com/codefoundries/UniversalRelayBoilerplate) [![GitHub stars](https://img.shields.io/github/stars/codefoundries/UniversalRelayBoilerplate?style=flat)](https://github.com/codefoundries/UniversalRelayBoilerplate/stargazers)
Boilerplate + examples for React Native (iOS, Android), React (isomorphic, Material-UI), Relay, GraphQL, JWT, Node.js, Apache Cassandra.
- [Relay on Rails Starter Kit](https://github.com/nethsix/relay-on-rails) [![GitHub stars](https://img.shields.io/github/stars/nethsix/relay-on-rails?style=flat)](https://github.com/nethsix/relay-on-rails/stargazers) - A barebones starter kit for Relay application on Rails server. Just clone and tweak!
- [Relay Fullstack](https://github.com/lvarayut/relay-fullstack) [![GitHub stars](https://img.shields.io/github/stars/lvarayut/relay-fullstack?style=flat)](https://github.com/lvarayut/relay-fullstack/stargazers) - Relay Starter Kit integrated with Relay, Express, Webpack, Babel, Material Design Lite, and PostCSS.

# Relay-Specific Server Support
## Go
- [Go Relay](https://github.com/graphql-go/relay) [![GitHub stars](https://img.shields.io/github/stars/graphql-go/relay?style=flat)](https://github.com/graphql-go/relay/stargazers) - A Go/Golang library to help construct a graphql-go server supporting react-relay.
- [`todomvc-relay-go`](https://github.com/sogko/todomvc-relay-go) [![GitHub stars](https://img.shields.io/github/stars/sogko/todomvc-relay-go?style=flat)](https://github.com/sogko/todomvc-relay-go/stargazers) - React/Relay TodoMVC app, driven by a Golang GraphQL backend.

## JavaScript
- [`graphql-relay-js`](https://github.com/graphql/graphql-relay-js) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphql-relay-js?style=flat)](https://github.com/graphql/graphql-relay-js/stargazers) - Simplifies creating a JS GraphQL server for `react-relay`.

## Python
- [`graphql-relay-py`](https://github.com/graphql-python/graphql-relay-py) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/graphql-relay-py?style=flat)](https://github.com/graphql-python/graphql-relay-py/stargazers) - A library to help construct a `graphql-py` server supporting `react-relay`.
 
## Ruby
- [`graphql-relay-ruby`](https://github.com/rmosolgo/graphql-relay-ruby) [![GitHub stars](https://img.shields.io/github/stars/rmosolgo/graphql-relay-ruby?style=flat)](https://github.com/rmosolgo/graphql-relay-ruby/stargazers) - Relay helpers for GraphQL & Ruby.

### Rails
- [GraphQL and Relay on Rails — First relay powered react component](https://medium.com/@gauravtiwari/graphql-and-relay-on-rails-first-relay-powered-react-component-cb3f9ee95eca#.c88zcoftn) - Full walk through of a simple Relay setup, including clonable code.
- [Relay/GraphQL On Rails](https://medium.com/@khor/relay-facebook-on-rails-8b4af2057152#.5hjih9wms) - A brief example of Relay with Rails, complete with several diagrams to aid in comprehension.
- [Relay on Rails Starter Kit](https://github.com/nethsix/relay-on-rails) [![GitHub stars](https://img.shields.io/github/stars/nethsix/relay-on-rails?style=flat)](https://github.com/nethsix/relay-on-rails/stargazers) - A barebones starter kit for Relay application on Rails server. Just clone and tweak!

## Scala
- [`sangria-relay`](https://github.com/sangria-graphql/sangria-relay) [![GitHub stars](https://img.shields.io/github/stars/sangria-graphql/sangria-relay?style=flat)](https://github.com/sangria-graphql/sangria-relay/stargazers) - Relay support for [Sangria](http://sangria-graphql.org).

# Testing
- [Writing Simple Unit Tests with Relay](https://medium.com/@mikaelberg/writing-simple-unit-tests-with-relay-707f19e90129) - An early first look at testing Relay. 
