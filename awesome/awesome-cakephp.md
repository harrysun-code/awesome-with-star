# CakePHP

[![GitHub stars](https://img.shields.io/github/stars/friendsofcake/awesome-cakephp?style=flat)](https://github.com/friendsofcake/awesome-cakephp/stargazers)

# Awesome CakePHP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of CakePHP plugins, resources, and tools.

[CakePHP](https://cakephp.org/) is a rapid development PHP framework that uses well-known design patterns like MVC and ORM. It provides a robust foundation for building web applications with conventions over configuration.

If you are looking for previous CakePHP resources please visit:
- the [CakePHP 2.x version](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake2) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/awesome-cakephp/tree/cake2?style=flat)](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake2/stargazers) of this awesome list
- the [CakePHP 3.x version](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake3) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/awesome-cakephp/tree/cake3?style=flat)](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake3/stargazers) of this awesome list
- the [CakePHP 4.x version](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake4) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/awesome-cakephp/tree/cake4?style=flat)](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake4/stargazers) of this awesome list
- this wiki with a [list of not-yet upgraded plugins](https://github.com/FriendsOfCake/awesome-cakephp/wiki#plugins-not-yet-upgraded-from-2x-to-3x)

Additional lists you might find useful:
- [CakePHP Plugins](https://plugins.cakephp.org)
- [Awesome PHP](https://github.com/ziadoz/awesome-php) [![GitHub stars](https://img.shields.io/github/stars/ziadoz/awesome-php?style=flat)](https://github.com/ziadoz/awesome-php/stargazers)
- [Awesome Awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers)

> For those wondering; this list differs from plugins.cakephp.org by supporting
> plugin subparts (instead of only the whole plugin/repo), more granular
> grouping and the primary focus on task-specific functionality.

## Contents

- [Plugins](#plugins)
	- [AI Tools](#ai-tools)
	- [Architecture](#architecture)
	- [Asset Management](#asset-management)
	- [Auditing / Logging](#auditing--logging)
	- [Authentication and Authorization](#authentication-and-authorization)
	- [Caching](#caching)
	- [Code Analysis](#code-analysis)
    - [Console](#console)
	- [Debugging](#debugging)
	- [Email](#email)
	- [File Manipulation](#file-manipulation)
	- [Filtering and Validation](#filtering-and-validation)
	- [Geolocation](#geolocation)
	- [I18n](#i18n)
	- [Imagery](#imagery)
	- [Libs](#libs)
	- [Markup](#markup)
	- [Migration](#migration)
	- [Miscellaneous](#miscellaneous)
	- [Navigation](#navigation)
	- [Notifications and Real-time Communication](#notifications-and-real-time-communication)
	- [ORM / Database / Datamapping](#orm--database--datamapping)
	- [PDF](#pdf)
	- [Queue](#queue)
	- [REST and API](#rest-and-api)
	- [Search](#search)
	- [Security](#security)
	- [SEO](#seo)
	- [Skeleton](#skeleton)
	- [Social](#social)
	- [Templating](#templating)
	- [Testing](#testing)
	- [Third Party APIs](#third-party-apis)
- [Software](#software)
	- [Development Environment](#development-environment)
	- [Web Applications](#web-applications)
	- [CMS and applications built on CakePHP](#cms-and-applications-built-on-cakephp)
	- [Demo](#demo)
- [Resources](#resources)
	- [Help](#help)
	- [CakePHP Websites](#cakephp-websites)
	- [CakePHP Books and Articles](#cakephp-books-and-articles)
	- [CakePHP Videos](#cakephp-videos)
	- [CakePHP Tutorials](#cakephp-tutorials)
	- [CakePHP Reading and Listening](#cakephp-reading-and-listening)
	- [CakePHP Internals Reading](#cakephp-internals-reading)
- [Conferences](#conferences)

## Plugins

### AI Tools
*Plugins and libraries for integrating artificial intelligence and machine learning tools.*

- [Crustum/OpenRouter plugin](https://github.com/crustum/cakephp-open-router) [![GitHub stars](https://img.shields.io/github/stars/crustum/cakephp-open-router?style=flat)](https://github.com/crustum/cakephp-open-router/stargazers) - Integration with OpenRouter service for unified LLM access, supporting multiple AI models with chat completions, streaming, tool calling, and web search.
- [Synapse plugin](https://github.com/josbeir/cakephp-synapse) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-synapse?style=flat)](https://github.com/josbeir/cakephp-synapse/stargazers) - Expose your application functionality via MCP, with built-in tools and documentation search to help you discover and interact with your app's capabilities.

### Architecture

- [Burzum/CakeServiceLayer plugin](https://github.com/burzum/cakephp-service-layer) [![GitHub stars](https://img.shields.io/github/stars/burzum/cakephp-service-layer?style=flat)](https://github.com/burzum/cakephp-service-layer/stargazers) - Service layer and domain/business model implementation.

### Asset Management
*Managing, compressing and minifying website assets.*

- [AssetCompress plugin](https://github.com/markstory/asset_compress) [![GitHub stars](https://img.shields.io/github/stars/markstory/asset_compress?style=flat)](https://github.com/markstory/asset_compress/stargazers) - A complete asset manager for CakePHP.
- [AssetMix plugin](https://github.com/ishanvyas22/asset-mix) [![GitHub stars](https://img.shields.io/github/stars/ishanvyas22/asset-mix?style=flat)](https://github.com/ishanvyas22/asset-mix/stargazers) - Provides integration with [Laravel Mix](https://laravel-mix.com) asset compilation.
- [CakeVite plugin](https://github.com/josbeir/cakephp-vite) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-vite?style=flat)](https://github.com/josbeir/cakephp-vite/stargazers) - A fully-featured [Vite](https://vite.dev/) plugin (spiritual successor of [brandcom/cakephp-vite](https://github.com/brandcom/cakephp-vite) [![GitHub stars](https://img.shields.io/github/stars/brandcom/cakephp-vite?style=flat)](https://github.com/brandcom/cakephp-vite/stargazers)).

### Auditing / Logging
*Tracking changes and events in your app.*

- [AuditStash plugin](https://github.com/dereuromark/cakephp-audit-stash) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-audit-stash?style=flat)](https://github.com/dereuromark/cakephp-audit-stash/stargazers) - Flexible and rock solid audit log tracking.
- [Bouncer plugin](https://github.com/dereuromark/cakephp-bouncer) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-bouncer?style=flat)](https://github.com/dereuromark/cakephp-bouncer/stargazers) - The pendant to AuditStash, allow moderation and approval of add/edit/delete actions before the actual change is applied.
- [DatabaseLog plugin](https://github.com/dereuromark/CakePHP-DatabaseLog) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/CakePHP-DatabaseLog?style=flat)](https://github.com/dereuromark/CakePHP-DatabaseLog/stargazers) - Simple and stand-alone logging to database instead of files.
- [Muffin/Footprint plugin](https://github.com/UseMuffin/Footprint) [![GitHub stars](https://img.shields.io/github/stars/UseMuffin/Footprint?style=flat)](https://github.com/UseMuffin/Footprint/stargazers) - Plugin to allow passing currently logged in user to model layer.
- [Version plugin](https://github.com/josegonzalez/cakephp-version) [![GitHub stars](https://img.shields.io/github/stars/josegonzalez/cakephp-version?style=flat)](https://github.com/josegonzalez/cakephp-version/stargazers) - A plugin that facilitates versioned database entities.

### Authentication and Authorization
*Plugins and libraries for implementing authentication and authorization.*

- [ADmad/SocialAuth plugin](https://github.com/ADmad/cakephp-social-auth) [![GitHub stars](https://img.shields.io/github/stars/ADmad/cakephp-social-auth?style=flat)](https://github.com/ADmad/cakephp-social-auth/stargazers) - A plugin which allows you to authenticate using social providers like Facebook/Google/Twitter etc. using [SocialConnect/auth](https://github.com/SocialConnect/auth) [![GitHub stars](https://img.shields.io/github/stars/SocialConnect/auth?style=flat)](https://github.com/SocialConnect/auth/stargazers) social sign on library.
- [ApiTokenAuthenticator plugin](https://github.com/rrd108/api-token-authenticator) [![GitHub stars](https://img.shields.io/github/stars/rrd108/api-token-authenticator?style=flat)](https://github.com/rrd108/api-token-authenticator/stargazers) - A simple token authentication plugin for CakePHP REST APIs.
- [Authentication plugin](https://github.com/cakephp/authentication) [![GitHub stars](https://img.shields.io/github/stars/cakephp/authentication?style=flat)](https://github.com/cakephp/authentication/stargazers) - Official CakePHP authentication middleware plugin.
- [Authorization plugin](https://github.com/cakephp/authorization) [![GitHub stars](https://img.shields.io/github/stars/cakephp/authorization?style=flat)](https://github.com/cakephp/authorization/stargazers) - Official CakePHP authorization stack.
- [CakeDC/Users plugin](https://github.com/CakeDC/users) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/users?style=flat)](https://github.com/CakeDC/users/stargazers) - Complete user management (admin panel, remember me, etc), Social login (FB, Twitter, LinkedIn, Google, Instagram), RBAC, API and more.
- [CakeVerification plugin](https://github.com/salines/cakephp-verification) [![GitHub stars](https://img.shields.io/github/stars/salines/cakephp-verification?style=flat)](https://github.com/salines/cakephp-verification/stargazers) - Two-factor verification supporting email OTP, email magic link, SMS OTP, and TOTP (Google Authenticator).

- [TinyAuth plugin](https://github.com/dereuromark/cakephp-tinyauth) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tinyauth?style=flat)](https://github.com/dereuromark/cakephp-tinyauth/stargazers) - Authentication and role-based (single/multi) authorization as very light-weight approach.
- [Tools:Passwordable](https://github.com/dereuromark/cakephp-tools) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tools?style=flat)](https://github.com/dereuromark/cakephp-tools/stargazers) - Containing [Passwordable behavior](https://dereuromark.github.io/cakephp-tools/behavior/passwordable) for a DRY approach on password hashing.
- [TwoFactorAuth plugin](https://github.com/andrej-griniuk/cakephp-two-factor-auth) [![GitHub stars](https://img.shields.io/github/stars/andrej-griniuk/cakephp-two-factor-auth?style=flat)](https://github.com/andrej-griniuk/cakephp-two-factor-auth/stargazers) - Allows two factor authentication using Google Authenticator or similar app to generate one-time codes. Based on [RobThree/TwoFactorAuth](https://github.com/RobThree/TwoFactorAuth) [![GitHub stars](https://img.shields.io/github/stars/RobThree/TwoFactorAuth?style=flat)](https://github.com/RobThree/TwoFactorAuth/stargazers) library.

### Caching
*Storing data for faster retrieval.*

- [Cache plugin](https://github.com/dereuromark/cakephp-cache) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-cache?style=flat)](https://github.com/dereuromark/cakephp-cache/stargazers) - For caching views (HTML, CSV, JSON, XML, ...) as static cache files.
- [CakeDC/CachedRouting plugin](https://github.com/CakeDC/cakephp-cached-routing) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/cakephp-cached-routing?style=flat)](https://github.com/CakeDC/cakephp-cached-routing/stargazers) - Provides a cached version of the RoutingMiddleware to improve the load time of routes.

### Code Analysis
*Analyzing, parsing and manipulation codebases.*

- [cakedc/cakephp-phpstan](https://github.com/CakeDC/cakephp-phpstan) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/cakephp-phpstan?style=flat)](https://github.com/CakeDC/cakephp-phpstan/stargazers) - A PHPStan extension to resolve CakePHP magic around getter return types for the static analyzer.
- [IdeHelper plugin](https://github.com/dereuromark/cakephp-ide-helper) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-ide-helper?style=flat)](https://github.com/dereuromark/cakephp-ide-helper/stargazers) - Helps to make IDE support better by adding annotations to your existing code similar to what baking does to new code.
- [IdeHelperExtra plugin](https://github.com/dereuromark/cakephp-ide-helper-extra) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-ide-helper-extra?style=flat)](https://github.com/dereuromark/cakephp-ide-helper-extra/stargazers) - Useful IdeHelper addons for other plugins or custom use cases.
- [lordsimal/cakephp-psalm](https://github.com/LordSimal/cakephp-psalm) [![GitHub stars](https://img.shields.io/github/stars/LordSimal/cakephp-psalm?style=flat)](https://github.com/LordSimal/cakephp-psalm/stargazers) - A Psalm extension to resolve CakePHP magic around getter return types for the static analyzer.
- [TestHelper plugin](https://github.com/dereuromark/cakephp-test-helper) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-test-helper?style=flat)](https://github.com/dereuromark/cakephp-test-helper/stargazers) - Provides testing enhancements and TDD support as browser backend.

### Console
*Command-line tools and improvements.*

- [SignalHandler plugin](https://github.com/skie/SignalHandler) [![GitHub stars](https://img.shields.io/github/stars/skie/SignalHandler?style=flat)](https://github.com/skie/SignalHandler/stargazers) - Cross-platform signal handling for CakePHP console commands with zero external dependencies. Supports Linux (pcntl), Windows (native API).
- [Scheduling plugin](https://github.com/skie/cakephp-scheduling) [![GitHub stars](https://img.shields.io/github/stars/skie/cakephp-scheduling?style=flat)](https://github.com/skie/cakephp-scheduling/stargazers) - The plugin provides task scheduling capabilities with sub-minute precision, allowing you to schedule tasks as frequently as every second, with single crontab entry point. It allows tasks monitoring.

### Debugging
*Debugging and local development.*

- [AssociationsDebugger plugin](https://github.com/zunnu/associations-debugger) [![GitHub stars](https://img.shields.io/github/stars/zunnu/associations-debugger?style=flat)](https://github.com/zunnu/associations-debugger/stargazers) - A plugin that draws your model associations as diagram.
- [CakephpWhoops plugin](https://github.com/dereuromark/cakephp-whoops) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-whoops?style=flat)](https://github.com/dereuromark/cakephp-whoops/stargazers) - PHP errors and exceptions for cool kids with [filp/whoops](https://github.com/filp/whoops) [![GitHub stars](https://img.shields.io/github/stars/filp/whoops?style=flat)](https://github.com/filp/whoops/stargazers).
- [DebugKit plugin](https://github.com/cakephp/debug_kit) [![GitHub stars](https://img.shields.io/github/stars/cakephp/debug_kit?style=flat)](https://github.com/cakephp/debug_kit/stargazers) - The de-facto standard for debugging.
- [Execution order](https://github.com/dereuromark/executionorder) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/executionorder?style=flat)](https://github.com/dereuromark/executionorder/stargazers) - A demo app to display the execution order of files, methods and callbacks.
- [Sentry plugin](https://github.com/lordsimal/cakephp-sentry) [![GitHub stars](https://img.shields.io/github/stars/lordsimal/cakephp-sentry?style=flat)](https://github.com/lordsimal/cakephp-sentry/stargazers) - A plugin to seamlessly integrate Sentry for errors and exceptions.
- [Setup plugin](https://github.com/dereuromark/cakephp-setup) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-setup?style=flat)](https://github.com/dereuromark/cakephp-setup/stargazers) - A lightweight setup plugin containing healthcheck(s), debugging and maintenance tools.

### Email
*Transports and tools for email handling.*

- [Queue plugin](https://github.com/dereuromark/cakephp-queue) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-queue?style=flat)](https://github.com/dereuromark/cakephp-queue/stargazers) - A dependency-free queue-based mail solution using Mailer/Email class, allowing re-queue on (network) failure.
- [SendGrid plugin](https://github.com/sprintcube/cakephp-sendgrid) [![GitHub stars](https://img.shields.io/github/stars/sprintcube/cakephp-sendgrid?style=flat)](https://github.com/sprintcube/cakephp-sendgrid/stargazers) - Email transport plugin for sending email via SendGrid API.

### File Manipulation
*Upload, storage, and file handling.*

- [FileStorage plugin](https://github.com/dereuromark/cakephp-file-storage) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-file-storage?style=flat)](https://github.com/dereuromark/cakephp-file-storage/stargazers) - Flexible file storage and upload plugin.
- [Josegonzalez/Upload plugin](https://github.com/FriendsOfCake/cakephp-upload) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/cakephp-upload?style=flat)](https://github.com/FriendsOfCake/cakephp-upload/stargazers) - A customisable plugin that uses [Flysystem](https://flysystem.thephpleague.com/) to write to multiple backends (Dropbox, FTP, S3, Local, etc.).

### Filtering and Validation
*Data sanitization and validation rules.*

- see Cake/Localized plugin below.
- see Tools plugin below.
- [RuleFlow plugin](https://github.com/skie/rule-flow) [![GitHub stars](https://img.shields.io/github/stars/skie/rule-flow?style=flat)](https://github.com/skie/rule-flow/stargazers) - A plugin that seamlessly transforms server-side validation rules into client-side JSON Logic validation, providing automatic form validation without requiring separate client-side validation code.


### Geolocation
*Geocoding addresses and working with latitudes and longitudes.*

- [Geo plugin](https://github.com/dereuromark/cakephp-geo) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-geo?style=flat)](https://github.com/dereuromark/cakephp-geo/stargazers) - Containing [Geocoder behavior](https://www.dereuromark.de/2012/06/12/geocoding-with-cakephp/) and [GoogleMaps helper](https://www.dereuromark.de/2010/12/21/googlemapsv3-cakephp-helper/).

### I18n
*I18n (Internationalization) and L10n (Localization).*

- [ADmad/I18n plugin](https://github.com/ADmad/cakephp-i18n) [![GitHub stars](https://img.shields.io/github/stars/ADmad/cakephp-i18n?style=flat)](https://github.com/ADmad/cakephp-i18n/stargazers) - A plugin with I18n related tools.
- [Cake/Localized plugin](https://github.com/cakephp/localized) [![GitHub stars](https://img.shields.io/github/stars/cakephp/localized?style=flat)](https://github.com/cakephp/localized/stargazers) - Localized validation and ready-to-use translation PO files.
- [Translate plugin](https://github.com/dereuromark/cakephp-translate) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-translate?style=flat)](https://github.com/dereuromark/cakephp-translate/stargazers) - Translate your translations in the backend with ease.

### Imagery
*Image processing and manipulation libraries.*

- [ADmad/Glide plugin](https://github.com/ADmad/cakephp-glide) [![GitHub stars](https://img.shields.io/github/stars/ADmad/cakephp-glide?style=flat)](https://github.com/ADmad/cakephp-glide/stargazers) - A plugin for using [Glide](https://glide.thephpleague.com/) image manipulation library.
- [file-storage-image-processor](https://github.com/php-collective/file-storage-image-processor) [![GitHub stars](https://img.shields.io/github/stars/php-collective/file-storage-image-processor?style=flat)](https://github.com/php-collective/file-storage-image-processor/stargazers) as `intervention/image` wrapper through [FileStorage plugin](https://github.com/dereuromark/cakephp-file-storage) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-file-storage?style=flat)](https://github.com/dereuromark/cakephp-file-storage/stargazers).
- [QrCode plugin](https://github.com/dereuromark/cakephp-qrcode/) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-qrcode/?style=flat)](https://github.com/dereuromark/cakephp-qrcode//stargazers) - Easily render SVG/PNG QR Codes for your app.

### Libs
*Useful libraries or tools that don't fit in any of the other categories.*

- [Chronos](https://github.com/cakephp/chronos) [![GitHub stars](https://img.shields.io/github/stars/cakephp/chronos?style=flat)](https://github.com/cakephp/chronos/stargazers) - A simple standalone DateTime API extension (successor of Carbon).
- [Composer Installers](https://github.com/composer/installers) [![GitHub stars](https://img.shields.io/github/stars/composer/installers?style=flat)](https://github.com/composer/installers/stargazers) - A multi framework Composer library installer.
- [Composer](https://getcomposer.org/)/[Packagist](https://packagist.org/) - A package and dependency manager.
- [Graphviz](https://github.com/alexandresalome/graphviz) [![GitHub stars](https://img.shields.io/github/stars/alexandresalome/graphviz?style=flat)](https://github.com/alexandresalome/graphviz/stargazers) - A Graphviz library.
- [Rocketeer](https://github.com/rocketeers/rocketeer) [![GitHub stars](https://img.shields.io/github/stars/rocketeers/rocketeer?style=flat)](https://github.com/rocketeers/rocketeer/stargazers) - PHP task runner and deployment package.

### Markup
*Syntax highlighting and markup processing.*

- [Markup plugin](https://github.com/dereuromark/cakephp-markup) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-markup?style=flat)](https://github.com/dereuromark/cakephp-markup/stargazers) - Allows to use PHP or JS based syntax highlighting.

### Migration
*Plugins and resources around migration and upgrading.*

- [Migrations plugin](https://github.com/cakephp/migrations) [![GitHub stars](https://img.shields.io/github/stars/cakephp/migrations?style=flat)](https://github.com/cakephp/migrations/stargazers) - (DB) Migration plugin.
- [Upgrade app](https://github.com/cakephp/upgrade) [![GitHub stars](https://img.shields.io/github/stars/cakephp/upgrade?style=flat)](https://github.com/cakephp/upgrade/stargazers) - Official upgrade app for 3.x=>4.x and 4.x=>5.x.
- [Upgrade app (extended)](https://github.com/dereuromark/upgrade) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/upgrade?style=flat)](https://github.com/dereuromark/upgrade/stargazers) - An extended upgrade app for 3.x=>4.x and some 5.x snippets.
- [Upgrade/Migration Guide](https://book.cakephp.org/5/en/appendices.html) - Official migration guide.

### Miscellaneous
*Misc plugins and libraries.*

- [Ajax plugin](https://github.com/dereuromark/cakephp-ajax) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-ajax?style=flat)](https://github.com/dereuromark/cakephp-ajax/stargazers) - A plugin to ease handling AJAX requests.
- [AttributeRegistry plugin](https://github.com/josbeir/cakephp-attribute-registry) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-attribute-registry?style=flat)](https://github.com/josbeir/cakephp-attribute-registry/stargazers) - A powerful CakePHP plugin for discovering, caching, and querying PHP 8 attributes across your application and plugins.
- [CakeDC/Enum plugin](https://github.com/CakeDC/enum) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/enum?style=flat)](https://github.com/CakeDC/enum/stargazers) - A plugin to add enumeration list support to your app.
- [CakeDto plugin](https://github.com/dereuromark/cakephp-dto) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-dto?style=flat)](https://github.com/dereuromark/cakephp-dto/stargazers) - Quickly generate useful data transfer objects for your app (mutable/immutable), replacing messy arrays and leveraging your IDE through typehinting and autocomplete.
- [CakeHtmx plugin](https://github.com/zunnu/cake-htmx) [![GitHub stars](https://img.shields.io/github/stars/zunnu/cake-htmx?style=flat)](https://github.com/zunnu/cake-htmx/stargazers) - CakePHP integration for [htmx](https://htmx.org/).
- [Calendar plugin](https://github.com/dereuromark/cakephp-calendar) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-calendar?style=flat)](https://github.com/dereuromark/cakephp-calendar/stargazers) - For generating basic calendars. Includes IcalView for ICS calendar file generation.
- [DatabaseBackup plugin](https://github.com/mirko-pagliai/cakephp-database-backup) [![GitHub stars](https://img.shields.io/github/stars/mirko-pagliai/cakephp-database-backup?style=flat)](https://github.com/mirko-pagliai/cakephp-database-backup/stargazers) - A plugin to export, import and manage database backups. Currently, the plugin supports MySQL, PostgreSQL and SQLite databases.
- [Feedback plugin](https://github.com/dereuromark/cakephp-feedback) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-feedback?style=flat)](https://github.com/dereuromark/cakephp-feedback/stargazers) - Allow visitors to send quick and easy feedback incl. a screenshot via sidebar form.
- [Flash plugin](https://github.com/dereuromark/cakephp-flash) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-flash?style=flat)](https://github.com/dereuromark/cakephp-flash/stargazers) - More powerful flash messages for your application.
- [Inertia plugin](https://github.com/CakeDC/cakephp-inertia) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/cakephp-inertia?style=flat)](https://github.com/CakeDC/cakephp-inertia/stargazers) - Plugin for connecting a Vue 3 app and use an API interface using a middleware.
- [OPCache Preloader](https://github.com/cnizzardini/cakephp-preloader) [![GitHub stars](https://img.shields.io/github/stars/cnizzardini/cakephp-preloader?style=flat)](https://github.com/cnizzardini/cakephp-preloader/stargazers) - An OPCache Preloader for CakePHP applications. 
- [Setup:Maintenance](https://github.com/dereuromark/cakephp-setup/blob/master/docs/Maintenance/Maintenance.md) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-setup/blob/master/docs/Maintenance/Maintenance.md?style=flat)](https://github.com/dereuromark/cakephp-setup/blob/master/docs/Maintenance/Maintenance.md/stargazers) - Maintenance shell to go into maintenance mode for all requests with optional IP whitelisting.
- [Shim plugin](https://github.com/dereuromark/cakephp-shim) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-shim?style=flat)](https://github.com/dereuromark/cakephp-shim/stargazers) - A plugin containing useful shims and improvements as basis for your application.
- [Tools plugin](https://github.com/dereuromark/cakephp-tools) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tools?style=flat)](https://github.com/dereuromark/cakephp-tools/stargazers) - Containing lots of useful helpers, behaviors, components, commands, helpers, libs and more.
- [Workflow plugin](https://github.com/dereuromark/cakephp-workflow) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-workflow?style=flat)](https://github.com/dereuromark/cakephp-workflow/stargazers) - Batteries-included state machine plugin with PHP 8 attributes, YAML config, audit trails, and visual admin dashboard.

### Navigation
*Building navigation structures.*

- [Icings/Menu plugin](https://github.com/icings/menu) [![GitHub stars](https://img.shields.io/github/stars/icings/menu?style=flat)](https://github.com/icings/menu/stargazers) - A [KnpMenu](https://github.com/KnpLabs/KnpMenu) [![GitHub stars](https://img.shields.io/github/stars/KnpLabs/KnpMenu?style=flat)](https://github.com/KnpLabs/KnpMenu/stargazers) seasoned menu plugin for CakePHP.
- [Menu plugin](https://github.com/dereuromark/cakephp-menu) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-menu?style=flat)](https://github.com/dereuromark/cakephp-menu/stargazers) - Composable menu builder and renderer for nested navigation, active-state matching, and breadcrumbs - and zero dependencies.

### Notifications and Real-time Communication
*Working with notification software.*

- [Crustum/Broadcasting plugin](https://github.com/crustum/broadcasting) [![GitHub stars](https://img.shields.io/github/stars/crustum/broadcasting?style=flat)](https://github.com/crustum/broadcasting/stargazers) - The Broadcasting plugin provides real-time event broadcasting for CakePHP applications using WebSocket connections compatible with the Pusher protocol or Redis pub/sub.
- [Crustum/Notification plugin](https://github.com/crustum/notification) [![GitHub stars](https://img.shields.io/github/stars/crustum/notification?style=flat)](https://github.com/crustum/notification/stargazers) - The Notification plugin provides support for sending notifications across a variety of delivery channels.
- [Mercure plugin](https://github.com/josbeir/cakephp-mercure) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-mercure?style=flat)](https://github.com/josbeir/cakephp-mercure/stargazers) - Push real-time updates to clients using the Mercure protocol.

### ORM / Database / Datamapping
*Plugins that implement object-relational mapping or data-mapping techniques.*

- [ADmad/Sequence plugin](https://github.com/ADmad/cakephp-sequence) [![GitHub stars](https://img.shields.io/github/stars/ADmad/cakephp-sequence?style=flat)](https://github.com/ADmad/cakephp-sequence/stargazers) - Behavior for maintaining ordered list of records.
- [CakeDecimal plugin](https://github.com/dereuromark/cakephp-decimal) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-decimal?style=flat)](https://github.com/dereuromark/cakephp-decimal/stargazers) - A value object approach on handling decimals.
- [CakeUid](https://github.com/josbeir/cakephp-uid) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-uid?style=flat)](https://github.com/josbeir/cakephp-uid/stargazers) - A collection of UID field types for your Tables (UUIDV4, UUIDV6, UUIDV7, ULID).
- [Duplicatable plugin](https://github.com/riesenia/cakephp-duplicatable) [![GitHub stars](https://img.shields.io/github/stars/riesenia/cakephp-duplicatable?style=flat)](https://github.com/riesenia/cakephp-duplicatable/stargazers) - Behavior for duplicating entities including related data.
- [Lampager/Cake plugin](https://github.com/lampager/lampager-cakephp) [![GitHub stars](https://img.shields.io/github/stars/lampager/lampager-cakephp?style=flat)](https://github.com/lampager/lampager-cakephp/stargazers) - Rapid pagination without using OFFSET.
- [Muffin/Orderly plugin](https://github.com/usemuffin/orderly) [![GitHub stars](https://img.shields.io/github/stars/usemuffin/orderly?style=flat)](https://github.com/usemuffin/orderly/stargazers) - Allows setting default order for your tables.
- [Muffin/Trash plugin](https://github.com/usemuffin/trash) [![GitHub stars](https://img.shields.io/github/stars/usemuffin/trash?style=flat)](https://github.com/usemuffin/trash/stargazers) - Soft-delete behavior for CakePHP.
- [Itosho/EasyQuery plugin](https://github.com/itosho/easy-query) [![GitHub stars](https://img.shields.io/github/stars/itosho/easy-query?style=flat)](https://github.com/itosho/easy-query/stargazers) - Behavior for easily generating some complicated queries like (bulk) insert/upsert etc.
- [Icings/Partitionable plugin](https://github.com/icings/partitionable) [![GitHub stars](https://img.shields.io/github/stars/icings/partitionable?style=flat)](https://github.com/icings/partitionable/stargazers) - Partitionable associations allowing for basic limiting per group.

### PDF
*Plugins and software for working with PDF files.*

- [CakePdf plugin](https://github.com/FriendsOfCake/CakePdf) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/CakePdf?style=flat)](https://github.com/FriendsOfCake/CakePdf/stargazers) - A plugin around PDF generation.

### Queue
*Working with event and task queues.*

- [Queue plugin](https://github.com/cakephp/queue) [![GitHub stars](https://img.shields.io/github/stars/cakephp/queue?style=flat)](https://github.com/cakephp/queue/stargazers) - CakePHP core queue system for the [php-queue](https://php-enqueue.github.io) queue library.
- [Cake/Enqueue plugin](https://github.com/CakeDC/cakephp-enqueue) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/cakephp-enqueue?style=flat)](https://github.com/CakeDC/cakephp-enqueue/stargazers) - Database-driven message queue integration using the Enqueue library for CakePHP Queue plugin.
- [Crustum/BatchQueue plugin](https://github.com/crustum/batch-queue) [![GitHub stars](https://img.shields.io/github/stars/crustum/batch-queue?style=flat)](https://github.com/crustum/batch-queue/stargazers) - Unified system for managing batch job processing with parallel execution and sequential chains.
- [Crustum/Temporal plugin](https://github.com/crustum/cakephp-temporal) [![GitHub stars](https://img.shields.io/github/stars/crustum/cakephp-temporal?style=flat)](https://github.com/crustum/cakephp-temporal/stargazers) - Workflow orchestration plugin for durable execution, reliable background jobs, and long-running processes with automatic retries.
- [Queue plugin](https://github.com/dereuromark/cakephp-queue) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-queue?style=flat)](https://github.com/dereuromark/cakephp-queue/stargazers) - A minimal and dependency-free queue solution.
- [QueueScheduler plugin](https://github.com/dereuromark/cakephp-queue-scheduler) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-queue-scheduler?style=flat)](https://github.com/dereuromark/cakephp-queue-scheduler/stargazers) - A dependency-free crontab-like scheduler as DB driven solution and addon to Queue (dereuromark) plugin.

### REST and API
*Plugins and web tools for developing REST-ful APIs.*

- [CRUD plugin](https://github.com/FriendsOfCake/crud) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/crud?style=flat)](https://github.com/FriendsOfCake/crud/stargazers) - CakePHP Application development on steroids - rapid prototyping / scaffolding & production-ready code.
- [CakeDC/Api plugin](https://github.com/CakeDC/cakephp-api) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/cakephp-api?style=flat)](https://github.com/CakeDC/cakephp-api/stargazers) - All-in-one solution to provide a complete API. It includes versioning, renderers, CRUD, authentication, extensions (paginate, filter, HATEOAS), and much more.
- [FractalTransformerView plugin](https://github.com/andrej-griniuk/cakephp-fractal-transformer-view) [![GitHub stars](https://img.shields.io/github/stars/andrej-griniuk/cakephp-fractal-transformer-view?style=flat)](https://github.com/andrej-griniuk/cakephp-fractal-transformer-view/stargazers) - A plugin which allows using [Fractal transformers](https://fractal.thephpleague.com/transformers/) for your API output.
- [MixerApi](https://mixerapi.com) - Streamline development of modern RESTful APIs for your team's CakePHP project.
- [SwaggerBake plugin](https://github.com/cnizzardini/cakephp-swagger-bake) [![GitHub stars](https://img.shields.io/github/stars/cnizzardini/cakephp-swagger-bake?style=flat)](https://github.com/cnizzardini/cakephp-swagger-bake/stargazers) - This plugin automatically builds OpenAPI from your existing models and routes for display in Swagger and Redoc.

### Search
*Plugins and software for indexing and performing search queries on data.*

- [Cake/Elasticsearch plugin](https://github.com/cakephp/elastic-search) [![GitHub stars](https://img.shields.io/github/stars/cakephp/elastic-search?style=flat)](https://github.com/cakephp/elastic-search/stargazers) - Alternative ORM using [Elasticsearch](https://www.elastic.co/) as its backend.
- [CakeDC/SearchFilter plugin](https://github.com/CakeDC/search-filter) [![GitHub stars](https://img.shields.io/github/stars/CakeDC/search-filter?style=flat)](https://github.com/CakeDC/search-filter/stargazers) - Powerful and flexible solution for implementing advanced search functionality. Provides a robust set of tools for creating dynamic, user-friendly search interfaces with minimal effort.
- [PlumSearch plugin](https://github.com/skie/plum_search) [![GitHub stars](https://img.shields.io/github/stars/skie/plum_search?style=flat)](https://github.com/skie/plum_search/stargazers) - Implements custom, flexible and extendable search strategies. Implements PRG pattern.
- [Search plugin](https://github.com/FriendsOfCake/search) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/search?style=flat)](https://github.com/FriendsOfCake/search/stargazers) - Provides easy searching/filtering for paginated views using PRG pattern.
- [Tags plugin](https://github.com/dereuromark/cakephp-tags) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tags?style=flat)](https://github.com/dereuromark/cakephp-tags/stargazers) - For tagging and finding tagged records.

### Security
*Plugins and information around security, preventing vulnerabilities and protection against XSS and alike.*

- [Captcha plugin](https://github.com/dereuromark/cakephp-captcha) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-captcha?style=flat)](https://github.com/dereuromark/cakephp-captcha/stargazers) - Simple, unobtrusive and extendable captcha solution providing by default an image based math captcha.
- [Expose plugin](https://github.com/dereuromark/cakephp-expose) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-expose?style=flat)](https://github.com/dereuromark/cakephp-expose/stargazers) - Expose entities through additional UUIDs instead of their AIID primary keys to obfuscate those IDs and data associated with these numerically ordered values.
- [Muffin/Obfuscate plugin](https://github.com/usemuffin/obfuscate) [![GitHub stars](https://img.shields.io/github/stars/usemuffin/obfuscate?style=flat)](https://github.com/usemuffin/obfuscate/stargazers) - Primary key obfuscation/shortening using UUIDs, HashIds, Optimus, Tiny and/or custom obfuscation strategies.
- [Muffin/Throttle plugin](https://github.com/usemuffin/throttle) [![GitHub stars](https://img.shields.io/github/stars/usemuffin/throttle?style=flat)](https://github.com/usemuffin/throttle/stargazers) - A plugin for rate limiting (API) requests.
- [Recaptcha plugin](https://github.com/ctlabvn/Recaptcha) [![GitHub stars](https://img.shields.io/github/stars/ctlabvn/Recaptcha?style=flat)](https://github.com/ctlabvn/Recaptcha/stargazers) - Simple, lightweight Google Recaptcha v2.

### SEO
*Search Engine Optimization.*

- [Muffin/Slug plugin](https://github.com/UseMuffin/Slug) [![GitHub stars](https://img.shields.io/github/stars/UseMuffin/Slug?style=flat)](https://github.com/UseMuffin/Slug/stargazers) - A plugin for generating slugs and finding records by slug. Uses a pluggable architecture which allows using your own slug generator class.
- [Tools:Slugged](https://github.com/dereuromark/cakephp-tools) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tools?style=flat)](https://github.com/dereuromark/cakephp-tools/stargazers) - Containing Slugged behavior to auto-generate URL-compatible slugs from titles.

### Skeleton
*Plugins and repositories around app skeletons.*

- [App template](https://github.com/cakephp/app) [![GitHub stars](https://img.shields.io/github/stars/cakephp/app?style=flat)](https://github.com/cakephp/app/stargazers) - An empty CakePHP project for use with composer.
- [BS flavored App template](https://github.com/dereuromark/cakephp-app) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-app?style=flat)](https://github.com/dereuromark/cakephp-app/stargazers) - An empty CakePHP project with BS5 and FontAwesome out of the box.

### Social
*Plugins around social features.*

- [Comments plugin](https://github.com/dereuromark/cakephp-comments) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-comments?style=flat)](https://github.com/dereuromark/cakephp-comments/stargazers) - Allows users to comment records, supporting different formats.
- [Favorites plugin](https://github.com/dereuromark/cakephp-favorites) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-favorites?style=flat)](https://github.com/dereuromark/cakephp-favorites/stargazers) - Allows users to star/like/favor records.
- [Ratings plugin](https://github.com/dereuromark/cakephp-ratings) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-ratings?style=flat)](https://github.com/dereuromark/cakephp-ratings/stargazers) - Allows users to rate records and displays ratings.

### Templating
*Template engines and view generation.*

- [Bake plugin](https://github.com/cakephp/bake) [![GitHub stars](https://img.shields.io/github/stars/cakephp/bake?style=flat)](https://github.com/cakephp/bake/stargazers) - Provides code generation functionality.
- [BootstrapUI plugin](https://github.com/friendsofcake/bootstrap-ui) [![GitHub stars](https://img.shields.io/github/stars/friendsofcake/bootstrap-ui?style=flat)](https://github.com/friendsofcake/bootstrap-ui/stargazers) - Bootstrap 4/5 integration.
- [CsvView plugin](https://github.com/FriendsOfCake/cakephp-csvview) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/cakephp-csvview?style=flat)](https://github.com/FriendsOfCake/cakephp-csvview/stargazers) - A view class to easily generate CSV.
- [Feed plugin](https://github.com/dereuromark/cakephp-feed) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-feed?style=flat)](https://github.com/dereuromark/cakephp-feed/stargazers) - Containing an RssView class to easily generate (complex) RSS feeds.
- [LatteView plugin](https://github.com/josbeir/cakephp-latte-view) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-latte-view?style=flat)](https://github.com/josbeir/cakephp-latte-view/stargazers) - A plugin providing Latte template engine integration.
- [Meta plugin](https://github.com/dereuromark/cakephp-meta) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-meta?style=flat)](https://github.com/dereuromark/cakephp-meta/stargazers) - Makes handling meta tags and SEO-relevant HTML markup DRY and easy.
- [TailwindUi plugin](https://github.com/dereuromark/cakephp-tailwind-ui) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tailwind-ui?style=flat)](https://github.com/dereuromark/cakephp-tailwind-ui/stargazers) - Tailwind CSS / DaisyUI (or KTUI/Metronic) integration for form, pagination, flash, and breadcrumb helpers.
- [TemplaterDefaults plugin](https://github.com/josbeir/cakephp-templater-defaults) [![GitHub stars](https://img.shields.io/github/stars/josbeir/cakephp-templater-defaults?style=flat)](https://github.com/josbeir/cakephp-templater-defaults/stargazers) - Allows the use of default HTML attributes within CakePHP's string template system.
- [Templating](https://github.com/dereuromark/cakephp-templating) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-templating?style=flat)](https://github.com/dereuromark/cakephp-templating/stargazers) - HTML snippets as value objects, (Font) icons, and templating topics.
- [Tools:Tree](https://github.com/dereuromark/cakephp-tools) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tools?style=flat)](https://github.com/dereuromark/cakephp-tools/stargazers) - Tree helper to work with Core Tree behavior and handle tree structure output.
- [TwigView plugin](https://github.com/cakephp/twig-view) [![GitHub stars](https://img.shields.io/github/stars/cakephp/twig-view?style=flat)](https://github.com/cakephp/twig-view/stargazers) - A plugin to use the Twig Templating Language for views.
- [XlsView plugin](https://github.com/impronta48/cakephp-xlsview) [![GitHub stars](https://img.shields.io/github/stars/impronta48/cakephp-xlsview?style=flat)](https://github.com/impronta48/cakephp-xlsview/stargazers) - A view class to easily generate XLS using PHPSpreadsheet.

### Testing
*Plugins/Tools for testing codebases and generating test data.*

- [CakePHP CodeSniffer rules](https://github.com/cakephp/cakephp-codesniffer) [![GitHub stars](https://img.shields.io/github/stars/cakephp/cakephp-codesniffer?style=flat)](https://github.com/cakephp/cakephp-codesniffer/stargazers) - The official CakePHP CS rules.
- [CakephpFixtureFactories plugin](https://github.com/dereuromark/cakephp-fixture-factories) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-fixture-factories?style=flat)](https://github.com/dereuromark/cakephp-fixture-factories/stargazers) - Create your fixtures dynamically on a test basis, accelerate the writing and maintenance of your tests.
- [FriendsOfCake/Fixturize plugin](https://github.com/FriendsOfCake/fixturize) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/fixturize?style=flat)](https://github.com/FriendsOfCake/fixturize/stargazers) - More efficient inserting fixtures when running test suites by decreasing amount of inserts (MySQL only).

### Third Party APIs
*Accessing third party APIs.*


## Software

*Software for creating a development environment.*

### Development Environment
*Software and tools for creating a sandboxed development environment.*

- [CakePHP Docker](https://github.com/cnizzardini/cakephp-docker) [![GitHub stars](https://img.shields.io/github/stars/cnizzardini/cakephp-docker?style=flat)](https://github.com/cnizzardini/cakephp-docker/stargazers) - A cakephp/app template for Docker.
- [CakePHP Vagrant Setup](https://github.com/cpierce/cakephp-vagrant-setup) [![GitHub stars](https://img.shields.io/github/stars/cpierce/cakephp-vagrant-setup?style=flat)](https://github.com/cpierce/cakephp-vagrant-setup/stargazers) - Tool for spinning up multiple CakePHP vanilla dev environments using Vagrant.
- [CakePHP Docker Setup](https://github.com/cpierce/cakephp-docker-setup) [![GitHub stars](https://img.shields.io/github/stars/cpierce/cakephp-docker-setup?style=flat)](https://github.com/cpierce/cakephp-docker-setup/stargazers) - Tool for spinning up multiple CakePHP vanilla dev environments using Docker.
- [DDEV](https://ddev.readthedocs.io/en/stable/) - Docker based local env.
- [Devilbox](https://devilbox.readthedocs.io/en/latest/) - A Docker development environment for (CakePHP) apps to be auto-setup including a lot of tools.
- [Docker](https://github.com/stefanvangastel/docker-cakephp) [![GitHub stars](https://img.shields.io/github/stars/stefanvangastel/docker-cakephp?style=flat)](https://github.com/stefanvangastel/docker-cakephp/stargazers) - CakePHP in a Docker container environment.
- [Galley](https://gitlab.com/amayer5125/galley) - A small Docker dev environment for CakePHP development which includes a simple command line utility.
- [NetBeans](https://github.com/junichi11/cakephp3-netbeans) [![GitHub stars](https://img.shields.io/github/stars/junichi11/cakephp3-netbeans?style=flat)](https://github.com/junichi11/cakephp3-netbeans/stargazers) - This package provides support for CakePHP in NetBeans 8.1+.
- [Puppet](https://puppetlabs.com/) - A server automation framework and application.
- [Vagrant](https://developer.hashicorp.com/vagrant) - A portable development environment utility.

IDE specific compatibility information and tips can be found [here](https://github.com/dereuromark/cakephp-ide-helper/wiki#ide-support-and-tips).

### Web Applications

- [Toolbox](https://toolbox.dereuromark.de) - Online toolbox with useful tools for modern CakePHP apps. Powers the awesome CI/linter.

### CMS and applications built on CakePHP

- [baserCMS](https://github.com/baserproject/basercms) [![GitHub stars](https://img.shields.io/github/stars/baserproject/basercms?style=flat)](https://github.com/baserproject/basercms/stargazers) - This is a website development framework with RESTful APIs. Installable as a plugin for CakePHP.

### Demo

*Web-based (demo) applications and tools.*

- [BlogMVC](https://github.com/Kareylo/BlogMVC-CakePHP3) [![GitHub stars](https://img.shields.io/github/stars/Kareylo/BlogMVC-CakePHP3?style=flat)](https://github.com/Kareylo/BlogMVC-CakePHP3/stargazers) - A simple Blog example with CakePHP based on [BlogMVC Project](https://github.com/Grafikart/BlogMVC) [![GitHub stars](https://img.shields.io/github/stars/Grafikart/BlogMVC?style=flat)](https://github.com/Grafikart/BlogMVC/stargazers).
- [Bookmarkr](https://github.com/lorenzo/cakephp3-bookmarkr) [![GitHub stars](https://img.shields.io/github/stars/lorenzo/cakephp3-bookmarkr?style=flat)](https://github.com/lorenzo/cakephp3-bookmarkr/stargazers) - A bookmarking application built with the CRUD plugin.
- [Fluentd + Grafana Loki demo application](https://github.com/ishanvyas22/cakephp-loki-demo) [![GitHub stars](https://img.shields.io/github/stars/ishanvyas22/cakephp-loki-demo?style=flat)](https://github.com/ishanvyas22/cakephp-loki-demo/stargazers) - A demo application to send CakePHP Docker container logs to [Grafana Loki](https://grafana.com/) via [Fluentd](https://www.fluentd.org/).
- [RealWorld](https://github.com/gothinkster/cakephp-realworld-example-app) [![GitHub stars](https://img.shields.io/github/stars/gothinkster/cakephp-realworld-example-app?style=flat)](https://github.com/gothinkster/cakephp-realworld-example-app/stargazers) - Example CakePHP codebase containing real world examples (CRUD, auth, advanced patterns and more) that adheres to the [RealWorld](https://github.com/gothinkster/realworld-example-apps) [![GitHub stars](https://img.shields.io/github/stars/gothinkster/realworld-example-apps?style=flat)](https://github.com/gothinkster/realworld-example-apps/stargazers) spec and API.
- [Sandbox](https://sandbox.dereuromark.de) - A sandbox CakePHP application with lots of demos and plugin showcasings.
- [TinyAuth demo](https://github.com/dereuromark/cakephp-tinyauth-demo) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/cakephp-tinyauth-demo?style=flat)](https://github.com/dereuromark/cakephp-tinyauth-demo/stargazers) - Full interactivate auth (TinyAuth incl. Authentication and Authorization core plugins) demo.
- [Query examples](https://github.com/lorenzo/cakephp3-examples) [![GitHub stars](https://img.shields.io/github/stars/lorenzo/cakephp3-examples?style=flat)](https://github.com/lorenzo/cakephp3-examples/stargazers) - Advanced query building examples.
- [Xeta](https://github.com/XetaIO/Xeta) [![GitHub stars](https://img.shields.io/github/stars/XetaIO/Xeta?style=flat)](https://github.com/XetaIO/Xeta/stargazers) - A resource to help people starting with CakePHP.
- [Vue.js demo app](https://github.com/ishanvyas22/cakephpvue-spa) [![GitHub stars](https://img.shields.io/github/stars/ishanvyas22/cakephpvue-spa?style=flat)](https://github.com/ishanvyas22/cakephpvue-spa/stargazers) - A CakePHP + Vue.js single page application skeleton.

## Resources

Various resources, such as books, websites and articles, for improving your CakePHP development skills and knowledge.

### Help
*Where to get help.*

- [Official CakePHP Forum](https://discourse.cakephp.org/) - This is for generic questions and alike.
- [stackoverflow.com/questions/tagged/cakephp](https://stackoverflow.com/questions/tagged/cakephp) - This is for specific questions, ideally along with some example code.

### CakePHP Websites
*Useful and current CakePHP-related websites and blogs.*

- [CakeDC](https://www.cakedc.com/articles) - Articles around CakePHP.
- [dereuromark.de](https://www.dereuromark.de) - An extensive CakePHP core dev blog.
- [josediazgonzalez.com](https://josediazgonzalez.com/) - A mainly CakePHP related core dev blog.
- [mark-story.com](https://mark-story.com) - CakePHP lead dev blog.

### CakePHP Books and Articles
*Fantastic CakePHP-related (e)books and other reading material.*

### CakePHP Videos
*Fantastic CakePHP-related videos.*

- [CakePHP](https://www.youtube.com/user/CakePHP) - Channel about CakePHP videos.


### CakePHP Tutorials
*Must-do tutorials.*

- [Official Content Management Tutorial](https://book.cakephp.org/5/en/tutorials-and-examples/cms/installation.html)

### CakePHP Reading and Listening
*Documentation and CakePHP-related reading and listening materials.*

- [CakePHP Cookbook(!)](https://book.cakephp.org/) - The official CakePHP documentation.

### CakePHP Internals Reading
*Reading materials related to the CakePHP internals and decisions.*

- [Top 10 (and more) core contributors](https://github.com/cakephp/cakephp/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/cakephp/cakephp/graphs/contributors?style=flat)](https://github.com/cakephp/cakephp/graphs/contributors/stargazers) - Give 'em a hand.

## Conferences

### Official
*International conference.*

- [cakefest.org](https://cakefest.org/) - Annual CakePHP Conference.

### MeetUps
*Regional meet-ups.*

- [CakePHP-DE](https://www.meetup.com/CakePHP-DE) - MeetUps in Germany.

## Footnotes
awesome-cakephp has been created by [dereuromark](https://github.com/dereuromark) [![GitHub stars](https://img.shields.io/github/stars/dereuromark?style=flat)](https://github.com/dereuromark/stargazers) and is currently maintained by him and the FriendsOfCake group. Thank you to all [contributors](https://github.com/FriendsOfCake/awesome-cakephp/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfCake/awesome-cakephp/graphs/contributors?style=flat)](https://github.com/FriendsOfCake/awesome-cakephp/graphs/contributors/stargazers), too.
