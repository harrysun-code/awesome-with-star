# ESLint

> 来源：[dustinspecker/awesome-eslint](https://github.com/dustinspecker/awesome-eslint)

[![GitHub stars](https://img.shields.io/github/stars/dustinspecker/awesome-eslint?style=flat)](https://github.com/dustinspecker/awesome-eslint/stargazers)

# Awesome ESLint [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://eslint.org/icon.svg" width="160" align="right" alt="eslint">](http://eslint.org)

> A list of awesome ESLint configs, plugins, etc.

If you want to contribute, please read the [contribution guidelines](contributing.md).

## Contents

- [Configs](#configs)
  - [Configs by Well-Known Companies/Organizations](#configs-by-well-known-companiesorganizations)
  - [Other Prominent Configs (100 stars or so)](#other-prominent-configs-100-stars-or-so)
  - [Other Configs](#other-configs)
- [Preconfigured Configs with ESLint Set up](#preconfigured-configs-with-eslint-set-up)
- [Plugins](#plugins)
  - [Code Quality](#code-quality)
  - [Compatibility](#compatibility)
  - [CSS in JS](#css-in-js)
  - [Deprecation](#deprecation)
  - [Embedded](#embedded)
  - [Frameworks](#frameworks)
  - [Languages and Environments](#languages-and-environments)
  - [Libraries](#libraries)
  - [Misc](#misc)
  - [Practices and Specific ES Features](#practices-and-specific-es-features)
  - [Performance](#performance)
  - [Security](#security)
  - [Style](#style)
  - [Testing Tools](#testing-tools)
- [Parsers](#parsers)
- [Formatters](#formatters)
- [Globals](#globals)
- [Tools](#tools)
- [Developing for ESLint](#developing-for-eslint)
- [Tutorials](#tutorials)
- [Installation and Setup](#installation-and-setup)

## Configs

### Configs by Well-Known Companies/Organizations

- [Airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb) [![GitHub stars](https://img.shields.io/github/stars/airbnb/javascript/tree/master/packages/eslint-config-airbnb?style=flat)](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb/stargazers) - Shareable config for [Airbnb's style guide](https://github.com/airbnb/javascript) [![GitHub stars](https://img.shields.io/github/stars/airbnb/javascript?style=flat)](https://github.com/airbnb/javascript/stargazers).
- [Airbnb-babel](https://github.com/davidjbradshaw/eslint-config-airbnb-babel) [![GitHub stars](https://img.shields.io/github/stars/davidjbradshaw/eslint-config-airbnb-babel?style=flat)](https://github.com/davidjbradshaw/eslint-config-airbnb-babel/stargazers) - Airbnb's ESLint config with Babel Support.
- [Alloy](https://github.com/AlloyTeam/eslint-config-alloy) [![GitHub stars](https://img.shields.io/github/stars/AlloyTeam/eslint-config-alloy?style=flat)](https://github.com/AlloyTeam/eslint-config-alloy/stargazers) - Progressive ESLint config for your React/Vue/TypeScript projects.
- [ESLint](https://github.com/eslint/eslint/tree/master/packages/eslint-config-eslint) [![GitHub stars](https://img.shields.io/github/stars/eslint/eslint/tree/master/packages/eslint-config-eslint?style=flat)](https://github.com/eslint/eslint/tree/master/packages/eslint-config-eslint/stargazers) - Contains the ESLint configuration used for projects maintained by the ESLint team.
- [Facebook](https://www.npmjs.com/package/eslint-config-fbjs) - Sharable config for Facebook's style guide.
- [Feedzai](https://github.com/feedzai/eslint-config-feedzai) [![GitHub stars](https://img.shields.io/github/stars/feedzai/eslint-config-feedzai?style=flat)](https://github.com/feedzai/eslint-config-feedzai/stargazers) - Feedzai's shareable config for JavaScript/React projects.
- [Shopify](https://github.com/Shopify/web-foundation/blob/main/packages/eslint-plugin/README.md) [![GitHub stars](https://img.shields.io/github/stars/Shopify/web-foundation/blob/main/packages/eslint-plugin/README.md?style=flat)](https://github.com/Shopify/web-foundation/blob/main/packages/eslint-plugin/README.md/stargazers) - Shareable config for [Shopify's style guide](https://github.com/Shopify/javascript) [![GitHub stars](https://img.shields.io/github/stars/Shopify/javascript?style=flat)](https://github.com/Shopify/javascript/stargazers).
- [Wikimedia](https://github.com/wikimedia/eslint-config-wikimedia) [![GitHub stars](https://img.shields.io/github/stars/wikimedia/eslint-config-wikimedia?style=flat)](https://github.com/wikimedia/eslint-config-wikimedia/stargazers) - Shareable config for [Wikimedia's style guide](https://www.mediawiki.org/wiki/Manual:Coding_conventions/JavaScript), used by [MediaWiki](https://www.mediawiki.org/).

### Other Prominent Configs (100 stars or so)

- [Auto](https://github.com/davidjbradshaw/eslint-config-auto) [![GitHub stars](https://img.shields.io/github/stars/davidjbradshaw/eslint-config-auto?style=flat)](https://github.com/davidjbradshaw/eslint-config-auto/stargazers) - Automatically configure ESLint based on your project's dependencies.
- [Canonical](https://github.com/gajus/eslint-config-canonical) [![GitHub stars](https://img.shields.io/github/stars/gajus/eslint-config-canonical?style=flat)](https://github.com/gajus/eslint-config-canonical/stargazers) - Shareable config for [Canonical style guide](https://github.com/gajus/canonical) [![GitHub stars](https://img.shields.io/github/stars/gajus/canonical?style=flat)](https://github.com/gajus/canonical/stargazers).
<!-- lint disable double-link -->
- [Standard](https://github.com/feross/eslint-config-standard) [![GitHub stars](https://img.shields.io/github/stars/feross/eslint-config-standard?style=flat)](https://github.com/feross/eslint-config-standard/stargazers) - Shareable config for JavaScript [Standard Style](https://github.com/feross/standard) [![GitHub stars](https://img.shields.io/github/stars/feross/standard?style=flat)](https://github.com/feross/standard/stargazers).
- [XO](https://github.com/xojs/eslint-config-xo) [![GitHub stars](https://img.shields.io/github/stars/xojs/eslint-config-xo?style=flat)](https://github.com/xojs/eslint-config-xo/stargazers) - Shareable config for [XO](https://github.com/xojs/xo) [![GitHub stars](https://img.shields.io/github/stars/xojs/xo?style=flat)](https://github.com/xojs/xo/stargazers).
- [Antfu Eslint Config](https://github.com/antfu/eslint-config) [![GitHub stars](https://img.shields.io/github/stars/antfu/eslint-config?style=flat)](https://github.com/antfu/eslint-config/stargazers) - Anthony's ESLint config preset.

### Other Configs

- [Adjunct](https://github.com/davidjbradshaw/eslint-config-adjunct) [![GitHub stars](https://img.shields.io/github/stars/davidjbradshaw/eslint-config-adjunct?style=flat)](https://github.com/davidjbradshaw/eslint-config-adjunct/stargazers) - A reasonable collection of plugins to use alongside your main ESLint configuration.
- [Ash-Nazg](https://github.com/brettz9/eslint-config-ash-nazg) [![GitHub stars](https://img.shields.io/github/stars/brettz9/eslint-config-ash-nazg?style=flat)](https://github.com/brettz9/eslint-config-ash-nazg/stargazers) - One config to rule them all!
- [Cecilia](https://github.com/SandroMiguel/eslint-config-cecilia) [![GitHub stars](https://img.shields.io/github/stars/SandroMiguel/eslint-config-cecilia?style=flat)](https://github.com/SandroMiguel/eslint-config-cecilia/stargazers) - ESLint configuration for awesome projects.
- [clean-typescript](https://github.com/cunarist/eslint-config-clean-typescript) [![GitHub stars](https://img.shields.io/github/stars/cunarist/eslint-config-clean-typescript?style=flat)](https://github.com/cunarist/eslint-config-clean-typescript/stargazers) - Enforce classic JavaScript featuress in TypeScript codebase by banning excessive keywords.
- [Hardcore](https://github.com/EvgenyOrekhov/eslint-config-hardcore) [![GitHub stars](https://img.shields.io/github/stars/EvgenyOrekhov/eslint-config-hardcore?style=flat)](https://github.com/EvgenyOrekhov/eslint-config-hardcore/stargazers) - The most strict (but practical) ESLint config out there.
- [Problems](https://github.com/RyanZim/eslint-config-problems) [![GitHub stars](https://img.shields.io/github/stars/RyanZim/eslint-config-problems?style=flat)](https://github.com/RyanZim/eslint-config-problems/stargazers) - Shareable config that only catches actual problems, and doesn't enforce stylistic preferences.
- [Supermind](https://github.com/supermind/eslint-config-supermind) [![GitHub stars](https://img.shields.io/github/stars/supermind/eslint-config-supermind?style=flat)](https://github.com/supermind/eslint-config-supermind/stargazers) - Shareable config for Supermind style.
- [Sheriff](https://github.com/AndreaPontrandolfo/sheriff) [![GitHub stars](https://img.shields.io/github/stars/AndreaPontrandolfo/sheriff?style=flat)](https://github.com/AndreaPontrandolfo/sheriff/stargazers) - Comprehensive and highly opinionated Eslint configuration. Typescript oriented.

## Preconfigured Configs with ESLint Set up

- [Node.js Standard Style](https://github.com/geek/node-style) [![GitHub stars](https://img.shields.io/github/stars/geek/node-style?style=flat)](https://github.com/geek/node-style/stargazers) - Node.js core config.
- [eslint-config-airbnb-extended](https://github.com/eslint-config/airbnb-extended) [![GitHub stars](https://img.shields.io/github/stars/eslint-config/airbnb-extended?style=flat)](https://github.com/eslint-config/airbnb-extended/stargazers) - A powerful ESLint configuration extending the popular Airbnb style guide, with added support for TypeScript.
- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) [![GitHub stars](https://img.shields.io/github/stars/prettier/eslint-config-prettier?style=flat)](https://github.com/prettier/eslint-config-prettier/stargazers) - Prettier config for ESlint maintained by Prettier team.
- [Standard](https://github.com/feross/standard) [![GitHub stars](https://img.shields.io/github/stars/feross/standard?style=flat)](https://github.com/feross/standard/stargazers) - JavaScript Standard Style.
- [Superlint](https://github.com/supermind/superlint) [![GitHub stars](https://img.shields.io/github/stars/supermind/superlint?style=flat)](https://github.com/supermind/superlint/stargazers) - JavaScript Supermind Style.
- [XO](https://github.com/sindresorhus/xo) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/xo?style=flat)](https://github.com/sindresorhus/xo/stargazers) - JavaScript happiness style linter ❤️.

## Plugins

### Code Quality

- [depend](https://github.com/es-tooling/eslint-plugin-depend) [![GitHub stars](https://img.shields.io/github/stars/es-tooling/eslint-plugin-depend?style=flat)](https://github.com/es-tooling/eslint-plugin-depend/stargazers) - Helps detect dependency tree bloat and redundant polyfills.
- [GitHub](https://github.com/github/eslint-plugin-github) [![GitHub stars](https://img.shields.io/github/stars/github/eslint-plugin-github?style=flat)](https://github.com/github/eslint-plugin-github/stargazers) - Misc. rules from GitHub.
- [SonarJS](https://github.com/SonarSource/SonarJS/blob/master/packages/jsts/src/rules/README.md) [![GitHub stars](https://img.shields.io/github/stars/SonarSource/SonarJS/blob/master/packages/jsts/src/rules/README.md?style=flat)](https://github.com/SonarSource/SonarJS/blob/master/packages/jsts/src/rules/README.md/stargazers) - Rules detecting bugs and suspicious patterns.
- [Unicorn](https://github.com/sindresorhus/eslint-plugin-unicorn) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/eslint-plugin-unicorn?style=flat)](https://github.com/sindresorhus/eslint-plugin-unicorn/stargazers) - Various awesome ESLint rules.
- [@mysticatea/eslint-plugin](https://github.com/mysticatea/eslint-plugin) [![GitHub stars](https://img.shields.io/github/stars/mysticatea/eslint-plugin?style=flat)](https://github.com/mysticatea/eslint-plugin/stargazers) - Misc. rules.
- [@brettz9/eslint-plugin](https://github.com/brettz9/eslint-plugin) [![GitHub stars](https://img.shields.io/github/stars/brettz9/eslint-plugin?style=flat)](https://github.com/brettz9/eslint-plugin/stargazers) - Misc. rules. of `@mysticatea` without the personal config.
- [De Morgan](https://github.com/azat-io/eslint-plugin-de-morgan) [![GitHub stars](https://img.shields.io/github/stars/azat-io/eslint-plugin-de-morgan?style=flat)](https://github.com/azat-io/eslint-plugin-de-morgan/stargazers) - Transforms logical expressions in code to make them easier to understand.
- [Deslint](https://github.com/jaydrao215/deslint) [![GitHub stars](https://img.shields.io/github/stars/jaydrao215/deslint?style=flat)](https://github.com/jaydrao215/deslint/stargazers) - The design quality gate for AI-generated frontend code. 20 rules covering arbitrary colors/spacing/typography, design-system drift, responsive coverage, and WCAG 2.2 / 2.1 AA accessibility across React, Vue, Svelte, Angular, and plain HTML.
- [eslint-plugin-code-complete](https://github.com/aryelu/eslint-plugin-code-complete) [![GitHub stars](https://img.shields.io/github/stars/aryelu/eslint-plugin-code-complete?style=flat)](https://github.com/aryelu/eslint-plugin-code-complete/stargazers) - A custom ESLint plugin that enforces principles of clean, maintainable software design — inspired by Code Complete.
- [eslint-plugin-ai-guard](https://github.com/YashJadhav21/eslint-plugin-ai-guard) [![GitHub stars](https://img.shields.io/github/stars/YashJadhav21/eslint-plugin-ai-guard?style=flat)](https://github.com/YashJadhav21/eslint-plugin-ai-guard/stargazers) - Detects bugs and security issues commonly introduced by AI-generated code (async misuse, empty catch, auth gaps, SQL concat, secrets).

### Compatibility

- [Compat](https://github.com/amilajack/eslint-plugin-compat) [![GitHub stars](https://img.shields.io/github/stars/amilajack/eslint-plugin-compat?style=flat)](https://github.com/amilajack/eslint-plugin-compat/stargazers) - Lint browser compatibility of APIs used ([caniuse](http://caniuse.com/#search=fetch) as an ESLint plugin).
- [ecmascript-compat](https://github.com/robatwilliams/es-compat) [![GitHub stars](https://img.shields.io/github/stars/robatwilliams/es-compat?style=flat)](https://github.com/robatwilliams/es-compat/stargazers) - Disable ECMAScript language features not supported by your browserslist targets.
- [es-x](https://github.com/eslint-community/eslint-plugin-es-x) [![GitHub stars](https://img.shields.io/github/stars/eslint-community/eslint-plugin-es-x?style=flat)](https://github.com/eslint-community/eslint-plugin-es-x/stargazers) - Disable specific ECMAScript language versions or individual features. Properly maintained fork of no longer maintained `eslint-plugin-es`.
- [es5](https://github.com/nkt/eslint-plugin-es5) [![GitHub stars](https://img.shields.io/github/stars/nkt/eslint-plugin-es5?style=flat)](https://github.com/nkt/eslint-plugin-es5/stargazers) - ESLint plugin for ES5 users (forbid ES2015+ usage).
- [ie11](https://github.com/Volox/eslint-plugin-ie11) [![GitHub stars](https://img.shields.io/github/stars/Volox/eslint-plugin-ie11?style=flat)](https://github.com/Volox/eslint-plugin-ie11/stargazers) - Detect unsupported ES6 features in IE11.

### CSS in JS

- [CSS-modules](https://github.com/atfzl/eslint-plugin-css-modules) [![GitHub stars](https://img.shields.io/github/stars/atfzl/eslint-plugin-css-modules?style=flat)](https://github.com/atfzl/eslint-plugin-css-modules/stargazers) - Lint undefined or unused rules for css modules.
- [Emotion](https://github.com/emotion-js/emotion/tree/master/packages/eslint-plugin) [![GitHub stars](https://img.shields.io/github/stars/emotion-js/emotion/tree/master/packages/eslint-plugin?style=flat)](https://github.com/emotion-js/emotion/tree/master/packages/eslint-plugin/stargazers) - ESLint rules for emotion.
- Styled Components
  - [Better Styled Components](https://github.com/tinloof/eslint-plugin-better-styled-components) [![GitHub stars](https://img.shields.io/github/stars/tinloof/eslint-plugin-better-styled-components?style=flat)](https://github.com/tinloof/eslint-plugin-better-styled-components/stargazers) - Auto fixable ESlint's rules for styled components.
  - [styled-components-a11y](https://github.com/brendanmorrell/eslint-plugin-styled-components-a11y) [![GitHub stars](https://img.shields.io/github/stars/brendanmorrell/eslint-plugin-styled-components-a11y?style=flat)](https://github.com/brendanmorrell/eslint-plugin-styled-components-a11y/stargazers) - A11y for Styled Components.
- [vanilla-extract](https://github.com/antebudimir/eslint-plugin-vanilla-extract) [![GitHub stars](https://img.shields.io/github/stars/antebudimir/eslint-plugin-vanilla-extract?style=flat)](https://github.com/antebudimir/eslint-plugin-vanilla-extract/stargazers) - An ESLint plugin for enforcing CSS property ordering in [vanilla-extract CSS](https://github.com/vanilla-extract-css/vanilla-extract) [![GitHub stars](https://img.shields.io/github/stars/vanilla-extract-css/vanilla-extract?style=flat)](https://github.com/vanilla-extract-css/vanilla-extract/stargazers) styles.

### Deprecation

- [deprecate](https://github.com/AlexMost/eslint-plugin-deprecate) [![GitHub stars](https://img.shields.io/github/stars/AlexMost/eslint-plugin-deprecate?style=flat)](https://github.com/AlexMost/eslint-plugin-deprecate/stargazers) - Mark functions or modules as deprecated and get lint messages when they are used.
- [disable](https://github.com/mradionov/eslint-plugin-disable) [![GitHub stars](https://img.shields.io/github/stars/mradionov/eslint-plugin-disable?style=flat)](https://github.com/mradionov/eslint-plugin-disable/stargazers) - Disable specified plugins using file path patterns and inline comments.

### Embedded

- [HTML](https://github.com/BenoitZugmeyer/eslint-plugin-html) [![GitHub stars](https://img.shields.io/github/stars/BenoitZugmeyer/eslint-plugin-html?style=flat)](https://github.com/BenoitZugmeyer/eslint-plugin-html/stargazers) - Linting for JavaScript inside of HTML `<script>` tags.
- [Markdown](https://github.com/eslint/eslint-plugin-markdown) [![GitHub stars](https://img.shields.io/github/stars/eslint/eslint-plugin-markdown?style=flat)](https://github.com/eslint/eslint-plugin-markdown/stargazers) - Linting for JavaScript inside of Markdown.

### Frameworks

- [Angular](https://github.com/angular-eslint/angular-eslint) [![GitHub stars](https://img.shields.io/github/stars/angular-eslint/angular-eslint?style=flat)](https://github.com/angular-eslint/angular-eslint/stargazers) - Linting rules for Angular (v2+).
- [AngularJS](https://github.com/Gillespie59/eslint-plugin-angular) [![GitHub stars](https://img.shields.io/github/stars/Gillespie59/eslint-plugin-angular?style=flat)](https://github.com/Gillespie59/eslint-plugin-angular/stargazers) - Linting rules to adhere to the [John Papa's AngularJS Styleguide](https://github.com/johnpapa/angular-styleguide) [![GitHub stars](https://img.shields.io/github/stars/johnpapa/angular-styleguide?style=flat)](https://github.com/johnpapa/angular-styleguide/stargazers).
- [Astro](https://github.com/ota-meshi/eslint-plugin-astro) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-astro?style=flat)](https://github.com/ota-meshi/eslint-plugin-astro/stargazers) - Plugin for [Astro components](https://docs.astro.build/en/core-concepts/astro-components/).
- [Backbone](https://github.com/ilyavolodin/eslint-plugin-backbone) [![GitHub stars](https://img.shields.io/github/stars/ilyavolodin/eslint-plugin-backbone?style=flat)](https://github.com/ilyavolodin/eslint-plugin-backbone/stargazers) - Linting rules for Backbone.
- [Ember](https://github.com/ember-cli/eslint-plugin-ember) [![GitHub stars](https://img.shields.io/github/stars/ember-cli/eslint-plugin-ember?style=flat)](https://github.com/ember-cli/eslint-plugin-ember/stargazers) - Linting rules for Ember.
- [Hapi](https://github.com/continuationlabs/eslint-plugin-hapi) [![GitHub stars](https://img.shields.io/github/stars/continuationlabs/eslint-plugin-hapi?style=flat)](https://github.com/continuationlabs/eslint-plugin-hapi/stargazers) - Linting rules for hapi.
- [Meteor](https://github.com/meteor/meteor/tree/devel/npm-packages/eslint-plugin-meteor) [![GitHub stars](https://img.shields.io/github/stars/meteor/meteor/tree/devel/npm-packages/eslint-plugin-meteor?style=flat)](https://github.com/meteor/meteor/tree/devel/npm-packages/eslint-plugin-meteor/stargazers) - Meteor specific linting rules for ESLint.
- React
  - [JSX a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) [![GitHub stars](https://img.shields.io/github/stars/jsx-eslint/eslint-plugin-jsx-a11y?style=flat)](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/stargazers) - Accessibility rules on JSX elements.
  - [React](https://github.com/yannickcr/eslint-plugin-react) [![GitHub stars](https://img.shields.io/github/stars/yannickcr/eslint-plugin-react?style=flat)](https://github.com/yannickcr/eslint-plugin-react/stargazers) - Linting rules for React and JSX.
  - [React Hooks](https://github.com/facebook/react/tree/master/packages/eslint-plugin-react-hooks) [![GitHub stars](https://img.shields.io/github/stars/facebook/react/tree/master/packages/eslint-plugin-react-hooks?style=flat)](https://github.com/facebook/react/tree/master/packages/eslint-plugin-react-hooks/stargazers) - Linting rules for React Hooks.
  - [React Native](https://github.com/Intellicode/eslint-plugin-react-native) [![GitHub stars](https://img.shields.io/github/stars/Intellicode/eslint-plugin-react-native?style=flat)](https://github.com/Intellicode/eslint-plugin-react-native/stargazers) - React Native specific linting rules.
  - [React-Redux](https://github.com/DianaSuvorova/eslint-plugin-react-redux) [![GitHub stars](https://img.shields.io/github/stars/DianaSuvorova/eslint-plugin-react-redux?style=flat)](https://github.com/DianaSuvorova/eslint-plugin-react-redux/stargazers) - React-Redux specific linting rules.
  - [React Refresh](https://github.com/ArnaudBarre/eslint-plugin-react-refresh) [![GitHub stars](https://img.shields.io/github/stars/ArnaudBarre/eslint-plugin-react-refresh?style=flat)](https://github.com/ArnaudBarre/eslint-plugin-react-refresh/stargazers) - Improve HMR experience when using Vite.
- [Solid](https://github.com/joshwilsonvu/eslint-plugin-solid) [![GitHub stars](https://img.shields.io/github/stars/joshwilsonvu/eslint-plugin-solid?style=flat)](https://github.com/joshwilsonvu/eslint-plugin-solid/stargazers) - Linting rules for Solid and JSX.
- [Svelte](https://github.com/sveltejs/eslint-plugin-svelte) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/eslint-plugin-svelte?style=flat)](https://github.com/sveltejs/eslint-plugin-svelte/stargazers) - Linting rules for Svelte v3 Components.
- Vue
  - [VueJS](https://github.com/vuejs/eslint-plugin-vue) [![GitHub stars](https://img.shields.io/github/stars/vuejs/eslint-plugin-vue?style=flat)](https://github.com/vuejs/eslint-plugin-vue/stargazers) - Plugin for VueJS.
  - [VueJS Scoped CSS](https://github.com/future-architect/eslint-plugin-vue-scoped-css) [![GitHub stars](https://img.shields.io/github/stars/future-architect/eslint-plugin-vue-scoped-css?style=flat)](https://github.com/future-architect/eslint-plugin-vue-scoped-css/stargazers) - Plugin for Scoped CSS in VueJS.

### Languages and Environments

- [Babel](https://github.com/babel/babel/tree/main/eslint/babel-eslint-plugin) [![GitHub stars](https://img.shields.io/github/stars/babel/babel/tree/main/eslint/babel-eslint-plugin?style=flat)](https://github.com/babel/babel/tree/main/eslint/babel-eslint-plugin/stargazers) - Adds replacements for built-in rules to include Babel features.
- [eslint-plugin-eslint-plugin](https://github.com/not-an-aardvark/eslint-plugin-eslint-plugin) [![GitHub stars](https://img.shields.io/github/stars/not-an-aardvark/eslint-plugin-eslint-plugin?style=flat)](https://github.com/not-an-aardvark/eslint-plugin-eslint-plugin/stargazers) - An ESLint plugin for linting ESLint plugins.
- Flow
  - [Flow](https://github.com/gajus/eslint-plugin-flowtype) [![GitHub stars](https://img.shields.io/github/stars/gajus/eslint-plugin-flowtype?style=flat)](https://github.com/gajus/eslint-plugin-flowtype/stargazers) - Flow type linting rules.
  - [Flow Errors](https://github.com/amilajack/eslint-plugin-flowtype-errors) [![GitHub stars](https://img.shields.io/github/stars/amilajack/eslint-plugin-flowtype-errors?style=flat)](https://github.com/amilajack/eslint-plugin-flowtype-errors/stargazers) - Run Flow as an ESLint plugin.
- [HTML](https://github.com/yeonjuan/html-eslint) [![GitHub stars](https://img.shields.io/github/stars/yeonjuan/html-eslint?style=flat)](https://github.com/yeonjuan/html-eslint/stargazers) - ESLint plugin for HTML.
- JSON
  - [JSON](https://github.com/azeemba/eslint-plugin-json) [![GitHub stars](https://img.shields.io/github/stars/azeemba/eslint-plugin-json?style=flat)](https://github.com/azeemba/eslint-plugin-json/stargazers) - Lint your JSON files.
  - [JSON, package.json](https://github.com/Bkucera/eslint-plugin-json-format) [![GitHub stars](https://img.shields.io/github/stars/Bkucera/eslint-plugin-json-format?style=flat)](https://github.com/Bkucera/eslint-plugin-json-format/stargazers) - Lint, format, and auto-fix your JSON files. Sort your `package.json`.
  - [JSON with Comments](https://github.com/ota-meshi/eslint-plugin-jsonc) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-jsonc?style=flat)](https://github.com/ota-meshi/eslint-plugin-jsonc/stargazers) - ESLint plugin for JSON, JSONC and JSON5.
  - [JSON Schema](https://github.com/ota-meshi/eslint-plugin-json-schema-validator) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-json-schema-validator?style=flat)](https://github.com/ota-meshi/eslint-plugin-json-schema-validator/stargazers) - Validates data defined in JavaScript, JSON, YAML and TOML using JSON Schema Validator.
  - [eslint-plugin-package-json](https://github.com/JoshuaKGoldberg/eslint-plugin-package-json) [![GitHub stars](https://img.shields.io/github/stars/JoshuaKGoldberg/eslint-plugin-package-json?style=flat)](https://github.com/JoshuaKGoldberg/eslint-plugin-package-json/stargazers) - Rules for consistent, readable, and valid package.json files.
- [MDX](https://github.com/mdx-js/eslint-mdx/tree/master/packages/eslint-plugin-mdx) [![GitHub stars](https://img.shields.io/github/stars/mdx-js/eslint-mdx/tree/master/packages/eslint-plugin-mdx?style=flat)](https://github.com/mdx-js/eslint-mdx/tree/master/packages/eslint-plugin-mdx/stargazers) - ESLint Parser/Plugin for MDX.
- [N](https://github.com/eslint-community/eslint-plugin-n) [![GitHub stars](https://img.shields.io/github/stars/eslint-community/eslint-plugin-n?style=flat)](https://github.com/eslint-community/eslint-plugin-n/stargazers) - Additional ESLint's rules for Node.js. Properly maintained fork of no longer maintained `eslint-plugin-node`.
- [SQL](https://github.com/gajus/eslint-plugin-sql) [![GitHub stars](https://img.shields.io/github/stars/gajus/eslint-plugin-sql?style=flat)](https://github.com/gajus/eslint-plugin-sql/stargazers) - SQL linting rules for ESLint.
- [TOML](https://github.com/ota-meshi/eslint-plugin-toml) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-toml?style=flat)](https://github.com/ota-meshi/eslint-plugin-toml/stargazers) - ESLint plugin for TOML.
- [TypeScript](https://typescript-eslint.io) - Linting rules for TypeScript.
  - [eslint-plugin-erasable-syntax-only](https://github.com/JoshuaKGoldberg/eslint-plugin-erasable-syntax-only) [![GitHub stars](https://img.shields.io/github/stars/JoshuaKGoldberg/eslint-plugin-erasable-syntax-only?style=flat)](https://github.com/JoshuaKGoldberg/eslint-plugin-erasable-syntax-only/stargazers) - Granularly enforces TypeScript's erasableSyntaxOnly flag.
  - [eslint-plugin-expect-type](https://github.com/JoshuaKGoldberg/eslint-plugin-expect-type) [![GitHub stars](https://img.shields.io/github/stars/JoshuaKGoldberg/eslint-plugin-expect-type?style=flat)](https://github.com/JoshuaKGoldberg/eslint-plugin-expect-type/stargazers) - Provides Twoslash, $ExpectError, and $ExpectType type assertions.
- [YAML](https://github.com/ota-meshi/eslint-plugin-yml) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-yml?style=flat)](https://github.com/ota-meshi/eslint-plugin-yml/stargazers) - ESLint plugin for YAML.

### Libraries

- GraphQL
  - [dotansimha/graphql-eslint](https://github.com/dotansimha/graphql-eslint) [![GitHub stars](https://img.shields.io/github/stars/dotansimha/graphql-eslint?style=flat)](https://github.com/dotansimha/graphql-eslint/stargazers) - Validates, prettifies and checks your GraphQL operations and GraphQL schema for best-practices.
  - [apollostack/eslint-plugin-graphql](https://github.com/apollostack/eslint-plugin-graphql) [![GitHub stars](https://img.shields.io/github/stars/apollostack/eslint-plugin-graphql?style=flat)](https://github.com/apollostack/eslint-plugin-graphql/stargazers) - Check your GraphQL query strings against a schema.
- [TypeGraphQL](https://github.com/borremosch/eslint-plugin-type-graphql) [![GitHub stars](https://img.shields.io/github/stars/borremosch/eslint-plugin-type-graphql?style=flat)](https://github.com/borremosch/eslint-plugin-type-graphql/stargazers) - Linting rules for TypeGraphQL, targeted at finding common mistakes.
- [jQuery](https://github.com/wikimedia/eslint-plugin-no-jquery) [![GitHub stars](https://img.shields.io/github/stars/wikimedia/eslint-plugin-no-jquery?style=flat)](https://github.com/wikimedia/eslint-plugin-no-jquery/stargazers) - Linting rules for jQuery, including versioned configs for deprecated features.
- [JSDoc](https://github.com/gajus/eslint-plugin-jsdoc) [![GitHub stars](https://img.shields.io/github/stars/gajus/eslint-plugin-jsdoc?style=flat)](https://github.com/gajus/eslint-plugin-jsdoc/stargazers) - Linting rules for JSDoc comments (including the JavaScript within `@example`).
- Lodash
  - [Lodash](https://github.com/wix/eslint-plugin-lodash) [![GitHub stars](https://img.shields.io/github/stars/wix/eslint-plugin-lodash?style=flat)](https://github.com/wix/eslint-plugin-lodash/stargazers) - Lodash specific linting rules.
  - [Lodash/fp](https://github.com/jfmengels/eslint-plugin-lodash-fp) [![GitHub stars](https://img.shields.io/github/stars/jfmengels/eslint-plugin-lodash-fp?style=flat)](https://github.com/jfmengels/eslint-plugin-lodash-fp/stargazers) - Lodash/fp specific linting rules.
  - [Lodash template](https://github.com/ota-meshi/eslint-plugin-lodash-template) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-lodash-template?style=flat)](https://github.com/ota-meshi/eslint-plugin-lodash-template/stargazers) - Plugin for Lodash template/Underscore template.
  - [Microtemplates](https://github.com/platinumazure/eslint-plugin-microtemplates) [![GitHub stars](https://img.shields.io/github/stars/platinumazure/eslint-plugin-microtemplates?style=flat)](https://github.com/platinumazure/eslint-plugin-microtemplates/stargazers) (Used in Lodash and Underscore.js)
- [Mongodb](https://github.com/nfroidure/eslint-plugin-mongodb) [![GitHub stars](https://img.shields.io/github/stars/nfroidure/eslint-plugin-mongodb?style=flat)](https://github.com/nfroidure/eslint-plugin-mongodb/stargazers) - Mongodb native Node.js driver linting rules.
- [Ramda](https://github.com/ramda/eslint-plugin-ramda) [![GitHub stars](https://img.shields.io/github/stars/ramda/eslint-plugin-ramda?style=flat)](https://github.com/ramda/eslint-plugin-ramda/stargazers) - Ramda specific linting rules.
- [RequireJS](https://github.com/cvisco/eslint-plugin-requirejs) [![GitHub stars](https://img.shields.io/github/stars/cvisco/eslint-plugin-requirejs?style=flat)](https://github.com/cvisco/eslint-plugin-requirejs/stargazers) - Linting rules for RequireJS.
- [Tailwind CSS](https://github.com/francoismassart/eslint-plugin-tailwindcss) [![GitHub stars](https://img.shields.io/github/stars/francoismassart/eslint-plugin-tailwindcss?style=flat)](https://github.com/francoismassart/eslint-plugin-tailwindcss/stargazers) - Linting rules for Tailwind CSS classnames.
- [Tailwind CSS v4](https://github.com/schoero/eslint-plugin-better-tailwindcss) [![GitHub stars](https://img.shields.io/github/stars/schoero/eslint-plugin-better-tailwindcss?style=flat)](https://github.com/schoero/eslint-plugin-better-tailwindcss/stargazers) - ESLint plugin to help you write better tailwindcss by improving readability with formatting rules and enforcing best practices with linting rules.

### Misc

- [Diff](https://github.com/paleite/eslint-plugin-diff) [![GitHub stars](https://img.shields.io/github/stars/paleite/eslint-plugin-diff?style=flat)](https://github.com/paleite/eslint-plugin-diff/stargazers) - Run ESLint on your changed lines only. Also supports CI!
- [Misc](https://github.com/ilyub/eslint-plugin-misc) [![GitHub stars](https://img.shields.io/github/stars/ilyub/eslint-plugin-misc?style=flat)](https://github.com/ilyub/eslint-plugin-misc/stargazers) - Miscellaneous rules including rules for creating custom checks and wrapping (modifying) third-party rules.
- [Notice](https://github.com/nickdeis/eslint-plugin-notice) [![GitHub stars](https://img.shields.io/github/stars/nickdeis/eslint-plugin-notice?style=flat)](https://github.com/nickdeis/eslint-plugin-notice/stargazers) - An eslint rule that checks the top of files and fixes them too!
- [Only-Error](https://github.com/davidjbradshaw/eslint-plugin-only-error) [![GitHub stars](https://img.shields.io/github/stars/davidjbradshaw/eslint-plugin-only-error?style=flat)](https://github.com/davidjbradshaw/eslint-plugin-only-error/stargazers) - Convert all rules to errors.
- [Only-Warn](https://github.com/bfanger/eslint-plugin-only-warn) [![GitHub stars](https://img.shields.io/github/stars/bfanger/eslint-plugin-only-warn?style=flat)](https://github.com/bfanger/eslint-plugin-only-warn/stargazers) - Convert all rules to warnings.
- [PutOut](https://github.com/coderaiser/putout/tree/master/packages/eslint-plugin-putout) [![GitHub stars](https://img.shields.io/github/stars/coderaiser/putout/tree/master/packages/eslint-plugin-putout?style=flat)](https://github.com/coderaiser/putout/tree/master/packages/eslint-plugin-putout/stargazers) - an ESLint plugin integrates [putout](https://github.com/coderaiser/putout) [![GitHub stars](https://img.shields.io/github/stars/coderaiser/putout?style=flat)](https://github.com/coderaiser/putout/stargazers) linter into ESLint.
- [TypeLint](https://github.com/yarax/eslint-plugin-typelint) [![GitHub stars](https://img.shields.io/github/stars/yarax/eslint-plugin-typelint?style=flat)](https://github.com/yarax/eslint-plugin-typelint/stargazers) - Introduces types, based on existing schemas (Swagger, Redux) and linting access to object properties, preventing `undefined` errors.
- [Woke](https://github.com/amwmedia/eslint-plugin-woke) [![GitHub stars](https://img.shields.io/github/stars/amwmedia/eslint-plugin-woke?style=flat)](https://github.com/amwmedia/eslint-plugin-woke/stargazers) - Helps catch insensitive words, promoting an inclusive codebase.

### Practices and Specific ES Features

- [array-func](https://github.com/freaktechnik/eslint-plugin-array-func) [![GitHub stars](https://img.shields.io/github/stars/freaktechnik/eslint-plugin-array-func?style=flat)](https://github.com/freaktechnik/eslint-plugin-array-func/stargazers) - Avoid redundancy when using es2015 array methods and functions.
- [arrow functions](https://github.com/getify/eslint-plugin-proper-arrows) [![GitHub stars](https://img.shields.io/github/stars/getify/eslint-plugin-proper-arrows?style=flat)](https://github.com/getify/eslint-plugin-proper-arrows/stargazers) - ESLint rules to ensure proper arrow function definitions.
- [boundaries](https://github.com/javierbrea/eslint-plugin-boundaries) [![GitHub stars](https://img.shields.io/github/stars/javierbrea/eslint-plugin-boundaries?style=flat)](https://github.com/javierbrea/eslint-plugin-boundaries/stargazers) - Ensures that your architecture boundaries are respected by the elements in your project checking file structure and dependencies.
- [@eslint-community/eslint-plugin-eslint-comments](https://github.com/eslint-community/eslint-plugin-eslint-comments) [![GitHub stars](https://img.shields.io/github/stars/eslint-community/eslint-plugin-eslint-comments?style=flat)](https://github.com/eslint-community/eslint-plugin-eslint-comments/stargazers) - Best practices about ESLint directive comments (`/*eslint-disable*/`, etc.). Properly maintained fork of no longer maintained `eslint-plugin-eslint-comments`.
- [eslint-plugin-error-cause](https://github.com/Amnish04/eslint-plugin-error-cause) [![GitHub stars](https://img.shields.io/github/stars/Amnish04/eslint-plugin-error-cause?style=flat)](https://github.com/Amnish04/eslint-plugin-error-cause/stargazers) - A plugin to preserve original error context when re-throwing exceptions.
- [eslint-plugin-hexagonal-architecture](https://github.com/CodelyTV/eslint-plugin-hexagonal-architecture) [![GitHub stars](https://img.shields.io/github/stars/CodelyTV/eslint-plugin-hexagonal-architecture?style=flat)](https://github.com/CodelyTV/eslint-plugin-hexagonal-architecture/stargazers) - A plugin that helps you to enforce hexagonal architecture best practices.
- [eslint-plugin-hex-under](https://github.com/2nd-Labs/eslint-plugin-hex-under) [![GitHub stars](https://img.shields.io/github/stars/2nd-Labs/eslint-plugin-hex-under?style=flat)](https://github.com/2nd-Labs/eslint-plugin-hex-under/stargazers) - A plugin to prove that a hexadecimal number is less than a specified value.
- [eslint-plugin-signature-design](https://github.com/Vladyslav-Soldatenko/eslint-plugin-signature-design) [![GitHub stars](https://img.shields.io/github/stars/Vladyslav-Soldatenko/eslint-plugin-signature-design?style=flat)](https://github.com/Vladyslav-Soldatenko/eslint-plugin-signature-design/stargazers) - Forbids functions with too many parameters of the same type, encouraging object-based signatures and preventing primitive obsession. 
- [eslint-plugin-write-good-comments](https://github.com/kantord/eslint-plugin-write-good-comments) [![GitHub stars](https://img.shields.io/github/stars/kantord/eslint-plugin-write-good-comments?style=flat)](https://github.com/kantord/eslint-plugin-write-good-comments/stargazers) - Enforce good writing style in comments.
- [eslint-plugin-exception-handling](https://github.com/Akronae/eslint-plugin-exception-handling) [![GitHub stars](https://img.shields.io/github/stars/Akronae/eslint-plugin-exception-handling?style=flat)](https://github.com/Akronae/eslint-plugin-exception-handling/stargazers) - Lints unhandled functions that might throw errors.
- [fp](https://github.com/jfmengels/eslint-plugin-fp) [![GitHub stars](https://img.shields.io/github/stars/jfmengels/eslint-plugin-fp?style=flat)](https://github.com/jfmengels/eslint-plugin-fp/stargazers) - ESLint rules for functional programming.
- [functional](https://github.com/jonaskello/eslint-plugin-functional) [![GitHub stars](https://img.shields.io/github/stars/jonaskello/eslint-plugin-functional?style=flat)](https://github.com/jonaskello/eslint-plugin-functional/stargazers) - ESLint rules to disable mutation and promote fp in JavaScript and TypeScript.
- [mutate](https://github.com/gchumillas/eslint-plugin-mutate) [![GitHub stars](https://img.shields.io/github/stars/gchumillas/eslint-plugin-mutate?style=flat)](https://github.com/gchumillas/eslint-plugin-mutate/stargazers) - Prevent accidental parameter mutations by enforcing explicit `mut` prefix (JavaScript) or `Mut<T>` type annotation (TypeScript).
- [ime-safe-form](https://github.com/hiroya-uga/eslint-plugin-ime-safe-form) [![GitHub stars](https://img.shields.io/github/stars/hiroya-uga/eslint-plugin-ime-safe-form?style=flat)](https://github.com/hiroya-uga/eslint-plugin-ime-safe-form/stargazers) - Prevents accidental form submission during IME composition by requiring `e.isComposing` guard or form `submit` event.
- [Immutable](https://github.com/jhusain/eslint-plugin-immutable) [![GitHub stars](https://img.shields.io/github/stars/jhusain/eslint-plugin-immutable?style=flat)](https://github.com/jhusain/eslint-plugin-immutable/stargazers) - Disable all mutation in JavaScript.
- [import](https://github.com/benmosher/eslint-plugin-import) [![GitHub stars](https://img.shields.io/github/stars/benmosher/eslint-plugin-import?style=flat)](https://github.com/benmosher/eslint-plugin-import/stargazers) - Linting of ES2015+ import/export syntax, and prevent issues with misspelling of file paths and import names.
- [import-x](https://github.com/un-ts/eslint-plugin-import-x) [![GitHub stars](https://img.shields.io/github/stars/un-ts/eslint-plugin-import-x?style=flat)](https://github.com/un-ts/eslint-plugin-import-x/stargazers) - Linting of ES2015+ import/export syntax, and prevent issues with misspelling of file paths and import names. Lightweight fork of `eslint-plugin-import`, but which breaks backwards compatibility.
- [logical-imports](https://gitlab.com/philbooth/eslint-plugin-logical-imports) - Sort imports logically by local name.
- [Math](https://github.com/ota-meshi/eslint-plugin-math) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-math?style=flat)](https://github.com/ota-meshi/eslint-plugin-math/stargazers) - ESLint plugin related to Math object and Number.
- [new-with-error](https://github.com/Trott/eslint-plugin-new-with-error) [![GitHub stars](https://img.shields.io/github/stars/Trott/eslint-plugin-new-with-error?style=flat)](https://github.com/Trott/eslint-plugin-new-with-error/stargazers) - Require errors to be thrown using `new`.
<!-- lint ignore awesome-spell-check -->
- [no-argument-spread](https://github.com/causalhq/eslint-plugin-no-argument-spread) [![GitHub stars](https://img.shields.io/github/stars/causalhq/eslint-plugin-no-argument-spread?style=flat)](https://github.com/causalhq/eslint-plugin-no-argument-spread/stargazers) - Lints against expressions like `Math.max(...args)` that can lead to a stack overflow for large arrays.
- [no-comments](https://github.com/wisniewski94/eslint-plugin-no-comments) [![GitHub stars](https://img.shields.io/github/stars/wisniewski94/eslint-plugin-no-comments?style=flat)](https://github.com/wisniewski94/eslint-plugin-no-comments/stargazers) - Prevents leaking comments into production if bundler is not used and stops developers from commenting out old lines of code.
- [no-constructor-bind](https://github.com/markalfred/eslint-plugin-no-constructor-bind) [![GitHub stars](https://img.shields.io/github/stars/markalfred/eslint-plugin-no-constructor-bind?style=flat)](https://github.com/markalfred/eslint-plugin-no-constructor-bind/stargazers) - Encourages use of class properties by reporting use of `this` with `bind` or setting state in constructors.
- [no-inferred-method-name](https://github.com/johnstonbl01/eslint-no-inferred-method-name) [![GitHub stars](https://img.shields.io/github/stars/johnstonbl01/eslint-no-inferred-method-name?style=flat)](https://github.com/johnstonbl01/eslint-no-inferred-method-name/stargazers) - Custom rule for ESLint that checks for inferred method names within object literals.
- [no-loops](https://github.com/buildo/eslint-plugin-no-loops) [![GitHub stars](https://img.shields.io/github/stars/buildo/eslint-plugin-no-loops?style=flat)](https://github.com/buildo/eslint-plugin-no-loops/stargazers) - It's 2019 and you still use loops?
- [no-restricted-syntax](https://github.com/brettz9/eslint-plugin-query) [![GitHub stars](https://img.shields.io/github/stars/brettz9/eslint-plugin-query?style=flat)](https://github.com/brettz9/eslint-plugin-query/stargazers) - Show queried syntax's content in messages.
- [no-use-extend-native](https://github.com/dustinspecker/eslint-plugin-no-use-extend-native) [![GitHub stars](https://img.shields.io/github/stars/dustinspecker/eslint-plugin-no-use-extend-native?style=flat)](https://github.com/dustinspecker/eslint-plugin-no-use-extend-native/stargazers) - Prevent using extended native objects.
- [Promise](https://github.com/xjamundx/eslint-plugin-promise) [![GitHub stars](https://img.shields.io/github/stars/xjamundx/eslint-plugin-promise?style=flat)](https://github.com/xjamundx/eslint-plugin-promise/stargazers) - Best practices when working with promises.
- [pure](https://github.com/purely-functional/eslint-plugin-pure) [![GitHub stars](https://img.shields.io/github/stars/purely-functional/eslint-plugin-pure?style=flat)](https://github.com/purely-functional/eslint-plugin-pure/stargazers) - Enforce pure functions (without side effects).
- [ReDoS](https://makenowjust-labs.github.io/recheck/docs/usage/as-eslint-plugin/) - ESLint plugin for finding possible ReDoS vulnerabilities.
- [ReDoSDetector](https://github.com/tjenkinson/eslint-plugin-redos-detector) [![GitHub stars](https://img.shields.io/github/stars/tjenkinson/eslint-plugin-redos-detector?style=flat)](https://github.com/tjenkinson/eslint-plugin-redos-detector/stargazers) - ESLint plugin for finding possible ReDoS vulnerabilities.
- [RegExp](https://github.com/ota-meshi/eslint-plugin-regexp) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-regexp?style=flat)](https://github.com/ota-meshi/eslint-plugin-regexp/stargazers) - ESLint plugin for finding regexp mistakes and style guide violations.
- [sort-keys-fix](https://github.com/leo-buneev/eslint-plugin-sort-keys-fix) [![GitHub stars](https://img.shields.io/github/stars/leo-buneev/eslint-plugin-sort-keys-fix?style=flat)](https://github.com/leo-buneev/eslint-plugin-sort-keys-fix/stargazers) - Adds fixer for ESLint `sort-keys` rule.
- [this](https://github.com/matijs/eslint-plugin-this) [![GitHub stars](https://img.shields.io/github/stars/matijs/eslint-plugin-this?style=flat)](https://github.com/matijs/eslint-plugin-this/stargazers) - Write pure functions, don't allow `this`.
- [toplevel](https://github.com/HKalbasi/eslint-plugin-toplevel) [![GitHub stars](https://img.shields.io/github/stars/HKalbasi/eslint-plugin-toplevel?style=flat)](https://github.com/HKalbasi/eslint-plugin-toplevel/stargazers) - An eslint plugin for disallow side effect at module toplevel.

### Performance

- [DOM](https://github.com/amilajack/eslint-plugin-dom) [![GitHub stars](https://img.shields.io/github/stars/amilajack/eslint-plugin-dom?style=flat)](https://github.com/amilajack/eslint-plugin-dom/stargazers)
- [Optimize Regex](https://github.com/BrainMaestro/eslint-plugin-optimize-regex) [![GitHub stars](https://img.shields.io/github/stars/BrainMaestro/eslint-plugin-optimize-regex?style=flat)](https://github.com/BrainMaestro/eslint-plugin-optimize-regex/stargazers) - Optimize regex literals.
- Perf-Standard [plugin](https://github.com/Raynos/eslint-plugin-perf-standard) [![GitHub stars](https://img.shields.io/github/stars/Raynos/eslint-plugin-perf-standard?style=flat)](https://github.com/Raynos/eslint-plugin-perf-standard/stargazers) and [Config](https://github.com/Raynos/eslint-config-perf-standard) [![GitHub stars](https://img.shields.io/github/stars/Raynos/eslint-config-perf-standard?style=flat)](https://github.com/Raynos/eslint-config-perf-standard/stargazers)

### Security

- [no-secrets](https://github.com/nickdeis/eslint-plugin-no-secrets) [![GitHub stars](https://img.shields.io/github/stars/nickdeis/eslint-plugin-no-secrets?style=flat)](https://github.com/nickdeis/eslint-plugin-no-secrets/stargazers) - An eslint plugin that detects potential secrets/credentials.
- [no-unsanitized](https://github.com/mozilla/eslint-plugin-no-unsanitized) [![GitHub stars](https://img.shields.io/github/stars/mozilla/eslint-plugin-no-unsanitized?style=flat)](https://github.com/mozilla/eslint-plugin-no-unsanitized/stargazers) - Checks for `innerHTML`, `outerHTML`, etc.
- [pii](https://github.com/shiva-hack/eslint-plugin-pii) [![GitHub stars](https://img.shields.io/github/stars/shiva-hack/eslint-plugin-pii?style=flat)](https://github.com/shiva-hack/eslint-plugin-pii/stargazers) - Checks and enforces PII Compliance of the code. i.e. no email address, birth date, IP address or phone number in comments or string literals.
- [pg](https://github.com/interlace-collie/eslint/tree/main/packages/eslint-plugin-pg) [![GitHub stars](https://img.shields.io/github/stars/interlace-collie/eslint/tree/main/packages/eslint-plugin-pg?style=flat)](https://github.com/interlace-collie/eslint/tree/main/packages/eslint-plugin-pg/stargazers) - PostgreSQL/node-postgres security: SQL injection prevention (CWE-89), connection pool leak detection (CWE-772), transaction safety. 13 rules with CWE mapping.
- [Security](https://github.com/nodesecurity/eslint-plugin-security) [![GitHub stars](https://img.shields.io/github/stars/nodesecurity/eslint-plugin-security?style=flat)](https://github.com/nodesecurity/eslint-plugin-security/stargazers) - ESLint rules for Node Security.
- [xss](https://github.com/Rantanen/eslint-plugin-xss) [![GitHub stars](https://img.shields.io/github/stars/Rantanen/eslint-plugin-xss?style=flat)](https://github.com/Rantanen/eslint-plugin-xss/stargazers) - Tries to detect XSS issues in codebase before they end up in production.

### Style

- [ESLint Stylistic](https://eslint.style/) - [Formatting and stylistic ESLint core rules moved to this project and are maintained by the community.](https://eslint.org/blog/2023/10/deprecating-formatting-rules/)
- [const case](https://www.npmjs.com/package/eslint-plugin-const-case) - Enforce capitalization of constant primitive literals.
- [editorconfig](https://github.com/platinumazure/eslint-plugin-editorconfig) [![GitHub stars](https://img.shields.io/github/stars/platinumazure/eslint-plugin-editorconfig?style=flat)](https://github.com/platinumazure/eslint-plugin-editorconfig/stargazers) - Derive rules from [`.editorconfig`](https://editorconfig.org/).
- [filenames](https://github.com/selaux/eslint-plugin-filenames) [![GitHub stars](https://img.shields.io/github/stars/selaux/eslint-plugin-filenames?style=flat)](https://github.com/selaux/eslint-plugin-filenames/stargazers) - Ensure consistent filenames for your JavaScript files. No longer maintained and does not work with ESlint 9 at all.
- [Simple import sort](https://github.com/lydell/eslint-plugin-simple-import-sort) [![GitHub stars](https://img.shields.io/github/stars/lydell/eslint-plugin-simple-import-sort?style=flat)](https://github.com/lydell/eslint-plugin-simple-import-sort/stargazers) - Easy autofixable import sorting.
- [perfectionist sorting](https://github.com/azat-io/eslint-plugin-perfectionist) [![GitHub stars](https://img.shields.io/github/stars/azat-io/eslint-plugin-perfectionist?style=flat)](https://github.com/azat-io/eslint-plugin-perfectionist/stargazers) - Sort objects, imports, TypeScript types, enums, JSX props, etc.
- [split-and-sort-imports](https://github.com/sngn/eslint-plugin-split-and-sort-imports) [![GitHub stars](https://img.shields.io/github/stars/sngn/eslint-plugin-split-and-sort-imports?style=flat)](https://github.com/sngn/eslint-plugin-split-and-sort-imports/stargazers) - Sorts imports and splits 'multiple' imports into single line imports.
- [Switch case](https://github.com/lukeapage/eslint-plugin-switch-case) [![GitHub stars](https://img.shields.io/github/stars/lukeapage/eslint-plugin-switch-case?style=flat)](https://github.com/lukeapage/eslint-plugin-switch-case/stargazers) - Switch-case-specific linting rules for ESLint.
- [padding](https://github.com/mu-io/eslint-plugin-padding) [![GitHub stars](https://img.shields.io/github/stars/mu-io/eslint-plugin-padding?style=flat)](https://github.com/mu-io/eslint-plugin-padding/stargazers) - Allows/disallows padding between statements.
- [paths](https://github.com/vitonsky/eslint-plugin-paths) [![GitHub stars](https://img.shields.io/github/stars/vitonsky/eslint-plugin-paths?style=flat)](https://github.com/vitonsky/eslint-plugin-paths/stargazers) - Use paths from tsconfig/jsconfig and auto fix relative paths to aliases.
- [@gitbutler/no-relative-imports](https://www.npmjs.com/package/@gitbutler/no-relative-imports) - Use paths from tsconfig and auto fix relative paths to aliases. Observes tsconfig inheritance.

### Testing Tools

- [AVA](https://github.com/avajs/eslint-plugin-ava) [![GitHub stars](https://img.shields.io/github/stars/avajs/eslint-plugin-ava?style=flat)](https://github.com/avajs/eslint-plugin-ava/stargazers) - Linting rules for AVA.
- Chai
  - [expect practices](https://github.com/turbo87/eslint-plugin-chai-expect) [![GitHub stars](https://img.shields.io/github/stars/turbo87/eslint-plugin-chai-expect?style=flat)](https://github.com/turbo87/eslint-plugin-chai-expect/stargazers)
  - [with unused expressions](https://github.com/ihordiachenko/eslint-plugin-chai-friendly) [![GitHub stars](https://img.shields.io/github/stars/ihordiachenko/eslint-plugin-chai-friendly?style=flat)](https://github.com/ihordiachenko/eslint-plugin-chai-friendly/stargazers)
  - [permitted keywords](https://github.com/gavinaiken/eslint-plugin-chai-expect-keywords) [![GitHub stars](https://img.shields.io/github/stars/gavinaiken/eslint-plugin-chai-expect-keywords?style=flat)](https://github.com/gavinaiken/eslint-plugin-chai-expect-keywords/stargazers)
  - [with chai-as-promised plugin](https://github.com/fintechstudios/eslint-plugin-chai-as-promised) [![GitHub stars](https://img.shields.io/github/stars/fintechstudios/eslint-plugin-chai-as-promised?style=flat)](https://github.com/fintechstudios/eslint-plugin-chai-as-promised/stargazers)
  <!-- lint disable double-link -->
  - [globals](https://github.com/t-huth/eslint-plugin-chai-assert-bdd) [![GitHub stars](https://img.shields.io/github/stars/t-huth/eslint-plugin-chai-assert-bdd?style=flat)](https://github.com/t-huth/eslint-plugin-chai-assert-bdd/stargazers)
- [Cucumber](https://github.com/darrinholst/eslint-plugin-cucumber) [![GitHub stars](https://img.shields.io/github/stars/darrinholst/eslint-plugin-cucumber?style=flat)](https://github.com/darrinholst/eslint-plugin-cucumber/stargazers) - Linting rules for Cucumber.
- [Cypress](https://github.com/cypress-io/eslint-plugin-cypress) [![GitHub stars](https://img.shields.io/github/stars/cypress-io/eslint-plugin-cypress?style=flat)](https://github.com/cypress-io/eslint-plugin-cypress/stargazers) - Linting rules for Cypress.
- [Jasmine](https://github.com/tlvince/eslint-plugin-jasmine) [![GitHub stars](https://img.shields.io/github/stars/tlvince/eslint-plugin-jasmine?style=flat)](https://github.com/tlvince/eslint-plugin-jasmine/stargazers) - Linting rules for Jasmine.
- Jest
  - [Enforcing practices](https://github.com/jest-community/eslint-plugin-jest) [![GitHub stars](https://img.shields.io/github/stars/jest-community/eslint-plugin-jest?style=flat)](https://github.com/jest-community/eslint-plugin-jest/stargazers) - Linting rules for Jest.
  - [Enforcing consistent formatting](https://github.com/dangreenisrael/eslint-plugin-jest-formatting) [![GitHub stars](https://img.shields.io/github/stars/dangreenisrael/eslint-plugin-jest-formatting?style=flat)](https://github.com/dangreenisrael/eslint-plugin-jest-formatting/stargazers) - Formatting rules for Jest.
  - [Jest-async](https://www.npmjs.com/package/eslint-plugin-jest-async) - Async linting rule for Jest.
  - [Jest-DOM](https://github.com/testing-library/eslint-plugin-jest-dom) [![GitHub stars](https://img.shields.io/github/stars/testing-library/eslint-plugin-jest-dom?style=flat)](https://github.com/testing-library/eslint-plugin-jest-dom/stargazers) - Linting rules for Jest-DOM.
- Vitest
  - [ESLint Plugin Vitest](https://github.com/vitest-dev/eslint-plugin-vitest) [![GitHub stars](https://img.shields.io/github/stars/vitest-dev/eslint-plugin-vitest?style=flat)](https://github.com/vitest-dev/eslint-plugin-vitest/stargazers) - ESLint plugin for Vitest.
- Mocha
  - [Enforcing practices](https://github.com/lo1tuma/eslint-plugin-mocha) [![GitHub stars](https://img.shields.io/github/stars/lo1tuma/eslint-plugin-mocha?style=flat)](https://github.com/lo1tuma/eslint-plugin-mocha/stargazers) - Linting rules for Mocha.
  - [Enforcing manageability](https://github.com/onechiporenko/eslint-plugin-mocha-cleanup/) [![GitHub stars](https://img.shields.io/github/stars/onechiporenko/eslint-plugin-mocha-cleanup/?style=flat)](https://github.com/onechiporenko/eslint-plugin-mocha-cleanup//stargazers)
- [Playwright](https://github.com/playwright-community/eslint-plugin-playwright) [![GitHub stars](https://img.shields.io/github/stars/playwright-community/eslint-plugin-playwright?style=flat)](https://github.com/playwright-community/eslint-plugin-playwright/stargazers) - Linting rules for Playwright.
- [QUnit](https://github.com/platinumazure/eslint-plugin-qunit) [![GitHub stars](https://img.shields.io/github/stars/platinumazure/eslint-plugin-qunit?style=flat)](https://github.com/platinumazure/eslint-plugin-qunit/stargazers) - Linting rules for QUnit.
- [TestCafe-Community](https://github.com/testcafe-community/eslint-plugin-testcafe-community) [![GitHub stars](https://img.shields.io/github/stars/testcafe-community/eslint-plugin-testcafe-community?style=flat)](https://github.com/testcafe-community/eslint-plugin-testcafe-community/stargazers) - TestCafe linting rules with env globals (fork from [TestCafe globals](https://github.com/miherlosev/eslint-plugin-testcafe) [![GitHub stars](https://img.shields.io/github/stars/miherlosev/eslint-plugin-testcafe?style=flat)](https://github.com/miherlosev/eslint-plugin-testcafe/stargazers)).
- [Testing Library](https://github.com/testing-library/eslint-plugin-testing-library) [![GitHub stars](https://img.shields.io/github/stars/testing-library/eslint-plugin-testing-library?style=flat)](https://github.com/testing-library/eslint-plugin-testing-library/stargazers) - Linting rules for Testing Library.

## Parsers

- [babel-eslint-parser](https://github.com/babel/babel/tree/main/eslint/babel-eslint-parser) [![GitHub stars](https://img.shields.io/github/stars/babel/babel/tree/main/eslint/babel-eslint-parser?style=flat)](https://github.com/babel/babel/tree/main/eslint/babel-eslint-parser/stargazers) - Allows you to lint ALL valid Babel code with the fantastic ESLint.
- [TypeScript](https://typescript-eslint.io/packages/parser) - A TypeScript parser that produces output compatible with ESLint.
- [BrightScript](https://github.com/RokuRoad/eslint-plugin-roku) [![GitHub stars](https://img.shields.io/github/stars/RokuRoad/eslint-plugin-roku?style=flat)](https://github.com/RokuRoad/eslint-plugin-roku/stargazers) - BrightScript plugin for Roku development. Includes Parser and Rules.
- [GraphQL](https://github.com/dotansimha/graphql-eslint) [![GitHub stars](https://img.shields.io/github/stars/dotansimha/graphql-eslint?style=flat)](https://github.com/dotansimha/graphql-eslint/stargazers) - Parser for the GraphQL AST. Includes parser, plugin, processor (for non-graphql files) and rules.

## Formatters

<!-- ignore is to keep "github" lower-case -->
<!--lint ignore awesome-spell-check-->

- [html](https://github.com/shuoshubao/eslint-formatter-html) [![GitHub stars](https://img.shields.io/github/stars/shuoshubao/eslint-formatter-html?style=flat)](https://github.com/shuoshubao/eslint-formatter-html/stargazers) - A enhanced ESLint formatter.
- [badger](https://github.com/brettz9/eslint-formatter-badger) [![GitHub stars](https://img.shields.io/github/stars/brettz9/eslint-formatter-badger?style=flat)](https://github.com/brettz9/eslint-formatter-badger/stargazers) - Make SVG-based badges summarizing ESLint results (e.g., for use on a README).
- [git-log](https://github.com/JamieMason/eslint-formatter-git-log) [![GitHub stars](https://img.shields.io/github/stars/JamieMason/eslint-formatter-git-log?style=flat)](https://github.com/JamieMason/eslint-formatter-git-log/stargazers) - ESLint Formatter featuring Git Author, Date, and Hash.
- [github](https://github.com/hipstersmoothie/eslint-formatter-github) [![GitHub stars](https://img.shields.io/github/stars/hipstersmoothie/eslint-formatter-github?style=flat)](https://github.com/hipstersmoothie/eslint-formatter-github/stargazers) - See ESLint errors and warnings directly in pull requests.
- [gitlab](https://gitlab.com/remcohaszing/eslint-formatter-gitlab) - Output ESLint results in the GitLab code quality results.
- [mo](https://github.com/fengzilong/eslint-formatter-mo) [![GitHub stars](https://img.shields.io/github/stars/fengzilong/eslint-formatter-mo?style=flat)](https://github.com/fengzilong/eslint-formatter-mo/stargazers) - Good-lookin' ESLint formatter and also for delightful reading experience.
- [SARIF](https://www.npmjs.com/package/@microsoft/eslint-formatter-sarif) - Generate a results in a SARIF format so it can be imported into tools like GitHub Advanced Security.
- [summary-chart](https://github.com/davidjbradshaw/eslint-formatter-summary-chart) [![GitHub stars](https://img.shields.io/github/stars/davidjbradshaw/eslint-formatter-summary-chart?style=flat)](https://github.com/davidjbradshaw/eslint-formatter-summary-chart/stargazers) - Format ESLint output into a bar chart.

## Globals

- [confusing-browser-globals](https://github.com/facebook/create-react-app/tree/main/packages/confusing-browser-globals) [![GitHub stars](https://img.shields.io/github/stars/facebook/create-react-app/tree/main/packages/confusing-browser-globals?style=flat)](https://github.com/facebook/create-react-app/tree/main/packages/confusing-browser-globals/stargazers) - A curated list of browser globals that commonly cause confusion and are not recommended to use without an explicit window. qualifier.
- [ES and browser globals](https://github.com/sindresorhus/globals) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/globals?style=flat)](https://github.com/sindresorhus/globals/stargazers) (originally from ESLint)
- [chai globals](https://github.com/t-huth/eslint-plugin-chai-assert-bdd) [![GitHub stars](https://img.shields.io/github/stars/t-huth/eslint-plugin-chai-assert-bdd?style=flat)](https://github.com/t-huth/eslint-plugin-chai-assert-bdd/stargazers)
- [TestCafe globals](https://github.com/miherlosev/eslint-plugin-testcafe) [![GitHub stars](https://img.shields.io/github/stars/miherlosev/eslint-plugin-testcafe?style=flat)](https://github.com/miherlosev/eslint-plugin-testcafe/stargazers) - `fixture` & `test` globals for TestCafe.

## Tools

- [es-file-traverse](https://github.com/brettz9/es-file-traverse) [![GitHub stars](https://img.shields.io/github/stars/brettz9/es-file-traverse?style=flat)](https://github.com/brettz9/es-file-traverse/stargazers) - Obtain a list of only those files which are in use based on imports and/or requires from an entry file or files; list passable to ESLint. Intended esp. for linting 3rd party dependencies.
- [eslint-find-rules](https://github.com/sarbbottam/eslint-find-rules) [![GitHub stars](https://img.shields.io/github/stars/sarbbottam/eslint-find-rules?style=flat)](https://github.com/sarbbottam/eslint-find-rules/stargazers) - Find built-in ESLint rules you don't have in your custom config.
- [eslint-index](https://github.com/wagerfield/eslint-index) [![GitHub stars](https://img.shields.io/github/stars/wagerfield/eslint-index?style=flat)](https://github.com/wagerfield/eslint-index/stargazers) - CLI for finding and managing rules in ESLint config files.
- [eslint-interactive](https://github.com/mizdra/eslint-interactive) [![GitHub stars](https://img.shields.io/github/stars/mizdra/eslint-interactive?style=flat)](https://github.com/mizdra/eslint-interactive/stargazers) - The CLI tool to fix huge number of ESLint errors.
- [eslint-multiplexer](https://github.com/pimlie/eslint-multiplexer) [![GitHub stars](https://img.shields.io/github/stars/pimlie/eslint-multiplexer?style=flat)](https://github.com/pimlie/eslint-multiplexer/stargazers) - Multiplex eslint results and merge results for common files.
- [eslint-nibble](https://github.com/IanVS/eslint-nibble) [![GitHub stars](https://img.shields.io/github/stars/IanVS/eslint-nibble?style=flat)](https://github.com/IanVS/eslint-nibble/stargazers) - Ease into ESLint, by fixing one rule at a time.
- [eslint-plugin-rule-adoption](https://github.com/Jugbot/eslint-plugin-rule-adoption) [![GitHub stars](https://img.shields.io/github/stars/Jugbot/eslint-plugin-rule-adoption?style=flat)](https://github.com/Jugbot/eslint-plugin-rule-adoption/stargazers) - An eslint plugin for incremental rule adoption, when `--fix` and codemods don't cut it.
- [eslint-rule-documentation](https://github.com/jfmengels/eslint-rule-documentation) [![GitHub stars](https://img.shields.io/github/stars/jfmengels/eslint-rule-documentation?style=flat)](https://github.com/jfmengels/eslint-rule-documentation/stargazers) - Find the url for the documentation of an ESLint rule.
- [ESlint Rules Index](https://eslint-rules-index.vercel.app/) - A big table of ESlint Rules to help developers find them easily.
- [eslint-watch](https://github.com/rizowski/eslint-watch) [![GitHub stars](https://img.shields.io/github/stars/rizowski/eslint-watch?style=flat)](https://github.com/rizowski/eslint-watch/stargazers) - Run ESLint with watch mode.
- [codacy-eslint](https://github.com/codacy/codacy-eslint) [![GitHub stars](https://img.shields.io/github/stars/codacy/codacy-eslint?style=flat)](https://github.com/codacy/codacy-eslint/stargazers) - Docker used at [Codacy](https://www.codacy.com) to run ESLint.
- [esprint](https://github.com/pinterest/esprint) [![GitHub stars](https://img.shields.io/github/stars/pinterest/esprint?style=flat)](https://github.com/pinterest/esprint/stargazers) - Run ESLint across multiple threads.
- [generator-eslint](https://github.com/eslint/generator-eslint) [![GitHub stars](https://img.shields.io/github/stars/eslint/generator-eslint?style=flat)](https://github.com/eslint/generator-eslint/stargazers) - Generate ESLint
  plugin and rules with [Yeoman](http://yeoman.io/).
- [editor-info](https://github.com/fisker/editor-info) [![GitHub stars](https://img.shields.io/github/stars/fisker/editor-info?style=flat)](https://github.com/fisker/editor-info/stargazers) - Detect whether one is within an editor/IDE and which type, allowing one to tweak ESLint configuration accordingly.
- [eslint-dashboard](https://github.com/fengzilong/eslint-dashboard) [![GitHub stars](https://img.shields.io/github/stars/fengzilong/eslint-dashboard?style=flat)](https://github.com/fengzilong/eslint-dashboard/stargazers) - Interactive ESLint workflow that lives in your terminal.
- [eslint-remote-tester](https://github.com/AriPerkkio/eslint-remote-tester) [![GitHub stars](https://img.shields.io/github/stars/AriPerkkio/eslint-remote-tester?style=flat)](https://github.com/AriPerkkio/eslint-remote-tester/stargazers) - CLI tool for testing given ESlint rules against multiple repositories at once.
- [eslint-disable-autofix](https://github.com/MorevM/eslint-disable-autofix/) [![GitHub stars](https://img.shields.io/github/stars/MorevM/eslint-disable-autofix/?style=flat)](https://github.com/MorevM/eslint-disable-autofix//stargazers) - Utility to disable autofix for specific ESLint rules.

## Developing for ESLint

- [eslint-doc-generator](https://github.com/bmish/eslint-doc-generator) [![GitHub stars](https://img.shields.io/github/stars/bmish/eslint-doc-generator?style=flat)](https://github.com/bmish/eslint-doc-generator/stargazers) - Generate documentation for your ESLint plugin including a rules table for your readme and header for your rule docs.
- [eslint-docgen](https://github.com/wikimedia/eslint-docgen) [![GitHub stars](https://img.shields.io/github/stars/wikimedia/eslint-docgen?style=flat)](https://github.com/wikimedia/eslint-docgen/stargazers) - Automatically generate ESLint plugin documentation from rule metadata and test cases.

## Tutorials

- [Creating an ESLint Plugin](https://medium.com/tumblbug-engineering/creating-an-eslint-plugin-87f1cb42767f) - Article walking through the creation of an ESLint rule and plugin.
- [Lint Like It's 2015](https://medium.com/@dan_abramov/lint-like-it-s-2015-6987d44c5b48#.5p3yk0b03) - Article walking through the benefits of using ESLint.
- [Writing a rule to spot undeclared props hiding in plain sight](http://blog.cowchimp.com/writing-a-custom-eslint-rule-to-spot-undeclared-props/) - Article about creating rules that require scope analysis.
- [Dear Old ESLint](https://adropincalm.com/blog/dear-old-eslint/) - Quick intro article on ESLint.

## Installation and Setup

- [Lintier](https://github.com/josh-stillman/lintier) [![GitHub stars](https://img.shields.io/github/stars/josh-stillman/lintier?style=flat)](https://github.com/josh-stillman/lintier/stargazers) - CLI to quickly scaffold an ESLint & Prettier setup in a TypeScript project.
