# Standards

[![GitHub stars](https://img.shields.io/github/stars/donBarbos/awesome-standards?style=flat)](https://github.com/donBarbos/awesome-standards/stargazers)

<!--lint disable awesome-heading-->
<div align="center">
  <h1>Awesome Standards</h1>
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="https://github.com/donBarbos/awesome-standards/graphs/contributors"><img src="https://img.shields.io/github/contributors/donbarbos/awesome-standards" alt="GitHub contributors" /></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat" alt="PRs welcome" /></a>
  <blockquote>A curated list of technical standards, they may be called requests for comments, proposals, drafts, notes, specifications, or something else.</blockquote>
</div>

## Contents

- [Web Technologies](#web-technologies)
- [APIs](#apis)
- [Programming Languages](#programming-languages)
- [Tools](#tools)
- [Decentralized Systems](#decentralized-systems)
- [Cybersecurity and Cryptography](#cybersecurity-and-cryptography)
- [Operating Systems](#operating-systems)
- [Electronics and Hardware](#electronics-and-hardware)
- [Databases and Storage](#databases-and-storage)
- [Telecommunications](#telecommunications)
- [General](#general)
- [Region Specific](#region-specific)
- [Related Awesome Lists](#related-awesome-lists)

## Web Technologies

- [IETF RFCs](https://www.ietf.org/standards/rfcs/) - Publication in a series from the principal technical development and standards-setting bodies for the Internet, most prominently the IETF.
- [BCPs](https://www.rfc-editor.org/rfc/bcp/bcp-index.txt) - Best Current Practice, sub-series of the RFC document series.
- [ECMA International Standards](https://www.ecma-international.org/publications-and-standards/standards/) - Standards for information and communication systems.
- [W3C](https://www.w3.org/TR/) - World Wide Web Consortium publishes a range of technical reports (Standards and supporting Notes) which help move the web forward.
- [W3C WAI](https://www.w3.org/WAI/) - Strategies, standards, and supporting resources to help you make the Web more accessible to people with disabilities.
- [WHATWG](https://whatwg.org/) - Web Hypertext Application Technology Working Group, founded by individuals of leading Web browser vendors.
- [Unicode Standards](https://www.unicode.org/reports/) - Text encoding standard maintained by the Unicode Consortium.
- [OASIS Open](https://www.oasis-open.org/standards/) - Standards by nonprofit consortium that works to develop both open standards and open source.
- [OpenID Specifications](https://openid.net/developers/specs/) - Identity standards, the most famous of which is the decentralized authentication protocol OpenID Connect.

## APIs

- [GraphQL Spec](https://spec.graphql.org/) - Specification for GraphQL, a query language and execution engine.
- [Protobuf Spec](https://protobuf.dev/reference/protobuf/) - Protocol Buffers are language-neutral, platform-neutral extensible mechanisms for serializing structured data.
- [gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) [![GitHub stars](https://img.shields.io/github/stars/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md?style=flat)](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md/stargazers) - This document serves as a detailed description for an implementation of gRPC carried over HTTP2 framing.
- [XML-RPC](https://xmlrpc.com/spec.md) - Remote procedure call protocol which uses XML to encode its calls and HTTP as a transport mechanism.
- [JSON-RPC](https://www.jsonrpc.org/specification) - Stateless, light-weight remote procedure call protocol.
- [Apache Avro](https://avro.apache.org/docs/++version++/specification/) - Serialization format for record data, and first choice for streaming data pipelines.
- [Apache Thrift](https://github.com/apache/thrift/tree/master/doc/specs) [![GitHub stars](https://img.shields.io/github/stars/apache/thrift/tree/master/doc/specs?style=flat)](https://github.com/apache/thrift/tree/master/doc/specs/stargazers) - Interface Definition Language and binary communication protocol used for defining and creating services for programming languages.
- [OpenRPC Spec](https://spec.open-rpc.org/) - The OpenRPC Specification defines a standard, programming language-agnostic interface description for JSON-RPC 2.0 APIs.
- [OpenAPI Spec](https://spec.openapis.org/) - The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to HTTP APIs.
- [API Blueprint Spec](https://apiblueprint.org/documentation/specification.html) - A markdown based language for describing APIs with interactive documentation support.
- [RAML Spec](https://github.com/raml-org/raml-spec) [![GitHub stars](https://img.shields.io/github/stars/raml-org/raml-spec?style=flat)](https://github.com/raml-org/raml-spec/stargazers) - RESTful API Modeling Language is a YAML based language for describing static APIs (but not REST APIs).
- [JSON Schema](https://json-schema.org/specification) - Standard providing a format for what JSON data is required for a given application and how to interact with it.
- [AsyncAPI Spec](https://www.asyncapi.com/docs/reference/specification/latest) - This specification allows you to create machine-readable definitions of your asynchronous APIs.
- [OpenMessaging Spec](https://github.com/openmessaging/specification) [![GitHub stars](https://img.shields.io/github/stars/openmessaging/specification?style=flat)](https://github.com/openmessaging/specification/stargazers) - Vendor-neutral and language-independent, aimed to develop messaging and streaming applications across heterogeneous systems.
- [CloudEvents Spec](https://github.com/cloudevents/spec) [![GitHub stars](https://img.shields.io/github/stars/cloudevents/spec?style=flat)](https://github.com/cloudevents/spec/stargazers) - A specification for describing event data in a common way.
- [HATEOAS](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-11) - Hypermedia as the engine of application state is a constraint of the REST software architectural style.
- [HAL](https://stateless.group/hal_specification.html) - Convention for defining hypermedia such as links to external resources within JSON or XML code.
- [JSON:API](https://jsonapi.org/) - A specification for building APIs in JSON, defines links and actions.
- [JSON-LD](https://json-ld.org/) - JSON for Linked Data is a standard for hyperlinks in JSON, does not address actions.
- [Ion](https://ionspec.org/) - Simple and intuitive JSON-based hypermedia type for REST.
- [Hydra](https://www.hydra-cg.com/spec/) - Builds on top of JSON-LD to add definition of actions.
- [Siren](https://github.com/kevinswiber/siren) [![GitHub stars](https://img.shields.io/github/stars/kevinswiber/siren?style=flat)](https://github.com/kevinswiber/siren/stargazers) - Structured Interface for Representing Entities, super-rad hypermedia, defines links and actions.
- [Collection+JSON](https://github.com/collection-json/spec) [![GitHub stars](https://img.shields.io/github/stars/collection-json/spec?style=flat)](https://github.com/collection-json/spec/stargazers) - JSON-based read/write hypermedia-type designed, defines links and actions.
- [Odata](https://www.odata.org/documentation/) - A protocol for querying and updating data using RESTful APIs, with rich query capabilities.
- [JSEND](https://github.com/omniti-labs/jsend) [![GitHub stars](https://img.shields.io/github/stars/omniti-labs/jsend?style=flat)](https://github.com/omniti-labs/jsend/stargazers) - Specification for a simple, no-frills, JSON based format for application-level communication.
- [Google API Design Guide](https://cloud.google.com/apis/design) - A general design guide for networked APIs provided by Google.
- [Microsoft REST API Guidelines](https://github.com/Microsoft/api-guidelines) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/api-guidelines?style=flat)](https://github.com/Microsoft/api-guidelines/stargazers) - Repository contains a collection of documents and related materials.
- [Zalando RESTful Guidelines](https://opensource.zalando.com/restful-api-guidelines/) - A model set of guidelines for RESTful APIs and Events, created by Zalando.
- [API Stylebook](https://apistylebook.com/) - Collections of resources for API Design from other companies guidelines.
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist) [![GitHub stars](https://img.shields.io/github/stars/shieldfy/API-Security-Checklist?style=flat)](https://github.com/shieldfy/API-Security-Checklist/stargazers) - Checklist of the most important security countermeasures.

## Programming Languages

- [ECMAScript Proposals](https://github.com/tc39/proposals) [![GitHub stars](https://img.shields.io/github/stars/tc39/proposals?style=flat)](https://github.com/tc39/proposals/stargazers) - Ecma TC39 (Technical Committee 39) is responsible for evolving the ECMAScript programming language and authoring the specification.
- [PEPs](https://peps.python.org/) - Python Enhancement Proposals for language improvements.
- [PHP FIG](https://www.php-fig.org/) - Standards proposed and approved by PHP Framework Interop Group.
- [Rust RFCs](https://rust-lang.github.io/rfcs/) - Proposals to evolve the Rust language.
- [Swift Evolution](https://www.swift.org/swift-evolution/) - Proposals for changes to the Swift language.
- [KEEP](https://github.com/Kotlin/KEEP) [![GitHub stars](https://img.shields.io/github/stars/Kotlin/KEEP?style=flat)](https://github.com/Kotlin/KEEP/stargazers) - Kotlin Evolution and Enhancement Process.
- [SIPs](https://docs.scala-lang.org/sips/) - Scala Improvement Proposals.
- [GHC Proposals](https://github.com/ghc-proposals/ghc-proposals) [![GitHub stars](https://img.shields.io/github/stars/ghc-proposals/ghc-proposals?style=flat)](https://github.com/ghc-proposals/ghc-proposals/stargazers) - Compiler and language changes for Haskell/GHC.
- [EEPs](https://www.erlang.org/eep) - Erlang Enhancement Proposals.
- [JSR](https://jcp.org/en/jsr/all) - Java Specification Requests to standardize Java.
- [Java SE Specs](https://docs.oracle.com/javase/specs/) - Java Language and JVM specifications for Java by Oracle.
- [Go Proposals](https://github.com/golang/proposal) [![GitHub stars](https://img.shields.io/github/stars/golang/proposal?style=flat)](https://github.com/golang/proposal/stargazers) - Design discussions for Go language evolution.
- [GoLang Spec](https://go.dev/ref/spec) - The Go Programming Language Specification.
- [Dart Design](https://github.com/dart-lang/language) [![GitHub stars](https://img.shields.io/github/stars/dart-lang/language?style=flat)](https://github.com/dart-lang/language/stargazers) - Design of the Dart language.
- [C# Design](https://github.com/dotnet/csharplang) [![GitHub stars](https://img.shields.io/github/stars/dotnet/csharplang?style=flat)](https://github.com/dotnet/csharplang/stargazers) - C# Language Design Proposals.
- [F# Design](https://github.com/fsharp/fslang-design) [![GitHub stars](https://img.shields.io/github/stars/fsharp/fslang-design?style=flat)](https://github.com/fsharp/fslang-design/stargazers) - F# Language Design RFCs.
- [Zig Proposals](https://github.com/ziglang/zig/issues?q=is:issue+is:open+label:proposal) [![GitHub stars](https://img.shields.io/github/stars/ziglang/zig/issues?q=is:issue+is:open+label:proposal?style=flat)](https://github.com/ziglang/zig/issues?q=is:issue+is:open+label:proposal/stargazers) - Issues with Proposal label in Zig repository.
- [C Standards](https://www.open-std.org/jtc1/sc22/wg14/www/projects) - ISO/IEC standards for the C programming language.
- [C++ Standards](https://www.open-std.org/jtc1/sc22/wg21/) - ISO/IEC standards for C++.
- [CEPs](https://github.com/coq/ceps) [![GitHub stars](https://img.shields.io/github/stars/coq/ceps?style=flat)](https://github.com/coq/ceps/stargazers) - Coq Enhancement Proposals.
- [OCaml RFCs](https://github.com/ocaml/RFCs) [![GitHub stars](https://img.shields.io/github/stars/ocaml/RFCs?style=flat)](https://github.com/ocaml/RFCs/stargazers) - Design discussions about the OCaml language.
- [SRFI](https://srfi.schemers.org/) - Scheme Requests for Implementation.
- [Scheme Standards](https://standards.scheme.org/) - Revised Report on Scheme and other standards.
- [CDR](https://cdr.common-lisp.dev/) - Common Lisp Document Repository.
- [PPCs](https://github.com/Perl/PPCs) [![GitHub stars](https://img.shields.io/github/stars/Perl/PPCs?style=flat)](https://github.com/Perl/PPCs/stargazers) - Proposed Perl Changes is proposals to change the Perl language.
- [DIPs](https://github.com/dlang/DIPs) [![GitHub stars](https://img.shields.io/github/stars/dlang/DIPs?style=flat)](https://github.com/dlang/DIPs/stargazers) - D language Improvement Proposals.
- [GEPs](https://groovy.apache.org/wiki/geps.html) - Groovy Enhancement Proposals and Issues tracked in Jira.
- [Vlang RFCs](https://github.com/vlang/rfcs) [![GitHub stars](https://img.shields.io/github/stars/vlang/rfcs?style=flat)](https://github.com/vlang/rfcs/stargazers) - RFCs for changes to V lang.

## Tools

- [npm RFCs](https://github.com/npm/rfcs) [![GitHub stars](https://img.shields.io/github/stars/npm/rfcs?style=flat)](https://github.com/npm/rfcs/stargazers) - Change proposals for npm.
- [Yarn RFCs](https://github.com/yarnpkg/rfcs) [![GitHub stars](https://img.shields.io/github/stars/yarnpkg/rfcs?style=flat)](https://github.com/yarnpkg/rfcs/stargazers) - Proposals for improvements in Yarn package manager.
- [React RFCs](https://github.com/reactjs/rfcs) [![GitHub stars](https://img.shields.io/github/stars/reactjs/rfcs?style=flat)](https://github.com/reactjs/rfcs/stargazers) - Change requests for React.
- [Vue RFCs](https://github.com/vuejs/rfcs) [![GitHub stars](https://img.shields.io/github/stars/vuejs/rfcs?style=flat)](https://github.com/vuejs/rfcs/stargazers) - Suggestions for major changes to Vue.js.
- [Svelte RFCs](https://github.com/sveltejs/rfcs) [![GitHub stars](https://img.shields.io/github/stars/sveltejs/rfcs?style=flat)](https://github.com/sveltejs/rfcs/stargazers) - Svelte framework enhancement discussions.
- [Ember RFCs](https://rfcs.emberjs.com/) - Standards for Ember.js framework evolution.
- [ESLint RFCs](https://github.com/eslint/rfcs) [![GitHub stars](https://img.shields.io/github/stars/eslint/rfcs?style=flat)](https://github.com/eslint/rfcs/stargazers) - Change requests for ESLint.
- [React Native RFCs](https://github.com/react-native-community/discussions-and-proposals) [![GitHub stars](https://img.shields.io/github/stars/react-native-community/discussions-and-proposals?style=flat)](https://github.com/react-native-community/discussions-and-proposals/stargazers) - React Native enhancement discussions.
- [Nix RFCs](https://github.com/NixOS/rfcs) [![GitHub stars](https://img.shields.io/github/stars/NixOS/rfcs?style=flat)](https://github.com/NixOS/rfcs/stargazers) - The Nix community RFCs.
- [DEPs](https://github.com/django/deps) [![GitHub stars](https://img.shields.io/github/stars/django/deps?style=flat)](https://github.com/django/deps/stargazers) - Django Enhancement Proposals.
- [CEPs](https://github.com/conda/ceps) [![GitHub stars](https://img.shields.io/github/stars/conda/ceps?style=flat)](https://github.com/conda/ceps/stargazers) - Conda Enhancement Proposals.
- [SLEPs](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/) - Enhancement proposals for scikit-learn.
- [JEPs](https://jupyter.org/enhancement-proposals) - Jupyter Ecosystem Enhancement Proposals.
- [JEPs](https://github.com/jenkinsci/jep) [![GitHub stars](https://img.shields.io/github/stars/jenkinsci/jep?style=flat)](https://github.com/jenkinsci/jep/stargazers) - Jenkins Enhancement Proposals.
- [REPs](https://www.ros.org/reps/rep-0000.html) - Enhancement proposals for ROS robotics framework.
- [KEPs](https://www.kubernetes.dev/resources/keps/) - Kubernetes Enhancement Proposals.
- [HIPs](https://github.com/helm/community) [![GitHub stars](https://img.shields.io/github/stars/helm/community?style=flat)](https://github.com/helm/community/stargazers) - Helm Improvement Proposals.
- [OTEPs](https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps/) [![GitHub stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-specification/tree/main/oteps/?style=flat)](https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps//stargazers) - OpenTelemetry Enhancement Proposals.
- [GIPs](https://godot-proposals-viewer.github.io/) - Godot (Multi-platform 2D and 3D game engine) Improvement Proposals.
- [Bazel Proposals](https://github.com/bazelbuild/proposals) [![GitHub stars](https://img.shields.io/github/stars/bazelbuild/proposals?style=flat)](https://github.com/bazelbuild/proposals/stargazers) - Index of all Bazel proposals and design documents.
- [Conventional Commits](https://www.conventionalcommits.org/) - A specification for adding human and machine readable meaning to commit messages.
- [Compose Specification](https://github.com/compose-spec/compose-spec) [![GitHub stars](https://img.shields.io/github/stars/compose-spec/compose-spec?style=flat)](https://github.com/compose-spec/compose-spec/stargazers) - The Compose Specification is developer focused for defining cloud and platform agnostic container-based applications.
- [Fluent Specs](https://github.com/projectfluent/fluent) [![GitHub stars](https://img.shields.io/github/stars/projectfluent/fluent?style=flat)](https://github.com/projectfluent/fluent/stargazers) - This repository contains the specification, the reference implementation of the parser and the documentation for Fluent.
- [\[x\]it!](https://xit.jotaen.net/) - A plain-text file format for todos and check lists.
- [SPDX Spec](https://spdx.github.io/spdx-spec/) - The System Package Data Exchange Specification.
- [HeadVer Spec](https://github.com/line/headver) [![GitHub stars](https://img.shields.io/github/stars/line/headver?style=flat)](https://github.com/line/headver/stargazers) - SemVer compatible version specification that has {head}.{yearweek}.{build} system.
- [SemVer Spec](https://semver.org/) - Semantic Versioning Specification.
- [CalVer Spec](https://calver.org/) - Calendar Versioning Specification.
- [OpenAutoComplete Spec](https://github.com/openautocomplete/openautocomplete) [![GitHub stars](https://img.shields.io/github/stars/openautocomplete/openautocomplete?style=flat)](https://github.com/openautocomplete/openautocomplete/stargazers) - CLI autocomplete specification.

## Decentralized Systems

- [BIPs](https://github.com/bitcoin/bips) [![GitHub stars](https://img.shields.io/github/stars/bitcoin/bips?style=flat)](https://github.com/bitcoin/bips/stargazers) - Bitcoin Improvement Proposals.
- [EIPs](https://eips.ethereum.org/) - Ethereum Improvement Proposals.
- [ZIPs](https://zips.z.cash/) - Zcash Improvement Proposals.
- [NEPs](https://github.com/near/NEPs) [![GitHub stars](https://img.shields.io/github/stars/near/NEPs?style=flat)](https://github.com/near/NEPs/stargazers) - NEAR Protocol Specifications and Standards.
- [BOLTs](https://github.com/lightning/bolts) [![GitHub stars](https://img.shields.io/github/stars/lightning/bolts?style=flat)](https://github.com/lightning/bolts/stargazers) - Basis of Lightning Technology (Lightning Network Specifications).
- [BEPs](https://github.com/bittorrent/bittorrent.org) [![GitHub stars](https://img.shields.io/github/stars/bittorrent/bittorrent.org?style=flat)](https://github.com/bittorrent/bittorrent.org/stargazers) - BitTorrent Enhancement Proposals.
- [BTIPs](https://github.com/bittorrent/BTIPs) [![GitHub stars](https://img.shields.io/github/stars/bittorrent/BTIPs?style=flat)](https://github.com/bittorrent/BTIPs/stargazers) - BitTorrent File System Improvement Proposals.
- [SLIPs](https://github.com/satoshilabs/slips) [![GitHub stars](https://img.shields.io/github/stars/satoshilabs/slips?style=flat)](https://github.com/satoshilabs/slips/stargazers) - SatoshiLabs Improvement Proposals.
- [YIPs](https://yips.yearn.fi/) - Yearn Finance Improvement Proposals.
- [AIPs](https://github.com/aave/aip) [![GitHub stars](https://img.shields.io/github/stars/aave/aip?style=flat)](https://github.com/aave/aip/stargazers) - Aave Improvement Proposals.
- [Optimism Specs](https://specs.optimism.io/) - Optimism Stack Specifications.
- [PIPs](https://github.com/maticnetwork/Polygon-Improvement-Proposals) [![GitHub stars](https://img.shields.io/github/stars/maticnetwork/Polygon-Improvement-Proposals?style=flat)](https://github.com/maticnetwork/Polygon-Improvement-Proposals/stargazers) - Polygon Improvement Proposals.
- [SIPs](https://sips.synthetix.io/) - Synthetix Improvement Proposals.
- [Fuel Specs](https://docs.fuel.network/docs/specs/) - Specifications for the Fuel protocol and the FuelVM.
- [Filecoin Specs](https://spec.filecoin.io/) - Filecoin protocol specification.
- [CAIPs](https://github.com/ChainAgnostic/CAIPs) [![GitHub stars](https://img.shields.io/github/stars/ChainAgnostic/CAIPs?style=flat)](https://github.com/ChainAgnostic/CAIPs/stargazers) - Chain Agnostic Improvement Proposals.
- [AIPs](https://governance.aptosfoundation.org/) - Aptos Improvement Proposals.
- [HIPs](https://github.com/helium/HIP) [![GitHub stars](https://img.shields.io/github/stars/helium/HIP?style=flat)](https://github.com/helium/HIP/stargazers) - Helium Improvement Proposals.
- [HCS](https://github.com/hiero-ledger/hiero-consensus-specifications) [![GitHub stars](https://img.shields.io/github/stars/hiero-ledger/hiero-consensus-specifications?style=flat)](https://github.com/hiero-ledger/hiero-consensus-specifications/stargazers) - Hiero Consensus Standards.
- [MIPs](https://github.com/makerdao/mips) [![GitHub stars](https://img.shields.io/github/stars/makerdao/mips?style=flat)](https://github.com/makerdao/mips/stargazers) - Maker Improvement Proposals.
- [SNIPs](https://github.com/starknet-io/SNIPs) [![GitHub stars](https://img.shields.io/github/stars/starknet-io/SNIPs?style=flat)](https://github.com/starknet-io/SNIPs/stargazers) - Starknet Improvement Proposals.
- [Nervos Network RFCs](https://github.com/nervosnetwork/rfcs) [![GitHub stars](https://img.shields.io/github/stars/nervosnetwork/rfcs?style=flat)](https://github.com/nervosnetwork/rfcs/stargazers) - Proposals, standards and documentations related to Nervos Network.
- [IPIP](https://specs.ipfs.tech/) - InterPlanetary Improvement Proposals, technical specifications for the IPFS protocol stack.
- [Tor Specs](https://spec.torproject.org/) - Tor Specifications including proposals.
- [I2P Specs](https://geti2p.net/spec) - I2P Specification Documents including proposals.
- [LibP2P Specs](https://github.com/libp2p/specs) [![GitHub stars](https://img.shields.io/github/stars/libp2p/specs?style=flat)](https://github.com/libp2p/specs/stargazers) - Technical specifications for the libp2p networking stack.

## Cybersecurity and Cryptography

- [NIST](https://www.nist.gov/documentary-standards) - National Institute of Standards and Technology of the United States.
- [FIPS](https://www.nist.gov/itl/publications-0/federal-information-processing-standards-fips) - Federal Information Processing Standards of the United States.
- [PKCS](https://arxiv.org/pdf/1207.5446v1.pdf) - Public Key Cryptography Standards is group of standards devised and published by RSA Security LLC.
- [FIDO Specifications](https://fidoalliance.org/specifications/) - Authentication standards that "help reduce the world's over-reliance on passwords".
- [OWASP MASVS](https://github.com/OWASP/owasp-masvs) [![GitHub stars](https://img.shields.io/github/stars/OWASP/owasp-masvs?style=flat)](https://github.com/OWASP/owasp-masvs/stargazers) - Mobile Application Security Verification Standard is the industry standard for mobile app security.

## Operating Systems

- [POSIX Standards](https://pubs.opengroup.org/onlinepubs/9799919799/) - The Portable Operating System Interface is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- [Windows API (WinAPI)](https://learn.microsoft.com/en-us/windows/win32/apiindex/windows-api-list) - Foundational API that allows a computer program to access the features of the Microsoft Windows OS.
- [LSB](https://refspecs.linuxfoundation.org/lsb.shtml) - Linux Standard Base.
- [SUS](https://unix.org/what_is_unix/single_unix_specification.html) - Single UNIX Specification.
- [X/Open Portability Guide (XPG)](https://bitsavers.computerhistory.org/pdf/xOpen/X_Open_Portability_Guide_1985/) - A precursor to POSIX and the Single UNIX Specification.
- [UEFI Specifications](https://uefi.org/specifications) - Unified Extensible Firmware Interface is a specification for the firmware architecture of a computing platform.
- [FHS](https://refspecs.linuxfoundation.org/fhs.shtml) - The Filesystem Hierarchy Standard is reference describing the conventions used for the layout of Unix-like systems.
- [LUKS](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/Specification) - The Linux Unified Key Setup is a disk encryption specification.
- [OVF (Open Virtualization Format)](https://www.dmtf.org/standards/ovf) - OS images for virtualized environments.
- [KVM (Kernel-based Virtual Machine)](https://public.dhe.ibm.com/software/dw/linux390/perf/ZSW03346USEN.pdf) - OS-level virtualization in Linux.
- [OCI (Open Container Initiative)](https://opencontainers.org/release-notices/overview/) - Standards for OS containers like Docker.
- [D-Bus](https://dbus.freedesktop.org/doc/dbus-specification.html) - Desktop Bus Specification is message-based inter-process communication system.

## Electronics and Hardware

- [IEEE](https://standards.ieee.org/standard/) - Institute of Electrical and Electronics Engineers.
- [PCI Standards](https://www.pcisecuritystandards.org/) - The Payment Card Industry Data Security Standard (PCI DSS).
- [HDMI Specifications](https://www.hdmi.org/spec/index) - High-Definition Multimedia Interface is a proprietary audio/video interface for transmitting uncompressed video data and compressed or uncompressed digital audio data.
- [Bluetooth Core Specifications](https://www.bluetooth.com/specifications/specs/core-specification-6-0/) - Short-range wireless technology standard.

## Databases and Storage

- [CEPs](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=95652201) - Cassandra Enhancement Proposals.
- [SPIPs](https://spark.apache.org/improvement-proposals.html) - Spark project improvement proposals.

## Telecommunications

- [ITU-T](https://www.itu.int/en/ITU-T/Pages/default.aspx) - International Telecommunication Union.
- [ETSI](https://www.etsi.org/standards) - European Telecommunications Standards Institute.

## General

> these are a series of standards whose standards can simultaneously relate to different topics

- [ISO](https://www.iso.org/standards.html) - International standard development organization composed of representatives from the national standards organizations of member countries.
- [IEC](https://www.iec.ch/publications/international-standards) - International standards organization that prepares and publishes international standards for all electrical, electronic and related technologies – collectively known as "electrotechnology".
- [ANSI](https://www.ansi.org/) - Private nonprofit organization that oversees the development of voluntary consensus standards for products, services, processes, systems, and personnel in the United States.

## Region Specific

> the use of these standards is specific to certain regions

- [BS](https://www.bsigroup.com/) - **British Standards**: Standards published by the BSI Group, the UK's National Standards Body (NSB). They provide guidelines for quality, safety, and sustainability across various sectors.
- [CEN](https://www.cencenelec.eu/) - **European Committee for Standardization**: Develops European Standards (ENs) to harmonize technical specifications and promote trade across Europe.
- [DIN](https://www.din.de/) - **Deutsches Institut für Normung**: German Institute for Standardization, which develops national and international standards for a wide range of industries.
- [AFNOR](https://www.afnor.org/) - **Association française de normalisation**: France's National Standardization Office.
- [NSAI](https://www.nsai.ie/) - **National Standards Authority of Ireland**: Ireland's official standards body.
- [CSA Group](https://www.csagroup.org/) - **Canadian Standards Association**: Develops standards to address safety, sustainability, and performance for Canada and global markets.
- [SII](https://www.sii.org.il/eng/) - **Standards Institution of Israel**: National body for standards and certification.
- [NOM](https://www.gob.mx/se/acciones-y-programas/standards) - **Normas Oficiales Mexicanas**: Official Mexican standards governing the safety, health and quality of goods and services.
- [ABNT](https://abnt.org.br/) - **Associação Brasileira de Normas Técnicas**: Brazilian National Standards Organization.
- [SS](https://www.singaporestandardseshop.sg/) - **Singapore Standards**: Organization handling trade and technology standards.
- [JIS](https://www.jisc.go.jp/eng/) - **Japanese Industrial Standards**: Specifications published by the Japanese Industrial Standards Committee (JISC) to ensure product quality and safety in Japan.
- [KATS](https://www.kats.go.kr/en/) - **Korean Agency for Technology and Standards**: Organization for developing standards across various sectors.
- [CNS](https://www.cnsonline.com.tw/) - **Chinese National Standards**: Taiwan's official standards, administered by the Bureau of Standards, Metrology, and Inspection.
- [GB](https://www.gbstandards.org/) - **Guobiao Standards**: China's national standards, including technical and industry-specific regulations.
- [GOST](https://www.gost.ru) - **Russian National Standards**: State standards developed by Rosstandart to regulate industries and ensure quality and compatibility in Russia.
- [TCVN](https://tcvn.gov.vn/?lang=en) - **Vietnamese National Standards**: Standards published by the Directorate for Standards, Metrology, and Quality of Vietnam to regulate local and international trade.
- [BIS](https://www.bis.gov.in/) - **Bureau of Indian Standards**: National standards for industry, products, and services.
- [PSQCA](https://www.psqca.com.pk/) - **Pakistan Standards and Quality Control Authority**: Organization responsible for developing and certifying standards.
- [TIS](https://www.tisi.go.th/home/en) - **Thai Industrial Standards**: National standards for Thailand.

## Related Awesome Lists

- [Awesome Guidelines](https://github.com/Kristories/awesome-guidelines) [![GitHub stars](https://img.shields.io/github/stars/Kristories/awesome-guidelines?style=flat)](https://github.com/Kristories/awesome-guidelines/stargazers) - Coding style conventions and standards.
- [Awesome API Devtools](https://github.com/yosriady/awesome-api-devtools) [![GitHub stars](https://img.shields.io/github/stars/yosriady/awesome-api-devtools?style=flat)](https://github.com/yosriady/awesome-api-devtools/stargazers) - A collection of useful resources for building RESTful HTTP+JSON APIs.
