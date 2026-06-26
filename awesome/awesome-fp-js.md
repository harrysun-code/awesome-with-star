# Functional Programming

[![GitHub stars](https://img.shields.io/github/stars/stoeffel/awesome-fp-js?style=flat)](https://github.com/stoeffel/awesome-fp-js/stargazers)

# Awesome FP JS [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This is a curated list of awesome [functional programming](https://en.wikipedia.org/wiki/Functional_programming) code and learning resources for JavaScript. As a multi-paradigm programming language, JavaScript can be written in many styles. With these resources we want to help you to make better use of JavaScript’s support for writing programs in a _functional_ way.

Functional programming is a [style of programming](https://wiki.haskell.org/Functional_programming) which models computations as the evaluation of expressions. Contrast this  with imperative programming where programs are composed of statements which change global state when executed. Functional programming typically avoids using mutable state and favors _side-effect free_ functions and _immutable_ data instead. This encourages writing composable and declarative programs that are easy to reason about.

##### Table of Contents

* [Libraries](#libraries)
  * [Data Structures](#data-structures)
  * [Algebraic Data Types](#algebraic-data-types)
  * [Lenses](#lenses)
* [Functional Languages that Compile to JavaScript](#functional-languages-that-compile-to-javascript)
* [Programming Tools](#programming-tools)
* [Resources](#resources)
  * [Books](#books)
  * [Articles](#articles)
  * [Videos](#videos)
  * [Examples and Exercises](#examples-and-exercises)
* [Community](#community)
* [Contribution](#contribution)

##### Tags
These may be appended to entries.  Each should be preceded by a "+" or "-" to indicate presence or absence of the tag's meaning.  "-" tags should only be included when they are likely to help someone filter libraries for their needs.  For instance, `-TS` tags are probably useful for Typescript users screening for types, but `-CT` tags would be less likely to be helpful to anyone.

* __CT__.  Category Theory.  This library appears to be inspired by Haskell, Scala, or another functional language's library with a grounding in Category Theory.
* __TS__.  Typescript.  This library has typescript types.

## Libraries

* [Ramda](https://github.com/ramda/ramda) [![GitHub stars](https://img.shields.io/github/stars/ramda/ramda?style=flat)](https://github.com/ramda/ramda/stargazers) – A practical functional library for JavaScript that is designed specifically for a functional programming style. A style that makes it easy to create functional pipelines and never mutates user data. +TS.
* [Ramda Adjunct](https://github.com/char0n/ramda-adjunct) [![GitHub stars](https://img.shields.io/github/stars/char0n/ramda-adjunct?style=flat)](https://github.com/char0n/ramda-adjunct/stargazers) is a community-maintained extension of Ramda.
* [Ramda-extension](https://github.com/tommmyy/ramda-extension) [![GitHub stars](https://img.shields.io/github/stars/tommmyy/ramda-extension?style=flat)](https://github.com/tommmyy/ramda-extension/stargazers) is set of utility point-free functions composed only from Ramda functions.
* [Rambda](https://github.com/selfrefactor/rambda) [![GitHub stars](https://img.shields.io/github/stars/selfrefactor/rambda?style=flat)](https://github.com/selfrefactor/rambda/stargazers) - A faster alternative to Ramda in under 10kB.
* [Rambdax](https://github.com/selfrefactor/rambdax) [![GitHub stars](https://img.shields.io/github/stars/selfrefactor/rambdax?style=flat)](https://github.com/selfrefactor/rambdax/stargazers) - Extended version of Rambda
* [Folktale](http://folktale.origamitower.com/) – A standard library for functional programming in JavaScript. Typescript support expected mid-2020.  -TS.
* [lodash/fp](https://github.com/lodash/lodash/wiki/FP-Guide) [![GitHub stars](https://img.shields.io/github/stars/lodash/lodash/wiki/FP-Guide?style=flat)](https://github.com/lodash/lodash/wiki/FP-Guide/stargazers) – An instance of [Lodash](https://github.com/lodash/lodash) [![GitHub stars](https://img.shields.io/github/stars/lodash/lodash?style=flat)](https://github.com/lodash/lodash/stargazers) with its methods wrapped to produce immutable, auto-curried, iteratee-first, data-last methods. +TS.
* [iterflow](https://github.com/gv-sh/iterflow) [![GitHub stars](https://img.shields.io/github/stars/gv-sh/iterflow?style=flat)](https://github.com/gv-sh/iterflow/stargazers) - Powerful iterator utilities for TypeScript with statistical operations, windowing, and lazy evaluation. +TS
* [functional.js](https://github.com/functionaljs/functional-js) [![GitHub stars](https://img.shields.io/github/stars/functionaljs/functional-js?style=flat)](https://github.com/functionaljs/functional-js/stargazers) – A lightweight functional JavaScript library that facilitates currying and point-free / tacit programming.
* [101](https://github.com/tjmehta/101) [![GitHub stars](https://img.shields.io/github/stars/tjmehta/101?style=flat)](https://github.com/tjmehta/101/stargazers) – A modern and modular JavaScript utility library made to work well with vanilla JavaScript methods.  -TS
* [fnuc](https://github.com/algesten/fnuc) [![GitHub stars](https://img.shields.io/github/stars/algesten/fnuc?style=flat)](https://github.com/algesten/fnuc/stargazers) – A functional library for CoffeeScript (and JavaScript) to facilitate functional composition and higher order functions.
* [barely-functional](https://github.com/cullophid/barely-functional) [![GitHub stars](https://img.shields.io/github/stars/cullophid/barely-functional?style=flat)](https://github.com/cullophid/barely-functional/stargazers) – A tiny (2.7kb) functional programming library using native ES5/6 operations. -TS.
* [bluebird-promisell](https://github.com/zhangchiqing/bluebird-promisell) [![GitHub stars](https://img.shields.io/github/stars/zhangchiqing/bluebird-promisell?style=flat)](https://github.com/zhangchiqing/bluebird-promisell/stargazers) - A practical functional programming library for promises.
* [prelude.ls](http://gkz.github.io/prelude-ls/) – A functionally oriented utility library somewhat based off of Haskell's Prelude module. -TS.
* [preludejs](https://github.com/alanrsoares/prelude-js) [![GitHub stars](https://img.shields.io/github/stars/alanrsoares/prelude-js?style=flat)](https://github.com/alanrsoares/prelude-js/stargazers) - Hardcore Functional Programming for JavaScript. -TS.
* [1-liners](https://github.com/1-liners/1-liners) [![GitHub stars](https://img.shields.io/github/stars/1-liners/1-liners?style=flat)](https://github.com/1-liners/1-liners/stargazers) – Functional tools that couldn’t be simpler. A dead simple functional utility belt, hand-crafted with love and attention.  -TS.
* [fn-curry](https://github.com/thunklife/fn-curry) [![GitHub stars](https://img.shields.io/github/stars/thunklife/fn-curry?style=flat)](https://github.com/thunklife/fn-curry/stargazers) – A simple function to curry a function.
* [curry](https://github.com/thisables/curry) [![GitHub stars](https://img.shields.io/github/stars/thisables/curry?style=flat)](https://github.com/thisables/curry/stargazers) – Curry your functions using function bind syntax.
* [compose-function](https://github.com/stoeffel/compose-function) [![GitHub stars](https://img.shields.io/github/stars/stoeffel/compose-function?style=flat)](https://github.com/stoeffel/compose-function/stargazers) – Compose a new function from smaller functions.
* [functionize](https://github.com/paldepind/functionize) [![GitHub stars](https://img.shields.io/github/stars/paldepind/functionize?style=flat)](https://github.com/paldepind/functionize/stargazers) – A collection of functions which aid in making non-functional libraries functional.
* [lambdajs](https://github.com/loop-recur/lambdajs) [![GitHub stars](https://img.shields.io/github/stars/loop-recur/lambdajs?style=flat)](https://github.com/loop-recur/lambdajs/stargazers) – The full ECMAScript API done a functional way.
* [fp-dom](https://github.com/fp-dom/) [![GitHub stars](https://img.shields.io/github/stars/fp-dom/?style=flat)](https://github.com/fp-dom//stargazers) – Making the DOM functional.
* [react-on-lambda](https://github.com/sultan99/react-on-lambda) [![GitHub stars](https://img.shields.io/github/stars/sultan99/react-on-lambda?style=flat)](https://github.com/sultan99/react-on-lambda/stargazers) - Replace JSX in React with functions (currying, compositions and etc). 
* [trifl](https://github.com/algesten/trifl) [![GitHub stars](https://img.shields.io/github/stars/algesten/trifl?style=flat)](https://github.com/algesten/trifl/stargazers) – A functional user interface library with unidirectional dataflow and a virtual dom.
* [funcy](https://github.com/bramstein/funcy) [![GitHub stars](https://img.shields.io/github/stars/bramstein/funcy?style=flat)](https://github.com/bramstein/funcy/stargazers) – An experiment in adding functional pattern matching to JavaScript. _Experimental_  :triangular_flag_on_post:
* [date-fp](https://github.com/cullophid/date-fp) [![GitHub stars](https://img.shields.io/github/stars/cullophid/date-fp?style=flat)](https://github.com/cullophid/date-fp/stargazers) – A functional utility library for working with JavaScript dates. All functions in date-fp are pure, autocurried and will not mutate the date objects they are applied to.
* [js-joda](https://github.com/js-joda/js-joda) [![GitHub stars](https://img.shields.io/github/stars/js-joda/js-joda?style=flat)](https://github.com/js-joda/js-joda/stargazers) – An immutable date and time library that provides a simple, domain-driven and clean API based on the ISO8601 calendar.
* [\_part\_](https://github.com/AutoSponge/_part_) [![GitHub stars](https://img.shields.io/github/stars/AutoSponge/_part_?style=flat)](https://github.com/AutoSponge/_part_/stargazers) – A micro library that encourages functional programming by making native methods available as partially applied functions.
* [claire](https://github.com/robotlolita/claire) [![GitHub stars](https://img.shields.io/github/stars/robotlolita/claire?style=flat)](https://github.com/robotlolita/claire/stargazers) – A property-based testing library for clearly specifying code invariants and behaviour.
* [FPO.js](https://github.com/getify/fpo) [![GitHub stars](https://img.shields.io/github/stars/getify/fpo?style=flat)](https://github.com/getify/fpo/stargazers) – FP library for JavaScript by Kyle Simpson (aka getify). Supports named-argument style methods.
* [Javascript Parser Combinator](https://github.com/d-plaindoux/parsec) [![GitHub stars](https://img.shields.io/github/stars/d-plaindoux/parsec?style=flat)](https://github.com/d-plaindoux/parsec/stargazers) – Javascript parser combinator implementation inspired by the Haskell's Parsec
* [fun-task](https://github.com/rpominov/fun-task) [![GitHub stars](https://img.shields.io/github/stars/rpominov/fun-task?style=flat)](https://github.com/rpominov/fun-task/stargazers) – An abstraction for managing asynchronous code in JS. Tasks are similar to Promises with the key difference that Tasks can represent a computation while Promises can represent only the results of a computation. Ships with Flow type definitions.
* [most](https://github.com/cujojs/most) [![GitHub stars](https://img.shields.io/github/stars/cujojs/most?style=flat)](https://github.com/cujojs/most/stargazers) – Ultra-high performance reactive programming to help you compose asynchronous operations on streams of values and events without many of the hazards of side effects and mutable shared state.
* [zen-signals](https://github.com/joaomilho/zen-signals) [![GitHub stars](https://img.shields.io/github/stars/joaomilho/zen-signals?style=flat)](https://github.com/joaomilho/zen-signals/stargazers) – ☯ The simplest signal library possible
* [funfix](https://github.com/funfix/funfix) [![GitHub stars](https://img.shields.io/github/stars/funfix/funfix?style=flat)](https://github.com/funfix/funfix/stargazers) – Funfix is a library of type classes and data types for Functional Programming in JavaScript, TypeScript and Flow.  +CT, +TS.
* [pico-lambda](https://github.com/trainyard/pico-lambda) [![GitHub stars](https://img.shields.io/github/stars/trainyard/pico-lambda?style=flat)](https://github.com/trainyard/pico-lambda/stargazers) - Arrays, Strings and things the functional way. A 640b functional library based on native methods. -TS.
* [pareto-js](https://github.com/concretesolutions/pareto.js/) [![GitHub stars](https://img.shields.io/github/stars/concretesolutions/pareto.js/?style=flat)](https://github.com/concretesolutions/pareto.js//stargazers) - An extremely small, intuitive and fast functional utility library for JavaScript -TS.
* [fpEs](https://github.com/TeaEntityLab/fpEs/) [![GitHub stars](https://img.shields.io/github/stars/TeaEntityLab/fpEs/?style=flat)](https://github.com/TeaEntityLab/fpEs//stargazers) - A small library provides simple usages of basic FP & pattern-matching/sumtype & MonadIO/Rx & Optional for Javascript. -TS.
* [Creed](http://blog.briancavalier.com/creed/) – Sophisticated and functionally-minded async with advanced features: coroutines, promises, ES2015 iterables, fantasy-land. -TS.
* [TGrid](https://github.com/samchon/tgrid) [![GitHub stars](https://img.shields.io/github/stars/samchon/tgrid?style=flat)](https://github.com/samchon/tgrid/stargazers) - Grid Computing Framework, Network & Thread extension of [TSTL](https://github.com/samchon/tstl) [![GitHub stars](https://img.shields.io/github/stars/samchon/tstl?style=flat)](https://github.com/samchon/tstl/stargazers), supporting RFC (Remote Function Call). +TS.
* [Ferrum](https://github.com/adobe/ferrum) [![GitHub stars](https://img.shields.io/github/stars/adobe/ferrum?style=flat)](https://github.com/adobe/ferrum/stargazers) – Iterator library with support for objects as iterables, lazy evaulation and`pipe()`; implements Traits (from Rust)/Type Classes (from Haskell) in JS. -TS.
* [fp-ts](https://gcanti.github.io/fp-ts/) - Typed functional programming in TypeScript. +CT, +TS.
* [iter-tools](https://github.com/iter-tools/iter-tools) [![GitHub stars](https://img.shields.io/github/stars/iter-tools/iter-tools?style=flat)](https://github.com/iter-tools/iter-tools/stargazers) - a rich toolset for working with iterables, both sync and async. +TS.
* [remeda](https://remedajs.com/) A function library roughly subsetting Ramda, but written in Typescript and thus more type-friendly. +TS.
* [futil-js](https://github.com/smartprocure/futil-js) [![GitHub stars](https://img.shields.io/github/stars/smartprocure/futil-js?style=flat)](https://github.com/smartprocure/futil-js/stargazers) - A collection of functional utilities that could conceivably be part of a library like lodash/fp, but for some reason or other are not.
* [rubico](https://github.com/a-synchronous/rubico) [![GitHub stars](https://img.shields.io/github/stars/a-synchronous/rubico?style=flat)](https://github.com/a-synchronous/rubico/stargazers) - 🏞 [a]synchronous functional syntax
* [rocket-pipes](https://github.com/darky/rocket-pipes) [![GitHub stars](https://img.shields.io/github/stars/darky/rocket-pipes?style=flat)](https://github.com/darky/rocket-pipes/stargazers) - Powerful pipes, that chain Promise and ADT like Maybe or Either from popular FP libraries. +TS
* [omg-curry](https://github.com/Debdut/omg-curry) [![GitHub stars](https://img.shields.io/github/stars/Debdut/omg-curry?style=flat)](https://github.com/Debdut/omg-curry/stargazers) - Comprehensive Curry Library with Operator Curry, Curry from functions, Decurry and Infifnite Curries.
* [lfi](https://github.com/TomerAberbach/lfi) [![GitHub stars](https://img.shields.io/github/stars/TomerAberbach/lfi?style=flat)](https://github.com/TomerAberbach/lfi/stargazers) - A Lazy Functional Iteration Library Supporting Sync, Async, and Concurrent Iteration.
* [ts-multimethod](https://github.com/darky/ts-multimethod) [![GitHub stars](https://img.shields.io/github/stars/darky/ts-multimethod?style=flat)](https://github.com/darky/ts-multimethod/stargazers) - TypeScript multimethods inspired by Clojure multimethods. +TS
* [ts-fp-di](https://github.com/darky/ts-fp-di) [![GitHub stars](https://img.shields.io/github/stars/darky/ts-fp-di?style=flat)](https://github.com/darky/ts-fp-di/stargazers) - Tiny TypeScript functional dependency injection, based on Node.js AsyncLocalStorage. +TS
* [effect-ts](https://github.com/Effect-TS/core) [![GitHub stars](https://img.shields.io/github/stars/Effect-TS/core?style=flat)](https://github.com/Effect-TS/core/stargazers) – A Fully-fledged functional effect system for typescript with a rich standard library. +TS
* [qio](https://github.com/tusharmath/qio) [![GitHub stars](https://img.shields.io/github/stars/tusharmath/qio?style=flat)](https://github.com/tusharmath/qio/stargazers) – A type-safe, functional, performant, lawful, composable data structure that solves practical problems of effect-full code in node and browser. +TS
* [Ditox.js](https://github.com/mnasyrov/ditox) [![GitHub stars](https://img.shields.io/github/stars/mnasyrov/ditox?style=flat)](https://github.com/mnasyrov/ditox/stargazers) - Powerful dependency injection container for building modular apps. +TS
* [RxEffects](https://github.com/mnasyrov/rx-effects) [![GitHub stars](https://img.shields.io/github/stars/mnasyrov/rx-effects?style=flat)](https://github.com/mnasyrov/rx-effects/stargazers) - Reactive state and effect management with RxJS. +TS
* [fxts](https://github.com/marpple/FxTS) [![GitHub stars](https://img.shields.io/github/stars/marpple/FxTS?style=flat)](https://github.com/marpple/FxTS/stargazers) - Lazy evaluation and concurrency. +TS
* [ts-belt](https://mobily.github.io/ts-belt/) - Fast, modern, and practical utility library for FP in TypeScript. (Uses a data-first approach like remeda, but is [faster](https://mobily.github.io/ts-belt/benchmarks/v3.7.0/macbook-air-2020) than remeda, ramda, rambda, and lodash/fp.)
* [fp-multik](https://github.com/lulldev/fp-multik) [![GitHub stars](https://img.shields.io/github/stars/lulldev/fp-multik?style=flat)](https://github.com/lulldev/fp-multik/stargazers) - JS/TS lightweight value-multimethod util
* [true-myth](https://github.com/true-myth/true-myth) [![GitHub stars](https://img.shields.io/github/stars/true-myth/true-myth?style=flat)](https://github.com/true-myth/true-myth/stargazers) A library for safe, idiomatic null and error handling in TypeScript, with `Maybe` and `Result` types, supporting both a functional style and a more traditional method-call style
* [ts-pattern](https://github.com/gvergnaud/ts-pattern) [![GitHub stars](https://img.shields.io/github/stars/gvergnaud/ts-pattern?style=flat)](https://github.com/gvergnaud/ts-pattern/stargazers) - The exhaustive Pattern Matching library for TypeScript, with smart type inference. Pattern Matching is a code-branching technique coming from FP languages.
* [hyogwa](https://github.com/ENvironmentSet/hyogwa) [![GitHub stars](https://img.shields.io/github/stars/ENvironmentSet/hyogwa?style=flat)](https://github.com/ENvironmentSet/hyogwa/stargazers) - Natural 🌿 effect system that fits TypeScript; Write codes as you write **plain typescript code**.
* [Verticalize](https://github.com/laurentpayot/verticalize) [![GitHub stars](https://img.shields.io/github/stars/laurentpayot/verticalize?style=flat)](https://github.com/laurentpayot/verticalize/stargazers) - Super lightweight function that looks and behaves like a pipe operator.
* [PureEval](https://github.com/PureEval/PureEval) [![GitHub stars](https://img.shields.io/github/stars/PureEval/PureEval?style=flat)](https://github.com/PureEval/PureEval/stargazers) - A powerful JavaScript functional programming toolset, including utility functions and abstract data structures.
* [context-fp](https://github.com/darky/context-fp) [![GitHub stars](https://img.shields.io/github/stars/darky/context-fp?style=flat)](https://github.com/darky/context-fp/stargazers) - Microscopic functional programming context aka dependency injection. +TS
* [klubok](https://github.com/darky/klubok) [![GitHub stars](https://img.shields.io/github/stars/darky/klubok?style=flat)](https://github.com/darky/klubok/stargazers) - Pipes with easy mocking, intended for huge amount of unit tests. +TS
* [fp-filters](https://github.com/Oaxoa/fp-filters) [![GitHub stars](https://img.shields.io/github/stars/Oaxoa/fp-filters?style=flat)](https://github.com/Oaxoa/fp-filters/stargazers) - A curated collection of 130+ common-use filter functions. 
  Written in a functional programming style. Lightweight direct imports. Supports ES modules and CommonJS. 100% Unit 
  tested. +TS
* [tinyeffect](https://github.com/Snowflyt/tinyeffect) [![GitHub stars](https://img.shields.io/github/stars/Snowflyt/tinyeffect?style=flat)](https://github.com/Snowflyt/tinyeffect/stargazers) - A tiny TypeScript library for handling side effects in a unified way using algebraic effects. +TS

### Data Structures

Write performant functional code by using the right data structures for the task.

* [Icepick](https://github.com/aearly/icepick) [![GitHub stars](https://img.shields.io/github/stars/aearly/icepick?style=flat)](https://github.com/aearly/icepick/stargazers) Utilities for treating frozen JavaScript objects as persistent immutable collections
* [Immutable.js](https://github.com/facebook/immutable-js) [![GitHub stars](https://img.shields.io/github/stars/facebook/immutable-js?style=flat)](https://github.com/facebook/immutable-js/stargazers) – Immutable persistent data collections.
* [Immer](https://github.com/mweststrate/immer) [![GitHub stars](https://img.shields.io/github/stars/mweststrate/immer?style=flat)](https://github.com/mweststrate/immer/stargazers) – Immer is a tiny package for immutable state based on copy-on-write mechanism. +TS.
* [Mori](https://github.com/swannodette/mori) [![GitHub stars](https://img.shields.io/github/stars/swannodette/mori?style=flat)](https://github.com/swannodette/mori/stargazers) – ClojureScript’s persistent data structures and supporting API from the comfort of vanilla JavaScript.
* [Baobab](https://github.com/Yomguithereal/baobab) [![GitHub stars](https://img.shields.io/github/stars/Yomguithereal/baobab?style=flat)](https://github.com/Yomguithereal/baobab/stargazers) – persistent and optionally immutable data tree with cursors.
* [immutable-sequence.js](https://github.com/qiao/immutable-sequence.js) [![GitHub stars](https://img.shields.io/github/stars/qiao/immutable-sequence.js?style=flat)](https://github.com/qiao/immutable-sequence.js/stargazers) –  High performance implementation of Immutable Sequence in JavaScript, based on [Finger Trees](https://github.com/qiao/fingertree.js) [![GitHub stars](https://img.shields.io/github/stars/qiao/fingertree.js?style=flat)](https://github.com/qiao/fingertree.js/stargazers).
* [Timm](http://guigrpa.github.io/timm/) – Immutability helpers with fast reads and acceptable writes.
* [Lazy.js](https://github.com/dtao/lazy.js) [![GitHub stars](https://img.shields.io/github/stars/dtao/lazy.js?style=flat)](https://github.com/dtao/lazy.js/stargazers) – A utility library with a lazy engine under the hood that strives to do as little work as possible while being as flexible as possible.
* [DerivableJS](https://github.com/ds300/derivablejs) [![GitHub stars](https://img.shields.io/github/stars/ds300/derivablejs?style=flat)](https://github.com/ds300/derivablejs/stargazers) – Functional Reactive State for JavaScript and TypeScript. DerivableJS enables you to make elegant declarative statements about how your bits of state are related. +TS.
* [imlazy](https://github.com/benji6/imlazy) [![GitHub stars](https://img.shields.io/github/stars/benji6/imlazy?style=flat)](https://github.com/benji6/imlazy/stargazers) – Library for creating and manipulating lazy iterables using the ES2015 iteration protocols.
* [collectable](https://github.com/frptools/collectable) [![GitHub stars](https://img.shields.io/github/stars/frptools/collectable?style=flat)](https://github.com/frptools/collectable/stargazers) – Super high-performance immutable data structures for modern JavaScript and TypeScript applications. +TS.
* [List](https://github.com/funkia/list) [![GitHub stars](https://img.shields.io/github/stars/funkia/list?style=flat)](https://github.com/funkia/list/stargazers) - An extremely fast immutable list with a comprehensive functional API. Designed to [seamlessly integrate with Ramda](https://github.com/funkia/list#seamless-ramda-integration).
* [prelude.ts](https://github.com/emmanueltouzery/prelude.ts) [![GitHub stars](https://img.shields.io/github/stars/emmanueltouzery/prelude.ts?style=flat)](https://github.com/emmanueltouzery/prelude.ts/stargazers) - Immutable persistent collections, functional constructs such as Option and Either, and combinators. Implemented in Typescript but supports javascript too.  +CT, +TS.
* [TSTL](https://github.com/samchon/tstl) [![GitHub stars](https://img.shields.io/github/stars/samchon/tstl?style=flat)](https://github.com/samchon/tstl/stargazers) - C++ STL (Standard Template Library) is implemented in TypeScript. STL Containers, iterators, algorithms and functors, that following functional programming rule, are provided. +TS.

### Algebraic Data Types

Use the laws of math instead of always reinventing your own thing. Algebraic!

* [Fantasy Land](https://github.com/fantasyland/fantasy-land) [![GitHub stars](https://img.shields.io/github/stars/fantasyland/fantasy-land?style=flat)](https://github.com/fantasyland/fantasy-land/stargazers) – Not a library, but a specification of the Monad laws for libraries to follow.
* [Static Land](https://github.com/rpominov/static-land) [![GitHub stars](https://img.shields.io/github/stars/rpominov/static-land?style=flat)](https://github.com/rpominov/static-land/stargazers) – Specification similar to Fantasy Land but based on static methods rather than instance methods.
* [immutable-ext](https://github.com/DrBoolean/immutable-ext) [![GitHub stars](https://img.shields.io/github/stars/DrBoolean/immutable-ext?style=flat)](https://github.com/DrBoolean/immutable-ext/stargazers) – FantasyLand extensions for [Immutable.js](https://github.com/facebook/immutable-js) [![GitHub stars](https://img.shields.io/github/stars/facebook/immutable-js?style=flat)](https://github.com/facebook/immutable-js/stargazers).
* [daggy](https://github.com/puffnfresh/daggy) [![GitHub stars](https://img.shields.io/github/stars/puffnfresh/daggy?style=flat)](https://github.com/puffnfresh/daggy/stargazers) – Library for creating tagged constructors.
* [Sanctuary](https://github.com/plaid/sanctuary) [![GitHub stars](https://img.shields.io/github/stars/plaid/sanctuary?style=flat)](https://github.com/plaid/sanctuary/stargazers) – Sanctuary makes it possible to write safe code without null checks.  +CT, +TS.
* [monet.js](http://cwmyers.github.io/monet.js/) – A library that assists functional programming by providing a rich set of Monads and other useful functions.  +CT, +TS.
* [union-type](https://github.com/paldepind/union-type) [![GitHub stars](https://img.shields.io/github/stars/paldepind/union-type?style=flat)](https://github.com/paldepind/union-type/stargazers) – A small JavaScript library for defining and using union types.
* [freeky](https://github.com/DrBoolean/freeky) [![GitHub stars](https://img.shields.io/github/stars/DrBoolean/freeky?style=flat)](https://github.com/DrBoolean/freeky/stargazers) – A collection of Free monads.
* [Fluture](https://github.com/Avaq/Fluture) [![GitHub stars](https://img.shields.io/github/stars/Avaq/Fluture?style=flat)](https://github.com/Avaq/Fluture/stargazers) – A Future library with included control utilities, high performance and great error messages.
* [fantasy-combinators](https://github.com/fantasyland/fantasy-combinators) [![GitHub stars](https://img.shields.io/github/stars/fantasyland/fantasy-combinators?style=flat)](https://github.com/fantasyland/fantasy-combinators/stargazers) – Common combinators.
* [fantasy-birds](https://github.com/fantasyland/fantasy-birds) [![GitHub stars](https://img.shields.io/github/stars/fantasyland/fantasy-birds?style=flat)](https://github.com/fantasyland/fantasy-birds/stargazers) – Port of the Haskell package Data.Aviary.Birds. Everything for your combinatory needs.
* [crocks](https://github.com/evilsoft/crocks) [![GitHub stars](https://img.shields.io/github/stars/evilsoft/crocks?style=flat)](https://github.com/evilsoft/crocks/stargazers) – A collection of popular Algebraic Data Types with the main goal to curate and provide not only a common interface between each type, but also all of the helper functions needed to hit the ground running. -TS.
* [kudo-js](https://github.com/blitzritz/kudojs) [![GitHub stars](https://img.shields.io/github/stars/blitzritz/kudojs?style=flat)](https://github.com/blitzritz/kudojs/stargazers) - A small utility library with a set of Algebraic Data Types and Helper functions to help you write code in a functional programming style in Javascript
* [purify](https://github.com/gigobyte/purify) [![GitHub stars](https://img.shields.io/github/stars/gigobyte/purify?style=flat)](https://github.com/gigobyte/purify/stargazers) - Functional programming library for TypeScript focusing on ADTs.  +CT, +TS.
* [MojiScript](https://github.com/joelnet/MojiScript) [![GitHub stars](https://img.shields.io/github/stars/joelnet/MojiScript?style=flat)](https://github.com/joelnet/MojiScript/stargazers)- an async-first, opinionated, and functional language designed to have 100% compatibility with JavaScript engines
* [Pratica](https://github.com/rametta/pratica) [![GitHub stars](https://img.shields.io/github/stars/rametta/pratica?style=flat)](https://github.com/rametta/pratica/stargazers) - Small, simple, easy FP data types for pragmatic and productive developers who need to ship reliable code fast.  +CT, +TS.
* [Tifi](https://github.com/mobily/tifi) [![GitHub stars](https://img.shields.io/github/stars/mobily/tifi?style=flat)](https://github.com/mobily/tifi/stargazers) - Tifi is a library for functional programming in TypeScript. It solves a problem of the existence of both `undefined` and `null`. Tifi is inspired by the OCaml/Reason utilities for the option data type. +CT, +TS.
* [sweet-monads](https://github.com/JSMonk/sweet-monads) [![GitHub stars](https://img.shields.io/github/stars/JSMonk/sweet-monads?style=flat)](https://github.com/JSMonk/sweet-monads/stargazers) - A collection of popular monads (such as `Either` and `Maybe`) and the lazy iterator.
* [NeverThrow](https://github.com/supermacro/neverthrow) [![GitHub stars](https://img.shields.io/github/stars/supermacro/neverthrow?style=flat)](https://github.com/supermacro/neverthrow/stargazers) - This package contains a `Result` type that represents either success (`Ok`) or failure (`Err`).

### Lenses

* [lenses](https://github.com/DrBoolean/lenses) [![GitHub stars](https://img.shields.io/github/stars/DrBoolean/lenses?style=flat)](https://github.com/DrBoolean/lenses/stargazers) – Composable [kmett](https://github.com/ekmett/lens) [![GitHub stars](https://img.shields.io/github/stars/ekmett/lens?style=flat)](https://github.com/ekmett/lens/stargazers) style lenses.
* [optics](https://github.com/flunc/optics) [![GitHub stars](https://img.shields.io/github/stars/flunc/optics?style=flat)](https://github.com/flunc/optics/stargazers) – Profunctor optics (Lens, Prism, iso).
* [ramda-lens](https://github.com/ramda/ramda-lens) [![GitHub stars](https://img.shields.io/github/stars/ramda/ramda-lens?style=flat)](https://github.com/ramda/ramda-lens/stargazers) – :ram: :mag_right: Lens library built on Ramda.
* [fantasy-lenses](https://github.com/fantasyland/fantasy-lenses) [![GitHub stars](https://img.shields.io/github/stars/fantasyland/fantasy-lenses?style=flat)](https://github.com/fantasyland/fantasy-lenses/stargazers) – Composable, immutable getters and setters. (Profunctor lenses WIP)
* [nanoscope](https://github.com/5outh/nanoscope) [![GitHub stars](https://img.shields.io/github/stars/5outh/nanoscope?style=flat)](https://github.com/5outh/nanoscope/stargazers) – Lenses with dotty support.
* [partial.lenses](https://github.com/calmm-js/partial.lenses) [![GitHub stars](https://img.shields.io/github/stars/calmm-js/partial.lenses?style=flat)](https://github.com/calmm-js/partial.lenses/stargazers) – Partial lenses is a comprehensive, high-performance optics library for JavaScript.
* [shades](https://github.com/jamesmcnamara/shades) [![GitHub stars](https://img.shields.io/github/stars/jamesmcnamara/shades?style=flat)](https://github.com/jamesmcnamara/shades/stargazers) – A lodash-inspired lens-like library for Javascript.

## Functional Languages that Compile to JavaScript

* [ClojureScript](https://github.com/clojure/clojurescript) [![GitHub stars](https://img.shields.io/github/stars/clojure/clojurescript?style=flat)](https://github.com/clojure/clojurescript/stargazers) – Compiles [Clojure](http://clojure.org/), a hosted Lisp with immutable persistent data structures, to JavaScript.
* [Elm](http://elm-lang.org/) – A type-safe functional programming language for declaratively creating web browser-based graphical user interfaces. Implemented in Haskell.
* [Fable](http://fable.io/) - Compiles [F#](http://fsharp.org) to readable JavaScript.
* [PureScript](http://www.purescript.org/) – A small strongly typed programming language that compiles to JavaScript.
* [Idris](http://www.idris-lang.org/) – A general purpose pure functional programming language with dependent types.
* [GHCJS](https://github.com/ghcjs/ghcjs) [![GitHub stars](https://img.shields.io/github/stars/ghcjs/ghcjs?style=flat)](https://github.com/ghcjs/ghcjs/stargazers) – [Haskell](https://www.haskell.org/) to JavaScript compiler, based on GHC.
* [ElixirScript](https://github.com/bryanjos/elixirscript) [![GitHub stars](https://img.shields.io/github/stars/bryanjos/elixirscript?style=flat)](https://github.com/bryanjos/elixirscript/stargazers) – Compiles a subset of [Elixir](http://elixir-lang.org/), a dynamic, functional language designed for building scalable and maintainable applications, to JavaScript.
* [Js\_of\_ocaml](http://ocsigen.org/js_of_ocaml/) – Compiles [OCaml](http://ocaml.org/) bytecode to JavaScript, making it possible to run OCaml programs in the browser.
* [Reason](https://reasonml.github.io) – Reason is a new interface to OCaml, a highly expressive dialect of the ML language featuring type inference and static type checking.
* [ReScript](https://rescript-lang.org/) – (previously known as [Bucklescript](https://rescript-lang.org/bucklescript-rebranding)) ReScript is a type-safe language that compiles to the highest quality of clean, readable and performant JavaScript code.
* [Scala.js](http://www.scala-js.org/) – Compiles [Scala](http://www.scala-lang.org/) to JavaScript.
* [LiveScript](http://gkz.github.io/LiveScript/) – LiveScript has a straightforward mapping to JavaScript and allows you to write expressive code devoid of repetitive boilerplate.
* [Quack](https://github.com/quack/quack) [![GitHub stars](https://img.shields.io/github/stars/quack/quack?style=flat)](https://github.com/quack/quack/stargazers) - A multi-paradigm programming language with gradual and duck typing that targets PHP and JS.
* [ion](https://github.com/ion-lang/ion) [![GitHub stars](https://img.shields.io/github/stars/ion-lang/ion?style=flat)](https://github.com/ion-lang/ion/stargazers) - no BS JS
* [RamdaScript](https://github.com/yosbelms/ramdascript) [![GitHub stars](https://img.shields.io/github/stars/yosbelms/ramdascript?style=flat)](https://github.com/yosbelms/ramdascript/stargazers) - A Lisp that compiles to opinionated JavaScript on top of RamdaJS
* [RacketScript](https://github.com/vishesh/racketscript) [![GitHub stars](https://img.shields.io/github/stars/vishesh/racketscript?style=flat)](https://github.com/vishesh/racketscript/stargazers) – RacketScript aims to leverage both JavaScript and Racket's ecosystem, and make interoperability between them clean and smooth.
* [Koka](https://www.microsoft.com/en-us/research/project/koka/) – Koka is a function-oriented programming language that seperates pure values from side-effecting computations with a familiar JavaScript like syntax.
* [TypeScript](https://www.typescriptlang.org/) - TypeScript is a typed superset of JavaScript that compiles to plain JavaScript.
* [Gleam](https://gleam.run) - Gleam is a typed, functional language that compiles to Erlang and JavaScript.

## Programming Tools

* [eslint-plugin-fp](https://github.com/jfmengels/eslint-plugin-fp) [![GitHub stars](https://img.shields.io/github/stars/jfmengels/eslint-plugin-fp?style=flat)](https://github.com/jfmengels/eslint-plugin-fp/stargazers) - ESLint rules for functional programming
* [4.5](https://github.com/TylorS/4.5) [![GitHub stars](https://img.shields.io/github/stars/TylorS/4.5?style=flat)](https://github.com/TylorS/4.5/stargazers) – A functional assertions library. If you prefer functional style APIs and practices in JavaScript, this library aims to solve this with functionally-oriented assertions that are lazy and monadic.
* [hm-def](https://github.com/xodio/hm-def) [![GitHub stars](https://img.shields.io/github/stars/xodio/hm-def?style=flat)](https://github.com/xodio/hm-def/stargazers) – Runtime type checking for JS with Hindley Milner signatures.
* [ftor](https://github.com/kongware/ftor) [![GitHub stars](https://img.shields.io/github/stars/kongware/ftor?style=flat)](https://github.com/kongware/ftor/stargazers) - A pluggable runtime type checker and functional debugging tool that supports parametric and row polymorphism, implicit rank-2 types and algebraic data types via Scott Encoding.

## Resources

### Books

* [Professor Frisby’s Mostly Adequate Guide to Functional Programming](https://github.com/MostlyAdequate/mostly-adequate-guide) [![GitHub stars](https://img.shields.io/github/stars/MostlyAdequate/mostly-adequate-guide?style=flat)](https://github.com/MostlyAdequate/mostly-adequate-guide/stargazers) – This is a book on the functional paradigm in general using the world’s most popular functional programming language: JavaScript. It’s a practical introduction that builds up intuition through real-world examples. Strongly recommended. By [Brian Lonsdorf](https://twitter.com/drboolean) (2016)
* [Functional-Light JavaScript](https://github.com/getify/functional-light-js) [![GitHub stars](https://img.shields.io/github/stars/getify/functional-light-js?style=flat)](https://github.com/getify/functional-light-js/stargazers) – This book explores the core principles of functional programming (FP) that can be applied to JavaScript. But what makes this book different is that it approaches these principles without all the heavy terminology.
* [JavaScript Allongé](https://leanpub.com/javascriptallongesix), the “Six” edition. Starts with as little as possible about functions – but no less! – and builds up towards powerful combinators and decorators. A foundational book. By [Reginald  Braithwaite](https://github.com/raganwald) [![GitHub stars](https://img.shields.io/github/stars/raganwald?style=flat)](https://github.com/raganwald/stargazers) (2016)
* [Functional Programming in JavaScript](https://www.manning.com/books/functional-programming-in-javascript) teaches JavaScript developers functional techniques that will improve extensibility, modularity, reusability, testability, and performance. Through concrete examples and jargon-free explanations, this book teaches you how to apply functional programming to real-life development tasks. By Luis Atencio (2016)
* [Eloquent JavaScript](http://eloquentjavascript.net/). A modern introduction to programming using JavaScript. By Marijn Haverbeke (2014)
* [Functional JavaScript](http://shop.oreilly.com/product/0636920028857.do) teaches how to create code that’s beautiful, safe, and simple to understand and test by using JavaScript’s functional programming support. By [Michael Fogus](https://github.com/fogus) [![GitHub stars](https://img.shields.io/github/stars/fogus?style=flat)](https://github.com/fogus/stargazers) (2013)
* [Grokking Simplicity](https://www.manning.com/books/grokking-simplicity) teaches functional programming from first principles. It uses JavaScript for all code examples and it uses real-world scenarios. By [Eric Normand](https://github.com/ericnormand) [![GitHub stars](https://img.shields.io/github/stars/ericnormand?style=flat)](https://github.com/ericnormand/stargazers) (2019)
* [scriptum](https://github.com/kongware/scriptum/blob/master/README.md) [![GitHub stars](https://img.shields.io/github/stars/kongware/scriptum/blob/master/README.md?style=flat)](https://github.com/kongware/scriptum/blob/master/README.md/stargazers) - a no-frills functional programming library and a online course based on it

### Articles

* [FP Concepts in JavaScript](https://medium.com/@collardeau/intro-to-functional-programming-concepts-in-javascript-b0650773139c) – An introduction to Functional Programming Concepts in JavaScript. Uses the Ramda library to teach the concepts of composition, pointfree style, and functors through the simplest of examples.
* [Functional programming with JavaScript](http://stephen-young.me.uk/2013/01/20/functional-programming-with-javascript.html) – Another introduction to Functional Programming in JavaScript with a focus on three key themes: computation as the application of functions, statelessness, avoiding side effects.
* [A gentle introduction to functional JavaScript](http://jrsinclair.com/articles/2016/gentle-introduction-to-functional-javascript-intro/) – A four-part series introduction functional programming in JavaScript that gets you up to speed what all the hype about functional programming is all about.
* [Functors from first principle - explained with JS](https://dev.to/snird/functors-from-first-principle-37lh) - Explaining functors concept using JavaScript.
* [Why Curry Helps](https://hughfdjackson.com/javascript/why-curry-helps/) – A short overview of how to write reusable and declarative code using currying.
* [Favoring Curry](http://fr.umio.us/favoring-curry/) - Practical applications of currying using Ramda.
* [Functional Mumbo Jumbo – ADTs](http://blog.jenkster.com/2016/06/functional-mumbo-jumbo-adts.html) – A beginner-friendly introduction to Algebraic Data Types.
* [JavaScript and Type Thinking](https://medium.com/@yelouafi/javascript-and-type-thinking-735edddc388d) – Learn to reason about your JavaScript code with _type thinking_. Algebraic Data Types are introduced as a conceptual basis to reason about program entities.
* [Lazy, composable, and modular JavaScript](https://codewords.recurse.com/issues/four/lazy-composable-and-modular-javascript) – Use four new features of ES6 – iterables, generators, fat arrows, and for-of – in conjunction with higher-order functions, function composition, and lazy evaluation, to write cleaner and more modular JavaScript.
* [Why Ramda](http://fr.umio.us/why-ramda/) – To those not used to functional programming, Ramda seems to serve no purpose whatsoever. However, it does offer a different style of coding, a style that’s taken for granted in purely functional programming languages: Ramda makes it simple for you to build complex logic through functional composition.
* [Monads in JavaScript](https://curiosity-driven.org/monads-in-javascript) – An introduction to the Monad design pattern in JavaScript.
* [A Monad in Practicality: First-Class Failures](https://web.archive.org/web/20241118045403/https://robotlolita.me/articles/2013/a-monad-in-practicality-first-class-failures/) – A walk through some practical use cases for specific monadic structures in JavaScript: use the `Maybe` monad to handle simple failure cases and model more complex scenarios with the `Either` monad or the `Validation` applicative functor.
* [Functional programming](https://glebbahmutov.com/blog/tags/functional/) – Many articles on various aspects of functional programming in JavaScript by Gleb Bahmutov.
* [Functional Programming Jargon](https://github.com/hemanth/functional-programming-jargon) [![GitHub stars](https://img.shields.io/github/stars/hemanth/functional-programming-jargon?style=flat)](https://github.com/hemanth/functional-programming-jargon/stargazers) – Jargon from the functional programming world explained in JavaScript.
* [Data Structures in JavaScript](http://blog.benoitvallon.com/data-structures-in-javascript/data-structures-in-javascript/) – A series of blog posts that reimplements various data structures in JavaScript to better understand their benefits and downsides.
* [So You Want to be a Functional Programmer](https://medium.com/@cscalfani/so-you-want-to-be-a-functional-programmer-part-1-1f15e387e536) - Easy to understand, with some examples, introduction to Functional Programming in Javascript and Elm.
* [Functional Programming for JavaScript People](https://medium.com/@chetcorcos/functional-programming-for-javascript-people-1915d8775504) - A complete introduction to functional programming patterns by Chet Corcos with a lot of javascript examples.
* [Introduction to Immutable.js and Functional Programming Concepts](https://auth0.com/blog/intro-to-immutable-js/) - Learn about functional data structures and their uses in this overview of Facebook's popular library for JavaScript: Immutable.js.
* [Master the JavaScript Interview: What is Functional Programming?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0) - A simple introduction by @ericelliott to functional principles and vocabulary.
* [Composing Software](https://medium.com/javascript-scene/the-rise-and-fall-and-rise-of-functional-programming-composable-software-c2d91b424c8c) - A series of articles on learning functional programming and compositional software techniques in JavaScript ES6+ from the ground up by @ericelliott.
* [Anonymous Recursion in JavaScript](https://dev.to/simov/anonymous-recursion-in-javascript) - Short and easy to understand article about implementing anonymous recursion in JavaScript.
* [Functional Composition in Javascript](https://joecortopassi.com/articles/functional-composition-in-javascript/) – Step by step explanation of how to compose functions in javascript.
* [Functional Programming Principles in Javascript](https://medium.freecodecamp.org/functional-programming-principles-in-javascript-1b8fc6c3563f) - Practical code examples to learn functional programming concepts like pure function, immutability, first-class entities, and higher order functions
* [Basic Monads in Javascript](https://dev.to/rametta/basic-monads-in-javascript-3el3) - Introduction to 2 easy monads in Javascript, Maybe & Either.
* [F# for JavaScript Devs](https://dev.to/rametta/f-for-js-devs-2b88) - Showcasing the similarities between F# and JavaScript
* [A practical guide to writing more functional Javascript](https://medium.com/@nadeesha/a-practical-guide-to-writing-more-functional-javascript-db49409f71) - A step by step guide to convert imperative JavaScript to more declarative, functional JavaScript.
* [You don't (may not) need loops ➿](https://github.com/you-dont-need/You-Dont-Need-Loops) [![GitHub stars](https://img.shields.io/github/stars/you-dont-need/You-Dont-Need-Loops?style=flat)](https://github.com/you-dont-need/You-Dont-Need-Loops/stargazers) - Loops are one of the first constructs that junior programmers learn, but they can pose many potential issues in the software development process, and could be avoided in many cases.

### Videos

* [Classroom Coding with Prof. Frisby](https://www.youtube.com/watch?v=h_tkIpwbsxY&list=PLK_hdtAJ4KqX0JOs_KMAmUNTNMRYhWEaC) – A series that builds a “practical” web application with React and functional programming in JavaScript.
* [Hey Underscore, You're Doing It Wrong!](https://www.youtube.com/watch?v=m3svKOdZijA) – Underscore.js claims to be a functional programming library, but is it really?
* [Functional programming patterns for the non-mathematician](https://www.youtube.com/watch?v=AvgwKjTPMmM) – Learn about practical use cases for functors, applicatives, and monads.
* [Pure JavaScript](https://vimeo.com/49384334) – Christian Johansen will show you how you can significantly up your game by leaving loops behind and embracing functions as the primary unit of abstraction.
* [Functional programming in JavaScript](https://www.youtube.com/playlist?list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84) - A series by Mattias Petter Johansson, from the youtube channel FunFunFunction, that is specifically about popularization of functional programming in JavaScript.
* [Functional Programming in TypeScript](https://www.youtube.com/playlist?list=PLuPevXgCPUIMbCxBEnc1dNwboH6e2ImQo) - Discover functional programming with Typescript and create a library like fp-ts alongside Sahand Javid in this beginner-friendly YouTube playlist.
* [Anjana Vakil: Learning Functional Programming with JavaScript - JSUnconf 2016](https://www.youtube.com/watch?v=e-5obm1G_FY) - A simple and understandable introduction of functional proramming in javascript.
* [Functional Programming Basics In ES6](https://www.youtube.com/watch?v=FYXpOjwYzcs) - A complete introduction to functional programming in javascript made it easy by ES6.
* [JavaScript Programmers Should Learn Algebraic Data Types -- May 2018 -- UtahJS Lehi](https://www.youtube.com/watch?v=B0VoyujJWIE) - Seth House explains how ADTs (Algebraic Data Types) can be useful to JavaScript developers.

### Examples and Exercises

* [FPJS-Class](https://github.com/loop-recur/FPJS-Class) [![GitHub stars](https://img.shields.io/github/stars/loop-recur/FPJS-Class?style=flat)](https://github.com/loop-recur/FPJS-Class/stargazers) – Functional Programming learned through JavaScript.
* [functional-javascript-workshop](https://github.com/timoxley/functional-javascript-workshop) [![GitHub stars](https://img.shields.io/github/stars/timoxley/functional-javascript-workshop?style=flat)](https://github.com/timoxley/functional-javascript-workshop/stargazers) – The goal of this workshop is to create realistic problems that can be solved using terse, vanilla, idiomatic JavaScript to teach fundamental functional programming features of JavaScript.
* [functional-frontend-architecture](https://github.com/paldepind/functional-frontend-architecture) [![GitHub stars](https://img.shields.io/github/stars/paldepind/functional-frontend-architecture?style=flat)](https://github.com/paldepind/functional-frontend-architecture/stargazers) – A functional frontend framework. Based on Ramda + union-type-js + Flyd + Snabbdom
* [cube-composer](https://github.com/sharkdp/cube-composer) [![GitHub stars](https://img.shields.io/github/stars/sharkdp/cube-composer?style=flat)](https://github.com/sharkdp/cube-composer/stargazers) – A puzzle game inspired by functional programming.
* [FP Youtube Search](https://github.com/jaysoo/example-fp-youtube-search) [![GitHub stars](https://img.shields.io/github/stars/jaysoo/example-fp-youtube-search?style=flat)](https://github.com/jaysoo/example-fp-youtube-search/stargazers) – YouTube search app with ReactJS, Redux, and FP concepts
* [Hardcore Functional Programming in JavaScript](https://frontendmasters.com/courses/functional-javascript/) – Learn to apply techniques from the forefront of computer science research to solve practical problems in Javascript. Discover functional programming and see it demonstrated step-by-step with how to build an example web app using abstract interfaces like Monads, Functors, Monoids and Applicatives. (_commercial_)
* [Escape from Callback Mountain](https://github.com/justsml/escape-from-callback-mountain) [![GitHub stars](https://img.shields.io/github/stars/justsml/escape-from-callback-mountain?style=flat)](https://github.com/justsml/escape-from-callback-mountain/stargazers) - Design & refactoring tips for Promise-based Functional JavaScript. Key benefits include better readability, testability, and reusability. MIT.
* [Learn Rx](http://reactivex.io/learnrx/) – A series of interactive exercises introducing five basic ingredients of functional (reactive) programming: the `map`, `filter`, `concatAll`, `reduce`, and `zip` functions.
* [Holdem Evaluator](https://github.com/laberin/holdem-eval) [![GitHub stars](https://img.shields.io/github/stars/laberin/holdem-eval?style=flat)](https://github.com/laberin/holdem-eval/stargazers) - Yet another Holdem Evaluator with Ramda functional style

## Community

### Related Lists

* [Awesome FRP JS](https://github.com/stoeffel/awesome-frp-js) [![GitHub stars](https://img.shields.io/github/stars/stoeffel/awesome-frp-js?style=flat)](https://github.com/stoeffel/awesome-frp-js/stargazers) – A curated list of awesome (functional) reactive programming stuff in JavaScript.
* [lucasviola/Awesome Functional Programming](https://github.com/lucasviola/awesome-functional-programming) [![GitHub stars](https://img.shields.io/github/stars/lucasviola/awesome-functional-programming?style=flat)](https://github.com/lucasviola/awesome-functional-programming/stargazers) – Awesome resources on functional programming theory and learning materials.
* [xgrommx/Awesome Functional Programming](https://github.com/xgrommx/awesome-functional-programming) [![GitHub stars](https://img.shields.io/github/stars/xgrommx/awesome-functional-programming?style=flat)](https://github.com/xgrommx/awesome-functional-programming/stargazers) – A ton of articles on functional programming, as well as a huge list of functional libraries for many programming languages.
* [Functional Programming Resources In JavaScript](https://github.com/busypeoples/functional-programming-javascript) [![GitHub stars](https://img.shields.io/github/stars/busypeoples/functional-programming-javascript?style=flat)](https://github.com/busypeoples/functional-programming-javascript/stargazers)
* [tk-learning-center/Functional Programming Learning Path](https://github.com/tk-learning-center/functional-programming-learning-path) [![GitHub stars](https://img.shields.io/github/stars/tk-learning-center/functional-programming-learning-path?style=flat)](https://github.com/tk-learning-center/functional-programming-learning-path/stargazers) - A Learning Path for Functional Programming

### Talk

* [Functional Programming Slack channel](https://fpslack.com/) – Community with a friendly channel for JavaScript as well as many other channels about functional programming in general.


## Contribution

:star: Suggestions and PRs are welcome! :star:

Please read the [contribution guidelines](./contributing.md) to get started.

## License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Christoph Hermann](http://stoeffel.github.io/) has waived all copyright and related or neighboring rights to this work.
