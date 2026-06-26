# MongoDB

[![GitHub stars](https://img.shields.io/github/stars/ramnes/awesome-mongodb?style=flat)](https://github.com/ramnes/awesome-mongodb/stargazers)

![Awesome MongoDB](logo.png)

# Awesome MongoDB [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[![Links check](https://github.com/ramnes/awesome-mongodb/actions/workflows/links.yml/badge.svg) [![GitHub stars](https://img.shields.io/github/stars/ramnes/awesome-mongodb/actions/workflows/links.yml/badge.svg?style=flat)](https://github.com/ramnes/awesome-mongodb/actions/workflows/links.yml/badge.svg/stargazers)](https://github.com/ramnes/awesome-mongodb/actions/workflows/links.yml)

> A curated list of awesome MongoDB resources, libraries, tools and applications

Inspired by the [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) list thing. Feel free to improve this list by [contributing](CONTRIBUTING.md)!

## Table of Contents
 - [Resources](#resources)
   - [Documentation](#documentation)
   - [Articles](#articles)
   - [Books](#books)
   - [Talks](#talks)
   - [Tutorials](#tutorials)
   - [More](#more)
 - [Libraries](#libraries)
   - [Ballerina](#ballerina)
   - [C](#c)
   - [C++](#c-1)
   - [C#/.NET](#cnet)
   - [D](#d)
   - [Dart](#dart)
   - [Delphi](#delphi)
   - [Elixir](#elixir)
   - [Erlang](#erlang)
   - [Go](#go)
   - [Haskell](#haskell)
   - [Java](#java)
   - [JavaScript](#javascript)
   - [Kotlin](#kotlin)
   - [Lisp](#lisp)
   - [OCaml](#ocaml)
   - [PHP](#php)
   - [PowerShell](#powershell)
   - [Python](#python)
   - [R](#r)
   - [Ruby](#ruby)
   - [Rust](#rust)
   - [Scala](#scala)
   - [Smalltalk](#smalltalk)
   - [Swift](#swift)
 - [Tools](#tools)
   - [Administration](#administration)
   - [Data](#data)
   - [Deployment](#deployment)
   - [Desktop](#desktop)
   - [Development](#development)
   - [Monitoring](#monitoring)
   - [Low-Code](#low-code)
   - [Shell](#shell)
   - [Web](#web)
 - [Applications](#applications)

## Resources
### Documentation
 - [MongoDB Server Introduction](https://www.mongodb.com/docs/manual/introduction/)
 - [MongoDB Server Documentation](https://www.mongodb.com/docs/manual/)
 - [MongoDB Tutorials](https://www.mongodb.com/docs/manual/tutorial/)
 - [MongoDB Guides](https://www.mongodb.com/docs/guides/)
 - [MongoDB Driver Documentation](https://www.mongodb.com/docs/drivers/)
 - [MongoDB Connectors](https://www.mongodb.com/connectors/)

### Articles

 - [14 Things I Wish I'd Known When Starting with MongoDB (Phil Factor)](https://www.infoq.com/articles/Starting-With-MongoDB/)
 - [A Custom WordPress Dashboard with MongoDB Atlas, Microsoft Azure, & Serverless Functions (Ahmad Awais)](https://ahmadawais.com/wordpress-mongodb-atlas-microsoft-azure-serverless-functions/)
 - [Building with Patterns](https://www.mongodb.com/blog/post/building-with-patterns-a-summary) - Series of articles regarding MongoDB Design Patterns and common use case of each Design Pattern with real world examples.
 - [Five Things About Scaling MongoDB (A. Jesse Jiryu Davis, MongoDB Inc.)](https://emptysqua.re/blog/five-things/) - Scale 101
 - [Optimizing MongoDB Compound Indexes (A. Jesse Jiryu Davis, MongoDB Inc.)](https://emptysqua.re/blog/optimizing-mongodb-compound-indexes/) - Everything you need/have to know about indexes
 - [Server Discovery And Monitoring In PyMongo, Perl, And C (A. Jesse Jiryu Davis, MongoDB Inc.) ](https://emptysqua.re/blog/server-discovery-and-monitoring-in-pymongo-perl-and-c/)
 - [Monitoring MongoDB performance metrics (Jean-Mathieu Saponaro, Datadog)](https://www.datadoghq.com/blog/monitoring-mongodb-performance-metrics-wiredtiger/)
 - [Tuning MongoDB performance for production systems (Marek Trunkat, Apify)](https://blog.apify.com/tuning-mongodb-performance/) - The techniques and MongoDB Cloud features to debug performance issues and expose sub-optimal queries

### Books
 - [50 Tips and Tricks for MongoDB Developers](https://www.oreilly.com/library/view/50-tips-and/9781449306779/) - Advanced MongoDB tips and tricks, given by a MongoDB inc. engineer
 - [MongoDB Applied Design Patterns (Rick Copeland)](https://www.oreilly.com/library/view/mongodb-applied-design/9781449340056/)
 - [MongoDB in Action, Third Edition (Arek Borucki)](https://www.manning.com/books/mongodb-in-action-third-edition)
 - [Practical MongoDB Aggregations E-Book](https://www.practical-mongodb-aggregations.com/) - Free e-book: How to develop effective and optimal data manipulation and analytics pipelines
 - [The Little MongoDB Book](https://github.com/mongodb-developer/the-little-mongodb-book) [![GitHub stars](https://img.shields.io/github/stars/mongodb-developer/the-little-mongodb-book?style=flat)](https://github.com/mongodb-developer/the-little-mongodb-book/stargazers) - Basic introduction

### Talks
 - [MongoDB Schema Design (Tugdual Grall, MongoDB Inc.)](https://www.youtube.com/watch?v=csKBT8zkRf0) [47']
 - [Partial and Fuzzy Matching with MongoDB (John Page, MongoDB Inc.)](https://www.youtube.com/watch?v=hXbLHInH5qU) [35']
 - [Scaling MongoDB on Amazon Web Services (Michael Saffitz, Apptentive)](https://www.youtube.com/watch?v=bkjVhEQocFI) [50']

### Tutorials
 - [Deploy a Highly-Available MongoDB Replica Set on AWS](https://eladnava.com/deploy-a-highly-available-mongodb-replica-set-on-aws/)
 - [Sharded Cluster with Docker Compose](https://github.com/minhhungit/mongodb-cluster-docker-compose) [![GitHub stars](https://img.shields.io/github/stars/minhhungit/mongodb-cluster-docker-compose?style=flat)](https://github.com/minhhungit/mongodb-cluster-docker-compose/stargazers)

### More
 - [MongoDB source code](https://github.com/mongodb/mongo) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo?style=flat)](https://github.com/mongodb/mongo/stargazers)
 - [MongoDB University](https://learn.mongodb.com/) - Certifications and free online courses
 - [MongoDB 101 by Academy 3T](https://studio3t.com/academy/) - Free and self-paced MongoDB courses for beginners

## Libraries

### Ballerina
 - [ballerina-mongodb](https://github.com/ballerina-platform/module-ballerinax-mongodb) [![GitHub stars](https://img.shields.io/github/stars/ballerina-platform/module-ballerinax-mongodb?style=flat)](https://github.com/ballerina-platform/module-ballerinax-mongodb/stargazers) - Official Ballerina driver

### C
 - [mongo-c-driver](https://github.com/mongodb/mongo-c-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-c-driver?style=flat)](https://github.com/mongodb/mongo-c-driver/stargazers) - Official C driver

### C++
 - [mongo-cxx-driver](https://github.com/mongodb/mongo-cxx-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-cxx-driver?style=flat)](https://github.com/mongodb/mongo-cxx-driver/stargazers) - Official C++ driver

### C#/.NET ###
 - [mongo-csharp-driver](https://github.com/mongodb/mongo-csharp-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-csharp-driver?style=flat)](https://github.com/mongodb/mongo-csharp-driver/stargazers) - Official C# driver
 - [mongo-efcore-provider](https://github.com/mongodb/mongo-efcore-provider) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-efcore-provider?style=flat)](https://github.com/mongodb/mongo-efcore-provider/stargazers) - Official Entity Framework (EF) Core provider for MongoDB
 - [MongoRepository](https://github.com/RobThree/MongoRepository) [![GitHub stars](https://img.shields.io/github/stars/RobThree/MongoRepository?style=flat)](https://github.com/RobThree/MongoRepository/stargazers) - Repository abstraction layer on top of the C# driver

### D
 - [vibe.d](https://vibed.org/docs#mongo) - D web framework shipping with a MongoDB driver

### Dart
 - [mongo_dart](https://github.com/mongo-dart/mongo_dart) [![GitHub stars](https://img.shields.io/github/stars/mongo-dart/mongo_dart?style=flat)](https://github.com/mongo-dart/mongo_dart/stargazers) - Community Dart driver

### Delphi
 - [Alcinoe](https://github.com/MagicFoundation/Alcinoe) [![GitHub stars](https://img.shields.io/github/stars/MagicFoundation/Alcinoe?style=flat)](https://github.com/MagicFoundation/Alcinoe/stargazers) - Library for Delphi that includes a MongoDB client
 - [TMongoWire](https://github.com/stijnsanders/TMongoWire) [![GitHub stars](https://img.shields.io/github/stars/stijnsanders/TMongoWire?style=flat)](https://github.com/stijnsanders/TMongoWire/stargazers) - Minimal community Delphi driver

### Elixir
 - [elixir-mongodb-driver](https://github.com/zookzook/elixir-mongodb-driver) [![GitHub stars](https://img.shields.io/github/stars/zookzook/elixir-mongodb-driver?style=flat)](https://github.com/zookzook/elixir-mongodb-driver/stargazers) - Community Elixir driver
 - [mongodb](https://github.com/kobil-systems/mongodb) [![GitHub stars](https://img.shields.io/github/stars/kobil-systems/mongodb?style=flat)](https://github.com/kobil-systems/mongodb/stargazers) - Community Elixir driver
 - [mongodb_ecto](https://github.com/kobil-systems/mongodb_ecto) [![GitHub stars](https://img.shields.io/github/stars/kobil-systems/mongodb_ecto?style=flat)](https://github.com/kobil-systems/mongodb_ecto/stargazers) - Adapter for the Ecto database wrapper

### Erlang
 - [mongodb-erlang](https://github.com/comtihon/mongodb-erlang) [![GitHub stars](https://img.shields.io/github/stars/comtihon/mongodb-erlang?style=flat)](https://github.com/comtihon/mongodb-erlang/stargazers) - Community Erlang driver

### Go
 - [Bongo](https://github.com/go-bongo/bongo) [![GitHub stars](https://img.shields.io/github/stars/go-bongo/bongo?style=flat)](https://github.com/go-bongo/bongo/stargazers) - ODM based on mgo
 - [bsonic](https://github.com/kyle-williams-1/bsonic) [![GitHub stars](https://img.shields.io/github/stars/kyle-williams-1/bsonic?style=flat)](https://github.com/kyle-williams-1/bsonic/stargazers) - Parse Lucene-style query syntax into BSON filters for MongoDB
 - [mgo](https://github.com/globalsign/mgo) [![GitHub stars](https://img.shields.io/github/stars/globalsign/mgo?style=flat)](https://github.com/globalsign/mgo/stargazers) - Community Go driver
 - [mongo-go-driver](https://github.com/mongodb/mongo-go-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-go-driver?style=flat)](https://github.com/mongodb/mongo-go-driver/stargazers) - Official Go driver

### Haskell
 - [mongodb](https://github.com/mongodb-haskell/mongodb/) [![GitHub stars](https://img.shields.io/github/stars/mongodb-haskell/mongodb/?style=flat)](https://github.com/mongodb-haskell/mongodb//stargazers) - Community Haskell driver

### Java
 - [Jongo](https://github.com/bguerout/jongo) [![GitHub stars](https://img.shields.io/github/stars/bguerout/jongo?style=flat)](https://github.com/bguerout/jongo/stargazers) - Query in Java as in Mongo shell
 - [Hibernate OGM](https://github.com/hibernate/hibernate-ogm) [![GitHub stars](https://img.shields.io/github/stars/hibernate/hibernate-ogm?style=flat)](https://github.com/hibernate/hibernate-ogm/stargazers) - The power and simplicity of JPA for NoSQL datastores
 - [mongo-java-driver](https://github.com/mongodb/mongo-java-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-java-driver?style=flat)](https://github.com/mongodb/mongo-java-driver/stargazers) - Official Java driver
 - [Mongojack](https://github.com/mongojack/mongojack) [![GitHub stars](https://img.shields.io/github/stars/mongojack/mongojack?style=flat)](https://github.com/mongojack/mongojack/stargazers) - Based on Jackson, allows you to easily handle your mongo objects as POJOs
 - [Morphia](https://github.com/MorphiaOrg/morphia) [![GitHub stars](https://img.shields.io/github/stars/MorphiaOrg/morphia?style=flat)](https://github.com/MorphiaOrg/morphia/stargazers) - Java ODM
 - [Morphium](https://github.com/sboesebeck/morphium) [![GitHub stars](https://img.shields.io/github/stars/sboesebeck/morphium?style=flat)](https://github.com/sboesebeck/morphium/stargazers) - Java ODM and caching layer
 - [Spring Data MongoDB](https://github.com/spring-projects/spring-data-mongodb) [![GitHub stars](https://img.shields.io/github/stars/spring-projects/spring-data-mongodb?style=flat)](https://github.com/spring-projects/spring-data-mongodb/stargazers) - Spring based, object-document support and repositories

### JavaScript
 - [Camo](https://github.com/scottwrobinson/camo) [![GitHub stars](https://img.shields.io/github/stars/scottwrobinson/camo?style=flat)](https://github.com/scottwrobinson/camo/stargazers) - Class-based ES6 ODM for Mongo-like databases
 - [connect-mongo](https://github.com/jdesboeufs/connect-mongo) [![GitHub stars](https://img.shields.io/github/stars/jdesboeufs/connect-mongo?style=flat)](https://github.com/jdesboeufs/connect-mongo/stargazers) - MongoDB session store for Connect and Express written in Typescript.
 - [deno_mongo](https://github.com/denodrivers/mongo) [![GitHub stars](https://img.shields.io/github/stars/denodrivers/mongo?style=flat)](https://github.com/denodrivers/mongo/stargazers) - Community Deno driver
 - [MEAN.JS](https://github.com/meanjs/mean) [![GitHub stars](https://img.shields.io/github/stars/meanjs/mean?style=flat)](https://github.com/meanjs/mean/stargazers) - Full stack based on MongoDB, Express, AngularJS, and Node.js
 - [MERN (mern-starter)](https://github.com/Hashnode/mern-starter) [![GitHub stars](https://img.shields.io/github/stars/Hashnode/mern-starter?style=flat)](https://github.com/Hashnode/mern-starter/stargazers) - Full stack based on MongoDB, Express, React and Node.js
 - [Meteor](https://github.com/meteor/meteor) [![GitHub stars](https://img.shields.io/github/stars/meteor/meteor?style=flat)](https://github.com/meteor/meteor/stargazers) - Real-time/reactive client-server framework based on MongoDB, with lots of features
 - [Monarch ORM](https://github.com/monarch-orm/monarch) [![GitHub stars](https://img.shields.io/github/stars/monarch-orm/monarch?style=flat)](https://github.com/monarch-orm/monarch/stargazers) - Type-safe ODM for MongoDB with complete type inference
 - [MongoMQ2](https://github.com/morris/mongomq2) [![GitHub stars](https://img.shields.io/github/stars/morris/mongomq2?style=flat)](https://github.com/morris/mongomq2/stargazers) - A general-purpose message and event queuing library for MongoDB
 - [Mongoose](https://github.com/Automattic/mongoose) [![GitHub stars](https://img.shields.io/github/stars/Automattic/mongoose?style=flat)](https://github.com/Automattic/mongoose/stargazers) - Node.js asynchronous ODM
 - [CASL Mongoose](https://github.com/stalniy/casl/tree/master/packages/casl-mongoose) [![GitHub stars](https://img.shields.io/github/stars/stalniy/casl/tree/master/packages/casl-mongoose?style=flat)](https://github.com/stalniy/casl/tree/master/packages/casl-mongoose/stargazers) - Permissions management library integrated with Mongoose
 - [mongration](https://github.com/awapps/mongration) [![GitHub stars](https://img.shields.io/github/stars/awapps/mongration?style=flat)](https://github.com/awapps/mongration/stargazers) - Node.js migration framework
 - [Neuledge](https://github.com/neuledge/engine-js) [![GitHub stars](https://img.shields.io/github/stars/neuledge/engine-js?style=flat)](https://github.com/neuledge/engine-js/stargazers) - Universal schema-based ORM with multi-state representation for entities
 - [node-mongodb-native](https://github.com/mongodb/node-mongodb-native) [![GitHub stars](https://img.shields.io/github/stars/mongodb/node-mongodb-native?style=flat)](https://github.com/mongodb/node-mongodb-native/stargazers) - Official Node.js driver
 - [Typegoose](https://github.com/typegoose/typegoose) [![GitHub stars](https://img.shields.io/github/stars/typegoose/typegoose?style=flat)](https://github.com/typegoose/typegoose/stargazers) - Define Mongoose models using TypeScript classes

### Kotlin
- [driver-kotlin-coroutine](https://github.com/mongodb/mongo-java-driver/tree/master/driver-kotlin-coroutine) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-java-driver/tree/master/driver-kotlin-coroutine?style=flat)](https://github.com/mongodb/mongo-java-driver/tree/master/driver-kotlin-coroutine/stargazers) - Official Kotlin driver
- [kmongo](https://github.com/Litote/kmongo) [![GitHub stars](https://img.shields.io/github/stars/Litote/kmongo?style=flat)](https://github.com/Litote/kmongo/stargazers) - Kotlin toolkit based on the Java driver

### Lisp
 - [cl-mongo](https://github.com/fons/cl-mongo) [![GitHub stars](https://img.shields.io/github/stars/fons/cl-mongo?style=flat)](https://github.com/fons/cl-mongo/stargazers) - Community Common Lisp interface

### OCaml
 - [Mongo.ml](http://massd.github.io/mongo/) - Community OCaml driver

### PHP
 - [laravel-mongodb](https://github.com/mongodb/laravel-mongodb) [![GitHub stars](https://img.shields.io/github/stars/mongodb/laravel-mongodb?style=flat)](https://github.com/mongodb/laravel-mongodb/stargazers) - Official Eloquent model and query builder for Laravel
 - [PHP Driver](https://github.com/mongodb/mongo-php-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-php-driver?style=flat)](https://github.com/mongodb/mongo-php-driver/stargazers) - Official PHP driver
 - [Doctrine MongoDB ODM](https://github.com/doctrine/mongodb-odm) [![GitHub stars](https://img.shields.io/github/stars/doctrine/mongodb-odm?style=flat)](https://github.com/doctrine/mongodb-odm/stargazers) and [MongoDB ODM Bundle for Symfony](https://github.com/doctrine/DoctrineMongoDBBundle) [![GitHub stars](https://img.shields.io/github/stars/doctrine/DoctrineMongoDBBundle?style=flat)](https://github.com/doctrine/DoctrineMongoDBBundle/stargazers) - Fully featured ORM with Symfony integration
 - [MongoDB Bundle](https://github.com/facile-it/mongodb-bundle) [![GitHub stars](https://img.shields.io/github/stars/facile-it/mongodb-bundle?style=flat)](https://github.com/facile-it/mongodb-bundle/stargazers) - Integration of the official library with Symfony, without ORM
 - [yii-mongodb](https://github.com/yiisoft/yii2-mongodb) [![GitHub stars](https://img.shields.io/github/stars/yiisoft/yii2-mongodb?style=flat)](https://github.com/yiisoft/yii2-mongodb/stargazers) - Yii 2 MongoDB extension
 - [opentelemetry php auto-mongodb](https://github.com/opentelemetry-php/contrib-auto-mongodb) [![GitHub stars](https://img.shields.io/github/stars/opentelemetry-php/contrib-auto-mongodb?style=flat)](https://github.com/opentelemetry-php/contrib-auto-mongodb/stargazers) - Automatic monitoring of MongoDB commands with OpenTelemetry
 - [mongo-php-adapter](https://github.com/alcaeus/mongo-php-adapter) [![GitHub stars](https://img.shields.io/github/stars/alcaeus/mongo-php-adapter?style=flat)](https://github.com/alcaeus/mongo-php-adapter/stargazers) - Adapter for applications using `ext-mongo`

### PowerShell
 - [Mdbc](https://github.com/nightroman/Mdbc) [![GitHub stars](https://img.shields.io/github/stars/nightroman/Mdbc?style=flat)](https://github.com/nightroman/Mdbc/stargazers) - MongoDB cmdlets for PowerShell

### Python
 - [AtlasQ](https://github.com/certego/AtlasQ) [![GitHub stars](https://img.shields.io/github/stars/certego/AtlasQ?style=flat)](https://github.com/certego/AtlasQ/stargazers) - MongoDB Atlas Search wrapper with MongoEngine syntax
 - [Beanie](https://github.com/roman-right/beanie) [![GitHub stars](https://img.shields.io/github/stars/roman-right/beanie?style=flat)](https://github.com/roman-right/beanie/stargazers) - Asynchronous ODM based on [Motor](https://motor.readthedocs.io/en/stable/) and [Pydantic](https://pydantic-docs.helpmanual.io/), which supports migrations out of the box
 - [Djongo](https://github.com/nesdis/djongo) [![GitHub stars](https://img.shields.io/github/stars/nesdis/djongo?style=flat)](https://github.com/nesdis/djongo/stargazers) - MongoDB connector for Django compatible with Django ORM
 - [Mongo-Thingy](https://github.com/numberly/mongo-thingy) [![GitHub stars](https://img.shields.io/github/stars/numberly/mongo-thingy?style=flat)](https://github.com/numberly/mongo-thingy/stargazers) - Powerful schema-less ODM for MongoDB and Python (sync + async)
 - [MongoEngine](https://github.com/MongoEngine/mongoengine) [![GitHub stars](https://img.shields.io/github/stars/MongoEngine/mongoengine?style=flat)](https://github.com/MongoEngine/mongoengine/stargazers) - ODM on top of PyMongo
 - [Motor](https://github.com/mongodb/motor) [![GitHub stars](https://img.shields.io/github/stars/mongodb/motor?style=flat)](https://github.com/mongodb/motor/stargazers) - Official non-blocking Python driver for Tornado or asyncio
 - [PyMongo](https://github.com/mongodb/mongo-python-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-python-driver?style=flat)](https://github.com/mongodb/mongo-python-driver/stargazers) - Official Python driver
 - [ODMantic](https://github.com/art049/odmantic) [![GitHub stars](https://img.shields.io/github/stars/art049/odmantic?style=flat)](https://github.com/art049/odmantic/stargazers) - Asynchronous ODM on top of pydantic
 - [TxMongo](https://github.com/twisted/txmongo) [![GitHub stars](https://img.shields.io/github/stars/twisted/txmongo?style=flat)](https://github.com/twisted/txmongo/stargazers) - Twisted's MongoDB driver

### R
 - [mongolite](https://github.com/jeroen/mongolite) [![GitHub stars](https://img.shields.io/github/stars/jeroen/mongolite?style=flat)](https://github.com/jeroen/mongolite/stargazers) - Fast and simple client for R
 - [mdbplyr](https://github.com/pbosetti/mdbplyr) [![GitHub stars](https://img.shields.io/github/stars/pbosetti/mdbplyr?style=flat)](https://github.com/pbosetti/mdbplyr/stargazers) - Build MongoDB queries and aggregations as if you were using `dplyr`, no more head-crushing JSON fights!

### Ruby
 - [mongo-ruby-driver](https://github.com/mongodb/mongo-ruby-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-ruby-driver?style=flat)](https://github.com/mongodb/mongo-ruby-driver/stargazers) - Official Ruby driver
 - [Mongoid](https://github.com/mongodb/mongoid) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongoid?style=flat)](https://github.com/mongodb/mongoid/stargazers) - ODM framework

### Rust
 - [mongodb-rust-driver](https://github.com/mongodb/mongo-rust-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-rust-driver?style=flat)](https://github.com/mongodb/mongo-rust-driver/stargazers) - Official Rust driver

### Scala
 - [driver-scala](https://github.com/mongodb/mongo-java-driver/tree/master/driver-scala) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-java-driver/tree/master/driver-scala?style=flat)](https://github.com/mongodb/mongo-java-driver/tree/master/driver-scala/stargazers) - Official Scala driver
 - [ReactiveMongo](https://github.com/ReactiveMongo/ReactiveMongo) [![GitHub stars](https://img.shields.io/github/stars/ReactiveMongo/ReactiveMongo?style=flat)](https://github.com/ReactiveMongo/ReactiveMongo/stargazers) - Non-blocking Scala driver
 - [Spark-MongoDB](https://github.com/Stratio/Spark-MongoDB) [![GitHub stars](https://img.shields.io/github/stars/Stratio/Spark-MongoDB?style=flat)](https://github.com/Stratio/Spark-MongoDB/stargazers) - Read/write data with Spark SQL

### Smalltalk
 - [MongoTalk](https://github.com/pharo-nosql/mongotalk) [![GitHub stars](https://img.shields.io/github/stars/pharo-nosql/mongotalk?style=flat)](https://github.com/pharo-nosql/mongotalk/stargazers) - Community Smalltalk driver

### Swift
 - [MongoSwift](https://github.com/mongodb/mongo-swift-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-swift-driver?style=flat)](https://github.com/mongodb/mongo-swift-driver/stargazers) - Official MongoDB Swift driver (discontinued)
 - [MongoKitten](https://github.com/orlandos-nl/MongoKitten) [![GitHub stars](https://img.shields.io/github/stars/orlandos-nl/MongoKitten?style=flat)](https://github.com/orlandos-nl/MongoKitten/stargazers) - Community asynchronous Swift driver

## Tools
### Administration
 - [mgob](https://github.com/stefanprodan/mgob) [![GitHub stars](https://img.shields.io/github/stars/stefanprodan/mgob?style=flat)](https://github.com/stefanprodan/mgob/stargazers) - Full-featured MongoDB dockerized backup agent
 - [mongoctl](https://github.com/mongolab/mongoctl) [![GitHub stars](https://img.shields.io/github/stars/mongolab/mongoctl?style=flat)](https://github.com/mongolab/mongoctl/stargazers) - Manage MongoDB servers and replica sets using JSON configurations
 - [mongodb-tools](https://github.com/jwilder/mongodb-tools) [![GitHub stars](https://img.shields.io/github/stars/jwilder/mongodb-tools?style=flat)](https://github.com/jwilder/mongodb-tools/stargazers) - Three neat Python scripts to work with collections and indexes
 - [mtools](https://github.com/rueckstiess/mtools) [![GitHub stars](https://img.shields.io/github/stars/rueckstiess/mtools?style=flat)](https://github.com/rueckstiess/mtools/stargazers) - Collection of scripts to set up test environments and visualize log files
 - [nginx-gridfs](https://github.com/mdirolf/nginx-gridfs) [![GitHub stars](https://img.shields.io/github/stars/mdirolf/nginx-gridfs?style=flat)](https://github.com/mdirolf/nginx-gridfs/stargazers) - Nginx module for serving files from GridFS
 - [pt-mongodb-query-digest](https://www.percona.com/doc/percona-toolkit/LATEST/pt-mongodb-query-digest.html) - Aggregates queries from query profiler and reports query usage statistics
 - [pt-mongodb-summary](https://www.percona.com/doc/percona-toolkit/LATEST/pt-mongodb-summary.html) - MongoDB cluster status overview command line tool

Services:
 - [MongoDB Atlas](https://www.mongodb.com/products/platform) - MongoDB Inc. DBaaS offer (works with AWS, Azure, or GCP)
 - [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager) - MongoDB Inc. databases management offer
 - [ObjectRocket](https://www.objectrocket.com/) - Rackspace DBaaS offer (has other database types too)
 - [Scalegrid](https://scalegrid.io) - Fully managed DBaaS (with option to bring your own Azure/AWS account)

### Data
 - [mongo-connector](https://github.com/yougov/mongo-connector) [![GitHub stars](https://img.shields.io/github/stars/yougov/mongo-connector?style=flat)](https://github.com/yougov/mongo-connector/stargazers) - Streaming replication to Elasticsearch, Solr, or MongoDB
 - [mongo_fdw](https://github.com/EnterpriseDB/mongo_fdw) [![GitHub stars](https://img.shields.io/github/stars/EnterpriseDB/mongo_fdw?style=flat)](https://github.com/EnterpriseDB/mongo_fdw/stargazers) - PostgreSQL foreign data wrapper
 - [mongo-hadoop](https://github.com/mongodb/mongo-hadoop) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-hadoop?style=flat)](https://github.com/mongodb/mongo-hadoop/stargazers) - Hadoop connector
 - [Mongolastic](https://github.com/ozlerhakan/mongolastic) [![GitHub stars](https://img.shields.io/github/stars/ozlerhakan/mongolastic?style=flat)](https://github.com/ozlerhakan/mongolastic/stargazers) - MongoDB to Elasticsearch (and vice-versa) migration tool

Services:
 - [Cluster to cluster sync](https://www.mongodb.com/products/cluster-to-cluster-sync) - MongoDB Inc. solution for continuous data sync between separate clusters

### Deployment
 - [ansible-role-mongodb](https://github.com/UnderGreen/ansible-role-mongodb) [![GitHub stars](https://img.shields.io/github/stars/UnderGreen/ansible-role-mongodb?style=flat)](https://github.com/UnderGreen/ansible-role-mongodb/stargazers) - Ansible role
 - [chef-mongodb](https://github.com/edelight/chef-mongodb) [![GitHub stars](https://img.shields.io/github/stars/edelight/chef-mongodb?style=flat)](https://github.com/edelight/chef-mongodb/stargazers) - Chef cookbook
 - [DockerHub Official Docker Image](https://hub.docker.com/_/mongo/)
 - [Helm Chart](https://github.com/helm/charts/tree/master/stable/mongodb) [![GitHub stars](https://img.shields.io/github/stars/helm/charts/tree/master/stable/mongodb?style=flat)](https://github.com/helm/charts/tree/master/stable/mongodb/stargazers)
 - [puppet-mongodb](https://github.com/voxpupuli/puppet-mongodb) [![GitHub stars](https://img.shields.io/github/stars/voxpupuli/puppet-mongodb?style=flat)](https://github.com/voxpupuli/puppet-mongodb/stargazers) - Puppet module (formerly puppetlabs-mongodb)

### Desktop
 - [Compass](https://github.com/mongodb-js/compass) [![GitHub stars](https://img.shields.io/github/stars/mongodb-js/compass?style=flat)](https://github.com/mongodb-js/compass/stargazers) - Free Cross-platform GUI from MongoDB
 - [DocKit](https://github.com/geek-fun/dockit) [![GitHub stars](https://img.shields.io/github/stars/geek-fun/dockit?style=flat)](https://github.com/geek-fun/dockit/stargazers) - Open-source MongoDB GUI client with built-in Data AI Agent for natural language queries, collection management, and import/export. Cross-platform (Tauri + Vue 3).
 - [MongoDB for VS Code](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode) - Connect to MongoDB and prototype queries from VS Code
 - [MongoDB MCP Server](https://github.com/mongodb-js/mongodb-mcp-server) [![GitHub stars](https://img.shields.io/github/stars/mongodb-js/mongodb-mcp-server?style=flat)](https://github.com/mongodb-js/mongodb-mcp-server/stargazers) - Official Model Context Protocol server for interacting with MongoDB databases and MongoDB Atlas
 - [MongoHub](https://github.com/jeromelebel/MongoHub-Mac) [![GitHub stars](https://img.shields.io/github/stars/jeromelebel/MongoHub-Mac?style=flat)](https://github.com/jeromelebel/MongoHub-Mac/stargazers) - Mac native client
 - [MQLens](https://github.com/mqlens/mqlens-mongodb) [![GitHub stars](https://img.shields.io/github/stars/mqlens/mqlens-mongodb?style=flat)](https://github.com/mqlens/mqlens-mongodb/stargazers) - Free, native, cross-platform GUI with all auth modes, TLS/SSH/SOCKS5, aggregation explain plans, schema analysis, GridFS, embedded mongosh and an optional AI query assistant; encrypted credentials, zero telemetry
 - [WebDB](https://github.com/WebDB-App/app) [![GitHub stars](https://img.shields.io/github/stars/WebDB-App/app?style=flat)](https://github.com/WebDB-App/app/stargazers) – Web-based and open-source "efficient database IDE". Provides ERDs, data generators, an AI assistant, a NoSQL structure manager, a time machine, auto-completion and more

Services:
 - [DataGrip](https://www.jetbrains.com/datagrip/) - Cross-platform JetBrains' IDE
 - [Mingo](https://mingo.io/) - MongoDB Admin. Intuitive UI. Fast. Reliable
 - [Monghoul](https://www.monghoul.com/) - MongoDB GUI with smart autocomplete, visual aggregation builder, and built-in MCP server
 - [Moon Modeler](https://www.datensen.com/) - Data modeling tool for MongoDB and relational databases
 - [NoSQLBooster](https://nosqlbooster.com) - Feature-rich but easy-to-use cross-platform IDE (formerly MongoBooster)
 - [Studio 3T](https://studio3t.com/) - Cross-platform GUI, stable and powerful (formerly MongoChef and Robo 3T)
 - [TablePlus](https://tableplus.com/) - Native, lightweight GUI on macOS
 - [VisuaLeaf](https://visualeaf.com/) - MongoDB GUI designed for speed, clarity, and effortless data exploration

### Development
 - [C# Analyzer](https://github.com/mongodb/mongo-csharp-analyzer) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-csharp-analyzer?style=flat)](https://github.com/mongodb/mongo-csharp-analyzer/stargazers) - View the MongoDB Query API equivalents of your builder expressions in Visual Studio
 - [mgodatagen](https://github.com/feliixx/mgodatagen) [![GitHub stars](https://img.shields.io/github/stars/feliixx/mgodatagen?style=flat)](https://github.com/feliixx/mgodatagen/stargazers) - Random data generator
 - [migrate-mongo](https://github.com/seppevs/migrate-mongo) [![GitHub stars](https://img.shields.io/github/stars/seppevs/migrate-mongo?style=flat)](https://github.com/seppevs/migrate-mongo/stargazers) - Database migration tool
 - [Mongo Playground](https://github.com/feliixx/mongoplayground) [![GitHub stars](https://img.shields.io/github/stars/feliixx/mongoplayground?style=flat)](https://github.com/feliixx/mongoplayground/stargazers) - Online query playground
 - [Mongo Seeding](https://github.com/pkosiec/mongo-seeding) [![GitHub stars](https://img.shields.io/github/stars/pkosiec/mongo-seeding?style=flat)](https://github.com/pkosiec/mongo-seeding/stargazers) - Node.js library, CLI and Docker image for populating databases using JS and JSON files
 - [Mongoeye](https://github.com/mongoeye/mongoeye) [![GitHub stars](https://img.shields.io/github/stars/mongoeye/mongoeye?style=flat)](https://github.com/mongoeye/mongoeye/stargazers) - Schema and data analyzer: explore data in your collections
 - [sql-to-mongo-db-query-converter](https://github.com/vincentrussell/sql-to-mongo-db-query-converter) [![GitHub stars](https://img.shields.io/github/stars/vincentrussell/sql-to-mongo-db-query-converter?style=flat)](https://github.com/vincentrussell/sql-to-mongo-db-query-converter/stargazers) - Query converter from SQL to MongoDB
 - [Variety](https://github.com/variety/variety) [![GitHub stars](https://img.shields.io/github/stars/variety/variety?style=flat)](https://github.com/variety/variety/stargazers) - Schema analyzer: see what fields are in your collection and what's their content
 - [VS Code Extension](https://github.com/mongodb-js/vscode) [![GitHub stars](https://img.shields.io/github/stars/mongodb-js/vscode?style=flat)](https://github.com/mongodb-js/vscode/stargazers)

Services:
 - [MongoDB Atlas App Services](https://www.mongodb.com/atlas/app-services) - MongoDB Inc. solution to run code without the operational overhead
 - [MongoDB Realm](https://www.mongodb.com/realm) - MongoDB Inc. solution for mobile data sync

### Monitoring
 - [mongo-munin](https://github.com/erh/mongo-munin) [![GitHub stars](https://img.shields.io/github/stars/erh/mongo-munin?style=flat)](https://github.com/erh/mongo-munin/stargazers) - Collection of Munin plugins
 - [nagios-plugin-mongodb](https://github.com/mzupan/nagios-plugin-mongodb) [![GitHub stars](https://img.shields.io/github/stars/mzupan/nagios-plugin-mongodb?style=flat)](https://github.com/mzupan/nagios-plugin-mongodb/stargazers) - Nagios plugin (in Python)
 - [Percona Monitoring and Management](https://github.com/percona/pmm) [![GitHub stars](https://img.shields.io/github/stars/percona/pmm?style=flat)](https://github.com/percona/pmm/stargazers) - Free and open-source platform for managing and monitoring databases performances
 - [mongotail](https://github.com/mrsarm/mongotail) [![GitHub stars](https://img.shields.io/github/stars/mrsarm/mongotail?style=flat)](https://github.com/mrsarm/mongotail/stargazers) - Log all MongoDB queries in a "tail"able way

Services:

 - [Datadog](https://www.datadoghq.com/blog/monitor-mongodb-performance-with-datadog/) - SaaS-based monitoring
 - [Solarwindws Database Performance Monitor](https://www.solarwinds.com/database-performance-monitor) - SaaS-based query performance analytics and monitoring

### Low-Code

> 💡 These tools are not necessarily made for MongoDB in particular, but support it.

 - [Appsmith](https://github.com/appsmithorg/appsmith) [![GitHub stars](https://img.shields.io/github/stars/appsmithorg/appsmith?style=flat)](https://github.com/appsmithorg/appsmith/stargazers) - Open-source Retool alternative
 - [Appwrite](https://github.com/appwrite/appwrite) [![GitHub stars](https://img.shields.io/github/stars/appwrite/appwrite?style=flat)](https://github.com/appwrite/appwrite/stargazers) - Open-source Firebase alternative
 - [Budibase](https://github.com/Budibase/budibase) [![GitHub stars](https://img.shields.io/github/stars/Budibase/budibase?style=flat)](https://github.com/Budibase/budibase/stargazers) - Open-source Retool alternative
 - [ILLA Builder](https://github.com/illacloud/illa-builder) [![GitHub stars](https://img.shields.io/github/stars/illacloud/illa-builder?style=flat)](https://github.com/illacloud/illa-builder/stargazers) - Open-source Retool alternative
 - [Tooljet](https://github.com/ToolJet/ToolJet) [![GitHub stars](https://img.shields.io/github/stars/ToolJet/ToolJet?style=flat)](https://github.com/ToolJet/ToolJet/stargazers) - Open-source Retool alternative

Services:
- [DronaHQ](https://www.dronahq.com/) - Retool alternative
- [Retool](https://retool.com/) - Drag-and-drop editor with pre-built components to build internal tools

### Shell
 - [MongoDB Atlas CLI](https://github.com/mongodb/mongodb-atlas-cli) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongodb-atlas-cli?style=flat)](https://github.com/mongodb/mongodb-atlas-cli/stargazers) - Official Atlas API command-line client
 - [mongosh](https://github.com/mongodb-js/mongosh) [![GitHub stars](https://img.shields.io/github/stars/mongodb-js/mongosh?style=flat)](https://github.com/mongodb-js/mongosh/stargazers) - Official command-line client

### Web
 - [adminMongo](https://github.com/mrvautin/adminMongo) [![GitHub stars](https://img.shields.io/github/stars/mrvautin/adminMongo?style=flat)](https://github.com/mrvautin/adminMongo/stargazers) - Web-based user interface to handle connections and databases needs
 - [mongo-express](https://github.com/mongo-express/mongo-express) [![GitHub stars](https://img.shields.io/github/stars/mongo-express/mongo-express?style=flat)](https://github.com/mongo-express/mongo-express/stargazers) - Web-based admin interface built with Express
 - [mongoadmin](https://github.com/thomasst/mongoadmin) [![GitHub stars](https://img.shields.io/github/stars/thomasst/mongoadmin?style=flat)](https://github.com/thomasst/mongoadmin/stargazers) - Admin interface built with Django
 - [Mongoku](https://github.com/huggingface/Mongoku) [![GitHub stars](https://img.shields.io/github/stars/huggingface/Mongoku?style=flat)](https://github.com/huggingface/Mongoku/stargazers) - MongoDB client for the web
 - [Rockmongo](https://github.com/iwind/rockmongo) [![GitHub stars](https://img.shields.io/github/stars/iwind/rockmongo?style=flat)](https://github.com/iwind/rockmongo/stargazers) - PHPMyAdmin for MongoDB, sort of

Services:

 - [HumongouS.io](https://www.humongous.io) - Easy online GUI and data-visualization dashboards

## Applications

Those open-source applications have MongoDB somewhere in their stack:

 - [BookCars](https://github.com/aelassas/bookcars) [![GitHub stars](https://img.shields.io/github/stars/aelassas/bookcars?style=flat)](https://github.com/aelassas/bookcars/stargazers) - Cross-platform, customizable and cost-efficient car rental management application
 - [CodeCombat](https://github.com/codecombat/codecombat) [![GitHub stars](https://img.shields.io/github/stars/codecombat/codecombat?style=flat)](https://github.com/codecombat/codecombat/stargazers) - Multiplayer programming game for learning how to code
 - [Countly](https://github.com/countly/countly-server) [![GitHub stars](https://img.shields.io/github/stars/countly/countly-server?style=flat)](https://github.com/countly/countly-server/stargazers) - Mobile & web analytics and marketing platform built with Node.js
 - [Errbit](https://github.com/errbit/errbit) [![GitHub stars](https://img.shields.io/github/stars/errbit/errbit?style=flat)](https://github.com/errbit/errbit/stargazers) - A Ruby on Rails based tool for collecting and managing errors from other applications.
 - [FactorJS](https://github.com/fiction-com/factor) [![GitHub stars](https://img.shields.io/github/stars/fiction-com/factor?style=flat)](https://github.com/fiction-com/factor/stargazers) - JavaScript CMS built with Mongoose
 - [GrandNode](https://github.com/grandnode/grandnode) [![GitHub stars](https://img.shields.io/github/stars/grandnode/grandnode?style=flat)](https://github.com/grandnode/grandnode/stargazers) - Multi-platform e-commerce shopping cart built with ASP.NET
 - [LastSaaS](https://github.com/jonradoff/lastsaas) [![GitHub stars](https://img.shields.io/github/stars/jonradoff/lastsaas?style=flat)](https://github.com/jonradoff/lastsaas/stargazers) - Open-source SaaS platform foundation with multi-tenant auth, Stripe billing, and MCP server, built with Go and MongoDB
 - [Leanote](https://github.com/leanote/leanote) [![GitHub stars](https://img.shields.io/github/stars/leanote/leanote?style=flat)](https://github.com/leanote/leanote/stargazers) - Evernote clone built with Go
 - [NodeBB](https://github.com/NodeBB/NodeBB) [![GitHub stars](https://img.shields.io/github/stars/NodeBB/NodeBB?style=flat)](https://github.com/NodeBB/NodeBB/stargazers) - Node.js based forum software ("built for the modern web")
 - [Reaction](https://github.com/reactioncommerce/reaction) [![GitHub stars](https://img.shields.io/github/stars/reactioncommerce/reaction?style=flat)](https://github.com/reactioncommerce/reaction/stargazers) - Event-driven, real-time commerce platform built with ES6
 - [SaaS Boilerplate](https://github.com/async-labs/saas) [![GitHub stars](https://img.shields.io/github/stars/async-labs/saas?style=flat)](https://github.com/async-labs/saas/stargazers) - Boilerplate for SaaS products, built with TypeScript, React and Express
 - [uptime](https://github.com/fzaninotto/uptime) [![GitHub stars](https://img.shields.io/github/stars/fzaninotto/uptime?style=flat)](https://github.com/fzaninotto/uptime/stargazers) - Remote monitoring application built with Node.js and Bootstrap
 - [WildDuck Mail Server](https://github.com/nodemailer/wildduck) [![GitHub stars](https://img.shields.io/github/stars/nodemailer/wildduck?style=flat)](https://github.com/nodemailer/wildduck/stargazers) - Scalable high availability email server that uses MongoDB for email storage

## License
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Guillaume Gelin](https://github.com/ramnes) [![GitHub stars](https://img.shields.io/github/stars/ramnes?style=flat)](https://github.com/ramnes/stargazers) has waived all copyright and related or neighboring rights to this work.
