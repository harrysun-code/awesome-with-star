# Vert.x

[![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-awesome?style=flat)](https://github.com/vert-x3/vertx-awesome/stargazers)

# Awesome Vert.x [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="vertx-logo.svg" align="right" width="250" alt="Vert.x logo">](http://vertx.io)

*Awesome Vert.x* is a list of awesome frameworks, libraries or other components related to
[Vert.x](https://github.com/eclipse/vert.x) [![GitHub stars](https://img.shields.io/github/stars/eclipse/vert.x?style=flat)](https://github.com/eclipse/vert.x/stargazers).

If you want your component to appear here, send a pull request to this repository to add it.

Please note that we can't vouch for the stability or production-worthiness of everything on this list unless it has
the icon <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px">
next to it. This icon means the component is part of the official
[Vert.x stack](https://vertx.io/docs/).

## Contents

* [Books](#books)
* [Build tools](#build-tools)
* [Web Frameworks](#web-frameworks)
* [Authentication Authorisation](#authentication-authorisation)
* [Database Clients](#database-clients)
* [Integration](#integration)
* [Middleware](#middleware)
* [Language Support](#language-support)
* [Reactive](#reactive)
* [Sync Thread Non Block](#sync-thread-non-block)
* [Vert.x Event Bus Clients](#vertx-event-bus-clients)
* [Vert.x Event Bus Extensions](#vertx-event-bus-extensions)
* [Cluster Managers](#cluster-managers)
* [Cloud Support](#cloud-support)
* [Microservices](#microservices)
* [Game development](#game-development)
* [Search Engines](#search-engines)
* [Service Factory](#service-factory)
* [Config](#config)
* [Dependency Injection](#dependency-injection)
* [Testing](#testing)
* [Development Tools](#development-tools)
* [Miscellaneous](#miscellaneous)
* [Distribution](#distribution)
* [Examples](#examples)
* [Deployment](#deployment)
* [Utilities](#utilities)
* [Articles](#articles)
* [Front-End](#front-end)

## Books

* [Building Reactive Microservices in Java](https://www.oreilly.com/library/view/building-reactive-microservices/9781491986295/) by Clément Escoffier
* [Vert.x in Action](https://www.manning.com/books/vertx-in-action) by Julien Ponge

## Build tools

* [Vert.x Maven plugin](https://github.com/reactiverse/vertx-maven-plugin) [![GitHub stars](https://img.shields.io/github/stars/reactiverse/vertx-maven-plugin?style=flat)](https://github.com/reactiverse/vertx-maven-plugin/stargazers)
* [Vert.x Gradle plugin](https://plugins.gradle.org/plugin/io.vertx.vertx-plugin)
* [Vert.x Codegen Gradle plugin](https://github.com/bulivlad/vertx-codegen-plugin) [![GitHub stars](https://img.shields.io/github/stars/bulivlad/vertx-codegen-plugin?style=flat)](https://github.com/bulivlad/vertx-codegen-plugin/stargazers) - A Gradle plugin to facilitate the codegen usage for Vert.x Java projects.

## Web Frameworks

* [Vert.x Web](https://github.com/vert-x3/vertx-web) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-web?style=flat)](https://github.com/vert-x3/vertx-web/stargazers)  <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Full featured web toolkit for Vert.x.
* [Vert.x Jersey](https://github.com/englishtown/vertx-jersey) [![GitHub stars](https://img.shields.io/github/stars/englishtown/vertx-jersey?style=flat)](https://github.com/englishtown/vertx-jersey/stargazers) - Create JAX-RS [Jersey](https://eclipse-ee4j.github.io/jersey/) resources in Vert.x.
* [Kovert](https://github.com/kohesive/kovert) [![GitHub stars](https://img.shields.io/github/stars/kohesive/kovert?style=flat)](https://github.com/kohesive/kovert/stargazers) - Invisible REST framework for Kotlin + Vert.x Web.
* [Handlers](https://github.com/spriet2000/vertx-handlers-http) [![GitHub stars](https://img.shields.io/github/stars/spriet2000/vertx-handlers-http?style=flat)](https://github.com/spriet2000/vertx-handlers-http/stargazers) - Open web framework for Vert.x.
* [QBit](https://github.com/advantageous/qbit) [![GitHub stars](https://img.shields.io/github/stars/advantageous/qbit?style=flat)](https://github.com/advantageous/qbit/stargazers) - REST and WebSocket method call marshaling and reactive library.
* [vertx-rest-storage](https://github.com/swisspush/vertx-rest-storage) [![GitHub stars](https://img.shields.io/github/stars/swisspush/vertx-rest-storage?style=flat)](https://github.com/swisspush/vertx-rest-storage/stargazers) - Persistence for REST resources in the filesystem or a redis database.
* [Jubilee](https://github.com/isaiah/jubilee) [![GitHub stars](https://img.shields.io/github/stars/isaiah/jubilee?style=flat)](https://github.com/isaiah/jubilee/stargazers) - A rack compatible Ruby HTTP server built on Vert.x 3.
* [Knot.x](https://github.com/Cognifide/knotx) [![GitHub stars](https://img.shields.io/github/stars/Cognifide/knotx?style=flat)](https://github.com/Cognifide/knotx/stargazers) - Efficient & high-performance integration platform for modern websites built on Vert.x 3.
* [Irked](https://github.com/GreenfieldTech/irked) [![GitHub stars](https://img.shields.io/github/stars/GreenfieldTech/irked?style=flat)](https://github.com/GreenfieldTech/irked/stargazers) - Annotations-based configuration for Vert.x Web, with a controller framework and expressive APIs for REST.
* [REST.VertX](https://github.com/zandero/rest.vertx) [![GitHub stars](https://img.shields.io/github/stars/zandero/rest.vertx?style=flat)](https://github.com/zandero/rest.vertx/stargazers) - Lightweight JAX-RS (RestEasy) like annotation processor for Vert.x verticals.
* [Atmosphere Vert.x](https://github.com/Atmosphere/atmosphere-vertx) [![GitHub stars](https://img.shields.io/github/stars/Atmosphere/atmosphere-vertx?style=flat)](https://github.com/Atmosphere/atmosphere-vertx/stargazers) - Realtime Client Server Framework for the JVM, supporting WebSockets and Server Sent Events with Cross-Browser Fallbacks.
* [Vert.x Vaadin](https://github.com/mcollovati/vertx-vaadin) [![GitHub stars](https://img.shields.io/github/stars/mcollovati/vertx-vaadin?style=flat)](https://github.com/mcollovati/vertx-vaadin/stargazers) - Run Vaadin applications on Vert.x.
* [Serverx](https://github.com/lukehutch/serverx) [![GitHub stars](https://img.shields.io/github/stars/lukehutch/serverx?style=flat)](https://github.com/lukehutch/serverx/stargazers) - Allows you to quickly and easily set up a Vert.x-powered server using only route handler annotations.
* [Cloudopt Next](https://github.com/cloudoptlab/cloudopt-next) [![GitHub stars](https://img.shields.io/github/stars/cloudoptlab/cloudopt-next?style=flat)](https://github.com/cloudoptlab/cloudopt-next/stargazers) - Cloudopt Next is a very lightweight and modern, JVM-based, full stack kotlin framework designed for building modular, easily testable JVM applications with support for Java, Kotlin language, crafted from the best of breed Java libraries and standards.
* [Donkey](https://github.com/AppsFlyer/donkey) [![GitHub stars](https://img.shields.io/github/stars/AppsFlyer/donkey?style=flat)](https://github.com/AppsFlyer/donkey/stargazers) - Modern Clojure HTTP server and client built for ease of use and performance.
* [SCX](https://github.com/scx567888/scx) [![GitHub stars](https://img.shields.io/github/stars/scx567888/scx?style=flat)](https://github.com/scx567888/scx/stargazers) - An open and easy-to-use web framework, most functions are based on annotations.
* [vertx-rest](https://github.com/dream11/vertx-rest) [![GitHub stars](https://img.shields.io/github/stars/dream11/vertx-rest?style=flat)](https://github.com/dream11/vertx-rest/stargazers) - Abstraction over resteasy-vertx to simplify writing a Vert.x REST application based on JAX-RS annotations.

## Authentication Authorisation

* [Vert.x Auth SQL](https://github.com/eclipse-vertx/vertx-auth) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-auth?style=flat)](https://github.com/eclipse-vertx/vertx-auth/stargazers)  <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x authentication/authorisation based on the Vert.x SQL client and a relational database.
* [Vert.x Auth JWT](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-jwt) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-auth/tree/master/vertx-auth-jwt?style=flat)](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-jwt/stargazers)  <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Authorisation based on JSON Web Tokens.
* [Vert.x Auth htdigest](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htdigest) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htdigest?style=flat)](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htdigest/stargazers)  <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Authorisation/Authentication based on [Apache htdigest](https://httpd.apache.org/docs/2.4/programs/htdigest.html).
* [Vert.x Auth Mongo](https://github.com/vert-x3/vertx-auth/tree/master/vertx-auth-mongo) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-auth/tree/master/vertx-auth-mongo?style=flat)](https://github.com/vert-x3/vertx-auth/tree/master/vertx-auth-mongo/stargazers)  <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Authorisation/Authentication based on [MongoDB](https://www.mongodb.com/).
* [Vert.x Auth OAuth2](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-oauth2) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-auth/tree/master/vertx-auth-oauth2?style=flat)](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-oauth2/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Authorisation/Authentication based on [OAuth 2](https://oauth.net/2/).
* [Vert.x Auth htpasswd](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htpasswd) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htpasswd?style=flat)](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htpasswd/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Authorisation/Authentication based on [htpasswd](https://httpd.apache.org/docs/2.4/programs/htpasswd.html).

* [Vert.x-Pac4j](https://github.com/pac4j/vertx-pac4j) [![GitHub stars](https://img.shields.io/github/stars/pac4j/vertx-pac4j?style=flat)](https://github.com/pac4j/vertx-pac4j/stargazers) - Vert.x authentication/authorisation implemented using [pac4j](http://www.pac4j.org/).

## Database Clients

*Clients for connecting to databases*

* Relational Databases
  * [Reactive SQL Client](https://github.com/eclipse-vertx/vertx-sql-client) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-sql-client?style=flat)](https://github.com/eclipse-vertx/vertx-sql-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - High performance reactive SQL client.
  * [JDBC](https://github.com/vert-x3/vertx-jdbc-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-jdbc-client?style=flat)](https://github.com/vert-x3/vertx-jdbc-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Asynchronous interface around a JDBC datasource.
  * [MySQL / PostgreSQL](https://github.com/vert-x3/vertx-mysql-postgresql-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-mysql-postgresql-client?style=flat)](https://github.com/vert-x3/vertx-mysql-postgresql-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Asynchronous Client for MySQL/PostgreSQL.
  * [PostgreSQL](https://github.com/vietj/reactive-pg-client) [![GitHub stars](https://img.shields.io/github/stars/vietj/reactive-pg-client?style=flat)](https://github.com/vietj/reactive-pg-client/stargazers) - Reactive PostgreSQL Client.
  * [database](https://github.com/susom/database) [![GitHub stars](https://img.shields.io/github/stars/susom/database?style=flat)](https://github.com/susom/database/stargazers) - Client for Oracle, PostgreSQL, SQL Server, HyperSQL, etc. designed for security, correctness, and ease of use.
  * [jOOQ](https://github.com/jklingsporn/vertx-jooq) [![GitHub stars](https://img.shields.io/github/stars/jklingsporn/vertx-jooq?style=flat)](https://github.com/jklingsporn/vertx-jooq/stargazers) - Doing typesafe, asynchronous SQL and generate code using jOOQ.
  * [jOOQx](https://github.com/zero88/jooqx) [![GitHub stars](https://img.shields.io/github/stars/zero88/jooqx?style=flat)](https://github.com/zero88/jooqx/stargazers) - Leverages the power of typesafe SQL from `jOOQ DSL` and uses the reactive and non-blocking SQL driver from Vert.x.
  * [Exposed Vert.x SQL Client](https://github.com/huanshankeji/exposed-vertx-sql-client) [![GitHub stars](https://img.shields.io/github/stars/huanshankeji/exposed-vertx-sql-client?style=flat)](https://github.com/huanshankeji/exposed-vertx-sql-client/stargazers) - Kotlin's [Exposed](https://github.com/JetBrains/Exposed) [![GitHub stars](https://img.shields.io/github/stars/JetBrains/Exposed?style=flat)](https://github.com/JetBrains/Exposed/stargazers) on top of [Vert.x Reactive SQL Client](https://github.com/eclipse-vertx/vertx-sql-client) [![GitHub stars](https://img.shields.io/github/stars/eclipse-vertx/vertx-sql-client?style=flat)](https://github.com/eclipse-vertx/vertx-sql-client/stargazers).

* NoSQL Databases
  * [MongoDB](https://github.com/vert-x3/vertx-mongo-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-mongo-client?style=flat)](https://github.com/vert-x3/vertx-mongo-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - An asynchronous client for interacting with a MongoDB database.
  * [Redis](https://github.com/vert-x3/vertx-redis-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-redis-client?style=flat)](https://github.com/vert-x3/vertx-redis-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Asynchronous API to interact with Redis.
  * [Cassandra](https://github.com/vert-x3/vertx-cassandra-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-cassandra-client?style=flat)](https://github.com/vert-x3/vertx-cassandra-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - A Vert.x client allowing applications to interact with a Cassandra service.
  * [Cassandra](https://github.com/englishtown/vertx-cassandra) [![GitHub stars](https://img.shields.io/github/stars/englishtown/vertx-cassandra?style=flat)](https://github.com/englishtown/vertx-cassandra/stargazers) - Asynchronous API to interact with Cassandra and Cassandra Mapping.
  * [Neo4j Java Driver Vert.x](https://github.com/romanbsd/neo4j-java-driver-vertx) [![GitHub stars](https://img.shields.io/github/stars/romanbsd/neo4j-java-driver-vertx?style=flat)](https://github.com/romanbsd/neo4j-java-driver-vertx/stargazers) - Vert.x wrapper around the Neo4j Java Driver.
  * [OrientDB](https://github.com/cstamas/vertx-orientdb) [![GitHub stars](https://img.shields.io/github/stars/cstamas/vertx-orientdb?style=flat)](https://github.com/cstamas/vertx-orientdb/stargazers) - Non-blocking OrientDB server integration.
  * [Bitsy](https://github.com/cstamas/vertx-bitsy) [![GitHub stars](https://img.shields.io/github/stars/cstamas/vertx-bitsy?style=flat)](https://github.com/cstamas/vertx-bitsy/stargazers) - Non-blocking Bitsy Graph server integration.
  * [MarkLogic](https://github.com/etourdot/vertx-marklogic) [![GitHub stars](https://img.shields.io/github/stars/etourdot/vertx-marklogic?style=flat)](https://github.com/etourdot/vertx-marklogic/stargazers) - Asynchronous client for Marklogic Database Server.
  * [SirixDB](https://github.com/sirixdb/sirix/tree/master/bundles/sirix-rest-api) [![GitHub stars](https://img.shields.io/github/stars/sirixdb/sirix/tree/master/bundles/sirix-rest-api?style=flat)](https://github.com/sirixdb/sirix/tree/master/bundles/sirix-rest-api/stargazers) - Non-blocking SirixDB HTTP-server.
  * [DGraph](https://github.com/aesteve/vertx-dgraph-client) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-dgraph-client?style=flat)](https://github.com/aesteve/vertx-dgraph-client/stargazers) - An example on how to build a Vert.x gRPC compliant client. Here targeting [dgraph](https://docs.dgraph.io)
  * [RxFirestore](https://github.com/pjgg/rxfirestore) [![GitHub stars](https://img.shields.io/github/stars/pjgg/rxfirestore?style=flat)](https://github.com/pjgg/rxfirestore/stargazers) - Non-blocking Firestore SDK written in a reactive way.
  * [MongoDB](https://github.com/imrafaelmerino/vertx-mongo-effect) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/vertx-mongo-effect?style=flat)](https://github.com/imrafaelmerino/vertx-mongo-effect/stargazers) - Pure functional and reactive MongoDB client on top of [Vert.x Effect](https://github.com/imrafaelmerino/vertx-mongo-effect) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/vertx-mongo-effect?style=flat)](https://github.com/imrafaelmerino/vertx-mongo-effect/stargazers). Full support for retry, fallback and recovery operations.
  * [Aerospike](https://github.com/dream11/vertx-aerospike-client) [![GitHub stars](https://img.shields.io/github/stars/dream11/vertx-aerospike-client?style=flat)](https://github.com/dream11/vertx-aerospike-client/stargazers) - Asynchronous and non-blocking API to interact with Aerospike server. Uses [AerospikeClient's](https://github.com/aerospike/aerospike-client-java) [![GitHub stars](https://img.shields.io/github/stars/aerospike/aerospike-client-java?style=flat)](https://github.com/aerospike/aerospike-client-java/stargazers) async commands internally and handles the result on the Vert.x Context.

* [vertx-pojo-mapper](https://github.com/BraintagsGmbH/vertx-pojo-mapper) [![GitHub stars](https://img.shields.io/github/stars/BraintagsGmbH/vertx-pojo-mapper?style=flat)](https://github.com/BraintagsGmbH/vertx-pojo-mapper/stargazers) - Non-blocking POJO mapping for MySQL and MongoDB.
* [vertx-mysql-binlog-client](https://github.com/guoyu511/vertx-mysql-binlog-client) [![GitHub stars](https://img.shields.io/github/stars/guoyu511/vertx-mysql-binlog-client?style=flat)](https://github.com/guoyu511/vertx-mysql-binlog-client/stargazers) - A Vert.x client for tapping into MySQL replication stream.

## Integration

* Server-Sent Events
  * [jEaSSE](https://github.com/mariomac/jeasse) [![GitHub stars](https://img.shields.io/github/stars/mariomac/jeasse?style=flat)](https://github.com/mariomac/jeasse/stargazers) - Java Easy SSE. A simple, lightweight implementation of SSE.
  * [vertx-sse](https://github.com/aesteve/vertx-sse) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-sse?style=flat)](https://github.com/aesteve/vertx-sse/stargazers) - Vert.x SSE implementation + event-bus SSE bridge.

* Mail
  * [SMTP](https://github.com/vert-x3/vertx-mail-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-mail-client?style=flat)](https://github.com/vert-x3/vertx-mail-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Async SMTP client.

* REST
  * [Retrofit adapter for Vert.x](https://github.com/vietj/retrofit-vertx) [![GitHub stars](https://img.shields.io/github/stars/vietj/retrofit-vertx?style=flat)](https://github.com/vietj/retrofit-vertx/stargazers) - A highly scalable adapter for Retrofit with Vert.x.
  * [openapi4j adapter for Vert.x](https://github.com/openapi4j/openapi4j/tree/master/openapi-operation-adapters/openapi-operation-vertx) [![GitHub stars](https://img.shields.io/github/stars/openapi4j/openapi4j/tree/master/openapi-operation-adapters/openapi-operation-vertx?style=flat)](https://github.com/openapi4j/openapi4j/tree/master/openapi-operation-adapters/openapi-operation-vertx/stargazers) - OpenAPI 3 request validator and router factory alternative.
  * [Vert.x Effect HTTP client](https://github.com/imrafaelmerino/vertx-effect) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/vertx-effect?style=flat)](https://github.com/imrafaelmerino/vertx-effect/stargazers) - Pure functional and reactive HTTP client using [Vert.x Effect](https://github.com/imrafaelmerino/vertx-effect) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/vertx-effect?style=flat)](https://github.com/imrafaelmerino/vertx-effect/stargazers) with OAuth support and retry, fallback and recovery operations.

* File Server
  * [Vert.x TFTP Client](https://github.com/OneManCrew/vertx-tftp-client) [![GitHub stars](https://img.shields.io/github/stars/OneManCrew/vertx-tftp-client?style=flat)](https://github.com/OneManCrew/vertx-tftp-client/stargazers) - TFTP client for Vert.x support download/upload files.
* Messaging
  * [AMQP 1.0](https://github.com/vert-x3/vertx-amqp-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-amqp-bridge?style=flat)](https://github.com/vert-x3/vertx-amqp-bridge/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Interact with AMQP 1.0 servers using the Vert.x Producer and Consumer APIs.
  * [MQTT](https://github.com/vert-x3/vertx-mqtt) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-mqtt?style=flat)](https://github.com/vert-x3/vertx-mqtt/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Provides two different components: an MQTT server for handling all the MQTT communication and messages exchanges with clients and an MQTT client for sending and receiving messages against an MQTT broker.
  * [RabbitMQ](https://github.com/vert-x3/vertx-rabbitmq-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-rabbitmq-client?style=flat)](https://github.com/vert-x3/vertx-rabbitmq-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - A RabbitMQ client (AMQP 0.9.1).
  * [Kafka Client](https://github.com/vert-x3/vertx-kafka-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-kafka-client?style=flat)](https://github.com/vert-x3/vertx-kafka-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - A Kafka client.
  * [kafka](https://github.com/cyngn/vertx-kafka) [![GitHub stars](https://img.shields.io/github/stars/cyngn/vertx-kafka?style=flat)](https://github.com/cyngn/vertx-kafka/stargazers) - Kafka client for consuming and producing messages.
  * [STOMP](https://github.com/vert-x3/vertx-stomp) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-stomp?style=flat)](https://github.com/vert-x3/vertx-stomp/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - A Kafka client and server.
  * [ZeroMQ](https://github.com/dano/vertx-zeromq) [![GitHub stars](https://img.shields.io/github/stars/dano/vertx-zeromq?style=flat)](https://github.com/dano/vertx-zeromq/stargazers) - ZeroMQ Event Bus bridge.
  * [Azure ServiceBus](https://github.com/TextBack/vertx-azure-servicebus) [![GitHub stars](https://img.shields.io/github/stars/TextBack/vertx-azure-servicebus?style=flat)](https://github.com/TextBack/vertx-azure-servicebus/stargazers) - Azure [ServiceBus](https://azure.microsoft.com/en-us/products/service-bus/) producer and consumer (fully async, doesn't use Microsoft Azure SDK).
  * [AMQP 1.0 - Kafka bridge](https://github.com/rhiot/amqp-kafka-bridge) [![GitHub stars](https://img.shields.io/github/stars/rhiot/amqp-kafka-bridge?style=flat)](https://github.com/rhiot/amqp-kafka-bridge/stargazers) - Bridge for sending/receiving messages to/from Apache Kafka using the AMQP 1.0 protocol.
  * [Vert.x Kafka Client](https://github.com/vert-x3/vertx-kafka-client) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-kafka-client?style=flat)](https://github.com/vert-x3/vertx-kafka-client/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Apache Kafka client for reading and sending messages from/to an Apache Kafka cluster.
  * [The White Rabbit](https://github.com/viartemev/the-white-rabbit) [![GitHub stars](https://img.shields.io/github/stars/viartemev/the-white-rabbit?style=flat)](https://github.com/viartemev/the-white-rabbit/stargazers) - An asynchronous RabbitMQ (AMQP) client based on Kotlin coroutines.
  * [WAMP Broker](https://github.com/i22-digitalagentur/vertx-wamp) [![GitHub stars](https://img.shields.io/github/stars/i22-digitalagentur/vertx-wamp?style=flat)](https://github.com/i22-digitalagentur/vertx-wamp/stargazers) - A WAMP broker you can embed into your Vert.x application.

* JavaEE
  * [JCA adaptor](https://github.com/vert-x3/vertx-jca) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-jca?style=flat)](https://github.com/vert-x3/vertx-jca/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Java Connector Architecture Adaptor for the Vert.x event bus.
  * [Weld](https://github.com/weld/weld-vertx) [![GitHub stars](https://img.shields.io/github/stars/weld/weld-vertx?style=flat)](https://github.com/weld/weld-vertx/stargazers) - Brings the CDI programming model into the Vert.x ecosystem (register CDI observer methods as Vert.x message consumers, CDI-powered Verticles, define routes in a declarative way, etc.).

* Meteor
  * [Meteor](https://github.com/jmusacchio/vertxbus/) [![GitHub stars](https://img.shields.io/github/stars/jmusacchio/vertxbus/?style=flat)](https://github.com/jmusacchio/vertxbus//stargazers) - Meteor integration support through Vert.x event bus.

* Metrics
  * [Hawkular metrics](https://github.com/tsegismont/vertx-monitor) [![GitHub stars](https://img.shields.io/github/stars/tsegismont/vertx-monitor?style=flat)](https://github.com/tsegismont/vertx-monitor/stargazers) - [Hawkular](http://www.hawkular.org/) implementation of the Vert.x Metrics SPI.
  * [DropWizard metrics](https://github.com/vert-x3/vertx-dropwizard-metrics) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-dropwizard-metrics?style=flat)](https://github.com/vert-x3/vertx-dropwizard-metrics/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Metrics implementation using DropWizard metrics.
  * [Micrometer metrics](https://github.com/vert-x3/vertx-micrometer-metrics) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-micrometer-metrics?style=flat)](https://github.com/vert-x3/vertx-micrometer-metrics/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Metrics implementation using Micrometer metrics.
  * [OpenTsDb Metrics](https://github.com/cyngn/vertx-opentsdb) [![GitHub stars](https://img.shields.io/github/stars/cyngn/vertx-opentsdb?style=flat)](https://github.com/cyngn/vertx-opentsdb/stargazers) - [OpenTsDb](http://opentsdb.net/) metrics client for Vert.x.
  * [Bosun Monitoring](https://github.com/cyngn/vertx-bosun) [![GitHub stars](https://img.shields.io/github/stars/cyngn/vertx-bosun?style=flat)](https://github.com/cyngn/vertx-bosun/stargazers) - [Bosun](https://bosun.org/) client library for Vert.x.

* Netflix - Hystrix
  * [Hystrix Metrics Stream](https://github.com/kennedyoliveira/hystrix-vertx-metrics-stream.git) [![GitHub stars](https://img.shields.io/github/stars/kennedyoliveira/hystrix-vertx-metrics-stream.git?style=flat)](https://github.com/kennedyoliveira/hystrix-vertx-metrics-stream.git/stargazers) - Emits metrics for Hystrix Dashboard from a Vert.x application with [Hystrix](https://github.com/Netflix/Hystrix) [![GitHub stars](https://img.shields.io/github/stars/Netflix/Hystrix?style=flat)](https://github.com/Netflix/Hystrix/stargazers).

* Dart
  * [Vert.x Dart SockJS](https://github.com/wem/vertx-dart-sockjs) [![GitHub stars](https://img.shields.io/github/stars/wem/vertx-dart-sockjs?style=flat)](https://github.com/wem/vertx-dart-sockjs/stargazers) - [Dart](https://www.dartlang.org/) integration for [Vert.x SockJS bridge](http://vertx.io/docs/vertx-web/java/#_sockjs_event_bus_bridge) and plain SockJS with use of dart:js.

* Push Notifications
  * [Onesignal](https://github.com/jklingsporn/vertx-push-onesignal) [![GitHub stars](https://img.shields.io/github/stars/jklingsporn/vertx-push-onesignal?style=flat)](https://github.com/jklingsporn/vertx-push-onesignal/stargazers) - Send push notifications to (mobile/web) apps from your Vert.x application with [OneSignal](https://onesignal.com/).

* CNCF CloudEvents
  * [CloudEvents.io Java SDK](https://github.com/cloudevents/sdk-java) [![GitHub stars](https://img.shields.io/github/stars/cloudevents/sdk-java?style=flat)](https://github.com/cloudevents/sdk-java/stargazers) - Send and receive [CloudEvents](https://cloudevents.io/) using the [Vert.x HTTP Transport](https://github.com/cloudevents/sdk-java/blob/master/http/vertx/README.md) [![GitHub stars](https://img.shields.io/github/stars/cloudevents/sdk-java/blob/master/http/vertx/README.md?style=flat)](https://github.com/cloudevents/sdk-java/blob/master/http/vertx/README.md/stargazers) for CloudEvents.

## Middleware

* [Apache Camel](https://camel.apache.org/components/vertx-component.html) - [Apache Camel](http://camel.apache.org/) component for bridging Camel with the Vert.x event bus.
* [Gateleen](https://github.com/swisspush/gateleen) [![GitHub stars](https://img.shields.io/github/stars/swisspush/gateleen?style=flat)](https://github.com/swisspush/gateleen/stargazers) - Middleware library based on Vert.x to build advanced JSON/REST communication servers.
* [Gravitee.io](https://gravitee.io) - An OSS API Platform including an API Gateway and an OAuth2 / OIDC authorization server based on Vert.x Core / Vert.x Web and other modules.
* [API Framework](https://github.com/vinscom/api-framework) [![GitHub stars](https://img.shields.io/github/stars/vinscom/api-framework?style=flat)](https://github.com/vinscom/api-framework/stargazers) - Vert.x and Glue based microservice framework removing distinction between standalone and serveless application. All services can run in standalone server, but, if required, same codebase can be used to run any service as serverless application.

## Language Support

*Programming language support for Vert.x*

* [Ceylon](https://github.com/vert-x3/vertx-lang-ceylon) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-ceylon?style=flat)](https://github.com/vert-x3/vertx-lang-ceylon/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Ceylon support.
* [Groovy](https://github.com/vert-x3/vertx-lang-groovy) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-groovy?style=flat)](https://github.com/vert-x3/vertx-lang-groovy/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Groovy support.
* [Java](https://github.com/eclipse/vert.x) [![GitHub stars](https://img.shields.io/github/stars/eclipse/vert.x?style=flat)](https://github.com/eclipse/vert.x/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x main repository (including the Java API).
* [JavaScript](https://github.com/vert-x3/vertx-lang-js) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-js?style=flat)](https://github.com/vert-x3/vertx-lang-js/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - JavaScript support.
* [Python](https://github.com/vert-x3/vertx-lang-python) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-python?style=flat)](https://github.com/vert-x3/vertx-lang-python/stargazers) - Python support.
* [Ruby](https://github.com/vert-x3/vertx-lang-ruby) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-ruby?style=flat)](https://github.com/vert-x3/vertx-lang-ruby/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Ruby support.
* [Scala](https://github.com/vert-x3/vertx-lang-scala) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-scala?style=flat)](https://github.com/vert-x3/vertx-lang-scala/stargazers) - <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Scala support.
* [Kotlin](https://github.com/vert-x3/vertx-lang-kotlin) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-kotlin?style=flat)](https://github.com/vert-x3/vertx-lang-kotlin/stargazers) - <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Kotlin support.
* [EcmaScript](https://github.com/reactiverse/es4x) [![GitHub stars](https://img.shields.io/github/stars/reactiverse/es4x?style=flat)](https://github.com/reactiverse/es4x/stargazers) - EcmaScript >=6 (JavaScript) support.
* [Php](https://github.com/vert-x-cn/vertx-lang-jphp) [![GitHub stars](https://img.shields.io/github/stars/vert-x-cn/vertx-lang-jphp?style=flat)](https://github.com/vert-x-cn/vertx-lang-jphp/stargazers) - Php support.

*Language extensions*

* [Grooveex](https://github.com/aesteve/grooveex) [![GitHub stars](https://img.shields.io/github/stars/aesteve/grooveex?style=flat)](https://github.com/aesteve/grooveex/stargazers) - Syntactic sugar + utilities (DSL builders, etc.) on top of [vertx-lang-groovy](https://github.com/vert-x3/vertx-lang-groovy) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-groovy?style=flat)](https://github.com/vert-x3/vertx-lang-groovy/stargazers).

## Reactive

* [Reactive Streams](https://github.com/vert-x3/vertx-reactive-streams) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-reactive-streams?style=flat)](https://github.com/vert-x3/vertx-reactive-streams/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Reactive Streams.
* [Vert.x Rx](https://github.com/vert-x3/vertx-rx) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-rx?style=flat)](https://github.com/vert-x3/vertx-rx/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Reactive Extensions.
* [Vert.x Sync](https://github.com/vert-x3/vertx-sync) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-sync?style=flat)](https://github.com/vert-x3/vertx-sync/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x fiber support.
* [Kotlin coroutines](https://github.com/vert-x3/vertx-lang-kotlin/tree/master/vertx-lang-kotlin-coroutines) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-lang-kotlin/tree/master/vertx-lang-kotlin-coroutines?style=flat)](https://github.com/vert-x3/vertx-lang-kotlin/tree/master/vertx-lang-kotlin-coroutines/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x support for Kotlin coroutines.
* [vertx-util](https://github.com/cyngn/vertx-util) [![GitHub stars](https://img.shields.io/github/stars/cyngn/vertx-util?style=flat)](https://github.com/cyngn/vertx-util/stargazers) - Light weight promises & latches for Vert.x.
* [QBit](https://github.com/advantageous/qbit) [![GitHub stars](https://img.shields.io/github/stars/advantageous/qbit?style=flat)](https://github.com/advantageous/qbit/stargazers) - Async typed actor-like lib that runs easily in Vert.x Async Callbacks. Callback management.
* [VxRifa](https://nsforth.github.io/vxrifa) - Utility library for Vert.X that allows using strong-typed interfaces in communication through EventBus.
* [Vert.x Effect](https://github.com/imrafaelmerino/vertx-effect) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/vertx-effect?style=flat)](https://github.com/imrafaelmerino/vertx-effect/stargazers) - Pure functional and reactive library based on the IO Monad to implement any complex flow. Full support for retry, fallback and recovery operations.
* [SmallRye Mutiny](https://smallrye.io/smallrye-mutiny/) - Intuitive event-driven reactive programming library for Java with [bindings for Vert.x](https://smallrye.io/smallrye-mutiny-vertx-bindings/).

## Sync Thread Non Block

* [Sync](https://github.com/vert-x3/vertx-sync) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-sync?style=flat)](https://github.com/vert-x3/vertx-sync/stargazers) - Synchronous but non-OS-thread-blocking verticles.

## Vert.x Event Bus Clients

*Clients to connect applications to the Vert.x event bus*

* [C++11](https://github.com/julien3/vertxbuspp) [![GitHub stars](https://img.shields.io/github/stars/julien3/vertxbuspp?style=flat)](https://github.com/julien3/vertxbuspp/stargazers) - C++11 event bus client.
* [Java](https://github.com/saffron-technology/vertx-eventbusbridge) [![GitHub stars](https://img.shields.io/github/stars/saffron-technology/vertx-eventbusbridge?style=flat)](https://github.com/saffron-technology/vertx-eventbusbridge/stargazers) - Java implementation of vertxbus.js.
* [Java](https://github.com/abdlquadri/vertx-eventbus-java) [![GitHub stars](https://img.shields.io/github/stars/abdlquadri/vertx-eventbus-java?style=flat)](https://github.com/abdlquadri/vertx-eventbus-java/stargazers) - Java and Android Event Bus Client.
* [Java](https://github.com/danielstieger/javaxbus) [![GitHub stars](https://img.shields.io/github/stars/danielstieger/javaxbus?style=flat)](https://github.com/danielstieger/javaxbus/stargazers) - Simple Java Event Bus Client using plain TCP socket I/O.
* [CLI](https://github.com/cinterloper/vxc) [![GitHub stars](https://img.shields.io/github/stars/cinterloper/vxc?style=flat)](https://github.com/cinterloper/vxc/stargazers) - Command-line binary client for Vert.x event bus - pipe in JSON, emit JSON.
* [Swift](https://github.com/tobias/vertx-swift-eventbus) [![GitHub stars](https://img.shields.io/github/stars/tobias/vertx-swift-eventbus?style=flat)](https://github.com/tobias/vertx-swift-eventbus/stargazers) - Event bus client for [Apple's Swift](https://swift.org) using the [TCP-based protocol](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-tcp-eventbus-bridge?style=flat)](https://github.com/vert-x3/vertx-tcp-eventbus-bridge/stargazers).
* [Python](https://github.com/jaymine/TCP-eventbus-client-Python) [![GitHub stars](https://img.shields.io/github/stars/jaymine/TCP-eventbus-client-Python?style=flat)](https://github.com/jaymine/TCP-eventbus-client-Python/stargazers) - Event bus client for Python using the [TCP-based protocol](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-tcp-eventbus-bridge?style=flat)](https://github.com/vert-x3/vertx-tcp-eventbus-bridge/stargazers).
* [C#](https://github.com/jaymine/TCP-eventbus-client-C-Sharp) [![GitHub stars](https://img.shields.io/github/stars/jaymine/TCP-eventbus-client-C-Sharp?style=flat)](https://github.com/jaymine/TCP-eventbus-client-C-Sharp/stargazers) - Event bus client for C# using the [TCP-based protocol](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-tcp-eventbus-bridge?style=flat)](https://github.com/vert-x3/vertx-tcp-eventbus-bridge/stargazers).
* [C](https://github.com/jaymine/TCP-eventbus-client-C) [![GitHub stars](https://img.shields.io/github/stars/jaymine/TCP-eventbus-client-C?style=flat)](https://github.com/jaymine/TCP-eventbus-client-C/stargazers) - Event bus client for C99 using the [TCP-based protocol](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-tcp-eventbus-bridge?style=flat)](https://github.com/vert-x3/vertx-tcp-eventbus-bridge/stargazers).
* [Go](https://github.com/jponge/vertx-go-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/jponge/vertx-go-tcp-eventbus-bridge?style=flat)](https://github.com/jponge/vertx-go-tcp-eventbus-bridge/stargazers)- Event bus client for Go-lang using the [TCP-based protocol](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-tcp-eventbus-bridge?style=flat)](https://github.com/vert-x3/vertx-tcp-eventbus-bridge/stargazers).
* [Smalltalk](https://github.com/mumez/VerStix) [![GitHub stars](https://img.shields.io/github/stars/mumez/VerStix?style=flat)](https://github.com/mumez/VerStix/stargazers)- Event bus client for [Pharo Smalltalk](http://pharo.org/) using the [TCP-based protocol](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-tcp-eventbus-bridge?style=flat)](https://github.com/vert-x3/vertx-tcp-eventbus-bridge/stargazers).
* [Java](https://github.com/nielsbaloe/vertxui/tree/master/vertxui-core/src/main/java/live/connector/vertxui/client/transport) [![GitHub stars](https://img.shields.io/github/stars/nielsbaloe/vertxui/tree/master/vertxui-core/src/main/java/live/connector/vertxui/client/transport?style=flat)](https://github.com/nielsbaloe/vertxui/tree/master/vertxui-core/src/main/java/live/connector/vertxui/client/transport/stargazers) - Event bus support in JavaScript through Java code.
* [Elixir](https://github.com/PharosProduction/ExVertx) [![GitHub stars](https://img.shields.io/github/stars/PharosProduction/ExVertx?style=flat)](https://github.com/PharosProduction/ExVertx/stargazers) - Event bus support for Elixir apps using TCP socket.
* [Rust](https://github.com/aesteve/vertx-eventbus-client-rs) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-eventbus-client-rs?style=flat)](https://github.com/aesteve/vertx-eventbus-client-rs/stargazers) - Event bus client for Rust applications through TCP.

## Vert.x Event Bus Extensions

* [Eventbus Service](https://github.com/wowselim/eventbus-service) [![GitHub stars](https://img.shields.io/github/stars/wowselim/eventbus-service?style=flat)](https://github.com/wowselim/eventbus-service/stargazers) - Code generator for type-safe event bus communication via simple Kotlin interfaces.

## Cluster Managers

*Implementations of the Vert.x cluster manager SPI*

* [Hazelcast Cluster Manager](https://github.com/vert-x3/vertx-hazelcast) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-hazelcast?style=flat)](https://github.com/vert-x3/vertx-hazelcast/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Hazelcast cluster manager.
* [Ignite Cluster Manager](https://github.com/vert-x3/vertx-ignite) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-ignite?style=flat)](https://github.com/vert-x3/vertx-ignite/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Ignite cluster manager.
* [JGroups Cluster Manager](https://github.com/vert-x3/vertx-jgroups) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-jgroups?style=flat)](https://github.com/vert-x3/vertx-jgroups/stargazers) - JGroups cluster manager.
* [Zookeeper Cluster Manager](https://github.com/vert-x3/vertx-zookeeper) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-zookeeper?style=flat)](https://github.com/vert-x3/vertx-zookeeper/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Zookeeper cluster manager.
* [Infinispan Cluster Manager](https://github.com/vert-x3/vertx-infinispan) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-infinispan?style=flat)](https://github.com/vert-x3/vertx-infinispan/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Infinispan cluster manager.
* [Consul Cluster Manager](https://github.com/reactiverse/consul-cluster-manager) [![GitHub stars](https://img.shields.io/github/stars/reactiverse/consul-cluster-manager?style=flat)](https://github.com/reactiverse/consul-cluster-manager/stargazers) - Consul cluster manager.

## Cloud Support

* [OpenShift DIY cartridge](https://github.com/vert-x3/vertx-openshift-diy-quickstart) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-openshift-diy-quickstart?style=flat)](https://github.com/vert-x3/vertx-openshift-diy-quickstart/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - OpenShift DIY Cartridge using Vert.x.
* [OpenShift Vert.x cartridge](https://github.com/vert-x3/vertx-openshift-cartridge) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-openshift-cartridge?style=flat)](https://github.com/vert-x3/vertx-openshift-cartridge/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - OpenShift Vert.x Cartridge using Vert.x.
* [AWS SDK](https://github.com/reactiverse/aws-sdk) [![GitHub stars](https://img.shields.io/github/stars/reactiverse/aws-sdk?style=flat)](https://github.com/reactiverse/aws-sdk/stargazers) - Use AWS Java SDK v2 (async) with Vert.x

## Microservices

* [Service Discovery](https://github.com/vert-x3/vertx-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-discovery?style=flat)](https://github.com/vert-x3/vertx-service-discovery/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Service Discovery" height="16px"> - Vert.x Service Discovery.
* [Circuit Breaker](https://github.com/vert-x3/vertx-circuit-breaker) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-circuit-breaker?style=flat)](https://github.com/vert-x3/vertx-circuit-breaker/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Circuit Breaker" height="16px"> - Vert.x Circuit Breaker.
* [Service Discovery - Consul](https://github.com/vert-x3/vertx-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-discovery?style=flat)](https://github.com/vert-x3/vertx-service-discovery/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Service Discovery - Consul" height="16px"> - [Consul](https://www.consul.io/) extension to Vert.x Service Discovery.
* [Service Discovery - Docker links](https://github.com/vert-x3/vertx-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-discovery?style=flat)](https://github.com/vert-x3/vertx-service-discovery/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Service Discovery - Docker Links" height="16px"> - [Docker](https://www.docker.com/) extension to Vert.x Service Discovery.
* [Service Discovery - Kubernetes](https://github.com/vert-x3/vertx-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-discovery?style=flat)](https://github.com/vert-x3/vertx-service-discovery/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Service Discovery - Kubernetes" height="16px"> - [Kubernetes](http://kubernetes.io/) extension to Vert.x Service Discovery.
* [Service Discovery - Redis backend](https://github.com/vert-x3/vertx-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-discovery?style=flat)](https://github.com/vert-x3/vertx-service-discovery/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Service Discovery - Redis backend" height="16px"> - [Redis](http://redis.io/) storage backend for Vert.x Service Discovery.
* [Vert.x GraphQL Service Discovery](https://github.com/engagingspaces/vertx-graphql-service-discovery) [![GitHub stars](https://img.shields.io/github/stars/engagingspaces/vertx-graphql-service-discovery?style=flat)](https://github.com/engagingspaces/vertx-graphql-service-discovery/stargazers) - [GraphQL](http://graphql.org/) service discovery and querying for your Vert.x microservices.
* [Resilience4j](https://github.com/resilience4j/resilience4j) [![GitHub stars](https://img.shields.io/github/stars/resilience4j/resilience4j?style=flat)](https://github.com/resilience4j/resilience4j/stargazers) - Resilience4j is a fault tolerance library designed for Java8 and functional programming. Resilience4j provides modules for Circuit Breaking, Rate Limiting, Bulkheading, Automatic retrying, Response caching and Metric measuring.
* [Failsafe](https://failsafe.dev/) - Failsafe is a lightweight, *zero-dependency* library for handling failures in Java 8+. Concise API. Integration with libraries that use their own schedulers for async executions, such as Akka or Vert.x. [Vert.x example](https://github.com/failsafe-lib/failsafe/blob/master/examples/src/main/java/dev/failsafe/examples/VertxExample.java) [![GitHub stars](https://img.shields.io/github/stars/failsafe-lib/failsafe/blob/master/examples/src/main/java/dev/failsafe/examples/VertxExample.java?style=flat)](https://github.com/failsafe-lib/failsafe/blob/master/examples/src/main/java/dev/failsafe/examples/VertxExample.java/stargazers)
* [Autonomous Services](https://github.com/mikand13/autonomous-services) [![GitHub stars](https://img.shields.io/github/stars/mikand13/autonomous-services?style=flat)](https://github.com/mikand13/autonomous-services/stargazers) - A toolkit for creating autonomous services. An architecture that leverages vert.x and nannoq-tools to provide an event-based reactive architecure without centralized components, neither for communication or data, providing a theoretically linear scalability across the architecture.
* [Apache ServiceComb Java Chassis](https://github.com/apache/servicecomb-java-chassis) [![GitHub stars](https://img.shields.io/github/stars/apache/servicecomb-java-chassis?style=flat)](https://github.com/apache/servicecomb-java-chassis/stargazers) - ServiceComb Java Chassis is a Software Development Kit (SDK) for rapid development of microservices in Java, providing service registration, service discovery, dynamic routing, and service management features.
* [SmallRye Fault Tolerance](https://github.com/smallrye/smallrye-fault-tolerance) [![GitHub stars](https://img.shields.io/github/stars/smallrye/smallrye-fault-tolerance?style=flat)](https://github.com/smallrye/smallrye-fault-tolerance/stargazers) - SmallRye Fault Tolerance is an implementation of Eclipse MicroProfile Fault Tolerance with additional features not defined by the specification. Native support of [Vert.x](https://smallrye.io/docs/smallrye-fault-tolerance/6.2.6/integration/event-loop.html) and [Mutiny](https://smallrye.io/docs/smallrye-fault-tolerance/6.2.6/reference/asynchronous.html#async-types).

## Game development

* [Orbital](https://github.com/tfkfan/orbital) [![GitHub stars](https://img.shields.io/github/stars/tfkfan/orbital?style=flat)](https://github.com/tfkfan/orbital/stargazers) - Vert.x based reactive distributed game server and battle-royale multiplayers development tool. Orbital contains basic extensible matchmaker, game/game room management, websocket integration and game lifecycle management features. Closest to "Colyseus" game engine competitor. [Docs](https://tfkfan.github.io/orbital).

## Search Engines

* [Vert.x Elasticsearch Service](https://github.com/englishtown/vertx-elasticsearch-service) [![GitHub stars](https://img.shields.io/github/stars/englishtown/vertx-elasticsearch-service?style=flat)](https://github.com/englishtown/vertx-elasticsearch-service/stargazers) - Vert.x 3 [Elasticsearch](https://www.elastic.co/) service with event bus proxying.
* [Vert.x Solr Service](https://github.com/englishtown/vertx-solr-service) [![GitHub stars](https://img.shields.io/github/stars/englishtown/vertx-solr-service?style=flat)](https://github.com/englishtown/vertx-solr-service/stargazers) - Vert.x 3 Solr service with event bus proxying.

## Service Factory

* [Service Factory](https://github.com/vert-x3/vertx-service-factory) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-factory?style=flat)](https://github.com/vert-x3/vertx-service-factory/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x Service Factory.
* [Maven Service Factory](https://github.com/vert-x3/vertx-maven-service-factory) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-maven-service-factory?style=flat)](https://github.com/vert-x3/vertx-maven-service-factory/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Maven Vert.x Service Factory.
* [HTTP Service Factory](https://github.com/vert-x3/vertx-http-service-factory) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-http-service-factory?style=flat)](https://github.com/vert-x3/vertx-http-service-factory/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x HTTP Service Factory.
* [Node.js Service Factory](https://github.com/mellster2012/vertx-nodejs-service-factory) [![GitHub stars](https://img.shields.io/github/stars/mellster2012/vertx-nodejs-service-factory?style=flat)](https://github.com/mellster2012/vertx-nodejs-service-factory/stargazers) - Vert.x Node.js Service Factory.
* [Eclipse SISU Service Factories](https://github.com/cstamas/vertx-sisu) [![GitHub stars](https://img.shields.io/github/stars/cstamas/vertx-sisu?style=flat)](https://github.com/cstamas/vertx-sisu/stargazers) - Vert.x integration with [Eclipse SISU](https://www.eclipse.org/sisu/) DI container offering alternatives for `vertx-service-factory` and `vertx-maven-service-factory`.

## Config

* [Vert.x Config AWS SSM Store](https://github.com/Finovertech/vertx-config-aws-ssm) [![GitHub stars](https://img.shields.io/github/stars/Finovertech/vertx-config-aws-ssm?style=flat)](https://github.com/Finovertech/vertx-config-aws-ssm/stargazers) - A [config store](http://vertx.io/docs/vertx-config/java/) implementation for retrieving configuration values from the [AWS EC2 SSM Parameter Store](https://aws.amazon.com/ec2/systems-manager/parameter-store/).
* [Vert.x Boot](https://github.com/jponge/vertx-boot) [![GitHub stars](https://img.shields.io/github/stars/jponge/vertx-boot?style=flat)](https://github.com/jponge/vertx-boot/stargazers) - Deploying verticles from a HOCON configuration.

## Dependency Injection

* [Vert.x Guice](https://github.com/englishtown/vertx-guice) [![GitHub stars](https://img.shields.io/github/stars/englishtown/vertx-guice?style=flat)](https://github.com/englishtown/vertx-guice/stargazers) - Vert.x verticle factory for Guice dependency injection.
* [Vert.x HK2](https://github.com/englishtown/vertx-hk2) [![GitHub stars](https://img.shields.io/github/stars/englishtown/vertx-hk2?style=flat)](https://github.com/englishtown/vertx-hk2/stargazers) - Vert.x verticle factory for HK2 dependency injection.
* [Spring Vert.x Extension](https://github.com/amoAHCP/spring-vertx-ext) [![GitHub stars](https://img.shields.io/github/stars/amoAHCP/spring-vertx-ext?style=flat)](https://github.com/amoAHCP/spring-vertx-ext/stargazers) - Vert.x verticle factory for Spring DI injection.
* [Vert.x Beans](https://github.com/rworsnop/vertx-beans) [![GitHub stars](https://img.shields.io/github/stars/rworsnop/vertx-beans?style=flat)](https://github.com/rworsnop/vertx-beans/stargazers) - Inject Vert.x objects as beans into your Spring application.
* [QBit](https://github.com/advantageous/qbit) [![GitHub stars](https://img.shields.io/github/stars/advantageous/qbit?style=flat)](https://github.com/advantageous/qbit/stargazers) - QBit works with Spring DI and Spring Boot (and of course Vert.x). Allows you to use QBit, Vert.x, Spring DI and Spring Boot in the same application.
* [Vert.x Eclipse SISU](https://github.com/cstamas/vertx-sisu) [![GitHub stars](https://img.shields.io/github/stars/cstamas/vertx-sisu?style=flat)](https://github.com/cstamas/vertx-sisu/stargazers) - Vert.x integration with [Eclipse SISU](https://www.eclipse.org/sisu/) DI container.
* [Vert.x Spring Verticle Factory](https://github.com/juanavelez/vertx-spring-verticle-factory) [![GitHub stars](https://img.shields.io/github/stars/juanavelez/vertx-spring-verticle-factory?style=flat)](https://github.com/juanavelez/vertx-spring-verticle-factory/stargazers) - A Vert.x Verticle Factory that makes use of Spring to obtain and configure Verticles.
* [Glue](https://github.com/vinscom/glue) [![GitHub stars](https://img.shields.io/github/stars/vinscom/glue?style=flat)](https://github.com/vinscom/glue/stargazers) - Proven and opinionated programming, and configuration model for Java and Vert.x based applications. Inspired from ATG Nucleus, provides powerful layer base configuration management using simple properties file.

## Testing

* [Vert.x Unit](https://github.com/vert-x3/vertx-unit) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-unit?style=flat)](https://github.com/vert-x3/vertx-unit/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Async polyglot unit testing for Vert.x.
* [Vert.x JUnit5](https://github.com/vert-x3/vertx-junit5) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-junit5?style=flat)](https://github.com/vert-x3/vertx-junit5/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Async unit testing for Vert.x with junit5.
* [Vert.x WireMongo](https://github.com/noenv/vertx-wiremongo) [![GitHub stars](https://img.shields.io/github/stars/noenv/vertx-wiremongo?style=flat)](https://github.com/noenv/vertx-wiremongo/stargazers) - Lightweight MongoDB mocking for Vert.x

## Development Tools

* [Vert.x shell](https://github.com/vert-x3/vertx-shell) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-shell?style=flat)](https://github.com/vert-x3/vertx-shell/stargazers)  <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Allows for interaction with Vert.x from the command line.
* [Vert.x health check](https://github.com/vert-x3/vertx-health-check) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-health-check?style=flat)](https://github.com/vert-x3/vertx-health-check/stargazers) - Allows for remote health checking in Vert.x projects.
* [Vert.x Hot](https://github.com/dazraf/vertx-hot) [![GitHub stars](https://img.shields.io/github/stars/dazraf/vertx-hot?style=flat)](https://github.com/dazraf/vertx-hot/stargazers) - A Maven plugin for the hot-deploy of Maven Vert.x projects.
* [Vert.x for Visual Studio Code](https://github.com/pmlopes/VertxSnippet) [![GitHub stars](https://img.shields.io/github/stars/pmlopes/VertxSnippet?style=flat)](https://github.com/pmlopes/VertxSnippet/stargazers) - A Visual Studio Code (polyglot) plugin for Vert.x. Also available from the [Marketplace](https://marketplace.visualstudio.com/items?itemName=pmlopes.vertxsnippet).
* [Vert.x Starter](http://www.jetdrone.xyz/vertx-starter/) - A browser-based project starter and project templates for Vert.x applications.
* [Vert.x LiveReload](https://github.com/ybonnel/vertx-livereload) [![GitHub stars](https://img.shields.io/github/stars/ybonnel/vertx-livereload?style=flat)](https://github.com/ybonnel/vertx-livereload/stargazers) - A simple livereload server for Vert.x applications.
* [openapi-generator](https://github.com/OpenAPITools/openapi-generator) [![GitHub stars](https://img.shields.io/github/stars/OpenAPITools/openapi-generator?style=flat)](https://github.com/OpenAPITools/openapi-generator/stargazers) - OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3).

## Miscellaneous

* [Vert.x Child Process](https://github.com/vietj/vertx-childprocess) [![GitHub stars](https://img.shields.io/github/stars/vietj/vertx-childprocess?style=flat)](https://github.com/vietj/vertx-childprocess/stargazers) - Spawn child process from Vert.x.
* [vertx-redisques](https://github.com/swisspush/vertx-redisques) [![GitHub stars](https://img.shields.io/github/stars/swisspush/vertx-redisques?style=flat)](https://github.com/swisspush/vertx-redisques/stargazers) - A highly scalable redis-persistent queuing system for Vert.x.
* [Simple File Server](https://github.com/pitchpoint-solutions/sfs) [![GitHub stars](https://img.shields.io/github/stars/pitchpoint-solutions/sfs?style=flat)](https://github.com/pitchpoint-solutions/sfs/stargazers) - An OpenStack Swift compatible distributed object storage server that can serve and securely store billions of large and small files using minimal resources implemented using Vert.x.
* [Vert.x Boot](https://github.com/jponge/vertx-boot) [![GitHub stars](https://img.shields.io/github/stars/jponge/vertx-boot?style=flat)](https://github.com/jponge/vertx-boot/stargazers) - Deploying verticles from a HOCON configuration.
* [GDH](https://github.com/maxamel/GDH) [![GitHub stars](https://img.shields.io/github/stars/maxamel/GDH?style=flat)](https://github.com/maxamel/GDH/stargazers) - Generalized Diffie-Hellman key exchange Java library built on top of Vert.x.
* [vertx-values](https://github.com/imrafaelmerino/vertx-values) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/vertx-values?style=flat)](https://github.com/imrafaelmerino/vertx-values/stargazers) - Send immutable and persistent JSON from [json-values](https://github.com/imrafaelmerino/json-values) [![GitHub stars](https://img.shields.io/github/stars/imrafaelmerino/json-values?style=flat)](https://github.com/imrafaelmerino/json-values/stargazers) across the event bus.

## Distribution

* [Vert.x Stack](https://github.com/vert-x3/vertx-stack) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-stack?style=flat)](https://github.com/vert-x3/vertx-stack/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x + the endorsed modules.

## Examples

* [Vert.x blueprint - Microservice application](https://github.com/sczyh30/vertx-blueprint-microservice) [![GitHub stars](https://img.shields.io/github/stars/sczyh30/vertx-blueprint-microservice?style=flat)](https://github.com/sczyh30/vertx-blueprint-microservice/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - The official Vert.x blueprint showing how to build a complex microservice application.
* [Vert.x blueprint - Job Queue](https://github.com/sczyh30/vertx-blueprint-job-queue) [![GitHub stars](https://img.shields.io/github/stars/sczyh30/vertx-blueprint-job-queue?style=flat)](https://github.com/sczyh30/vertx-blueprint-job-queue/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - The official Vert.x blueprint showing how to build a distributed job processing application.
* [Vert.x blueprint - TODO backend](https://github.com/sczyh30/vertx-blueprint-todo-backend) [![GitHub stars](https://img.shields.io/github/stars/sczyh30/vertx-blueprint-todo-backend?style=flat)](https://github.com/sczyh30/vertx-blueprint-todo-backend/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - The official Vert.x blueprint showing how to build a backend for a TODO application.
* [Vert.x examples](https://github.com/vert-x3/vertx-examples) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-examples?style=flat)](https://github.com/vert-x3/vertx-examples/stargazers) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - The official Vert.x examples including web examples, how to use the official database clients, etc.
* [Vert.x feeds](https://github.com/aesteve/vertx-feeds) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-feeds?style=flat)](https://github.com/aesteve/vertx-feeds/stargazers) - Example of an RSS aggregator built using Vert.x, Gradle, MongoDB, Redis, Handlebars templates, AngularJS, the event bus and SockJS.
* [Vert.x Markdown service](https://github.com/aesteve/vertx-markdown-service) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-markdown-service?style=flat)](https://github.com/aesteve/vertx-markdown-service/stargazers) - Example on how to use [service-proxy](https://github.com/vert-x3/vertx-service-proxy) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-service-proxy?style=flat)](https://github.com/vert-x3/vertx-service-proxy/stargazers) with Gradle.
* [Example using event bus and service proxies to connect vertx and node](https://github.com/advantageous/vertx-node-ec2-eventbus-example) [![GitHub stars](https://img.shields.io/github/stars/advantageous/vertx-node-ec2-eventbus-example?style=flat)](https://github.com/advantageous/vertx-node-ec2-eventbus-example/stargazers) - Step by step example with wiki description showing how to connect Vert.x and Node using event bus and service proxies.
* [Vert.x Todo-Backend implementation](https://github.com/aesteve/todo-backend-vertx) [![GitHub stars](https://img.shields.io/github/stars/aesteve/todo-backend-vertx?style=flat)](https://github.com/aesteve/todo-backend-vertx/stargazers) - Pure Java 8 implementation of the Todo MVC backend. Uses a Vert.x LocalMap for storage.
* [Kotlin Todo-Backend implementation](https://github.com/aesteve/vertx-kotlin-todomvc) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-kotlin-todomvc?style=flat)](https://github.com/aesteve/vertx-kotlin-todomvc/stargazers) - Kotlin implementation of the Todo MVC backend.
* [Scala Todo-Backend implementation](https://github.com/aesteve/vertx-scala-todomvc) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-scala-todomvc?style=flat)](https://github.com/aesteve/vertx-scala-todomvc/stargazers) - Scala implementation of the Todo MVC backend.
* [Grooveex Todo-Backend implementation](https://github.com/aesteve/todo-backend-grooveex) [![GitHub stars](https://img.shields.io/github/stars/aesteve/todo-backend-grooveex?style=flat)](https://github.com/aesteve/todo-backend-grooveex/stargazers) - Todo MVC backend implementation with Vert.x + Groovy + some syntactic sugar + DSL routing facilities.
* [Vert.x Gradle Starter](https://github.com/yyunikov/vertx-gradle-starter) [![GitHub stars](https://img.shields.io/github/stars/yyunikov/vertx-gradle-starter?style=flat)](https://github.com/yyunikov/vertx-gradle-starter/stargazers) - Java 8 starter application with example of using Vert.x with Gradle build system, profiles configuration and SLF4J.
* [Vert.x Gentics Mesh Example](https://github.com/gentics/mesh-vertx-example) [![GitHub stars](https://img.shields.io/github/stars/gentics/mesh-vertx-example?style=flat)](https://github.com/gentics/mesh-vertx-example/stargazers) - Example on how to build a template-based web server with Gentics Mesh and handlebars.
* [HTTP/2 showcase](https://github.com/aesteve/http2-showcase) [![GitHub stars](https://img.shields.io/github/stars/aesteve/http2-showcase?style=flat)](https://github.com/aesteve/http2-showcase/stargazers) - A simple demo, showing how HTTP/2 can drastically improve user experience when a huge latency is involved.
* [Vert.x Music Store](https://github.com/tsegismont/vertx-musicstore) [![GitHub stars](https://img.shields.io/github/stars/tsegismont/vertx-musicstore?style=flat)](https://github.com/tsegismont/vertx-musicstore/stargazers) - An example application on how to build Vert.x applications with RxJava.
* [Crabzilla](https://github.com/crabzilla/crabzilla) [![GitHub stars](https://img.shields.io/github/stars/crabzilla/crabzilla?style=flat)](https://github.com/crabzilla/crabzilla/stargazers) - Yet another Event Sourcing experiment. A project exploring Vert.x to develop Event Sourcing / CQRS applications.
* [Vert.x PostgreSQL Starter](https://github.com/BillyYccc/vertx-postgresql-starter) [![GitHub stars](https://img.shields.io/github/stars/BillyYccc/vertx-postgresql-starter?style=flat)](https://github.com/BillyYccc/vertx-postgresql-starter/stargazers) - A starter to build a monolithic CRUD RESTful Web Service with Vert.x stack and PostgreSQL.
* [Cloud Foundry](https://github.com/amdelamar/vertx-cloudfoundry) [![GitHub stars](https://img.shields.io/github/stars/amdelamar/vertx-cloudfoundry?style=flat)](https://github.com/amdelamar/vertx-cloudfoundry/stargazers) - An example Vert.x for deploying to a [Cloud Foundry](https://www.cloudfoundry.org/) service provider.
* [Knative](https://github.com/knative/docs/tree/main/code-samples/community/serving/helloworld-vertx) [![GitHub stars](https://img.shields.io/github/stars/knative/docs/tree/main/code-samples/community/serving/helloworld-vertx?style=flat)](https://github.com/knative/docs/tree/main/code-samples/community/serving/helloworld-vertx/stargazers) - An example application on how to use [Reactive Extensions Vert.x](https://github.com/vert-x3/vertx-rx) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-rx?style=flat)](https://github.com/vert-x3/vertx-rx/stargazers) with [Knative](https://github.com/knative) [![GitHub stars](https://img.shields.io/github/stars/knative?style=flat)](https://github.com/knative/stargazers).
* [Starter Single Verticle API](https://github.com/jgarciasm/ssv-api) [![GitHub stars](https://img.shields.io/github/stars/jgarciasm/ssv-api?style=flat)](https://github.com/jgarciasm/ssv-api/stargazers) - REST API Starter and Project Template ready to deploy with lots of plumbing code, examples, and documentation to quickly develope an API with almost no knowledge of vert.x and without any waste of time.
* [AI model output API based on PMML with Vert.x](https://github.com/immusen/vertx-pmml) [![GitHub stars](https://img.shields.io/github/stars/immusen/vertx-pmml?style=flat)](https://github.com/immusen/vertx-pmml/stargazers) - High performance PMML evaluator API based on Vert.x. Supports dynamic routing configuration for multiple PMML models via JSON.

## Deployment

* [Vert.x Deploy Application](https://github.com/msoute/vertx-deploy-tools) [![GitHub stars](https://img.shields.io/github/stars/msoute/vertx-deploy-tools?style=flat)](https://github.com/msoute/vertx-deploy-tools/stargazers) - (Seamless) deploy to AWS based Vert.x application clusters.

## Utilities

* [Chime](https://github.com/LisiLisenok/Chime) [![GitHub stars](https://img.shields.io/github/stars/LisiLisenok/Chime?style=flat)](https://github.com/LisiLisenok/Chime/stargazers) - Time scheduler working on Vert.x event bus allowing for scheduling with *cron-style* and *interval* timers.
* [Vert.x Cron](https://github.com/diabolicallabs/vertx-cron) [![GitHub stars](https://img.shields.io/github/stars/diabolicallabs/vertx-cron?style=flat)](https://github.com/diabolicallabs/vertx-cron/stargazers) - Schedule events with cron specifications. Has event bus and Observable versions.
* [Vert.x CronUtils](https://github.com/NoEnv/vertx-cronutils) [![GitHub stars](https://img.shields.io/github/stars/NoEnv/vertx-cronutils?style=flat)](https://github.com/NoEnv/vertx-cronutils/stargazers) - An abstraction of cron-utils for the vertx scheduler. Unix, Cron4j and Quartz style expressions are supported.
* [Vert.x Scheduler](https://github.com/zero88/vertx-scheduler) [![GitHub stars](https://img.shields.io/github/stars/zero88/vertx-scheduler?style=flat)](https://github.com/zero88/vertx-scheduler/stargazers) - A lightweight plugable scheduler based on plain Vert.x core without any external libs for scheduling with *cron-style* and *interval* timers with a detail *monitor* on both sync and async task.
* [Vert.x POJO config](https://github.com/aesteve/vertx-pojo-config) [![GitHub stars](https://img.shields.io/github/stars/aesteve/vertx-pojo-config?style=flat)](https://github.com/aesteve/vertx-pojo-config/stargazers) - Allows for mapping between standard JSON configuration and a (type-safe) configuration Java bean. Also allows the configuration bean to be validated through JSR 303.
* [Vert.x Async](https://github.com/gchauvet/vertx-async) [![GitHub stars](https://img.shields.io/github/stars/gchauvet/vertx-async?style=flat)](https://github.com/gchauvet/vertx-async/stargazers) - Portage of caolan/async nodejs module to Vert.x framework that provides helpers methods for common async patterns.
* [Vert.x JOLT](https://github.com/lusoalex/vertx-jolt) [![GitHub stars](https://img.shields.io/github/stars/lusoalex/vertx-jolt?style=flat)](https://github.com/lusoalex/vertx-jolt/stargazers) - JSON to JSON transformation tool based on the original bazaarvoice JOLT project. Helpful to transform different json structure into an expected json format.
* [Vert.x Dependent Verticle Deployer](https://github.com/juanavelez/vertx-dependent-verticle-deployer) [![GitHub stars](https://img.shields.io/github/stars/juanavelez/vertx-dependent-verticle-deployer?style=flat)](https://github.com/juanavelez/vertx-dependent-verticle-deployer/stargazers) - A Vert.x Verticle intended to deploy verticles and their dependent verticles.
* [Vert.x Dataloader](https://github.com/engagingspaces/vertx-dataloader) [![GitHub stars](https://img.shields.io/github/stars/engagingspaces/vertx-dataloader?style=flat)](https://github.com/engagingspaces/vertx-dataloader/stargazers) - Java port of Facebook Dataloader for Vert.x. Efficient batching and caching for your data layer.
* [Vert.x Util](https://github.com/juanavelez/vertx-util) [![GitHub stars](https://img.shields.io/github/stars/juanavelez/vertx-util?style=flat)](https://github.com/juanavelez/vertx-util/stargazers) - A collection of Vert.x utility methods.
* [Vert.x Web Accesslog](https://github.com/romanpierson/vertx-web-accesslog) [![GitHub stars](https://img.shields.io/github/stars/romanpierson/vertx-web-accesslog?style=flat)](https://github.com/romanpierson/vertx-web-accesslog/stargazers) - Just a simple handler to be used in Vert.x Web to generate access logs.
* [Vert.x GraphQL Utils](http://github.com/tibor-kocsis/vertx-graphql-utils) - A route handler and Vert.x compatible interfaces to handle GraphQL queries in Vert.x and Vert.x Web.
* [Nannoq-Tools](https://noriginmedia.github.io/nannoq-tools/) - Nannoq-Tools is a toolkit for constructing robust, scalable and distributed applications leveraging Vert.x including modules for authentication, cluster management, Firebase Cloud Messaging, DynamoDB, fully generic queries, REST, and more.
* [Contextual logging](https://github.com/reactiverse/reactiverse-contextual-logging) [![GitHub stars](https://img.shields.io/github/stars/reactiverse/reactiverse-contextual-logging?style=flat)](https://github.com/reactiverse/reactiverse-contextual-logging/stargazers) - Mapped Diagnostic Context (MDC) that works with the Vert.x event-loop model.
* [Vert.x JsonPath](https://github.com/NoEnv/vertx-jsonpath) [![GitHub stars](https://img.shields.io/github/stars/NoEnv/vertx-jsonpath?style=flat)](https://github.com/NoEnv/vertx-jsonpath/stargazers) - A very basic implementation of JsonPath using Vert.x’s JsonObject and JsonArray, mimicking their getX, containsKey, put and remove methods.

## Presentations

* [Vert.x Youtube channel](https://www.youtube.com/channel/UCGN6L3tRhs92Uer3c6VxOSA)

## Community

* [User Group](https://groups.google.com/forum/?fromgroups#!forum/vertx) - Discuss all user issues related to *using* Vert.x.
* [Developer Group](https://groups.google.com/forum/?fromgroups#!forum/vertx-dev) - A group for Vert.x core *developers* and *contributors*.
* [Discord Server](https://discord.gg/KzEMwP2) - Chat about any Vert.x-related topic.
* [Issues](https://github.com/vert-x3/issues/issues) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/issues/issues?style=flat)](https://github.com/vert-x3/issues/issues/stargazers) - Vert.x core issue tracker.
* [Wiki](https://github.com/vert-x3/wiki/wiki) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/wiki/wiki?style=flat)](https://github.com/vert-x3/wiki/wiki/stargazers) - Contains useful information about Vert.x.
* [Blog](http://vertx.io/blog/) - The official Vert.x blog containing many tutorials and other information.

## Articles

* [Embracing Reactive Applications on JVM: a Deep Dive into Modern I/O Models and Vert.x](https://www.infoq.com/articles/reactive-java-vertx-deep-dive/)
* [Going reactive with Eclipse Vert.x and RX Java](https://blogs.oracle.com/javamagazine/post/going-reactive-with-eclipse-vertx-and-rxjava)
* [Vert.x 3.3.0 Features Enhanced Networking Microservices, Testing and More](https://www.infoq.com/news/2016/06/Vert.x-3.3.0-release-features)
* [Interview with Tim Fox About Vert.x 3, the Original Reactive, Microservice Toolkit for the JVM](http://www.infoq.com/articles/vertx-3-tim-fox)

## Tutorials

* [Introduction to Vert.x](https://vertx.io/get-started/)

## Front-End

* [VertxUI](https://github.com/nielsbaloe/vertxui) [![GitHub stars](https://img.shields.io/github/stars/nielsbaloe/vertxui?style=flat)](https://github.com/nielsbaloe/vertxui/stargazers) - A pure Java front-end toolkit with descriptive fluent views-on-models, POJO traffic, JUnit testing on the virtual DOM or mixed-language on a real DOM, and more.

## Contribute

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
