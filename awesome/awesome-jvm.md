# JVM

> 来源：[deephacks/awesome-jvm](https://github.com/deephacks/awesome-jvm)

[![GitHub stars](https://img.shields.io/github/stars/deephacks/awesome-jvm?style=flat)](https://github.com/deephacks/awesome-jvm/stargazers)

# Awesome JVM [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome JVM low level, performance and non-framework related stuff.

- [Awesome JVM](#awesome-jvm)
    - [Bytecode](#bytecode)
    - [Garbage collectors](#garbage-collectors)
    - [Load tools](#load-tools)
    - [Languages](#languages)
    - [Machine Learning](#machine-learning)
    - [Memory and Concurrency](#memory-and-concurrency)
    - [Metaprogramming](#metaprogramming)
    - [Native](#native)
    - [Network](#network)
    - [Nix tools](#nix-tools)
    - [Profilers](#profilers)
    - [Runtimes](#runtimes)
    - [Virtual Machines](#virtual-machines)
- [Resources](#resources)
    - [Communities](#communities)    
    - [Documentation](#documentation)
    - [Media](#media)
    - [People](#people)
- [Contributing](#contributing)


## Bytecode

*Tools for bytecode manipulation and analysis.*

* [asmtools](https://wiki.openjdk.java.net/display/CodeTools/asmtools) - Used to develop tools for the production of Java .class files.
* [Byte Buddy](http://bytebuddy.net) - Code generation library creating Java classes at runtime without the help of a compiler.
* [Jitescript](https://github.com/qmx/jitescript) [![GitHub stars](https://img.shields.io/github/stars/qmx/jitescript?style=flat)](https://github.com/qmx/jitescript/stargazers) - Bytecode generation library similar to BiteScript. 

## Garbage collectors

*Garbage collectors for the JVM.*

* [Azul Pauseless Garbage Collection](https://www.azul.com/files/wp_pgc_zing_v52.pdf) - Providing continuous, pauseless operation for Java applications.
* [Balanced GC](http://www.ibm.com/developerworks/websphere/techjournal/1108_sciampacone/1108_sciampacone.html) - GC policy available in the Java Virtual Machine for IBM WebSphere Application Server V8.
* [Epsilon GC](http://openjdk.java.net/jeps/318) - Completely passive GC implementation with bounded allocation limit, and lowest runtime performance overhead possible.
* [G1](http://www.oracle.com/technetwork/java/javase/tech/g1-intro-jsp-135488.html) - The Garbage-First Garbage Collector.
* [Shenandoah](http://openjdk.java.net/jeps/189) - Ultra-Low-Pause-Time Garbage Collector.
* [The Garbage Collection Handbook](http://gchandbook.org) - Book that addresses new challenges to garbage collection made by recent advances in hardware and software.
* [ZGC](http://mail.openjdk.java.net/pipermail/announce/2017-October/000237.html) - Garbage collector optimized for low latency and very large heaps.

## Load tools

*Tools that generate load and measure the system accurately without coordinated omission*

* [Gatling](http://gatling.io) - Asynchronous non-blocking scenario driven load testing tool for testing HTTP servers.
* [wrk2](https://github.com/giltene/wrk2) [![GitHub stars](https://img.shields.io/github/stars/giltene/wrk2?style=flat)](https://github.com/giltene/wrk2/stargazers) - A constant throughput, correct latency recording variant of wrk.

## Languages

*Languages running on the JVM.*
* [Ceylon](http://ceylon-lang.org/) - Object-oriented, strong and static programming language with an emphasis on immutability, created by Red Hat.
* [Clojure](http://clojure.org/) - Dialect of Lisp created by Rich Hickey. Dynamically typed with emphasis on functional programming.
* [Erjang](http://www.erjang.org) - A JVM-based Erlang VM.
* [Eta](http://eta-lang.org/) - Pure, lazy, strongly typed functional programming language on the JVM.
* [Frege](https://github.com/Frege/frege) [![GitHub stars](https://img.shields.io/github/stars/Frege/frege?style=flat)](https://github.com/Frege/frege/stargazers) - Pure functional programming language in the spirit of Haskell.
* [gojava](https://github.com/sridharv/gojava) [![GitHub stars](https://img.shields.io/github/stars/sridharv/gojava?style=flat)](https://github.com/sridharv/gojava/stargazers) - Java bindings for Go packages.
* [Golo](http://golo-lang.org/) - A simple dynamic language that makes extensive usage of `invokedynamic`.
* [Groovy](http://www.groovy-lang.org/) - Optionally typed and dynamic language, with static-typing and static compilation capabilities.
* [Java](http://www.oracle.com/technetwork/java/javase/overview/index.html) - General-purpose, concurrent, strongly typed, class-based object-oriented language.
* [JRuby](http://jruby.org) - Implementation of the Ruby language on the JVM.
* [JPHP](https://github.com/jphp-group/jphp) [![GitHub stars](https://img.shields.io/github/stars/jphp-group/jphp?style=flat)](https://github.com/jphp-group/jphp/stargazers) - PHP on the Java VM.
* [Jython](http://www.jython.org) - Python for the Java Platform.
* [Kawa](http://www.gnu.org/software/kawa/) - Extension of the Scheme language, which is in the Lisp family of programming languages.
* [Kotlin](http://kotlinlang.org/) - Statically typed programming language for the JVM, Android and the browser.
* [LuaJ](http://www.luaj.org/luaj/3.0/README.html) - Java-centric implementation of lua vm built to leverage standard Java features.
* [Nashorn](http://openjdk.java.net/projects/nashorn/) - Lightweight high-performance JavaScript runtime in Java with a native JVM.
* [OCaml-Java](http://www.ocamljava.org/) - Supports OCaml language v4. Generates plain Java bytecode and have seamless integration with Java.
* [Rembulan](https://github.com/mjanicek/rembulan) [![GitHub stars](https://img.shields.io/github/stars/mjanicek/rembulan?style=flat)](https://github.com/mjanicek/rembulan/stargazers) - Rembulan is an implementation of Lua 5.3 for the JVM, written in pure Java with minimal dependencies.
* [Renjin](http://www.renjin.org/) - JVM-based interpreter for the R language for the statistical analysis
* [Scala](http://www.scala-lang.org/) - Strong and static programming language that combine object-oriented and functional programming ideas.
* [Xtend](http://www.eclipse.org/xtend/) - Flexible and expressive dialect of Java, which compiles into Java 5 source code.

## Machine Learning
* [Deeplearning4j](https://deeplearning4j.org/) - Open-Source, Distributed, Deep Learning Library for the JVM.
* [H2O](https://www.h2o.ai/) - Fast statistical, machine learning & math runtime.
* [Smile](https://github.com/haifengl/smile) [![GitHub stars](https://img.shields.io/github/stars/haifengl/smile?style=flat)](https://github.com/haifengl/smile/stargazers) - Statistical Machine Intelligence & Learning Engine.

## Memory and concurrency

*Tools and data structures for efficient memory layout and concurrent access.*

* [Agera](https://github.com/google/agera) [![GitHub stars](https://img.shields.io/github/stars/google/agera?style=flat)](https://github.com/google/agera/stargazers) - Reactive Programming for Android by Google.
* [Agrona](https://github.com/real-logic/Agrona) [![GitHub stars](https://img.shields.io/github/stars/real-logic/Agrona?style=flat)](https://github.com/real-logic/Agrona/stargazers) - Library of data structures and utility methods that are a common need when building high-performance applications.
* [Apache Arrow](http://arrow.apache.org/) - A high-performance cross-system data layer for columnar in-memory analytics.
* [bloofi](https://github.com/lemire/bloofi) [![GitHub stars](https://img.shields.io/github/stars/lemire/bloofi?style=flat)](https://github.com/lemire/bloofi/stargazers) - Java implementation of multidimensional Bloom filters
* [Cap’n Proto](https://capnproto.org/) - Insanely fast data interchange format and capability-based RPC system.
* [caffeine](https://github.com/ben-manes/caffeine) [![GitHub stars](https://img.shields.io/github/stars/ben-manes/caffeine?style=flat)](https://github.com/ben-manes/caffeine/stargazers) - A high performance caching library for Java 8.
* [Chronicle-Bytes](https://github.com/OpenHFT/Chronicle-Bytes) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/Chronicle-Bytes?style=flat)](https://github.com/OpenHFT/Chronicle-Bytes/stargazers) - Low level memory access wrappers.
* [Chronicle-Queue](https://github.com/OpenHFT/Chronicle-Queue) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/Chronicle-Queue?style=flat)](https://github.com/OpenHFT/Chronicle-Queue/stargazers) - Micro second messaging that stores everything to disk.
* [Chronicle-Map](https://github.com/OpenHFT/Chronicle-Map) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/Chronicle-Map?style=flat)](https://github.com/OpenHFT/Chronicle-Map/stargazers) - In-memory key-value store designed for low-latency and/or multi-process applications.
* [clj-ds](https://github.com/krukow/clj-ds) [![GitHub stars](https://img.shields.io/github/stars/krukow/clj-ds?style=flat)](https://github.com/krukow/clj-ds/stargazers) - Clojure's data structures modified for use outside of Clojure.
* [colfer](https://github.com/pascaldekloe/colfer) [![GitHub stars](https://img.shields.io/github/stars/pascaldekloe/colfer?style=flat)](https://github.com/pascaldekloe/colfer/stargazers) - Binary serialization format and class generator.
* [commons-math](http://commons.apache.org/proper/commons-math) - Library of lightweight, self-contained mathematics and statistics components.
* [CuckooFilter4J](https://github.com/MGunlogson/CuckooFilter4J) [![GitHub stars](https://img.shields.io/github/stars/MGunlogson/CuckooFilter4J?style=flat)](https://github.com/MGunlogson/CuckooFilter4J/stargazers) - Bloom filter replacement for approximated set-membership queries.
* [cyclops](https://github.com/aol/cyclops) [![GitHub stars](https://img.shields.io/github/stars/aol/cyclops?style=flat)](https://github.com/aol/cyclops/stargazers) - Integration modules for RxJava, Reactor, FunctionalJava, Guava & Javaslang.
* [Eclipse Collections](https://github.com/eclipse/eclipse-collections) [![GitHub stars](https://img.shields.io/github/stars/eclipse/eclipse-collections?style=flat)](https://github.com/eclipse/eclipse-collections/stargazers) - Collections framework for Java.
* [externalsortinginjava](https://github.com/lemire/externalsortinginjava) [![GitHub stars](https://img.shields.io/github/stars/lemire/externalsortinginjava?style=flat)](https://github.com/lemire/externalsortinginjava/stargazers) - Sort very large files using multiple cores and an external-memory algorithm.
* [failsafe](https://github.com/jhalterman/failsafe) [![GitHub stars](https://img.shields.io/github/stars/jhalterman/failsafe?style=flat)](https://github.com/jhalterman/failsafe/stargazers) - A lightweight, zero-dependency library for handling failures.
* [fasttuple](https://github.com/boundary/fasttuple) [![GitHub stars](https://img.shields.io/github/stars/boundary/fasttuple?style=flat)](https://github.com/boundary/fasttuple/stargazers) - Collections that are laid out adjacently in both on- and off-heap memory.
* [fast-uuid](https://github.com/jchambers/fast-uuid) [![GitHub stars](https://img.shields.io/github/stars/jchambers/fast-uuid?style=flat)](https://github.com/jchambers/fast-uuid/stargazers) - Java library for quickly and efficiently parsing and writing UUIDs.
* [FlatBuffers](http://google.github.io/flatbuffers/) - Efficient cross platform serialization library for C++, C#, Go, Java, JavaScript, PHP, and Python.
* [geohash](https://github.com/davidmoten/geo) [![GitHub stars](https://img.shields.io/github/stars/davidmoten/geo?style=flat)](https://github.com/davidmoten/geo/stargazers) - Java utility methods for geohashing.
* [gs-collections](https://github.com/goldmansachs/gs-collections) [![GitHub stars](https://img.shields.io/github/stars/goldmansachs/gs-collections?style=flat)](https://github.com/goldmansachs/gs-collections/stargazers) - Goldman Sachs collections framework.
* [hollow](https://github.com/Netflix/hollow) [![GitHub stars](https://img.shields.io/github/stars/Netflix/hollow?style=flat)](https://github.com/Netflix/hollow/stargazers) - Java library and comprehensive toolset for harnessing small to moderately sized in-memory datasets.
* [high-scale-lib](https://github.com/boundary/high-scale-lib) [![GitHub stars](https://img.shields.io/github/stars/boundary/high-scale-lib?style=flat)](https://github.com/boundary/high-scale-lib/stargazers) - Cliff Click's High Scale Library.
* [hppc](https://github.com/carrotsearch/hppc) [![GitHub stars](https://img.shields.io/github/stars/carrotsearch/hppc?style=flat)](https://github.com/carrotsearch/hppc/stargazers) - High Performance Primitive Collections.
* [injector](https://github.com/belliottsmith/injector) [![GitHub stars](https://img.shields.io/github/stars/belliottsmith/injector?style=flat)](https://github.com/belliottsmith/injector/stargazers) - A new Executor for Java.
* [java-concurrent-hash-trie-map](https://github.com/romix/java-concurrent-hash-trie-map) [![GitHub stars](https://img.shields.io/github/stars/romix/java-concurrent-hash-trie-map?style=flat)](https://github.com/romix/java-concurrent-hash-trie-map/stargazers) - Java port of a concurrent trie hash map implementation from Scala collections.
* [java-hll](https://github.com/aggregateknowledge/java-hll) [![GitHub stars](https://img.shields.io/github/stars/aggregateknowledge/java-hll?style=flat)](https://github.com/aggregateknowledge/java-hll/stargazers) - Java library for the HyperLogLog algorithm.
* [JavaFastPFOR](https://github.com/lemire/JavaFastPFOR) [![GitHub stars](https://img.shields.io/github/stars/lemire/JavaFastPFOR?style=flat)](https://github.com/lemire/JavaFastPFOR/stargazers) - Library to compress and uncompress arrays of integers very fast.
* [java-string-similarity](https://github.com/tdebatty/java-string-similarity) [![GitHub stars](https://img.shields.io/github/stars/tdebatty/java-string-similarity?style=flat)](https://github.com/tdebatty/java-string-similarity/stargazers) - String similarity and distance measures, including Levenshtein edit distance and sibblings, Jaro-Winkler, Longest Common Subsequence, cosine similarity etc.
* [JCTools](http://jctools.github.io/JCTools/) - Concurrent data structures currently missing from the JDK.
* [DSL-JSON](http://github.com/ngs-doo/dsl-json) - High performance JSON library with advanced compile-time databinding.
* [jsoniter](http://jsoniter.com/) - Claims to be the fastest JSON parser ever (copy of DSL-JSON).
* [jOOL](https://github.com/jOOQ/jOOL) [![GitHub stars](https://img.shields.io/github/stars/jOOQ/jOOL?style=flat)](https://github.com/jOOQ/jOOL/stargazers) - Useful extensions to Java 8 lambdas.
* [Koloboke](https://github.com/OpenHFT/Koloboke) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/Koloboke?style=flat)](https://github.com/OpenHFT/Koloboke/stargazers) - Java Collections til the last breadcrumb of memory and performance.
* [LevelDB](https://github.com/dain/leveldb) [![GitHub stars](https://img.shields.io/github/stars/dain/leveldb?style=flat)](https://github.com/dain/leveldb/stargazers) - Rewrite (port) of LevelDB in Java.
* [lightweight_trie](https://github.com/bryanduxbury/lightweight_trie) [![GitHub stars](https://img.shields.io/github/stars/bryanduxbury/lightweight_trie?style=flat)](https://github.com/bryanduxbury/lightweight_trie/stargazers) - A very memory-efficient trie (radix tree) implementation.
* [lmdbjni](https://github.com/deephacks/lmdbjni) [![GitHub stars](https://img.shields.io/github/stars/deephacks/lmdbjni?style=flat)](https://github.com/deephacks/lmdbjni/stargazers) - Java API to LMDB (HawtJNI) which is an ultra-fast, ultra-compact key-value embedded data store written in C.
* [lmdbjava](https://github.com/lmdbjava/lmdbjava) [![GitHub stars](https://img.shields.io/github/stars/lmdbjava/lmdbjava?style=flat)](https://github.com/lmdbjava/lmdbjava/stargazers) - Java API to LMDB (JNR) which is an ultra-fast, ultra-compact key-value embedded data store written in C.
* [low-gc-membuffers](https://github.com/cowtowncoder/low-gc-membuffers) [![GitHub stars](https://img.shields.io/github/stars/cowtowncoder/low-gc-membuffers?style=flat)](https://github.com/cowtowncoder/low-gc-membuffers/stargazers) - In-memory circular buffers that use direct ByteBuffers to minimize GC overhead.
* [lwjgl3](https://github.com/LWJGL/lwjgl3) [![GitHub stars](https://img.shields.io/github/stars/LWJGL/lwjgl3?style=flat)](https://github.com/LWJGL/lwjgl3/stargazers) - Java library that enables cross-platform access to popular native APIs useful in the development of graphics (OpenGL), audio (OpenAL) and parallel computing (OpenCL) applications.
* [MapDB](http://www.mapdb.org) - Collections backed by off-heap or on-disk storage.
* [mph-table](https://github.com/indeedeng/mph-table) [![GitHub stars](https://img.shields.io/github/stars/indeedeng/mph-table?style=flat)](https://github.com/indeedeng/mph-table/stargazers) - Minimal Perfect Hash Tables are an immutable key/value store with efficient space utilization and fast reads.
* [mug](https://google.github.io/mug/) - A small, zero-dep functional util library originating from Google. 
* [netty-buffers](http://netty.io/wiki/using-as-a-generic-library.html#wiki-h2-1) - Memory buffer pool implementation similar to jemalloc.
* [ObjectLayout](http://objectlayout.org) - A layout-optimized Java data structure package.
* [ohc](https://github.com/snazy/ohc) [![GitHub stars](https://img.shields.io/github/stars/snazy/ohc?style=flat)](https://github.com/snazy/ohc/stargazers) - Java large off heap cache developed for Apache Cassandra 3.0.
* [okio](https://github.com/square/okio) [![GitHub stars](https://img.shields.io/github/stars/square/okio?style=flat)](https://github.com/square/okio/stargazers) - Modern Java IO library that do clever things to save CPU and memory.
* [onyx-java](https://github.com/onyx-platform/onyx-java) [![GitHub stars](https://img.shields.io/github/stars/onyx-platform/onyx-java?style=flat)](https://github.com/onyx-platform/onyx-java/stargazers) - Mirrors the Onyx Platform core API by providing a Java equivalent for each component of an Onyx workflow.
* [parquet](https://parquet.apache.org/) - Columnar storage format that uses the record shredding and assembly algorithm described in the Dremel paper.
* [PauselessHashMap](https://github.com/giltene/PauselessHashMap) [![GitHub stars](https://img.shields.io/github/stars/giltene/PauselessHashMap?style=flat)](https://github.com/giltene/PauselessHashMap/stargazers) - A java.util.HashMap compatible map that won't stall puts or gets when resizing.
* [pcollections](https://github.com/hrldcpr/pcollections) [![GitHub stars](https://img.shields.io/github/stars/hrldcpr/pcollections?style=flat)](https://github.com/hrldcpr/pcollections/stargazers) - A Persistent Java Collections Library.
* [protobuf](https://developers.google.com/protocol-buffers) - Google's data interchange format.
* [Quasar](http://www.paralleluniverse.co/quasar/) - Lightweight threads and actors for the JVM.
* [rtree](https://github.com/davidmoten/rtree) [![GitHub stars](https://img.shields.io/github/stars/davidmoten/rtree?style=flat)](https://github.com/davidmoten/rtree/stargazers) - Immutable in-memory R-tree and R*-tree implementations in Java with reactive api.
* [RTree2D](https://github.com/Sizmek/rtree2d) [![GitHub stars](https://img.shields.io/github/stars/Sizmek/rtree2d?style=flat)](https://github.com/Sizmek/rtree2d/stargazers) - RTree2D is a 2D immutable R-tree with STR (Sort-Tile-Recursive) packing for ultra-fast nearest and intersection queries on plane and spherical surfaces.
* [Reactive Streams](http://www.reactive-streams.org/) - Standard for asynchronous stream processing with non-blocking back pressure.
* [Reactive Streams Utilities](https://github.com/lightbend/reactive-streams-utils) [![GitHub stars](https://img.shields.io/github/stars/lightbend/reactive-streams-utils?style=flat)](https://github.com/lightbend/reactive-streams-utils/stargazers) - Future standard utilities library for Reactive Streams.
* [RoaringBitmap](https://github.com/RoaringBitmap/RoaringBitmap) [![GitHub stars](https://img.shields.io/github/stars/RoaringBitmap/RoaringBitmap?style=flat)](https://github.com/RoaringBitmap/RoaringBitmap/stargazers) - A better compressed bitset in Java.
* [rollinghashjava](https://github.com/lemire/rollinghashjava) [![GitHub stars](https://img.shields.io/github/stars/lemire/rollinghashjava?style=flat)](https://github.com/lemire/rollinghashjava/stargazers) - Rolling hash functions in Java.
* [Reactor](http://projectreactor.io/) - Reactive data applications on the JVM for Java, Groovy, Clojure and other.
* [RxJava](https://github.com/ReactiveX/RxJava) [![GitHub stars](https://img.shields.io/github/stars/ReactiveX/RxJava?style=flat)](https://github.com/ReactiveX/RxJava/stargazers) - Library for composing asynchronous and event-based programs using observable sequences.
* [SmoothieMap](https://github.com/OpenHFT/SmoothieMap) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/SmoothieMap?style=flat)](https://github.com/OpenHFT/SmoothieMap/stargazers) - java.util.Map impl with worst put latencies more than 100 times smaller than java.util.HashMap.
* [Simple Binary Encoding](https://github.com/real-logic/simple-binary-encoding) [![GitHub stars](https://img.shields.io/github/stars/real-logic/simple-binary-encoding?style=flat)](https://github.com/real-logic/simple-binary-encoding/stargazers) - High Performance Message Codec.
* [splitmap](https://github.com/richardstartin/splitmap/) [![GitHub stars](https://img.shields.io/github/stars/richardstartin/splitmap/?style=flat)](https://github.com/richardstartin/splitmap//stargazers) - A parallel bitmap implementation.
* [DataSketches](https://datasketches.github.io/) - A Java software library of stochastic streaming algorithms.
* [stormpot](https://github.com/chrisvest/stormpot) [![GitHub stars](https://img.shields.io/github/stars/chrisvest/stormpot?style=flat)](https://github.com/chrisvest/stormpot/stargazers) - A fast object pool for the JVM.
* [stream-lib](https://github.com/addthis/stream-lib) [![GitHub stars](https://img.shields.io/github/stars/addthis/stream-lib?style=flat)](https://github.com/addthis/stream-lib/stargazers) - A Java library for summarizing data in streams for which it is infeasible to store all events.
* [streamvbyte](https://github.com/lemire/streamvbyte) [![GitHub stars](https://img.shields.io/github/stars/lemire/streamvbyte?style=flat)](https://github.com/lemire/streamvbyte/stargazers) - Fast integer compression in C using the StreamVByte codec.
* [TraneIO](http://trane.io/) - High-performance implementation of the Future abstraction.
* [transducers-java](https://github.com/cognitect-labs/transducers-java) [![GitHub stars](https://img.shields.io/github/stars/cognitect-labs/transducers-java?style=flat)](https://github.com/cognitect-labs/transducers-java/stargazers) - Composable algorithmic transformations independent from the context of their input and output sources.
* [VarInt](https://github.com/bazelbuild/bazel/blob/master/src/main/java/com/google/devtools/build/lib/util/VarInt.java) [![GitHub stars](https://img.shields.io/github/stars/bazelbuild/bazel/blob/master/src/main/java/com/google/devtools/build/lib/util/VarInt.java?style=flat)](https://github.com/bazelbuild/bazel/blob/master/src/main/java/com/google/devtools/build/lib/util/VarInt.java/stargazers) - No-deps variable int implementation without deps (by Bazel).
* [vavr](http://www.vavr.io/) - Functional Library for Java 8+.
* [wire](https://github.com/square/wire) [![GitHub stars](https://img.shields.io/github/stars/square/wire?style=flat)](https://github.com/square/wire/stargazers) - Clean, lightweight protocol buffers for Android and Java.
* [Zero-Allocation-Hashing](https://github.com/OpenHFT/Zero-Allocation-Hashing) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/Zero-Allocation-Hashing?style=flat)](https://github.com/OpenHFT/Zero-Allocation-Hashing/stargazers) - Hashing any sequences of bytes in Java, including all kinds of primitive arrays, buffers, CharSequences and more.

## Metaprogramming

*Parsers, interpreters, compilers and source generation targeted for the JVM.*

* [Antlr](http://www.antlr.org/) - Parser generator for reading, processing, executing, or translating structured text or binary files.
* [auto](https://github.com/google/auto) [![GitHub stars](https://img.shields.io/github/stars/google/auto?style=flat)](https://github.com/google/auto/stargazers) - A collection of source code generators for Java.
* [Apache Calcite](http://calcite.apache.org/docs/) - Dynamic data management framework and SQL parser plugin.
* [Checker Framework](http://types.cs.washington.edu/checker-framework/) - Compiler plug-ins that find bugs or verify their absence.
* [compile-testing](https://github.com/google/compile-testing) [![GitHub stars](https://img.shields.io/github/stars/google/compile-testing?style=flat)](https://github.com/google/compile-testing/stargazers) - Testing tools for javac and annotation processors.
* [derive4j](https://github.com/derive4j/derive4j) [![GitHub stars](https://img.shields.io/github/stars/derive4j/derive4j?style=flat)](https://github.com/derive4j/derive4j/stargazers) - Algebraic data types constructors, pattern-matching, morphisms, optics and typeclasses.
* [error-prone](https://github.com/google/error-prone) [![GitHub stars](https://img.shields.io/github/stars/google/error-prone?style=flat)](https://github.com/google/error-prone/stargazers) - Catch common Java mistakes as compile-time errors.
* [GHCVM](https://github.com/rahulmutt/ghcvm) [![GitHub stars](https://img.shields.io/github/stars/rahulmutt/ghcvm?style=flat)](https://github.com/rahulmutt/ghcvm/stargazers) - A Haskell to JVM compiler that supports GHC Haskell.
* [Graal](http://openjdk.java.net/projects/graal/) - New experimental just-in-time compiler for Java that is integrated with the HotSpot virtual machine.
* [grappa](https://github.com/fge/grappa) [![GitHub stars](https://img.shields.io/github/stars/fge/grappa?style=flat)](https://github.com/fge/grappa/stargazers) - Java fork of Parboiled. Write grammars with no preprocessing phase.
* [immutables](http://immutables.github.io/) - Generate simple, safe and consistent value objects.
* [javacc](https://javacc.java.net/) - Parser generator for use with Java.
* [javaparser](https://github.com/javaparser/javaparser) [![GitHub stars](https://img.shields.io/github/stars/javaparser/javaparser?style=flat)](https://github.com/javaparser/javaparser/stargazers) - Java 1.8 Parser and Abstract Syntax Tree for Java.
* [JavaPoet](https://github.com/square/javapoet) [![GitHub stars](https://img.shields.io/github/stars/square/javapoet?style=flat)](https://github.com/square/javapoet/stargazers) - A Java API for generating .java source files.
* [jparsec](https://github.com/jparsec/jparsec) [![GitHub stars](https://img.shields.io/github/stars/jparsec/jparsec?style=flat)](https://github.com/jparsec/jparsec/stargazers) - Builds mini parsers in pure Java a la Haskell Parsec.
* [JSweet](http://www.jsweet.org/) - A transpiler from Java to TypeScript/JavaScript.
* [MPS](https://www.jetbrains.com/mps/) - Design and build extensible DSLs and editors.
* [lombok](https://projectlombok.org/) - Reduce the amount of boilerplate code that is commonly written for Java classes.
* [parboiled](https://github.com/sirthias/parboiled) [![GitHub stars](https://img.shields.io/github/stars/sirthias/parboiled?style=flat)](https://github.com/sirthias/parboiled/stargazers) - Parsing of arbitrary input text based on parsing expression grammars.
* [Sulong](https://github.com/graalvm/sulong) [![GitHub stars](https://img.shields.io/github/stars/graalvm/sulong?style=flat)](https://github.com/graalvm/sulong/stargazers) - LLVM IR interpreter written in Java using Truffle and Graal.
* [TeaVM](https://github.com/konsoletyper/teavm) [![GitHub stars](https://img.shields.io/github/stars/konsoletyper/teavm?style=flat)](https://github.com/konsoletyper/teavm/stargazers) - Ahead-of-time translating compiler (transpiler) from Java bytecode to JavaScript.
* [Truffle](https://github.com/graalvm/truffle) [![GitHub stars](https://img.shields.io/github/stars/graalvm/truffle?style=flat)](https://github.com/graalvm/truffle/stargazers) - Framework for implementing languages as simple interpreters.
* [Xtext](https://eclipse.org/Xtext/) - Framework for development of programming languages and DSLs.

## Native

*Interconnecting JVM and native code* 

* [hawtjni](https://github.com/fusesource/hawtjni) [![GitHub stars](https://img.shields.io/github/stars/fusesource/hawtjni?style=flat)](https://github.com/fusesource/hawtjni/stargazers) - A JNI code generator based on the JNI generator used in Eclipse SWT.
* [Java Grinder](https://github.com/mikeakohn/java_grinder) [![GitHub stars](https://img.shields.io/github/stars/mikeakohn/java_grinder?style=flat)](https://github.com/mikeakohn/java_grinder/stargazers) - Compile Java bytecode to microcontroller assembly.
* [j2v8](https://github.com/eclipsesource/j2v8) [![GitHub stars](https://img.shields.io/github/stars/eclipsesource/j2v8?style=flat)](https://github.com/eclipsesource/j2v8/stargazers) - Java API for Google's V8 JavaScript engine.
* [JavaCPP](https://github.com/bytedeco/javacpp) [![GitHub stars](https://img.shields.io/github/stars/bytedeco/javacpp?style=flat)](https://github.com/bytedeco/javacpp/stargazers) - JavaCPP provides efficient access to native C++ inside Java.
* [jnr-ffi](https://github.com/jnr/jnr-ffi) [![GitHub stars](https://img.shields.io/github/stars/jnr/jnr-ffi?style=flat)](https://github.com/jnr/jnr-ffi/stargazers) - Load native libraries without writing JNI code by hand.
* [jssembly](https://github.com/dvx/jssembly) [![GitHub stars](https://img.shields.io/github/stars/dvx/jssembly?style=flat)](https://github.com/dvx/jssembly/stargazers) - Execution of native assembly from Java.
* [NuProcess](https://github.com/brettwooldridge/NuProcess) [![GitHub stars](https://img.shields.io/github/stars/brettwooldridge/NuProcess?style=flat)](https://github.com/brettwooldridge/NuProcess/stargazers) - A low-overhead, non-blocking I/O, external Process execution implementation for Java.
* [Project Panama](http://openjdk.java.net/projects/panama/) - Enriching the connections between the JVM and APIs used by C programmers.

## Network

*Tools for network programming, packet capture, monitoring, testing and resiliency.*

* [Aeron](https://github.com/real-logic/Aeron) [![GitHub stars](https://img.shields.io/github/stars/real-logic/Aeron?style=flat)](https://github.com/real-logic/Aeron/stargazers) - Efficient reliable UDP unicast, UDP multicast, and IPC message transport.
* [armeria](https://github.com/line/armeria) [![GitHub stars](https://img.shields.io/github/stars/line/armeria?style=flat)](https://github.com/line/armeria/stargazers) - Asynchronous RPC/API client/server library built on top of Java 8, Netty 4.1, HTTP/2, and Thrift.
* [Chronicle-Network](https://github.com/OpenHFT/Chronicle-Network) [![GitHub stars](https://img.shields.io/github/stars/OpenHFT/Chronicle-Network?style=flat)](https://github.com/OpenHFT/Chronicle-Network/stargazers) - A High Performance Network library.
* [comcast](https://github.com/tylertreat/comcast) [![GitHub stars](https://img.shields.io/github/stars/tylertreat/comcast?style=flat)](https://github.com/tylertreat/comcast/stargazers) - Simulating shitty network connections.
* [gor](https://github.com/buger/gor) [![GitHub stars](https://img.shields.io/github/stars/buger/gor?style=flat)](https://github.com/buger/gor/stargazers) - HTTP traffic replay in real-time.
* [gRPC](http://www.grpc.io/) - A high performance, open source, general RPC framework that puts mobile and HTTP/2 first.
* [jRT](https://github.com/LatencyUtils/jRT) [![GitHub stars](https://img.shields.io/github/stars/LatencyUtils/jRT?style=flat)](https://github.com/LatencyUtils/jRT/stargazers) - Measures response time of a java application to socket-based requests.
* [JXIO](https://github.com/accelio/JXIO) [![GitHub stars](https://img.shields.io/github/stars/accelio/JXIO?style=flat)](https://github.com/accelio/JXIO/stargazers) - Java API over AccelIO (C library), a high-performance asynchronous reliable messaging and RPC library optimized for hardware acceleration.
* [K3PO](https://github.com/k3po/k3po) [![GitHub stars](https://img.shields.io/github/stars/k3po/k3po?style=flat)](https://github.com/k3po/k3po/stargazers) - Create arbitrary network traffic and behavior to certify whether a network endpoint behaves correctly.
* [muxy](https://github.com/mefellows/muxy) [![GitHub stars](https://img.shields.io/github/stars/mefellows/muxy?style=flat)](https://github.com/mefellows/muxy/stargazers) - Simulating real-world distributed system failures.
* [Netty](http://netty.io/) - Async event-driven network library for high performance protocol servers & clients.
* [okhttp](https://github.com/square/okhttp) [![GitHub stars](https://img.shields.io/github/stars/square/okhttp?style=flat)](https://github.com/square/okhttp/stargazers) - An HTTP+HTTP/2 client for Android and Java applications.
* [one-nio](https://github.com/odnoklassniki/one-nio) [![GitHub stars](https://img.shields.io/github/stars/odnoklassniki/one-nio?style=flat)](https://github.com/odnoklassniki/one-nio/stargazers) - library for building high performance Java servers.
* [proteus-java](https://github.com/netifi-proteus/proteus-java) [![GitHub stars](https://img.shields.io/github/stars/netifi-proteus/proteus-java?style=flat)](https://github.com/netifi-proteus/proteus-java/stargazers) - Proteus Java Client based on RSocket.
* [reactive-grpc](https://github.com/salesforce/reactive-grpc) [![GitHub stars](https://img.shields.io/github/stars/salesforce/reactive-grpc?style=flat)](https://github.com/salesforce/reactive-grpc/stargazers) - Reactive gRPC is a suite of libraries for using gRPC with Reactive Streams programming libraries.
* [RSocket](http://rsocket.io/) - RSocket is a binary protocol for use on byte stream transports such as TCP, WebSockets, and Aeron.
* [SimianArmy](https://github.com/Netflix/SimianArmy) [![GitHub stars](https://img.shields.io/github/stars/Netflix/SimianArmy?style=flat)](https://github.com/Netflix/SimianArmy/stargazers) - Resiliency tool that helps ensure that your applications can tolerate random instance failures.
* [pcap4j](https://github.com/kaitoy/pcap4j) [![GitHub stars](https://img.shields.io/github/stars/kaitoy/pcap4j?style=flat)](https://github.com/kaitoy/pcap4j/stargazers) - Java library for capturing, crafting, and sending packets using libpcap.
* [pig](https://github.com/rafael-santiago/pig) [![GitHub stars](https://img.shields.io/github/stars/rafael-santiago/pig?style=flat)](https://github.com/rafael-santiago/pig/stargazers) - A Linux packet crafting tool.
* [tcpdump](http://www.tcpdump.org/) - Packet analyzer for network traffic capture.
* [tcpflow](https://github.com/simsong/tcpflow) [![GitHub stars](https://img.shields.io/github/stars/simsong/tcpflow?style=flat)](https://github.com/simsong/tcpflow/stargazers) - Captures TCP connections flows in a way that is convenient for protocol analysis and debugging.
* [tcpreplay](https://github.com/appneta/tcpreplay) [![GitHub stars](https://img.shields.io/github/stars/appneta/tcpreplay?style=flat)](https://github.com/appneta/tcpreplay/stargazers) - Pcap editing and replay tools.

## Nix tools

*Useful *nix tools when profiling the JVM and interaction with the host environment*
* [atoptool](http://www.atoptool.nl/) - Logging of system and process activity for long-term analysis, highlighting overloaded system.
* [bcc](https://github.com/iovisor/bcc) [![GitHub stars](https://img.shields.io/github/stars/iovisor/bcc?style=flat)](https://github.com/iovisor/bcc/stargazers) - Tools for BPF-based Linux IO analysis, networking, monitoring, and more.
* [Flame Graphs](http://www.brendangregg.com/flamegraphs.html) - Visualization of profiled software, allowing the most frequent code-paths to be identified quickly and accurately.
* [ioping](https://github.com/koct9i/ioping) [![GitHub stars](https://img.shields.io/github/stars/koct9i/ioping?style=flat)](https://github.com/koct9i/ioping/stargazers) - Simple disk I/0 latency measuring tool.
* [javap](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/javap.html) - Disassembles class files into code that reflects the java bytecode.
* [jhat](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html) - Java Heap Analysis Tool
* [jhsdb](https://docs.oracle.com/javase/9/tools/jhsdb.htm) - Launch a postmortem debugger to analyze the content of a core-dump from a crashed JVM.
* [jinfo](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jinfo.html) - Prints configuration information for a given process.
* [jstack](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstack.html) - Prints stack traces of threads for a given Java process.
* [jstat](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html) - Monitors GC and compiler statistics in the JVM.
* [hwloc](http://linux.die.net/man/7/hwloc) - Reports the structure of the processor, number of cores, hyperthreads and cache size.
* [likwid](https://github.com/RRZE-HPC/likwid) [![GitHub stars](https://img.shields.io/github/stars/RRZE-HPC/likwid?style=flat)](https://github.com/RRZE-HPC/likwid/stargazers) - Read hardware performance counters on Intel and AMD processors.
* [numactl](http://linux.die.net/man/8/numactl) - Control NUMA policy for processes or shared memory.
* [oprofile](http://oprofile.sourceforge.net/news/) - System-wide hardware performance monitoring with easy-to-use interface at low overhead.
* [perf](https://perf.wiki.kernel.org/index.php/Main_Page) - Linux profiling with performance counters.
* [perf-tools](https://github.com/brendangregg/perf-tools) [![GitHub stars](https://img.shields.io/github/stars/brendangregg/perf-tools?style=flat)](https://github.com/brendangregg/perf-tools/stargazers) - Performance analysis tools based on Linux perf_events (aka perf) and ftrace.
* [sysdig](http://www.sysdig.org/) - Capture system state and activity from a running Linux instance, then save, filter and analyze.
* [sysstat](http://sebastien.godard.pagesperso-orange.fr) - Performance monitoring tools for Linux.
* [taskset/process-affinity](https://www.glennklockwood.com/hpc-howtos/process-affinity.html) - Retrieve or set a processes’s CPU affinity.
* [tiptop](http://tiptop.gforge.inria.fr/) - Like top but also shows instructions per cycle (IPC).

## Profilers

*Tools that provide profiling and tracing information to aid program optimization*

* [allocation-instrumenter](https://github.com/google/allocation-instrumenter) [![GitHub stars](https://img.shields.io/github/stars/google/allocation-instrumenter?style=flat)](https://github.com/google/allocation-instrumenter/stargazers) - Java agent that rewrites bytecode to instrument allocation sites.
* [aprof](https://github.com/Devexperts/aprof) [![GitHub stars](https://img.shields.io/github/stars/Devexperts/aprof?style=flat)](https://github.com/Devexperts/aprof/stargazers) - Java memory allocation profiler.
* [async-profiler](https://github.com/jvm-profiling-tools/async-profiler) [![GitHub stars](https://img.shields.io/github/stars/jvm-profiling-tools/async-profiler?style=flat)](https://github.com/jvm-profiling-tools/async-profiler/stargazers) - Sampling CPU profiler for Java featuring AsyncGetCallTrace + perf_events.
* [BTrace](https://github.com/jbachorik/btrace) [![GitHub stars](https://img.shields.io/github/stars/jbachorik/btrace?style=flat)](https://github.com/jbachorik/btrace/stargazers) - a safe, dynamic tracing tool for the Java platform.
* [Byteman](http://byteman.jboss.org/) - tracing, monitoring and testing tool for Java
* [bytestacks](https://github.com/cl4es/bytestacks) [![GitHub stars](https://img.shields.io/github/stars/cl4es/bytestacks?style=flat)](https://github.com/cl4es/bytestacks/stargazers) - Turn JVM bytecode execution into flame graphs. 
* [Chronon](http://chrononsystems.com) - Record your entire java program. Replay on any machine.
* [GCeasy](http://gceasy.io/) - Machine learning guided Garbage collection log analysis tool. Auto-detect problems in the JVM GC logs and recommend solutions to it.
* [GCViewer](https://github.com/chewiebug/GCViewer) [![GitHub stars](https://img.shields.io/github/stars/chewiebug/GCViewer?style=flat)](https://github.com/chewiebug/GCViewer/stargazers) - GCViewer is a tool that visualizes verbose GC output.
* [grav](https://github.com/epickrram/grav) [![GitHub stars](https://img.shields.io/github/stars/epickrram/grav?style=flat)](https://github.com/epickrram/grav/stargazers) - A collection of tools to help visualise process execution.
* [hawkshaw](https://github.com/jClarity/hawkshaw) [![GitHub stars](https://img.shields.io/github/stars/jClarity/hawkshaw?style=flat)](https://github.com/jClarity/hawkshaw/stargazers) - Tools for tracking down memory / JVM problems & generating predictable-as-possible VM behaviour.
* [HdrHistogram](http://hdrhistogram.github.io/HdrHistogram/) - A Histogram that supports recording and analyzing sampled data value counts.
* [hdrhistogram-metrics-reservoir](https://bitbucket.org/marshallpierce/hdrhistogram-metrics-reservoir) - A Metrics Reservoir implementation backed by HdrHistogram.
* [HdrLogProcessing](https://github.com/nitsanw/HdrLogProcessing) [![GitHub stars](https://img.shields.io/github/stars/nitsanw/HdrLogProcessing?style=flat)](https://github.com/nitsanw/HdrLogProcessing/stargazers) - Utilities for HDR Histogram logs manipulation.
* [heapster](https://github.com/mariusae/heapster) [![GitHub stars](https://img.shields.io/github/stars/mariusae/heapster?style=flat)](https://github.com/mariusae/heapster/stargazers) - Production heap profiling for the JVM.
* [honest-profiler](https://github.com/RichardWarburton/honest-profiler) [![GitHub stars](https://img.shields.io/github/stars/RichardWarburton/honest-profiler?style=flat)](https://github.com/RichardWarburton/honest-profiler/stargazers) - Sampling JVM profiler without the safepoint sample bias.
* [jamm](https://github.com/jbellis/jamm) [![GitHub stars](https://img.shields.io/github/stars/jbellis/jamm?style=flat)](https://github.com/jbellis/jamm/stargazers) - Measure actual object memory use including JVM overhead.
* [Java Flight Recorder (JFR)](http://www.oracle.com/technetwork/java/javaseproducts/mission-control/java-mission-control-1998576.html) - Tool for collecting diagnostic and profiling data about a running Java application with almost no performance overhead.
* [java-sizeof](https://github.com/dweiss/java-sizeof) [![GitHub stars](https://img.shields.io/github/stars/dweiss/java-sizeof?style=flat)](https://github.com/dweiss/java-sizeof/stargazers) - Memory consumption estimator for Java.
* [jcstress](http://openjdk.java.net/projects/code-tools/jcstress/) - Experimental harness and tests to aid the research in the correctness of concurrency support in the JVM, class libraries, and hardware.
* [jfr-flame-graph](https://github.com/chrishantha/jfr-flame-graph) [![GitHub stars](https://img.shields.io/github/stars/chrishantha/jfr-flame-graph?style=flat)](https://github.com/chrishantha/jfr-flame-graph/stargazers) - Converting JFR Method Profiling Samples to FlameGraph compatible format.
* [jfr-report-tool](https://github.com/lhotari/jfr-report-tool) [![GitHub stars](https://img.shields.io/github/stars/lhotari/jfr-report-tool?style=flat)](https://github.com/lhotari/jfr-report-tool/stargazers) - Tool for creating reports from Java Flight Recorder dumps.
* [jitwatch](https://github.com/AdoptOpenJDK/jitwatch) [![GitHub stars](https://img.shields.io/github/stars/AdoptOpenJDK/jitwatch?style=flat)](https://github.com/AdoptOpenJDK/jitwatch/stargazers) - Log analyser / visualiser for Java HotSpot JIT compiler.
* [jitwatch-intellij](https://github.com/yole/jitwatch-intellij) [![GitHub stars](https://img.shields.io/github/stars/yole/jitwatch-intellij?style=flat)](https://github.com/yole/jitwatch-intellij/stargazers) - JITWatch plugin for IntelliJ IDEA.
* [jHiccup](http://www.azul.com/jhiccup/) - jHiccup is an open source tool designed to measure the pauses and stalls associated with an application’s underlying Java runtime platform.
* [jmh](http://openjdk.java.net/projects/code-tools/jmh/) - Micro benchmarks written in Java and other languages targetting the JVM.
* [jmh-compare-gui](https://github.com/akarnokd/jmh-compare-gui) [![GitHub stars](https://img.shields.io/github/stars/akarnokd/jmh-compare-gui?style=flat)](https://github.com/akarnokd/jmh-compare-gui/stargazers) - GUI for comparing JMH results.
* [JOL](http://openjdk.java.net/projects/code-tools/jol/) - Analyze actual object layout schemes, footprint, and references in JVMs.
* [JProfiler](https://www.ej-technologies.com/products/jprofiler/overview.html) - Helps resolve performance bottlenecks, pin down memory leaks and understand threading issues.
* [JVMTI](https://docs.oracle.com/javase/8/docs/technotes/guides/jvmti/) - Provide a native API to inspect the state and to control the execution of applications running in the JVM.
* [jvmtop](https://github.com/patric-r/jvmtop) [![GitHub stars](https://img.shields.io/github/stars/patric-r/jvmtop?style=flat)](https://github.com/patric-r/jvmtop/stargazers) - Lightweight console application to monitor running jvms on a machine in top-like manner.
* [jvm-profiler](https://github.com/uber-common/jvm-profiler) [![GitHub stars](https://img.shields.io/github/stars/uber-common/jvm-profiler?style=flat)](https://github.com/uber-common/jvm-profiler/stargazers) - Java Agent to collect various metrics and stacktraces for Hadoop/Spark JVM processes in a distributed way.
* [MAT](https://eclipse.org/mat/) - Java heap analyzer that help find memory leaks and reduce memory consumption.
* [leakcanary](https://github.com/square/leakcanary) [![GitHub stars](https://img.shields.io/github/stars/square/leakcanary?style=flat)](https://github.com/square/leakcanary/stargazers) - A memory leak detection library for Android and Java.
* [metrics](http://metrics.dropwizard.io/) - Measure the behavior of critical components in production environment.
* [micrometer](https://github.com/micrometer-metrics/micrometer) [![GitHub stars](https://img.shields.io/github/stars/micrometer-metrics/micrometer?style=flat)](https://github.com/micrometer-metrics/micrometer/stargazers) - An application metrics facade for the most popular monitoring tools.
* [osquery](https://osquery.io/) - osquery is an instrumentation framework that expose the operating system as a high-performance relational database.
* [Overseer](http://www.peternier.com/projects/overseer/overseer.php) - Low-Level Hardware Monitoring and Management for Java.
* [OpenTracing](http://opentracing.io/) - A vendor-neutral open standard for distributed tracing.
* [perf-map-agent](https://github.com/jrudolph/perf-map-agent) [![GitHub stars](https://img.shields.io/github/stars/jrudolph/perf-map-agent?style=flat)](https://github.com/jrudolph/perf-map-agent/stargazers) - Generate method mappings to use with the linux `perf` tool.
* [perfj](https://github.com/coderplay/perfj) [![GitHub stars](https://img.shields.io/github/stars/coderplay/perfj?style=flat)](https://github.com/coderplay/perfj/stargazers) - Linux perf for java programs.
* [polarbear](https://github.com/Cue/polarbear) [![GitHub stars](https://img.shields.io/github/stars/Cue/polarbear?style=flat)](https://github.com/Cue/polarbear/stargazers) - A tool to help diagnose OutOfMemoryError conditions.
* [Riemann JVM Profiler](https://github.com/riemann/riemann-jvm-profiler) [![GitHub stars](https://img.shields.io/github/stars/riemann/riemann-jvm-profiler?style=flat)](https://github.com/riemann/riemann-jvm-profiler/stargazers) - JVM agent which sends function-level profiler telemetry to a Riemann server for analysis, visualization, and storage.
* [statsd-jvm-profiler](https://github.com/etsy/statsd-jvm-profiler) [![GitHub stars](https://img.shields.io/github/stars/etsy/statsd-jvm-profiler?style=flat)](https://github.com/etsy/statsd-jvm-profiler/stargazers) - JVM agent profiler that sends profiling data to StatsD.
* [Swiss Java Knife](https://github.com/aragozin/jvm-tools) [![GitHub stars](https://img.shields.io/github/stars/aragozin/jvm-tools?style=flat)](https://github.com/aragozin/jvm-tools/stargazers) - Small set of tools for JVM troublshooting, monitoring and profiling.
* [Takipi](https://www.takipi.com/) - Tells you when and why code breaks in production.
* [Tracer](https://github.com/zalando/tracer) [![GitHub stars](https://img.shields.io/github/stars/zalando/tracer?style=flat)](https://github.com/zalando/tracer/stargazers) - Manages custom trace identifiers and carries them through distributed systems.
* [YourKit](https://www.yourkit.com/) - Fully featured, easy to use, low overhead profiler.
* [Zipkin](https://github.com/openzipkin/zipkin) [![GitHub stars](https://img.shields.io/github/stars/openzipkin/zipkin?style=flat)](https://github.com/openzipkin/zipkin/stargazers) - A distributed tracing system gather timing data for disparate services developed by Twitter.


## Runtimes

*Tools for managing jvm runtime processes*
* [Capsule](https://github.com/puniverse/capsule) [![GitHub stars](https://img.shields.io/github/stars/puniverse/capsule?style=flat)](https://github.com/puniverse/capsule/stargazers) - Dead-Simple Packaging and Deployment for JVM Apps.
* [CRaSH](http://www.crashub.org/) - The shell for the Java Platform.
* [Drip](https://github.com/ninjudd/drip) [![GitHub stars](https://img.shields.io/github/stars/ninjudd/drip?style=flat)](https://github.com/ninjudd/drip/stargazers) - Fast JVM launching without the hassle of persistent JVMs.
* [HotswapAgent](https://github.com/HotswapProjects/HotswapAgent) [![GitHub stars](https://img.shields.io/github/stars/HotswapProjects/HotswapAgent?style=flat)](https://github.com/HotswapProjects/HotswapAgent/stargazers) - Redefine classes at runtime and skip the redeploy process.
* [jvmkill](https://github.com/airlift/jvmkill) [![GitHub stars](https://img.shields.io/github/stars/airlift/jvmkill?style=flat)](https://github.com/airlift/jvmkill/stargazers) - Agent that forcibly terminates the JVM when it is unable to allocate memory or create a thread.
* [Nailgun](http://martiansoftware.com/nailgun/) - Nailgun is a client, protocol, and server for running Java programs from the command line without incurring the JVM startup overhead.

## Virtual Machines

*Virtual machines that implement the JVM specification or parts of it.*
* [Avian](https://github.com/ReadyTalk/avian) [![GitHub stars](https://img.shields.io/github/stars/ReadyTalk/avian?style=flat)](https://github.com/ReadyTalk/avian/stargazers) - Lightweight highly portable JVM with an option for AOT compilation.
* [Dalvik](https://source.android.com/devices/tech/dalvik/) - Android runtime (ART) is the managed runtime used by applications and some system services on Android.
* [DCEVM](http://dcevm.github.io) - Modification of Java HotSwap VM with unlimited support for reloading classes at runtime.
* [HotSpot](http://openjdk.java.net/groups/hotspot/) - HotSpot virtual machine maintained and distributed by Oracle Corporation.
* [IBM J9](http://www.ibm.com/developerworks/java/jdk/) - JVM developed by IBM.
* [Eclipse OpenJ9](https://github.com/eclipse/openj9) [![GitHub stars](https://img.shields.io/github/stars/eclipse/openj9?style=flat)](https://github.com/eclipse/openj9/stargazers) - Eclipse OpenJ9.
* [J2ObjC](https://github.com/google/j2objc) [![GitHub stars](https://img.shields.io/github/stars/google/j2objc?style=flat)](https://github.com/google/j2objc/stargazers) - Translator from Java source to Objective-C code. Keeps shared code between iOS native apps and Android native apps. 
* [jvm.go](https://github.com/zxh0/jvm.go) [![GitHub stars](https://img.shields.io/github/stars/zxh0/jvm.go?style=flat)](https://github.com/zxh0/jvm.go/stargazers) - A JVM written in Go.
* [ParparVM](https://github.com/codenameone/CodenameOne/tree/master/vm) [![GitHub stars](https://img.shields.io/github/stars/codenameone/CodenameOne/tree/master/vm?style=flat)](https://github.com/codenameone/CodenameOne/tree/master/vm/stargazers) - An Open Source Java bytecode to C translator for iOS native development. Designed as a part of the [Codename One](https://www.codenameone.com/) WORA for mobile project.
* [MobiDevelop's RoboVM Fork](https://github.com/MobiVM/robovm) [![GitHub stars](https://img.shields.io/github/stars/MobiVM/robovm?style=flat)](https://github.com/MobiVM/robovm/stargazers) - Ahead of time compiler for JVM bytecode targeting iOS, Mac OSX and Linux.
* [Zing](https://www.azul.com/products/zing/) - The only JVM that eliminates Java garbage collection pauses for large heap sizes.
* [Zulu](https://www.azul.com/products/zulu/) - The only certified multi-platform build of OpenJDK: Free, 100% open source Java.

# Resources

## Documentation

*Documentation related to JVM*
* [TCP Tracepoints](http://www.brendangregg.com/blog/2018-03-22/tcp-tracepoints.html) Linux bcc/BPF using tcplife by Brendan Gregg
* [Linux tracing workshop](https://github.com/goldshtn/linux-tracing-workshop) [![GitHub stars](https://img.shields.io/github/stars/goldshtn/linux-tracing-workshop?style=flat)](https://github.com/goldshtn/linux-tracing-workshop/stargazers) - JVM monitoring with BPF, examples and hands-on labs for Linux tracing tools workshops.
* [JVM Anatomy Park](https://shipilev.net/jvm-anatomy-park/) - mini-post series where every post goes deep for only a single topic by Aleksey Shipilёv.
* [Coordinated Omission problem](https://groups.google.com/forum/#!msg/mechanical-sympathy/icNZJejUHfE/BfDekfBEs_sJ) - Discussion on Mechanical Sympathy.
* [False sharing](http://mechanical-sympathy.blogspot.se/2011/07/false-sharing.html) - Threads impact the performance of each other while modifying independent variables sharing the same cache line. Martin Thompson.
* [The JVM specification](https://docs.oracle.com/javase/specs/jvms/se8/jvms8.pdf) - The Java Virtual
Machine Specification Java SE 8 Edition.
* [The Java Memory Model](http://www.cs.umd.edu/~pugh/java/memoryModel/) - Starting point for discussions of and information concerning the Java Memory Model.
* [The JSR-133 Cookbook for Compiler Writers](http://gee.cs.oswego.edu/dl/jmm/cookbook.html) - Unofficial guide to implementing the new Java Memory Model (JMM) specified by JSR-133.
* [Garbage Collection Tuning Guide](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/) - HotSpot Virtual Machine Garbage Collection Tuning Guide.
* [Safepoints](http://psy-lob-saw.blogspot.se/2014/03/where-is-my-safepoint.html) - Where is my safepoint? Nitsan Wakart.
* [Topics in High-Performance Messaging](https://www.informatica.com/downloads/1568_high_perf_messaging_wp/Topics-in-High-Performance-Messaging.htm) - Design decisions, experience and constraints explained in high performance messaging systems.
* [Top 10 Performance Mistakes](http://www.infoq.com/articles/top-10-performance-mistakes) - Digest of the top 10 performance related mistakes Martin Thompson has seen in production.
* [The USE method](http://www.brendangregg.com/usemethod.html) - The Utilization Saturation and Errors (USE) Method is a methodology for analyzing the performance of any system. Brendan Gregg.
* [An introduction to distributed systems](https://github.com/aphyr/distsys-class) [![GitHub stars](https://img.shields.io/github/stars/aphyr/distsys-class?style=flat)](https://github.com/aphyr/distsys-class/stargazers) - Kyle Kingsbury (author of Jepsen).
* [Using JDK 9 Memory Order Modes](http://gee.cs.oswego.edu/dl/html/j9mm.html) - For expert programmers familiar with Java concurrency, but unfamiliar with the memory order modes available in JDK 9 provided by VarHandles.
* [CPU Utilization is Wrong](http://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html) - Measure instructions per cycle (IPC) for CPU utilization. Brendan Gregg.
* [Linux Load Averages: Solving the Mystery](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html) - Brendan Gregg.
* [What every programmer should know about solid-state drives](http://codecapsule.com/2014/02/12/coding-for-ssds-part-6-a-summary-what-every-programmer-should-know-about-solid-state-drives/) - Emmanuel Goossaert.
* [Quick Tips for Fast Code on the JVM](https://gist.github.com/djspiewak/464c11307cabc80171c90397d4ec34ef) - Daniel Spiewak.
## Communities

*Active discussions.*

* [concurrency-interest](http://altair.cs.oswego.edu/mailman/listinfo/concurrency-interest) - Discussion list for JSR-166.
* [hotspot-compiler-dev](http://mail.openjdk.java.net/mailman/listinfo/hotspot-compiler-dev) - Technical discussion about the development of the HotSpot bytecode compilers.
* [hotspot-dev](http://mail.openjdk.java.net/mailman/listinfo/hotspot-dev) - HotSpot development mailing list.
* [hotspot-gc-dev](http://mail.openjdk.java.net/mailman/listinfo/hotspot-gc-dev) - Technical discussion about the development of the HotSpot garbage collectors.
* [mechanical-sympathy](https://groups.google.com/forum/#!forum/mechanical-sympathy) - Discussing how to code sympathetically to and measure the underlying stack/platform so good performance can be extracted.
* [Performance Java User's Group](https://plus.google.com/u/0/communities/107178245817384004088/) - For expert Java *developers* who want to push their systems to the next level
* [Virtual Machine Meetup 2017](http://vmmeetup.github.io/2017/) - Venue for discussing the latest research and developments in the area of managed language execution. 

## Media

*Videos, podcasts and other media related to JVMs*
* [FOSDEM 2018](https://fosdem.org/2018/schedule/track/free_java/) - FOSDEM 2018 Free Java devroom.
* [JFokus 2018](https://www.youtube.com/playlist?list=PL2ekzZZrxVUkhrcMKuPMbiKoghc777plr) - The GC edition. Shenandoah, ZGC, Zing, Fibers, Falcon etc.
* [G1 Garbage Collector in Java 8/9](http://nighthacking.com/g1-gc-with-kirk-pepperdine/) - Kirk Pepperdine.
* [Extreme Profiling: Digging Into Hotspots](https://youtu.be/7PkkxDaFDj8?list=PLKuh52zVrL6l6jzeSwNce77yLdfKmHAgD) - Nitsan Wakart.
* [Java vs. C Performance](http://www.infoq.com/presentations/java-vs-c-performance) - Cliff Click.
* [Why JNI is slow?](https://www.youtube.com/watch?v=LoyBTqkSkZk) - Cliff Click
* [A Crash Course in Modern Hardware](https://www.youtube.com/watch?v=OFgxAFdxYAQ) - Cliff Click
* [Java Profiling from the Ground Up](https://www.youtube.com/watch?v=_6vJyciXkwo) - Nitsan Wakart.
* [The Illusion of Execution](https://www.youtube.com/watch?v=3g9R-RVIkOE) - Nitsan Wakart.
* [Mythbusting Modern Hardware to Gain 'Mechanical Sympathy'](https://www.youtube.com/watch?v=MC1EKLQ2Wmg) - Martin Thompson.
* [Designing for Performance](https://www.youtube.com/watch?v=fDGWWpHlzvw) - Martin Thompson.
* [How NOT to Measure Latency](https://www.youtube.com/watch?v=lJ8ydIuPFeU) - Gil Tene.
* [JVM Language Summit 2015](http://openjdk.java.net/projects/mlvm/jvmlangsummit/) - JVM Language Summit 2015.
* [JVM Language Summit 2016](https://www.youtube.com/playlist?list=PLX8CzqL3ArzUY6rQAQTwI_jKvqJxrRrP_) - JVM Language Summit 2016.
* [JVM Language Summit 2017](https://www.youtube.com/playlist?list=PLX8CzqL3ArzXJ2EGftrmz4SzS6NRr6p2n) - JVM Language Summit 2017.
* [Bits of advice for VM writers](https://www.youtube.com/watch?v=vzzABBxo44g) - Cliff Click.
* [Understanding Java garbage collection ...](https://www.youtube.com/watch?v=_e5hujoTkgY) - Gil Tene.
* [Faster Object Arrays](https://www.youtube.com/watch?v=bZuPTCaciLU) - Gil Tene at GOTO Conferences.
* [Java Memory Model Pragmatics](https://www.youtube.com/watch?v=TxqsKzxyySo) - Aleksey Shipilev.
* [With GC Solved, What Else Makes a JVM Pause?](https://www.youtube.com/watch?v=Y39kllzX1P8) - John Cuthbertson.
* [JVM Mechanics](https://vimeo.com/120533011) - Douglas Hawkins.
* [Give me 15 minutes and I'll change your view of Linux tracing](https://www.youtube.com/watch?v=GsMs3n8CB6g) - Brendan Gregg.
* [Kernel Recipes 2017: Performance Analysis with BPF](https://www.slideshare.net/brendangregg/kernel-recipes-2017-performance-analysis-with-bpf) - Brendan Gregg.
* [Shenandoah deep talk](https://shipilev.net/talks/vmm-Sep2017-shenandoah.pdf) - Aleksey Shipilëv slightly-deeper-than-usual Shenandoah talk from Virtual Machine Meetup 2017.
* [Shenandoah: The Garbage Collector That Could](https://www.youtube.com/watch?v=VCeHkcwfF9Q) - Aleksey Shipilev - Devoxx 2017/11
* [Analyzing and Debugging the Java HotSpot VM at the OS Level](https://www.youtube.com/watch?v=k7IX_diKCEo) - Volker Simonis.
* [Cliff Click podcast 2017/09/16](http://www.cliffc.org/blog/2017/09/16/programming-and-performance-intro/) - Programming and Performance Intro.
* [Cliff Click podcast 2017/09/16](http://www.cliffc.org/blog/2017/09/16/of-bugs-and-coding-styles/) - Bugs and Coding Styles.
* [Cliff Click podcast 2017/09/18](http://www.cliffc.org/blog/2017/09/18/java-vs-cc-the-podcast/) - Java vs C/C++.
* [Cliff Click podcast 2017/09/21](http://www.cliffc.org/blog/2017/09/21/debugging-data-races/) - Debugging Data Races.
* [Cliff Click podcast 2017/09/24](http://www.cliffc.org/blog/2017/09/24/fast-bytecodes-for-funny-languages/) - Fast Bytecodes for Funny Languages.
* [Cliff Click podcast 2017/09/28](http://www.cliffc.org/blog/2017/09/28/struct-of-arrays-vs-array-of-structs/) - Struct of Arrays vs Array of Structs.
* [Cliff Click podcast 2017/10/04](http://www.cliffc.org/blog/2017/10/04/the-3-hardest-problems-in-programming/) - The 3 Hardest Problems in Programming.
* [Cliff Click podcast 2017/11/05](http://cliffc.org/blog/2017/11/05/modern-hardware-performance-cache-lines/) - Modern Hardware Performance and Cache Lines.
* [Cliff Click podcast 2017/11/09](http://cliffc.org/blog/2017/11/09/queuing-in-practice/) - Queuing In Practice.
* [Which technique do programming language parsers and interpreters use?](https://www.quora.com/Which-technique-do-programming-language-parsers-and-interpreters-use/answer/Cliff-Click-1?srid=dZAx) - Cliff Click.
* [Everything about Stack Traces and Heap Dumps](https://vimeo.com/233820012) - Andrei Pangin.
* [Fast and safe production monitoring of JVM with BPF tools](http://s.sashag.net/velny17-jvm) - Sasha Goldshtein.
* [The Future of the Linux Page Cache](https://www.youtube.com/watch?time_continue=1&v=xxWaa-lPR-8) - Matthew Wilcox.

## People

*People that share hard-earned, often undocumented, knowledge and data of the inner workings of the JVM*
* [Aleksey Shipilëv](http://shipilev.net/) - Developing Oracle/Open JDK/Hotspot and other Java-related technologies.
* [Andrey Breslav](https://twitter.com/abreslav) - Lead Language Designer of Kotlin @ JetBrains.
* [Brian Goetz](https://twitter.com/BrianGoetz) - Java Language Architect at Oracle.
* [Ben Christensen](https://twitter.com/benjchristensen) - Facebook, Netflix, Apple engineering.
* [Brendan Gregg](http://www.brendangregg.com) - Cloud performance, kernel engineer, speaker, author.
* [Charles Nutter](https://twitter.com/headius) - JRuby guy.
* [Claes Redestad](https://twitter.com/cl4es) - Working with OpenJDK stuff @ Oracle.
* [Cliff Click](http://www.cliffc.org/blog/) - Creator of the HotSpot Server Compiler.
* [Dave Dice](https://blogs.oracle.com/dave/) - Senior research scientist in the Scalable Synchronization Research Group within Oracle.
* [Dávid Karnok](http://akarnokd.blogspot.se/) - RxJava committer that blogs about advanced RxJava.
* [Doug Lea](http://g.oswego.edu/) - Author of the Java memory model.
* [Gil Tene](https://twitter.com/giltene) - Azul Systems.
* [Heinz Kabutz](https://twitter.com/heinzkabutz) - Author of 250+ Java Specialists' Newsletters.
* [Ivan Krylov](https://twitter.com/JohnWings) - JVM expert.
* [Jake Wharton](https://twitter.com/JakeWharton) - Square, Google, open source hacker.
* [John Rose](https://blogs.oracle.com/jrose/) - HotSpot developer.
* [Jonas Bonér](https://twitter.com/jboner) - Founder & CTO of Lightbend.
* [Lukas Eder](https://twitter.com/lukaseder) - Blogger. Author of JOOQ.
* [Marcus Lagergren](https://twitter.com/lagergren) - Java language team alumnus.
* [Mark Reinhold](https://twitter.com/mreinhold) - Chief Architect, Java Platform Group, Oracle.
* [Martin Thompson](http://mechanical-sympathy.blogspot.se/) - Pasty faced performance gangster.
* [Martijn Verburg](https://twitter.com/karianna) - Java Champion.
* [Kirk Pepperdine](https://twitter.com/javaperftuning) - Working in high performance and distributed computing for nearly 20 years.
* [Nitsan Wakart](http://psy-lob-saw.blogspot.se/2014/03/where-is-my-safepoint.html) - Azul Systems.
* [Norman Maurer](https://twitter.com/normanmaurer) - Netty developer.
* [Paul Phillips](https://twitter.com/contrarivariant) - Forever undisputed SLOC Scala compiler dev.
* [Per Liden](https://twitter.com/perliden) - Hacking on the HotSpot JVM at Oracle.
* [Peter Lawrey](https://twitter.com/PeterLawrey) - Innovative developer of high performance Java systems for competitive advantage.
* [Rafael Winterhalter](https://twitter.com/rafaelcodes) - Author of ByteBuddy.
* [Richard Warburton](https://twitter.com/RichardWarburto) - Developer, Speaker, Author.
* [Richard Startin](http://richardstartin.uk/) - Performance Analyst, developer, blogger.
* [Ron Pressler](https://twitter.com/pressron) - Parallel Universe. Leading Fibers and Continuations for the JVM.
* [Stephen Colebourne](https://twitter.com/jodastephen) - Java Champion. Occasional blogger and speaker. Best known for Joda projects and JSR-310.
* [Todd L. Montgomery](https://twitter.com/toddlmontgomery) - Ex-CTO, Ex-NASA researcher, network geek, messaging middleware designer.
* [Stéphane Maldini](https://twitter.com/smaldini) - Project Reactor Lead @Pivotal.
* [Stuart Marks](https://twitter.com/stuartmarks) - Doctor Deprecator. Java/JDK/OpenJDK developer 
* [Vladimir Ivanov](https://twitter.com/iwan0www) - hacking HotSpot JVM @ Oracle.
* [Viktor Klang](https://twitter.com/viktorklang) - Deputy CTO at Typesafe Inc.


# Contributing

Contributions are very welcome!

Please have a look at [contributing.md](https://github.com/deephacks/awesome-jvm/blob/master/contributing.md) [![GitHub stars](https://img.shields.io/github/stars/deephacks/awesome-jvm/blob/master/contributing.md?style=flat)](https://github.com/deephacks/awesome-jvm/blob/master/contributing.md/stargazers) for guidelines.
