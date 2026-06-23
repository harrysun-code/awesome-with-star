# FastAPI

[![GitHub stars](https://img.shields.io/github/stars/mjhea0/awesome-fastapi?style=flat)](https://github.com/mjhea0/awesome-fastapi/stargazers)

<!--lint disable double-link-->

# Awesome FastAPI | [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome things related to FastAPI.

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance, batteries-included Python web framework that's perfect for building RESTful APIs.

## Contents

- [Third-Party Extensions](#third-party-extensions)
  - [Admin](#admin)
  - [Auth](#auth)
  - [CyberSecurity](#cybersecurity)
  - [Databases](#databases)
  - [Dependency Injection](#dependency-injection)
  - [Developer Tools](#developer-tools)
  - [Email](#email)
  - [Utils](#utils)
- [Resources](#resources)
  - [Official Resources](#official-resources)
  - [External Resources](#external-resources)
  - [Podcasts](#podcasts)
  - [Articles](#articles)
  - [Tutorials](#tutorials)
  - [Talks](#talks)
  - [Videos](#videos)
  - [Courses](#courses)
  - [Best Practices](#best-practices)
- [Hosting](#hosting)
  - [PaaS](#paas)
  - [IaaS](#iaas)
  - [Serverless](#serverless)
- [Projects](#projects)
  - [Boilerplate](#boilerplate)
  - [Docker Images](#docker-images)
  - [Open Source Projects](#open-source-projects)
- [Sponsors](#sponsors)

## Third-Party Extensions

### Admin

- [FastAPI Admin](https://github.com/fastapi-admin/fastapi-admin) [![GitHub stars](https://img.shields.io/github/stars/fastapi-admin/fastapi-admin?style=flat)](https://github.com/fastapi-admin/fastapi-admin/stargazers) - Functional admin panel that provides a user interface for performing CRUD operations on your data. Currently only works with the Tortoise ORM.
- [FastAPI Amis Admin](https://github.com/amisadmin/fastapi-amis-admin) [![GitHub stars](https://img.shields.io/github/stars/amisadmin/fastapi-amis-admin?style=flat)](https://github.com/amisadmin/fastapi-amis-admin/stargazers) - A high-performance, efficient and easily extensible FastAPI admin framework.
- [Piccolo Admin](https://github.com/piccolo-orm/piccolo_admin) [![GitHub stars](https://img.shields.io/github/stars/piccolo-orm/piccolo_admin?style=flat)](https://github.com/piccolo-orm/piccolo_admin/stargazers) - A powerful and modern admin GUI, using the Piccolo ORM.
- [SQLAlchemy Admin](https://github.com/aminalaee/sqladmin) [![GitHub stars](https://img.shields.io/github/stars/aminalaee/sqladmin?style=flat)](https://github.com/aminalaee/sqladmin/stargazers) - Admin Panel for FastAPI/Starlette that works with SQLAlchemy models.
- [Starlette Admin](https://github.com/jowilf/starlette-admin) [![GitHub stars](https://img.shields.io/github/stars/jowilf/starlette-admin?style=flat)](https://github.com/jowilf/starlette-admin/stargazers) - Admin framework for FastAPI/Starlette, supporting SQLAlchemy, SQLModel, MongoDB, and ODMantic.


### Auth

- [AuthX](https://github.com/yezz123/AuthX) [![GitHub stars](https://img.shields.io/github/stars/yezz123/AuthX?style=flat)](https://github.com/yezz123/AuthX/stargazers) - Customizable Authentications and Oauth2 management for FastAPI.
- [FastAPI Auth](https://github.com/dmontagu/fastapi-auth) [![GitHub stars](https://img.shields.io/github/stars/dmontagu/fastapi-auth?style=flat)](https://github.com/dmontagu/fastapi-auth/stargazers) - Pluggable auth that supports the OAuth2 Password Flow with JWT access and refresh tokens.
- [FastAPI Azure Auth](https://github.com/Intility/fastapi-azure-auth) [![GitHub stars](https://img.shields.io/github/stars/Intility/fastapi-azure-auth?style=flat)](https://github.com/Intility/fastapi-azure-auth/stargazers) - Azure AD authentication for your APIs with single and multi tenant support.
- [FastAPI Casbin Auth](https://github.com/officialpycasbin/fastapi-casbin-auth) [![GitHub stars](https://img.shields.io/github/stars/officialpycasbin/fastapi-casbin-auth?style=flat)](https://github.com/officialpycasbin/fastapi-casbin-auth/stargazers) - Authorization which supports various access control models like RBAC, ReBAC and ABAC through Casbin.
- [FastAPI Cloud Auth](https://github.com/tokusumi/fastapi-cloudauth) [![GitHub stars](https://img.shields.io/github/stars/tokusumi/fastapi-cloudauth?style=flat)](https://github.com/tokusumi/fastapi-cloudauth/stargazers) - Simple integration between FastAPI and cloud authentication services (AWS Cognito, Auth0, Firebase Authentication).
- [FastAPI Login](https://github.com/maxrdu/fastapi_login) [![GitHub stars](https://img.shields.io/github/stars/maxrdu/fastapi_login?style=flat)](https://github.com/maxrdu/fastapi_login/stargazers) - Account management and authentication (based on [Flask-Login](https://github.com/maxcountryman/flask-login) [![GitHub stars](https://img.shields.io/github/stars/maxcountryman/flask-login?style=flat)](https://github.com/maxcountryman/flask-login/stargazers)).
- [FastAPI JWT Auth](https://github.com/IndominusByte/fastapi-jwt-auth) [![GitHub stars](https://img.shields.io/github/stars/IndominusByte/fastapi-jwt-auth?style=flat)](https://github.com/IndominusByte/fastapi-jwt-auth/stargazers) - JWT auth (based on [Flask-JWT-Extended](https://github.com/vimalloc/flask-jwt-extended) [![GitHub stars](https://img.shields.io/github/stars/vimalloc/flask-jwt-extended?style=flat)](https://github.com/vimalloc/flask-jwt-extended/stargazers)).
- [FastAPI Permissions](https://github.com/holgi/fastapi-permissions) [![GitHub stars](https://img.shields.io/github/stars/holgi/fastapi-permissions?style=flat)](https://github.com/holgi/fastapi-permissions/stargazers) - Row-level permissions.
- [FastAPI Security](https://github.com/jacobsvante/fastapi-security) [![GitHub stars](https://img.shields.io/github/stars/jacobsvante/fastapi-security?style=flat)](https://github.com/jacobsvante/fastapi-security/stargazers) - Implements authentication and authorization as dependencies in FastAPI.
- [FastAPI Simple Security](https://github.com/mrtolkien/fastapi_simple_security) [![GitHub stars](https://img.shields.io/github/stars/mrtolkien/fastapi_simple_security?style=flat)](https://github.com/mrtolkien/fastapi_simple_security/stargazers) - Out-of-the-box API key security manageable through path operations.
- [FastAPI Users](https://github.com/fastapi-users/fastapi-users) [![GitHub stars](https://img.shields.io/github/stars/fastapi-users/fastapi-users?style=flat)](https://github.com/fastapi-users/fastapi-users/stargazers) - Account management, authentication, authorization.

### CyberSecurity

- [FastAPI Guard](https://github.com/rennf93/fastapi-guard) [![GitHub stars](https://img.shields.io/github/stars/rennf93/fastapi-guard?style=flat)](https://github.com/rennf93/fastapi-guard/stargazers) - Rate Limiting, Automatically Ban IPs, Penetration Attack Detection, Whitelist/blacklist (countries, IPs, Cloud Providers), User Agent Filtering, Geolocation, Redis integration for persistence, and more.

### Databases

#### ORMs

- [Edgy ORM](https://github.com/dymmond/edgy) [![GitHub stars](https://img.shields.io/github/stars/dymmond/edgy?style=flat)](https://github.com/dymmond/edgy/stargazers) - Complex databases made simple.
- [FastAPI SQLAlchemy](https://github.com/mfreeborn/fastapi-sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/mfreeborn/fastapi-sqlalchemy?style=flat)](https://github.com/mfreeborn/fastapi-sqlalchemy/stargazers) - Simple integration between FastAPI and [SQLAlchemy](https://www.sqlalchemy.org/).
- [Fastapi-SQLA](https://github.com/dialoguemd/fastapi-sqla) [![GitHub stars](https://img.shields.io/github/stars/dialoguemd/fastapi-sqla?style=flat)](https://github.com/dialoguemd/fastapi-sqla/stargazers) - SQLAlchemy extension for FastAPI with support for pagination, asyncio, and pytest.
- [FastAPIwee](https://github.com/Ignisor/FastAPIwee) [![GitHub stars](https://img.shields.io/github/stars/Ignisor/FastAPIwee?style=flat)](https://github.com/Ignisor/FastAPIwee/stargazers) - A simple way to create REST API based on [PeeWee](https://github.com/coleifer/peewee) [![GitHub stars](https://img.shields.io/github/stars/coleifer/peewee?style=flat)](https://github.com/coleifer/peewee/stargazers) models.
- [FastSQLA](https://github.com/hadrien/FastSQLA) [![GitHub stars](https://img.shields.io/github/stars/hadrien/FastSQLA?style=flat)](https://github.com/hadrien/FastSQLA/stargazers) - Async SQLAlchemy 2.0+ extension for FastAPI with SQLModel support, built-in pagination & more.
- [GINO](https://github.com/python-gino/gino) [![GitHub stars](https://img.shields.io/github/stars/python-gino/gino?style=flat)](https://github.com/python-gino/gino/stargazers) - A lightweight asynchronous ORM built on top of SQLAlchemy core for Python asyncio.
  - [FastAPI Example](https://github.com/leosussan/fastapi-gino-arq-uvicorn) [![GitHub stars](https://img.shields.io/github/stars/leosussan/fastapi-gino-arq-uvicorn?style=flat)](https://github.com/leosussan/fastapi-gino-arq-uvicorn/stargazers)
- [ORM](https://github.com/encode/orm) [![GitHub stars](https://img.shields.io/github/stars/encode/orm?style=flat)](https://github.com/encode/orm/stargazers) - An async ORM.
- [ormar](https://collerek.github.io/ormar/) - Ormar is an async ORM that uses Pydantic validation and can be used directly in FastAPI requests and responses so you are left with only one set of models to maintain. Alembic migrations included.
  - [FastAPI Example](https://collerek.github.io/ormar/latest/fastapi/) - Using FastAPI with ormar.
- [Piccolo](https://github.com/piccolo-orm/piccolo) [![GitHub stars](https://img.shields.io/github/stars/piccolo-orm/piccolo?style=flat)](https://github.com/piccolo-orm/piccolo/stargazers) - An async ORM and query builder, supporting Postgres and SQLite, with batteries (migrations, security, etc).
  - [FastAPI Examples](https://github.com/piccolo-orm/piccolo_examples) [![GitHub stars](https://img.shields.io/github/stars/piccolo-orm/piccolo_examples?style=flat)](https://github.com/piccolo-orm/piccolo_examples/stargazers) - Using FastAPI with Piccolo.
- [Tortoise ORM](https://tortoise.github.io) - An easy-to-use asyncio ORM (Object Relational Mapper) inspired by Django.
  - [FastAPI Example](https://tortoise.github.io/examples/fastapi.html) - An example of the Tortoise-ORM FastAPI integration.
  - [Tutorial: Setting up Tortoise ORM with FastAPI](https://web.archive.org/web/20200523174158/https://robwagner.dev/tortoise-fastapi-setup/)
  - [Aerich](https://github.com/tortoise/aerich) [![GitHub stars](https://img.shields.io/github/stars/tortoise/aerich?style=flat)](https://github.com/tortoise/aerich/stargazers) - Tortoise ORM migrations tools.
- [Saffier ORM](https://github.com/tarsil/saffier) [![GitHub stars](https://img.shields.io/github/stars/tarsil/saffier?style=flat)](https://github.com/tarsil/saffier/stargazers) - The only Python ORM you will ever need.
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQLModel (which is powered by Pydantic and SQLAlchemy) is a library for interacting with SQL databases from Python code, with Python objects.

#### Query Builders

- [asyncpgsa](https://github.com/CanopyTax/asyncpgsa) [![GitHub stars](https://img.shields.io/github/stars/CanopyTax/asyncpgsa?style=flat)](https://github.com/CanopyTax/asyncpgsa/stargazers) - A wrapper around [asyncpg](https://github.com/MagicStack/asyncpg) [![GitHub stars](https://img.shields.io/github/stars/MagicStack/asyncpg?style=flat)](https://github.com/MagicStack/asyncpg/stargazers) for use with [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/).
- [Databases](https://github.com/encode/databases) [![GitHub stars](https://img.shields.io/github/stars/encode/databases?style=flat)](https://github.com/encode/databases/stargazers) - Async SQL query builder that works on top of the [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/) expression language.
- [PyPika](https://github.com/kayak/pypika) [![GitHub stars](https://img.shields.io/github/stars/kayak/pypika?style=flat)](https://github.com/kayak/pypika/stargazers) - A SQL query builder that exposes the full richness of the SQL language.

#### ODMs

- [Beanie](https://github.com/BeanieODM/beanie) [![GitHub stars](https://img.shields.io/github/stars/BeanieODM/beanie?style=flat)](https://github.com/BeanieODM/beanie/stargazers) - Asynchronous Python ODM for MongoDB, based on [Motor](https://motor.readthedocs.io/en/stable/) and [Pydantic](https://docs.pydantic.dev/latest/), which supports data and schema migrations out of the box.
- [MongoEngine](https://github.com/MongoEngine/mongoengine) [![GitHub stars](https://img.shields.io/github/stars/MongoEngine/mongoengine?style=flat)](https://github.com/MongoEngine/mongoengine/stargazers) - A Document-Object Mapper (think ORM, but for document databases) for working with MongoDB from Python.
- [Motor](https://motor.readthedocs.io/) - Asynchronous Python driver for MongoDB.
- [ODMantic](https://art049.github.io/odmantic/) - AsyncIO MongoDB ODM integrated with [Pydantic](https://docs.pydantic.dev/latest/).
- [PynamoDB](https://github.com/pynamodb/PynamoDB) [![GitHub stars](https://img.shields.io/github/stars/pynamodb/PynamoDB?style=flat)](https://github.com/pynamodb/PynamoDB/stargazers) - A pythonic interface to Amazon's DynamoDB.

#### Other Tools

- [Pydantic-SQLAlchemy](https://github.com/tiangolo/pydantic-sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/tiangolo/pydantic-sqlalchemy?style=flat)](https://github.com/tiangolo/pydantic-sqlalchemy/stargazers) - Convert SQLAlchemy models to [Pydantic](https://docs.pydantic.dev/latest/) models.
- [FastAPI-CamelCase](https://nf1s.github.io/fastapi-camelcase/) - CamelCase JSON support for FastAPI utilizing [Pydantic](https://docs.pydantic.dev/latest/).
  - [CamelCase Models with FastAPI and Pydantic](https://medium.com/analytics-vidhya/camel-case-models-with-fast-api-and-pydantic-5a8acb6c0eee) - Accompanying blog post from the author of the extension.
 
### Dependency Injection
- [Wireup](https://github.com/maldoinc/wireup) [![GitHub stars](https://img.shields.io/github/stars/maldoinc/wireup?style=flat)](https://github.com/maldoinc/wireup/stargazers) - Inject dependencies with zero runtime overhead in FastAPI; Share dependencies across web, cli or other interfaces.

### Developer Tools

- [FastAPI Code Generator](https://github.com/koxudaxi/fastapi-code-generator) [![GitHub stars](https://img.shields.io/github/stars/koxudaxi/fastapi-code-generator?style=flat)](https://github.com/koxudaxi/fastapi-code-generator/stargazers) - Create a FastAPI app from an OpenAPI file, enabling schema-driven development.
- [FastAPI Client Generator](https://github.com/dmontagu/fastapi_client) [![GitHub stars](https://img.shields.io/github/stars/dmontagu/fastapi_client?style=flat)](https://github.com/dmontagu/fastapi_client/stargazers) - Generate a mypy- and IDE-friendly API client from an OpenAPI spec.
- [FastAPI Cruddy Framework](https://github.com/mdconaway/fastapi-cruddy-framework) [![GitHub stars](https://img.shields.io/github/stars/mdconaway/fastapi-cruddy-framework?style=flat)](https://github.com/mdconaway/fastapi-cruddy-framework/stargazers) - A companion library to FastAPI designed to bring the development productivity of Ruby on Rails, Ember.js or Sails.js to the FastAPI ecosystem.
- [FastAPI MVC](https://github.com/fastapi-mvc/fastapi-mvc) [![GitHub stars](https://img.shields.io/github/stars/fastapi-mvc/fastapi-mvc?style=flat)](https://github.com/fastapi-mvc/fastapi-mvc/stargazers) - Developer productivity tool for making high-quality FastAPI production-ready APIs.
- [FastAPI Profiler](https://github.com/sunhailin-Leo/fastapi_profiler) [![GitHub stars](https://img.shields.io/github/stars/sunhailin-Leo/fastapi_profiler?style=flat)](https://github.com/sunhailin-Leo/fastapi_profiler/stargazers) - A FastAPI Middleware of joerick/pyinstrument to check your service performance.
- [FastAPI Versioning](https://github.com/DeanWay/fastapi-versioning) [![GitHub stars](https://img.shields.io/github/stars/DeanWay/fastapi-versioning?style=flat)](https://github.com/DeanWay/fastapi-versioning/stargazers) - API versioning.
- [Jupyter Notebook REST API](https://github.com/Invictify/Jupter-Notebook-REST-API) [![GitHub stars](https://img.shields.io/github/stars/Invictify/Jupter-Notebook-REST-API?style=flat)](https://github.com/Invictify/Jupter-Notebook-REST-API/stargazers) - Run your Jupyter notebooks as RESTful API endpoints.
- [Manage FastAPI](https://github.com/ycd/manage-fastapi) [![GitHub stars](https://img.shields.io/github/stars/ycd/manage-fastapi?style=flat)](https://github.com/ycd/manage-fastapi/stargazers) - CLI tool for generating and managing FastAPI projects.
- [msgpack-asgi](https://github.com/florimondmanca/msgpack-asgi) [![GitHub stars](https://img.shields.io/github/stars/florimondmanca/msgpack-asgi?style=flat)](https://github.com/florimondmanca/msgpack-asgi/stargazers) - Automatic [MessagePack](https://msgpack.org/) content negotiation.
- [python-cqrs](https://github.com/pypatterns/python-cqrs) [![GitHub stars](https://img.shields.io/github/stars/pypatterns/python-cqrs?style=flat)](https://github.com/pypatterns/python-cqrs/stargazers) - Event-Driven Architecture Framework with CQRS, Transaction Outbox, Saga orchestration, seamless FastAPI/FastStream integration.

### Email

- [FastAPI Mail](https://github.com/sabuhish/fastapi-mail) [![GitHub stars](https://img.shields.io/github/stars/sabuhish/fastapi-mail?style=flat)](https://github.com/sabuhish/fastapi-mail/stargazers) - Lightweight mail system for sending emails and attachments (individual and bulk).

### Utils

- [Apitally](https://github.com/apitally/apitally-py) [![GitHub stars](https://img.shields.io/github/stars/apitally/apitally-py?style=flat)](https://github.com/apitally/apitally-py/stargazers) - API analytics, monitoring, and request logging for FastAPI.
- [ASGI Correlation ID](https://github.com/snok/asgi-correlation-id) [![GitHub stars](https://img.shields.io/github/stars/snok/asgi-correlation-id?style=flat)](https://github.com/snok/asgi-correlation-id/stargazers) - Request ID logging middleware.
- [FastAPI Cache](https://github.com/comeuplater/fastapi_cache) [![GitHub stars](https://img.shields.io/github/stars/comeuplater/fastapi_cache?style=flat)](https://github.com/comeuplater/fastapi_cache/stargazers) - A simple lightweight cache system.
- [FastAPI Cache](https://github.com/long2ice/fastapi-cache) [![GitHub stars](https://img.shields.io/github/stars/long2ice/fastapi-cache?style=flat)](https://github.com/long2ice/fastapi-cache/stargazers) - A tool to cache FastAPI response and function results, with support for Redis, Memcached, DynamoDB, and in-memory backends.
- [FastAPI Chameleon](https://github.com/mikeckennedy/fastapi-chameleon) [![GitHub stars](https://img.shields.io/github/stars/mikeckennedy/fastapi-chameleon?style=flat)](https://github.com/mikeckennedy/fastapi-chameleon/stargazers) - Adds integration of the Chameleon template language to FastAPI.
- [FastAPI CloudEvents](https://github.com/sasha-tkachev/fastapi-cloudevents) [![GitHub stars](https://img.shields.io/github/stars/sasha-tkachev/fastapi-cloudevents?style=flat)](https://github.com/sasha-tkachev/fastapi-cloudevents/stargazers) - [CloudEvents](https://cloudevents.io/) integration for FastAPI.
- [FastAPI Contrib](https://github.com/identixone/fastapi_contrib) [![GitHub stars](https://img.shields.io/github/stars/identixone/fastapi_contrib?style=flat)](https://github.com/identixone/fastapi_contrib/stargazers) - Opinionated set of utilities: pagination, auth middleware, permissions, custom exception handlers, MongoDB support, and Opentracing middleware.
- [FastAPI FastCRUD](https://github.com/benavlabs/fastcrud) [![GitHub stars](https://img.shields.io/github/stars/benavlabs/fastcrud?style=flat)](https://github.com/benavlabs/fastcrud/stargazers)) - Robust async CRUD operations and flexible endpoint creation utilities.
- [FastAPI Events](https://github.com/melvinkcx/fastapi-events) [![GitHub stars](https://img.shields.io/github/stars/melvinkcx/fastapi-events?style=flat)](https://github.com/melvinkcx/fastapi-events/stargazers) - Asynchronous event dispatching/handling library for FastAPI and Starlette.
- [FastAPI FeatureFlags](https://github.com/Pytlicek/fastapi-featureflags) [![GitHub stars](https://img.shields.io/github/stars/Pytlicek/fastapi-featureflags?style=flat)](https://github.com/Pytlicek/fastapi-featureflags/stargazers) - Simple implementation of feature flags for FastAPI.
- [FastAPI Injectable](https://github.com/JasperSui/fastapi-injectable) [![GitHub stars](https://img.shields.io/github/stars/JasperSui/fastapi-injectable?style=flat)](https://github.com/JasperSui/fastapi-injectable/stargazers) - Use FastAPI's dependency injection outside route handlers in CLI tools, background tasks, workers, and more.
- [FastAPI Jinja](https://github.com/AGeekInside/fastapi-jinja) [![GitHub stars](https://img.shields.io/github/stars/AGeekInside/fastapi-jinja?style=flat)](https://github.com/AGeekInside/fastapi-jinja/stargazers) - Adds integration of the Jinja template language to FastAPI.
- [FastAPI Lazy](https://github.com/yezz123/fastango) [![GitHub stars](https://img.shields.io/github/stars/yezz123/fastango?style=flat)](https://github.com/yezz123/fastango/stargazers) - Lazy package to start your project using FastAPI.
- [FastAPI Limiter](https://github.com/long2ice/fastapi-limiter) [![GitHub stars](https://img.shields.io/github/stars/long2ice/fastapi-limiter?style=flat)](https://github.com/long2ice/fastapi-limiter/stargazers) - A request rate limiter for FastAPI.
- [FastAPI Listing](https://github.com/danielhasan1/fastapi-listing) [![GitHub stars](https://img.shields.io/github/stars/danielhasan1/fastapi-listing?style=flat)](https://github.com/danielhasan1/fastapi-listing/stargazers) - A library to design/build listing APIs using component-based architecture, inbuilt query paginator, sorter, django-admin like filters & much more.
- [FastAPI MQTT](https://github.com/sabuhish/fastapi-mqtt) [![GitHub stars](https://img.shields.io/github/stars/sabuhish/fastapi-mqtt?style=flat)](https://github.com/sabuhish/fastapi-mqtt/stargazers) - An extension for the MQTT protocol.
- [FastAPI Opentracing](https://github.com/wesdu/fastapi-opentracing) [![GitHub stars](https://img.shields.io/github/stars/wesdu/fastapi-opentracing?style=flat)](https://github.com/wesdu/fastapi-opentracing/stargazers) - Opentracing middleware and database tracing support for FastAPI.
- [FastAPI Pagination](https://github.com/uriyyo/fastapi-pagination) [![GitHub stars](https://img.shields.io/github/stars/uriyyo/fastapi-pagination?style=flat)](https://github.com/uriyyo/fastapi-pagination/stargazers) - Pagination for FastAPI.
- [FastAPI Plugins](https://github.com/madkote/fastapi-plugins) [![GitHub stars](https://img.shields.io/github/stars/madkote/fastapi-plugins?style=flat)](https://github.com/madkote/fastapi-plugins/stargazers) - Redis and Scheduler plugins.
- [FastAPI ServiceUtils](https://github.com/skallfass/fastapi_serviceutils) [![GitHub stars](https://img.shields.io/github/stars/skallfass/fastapi_serviceutils?style=flat)](https://github.com/skallfass/fastapi_serviceutils/stargazers) - Generator for creating API services.
- [FastAPI Shield](https://github.com/jymchng/fastapi-shield) [![GitHub stars](https://img.shields.io/github/stars/jymchng/fastapi-shield?style=flat)](https://github.com/jymchng/fastapi-shield/stargazers) - General FastAPI library for writing any generic endpoint decorators capable of lazy dependencies injection.
- [FastAPI SocketIO](https://github.com/pyropy/fastapi-socketio) [![GitHub stars](https://img.shields.io/github/stars/pyropy/fastapi-socketio?style=flat)](https://github.com/pyropy/fastapi-socketio/stargazers) - Easy integration for FastAPI and SocketIO.
- [FastAPI Utilities](https://github.com/fastapiutils/fastapi-utils) [![GitHub stars](https://img.shields.io/github/stars/fastapiutils/fastapi-utils?style=flat)](https://github.com/fastapiutils/fastapi-utils/stargazers) - Reusable utilities: class-based views, response inferring router, periodic tasks, timing middleware, SQLAlchemy session, OpenAPI spec simplification.
- [FastAPI Websocket Pub/Sub](https://github.com/authorizon/fastapi_websocket_pubsub) [![GitHub stars](https://img.shields.io/github/stars/authorizon/fastapi_websocket_pubsub?style=flat)](https://github.com/authorizon/fastapi_websocket_pubsub/stargazers) - The classic pub/sub pattern made easily accessible and scalable over the web and across your cloud in realtime.
- [FastAPI Websocket RPC](https://github.com/authorizon/fastapi_websocket_rpc) [![GitHub stars](https://img.shields.io/github/stars/authorizon/fastapi_websocket_rpc?style=flat)](https://github.com/authorizon/fastapi_websocket_rpc/stargazers) - RPC (bidirectional JSON RPC) over Websockets made easy, robust, and production ready.
- [OpenTelemetry FastAPI Instrumentation](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-fastapi) [![GitHub stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-fastapi?style=flat)](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-fastapi/stargazers) - Library provides automatic and manual instrumentation of FastAPI web frameworks, instrumenting http requests served by applications utilizing the framework.
- [Prerender Python Starlette](https://github.com/BeeMyDesk/prerender-python-starlette) [![GitHub stars](https://img.shields.io/github/stars/BeeMyDesk/prerender-python-starlette?style=flat)](https://github.com/BeeMyDesk/prerender-python-starlette/stargazers) - Starlette middleware for Prerender.
- [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator) [![GitHub stars](https://img.shields.io/github/stars/trallnag/prometheus-fastapi-instrumentator?style=flat)](https://github.com/trallnag/prometheus-fastapi-instrumentator/stargazers) - A configurable and modular Prometheus Instrumentator for your FastAPI application.
- [SlowApi](https://github.com/laurents/slowapi) [![GitHub stars](https://img.shields.io/github/stars/laurents/slowapi?style=flat)](https://github.com/laurents/slowapi/stargazers) - Rate limiter (based on [Flask-Limiter](https://flask-limiter.readthedocs.io)).
- [Starlette Context](https://github.com/tomwojcik/starlette-context) [![GitHub stars](https://img.shields.io/github/stars/tomwojcik/starlette-context?style=flat)](https://github.com/tomwojcik/starlette-context/stargazers) - Allows you to store and access the request data anywhere in your project, useful for logging.
- [Starlette Exporter](https://github.com/stephenhillier/starlette_exporter) [![GitHub stars](https://img.shields.io/github/stars/stephenhillier/starlette_exporter?style=flat)](https://github.com/stephenhillier/starlette_exporter/stargazers) - One more prometheus integration for FastAPI and Starlette.
- [Starlette OpenTracing](https://github.com/acidjunk/starlette-opentracing) [![GitHub stars](https://img.shields.io/github/stars/acidjunk/starlette-opentracing?style=flat)](https://github.com/acidjunk/starlette-opentracing/stargazers) - Opentracing support for Starlette and FastAPI.
- [Starlette Prometheus](https://github.com/perdy/starlette-prometheus) [![GitHub stars](https://img.shields.io/github/stars/perdy/starlette-prometheus?style=flat)](https://github.com/perdy/starlette-prometheus/stargazers) - Prometheus integration for FastAPI and Starlette.
- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry) [![GitHub stars](https://img.shields.io/github/stars/strawberry-graphql/strawberry?style=flat)](https://github.com/strawberry-graphql/strawberry/stargazers) - Python GraphQL library based on dataclasses.
- [Pydantic Resolve](https://github.com/allmonday/pydantic-resolve) [![GitHub stars](https://img.shields.io/github/stars/allmonday/pydantic-resolve?style=flat)](https://github.com/allmonday/pydantic-resolve/stargazers) -  Turns pydantic class into a powerful composable computing container by introducing resolve and post-process hooks.

## Resources

### Official Resources

- [Documentation](https://fastapi.tiangolo.com/) - Comprehensive documentation.
- [Tutorial](https://fastapi.tiangolo.com/tutorial/) - Official tutorial showing you how to use FastAPI with most of its features, step by step.
- [Source Code](https://github.com/fastapi/fastapi) [![GitHub stars](https://img.shields.io/github/stars/fastapi/fastapi?style=flat)](https://github.com/fastapi/fastapi/stargazers) - Hosted on GitHub.
- [Discord](https://discord.com/invite/VQjSZaeJmf) - Chat with other FastAPI users.

### External Resources

- [TestDriven.io FastAPI](https://testdriven.io/blog/topics/fastapi/) - Multiple FastAPI-specific articles that focus on developing and testing production-ready RESTful APIs, serving up machine learning models, and more.

### Podcasts

- [Build The Next Generation Of Python Web Applications With FastAPI](https://www.pythonpodcast.com/fastapi-web-application-framework-episode-259/) - In this episode of [Podcast Init](https://www.pythonpodcast.com/), the creator of FastAPI, [Sebastián Ramirez](https://tiangolo.com/), shares his motivations for building FastAPI and how it works under the hood.
- [FastAPI on PythonBytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855) - Nice overview of the project.

### Articles

- [FastAPI has Ruined Flask Forever for Me](https://medium.com/data-science/fastapi-has-ruined-flask-forever-for-me-73916127da)
- [Why we switched from Flask to FastAPI for production machine learning](https://medium.com/@calebkaiser/why-we-switched-from-flask-to-fastapi-for-production-machine-learning-765aab9b3679) - In-depth look at why you may want to move from Flask to FastAPI.

### Tutorials

- [Async SQLAlchemy with FastAPI](https://stribny.name/posts/fastapi-asyncalchemy/) - Learn how to use SQLAlchemy asynchronously.
- [Deploy Machine Learning Models with Keras, FastAPI, Redis and Docker](https://medium.com/analytics-vidhya/deploy-machine-learning-models-with-keras-fastapi-redis-and-docker-4940df614ece)
- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/) - Develop and test an asynchronous API with FastAPI, Postgres, Pytest, and Docker using Test-Driven Development.
- [FastAPI for Flask Users](https://amitness.com/posts/fastapi-vs-flask) - Learn FastAPI with a side-by-side code comparison to Flask.
- [Implementing FastAPI Services – Abstraction and Separation of Concerns](https://camillovisini.com/coding/abstracting-fastapi-services) - FastAPI application and service structure for a more maintainable codebase.
- [Introducing FARM Stack - FastAPI, React, and MongoDB](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/integrations/fastapi-integration/) - Getting started with a complete FastAPI web application stack.
- [Multitenancy with FastAPI, SQLAlchemy and PostgreSQL](https://mergeboard.com/blog/6-multitenancy-fastapi-sqlalchemy-postgresql/) - Learn how to make FastAPI applications multi-tenant ready.
- [Porting Flask to FastAPI for ML Model Serving](https://www.pluralsight.com/tech-blog/porting-flask-to-fastapi-for-ml-model-serving/) - Comparison of Flask vs FastAPI.
- [Real-time data streaming using FastAPI and WebSockets](https://stribny.name/posts/real-time-data-streaming-using-fastapi-and-websockets/) - Learn how to stream data from FastAPI directly into a real-time chart.
- [Running FastAPI applications in production](https://stribny.name/posts/fastapi-production/) - Use Gunicorn with systemd for production deployments.
- [Serving Machine Learning Models with FastAPI in Python](https://medium.com/@8B_EC/tutorial-serving-machine-learning-models-with-fastapi-in-python-c1a27319c459) - Use FastAPI to quickly and easily deploy and serve machine learning models in Python as a RESTful API.
- [Streaming video with FastAPI](https://stribny.name/posts/fastapi-video/) - Learn how to serve video streams.
- [Using Hypothesis and Schemathesis to Test FastAPI](https://testdriven.io/blog/fastapi-hypothesis/) - Apply property-based testing to FastAPI.

### Talks

- [PyConBY 2020: Serve ML models easily with FastAPI](https://www.youtube.com/watch?v=z9K5pwb0rt8) - From the talk by Sebastian Ramirez you will learn how to easily build a production-ready web (JSON) API for your ML models with FastAPI, including best practices by default.
- [PyCon UK 2019: FastAPI from the ground up](https://www.youtube.com/watch?v=3DLwPcrE5mA) - This talk shows how to build a simple REST API for a database from the ground up using FastAPI.

### Videos

- [Building a Stock Screener with FastAPI](https://www.youtube.com/watch?v=5GorMC2lPpk) - A you build a web-based stock screener with FastAPI, you'll be introduced to many of FastAPI's features, including Pydantic models, dependency injection, background tasks, and SQLAlchemy integration.
- [Building Web APIs Using FastAPI](https://www.youtube.com/watch?v=Pe66M8mn-wA) - Use FastAPI to build a web application programming interface (RESTful API).
- [FastAPI - A Web Framework for Python](https://www.youtube.com/watch?v=PUhio8CprhI&list=PL5gdMNl42qynpY-o43Jk3evfxEKSts3HS) - See how to do numeric validations with FastAPI.
- [FastAPI vs. Django vs. Flask](https://www.youtube.com/watch?v=9YBAOYQOzWs) - Which framework is best for Python in 2020? Which uses async/await the best? Which is the fastest?
- [Serving Machine Learning Models As API with FastAPI](https://www.youtube.com/watch?v=mkDxuRvKUL8) - Build a machine learning API with FastAPI.

### Courses

- [Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/) - Learn how to build, test, and deploy a text summarization microservice with Python, FastAPI, and Docker.
- [Modern APIs with FastAPI and Python](https://training.talkpython.fm/courses/modern-fastapi-apis) - A course designed to get you creating new APIs running in the cloud with FastAPI quickly.
- [Full Web Apps with FastAPI Course](https://training.talkpython.fm/courses/full-html-web-applications-with-fastapi) - You'll learn to build full web apps with FastAPI, equivalent to what you can do with Flask or Django.
- [The Definitive Guide to Celery and FastAPI](https://testdriven.io/courses/fastapi-celery/) - Learn how to add Celery to a FastAPI application to provide asynchronous task processing.

### Best Practices

- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices) [![GitHub stars](https://img.shields.io/github/stars/zhanymkanov/fastapi-best-practices?style=flat)](https://github.com/zhanymkanov/fastapi-best-practices/stargazers) - Collection of best practices in a GitHub repo.
- [FastAPI-Dishka-FastStream](https://github.com/faststream-community/fastapi-dishka-faststream) [![GitHub stars](https://img.shields.io/github/stars/faststream-community/fastapi-dishka-faststream?style=flat)](https://github.com/faststream-community/fastapi-dishka-faststream/stargazers) - Combines FastAPI, dishka, faststream, sqlalchemy, pydantic.
- [FastAPI Clean Example](https://github.com/ivan-borovets/fastapi-clean-example) [![GitHub stars](https://img.shields.io/github/stars/ivan-borovets/fastapi-clean-example?style=flat)](https://github.com/ivan-borovets/fastapi-clean-example/stargazers) - Clean Architecture backend example built with FastAPI.

## Hosting

### PaaS

(Platforms-as-a-Service)

- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- [Fly](https://fly.io) ([tutorial](https://fly.io/docs/python/frameworks/fastapi/), [Deploy from a Git repo](https://github.com/fly-apps/hello-fastapi) [![GitHub stars](https://img.shields.io/github/stars/fly-apps/hello-fastapi?style=flat)](https://github.com/fly-apps/hello-fastapi/stargazers))
- [Google App Engine](https://cloud.google.com/appengine)
- [Heroku](https://www.heroku.com/) ([Step-by-step tutorial](https://tutlinks.com/create-and-deploy-fastapi-app-to-heroku/), [ML model on Heroku tutorial](https://testdriven.io/blog/fastapi-machine-learning/))
- [Microsoft Azure App Service](https://azure.microsoft.com/en-us/products/app-service/)

### IaaS

(Infrastructure-as-a-Service)

- [AWS EC2](https://aws.amazon.com/ec2/)
- [Google Compute Engine](https://cloud.google.com/compute)
- [Digital Ocean](https://www.digitalocean.com/)
- [Linode](https://www.linode.com/)

### Serverless

Frameworks:

- [Chalice](https://github.com/aws/chalice) [![GitHub stars](https://img.shields.io/github/stars/aws/chalice?style=flat)](https://github.com/aws/chalice/stargazers)
- [Mangum](https://mangum.io/) - Adapter for running ASGI applications with AWS Lambda and API Gateway.
- [Vercel](https://vercel.com/) - (formerly Zeit) ([example](https://github.com/Snailedlt/Markdown-Videos) [![GitHub stars](https://img.shields.io/github/stars/Snailedlt/Markdown-Videos?style=flat)](https://github.com/Snailedlt/Markdown-Videos/stargazers)).

Compute:

- [AWS Lambda](https://aws.amazon.com/lambda/) ([example](https://github.com/iwpnd/fastapi-aws-lambda-example) [![GitHub stars](https://img.shields.io/github/stars/iwpnd/fastapi-aws-lambda-example?style=flat)](https://github.com/iwpnd/fastapi-aws-lambda-example/stargazers))
- [Google Cloud Functions](https://cloud.google.com/functions)
- [Azure Functions](https://azure.microsoft.com/en-us/products/functions/)
- [Google Cloud Run](https://cloud.google.com/run) ([example](https://github.com/anthonycorletti/cloudrun-fastapi) [![GitHub stars](https://img.shields.io/github/stars/anthonycorletti/cloudrun-fastapi?style=flat)](https://github.com/anthonycorletti/cloudrun-fastapi/stargazers))

## Projects

### Boilerplate

- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/fastapi/full-stack-fastapi-template) [![GitHub stars](https://img.shields.io/github/stars/fastapi/full-stack-fastapi-template?style=flat)](https://github.com/fastapi/full-stack-fastapi-template/stargazers) - Full Stack FastAPI Template
, which includes FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS, and more (developed by the creator of FastAPI, [Sebastián Ramírez](https://github.com/tiangolo) [![GitHub stars](https://img.shields.io/github/stars/tiangolo?style=flat)](https://github.com/tiangolo/stargazers)).
- [FastAPI and Tortoise ORM](https://github.com/prostomarkeloff/fastapi-tortoise) [![GitHub stars](https://img.shields.io/github/stars/prostomarkeloff/fastapi-tortoise?style=flat)](https://github.com/prostomarkeloff/fastapi-tortoise/stargazers) - Powerful but simple template for web APIs w/ FastAPI (as web framework) and Tortoise-ORM (for working via database without headache).
- [FastAPI Model Server Skeleton](https://github.com/eightBEC/fastapi-ml-skeleton) [![GitHub stars](https://img.shields.io/github/stars/eightBEC/fastapi-ml-skeleton?style=flat)](https://github.com/eightBEC/fastapi-ml-skeleton/stargazers) - Skeleton app to serve machine learning models production-ready.
- [cookiecutter-spacy-fastapi](https://github.com/microsoft/cookiecutter-spacy-fastapi) [![GitHub stars](https://img.shields.io/github/stars/microsoft/cookiecutter-spacy-fastapi?style=flat)](https://github.com/microsoft/cookiecutter-spacy-fastapi/stargazers) - Quick deployments of spaCy models with FastAPI.
- [cookiecutter-fastapi](https://github.com/arthurhenrique/cookiecutter-fastapi) [![GitHub stars](https://img.shields.io/github/stars/arthurhenrique/cookiecutter-fastapi?style=flat)](https://github.com/arthurhenrique/cookiecutter-fastapi/stargazers) - Cookiecutter template for FastAPI projects using: Machine Learning, Poetry, Azure Pipelines and pytest.
- [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) [![GitHub stars](https://img.shields.io/github/stars/openapi-generators/openapi-python-client?style=flat)](https://github.com/openapi-generators/openapi-python-client/stargazers) - Generate modern FastAPI Python clients (via FastAPI) from OpenAPI.
- [Pywork](https://github.com/vutran1710/YeomanPywork) [![GitHub stars](https://img.shields.io/github/stars/vutran1710/YeomanPywork?style=flat)](https://github.com/vutran1710/YeomanPywork/stargazers) - [Yeoman](https://yeoman.io/) generator to scaffold a FastAPI app.
- [fastapi-gino-arq-uvicorn](https://github.com/leosussan/fastapi-gino-arq-uvicorn) [![GitHub stars](https://img.shields.io/github/stars/leosussan/fastapi-gino-arq-uvicorn?style=flat)](https://github.com/leosussan/fastapi-gino-arq-uvicorn/stargazers) - Template for a high-performance async REST API, in Python. FastAPI + GINO + Arq + Uvicorn (w/ Redis and PostgreSQL).
- [FastAPI and React Template](https://github.com/Buuntu/fastapi-react) [![GitHub stars](https://img.shields.io/github/stars/Buuntu/fastapi-react?style=flat)](https://github.com/Buuntu/fastapi-react/stargazers) - Full stack cookiecutter boilerplate using FastAPI, TypeScript, Docker, PostgreSQL, and React.
- [FastAPI Nano](https://github.com/rednafi/fastapi-nano) [![GitHub stars](https://img.shields.io/github/stars/rednafi/fastapi-nano?style=flat)](https://github.com/rednafi/fastapi-nano/stargazers) - Simple FastAPI template with factory pattern architecture.
- [FastAPI template](https://github.com/s3rius/FastAPI-template) [![GitHub stars](https://img.shields.io/github/stars/s3rius/FastAPI-template?style=flat)](https://github.com/s3rius/FastAPI-template/stargazers) - Flexible, lightweight FastAPI project generator. It includes support for SQLAlchemy, multiple databases, CI/CD, Docker, and Kubernetes.
- [FastAPI on Google Cloud Run](https://github.com/anthonycorletti/cloudrun-fastapi) [![GitHub stars](https://img.shields.io/github/stars/anthonycorletti/cloudrun-fastapi?style=flat)](https://github.com/anthonycorletti/cloudrun-fastapi/stargazers) - Boilerplate for API building with FastAPI, SQLModel, and Google Cloud Run.
- [FastAPI with Firestore](https://github.com/anthonycorletti/firestore-fastapi) [![GitHub stars](https://img.shields.io/github/stars/anthonycorletti/firestore-fastapi?style=flat)](https://github.com/anthonycorletti/firestore-fastapi/stargazers) - Boilerplate for API building with FastAPI and Google Cloud Firestore.
- [fastapi-alembic-sqlmodel-async](https://github.com/vargasjona/fastapi-alembic-sqlmodel-async) [![GitHub stars](https://img.shields.io/github/stars/vargasjona/fastapi-alembic-sqlmodel-async?style=flat)](https://github.com/vargasjona/fastapi-alembic-sqlmodel-async/stargazers) - This is a project template which uses FastAPI, Alembic, and async SQLModel as ORM.
- [fastapi-starter-project](https://github.com/mirzadelic/fastapi-starter-project) [![GitHub stars](https://img.shields.io/github/stars/mirzadelic/fastapi-starter-project?style=flat)](https://github.com/mirzadelic/fastapi-starter-project/stargazers) - A project template which uses FastAPI, SQLModel, Alembic, Pytest, Docker, GitHub Actions CI.
- [Full Stack FastAPI and MongoDB - Base Project Generator](https://github.com/mongodb-labs/full-stack-fastapi-mongodb) [![GitHub stars](https://img.shields.io/github/stars/mongodb-labs/full-stack-fastapi-mongodb?style=flat)](https://github.com/mongodb-labs/full-stack-fastapi-mongodb/stargazers) - Full stack, modern web application generator, which includes FastAPI, MongoDB, Docker, Celery, React frontend, automatic HTTPS and more.
- [Uvicorn Poetry FastAPI Project Template](https://github.com/max-pfeiffer/uvicorn-poetry-fastapi-project-template) [![GitHub stars](https://img.shields.io/github/stars/max-pfeiffer/uvicorn-poetry-fastapi-project-template?style=flat)](https://github.com/max-pfeiffer/uvicorn-poetry-fastapi-project-template/stargazers) - Cookiecutter project template for starting a FastAPI application. Runs in a Docker container with Uvicorn ASGI server on Kubernetes. Supports AMD64 and ARM64 CPU architectures.

### Docker Images

- [inboard](https://github.com/br3ndonland/inboard) [![GitHub stars](https://img.shields.io/github/stars/br3ndonland/inboard?style=flat)](https://github.com/br3ndonland/inboard/stargazers) - Docker images to power your FastAPI apps and help you ship faster.
- [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) [![GitHub stars](https://img.shields.io/github/stars/tiangolo/uvicorn-gunicorn-fastapi-docker?style=flat)](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/stargazers) - Docker image with Uvicorn managed by Gunicorn for high-performance FastAPI web applications in Python 3.7 and 3.6 with performance auto-tuning.
- [uvicorn-gunicorn-poetry](https://github.com/max-pfeiffer/uvicorn-gunicorn-poetry) [![GitHub stars](https://img.shields.io/github/stars/max-pfeiffer/uvicorn-gunicorn-poetry?style=flat)](https://github.com/max-pfeiffer/uvicorn-gunicorn-poetry/stargazers) - Docker image with Gunicorn using Uvicorn workers for running Python web applications. Uses Poetry for managing dependencies and setting up a virtual environment. Supports AMD64 and ARM64 CPU architectures.
- [uvicorn-poetry](https://github.com/max-pfeiffer/uvicorn-poetry) [![GitHub stars](https://img.shields.io/github/stars/max-pfeiffer/uvicorn-poetry?style=flat)](https://github.com/max-pfeiffer/uvicorn-poetry/stargazers) - Docker image with Uvicorn ASGI server for running Python web applications on Kubernetes. Uses Poetry for managing dependencies and setting up a virtual environment. Supports AMD64 and ARM64 CPU architectures.

### Open Source Projects

- [Astrobase](https://github.com/anthonycorletti/astrobase) [![GitHub stars](https://img.shields.io/github/stars/anthonycorletti/astrobase?style=flat)](https://github.com/anthonycorletti/astrobase/stargazers) - Simple, fast, and secure deployments anywhere.
- [Awesome FastAPI Projects](https://github.com/Kludex/awesome-fastapi-projects) [![GitHub stars](https://img.shields.io/github/stars/Kludex/awesome-fastapi-projects?style=flat)](https://github.com/Kludex/awesome-fastapi-projects/stargazers) - Organized list of projects that use FastAPI.
- [Bitcart](https://github.com/bitcart/bitcart) [![GitHub stars](https://img.shields.io/github/stars/bitcart/bitcart?style=flat)](https://github.com/bitcart/bitcart/stargazers) - Platform for merchants, users and developers which offers easy setup and use.
- [Bali](https://github.com/bali-framework/bali) [![GitHub stars](https://img.shields.io/github/stars/bali-framework/bali?style=flat)](https://github.com/bali-framework/bali/stargazers) - Simplify Cloud Native Microservices development base on FastAPI and gRPC.
- [Bunnybook](https://github.com/pietrobassi/bunnybook) [![GitHub stars](https://img.shields.io/github/stars/pietrobassi/bunnybook?style=flat)](https://github.com/pietrobassi/bunnybook/stargazers) - A tiny social network built with FastAPI, React+RxJs, Neo4j, PostgreSQL, and Redis.
- [Coronavirus-tg-api](https://github.com/egbakou/coronavirus-tg-api) [![GitHub stars](https://img.shields.io/github/stars/egbakou/coronavirus-tg-api?style=flat)](https://github.com/egbakou/coronavirus-tg-api/stargazers) - API for tracking the global coronavirus (COVID-19, SARS-CoV-2) outbreak.
- [Dispatch](https://github.com/Netflix/dispatch) [![GitHub stars](https://img.shields.io/github/stars/Netflix/dispatch?style=flat)](https://github.com/Netflix/dispatch/stargazers) - Manage security incidents.
- FastAPI CRUD Example:
  - [Async flavor](https://github.com/testdrivenio/fastapi-crud-async) [![GitHub stars](https://img.shields.io/github/stars/testdrivenio/fastapi-crud-async?style=flat)](https://github.com/testdrivenio/fastapi-crud-async/stargazers)
  - [Sync Flavor](https://github.com/testdrivenio/fastapi-crud-sync) [![GitHub stars](https://img.shields.io/github/stars/testdrivenio/fastapi-crud-sync?style=flat)](https://github.com/testdrivenio/fastapi-crud-sync/stargazers)
- [FastAPI with Observability](https://github.com/Blueswen/fastapi-observability) [![GitHub stars](https://img.shields.io/github/stars/Blueswen/fastapi-observability?style=flat)](https://github.com/Blueswen/fastapi-observability/stargazers) - Observe FastAPI app with three pillars of observability: Traces (Tempo), Metrics (Prometheus), Logs (Loki) on Grafana through OpenTelemetry and OpenMetrics.
- [DogeAPI](https://github.com/yezz123/DogeAPI) [![GitHub stars](https://img.shields.io/github/stars/yezz123/DogeAPI?style=flat)](https://github.com/yezz123/DogeAPI/stargazers) - API with high performance to create a simple blog and CRUD with OAuth2PasswordBearer.
- [FastAPI Websocket Broadcast](https://github.com/kthwaite/fastapi-websocket-broadcast) [![GitHub stars](https://img.shields.io/github/stars/kthwaite/fastapi-websocket-broadcast?style=flat)](https://github.com/kthwaite/fastapi-websocket-broadcast/stargazers) - Websocket 'broadcast' demo.
- [FastAPI with Celery, RabbitMQ, and Redis](https://github.com/GregaVrbancic/fastapi-celery) [![GitHub stars](https://img.shields.io/github/stars/GregaVrbancic/fastapi-celery?style=flat)](https://github.com/GregaVrbancic/fastapi-celery/stargazers) - Minimal example utilizing FastAPI and Celery with RabbitMQ for task queue, Redis for Celery backend, and Flower for monitoring the Celery tasks.
- [FuturamaAPI](https://github.com/koldakov/futuramaapi) [![GitHub stars](https://img.shields.io/github/stars/koldakov/futuramaapi?style=flat)](https://github.com/koldakov/futuramaapi/stargazers) - A REST and GraphQL playground built with best practices, providing WebSockets, SSE, callbacks, secret messages, and more.
- [JeffQL](https://github.com/yezz123/JeffQL/) [![GitHub stars](https://img.shields.io/github/stars/yezz123/JeffQL/?style=flat)](https://github.com/yezz123/JeffQL//stargazers) - Simple authentication and login API using GraphQL and JWT.
- [JSON-RPC Server](https://github.com/smagafurov/fastapi-jsonrpc) [![GitHub stars](https://img.shields.io/github/stars/smagafurov/fastapi-jsonrpc?style=flat)](https://github.com/smagafurov/fastapi-jsonrpc/stargazers) - JSON-RPC server based on FastAPI.
- [Mailer](https://github.com/rclement/mailer) [![GitHub stars](https://img.shields.io/github/stars/rclement/mailer?style=flat)](https://github.com/rclement/mailer/stargazers) - Dead-simple mailer micro-service for static websites.
- [Markdown-Videos](https://github.com/Snailedlt/Markdown-Videos) [![GitHub stars](https://img.shields.io/github/stars/Snailedlt/Markdown-Videos?style=flat)](https://github.com/Snailedlt/Markdown-Videos/stargazers) - API for generating thumbnails to embed into your markdown content.
- [Nemo](https://github.com/harshitsinghai77/nemo-backend) [![GitHub stars](https://img.shields.io/github/stars/harshitsinghai77/nemo-backend?style=flat)](https://github.com/harshitsinghai77/nemo-backend/stargazers) - Be productive with Nemo.
- [OPAL (Open Policy Administration Layer)](https://github.com/authorizon/opal) [![GitHub stars](https://img.shields.io/github/stars/authorizon/opal?style=flat)](https://github.com/authorizon/opal/stargazers) - Real-time authorization updates on top of Open-Policy; built with FastAPI, Typer, and FastAPI WebSocket pub/sub.
- [OSBot-Fast-API](https://github.com/owasp-sbot/OSBot-Fast-API) [![GitHub stars](https://img.shields.io/github/stars/owasp-sbot/OSBot-Fast-API?style=flat)](https://github.com/owasp-sbot/OSBot-Fast-API/stargazers) - Type-safe FastAPI wrapper that provides middleware, HTTP event tracking, AWS Lambda integration, test utilities, and auto-conversion between Type_Safe, Pydantic, and dataclasses.
- [Polar](https://github.com/polarsource/polar) [![GitHub stars](https://img.shields.io/github/stars/polarsource/polar?style=flat)](https://github.com/polarsource/polar/stargazers) - A funding and monetization platform for developers, built with FastAPI, SQLAlchemy, Alembic, and Arq.
- [RealWorld Example App - mongo](https://github.com/markqiu/fastapi-mongodb-realworld-example-app) [![GitHub stars](https://img.shields.io/github/stars/markqiu/fastapi-mongodb-realworld-example-app?style=flat)](https://github.com/markqiu/fastapi-mongodb-realworld-example-app/stargazers)
- [RealWorld Example App - postgres](https://github.com/nsidnev/fastapi-realworld-example-app) [![GitHub stars](https://img.shields.io/github/stars/nsidnev/fastapi-realworld-example-app?style=flat)](https://github.com/nsidnev/fastapi-realworld-example-app/stargazers)
- [redis-streams-fastapi-chat](https://github.com/leonh/redis-streams-fastapi-chat) [![GitHub stars](https://img.shields.io/github/stars/leonh/redis-streams-fastapi-chat?style=flat)](https://github.com/leonh/redis-streams-fastapi-chat/stargazers) - A simple Redis Streams backed chat app using Websockets, Asyncio and FastAPI/Starlette.
- [Sprites as a service](https://github.com/ljvmiranda921/sprites-as-a-service) [![GitHub stars](https://img.shields.io/github/stars/ljvmiranda921/sprites-as-a-service?style=flat)](https://github.com/ljvmiranda921/sprites-as-a-service/stargazers) - Generate your personal 8-bit avatars using Cellular Automata.
- [Slackers](https://github.com/uhavin/slackers) [![GitHub stars](https://img.shields.io/github/stars/uhavin/slackers?style=flat)](https://github.com/uhavin/slackers/stargazers) - Slack webhooks API.
- [TermPair](https://github.com/cs01/termpair) [![GitHub stars](https://img.shields.io/github/stars/cs01/termpair?style=flat)](https://github.com/cs01/termpair/stargazers) - View and control terminals from your browser with end-to-end encryption.
- [Universities](https://github.com/ycd/universities) [![GitHub stars](https://img.shields.io/github/stars/ycd/universities?style=flat)](https://github.com/ycd/universities/stargazers) - API service for obtaining information about +9600 universities worldwide.

## Sponsors

Please support this open source project by checking out our sponsors:

<a href="https://testdriven.io/courses/tdd-fastapi/?ref=awesome-fastapi" target="_blank" title="Learn to build high-quality web apps with best practices"><img src="images/testdriven.svg"></a>
