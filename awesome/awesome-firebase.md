# Firebase

> 来源：[jthegedus/awesome-firebase](https://github.com/jthegedus/awesome-firebase)

[![GitHub stars](https://img.shields.io/github/stars/jthegedus/awesome-firebase?style=flat)](https://github.com/jthegedus/awesome-firebase/stargazers)

<!-- badges -->
<div align="center">

<!-- title -->
<!--lint ignore no-dead-urls-->
# Awesome Firebase [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Lint Awesome List](https://github.com/jthegedus/awesome-firebase/workflows/lint/badge.svg) [![GitHub stars](https://img.shields.io/github/stars/jthegedus/awesome-firebase/workflows/lint/badge.svg?style=flat)](https://github.com/jthegedus/awesome-firebase/workflows/lint/badge.svg/stargazers)

<!-- subtitle -->

The most **up to date** list of Firebase docs, talks, tools, examples & articles the internet has to offer.

<!-- image -->

<a href="https://firebase.google.com/docs/" target="_blank" rel="noopener noreferrer">
  <img src="images/firebase-services.gif" />
</a>

<!-- translations -->

Translations: [🇬🇧 en](readme.md) · [🇰🇷 ko](readme-ko.md) · [🇷🇺 ru](readme-ru.md) <!-- · [🇪🇸 es](readme-es.md) · [🇮🇩 id](readme-id.md) · [🇯🇵 ja](readme-ja.md) · [🇵🇹 pt](readme-pt.md) · [🇨🇳 zh](readme-zh.md) -->

[Firebase](https://firebase.google.com) is an app dev platform built on the [Google Cloud Platform](https://cloud.google.com/products) providing services and cross-platform SDKs!

</div>

<!-- toc -->

## Contents

- [Featured (new releases)](#featured-new-releases)
- [Official Docs & Quickstarts](#official-docs--quickstarts)
- [Firebase Extensions](#firebase-extensions)
- [Web](#web)
- [Mobile](#mobile)
- [Games](#games)
- [Server-side (Cloud Functions, BigQuery etc)](#server-side-cloud-functions-bigquery-etc)
- [CLI & Editor](#cli--editor)
- [Other](#other)
- [Follow](#follow)

**Legend**: 📝 blog posts · 💡 examples · 📖 docs · 🔌 libraries · 🔧 tools · 📹 talks/video · 🔊 podcasts

<!-- START content -->

## Featured (new releases)

- 🔧 [(Unofficial) Firebase Admin SDK for PHP](https://github.com/kreait/firebase-php) [![GitHub stars](https://img.shields.io/github/stars/kreait/firebase-php?style=flat)](https://github.com/kreait/firebase-php/stargazers) - The Firebase Admin PHP SDK enables access to Firebase services from privileged environments (such as servers or cloud) in PHP.
- 📖 [App Check](https://firebase.google.com/docs/app-check) - Protect your backend resources from abuse, such as billing fraud or phishing.
- 📖 [Firestore Data Bundles](https://firebase.google.com/docs/firestore/bundles) - Data Bundles are static query results for CDN caching to speed first page loads.
- 📖 [Modular Web SDK (v9)](https://firebase.google.com/docs/web/learn-more#modular-version) - Import only what you need reducing SDK size up to 80%.

## Official Docs & Quickstarts

- 📖 [Firebase Documentation](https://firebase.google.com/docs) - Official Firebase Documentation.
- 🔧 [Firebase Status Dashboard](https://status.firebase.google.com) - This page provides status information on the services that are part of Firebase.
- 💡 [Firebase Quickstarts](https://github.com/firebase?utf8=%E2%9C%93&q=quickstart&type=&language=) [![GitHub stars](https://img.shields.io/github/stars/firebase?utf8=%E2%9C%93&q=quickstart&type=&language=?style=flat)](https://github.com/firebase?utf8=%E2%9C%93&q=quickstart&type=&language=/stargazers) - Official Firebase Quickstarts.
- 💡 [Google Codelabs | Firebase](https://codelabs.developers.google.com/?cat=Firebase) - Google Developers Codelabs provide a guided, tutorial, hands-on coding experience.
- 📖 [Firebase for Games](https://firebase.google.com/games) - New Firebase for Games landing page with links to Firebase/Google resources for game developers.

## Firebase Extensions

- 🔧 [Firebase Extensions](https://firebase.google.com/products/extensions) - Firebase Extensions provide extended functionality to your apps without the need to research, write, or debug code on your own.
- 🔧 [Experimental Firebase Extensions](https://github.com/FirebaseExtended/experimental-extensions) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/experimental-extensions?style=flat)](https://github.com/FirebaseExtended/experimental-extensions/stargazers) -  laboratory for new extensions created by Firebase.
- 🔧 [Stripe Extensions](https://github.com/stripe/stripe-firebase-extensions) [![GitHub stars](https://img.shields.io/github/stars/stripe/stripe-firebase-extensions?style=flat)](https://github.com/stripe/stripe-firebase-extensions/stargazers) - Official Stripe subscriptions and invoices extensions.
- 🔧 [MessageBird Extensions](https://github.com/messagebird/firestore-send-msg) [![GitHub stars](https://img.shields.io/github/stars/messagebird/firestore-send-msg?style=flat)](https://github.com/messagebird/firestore-send-msg/stargazers) - Official MessageBird extension to send messages via the MessageBird Converstations API.
- 🔧 [Algolia Extensions](https://github.com/algolia/firestore-algolia-search) [![GitHub stars](https://img.shields.io/github/stars/algolia/firestore-algolia-search?style=flat)](https://github.com/algolia/firestore-algolia-search/stargazers) - Official Algolia extension to enable full text search of Cloud Firestore with Algolia.
- 🔧 [Mailchimp Extensions](https://github.com/mailchimp/Firebase) [![GitHub stars](https://img.shields.io/github/stars/mailchimp/Firebase?style=flat)](https://github.com/mailchimp/Firebase/stargazers) - Official Mailchimp extension to sync Firebase Authentication events to create member tags, merge fields, and member events with Mailchimp.
- 🔧 [Typesense Extension for Full-Text Search](https://github.com/typesense/firestore-typesense-search) [![GitHub stars](https://img.shields.io/github/stars/typesense/firestore-typesense-search?style=flat)](https://github.com/typesense/firestore-typesense-search/stargazers) - Official Typesense extension to add full-text search in Firestore, by syncing the data to [Typesense](https://github.com/typesense/typesense) [![GitHub stars](https://img.shields.io/github/stars/typesense/typesense?style=flat)](https://github.com/typesense/typesense/stargazers), an OSS alternative to Algolia.

## Web

- 🔌 [Firestore Lite](https://github.com/samuelgozi/firebase-firestore-lite) [![GitHub stars](https://img.shields.io/github/stars/samuelgozi/firebase-firestore-lite?style=flat)](https://github.com/samuelgozi/firebase-firestore-lite/stargazers) - Lightweight Cloud Firestore library for the browser.
- 🔌 [SvelteFire](https://github.com/codediodeio/sveltefire) [![GitHub stars](https://img.shields.io/github/stars/codediodeio/sveltefire?style=flat)](https://github.com/codediodeio/sveltefire/stargazers) - Cybernetically enhanced Firebase apps.
- 🔌 [React Fire](https://github.com/FirebaseExtended/reactfire) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/reactfire?style=flat)](https://github.com/FirebaseExtended/reactfire/stargazers) - Official Firebase React library with Hooks, Context Providers, and Components that make it easy to interact with Firebase.
- 🔧 [Remote Styles with Remote Config](https://github.com/firebaseextended/remote-styles/) [![GitHub stars](https://img.shields.io/github/stars/firebaseextended/remote-styles/?style=flat)](https://github.com/firebaseextended/remote-styles//stargazers) - Dynamic/Conditional loading of CSS stored in Remote Config. ([Launch post](https://medium.com/firebase-developers/introducing-remote-styles-conditional-css-loading-made-easy-daddbbcce050)).
- 🔌 [React Firebase Hooks](https://github.com/CSFrequency/react-firebase-hooks) [![GitHub stars](https://img.shields.io/github/stars/CSFrequency/react-firebase-hooks?style=flat)](https://github.com/CSFrequency/react-firebase-hooks/stargazers) - React Hooks for Firebase services.
- 🔌 [Firebase UI](https://github.com/firebase/firebaseui-web) [![GitHub stars](https://img.shields.io/github/stars/firebase/firebaseui-web?style=flat)](https://github.com/firebase/firebaseui-web/stargazers) - FirebaseUI is an open-source JavaScript library for Web that provides simple, customizable UI bindings on top of Firebase SDKs to eliminate boilerplate code and promote best practices.
- 🔌 [Firebase UI for React](https://github.com/firebase/firebaseui-web-react) [![GitHub stars](https://img.shields.io/github/stars/firebase/firebaseui-web-react?style=flat)](https://github.com/firebase/firebaseui-web-react/stargazers) - React Wrapper for firebaseUI Web.
- 🔌 [GeoFire for JavaScript](https://github.com/firebase/geofire-js) [![GitHub stars](https://img.shields.io/github/stars/firebase/geofire-js?style=flat)](https://github.com/firebase/geofire-js/stargazers) - Realtime location queries with Firebase.
- 💡 [FirePad](https://github.com/FirebaseExtended/firepad) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/firepad?style=flat)](https://github.com/FirebaseExtended/firepad/stargazers) - Collaborative Text Editor Powered by Firebase.
- 🔌 [Ember Fire](https://github.com/firebase/emberFire) [![GitHub stars](https://img.shields.io/github/stars/firebase/emberFire?style=flat)](https://github.com/firebase/emberFire/stargazers) - Official Ember data adapter for Firebase.
- 🔌 [Firebase Dart](https://github.com/FirebaseExtended/firebase-dart) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/firebase-dart?style=flat)](https://github.com/FirebaseExtended/firebase-dart/stargazers) - Dart wrapper for Firebase.
- 🔌 [PolymerFire](https://github.com/FirebaseExtended/polymerfire) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/polymerfire?style=flat)](https://github.com/FirebaseExtended/polymerfire/stargazers) - Polymer Web Components for Firebase.
- 🔌 [VueFire](https://github.com/vuejs/vuefire) [![GitHub stars](https://img.shields.io/github/stars/vuejs/vuefire?style=flat)](https://github.com/vuejs/vuefire/stargazers) - Firebase bindings for Vue.js.
- 🔌 [Angular Fire 2](https://github.com/angular/angularfire2) [![GitHub stars](https://img.shields.io/github/stars/angular/angularfire2?style=flat)](https://github.com/angular/angularfire2/stargazers) - Official library for Firebase and Angular.
- 🔌 [Re-base](https://github.com/tylermcginnis/re-base) [![GitHub stars](https://img.shields.io/github/stars/tylermcginnis/re-base?style=flat)](https://github.com/tylermcginnis/re-base/stargazers) - Relay inspired library for building React.js + Firebase applications.
- 🔌 [React Redux Firebase](https://github.com/prescottprue/react-redux-firebase) [![GitHub stars](https://img.shields.io/github/stars/prescottprue/react-redux-firebase?style=flat)](https://github.com/prescottprue/react-redux-firebase/stargazers) - Redux bindings for Firebase. Includes Higher Order Component for use with React.
- 🔌 [GatsbyJS Firebase Data Source](https://www.gatsbyjs.org/packages/) - Query your Firebase data right into your statically generated pages with Gatsby.
- 🔌 [Apollo Link Firebase](https://github.com/Canner/apollo-link-firebase) [![GitHub stars](https://img.shields.io/github/stars/Canner/apollo-link-firebase?style=flat)](https://github.com/Canner/apollo-link-firebase/stargazers) - Provides a local GraphQL interface to RealtimeDB. DB syncs locally to device, Apollo Link provides querying into the local DB.
- 🔌 [BuckleScript Bindings for Firebase](https://github.com/avohq/bs-firebase) [![GitHub stars](https://img.shields.io/github/stars/avohq/bs-firebase?style=flat)](https://github.com/avohq/bs-firebase/stargazers) - BuckleScript bindings for Firebase for use in ReasonML projects.
- 💡 [Angular Firebase PWA](https://github.com/codediodeio/angular-firestarter) [![GitHub stars](https://img.shields.io/github/stars/codediodeio/angular-firestarter?style=flat)](https://github.com/codediodeio/angular-firestarter/stargazers) - Is an Angular PWA powered by Firebase. It can serve as a foundation to learn this stack and roll out more complex features.
- 🔌 [FireSQL](https://github.com/jsayol/FireSQL) [![GitHub stars](https://img.shields.io/github/stars/jsayol/FireSQL?style=flat)](https://github.com/jsayol/FireSQL/stargazers) - Query Firestore using SQL syntax. Issues the minimum amount of queries necessary in order to get the data that you request.
- 📖 [Hosting Version History](https://firebase.google.com/docs/hosting/deploying#set_limit_for_retained_versions) - Automatic deletion of older versions of your site deployments.
- 🔌 [Firestorter](https://github.com/IjzerenHein/firestorter) [![GitHub stars](https://img.shields.io/github/stars/IjzerenHein/firestorter?style=flat)](https://github.com/IjzerenHein/firestorter/stargazers) - Use Firestore in React with zero effort, using MobX (also for react-native).
- 💡 [Nextbase](https://github.com/martyan/nextbase) [![GitHub stars](https://img.shields.io/github/stars/martyan/nextbase?style=flat)](https://github.com/martyan/nextbase/stargazers) - Boilerplate of Next.js, Redux & Firebase for developers who want a quick start project.
- 🔧 [Typesaurus](https://github.com/kossnocorp/typesaurus) [![GitHub stars](https://img.shields.io/github/stars/kossnocorp/typesaurus?style=flat)](https://github.com/kossnocorp/typesaurus/stargazers) - Type-safe TypeScript-first ODM for Firestore.
- 🔌 [firebase-kotlin-sdk](https://github.com/GitLiveApp/firebase-kotlin-sdk/) [![GitHub stars](https://img.shields.io/github/stars/GitLiveApp/firebase-kotlin-sdk/?style=flat)](https://github.com/GitLiveApp/firebase-kotlin-sdk//stargazers) - Kotlin-first SDK for Firebase supporting multiplatform projects (`ios`, `android` & `js`).
- 🔌 [GeoFirestore](https://github.com/MichaelSolati/geofirestore-js) [![GitHub stars](https://img.shields.io/github/stars/MichaelSolati/geofirestore-js?style=flat)](https://github.com/MichaelSolati/geofirestore-js/stargazers) - Location-based querying and filtering using Firebase Firestore.
- 🔧 [FirelordJS](https://github.com/tylim88/FirelordJS) [![GitHub stars](https://img.shields.io/github/stars/tylim88/FirelordJS?style=flat)](https://github.com/tylim88/FirelordJS/stargazers) - Extremely High Precision Typescript Wrapper for Firestore Web. ([Admin version](https://github.com/tylim88/Firelord) [![GitHub stars](https://img.shields.io/github/stars/tylim88/Firelord?style=flat)](https://github.com/tylim88/Firelord/stargazers))
- 🔧 [FireSageJS](https://github.com/tylim88/FireSageJS) [![GitHub stars](https://img.shields.io/github/stars/tylim88/FireSageJS?style=flat)](https://github.com/tylim88/FireSageJS/stargazers) - Extreme Type Safe For Realtime Database Web.

## Mobile

- 📝 [App Distribution App Bundles](https://firebase.googleblog.com/2021/05/app-distribution-adds-support-to-android-app-bundles.html) - Support for Android App Bundles (AAB) is officially supported in App Distribution.
- 📖 [Firebase Flutter Documentation](https://firebase.google.com/docs/flutter/setup) - Official Firebase Flutter Setup.
- 🔌 [NativeScript plugin Firebase](https://github.com/EddyVerbruggen/nativescript-plugin-firebase) [![GitHub stars](https://img.shields.io/github/stars/EddyVerbruggen/nativescript-plugin-firebase?style=flat)](https://github.com/EddyVerbruggen/nativescript-plugin-firebase/stargazers) - NativeScript plugin for Firebase.
- 🔌 [FlutterFire](https://github.com/FirebaseExtended/flutterfire) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/flutterfire?style=flat)](https://github.com/FirebaseExtended/flutterfire/stargazers) - Collection of Firebase plugins for [Flutter](https://flutter.io/) apps.
- 🔌 [React Native Firebase](https://github.com/invertase/react-native-firebase) [![GitHub stars](https://img.shields.io/github/stars/invertase/react-native-firebase?style=flat)](https://github.com/invertase/react-native-firebase/stargazers) - Well-tested feature rich modular Firebase implementation for React Native. Supports both iOS & Android platforms.
- 🔌 [React Native Firebase Cloud Messaging](https://github.com/evollu/react-native-fcm) [![GitHub stars](https://img.shields.io/github/stars/evollu/react-native-fcm?style=flat)](https://github.com/evollu/react-native-fcm/stargazers) -
  React Native module for Firebase Cloud Messaging and local notification.
- 💡 [Expo Native Firebase](https://github.com/EvanBacon/expo-native-firebase) [![GitHub stars](https://img.shields.io/github/stars/EvanBacon/expo-native-firebase?style=flat)](https://github.com/EvanBacon/expo-native-firebase/stargazers) - Native Firebase Expo App (iOS, Android) Demo for Firestore, Notifications, Analytics, Storage, Messaging, Database.
- 💡 [Flutter Calendar App](https://github.com/mattgraham1/FlutterCalendar) [![GitHub stars](https://img.shields.io/github/stars/mattgraham1/FlutterCalendar?style=flat)](https://github.com/mattgraham1/FlutterCalendar/stargazers) -
  New Flutter application implementing a simple mobile calendar app for storing basic events into Firebase cloud database.
- 🔧 [Firebase App Distribution](https://firebase.google.com/products/app-distribution/) - Distribute pre-release versions of your app to your trusted testers.
- 🔌 [Flamingo](https://github.com/hukusuke1007/flamingo) [![GitHub stars](https://img.shields.io/github/stars/hukusuke1007/flamingo?style=flat)](https://github.com/hukusuke1007/flamingo/stargazers) - A Firebase Firestore model framework for Dart.

### Android

- 🔌 [GeoFire for Java](https://github.com/firebase/geofire-java) [![GitHub stars](https://img.shields.io/github/stars/firebase/geofire-java?style=flat)](https://github.com/firebase/geofire-java/stargazers) - Realtime location queries with Firebase.
- 🔌 [Firebase UI](https://github.com/firebase/firebaseui-android) [![GitHub stars](https://img.shields.io/github/stars/firebase/firebaseui-android?style=flat)](https://github.com/firebase/firebaseui-android/stargazers) - Optimized UI components for Firebase.
- 🔌 [FireXtensions](https://github.com/rosariopfernandes/firextensions) [![GitHub stars](https://img.shields.io/github/stars/rosariopfernandes/firextensions?style=flat)](https://github.com/rosariopfernandes/firextensions/stargazers) - Unofficial Kotlin Extensions for the Firebase Android SDK.
- 🔌 [Firecoil](https://github.com/rosariopfernandes/firecoil) [![GitHub stars](https://img.shields.io/github/stars/rosariopfernandes/firecoil?style=flat)](https://github.com/rosariopfernandes/firecoil/stargazers) - Load images from GCS in your Android app using the image loading library Coil.

### iOS

- 🔌 [GeoFire for Objective-C](https://github.com/firebase/geofire-objc) [![GitHub stars](https://img.shields.io/github/stars/firebase/geofire-objc?style=flat)](https://github.com/firebase/geofire-objc/stargazers) - Realtime location queries with Firebase.
- 🔌 [Firebase UI](https://github.com/firebase/firebaseui-ios) [![GitHub stars](https://img.shields.io/github/stars/firebase/firebaseui-ios?style=flat)](https://github.com/firebase/firebaseui-ios/stargazers) - iOS UI bindings for Firebase.
- 💡 [MLKit - ARCore](https://github.com/FirebaseExtended/MLKit-ARCore) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/MLKit-ARCore?style=flat)](https://github.com/FirebaseExtended/MLKit-ARCore/stargazers) - Example detecting objects and tags them with 3D labels in Augmented Reality. Uses Firebase ML Kit, ARCore and Firebase RTDB.
- 💡 [MLKit - ARKit](https://github.com/FirebaseExtended/MLKit-ARKit) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/MLKit-ARKit?style=flat)](https://github.com/FirebaseExtended/MLKit-ARKit/stargazers) - Example detecting objects using Firebase ML Kit and tags them with 3D labels in Augmented Reality.

## Games

- 📖 [Firestore for C++ and Unity](https://firebase.google.com/docs/firestore) - C++ and Unity SDKs for C++ and Unity (with Firebase Unity SDKs available via Unity Package Manager).

## Server-side (Cloud Functions, BigQuery etc)

- 📖 [Firebase Admin Documentation](https://firebase.google.com/docs/admin/setup) - Official Firebase Admin SDK Server Setup.
- 💡 [Functions Samples](https://github.com/firebase/functions-samples) [![GitHub stars](https://img.shields.io/github/stars/firebase/functions-samples?style=flat)](https://github.com/firebase/functions-samples/stargazers) - Collection of sample apps showcasing popular use cases using Cloud Functions for Firebase.
- 💡 [Express Server on Cloud Functions](https://github.com/jthegedus/firebase-gcp-examples/tree/main/functions-express) [![GitHub stars](https://img.shields.io/github/stars/jthegedus/firebase-gcp-examples/tree/main/functions-express?style=flat)](https://github.com/jthegedus/firebase-gcp-examples/tree/main/functions-express/stargazers) - Host an Express server on Cloud Functions.
- 📝 [GraphQL Server on Cloud Functions](https://codeburst.io/graphql-server-on-cloud-functions-for-firebase-ae97441399c0) - Host an Express server with GraphQL middleware on Cloud Functions.
- 💡 [Compiled Code with Cloud Functions](https://github.com/jthegedus/firebase-gcp-examples/tree/main/functions-w-parcel) [![GitHub stars](https://img.shields.io/github/stars/jthegedus/firebase-gcp-examples/tree/main/functions-w-parcel?style=flat)](https://github.com/jthegedus/firebase-gcp-examples/tree/main/functions-w-parcel/stargazers) - Compile your Flow, TypeScript or ReasonML to the correct Node runtime using Babel, TypeScript Compiler or ParcelJS.
- 📝 [BigQuery & Google Analytics](https://medium.com/firebase-developers/how-do-i-create-a-closed-funnel-in-google-analytics-for-firebase-using-bigquery-6eb2645917e1) - How Do I Create a Closed Funnel in Google Analytics for Firebase Using BigQuery.
<!--lint ignore double-link-->
- 📹 [Official Cloud Function #Firecasts](https://www.youtube.com/watch?v=2mjfI0FYP7Y&list=PLl-K7zZEsYLm9A9rcHb1IkyQUu6QwbjdM) - YouTube video series about understanding how Cloud Functions work.
- 📝 [Firebase Hosting for Cloud Run Services](https://firebase.googleblog.com/2019/04/firebase-hosting-and-cloud-run.html) - Dynamic content with Hosting Rewrites & Cloud Run Services.
- 📝 [Scheduled (Cron) Cloud Functions for Firebase](https://firebase.googleblog.com/2019/04/schedule-cloud-functions-firebase-cron.html) - Firebase-native Cron triggers for Firebase Cloud Functions.
- 🔌 [Integrify](https://github.com/anishkny/integrify) [![GitHub stars](https://img.shields.io/github/stars/anishkny/integrify?style=flat)](https://github.com/anishkny/integrify/stargazers) - Enforce referential and data integrity in Firestore using pre-canned Cloud Functions triggers.
- 🔌 [Free Product Analytics with Firebase + BigQuery + Rakam](https://rakam.io/blog/free-product-analytics-with-firebase---bigquery---rakam/) - How to do behavioral & segmentation analysis on Firebase event data via BigQuery Export and Rakam.
- 🔌 [Firestore Queue System](https://github.com/sbarbat/firestore-queuer) [![GitHub stars](https://img.shields.io/github/stars/sbarbat/firestore-queuer?style=flat)](https://github.com/sbarbat/firestore-queuer/stargazers) - Simple queue system using Firestore and Cloud Functions.
- 🔌 [Pyrebase](https://github.com/thisbejim/Pyrebase) [![GitHub stars](https://img.shields.io/github/stars/thisbejim/Pyrebase?style=flat)](https://github.com/thisbejim/Pyrebase/stargazers) - A simple python wrapper for the Firebase API.
- 🔌 [Firecode](https://github.com/kafkas/firecode) [![GitHub stars](https://img.shields.io/github/stars/kafkas/firecode?style=flat)](https://github.com/kafkas/firecode/stargazers) - A light, fast, and memory-efficient collection traversal library for Firestore and Node.js.

## CLI & Editor

- 📖 [Firebase Tools UI](https://github.com/firebase/firebase-tools-ui) [![GitHub stars](https://img.shields.io/github/stars/firebase/firebase-tools-ui?style=flat)](https://github.com/firebase/firebase-tools-ui/stargazers) - Web UI for Firebase Emulator Suite.
- 📖 [Storage in Emulator Suite](https://firebase.google.com/docs/emulator-suite/connect_storage) - Emulator suite is now complete!
- 🔧 [VSCode Firebase Explorer](https://github.com/jsayol/vscode-firebase-explorer) [![GitHub stars](https://img.shields.io/github/stars/jsayol/vscode-firebase-explorer?style=flat)](https://github.com/jsayol/vscode-firebase-explorer/stargazers) - Explore and manage your Firebase projects.
- 🔧 [Firebase Tools](https://github.com/firebase/firebase-tools) [![GitHub stars](https://img.shields.io/github/stars/firebase/firebase-tools?style=flat)](https://github.com/firebase/firebase-tools/stargazers) - The Firebase Command Line Tools.
- 🔧 [Firebase CI](https://github.com/prescottprue/firebase-ci) [![GitHub stars](https://img.shields.io/github/stars/prescottprue/firebase-ci?style=flat)](https://github.com/prescottprue/firebase-ci/stargazers) - Simplified Firebase interaction for continuous integration.
- 🔧 [Firecode](https://github.com/ChFlick/firecode) [![GitHub stars](https://img.shields.io/github/stars/ChFlick/firecode?style=flat)](https://github.com/ChFlick/firecode/stargazers) -  VS Code Firestore Rules Extension.
- 🔧 [Firebase Firestore Snippets](https://github.com/peterhdd/firebase-firestore-snippets) [![GitHub stars](https://img.shields.io/github/stars/peterhdd/firebase-firestore-snippets?style=flat)](https://github.com/peterhdd/firebase-firestore-snippets/stargazers) - Contains the snippet for both Firebase and Firestore in VS Code editor.
- 🔧 [Fuego](https://github.com/sgarciac/fuego) [![GitHub stars](https://img.shields.io/github/stars/sgarciac/fuego?style=flat)](https://github.com/sgarciac/fuego/stargazers) - Firestore client CLI supporting document add/update/query with filtering and pagination.
- 🔧 [Firestore Rules Generator](https://github.com/FirebaseExtended/protobuf-rules-gen) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/protobuf-rules-gen?style=flat)](https://github.com/FirebaseExtended/protobuf-rules-gen/stargazers) - Official (but experimental) Firebase Rules Generator for Cloud Firestore based on Google's Protocol Buffer format.
- 🔧 [Firepit](https://github.com/abehaskins/firepit) [![GitHub stars](https://img.shields.io/github/stars/abehaskins/firepit?style=flat)](https://github.com/abehaskins/firepit/stargazers) - Firepit is a standalone, portable version of the Firebase CLI which has no depedencies (including Node.js).
- 🔧 [Fireward](https://github.com/bijoutrouvaille/fireward) [![GitHub stars](https://img.shields.io/github/stars/bijoutrouvaille/fireward?style=flat)](https://github.com/bijoutrouvaille/fireward/stargazers) - Easy to use language for Firestore rules, similar to Firebase Bolt.
- 🔧 [Svarog](https://github.com/dantothefuture/svarog) [![GitHub stars](https://img.shields.io/github/stars/dantothefuture/svarog?style=flat)](https://github.com/dantothefuture/svarog/stargazers) - Cloud Firestore schema validation with JSON Schema generated Security Rule helper functions.
- 🔧 [Firetable](https://github.com/AntlerVC/firetable) [![GitHub stars](https://img.shields.io/github/stars/AntlerVC/firetable?style=flat)](https://github.com/AntlerVC/firetable/stargazers) - Excel/Google Sheets like UI for Firebase/Firestore. No more admin portals!
- 🔧 [VSFire](https://github.com/toba/vsfire) [![GitHub stars](https://img.shields.io/github/stars/toba/vsfire?style=flat)](https://github.com/toba/vsfire/stargazers) - Deprecated ~VSCode extension for syntax highlighting & code completions with Firestore security rules & indexes.~
- 📝 [Refi App](https://refiapp.io/) - A GUI tool to make developers less painful when interacting with Firestore DB
- 🔧 [Firefoo](https://firefoo.app) - Cloud Firestore GUI Admin Tool with JSON/CSV Export and JavaScript Query Shell.
- 🔧 [asdf-firebase](https://github.com/jthegedus/asdf-firebase) [![GitHub stars](https://img.shields.io/github/stars/jthegedus/asdf-firebase?style=flat)](https://github.com/jthegedus/asdf-firebase/stargazers) - An [asdf-vm](https://asdf-vm.com/) plugin for `firebase-tools`. Manage your Firebase CLI without Node.js or `npm`! Great for `python`, `golang`, `c++` & `java` Firebase projects.

## Other

- 🔧 [FireCMS](https://firecms.co/docs/) - FireCMS is an open source headless CMS and admin panel built by developers for developers. It generates CRUD views based on your configuration.
- 🔧 [Flank](https://github.com/flank/flank/) [![GitHub stars](https://img.shields.io/github/stars/flank/flank/?style=flat)](https://github.com/flank/flank//stargazers) - Massively parallel Android and iOS test runner for Firebase Test Lab.
- 🔌 [Firestore Query Browser](https://firestore-query-browser.firebaseapp.com) - WebApp to Query, (Batch-)Edit & Export documents with app & user switching.
- 🔌 [FireDrill](https://github.com/scottlepp/fire-drill) [![GitHub stars](https://img.shields.io/github/stars/scottlepp/fire-drill?style=flat)](https://github.com/scottlepp/fire-drill/stargazers) - Find, Edit, Add, Remove, Import, Export, and Report on your Firebase data.
- 💡 [Unity Solutions](https://github.com/FirebaseExtended/unity-solutions) [![GitHub stars](https://img.shields.io/github/stars/FirebaseExtended/unity-solutions?style=flat)](https://github.com/FirebaseExtended/unity-solutions/stargazers) - Use Firebase tools to incorporate common features into your games.
- 🔌 [Firebase AIR Native Extension](https://github.com/myflashlab/Firebase-ANE) [![GitHub stars](https://img.shields.io/github/stars/myflashlab/Firebase-ANE?style=flat)](https://github.com/myflashlab/Firebase-ANE/stargazers) - Firebase ANE collection give you access to the Google Firebase project in your AdobeAir projects supported on both Android and iOS with 100% identical ActionScript API.
- 🔌 [QtFirebase](https://github.com/Larpon/QtFirebase) [![GitHub stars](https://img.shields.io/github/stars/Larpon/QtFirebase?style=flat)](https://github.com/Larpon/QtFirebase/stargazers) - An effort to bring Google's Firebase C++ API to Qt + QML.
- 📝 [StackBlitz to Firebase Hosting Deployments](https://medium.com/@ericsimons/announcing-split-second-static-deploys-for-firebase-7440d8e84879) - StackBlitz (online code editor) to Firebase Hosting static deployments.
- 🔧 [Flamelink](https://flamelink.io/) - CMS for Firebase. Supports Firestore, RealtimeDatabase & Storage.
- 📹 [Firebase Summit 2018](https://www.youtube.com/watch?v=lN0VXVXsj9k&list=PLl-K7zZEsYLnqdlmz7iFe9Lb6cRU3Nv4R) - All Firebase Summit 2018 talks.
- 📹 [Firebase @ Google Cloud Next '18](https://www.youtube.com/watch?v=OPj26MY16F8&list=PLl-K7zZEsYLmYx3MkJRIUPH_JVFHLTlwL) - All Firebase talks @ Google Cloud Next 2018.
- 📹 [Firebase @ Google IO '18](https://www.youtube.com/watch?v=e-8fiv-vteQ&list=PLl-K7zZEsYLn1omgx_VUhCDFsQMA7PRDd) - All Firebase talks @ Google IO 2018.
- 📹 [#AskFirebase YouTube Playlist](https://www.youtube.com/watch?v=TSzhzR4wzSE&list=PLl-K7zZEsYLkkCFs6T9mlqG8v6NCs38pA) - Official #AskFirebase playlist on YouTube.
- 📝 [State of Firebase (mid 2019)](https://codeburst.io/the-state-of-firebase-mid-2019-2b002c458d70) - Cloud Next & Google I/O 2019 updates!
- 📹 [Firebase @ Google IO '19](https://www.youtube.com/playlist?list=PLl-K7zZEsYLlo2L4rfPds-fFLEtOWheoO) - All Firebase talks @ Google IO 2019.
- 📹 [Firebase Summit 2019](https://www.youtube.com/watch?v=YKZ6rP4kwV8&list=PLl-K7zZEsYLk2OolaVXVyYrFErctrZXSX) - All Firebase talks @ the Firebase Summit 2019.
- 📹 [Firebase Live 2020](https://www.youtube.com/playlist?list=PLl-K7zZEsYLnw0-bXz2f9zo6745VQ_2ep) - Firebase Live is a web series for app developers consisting of talks, tips, and technical tutorials aimed at increasing their productivity, knowledge, and collaboration.
- 📹 [Firebase Summit 2020](https://goo.gle/firebasesummit2020) - All Firebase talks @ the Firebase Summit 2020.
- 🔧 [Dynaboard](https://dynaboard.com) - Generate low-code web apps from Firebase using AI.

<!-- END content -->

## Follow

### Official

- 📹 [Firebase YouTube](https://www.youtube.com/user/Firebase)
- 📝 [Firebase Blog](https://firebase.googleblog.com/)
- 🐦 [@firebase](https://twitter.com/firebase)
- 👤 [Firebase Facebook](https://www.facebook.com/Firebase)
- 🔊 [The Firebase Podcast](https://podcasts.google.com/feed/aHR0cDovL2ZpcmViYXNlcG9kY2FzdC5nb29nbGVkZXZlbG9wZXJzLmxpYnN5bnByby5jb20vcnNz) - This is the place where we dive deep into Firebase products and learn new tips and tricks along the way.

### Community

- :fire: [Firebase Developers Discord](https://discord.gg/BN2cgc3) - an open community dedicated to Firebase and its services, where you can to socialize and help other web and app developers from around the world.
- 📹 [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) - A YouTube channel by Jeff Delaney, a Google Firebase expert and creator of the famous "X in 100 Seconds" videos.
- 📹 ru [@firebase_ru - Telegram friendly chat](https://t.me/firebase_ru)

Who else should we be following!?

## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/jthegedus/awesome-firebase/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/jthegedus/awesome-firebase/graphs/contributors?style=flat)](https://github.com/jthegedus/awesome-firebase/graphs/contributors/stargazers)!
