# Coq

[![GitHub stars](https://img.shields.io/github/stars/coq-community/awesome-coq?style=flat)](https://github.com/coq-community/awesome-coq/stargazers)

# Awesome Coq [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="coq-logo.svg" align="right" width="100" alt="coq-community logo" title="Awesome Coq is a coq-community project">](https://github.com/coq-community/manifesto) [![GitHub stars](https://img.shields.io/github/stars/coq-community/manifesto?style=flat)](https://github.com/coq-community/manifesto/stargazers)

> A curated list of awesome Coq libraries, plugins, tools, and resources.

The [Coq proof assistant](https://coq.inria.fr) provides a formal language to write mathematical definitions, executable algorithms, and theorems, together with an environment for semi-interactive development of machine-checked proofs.

Contributions welcome! Read the [contribution guidelines](https://github.com/coq-community/awesome-coq/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/coq-community/awesome-coq/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/coq-community/awesome-coq/blob/master/CONTRIBUTING.md/stargazers) first.

## Contents

- [Projects](#projects)
  - [Frameworks](#frameworks)
  - [User Interfaces](#user-interfaces)
  - [Libraries](#libraries)
  - [Package and Build Management](#package-and-build-management)
  - [Plugins](#plugins)
  - [Puzzles and Games](#puzzles-and-games)
  - [Tools](#tools)
  - [Type Theory and Mathematics](#type-theory-and-mathematics)
  - [Verified Software](#verified-software)
- [Resources](#resources)
  - [Community](#community)
  - [Blogs](#blogs)
  - [Books](#books)
  - [Course Material](#course-material)
  - [Tutorials and Hints](#tutorials-and-hints)

---

## Projects

### Frameworks

- [ConCert](https://github.com/AU-COBRA/ConCert) [![GitHub stars](https://img.shields.io/github/stars/AU-COBRA/ConCert?style=flat)](https://github.com/AU-COBRA/ConCert/stargazers) - Framework for smart contract testing and verification featuring a code extraction pipeline to several smart contract languages.
- [CoqEAL](https://github.com/CoqEAL/CoqEAL) [![GitHub stars](https://img.shields.io/github/stars/CoqEAL/CoqEAL?style=flat)](https://github.com/CoqEAL/CoqEAL/stargazers) - Framework to ease change of data representations in proofs.
- [FCF](https://github.com/adampetcher/fcf) [![GitHub stars](https://img.shields.io/github/stars/adampetcher/fcf?style=flat)](https://github.com/adampetcher/fcf/stargazers) - Framework for proofs of cryptography.
- [Fiat](https://github.com/mit-plv/fiat) [![GitHub stars](https://img.shields.io/github/stars/mit-plv/fiat?style=flat)](https://github.com/mit-plv/fiat/stargazers) - Mostly automated synthesis of correct-by-construction programs.
- [FreeSpec](https://github.com/lthms/FreeSpec) [![GitHub stars](https://img.shields.io/github/stars/lthms/FreeSpec?style=flat)](https://github.com/lthms/FreeSpec/stargazers) - Framework for modularly verifying programs with effects and effect handlers.
- [Hoare Type Theory](https://github.com/imdea-software/htt/) [![GitHub stars](https://img.shields.io/github/stars/imdea-software/htt/?style=flat)](https://github.com/imdea-software/htt//stargazers) - A shallow embedding of sequential separation logic formulated as a type theory.
- [Hybrid](https://www.site.uottawa.ca/~afelty/HybridCoq/) - System for reasoning using higher-order abstract syntax representations of object logics.
- [Iris](https://iris-project.org) - Higher-order concurrent separation logic framework.
- [Q\*cert](https://github.com/querycert/qcert) [![GitHub stars](https://img.shields.io/github/stars/querycert/qcert?style=flat)](https://github.com/querycert/qcert/stargazers) - Platform for implementing and verifying query compilers.
- [SSProve](https://github.com/SSProve/ssprove) [![GitHub stars](https://img.shields.io/github/stars/SSProve/ssprove?style=flat)](https://github.com/SSProve/ssprove/stargazers) - Framework for modular cryptographic proofs based on the Mathematical Components library.
- [VCFloat](https://github.com/VeriNum/vcfloat) [![GitHub stars](https://img.shields.io/github/stars/VeriNum/vcfloat?style=flat)](https://github.com/VeriNum/vcfloat/stargazers) - Framework for verifying C programs with floating-point computations.
- [Verdi](https://github.com/uwplse/verdi) [![GitHub stars](https://img.shields.io/github/stars/uwplse/verdi?style=flat)](https://github.com/uwplse/verdi/stargazers) - Framework for formally verifying distributed systems implementations.
- [VST](https://vst.cs.princeton.edu) - Toolchain for verifying C code inside Coq in a higher-order concurrent, impredicative separation logic that is sound w.r.t. the Clight language of the CompCert compiler.

### User Interfaces

- [CoqIDE](https://coq.inria.fr/refman/practical-tools/coqide.html) - Standalone graphical tool for interacting with Coq.
- [Coqtail](https://github.com/whonore/Coqtail) [![GitHub stars](https://img.shields.io/github/stars/whonore/Coqtail?style=flat)](https://github.com/whonore/Coqtail/stargazers) - Interface for Coq based on the Vim text editor.
- [Coq LSP](https://github.com/ejgallego/coq-lsp) [![GitHub stars](https://img.shields.io/github/stars/ejgallego/coq-lsp?style=flat)](https://github.com/ejgallego/coq-lsp/stargazers) - Language server and extension for the Visual Studio Code and VSCodium editors with custom document checking engine.
- [Proof General](https://proofgeneral.github.io) - Generic interface for proof assistants based on the extensible, customizable text editor Emacs.
- [Company-Coq](https://github.com/cpitclaudel/company-coq) [![GitHub stars](https://img.shields.io/github/stars/cpitclaudel/company-coq?style=flat)](https://github.com/cpitclaudel/company-coq/stargazers) - IDE extensions for Proof General's Coq mode.
- [opam-switch-mode](https://github.com/ProofGeneral/opam-switch-mode) [![GitHub stars](https://img.shields.io/github/stars/ProofGeneral/opam-switch-mode?style=flat)](https://github.com/ProofGeneral/opam-switch-mode/stargazers) - IDE extension for Proof General to locally change or reset the opam switch from a menu or using a command.
- [jsCoq](https://github.com/jscoq/jscoq) [![GitHub stars](https://img.shields.io/github/stars/jscoq/jscoq?style=flat)](https://github.com/jscoq/jscoq/stargazers) - Port of Coq to JavaScript, which enables running Coq projects in a browser.
- [Jupyter kernel for Coq](https://github.com/EugeneLoy/coq_jupyter) [![GitHub stars](https://img.shields.io/github/stars/EugeneLoy/coq_jupyter?style=flat)](https://github.com/EugeneLoy/coq_jupyter/stargazers) - Coq support for the Jupyter Notebook web environment.
- [VsCoq](https://github.com/coq-community/vscoq) [![GitHub stars](https://img.shields.io/github/stars/coq-community/vscoq?style=flat)](https://github.com/coq-community/vscoq/stargazers) - Language server and extension for the Visual Studio Code and VSCodium editors.
- [VsCoq Legacy](https://github.com/coq-community/vscoq/tree/vscoq1) [![GitHub stars](https://img.shields.io/github/stars/coq-community/vscoq/tree/vscoq1?style=flat)](https://github.com/coq-community/vscoq/tree/vscoq1/stargazers) - Backwards-compatible extension for the Visual Studio Code and VSCodium editors using Coq's legacy XML protocol.
- [Waterproof editor](https://github.com/impermeable/waterproof) [![GitHub stars](https://img.shields.io/github/stars/impermeable/waterproof?style=flat)](https://github.com/impermeable/waterproof/stargazers) - Educational environment for writing mathematical proofs in interactive notebooks.
- [Tree Sitter Rocq](https://github.com/lamg/tree-sitter-rocq) [![GitHub stars](https://img.shields.io/github/stars/lamg/tree-sitter-rocq?style=flat)](https://github.com/lamg/tree-sitter-rocq/stargazers) - Partial Rocq tree-sitter grammar useful for syntax highlighting in text editors like [Helix](https://github.com/helix-editor/helix) [![GitHub stars](https://img.shields.io/github/stars/helix-editor/helix?style=flat)](https://github.com/helix-editor/helix/stargazers), but not recommended for full parsing of Rocq code.

### Libraries

- [ALEA](https://github.com/coq-community/alea) [![GitHub stars](https://img.shields.io/github/stars/coq-community/alea?style=flat)](https://github.com/coq-community/alea/stargazers) - Library for reasoning on randomized algorithms.
- [Algebra Tactics](https://github.com/math-comp/algebra-tactics) [![GitHub stars](https://img.shields.io/github/stars/math-comp/algebra-tactics?style=flat)](https://github.com/math-comp/algebra-tactics/stargazers) - Ring and field tactics for Mathematical Components.
- [Bignums](https://github.com/coq/bignums) [![GitHub stars](https://img.shields.io/github/stars/coq/bignums?style=flat)](https://github.com/coq/bignums/stargazers) - Library of arbitrarily large numbers.
- [Bedrock Bit Vectors](https://github.com/mit-plv/bbv) [![GitHub stars](https://img.shields.io/github/stars/mit-plv/bbv?style=flat)](https://github.com/mit-plv/bbv/stargazers) - Library for reasoning on fixed precision machine words.
- [CertiGraph](https://github.com/Salamari/CertiGraph) [![GitHub stars](https://img.shields.io/github/stars/Salamari/CertiGraph?style=flat)](https://github.com/Salamari/CertiGraph/stargazers) - Library for reasoning about directed graphs and their embedding in separation logic.
- [CoLoR](https://github.com/fblanqui/color) [![GitHub stars](https://img.shields.io/github/stars/fblanqui/color?style=flat)](https://github.com/fblanqui/color/stargazers) - Library on rewriting theory, lambda-calculus and termination, with sub-libraries on common data structures extending the Coq standard library.
- [coq-haskell](https://github.com/jwiegley/coq-haskell) [![GitHub stars](https://img.shields.io/github/stars/jwiegley/coq-haskell?style=flat)](https://github.com/jwiegley/coq-haskell/stargazers) - Library smoothing the transition to Coq for Haskell users.
- [Coq-Kruskal](https://github.com/DmxLarchey/Coq-Kruskal) [![GitHub stars](https://img.shields.io/github/stars/DmxLarchey/Coq-Kruskal?style=flat)](https://github.com/DmxLarchey/Coq-Kruskal/stargazers) - Collection of libraries related to rose trees and Kruskal's tree theorem.
- [CoqInterval](https://gitlab.inria.fr/coqinterval/interval/) - Tactics for performing proofs of inequalities on expressions of real numbers.
- [Coq record update](https://github.com/tchajed/coq-record-update) [![GitHub stars](https://img.shields.io/github/stars/tchajed/coq-record-update?style=flat)](https://github.com/tchajed/coq-record-update/stargazers) - Library which provides a generic way to update Coq record fields.
- [Coq-std++](https://gitlab.mpi-sws.org/iris/stdpp) - Extended alternative standard library for Coq.
- [ExtLib](https://github.com/coq-community/coq-ext-lib) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coq-ext-lib?style=flat)](https://github.com/coq-community/coq-ext-lib/stargazers) - Collection of theories and plugins that may be useful in other Coq developments.
- [FCSL-PCM](https://github.com/imdea-software/fcsl-pcm) [![GitHub stars](https://img.shields.io/github/stars/imdea-software/fcsl-pcm?style=flat)](https://github.com/imdea-software/fcsl-pcm/stargazers) - Formalization of partial commutative monoids as used in verification of pointer-manipulating programs.
- [Flocq](https://gitlab.inria.fr/flocq/flocq) - Formalization of floating-point numbers and computations.
- [Formalised Undecidable Problems](https://github.com/uds-psl/coq-library-undecidability) [![GitHub stars](https://img.shields.io/github/stars/uds-psl/coq-library-undecidability?style=flat)](https://github.com/uds-psl/coq-library-undecidability/stargazers) - Library of undecidable problems and reductions between them.
- [Hahn](https://github.com/vafeiadis/hahn) [![GitHub stars](https://img.shields.io/github/stars/vafeiadis/hahn?style=flat)](https://github.com/vafeiadis/hahn/stargazers) - Library for reasoning on lists and binary relations.
- [Interaction Trees](https://github.com/DeepSpec/InteractionTrees) [![GitHub stars](https://img.shields.io/github/stars/DeepSpec/InteractionTrees?style=flat)](https://github.com/DeepSpec/InteractionTrees/stargazers) - Library for representing recursive and impure programs.
- [LibHyps](https://github.com/Matafou/LibHyps) [![GitHub stars](https://img.shields.io/github/stars/Matafou/LibHyps?style=flat)](https://github.com/Matafou/LibHyps/stargazers) - Library of Ltac tactics to manage and manipulate hypotheses in proofs.
- [MathComp Extra](https://github.com/thery/mathcomp-extra) [![GitHub stars](https://img.shields.io/github/stars/thery/mathcomp-extra?style=flat)](https://github.com/thery/mathcomp-extra/stargazers) - Extra material for the Mathematical Components library, including the AKS primality test and RSA encryption and decryption.
- [Mczify](https://github.com/math-comp/mczify) [![GitHub stars](https://img.shields.io/github/stars/math-comp/mczify?style=flat)](https://github.com/math-comp/mczify/stargazers) - Library enabling Micromega arithmetic solvers to work when using Mathematical Components number definitions.
- [Metalib](https://github.com/plclub/metalib) [![GitHub stars](https://img.shields.io/github/stars/plclub/metalib?style=flat)](https://github.com/plclub/metalib/stargazers) - Library for programming language metatheory using locally nameless variable binding representations.
- [Paco](http://plv.mpi-sws.org/paco/) - Library for parameterized coinduction.
- [Regular Language Representations](https://github.com/coq-community/reglang) [![GitHub stars](https://img.shields.io/github/stars/coq-community/reglang?style=flat)](https://github.com/coq-community/reglang/stargazers) - Translations between different definitions of regular languages, including regular expressions and automata.
- [Relation Algebra](https://github.com/damien-pous/relation-algebra) [![GitHub stars](https://img.shields.io/github/stars/damien-pous/relation-algebra?style=flat)](https://github.com/damien-pous/relation-algebra/stargazers) - Modular formalization of algebras with heterogeneous binary relations as models.
- [Simple IO](https://github.com/Lysxia/coq-simple-io) [![GitHub stars](https://img.shields.io/github/stars/Lysxia/coq-simple-io?style=flat)](https://github.com/Lysxia/coq-simple-io/stargazers) - Input/output monad with user-definable primitive operations.
- [TLC](https://github.com/charguer/tlc) [![GitHub stars](https://img.shields.io/github/stars/charguer/tlc?style=flat)](https://github.com/charguer/tlc/stargazers) - Non-constructive alternative to Coq's standard library.

### Package and Build Management

- [coq_makefile](https://coq.inria.fr/refman/practical-tools/utilities.html) - Build tool distributed with Coq and based on generating a makefile.
- [Coq Nix Toolbox](https://github.com/coq-community/coq-nix-toolbox) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coq-nix-toolbox?style=flat)](https://github.com/coq-community/coq-nix-toolbox/stargazers) - Nix helper scripts to automate local builds and continuous integration for Coq.
- [Coq Package Index](https://coq.inria.fr/opam/www/) - Collection of Coq packages based on opam.
- [Coq Platform](https://github.com/coq/platform) [![GitHub stars](https://img.shields.io/github/stars/coq/platform?style=flat)](https://github.com/coq/platform/stargazers) - Curated collection of packages to support Coq use in industry, education, and research.
- [coq-community Templates](https://github.com/coq-community/templates) [![GitHub stars](https://img.shields.io/github/stars/coq-community/templates?style=flat)](https://github.com/coq-community/templates/stargazers) - Templates for generating configuration files for Coq projects.
- [Debian Coq packages](https://people.debian.org/~jpuydt/coq_platform.html) - Coq-related packages available in the testing distribution of Debian.
- [Docker-Coq](https://github.com/coq-community/docker-coq) [![GitHub stars](https://img.shields.io/github/stars/coq-community/docker-coq?style=flat)](https://github.com/coq-community/docker-coq/stargazers) - Docker images for many versions of Coq.
- [Docker-MathComp](https://github.com/math-comp/docker-mathcomp) [![GitHub stars](https://img.shields.io/github/stars/math-comp/docker-mathcomp?style=flat)](https://github.com/math-comp/docker-mathcomp/stargazers) - Docker images for many combinations of versions of Coq and the Mathematical Components library.
- [Docker-Coq GitHub Action](https://github.com/marketplace/actions/docker-coq-action) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/docker-coq-action?style=flat)](https://github.com/marketplace/actions/docker-coq-action/stargazers) - GitHub container action that can be used with Docker-Coq or Docker-MathComp.
- [Dune](https://dune.build) - Composable and opinionated build system for OCaml and Coq (former jbuilder).
- [Nix](https://nixos.org/nix/) - Package manager for Linux and other Unix systems, supporting atomic upgrades and rollbacks.
- [Nix Coq packages](https://search.nixos.org/packages?channel=unstable&query=coqPackages) - Collection of Coq-related packages for Nix.
- [opam](https://opam.ocaml.org) - Flexible and Git-friendly package manager for OCaml and Coq with multiple compiler support.

### Plugins

- [AAC Tactics](https://github.com/coq-community/aac-tactics) [![GitHub stars](https://img.shields.io/github/stars/coq-community/aac-tactics?style=flat)](https://github.com/coq-community/aac-tactics/stargazers) - Tactics for rewriting universally quantified equations, modulo associativity and commutativity of some operator.
- [Coinduction](https://github.com/damien-pous/coinduction) [![GitHub stars](https://img.shields.io/github/stars/damien-pous/coinduction?style=flat)](https://github.com/damien-pous/coinduction/stargazers) - Plugin for doing proofs by enhanced coinduction.
- [Coq-Elpi](https://github.com/LPCIC/coq-elpi) [![GitHub stars](https://img.shields.io/github/stars/LPCIC/coq-elpi?style=flat)](https://github.com/LPCIC/coq-elpi/stargazers) - Extension framework based on λProlog providing an extensive API to implement commands and tactics.
- [CoqHammer](https://github.com/lukaszcz/coqhammer) [![GitHub stars](https://img.shields.io/github/stars/lukaszcz/coqhammer?style=flat)](https://github.com/lukaszcz/coqhammer/stargazers) - General-purpose automated reasoning hammer tool that combines learning from previous proofs with the translation of problems to automated provers and the reconstruction of found proofs.
- [Equations](https://github.com/mattam82/Coq-Equations) [![GitHub stars](https://img.shields.io/github/stars/mattam82/Coq-Equations?style=flat)](https://github.com/mattam82/Coq-Equations/stargazers) - Function definition package for Coq.
- [Gappa](https://gitlab.inria.fr/gappa/coq) - Tactic for discharging goals about floating-point arithmetic and round-off errors.
- [Hierarchy Builder](https://github.com/math-comp/hierarchy-builder) [![GitHub stars](https://img.shields.io/github/stars/math-comp/hierarchy-builder?style=flat)](https://github.com/math-comp/hierarchy-builder/stargazers) - Collection of commands for declaring Coq hierarchies based on packed classes.
- [Itauto](https://gitlab.inria.fr/fbesson/itauto) - SMT-like tactics for combined propositional reasoning about function symbols, constructors, and arithmetic.
- [Ltac2](https://coq.inria.fr/refman/proof-engine/ltac2.html) - Experimental typed tactic language similar to Coq's classic Ltac language.
- [MetaCoq](https://github.com/MetaCoq/metacoq) [![GitHub stars](https://img.shields.io/github/stars/MetaCoq/metacoq?style=flat)](https://github.com/MetaCoq/metacoq/stargazers) - Project formalizing Coq in Coq and providing tools for manipulating Coq terms and developing certified plugins.
- [Mtac2](https://github.com/Mtac2/Mtac2) [![GitHub stars](https://img.shields.io/github/stars/Mtac2/Mtac2?style=flat)](https://github.com/Mtac2/Mtac2/stargazers) - Plugin adding typed tactics for backward reasoning.
- [Paramcoq](https://github.com/coq-community/paramcoq) [![GitHub stars](https://img.shields.io/github/stars/coq-community/paramcoq?style=flat)](https://github.com/coq-community/paramcoq/stargazers) - Plugin to generate parametricity translations of Coq terms.
- [QuickChick](https://github.com/QuickChick/QuickChick) [![GitHub stars](https://img.shields.io/github/stars/QuickChick/QuickChick?style=flat)](https://github.com/QuickChick/QuickChick/stargazers) - Plugin for randomized property-based testing.
- [SMTCoq](https://github.com/smtcoq/smtcoq) [![GitHub stars](https://img.shields.io/github/stars/smtcoq/smtcoq?style=flat)](https://github.com/smtcoq/smtcoq/stargazers) - Tool that checks proof witnesses coming from external SAT and SMT solvers.
- [Tactician](https://coq-tactician.github.io) - Interactive tool which learns from previously written tactic scripts across all the installed Coq packages and suggests the next tactic to be executed or tries to automate proof synthesis fully.
- [Unicoq](https://github.com/unicoq/unicoq) [![GitHub stars](https://img.shields.io/github/stars/unicoq/unicoq?style=flat)](https://github.com/unicoq/unicoq/stargazers) - Plugin that replaces the existing unification algorithm with an enhanced one.
- [Waterproof proof language](https://github.com/impermeable/coq-waterproof) [![GitHub stars](https://img.shields.io/github/stars/impermeable/coq-waterproof?style=flat)](https://github.com/impermeable/coq-waterproof/stargazers) - Plugin providing a language for writing proof scripts in a style that resembles non-mechanized mathematical proof.

### Puzzles and Games

- [Coqoban](https://github.com/coq-community/coqoban) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coqoban?style=flat)](https://github.com/coq-community/coqoban/stargazers) - Coq implementation of Sokoban, the Japanese warehouse keepers' game.
- [Hanoi](https://github.com/thery/hanoi) [![GitHub stars](https://img.shields.io/github/stars/thery/hanoi?style=flat)](https://github.com/thery/hanoi/stargazers) - The Tower of Hanoi puzzle in Coq, including generalizations and theorems about configurations.
- [Mini-Rubik](https://github.com/thery/minirubik) [![GitHub stars](https://img.shields.io/github/stars/thery/minirubik?style=flat)](https://github.com/thery/minirubik/stargazers) - Coq formalization and solver of the 2x2x2 version of the Rubik's Cube puzzle.
- [Name the Biggest Number](https://github.com/codyroux/name-the-biggest-number) [![GitHub stars](https://img.shields.io/github/stars/codyroux/name-the-biggest-number?style=flat)](https://github.com/codyroux/name-the-biggest-number/stargazers) - Repository for submitting proven contenders for the title of biggest number in Coq.
- [Natural Number Game](https://github.com/uncomputable/natural-number-game) [![GitHub stars](https://img.shields.io/github/stars/uncomputable/natural-number-game?style=flat)](https://github.com/uncomputable/natural-number-game/stargazers) - Coq version of the natural number game developed for the Lean prover.
- [Sudoku](https://github.com/coq-community/sudoku) [![GitHub stars](https://img.shields.io/github/stars/coq-community/sudoku?style=flat)](https://github.com/coq-community/sudoku/stargazers) - Formalization and solver of the Sudoku number-placement puzzle in Coq.
- [T2048](https://github.com/thery/T2048) [![GitHub stars](https://img.shields.io/github/stars/thery/T2048?style=flat)](https://github.com/thery/T2048/stargazers) - Coq version of the 2048 sliding tile game.

### Tools

- [Alectryon](https://github.com/cpitclaudel/alectryon) [![GitHub stars](https://img.shields.io/github/stars/cpitclaudel/alectryon?style=flat)](https://github.com/cpitclaudel/alectryon/stargazers) - Collection of tools for writing technical documents that mix Coq code and prose.
- [Autosubst-ocaml](https://github.com/uds-psl/autosubst-ocaml) [![GitHub stars](https://img.shields.io/github/stars/uds-psl/autosubst-ocaml?style=flat)](https://github.com/uds-psl/autosubst-ocaml/stargazers) - Tool that generates Coq code for handling binders in syntax, such as for renaming and substitutions.
- [CFML](https://gitlab.inria.fr/charguer/cfml2) - Tool for proving properties of OCaml programs in separation logic.
- [coq2html](https://github.com/xavierleroy/coq2html) [![GitHub stars](https://img.shields.io/github/stars/xavierleroy/coq2html?style=flat)](https://github.com/xavierleroy/coq2html/stargazers) - Alternative HTML documentation generator for Coq.
- [coqdoc](https://coq.inria.fr/refman/using/tools/coqdoc.html) - Standard documentation tool that generates LaTeX or HTML files from Coq code.
- [CoqOfOCaml](https://github.com/clarus/coq-of-ocaml) [![GitHub stars](https://img.shields.io/github/stars/clarus/coq-of-ocaml?style=flat)](https://github.com/clarus/coq-of-ocaml/stargazers) - Tool for generating idiomatic Coq from OCaml code.
- [coq-dpdgraph](https://github.com/coq-community/coq-dpdgraph) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coq-dpdgraph?style=flat)](https://github.com/coq-community/coq-dpdgraph/stargazers) - Tool for building dependency graphs between Coq objects.
- [coq-scripts](https://github.com/JasonGross/coq-scripts) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-scripts?style=flat)](https://github.com/JasonGross/coq-scripts/stargazers) - Scripts for dealing with Coq files, including tabulating proof times.
- [coq-tools](https://github.com/JasonGross/coq-tools) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools?style=flat)](https://github.com/JasonGross/coq-tools/stargazers) - Scripts for manipulating Coq developments.
  - [`find-bug.py`](https://github.com/JasonGross/coq-tools/blob/master/find-bug.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/find-bug.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/find-bug.py/stargazers) - Automatically minimizes source files producing an error, creating small test cases for Coq bugs.
  - [`absolutize-imports.py`](https://github.com/JasonGross/coq-tools/blob/master/absolutize-imports.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/absolutize-imports.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/absolutize-imports.py/stargazers) - Processes source files to make loading of dependencies robust against shadowing of file names.
  - [`inline-imports.py`](https://github.com/JasonGross/coq-tools/blob/master/inline-imports.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/inline-imports.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/inline-imports.py/stargazers) - Creates stand-alone source files from developments by inlining the loading of all dependencies.
  - [`minimize-requires.py`](https://github.com/JasonGross/coq-tools/blob/master/minimize-requires.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/minimize-requires.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/minimize-requires.py/stargazers) - Removes loading of unused dependencies.
  - [`move-requires.py`](https://github.com/JasonGross/coq-tools/blob/master/move-requires.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/move-requires.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/move-requires.py/stargazers) - Moves all dependency loading statements to the top of source files.
  - [`move-vernaculars.py`](https://github.com/JasonGross/coq-tools/blob/master/move-vernaculars.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/move-vernaculars.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/move-vernaculars.py/stargazers) - Lifts many vernacular commands and inner lemmas out of proof script blocks.
  - [`proof-using-helper.py`](https://github.com/JasonGross/coq-tools/blob/master/proof-using-helper.py) [![GitHub stars](https://img.shields.io/github/stars/JasonGross/coq-tools/blob/master/proof-using-helper.py?style=flat)](https://github.com/JasonGross/coq-tools/blob/master/proof-using-helper.py/stargazers) - Modifies source files to include proof annotations for faster parallel proving.
- [Cosette](https://github.com/uwdb/Cosette) [![GitHub stars](https://img.shields.io/github/stars/uwdb/Cosette?style=flat)](https://github.com/uwdb/Cosette/stargazers) - Automated solver for reasoning about SQL query equivalences.
- [hs-to-coq](https://github.com/plclub/hs-to-coq) [![GitHub stars](https://img.shields.io/github/stars/plclub/hs-to-coq?style=flat)](https://github.com/plclub/hs-to-coq/stargazers) - Converter from Haskell code to equivalent Coq code.
- [lngen](https://github.com/plclub/lngen) [![GitHub stars](https://img.shields.io/github/stars/plclub/lngen?style=flat)](https://github.com/plclub/lngen/stargazers) - Tool for generating locally nameless Coq definitions and proofs.
- [Menhir](http://gallium.inria.fr/~fpottier/menhir/) - Parser generator that can output Coq code for verified parsers.
- [mCoq](https://github.com/EngineeringSoftware/mcoq) [![GitHub stars](https://img.shields.io/github/stars/EngineeringSoftware/mcoq?style=flat)](https://github.com/EngineeringSoftware/mcoq/stargazers) - Mutation analysis tool for Coq projects.
- [Ott](https://github.com/ott-lang/ott) [![GitHub stars](https://img.shields.io/github/stars/ott-lang/ott?style=flat)](https://github.com/ott-lang/ott/stargazers) - Tool for writing definitions of programming languages and calculi that can be translated to Coq.
- [PyCoq](https://github.com/ejgallego/pycoq) [![GitHub stars](https://img.shields.io/github/stars/ejgallego/pycoq?style=flat)](https://github.com/ejgallego/pycoq/stargazers) - Set of bindings and libraries for interacting with Coq from inside Python 3.
- [Rocqnavi](https://github.com/affeldt-aist/rocqnavi) [![GitHub stars](https://img.shields.io/github/stars/affeldt-aist/rocqnavi?style=flat)](https://github.com/affeldt-aist/rocqnavi/stargazers) - Fork of coq2html that adds indexes, clickable notations, Markdown and LaTeX formatting in comments, and more.
- [Roosterize](https://github.com/EngineeringSoftware/roosterize) [![GitHub stars](https://img.shields.io/github/stars/EngineeringSoftware/roosterize?style=flat)](https://github.com/EngineeringSoftware/roosterize/stargazers) - Tool for suggesting lemma names in Coq projects.
- [Sail](https://github.com/rems-project/sail) [![GitHub stars](https://img.shields.io/github/stars/rems-project/sail?style=flat)](https://github.com/rems-project/sail/stargazers) - Tool for specifying instruction set architecture (ISA) semantics of processors and generating Coq definitions.
- [SerAPI](https://github.com/ejgallego/coq-serapi) [![GitHub stars](https://img.shields.io/github/stars/ejgallego/coq-serapi?style=flat)](https://github.com/ejgallego/coq-serapi/stargazers) - Tools and OCaml library for (de)serialization of Coq code to and from JSON and S-expressions.
- [Trakt](https://github.com/ecranceMERCE/trakt) [![GitHub stars](https://img.shields.io/github/stars/ecranceMERCE/trakt?style=flat)](https://github.com/ecranceMERCE/trakt/stargazers) - Generic goal preprocessing tool for proof automation tactics.

### Type Theory and Mathematics

- [Analysis](https://github.com/math-comp/analysis) [![GitHub stars](https://img.shields.io/github/stars/math-comp/analysis?style=flat)](https://github.com/math-comp/analysis/stargazers) - Library for classical real analysis compatible with Mathematical Components.
- [Category Theory in Coq](https://github.com/jwiegley/category-theory) [![GitHub stars](https://img.shields.io/github/stars/jwiegley/category-theory?style=flat)](https://github.com/jwiegley/category-theory/stargazers) - Axiom-free formalization of category theory.
- [Completeness and Decidability of Modal Logic Calculi](https://github.com/coq-community/comp-dec-modal) [![GitHub stars](https://img.shields.io/github/stars/coq-community/comp-dec-modal?style=flat)](https://github.com/coq-community/comp-dec-modal/stargazers) - Soundness, completeness, and decidability for the logics K, K*, CTL, and PDL.
- [CoqPrime](https://github.com/thery/coqprime) [![GitHub stars](https://img.shields.io/github/stars/thery/coqprime?style=flat)](https://github.com/thery/coqprime/stargazers) - Library for certifying primality using Pocklington and Elliptic Curve certificates.
- [CoRN](https://github.com/coq-community/corn) [![GitHub stars](https://img.shields.io/github/stars/coq-community/corn?style=flat)](https://github.com/coq-community/corn/stargazers) - Library of constructive real analysis and algebra.
- [Coqtail Math](https://github.com/coq-community/coqtail-math) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coqtail-math?style=flat)](https://github.com/coq-community/coqtail-math/stargazers) - Library of mathematical results ranging from arithmetic to real and complex analysis.
- [Coquelicot](https://gitlab.inria.fr/coquelicot/coquelicot) - Formalization of classical real analysis compatible with the standard library and focusing on usability.
- [Finmap](https://github.com/math-comp/finmap) [![GitHub stars](https://img.shields.io/github/stars/math-comp/finmap?style=flat)](https://github.com/math-comp/finmap/stargazers) - Extension of Mathematical Components with finite maps, sets, and multisets.
- [Four Color Theorem](https://github.com/coq-community/fourcolor) [![GitHub stars](https://img.shields.io/github/stars/coq-community/fourcolor?style=flat)](https://github.com/coq-community/fourcolor/stargazers) - Formal proof of the Four Color Theorem, a landmark result of graph theory.
- [Gaia](https://github.com/coq-community/gaia) [![GitHub stars](https://img.shields.io/github/stars/coq-community/gaia?style=flat)](https://github.com/coq-community/gaia/stargazers) - Implementation of books from Bourbaki's Elements of Mathematics, including set theory and number theory.
- [GeoCoq](https://github.com/GeoCoq/GeoCoq) [![GitHub stars](https://img.shields.io/github/stars/GeoCoq/GeoCoq?style=flat)](https://github.com/GeoCoq/GeoCoq/stargazers) - Formalization of geometry based on Tarski's axiom system.
- [Graph Theory](https://github.com/coq-community/graph-theory) [![GitHub stars](https://img.shields.io/github/stars/coq-community/graph-theory?style=flat)](https://github.com/coq-community/graph-theory/stargazers) - Formalized graph theory results.
- [Homotopy Type Theory](https://github.com/HoTT/Coq-HoTT) [![GitHub stars](https://img.shields.io/github/stars/HoTT/Coq-HoTT?style=flat)](https://github.com/HoTT/Coq-HoTT/stargazers) - Development of homotopy-theoretic ideas.
- [Infotheo](https://github.com/affeldt-aist/infotheo) [![GitHub stars](https://img.shields.io/github/stars/affeldt-aist/infotheo?style=flat)](https://github.com/affeldt-aist/infotheo/stargazers) - Formalization of information theory and linear error-correcting codes.
- [Mathematical Components](http://math-comp.github.io) - Formalization of mathematical theories, focusing in particular on group theory.
- [Math Classes](https://github.com/coq-community/math-classes) [![GitHub stars](https://img.shields.io/github/stars/coq-community/math-classes?style=flat)](https://github.com/coq-community/math-classes/stargazers) - Abstract interfaces for mathematical structures based on type classes.
- [Monae](https://github.com/affeldt-aist/monae) [![GitHub stars](https://img.shields.io/github/stars/affeldt-aist/monae?style=flat)](https://github.com/affeldt-aist/monae/stargazers) - Monadic effects and equational reasoning.
- [Odd Order Theorem](https://github.com/math-comp/odd-order) [![GitHub stars](https://img.shields.io/github/stars/math-comp/odd-order?style=flat)](https://github.com/math-comp/odd-order/stargazers) - Formal proof of the Odd Order Theorem, a landmark result of finite group theory.
- [Puiseuxth](https://github.com/roglo/puiseuxth) [![GitHub stars](https://img.shields.io/github/stars/roglo/puiseuxth?style=flat)](https://github.com/roglo/puiseuxth/stargazers) - Proof of Puiseux's theorem and computation of roots of polynomials of Puiseux's series.
- [UniMath](https://github.com/UniMath/UniMath) [![GitHub stars](https://img.shields.io/github/stars/UniMath/UniMath?style=flat)](https://github.com/UniMath/UniMath/stargazers) - Library which aims to formalize a substantial body of mathematics using the univalent point of view.

### Verified Software

- [CompCert](http://compcert.inria.fr) - High-assurance compiler for almost all of the C language (ISO C99), generating efficient code for the PowerPC, ARM, RISC-V and x86 processors.
- [Ceramist](https://github.com/certichain/ceramist) [![GitHub stars](https://img.shields.io/github/stars/certichain/ceramist?style=flat)](https://github.com/certichain/ceramist/stargazers) - Verified hash-based approximate membership structures such as Bloom filters.
- [CertiCoq](https://github.com/CertiCoq/certicoq) [![GitHub stars](https://img.shields.io/github/stars/CertiCoq/certicoq?style=flat)](https://github.com/CertiCoq/certicoq/stargazers) - Verified compiler from Gallina, the internal language of Coq, down to CompCert's Clight language.
- [Fiat-Crypto](https://github.com/mit-plv/fiat-crypto) [![GitHub stars](https://img.shields.io/github/stars/mit-plv/fiat-crypto?style=flat)](https://github.com/mit-plv/fiat-crypto/stargazers) - Cryptographic primitive code generation.
- [Functional Algorithms Verified in SSReflect](https://github.com/clayrat/fav-ssr) [![GitHub stars](https://img.shields.io/github/stars/clayrat/fav-ssr?style=flat)](https://github.com/clayrat/fav-ssr/stargazers) - Purely functional verified implementations of algorithms for searching, sorting, and other fundamental problems.
- [Incremental Cycles](https://gitlab.inria.fr/agueneau/incremental-cycles) - Verified OCaml implementation of an algorithm for incremental cycle detection in graphs.
- [Jasmin](https://github.com/jasmin-lang/jasmin) [![GitHub stars](https://img.shields.io/github/stars/jasmin-lang/jasmin?style=flat)](https://github.com/jasmin-lang/jasmin/stargazers) - Formalized language and verified compiler for high-assurance and high-speed cryptography.
- [JSCert](https://github.com/jscert/jscert) [![GitHub stars](https://img.shields.io/github/stars/jscert/jscert?style=flat)](https://github.com/jscert/jscert/stargazers) - Coq specification of ECMAScript 5 (JavaScript) with verified reference interpreter.
- [lambda-rust](https://gitlab.mpi-sws.org/iris/lambda-rust) - Formal model of a Rust core language and type system, a logical relation for the type system, and safety proofs for some Rust libraries.
- [Prosa](https://gitlab.mpi-sws.org/RT-PROOFS/rt-proofs) - Definitions and proofs for real-time system schedulability analysis.
- [RISC-V Specification in Coq](https://github.com/mit-plv/riscv-coq) [![GitHub stars](https://img.shields.io/github/stars/mit-plv/riscv-coq?style=flat)](https://github.com/mit-plv/riscv-coq/stargazers) - Definition of the RISC-V processor instruction set architecture and extensions.
- [Stable sort algorithms in Coq](https://github.com/pi8027/stablesort) [![GitHub stars](https://img.shields.io/github/stars/pi8027/stablesort?style=flat)](https://github.com/pi8027/stablesort/stargazers) - Generic and modular proofs of correctness, including stability, of mergesort functions.
- [Tarjan and Kosaraju](https://github.com/math-comp/tarjan) [![GitHub stars](https://img.shields.io/github/stars/math-comp/tarjan?style=flat)](https://github.com/math-comp/tarjan/stargazers) - Verified implementations of algorithms for topological sorting and finding strongly connected components in finite graphs.
- [Vélus](http://velus.inria.fr) - Verified compiler for a Lustre/Scade-like dataflow synchronous language.
- [Verdi Raft](https://github.com/uwplse/verdi-raft) [![GitHub stars](https://img.shields.io/github/stars/uwplse/verdi-raft?style=flat)](https://github.com/uwplse/verdi-raft/stargazers) - Implementation of the Raft distributed consensus protocol, verified in Coq using the Verdi framework.
- [WasmCert-Coq](https://github.com/WasmCert/WasmCert-Coq/) [![GitHub stars](https://img.shields.io/github/stars/WasmCert/WasmCert-Coq/?style=flat)](https://github.com/WasmCert/WasmCert-Coq//stargazers) - Formalization in Coq of the WebAssembly (aka Wasm) 1.0 specification.

## Resources

### Community

- [Official Coq website](https://coq.inria.fr)
- [Official Coq manual](https://coq.inria.fr/refman/)
- [Official Coq standard library](https://coq.inria.fr/stdlib/)
- [Official Coq Discourse forum](https://coq.discourse.group)
- [Official Coq Zulip chat](https://coq.zulipchat.com)
- [Official Coq-Club mailing list](https://sympa.inria.fr/sympa/arc/coq-club)
- [Official Coq wiki](https://github.com/coq/coq/wiki) [![GitHub stars](https://img.shields.io/github/stars/coq/coq/wiki?style=flat)](https://github.com/coq/coq/wiki/stargazers)
- [Official Coq X/Twitter](https://x.com/CoqLang)
- [Coq Zulip chat archive](https://coq.gitlab.io/zulip-archive/)
- [Coq subreddit](https://www.reddit.com/r/Coq/)
- [Coq tag on Stack Overflow](https://stackoverflow.com/questions/tagged/coq)
- [Coq tag on Theoretical Computer Science Stack Exchange](https://cstheory.stackexchange.com/questions/tagged/coq)
- [Coq tag on Proof Assistants Stack Exchange](https://proofassistants.stackexchange.com/questions/tagged/coq)
- [Coq keyword on Zenodo](https://zenodo.org/search?q=keywords%3A%22Coq%22)
- [Coq-community package maintenance project](https://github.com/coq-community/manifesto) [![GitHub stars](https://img.shields.io/github/stars/coq-community/manifesto?style=flat)](https://github.com/coq-community/manifesto/stargazers)
- [Mathematical Components wiki](https://github.com/math-comp/math-comp/wiki) [![GitHub stars](https://img.shields.io/github/stars/math-comp/math-comp/wiki?style=flat)](https://github.com/math-comp/math-comp/wiki/stargazers)
- [100 famous theorems proved using Coq](https://github.com/coq-community/coq-100-theorems) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coq-100-theorems?style=flat)](https://github.com/coq-community/coq-100-theorems/stargazers)
- [Planet Coq link aggregator](https://coq.pl-a.net)

### Blogs

- [Coq Exchange: ideas and experiment reports about Coq](https://project.inria.fr/coqexchange/news/)
- [Gagallium](http://gallium.inria.fr/blog)
- [Gregory Malecha's blog](https://gmalecha.github.io)
- [Joachim Breitner's blog posts on Coq](http://www.joachim-breitner.de/blog/tag/Coq)
- [Lysxia's blog](https://blog.poisson.chat)
- [MIT PLV blog posts on Coq](http://plv.csail.mit.edu/blog/category/coq.html)
- [PLClub Blog](https://www.seas.upenn.edu/~plclub/blog/)
- [Poleiro: a Coq blog by Arthur Azevedo de Amorim](http://poleiro.info)
- [Ralf Jung's blog posts on Coq](https://www.ralfj.de/blog/categories/coq.html)
- [Thomas Letan's blog posts on Coq](https://soap.coffee/~lthms/tags/coq.html)

### Books

- [Coq'Art](https://www.labri.fr/perso/casteran/CoqArt/) - The first book dedicated to Coq.
- [Software Foundations](https://softwarefoundations.cis.upenn.edu) - Series of Coq-based textbooks on logic, functional programming, and foundations of programming languages, aimed at being accessible to beginners.
  - [Volume 1: Logical Foundations](https://softwarefoundations.cis.upenn.edu/lf-current/index.html) - Introduction to functional programming, basic concepts of logic, and computer-assisted theorem proving.
  - [Volume 2: Programming Language Foundations](https://softwarefoundations.cis.upenn.edu/plf-current/index.html) - Introduction to the theory of programming languages, including operational semantics, Hoare logic, and static type systems.
  - [Volume 3: Verified Functional Algorithms](https://softwarefoundations.cis.upenn.edu/vfa-current/index.html) - Demonstration of how a variety of fundamental data structures can be specified and verified.
  - [Volume 4: QuickChick](https://softwarefoundations.cis.upenn.edu/qc-current/index.html) - Introduction to tools for combining randomized property-based testing with formal specification and proof.
  - [Volume 5: Verifiable C](https://softwarefoundations.cis.upenn.edu/vc-current/index.html) - An extended tutorial on specifying and verifying C programs using the Verified Software Toolchain.
  - [Volume 6: Separation Logic Foundations](https://softwarefoundations.cis.upenn.edu/slf-current/index.html) - An introduction to separation logic and how to build program verification tools on top of it.
- [Certified Programming with Dependent Types](http://adam.chlipala.net/cpdt/) - Textbook about practical engineering with Coq which teaches advanced practical tricks and a very specific style of proof.
- [Program Logics for Certified Compilers](https://www.cs.princeton.edu/~appel/papers/plcc.pdf) - Book that explains how to construct program logics using separation logic, accompanied by a formal model in Coq which is applied to the Clight programming language and other examples.
- [Formal Reasoning About Programs](http://adam.chlipala.net/frap/) - Book that simultaneously provides a general introduction to formal logical reasoning about the correctness of programs and to using Coq for this purpose.
- [Programs and Proofs](https://ilyasergey.net/pnp/) - Book that gives a brief and practically-oriented introduction to interactive proofs in Coq which emphasizes the computational nature of inductive reasoning about decidable propositions via a small set of primitives from the SSReflect proof language.
- [Computer Arithmetic and Formal Proofs](https://www.sciencedirect.com/book/9781785481123/computer-arithmetic-and-formal-proofs) - Book that describes how to formally specify and verify floating-point algorithms in Coq using the Flocq library.
- [The Mathematical Components book](https://math-comp.github.io/mcb/) - Book oriented towards mathematically inclined users, focusing on the Mathematical Components library and the SSReflect proof language.
- [Modeling and Proving in Computational Type Theory](https://github.com/uds-psl/MPCTT) [![GitHub stars](https://img.shields.io/github/stars/uds-psl/MPCTT?style=flat)](https://github.com/uds-psl/MPCTT/stargazers) - Book covering topics in computational logic using Coq, including foundations, canonical case studies, and practical programming.
- [Hydras & Co.](https://github.com/coq-community/hydra-battles) [![GitHub stars](https://img.shields.io/github/stars/coq-community/hydra-battles?style=flat)](https://github.com/coq-community/hydra-battles/stargazers) - Continuously in-progress book and library on Kirby and Paris' hydra battles and other entertaining formalized mathematics in Coq, including a proof of the Gödel-Rosser first incompleteness theorem.

### Course Material

- [An Introduction to MathComp-Analysis](https://staff.aist.go.jp/reynald.affeldt/documents/karate-coq.pdf) - Lecture notes on getting started with the Mathematical Components library and using it for classical reasoning and real analysis.
- [Foundations of Separation Logic](https://chargueraud.org/teach/verif/) - Introduction to using separation logic to reason about sequential imperative programs in Coq.
- [Floating-Point Numbers and Formal Proof](https://github.com/thery/FlocqLecture) [![GitHub stars](https://img.shields.io/github/stars/thery/FlocqLecture?style=flat)](https://github.com/thery/FlocqLecture/stargazers) - Introductory course on Coq real numbers and floating-point numbers from the Flocq library.
- [Introduction to the Theory of Computation](https://gitlab.com/umb-svl/turing) - Formalization to support an undergraduate course on the theory of computation, including languages and Turing machines.
- [Lectures on Software Foundations](https://github.com/clarksmr/sf-lectures) [![GitHub stars](https://img.shields.io/github/stars/clarksmr/sf-lectures?style=flat)](https://github.com/clarksmr/sf-lectures/stargazers) - Material on the Software Foundations series of textbooks, including a series of YouTube videos.
- [MathComp School](https://github.com/gares/math-comp-school-2022) [![GitHub stars](https://img.shields.io/github/stars/gares/math-comp-school-2022?style=flat)](https://github.com/gares/math-comp-school-2022/stargazers) - Coq sources for lessons and exercises that introduce the SSReflect proof language and the Mathematical Components library.
- [Mechanized Semantics](https://github.com/xavierleroy/cdf-mech-sem) [![GitHub stars](https://img.shields.io/github/stars/xavierleroy/cdf-mech-sem?style=flat)](https://github.com/xavierleroy/cdf-mech-sem/stargazers) - Companion Coq sources for a course on programming language semantics at Collège de France.
- [Program Logics](https://github.com/xavierleroy/cdf-program-logics) [![GitHub stars](https://img.shields.io/github/stars/xavierleroy/cdf-program-logics?style=flat)](https://github.com/xavierleroy/cdf-program-logics/stargazers) - Companion Coq sources for a course on program logics at Collège de France.
- [Program verification with types and logic](https://gitlab.science.ru.nl/program-verification/course-2023-2024) - Lectures and exercise material for a course in programming language semantics, type systems and program logics, using Coq, at Radboud University Nijmegen.
- [Proofs and Reliable Programming using Coq](https://team.inria.fr/stamp/proofs-and-reliable-programming-using-coq-2022/) - Introduction to developing and verifying programs with Coq.

### Tutorials and Hints

- [Coq'Art Exercises and Tutorials](https://github.com/coq-community/coq-art) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coq-art?style=flat)](https://github.com/coq-community/coq-art/stargazers) - Coq code and exercises from the Coq'Art book, including additional tutorials.
- [Coq in a Hurry](http://cel.archives-ouvertes.fr/inria-00001173) - Introduction to how Coq can be used to define logical concepts and functions and reason about them.
- [Coq requirements in Common Criteria evaluations](https://inria.hal.science/hal-04452421) - Guide on how to write readable and reviewable Coq code in high assurance applications.
- [Coq Tactics in Plain English](https://charlesaverill.github.io/ctpe/) - Guide to Coq tactics with explanations and examples.
- [Learn X in Y minutes where X=Coq](https://learnxinyminutes.com/docs/coq/) - Whirlwind tour of Coq as a language.
- [Lemma Overloading](https://github.com/coq-community/lemma-overloading) [![GitHub stars](https://img.shields.io/github/stars/coq-community/lemma-overloading?style=flat)](https://github.com/coq-community/lemma-overloading/stargazers) - Demonstration of design patterns for programming and proving with canonical structures.
- [MathComp Tutorial Materials](https://github.com/math-comp/tutorial_material) [![GitHub stars](https://img.shields.io/github/stars/math-comp/tutorial_material?style=flat)](https://github.com/math-comp/tutorial_material/stargazers) - Source code for Mathematical Components tutorials.
- [Mike Nahas's Coq Tutorial](https://mdnahas.github.io/doc/nahas_tutorial.html) - Basics of using Coq to write formal proofs.
- [Tricks in Coq](https://github.com/coq-community/coq-tricks) [![GitHub stars](https://img.shields.io/github/stars/coq-community/coq-tricks?style=flat)](https://github.com/coq-community/coq-tricks/stargazers) - Tips, tricks, and features in Coq that are hard to discover.
