# Visual Regression Testing

[![GitHub stars](https://img.shields.io/github/stars/mojoaxel/awesome-regression-testing?style=flat)](https://github.com/mojoaxel/awesome-regression-testing/stargazers)

# Awesome Visual Regression Testing [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> Curated list of awesome visual regression testing resources.

Regression testing is a type of software testing which verifies that software which was previously developed and tested still performs the same way after it was changed or interfaced with other software. The purpose of regression testing is to ensure that changes to the software have not introduced new faults.

## Foreword

This is intended to be an *incomplete* list of resources about visual regression testing. It is not tailored to a specific area or role (Developer/QA/UX-Designer). Note that this is for all areas of regression software testing *after* the code in question is written. For a awesome list on general software testing see e.g. [awesome-testing](https://github.com/TheJambo/awesome-testing) [![GitHub stars](https://img.shields.io/github/stars/TheJambo/awesome-testing?style=flat)](https://github.com/TheJambo/awesome-testing/stargazers).

Finally, I'm sure everyone who reads this list has one thing they want to add. Please read the [How to Contribute](.github/CONTRIBUTING.md) page and **Feel free to add to the list!!**. If you think this is helpful **Please give a Star ⭐️**.

## Contents

- [General information](#general-information)
- [Browser automation](#browser-automation)
- [Tools and frameworks](#tools-and-frameworks)
- [Online services](#online-services)
- [Blog posts](#blog-posts)
- [Slideshows, talks and videos](#slideshows-talks-and-videos)
- [Deprecated](#deprecated)
- [Miscellaneous](#Miscellaneous)
  - [Contributing](#contributing)
  - [Code of Conduct](#code-of-conduct)
  - [License](#license)

## General information

- [Survey of screenshot-based CSS testing tools](https://gist.github.com/cvrebert/adf91e429906a4d746cd)
- [Wikipedia: Regression testing](https://en.wikipedia.org/wiki/Regression_testing)

## Browser automation

- [Cypress.io](https://www.cypress.io/) - An automation framework that runs in-browser.
- [Selenium](https://github.com/SeleniumHQ/selenium) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium?style=flat)](https://github.com/SeleniumHQ/selenium/stargazers) - Browser automation framework and ecosystem.
- [SlimerJS](https://github.com/laurentj/slimerjs) [![GitHub stars](https://img.shields.io/github/stars/laurentj/slimerjs?style=flat)](https://github.com/laurentj/slimerjs/stargazers) - Scriptable browser like PhantomJS, based on Firefox.
- [Webdriver.io](https://github.com/webdriverio/webdriverio/) [![GitHub stars](https://img.shields.io/github/stars/webdriverio/webdriverio/?style=flat)](https://github.com/webdriverio/webdriverio//stargazers) - Node.js bindings implementation for the W3C WebDriver protocol.

## Tools and frameworks (a-z↓)

- [AET](https://github.com/Cognifide/aet) [![GitHub stars](https://img.shields.io/github/stars/Cognifide/aet?style=flat)](https://github.com/Cognifide/aet/stargazers) - Scalable testing tool providing visual regression testing, accessibility and performance validation, markup analysis and more.
- [AyeSpy](https://github.com/newsuk/ayespy) [![GitHub stars](https://img.shields.io/github/stars/newsuk/ayespy?style=flat)](https://github.com/newsuk/ayespy/stargazers) - 44 image comparisons in 90 seconds.
- [BackstopJS](https://github.com/garris/BackstopJS) [![GitHub stars](https://img.shields.io/github/stars/garris/BackstopJS?style=flat)](https://github.com/garris/BackstopJS/stargazers) - Config-driven automated screenshot test framework.
- [basset](https://basset.io) - Open source platform for generating and reviewing visual differences. Supports multiple browsers, integrations for github and slack.
- [BitDive](https://bitdive.io/) - BitDive is a zero-code regression testing tool for Java/Kotlin applications. It captures real runtime behavior (methods, SQL, HTTP) and enables Live Context Replay with automatic mocking to detect semantic drift between versions.
- [BFFless](https://bffless.app) - Self-hosted platform for hosting and viewing visual regression screenshots from CI/CD pipelines with GitHub Actions integration.
- [Chimp](https://github.com/xolvio/chimp) [![GitHub stars](https://img.shields.io/github/stars/xolvio/chimp?style=flat)](https://github.com/xolvio/chimp/stargazers) - Develop acceptance tests & end-to-end tests with realtime feedback.
- [CodeceptJS](https://github.com/codeception/codeceptjs/) [![GitHub stars](https://img.shields.io/github/stars/codeception/codeceptjs/?style=flat)](https://github.com/codeception/codeceptjs//stargazers) - Modern Era Acceptance Testing Framework for NodeJS.
- [Creevey](https://github.com/wKich/creevey) [![GitHub stars](https://img.shields.io/github/stars/wKich/creevey?style=flat)](https://github.com/wKich/creevey/stargazers) - Cross-browser visual testing with magic. Feature-rich tool with UI Runner, Tests Hot Reloading, Docker and Storybook integration.
- [CSSCritic](https://github.com/cburgmer/csscritic) [![GitHub stars](https://img.shields.io/github/stars/cburgmer/csscritic?style=flat)](https://github.com/cburgmer/csscritic/stargazers) - Lightweight CSS regression testing.
- [Differencify](https://github.com/NimaSoroush/differencify) [![GitHub stars](https://img.shields.io/github/stars/NimaSoroush/differencify?style=flat)](https://github.com/NimaSoroush/differencify/stargazers) - A library for visual regression testing using [Puppeteer](https://github.com/GoogleChrome/puppeteer) [![GitHub stars](https://img.shields.io/github/stars/GoogleChrome/puppeteer?style=flat)](https://github.com/GoogleChrome/puppeteer/stargazers).
- [DiffGoblin Action](https://github.com/neg-0/diffgoblin-action) [![GitHub stars](https://img.shields.io/github/stars/neg-0/diffgoblin-action?style=flat)](https://github.com/neg-0/diffgoblin-action/stargazers) - GitHub Action that screenshots two URLs and posts a visual diff as a PR comment. Zero config, no external service needed.
- [ember-visual-test](https://github.com/Cropster/ember-visual-test) [![GitHub stars](https://img.shields.io/github/stars/Cropster/ember-visual-test?style=flat)](https://github.com/Cropster/ember-visual-test/stargazers) - Simple visual regression testing for [Ember](https://emberjs.com/).
- [FuncUnit](https://github.com/bitovi/funcunit) [![GitHub stars](https://img.shields.io/github/stars/bitovi/funcunit?style=flat)](https://github.com/bitovi/funcunit/stargazers) - A functional test suite based on jQuery
- [Frostbyte Screenshot Action](https://github.com/OzorOwn/frostbyte-screenshot-action) [![GitHub stars](https://img.shields.io/github/stars/OzorOwn/frostbyte-screenshot-action?style=flat)](https://github.com/OzorOwn/frostbyte-screenshot-action/stargazers) - GitHub Action for automated website screenshots in CI/CD. API-based (no local browser), supports 5 viewports, full-page capture, dark mode.
- [Galen](https://github.com/galenframework/galen) [![GitHub stars](https://img.shields.io/github/stars/galenframework/galen?style=flat)](https://github.com/galenframework/galen/stargazers) - Java framework based on [Selenium](https://github.com/SeleniumHQ/selenium) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium?style=flat)](https://github.com/SeleniumHQ/selenium/stargazers).
- [gatling](https://github.com/gabrielrotbart/gatling) [![GitHub stars](https://img.shields.io/github/stars/gabrielrotbart/gatling?style=flat)](https://github.com/gabrielrotbart/gatling/stargazers) - Integrated visual RSpec matcher which makes real visual testing easy (Ruby).
- [grunt-photobox](https://github.com/stefanjudis/grunt-photobox) [![GitHub stars](https://img.shields.io/github/stars/stefanjudis/grunt-photobox?style=flat)](https://github.com/stefanjudis/grunt-photobox/stargazers) - Plugin to prevent your project of broken layout via screenshot photo sessions of your site.
- [Happo](https://github.com/happo/happo.io) [![GitHub stars](https://img.shields.io/github/stars/happo/happo.io?style=flat)](https://github.com/happo/happo.io/stargazers) - Visual diffing in CI for user interfaces.
- [Hardy](https://github.com/thingsinjars/Hardy) [![GitHub stars](https://img.shields.io/github/stars/thingsinjars/Hardy?style=flat)](https://github.com/thingsinjars/Hardy/stargazers) - Selenium-driven, cucumber-powered CSS testing.
- [jest-image-snapshot](https://github.com/americanexpress/jest-image-snapshot) [![GitHub stars](https://img.shields.io/github/stars/americanexpress/jest-image-snapshot?style=flat)](https://github.com/americanexpress/jest-image-snapshot/stargazers) - Jest matcher that performs image comparisons using [pixelmatch](https://www.npmjs.com/package/pixelmatch)
- [jest-puppeteer-react](https://github.com/Hapag-Lloyd/jest-puppeteer-react) [![GitHub stars](https://img.shields.io/github/stars/Hapag-Lloyd/jest-puppeteer-react?style=flat)](https://github.com/Hapag-Lloyd/jest-puppeteer-react/stargazers) - Visual regression testing with Jest and puppeteer for React components
- [Karma](http://karma-runner.github.io/latest/index.html) - A test runner by the AngularJS team, that fits all our needs.
- [Lastest](https://github.com/las-team/lastest) [![GitHub stars](https://img.shields.io/github/stars/las-team/lastest?style=flat)](https://github.com/las-team/lastest/stargazers) - Visual regression testing platform built on Playwright with screenshot diffing, baseline review, and AI flake triage. Self-hostable via docker-compose or k8s.
- [Loki](https://github.com/oblador/loki) [![GitHub stars](https://img.shields.io/github/stars/oblador/loki?style=flat)](https://github.com/oblador/loki/stargazers) - Visual regression testing for Storybook using Chrome in docker et al.
- [Look-alike](https://github.com/kdzwinel/Look-alike) [![GitHub stars](https://img.shields.io/github/stars/kdzwinel/Look-alike?style=flat)](https://github.com/kdzwinel/Look-alike/stargazers) - Chrome Extension for taking and comparing screenshots.
- [Lost Pixel](https://github.com/lost-pixel/lost-pixel) [![GitHub stars](https://img.shields.io/github/stars/lost-pixel/lost-pixel?style=flat)](https://github.com/lost-pixel/lost-pixel/stargazers) - Holistic visual regression testing for full pages, components (via Storybook and Ladle integration), and custom shots (e.g. via Cypress).
- [Muppeteer](https://github.com/HuddleEng/Muppeteer) [![GitHub stars](https://img.shields.io/github/stars/HuddleEng/Muppeteer?style=flat)](https://github.com/HuddleEng/Muppeteer/stargazers) - Visual regression testing framework for Chrome using [Mocha](https://mochajs.org/) and [Puppeteer](https://github.com/GoogleChrome/puppeteer) [![GitHub stars](https://img.shields.io/github/stars/GoogleChrome/puppeteer?style=flat)](https://github.com/GoogleChrome/puppeteer/stargazers).
- [Needle](https://github.com/python-needle/needle) [![GitHub stars](https://img.shields.io/github/stars/python-needle/needle?style=flat)](https://github.com/python-needle/needle/stargazers) - Needle is a tool for testing visuals with Selenium and nose (Python).
- [Nightmare](https://github.com/segmentio/nightmare) [![GitHub stars](https://img.shields.io/github/stars/segmentio/nightmare?style=flat)](https://github.com/segmentio/nightmare/stargazers) - High-level browser automation library based on Electron.
- [Nightwatch](https://github.com/nightwatchjs/nightwatch) [![GitHub stars](https://img.shields.io/github/stars/nightwatchjs/nightwatch?style=flat)](https://github.com/nightwatchjs/nightwatch/stargazers) - Automated testing and continuous integration framework based on Node.js and using the Webdriver protocol.
- [OSnap](https://github.com/eWert-Online/osnap) [![GitHub stars](https://img.shields.io/github/stars/eWert-Online/osnap?style=flat)](https://github.com/eWert-Online/osnap/stargazers) - The speedy and easy to use Snapshot Testing tool for your project (1200 snapshots will run in under 3 minutes).
- [Playwright](https://github.com/microsoft/playwright) [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright?style=flat)](https://github.com/microsoft/playwright/stargazers) - Node library to automate Chromium, Firefox and WebKit with a single API.
- [Protractor](https://github.com/angular/protractor) [![GitHub stars](https://img.shields.io/github/stars/angular/protractor?style=flat)](https://github.com/angular/protractor/stargazers) - E2E test framework for Angular apps.
- [Puppeteer](https://github.com/GoogleChrome/puppeteer) [![GitHub stars](https://img.shields.io/github/stars/GoogleChrome/puppeteer?style=flat)](https://github.com/GoogleChrome/puppeteer/stargazers) - Headless Google Chrome Node API.
- [qd_screenshottests](https://www.drupal.org/project/qd_screenshottests) - CasperJS-based UI regression and functional testing focused on Drupal 8 sites.
- [reg-cli](https://github.com/bokuweb/reg-cli) [![GitHub stars](https://img.shields.io/github/stars/bokuweb/reg-cli?style=flat)](https://github.com/bokuweb/reg-cli/stargazers) - Visual regression test tool which output easy-to-read single file html report.
- [reg-suit](https://github.com/reg-viz/reg-suit) [![GitHub stars](https://img.shields.io/github/stars/reg-viz/reg-suit?style=flat)](https://github.com/reg-viz/reg-suit/stargazers) - Visual regression testing suite which compares images, stores snapshots, and notifies the difference to your GitHub repo.
- [ResembleJS](https://github.com/Huddle/Resemble.js) [![GitHub stars](https://img.shields.io/github/stars/Huddle/Resemble.js?style=flat)](https://github.com/Huddle/Resemble.js/stargazers) - Analyse and compare images with Javascript and HTML5.
- [Selenide](https://github.com/selenide/selenide) [![GitHub stars](https://img.shields.io/github/stars/selenide/selenide?style=flat)](https://github.com/selenide/selenide/stargazers) - Framework powered by Selenium WebDriver for writing easy-to-read and easy-to-maintain automated tests in Java.
- [Shoov](https://github.com/shoov/shoov) [![GitHub stars](https://img.shields.io/github/stars/shoov/shoov?style=flat)](https://github.com/shoov/shoov/stargazers) - UI regression and functional testing focused on Drupal 7 sites.
- [Spectre](https://github.com/wearefriday/spectre) [![GitHub stars](https://img.shields.io/github/stars/wearefriday/spectre?style=flat)](https://github.com/wearefriday/spectre/stargazers) - Provides image comparison capabilities and an admin interface for managing screenshots.
- [test-crawler](https://github.com/apiel/test-crawler) [![GitHub stars](https://img.shields.io/github/stars/apiel/test-crawler?style=flat)](https://github.com/apiel/test-crawler/stargazers) - Visual regression testing, by crawling a website and providing snapshot comparison reports.
- [TestCafe](https://github.com/DevExpress/testcafe) [![GitHub stars](https://img.shields.io/github/stars/DevExpress/testcafe?style=flat)](https://github.com/DevExpress/testcafe/stargazers) - Automated browser testing for the modern web development stack.
- [Touca](https://github.com/trytouca/trytouca) [![GitHub stars](https://img.shields.io/github/stars/trytouca/trytouca?style=flat)](https://github.com/trytouca/trytouca/stargazers) - Open source continuous regression testing without the hassle of managing snapshot files.
- [vrtest](https://github.com/nathanmarks/vrtest) [![GitHub stars](https://img.shields.io/github/stars/nathanmarks/vrtest?style=flat)](https://github.com/nathanmarks/vrtest/stargazers) - JavaScript library for running visual regression tests on your components cross browser via selenium.
- [wdio-visual-regression](https://github.com/ennjin/wdio-visual-regression) [![GitHub stars](https://img.shields.io/github/stars/ennjin/wdio-visual-regression?style=flat)](https://github.com/ennjin/wdio-visual-regression/stargazers) - Visual regression tool for webdriver.io
- [Wendigo](https://github.com/angrykoala/wendigo) [![GitHub stars](https://img.shields.io/github/stars/angrykoala/wendigo?style=flat)](https://github.com/angrykoala/wendigo/stargazers) - Test-oriented browser automation library based on Puppeteer.
- [Wraith](https://github.com/BBC-News/wraith) [![GitHub stars](https://img.shields.io/github/stars/BBC-News/wraith?style=flat)](https://github.com/BBC-News/wraith/stargazers) - Easy to use ruby tool with docker support.
- [Zombie.js](http://zombie.js.org/) - Insanely fast, headless full-stack testing using Node.js.

## Online services (a-z↓)

- [applitools](https://applitools.com) - Cloud base visual tests.
- [Argos](https://argos-ci.com) - The open source visual testing platform for modern engineering teams.
- [Axcept](https://axcept.io) - Testing for the whole team. Up to 100 tests in parallel. Endpoint Mocking. Code Coverage. 
- [Browser Shots](http://browsershots.org) - Screenshots only.
- [browserling](https://www.browserling.com) - LIVE interactive cross-browser testing.
- [BrowserStack](https://www.browserstack.com) - Free for Open Source. Supports [Selenium Webdriver](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver?style=flat)](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver/stargazers).
- [BugBug.io](https://bugbug.io/) - Lightweight test automation tool for web applications. Easy to learn and doesn't require coding. It's free, with unlimited tests. For an additional monthly fee, you also get cloud monitoring and CI/CD integration.
- [Chromatic](https://www.chromatic.com/) - Visual testing and UI review for component libraries. Cloud-based. [Video](https://youtu.be/6KDLJBcutQE)
- [CrossBrowserTesting](https://crossbrowsertesting.com) - Manual & exploratory testing on 1500+ real browsers and mobile devices.
- [Diffy](https://diffy.website) - Cloud based visual regression tool that focuses on Drupal and WordPress. Full page screenshots and minimal number of false positives. Just provide URLs of your sites to get started. No coding required.
- [Fluxguard](https://fluxguard.com) - Screenshot pixel and DOM change comparisons and regressions.
- [Ghost Inspector](https://ghostinspector.com) - See [introduction video](https://vimeo.com/ghostinspector/intro).
- [Happo](https://happo.io/) - Cloud-based screenshot testing service with support for multiple browsers.
- [HeadSpin](https://www.headspin.io/) - HeadSpin's Regression testing gives you a powerful comparison tool for analysing degradation across new app builds, OS releases, feature additions, locations, and more.
- [Keploy](https://keploy.io) - Open-source regression testing tool that automatically generates test cases and mocks from real API calls.

- [LambdaTest](https://www.lambdatest.com/) - Perform Automated and Live Interactive Cross Browser Testing on 2000+ Real Browsers and Operating Systems Online.
- [Meticulous.ai](https://meticulous.ai) - Easily create frontend tests without writing code. Use Meticulous to record workflows on your web app. You can then replay those flows on new frontend code, and create a test by diffing two replays.
- [Micoo](https://github.com/Mikuu/Micoo) [![GitHub stars](https://img.shields.io/github/stars/Mikuu/Micoo?style=flat)](https://github.com/Mikuu/Micoo/stargazers) - Open source service for all UI application visual regression solution
- [MyVisReg](https://myvisreg.com) – Run visual regression tests directly in your browser with no installs or setup.
- [PageBolt](https://pagebolt.dev) - Screenshot, video recording, PDF, and page inspection API with device emulation, ad blocking, and cookie banner removal.
- [percy.io](https://percy.io) - Continuous visual reviews for web apps.
- [Pixeleye](https://pixeleye.io/home) - Open-source, multi-browser visual review and testing platform with the option to self-host. It has first-class support for Storybook, Cypress, Playwright & Puppeteer. 
- [Preflight: Cypress Recorder](https://cypress.preflight.com) - Create AI-powered Cypress Tests/POM models in your browser and automate Email & Visual testing for Cypress.
- [Preflight](https://preflight.com) - Easiest Visual regression testing and Automated Web Testing tool. (Limited) free use.
- [Reflect](https://reflect.run) - Visual regression testing and test automation tool.
- [screener.io](https://screener.io) - For React, looks open source.
- [screenster.io](http://screenster.io) - Cloud based automation testing platform for web and mobile UI.
- [Sherlo](https://github.com/sherlo-io/sherlo) [![GitHub stars](https://img.shields.io/github/stars/sherlo-io/sherlo?style=flat)](https://github.com/sherlo-io/sherlo/stargazers) - Visual testing platform for React Native Storybook. Captures screenshots on iOS and Android simulators in the cloud and detects visual changes automatically.
- [TestGrid](https://www.testgrid.io/) - Perform End to End test automation be it cross browser testing, mobile app testing, performance testing or API testing on cloud or on-premise.
- [TestingBot](https://testingbot.com) - Provides +3600 browsers to run automated visual tests. Free for Open Source.
- [Testomat.io Reporter](https://github.com/testomatio/reporter) [![GitHub stars](https://img.shields.io/github/stars/testomatio/reporter?style=flat)](https://github.com/testomatio/reporter/stargazers) - Allows to collect tests to a Test Case Management System (TCMS) like testomat.io and sync manual and automated tests in one place.
- [testRigor](https://testrigor.com) - E2E functional test automation tool for web, mobile, and desktop tests.
- [Vidiff](https://vidiff.com) - Cloud-based visual regression testing across stages.
- [Visual Knight](https://visual-knight.io/) - Cloud-based visual testing platform with realtime results for testing tools.
- [Visual Regression Tracker](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker) [![GitHub stars](https://img.shields.io/github/stars/Visual-Regression-Tracker/Visual-Regression-Tracker?style=flat)](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker/stargazers) - Open Source selfhosted service for visual regression testing
- [VisWiz.io](https://www.viswiz.io) - Flexible visual regression testing service.
- [VRTs - Visual Regression Tests](https://bleech.de/en/products/visual-regression-tests/) – WordPress plugin auto-updating screenshots on content updates, preventing false positives.
- [Wopee.io](https://wopee.io) - Autonomous visual regression testing platform with AI-powered test agents. Integrates with Playwright, Cypress, and Robot Framework.

## Blog posts  (a-z↓)

- [Angela Riggs: Visual Regression Testing with BackstopJS](https://www.metaltoad.com/blog/visual-regression-testing-backstopjs) - Tutorial using BackstopJS.
- [Automated screenshot comparison tests with headless Chrome, Puppeteer and Pixelmatch, in Bitbucket pipeline](https://jakobzanker.de/blog/automated-screenshot-comparison-test-with-headless-chrome-in-bitbucket-pipeline/)
- [Automatic visual diffing with Puppeteer](https://meowni.ca/posts/2017-puppeteer-tests/)
- [Chromeless, Chrominator, Chromy, Navalia, Lambdium, GhostJS, AutoGCD](https://medium.com/@kensoh/chromeless-chrominator-chromy-navalia-lambdium-ghostjs-autogcd-ef34bcd26907) - Headless Chrome is shaking up traditional approaches to test automation.
- [CodeLift: Introduction to Diffy for Visual Regression Testing](https://codelift.ai/resources/tech-articles/introduction-diffy-visual-regression-testing) - Catch visual and functional issues before they reach production.
- [Everything you need to know about Visual Regression Testing in 2022](https://david-x.medium.com/the-state-of-visual-regression-testing-in-2022-5de10ffe8f6f) - Intro to visual regression testing with tools updated as of 2022.
- [Garris Shipon: Automating CSS Regression Testing](https://css-tricks.com/automating-css-regression-testing/) - Tutorial using BackstopJS.
- [Garris Shipon: Visual Regression Testing For Angular Applications](https://davidwalsh.name/visual-regression-testing-angular-applications) -  Tutorial using BackstopJS.
- [Keeping a React Design System consistent: using visual regression testing to save time and headaches](https://techblog.commercetools.com/keeping-a-react-design-system-consistent-f055160d5166) - Using percy, and jest puppeteer to visually test a React component library.
- [Kevin Lamping: The 5 best visual regression testing tools](http://www.creativebloq.com/features/the-5-best-visual-regression-testing-tools) - Compares: Wraith, PhantomCSS, Gemini, WebdriverCSS and Spectre.
- [Make visual regression testing easier](https://medium.com/@nima.soroush.h/make-visual-regression-testing-easier-4a3dc7073737) - Introduction to [Differencify](https://github.com/NimaSoroush/differencify) [![GitHub stars](https://img.shields.io/github/stars/NimaSoroush/differencify?style=flat)](https://github.com/NimaSoroush/differencify/stargazers) and how to use it.
- [Pavels Jelisejevs: Visual Regression Testing with PhantomCSS](https://www.sitepoint.com/visual-regression-testing-with-phantomcss) - Introduction to PhantomCSS.
- [Phillip Gourley: Making visual regression useful](https://medium.com/@philgourley/making-visual-regression-useful-acfae27e5031) - Why you should use BackstopJS.
- [Poor man's visual regression testing](https://idkshite.com/posts/compare-visual-changes) - Improved manual visual regression testing with the PerfectPixel chrome plugin.
- [theheadless.dev](https://theheadless.dev) - Blog with practical guides and runnable examples on Playwright and Puppeteer.
- [UI Visual Regression Testing with Micoo](https://mikuu.medium.com/ui-visual-regression-testing-with-micoo-12c7a4a036b9) - Introduction about how to do visual regression testing with Micoo service
- [Visual Regression Test with WebdriverIO & WebdriverCSS](https://medium.com/@dalenguyen/visual-regression-test-with-webdriverio-webdrivercss-d7675a1812b2) - Tutorial using WebdriverIO and WebdriverCSS with Spec Reporter
- [Visual regression testing for Hugo with Github-CI and BackstopJS](https://jameskiefer.com/posts/visual-regression-testing-for-hugo-with-github-ci-and-backstopjs/) - How to automate regression testing for Hugo with BackstopJS
- [Visual regression testing using Jest, Chromeless and AWS Lambda](https://github.com/novemberfiveco/visual-regression-testing-jest-chromeless) [![GitHub stars](https://img.shields.io/github/stars/novemberfiveco/visual-regression-testing-jest-chromeless?style=flat)](https://github.com/novemberfiveco/visual-regression-testing-jest-chromeless/stargazers) - Tutorial using Chromeless and jest-image-snapshot.
- [Visual Regression Testing with Puppeteer & Jest](https://www.viswiz.io/help/tutorials/puppeteer) - Tutorial to setup visual testing with Puppeteer, Jest and VisWiz.io.

## Slideshows, talks and videos  (a-z↓)

- [CSS Regression Testing with Wraith](https://youtu.be/gE_19L0l2q0) - Screencast: Basic introduction to wraith, a screenshot comparison tool.
- [Cypress in 100 Seconds](https://www.youtube.com/watch?v=BQqzfHQkREo&ab_channel=Fireship) - Introduction video by Fireship.
- [Look-alike - visual regression testing tool](https://youtu.be/vTyoQuC0To8) - Demo what the Look-alike Chrome extension is, how it works and how and why it was build.
- [Screencast on CSS critic - a lightweight testing framework for CSS](https://youtu.be/AqQ2bNPtF60) - How to write your first CSS test with CSS critic, make it pass, break it, and make it pass again.
- [Screenster Tutorial](https://youtu.be/Zy8y_dGzZXI) - Tutorial on how to create visual automated tests with Screenster.
- [Visual Regression Testing - from a tool to a process](https://speakerdeck.com/nikhilverma/visual-regression-testing-from-a-tool-to-a-process) by Nikhil Verma - How the Mobile Web team in Badoo converted and integrated PhantomCSS into their workflow and connected it to their CI process.
- [Visual Regression Testing with PhantomCSS](https://youtu.be/Vp8vnXMjIfw) - Talk by Jon Bellah on how to use PhantomCSS during wordpress development.
- [Visual Regression Testing with Shoov](https://youtu.be/CBBiJ6YlXLc) - How to setup shoov and get your first test written.
- [Visual Regression Testing: Sanity Checks With BackstopJS](https://youtu.be/l8lGj8Zh0k4) - Screencast with code demo and best practices.
- [Scaling up your Screenshot Testing, without the Friction](https://www.youtube.com/watch?v=9sarjgIHF2g) - Mobile focussed talk from Droidcon/Fluttercon India. Explains the bottlenecks with scaling up screenshot testing and how to solve them.

## Deprecated  (a-z↓)

The following projects are no longer maintained actively but are still worth mentioning because of their user base.

- [CasperJS](https://github.com/casperjs/casperjs) [![GitHub stars](https://img.shields.io/github/stars/casperjs/casperjs?style=flat)](https://github.com/casperjs/casperjs/stargazers) - Navigation scripting and testing utility for PhantomJS and SlimerJS. (archived 2018)
- [Chromeless](https://github.com/graphcool/chromeless) [![GitHub stars](https://img.shields.io/github/stars/graphcool/chromeless?style=flat)](https://github.com/graphcool/chromeless/stargazers) - Chrome automation made simple. Runs locally or headless on AWS Lambda. (archived 2018)
- [DalekJS](https://github.com/dalekjs/dalek) [![GitHub stars](https://img.shields.io/github/stars/dalekjs/dalek?style=flat)](https://github.com/dalekjs/dalek/stargazers) - Automated cross browser testing with JavaScript. No longer maintained since 4 Jun 2017.
- [dpxdt](https://github.com/bslatkin/dpxdt) [![GitHub stars](https://img.shields.io/github/stars/bslatkin/dpxdt?style=flat)](https://github.com/bslatkin/dpxdt/stargazers) - End-to-end testing with Python.
- [Gemini](https://github.com/gemini-testing/gemini) [![GitHub stars](https://img.shields.io/github/stars/gemini-testing/gemini?style=flat)](https://github.com/gemini-testing/gemini/stargazers) - Feature rich framework with support for [Selenium](https://github.com/SeleniumHQ/selenium) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium?style=flat)](https://github.com/SeleniumHQ/selenium/stargazers) and  [CasperJS](https://github.com/casperjs/casperjs) [![GitHub stars](https://img.shields.io/github/stars/casperjs/casperjs?style=flat)](https://github.com/casperjs/casperjs/stargazers). Gemini is deprecated, use hermione instead.
- [Huxley](https://github.com/facebookarchive/huxley) [![GitHub stars](https://img.shields.io/github/stars/facebookarchive/huxley?style=flat)](https://github.com/facebookarchive/huxley/stargazers) - Python framework based on [Selenium Webdriver](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver?style=flat)](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver/stargazers).
- [Navalia](https://github.com/joelgriffith/navalia) [![GitHub stars](https://img.shields.io/github/stars/joelgriffith/navalia?style=flat)](https://github.com/joelgriffith/navalia/stargazers) - Browser Automation based on headless Chrome and GraphQL. (archived 2018)
- [OcularJS](https://github.com/mmacartney10/ocularjs) [![GitHub stars](https://img.shields.io/github/stars/mmacartney10/ocularjs?style=flat)](https://github.com/mmacartney10/ocularjs/stargazers) - uses [PhantomJS](https://github.com/ariya/phantomjs) [![GitHub stars](https://img.shields.io/github/stars/ariya/phantomjs?style=flat)](https://github.com/ariya/phantomjs/stargazers).
- [PhantomCSS](https://github.com/Huddle/PhantomCSS) [![GitHub stars](https://img.shields.io/github/stars/Huddle/PhantomCSS?style=flat)](https://github.com/Huddle/PhantomCSS/stargazers) - Visual/CSS regression testing with PhantomJS or SlimerJS. No longer maintained since 22 Dec 2017.
- [PhantomFlow](https://github.com/Huddle/PhantomFlow) [![GitHub stars](https://img.shields.io/github/stars/Huddle/PhantomFlow?style=flat)](https://github.com/Huddle/PhantomFlow/stargazers) - Experimental approach to UI testing, based on Decision Trees.
- [PhantomJS](https://github.com/ariya/phantomjs) [![GitHub stars](https://img.shields.io/github/stars/ariya/phantomjs?style=flat)](https://github.com/ariya/phantomjs/stargazers) - Scriptable Headless WebKit. No longer maintained since 2 June 2018.
- [trifleJS](https://github.com/sdesalas/trifleJS) [![GitHub stars](https://img.shields.io/github/stars/sdesalas/trifleJS?style=flat)](https://github.com/sdesalas/trifleJS/stargazers) - Headless automation for Internet Explorer. (last update 2016)
- [Visual Review](https://github.com/xebia/VisualReview) [![GitHub stars](https://img.shields.io/github/stars/xebia/VisualReview?style=flat)](https://github.com/xebia/VisualReview/stargazers) - A human-friendly tool for testing and reviewing visual regressions.
- [WebdriverCSS](https://github.com/webdriverio/webdrivercss) [![GitHub stars](https://img.shields.io/github/stars/webdriverio/webdrivercss?style=flat)](https://github.com/webdriverio/webdrivercss/stargazers) - WebdriverCSS sits on top of [Webdriver.io](https://github.com/webdriverio/webdriverio/) [![GitHub stars](https://img.shields.io/github/stars/webdriverio/webdriverio/?style=flat)](https://github.com/webdriverio/webdriverio//stargazers) and hooks into [Selenium](https://github.com/SeleniumHQ/selenium) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium?style=flat)](https://github.com/SeleniumHQ/selenium/stargazers).

## Miscellaneous

### Contributing

See the [Contribution Guide](.github/CONTRIBUTING.md) for details on how to contribute.

### Code of Conduct

See the [Code of Conduct](.github/CODE-OF-CONDUCT.md) for details. Basically it comes down to:
> In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and orientation.

### License

[![CC-BY-SA](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
License holders are [all contributors](https://github.com/mojoaxel/awesome-regression-testing/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/mojoaxel/awesome-regression-testing/graphs/contributors?style=flat)](https://github.com/mojoaxel/awesome-regression-testing/graphs/contributors/stargazers).
