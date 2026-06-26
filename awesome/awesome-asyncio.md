# Asyncio

[![GitHub stars](https://img.shields.io/github/stars/timofurrer/awesome-asyncio?style=flat)](https://github.com/timofurrer/awesome-asyncio/stargazers)

> [!WARNING]
> This project is looking for a new home. I'm no longer maintaining it.
> Please let me know if you want to take over maintainance for it.
> Write me an email to timo@furrer.life

# Awesome asyncio [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A carefully curated list of awesome Python asyncio frameworks, libraries, software and resources.

The Python [asyncio](https://docs.python.org/3/library/asyncio.html) module introduced to the standard library with Python 3.4 provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.

Asyncio is not really a brand-new technology however it appears to be very trending since a few years - especially in the Python community and with the release of Python 3.4 in March 2014.
Thus, it's pretty hard to keep yourself up-to-date with the most awesome packages out there.
Find some of those *awesome* packages here and if you are missing one we count on you to [create an Issue or a Pull Request](https://github.com/timofurrer/awesome-asyncio/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/timofurrer/awesome-asyncio/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/timofurrer/awesome-asyncio/blob/master/CONTRIBUTING.md/stargazers) with your suggestion.


## Contents

* [Web Frameworks](#web-frameworks)
* [Message Queues](#message-queues)
* [Database Drivers](#database-drivers)
* [Networking](#networking)
* [GraphQL](#graphql)
* [Testing](#testing)
* [Alternative Loops](#alternative-loops)
* [Misc](#misc)
* [Writings](#writings)
* [Talks](#talks)
* [Alternatives to asyncio](#alternatives-to-asyncio)

***

## Web Frameworks

*Libraries to build web applications.*

* [FastAPI](https://github.com/tiangolo/fastapi) [![GitHub stars](https://img.shields.io/github/stars/tiangolo/fastapi?style=flat)](https://github.com/tiangolo/fastapi/stargazers) - A very high performance Python 3.6+ API framework based on type hints. Powered by Starlette and Pydantic.
* [Django](https://www.djangoproject.com/) - An established, high-level Python web framework with a huge community and ecosystem.
* [Starlette](https://github.com/encode/starlette) [![GitHub stars](https://img.shields.io/github/stars/encode/starlette?style=flat)](https://github.com/encode/starlette/stargazers) - A lightweight ASGI framework/toolkit for building high performance services.
* [aiohttp](https://github.com/KeepSafe/aiohttp) [![GitHub stars](https://img.shields.io/github/stars/KeepSafe/aiohttp?style=flat)](https://github.com/KeepSafe/aiohttp/stargazers) - Http client/server for asyncio (PEP-3156).
* [sanic](https://github.com/channelcat/sanic) [![GitHub stars](https://img.shields.io/github/stars/channelcat/sanic?style=flat)](https://github.com/channelcat/sanic/stargazers) - Python 3.5+ web server that's written to go fast.
* [Quart](https://github.com/pallets/quart) [![GitHub stars](https://img.shields.io/github/stars/pallets/quart?style=flat)](https://github.com/pallets/quart/stargazers) - An asyncio web microframework with the same API as Flask.
* [autobahn](https://github.com/crossbario/autobahn-python) [![GitHub stars](https://img.shields.io/github/stars/crossbario/autobahn-python?style=flat)](https://github.com/crossbario/autobahn-python/stargazers) - WebSocket and WAMP supporting asyncio and Twisted, for clients and servers.
* [websockets](https://github.com/aaugustin/websockets/) [![GitHub stars](https://img.shields.io/github/stars/aaugustin/websockets/?style=flat)](https://github.com/aaugustin/websockets//stargazers) - A library for building WebSocket servers and clients in Python with a focus on correctness and simplicity.
* [Tornado](http://www.tornadoweb.org/en/stable/) - Performant web framework and asynchronous networking library.
* [uvicorn](https://github.com/encode/uvicorn) [![GitHub stars](https://img.shields.io/github/stars/encode/uvicorn?style=flat)](https://github.com/encode/uvicorn/stargazers) - The lightning-fast ASGI server.


## Message Queues

*Libraries to implement applications using message queues.*

* [aioamqp](https://github.com/Polyconseil/aioamqp) [![GitHub stars](https://img.shields.io/github/stars/Polyconseil/aioamqp?style=flat)](https://github.com/Polyconseil/aioamqp/stargazers) - AMQP implementation using asyncio.
* [pyzmq](https://github.com/zeromq/pyzmq) [![GitHub stars](https://img.shields.io/github/stars/zeromq/pyzmq?style=flat)](https://github.com/zeromq/pyzmq/stargazers) - Python bindings for ZeroMQ.
* [aiozmq](https://github.com/aio-libs/aiozmq) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiozmq?style=flat)](https://github.com/aio-libs/aiozmq/stargazers) - Alternative Asyncio integration with ZeroMQ.
* [crossbar](https://github.com/crossbario/crossbar) [![GitHub stars](https://img.shields.io/github/stars/crossbario/crossbar?style=flat)](https://github.com/crossbario/crossbar/stargazers) - Crossbar.io is a networking platform for distributed and microservice applications.
* [asyncio-nats](https://github.com/nats-io/asyncio-nats) [![GitHub stars](https://img.shields.io/github/stars/nats-io/asyncio-nats?style=flat)](https://github.com/nats-io/asyncio-nats/stargazers) - Client for the NATS messaging system.
* [aiokafka](https://github.com/aio-libs/aiokafka) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiokafka?style=flat)](https://github.com/aio-libs/aiokafka/stargazers) - Client for Apache Kafka.

## Database Drivers

*Libraries to connect to databases.*

* [asyncpg](https://github.com/MagicStack/asyncpg) [![GitHub stars](https://img.shields.io/github/stars/MagicStack/asyncpg?style=flat)](https://github.com/MagicStack/asyncpg/stargazers) - Fast PostgreSQL Database Client Library for Python/asyncio.
* [asyncpgsa](https://github.com/CanopyTax/asyncpgsa) [![GitHub stars](https://img.shields.io/github/stars/CanopyTax/asyncpgsa?style=flat)](https://github.com/CanopyTax/asyncpgsa/stargazers) - Asyncpg with sqlalchemy core support.
* [aiopg](https://github.com/aio-libs/aiopg/) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiopg/?style=flat)](https://github.com/aio-libs/aiopg//stargazers) - Library for accessing a PostgreSQL database.
* [aiomysql](https://github.com/aio-libs/aiomysql) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiomysql?style=flat)](https://github.com/aio-libs/aiomysql/stargazers) - Library for accessing a MySQL database
* [aioodbc](https://github.com/aio-libs/aioodbc) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aioodbc?style=flat)](https://github.com/aio-libs/aioodbc/stargazers) - Library for accessing a ODBC databases.
* [pymongo](https://github.com/mongodb/mongo-python-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-python-driver?style=flat)](https://github.com/mongodb/mongo-python-driver/stargazers) - The Official MongoDB Python driver, offering both synchronous and asynchronous APIs.
* [redis-py](https://github.com/redis/redis-py) [![GitHub stars](https://img.shields.io/github/stars/redis/redis-py?style=flat)](https://github.com/redis/redis-py/stargazers) - Redis Python Client (which includes [aioreadis](https://github.com/aio-libs/aioredis) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aioredis?style=flat)](https://github.com/aio-libs/aioredis/stargazers) now).
* [aiocouchdb](https://github.com/aio-libs/aiocouchdb) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiocouchdb?style=flat)](https://github.com/aio-libs/aiocouchdb/stargazers) - CouchDB client built on top of aiohttp (asyncio).
* [aioinflux](https://github.com/plugaai/aioinflux) [![GitHub stars](https://img.shields.io/github/stars/plugaai/aioinflux?style=flat)](https://github.com/plugaai/aioinflux/stargazers) - InfluxDB client built on top of aiohttp.
* [aioes](https://github.com/aio-libs/aioes) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aioes?style=flat)](https://github.com/aio-libs/aioes/stargazers) - Asyncio compatible driver for elasticsearch.
* [peewee-async](https://github.com/05bit/peewee-async) [![GitHub stars](https://img.shields.io/github/stars/05bit/peewee-async?style=flat)](https://github.com/05bit/peewee-async/stargazers) - ORM implementation based on [peewee](https://github.com/coleifer/peewee) [![GitHub stars](https://img.shields.io/github/stars/coleifer/peewee?style=flat)](https://github.com/coleifer/peewee/stargazers) and aiopg.
* [GINO](https://github.com/fantix/gino) [![GitHub stars](https://img.shields.io/github/stars/fantix/gino?style=flat)](https://github.com/fantix/gino/stargazers) - is a lightweight asynchronous Python ORM based on [SQLAlchemy](https://www.sqlalchemy.org/) core, with [asyncpg](https://github.com/MagicStack/asyncpg) [![GitHub stars](https://img.shields.io/github/stars/MagicStack/asyncpg?style=flat)](https://github.com/MagicStack/asyncpg/stargazers) dialect.
* [Tortoise ORM](https://github.com/tortoise/tortoise-orm) [![GitHub stars](https://img.shields.io/github/stars/tortoise/tortoise-orm?style=flat)](https://github.com/tortoise/tortoise-orm/stargazers) - native multi-backend ORM with Django-like API and easy relations management.
* [Databases](https://github.com/encode/databases) [![GitHub stars](https://img.shields.io/github/stars/encode/databases?style=flat)](https://github.com/encode/databases/stargazers) - Async database access for SQLAlchemy core, with support for PostgreSQL, MySQL, and SQLite.
* [Prisma Client Python](https://github.com/RobertCraigie/prisma-client-py) [![GitHub stars](https://img.shields.io/github/stars/RobertCraigie/prisma-client-py?style=flat)](https://github.com/RobertCraigie/prisma-client-py/stargazers) - An auto-generated, fully type safe ORM powered by Pydantic and tailored specifically for your schema - supports SQLite, PostgreSQL, MySQL, MongoDB, MariaDB and more.
* [Piccolo](https://github.com/piccolo-orm/piccolo) [![GitHub stars](https://img.shields.io/github/stars/piccolo-orm/piccolo?style=flat)](https://github.com/piccolo-orm/piccolo/stargazers) - An ORM / query builder which can work in async and sync modes, with a nice admin GUI, and ASGI middleware.
* [Beanie](https://beanie-odm.dev) - An async MongoDB ODM built on [pymongo](https://github.com/mongodb/mongo-python-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-python-driver?style=flat)](https://github.com/mongodb/mongo-python-driver/stargazers) and [Pydantic](https://pydantic-docs.helpmanual.io).

## Networking

*Libraries to communicate in your network.*

* [AsyncSSH](https://github.com/ronf/asyncssh) [![GitHub stars](https://img.shields.io/github/stars/ronf/asyncssh?style=flat)](https://github.com/ronf/asyncssh/stargazers) - Provides an asynchronous client and server implementation of the SSHv2 protocol.
* [aiodns](https://github.com/saghul/aiodns) [![GitHub stars](https://img.shields.io/github/stars/saghul/aiodns?style=flat)](https://github.com/saghul/aiodns/stargazers) - Simple DNS resolver for asyncio.
* [aioping](https://github.com/stellarbit/aioping) [![GitHub stars](https://img.shields.io/github/stars/stellarbit/aioping?style=flat)](https://github.com/stellarbit/aioping/stargazers) - Fast asyncio implementation of ICMP (ping) protocol.
* [httpx](https://github.com/encode/httpx) [![GitHub stars](https://img.shields.io/github/stars/encode/httpx?style=flat)](https://github.com/encode/httpx/stargazers) - asynchronous HTTP client for Python 3 with [requests](https://github.com/psf/requests) [![GitHub stars](https://img.shields.io/github/stars/psf/requests?style=flat)](https://github.com/psf/requests/stargazers) compatible API.

## GraphQL

*Libraries to build GraphQL servers.*

* [Ariadne](https://ariadnegraphql.org) - Schema-first Python library for implementing GraphQL servers.
* [Tartiflette](https://tartiflette.io/) - Schema-first Python 3.6+ GraphQL engine built on top of `libgraphqlparser`.
* [Strawberry](https://strawberry.rocks) - Code-first Python 3 GraphQL server with Django, Flask and FastAPI/Starlette support.

## Testing

*Libraries to test asyncio based applications.*

* [aiomock](https://github.com/nhumrich/aiomock/) [![GitHub stars](https://img.shields.io/github/stars/nhumrich/aiomock/?style=flat)](https://github.com/nhumrich/aiomock//stargazers) - A python mock library that supports async methods.
* [asynctest](https://github.com/Martiusweb/asynctest/) [![GitHub stars](https://img.shields.io/github/stars/Martiusweb/asynctest/?style=flat)](https://github.com/Martiusweb/asynctest//stargazers) - Enhance the standard unittest package with features for testing. asyncio libraries
* [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) [![GitHub stars](https://img.shields.io/github/stars/pytest-dev/pytest-asyncio?style=flat)](https://github.com/pytest-dev/pytest-asyncio/stargazers) - Pytest support for asyncio.
* [aresponses](https://github.com/CircleUp/aresponses) [![GitHub stars](https://img.shields.io/github/stars/CircleUp/aresponses?style=flat)](https://github.com/CircleUp/aresponses/stargazers) - Asyncio http mocking. Similar to the [responses](https://github.com/getsentry/responses) [![GitHub stars](https://img.shields.io/github/stars/getsentry/responses?style=flat)](https://github.com/getsentry/responses/stargazers) library used for [requests](https://github.com/requests/requests) [![GitHub stars](https://img.shields.io/github/stars/requests/requests?style=flat)](https://github.com/requests/requests/stargazers).
* [aioresponses](https://github.com/pnuckowski/aioresponses) [![GitHub stars](https://img.shields.io/github/stars/pnuckowski/aioresponses?style=flat)](https://github.com/pnuckowski/aioresponses/stargazers) - Helper for mock/fake web requests in Python aiohttp package.

## Alternative Loops

*Alternative asyncio loop implementations.*

* [uvloop](https://github.com/MagicStack/uvloop) [![GitHub stars](https://img.shields.io/github/stars/MagicStack/uvloop?style=flat)](https://github.com/MagicStack/uvloop/stargazers) - Ultra fast implementation of asyncio event loop on top of libuv.

## Misc

*Other awesome asyncio libraries.*

* [aiochan](https://github.com/zh217/aiochan) [![GitHub stars](https://img.shields.io/github/stars/zh217/aiochan?style=flat)](https://github.com/zh217/aiochan/stargazers) - CSP-style concurrency with channels, select and multiprocessing on top of asyncio.
* [aiocache](https://github.com/argaen/aiocache) [![GitHub stars](https://img.shields.io/github/stars/argaen/aiocache?style=flat)](https://github.com/argaen/aiocache/stargazers) - Cache manager for different backends.
* [aiofiles](https://github.com/Tinche/aiofiles/) [![GitHub stars](https://img.shields.io/github/stars/Tinche/aiofiles/?style=flat)](https://github.com/Tinche/aiofiles//stargazers) - File support for asyncio.
* [aiopath](https://github.com/alexdelorenzo/aiopath) [![GitHub stars](https://img.shields.io/github/stars/alexdelorenzo/aiopath?style=flat)](https://github.com/alexdelorenzo/aiopath/stargazers) - Asynchronous `pathlib` for asyncio.
* [aiodebug](https://github.com/qntln/aiodebug) [![GitHub stars](https://img.shields.io/github/stars/qntln/aiodebug?style=flat)](https://github.com/qntln/aiodebug/stargazers) - A tiny library for monitoring and testing asyncio programs.
* [aiorun](https://github.com/cjrh/aiorun) [![GitHub stars](https://img.shields.io/github/stars/cjrh/aiorun?style=flat)](https://github.com/cjrh/aiorun/stargazers) - A `run()` function that handles all the usual boilerplate for startup and graceful shutdown.
* [aiosc](https://github.com/artfwo/aiosc) [![GitHub stars](https://img.shields.io/github/stars/artfwo/aiosc?style=flat)](https://github.com/artfwo/aiosc/stargazers) -  Lightweight Open Sound Control implementation.
* [aioserial](https://github.com/changyuheng/aioserial) [![GitHub stars](https://img.shields.io/github/stars/changyuheng/aioserial?style=flat)](https://github.com/changyuheng/aioserial/stargazers) - A drop-in replacement of [pySerial](https://github.com/pyserial/pyserial) [![GitHub stars](https://img.shields.io/github/stars/pyserial/pyserial?style=flat)](https://github.com/pyserial/pyserial/stargazers).
* [aiozipkin](https://github.com/aio-libs/aiozipkin) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiozipkin?style=flat)](https://github.com/aio-libs/aiozipkin/stargazers) - Distributed tracing instrumentation for asyncio with zipkin
* [asgiref](https://github.com/django/asgiref) [![GitHub stars](https://img.shields.io/github/stars/django/asgiref?style=flat)](https://github.com/django/asgiref/stargazers) - Backend utils for ASGI to WSGI integration, includes sync_to_async and async_to_sync function wrappers.
* [async_property](https://github.com/ryananguiano/async_property) [![GitHub stars](https://img.shields.io/github/stars/ryananguiano/async_property?style=flat)](https://github.com/ryananguiano/async_property/stargazers) - Python decorator for async properties.
* [ruia](https://github.com/howie6879/ruia) [![GitHub stars](https://img.shields.io/github/stars/howie6879/ruia?style=flat)](https://github.com/howie6879/ruia/stargazers) - An async web scraping micro-framework based on asyncio.
* [kubernetes_asyncio](https://github.com/tomplus/kubernetes_asyncio) [![GitHub stars](https://img.shields.io/github/stars/tomplus/kubernetes_asyncio?style=flat)](https://github.com/tomplus/kubernetes_asyncio/stargazers) - Asynchronous client library for Kubernetes.
* [aiomisc](https://github.com/aiokitchen/aiomisc) [![GitHub stars](https://img.shields.io/github/stars/aiokitchen/aiomisc?style=flat)](https://github.com/aiokitchen/aiomisc/stargazers) - Miscellaneous utils for `asyncio`.
* [taskiq](https://taskiq-python.github.io/) - Asynchronous distributed task manager (like celery, but async). 

## Writings

*Documentation, blog posts, and other awesome writing about asyncio.*

* [Official asyncio documentation](https://docs.python.org/3/library/asyncio.html) - Asynchronous I/O, event loop, coroutines and tasks.
* [Short well-written intro to asyncio](https://masnun.com/python-generators-coroutines-native-coroutines-and-async-await/) - Generators, Coroutines, Native Coroutines and async/await.
* [AsyncIO for the Working Python Developer](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e) - A gentle introduction to asynchronous programming from basic examples working up to URL fetching.
* [Test limits of Python aiohttp](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html) - Making 1 million requests with python-aiohttp.
* [ASGI (Asynchronous Server Gateway Interface)](https://asgi.readthedocs.io/en/latest/) - A spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.
* [First Principles Introduction to Asyncio](https://hackernoon.com/a-simple-introduction-to-pythons-asyncio-595d9c9ecf8c) - A no-buzzword first principles introduction to the internal workings of asyncio.
* [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/) - This tutorial looks at how to develop and test an asynchronous API with FastAPI using Test-Driven Development (TDD).
* [Python Concurrency with asyncio](https://www.manning.com/books/python-concurrency-with-asyncio) - Learn how to speed up slow Python code with concurrent programming and the cutting-edge asyncio library.

## Talks

*Recordings of awesome talks about asyncio.*

* [Topics of Interest (Python Asyncio)](https://youtu.be/ZzfHjytDceU) | [screencast](https://youtu.be/lYe8W04ERnY) | [slides](https://speakerdeck.com/dabeaz/topics-of-interest-async) - PyCon Brasil 2015 keynote (David Beazley).
* [Python Asynchronous I/O Walkthrough](https://www.youtube.com/playlist?list=PLpEcQSRWP2IjVRlTUptdD05kG-UkJynQT) - 8-part code walkthrough (Philip Guo).
* [Async/await in Python 3.5 and why it is awesome](https://www.youtube.com/watch?v=m28fiN9y_r8&t=132s) - EuroPython 2016 (Yury Selivanov).
* [Fear and Awaiting in Async: A Savage Journey to the Heart of the Coroutine Dream](https://www.youtube.com/watch?v=E-1Y4kSsAFc) | [screencast](https://www.youtube.com/watch?v=Bm96RqNGbGo) - PyOhio 2016 keynote (David Beazley).
* [Asynchronous Python for the Complete Beginner](https://www.youtube.com/watch?v=iG6fr81xHKA) | [slides](https://speakerdeck.com/pycon2017/miguel-grinberg-asynchronous-python-for-the-complete-beginner) - PyCon 2017 (Miguel Grinberg).
* [Demystifying Python's Async and Await Keywords](https://www.youtube.com/watch?v=F19R_M4Nay4) - JetBrains TV 2020 (Michael Kennedy)

## Alternatives to asyncio

*Alternative approaches to async programming in Python, some of which attempt to support some compatibility with `asyncio`, others are not compatible at all.*

* [curio](https://github.com/dabeaz/curio) [![GitHub stars](https://img.shields.io/github/stars/dabeaz/curio?style=flat)](https://github.com/dabeaz/curio/stargazers) - The coroutine concurrency library.
  * [Curio-Asyncio Bridge](https://github.com/dabeaz/curio/issues/190) [![GitHub stars](https://img.shields.io/github/stars/dabeaz/curio/issues/190?style=flat)](https://github.com/dabeaz/curio/issues/190/stargazers) - basic curio -> asyncio coroutine bridge.
* [trio](https://github.com/python-trio/trio) [![GitHub stars](https://img.shields.io/github/stars/python-trio/trio?style=flat)](https://github.com/python-trio/trio/stargazers) - Pythonic async I/O for humans and snake people.
  * [trio-asyncio](https://github.com/python-trio/trio-asyncio) [![GitHub stars](https://img.shields.io/github/stars/python-trio/trio-asyncio?style=flat)](https://github.com/python-trio/trio-asyncio/stargazers) - re-implementation of the asyncio mainloop on top of Trio.
* [AnyIO](https://github.com/agronholm/anyio) [![GitHub stars](https://img.shields.io/github/stars/agronholm/anyio?style=flat)](https://github.com/agronholm/anyio/stargazers) - High level asynchronous concurrency and networking framework that works on top of either trio or asyncio.
