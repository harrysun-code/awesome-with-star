# Meteor

[![GitHub stars](https://img.shields.io/github/stars/Urigo/awesome-meteor?style=flat)](https://github.com/Urigo/awesome-meteor/stargazers)

# Awesome Meteor [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome Meteor Packages, libraries and software.

The official Meteor resources page can be found [here](https://www.meteor.com/tools/resources)

- [Awesome Meteor](#awesome-meteor)
  - [Getting Started](#getting-started)
  - [Collections](#collections)
  - [Forms and Templates](#forms-and-templates)
  - [Users and Authentication](#users-and-authentication)
  - [REST](#rest)
  - [Files](#files)
  - [Routers](#routers)
  - [Debugging Tools](#debugging-tools)
  - [Editor Plugins](#editor-plugins)
  - [Search, sort and paginate](#search-sort-paginate)
  - [Mobile](#mobile)
  - [Offline](#offline)
  - [Testing](#testing)
  - [SEO](#seo)
  - [Data Visualization](#data-visualization)
  - [Analytics](#analytics)
  - [Cron Jobs](#cron-jobs)
  - [Administration](#administration)
  - [Performance](#performance)
  - [Monitoring](#monitoring)
  - [Deployment](#deployment)
    - [Docker Images](#docker-images)
  - [Front End Frameworks](#front-end-frameworks)
  - [Alternative Databases](#alternative-databases)
  - [Boilerplate](#boilerplate)
  - [Open Source Apps](#open-source-apps)
  - [Internationalization](#internationalization)
  - [Scaffolding](#scaffolding)
  - [Tooling](#tooling)
- [Resources](#resources)
  - [Books](#books)
  - [Courses](#courses)
    - [Free](#free)
    - [Paid](#paid)
  - [Tutorials](#tutorials)
  - [Blogs](#blogs)
  - [Websites](#websites)
  - [Q&A](#q&a)
  - [Community Newsletters](#community-newsletters)	
  - [Social](#social)
  - [Work Opportunities](#work-opportunities)
  - [Related](#related)
- [Built With Meteor](#built-with-meteor)
- [Deprecated](#deprecated)
- [Contributing](#contributing)

---

## Getting Started

_Where to start_

- [Official Meteor tutorial](https://www.meteor.com/tutorials/react/creating-an-app)
- [Official Guide](http://guide.meteor.com/)

## Collections

_Helpers and expensions for collections_

- [simple-schema](https://github.com/aldeed/simple-schema-js) [![GitHub stars](https://img.shields.io/github/stars/aldeed/simple-schema-js?style=flat)](https://github.com/aldeed/simple-schema-js/stargazers) - A JavaScript schema validation package that supports direct validation of MongoDB update modifier objects.
- [aldeed:collection2](https://github.com/aldeed/meteor-collection2/) [![GitHub stars](https://img.shields.io/github/stars/aldeed/meteor-collection2/?style=flat)](https://github.com/aldeed/meteor-collection2//stargazers) - Automatic validation of insert and update operations on the client and server.
- [dburles:collection-helpers](https://github.com/dburles/meteor-collection-helpers/) [![GitHub stars](https://img.shields.io/github/stars/dburles/meteor-collection-helpers/?style=flat)](https://github.com/dburles/meteor-collection-helpers//stargazers) – Transform your collections with helpers that you define.
- [matb33:collection-hooks](https://github.com/Meteor-Community-Packages/meteor-collection-hooks) [![GitHub stars](https://img.shields.io/github/stars/Meteor-Community-Packages/meteor-collection-hooks?style=flat)](https://github.com/Meteor-Community-Packages/meteor-collection-hooks/stargazers) - Extends Mongo.Collection with before/after hooks for insert/update/remove/find/findOne.
- [reywood:publish-composite](https://github.com/Meteor-Community-Packages/meteor-publish-composite) [![GitHub stars](https://img.shields.io/github/stars/Meteor-Community-Packages/meteor-publish-composite?style=flat)](https://github.com/Meteor-Community-Packages/meteor-publish-composite/stargazers) - publish a set of related documents from various collections using a reactive join.
- [jagi:astronomy](https://github.com/jagi/meteor-astronomy/) [![GitHub stars](https://img.shields.io/github/stars/jagi/meteor-astronomy/?style=flat)](https://github.com/jagi/meteor-astronomy//stargazers) - The Model layer for Meteor.
- [cultofcoders:grapher](https://github.com/cult-of-coders/grapher) [![GitHub stars](https://img.shields.io/github/stars/cult-of-coders/grapher?style=flat)](https://github.com/cult-of-coders/grapher/stargazers) - Grapher: Meteor Collection Joins + Reactive GraphQL like queries.
- [sakulstra:aggregate](https://github.com/sakulstra/meteor-aggregate) [![GitHub stars](https://img.shields.io/github/stars/sakulstra/meteor-aggregate?style=flat)](https://github.com/sakulstra/meteor-aggregate/stargazers) - Add proper aggregation support for Meteor.
- [quave:collections](https://github.com/quavedev/collections) [![GitHub stars](https://img.shields.io/github/stars/quavedev/collections?style=flat)](https://github.com/quavedev/collections/stargazers) - Create collections in a standard way.

## REST

_REST support for Meteor_

- [maka:rest](https://atmospherejs.com/maka/rest) - automatically make your Meteor app accessible over HTTP and DDP alike.
- [vatfree:restivus](https://github.com/vatfree/meteor-restivus) [![GitHub stars](https://img.shields.io/github/stars/vatfree/meteor-restivus?style=flat)](https://github.com/vatfree/meteor-restivus/stargazers) - Make REST endpoints for your Meteor app with incredible ease.

## Forms and Templates

_Helpers for templates_

- [uniforms](https://github.com/vazco/uniforms) [![GitHub stars](https://img.shields.io/github/stars/vazco/uniforms?style=flat)](https://github.com/vazco/uniforms/stargazers) - Bunch of React components and helpers to easily generate and validate forms. [Seamlessly integrate with `simpl-schema`](https://uniforms.tools/docs/installation).
- [aldeed:autoform](https://github.com/aldeed/meteor-autoform) [![GitHub stars](https://img.shields.io/github/stars/aldeed/meteor-autoform?style=flat)](https://github.com/aldeed/meteor-autoform/stargazers) - UI components and helpers to easily create basic forms with automatic insert and update events, and automatic reactive validation.
- [ostrio:templatehelpers](https://github.com/VeliovGroup/Meteor-Template-helpers) [![GitHub stars](https://img.shields.io/github/stars/VeliovGroup/Meteor-Template-helpers?style=flat)](https://github.com/VeliovGroup/Meteor-Template-helpers/stargazers) - Utility helpers for your Blaze templates.
- [aldeed:template-extension](https://github.com/aldeed/meteor-template-extension) [![GitHub stars](https://img.shields.io/github/stars/aldeed/meteor-template-extension?style=flat)](https://github.com/aldeed/meteor-template-extension/stargazers) - A Meteor package: Replace already defined templates, inherit helpers and events from other templates.
- [kadira:blaze-layout](https://github.com/TeamGrid/blaze-layout) [![GitHub stars](https://img.shields.io/github/stars/TeamGrid/blaze-layout?style=flat)](https://github.com/TeamGrid/blaze-layout/stargazers) - Layout Manager for Blaze (works well with Meteor FlowRouter)

## Users and Authentication

_Tools for handling users and authentication_

- [accounts-js](https://github.com/accounts-js/accounts) [![GitHub stars](https://img.shields.io/github/stars/accounts-js/accounts?style=flat)](https://github.com/accounts-js/accounts/stargazers) - A suite of packages aims to provide all the tools you need to build a flexible authentication and accounts management solution for your application.
- [alanning:roles](https://github.com/Meteor-Community-Packages/meteor-roles) [![GitHub stars](https://img.shields.io/github/stars/Meteor-Community-Packages/meteor-roles?style=flat)](https://github.com/Meteor-Community-Packages/meteor-roles/stargazers) - Roles support for the built-in accounts packages.
- [meteor-user-status](https://github.com/Meteor-Community-Packages/meteor-user-status) [![GitHub stars](https://img.shields.io/github/stars/Meteor-Community-Packages/meteor-user-status?style=flat)](https://github.com/Meteor-Community-Packages/meteor-user-status/stargazers) - Keeps track of users and their meta data.
- [accounts-ui](https://github.com/e-Potek/accounts-ui/) [![GitHub stars](https://img.shields.io/github/stars/e-Potek/accounts-ui/?style=flat)](https://github.com/e-Potek/accounts-ui//stargazers) - Accounts UI for React in Meteor 1.3+.

## Administration

_Tools for administrating your Meteor apps_

- [Meteor Candy](https://www.meteorcandy.com/) - Fastest and easier way to add an admin panel to your app.
- [yogiben:admin](https://github.com/yogiben/meteor-admin) [![GitHub stars](https://img.shields.io/github/stars/yogiben/meteor-admin?style=flat)](https://github.com/yogiben/meteor-admin/stargazers) - A complete admin dashboard solution.
- [houston:admin](https://github.com/gterrono/houston) [![GitHub stars](https://img.shields.io/github/stars/gterrono/houston?style=flat)](https://github.com/gterrono/houston/stargazers) - A zero-config, Django Admin-like admin for Meteor.
- [zodern:pure-admin](https://github.com/zodern/meteor-pure-admin) [![GitHub stars](https://img.shields.io/github/stars/zodern/meteor-pure-admin?style=flat)](https://github.com/zodern/meteor-pure-admin/stargazers) - An isolated, customizable admin panel for Meteor.

## Monitoring

_Tools for monitoring your Meteor apps_

- [kschingiz:meteor-elastic-apm](https://github.com/kschingiz/meteor-elastic-apm) [![GitHub stars](https://img.shields.io/github/stars/kschingiz/meteor-elastic-apm?style=flat)](https://github.com/kschingiz/meteor-elastic-apm/stargazers) - Perfomance Monitoring for Meteor based on Elastic APM
- [monti-apm-agent](https://github.com/monti-apm/monti-apm-agent) [![GitHub stars](https://img.shields.io/github/stars/monti-apm/monti-apm-agent?style=flat)](https://github.com/monti-apm/monti-apm-agent/stargazers) - Performance Monitoring for Meteor
- [lmachens:kadira](https://github.com/lmachens/kadira) [![GitHub stars](https://img.shields.io/github/stars/lmachens/kadira?style=flat)](https://github.com/lmachens/kadira/stargazers) - Performance Monitoring for Meteor

## Performance

_Tools for speeding up your Meteor apps_

- [cultofcoders:redis-oplog](https://github.com/cult-of-coders/redis-oplog) [![GitHub stars](https://img.shields.io/github/stars/cult-of-coders/redis-oplog?style=flat)](https://github.com/cult-of-coders/redis-oplog/stargazers) - Redis Oplog implementation to fully replace MongoDB Oplog in Meteor
- [staringatlights:fast-render](https://github.com/abecks/meteor-fast-render) [![GitHub stars](https://img.shields.io/github/stars/abecks/meteor-fast-render?style=flat)](https://github.com/abecks/meteor-fast-render/stargazers) - An active fork of fast-render
- [epotek:method-cache](https://github.com/e-Potek/method-cache) [![GitHub stars](https://img.shields.io/github/stars/e-Potek/method-cache?style=flat)](https://github.com/e-Potek/method-cache/stargazers) - Meteor method caching using DataLoader
- [maestroqadev:pub-sub-lite](https://github.com/adtribute/pub-sub-lite) [![GitHub stars](https://img.shields.io/github/stars/adtribute/pub-sub-lite?style=flat)](https://github.com/adtribute/pub-sub-lite/stargazers) - Transform publications to be non-reactive.
- [artillery-engine-meteor](https://github.com/kschingiz/artillery-engine-meteor) [![GitHub stars](https://img.shields.io/github/stars/kschingiz/artillery-engine-meteor?style=flat)](https://github.com/kschingiz/artillery-engine-meteor/stargazers) - Artillery load testing for MeteorJS applications.

## Deployment

_Tools for deploying and maintaining Meteor apps_

- [meteor-up](https://github.com/zodern/meteor-up) [![GitHub stars](https://img.shields.io/github/stars/zodern/meteor-up?style=flat)](https://github.com/zodern/meteor-up/stargazers) – Meteor Deployments.
- [meteor-google-cloud](https://github.com/EducationLink/meteor-google-cloud) [![GitHub stars](https://img.shields.io/github/stars/EducationLink/meteor-google-cloud?style=flat)](https://github.com/EducationLink/meteor-google-cloud/stargazers) - Automate Meteor deployments on Google Cloud App Engine Flexible
- [mup-aws-beanstalk](https://github.com/zodern/mup-aws-beanstalk) [![GitHub stars](https://img.shields.io/github/stars/zodern/mup-aws-beanstalk?style=flat)](https://github.com/zodern/mup-aws-beanstalk/stargazers) - Deploy Meteor apps to AWS Elastic Beanstalk using Meteor Up
- [meteor-azure](https://github.com/fractal-code/meteor-azure) [![GitHub stars](https://img.shields.io/github/stars/fractal-code/meteor-azure?style=flat)](https://github.com/fractal-code/meteor-azure/stargazers) - Automate Meteor deployments on Azure App Service
- [pm2-meteor](https://github.com/andruschka/pm2-meteor) [![GitHub stars](https://img.shields.io/github/stars/andruschka/pm2-meteor?style=flat)](https://github.com/andruschka/pm2-meteor/stargazers) - Simplest way to deploy, scale and run Meteor Apps with PM2.
- [meteor-hero](https://github.com/jkrup/meteor-hero) [![GitHub stars](https://img.shields.io/github/stars/jkrup/meteor-hero?style=flat)](https://github.com/jkrup/meteor-hero/stargazers) - Deploy MeteorJS applications for free with one command utilizing Heroku's service.
- [meteor-kubernetes-guide](https://github.com/Gregivy/meteor-kubernetes-guide) [![GitHub stars](https://img.shields.io/github/stars/Gregivy/meteor-kubernetes-guide?style=flat)](https://github.com/Gregivy/meteor-kubernetes-guide/stargazers) - Deploy a Meteor app with Kubernetes.
- [meteorhacks:cluster](https://github.com/lmachens/cluster) [![GitHub stars](https://img.shields.io/github/stars/lmachens/cluster?style=flat)](https://github.com/lmachens/cluster/stargazers) - Clustering solution for Meteor with load balancing and service discovery
- [demeteorizer](https://github.com/onmodulus/demeteorizer) [![GitHub stars](https://img.shields.io/github/stars/onmodulus/demeteorizer?style=flat)](https://github.com/onmodulus/demeteorizer/stargazers) - Converts a Meteor app into a "standard" Node.js application
- [percolate:migrations](https://github.com/percolatestudio/meteor-migrations) [![GitHub stars](https://img.shields.io/github/stars/percolatestudio/meteor-migrations?style=flat)](https://github.com/percolatestudio/meteor-migrations/stargazers) - Simple migration system for Meteor
- [yamup](https://github.com/bordalix/yamup) [![GitHub stars](https://img.shields.io/github/stars/bordalix/yamup?style=flat)](https://github.com/bordalix/yamup/stargazers) - Deploy Meteor apps to your own Ubuntu server (EC2, ...) without dockers
- [waveshosting](https://github.com/nicolaslopezj/waveshosting) [![GitHub stars](https://img.shields.io/github/stars/nicolaslopezj/waveshosting?style=flat)](https://github.com/nicolaslopezj/waveshosting/stargazers) - Web application to manage meteor deployments.

## Docker Images

- [meteor-docker](https://github.com/zodern/meteor-docker) [![GitHub stars](https://img.shields.io/github/stars/zodern/meteor-docker?style=flat)](https://github.com/zodern/meteor-docker/stargazers)
- [meteor-base](https://github.com/disney/meteor-base) [![GitHub stars](https://img.shields.io/github/stars/disney/meteor-base?style=flat)](https://github.com/disney/meteor-base/stargazers)
- [docker-meteor](https://github.com/tozd/docker-meteor) [![GitHub stars](https://img.shields.io/github/stars/tozd/docker-meteor?style=flat)](https://github.com/tozd/docker-meteor/stargazers)

## Routers

_Routers for Blaze_

- [ostrio:flow-router-extra](https://github.com/VeliovGroup/flow-router) [![GitHub stars](https://img.shields.io/github/stars/VeliovGroup/flow-router?style=flat)](https://github.com/VeliovGroup/flow-router/stargazers) - Carefully extended `flow-router` package. Up-to-date version with support of latest Meteor's releases.
- [msavin:parrot](https://github.com/msavin/Parrot) [![GitHub stars](https://img.shields.io/github/stars/msavin/Parrot?style=flat)](https://github.com/msavin/Parrot/stargazers) - Web router specially designed for building SPAs using Meteor
- [meteorhacks:picker](https://github.com/meteorhacks/picker) [![GitHub stars](https://img.shields.io/github/stars/meteorhacks/picker?style=flat)](https://github.com/meteorhacks/picker/stargazers) - Server Side Router for Meteor.
- [iron:router](https://github.com/iron-meteor/iron-router) [![GitHub stars](https://img.shields.io/github/stars/iron-meteor/iron-router?style=flat)](https://github.com/iron-meteor/iron-router/stargazers) - A router that works on the server and the browser, designed specifically for Meteor. 

## Offline

_Tools for Meteor offline support_

- [ground:db](https://github.com/GroundMeteor/db) [![GitHub stars](https://img.shields.io/github/stars/GroundMeteor/db?style=flat)](https://github.com/GroundMeteor/db/stargazers) - GroundDB is a thin layer providing Meteor offline database and methods.
- [npdev:collections](https://github.com/CaptainN/npdev-collections) [![GitHub stars](https://img.shields.io/github/stars/CaptainN/npdev-collections?style=flat)](https://github.com/CaptainN/npdev-collections/stargazers) - An easy way to create offline collections with SSR for Meteor
- [meteor-service-worker](https://github.com/NitroBAY/meteor-service-worker) [![GitHub stars](https://img.shields.io/github/stars/NitroBAY/meteor-service-worker?style=flat)](https://github.com/NitroBAY/meteor-service-worker/stargazers) - Meteor specific service worker implementaion.
- [quave:pwa](https://github.com/quavedev/pwa) [![GitHub stars](https://img.shields.io/github/stars/quavedev/pwa?style=flat)](https://github.com/quavedev/pwa/stargazers) - A Meteor package that allows you to configure your PWA.

## Testing

_Testing tools_

- [meteortesting:mocha](https://github.com/meteortesting/meteor-mocha) [![GitHub stars](https://img.shields.io/github/stars/meteortesting/meteor-mocha?style=flat)](https://github.com/meteortesting/meteor-mocha/stargazers) - Mocha test driver package for Meteor.
- [lmieulet:meteor-coverage](https://github.com/serut/meteor-coverage) [![GitHub stars](https://img.shields.io/github/stars/serut/meteor-coverage?style=flat)](https://github.com/serut/meteor-coverage/stargazers) - Test coverage for Meteor.
- [hubroedu:mocha](https://github.com/hubroedu/meteor-mocha/) [![GitHub stars](https://img.shields.io/github/stars/hubroedu/meteor-mocha/?style=flat)](https://github.com/hubroedu/meteor-mocha//stargazers) - Decaffed cultofcoders:mocha fork.
- [antwaremx:meteorman](https://github.com/antwaremx/meteorman) [![GitHub stars](https://img.shields.io/github/stars/antwaremx/meteorman?style=flat)](https://github.com/antwaremx/meteorman/stargazers) - Meteorman: A DDP Client with GUI to test Meteor methods and publications (like Postman).

## SEO

_Search Engine Optimization tools_

- [ostrio:spiderable-middleware](https://github.com/VeliovGroup/spiderable-middleware/) [![GitHub stars](https://img.shields.io/github/stars/VeliovGroup/spiderable-middleware/?style=flat)](https://github.com/VeliovGroup/spiderable-middleware//stargazers) - Prerendering (_a.k.a. Spiderable_) with support of ES6 (ECMAScript2015) - Meteor app crawled perfectly by search engines.

## Files

_Handling files in Meteor_

- [ostrio:files](https://github.com/VeliovGroup/Meteor-Files) [![GitHub stars](https://img.shields.io/github/stars/VeliovGroup/Meteor-Files?style=flat)](https://github.com/VeliovGroup/Meteor-Files/stargazers) - Upload files via DDP, HTTP and WebRTC/DC. To Meteor server FS, AWS, GridFS, DropBox or Google Drive. Fast, secure and robust.
- [@reactioncommerce/file-collections](https://github.com/reactioncommerce/reaction-file-collections) [![GitHub stars](https://img.shields.io/github/stars/reactioncommerce/reaction-file-collections?style=flat)](https://github.com/reactioncommerce/reaction-file-collections/stargazers) - Reaction FileCollections is a set of NPM packages that provide the ability to support file uploads, storage, and downloads in Node and Meteor apps, and in browser JavaScript.
- [netanelgilad:excel](https://github.com/netanelgilad/meteor-excel) [![GitHub stars](https://img.shields.io/github/stars/netanelgilad/meteor-excel?style=flat)](https://github.com/netanelgilad/meteor-excel/stargazers) - Parsing and generating excel files (xlsx, xls).
- [mikkelking:slingshot](https://github.com/Back2bikes/meteor-slingshot) [![GitHub stars](https://img.shields.io/github/stars/Back2bikes/meteor-slingshot?style=flat)](https://github.com/Back2bikes/meteor-slingshot/stargazers) - Upload files directly to AWS S3, Google Cloud Storage and others in meteor.

## Search, sort and paginate

_Search, sort and paginate related tools_

- [percolate:find-from-publication](https://github.com/versolearning/find-from-publication) [![GitHub stars](https://img.shields.io/github/stars/versolearning/find-from-publication?style=flat)](https://github.com/versolearning/find-from-publication/stargazers) - Enable finding all documents that have been published by a given publication.
- [meteor-publish-join](https://github.com/nlhuykhang/meteor-publish-join#readme) - A performant NPM package for publishing non-reactive or aggregated values.
- [tmeasday:publish-counts](https://github.com/percolatestudio/publish-counts) [![GitHub stars](https://img.shields.io/github/stars/percolatestudio/publish-counts?style=flat)](https://github.com/percolatestudio/publish-counts/stargazers) - Publish the count of a cursor, in real time.
- [meteorhacks:search-source](https://github.com/meteorhacks/search-source) [![GitHub stars](https://img.shields.io/github/stars/meteorhacks/search-source?style=flat)](https://github.com/meteorhacks/search-source/stargazers) - Reactive Data Source for Search.
- [matteodem:easy-search](https://github.com/matteodem/meteor-easy-search) [![GitHub stars](https://img.shields.io/github/stars/matteodem/meteor-easy-search?style=flat)](https://github.com/matteodem/meteor-easy-search/stargazers) - Easy-to-use search with Blaze Components (+ Elastic Search Support)
- [alethes:pages](https://github.com/alethes/meteor-pages) [![GitHub stars](https://img.shields.io/github/stars/alethes/meteor-pages?style=flat)](https://github.com/alethes/meteor-pages/stargazers) - Out of the box Meteor pagination.

## Mobile

_Mobile Development_

- [meteor-react-native](https://github.com/TheRealNate/meteor-react-native) [![GitHub stars](https://img.shields.io/github/stars/TheRealNate/meteor-react-native?style=flat)](https://github.com/TheRealNate/meteor-react-native/stargazers) - Meteor client for React Native matching Meteor Spec.
- [meteor-push](https://github.com/activitree/meteor-push) [![GitHub stars](https://img.shields.io/github/stars/activitree/meteor-push?style=flat)](https://github.com/activitree/meteor-push/stargazers) - Push notifications for cordova (ios, android) browser (Chrome, Safari, Firefox).
- [quave:universal-links](https://github.com/quavedev/universal-links) [![GitHub stars](https://img.shields.io/github/stars/quavedev/universal-links?style=flat)](https://github.com/quavedev/universal-links/stargazers) - A Meteor package that allows you to expose your native iOS settings to enable Universal Links. 
- [meteoric:ionic](https://github.com/meteoric/meteor-ionic) [![GitHub stars](https://img.shields.io/github/stars/meteoric/meteor-ionic?style=flat)](https://github.com/meteoric/meteor-ionic/stargazers) - Ionic components for Meteor.
- [driftyco:ionic](https://github.com/driftyco/ionic) [![GitHub stars](https://img.shields.io/github/stars/driftyco/ionic?style=flat)](https://github.com/driftyco/ionic/stargazers) - Official Ionic support for Meteor.
- [martijnwalraven:meteor-ios](https://github.com/martijnwalraven/meteor-ios) [![GitHub stars](https://img.shields.io/github/stars/martijnwalraven/meteor-ios?style=flat)](https://github.com/martijnwalraven/meteor-ios/stargazers) - Integrates native iOS apps with the Meteor platform through DDP.
- [delight-im/Android-DDP](https://github.com/delight-im/Android-DDP) [![GitHub stars](https://img.shields.io/github/stars/delight-im/Android-DDP?style=flat)](https://github.com/delight-im/Android-DDP/stargazers) - DDP for clients on Android.
- [okland:accounts-phone](https://github.com/okland/accounts-phone) [![GitHub stars](https://img.shields.io/github/stars/okland/accounts-phone?style=flat)](https://github.com/okland/accounts-phone/stargazers) - A login service based on mobile phone number for Meteor.
- [okland:camera-ui](https://github.com/okland/camera-ui) [![GitHub stars](https://img.shields.io/github/stars/okland/camera-ui?style=flat)](https://github.com/okland/camera-ui/stargazers) - Meteor package for taking photos with user interface, one function call on desktop and mobile. Allows to choose between camera to photoLibrary on mobile.
- [percolatestudio/cordova-plugin-safe-reload](https://github.com/percolatestudio/cordova-plugin-safe-reload) [![GitHub stars](https://img.shields.io/github/stars/percolatestudio/cordova-plugin-safe-reload?style=flat)](https://github.com/percolatestudio/cordova-plugin-safe-reload/stargazers) - Cordova plugin to watch and recover after a broken Meteor Hot Code Push.

## Data Visualization

_Data Visualization in Meteor: charts, maps, tables, etc._

- [aldeed:tabular](https://github.com/aldeed/meteor-tabular) [![GitHub stars](https://img.shields.io/github/stars/aldeed/meteor-tabular?style=flat)](https://github.com/aldeed/meteor-tabular/stargazers) - Reactive datatables for large or small datasets.
- [aslagle:reactive-table](https://github.com/aslagle/reactive-table/) [![GitHub stars](https://img.shields.io/github/stars/aslagle/reactive-table/?style=flat)](https://github.com/aslagle/reactive-table//stargazers) - Reactive table for Meteor, using Blaze.
- [luixal:blaze-paginated-custom-list](https://github.com/luixal/meteor-blaze-paginated-custom-list) [![GitHub stars](https://img.shields.io/github/stars/luixal/meteor-blaze-paginated-custom-list?style=flat)](https://github.com/luixal/meteor-blaze-paginated-custom-list/stargazers) - Reactive and paginated item list.
- [luixal:meteor-apexcharts](https://github.com/luixal/meteor-apexcharts) [![GitHub stars](https://img.shields.io/github/stars/luixal/meteor-apexcharts?style=flat)](https://github.com/luixal/meteor-apexcharts/stargazers) - Reactive ApexCharts library packaged for Meteor.

## Analytics

_Analytics_

- [okgrow:analytics](https://github.com/okgrow/analytics/) [![GitHub stars](https://img.shields.io/github/stars/okgrow/analytics/?style=flat)](https://github.com/okgrow/analytics//stargazers) - Google Analytics, Mixpanel, KISSmetrics (and more) integration for meteor.
- [quave:analytics](https://github.com/quavedev/analytics) [![GitHub stars](https://img.shields.io/github/stars/quavedev/analytics?style=flat)](https://github.com/quavedev/analytics/stargazers) - A Meteor package that allows you to send your page views and more to Google Analytics.

## Cron Jobs

_Cron Jobs in Meteor_

- [msavin:sjobs](https://github.com/msavin/stevejobs/) [![GitHub stars](https://img.shields.io/github/stars/msavin/stevejobs/?style=flat)](https://github.com/msavin/stevejobs//stargazers) - A Meteor-first jobs queue / task scheduler.
- [percolate:synced-cron](https://github.com/percolatestudio/meteor-synced-cron) [![GitHub stars](https://img.shields.io/github/stars/percolatestudio/meteor-synced-cron?style=flat)](https://github.com/percolatestudio/meteor-synced-cron/stargazers) - Cron system for Meteor. It supports syncronizing jobs between multiple processes.
- [ostrio:cron-jobs](https://github.com/VeliovGroup/Meteor-CRON-jobs) [![GitHub stars](https://img.shields.io/github/stars/VeliovGroup/Meteor-CRON-jobs?style=flat)](https://github.com/VeliovGroup/Meteor-CRON-jobs/stargazers) - Package with similar API to native `setTimeout` and `setInterval` methods, but synced between all running Meteor (NodeJS) instances.

## Debugging Tools

_Debugging Tools_

- [meteor-devtools-evolved](https://github.com/leonardoventurini/meteor-devtools-evolved) [![GitHub stars](https://img.shields.io/github/stars/leonardoventurini/meteor-devtools-evolved?style=flat)](https://github.com/leonardoventurini/meteor-devtools-evolved/stargazers) - A chrome extension.
- [msavin:mongol](https://github.com/msavin/Mongol/) [![GitHub stars](https://img.shields.io/github/stars/msavin/Mongol/?style=flat)](https://github.com/msavin/Mongol//stargazers) - Visual Editing Tool for Meteor for MongoDB Collections.
- [msavin:jetsetter](https://github.com/msavin/JetSetter) [![GitHub stars](https://img.shields.io/github/stars/msavin/JetSetter?style=flat)](https://github.com/msavin/JetSetter/stargazers) - Visual Get/Set Tool for Meteor Session Variables.
- [babrahams:constellation](https://github.com/JackAdams/constellation-distro/) [![GitHub stars](https://img.shields.io/github/stars/JackAdams/constellation-distro/?style=flat)](https://github.com/JackAdams/constellation-distro//stargazers) - An extensible dev console for Meteor.

## Editor Plugins

- [meteor-api](https://atom.io/packages/meteor-api) - Meteor addons for Atom.
- [meteor-zsh](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins#meteor) - Completion for the meteor command.

## Scaffolding

_Scaffolding_

- [Meteor Kitchen](http://www.meteorkitchen.com/) - Code generator for Meteor.
- [iron-cli](https://github.com/iron-meteor/iron-cli) [![GitHub stars](https://img.shields.io/github/stars/iron-meteor/iron-cli?style=flat)](https://github.com/iron-meteor/iron-cli/stargazers) - A scaffolding command line tool for Meteor applications.
- [maka-cli](https://github.com/maka-io/maka-cli) [![GitHub stars](https://img.shields.io/github/stars/maka-io/maka-cli?style=flat)](https://github.com/maka-io/maka-cli/stargazers) - Maka-CLI is a command line tool, which organizes a web application's file structure and automates everyday package installation tasks for various application frameworks.

## Tooling

- [ESLint-plugin-Meteor](https://github.com/dferber90/eslint-plugin-meteor/) [![GitHub stars](https://img.shields.io/github/stars/dferber90/eslint-plugin-meteor/?style=flat)](https://github.com/dferber90/eslint-plugin-meteor//stargazers) - ESLint plugin for Meteor.

## Boilerplate

- [CaptainN - meteor-react-starter](https://github.com/CaptainN/meteor-react-starter) [![GitHub stars](https://img.shields.io/github/stars/CaptainN/meteor-react-starter?style=flat)](https://github.com/CaptainN/meteor-react-starter/stargazers) - A starter project on Meteor with React.
- [Pup](https://github.com/cleverbeagle/pup) [![GitHub stars](https://img.shields.io/github/stars/cleverbeagle/pup?style=flat)](https://github.com/cleverbeagle/pup/stargazers)
- [matteodem - meteor-boilerplate](https://github.com/matteodem/meteor-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/matteodem/meteor-boilerplate?style=flat)](https://github.com/matteodem/meteor-boilerplate/stargazers)
- [React with Webpack + Meteor as a backend](http://julian.io/react-with-webpack-meteor-as-a-backend/)

## Open source apps

- [Rocket.Chat](https://rocket.chat/) - Realtime chat application built with Meteor.
- [Wekan](https://github.com/wekan/wekan) [![GitHub stars](https://img.shields.io/github/stars/wekan/wekan?style=flat)](https://github.com/wekan/wekan/stargazers) - Open source Trello-like kanban.
- [Unchained Shop](https://github.com/unchainedshop/unchained) [![GitHub stars](https://img.shields.io/github/stars/unchainedshop/unchained?style=flat)](https://github.com/unchainedshop/unchained/stargazers) - Open source Commerce platform developed with Meteor.
- [VulcanJS](https://github.com/VulcanJS/Vulcan) [![GitHub stars](https://img.shields.io/github/stars/VulcanJS/Vulcan?style=flat)](https://github.com/VulcanJS/Vulcan/stargazers) - A toolkit to quickly build apps with React, GraphQL & Meteor.
- [Nosqlclient](https://github.com/nosqlclient/nosqlclient) [![GitHub stars](https://img.shields.io/github/stars/nosqlclient/nosqlclient?style=flat)](https://github.com/nosqlclient/nosqlclient/stargazers) - MongoDB management tool.
- [radgrad2](https://github.com/radgrad/radgrad2) [![GitHub stars](https://img.shields.io/github/stars/radgrad/radgrad2?style=flat)](https://github.com/radgrad/radgrad2/stargazers) - Meteor based education management system.
- [coauthor](https://github.com/edemaine/coauthor) [![GitHub stars](https://img.shields.io/github/stars/edemaine/coauthor?style=flat)](https://github.com/edemaine/coauthor/stargazers) - Coauthor supercollaboration/discussion forum.

## Internationalization

- [Meteor-Internationalization](https://github.com/veliovgroup/Meteor-Internationalization) [![GitHub stars](https://img.shields.io/github/stars/veliovgroup/Meteor-Internationalization?style=flat)](https://github.com/veliovgroup/Meteor-Internationalization/stargazers) - Super-Lightweight and fast i18n isomorphic driver for Meteor with support of placeholders.
- [meteor-accounts-t9n](https://github.com/softwarerero/meteor-accounts-t9n/) [![GitHub stars](https://img.shields.io/github/stars/softwarerero/meteor-accounts-t9n/?style=flat)](https://github.com/softwarerero/meteor-accounts-t9n//stargazers) - Translations for meteor account's error messages.
- [meteor-universe-i18n](https://github.com/vazco/meteor-universe-i18n) [![GitHub stars](https://img.shields.io/github/stars/vazco/meteor-universe-i18n?style=flat)](https://github.com/vazco/meteor-universe-i18n/stargazers) - Internationalization package for React and Meteor.

## Front End Frameworks

_Alternative Front End Frameworks to Blaze_

- [React](http://react-in-meteor.readthedocs.org/en/latest/) - Working with React and Meteor.
- [Vue](https://github.com/meteor-vue) [![GitHub stars](https://img.shields.io/github/stars/meteor-vue?style=flat)](https://github.com/meteor-vue/stargazers) - Working with Vue and Meteor (plus single-file components & apollo support).
- [Svelte](https://github.com/zodern/melte) [![GitHub stars](https://img.shields.io/github/stars/zodern/melte?style=flat)](https://github.com/zodern/melte/stargazers) - Build cybernetically enhanced web apps with Meteor and Svelte.
- [Angular 2](https://github.com/Urigo/angular2-meteor) [![GitHub stars](https://img.shields.io/github/stars/Urigo/angular2-meteor?style=flat)](https://github.com/Urigo/angular2-meteor/stargazers) - Working with Angular 2 and Meteor.
- [Angular](https://github.com/Urigo/angular-meteor) [![GitHub stars](https://img.shields.io/github/stars/Urigo/angular-meteor?style=flat)](https://github.com/Urigo/angular-meteor/stargazers) - Working with Angular and Meteor.
- [Famo.us](https://github.com/gadicc/meteor-famous-views/) [![GitHub stars](https://img.shields.io/github/stars/gadicc/meteor-famous-views/?style=flat)](https://github.com/gadicc/meteor-famous-views//stargazers) - Famo.us and Meteor.
- [frozeman:build-client](https://github.com/frozeman/meteor-build-client) [![GitHub stars](https://img.shields.io/github/stars/frozeman/meteor-build-client?style=flat)](https://github.com/frozeman/meteor-build-client/stargazers) - A tool to bundle the client part of a Meteor app.
- [Asteroid](https://github.com/mondora/asteroid) [![GitHub stars](https://img.shields.io/github/stars/mondora/asteroid?style=flat)](https://github.com/mondora/asteroid/stargazers) - An alternative client for a Meteor backend.
- [ddp.js](https://github.com/mondora/ddp.js) [![GitHub stars](https://img.shields.io/github/stars/mondora/ddp.js?style=flat)](https://github.com/mondora/ddp.js/stargazers) - Isomorphic JavaScript DDP client.
- [elm](https://github.com/ni-ko-o-kin/meteor-elm-example) [![GitHub stars](https://img.shields.io/github/stars/ni-ko-o-kin/meteor-elm-example?style=flat)](https://github.com/ni-ko-o-kin/meteor-elm-example/stargazers) - elm as the view layer for a meteor based project.

## Alternative Databases

_Alternative Databases for MongoDB_

- [vlasky:mysql](https://github.com/vlasky/meteor-mysql) [![GitHub stars](https://img.shields.io/github/stars/vlasky/meteor-mysql?style=flat)](https://github.com/vlasky/meteor-mysql/stargazers) - Reactive MySQL for Meteor
- [meteor-pg](https://github.com/Richie765/meteor-pg) [![GitHub stars](https://img.shields.io/github/stars/Richie765/meteor-pg?style=flat)](https://github.com/Richie765/meteor-pg/stargazers) - New and improved PostgreSQL support for Meteor
- [ostrio:neo4jdriver](https://github.com/VeliovGroup/ostrio-neo4jdriver/) [![GitHub stars](https://img.shields.io/github/stars/VeliovGroup/ostrio-neo4jdriver/?style=flat)](https://github.com/VeliovGroup/ostrio-neo4jdriver//stargazers) - Neo4j Driver for Meteor, with support of GrapheneDB
- [numtel:pg](https://github.com/numtel/meteor-pg) [![GitHub stars](https://img.shields.io/github/stars/numtel/meteor-pg?style=flat)](https://github.com/numtel/meteor-pg/stargazers) - Reactive PostgreSQL for Meteor
- [simple:rethink](https://github.com/Slava/meteor-rethinkdb) [![GitHub stars](https://img.shields.io/github/stars/Slava/meteor-rethinkdb?style=flat)](https://github.com/Slava/meteor-rethinkdb/stargazers) - RethinkDB integration for Meteor

# Resources

_Where to discover new Meteor things_

## Books

- [Meteor Explained](https://gumroad.com/l/meteor-explained)
- [Secure Meteor](https://www.securemeteor.com/)
- [meteor-tuts](https://www.meteor-tuts.com/) - Free
- [Meteor Tips](http://meteortips.com/) - Free
- [Pro Meteor](https://pdfslide.net/documents/pro-meteor-book.html) - Free
- [Meteor Cookbook](https://github.com/awatson1978/meteor-cookbook) [![GitHub stars](https://img.shields.io/github/stars/awatson1978/meteor-cookbook?style=flat)](https://github.com/awatson1978/meteor-cookbook/stargazers)

## Courses

- #### Free

  - [How to Create an App](https://www.youtube.com/c/Howtocreateanappdev/videos) - Most updated.
  - [EventedMind](https://learn-meteor.netlify.app/) - It's old but goes into detail regarding how Meteor internals.

- #### Paid
  - [Udemy - Learn React and Meteor in 2021: Build a multiplayer game](https://www.udemy.com/course/modern-web-development-with-react-and-meteor-2021/)
  - [Udemy - Realtime Applications with Meteor and Vue](https://www.udemy.com/course/meteor-vue) - Course in Spanish.
  - [leveluptutorials](https://www.leveluptutorials.com/) - Contains some free tutorials but mostly on 1.x.

## Tutorials


- [Phusion Passenger: Meteor tutorial](https://github.com/phusion/passenger/wiki/Phusion-Passenger:-Meteor-tutorial) [![GitHub stars](https://img.shields.io/github/stars/phusion/passenger/wiki/Phusion-Passenger:-Meteor-tutorial?style=flat)](https://github.com/phusion/passenger/wiki/Phusion-Passenger:-Meteor-tutorial/stargazers)
- [When a Meteor finally hits production](https://medium.com/@davidyahalomi/when-a-meteor-finally-hits-production-6c37b81f795b) - Blog post about deploying Meteor apps
- [Transform any Meteor App into a PWA](https://dev.to/jankapunkt/transform-any-meteor-app-into-a-pwa-4k44)

## Blogs

- [Official Meteor blog](http://blog.meteor.com)
- [The Meteor podcast](http://podcast.crater.io)

## Websites

- [Official website](https://www.meteor.com/)
- [Official Documentation](http://docs.meteor.com/)
- [Official Guide](http://guide.meteor.com/)
- [Atmosphere](https://atmospherejs.com/) - The catalog of Meteor packages, resources and tools.
- [Packosphere](https://packosphere.com/) - Alternative front-end for Meteor package system, built by [Kelly Copley
](https://github.com/copleykj)
- [Discover Meteor](https://book.discovermeteor.com/)
- [Meteorpedia](http://www.meteorpedia.com) ([infrequently](http://www.meteorpedia.com/special/RecentChanges/) updated)
- [Meetups](http://meteor.meetup.com/)
- [Reddit](https://www.reddit.com/r/meteor)
- [YouTube](https://www.youtube.com/channel/UC3fBiJrFFMhKlsWM46AsAYw) videos from meetups around the world
- [Unofficial Meteor FAQ](https://github.com/oortcloud/unofficial-meteor-faq) [![GitHub stars](https://img.shields.io/github/stars/oortcloud/unofficial-meteor-faq?style=flat)](https://github.com/oortcloud/unofficial-meteor-faq/stargazers)
- [The Meteor Chef](https://themeteorchef.com)

### Q&A

- [Stack Overflow](http://stackoverflow.com/questions/tagged/meteor?sort=newest&pagesize=15)
- [Meteor forums](https://forums.meteor.com/)

### Community Newsletters

- [zodern](https://zodern.me/newsletter.html)
- [StorytellerCZ](https://forums.meteor.com/t/meteor-community-newsletter/50598)

## Social

- [Official Twitter Account](https://twitter.com/meteorjs)
- [Meteor Community Organization Slack Channel](https://github.com/Meteor-Community-Packages/organization#slack)


## Work Opportunities

- [Awesome Meteor Jobs](https://github.com/harryadel/awesome-meteor-jobs) [![GitHub stars](https://img.shields.io/github/stars/harryadel/awesome-meteor-jobs?style=flat)](https://github.com/harryadel/awesome-meteor-jobs/stargazers)
- [We work Meteor](https://www.weworkmeteor.com/)
- [Official Job Board](https://jobs.meteor.com/)

## Related

- [Awesome Meteor Developers](https://github.com/harryadelb/awesome-meteor-developers) [![GitHub stars](https://img.shields.io/github/stars/harryadelb/awesome-meteor-developers?style=flat)](https://github.com/harryadelb/awesome-meteor-developers/stargazers)
- [Awesome Blaze](https://github.com/arggh/awesome-blaze) [![GitHub stars](https://img.shields.io/github/stars/arggh/awesome-blaze?style=flat)](https://github.com/arggh/awesome-blaze/stargazers)

## Built With Meteor

_Commercial Grade Applications Built With Meteor_

- [Qualia](https://www.qualia.com/) - Real Estate Startup
- [Code Signal](https://codesignal.com/) - Skills-based assessment platform
- [Pathable](Pathable) - Events managment suite
- [MaestroQA](https://www.maestroqa.com/) - Quality assurance software

## Deprecated

_This section is desginated for resources which are no longer compatible with the current version of Meteor_

- [Meteor 1.4 + React For Everyone Tutorials](https://www.leveluptutorials.com/tutorials/meteor-1-4-react-for-everyone-tutorials)
- [Meteor 1.4 For Everyone](https://www.leveluptutorials.com/tutorials/meteor-1-4-for-everyone)
- [Intermediate Meteor](https://www.leveluptutorials.com/tutorials/intermediate-meteor)
- [Meteor For Everyone Tutorials](https://www.leveluptutorials.com/tutorials/meteor-for-everyone-tutorials)
- [tuts+ - Single Page Web Apps with Meteor](http://code.tutsplus.com/courses/single-page-web-apps-with-meteor)
- [Building a CMS-powered blog in Meteor](https://buttercms.com/blog/meteor-cms-blog-tutorial)
- [scotch.io - Building a Slack Clone in Meteor](https://scotch.io/tutorials/building-a-slack-clone-in-meteor-js-getting-started)

## [Contributing](https://github.com/urigo/awesome-meteor/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/urigo/awesome-meteor/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/urigo/awesome-meteor/blob/master/CONTRIBUTING.md/stargazers)

Your contributions are always welcome!

Thank you @gillesfabio for creating this repo!
