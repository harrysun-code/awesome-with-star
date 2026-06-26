# Regex

[![GitHub stars](https://img.shields.io/github/stars/slevithan/awesome-regex?style=flat)](https://github.com/slevithan/awesome-regex/stargazers)

<!--lint ignore awesome-heading-->
<div align="center">

[![Awesome Regex](media/awesome-regex-banner.svg)](https://github.com/slevithan/awesome-regex)

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) &nbsp;<sup>Shortcut URL: [`regex.cool`](https://regex.cool/)</sup>
</div>

Awesome Regex curates the best regular expression tools, tutorials, libraries, and other resources, covering all major regex flavors.

> Regular expressions (regex or regexp) are a powerful and concise way to search, parse, and process text. They're built into many programming languages, text editors, IDEs, database engines, word processors, and other tools.

Contributions are welcome. Add links through pull requests ([guidelines](CONTRIBUTING.md)).

<details>
  <summary>📖 <b>Glossary</b></summary>
  <br>

*A brief glossary of regular expression terms as used in this list.*

- **Regex engine:** Software that interprets and executes regular expressions, either built into a programming language or as a standalone library.
- **Regex flavor:** A unique set of regex syntax and behavior. Basic syntax is typically shared across flavors, but more advanced features often vary, sometimes in subtle or incompatible ways. A flavor might be shared across multiple implementations or programming languages.
  - Ex: The “JavaScript” flavor is defined by the ECMAScript spec; implemented by multiple engines (V8, etc.).
  - Ex: The “PCRE” flavor is the PCRE2 library, used by numerous programming languages and tools.
  - Ex: Ruby swapped its regex implementation twice from version 1.8 → 1.9 → 2.0, so each used a distinct flavor. The Ruby 2.0+ flavor is referred to here as either “Ruby” or “Onigmo” (the underlying regex library).
- **Non-backtracking engine:** A regex implementation that uses a non-backtracking algorithm and runs in linear time. This rules out worst case performance from superlinear backtracking, but it's slower with some patterns and precludes some useful features like backreferences.
</details>

### Featured resource

<a href="https://github.com/slevithan/regex">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/slevithan/regex@6.1.0/media/logo-dark.svg">
    <img alt="Regex+ logo" height="100" width="225" align="right" src="https://cdn.jsdelivr.net/gh/slevithan/regex@6.1.0/media/logo.svg">
  </picture>
</a>

[Regex+](https://github.com/slevithan/regex) [![GitHub stars](https://img.shields.io/github/stars/slevithan/regex?style=flat)](https://github.com/slevithan/regex/stargazers) is a lightweight JavaScript library for more readable, high-performance, native JavaScript regexes with powerful features including free spacing, atomic groups, possessive quantifiers, subroutines, definition groups, and context-aware interpolation.

## Contents

- [Testers](#testers)
- [Syntax-free regex builders](#syntax-free-regex-builders)
- [Visualizers](#visualizers)
- [Grep-like tools](#grep-like-tools)
- [Tutorials](#tutorials)
- [Regex engines](#regex-engines)
  - [Documentation](#documentation)
  - [Source code](#source-code)
  - [Flavor differences](#flavor-differences)
- [Performance](#performance)
- [Collections of patterns](#collections-of-patterns)
- [JavaScript regex libraries](#javascript-regex-libraries)
- [JavaScript regex evolution](#javascript-regex-evolution)
- [Books](#books)
- [Articles](#articles)
- [Communities](#communities)
- [Miscellaneous](#miscellaneous)

## Testers

*For building, testing, and playing with regexes.*

- [regex101](https://regex101.com/) - **Best free and best web-based tester**.
  - Flavors: Java, JavaScript, .NET, PCRE, RE2, Rust, and emulates Python.
  - Includes regex debugger (PCRE only).
- [RegexBuddy](https://www.regexbuddy.com/) (Windows, $40) - **Best tester**.
  - Flavors: Emulates hundreds of flavors/versions, with deep knowledge of differences.
  - Includes regex debugger.
- [RegExr](https://regexr.com/) \[[*GitHub*](https://github.com/gskinner/regexr/) [![GitHub stars](https://img.shields.io/github/stars/gskinner/regexr/?style=flat)](https://github.com/gskinner/regexr//stargazers)] - **Best open source tester**.
  - Flavors: JavaScript, PCRE.
  - Languages: 🇺🇸, 🇨🇳 ([fork](https://regexr-cn.com/)).
- [RegexLearn](https://regexlearn.com/playground) \[[*GitHub*](https://github.com/aykutkardas/regexlearn.com/blob/develop/src/pages/%5Blang%5D/playground.tsx) [![GitHub stars](https://img.shields.io/github/stars/aykutkardas/regexlearn.com/blob/develop/src/pages/%5Blang%5D/playground.tsx?style=flat)](https://github.com/aykutkardas/regexlearn.com/blob/develop/src/pages/%5Blang%5D/playground.tsx/stargazers)] - **Best multilingual tester** (JavaScript).
  - Languages: 🇺🇸, 🇹🇷, 🇷🇺, 🇪🇸, 🇨🇳, 🇩🇪, 🇺🇦, 🇫🇷, 🇵🇱, 🇰🇷, 🇧🇷, 🇨🇿, 🇬🇪.
- [regexplained](https://regexplained.com/) \[[*GitHub*](https://github.com/LeaVerou/regexplained) [![GitHub stars](https://img.shields.io/github/stars/LeaVerou/regexplained?style=flat)](https://github.com/LeaVerou/regexplained/stargazers)] - **Best tester for presentations** (JavaScript).

<details>
  <summary>✳️ <b>Notable mentions</b></summary>
  <br>

**Command line**

- [pcre2test](https://pcre2project.github.io/pcre2/doc/pcre2test/) - Includes regex debugger. Flavor: PCRE.
- [rxrx](https://metacpan.org/dist/Regexp-Debugger/view/bin/rxrx) - Includes regex debugger ([video intro](https://www.youtube.com/watch?v=zcSFIUiMgAs)). Flavor: Perl.

**By flavor**

- fancy-regex (Rust library): [fancy-regex playground](https://fancy-regex.github.io/fancy-regex/) \[[*GitHub*](https://github.com/fancy-regex/fancy-regex/tree/main/playground) [![GitHub stars](https://img.shields.io/github/stars/fancy-regex/fancy-regex/tree/main/playground?style=flat)](https://github.com/fancy-regex/fancy-regex/tree/main/playground/stargazers)].
- JavaScript: [RegViz](http://regviz.org/).
- .NET: [Regex Storm](http://regexstorm.net/tester) \[[*GitHub*](https://github.com/lonekorean/regex-storm) [![GitHub stars](https://img.shields.io/github/stars/lonekorean/regex-storm?style=flat)](https://github.com/lonekorean/regex-storm/stargazers)].
- PCRE: [PHP Live Regex](https://www.phpliveregex.com/).
- Python: [Pythex](https://pythex.org/).
- Ruby: [Rubular](https://rubular.com/).
- sed: [GNU sed REPL](https://sed.js.org/).
- Swift: [Swift Regex](https://swiftregex.com/) \[[*GitHub*](https://github.com/swiftfiddle/swiftregex) [![GitHub stars](https://img.shields.io/github/stars/swiftfiddle/swiftregex?style=flat)](https://github.com/swiftfiddle/swiftregex/stargazers)] - Includes regex debugger, DSL builder.

**Multiple flavors**

- [CyrilEx](https://extendsclass.com/regex-tester.html) \[[*GitHub*](https://github.com/cyrilbois/cyrilex) [![GitHub stars](https://img.shields.io/github/stars/cyrilbois/cyrilex?style=flat)](https://github.com/cyrilbois/cyrilex/stargazers)] - Java, JavaScript, MySQL, PHP, Python, Ruby.
- [Patterns](https://krillapps.com/patterns/) (macOS, $3) - Bash, Emacs, grep, Java, Oniguruma, PCRE, POSIX BRE, POSIX ERE, Ruby, sed.
- [RegexPlanet](https://www.regexplanet.com/) \[[*GitHub*](https://github.com/regexplanet) [![GitHub stars](https://img.shields.io/github/stars/regexplanet?style=flat)](https://github.com/regexplanet/stargazers)] - Go, Java, JavaScript (Bun, Deno, Node.js), .NET, Perl, PHP, PostgreSQL, Python, Ruby, Rust, Swift, Tcl, XRegExp.
</details>

## Syntax-free regex builders

*Build regexes without writing regex syntax or code.*

- [ChatGPT](https://chat.openai.com/) and other LLMs - Ex: *"create a regex that matches `X` and explain it step by step"*.
- [RegexMagic](https://www.regexmagic.com/) (Windows, $40) - Generate regexes using samples and rules.
  - Flavors: Emulates hundreds of flavors/versions.

<details>
  <summary>✳️ <b>Notable mentions</b></summary>
  <br>

- [Regex Generator](https://regex-generator.olafneumann.org/) \[[*GitHub*](https://github.com/noxone/regex-generator) [![GitHub stars](https://img.shields.io/github/stars/noxone/regex-generator?style=flat)](https://github.com/noxone/regex-generator/stargazers)] - Generate simple regexes from a sample text.
- [Regex.ai](https://regex.ai/) - Mark samples in a text and use AI to generate potential regexes.
</details>

## Visualizers

*Visualize how your regular expressions are structured or operate.*

- [Regex Vis](https://regex-vis.com/) \[[*GitHub*](https://github.com/Bowen7/regex-vis) [![GitHub stars](https://img.shields.io/github/stars/Bowen7/regex-vis?style=flat)](https://github.com/Bowen7/regex-vis/stargazers)] - Create railroad diagrams, with visual editor. Flavor: JavaScript.
  - Languages: 🇺🇸, 🇨🇳.
- [Regulex](https://jex.im/regulex/) \[[*GitHub*](https://github.com/CJex/regulex) [![GitHub stars](https://img.shields.io/github/stars/CJex/regulex?style=flat)](https://github.com/CJex/regulex/stargazers)] - Create railroad diagrams. Flavor: JavaScript.
- [Nodexr](https://www.nodexr.net/) \[[*GitHub*](https://github.com/Jcparkyn/nodexr) [![GitHub stars](https://img.shields.io/github/stars/Jcparkyn/nodexr?style=flat)](https://github.com/Jcparkyn/nodexr/stargazers)] - Graphical editor with visual hierarchy. Flavor: .NET.

<details>
  <summary>✳️ <b>Notable mentions</b></summary>
  <br>

- [Regex Nodes](https://johannesvollmer.com/regex-nodes/) \[[*GitHub*](https://github.com/johannesvollmer/regex-nodes) [![GitHub stars](https://img.shields.io/github/stars/johannesvollmer/regex-nodes?style=flat)](https://github.com/johannesvollmer/regex-nodes/stargazers)] - Graphical editor with visual hierarchy. Flavor: JavaScript.
- [Debuggex](https://www.debuggex.com/) - Create railroad diagrams. Flavors: JavaScript, PCRE, Python.
- [Regexper](https://regexper.com/) \[[*GitLab*](https://gitlab.com/javallone/regexper-static)] - Create railroad diagrams. Flavor: JavaScript.
</details>

## Grep-like tools

*Search and replace through files.*

### Command line

- [ripgrep](https://github.com/BurntSushi/ripgrep) [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/ripgrep?style=flat)](https://github.com/BurntSushi/ripgrep/stargazers) - Better and faster grep. Recursively searches directories while respecting gitignore rules and skipping hidden/binary files.
  - Flavors: Rust (default), PCRE.
- [nomino](https://github.com/yaa110/nomino) [![GitHub stars](https://img.shields.io/github/stars/yaa110/nomino?style=flat)](https://github.com/yaa110/nomino/stargazers) - Rename files uses regexes.
  - Flavor: Rust.

➕ **See also:** [Feature comparison of grep-like tools](https://beyondgrep.com/feature-comparison/).

### GUI

- [Aba Search and Replace](https://www.abareplace.com/) (Windows, $30) - Displays matches as you type.
- [PowerGREP](https://www.powergrep.com/) (Windows, $159) - Can search through archives, binary files, PDFs, docs/sheets, emails, etc., via its GUI or the command line.
  - Flavors: Emulates hundreds of flavors/versions.
- [PowerRename](https://github.com/microsoft/PowerToys) [![GitHub stars](https://img.shields.io/github/stars/microsoft/PowerToys?style=flat)](https://github.com/microsoft/PowerToys/stargazers) (Windows) - Rename files using regexes.

## Tutorials

*Learn how to use regular expressions.*

### Traditional

- [Regular-Expressions.info](https://www.regular-expressions.info/) - Covers numerous regex flavors.
- [The Modern JavaScript Tutorial: Regular expressions](https://javascript.info/regular-expressions) \[[*GitHub*](https://github.com/javascript-tutorial/en.javascript.info) [![GitHub stars](https://img.shields.io/github/stars/javascript-tutorial/en.javascript.info?style=flat)](https://github.com/javascript-tutorial/en.javascript.info/stargazers)] - Guide to using regexes in JavaScript.
  - Languages: 🇺🇸, 🇪🇸, 🇫🇷, 🇮🇹, 🇯🇵, 🇷🇺, 🇺🇦, 🇨🇳 (partial for [others](https://javascript.info/translate)).

<details>
  <summary>✳️ <b>Notable mentions</b></summary>
  <br>

- [RexEgg](https://rexegg.com/) - Detailed tutorial with advanced topics.
- [learnbyexample](https://learnbyexample.github.io/books/) \[[*GitHub*](https://github.com/learnbyexample) [![GitHub stars](https://img.shields.io/github/stars/learnbyexample?style=flat)](https://github.com/learnbyexample/stargazers)] - Ebooks on regexes ([JavaScript](https://learnbyexample.github.io/learn_js_regexp/), [Python](https://learnbyexample.github.io/py_regular_expressions/), [Ruby](https://learnbyexample.github.io/Ruby_Regexp/)) and command line text processing.
- [Regular Expressions for Regular Folk](https://refrf.dev/) \[[*GitHub*](https://github.com/shreyasminocha/regex-for-regular-folk) [![GitHub stars](https://img.shields.io/github/stars/shreyasminocha/regex-for-regular-folk?style=flat)](https://github.com/shreyasminocha/regex-for-regular-folk/stargazers)] - Visual, example-based ebook for beginners.
</details>

### With interactive exercises

- [RegexLearn](https://regexlearn.com/) \[[*GitHub*](https://github.com/aykutkardas/regexlearn.com) [![GitHub stars](https://img.shields.io/github/stars/aykutkardas/regexlearn.com?style=flat)](https://github.com/aykutkardas/regexlearn.com/stargazers)] - Interactive tutorial and practice problems.
  - Languages: 🇺🇸, 🇹🇷, 🇷🇺, 🇪🇸, 🇨🇳, 🇩🇪, 🇺🇦, 🇫🇷, 🇵🇱, 🇰🇷, 🇧🇷, 🇨🇿, 🇬🇪.
- [RegexOne](https://regexone.com/) - Interactive tutorial and practice problems.

### Videos

- [*Demystifying Regular Expressions*](https://www.youtube.com/watch?v=M7vDtxaD7ZU) - Great presentation for beginners, by Lea Verou at HolyJS 2017 (1hr 12m).
- [*Learn Regular Expressions In 20 Minutes*](https://www.youtube.com/watch?v=rhzKDrUiJVk) - Live syntax walkthrough in a regex tester, by Kyle Cook.
- Many options for video courses are available on [Udemy](https://www.udemy.com/topic/regular-expressions/) ($).

## Regex engines

*Major regex implementations, built into programming languages or as standalone libraries.*

### Documentation

*Official regex references and guides.*

#### Regex flavors

- Boost.Regex: [Manual](https://boost.org/libs/regex).
- C++: [Regular expressions library](https://en.cppreference.com/w/cpp/regex).
- Hyperscan: [Introduction](https://www.hyperscan.io/).
- ICU: [Regular Expressions](https://unicode-org.github.io/icu/userguide/strings/regexp.html).
- Java: [Pattern](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/regex/Pattern.html), [API](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/regex/package-summary.html).
- JavaScript: [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp), [Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions), [Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions), [Cheatsheet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet).
- .NET: [Overview](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions), [Language](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference), [API](https://learn.microsoft.com/en-us/dotnet/api/system.text.regularexpressions).
- Onigmo: [RE](https://github.com/k-takata/Onigmo/blob/master/doc/RE) [![GitHub stars](https://img.shields.io/github/stars/k-takata/Onigmo/blob/master/doc/RE?style=flat)](https://github.com/k-takata/Onigmo/blob/master/doc/RE/stargazers).
- Oniguruma: [RE](https://github.com/kkos/oniguruma/blob/master/doc/RE) [![GitHub stars](https://img.shields.io/github/stars/kkos/oniguruma/blob/master/doc/RE?style=flat)](https://github.com/kkos/oniguruma/blob/master/doc/RE/stargazers).
- PCRE2: [Pattern](https://pcre2project.github.io/pcre2/doc/pcre2pattern/), [API](https://pcre2project.github.io/pcre2/doc/).
- Perl: [Syntax](https://perldoc.perl.org/perlre), [Tutorial](https://perldoc.perl.org/perlretut), [Quick Start](https://perldoc.perl.org/perlrequick).
- Python: [re](https://docs.python.org/library/re.html).
- RE2: [Syntax](https://github.com/google/re2/wiki/Syntax) [![GitHub stars](https://img.shields.io/github/stars/google/re2/wiki/Syntax?style=flat)](https://github.com/google/re2/wiki/Syntax/stargazers).
- Rust: [regex](https://docs.rs/regex) - See also: [regex-lite](https://docs.rs/regex-lite).
- Swift: [Regex](https://developer.apple.com/documentation/swift/regex/) - See also: [RegexBuilder](https://developer.apple.com/documentation/regexbuilder), [NSRegularExpression](https://developer.apple.com/documentation/foundation/nsregularexpression).

ℹ️ Raku (formerly Perl 6) reimagines regexes. See: [Grammars](https://docs.raku.org/language/grammars) ([tutorial](https://docs.raku.org/language/grammar_tutorial)), [Regexes](https://docs.raku.org/language/regexes) ([best practices](https://docs.raku.org/language/regexes-best-practices)).

#### Without own flavor

- Go: [regexp](https://pkg.go.dev/regexp) - Flavor: RE2.
- MySQL: [Regular Expressions](https://dev.mysql.com/doc/refman/en/regexp.html) - Flavor: ICU.
- PHP: [Regular Expressions](https://www.php.net/manual/en/book.pcre.php) - Flavor: PCRE.
- Ruby: [Regexp](https://docs.ruby-lang.org/en/master/Regexp.html) - Flavor: Onigmo.

### Source code

*Read or contribute to the code behind major regex implementations.*

- [Boost.Regex](https://github.com/boostorg/regex) [![GitHub stars](https://img.shields.io/github/stars/boostorg/regex?style=flat)](https://github.com/boostorg/regex/stargazers) - C++ regex library.
- [Hyperscan](https://github.com/intel/hyperscan) [![GitHub stars](https://img.shields.io/github/stars/intel/hyperscan?style=flat)](https://github.com/intel/hyperscan/stargazers) - Intel's high-performance library, used for [DPI](https://en.wikipedia.org/wiki/Deep_packet_inspection).
- [ICU](https://github.com/unicode-org/icu/blob/main/icu4c/source/i18n/regexcmp.cpp) [![GitHub stars](https://img.shields.io/github/stars/unicode-org/icu/blob/main/icu4c/source/i18n/regexcmp.cpp?style=flat)](https://github.com/unicode-org/icu/blob/main/icu4c/source/i18n/regexcmp.cpp/stargazers) - Unicode org's package with full Unicode support.
- [Java: java.util.regex](https://github.com/openjdk/jdk/tree/master/src/java.base/share/classes/java/util/regex) [![GitHub stars](https://img.shields.io/github/stars/openjdk/jdk/tree/master/src/java.base/share/classes/java/util/regex?style=flat)](https://github.com/openjdk/jdk/tree/master/src/java.base/share/classes/java/util/regex/stargazers) - JDK standard regexes.
- JavaScript:
  - [JavaScriptCore: RegExp](https://github.com/WebKit/WebKit/blob/main/Source/JavaScriptCore/runtime/RegExp.cpp) [![GitHub stars](https://img.shields.io/github/stars/WebKit/WebKit/blob/main/Source/JavaScriptCore/runtime/RegExp.cpp?style=flat)](https://github.com/WebKit/WebKit/blob/main/Source/JavaScriptCore/runtime/RegExp.cpp/stargazers) - Regex engine used by Safari.
  - [V8: Irregexp](https://github.com/v8/v8/tree/main/src/regexp) [![GitHub stars](https://img.shields.io/github/stars/v8/v8/tree/main/src/regexp?style=flat)](https://github.com/v8/v8/tree/main/src/regexp/stargazers) - Regex engine used by Chrome, Edge, [Firefox](https://hacks.mozilla.org/2020/06/a-new-regexp-engine-in-spidermonkey/), etc.
- [.NET: System.Text.RegularExpressions](https://github.com/dotnet/runtime/tree/main/src/libraries/System.Text.RegularExpressions) [![GitHub stars](https://img.shields.io/github/stars/dotnet/runtime/tree/main/src/libraries/System.Text.RegularExpressions?style=flat)](https://github.com/dotnet/runtime/tree/main/src/libraries/System.Text.RegularExpressions/stargazers) - Shared by all .NET languages (C#, VB, etc.).
- [Onigmo](https://github.com/k-takata/Onigmo) [![GitHub stars](https://img.shields.io/github/stars/k-takata/Onigmo?style=flat)](https://github.com/k-takata/Onigmo/stargazers) - Forked from Oniguruma. Used by Ruby 2.0+.
- [Oniguruma](https://github.com/kkos/oniguruma) [![GitHub stars](https://img.shields.io/github/stars/kkos/oniguruma?style=flat)](https://github.com/kkos/oniguruma/stargazers) - C regex library used by Ruby 1.9, TextMate grammars, etc.
- [PCRE2](https://github.com/PCRE2Project/pcre2) [![GitHub stars](https://img.shields.io/github/stars/PCRE2Project/pcre2?style=flat)](https://github.com/PCRE2Project/pcre2/stargazers) - Popular C regex library used by PHP, R, etc.
- [Perl](https://github.com/Perl/perl5/blob/blead/regexp.h) [![GitHub stars](https://img.shields.io/github/stars/Perl/perl5/blob/blead/regexp.h?style=flat)](https://github.com/Perl/perl5/blob/blead/regexp.h/stargazers) - See [perlreguts](https://perldoc.perl.org/perlreguts).
- [Python: re](https://github.com/python/cpython/tree/main/Lib/re) [![GitHub stars](https://img.shields.io/github/stars/python/cpython/tree/main/Lib/re?style=flat)](https://github.com/python/cpython/tree/main/Lib/re/stargazers) and [regex](https://github.com/mrabarnett/mrab-regex) [![GitHub stars](https://img.shields.io/github/stars/mrabarnett/mrab-regex?style=flat)](https://github.com/mrabarnett/mrab-regex/stargazers) - Standard and extended regex libraries.
- [RE2](https://github.com/google/re2) [![GitHub stars](https://img.shields.io/github/stars/google/re2?style=flat)](https://github.com/google/re2/stargazers) - Popular C++ regex library used by Go, etc. Non-backtracking engine.
- [Rust: regex](https://github.com/rust-lang/regex) [![GitHub stars](https://img.shields.io/github/stars/rust-lang/regex?style=flat)](https://github.com/rust-lang/regex/stargazers) - Non-backtracking engine.

### Flavor differences

*Syntax and behavior differences between regex flavors.*

- Ron Buckton: [Regular Expression Feature Comparisons](https://rbuckton.github.io/regexp-features/) \[[*GitHub*](https://github.com/rbuckton/regexp-features) [![GitHub stars](https://img.shields.io/github/stars/rbuckton/regexp-features?style=flat)](https://github.com/rbuckton/regexp-features/stargazers)].
- Regular-Expressions.info: [Tools & Languages](https://www.regular-expressions.info/tools.html).
- Steven Levithan: [Named capture](https://xregexp.com/syntax/named_capture_comparison/), [Lookbehind](https://stevenlevithan.com/regex/tests/lookbehind.html).
- Wikipedia: [Comparison of regular expression engines](https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines).

## Performance

*Pattern and engine performance, benchmarks, and [ReDoS](https://en.wikipedia.org/wiki/ReDoS) prevention.*

### Crafting efficient regexes

- [Runaway Regular Expressions: Catastrophic Backtracking](https://www.regular-expressions.info/catastrophic.html) - Exploration and solutions for superlinear backtracking.
- [Book: High Performance JavaScript](https://www.amazon.com/dp/059680279X/?tag=slev-20) (2010) - *Chapter 5: Strings and Regular Expressions*.
- [Book: Mastering Regular Expressions, 3rd Edition](https://www.amazon.com/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124/?tag=slev-20) (2006) - *Chapter 6: Crafting an Efficient Expression*.
- [Performance of Greedy vs. Lazy Regex Quantifiers](https://blog.stevenlevithan.com/archives/greedy-lazy-performance) - Illustrates the mechanics of backtracking.

ℹ️ With backtracking engines, how you craft a regex can affect how fast it finds matches or reports failures.

<details>
  <summary>✳️ <b>Notable mentions</b></summary>
  <br>

- [Performance of Regular Expressions](https://medium.com/textmaster-engineering/performance-of-regular-expressions-81371f569698) - On backtracking performance, with detailed examples.
</details>

### Regex engine optimization

- [Regular Expression Matching Can Be Simple And Fast](https://swtch.com/~rsc/regexp/regexp1.html) - On non-backtracking engines. A [follow up](https://swtch.com/~rsc/regexp/regexp3.html) includes comparisons of RE2 and PCRE performance.
- [Regular Expression Improvements in .NET 7](https://devblogs.microsoft.com/dotnet/regular-expression-improvements-in-dotnet-7/) and [.NET 5](https://devblogs.microsoft.com/dotnet/regex-performance-improvements-in-net-5/) - Includes detailed explanations of performance optimizations.
- [ripgrep is faster than {grep, …}](https://blog.burntsushi.net/ripgrep/) - Includes details about what makes ripgrep and Rust's `regex` fast.

### Benchmarking

- Cross-engine benchmarking libraries: [rebar](https://github.com/BurntSushi/rebar) [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/rebar?style=flat)](https://github.com/BurntSushi/rebar/stargazers), [regex-benchmark](https://github.com/mariomka/regex-benchmark) [![GitHub stars](https://img.shields.io/github/stars/mariomka/regex-benchmark?style=flat)](https://github.com/mariomka/regex-benchmark/stargazers).
- [Boost.Regex: Performance](https://www.boost.org/doc/libs/release/libs/regex/doc/html/boost_regex/background/performance.html) - Compares Boost, C++ `std::regex`, and others.

### ReDoS checkers

- [regex.rip](https://regex.rip/) - Test a regex for ReDoS vulnerability.
- [recheck](https://github.com/makenowjust-labs/recheck) [![GitHub stars](https://img.shields.io/github/stars/makenowjust-labs/recheck?style=flat)](https://github.com/makenowjust-labs/recheck/stargazers) \[[*home*](https://makenowjust-labs.github.io/recheck/)] - JavaScript and Scala library for detecting ReDoS vulnerability. Can be used as an ESLint plugin.
- [vuln-regex-detector](https://github.com/davisjam/vuln-regex-detector) [![GitHub stars](https://img.shields.io/github/stars/davisjam/vuln-regex-detector?style=flat)](https://github.com/davisjam/vuln-regex-detector/stargazers) - Perl library for detecting ReDoS vulnerability.

⚠️ These tools have limitations on supported syntax.

## Collections of patterns

*Prewritten regexes for specific tasks.*

- [Book: Regular Expressions Cookbook, 2nd Edition](https://www.amazon.com/Regular-Expressions-Cookbook-Solutions-Programming/dp/1449319432/?tag=slev-20) (2012) - High-quality solutions with detailed explanations.
  - Flavors: Java, JavaScript, .NET, PCRE, Perl, Python, Ruby, XRegExp.
- [Regex DB](https://rgxdb.com/) - Solutions include basic descriptions and examples of matching and non-matching text.

<details>
  <summary>⚠️ <b>Word of warning</b></summary>
  <br>

Many regexes found online are low quality. It's risky to use regexes you don't fully understand in code, since they might have false positives/negatives, be vulnerable to performance problems with certain target strings, or assume a different regex flavor.
</details>

## JavaScript regex libraries

*Open source JavaScript libraries for advanced regex use and processing.*

### Alternative regex builders and engines

- [Regex+](https://github.com/slevithan/regex) [![GitHub stars](https://img.shields.io/github/stars/slevithan/regex?style=flat)](https://github.com/slevithan/regex/stargazers) - A template tag for extended, readable, high-performance JavaScript regexes.
- [Oniguruma-To-ES](https://github.com/slevithan/oniguruma-to-es) [![GitHub stars](https://img.shields.io/github/stars/slevithan/oniguruma-to-es?style=flat)](https://github.com/slevithan/oniguruma-to-es/stargazers) - Convert Oniguruma patterns to native JavaScript regexes.
- Use other engines via WebAssembly: [node-re2](https://github.com/uhop/node-re2) [![GitHub stars](https://img.shields.io/github/stars/uhop/node-re2?style=flat)](https://github.com/uhop/node-re2/stargazers) (RE2), [rregex](https://github.com/2fd/rregex) [![GitHub stars](https://img.shields.io/github/stars/2fd/rregex?style=flat)](https://github.com/2fd/rregex/stargazers) (Rust's `regex`), [vscode-oniguruma](https://github.com/microsoft/vscode-oniguruma) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vscode-oniguruma?style=flat)](https://github.com/microsoft/vscode-oniguruma/stargazers) (Oniguruma).

### Abstracted regex syntax

- [Rexx](https://github.com/yyytcool/rexx) [![GitHub stars](https://img.shields.io/github/stars/yyytcool/rexx?style=flat)](https://github.com/yyytcool/rexx/stargazers) - A template tag that uses structured syntax with variables and comments.
- [Melody](https://github.com/yoav-lavi/melody) [![GitHub stars](https://img.shields.io/github/stars/yoav-lavi/melody?style=flat)](https://github.com/yoav-lavi/melody/stargazers) \[[*docs*](https://yoav-lavi.github.io/melody/book/)] - A language that compiles to regexes.
- Compose with functions: [compose-regexp.js](https://github.com/compose-regexp/compose-regexp.js) [![GitHub stars](https://img.shields.io/github/stars/compose-regexp/compose-regexp.js?style=flat)](https://github.com/compose-regexp/compose-regexp.js/stargazers), [VerbalExpressions](https://github.com/VerbalExpressions/JSVerbalExpressions) [![GitHub stars](https://img.shields.io/github/stars/VerbalExpressions/JSVerbalExpressions?style=flat)](https://github.com/VerbalExpressions/JSVerbalExpressions/stargazers) (implementations for [many languages](https://verbalexpressions.github.io/)), [magic-regexp](https://github.com/unjs/magic-regexp) [![GitHub stars](https://img.shields.io/github/stars/unjs/magic-regexp?style=flat)](https://github.com/unjs/magic-regexp/stargazers) \[[*home*](https://regexp.dev/)], [Super Expressive](https://github.com/francisrstokes/super-expressive) [![GitHub stars](https://img.shields.io/github/stars/francisrstokes/super-expressive?style=flat)](https://github.com/francisrstokes/super-expressive/stargazers) \[[*playground*](https://nartc.github.io/ng-super-expressive/)].

### Regex processors, utilities, and more

- AST builders: [regexpp](https://github.com/eslint-community/regexpp) [![GitHub stars](https://img.shields.io/github/stars/eslint-community/regexpp?style=flat)](https://github.com/eslint-community/regexpp/stargazers), [regexp-tree](https://github.com/DmitrySoshnikov/regexp-tree) [![GitHub stars](https://img.shields.io/github/stars/DmitrySoshnikov/regexp-tree?style=flat)](https://github.com/DmitrySoshnikov/regexp-tree/stargazers), [regjsparser](https://github.com/jviereck/regjsparser) [![GitHub stars](https://img.shields.io/github/stars/jviereck/regjsparser?style=flat)](https://github.com/jviereck/regjsparser/stargazers)/[regjsgen](https://github.com/bnjmnt4n/regjsgen) [![GitHub stars](https://img.shields.io/github/stars/bnjmnt4n/regjsgen?style=flat)](https://github.com/bnjmnt4n/regjsgen/stargazers), [regexp-simple-parser](https://github.com/fabiospampinato/regexp-simple-parser) [![GitHub stars](https://img.shields.io/github/stars/fabiospampinato/regexp-simple-parser?style=flat)](https://github.com/fabiospampinato/regexp-simple-parser/stargazers).
  - AST explorers: [AST Explorer: RegExp](https://astexplorer.net/#/gist/56d33dc28d07c7f57bdf5ca0f4061320/c6b67a829334151af01ba55960c653e4462df437), [JS RegExp AST Viewer](https://leaysgur.github.io/js-regexp-ast-viewer/).
  - [regexp-ast-analysis](https://github.com/RunDevelopment/regexp-ast-analysis) [![GitHub stars](https://img.shields.io/github/stars/RunDevelopment/regexp-ast-analysis?style=flat)](https://github.com/RunDevelopment/regexp-ast-analysis/stargazers) \[[*docs*](https://rundevelopment.github.io/regexp-ast-analysis/docs/latest/)] - Analyze AST nodes produced by regexpp.
- [eslint-plugin-regexp](https://github.com/ota-meshi/eslint-plugin-regexp) [![GitHub stars](https://img.shields.io/github/stars/ota-meshi/eslint-plugin-regexp?style=flat)](https://github.com/ota-meshi/eslint-plugin-regexp/stargazers) \[[*home*](https://ota-meshi.github.io/eslint-plugin-regexp/)] - ESLint plugin for finding regex mistakes, etc.
- [arkregex](https://github.com/arktypeio/arktype/tree/main/ark/regex) [![GitHub stars](https://img.shields.io/github/stars/arktypeio/arktype/tree/main/ark/regex?style=flat)](https://github.com/arktypeio/arktype/tree/main/ark/regex/stargazers) - `RegExp`-equivalent constructor with TS types.
- [super-regex](https://github.com/sindresorhus/super-regex) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/super-regex?style=flat)](https://github.com/sindresorhus/super-regex/stargazers) - Add an execution timeout to regexes.
- Partial regex matching: [regex-partial-match](https://github.com/TomStrepsil/regex-partial-match) [![GitHub stars](https://img.shields.io/github/stars/TomStrepsil/regex-partial-match?style=flat)](https://github.com/TomStrepsil/regex-partial-match/stargazers), [incr-regex-package](https://github.com/nurulc/incr-regex-package) [![GitHub stars](https://img.shields.io/github/stars/nurulc/incr-regex-package?style=flat)](https://github.com/nurulc/incr-regex-package/stargazers).
- [regex-utils](https://github.com/gruhn/regex-utils) [![GitHub stars](https://img.shields.io/github/stars/gruhn/regex-utils?style=flat)](https://github.com/gruhn/regex-utils/stargazers) - Check regex equivalence, build regex intersections, and other utilities.
- Generate strings that match a given regex: [randexp.js](https://github.com/fent/randexp.js) [![GitHub stars](https://img.shields.io/github/stars/fent/randexp.js?style=flat)](https://github.com/fent/randexp.js/stargazers), [regex-to-strings](https://github.com/wimpyprogrammer/regex-to-strings) [![GitHub stars](https://img.shields.io/github/stars/wimpyprogrammer/regex-to-strings?style=flat)](https://github.com/wimpyprogrammer/regex-to-strings/stargazers).
- [regexgen](https://github.com/devongovett/regexgen) [![GitHub stars](https://img.shields.io/github/stars/devongovett/regexgen?style=flat)](https://github.com/devongovett/regexgen/stargazers) - Generate a regex that matches a set of strings.
- [Regex Colorizer](https://github.com/slevithan/regex-colorizer) [![GitHub stars](https://img.shields.io/github/stars/slevithan/regex-colorizer?style=flat)](https://github.com/slevithan/regex-colorizer/stargazers) \[[*home*](https://slevithan.github.io/regex-colorizer/demo/)] - Highlight regex syntax.
- [regex-to-mermaid](https://github.com/tayles/regex-to-mermaid) [![GitHub stars](https://img.shields.io/github/stars/tayles/regex-to-mermaid?style=flat)](https://github.com/tayles/regex-to-mermaid/stargazers) - Generate Mermaid diagrams to visualize regexes.

## JavaScript regex evolution

*The history of improvements to regular expressions in the JavaScript [standard](https://tc39.es/ecma262/multipage/). Starting with ES2018, includes links to the TC39 proposals where features were developed and discussed.*

- ES3 (1999) introduced regular expressions.
- ES5 (2009) fixed unintuitive behavior by creating a new object every time regex literals are evaluated \[[*explainer*](https://whereswalden.com/2010/01/15/more-es5-incompatible-changes-regular-expressions-now-evaluate-to-a-new-object-not-the-same-object-each-time-theyre-encountered/)], and allowed regex literals to use unescaped forward slashes within character classes (`/[/]/`).
- ES6/ES2015 added: \[[*explainer*](https://2ality.com/2015/07/regexp-es6.html)]
  - Flag `y` (`sticky`), which anchors matches to `lastIndex`.
  - Flag `u` (`unicode`) \[[*explainer*](https://mathiasbynens.be/notes/es6-unicode-regex)] \[[*2016 spec fix*](https://github.com/tc39/ecma262/pull/525) [![GitHub stars](https://img.shields.io/github/stars/tc39/ecma262/pull/525?style=flat)](https://github.com/tc39/ecma262/pull/525/stargazers)], which adds Unicode code point escapes via `\u{…}`, strict errors (for unreserved escapes, octal escapes, quantified lookahead, and unescaped special characters in some contexts), Unicode case-folding for flag `i`, and code point matching (with impact on quantifiers, character classes, ranges, and built-in sets).
  - Getter `RegExp.prototype.flags`, the ability to copy a regex using `RegExp` (optionally with new flags), and support for subclassing `RegExp` (along with `RegExp.prototype[Symbol.match`/`replace`/`search`/`split]` and `RegExp[Symbol.species]`).
- ES2018 added [flag `s`](https://github.com/tc39/proposal-regexp-dotall-flag) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-dotall-flag?style=flat)](https://github.com/tc39/proposal-regexp-dotall-flag/stargazers) (`dotAll`), [lookbehind](https://github.com/tc39/proposal-regexp-lookbehind) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-lookbehind?style=flat)](https://github.com/tc39/proposal-regexp-lookbehind/stargazers), [named capture](https://github.com/tc39/proposal-regexp-named-groups) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-named-groups?style=flat)](https://github.com/tc39/proposal-regexp-named-groups/stargazers), and [Unicode properties](https://github.com/tc39/proposal-regexp-unicode-property-escapes) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-unicode-property-escapes?style=flat)](https://github.com/tc39/proposal-regexp-unicode-property-escapes/stargazers) (via `\p{…}` and `\P{…}` which require flag `u`; see [list](https://github.com/mathiasbynens/regexpu-core/blob/main/property-escapes.md) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/regexpu-core/blob/main/property-escapes.md?style=flat)](https://github.com/mathiasbynens/regexpu-core/blob/main/property-escapes.md/stargazers)).
- ES2020 added string method [`matchAll`](https://github.com/tc39/proposal-string-matchall) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-string-matchall?style=flat)](https://github.com/tc39/proposal-string-matchall/stargazers) (which returns an iterator), plus `RegExp.prototype[Symbol.matchAll]`.
- ES2022 added [flag `d`](https://github.com/tc39/proposal-regexp-match-indices) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-match-indices?style=flat)](https://github.com/tc39/proposal-regexp-match-indices/stargazers) (`hasIndices`), which provides start/end indices for matched substrings.
- ES2024 added [flag `v`](https://github.com/tc39/proposal-regexp-v-flag) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-v-flag?style=flat)](https://github.com/tc39/proposal-regexp-v-flag/stargazers) (`unicodeSets`) \[[*explainer*](https://v8.dev/features/regexp-v-flag)] as an upgrade to flag `u`, which adds a set of multicharacter "properties of strings" to `\p{…}`, multicharacter elements within character classes via `\p{…}` and `\q{…|…}`, nested character classes, set operators `[…--…]` and `[…&&…]`, and different escaping rules within character classes. It also fixes case-insensitive matching for `\p` and `\P` within negated `[^…]`.
- ES2025 added [modifiers](https://github.com/tc39/proposal-regexp-modifiers) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-modifiers?style=flat)](https://github.com/tc39/proposal-regexp-modifiers/stargazers) like `(?ims:…)`, [duplicate named capturing groups](https://github.com/tc39/proposal-duplicate-named-capturing-groups) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-duplicate-named-capturing-groups?style=flat)](https://github.com/tc39/proposal-duplicate-named-capturing-groups/stargazers) in separate alternation paths, and [`RegExp.escape`](https://github.com/tc39/proposal-regex-escaping) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regex-escaping?style=flat)](https://github.com/tc39/proposal-regex-escaping/stargazers).

> Editions from ES2019 onward have added additional Unicode properties that can be used via `\p{…}` and `\P{…}`. ES2021 added string method [`replaceAll`](https://github.com/tc39/proposal-string-replaceall) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-string-replaceall?style=flat)](https://github.com/tc39/proposal-string-replaceall/stargazers), although the only difference from ES3's `replace` when given a regex is that it throws if not using flag `g`.
<details>
  <summary>➕ <b>See also</b></summary>
  <br>

- [*Regexes Got Good: The History And Future Of Regular Expressions In JavaScript*](https://www.smashingmagazine.com/2024/08/history-future-regular-expressions-javascript/)
- Backcompat libraries: [regexpu](https://github.com/mathiasbynens/regexpu) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/regexpu?style=flat)](https://github.com/mathiasbynens/regexpu/stargazers), [regenerate](https://github.com/mathiasbynens/regenerate) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/regenerate?style=flat)](https://github.com/mathiasbynens/regenerate/stargazers) ([Unicode property sets](https://github.com/mathiasbynens/regenerate-unicode-properties) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/regenerate-unicode-properties?style=flat)](https://github.com/mathiasbynens/regenerate-unicode-properties/stargazers)).
- Chrome's `l` (`linear`) regex flag, behind a V8 flag \[[*explainer*](https://v8.dev/blog/non-backtracking-regexp)] \[[*how to run*](https://www.chromium.org/developers/how-tos/run-chromium-with-flags/)].
- [Can I use](https://caniuse.com/) - Up-to-date browser support tables for individual features.
</details>

<details>
  <summary>🔮 <b>Future: Active proposals</b></summary>
  <br>

- [Extended mode and comments](https://github.com/tc39/proposal-regexp-x-mode) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-x-mode?style=flat)](https://github.com/tc39/proposal-regexp-x-mode/stargazers) (2021) - Flag `x` (`extended`) with insignificant whitespace and line comments (`#…`), plus inline comments via `(?#…)`.
- [Atomic operators](https://github.com/tc39/proposal-regexp-atomic-operators) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-atomic-operators?style=flat)](https://github.com/tc39/proposal-regexp-atomic-operators/stargazers) (2021) - Atomic groups via `(?>…)` and possessive quantifiers (ex: `*+`, `++`).
- [Buffer boundaries](https://github.com/tc39/proposal-regexp-buffer-boundaries) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-buffer-boundaries?style=flat)](https://github.com/tc39/proposal-regexp-buffer-boundaries/stargazers) (2021) - Anchors `\A` and `\z`, not affected by flag `m`.
- [\R escape](https://github.com/tc39/proposal-regexp-r-escape) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-r-escape?style=flat)](https://github.com/tc39/proposal-regexp-r-escape/stargazers) (2021) - Outside character classes, `\R` matches any line terminator.
- [Restrict subclassing support in built-ins](https://github.com/tc39/proposal-rm-builtin-subclassing) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-rm-builtin-subclassing?style=flat)](https://github.com/tc39/proposal-rm-builtin-subclassing/stargazers) (2020) - Scaled back `RegExp` subclassing.
- [Legacy RegExp features](https://github.com/tc39/proposal-regexp-legacy-features) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposal-regexp-legacy-features?style=flat)](https://github.com/tc39/proposal-regexp-legacy-features/stargazers) (2015) - Standardization of legacy features.
</details>

## Books

*A curated list of regex books.*

- [*Regular Expressions Cookbook, 2nd Edition*](https://www.amazon.com/dp/1449319432/?tag=slev-20) (2012) by Jan Goyvaerts and Steven Levithan - Regex tutorial with code samples for eight programming languages, 100+ regex recipes for practical problems, and a deep focus on cross-flavor differences.
  - Flavors: Java, JavaScript, .NET, PCRE, Perl, Python, Ruby, XRegExp.
- [*Mastering Regular Expressions, 3rd Edition*](https://www.amazon.com/dp/0596528124/?tag=slev-20) (2006) by Jeffrey Friedl - A computer science classic, best for people who already know the basics. Includes good coverage of crafting efficient regexes.
  - Flavors: Dedicated chapters on Java, .NET, Perl, and PHP (PCRE), with more limited coverage of Python, Tcl, command line tools, etc.
- [*Introducing Regular Expressions*](https://www.amazon.com/dp/1449392687/?tag=slev-20) (2012) by Michael Fitzgerald - An intro for programmers new to regular expressions that sticks to the basics.

## Articles

*A curated list of regex articles.*

- [*The World's Shortest Regex Compiler?*](https://jasonhpriestley.com/regex) and a [follow up](https://jasonhpriestley.com/regex-dfa) on optimization - Introduction to writing a non-backtracking regex engine (in JavaScript).
- [*Regex Legends: The People Behind the Magic*](https://blog.stevenlevithan.com/archives/regex-legends) - Influential people behind the technology.

## Communities

*Discuss, assist, and get help with regular expressions.*

- [Reddit: r/regex](https://www.reddit.com/r/regex/)
- [Stack Overflow: &lsqb;regex&rsqb;](https://stackoverflow.com/questions/tagged/regex?tab=Votes)

## Miscellaneous

*Other interesting, fun, and useful stuff.*

- Quiz: [regex101 Regex Quiz](https://regex101.com/quiz) - Requires sign-in.
- Games: [Regex Crossword](https://regexcrossword.com/), [regexle](https://regexle.com/), [The Typing of the RegEX](https://thetypingoftheregex.com/), [Regex Machina](https://codepip.com/games/regex-machina/) ($).
- Comics: [xkcd](https://xkcd.com/208/), [Garabato Kid](https://twitter.com/garabatokid/status/1147063121678389253).

## About

Awesome Regex was created by [Steven Levithan](https://github.com/slevithan) [![GitHub stars](https://img.shields.io/github/stars/slevithan?style=flat)](https://github.com/slevithan/stargazers) and [contributors](https://github.com/slevithan/awesome-regex/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/slevithan/awesome-regex/graphs/contributors?style=flat)](https://github.com/slevithan/awesome-regex/graphs/contributors/stargazers).

### Sponsors and backers

[<img src="https://github.com/roboflow.png" width="40" height="40">](https://github.com/roboflow) [![GitHub stars](https://img.shields.io/github/stars/roboflow?style=flat)](https://github.com/roboflow/stargazers)

### Past sponsors

[<img src="https://github.com/antfu.png" width="40" height="40">](https://github.com/antfu) [![GitHub stars](https://img.shields.io/github/stars/antfu?style=flat)](https://github.com/antfu/stargazers)
[<img src="https://github.com/brc-dd.png" width="40" height="40">](https://github.com/brc-dd) [![GitHub stars](https://img.shields.io/github/stars/brc-dd?style=flat)](https://github.com/brc-dd/stargazers)

If you want to support this project, I'd love your help by contributing improvements, sharing it with others, or [sponsoring](https://github.com/sponsors/slevithan) [![GitHub stars](https://img.shields.io/github/stars/sponsors/slevithan?style=flat)](https://github.com/sponsors/slevithan/stargazers) ongoing development.

© 2024–present. CC BY 4.0.
