# Gems

[![GitHub stars](https://img.shields.io/github/stars/hothero/awesome-rails-gem?style=flat)](https://github.com/hothero/awesome-rails-gem/stargazers)

# Awesome Rails Gem [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A collection of awesome Ruby Gems for Rails development.

The goal is to help every Rails developer to build an awesome Rails product/service.

* [Rails Gem List](#rails-gem-list)
  * [User](#user)
  * [Active Record](#active-record)
  * [Plugins](#plugins)
  * [API](#api)
  * [Email](#email)
  * [File Uploading](#file-uploading)
  * [Searching](#searching)
  * [Scheduled/Recurrence Jobs](#scheduledrecurrence-jobs)
  * [View Helper](#view-helper)
  * [Environment Variables](#environment-variables)
  * [Admin Panel](#admin-panel)
  * [Logging](#logging)
  * [Debug](#debug)
  * [Coding Style](#coding-style)
  * [Testing](#testing)
  * [Production](#production)
  * [Error Logging](#error-logging)
  * [Database](#database)

## User

### Authentication
* [Devise](https://github.com/plataformatec/devise/) [![GitHub stars](https://img.shields.io/github/stars/plataformatec/devise/?style=flat)](https://github.com/plataformatec/devise//stargazers) - Devise is a flexible authentication solution for Rails based on Warden.
* [Knock](https://github.com/nsarno/knock) [![GitHub stars](https://img.shields.io/github/stars/nsarno/knock?style=flat)](https://github.com/nsarno/knock/stargazers) - Seamless JWT authentication for Rails API.
* [Clearance](https://github.com/thoughtbot/clearance) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/clearance?style=flat)](https://github.com/thoughtbot/clearance/stargazers) - Rails authentication with email & password.
* [Devise token auth](https://github.com/lynndylanhurley/devise_token_auth) [![GitHub stars](https://img.shields.io/github/stars/lynndylanhurley/devise_token_auth?style=flat)](https://github.com/lynndylanhurley/devise_token_auth/stargazers) - Token based authentication for Rails JSON APIs.
* [Sorcery](https://github.com/Sorcery/sorcery) [![GitHub stars](https://img.shields.io/github/stars/Sorcery/sorcery?style=flat)](https://github.com/Sorcery/sorcery/stargazers) - Magical Authentication for Rails. Supports ActiveRecord, DataMapper, Mongoid and MongoMapper.

### Authorization
* [Pundit](https://github.com/elabs/pundit) [![GitHub stars](https://img.shields.io/github/stars/elabs/pundit?style=flat)](https://github.com/elabs/pundit/stargazers) - Pundit provides a set of helpers which guide you in leveraging regular Ruby classes and object oriented design patterns to build a simple, robust and scaleable authorization system.
* [cancancan](https://github.com/CanCanCommunity/cancancan) [![GitHub stars](https://img.shields.io/github/stars/CanCanCommunity/cancancan?style=flat)](https://github.com/CanCanCommunity/cancancan/stargazers) - Continuation of CanCan, the authorization Gem for Ruby on Rails.CanCan is an authorization library for Ruby on Rails which restricts what resources a given user is allowed to access. All permissions are defined in a single location (the Ability class) and not duplicated across controllers, views, and database queries.
* [rolify](https://github.com/RolifyCommunity/rolify) [![GitHub stars](https://img.shields.io/github/stars/RolifyCommunity/rolify?style=flat)](https://github.com/RolifyCommunity/rolify/stargazers) - Role management library with resource scoping.
* [acl9](https://github.com/be9/acl9/) [![GitHub stars](https://img.shields.io/github/stars/be9/acl9/?style=flat)](https://github.com/be9/acl9//stargazers) - Acl9 is a role-based authorization system that provides a concise DSL for securing your Rails application.


### Omniauth
* [omniauth-facebook](https://github.com/mkdynamic/omniauth-facebook) [![GitHub stars](https://img.shields.io/github/stars/mkdynamic/omniauth-facebook?style=flat)](https://github.com/mkdynamic/omniauth-facebook/stargazers)
* [omniauth-google-oauth2](https://github.com/zquestz/omniauth-google-oauth2) [![GitHub stars](https://img.shields.io/github/stars/zquestz/omniauth-google-oauth2?style=flat)](https://github.com/zquestz/omniauth-google-oauth2/stargazers)
* [omniauth-weibo-oauth2](https://github.com/beenhero/omniauth-weibo-oauth2) [![GitHub stars](https://img.shields.io/github/stars/beenhero/omniauth-weibo-oauth2?style=flat)](https://github.com/beenhero/omniauth-weibo-oauth2/stargazers)
* [omniauth-twitter](https://github.com/arunagw/omniauth-twitter) [![GitHub stars](https://img.shields.io/github/stars/arunagw/omniauth-twitter?style=flat)](https://github.com/arunagw/omniauth-twitter/stargazers)
* [omniauth-github](https://github.com/intridea/omniauth-github) [![GitHub stars](https://img.shields.io/github/stars/intridea/omniauth-github?style=flat)](https://github.com/intridea/omniauth-github/stargazers)
* [omniauth-linkedin-oauth2](https://github.com/decioferreira/omniauth-linkedin-oauth2) [![GitHub stars](https://img.shields.io/github/stars/decioferreira/omniauth-linkedin-oauth2?style=flat)](https://github.com/decioferreira/omniauth-linkedin-oauth2/stargazers)

## Active Record
* [Enumerize](https://github.com/brainspec/enumerize) [![GitHub stars](https://img.shields.io/github/stars/brainspec/enumerize?style=flat)](https://github.com/brainspec/enumerize/stargazers) - Enumerated attributes with I18n and ActiveRecord/Mongoid support. It can be integrated with Simple Form.
* [counter_culture](https://github.com/magnusvk/counter_culture) [![GitHub stars](https://img.shields.io/github/stars/magnusvk/counter_culture?style=flat)](https://github.com/magnusvk/counter_culture/stargazers) - Turbo-charged counter caches for your Rails app. Huge improvements over the Rails standard counter caches.
* [custom_counter_cache](https://github.com/cedric/custom_counter_cache) [![GitHub stars](https://img.shields.io/github/stars/cedric/custom_counter_cache?style=flat)](https://github.com/cedric/custom_counter_cache/stargazers) - A simple approach to creating a custom counter cache that can be used across multiple models.
* [Sequenced](https://github.com/djreimer/sequenced) [![GitHub stars](https://img.shields.io/github/stars/djreimer/sequenced?style=flat)](https://github.com/djreimer/sequenced/stargazers) - Sequenced is a simple gem that generates scoped sequential IDs for ActiveRecord models.
* [FriendlyId](https://github.com/norman/friendly_id) [![GitHub stars](https://img.shields.io/github/stars/norman/friendly_id?style=flat)](https://github.com/norman/friendly_id/stargazers) - FriendlyId is the “Swiss Army bulldozer” of slugging and permalink plugins for ActiveRecord. It allows you to create pretty URL’s and work with human-friendly strings as if they were numeric ids for ActiveRecord models.
* [AASM](https://github.com/aasm/aasm) [![GitHub stars](https://img.shields.io/github/stars/aasm/aasm?style=flat)](https://github.com/aasm/aasm/stargazers) - State machines for Ruby classes (plain Ruby, Rails Active Record, Mongoid).
* [PaperTrail](https://github.com/airblade/paper_trail) [![GitHub stars](https://img.shields.io/github/stars/airblade/paper_trail?style=flat)](https://github.com/airblade/paper_trail/stargazers) - PaperTrail lets you track changes to your models' data. It's good for auditing or versioning.
* [paranoia](https://github.com/rubysherpas/paranoia) [![GitHub stars](https://img.shields.io/github/stars/rubysherpas/paranoia?style=flat)](https://github.com/rubysherpas/paranoia/stargazers) - ActiveRecord plugin allowing you to hide and restore records without actually deleting them.
* [Validates](https://github.com/kaize/validates) [![GitHub stars](https://img.shields.io/github/stars/kaize/validates?style=flat)](https://github.com/kaize/validates/stargazers) - Validates provides collection of useful custom validators for Rails applications, including:
  * EmailValidator
  * UrlValidator
  * SlugValidator
  * MoneyValidator
  * IpValidator
  * AssociationLengthValidator
  * AbsolutePathValidator
  * UriComponentValidator
  * ColorValidator
  * EanValidator (EAN-8 & EAN-13)
* [globalize](https://github.com/globalize/globalize) [![GitHub stars](https://img.shields.io/github/stars/globalize/globalize?style=flat)](https://github.com/globalize/globalize/stargazers) - Rails I18n de-facto standard library for ActiveRecord model/data translation.
* [deep_cloneable](https://github.com/moiristo/deep_cloneable) [![GitHub stars](https://img.shields.io/github/stars/moiristo/deep_cloneable?style=flat)](https://github.com/moiristo/deep_cloneable/stargazers) - This gem gives every ActiveRecord::Base object the possibility to do a deep clone that includes user specified associations.
* [social_shares](https://github.com/Timrael/social_shares) [![GitHub stars](https://img.shields.io/github/stars/Timrael/social_shares?style=flat)](https://github.com/Timrael/social_shares/stargazers) - Check how many times url was shared in social networks.
* [public_activity](https://github.com/chaps-io/public_activity) [![GitHub stars](https://img.shields.io/github/stars/chaps-io/public_activity?style=flat)](https://github.com/chaps-io/public_activity/stargazers) - Easy activity tracking for models - similar to Github's Public Activity.
* [goldiloader](https://github.com/salsify/goldiloader) [![GitHub stars](https://img.shields.io/github/stars/salsify/goldiloader?style=flat)](https://github.com/salsify/goldiloader/stargazers) - Automatic ActiveRecord eager loading to reduce the number of database queries run by your application.
* Tagging
  * [ActsAsTaggableOn](https://github.com/mbleigh/acts-as-taggable-on) [![GitHub stars](https://img.shields.io/github/stars/mbleigh/acts-as-taggable-on?style=flat)](https://github.com/mbleigh/acts-as-taggable-on/stargazers) - A tagging plugin for Rails applications that allows for custom tagging along dynamic contexts.
  * [closure_tree](https://github.com/mceachen/closure_tree) [![GitHub stars](https://img.shields.io/github/stars/mceachen/closure_tree?style=flat)](https://github.com/mceachen/closure_tree/stargazers) - Easily and efficiently make your ActiveRecord models support hierarchies.
* [ActionStore](https://github.com/rails-engine/action-store) [![GitHub stars](https://img.shields.io/github/stars/rails-engine/action-store?style=flat)](https://github.com/rails-engine/action-store/stargazers) - Store different kind of actions (Like, Follow, Star, Block ...) in one table via ActiveRecord Polymorphic Association.

## Plugins
* [Spreadsheet](https://github.com/zdavatz/spreadsheet) [![GitHub stars](https://img.shields.io/github/stars/zdavatz/spreadsheet?style=flat)](https://github.com/zdavatz/spreadsheet/stargazers) - Library is designed to read and write Spreadsheet Documents.
* [Chartkick](https://github.com/ankane/chartkick) [![GitHub stars](https://img.shields.io/github/stars/ankane/chartkick?style=flat)](https://github.com/ankane/chartkick/stargazers) - Chartkick helps your to create beautiful Javascript charts with one line of Ruby.
* [kaminari](https://github.com/amatsuda/kaminari) [![GitHub stars](https://img.shields.io/github/stars/amatsuda/kaminari?style=flat)](https://github.com/amatsuda/kaminari/stargazers) - A Scope & Engine based, clean, powerful, customizable and sophisticated paginator for Rails 3 and 4.
* [CKEditor](https://github.com/galetahub/ckeditor) [![GitHub stars](https://img.shields.io/github/stars/galetahub/ckeditor?style=flat)](https://github.com/galetahub/ckeditor/stargazers) - CKEditor is a WYSIWYG text editor designed to simplify web content creation. It brings common word processing features directly to your web pages. Enhance your website experience with our community maintained editor. [ckeditor.com](http://ckeditor.com)
* [HTML::Pipeline](https://github.com/jch/html-pipeline) [![GitHub stars](https://img.shields.io/github/stars/jch/html-pipeline?style=flat)](https://github.com/jch/html-pipeline/stargazers) - GitHub HTML processing filters and utilities. This module includes a small framework for defining DOM based content filters and applying them to user provided content.
* [Slack Notifier](https://github.com/stevenosloan/slack-notifier) [![GitHub stars](https://img.shields.io/github/stars/stevenosloan/slack-notifier?style=flat)](https://github.com/stevenosloan/slack-notifier/stargazers) is a simple wrapper to send notifications to [Slack](https://slack.com/) webhooks.
* [Rails ERD](https://github.com/voormedia/rails-erd) [![GitHub stars](https://img.shields.io/github/stars/voormedia/rails-erd?style=flat)](https://github.com/voormedia/rails-erd/stargazers) - Generate Entity-Relationship Diagrams for Rails applications.
* [Parity](https://github.com/thoughtbot/parity) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/parity?style=flat)](https://github.com/thoughtbot/parity/stargazers) - Shell commands for development, staging, and production parity for Heroku apps.
* [Airbrussh](https://github.com/mattbrictson/airbrussh) [![GitHub stars](https://img.shields.io/github/stars/mattbrictson/airbrussh?style=flat)](https://github.com/mattbrictson/airbrussh/stargazers) - Airbrussh pretties up your SSHKit and Capistrano output

## API
* [Grape](https://github.com/ruby-grape/grape) [![GitHub stars](https://img.shields.io/github/stars/ruby-grape/grape?style=flat)](https://github.com/ruby-grape/grape/stargazers) - Microframework to create REST-ful APIs in Ruby.
* [ActiveModel::Serializers](https://github.com/rails-api/active_model_serializers) [![GitHub stars](https://img.shields.io/github/stars/rails-api/active_model_serializers?style=flat)](https://github.com/rails-api/active_model_serializers/stargazers) - Serializer brings convention over configuration to your JSON generation.
* [Jbuilder](https://github.com/rails/jbuilder) [![GitHub stars](https://img.shields.io/github/stars/rails/jbuilder?style=flat)](https://github.com/rails/jbuilder/stargazers) - Jbuilder gives you a simple DSL for declaring JSON structures that beats massaging giant hash structures. This is particularly helpful when the generation process is fraught with conditionals and loops.
* [rest-client](https://github.com/rest-client/rest-client) [![GitHub stars](https://img.shields.io/github/stars/rest-client/rest-client?style=flat)](https://github.com/rest-client/rest-client/stargazers) - Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions.
* [has_scope](https://github.com/plataformatec/has_scope) [![GitHub stars](https://img.shields.io/github/stars/plataformatec/has_scope?style=flat)](https://github.com/plataformatec/has_scope/stargazers) - Map incoming controller parameters to named scopes in your resources.
* Documentation
	* [Grape Swagger](https://github.com/ruby-grape/grape-swagger) [![GitHub stars](https://img.shields.io/github/stars/ruby-grape/grape-swagger?style=flat)](https://github.com/ruby-grape/grape-swagger/stargazers) - Autogenerate documentation on Grape API.
	* [Grape Swagger UI](https://github.com/swagger-api/swagger-ui) [![GitHub stars](https://img.shields.io/github/stars/swagger-api/swagger-ui?style=flat)](https://github.com/swagger-api/swagger-ui/stargazers) - Display documentation that is generated using Grape Swagger.
	* [apiary](https://apiary.io/) - Work together to quickly design, prototype, document and test APIs.
	* [apiblueprint](https://apiblueprint.org) - API Documentation with powerful tooling.

## Email
* [letter_opener](https://github.com/ryanb/letter_opener) [![GitHub stars](https://img.shields.io/github/stars/ryanb/letter_opener?style=flat)](https://github.com/ryanb/letter_opener/stargazers) - Preview mail in the browser instead of sending.

## File Uploading
* [Carrierwave](https://github.com/carrierwaveuploader/carrierwave) [![GitHub stars](https://img.shields.io/github/stars/carrierwaveuploader/carrierwave?style=flat)](https://github.com/carrierwaveuploader/carrierwave/stargazers) - Carrierwave is a classier solution for file uploads for Rails, Sinatra and other Ruby web frameworks.
  * [carrierwave_backgrounder](https://github.com/lardawge/carrierwave_backgrounder) [![GitHub stars](https://img.shields.io/github/stars/lardawge/carrierwave_backgrounder?style=flat)](https://github.com/lardawge/carrierwave_backgrounder/stargazers) - Offload CarrierWave's image processing and storage to a background process using Delayed Job, Resque, Sidekiq, Qu, Queue Classic or Girl Friday.
  * [CarrierWave Crop](https://github.com/kirtithorat/carrierwave-crop/) [![GitHub stars](https://img.shields.io/github/stars/kirtithorat/carrierwave-crop/?style=flat)](https://github.com/kirtithorat/carrierwave-crop//stargazers) - Carrierwave extension to crop uploaded images using Jcrop plugin with preview.
  * [CarrierWave ImageOptimizer](https://github.com/jtescher/carrierwave-imageoptimizer) [![GitHub stars](https://img.shields.io/github/stars/jtescher/carrierwave-imageoptimizer?style=flat)](https://github.com/jtescher/carrierwave-imageoptimizer/stargazers) - This gem allows you to simply optimize CarrierWave images via jpegoptim or optipng using the image_optimizer gem.
* [remotipart](https://github.com/JangoSteve/remotipart) [![GitHub stars](https://img.shields.io/github/stars/JangoSteve/remotipart?style=flat)](https://github.com/JangoSteve/remotipart/stargazers) - Rails jQuery file uploads via standard Rails "remote: true" forms.
* [MiniMagick](https://github.com/minimagick/minimagick) [![GitHub stars](https://img.shields.io/github/stars/minimagick/minimagick?style=flat)](https://github.com/minimagick/minimagick/stargazers) - MiniMagick is a ruby wrapper for ImageMagick or GraphicsMagick command line.
* [fog](https://github.com/fog/fog) [![GitHub stars](https://img.shields.io/github/stars/fog/fog?style=flat)](https://github.com/fog/fog/stargazers) - Fog is the Ruby cloud services library, top to bottom.
* [refile](https://github.com/refile/refile) [![GitHub stars](https://img.shields.io/github/stars/refile/refile?style=flat)](https://github.com/refile/refile/stargazers) - Refile is a modern file upload library for Ruby applications. It is simple, yet powerful.
* [Paperclip](https://github.com/thoughtbot/paperclip) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/paperclip?style=flat)](https://github.com/thoughtbot/paperclip/stargazers) - Easy file attachment management for ActiveRecord.
* [Dragonfly](http://markevans.github.io/dragonfly) - Dragonfly is for on-the-fly file processing - suitable for images or other attachments
* [shrine](https://github.com/janko-m/shrine) [![GitHub stars](https://img.shields.io/github/stars/janko-m/shrine?style=flat)](https://github.com/janko-m/shrine/stargazers) -File Attachment toolkit for Ruby applications  

## Searching
* [ransack](https://github.com/activerecord-hackery/ransack) [![GitHub stars](https://img.shields.io/github/stars/activerecord-hackery/ransack?style=flat)](https://github.com/activerecord-hackery/ransack/stargazers) - Ransack enables the creation of both simple and advanced search forms for your Ruby on Rails application.
* [elasticsearch-rails](https://github.com/elastic/elasticsearch-rails) [![GitHub stars](https://img.shields.io/github/stars/elastic/elasticsearch-rails?style=flat)](https://github.com/elastic/elasticsearch-rails/stargazers) - Elasticsearch integrations for ActiveModel/Record and Ruby on Rails.
* [Chewy](https://github.com/toptal/chewy) [![GitHub stars](https://img.shields.io/github/stars/toptal/chewy?style=flat)](https://github.com/toptal/chewy/stargazers) - High-level Elasticsearch Ruby framework based on the official elasticsearch-ruby client.
* [pg_search](https://github.com/Casecommons/pg_search) [![GitHub stars](https://img.shields.io/github/stars/Casecommons/pg_search?style=flat)](https://github.com/Casecommons/pg_search/stargazers) - pg_search builds ActiveRecord named scopes that take advantage of PostgreSQL's full text search
* [sunspot](https://github.com/sunspot/sunspot) [![GitHub stars](https://img.shields.io/github/stars/sunspot/sunspot?style=flat)](https://github.com/sunspot/sunspot/stargazers) - Sunspot is a Ruby library for expressive, powerful interaction with the Solr search engine. Sunspot is built on top of the RSolr library, which provides a low-level interface for Solr interaction; Sunspot provides a simple, intuitive, expressive DSL backed by powerful features for indexing objects and searching for them.
* [searchkick](https://github.com/ankane/searchkick) [![GitHub stars](https://img.shields.io/github/stars/ankane/searchkick?style=flat)](https://github.com/ankane/searchkick/stargazers) - Intelligent search made easy with Rails and Elasticsearch.

## Scheduled/Recurrence Jobs
* [Whenever](https://github.com/javan/whenever) [![GitHub stars](https://img.shields.io/github/stars/javan/whenever?style=flat)](https://github.com/javan/whenever/stargazers) - Whenever is a Ruby gem that provides a clear syntax for writing and deploying cron jobs.
* [Resque](https://github.com/resque/resque) [![GitHub stars](https://img.shields.io/github/stars/resque/resque?style=flat)](https://github.com/resque/resque/stargazers) - Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later.
* [Rufus-Scheduler](https://github.com/jmettraux/rufus-scheduler) [![GitHub stars](https://img.shields.io/github/stars/jmettraux/rufus-scheduler?style=flat)](https://github.com/jmettraux/rufus-scheduler/stargazers) - Rufus-scheduler is a Ruby gem for scheduling pieces of code (jobs). It understands running a job AT a certain time, IN a certain time, EVERY x time or simply via a CRON statement.
* [Delayed Job](https://github.com/collectiveidea/delayed_job) [![GitHub stars](https://img.shields.io/github/stars/collectiveidea/delayed_job?style=flat)](https://github.com/collectiveidea/delayed_job/stargazers) - Database based asynchronous priority queue system.
* [Sidekiq](https://github.com/mperham/sidekiq) [![GitHub stars](https://img.shields.io/github/stars/mperham/sidekiq?style=flat)](https://github.com/mperham/sidekiq/stargazers) - Simple, efficient background processing for Ruby.
  * [sidetiq](https://github.com/tobiassvn/sidetiq) [![GitHub stars](https://img.shields.io/github/stars/tobiassvn/sidetiq?style=flat)](https://github.com/tobiassvn/sidetiq/stargazers) - Recurring jobs for sidekiq.
  * [sidekiq-cron](https://github.com/ondrejbartas/sidekiq-cron) [![GitHub stars](https://img.shields.io/github/stars/ondrejbartas/sidekiq-cron?style=flat)](https://github.com/ondrejbartas/sidekiq-cron/stargazers) - Scheduler / Cron for Sidekiq jobs
  * [sidekiq-scheduler](https://github.com/Moove-it/sidekiq-scheduler) [![GitHub stars](https://img.shields.io/github/stars/Moove-it/sidekiq-scheduler?style=flat)](https://github.com/Moove-it/sidekiq-scheduler/stargazers) - Lightweight job scheduler extension for Sidekiq
* [Sucker Punch](https://github.com/brandonhilkert/sucker_punch) [![GitHub stars](https://img.shields.io/github/stars/brandonhilkert/sucker_punch?style=flat)](https://github.com/brandonhilkert/sucker_punch/stargazers) - Sucker punch is a single-process Ruby asynchronous processing library.

## View Helper
* [formtastic](https://github.com/justinfrench/formtastic) [![GitHub stars](https://img.shields.io/github/stars/justinfrench/formtastic?style=flat)](https://github.com/justinfrench/formtastic/stargazers) - Formtastic is a Rails FormBuilder DSL (with some other goodies) to make it far easier to create beautiful, semantically rich, syntactically awesome, readily stylable and wonderfully accessible HTML forms in your Rails applications
* [Simple Form](https://github.com/plataformatec/simple_form) [![GitHub stars](https://img.shields.io/github/stars/plataformatec/simple_form?style=flat)](https://github.com/plataformatec/simple_form/stargazers) - Simple form aims to be as flexible as possible while helping you with powerful components to create your forms. The basic goal of Simple Form is to not touch your way of defining the layout, letting you find the better design for your eyes.
* [Nested Form](https://github.com/ryanb/nested_form) [![GitHub stars](https://img.shields.io/github/stars/ryanb/nested_form?style=flat)](https://github.com/ryanb/nested_form/stargazers) - This is a Rails gem for conveniently manage multiple nested models in a single form. It does so in an unobtrusive way through jQuery or Prototype. It can also be integrated with Simple Form.
* [meta-tags](https://github.com/kpumuk/meta-tags) [![GitHub stars](https://img.shields.io/github/stars/kpumuk/meta-tags?style=flat)](https://github.com/kpumuk/meta-tags/stargazers) - Search Engine Optimization (SEO) plugin for Ruby on Rails applications.
* [active_link_to](https://github.com/comfy/active_link_to) [![GitHub stars](https://img.shields.io/github/stars/comfy/active_link_to?style=flat)](https://github.com/comfy/active_link_to/stargazers) - active_link_to adds css 'active' class to your links.
* [cells](https://github.com/apotonick/cells) [![GitHub stars](https://img.shields.io/github/stars/apotonick/cells?style=flat)](https://github.com/apotonick/cells/stargazers) - Cells allow you to encapsulate parts of your UI into components into view models. View models, or cells, are simple ruby classes that can render templates.
* [i18n Country Code Select](https://github.com/onomojo/i18n_country_select) [![GitHub stars](https://img.shields.io/github/stars/onomojo/i18n_country_select?style=flat)](https://github.com/onomojo/i18n_country_select/stargazers) - I18n Country Code Select Form Helper for Rails 3 & 4.
* [Subdivision Select](https://github.com/cllns/subdivision_select) [![GitHub stars](https://img.shields.io/github/stars/cllns/subdivision_select?style=flat)](https://github.com/cllns/subdivision_select/stargazers) - A Rails plugin to populate a state/province select box from country_select.
* [cocoon](https://github.com/nathanvda/cocoon) [![GitHub stars](https://img.shields.io/github/stars/nathanvda/cocoon?style=flat)](https://github.com/nathanvda/cocoon/stargazers) - Dynamic nested forms using jQuery made easy

## Environment Variables
* [Config](https://github.com/railsconfig/config) [![GitHub stars](https://img.shields.io/github/stars/railsconfig/config?style=flat)](https://github.com/railsconfig/config/stargazers) - Multi-environment YAML style configurations that helps easily manage environment specific settings in an easy and usable manner.
* [Figaro](https://github.com/laserlemon/figaro) [![GitHub stars](https://img.shields.io/github/stars/laserlemon/figaro?style=flat)](https://github.com/laserlemon/figaro/stargazers) - Figaro is very simple, Heroku-friendly Rails app configuration using ENV and a single YAML file.
* [dotenv](https://github.com/bkeepers/dotenv) [![GitHub stars](https://img.shields.io/github/stars/bkeepers/dotenv?style=flat)](https://github.com/bkeepers/dotenv/stargazers) - Dotenv is a gem that allows you to set your environment variables in .env file, and it will load it in to ENV.
* [opsworks-dotenv](https://github.com/mikamai/opsworks-dotenv) [![GitHub stars](https://img.shields.io/github/stars/mikamai/opsworks-dotenv?style=flat)](https://github.com/mikamai/opsworks-dotenv/stargazers) - Opsworks-dotenv let you configure the environment for you Rails application using OpsWorks, Chef and Dotenv.

## Admin Panel
* [ActiveAdmin](http://activeadmin.info) - ActiveAdmin is a administration framework for Ruby on Rails applications.
  - [active_skin](https://github.com/rstgroup/active_skin) [![GitHub stars](https://img.shields.io/github/stars/rstgroup/active_skin?style=flat)](https://github.com/rstgroup/active_skin/stargazers): Flat skin for active admin.
* [RailsAdmin](https://github.com/sferik/rails_admin) [![GitHub stars](https://img.shields.io/github/stars/sferik/rails_admin?style=flat)](https://github.com/sferik/rails_admin/stargazers) - RailsAdmin is a Rails engine that provides an easy-to-use interface for managing your data.
* [Typus](https://github.com/typus/typus) [![GitHub stars](https://img.shields.io/github/stars/typus/typus?style=flat)](https://github.com/typus/typus/stargazers) - Typus is a control panel for Ruby on Rails applications to allow trusted users edit structured content.
* [administrate](https://github.com/thoughtbot/administrate) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/administrate?style=flat)](https://github.com/thoughtbot/administrate/stargazers) - A Rails engine that helps you put together a super-flexible admin dashboard.
* [Trestle](https://github.com/TrestleAdmin/trestle) [![GitHub stars](https://img.shields.io/github/stars/TrestleAdmin/trestle?style=flat)](https://github.com/TrestleAdmin/trestle/stargazers) - A modern, responsive admin framework for Ruby on Rails

## Logging
* [Impressionist](https://github.com/charlotte-ruby/impressionist) [![GitHub stars](https://img.shields.io/github/stars/charlotte-ruby/impressionist?style=flat)](https://github.com/charlotte-ruby/impressionist/stargazers) - Impressionist can log page impressions (technically action impressions), but it is not limited to that. You can log impressions multiple times per request. And you can also attach it to a model. The goal of this project is to provide customizable stats that are immediately accessible in your application as opposed to using Google Analytics and pulling data using their API.
* [Ahoy](https://github.com/ankane/ahoy) [![GitHub stars](https://img.shields.io/github/stars/ankane/ahoy?style=flat)](https://github.com/ankane/ahoy/stargazers) - Ahoy provides a solid foundation to track visits and events in Ruby, JavaScript, and native apps.
* [Lograge](https://github.com/roidrage/lograge) [![GitHub stars](https://img.shields.io/github/stars/roidrage/lograge?style=flat)](https://github.com/roidrage/lograge/stargazers) - An attempt to tame Rails' default policy to log everything.

## Debug
* [byebug](https://github.com/deivid-rodriguez/byebug) [![GitHub stars](https://img.shields.io/github/stars/deivid-rodriguez/byebug?style=flat)](https://github.com/deivid-rodriguez/byebug/stargazers) - Byebug is a simple to use, feature rich debugger for Ruby 2. It uses the new TracePoint API for execution control and the new Debug Inspector API for call stack navigation, so it doesn't depend on internal core sources.
  * [pry-byebug](https://github.com/deivid-rodriguez/pry-byebug) [![GitHub stars](https://img.shields.io/github/stars/deivid-rodriguez/pry-byebug?style=flat)](https://github.com/deivid-rodriguez/pry-byebug/stargazers) - Pry navigation commands via byebug.
* [pry-rails](https://github.com/rweng/pry-rails) [![GitHub stars](https://img.shields.io/github/stars/rweng/pry-rails?style=flat)](https://github.com/rweng/pry-rails/stargazers) - Avoid repeating yourself, use pry-rails instead of copying the initializer to every rails project. This is a small gem which causes rails console to open pry. It therefore depends on pry.
* [awesome_print](https://github.com/awesome-print/awesome_print) [![GitHub stars](https://img.shields.io/github/stars/awesome-print/awesome_print?style=flat)](https://github.com/awesome-print/awesome_print/stargazers) - Awesome Print is a Ruby library that pretty prints Ruby objects in full color exposing their internal structure with proper indentation.
* [web-console](https://github.com/rails/web-console) [![GitHub stars](https://img.shields.io/github/stars/rails/web-console?style=flat)](https://github.com/rails/web-console/stargazers) - Web Console is a debugging tool for your Ruby on Rails applications.
* [spring](https://github.com/rails/spring) [![GitHub stars](https://img.shields.io/github/stars/rails/spring?style=flat)](https://github.com/rails/spring/stargazers) - Spring is a Rails application preloader. It speeds up development by keeping your application running in the background so you don't need to boot it every time you run a test, rake task or migration.
* [rails-footnotes](https://github.com/josevalim/rails-footnotes) [![GitHub stars](https://img.shields.io/github/stars/josevalim/rails-footnotes?style=flat)](https://github.com/josevalim/rails-footnotes/stargazers) - Rails footnotes displays footnotes in your application for easy debugging, such as sessions, request parameters, cookies, filter chain, routes, queries, etc.
* [g](https://github.com/jugyo/g) [![GitHub stars](https://img.shields.io/github/stars/jugyo/g?style=flat)](https://github.com/jugyo/g/stargazers) - The Kernel.g that works like Kernel.p by using terminal-notifier or growl.
* [terminal-notifier](https://github.com/julienXX/terminal-notifier) [![GitHub stars](https://img.shields.io/github/stars/julienXX/terminal-notifier?style=flat)](https://github.com/julienXX/terminal-notifier/stargazers) - terminal-notifier is a command-line tool to send Mac OS X User Notifications, which are available in Mac OS X 10.8 and higher.
* [letter_opener](https://github.com/ryanb/letter_opener) [![GitHub stars](https://img.shields.io/github/stars/ryanb/letter_opener?style=flat)](https://github.com/ryanb/letter_opener/stargazers) - Preview email in the default browser instead of sending it. This means you do not need to set up email delivery in your development environment, and you no longer need to worry about accidentally sending a test email to someone else's address.
* [Better Errors](https://github.com/charliesome/better_errors) [![GitHub stars](https://img.shields.io/github/stars/charliesome/better_errors?style=flat)](https://github.com/charliesome/better_errors/stargazers) - Better errors replaces the standard Rails error page with a much better and more useful error page.
  * If you would like to use Better Errors' advanced features (REPL, local/instance variable inspection, pretty stack frame names), you need to add the [binding_ _of__caller](https://github.com/banister/binding_of_caller) [![GitHub stars](https://img.shields.io/github/stars/banister/binding_of_caller?style=flat)](https://github.com/banister/binding_of_caller/stargazers).
* [RailsPanel](https://github.com/dejan/rails_panel) [![GitHub stars](https://img.shields.io/github/stars/dejan/rails_panel?style=flat)](https://github.com/dejan/rails_panel/stargazers) - RailsPanel is a Chrome extension for Rails development that will end your tailing of development.log.

## Coding Style
* [RuboCop](https://github.com/bbatsov/rubocop) [![GitHub stars](https://img.shields.io/github/stars/bbatsov/rubocop?style=flat)](https://github.com/bbatsov/rubocop/stargazers) - Rubocop is a Ruby static code analyzer. Out of the box it will enforce many of the guidelines outlined in the community [Ruby Style Guide](https://github.com/bbatsov/ruby-style-guide) [![GitHub stars](https://img.shields.io/github/stars/bbatsov/ruby-style-guide?style=flat)](https://github.com/bbatsov/ruby-style-guide/stargazers).
* [Rails Best Practice](https://github.com/railsbp/rails_best_practices) [![GitHub stars](https://img.shields.io/github/stars/railsbp/rails_best_practices?style=flat)](https://github.com/railsbp/rails_best_practices/stargazers) - Rails best practice is a code metric tool to check the quality of rails codes.
* [Metric Fu]( https://github.com/metricfu/metric_fu) - A fist full of code metrics
* [Pronto](https://github.com/mmozuras/pronto) [![GitHub stars](https://img.shields.io/github/stars/mmozuras/pronto?style=flat)](https://github.com/mmozuras/pronto/stargazers) - Quick automated code review of your changes

## Testing
* [rspec-rails](https://github.com/rspec/rspec-rails) [![GitHub stars](https://img.shields.io/github/stars/rspec/rspec-rails?style=flat)](https://github.com/rspec/rspec-rails/stargazers) - Rspec-rails is a testing framework for Rails 3.x and 4.x.
* [Capybara](https://github.com/jnicklas/capybara) [![GitHub stars](https://img.shields.io/github/stars/jnicklas/capybara?style=flat)](https://github.com/jnicklas/capybara/stargazers) - Capybara helps you test web applications by simulating how a real user would interact with your app. And drivers:
  - [capybara-webkit](https://github.com/thoughtbot/capybara-webkit) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/capybara-webkit?style=flat)](https://github.com/thoughtbot/capybara-webkit/stargazers) - Capybara-webkit is a capybara driver that uses Webkit via QtWebkit.
  - [selenium-webdriver](https://github.com/vertis/selenium-webdriver) [![GitHub stars](https://img.shields.io/github/stars/vertis/selenium-webdriver?style=flat)](https://github.com/vertis/selenium-webdriver/stargazers) - Selenium-webdriver provides ruby bindings for WebDriver.
  - [poltergeist](https://github.com/teampoltergeist/poltergeist) [![GitHub stars](https://img.shields.io/github/stars/teampoltergeist/poltergeist?style=flat)](https://github.com/teampoltergeist/poltergeist/stargazers) - Poltergeist allows you to run your Capybara tests on a headless WebKit browser, provided by PhantomJS.
  - [page-object](https://github.com/cheezy/page-object) [![GitHub stars](https://img.shields.io/github/stars/cheezy/page-object?style=flat)](https://github.com/cheezy/page-object/stargazers) - Page-object is a simple gem that assists in creating flexible page objects for testing browser based applications.
* [factory_bot](https://github.com/thoughtbot/factory_bot) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/factory_bot?style=flat)](https://github.com/thoughtbot/factory_bot/stargazers) - Factory_bot is a fixtures replacement with a straightforward definition syntax, support for multiple build strategies (saved instances, unsaved instances, attribute hashes, and stubbed objects), and support for multiple factories for the same class (user, admin_user, and so on), including factory inheritance.
* [factory_bot_rails](https://github.com/thoughtbot/factory_bot_rails) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/factory_bot_rails?style=flat)](https://github.com/thoughtbot/factory_bot_rails/stargazers) - Factory_bot_rails provides Rails integration for factory_bot.
* [factory_factory_girl](https://github.com/st0012/factory_factory_girl) [![GitHub stars](https://img.shields.io/github/stars/st0012/factory_factory_girl?style=flat)](https://github.com/st0012/factory_factory_girl/stargazers) - FactoryFactoryGirl lets you generate factory files more efficiently with naming rules.
* [Database Cleaner](https://github.com/DatabaseCleaner/database_cleaner) [![GitHub stars](https://img.shields.io/github/stars/DatabaseCleaner/database_cleaner?style=flat)](https://github.com/DatabaseCleaner/database_cleaner/stargazers) - Database Cleaner is a set of strategies for cleaning your database in Ruby.Support ActiveRecord, DataMapper, Sequel, MongoMapper, Mongoid, CouchPotato, Ohm and Redis.
* [shoulda-matchers](https://github.com/thoughtbot/shoulda-matchers) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/shoulda-matchers?style=flat)](https://github.com/thoughtbot/shoulda-matchers/stargazers) - Shoulda-matchers provides serveral matchers for testing common Rails functionality.
* [ResponseCodeMatchers](https://github.com/r7kamura/response_code_matchers) [![GitHub stars](https://img.shields.io/github/stars/r7kamura/response_code_matchers?style=flat)](https://github.com/r7kamura/response_code_matchers/stargazers) - ResponseCodeMatchers provides rspec matchers to match http response code.
* [SimpleCov](https://github.com/colszowka/simplecov) [![GitHub stars](https://img.shields.io/github/stars/colszowka/simplecov?style=flat)](https://github.com/colszowka/simplecov/stargazers) - SimpleCov is a code coverage analysis tool for Ruby.
* [Timecop](https://github.com/travisjeffery/timecop) [![GitHub stars](https://img.shields.io/github/stars/travisjeffery/timecop?style=flat)](https://github.com/travisjeffery/timecop/stargazers) - A gem providing "time travel" and "time freezing" capabilities, making it dead simple to test time-dependent code.
* [VCR](https://github.com/vcr/vcr) [![GitHub stars](https://img.shields.io/github/stars/vcr/vcr?style=flat)](https://github.com/vcr/vcr/stargazers) - Record your test suite's HTTP interactions and replay them during future test runs for fast, deterministic, accurate tests.

### Security
* [brakeman](https://github.com/presidentbeef/brakeman) [![GitHub stars](https://img.shields.io/github/stars/presidentbeef/brakeman?style=flat)](https://github.com/presidentbeef/brakeman/stargazers) - Brakeman is a static analysis tool which checks Ruby on Rails applications for security vulnerabilities.
* [bundle-audit](https://github.com/rubysec/bundler-audit) [![GitHub stars](https://img.shields.io/github/stars/rubysec/bundler-audit?style=flat)](https://github.com/rubysec/bundler-audit/stargazers) - bundler-audit is a patch-level verification tool for Bundler which checks for vulnerable versions of gems and insecure gem sources.
* [Secure Headers](https://github.com/twitter/secureheaders) [![GitHub stars](https://img.shields.io/github/stars/twitter/secureheaders?style=flat)](https://github.com/twitter/secureheaders/stargazers) -  Secure Headers will automatically apply several headers that are related to security.

## Production
* [Capistrano](https://github.com/capistrano/capistrano) [![GitHub stars](https://img.shields.io/github/stars/capistrano/capistrano?style=flat)](https://github.com/capistrano/capistrano/stargazers) - Remote multi-server automation tool.
* [Slowpoke](https://github.com/ankane/slowpoke) [![GitHub stars](https://img.shields.io/github/stars/ankane/slowpoke?style=flat)](https://github.com/ankane/slowpoke/stargazers) - Rack::Timeout is great. Slowpoke makes it better.
* [Rack Attack](https://github.com/kickstarter/rack-attack) [![GitHub stars](https://img.shields.io/github/stars/kickstarter/rack-attack?style=flat)](https://github.com/kickstarter/rack-attack/stargazers) - Rack middleware to blocking & throttling.
* [Responders](https://github.com/plataformatec/responders) [![GitHub stars](https://img.shields.io/github/stars/plataformatec/responders?style=flat)](https://github.com/plataformatec/responders/stargazers) - A set of Rails responders to dry up your application.
* [production_rails](https://github.com/ankane/production_rails) [![GitHub stars](https://img.shields.io/github/stars/ankane/production_rails?style=flat)](https://github.com/ankane/production_rails/stargazers) - Best practices for running Rails in production.
* [Mina](https://github.com/mina-deploy/mina) [![GitHub stars](https://img.shields.io/github/stars/mina-deploy/mina?style=flat)](https://github.com/mina-deploy/mina/stargazers) - fast deployer and server automation tool.

## Error Logging
* [Rollbar](https://github.com/rollbar/rollbar-gem) [![GitHub stars](https://img.shields.io/github/stars/rollbar/rollbar-gem?style=flat)](https://github.com/rollbar/rollbar-gem/stargazers) - Exception tracking and logging from Ruby to Rollbar.
* [Airbrake](https://github.com/airbrake/airbrake) [![GitHub stars](https://img.shields.io/github/stars/airbrake/airbrake?style=flat)](https://github.com/airbrake/airbrake/stargazers) - Notifier gem for integrating apps with Airbrake
* [Errbit](https://github.com/errbit/errbit) [![GitHub stars](https://img.shields.io/github/stars/errbit/errbit?style=flat)](https://github.com/errbit/errbit/stargazers) - Open source notifier gem compliant with Airbrake.

## Database
* [rails_db](https://github.com/igorkasyanchuk/rails_db) [![GitHub stars](https://img.shields.io/github/stars/igorkasyanchuk/rails_db?style=flat)](https://github.com/igorkasyanchuk/rails_db/stargazers) - Rails Database Viewer and SQL Query Runner

## Asset Pipeline
* [Alaska](https://github.com/mavenlink/alaska) [![GitHub stars](https://img.shields.io/github/stars/mavenlink/alaska?style=flat)](https://github.com/mavenlink/alaska/stargazers) - ExecJS runtime with persistent connection to nodejs, speeds up your coffeescript compilation process during development and deployment.

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
