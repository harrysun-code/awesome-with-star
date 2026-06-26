# Pyramid

[![GitHub stars](https://img.shields.io/github/stars/uralbash/awesome-pyramid?style=flat)](https://github.com/uralbash/awesome-pyramid/stargazers)

# Awesome Pyramid
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![IRC
Freenode](https://img.shields.io/badge/irc-freenode-blue.svg)](https://webchat.freenode.net/?channels=pyramid)

A curated list of awesome Pyramid apps, projects and resources. Inspired by and
based on [awesome-python](https://github.com/vinta/awesome-python/) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python/?style=flat)](https://github.com/vinta/awesome-python//stargazers).

- [Awesome Pyramid](#awesome-pyramid)
    - [Admin Interface](#admin-interface)
    - [Asset Management](#asset-management)
    - [Async](#async)
    - [Authentication](#authentication)
    - [Authorization](#authorization)
    - [Caching & Session](#caching--session)
    - [Debugging](#debugging)
    - [Email](#email)
    - [Forms](#forms)
    - [Media-Management](#media-management)
    - [RESTful API](#restful-api)
    - [Search](#search)
    - [Security](#security)
    - [Services](#services)
    - [Settings](#settings)
    - [Storage](#storage)
    - [Task Queue](#task-queue)
    - [Testing](#testing)
    - [Translations](#translations)
    - [Web frontend integration](#web-frontend-integration)
    - [Workflows](#workflows)
    - [Other](#other)
- [Projects](#projects)
    - [Framework](#framework)
    - [CMS](#cms)
    - [Cookiecutters](#cookiecutters)
    - [e-Commerce](#e-commerce)
    - [Project Management](#project-management)
    - [Other](#other)
- [Resources](#resources)
    - [Books](#books)
    - [Websites](#websites)
    - [Conferences](#conferences)
    - [Videos](#videos)
    - [Who uses it?](#who-uses-it)
- [Contributing](#contributing)

## Admin interface

*Packages that extend the Admin interface, adding or improving features.*

* [pyramid_formalchemy](https://github.com/FormAlchemy/pyramid_formalchemy) [![GitHub stars](https://img.shields.io/github/stars/FormAlchemy/pyramid_formalchemy?style=flat)](https://github.com/FormAlchemy/pyramid_formalchemy/stargazers) -
  provides a CRUD interface for pyramid based on FormAlchemy.
* [pyramid_sacrud](https://github.com/sacrud/pyramid_sacrud) [![GitHub stars](https://img.shields.io/github/stars/sacrud/pyramid_sacrud?style=flat)](https://github.com/sacrud/pyramid_sacrud/stargazers) -    Pyramid CRUD interface.
  Provides an administration web interface for Pyramid.
  Unlike classic CRUD, pyramid_sacrud allows overrides and flexibility to
  customize your interface, similar to django.contrib.admin but uses a
  different backend to provide resources. [New Architecture](
  <http://pyramid-sacrud.readthedocs.io/pages/contribute/architecture.html>)
  built on the resources and mechanism traversal, allows to use it in various cases.
    * [ps_alchemy](https://github.com/sacrud/ps_alchemy) [![GitHub stars](https://img.shields.io/github/stars/sacrud/ps_alchemy?style=flat)](https://github.com/sacrud/ps_alchemy/stargazers) - extension for pyramid_sacrud
      which provides SQLAlchemy models.
    * [ps_tree](https://github.com/sacrud/ps_tree) [![GitHub stars](https://img.shields.io/github/stars/sacrud/ps_tree?style=flat)](https://github.com/sacrud/ps_tree/stargazers) - extension for
      [pyramid_sacrud](https://github.com/sacrud/pyramid_sacrud) [![GitHub stars](https://img.shields.io/github/stars/sacrud/pyramid_sacrud?style=flat)](https://github.com/sacrud/pyramid_sacrud/stargazers) which displays
      a list of records as tree. This works fine with models from
      [sqlalchemy_mptt](https://github.com/uralbash/sqlalchemy_mptt) [![GitHub stars](https://img.shields.io/github/stars/uralbash/sqlalchemy_mptt?style=flat)](https://github.com/uralbash/sqlalchemy_mptt/stargazers).
* [Websauna](https://websauna.org/docs/) - a full stack application framework for Pyramid

## Asset Management

*Packages that help manage the static assets of a project.*

* [pyramid_webassets](https://github.com/sontek/pyramid_webassets) [![GitHub stars](https://img.shields.io/github/stars/sontek/pyramid_webassets?style=flat)](https://github.com/sontek/pyramid_webassets/stargazers) - Pyramid
  extension for working with the webassets library.
* [pyramid_bowerstatic](https://github.com/mrijken/pyramid_bowerstatic) [![GitHub stars](https://img.shields.io/github/stars/mrijken/pyramid_bowerstatic?style=flat)](https://github.com/mrijken/pyramid_bowerstatic/stargazers) -
  integration of Bowerstatic in Pyramid

## Async

* [aiopyramid](https://github.com/housleyjk/aiopyramid) [![GitHub stars](https://img.shields.io/github/stars/housleyjk/aiopyramid?style=flat)](https://github.com/housleyjk/aiopyramid/stargazers) - Run pyramid using
  asyncio.
* [gevent-socketio](https://github.com/abourget/gevent-socketio) [![GitHub stars](https://img.shields.io/github/stars/abourget/gevent-socketio?style=flat)](https://github.com/abourget/gevent-socketio/stargazers) -
  gevent-socketio is a Python implementation of the Socket.IO protocol,
  developed originally for Node.js by LearnBoost and then ported to other
  languages.
* [Stargate](https://github.com/boothead/stargate) [![GitHub stars](https://img.shields.io/github/stars/boothead/stargate?style=flat)](https://github.com/boothead/stargate/stargazers) - Stargate is a package for
  adding WebSockets support to pyramid applications using the excellent
  eventlet library for long running connections.
* [channelstream](https://github.com/AppEnlight/channelstream) [![GitHub stars](https://img.shields.io/github/stars/AppEnlight/channelstream?style=flat)](https://github.com/AppEnlight/channelstream/stargazers) - websocket communication server (gevent).

## Authentication

*Packages that improve or extend the authentication methods of Pyramid.*

* [pyramid_ldap](https://github.com/Pylons/pyramid_ldap) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_ldap?style=flat)](https://github.com/Pylons/pyramid_ldap/stargazers) - an LDAP
  authentication policy for Pyramid.
* [pyramid_ldap3](https://github.com/Cito/pyramid_ldap3) [![GitHub stars](https://img.shields.io/github/stars/Cito/pyramid_ldap3?style=flat)](https://github.com/Cito/pyramid_ldap3/stargazers) - Provides LDAP authentication
  services for your Pyramid application based on the ldap3 package.
* [pyramid_who](https://github.com/Pylons/pyramid_who) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_who?style=flat)](https://github.com/Pylons/pyramid_who/stargazers) - Authentication policy
  for pyramid using repoze.who 2.0 API.
* [velruse](https://github.com/bbangert/velruse) [![GitHub stars](https://img.shields.io/github/stars/bbangert/velruse?style=flat)](https://github.com/bbangert/velruse/stargazers) - Simplifying third-party
  authentication for web applications. it supports most of auth
  [providers](https://github.com/bbangert/velruse/tree/master/velruse/providers) [![GitHub stars](https://img.shields.io/github/stars/bbangert/velruse/tree/master/velruse/providers?style=flat)](https://github.com/bbangert/velruse/tree/master/velruse/providers/stargazers).
* [pyramid_simpleauth](https://github.com/thruflo/pyramid_simpleauth) [![GitHub stars](https://img.shields.io/github/stars/thruflo/pyramid_simpleauth?style=flat)](https://github.com/thruflo/pyramid_simpleauth/stargazers) - session
  based authentication and role based security for Pyramid application
* [Python Social Auth](https://github.com/omab/python-social-auth) [![GitHub stars](https://img.shields.io/github/stars/omab/python-social-auth?style=flat)](https://github.com/omab/python-social-auth/stargazers) - Social
  authentication/registration mechanism with support for a large number of
  [providers](https://github.com/omab/python-social-auth#auth-providers).
* [Authomatic](https://github.com/authomatic/authomatic) [![GitHub stars](https://img.shields.io/github/stars/authomatic/authomatic?style=flat)](https://github.com/authomatic/authomatic/stargazers) -  Simple yet powerful
  authorization / authentication client library for Python web applications.
* [apex](https://github.com/cd34/apex) [![GitHub stars](https://img.shields.io/github/stars/cd34/apex?style=flat)](https://github.com/cd34/apex/stargazers) - Toolkit for Pyramid, a Pylons Project,
  to add Authentication and Authorization using Velruse (OAuth) and/or a local
  database, CSRF, ReCaptcha, Sessions, Flash messages and I18N.
* [pyramid_authsanity](https://github.com/usingnamespace/pyramid_authsanity) [![GitHub stars](https://img.shields.io/github/stars/usingnamespace/pyramid_authsanity?style=flat)](https://github.com/usingnamespace/pyramid_authsanity/stargazers) -
  That will make it simpler to have a secure authentication policy with an easy
  to use backend.
* [pyramid_jwt](https://github.com/wichert/pyramid_jwt) [![GitHub stars](https://img.shields.io/github/stars/wichert/pyramid_jwt?style=flat)](https://github.com/wichert/pyramid_jwt/stargazers) - This package
  implements an authentication policy for Pyramid that using [JSON Web Tokens].
  This standard ([RFC 7519]) is often used to secure backens APIs. The
  excellent [PyJWT] library is used for the JWT encoding / decoding logic.
* [pyramid_ipauth](https://github.com/mozilla-services/pyramid_ipauth) [![GitHub stars](https://img.shields.io/github/stars/mozilla-services/pyramid_ipauth?style=flat)](https://github.com/mozilla-services/pyramid_ipauth/stargazers) -
  Pyramid authentication policy based on remote ip address.

  [JSON Web Tokens]: https://jwt.io/
  [RFC 7519]: https://tools.ietf.org/html/rfc7519
  [PyJWT]: https://pyjwt.readthedocs.io/en/latest/


## Authorization

*Packages related to authorization infrastructure and permissions.*

* [ziggurat_foundations](https://github.com/ergo/ziggurat_foundations) [![GitHub stars](https://img.shields.io/github/stars/ergo/ziggurat_foundations?style=flat)](https://github.com/ergo/ziggurat_foundations/stargazers) -
  Framework agnostic set of sqlalchemy classes that make building applications
  that require permissions an easy task.
* [pyramid_multiauth](https://github.com/mozilla-services/pyramid_multiauth) [![GitHub stars](https://img.shields.io/github/stars/mozilla-services/pyramid_multiauth?style=flat)](https://github.com/mozilla-services/pyramid_multiauth/stargazers) -
  An authentication policy for Pyramid that proxies to a stack of other
  authentication policies.
* [pyramid_authstack](https://github.com/wichert/pyramid_authstack) [![GitHub stars](https://img.shields.io/github/stars/wichert/pyramid_authstack?style=flat)](https://github.com/wichert/pyramid_authstack/stargazers) -  Use
  multiple authentication policies with Pyramid.
* [horus](https://github.com/Pylons/horus) [![GitHub stars](https://img.shields.io/github/stars/Pylons/horus?style=flat)](https://github.com/Pylons/horus/stargazers) - User registration and login system
  for the Pyramid Web Framework.
* [pyramid_yosai](https://github.com/YosaiProject/pyramid_yosai) [![GitHub stars](https://img.shields.io/github/stars/YosaiProject/pyramid_yosai?style=flat)](https://github.com/YosaiProject/pyramid_yosai/stargazers) - Pyramid integration with security Framework for Python applications featuring Authorization (rbac permissions and roles), Authentication (2fa totp), Session Management and an extensive Audit Trail https://yosaiproject.github.io/yosai/

## Caching & Session

*Packages that help with caching and session.*

* [pyramid_beaker](https://github.com/Pylons/pyramid_beaker) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_beaker?style=flat)](https://github.com/Pylons/pyramid_beaker/stargazers) - A Beaker session
  factory backend for Pyramid, also cache configurator.
    * [Why You'll Want to Switch to
      dogpile.cache](http://techspot.zzzeek.org/2012/04/19/using-beaker-for-caching-why-you-ll-want-to-switch-to-dogpile.cache/)
* [pyramid_redis_sessions](https://github.com/ericrasmussen/pyramid_redis_sessions) [![GitHub stars](https://img.shields.io/github/stars/ericrasmussen/pyramid_redis_sessions?style=flat)](https://github.com/ericrasmussen/pyramid_redis_sessions/stargazers) -
  Pyramid web framework session factory backed by Redis.
* [pyramid_dogpile_cache](https://github.com/moriyoshi/pyramid_dogpile_cache) [![GitHub stars](https://img.shields.io/github/stars/moriyoshi/pyramid_dogpile_cache?style=flat)](https://github.com/moriyoshi/pyramid_dogpile_cache/stargazers) -
  dogpile.cache configuration package for Pyramid
* [pyramid_sessions](https://github.com/joulez/pyramid_sessions) [![GitHub stars](https://img.shields.io/github/stars/joulez/pyramid_sessions?style=flat)](https://github.com/joulez/pyramid_sessions/stargazers) - Multiple
  session support for the Pyramid Web Framework
* [pyramid_nacl_session](https://github.com/Pylons/pyramid_nacl_session) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_nacl_session?style=flat)](https://github.com/Pylons/pyramid_nacl_session/stargazers) -
  defines an encrypting, pickle-based cookie serializer, using
  [PyNaCl](http://pynacl.readthedocs.io/en/latest/secret/) to generate the
  symmetric encryption for the cookie state.

## Debugging

*Packages that help hunt down bugs.*

* [pyramid_debugtoolbar](https://github.com/Pylons/pyramid_debugtoolbar) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_debugtoolbar?style=flat)](https://github.com/Pylons/pyramid_debugtoolbar/stargazers) -
  provides a debug toolbar useful while you're developing your Pyramid
  application.
* [pyramid_exclog](https://github.com/Pylons/pyramid_exclog) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_exclog?style=flat)](https://github.com/Pylons/pyramid_exclog/stargazers) - a package which
  logs exceptions from Pyramid applications.
* [pyramid_debugtoolbar_dogpile](https://github.com/jvanasco/pyramid_debugtoolbar_dogpile) [![GitHub stars](https://img.shields.io/github/stars/jvanasco/pyramid_debugtoolbar_dogpile?style=flat)](https://github.com/jvanasco/pyramid_debugtoolbar_dogpile/stargazers) -
  dogpile caching support for pyramid_debugtoolbar
* [pyramid_ipython](https://github.com/Pylons/pyramid_ipython) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_ipython?style=flat)](https://github.com/Pylons/pyramid_ipython/stargazers) - IPython
  bindings for Pyramid's pshell
* [pyramid_bpython](https://github.com/Pylons/pyramid_bpython) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_bpython?style=flat)](https://github.com/Pylons/pyramid_bpython/stargazers) - bpython
  bindings for Pyramid's pshell
* [pyramid_pycallgraph](https://github.com/disko/pyramid_pycallgraph) [![GitHub stars](https://img.shields.io/github/stars/disko/pyramid_pycallgraph?style=flat)](https://github.com/disko/pyramid_pycallgraph/stargazers) - Pyramid tween to generate a callgraph image for every request

## Email

*Packages that help manage email sending.*

* [pyramid_mailer](https://github.com/Pylons/pyramid_mailer) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_mailer?style=flat)](https://github.com/Pylons/pyramid_mailer/stargazers) - A package for
  sending email from your Pyramid application.
* [pyramid_marrowmailer](https://github.com/domenkozar/pyramid_marrowmailer) [![GitHub stars](https://img.shields.io/github/stars/domenkozar/pyramid_marrowmailer?style=flat)](https://github.com/domenkozar/pyramid_marrowmailer/stargazers) -
  Pyramid integration package for marrow.mailer, formerly known as TurboMail
* [pyramid_mailgun](https://github.com/evannook/pyramid_mailgun) [![GitHub stars](https://img.shields.io/github/stars/evannook/pyramid_mailgun?style=flat)](https://github.com/evannook/pyramid_mailgun/stargazers) - Mailgun integration for Pyramid framework.

## Forms

*Packages that extend the functionality of forms or add new types of forms.*

* [deform](https://github.com/Pylons/deform) [![GitHub stars](https://img.shields.io/github/stars/Pylons/deform?style=flat)](https://github.com/Pylons/deform/stargazers) - is a Python HTML form generation
  library.
* [colander](https://github.com/Pylons/colander) [![GitHub stars](https://img.shields.io/github/stars/Pylons/colander?style=flat)](https://github.com/Pylons/colander/stargazers) - A
  serialization/deserialization/validation library for strings, mappings and
  lists.
* [WTForms](https://github.com/wtforms/wtforms) [![GitHub stars](https://img.shields.io/github/stars/wtforms/wtforms?style=flat)](https://github.com/wtforms/wtforms/stargazers) - is a flexible forms
  validation and rendering library for python web development.
* [ColanderAlchemy](https://github.com/stefanofontanelli/ColanderAlchemy) [![GitHub stars](https://img.shields.io/github/stars/stefanofontanelli/ColanderAlchemy?style=flat)](https://github.com/stefanofontanelli/ColanderAlchemy/stargazers) -
  helps you to auto-generate Colander schemas that are based on SQLAlchemy
  mapped classes.
* [marshmallow](https://github.com/marshmallow-code/marshmallow) [![GitHub stars](https://img.shields.io/github/stars/marshmallow-code/marshmallow?style=flat)](https://github.com/marshmallow-code/marshmallow/stargazers) - A
  lightweight library for converting complex objects to and from simple Python
  datatypes (i.e. (de)serialization and validation).

## Media-Management

* [pyramid_elfinder](https://github.com/uralbash/pyramid_elfinder) [![GitHub stars](https://img.shields.io/github/stars/uralbash/pyramid_elfinder?style=flat)](https://github.com/uralbash/pyramid_elfinder/stargazers) - This is
  conector for elfinder file manager, written for pyramid framework.
* [pyramid_storage](https://github.com/danjac/pyramid_storage) [![GitHub stars](https://img.shields.io/github/stars/danjac/pyramid_storage?style=flat)](https://github.com/danjac/pyramid_storage/stargazers) - This is a package for handling file uploads in your Pyramid framework application.

## RESTful API

*Packages for developing RESTful APIs.*

* [cornice](https://github.com/Cornices/cornice) [![GitHub stars](https://img.shields.io/github/stars/Cornices/cornice?style=flat)](https://github.com/Cornices/cornice/stargazers) - provides helpers to
  build & document REST-ish Web Services with Pyramid, with decent default
  behaviors. It takes care of following the HTTP specification in an automated
  way where possible.
* [rest_toolkit](https://github.com/wichert/rest_toolkit) [![GitHub stars](https://img.shields.io/github/stars/wichert/rest_toolkit?style=flat)](https://github.com/wichert/rest_toolkit/stargazers) - is a Python package
  which provides a very convenient way to build REST servers. It is build on
  top of Pyramid, but you do not need to know much about Pyramid to use
  rest_toolkit.
* [pyramid_royal](https://github.com/hadrien/pyramid_royal) [![GitHub stars](https://img.shields.io/github/stars/hadrien/pyramid_royal?style=flat)](https://github.com/hadrien/pyramid_royal/stargazers) - Royal is a
  pyramid extension which eases writing RESTful web applications.
* [cliquet](https://github.com/mozilla-services/cliquet) [![GitHub stars](https://img.shields.io/github/stars/mozilla-services/cliquet?style=flat)](https://github.com/mozilla-services/cliquet/stargazers) - Cliquet is a toolkit
  to ease the implementation of HTTP microservices, such as data-driven REST
  APIs.
* [webargs](https://github.com/sloria/webargs) [![GitHub stars](https://img.shields.io/github/stars/sloria/webargs?style=flat)](https://github.com/sloria/webargs/stargazers) - A friendly library for parsing
  HTTP request arguments, with built-in support for popular web frameworks.
* [ramses](https://github.com/ramses-tech/ramses) [![GitHub stars](https://img.shields.io/github/stars/ramses-tech/ramses?style=flat)](https://github.com/ramses-tech/ramses/stargazers) - Generate a RESTful API using
  RAML. It uses Nefertari which provides ElasticSearch-powered views.
* [nefertari](https://github.com/ramses-tech/nefertari) [![GitHub stars](https://img.shields.io/github/stars/ramses-tech/nefertari?style=flat)](https://github.com/ramses-tech/nefertari/stargazers) -  Nefertari is a REST
  API framework sitting on top of Pyramid and ElasticSearch.
* [pyramid_swagger](https://github.com/striglia/pyramid_swagger) [![GitHub stars](https://img.shields.io/github/stars/striglia/pyramid_swagger?style=flat)](https://github.com/striglia/pyramid_swagger/stargazers) - Convenient
  tools for using Swagger to define and validate your interfaces in a Pyramid webapp. (Swagger 2.0 document)
* [pyramid-openapi3](https://github.com/niteoweb/pyramid_openapi3) [![GitHub stars](https://img.shields.io/github/stars/niteoweb/pyramid_openapi3?style=flat)](https://github.com/niteoweb/pyramid_openapi3/stargazers) - Validate Pyramid views against an OpenAPI 3.0 document. Similar to pyramid_swagger but for OpenAPI 3.0.
* [pyramid_jsonapi](https://github.com/colinhiggs/pyramid-jsonapi) [![GitHub stars](https://img.shields.io/github/stars/colinhiggs/pyramid-jsonapi?style=flat)](https://github.com/colinhiggs/pyramid-jsonapi/stargazers) - Automatically 
  create a [JSON API](http://jsonapi.org/) standard API from a database using the
  sqlAlchemy ORM and pyramid framework.
* [pyramid_apispec](https://github.com/ergo/pyramid_apispec) [![GitHub stars](https://img.shields.io/github/stars/ergo/pyramid_apispec?style=flat)](https://github.com/ergo/pyramid_apispec/stargazers) - Create an OpenAPI
  specification file using apispec and Marshmallow schemas.


## Search

*Packages that provide search capabilities to projects.*

* [hypatia](https://github.com/Pylons/hypatia) [![GitHub stars](https://img.shields.io/github/stars/Pylons/hypatia?style=flat)](https://github.com/Pylons/hypatia/stargazers) - A Python indexing and
  searching system.

## Security

*Packages that improve the security of a project.*

## Services

* [pyramid_sms](https://github.com/websauna/pyramid_sms) [![GitHub stars](https://img.shields.io/github/stars/websauna/pyramid_sms?style=flat)](https://github.com/websauna/pyramid_sms/stargazers) -
   SMS services for Pyramid web framework.

## Settings

*Packages that help manage the configurability of projects.*

* [pyramid_zcml](https://github.com/Pylons/pyramid_zcml) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_zcml?style=flat)](https://github.com/Pylons/pyramid_zcml/stargazers) - Zope Configuration
  Markup Language configuration support for Pyramid.
* [pyramid_services](https://github.com/mmerickel/pyramid_services) [![GitHub stars](https://img.shields.io/github/stars/mmerickel/pyramid_services?style=flat)](https://github.com/mmerickel/pyramid_services/stargazers) - defines a
  pattern and helper methods for accessing a pluggable service layer from
  within your Pyramid apps.
* [hupper](https://github.com/Pylons/hupper) [![GitHub stars](https://img.shields.io/github/stars/Pylons/hupper?style=flat)](https://github.com/Pylons/hupper/stargazers) - A process monitor/reloader for developers
    that can watch files for changes and restart the process.

## Storage

*Packages that extend the functionality of the existing storage backend or
provide new storage backends.*

* [pyramid_tm](https://github.com/Pylons/pyramid_tm) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_tm?style=flat)](https://github.com/Pylons/pyramid_tm/stargazers) - Centralized transaction
  management for Pyramid applications (without middleware).
* [zope.sqlalchemy](https://github.com/zopefoundation/zope.sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/zopefoundation/zope.sqlalchemy?style=flat)](https://github.com/zopefoundation/zope.sqlalchemy/stargazers) -
  Integration of SQLAlchemy with transaction management.
    * [What the Zope Transaction Manager Means To Me (and
      you)](https://metaclassical.com/what-the-zope-transaction-manager-means-to-me-and-you/)
* [pyramid_sqlalchemy](https://github.com/wichert/pyramid_sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/wichert/pyramid_sqlalchemy?style=flat)](https://github.com/wichert/pyramid_sqlalchemy/stargazers) -
  provides some basic glue to facilitate using SQLAlchemy with Pyramid.
* [pyramid_zodbconn](https://github.com/Pylons/pyramid_zodbconn) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_zodbconn?style=flat)](https://github.com/Pylons/pyramid_zodbconn/stargazers) - ZODB
  Database connection management for Pyramid.
* [pyramid_mongoengine](https://github.com/marioidival/pyramid_mongoengine) [![GitHub stars](https://img.shields.io/github/stars/marioidival/pyramid_mongoengine?style=flat)](https://github.com/marioidival/pyramid_mongoengine/stargazers) -
  pyramid-mongoengine package based on flask-mongoengine
* [pyramid_mongodb](https://github.com/niallo/pyramid_mongodb) [![GitHub stars](https://img.shields.io/github/stars/niallo/pyramid_mongodb?style=flat)](https://github.com/niallo/pyramid_mongodb/stargazers) - 
  Basic Pyramid Scaffold to easily use MongoDB for persistence with the Pyramid Web framework
* [pyramid-excel](https://github.com/pyexcel-webwares/pyramid-excel) [![GitHub stars](https://img.shields.io/github/stars/pyexcel-webwares/pyramid-excel?style=flat)](https://github.com/pyexcel-webwares/pyramid-excel/stargazers) - pyramid-excel is based on [pyexcel](https://github.com/pyexcel/pyexcel) [![GitHub stars](https://img.shields.io/github/stars/pyexcel/pyexcel?style=flat)](https://github.com/pyexcel/pyexcel/stargazers) and makes it easy to consume/produce information stored in excel files over HTTP protocol as well as on file system. This library can turn the excel data into a list of lists, a list of records(dictionaries), dictionaries of lists. And vice versa. Hence it lets you focus on data in Pyramid based web development, instead of file formats.

## Task Queue

*Packages that make working with task/background queues easier.*

* [pyramid_celery](https://github.com/sontek/pyramid_celery) [![GitHub stars](https://img.shields.io/github/stars/sontek/pyramid_celery?style=flat)](https://github.com/sontek/pyramid_celery/stargazers) - Pyramid
  configuration with celery integration. Allows you to use pyramid .ini files
  to configure celery and have your pyramid configuration inside celery tasks.
* [pyramid_rq](https://github.com/wichert/pyramid_rq) [![GitHub stars](https://img.shields.io/github/stars/wichert/pyramid_rq?style=flat)](https://github.com/wichert/pyramid_rq/stargazers) - Support using the rq
  queueing system with pyramid. The easiest way to monitor and use
  [RQ](http://python-rq.org) in your Pyramid projects.

## Templates

* [pyramid_mako](https://github.com/Pylons/pyramid_mako) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_mako?style=flat)](https://github.com/Pylons/pyramid_mako/stargazers) - Mako templating
  system bindings for the Pyramid web framework.
* [pyramid_chameleon](https://github.com/Pylons/pyramid_chameleon) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_chameleon?style=flat)](https://github.com/Pylons/pyramid_chameleon/stargazers) - Chameleon
  template compiler for pyramid.
* [pyramid_jinja2](https://github.com/Pylons/pyramid_jinja2) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_jinja2?style=flat)](https://github.com/Pylons/pyramid_jinja2/stargazers) - Jinja2
  templating system bindings for the Pyramid web framework.
* [Tonnikala](https://github.com/ztane/Tonnikala) [![GitHub stars](https://img.shields.io/github/stars/ztane/Tonnikala?style=flat)](https://github.com/ztane/Tonnikala/stargazers) - Python templating engine
  with Pyramid integration
* [Kajiki](https://github.com/nandoflorestan/kajiki) [![GitHub stars](https://img.shields.io/github/stars/nandoflorestan/kajiki?style=flat)](https://github.com/nandoflorestan/kajiki/stargazers) - provides fast well-formed XML templates, with [Pyramid integration](https://github.com/nandoflorestan/kajiki/blob/master/kajiki/integration/pyramid.py) [![GitHub stars](https://img.shields.io/github/stars/nandoflorestan/kajiki/blob/master/kajiki/integration/pyramid.py?style=flat)](https://github.com/nandoflorestan/kajiki/blob/master/kajiki/integration/pyramid.py/stargazers)

## Testing

*Packages that help test code or generate test data.*

* [webtest](https://github.com/Pylons/webtest) [![GitHub stars](https://img.shields.io/github/stars/Pylons/webtest?style=flat)](https://github.com/Pylons/webtest/stargazers) - Wraps any WSGI application and
  makes it easy to send test requests to that application, without starting up
  an HTTP server.

## Translations

*Packages help with the task of translating projects.*

* [lingua](https://github.com/wichert/lingua) [![GitHub stars](https://img.shields.io/github/stars/wichert/lingua?style=flat)](https://github.com/wichert/lingua/stargazers) - Lingua is a package with tools
  to extract translatable texts from your code, and to check existing
  translations. It replaces the use of the xgettext command from gettext, or
  pybabel from Babel.
* [pyramid_i18n_helper](https://github.com/sahama/pyramid_i18n_helper) [![GitHub stars](https://img.shields.io/github/stars/sahama/pyramid_i18n_helper?style=flat)](https://github.com/sahama/pyramid_i18n_helper/stargazers) - helper to create new smgid and translate msgid to local langs .

## Web frontend integration

* [PyramidVue](https://github.com/eddyekofo94/pyramidVue) [![GitHub stars](https://img.shields.io/github/stars/eddyekofo94/pyramidVue?style=flat)](https://github.com/eddyekofo94/pyramidVue/stargazers) - Pyramid and VueJs (JavaScript) template with Hot-Module-Replacement starter template.

## Workflows

*Packages that do process, procedure and/or business tasks management.*

## Other

* [pyramid_layout](https://github.com/Pylons/pyramid_layout) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_layout?style=flat)](https://github.com/Pylons/pyramid_layout/stargazers) - Pyramid add-on
  for managing UI layouts.
* [pyramid_skins](https://github.com/Pylons/pyramid_skins) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_skins?style=flat)](https://github.com/Pylons/pyramid_skins/stargazers) - This package
  provides a simple framework to integrate code with templates and resources.
* [waitress](https://github.com/Pylons/waitress) [![GitHub stars](https://img.shields.io/github/stars/Pylons/waitress?style=flat)](https://github.com/Pylons/waitress/stargazers) - Waitress is meant to be a
  production-quality pure-Python WSGI server with very acceptable performance.
  It has no dependencies except ones which live in the Python standard library.
* [pyramid_handlers](https://github.com/Pylons/pyramid_handlers) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_handlers?style=flat)](https://github.com/Pylons/pyramid_handlers/stargazers) - analogue of
  Pylons-style “controllers” for Pyramid.
* [pyramid_rpc](https://github.com/Pylons/pyramid_rpc) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_rpc?style=flat)](https://github.com/Pylons/pyramid_rpc/stargazers) - RPC service add-on for
  Pyramid, supports XML-RPC in a more extensible manner than pyramid_xmlrpc
  with support for JSON-RPC and AMF.
* [pyramid_autodoc](https://github.com/SurveyMonkey/pyramid_autodoc) [![GitHub stars](https://img.shields.io/github/stars/SurveyMonkey/pyramid_autodoc?style=flat)](https://github.com/SurveyMonkey/pyramid_autodoc/stargazers) - Sphinx
  extension for documenting your Pyramid APIs.
* [pyramid_pages](https://github.com/uralbash/pyramid_pages) [![GitHub stars](https://img.shields.io/github/stars/uralbash/pyramid_pages?style=flat)](https://github.com/uralbash/pyramid_pages/stargazers) - Provides a
  collections of tree pages to your Pyramid application. This is very similar
  to django.contrib.flatpages but with a tree structure and traversal algorithm
  in URL dispatch.
* [paginate](https://github.com/Pylons/paginate) [![GitHub stars](https://img.shields.io/github/stars/Pylons/paginate?style=flat)](https://github.com/Pylons/paginate/stargazers) - Python pagination module.
* [pyramid_tablib](https://github.com/lxneng/pyramid_tablib) [![GitHub stars](https://img.shields.io/github/stars/lxneng/pyramid_tablib?style=flat)](https://github.com/lxneng/pyramid_tablib/stargazers) - tablib renderer
  (xlsx, xls, csv) for pyramid
* [tomb_routes](https://github.com/sontek/tomb_routes) [![GitHub stars](https://img.shields.io/github/stars/sontek/tomb_routes?style=flat)](https://github.com/sontek/tomb_routes/stargazers) - Simple utility library
  around pyramid routing
* [pyramid_extdirect](https://github.com/jenner/pyramid_extdirect) [![GitHub stars](https://img.shields.io/github/stars/jenner/pyramid_extdirect?style=flat)](https://github.com/jenner/pyramid_extdirect/stargazers) - This pyramid plugin provides a router for the ExtDirect Sencha API included in ExtJS. ExtDirect allows to run server-side callbacks directly through JavaScript without the extra AJAX boilerplate. 
* [pyramid_retry](https://github.com/Pylons/pyramid_retry) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid_retry?style=flat)](https://github.com/Pylons/pyramid_retry/stargazers) - pyramid_retry is an execution policy for Pyramid that wraps requests and can retry them a configurable number of times under certain "retryable" error conditions before indicating a failure to the client.

# Projects

*Outstanding Pyramid projects.*

## Framework

* [Ringo](http://www.ringo-framework.org/) - Ringo is a Python based high level
  web application framework build on top of Pyramid. The framework can be used
  to build form based management or administration software.
* [cone.app](https://github.com/conestack/cone.app) [![GitHub stars](https://img.shields.io/github/stars/conestack/cone.app?style=flat)](https://github.com/conestack/cone.app/stargazers) - A comprehensive web application stub on top of Pyramid.

## CMS

* [nive_cms](https://github.com/nive/nive_cms) [![GitHub stars](https://img.shields.io/github/stars/nive/nive_cms?style=flat)](https://github.com/nive/nive_cms/stargazers) - Nive is professional out the
  box content management system for mobile and desktop websites based on python
  and the webframework pyramid. Please refer to the website cms.nive.co for
  detailed information.
* [substanced](https://github.com/Pylons/substanced) [![GitHub stars](https://img.shields.io/github/stars/Pylons/substanced?style=flat)](https://github.com/Pylons/substanced/stargazers) - An application server
  built upon the Pyramid web framework. It provides a user interface for
  managing content as well as libraries and utilities which make it easy to
  create applications.
* [Kotti](https://github.com/Kotti/Kotti) [![GitHub stars](https://img.shields.io/github/stars/Kotti/Kotti?style=flat)](https://github.com/Kotti/Kotti/stargazers) - A user-friendly, light-weight and
  extensible web content management system. Based on Pyramid and SQLAlchemy.
* [KARL](https://karlproject.readthedocs.io/en/latest/) - A moderately-sized
  application (roughly 80K lines of Python code) built on top of Pyramid. It is
  an open source web
  system for collaboration, organizational intranets, and knowledge management.
  It provides facilities for wikis, calendars, manuals, searching, tagging,
  commenting, and file uploads. See the KARL site for download and installation
  details.
  
## Cookiecutters

* [Pylons](https://github.com/Pylons?q=cookiecutter) [![GitHub stars](https://img.shields.io/github/stars/Pylons?q=cookiecutter?style=flat)](https://github.com/Pylons?q=cookiecutter/stargazers) - official cookiecutter templates
* [Pyramid Runner](https://github.com/asif-mahmud/pyramid_runner) [![GitHub stars](https://img.shields.io/github/stars/asif-mahmud/pyramid_runner?style=flat)](https://github.com/asif-mahmud/pyramid_runner/stargazers) - A minimal Pyramid
  scaffold that aims to provide a starter template to build small to large web services.
  
  * Traversal based application
  * JSON only response
  * JWT authentication policy
  * Alembic for database revisions
  * Some simple modifications to base tests, views and models base to reduce typing


## e-Commerce

## Other

* [cluegun](https://github.com/Pylons/cluegun) [![GitHub stars](https://img.shields.io/github/stars/Pylons/cluegun?style=flat)](https://github.com/Pylons/cluegun/stargazers) - A simple pastebin application
  based on Rocky Burt’s ClueBin. It demonstrates form processing, security, and
  the use of ZODB within a Pyramid application.
* [shootout](https://github.com/Pylons/shootout) [![GitHub stars](https://img.shields.io/github/stars/Pylons/shootout?style=flat)](https://github.com/Pylons/shootout/stargazers) - An example “idea
  competition” application by Carlos de la Guardia and Lukasz Fidosz. It
  demonstrates URL dispatch, simple authentication, integration with SQLAlchemy
  and pyramid_simpleform.
* [virginia](https://github.com/Pylons/virginia) [![GitHub stars](https://img.shields.io/github/stars/Pylons/virginia?style=flat)](https://github.com/Pylons/virginia/stargazers) - A very simple dynamic
  file rendering application. It is willing to render structured text
  documents, HTML documents, and images from a filesystem directory. It’s also
  a good example of traversal. An earlier version of this application runs the
  repoze.org website.
* [Akhet](https://docs.pylonsproject.org/projects/akhet/en/latest/) -     A
  Pyramid library and demo application with a Pylons-like feel. Its most known
  for its former application scaffold, which helped users transition from
      Pylons and those preferring a more Pylons-like API. The scaffold has been
      retired but the demo plays a similar role.
* [Khufu Project](http://khufuproject.github.io/) - Khufu is an application
  scaffolding for Pyramid that provides an environment to work with Jinja2 and
  SQLAlchemy.
* [Ptah](https://github.com/ptahproject/ptah) [![GitHub stars](https://img.shields.io/github/stars/ptahproject/ptah?style=flat)](https://github.com/ptahproject/ptah/stargazers) - Ptah is a fast, fun, open
  source high-level Python web development environment.
* [warehouse](https://github.com/pypa/warehouse) [![GitHub stars](https://img.shields.io/github/stars/pypa/warehouse?style=flat)](https://github.com/pypa/warehouse/stargazers) - Warehouse is a next
  generation Python Package Repository designed to replace the legacy code base
  that currently powers PyPI.
* [travelcrm](https://github.com/mazvv/travelcrm) [![GitHub stars](https://img.shields.io/github/stars/mazvv/travelcrm?style=flat)](https://github.com/mazvv/travelcrm/stargazers) - TravelCRM is effective free and open source application for the automation of customer relationships for travel agencies at all levels, from small to large networks.
* [RhodeCode](https://rhodecode.com/) - enterprise source code management platform. It applies unified user control, permissions, code reviews, and tool integration across Mercurial, Git, and Subversion repositories. Large and growing software teams all over the world use RhodeCode to collaborate in a secure, behind-the-firewall environment. 

## Project Management

* [AppEnlight](https://getappenlight.com/) - Performance, exception, and uptime monitoring for the Web

# Resources

Where to discover new Pyramid apps and projects.

## Books

* [Python Web Frameworks](http://www.oreilly.com/web-platform/free/python-web-frameworks.csp) - Dive into details on the top
   six Python frameworks—Django, Flask, Tornado, Bottle, Pyramid, and CherryPy.

## Websites

* [Try Pyramid](https://trypyramid.com/) - The Start Small, Finish Big,
  Stay Finished Framework. Official website.

## Conferences

* [Sushi Sprint at PloneConf 2018 in Tokyo, Japan](https://2018.ploneconf.org/sprints) (November 10-11, 2018)
* [Pyramid Workshop in Munich, Germany.](https://pyconweb.com/talks/28-05-2017/pyramid-workshop) (May 28, 2017, 10:30 a.m. - 12:30 p.m.)
* [PloneConf 2017](https://2017.ploneconf.org/) - Barcelona Plone Digital Experience Conference (16~22 Oct. 2017)
* [PloneConf 2016](https://2016.ploneconf.org/) - Boston Plone Digital Experience Conference (17~23 Oct. 2016)
* [DragonSprint 2016](http://dragonsprint.com/) - DragonSprint is a week-long sprint on Pyramid. The sprint takes place in Ljubljana, Slovenia, EU in the first week of December (5th to 9th). The main two sprint topics are Pyramid 2.0 and Pyramid for Newcomers.


## Videos
* [List of videos from the official site](https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/misc/videos.html)
* [Online Video Courses at Talk Python Training](https://training.talkpython.fm/courses/all)
* [Web Applications with Python and the Pyramid
  Framework](http://shop.oreilly.com/product/0636920041900.do) -
  In this Web Applications with Python and the Pyramid Framework training
  course, expert author Paul Everitt will teach you about the features needed
  for Python web development, as well as Pyramid's unique features. This
  course is designed for users that already have a basic knowledge of Python.

  You will start by learning about single file web apps, templating, and
  multiple routes and views. From there, Paul will teach you about MyApp
  Python package, views and routes, and templating and static assets. This
  video tutorial also covers forms, databases, and sessions, authentication
  and authorization, and JSON. Finally, you will learn about extensibility,
  including custom configuration settings, extending and overriding, and
  custom view predicates.

  Once you have completed this computer based training course, you will have
  gained a basic understanding of the features needed for Python web
  development and the features unique to Pyramid.

## Who uses it?

* [Projects, Websites, Companies and Organizations that use
  Pyramid](https://trypyramid.com/community-powered-by-pyramid.html) - add your project to the list

# Contributing

Just fork and send a pull request with your awesome Pyramid apps, projects or
resources.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, @uralbash has waived all copyright and related
or neighboring rights to this work.
