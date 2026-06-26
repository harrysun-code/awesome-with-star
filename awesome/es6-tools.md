# ES6 Tools

[![GitHub stars](https://img.shields.io/github/stars/addyosmani/es6-tools?style=flat)](https://github.com/addyosmani/es6-tools/stargazers)

# <img src="http://i.imgur.com/yy1sACZ.png" width="100px"/> ECMAScript 6 Tools [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

## Transpilers

* [Babel](https://github.com/babel/babel) [![GitHub stars](https://img.shields.io/github/stars/babel/babel?style=flat)](https://github.com/babel/babel/stargazers) - Turn ES6+ code into vanilla ES5 with no runtime
* [Traceur compiler](https://github.com/google/traceur-compiler) [![GitHub stars](https://img.shields.io/github/stars/google/traceur-compiler?style=flat)](https://github.com/google/traceur-compiler/stargazers) - ES6 features > ES5. Includes classes, generators, promises, destructuring patterns, default parameters & more.
* [es6ify](https://github.com/thlorenz/es6ify) [![GitHub stars](https://img.shields.io/github/stars/thlorenz/es6ify?style=flat)](https://github.com/thlorenz/es6ify/stargazers) - Traceur compiler wrapped as a [Browserify](http://browserify.org/) v2 transform
* [babelify](https://github.com/babel/babelify) [![GitHub stars](https://img.shields.io/github/stars/babel/babelify?style=flat)](https://github.com/babel/babelify/stargazers) - Babel transpiler wrapped as a [Browserify](http://browserify.org/) transform
* [es6-transpiler](https://github.com/termi/es6-transpiler) [![GitHub stars](https://img.shields.io/github/stars/termi/es6-transpiler?style=flat)](https://github.com/termi/es6-transpiler/stargazers) - ES6 > ES5. Includes classes, destructuring, default parameters, spread
* Square's [es6-module-transpiler](https://github.com/esnext/es6-module-transpiler) [![GitHub stars](https://img.shields.io/github/stars/esnext/es6-module-transpiler?style=flat)](https://github.com/esnext/es6-module-transpiler/stargazers) - ES6 modules to AMD or CJS
* Facebook's [regenerator](https://github.com/facebook/regenerator) [![GitHub stars](https://img.shields.io/github/stars/facebook/regenerator?style=flat)](https://github.com/facebook/regenerator/stargazers) - transform ES6 yield/generator functions to ES5
* Facebook's [jstransform](https://github.com/facebookarchive/jstransform) [![GitHub stars](https://img.shields.io/github/stars/facebookarchive/jstransform?style=flat)](https://github.com/facebookarchive/jstransform/stargazers) - A simple utility for pluggable JS syntax transforms. Comes with a small set of ES6 -> ES5 transforms
* [defs](https://github.com/olov/defs) [![GitHub stars](https://img.shields.io/github/stars/olov/defs?style=flat)](https://github.com/olov/defs/stargazers) - ES6 block-scoped const and let variables to ES3 vars
* [es6_module_transpiler-rails](https://github.com/DavyJonesLocker/es6_module_transpiler-rails) [![GitHub stars](https://img.shields.io/github/stars/DavyJonesLocker/es6_module_transpiler-rails?style=flat)](https://github.com/DavyJonesLocker/es6_module_transpiler-rails/stargazers) - ES6 Modules in the Rails Asset Pipeline
* [Some Sweet.js macros](https://github.com/jlongster/es6-macros) [![GitHub stars](https://img.shields.io/github/stars/jlongster/es6-macros?style=flat)](https://github.com/jlongster/es6-macros/stargazers) that compile from ES6 to ES5
* Bitovi's [transpile](https://github.com/stealjs/transpile) [![GitHub stars](https://img.shields.io/github/stars/stealjs/transpile?style=flat)](https://github.com/stealjs/transpile/stargazers) - Converts ES6 to AMD, CJS, and StealJS.
* [regexpu](https://github.com/mathiasbynens/regexpu) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/regexpu?style=flat)](https://github.com/mathiasbynens/regexpu/stargazers) — Transform Unicode-aware ES6 regular expressions to ES5
* [Lebab](https://github.com/mohebifar/lebab) [![GitHub stars](https://img.shields.io/github/stars/mohebifar/lebab?style=flat)](https://github.com/mohebifar/lebab/stargazers) - Transformations for ES5 code to ES6 (approximates)

## Build-time transpilation

### Gulp Plugins
* Babel: [gulp-babel](https://github.com/babel/gulp-babel) [![GitHub stars](https://img.shields.io/github/stars/babel/gulp-babel?style=flat)](https://github.com/babel/gulp-babel/stargazers)
* Traceur: [gulp-traceur](https://github.com/sindresorhus/gulp-traceur) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/gulp-traceur?style=flat)](https://github.com/sindresorhus/gulp-traceur/stargazers)
* Regenerator: [gulp-regenerator](https://github.com/sindresorhus/gulp-regenerator) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/gulp-regenerator?style=flat)](https://github.com/sindresorhus/gulp-regenerator/stargazers)
* ES6 Module Transpiler: [gulp-es6-module-transpiler](https://github.com/ryanseddon/gulp-es6-module-transpiler) [![GitHub stars](https://img.shields.io/github/stars/ryanseddon/gulp-es6-module-transpiler?style=flat)](https://github.com/ryanseddon/gulp-es6-module-transpiler/stargazers)
* es6-transpiler: [gulp-es6-transpiler](https://github.com/sindresorhus/gulp-es6-transpiler) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/gulp-es6-transpiler?style=flat)](https://github.com/sindresorhus/gulp-es6-transpiler/stargazers) - ES6 → ES5
* es6-jstransform: [gulp-jstransform](https://github.com/hemanth/gulp-jstransform) [![GitHub stars](https://img.shields.io/github/stars/hemanth/gulp-jstransform?style=flat)](https://github.com/hemanth/gulp-jstransform/stargazers) - ES6 → ES5 using FB's [jstransform](https://github.com/facebook/jstransform) [![GitHub stars](https://img.shields.io/github/stars/facebook/jstransform?style=flat)](https://github.com/facebook/jstransform/stargazers)
* regexpu: [gulp-regexpu](https://github.com/mathiasbynens/gulp-regexpu) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/gulp-regexpu?style=flat)](https://github.com/mathiasbynens/gulp-regexpu/stargazers)
* TypeScript: [gulp-typescript](https://github.com/ivogabe/gulp-typescript) [![GitHub stars](https://img.shields.io/github/stars/ivogabe/gulp-typescript?style=flat)](https://github.com/ivogabe/gulp-typescript/stargazers)

### Grunt Tasks
* Babel: [grunt-babel](https://github.com/babel/grunt-babel) [![GitHub stars](https://img.shields.io/github/stars/babel/grunt-babel?style=flat)](https://github.com/babel/grunt-babel/stargazers) - Turn ES6+ code into vanilla ES5 with no runtime
* Traceur: [grunt-traceur](https://github.com/aaronfrost/grunt-traceur) [![GitHub stars](https://img.shields.io/github/stars/aaronfrost/grunt-traceur?style=flat)](https://github.com/aaronfrost/grunt-traceur/stargazers) ES6 > ES5 transpilation, [grunt-traceur-build](https://github.com/tarruda/grunt-traceur-build) [![GitHub stars](https://img.shields.io/github/stars/tarruda/grunt-traceur-build?style=flat)](https://github.com/tarruda/grunt-traceur-build/stargazers)
* ES6 Module Transpiler: [grunt-es6-module-transpiler](https://github.com/joefiorini/grunt-es6-module-transpiler) [![GitHub stars](https://img.shields.io/github/stars/joefiorini/grunt-es6-module-transpiler?style=flat)](https://github.com/joefiorini/grunt-es6-module-transpiler/stargazers)
* Regenerator: [grunt-regenerator](https://github.com/sindresorhus/grunt-regenerator) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/grunt-regenerator?style=flat)](https://github.com/sindresorhus/grunt-regenerator/stargazers) - ES6 generator functions to ES5
* [grunt-microlib](https://github.com/thomasboyt/grunt-microlib) [![GitHub stars](https://img.shields.io/github/stars/thomasboyt/grunt-microlib?style=flat)](https://github.com/thomasboyt/grunt-microlib/stargazers) - tools for libs using ES6 module transpiler (sample [Gruntfile](https://github.com/jakearchibald/es6-promise/blob/c3336087fffc52e66cf5398e5b56b23a291080fc/Gruntfile.js) [![GitHub stars](https://img.shields.io/github/stars/jakearchibald/es6-promise/blob/c3336087fffc52e66cf5398e5b56b23a291080fc/Gruntfile.js?style=flat)](https://github.com/jakearchibald/es6-promise/blob/c3336087fffc52e66cf5398e5b56b23a291080fc/Gruntfile.js/stargazers))
* [grunt-defs](https://github.com/EE/grunt-defs) [![GitHub stars](https://img.shields.io/github/stars/EE/grunt-defs?style=flat)](https://github.com/EE/grunt-defs/stargazers) - ES6 block scoped const and let variables, to ES3
* es6-transpiler: [grunt-es6-transpiler](https://github.com/sindresorhus/grunt-es6-transpiler) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/grunt-es6-transpiler?style=flat)](https://github.com/sindresorhus/grunt-es6-transpiler/stargazers) - ES6 → ES5
* TypeScript: [grunt-ts](https://github.com/TypeStrong/grunt-ts) [![GitHub stars](https://img.shields.io/github/stars/TypeStrong/grunt-ts?style=flat)](https://github.com/TypeStrong/grunt-ts/stargazers) - ES6+ > ES5/ES3 transpilation

### Broccoli Plugins
* Babel: [broccoli-babel-transpiler](https://github.com/babel/broccoli-babel-transpiler) [![GitHub stars](https://img.shields.io/github/stars/babel/broccoli-babel-transpiler?style=flat)](https://github.com/babel/broccoli-babel-transpiler/stargazers)
* Traceur: [broccoli-traceur](https://github.com/sindresorhus/broccoli-traceur) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/broccoli-traceur?style=flat)](https://github.com/sindresorhus/broccoli-traceur/stargazers)
* Regenerator: [broccoli-regenerator](https://github.com/sindresorhus/broccoli-regenerator) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/broccoli-regenerator?style=flat)](https://github.com/sindresorhus/broccoli-regenerator/stargazers)
* ES6 Transpiler: [broccoli-transpiler](https://github.com/sindresorhus/broccoli-es6-transpiler) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/broccoli-es6-transpiler?style=flat)](https://github.com/sindresorhus/broccoli-es6-transpiler/stargazers)
* ES6 Module Transpiler: [broccoli-es6-module-transpiler](https://github.com/mmun/broccoli-es6-module-transpiler) [![GitHub stars](https://img.shields.io/github/stars/mmun/broccoli-es6-module-transpiler?style=flat)](https://github.com/mmun/broccoli-es6-module-transpiler/stargazers)
* ES6 fat arrow transpiler: [broccoli-es6-arrow](https://github.com/hemanth/broccoli-es6-arrow.git) [![GitHub stars](https://img.shields.io/github/stars/hemanth/broccoli-es6-arrow.git?style=flat)](https://github.com/hemanth/broccoli-es6-arrow.git/stargazers)
* TypeScript: [broccoli-tsc](https://github.com/ngParty/broccoli-tsc) [![GitHub stars](https://img.shields.io/github/stars/ngParty/broccoli-tsc?style=flat)](https://github.com/ngParty/broccoli-tsc/stargazers)

### Brunch Plugins
* Babel: [babel-brunch](https://github.com/babel/babel-brunch) [![GitHub stars](https://img.shields.io/github/stars/babel/babel-brunch?style=flat)](https://github.com/babel/babel-brunch/stargazers)
* ES6 Module Transpiler: [es6-module-transpiler-brunch](https://github.com/gcollazo/es6-module-transpiler-brunch) [![GitHub stars](https://img.shields.io/github/stars/gcollazo/es6-module-transpiler-brunch?style=flat)](https://github.com/gcollazo/es6-module-transpiler-brunch/stargazers)
* TypeScript: [typescript-brunch](https://github.com/joshheyse/typescript-brunch) [![GitHub stars](https://img.shields.io/github/stars/joshheyse/typescript-brunch?style=flat)](https://github.com/joshheyse/typescript-brunch/stargazers)

## Webpack plugins
* Babel: [babel-loader](https://github.com/babel/babel-loader) [![GitHub stars](https://img.shields.io/github/stars/babel/babel-loader?style=flat)](https://github.com/babel/babel-loader/stargazers)
* Traceur: [traceur-compiler-loader](https://github.com/gdi2290/traceur-compiler-loader) [![GitHub stars](https://img.shields.io/github/stars/gdi2290/traceur-compiler-loader?style=flat)](https://github.com/gdi2290/traceur-compiler-loader/stargazers)
* TypeScript: [awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader) [![GitHub stars](https://img.shields.io/github/stars/s-panferov/awesome-typescript-loader?style=flat)](https://github.com/s-panferov/awesome-typescript-loader/stargazers)

## Duo plugins
* Babel: [duo-babel](https://github.com/babel/duo-babel) [![GitHub stars](https://img.shields.io/github/stars/babel/duo-babel?style=flat)](https://github.com/babel/duo-babel/stargazers)
* TypeScript: [duo-typescript](https://github.com/frankwallis/duo-typescript) [![GitHub stars](https://img.shields.io/github/stars/frankwallis/duo-typescript?style=flat)](https://github.com/frankwallis/duo-typescript/stargazers)

## Connect plugins
* Babel: [babel-connect](https://github.com/babel/babel-connect) [![GitHub stars](https://img.shields.io/github/stars/babel/babel-connect?style=flat)](https://github.com/babel/babel-connect/stargazers)
* TypeScript: [typescript-middleware](https://github.com/brn/typescript-middleware) [![GitHub stars](https://img.shields.io/github/stars/brn/typescript-middleware?style=flat)](https://github.com/brn/typescript-middleware/stargazers)

## Gobble plugins
* Babel: [gobble-babel](https://github.com/babel/gobble-babel) [![GitHub stars](https://img.shields.io/github/stars/babel/gobble-babel?style=flat)](https://github.com/babel/gobble-babel/stargazers)
* Traceur: [gobble-es6-transpiler](https://github.com/gobblejs/gobble-es6-transpiler) [![GitHub stars](https://img.shields.io/github/stars/gobblejs/gobble-es6-transpiler?style=flat)](https://github.com/gobblejs/gobble-es6-transpiler/stargazers)

## Jade plugins
* Babel: [jade-babel](https://github.com/babel/jade-babel) [![GitHub stars](https://img.shields.io/github/stars/babel/jade-babel?style=flat)](https://github.com/babel/jade-babel/stargazers)
* Traceur: [jade-traceur](https://www.npmjs.com/package/jade-traceur)

## Jest plugins
* Babel: [babel-jest](https://github.com/babel/babel-jest) [![GitHub stars](https://img.shields.io/github/stars/babel/babel-jest?style=flat)](https://github.com/babel/babel-jest/stargazers)

## Karma plugins
* Babel: [karma-babel-preprocessor](https://github.com/babel/karma-babel-preprocessor) [![GitHub stars](https://img.shields.io/github/stars/babel/karma-babel-preprocessor?style=flat)](https://github.com/babel/karma-babel-preprocessor/stargazers)
* Traceur: [karma-traceur-preprocessor](https://github.com/karma-runner/karma-traceur-preprocessor) [![GitHub stars](https://img.shields.io/github/stars/karma-runner/karma-traceur-preprocessor?style=flat)](https://github.com/karma-runner/karma-traceur-preprocessor/stargazers)
* TypeScript: [karma-typescript-preprocessor](https://github.com/sergeyt/karma-typescript-preprocessor) [![GitHub stars](https://img.shields.io/github/stars/sergeyt/karma-typescript-preprocessor?style=flat)](https://github.com/sergeyt/karma-typescript-preprocessor/stargazers)

## Sprockets plugins
* Babel: [sprockets-es6](https://github.com/josh/sprockets-es6) [![GitHub stars](https://img.shields.io/github/stars/josh/sprockets-es6?style=flat)](https://github.com/josh/sprockets-es6/stargazers)
* Traceur: [sprockets-traceur](https://github.com/gunpowderlabs/sprockets-traceur) [![GitHub stars](https://img.shields.io/github/stars/gunpowderlabs/sprockets-traceur?style=flat)](https://github.com/gunpowderlabs/sprockets-traceur/stargazers)
* TypeScript: [typescript-rails](https://github.com/typescript-ruby/typescript-rails) [![GitHub stars](https://img.shields.io/github/stars/typescript-ruby/typescript-rails?style=flat)](https://github.com/typescript-ruby/typescript-rails/stargazers)

## Browser plugins
* [Scratch JS](https://github.com/richgilbank/Scratch-JS) [![GitHub stars](https://img.shields.io/github/stars/richgilbank/Scratch-JS?style=flat)](https://github.com/richgilbank/Scratch-JS/stargazers) - A Chrome/Opera DevTools extension to run ES6 on a page with either Babel or Traceur
* [generator-typescript](https://github.com/mrkev/generator-typescript) [![GitHub stars](https://img.shields.io/github/stars/mrkev/generator-typescript?style=flat)](https://github.com/mrkev/generator-typescript/stargazers) - Yeoman generator for TypeScript apps

## Mocha plugins
* [Mocha Traceur](https://github.com/domenic/mocha-traceur) [![GitHub stars](https://img.shields.io/github/stars/domenic/mocha-traceur?style=flat)](https://github.com/domenic/mocha-traceur/stargazers) - A simple plugin for Mocha to pass JS files through the Traceur compiler

## Module Loaders

* ES6 [Module Loader polyfill](https://github.com/ModuleLoader/es6-module-loader) [![GitHub stars](https://img.shields.io/github/stars/ModuleLoader/es6-module-loader?style=flat)](https://github.com/ModuleLoader/es6-module-loader/stargazers) (compat with latest spec and Traceur)
* [js-loaders](https://github.com/jorendorff/js-loaders) [![GitHub stars](https://img.shields.io/github/stars/jorendorff/js-loaders?style=flat)](https://github.com/jorendorff/js-loaders/stargazers) - Mozilla's spec-compliant loader prototype
* [JSPM](http://jspm.io/) - ES6, AMD, CJS module loading/package management
* [Babel Module Loader](https://github.com/babel/babel-loader) [![GitHub stars](https://img.shields.io/github/stars/babel/babel-loader?style=flat)](https://github.com/babel/babel-loader/stargazers)
* [beck.js](https://github.com/unscriptable/beck) [![GitHub stars](https://img.shields.io/github/stars/unscriptable/beck?style=flat)](https://github.com/unscriptable/beck/stargazers) - toolkit for ES6 Module Loader pipelines, shim for legacy environments

## Boilerplates
* [es6-boilerplate](https://github.com/davidjnelson/es6-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/davidjnelson/es6-boilerplate?style=flat)](https://github.com/davidjnelson/es6-boilerplate/stargazers) - Tooling to allow the community to use es6 now via traceur in conjunction with amd and browser global modules, with source maps, concatenation, minification, compression, and unit testing in real browsers.
* [es6-jspm-gulp-boilerplate](https://github.com/alexweber/es6-jspm-gulp-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/alexweber/es6-jspm-gulp-boilerplate?style=flat)](https://github.com/alexweber/es6-jspm-gulp-boilerplate/stargazers) - Tooling to allow the community to use es6 now via babel in conjunction jspm, with source maps, concatenation, minification, compression, and unit testing in real browsers using es6.

## Code generation

* [generator-node-esnext](https://github.com/briandipalma/generator-node-esnext) [![GitHub stars](https://img.shields.io/github/stars/briandipalma/generator-node-esnext?style=flat)](https://github.com/briandipalma/generator-node-esnext/stargazers) - Yeoman generator for Traceur apps
* [generator-es6-babel](https://github.com/HenriqueLimas/generator-es6-babel) [![GitHub stars](https://img.shields.io/github/stars/HenriqueLimas/generator-es6-babel?style=flat)](https://github.com/HenriqueLimas/generator-es6-babel/stargazers) - Yeoman generator for Babel apps
* [generator-gulp-babelify](https://github.com/HenriqueLimas/generator-gulp-babelify) [![GitHub stars](https://img.shields.io/github/stars/HenriqueLimas/generator-gulp-babelify?style=flat)](https://github.com/HenriqueLimas/generator-gulp-babelify/stargazers) - Yeoman generator for [Babel](https://babeljs.io/), [Browserify](http://browserify.org/) and [Gulp](http://gulpjs.com/)
* [grunt-init-es6](https://www.npmjs.com/package/grunt-init-es6) - scaffold node modules with unit tests, authored in ES6
* [Loom generators with ES6 ember modules](https://github.com/ryanflorence/loom-generators-ember) [![GitHub stars](https://img.shields.io/github/stars/ryanflorence/loom-generators-ember?style=flat)](https://github.com/ryanflorence/loom-generators-ember/stargazers)
* Brunch [plugin](https://www.npmjs.com/package/es6-module-transpiler-brunch) for ES6 module transpilation

## Polyfills

* [core-js](https://github.com/zloirock/core-js) [![GitHub stars](https://img.shields.io/github/stars/zloirock/core-js?style=flat)](https://github.com/zloirock/core-js/stargazers) - Modular and compact polyfills for ES6 including Symbols, Map, Set, Iterators, Promises, setImmediate, Array generics, etc. The standard library used by [Babel](https://github.com/babel/babel) [![GitHub stars](https://img.shields.io/github/stars/babel/babel?style=flat)](https://github.com/babel/babel/stargazers).
* [es6-shim](https://github.com/paulmillr/es6-shim) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/es6-shim?style=flat)](https://github.com/paulmillr/es6-shim/stargazers) - almost all new ES6 methods — from Map, Set, String, Array, Object, Object.is and more.
* [WeakMap, Map, Set, HashMap - ES6 Collections](https://github.com/Benvie/harmony-collections) [![GitHub stars](https://img.shields.io/github/stars/Benvie/harmony-collections?style=flat)](https://github.com/Benvie/harmony-collections/stargazers)
* Polymer's [WeakMap shim](https://github.com/Polymer/WeakMap) [![GitHub stars](https://img.shields.io/github/stars/Polymer/WeakMap?style=flat)](https://github.com/Polymer/WeakMap/stargazers)
* [`String.prototype.startsWith`](https://github.com/mathiasbynens/String.prototype.startsWith) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.prototype.startsWith?style=flat)](https://github.com/mathiasbynens/String.prototype.startsWith/stargazers)
* [`String.prototype.endsWith`](https://github.com/mathiasbynens/String.prototype.endsWith) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.prototype.endsWith?style=flat)](https://github.com/mathiasbynens/String.prototype.endsWith/stargazers)
* [`String.prototype.at`](https://github.com/mathiasbynens/String.prototype.at) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.prototype.at?style=flat)](https://github.com/mathiasbynens/String.prototype.at/stargazers)
* [`String.prototype.repeat`](https://github.com/mathiasbynens/String.prototype.repeat) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.prototype.repeat?style=flat)](https://github.com/mathiasbynens/String.prototype.repeat/stargazers)
* [`String.prototype.includes`](https://github.com/mathiasbynens/String.prototype.includes) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.prototype.includes?style=flat)](https://github.com/mathiasbynens/String.prototype.includes/stargazers)
* [`String.prototype.codePointAt`](https://github.com/mathiasbynens/String.prototype.codePointAt) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.prototype.codePointAt?style=flat)](https://github.com/mathiasbynens/String.prototype.codePointAt/stargazers)
* [`String.fromCodePoint`](https://github.com/mathiasbynens/String.fromCodePoint) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/String.fromCodePoint?style=flat)](https://github.com/mathiasbynens/String.fromCodePoint/stargazers)
* [`Array.prototype.find`](https://github.com/paulmillr/Array.prototype.find) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/Array.prototype.find?style=flat)](https://github.com/paulmillr/Array.prototype.find/stargazers)
* [`Array.prototype.findIndex`](https://github.com/paulmillr/Array.prototype.findIndex) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/Array.prototype.findIndex?style=flat)](https://github.com/paulmillr/Array.prototype.findIndex/stargazers)
* [`Array.from`](https://github.com/mathiasbynens/Array.from) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/Array.from?style=flat)](https://github.com/mathiasbynens/Array.from/stargazers)
* [`Array.of`](https://github.com/mathiasbynens/Array.of) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/Array.of?style=flat)](https://github.com/mathiasbynens/Array.of/stargazers)
* [`Object.assign`](https://github.com/sindresorhus/object-assign) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/object-assign?style=flat)](https://github.com/sindresorhus/object-assign/stargazers)
* [`Number.isFinite`](https://github.com/sindresorhus/is-finite) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/is-finite?style=flat)](https://github.com/sindresorhus/is-finite/stargazers)
* [`Math.sign`](https://github.com/sindresorhus/math-sign) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/math-sign?style=flat)](https://github.com/sindresorhus/math-sign/stargazers)
* [`RegExp.prototype.match`](https://github.com/mathiasbynens/RegExp.prototype.match) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/RegExp.prototype.match?style=flat)](https://github.com/mathiasbynens/RegExp.prototype.match/stargazers)
* [`RegExp.prototype.search`](https://github.com/mathiasbynens/RegExp.prototype.search) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/RegExp.prototype.search?style=flat)](https://github.com/mathiasbynens/RegExp.prototype.search/stargazers)
* [es6-promise](https://github.com/jakearchibald/es6-promise) [![GitHub stars](https://img.shields.io/github/stars/jakearchibald/es6-promise?style=flat)](https://github.com/jakearchibald/es6-promise/stargazers) - polyfill for Promises matching the ES6 API
* [ES6 Map Shim](https://github.com/eriwen/es6-map-shim) [![GitHub stars](https://img.shields.io/github/stars/eriwen/es6-map-shim?style=flat)](https://github.com/eriwen/es6-map-shim/stargazers) - destructive shim that follows the latest specification as closely as possible.
* [`Function.create`](https://github.com/walling/Function.create.js) [![GitHub stars](https://img.shields.io/github/stars/walling/Function.create.js?style=flat)](https://github.com/walling/Function.create.js/stargazers)
* [ES6 shim](https://github.com/inexorabletash/polyfill/blob/master/es6.md) [![GitHub stars](https://img.shields.io/github/stars/inexorabletash/polyfill/blob/master/es6.md?style=flat)](https://github.com/inexorabletash/polyfill/blob/master/es6.md/stargazers)
* [ES6 Symbol polyfill](https://github.com/medikoo/es6-symbol) [![GitHub stars](https://img.shields.io/github/stars/medikoo/es6-symbol?style=flat)](https://github.com/medikoo/es6-symbol/stargazers)
* [ES6 Map, Set, WeakMap](https://github.com/EliSnow/Blitz-Collections) [![GitHub stars](https://img.shields.io/github/stars/EliSnow/Blitz-Collections?style=flat)](https://github.com/EliSnow/Blitz-Collections/stargazers)
* [harmony-reflect](https://github.com/tvcutsem/harmony-reflect) [![GitHub stars](https://img.shields.io/github/stars/tvcutsem/harmony-reflect?style=flat)](https://github.com/tvcutsem/harmony-reflect/stargazers) - ES6 [reflection module](http://wiki.ecmascript.org/doku.php?id=harmony:reflect_api) (contains the [Proxy API](http://soft.vub.ac.be/~tvcutsem/proxies/))
* [ES5 based shims in pure CJS style](https://gist.github.com/medikoo/102b7d0e697627133788#list-of-ecmascript-6-shims) -  Array, Object, Number, Math and String functions/methods, plus Map, Set, Symbol and WeakMap objects

## Editors

* ES6 syntax highlighting for [Sublime Text and TextMate](https://github.com/Benvie/JavaScriptNext.tmLanguage) [![GitHub stars](https://img.shields.io/github/stars/Benvie/JavaScriptNext.tmLanguage?style=flat)](https://github.com/Benvie/JavaScriptNext.tmLanguage/stargazers)
* ES6 syntax support in [WebStorm](https://www.jetbrains.com/webstorm/) and [PhpStorm](https://www.jetbrains.com/phpstorm/), compilation to ES5 with [file watchers or task runners](http://blog.jetbrains.com/webstorm/2015/05/ecmascript-6-in-webstorm-transpiling/)
* DocPad [plugin](https://github.com/pflannery/docpad-plugin-traceur) [![GitHub stars](https://img.shields.io/github/stars/pflannery/docpad-plugin-traceur?style=flat)](https://github.com/pflannery/docpad-plugin-traceur/stargazers) for Traceur
* Grammar and transpilation [package](https://github.com/gandm/language-babel) [![GitHub stars](https://img.shields.io/github/stars/gandm/language-babel?style=flat)](https://github.com/gandm/language-babel/stargazers)  for [Atom](https://atom.io/)
* Learn ES6 transpilation options in Webstorm [Read Blog Post](http://blog.jetbrains.com/webstorm/2015/05/ecmascript-6-in-webstorm-transpiling/)

## Parsers

* [Esprima](http://esprima.org) - JavaScript parser supporting ES6, parses to [ESTree AST format](https://github.com/estree/estree) [![GitHub stars](https://img.shields.io/github/stars/estree/estree?style=flat)](https://github.com/estree/estree/stargazers)
* [Acorn](https://github.com/ternjs/acorn) [![GitHub stars](https://img.shields.io/github/stars/ternjs/acorn?style=flat)](https://github.com/ternjs/acorn/stargazers) - A small, fast, JavaScript-based JavaScript parser with ES6 support, parses to [SpiderMonkey AST](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API) format.
* [esparse](https://github.com/zenparsing/esparse) [![GitHub stars](https://img.shields.io/github/stars/zenparsing/esparse?style=flat)](https://github.com/zenparsing/esparse/stargazers) - ES6 parser written in ES6.
* [Traceur compiler](https://github.com/google/traceur-compiler) [![GitHub stars](https://img.shields.io/github/stars/google/traceur-compiler?style=flat)](https://github.com/google/traceur-compiler/stargazers) also has built-in parser available under `traceur.syntax.Parser`.

## Other

* [ES.next showcase](https://github.com/sindresorhus/esnext-showcase) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/esnext-showcase?style=flat)](https://github.com/sindresorhus/esnext-showcase/stargazers) - real-world usage examples of ES6 features
* [looper](https://github.com/wycats/looper) [![GitHub stars](https://img.shields.io/github/stars/wycats/looper?style=flat)](https://github.com/wycats/looper/stargazers) - static analysis tools for ES6
* [es6-module-packager](https://www.npmjs.com/package/es6-module-packager)
* [es-dependency-graph](https://github.com/yahoo/es-dependency-graph) [![GitHub stars](https://img.shields.io/github/stars/yahoo/es-dependency-graph?style=flat)](https://github.com/yahoo/es-dependency-graph/stargazers) and [grunt-es-dependency-graph](https://github.com/yahoo/grunt-es-dependency-graph) [![GitHub stars](https://img.shields.io/github/stars/yahoo/grunt-es-dependency-graph?style=flat)](https://github.com/yahoo/grunt-es-dependency-graph/stargazers) - Generate a list of imports and exports from ES6 module files, useful for preloading, bundling, etc.
* [es6-import-validate](https://github.com/sproutsocial/es6-import-validate) [![GitHub stars](https://img.shields.io/github/stars/sproutsocial/es6-import-validate?style=flat)](https://github.com/sproutsocial/es6-import-validate/stargazers) and [grunt-es6-import-validate](https://github.com/sproutsocial/grunt-es6-import-validate) [![GitHub stars](https://img.shields.io/github/stars/sproutsocial/grunt-es6-import-validate?style=flat)](https://github.com/sproutsocial/grunt-es6-import-validate/stargazers) - validate matching named/default import statements in ES6 modules.
* [let-er](https://github.com/getify/let-er) [![GitHub stars](https://img.shields.io/github/stars/getify/let-er?style=flat)](https://github.com/getify/let-er/stargazers) - transpiles [let-block block-scoping](http://wiki.ecmascript.org/doku.php?id=proposals:block_expressions#let_statement) (not accepted into ES6) into either ES3 or ES6
* [Recast](https://github.com/benjamn/recast) [![GitHub stars](https://img.shields.io/github/stars/benjamn/recast?style=flat)](https://github.com/benjamn/recast/stargazers) - Esprima-based JavaScript syntax tree transformer, conservative pretty-printer, and automatic source map generator. Used by several of the transpilers listed above, including [regenerator](https://github.com/facebook/regenerator) [![GitHub stars](https://img.shields.io/github/stars/facebook/regenerator?style=flat)](https://github.com/facebook/regenerator/stargazers) and [es6-arrow-function](https://github.com/esnext/es6-arrow-function) [![GitHub stars](https://img.shields.io/github/stars/esnext/es6-arrow-function?style=flat)](https://github.com/esnext/es6-arrow-function/stargazers).
* [Paws on ES6](https://github.com/hemanth/paws-on-es6) [![GitHub stars](https://img.shields.io/github/stars/hemanth/paws-on-es6?style=flat)](https://github.com/hemanth/paws-on-es6/stargazers) -  Minimalist examples of ES6 functionalities.
* [ES6 on node](http://h3manth.com/new/blog/2013/es6-on-nodejs/) - How to use ES6 features in node.js.
* [es6-translate](https://github.com/calvinmetcalf/es6-translate) [![GitHub stars](https://img.shields.io/github/stars/calvinmetcalf/es6-translate?style=flat)](https://github.com/calvinmetcalf/es6-translate/stargazers) - Uses the ES6 loader hooks to load (node flavored) commonjs packages in ES6.
* [Isparta](https://github.com/douglasduteil/isparta) [![GitHub stars](https://img.shields.io/github/stars/douglasduteil/isparta?style=flat)](https://github.com/douglasduteil/isparta/stargazers)
* [babel-node](https://babeljs.io/docs/usage/cli/#babel-node) - Run node cli with ES6 transpiling using Babel.
* [ES6 Lab setup](https://github.com/hemanth/es6-lab-setup) [![GitHub stars](https://img.shields.io/github/stars/hemanth/es6-lab-setup?style=flat)](https://github.com/hemanth/es6-lab-setup/stargazers) - A simple setup for transpiling ES6 to ES5 using `Babel` or `traceur` with `gulp` and `jasmine` support.
* [TypeScript](http://www.typescriptlang.org/) - A superset of ECMAScript with strict typing that aims to align with ES6
* [Rollup](http://rollupjs.org/) - Rollup is a next-generation JavaScript module bundler. Author your app or library using ES2015 modules, then efficiently bundle them up into a single file for use in browsers and Node.js
