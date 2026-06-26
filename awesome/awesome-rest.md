# REST

[![GitHub stars](https://img.shields.io/github/stars/marmelab/awesome-rest?style=flat)](https://github.com/marmelab/awesome-rest/stargazers)

# Awesome REST [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A collaborative list of great resources about RESTful API architecture, development, test, and performance. Feel free to contribute to this on-going list.

* [Design](#design)
  * [Guidelines](#guidelines)
* [Standards](#standards)
* [Clients](#clients)
  * [PHP](#php-clients)
  * [Client-side JavaScript](#javascript-clients)
  * [Node.js](#nodejs-clients)
  * [Ruby](#ruby-clients)
  * [Go](#go-clients)
  * [.Net](#net-clients)
  * [Generators](#generators)
* [Servers](#servers)
  * [Directly On Top Of A RMDB](#directly-on-top-of-a-rmdb)
  * [Node.js](#nodejs)
  * [PHP](#php)
  * [Symfony2](#symfony2)
  * [Python](#python)
  * [Ruby](#ruby)
  * [Go](#go)
  * [Java](#java)
  * [Haskell](#haskell)
* [Testing](#testing)
  * [Querying](#querying)
  * [Mocking](#mocking)
  * [Debugging Proxies](#debugging-proxies)
  * [Public REST APIs To Use In Tests](#public-rest-apis-to-use-in-tests)
* [Documentation](#documentation)
* [API Gateway](#api-gateway)
* [SaaS Tools](#saas-tools)
* [Miscellaneous](#miscellaneous)



## Design

* [Architectural Styles and the Design of Network-based Software Architectures](https://roy.gbiv.com/pubs/dissertation/top.htm) - Roy Fielding's dissertation defining REST
* [HTTP API design guide extracted from work on the Heroku Platform API](https://github.com/interagent/http-api-design) [![GitHub stars](https://img.shields.io/github/stars/interagent/http-api-design?style=flat)](https://github.com/interagent/http-api-design/stargazers)
* [Best Practices for Designing a Pragmatic RESTful API](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
* [How to design a REST API?](https://blog.octo.com/en/design-a-rest-api/) - Full guide tackling security, pagination, filtering, versioning, partial answers, CORS, etc.
* [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html) - Explained by Martin Fowler, originally presented by Leonard Richardson at the [QCon 2008](https://www.crummy.com/writing/speaking/2008-QCon/act3.html).
* [Enterprise Integration Using REST](https://martinfowler.com/articles/enterpriseREST.html) - Discusses the constraints and flexibility that you have with nonpublic APIs, and lessons learned from doing large scale RESTful integration across multiple teams.
* [HATEOAS](https://web.archive.org/web/20201111235328/timelessrepo.com/haters-gonna-hateoas) - Clear explanation on what HATEOAS is, and why you should use it.
* [How to GET a cup of coffee](https://www.infoq.com/articles/webber-rest-workflow/)
* [REST API Tutorial](https://www.restapitutorial.com/) - RestApiTutorial.com is dedicated to tracking REST API best practices and making resources available to enable quick reference and self education for the development crafts-person.
* [API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist) [![GitHub stars](https://img.shields.io/github/stars/shieldfy/API-Security-Checklist?style=flat)](https://github.com/shieldfy/API-Security-Checklist/stargazers) - Best practices about REST API security

### Guidelines

* [Adidas REST API Guidelines](https://github.com/adidas/api-guidelines/blob/master/rest-api-guidelines/rest.md) [![GitHub stars](https://img.shields.io/github/stars/adidas/api-guidelines/blob/master/rest-api-guidelines/rest.md?style=flat)](https://github.com/adidas/api-guidelines/blob/master/rest-api-guidelines/rest.md/stargazers) - Adidas REST API Guidelines define standards and guidelines for building REST APIs at adidas.
* [Atlassian REST API design guidelines version 1](https://developer.atlassian.com/server/framework/atlassian-sdk/atlassian-rest-api-design-guidelines-version-1/) - This document provides guidelines to Atlassian developers who are designing REST APIs for Atlassian applications.
* [Cisco REST API Guide](https://github.com/CiscoDevNet/api-design-guide) [![GitHub stars](https://img.shields.io/github/stars/CiscoDevNet/api-design-guide?style=flat)](https://github.com/CiscoDevNet/api-design-guide/stargazers) - Guidelines for designing REST APIs at Cisco.
* [Google Cloud API design guide](https://cloud.google.com/apis/design/) - Guidelines Google follows when designing Cloud APIs and other Google APIs (REST APIs and gRPC APIs).
* [Haufe API Style Guide](https://github.com/Haufe-Lexware/api-style-guide) [![GitHub stars](https://img.shields.io/github/stars/Haufe-Lexware/api-style-guide?style=flat)](https://github.com/Haufe-Lexware/api-style-guide/stargazers) - Guidelines created by Haufe-Lexware CTO team.
* [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/graph/GuidelinesGraph.md) [![GitHub stars](https://img.shields.io/github/stars/microsoft/api-guidelines/blob/vNext/graph/GuidelinesGraph.md?style=flat)](https://github.com/microsoft/api-guidelines/blob/vNext/graph/GuidelinesGraph.md/stargazers) - The Microsoft REST API Guidelines, as a design principle, encourages application developers to have resources accessible to them via a RESTful HTTP interface.
* [Restful API Guidelines by Zalando](https://github.com/zalando/restful-api-guidelines) [![GitHub stars](https://img.shields.io/github/stars/zalando/restful-api-guidelines?style=flat)](https://github.com/zalando/restful-api-guidelines/stargazers) - Developing Restful APIs: A Comprehensive Set of Guidelines.

## Standards

* [JSON API](https://jsonapi.org/) - Standard for building APIs in JSON.
* [RAML](https://raml.org/) - Simple and succinct way to describe RESTful API.
* [JSend](https://github.com/omniti-labs/jsend) [![GitHub stars](https://img.shields.io/github/stars/omniti-labs/jsend?style=flat)](https://github.com/omniti-labs/jsend/stargazers) - Simple specification that lays down some rules for how JSON responses from web servers should be formatted.
* [OData](https://www.odata.org/) - Open protocol to allow the creation and consumption of queryable and interoperable RESTful APIs. Quite complex.
* [HAL](https://tools.ietf.org/html/draft-kelly-json-hal-06) - Simple format that gives a consistent and easy way to hyperlink between resources in your API.
* [JSON-LD](https://json-ld.org/) - Standard for describing Linked Data and hypermedia relations in JSON (W3C).
* [Hydra](https://www.hydra-cg.com/) - Vocabulary for Hypermedia-Driven Web APIs (W3C).
* [Schema.org](https://schema.org) - Collection of schemas describing common data models.
* [OpenAPI](https://openapis.org/) - Formerly known as the Swagger Specification, OpenAPI specifcation is the world’s most popular description format for defining Restful APIs.

## Clients

### PHP Clients

* [Guzzle](https://guzzle.readthedocs.org/en/latest/) - HTTP client and framework for consuming RESTful web services.
* [Buzz](https://github.com/kriswallsmith/buzz) [![GitHub stars](https://img.shields.io/github/stars/kriswallsmith/buzz?style=flat)](https://github.com/kriswallsmith/buzz/stargazers) - Another lightweight HTTP client.
* [unirest for PHP](https://github.com/Mashape/unirest-php) [![GitHub stars](https://img.shields.io/github/stars/Mashape/unirest-php?style=flat)](https://github.com/Mashape/unirest-php/stargazers) - Simplified, lightweight HTTP client library.

### JavaScript Clients

* [restangular](https://github.com/mgonto/restangular) [![GitHub stars](https://img.shields.io/github/stars/mgonto/restangular?style=flat)](https://github.com/mgonto/restangular/stargazers) - AngularJS service to handle REST API properly and easily.
* [restful.js](https://github.com/marmelab/restful.js) [![GitHub stars](https://img.shields.io/github/stars/marmelab/restful.js?style=flat)](https://github.com/marmelab/restful.js/stargazers) - JS client for interacting with server-side RESTful resources.
* [traverson](https://github.com/basti1302/traverson) [![GitHub stars](https://img.shields.io/github/stars/basti1302/traverson?style=flat)](https://github.com/basti1302/traverson/stargazers) - A Hypermedia API/HATEOAS Client for Node.js and the Browser
* [raml-client-generator](https://github.com/mulesoft/raml-client-generator) [![GitHub stars](https://img.shields.io/github/stars/mulesoft/raml-client-generator?style=flat)](https://github.com/mulesoft/raml-client-generator/stargazers) - Generates static client libs for js.

### Node.js Clients

 * [restler](https://github.com/danwrong/restler) [![GitHub stars](https://img.shields.io/github/stars/danwrong/restler?style=flat)](https://github.com/danwrong/restler/stargazers) - REST client library for node.js.
 * [unirest for Node.js](https://github.com/Mashape/unirest-nodejs) [![GitHub stars](https://img.shields.io/github/stars/Mashape/unirest-nodejs?style=flat)](https://github.com/Mashape/unirest-nodejs/stargazers) - Simplified, lightweight HTTP client library.

### Ruby Clients

* [RESTClient](https://github.com/rest-client/rest-client) [![GitHub stars](https://img.shields.io/github/stars/rest-client/rest-client?style=flat)](https://github.com/rest-client/rest-client/stargazers) - Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions.
* [Spyke](https://github.com/balvig/spyke) [![GitHub stars](https://img.shields.io/github/stars/balvig/spyke?style=flat)](https://github.com/balvig/spyke/stargazers) - Interact with REST services in an ActiveRecord-like manner.
* [excon](https://github.com/excon/excon) [![GitHub stars](https://img.shields.io/github/stars/excon/excon?style=flat)](https://github.com/excon/excon/stargazers) - Usable, fast, simple Ruby HTTP 1.1. It works great as a general HTTP(s) client and is particularly well suited to usage in API clients.
* [httparty](https://github.com/jnunemaker/httparty) [![GitHub stars](https://img.shields.io/github/stars/jnunemaker/httparty?style=flat)](https://github.com/jnunemaker/httparty/stargazers) - Makes HTTP fun again!
* [Net::HTTP](https://ruby-doc.org/3.2.0/stdlibs/net/Net/HTTP.html) - Net::HTTP provides a rich library which can be used to build HTTP user-agents.
* [raml-ruby-client-generator](https://github.com/zlx/raml-ruby-client-generator) [![GitHub stars](https://img.shields.io/github/stars/zlx/raml-ruby-client-generator?style=flat)](https://github.com/zlx/raml-ruby-client-generator/stargazers) - Auto generate API client from a RAML file.

### Go Clients

* [gopencils](https://github.com/bndr/gopencils) [![GitHub stars](https://img.shields.io/github/stars/bndr/gopencils?style=flat)](https://github.com/bndr/gopencils/stargazers) - Small and simple package to easily consume REST APIs.
* [resty](https://github.com/go-resty/resty) [![GitHub stars](https://img.shields.io/github/stars/go-resty/resty?style=flat)](https://github.com/go-resty/resty/stargazers) - Simple HTTP and REST client for Go inspired by Ruby rest-client.

### .NET Clients

* [RestSharp](https://github.com/restsharp/RestSharp) [![GitHub stars](https://img.shields.io/github/stars/restsharp/RestSharp?style=flat)](https://github.com/restsharp/RestSharp/stargazers) - Simple REST and HTTP API client for .NET
* [Refit](https://github.com/reactiveui/refit) [![GitHub stars](https://img.shields.io/github/stars/reactiveui/refit?style=flat)](https://github.com/reactiveui/refit/stargazers) - The automatic type-safe REST library for Xamarin and .NET
* [Flurl](https://flurl.dev) - Fluent, portable, testable REST/HTTP client library
* [RestEase](https://github.com/canton7/RestEase) [![GitHub stars](https://img.shields.io/github/stars/canton7/RestEase?style=flat)](https://github.com/canton7/RestEase/stargazers) - Easy-to-use typesafe REST API client library, which is simple and customisable. Heavily inspired by Refit
* [Tiny.RestClient](https://github.com/jgiacomini/Tiny.RestClient) [![GitHub stars](https://img.shields.io/github/stars/jgiacomini/Tiny.RestClient?style=flat)](https://github.com/jgiacomini/Tiny.RestClient/stargazers) - Simpliest Fluent REST client for .NET.
* [RestLess](https://github.com/letsar/RestLess) [![GitHub stars](https://img.shields.io/github/stars/letsar/RestLess?style=flat)](https://github.com/letsar/RestLess/stargazers) - The automatic type-safe-reflectionless REST API client library for .Net Standard.
* [Apizr](https://github.com/Respawnsive/Apizr) [![GitHub stars](https://img.shields.io/github/stars/Respawnsive/Apizr?style=flat)](https://github.com/Respawnsive/Apizr/stargazers) - Refit-based web api client, but resilient (retry, connectivity, cache, auth, log, priority, etc...).

### Generators

* [openapi-generator](https://github.com/OpenAPITools/openapi-generator) [![GitHub stars](https://img.shields.io/github/stars/OpenAPITools/openapi-generator?style=flat)](https://github.com/OpenAPITools/openapi-generator/stargazers) - OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3).

## Servers

### Directly On Top Of A RMDB

* [postgrest](https://github.com/begriffs/postgrest) [![GitHub stars](https://img.shields.io/github/stars/begriffs/postgrest?style=flat)](https://github.com/begriffs/postgrest/stargazers) - Serve a fully RESTful API directly from an existing PostgreSQL database.
* [MySQL HTTP plugin](http://blog.ulf-wendel.de/2014/mysql-5-7-http-plugin-mysql/) - Simple REST-like / CRUD server for any MySQL database.
* [pREST](https://github.com/prest/prest) [![GitHub stars](https://img.shields.io/github/stars/prest/prest?style=flat)](https://github.com/prest/prest/stargazers) - A fully RESTful API from any existing PostgreSQL database written in Go.

### Node.js

* [node-restify](https://github.com/restify/node-restify) [![GitHub stars](https://img.shields.io/github/stars/restify/node-restify?style=flat)](https://github.com/restify/node-restify/stargazers) - Framework specifically meant for REST API.
* [Sails.js](https://sailsjs.org/) - Node.js Web framework embedding a command to generate automatically a REST API.
* [mers](https://github.com/jspears/mers) [![GitHub stars](https://img.shields.io/github/stars/jspears/mers?style=flat)](https://github.com/jspears/mers/stargazers) - Express service exposing Mongoose finders as RESTful API.
* [flatiron/resourceful](https://github.com/flatiron/resourceful) [![GitHub stars](https://img.shields.io/github/stars/flatiron/resourceful?style=flat)](https://github.com/flatiron/resourceful/stargazers) - Isomorphic Resource engine for JavaScript.
* [loopback](https://loopback.io/) - Powerful Node.js framework for creating APIs and easily connecting to backend data sources.
* [Feathers](https://feathersjs.com/) - is a real-time, micro-service web framework that gives you control over your data via RESTful resources, sockets and flexible plug-ins.
* [Expressa](https://github.com/thomas4019/expressa) [![GitHub stars](https://img.shields.io/github/stars/thomas4019/expressa?style=flat)](https://github.com/thomas4019/expressa/stargazers) - Express middleware for creating APIs from JSON schemas with a simple admin editor and permissions model.
* [rest-hapi](https://github.com/JKHeadley/rest-hapi) [![GitHub stars](https://img.shields.io/github/stars/JKHeadley/rest-hapi?style=flat)](https://github.com/JKHeadley/rest-hapi/stargazers) - Generate RESTful API based on mongoose models that supports relational data.
* [Nestjsx/crud](https://github.com/nestjsx/crud) [![GitHub stars](https://img.shields.io/github/stars/nestjsx/crud?style=flat)](https://github.com/nestjsx/crud/stargazers) - Generate CRUD controllers and services for RESTful API with NestJS and TypeORM.

### PHP

* [Microrest](https://github.com/marmelab/microrest.php) [![GitHub stars](https://img.shields.io/github/stars/marmelab/microrest.php?style=flat)](https://github.com/marmelab/microrest.php/stargazers) - Micro-web application providing a REST API on top of any relational database.
* [Negotiation](https://github.com/willdurand/Negotiation) [![GitHub stars](https://img.shields.io/github/stars/willdurand/Negotiation?style=flat)](https://github.com/willdurand/Negotiation/stargazers) - Content negotiation library.
* [Drest](https://github.com/leedavis81/drest) [![GitHub stars](https://img.shields.io/github/stars/leedavis81/drest?style=flat)](https://github.com/leedavis81/drest/stargazers) - Library for exposing Doctrine entities as REST resource endpoints.
* [Restler](https://github.com/Luracast/Restler) [![GitHub stars](https://img.shields.io/github/stars/Luracast/Restler?style=flat)](https://github.com/Luracast/Restler/stargazers) - Lightweight framework to expose PHP methods as RESTful web API.
* [HAL](https://github.com/blongden/hal) [![GitHub stars](https://img.shields.io/github/stars/blongden/hal?style=flat)](https://github.com/blongden/hal/stargazers) - Hypertext Application Language (HAL) builder library.
* [Apigility](https://github.com/zfcampus/zf-apigility-skeleton) [![GitHub stars](https://img.shields.io/github/stars/zfcampus/zf-apigility-skeleton?style=flat)](https://github.com/zfcampus/zf-apigility-skeleton/stargazers) - API builder built with Zend Framework 2.
* [phprest](https://github.com/phprest/phprest) [![GitHub stars](https://img.shields.io/github/stars/phprest/phprest?style=flat)](https://github.com/phprest/phprest/stargazers) - Specialized REST microframework for PHP.
* [Hateoas](https://github.com/willdurand/Hateoas) [![GitHub stars](https://img.shields.io/github/stars/willdurand/Hateoas?style=flat)](https://github.com/willdurand/Hateoas/stargazers) - PHP library to support implementing representations for HATEOAS REST web services.
* [Fusio](https://github.com/apioo/fusio) [![GitHub stars](https://img.shields.io/github/stars/apioo/fusio?style=flat)](https://github.com/apioo/fusio/stargazers) - Open source API management platform.

#### Symfony2

* [REST APIs with Symfony2: the Right Way](https://williamdurand.fr/2012/08/02/rest-apis-with-symfony2-the-right-way/) - Complete guide to build a state-of-the-art REST API with Symfony2 framework.
* [FOSRestBundle](https://github.com/FriendsOfSymfony/FOSRestBundle) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfSymfony/FOSRestBundle?style=flat)](https://github.com/FriendsOfSymfony/FOSRestBundle/stargazers) - Bundle handling view, routing, error handling, etc. for your REST API.
* [stanlemon/rest-bundle](https://github.com/stanlemon/rest-bundle) [![GitHub stars](https://img.shields.io/github/stars/stanlemon/rest-bundle?style=flat)](https://github.com/stanlemon/rest-bundle/stargazers) - Build a REST API based on Doctrine entities using conventions over configuration.
* [BazingaHateoasBundle](https://github.com/willdurand/BazingaHateoasBundle) [![GitHub stars](https://img.shields.io/github/stars/willdurand/BazingaHateoasBundle?style=flat)](https://github.com/willdurand/BazingaHateoasBundle/stargazers) - Integrate the [Hateoas](https://github.com/willdurand/Hateoas) [![GitHub stars](https://img.shields.io/github/stars/willdurand/Hateoas?style=flat)](https://github.com/willdurand/Hateoas/stargazers) library into a Symfony2 application.
* [Symfony REST Edition](https://github.com/gimler/symfony-rest-edition) [![GitHub stars](https://img.shields.io/github/stars/gimler/symfony-rest-edition?style=flat)](https://github.com/gimler/symfony-rest-edition/stargazers) - Start with a Symfony2 application with all REST-friendly bundles pre-configured.
* [NgAdminGeneratorBundle](https://github.com/marmelab/NgAdminGeneratorBundle) [![GitHub stars](https://img.shields.io/github/stars/marmelab/NgAdminGeneratorBundle?style=flat)](https://github.com/marmelab/NgAdminGeneratorBundle/stargazers) - Boostrap ng-admin configuration based on `stanlemon/rest-bundle`.
* [DunglasApiBundle](https://github.com/dunglas/DunglasApiBundle) [![GitHub stars](https://img.shields.io/github/stars/dunglas/DunglasApiBundle?style=flat)](https://github.com/dunglas/DunglasApiBundle/stargazers) - Build a REST API which follow Hydra/JSON-LD specification.
* [API Platform](https://github.com/api-platform/api-platform) [![GitHub stars](https://img.shields.io/github/stars/api-platform/api-platform?style=flat)](https://github.com/api-platform/api-platform/stargazers) - Specialize Symfony edition for the creation of hypermedia REST APIs.
* [NelmioApiDocBundle](https://github.com/nelmio/NelmioApiDocBundle) [![GitHub stars](https://img.shields.io/github/stars/nelmio/NelmioApiDocBundle?style=flat)](https://github.com/nelmio/NelmioApiDocBundle/stargazers) - Generate documentation for your REST API from annotations.

### PowerShell

* [Pode](https://github.com/Badgerati/Pode) [![GitHub stars](https://img.shields.io/github/stars/Badgerati/Pode?style=flat)](https://github.com/Badgerati/Pode/stargazers) - Pode is an cross-platform, open-source, community-supported web server and REST API framework for PowerShell developers

### Python

* [Django REST framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit that makes it easy to build Web APIs.
* [django-tastypie](http://tastypieapi.org/) - Creating delicious APIs for Django apps.
* [flask-restful](https://flask-restful.readthedocs.org/) - Extension for Flask that adds support for quickly building REST APIs.
* [flask-restless](https://flask-restless.readthedocs.org/en/latest/) - Flask extension for generating ReSTful APIs for database models defined with SQLAlchemy (or Flask-SQLAlchemy).
* [sandman](https://github.com/jeffknupp/sandman) [![GitHub stars](https://img.shields.io/github/stars/jeffknupp/sandman?style=flat)](https://github.com/jeffknupp/sandman/stargazers) - Automated REST APIs for existing database-driven systems.
* [restless](https://restless.readthedocs.org/en/latest/) - Framework agnostic REST framework based on lessons learned from TastyPie.
* [Python Eve](https://python-eve.org/) - Eve is an open source Python REST API framework designed for human beings. It allows to effortlessly build and deploy highly customizable, fully featured RESTful Web Services.
* [Ramses](https://ramses.readthedocs.org/en/stable/) - Makes RAML files executable by generating production-ready APIs from them at runtime.
* [Flask-Potion](https://github.com/biosustain/potion) [![GitHub stars](https://img.shields.io/github/stars/biosustain/potion?style=flat)](https://github.com/biosustain/potion/stargazers) - Flask-Potion is a powerful Flask extension for building RESTful JSON APIs. It also provides several Clients for easier access to the API.
* [apistar](https://github.com/encode/apistar) [![GitHub stars](https://img.shields.io/github/stars/encode/apistar?style=flat)](https://github.com/encode/apistar/stargazers) - A smart Web API framework, designed for Python 3. 
* [Falcon](https://github.com/falconry/falcon) [![GitHub stars](https://img.shields.io/github/stars/falconry/falcon?style=flat)](https://github.com/falconry/falcon/stargazers) - Falcon is a bare-metal Python web API framework for building high-performance microservices, app backends, and higher-level frameworks.
* [FastAPI](https://github.com/tiangolo/fastapi) [![GitHub stars](https://img.shields.io/github/stars/tiangolo/fastapi?style=flat)](https://github.com/tiangolo/fastapi/stargazers) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. With automatic API documentation using Swagger UI and ReDoc, based on OpenAPI and JSON Schema.
* [Zato](https://github.com/zatosource/zato/) [![GitHub stars](https://img.shields.io/github/stars/zatosource/zato/?style=flat)](https://github.com/zatosource/zato//stargazers) - Platform for building server-side integrations, automations and API backends in Python.

### Ruby

* [Grape](https://www.ruby-grape.org) - Opinionated micro-framework for creating REST-like APIs in Ruby.
* [Rails](https://guides.rubyonrails.org/api_app.html) - RailsGuides: Using Rails for API-only applications.

### Go

* [gocrud](https://github.com/manishrjain/gocrud) [![GitHub stars](https://img.shields.io/github/stars/manishrjain/gocrud?style=flat)](https://github.com/manishrjain/gocrud/stargazers): Go library to simplify creating, updating and deleting arbitrary depth structured data — to make building REST services fast and easy.
* [go-json-rest](https://github.com/ant0ine/go-json-rest) [![GitHub stars](https://img.shields.io/github/stars/ant0ine/go-json-rest?style=flat)](https://github.com/ant0ine/go-json-rest/stargazers) - Thin layer on top of `net/http` that helps building RESTful APIs easily.
* [sleepy](https://github.com/dougblack/sleepy) [![GitHub stars](https://img.shields.io/github/stars/dougblack/sleepy?style=flat)](https://github.com/dougblack/sleepy/stargazers) - RESTful micro-framework written in Go.
* [restit](https://github.com/yookoala/restit) [![GitHub stars](https://img.shields.io/github/stars/yookoala/restit?style=flat)](https://github.com/yookoala/restit/stargazers) - Go micro framework to help writing RESTful API integration test.
* [go-relax](https://github.com/codehack/go-relax) [![GitHub stars](https://img.shields.io/github/stars/codehack/go-relax?style=flat)](https://github.com/codehack/go-relax/stargazers) - Framework of pluggable components to build RESTful API's.
* [go-rest](https://github.com/ungerik/go-rest) [![GitHub stars](https://img.shields.io/github/stars/ungerik/go-rest?style=flat)](https://github.com/ungerik/go-rest/stargazers) - Small and evil REST framework for Go.
* [go-restful](https://github.com/emicklei/go-restful) [![GitHub stars](https://img.shields.io/github/stars/emicklei/go-restful?style=flat)](https://github.com/emicklei/go-restful/stargazers) - A declarative highly readable framework for building restful API's.
* [Resoursea](https://github.com/resoursea/api) [![GitHub stars](https://img.shields.io/github/stars/resoursea/api?style=flat)](https://github.com/resoursea/api/stargazers) - REST framework for quickly writing resource based services.

### Java

* [RestExpress](https://github.com/RestExpress/RestExpress) [![GitHub stars](https://img.shields.io/github/stars/RestExpress/RestExpress?style=flat)](https://github.com/RestExpress/RestExpress/stargazers) - Netty-based, highly performant, lightweight, container-less, plugin-extensible, framework that is ideal for microservice architectures.
* [Vertx-Web](https://github.com/vert-x3/vertx-web) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-web?style=flat)](https://github.com/vert-x3/vertx-web/stargazers) - Vert.x-Web is a set of building blocks for building web applications with Vert.x, a toolkit for building reactive applications on the JVM.
* [Dropwizard](https://github.com/dropwizard/dropwizard) [![GitHub stars](https://img.shields.io/github/stars/dropwizard/dropwizard?style=flat)](https://github.com/dropwizard/dropwizard/stargazers) - A framework for developing ops-friendly, high-performance, RESTful web services.

### Scala

* [Chaos](https://github.com/mesosphere/chaos) [![GitHub stars](https://img.shields.io/github/stars/mesosphere/chaos?style=flat)](https://github.com/mesosphere/chaos/stargazers) - A lightweight framework for writing REST services in Scala.


### Haskell
* [Rest for Haskell](https://github.com/silkapp/rest) [![GitHub stars](https://img.shields.io/github/stars/silkapp/rest?style=flat)](https://github.com/silkapp/rest/stargazers) - This package allows you to create REST APIs in Haskell. These APIs can be run in different web frameworks. They can also be used to automatically generate documentation as well as client libraries.

## Testing

### Querying

* [httpie](https://github.com/jkbrzt/httpie) [![GitHub stars](https://img.shields.io/github/stars/jkbrzt/httpie?style=flat)](https://github.com/jkbrzt/httpie/stargazers) - Command line HTTP client, far more dev-friendly than `curl`.
* [resty](https://github.com/micha/resty) [![GitHub stars](https://img.shields.io/github/stars/micha/resty?style=flat)](https://github.com/micha/resty/stargazers) - Little command line REST client that you can use in pipelines (bash or zsh).
* [jq](https://github.com/stedolan/jq) [![GitHub stars](https://img.shields.io/github/stars/stedolan/jq?style=flat)](https://github.com/stedolan/jq/stargazers) - Command line JSON processor, to use in combination with a command-line HTTP client like cURL.
* [HttpMaster](https://www.httpmaster.net) - GUI tool for testing REST APIs and services. Windows OS only.
* [Http-console](https://github.com/cloudhead/http-console) [![GitHub stars](https://img.shields.io/github/stars/cloudhead/http-console?style=flat)](https://github.com/cloudhead/http-console/stargazers) - Command line interface for HTTP that let you *speak HTTP like a local*
* [HTTP Prompt](https://github.com/eliangcs/http-prompt) [![GitHub stars](https://img.shields.io/github/stars/eliangcs/http-prompt?style=flat)](https://github.com/eliangcs/http-prompt/stargazers) - HTTP Prompt is an interactive command-line HTTP client featuring autocomplete and syntax highlighting, built on HTTPie and prompt_toolkit.
* [rest-assured](https://github.com/rest-assured/rest-assured) [![GitHub stars](https://img.shields.io/github/stars/rest-assured/rest-assured?style=flat)](https://github.com/rest-assured/rest-assured/stargazers) - Java DSL for easy testing of REST services.
* [Insomnia](https://github.com/getinsomnia/insomnia) [![GitHub stars](https://img.shields.io/github/stars/getinsomnia/insomnia?style=flat)](https://github.com/getinsomnia/insomnia/stargazers) - Cross-platform HTTP and GraphQL Client
* [ExtendsClass](https://extendsclass.com/rest-client-online.html) - Make HTTP requests with a simple web-based HTTP client.
* [TestMace](https://testmace.com) - Cross-platform simple but powerful IDE for API automation testing.
* [Milkman](https://github.com/warmuuh/milkman) [![GitHub stars](https://img.shields.io/github/stars/warmuuh/milkman?style=flat)](https://github.com/warmuuh/milkman/stargazers) - Extensible cross-platform request/response workbench, not only for http calls.
* [Schemathesis](https://github.com/schemathesis/schemathesis) [![GitHub stars](https://img.shields.io/github/stars/schemathesis/schemathesis?style=flat)](https://github.com/schemathesis/schemathesis/stargazers) - Property-based testing tool for web applications built with Open API and GraphQL specifications.
* [Step CI](https://github.com/stepci/stepci) [![GitHub stars](https://img.shields.io/github/stars/stepci/stepci?style=flat)](https://github.com/stepci/stepci/stargazers) - Open-source framework for API Quality Assurance, which tests REST, GraphQL and gRPC automated and from Open API spec.
* [RestQA](https://github.com/restqa/restqa) [![GitHub stars](https://img.shields.io/github/stars/restqa/restqa?style=flat)](https://github.com/restqa/restqa/stargazers) - A REST API testing Framework based on BDD / Gherkin to manage microservice local testing.
* [Postman](https://www.postman.com/) - Cross-platform API development and testing platform.
* [SoapUI](https://www.soapui.org/) - Cross-platform API testing tool for REST and SOAP APIs.
* [RapidAPI](https://paw.cloud/) - Full-featured HTTP client for macOS.

### Mocking

* [FakeRest](https://github.com/marmelab/FakeRest) [![GitHub stars](https://img.shields.io/github/stars/marmelab/FakeRest?style=flat)](https://github.com/marmelab/FakeRest/stargazers) - Redirect fetch() calls to a client-side fake REST API.
* [json-server](https://github.com/typicode/json-server) [![GitHub stars](https://img.shields.io/github/stars/typicode/json-server?style=flat)](https://github.com/typicode/json-server/stargazers) - Serve a REST API from fixture files using quick prototyping.
* [RequestBin](https://requestbin.com/) - Inspect and debug webhook requests sent by your clients or third-party APIs.
* [httpbin](https://httpbin.org) - HTTP request and response service - a/k/a Swiss Army Knife for HTTP.
* [MockServer](https://www.mock-server.com/) - Easy mocking of any system you integrate with via HTTP or HTTPS.
* [Request Baskets](https://github.com/darklynx/request-baskets) [![GitHub stars](https://img.shields.io/github/stars/darklynx/request-baskets?style=flat)](https://github.com/darklynx/request-baskets/stargazers) - Service to collect HTTP requests and inspect them via RESTful API or web UI.
* [DuckRails](https://github.com/iridakos/duckrails) [![GitHub stars](https://img.shields.io/github/stars/iridakos/duckrails?style=flat)](https://github.com/iridakos/duckrails/stargazers) - Mock quickly & dynamically API endpoints.
* [Mockoon](https://mockoon.com) - Easily create mock APIs locally. No remote deployment, no account required, open source.
* [Mockintosh](https://mockintosh.io/) - A mock server generator that's capable to generate RESTful APIs and communicate with the message queues to mimick asynchronous tasks.
* [Mockae](https://mockae.com/) - Fake REST API powered by Lua.

### Debugging Proxies

* [mitmproxy](https://mitmproxy.org/) - Free, open-source interactive HTTPS proxy for debugging API traffic.
* [Charles](https://www.charlesproxy.com/) - HTTP proxy/monitor for inspecting API traffic on Windows, Mac, and Linux.
* [Fiddler](https://www.telerik.com/fiddler) - Web debugging proxy tool by Telerik/Progress.

### Validating

* [JSON Schema](http://json-schema.org/) - Declarative language that allows you to annotate and validate JSON documents

### Public REST APIs To Use In Tests

* [Public APIs](https://publicapis.dev/) - The world's largest directory of public APIs.
* [APIs.guru](https://APIs.guru) - Wikipedia for Web APIs, each API has OpenAPI/Swagger description.
* [JSON Placeholder](https://jsonplaceholder.typicode.com/) - Fake REST API abput posts, users and comments

## Documentation

* [Swagger](https://swagger.io/) - Documentation/querying web interface for REST APIs.
* [API doc](https://apidocjs.com/) - Inline Documentation for RESTful web APIs.
* [raml2html](https://github.com/raml2html/raml2html) [![GitHub stars](https://img.shields.io/github/stars/raml2html/raml2html?style=flat)](https://github.com/raml2html/raml2html/stargazers) - Generates HTML documentation from a RAML file.
* [ReDoc](https://github.com/Rebilly/ReDoc/) [![GitHub stars](https://img.shields.io/github/stars/Rebilly/ReDoc/?style=flat)](https://github.com/Rebilly/ReDoc//stargazers) - OpenAPI/Swagger-powered three-panel documentation.
* [Slate](https://github.com/lord/slate) [![GitHub stars](https://img.shields.io/github/stars/lord/slate?style=flat)](https://github.com/lord/slate/stargazers) - Beautiful and responsive three-panel API documentation using Middleman.
* [Optic](https://github.com/opticdev/optic) [![GitHub stars](https://img.shields.io/github/stars/opticdev/optic?style=flat)](https://github.com/opticdev/optic/stargazers) - Maintain an accurate API specification without writing OpenAPI/Swagger. Works with any Stack
* [Zudoku](https://zudoku.dev/) - Create clean, consistent API docs with Zudoku — open source, extensible, and developer-first
* [Sourcey](https://sourcey.com) - Open source documentation platform for OpenAPI specs and markdown. Static HTML output.
* [Stoplight](https://stoplight.io/) - Design-first API platform with visual OpenAPI editor, documentation, and mocking.

## API Gateway

* [Kong](https://github.com/Kong/kong) [![GitHub stars](https://img.shields.io/github/stars/Kong/kong?style=flat)](https://github.com/Kong/kong/stargazers) - Scalable, distributed, and plugin oriented API gateway backed by Nginx.
* [Tyk API Gateway](https://github.com/TykTechnologies/tyk) [![GitHub stars](https://img.shields.io/github/stars/TykTechnologies/tyk?style=flat)](https://github.com/TykTechnologies/tyk/stargazers) - Lightweight API gateway with analytics logging, written in Go.
* [API Umbrella](https://github.com/NREL/api-umbrella) [![GitHub stars](https://img.shields.io/github/stars/NREL/api-umbrella?style=flat)](https://github.com/NREL/api-umbrella/stargazers) - API management platform for exposing web services, with web interface and analytics, written in Lua.
* [WSO2 API Management](https://github.com/wso2/product-apim) [![GitHub stars](https://img.shields.io/github/stars/wso2/product-apim?style=flat)](https://github.com/wso2/product-apim/stargazers) - API management tool with lightweight gateway and API lifecycle management, written in Java.
* [Express Gateway](https://github.com/ExpressGateway/express-gateway) [![GitHub stars](https://img.shields.io/github/stars/ExpressGateway/express-gateway?style=flat)](https://github.com/ExpressGateway/express-gateway/stargazers) - Microservices API Gateway built on top of ExpressJS (Node.js).
* [Lura](https://github.com/luraproject/lura) [![GitHub stars](https://img.shields.io/github/stars/luraproject/lura?style=flat)](https://github.com/luraproject/lura/stargazers) - Ultra performant API Gateway with middleware. Written in Go.
* [AWS API Gateway](https://aws.amazon.com/api-gateway/) - Fully managed service that helps developers to create, publish, maintain, monitor, and secure APIs at any scale.
* [Zuplo](https://zuplo.com/) - OpenAPI-Powered API & MCP Management platform for Security, Deployment, and Documentation. Add auth, rate-limiting, and monetization to your API or MCP Server in minutes, written in TypeScript & Go.

## SaaS Tools

* [Nango](https://github.com/NangoHQ/nango) [![GitHub stars](https://img.shields.io/github/stars/NangoHQ/nango?style=flat)](https://github.com/NangoHQ/nango/stargazers) - Native integrations framework to consume REST APIs (open-source).
* [Runscope](https://www.runscope.com/) - Automated API Monitoring & Testing.
* [Keploy](https://keploy.io) - Open-source API testing and data mocking tool that generates test cases and stubs automatically from real traffic, enabling end-to-end API testing and monitoring.
* [Ping-API](https://ping-api.com/) - Automated API Monitoring & Testing.
* [Apiary](https://apiary.io/) - Collaborative design, instant API mock, generated documentation, integrated code samples, debugging and automated testing.
* [Amazon API Gateway](https://aws.amazon.com/api-gateway/) - Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
* [Apigee](https://apigee.com) - Apigee is the leading provider of API technology and services for enterprises and developers.
* [3scale](https://www.3scale.net/) - Nginx based API gateway to integrate internal and external API services with 3scale's API Management Platform.
* [Assertible](https://assertible.com) - Continuously test and monitor your APIs after deployments and across environments.
* [Moesif](https://www.moesif.com) - API Analytics for Debugging, Monitoring, and Usage Tracking for RESTful and GraphQL.
* [Beeceptor](https://beeceptor.com/) - An HTTP inspecting, mocking and proxing service. Gives named endpoints for creating mock API endpoints and simulate responses.
* [Apitally](https://apitally.io) - Analytics, request logging and monitoring for REST APIs with a focus on simplicity and data privacy.
* [BlazeMeter](https://www.blazemeter.com/) - Continuous testing platform for API performance and load testing at scale.
* [Loader.io](https://loader.io/) - Free cloud-based load testing service for APIs.

## Miscellaneous

* [shadcn-admin-kit](https://github.com/marmelab/shadcn-admin-kit) [![GitHub stars](https://img.shields.io/github/stars/marmelab/shadcn-admin-kit?style=flat)](https://github.com/marmelab/shadcn-admin-kit/stargazers) - Build internal tools, admin panels, B2B apps, and dashboards on top of any REST API
* [react-admin](https://github.com/marmelab/react-admin) [![GitHub stars](https://img.shields.io/github/stars/marmelab/react-admin?style=flat)](https://github.com/marmelab/react-admin/stargazers) - Add a ReactJS admin GUI to any RESTful API.
* [ng-admin](https://github.com/marmelab/ng-admin) [![GitHub stars](https://img.shields.io/github/stars/marmelab/ng-admin?style=flat)](https://github.com/marmelab/ng-admin/stargazers) - Add an AngularJS admin GUI to any RESTful API.
* [swagger-codegen](https://github.com/swagger-api/swagger-codegen) [![GitHub stars](https://img.shields.io/github/stars/swagger-api/swagger-codegen?style=flat)](https://github.com/swagger-api/swagger-codegen/stargazers) - Auto generation of client libraries or server stubs given an OpenAPI specification (formerly known as the Swagger Specification).
* [Linx](https://linx.software) - Low-code API platform. Build, debug and host REST APIs 


## License

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
