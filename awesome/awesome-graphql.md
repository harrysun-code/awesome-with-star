# GraphQL

> 来源：[chentsulin/awesome-graphql](https://github.com/chentsulin/awesome-graphql)

[![GitHub stars](https://img.shields.io/github/stars/chentsulin/awesome-graphql?style=flat)](https://github.com/chentsulin/awesome-graphql/stargazers)

# Awesome GraphQL [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A query language and runtime for APIs that prioritizes precise data fetching and strongly typed schemas.

## Contents

- [Specifications](#specifications)
- [Federation & Schema Composition](#federation--schema-composition)
- [Foundations](#foundations)
- [Communities](#communities)
- [Meetups](#meetups)
- [Implementations](#implementations)
- [Tools](#tools)
- [Databases & Data Platforms](#databases--data-platforms)
- [Services](#services)
- [Tutorials](#tutorials)
- [Books](#books)
- [Videos](#videos)
- [Podcasts](#podcasts)
- [Style Guides](#style-guides)
- [Blogs](#blogs)
- [Posts](#posts)

<a name="spec" />

## Specifications

- [GraphQL](https://github.com/graphql/graphql-spec) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphql-spec?style=flat)](https://github.com/graphql/graphql-spec/stargazers) - Working draft of the specification for GraphQL.
- [GraphQL over HTTP](https://github.com/graphql/graphql-over-http) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphql-over-http?style=flat)](https://github.com/graphql/graphql-over-http/stargazers) - Working draft of "GraphQL over HTTP" specification.
- [GraphQL Relay](https://relay.dev/docs/guides/graphql-server-specification/) - Relay-compliant GraphQL server specification.
- [OpenCRUD](https://github.com/opencrud/opencrud) [![GitHub stars](https://img.shields.io/github/stars/opencrud/opencrud?style=flat)](https://github.com/opencrud/opencrud/stargazers) - CRUD API specification for GraphQL databases.
- [GraphQXL](https://gabotechs.github.io/graphqxl/) - Extension of the GraphQL language for creating large, scalable server-side schemas.
- [GraphQL Scalars](https://www.graphql-scalars.com/) - Hosts community-defined custom scalar specifications for use with `@specifiedBy`.
- [Apollo Technical Specifications](https://specs.apollo.dev/) - Registry of Apollo's versioned GraphQL schema and protocol specifications.
- [Apollo Link](https://specs.apollo.dev/link/v1.0/) - Draft specification for linking a GraphQL schema to external schemas and importing their definitions.
- [Apollo Incremental Delivery](https://specs.apollo.dev/incremental/v0.2/) - Specification for the response format and client behavior used with `@defer` and `@stream`.

## Federation & Schema Composition

### Specification

- [GraphQL Federation](https://graphql.github.io/graphql-federation-spec/) - Prerelease working draft for composing independently developed GraphQL schemas into a unified graph.
- [Apollo Federation](https://specs.apollo.dev/federation/v2.9/) - Apollo's specification for composing subgraphs into a federated supergraph.
- [Apollo Join](https://specs.apollo.dev/join/v0.3/) - Specification for describing subgraphs and field resolution in a supergraph schema.

### Implementations & Platforms

- [federation-jvm](https://github.com/apollographql/federation-jvm) [![GitHub stars](https://img.shields.io/github/stars/apollographql/federation-jvm?style=flat)](https://github.com/apollographql/federation-jvm/stargazers) - Apollo Federation on the JVM.
- [WunderGraph Cosmo](https://github.com/wundergraph/cosmo) [![GitHub stars](https://img.shields.io/github/stars/wundergraph/cosmo?style=flat)](https://github.com/wundergraph/cosmo/stargazers) - Open source GraphQL federation solution with schema registry, composition checks, analytics, metrics, tracing, and routing.
- [graphql-mesh](https://github.com/ardatan/graphql-mesh) [![GitHub stars](https://img.shields.io/github/stars/ardatan/graphql-mesh?style=flat)](https://github.com/ardatan/graphql-mesh/stargazers) - A GraphQL federation framework for unifying GraphQL, REST, OpenAPI, SOAP, gRPC, and other API services.
- [graphql-orchestrator-java](https://github.com/graph-quilt/graphql-orchestrator-java) [![GitHub stars](https://img.shields.io/github/stars/graph-quilt/graphql-orchestrator-java?style=flat)](https://github.com/graph-quilt/graphql-orchestrator-java/stargazers) - Orchestrator and gateway library that combines schemas from multiple GraphQL microservices using schema stitching and Apollo Federation directives.

### Examples

- [Mocked Managed Federation - Apollo Server 3](https://github.com/setchy/apollo-server-3-mocked-federation) [![GitHub stars](https://img.shields.io/github/stars/setchy/apollo-server-3-mocked-federation?style=flat)](https://github.com/setchy/apollo-server-3-mocked-federation/stargazers) - Example of mocking a managed federation subgraph using Apollo Server 3.x.
- [Mocked Managed Federation - Apollo Server 4](https://github.com/setchy/apollo-server-4-mocked-federation) [![GitHub stars](https://img.shields.io/github/stars/setchy/apollo-server-4-mocked-federation?style=flat)](https://github.com/setchy/apollo-server-4-mocked-federation/stargazers) - Example of mocking a managed federation subgraph using Apollo Server 4.x.
- [graphql-java-kickstart-federation-example](https://github.com/setchy/graphql-java-kickstart-federation-example) [![GitHub stars](https://img.shields.io/github/stars/setchy/graphql-java-kickstart-federation-example?style=flat)](https://github.com/setchy/graphql-java-kickstart-federation-example/stargazers) - A GraphQL Java Kickstart federation example.
- [dgs-federation-example](https://github.com/Netflix/dgs-federation-example) [![GitHub stars](https://img.shields.io/github/stars/Netflix/dgs-federation-example?style=flat)](https://github.com/Netflix/dgs-federation-example/stargazers) - A Netflix DGS federation example.

### Posts

- [GraphQL federation example with Apollo Federation and Apollo GraphOS](https://cube.dev/blog/graphql-federation-example-with-apollo-federation-and-apollo-graphos) - Tutorial for federating services with Apollo Federation, GraphOS, and Cube.
- [GraphQL federation with Hasura GraphQL Engine and Cube](https://cube.dev/blog/graphql-federation-with-hasura-graphql-engine) - Tutorial for federating Hasura and Cube GraphQL APIs.

<a name="foundation" />

## Foundations

- [GraphQL Foundation](https://graphql.org/foundation/) - Organization supporting GraphQL under the Linux Foundation.

<a name="community" />

## Communities

- [Discord - GraphQL](https://discord.graphql.org/) - Official GraphQL.org Discord channel.
- [GraphQL Weekly](https://www.graphqlweekly.com/) - A weekly newsletter highlighting resources and news from the GraphQL community.
- [Apollo GraphQL Community](https://community.apollographql.com/) - Connect with other developers and share knowledge about every part of the Apollo GraphQL platform.
- [Discord - Reactiflux](http://join.reactiflux.com/) - Join `#help-graphql` on the Reactiflux Discord server.
- [Facebook](https://www.facebook.com/groups/795330550572866/) - Group for discussions, articles and knowledge sharing.
- [X](https://x.com/search?q=%23GraphQL) - Use the hashtag `#graphql`.
- [Stack Overflow](https://stackoverflow.com/questions/tagged/graphql) - Questions and answers using the tag `graphql`.
- [GraphQL APIs](https://github.com/APIs-guru/graphql-apis) [![GitHub stars](https://img.shields.io/github/stars/APIs-guru/graphql-apis?style=flat)](https://github.com/APIs-guru/graphql-apis/stargazers) - A collective list of public GraphQL APIs.
- [/r/GraphQL](https://www.reddit.com/r/graphql/) - A subreddit for GraphQL news, resources, and discussions.

<a name="meetup" />

## Meetups

- [Relay Meetup](https://relaymeetup.com/) - A global, online meetup on Relay, the GraphQL client.
- [Amsterdam](https://www.meetup.com/Amsterdam-GraphQL-Meetup/) - Local GraphQL meetup community.
- [Bangalore](https://www.meetup.com/graphql-bangalore/) - Local GraphQL meetup community.
- [Berlin](https://www.meetup.com/graphql-berlin/) - Local GraphQL meetup community.
- [Buenos Aires](https://www.meetup.com/es-ES/GraphQL-BA/) - Local GraphQL meetup community.
- [Copenhagen](https://www.meetup.com/Copenhagen-GraphQL-Meetup-Group/) - Local GraphQL meetup community.
- [Dallas-Fort Worth](https://www.meetup.com/DFW-GraphQL-Meetup/) - Local GraphQL meetup community.
- [Hamburg](https://www.meetup.com/GraphQL-Hamburg/) - Local GraphQL meetup community.
- [London](https://www.meetup.com/GraphQL-London/) - Local GraphQL meetup community.
- [Melbourne](https://www.meetup.com/GraphQL-Melbourne/) - Local GraphQL meetup community.
- [Munich](https://www.meetup.com/GraphQL-Munich/) - Local GraphQL meetup community.
- [New York City](https://www.meetup.com/GraphQL-NYC/) - Local GraphQL meetup community.
- [San Francisco](https://www.meetup.com/GraphQL-SF/) - Local GraphQL meetup community.
- [Seattle](https://www.meetup.com/Seattle-GraphQL/) - Local GraphQL meetup community.
- [Sydney](https://www.meetup.com/GraphQL-Sydney/) - Local GraphQL meetup community.
- [Tel Aviv](https://www.meetup.com/GraphQL-TLV/) - Local GraphQL meetup community.
- [Wrocław](https://www.meetup.com/GraphQL-Wroclaw/) - Local GraphQL meetup community.
- [Singapore](https://www.meetup.com/GraphQL-SG/) - Local GraphQL meetup community.
- [Zurich](https://www.meetup.com/GraphQL-Zurich/) - Local GraphQL meetup community.

<a name="impl" />

## Implementations

<a name="js" />

### JavaScript/TypeScript

- [graphql-js](https://github.com/graphql/graphql-js) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphql-js?style=flat)](https://github.com/graphql/graphql-js/stargazers) - A reference implementation of GraphQL for JavaScript.
- [graphql-jit](https://github.com/zalando-incubator/graphql-jit) [![GitHub stars](https://img.shields.io/github/stars/zalando-incubator/graphql-jit?style=flat)](https://github.com/zalando-incubator/graphql-jit/stargazers) - GraphQL execution using a JIT compiler.
- [Gra**fast**](https://grafast.org) - A cutting edge planning and execution engine for GraphQL.

#### Clients

- [apollo-client](https://github.com/apollographql/apollo-client) [![GitHub stars](https://img.shields.io/github/stars/apollographql/apollo-client?style=flat)](https://github.com/apollographql/apollo-client/stargazers) - A production-ready GraphQL client for TypeScript and JavaScript with caching, framework integrations, and developer tools.
- [Graffle](https://github.com/graffle-js/graffle) [![GitHub stars](https://img.shields.io/github/stars/graffle-js/graffle?style=flat)](https://github.com/graffle-js/graffle/stargazers) - A minimal, extensible, type-safe GraphQL client for JavaScript and TypeScript runtimes.
- [typescript-graphql-request](https://graphql-code-generator.com/docs/plugins/typescript-graphql-request) - Use GraphQL Request as a fully typed SDK.
- [graphql-zeus](https://github.com/graphql-editor/graphql-zeus) [![GitHub stars](https://img.shields.io/github/stars/graphql-editor/graphql-zeus?style=flat)](https://github.com/graphql-editor/graphql-zeus/stargazers) - Generates type-safe JavaScript and TypeScript GraphQL clients with autocomplete.
- [graphqurl](https://github.com/hasura/graphqurl) [![GitHub stars](https://img.shields.io/github/stars/hasura/graphqurl?style=flat)](https://github.com/hasura/graphqurl/stargazers) - Curl for GraphQL with autocomplete, subscriptions, and GraphiQL, plus a universal JavaScript GraphQL client.
- [aws-amplify](https://github.com/aws-amplify/amplify-js) [![GitHub stars](https://img.shields.io/github/stars/aws-amplify/amplify-js?style=flat)](https://github.com/aws-amplify/amplify-js/stargazers) - A JavaScript library for building applications with AWS cloud services, including GraphQL APIs through AWS AppSync.
- [gqty](https://github.com/gqty-dev/gqty) [![GitHub stars](https://img.shields.io/github/stars/gqty-dev/gqty?style=flat)](https://github.com/gqty-dev/gqty/stargazers) - No-query-language GraphQL client for TypeScript.
- [genql](https://github.com/remorses/genql) [![GitHub stars](https://img.shields.io/github/stars/remorses/genql?style=flat)](https://github.com/remorses/genql/stargazers) - Type safe TypeScript client for any GraphQL API.
- [zodql](https://github.com/mattiasahlsen/zodql) [![GitHub stars](https://img.shields.io/github/stars/mattiasahlsen/zodql?style=flat)](https://github.com/mattiasahlsen/zodql/stargazers) - Type-safe GraphQL client that uses Zod schemas as the single source of truth to build queries, infer response types, and validate responses at runtime.

##### Frontend Framework Integrations

- [vue-apollo](https://github.com/vuejs/apollo) [![GitHub stars](https://img.shields.io/github/stars/vuejs/apollo?style=flat)](https://github.com/vuejs/apollo/stargazers) - Apollo Client integration for Vue.js.
- [apollo-angular](https://github.com/the-guild-org/apollo-angular) [![GitHub stars](https://img.shields.io/github/stars/the-guild-org/apollo-angular?style=flat)](https://github.com/the-guild-org/apollo-angular/stargazers) - Apollo Client integration for Angular with declarative data fetching and caching.
- [svelte-apollo](https://github.com/timhall/svelte-apollo) [![GitHub stars](https://img.shields.io/github/stars/timhall/svelte-apollo?style=flat)](https://github.com/timhall/svelte-apollo/stargazers) - Svelte integration for Apollo GraphQL.
- [ember-apollo-client](https://github.com/ember-graphql/ember-apollo-client) [![GitHub stars](https://img.shields.io/github/stars/ember-graphql/ember-apollo-client?style=flat)](https://github.com/ember-graphql/ember-apollo-client/stargazers) - An ember-cli addon for Apollo Client and GraphQL.
- [apollo-elements](https://github.com/apollo-elements/apollo-elements) [![GitHub stars](https://img.shields.io/github/stars/apollo-elements/apollo-elements?style=flat)](https://github.com/apollo-elements/apollo-elements/stargazers) - GraphQL web components that work in any frontend framework.
- [sveltekit-kitql](https://github.com/jycouet/kitql) [![GitHub stars](https://img.shields.io/github/stars/jycouet/kitql?style=flat)](https://github.com/jycouet/kitql/stargazers) - A collection of tools for building SvelteKit applications with GraphQL.

###### React

- [react-apollo](https://www.apollographql.com/docs/react/) - The core @apollo/client library provides built-in integration with React.
- [relay](https://github.com/facebook/relay) [![GitHub stars](https://img.shields.io/github/stars/facebook/relay?style=flat)](https://github.com/facebook/relay/stargazers) - JavaScript framework for building data-driven React applications.
- [urql](https://github.com/urql-graphql/urql) [![GitHub stars](https://img.shields.io/github/stars/urql-graphql/urql?style=flat)](https://github.com/urql-graphql/urql/stargazers) - A customizable GraphQL client with framework bindings and extensible caching.
- [graphql-hooks](https://github.com/nearform/graphql-hooks) [![GitHub stars](https://img.shields.io/github/stars/nearform/graphql-hooks?style=flat)](https://github.com/nearform/graphql-hooks/stargazers) - Minimal hooks-first GraphQL client with caching and server-side rendering support.
- [mst-gql](https://github.com/mobxjs/mst-gql) [![GitHub stars](https://img.shields.io/github/stars/mobxjs/mst-gql?style=flat)](https://github.com/mobxjs/mst-gql/stargazers) - Bindings for mobx-state-tree and GraphQL.
- [micro-graphql-react](https://github.com/arackaf/micro-graphql-react) [![GitHub stars](https://img.shields.io/github/stars/arackaf/micro-graphql-react?style=flat)](https://github.com/arackaf/micro-graphql-react/stargazers) - A lightweight React GraphQL client with simple caching and support for service-worker caching through GET requests.

#### Servers

- [apollo-server](https://github.com/apollographql/apollo-server) [![GitHub stars](https://img.shields.io/github/stars/apollographql/apollo-server?style=flat)](https://github.com/apollographql/apollo-server/stargazers) - A spec-compliant, production-ready JavaScript GraphQL server for schema-first development with standalone and web framework integrations.
- [hapi-graphql](https://github.com/SimonDegraeve/hapi-graphql) [![GitHub stars](https://img.shields.io/github/stars/SimonDegraeve/hapi-graphql?style=flat)](https://github.com/SimonDegraeve/hapi-graphql/stargazers) - Create a GraphQL HTTP server with Hapi.
- [hapi-plugin-graphiql](https://github.com/rse/hapi-plugin-graphiql) [![GitHub stars](https://img.shields.io/github/stars/rse/hapi-plugin-graphiql?style=flat)](https://github.com/rse/hapi-plugin-graphiql/stargazers) - HAPI plugin for GraphiQL integration.
- [graphql-api-koa](https://github.com/jaydenseric/graphql-api-koa) [![GitHub stars](https://img.shields.io/github/stars/jaydenseric/graphql-api-koa?style=flat)](https://github.com/jaydenseric/graphql-api-koa/stargazers) - GraphQL Koa middleware that implements GraphQL.js from scratch and supports native ESM.
- [koa-graphql](https://github.com/chentsulin/koa-graphql) [![GitHub stars](https://img.shields.io/github/stars/chentsulin/koa-graphql?style=flat)](https://github.com/chentsulin/koa-graphql/stargazers) - GraphQL Koa Middleware.
- [graphql-koa-scripts](https://github.com/ryanhs/graphql-koa-scripts) [![GitHub stars](https://img.shields.io/github/stars/ryanhs/graphql-koa-scripts?style=flat)](https://github.com/ryanhs/graphql-koa-scripts/stargazers) - GraphQL Koa 1 file simplified. Useful for quick test.
- [gql](https://github.com/deno-libs/gql) [![GitHub stars](https://img.shields.io/github/stars/deno-libs/gql?style=flat)](https://github.com/deno-libs/gql/stargazers) - Universal GraphQL HTTP middleware for Deno.
- [mercurius](https://github.com/mercurius-js/mercurius) [![GitHub stars](https://img.shields.io/github/stars/mercurius-js/mercurius?style=flat)](https://github.com/mercurius-js/mercurius/stargazers) - GraphQL plugin for Fastify.
- [graphql-yoga](https://github.com/graphql-hive/graphql-yoga) [![GitHub stars](https://img.shields.io/github/stars/graphql-hive/graphql-yoga?style=flat)](https://github.com/graphql-hive/graphql-yoga/stargazers) - A fully featured GraphQL server built on the WHATWG Fetch API for deployment in any JavaScript environment.
- [graphitejs](https://github.com/graphitejs/server) [![GitHub stars](https://img.shields.io/github/stars/graphitejs/server?style=flat)](https://github.com/graphitejs/server/stargazers) - Node.js framework for GraphQL.
- [graphql-helix](https://github.com/contrawork/graphql-helix) [![GitHub stars](https://img.shields.io/github/stars/contrawork/graphql-helix?style=flat)](https://github.com/contrawork/graphql-helix/stargazers) - A highly evolved GraphQL HTTP Server.
- [pylon](https://github.com/getcronit/pylon) [![GitHub stars](https://img.shields.io/github/stars/getcronit/pylon?style=flat)](https://github.com/getcronit/pylon/stargazers) - Write full-feature APIs with just functions. No more boilerplate code, no more setup. Just write functions and deploy.
- [Booster framework](https://booster.cloud/) - Open-source serverless framework that generates GraphQL queries, mutations, and subscriptions from application models.

##### Databases & ORMs

- [graphql-sequelize](https://github.com/mickhansen/graphql-sequelize) [![GitHub stars](https://img.shields.io/github/stars/mickhansen/graphql-sequelize?style=flat)](https://github.com/mickhansen/graphql-sequelize/stargazers) - Sequelize helpers for GraphQL.
- [graphql-bookshelf](https://github.com/brysgo/graphql-bookshelf) [![GitHub stars](https://img.shields.io/github/stars/brysgo/graphql-bookshelf?style=flat)](https://github.com/brysgo/graphql-bookshelf/stargazers) - Some help defining GraphQL schema around BookshelfJS models.
- [join-monster](https://github.com/acarl005/join-monster) [![GitHub stars](https://img.shields.io/github/stars/acarl005/join-monster?style=flat)](https://github.com/acarl005/join-monster/stargazers) - A GraphQL-to-SQL query execution layer for batch data fetching.
- [Simfinity.js](https://github.com/simtlix/simfinity.js) [![GitHub stars](https://img.shields.io/github/stars/simtlix/simfinity.js?style=flat)](https://github.com/simtlix/simfinity.js/stargazers) - Generates GraphQL queries, mutations, relationships, and MongoDB or PostgreSQL storage from GraphQL object types.

##### PubSub

- [graphql-ably-pubsub](https://github.com/ably-labs/graphql-ably-pubsub) [![GitHub stars](https://img.shields.io/github/stars/ably-labs/graphql-ably-pubsub?style=flat)](https://github.com/ably-labs/graphql-ably-pubsub/stargazers) - Ably PubSub implementation for GraphQL to publish mutation updates and subscribe to the result through a subscription query.

#### Custom Scalars

- [graphql-scalars](https://github.com/Urigo/graphql-scalars) [![GitHub stars](https://img.shields.io/github/stars/Urigo/graphql-scalars?style=flat)](https://github.com/Urigo/graphql-scalars/stargazers) - A library of custom GraphQL Scalars for creating precise type-safe GraphQL schemas.

#### Schema Builders

- [type-graphql](https://github.com/MichalLytek/type-graphql) [![GitHub stars](https://img.shields.io/github/stars/MichalLytek/type-graphql?style=flat)](https://github.com/MichalLytek/type-graphql/stargazers) - Creates GraphQL schemas and resolvers with TypeScript classes and decorators.
- [graphql-nexus](https://github.com/graphql-nexus/nexus) [![GitHub stars](https://img.shields.io/github/stars/graphql-nexus/nexus?style=flat)](https://github.com/graphql-nexus/nexus/stargazers) - Code-First, Type-Safe, GraphQL Schema Construction.
- [pothos](https://github.com/hayes/pothos) [![GitHub stars](https://img.shields.io/github/stars/hayes/pothos?style=flat)](https://github.com/hayes/pothos/stargazers) - Plugin-based GraphQL schema builder for TypeScript.
- [garph](https://github.com/stepci/garph) [![GitHub stars](https://img.shields.io/github/stars/stepci/garph?style=flat)](https://github.com/stepci/garph/stargazers) - Full-stack framework for building type-safe GraphQL APIs in TypeScript.
- [gqloom](https://github.com/modevol-com/gqloom) [![GitHub stars](https://img.shields.io/github/stars/modevol-com/gqloom?style=flat)](https://github.com/modevol-com/gqloom/stargazers) - GraphQL weaver for TypeScript/JavaScript that weaves GraphQL schema and resolvers using Valibot, Zod, or Yup.
- [fast-graphql](https://github.com/idurar/fast-graphql) [![GitHub stars](https://img.shields.io/github/stars/idurar/fast-graphql?style=flat)](https://github.com/idurar/fast-graphql/stargazers) - GraphQL tools to structure and combine resolvers and merge schema definitions for Node.js, Next.js, and Apollo Server.

#### Code Generation & Typed Documents

- [graphql-code-generator](https://github.com/dotansimha/graphql-code-generator) [![GitHub stars](https://img.shields.io/github/stars/dotansimha/graphql-code-generator?style=flat)](https://github.com/dotansimha/graphql-code-generator/stargazers) - GraphQL code generator with flexible support for custom plugins and templates such as TypeScript, React Hooks, and resolver signatures.
- [graphql-to-type](https://github.com/lkster/graphql-to-type) [![GitHub stars](https://img.shields.io/github/stars/lkster/graphql-to-type?style=flat)](https://github.com/lkster/graphql-to-type/stargazers) - GraphQL query parser written entirely in TypeScript's type system for creating interfaces from a provided query.
- [gql.tada](https://github.com/0no-co/gql.tada) [![GitHub stars](https://img.shields.io/github/stars/0no-co/gql.tada?style=flat)](https://github.com/0no-co/gql.tada/stargazers) - GraphQL document authoring library, inferring the result and variables types of GraphQL queries and fragments in the TypeScript type system.

#### Miscellaneous

- [graphql-tools](https://github.com/ardatan/graphql-tools) [![GitHub stars](https://img.shields.io/github/stars/ardatan/graphql-tools?style=flat)](https://github.com/ardatan/graphql-tools/stargazers) - Utilities for building, mocking, and stitching GraphQL schemas.
- [graphql-tag](https://github.com/apollographql/graphql-tag) [![GitHub stars](https://img.shields.io/github/stars/apollographql/graphql-tag?style=flat)](https://github.com/apollographql/graphql-tag/stargazers) - A JavaScript template literal tag that parses GraphQL queries.
- [load-gql](https://github.com/KunalSin9h/load-gql) [![GitHub stars](https://img.shields.io/github/stars/KunalSin9h/load-gql?style=flat)](https://github.com/KunalSin9h/load-gql/stargazers) - A tiny, zero dependency GraphQL schema loader from files and folders.
- [graphql-compose](https://github.com/graphql-compose/graphql-compose) [![GitHub stars](https://img.shields.io/github/stars/graphql-compose/graphql-compose?style=flat)](https://github.com/graphql-compose/graphql-compose/stargazers) - Tool for constructing flexible GraphQL schemas from different data sources via plugins.
- [graphql-modules](https://github.com/graphql-hive/graphql-modules) [![GitHub stars](https://img.shields.io/github/stars/graphql-hive/graphql-modules?style=flat)](https://github.com/graphql-hive/graphql-modules/stargazers) - Modularizes GraphQL schemas and resolvers into reusable, testable feature units.
- [graphql-shield](https://github.com/maticzav/graphql-shield) [![GitHub stars](https://img.shields.io/github/stars/maticzav/graphql-shield?style=flat)](https://github.com/maticzav/graphql-shield/stargazers) - Library for creating a permission layer for a GraphQL API.
- [graphql-shield-generator](https://github.com/omar-dulaimi/graphql-shield-generator) [![GitHub stars](https://img.shields.io/github/stars/omar-dulaimi/graphql-shield-generator?style=flat)](https://github.com/omar-dulaimi/graphql-shield-generator/stargazers) - Emits a GraphQL Shield from your GraphQL schema.
- [graphqlgate](https://github.com/oslabs-beta/GraphQL-Gate) [![GitHub stars](https://img.shields.io/github/stars/oslabs-beta/GraphQL-Gate?style=flat)](https://github.com/oslabs-beta/GraphQL-Gate/stargazers) - GraphQL rate-limiting library with query complexity analysis for Node.js.
- [graphql-let](https://github.com/piglovesyou/graphql-let) [![GitHub stars](https://img.shields.io/github/stars/piglovesyou/graphql-let?style=flat)](https://github.com/piglovesyou/graphql-let/stargazers) - Webpack loader for importing type-protected code generation results directly from GraphQL documents.
- [graphql-config](https://github.com/graphql-hive/graphql-config) [![GitHub stars](https://img.shields.io/github/stars/graphql-hive/graphql-config?style=flat)](https://github.com/graphql-hive/graphql-config/stargazers) - Provides shared configuration for GraphQL tools, editors, and IDEs.
- [graphql-cli](https://github.com/urigo/graphql-cli) [![GitHub stars](https://img.shields.io/github/stars/urigo/graphql-cli?style=flat)](https://github.com/urigo/graphql-cli/stargazers) - A command line tool for common GraphQL development workflows.
- [graphql-toolkit](https://github.com/ardatan/graphql-toolkit) [![GitHub stars](https://img.shields.io/github/stars/ardatan/graphql-toolkit?style=flat)](https://github.com/ardatan/graphql-toolkit/stargazers) - A set of utils for faster development of GraphQL tools (Schema and documents loading, Schema merging and more).
- [sofa](https://github.com/graphql-hive/SOFA) [![GitHub stars](https://img.shields.io/github/stars/graphql-hive/SOFA?style=flat)](https://github.com/graphql-hive/SOFA/stargazers) - Generates RESTful APIs from a GraphQL server.
- [graphback](https://github.com/aerogear/graphback) [![GitHub stars](https://img.shields.io/github/stars/aerogear/graphback?style=flat)](https://github.com/aerogear/graphback/stargazers) - Framework and CLI to add a GraphQLCRUD API layer to a GraphQL server using data models.
- [graphql-middleware](https://github.com/maticzav/graphql-middleware) [![GitHub stars](https://img.shields.io/github/stars/maticzav/graphql-middleware?style=flat)](https://github.com/maticzav/graphql-middleware/stargazers) - Split up your GraphQL resolvers in middleware functions.
- [graphql-relay-js](https://github.com/graphql/graphql-relay-js) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphql-relay-js?style=flat)](https://github.com/graphql/graphql-relay-js/stargazers) - A library to help construct a graphql-js server supporting react-relay.
- [graphql-normalizr](https://github.com/monojack/graphql-normalizr) [![GitHub stars](https://img.shields.io/github/stars/monojack/graphql-normalizr?style=flat)](https://github.com/monojack/graphql-normalizr/stargazers) - Normalize GraphQL responses for persisting in the client cache/state.
- [babel-plugin-graphql](https://github.com/ooflorent/babel-plugin-graphql) [![GitHub stars](https://img.shields.io/github/stars/ooflorent/babel-plugin-graphql?style=flat)](https://github.com/ooflorent/babel-plugin-graphql/stargazers) - Babel plugin that compiles GraphQL tagged template strings.
- [eslint-plugin-graphql](https://github.com/apollographql/eslint-plugin-graphql) [![GitHub stars](https://img.shields.io/github/stars/apollographql/eslint-plugin-graphql?style=flat)](https://github.com/apollographql/eslint-plugin-graphql/stargazers) - An ESLint plugin that checks your GraphQL strings against a schema.
- [graphql-ws](https://github.com/enisdenjo/graphql-ws) [![GitHub stars](https://img.shields.io/github/stars/enisdenjo/graphql-ws?style=flat)](https://github.com/enisdenjo/graphql-ws/stargazers) - Coherent, zero-dependency, lazy, simple, GraphQL over WebSocket Protocol compliant server and client.
- [graphql-live-query](https://github.com/n1ru4l/graphql-live-query) [![GitHub stars](https://img.shields.io/github/stars/n1ru4l/graphql-live-query?style=flat)](https://github.com/n1ru4l/graphql-live-query/stargazers) - Realtime GraphQL Live Queries with JavaScript.
- [microfiber](https://github.com/anvilco/graphql-introspection-tools) [![GitHub stars](https://img.shields.io/github/stars/anvilco/graphql-introspection-tools?style=flat)](https://github.com/anvilco/graphql-introspection-tools/stargazers) - Query and manipulate GraphQL introspection query results in useful ways.
- [GraphQL Constraint Directive](https://github.com/confuser/graphql-constraint-directive) [![GitHub stars](https://img.shields.io/github/stars/confuser/graphql-constraint-directive?style=flat)](https://github.com/confuser/graphql-constraint-directive/stargazers) - Allows `@constraint` directives to validate input data, inspired by the Constraints Directives RFC and OpenAPI.
- [Validator.js Wrapper Directive](https://github.com/ktutnik/graphql-directive/tree/master/packages/validator) [![GitHub stars](https://img.shields.io/github/stars/ktutnik/graphql-directive/tree/master/packages/validator?style=flat)](https://github.com/ktutnik/graphql-directive/tree/master/packages/validator/stargazers) - Wraps Validator.js functionality in validation directives.
- [graphql-sunset](https://github.com/sophiabits/graphql-sunset) [![GitHub stars](https://img.shields.io/github/stars/sophiabits/graphql-sunset?style=flat)](https://github.com/sophiabits/graphql-sunset/stargazers) - Quickly and easily add support for the `Sunset` header to your GraphQL server, to better communicate upcoming breaking changes.

<a name="js-example" />

#### JavaScript Examples

- [React Starter Kit](https://github.com/kriasoft/react-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/kriasoft/react-starter-kit?style=flat)](https://github.com/kriasoft/react-starter-kit/stargazers) - Frontend starter kit using React, Relay, GraphQL, and JAMstack architecture.
- [SWAPI GraphQL Wrapper](https://github.com/graphql/swapi-graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql/swapi-graphql?style=flat)](https://github.com/graphql/swapi-graphql/stargazers) - A GraphQL schema and server wrapping SWAPI.
- [Relay TodoMVC](https://github.com/taion/relay-todomvc) [![GitHub stars](https://img.shields.io/github/stars/taion/relay-todomvc?style=flat)](https://github.com/taion/relay-todomvc/stargazers) - TodoMVC example with Relay and routing.
- [Apollo Server tools documentation](https://www.apollographql.com/docs/apollo-server/) - Documentation, tutorial and examples for building GraphQL server and connecting to SQL, MongoDB and REST endpoints.
- [F8 App 2017](https://github.com/fbsamples/f8app) [![GitHub stars](https://img.shields.io/github/stars/fbsamples/f8app?style=flat)](https://github.com/fbsamples/f8app/stargazers) - Source code for the official 2017 F8 app, built with React Native, Relay, and GraphQL.
- [Apollo React example for GitHub GraphQL API](https://github.com/katopz/react-apollo-graphql-github-example) [![GitHub stars](https://img.shields.io/github/stars/katopz/react-apollo-graphql-github-example?style=flat)](https://github.com/katopz/react-apollo-graphql-github-example/stargazers) - Example using Apollo React with the GitHub GraphQL API and Create React App.
- [Next.js TypeScript and GraphQL Example](https://github.com/zeit/next.js/tree/canary/examples/with-typescript-graphql) [![GitHub stars](https://img.shields.io/github/stars/zeit/next.js/tree/canary/examples/with-typescript-graphql?style=flat)](https://github.com/zeit/next.js/tree/canary/examples/with-typescript-graphql/stargazers) - Type-protected GraphQL example on Next.js running graphql-codegen under the hood.
- [GraphQL StackBlitz Starter](https://stackblitz.com/fork/graphql) - Live, editable demo that starts in a browser in about two seconds.
- [VulcanJS](http://vulcanjs.org) - Full-stack React and GraphQL framework.
- [RAN Toolkit](https://github.com/sly777/ran) [![GitHub stars](https://img.shields.io/github/stars/sly777/ran?style=flat)](https://github.com/sly777/ran/stargazers) - Production-ready toolkit/boilerplate with support for GraphQL, SSR, Hot-reload, CSS-in-JS, caching, and more.

<a name="ts-example" />

#### TypeScript Examples

- [Node.js API Starter](https://github.com/kriasoft/graphql-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/kriasoft/graphql-starter-kit?style=flat)](https://github.com/kriasoft/graphql-starter-kit/stargazers) - Monorepo starter with a code-first GraphQL API, PostgreSQL, React, and Joy UI.
- [Next.js Apollo TypeScript Starter](https://github.com/borisowsky/nextjs-apollo-ts-starter) [![GitHub stars](https://img.shields.io/github/stars/borisowsky/nextjs-apollo-ts-starter?style=flat)](https://github.com/borisowsky/nextjs-apollo-ts-starter/stargazers) - Next.js starter project focused on developer experience.
- [GraphQL Starter](https://github.com/cerino-ligutom/GraphQL-Starter) [![GitHub stars](https://img.shields.io/github/stars/cerino-ligutom/GraphQL-Starter?style=flat)](https://github.com/cerino-ligutom/GraphQL-Starter/stargazers) - A boilerplate for TypeScript + Node Express + Apollo GraphQL APIs.
- [Next.js Advanced GraphQL CRUD MongoDB Starter](https://github.com/idurar/starter-advanced-graphql-crud-next-js-mongodb) [![GitHub stars](https://img.shields.io/github/stars/idurar/starter-advanced-graphql-crud-next-js-mongodb?style=flat)](https://github.com/idurar/starter-advanced-graphql-crud-next-js-mongodb/stargazers) - Generic CRUD starter with an advanced Apollo GraphQL server, Next.js, MongoDB, and TypeScript.

<a name="rb" />

### Ruby

- [graphql-ruby](https://github.com/rmosolgo/graphql-ruby) [![GitHub stars](https://img.shields.io/github/stars/rmosolgo/graphql-ruby?style=flat)](https://github.com/rmosolgo/graphql-ruby/stargazers) - Ruby implementation of GraphQL with tools for defining schemas, executing queries, and serving subscriptions.
- [graphql-batch](https://github.com/Shopify/graphql-batch) [![GitHub stars](https://img.shields.io/github/stars/Shopify/graphql-batch?style=flat)](https://github.com/Shopify/graphql-batch/stargazers) - Query batching executor for the GraphQL Ruby gem.
- [graphql-auth](https://github.com/o2web/graphql-auth) [![GitHub stars](https://img.shields.io/github/stars/o2web/graphql-auth?style=flat)](https://github.com/o2web/graphql-auth/stargazers) - A JWT auth wrapper working with devise.
- [agoo](https://github.com/ohler55/agoo) [![GitHub stars](https://img.shields.io/github/stars/ohler55/agoo?style=flat)](https://github.com/ohler55/agoo/stargazers) - High-performance Ruby web server with GraphQL support.
- [GQLi](https://github.com/contentful-labs/gqli.rb) [![GitHub stars](https://img.shields.io/github/stars/contentful-labs/gqli.rb?style=flat)](https://github.com/contentful-labs/gqli.rb/stargazers) - A GraphQL client and DSL for writing queries in native Ruby.

<a name="rb-example" />

#### Ruby Examples

- [graphql-ruby-demo](https://github.com/rmosolgo/graphql-ruby-demo) [![GitHub stars](https://img.shields.io/github/stars/rmosolgo/graphql-ruby-demo?style=flat)](https://github.com/rmosolgo/graphql-ruby-demo/stargazers) - Use graphql-ruby to expose a Rails app.
- [github-graphql-rails-example](https://github.com/github/github-graphql-rails-example) [![GitHub stars](https://img.shields.io/github/stars/github/github-graphql-rails-example?style=flat)](https://github.com/github/github-graphql-rails-example/stargazers) - Example Rails app using GitHub's GraphQL API.
- [relay-on-rails](https://github.com/nethsix/relay-on-rails) [![GitHub stars](https://img.shields.io/github/stars/nethsix/relay-on-rails?style=flat)](https://github.com/nethsix/relay-on-rails/stargazers) - Barebones starter kit for Relay application with Rails GraphQL server.
- [relay-rails-blog](https://github.com/gauravtiwari/relay-rails-blog) [![GitHub stars](https://img.shields.io/github/stars/gauravtiwari/relay-rails-blog?style=flat)](https://github.com/gauravtiwari/relay-rails-blog/stargazers) - Demo weblog powered by GraphQL, Relay, and a standard Rails application.
- [to_eat_app](https://github.com/jcdavison/to_eat_app) [![GitHub stars](https://img.shields.io/github/stars/jcdavison/to_eat_app?style=flat)](https://github.com/jcdavison/to_eat_app/stargazers) - Sample GraphQL, Rails, and Relay application with a related three-part article series.
- [agoo-demo](https://github.com/ohler55/agoo/tree/develop/example/graphql) [![GitHub stars](https://img.shields.io/github/stars/ohler55/agoo/tree/develop/example/graphql?style=flat)](https://github.com/ohler55/agoo/tree/develop/example/graphql/stargazers) - Use of the Agoo server to demonstrate a simple GraphQL application.
- [rails-devise-graphql](https://github.com/zauberware/rails-devise-graphql) [![GitHub stars](https://img.shields.io/github/stars/zauberware/rails-devise-graphql?style=flat)](https://github.com/zauberware/rails-devise-graphql/stargazers) - Rails 6 boilerplate with Devise, GraphQL, and JWT authentication.

<a name="php" />

### PHP

- [graphql-php](https://github.com/webonyx/graphql-php) [![GitHub stars](https://img.shields.io/github/stars/webonyx/graphql-php?style=flat)](https://github.com/webonyx/graphql-php/stargazers) - A PHP port of GraphQL reference implementation.
- [graphql-relay-php](https://github.com/ivome/graphql-relay-php) [![GitHub stars](https://img.shields.io/github/stars/ivome/graphql-relay-php?style=flat)](https://github.com/ivome/graphql-relay-php/stargazers) - Relay helpers for webonyx/graphql-php implementation of GraphQL.
- [lighthouse](https://github.com/nuwave/lighthouse) [![GitHub stars](https://img.shields.io/github/stars/nuwave/lighthouse?style=flat)](https://github.com/nuwave/lighthouse/stargazers) - A PHP package that allows to serve a GraphQL endpoint from your Laravel application.
- [graphql-laravel](https://github.com/rebing/graphql-laravel) [![GitHub stars](https://img.shields.io/github/stars/rebing/graphql-laravel?style=flat)](https://github.com/rebing/graphql-laravel/stargazers) - Laravel package for building GraphQL APIs with webonyx/graphql-php.
- [overblog/graphql-bundle](https://github.com/overblog/GraphQLBundle) [![GitHub stars](https://img.shields.io/github/stars/overblog/GraphQLBundle?style=flat)](https://github.com/overblog/GraphQLBundle/stargazers) - This bundle provides tools to build a complete GraphQL server in your Symfony App. Supports react-relay.
- [wp-graphql](https://github.com/wp-graphql/wp-graphql) [![GitHub stars](https://img.shields.io/github/stars/wp-graphql/wp-graphql?style=flat)](https://github.com/wp-graphql/wp-graphql/stargazers) - GraphQL API for WordPress.
- [graphqlite](https://github.com/thecodingmachine/graphqlite) [![GitHub stars](https://img.shields.io/github/stars/thecodingmachine/graphqlite?style=flat)](https://github.com/thecodingmachine/graphqlite/stargazers) - Framework agnostic library that allows you to write GraphQL server by annotating your PHP classes.
- [siler](https://github.com/leocavalcante/siler) [![GitHub stars](https://img.shields.io/github/stars/leocavalcante/siler?style=flat)](https://github.com/leocavalcante/siler/stargazers) - Plain-old functions providing a declarative API for GraphQL servers with Subscriptions support.
- [graphql-request-builder](https://github.com/dpauli/php-graphql-request-builder) [![GitHub stars](https://img.shields.io/github/stars/dpauli/php-graphql-request-builder?style=flat)](https://github.com/dpauli/php-graphql-request-builder/stargazers) - Builds request payload in GraphQL structure.
- [Drupal GraphQL](https://www.drupal.org/project/graphql) - Drupal module for crafting and exposing GraphQL schemas.
- [jerowork/graphql-schema-builder](https://github.com/jerowork/graphql-attribute-schema) [![GitHub stars](https://img.shields.io/github/stars/jerowork/graphql-attribute-schema?style=flat)](https://github.com/jerowork/graphql-attribute-schema/stargazers) - Easily build your GraphQL schema for webonyx/graphql-php using PHP attributes instead of large configuration arrays.

<a name="php-example" />

#### PHP Examples

- [siler-graphql](https://github.com/leocavalcante/siler/tree/main/examples/graphql) [![GitHub stars](https://img.shields.io/github/stars/leocavalcante/siler/tree/main/examples/graphql?style=flat)](https://github.com/leocavalcante/siler/tree/main/examples/graphql/stargazers) - An example GraphQL server written with Siler.

<a name="py" />

### Python

- [graphql-parser](https://github.com/tryolabs/graphql-parser) [![GitHub stars](https://img.shields.io/github/stars/tryolabs/graphql-parser?style=flat)](https://github.com/tryolabs/graphql-parser/stargazers) - GraphQL parser for Python.
- [graphql-core](https://github.com/graphql-python/graphql-core) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/graphql-core?style=flat)](https://github.com/graphql-python/graphql-core/stargazers) - Python port of the GraphQL.js reference implementation.
- [graphql-relay-py](https://github.com/graphql-python/graphql-relay-py) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/graphql-relay-py?style=flat)](https://github.com/graphql-python/graphql-relay-py/stargazers) - A library for building GraphQL servers that support the Relay server specification.
- [graphql-parser-python](https://github.com/tallstreet/graphql-parser-python) [![GitHub stars](https://img.shields.io/github/stars/tallstreet/graphql-parser-python?style=flat)](https://github.com/tallstreet/graphql-parser-python/stargazers) - A python wrapper around libgraphqlparser.
- [graphene](https://github.com/graphql-python/graphene) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/graphene?style=flat)](https://github.com/graphql-python/graphene/stargazers) - A package for creating GraphQL schemas/types in a Pythonic easy way.
- [graphene-gae](https://github.com/graphql-python/graphene-gae) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/graphene-gae?style=flat)](https://github.com/graphql-python/graphene-gae/stargazers) - Adds GraphQL support to Google AppEngine (GAE).
- [django-graphiql](https://github.com/GraphQL-python-archive/django-graphiql) [![GitHub stars](https://img.shields.io/github/stars/GraphQL-python-archive/django-graphiql?style=flat)](https://github.com/GraphQL-python-archive/django-graphiql/stargazers) - Integrate GraphiQL easily into your Django project.
- [flask-graphql](https://github.com/graphql-python/flask-graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/flask-graphql?style=flat)](https://github.com/graphql-python/flask-graphql/stargazers) - Adds GraphQL support to your Flask application.
- [python-graphql-client](https://github.com/prisma/python-graphql-client) [![GitHub stars](https://img.shields.io/github/stars/prisma/python-graphql-client?style=flat)](https://github.com/prisma/python-graphql-client/stargazers) - Simple GraphQL client for Python 2.7+.
- [python-graphjoiner](https://github.com/healx/python-graphjoiner) [![GitHub stars](https://img.shields.io/github/stars/healx/python-graphjoiner?style=flat)](https://github.com/healx/python-graphjoiner/stargazers) - Create GraphQL APIs using joins, SQL or otherwise.
- [graphene-django](https://github.com/graphql-python/graphene-django) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/graphene-django?style=flat)](https://github.com/graphql-python/graphene-django/stargazers) - A Django integration for Graphene.
- [Flask-GraphQL-Auth](https://github.com/callsign-viper/Flask-GraphQL-Auth) [![GitHub stars](https://img.shields.io/github/stars/callsign-viper/Flask-GraphQL-Auth?style=flat)](https://github.com/callsign-viper/Flask-GraphQL-Auth/stargazers) - An authentication library for Flask inspired from flask-jwt-extended.
- [tartiflette](https://github.com/dailymotion/tartiflette) [![GitHub stars](https://img.shields.io/github/stars/dailymotion/tartiflette?style=flat)](https://github.com/dailymotion/tartiflette/stargazers) - Schema-first asynchronous GraphQL engine for Python.
- [tartiflette-aiohttp](https://github.com/tartiflette/tartiflette-aiohttp) [![GitHub stars](https://img.shields.io/github/stars/tartiflette/tartiflette-aiohttp?style=flat)](https://github.com/tartiflette/tartiflette-aiohttp/stargazers) - Wrapper for exposing Tartiflette GraphQL APIs over HTTP with aiohttp.
- [Ariadne](https://github.com/mirumee/ariadne) [![GitHub stars](https://img.shields.io/github/stars/mirumee/ariadne?style=flat)](https://github.com/mirumee/ariadne/stargazers) - Library for implementing GraphQL servers using a schema-first approach. Asynchronous query execution, batteries included for ASGI, WSGI and popular web frameworks with comprehensive documentation.
- [django-graphql-auth](https://github.com/PedroBern/django-graphql-auth) [![GitHub stars](https://img.shields.io/github/stars/PedroBern/django-graphql-auth?style=flat)](https://github.com/PedroBern/django-graphql-auth/stargazers) - Django registration and authentication with GraphQL.
- [strawberry](https://github.com/strawberry-graphql/strawberry) [![GitHub stars](https://img.shields.io/github/stars/strawberry-graphql/strawberry?style=flat)](https://github.com/strawberry-graphql/strawberry/stargazers) - Python GraphQL library that uses type annotations to define schemas.
- [turms](https://github.com/jhnnsrs/turms) [![GitHub stars](https://img.shields.io/github/stars/jhnnsrs/turms?style=flat)](https://github.com/jhnnsrs/turms/stargazers) - Pythonic GraphQL code generator built around graphql-core and Pydantic.
- [rath](https://github.com/jhnnsrs/rath) [![GitHub stars](https://img.shields.io/github/stars/jhnnsrs/rath?style=flat)](https://github.com/jhnnsrs/rath/stargazers) - Apollo-like GraphQL client with asynchronous and synchronous interfaces.
- [sgqlc](https://github.com/profusion/sgqlc) [![GitHub stars](https://img.shields.io/github/stars/profusion/sgqlc?style=flat)](https://github.com/profusion/sgqlc/stargazers) - Simple GraphQL Client makes working with GraphQL API responses easier in Python.

<a name="py-example" />

#### Python Examples

- [swapi-graphene](https://github.com/graphql-python/swapi-graphene) [![GitHub stars](https://img.shields.io/github/stars/graphql-python/swapi-graphene?style=flat)](https://github.com/graphql-python/swapi-graphene/stargazers) - GraphQL schema and server using Graphene.
- [Python Backend Tutorial](https://hasura.io/learn/graphql/backend-stack/languages/python/) - Tutorial on creating a GraphQL server with Strawberry and a client with Qlient.

<a name="java" />

### Java

- [graphql-java](https://github.com/graphql-java/graphql-java) [![GitHub stars](https://img.shields.io/github/stars/graphql-java/graphql-java?style=flat)](https://github.com/graphql-java/graphql-java/stargazers) - GraphQL Java implementation.
- [java-dataloader](https://github.com/graphql-java/java-dataloader) [![GitHub stars](https://img.shields.io/github/stars/graphql-java/java-dataloader?style=flat)](https://github.com/graphql-java/java-dataloader/stargazers) - DataLoader implementation that provides batching and caching to avoid N+1 data-fetching problems.
- [DGS Framework](https://github.com/Netflix/dgs-framework) [![GitHub stars](https://img.shields.io/github/stars/Netflix/dgs-framework?style=flat)](https://github.com/Netflix/dgs-framework/stargazers) - A GraphQL server framework for Spring Boot, developed by Netflix.
- [Spring for GraphQL](https://spring.io/projects/spring-graphql) - Official Spring integration for applications built on GraphQL Java.
- [MicroProfile GraphQL](https://github.com/microprofile/microprofile-graphql) [![GitHub stars](https://img.shields.io/github/stars/microprofile/microprofile-graphql?style=flat)](https://github.com/microprofile/microprofile-graphql/stargazers) - Specification for developing portable, code-first GraphQL services with Enterprise Java.
- [SmallRye GraphQL](https://github.com/smallrye/smallrye-graphql) [![GitHub stars](https://img.shields.io/github/stars/smallrye/smallrye-graphql?style=flat)](https://github.com/smallrye/smallrye-graphql/stargazers) - Implementation of MicroProfile GraphQL with server, client, and tooling support.
- [Micronaut GraphQL](https://github.com/micronaut-projects/micronaut-graphql) [![GitHub stars](https://img.shields.io/github/stars/micronaut-projects/micronaut-graphql?style=flat)](https://github.com/micronaut-projects/micronaut-graphql/stargazers) - Official Micronaut integration for building GraphQL Java servers.
- [Vert.x Web GraphQL](https://vertx.io/docs/vertx-web-graphql/java/) - Official GraphQL Java integration for Vert.x Web.
- [graphql-java-generator](https://github.com/graphql-java-generator) [![GitHub stars](https://img.shields.io/github/stars/graphql-java-generator?style=flat)](https://github.com/graphql-java-generator/stargazers) - Maven and Gradle plugins that generate both the **client** and the **server** (POJOs and utility classes). The server part is based on graphql-java and hides its boilerplate code.
- [gaphql-java-type-generator](https://github.com/graphql-java/graphql-java-type-generator) [![GitHub stars](https://img.shields.io/github/stars/graphql-java/graphql-java-type-generator?style=flat)](https://github.com/graphql-java/graphql-java-type-generator/stargazers) - Automatically generates types for use with GraphQL Java.
- [schemagen-graphql](https://github.com/bpatters/schemagen-graphql) [![GitHub stars](https://img.shields.io/github/stars/bpatters/schemagen-graphql?style=flat)](https://github.com/bpatters/schemagen-graphql/stargazers) - Schema generation and execution package that turns POJO's into a GraphQL Java queryable set of objects. Enables exposing any service as a GraphQL service using Annotations.
- [graphql-java-annotations](https://github.com/Enigmatis/graphql-java-annotations) [![GitHub stars](https://img.shields.io/github/stars/Enigmatis/graphql-java-annotations?style=flat)](https://github.com/Enigmatis/graphql-java-annotations/stargazers) - Provides annotations-based syntax for schema definition with GraphQL Java.
- [graphql-java-tools](https://github.com/graphql-java-kickstart/graphql-java-tools) [![GitHub stars](https://img.shields.io/github/stars/graphql-java-kickstart/graphql-java-tools?style=flat)](https://github.com/graphql-java-kickstart/graphql-java-tools/stargazers) - Schema-first graphql-java convenience library that makes it easy to bring your own implementations as data resolvers, inspired by graphql-tools for JS.
- [graphql-java-codegen-maven-plugin](https://github.com/kobylynskyi/graphql-java-codegen-maven-plugin) [![GitHub stars](https://img.shields.io/github/stars/kobylynskyi/graphql-java-codegen-maven-plugin?style=flat)](https://github.com/kobylynskyi/graphql-java-codegen-maven-plugin/stargazers) - Schema-first Maven plugin for generating Java types and resolver interfaces. Works with graphql-java-tools and was inspired by swagger-codegen-maven-plugin.
- [graphql-java-codegen-gradle-plugin](https://github.com/kobylynskyi/graphql-java-codegen-gradle-plugin) [![GitHub stars](https://img.shields.io/github/stars/kobylynskyi/graphql-java-codegen-gradle-plugin?style=flat)](https://github.com/kobylynskyi/graphql-java-codegen-gradle-plugin/stargazers) - Schema-first Gradle plugin for generating Java types and resolver interfaces. Works with graphql-java-tools and was inspired by gradle-swagger-generator-plugin.
- [graphql-java-servlet](https://github.com/graphql-java-kickstart/graphql-java-servlet) [![GitHub stars](https://img.shields.io/github/stars/graphql-java-kickstart/graphql-java-servlet?style=flat)](https://github.com/graphql-java-kickstart/graphql-java-servlet/stargazers) - A framework-agnostic java servlet for exposing graphql-java query endpoints with GET, POST, and multipart uploads.
- [manifold-graphql](https://github.com/manifold-systems/manifold/tree/master/manifold-deps-parent/manifold-graphql) [![GitHub stars](https://img.shields.io/github/stars/manifold-systems/manifold/tree/master/manifold-deps-parent/manifold-graphql?style=flat)](https://github.com/manifold-systems/manifold/tree/master/manifold-deps-parent/manifold-graphql/stargazers) - Comprehensive schema-first GraphQL client with type-safe types, queries, and results, no code generators, no POJOs, and no annotations. Includes IDE support for IntelliJ IDEA and Android Studio. See the [Java example](#java-examples) below.
- [spring-graphql-common](https://github.com/oembedler/spring-graphql-common) [![GitHub stars](https://img.shields.io/github/stars/oembedler/spring-graphql-common?style=flat)](https://github.com/oembedler/spring-graphql-common/stargazers) - Spring Framework GraphQL Library.
- [graphql-spring-boot](https://github.com/graphql-java-kickstart/graphql-spring-boot) [![GitHub stars](https://img.shields.io/github/stars/graphql-java-kickstart/graphql-spring-boot?style=flat)](https://github.com/graphql-java-kickstart/graphql-spring-boot/stargazers) - GraphQL and GraphiQL Spring Framework Boot Starters.
- [vertx-graphql-service-discovery](https://github.com/engagingspaces/vertx-graphql-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/engagingspaces/vertx-graphql-service-discovery?style=flat)](https://github.com/engagingspaces/vertx-graphql-service-discovery/stargazers) - Asynchronous GraphQL service discovery and querying for your microservices.
- [vertx-dataloader](https://github.com/engagingspaces/vertx-dataloader) [![GitHub stars](https://img.shields.io/github/stars/engagingspaces/vertx-dataloader?style=flat)](https://github.com/engagingspaces/vertx-dataloader/stargazers) - Port of Facebook DataLoader for efficient, asynchronous batching and caching in clustered GraphQL environments.
- [graphql-spqr](https://github.com/leangen/GraphQL-SPQR) [![GitHub stars](https://img.shields.io/github/stars/leangen/GraphQL-SPQR?style=flat)](https://github.com/leangen/GraphQL-SPQR/stargazers) - Java 8+ API for rapid development of GraphQL services.
- [Light Java GraphQL](https://github.com/networknt/light-graphql-4j) [![GitHub stars](https://img.shields.io/github/stars/networknt/light-graphql-4j?style=flat)](https://github.com/networknt/light-graphql-4j/stargazers) - Lightweight, fast microservices framework with cross-cutting concerns addressed and support for GraphQL schemas.
- [Elide](https://elide.io) - Java library that exposes a JPA-annotated data model as a GraphQL service over a relational database.
- [GraphQL JPA Query](https://github.com/introproventures/graphql-jpa-query) [![GitHub stars](https://img.shields.io/github/stars/introproventures/graphql-jpa-query?style=flat)](https://github.com/introproventures/graphql-jpa-query/stargazers) - Generates GraphQL query APIs from JPA entity models.
- [graphql-java-extended-validation](https://github.com/graphql-java/graphql-java-extended-validation) [![GitHub stars](https://img.shields.io/github/stars/graphql-java/graphql-java-extended-validation?style=flat)](https://github.com/graphql-java/graphql-java-extended-validation/stargazers) - Provides extended validation of fields and field arguments for graphql-java.
- [dgs-extended-formatters](https://github.com/setchy/dgs-extended-formatters) [![GitHub stars](https://img.shields.io/github/stars/setchy/dgs-extended-formatters?style=flat)](https://github.com/setchy/dgs-extended-formatters/stargazers) - An experimental set of DGS Directives for common formatting use-cases.

#### Custom Scalars

- [graphql-java-datetime](https://github.com/donbeave/graphql-java-datetime) [![GitHub stars](https://img.shields.io/github/stars/donbeave/graphql-java-datetime?style=flat)](https://github.com/donbeave/graphql-java-datetime/stargazers) - GraphQL ISO Date is a set of RFC 3339 compliant date/time scalar types to be used with graphql-java.
- [graphql-java-extended-scalars](https://github.com/graphql-java/graphql-java-extended-scalars) [![GitHub stars](https://img.shields.io/github/stars/graphql-java/graphql-java-extended-scalars?style=flat)](https://github.com/graphql-java/graphql-java-extended-scalars/stargazers) - Extended scalars for graphql-java.

<a name="java-example" />

#### Java Examples

- [light-java-graphql examples](https://github.com/networknt/light-example-4j/tree/master/graphql) [![GitHub stars](https://img.shields.io/github/stars/networknt/light-example-4j/tree/master/graphql?style=flat)](https://github.com/networknt/light-example-4j/tree/master/graphql/stargazers) - Examples of Light Java GraphQL and tutorials.
- [graphql-spqr-samples](https://github.com/leangen/graphql-spqr-samples) [![GitHub stars](https://img.shields.io/github/stars/leangen/graphql-spqr-samples?style=flat)](https://github.com/leangen/graphql-spqr-samples/stargazers) - An example GraphQL server written with Spring MVC and GraphQL-SPQR.
- [manifold-graphql sample](https://github.com/manifold-systems/manifold-sample-graphql-app) [![GitHub stars](https://img.shields.io/github/stars/manifold-systems/manifold-sample-graphql-app?style=flat)](https://github.com/manifold-systems/manifold-sample-graphql-app/stargazers) - A simple application, both client and server, demonstrating the Manifold GraphQL library.
- [graphql-java-kickstart_samples](https://github.com/graphql-java-kickstart/samples) [![GitHub stars](https://img.shields.io/github/stars/graphql-java-kickstart/samples?style=flat)](https://github.com/graphql-java-kickstart/samples/stargazers) - Samples for using the GraphQL Java Kickstart projects.
- [Spring for GraphQL reference](https://docs.spring.io/spring-graphql/reference/) - Official reference documentation for building GraphQL services with Spring.
- [Spring Boot backend tutorial](https://hasura.io/learn/graphql/backend-stack/languages/java/) - A tutorial creating a GraphQL server and client using Spring Boot and Netflix DGS.

<a name="kotlin" />

### Kotlin

- [graphql-kotlin](https://github.com/ExpediaGroup/graphql-kotlin) [![GitHub stars](https://img.shields.io/github/stars/ExpediaGroup/graphql-kotlin?style=flat)](https://github.com/ExpediaGroup/graphql-kotlin/stargazers) - GraphQL Kotlin implementation.
- [KGraphQL](https://github.com/aPureBase/KGraphQL) [![GitHub stars](https://img.shields.io/github/stars/aPureBase/KGraphQL?style=flat)](https://github.com/aPureBase/KGraphQL/stargazers) - Pure Kotlin implementation for setting up a GraphQL server.
- [Kobby](https://github.com/ermadmi78/kobby) [![GitHub stars](https://img.shields.io/github/stars/ermadmi78/kobby?style=flat)](https://github.com/ermadmi78/kobby/stargazers) - Codegen plugin of Kotlin DSL Client by GraphQL schema. The generated DSL supports execution of complex GraphQL queries, mutation and subscriptions in Kotlin with syntax similar to native GraphQL syntax.
- [Graphkt](https://github.com/cufyorg/graphkt) [![GitHub stars](https://img.shields.io/github/stars/cufyorg/graphkt?style=flat)](https://github.com/cufyorg/graphkt/stargazers) - DSL-based GraphQL server library for Kotlin, backed by graphql-java.

<a name="kotlin-example" />

#### Kotlin Examples

- [manifold-graphql sample](https://github.com/manifold-systems/manifold-sample-kotlin-app) [![GitHub stars](https://img.shields.io/github/stars/manifold-systems/manifold-sample-kotlin-app?style=flat)](https://github.com/manifold-systems/manifold-sample-kotlin-app/stargazers) - A simple GraphQL application, both client and server, demonstrating the Manifold GraphQL library with Kotlin.

<a name="c" />

### C/C++

- [libgraphqlparser](https://github.com/graphql/libgraphqlparser) [![GitHub stars](https://img.shields.io/github/stars/graphql/libgraphqlparser?style=flat)](https://github.com/graphql/libgraphqlparser/stargazers) - A GraphQL query parser in C++ with C and C++ APIs.
- [agoo-c](https://github.com/ohler55/agoo-c) [![GitHub stars](https://img.shields.io/github/stars/ohler55/agoo-c?style=flat)](https://github.com/ohler55/agoo-c/stargazers) - High-performance GraphQL server written in C with published benchmarks.
- [cppgraphqlgen](https://github.com/Microsoft/cppgraphqlgen) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/cppgraphqlgen?style=flat)](https://github.com/Microsoft/cppgraphqlgen/stargazers) - C++ GraphQL schema service generator.
- [CaffQL](https://github.com/caffeinetv/CaffQL) [![GitHub stars](https://img.shields.io/github/stars/caffeinetv/CaffQL?style=flat)](https://github.com/caffeinetv/CaffQL/stargazers) - Generates C++ client types and request/response serialization from a GraphQL introspection query.

<a name="go" />

### Go

- [GraphQL](https://github.com/graphql-go/graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-go/graphql?style=flat)](https://github.com/graphql-go/graphql/stargazers) - Implementation of GraphQL for Go that follows graphql-js.
- [graphql-go](https://github.com/graph-gophers/graphql-go) [![GitHub stars](https://img.shields.io/github/stars/graph-gophers/graphql-go?style=flat)](https://github.com/graph-gophers/graphql-go/stargazers) - GraphQL server with a focus on ease of use.
- [gql](https://github.com/kadirpekel/gql) [![GitHub stars](https://img.shields.io/github/stars/kadirpekel/gql?style=flat)](https://github.com/kadirpekel/gql/stargazers) - Code-first schema builder based on the reference Go implementation.
- [gqlgen](https://github.com/99designs/gqlgen) [![GitHub stars](https://img.shields.io/github/stars/99designs/gqlgen?style=flat)](https://github.com/99designs/gqlgen/stargazers) - Go generate-based GraphQL server library.
- [graphql-relay-go](https://github.com/graphql-go/relay) [![GitHub stars](https://img.shields.io/github/stars/graphql-go/relay?style=flat)](https://github.com/graphql-go/relay/stargazers) - A Go/Golang library to help construct a server supporting react-relay.
- [graphjin](https://github.com/dosco/graphjin) [![GitHub stars](https://img.shields.io/github/stars/dosco/graphjin?style=flat)](https://github.com/dosco/graphjin/stargazers) - Instant GraphQL-to-SQL compiler for building APIs quickly.
- [graphql-go-tools](https://github.com/wundergraph/graphql-go-tools) [![GitHub stars](https://img.shields.io/github/stars/wundergraph/graphql-go-tools?style=flat)](https://github.com/wundergraph/graphql-go-tools/stargazers) - GraphQL router and API gateway framework written in Go, focused on correctness, extensibility, and performance.
- [Thunder](https://github.com/Raezil/Thunder) [![GitHub stars](https://img.shields.io/github/stars/Raezil/Thunder?style=flat)](https://github.com/Raezil/Thunder/stargazers) - Scalable microservices framework powered by Go, gRPC-Gateway, Prisma, and Kubernetes that exposes REST, gRPC, and GraphQL.
- [grpc-graphql-gateway](https://github.com/ysugimoto/grpc-graphql-gateway) [![GitHub stars](https://img.shields.io/github/stars/ysugimoto/grpc-graphql-gateway?style=flat)](https://github.com/ysugimoto/grpc-graphql-gateway/stargazers) - Protoc plugin that generates GraphQL execution code from Protocol Buffers.
<a name="go-example" />

#### Go Examples

- [golang-relay-starter-kit](https://github.com/sogko/golang-relay-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/sogko/golang-relay-starter-kit?style=flat)](https://github.com/sogko/golang-relay-starter-kit/stargazers) - Barebones starting point for a Relay application with Golang GraphQL server.
- [todomvc-relay-go](https://github.com/sogko/todomvc-relay-go) [![GitHub stars](https://img.shields.io/github/stars/sogko/todomvc-relay-go?style=flat)](https://github.com/sogko/todomvc-relay-go/stargazers) - Port of the React/Relay TodoMVC app, driven by a Golang GraphQL backend.
- [go-graphql-subscription-example](https://github.com/ccamel/go-graphql-subscription-example) [![GitHub stars](https://img.shields.io/github/stars/ccamel/go-graphql-subscription-example?style=flat)](https://github.com/ccamel/go-graphql-subscription-example/stargazers) - A GraphQL schema and server that demonstrates GraphQL [subscriptions](https://github.com/apollographql/subscriptions-transport-ws/blob/v0.9.4/PROTOCOL.md) [![GitHub stars](https://img.shields.io/github/stars/apollographql/subscriptions-transport-ws/blob/v0.9.4/PROTOCOL.md?style=flat)](https://github.com/apollographql/subscriptions-transport-ws/blob/v0.9.4/PROTOCOL.md/stargazers) over WebSocket to consume [Apache Kafka](https://kafka.apache.org/) messages.
- [Go Backend Tutorial](https://hasura.io/learn/graphql/backend-stack/languages/go/) - A tutorial showing how to make a Go GraphQL server and client using code generation.

<a name="scala" />

### Scala

- [sangria](https://github.com/sangria-graphql/sangria) [![GitHub stars](https://img.shields.io/github/stars/sangria-graphql/sangria?style=flat)](https://github.com/sangria-graphql/sangria/stargazers) - Scala GraphQL server implementation.
- [sangria-relay](https://github.com/sangria-graphql/sangria-relay) [![GitHub stars](https://img.shields.io/github/stars/sangria-graphql/sangria-relay?style=flat)](https://github.com/sangria-graphql/sangria-relay/stargazers) - Sangria Relay Support.
- [caliban](https://github.com/ghostdogpr/caliban) [![GitHub stars](https://img.shields.io/github/stars/ghostdogpr/caliban?style=flat)](https://github.com/ghostdogpr/caliban/stargazers) - Purely functional library for creating GraphQL backends in Scala.

<a name="scala-example" />

#### Scala Examples

- [sangria-akka-http-example](https://github.com/sangria-graphql/sangria-akka-http-example) [![GitHub stars](https://img.shields.io/github/stars/sangria-graphql/sangria-akka-http-example?style=flat)](https://github.com/sangria-graphql/sangria-akka-http-example/stargazers) - An example GraphQL server written with akka-http and [sangria](https://sangria-graphql.github.io/).
- [sangria-playground](https://github.com/sangria-graphql/sangria-playground) [![GitHub stars](https://img.shields.io/github/stars/sangria-graphql/sangria-playground?style=flat)](https://github.com/sangria-graphql/sangria-playground/stargazers) - An example of GraphQL server written with Play and sangria.

<a name="dotnet" />

### .NET

- [graphql-dotnet](https://github.com/graphql-dotnet/graphql-dotnet) [![GitHub stars](https://img.shields.io/github/stars/graphql-dotnet/graphql-dotnet?style=flat)](https://github.com/graphql-dotnet/graphql-dotnet/stargazers) - GraphQL for .NET.
- [graphql-net](https://github.com/ckimes89/graphql-net) [![GitHub stars](https://img.shields.io/github/stars/ckimes89/graphql-net?style=flat)](https://github.com/ckimes89/graphql-net/stargazers) - GraphQL to IQueryable for .NET.
- [Hot Chocolate](https://github.com/ChilliCream/graphql-platform) [![GitHub stars](https://img.shields.io/github/stars/ChilliCream/graphql-platform?style=flat)](https://github.com/ChilliCream/graphql-platform/stargazers) - .NET GraphQL platform containing the Hot Chocolate server, Strawberry Shake client, and Nitro IDE.
- [Snowflaqe](https://github.com/Zaid-Ajaj/Snowflaqe) [![GitHub stars](https://img.shields.io/github/stars/Zaid-Ajaj/Snowflaqe?style=flat)](https://github.com/Zaid-Ajaj/Snowflaqe/stargazers) - Type-safe GraphQL code generator for F# and Fable.
- [EntityGraphQL](https://github.com/EntityGraphQL/EntityGraphQL) [![GitHub stars](https://img.shields.io/github/stars/EntityGraphQL/EntityGraphQL?style=flat)](https://github.com/EntityGraphQL/EntityGraphQL/stargazers) - Library for building a GraphQL API on top of a data model with support for multiple data sources.
- [ZeroQL](https://github.com/byme8/ZeroQL) [![GitHub stars](https://img.shields.io/github/stars/byme8/ZeroQL?style=flat)](https://github.com/byme8/ZeroQL/stargazers) - Type-safe GraphQL client with a LINQ-like interface for C#.

<a name="net-example" />

#### .NET Examples

- [.NET backend tutorial](https://hasura.io/learn/graphql/backend-stack/languages/dotnet/) - A tutorial creating a GraphQL server and client with .NET.

<a name="elixir" />

### Elixir

- [absinthe-graphql](https://github.com/absinthe-graphql/absinthe) [![GitHub stars](https://img.shields.io/github/stars/absinthe-graphql/absinthe?style=flat)](https://github.com/absinthe-graphql/absinthe/stargazers) - Fully Featured Elixir GraphQL Library.
- [graphql-elixir](https://github.com/graphql-elixir/graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-elixir/graphql?style=flat)](https://github.com/graphql-elixir/graphql/stargazers) - GraphQL Elixir. (No longer maintained)
- [plug_graphql](https://github.com/graphql-elixir/plug_graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-elixir/plug_graphql?style=flat)](https://github.com/graphql-elixir/plug_graphql/stargazers) - Plug integration for GraphQL Elixir.
- [graphql_relay](https://github.com/graphql-elixir/graphql_relay) [![GitHub stars](https://img.shields.io/github/stars/graphql-elixir/graphql_relay?style=flat)](https://github.com/graphql-elixir/graphql_relay/stargazers) - Relay helpers for GraphQL Elixir.
- [graphql_parser](https://github.com/graphql-elixir/graphql_parser) [![GitHub stars](https://img.shields.io/github/stars/graphql-elixir/graphql_parser?style=flat)](https://github.com/graphql-elixir/graphql_parser/stargazers) - Elixir bindings for libgraphqlparser.
- [GraphQL](https://github.com/asonge/graphql) [![GitHub stars](https://img.shields.io/github/stars/asonge/graphql?style=flat)](https://github.com/asonge/graphql/stargazers) - Elixir GraphQL parser.
- [plot](https://github.com/peburrows/plot) [![GitHub stars](https://img.shields.io/github/stars/peburrows/plot?style=flat)](https://github.com/peburrows/plot/stargazers) - GraphQL parser and resolver for Elixir.

<a name="elixir-example" />

#### Elixir Examples

- [hello_graphql_phoenix](https://github.com/graphql-elixir/hello_graphql_phoenix) [![GitHub stars](https://img.shields.io/github/stars/graphql-elixir/hello_graphql_phoenix?style=flat)](https://github.com/graphql-elixir/hello_graphql_phoenix/stargazers) - Examples of GraphQL Elixir Plug endpoints mounted in Phoenix.

<a name="haskell" />

### Haskell

- [graphql-haskell](https://github.com/jdnavarro/graphql-haskell) [![GitHub stars](https://img.shields.io/github/stars/jdnavarro/graphql-haskell?style=flat)](https://github.com/jdnavarro/graphql-haskell/stargazers) - GraphQL AST and parser for Haskell.
- [morpheus-graphql](https://github.com/morpheusgraphql/morpheus-graphql) [![GitHub stars](https://img.shields.io/github/stars/morpheusgraphql/morpheus-graphql?style=flat)](https://github.com/morpheusgraphql/morpheus-graphql/stargazers) - Haskell GraphQL Api, Client and Tools.

<a name="sql" />

### SQL

- [GraphpostgresQL](https://github.com/solidsnack/GraphpostgresQL) [![GitHub stars](https://img.shields.io/github/stars/solidsnack/GraphpostgresQL?style=flat)](https://github.com/solidsnack/GraphpostgresQL/stargazers) - GraphQL for Postgres.
- [sql-to-graphql](https://github.com/rexxars/sql-to-graphql) [![GitHub stars](https://img.shields.io/github/stars/rexxars/sql-to-graphql?style=flat)](https://github.com/rexxars/sql-to-graphql/stargazers) - Generate a GraphQL API based on your SQL database structure.
- [PostGraphile](https://github.com/graphile/crystal) [![GitHub stars](https://img.shields.io/github/stars/graphile/crystal?style=flat)](https://github.com/graphile/crystal/stargazers) - Extensible, plugin-based tooling for building high-performance GraphQL APIs from PostgreSQL schemas.
- [Hasura](https://github.com/hasura/graphql-engine) [![GitHub stars](https://img.shields.io/github/stars/hasura/graphql-engine?style=flat)](https://github.com/hasura/graphql-engine/stargazers) - Provides instant real-time GraphQL APIs over new or existing PostgreSQL databases.

<a name="lua" />

### Lua

- [graphql-lua](https://github.com/bjornbytes/graphql-lua) [![GitHub stars](https://img.shields.io/github/stars/bjornbytes/graphql-lua?style=flat)](https://github.com/bjornbytes/graphql-lua/stargazers) - GraphQL for Lua.

<a name="elm" />

### Elm

- [elm-graphql](https://github.com/dillonkearns/elm-graphql) [![GitHub stars](https://img.shields.io/github/stars/dillonkearns/elm-graphql?style=flat)](https://github.com/dillonkearns/elm-graphql/stargazers) - GraphQL for Elm.

<a name="clojure" />

### Clojure

- [graphql-clj](https://github.com/tendant/graphql-clj) [![GitHub stars](https://img.shields.io/github/stars/tendant/graphql-clj?style=flat)](https://github.com/tendant/graphql-clj/stargazers) - A Clojure library designed to provide GraphQL implementation.
- [Lacinia](https://github.com/walmartlabs/lacinia) [![GitHub stars](https://img.shields.io/github/stars/walmartlabs/lacinia?style=flat)](https://github.com/walmartlabs/lacinia/stargazers) - GraphQL implementation in pure Clojure.
- [graphql-query](https://github.com/district0x/graphql-query) [![GitHub stars](https://img.shields.io/github/stars/district0x/graphql-query?style=flat)](https://github.com/district0x/graphql-query/stargazers) - Clojure(Script) GraphQL query generation.

<a name="clojure-example" />

#### Clojure Examples

- [Clojure Game Geek](https://github.com/walmartlabs/clojure-game-geek) [![GitHub stars](https://img.shields.io/github/stars/walmartlabs/clojure-game-geek?style=flat)](https://github.com/walmartlabs/clojure-game-geek/stargazers) - Example code for the Lacinia GraphQL framework tutorial.

<a name="swift" />

### Swift

- [GraphQL](https://github.com/GraphQLSwift/GraphQL) [![GitHub stars](https://img.shields.io/github/stars/GraphQLSwift/GraphQL?style=flat)](https://github.com/GraphQLSwift/GraphQL/stargazers) - The Swift implementation for GraphQL.

<a name="ocaml" />

### OCaml

- [ocaml-graphql-server](https://github.com/andreas/ocaml-graphql-server) [![GitHub stars](https://img.shields.io/github/stars/andreas/ocaml-graphql-server?style=flat)](https://github.com/andreas/ocaml-graphql-server/stargazers) - GraphQL servers in OCaml.

<a name="android" />

### Android

- [apollo-kotlin](https://github.com/apollographql/apollo-kotlin) [![GitHub stars](https://img.shields.io/github/stars/apollographql/apollo-kotlin?style=flat)](https://github.com/apollographql/apollo-kotlin/stargazers) - A strongly typed, caching GraphQL client for the JVM, Android, and Kotlin Multiplatform.

<a name="android-example" />

#### Android Examples

- [apollo-frontpage-android-app](https://github.com/rnitame/apollo-frontpage-android-app) [![GitHub stars](https://img.shields.io/github/stars/rnitame/apollo-frontpage-android-app?style=flat)](https://github.com/rnitame/apollo-frontpage-android-app/stargazers) - 📄 Apollo "hello world" app, for Android.

<a name="ios" />

### iOS

- [apollo-ios](https://github.com/apollographql/apollo-ios) [![GitHub stars](https://img.shields.io/github/stars/apollographql/apollo-ios?style=flat)](https://github.com/apollographql/apollo-ios/stargazers) - 📱 A strongly-typed, caching GraphQL client for iOS, written in Swift.
- [ApolloDeveloperKit](https://github.com/manicmaniac/ApolloDeveloperKit) [![GitHub stars](https://img.shields.io/github/stars/manicmaniac/ApolloDeveloperKit?style=flat)](https://github.com/manicmaniac/ApolloDeveloperKit/stargazers) - Apollo Client developer tools bridge for Apollo iOS.
- [Graphaello](https://github.com/nerdsupremacist/Graphaello) [![GitHub stars](https://img.shields.io/github/stars/nerdsupremacist/Graphaello?style=flat)](https://github.com/nerdsupremacist/Graphaello/stargazers) - Type Safe GraphQL directly from SwiftUI.

<a name="ios-example" />

#### iOS Examples

- [frontpage-ios-app](https://github.com/apollographql/frontpage-ios-app) [![GitHub stars](https://img.shields.io/github/stars/apollographql/frontpage-ios-app?style=flat)](https://github.com/apollographql/frontpage-ios-app/stargazers) - 📄 Apollo "hello world" app, for iOS.

<a name="clojurescript" />

### ClojureScript

- [re-graph](https://github.com/oliyh/re-graph) [![GitHub stars](https://img.shields.io/github/stars/oliyh/re-graph?style=flat)](https://github.com/oliyh/re-graph/stargazers) - A GraphQL client for ClojureScript with bindings for re-frame applications.

<a name="reasonml" />

### ReasonML

- [reason-apollo](https://github.com/apollographql/reason-apollo) [![GitHub stars](https://img.shields.io/github/stars/apollographql/reason-apollo?style=flat)](https://github.com/apollographql/reason-apollo/stargazers) - ReasonML binding for Apollo Client.
- [ReasonQL](https://github.com/sainthkh/reasonql) [![GitHub stars](https://img.shields.io/github/stars/sainthkh/reasonql?style=flat)](https://github.com/sainthkh/reasonql/stargazers) - Type-safe and simple GraphQL Client for ReasonML developers.
- [reason-urql](https://github.com/FormidableLabs/reason-urql) [![GitHub stars](https://img.shields.io/github/stars/FormidableLabs/reason-urql?style=flat)](https://github.com/FormidableLabs/reason-urql/stargazers) - ReasonML binding for urql Client.

<a name="dart" />

### Dart

- [graphql-flutter](https://github.com/zino-app/graphql-flutter) [![GitHub stars](https://img.shields.io/github/stars/zino-app/graphql-flutter?style=flat)](https://github.com/zino-app/graphql-flutter/stargazers) - A GraphQL client for Flutter.
- [Artemis](https://github.com/comigor/artemis) [![GitHub stars](https://img.shields.io/github/stars/comigor/artemis?style=flat)](https://github.com/comigor/artemis/stargazers) - A GraphQL type and query generator for Dart/Flutter.

<a name="rust" />

### Rust

- [async-graphql](https://github.com/async-graphql/async-graphql) [![GitHub stars](https://img.shields.io/github/stars/async-graphql/async-graphql?style=flat)](https://github.com/async-graphql/async-graphql/stargazers) - High-performance server-side library that supports all GraphQL specifications.
- [juniper](https://github.com/graphql-rust/juniper) [![GitHub stars](https://img.shields.io/github/stars/graphql-rust/juniper?style=flat)](https://github.com/graphql-rust/juniper/stargazers) - GraphQL server library for Rust.
- [graphql-client](https://github.com/tomhoule/graphql-client) [![GitHub stars](https://img.shields.io/github/stars/tomhoule/graphql-client?style=flat)](https://github.com/tomhoule/graphql-client/stargazers) - GraphQL client library for Rust with WebAssembly support.
- [graphql-parser](https://github.com/graphql-rust/graphql-parser) [![GitHub stars](https://img.shields.io/github/stars/graphql-rust/graphql-parser?style=flat)](https://github.com/graphql-rust/graphql-parser/stargazers) - A parser, formatter and AST for the GraphQL query and schema definition language for Rust.

<a name="rust-example" />

#### Rust Examples

- [Warp GraphQL Juniper](https://graphql-rust.github.io/) - Warp web framework integration example with a Juniper GraphQL server.

<a name="d" />

### D (dlang)

- [graphqld](https://github.com/burner/graphqld) [![GitHub stars](https://img.shields.io/github/stars/burner/graphqld?style=flat)](https://github.com/burner/graphqld/stargazers) - GraphQL server library for D.

<a name="r" />

### R (Rstat)

- [ghql](https://github.com/ropensci/ghql) [![GitHub stars](https://img.shields.io/github/stars/ropensci/ghql?style=flat)](https://github.com/ropensci/ghql/stargazers) - General purpose GraphQL R client.
- [GraphQL](https://github.com/ropensci/graphql) [![GitHub stars](https://img.shields.io/github/stars/ropensci/graphql?style=flat)](https://github.com/ropensci/graphql/stargazers) - Bindings to the 'libgraphqlparser' C++ library. Parses GraphQL syntax and exports the AST in JSON format.
- [gqlr](https://github.com/schloerke/gqlr) [![GitHub stars](https://img.shields.io/github/stars/schloerke/gqlr?style=flat)](https://github.com/schloerke/gqlr/stargazers) - R GraphQL Implementation.

<a name="julia" />

### Julia

- [Diana.jl](https://github.com/codeneomatrix/Diana.jl) [![GitHub stars](https://img.shields.io/github/stars/codeneomatrix/Diana.jl?style=flat)](https://github.com/codeneomatrix/Diana.jl/stargazers) - A Julia GraphQL client/server implementation.
- [GraphQLClient.jl](https://github.com/DeloitteDigitalAPAC/GraphQLClient.jl) [![GitHub stars](https://img.shields.io/github/stars/DeloitteDigitalAPAC/GraphQLClient.jl?style=flat)](https://github.com/DeloitteDigitalAPAC/GraphQLClient.jl/stargazers) - A Julia GraphQL client for seamless integration with a server.

<a name="crystal" />

### Crystal

- [GraphQL](https://github.com/graphql-crystal/graphql) [![GitHub stars](https://img.shields.io/github/stars/graphql-crystal/graphql?style=flat)](https://github.com/graphql-crystal/graphql/stargazers) - Server library for Crystal.
- [graphql-crystal](https://github.com/ziprandom/graphql-crystal) [![GitHub stars](https://img.shields.io/github/stars/ziprandom/graphql-crystal?style=flat)](https://github.com/ziprandom/graphql-crystal/stargazers) - Library inspired by graphql-ruby, go-graphql, and graphql-parser.
- [crystal-gql](https://github.com/itsezc/crystal-gql) [![GitHub stars](https://img.shields.io/github/stars/itsezc/crystal-gql?style=flat)](https://github.com/itsezc/crystal-gql/stargazers) - GraphQL client shard inspired by Apollo client.
- [graphql.cr](https://github.com/garymardell/graphql.cr) [![GitHub stars](https://img.shields.io/github/stars/garymardell/graphql.cr?style=flat)](https://github.com/garymardell/graphql.cr/stargazers) - GraphQL shard.

### Ballerina

- [GraphQL](https://github.com/ballerina-platform/module-ballerina-graphql) [![GitHub stars](https://img.shields.io/github/stars/ballerina-platform/module-ballerina-graphql?style=flat)](https://github.com/ballerina-platform/module-ballerina-graphql/stargazers) - Standard Ballerina library providing GraphQL client and server implementations with built-in subscription support.
- [GraphQL CLI](https://github.com/ballerina-platform/graphql-tools) [![GitHub stars](https://img.shields.io/github/stars/ballerina-platform/graphql-tools?style=flat)](https://github.com/ballerina-platform/graphql-tools/stargazers) - A CLI tool to generate Ballerina code from GraphQL schema and GraphQL schema from Ballerina code. It also provides functionality to generate usage-specific GraphQL clients using GraphQL schemas and documents.

#### Ballerina Samples

- [Ballerina GraphQL Examples](https://github.com/ballerina-platform/module-ballerina-graphql/tree/master/examples) [![GitHub stars](https://img.shields.io/github/stars/ballerina-platform/module-ballerina-graphql/tree/master/examples?style=flat)](https://github.com/ballerina-platform/module-ballerina-graphql/tree/master/examples/stargazers) - Sample implementations of GraphQL services in Ballerina.
- [Convert Weather REST API to GraphQL API](https://github.com/ThisaruGuruge/weather-rest-api-to-graphql) [![GitHub stars](https://img.shields.io/github/stars/ThisaruGuruge/weather-rest-api-to-graphql?style=flat)](https://github.com/ThisaruGuruge/weather-rest-api-to-graphql/stargazers) - Example demonstrating REST API conversion to GraphQL.

<a name="tools" />

## Tools

### Tools - IDEs & Schema Explorers

- [GraphiQL](https://github.com/graphql/graphiql) [![GitHub stars](https://img.shields.io/github/stars/graphql/graphiql?style=flat)](https://github.com/graphql/graphiql/stargazers) - Reference ecosystem for building browser and IDE tools around GraphQL and the GraphQL language server.
- [GraphQL Editor](https://github.com/graphql-editor/graphql-editor) [![GitHub stars](https://img.shields.io/github/stars/graphql-editor/graphql-editor?style=flat)](https://github.com/graphql-editor/graphql-editor/stargazers) - Visual Editor & GraphQL IDE.
- [GraphQL Voyager](https://github.com/APIs-guru/graphql-voyager) [![GitHub stars](https://img.shields.io/github/stars/APIs-guru/graphql-voyager?style=flat)](https://github.com/APIs-guru/graphql-voyager/stargazers) - Represent any GraphQL API as an interactive graph.
- [Brangr](https://github.com/networkimprov/brangr) [![GitHub stars](https://img.shields.io/github/stars/networkimprov/brangr?style=flat)](https://github.com/networkimprov/brangr/stargazers) - A unique, user-friendly data browser/viewer for any GraphQL service, with attractive result layouts.
- [GraphQL Birdseye](https://github.com/Novvum/graphql-birdseye) [![GitHub stars](https://img.shields.io/github/stars/Novvum/graphql-birdseye?style=flat)](https://github.com/Novvum/graphql-birdseye/stargazers) - View any GraphQL schema as a dynamic and interactive graph.
- [AST Explorer](https://astexplorer.net/) - Select "GraphQL" at the top, explore the GraphQL AST and highlight different parts by clicking in the query.
- [CraftQL](https://github.com/yamafaktory/craftql) [![GitHub stars](https://img.shields.io/github/stars/yamafaktory/craftql?style=flat)](https://github.com/yamafaktory/craftql/stargazers) - A CLI tool to visualize GraphQL schemas and to output a graph data structure as a graphviz .dot format.
- [Hackolade](https://studio.hackolade.com/) - Visual GraphQL schema editor that generates Schema Definition Language files and documents existing endpoints with introspection.
- [Smart Formatter - GraphQL Query Formatter](https://smartformatter.com/tools/graphql-query-formatter) - A client-side, browser-only tool to format, beautify, and validate GraphQL queries and schemas instantly.
- [GraphVinci](https://github.com/Comcast/graphvinci) [![GitHub stars](https://img.shields.io/github/stars/Comcast/graphvinci?style=flat)](https://github.com/Comcast/graphvinci/stargazers) - An interactive schema visualizer for GraphQL APIs.

### Tools - API Clients & Workbenches

- [Altair GraphQL Client](https://github.com/altair-graphql/altair) [![GitHub stars](https://img.shields.io/github/stars/altair-graphql/altair?style=flat)](https://github.com/altair-graphql/altair/stargazers) - A beautiful feature-rich GraphQL Client for all platforms.
- [Insomnia](https://insomnia.rest/) - A full-featured API client with first-party GraphQL query editor.
- [Postman](https://learning.postman.com/docs/sending-requests/supported-api-frameworks/graphql/) - An HTTP Client that supports editing GraphQL queries.
- [Bruno](https://github.com/usebruno/bruno) [![GitHub stars](https://img.shields.io/github/stars/usebruno/bruno?style=flat)](https://github.com/usebruno/bruno/stargazers) - Fast, open source API client, which stores collections offline-only in a Git-friendly plain text markup language.
- [Escape GraphMan](https://github.com/Escape-Technologies/graphman) [![GitHub stars](https://img.shields.io/github/stars/Escape-Technologies/graphman?style=flat)](https://github.com/Escape-Technologies/graphman/stargazers) - Generate a complete Postman collection from a GraphQL endpoint.
- [Apollo Sandbox](https://sandbox.apollo.dev/) - The quickest way to navigate and test your GraphQL endpoints.
- [Firecamp - GraphQL Playground](https://firecamp.io/graphql) - The fastest collaborative GraphQL playground.
- [gqt](https://github.com/eerimoq/gqt) [![GitHub stars](https://img.shields.io/github/stars/eerimoq/gqt?style=flat)](https://github.com/eerimoq/gqt/stargazers) - Build and execute GraphQL queries in the terminal.
- [Mongrel](https://www.visorcraft.com/) - Desktop workbench with a GraphQL client, plus HTTP, WebSocket, and gRPC, inside a multi-database GUI.
- [GalleonQL](https://galleonql.com/) - A desktop API client built specifically for GraphQL (macOS, Windows, Linux), pairing an introspected schema browser with an incremental query builder and switchable endpoint profiles.


<a name="tool-testing" />

### Tools - Testing, Prototyping & Mocking

- [Beeceptor](https://beeceptor.com/graphql-mock-server/) - A no-code platform for creating AI-powered **GraphQL Mock Servers** from your schema (SDL) with rules, stateful mocking, mutation/subscription, to speed up development and integration testing.
- [graphql-to-karate](https://github.com/wbaldoumas/graphql-to-karate) [![GitHub stars](https://img.shields.io/github/stars/wbaldoumas/graphql-to-karate?style=flat)](https://github.com/wbaldoumas/graphql-to-karate/stargazers) - **Generate Karate API tests** from your GraphQL schemas.
- [GraphQL Faker](https://github.com/APIs-guru/graphql-faker) [![GitHub stars](https://img.shields.io/github/stars/APIs-guru/graphql-faker?style=flat)](https://github.com/APIs-guru/graphql-faker/stargazers) - 🎲 Mock or extend your GraphQL API with faked data. No coding required.
- [GraphQL Inspector](https://the-guild.dev/graphql/inspector) - A tool to **validate schemas**, compare schema changes, find breaking changes, and check document coverage against a schema.
- [Microcks](https://microcks.io/) - Open source, cloud native tool for API mocking and testing with GraphQL support.
- [mockd](https://github.com/getmockd/mockd) [![GitHub stars](https://img.shields.io/github/stars/getmockd/mockd?style=flat)](https://github.com/getmockd/mockd/stargazers) - Multi-protocol mock server with GraphQL schema mocking, resolver configuration, and query validation. Also supports HTTP, gRPC, WebSocket, MQTT, and SOAP.
- [Keploy](https://keploy.io/) - Open-source AI Powered API testing tool that generates test cases and **data mocks automatically by recording real API traffic**. Supports GraphQL, REST, and gRPC.
- [Step CI](https://stepci.com) - Open source API **testing and monitoring** with GraphQL support.
- [MockBase](https://mockbase.org) - Hosted mock server for REST, GraphQL, and SOAP with fault injection, stateful mocks, and OpenAPI import.
- [json-graphql-server](https://github.com/marmelab/json-graphql-server) [![GitHub stars](https://img.shields.io/github/stars/marmelab/json-graphql-server?style=flat)](https://github.com/marmelab/json-graphql-server/stargazers) - Get a full fake GraphQL API with zero coding in less than 30 seconds, based on a JSON data file.
- [supertest-graphql](https://github.com/alexstrat/supertest-graphql) [![GitHub stars](https://img.shields.io/github/stars/alexstrat/supertest-graphql?style=flat)](https://github.com/alexstrat/supertest-graphql/stargazers) - Extends supertest to easily test a GraphQL endpoint.
- [schemathesis](https://github.com/schemathesis/schemathesis) [![GitHub stars](https://img.shields.io/github/stars/schemathesis/schemathesis?style=flat)](https://github.com/schemathesis/schemathesis/stargazers) - Runs arbitrary queries matching a GraphQL schema to find server errors.

<a name="tool-security" />

### Tools - Security

- [GraphCrawler - The all-in-one GraphQL Security toolkit](https://github.com/gsmith257-cyber/GraphCrawler) [![GitHub stars](https://img.shields.io/github/stars/gsmith257-cyber/GraphCrawler?style=flat)](https://github.com/gsmith257-cyber/GraphCrawler/stargazers) - Automated penetration testing toolkit for GraphQL, written in Python.
- [Escape - The GraphQL Security Scanner](https://graphql.security/) - One-click security scan of your GraphQL endpoints. Free, no login required.
- [Escape Graphinder - GraphQL Subdomain Enumeration](https://github.com/Escape-Technologies/graphinder) [![GitHub stars](https://img.shields.io/github/stars/Escape-Technologies/graphinder?style=flat)](https://github.com/Escape-Technologies/graphinder/stargazers) - Blazing fast GraphQL endpoint finder using subdomain enumeration, script analysis, and brute force.
- [StackHawk - GraphQL Vulnerability Scanner](https://www.stackhawk.com/blog/automated-graphql-security-testing) - Automated GraphQL security scanning and vulnerability detection.
- [InQL Scanner](https://github.com/doyensec/inql) [![GitHub stars](https://img.shields.io/github/stars/doyensec/inql?style=flat)](https://github.com/doyensec/inql/stargazers) - Burp extension for GraphQL security testing.
- [GraphQL Raider](https://portswigger.net/bappstore/4841f0d78a554ca381c65b26d48207e6) - Burp Suite extension for GraphQL security testing.
- [WAF for GraphQL](https://lab.wallarm.com/api-security-solution/) - Web application firewall for GraphQL APIs.
- [GraphQL Intruder](https://github.com/davinerd/gql_intruder) [![GitHub stars](https://img.shields.io/github/stars/davinerd/gql_intruder?style=flat)](https://github.com/davinerd/gql_intruder/stargazers) - Plugin-based Python script for performing GraphQL vulnerability assessments.
- [GraphQL Cop](https://github.com/dolevf/graphql-cop) [![GitHub stars](https://img.shields.io/github/stars/dolevf/graphql-cop?style=flat)](https://github.com/dolevf/graphql-cop/stargazers) - Security audit utility for GraphQL.
- [GraphQLer](https://github.com/omar2535/GraphQLer) [![GitHub stars](https://img.shields.io/github/stars/omar2535/GraphQLer?style=flat)](https://github.com/omar2535/GraphQLer/stargazers) - Dependency-aware dynamic GraphQL testing tool.
- [Vulert](https://vulert.com) - Detects vulnerabilities in open source dependencies without accessing code, with support for JavaScript, PHP, Java, Python, and more.
- [hasura-security](https://github.com/Perufitlife/hasura-security) [![GitHub stars](https://img.shields.io/github/stars/Perufitlife/hasura-security?style=flat)](https://github.com/Perufitlife/hasura-security/stargazers) - Active-probe security auditor for self-hosted Hasura GraphQL Engine that detects open introspection, public-role data leaks, and unauthenticated endpoints.
- [graphql-armor](https://github.com/Escape-Technologies/graphql-armor) [![GitHub stars](https://img.shields.io/github/stars/Escape-Technologies/graphql-armor?style=flat)](https://github.com/Escape-Technologies/graphql-armor/stargazers) - An instant security layer for production GraphQL Endpoints.
- [goctopus](https://github.com/Escape-Technologies/goctopus) [![GitHub stars](https://img.shields.io/github/stars/Escape-Technologies/goctopus?style=flat)](https://github.com/Escape-Technologies/goctopus/stargazers) - Fast GraphQL discovery and fingerprinting toolbox.

### Tools - Developer Extensions

- [Apollo Client Developer Tools](https://github.com/apollographql/apollo-client-devtools) [![GitHub stars](https://img.shields.io/github/stars/apollographql/apollo-client-devtools?style=flat)](https://github.com/apollographql/apollo-client-devtools/stargazers) - GraphQL debugging tools for Apollo Client in the Chrome developer console.
- [GraphQL Network Inspector](https://chrome.google.com/webstore/detail/graphql-network-inspector/ndlbedplllcgconngcnfmkadhokfaaln) - A simple and clean chrome dev-tools extension for GraphQL network inspection.
- [Apollo GraphQL VSCode Extension](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo) - Rich editor support for GraphQL client and server development that integrates with the Apollo platform.
- [js-graphql-intellij-plugin](https://github.com/jimkyndemeyer/js-graphql-intellij-plugin/) [![GitHub stars](https://img.shields.io/github/stars/jimkyndemeyer/js-graphql-intellij-plugin/?style=flat)](https://github.com/jimkyndemeyer/js-graphql-intellij-plugin//stargazers) - GraphQL language support for IntelliJ IDEA and WebStorm, including Relay.QL tagged templates in JavaScript and TypeScript.
- [vim-graphql](https://github.com/jparise/vim-graphql) [![GitHub stars](https://img.shields.io/github/stars/jparise/vim-graphql?style=flat)](https://github.com/jparise/vim-graphql/stargazers) - A Vim plugin that provides GraphQL file detection and syntax highlighting.
- [graphql-autocomplete](https://github.com/orionsoft/atom-graphql-autocomplete) [![GitHub stars](https://img.shields.io/github/stars/orionsoft/atom-graphql-autocomplete?style=flat)](https://github.com/orionsoft/atom-graphql-autocomplete/stargazers) - Autocomplete and lint from a GraphQL endpoint in Atom.
- [ts-graphql-plugin](https://github.com/Quramy/ts-graphql-plugin) [![GitHub stars](https://img.shields.io/github/stars/Quramy/ts-graphql-plugin?style=flat)](https://github.com/Quramy/ts-graphql-plugin/stargazers) - A language service plugin complete and validate GraphQL query in TypeScript template strings.
- [Apollo APQ Debugger](https://github.com/rookieInTraining/apq-debugger) [![GitHub stars](https://img.shields.io/github/stars/rookieInTraining/apq-debugger?style=flat)](https://github.com/rookieInTraining/apq-debugger/stargazers) - Reveal full GraphQL queries behind Apollo APQ hashes. Inspect fallback flow and debug Automatic Persisted Queries in DevTools.

### Tools - Docs

- [graphdoc](https://github.com/2fd/graphdoc) [![GitHub stars](https://img.shields.io/github/stars/2fd/graphdoc?style=flat)](https://github.com/2fd/graphdoc/stargazers) - Static page generator for documenting GraphQL Schema.
- [gqldoc](https://github.com/Code-Hex/gqldoc) [![GitHub stars](https://img.shields.io/github/stars/Code-Hex/gqldoc?style=flat)](https://github.com/Code-Hex/gqldoc/stargazers) - The easiest way to make API documents for GraphQL.
- [spectaql](https://github.com/anvilco/spectaql) [![GitHub stars](https://img.shields.io/github/stars/anvilco/spectaql?style=flat)](https://github.com/anvilco/spectaql/stargazers) - Autogenerate static GraphQL API documentation.
- [graphql-markdown](https://graphql-markdown.github.io/) - Flexible documentation for GraphQL powered with Docusaurus.
- [xyd](https://xyd.dev) - Generate GraphQL API docs.
- [Cortex](https://github.com/cortex-docs/cortex) [![GitHub stars](https://img.shields.io/github/stars/cortex-docs/cortex?style=flat)](https://github.com/cortex-docs/cortex/stargazers) - Generates interactive API documentation and typed SDKs from GraphQL schemas.

### Tools - API Integration & Transformation

- [swagger-to-graphql](https://github.com/yarax/swagger-to-graphql) [![GitHub stars](https://img.shields.io/github/stars/yarax/swagger-to-graphql?style=flat)](https://github.com/yarax/swagger-to-graphql/stargazers) - GraphQL types builder based on a REST API described in Swagger that supports migrating from REST to GraphQL in five minutes.
- [openapi-to-graphql](https://github.com/ibm/openapi-to-graphql) [![GitHub stars](https://img.shields.io/github/stars/ibm/openapi-to-graphql?style=flat)](https://github.com/ibm/openapi-to-graphql/stargazers) - Convert OpenAPI Specification or Swagger definitions to GraphQL interfaces.
- [Blendbase](https://github.com/blendbase/blendbase) [![GitHub stars](https://img.shields.io/github/stars/blendbase/blendbase?style=flat)](https://github.com/blendbase/blendbase/stargazers) - Single open source GraphQL API for connecting CRMs to SaaS applications.
- [Schemato](https://www.schemato.top/graphql-to-typescript) - Browser-only GraphQL SDL converter for generating TypeScript, Zod, Pydantic, Go, Rust, and other typed models.

### Tools - Data Access & ORMs

- [Prisma](https://github.com/prisma/orm) [![GitHub stars](https://img.shields.io/github/stars/prisma/orm?style=flat)](https://github.com/prisma/orm/stargazers) - Type-safe ORM for Node.js and TypeScript that can serve as the data layer for GraphQL APIs.
- [Typetta](https://github.com/twinlogix/typetta) [![GitHub stars](https://img.shields.io/github/stars/twinlogix/typetta?style=flat)](https://github.com/twinlogix/typetta/stargazers) - Node.js ORM written in TypeScript for type lovers and the GraphQL, Node.js, and TypeScript stack.
- [tuql](https://github.com/bradleyboy/tuql) [![GitHub stars](https://img.shields.io/github/stars/bradleyboy/tuql?style=flat)](https://github.com/bradleyboy/tuql/stargazers) - Automatically create a GraphQL server from any SQLite database.
- [dataloader-codegen](https://github.com/Yelp/dataloader-codegen) [![GitHub stars](https://img.shields.io/github/stars/Yelp/dataloader-codegen?style=flat)](https://github.com/Yelp/dataloader-codegen/stargazers) - An opinionated JavaScript library for automatically generating predictable, type safe DataLoaders over a set of resources (e.g. HTTP endpoints).

### Tools - Low-Code & App Builders

- [Retool](https://retool.com/) - Internal tools builder on top of GraphQL APIs with a GraphQL IDE and schema explorer.
- [amplication](https://github.com/amplication/amplication) [![GitHub stars](https://img.shields.io/github/stars/amplication/amplication?style=flat)](https://github.com/amplication/amplication/stargazers) - Platform for defining golden paths and generating standardized backend services, including GraphQL APIs through plugins.
- [DronaHQ](https://www.dronahq.com/) - Build internal tools, dashboards, and admin panels on top of GraphQL data in minutes.
- [Dynaboard](https://dynaboard.com) - Generate low-code web apps from any GraphQL API using AI.

### Tools - Performance & Query Utilities

- [apollo-tracing](https://github.com/apollographql/apollo-tracing) [![GitHub stars](https://img.shields.io/github/stars/apollographql/apollo-tracing?style=flat)](https://github.com/apollographql/apollo-tracing/stargazers) - GraphQL extension that enables you to easily get resolver-level performance information as part of a GraphQL response.
- [gqlhash](https://github.com/romshark/gqlhash) [![GitHub stars](https://img.shields.io/github/stars/romshark/gqlhash?style=flat)](https://github.com/romshark/gqlhash/stargazers) - Lightning fast query hasher that ignores formatting diffs and comments and supports multiple hashing functions.
  <a name="databases--data-platforms" />


## Databases & Data Platforms

- [Cube](https://github.com/cube-js/cube) [![GitHub stars](https://img.shields.io/github/stars/cube-js/cube?style=flat)](https://github.com/cube-js/cube/stargazers) - Open-source semantic layer for AI, BI, and embedded analytics with GraphQL, SQL, and REST APIs.
- [Dgraph](https://dgraph.io/) - Scalable, distributed, low-latency, high-throughput graph database with GraphQL as the query language.
- [ArangoDB](https://arangodb.com/) - Native multi-model database with GraphQL support through Foxx microservices.
- [Weaviate](https://github.com/weaviate/weaviate) [![GitHub stars](https://img.shields.io/github/stars/weaviate/weaviate?style=flat)](https://github.com/weaviate/weaviate/stargazers) - Open-source vector database combining vector search, structured filtering, and a GraphQL interface.

<a name="services" />

## Services

### GraphQL Platforms & Backends

- [AWS AppSync](https://aws.amazon.com/appsync/) - Scalable managed GraphQL service with subscriptions for building real-time and offline-first apps.
- [Nhost](https://nhost.io/) - Open source backend with a GraphQL API over PostgreSQL, plus auth, storage and functions.
- [Grafbase](https://grafbase.com) - Instant GraphQL APIs for any data source.
- [Graphweaver](https://graphweaver.com/) - Turn multiple datasources into a single GraphQL API.

### API Management, Delivery & Observability

- [Moesif API Analytics](https://www.moesif.com/features/graphql-analytics) - GraphQL analytics and monitoring service for identifying functional and performance issues.
- [Stellate](https://stellate.co/) - GraphQL edge platform for caching, observability, and API security, formerly known as GraphCDN.

### Data APIs & Gateways

- [Stargate](https://stargate.io/docs/latest/quickstart/qs-graphql-cql-first.html) - Open-source data gateway that generates GraphQL APIs for Apache Cassandra and DataStax Enterprise tables.
- [Vedika](https://vedika.io) - Vedic astrology AI API with GraphQL support for horoscopes, birth charts, kundali matching, and 108+ endpoints.
- [Codex](https://www.codex.io) - GraphQL API for real-time and historical on-chain data, including token prices, charts, and holders across 90+ networks.

### Commerce

- [Saleor](https://github.com/saleor/saleor/) [![GitHub stars](https://img.shields.io/github/stars/saleor/saleor/?style=flat)](https://github.com/saleor/saleor//stargazers) - High-performance, composable headless commerce API built with GraphQL.
- [Unchained Engine](https://github.com/unchainedshop/unchained) [![GitHub stars](https://img.shields.io/github/stars/unchainedshop/unchained?style=flat)](https://github.com/unchainedshop/unchained/stargazers) - GraphQL-first open-source headless e-commerce framework for Node.js.

### CMS

- [DatoCMS](https://www.datocms.com/) - Headless content management system with a CDN-backed GraphQL Content Delivery API.
- [Apito](https://apito.io/) - Cloud-based headless CMS with GraphQL APIs, a CDN, webhooks, collaboration, revisions, and cloud functions.
- [Hygraph](https://hygraph.com/) - Federated content platform for composing and delivering content through GraphQL APIs.
- [Cosmic](https://www.cosmicjs.com/) - GraphQL-powered Headless CMS and API toolkit.

<a name="tutorials" />

## Tutorials

- [How to GraphQL](https://www.howtographql.com) - Fullstack Tutorial Website with Tracks for all Major Frameworks & Languages including React, Apollo, Relay, JavaScript, Ruby, Java, Elixir and many more.
- [Apollo Odyssey](https://odyssey.apollographql.com/) - Apollo's free interactive learning platform.
- [learning-graphql](https://github.com/mugli/learning-graphql) [![GitHub stars](https://img.shields.io/github/stars/mugli/learning-graphql?style=flat)](https://github.com/mugli/learning-graphql/stargazers) - An attempt to learn GraphQL.
- [GraphQL Roadmap](https://roadmap.sh/graphql) - Step by step guide to learn GraphQL.
- [OWASP GraphQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) - Comprehensive guide for securing GraphQL endpoints and preventing vulnerabilities.

<a name="book" />

## Books

- [The GraphQL Guide](https://graphql.guide) - Comprehensive GraphQL learning guide.
- [Craft GraphQL APIs in Elixir with Absinthe](https://pragprog.com/book/wwgraphql/craft-graphql-apis-in-elixir-with-absinthe) - Guide to building GraphQL APIs in Elixir.
- [The Road to GraphQL](https://www.roadtographql.com/) - Full-stack GraphQL tutorial and learning resource.
- [Practical GraphQL](https://leanpub.com/book-graphql) - Practical guide to implementing GraphQL applications.
- [Production Ready GraphQL](https://book.productionreadygraphql.com) - Best practices for production GraphQL systems.
- [Full Stack GraphQL Applications](https://www.manning.com/books/fullstack-graphql-applications) - Complete guide to full-stack GraphQL development.

<a name="video" />

## Videos

- [GraphQL: The Documentary](https://www.youtube.com/watch?v=783ccP__No8) - Documentary on the history and development of GraphQL.
- [Zero to GraphQL in 30 Minutes](https://www.youtube.com/embed/UBGzsb2UkeY) - Quick introduction to GraphQL fundamentals.
- [Data fetching for React applications at Facebook](https://www.youtube.com/watch?v=9sc8Pyc51uU) - Talk on data fetching patterns for React.
- [React Native & Relay: Bringing Modern Web Techniques to Mobile](https://www.youtube.com/watch?v=X6YbAKiLCLU) - Presentation on React Native and Relay integration.
- [Exploring GraphQL](https://www.youtube.com/watch?v=WQLzZf34FJ8) - Overview of GraphQL concepts and capabilities.
- [Creating a GraphQL Server](https://www.youtube.com/watch?v=gY48GW87Feo) - Tutorial on building a GraphQL server.
- [GraphQL at The Financial Times](https://www.youtube.com/watch?v=S0s935RKKB4) - Case study of GraphQL adoption at the Financial Times.
- [Relay: An Application Framework For React](https://www.youtube.com/watch?v=IrgHurBjQbg) - Introduction to the Relay framework for React applications.
- [Building and Deploying Relay with Facebook](https://www.youtube.com/watch?t=643&v=Pxdgu2XIAAg) - Guide to building and deploying Relay applications.
- [Introduction to GraphQL](https://vimeo.com/144817545) - Introductory talk on GraphQL.
- [Exploring GraphQL@Scale](https://www.youtube.com/watch?v=_9RgHXqH8J0) - Strategies for scaling GraphQL APIs.
- [What's Next for Phoenix by Chris McCord](https://www.youtube.com/watch?v=IMUpYOc9z3c&feature=youtu.be) - Future directions of the Phoenix web framework.
- [GraphQL with Nick Schrock](https://www.youtube.com/watch?v=Ed6oJXKt3-M) - Discussion about GraphQL development.
- [Build a GraphQL server for Node.js using PostgreSQL/MySQL](https://www.youtube.com/watch?v=DNPVqK_woRQ) - Tutorial on building GraphQL servers with Node.js.
- [GraphQL server tutorial for Node.js with SQL, MongoDB and REST](https://www.youtube.com/watch?v=PHabPhgRUuU) - Comprehensive GraphQL server tutorial.
- [JavaScript Air Episode 023: Transitioning from REST to GraphQL](https://www.youtube.com/watch?v=ENqDNIp1Nd8) - Podcast episode on REST to GraphQL migration.
- [GraphQL Future at react-europe 2016](https://www.youtube.com/watch?v=ViXL0YQnioU) - Conference talk on the future of GraphQL.
- [GraphQL at Facebook at react-europe 2016](https://www.youtube.com/watch?v=etax3aEe2dA) - Facebook's perspective on GraphQL usage.
- [Building native mobile apps with GraphQL at react-europe 2016](https://www.youtube.com/watch?v=z5rz3saDPJ8) - Mobile development with GraphQL.
- [Build a GraphQL Server](https://www.youtube.com/watch?v=PEcJxkylcRM&list=PLillGF-RfqbYZty73_PHBqKRDnv7ikh68) - Video series on GraphQL server development.
- [GraphQL Tutorial](https://www.youtube.com/watch?v=Y0lDGjwRYKw&list=PL4cUxeGkcC9iK6Qhn-QLcXCXPQUov1U7f) - Complete GraphQL tutorial series.
- [Five years of GraphQL](https://www.youtube.com/watch?v=s8meG38iZAM) - Retrospective on five years of GraphQL.
- [GraphQL is for Everyone by Moon Highway](https://moonhighway.teachable.com/p/graphql-is-for-everyone) - Beginner-friendly GraphQL course.

<a name="podcast" />

## Podcasts

- [GraphQL.FM](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy8zNjE5NmViMC9wb2RjYXN0L3Jzcw==) - Podcast series on GraphQL development and best practices.

<a name="style-guide" />

## Style Guides

- [Shopify GraphQL Design Tutorial](https://github.com/Shopify/graphql-design-tutorial) [![GitHub stars](https://img.shields.io/github/stars/Shopify/graphql-design-tutorial?style=flat)](https://github.com/Shopify/graphql-design-tutorial/stargazers) - This tutorial was originally created by Shopify for internal purposes. It's based on lessons learned from creating and evolving production schemas at Shopify over almost 3 years.
- [GitLab GraphQL API Style Guide](https://docs.gitlab.com/ee/development/api_graphql_styleguide.html) - This document outlines the style guide for the GitLab GraphQL API.
- [Yelp GraphQL Guidelines](https://yelp.github.io/graphql-guidelines/) - This repo contains documentation and guidelines for a standardized and mostly reasonable approach to GraphQL (at Yelp).
- [Principled GraphQL](https://principledgraphql.com/) - Apollo's 10 GraphQL Principles, broken out into three categories, in a format inspired by the Twelve Factor App.

<a name="blogs" />

## Blogs

- [Official GraphQL blog](https://graphql.org/blog/) - News and technical articles from the GraphQL project.
- [Building Apollo](https://blog.apollographql.com/) - Product updates and engineering articles from Apollo GraphQL.
- [The Guild blog](https://medium.com/the-guild) - Articles from The Guild about GraphQL tools and practices.
- [Production Ready GraphQL blog](https://productionreadygraphql.com) - Guidance for designing and operating production GraphQL systems.

<a name="security-blog" />

### Blogs - Security

- [Escape - The GraphQL Security Blog](https://escape.tech/blog) - Learn about GraphQL security, performance, testing and building production-ready APIs with the latest tools and best practices of the GraphQL ecosystem.

<a name="post" />

## Posts

### Posts - General

- [Using DataLoader to batch GraphQL requests](https://medium.com/@gajus/using-dataloader-to-batch-requests-c345f4b23433) - Guide to batching and caching data access with DataLoader.
- [Introducing Relay and GraphQL](https://reactjs.org/blog/2015/02/20/introducing-relay-and-graphql.html) - Original announcement introducing Relay and GraphQL.
- [GraphQL Introduction](https://reactjs.org/blog/2015/05/01/graphql-introduction.html) - Early overview of GraphQL's design and query model.
- [Unofficial Relay FAQ](https://gist.github.com/wincent/598fa75e22bdfa44cf47) - Community answers to common questions about Relay.
- [Your First GraphQL Server](https://medium.com/the-graphqlhub/your-first-graphql-server-3c766ab4f0a2) - Tutorial for creating a basic GraphQL server.
- [GraphQL Overview - Getting Started with GraphQL and Node.js](https://blog.risingstack.com/graphql-overview-getting-started-with-graphql-and-nodejs/) - Introduction to building GraphQL APIs with Node.js.
- [4 Reasons you should try out GraphQL](https://medium.freecodecamp.org/introduction-to-graphql-1d8011b80159) - Introduction to GraphQL and its benefits over REST APIs.
- [Moving from REST to GraphQL](https://medium.com/@frikille/moving-from-rest-to-graphql-e3650b6f5247) - Account of migrating an API from REST to GraphQL.
- [Writing a Basic API with GraphQL](http://davidandsuzi.com/writing-a-basic-api-with-graphql/) - Tutorial for implementing a basic GraphQL API.
- [Building a GraphQL Server with Node.js and SQL](https://www.reindex.io/blog/building-a-graphql-server-with-node-js-and-sql/) - Tutorial for connecting a Node.js GraphQL server to SQL.
- [GraphQL at The Financial Times](https://www.slideshare.net/LondonReact/graph-ql) - Presentation about GraphQL adoption at the Financial Times.
- [From REST to GraphQL](https://jacobwgillespie.com/2015-10-09-from-rest-to-graphql) - Comparison of GraphQL's data model with REST APIs.
- [GraphQL: A data query language](https://graphql.org/blog/graphql-a-query-language/) - Original announcement explaining GraphQL's purpose and design.
- [Subscriptions in GraphQL and Relay](https://graphql.org/blog/subscriptions-in-graphql-and-relay/) - Introduction to real-time GraphQL subscriptions with Relay.
- [Relay 101: Building A Hacker News Client](https://medium.com/@clayallsopp/relay-101-building-a-hacker-news-client-bb8b2bdc76e6) - Tutorial for building a Hacker News client with Relay.
- [GraphQL Schema Reference](https://graphql.org/learn/schema/) - Official documentation explaining GraphQL schema definition language and shorthand notation.
- [The GitHub GraphQL API](https://githubengineering.com/the-github-graphql-api/) - Introduction to the design of GitHub's GraphQL API.
- [GitHub GraphQL API React Example](https://medium.com/@katopz/github-graphql-api-react-example-eace824d7b61) - Tutorial for consuming GitHub's GraphQL API from React.
- [Testing a GraphQL Server using Jest](https://medium.com/entria/testing-a-graphql-server-using-jest-4e00d0e4980e) - Guide to testing GraphQL queries and mutations with Jest.
- [Mock your GraphQL server realistically with faker.js](https://dev.to/yvonnickfrin/mock-your-graphql-server-realistically-with-faker-js-25oo) - Tutorial for generating realistic mock GraphQL data with Faker.
- [Create an infinite loading list with React and GraphQL](https://dev.to/yvonnickfrin/create-an-infinite-loading-list-with-react-and-graphql-19hh) - Tutorial for cursor-based pagination with React and GraphQL.
- [REST vs GraphQL](https://www.moesif.com/blog/technical/graphql/REST-vs-GraphQL-APIs-the-good-the-bad-the-ugly/) - Comparison of REST and GraphQL API tradeoffs.
- [Build a GraphQL API with Siler on top of Swoole](https://www.swoole.co.uk/article/Build-a-GraphQL-API-on-top-of-Swoole) - Tutorial for building a PHP GraphQL API with Siler and Swoole.
- [Fluent GraphQL clients: how to write queries like a boss](https://hasura.io/blog/fluent-graphql-clients-how-to-write-queries-like-a-boss/) - Survey of fluent GraphQL client libraries across several languages.
- [Level up your serverless game with a GraphQL data-as-a-service layer](https://hasura.io/blog/level-up-your-serverless-game-with-a-graphql-data-as-a-service-layer/) - Guide to using GraphQL as a data layer for serverless applications.
- [A deep-dive into Relay, the friendly & opinionated GraphQL client](https://hasura.io/blog/deep-dive-into-relay-graphql-client/) - Detailed introduction to Relay's architecture and data-fetching model.
- [Make Your GraphQL API Easier to Adopt Through Components](https://hackernoon.com/make-your-graphql-api-easier-to-adopt-through-components-74b022f195c1) - Guide to packaging GraphQL schemas and resolvers as reusable components.
- [GraphQL Subscriptions with Apache Kafka in Ballerina](https://medium.com/ballerina-techblog/graphql-subscriptions-with-apache-kafka-in-ballerina-b3c296d333cd) - Tutorial for streaming Kafka messages through Ballerina GraphQL subscriptions.

### Posts - Security

- [9 GraphQL Security Best Practices](https://escape.tech/blog/9-graphql-security-best-practices/) - Practical measures for protecting GraphQL APIs from common attacks.
- [Discovering GraphQL Endpoints and SQLi Vulnerabilities](https://medium.com/@localh0t/discovering-graphql-endpoints-and-sqli-vulnerabilities-5d39f26cea2e) - Walkthrough of GraphQL endpoint discovery and SQL injection testing.
- [Securing GraphQL API](https://lab.wallarm.com/securing-graphql-api/) - Overview of common GraphQL security risks and mitigations.
- [Security Points to Consider Before Implementing GraphQL](https://nordicapis.com/security-points-to-consider-before-implementing-graphql/) - Security considerations for teams adopting GraphQL.
- [Authorization Patterns in GraphQL](https://www.osohq.com/post/graphql-authorization) - Comparison of authorization patterns for GraphQL APIs.
- [Implementing GraphQL RBAC Authorization: A Practical Guide](https://www.permit.io/blog/implementing-graphql-authorization) - Guide to implementing role-based access control in GraphQL APIs.
- [How to implement viewerCanSee in GraphQL](https://medium.com/entria/how-to-implement-viewercansee-in-graphql-78cc48de7464) - Guide to exposing field visibility through a GraphQL schema.
- [Preventing traversal attacks on your GraphQL API](https://blog.morethancode.dev/preventing-traversal-attacks-in-your-graphql-api/) - Techniques for limiting maliciously deep GraphQL queries.
- [Authentication and Authorization for GraphQL APIs](https://www.moesif.com/blog/technical/api-design/Steps-to-Building-Authentication-and-Authorization-For-GraphQL-APIs/) - Guide to authentication and authorization patterns for GraphQL APIs.
- [Undocumented: keeping parts of your GraphQL schema hidden from introspection](https://www.useanvil.com/blog/engineering/undocumented-directive/) - Guide to hiding selected schema elements from GraphQL introspection.
- [How to Test your GraphQL Endpoints](https://escape.tech/blog/8-most-common-graphql-vulnerabilities/) - Overview of common GraphQL vulnerabilities and how to test for them.

## Contributing

Contributions are welcome. Read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.
