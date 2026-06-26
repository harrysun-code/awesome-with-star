# Scala Native

[![GitHub stars](https://img.shields.io/github/stars/tindzk/awesome-scala-native?style=flat)](https://github.com/tindzk/awesome-scala-native/stargazers)

# Awesome Scala Native [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="http://www.scala-native.org/"><img alt="Scala Native" align="right" width="250" height="250" src="logo.png"></a>

[Scala Native](http://www.scala-native.org/) is an optimising ahead-of-time compiler for the [Scala programming language](https://www.scala-lang.org/). Traditionally, a virtual machine, the [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine), was required to run Scala programs. Scala Native taps into the compiler to emit [LLVM intermediate representation](http://llvm.org/docs/LangRef.html) rather than JVM bytecode. Then, the [LLVM](http://llvm.org/) compiler infrastructure is used to produce native libraries and executables. Given that Scala Native executables are stand-alone programs, they generally have a shorter start-up time and low memory consumption. This opens up new avenues to deploy Scala programs where previously the virtual machine would be the limiting factor. For example, developers could write programs for the command line or embedded devices.

## Contents
- [Awesome Scala Native ](#awesome-scala-native-)
  - [Contents](#contents)
  - [Tutorials and Examples](#tutorials-and-examples)
  - [Build Tools](#build-tools)
  - [Functional Programming](#functional-programming)
  - [Unit Tests](#unit-tests)
  - [Bindings](#bindings)
  - [File Formats and Parsers](#file-formats-and-parsers)
  - [Databases](#databases)
  - [Web Development](#web-development)
  - [Concurrency](#concurrency)
  - [Logging](#logging)
  - [Console](#console)
  - [Robotics](#robotics)
  - [Programs](#programs)
  - [Infrastructure](#infrastructure)
  - [Licence](#licence)

## Tutorials and Examples
* [Giter8 template for a minimal Scala Native project](https://github.com/scala-native/scala-native.g8) [![GitHub stars](https://img.shields.io/github/stars/scala-native/scala-native.g8?style=flat)](https://github.com/scala-native/scala-native.g8/stargazers) - Official [Giter8](http://www.foundweekends.org/giter8/) template for a minimal Scala Native project.
* [Hands on Scala Native](https://github.com/MasseGuillaume/hands-on-scala-native) [![GitHub stars](https://img.shields.io/github/stars/MasseGuillaume/hands-on-scala-native?style=flat)](https://github.com/MasseGuillaume/hands-on-scala-native/stargazers) - Tutorial for implementing a bandwidth monitor with Ncurses.
* [Starter for Scala Native](https://github.com/GnaneshKunal/scala-native-starter) [![GitHub stars](https://img.shields.io/github/stars/GnaneshKunal/scala-native-starter?style=flat)](https://github.com/GnaneshKunal/scala-native-starter/stargazers) - Scala Native project that links to a custom C library.
* [Building C code using sbt-jni](https://github.com/nadavwr/scala-native-sbt-jni-example) [![GitHub stars](https://img.shields.io/github/stars/nadavwr/scala-native-sbt-jni-example?style=flat)](https://github.com/nadavwr/scala-native-sbt-jni-example/stargazers) - Example for compiling C code in a Scala Native project using [sbt-jni](https://github.com/jodersky/sbt-jni) [![GitHub stars](https://img.shields.io/github/stars/jodersky/sbt-jni?style=flat)](https://github.com/jodersky/sbt-jni/stargazers).
* [Example project with external dependencies](https://github.com/lihaoyi/scala-native-example-app) [![GitHub stars](https://img.shields.io/github/stars/lihaoyi/scala-native-example-app?style=flat)](https://github.com/lihaoyi/scala-native-example-app/stargazers) - Example project that uses external dependencies to generate HTML and run a test suite.
* [Starter for Gtk+ Projects](https://github.com/jokade/scalanative-gtk-seed.g8) [![GitHub stars](https://img.shields.io/github/stars/jokade/scalanative-gtk-seed.g8?style=flat)](https://github.com/jokade/scalanative-gtk-seed.g8/stargazers) - [Giter8](http://www.foundweekends.org/giter8/) template for Scala Native GUI projects using [Gtk+](https://developer.gnome.org/gtk3/stable/index.html).
* [Modern systems programming with scala native](https://pragprog.com/titles/rwscala/modern-systems-programming-with-scala-native/) book.
* [Write a simple CLI application in Scala Native](https://github.com/ItoYo16u/prettytable-native) [![GitHub stars](https://img.shields.io/github/stars/ItoYo16u/prettytable-native?style=flat)](https://github.com/ItoYo16u/prettytable-native/stargazers)
## Build Tools
* [sbt](https://www.scala-sbt.org/) - Scala's standard build tool.
* [Mill](https://github.com/com-lihaoyi/mill) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/mill?style=flat)](https://github.com/com-lihaoyi/mill/stargazers) - Build tool striving for simplicity, inspired by [Bazel](https://www.bazel.build/).
* [Bloop](https://github.com/scalacenter/bloop) [![GitHub stars](https://img.shields.io/github/stars/scalacenter/bloop?style=flat)](https://github.com/scalacenter/bloop/stargazers) - Scala build server and command-line tool for fast developer workflows.
* [Seed](https://github.com/tindzk/seed) [![GitHub stars](https://img.shields.io/github/stars/tindzk/seed?style=flat)](https://github.com/tindzk/seed/stargazers) - Build tool based on Bloop. Focuses on user experience and cross-platform builds, inspired by [Cargo](https://github.com/rust-lang/cargo) [![GitHub stars](https://img.shields.io/github/stars/rust-lang/cargo?style=flat)](https://github.com/rust-lang/cargo/stargazers).

## Functional Programming
* [Shapeless](https://github.com/milessabin/shapeless) [![GitHub stars](https://img.shields.io/github/stars/milessabin/shapeless?style=flat)](https://github.com/milessabin/shapeless/stargazers) - Library for generic programming.
* [Squants](https://github.com/typelevel/squants) [![GitHub stars](https://img.shields.io/github/stars/typelevel/squants?style=flat)](https://github.com/typelevel/squants/stargazers) - DSL for quantities, units of measure and dimensional analysis.
* [scalaz](https://github.com/scalaz/scalaz) [![GitHub stars](https://img.shields.io/github/stars/scalaz/scalaz?style=flat)](https://github.com/scalaz/scalaz/stargazers) - Type classes and instances for data structures.
* [nobox](https://github.com/xuwei-k/nobox) [![GitHub stars](https://img.shields.io/github/stars/xuwei-k/nobox?style=flat)](https://github.com/xuwei-k/nobox/stargazers) - Immutable primitive array wrapper without boxing.
* [PPrint](https://github.com/lihaoyi/PPrint) [![GitHub stars](https://img.shields.io/github/stars/lihaoyi/PPrint?style=flat)](https://github.com/lihaoyi/PPrint/stargazers) - Pretty-print values and types.
* [SourceCode](https://github.com/lihaoyi/sourcecode) [![GitHub stars](https://img.shields.io/github/stars/lihaoyi/sourcecode?style=flat)](https://github.com/lihaoyi/sourcecode/stargazers) - Implicits providing meta data similar to `__LINE__` in C.
* [reactify](https://github.com/outr/reactify) [![GitHub stars](https://img.shields.io/github/stars/outr/reactify?style=flat)](https://github.com/outr/reactify/stargazers) - Functional Reactive Programming framework for Scala.
* [chimney](https://github.com/scalalandio/chimney) [![GitHub stars](https://img.shields.io/github/stars/scalalandio/chimney?style=flat)](https://github.com/scalalandio/chimney/stargazers) - Boilerplate-free data transformations.
* [Quicklens](https://github.com/softwaremill/quicklens) [![GitHub stars](https://img.shields.io/github/stars/softwaremill/quicklens?style=flat)](https://github.com/softwaremill/quicklens/stargazers) - Modify deeply nested case class fields.
* [Cats](https://github.com/typelevel/cats) [![GitHub stars](https://img.shields.io/github/stars/typelevel/cats?style=flat)](https://github.com/typelevel/cats/stargazers) - Abstractions for functional programming in Scala.

## Unit Tests
* [µTest](https://github.com/lihaoyi/utest) [![GitHub stars](https://img.shields.io/github/stars/lihaoyi/utest?style=flat)](https://github.com/lihaoyi/utest/stargazers) - Library for unit tests.
* [minitest](https://github.com/monix/minitest) [![GitHub stars](https://img.shields.io/github/stars/monix/minitest?style=flat)](https://github.com/monix/minitest/stargazers) - Lightweight testing library.
* [scalaprops](https://github.com/scalaprops/scalaprops) [![GitHub stars](https://img.shields.io/github/stars/scalaprops/scalaprops?style=flat)](https://github.com/scalaprops/scalaprops/stargazers) - Library for property-based testing.
  * [scalaprops-shapeless](https://github.com/scalaprops/scalaprops-shapeless) [![GitHub stars](https://img.shields.io/github/stars/scalaprops/scalaprops-shapeless?style=flat)](https://github.com/scalaprops/scalaprops-shapeless/stargazers) - Generation of arbitrary ADT instances.
  * [scalaprops-cross-example](https://github.com/scalaprops/scalaprops-cross-example) [![GitHub stars](https://img.shields.io/github/stars/scalaprops/scalaprops-cross-example?style=flat)](https://github.com/scalaprops/scalaprops-cross-example/stargazers) - Cross-platform example.
* [ScalaCheck](https://github.com/typelevel/scalacheck) [![GitHub stars](https://img.shields.io/github/stars/typelevel/scalacheck?style=flat)](https://github.com/typelevel/scalacheck/stargazers) - Property-based testing for Scala.
* [ScalaTest](https://github.com/scalatest/scalatest) [![GitHub stars](https://img.shields.io/github/stars/scalatest/scalatest?style=flat)](https://github.com/scalatest/scalatest/stargazers) - Testing library.
* [specs2](https://github.com/etorreborre/specs2) [![GitHub stars](https://img.shields.io/github/stars/etorreborre/specs2?style=flat)](https://github.com/etorreborre/specs2/stargazers) - Software Specifications for Scala.
* [Makeshift](https://github.com/nadavwr/makeshift) [![GitHub stars](https://img.shields.io/github/stars/nadavwr/makeshift?style=flat)](https://github.com/nadavwr/makeshift/stargazers) - Library for unit tests.
* [MUnit](https://github.com/scalameta/munit) [![GitHub stars](https://img.shields.io/github/stars/scalameta/munit?style=flat)](https://github.com/scalameta/munit/stargazers) - Scala testing library with actionable errors and extensible APIs.

## Bindings
* [cmark](https://github.com/sparsetech/cmark-scala) [![GitHub stars](https://img.shields.io/github/stars/sparsetech/cmark-scala?style=flat)](https://github.com/sparsetech/cmark-scala/stargazers) - Bindings for the [cmark](https://github.com/commonmark/cmark) [![GitHub stars](https://img.shields.io/github/stars/commonmark/cmark?style=flat)](https://github.com/commonmark/cmark/stargazers) CommonMark parser library.
* [libuv](https://github.com/TimothyKlim/scala-native-libuv) [![GitHub stars](https://img.shields.io/github/stars/TimothyKlim/scala-native-libuv?style=flat)](https://github.com/TimothyKlim/scala-native-libuv/stargazers) - Bindings for [libuv](https://github.com/libuv/libuv) [![GitHub stars](https://img.shields.io/github/stars/libuv/libuv?style=flat)](https://github.com/libuv/libuv/stargazers), a library for asynchronous I/O.
* [SDL2 and OpenGL](https://github.com/regb/scalanative-graphics-bindings) [![GitHub stars](https://img.shields.io/github/stars/regb/scalanative-graphics-bindings?style=flat)](https://github.com/regb/scalanative-graphics-bindings/stargazers) - Bindings for the graphical frameworks [SDL2](https://www.libsdl.org/) and [OpenGL](https://www.opengl.org).
* [Cocoa](https://github.com/jokade/scalanative-cocoa) [![GitHub stars](https://img.shields.io/github/stars/jokade/scalanative-cocoa?style=flat)](https://github.com/jokade/scalanative-cocoa/stargazers) - Bindings for the macOS graphical framework [Cocoa](https://en.wikipedia.org/wiki/Cocoa_(API)).
* [GNU Scientific Library](https://github.com/ruivieira/scala-gsl) [![GitHub stars](https://img.shields.io/github/stars/ruivieira/scala-gsl?style=flat)](https://github.com/ruivieira/scala-gsl/stargazers) - Bindings for [GNU Scientific Library (GSL)](https://www.gnu.org/software/gsl).
* [BLAS](https://github.com/ekrich/sblas) [![GitHub stars](https://img.shields.io/github/stars/ekrich/sblas?style=flat)](https://github.com/ekrich/sblas/stargazers) - Bindings for [BLAS](http://www.netlib.org/blas/), a library for Linear Algebra.
* [Gtk+](https://github.com/jokade/scalanative-gtk) [![GitHub stars](https://img.shields.io/github/stars/jokade/scalanative-gtk?style=flat)](https://github.com/jokade/scalanative-gtk/stargazers) - Bindings for the [GTK+](https://www.gtk.org/) graphical toolkit.
* [libsoup](https://github.com/jokade/scalanative-libsoup) [![GitHub stars](https://img.shields.io/github/stars/jokade/scalanative-libsoup?style=flat)](https://github.com/jokade/scalanative-libsoup/stargazers) - Bindings for the [libsoup](https://wiki.gnome.org/Projects/libsoup) HTTP client/server library.
* [libui](https://github.com/lolgab/scalaui) [![GitHub stars](https://img.shields.io/github/stars/lolgab/scalaui?style=flat)](https://github.com/lolgab/scalaui/stargazers) - GUI framework based on [libui](https://github.com/andlabs/libui) [![GitHub stars](https://img.shields.io/github/stars/andlabs/libui?style=flat)](https://github.com/andlabs/libui/stargazers).
* [GStreamer](https://github.com/jokade/scalanative-gstreamer) [![GitHub stars](https://img.shields.io/github/stars/jokade/scalanative-gstreamer?style=flat)](https://github.com/jokade/scalanative-gstreamer/stargazers) - Bindings for the [GStreamer](https://gstreamer.freedesktop.org) multimedia framework.
* [Qt](https://github.com/jokade/scalanative-qt5) [![GitHub stars](https://img.shields.io/github/stars/jokade/scalanative-qt5?style=flat)](https://github.com/jokade/scalanative-qt5/stargazers) - Bindings for [Qt](https://www.qt.io).
* [ncurses](https://github.com/edadma/ncurses) [![GitHub stars](https://img.shields.io/github/stars/edadma/ncurses?style=flat)](https://github.com/edadma/ncurses/stargazers) - Bindings for the [GNU Ncurses Library](https://www.gnu.org/software/ncurses/).
* [readline](https://github.com/edadma/readline) [![GitHub stars](https://img.shields.io/github/stars/edadma/readline?style=flat)](https://github.com/edadma/readline/stargazers) - Bindings for the [GNU Readline Library](https://www.gnu.org/software/readline/).
* [libsndfile](https://github.com/edadma/libsndfile) [![GitHub stars](https://img.shields.io/github/stars/edadma/libsndfile?style=flat)](https://github.com/edadma/libsndfile/stargazers) - Bindings for the [Libsndfile](https://tiswww.cwru.edu/php/chet/libsndfile/rltop.html) C library for sampled sound manipulation.
* [libpng](https://github.com/edadma/libpng) [![GitHub stars](https://img.shields.io/github/stars/edadma/libpng?style=flat)](https://github.com/edadma/libpng/stargazers) - Bindings for the [libpng](http://www.libpng.org/) C reference library for reading and writing PNGs.
* [libcairo](https://github.com/edadma/libcairo) [![GitHub stars](https://img.shields.io/github/stars/edadma/libcairo?style=flat)](https://github.com/edadma/libcairo/stargazers) - Bindings for the [Cairo](https://www.cairographics.org/) 2D graphics C library.
* [cairo-xlib](https://github.com/edadma/cairo-xlib) [![GitHub stars](https://img.shields.io/github/stars/edadma/cairo-xlib?style=flat)](https://github.com/edadma/cairo-xlib/stargazers) - Bindings for the [Cairo](https://www.cairographics.org/) 2D graphics [XLib Surfaces](https://www.cairographics.org/manual/cairo-XLib-Surfaces.html) with bindings for [XLib](https://www.x.org/releases/current/doc/libX11/libX11/libX11.html) as well.
* [libyaml](https://github.com/edadma/libyaml) [![GitHub stars](https://img.shields.io/github/stars/edadma/libyaml?style=flat)](https://github.com/edadma/libyaml/stargazers) - Bindings for the [LibYAML](https://pyyaml.org/wiki/LibYAML) C library for parsing [YAML](https://yaml.org/).
* [iup](https://github.com/edadma/iup) [![GitHub stars](https://img.shields.io/github/stars/edadma/iup?style=flat)](https://github.com/edadma/iup/stargazers) - Bindings for the [IUP](https://www.tecgraf.puc-rio.br/iup/) multi-platform toolkit for building graphical user interfaces.

## File Formats and Parsers
* [msgpack4z](https://github.com/msgpack4z/msgpack4z-native) [![GitHub stars](https://img.shields.io/github/stars/msgpack4z/msgpack4z-native?style=flat)](https://github.com/msgpack4z/msgpack4z-native/stargazers) - Implementation of [MessagePack](https://msgpack.org/), a binary serialisation format.
* [FastParse](https://github.com/com-lihaoyi/fastparse) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/fastparse?style=flat)](https://github.com/com-lihaoyi/fastparse/stargazers) - Library for defining and running parsers.
* [scalatags](https://github.com/com-lihaoyi/scalatags) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/scalatags?style=flat)](https://github.com/com-lihaoyi/scalatags/stargazers) - HTML/XML construction and rendering.
* [Pine](https://github.com/sparsetech/pine) [![GitHub stars](https://img.shields.io/github/stars/sparsetech/pine?style=flat)](https://github.com/sparsetech/pine/stargazers) - HTML/XML parsing, manipulation and rendering.
* [scala-json](https://github.com/MediaMath/scala-json) [![GitHub stars](https://img.shields.io/github/stars/MediaMath/scala-json?style=flat)](https://github.com/MediaMath/scala-json/stargazers) - JSON parser.
* [uPickle](https://github.com/com-lihaoyi/upickle) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/upickle?style=flat)](https://github.com/com-lihaoyi/upickle/stargazers) - uPickle: a simple, fast, dependency-free JSON & Binary (MessagePack) serialization library for Scala
* [toml-scala](https://github.com/sparsetech/toml-scala) [![GitHub stars](https://img.shields.io/github/stars/sparsetech/toml-scala?style=flat)](https://github.com/sparsetech/toml-scala/stargazers) - [TOML](https://github.com/toml-lang/toml) [![GitHub stars](https://img.shields.io/github/stars/toml-lang/toml?style=flat)](https://github.com/toml-lang/toml/stargazers) parser with codec derivation.
* [argonaut](https://github.com/argonaut-io/argonaut) [![GitHub stars](https://img.shields.io/github/stars/argonaut-io/argonaut?style=flat)](https://github.com/argonaut-io/argonaut/stargazers) - Purely functional JSON parser and library.
* [ScalaPB](https://github.com/scalapb/ScalaPB) [![GitHub stars](https://img.shields.io/github/stars/scalapb/ScalaPB?style=flat)](https://github.com/scalapb/ScalaPB/stargazers) - [Protocol Buffer](https://developers.google.com/protocol-buffers/) compiler for Scala.
  * [scalapb-argonaut](https://github.com/scalapb-json/scalapb-argonaut) [![GitHub stars](https://img.shields.io/github/stars/scalapb-json/scalapb-argonaut?style=flat)](https://github.com/scalapb-json/scalapb-argonaut/stargazers) - JSON and Protocol Buffer converters for ScalaPB based on [Argonaut](http://argonaut.io).
* [sconfig](https://github.com/ekrich/sconfig) [![GitHub stars](https://img.shields.io/github/stars/ekrich/sconfig?style=flat)](https://github.com/ekrich/sconfig/stargazers) - [HOCON](https://github.com/ekrich/sconfig/blob/master/docs/original/HOCON.md) [![GitHub stars](https://img.shields.io/github/stars/ekrich/sconfig/blob/master/docs/original/HOCON.md?style=flat)](https://github.com/ekrich/sconfig/blob/master/docs/original/HOCON.md/stargazers) parser.
* [squiggly](https://github.com/edadma/squiggly) [![GitHub stars](https://img.shields.io/github/stars/edadma/squiggly?style=flat)](https://github.com/edadma/squiggly/stargazers) - Cross-platform template language for Scala, inspired by Liquid and Hugo templates.

## Databases
* [scala-native-jdbc](https://github.com/lolgab/scala-native-jdbc) [![GitHub stars](https://img.shields.io/github/stars/lolgab/scala-native-jdbc?style=flat)](https://github.com/lolgab/scala-native-jdbc/stargazers) - Port of the database access layer [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity) to Scala Native.
* [SQLite4S](https://github.com/david-bouyssie/sqlite4s) [![GitHub stars](https://img.shields.io/github/stars/david-bouyssie/sqlite4s?style=flat)](https://github.com/david-bouyssie/sqlite4s/stargazers) - Port of the Java library [Sqlite4java](https://bitbucket.org/almworks/sqlite4java). Includes bindings for the SQLite native library.
* [libpq4s](https://github.com/david-bouyssie/libpq4s) [![GitHub stars](https://img.shields.io/github/stars/david-bouyssie/libpq4s?style=flat)](https://github.com/david-bouyssie/libpq4s/stargazers) - Scala wrapper around the async PostgreSQL C library libpq.
* [skunk](https://github.com/typelevel/skunk) [![GitHub stars](https://img.shields.io/github/stars/typelevel/skunk?style=flat)](https://github.com/typelevel/skunk/stargazers) -  A data access library for Scala + Postgres.

## Web Development
* [Trail](https://github.com/sparsetech/trail) [![GitHub stars](https://img.shields.io/github/stars/sparsetech/trail?style=flat)](https://github.com/sparsetech/trail/stargazers) - Routing library.
* [sttp](https://github.com/softwaremill/sttp) [![GitHub stars](https://img.shields.io/github/stars/softwaremill/sttp?style=flat)](https://github.com/softwaremill/sttp/stargazers) - HTTP Client library.
* [snunit](https://github.com/lolgab/snunit) [![GitHub stars](https://img.shields.io/github/stars/lolgab/snunit?style=flat)](https://github.com/lolgab/snunit/stargazers) - Scala Native HTTP server based on NGINX Unit.

## Concurrency
* [scala-native-loop](https://github.com/scala-native/scala-native-loop) [![GitHub stars](https://img.shields.io/github/stars/scala-native/scala-native-loop?style=flat)](https://github.com/scala-native/scala-native-loop/stargazers) - Event loop and async-oriented IO for Scala Native
* [castor](https://github.com/com-lihaoyi/castor) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/castor?style=flat)](https://github.com/com-lihaoyi/castor/stargazers) - Lightweight, typed Actor library for Scala.

## Logging
* [scribe](https://github.com/outr/scribe) [![GitHub stars](https://img.shields.io/github/stars/outr/scribe?style=flat)](https://github.com/outr/scribe/stargazers) - Fast and simple logging library.
* [slogging](https://github.com/jokade/slogging) [![GitHub stars](https://img.shields.io/github/stars/jokade/slogging?style=flat)](https://github.com/jokade/slogging/stargazers) - [Typesafe-logging](https://github.com/lightbend/scala-logging) [![GitHub stars](https://img.shields.io/github/stars/lightbend/scala-logging?style=flat)](https://github.com/lightbend/scala-logging/stargazers) and [SLF4J](https://www.slf4j.org/)-compatible logging library based on macros.

## Console
* [fansi](https://github.com/com-lihaoyi/fansi) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/fansi?style=flat)](https://github.com/com-lihaoyi/fansi/stargazers) - Library for creating [ANSI-coloured strings](https://en.wikipedia.org/wiki/ANSI_escape_code).
* [scopt](https://github.com/scopt/scopt) [![GitHub stars](https://img.shields.io/github/stars/scopt/scopt?style=flat)](https://github.com/scopt/scopt/stargazers) - Command-line argument parser.
* [scala-optparse-applicative](https://github.com/xuwei-k/optparse-applicative) [![GitHub stars](https://img.shields.io/github/stars/xuwei-k/optparse-applicative?style=flat)](https://github.com/xuwei-k/optparse-applicative/stargazers) - Port of Haskell's CLI argument parsing library [optparse-applicative](https://hackage.haskell.org/package/optparse-applicative).
* [scallop](https://github.com/scallop/scallop) [![GitHub stars](https://img.shields.io/github/stars/scallop/scallop?style=flat)](https://github.com/scallop/scallop/stargazers) - A simple Scala CLI parsing library.
* [mainargs](https://github.com/com-lihaoyi/mainargs) [![GitHub stars](https://img.shields.io/github/stars/com-lihaoyi/mainargs?style=flat)](https://github.com/com-lihaoyi/mainargs/stargazers) - Small, dependency-free library for command line argument parsing in Scala.
* [decline](https://github.com/bkirwi/decline) [![GitHub stars](https://img.shields.io/github/stars/bkirwi/decline?style=flat)](https://github.com/bkirwi/decline/stargazers) - A composable command-line parser for Scala.

## Robotics
* [Potassium](https://github.com/Team846/potassium) [![GitHub stars](https://img.shields.io/github/stars/Team846/potassium?style=flat)](https://github.com/Team846/potassium/stargazers) - Framework for writing robot software.
* [WPILib](https://github.com/Team846/scala-native-wpilib) [![GitHub stars](https://img.shields.io/github/stars/Team846/scala-native-wpilib?style=flat)](https://github.com/Team846/scala-native-wpilib/stargazers) - Reimplementation of the [FIRST Robotics WPILib libraries](http://first.wpi.edu/FRC/roborio/release/docs/java/).

## Programs
* [sglgears](https://github.com/Milyardo/sglgears) [![GitHub stars](https://img.shields.io/github/stars/Milyardo/sglgears?style=flat)](https://github.com/Milyardo/sglgears/stargazers) - Port of GL [gears.c](https://github.com/JoakimSoderberg/mesademos/blob/master/src/xdemos/glxgears.c) [![GitHub stars](https://img.shields.io/github/stars/JoakimSoderberg/mesademos/blob/master/src/xdemos/glxgears.c?style=flat)](https://github.com/JoakimSoderberg/mesademos/blob/master/src/xdemos/glxgears.c/stargazers).
* [k8s-cli](https://github.com/fsat/k8s-cli) [![GitHub stars](https://img.shields.io/github/stars/fsat/k8s-cli?style=flat)](https://github.com/fsat/k8s-cli/stargazers) - CLI tools to generate [Kubernetes](https://kubernetes.io/) resources for [Akka](https://akka.io/), [Play Framework](https://www.playframework.com/) and [Lagom](https://www.lagomframework.com/)-based applications.
* [Coursier](https://github.com/coursier/coursier) [![GitHub stars](https://img.shields.io/github/stars/coursier/coursier?style=flat)](https://github.com/coursier/coursier/stargazers) - Coursier's [`bootstrap` command](https://get-coursier.io/docs/cli-native-bootstrap) generates native launchers.
* [fractals](https://github.com/Rusty-Bike/fractals) [![GitHub stars](https://img.shields.io/github/stars/Rusty-Bike/fractals?style=flat)](https://github.com/Rusty-Bike/fractals/stargazers) - A self-similar fractal generator with basic animation support.
## Infrastructure
* [Seed Docker image](https://hub.docker.com/r/tindzk/seed/tags) - Docker image for cross-platform builds with [Seed](https://github.com/tindzk/seed) [![GitHub stars](https://img.shields.io/github/stars/tindzk/seed?style=flat)](https://github.com/tindzk/seed/stargazers).
* [scala-native-sbt-docker](https://github.com/ScalaWilliam/scala-native-sbt-docker) [![GitHub stars](https://img.shields.io/github/stars/ScalaWilliam/scala-native-sbt-docker?style=flat)](https://github.com/ScalaWilliam/scala-native-sbt-docker/stargazers) - Docker image for Scala Native and sbt.

## Licence
<a rel="licence" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg" /></a><br />This work is licenced under a <a rel="licence" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International Licence</a>.
