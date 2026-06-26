# Tiny JS

[![GitHub stars](https://img.shields.io/github/stars/thoughtspile/awesome-tiny-js?style=flat)](https://github.com/thoughtspile/awesome-tiny-js/stargazers)

# Awesome Tiny JS [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A collection of tiny JS libraries to put your bundle on a diet. Curated by [Vladimir Klepov](https://blog.thoughtspile.tech) Rules:

- Size is under 2Kb-ish, min + gzip, with all deps, except where noted.
- For multi-purpose libraries, the size of a useful subset must be under 2Kb-ish.
- Second-level libraries only allowed for React, Vue, Angular, svelte. 
- Useful client-side. I haven't figured out participation rules for node-only libraries, and I'm not too worried about them.
- 100+ GitHub stars. Adding every obsure library will dilute the list.
- No zero-JS (CSS- or type-only) libraries. It's not awesome-css or something.

Disclaimers:

- Most framework-specific libraries are for React, because that's what I'm familiar with.

## Contents

- [UI Frameworks](#ui-frameworks)
- [Event Emitters](#event-emitters)
- [Reactive Programming](#reactive-programming)
- [State Managers](#state-managers)
- [Routers and URL Utils](#routers-and-url-utils)
- [API Layer](#api-layer)
- [I18N](#i18n)
- [Dates and Time](#dates-and-time)
- [Generic Utilities](#generic-utilities)
- [Unique ID Generation](#unique-id-generation)
- [Colors](#colors)
- [To be Continued](#to-be-continued)

## UI Frameworks

UI frameworks (libraries?) provide declarative templates, event bindings, and observable state to update the view. I've been generous and expanded the size limit for this category to 4Kb, but also increased the star limit to 3K. 

- [preact](https://github.com/preactjs/preact) [![GitHub stars](https://img.shields.io/github/stars/preactjs/preact?style=flat)](https://github.com/preactjs/preact/stargazers) - React-like API (pre-hooks) in 4Kb. Cool ecosystem of similarly tiny tools and components. Highly recommended.

The following libraries are small and cool, but note they're about [500x less popular than preact.](https://npmtrends.com/fre-vs-hyperapp-vs-million-vs-preact-vs-redom-vs-riot) Kudos for deconstrucing the very essence of a "framework":

- [million](https://github.com/aidenybai/million) [![GitHub stars](https://img.shields.io/github/stars/aidenybai/million?style=flat)](https://github.com/aidenybai/million/stargazers) - Marketed as a _drop-in replacement for React,_ but in under 2Kb.
- [fre](https://github.com/frejs/fre) [![GitHub stars](https://img.shields.io/github/stars/frejs/fre?style=flat)](https://github.com/frejs/fre/stargazers) - React-like library with hooks and concurrency, 1–3Kb.
- [hyperapp](https://github.com/jorgebucaran/hyperapp) [![GitHub stars](https://img.shields.io/github/stars/jorgebucaran/hyperapp?style=flat)](https://github.com/jorgebucaran/hyperapp/stargazers) - Declarative UI with pure JS syntax and immutable state, under 2Kb.
- [redom](https://github.com/redom/redom) [![GitHub stars](https://img.shields.io/github/stars/redom/redom?style=flat)](https://github.com/redom/redom/stargazers) - Hyperapp-style templates with _imperative_ event listeners and updates, around 2Kb.

And if being declarative is not your thing:

- [umbrella](https://github.com/franciscop/umbrella) [![GitHub stars](https://img.shields.io/github/stars/franciscop/umbrella?style=flat)](https://github.com/franciscop/umbrella/stargazers) - jQuery-style DOM manipulation library in 3Kb.

## Event Emitters

Event emitter pattern is fairly easy to implement yourself, but why bother when you have these cool tools? With an arms race to build the smallest one, the limit is 0.5Kb.

- [mitt](https://github.com/developit/mitt) [![GitHub stars](https://img.shields.io/github/stars/developit/mitt?style=flat)](https://github.com/developit/mitt/stargazers) - 200-byte emitter. I use it on most projects.
- [nanoevents](https://github.com/ai/nanoevents) [![GitHub stars](https://img.shields.io/github/stars/ai/nanoevents?style=flat)](https://github.com/ai/nanoevents/stargazers) - Smaller and with nicer unsubscribe API, but no '*' event.
- [eev](https://github.com/chrisdavies/eev) [![GitHub stars](https://img.shields.io/github/stars/chrisdavies/eev?style=flat)](https://github.com/chrisdavies/eev/stargazers) - More of the same in 500b.
- [onfire.js](https://github.com/hustcc/onfire.js) [![GitHub stars](https://img.shields.io/github/stars/hustcc/onfire.js?style=flat)](https://github.com/hustcc/onfire.js/stargazers) - 500b, but has `.once`.

## Reactive Programming

A step up from a raw event emitter, reactive libraries can build chains of event transforms, filters, and side-effects. You can already use these to build UIs by manually updating DOM on state change:

- [flyd](https://github.com/paldepind/flyd) [![GitHub stars](https://img.shields.io/github/stars/paldepind/flyd?style=flat)](https://github.com/paldepind/flyd/stargazers) - Rx-styled event streams in a 2Kb-ish package.
- [hyperactiv](https://github.com/elbywan/hyperactiv) [![GitHub stars](https://img.shields.io/github/stars/elbywan/hyperactiv?style=flat)](https://github.com/elbywan/hyperactiv/stargazers) - 4 functions to make objects observable and listen to changes, in 1Kb.
- [flimsy](https://github.com/fabiospampinato/flimsy) [![GitHub stars](https://img.shields.io/github/stars/fabiospampinato/flimsy?style=flat)](https://github.com/fabiospampinato/flimsy/stargazers) - 1Kb reactive core of solid.js that _almost_ fit into UI frameworks category. Author warning: _is probably buggier._

Honorable mentions: [callbag-basics](https://github.com/staltz/callbag-basics) [![GitHub stars](https://img.shields.io/github/stars/staltz/callbag-basics?style=flat)](https://github.com/staltz/callbag-basics/stargazers) and [oby](https://github.com/vobyjs/oby) [![GitHub stars](https://img.shields.io/github/stars/vobyjs/oby?style=flat)](https://github.com/vobyjs/oby/stargazers) _could_ make it _if_ they had tree-shaking, but otherwise are around 7Kb.

## State Managers

State managers combine observable state with actions and framework bindings, intended for app-wide state.

- [zustand](https://github.com/pmndrs/zustand) [![GitHub stars](https://img.shields.io/github/stars/pmndrs/zustand?style=flat)](https://github.com/pmndrs/zustand/stargazers) - ~1Kb store with pleasant actions and selectors. React / vanilla.
- [nanostores](https://github.com/nanostores/nanostores) [![GitHub stars](https://img.shields.io/github/stars/nanostores/nanostores?style=flat)](https://github.com/nanostores/nanostores/stargazers) - Modular store in sub-1Kb with lots of framework connectors.
- [reatom](https://github.com/artalar/reatom) [![GitHub stars](https://img.shields.io/github/stars/artalar/reatom?style=flat)](https://github.com/artalar/reatom/stargazers) — Reactive stores with a 2Kb core. React / svelte connectors cost extra.
- [storeon](https://github.com/storeon/storeon) [![GitHub stars](https://img.shields.io/github/stars/storeon/storeon?style=flat)](https://github.com/storeon/storeon/stargazers) - Minimal 400-byte redux-styled store. (p)react, has third-party connectors.
- [unistore](https://github.com/developit/unistore) [![GitHub stars](https://img.shields.io/github/stars/developit/unistore?style=flat)](https://github.com/developit/unistore/stargazers) - Sub-1Kb store with actions from preact developers, (p)react support.
- [teaful](https://github.com/teafuljs/teaful) [![GitHub stars](https://img.shields.io/github/stars/teafuljs/teaful?style=flat)](https://github.com/teafuljs/teaful/stargazers) - (p)react store with useState-like API in 1Kb.

## Routers and URL Utils

Do stuff on URL / history changes, with path matching and parsing:

- [wouter](https://github.com/molefrog/wouter) [![GitHub stars](https://img.shields.io/github/stars/molefrog/wouter?style=flat)](https://github.com/molefrog/wouter/stargazers) - Declarative routes for (p)react in 1.5Kb, or a 400-byte hook.
- [@nanostores/router](https://github.com/nanostores/router) [![GitHub stars](https://img.shields.io/github/stars/nanostores/router?style=flat)](https://github.com/nanostores/router/stargazers) - Routes as a nanostores store (framework-agnostic), sub-1Kb.
- [navaid](https://github.com/lukeed/navaid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/navaid?style=flat)](https://github.com/lukeed/navaid/stargazers) - History-based observable router, sub-1Kb.
- [routie](https://github.com/jgallen23/routie) [![GitHub stars](https://img.shields.io/github/stars/jgallen23/routie?style=flat)](https://github.com/jgallen23/routie/stargazers) - Hash-based observable router, sub-1Kb.

Just want to parse or match URL paths without observing them? Here you go:

- [matchit](https://github.com/lukeed/matchit) [![GitHub stars](https://img.shields.io/github/stars/lukeed/matchit?style=flat)](https://github.com/lukeed/matchit/stargazers) - Route parser and matcher, sub-1Kb.
- [regexparam](https://github.com/lukeed/regexparam) [![GitHub stars](https://img.shields.io/github/stars/lukeed/regexparam?style=flat)](https://github.com/lukeed/regexparam/stargazers) - Convert path to regexp in 400 bytes.
- [qss](https://github.com/lukeed/qss) [![GitHub stars](https://img.shields.io/github/stars/lukeed/qss?style=flat)](https://github.com/lukeed/qss/stargazers) - Parse querystrings in 300b. Not sure you need it, [URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL) support is good.

## API Layer

`fetch` API has some boilerplate associated with it: serialize & parse data, reject on non-200 response, etc. These tiny packages handle it for you:

- [redaxios](https://github.com/developit/redaxios) [![GitHub stars](https://img.shields.io/github/stars/developit/redaxios?style=flat)](https://github.com/developit/redaxios/stargazers) - Drop-in axios replacement in 800 bytes.
- [wretch](https://github.com/elbywan/wretch) [![GitHub stars](https://img.shields.io/github/stars/elbywan/wretch?style=flat)](https://github.com/elbywan/wretch/stargazers) - Chainable API with error processing in 2Kb, and lots of extra plugins.
- [gretchen](https://github.com/truework/gretchen) [![GitHub stars](https://img.shields.io/github/stars/truework/gretchen?style=flat)](https://github.com/truework/gretchen/stargazers) - Chainable API with type-safe errors in 2Kb.

If for some reason you still need a fetch polyfill, try this one:

- [unfetch](https://github.com/developit/unfetch) [![GitHub stars](https://img.shields.io/github/stars/developit/unfetch?style=flat)](https://github.com/developit/unfetch/stargazers) - Loose fetch polyfill in 500 bytes.

## I18N

A map of strings might seem enough to translate an app, but these tools also handle interpolation and some extra goodies:

- [@nanostores/i18n](https://github.com/nanostores/i18n) [![GitHub stars](https://img.shields.io/github/stars/nanostores/i18n?style=flat)](https://github.com/nanostores/i18n/stargazers) - Detect locale, load dictionaries, format dates / numbers in sub-1Kb.
- [rosetta](https://github.com/lukeed/rosetta) [![GitHub stars](https://img.shields.io/github/stars/lukeed/rosetta?style=flat)](https://github.com/lukeed/rosetta/stargazers) - Bare-bones interpolation in 300 bytes.
- [lingui](https://github.com/lingui/js-lingui) [![GitHub stars](https://img.shields.io/github/stars/lingui/js-lingui?style=flat)](https://github.com/lingui/js-lingui/stargazers) - 1.7Kb core with template strings and optional react connector. babel-depenent.
- [eo-locale](https://github.com/ibitcy/eo-locale) [![GitHub stars](https://img.shields.io/github/stars/ibitcy/eo-locale?style=flat)](https://github.com/ibitcy/eo-locale/stargazers) - Interpolation & dates / numbers in under 2Kb, including react bindings.

## Dates and Time

Date and time manipulation in pure JS is quite verbose. Luckily, two of the top date libraries have sensible size:

- [date-fns](https://github.com/date-fns/date-fns/) [![GitHub stars](https://img.shields.io/github/stars/date-fns/date-fns/?style=flat)](https://github.com/date-fns/date-fns//stargazers) - Not tiny as a whole, but most functions are under 1Kb each (`format` is quite heavy).
- [dayjs](https://github.com/iamkun/dayjs) [![GitHub stars](https://img.shields.io/github/stars/iamkun/dayjs?style=flat)](https://github.com/iamkun/dayjs/stargazers) - 2Kb-ish library with _alomost_ moment.js-compatible API, covers most use cases.

And here are some more packages that only do formatting:

- [tinytime](https://github.com/aweary/tinytime) [![GitHub stars](https://img.shields.io/github/stars/aweary/tinytime?style=flat)](https://github.com/aweary/tinytime/stargazers) - Simple 1Kb date formatter, like `{h}:{mm} -> 9:33`.
- [tinydate](https://github.com/lukeed/tinydate) [![GitHub stars](https://img.shields.io/github/stars/lukeed/tinydate?style=flat)](https://github.com/lukeed/tinydate/stargazers) - 400-byte date formatter, only supports padded numeric format (September -> 09).
- [time-stamp](https://github.com/jonschlinkert/time-stamp) [![GitHub stars](https://img.shields.io/github/stars/jonschlinkert/time-stamp?style=flat)](https://github.com/jonschlinkert/time-stamp/stargazers) - More of the same, in 700 bytes.
- [ms](https://github.com/vercel/ms) [![GitHub stars](https://img.shields.io/github/stars/vercel/ms?style=flat)](https://github.com/vercel/ms/stargazers) - Parse & format ms durations, e.g. `"1m" <-> 60000`, in 900 bytes.
- [timeago.js](https://github.com/hustcc/timeago.js) [![GitHub stars](https://img.shields.io/github/stars/hustcc/timeago.js?style=flat)](https://github.com/hustcc/timeago.js/stargazers) - Format dates into stuff like _X minutes ago_ or _in X hours,_ 2Kb.
- [fromnow](https://github.com/lukeed/fromnow) [![GitHub stars](https://img.shields.io/github/stars/lukeed/fromnow?style=flat)](https://github.com/lukeed/fromnow/stargazers) - More of the same, but in 350 bytes.

Note that the built-in [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat) has decent support.

## Generic Utilities

Something you'd find in lodash or ramda, but smaller. Most are pretty similar and very small, with minor differences in package structure (single / package-per-helper) and tree shaking vs direct helper import.

- [remeda](https://github.com/remeda/remeda) [![GitHub stars](https://img.shields.io/github/stars/remeda/remeda?style=flat)](https://github.com/remeda/remeda/stargazers) - 90 tree-shakable helpers.
- [rambda](https://github.com/selfrefactor/rambda) [![GitHub stars](https://img.shields.io/github/stars/selfrefactor/rambda?style=flat)](https://github.com/selfrefactor/rambda/stargazers) - 187 tree-shakable helpers.
- [just](https://github.com/angus-c/just) [![GitHub stars](https://img.shields.io/github/stars/angus-c/just?style=flat)](https://github.com/angus-c/just/stargazers) - 82 helpers in separate packages.
- [@tinkoff/utils](https://github.com/Tinkoff/utils.js) [![GitHub stars](https://img.shields.io/github/stars/Tinkoff/utils.js?style=flat)](https://github.com/Tinkoff/utils.js/stargazers) - 173 helpers, 1 import per helper. Conservative browser target.
- [@fxts/core](https://github.com/marpple/FxTS) [![GitHub stars](https://img.shields.io/github/stars/marpple/FxTS?style=flat)](https://github.com/marpple/FxTS/stargazers) - 96 tree-shakable helpers. Lazy evaluation support.

Honorable mention: [underscore,](https://github.com/jashkenas/underscore) [![GitHub stars](https://img.shields.io/github/stars/jashkenas/underscore?style=flat)](https://github.com/jashkenas/underscore/stargazers) outshined by lodash by chance, contains many sub-1Kb helpers. It does not tree-shake as well as the libraries above due to codebase structure.

Note: lodash itself is not tree-shakable, but has made many attempts at modulaity with `lodash.method` packages, imports from `lodash/method`, and `lodash-es`, none of which work well in practice. But yes, lodash does handle some corner cases.

Also note that much of the original lodash functionality comes built-in with modern ES. Prefer native versions over libraries as your browser target allows.

## Unique ID Generation

Unique ID generation does not take a lot of code, but it's not someting I'd want to write myself. Limit is 500 bytes. Also note that the [native `crypto.randomUUID`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) has [OK support.](https://caniuse.com/mdn-api_crypto_randomuuid)

- [uuid](https://github.com/lukeed/uuid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/uuid?style=flat)](https://github.com/lukeed/uuid/stargazers) - Real UUIDs in 240 bytes.
- [nanoid](https://github.com/ai/nanoid) [![GitHub stars](https://img.shields.io/github/stars/ai/nanoid?style=flat)](https://github.com/ai/nanoid/stargazers) - Random IDs with larger alphabet in 130 bytes.
- [uid](https://github.com/lukeed/uid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/uid?style=flat)](https://github.com/lukeed/uid/stargazers) - Can do in in 130–205 bytes.
- [hexoid](https://github.com/lukeed/hexoid) [![GitHub stars](https://img.shields.io/github/stars/lukeed/hexoid?style=flat)](https://github.com/lukeed/hexoid/stargazers) - Hex IDs in 190 bytes.

## Colors

Color manipulation is rare in pure UI development, but very helpful for data visualization, and uses [freaky math.](https://en.wikipedia.org/wiki/HSL_and_HSV#Color_conversion_formulae) Don't fry your brain, take these:

- [colord](https://github.com/omgovich/colord) [![GitHub stars](https://img.shields.io/github/stars/omgovich/colord?style=flat)](https://github.com/omgovich/colord/stargazers) - Manipulate colors and convert formats. 1.7Kb, exotic color spaces as plugins.
- [colr](https://github.com/stayradiated/colr) [![GitHub stars](https://img.shields.io/github/stars/stayradiated/colr?style=flat)](https://github.com/stayradiated/colr/stargazers) - Fits more color spaces, but fewer manipulations than colord, into 1.9Kb.
- [randomcolor](https://github.com/davidmerfield/randomColor) [![GitHub stars](https://img.shields.io/github/stars/davidmerfield/randomColor?style=flat)](https://github.com/davidmerfield/randomColor/stargazers) - Random attractive colors with configuration, just above 2Kb.
- [polychrome](https://github.com/cdonohue/polychrome) [![GitHub stars](https://img.shields.io/github/stars/cdonohue/polychrome?style=flat)](https://github.com/cdonohue/polychrome/stargazers) - Color manipulation in 2Kb.

## To be Continued

See [WIP.md](./WIP.md) for a list of small libraries I have found, but not yet analyzed deeply.

Suggestions welcome! Please check that the lib you're suggesting:

- Fits the [criteria.](#awesome-tiny-js)
- Is not already in [WIP.](./WIP.md) 

And drop a pull request or an [issue](https://github.com/thoughtspile/awesome-tiny-js/issues) [![GitHub stars](https://img.shields.io/github/stars/thoughtspile/awesome-tiny-js/issues?style=flat)](https://github.com/thoughtspile/awesome-tiny-js/issues/stargazers).

---

Collected and reviewed by [Vladimir Klepov](https://blog.thoughtspile.tech) in 2023. [CC0 license.](./LICENSE)
