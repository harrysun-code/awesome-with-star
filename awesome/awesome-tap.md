# TAP

> 来源：[sindresorhus/awesome-tap](https://github.com/sindresorhus/awesome-tap)

[![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome-tap?style=flat)](https://github.com/sindresorhus/awesome-tap/stargazers)

# Awesome TAP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [<img src="https://testanything.org/images/tap.png" width="67" align="right">](https://testanything.org)

> Useful resources for the [Test Anything Protocol](https://testanything.org)

TAP is a simple text-based interface between testing modules in a test harness.

*The list is very JavaScript focused right now. That's just because I'm only familiar with TAP stuff in the JS world. Contributions welcome for any language.*

## Contents

- [Reporters](#reporters)
- [Producers](#producers)
- [Consumers](#consumers)
- [Tools](#tools)
- [Articles](#articles)
- [Tutorials](#tutorials)
- [Documentation](#documentation)
- [Community](#community)

## Reporters

### JavaScript

- [tap-dot](https://github.com/scottcorgan/tap-dot) [![GitHub stars](https://img.shields.io/github/stars/scottcorgan/tap-dot?style=flat)](https://github.com/scottcorgan/tap-dot/stargazers) - Dotted output.
- [tap-spec](https://github.com/scottcorgan/tap-spec) [![GitHub stars](https://img.shields.io/github/stars/scottcorgan/tap-spec?style=flat)](https://github.com/scottcorgan/tap-spec/stargazers) - Mocha-like spec reporter.
- [tap-nyan](https://github.com/calvinmetcalf/tap-nyan) [![GitHub stars](https://img.shields.io/github/stars/calvinmetcalf/tap-nyan?style=flat)](https://github.com/calvinmetcalf/tap-nyan/stargazers) - Nyan cat.
- [tap-min](https://github.com/derhuerst/tap-min) [![GitHub stars](https://img.shields.io/github/stars/derhuerst/tap-min?style=flat)](https://github.com/derhuerst/tap-min/stargazers) - Minimal output.
- [tap-difflet](https://github.com/namuol/tap-difflet) [![GitHub stars](https://img.shields.io/github/stars/namuol/tap-difflet?style=flat)](https://github.com/namuol/tap-difflet/stargazers) - Minimal output with diffing.
- [tap-diff](https://github.com/axross/tap-diff) [![GitHub stars](https://img.shields.io/github/stars/axross/tap-diff?style=flat)](https://github.com/axross/tap-diff/stargazers) - Human-friendly output with diffing.
- [tap-simple](https://github.com/joeybaker/tap-simple) [![GitHub stars](https://img.shields.io/github/stars/joeybaker/tap-simple?style=flat)](https://github.com/joeybaker/tap-simple/stargazers) - Simple output.
- [faucet](https://github.com/substack/faucet) [![GitHub stars](https://img.shields.io/github/stars/substack/faucet?style=flat)](https://github.com/substack/faucet/stargazers) - Human-readable summarizer.
- [tap-mocha-reporter](https://github.com/isaacs/tap-mocha-reporter) [![GitHub stars](https://img.shields.io/github/stars/isaacs/tap-mocha-reporter?style=flat)](https://github.com/isaacs/tap-mocha-reporter/stargazers) - Use any of the [Mocha reporters](https://github.com/isaacs/tap-mocha-reporter/tree/master/lib/reporters) [![GitHub stars](https://img.shields.io/github/stars/isaacs/tap-mocha-reporter/tree/master/lib/reporters?style=flat)](https://github.com/isaacs/tap-mocha-reporter/tree/master/lib/reporters/stargazers).
- [tap-summary](https://github.com/zoubin/tap-summary) [![GitHub stars](https://img.shields.io/github/stars/zoubin/tap-summary?style=flat)](https://github.com/zoubin/tap-summary/stargazers) - Summarized output.
- [tap-pessimist](https://github.com/clux/tap-pessimist) [![GitHub stars](https://img.shields.io/github/stars/clux/tap-pessimist?style=flat)](https://github.com/clux/tap-pessimist/stargazers) - Only shows failed tests.
- [tap-prettify](https://github.com/toolness/tap-prettify) [![GitHub stars](https://img.shields.io/github/stars/toolness/tap-prettify?style=flat)](https://github.com/toolness/tap-prettify/stargazers) - Nice readable output with diffing.
- [tap-colorize](https://github.com/substack/tap-colorize) [![GitHub stars](https://img.shields.io/github/stars/substack/tap-colorize?style=flat)](https://github.com/substack/tap-colorize/stargazers) - Colorize the output while preserving machine-readability.
- [tap-bail](https://github.com/juliangruber/tap-bail) [![GitHub stars](https://img.shields.io/github/stars/juliangruber/tap-bail?style=flat)](https://github.com/juliangruber/tap-bail/stargazers) - Bail out when the first test fails.
- [tap-notify](https://github.com/axross/tap-notify) [![GitHub stars](https://img.shields.io/github/stars/axross/tap-notify?style=flat)](https://github.com/axross/tap-notify/stargazers) - Notifier for macOS, Linux and Windows.
- [tap-json](https://github.com/gummesson/tap-json) [![GitHub stars](https://img.shields.io/github/stars/gummesson/tap-json?style=flat)](https://github.com/gummesson/tap-json/stargazers) - JSON output.
- [ava-tap-json](https://github.com/yovasx2/ava-tap-json) [![GitHub stars](https://img.shields.io/github/stars/yovasx2/ava-tap-json?style=flat)](https://github.com/yovasx2/ava-tap-json/stargazers) - JSON output with AVA compatibility.
- [tap-xunit](https://github.com/aghassemi/tap-xunit) [![GitHub stars](https://img.shields.io/github/stars/aghassemi/tap-xunit?style=flat)](https://github.com/aghassemi/tap-xunit/stargazers) - xUnit output.
- [tap-teamcity](https://github.com/smockle/tap-teamcity) [![GitHub stars](https://img.shields.io/github/stars/smockle/tap-teamcity?style=flat)](https://github.com/smockle/tap-teamcity/stargazers) - Output for TeamCity.

### Go

- [tapfmt](https://github.com/coreybutler/tapfmt) [![GitHub stars](https://img.shields.io/github/stars/coreybutler/tapfmt?style=flat)](https://github.com/coreybutler/tapfmt/stargazers) - Standalone cross-platform formatter.

## Producers

Things that produce TAP output.

### JavaScript

- [AVA](https://github.com/sindresorhus/ava) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/ava?style=flat)](https://github.com/sindresorhus/ava/stargazers) - Futuristic test runner (`$ ava --tap`).
- [tap](https://github.com/isaacs/node-tap) [![GitHub stars](https://img.shields.io/github/stars/isaacs/node-tap?style=flat)](https://github.com/isaacs/node-tap/stargazers) - TAP test framework for Node.js.
- [tape](https://github.com/substack/tape) [![GitHub stars](https://img.shields.io/github/stars/substack/tape?style=flat)](https://github.com/substack/tape/stargazers) - TAP-producing test harness for Node.js and browsers.
- [ESLint](https://eslint.org/docs/user-guide/formatters/#tap) - Pluggable JavaScript linter (`$ eslint --format=tap`).
- [Mocha](https://mochajs.org) - Feature-rich test framework for Node.js and browsers (`$ mocha reporter=tap`).
- [qunit-tap](https://github.com/twada/qunit-tap) [![GitHub stars](https://img.shields.io/github/stars/twada/qunit-tap?style=flat)](https://github.com/twada/qunit-tap/stargazers) - TAP output for QUnit.
- [jasmine-reporters](https://github.com/larrymyers/jasmine-reporters) [![GitHub stars](https://img.shields.io/github/stars/larrymyers/jasmine-reporters?style=flat)](https://github.com/larrymyers/jasmine-reporters/stargazers) - TAP output for Jasmine.
- [karma-tap-reporter](https://github.com/fumiakiy/karma-tap-reporter) [![GitHub stars](https://img.shields.io/github/stars/fumiakiy/karma-tap-reporter?style=flat)](https://github.com/fumiakiy/karma-tap-reporter/stargazers) - TAP output for Karma.
- [mos](https://github.com/zkochan/mos) [![GitHub stars](https://img.shields.io/github/stars/zkochan/mos?style=flat)](https://github.com/zkochan/mos/stargazers) - Markdown file generator and tester (`$ mos test --tap`).
- [zora](https://github.com/lorenzofox3/zora) [![GitHub stars](https://img.shields.io/github/stars/lorenzofox3/zora?style=flat)](https://github.com/lorenzofox3/zora/stargazers) - TAP-producing test runner that works with ES2015 without Babel.
- [node:test](https://nodejs.org/api/test.html) - Minimal TAP test runner included with Node.js.

### Swift

- [TAP](https://github.com/swiftdocorg/tap) [![GitHub stars](https://img.shields.io/github/stars/swiftdocorg/tap?style=flat)](https://github.com/swiftdocorg/tap/stargazers) - A Swift package for the Test Anything Protocol (v13).

### Fish

- [Fishtape](https://github.com/fisherman/fishtape) [![GitHub stars](https://img.shields.io/github/stars/fisherman/fishtape?style=flat)](https://github.com/fisherman/fishtape/stargazers) - TAP producer and test harness for fish.

### Bash

- [bats](https://github.com/sstephenson/bats) [![GitHub stars](https://img.shields.io/github/stars/sstephenson/bats?style=flat)](https://github.com/sstephenson/bats/stargazers) - Bash Automated Testing System.
- [ShellSpec](https://github.com/shellspec/shellspec) [![GitHub stars](https://img.shields.io/github/stars/shellspec/shellspec?style=flat)](https://github.com/shellspec/shellspec/stargazers) - A full-featured BDD unit testing framework for POSIX shells.

[More…](https://testanything.org/producers.html)

## Consumers

Things that consume TAP output.

### JavaScript

- [tap-parser](https://github.com/substack/tap-parser) [![GitHub stars](https://img.shields.io/github/stars/substack/tap-parser?style=flat)](https://github.com/substack/tap-parser/stargazers) - TAP parser.
- [tap-out](https://github.com/scottcorgan/tap-out) [![GitHub stars](https://img.shields.io/github/stars/scottcorgan/tap-out?style=flat)](https://github.com/scottcorgan/tap-out/stargazers) - TAP parser.
- [yamlish](https://github.com/isaacs/yamlish) [![GitHub stars](https://img.shields.io/github/stars/isaacs/yamlish?style=flat)](https://github.com/isaacs/yamlish/stargazers) - YAML-block parser.

[More…](https://testanything.org/consumers.html)

## Tools

### JavaScript

- [tap-dev-tool](https://github.com/Jam3/tap-dev-tool) [![GitHub stars](https://img.shields.io/github/stars/Jam3/tap-dev-tool?style=flat)](https://github.com/Jam3/tap-dev-tool/stargazers) - Prettify TAP in the browser console.
- [tap-merge](https://github.com/anko/tap-merge) [![GitHub stars](https://img.shields.io/github/stars/anko/tap-merge?style=flat)](https://github.com/anko/tap-merge/stargazers) - Merge multiple TAP streams.
- [smokestack](https://github.com/hughsk/smokestack) [![GitHub stars](https://img.shields.io/github/stars/hughsk/smokestack?style=flat)](https://github.com/hughsk/smokestack/stargazers) - Run TAP tests in a browser and write the output to `stdout`.
- [chutney](https://github.com/derhuerst/chutney) [![GitHub stars](https://img.shields.io/github/stars/derhuerst/chutney?style=flat)](https://github.com/derhuerst/chutney/stargazers) - Run TAP tests at Sauce Labs. Lightweight [smokestack](https://github.com/hughsk/smokestack) [![GitHub stars](https://img.shields.io/github/stars/hughsk/smokestack?style=flat)](https://github.com/hughsk/smokestack/stargazers) alternative.

### Python

- [tappy](https://github.com/mblayman/tappy) [![GitHub stars](https://img.shields.io/github/stars/mblayman/tappy?style=flat)](https://github.com/mblayman/tappy/stargazers) - Tools for working with TAP.

## Articles

- [Understand the Test Anything Protocol](https://www.effectiveperlprogramming.com/2011/05/understand-the-test-anything-protocol/)

## Tutorials

- [test-anything](https://github.com/finnp/test-anything) [![GitHub stars](https://img.shields.io/github/stars/finnp/test-anything?style=flat)](https://github.com/finnp/test-anything/stargazers) - Learn to test anything with TAP through an interactive workshop.

## Documentation

- [Specification](https://testanything.org/tap-version-13-specification.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Test_Anything_Protocol)

## Community

- [Discuss](https://github.com/TestAnything/Specification/issues)
- [Reddit](https://www.reddit.com/r/testanythingprotocol)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/tap)
