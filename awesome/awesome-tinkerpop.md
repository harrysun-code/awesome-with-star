# TinkerPop

[![GitHub stars](https://img.shields.io/github/stars/mohataher/awesome-tinkerpop?style=flat)](https://github.com/mohataher/awesome-tinkerpop/stargazers)

# Awesome TinkerPop [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

![alt tag](https://raw.githubusercontent.com/mohataher/awesome-tinkerpop/master/tinkerpop-splash.png)


A curated list of only awesome TinkerPop libraries on Github.

>Apache TinkerPop™ is a graph computing framework for both graph databases (OLTP) and graph analytic systems (OLAP).

### Table of Contents
* [TinkerPop3](#tinkerpop3)
	- [Implementations](#tinkerpop3-implementations)
	- [Wrappers/Clients](#wrappers)
	- [Query Languages](#qlang)
* [TinkerPop2](#tinkerpop2)
* [Communites](#communites)
* [People to Follow](#people-to-follow)
* [Tutorials and Resources](#tutorials-and-resources)
* [How to Contribute](#contributing)
* [License](#license)

### <A NAME="tinkerpop3"></A>TinkerPop3 Libraries
#### <A NAME="tinkerpop3-implementations"></A>Implementations
* [TinkerPop3 implementation](https://github.com/apache/tinkerpop) [![GitHub stars](https://img.shields.io/github/stars/apache/tinkerpop?style=flat)](https://github.com/apache/tinkerpop/stargazers) - Mirror of Apache TinkerPop.
* [sqlg](https://github.com/pietermartin/sqlg) [![GitHub stars](https://img.shields.io/github/stars/pietermartin/sqlg?style=flat)](https://github.com/pietermartin/sqlg/stargazers) - Sqlg is a implementation of TinkerPop3 on a RDBMS.
* [blazegraph](https://github.com/blazegraph/database) [![GitHub stars](https://img.shields.io/github/stars/blazegraph/database?style=flat)](https://github.com/blazegraph/database/stargazers) - TinkerPop3 [implementation](https://github.com/blazegraph/tinkerpop3) [![GitHub stars](https://img.shields.io/github/stars/blazegraph/tinkerpop3?style=flat)](https://github.com/blazegraph/tinkerpop3/stargazers) for Blaze Graph; a high performance graph database.
* [tinkergraph-js](https://github.com/jbmusso/tinkergraph-js) [![GitHub stars](https://img.shields.io/github/stars/jbmusso/tinkergraph-js?style=flat)](https://github.com/jbmusso/tinkergraph-js/stargazers) - A pure JavaScript implementation of TinkerPop's TinkerGraph in-memory graph database.
* [gremlin-javascript](https://github.com/jbmusso/gremlin-javascript) [![GitHub stars](https://img.shields.io/github/stars/jbmusso/gremlin-javascript?style=flat)](https://github.com/jbmusso/gremlin-javascript/stargazers) - JavaScript graph database client for TinkerPop3 Gremlin Server.
* [Elastic Gremlin](https://github.com/rmagen/elastic-gremlin) [![GitHub stars](https://img.shields.io/github/stars/rmagen/elastic-gremlin?style=flat)](https://github.com/rmagen/elastic-gremlin/stargazers) - TinkerPop3 implementation on Elasticsearch backend.
* [Hadoop (Giraph)](http://tinkerpop.apache.org/docs/current/reference/#giraphgraphcomputer) - OLAP graph processor using Giraph.
* [Hadoop (Spark)](http://tinkerpop.apache.org/docs/current/reference/#sparkgraphcomputer) - OLAP graph processor using Spark.
* [IBM Graph](https://console.ng.bluemix.net/catalog/services/ibm-graph/) - OLTP graph database as a service.
* [Neo4j](http://tinkerpop.apache.org/docs/currentg/#neo4j-gremlin) - OLTP graph database.
* [Stardog](http://stardog.com/) - RDF graph database with OLTP and OLAP support.
* [TinkerGraph](http://tinkerpop.apache.org/docs/current/reference/#tinkergraph-gremlin) - In-memory OLTP and OLAP reference implementation.
* [Unipop](https://github.com/rmagen/unipop) [![GitHub stars](https://img.shields.io/github/stars/rmagen/unipop?style=flat)](https://github.com/rmagen/unipop/stargazers) - OLTP Elasticsearch and JDBC backed graph.
* [DuctileDB](https://github.com/PureSolTechnologies/DuctileDB) [![GitHub stars](https://img.shields.io/github/stars/PureSolTechnologies/DuctileDB?style=flat)](https://github.com/PureSolTechnologies/DuctileDB/stargazers) - Ductile DB is a graph database based on Hadoop/HBase which provides a vast set of features.
* [hgraphdb](https://github.com/rayokota/hgraphdb) [![GitHub stars](https://img.shields.io/github/stars/rayokota/hgraphdb?style=flat)](https://github.com/rayokota/hgraphdb/stargazers) - HBase as a TinkerPop Graph Database.
* [JanusGraph](https://github.com/JanusGraph/janusgraph) [![GitHub stars](https://img.shields.io/github/stars/JanusGraph/janusgraph?style=flat)](https://github.com/JanusGraph/janusgraph/stargazers) - JanusGraph: an open-source, distributed graph database http://janusgraph.org 
* [JanusGraph for DynamoDB (Amazon)](https://github.com/awslabs/dynamodb-janusgraph-storage-backend) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-janusgraph-storage-backend?style=flat)](https://github.com/awslabs/dynamodb-janusgraph-storage-backend/stargazers) - The Amazon DynamoDB storage backend for JanusGraph.
* [orientdb-gremlin](https://github.com/orientechnologies/orientdb-gremlin) [![GitHub stars](https://img.shields.io/github/stars/orientechnologies/orientdb-gremlin?style=flat)](https://github.com/orientechnologies/orientdb-gremlin/stargazers) - TinkerPop3 Graph Structure Implementation for OrientDB.


#### <A NAME="wrappers"></A>Wrappers/Clients
##### C# .NET
*   [Teva Gremlin](https://www.nuget.org/packages/Teva.Common.Data.Gremlin/) (.NET - C#) - A Gremlin Server driver for .NET.

##### Clojure
* [ogre](https://github.com/clojurewerkz/ogre) [![GitHub stars](https://img.shields.io/github/stars/clojurewerkz/ogre?style=flat)](https://github.com/clojurewerkz/ogre/stargazers) - Clojure library for querying TinkerPop graphs.
* [scalajs-gremlin-client](https://github.com/viagraphs/scalajs-gremlin-client) [![GitHub stars](https://img.shields.io/github/stars/viagraphs/scalajs-gremlin-client?style=flat)](https://github.com/viagraphs/scalajs-gremlin-client/stargazers) (scala) - A Gremlin-Server client with ad-hoc extensible, reactive, typeclass based API.

##### Go
* [go-gremlin](https://github.com/go-gremlin/gremlin) [![GitHub stars](https://img.shields.io/github/stars/go-gremlin/gremlin?style=flat)](https://github.com/go-gremlin/gremlin/stargazers) - Go graph database client for TinkerPop3 Gremlin Server.
* [Gremgo](https://github.com/qasaur/gremgo) [![GitHub stars](https://img.shields.io/github/stars/qasaur/gremgo?style=flat)](https://github.com/qasaur/gremgo/stargazers) - A fast, efficient, and easy-to-use Go client for the TinkerPop graph database stack.
* [grammes](https://github.com/northwesternmutual/grammes) [![GitHub stars](https://img.shields.io/github/stars/northwesternmutual/grammes?style=flat)](https://github.com/northwesternmutual/grammes/stargazers) - A Go package built to communicate with Apache TinkerPop™ Graph computing framework using Gremlin.

##### Haskell
* [greskell-websocket](https://github.com/debug-ito/greskell) [![GitHub stars](https://img.shields.io/github/stars/debug-ito/greskell?style=flat)](https://github.com/debug-ito/greskell/stargazers) - Haskell client for TinkerPop3 Gremlin Server.

##### Java
* [gremlin-driver](http://tinkerpop.apache.org/docs/current/reference/#connecting-via-java) (java) - A Gremlin Server driver for Java.
* [neo4j-tinkerpop-api](https://github.com/neo4j-contrib/neo4j-tinkerpop-api) [![GitHub stars](https://img.shields.io/github/stars/neo4j-contrib/neo4j-tinkerpop-api?style=flat)](https://github.com/neo4j-contrib/neo4j-tinkerpop-api/stargazers) - Apache Licensed Neo4j API for TinkerPop3.
* [neo4j-gremlin-bolt](https://github.com/SteelBridgeLabs/neo4j-gremlin-bolt) [![GitHub stars](https://img.shields.io/github/stars/SteelBridgeLabs/neo4j-gremlin-bolt?style=flat)](https://github.com/SteelBridgeLabs/neo4j-gremlin-bolt/stargazers) - Allows use of the Apache Tinkerpop Java API with the neo4j server using the BOLT protocol.
* [Ferma](https://github.com/Syncleus/Ferma) [![GitHub stars](https://img.shields.io/github/stars/Syncleus/Ferma?style=flat)](https://github.com/Syncleus/Ferma/stargazers) - An ORM / OGM for the TinkerPop graph stack.

##### Javascript
* [ts-tinkerpop](https://github.com/RedSeal-co/ts-tinkerpop) [![GitHub stars](https://img.shields.io/github/stars/RedSeal-co/ts-tinkerpop?style=flat)](https://github.com/RedSeal-co/ts-tinkerpop/stargazers) - Utilities for using TinkerPop3 via the node-java API in Typescript.
* [gremlin-javascript](https://github.com/jbmusso/gremlin-javascript) [![GitHub stars](https://img.shields.io/github/stars/jbmusso/gremlin-javascript?style=flat)](https://github.com/jbmusso/gremlin-javascript/stargazers) (js) - A Gremlin Server driver for JavaScript.

##### PHP
* [gremlin-php](https://github.com/PommeVerte/gremlin-php) [![GitHub stars](https://img.shields.io/github/stars/PommeVerte/gremlin-php?style=flat)](https://github.com/PommeVerte/gremlin-php/stargazers) - gremlin-server php driver compatible with TinkerPop3. It will allow you to connect to gremlin-server and it's backends (Neo4J, Titan, etc.).

##### Python
* [Mogwai](https://github.com/platinummonkey/mogwai) [![GitHub stars](https://img.shields.io/github/stars/platinummonkey/mogwai?style=flat)](https://github.com/platinummonkey/mogwai/stargazers) - TinkerPop3 Graph Database Library for Python.
* [python-gremlin-rest](https://github.com/windj007/python-gremlin-rest) [![GitHub stars](https://img.shields.io/github/stars/windj007/python-gremlin-rest?style=flat)](https://github.com/windj007/python-gremlin-rest/stargazers) - A REST-based client for Gremlin Server.
* [gremlinclient](https://github.com/davebshow/gremlinclient) [![GitHub stars](https://img.shields.io/github/stars/davebshow/gremlinclient?style=flat)](https://github.com/davebshow/gremlinclient/stargazers) - An asynchronous Python 2/3 client for Gremlin Server that allows for flexible coroutine syntax - Trollius, Tornado, Asyncio.
* [aiogremlin](https://github.com/davebshow/aiogremlin) [![GitHub stars](https://img.shields.io/github/stars/davebshow/aiogremlin?style=flat)](https://github.com/davebshow/aiogremlin/stargazers) (python) - A Python 3 library based on asyncio and aiohttp that uses websockets to communicate with the Gremlin Server.
* [gremlinrestclient](http://gremlinrestclient.readthedocs.org/en/latest/) (python) - Python 2/3 library that uses HTTP to communicate with the Gremlin Server over REST.
* [goblin](https://github.com/ZEROFAIL/goblin) [![GitHub stars](https://img.shields.io/github/stars/ZEROFAIL/goblin?style=flat)](https://github.com/ZEROFAIL/goblin/stargazers) - OGM for TinkerPop3 Gremlin Server.
* [goblin 3.5](https://github.com/davebshow/goblin) [![GitHub stars](https://img.shields.io/github/stars/davebshow/goblin?style=flat)](https://github.com/davebshow/goblin/stargazers) - A Python 3.5 rewrite of the TinkerPop 3 OGM Goblin.

##### Reactive
* [reactive-gremlin](https://github.com/coreyauger/reactive-gremlin) [![GitHub stars](https://img.shields.io/github/stars/coreyauger/reactive-gremlin?style=flat)](https://github.com/coreyauger/reactive-gremlin/stargazers) (scala) - An Akka HTTP Websocket Connector.

##### Scala
* [Gremlin Scala](https://github.com/mpollmeier/gremlin-scala) [![GitHub stars](https://img.shields.io/github/stars/mpollmeier/gremlin-scala?style=flat)](https://github.com/mpollmeier/gremlin-scala/stargazers) - Scala wrapper for Apache TinkerPop3 Graph DSL.
* [blueprints-scala](https://github.com/anvie/blueprints-scala) [![GitHub stars](https://img.shields.io/github/stars/anvie/blueprints-scala?style=flat)](https://github.com/anvie/blueprints-scala/stargazers) - Tinkerpop Blueprints Scala.

#### <A NAME="qlang"></A>Query Languages
* [gremlin-py](https://github.com/emehrkay/gremlinpy) [![GitHub stars](https://img.shields.io/github/stars/emehrkay/gremlinpy?style=flat)](https://github.com/emehrkay/gremlinpy/stargazers) - Write pure Python Gremlin that can be sent to Gremlin Server.
* [gremlin-scala](https://github.com/mpollmeier/gremlin-scala) [![GitHub stars](https://img.shields.io/github/stars/mpollmeier/gremlin-scala?style=flat)](https://github.com/mpollmeier/gremlin-scala/stargazers) - A Scala language wrapper for TinkerPop3.
* [gremlin-template-string](https://github.com/jbmusso/gremlin-template-string) [![GitHub stars](https://img.shields.io/github/stars/jbmusso/gremlin-template-string?style=flat)](https://github.com/jbmusso/gremlin-template-string/stargazers) - A Javascript Gremlin language builder.
* [ipython-gremlin](https://github.com/davebshow/ipython-gremlin) [![GitHub stars](https://img.shields.io/github/stars/davebshow/ipython-gremlin?style=flat)](https://github.com/davebshow/ipython-gremlin/stargazers) - Gremlin in IPython and Jupyter.
* [ogre](http://ogre.clojurewerkz.org/) - A Clojure language wrapper for TinkerPop3.
* [Peapod](https://github.com/bayofmany/peapod) [![GitHub stars](https://img.shields.io/github/stars/bayofmany/peapod?style=flat)](https://github.com/bayofmany/peapod/stargazers) - A new object-graph-wrapper for the Tinkerpop3 graph stack.
* [sparql-gremlin](https://github.com/dkuppitz/sparql-gremlin) [![GitHub stars](https://img.shields.io/github/stars/dkuppitz/sparql-gremlin?style=flat)](https://github.com/dkuppitz/sparql-gremlin/stargazers) - A SPARQL to Gremlin traversal compiler.
* [sql-gremlin](https://github.com/twilmes/sql-gremlin) [![GitHub stars](https://img.shields.io/github/stars/twilmes/sql-gremlin?style=flat)](https://github.com/twilmes/sql-gremlin/stargazers) - A SQL to Gremlin traversal compiler.
* [greskell](https://github.com/debug-ito/greskell) [![GitHub stars](https://img.shields.io/github/stars/debug-ito/greskell?style=flat)](https://github.com/debug-ito/greskell/stargazers) - Haskell binding for Gremlin graph query language
* [Cypher for Gremlin](https://github.com/opencypher/cypher-for-gremlin) [![GitHub stars](https://img.shields.io/github/stars/opencypher/cypher-for-gremlin?style=flat)](https://github.com/opencypher/cypher-for-gremlin/stargazers) -  Cypher for Gremlin adds Cypher support to any Gremlin graph database.

### <A NAME="tinkerpop2"></A>TinkerPop 2 Libraries
* [Ferma](https://github.com/Syncleus/Ferma) [![GitHub stars](https://img.shields.io/github/stars/Syncleus/Ferma?style=flat)](https://github.com/Syncleus/Ferma/stargazers) - An ORM / OGM for the TinkerPop graph stack.
* [Frames](https://github.com/tinkerpop/frames) [![GitHub stars](https://img.shields.io/github/stars/tinkerpop/frames?style=flat)](https://github.com/tinkerpop/frames/stargazers) - An Object to Graph Framework.
* [Archimedes](https://github.com/clojurewerkz/archimedes) [![GitHub stars](https://img.shields.io/github/stars/clojurewerkz/archimedes?style=flat)](https://github.com/clojurewerkz/archimedes/stargazers) - Clojure library for Blueprints (part of the TinkerPop graph stack).
* [AccumuloGraph](https://github.com/JHUAPL/AccumuloGraph) [![GitHub stars](https://img.shields.io/github/stars/JHUAPL/AccumuloGraph?style=flat)](https://github.com/JHUAPL/AccumuloGraph/stargazers) - An implementation of TinkerPop Blueprints using Accumulo.
* [Frontenac](https://github.com/Loupi/Frontenac) [![GitHub stars](https://img.shields.io/github/stars/Loupi/Frontenac?style=flat)](https://github.com/Loupi/Frontenac/stargazers) - A .NET port of the TinkerPop Stack.
* [Mogwai](https://github.com/platinummonkey/mogwai) [![GitHub stars](https://img.shields.io/github/stars/platinummonkey/mogwai?style=flat)](https://github.com/platinummonkey/mogwai/stargazers) - TinkerPop 2 Graph Database Library for Python.
* [spring-data-gremlin](https://github.com/gjrwebber/spring-data-gremlin) [![GitHub stars](https://img.shields.io/github/stars/gjrwebber/spring-data-gremlin?style=flat)](https://github.com/gjrwebber/spring-data-gremlin/stargazers) - Spring data gremlin makes it easier to implement Graph based repositories. This module extends Spring Data to allow support for potentially any Graph database that implements the TinkerPop Blueprints 2.x API.
* [blueprints-scala](https://github.com/anvie/blueprints-scala) [![GitHub stars](https://img.shields.io/github/stars/anvie/blueprints-scala?style=flat)](https://github.com/anvie/blueprints-scala/stargazers) - TinkerPop Blueprints Scala.

## <A NAME="communites"></A>Communities
* [Gremlin-users](https://groups.google.com/forum/#!forum/gremlin-users) - Mailing list for Gremlin users.
* [Stack Overflow](http://stackoverflow.com/questions/tagged/tinkerpop3) - Stack Overflow has a relatively active community.
* [TinkerPop-dev](http://mail-archives.apache.org/mod_mbox/incubator-tinkerpop-dev/) - Mailing list for TP3 deverlopers.

## <A NAME="people-to-follow"></A>People to Follow 
* [Marko Rodriguez](https://markorodriguez.com/) - Founder of TinkerPop and Aurelius.
* [Stephen Mallette](https://twitter.com/spmallette?lang=en-gb) - Senior developer for Gremlin, TinkerPop and Titan DB.
* [Daniel Kuppitz](https://about.me/daniel.kuppitz) - One of the main developers of Gremlin.
* [Jason Plurad](https://github.com/pluradj) [![GitHub stars](https://img.shields.io/github/stars/pluradj?style=flat)](https://github.com/pluradj/stargazers) - Senior Developer at IBM. TinkerPop committer and active on the community.

## <A NAME="tutorials-and-resources"></A>Tutorials and Resources
* [Introduction to Gremlin](http://tinkerpop.apache.org/gremlin.html) - Official introduction to the Gremlin language.
* [Datastax Introduction](https://academy.datastax.com/resources/getting-started-tinkerpop-and-gremlin) - A tutorial provided by Datastax to Gremlin and TinkerPop3.
* [TinkerPop Book](http://www.tinkerpopbook.com/) - A long promised book for Tinkeprop but never fulfilled until now. You cans till request a notification.
* [Linux Foundation Presentation](http://events.linuxfoundation.org/sites/events/files/slides/ApacheCon2015TinkerPop3.pdf) - A presentation by Linux Foundation given by David Robinson at IBM aboit Apache TinkerPop3.
* [Getting Started with TinkerPop](http://tinkerpop.apache.org/docs/current/tutorials/getting-started/) - Learn the basics of getting up and going with TinkerPop.
* [The Gremlin Console](http://tinkerpop.apache.org/docs/current/tutorials/the-gremlin-console/) - Discusses uses cases of the Gremlin Console and usage patterns.
* [Gremlin Recipes](http://tinkerpop.apache.org/docs/3.2.1-SNAPSHOT/recipes/) - Reference for common traversal patterns and style.
* [Gremlin Language Variants](http://tinkerpop.apache.org/docs/3.2.1-SNAPSHOT/tutorials/gremlin-language-variants/) - Learn how to embed Gremlin in a host programming language.
* [SQL2Gremlin](http://sql2gremlin.com/) - Learn Gremlin using typical patterns found when querying data with SQL.
* [Getting Started with Graph Databases](https://academy.datastax.com/demos/getting-started-graph-databases) - Compares relational databases to graph databases and SQL to Gremlin.
* [Graph](https://github.com/krlawrence/graph) [![GitHub stars](https://img.shields.io/github/stars/krlawrence/graph?style=flat)](https://github.com/krlawrence/graph/stargazers) - Graph Databases, Gremlin and TinkerPop - A Tutorial.


## <A NAME="contributing"></A>How to Contribute
![alt tag](awesome-tinkerpop.jpg)

Please follow the [guidelines here](contributing.md). Please, make sure your contribution and PR are awesome!

## <A NAME="license"></A>License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [@mohataher](https://github.com/mohataher) [![GitHub stars](https://img.shields.io/github/stars/mohataher?style=flat)](https://github.com/mohataher/stargazers) has waived all copyright and related or neighboring rights to this work.
