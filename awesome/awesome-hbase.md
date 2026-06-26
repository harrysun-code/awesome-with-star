# HBase

[![GitHub stars](https://img.shields.io/github/stars/rayokota/awesome-hbase?style=flat)](https://github.com/rayokota/awesome-hbase/stargazers)

# Awesome HBase [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://cdn.rawgit.com/rayokota/awesome-hbase/c197f415/hbase_logo_with_orca-2.png" align="right" width="150">](http://hbase.apache.org/)

A curated list of awesome HBase projects and resources.

[HBase](http://hbase.apache.org) is a distributed, scalable, big data store.

## Contents

- [Projects](#projects)
    - [Clients](#clients)
    - [Cloud](#cloud)
    - [Frameworks](#frameworks)
        - [Datasets](#datasets)
        - [Document](#document)
        - [Entity/JPA](#entityjpa)
        - [Geospatial](#geospatial)
        - [Graph](#graph)
        - [SQL/OLAP](#sqlolap)
        - [Time Series](#time-series)
    - [Infrastructure](#infrastructure)
        - [Secondary Indices](#secondary-indices)
        - [Transactions](#transactions)
    - [Integrations](#integrations)
    - [Tools](#tools)
    - [Miscellaneous](#miscellaneous)

- [Resources](#resources)
    - [Books](#books)
    - [Papers](#papers)
    - [Community](#community)

    
## Projects

### Clients

* [asynchbase](https://github.com/OpenTSDB/asynchbase) [![GitHub stars](https://img.shields.io/github/stars/OpenTSDB/asynchbase?style=flat)](https://github.com/OpenTSDB/asynchbase/stargazers) - Fully asynchronous, non-blocking HBase client.
* [gohbase](https://github.com/tsuna/gohbase) [![GitHub stars](https://img.shields.io/github/stars/tsuna/gohbase?style=flat)](https://github.com/tsuna/gohbase/stargazers) - Pure Go client for HBase.
* [happybase](https://github.com/wbolster/happybase) [![GitHub stars](https://img.shields.io/github/stars/wbolster/happybase?style=flat)](https://github.com/wbolster/happybase/stargazers) - Python client for HBase.


### Cloud

* [Amazon EMR](https://aws.amazon.com/emr/) - Amazon's Hadoop/HBase offering on AWS.
* [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) - Microsoft's Hadoop/HBase offering on Azure.
* [Cloudera Director](https://www.cloudera.com/products/product-components/cloudera-director.html) - Run Hadoop/HBase clusters on AWS, Azure or Google Cloud.
* [Google Cloud Bigtable](https://cloud.google.com/bigtable/) - High-performance NoSQL database service accessible via HBase client API.
* [Hortonworks Cloudbreak](https://hortonworks.com/open-source/cloudbreak/) - Provision Hadoop/HBase clusters on AWS, Azure, Google Cloud, or OpenStack.

### Frameworks

#### Datasets

* [Kite](http://kitesdk.org) - High-level data layer for Hadoop/HBase.

#### Document

* [HDocDB](https://github.com/rayokota/hdocdb) [![GitHub stars](https://img.shields.io/github/stars/rayokota/hdocdb?style=flat)](https://github.com/rayokota/hdocdb/stargazers) - HBase as a JSON document database.

#### Entity/JPA

* [DataNucleus](http://www.datanucleus.org) - JPA persistence layer with support for HBase.
* [Gora](http://gora.apache.org) - Persistence library for big data with support for HBase.
* [HBase ORM](https://github.com/flipkart-incubator/hbase-orm) [![GitHub stars](https://img.shields.io/github/stars/flipkart-incubator/hbase-orm?style=flat)](https://github.com/flipkart-incubator/hbase-orm/stargazers) - A production-grade HBase ORM library.
* [HEntityDB](https://github.com/rayokota/hentitydb) [![GitHub stars](https://img.shields.io/github/stars/rayokota/hentitydb?style=flat)](https://github.com/rayokota/hentitydb/stargazers) - HBase as an entity database.
* [Kundera](https://github.com/impetus-opensource/Kundera) [![GitHub stars](https://img.shields.io/github/stars/impetus-opensource/Kundera?style=flat)](https://github.com/impetus-opensource/Kundera/stargazers) - JPA client with support for HBase.

#### Geospatial

* [GeoMesa](http://www.geomesa.org/) - Spatial-temporal database with support for Accumulo, HBase, Cassandra, and Kafka.

#### Graph
* [Gradoop](https://github.com/dbs-leipzig/gradoop) [![GitHub stars](https://img.shields.io/github/stars/dbs-leipzig/gradoop?style=flat)](https://github.com/dbs-leipzig/gradoop/stargazers) - Research framework for scalable graph analytics built on Flink and HBase.
* [HGraphDB](https://github.com/rayokota/hgraphdb) [![GitHub stars](https://img.shields.io/github/stars/rayokota/hgraphdb?style=flat)](https://github.com/rayokota/hgraphdb/stargazers) - HBase as a TinkerPop graph database.
* [HugeGraph](https://github.com/apache/incubator-hugegraph) [![GitHub stars](https://img.shields.io/github/stars/apache/incubator-hugegraph?style=flat)](https://github.com/apache/incubator-hugegraph/stargazers) - A graph database that supports more than 10+ billion data, high performance and scalability.
* [JanusGraph](http://janusgraph.org/) - Scalable graph database with support for Cassandra, HBase, Google Cloud Bigtable, and BerkeleyDB.
* [NebulaGraph](https://github.com/vesoft-inc/nebula) [![GitHub stars](https://img.shields.io/github/stars/vesoft-inc/nebula?style=flat)](https://github.com/vesoft-inc/nebula/stargazers) - A high performance distributed Graph database.
* [S2Graph](http://s2graph.incubator.apache.org) - High-performance distributed graph database built on HBase.
* [Actionbase](https://github.com/kakao/actionbase) [![GitHub stars](https://img.shields.io/github/stars/kakao/actionbase?style=flat)](https://github.com/kakao/actionbase/stargazers) - A database for user interactions (likes, views, follows) represented as graphs, with precomputed reads served in real-time.

#### SQL/OLAP

* [AntsDB](http://antsdb.com/) - AntsDB is a low latency, high concurrency, MySQL compliant SQL layer for HBase.
* [EsgynDB](https://esgyn.com/) - Commercial SQL engine providing ACID transactions and BI analytics on top of Hadoop, based on Trafodian.
* [Kylin](http://kylin.apache.org) - Extreme OLAP engine for big data that stores data in HBase.
* [LeanXScale](http://www.leanxcale.com) - Commercial full ACID full SQL product built on Hadoop/HBase.
* [Phoenix](https://phoenix.apache.org) - SQL layer on top of HBase.
* [Splice Machine](https://www.splicemachine.com) - Commercial RDBMS built on top of HBase.
* [Trafodian](http://trafodion.apache.org) - Transactional SQL-on-Hadoop/HBase.

#### Time Series

* [Axibase](http://axibase.com/products/axibase-time-series-database/) - Distributed time series database built on HBase.
* [OpenTSDB](http://opentsdb.net) - Scalable time series database built on HBase.
* [Warp 10](http://www.warp10.io) - Time series database for sensor data.

### Infrastructure

#### Secondary Indices

* [hindex](https://github.com/Huawei-Hadoop/hindex) [![GitHub stars](https://img.shields.io/github/stars/Huawei-Hadoop/hindex?style=flat)](https://github.com/Huawei-Hadoop/hindex/stargazers) - Secondary index for HBase.
* [Lily HBase Indexer](http://ngdata.github.io/hbase-indexer/) - Quickly and easily search for content stored in HBase.

#### Transactions

* [Haeinsa](https://github.com/VCNC/haeinsa) [![GitHub stars](https://img.shields.io/github/stars/VCNC/haeinsa?style=flat)](https://github.com/VCNC/haeinsa/stargazers) - Multi-row/multi-table transaction library for HBase.
* [HBase-QoD](https://github.com/algarecu/hbase-0.94.8-qod) [![GitHub stars](https://img.shields.io/github/stars/algarecu/hbase-0.94.8-qod?style=flat)](https://github.com/algarecu/hbase-0.94.8-qod/stargazers) - Vector-field consistency for HBase fine-grained transactional inter-DC replication.
* [Omid](https://github.com/apache/incubator-omid) [![GitHub stars](https://img.shields.io/github/stars/apache/incubator-omid?style=flat)](https://github.com/apache/incubator-omid/stargazers) - Transactional support for HBase.
* [Tephra](http://tephra.incubator.apache.org) - Globally consistent transactions on top of HBase.
* [Themis](https://github.com/XiaoMi/themis) [![GitHub stars](https://img.shields.io/github/stars/XiaoMi/themis?style=flat)](https://github.com/XiaoMi/themis/stargazers) - Cross-row/cross-table transactions on HBase based on Google's Percolator.

### Integrations

* [Apex](https://github.com/apache/apex-malhar/tree/master/contrib/src/test/java/org/apache/apex/malhar/contrib/hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/apex-malhar/tree/master/contrib/src/test/java/org/apache/apex/malhar/contrib/hbase?style=flat)](https://github.com/apache/apex-malhar/tree/master/contrib/src/test/java/org/apache/apex/malhar/contrib/hbase/stargazers) - Apex-HBase connector.
* [Beam](https://github.com/apache/beam/tree/master/sdks/java/io/hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/beam/tree/master/sdks/java/io/hbase?style=flat)](https://github.com/apache/beam/tree/master/sdks/java/io/hbase/stargazers) - Beam HBase integration.
* [Camel](http://camel.apache.org/hbase.html) - Camel HBase component.
* [Cascading](https://github.com/Cascading/cascading.hbase) [![GitHub stars](https://img.shields.io/github/stars/Cascading/cascading.hbase?style=flat)](https://github.com/Cascading/cascading.hbase/stargazers) - HBase adapters for Cascading.
* [Cascalog](https://github.com/sorenmacbeth/hbase-cascalog) [![GitHub stars](https://img.shields.io/github/stars/sorenmacbeth/hbase-cascalog?style=flat)](https://github.com/sorenmacbeth/hbase-cascalog/stargazers) - Wrapper around Cascading.HBase for use in Cascalog.
* [Crunch](https://github.com/apache/crunch/tree/master/crunch-hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/crunch/tree/master/crunch-hbase?style=flat)](https://github.com/apache/crunch/tree/master/crunch-hbase/stargazers) - HBase adapters for Crunch.
* [Drill](https://drill.apache.org/docs/querying-hbase/) - HBase storage plugin for Drill.
* [Elasticsearch](https://github.com/mallocator/Elasticsearch-HBase-River) [![GitHub stars](https://img.shields.io/github/stars/mallocator/Elasticsearch-HBase-River?style=flat)](https://github.com/mallocator/Elasticsearch-HBase-River/stargazers) - Elasticsearch import river for HBase.
* [Flink](https://github.com/apache/flink/tree/master/flink-connectors/flink-connector-hbase-2.2) [![GitHub stars](https://img.shields.io/github/stars/apache/flink/tree/master/flink-connectors/flink-connector-hbase-2.2?style=flat)](https://github.com/apache/flink/tree/master/flink-connectors/flink-connector-hbase-2.2/stargazers) - Flink-HBase connector.
* [Gearpump](https://github.com/apache/incubator-gearpump/tree/master/external/hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/incubator-gearpump/tree/master/external/hbase?style=flat)](https://github.com/apache/incubator-gearpump/tree/master/external/hbase/stargazers) - Gearpump integration for HBase.
* [Giraph](https://github.com/apache/giraph/tree/trunk/giraph-hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/giraph/tree/trunk/giraph-hbase?style=flat)](https://github.com/apache/giraph/tree/trunk/giraph-hbase/stargazers) - Giraph input and output formats for HBase.
* [HAWQ](https://hawq.apache.org/docs/userguide/2.3.0.0-incubating/pxf/HBasePXF.html) - HAWQ PXF external tables on HBase.
* [Hive](https://cwiki.apache.org/confluence/display/Hive/HBaseIntegration) - Hive HBase integration.
* [Impala](https://www.cloudera.com/documentation/enterprise/latest/topics/impala_hbase.html) - Impala support for querying HBase tables.
* [Kafka](https://github.com/apache/hbase-connectors/tree/master/kafka) [![GitHub stars](https://img.shields.io/github/stars/apache/hbase-connectors/tree/master/kafka?style=flat)](https://github.com/apache/hbase-connectors/tree/master/kafka/stargazers) - HBase Kafka proxy.
* [Pig](https://github.com/apache/pig/tree/trunk/src/org/apache/pig/backend/hadoop/hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/pig/tree/trunk/src/org/apache/pig/backend/hadoop/hbase?style=flat)](https://github.com/apache/pig/tree/trunk/src/org/apache/pig/backend/hadoop/hbase/stargazers) - Pig HBase integration.
* [Presto](https://github.com/analysys/presto-hbase-connector) [![GitHub stars](https://img.shields.io/github/stars/analysys/presto-hbase-connector?style=flat)](https://github.com/analysys/presto-hbase-connector/stargazers) - Presto-HBase connector.
* [Pulsar](http://pulsar.apache.org/docs/en/io-hbase/) - HBase connector for Pulsar.
* [Ranger](https://cwiki.apache.org/confluence/display/RANGER/HBase+Plugin) - HBase plugin for Apache Ranger.
* [Spark](https://github.com/hortonworks-spark/shc) [![GitHub stars](https://img.shields.io/github/stars/hortonworks-spark/shc?style=flat)](https://github.com/hortonworks-spark/shc/stargazers) - Spark-HBase connector.
* [Spring for Apache Hadoop](https://projects.spring.io/spring-hadoop/) - Spring-Hadoop integration, including HBase support.
* [Storm](https://github.com/apache/storm/tree/master/external/storm-hbase) [![GitHub stars](https://img.shields.io/github/stars/apache/storm/tree/master/external/storm-hbase?style=flat)](https://github.com/apache/storm/tree/master/external/storm-hbase/stargazers) - Storm/Trident integration for HBase.
* [Tajo](https://tajo.apache.org/docs/current/hbase_integration.html) - Tajo integration with HBase.
* [Zeppelin](https://zeppelin.apache.org/docs/0.6.2/interpreter/hbase.html) - HBase shell interpreter for Apache Zeppelin.

### Tools

* [Ambari](https://ambari.apache.org) - Software for provisioning, managing, and monitor Hadoop/HBase clusters.
* [Cloudera Manager](https://www.cloudera.com/products/product-components/cloudera-manager.html) - Tool for managing Hadoop/HBase in production.
* [DbSchema](http://www.dbschema.com/index.html) - Diagram-oriented database designer with support for HBase.
* [Hannibal](https://github.com/sentric/hannibal) [![GitHub stars](https://img.shields.io/github/stars/sentric/hannibal?style=flat)](https://github.com/sentric/hannibal/stargazers) - Tool to monitor and maintain HBase clusters.
* [h-rider](https://github.com/NiceSystems/hrider) [![GitHub stars](https://img.shields.io/github/stars/NiceSystems/hrider?style=flat)](https://github.com/NiceSystems/hrider/stargazers) - GUI for viewing and manipulating data in HBase.
* [Hue](http://gethue.com) - Smart analytics workbench that includes an HBase browser.
* [Sematext SPM](http://sematext.com/spm) - Tool for [monitoring HBase](http://sematext.com/spm/integrations/hbase-monitoring), HDFS, etc.

### Miscellaneous

* [HubSpot HBase support](https://github.com/HubSpot/hbase-support) [![GitHub stars](https://img.shields.io/github/stars/HubSpot/hbase-support?style=flat)](https://github.com/HubSpot/hbase-support/stargazers) - Configs and tools for HBase at HubSpot, including Hystrix integration and coprocessors.

## Resources

### Books

* [HBase in Action](https://www.manning.com/books/hbase-in-action) - Experience-driven guide that shows you how to use HBase.
* [HBase: The Definitive Guide](http://shop.oreilly.com/product/0636920014348.do) - Comprehensive guide to HBase.
* [Architecting HBase Applications](http://shop.oreilly.com/product/0636920035688.do) - Includes HBase principles, cluster guidelines, and in-depth case studies.
* [HBase Administration Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/hbase-administration-cookbook) - How to master HBase configuration and administration.
* [HBase Essentials](https://www.packtpub.com/big-data-and-business-intelligence/hbase-essentials) - A practical guide to using HBase.
* [HBase Design Patterns](https://www.packtpub.com/big-data-and-business-intelligence/hbase-design-patterns) - Successful patterns to develop scalable applications with HBase.
* [Learning HBase](https://www.packtpub.com/big-data-and-business-intelligence/learning-hbase) - Learn the fundamentals of HBase administration and development.
* [HBase High Performance Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/hbase-high-performance-cookbook) - Exciting projects that teach you how to use HBase.
* [Apache HBase Primer](http://www.apress.com/us/book/9781484224236) - A compact guide to HBase essentials.
* [Pro Apache Phoenix](http://www.apress.com/us/book/9781484223697) - Basic and best practices for using Phoenix.
* [Mathematics of Big Data](https://mitpress.mit.edu/9780262038393/mathematics-of-big-data/) - The mathematical theory behind wide-column stores such as HBase.

### Papers

* [Bigtable: A Distributed Storage System for Structured Data](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf) - The inspiration for HBase.
* [Apache Hadoop Goes Realtime at Facebook](https://pdfs.semanticscholar.org/865a/215390cd49af9e4941e03107120e631dcaa0.pdf) - How Facebook deployed HBase to production.

### Community

* [Blog](https://blogs.apache.org/hbase/)
* [Mailing Lists](http://hbase.apache.org/mail-lists.html)
* [Reddit](https://www.reddit.com/r/hbase/)
* [Stack Overflow](https://stackoverflow.com/questions/tagged/hbase)
* [Twitter](https://twitter.com/HBase)

## License

<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="http://creativecommons.org/publicdomain/mark/1.0/">
<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/publicdomain.svg"
     style="border-style: none;" alt="Public Domain Mark" />
</a>
