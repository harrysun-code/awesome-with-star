# Erlang

[![GitHub stars](https://img.shields.io/github/stars/drobakowski/awesome-erlang?style=flat)](https://github.com/drobakowski/awesome-erlang/stargazers)

# Awesome Erlang [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Analytics](https://ga-beacon.appspot.com/UA-82766782-1/awesome-erlang?flat&useReferer)](https://github.com/drobakowski/awesome-erlang)
A curated list of amazingly awesome Erlang libraries, resources and shiny thing inspired by [awesome-elixir](https://github.com/h4cc/awesome-elixir) [![GitHub stars](https://img.shields.io/github/stars/h4cc/awesome-elixir?style=flat)](https://github.com/h4cc/awesome-elixir/stargazers).

- [Awesome Erlang](#awesome-Erlang)
    - [Package Management](#package-management)
    - [Release Management](#release-management)
    - [Configuration Management](#configuration-management)
    - [Codebase Maintenance](#codebase-maintenance)
    - [Web Frameworks](#web-frameworks)
    - [Web Framework Components](#web-framework-components)
    - [HTTP](#http)
    - [Testing](#testing)
    - [Logging](#logging)
    - [Monitoring](#monitoring)
    - [Deployment](#deployment)
    - [Distributed Systems](#distributed-systems)
    - [Code Analysis](#code-analysis)
    - [Build Tools](#build-tools)
    - [Geolocation](#geolocation)
    - [Debugging](#debugging)
    - [Actors](#actors)
    - [Date and Time](#date-and-time)
    - [ORM and Datamapping](#orm-and-datamapping)
    - [Queue](#queue)
    - [Authentication](#authentication)
    - [Text and Numbers](#text-and-numbers)
    - [REST and API](#rest-and-api)
    - [Caching](#caching)
    - [Third Party APIs](#third-party-apis)
    - [Networking](#networking)
    - [Internet of Things](#internet-of-things)
    - [Algorithms and Datastructures](#algorithms-and-datastructures)
    - [Translations and Internationalizations](#translations-and-internationalizations)
    - [Miscellaneous](#miscellaneous)
- [Resources](#resources)
    - [Websites](#websites)
    - [Books](#books)
    - [Web Reading](#web-reading)
    - [Erlang Reading](#Erlang-reading)
    - [Screencasts](#screencasts)
- [Other Awesome Lists](#other-awesome-lists)
- [Contributing](#contributing)

## Package Management
*Libraries and tools for package and dependency management.*

* [hex.pm](https://hex.pm/) - A package manager for the Erlang ecosystem.

## Release Management
*Libraries and tools for release management.*

* [relx](https://github.com/erlware/relx) [![GitHub stars](https://img.shields.io/github/stars/erlware/relx?style=flat)](https://github.com/erlware/relx/stargazers) - A release assembler for Erlang.

## Configuration Management
*Libraries and tools related to configuration management.*

* [stillir](https://github.com/heroku/stillir) [![GitHub stars](https://img.shields.io/github/stars/heroku/stillir?style=flat)](https://github.com/heroku/stillir/stargazers) - Cache environment variables as Erlang app variables.

## Codebase Maintenance
*Libraries and tools to maintain a clean codebase.*

* [elvis](https://github.com/inaka/elvis) [![GitHub stars](https://img.shields.io/github/stars/inaka/elvis?style=flat)](https://github.com/inaka/elvis/stargazers) - Erlang Style Reviewer.

## Web Frameworks
*Web development frameworks.*

* [Axiom](https://github.com/tsujigiri/axiom) [![GitHub stars](https://img.shields.io/github/stars/tsujigiri/axiom?style=flat)](https://github.com/tsujigiri/axiom/stargazers) - A micro-framework, inspired by Ruby's [Sinatra](https://github.com/sinatra/sinatra) [![GitHub stars](https://img.shields.io/github/stars/sinatra/sinatra?style=flat)](https://github.com/sinatra/sinatra/stargazers).
* [ChicagoBoss](https://github.com/ChicagoBoss/ChicagoBoss) [![GitHub stars](https://img.shields.io/github/stars/ChicagoBoss/ChicagoBoss?style=flat)](https://github.com/ChicagoBoss/ChicagoBoss/stargazers) - A server framework inspired by Rails and written in Erlang.
* [cowboy](https://github.com/ninenines/cowboy) [![GitHub stars](https://img.shields.io/github/stars/ninenines/cowboy?style=flat)](https://github.com/ninenines/cowboy/stargazers) - A simple HTTP server.
* [Giallo](https://github.com/kivra/giallo) [![GitHub stars](https://img.shields.io/github/stars/kivra/giallo?style=flat)](https://github.com/kivra/giallo/stargazers) - A small and flexible web framework on top of [Cowboy](https://github.com/ninenines/cowboy) [![GitHub stars](https://img.shields.io/github/stars/ninenines/cowboy?style=flat)](https://github.com/ninenines/cowboy/stargazers).
* [MochiWeb](https://github.com/mochi/mochiweb) [![GitHub stars](https://img.shields.io/github/stars/mochi/mochiweb?style=flat)](https://github.com/mochi/mochiweb/stargazers) - An Erlang library for building lightweight HTTP servers.
* [N2O](https://github.com/synrc/n2o) [![GitHub stars](https://img.shields.io/github/stars/synrc/n2o?style=flat)](https://github.com/synrc/n2o/stargazers) - WebSocket Application Server.
* [Nitrogen](https://github.com/nitrogen/nitrogen) [![GitHub stars](https://img.shields.io/github/stars/nitrogen/nitrogen?style=flat)](https://github.com/nitrogen/nitrogen/stargazers) - Framework to build web applications (including front-end) in pure Erlang.
* [Zotonic](https://github.com/zotonic/zotonic) [![GitHub stars](https://img.shields.io/github/stars/zotonic/zotonic?style=flat)](https://github.com/zotonic/zotonic/stargazers) - High speed, real-time web framework and content management system.

## Web Framework Components
*Standalone component from web development frameworks.*

* [cb_admin](https://github.com/ChicagoBoss/cb_admin) [![GitHub stars](https://img.shields.io/github/stars/ChicagoBoss/cb_admin?style=flat)](https://github.com/ChicagoBoss/cb_admin/stargazers) - An admin interface for Chicago Boss.
* [cb_websocket_controller](https://github.com/dkuhlman/cb_websocket_controller) [![GitHub stars](https://img.shields.io/github/stars/dkuhlman/cb_websocket_controller?style=flat)](https://github.com/dkuhlman/cb_websocket_controller/stargazers) - A template for implementing a Websocket controller for ChicagoBoss.
* [giallo_session](https://github.com/kivra/giallo_session) [![GitHub stars](https://img.shields.io/github/stars/kivra/giallo_session?style=flat)](https://github.com/kivra/giallo_session/stargazers) - A session management library for the Giallo web framework.
* [simple_bridge](https://github.com/nitrogen/simple_bridge) [![GitHub stars](https://img.shields.io/github/stars/nitrogen/simple_bridge?style=flat)](https://github.com/nitrogen/simple_bridge/stargazers) - An abstraction layer providing a unified interface to popular Erlang web servers (Cowboy, Inets, Mochiweb, Webmachine, and Yaws).

## HTTP
*Libraries for working with HTTP and scraping websites.*

* [bullet](https://github.com/ninenines/bullet) [![GitHub stars](https://img.shields.io/github/stars/ninenines/bullet?style=flat)](https://github.com/ninenines/bullet/stargazers) - Simple, reliable, efficient streaming for Cowboy.
* [gun](https://github.com/ninenines/gun) [![GitHub stars](https://img.shields.io/github/stars/ninenines/gun?style=flat)](https://github.com/ninenines/gun/stargazers) - Erlang HTTP client with support for HTTP/1.1, SPDY and Websocket.
* [hackney](https://github.com/benoitc/hackney) [![GitHub stars](https://img.shields.io/github/stars/benoitc/hackney?style=flat)](https://github.com/benoitc/hackney/stargazers) - Simple HTTP client in Erlang.
* [ibrowse](https://github.com/cmullaparthi/ibrowse) [![GitHub stars](https://img.shields.io/github/stars/cmullaparthi/ibrowse?style=flat)](https://github.com/cmullaparthi/ibrowse/stargazers) - Erlang HTTP client.
* [lhttpc](https://github.com/esl/lhttpc) [![GitHub stars](https://img.shields.io/github/stars/esl/lhttpc?style=flat)](https://github.com/esl/lhttpc/stargazers) - A lightweight HTTP/1.1 client implemented in Erlang.
* [shotgun](https://github.com/inaka/shotgun) [![GitHub stars](https://img.shields.io/github/stars/inaka/shotgun?style=flat)](https://github.com/inaka/shotgun/stargazers) - For the times you need more than just a gun.

## Testing
*Libraries for testing codebases and generating test data.*

* [PropEr](https://github.com/manopapad/proper) [![GitHub stars](https://img.shields.io/github/stars/manopapad/proper?style=flat)](https://github.com/manopapad/proper/stargazers) - A QuickCheck-inspired property-based testing tool for Erlang.
* [tracerl](https://github.com/esl/tracerl) [![GitHub stars](https://img.shields.io/github/stars/esl/tracerl?style=flat)](https://github.com/esl/tracerl/stargazers) - Dynamic tracing tests and utilities for Erlang/OTP

## Logging
*Libraries for generating and working with log files.*

* [lager](https://github.com/basho/lager) [![GitHub stars](https://img.shields.io/github/stars/basho/lager?style=flat)](https://github.com/basho/lager/stargazers) - A logging framework for Erlang/OTP.
* [lager_amqp_backend](https://github.com/jbrisbin/lager_amqp_backend) [![GitHub stars](https://img.shields.io/github/stars/jbrisbin/lager_amqp_backend?style=flat)](https://github.com/jbrisbin/lager_amqp_backend/stargazers) - AMQP RabbitMQ Lager backend.
* [lager_hipchat](https://github.com/synlay/lager_hipchat) [![GitHub stars](https://img.shields.io/github/stars/synlay/lager_hipchat?style=flat)](https://github.com/synlay/lager_hipchat/stargazers) - HipChat backend for lager.
* [lager_loggly](https://github.com/kivra/lager_loggly) [![GitHub stars](https://img.shields.io/github/stars/kivra/lager_loggly?style=flat)](https://github.com/kivra/lager_loggly/stargazers) - Loggly backend for lager.
* [lager_smtp](https://github.com/blinkov/lager_smtp) [![GitHub stars](https://img.shields.io/github/stars/blinkov/lager_smtp?style=flat)](https://github.com/blinkov/lager_smtp/stargazers) - SMTP backend for lager.
* [lager_slack](https://github.com/furmanOFF/lager_slack) [![GitHub stars](https://img.shields.io/github/stars/furmanOFF/lager_slack?style=flat)](https://github.com/furmanOFF/lager_slack/stargazers) - Simple Slack backend for lager.
* [logplex](https://github.com/heroku/logplex) [![GitHub stars](https://img.shields.io/github/stars/heroku/logplex?style=flat)](https://github.com/heroku/logplex/stargazers) - Heroku log router.

## Monitoring
*Libraries for gathering metrics and monitoring.*

* [entop](https://github.com/mazenharake/entop) [![GitHub stars](https://img.shields.io/github/stars/mazenharake/entop?style=flat)](https://github.com/mazenharake/entop/stargazers) - A top-like Erlang node monitoring tool.
* [eper](https://github.com/massemanet/eper) [![GitHub stars](https://img.shields.io/github/stars/massemanet/eper?style=flat)](https://github.com/massemanet/eper/stargazers) - A loose collection of Erlang Performance related tools.
* [Exometer](https://github.com/Feuerlabs/exometer) [![GitHub stars](https://img.shields.io/github/stars/Feuerlabs/exometer?style=flat)](https://github.com/Feuerlabs/exometer/stargazers) - An Erlang instrumentation package.
* [folsom](https://github.com/boundary/folsom) [![GitHub stars](https://img.shields.io/github/stars/boundary/folsom?style=flat)](https://github.com/boundary/folsom/stargazers) - An Erlang based metrics system inspired by Coda Hale's [metrics](https://github.com/codahale/metrics) [![GitHub stars](https://img.shields.io/github/stars/codahale/metrics?style=flat)](https://github.com/codahale/metrics/stargazers).
* [statsderl](https://github.com/lpgauth/statsderl) [![GitHub stars](https://img.shields.io/github/stars/lpgauth/statsderl?style=flat)](https://github.com/lpgauth/statsderl/stargazers) - A statsd Erlang client.
* [vmstats](https://github.com/ferd/vmstats) [![GitHub stars](https://img.shields.io/github/stars/ferd/vmstats?style=flat)](https://github.com/ferd/vmstats/stargazers) - Tiny Erlang app that works in conjunction with statsderl in order to generate information on the Erlang VM for graphite logs.

## Deployment
*Libraries and tools related to deployment of Erlang/OTP applications.*

* [docker-erlang](https://github.com/synlay/docker-erlang) [![GitHub stars](https://img.shields.io/github/stars/synlay/docker-erlang?style=flat)](https://github.com/synlay/docker-erlang/stargazers) - Basic Docker Container Images for Erlang/OTP.

## Distributed Systems
 *Tools for stress/load testing, latency issues, etc. across microservices.*

 * [Typhoon](https://github.com/fogfish/typhoon) [![GitHub stars](https://img.shields.io/github/stars/fogfish/typhoon?style=flat)](https://github.com/fogfish/typhoon/stargazers) - Stress and load testing tool for distributed systems that simulates traffic from a test cluster toward a system-under-test (SUT) and visualizes related latencies.
## Code Analysis
*Libraries and tools for analysing, parsing and manipulation codebases.*

* [Concuerror](https://github.com/parapluu/Concuerror) [![GitHub stars](https://img.shields.io/github/stars/parapluu/Concuerror?style=flat)](https://github.com/parapluu/Concuerror/stargazers) - Concuerror is a systematic testing tool for concurrent Erlang programs.
* [eflame](https://github.com/proger/eflame) [![GitHub stars](https://img.shields.io/github/stars/proger/eflame?style=flat)](https://github.com/proger/eflame/stargazers) - A Flame Graph profiler for Erlang.
* [geas](https://github.com/crownedgrouse/geas) [![GitHub stars](https://img.shields.io/github/stars/crownedgrouse/geas?style=flat)](https://github.com/crownedgrouse/geas/stargazers) - Geas is a tool that will detect the runnable official Erlang release window for your project, including its dependencies and provides many useful informations.

## Build Tools
*Project build and automation tools.*

* [rebar](https://github.com/rebar/rebar) [![GitHub stars](https://img.shields.io/github/stars/rebar/rebar?style=flat)](https://github.com/rebar/rebar/stargazers) - Erlang build tool that makes it easy to compile and test Erlang applications, port drivers and releases.
* [rebar3](https://github.com/rebar/rebar3) [![GitHub stars](https://img.shields.io/github/stars/rebar/rebar3?style=flat)](https://github.com/rebar/rebar3/stargazers) - A build tool for Erlang which can manage Erlang packages from [Hex.pm](https://hex.pm/). See more at [rebar3.org](https://www.rebar3.org/)
* [sync](https://github.com/rustyio/sync) [![GitHub stars](https://img.shields.io/github/stars/rustyio/sync?style=flat)](https://github.com/rustyio/sync/stargazers) - On-the-fly recompiling for Erlang.

## Geolocation
*Libraries for geocoding addresses and working with latitudes and longitudes.*

* [erl-rstar](https://github.com/armon/erl-rstar) [![GitHub stars](https://img.shields.io/github/stars/armon/erl-rstar?style=flat)](https://github.com/armon/erl-rstar/stargazers) - An Erlang implementation of the R*-tree spacial data structure.
* [GeoCouch](https://github.com/couchbase/geocouch) [![GitHub stars](https://img.shields.io/github/stars/couchbase/geocouch?style=flat)](https://github.com/couchbase/geocouch/stargazers) - A spatial extension for Couchbase and Apache CouchDB.
* [Teles](https://github.com/armon/teles) [![GitHub stars](https://img.shields.io/github/stars/armon/teles?style=flat)](https://github.com/armon/teles/stargazers) - An Erlang network service for manipulating geographic data.

## Debugging
*Libraries and tools for debugging code and applications.*

* [tx](https://github.com/kvakvs/tx) [![GitHub stars](https://img.shields.io/github/stars/kvakvs/tx?style=flat)](https://github.com/kvakvs/tx/stargazers) - An HTML Erlang term viewer, starts own webserver and displays any term you give it from your Erlang node.

## Actors
*Libraries and tools for working with actors and such.*

* [poolboy](https://github.com/devinus/poolboy) [![GitHub stars](https://img.shields.io/github/stars/devinus/poolboy?style=flat)](https://github.com/devinus/poolboy/stargazers) - A hunky Erlang worker pool factory.

## Date and Time
*Libraries for working with dates and times.*

* [erlang_localtime](https://github.com/dmitryme/erlang_localtime) [![GitHub stars](https://img.shields.io/github/stars/dmitryme/erlang_localtime?style=flat)](https://github.com/dmitryme/erlang_localtime/stargazers) - Erlang library for conversion from one local time to another.
* [qdate](https://github.com/choptastic/qdate) [![GitHub stars](https://img.shields.io/github/stars/choptastic/qdate?style=flat)](https://github.com/choptastic/qdate/stargazers) - Erlang date, time, and timezone management: formatting, conversion, and date arithmetic.

## ORM and Datamapping
*Libraries that implement object-relational mapping or datamapping techniques.*

* [boss_db](https://github.com/ErlyORM/boss_db) [![GitHub stars](https://img.shields.io/github/stars/ErlyORM/boss_db?style=flat)](https://github.com/ErlyORM/boss_db/stargazers) - A sharded, caching, pooling, evented ORM for Erlang.
* [epgsql](https://github.com/epgsql/epgsql) [![GitHub stars](https://img.shields.io/github/stars/epgsql/epgsql?style=flat)](https://github.com/epgsql/epgsql/stargazers) - PostgreSQL Driver for Erlang.
* [mysql-otp](https://github.com/mysql-otp/mysql-otp) [![GitHub stars](https://img.shields.io/github/stars/mysql-otp/mysql-otp?style=flat)](https://github.com/mysql-otp/mysql-otp/stargazers) - MySQL/OTP – MySQL driver for Erlang/OTP.
* [pgsql_migration](https://github.com/artemeff/pgsql_migration) [![GitHub stars](https://img.shields.io/github/stars/artemeff/pgsql_migration?style=flat)](https://github.com/artemeff/pgsql_migration/stargazers) – PostgreSQL migrations for Erlang.

## Queue
*Libraries for working with event and task queues.*

* [dq](https://github.com/darach/dq) [![GitHub stars](https://img.shields.io/github/stars/darach/dq?style=flat)](https://github.com/darach/dq/stargazers) - Distributed Fault Tolerant Queue library.
* [ebqueue](https://github.com/rgrinberg/ebqueue) [![GitHub stars](https://img.shields.io/github/stars/rgrinberg/ebqueue?style=flat)](https://github.com/rgrinberg/ebqueue/stargazers) - Tiny simple blocking queue in erlang.
* [pqueue](https://github.com/okeuday/pqueue) [![GitHub stars](https://img.shields.io/github/stars/okeuday/pqueue?style=flat)](https://github.com/okeuday/pqueue/stargazers) - Erlang Priority Queues.
* [tinymq](https://github.com/ChicagoBoss/tinymq) [![GitHub stars](https://img.shields.io/github/stars/ChicagoBoss/tinymq?style=flat)](https://github.com/ChicagoBoss/tinymq/stargazers) - A diminutive, in-memory message queue for Erlang.

## Authentication
*Libraries for implementing authentications schemes.*

* [oauth2](https://github.com/kivra/oauth2) [![GitHub stars](https://img.shields.io/github/stars/kivra/oauth2?style=flat)](https://github.com/kivra/oauth2/stargazers) - Erlang Oauth2 implementation.

## Text and Numbers
*Libraries for parsing and manipulating text and numbers.*

* [ejsv](https://github.com/patternmatched/ejsv) [![GitHub stars](https://img.shields.io/github/stars/patternmatched/ejsv?style=flat)](https://github.com/patternmatched/ejsv/stargazers) - Erlang JSON schema validator.
* [eql](https://github.com/artemeff/eql) [![GitHub stars](https://img.shields.io/github/stars/artemeff/eql?style=flat)](https://github.com/artemeff/eql/stargazers) - Erlang with SQL or not.
* [jiffy](https://github.com/davisp/jiffy) [![GitHub stars](https://img.shields.io/github/stars/davisp/jiffy?style=flat)](https://github.com/davisp/jiffy/stargazers) - JSON NIFs for Erlang.
* [jsx](https://github.com/talentdeficit/jsx) [![GitHub stars](https://img.shields.io/github/stars/talentdeficit/jsx?style=flat)](https://github.com/talentdeficit/jsx/stargazers) - An erlang application for consuming, producing and manipulating json.
* [miffy](https://github.com/expelledboy/miffy) [![GitHub stars](https://img.shields.io/github/stars/expelledboy/miffy?style=flat)](https://github.com/expelledboy/miffy/stargazers) - Jiffy wrapper which returns pretty maps.
* [qsp](https://github.com/artemeff/qsp) [![GitHub stars](https://img.shields.io/github/stars/artemeff/qsp?style=flat)](https://github.com/artemeff/qsp/stargazers) - Enhanced query string parser for Erlang.
* [rec2json](https://github.com/lordnull/rec2json) [![GitHub stars](https://img.shields.io/github/stars/lordnull/rec2json?style=flat)](https://github.com/lordnull/rec2json/stargazers) - Generate JSON encoder/decoder from record specs.

## REST and API
*Libraries and web tools for developing REST-ful APIs.*

* [leptus](https://github.com/s1n4/leptus) [![GitHub stars](https://img.shields.io/github/stars/s1n4/leptus?style=flat)](https://github.com/s1n4/leptus/stargazers) - Leptus is an Erlang REST framework that runs on top of cowboy.
* [rooster](https://github.com/FelipeBB/rooster) [![GitHub stars](https://img.shields.io/github/stars/FelipeBB/rooster?style=flat)](https://github.com/FelipeBB/rooster/stargazers) - rooster is a lightweight REST framework that runs on top of mochiweb.

## Caching
*Libraries for caching data.*

* [cache](https://github.com/fogfish/cache) [![GitHub stars](https://img.shields.io/github/stars/fogfish/cache?style=flat)](https://github.com/fogfish/cache/stargazers) - In-memory Segmented Cache

## Third Party APIs
*Libraries for accessing third party APIs.*

* [google-token-erlang](https://github.com/ruel/google-token-erlang) [![GitHub stars](https://img.shields.io/github/stars/ruel/google-token-erlang?style=flat)](https://github.com/ruel/google-token-erlang/stargazers) - Google ID token verifier for Erlang.
* [restc](https://github.com/kivra/restclient) [![GitHub stars](https://img.shields.io/github/stars/kivra/restclient?style=flat)](https://github.com/kivra/restclient/stargazers) - An Erlang REST client
* [oauth2c](https://github.com/kivra/oauth2_client) [![GitHub stars](https://img.shields.io/github/stars/kivra/oauth2_client?style=flat)](https://github.com/kivra/oauth2_client/stargazers) - An Erlang oAuth 2 client (uses restc)

## Networking
*Libraries and tools for using network related stuff.*

* [barrel_tcp](https://github.com/benoitc-attic/barrel_tcp) [![GitHub stars](https://img.shields.io/github/stars/benoitc-attic/barrel_tcp?style=flat)](https://github.com/benoitc-attic/barrel_tcp/stargazers) - barrel_tcp is a generic TCP acceptor pool with low latency in Erlang.
* [gen_rpc](https://github.com/priestjim/gen_rpc) [![GitHub stars](https://img.shields.io/github/stars/priestjim/gen_rpc?style=flat)](https://github.com/priestjim/gen_rpc/stargazers) - A scalable RPC library for Erlang-VM based languages.
* [gen_tcp_server](https://github.com/rpt/gen_tcp_server) [![GitHub stars](https://img.shields.io/github/stars/rpt/gen_tcp_server?style=flat)](https://github.com/rpt/gen_tcp_server/stargazers) - A library that takes the concept of gen_server and introduces the same mechanics for operating a TCP server.
* [gossiperl](https://github.com/gossiperl/gossiperl) [![GitHub stars](https://img.shields.io/github/stars/gossiperl/gossiperl?style=flat)](https://github.com/gossiperl/gossiperl/stargazers) - Language agnostic gossip middleware and message bus written in Erlang.
* [nat_upnp](https://github.com/benoitc/nat_upnp) [![GitHub stars](https://img.shields.io/github/stars/benoitc/nat_upnp?style=flat)](https://github.com/benoitc/nat_upnp/stargazers) - Erlang library to map your internal port to an external using UNP IGD.
* [ranch](https://github.com/ninenines/ranch) [![GitHub stars](https://img.shields.io/github/stars/ninenines/ranch?style=flat)](https://github.com/ninenines/ranch/stargazers) - Socket acceptor pool for TCP protocols.

## Internet of Things
*Libraries and tools for interacting with the physical world.*

* [GRiSP](https://grisp.org/) - Run the Erlang VM on an IoT board with many hardware interfaces and low-level drivers using a small realtime unikernel called RTEMS
* [lemma_erlang](https://github.com/noam-io/lemma_erlang) [![GitHub stars](https://img.shields.io/github/stars/noam-io/lemma_erlang?style=flat)](https://github.com/noam-io/lemma_erlang/stargazers) - A lemma for IDEO's Noam internet-of-things prototyping platform.

## Algorithms and Datastructures
*Libraries and implementations of algorithms and datastructures.*

* [datum](https://github.com/fogfish/datum) [![GitHub stars](https://img.shields.io/github/stars/fogfish/datum?style=flat)](https://github.com/fogfish/datum/stargazers) - A pure functional and generic programming for Erlang
* [erlando](https://github.com/travelping/erlando) [![GitHub stars](https://img.shields.io/github/stars/travelping/erlando?style=flat)](https://github.com/travelping/erlando/stargazers) - A set of syntax extensions like currying and monads for Erlang.
* [statebox](https://github.com/mochi/statebox) [![GitHub stars](https://img.shields.io/github/stars/mochi/statebox?style=flat)](https://github.com/mochi/statebox/stargazers) - Erlang state "monad" with merge/conflict-resolution capabilities.
* [riak_dt](https://github.com/basho/riak_dt) [![GitHub stars](https://img.shields.io/github/stars/basho/riak_dt?style=flat)](https://github.com/basho/riak_dt/stargazers) - Erlang library of state based CRDTs.

## Translations and Internationalizations
*Libraries providing translations or internationalizations.*

## Miscellaneous
*Useful libraries or tools that don't fit in the categories above.*

* [erlang-history](https://github.com/ferd/erlang-history) [![GitHub stars](https://img.shields.io/github/stars/ferd/erlang-history?style=flat)](https://github.com/ferd/erlang-history/stargazers) - Hacks to add shell history to Erlang's shell.
* [erld](https://github.com/ShoreTel-Inc/erld) [![GitHub stars](https://img.shields.io/github/stars/ShoreTel-Inc/erld?style=flat)](https://github.com/ShoreTel-Inc/erld/stargazers) - erld is a small program designed to solve the problem of running Erlang programs as a UNIX daemon.

# Resources
Various resources, such as books, websites and articles, for improving your Erlang development skills and knowledge.

## Websites
*Useful web and Erlang-related websites and newsletters.*

* [Erlang Bookmarks](https://github.com/0xAX/erlang-bookmarks/wiki/Erlang-bookmarks) [![GitHub stars](https://img.shields.io/github/stars/0xAX/erlang-bookmarks/wiki/Erlang-bookmarks?style=flat)](https://github.com/0xAX/erlang-bookmarks/wiki/Erlang-bookmarks/stargazers) - All about erlang programming language [powerd by community].
* [Erlang Central](https://erlangcentral.org/) - An awesome collections of erlang resource along with live community chat for discussing and seeking help.
* [Planet Erlang](http://www.planeterlang.com/) - Planet site/RSS feed of blog posts covering topics across the Erlang ecosystem.
* [Spawned Shelter](http://spawnedshelter.com/) - Erlang Spawned Shelter. A collection of the best articles, videos and presentations related to Erlang.

## Books
*Fantastic books and e-books.*

* [Erlang and Elixir for Imperative Programmers](https://leanpub.com/erlangandelixirforimperativeprogrammers) - Introduction to Erlang and Elixir in the context of functional concepts by Wolfgang Loder (2016)
* [Learn You Some Erlang](http://learnyousomeerlang.com/) - Learn you some Erlang - for great good! A very thorough resource covering everything from beginning Erlang programming to large-scale development and deployment.
* [Stuff Goes Bad - ERLANG IN ANGER](http://www.erlang-in-anger.com/) - This book intends to be a little guide about how to be the Erlang medic in a time of war.

## Web Reading
*General web-development-related reading materials.*

## Erlang Reading
*Erlang-releated reading materials.*

* [The Joy of Erlang; Or, How To Ride A Toruk](http://www.evanmiller.org/joy-of-erlang.html) - The Joy of Erlang; Or, How To Ride A Toruk A fast track introduction to Erlang that teaches the language by walking through a few example projects.

## Screencasts
*Cool video tutorials.*

# Contributing
Please see [CONTRIBUTING](https://github.com/drobakowski/awesome-erlang/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/drobakowski/awesome-erlang/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/drobakowski/awesome-erlang/blob/master/CONTRIBUTING.md/stargazers) for details.
