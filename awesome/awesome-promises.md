# Promises

[![GitHub stars](https://img.shields.io/github/stars/wbinnssmith/awesome-promises?style=flat)](https://github.com/wbinnssmith/awesome-promises/stargazers)

<a href="https://promisesaplus.com/">
    <img src="https://promisesaplus.com/assets/logo-small.png" alt="Promises/A+ logo" align="right" />
</a>

# Awesome Promises [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of useful resources for JavaScript Promises

Inspired by the [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) list thing. Not to be confused with other awesome promises like "I promise you a million dollars" or "I promise you'll stay fit and never have to go to the gym again".

**Table of Contents**

- [Resources, Blogs, and Books](#resources-blogs-and-books)
- [Promises/A+ Implementations (ES6/ES2015 compatible)](#promisesa-implementations-es6es2015-compatible)
  - [Strict Implementations](#strict-implementations)
  - [Implementations with extras](#implementations-with-extras)
  - [Fallbacks](#fallbacks)
- [Convenience Utilities](#convenience-utilities)

## Resources, Blogs, and Books

### For beginners
* [Promise Cookbook](https://github.com/mattdesl/promise-cookbook) [![GitHub stars](https://img.shields.io/github/stars/mattdesl/promise-cookbook?style=flat)](https://github.com/mattdesl/promise-cookbook/stargazers) - The why, what, and how. "A brief introduction [...] primarily aimed at frontend developers".
* [Promises for Asynchronous Programming](http://exploringjs.com/es6/ch_promises.html) - Chapter from [Exploring ES6](http://exploringjs.com/)
* [You Don't Know JS: Promises](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20&%20performance/ch3.md) [![GitHub stars](https://img.shields.io/github/stars/getify/You-Dont-Know-JS/blob/master/async%20&%20performance/ch3.md?style=flat)](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20&%20performance/ch3.md/stargazers) - Chapter from [You Don't Know JS: Async & Performance](https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance) [![GitHub stars](https://img.shields.io/github/stars/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance?style=flat)](https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance/stargazers)
* [JavaScript Promises: an Introduction](https://developers.google.com/web/fundamentals/getting-started/primers/promises) - Basics of JavaScript's native promise implementation.
* [JavaScript with Promises](http://shop.oreilly.com/product/0636920032151.do) - from O'Reilly. Short and to-the-point. Uses native and bluebird.
* [Promise it won't hurt](https://github.com/stevekane/promise-it-wont-hurt) [![GitHub stars](https://img.shields.io/github/stars/stevekane/promise-it-wont-hurt?style=flat)](https://github.com/stevekane/promise-it-wont-hurt/stargazers) - An interactive [nodeschool](https://nodeschool.io/) workshop
* [ES6 Kata Promises](http://es6katas.org/) - Promises Katas : [Basics](http://tddbin.com/#?kata=es6/language/promise/basics)
* [ES6 Promises in Depth](https://ponyfoo.com/articles/es6-promises-in-depth)
* [An Incremental Tutorial on Promises](http://www.sohamkamani.com/blog/2016/08/28/incremenal-tutorial-to-promises/) - An FAQ styled tutorial for beginners.

### Deep Dive
* [Promise Fun](https://github.com/sindresorhus/promise-fun) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/promise-fun?style=flat)](https://github.com/sindresorhus/promise-fun/stargazers) - @sindresorhus's notes, patterns, and solutions to common Promise problems
* [You're Missing the Point of Promises](https://blog.domenic.me/youre-missing-the-point-of-promises/) - Promises are much more than callback aggregation, and that jQuery's implementation (prior to 3.0) isn't enough.
* [We have a problem with promises](https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html) - "Many of us are using promises without really understanding them."
* [Promise anti-patterns](https://github.com/petkaantonov/bluebird/wiki/Promise-anti-patterns) [![GitHub stars](https://img.shields.io/github/stars/petkaantonov/bluebird/wiki/Promise-anti-patterns?style=flat)](https://github.com/petkaantonov/bluebird/wiki/Promise-anti-patterns/stargazers) - Common misuses and how to avoid them.
* [Promise anti-patterns (2)](http://taoofcode.net/promise-anti-patterns/) - Another set of promises anti-patterns
* [Promise Ponderings, (Anti-)Patterns, and Apologies](https://sdgluck.github.io/2015/08/24/promise-ponderings-patterns-apologies/) - Promise behaviour demonstrated and explained by common questions and their answers.
* [Javascript Promises...In Wicked Detail](http://www.mattgreer.org/articles/promises-in-wicked-detail/) - Recreate the promise implementation
* [Writing Promise-Using Specifications](https://www.w3.org/2001/tag/doc/promises-guide) - "This document gives guidance on how to write specifications that create, accept, or manipulate promises"
* [Async functions - making promises friendly](https://developers.google.com/web/fundamentals/getting-started/primers/async-functions)

### References
* [Promises/A+ specification](https://promisesaplus.com/)
* [caniuse promises](http://caniuse.com/#feat=promises)
* [Fates and States](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md) [![GitHub stars](https://img.shields.io/github/stars/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md?style=flat)](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md/stargazers) - Quick definitions of possible states.
* [Promisees](https://bevacqua.github.io/promisees/) - Promise visualization playground for the adventurous.

## Promises/A+ Implementations (ES6/ES2015 compatible)

### Strict Implementations
These implement no more or less than the es6 spec. They make great polyfills and are exceptionally compatible with native promises.

* [pinkie](https://github.com/floatdrop/pinkie) [![GitHub stars](https://img.shields.io/github/stars/floatdrop/pinkie?style=flat)](https://github.com/floatdrop/pinkie/stargazers) - Ponyfill. Node-oriented, but [browserifyable](https://github.com/substack/node-browserify) [![GitHub stars](https://img.shields.io/github/stars/substack/node-browserify?style=flat)](https://github.com/substack/node-browserify/stargazers). *Extremely* small implementation.
* [native-promise-only](https://github.com/getify/native-promise-only) [![GitHub stars](https://img.shields.io/github/stars/getify/native-promise-only?style=flat)](https://github.com/getify/native-promise-only/stargazers) - Polyfill. Browser and node-compatible.
* [es6-promise](https://github.com/stefanpenner/es6-promise) [![GitHub stars](https://img.shields.io/github/stars/stefanpenner/es6-promise?style=flat)](https://github.com/stefanpenner/es6-promise/stargazers) - Opt-in polyfill. A strict-spec subset of rsvp.js.
* [lie](https://github.com/calvinmetcalf/lie) [![GitHub stars](https://img.shields.io/github/stars/calvinmetcalf/lie?style=flat)](https://github.com/calvinmetcalf/lie/stargazers) - Small, browserifyable with an opt-in polyfill.

### Implementations with extras
All of these provide more features than the language yet remain compatible. Node + Browsers for all.

* [bluebird](https://github.com/petkaantonov/bluebird) [![GitHub stars](https://img.shields.io/github/stars/petkaantonov/bluebird?style=flat)](https://github.com/petkaantonov/bluebird/stargazers) - Fully featured, extremely performant. Long stack traces & generator/coroutine support.
* [creed](https://github.com/briancavalier/creed) [![GitHub stars](https://img.shields.io/github/stars/briancavalier/creed?style=flat)](https://github.com/briancavalier/creed/stargazers) - Hyper performant & full featured like Bluebird, but FP-oriented. Coroutines, generators, promises, ES2015 iterables, & fantasy-land spec.
* [rsvp.js](https://github.com/tildeio/rsvp.js/) [![GitHub stars](https://img.shields.io/github/stars/tildeio/rsvp.js/?style=flat)](https://github.com/tildeio/rsvp.js//stargazers) - Lightweight with a few extras. Compatible down to IE6!
* [Q](https://github.com/kriskowal/q) [![GitHub stars](https://img.shields.io/github/stars/kriskowal/q?style=flat)](https://github.com/kriskowal/q/stargazers) - One of the original implementations. Long stack traces and other goodies.
* [then/promise](https://github.com/then/promise) [![GitHub stars](https://img.shields.io/github/stars/then/promise?style=flat)](https://github.com/then/promise/stargazers) - Small with `nodeify`, `denodify` and `done()` additions.
* [when.js](https://github.com/cujojs/when) [![GitHub stars](https://img.shields.io/github/stars/cujojs/when?style=flat)](https://github.com/cujojs/when/stargazers) - Packed with control flow, functional, and utility methods.


### Fallbacks
* [native-or-bluebird](https://www.npmjs.com/package/native-or-bluebird) - Helps transition to completely native.
* [pinkie-promise](https://github.com/floatdrop/pinkie-promise) [![GitHub stars](https://img.shields.io/github/stars/floatdrop/pinkie-promise?style=flat)](https://github.com/floatdrop/pinkie-promise/stargazers) - Use native, or fall back to `pinkie`. Great for node library authors.
* [any-promise](https://github.com/kevinbeaty/any-promise) [![GitHub stars](https://img.shields.io/github/stars/kevinbeaty/any-promise?style=flat)](https://github.com/kevinbeaty/any-promise/stargazers) - Loads the first available implementation. Safe for browserify.

## Convenience Utilities
Native and strictly spec-compliant promises are awesome for compatibility, future-proofness, library authors, and browsers. However, libraries like bluebird patch goodies onto the `Promise` constructor and prototype. Solution? tiny modules of course!

### sindresorhus's many Promise utilities ([see notes](https://github.com/sindresorhus/promise-fun) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/promise-fun?style=flat)](https://github.com/sindresorhus/promise-fun/stargazers))
* [delay](https://github.com/sindresorhus/delay) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/delay?style=flat)](https://github.com/sindresorhus/delay/stargazers) - Delay a promise a specified amount of time.
* [pify](https://github.com/sindresorhus/pify) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/pify?style=flat)](https://github.com/sindresorhus/pify/stargazers) - Promisify ("denodify") a callback-style function.
* [loud-rejection](https://github.com/sindresorhus/loud-rejection) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/loud-rejection?style=flat)](https://github.com/sindresorhus/loud-rejection/stargazers) - Make unhandled promise rejections fail loudly instead of the default silent fail.
* [hard-rejection](https://github.com/sindresorhus/hard-rejection) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/hard-rejection?style=flat)](https://github.com/sindresorhus/hard-rejection/stargazers) - Make unhandled promise rejections fail hard right away instead of the default silent fail
* [p-queue](https://github.com/sindresorhus/p-queue) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-queue?style=flat)](https://github.com/sindresorhus/p-queue/stargazers) - Promise queue with concurrency control
* [p-break](https://github.com/sindresorhus/p-break) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-break?style=flat)](https://github.com/sindresorhus/p-break/stargazers) - Break out of a promise chain
* [p-lazy](https://github.com/sindresorhus/p-lazy) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-lazy?style=flat)](https://github.com/sindresorhus/p-lazy/stargazers) - Create a lazy promise that defers execution until `.then()` or `.catch()` is called
* [p-defer](https://github.com/sindresorhus/p-defer) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-defer?style=flat)](https://github.com/sindresorhus/p-defer/stargazers) - Create a deferred promise
* [p-if](https://github.com/sindresorhus/p-if) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-if?style=flat)](https://github.com/sindresorhus/p-if/stargazers) - Conditional promise chains
* [p-tap](https://github.com/sindresorhus/p-tap) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-tap?style=flat)](https://github.com/sindresorhus/p-tap/stargazers) - Tap into a promise chain without affecting its value or state
* [p-map](https://github.com/sindresorhus/p-map) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-map?style=flat)](https://github.com/sindresorhus/p-map/stargazers) - Map over promises concurrently
* [p-all](https://github.com/sindresorhus/p-all) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-all?style=flat)](https://github.com/sindresorhus/p-all/stargazers) - Run promise-returning & async functions concurrently with optional limited concurrency
* [p-limit](https://github.com/sindresorhus/p-limit) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-limit?style=flat)](https://github.com/sindresorhus/p-limit/stargazers) - Run multiple promise-returning & async functions with limited concurrency
* [p-times](https://github.com/sindresorhus/p-times) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-times?style=flat)](https://github.com/sindresorhus/p-times/stargazers) - Run promise-returning & async functions a specific number of times concurrently
* [p-catch-if](https://github.com/sindresorhus/p-catch-if) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-catch-if?style=flat)](https://github.com/sindresorhus/p-catch-if/stargazers) - Conditional promise catch handler
* [p-time](https://github.com/sindresorhus/p-time) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-time?style=flat)](https://github.com/sindresorhus/p-time/stargazers) - Measure the time a promise takes to resolve
* [p-log](https://github.com/sindresorhus/p-log) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-log?style=flat)](https://github.com/sindresorhus/p-log/stargazers) - Log the value/error of a promise
* [p-filter](https://github.com/sindresorhus/p-filter) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-filter?style=flat)](https://github.com/sindresorhus/p-filter/stargazers) - Filter promises concurrently
* [p-settle](https://github.com/sindresorhus/p-settle) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-settle?style=flat)](https://github.com/sindresorhus/p-settle/stargazers) - Settle promises concurrently and get their fulfillment value or rejection reason
* [p-memoize](https://github.com/sindresorhus/p-memoize) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-memoize?style=flat)](https://github.com/sindresorhus/p-memoize/stargazers) - Memoize promise-returning & async functions
* [p-whilst](https://github.com/sindresorhus/p-whilst) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-whilst?style=flat)](https://github.com/sindresorhus/p-whilst/stargazers) - Calls a function repeatedly while a condition returns true and then resolves the promise
* [p-throttle](https://github.com/sindresorhus/p-throttle) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-throttle?style=flat)](https://github.com/sindresorhus/p-throttle/stargazers) - Throttle promise-returning & async functions
* [p-debounce](https://github.com/sindresorhus/p-debounce) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-debounce?style=flat)](https://github.com/sindresorhus/p-debounce/stargazers) - Debounce promise-returning & async functions
* [p-retry](https://github.com/sindresorhus/p-retry) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-retry?style=flat)](https://github.com/sindresorhus/p-retry/stargazers) - Retry a promise-returning or async function
* [p-wait-for](https://github.com/sindresorhus/p-wait-for) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-wait-for?style=flat)](https://github.com/sindresorhus/p-wait-for/stargazers) - Wait for a condition to be true
* [p-timeout](https://github.com/sindresorhus/p-timeout) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-timeout?style=flat)](https://github.com/sindresorhus/p-timeout/stargazers) - Timeout a promise after a specified amount of time
* [p-race](https://github.com/sindresorhus/p-race) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-race?style=flat)](https://github.com/sindresorhus/p-race/stargazers) - A better `Promise.race()`
* [p-try](https://github.com/sindresorhus/p-try) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-try?style=flat)](https://github.com/sindresorhus/p-try/stargazers) - `Promise#try()` ponyfill - Starts a promise chain
* [p-finally](https://github.com/sindresorhus/p-finally) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-finally?style=flat)](https://github.com/sindresorhus/p-finally/stargazers) - `Promise#finally()` ponyfill - Invoked when the promise is settled regardless of outcome
* [p-any](https://github.com/sindresorhus/p-any) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-any?style=flat)](https://github.com/sindresorhus/p-any/stargazers) - Wait for any promise to be fulfilled
* [p-some](https://github.com/sindresorhus/p-some) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-some?style=flat)](https://github.com/sindresorhus/p-some/stargazers) - Wait for a specified number of promises to be fulfilled
* [p-pipe](https://github.com/sindresorhus/p-pipe) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-pipe?style=flat)](https://github.com/sindresorhus/p-pipe/stargazers) - Compose promise-returning & async functions into a reusable pipeline
* [p-each-series](https://github.com/sindresorhus/p-each-series) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-each-series?style=flat)](https://github.com/sindresorhus/p-each-series/stargazers) - Iterate over promises serially
* [p-map-series](https://github.com/sindresorhus/p-map-series) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-map-series?style=flat)](https://github.com/sindresorhus/p-map-series/stargazers) - Map over promises serially
* [p-reduce](https://github.com/sindresorhus/p-reduce) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-reduce?style=flat)](https://github.com/sindresorhus/p-reduce/stargazers) - Reduce a list of values using promises into a promise for a value
* [p-props](https://github.com/sindresorhus/p-props) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/p-props?style=flat)](https://github.com/sindresorhus/p-props/stargazers) - Like `Promise.all()` but for `Map` and `Object`

### Others
* [promise-method](https://github.com/wbinnssmith/promise-method) [![GitHub stars](https://img.shields.io/github/stars/wbinnssmith/promise-method?style=flat)](https://github.com/wbinnssmith/promise-method/stargazers) - Standalone `bluebird.method`. Turn a synchronously-returning method into a promise-returning one.
* [is-promise](https://github.com/then/is-promise) [![GitHub stars](https://img.shields.io/github/stars/then/is-promise?style=flat)](https://github.com/then/is-promise/stargazers) - Determine if something looks like a Promise.
* [sprom](https://github.com/then/sprom) [![GitHub stars](https://img.shields.io/github/stars/then/sprom?style=flat)](https://github.com/then/sprom/stargazers) - Resolve when a stream ends. Optional buffering (be careful with this!)
* [task.js](https://github.com/mozilla/task.js) [![GitHub stars](https://img.shields.io/github/stars/mozilla/task.js?style=flat)](https://github.com/mozilla/task.js/stargazers) - Write async functions in a blocking style using promises and generators. Like `bluebird.coroutine`.
* [co](https://github.com/tj/co) [![GitHub stars](https://img.shields.io/github/stars/tj/co?style=flat)](https://github.com/tj/co/stargazers) - Like `task.js` and `bluebird.coroutine`, but supports thunks too.
* [lie-fs](https://www.npmjs.com/package/lie-fs) - Promise wrappers for Node's FS API.
* [promise-do-until](https://github.com/busterc/promise-do-until) [![GitHub stars](https://img.shields.io/github/stars/busterc/promise-do-until?style=flat)](https://github.com/busterc/promise-do-until/stargazers) - Calls a function repeatedly until a condition returns true and then resolves the promise.
* [promise-do-whilst](https://github.com/busterc/promise-do-whilst) [![GitHub stars](https://img.shields.io/github/stars/busterc/promise-do-whilst?style=flat)](https://github.com/busterc/promise-do-whilst/stargazers) - Calls a function repeatedly while a condition returns true and then resolves the promise.
* [promise-semaphore](https://github.com/samccone/promise-semaphore) [![GitHub stars](https://img.shields.io/github/stars/samccone/promise-semaphore?style=flat)](https://github.com/samccone/promise-semaphore/stargazers) - Push a set of work to be done in a configurable serial fashion
* [promise-nodeify](https://github.com/kevinoid/promise-nodeify) [![GitHub stars](https://img.shields.io/github/stars/kevinoid/promise-nodeify?style=flat)](https://github.com/kevinoid/promise-nodeify/stargazers) - Standalone `nodeify` method which calls a Node-style callback on resolution or rejection.

## License
Licensed under the [Creative Commons CC0 License](https://creativecommons.org/publicdomain/zero/1.0/).
