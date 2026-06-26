# PHP

[![GitHub stars](https://img.shields.io/github/stars/ziadoz/awesome-php?style=flat)](https://github.com/ziadoz/awesome-php/stargazers)

# Awesome PHP [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome PHP libraries, resources, and useful tools.

## Contributing and Collaborating
Please see [CONTRIBUTING](https://github.com/ziadoz/awesome-php/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/ziadoz/awesome-php/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/ziadoz/awesome-php/blob/master/CONTRIBUTING.md/stargazers), [CODE-OF-CONDUCT](https://github.com/ziadoz/awesome-php/blob/master/CODE-OF-CONDUCT.md) [![GitHub stars](https://img.shields.io/github/stars/ziadoz/awesome-php/blob/master/CODE-OF-CONDUCT.md?style=flat)](https://github.com/ziadoz/awesome-php/blob/master/CODE-OF-CONDUCT.md/stargazers) and [COLLABORATING](https://github.com/ziadoz/awesome-php/blob/master/COLLABORATING.md) [![GitHub stars](https://img.shields.io/github/stars/ziadoz/awesome-php/blob/master/COLLABORATING.md?style=flat)](https://github.com/ziadoz/awesome-php/blob/master/COLLABORATING.md/stargazers) for details.

## Table of Contents
- [Awesome PHP](#awesome-php)
  - [Composer Repositories](#composer-repositories)
  - [Dependency Management](#dependency-management)
  - [Dependency Management Extras](#dependency-management-extras)
  - [Frameworks](#frameworks)
  - [Framework Extras](#framework-extras)
  - [Content Management Systems](#content-management-systems-cms)
  - [Components](#components)
  - [Micro Frameworks](#micro-frameworks)
  - [Micro Framework Extras](#micro-framework-extras)
  - [Routers](#routers)
  - [Templating](#templating)
  - [Static Site Generators](#static-site-generators)
  - [HTTP](#http)
  - [Scraping](#scraping)
  - [Middlewares](#middlewares)
  - [URL](#url)
  - [Email](#email)
  - [Files](#files)
  - [Streams](#streams)
  - [Dependency Injection](#dependency-injection)
  - [Imagery](#imagery)
  - [Testing](#testing)
  - [Continuous Integration](#continuous-integration)
  - [Documentation](#documentation)
  - [Security](#security)
  - [Passwords](#passwords)
  - [Code Analysis](#code-analysis)
  - [Code Quality](#code-quality)
  - [Static Analysis](#static-analysis)
  - [Architectural](#architectural)
  - [Debugging and Profiling](#debugging-and-profiling)
  - [Error Tracking and Monitoring Services](#error-tracking-and-monitoring-services)
  - [Build Tools](#build-tools)
  - [Task Runners](#task-runners)
  - [Navigation](#navigation)
  - [Asset Management](#asset-management)
  - [Geolocation](#geolocation)
  - [Date and Time](#date-and-time)
  - [Event](#event)
  - [Logging](#logging)
  - [E-commerce](#e-commerce)
  - [PDF](#pdf)
  - [Office](#office)
  - [Database](#database)
  - [Migrations](#migrations)
  - [NoSQL](#nosql)
  - [Queue](#queue)
  - [Search](#search)
  - [Command Line](#command-line)
  - [Authentication and Authorization](#authentication-and-authorization)
  - [Markup and CSS](#markup-and-css)
  - [JSON](#json)
  - [Strings](#strings)
  - [Numbers](#numbers)
  - [Filtering, Sanitizing and Validation](#filtering-sanitizing-and-validation)
  - [API](#api)
  - [Caching and Locking](#caching-and-locking)
  - [Data Structure and Storage](#data-structure-and-storage)
  - [Notifications](#notifications)
  - [Deployment](#deployment)
  - [Internationalisation and Localisation](#internationalisation-and-localisation)
  - [Serverless](#serverless)
  - [Configuration](#configuration)
  - [LLMs](#llms)
  - [Third Party APIs](#third-party-apis)
  - [Extensions](#extensions)
  - [Miscellaneous](#miscellaneous)
- [Software](#software)
  - [PHP Installation](#php-installation)
  - [Development Environment](#development-environment)
  - [Virtual Machines](#virtual-machines)
  - [Text Editors and IDEs](#text-editors-and-ides)
  - [Web Applications](#web-applications)
  - [Infrastructure](#infrastructure)
- [Resources](#resources)
  - [PHP Websites](#php-websites)
  - [PHP Books](#php-books)
  - [PHP Videos](#php-videos)
  - [PHP Conferences](#php-conferences)
  - [PHP Podcasts](#php-podcasts)
  - [PHP Newsletters](#php-newsletters)
  - [PHP Reading](#php-reading)
  - [PHP Internals Reading](#php-internals-reading)

### Composer Repositories
*Composer Repositories.*

* [Firegento](https://packages.firegento.com/) - Magento Module Composer Repository.
* [Packagist](https://packagist.org/) - The PHP Package Repository.
* [Packalyst](https://packalyst.com/) - The Laravel package repository.
* [Private Packagist](https://packagist.com/) - Composer package archive as a service for PHP.
* [WordPress Packagist](https://wpackagist.org/) - Manage your plugins with Composer.

### Dependency Management
*Libraries for dependency and package management.*

* [Composer](https://getcomposer.org/) - A package and dependency manager.
* [Composer Installers](https://github.com/composer/installers) [![GitHub stars](https://img.shields.io/github/stars/composer/installers?style=flat)](https://github.com/composer/installers/stargazers) - A multi-framework Composer library installer.
* [Phive](https://phar.io/) - A PHAR manager.
* [Pickle](https://github.com/FriendsOfPHP/pickle) [![GitHub stars](https://img.shields.io/github/stars/FriendsOfPHP/pickle?style=flat)](https://github.com/FriendsOfPHP/pickle/stargazers) - A PHP extension installer.
* [Pie](https://github.com/php/pie) [![GitHub stars](https://img.shields.io/github/stars/php/pie?style=flat)](https://github.com/php/pie/stargazers) - The official PHP installer for extensions.

### Dependency Management Extras
*Extras related to dependency management.*

* [Composer Merge Plugin](https://github.com/wikimedia/composer-merge-plugin) [![GitHub stars](https://img.shields.io/github/stars/wikimedia/composer-merge-plugin?style=flat)](https://github.com/wikimedia/composer-merge-plugin/stargazers) - A composer plugin to merge several `composer.json` files.
* [Composer Normalize](https://github.com/ergebnis/composer-normalize) [![GitHub stars](https://img.shields.io/github/stars/ergebnis/composer-normalize?style=flat)](https://github.com/ergebnis/composer-normalize/stargazers) - A plugin for normalizing `composer.json` files.
* [Composer Patches](https://github.com/cweagans/composer-patches) [![GitHub stars](https://img.shields.io/github/stars/cweagans/composer-patches?style=flat)](https://github.com/cweagans/composer-patches/stargazers) - A plugin for Composer to apply patches.
* [Composer Prefer Lowest Validator](https://github.com/dereuromark/composer-prefer-lowest) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/composer-prefer-lowest?style=flat)](https://github.com/dereuromark/composer-prefer-lowest/stargazers) - A plugin to check if minimum dependencies can be installed and tested.
* [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) [![GitHub stars](https://img.shields.io/github/stars/maglnet/ComposerRequireChecker?style=flat)](https://github.com/maglnet/ComposerRequireChecker/stargazers) - CLI tool to analyze composer dependencies and verify that no unknown symbols are used in the sources of a package.
* [Composer Unused](https://github.com/composer-unused/composer-unused) [![GitHub stars](https://img.shields.io/github/stars/composer-unused/composer-unused?style=flat)](https://github.com/composer-unused/composer-unused/stargazers) - A CLI Tool to scan for unused composer packages.
* [Repman](https://repman.io) - A private PHP package repository manager and Packagist proxy.
* [Satis](https://github.com/composer/satis) [![GitHub stars](https://img.shields.io/github/stars/composer/satis?style=flat)](https://github.com/composer/satis/stargazers) - A static Composer repository generator.

### Frameworks
*Web development frameworks.*

* [CakePHP](https://cakephp.org/) - A rapid application development framework.
* [CodeIgniter](https://codeigniter.com/) - A powerful PHP framework with a very small footprint.
* [Ecotone](https://docs.ecotone.tech/) - A Service Bus for PHP based on architectural principles of DDD CQRS and Event Sourcing.
* [Laminas](https://getlaminas.org/) - A framework comprised of individual components (previously Zend Framework).
* [Laravel](https://laravel.com/) - A web application framework with expressive, elegant syntax.
* [Nette](https://nette.org) - A web framework comprised of mature components.
* [Phalcon](https://phalcon.io/en-us) - A framework implemented as a C extension.
* [Spiral](https://spiral.dev/) - A high-performance PHP/Go framework.
* [Symfony](https://symfony.com/) - A set of reusable components and a web framework.
* [Tempest](https://github.com/tempestphp/tempest-framework) [![GitHub stars](https://img.shields.io/github/stars/tempestphp/tempest-framework?style=flat)](https://github.com/tempestphp/tempest-framework/stargazers) - A framework that gets out of your way.
* [Yii2](https://github.com/yiisoft/yii2/) [![GitHub stars](https://img.shields.io/github/stars/yiisoft/yii2/?style=flat)](https://github.com/yiisoft/yii2//stargazers) - A fast, secure, and efficient web framework.

### Framework Extras
*Extras related to web development frameworks.*

* [CakePHP CRUD](https://github.com/friendsofcake/crud) [![GitHub stars](https://img.shields.io/github/stars/friendsofcake/crud?style=flat)](https://github.com/friendsofcake/crud/stargazers) - A Rapid Application Development (RAD) plugin for CakePHP.
* [Filament PHP](https://filamentphp.com/) - A powerful open source UI framework for Laravel.
* [Inertia.js](https://inertiajs.com/) - An adapter for building single-page applications using server-side routing and controllers, without a separate API.
* [LaravelS](https://github.com/hhxsv5/laravel-s) [![GitHub stars](https://img.shields.io/github/stars/hhxsv5/laravel-s?style=flat)](https://github.com/hhxsv5/laravel-s/stargazers) - An out-of-the-box adapter between Laravel/Lumen and Swoole.
* [Livewire](https://livewire.laravel.com/) - Powerful, dynamic, front-end UIs without leaving PHP.

### Content Management Systems (CMS)
*Tools for managing digital content.*

* [Backdrop](https://backdropcms.org) - A CMS targeting small-to-medium-sized business and non-profits (a fork of Drupal).
* [Concrete5](https://www.concretecms.com/) - A CMS targeting users with a minimum of technical skills.
* [CraftCMS](https://github.com/craftcms/cms) [![GitHub stars](https://img.shields.io/github/stars/craftcms/cms?style=flat)](https://github.com/craftcms/cms/stargazers) - A flexible, user-friendly CMS for creating custom digital experiences on the web and beyond.
* [Drupal](https://new.drupal.org/home) - An enterprise level CMS.
* [Grav](https://github.com/getgrav/grav) [![GitHub stars](https://img.shields.io/github/stars/getgrav/grav?style=flat)](https://github.com/getgrav/grav/stargazers) - A modern flat-file CMS.
* [Joomla](https://www.joomla.org/) - Another leading CMS.
* [Kirby](https://getkirby.com/) - A flat-file CMS that adapts to any project.
* [Magento](https://github.com/magento/magento2) [![GitHub stars](https://img.shields.io/github/stars/magento/magento2?style=flat)](https://github.com/magento/magento2/stargazers) - A widely used open-source e-commerce platform.
* [Moodle](https://moodle.org/) - An open-source learning platform.
* [OctoberCMS](https://octobercms.com/) - A CMS built on Laravel.
* [OpenMage](https://github.com/OpenMage/magento-lts) [![GitHub stars](https://img.shields.io/github/stars/OpenMage/magento-lts?style=flat)](https://github.com/OpenMage/magento-lts/stargazers) - Fork of EoL Magento 1 e-commerce platform.
* [Pico CMS](https://picocms.org/) - A lightweight flat-file CMS.
* [Silverstripe](https://www.silverstripe.org/) - A simple, flexible, and secure CMS.
* [Statamic](https://statamic.com/) - A flat-file and Git-based CMS built on Laravel.
* [Sulu](https://sulu.io/) - A user- and developer-friendly CMS built on the Symfony Framework.
* [TYPO3](https://typo3.org) - An enterprise level CMS.
* [WinterCMS](https://wintercms.com) - A community-maintained fork of OctoberCMS built on Laravel.
* [WordPress](https://github.com/WordPress/WordPress) [![GitHub stars](https://img.shields.io/github/stars/WordPress/WordPress?style=flat)](https://github.com/WordPress/WordPress/stargazers) - A blogging platform and CMS.

### Components
*Standalone components from web development frameworks and development groups.*

* [Aura](https://auraphp.com/) - Independent components, fully decoupled from each other and from any framework.
* [CakePHP Plugins](https://plugins.cakephp.org/) - A directory of CakePHP plugins.
* [Laminas Components](https://docs.laminas.dev/components/) - The components that make the Laminas Framework.
* [Laravel Components](https://github.com/illuminate) [![GitHub stars](https://img.shields.io/github/stars/illuminate?style=flat)](https://github.com/illuminate/stargazers) - The Laravel Framework components.
* [League of Extraordinary Packages](https://thephpleague.com/) - A PHP package development group.
* [Spatie Open Source](https://spatie.be/open-source) - A collection of open-source PHP and Laravel packages.
* [Symfony Packages](https://symfony.com/packages) - Decoupled libraries for PHP applications.

### Micro Frameworks
*Micro frameworks and routers.*

* [Laravel Zero](https://laravel-zero.com) - A micro-framework for console applications.
* [Mezzio](https://getexpressive.org/) - A micro-framework by Laminas.
* [Minicli](https://github.com/minicli/minicli) [![GitHub stars](https://img.shields.io/github/stars/minicli/minicli?style=flat)](https://github.com/minicli/minicli/stargazers) - Minimalist, dependency-free framework for building CLI-centric PHP applications.
* [Silly](https://github.com/mnapoli/silly) [![GitHub stars](https://img.shields.io/github/stars/mnapoli/silly?style=flat)](https://github.com/mnapoli/silly/stargazers) - A micro-framework for CLI applications.
* [Slim](https://www.slimframework.com/) - Another simple micro framework.

### Micro Framework Extras
*Extras related to micro frameworks and routers.*

* [Slim Skeleton](https://github.com/slimphp/Slim-Skeleton) [![GitHub stars](https://img.shields.io/github/stars/slimphp/Slim-Skeleton?style=flat)](https://github.com/slimphp/Slim-Skeleton/stargazers) - A skeleton for Slim.
* [Slim PHP View](https://github.com/slimphp/PHP-View) [![GitHub stars](https://img.shields.io/github/stars/slimphp/PHP-View?style=flat)](https://github.com/slimphp/PHP-View/stargazers) - A simple PHP renderer for Slim.

### Routers
*Libraries for handling application routing.*

* [Aura.Router](https://github.com/auraphp/Aura.Router) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Router?style=flat)](https://github.com/auraphp/Aura.Router/stargazers) - A full-featured routing library.
* [Fast Route](https://github.com/nikic/FastRoute) [![GitHub stars](https://img.shields.io/github/stars/nikic/FastRoute?style=flat)](https://github.com/nikic/FastRoute/stargazers) - A fast routing library.
* [Klein](https://github.com/klein/klein.php) [![GitHub stars](https://img.shields.io/github/stars/klein/klein.php?style=flat)](https://github.com/klein/klein.php/stargazers) - A flexible router.
* [Route](https://github.com/thephpleague/route) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/route?style=flat)](https://github.com/thephpleague/route/stargazers) - A routing library built on top of Fast Route.

### Templating
*Libraries and tools for templating and lexing.*

* [Latte](https://latte.nette.org/) - The safest and truly intuitive templates for PHP.
* [MtHaml](https://github.com/arnaud-lb/MtHaml) [![GitHub stars](https://img.shields.io/github/stars/arnaud-lb/MtHaml?style=flat)](https://github.com/arnaud-lb/MtHaml/stargazers) - A PHP implementation of the HAML template language.
* [Mustache](https://github.com/bobthecow/mustache.php) [![GitHub stars](https://img.shields.io/github/stars/bobthecow/mustache.php?style=flat)](https://github.com/bobthecow/mustache.php/stargazers) - A PHP implementation of the Mustache template language.
* [PHPTAL](https://phptal.org/) - A PHP implementation of the [TAL](https://en.wikipedia.org/wiki/Template_Attribute_Language) templating language.
* [Plates](https://platesphp.com/) - A native PHP templating library.
* [Smarty](https://www.smarty.net/) - A template engine to complement PHP.
* [Twig](https://twig.symfony.com/) - A comprehensive templating language.

### Static Site Generators
*Tools for pre-processing content to generate web pages.*

* [Cecil](https://cecil.app/) - A simple and powerful content-driven static site generator.
* [Couscous](https://couscous.io) - A tool for converting Markdown documentation into websites.
* [Jigsaw](https://jigsaw.tighten.com/) - Simple static sites with Laravel's Blade.
* [Sculpin](https://sculpin.io) - A tool that converts Markdown and Twig into static HTML.

### HTTP
*Libraries for working with HTTP.*

* [Buzz](https://github.com/kriswallsmith/Buzz) [![GitHub stars](https://img.shields.io/github/stars/kriswallsmith/Buzz?style=flat)](https://github.com/kriswallsmith/Buzz/stargazers) - Another HTTP client.
* [Guzzle](https://github.com/guzzle/guzzle) [![GitHub stars](https://img.shields.io/github/stars/guzzle/guzzle?style=flat)](https://github.com/guzzle/guzzle/stargazers) - A comprehensive HTTP client.
* [HTTPlug](https://httplug.io) - An HTTP client abstraction without binding to a specific implementation.
* [Nyholm PSR-7](https://github.com/Nyholm/psr7) [![GitHub stars](https://img.shields.io/github/stars/Nyholm/psr7?style=flat)](https://github.com/Nyholm/psr7/stargazers) - A super lightweight PSR-7 implementation. Very strict and very fast.
* [PHP VCR](https://php-vcr.github.io/) - A library for recording and replaying HTTP requests.
* [Requests](https://github.com/WordPress/Requests) [![GitHub stars](https://img.shields.io/github/stars/WordPress/Requests?style=flat)](https://github.com/WordPress/Requests/stargazers) - A simple HTTP library.
* [Retrofit](https://github.com/tebru/retrofit-php) [![GitHub stars](https://img.shields.io/github/stars/tebru/retrofit-php?style=flat)](https://github.com/tebru/retrofit-php/stargazers) - A library to ease creation of REST API clients.
* [Saloon](https://github.com/saloonphp/saloon) [![GitHub stars](https://img.shields.io/github/stars/saloonphp/saloon?style=flat)](https://github.com/saloonphp/saloon/stargazers) - A framework for building beautiful API integrations and SDKs.
* [Symfony HTTP Client](https://github.com/symfony/http-client) [![GitHub stars](https://img.shields.io/github/stars/symfony/http-client?style=flat)](https://github.com/symfony/http-client/stargazers) - A component to fetch HTTP resources synchronously or asynchronously.
* [Laminas Diactoros](https://github.com/laminas/laminas-diactoros) [![GitHub stars](https://img.shields.io/github/stars/laminas/laminas-diactoros?style=flat)](https://github.com/laminas/laminas-diactoros/stargazers) - PSR-7 HTTP Message implementation.

### Scraping
*Libraries for scraping websites and detecting crawlers.*

* [Chrome PHP](https://github.com/chrome-php/chrome) [![GitHub stars](https://img.shields.io/github/stars/chrome-php/chrome?style=flat)](https://github.com/chrome-php/chrome/stargazers) - Instrument headless Chrome/Chromium instances from PHP.
* [CrawlerDetect](https://github.com/JayBizzle/Crawler-Detect) [![GitHub stars](https://img.shields.io/github/stars/JayBizzle/Crawler-Detect?style=flat)](https://github.com/JayBizzle/Crawler-Detect/stargazers) - A PHP class for detecting bots/crawlers/spiders via the user agent.
* [DiDOM](https://github.com/Imangazaliev/DiDOM) [![GitHub stars](https://img.shields.io/github/stars/Imangazaliev/DiDOM?style=flat)](https://github.com/Imangazaliev/DiDOM/stargazers) - A super-fast HTML scrapper and parser.
* [Embed](https://github.com/php-embed/Embed) [![GitHub stars](https://img.shields.io/github/stars/php-embed/Embed?style=flat)](https://github.com/php-embed/Embed/stargazers) - An information extractor from any web service or page.
* [PHP Spider](https://github.com/mvdbos/php-spider) [![GitHub stars](https://img.shields.io/github/stars/mvdbos/php-spider?style=flat)](https://github.com/mvdbos/php-spider/stargazers) - A configurable and extensible PHP web spider.
* [Symfony Panther](https://github.com/symfony/panther) [![GitHub stars](https://img.shields.io/github/stars/symfony/panther?style=flat)](https://github.com/symfony/panther/stargazers) - A browser testing and web crawling library for PHP and Symfony.

### Middlewares
*Libraries for building application using middlewares.*

* [PSR-15 Middlewares](https://github.com/middlewares/psr15-middlewares) [![GitHub stars](https://img.shields.io/github/stars/middlewares/psr15-middlewares?style=flat)](https://github.com/middlewares/psr15-middlewares/stargazers) - Inspiring collection of handy middlewares.
* [Stack](https://github.com/stackphp) [![GitHub stars](https://img.shields.io/github/stars/stackphp?style=flat)](https://github.com/stackphp/stargazers) - A library of stackable middleware for Symfony.
* [Laminas Stratigility](https://github.com/laminas/laminas-stratigility) [![GitHub stars](https://img.shields.io/github/stars/laminas/laminas-stratigility?style=flat)](https://github.com/laminas/laminas-stratigility/stargazers) - Middleware for PHP built on top of PSR-7.

### URL
*Libraries for parsing URLs.*

* [PHP Domain Parser](https://github.com/jeremykendall/php-domain-parser) [![GitHub stars](https://img.shields.io/github/stars/jeremykendall/php-domain-parser?style=flat)](https://github.com/jeremykendall/php-domain-parser/stargazers) - A domain suffix parser library.
* [sabre/uri](https://github.com/sabre-io/uri) [![GitHub stars](https://img.shields.io/github/stars/sabre-io/uri?style=flat)](https://github.com/sabre-io/uri/stargazers) - A functional URI manipulation library.
* [Uri](https://github.com/thephpleague/uri) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/uri?style=flat)](https://github.com/thephpleague/uri/stargazers) - Another URL manipulation library.

### Email
*Libraries for sending and parsing email.*

* [CssToInlineStyles](https://github.com/tijsverkoyen/CssToInlineStyles) [![GitHub stars](https://img.shields.io/github/stars/tijsverkoyen/CssToInlineStyles?style=flat)](https://github.com/tijsverkoyen/CssToInlineStyles/stargazers) - A library to inline CSS in email templates.
* [ddeboer/imap](https://github.com/ddeboer/imap) [![GitHub stars](https://img.shields.io/github/stars/ddeboer/imap?style=flat)](https://github.com/ddeboer/imap/stargazers) - Object-oriented, fully tested PHP IMAP library.
* [Email Reply Parser](https://github.com/willdurand/EmailReplyParser) [![GitHub stars](https://img.shields.io/github/stars/willdurand/EmailReplyParser?style=flat)](https://github.com/willdurand/EmailReplyParser/stargazers) - An email reply parser library.
* [Fetch](https://github.com/tedious/Fetch) [![GitHub stars](https://img.shields.io/github/stars/tedious/Fetch?style=flat)](https://github.com/tedious/Fetch/stargazers) - An IMAP library.
* [Mautic](https://github.com/mautic/mautic) [![GitHub stars](https://img.shields.io/github/stars/mautic/mautic?style=flat)](https://github.com/mautic/mautic/stargazers) - Email marketing automation.
* [PHPMailer](https://github.com/PHPMailer/PHPMailer) [![GitHub stars](https://img.shields.io/github/stars/PHPMailer/PHPMailer?style=flat)](https://github.com/PHPMailer/PHPMailer/stargazers) - Another mailer solution.
* [Stampie](https://github.com/Stampie/Stampie) [![GitHub stars](https://img.shields.io/github/stars/Stampie/Stampie?style=flat)](https://github.com/Stampie/Stampie/stargazers) - A library for email services such as [SendGrid](https://www.twilio.com/en-us/sendgrid), [PostMark](https://postmarkapp.com), [MailGun](https://www.mailgun.com/) and [MailChimp](https://mailchimp.com/features/transactional-email/).
* [Symfony Mailer](https://github.com/symfony/mailer) [![GitHub stars](https://img.shields.io/github/stars/symfony/mailer?style=flat)](https://github.com/symfony/mailer/stargazers) - A powerful library for creating and sending emails.

### Files
*Libraries for file manipulation and MIME type detection.*

* [CSV](https://github.com/thephpleague/csv) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/csv?style=flat)](https://github.com/thephpleague/csv/stargazers) - A CSV data manipulation library.
* [Flysystem](https://github.com/thephpleague/Flysystem) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/Flysystem?style=flat)](https://github.com/thephpleague/Flysystem/stargazers) - Abstraction for local and remote filesystems.
* [Gaufrette](https://github.com/KnpLabs/Gaufrette) [![GitHub stars](https://img.shields.io/github/stars/KnpLabs/Gaufrette?style=flat)](https://github.com/KnpLabs/Gaufrette/stargazers) - A filesystem abstraction layer.
* [PHP FFmpeg](https://github.com/PHP-FFmpeg/PHP-FFmpeg/) [![GitHub stars](https://img.shields.io/github/stars/PHP-FFmpeg/PHP-FFmpeg/?style=flat)](https://github.com/PHP-FFmpeg/PHP-FFmpeg//stargazers) - A wrapper for the [FFmpeg](https://www.ffmpeg.org/) video library.
* [UnifiedArchive](https://github.com/wapmorgan/UnifiedArchive) [![GitHub stars](https://img.shields.io/github/stars/wapmorgan/UnifiedArchive?style=flat)](https://github.com/wapmorgan/UnifiedArchive/stargazers) - A unified reader and writer of compressed archives.
* [Parquet](https://github.com/flow-php/parquet) [![GitHub stars](https://img.shields.io/github/stars/flow-php/parquet?style=flat)](https://github.com/flow-php/parquet/stargazers) - PHP implementation of Parquet file format.

### Streams
*Libraries for working with streams.*

* [ByteStream](https://amphp.org/byte-stream) - An asynchronous stream abstraction.

### Dependency Injection
*Libraries that implement the dependency injection design pattern.*

* [Aura.Di](https://github.com/auraphp/Aura.Di) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Di?style=flat)](https://github.com/auraphp/Aura.Di/stargazers) - A serializable dependency injection container with constructor and setter injection, interface and trait awareness, configuration inheritance, and much more.
* [Acclimate](https://github.com/AcclimateContainer/acclimate-container) [![GitHub stars](https://img.shields.io/github/stars/AcclimateContainer/acclimate-container?style=flat)](https://github.com/AcclimateContainer/acclimate-container/stargazers) - A common interface to dependency injection containers and service locators.
* [Auryn](https://github.com/rdlowrey/Auryn) [![GitHub stars](https://img.shields.io/github/stars/rdlowrey/Auryn?style=flat)](https://github.com/rdlowrey/Auryn/stargazers) - A recursive dependency injector.
* [Container](https://github.com/thephpleague/container) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/container?style=flat)](https://github.com/thephpleague/container/stargazers) - Another flexible dependency injection container.
* [Disco](https://github.com/bitExpert/disco) [![GitHub stars](https://img.shields.io/github/stars/bitExpert/disco?style=flat)](https://github.com/bitExpert/disco/stargazers) - A PSR-11 compatible, annotation-based dependency injection container.
* [PHP-DI](https://php-di.org/) - A dependency injection container that supports autowiring.
* [Pimple](https://github.com/silexphp/Pimple) [![GitHub stars](https://img.shields.io/github/stars/silexphp/Pimple?style=flat)](https://github.com/silexphp/Pimple/stargazers) - A tiny dependency injection container.
* [Symfony DI](https://github.com/symfony/dependency-injection) [![GitHub stars](https://img.shields.io/github/stars/symfony/dependency-injection?style=flat)](https://github.com/symfony/dependency-injection/stargazers) - A dependency injection container component.

### Imagery
*Libraries for manipulating images.*

* [Color Extractor](https://github.com/thephpleague/color-extractor) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/color-extractor?style=flat)](https://github.com/thephpleague/color-extractor/stargazers) - A library for extracting colours from images.
* [Glide](https://github.com/thephpleague/glide) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/glide?style=flat)](https://github.com/thephpleague/glide/stargazers) - An on-demand image manipulation library.
* [Image Hash](https://github.com/jenssegers/imagehash) [![GitHub stars](https://img.shields.io/github/stars/jenssegers/imagehash?style=flat)](https://github.com/jenssegers/imagehash/stargazers) - A library for generating perceptual image hashes.
* [Image Optimizer](https://github.com/psliwa/image-optimizer) [![GitHub stars](https://img.shields.io/github/stars/psliwa/image-optimizer?style=flat)](https://github.com/psliwa/image-optimizer/stargazers) - A library for optimizing images.
* [Imagine](https://imagine.readthedocs.io/en/latest/index.html) - An image manipulation library.
* [Intervention Image](https://github.com/Intervention/image) [![GitHub stars](https://img.shields.io/github/stars/Intervention/image?style=flat)](https://github.com/Intervention/image/stargazers) - Another image manipulation library.
* [PHP Image Workshop](https://github.com/Sybio/ImageWorkshop) [![GitHub stars](https://img.shields.io/github/stars/Sybio/ImageWorkshop?style=flat)](https://github.com/Sybio/ImageWorkshop/stargazers) - Another image manipulation library.
* [PHP QR Code](https://github.com/chillerlan/php-qrcode/) [![GitHub stars](https://img.shields.io/github/stars/chillerlan/php-qrcode/?style=flat)](https://github.com/chillerlan/php-qrcode//stargazers) - QR Code generator and reader.

### Testing
*Libraries for testing codebases and generating test data.*

* [Alice](https://github.com/nelmio/alice) [![GitHub stars](https://img.shields.io/github/stars/nelmio/alice?style=flat)](https://github.com/nelmio/alice/stargazers) - An expressive fixture generation library.
* [Behat](https://docs.behat.org/en/latest/) - A behaviour driven development (BDD) testing framework.
* [Codeception](https://github.com/Codeception/Codeception) [![GitHub stars](https://img.shields.io/github/stars/Codeception/Codeception?style=flat)](https://github.com/Codeception/Codeception/stargazers) - A full stack testing framework.
* [Faker](https://github.com/fakerphp/faker) [![GitHub stars](https://img.shields.io/github/stars/fakerphp/faker?style=flat)](https://github.com/fakerphp/faker/stargazers) - A fake data generator library.
* [Foundry](https://github.com/zenstruck/foundry) [![GitHub stars](https://img.shields.io/github/stars/zenstruck/foundry?style=flat)](https://github.com/zenstruck/foundry/stargazers) - A fixture factory generation library for Doctrine.
* [Infection](https://github.com/infection/infection) [![GitHub stars](https://img.shields.io/github/stars/infection/infection?style=flat)](https://github.com/infection/infection/stargazers) - An AST-based PHP Mutation testing framework.
* [Kahlan](https://github.com/kahlan/kahlan) [![GitHub stars](https://img.shields.io/github/stars/kahlan/kahlan?style=flat)](https://github.com/kahlan/kahlan/stargazers) - Full stack Unit/BDD testing framework with built-in stub, mock and code-coverage support.
* [Mink](https://mink.behat.org/en/latest/) - Web acceptance testing.
* [Mockery](https://github.com/mockery/mockery) [![GitHub stars](https://img.shields.io/github/stars/mockery/mockery?style=flat)](https://github.com/mockery/mockery/stargazers) - A mock object library for testing.
* [Nette Tester](https://github.com/nette/tester) [![GitHub stars](https://img.shields.io/github/stars/nette/tester?style=flat)](https://github.com/nette/tester/stargazers) - A productive and enjoyable parallel unit testing framework.
* [ParaTest](https://github.com/paratestphp/paratest) [![GitHub stars](https://img.shields.io/github/stars/paratestphp/paratest?style=flat)](https://github.com/paratestphp/paratest/stargazers) - A parallel testing library for PHPUnit.
* [Pest](https://pestphp.com/) - A testing framework with a focus on simplicity.
* [Phake](https://github.com/phake/phake) [![GitHub stars](https://img.shields.io/github/stars/phake/phake?style=flat)](https://github.com/phake/phake/stargazers) - Another mock object library for testing.
* [PHP-Mock](https://github.com/php-mock/php-mock) [![GitHub stars](https://img.shields.io/github/stars/php-mock/php-mock?style=flat)](https://github.com/php-mock/php-mock/stargazers) - A mock library for built-in PHP functions (e.g. time()).
* [PHP MySQL Engine](https://github.com/vimeo/php-mysql-engine) [![GitHub stars](https://img.shields.io/github/stars/vimeo/php-mysql-engine?style=flat)](https://github.com/vimeo/php-mysql-engine/stargazers) - A MySQL engine written in pure PHP.
* [PHPSpec](https://github.com/phpspec/phpspec) [![GitHub stars](https://img.shields.io/github/stars/phpspec/phpspec?style=flat)](https://github.com/phpspec/phpspec/stargazers) - A design by specification unit testing library.
* [PHPT](https://php.github.io/php-src/miscellaneous/writing-tests.html) - A test tool used by PHP itself.
* [PHPUnit](https://github.com/sebastianbergmann/phpunit) [![GitHub stars](https://img.shields.io/github/stars/sebastianbergmann/phpunit?style=flat)](https://github.com/sebastianbergmann/phpunit/stargazers) - A unit testing framework.
* [PHPUnit Polyfills](https://github.com/Yoast/PHPUnit-Polyfills/) [![GitHub stars](https://img.shields.io/github/stars/Yoast/PHPUnit-Polyfills/?style=flat)](https://github.com/Yoast/PHPUnit-Polyfills//stargazers) - Simplifies running PHPUnit tests on multiple PHPUnit versions.
* [Prophecy](https://github.com/phpspec/prophecy) [![GitHub stars](https://img.shields.io/github/stars/phpspec/prophecy?style=flat)](https://github.com/phpspec/prophecy/stargazers) - A highly opinionated mocking framework.
* [VFS Stream](https://github.com/bovigo/vfsStream) [![GitHub stars](https://img.shields.io/github/stars/bovigo/vfsStream?style=flat)](https://github.com/bovigo/vfsStream/stargazers) - A virtual filesystem stream wrapper for testing.

### Continuous Integration
*Libraries and applications for continuous integration.*

* [CircleCI](https://circleci.com) - A continuous integration platform.
* [GitLab CI](https://about.gitlab.com/solutions/continuous-integration/) - A continuous integration platform.
* [Jenkins](https://www.jenkins.io/) - A continuous integration platform with [PHP support](https://www.jenkins.io/solutions/php/).
* [SemaphoreCI](https://semaphore.io/) - A continuous integration platform for open-source and private projects.
* [Travis CI](https://www.travis-ci.com) - A continuous integration platform.
* [Setup PHP](https://github.com/shivammathur/setup-php) [![GitHub stars](https://img.shields.io/github/stars/shivammathur/setup-php?style=flat)](https://github.com/shivammathur/setup-php/stargazers) - A GitHub Action for PHP.

### Documentation
*Libraries for generating project documentation.*

* [APIGen](https://github.com/apigen/apigen) [![GitHub stars](https://img.shields.io/github/stars/apigen/apigen?style=flat)](https://github.com/apigen/apigen/stargazers) - Another API documentation generator.
* [daux.io](https://github.com/dauxio/daux.io) [![GitHub stars](https://img.shields.io/github/stars/dauxio/daux.io?style=flat)](https://github.com/dauxio/daux.io/stargazers) - A documentation generator that uses Markdown files.
* [phpDocumentor](https://phpdoc.org/) - A documentation generator.
* [Scramble](https://github.com/dedoc/scramble) [![GitHub stars](https://img.shields.io/github/stars/dedoc/scramble?style=flat)](https://github.com/dedoc/scramble/stargazers) - Automatically generates OpenAPI documentation from your code without annotations.
* [zircote/swagger-php](https://github.com/zircote/swagger-php) [![GitHub stars](https://img.shields.io/github/stars/zircote/swagger-php?style=flat)](https://github.com/zircote/swagger-php/stargazers) - Generate OpenAPI documentation for your RESTful API.

### Security
*Libraries for generating secure random numbers, encrypting data and scanning and testing for vulnerabilities.*

* [AntiXSS](https://github.com/voku/anti-xss) [![GitHub stars](https://img.shields.io/github/stars/voku/anti-xss?style=flat)](https://github.com/voku/anti-xss/stargazers) - A library that tries to preventing Cross-Site Scripting (XSS) attacks by blacklisting.
* [Halite](https://paragonie.com/project/halite) - A simple library for encryption using [libsodium](https://github.com/jedisct1/libsodium) [![GitHub stars](https://img.shields.io/github/stars/jedisct1/libsodium?style=flat)](https://github.com/jedisct1/libsodium/stargazers).
* [Optimus](https://github.com/jenssegers/optimus) [![GitHub stars](https://img.shields.io/github/stars/jenssegers/optimus?style=flat)](https://github.com/jenssegers/optimus/stargazers) - Id obfuscation based on Knuth's multiplicative hashing method.
* [OWASP](https://owasp.org/) - Explore the world of cyber security.
* [PHPGGC](https://github.com/ambionics/phpggc) [![GitHub stars](https://img.shields.io/github/stars/ambionics/phpggc?style=flat)](https://github.com/ambionics/phpggc/stargazers) - A library of PHP unserializable payloads along with a tool to generate them.
* [PHP Encryption](https://github.com/defuse/php-encryption) [![GitHub stars](https://img.shields.io/github/stars/defuse/php-encryption?style=flat)](https://github.com/defuse/php-encryption/stargazers) - Secure PHP Encryption Library.
* [PHPSecLib](https://github.com/phpseclib/phpseclib) [![GitHub stars](https://img.shields.io/github/stars/phpseclib/phpseclib?style=flat)](https://github.com/phpseclib/phpseclib/stargazers) - A pure PHP secure communications library.
* [Roave Security Advisories](https://github.com/Roave/SecurityAdvisories) [![GitHub stars](https://img.shields.io/github/stars/Roave/SecurityAdvisories?style=flat)](https://github.com/Roave/SecurityAdvisories/stargazers) - This package ensures that your application doesn't have installed dependencies with known security vulnerabilities.
* [Secure Headers](https://github.com/BePsvPT/secure-headers) [![GitHub stars](https://img.shields.io/github/stars/BePsvPT/secure-headers?style=flat)](https://github.com/BePsvPT/secure-headers/stargazers) - A package that adds security related headers to HTTP response.
* [SQLMap](https://github.com/sqlmapproject/sqlmap) [![GitHub stars](https://img.shields.io/github/stars/sqlmapproject/sqlmap?style=flat)](https://github.com/sqlmapproject/sqlmap/stargazers) - An automatic SQL injection and database takeover tool.
* [Zap](https://github.com/zaproxy/zaproxy) [![GitHub stars](https://img.shields.io/github/stars/zaproxy/zaproxy?style=flat)](https://github.com/zaproxy/zaproxy/stargazers) - An integrated penetration testing tool for web applications.

### Passwords
*Libraries and tools for working with and storing passwords.*

* [GenPhrase](https://github.com/timoh6/GenPhrase) [![GitHub stars](https://img.shields.io/github/stars/timoh6/GenPhrase?style=flat)](https://github.com/timoh6/GenPhrase/stargazers) - A library for generating secure random passphrases.
* [Password Validator](https://github.com/jeremykendall/password-validator) [![GitHub stars](https://img.shields.io/github/stars/jeremykendall/password-validator?style=flat)](https://github.com/jeremykendall/password-validator/stargazers) - A library for validating and upgrading password hashes.
* [Password-Generator](https://github.com/hackzilla/password-generator) [![GitHub stars](https://img.shields.io/github/stars/hackzilla/password-generator?style=flat)](https://github.com/hackzilla/password-generator/stargazers) - PHP library to generate random passwords.
* [phpass](https://www.openwall.com/phpass/) - A portable password hashing framework.
* [Zxcvbn PHP](https://github.com/bjeavons/zxcvbn-php) [![GitHub stars](https://img.shields.io/github/stars/bjeavons/zxcvbn-php?style=flat)](https://github.com/bjeavons/zxcvbn-php/stargazers) - A realistic PHP password strength estimate library based on Zxcvbn JS.

### Code Analysis
*Libraries and tools for analysing, parsing and manipulating codebases.*

* [Better Reflection](https://github.com/Roave/BetterReflection) [![GitHub stars](https://img.shields.io/github/stars/Roave/BetterReflection?style=flat)](https://github.com/Roave/BetterReflection/stargazers) - An AST-based reflection library that allows analysis and manipulation of code.
* [Bladestan](https://github.com/bladestan/bladestan) [![GitHub stars](https://img.shields.io/github/stars/bladestan/bladestan?style=flat)](https://github.com/bladestan/bladestan/stargazers) - A PHPStan extension for static analysis of Blade templates.
* [Code Climate](https://codeclimate.com) - An automated code review.
* [Editorconfig-Checker](https://github.com/editorconfig-checker/editorconfig-checker.php) [![GitHub stars](https://img.shields.io/github/stars/editorconfig-checker/editorconfig-checker.php?style=flat)](https://github.com/editorconfig-checker/editorconfig-checker.php/stargazers) - A command line utility which verifies that your files implement your `.editorconfig` rules.
* [GrumPHP](https://github.com/phpro/grumphp) [![GitHub stars](https://img.shields.io/github/stars/phpro/grumphp?style=flat)](https://github.com/phpro/grumphp/stargazers) - A PHP code-quality tool.
* [PHP AST Viewer](https://php-ast-viewer.com/) - A tool for viewing the Abstract Syntax Tree of PHP code.
* [PHP Magic Number Detector](https://github.com/povils/phpmnd) [![GitHub stars](https://img.shields.io/github/stars/povils/phpmnd?style=flat)](https://github.com/povils/phpmnd/stargazers) - A library that detects magic numbers in code.
* [PHP Parser](https://github.com/nikic/PHP-Parser) [![GitHub stars](https://img.shields.io/github/stars/nikic/PHP-Parser?style=flat)](https://github.com/nikic/PHP-Parser/stargazers) - A PHP parser written in PHP.
* [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) [![GitHub stars](https://img.shields.io/github/stars/tomzx/php-semver-checker?style=flat)](https://github.com/tomzx/php-semver-checker/stargazers) - A command line utility that compares two source sets and determines the appropriate semantic versioning to apply.
* [Phpactor](https://github.com/phpactor/phpactor) [![GitHub stars](https://img.shields.io/github/stars/phpactor/phpactor?style=flat)](https://github.com/phpactor/phpactor/stargazers) - PHP completion, refactoring and introspection tool.
* [PHPQA](https://github.com/EdgedesignCZ/phpqa) [![GitHub stars](https://img.shields.io/github/stars/EdgedesignCZ/phpqa?style=flat)](https://github.com/EdgedesignCZ/phpqa/stargazers) - A tool for running QA tools (phploc, phpcpd, phpcs, pdepend, phpmd, phpmetrics).
* [Rector](https://github.com/rectorphp/rector) [![GitHub stars](https://img.shields.io/github/stars/rectorphp/rector?style=flat)](https://github.com/rectorphp/rector/stargazers) - A tool to upgrade and refactor code.
* [Scrutinizer](https://scrutinizer-ci.com/) - A web tool to [scrutinise PHP code](https://github.com/scrutinizer-ci/php-analyzer) [![GitHub stars](https://img.shields.io/github/stars/scrutinizer-ci/php-analyzer?style=flat)](https://github.com/scrutinizer-ci/php-analyzer/stargazers).
* [UBench](https://github.com/devster/ubench) [![GitHub stars](https://img.shields.io/github/stars/devster/ubench?style=flat)](https://github.com/devster/ubench/stargazers) - A simple micro-benchmark library.

### Code Quality
*Libraries for managing code quality, formatting and linting.*

* [CaptainHook](https://github.com/captainhook-git/captainhook) [![GitHub stars](https://img.shields.io/github/stars/captainhook-git/captainhook?style=flat)](https://github.com/captainhook-git/captainhook/stargazers) - An easy-to-use and flexible Git hook library.
* [Laravel Pint](https://github.com/laravel/pint) [![GitHub stars](https://img.shields.io/github/stars/laravel/pint?style=flat)](https://github.com/laravel/pint/stargazers) - A coding standards fixer library for Laravel.
* [PHP CodeSniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) [![GitHub stars](https://img.shields.io/github/stars/PHPCSStandards/PHP_CodeSniffer?style=flat)](https://github.com/PHPCSStandards/PHP_CodeSniffer/stargazers) - A library that detects and can auto-fix PHP, CSS and JS coding standard violations.
* [PHP CS Fixer](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer) [![GitHub stars](https://img.shields.io/github/stars/PHP-CS-Fixer/PHP-CS-Fixer?style=flat)](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer/stargazers) - A coding standards fixer library.
* [PHP CS Fixer Configurator](https://mlocati.github.io/php-cs-fixer-configurator/) - A web application to help configure PHP CS Fixer rule sets.
* [PHP Mess Detector](https://github.com/phpmd/phpmd) [![GitHub stars](https://img.shields.io/github/stars/phpmd/phpmd?style=flat)](https://github.com/phpmd/phpmd/stargazers) - A library that scans code for bugs, sub-optimal code, unused parameters and more.
* [PHPCheckstyle](https://github.com/PHPCheckstyle/phpcheckstyle) [![GitHub stars](https://img.shields.io/github/stars/PHPCheckstyle/phpcheckstyle?style=flat)](https://github.com/PHPCheckstyle/phpcheckstyle/stargazers) - A tool to help adhere to certain coding conventions.

### Static Analysis
*Libraries for performing static analysis of PHP code.*

* [Dead Code Detector](https://github.com/shipmonk-rnd/dead-code-detector) [![GitHub stars](https://img.shields.io/github/stars/shipmonk-rnd/dead-code-detector?style=flat)](https://github.com/shipmonk-rnd/dead-code-detector/stargazers) - A PHPStan extension for finding unused PHP code.
* [Deptrac](https://github.com/deptrac/deptrac) [![GitHub stars](https://img.shields.io/github/stars/deptrac/deptrac?style=flat)](https://github.com/deptrac/deptrac/stargazers) - A static analysis tool for enforcing dependency rules between architectural layers.
* [Exakat](https://github.com/exakat/exakat) [![GitHub stars](https://img.shields.io/github/stars/exakat/exakat?style=flat)](https://github.com/exakat/exakat/stargazers) - A static analysis engine for PHP.
* [Larastan](https://github.com/larastan/larastan) [![GitHub stars](https://img.shields.io/github/stars/larastan/larastan?style=flat)](https://github.com/larastan/larastan/stargazers) - A PHPStan wrapper for Laravel that adds static analysis to Laravel projects.
* [Mago](https://github.com/carthage-software/mago) [![GitHub stars](https://img.shields.io/github/stars/carthage-software/mago?style=flat)](https://github.com/carthage-software/mago/stargazers) - A toolchain for PHP that aims to improve the developer experience.
* [phan](https://github.com/phan/phan) [![GitHub stars](https://img.shields.io/github/stars/phan/phan?style=flat)](https://github.com/phan/phan/stargazers) - A static analyzer based on PHP 7+ and the php-ast extension.
* [PHP Architecture Tester](https://github.com/carlosas/phpat) [![GitHub stars](https://img.shields.io/github/stars/carlosas/phpat?style=flat)](https://github.com/carlosas/phpat/stargazers) - Easy-to-use architecture testing tool for PHP.
* [PHPCompatibility](https://github.com/PHPCompatibility/PHPCompatibility) [![GitHub stars](https://img.shields.io/github/stars/PHPCompatibility/PHPCompatibility?style=flat)](https://github.com/PHPCompatibility/PHPCompatibility/stargazers) - A PHP compatibility checker for PHP CodeSniffer.
* [PHPDoc Parser](https://github.com/phpstan/phpdoc-parser) [![GitHub stars](https://img.shields.io/github/stars/phpstan/phpdoc-parser?style=flat)](https://github.com/phpstan/phpdoc-parser/stargazers) - Next-gen phpDoc parser with support for intersection types and generics.
* [PHP Metrics](https://github.com/phpmetrics/PhpMetrics) [![GitHub stars](https://img.shields.io/github/stars/phpmetrics/PhpMetrics?style=flat)](https://github.com/phpmetrics/PhpMetrics/stargazers) - A static metric library.
* [PHPStan](https://github.com/phpstan/phpstan) [![GitHub stars](https://img.shields.io/github/stars/phpstan/phpstan?style=flat)](https://github.com/phpstan/phpstan/stargazers) - A PHP Static Analysis Tool.
* [Psalm](https://github.com/vimeo/psalm) [![GitHub stars](https://img.shields.io/github/stars/vimeo/psalm?style=flat)](https://github.com/vimeo/psalm/stargazers) - A static analysis tool for finding errors in PHP applications.

### Architectural
*Libraries related to design patterns, programming approaches and ways to organize code.*

* [Design Patterns PHP](https://github.com/DesignPatternsPHP/DesignPatternsPHP) [![GitHub stars](https://img.shields.io/github/stars/DesignPatternsPHP/DesignPatternsPHP?style=flat)](https://github.com/DesignPatternsPHP/DesignPatternsPHP/stargazers) - A repository of software patterns implemented in PHP.
* [Finite](https://github.com/yohang/Finite) [![GitHub stars](https://img.shields.io/github/stars/yohang/Finite?style=flat)](https://github.com/yohang/Finite/stargazers) - A simple PHP finite state machine.
* [Functional PHP](https://github.com/lstrojny/functional-php) [![GitHub stars](https://img.shields.io/github/stars/lstrojny/functional-php?style=flat)](https://github.com/lstrojny/functional-php/stargazers) - A functional programming library.
* [Iter](https://github.com/nikic/iter) [![GitHub stars](https://img.shields.io/github/stars/nikic/iter?style=flat)](https://github.com/nikic/iter/stargazers) - A library that provides iteration primitives using generators.
* [IterTools PHP](https://github.com/markrogoyski/itertools-php) [![GitHub stars](https://img.shields.io/github/stars/markrogoyski/itertools-php?style=flat)](https://github.com/markrogoyski/itertools-php/stargazers) - A library that provides functionality for working with iterable entities (similar to itertools library in Python).
* [Pipeline](https://github.com/thephpleague/pipeline) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/pipeline?style=flat)](https://github.com/thephpleague/pipeline/stargazers) - A pipeline pattern implementation.
* [Porter](https://github.com/ScriptFUSION/Porter) [![GitHub stars](https://img.shields.io/github/stars/ScriptFUSION/Porter?style=flat)](https://github.com/ScriptFUSION/Porter/stargazers) - Data import abstraction library for consuming Web APIs and other data sources.
* [RulerZ](https://github.com/K-Phoen/rulerz) [![GitHub stars](https://img.shields.io/github/stars/K-Phoen/rulerz?style=flat)](https://github.com/K-Phoen/rulerz/stargazers) - A powerful rule engine and implementation of the Specification pattern.

### Debugging and Profiling
*Libraries and tools for debugging errors and profiling code.*

* [APM](https://pecl.php.net/package/APM) - Monitoring extension collecting errors and statistics into SQLite/MySQL/StatsD.
* [Barbushin PHP Console](https://github.com/barbushin/php-console) [![GitHub stars](https://img.shields.io/github/stars/barbushin/php-console?style=flat)](https://github.com/barbushin/php-console/stargazers) - Another web debugging console using Google Chrome.
* [Kint](https://github.com/kint-php/kint) [![GitHub stars](https://img.shields.io/github/stars/kint-php/kint?style=flat)](https://github.com/kint-php/kint/stargazers) - A debugging and profiling tool.
* [LaraDumps](https://github.com/laradumps/laradumps) [![GitHub stars](https://img.shields.io/github/stars/laradumps/laradumps?style=flat)](https://github.com/laradumps/laradumps/stargazers) - A debugging tool for Laravel with a dedicated desktop application.
* [Metrics](https://github.com/beberlei/metrics) [![GitHub stars](https://img.shields.io/github/stars/beberlei/metrics?style=flat)](https://github.com/beberlei/metrics/stargazers) - A simple metrics API library.
* [PCOV](https://github.com/krakjoe/pcov) [![GitHub stars](https://img.shields.io/github/stars/krakjoe/pcov?style=flat)](https://github.com/krakjoe/pcov/stargazers) - A self-contained code coverage compatible driver.
* [PHP Console](https://github.com/Seldaek/php-console) [![GitHub stars](https://img.shields.io/github/stars/Seldaek/php-console?style=flat)](https://github.com/Seldaek/php-console/stargazers) - A web debugging console.
* [PHP Debug Bar](https://php-debugbar.com/) - A debugging toolbar.
* [PHPBench](https://github.com/phpbench/phpbench) [![GitHub stars](https://img.shields.io/github/stars/phpbench/phpbench?style=flat)](https://github.com/phpbench/phpbench/stargazers) - A benchmarking framework.
* [PHPSpy](https://github.com/adsr/phpspy) [![GitHub stars](https://img.shields.io/github/stars/adsr/phpspy?style=flat)](https://github.com/adsr/phpspy/stargazers) - A low-overhead sampling profiler.
* [Symfony VarDumper](https://github.com/symfony/var-dumper) [![GitHub stars](https://img.shields.io/github/stars/symfony/var-dumper?style=flat)](https://github.com/symfony/var-dumper/stargazers) - A variable dumper component.
* [Tracy](https://github.com/nette/tracy) [![GitHub stars](https://img.shields.io/github/stars/nette/tracy?style=flat)](https://github.com/nette/tracy/stargazers) - A simple error detection, logging and time measuring library.
* [Trap](https://github.com/buggregator/trap) [![GitHub stars](https://img.shields.io/github/stars/buggregator/trap?style=flat)](https://github.com/buggregator/trap/stargazers) - An extended variable dumper with a web interface and IDE plugin.
* [Whoops](https://github.com/filp/whoops) [![GitHub stars](https://img.shields.io/github/stars/filp/whoops?style=flat)](https://github.com/filp/whoops/stargazers) - A pretty error-handling library.
* [xDebug](https://github.com/xdebug/xdebug) [![GitHub stars](https://img.shields.io/github/stars/xdebug/xdebug?style=flat)](https://github.com/xdebug/xdebug/stargazers) - A debug and profile tool for PHP.
* [XHProf](https://github.com/phacility/xhprof) [![GitHub stars](https://img.shields.io/github/stars/phacility/xhprof?style=flat)](https://github.com/phacility/xhprof/stargazers) - A profiling tool originally developed by Facebook.
* [Z-Ray](https://www.zend.com/products/z-ray) - A debug and profile tool for Zend Server.

### Error Tracking and Monitoring Services
*Self-hosted or cloud-based application performance monitoring & error tracking tools*

* [Blackfire](https://www.blackfire.io) - A low-overhead code profiler.
* [Buggregator](https://buggregator.dev) - A debug server that aggregates var-dumps, profiling data, emails, logs and Sentry events.
* [BugSnag](https://www.bugsnag.com/) - Error and Real User Monitoring.
* [Honeybadger](https://www.honeybadger.io/) - Error Tracking & Application Monitoring for Developers.
* [Rollbar](https://rollbar.com/) - Error Logging & Tracking Service for Software Teams.
* [Sentry](https://sentry.io/welcome/) - Application Performance Monitoring & Error Tracking Software.
* [Tideways](https://tideways.com/) - Monitoring and profiling tool.

### Build Tools
*Project build and automation tools.*

* [Box](https://github.com/box-project/box) [![GitHub stars](https://img.shields.io/github/stars/box-project/box?style=flat)](https://github.com/box-project/box/stargazers) - A utility to build PHAR files.
* [PHPacker](https://github.com/phpacker/phpacker) [![GitHub stars](https://img.shields.io/github/stars/phpacker/phpacker?style=flat)](https://github.com/phpacker/phpacker/stargazers) - A PHAR builder that compiles PHP apps to standalone executables.
* [Phing](https://www.phing.info/) - A PHP project build system inspired by Apache Ant.
* [RMT](https://github.com/liip/RMT) [![GitHub stars](https://img.shields.io/github/stars/liip/RMT?style=flat)](https://github.com/liip/RMT/stargazers) - A library for versioning and releasing software.

### Task Runners
*Libraries for automating and running tasks.*

* [Jobby](https://github.com/jobbyphp/jobby) [![GitHub stars](https://img.shields.io/github/stars/jobbyphp/jobby?style=flat)](https://github.com/jobbyphp/jobby/stargazers) - A PHP cron job manager without modifying crontab.
* [Robo](https://github.com/consolidation/Robo) [![GitHub stars](https://img.shields.io/github/stars/consolidation/Robo?style=flat)](https://github.com/consolidation/Robo/stargazers) - A PHP task runner with object-oriented configurations.

### Navigation
*Tools for building navigation structures.*

* [KnpMenu](https://github.com/KnpLabs/KnpMenu) [![GitHub stars](https://img.shields.io/github/stars/KnpLabs/KnpMenu?style=flat)](https://github.com/KnpLabs/KnpMenu/stargazers) - A menu library.
* [Menu](https://github.com/spatie/menu) [![GitHub stars](https://img.shields.io/github/stars/spatie/menu?style=flat)](https://github.com/spatie/menu/stargazers) - A flexible menu library with a fluent interface.

### Asset Management
*Tools for managing, compressing and minifying website assets.*

* [JShrink](https://github.com/tedious/JShrink) [![GitHub stars](https://img.shields.io/github/stars/tedious/JShrink?style=flat)](https://github.com/tedious/JShrink/stargazers) - A JavaScript minifier library.
* [Laravel Mix](https://github.com/laravel-mix/laravel-mix) [![GitHub stars](https://img.shields.io/github/stars/laravel-mix/laravel-mix?style=flat)](https://github.com/laravel-mix/laravel-mix/stargazers) - An elegant wrapper around Webpack for the 80% use case.
* [Symfony Asset](https://github.com/symfony/asset) [![GitHub stars](https://img.shields.io/github/stars/symfony/asset?style=flat)](https://github.com/symfony/asset/stargazers) - Manages URL generation and versioning of web assets.
* [Symfony Encore](https://github.com/symfony/webpack-encore) [![GitHub stars](https://img.shields.io/github/stars/symfony/webpack-encore?style=flat)](https://github.com/symfony/webpack-encore/stargazers) - A simple but powerful API for processing and compiling assets built around Webpack.

### Geolocation
*Libraries for geocoding addresses and working with latitudes and longitudes.*

* [Country List](https://github.com/umpirsky/country-list) [![GitHub stars](https://img.shields.io/github/stars/umpirsky/country-list?style=flat)](https://github.com/umpirsky/country-list/stargazers) - A list of all countries with names and ISO 3166-1 codes.
* [GeoCoder](https://geocoder-php.org/) - A geocoding library.
* [GeoJSON](https://github.com/jmikola/geojson) [![GitHub stars](https://img.shields.io/github/stars/jmikola/geojson?style=flat)](https://github.com/jmikola/geojson/stargazers) - A GeoJSON implementation.
* [GeoTools](https://github.com/thephpleague/geotools) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/geotools?style=flat)](https://github.com/thephpleague/geotools/stargazers) - A library of geo-related tools.
* [PHPGeo](https://github.com/mjaschen/phpgeo) [![GitHub stars](https://img.shields.io/github/stars/mjaschen/phpgeo?style=flat)](https://github.com/mjaschen/phpgeo/stargazers) - A simple geo library.

### Date and Time
*Libraries for working with dates and times.*

* [Business Time](https://github.com/kylekatarnls/business-time) [![GitHub stars](https://img.shields.io/github/stars/kylekatarnls/business-time?style=flat)](https://github.com/kylekatarnls/business-time/stargazers) - A Carbon extension for handling business hours and working days.
* [CalendR](https://github.com/yohang/CalendR) [![GitHub stars](https://img.shields.io/github/stars/yohang/CalendR?style=flat)](https://github.com/yohang/CalendR/stargazers) - A calendar management library.
* [Carbon](https://github.com/briannesbitt/Carbon) [![GitHub stars](https://img.shields.io/github/stars/briannesbitt/Carbon?style=flat)](https://github.com/briannesbitt/Carbon/stargazers) - A simple DateTime API extension.
* [Chronos](https://github.com/cakephp/chronos) [![GitHub stars](https://img.shields.io/github/stars/cakephp/chronos?style=flat)](https://github.com/cakephp/chronos/stargazers) - A DateTime API extension supporting both mutable and immutable date/time.
* [Moment.php](https://github.com/fightbulc/moment.php) [![GitHub stars](https://img.shields.io/github/stars/fightbulc/moment.php?style=flat)](https://github.com/fightbulc/moment.php/stargazers) - Moment.js inspired PHP DateTime handler with i18n support.
* [PHP RRule](https://github.com/rlanvin/php-rrule) [![GitHub stars](https://img.shields.io/github/stars/rlanvin/php-rrule?style=flat)](https://github.com/rlanvin/php-rrule/stargazers) - A library for working with recurring dates and times based on the iCalendar RRule spec.
* [Yasumi](https://github.com/azuyalabs/yasumi) [![GitHub stars](https://img.shields.io/github/stars/azuyalabs/yasumi?style=flat)](https://github.com/azuyalabs/yasumi/stargazers) - A library to help you calculate the dates and names of holidays.

### Event
*Libraries that are event-driven or implement non-blocking event loops.*

* [Amp](https://github.com/amphp/amp) [![GitHub stars](https://img.shields.io/github/stars/amphp/amp?style=flat)](https://github.com/amphp/amp/stargazers) - An event-driven non-blocking I/O library.
* [Broadway](https://github.com/broadway/broadway) [![GitHub stars](https://img.shields.io/github/stars/broadway/broadway?style=flat)](https://github.com/broadway/broadway/stargazers) - An event source and CQRS library.
* [CakePHP Event](https://github.com/cakephp/event) [![GitHub stars](https://img.shields.io/github/stars/cakephp/event?style=flat)](https://github.com/cakephp/event/stargazers) - An event dispatcher library.
* [Elephant.io](https://github.com/ElephantIO/elephant.io) [![GitHub stars](https://img.shields.io/github/stars/ElephantIO/elephant.io?style=flat)](https://github.com/ElephantIO/elephant.io/stargazers) - Yet another web socket library.
* [Evenement](https://github.com/igorw/evenement) [![GitHub stars](https://img.shields.io/github/stars/igorw/evenement?style=flat)](https://github.com/igorw/evenement/stargazers) - An event dispatcher library.
* [Event](https://github.com/thephpleague/event) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/event?style=flat)](https://github.com/thephpleague/event/stargazers) - An event library with a focus on domain events.
* [Fast CGI Client](https://github.com/hollodotme/fast-cgi-client) [![GitHub stars](https://img.shields.io/github/stars/hollodotme/fast-cgi-client?style=flat)](https://github.com/hollodotme/fast-cgi-client/stargazers) - A client to make synchronous/asynchronous requests through php-fpm socket.
* [FrankenPHP](https://frankenphp.dev/) - A modern PHP app server written in Go.
* [Pawl](https://github.com/ratchetphp/Pawl) [![GitHub stars](https://img.shields.io/github/stars/ratchetphp/Pawl?style=flat)](https://github.com/ratchetphp/Pawl/stargazers) - An asynchronous web socket client.
* [Prooph Event Store](https://github.com/prooph/event-store) [![GitHub stars](https://img.shields.io/github/stars/prooph/event-store?style=flat)](https://github.com/prooph/event-store/stargazers) - An event source component to persist event messages.
* [PHP Defer](https://github.com/php-defer/php-defer) [![GitHub stars](https://img.shields.io/github/stars/php-defer/php-defer?style=flat)](https://github.com/php-defer/php-defer/stargazers) - Golang's defer statement for PHP.
* [Ratchet](https://github.com/ratchetphp/Ratchet) [![GitHub stars](https://img.shields.io/github/stars/ratchetphp/Ratchet?style=flat)](https://github.com/ratchetphp/Ratchet/stargazers) - A web socket library.
* [ReactPHP](https://github.com/reactphp/reactphp) [![GitHub stars](https://img.shields.io/github/stars/reactphp/reactphp?style=flat)](https://github.com/reactphp/reactphp/stargazers) - An event-driven non-blocking I/O library.
* [RxPHP](https://github.com/ReactiveX/RxPHP) [![GitHub stars](https://img.shields.io/github/stars/ReactiveX/RxPHP?style=flat)](https://github.com/ReactiveX/RxPHP/stargazers) - A reactive extension library.
* [Swoole](https://github.com/swoole/swoole-src) [![GitHub stars](https://img.shields.io/github/stars/swoole/swoole-src?style=flat)](https://github.com/swoole/swoole-src/stargazers) - An event-driven asynchronous and concurrent networking communication framework with high performance for PHP written in C.
* [Workerman](https://github.com/walkor/Workerman) [![GitHub stars](https://img.shields.io/github/stars/walkor/Workerman?style=flat)](https://github.com/walkor/Workerman/stargazers) - An event-driven non-blocking I/O library.

### Logging
*Libraries for generating and working with log files.*

* [Monolog](https://github.com/Seldaek/monolog) [![GitHub stars](https://img.shields.io/github/stars/Seldaek/monolog?style=flat)](https://github.com/Seldaek/monolog/stargazers) - A comprehensive logger.

### E-commerce
*Libraries and applications for taking payments and building online e-commerce stores.*

* [Money](https://github.com/moneyphp/money) [![GitHub stars](https://img.shields.io/github/stars/moneyphp/money?style=flat)](https://github.com/moneyphp/money/stargazers) - A PHP implementation of Fowler's money pattern.
* [Brick Money](https://github.com/brick/money) [![GitHub stars](https://img.shields.io/github/stars/brick/money?style=flat)](https://github.com/brick/money/stargazers) - A money library for PHP, with support for contexts, cash roundings, currency conversion.
* [OmniPay](https://github.com/thephpleague/omnipay) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/omnipay?style=flat)](https://github.com/thephpleague/omnipay/stargazers) - A framework agnostic multi-gateway payment processing library.
* [Payum](https://github.com/payum/payum) [![GitHub stars](https://img.shields.io/github/stars/payum/payum?style=flat)](https://github.com/payum/payum/stargazers) - A payment abstraction library.
* [Shopsys Framework](https://github.com/shopsys/shopsys/) [![GitHub stars](https://img.shields.io/github/stars/shopsys/shopsys/?style=flat)](https://github.com/shopsys/shopsys//stargazers) - An open source e-commerce platform for in-house development teams.
* [Shopware](https://github.com/shopware/shopware) [![GitHub stars](https://img.shields.io/github/stars/shopware/shopware?style=flat)](https://github.com/shopware/shopware/stargazers) - Highly customizable e-commerce software.
* [Swap](https://github.com/florianv/swap) [![GitHub stars](https://img.shields.io/github/stars/florianv/swap?style=flat)](https://github.com/florianv/swap/stargazers) - An exchange rates library.
* [Sylius](https://sylius.com/) - An open source e-commerce solution.

### PDF
*Libraries and software for working with PDF files.*

* [Browsershot](https://github.com/spatie/browsershot) [![GitHub stars](https://img.shields.io/github/stars/spatie/browsershot?style=flat)](https://github.com/spatie/browsershot/stargazers) - Convert HTML to an image, PDF or string.
* [Dompdf](https://github.com/dompdf/dompdf) [![GitHub stars](https://img.shields.io/github/stars/dompdf/dompdf?style=flat)](https://github.com/dompdf/dompdf/stargazers) - A HTML to PDF converter.
* [Gotenberg](https://github.com/gotenberg/gotenberg-php) [![GitHub stars](https://img.shields.io/github/stars/gotenberg/gotenberg-php?style=flat)](https://github.com/gotenberg/gotenberg-php/stargazers) - A PHP client for interacting with Gotenberg.
* [Snappy](https://github.com/KnpLabs/snappy) [![GitHub stars](https://img.shields.io/github/stars/KnpLabs/snappy?style=flat)](https://github.com/KnpLabs/snappy/stargazers) - A PDF and image generation library.
* [TCPDF](https://tcpdf.org/) - An open source PHP class for generating PDF documents.

### Office
*Libraries for working with office suite documents.*

* [PHPPowerPoint](https://github.com/PHPOffice/PHPPresentation) [![GitHub stars](https://img.shields.io/github/stars/PHPOffice/PHPPresentation?style=flat)](https://github.com/PHPOffice/PHPPresentation/stargazers) - A library for working with Microsoft PowerPoint Presentations.
* [PHPWord](https://github.com/PHPOffice/PHPWord) [![GitHub stars](https://img.shields.io/github/stars/PHPOffice/PHPWord?style=flat)](https://github.com/PHPOffice/PHPWord/stargazers) - A library for working with Microsoft Word documents.
* [PHPSpreadsheet](https://github.com/PHPOffice/PhpSpreadsheet) [![GitHub stars](https://img.shields.io/github/stars/PHPOffice/PhpSpreadsheet?style=flat)](https://github.com/PHPOffice/PhpSpreadsheet/stargazers) - A pure PHP library for reading and writing spreadsheet files (successor of PHPExcel).
* [OpenSpout](https://github.com/openspout/openspout) [![GitHub stars](https://img.shields.io/github/stars/openspout/openspout?style=flat)](https://github.com/openspout/openspout/stargazers) - A community driven fork of `box/spout`, a PHP library to read and write spreadsheet files (CSV, XLSX and ODS), in a fast and scalable way.

### Database
*Libraries for interacting with databases using object-relational mapping (ORM) or datamapping techniques.*

* [Atlas.Orm](https://github.com/atlasphp/Atlas.Orm) [![GitHub stars](https://img.shields.io/github/stars/atlasphp/Atlas.Orm?style=flat)](https://github.com/atlasphp/Atlas.Orm/stargazers) - A data mapper implementation for your persistence model in PHP.
* [Aura.Sql](https://github.com/auraphp/Aura.Sql) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Sql?style=flat)](https://github.com/auraphp/Aura.Sql/stargazers) - Provides an extension to the native PDO along with a profiler and connection locator.
* [Aura.SqlQuery](https://github.com/auraphp/Aura.SqlQuery) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.SqlQuery?style=flat)](https://github.com/auraphp/Aura.SqlQuery/stargazers) - Independent query builders for MySQL, PostgreSQL, SQLite, and Microsoft SQL Server.
* [Baum](https://github.com/etrepat/baum) [![GitHub stars](https://img.shields.io/github/stars/etrepat/baum?style=flat)](https://github.com/etrepat/baum/stargazers) - A nested set implementation for Eloquent.
* [CakePHP ORM](https://github.com/cakephp/orm) [![GitHub stars](https://img.shields.io/github/stars/cakephp/orm?style=flat)](https://github.com/cakephp/orm/stargazers) - Object-Relational Mapper, implemented using the DataMapper pattern.
* [Cycle ORM](https://github.com/cycle/orm) [![GitHub stars](https://img.shields.io/github/stars/cycle/orm?style=flat)](https://github.com/cycle/orm/stargazers) - PHP DataMapper, ORM.
* [Doctrine Extensions](https://github.com/doctrine-extensions/DoctrineExtensions) [![GitHub stars](https://img.shields.io/github/stars/doctrine-extensions/DoctrineExtensions?style=flat)](https://github.com/doctrine-extensions/DoctrineExtensions/stargazers) - A collection of Doctrine behavioural extensions.
* [Doctrine](https://www.doctrine-project.org/) - A comprehensive DBAL and ORM.
* [Laravel Eloquent](https://github.com/illuminate/database) [![GitHub stars](https://img.shields.io/github/stars/illuminate/database?style=flat)](https://github.com/illuminate/database/stargazers) - A simple ORM.
* [ProxyManager](https://github.com/Ocramius/ProxyManager) [![GitHub stars](https://img.shields.io/github/stars/Ocramius/ProxyManager?style=flat)](https://github.com/Ocramius/ProxyManager/stargazers) - A set of utilities to generate proxy objects for data mappers.
* [RedBean](https://redbeanphp.com/index.php) - A lightweight, configuration-less ORM.
* [Slimdump](https://github.com/webfactory/slimdump) [![GitHub stars](https://img.shields.io/github/stars/webfactory/slimdump?style=flat)](https://github.com/webfactory/slimdump/stargazers) - An easy dumper tool for MySQL.
* [Spot2](https://github.com/spotorm/spot2) [![GitHub stars](https://img.shields.io/github/stars/spotorm/spot2?style=flat)](https://github.com/spotorm/spot2/stargazers) - A MySQL datamapper ORM.

### Migrations
*Libraries to help manage database schemas and migrations.*

* [Doctrine Migrations](https://www.doctrine-project.org/projects/migrations.html) - A migration library for Doctrine.
* [Phinx](https://github.com/cakephp/phinx) [![GitHub stars](https://img.shields.io/github/stars/cakephp/phinx?style=flat)](https://github.com/cakephp/phinx/stargazers) - Another database migration library.
* [PHPMig](https://github.com/davedevelopment/phpmig) [![GitHub stars](https://img.shields.io/github/stars/davedevelopment/phpmig?style=flat)](https://github.com/davedevelopment/phpmig/stargazers) - Another migration management library.
* [Ruckusing](https://github.com/ruckus/ruckusing-migrations) [![GitHub stars](https://img.shields.io/github/stars/ruckus/ruckusing-migrations?style=flat)](https://github.com/ruckus/ruckusing-migrations/stargazers) - Database migrations for PHP ala ActiveRecord Migrations with support for MySQL, Postgres, SQLite.

### NoSQL
*Libraries for working with "NoSQL" backends.*

* [MongoDB](https://github.com/mongodb/mongo-php-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-php-driver?style=flat)](https://github.com/mongodb/mongo-php-driver/stargazers) - MongoDB PHP Driver.
* [MongoDB PHP Library](https://github.com/mongodb/mongo-php-library) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-php-library?style=flat)](https://github.com/mongodb/mongo-php-library/stargazers) - The official high-level MongoDB PHP library built on top of the MongoDB PHP Driver.
* [Predis](https://github.com/predis/predis) [![GitHub stars](https://img.shields.io/github/stars/predis/predis?style=flat)](https://github.com/predis/predis/stargazers) - A feature-complete Redis library.

### Queue
*Libraries for working with event and task queues.*

* [BunnyPHP](https://github.com/jakubkulhan/bunny) [![GitHub stars](https://img.shields.io/github/stars/jakubkulhan/bunny?style=flat)](https://github.com/jakubkulhan/bunny/stargazers) - A performant pure-PHP AMQP (RabbitMQ) sync and also async (ReactPHP) library.
* [Pheanstalk](https://github.com/pheanstalk/pheanstalk) [![GitHub stars](https://img.shields.io/github/stars/pheanstalk/pheanstalk?style=flat)](https://github.com/pheanstalk/pheanstalk/stargazers) - A Beanstalkd client library.
* [PHP AMQP](https://github.com/php-amqplib/php-amqplib) [![GitHub stars](https://img.shields.io/github/stars/php-amqplib/php-amqplib?style=flat)](https://github.com/php-amqplib/php-amqplib/stargazers) - A pure PHP AMQP library.
* [Tarantool Queue](https://github.com/tarantool-php/queue) [![GitHub stars](https://img.shields.io/github/stars/tarantool-php/queue?style=flat)](https://github.com/tarantool-php/queue/stargazers) - PHP bindings for Tarantool Queue.
* [Thumper](https://github.com/php-amqplib/Thumper) [![GitHub stars](https://img.shields.io/github/stars/php-amqplib/Thumper?style=flat)](https://github.com/php-amqplib/Thumper/stargazers) - A RabbitMQ pattern library.
* [Enqueue](https://github.com/php-enqueue/enqueue-dev) [![GitHub stars](https://img.shields.io/github/stars/php-enqueue/enqueue-dev?style=flat)](https://github.com/php-enqueue/enqueue-dev/stargazers) - A message queue package for PHP that supports RabbitMQ, AMQP, STOMP, Amazon SQS, Redis and Doctrine transports.

### Search
*Libraries and software for indexing and performing search queries on data.*

* [Elastica](https://github.com/ruflin/Elastica) [![GitHub stars](https://img.shields.io/github/stars/ruflin/Elastica?style=flat)](https://github.com/ruflin/Elastica/stargazers) - A client library for ElasticSearch.
* [ElasticSearch PHP](https://github.com/elastic/elasticsearch-php) [![GitHub stars](https://img.shields.io/github/stars/elastic/elasticsearch-php?style=flat)](https://github.com/elastic/elasticsearch-php/stargazers) - The official client library for [ElasticSearch](https://www.elastic.co/).
* [Solarium](https://www.solarium-project.org/) - A client library for [Solr](https://solr.apache.org/).
* [SphinxQL Query Builder](https://foolcode.github.io/SphinxQL-Query-Builder/) - A query library for the [Sphinx](https://sphinxsearch.com/) and [Manticore](https://manticoresearch.com/) search engines.

### Command Line
*Libraries related to the command line.*

* [Aura.Cli](https://github.com/auraphp/Aura.Cli) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Cli?style=flat)](https://github.com/auraphp/Aura.Cli/stargazers) - Provides the equivalent of request ( Context ) and response ( Stdio ) objects for the command line interface, including Getopt support, and an independent Help object for describing commands.
* [CLI Menu](https://github.com/php-school/cli-menu) [![GitHub stars](https://img.shields.io/github/stars/php-school/cli-menu?style=flat)](https://github.com/php-school/cli-menu/stargazers) - A library for building CLI menus.
* [CLIFramework](https://github.com/c9s/CLIFramework) [![GitHub stars](https://img.shields.io/github/stars/c9s/CLIFramework?style=flat)](https://github.com/c9s/CLIFramework/stargazers) - A command-line framework that supports zsh/bash completion generation, subcommands and option constraints. It also powers phpbrew.
* [CLImate](https://github.com/thephpleague/climate) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/climate?style=flat)](https://github.com/thephpleague/climate/stargazers) - A library for outputting colors and special formatting.
* [Commando](https://github.com/nategood/commando) [![GitHub stars](https://img.shields.io/github/stars/nategood/commando?style=flat)](https://github.com/nategood/commando/stargazers) - Another simple command line opt parser.
* [Cron Expression](https://github.com/mtdowling/cron-expression) [![GitHub stars](https://img.shields.io/github/stars/mtdowling/cron-expression?style=flat)](https://github.com/mtdowling/cron-expression/stargazers) - A library to calculate cron run dates.
* [GetOpt](https://github.com/getopt-php/getopt-php) [![GitHub stars](https://img.shields.io/github/stars/getopt-php/getopt-php?style=flat)](https://github.com/getopt-php/getopt-php/stargazers) - A command line opt parser.
* [GetOptionKit](https://github.com/c9s/GetOptionKit) [![GitHub stars](https://img.shields.io/github/stars/c9s/GetOptionKit?style=flat)](https://github.com/c9s/GetOptionKit/stargazers) - Another command line opt parser.
* [PsySH](https://github.com/bobthecow/psysh) [![GitHub stars](https://img.shields.io/github/stars/bobthecow/psysh?style=flat)](https://github.com/bobthecow/psysh/stargazers) - Another PHP REPL.
* [ShellWrap](https://github.com/MrRio/shellwrap) [![GitHub stars](https://img.shields.io/github/stars/MrRio/shellwrap?style=flat)](https://github.com/MrRio/shellwrap/stargazers) - A simple command line wrapper library.

### Authentication and Authorization
*Libraries for implementing user authentication and authorization.*

* [Aura.Auth](https://github.com/auraphp/Aura.Auth) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Auth?style=flat)](https://github.com/auraphp/Aura.Auth/stargazers) - Provides authentication functionality and session tracking using various adapters.
* [SocialConnect Auth](https://github.com/socialConnect/auth) [![GitHub stars](https://img.shields.io/github/stars/socialConnect/auth?style=flat)](https://github.com/socialConnect/auth/stargazers) - An open source social sign (OAuth1\OAuth2\OpenID\OpenIDConnect).
* [Json Web Token](https://github.com/lcobucci/jwt) [![GitHub stars](https://img.shields.io/github/stars/lcobucci/jwt?style=flat)](https://github.com/lcobucci/jwt/stargazers) - Json Tokens to authenticate and transmit information.
* [OAuth 1.0 Client](https://github.com/thephpleague/oauth1-client) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/oauth1-client?style=flat)](https://github.com/thephpleague/oauth1-client/stargazers) - An OAuth 1.0 client library.
* [OAuth 2.0 Client](https://github.com/thephpleague/oauth2-client) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/oauth2-client?style=flat)](https://github.com/thephpleague/oauth2-client/stargazers) - An OAuth 2.0 client library.
* [OAuth2 Server](https://bshaffer.github.io/oauth2-server-php-docs/) - Another OAuth2 server implementation.
* [OAuth2 Server](https://oauth2.thephpleague.com/) - An OAuth2 authentication server, resource server and client library.
* [Paseto](https://github.com/paragonie/paseto) [![GitHub stars](https://img.shields.io/github/stars/paragonie/paseto?style=flat)](https://github.com/paragonie/paseto/stargazers) - Platform-Agnostic Security Tokens.
* [PHP oAuthLib](https://github.com/daviddesberg/PHPoAuthLib) [![GitHub stars](https://img.shields.io/github/stars/daviddesberg/PHPoAuthLib?style=flat)](https://github.com/daviddesberg/PHPoAuthLib/stargazers) - Another OAuth library.
* [TwitterOAuth](https://github.com/abraham/twitteroauth) [![GitHub stars](https://img.shields.io/github/stars/abraham/twitteroauth?style=flat)](https://github.com/abraham/twitteroauth/stargazers) - A Twitter OAuth library.

### Markup and CSS
*Libraries for working with markup and CSS formats.*

* [Cebe Markdown](https://github.com/cebe/markdown) [![GitHub stars](https://img.shields.io/github/stars/cebe/markdown?style=flat)](https://github.com/cebe/markdown/stargazers) - A fast and extensible Markdown parser.
* [CommonMark PHP](https://github.com/thephpleague/commonmark) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/commonmark?style=flat)](https://github.com/thephpleague/commonmark/stargazers) - Highly-extensible Markdown parser which fully supports the [CommonMark spec](https://spec.commonmark.org/).
* [Decoda](https://github.com/milesj/decoda) [![GitHub stars](https://img.shields.io/github/stars/milesj/decoda?style=flat)](https://github.com/milesj/decoda/stargazers) - A lightweight markup parser library.
* [Djot](https://github.com/php-collective/djot-php) [![GitHub stars](https://img.shields.io/github/stars/php-collective/djot-php?style=flat)](https://github.com/php-collective/djot-php/stargazers) - A PHP parser for [Djot](https://djot.net/), a modern light markup language (successor of Markdown).
* [Essence](https://github.com/essence/essence) [![GitHub stars](https://img.shields.io/github/stars/essence/essence?style=flat)](https://github.com/essence/essence/stargazers) - A library for extracting web media.
* [Embera](https://github.com/mpratt/Embera) [![GitHub stars](https://img.shields.io/github/stars/mpratt/Embera?style=flat)](https://github.com/mpratt/Embera/stargazers) - An Oembed consumer library.
* [HTML to Markdown](https://github.com/thephpleague/html-to-markdown) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/html-to-markdown?style=flat)](https://github.com/thephpleague/html-to-markdown/stargazers) - Converts HTML into Markdown.
* [HTML5 PHP](https://github.com/Masterminds/html5-php) [![GitHub stars](https://img.shields.io/github/stars/Masterminds/html5-php?style=flat)](https://github.com/Masterminds/html5-php/stargazers) - An HTML5 parser and serializer library.
* [Parsedown](https://github.com/erusev/parsedown) [![GitHub stars](https://img.shields.io/github/stars/erusev/parsedown?style=flat)](https://github.com/erusev/parsedown/stargazers) - Another Markdown parser.
* [PHP CSS Parser](https://github.com/MyIntervals/PHP-CSS-Parser) [![GitHub stars](https://img.shields.io/github/stars/MyIntervals/PHP-CSS-Parser?style=flat)](https://github.com/MyIntervals/PHP-CSS-Parser/stargazers) - A Parser for CSS Files written in PHP.
* [PHP Markdown](https://github.com/michelf/php-markdown) [![GitHub stars](https://img.shields.io/github/stars/michelf/php-markdown?style=flat)](https://github.com/michelf/php-markdown/stargazers) - A Markdown parser.
* [Shiki PHP](https://github.com/spatie/shiki-php) [![GitHub stars](https://img.shields.io/github/stars/spatie/shiki-php?style=flat)](https://github.com/spatie/shiki-php/stargazers) - A [Shiki](https://github.com/shikijs/shiki) [![GitHub stars](https://img.shields.io/github/stars/shikijs/shiki?style=flat)](https://github.com/shikijs/shiki/stargazers) code highlighting package in PHP.
* [VObject](https://github.com/sabre-io/vobject) [![GitHub stars](https://img.shields.io/github/stars/sabre-io/vobject?style=flat)](https://github.com/sabre-io/vobject/stargazers) - A library for parsing VCard and iCalendar objects.

### JSON
*Libraries for working with JSON.*

* [JSON Lint](https://github.com/Seldaek/jsonlint) [![GitHub stars](https://img.shields.io/github/stars/Seldaek/jsonlint?style=flat)](https://github.com/Seldaek/jsonlint/stargazers) - A JSON lint utility.
* [JSONMapper](https://github.com/JsonMapper/JsonMapper) [![GitHub stars](https://img.shields.io/github/stars/JsonMapper/JsonMapper?style=flat)](https://github.com/JsonMapper/JsonMapper/stargazers) - A library for mapping JSON to PHP objects.
* [Lazy JSON](https://github.com/cerbero90/lazy-json) [![GitHub stars](https://img.shields.io/github/stars/cerbero90/lazy-json?style=flat)](https://github.com/cerbero90/lazy-json/stargazers) - A memory-efficient lazy parser for large JSON files.

### Strings
*Libraries for parsing and manipulating strings.*

* [Agent](https://github.com/jenssegers/agent) [![GitHub stars](https://img.shields.io/github/stars/jenssegers/agent?style=flat)](https://github.com/jenssegers/agent/stargazers) - A PHP desktop/mobile user agent parser, based on Mobiledetect.
* [ANSI to HTML5](https://github.com/sensiolabs/ansi-to-html) [![GitHub stars](https://img.shields.io/github/stars/sensiolabs/ansi-to-html?style=flat)](https://github.com/sensiolabs/ansi-to-html/stargazers) - An ANSI to HTML5 converter library.
* [Color Jizz](https://github.com/mikeemoo/ColorJizz-PHP) [![GitHub stars](https://img.shields.io/github/stars/mikeemoo/ColorJizz-PHP?style=flat)](https://github.com/mikeemoo/ColorJizz-PHP/stargazers) - A library for manipulating and converting colors.
* [Device Detector](https://github.com/matomo-org/device-detector) [![GitHub stars](https://img.shields.io/github/stars/matomo-org/device-detector?style=flat)](https://github.com/matomo-org/device-detector/stargazers) - Another library for parsing user agent strings.
* [Hyphenation](https://github.com/heiglandreas/Org_Heigl_Hyphenator) [![GitHub stars](https://img.shields.io/github/stars/heiglandreas/Org_Heigl_Hyphenator?style=flat)](https://github.com/heiglandreas/Org_Heigl_Hyphenator/stargazers) - Text hyphenation based on the TeX hyphenation algorithm.
* [Jieba-PHP](https://github.com/fukuball/jieba-php) [![GitHub stars](https://img.shields.io/github/stars/fukuball/jieba-php?style=flat)](https://github.com/fukuball/jieba-php/stargazers) - A PHP port of Python's jieba. Chinese text segmentation for natural language processing.
* [Mobile-Detect](https://github.com/serbanghita/Mobile-Detect) [![GitHub stars](https://img.shields.io/github/stars/serbanghita/Mobile-Detect?style=flat)](https://github.com/serbanghita/Mobile-Detect/stargazers) - A lightweight PHP class for detecting mobile devices (including tablets).
* [Patchwork UTF-8](https://github.com/nicolas-grekas/Patchwork-UTF8) [![GitHub stars](https://img.shields.io/github/stars/nicolas-grekas/Patchwork-UTF8?style=flat)](https://github.com/nicolas-grekas/Patchwork-UTF8/stargazers) - A portable library for working with UTF-8 strings.
* [Portable ASCII](https://github.com/voku/portable-ascii) [![GitHub stars](https://img.shields.io/github/stars/voku/portable-ascii?style=flat)](https://github.com/voku/portable-ascii/stargazers) - A library to convert strings to ASCII.
* [Portable UTF-8](https://github.com/voku/portable-utf8) [![GitHub stars](https://img.shields.io/github/stars/voku/portable-utf8?style=flat)](https://github.com/voku/portable-utf8/stargazers) - A string manipulation library with UTF-8 safe replacement methods.
* [Slugify](https://github.com/cocur/slugify) [![GitHub stars](https://img.shields.io/github/stars/cocur/slugify?style=flat)](https://github.com/cocur/slugify/stargazers) - A library to convert strings to slugs.
* [SQL Formatter](https://github.com/jdorn/sql-formatter/) [![GitHub stars](https://img.shields.io/github/stars/jdorn/sql-formatter/?style=flat)](https://github.com/jdorn/sql-formatter//stargazers) - A library for formatting SQL statements.
* [Stringy](https://github.com/voku/Stringy) [![GitHub stars](https://img.shields.io/github/stars/voku/Stringy?style=flat)](https://github.com/voku/Stringy/stargazers) - A string manipulation library with multibyte support.
* [Url highlight](https://github.com/vstelmakh/url-highlight) [![GitHub stars](https://img.shields.io/github/stars/vstelmakh/url-highlight?style=flat)](https://github.com/vstelmakh/url-highlight/stargazers) - A library for parsing URLs from text and converting them into clickable links.
* [URLify](https://github.com/jbroadway/urlify) [![GitHub stars](https://img.shields.io/github/stars/jbroadway/urlify?style=flat)](https://github.com/jbroadway/urlify/stargazers) - A PHP port of Django's URLify.js.
* [UUID](https://github.com/ramsey/uuid) [![GitHub stars](https://img.shields.io/github/stars/ramsey/uuid?style=flat)](https://github.com/ramsey/uuid/stargazers) - A library for generating UUIDs.

### Numbers
*Libraries for working with numbers.*

* [Brick Math](https://github.com/brick/math) [![GitHub stars](https://img.shields.io/github/stars/brick/math?style=flat)](https://github.com/brick/math/stargazers) - A library providing large number support: `BigInteger`, `BigDecimal` and `BigRational`.
* [ByteUnits](https://github.com/gabrielelana/byte-units) [![GitHub stars](https://img.shields.io/github/stars/gabrielelana/byte-units?style=flat)](https://github.com/gabrielelana/byte-units/stargazers) - A library to parse, format and convert byte units in binary and metric systems.
* [DecimalObject](https://github.com/php-collective/decimal-object) [![GitHub stars](https://img.shields.io/github/stars/php-collective/decimal-object?style=flat)](https://github.com/php-collective/decimal-object/stargazers) - A value object to handle decimals/floats easily and more precisely.
* [IP](https://github.com/darsyn/ip) [![GitHub stars](https://img.shields.io/github/stars/darsyn/ip?style=flat)](https://github.com/darsyn/ip/stargazers) - An immutable value object for working with IPv4 and IPv6 addresses.
* [PHP Conversion](https://github.com/cniska/php-conversion) [![GitHub stars](https://img.shields.io/github/stars/cniska/php-conversion?style=flat)](https://github.com/cniska/php-conversion/stargazers) - Another library for converting between units of measure.
* [PHP Units of Measure](https://github.com/triplepoint/php-units-of-measure) [![GitHub stars](https://img.shields.io/github/stars/triplepoint/php-units-of-measure?style=flat)](https://github.com/triplepoint/php-units-of-measure/stargazers) - A library for converting between units of measure.
* [MathPHP](https://github.com/markrogoyski/math-php) [![GitHub stars](https://img.shields.io/github/stars/markrogoyski/math-php?style=flat)](https://github.com/markrogoyski/math-php/stargazers) - A math library for PHP.

### Filtering, Sanitizing and Validation
*Libraries for filtering, sanitizing and validating data.*

* [Assert](https://github.com/beberlei/assert) [![GitHub stars](https://img.shields.io/github/stars/beberlei/assert?style=flat)](https://github.com/beberlei/assert/stargazers) - A validation library with a rich set of assertions. Supports assertion chaining and lazy assertions.
* [Aura.Filter](https://github.com/auraphp/Aura.Filter) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Filter?style=flat)](https://github.com/auraphp/Aura.Filter/stargazers) - Provides tools to validate and sanitize objects and arrays.
* [CakePHP Validation](https://github.com/cakephp/validation) [![GitHub stars](https://img.shields.io/github/stars/cakephp/validation?style=flat)](https://github.com/cakephp/validation/stargazers) - Another validation library.
* [Filterus](https://github.com/ircmaxell/filterus) [![GitHub stars](https://img.shields.io/github/stars/ircmaxell/filterus?style=flat)](https://github.com/ircmaxell/filterus/stargazers) - A simple PHP filtering library.
* [HTML Purifier](https://github.com/ezyang/htmlpurifier) [![GitHub stars](https://img.shields.io/github/stars/ezyang/htmlpurifier?style=flat)](https://github.com/ezyang/htmlpurifier/stargazers) - A standards compliant HTML filter.
* [ISO-codes](https://github.com/ronanguilloux/IsoCodes) [![GitHub stars](https://img.shields.io/github/stars/ronanguilloux/IsoCodes?style=flat)](https://github.com/ronanguilloux/IsoCodes/stargazers) - A library for validating inputs according to standards from ISO, International Finance, Public Administrations, GS1, Book Industry, Phone numbers & Zipcodes for many countries.
* [JSON Schema](https://github.com/jsonrainbow/json-schema) [![GitHub stars](https://img.shields.io/github/stars/jsonrainbow/json-schema?style=flat)](https://github.com/jsonrainbow/json-schema/stargazers) - A [JSON Schema](https://json-schema.org/) validation library.
* [LibPhoneNumber for PHP](https://github.com/giggsey/libphonenumber-for-php) [![GitHub stars](https://img.shields.io/github/stars/giggsey/libphonenumber-for-php?style=flat)](https://github.com/giggsey/libphonenumber-for-php/stargazers) - A PHP implementation of Google's phone number handling library.
* [MetaYaml](https://github.com/romaricdrigon/MetaYaml) [![GitHub stars](https://img.shields.io/github/stars/romaricdrigon/MetaYaml?style=flat)](https://github.com/romaricdrigon/MetaYaml/stargazers) - A schema validation library that supports YAML, JSON and XML.
* [Respect Validation](https://github.com/Respect/Validation) [![GitHub stars](https://img.shields.io/github/stars/Respect/Validation?style=flat)](https://github.com/Respect/Validation/stargazers) - A simple validation library.
* [Symfony HTML Sanitizer](https://github.com/symfony/html-sanitizer) [![GitHub stars](https://img.shields.io/github/stars/symfony/html-sanitizer?style=flat)](https://github.com/symfony/html-sanitizer/stargazers) - An HTML sanitizer library.
* [Valitron](https://github.com/vlucas/valitron) [![GitHub stars](https://img.shields.io/github/stars/vlucas/valitron?style=flat)](https://github.com/vlucas/valitron/stargazers) - Another validation library.
* [Valinor](https://github.com/CuyZ/Valinor) [![GitHub stars](https://img.shields.io/github/stars/CuyZ/Valinor?style=flat)](https://github.com/CuyZ/Valinor/stargazers) - A library for mapping to strongly typed value objects.
* [Volan](https://github.com/serkin/Volan) [![GitHub stars](https://img.shields.io/github/stars/serkin/Volan?style=flat)](https://github.com/serkin/Volan/stargazers) - Another simplified validation library.

### API
*Libraries and web tools for developing APIs.*

* [API Platform](https://api-platform.com) - Expose in minutes a hypermedia REST API that embraces JSON-LD, Hydra format.
* [Laminas API Tool Skeleton](https://github.com/laminas-api-tools/api-tools-skeleton) [![GitHub stars](https://img.shields.io/github/stars/laminas-api-tools/api-tools-skeleton?style=flat)](https://github.com/laminas-api-tools/api-tools-skeleton/stargazers) - An API builder built with the Laminas Framework.
* [HAL](https://github.com/blongden/hal) [![GitHub stars](https://img.shields.io/github/stars/blongden/hal?style=flat)](https://github.com/blongden/hal/stargazers) - A Hypertext Application Language (HAL) builder library.
* [Hateoas](https://github.com/willdurand/Hateoas) [![GitHub stars](https://img.shields.io/github/stars/willdurand/Hateoas?style=flat)](https://github.com/willdurand/Hateoas/stargazers) - A HATEOAS REST web service library.
* [Jane](https://github.com/janephp/janephp/) [![GitHub stars](https://img.shields.io/github/stars/janephp/janephp/?style=flat)](https://github.com/janephp/janephp//stargazers) - An OpenApi client generator with validation support.
* [Negotiation](https://github.com/willdurand/Negotiation) [![GitHub stars](https://img.shields.io/github/stars/willdurand/Negotiation?style=flat)](https://github.com/willdurand/Negotiation/stargazers) - A content negotiation library.
* [Restler](https://github.com/Luracast/Restler) [![GitHub stars](https://img.shields.io/github/stars/Luracast/Restler?style=flat)](https://github.com/Luracast/Restler/stargazers) - A lightweight framework to expose PHP methods as RESTful web API.
* [PackageGenerator](https://github.com/WsdlToPhp/PackageGenerator) [![GitHub stars](https://img.shields.io/github/stars/WsdlToPhp/PackageGenerator?style=flat)](https://github.com/WsdlToPhp/PackageGenerator/stargazers) - Package Generator generates a PHP SDK from any WSDL.

### Caching and Locking
*Libraries for caching data and acquiring locks.*

* [APIx Cache](https://github.com/apix/cache) [![GitHub stars](https://img.shields.io/github/stars/apix/cache?style=flat)](https://github.com/apix/cache/stargazers) - A thin PSR-6 cache wrapper to various caching backends emphasizing cache tagging and indexing.
* [CacheTool](https://github.com/gordalina/cachetool) [![GitHub stars](https://img.shields.io/github/stars/gordalina/cachetool?style=flat)](https://github.com/gordalina/cachetool/stargazers) - A tool to clear APC/opcode caches from the command line.
* [CakePHP Cache](https://github.com/cakephp/cache) [![GitHub stars](https://img.shields.io/github/stars/cakephp/cache?style=flat)](https://github.com/cakephp/cache/stargazers) - A caching library.
* [Doctrine Cache](https://github.com/doctrine/cache) [![GitHub stars](https://img.shields.io/github/stars/doctrine/cache?style=flat)](https://github.com/doctrine/cache/stargazers) - A caching library.
* [Metaphore](https://github.com/sobstel/metaphore) [![GitHub stars](https://img.shields.io/github/stars/sobstel/metaphore?style=flat)](https://github.com/sobstel/metaphore/stargazers) - Cache slam defense using a semaphore to prevent dogpile effect.
* [Stash](https://github.com/tedious/Stash) [![GitHub stars](https://img.shields.io/github/stars/tedious/Stash?style=flat)](https://github.com/tedious/Stash/stargazers) - Another library for caching.
* [Laminas Cache](https://github.com/laminas/laminas-cache) [![GitHub stars](https://img.shields.io/github/stars/laminas/laminas-cache?style=flat)](https://github.com/laminas/laminas-cache/stargazers) - Another caching library.
* [Lock](https://github.com/php-lock/lock) [![GitHub stars](https://img.shields.io/github/stars/php-lock/lock?style=flat)](https://github.com/php-lock/lock/stargazers) - A lock library to provide exclusive execution.

### Data Structure and Storage
*Libraries that implement data structure or storage techniques.*

* [CakePHP Collection](https://github.com/cakephp/collection) [![GitHub stars](https://img.shields.io/github/stars/cakephp/collection?style=flat)](https://github.com/cakephp/collection/stargazers) - A simple collections library.
* [Fractal](https://github.com/thephpleague/fractal) [![GitHub stars](https://img.shields.io/github/stars/thephpleague/fractal?style=flat)](https://github.com/thephpleague/fractal/stargazers) - A library for converting complex data structures to JSON output.
* [JsonMapper](https://github.com/cweiske/jsonmapper) [![GitHub stars](https://img.shields.io/github/stars/cweiske/jsonmapper?style=flat)](https://github.com/cweiske/jsonmapper/stargazers) - A library that maps nested JSON structures onto PHP classes.
* [JSON Machine](https://github.com/halaxa/json-machine) [![GitHub stars](https://img.shields.io/github/stars/halaxa/json-machine?style=flat)](https://github.com/halaxa/json-machine/stargazers) - Provides iteration over huge JSONs using simple `foreach`.
* [msgpack.php](https://github.com/rybakit/msgpack.php) [![GitHub stars](https://img.shields.io/github/stars/rybakit/msgpack.php?style=flat)](https://github.com/rybakit/msgpack.php/stargazers) - A pure PHP implementation of the [MessagePack](https://msgpack.org/) serialization format.
* [Serializer](https://github.com/schmittjoh/serializer) [![GitHub stars](https://img.shields.io/github/stars/schmittjoh/serializer?style=flat)](https://github.com/schmittjoh/serializer/stargazers) - A library for serializing and de-serializing data.
* [YaLinqo](https://github.com/Athari/YaLinqo) [![GitHub stars](https://img.shields.io/github/stars/Athari/YaLinqo?style=flat)](https://github.com/Athari/YaLinqo/stargazers) - Yet Another LINQ to Objects for PHP.
* [Laminas Serializer](https://github.com/laminas/laminas-serializer) [![GitHub stars](https://img.shields.io/github/stars/laminas/laminas-serializer?style=flat)](https://github.com/laminas/laminas-serializer/stargazers) - Another library for serialising and de-serialising data.

### Notifications
*Libraries for working with notification software.*

* [JoliNotif](https://github.com/jolicode/JoliNotif) [![GitHub stars](https://img.shields.io/github/stars/jolicode/JoliNotif?style=flat)](https://github.com/jolicode/JoliNotif/stargazers) - A cross-platform library for desktop notification (support for Growl, notify-send, toaster, etc).

### Deployment
*Libraries for project deployment.*

* [Deployer](https://github.com/deployphp/deployer) [![GitHub stars](https://img.shields.io/github/stars/deployphp/deployer?style=flat)](https://github.com/deployphp/deployer/stargazers) - A deployment tool.
* [Envoy](https://github.com/laravel/envoy) [![GitHub stars](https://img.shields.io/github/stars/laravel/envoy?style=flat)](https://github.com/laravel/envoy/stargazers) - A tool to run SSH tasks with PHP.

### Internationalisation and Localisation
*Libraries for Internationalization (I18n) and Localization (L10n).*

* [Aura.Intl](https://github.com/auraphp/Aura.Intl) [![GitHub stars](https://img.shields.io/github/stars/auraphp/Aura.Intl?style=flat)](https://github.com/auraphp/Aura.Intl/stargazers) - Provides internationalization (I18N) tools, specifically package-oriented per-locale message translation.
* [CakePHP I18n](https://github.com/cakephp/i18n) [![GitHub stars](https://img.shields.io/github/stars/cakephp/i18n?style=flat)](https://github.com/cakephp/i18n/stargazers) - Message translation and localization for dates and numbers.

### Serverless
*Libraries and tools to help build serverless web applications.*

* [Bref](https://bref.sh/) - Serverless PHP on AWS Lambda.
* [OpenWhisk](https://openwhisk.apache.org/) - An open-source serverless cloud platform.
* [Serverless Framework](https://www.serverless.com/framework) - An open-source framework for building serverless applications.
* [Laravel Vapor](https://vapor.laravel.com/) - A serverless deployment platform for Laravel, powered by AWS.

### Configuration
*Libraries and tools for configuration.*

* [PHP Dotenv](https://github.com/vlucas/phpdotenv) [![GitHub stars](https://img.shields.io/github/stars/vlucas/phpdotenv?style=flat)](https://github.com/vlucas/phpdotenv/stargazers) - Parse and load environment variables from `.env` files.
* [Symfony Dotenv](https://github.com/symfony/dotenv) [![GitHub stars](https://img.shields.io/github/stars/symfony/dotenv?style=flat)](https://github.com/symfony/dotenv/stargazers) - Parse and load environment variables from `.env` files.
* [Toml](https://github.com/php-collective/toml) [![GitHub stars](https://img.shields.io/github/stars/php-collective/toml?style=flat)](https://github.com/php-collective/toml/stargazers) - A TOML parser and encoder with AST access and error recovery.

### LLMs
*Libraries for working with Large Language Models.*

* [Anthropic](https://github.com/mozex/anthropic-php) [![GitHub stars](https://img.shields.io/github/stars/mozex/anthropic-php?style=flat)](https://github.com/mozex/anthropic-php/stargazers) - A PHP client for the Anthropic API, supporting messages, streaming, tool use, and batch processing.
* [Anthropic for Laravel](https://github.com/mozex/anthropic-laravel) [![GitHub stars](https://img.shields.io/github/stars/mozex/anthropic-laravel?style=flat)](https://github.com/mozex/anthropic-laravel/stargazers) - A Laravel wrapper for the Anthropic PHP client with Facades, config publishing, and testing fakes.
* [Instructor for PHP](https://github.com/cognesy/instructor-php) [![GitHub stars](https://img.shields.io/github/stars/cognesy/instructor-php?style=flat)](https://github.com/cognesy/instructor-php/stargazers) - Structured data outputs with LLMs, in PHP.
* [LLPhant](https://github.com/LLPhant/LLPhant) [![GitHub stars](https://img.shields.io/github/stars/LLPhant/LLPhant?style=flat)](https://github.com/LLPhant/LLPhant/stargazers) - A comprehensive PHP Generative AI Framework using OpenAI GPT 4. Inspired by Langchain.
* [OpenAI Client](https://github.com/openai-php/client) [![GitHub stars](https://img.shields.io/github/stars/openai-php/client?style=flat)](https://github.com/openai-php/client/stargazers) - OpenAI PHP is a supercharged community-maintained PHP API client that allows you to interact with OpenAI API.
* [OpenAI Client for Laravel](https://github.com/openai-php/laravel) [![GitHub stars](https://img.shields.io/github/stars/openai-php/laravel?style=flat)](https://github.com/openai-php/laravel/stargazers) - OpenAI PHP for Laravel is a supercharged PHP API client that allows you to interact with OpenAI API.
* [PHP Mistral AI SDK](https://github.com/SoftCreatR/php-mistral-ai-sdk) [![GitHub stars](https://img.shields.io/github/stars/SoftCreatR/php-mistral-ai-sdk?style=flat)](https://github.com/SoftCreatR/php-mistral-ai-sdk/stargazers) - A powerful and easy-to-use PHP SDK for the Mistral AI API, allowing seamless integration of advanced AI-powered features into your PHP projects.

### Third Party APIs
*Libraries for accessing third party APIs.*

* [Amazon Web Service SDK](https://github.com/aws/aws-sdk-php) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-php?style=flat)](https://github.com/aws/aws-sdk-php/stargazers) - The official PHP AWS SDK library.
* [AsyncAWS](https://async-aws.com/) - An unofficial asynchronous PHP AWS SDK.
* [Campaign Monitor](https://campaignmonitor.github.io/createsend-php/) - The official Campaign Monitor PHP library.
* [Github](https://github.com/KnpLabs/php-github-api) [![GitHub stars](https://img.shields.io/github/stars/KnpLabs/php-github-api?style=flat)](https://github.com/KnpLabs/php-github-api/stargazers) - A library to interface with the Github API.
* [Mailgun](https://github.com/mailgun/mailgun-php) [![GitHub stars](https://img.shields.io/github/stars/mailgun/mailgun-php?style=flat)](https://github.com/mailgun/mailgun-php/stargazers) - The official Mailgun PHP API.
* [Stripe](https://github.com/stripe/stripe-php) [![GitHub stars](https://img.shields.io/github/stars/stripe/stripe-php?style=flat)](https://github.com/stripe/stripe-php/stargazers) - The official Stripe PHP library.
* [Twilio](https://github.com/twilio/twilio-php) [![GitHub stars](https://img.shields.io/github/stars/twilio/twilio-php?style=flat)](https://github.com/twilio/twilio-php/stargazers) - The official Twilio PHP REST API.

### Extensions
*Libraries to help build PHP extensions.*

* [PHP CPP](https://www.php-cpp.com/) - A C++ library for developing PHP extensions.
* [Zephir](https://github.com/zephir-lang/zephir) [![GitHub stars](https://img.shields.io/github/stars/zephir-lang/zephir?style=flat)](https://github.com/zephir-lang/zephir/stargazers) - A compiled language between PHP and C++ for developing PHP extensions.

### Miscellaneous
*Useful libraries or utilities that don't fit into the categories above.*

* [Annotations](https://github.com/doctrine/annotations) [![GitHub stars](https://img.shields.io/github/stars/doctrine/annotations?style=flat)](https://github.com/doctrine/annotations/stargazers) - An annotation library (part of Doctrine).
* [BotMan](https://github.com/botman/botman) [![GitHub stars](https://img.shields.io/github/stars/botman/botman?style=flat)](https://github.com/botman/botman/stargazers) - A framework agnostic PHP library to build cross-platform chatbots.
* [ClassPreloader](https://github.com/ClassPreloader/ClassPreloader) [![GitHub stars](https://img.shields.io/github/stars/ClassPreloader/ClassPreloader?style=flat)](https://github.com/ClassPreloader/ClassPreloader/stargazers) - A library for optimizing autoloading.
* [Ganesha](https://github.com/ackintosh/ganesha) [![GitHub stars](https://img.shields.io/github/stars/ackintosh/ganesha?style=flat)](https://github.com/ackintosh/ganesha/stargazers) - A PHP implementation of Circuit Breaker pattern.
* [Hprose-PHP](https://github.com/hprose/hprose-php) [![GitHub stars](https://img.shields.io/github/stars/hprose/hprose-php?style=flat)](https://github.com/hprose/hprose-php/stargazers) - A cross-language RPC.
* [Laravel Serializable Closure](https://github.com/laravel/serializable-closure) [![GitHub stars](https://img.shields.io/github/stars/laravel/serializable-closure?style=flat)](https://github.com/laravel/serializable-closure/stargazers) - A library that allows Closures to be serialized.
* [noCAPTCHA](https://github.com/ARCANEDEV/noCAPTCHA) [![GitHub stars](https://img.shields.io/github/stars/ARCANEDEV/noCAPTCHA?style=flat)](https://github.com/ARCANEDEV/noCAPTCHA/stargazers) - Helper for Google's noCAPTCHA (reCAPTCHA).
* [Pagerfanta](https://github.com/whiteoctober/Pagerfanta) [![GitHub stars](https://img.shields.io/github/stars/whiteoctober/Pagerfanta?style=flat)](https://github.com/whiteoctober/Pagerfanta/stargazers) - A pagination library.
* [Safe](https://github.com/thecodingmachine/safe) [![GitHub stars](https://img.shields.io/github/stars/thecodingmachine/safe?style=flat)](https://github.com/thecodingmachine/safe/stargazers) - All PHP functions, rewritten to throw exceptions instead of returning false.

# Software
*Software for creating a development environment.*

### PHP Installation
*Tools to help install and manage PHP on your computer.*

* [Brew PHP Switcher](https://github.com/philcook/brew-php-switcher) [![GitHub stars](https://img.shields.io/github/stars/philcook/brew-php-switcher?style=flat)](https://github.com/philcook/brew-php-switcher/stargazers) - Brew PHP switcher.
* [Homebrew](https://brew.sh/) - A package manager for macOS.
* [PHP Brew](https://github.com/phpbrew/phpbrew) [![GitHub stars](https://img.shields.io/github/stars/phpbrew/phpbrew?style=flat)](https://github.com/phpbrew/phpbrew/stargazers) - A PHP version manager and installer.
* [PHP Build](https://github.com/php-build/php-build) [![GitHub stars](https://img.shields.io/github/stars/php-build/php-build?style=flat)](https://github.com/php-build/php-build/stargazers) - Another PHP version installer.
* [Static PHP CLI](https://github.com/crazywhalecc/static-php-cli) [![GitHub stars](https://img.shields.io/github/stars/crazywhalecc/static-php-cli?style=flat)](https://github.com/crazywhalecc/static-php-cli/stargazers) - Build or [download](https://dl.static-php.dev/static-php-cli/) static versions of PHP CLI and FPM.

### Development Environment
*Software and tools for creating and sharing a development environment.*

* [Ansible](https://www.redhat.com/en/ansible-collaborative) - A radically simple orchestration framework.
* [DDEV](https://github.com/ddev/ddev) [![GitHub stars](https://img.shields.io/github/stars/ddev/ddev?style=flat)](https://github.com/ddev/ddev/stargazers) - A local web development environment system for PHP.
* [Docker](https://www.docker.com/) - A containerization platform.
* [Docker PHP Extension Installer](https://github.com/mlocati/docker-php-extension-installer) [![GitHub stars](https://img.shields.io/github/stars/mlocati/docker-php-extension-installer?style=flat)](https://github.com/mlocati/docker-php-extension-installer/stargazers) - Easily install PHP extensions in Docker containers.
* [Docksal](https://github.com/docksal/docksal) [![GitHub stars](https://img.shields.io/github/stars/docksal/docksal?style=flat)](https://github.com/docksal/docksal/stargazers) - Unified, Docker :whale: powered web development environments for macOS, Windows, and Linux.
* [Expose](https://github.com/exposedev/expose) [![GitHub stars](https://img.shields.io/github/stars/exposedev/expose?style=flat)](https://github.com/exposedev/expose/stargazers) - An open-source PHP tunneling service.
* [Lando](https://lando.dev/) - Push-button development environments.
* [Laravel Homestead](https://laravel.com/docs/master/homestead) - A local development environment for Laravel.
* [Laravel Herd](https://herd.laravel.com/windows) - A one click PHP development environment for macOS and Windows.
* [Laradock](https://laradock.io/) - A full PHP development environment based on Docker.
* [PHPMon](https://phpmon.app/) - A macOS menu bar app for managing PHP installations (works with [Laravel Valet](https://laravel.com/docs/master/valet)).
* [Puppet](https://www.puppet.com) - A server automation framework and application.
* [Solo](https://github.com/soloterm/solo) [![GitHub stars](https://img.shields.io/github/stars/soloterm/solo?style=flat)](https://github.com/soloterm/solo/stargazers) - A terminal application to manage processes for a Laravel application.
* [Takeout](https://github.com/tighten/takeout) [![GitHub stars](https://img.shields.io/github/stars/tighten/takeout?style=flat)](https://github.com/tighten/takeout/stargazers) - A Docker-based development-only dependency manager.
* [Vagrant](https://developer.hashicorp.com/vagrant) - A portable development environment utility.

### Virtual Machines
*Alternative PHP virtual machines.*

* [Hack](https://hacklang.org/) - A programming language for HHVM.
* [HHVM](https://github.com/facebook/hhvm) [![GitHub stars](https://img.shields.io/github/stars/facebook/hhvm?style=flat)](https://github.com/facebook/hhvm/stargazers) - A Virtual Machine, Runtime and JIT for PHP by Facebook.
* [PeachPie](https://github.com/peachpiecompiler/peachpie) [![GitHub stars](https://img.shields.io/github/stars/peachpiecompiler/peachpie?style=flat)](https://github.com/peachpiecompiler/peachpie/stargazers) - PHP compiler and runtime for .NET and .NET Core.

### Text Editors and IDEs
*Text Editors and Integrated Development Environments (IDE) with support for PHP.*

* [Eclipse for PHP Developers](https://www.eclipse.org/downloads/) - A PHP IDE based on the Eclipse platform.
* [Apache NetBeans](https://netbeans.apache.org/front/main/index.html) - An IDE with support for PHP and HTML5.
* [PhpEd](https://www.nusphere.com/products/phped.htm) - An IDE with professional commercial debugger.
* [PhpStorm](https://www.jetbrains.com/phpstorm/) - A commercial PHP IDE.
* [VS Code](https://code.visualstudio.com/) - An open source code editor.

### Web Applications
*Web-based applications and tools.*

* [3V4L](https://3v4l.org/) - An online PHP & HHVM shell.
* [Adminer](https://www.adminer.org/en/) - Database management in a single PHP file.
* [Cachet](https://github.com/cachethq/cachet) [![GitHub stars](https://img.shields.io/github/stars/cachethq/cachet?style=flat)](https://github.com/cachethq/cachet/stargazers) - The open source status page system.
* [Lychee](https://github.com/electerious/Lychee) [![GitHub stars](https://img.shields.io/github/stars/electerious/Lychee?style=flat)](https://github.com/electerious/Lychee/stargazers) - An easy to use and great looking photo-management-system.
* [Leantime](https://leantime.io) - Strategic project management system for the non project manager.
* [MailCatcher](https://github.com/sj26/mailcatcher) [![GitHub stars](https://img.shields.io/github/stars/sj26/mailcatcher?style=flat)](https://github.com/sj26/mailcatcher/stargazers) - A web tool for capturing and viewing emails.
* [Mailpit](https://github.com/axllent/mailpit) [![GitHub stars](https://img.shields.io/github/stars/axllent/mailpit?style=flat)](https://github.com/axllent/mailpit/stargazers) - An email and SMTP testing tool for developers.
* [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) [![GitHub stars](https://img.shields.io/github/stars/phpmyadmin/phpmyadmin?style=flat)](https://github.com/phpmyadmin/phpmyadmin/stargazers) - A web interface for MySQL/MariaDB.
* [PHP Queue](https://github.com/CoderKungfu/php-queue) [![GitHub stars](https://img.shields.io/github/stars/CoderKungfu/php-queue?style=flat)](https://github.com/CoderKungfu/php-queue/stargazers) - An application for managing queueing backends.
* [phpRedisAdmin](https://github.com/ErikDubbelboer/phpRedisAdmin) [![GitHub stars](https://img.shields.io/github/stars/ErikDubbelboer/phpRedisAdmin?style=flat)](https://github.com/ErikDubbelboer/phpRedisAdmin/stargazers) - A simple web interface to manage [Redis](https://redis.io/) databases.
* [PHPSandbox](https://phpsandbox.io) - An online IDE for PHP in the browser.

### Infrastructure
*Infrastructure for providing PHP applications and services.*

* [appserver.io](https://github.com/appserver-io/appserver) [![GitHub stars](https://img.shields.io/github/stars/appserver-io/appserver?style=flat)](https://github.com/appserver-io/appserver/stargazers) - A multithreaded application server for PHP, written in PHP.
* [php-pm](https://github.com/php-pm/php-pm) [![GitHub stars](https://img.shields.io/github/stars/php-pm/php-pm?style=flat)](https://github.com/php-pm/php-pm/stargazers) - A process manager, supercharger and load balancer for PHP applications.
* [RoadRunner](https://github.com/roadrunner-server/roadrunner) [![GitHub stars](https://img.shields.io/github/stars/roadrunner-server/roadrunner?style=flat)](https://github.com/roadrunner-server/roadrunner/stargazers) - High-performance PHP application server, load-balancer and process manager.

# Resources
Various resources, such as books, websites and articles, for improving your PHP development skills and knowledge.

### PHP Websites
*Useful PHP-related websites.*

* [Nomad PHP](https://nomadphp.com/) - A online PHP learning resource.
* [Laravel News](https://laravel-news.com/) - The official Laravel blog.
* [PHP Annotated Monthly](https://blog.jetbrains.com/phpstorm/tag/php-annotated-monthly/) - A monthly digest of PHP news.
* [PHP FIG](https://www.php-fig.org/) - The PHP Framework Interoperability Group.
* [PHP Package Development Standards](https://php-pds.com/) - Package development standards for PHP.
* [PHP School](https://www.phpschool.io/) - Open Source Learning for PHP.
* [PHP The Right Way](https://phptherightway.com/) - A PHP best practice quick reference guide.
* [PHP UG](https://php.ug) - A website to help people locate their nearest PHP user group (UG).
* [PHP Watch](https://php.watch/) - PHP articles, news, upcoming changes, RFCs and more.
* [Unit Testing Tips](https://testing-tips.sarvendev.com/) - Unit Testing Tips by examples in PHP.

### PHP Books
*Fantastic PHP-related books.*

* [Domain-Driven Design in PHP](https://leanpub.com/ddd-in-php) - Real examples written in PHP showcasing DDD Architectural Styles.
* [Functional Programming in PHP](https://www.functionalphp.com/) - A book on applying functional programming principles and techniques in PHP.
* [Mastering Object-Orientated PHP](https://masteringobjectorientedphp.com/) - A book about object-orientated PHP by Brandon Savage.
* [PHP Cookbook](https://www.oreilly.com/library/view/php-cookbook/9781098121310/) - This cookbook provides code recipes to help you resolve a variety of coding issues.
* [Modernizing Legacy Applications in PHP](https://leanpub.com/mlaphp) - A book about modernizing legacy PHP applications by Paul M. Jones.
* [Scaling PHP Applications](https://www.scalingphpbook.com) - An ebook about scaling PHP applications by Steve Corona.
* [Securing PHP: Core Concepts](https://leanpub.com/securingphp-coreconcepts) - A book about common security terms and practices for PHP by Chris Cornutt.
* [Signaling PHP](https://leanpub.com/signalingphp) - A book about catching PCNTL signals in CLI scripts by Cal Evans.
* [XML Parsing with PHP](https://www.phparch.com/books/xml-parsing-with-php/) - This book covers parsing and validating XML documents, leveraging XPath expressions, and working with namespaces as well as how to create and modify XML files programmatically.

### PHP Videos
*Fantastic PHP-related videos.*

* [Laracasts](https://laracasts.com) - Screencasts about Laravel, Vue JS and more.
* [Laravel YouTube Channel](https://www.youtube.com/channel/UCfO2GiQwb-cwJTb1CuRSkwg) - The official Laravel YouTube channel.
* [Program With Gio](https://www.youtube.com/playlist?list=PLr3d3QYzkw2xabQRUpcZ_IBk9W50M9pe-) - PHP 8 course by Gio.
* [Programming with Anthony](https://www.youtube.com/playlist?list=PLM-218uGSX3DQ3KsB5NJnuOqPqc5CW2kW) - A video series by Anthony Ferrara.
* [SymfonyCasts](https://symfonycasts.com/) - Screencasts and tutorials about PHP and Symfony.

### PHP Conferences
*PHP conferences.*

* [Laracon EU](https://www.youtube.com/@LaraconEU) - Laracon EU is a 2-day event for people who are interested in learning Laravel and related technologies, or who want to share their knowledge with others.
* [PHP[TEK]](https://phptek.io/) - The longest-running web developer conference in the United States that has a focus on the PHP programming language.
* [PHP UK Conference](https://www.youtube.com/user/phpukconference/videos) - A collection of videos from the PHP UK Conference.

### PHP Podcasts
*Podcasts with a focus on PHP topics.*

* [Laravel News Podcast](https://podcast.laravel-news.com/) - The Laravel News Podcast brings you all the latest news and events related to the Laravel PHP Framework.
* [Mostly Technical](https://mostlytechnical.com/) - Hosted by Ian Landsman and Aaron Francis, Mostly Technical is a lively discussion on Laravel, business, and an eclectic mix of related topics.
* [No Compromises](https://show.nocompromises.io/) - Two seasoned salty programming veterans talk best practices based on years of working with Laravel SaaS teams.
* [North Meets South Web Podcast](https://www.northmeetssouth.audio/) - Jacob Bennett and Michael Dyrynda conquer a 14.5 hour time difference to talk about life as web developers.
* [Over Engineered](https://overengineered.fm/) - A podcast in mini-series where we explore unimportant programming questions in extreme detail.
* [PHP Internals News](https://phpinternals.news) - A podcast about PHP internals.
* [PHP Town Hall](https://phptownhall.com/) - A casual PHP podcast by Ben Edmunds and Phil Sturgeon.
* [php[podcast] episodes from php[architect]](https://www.phparch.com/podcast/) - The official podcast of php[architect] the industry's leading tech magazine and publisher focused on PHP and web development.
* [PHPUgly](https://www.phpugly.com/) - The ramblings of a few overworked PHP Developers.
* [The Laracasts Snippet](https://laracasts.simplecast.com) - The Laracasts snippet, each episode, offers a single thought on some aspect of web development.
* [The Laravel Podcast](https://laravelpodcast.com/) - Laravel and PHP development news and discussion.
* [The PHP Roundtable](https://phproundtable.com/) - The PHP Roundtable is a casual gathering of developers discussing topics that PHP nerds care about.

### PHP Newsletters
*PHP-related news directly to your inbox.*

* [PHP Weekly](https://www.phpweekly.com/) - A weekly newsletter about PHP.

### PHP Reading
*PHP-related reading materials.*

* [php[architect]](https://www.phparch.com/magazine/) - A monthly magazine dedicated to PHP.

### PHP Internals Reading
*Reading materials related to the PHP internals or performance.*

* [PHP RFCs](https://wiki.php.net/rfc) - The home of PHP RFCs (Request for Comments).
* [Externals](https://externals.io/) - PHP internal discussions.
* [PHP RFC Watch](https://github.com/beberlei/php-rfc-watch) [![GitHub stars](https://img.shields.io/github/stars/beberlei/php-rfc-watch?style=flat)](https://github.com/beberlei/php-rfc-watch/stargazers) - Watch the latest PHP [RFCs](https://wiki.php.net/rfc).
* [PHP Internals Book](https://www.phpinternalsbook.com/) - An online book about PHP internals, written by three core developers.
