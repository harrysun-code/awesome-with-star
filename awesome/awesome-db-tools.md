# Database Tools

[![GitHub stars](https://img.shields.io/github/stars/mgramin/awesome-db-tools?style=flat)](https://github.com/mgramin/awesome-db-tools/stargazers)

# Awesome Database Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Community driven list of database tools

Here we will collect information about awesome useful and awesome experimental tools that simplify working with databases for DBA, DevOps, Developers and mere mortals.

Feel free to add information about your own db-tools or your favorite third-party db-tools.

For updates on `awesome-db-tools` and thoughts/news about databases/tools/SQL follow me at [@GraminMaksim](https://twitter.com/GraminMaksim)

## Contents
- [IDE](#ide)
- [GUI](#gui)
- [CLI](#cli)
- [Schema](#schema)
  - [Changes](#changes)
  - [Code generation](#code-generation)
  - [Diagrams](#diagrams)
  - [Documentations](#documentations)
  - [Design](#design)
  - [Samples](#samples)
- [API](#api)
- [Application platforms](#application-platforms)
- [Backup](#backup)
- [Cloning](#cloning)
- [Monitoring/Statistics/Perfomance](#monitoringstatisticsperfomance)
  - [Prometheus](#prometheus)
  - [Zabbix](#zabbix)
- [Testing](#testing)
- [HA/Failover/Sharding](#hafailoversharding)
- [Kubernetes](#kubernetes)
- [Configuration Tuning](#configuration-tuning)
- [DevOps](#devops)
- [Reporting](#reporting)
- [Distributions](#distributions)
- [Security](#security)
- [SQL](#sql)
  - [Analyzers](#analyzers)
  - [Code Generators](#code-generators)
  - [Extensions](#extensions)
  - [Frameworks](#frameworks)
  - [Formatters](#formatters)
  - [Games](#games)
  - [Parsers](#parsers)
  - [Über SQL](#über-sql)
  - [Language Server Protocol](#language-server-protocol)
  - [Learning](#learning)
  - [Plan](#plan)
  - [Scripts](#scripts)
- [Data](#data)
  - [Catalog](#catalog)
  - [Lineage](#lineage) 
  - [Generation/Masking/Subsetting](#generationmaskingsubsetting)
  - [Data Profilers](#data-profilers)
  - [Replication](#replication) 
  - [Compare](#compare) 
- [Papers](#papers)
- [Machine Learning](#machine-learning)

## IDE
- [AnySQL Maestro](https://www.sqlmaestro.com/products/anysql/maestro) - Premier multi-purpose admin tool for database management, control and development.
- [Aqua Data Studio](https://www.aquafold.com/aquadatastudio) - Productivity software for Database Developers, DBAs, and Analysts.
- [Coginiti Pro](https://www.coginiti.co/products/coginiti-pro/) - Modern IDE for analyst and analytics engineers with proweful script and grid functionality.
- [Database .net](http://fishcodelib.com/Database.htm) - Multiple database management tool with support for 20+ databases.
- [Database Workbench](https://www.upscene.com/database_workbench/) - Complete IDE for database design, development and testing for Oracle, SQL Server, PostgreSQL, MySQL, MariaDB, Firebird, InterBase, SQLite and NexusDB.
- [DataGrip](https://www.jetbrains.com/datagrip) - Cross-Platform IDE for Databases & SQL by JetBrains.
- [DataStation](https://github.com/multiprocessio/datastation) [![GitHub stars](https://img.shields.io/github/stars/multiprocessio/datastation?style=flat)](https://github.com/multiprocessio/datastation/stargazers) - Easily query, script, and visualize data from every database, file, and API.
- [DBeaver](https://github.com/dbeaver/dbeaver) [![GitHub stars](https://img.shields.io/github/stars/dbeaver/dbeaver?style=flat)](https://github.com/dbeaver/dbeaver/stargazers) - Free universal database manager and SQL client.
- [dbForge Edge](https://www.devart.com/dbforge/edge/) - Multidatabase solution for DB development, design, management, and administration of MySQL, MariaDB, SQL Server, Oracle, PostgreSQL databases, and various cloud services.
- [dbForge Studio for MySQL](https://www.devart.com/dbforge/mysql/studio) - Universal IDE for MySQL and MariaDB database development, management, and administration.
- [dbForge Studio for Oracle](https://www.devart.com/dbforge/oracle/studio) - Powerful IDE for Oracle management, administration, and development.
- [dbForge Studio for PostgreSQL](https://www.devart.com/dbforge/postgresql/studio) - GUI tool for managing and developing databases and objects.
- [dbForge Studio for SQL Server](https://www.devart.com/dbforge/sql/studio) - Powerful integrated development environment for SQL Server development, management, administration, data analysis, and reporting.
- [DBHawk](https://www.datasparc.com/) - Datasparc offers database security, database management, database governance and data analytics - all in one solution.
- [dbKoda](https://github.com/SouthbankSoftware/dbkoda) [![GitHub stars](https://img.shields.io/github/stars/SouthbankSoftware/dbkoda?style=flat)](https://github.com/SouthbankSoftware/dbkoda/stargazers) - Modern (JavaScript/Electron framework), open source IDE for MongoDB. It has features to support development, administration and performance tuning on MongoDB databases.
- [IBExpert](http://www.ibexpert.net/ibe) - Comprehensive GUI tool for Firebird and InterBase.
- [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) [![GitHub stars](https://img.shields.io/github/stars/HeidiSQL/HeidiSQL?style=flat)](https://github.com/HeidiSQL/HeidiSQL/stargazers) - A lightweight client for managing MySQL, MSSQL and PostgreSQL, written in Delphi.
- [Kangaroo](https://github.com/dbkangaroo/kangaroo) [![GitHub stars](https://img.shields.io/github/stars/dbkangaroo/kangaroo?style=flat)](https://github.com/dbkangaroo/kangaroo/stargazers) - A AI-powered SQL client and admin tool for popular databases(SQLite / MySQL / PostgreSQL / etc) on Windows / macOS / Linux, support table design, query, model, sync, export/import etc, focus on comfortable, fun and developer friendly.
- [KeepTool](https://keeptool.com) - A professional suite of tools for Oracle Database developers, administrators and advanced application users.
- [MySQL Workbench](https://www.mysql.com/products/workbench) - Unified visual tool for database architects, developers, and DBAs.
- [Navicat](https://www.navicat.com/en/products#navicat) - A database development tool that allows you to simultaneously connect to MySQL, MariaDB, SQL Server, Oracle, PostgreSQL, and SQLite databases from a single application.
- [Oracle SQL Developer](http://www.oracle.com/technetwork/developer-tools/sql-developer) - Free, integrated development environment that simplifies the development and management of Oracle Database in both traditional and Cloud deployments.
- [pgAdmin](https://www.pgadmin.org) - The most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world.
- [pgAdmin3](https://www.bigsql.org/pgadmin3) - Long Term Support for pgAdmin3.
- [PL/SQL Developer](https://www.allroundautomations.com/products/pl-sql-developer) - IDE that is specifically targeted at the development of stored program units for Oracle Databases.
- [PostgreSQL Maestro](https://www.sqlmaestro.com/products/postgresql/maestro) - Complete and powerful database management, admin and development tool for PostgreSQL.
- [Querybook](https://github.com/pinterest/querybook) [![GitHub stars](https://img.shields.io/github/stars/pinterest/querybook?style=flat)](https://github.com/pinterest/querybook/stargazers) - Pinterest open-source Big Data Querying UI, combining collocated table metadata and a simple notebook IDE interface.
- [Slashbase](https://github.com/slashbaseide/slashbase) [![GitHub stars](https://img.shields.io/github/stars/slashbaseide/slashbase?style=flat)](https://github.com/slashbaseide/slashbase/stargazers) - The open-source collaborative IDE for your databases. Connect to your database, browse data, run a bunch of SQL commands or share SQL queries with your team, right from your browser.
- [Sql Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms) - Integrated environment for managing any SQL infrastructure, for SQL Server and Azure SQL Databases.
- [Toad](https://www.quest.com/toad/) - Premier database solution for developers, admins and data analysts. Manage complex database changes with a single database management tool.
- [Toad Edge](https://www.toadworld.com/products/toad-edge) - Simplified database development tool for MySQL and PostgreSQL.
- [TOra](https://github.com/tora-tool/tora) [![GitHub stars](https://img.shields.io/github/stars/tora-tool/tora?style=flat)](https://github.com/tora-tool/tora/stargazers) - Open source SQL IDE for Oracle, MySQL and PostgreSQL dbs.
- [Valentina Studio](https://www.valentina-db.com/en/valentina-studio-overview) - Create, administer, query and explore Valentina DB, MySQL, MariaDB, PostgreSQL and SQLite databases for FREE.
- [WebDB](https://webdb.app) - Free Efficient Database IDE. Featuring Server Discovery, ERD, Data Generator, AI, NoSQL Structure Manager, Database Versioning and many more.


## GUI
- [Adminer](https://github.com/vrana/adminer) [![GitHub stars](https://img.shields.io/github/stars/vrana/adminer?style=flat)](https://github.com/vrana/adminer/stargazers) - Database management in a single PHP file.
- [Another Redis Desktop Manager](https://github.com/qishibo/AnotherRedisDesktopManager) [![GitHub stars](https://img.shields.io/github/stars/qishibo/AnotherRedisDesktopManager?style=flat)](https://github.com/qishibo/AnotherRedisDesktopManager/stargazers) - Free Open Source Redis Manager. Available on Mac, Linux, Windows, Homebrew, Snap, winget, and more.
- [Antares SQL](https://github.com/antares-sql/antares) [![GitHub stars](https://img.shields.io/github/stars/antares-sql/antares?style=flat)](https://github.com/antares-sql/antares/stargazers) - A modern, fast and productivity driven SQL client with a focus in UX. Available for Mac, Linux and Windows.
- [Azure Data Studio](https://github.com/microsoft/azuredatastudio) [![GitHub stars](https://img.shields.io/github/stars/microsoft/azuredatastudio?style=flat)](https://github.com/microsoft/azuredatastudio/stargazers) - A data management tool that enables working with SQL Server, PostgreSQL, Azure SQL DB and SQL DW from Windows, macOS and Linux.
- [Beekeeper Studio](https://github.com/beekeeper-studio/beekeeper-studio) [![GitHub stars](https://img.shields.io/github/stars/beekeeper-studio/beekeeper-studio?style=flat)](https://github.com/beekeeper-studio/beekeeper-studio/stargazers) - Open Source SQL Editor and Database Manager with a privacy commitment in their mission statement.
- [Clidey WhoDB](https://github.com/clidey/whodb) [![GitHub stars](https://img.shields.io/github/stars/clidey/whodb?style=flat)](https://github.com/clidey/whodb/stargazers) - A lightweight database explorer with next-gen UX for all SQL, NoSQL, Caches, and Queues.
- [DbGate](https://github.com/dbgate/dbgate) [![GitHub stars](https://img.shields.io/github/stars/dbgate/dbgate?style=flat)](https://github.com/dbgate/dbgate/stargazers) - Database manager for MySQL, PostgreSQL, SQL Server, MongoDB, SQLite and others. Runs under Windows, Linux, Mac or as web application.
- [DB Lens](https://github.com/dblens/app) [![GitHub stars](https://img.shields.io/github/stars/dblens/app?style=flat)](https://github.com/dblens/app/stargazers) - Open Source PostgreSQL GUI - Automatic ER diagrams, Internal DB Insights, Disk Utilisation, Performance Metrics, Index Usage, Sequential scan counts and more.
- [DbVisualizer](https://www.dbvis.com) - Universal database tool for developers, DBAs and analysts.
- [JackDB](https://www.jackdb.com) - Direct SQL access to all your data, no matter where it lives.
- [Jailer](https://github.com/Wisser/Jailer) [![GitHub stars](https://img.shields.io/github/stars/Wisser/Jailer?style=flat)](https://github.com/Wisser/Jailer/stargazers) - Database Subsetting and Relational Data Browsing Tool/Client.
- [Malewicz](https://github.com/mgramin/malewicz) [![GitHub stars](https://img.shields.io/github/stars/mgramin/malewicz?style=flat)](https://github.com/mgramin/malewicz/stargazers) - Yet Another WEB client for DB schema exploring and performance analysis, but originally created specifically for hacking and extending.
- [MissionKontrol](https://www.missionkontrol.io) - Modern drag & drop admin panel/client with full user permissions for non-technical users.
- [ocelotgui](https://github.com/ocelot-inc/ocelotgui) [![GitHub stars](https://img.shields.io/github/stars/ocelot-inc/ocelotgui?style=flat)](https://github.com/ocelot-inc/ocelotgui/stargazers) - For MySQL, MariaDB, and Tarantool. Developed for Linux but can run on Windows.
- [OmniDB](https://github.com/OmniDB/OmniDB) [![GitHub stars](https://img.shields.io/github/stars/OmniDB/OmniDB?style=flat)](https://github.com/OmniDB/OmniDB/stargazers) - Web tool for database management.
- [Pgweb](https://github.com/sosedoff/pgweb) [![GitHub stars](https://img.shields.io/github/stars/sosedoff/pgweb?style=flat)](https://github.com/sosedoff/pgweb/stargazers) - Web-based database browser for PostgreSQL, written in Go and works on macOS, Linux and Windows machines.
- [phpLiteAdmin](https://www.phpliteadmin.org) - Web-based SQLite database admin tool written in PHP with support for SQLite3 and SQLite2.
- [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) [![GitHub stars](https://img.shields.io/github/stars/phpmyadmin/phpmyadmin?style=flat)](https://github.com/phpmyadmin/phpmyadmin/stargazers) - A web interface for MySQL and MariaDB.
- [psequel](http://www.psequel.com) - Provides a clean and simple interface for you to perform common PostgreSQL tasks quickly.
- [PopSQL](https://popsql.com) - Modern, collaborative SQL editor for your team.
- [Postico](https://eggerapps.at/postico) - A Modern PostgreSQL Client for the Mac.
- [Robo 3T](https://github.com/Studio3T/robomongo) [![GitHub stars](https://img.shields.io/github/stars/Studio3T/robomongo?style=flat)](https://github.com/Studio3T/robomongo/stargazers) - Shell-centric cross-platform MongoDB management tool.
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) [![GitHub stars](https://img.shields.io/github/stars/Sequel-Ace/Sequel-Ace?style=flat)](https://github.com/Sequel-Ace/Sequel-Ace/stargazers) - MySQL/MariaDB database management for macOS.
- [Sequel Pro](https://github.com/sequelpro/sequelpro) [![GitHub stars](https://img.shields.io/github/stars/sequelpro/sequelpro?style=flat)](https://github.com/sequelpro/sequelpro/stargazers) - Fast, easy-to-use Mac database management application for working with MySQL & MariaDB databases.
- [SQLite Expert](http://www.sqliteexpert.com/index.html) - Graphical interface supports all SQLite features.
- [sqlite-tui](https://github.com/mathaou/sqlite-tui) [![GitHub stars](https://img.shields.io/github/stars/mathaou/sqlite-tui?style=flat)](https://github.com/mathaou/sqlite-tui/stargazers) - A TUI for viewing SQLite databases, written in Go.
- [sqlpad](https://github.com/rickbergfalk/sqlpad) [![GitHub stars](https://img.shields.io/github/stars/rickbergfalk/sqlpad?style=flat)](https://github.com/rickbergfalk/sqlpad/stargazers) - Web-based SQL editor run in your own private cloud.
- [SQLPro](https://www.macpostgresclient.com) - A simple, powerful PostgreSQL manager for macOS.
- [SQuirreL](https://sourceforge.net/projects/squirrel-sql) - Graphical SQL client written in Java that will allow you to view the structure of a JDBC compliant database, browse the data in tables, issue SQL commands etc.
- [SQLTools](https://github.com/mtxr/vscode-sqltools) [![GitHub stars](https://img.shields.io/github/stars/mtxr/vscode-sqltools?style=flat)](https://github.com/mtxr/vscode-sqltools/stargazers) - Database management for VSCode.
- [SQLyog](https://www.webyog.com/product/sqlyog) - The most complete and easy to use MySQL GUI.
- [Tabix](https://github.com/tabixio/tabix) [![GitHub stars](https://img.shields.io/github/stars/tabixio/tabix?style=flat)](https://github.com/tabixio/tabix/stargazers) - SQL Editor & Open source simple business intelligence for Clickhouse.
- [TablePlus](https://github.com/TablePlus/TablePlus) [![GitHub stars](https://img.shields.io/github/stars/TablePlus/TablePlus?style=flat)](https://github.com/TablePlus/TablePlus/stargazers) - Modern, native, and friendly GUI tool for relational databases: MySQL, PostgreSQL, SQLite & more.
- [TeamPostgreSQL](http://www.teampostgresql.com) - PostgreSQL Web Administration GUI - use your PostgreSQL databases from anywhere, with rich, lightning-fast AJAX web interface.
- [Query.me](https://query.me) - Collaborative SQL editor in Notebook format. Let's you reference query results using JINJA, visualize data, and schedule runs and exports.


## CLI
- [ipython-sql](https://github.com/catherinedevlin/ipython-sql) [![GitHub stars](https://img.shields.io/github/stars/catherinedevlin/ipython-sql?style=flat)](https://github.com/catherinedevlin/ipython-sql/stargazers) - Connect to a database for issue SQL commands within IPython or IPython Notebook.
- [iredis](https://github.com/laixintao/iredis) [![GitHub stars](https://img.shields.io/github/stars/laixintao/iredis?style=flat)](https://github.com/laixintao/iredis/stargazers) - A Cli for Redis with AutoCompletion and Syntax Highlighting.
- [pgcenter](https://github.com/lesovsky/pgcenter) [![GitHub stars](https://img.shields.io/github/stars/lesovsky/pgcenter?style=flat)](https://github.com/lesovsky/pgcenter/stargazers) - Top-like admin tool for PostgreSQL.
- [pg_activity](https://github.com/julmon/pg_activity) [![GitHub stars](https://img.shields.io/github/stars/julmon/pg_activity?style=flat)](https://github.com/julmon/pg_activity/stargazers) - Top-like application for PostgreSQL server activity monitoring.
- [pg_top](https://github.com/markwkm/pg_top) [![GitHub stars](https://img.shields.io/github/stars/markwkm/pg_top?style=flat)](https://github.com/markwkm/pg_top/stargazers) - Top for PostgreSQL.
- [pspg](https://github.com/okbob/pspg) [![GitHub stars](https://img.shields.io/github/stars/okbob/pspg?style=flat)](https://github.com/okbob/pspg/stargazers) - PostgreSQL Pager.
- [diesel-guard](https://github.com/ayarotsky/diesel-guard) [![GitHub stars](https://img.shields.io/github/stars/ayarotsky/diesel-guard?style=flat)](https://github.com/ayarotsky/diesel-guard/stargazers) - Linter for dangerous PostgreSQL migration patterns. It works seamlessly with PostgreSQL SQL files and integrates natively with projects using Diesel and SQLx.
- [SQLcl](http://www.oracle.com/technetwork/developer-tools/sqlcl/overview/index.html) - Oracle SQL Developer Command Line (SQLcl) is a free command line interface for Oracle Database.
- [sqlite-utils](https://github.com/simonw/sqlite-utils) [![GitHub stars](https://img.shields.io/github/stars/simonw/sqlite-utils?style=flat)](https://github.com/simonw/sqlite-utils/stargazers) - CLI tools for manipulating SQLite database files - inserting data, running queries, creating indexes, configuring full-text search and more.
- [SQLLine](https://github.com/julianhyde/sqlline) [![GitHub stars](https://img.shields.io/github/stars/julianhyde/sqlline?style=flat)](https://github.com/julianhyde/sqlline/stargazers) - Command-line shell for issuing SQL to relational databases via JDBC.
- [usql](https://github.com/xo/usql) [![GitHub stars](https://img.shields.io/github/stars/xo/usql?style=flat)](https://github.com/xo/usql/stargazers) - A universal command-line interface for PostgreSQL, MySQL, Oracle Database, SQLite3, Microsoft SQL Server, and many other databases including NoSQL and non-relational databases!

### dbcli
- [athenacli](https://github.com/dbcli/athenacli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/athenacli?style=flat)](https://github.com/dbcli/athenacli/stargazers) - CLI tool for AWS Athena service that can do auto-completion and syntax highlighting.
- [litecli](https://github.com/dbcli/litecli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/litecli?style=flat)](https://github.com/dbcli/litecli/stargazers) - CLI for SQLite Databases with auto-completion and syntax highlighting.
- [mssql-cli](https://github.com/dbcli/mssql-cli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/mssql-cli?style=flat)](https://github.com/dbcli/mssql-cli/stargazers) - A command-line client for SQL Server with auto-completion and syntax highlighting.
- [mycli](https://github.com/dbcli/mycli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/mycli?style=flat)](https://github.com/dbcli/mycli/stargazers) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
- [pgcli](https://github.com/dbcli/pgcli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/pgcli?style=flat)](https://github.com/dbcli/pgcli/stargazers) - PostgreSQL CLI with autocompletion and syntax highlighting.
- [vcli](https://github.com/dbcli/vcli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/vcli?style=flat)](https://github.com/dbcli/vcli/stargazers) - Vertica CLI with auto-completion and syntax highlighting.


## Schema

### Changes
- [2bass](https://github.com/CourseOrchestra/2bass) [![GitHub stars](https://img.shields.io/github/stars/CourseOrchestra/2bass?style=flat)](https://github.com/CourseOrchestra/2bass/stargazers) - Database configuration-as-code tool that utilizes concept of idempotent DDL scripts.
- [Atlas](https://github.com/ariga/atlas) [![GitHub stars](https://img.shields.io/github/stars/ariga/atlas?style=flat)](https://github.com/ariga/atlas/stargazers) - Inspect and Apply changes to your database schema.
- [Bytebase](https://github.com/bytebase/bytebase) [![GitHub stars](https://img.shields.io/github/stars/bytebase/bytebase?style=flat)](https://github.com/bytebase/bytebase/stargazers) - Web-based, zero-config, dependency-free database schema change and version control tool for teams.
- [flyway](https://github.com/flyway/flyway) [![GitHub stars](https://img.shields.io/github/stars/flyway/flyway?style=flat)](https://github.com/flyway/flyway/stargazers) - Database migration tool.
- [gh-ost](https://github.com/github/gh-ost) [![GitHub stars](https://img.shields.io/github/stars/github/gh-ost?style=flat)](https://github.com/github/gh-ost/stargazers) - Online schema migration for MySQL.
- [liquibase](https://github.com/liquibase/liquibase) [![GitHub stars](https://img.shields.io/github/stars/liquibase/liquibase?style=flat)](https://github.com/liquibase/liquibase/stargazers) - Database-independent library for tracking, managing and applying database schema changes.
- [migra](https://github.com/djrobstep/migra) [![GitHub stars](https://img.shields.io/github/stars/djrobstep/migra?style=flat)](https://github.com/djrobstep/migra/stargazers) - Like diff but for PostgreSQL schemas.
- [node-pg-migrate](https://github.com/salsita/node-pg-migrate) [![GitHub stars](https://img.shields.io/github/stars/salsita/node-pg-migrate?style=flat)](https://github.com/salsita/node-pg-migrate/stargazers) - Node.js database migration management built exclusively for PostgreSQL. (But can also be used for other DBs conforming to SQL standard - e.g. CockroachDB.)
- [pg-osc](https://github.com/shayonj/pg-osc) [![GitHub stars](https://img.shields.io/github/stars/shayonj/pg-osc?style=flat)](https://github.com/shayonj/pg-osc/stargazers) - Easy CLI tool for making zero downtime schema changes and backfills in PostgreSQL.
- [Prisma Migrate](https://github.com/prisma/migrate) [![GitHub stars](https://img.shields.io/github/stars/prisma/migrate?style=flat)](https://github.com/prisma/migrate/stargazers) - Declarative database schema migration tool that uses a declarative data modeling syntax to describe your database schema.
- [Pyrseas](https://github.com/perseas/Pyrseas) [![GitHub stars](https://img.shields.io/github/stars/perseas/Pyrseas?style=flat)](https://github.com/perseas/Pyrseas/stargazers) - Provides utilities to describe a PostgreSQL database schema as YAML.
- [Reshape](https://github.com/fabianlindfors/reshape) [![GitHub stars](https://img.shields.io/github/stars/fabianlindfors/reshape?style=flat)](https://github.com/fabianlindfors/reshape/stargazers) - An easy-to-use, zero-downtime schema migration tool for Postgres.
- [SchemaHero](https://github.com/schemahero/schemahero) [![GitHub stars](https://img.shields.io/github/stars/schemahero/schemahero?style=flat)](https://github.com/schemahero/schemahero/stargazers) - A Kubernetes operator for declarative database schema management (gitops for database schemas).
- [Skeema](https://github.com/skeema/skeema) [![GitHub stars](https://img.shields.io/github/stars/skeema/skeema?style=flat)](https://github.com/skeema/skeema/stargazers) - Declarative pure-SQL schema management system for MySQL and MariaDB, with support for sharding and external online schema change tools.
- [Sqitch](https://github.com/sqitchers/sqitch) [![GitHub stars](https://img.shields.io/github/stars/sqitchers/sqitch?style=flat)](https://github.com/sqitchers/sqitch/stargazers) - Sensible database-native change management for framework-free development and dependable deployment.
- [sqldef](https://github.com/k0kubun/sqldef) [![GitHub stars](https://img.shields.io/github/stars/k0kubun/sqldef?style=flat)](https://github.com/k0kubun/sqldef/stargazers) - Idempotent schema management for MySQL, PostgreSQL, and more.
- [yuniql](https://github.com/rdagumampan/yuniql) [![GitHub stars](https://img.shields.io/github/stars/rdagumampan/yuniql?style=flat)](https://github.com/rdagumampan/yuniql/stargazers) - Yet another schema versioning and migration tool just made with native .NET Core 3.0+ and hopefully better.

### Code generation
- [ddl-generator](https://github.com/catherinedevlin/ddl-generator) [![GitHub stars](https://img.shields.io/github/stars/catherinedevlin/ddl-generator?style=flat)](https://github.com/catherinedevlin/ddl-generator/stargazers) - Infers SQL DDL (Data Definition Language) from table data.
- [scheme2ddl](https://github.com/qwazer/scheme2ddl) [![GitHub stars](https://img.shields.io/github/stars/qwazer/scheme2ddl?style=flat)](https://github.com/qwazer/scheme2ddl/stargazers) - Command line util for export Oracle schema to set of ddl init scripts with ability to filter undesirable information, separate DDL in different files, pretty format output.

### Diagrams
- [Azimutt](https://github.com/azimuttapp/azimutt) [![GitHub stars](https://img.shields.io/github/stars/azimuttapp/azimutt?style=flat)](https://github.com/azimuttapp/azimutt/stargazers) - An Entity Relationship diagram (ERD) visualization tool, with various filters and inputs to help understand your database schema.
- [ChartDB](https://github.com/chartdb/chartdb) [![GitHub stars](https://img.shields.io/github/stars/chartdb/chartdb?style=flat)](https://github.com/chartdb/chartdb/stargazers) - Free and Open-source database diagrams editor, visualize and design your DB with a single query.
- [DrawDB](https://github.com/drawdb-io/drawdb) [![GitHub stars](https://img.shields.io/github/stars/drawdb-io/drawdb?style=flat)](https://github.com/drawdb-io/drawdb/stargazers) - Free, simple, and intuitive online database design tool and SQL generator. 
- [DrawSQL](https://drawsql.app) - Online database schema diagram editor with SQL import, AI generation, and real-time team collaboration.
- [ERAlchemy](https://github.com/Alexis-benoist/eralchemy) [![GitHub stars](https://img.shields.io/github/stars/Alexis-benoist/eralchemy?style=flat)](https://github.com/Alexis-benoist/eralchemy/stargazers) - Entity Relation Diagrams generation tool.
- [ERD Lab](https://www.erdlab.io/) - Free cloud based entity relationship diagram (ERD) tool made for developers.
- [Liam ERD](https://github.com/liam-hq/liam) [![GitHub stars](https://img.shields.io/github/stars/liam-hq/liam?style=flat)](https://github.com/liam-hq/liam/stargazers) - Open-source tool that generates beautiful and easy-to-read Entity Relationship Diagrams from your database and ORMs.
- [QuickDBD](https://www.quickdatabasediagrams.com/) - Simple online tool to quickly draw database diagrams.

### Documentations
- [dbdocs](https://dbdocs.io/) - Create web-based database documentation using DSL code.
- [DBML](https://github.com/holistics/dbml) [![GitHub stars](https://img.shields.io/github/stars/holistics/dbml?style=flat)](https://github.com/holistics/dbml/stargazers) - Database Markup Language, designed to define and document database structures.
- [SchemaCrawler](https://github.com/schemacrawler/SchemaCrawler) [![GitHub stars](https://img.shields.io/github/stars/schemacrawler/SchemaCrawler?style=flat)](https://github.com/schemacrawler/SchemaCrawler/stargazers) - A free database schema discovery and comprehension tool.
- [Schema Spy](https://github.com/schemaspy/schemaspy) [![GitHub stars](https://img.shields.io/github/stars/schemaspy/schemaspy?style=flat)](https://github.com/schemaspy/schemaspy/stargazers) - Generating your database to HTML documentation, including Entity Relationship diagrams.
- [tbls](https://github.com/k1LoW/tbls) [![GitHub stars](https://img.shields.io/github/stars/k1LoW/tbls?style=flat)](https://github.com/k1LoW/tbls/stargazers) - CI-Friendly tool for document a database, written in Go.

### Design
- [Database Design](https://github.com/alextanhongpin/database-design) [![GitHub stars](https://img.shields.io/github/stars/alextanhongpin/database-design?style=flat)](https://github.com/alextanhongpin/database-design/stargazers) - Useful tips for designing robust database schema.
- [DBDiagram](https://dbdiagram.io) - A free, simple tool to draw ER diagrams by just writing code.
- [DbSchema](https://dbschema.com/) - Universal database designer for out-of-the-box schema management, schema documentation, design in a team, and deployment on multiple databases. DbSchema features tools for writing and executing queries, exploring the data, generating data, and building reports.
- [ERBuilder Data Modeler](https://soft-builder.com/erbuilder-data-modeler) - Easy-to-use database modeling software for high-quality data models. It's a complete data modeling solution for data modelers and data architects.
- [Moon Modeler](https://www.datensen.com) - Data modeling tool for both noSQL and relational databases. Available for Windows, Linux and macOS.
- [Navicat Data Modeler](https://www.navicat.com/en/products/navicat-data-modeler) - A powerful and cost-effective database design tool which helps you build high-quality conceptual, logical and physical data models.
- [Oracle SQL Developer Data Modeler](http://www.oracle.com/technetwork/developer-tools/datamodeler/overview/index.html) - Free graphical tool that enhances productivity and simplifies data modeling tasks.
- [pgmodeler](https://github.com/pgmodeler/pgmodeler) [![GitHub stars](https://img.shields.io/github/stars/pgmodeler/pgmodeler?style=flat)](https://github.com/pgmodeler/pgmodeler/stargazers) - Data modeling tool designed for PostgreSQL.
- [WWW SQL Designer](https://github.com/ondras/wwwsqldesigner) [![GitHub stars](https://img.shields.io/github/stars/ondras/wwwsqldesigner?style=flat)](https://github.com/ondras/wwwsqldesigner/stargazers) - Online SQL diagramming tool.

### Samples
- [Oracle Database Sample Schemas](https://github.com/oracle/db-sample-schemas) [![GitHub stars](https://img.shields.io/github/stars/oracle/db-sample-schemas?style=flat)](https://github.com/oracle/db-sample-schemas/stargazers) - Sample schemas for Oracle Database.


## API
Building API for your Data
- [Datasette](https://github.com/simonw/datasette) [![GitHub stars](https://img.shields.io/github/stars/simonw/datasette?style=flat)](https://github.com/simonw/datasette/stargazers) - A tool for exploring and publishing data.
- [DreamFactory](https://github.com/dreamfactorysoftware/dreamfactory) [![GitHub stars](https://img.shields.io/github/stars/dreamfactorysoftware/dreamfactory?style=flat)](https://github.com/dreamfactorysoftware/dreamfactory/stargazers) - A open source REST API backend for mobile, web, and IoT applications.
- [Graphweaver](https://github.com/exogee-technology/graphweaver) [![GitHub stars](https://img.shields.io/github/stars/exogee-technology/graphweaver?style=flat)](https://github.com/exogee-technology/graphweaver/stargazers) - Turn multiple data sources into a single GraphQL API.
- [Hasura GraphQL Engine](https://github.com/hasura/graphql-engine) [![GitHub stars](https://img.shields.io/github/stars/hasura/graphql-engine?style=flat)](https://github.com/hasura/graphql-engine/stargazers) - Blazing fast, instant realtime GraphQL APIs on PostgreSQL with fine grained access control, also trigger webhooks on database events.
- [JdbcREST](https://github.com/synthesized-io/jdbcrest/) [![GitHub stars](https://img.shields.io/github/stars/synthesized-io/jdbcrest/?style=flat)](https://github.com/synthesized-io/jdbcrest//stargazers) - REST API for any JDBC-backed database, a PostgREST clone written in Java.
- [Oracle REST Data Services](http://www.oracle.com/technetwork/developer-tools/rest-data-services) - A mid-tier Java application, ORDS maps HTTP(S) verbs (GET, POST, PUT, DELETE, etc.) to database transactions and returns any results formatted using JSON.
- [Prisma](https://github.com/prismagraphql/prisma) [![GitHub stars](https://img.shields.io/github/stars/prismagraphql/prisma?style=flat)](https://github.com/prismagraphql/prisma/stargazers) - Turns your database into a realtime GraphQL API.
- [PostGraphile](https://github.com/graphile/postgraphile) [![GitHub stars](https://img.shields.io/github/stars/graphile/postgraphile?style=flat)](https://github.com/graphile/postgraphile/stargazers) - Instantly spin-up a GraphQL API server by pointing PostGraphile at your existing PostgreSQL database.
- [PostgREST](https://github.com/PostgREST/postgrest) [![GitHub stars](https://img.shields.io/github/stars/PostgREST/postgrest?style=flat)](https://github.com/PostgREST/postgrest/stargazers) - REST API for any PostgreSQL database.
- [prest](https://github.com/prest/prest) [![GitHub stars](https://img.shields.io/github/stars/prest/prest?style=flat)](https://github.com/prest/prest/stargazers) - Is a way to serve a RESTful API from any databases written in Go.
- [Remult](https://github.com/remult/remult) [![GitHub stars](https://img.shields.io/github/stars/remult/remult?style=flat)](https://github.com/remult/remult/stargazers) - End-to-end type-safe CRUD via REST API for your database, with fine-grained access control.
- [restSQL](https://github.com/restsql/restsql) [![GitHub stars](https://img.shields.io/github/stars/restsql/restsql?style=flat)](https://github.com/restsql/restsql/stargazers) - SQL generator with Java and HTTP APIs, uses a simple RESTful HTTP API with XML or JSON serialization.
- [resquel](https://github.com/formio/resquel) [![GitHub stars](https://img.shields.io/github/stars/formio/resquel?style=flat)](https://github.com/formio/resquel/stargazers) - Easily convert your SQL database into a REST API.
- [sandman2](https://github.com/jeffknupp/sandman2) [![GitHub stars](https://img.shields.io/github/stars/jeffknupp/sandman2?style=flat)](https://github.com/jeffknupp/sandman2/stargazers) - Automatically generate a RESTful API service for your legacy database.
- [soul](https://github.com/thevahidal/soul) [![GitHub stars](https://img.shields.io/github/stars/thevahidal/soul?style=flat)](https://github.com/thevahidal/soul/stargazers) - Automatic SQLite RESTful and realtime API server.
- [VulcanSQL](https://github.com/Canner/vulcan-sql) [![GitHub stars](https://img.shields.io/github/stars/Canner/vulcan-sql?style=flat)](https://github.com/Canner/vulcan-sql/stargazers) - Write templated SQL to automatically exposing RESTful APIs from your database/data warehouse/data lake.

## Application platforms
Low-code and no-code platforms for application building
- [Appsmith](https://github.com/appsmithorg/appsmith) [![GitHub stars](https://img.shields.io/github/stars/appsmithorg/appsmith?style=flat)](https://github.com/appsmithorg/appsmith/stargazers) - Powerful open source low code framework to build internal applications really quickly.
- [Budibase](https://github.com/Budibase/budibase) [![GitHub stars](https://img.shields.io/github/stars/Budibase/budibase?style=flat)](https://github.com/Budibase/budibase/stargazers) - Low-code platform for creating internal apps in minutes.
- [ILLA Cloud](https://github.com/illacloud/illa-builder) [![GitHub stars](https://img.shields.io/github/stars/illacloud/illa-builder?style=flat)](https://github.com/illacloud/illa-builder/stargazers) - Low-code internal tool building platform.
- [Nhost](https://github.com/nhost/nhost) [![GitHub stars](https://img.shields.io/github/stars/nhost/nhost?style=flat)](https://github.com/nhost/nhost/stargazers) - The Open Source Firebase Alternative with GraphQL.
- [Saltcorn](https://github.com/saltcorn/saltcorn) [![GitHub stars](https://img.shields.io/github/stars/saltcorn/saltcorn?style=flat)](https://github.com/saltcorn/saltcorn/stargazers) - Open source no-code builder for web datatabase applications. Server and drag-and-drop UI builder, data stored in PostgreSQL or SQLite.
- [SQLPage](https://github.com/sqlpage/SQLPage) [![GitHub stars](https://img.shields.io/github/stars/sqlpage/SQLPage?style=flat)](https://github.com/sqlpage/SQLPage/stargazers) - Fast SQL-only data application builder. Automatically build a UI on top of SQL queries.
- [Tooljet](https://github.com/ToolJet/ToolJet) [![GitHub stars](https://img.shields.io/github/stars/ToolJet/ToolJet?style=flat)](https://github.com/ToolJet/ToolJet/stargazers) - Open-source low-code platform to build internal tools.


## Backup
- [BaRMan](https://github.com/2ndquadrant-it/barman) [![GitHub stars](https://img.shields.io/github/stars/2ndquadrant-it/barman?style=flat)](https://github.com/2ndquadrant-it/barman/stargazers) - Backup and Recovery Manager for PostgreSQL.
- [Databasus](https://github.com/databasus/databasus) [![GitHub stars](https://img.shields.io/github/stars/databasus/databasus?style=flat)](https://github.com/databasus/databasus/stargazers) - Tool for scheduled PostgreSQL backups via web UI with external storages (local, S3, FTP, Google Drive, etc.), notifications (webhook, Discord, Slack, etc.) and team management.
- [pgbackrest](https://github.com/pgbackrest/pgbackrest) [![GitHub stars](https://img.shields.io/github/stars/pgbackrest/pgbackrest?style=flat)](https://github.com/pgbackrest/pgbackrest/stargazers) - Reliable PostgreSQL Backup & Restore.
- [pgcopydb](https://github.com/dimitri/pgcopydb) [![GitHub stars](https://img.shields.io/github/stars/dimitri/pgcopydb?style=flat)](https://github.com/dimitri/pgcopydb/stargazers) - Copy a PostgreSQL database to a target PostgreSQL server (pg_dump | pg_restore on steroids).
- [pg_probackup](https://github.com/postgrespro/pg_probackup) [![GitHub stars](https://img.shields.io/github/stars/postgrespro/pg_probackup?style=flat)](https://github.com/postgrespro/pg_probackup/stargazers) - A backup and recovery manager for PostgreSQL.
- [Portabase](https://github.com/Portabase/portabase) [![GitHub stars](https://img.shields.io/github/stars/Portabase/portabase?style=flat)](https://github.com/Portabase/portabase/stargazers) - Agent-based platform for PostgreSQL backups and restores with decentralized execution and centralized orchestration. 

## Cloning
- [Database Lab Engine](https://gitlab.com/postgres-ai/database-lab) - Instant thin cloning for PostgreSQL to scale the development process.
- [clone_schema](https://github.com/denishpatel/pg-clone-schema) [![GitHub stars](https://img.shields.io/github/stars/denishpatel/pg-clone-schema?style=flat)](https://github.com/denishpatel/pg-clone-schema/stargazers) - PostgreSQL clone schema utility without need of going outside of database.
- [Spawn](https://spawn.cc/) - Cloud service for creating instant database copies for development and CI. No more local db installs, instant recovery to arbitrary save points, isolated copies for each feature branch or test. Instant provisioning regardless of database size.


## Monitoring/Statistics/Perfomance
- [ASH Viewer](https://github.com/akardapolov/ASH-Viewer) [![GitHub stars](https://img.shields.io/github/stars/akardapolov/ASH-Viewer?style=flat)](https://github.com/akardapolov/ASH-Viewer/stargazers) - Provides a graphical view of active session history data within the Oracle and PostgreSQL DB.
- [Metis](https://www.metisdata.io/product/troubleshooting) - Provides observability and performance tuning for SQL databases.
- [Monyog](https://www.webyog.com/product/monyog) - Agentless & Cost-effective MySQL Monitoring Tool.
- [mssql-monitoring](https://github.com/microsoft/mssql-monitoring) [![GitHub stars](https://img.shields.io/github/stars/microsoft/mssql-monitoring?style=flat)](https://github.com/microsoft/mssql-monitoring/stargazers) - Monitor your SQL Server on Linux performance using collectd, InfluxDB and Grafana.
- [Navicat Monitor](https://www.navicat.com/en/products/navicat-monitor) - A safe, simple and agentless remote server monitoring tool that is packed with powerful features to make your monitoring effective as possible.
- [Percona Monitoring and Management](https://github.com/percona/pmm) [![GitHub stars](https://img.shields.io/github/stars/percona/pmm?style=flat)](https://github.com/percona/pmm/stargazers) - Open source platform for managing and monitoring MySQL and MongoDB performance.
- [pganalyze collector](https://github.com/pganalyze/collector) [![GitHub stars](https://img.shields.io/github/stars/pganalyze/collector?style=flat)](https://github.com/pganalyze/collector/stargazers) - Pganalyze statistics collector for gathering PostgreSQL metrics and log data.
- [pgbadger](https://github.com/dalibo/pgbadger) [![GitHub stars](https://img.shields.io/github/stars/dalibo/pgbadger?style=flat)](https://github.com/dalibo/pgbadger/stargazers) - A fast PostgreSQL Log Analyzer.
- [pgDash](https://pgdash.io) - Measure and track every aspect of your PostgreSQL databases.
- [PgHero](https://github.com/ankane/pghero) [![GitHub stars](https://img.shields.io/github/stars/ankane/pghero?style=flat)](https://github.com/ankane/pghero/stargazers) - A performance dashboard for PostgreSQL - health checks, suggested indexes, and more.
- [pgmetrics](https://github.com/rapidloop/pgmetrics) [![GitHub stars](https://img.shields.io/github/stars/rapidloop/pgmetrics?style=flat)](https://github.com/rapidloop/pgmetrics/stargazers) - Collect and display information and stats from a running PostgreSQL server.
- [pgMonitor](https://github.com/CrunchyData/pgmonitor) [![GitHub stars](https://img.shields.io/github/stars/CrunchyData/pgmonitor?style=flat)](https://github.com/CrunchyData/pgmonitor/stargazers) - All-in-one tool to easily create an environment to visualize the health and performance of your PostgreSQL cluster.
- [pgMustard](https://www.pgmustard.com) - A user interface for PostgreSQL explain plans, plus tips to improve performance.
- [pgstats](https://github.com/gleu/pgstats) [![GitHub stars](https://img.shields.io/github/stars/gleu/pgstats?style=flat)](https://github.com/gleu/pgstats/stargazers) - Collects PostgreSQL statistics, and either saves them in CSV files or print them on the stdout.
- [pgwatch2](https://github.com/cybertec-postgresql/pgwatch2) [![GitHub stars](https://img.shields.io/github/stars/cybertec-postgresql/pgwatch2?style=flat)](https://github.com/cybertec-postgresql/pgwatch2/stargazers) - Flexible self-contained PostgreSQL metrics monitoring/dashboarding solution.
- [PostgreSQL Metrics](https://github.com/spotify/postgresql-metrics) [![GitHub stars](https://img.shields.io/github/stars/spotify/postgresql-metrics?style=flat)](https://github.com/spotify/postgresql-metrics/stargazers) - Service to extract and provide metrics on your PostgreSQL database.
- [PostgreSQL Monitor](https://postgresmonitor.com) - An easy-to-use monitoring service for PostgreSQL providing alerts, dashboards, query stats and dynamic recommendations.
- [postgres-checkup](https://gitlab.com/postgres-ai/postgres-checkup) - New-generation diagnostics tool that allows users to do a deep analysis of the health of PostgreSQL databases.
- [Promscale](https://github.com/timescale/promscale) [![GitHub stars](https://img.shields.io/github/stars/timescale/promscale?style=flat)](https://github.com/timescale/promscale/stargazers) - The open-source observability backend for metrics and traces powered by SQL.
- [Releem](https://releem.com) - Performance monitoring and optimization tool for MySQL & MariaDB that delivers actionable insights and safe automation for misconfigurations, slow queries, schema issues, and deadlocks, reducing manual work at scale.
- [Telegraf PostgreSQL plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/postgresql) [![GitHub stars](https://img.shields.io/github/stars/influxdata/telegraf/tree/master/plugins/inputs/postgresql?style=flat)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/postgresql/stargazers) - Provides metrics for your PostgreSQL database.

### Prometheus
- [pgSCV](https://github.com/weaponry/pgscv) [![GitHub stars](https://img.shields.io/github/stars/weaponry/pgscv?style=flat)](https://github.com/weaponry/pgscv/stargazers) - Metrics exporter for PostgreSQL and PostgreSQL-related services.
- [postgres_exporter](https://github.com/wrouesnel/postgres_exporter) [![GitHub stars](https://img.shields.io/github/stars/wrouesnel/postgres_exporter?style=flat)](https://github.com/wrouesnel/postgres_exporter/stargazers) - Prometheus exporter for PostgreSQL server metrics.
- [pg_exporter](https://github.com/Vonng/pg_exporter) [![GitHub stars](https://img.shields.io/github/stars/Vonng/pg_exporter?style=flat)](https://github.com/Vonng/pg_exporter/stargazers) - Fully customizable Prometheus exporter for PostgreSQL & Pgbouncer with fine-grained execution control.

### Zabbix
- [Mamonsu](https://github.com/postgrespro/mamonsu) [![GitHub stars](https://img.shields.io/github/stars/postgrespro/mamonsu?style=flat)](https://github.com/postgrespro/mamonsu/stargazers) - Monitoring agent for PostgreSQL.
- [Orabbix](http://www.smartmarmot.com/wiki/index.php?title=Orabbix) - Plugin designed to work with Zabbix Enterprise Monitor to provide multi-tiered monitoring, performance and availability reporting and measurement for Oracle Databases, along with server performance metrics.
- [pg_monz](https://github.com/pg-monz/pg_monz) [![GitHub stars](https://img.shields.io/github/stars/pg-monz/pg_monz?style=flat)](https://github.com/pg-monz/pg_monz/stargazers) - This is the Zabbix monitoring template for PostgreSQL Database.
- [Pyora](https://github.com/bicofino/Pyora) [![GitHub stars](https://img.shields.io/github/stars/bicofino/Pyora?style=flat)](https://github.com/bicofino/Pyora/stargazers) - Python script to monitor Oracle Databases.
- [ZabbixDBA](https://github.com/anetrusov/ZabbixDBA) [![GitHub stars](https://img.shields.io/github/stars/anetrusov/ZabbixDBA?style=flat)](https://github.com/anetrusov/ZabbixDBA/stargazers) - Fast, flexible, and continuously developing plugin to monitor your RDBMS.


## Testing
- [DbFit](https://github.com/dbfit/dbfit) [![GitHub stars](https://img.shields.io/github/stars/dbfit/dbfit?style=flat)](https://github.com/dbfit/dbfit/stargazers) - A database testing framework that supports easy test-driven development of your database code.
- [pgTAP](https://github.com/theory/pgtap) [![GitHub stars](https://img.shields.io/github/stars/theory/pgtap?style=flat)](https://github.com/theory/pgtap/stargazers) - Unit Testing for PostgreSQL.
- [RegreSQL](https://github.com/dimitri/regresql) [![GitHub stars](https://img.shields.io/github/stars/dimitri/regresql?style=flat)](https://github.com/dimitri/regresql/stargazers) - Regression Testing your SQL queries.
- [SQLancer](https://github.com/sqlancer/sqlancer) [![GitHub stars](https://img.shields.io/github/stars/sqlancer/sqlancer?style=flat)](https://github.com/sqlancer/sqlancer/stargazers) - Automatically test DBMS in order to find logic bugs in their implementation.


## HA/Failover/Sharding
- [Citus](https://github.com/citusdata/citus) [![GitHub stars](https://img.shields.io/github/stars/citusdata/citus?style=flat)](https://github.com/citusdata/citus/stargazers) - PostgreSQL extension that distributes your data and your queries across multiple nodes.
- [patroni](https://github.com/zalando/patroni) [![GitHub stars](https://img.shields.io/github/stars/zalando/patroni?style=flat)](https://github.com/zalando/patroni/stargazers) - A template for PostgreSQL High Availability with ZooKeeper, etcd, or Consul.
- [Percona XtraDB Cluster](https://github.com/percona/percona-xtradb-cluster) [![GitHub stars](https://img.shields.io/github/stars/percona/percona-xtradb-cluster?style=flat)](https://github.com/percona/percona-xtradb-cluster/stargazers) - A High Scalability Solution for MySQL Clustering and High Availability.
- [ShardingSphere](https://github.com/apache/shardingsphere) [![GitHub stars](https://img.shields.io/github/stars/apache/shardingsphere?style=flat)](https://github.com/apache/shardingsphere/stargazers) - Distributed SQL transaction & query engine for data sharding, scaling, encryption, and more - on any database.
- [stolon](https://github.com/sorintlab/stolon) [![GitHub stars](https://img.shields.io/github/stars/sorintlab/stolon?style=flat)](https://github.com/sorintlab/stolon/stargazers) - Cloud native PostgreSQL manager for PostgreSQL high availability.
- [pg_auto_failover](https://github.com/citusdata/pg_auto_failover) [![GitHub stars](https://img.shields.io/github/stars/citusdata/pg_auto_failover?style=flat)](https://github.com/citusdata/pg_auto_failover/stargazers) - PostgreSQL extension and service for automated failover and high-availability.
- [pglookout](https://github.com/aiven/pglookout) [![GitHub stars](https://img.shields.io/github/stars/aiven/pglookout?style=flat)](https://github.com/aiven/pglookout/stargazers) - PostgreSQL replication monitoring and failover daemon.
- [pgslice](https://github.com/ankane/pgslice) [![GitHub stars](https://img.shields.io/github/stars/ankane/pgslice?style=flat)](https://github.com/ankane/pgslice/stargazers) - PostgreSQL partitioning as easy as pie.
- [PostgreSQL Automatic Failover](https://github.com/ClusterLabs/PAF) [![GitHub stars](https://img.shields.io/github/stars/ClusterLabs/PAF?style=flat)](https://github.com/ClusterLabs/PAF/stargazers) - High-Availibility for PostgreSQL, based on industry references Pacemaker and Corosync.
- [autobase](https://github.com/vitabaks/autobase) [![GitHub stars](https://img.shields.io/github/stars/vitabaks/autobase?style=flat)](https://github.com/vitabaks/autobase/stargazers) - Open-source DBaaS that automates the deployment and management of highly available PostgreSQL clusters.
- [Vitess](https://github.com/vitessio/vitess) [![GitHub stars](https://img.shields.io/github/stars/vitessio/vitess?style=flat)](https://github.com/vitessio/vitess/stargazers) - Database clustering system for horizontal scaling of MySQL through generalized sharding.


## Kubernetes
- [KubeDB](https://kubedb.com) - Making running production-grade databases easy on Kubernetes.
- [PostgreSQL operator](https://github.com/zalando/postgres-operator) [![GitHub stars](https://img.shields.io/github/stars/zalando/postgres-operator?style=flat)](https://github.com/zalando/postgres-operator/stargazers) - The PostgreSQL Operator enables highly-available PostgreSQL clusters on Kubernetes (Kubernetes) powered by Patroni.
- [Spilo](https://github.com/zalando/spilo) [![GitHub stars](https://img.shields.io/github/stars/zalando/spilo?style=flat)](https://github.com/zalando/spilo/stargazers) - HA PostgreSQL Clusters with Docker.
- [StackGres](https://gitlab.com/ongresinc/stackgres) - Enterprise-grade, Full Stack PostgreSQL on Kubernetes.


## Configuration Tuning
- [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) [![GitHub stars](https://img.shields.io/github/stars/major/MySQLTuner-perl?style=flat)](https://github.com/major/MySQLTuner-perl/stargazers) - Script written in Perl that allows you to review a MySQL installation quickly and make adjustments to increase performance and stability.
- [PGConfigurator](https://pgconfigurator.cybertec-postgresql.com) - Free online tool to generate an optimized `postgresql.conf`.
- [pgtune](https://github.com/gregs1104/pgtune) [![GitHub stars](https://img.shields.io/github/stars/gregs1104/pgtune?style=flat)](https://github.com/gregs1104/pgtune/stargazers) - PostgreSQL configuration wizard.
- [postgresqltuner.pl](https://github.com/jfcoz/postgresqltuner) [![GitHub stars](https://img.shields.io/github/stars/jfcoz/postgresqltuner?style=flat)](https://github.com/jfcoz/postgresqltuner/stargazers) - Simple script to analyse your PostgreSQL database configuration, and give tuning advice.


## DevOps
- [DBmaestro](https://www.dbmaestro.com) - Accelerates release cycles & supports agility across the entire IT ecosystem.
- [Toad DevOps Toolkit](https://www.quest.com/products/toad-devops-toolkit/) - Executes key database development functions within your DevOps workflow —without compromising quality, performance or reliability.


## Reporting
- [Chartbrew](https://chartbrew.com) - Create live dashboards, charts, and client reports from multiple databases and services.
- [Poli](https://github.com/shzlw/poli) [![GitHub stars](https://img.shields.io/github/stars/shzlw/poli?style=flat)](https://github.com/shzlw/poli/stargazers) - An easy-to-use SQL reporting application built for SQL lovers.


## Distributions
- [DBdeployer](https://github.com/datacharmer/dbdeployer) [![GitHub stars](https://img.shields.io/github/stars/datacharmer/dbdeployer?style=flat)](https://github.com/datacharmer/dbdeployer/stargazers) - Tool that deploys MySQL database servers easily.
- [dbatools](https://github.com/sqlcollaborative/dbatools) [![GitHub stars](https://img.shields.io/github/stars/sqlcollaborative/dbatools?style=flat)](https://github.com/sqlcollaborative/dbatools/stargazers) - PowerShell module that you may think of like a command-line SQL Server Management Studio.
- [Postgres.app](https://github.com/PostgresApp/PostgresApp) [![GitHub stars](https://img.shields.io/github/stars/PostgresApp/PostgresApp?style=flat)](https://github.com/PostgresApp/PostgresApp/stargazers) - Full-featured PostgreSQL installation packaged as a standard Mac app.
- [BigSQL](https://www.bigsql.org) - A developer-friendly distribution of PostgreSQL.
- [Elephant Shed](https://github.com/credativ/elephant-shed) [![GitHub stars](https://img.shields.io/github/stars/credativ/elephant-shed?style=flat)](https://github.com/credativ/elephant-shed/stargazers) - Web-based PostgreSQL management front-end that bundles several utilities and applications for use with PostgreSQL.
- [Pigsty](https://github.com/Vonng/pigsty) [![GitHub stars](https://img.shields.io/github/stars/Vonng/pigsty?style=flat)](https://github.com/Vonng/pigsty/stargazers) - Battery-Included Open-Source Distribution for PostgreSQL with ultimate observability & Database-as-Code toolbox for developers.


## Security
- [Acra](https://github.com/cossacklabs/acra) [![GitHub stars](https://img.shields.io/github/stars/cossacklabs/acra?style=flat)](https://github.com/cossacklabs/acra/stargazers) - Database security suite. Database proxy with field-level encryption, search through encrypted data, SQL injections prevention, intrusion detection, honeypots. Supports client-side and proxy-side ("transparent") encryption. SQL, NoSQL.
- [Databunker](https://github.com/securitybunker/databunker) [![GitHub stars](https://img.shields.io/github/stars/securitybunker/databunker?style=flat)](https://github.com/securitybunker/databunker/stargazers) - Special GDPR compliant secure vault for customer records built on top of regular DB.
- [Inspektor](https://github.com/poonai/inspektor) [![GitHub stars](https://img.shields.io/github/stars/poonai/inspektor?style=flat)](https://github.com/poonai/inspektor/stargazers) - Access control layer for databases. Inspektor leverages open policy agent to make policy decisions.


## SQL

### Analyzers
- [Holistic.dev](https://holistic.dev) - Automatic detection service for database performance, security, and architecture issues.
- [SQLCheck](https://github.com/jarulraj/sqlcheck) [![GitHub stars](https://img.shields.io/github/stars/jarulraj/sqlcheck?style=flat)](https://github.com/jarulraj/sqlcheck/stargazers) - Automatically detects common SQL anti-patterns.
- [SQLFluff](https://github.com/sqlfluff/sqlfluff) [![GitHub stars](https://img.shields.io/github/stars/sqlfluff/sqlfluff?style=flat)](https://github.com/sqlfluff/sqlfluff/stargazers) - Dialect-flexible and configurable SQL linter.
- [SQLLineage](https://github.com/reata/sqllineage) [![GitHub stars](https://img.shields.io/github/stars/reata/sqllineage?style=flat)](https://github.com/reata/sqllineage/stargazers) - SQL Lineage Analysis Tool powered by Python.
- [TSQLLint](https://github.com/tsqllint/tsqllint) [![GitHub stars](https://img.shields.io/github/stars/tsqllint/tsqllint?style=flat)](https://github.com/tsqllint/tsqllint/stargazers) - A tool for describing, identifying, and reporting the presence of anti-patterns in TSQL scripts.

### Code Generators
- [sqlc](https://sqlc.dev) - SQL-first code generator producing type-safe bindings for various languages and various databases.
- [SQLDelight](https://sqldelight.github.io/sqldelight) - SQL-first code generator producing type-safe bindings for Kotlin and various databases.
- [pGenie](https://pgenie.io) - SQL-first code generator producing type-safe bindings for various languages and specializing on the PostgreSQL database.

### Extensions
- [PartiQL](https://partiql.org) - SQL-compatible access to relational, semi-structured, and nested data.

### Frameworks
- [Apache Calcite](https://calcite.apache.org) - Dynamic data management framework with advanced SQL features.
- [ZetaSQL](https://github.com/google/zetasql) [![GitHub stars](https://img.shields.io/github/stars/google/zetasql?style=flat)](https://github.com/google/zetasql/stargazers) - Analyzer Framework for SQL.

### Formatters
- [CodeBuff](https://github.com/antlr/codebuff) [![GitHub stars](https://img.shields.io/github/stars/antlr/codebuff?style=flat)](https://github.com/antlr/codebuff/stargazers) - Language-agnostic pretty-printing through machine learning.
- [JSQLFormatter](https://github.com/manticore-projects/jsqlformatter) [![GitHub stars](https://img.shields.io/github/stars/manticore-projects/jsqlformatter?style=flat)](https://github.com/manticore-projects/jsqlformatter/stargazers) - Open Source Java SQL Formatter for many RDBMS based on JSqlParser.
- [SQL Online](https://sqlonline.in) - A Free Tool to format your SQL Queries followed by content for Analysts.
- [pgFormatter](https://github.com/darold/pgFormatter) [![GitHub stars](https://img.shields.io/github/stars/darold/pgFormatter?style=flat)](https://github.com/darold/pgFormatter/stargazers) - A PostgreSQL SQL syntax beautifier.
- [Poor SQL](https://poorsql.com) - Instant free and open-source T-SQL formatting. 
- [SQL Formatter](https://github.com/zeroturnaround/sql-formatter) [![GitHub stars](https://img.shields.io/github/stars/zeroturnaround/sql-formatter?style=flat)](https://github.com/zeroturnaround/sql-formatter/stargazers) - JavaScript library for pretty-printing SQL queries.

### Games
- [Lost at SQL](https://lost-at-sql.therobinlord.com) - A SQL learning game to help you pick up basic SQL skills - so that you can use queries to get information.
- [Querymon](https://codepip.com/games/querymon/) - Learn to use SQL queries on the Querydex, a database of monsters from common to legendary.
- [Schemaverse](https://datalemur.com/blog/games-to-learn-sql#schemaverse) - A Space-based strategy game implemented entirely within a PostgreSQL database.
- [SQL Island](https://sql-island.informatik.uni-kl.de) - After the survived plane crash, you will be stuck on SQL Island for the time being. By making progress in the game, you will find a way to escape from this island.
- [SQL Murder Mystery](https://mystery.knightlab.com) - Designed to be both a self-directed lesson to learn SQL concepts and commands and a fun game for experienced SQL users to solve an intriguing crime.
- [SQL Police Department](https://sqlpd.com) - In SQLPD, you get to solve crimes while learning SQL at the same time.

### Parsers
- [General SQL Parser](https://www.sqlparser.com) - Parsing, formatting, modification and analysis for SQL.
- [jOOQ](https://github.com/jOOQ/jOOQ) [![GitHub stars](https://img.shields.io/github/stars/jOOQ/jOOQ?style=flat)](https://github.com/jOOQ/jOOQ/stargazers) - Parses SQL, translates it to other dialects, and allows for expression tree transformations.
- [JSqlParser](https://github.com/JSQLParser/JSqlParser) [![GitHub stars](https://img.shields.io/github/stars/JSQLParser/JSqlParser?style=flat)](https://github.com/JSQLParser/JSqlParser/stargazers) - Parses an SQL statement and translate it into a hierarchy of Java classes.
- [libpg_query](https://github.com/pganalyze/libpg_query) [![GitHub stars](https://img.shields.io/github/stars/pganalyze/libpg_query?style=flat)](https://github.com/pganalyze/libpg_query/stargazers) - C library for accessing the PostgreSQL parser outside of the server environment.
- [More SQL Parsing!](https://github.com/klahnakoski/mo-sql-parsing) [![GitHub stars](https://img.shields.io/github/stars/klahnakoski/mo-sql-parsing?style=flat)](https://github.com/klahnakoski/mo-sql-parsing/stargazers) - Parse SQL into JSON.
- [sqlparse](https://github.com/andialbrecht/sqlparse) [![GitHub stars](https://img.shields.io/github/stars/andialbrecht/sqlparse?style=flat)](https://github.com/andialbrecht/sqlparse/stargazers) - Non-validating SQL parser for Python.
- [SQLGlot](https://github.com/tobymao/sqlglot) [![GitHub stars](https://img.shields.io/github/stars/tobymao/sqlglot?style=flat)](https://github.com/tobymao/sqlglot/stargazers) - Pure Python SQL parser, transpiler, and builder.

### Über SQL
Run SQL queries against anything
- [CloudQuery](https://github.com/cloudquery/cloudquery) [![GitHub stars](https://img.shields.io/github/stars/cloudquery/cloudquery?style=flat)](https://github.com/cloudquery/cloudquery/stargazers) - Extracts, transforms, and loads your cloud assets into normalized PostgreSQL tables.
- [csvq](https://github.com/mithrandie/csvq) [![GitHub stars](https://img.shields.io/github/stars/mithrandie/csvq?style=flat)](https://github.com/mithrandie/csvq/stargazers) - SQL-like query language for CSV.
- [dsq](https://github.com/multiprocessio/dsq) [![GitHub stars](https://img.shields.io/github/stars/multiprocessio/dsq?style=flat)](https://github.com/multiprocessio/dsq/stargazers) - Commandline tool for running SQL queries against JSON, CSV, Excel, Parquet, and more.
- [MAT Calcite plugin](https://github.com/vlsi/mat-calcite-plugin) [![GitHub stars](https://img.shields.io/github/stars/vlsi/mat-calcite-plugin?style=flat)](https://github.com/vlsi/mat-calcite-plugin/stargazers) - This plugin for Eclipse Memory Analyzer allows to query heap dump via SQL.
- [OctoSQL](https://github.com/cube2222/octosql) [![GitHub stars](https://img.shields.io/github/stars/cube2222/octosql?style=flat)](https://github.com/cube2222/octosql/stargazers) - Query tool that allows you to join, analyse and transform data from multiple databases and file formats using SQL.
- [osquery](https://github.com/osquery/osquery) [![GitHub stars](https://img.shields.io/github/stars/osquery/osquery?style=flat)](https://github.com/osquery/osquery/stargazers) - SQL powered operating system instrumentation, monitoring, and analytics.
- [Resmo](https://www.resmo.com) - Audit and evaluate resources using SQL.
- [sq](https://github.com/neilotoole/sq) [![GitHub stars](https://img.shields.io/github/stars/neilotoole/sq?style=flat)](https://github.com/neilotoole/sq/stargazers) - Command line tool that provides jq-style access to structured data sources: SQL databases, or document formats like CSV or Excel. It is the lovechild of sql+jq.
- [Steampipe](https://github.com/turbot/steampipe) [![GitHub stars](https://img.shields.io/github/stars/turbot/steampipe?style=flat)](https://github.com/turbot/steampipe/stargazers) - Use SQL to instantly query your cloud services (AWS, Azure, GCP and more).
- [TextQL](https://github.com/dinedal/textql) [![GitHub stars](https://img.shields.io/github/stars/dinedal/textql?style=flat)](https://github.com/dinedal/textql/stargazers) - Execute SQL against structured text like CSV or TSV.
- [trdsql](https://github.com/noborus/trdsql) [![GitHub stars](https://img.shields.io/github/stars/noborus/trdsql?style=flat)](https://github.com/noborus/trdsql/stargazers) - CLI tool that can execute SQL queries on CSV, LTSV, JSON and TBLN.
- [Trino](https://github.com/trinodb/trino) [![GitHub stars](https://img.shields.io/github/stars/trinodb/trino?style=flat)](https://github.com/trinodb/trino/stargazers) - Distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources.

### Language Server Protocol
- [SQLLanguageServer](https://github.com/joe-re/sql-language-server) [![GitHub stars](https://img.shields.io/github/stars/joe-re/sql-language-server?style=flat)](https://github.com/joe-re/sql-language-server/stargazers) - SQL Language Server.
- [sqls](https://github.com/lighttiger2505/sqls) [![GitHub stars](https://img.shields.io/github/stars/lighttiger2505/sqls?style=flat)](https://github.com/lighttiger2505/sqls/stargazers) - SQL Language Server written in Go.

### Learning
Learning and puzzles for SQL
- [Advanced SQL Puzzles](https://github.com/smpetersgithub/AdvancedSQLPuzzles) [![GitHub stars](https://img.shields.io/github/stars/smpetersgithub/AdvancedSQLPuzzles?style=flat)](https://github.com/smpetersgithub/AdvancedSQLPuzzles/stargazers) - Difficult set-based SQL puzzles.
- [Hackerrank](https://www.hackerrank.com/domains/sql) - Practice coding, prepare for interviews, and get hired.
- [Learn SQL in a Month of Lunches](https://www.manning.com/books/learn-sql-in-a-month-of-lunches) - A book about how to use SQL to retrieve, filter, and analyze data.
- [LeetCode](https://leetcode.com/problemset/database) - Enhance your skills, expand your knowledge and prepare for technical interviews.
- [Select Star SQL](https://selectstarsql.com) - Free interactive book which aims to be the best place on the internet for learning SQL.
- [StrataScratch](https://www.stratascratch.com/blog/categories/sql) - Data science educational resources.
- [SQL Murder Mystery](https://github.com/NUKnightLab/sql-mysteries) [![GitHub stars](https://img.shields.io/github/stars/NUKnightLab/sql-mysteries?style=flat)](https://github.com/NUKnightLab/sql-mysteries/stargazers) - Self-directed lesson to learn SQL concepts and commands and a fun game for experienced SQL users to solve an intriguing crime.

### Plan
- [pev2](https://github.com/dalibo/pev2) [![GitHub stars](https://img.shields.io/github/stars/dalibo/pev2?style=flat)](https://github.com/dalibo/pev2/stargazers) - A Vue.js component to show a graphical vizualization of a PostgreSQL execution plan.
- [pg_flame](https://github.com/mgartner/pg_flame) [![GitHub stars](https://img.shields.io/github/stars/mgartner/pg_flame?style=flat)](https://github.com/mgartner/pg_flame/stargazers) - A flamegraph generator for PostgreSQL `EXPLAIN ANALYZE` output.

### Scripts
Useful SQL-scripts for various purposes
- [DBA MultiTool](https://github.com/LowlyDBA/dba-multitool) [![GitHub stars](https://img.shields.io/github/stars/LowlyDBA/dba-multitool?style=flat)](https://github.com/LowlyDBA/dba-multitool/stargazers) - T-SQL scripts for the long haul: optimizing storage, on-the-fly documentation, and general administrative needs for SQL Server.
- [pgx_scripts](https://github.com/pgexperts/pgx_scripts) [![GitHub stars](https://img.shields.io/github/stars/pgexperts/pgx_scripts?style=flat)](https://github.com/pgexperts/pgx_scripts/stargazers) - A collection of useful little scripts for database analysis and administration, created by our team at PostgreSQL Experts.
- [pgsql-bloat-estimation](https://github.com/ioguix/pgsql-bloat-estimation) [![GitHub stars](https://img.shields.io/github/stars/ioguix/pgsql-bloat-estimation?style=flat)](https://github.com/ioguix/pgsql-bloat-estimation/stargazers) - Queries to mesure statistical bloat in indexes and tables for PostgreSQL.
- [pgWikiDont](https://gitlab.com/depesz/pgWikiDont) - SQL test that checks if your database follows rules from <https://wiki.postgresql.org/wiki/Don't_Do_This>.
- [pg-utils](https://github.com/dataegret/pg-utils) [![GitHub stars](https://img.shields.io/github/stars/dataegret/pg-utils?style=flat)](https://github.com/dataegret/pg-utils/stargazers) - Useful PostgreSQL utilities.
- [PostgreSQL cheat sheet](https://postgrescheatsheet.com) - Useful SQL-scripts and commands by <timescale.com>.
- [postgres_dba](https://github.com/NikolayS/postgres_dba) [![GitHub stars](https://img.shields.io/github/stars/NikolayS/postgres_dba?style=flat)](https://github.com/NikolayS/postgres_dba/stargazers) - The missing set of useful tools for PostgreSQL DBAs and all engineers.
- [postgres_queries_and_commands.sql](https://gist.github.com/rgreenjr/3637525) - Useful PostgreSQL Queries and Commands.
- [TPT](https://github.com/tanelpoder/tpt-oracle) [![GitHub stars](https://img.shields.io/github/stars/tanelpoder/tpt-oracle?style=flat)](https://github.com/tanelpoder/tpt-oracle/stargazers) - These sqlplus scripts are for Oracle Database performance optimization & troubleshooting.


## Data
- [dbt](https://github.com/dbt-labs/dbt-core) [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=flat)](https://github.com/dbt-labs/dbt-core/stargazers) - Transform your data by simply writing select statements, while dbt handles turning these statements into tables and views in a data warehouse.
- [QuickTable](https://quicktable.io) - Empowers everyone to access, clean, analyze, transform, and model data with no code.

### Catalog
- [Amundsen](https://github.com/amundsen-io/amundsen) [![GitHub stars](https://img.shields.io/github/stars/amundsen-io/amundsen?style=flat)](https://github.com/amundsen-io/amundsen/stargazers) - Metadata driven application for improving the productivity of data analysts, data scientists and engineers when interacting with data.
- [DataHub](https://github.com/datahub-project/datahub) [![GitHub stars](https://img.shields.io/github/stars/datahub-project/datahub?style=flat)](https://github.com/datahub-project/datahub/stargazers) - The Metadata Platform for the Modern Data Stack.
- [Marquez](https://github.com/MarquezProject/marquez) [![GitHub stars](https://img.shields.io/github/stars/MarquezProject/marquez?style=flat)](https://github.com/MarquezProject/marquez/stargazers) - Collect, aggregate, and visualize a data ecosystem's metadata.

### Lineage
- [Dwh.dev](https://dwh.dev) - Nexgen data lineage for Snowflake.

### Generation/Masking/Subsetting
- [Benerator](https://github.com/rapiddweller/rapiddweller-benerator-ce) [![GitHub stars](https://img.shields.io/github/stars/rapiddweller/rapiddweller-benerator-ce?style=flat)](https://github.com/rapiddweller/rapiddweller-benerator-ce/stargazers) - Generate, obfuscate (anonymize / pseudonymize) and migrate data for development, testing and training purposes.
- [dbForge Data Generator for MySQL](https://www.devart.com/dbforge/mysql/data-generator) - Powerful GUI tool for creating massive volumes of realistic test data.
- [dbForge Data Generator for Oracle](https://www.devart.com/dbforge/oracle/data-generator) - Small but mighty GUI tool for populating Oracle schemas with tons of realistic test data.
- [dbForge Data Generator for SQL Server](https://www.devart.com/dbforge/sql/data-generator) - Powerful GUI tool for a fast generation of meaningful test data for databases.
- [Faker](https://github.com/faker-js/faker) [![GitHub stars](https://img.shields.io/github/stars/faker-js/faker?style=flat)](https://github.com/faker-js/faker/stargazers) - Generate massive amounts of fake data in the browser and Node.js.
- [Greenmask](https://github.com/GreenmaskIO/greenmask) [![GitHub stars](https://img.shields.io/github/stars/GreenmaskIO/greenmask?style=flat)](https://github.com/GreenmaskIO/greenmask/stargazers) - Database anonymization and synthetic data generation tool for MySQL and PostgreSQL.
- [myanon](https://github.com/ppomes/myanon) [![GitHub stars](https://img.shields.io/github/stars/ppomes/myanon?style=flat)](https://github.com/ppomes/myanon/stargazers) - Streaming anonymizer for MySQL dump files. Reads mysqldump from stdin, writes anonymized version to stdout. Supports deterministic hashing, fixed values, JSON field anonymization, and Python extensions.
- [Noisia](https://github.com/lesovsky/noisia) [![GitHub stars](https://img.shields.io/github/stars/lesovsky/noisia?style=flat)](https://github.com/lesovsky/noisia/stargazers) - Harmful workload generator for PostgreSQL.
- [quick-seed](https://github.com/miit-daga/quick-seed) [![GitHub stars](https://img.shields.io/github/stars/miit-daga/quick-seed?style=flat)](https://github.com/miit-daga/quick-seed/stargazers) - Database-agnostic seeding tool for generating realistic test data with support for PostgreSQL, MySQL, SQLite, Prisma, and Drizzle ORM.
- [SB Data Generator](https://soft-builder.com/sb-data-generator) - Simple and powerful tool to generate and populate selected tables or entire databases with realistic test data for your applications. Generate test data for: Oracle, MS SQL Server, MySQL, PostgreSQL, Firebird, SQLite, Azure SQL Database, Amazon Redshift and Amazon RDS.
- [SQLable](https://sqlable.com/generator/) - Generate fake data in the browser.
- [Synthesized TDK](https://docs.synthesized.io/tdk/latest) - DevOps' best friend for database masking and generation.

### Data Profilers
- [Data Profiler](https://github.com/capitalone/dataprofiler) [![GitHub stars](https://img.shields.io/github/stars/capitalone/dataprofiler?style=flat)](https://github.com/capitalone/dataprofiler/stargazers) - The DataProfiler is a Python library designed to make data analysis, monitoring, and sensitive data detection easy.
- [Desbordante](https://github.com/desbordante/desbordante-core) [![GitHub stars](https://img.shields.io/github/stars/desbordante/desbordante-core?style=flat)](https://github.com/desbordante/desbordante-core/stargazers) - An open-source data profiler specifically focused on discovery and validation of complex patterns in data.
- [YData Profiling](https://github.com/ydataai/ydata-profiling) [![GitHub stars](https://img.shields.io/github/stars/ydataai/ydata-profiling?style=flat)](https://github.com/ydataai/ydata-profiling/stargazers) - A general-purpose open-source data profiler for high-level analysis of a dataset.

### Replication
- [dtle](https://github.com/actiontech/dtle) [![GitHub stars](https://img.shields.io/github/stars/actiontech/dtle?style=flat)](https://github.com/actiontech/dtle/stargazers) - Distributed Data Transfer Service for MySQL.
- [Litestream](https://github.com/benbjohnson/litestream) [![GitHub stars](https://img.shields.io/github/stars/benbjohnson/litestream?style=flat)](https://github.com/benbjohnson/litestream/stargazers) - Streaming replication for SQLite.
- [pgsync](https://github.com/ankane/pgsync) [![GitHub stars](https://img.shields.io/github/stars/ankane/pgsync?style=flat)](https://github.com/ankane/pgsync/stargazers) - Sync PostgreSQL data between databases.
- [pg_chameleon](https://github.com/the4thdoctor/pg_chameleon) [![GitHub stars](https://img.shields.io/github/stars/the4thdoctor/pg_chameleon?style=flat)](https://github.com/the4thdoctor/pg_chameleon/stargazers) - MySQL to PostgreSQL replica system written in Python 3. The system use the library mysql-replication to pull the row images from MySQL which are stored into PostgreSQL as JSONB.
- [PGDeltaStream](https://github.com/hasura/pgdeltastream) [![GitHub stars](https://img.shields.io/github/stars/hasura/pgdeltastream?style=flat)](https://github.com/hasura/pgdeltastream/stargazers) - A Golang webserver to stream PostgreSQL changes atleast-once over websockets, using PostgreSQL logical decoding feature.
- [repmgr](https://github.com/2ndQuadrant/repmgr) [![GitHub stars](https://img.shields.io/github/stars/2ndQuadrant/repmgr?style=flat)](https://github.com/2ndQuadrant/repmgr/stargazers) - The Most Popular Replication Manager for PostgreSQL.

### Compare
- [data-diff](https://github.com/datafold/data-diff) [![GitHub stars](https://img.shields.io/github/stars/datafold/data-diff?style=flat)](https://github.com/datafold/data-diff/stargazers) - Command-line tool and Python library to efficiently diff rows across two different databases.
- [KS DB Merge Tools](https://ksdbmerge.tools) - GUI to compare and sync DB schema and data. For Oracle Database, MySQL, MariaDB, SQL Server, PostgreSQL, SQLite, MS Access and Cross-DBMS.

## Papers
Documents, articles, manifestos and other theoretical materials on database tools
- [The "Database as Code" Manifesto](https://github.com/mgramin/database-as-code) [![GitHub stars](https://img.shields.io/github/stars/mgramin/database-as-code?style=flat)](https://github.com/mgramin/database-as-code/stargazers) - Treat your database as Code.
- [Grokking Relational Database Design](https://www.manning.com/books/grokking-relational-database-design) - A friendly illustrated guide to designing and implementing your first database.

## Machine Learning
- [MindsDB](https://github.com/mindsdb/mindsdb) [![GitHub stars](https://img.shields.io/github/stars/mindsdb/mindsdb?style=flat)](https://github.com/mindsdb/mindsdb/stargazers) - In-database Machine Learning.
- [SQLFlow](https://github.com/sql-machine-learning/sqlflow) [![GitHub stars](https://img.shields.io/github/stars/sql-machine-learning/sqlflow?style=flat)](https://github.com/sql-machine-learning/sqlflow/stargazers) - Brings SQL and AI together.

## Contributing
- Your contributions are always welcome! Please read the [contribution guidelines](contributing.md) first.
