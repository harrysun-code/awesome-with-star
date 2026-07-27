# Pest

> 来源：[pest-parser/awesome-pest](https://github.com/pest-parser/awesome-pest)

[![GitHub stars](https://img.shields.io/github/stars/pest-parser/awesome-pest?style=flat)](https://github.com/pest-parser/awesome-pest/stargazers)

# Awesome Pest. The Elegant Parser [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://avatars.githubusercontent.com/u/26044607" align="right" width="100">](https://github.com/pest-parser/pest/) [![GitHub stars](https://img.shields.io/github/stars/pest-parser/pest/?style=flat)](https://github.com/pest-parser/pest//stargazers)

> A curated list of resources, projects, and tools using or for the pest parser generator in Rust

pest is a general purpose parser written in Rust with a focus on accessibility, correctness, and performance. It uses parsing expression grammars (or [PEG](https://en.wikipedia.org/wiki/Parsing_expression_grammar)) as input, which are similar in spirit to regular expressions, but which offer the enhanced expressivity needed to parse complex languages.

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

## Contents

- [Resources](#resources)
- [Projects](#projects)
- [Tooling](#tooling)

## Resources

- [Book](https://pest.rs/book) - The recommended way to start parsing with pest is to read this official book.
- [API reference on docs.rs](https://docs.rs/pest)
- [fiddle editor on pest.rs](https://pest.rs/#editor) - Play with grammars and share them on the official website (and format them!).
- [Gitter](https://gitter.im/pest-parser/pest)
- [Discord](https://discord.gg/XEGACtWpT2)
- [GitHub Discussions](https://github.com/pest-parser/pest/discussions)

## Projects

Here are some example projects using pest:

- [pest_meta](https://github.com/pest-parser/pest/blob/master/meta/src/grammar.pest) [![GitHub stars](https://img.shields.io/github/stars/pest-parser/pest/blob/master/meta/src/grammar.pest?style=flat)](https://github.com/pest-parser/pest/blob/master/meta/src/grammar.pest/stargazers) - The pest itself is bootstrapped using pest.
- [AshPaper](https://github.com/shnewto/ashpaper) [![GitHub stars](https://img.shields.io/github/stars/shnewto/ashpaper?style=flat)](https://github.com/shnewto/ashpaper/stargazers) - Rust Inpterpreter for Esopo language AshPaper conceived by William Hicks.
- [cicada](https://github.com/mitnk/cicada) [![GitHub stars](https://img.shields.io/github/stars/mitnk/cicada?style=flat)](https://github.com/mitnk/cicada/stargazers) - An old-school bash-like Unix shell written in Rust.
- [elastic-rs](https://github.com/cch123/elastic-rs) [![GitHub stars](https://img.shields.io/github/stars/cch123/elastic-rs?style=flat)](https://github.com/cch123/elastic-rs/stargazers) - Convert bool expressions to Elasticsearch DSL in Rust.
- [handlebars-rust](https://github.com/sunng87/handlebars-rust) [![GitHub stars](https://img.shields.io/github/stars/sunng87/handlebars-rust?style=flat)](https://github.com/sunng87/handlebars-rust/stargazers) - Rust templating with Handlebars.
- [hexdino](https://github.com/Luz/hexdino) [![GitHub stars](https://img.shields.io/github/stars/Luz/hexdino?style=flat)](https://github.com/Luz/hexdino/stargazers) - A hex editor with vim like keybindings written in Rust.
- [insta](https://github.com/mitsuhiko/insta) [![GitHub stars](https://img.shields.io/github/stars/mitsuhiko/insta?style=flat)](https://github.com/mitsuhiko/insta/stargazers) - A snapshot testing library for rust.
- [jql](https://github.com/yamafaktory/jql) [![GitHub stars](https://img.shields.io/github/stars/yamafaktory/jql?style=flat)](https://github.com/yamafaktory/jql/stargazers) - A JSON Query Language CLI tool.
- [json5-rs](https://github.com/callum-oakley/json5-rs) [![GitHub stars](https://img.shields.io/github/stars/callum-oakley/json5-rs?style=flat)](https://github.com/callum-oakley/json5-rs/stargazers) - A Rust JSON5 serializer and deserializer which speaks Serde.
- [mt940](https://github.com/svenstaro/mt940-rs) [![GitHub stars](https://img.shields.io/github/stars/svenstaro/mt940-rs?style=flat)](https://github.com/svenstaro/mt940-rs/stargazers) - A MT940 parser in Rust.
- [py_literal](https://github.com/jturner314/py_literal) [![GitHub stars](https://img.shields.io/github/stars/jturner314/py_literal?style=flat)](https://github.com/jturner314/py_literal/stargazers) - Rust crate for parsing/formatting Python literals.
- [rouler](https://github.com/jarcane/rouler) [![GitHub stars](https://img.shields.io/github/stars/jarcane/rouler?style=flat)](https://github.com/jarcane/rouler/stargazers) - An easy to use dice rolling library for Rust.
- [RuSh](https://github.com/lwandrebeck/RuSh) [![GitHub stars](https://img.shields.io/github/stars/lwandrebeck/RuSh?style=flat)](https://github.com/lwandrebeck/RuSh/stargazers) - RuSh aims to be a bash compatible shell with candies, written in Rust.
- [rs_pbrt](https://github.com/wahn/rs_pbrt) [![GitHub stars](https://img.shields.io/github/stars/wahn/rs_pbrt?style=flat)](https://github.com/wahn/rs_pbrt/stargazers) - Rust crate to implement a counterpart to the PBRT book's (3rd edition) C++ code.
- [stache](https://github.com/dgraham/stache) [![GitHub stars](https://img.shields.io/github/stars/dgraham/stache?style=flat)](https://github.com/dgraham/stache/stargazers) - A Mustache template compiler.
- [tera](https://github.com/Keats/tera) [![GitHub stars](https://img.shields.io/github/stars/Keats/tera?style=flat)](https://github.com/Keats/tera/stargazers) - A template engine for Rust based on Jinja2/Django.
- [ZoKrates](https://github.com/ZoKrates/ZoKrates) [![GitHub stars](https://img.shields.io/github/stars/ZoKrates/ZoKrates?style=flat)](https://github.com/ZoKrates/ZoKrates/stargazers) - A toolbox for zkSNARKs on Ethereum.
- [Vector](https://github.com/timberio/vector) [![GitHub stars](https://img.shields.io/github/stars/timberio/vector?style=flat)](https://github.com/timberio/vector/stargazers) - A high-performance observability data pipeline.
- [AutoCorrect](https://github.com/huacnlee/autocorrect) [![GitHub stars](https://img.shields.io/github/stars/huacnlee/autocorrect?style=flat)](https://github.com/huacnlee/autocorrect/stargazers) - A linter and formatter to help you to improve copywriting, correct spaces, words, and punctuations between CJK (Chinese, Japanese, Korean).
- [yaml-peg](https://github.com/aofdev/yaml-peg) [![GitHub stars](https://img.shields.io/github/stars/aofdev/yaml-peg?style=flat)](https://github.com/aofdev/yaml-peg/stargazers) - PEG parser for YAML written in Rust.
- [qubit](https://github.com/abhimanyu003/qubit) [![GitHub stars](https://img.shields.io/github/stars/abhimanyu003/qubit?style=flat)](https://github.com/abhimanyu003/qubit/stargazers) - A handy calculator, based on Rust and WebAssembly.
- [caith](https://github.com/Geobert/caith) [![GitHub stars](https://img.shields.io/github/stars/Geobert/caith?style=flat)](https://github.com/Geobert/caith/stargazers) - A dice roller crate.
- [Melody](https://github.com/yoav-lavi/melody) [![GitHub stars](https://img.shields.io/github/stars/yoav-lavi/melody?style=flat)](https://github.com/yoav-lavi/melody/stargazers) - Melody is a language that compiles to regular expressions and aims to be more easily readable and maintainable.
- [PTA-Parser](https://github.com/AltaModaTech/pta-parser/) [![GitHub stars](https://img.shields.io/github/stars/AltaModaTech/pta-parser/?style=flat)](https://github.com/AltaModaTech/pta-parser//stargazers) - A Plain Text Accounting parser built in Rust for [Beancount](https://github.com/beancount/beancount) [![GitHub stars](https://img.shields.io/github/stars/beancount/beancount?style=flat)](https://github.com/beancount/beancount/stargazers), [Ledger](https://github.com/ledger/ledger) [![GitHub stars](https://img.shields.io/github/stars/ledger/ledger?style=flat)](https://github.com/ledger/ledger/stargazers), and other PTA formats.
- [Keadex Mina](https://github.com/keadex/keadex) [![GitHub stars](https://img.shields.io/github/stars/keadex/keadex?style=flat)](https://github.com/keadex/keadex/stargazers) - Open Source, serverless IDE to code with C4-PlantUML and organize at a scale C4 model diagrams.
- [Liquid Grammar](https://github.com/rust-utilities/liquid-grammar-pest/) [![GitHub stars](https://img.shields.io/github/stars/rust-utilities/liquid-grammar-pest/?style=flat)](https://github.com/rust-utilities/liquid-grammar-pest//stargazers) - Generate `Pairs` and/or `Rules` for [Shopify](https://shopify.github.io/liquid/) Liquid (hash-tags _not-sponsored_ or _affiliated_) for use in consuming crates
- [ws2markdown](https://code.rosaelefanten.org/ws2markdown) - Converts WordStar documents into Markdown files.
- [TypeQL Rust](https://github.com/typedb/typeql/tree/master/rust) [![GitHub stars](https://img.shields.io/github/stars/typedb/typeql/tree/master/rust?style=flat)](https://github.com/typedb/typeql/tree/master/rust/stargazers) - TypeDB's query language, written in Pest
- [Woxi](https://github.com/ad-si/Woxi) [![GitHub stars](https://img.shields.io/github/stars/ad-si/Woxi?style=flat)](https://github.com/ad-si/Woxi/stargazers) - Interpreter and computer algebra system for a subset of the Wolfram Language.

## Tooling

### IDE Support

- [pest IDE tools](https://github.com/pest-parser/pest-ide-tools) [![GitHub stars](https://img.shields.io/github/stars/pest-parser/pest-ide-tools?style=flat)](https://github.com/pest-parser/pest-ide-tools/stargazers) - A main repository with LSP server and VSCode extension.
- [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=pest.pest-ide-tools)
- [IntelliJ IDEA Plugin](https://plugins.jetbrains.com/plugin/12046-pest)
- [pest.vim](https://github.com/pest-parser/pest.vim) [![GitHub stars](https://img.shields.io/github/stars/pest-parser/pest.vim?style=flat)](https://github.com/pest-parser/pest.vim/stargazers)
- [pest-fmt](https://github.com/pest-parser/pest-fmt) [![GitHub stars](https://img.shields.io/github/stars/pest-parser/pest-fmt?style=flat)](https://github.com/pest-parser/pest-fmt/stargazers) - It can help to format
pest grammars.
- [pest web debugger](https://github.com/tomtau/pest-web-debug) [![GitHub stars](https://img.shields.io/github/stars/tomtau/pest-web-debug?style=flat)](https://github.com/tomtau/pest-web-debug/stargazers) - Try it [online](https://tomtau.github.io/pest-web-debug/).

### Boilerplate reduction and testing

- [pest-ast](https://github.com/pest-parser/ast) [![GitHub stars](https://img.shields.io/github/stars/pest-parser/ast?style=flat)](https://github.com/pest-parser/ast/stargazers) - It can help to reduce boilerplate when converting pest parse trees to abstract syntax trees.
- [pest_consume](https://crates.io/crates/pest_consume) - This crate can help with the parse tree traversing boilerplate.
- [pest-test](https://crates.io/crates/pest-test) - It is a testing framework for pest grammars.
- [pest_ascii_tree](https://crates.io/crates/pest_ascii_tree) - Output `Pairs` in a tree on the console

### CLI Debugger

- [pest_debugger](https://docs.rs/pest_debugger/latest/pest_debugger/) - It is a crate for debugging pest grammars. It can be used as a CLI tool or as a library. [See instructions for using the CLI debugger](debugger.md).
