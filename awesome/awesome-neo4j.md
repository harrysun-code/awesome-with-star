# Neo4j

[![GitHub stars](https://img.shields.io/github/stars/neueda/awesome-neo4j?style=flat)](https://github.com/neueda/awesome-neo4j/stargazers)

Awesome Neo4j
==============
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Build Status](https://api.travis-ci.org/neueda/awesome-neo4j.svg?branch=master )](https://travis-ci.org/neueda/awesome-neo4j)

A curated list of awesome [Neo4j](https://neo4j.com/) resources.  
Inspired by the `awesome-*` trend on GitHub.

The goal is to build a categorized community-driven collection of very well-known resources.  
Sharing, suggestions and contributions are always welcome!

Thanks to all [contributors](https://github.com/Neueda/awesome-neo4j/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/Neueda/awesome-neo4j/graphs/contributors?style=flat)](https://github.com/Neueda/awesome-neo4j/graphs/contributors/stargazers).

Maintained by [Neueda R&D](http://labs.neueda.com/).

Table of Contents
=================

  * [Basics](#basics)
  * [Connectors](#connectors)
    * [Bolt](#bolt)
    * [REST API](#rest-api)
      * [Java](#java)
      * [Ruby](#ruby)
      * [Python](#python)
      * [PHP](#php)
      * [Other](#other)
  * [Cloud](#cloud)
  * [Packages](#packages)
  * [Docker](#docker)
  * [Full\-text search](#full-text-search)
  * [Import](#import)
  * [Benchmarking](#benchmarking)
  * [Extensions](#extensions)
  * [Stored Procedures](#stored-procedures)
  * [Development](#development)
  * [Editors](#editors)
  * [Shell](#shell)
  * [Visualization](#visualization)
  * [Tools](#tools)
  * [Resources](#resources)
    * [Learn](#learn)
    * [Certification](#certification)
    * [Bolt](#bolt-1)
    * [Books](#books)
    * [Miscellaneous](#miscellaneous)
  * [License](#license)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go) [![GitHub stars](https://img.shields.io/github/stars/ekalinin/github-markdown-toc.go?style=flat)](https://github.com/ekalinin/github-markdown-toc.go/stargazers)

# Basics

- [Official documentation](https://neo4j.com/docs/)
- [Cypher Refcard](https://neo4j.com/docs/cypher-refcard/current/)
- [Developer resources](https://neo4j.com/developer/get-started/)
- [Gists](http://graphgist.neo4j.com/) - With Neo4j GraphGists you can describe and model your domain in a simple text file and render it as a rich, interactive page in any browser. Perfect to document a specific domain, use-case, question or graph problem.
- [Neo4j Examples](https://github.com/neo4j-examples) [![GitHub stars](https://img.shields.io/github/stars/neo4j-examples?style=flat)](https://github.com/neo4j-examples/stargazers) - Examples for Neo4j and Library Usage.

# Related project

- [openCypher](http://www.opencypher.org/) - openCypher is an open source project to bring a new public implementation of the industry’s most widely adopted graph query language: Cypher.
- [Bolt Protocol](https://boltprotocol.org) - The Bolt network protocol is a highly efficient, lightweight client-server protocol designed for database applications.

# Connectors

## Bolt

- [neo4j-java-driver](https://github.com/neo4j/neo4j-java-driver) [![GitHub stars](https://img.shields.io/github/stars/neo4j/neo4j-java-driver?style=flat)](https://github.com/neo4j/neo4j-java-driver/stargazers) - Java driver for Neo4j binary protocol.
- [neo4j-python-driver](https://github.com/neo4j/neo4j-python-driver) [![GitHub stars](https://img.shields.io/github/stars/neo4j/neo4j-python-driver?style=flat)](https://github.com/neo4j/neo4j-python-driver/stargazers) - Python driver for Neo4j binary protocol.
- [neo4j-javascript-driver](https://github.com/neo4j/neo4j-javascript-driver) [![GitHub stars](https://img.shields.io/github/stars/neo4j/neo4j-javascript-driver?style=flat)](https://github.com/neo4j/neo4j-javascript-driver/stargazers) - JavaScript driver for Neo4j binary protocol.
- [neo4j-dotnet-driver](https://github.com/neo4j/neo4j-dotnet-driver) [![GitHub stars](https://img.shields.io/github/stars/neo4j/neo4j-dotnet-driver?style=flat)](https://github.com/neo4j/neo4j-dotnet-driver/stargazers) - .Net driver for Neo4j (Bolt).
- [neo4j-bolt-php](https://github.com/graphaware/neo4j-bolt-php) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-bolt-php?style=flat)](https://github.com/graphaware/neo4j-bolt-php/stargazers) - PHP driver for Neo4j binary protocol.
- [libneo4j-client](https://github.com/cleishm/libneo4j-client) [![GitHub stars](https://img.shields.io/github/stars/cleishm/libneo4j-client?style=flat)](https://github.com/cleishm/libneo4j-client/stargazers) - libneo4j-client is a client library written in C for Neo4j. It is not intended as a complete driver, but rather as a foundation on which basic tools and drivers for various languages may be built. libneo4j-client takes care of all the detail of establishing a session with a Neo4j server, sending statements for evaluation, and retrieving results.
- [neo4j-spark-connector](https://github.com/neo4j-contrib/neo4j-spark-connector) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neo4j-spark-connector?style=flat)](https://github.com/neo4j-contrib/neo4j-spark-connector/stargazers) - Neo4j-Spark-Connector based on Neo4j 3.0's Bolt protocol
- [neo4j-elixir-driver](https://github.com/mschae/boltex) [![GitHub stars](https://img.shields.io/github/stars/mschae/boltex?style=flat)](https://github.com/mschae/boltex/stargazers) - Elixir driver for the neo4j bolt protocol
- [neo4j-elixir-wrapper](https://github.com/florinpatrascu/bolt_sips) [![GitHub stars](https://img.shields.io/github/stars/florinpatrascu/bolt_sips?style=flat)](https://github.com/florinpatrascu/bolt_sips/stargazers) - Neo4j driver for Elixir, wrapped around the Bolt protocol. Fork of the Boltex.

## REST API

### Java

- [neo4j-ogm](https://github.com/neo4j/neo4j-ogm) [![GitHub stars](https://img.shields.io/github/stars/neo4j/neo4j-ogm?style=flat)](https://github.com/neo4j/neo4j-ogm/stargazers) - Object-Graph Mapping Library for Neo4j.
- [spring-data-neo4j](https://github.com/spring-projects/spring-data-neo4j) [![GitHub stars](https://img.shields.io/github/stars/spring-projects/spring-data-neo4j?style=flat)](https://github.com/spring-projects/spring-data-neo4j/stargazers) - Provides support to increase developer productivity in Java when using the neo4j graph database.
- [neo4j-jdbc](https://github.com/neo4j-contrib/neo4j-jdbc) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neo4j-jdbc?style=flat)](https://github.com/neo4j-contrib/neo4j-jdbc/stargazers) - Neo4j JDBC driver.
- [jcypher](https://github.com/Wolfgang-Schuetzelhofer/jcypher) [![GitHub stars](https://img.shields.io/github/stars/Wolfgang-Schuetzelhofer/jcypher?style=flat)](https://github.com/Wolfgang-Schuetzelhofer/jcypher/stargazers) - Java access to Neo4J graph databases at multiple levels of abstraction.

### Ruby

- [neo4jrb](https://github.com/neo4jrb/neo4j) [![GitHub stars](https://img.shields.io/github/stars/neo4jrb/neo4j?style=flat)](https://github.com/neo4jrb/neo4j/stargazers) - An active model wrapper for the Neo4j Graph Database for Ruby.
- [neography](https://github.com/maxdemarzi/neography) [![GitHub stars](https://img.shields.io/github/stars/maxdemarzi/neography?style=flat)](https://github.com/maxdemarzi/neography/stargazers) - A thin Ruby wrapper to the Neo4j Rest API.

### Python

- [py2neo](https://github.com/nigelsmall/py2neo) [![GitHub stars](https://img.shields.io/github/stars/nigelsmall/py2neo?style=flat)](https://github.com/nigelsmall/py2neo/stargazers) - Py2neo is a comprehensive toolkit for working with Neo4j from within Python applications or from the command line.
- [neomodel](https://github.com/neo4j-contrib/neomodel) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neomodel?style=flat)](https://github.com/neo4j-contrib/neomodel/stargazers) - An Object Graph Mapper (OGM) for the neo4j graph database, built on the awesome py2neo.

### PHP

- [Neo4j-PHP-OGM](https://github.com/graphaware/neo4j-php-ogm) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-php-ogm?style=flat)](https://github.com/graphaware/neo4j-php-ogm/stargazers) - Doctrine style Object Graph Mapper for Neo4j
- [neo4jphp](https://github.com/jadell/neo4jphp) [![GitHub stars](https://img.shields.io/github/stars/jadell/neo4jphp?style=flat)](https://github.com/jadell/neo4jphp/stargazers) - PHP wrapper of the Neo4j REST interface.
- [NeoEloquent](https://github.com/Vinelab/NeoEloquent) [![GitHub stars](https://img.shields.io/github/stars/Vinelab/NeoEloquent?style=flat)](https://github.com/Vinelab/NeoEloquent/stargazers) - A Neo4j ORM - Based on Eloquent.
- [neo4j-php-client](https://github.com/graphaware/neo4j-php-client/tree/4.0) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-php-client/tree/4.0?style=flat)](https://github.com/graphaware/neo4j-php-client/tree/4.0/stargazers) - PHP Client for Neo4j leveraging the Http and Bolt protocols.
- [Spider](https://github.com/spider/spider) [![GitHub stars](https://img.shields.io/github/stars/spider/spider?style=flat)](https://github.com/spider/spider/stargazers) - A simple, flexible, and beautiful graph-data abstraction for php.

### Other

- [node-neo4j](https://github.com/thingdom/node-neo4j) [![GitHub stars](https://img.shields.io/github/stars/thingdom/node-neo4j?style=flat)](https://github.com/thingdom/node-neo4j/stargazers) - REST API client for Node.
- [Neo4jClient](https://github.com/Readify/Neo4jClient) [![GitHub stars](https://img.shields.io/github/stars/Readify/Neo4jClient?style=flat)](https://github.com/Readify/Neo4jClient/stargazers) - .NET client binding.
- [neoism](https://github.com/jmcvetta/neoism) [![GitHub stars](https://img.shields.io/github/stars/jmcvetta/neoism?style=flat)](https://github.com/jmcvetta/neoism/stargazers) - Client for Golang.
- [neocons](https://github.com/michaelklishin/neocons) [![GitHub stars](https://img.shields.io/github/stars/michaelklishin/neocons?style=flat)](https://github.com/michaelklishin/neocons/stargazers) - A feature rich idiomatic Clojure client for the REST API.
- [RNeo4j](https://github.com/nicolewhite/RNeo4j) [![GitHub stars](https://img.shields.io/github/stars/nicolewhite/RNeo4j?style=flat)](https://github.com/nicolewhite/RNeo4j/stargazers) - Driver for R.
- [AnormCypher](https://github.com/AnormCypher/AnormCypher) [![GitHub stars](https://img.shields.io/github/stars/AnormCypher/AnormCypher?style=flat)](https://github.com/AnormCypher/AnormCypher/stargazers) - Scala library based on Anorm in the Play Framework.

# Cloud

- [GrapheneDB](https://www.graphenedb.com/) - The world's first fully managed
Neo4j graph database.
- [GraphStory](https://www.graphstory.com/) - Neo4j enterprise cloud provider

# Packages

- [Debian Packages](http://debian.neo4j.org/)
- [Yum Repo](http://yum.neo4j.org/stable/)

# Docker

- [docker-neo4j](https://github.com/neo4j/docker-neo4j) [![GitHub stars](https://img.shields.io/github/stars/neo4j/docker-neo4j?style=flat)](https://github.com/neo4j/docker-neo4j/stargazers) - Docker Images for the Neo4j Graph Database.
- [docker-neo4j-cluster](https://github.com/ekino/docker-neo4j-cluster) [![GitHub stars](https://img.shields.io/github/stars/ekino/docker-neo4j-cluster?style=flat)](https://github.com/ekino/docker-neo4j-cluster/stargazers) - Up & Running Neo4j cluster in no time.

# Full-text search

- [GraphAware Neo4j Elasticsearch Integration](https://github.com/graphaware/neo4j-to-elasticsearch) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-to-elasticsearch?style=flat)](https://github.com/graphaware/neo4j-to-elasticsearch/stargazers) - GraphAware Framework Module for Integrating Neo4j with Elasticsearch.
- [GraphAware Graph-Aided Search](https://github.com/graphaware/graph-aided-search) [![GitHub stars](https://img.shields.io/github/stars/graphaware/graph-aided-search?style=flat)](https://github.com/graphaware/graph-aided-search/stargazers) - Elasticsearch plugin offering Neo4j integration for Personalized Search.
- [neo4j-elasticsearch](https://github.com/neo4j-contrib/neo4j-elasticsearch) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neo4j-elasticsearch?style=flat)](https://github.com/neo4j-contrib/neo4j-elasticsearch/stargazers) - Neo4j ElasticSearch Integration.

# Import

- [GraphAware Neo4j Importer](https://github.com/graphaware/neo4j-importer) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-importer?style=flat)](https://github.com/graphaware/neo4j-importer/stargazers) - Java importer skeleton for complicated, business-logic-heavy high-performance Neo4j imports directly from SQL databases, CSV files, etc.
- [neo4j-csv-firehose](https://github.com/sarmbruster/neo4j-csv-firehose) [![GitHub stars](https://img.shields.io/github/stars/sarmbruster/neo4j-csv-firehose?style=flat)](https://github.com/sarmbruster/neo4j-csv-firehose/stargazers) - Enables Neo4j’s `LOAD CSV` Cypher command to load from other datasources as well.
- [neo4j-rdbms-import](https://github.com/jexp/neo4j-rdbms-import) [![GitHub stars](https://img.shields.io/github/stars/jexp/neo4j-rdbms-import?style=flat)](https://github.com/jexp/neo4j-rdbms-import/stargazers) - An automatic importer for relational databases into Neo4j.
- [Doc manager for Neo4j](https://github.com/neo4j-contrib/neo4j_doc_manager) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neo4j_doc_manager?style=flat)](https://github.com/neo4j-contrib/neo4j_doc_manager/stargazers) - The Neo4j Doc Manager takes MongoDB documents and makes it easy to query them for relationships by making them available in a Neo4j graph structure, following the format specified by Mongo Connector.
- [neoloadcsvskelgen](https://github.com/wadael/neoloadcsvskelgen) [![GitHub stars](https://img.shields.io/github/stars/wadael/neoloadcsvskelgen?style=flat)](https://github.com/wadael/neoloadcsvskelgen/stargazers) - Will output a skeleton of LOAD CSV Cypher code, from very little input (filename, separator, hints). Save time, avoid typos. 

# Benchmarking

- [neoprofiler](https://github.com/moxious/neoprofiler) [![GitHub stars](https://img.shields.io/github/stars/moxious/neoprofiler?style=flat)](https://github.com/moxious/neoprofiler/stargazers) - Neo4J database profiling utility.

# Extensions

- [GraphAware Neo4j UUID](https://github.com/graphaware/neo4j-uuid) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-uuid?style=flat)](https://github.com/graphaware/neo4j-uuid/stargazers) - GraphAware Runtime Module that assigns a UUID to all nodes in the graph transparently.
- [GraphAware Neo4j ChangeFeed](https://github.com/graphaware/neo4j-changefeed) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-changefeed?style=flat)](https://github.com/graphaware/neo4j-changefeed/stargazers) - A GraphAware Framework Runtime Module allowing users to find out what were the latest changes performed on the graph.
- [GraphAware Neo4j TimeTree](https://github.com/graphaware/neo4j-timetree) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-timetree?style=flat)](https://github.com/graphaware/neo4j-timetree/stargazers) - Java and REST APIs for working with time-representing tree in Neo4j.
- [GraphAware Neo4j Recommendation Engine](https://github.com/graphaware/neo4j-reco) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-reco?style=flat)](https://github.com/graphaware/neo4j-reco/stargazers) - Neo4j-based recommendation engine module with real-time and pre-computed recommendations.
- [GraphAware Neo4j Algorithms](https://github.com/graphaware/neo4j-algorithms) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-algorithms?style=flat)](https://github.com/graphaware/neo4j-algorithms/stargazers) - Custom graph algorithms for Neo4j with own Java and REST APIs.
- [GraphAware Neo4j Warmup](https://github.com/graphaware/neo4j-warmup) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-warmup?style=flat)](https://github.com/graphaware/neo4j-warmup/stargazers) - Simple library that warms up Neo4j caches with a single REST call.
- [GraphAware Neo4j RestTest](https://github.com/graphaware/neo4j-resttest) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-resttest?style=flat)](https://github.com/graphaware/neo4j-resttest/stargazers) - GraphAware RestTest is a simple library for testing code that talks to Neo4j running in standalone server mode.
- [GraphAware Neo4j Expire](https://github.com/graphaware/neo4j-expire) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-expire?style=flat)](https://github.com/graphaware/neo4j-expire/stargazers) - GraphAware Expire is a simple library that automatically deletes nodes and relationships from the database when they've reached their expiration date or time-to-live (TTL).
- [Spatial](https://github.com/neo4j-contrib/spatial) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/spatial?style=flat)](https://github.com/neo4j-contrib/spatial/stargazers) - Neo4j Spatial is a library of utilities for Neo4j that faciliates the enabling of spatial operations on data.
- [Graphify](https://github.com/Graphify/graphify) [![GitHub stars](https://img.shields.io/github/stars/Graphify/graphify?style=flat)](https://github.com/Graphify/graphify/stargazers) - Graphify is a Neo4j unmanaged extension used for document and text classification using graph-based hierarchical pattern recognition.
- [neo4j-tx-participation](https://github.com/jexp/neo4j-tx-participation) [![GitHub stars](https://img.shields.io/github/stars/jexp/neo4j-tx-participation?style=flat)](https://github.com/jexp/neo4j-tx-participation/stargazers) - This is a Neo4j Server Extension to make Neo4j REST-API participate in transactions started by the transactional Cypher endpoint.

# Stored Procedures

- [Apoc : Awesome Procedures on Cypher](https://github.com/neo4j-contrib/neo4j-apoc-procedures) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neo4j-apoc-procedures?style=flat)](https://github.com/neo4j-contrib/neo4j-apoc-procedures/stargazers) - Collection of useful procedures for Neo4j 3.x
- [Graphgen](https://github.com/graphaware/neo4j-graphgen-procedure) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-graphgen-procedure?style=flat)](https://github.com/graphaware/neo4j-graphgen-procedure/stargazers) - Neo4j procedure for generating test data easily with Cypher

# Development

- [Maven repositories](https://m2.neo4j.org/index.html) - Neo4j Maven repositories (releases, snapshots).
- [GraphAware Neo4j Framework](https://github.com/graphaware/neo4j-framework) [![GitHub stars](https://img.shields.io/github/stars/graphaware/neo4j-framework?style=flat)](https://github.com/graphaware/neo4j-framework/stargazers)- GraphAware Framework speeds up development with Neo4j by providing a platform for building useful generic as well as domain-specific functionality, analytical capabilities, (iterative) graph algorithms, etc.
- [cypher-dsl](https://github.com/neo4j-contrib/cypher-dsl) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/cypher-dsl?style=flat)](https://github.com/neo4j-contrib/cypher-dsl/stargazers) - A Java DSL for the Cypher Query Language and an optional Query DSL mode.
- [Liquigraph](https://github.com/liquigraph/liquigraph) [![GitHub stars](https://img.shields.io/github/stars/liquigraph/liquigraph?style=flat)](https://github.com/liquigraph/liquigraph/stargazers) - Database migrations management tool, based on how Liquibase works.
- [blueprints](https://github.com/tinkerpop/blueprints) [![GitHub stars](https://img.shields.io/github/stars/tinkerpop/blueprints?style=flat)](https://github.com/tinkerpop/blueprints/stargazers) - Blueprints is a collection of interfaces, implementations, ouplementations, and test suites for the property graph data model. Blueprints is analogous to the JDBC, but for graph databases.
- [structr](https://github.com/structr/structr) [![GitHub stars](https://img.shields.io/github/stars/structr/structr?style=flat)](https://github.com/structr/structr/stargazers) - Graph Application Platform based on Neo4j.
- [Reco4PHP](https://github.com/graphaware/reco4php) [![GitHub stars](https://img.shields.io/github/stars/graphaware/reco4php?style=flat)](https://github.com/graphaware/reco4php/stargazers) - Neo4j based Recommendation Engine Framework for PHP.

# Editors

- [jetbrains-plugin-graph-database-support](https://github.com/neueda/jetbrains-plugin-graph-database-support) [![GitHub stars](https://img.shields.io/github/stars/neueda/jetbrains-plugin-graph-database-support?style=flat)](https://github.com/neueda/jetbrains-plugin-graph-database-support/stargazers) - Graph Databases support for Jetbrains family IDE's.
- [cypher-vim-syntax](https://github.com/neo4j-contrib/cypher-vim-syntax) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/cypher-vim-syntax?style=flat)](https://github.com/neo4j-contrib/cypher-vim-syntax/stargazers) - Very basic Vim syntax for Cypher.

# Shell

- [cycli](https://github.com/nicolewhite/cycli) [![GitHub stars](https://img.shields.io/github/stars/nicolewhite/cycli?style=flat)](https://github.com/nicolewhite/cycli/stargazers) - A Command Line Interface for Cypher.
- [neo4j-shell-tools](https://github.com/jexp/neo4j-shell-tools) [![GitHub stars](https://img.shields.io/github/stars/jexp/neo4j-shell-tools?style=flat)](https://github.com/jexp/neo4j-shell-tools/stargazers) - A bunch of import/export tools for the neo4j-shell.

# Visualization

- [neoclipse](https://github.com/neo4j-contrib/neoclipse) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neoclipse?style=flat)](https://github.com/neo4j-contrib/neoclipse/stargazers) - Neoclipse is a tool to view, edit and explore Neo4j databases.
- [Gephi](https://github.com/gephi/gephi) [![GitHub stars](https://img.shields.io/github/stars/gephi/gephi?style=flat)](https://github.com/gephi/gephi/stargazers) - Gephi is an award-winning open-source platform for visualizing and manipulating large graphs.
- [Linkurious](https://linkurio.us/) - Linkurious helps search and visualize your graph data through a simple web-based interface.
- [yFiles for HTML](https://www.yworks.com/products/yfiles-for-html) - yFiles is a commercial generic graph visualization programming library that comes with [a demo to visualize your neo4j databases in JavaScript](http://live.yworks.com/demos/#neo4j). It's also the basis for the [free neo4j Graph Explorer app](https://www.yworks.com/neo4j-explorer/).

# Tools

- [Graphgen](http://graphgen.graphaware.com) - Graph Generation engine based on the Cypher DSL.
- [store-utils](https://github.com/jexp/store-utils) [![GitHub stars](https://img.shields.io/github/stars/jexp/store-utils?style=flat)](https://github.com/jexp/store-utils/stargazers) - Utilities to compact, copy, fix, analyse Neo4j stores.
- [ineo](https://github.com/cohesivestack/ineo) [![GitHub stars](https://img.shields.io/github/stars/cohesivestack/ineo?style=flat)](https://github.com/cohesivestack/ineo/stargazers)- A simple but useful Neo4j instance manager.
- [yFiles neo4j Graph Explorer](https://www.yworks.com/blog/neo4j-node-design) - A simple, free online tool to visualize your graph data and database schema.

## Learn

- [Getting Started with Neo4j](https://neo4j.com/graphacademy/online-training/getting-started-graph-databases-using-neo4j/)
- [Neo4j in Production](https://neo4j.com/graphacademy/online-training/neo4j-production/)
- [Neo4j Koans](https://github.com/jimwebber/neo4j-tutorial) [![GitHub stars](https://img.shields.io/github/stars/jimwebber/neo4j-tutorial?style=flat)](https://github.com/jimwebber/neo4j-tutorial/stargazers) - A koan-style tutorial in Java for Neo4j.

## Certification

- [Neo4j Certification](https://neo4j.com/graphacademy/neo4j-certification/) - Become a Neo4j-Certified Professional.

## Miscellaneous

- [Neo4j's Idea board](https://trello.com/b/2zFtvDnV/public-idea-board)
- [Hardware Sizing Calculator](https://neo4j.com/hardware-sizing-calculator/)

# License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Neueda R&D](https://github.com/Neueda) [![GitHub stars](https://img.shields.io/github/stars/Neueda?style=flat)](https://github.com/Neueda/stargazers) has waived all copyright and related or neighboring rights to this work.
