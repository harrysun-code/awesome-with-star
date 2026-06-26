# MySQL

[![GitHub stars](https://img.shields.io/github/stars/shlomi-noach/awesome-mysql?style=flat)](https://github.com/shlomi-noach/awesome-mysql/stargazers)

# awesome-mysql

A curated list of awesome MySQL free and opensource software, libraries and resources. [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This list accepts and encourages pull requests. See [CONTRIBUTING](https://github.com/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md/stargazers)

### Contents

- [Awesome MySQL](#awesome-mysql)
    - [Analysis](#analysis)
    - [Backup](#backup)
    - [Benchmarking](#benchmarking)
    - [Binlog Replication](#binlog-replication)
    - [ChatOps](#chatops)
    - [Configuration](#configuration)
    - [Connectors](#connectors)
    - [Deployment](#deployment)
    - [Development](#development)
    - [GUI](#gui)
    - [HA](#ha)
    - [MCP](#mcp)
    - [Proxy](#proxy)
    - [Replication](#replication)
    - [Schema](#schema)
    - [Security](#security)
    - [Server](#server)
    - [Sharding](#sharding)
    - [Toolkits](#toolkits)

- [Resources](#resources)
    - [E-Books](#e-books)


## Analysis

*Performance, structure & data analysis tools*

- [Anemometer](https://github.com/box/Anemometer) [![GitHub stars](https://img.shields.io/github/stars/box/Anemometer?style=flat)](https://github.com/box/Anemometer/stargazers) - Box SQL slow query monitor.
- [innodb-ruby](https://github.com/jeremycole/innodb_ruby) [![GitHub stars](https://img.shields.io/github/stars/jeremycole/innodb_ruby?style=flat)](https://github.com/jeremycole/innodb_ruby/stargazers) - A parser for InnoDB file formats, in Ruby.
- [innotop](https://github.com/innotop/innotop) [![GitHub stars](https://img.shields.io/github/stars/innotop/innotop?style=flat)](https://github.com/innotop/innotop/stargazers) - a 'top' clone for MySQL with many features and flexibility.
- [MySQL Explain Analyzer](https://github.com/Preetam/explain-analyzer) [![GitHub stars](https://img.shields.io/github/stars/Preetam/explain-analyzer?style=flat)](https://github.com/Preetam/explain-analyzer/stargazers) - A web-based analyzer of `EXPLAIN FORMAT=JSON` output, providing comments, scalability analysis and permalinks for saved samples.
- [mysql-statsd](https://github.com/db-art/mysql-statsd) [![GitHub stars](https://img.shields.io/github/stars/db-art/mysql-statsd?style=flat)](https://github.com/db-art/mysql-statsd/stargazers) - A Python daemon to collect information from MySQL and send it via StatsD to Graphite.
- [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) [![GitHub stars](https://img.shields.io/github/stars/major/MySQLTuner-perl?style=flat)](https://github.com/major/MySQLTuner-perl/stargazers) - A script that allows you to review a MySQL installation quickly and make adjustments to increase performance and stability.
- [Prometheus](https://github.com/prometheus/prometheus) [![GitHub stars](https://img.shields.io/github/stars/prometheus/prometheus?style=flat)](https://github.com/prometheus/prometheus/stargazers)/[mysqld_exporter](https://github.com/prometheus/mysqld_exporter) [![GitHub stars](https://img.shields.io/github/stars/prometheus/mysqld_exporter?style=flat)](https://github.com/prometheus/mysqld_exporter/stargazers) - Time series database for real-time monitoring and alerting.
- [pstop](https://github.com/sjmudd/ps-top) [![GitHub stars](https://img.shields.io/github/stars/sjmudd/ps-top?style=flat)](https://github.com/sjmudd/ps-top/stargazers) - a top-like program for MySQL, collecting, aggregating and displaying information from performance_schema.
- [ReliaDB EXPLAIN Analyzer](https://github.com/Mughees52/mysql-explain-analyzer) [![GitHub stars](https://img.shields.io/github/stars/Mughees52/mysql-explain-analyzer?style=flat)](https://github.com/Mughees52/mysql-explain-analyzer/stargazers) - a browser-based MySQL and MariaDB EXPLAIN visualizer with issue detection, index recommendations, and query rewrites. 100% client-side.
- [Wireshark](https://gitlab.com/wireshark/wireshark/) - a protocol analyzer that can decode the MySQL protocol.
- [Dolphie](https://github.com/charles-001/dolphie) [![GitHub stars](https://img.shields.io/github/stars/charles-001/dolphie?style=flat)](https://github.com/charles-001/dolphie/stargazers) - a modern terminal tool for real-time analytics into MySQL/MariaDB & ProxySQL
- [sql-tap](https://github.com/mickamy/sql-tap) [![GitHub stars](https://img.shields.io/github/stars/mickamy/sql-tap?style=flat)](https://github.com/mickamy/sql-tap/stargazers) - Real-time SQL traffic viewer.

## Backup

*Backup/restore/recovery tools*

- [Databasus](https://github.com/databasus/databasus) [![GitHub stars](https://img.shields.io/github/stars/databasus/databasus?style=flat)](https://github.com/databasus/databasus/stargazers) - tool for scheduled MySQL backups via web UI with external storages (local, S3, FTP, Google Drive, etc.), notifications (webhook, Discord, Slack, etc.) and team management.
- [Dumpling](https://github.com/pingcap/tidb/tree/master/dumpling) [![GitHub stars](https://img.shields.io/github/stars/pingcap/tidb/tree/master/dumpling?style=flat)](https://github.com/pingcap/tidb/tree/master/dumpling/stargazers) - Logical, parallel backup/dumper tool for MySQL/TiDB written in GoLang - support csv format output and integrated as library
- [MyDumper](https://github.com/mydumper/mydumper) [![GitHub stars](https://img.shields.io/github/stars/mydumper/mydumper?style=flat)](https://github.com/mydumper/mydumper/stargazers) - Logical, parallel backup/dumper tool for MySQL
- [Percona Xtrabackup](https://github.com/percona/percona-xtrabackup) [![GitHub stars](https://img.shields.io/github/stars/percona/percona-xtrabackup?style=flat)](https://github.com/percona/percona-xtrabackup/stargazers) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.
- [Portabase](https://github.com/Portabase/portabase) [![GitHub stars](https://img.shields.io/github/stars/Portabase/portabase?style=flat)](https://github.com/Portabase/portabase/stargazers) - Agent-based platform for MySQL backups and restores with decentralized execution and centralized orchestration.

## Benchmarking

*Tools to stress your servers*

- [HammerDB](https://github.com/TPC-Council/HammerDB) [![GitHub stars](https://img.shields.io/github/stars/TPC-Council/HammerDB?style=flat)](https://github.com/TPC-Council/HammerDB/stargazers) - An open-source database benchmark for MySQL/MariaDB and other open source and commercial databases.
- [go-tpc](https://github.com/pingcap/go-tpc) [![GitHub stars](https://img.shields.io/github/stars/pingcap/go-tpc?style=flat)](https://github.com/pingcap/go-tpc/stargazers) - A golang port of [TPCC](http://www.tpc.org/tpcc/) and [TPCH](http://www.tpc.org/tpch/) benchmark for MySQL.
- [iibench-mysql](https://github.com/tmcallaghan/iibench-mysql) [![GitHub stars](https://img.shields.io/github/stars/tmcallaghan/iibench-mysql?style=flat)](https://github.com/tmcallaghan/iibench-mysql/stargazers) - Java based version of the Index Insertion Benchmark for MySQL/Percona/MariaDB.
- [Sysbench](https://github.com/akopytov/sysbench) [![GitHub stars](https://img.shields.io/github/stars/akopytov/sysbench?style=flat)](https://github.com/akopytov/sysbench/stargazers) - a modular, cross-platform and multi-threaded benchmark tool.
- [TPCC-MySQL](https://github.com/Percona-Lab/tpcc-mysql) [![GitHub stars](https://img.shields.io/github/stars/Percona-Lab/tpcc-mysql?style=flat)](https://github.com/Percona-Lab/tpcc-mysql/stargazers) (archived) - A port of the popular [TPCC](http://www.tpc.org/tpcc/) benchmark for MySQL.

## Binlog-Replication

- [DM](https://github.com/pingcap/tiflow) [![GitHub stars](https://img.shields.io/github/stars/pingcap/tiflow?style=flat)](https://github.com/pingcap/tiflow/stargazers) - A High-Availability data migration platform which supports migrating data from MySQL/MariaDB to TiDB and merging shard tables
- [Kingbus](https://github.com/flike/kingbus) [![GitHub stars](https://img.shields.io/github/stars/flike/kingbus?style=flat)](https://github.com/flike/kingbus/stargazers) - A distributed MySQL binlog storage system built on Raft
- [mysql-ripple](https://github.com/google/mysql-ripple) [![GitHub stars](https://img.shields.io/github/stars/google/mysql-ripple?style=flat)](https://github.com/google/mysql-ripple/stargazers) (archived) - Ripple, a server that can serve as a middleman in MySQL replication

## ChatOps

*Scripts integrated into chat rooms*

- [Hubot MySQL ChatOps](https://github.com/samlambert/hubot-mysql-chatops) [![GitHub stars](https://img.shields.io/github/stars/samlambert/hubot-mysql-chatops?style=flat)](https://github.com/samlambert/hubot-mysql-chatops/stargazers)

## Configuration

*MySQL sample configuration and advisors*

- [mysql-compatibility-config](https://github.com/morgo/mysql-compatibility-config) [![GitHub stars](https://img.shields.io/github/stars/morgo/mysql-compatibility-config?style=flat)](https://github.com/morgo/mysql-compatibility-config/stargazers) - make MySQL configuration behave more like newer (or older) releases of MySQL.

## Connectors

*MySQL connectors for various programming languages*

- [ballerinax/mysql](https://github.com/ballerina-platform/module-ballerinax-mysql) [![GitHub stars](https://img.shields.io/github/stars/ballerina-platform/module-ballerinax-mysql?style=flat)](https://github.com/ballerina-platform/module-ballerinax-mysql/stargazers) - Official Ballerina connector for MySQL.
- [DBD::MariaDB](https://github.com/perl5-dbi/DBD-MariaDB) [![GitHub stars](https://img.shields.io/github/stars/perl5-dbi/DBD-MariaDB?style=flat)](https://github.com/perl5-dbi/DBD-MariaDB/stargazers) - MariaDB and MySQL driver for the Perl5 Database Interface.
- [DBD::mysql](https://github.com/perl5-dbi/DBD-mysql) [![GitHub stars](https://img.shields.io/github/stars/perl5-dbi/DBD-mysql?style=flat)](https://github.com/perl5-dbi/DBD-mysql/stargazers) - MySQL driver for the Perl5 Database Interface.
- [go-sql-driver](https://github.com/go-sql-driver/mysql) [![GitHub stars](https://img.shields.io/github/stars/go-sql-driver/mysql?style=flat)](https://github.com/go-sql-driver/mysql/stargazers) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
- [libAttachSQL](https://github.com/libattachsql/libattachsql) [![GitHub stars](https://img.shields.io/github/stars/libattachsql/libattachsql?style=flat)](https://github.com/libattachsql/libattachsql/stargazers) - libAttachSQL is a lightweight, non-blocking C API for MySQL servers.
- [MariaDB Connector/J](https://github.com/mariadb-corporation/mariadb-connector-j) [![GitHub stars](https://img.shields.io/github/stars/mariadb-corporation/mariadb-connector-j?style=flat)](https://github.com/mariadb-corporation/mariadb-connector-j/stargazers) - LGPL-licensed MariaDB Client Library for Java Applications.
- [mex-mariadb](https://github.com/markuman/mex-mariadb) [![GitHub stars](https://img.shields.io/github/stars/markuman/mex-mariadb?style=flat)](https://github.com/markuman/mex-mariadb/stargazers) - MIT licensed MariaDB/MySQL Client Library for GNU Octave and Matlab.
- [MySQL C API](https://dev.mysql.com/downloads/c-api/) - Official C driver for MySQL.
- [MySQL Connector/C++](https://github.com/mysql/mysql-connector-cpp) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-connector-cpp?style=flat)](https://github.com/mysql/mysql-connector-cpp/stargazers) - Official C/C++ driver for MySQL.
- [MySQL Connector/J](https://github.com/mysql/mysql-connector-j) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-connector-j?style=flat)](https://github.com/mysql/mysql-connector-j/stargazers) - a standardized database driver for the Java platforms and development.
- [MySQL Connector/NET](https://github.com/mysql/mysql-connector-net) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-connector-net?style=flat)](https://github.com/mysql/mysql-connector-net/stargazers) - a standardized database driver for .Net platforms and development.
- [MySQL Connector/Node.js](https://github.com/mysql/mysql-connector-nodejs) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-connector-nodejs?style=flat)](https://github.com/mysql/mysql-connector-nodejs/stargazers) - Official Node.js driver for MySQL.
- [MySQL Connector/Python](https://github.com/mysql/mysql-connector-python) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-connector-python?style=flat)](https://github.com/mysql/mysql-connector-python/stargazers) - a standardized database driver for Python platforms and development.
- [mysqlclient-python](https://github.com/PyMySQL/mysqlclient) [![GitHub stars](https://img.shields.io/github/stars/PyMySQL/mysqlclient?style=flat)](https://github.com/PyMySQL/mysqlclient/stargazers) - MySQL database connector for Python.
- [node-mysql](https://github.com/mysqljs/mysql) [![GitHub stars](https://img.shields.io/github/stars/mysqljs/mysql?style=flat)](https://github.com/mysqljs/mysql/stargazers) - A pure Nodejs Javascript client implementing the MySQL protocol.
- [PHP mysqlnd](https://www.php.net/manual/en/book.mysqlnd.php) - MySQL native driver for PHP.
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) [![GitHub stars](https://img.shields.io/github/stars/PyMySQL/PyMySQL?style=flat)](https://github.com/PyMySQL/PyMySQL/stargazers) - MySQL database connector for Python.
- [Ruby Mysql2 gem](https://github.com/brianmario/mysql2) [![GitHub stars](https://img.shields.io/github/stars/brianmario/mysql2?style=flat)](https://github.com/brianmario/mysql2/stargazers) - MySQL driver for Ruby and Rails projects.
- [MyZql](https://github.com/speed2exe/myzql) [![GitHub stars](https://img.shields.io/github/stars/speed2exe/myzql?style=flat)](https://github.com/speed2exe/myzql/stargazers) - MySQL and MariaDB driver in native Zig.
- [wtx](https://github.com/c410-f3r/wtx) [![GitHub stars](https://img.shields.io/github/stars/c410-f3r/wtx?style=flat)](https://github.com/c410-f3r/wtx/stargazers) - Client for MySQL/MariaDB/Percona written in Rust

## Deployment

*MySQL deployment tools*

- [MariaDB4j](https://github.com/MariaDB4j/MariaDB4j) [![GitHub stars](https://img.shields.io/github/stars/MariaDB4j/MariaDB4j?style=flat)](https://github.com/MariaDB4j/MariaDB4j/stargazers) - A Java launcher to run MariaDB without installation or external dependencies.


## Development

*Tools to support MySQL-related development*

- [Flywaydb](https://github.com/flyway/flyway) [![GitHub stars](https://img.shields.io/github/stars/flyway/flyway?style=flat)](https://github.com/flyway/flyway/stargazers) - Database migrations; Evolve your database schema easily and reliably across all your instances
- [dbsafe](https://github.com/nethalo/dbsafe) [![GitHub stars](https://img.shields.io/github/stars/nethalo/dbsafe?style=flat)](https://github.com/nethalo/dbsafe/stargazers) - Pre-execution safety analysis for MySQL DDL/DML operations
- [Liquibase](https://github.com/liquibase/liquibase) [![GitHub stars](https://img.shields.io/github/stars/liquibase/liquibase?style=flat)](https://github.com/liquibase/liquibase/stargazers) - Source control for your database
- [Shift](https://github.com/square/shift) [![GitHub stars](https://img.shields.io/github/stars/square/shift?style=flat)](https://github.com/square/shift/stargazers) - An application that helps you run schema migrations on MySQL databases
- [Skeema](https://github.com/skeema/skeema) [![GitHub stars](https://img.shields.io/github/stars/skeema/skeema?style=flat)](https://github.com/skeema/skeema/stargazers) - Declarative pure-SQL schema management system for MySQL and MariaDB, with support for sharding and external online schema change tools
- [SQLE](https://github.com/actiontech/sqle/blob/main/README_en.md) [![GitHub stars](https://img.shields.io/github/stars/actiontech/sqle/blob/main/README_en.md?style=flat)](https://github.com/actiontech/sqle/blob/main/README_en.md/stargazers) - SQLE is a SQL audit platform for DBA or developer
- [Test database](https://github.com/datacharmer/test_db) [![GitHub stars](https://img.shields.io/github/stars/datacharmer/test_db?style=flat)](https://github.com/datacharmer/test_db/stargazers) - A sample MySQL database with an integrated test suite, used to test applications and servers
- [cover_me](https://github.com/verizonconnect/database-development) [![GitHub stars](https://img.shields.io/github/stars/verizonconnect/database-development?style=flat)](https://github.com/verizonconnect/database-development/stargazers) - code coverage tool for mysql stored procedures and functions

## GUI

*GUI frontends & applications*

- [Adminer](https://github.com/vrana/adminer/) [![GitHub stars](https://img.shields.io/github/stars/vrana/adminer/?style=flat)](https://github.com/vrana/adminer//stargazers) - Database management in a single PHP file.
- [DBeaver](https://github.com/dbeaver/dbeaver/) [![GitHub stars](https://img.shields.io/github/stars/dbeaver/dbeaver/?style=flat)](https://github.com/dbeaver/dbeaver//stargazers) - A cross-platform SQL and NoSQL database client.
- [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) [![GitHub stars](https://img.shields.io/github/stars/HeidiSQL/HeidiSQL?style=flat)](https://github.com/HeidiSQL/HeidiSQL/stargazers) - MySQL GUI frontend for Windows.
- [ILLA Cloud](https://github.com/illacloud/illa-builder) [![GitHub stars](https://img.shields.io/github/stars/illacloud/illa-builder?style=flat)](https://github.com/illacloud/illa-builder/stargazers) - Low-code internal tool builder integrated with Mysql, can be used as GUI for Mysql. 
- [mycli](https://github.com/dbcli/mycli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/mycli?style=flat)](https://github.com/dbcli/mycli/stargazers) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
- [MySQL Shell](https://github.com/mysql/mysql-shell/) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-shell/?style=flat)](https://github.com/mysql/mysql-shell//stargazers) - Advanced client and code editor for MySQL that supports development and administration for the MySQL Server and MySQL InnoDB cluster (AdminAPI) with an interactive JavaScript, Python, or SQL interface.
- [MySQL Workbench](https://github.com/mysql/mysql-workbench) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-workbench?style=flat)](https://github.com/mysql/mysql-workbench/stargazers) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
- [Ocelot GUI](https://github.com/ocelot-inc/ocelotgui) [![GitHub stars](https://img.shields.io/github/stars/ocelot-inc/ocelotgui?style=flat)](https://github.com/ocelot-inc/ocelotgui/stargazers) - GUI client for MySQL or MariaDB, including debugger.
- [OmniDB: Web tool for database management](https://github.com/OmniDB/OmniDB) [![GitHub stars](https://img.shields.io/github/stars/OmniDB/OmniDB?style=flat)](https://github.com/OmniDB/OmniDB/stargazers)
- [Percona Monitoring and Management](https://github.com/percona/pmm) [![GitHub stars](https://img.shields.io/github/stars/percona/pmm?style=flat)](https://github.com/percona/pmm/stargazers) - An open-source platform for managing and monitoring MySQL performance.
- [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) [![GitHub stars](https://img.shields.io/github/stars/phpmyadmin/phpmyadmin?style=flat)](https://github.com/phpmyadmin/phpmyadmin/stargazers) - a free software tool written in PHP, intended to handle the administration of MySQL over the Web.
- [pspg](https://github.com/okbob/pspg) [![GitHub stars](https://img.shields.io/github/stars/okbob/pspg?style=flat)](https://github.com/okbob/pspg/stargazers) - provides a pager with enhanced visualization and navigation for tabular data. Originally implemented for PostgreSQL, but also supports MySQL.
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) [![GitHub stars](https://img.shields.io/github/stars/Sequel-Ace/Sequel-Ace?style=flat)](https://github.com/Sequel-Ace/Sequel-Ace/stargazers) - a Mac database management application for working with MySQL databases.
- [TablePro](https://github.com/TableProApp/TablePro) [![GitHub stars](https://img.shields.io/github/stars/TableProApp/TablePro?style=flat)](https://github.com/TableProApp/TablePro/stargazers) - Native macOS client for MySQL and many other databases with inline editing, SSH tunneling, and AI assistant. Free and open-source.
- [SQLyog Community edition](https://github.com/webyog/sqlyog-community) [![GitHub stars](https://img.shields.io/github/stars/webyog/sqlyog-community?style=flat)](https://github.com/webyog/sqlyog-community/stargazers) - SQLyog Community edition. For Windows, works fine under wine in Mac and Linux
- [squix](https://github.com/eduardofuncao/squix) [![GitHub stars](https://img.shields.io/github/stars/eduardofuncao/squix?style=flat)](https://github.com/eduardofuncao/squix/stargazers) - SQL command-line client with query management and interactive results.
- [WebDB](https://github.com/WebDB-App/app) [![GitHub stars](https://img.shields.io/github/stars/WebDB-App/app?style=flat)](https://github.com/WebDB-App/app/stargazers) – Open Source and Efficient Database IDE. Featuring Easy server connection, Modern ERD, Intelligent data generator, AI assistant, NoSQL structure manager, Time machine and Powerful query editor

## HA

*High availability solutions*

- [Galera Cluster](https://github.com/codership/galera) [![GitHub stars](https://img.shields.io/github/stars/codership/galera?style=flat)](https://github.com/codership/galera/stargazers) - a true Multimaster Cluster based on synchronous replication.
- [mha4mysql-node](https://github.com/yoshinorim/mha4mysql-node) [![GitHub stars](https://img.shields.io/github/stars/yoshinorim/mha4mysql-node?style=flat)](https://github.com/yoshinorim/mha4mysql-node/stargazers) and [mha4mysql-manager](https://github.com/yoshinorim/mha4mysql-manager) [![GitHub stars](https://img.shields.io/github/stars/yoshinorim/mha4mysql-manager?style=flat)](https://github.com/yoshinorim/mha4mysql-manager/stargazers) (both unmaintained) - Master High Availability Manager and tools for MySQL.
- [Orchestrator](https://github.com/openark/orchestrator) [![GitHub stars](https://img.shields.io/github/stars/openark/orchestrator?style=flat)](https://github.com/openark/orchestrator/stargazers) (archived) - MySQL replication topology management and High Availability solution.
- [Percona Replication Manager](https://github.com/percona/replication-manager) [![GitHub stars](https://img.shields.io/github/stars/percona/replication-manager?style=flat)](https://github.com/percona/replication-manager/stargazers) - Asynchronous MySQL replication manager agent for Pacemaker. Supports file and GTID based replication, geo-distributed clusters using booth.
- [replication-manager](https://github.com/signal18/replication-manager) [![GitHub stars](https://img.shields.io/github/stars/signal18/replication-manager?style=flat)](https://github.com/signal18/replication-manager/stargazers) - a high availability solution to manage MariaDB 10.x and MySQL & Percona Server 5.7 GTID replication topologies.

## MCP

- [MCP MariaDB Server](https://github.com/MariaDB/mcp) [![GitHub stars](https://img.shields.io/github/stars/MariaDB/mcp?style=flat)](https://github.com/MariaDB/mcp/stargazers) - the official MariaDB MCP server.
- [MySQL MCP Server](https://github.com/askdba/mysql-mcp-server) [![GitHub stars](https://img.shields.io/github/stars/askdba/mysql-mcp-server?style=flat)](https://github.com/askdba/mysql-mcp-server/stargazers) - Advanced MCP server exposing MySQL via the Model Context Protocol
- [TiDB MCP Server](https://pingcap.github.io/ai/integrations/tidb-mcp-server/) - MCP Server for TiDB.

## Proxy

*Proxies to MySQL*

- [MySQL Router](https://dev.mysql.com/doc/mysql-router/en/) - MySQL Router is part of InnoDB cluster, and is a lightweight middleware that provides transparent routing between your application and back-end MySQL Servers.
- [ProxySQL](https://github.com/sysown/proxysql) [![GitHub stars](https://img.shields.io/github/stars/sysown/proxysql?style=flat)](https://github.com/sysown/proxysql/stargazers) - High performance proxy for MySQL.

## Replication

*Replication related software*

* [data-diff](https://github.com/datafold/data-diff) [![GitHub stars](https://img.shields.io/github/stars/datafold/data-diff?style=flat)](https://github.com/datafold/data-diff/stargazers) (archived) - Command-line tool and Python library to efficiently diff rows across two different databases.


## Schema

*Add-on schemas*

- [common_schema](https://github.com/shlomi-noach/common_schema) [![GitHub stars](https://img.shields.io/github/stars/shlomi-noach/common_schema?style=flat)](https://github.com/shlomi-noach/common_schema/stargazers) - DBA's framework for MySQL, providing a function library, views library and QueryScript interpreter.
- [sys](https://github.com/mysql/mysql-sys) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-sys?style=flat)](https://github.com/mysql/mysql-sys/stargazers) (archived) - A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage. See [sys schema docs](https://dev.mysql.com/doc/refman/8.4/en/sys-schema.html)


## Security

*Tools that prevents leaking of sensitive data from database (encryption, masking and tokenization, honey-pots, etc)*

- [Acra](https://github.com/cossacklabs/acra) [![GitHub stars](https://img.shields.io/github/stars/cossacklabs/acra?style=flat)](https://github.com/cossacklabs/acra/stargazers) - SQL database protection suite: strong selective encryption, SQL injections prevention, intrusion detection system.
- [myanon](https://github.com/ppomes/myanon) [![GitHub stars](https://img.shields.io/github/stars/ppomes/myanon?style=flat)](https://github.com/ppomes/myanon/stargazers) - Streaming anonymizer for MySQL dump files, reading mysqldump output from stdin and writing anonymized data to stdout. Supports deterministic hashing, fixed values, JSON field anonymization, and Python extensions.
- [myldapsync](https://github.com/6eh01der/myldapsync) [![GitHub stars](https://img.shields.io/github/stars/6eh01der/myldapsync?style=flat)](https://github.com/6eh01der/myldapsync/stargazers) - Synchronize MySQL or MariaDB users with users in an LDAP directory.

## Server

*MySQL server flavors*

- [MariaDB](https://github.com/MariaDB/server) [![GitHub stars](https://img.shields.io/github/stars/MariaDB/server?style=flat)](https://github.com/MariaDB/server/stargazers) - Community developed fork of MySQL server.
- [MySQL Server & MySQL Cluster](https://github.com/mysql/mysql-server) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-server?style=flat)](https://github.com/mysql/mysql-server/stargazers) - Official Oracle's MySQL server & MySQL Cluster distribution.
- [MyVector](https://github.com/askdba/myvector) [![GitHub stars](https://img.shields.io/github/stars/askdba/myvector?style=flat)](https://github.com/askdba/myvector/stargazers) - Native vector search plugin for MySQL, shipped as a server plugin.
- [Percona Server](https://github.com/percona/percona-server) [![GitHub stars](https://img.shields.io/github/stars/percona/percona-server?style=flat)](https://github.com/percona/percona-server/stargazers) - An enhanced, drop-in MySQL replacement.
- [TiDB](https://github.com/pingcap/tidb) [![GitHub stars](https://img.shields.io/github/stars/pingcap/tidb?style=flat)](https://github.com/pingcap/tidb/stargazers) - A distributed HTAP database compatible with the MySQL protocol.

## Sharding

*Sharding solutions/frameworks*

- [Jetpants](https://github.com/tumblr/jetpants) [![GitHub stars](https://img.shields.io/github/stars/tumblr/jetpants?style=flat)](https://github.com/tumblr/jetpants/stargazers) - An automation suite for managing large range sharding clusters, by Tumblr.
- [Vitess](https://github.com/vitessio/vitess) [![GitHub stars](https://img.shields.io/github/stars/vitessio/vitess?style=flat)](https://github.com/vitessio/vitess/stargazers) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.


## Toolkits

*Toolkits, general purpose scripts*

- [gh-ost](https://github.com/github/gh-ost/) [![GitHub stars](https://img.shields.io/github/stars/github/gh-ost/?style=flat)](https://github.com/github/gh-ost//stargazers) - GitHub's online schema migration for MySQL.
- [go-mysql](https://github.com/go-mysql-org/go-mysql) [![GitHub stars](https://img.shields.io/github/stars/go-mysql-org/go-mysql?style=flat)](https://github.com/go-mysql-org/go-mysql/stargazers) - A pure go library to handle MySQL network protocol and replication.
- [MySQL Utilities](https://github.com/mysql/mysql-utilities) [![GitHub stars](https://img.shields.io/github/stars/mysql/mysql-utilities?style=flat)](https://github.com/mysql/mysql-utilities/stargazers) (deprecated) - a collection of command-line utilities, written in Python, that are used for maintaining and administering MySQL servers, either individually, or within Replication hierarchies.
- [Percona Toolkit](https://github.com/percona/percona-toolkit) [![GitHub stars](https://img.shields.io/github/stars/percona/percona-toolkit?style=flat)](https://github.com/percona/percona-toolkit/stargazers) - a collection of advanced command-line tools to perform a variety of MySQL server and system tasks that are too difficult or complex to perform manually.
- [sql-splitter](https://github.com/HelgeSverre/sql-splitter) [![GitHub stars](https://img.shields.io/github/stars/HelgeSverre/sql-splitter?style=flat)](https://github.com/HelgeSverre/sql-splitter/stargazers) - High-performance CLI for splitting, merging, converting, validating, and sampling mysqldump files.
- [Swoof](https://github.com/StirlingMarketingGroup/swoof) [![GitHub stars](https://img.shields.io/github/stars/StirlingMarketingGroup/swoof?style=flat)](https://github.com/StirlingMarketingGroup/swoof/stargazers) - Ultra fast MySQL table importer that stages swaps through temporary tables and supports file/clipboard targets.
- [UnDROP](https://github.com/twindb/undrop-for-innodb) [![GitHub stars](https://img.shields.io/github/stars/twindb/undrop-for-innodb?style=flat)](https://github.com/twindb/undrop-for-innodb/stargazers) (archived) - a tool to recover data from dropped or corrupted InnoDB tables.

# Resources

*At this stage "resources" will not include websites, blogs, slides, presentation videos, etc. in fear of list size*

## e-books

*e-books as well as relevant materials on and around MySQL*

- [Database Systems Lecture Notes](http://spots.augusta.edu/caubert/db/ln/) - lecture notes on Database Systems (available in pdf, html, odt and markdown) including a Chapter on SQL that covers basic set-up, exercises and problems.
- [SQL-exercise](https://github.com/XD-DENG/SQL-exercise) [![GitHub stars](https://img.shields.io/github/stars/XD-DENG/SQL-exercise?style=flat)](https://github.com/XD-DENG/SQL-exercise/stargazers) - contains several SQL exercises, including the schema description figure, SQL code to build schema, questions and solutions in SQL. Based on wikibook [SQL Exercises](https://en.wikibooks.org/wiki/SQL_Exercises).

## Incubating

Projects that are known to be non-production and yet have either traction or substance that warrants exposure.

- [VillageSQL](https://github.com/villagesql/villagesql-server) [![GitHub stars](https://img.shields.io/github/stars/villagesql/villagesql-server?style=flat)](https://github.com/villagesql/villagesql-server/stargazers) - A drop-in replacement for MySQL with extensions for the agentic AI era.
