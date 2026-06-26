# Groovy

[![GitHub stars](https://img.shields.io/github/stars/kdabir/awesome-groovy?style=flat)](https://github.com/kdabir/awesome-groovy/stargazers)

Awesome Groovy [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
==============

Curated list of awesome groovy libraries, frameworks and resources. Inspired by many other awesome-* repositories.

- [Awesome Groovy](#awesome-groovy)
    - [Build Tools, Setup and CI](#build-tools-setup-and-ci)
    - [Concurrency](#concurrency)
    - [Database](#database)
    - [Desktop App Frameworks](#rich-applications)
    - [HTTP](#http)
    - [IDE and Editor Support](#ide-and-editor-support)
    - [Testing](#testing)
    - [Code analysis](#code-analysis)
    - [Web Frameworks](#web-frameworks)
    - [Transpilers](#transpilers)
    - [Static Web](#static-web)
    - [Language Utilities](#language-utilities)
    - [File System Utilities](#file-system-utilities)
    - [File Format DSL](#file-format-dsl)
    - [Scripting Tools](#scripting-tools)
    - [Rule Engines](#rule-engines)
- [Resources](#resources)
- [Contributing](#contributing)
- [Credits](#credits)

## Build tools, setup and CI
* [Gradle](https://www.gradle.org/) - A powerful build system for the JVM
* [GMavenPlus](https://github.com/groovy/GMavenPlus) [![GitHub stars](https://img.shields.io/github/stars/groovy/GMavenPlus?style=flat)](https://github.com/groovy/GMavenPlus/stargazers) - A rewrite of GMaven, a Maven plugin for Groovy
* [SDKMAN](https://sdkman.io) - The Software Development Kit Manager (Previously known as GVM)
* [skeletal](https://github.com/cbmarcum/skeletal) [![GitHub stars](https://img.shields.io/github/stars/cbmarcum/skeletal?style=flat)](https://github.com/cbmarcum/skeletal/stargazers) - A simple project creation tool that uses packaged templates (successor of Lazybones)
* [Lazybones](https://github.com/pledbrook/lazybones) [![GitHub stars](https://img.shields.io/github/stars/pledbrook/lazybones?style=flat)](https://github.com/pledbrook/lazybones/stargazers) - A simple project creation tool that uses packaged project templates.
* [Jenkins job-dsl-plugin](https://github.com/jenkinsci/job-dsl-plugin) [![GitHub stars](https://img.shields.io/github/stars/jenkinsci/job-dsl-plugin?style=flat)](https://github.com/jenkinsci/job-dsl-plugin/stargazers) - A Groovy DSL for Jenkins Jobs
* [travis-groovy](https://github.com/kdabir/travis-groovy) [![GitHub stars](https://img.shields.io/github/stars/kdabir/travis-groovy?style=flat)](https://github.com/kdabir/travis-groovy/stargazers) - execute groovy scripts on travis-ci
* [Android Groovy Shell](https://play.google.com/store/apps/details?id=com.tambapps.android.grooidshell) - code and execute groovy scripts directly on your smartphone

## IDE and Editor Support
* [IntelliJ IDEA](http://www.jetbrains.com/idea/) - The Most Intelligent IDE for the Java Platform
* [Groovy Grails Tool Suite](https://marketplace.eclipse.org/content/groovygrails-tool-suite-ggts-eclipse) -  Eclipse-based IDE optimized for developing, debugging and executing Groovy and Grails applications
* [Groovy Web Console](http://groovyconsole.appspot.com) - The online Groovy console
* [LightTable Plugin](https://github.com/rundis/LightTable-Groovy) [![GitHub stars](https://img.shields.io/github/stars/rundis/LightTable-Groovy?style=flat)](https://github.com/rundis/LightTable-Groovy/stargazers) - LightTable Support
* [SpaceVim](https://spacevim.org/layers/lang/groovy/) - SpaceVim `lang#groovy` layer
* [Sublime Text 2/3](https://gist.github.com/kdabir/2203530) - Run groovy scripts from Sublime Text

## Web Frameworks

* [Grails](https://github.com/grails/grails) [![GitHub stars](https://img.shields.io/github/stars/grails/grails?style=flat)](https://github.com/grails/grails/stargazers) - A powerful web application framework based on the Groovy language
* [Micronaut](http://micronaut.io/) - A brand new microservices framework created by the Grails team
* [Spring-Boot](https://projects.spring.io/spring-boot) - Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that can you can "just run". Use Groovy as your coding language.
* [Gaelyk](https://github.com/gaelyk/gaelyk) [![GitHub stars](https://img.shields.io/github/stars/gaelyk/gaelyk?style=flat)](https://github.com/gaelyk/gaelyk/stargazers) - A lightweight Groovy toolkit for Google App Engine Java
* [Glide](https://github.com/kdabir/glide) [![GitHub stars](https://img.shields.io/github/stars/kdabir/glide?style=flat)](https://github.com/kdabir/glide/stargazers) - Create awesome apps on Google App Engine in a snap
* [Ratpack](https://github.com/ratpack/ratpack) [![GitHub stars](https://img.shields.io/github/stars/ratpack/ratpack?style=flat)](https://github.com/ratpack/ratpack/stargazers) - A toolkit for JVM web applications
* [gServ](https://github.com/javaConductor/gserv) [![GitHub stars](https://img.shields.io/github/stars/javaConductor/gserv?style=flat)](https://github.com/javaConductor/gserv/stargazers) - A Groovy toolkit for creating SPAs and REST based micro-services without the need for a container (Tomcat, JBoss, etc.).

## Database
* [GORM](https://gorm.grails.org) - Grails ORM, but can be used stand-alone without Grails
* [Gmongo](https://github.com/poiati/gmongo) [![GitHub stars](https://img.shields.io/github/stars/poiati/gmongo?style=flat)](https://github.com/poiati/gmongo/stargazers) - A Groovy wrapper to the mongodb Java driver
* [Gstorm](https://github.com/kdabir/gstorm) [![GitHub stars](https://img.shields.io/github/stars/kdabir/gstorm?style=flat)](https://github.com/kdabir/gstorm/stargazers) - A simple ORM for simple databases and CSV files to be used in groovy scripts
* [Tayra](https://github.com/EqualExperts/Tayra) [![GitHub stars](https://img.shields.io/github/stars/EqualExperts/Tayra?style=flat)](https://github.com/EqualExperts/Tayra/stargazers) - Incremental backup tool for MongoDB
* [Groovy-liquibase](https://github.com/tlberglund/groovy-liquibase) [![GitHub stars](https://img.shields.io/github/stars/tlberglund/groovy-liquibase?style=flat)](https://github.com/tlberglund/groovy-liquibase/stargazers) - Yet Another Groovy DSL for Liquibase
* [Effigy](https://github.com/cjstehno/effigy) [![GitHub stars](https://img.shields.io/github/stars/cjstehno/effigy?style=flat)](https://github.com/cjstehno/effigy/stargazers) - Groovy annotation-driven JDBC row mapping framework (abandoned)
* [elasticsearch-groovy](https://github.com/elastic/elasticsearch-groovy) [![GitHub stars](https://img.shields.io/github/stars/elastic/elasticsearch-groovy?style=flat)](https://github.com/elastic/elasticsearch-groovy/stargazers) - Elasticsearch Groovy client

## Rich Application

* [Griffon](http://griffon-framework.org/) - Griffon is an application framework for developing desktop applications in the JVM
* [GroovyFx](http://groovyfx.org/) - GroovyFX provides a Groovy binding for JavaFX 2.0.

## HTTP
* [Http-Builder](https://github.com/jgritman/httpbuilder) [![GitHub stars](https://img.shields.io/github/stars/jgritman/httpbuilder?style=flat)](https://github.com/jgritman/httpbuilder/stargazers) - HTTPBuilder is the easiest way to manipulate HTTP-based resources from the JVM
* [HTTP Builder NG](https://github.com/http-builder-ng/http-builder-ng) [![GitHub stars](https://img.shields.io/github/stars/http-builder-ng/http-builder-ng?style=flat)](https://github.com/http-builder-ng/http-builder-ng/stargazers) - HTTP Builder NG is a modern Groovy DSL for making http requests.
* [HTTP Builder NG Gradle Plugin](https://github.com/http-builder-ng/gradle-http-plugin) [![GitHub stars](https://img.shields.io/github/stars/http-builder-ng/gradle-http-plugin?style=flat)](https://github.com/http-builder-ng/gradle-http-plugin/stargazers) - Gradle plugin providing HTTP Builder NG support in a Gradle build configuration.
* [AsyncRestClient](https://github.com/eginez/AsyncRestClient) [![GitHub stars](https://img.shields.io/github/stars/eginez/AsyncRestClient?style=flat)](https://github.com/eginez/AsyncRestClient/stargazers) - Combine the power of RESTClient with RxGroovy for async http calls
* [Groovy-wslite](https://github.com/jwagenleitner/groovy-wslite) [![GitHub stars](https://img.shields.io/github/stars/jwagenleitner/groovy-wslite?style=flat)](https://github.com/jwagenleitner/groovy-wslite/stargazers) - Lightweight SOAP and REST webservice clients for Groovy
* [Hyperpoet](https://github.com/tambapps/hyperpoet) [![GitHub stars](https://img.shields.io/github/stars/tambapps/hyperpoet?style=flat)](https://github.com/tambapps/hyperpoet/stargazers) - Easy-to-use and customizable HTTP client for Groovy

## Testing
* [Spock](https://github.com/spockframework/spock) [![GitHub stars](https://img.shields.io/github/stars/spockframework/spock?style=flat)](https://github.com/spockframework/spock/stargazers) - The Enterprise-ready testing and specification framework.
* [Geb](https://github.com/geb/geb) [![GitHub stars](https://img.shields.io/github/stars/geb/geb?style=flat)](https://github.com/geb/geb/stargazers) - Very Groovy Browser Automation
* [Betamax](https://github.com/betamaxteam/betamax) [![GitHub stars](https://img.shields.io/github/stars/betamaxteam/betamax?style=flat)](https://github.com/betamaxteam/betamax/stargazers) - Betamax is a tool for mocking external HTTP resources such as web services and REST APIs in your tests.
* [HTTP Mock Server](https://github.com/TouK/http-mock-server) [![GitHub stars](https://img.shields.io/github/stars/TouK/http-mock-server?style=flat)](https://github.com/TouK/http-mock-server/stargazers) - HTTP Mock Server allows to mock HTTP request using groovy closures.
* [Ersatz Mock Server](https://github.com/cjstehno/ersatz) [![GitHub stars](https://img.shields.io/github/stars/cjstehno/ersatz?style=flat)](https://github.com/cjstehno/ersatz/stargazers) - A simple and expressive simulated HTTP server for testing client code with configurable responses.
* [Dru](https://agorapulse.github.io/dru/) - Data Reconstruction Utility loads data from external sources JSON, YML for easy testing GORM, DynamoDB or just plain POJOs.
* [Gru](https://agorapulse.github.io/gru/) - Groovy HTTP Testing Framework for running integration and semi-ingetration tests for any HTTP backend with native unit test support for Grails and Spring MVC.

## Concurrency
* [GPars](https://github.com/GPars/GPars) [![GitHub stars](https://img.shields.io/github/stars/GPars/GPars?style=flat)](https://github.com/GPars/GPars/stargazers) - The GPars concurrency and parallelism framework for the JVM
* [RxGroovy](https://github.com/ReactiveX/RxGroovy) [![GitHub stars](https://img.shields.io/github/stars/ReactiveX/RxGroovy?style=flat)](https://github.com/ReactiveX/RxGroovy/stargazers) - RxJava bindings for Groovy
* [Vertx](https://vertx.io/) - Vert.x is a lightweight, high performance application platform for the JVM

## Code Analysis
* [CodeNarc](http://codenarc.sourceforge.net/) - Static analysis tool for Groovy
* [Sonar-Groovy](https://github.com/pmayweg/sonar-groovy) [![GitHub stars](https://img.shields.io/github/stars/pmayweg/sonar-groovy?style=flat)](https://github.com/pmayweg/sonar-groovy/stargazers) - SonarQube Groovy plugin

## Transpilers
* [Grooscript](https://github.com/chiquitinxx/grooscript) [![GitHub stars](https://img.shields.io/github/stars/chiquitinxx/grooscript?style=flat)](https://github.com/chiquitinxx/grooscript/stargazers) - Converts your Groovy code to Javascript

## Static Web
* [Grain](https://github.com/sysgears/grain) [![GitHub stars](https://img.shields.io/github/stars/sysgears/grain?style=flat)](https://github.com/sysgears/grain/stargazers) - Static Web Site Building Framework For Groovy
* [Gaiden](https://github.com/kobo/gaiden) [![GitHub stars](https://img.shields.io/github/stars/kobo/gaiden?style=flat)](https://github.com/kobo/gaiden/stargazers) - Gaiden is a tool that makes it easy to create documentation with Markdown.

## Language Utilities
* [Functionalgroovy](https://github.com/mperry/functionalgroovy) [![GitHub stars](https://img.shields.io/github/stars/mperry/functionalgroovy?style=flat)](https://github.com/mperry/functionalgroovy/stargazers) - Functional programming in Groovy
* [Groovy-stream](https://github.com/timyates/groovy-stream) [![GitHub stars](https://img.shields.io/github/stars/timyates/groovy-stream?style=flat)](https://github.com/timyates/groovy-stream/stargazers) - A collection of classes to give a fluent builder for Streams (Lazy Groovy Generators)
* [Flipside](https://github.com/johnnywey/flipside) [![GitHub stars](https://img.shields.io/github/stars/johnnywey/flipside?style=flat)](https://github.com/johnnywey/flipside/stargazers) - Simple Groovy options library
* [groovy-common-extensions](https://github.com/timyates/groovy-common-extensions) [![GitHub stars](https://img.shields.io/github/stars/timyates/groovy-common-extensions?style=flat)](https://github.com/timyates/groovy-common-extensions/stargazers) - Lets you add things commonly useful to the Groovy language via the extension system
* [groovy-extra-list-behaviour](https://github.com/dnahodil/groovy-extra-list-behaviour) [![GitHub stars](https://img.shields.io/github/stars/dnahodil/groovy-extra-list-behaviour?style=flat)](https://github.com/dnahodil/groovy-extra-list-behaviour/stargazers) - Adds extra methods to Lists via the extension system
* [GPerfUtils](https://github.com/gperfutils) [![GitHub stars](https://img.shields.io/github/stars/gperfutils?style=flat)](https://github.com/gperfutils/stargazers) - Groovy-based tools verifying performance of your code
  * [gprof](https://github.com/gperfutils/gprof) [![GitHub stars](https://img.shields.io/github/stars/gperfutils/gprof?style=flat)](https://github.com/gperfutils/gprof/stargazers) - The profiling module for Groovy
  * [gbench](https://github.com/gperfutils/gbench) [![GitHub stars](https://img.shields.io/github/stars/gperfutils/gbench?style=flat)](https://github.com/gperfutils/gbench/stargazers) - The benchmarking module for Groovy
* [Fuzzy-CSV](https://github.com/kayr/fuzzy-csv) [![GitHub stars](https://img.shields.io/github/stars/kayr/fuzzy-csv?style=flat)](https://github.com/kayr/fuzzy-csv/stargazers) - Simple lightweight data processing library, useful for shaping/processing your tabular data before its consumed by another service or library.

## Data Processing
* [Nextflow](https://www.nextflow.io/) - Groovy DSL for Data-driven computational pipelines

## File System Utilities
* [Groovy-Vfs](https://github.com/ysb33r/groovy-vfs) [![GitHub stars](https://img.shields.io/github/stars/ysb33r/groovy-vfs?style=flat)](https://github.com/ysb33r/groovy-vfs/stargazers) - A DSL for Groovy on top of Apache VFS2
* [Directree](https://github.com/kdabir/directree) [![GitHub stars](https://img.shields.io/github/stars/kdabir/directree?style=flat)](https://github.com/kdabir/directree/stargazers) - A Simple DSL to create Directory Tree with Text Files

## DSLs
* [document-builder](https://github.com/craigburke/document-builder) [![GitHub stars](https://img.shields.io/github/stars/craigburke/document-builder?style=flat)](https://github.com/craigburke/document-builder/stargazers) - A document builder for Groovy for PDF or Word documents.
* [spreadsheet-builder](http://spreadsheet.dsl.builders/) - Spreadsheet builder provides convenient way how to create MS Excel OfficeOpenXML Documents (XSLX)
* [GroovyCSV](http://xlson.com/groovycsv/) - A simple CSV parsing library for groovy
* [Groogle](https://groogle.gitlab.io/groogle/latest/index.html) - A Groovy DSL written to use Google services APIs.

## Scripting Tools
* [EasyDokkaPlugin](https://github.com/Vorlonsoft/EasyDokkaPlugin) [![GitHub stars](https://img.shields.io/github/stars/Vorlonsoft/EasyDokkaPlugin?style=flat)](https://github.com/Vorlonsoft/EasyDokkaPlugin/stargazers) - Gradle script plugin to generate documentation by Dokka documentation engine for Java and Kotlin
* [GradleMavenPush](https://github.com/Vorlonsoft/GradleMavenPush) [![GitHub stars](https://img.shields.io/github/stars/Vorlonsoft/GradleMavenPush?style=flat)](https://github.com/Vorlonsoft/GradleMavenPush/stargazers) - Gradle script plugin to upload Gradle Artifacts to Maven repositories
* [picocli](https://github.com/remkop/picocli) [![GitHub stars](https://img.shields.io/github/stars/remkop/picocli?style=flat)](https://github.com/remkop/picocli/stargazers) - Parser library and framework for CLI. Usage help with ANSI colors. Autocomplete. Nested subcommands and more.
* [sshoogr](https://github.com/aestasit/sshoogr) [![GitHub stars](https://img.shields.io/github/stars/aestasit/sshoogr?style=flat)](https://github.com/aestasit/sshoogr/stargazers) - DSL library for working with remote servers through SSH.


## Rule Engines
* [grules](https://github.com/zhaber/grules) [![GitHub stars](https://img.shields.io/github/stars/zhaber/grules?style=flat)](https://github.com/zhaber/grules/stargazers) - rule engine for data preprocessing
* [n-cube](https://github.com/jdereg/n-cube) [![GitHub stars](https://img.shields.io/github/stars/jdereg/n-cube?style=flat)](https://github.com/jdereg/n-cube/stargazers) - a Rules Engine, Decision Table, Decision Tree, Templating Engine, and Enterprise Spreadsheet, built as a hyper-space.

# Resources

## Official Resources
* [The official groovy home](http://www.groovy-lang.org/) - Groovy's new home
* [Groovy's source](https://github.com/apache/groovy) [![GitHub stars](https://img.shields.io/github/stars/apache/groovy?style=flat)](https://github.com/apache/groovy/stargazers) - Groovy's source code mirrored on Github
* [Groovy mailing lists](http://www.groovy-lang.org/mailing-lists.html) - Note the new mailing list
* [Official Documentation](http://www.groovy-lang.org/documentation.html) - the definitive source of groovy documentation

## Try Groovy in Browser
* [Groovy Web Console](https://gwc-experiment.appspot.com/)
* [Groovy Playground](https://groovy-playground.appspot.com/)

## Groovy Code Examples
* [MrHaKi's Goodness](http://mrhaki.blogspot.com/) - Look out for entries titled "Groovy Goodness" , "Grails Goodness", Gradle Goodness"
* [PLEAC Groovy](http://pleac.sourceforge.net/pleac_groovy/) - Groovy is one of the 3 languages out of 32, having completed 100% of PLEAC examples.

## Staying up to date
* [Groovy Calamari](http://groovycalamari.com/) - Weekly curated publication about the Groovy Ecosystem
* [Groovy Weekly](http://glaforge.appspot.com/category/Groovy%20Weekly) - Groovy weekly newsletter
* [Grails Diary](https://grydeske.dk/news/index) - Particulary useful for Grails developers
* [Groovy Podcast](https://nofluffjuststuff.com/groovypodcast) - Ken Kousen and Baruch Sadogursky discuss news and insight from the Groovy ecosystem.

## Interactive Learning
* [Groovy-Koans](http://nadavc.github.io/groovykoans/) - Collection of small exercises in the form of unit tests

## Blogs of core committer
* [Guillaume Laforge's blog](http://glaforge.appspot.com/)
* [Cédric Champeau's blog](http://melix.github.io/blog/)
* [Jochen Theodorou's blog](http://blackdragsview.blogspot.com/)
* [Grails Team blog](http://grailsblog.objectcomputing.com/)

## Conferences
* [Community Over Code](https://communityovercode.org/) - have a Groovy Track
* [Greachconf](http://greachconf.com) (discontinued)
* [GR8Conf Europe](https://gr8conf.eu) (discontinued)
* [GR8Conf USA](http://gr8conf.us) (discontinued)

# Contributing

Fork this repository, edit this file and send a pull request.

## Using awesome.groovy script

You can use the `awesome.groovy` script to search awesome projects on github and generate the entry prepoulated with project name, repo url and description in markdown format. All you need to do is place it under right group in the markdown list in `README.md`.

### Examples

to find out repos where language is groovy and whose name contain gpars and

    ./awesome.groovy -l groovy gpars

to find out repos by user 'kdabir' and name contains glide

    ./awesome.groovy -u kdabir glide

to find out repos whose name contains glide

    ./awesome.groovy glide

If you are lazy to download the repo, an easy way is:

    groovy "https://git.io/awesome" -l groovy glide

# Credits

To all the awesome-* repos out there and their aggreators like [this](https://github.com/erichs/awesome-awesome) [![GitHub stars](https://img.shields.io/github/stars/erichs/awesome-awesome?style=flat)](https://github.com/erichs/awesome-awesome/stargazers) and [this](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers).
