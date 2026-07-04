# Tiny JS

> 来源：[thoughtspile/awesome-tiny-js](https://github.com/thoughtspile/awesome-tiny-js)

[![GitHub stars](https://img.shields.io/github/stars/thoughtspile/awesome-tiny-js?style=flat)](https://github.com/thoughtspile/awesome-tiny-js/stargazers)

# Awesome Tiny JS [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

<div align="center">
  <a href="https://github.com/thoughtspile/awesome-tiny-js#readme">
    <img src="./awesome-logo.png" width="300" height="207">
  </a>
</div>

Tiny front-end libraries to put your bundle on a diet. Rules:

- Size is under 2 kB-ish, min + gzip, with all dependencies, except where noted.
- For multi-purpose libraries, the size of a useful subset must be under 2 kB-ish.
- Useful client-side. I haven't figured out participation rules for node-only libraries, and I'm not too worried about them.
- Second-level libraries only allowed for React, Vue, Angular, svelte. 
- 100+ GitHub stars _or_ 500+ weekly npm installs to focus on tools with some community review.
- No zero-JS (CSS- or type-only) libraries. It's not awesome-css or something.

## Contents

- [UI Frameworks](#ui-frameworks)
- [Event Emitters](#event-emitters)
- [State Managers](#state-managers)
  - [Signals](#signals)
  - [Reactive Programming](#reactive-programming)
- [Routers and URL Utils](#routers-and-url-utils)
- [API Layer](#api-layer)
- [I18N](#i18n)
- [Dates and Time](#dates-and-time)
- [Generic Utilities](#generic-utilities)
- [Validation](#validation)
- [Unique ID Generation](#unique-id-generation)
- [Colors](#colors)
- [Touch Gestures](#touch-gestures)
- [Text Search](#text-search)

## UI Frameworks

UI frameworks (libraries?) provide declarative templates, event bindings, and observable state to update the view. I've been generous and expanded the size limit for this category to 4.5 kB (if you're boring, count them as 2 libraries), but also increased the star limit to 2K. 

- [preact](https://github.com/preactjs/preact) [![GitHub stars](https://img.shields.io/github/stars/preactjs/preact?style=flat)](https://github.com/preactjs/preact/stargazers) - React-like API (pre-hooks). Cool ecosystem of similarly tiny tools and components. Highly recommended. <img align="top" height="24" src="./img/preact.svg">

The following libraries are small and cool, but note they're about [500x less popular than preact.](https://npmtrends.com/preact-vs-hyperapp-vs-redom) Kudos for deconstrucing the very essence of a "framework":

- [hyperapp](https://github.com/jorgebucaran/hyperapp) [![GitHub stars](https://img.shields.io/github/stars/jorgebucaran/hyperapp?style=flat)](https://github.com/jorgebucaran/hyperapp/stargazers) - vDOM framework with pure JS syntax and immutable state, <img align="top" height="24" src="./img/hyperapp.svg">
- [redom](https://github.com/redom/redom) [![GitHub stars](https://img.shields.io/github/stars/redom/redom?style=flat)](https://github.com/redom/redom/stargazers) - Hyperapp-style templates with _imperative_ event listeners and updates, <img align="top" height="24" src="./img/redom.svg">

Now, for the [openly experimental](https://npmtrends.com/@arrow-js/core-vs-fre-vs-hyperapp-vs-redom-vs-superfine-vs-vanjs-core) UI libraries:

- [fre](https://github.com/frejs/fre) [![GitHub stars](https://img.shields.io/github/stars/frejs/fre?style=flat)](https://github.com/frejs/fre/stargazers) - React-like library with hooks and concurrency, <img align="top" height="24" src="./img/fre.svg">
- [van](https://github.com/vanjs-org/van) [![GitHub stars](https://img.shields.io/github/stars/vanjs-org/van?style=flat)](https://github.com/vanjs-org/van/stargazers) - vDOM-based framework optimized for no-build setups, <img align="top" height="24" src="./img/vanjs-core.svg">
- [superfine](https://github.com/jorgebucaran/superfine) [![GitHub stars](https://img.shields.io/github/stars/jorgebucaran/superfine?style=flat)](https://github.com/jorgebucaran/superfine/stargazers) - Hyperapp with state & effect hooks removed, <img align="top" height="24" src="./img/superfine.svg">
- [arrowjs](https://github.com/justin-schroeder/arrow-js) [![GitHub stars](https://img.shields.io/github/stars/justin-schroeder/arrow-js?style=flat)](https://github.com/justin-schroeder/arrow-js/stargazers) - Tagged templates + reactive data, <img align="top" height="24" src="./img/arrow-jscore.svg">

And if being declarative is not your thing:

- [umbrella](https://github.com/franciscop/umbrella) [![GitHub stars](https://img.shields.io/github/stars/franciscop/umbrella?style=flat)](https://github.com/franciscop/umbrella/stargazers) - jQuery-style DOM manipulation library, <img align="top" height="24" src="./img/umbrellajs.svg">

## Event Emitters

Event emitter pattern is fairly easy to implement yourself, but why bother when you have these cool tools? With an arms race to build the smallest one, the limit is 0.5 kB.

- [mitt](https://github.com/developit/mitt) [![GitHub stars](https://img.shields.io/github/stars/developit/mitt?style=flat)](https://github.com/developit/mitt/stargazers) - Plain event emitter that I use on most projects, <img align="top" height="24" src="./img/mitt.svg">
- [nanoevents](https://github.com/ai/nanoevents) [![GitHub stars](https://img.shields.io/github/stars/ai/nanoevents?style=flat)](https://github.com/ai/nanoevents/stargazers) - Nicer unsubscribe API, but no `*` event, <img align="top" height="24" src="./img/nanoevents.svg">
- [onfire.js](https://github.com/hustcc/onfire.js) [![GitHub stars](https://img.shields.io/github/stars/hustcc/onfire.js?style=flat)](https://github.com/hustcc/onfire.js/stargazers) - Also has `.once` method, <img align="top" height="24" src="./img/onfirejs.svg">

## State Managers

State managers combine observable state with actions and framework bindings, intended for app-wide state.

- [zustand](https://github.com/pmndrs/zustand) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/zustand?style=flat)](https://github.com/pmndrs/zustand/stargazers) - Simple stores with pleasant actions and selectors. Vanilla <img align="top" height="24" src="./img/zustandvanilla.svg">, React <img align="top" height="24" src="./img/zustand.svg">
- [nanostores](https://github.com/nanostores/nanostores) [![GitHub stars](https://img.shields.io/github/stars/nanostores/nanostores?style=flat)](https://github.com/nanostores/nanostores/stargazers) - Modular store with good tree-shaking support, <img align="top" height="24" src="./img/nanostores.svg"> vanilla, + React <img align="top" height="24" src="./img/nanostoresreact.svg"> extra. Supports all the top frameworks.
- [exome](https://github.com/marcisbee/exome) [![GitHub stars](https://img.shields.io/github/stars/marcisbee/exome?style=flat)](https://github.com/marcisbee/exome/stargazers) - Atomic stores with lots of framework connectors, <img align="top" height="24" src="./img/exome.svg"> + React <img align="top" height="24" src="./img/exomereact.svg"> extra. Supports all the top frameworks.
- [storeon](https://github.com/storeon/storeon) [![GitHub stars](https://img.shields.io/github/stars/storeon/storeon?style=flat)](https://github.com/storeon/storeon/stargazers) - Minimal redux-styled store with lots of framework connectors, <img align="top" height="24" src="./img/storeon.svg">. React extra <img align="top" height="24" src="./img/storeonreact.svg"> + Vue, Svelte, Angular.
- [unistore](https://github.com/developit/unistore) [![GitHub stars](https://img.shields.io/github/stars/developit/unistore?style=flat)](https://github.com/developit/unistore/stargazers) - Centralized store with actions, <img align="top" height="24" src="./img/unistore.svg"> + React <img align="top" height="24" src="./img/unistorereact.svg">
- [teaful](https://github.com/teafuljs/teaful) [![GitHub stars](https://img.shields.io/github/stars/teafuljs/teaful?style=flat)](https://github.com/teafuljs/teaful/stargazers) - Store with useState-like API, <img align="top" height="24" src="./img/teaful.svg">, including React / preact connector.

### Signals

A signal-styled state manager provides observable values (aka _signals_), derived values and effects.

- [@preact/signals](https://github.com/preactjs/signals) [![GitHub stars](https://img.shields.io/github/stars/preactjs/signals?style=flat)](https://github.com/preactjs/signals/stargazers) - The OG signals from preact <img align="top" height="24" src="./img/preactsignals-core.svg"> core, <img align="top" height="24" src="./img/preactsignals-react.svg"> with react integration.
- [usignal](https://github.com/WebReflection/usignal) [![GitHub stars](https://img.shields.io/github/stars/WebReflection/usignal?style=flat)](https://github.com/WebReflection/usignal/stargazers) - A smaller signal implementation, <img align="top" height="24" src="./img/usignal.svg">
- [hyperactiv](https://github.com/elbywan/hyperactiv) [![GitHub stars](https://img.shields.io/github/stars/elbywan/hyperactiv?style=flat)](https://github.com/elbywan/hyperactiv/stargazers) - 4 functions to make objects observable and listen to changes, <img align="top" height="24" src="./img/hyperactiv.svg">
- [flimsy](https://github.com/fabiospampinato/flimsy) [![GitHub stars](https://img.shields.io/github/stars/fabiospampinato/flimsy?style=flat)](https://github.com/fabiospampinato/flimsy/stargazers) - Signals from Solid (it _almost_ fit into UI frameworks category itself). Author warning: _it's probably buggy._ <img align="top" height="24" src="./img/flimsy.svg">

Honorable mention: [oby](https://github.com/vobyjs/oby) [![GitHub stars](https://img.shields.io/github/stars/vobyjs/oby?style=flat)](https://github.com/vobyjs/oby/stargazers) _could_ make it _if_ it had tree-shaking, but otherwise is around 7 kB.

### Reactive Programming

Another well-known state management approach is reactive programmning — operating on event streams, applying filters and transforms to end up with an observable value. Think RxJS, but tiny:

- [flyd](https://github.com/paldepind/flyd) [![GitHub stars](https://img.shields.io/github/stars/paldepind/flyd?style=flat)](https://github.com/paldepind/flyd/stargazers) - Rx-styled event streams, <img align="top" height="24" src="./img/flyd.svg">
- [callbag-basics](https://github.com/staltz/callbag-basics) [![GitHub stars](https://img.shields.io/github/stars/staltz/callbag-basics?style=flat)](https://github.com/staltz/callbag-basics/stargazers) - Rx-style event streams, <img align="top" height="24" src="./img/callbag-basics.svg">

## Routers and URL Utils

Do stuff on URL / history changes, with path matching and parsing:

- [wouter](https://github.com/molefrog/wouter) [![GitHub stars](https://img.shields.io/github/stars/molefrog/wouter?style=flat)](https://github.com/molefrog/wouter/stargazers) - Declarative router for React / preact, <img align="top" height="24" src="./img/wouter.svg">, also available as a standalone hook: <img align="top" height="24" src="./img/wouteruse-browser-location.svg">
- [@nanostores/router](https://github.com/nanostores/router) [![GitHub stars](https://img.shields.io/github/stars/nanostores/router?style=flat)](https://github.com/nanostores/router/stargazers) - Routes as a nanostores store (framework-agnostic), <img align="top" height="24" src="./img/nanostoresrouter.svg">
- [navaid](https://github.com/lukeed/navaid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/navaid?style=flat)](https://github.com/lukeed/navaid/stargazers) - History-based observable router, <img align="top" height="24" src="./img/navaid.svg">

Just want to parse or match URL paths without observing them? Here you go:

- [matchit](https://github.com/lukeed/matchit) [![GitHub stars](https://img.shields.io/github/stars/lukeed/matchit?style=flat)](https://github.com/lukeed/matchit/stargazers) - Route parser and matcher in <img align="top" height="24" src="./img/matchit.svg">
- [regexparam](https://github.com/lukeed/regexparam) [![GitHub stars](https://img.shields.io/github/stars/lukeed/regexparam?style=flat)](https://github.com/lukeed/regexparam/stargazers) - Convert path to regexp in <img align="top" height="24" src="./img/regexparam.svg">
- [qss](https://github.com/lukeed/qss) [![GitHub stars](https://img.shields.io/github/stars/lukeed/qss?style=flat)](https://github.com/lukeed/qss/stargazers) - Parse querystrings in <img align="top" height="24" src="./img/qss.svg">. Not sure you need it, [URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL) support is good. 

## API Layer

`fetch` API has some boilerplate associated with it: serialize & parse data, reject on non-200 response, etc. These tiny packages handle it for you:

- [redaxios](https://github.com/developit/redaxios) [![GitHub stars](https://img.shields.io/github/stars/developit/redaxios?style=flat)](https://github.com/developit/redaxios/stargazers) - Drop-in axios replacement for modern browsers, <img align="top" height="24" src="./img/redaxios.svg">
- [wretch](https://github.com/elbywan/wretch) [![GitHub stars](https://img.shields.io/github/stars/elbywan/wretch?style=flat)](https://github.com/elbywan/wretch/stargazers) - Chainable API with error processing and lots of extra plugins, <img align="top" height="24" src="./img/wretch.svg">
- [gretchen](https://github.com/truework/gretchen) [![GitHub stars](https://img.shields.io/github/stars/truework/gretchen?style=flat)](https://github.com/truework/gretchen/stargazers) - Chainable API with type-safe errors, <img align="top" height="24" src="./img/gretchen.svg">

If for some reason you still need a fetch polyfill, try this one:

- [unfetch](https://github.com/developit/unfetch) [![GitHub stars](https://img.shields.io/github/stars/developit/unfetch?style=flat)](https://github.com/developit/unfetch/stargazers) - Loose fetch polyfill, <img align="top" height="24" src="./img/unfetch.svg">

## I18N

A map of strings might seem enough to translate an app, but these tools also handle interpolation and some extra goodies:

- [@nanostores/i18n](https://github.com/nanostores/i18n) [![GitHub stars](https://img.shields.io/github/stars/nanostores/i18n?style=flat)](https://github.com/nanostores/i18n/stargazers) - Detect locale, load dictionaries, format dates / numbers, <img align="top" height="24" src="./img/nanostoresin.svg"> including nanostores.
- [eo-locale](https://github.com/ibitcy/eo-locale) [![GitHub stars](https://img.shields.io/github/stars/ibitcy/eo-locale?style=flat)](https://github.com/ibitcy/eo-locale/stargazers) - Interpolation and dates / numbers, <img align="top" height="24" src="./img/eo-localecore.svg">, or <img align="top" height="24" src="./img/eo-localereact.svg"> with react bindings.
- [rosetta](https://github.com/lukeed/rosetta) [![GitHub stars](https://img.shields.io/github/stars/lukeed/rosetta?style=flat)](https://github.com/lukeed/rosetta/stargazers) - Bare-bones template strings (`{{hello}}, {{username}}`) and custom functions for everyting else, <img align="top" height="24" src="./img/rosetta.svg">
- [lingui](https://github.com/lingui/js-lingui) [![GitHub stars](https://img.shields.io/github/stars/lingui/js-lingui?style=flat)](https://github.com/lingui/js-lingui/stargazers) - Small core with template strings, <img align="top" height="24" src="./img/linguicore.svg">

## Dates and Time

Date and time manipulation in pure JS is verbose. Luckily, two of the top date libraries have sensible size:

- [date-fns](https://github.com/date-fns/date-fns/) [![GitHub stars](https://img.shields.io/github/stars/date-fns/date-fns/?style=flat)](https://github.com/date-fns/date-fns//stargazers) - Not tiny as a whole, but [most functions](https://bundlephobia.com/package/date-fns) are under 1 kB each (format and parse are quite heavy).
- [dayjs](https://github.com/iamkun/dayjs) [![GitHub stars](https://img.shields.io/github/stars/iamkun/dayjs?style=flat)](https://github.com/iamkun/dayjs/stargazers) - _Almost_ moment.js-compatible API, covers most use cases, <img align="top" height="24" src="./img/dayjsesm.svg">

And some more packages that only do formatting:

- [tinytime](https://github.com/aweary/tinytime) [![GitHub stars](https://img.shields.io/github/stars/aweary/tinytime?style=flat)](https://github.com/aweary/tinytime/stargazers) - Simple date / time formatter: `{h}:{mm} -> 9:33`, <img align="top" height="24" src="./img/tinytime.svg">
- [tinydate](https://github.com/lukeed/tinydate) [![GitHub stars](https://img.shields.io/github/stars/lukeed/tinydate?style=flat)](https://github.com/lukeed/tinydate/stargazers) - Date / time formatter, only supports padded numeric output (`September -> 09`), <img align="top" height="24" src="./img/tinydate.svg">
- [time-stamp](https://github.com/jonschlinkert/time-stamp) [![GitHub stars](https://img.shields.io/github/stars/jonschlinkert/time-stamp?style=flat)](https://github.com/jonschlinkert/time-stamp/stargazers) - More of the same, <img align="top" height="24" src="./img/time-stamp.svg">
- [ms](https://github.com/vercel/ms) [![GitHub stars](https://img.shields.io/github/stars/vercel/ms?style=flat)](https://github.com/vercel/ms/stargazers) - Parse & format ms durations, e.g. `"1m" <-> 60000`, <img align="top" height="24" src="./img/ms.svg">
- [timeago.js](https://github.com/hustcc/timeago.js) [![GitHub stars](https://img.shields.io/github/stars/hustcc/timeago.js?style=flat)](https://github.com/hustcc/timeago.js/stargazers) - Format dates into stuff like _X minutes ago_ or _in X hours,_ <img align="top" height="24" src="./img/timeagojs.svg">
- [fromnow](https://github.com/lukeed/fromnow) [![GitHub stars](https://img.shields.io/github/stars/lukeed/fromnow?style=flat)](https://github.com/lukeed/fromnow/stargazers) - More of the same, <img align="top" height="24" src="./img/fromnow.svg">

Note that the built-in [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat) has decent support.

## Generic Utilities

Something you'd find in lodash or ramda, but smaller. Most are pretty similar and very small, with minor differences in package structure (single / package-per-helper) and tree shaking vs direct helper import.

- [remeda](https://github.com/remeda/remeda) [![GitHub stars](https://img.shields.io/github/stars/remeda/remeda?style=flat)](https://github.com/remeda/remeda/stargazers) - 90 tree-shakable helpers [(list).](https://bundlephobia.com/package/remeda)
- [rambda](https://github.com/selfrefactor/rambda) [![GitHub stars](https://img.shields.io/github/stars/selfrefactor/rambda?style=flat)](https://github.com/selfrefactor/rambda/stargazers) - 187 tree-shakable helpers [(list).](https://bundlephobia.com/package/rambda)
- [just](https://github.com/angus-c/just) [![GitHub stars](https://img.shields.io/github/stars/angus-c/just?style=flat)](https://github.com/angus-c/just/stargazers) - 82 helpers in separate packages [(list).](https://anguscroll.com/just/)
- [@fxts/core](https://github.com/marpple/FxTS) [![GitHub stars](https://img.shields.io/github/stars/marpple/FxTS?style=flat)](https://github.com/marpple/FxTS/stargazers) - 96 tree-shakable helpers. Lazy evaluation support.

Honorable mention: [underscore,](https://github.com/jashkenas/underscore) [![GitHub stars](https://img.shields.io/github/stars/jashkenas/underscore?style=flat)](https://github.com/jashkenas/underscore/stargazers) contains many sub-1 kB helpers. It does not tree-shake as well as the libraries above due to codebase structure.

Note: lodash itself is not tree-shakable, but has made many attempts at modulaity with `lodash.method` packages, imports from `lodash/method`, and `lodash-es`, none of which work well in practice.

Also note that much of the original lodash functionality comes built-in with modern ES. Prefer native versions over libraries as your browser target allows.

## Validation

To check if an object matches an expected schema, you'd often use zod, yup, joi or ajv. But 90% of the time you can get what you need in under 2 kB. _Note:_ I compare a base validation subset (core + object / array + string / number / boolean) under tree-shaking to avoid punishing libs that have more features.

- [v8n](https://github.com/imbrn/v8n) [![GitHub stars](https://img.shields.io/github/stars/imbrn/v8n?style=flat)](https://github.com/imbrn/v8n/stargazers) - zod-style API with fine-grained checks: `v8n().string().minLength(5).first("H").last("o")`. No tree shaking, <img align="top" height="24" src="./img/vn.svg">
- [banditypes](https://github.com/thoughtspile/banditypes) [![GitHub stars](https://img.shields.io/github/stars/thoughtspile/banditypes?style=flat)](https://github.com/thoughtspile/banditypes/stargazers) - The smallest validation library: <img align="top" height="24" src="./img/banditypes.svg">
- [superstruct](https://github.com/ianstormtaylor/superstruct) [![GitHub stars](https://img.shields.io/github/stars/ianstormtaylor/superstruct?style=flat)](https://github.com/ianstormtaylor/superstruct/stargazers) - The most popular modular validation library with good tree-shaking, <img align="top" height="24" src="./img/superstruct.svg">
- [valibot](https://github.com/fabian-hiller/valibot) [![GitHub stars](https://img.shields.io/github/stars/fabian-hiller/valibot?style=flat)](https://github.com/fabian-hiller/valibot/stargazers) - Another modular validation library, <img align="top" height="24" src="./img/valibot.svg">
- [deep-waters](https://github.com/antonioru/deep-waters) [![GitHub stars](https://img.shields.io/github/stars/antonioru/deep-waters?style=flat)](https://github.com/antonioru/deep-waters/stargazers) - Composable functional validators, <img align="top" height="24" src="./img/deep-waterscompose-deep-watershasShape-deep-watersarrayOf-deep-watersisString-deep-watersisNumber-deep-watersisBoolean.svg">.

## Unique ID Generation

Unique ID generation does not take a lot of code, but it's not someting I'd want to write myself. Limit is 500 bytes. Also note that the [native `crypto.randomUUID`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) has [OK support.](https://caniuse.com/mdn-api_crypto_randomuuid)

- [@lukeed/uuid](https://github.com/lukeed/uuid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/uuid?style=flat)](https://github.com/lukeed/uuid/stargazers) - Real UUIDs, <img align="top" height="24" src="./img/lukeeduuid.svg">
- [nanoid](https://github.com/ai/nanoid) [![GitHub stars](https://img.shields.io/github/stars/ai/nanoid?style=flat)](https://github.com/ai/nanoid/stargazers) - Random IDs with larger alphabet, <img align="top" height="24" src="./img/nanoid.svg">
- [uid](https://github.com/lukeed/uid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/uid?style=flat)](https://github.com/lukeed/uid/stargazers) - More of the same, <img align="top" height="24" src="./img/uid.svg">
- [hexoid](https://github.com/lukeed/hexoid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/hexoid?style=flat)](https://github.com/lukeed/hexoid/stargazers) - Hexadecimal IDs, <img align="top" height="24" src="./img/hexoid.svg">

## Colors

Color manipulation is rare in pure UI development, but very helpful for data visualization, and uses [freaky math.](https://en.wikipedia.org/wiki/HSL_and_HSV#Color_conversion_formulae) Don't fry your brain, take these:

- [colord](https://github.com/omgovich/colord) [![GitHub stars](https://img.shields.io/github/stars/omgovich/colord?style=flat)](https://github.com/omgovich/colord/stargazers) - Manipulate colors and convert between spaces, <img align="top" height="24" src="./img/colord.svg">. Extra features come as plugins, 150b to 1.5 kB each.
- [colr](https://github.com/stayradiated/colr) [![GitHub stars](https://img.shields.io/github/stars/stayradiated/colr?style=flat)](https://github.com/stayradiated/colr/stargazers) - More of the same, <img align="top" height="24" src="./img/colr.svg" >
- [polychrome](https://github.com/cdonohue/polychrome) [![GitHub stars](https://img.shields.io/github/stars/cdonohue/polychrome?style=flat)](https://github.com/cdonohue/polychrome/stargazers) - More of the same, <img align="top" height="24" src="./img/polychrome.svg">
- [randomcolor](https://github.com/davidmerfield/randomColor) [![GitHub stars](https://img.shields.io/github/stars/davidmerfield/randomColor?style=flat)](https://github.com/davidmerfield/randomColor/stargazers) - Attractive random colors with configuration. <img align="top" height="24" src="./img/randomcolor.svg">

## Touch Gestures

Touch gestures like swipe, drag, pinch or doubletap are a staple of mobile UX, but recognizing a series of touchmove / pointer events as a gesture is tricky, and testing is painful. Here are two libraries that do the heavy lifting for you:

- [alloyfinger](https://github.com/AlloyTeam/AlloyFinger) [![GitHub stars](https://img.shields.io/github/stars/AlloyTeam/AlloyFinger?style=flat)](https://github.com/AlloyTeam/AlloyFinger/stargazers) - Pan, swipe, tap, doubletap, longpress, _and_ pinch / rotate. My personal favorite. <img align="top" height="24" src="./img/alloyfinger.svg">.
- [tinygesture](https://github.com/sciactive/tinygesture) [![GitHub stars](https://img.shields.io/github/stars/sciactive/tinygesture?style=flat)](https://github.com/sciactive/tinygesture/stargazers) - Configurable pan, swipe, tap, doubletap, longpress. <img align="top" height="24" src="./img/tinygesture.svg">.

Even if you want to detect gestures yourself, juggling mouse, touch and pointer events is hard enough, and browser inconsistencies don't help. Here are two more libraries to assist with that:

- [pointer-tracker](https://github.com/GoogleChromeLabs/pointer-tracker) [![GitHub stars](https://img.shields.io/github/stars/GoogleChromeLabs/pointer-tracker?style=flat)](https://github.com/GoogleChromeLabs/pointer-tracker/stargazers) - Unified interface for mouse, touch and pointer events, <img align="top" height="24" src="./img/pointer-tracker.svg">
- [detect-it](https://github.com/rafgraph/detect-it) [![GitHub stars](https://img.shields.io/github/stars/rafgraph/detect-it?style=flat)](https://github.com/rafgraph/detect-it/stargazers) - Detect present and primary input method (touch / mouse) and supported events, <img align="top" height="24" src="./img/detect-it.svg">

Honorable mentions: [any-touch](https://github.com/any86/any-touch) [![GitHub stars](https://img.shields.io/github/stars/any86/any-touch?style=flat)](https://github.com/any86/any-touch/stargazers) attempts a modular approach to gesture detection, but the core is around 2 kB without any gesture recognizers. [rc-gesture,](https://github.com/react-component/gesture) [![GitHub stars](https://img.shields.io/github/stars/react-component/gesture?style=flat)](https://github.com/react-component/gesture/stargazers) used in ant design system, could be the only react component on the list, but babel-runtime / corejs polyfills hard-wired into the build push the ~2.5 kB size to over 10 kB.

## Text Search

Text search is important for client-side filtering and autosuggests. Naive `option.includes(search)` has no sensible order on the results, and ignoring word boundaries gives unexpected matches like _spa -> newSPAper._ First, here are some libraries that prioritize word matches:

- [js-search](https://github.com/bvaughn/js-search) [![GitHub stars](https://img.shields.io/github/stars/bvaughn/js-search?style=flat)](https://github.com/bvaughn/js-search/stargazers) - Feature-rich and customizable: multi-field indices, stop words, custom stemmers and tokenizers. <img align="top" height="24" src="./img/js-search.svg">
- [ndx](https://github.com/localvoid/ndx) [![GitHub stars](https://img.shields.io/github/stars/localvoid/ndx?style=flat)](https://github.com/localvoid/ndx/stargazers) - Similar to js-search, differs in [ranking](https://kmwllc.com/index.php/2020/03/20/understanding-tf-idf-and-bm-25/) and is less strict for multi-word queries [(compare)](https://leeoniya.github.io/uFuzzy/demos/compare.html?libs=js-search,ndx,Wade&search=twilight%20sag). Supports field weights. <img align="top" height="24" src="./img/ndx-ndxquery.svg">
- [wade](https://github.com/kbrsh/wade) [![GitHub stars](https://img.shields.io/github/stars/kbrsh/wade?style=flat)](https://github.com/kbrsh/wade/stargazers) - Also similar, [(compare)](https://leeoniya.github.io/uFuzzy/demos/compare.html?libs=js-search,Wade,ndx&search=twilight%20sag) <img align="top" height="24" src="./img/wade.svg">
- [libsearch](https://github.com/thesephist/libsearch) [![GitHub stars](https://img.shields.io/github/stars/thesephist/libsearch?style=flat)](https://github.com/thesephist/libsearch/stargazers) - Index-free search (slower, but easier to use) with sane ordering <img align="top" height="24" src="./img/libsearch.svg">

One way to find sensible inexact matches is _stemming_ — converting words to a root form. _Walked_ will match _walking,_ etc. Here are a few [Porter stemmers](https://vijinimallawaarachchi.com/2017/05/09/porter-stemming-algorithm/) for English language:

- [stemmer](https://github.com/words/stemmer) [![GitHub stars](https://img.shields.io/github/stars/words/stemmer?style=flat)](https://github.com/words/stemmer/stargazers) - <img align="top" height="24" src="./img/stemmer.svg">
- [porter-stemmer](https://github.com/jedp/porter-stemmer) [![GitHub stars](https://img.shields.io/github/stars/jedp/porter-stemmer?style=flat)](https://github.com/jedp/porter-stemmer/stargazers) - <img align="top" height="24" src="./img/porter-stemmer.svg">

For non-English words, I only have honorable mentions: [snowball-js](https://github.com/fortnightlabs/snowball-js) [![GitHub stars](https://img.shields.io/github/stars/fortnightlabs/snowball-js?style=flat)](https://github.com/fortnightlabs/snowball-js/stargazers) is 17 kB with 15 languages, [lunr-languages](https://github.com/MihaiValentin/lunr-languages) [![GitHub stars](https://img.shields.io/github/stars/MihaiValentin/lunr-languages?style=flat)](https://github.com/MihaiValentin/lunr-languages/stargazers) supports 30 languages but only works with [lunr,](https://github.com/olivernn/lunr.js) [![GitHub stars](https://img.shields.io/github/stars/olivernn/lunr.js?style=flat)](https://github.com/olivernn/lunr.js/stargazers) the most promising one is [natural](https://github.com/NaturalNode/natural/tree/master/lib/natural/stemmers) [![GitHub stars](https://img.shields.io/github/stars/NaturalNode/natural/tree/master/lib/natural/stemmers?style=flat)](https://github.com/NaturalNode/natural/tree/master/lib/natural/stemmers/stargazers) but it depends on Node.js.

### Fuzzy search

__Fuzzy search__ is another take on inexact matching — the words can be modified. First, we have libraries that only allow insertion: spacecat -> SPACECrAfT. Not perfect for general-purpose text search, but great for filename, command, or URL lookups.

- [fuzzy](https://github.com/mattyork/fuzzy) [![GitHub stars](https://img.shields.io/github/stars/mattyork/fuzzy?style=flat)](https://github.com/mattyork/fuzzy/stargazers) - Index-free, can highlight matches. <img align="top" height="24" src="./img/fuzzy.svg">
- [fuzzy-search](https://github.com/wouterrutgers/fuzzy-search) [![GitHub stars](https://img.shields.io/github/stars/wouterrutgers/fuzzy-search?style=flat)](https://github.com/wouterrutgers/fuzzy-search/stargazers) - With stateful index. <img align="top" height="24" src="./img/fuzzy-search.svg">
- [fzy.js](https://github.com/jhawthorn/fzy.js) [![GitHub stars](https://img.shields.io/github/stars/jhawthorn/fzy.js?style=flat)](https://github.com/jhawthorn/fzy.js/stargazers) - Matches one string at a time, tree-shakeable scores and match highlighting. <img align="top" height="24" src="./img/fzyjs.svg"> total, or ~150 bytes for `hasMatch` only.
- [fuzzysearch](https://github.com/bevacqua/fuzzysearch) [![GitHub stars](https://img.shields.io/github/stars/bevacqua/fuzzysearch?style=flat)](https://github.com/bevacqua/fuzzysearch/stargazers) -  One string at a time, does not compute score / rank. <img align="top" height="24" src="./img/fuzzysearch.svg">
- [liquidmetal](https://github.com/rmm5t/liquidmetal) [![GitHub stars](https://img.shields.io/github/stars/rmm5t/liquidmetal?style=flat)](https://github.com/rmm5t/liquidmetal/stargazers) - Quicksilver algorithm, prioritizes matches at start of word for command abbreviations (e.g. `gp` -> `git push`). One string at a time. <img align="top" height="24" src="./img/liquidmetal.svg">
- [quick-score](https://github.com/fwextensions/quick-score) [![GitHub stars](https://img.shields.io/github/stars/fwextensions/quick-score?style=flat)](https://github.com/fwextensions/quick-score/stargazers) - Another quicksilver-based lib, tweaked for long strings. Built-in list filtering and sorting, <img align="top" height="24" src="./img/quick-score.svg"> or 1.2 kB for single-string scoring.

Finally, one library is specifically built for spellchecking:

- [fuzzyset](https://github.com/Glench/fuzzyset.js) [![GitHub stars](https://img.shields.io/github/stars/Glench/fuzzyset.js?style=flat)](https://github.com/Glench/fuzzyset.js/stargazers) - Find misspellings, e.g. missipissi -> Missisipi, <img align="top" height="24" src="./img/fuzzyset.svg"> Commercial usage costs $42.


## Contributing

Suggestions welcome! See [contributing.md](contributing.md), or drop an [issue](https://github.com/thoughtspile/awesome-tiny-js/issues).

## Footnotes

See [WIP](wip.md) for possibly awesome libraries I have found, but not yet analyzed deeply, and [incubate](incubate.md) for awesome libraries that don't meet popularity criteria yet.

Collected and reviewed by [Vladimir Klepov](https://blog.thoughtspile.tech) in 2023.
