# JSON

[![GitHub stars](https://img.shields.io/github/stars/burningtree/awesome-json?style=flat)](https://github.com/burningtree/awesome-json/stargazers)

# Awesome JSON [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A curated list of awesome JSON libraries and resources.

Inspired by the [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) list.

[![Links](https://github.com/burningtree/awesome-json/actions/workflows/links.yml/badge.svg) [![GitHub stars](https://img.shields.io/github/stars/burningtree/awesome-json/actions/workflows/links.yml/badge.svg?style=flat)](https://github.com/burningtree/awesome-json/actions/workflows/links.yml/badge.svg/stargazers)](https://github.com/burningtree/awesome-json/actions/workflows/links.yml)

---

* [Awesome JSON](#awesome-json)
  * [Applications](#applications)
  * [Binary Serialization](#binary-serialization)
  * [Browser Extensions](#browser-extensions)
  * [Command-line tools](#command-line-tools)
  * [Databases](#databases)
  * [Datasets](#datasets)
  * [Data modeling](#data-modeling)
  * [Data generation](#data-generation)
  * [Differencing](#differencing)
  * [Editors](#editors)
  * [Format Extensions](#format-extensions)
  * [Frontend components](#frontend-components)
  * [Libraries](#libraries)
  * [Linters](#linters)
  * [Online tools](#online-tools)
  * [Schema Specifications](#schema-specifications)
  * [Services](#services)
  * [Supersets](#supersets)
  * [Related formats](#related-formats)
  * [Resources](#resources)
  * [Templates](#templates)
  * [Testing](#testing)
  * [Text Editor Plugins](#text-editor-plugins)
  * [Transformations](#transformations)
  * [Tutorials](#tutorials)
  * [Queries](#queries)
  * [JSON Schema Frontend components](#json-schema-frontend-components)
  * [JSON Schema Tools](#json-schema-tools)
  * [JSON Schema Resources](#json-schema-resources)
  * [JSON Schema Validators](#json-schema-validators)
  * [Contribute](#contribute)

## Applications
* [Dadroit JSON Viewer](https://dadroit.com) - Very fast JSON Viewer, supporting huge (multi gigabytes) files, JSON log (JSON-Lines and ndjson).

**OS X**
* [JSON Design Studio](https://stevespringett.com/free-tools/json-design-studio/) - Professional schema authoring environment.
* [Visual JSON](https://github.com/youknowone/VisualJSON) [![GitHub stars](https://img.shields.io/github/stars/youknowone/VisualJSON?style=flat)](https://github.com/youknowone/VisualJSON/stargazers) - simple JSON pretty-viewer for Mac OS X. (inactive)
* [JSONExport](https://github.com/Ahmed-Ali/JSONExport) [![GitHub stars](https://img.shields.io/github/stars/Ahmed-Ali/JSONExport?style=flat)](https://github.com/Ahmed-Ali/JSONExport/stargazers) - convert a object to a class of one of the currently supported languages.

## Binary Serialization
* [BSON](https://bsonspec.org/) - Binary JSON.
* [MessagePack](https://msgpack.org/) - An extremely efficient object serialization library.
* [UBJSON](https://ubjson.org/) - The universally compatible format specification for binary JSON.
* [CBOR](https://datatracker.ietf.org/doc/html/rfc7049) - Concise Binary Object Representation.
* [PSON](https://github.com/dcodeIO/PSON) [![GitHub stars](https://img.shields.io/github/stars/dcodeIO/PSON?style=flat)](https://github.com/dcodeIO/PSON/stargazers) - Protocol JSON, super efficient binary serialization format.
* [JSON BinPack](https://www.jsonbinpack.org) - Space-efficient binary JSON serialization format based on JSON Schema.

## Browser Extensions
**Chrome**
* [JSON Formatter](https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) ([github](https://github.com/callumlocke/json-formatter) [![GitHub stars](https://img.shields.io/github/stars/callumlocke/json-formatter?style=flat)](https://github.com/callumlocke/json-formatter/stargazers)) - Makes JSON easy to read. Open source.
* [JSON Viewer](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh) ([github](https://github.com/tulios/json-viewer) [![GitHub stars](https://img.shields.io/github/stars/tulios/json-viewer?style=flat)](https://github.com/tulios/json-viewer/stargazers)) - It is a Chrome extension for printing JSON and JSONP.
* [JSON Finder](https://chromewebstore.google.com/detail/json-finder/flhdcaebggmmpnnaljiajhihdfconkbj) ([github](https://github.com/rapee/jsonfinder) [![GitHub stars](https://img.shields.io/github/stars/rapee/jsonfinder?style=flat)](https://github.com/rapee/jsonfinder/stargazers)) - Browse like you do it in Finder.
* [JSON Viewer Pro](https://chromewebstore.google.com/detail/json-viewer-pro/eifflpmocdbdmepbjaopkkhbfmdgijcc) ([github](https://github.com/rbrahul/Awesome-JSON-Viewer) [![GitHub stars](https://img.shields.io/github/stars/rbrahul/Awesome-JSON-Viewer?style=flat)](https://github.com/rbrahul/Awesome-JSON-Viewer/stargazers) - An open source Chrome extension for browsing JSON with syntax highlighting and folding, or as a visual graph.
* [Discoverable JSON](https://chromewebstore.google.com/detail/json-manipulator-json-to/pcakbljjigdafljigcpbmjllkbhlncjg) ([github](https://github.com/noitcudni/discoverable-json) [![GitHub stars](https://img.shields.io/github/stars/noitcudni/discoverable-json?style=flat)](https://github.com/noitcudni/discoverable-json/stargazers)) - Gron inspired Extension. Convert a JSON document into javascript expressions. Comes with filter, remove, find-and-replace capabilities.

**Firefox**
* [JSONView](https://addons.mozilla.org/en-US/firefox/addon/jsonview/) ([github](https://github.com/bhollis/jsonview) [![GitHub stars](https://img.shields.io/github/stars/bhollis/jsonview?style=flat)](https://github.com/bhollis/jsonview/stargazers)) - View JSON documents in the browser.

**Safari**
* [JSONAce](https://apps.apple.com/us/story/id1377753262?id=com.acrogenesis.jsonace-56Q494QF3LL) ([github](https://github.com/acrogenesis/JSONAce) [![GitHub stars](https://img.shields.io/github/stars/acrogenesis/JSONAce?style=flat)](https://github.com/acrogenesis/JSONAce/stargazers)) - Formats & syntax highlights JSON viewed inside of the web browser using the ACE editor.
* [JSONView](https://apps.apple.com/us/story/id1377753262?id=com.acrogenesis.jsonview-56Q494QF3L) ([github](https://github.com/acrogenesis/jsonview-safari) [![GitHub stars](https://img.shields.io/github/stars/acrogenesis/jsonview-safari?style=flat)](https://github.com/acrogenesis/jsonview-safari/stargazers)) - A port of the JSONView Firefox extension that formats and syntax highlights JSON viewed inside of the browser

## Command-line tools
* [dsq](https://github.com/multiprocessio/dsq) [![GitHub stars](https://img.shields.io/github/stars/multiprocessio/dsq?style=flat)](https://github.com/multiprocessio/dsq/stargazers) - Tool for running SQL queries against JSON, CSV, Excel, Parquet, and more.
* [fx](https://github.com/antonmedv/fx) [![GitHub stars](https://img.shields.io/github/stars/antonmedv/fx?style=flat)](https://github.com/antonmedv/fx/stargazers) - A interactive terminal tool.
* [jo](https://github.com/jpmens/jo) [![GitHub stars](https://img.shields.io/github/stars/jpmens/jo?style=flat)](https://github.com/jpmens/jo/stargazers) - A small utility to create JSON objects
* [jsoncat](https://github.com/pantuza/jsoncat) [![GitHub stars](https://img.shields.io/github/stars/pantuza/jsoncat?style=flat)](https://github.com/pantuza/jsoncat/stargazers) - Pretty-print Json in terminal with colors and adjusting tabs size.
* [jq](https://github.com/jqlang/jq) [![GitHub stars](https://img.shields.io/github/stars/jqlang/jq?style=flat)](https://github.com/jqlang/jq/stargazers) - A lightweight and flexible command-line JSON processor.
  * [jaq](https://github.com/01mf02/jaq) [![GitHub stars](https://img.shields.io/github/stars/01mf02/jaq?style=flat)](https://github.com/01mf02/jaq/stargazers) - A jq clone focussed on correctness, speed, and simplicity. Written in Rust.
  * [gojq](https://github.com/itchyny/gojq) [![GitHub stars](https://img.shields.io/github/stars/itchyny/gojq?style=flat)](https://github.com/itchyny/gojq/stargazers) - Pure Go implementation of jq. A bit faster and more portable.
* [JSONKit](https://github.com/vesper-astrena/jsonkit) [![GitHub stars](https://img.shields.io/github/stars/vesper-astrena/jsonkit?style=flat)](https://github.com/vesper-astrena/jsonkit/stargazers) - Swiss Army knife: format, validate, query via dot-notation, diff, flatten, convert to CSV, and stats. Zero dependencies, Python 3.10+.
* [livejq](https://github.com/kunalsin9h/livejq) [![GitHub stars](https://img.shields.io/github/stars/kunalsin9h/livejq?style=flat)](https://github.com/kunalsin9h/livejq/stargazers) - An alternative `jq` implementation in rust for continuous parsing without crashing on invalid JSON
* [json](http://trentm.com/json/) - A "json" command for massaging JSON on your Unix command line.
* [json-search](https://github.com/cosmo-ray/json-search) [![GitHub stars](https://img.shields.io/github/stars/cosmo-ray/json-search?style=flat)](https://github.com/cosmo-ray/json-search/stargazers) - A small tool to search for objects/values in json files.
* [jshon](https://web.archive.org/web/20240206155217/http://kmkeen.com/jshon/) - A parser designed for maximum convenience within the shell.
* [jarg](http://jdp.github.io/jarg/) - Shorthand JSON and form encoding syntax in the shell.
* [jsawk](https://github.com/micha/jsawk) [![GitHub stars](https://img.shields.io/github/stars/micha/jsawk?style=flat)](https://github.com/micha/jsawk/stargazers) - Like awk, but for JSON.
* [json-dotenv](https://github.com/decryptus/json-dotenv) [![GitHub stars](https://img.shields.io/github/stars/decryptus/json-dotenv?style=flat)](https://github.com/decryptus/json-dotenv/stargazers) - Manipulate and extract envfiles in json format.
* [gron](https://github.com/tomnomnom/gron) [![GitHub stars](https://img.shields.io/github/stars/tomnomnom/gron?style=flat)](https://github.com/tomnomnom/gron/stargazers) - Convert a JSON file into discrete assignments that are greppable.
* [jid](https://github.com/simeji/jid) [![GitHub stars](https://img.shields.io/github/stars/simeji/jid?style=flat)](https://github.com/simeji/jid/stargazers) - Incremental Digger. Drill down JSON interactively by using filtering queries like jq.
* [jiq](https://github.com/fiatjaf/jiq) [![GitHub stars](https://img.shields.io/github/stars/fiatjaf/jiq?style=flat)](https://github.com/fiatjaf/jiq/stargazers) - It's `jid` with `jq`. You can drill down interactively by using `jq` filtering queries.
* [jv](https://github.com/maxzender/jv) [![GitHub stars](https://img.shields.io/github/stars/maxzender/jv?style=flat)](https://github.com/maxzender/jv/stargazers) - jv (for jsonviewer) helps you view your JSON.
* [jl](https://github.com/chrisdone/jl) [![GitHub stars](https://img.shields.io/github/stars/chrisdone/jl?style=flat)](https://github.com/chrisdone/jl/stargazers) - Functional sed for JSON.
* [oj](https://github.com/ohler55/ojg) [![GitHub stars](https://img.shields.io/github/stars/ohler55/ojg?style=flat)](https://github.com/ohler55/ojg/stargazers) - A fast and flexible command line JSON processor.
* [Parsrs](https://github.com/ShellShoccar-jpn/Parsrs) [![GitHub stars](https://img.shields.io/github/stars/ShellShoccar-jpn/Parsrs?style=flat)](https://github.com/ShellShoccar-jpn/Parsrs/stargazers) - CSV, XML, and data text parsers and generators written in pure POSIX shellscript. Includes `parsrj.sh` and `makrj.sh`.
* [visidata](https://github.com/saulpw/visidata) [![GitHub stars](https://img.shields.io/github/stars/saulpw/visidata?style=flat)](https://github.com/saulpw/visidata/stargazers) - A terminal spreadsheet-like tool for interactively exploring data.
* [jc](https://github.com/kellyjonbrazil/jc) [![GitHub stars](https://img.shields.io/github/stars/kellyjonbrazil/jc?style=flat)](https://github.com/kellyjonbrazil/jc/stargazers) - Converts the output of many CLI tools, file-types, and common strings into JSON
* [logdy](https://github.com/logdyhq/logdy-core) [![GitHub stars](https://img.shields.io/github/stars/logdyhq/logdy-core?style=flat)](https://github.com/logdyhq/logdy-core/stargazers) - jq, tail, less, grep and awk merged together and available in a clean web UI.
* [jsonskim](https://github.com/rxzzh/jsonskim) [![GitHub stars](https://img.shields.io/github/stars/rxzzh/jsonskim?style=flat)](https://github.com/rxzzh/jsonskim/stargazers) - Extract structure by collapsing arrays and truncating strings. LLM-ready output.

## Databases
* [MongoDB](https://www.mongodb.com/) - an open-source document database, and the leading NoSQL database.
* [RethinkDB](https://rethinkdb.com/) - An open-source distributed document database with a pleasant and powerful query language.
* [EJDB](https://github.com/Softmotions/ejdb) [![GitHub stars](https://img.shields.io/github/stars/Softmotions/ejdb?style=flat)](https://github.com/Softmotions/ejdb/stargazers) - Embedded JSON Database engine published under MIT license. (C)
* [lowdb](https://github.com/typicode/lowdb) [![GitHub stars](https://img.shields.io/github/stars/typicode/lowdb?style=flat)](https://github.com/typicode/lowdb/stargazers) - Flat file database built on lodash API. (Javascript)
* [Lawnchair](https://github.com/brianleroux/lawnchair) [![GitHub stars](https://img.shields.io/github/stars/brianleroux/lawnchair?style=flat)](https://github.com/brianleroux/lawnchair/stargazers) - A lightweight clientside document store. (Javascript)
* [JSON ODM](https://github.com/konsultaner/jsonOdm) [![GitHub stars](https://img.shields.io/github/stars/konsultaner/jsonOdm?style=flat)](https://github.com/konsultaner/jsonOdm/stargazers) - Object document mapper for JavaScript to use on the server or in the browser. (Javascript)
* [JSON Server](https://github.com/typicode/json-server) [![GitHub stars](https://img.shields.io/github/stars/typicode/json-server?style=flat)](https://github.com/typicode/json-server/stargazers) - Get a full fake REST API with zero coding in less than 30 seconds.
* [Kinto](https://github.com/Kinto/kinto) [![GitHub stars](https://img.shields.io/github/stars/Kinto/kinto?style=flat)](https://github.com/Kinto/kinto/stargazers) - A lightweight JSON storage service with synchronisation and sharing abilities.
* [CouchDB](https://couchdb.apache.org/) - Seamless multi-master sync, that scales from Big Data to Mobile, with an Intuitive HTTP/JSON API and designed for Reliability.
* [RxDB](https://github.com/pubkey/rxdb) [![GitHub stars](https://img.shields.io/github/stars/pubkey/rxdb?style=flat)](https://github.com/pubkey/rxdb/stargazers) - Event-driven JSON-Database with JSON-Schema, mango-Query and CouchDB-sync. (Javascript)
* [JSONlite](https://github.com/nodesocket/jsonlite) [![GitHub stars](https://img.shields.io/github/stars/nodesocket/jsonlite?style=flat)](https://github.com/nodesocket/jsonlite/stargazers) - A simple, self-contained, serverless, zero-configuration, json document store. (Bash)

## Datasets
* [country.io](http://country.io/data/) - Various country related datasets, as JSON inc currency, country codes, names and more
* [countries](https://github.com/mledoze/countries) [![GitHub stars](https://img.shields.io/github/stars/mledoze/countries?style=flat)](https://github.com/mledoze/countries/stargazers) - World countries.
* [MTG JSON](https://mtgjson.com/) - Up to date Magic the Gathering card data.
* [Heartstone JSON](https://hearthstonejson.com/) - Up to date Hearthstone card data.
* [getCountries()](https://peric.github.io/GetCountries/) - Generator for custom Countries data.

## Data modeling
* [JSONModel](https://github.com/jsonmodel/jsonmodel) [![GitHub stars](https://img.shields.io/github/stars/jsonmodel/jsonmodel?style=flat)](https://github.com/jsonmodel/jsonmodel/stargazers) - Magical Data Modelling Framework. (Objective-C)

## Data generation
* [jsonymize](https://github.com/cameronhunter/jsonymize) [![GitHub stars](https://img.shields.io/github/stars/cameronhunter/jsonymize?style=flat)](https://github.com/cameronhunter/jsonymize/stargazers) - Reads data from standard input, anonymizes, then writes to standard output.
* [dyson](https://github.com/webpro/dyson) [![GitHub stars](https://img.shields.io/github/stars/webpro/dyson?style=flat)](https://github.com/webpro/dyson/stargazers) - Server for dynamic, fake JSON. (node.js)

## Differencing
* [JSONPatch](https://jsonpatch.com/) - A format for describing changes to a document.
* [JSON-Patch](https://github.com/Starcounter-Jack/JSON-Patch) [![GitHub stars](https://img.shields.io/github/stars/Starcounter-Jack/JSON-Patch?style=flat)](https://github.com/Starcounter-Jack/JSON-Patch/stargazers) - Lean and mean Javascript implementation of the JSON-Patch standard (RFC 6902). (Javascript)
* [jiff](https://github.com/cujojs/jiff) [![GitHub stars](https://img.shields.io/github/stars/cujojs/jiff?style=flat)](https://github.com/cujojs/jiff/stargazers) - JSON Patch and diff based on rfc6902. (Javascript)
* [json-patch-php](https://github.com/mikemccabe/json-patch-php) [![GitHub stars](https://img.shields.io/github/stars/mikemccabe/json-patch-php?style=flat)](https://github.com/mikemccabe/json-patch-php/stargazers) - implementation of JSON-patch (IETF RFC 6902) (PHP)
* [dffptch](https://github.com/paldepind/dffptch) [![GitHub stars](https://img.shields.io/github/stars/paldepind/dffptch?style=flat)](https://github.com/paldepind/dffptch/stargazers) - A micro library for diffing and patching using a compact diff format. (Javascript)
* [jsondiffpatch](https://github.com/benjamine/jsondiffpatch) [![GitHub stars](https://img.shields.io/github/stars/benjamine/jsondiffpatch?style=flat)](https://github.com/benjamine/jsondiffpatch/stargazers) - Diff & patch for JavaScript objects. (Javascript)

## Editors
* [FrontAid CMS](https://frontaid.io/) - Content Management System that supports arbitrary data model structures.
* [JSON table editor](https://jsontable.app/) - Display JSON array as table, provides search, filtering and edition features. It supports large files of multiple gigabytes. (Rust).
* [JSONEdit](http://mb21.github.io/JSONedit/) - User friendly, visual editor built as an AngularJS directive.
* [JSON Crack](https://jsoncrack.com/) - Display your JSON as a graph

## Format Extensions
* [GeoJSON](https://geojson.org/) - A geospatial data interchange format.
* [JSON-LD](https://json-ld.org/) - A lightweight Linked Data format.
* [JSON-RPC](https://www.jsonrpc.org/) - A stateless, light-weight remote procedure call (RPC) protocol.
* [JSONP](https://en.wikipedia.org/wiki/JSONP) - Safer cross-domain Ajax with JSON-P/JSONP.
* [JsonML](http://www.jsonml.org/) - A compact format for transporting XML-based markup as JSON which allows it to be losslessly converted back to its original form.
* [JSON5](https://json5.org/) - a extension that aims to make it easier for humans to write and maintain by hand.
* [JSON6](https://github.com/d3x0r/json6) [![GitHub stars](https://img.shields.io/github/stars/d3x0r/json6?style=flat)](https://github.com/d3x0r/json6/stargazers) - JSON for Humans (ES6).
* [JSON 1.1/JSONX](https://json-next.github.io/) - An evolved version 1.1 with format extension for humans incl. comments, unquoted and multi-line strings, optional and trailing commas and more.
* [JSON Resume](https://jsonresume.org/) - The open source initiative to create standard for resumes.
* [JSON Web Tokens](https://jwt.io/) - A compact URL-safe means of representing claims to be transferred between two parties.
* [JSON API](https://jsonapi.org/) - A standard for building APIs.
* [JSON Activity Streams](https://activitystrea.ms/) - A format for syndicating social activities around the web.
* [JSON-stat](https://github.com/jsonstat/jsonstat) [![GitHub stars](https://img.shields.io/github/stars/jsonstat/jsonstat?style=flat)](https://github.com/jsonstat/jsonstat/stargazers) - Simple lightweight format for data dissemination.
* [/contribute.json](https://www.contributejson.org/) - Making open source contribution information easier to access, across projects.
* [NDJSON](https://github.com/ndjson/ndjson-spec) [![GitHub stars](https://img.shields.io/github/stars/ndjson/ndjson-spec?style=flat)](https://github.com/ndjson/ndjson-spec/stargazers) (Newline delimited JSON) - a standard for delimiting JSON in stream protocols.
* [survey.js](https://surveyjs.io/form-library) - JSON based survey library.
* [JSON Meta Application Protocol (JMAP)](https://jmap.io/) - A protocol for synchronising JSON-based data objects efficiently, with support for push and out-of-band binary data upload/download.
* [J<sub>ack</sub>SON: JSON secret keeper](https://github.com/rosehgal/jackson) [![GitHub stars](https://img.shields.io/github/stars/rosehgal/jackson?style=flat)](https://github.com/rosehgal/jackson/stargazers) - JSONic way of storing secrets in config file.
* [Sequence JSON](https://github.com/soundio/music-json/) [![GitHub stars](https://img.shields.io/github/stars/soundio/music-json/?style=flat)](https://github.com/soundio/music-json//stargazers) - A proposal for a standard way of creating music sequence data in JSON.

## Frontend components
* [JSON editor jQuery plugin](https://github.com/DavidDurman/FlexiJsonEditor) [![GitHub stars](https://img.shields.io/github/stars/DavidDurman/FlexiJsonEditor?style=flat)](https://github.com/DavidDurman/FlexiJsonEditor/stargazers) - component for you web apps/pages. (jQuery)
* [jqTree](http://mbraak.github.io/jqTree/) - Widget for displaying a tree structure in html. (jQuery)
* [jsTree](https://www.jstree.com/docs/json/) - jquery plugin, that provides interactive trees. (jQuery)
* [Dynatable.js](https://github.com/alfajango/jquery-dynatable) [![GitHub stars](https://img.shields.io/github/stars/alfajango/jquery-dynatable?style=flat)](https://github.com/alfajango/jquery-dynatable/stargazers) - A funner, semantic, HTML5+JSON, interactive table plugin. (jQuery)
* [JSON Formatter](https://github.com/mohsen1/json-formatter) [![GitHub stars](https://img.shields.io/github/stars/mohsen1/json-formatter?style=flat)](https://github.com/mohsen1/json-formatter/stargazers) - Angular directive for collapsible JSON in HTML. (AngularJS)
* [react-jsonschema-form](https://rjsf-team.github.io/react-jsonschema-form/) - A React component for building Web forms from JSON Schema. (React)
* [@textea/json-viewer](https://github.com/TexteaInc/json-viewer) [![GitHub stars](https://img.shields.io/github/stars/TexteaInc/json-viewer?style=flat)](https://github.com/TexteaInc/json-viewer/stargazers) - A React component for JSON viewer. (React)
* [ngx-formly](https://github.com/ngx-formly/ngx-formly) [![GitHub stars](https://img.shields.io/github/stars/ngx-formly/ngx-formly?style=flat)](https://github.com/ngx-formly/ngx-formly/stargazers) - JSON powered / Dynamic forms for Angular

* [SmarkForm](https://smarkform.bitifet.net) - Enhance HTML forms to import/export any possible data, including arrays and subforms to any depth.
## Libraries
**C**
* [codables](https://codableslib.com/) - Declarative, type-rich (de)serializer able to handle almost any data type.
* [Jansson](https://github.com/akheron/jansson) [![GitHub stars](https://img.shields.io/github/stars/akheron/jansson?style=flat)](https://github.com/akheron/jansson/stargazers) - A C library for encoding, decoding and manipulating data.
* [jsmn](https://zserge.com/jsmn.html) - A minimalistic parser in C. It can be easily integrated into the resource-limited projects or embedded systems.
* [json-build](https://github.com/lcsmuller/json-build) [![GitHub stars](https://img.shields.io/github/stars/lcsmuller/json-build?style=flat)](https://github.com/lcsmuller/json-build/stargazers) - A minimalistic serializer in C. It can be easily integrated into the resource-limited projects or embedded systems.
* [ojc](https://github.com/ohler55/ojc) [![GitHub stars](https://img.shields.io/github/stars/ohler55/ojc?style=flat)](https://github.com/ohler55/ojc/stargazers) - A fast JSON parser.

**C++**
* [ArduinoJson](https://github.com/bblanchon/ArduinoJson) [![GitHub stars](https://img.shields.io/github/stars/bblanchon/ArduinoJson?style=flat)](https://github.com/bblanchon/ArduinoJson/stargazers) - An efficient library for embedded systems.
* [JSON++](https://github.com/tunnuz/json) [![GitHub stars](https://img.shields.io/github/stars/tunnuz/json?style=flat)](https://github.com/tunnuz/json/stargazers) - A self contained Flex/Bison parser for C++11.
* [json11](https://github.com/dropbox/json11) [![GitHub stars](https://img.shields.io/github/stars/dropbox/json11?style=flat)](https://github.com/dropbox/json11/stargazers) - A tiny library for C++11.
* [Nlohmann JSON](https://github.com/nlohmann/json) [![GitHub stars](https://img.shields.io/github/stars/nlohmann/json?style=flat)](https://github.com/nlohmann/json/stargazers) - A C++11 header-only class.
* [qjson](https://github.com/qinyonghang/json) [![GitHub stars](https://img.shields.io/github/stars/qinyonghang/json?style=flat)](https://github.com/qinyonghang/json/stargazers) - A fast library for C++17 that is header-only.
* [RapidJSON](https://github.com/Tencent/rapidjson) [![GitHub stars](https://img.shields.io/github/stars/Tencent/rapidjson?style=flat)](https://github.com/Tencent/rapidjson/stargazers) - A fast JSON parser/generator for C++ with both SAX/DOM style API
* [simdjson](https://github.com/simdjson/simdjson) [![GitHub stars](https://img.shields.io/github/stars/simdjson/simdjson?style=flat)](https://github.com/simdjson/simdjson/stargazers) - Parsing gigabytes of JSON per second.

**Clojure**
* [data.json](https://github.com/clojure/data.json) [![GitHub stars](https://img.shields.io/github/stars/clojure/data.json?style=flat)](https://github.com/clojure/data.json/stargazers) - parser/generator to/from Clojure data structures.

**Fortran**
* [JSON-Fortran](https://github.com/jacobwilliams/json-fortran) [![GitHub stars](https://img.shields.io/github/stars/jacobwilliams/json-fortran?style=flat)](https://github.com/jacobwilliams/json-fortran/stargazers) - A Fortran library for writing, reading, and manipulating JSON files and data structures.

**Go**
* [ojg](https://github.com/ohler55/ojg) [![GitHub stars](https://img.shields.io/github/stars/ohler55/ojg?style=flat)](https://github.com/ohler55/ojg/stargazers) - A collection of high performance JSON processing and generating tool.

**Haskell**
* [aeson-qq](https://github.com/sol/aeson-qq) [![GitHub stars](https://img.shields.io/github/stars/sol/aeson-qq?style=flat)](https://github.com/sol/aeson-qq/stargazers) - JSON quasiquoter for Haskell.
* [json-schema](http://hackage.haskell.org/package/json-schema) - JSON Schema library for Haskell
* [hjsonschema](http://hackage.haskell.org/package/hjsonschema) - JSON Schema Draft 4 library for Haskell

**Java**
* [JSON-java](https://github.com/stleary/JSON-java) [![GitHub stars](https://img.shields.io/github/stars/stleary/JSON-java?style=flat)](https://github.com/stleary/JSON-java/stargazers) - A reference implementation.
* [Fast JSON Processor](https://github.com/alibaba/fastjson) [![GitHub stars](https://img.shields.io/github/stars/alibaba/fastjson?style=flat)](https://github.com/alibaba/fastjson/stargazers)
* [Gson](https://github.com/google/gson) [![GitHub stars](https://img.shields.io/github/stars/google/gson?style=flat)](https://github.com/google/gson/stargazers) - A Java library to convert JSON to Java objects and vice-versa.
* [Jackson](https://github.com/FasterXML/jackson) [![GitHub stars](https://img.shields.io/github/stars/FasterXML/jackson?style=flat)](https://github.com/FasterXML/jackson/stargazers) - A multi-purpose Java library for processing JSON data format.
* [moshi](https://github.com/square/moshi) [![GitHub stars](https://img.shields.io/github/stars/square/moshi?style=flat)](https://github.com/square/moshi/stargazers) - A modern JSON library for Android and Java.
* [essential-json](https://github.com/arkanovicz/essential-json) [![GitHub stars](https://img.shields.io/github/stars/arkanovicz/essential-json?style=flat)](https://github.com/arkanovicz/essential-json/stargazers) - A lightweight Java library for serialization, parsing and manipulation with a clean and precise API.
* [dsl-json](https://github.com/ngs-doo/dsl-json) [![GitHub stars](https://img.shields.io/github/stars/ngs-doo/dsl-json?style=flat)](https://github.com/ngs-doo/dsl-json/stargazers) - A very fast streaming JSON library. Operates on byte arrays.
* [mjson](https://github.com/bolerio/mjson) [![GitHub stars](https://img.shields.io/github/stars/bolerio/mjson?style=flat)](https://github.com/bolerio/mjson/stargazers) - Lean JSON Library for Java, with a compact, elegant API.

**Javascript**
* [JSON-js](https://github.com/douglascrockford/JSON-js) [![GitHub stars](https://img.shields.io/github/stars/douglascrockford/JSON-js?style=flat)](https://github.com/douglascrockford/JSON-js/stargazers) - JSON in JavaScript.
* [JSON 3](https://bestiejs.github.io/json3/) - A modern implementation.
* [oboe.js](https://github.com/jimhigson/oboe.js) [![GitHub stars](https://img.shields.io/github/stars/jimhigson/oboe.js?style=flat)](https://github.com/jimhigson/oboe.js/stargazers) - A streaming approach, speeds up web applications by providing parsed objects before the response completes.
* [FracturedJsonJs](https://www.npmjs.com/package/fracturedjsonjs) - A JSON formatter that produces human-readable but fairly compact output.
* [JsonHilo](https://github.com/xtao-org/jsonhilo) [![GitHub stars](https://img.shields.io/github/stars/xtao-org/jsonhilo?style=flat)](https://github.com/xtao-org/jsonhilo/stargazers) - Minimal lossless parse event streaming, akin to SAX.

**Objective-C**
* [JSONKit](https://github.com/johnezang/JSONKit) [![GitHub stars](https://img.shields.io/github/stars/johnezang/JSONKit?style=flat)](https://github.com/johnezang/JSONKit/stargazers) - Objective-C library.
* [SBJson](https://github.com/SBJson/SBJson) [![GitHub stars](https://img.shields.io/github/stars/SBJson/SBJson?style=flat)](https://github.com/SBJson/SBJson/stargazers) - Parse one or more chunks of data.

**Perl**
* [JSON::Tiny](https://github.com/daoswald/JSON-Tiny) [![GitHub stars](https://img.shields.io/github/stars/daoswald/JSON-Tiny?style=flat)](https://github.com/daoswald/JSON-Tiny/stargazers) - Perl module for encoding and decoding JSON in a minimalistic way.

**PL/SQL**
* [PL/JSON](https://github.com/pljson/pljson) [![GitHub stars](https://img.shields.io/github/stars/pljson/pljson?style=flat)](https://github.com/pljson/pljson/stargazers) - A generic JSON object written in PL/SQL.

**PHP**
* [TOON PHP Lite](https://github.com/manojrammurthy/toon-php-lite) [![GitHub stars](https://img.shields.io/github/stars/manojrammurthy/toon-php-lite?style=flat)](https://github.com/manojrammurthy/toon-php-lite/stargazers) - Lightweight TOON encoder/decoder for human-readable, LLM-friendly structured data. (PHP).
* [Webmozart JSON](https://github.com/webmozart/json) [![GitHub stars](https://img.shields.io/github/stars/webmozart/json?style=flat)](https://github.com/webmozart/json/stargazers) - A robust decoder/encoder with support for schema validation.

**Python**
* [simplejson](https://github.com/simplejson/simplejson) [![GitHub stars](https://img.shields.io/github/stars/simplejson/simplejson?style=flat)](https://github.com/simplejson/simplejson/stargazers) - A simple, fast, extensible encoder/decoder
* [jsonpickle](http://jsonpickle.github.io/) - Library for serializing any arbitrary object graph.
* [metamagic.json](https://pypi.org/project/metamagic.json/) - An ultra-fast Python 3 implementation of a JSON encoder.

**Ruby**
* [oj](https://github.com/ohler55/oj) [![GitHub stars](https://img.shields.io/github/stars/ohler55/oj?style=flat)](https://github.com/ohler55/oj/stargazers) - A fast JSON parser and Object marshaller as a Ruby gem.
* [MultiJSON](https://github.com/intridea/multi_json) [![GitHub stars](https://img.shields.io/github/stars/intridea/multi_json?style=flat)](https://github.com/intridea/multi_json/stargazers) - A generic swappable back-end for JSON handling.

**React**
* [json2react](https://github.com/txgruppi/json2react) [![GitHub stars](https://img.shields.io/github/stars/txgruppi/json2react?style=flat)](https://github.com/txgruppi/json2react/stargazers) - Use JSON to create React Stateless Components.

**.NET**
* [jsonfx](https://github.com/jsonfx/jsonfx) [![GitHub stars](https://img.shields.io/github/stars/jsonfx/jsonfx?style=flat)](https://github.com/jsonfx/jsonfx/stargazers) - serialization framework for .NET.
* [jsonapi-consumer](https://github.com/OKTAYKIR/jsonapi-consumer) [![GitHub stars](https://img.shields.io/github/stars/OKTAYKIR/jsonapi-consumer?style=flat)](https://github.com/OKTAYKIR/jsonapi-consumer/stargazers) - Client framework for consuming JSONAPI based APIs on the [JSON API standard](https://jsonapi.org).

**Scala**
* [spray-json](https://github.com/spray/spray-json) [![GitHub stars](https://img.shields.io/github/stars/spray/spray-json?style=flat)](https://github.com/spray/spray-json/stargazers) - A lightweight, clean and simple implementation in Scala.
* [circe](https://github.com/circe/circe) [![GitHub stars](https://img.shields.io/github/stars/circe/circe?style=flat)](https://github.com/circe/circe/stargazers) - Yet another JSON library for Scala.
* [scala-jsonapi](https://github.com/scala-jsonapi/scala-jsonapi) [![GitHub stars](https://img.shields.io/github/stars/scala-jsonapi/scala-jsonapi?style=flat)](https://github.com/scala-jsonapi/scala-jsonapi/stargazers) - Support library for integrating the JSON:API spec with Play, Spray and/or Circe backends.
* [jsoniter-scala](https://github.com/plokhotnyuk/jsoniter-scala) [![GitHub stars](https://img.shields.io/github/stars/plokhotnyuk/jsoniter-scala?style=flat)](https://github.com/plokhotnyuk/jsoniter-scala/stargazers) - Scala macros for compile-time generation of ultra-fast JSON codecs.

**Shell**
* [jshn](https://openwrt.org/docs/guide-developer/jshn) - JSON parsing and generation library in for shell scripts (Ash/Bash)

**Swift**
* [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) [![GitHub stars](https://img.shields.io/github/stars/SwiftyJSON/SwiftyJSON?style=flat)](https://github.com/SwiftyJSON/SwiftyJSON/stargazers) - The better way to deal with data in Swift.

* [yyjson](https://github.com/ibireme/yyjson) [![GitHub stars](https://img.shields.io/github/stars/ibireme/yyjson?style=flat)](https://github.com/ibireme/yyjson/stargazers) - High performance parser and serializer in C.
## Linters
* [jsonlint](https://github.com/zaach/jsonlint) [![GitHub stars](https://img.shields.io/github/stars/zaach/jsonlint?style=flat)](https://github.com/zaach/jsonlint/stargazers) - Parser and validator with a CLI. (Javascript)
* [JSON Lint](https://github.com/Seldaek/jsonlint) [![GitHub stars](https://img.shields.io/github/stars/Seldaek/jsonlint?style=flat)](https://github.com/Seldaek/jsonlint/stargazers) - PHP linter. (PHP)

## Online tools
* [Dadroit V Web](https://dadroit.com/vweb/) - In-browser viewer for large files with tree view, RegEx search, and URL loading with auth. Fully client-side.
* [DataFormatter Pro](https://dataformatterpro.com/) - Browser-based formatter, validator, diff, and converter with a tree view.
* [JSON Blob](https://jsonblob.com/) - An online tool to view, edit, format, and share data. Also has an API for making requests against stored blobs.
* [JSON Viewer Tool](https://jsonviewertool.com/) - Online tool to view, format, validate, minify, and convert data in the browser.
* [JSONLint](https://jsonlint.com/) - The JSON Validator.
* [JSONCompare](https://jsoncompare.com/) - The Advanced Version of the JSON Linter.
* [JSONMaster](https://jsonmaster.com/) - Free online validator, formatter, minifier and viewer.
* [JSONMate](https://www.jsonmate.com/) - JSON editor, inspector and beautifier.
* [JSON Editor online](https://jsoneditoronline.org/) - A web-based tool to view, edit and format.
* [Collapsible JSON Formatter](http://www.bodurov.com/JsonFormatter/) - Formatter and Colorer of Raw Code.
* [JSON Formatter and Validator](https://jsonformatter.curiousconcept.com/) - Formatter to help with debugging.
* [JSON Generator](https://json-generator.com/) - Tool for generating random data.
* [FakeJSON](https://fakejson.com/) - Web API to quickly generate fake data for your application.
* [JSON to CSV](https://konklone.io/json/) - A free, in-browser JSON to CSV converter.
* [CSV to JSON](https://alef.website/tools/csv-to-json) - Easy, privacy-friendly and offline-first online csv to json converter
* [json2csharp](https://json2csharp.com/) - Generate c# classes from a json string or url.
* [JSON Utils](http://jsonutils.com/) - Site for generating C#, VB.Net, and Javascript classes from JSON.
* [geojson.io](https://geojson.io/) - Simply edit GeoJSON map data.
* [jq play](https://jqplay.org/) - A playground for jq.
* [json2yaml](https://www.json2yaml.com/) - Convert JSON to YAML online.
* [JSON Selector Generator](http://jsonselector.com/) - A simple GUI for generating the selectors to access.
* [JSON.fr](https://www.json.fr/) - Fully client-side validator and formatter.
* [JSONtapose](https://www.jsontapose.com/) - Intuitive, beautiful and secure client-side comparison and visualization tool.
* [jsontosdk](https://jsontosdk.vercel.app) - Paste a data sample to get typed TypeScript interfaces and a Zod schema with LLM-named types. No signup.
* [ObjGen](https://www.objgen.com/json) - Online live JSON generator.
* [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Fake Online REST API for Testing and Prototyping.
* [Extends Class](https://extendsclass.com/json-diff.html) - Diff tool to compare two files.
* [JSON Schema Validate API](https://assertible.com/json-schema-validation) - A simple and free JSON Schema Validation API.
* [JSONPerf](https://jsonperf.com) - A Visual, Unbiased and Up-to-Date JSON Performance Benchmark.
* [FracturedJson](https://j-brooke.github.io/FracturedJson/) - Formatter that produces human-readable but fairly compact output.
* [Softwium](https://softwium.com/fake-api/) - Fake and dummy REST API for testing.
* [JSONing](https://jsoning.com/) - A toolset including a formatter, comparer, JSONPath tester, patch generator, and data generator.

## Schema Specifications
* [JSON Model](https://github.com/clairey-zx81/json-model) [![GitHub stars](https://img.shields.io/github/stars/clairey-zx81/json-model?style=flat)](https://github.com/clairey-zx81/json-model/stargazers) - A lightweight featureful DSL for data modeling.
* [JSON Schema](https://json-schema.org/) - a JSON based format for defining the structure of JSON data.
* [Itemscript](https://code.google.com/archive/p/itemscript/) - Language for validating and specifying values.
* [Kwalify](https://github.com/kvs/kwalify) [![GitHub stars](https://img.shields.io/github/stars/kvs/kwalify?style=flat)](https://github.com/kvs/kwalify/stargazers) - A parser, schema validator, and data binding tool
* [Rx](https://rx.codesimply.com/) - Simple, Extensible Schemata.

## Services
* [Exchange Rate API](https://www.exchangerate-api.com) - A simple and free API for currency exchange rate data.
* [ipinfo.io](https://ipinfo.io) - JSON IP and GeoIP REST API.
* [JSONProxy](https://github.com/afeld/jsonp) [![GitHub stars](https://img.shields.io/github/stars/afeld/jsonp?style=flat)](https://github.com/afeld/jsonp/stargazers) - Simple HTTP proxy that enables cross-domain requests to any JSON API.
* [Telize](https://www.telize.com/) - JSON IP and GeoIP REST API.
* [jsonpad](https://jsonpad.io/) - a simple JSON storage platform.

## Supersets
* [YAML](https://yaml.org) - A human friendly data serialization standard for all programming languages.
* [HanSON](https://github.com/timjansen/hanson) [![GitHub stars](https://img.shields.io/github/stars/timjansen/hanson?style=flat)](https://github.com/timjansen/hanson/stargazers) - JSON for Humans - with unquoted identifiers, multi-line strings and comments.
* [μson](https://github.com/burningtree/uson) [![GitHub stars](https://img.shields.io/github/stars/burningtree/uson?style=flat)](https://github.com/burningtree/uson/stargazers) (uson) - a shorthand for JSON.
* [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md) [![GitHub stars](https://img.shields.io/github/stars/lightbend/config/blob/master/HOCON.md?style=flat)](https://github.com/lightbend/config/blob/master/HOCON.md/stargazers) - Human-Optimized Config Object Notation.
* [ASON](https://github.com/sadmac7000/libason) [![GitHub stars](https://img.shields.io/github/stars/sadmac7000/libason?style=flat)](https://github.com/sadmac7000/libason/stargazers) - A semantically complete superset of JSON (draft).
* [TOML](https://github.com/toml-lang/toml) [![GitHub stars](https://img.shields.io/github/stars/toml-lang/toml?style=flat)](https://github.com/toml-lang/toml/stargazers) - A minimal configuration file format that's easy to read due to obvious semantics.
* [HCL](https://github.com/hashicorp/hcl) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/hcl?style=flat)](https://github.com/hashicorp/hcl/stargazers) - A structured configuration language that is both human and machine friendly.

## Tutorials
* [Introducing JSON](http://json.org/)
* [JSON Tutorial](https://www.w3resource.com/JSON/introduction.php) - An introductory tutorial on JavaScript Object Notation (JSON).
* [JSON - Rosetta Code](https://rosettacode.org/wiki/JSON) - Basic operations in different languages (57 languages in this moment).
* [What is JSON and how to use it](https://ilovecoding.org/lessons/json-what-is-json-and-how-to-use-it) - Video tutorial for beginners.
* [jq Primer: Munging JSON Data](https://andrew.gibiansky.com/) - How jq can be used to process JSON files just as effectively as traditional Unix tools.

## Related formats
* [AXON](https://github.com/intellimath/pyaxon) [![GitHub stars](https://img.shields.io/github/stars/intellimath/pyaxon?style=flat)](https://github.com/intellimath/pyaxon/stargazers) - A simple text based format for interchanging of objects, documents and data. It tries to combine the best of JSON, XML and YAML.
* [CSON](https://github.com/bevry/cson) [![GitHub stars](https://img.shields.io/github/stars/bevry/cson?style=flat)](https://github.com/bevry/cson/stargazers) - CoffeeScript-Object-Notation. JSON for CoffeeScript objects.
* [MSON](https://github.com/apiaryio/mson) [![GitHub stars](https://img.shields.io/github/stars/apiaryio/mson?style=flat)](https://github.com/apiaryio/mson/stargazers) - Markdown syntax compatible with describing JSON and JSON Schema.
* [ArchieML](http://archieml.org/) - Structured text format optimized for human writability.

## Resources
* [Type-o-rama](https://github.com/stereobooster/type-o-rama) [![GitHub stars](https://img.shields.io/github/stars/stereobooster/type-o-rama?style=flat)](https://github.com/stereobooster/type-o-rama/stargazers) - JS type systems interportability, comparison of different JS type systems and conversion between them.
* [Awesome jq](https://github.com/fiatjaf/awesome-jq) [![GitHub stars](https://img.shields.io/github/stars/fiatjaf/awesome-jq?style=flat)](https://github.com/fiatjaf/awesome-jq/stargazers) - A curated list of awesome jq tools and resources.

## Templates
* [Jsonnet](https://jsonnet.org/) - A domain specific configuration language that helps you define JSON data.
* [rabl](https://github.com/nesquena/rabl) [![GitHub stars](https://img.shields.io/github/stars/nesquena/rabl?style=flat)](https://github.com/nesquena/rabl/stargazers) - General ruby templating with json, bson, xml, plist and msgpack support. (Ruby)
* [json2html](http://json2html.com/) - HTML templating library with wrappers for both jQuery and Node.js. (Javascript)

## Testing
* [JSON Test](http://www.jsontest.com/) - Testing platform for services utilizing JavaScript Object Notation (JSON).
* [JSONassert](https://github.com/skyscreamer/JSONassert) [![GitHub stars](https://img.shields.io/github/stars/skyscreamer/JSONassert?style=flat)](https://github.com/skyscreamer/JSONassert/stargazers) - Write JSON unit tests in less code. Great for testing REST interfaces. (Java)
* [JsonUnit](https://github.com/lukas-krecan/JsonUnit) [![GitHub stars](https://img.shields.io/github/stars/lukas-krecan/JsonUnit?style=flat)](https://github.com/lukas-krecan/JsonUnit/stargazers) - A library that simplifies JSON comparison in unit tests. It's strongly inspired by XmlUnit.
* [JSON Parsing Test Suite](https://github.com/nst/JSONTestSuite) [![GitHub stars](https://img.shields.io/github/stars/nst/JSONTestSuite?style=flat)](https://github.com/nst/JSONTestSuite/stargazers) - A very complete test suite and validation framework.

## Text Editor Plugins
**Emacs**
* [JSON Reformat](https://github.com/gongo/json-reformat) [![GitHub stars](https://img.shields.io/github/stars/gongo/json-reformat?style=flat)](https://github.com/gongo/json-reformat/stargazers) - Reformat tool.

**Vim**
* [vim-json](https://github.com/elzr/vim-json) [![GitHub stars](https://img.shields.io/github/stars/elzr/vim-json?style=flat)](https://github.com/elzr/vim-json/stargazers) - A better JSON for Vim: distinct highlighting of keywords vs values, JSON-specific (non-JS) warnings, quote concealing. Pathogen-friendly.

**Visual Studio Code**

**Neovim**
* [nvim-jqx](https://github.com/gennaro-tedesco/nvim-jqx) [![GitHub stars](https://img.shields.io/github/stars/gennaro-tedesco/nvim-jqx?style=flat)](https://github.com/gennaro-tedesco/nvim-jqx/stargazers) - Browse and query json files in neovim from the quickfix window. (Lua)

## Transformations
* [json-sharp](https://github.com/globocom/json-sharp) [![GitHub stars](https://img.shields.io/github/stars/globocom/json-sharp?style=flat)](https://github.com/globocom/json-sharp/stargazers) - Javascript tool to process operations on pure JSON objects. (Javascript)
* [json2json](https://github.com/joelvh/json2json) [![GitHub stars](https://img.shields.io/github/stars/joelvh/json2json?style=flat)](https://github.com/joelvh/json2json/stargazers) - Transform (reformat) structures from one to another. (Javascript)
* [trans](https://github.com/gabesoft/trans) [![GitHub stars](https://img.shields.io/github/stars/gabesoft/trans?style=flat)](https://github.com/gabesoft/trans/stargazers) - The ultimate object transformer. (Javascript)
* [osmtogeojson](https://github.com/tyrasd/osmtogeojson) [![GitHub stars](https://img.shields.io/github/stars/tyrasd/osmtogeojson?style=flat)](https://github.com/tyrasd/osmtogeojson/stargazers) - Converts OSM data to GeoJSON. (Javascript)
* [fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser) [![GitHub stars](https://img.shields.io/github/stars/NaturalIntelligence/fast-xml-parser?style=flat)](https://github.com/NaturalIntelligence/fast-xml-parser/stargazers) - Fast XML to JSON and vice versa javascript/JSON conversion.
* [x2js](https://github.com/abdolence/x2js) [![GitHub stars](https://img.shields.io/github/stars/abdolence/x2js?style=flat)](https://github.com/abdolence/x2js/stargazers) - XML to JSON and vice versa javascript conversion functions. (Javascript)
* [JSONC](https://github.com/tcorral/JSONC) [![GitHub stars](https://img.shields.io/github/stars/tcorral/JSONC?style=flat)](https://github.com/tcorral/JSONC/stargazers) - JSON compressor and decompressor. (Javascript)
* [JsonMapper](https://github.com/cweiske/jsonmapper) [![GitHub stars](https://img.shields.io/github/stars/cweiske/jsonmapper?style=flat)](https://github.com/cweiske/jsonmapper/stargazers) - Map nested structures onto PHP classes (PHP)
* [SassyJSON](https://github.com/KittyGiraudel/SassyJSON) [![GitHub stars](https://img.shields.io/github/stars/KittyGiraudel/SassyJSON?style=flat)](https://github.com/KittyGiraudel/SassyJSON/stargazers) - Sass-powered API. (Sass)
* [json.human.js](http://marianoguerra.github.io/json.human.js/) - A small library to convert a JSON object into a human readable HTML representation that is easy to style for different purposes.
* [fanci](https://github.com/liip/fanci) [![GitHub stars](https://img.shields.io/github/stars/liip/fanci?style=flat)](https://github.com/liip/fanci/stargazers) - Extract, rename and transform JSON based on a template. (node.js)
* [deepjson](https://www.npmjs.com/package/deepjson/) - A better way to load big json config files. (node.js)
* [jsontl](https://github.com/DoublePrecisionSoftware/jsontl) [![GitHub stars](https://img.shields.io/github/stars/DoublePrecisionSoftware/jsontl?style=flat)](https://github.com/DoublePrecisionSoftware/jsontl/stargazers) - allow transformation using a JSON-based transformation language. (node.js)
* [json-transforms](https://github.com/ColinEberhardt/json-transforms) [![GitHub stars](https://img.shields.io/github/stars/ColinEberhardt/json-transforms?style=flat)](https://github.com/ColinEberhardt/json-transforms/stargazers) - A recursive, pattern-matching, approach to transforming JSON structures.
* [normalizr](https://github.com/paularmstrong/normalizr) [![GitHub stars](https://img.shields.io/github/stars/paularmstrong/normalizr?style=flat)](https://github.com/paularmstrong/normalizr/stargazers) - Normalizes nested JSON according to a schema. (Javascript)
* [JSON-populate](https://github.com/eiriklv/json-populate) [![GitHub stars](https://img.shields.io/github/stars/eiriklv/json-populate?style=flat)](https://github.com/eiriklv/json-populate/stargazers) - Tool for populating JSON data with infinitely recursive circular references. Sort of like Falcor, but for plain JSON.
* [CircularJSON](https://github.com/WebReflection/circular-json) [![GitHub stars](https://img.shields.io/github/stars/WebReflection/circular-json?style=flat)](https://github.com/WebReflection/circular-json/stargazers) - JSON does not handle circular references. Now it does.
* [Sawmill](https://github.com/logzio/sawmill) [![GitHub stars](https://img.shields.io/github/stars/logzio/sawmill?style=flat)](https://github.com/logzio/sawmill/stargazers) - JSON transformation library (Java)
* [nimnjs](https://github.com/NaturalIntelligence/nimnjs) [![GitHub stars](https://img.shields.io/github/stars/NaturalIntelligence/nimnjs?style=flat)](https://github.com/NaturalIntelligence/nimnjs/stargazers) - JSON to nimn bidirectional converter.
* [stylops](https://github.com/cruel-intentions/stylops) [![GitHub stars](https://img.shields.io/github/stars/cruel-intentions/stylops?style=flat)](https://github.com/cruel-intentions/stylops/stargazers) - CSS subset to JSON conversion. (node.js)

## Queries
* [dasel](https://github.com/tomwright/dasel) [![GitHub stars](https://img.shields.io/github/stars/tomwright/dasel?style=flat)](https://github.com/tomwright/dasel/stargazers) - Query and update data structures using selectors from the command line. Comparable to [jq](https://github.com/jqlang/jq) [![GitHub stars](https://img.shields.io/github/stars/jqlang/jq?style=flat)](https://github.com/jqlang/jq/stargazers) / [yq](https://github.com/kislyuk/yq) [![GitHub stars](https://img.shields.io/github/stars/kislyuk/yq?style=flat)](https://github.com/kislyuk/yq/stargazers) but supports JSON, YAML, TOML and XML with zero runtime dependencies.
* [JMESPath](https://jmespath.org/) - A query language for JSON.
* [JSON Mask](https://github.com/nemtsov/json-mask) [![GitHub stars](https://img.shields.io/github/stars/nemtsov/json-mask?style=flat)](https://github.com/nemtsov/json-mask/stargazers) - Tiny language and engine for selecting specific parts of a JS object, hiding the rest. (Javascript)
* [JSONiq](https://www.jsoniq.org/) - The JSON Query Language.
* [ObjectPath](https://objectpath.org/) - The agile query language for semi-structured data. (Python)
* [DefiantJS](https://www.defiantjs.com/) - Lightning-fast searches using XPath expressions, and transform using XSL. (Javascript)
* [JSONSelect](https://github.com/lloyd/JSONSelect) [![GitHub stars](https://img.shields.io/github/stars/lloyd/JSONSelect?style=flat)](https://github.com/lloyd/JSONSelect/stargazers) - CSS-like selectors. (Javascript)
* [JSONPath](https://goessner.net/articles/JsonPath/) - XPath implementation. (Javascript/PHP)
* [searchjs](https://github.com/deitch/searchjs) [![GitHub stars](https://img.shields.io/github/stars/deitch/searchjs?style=flat)](https://github.com/deitch/searchjs/stargazers) - A library for filtering based on a json SQL-like language.
* [json-rel](https://github.com/slurmulon/json-where) [![GitHub stars](https://img.shields.io/github/stars/slurmulon/json-where?style=flat)](https://github.com/slurmulon/json-where/stargazers) - Transparent references in JSON.
* [JSONata](https://jsonata.org/) - Query and transformation language used in Node-RED, supports function expressions.

## JSON Schema Frontend components
* [JSON Editor](https://github.com/jdorn/json-editor) [![GitHub stars](https://img.shields.io/github/stars/jdorn/json-editor?style=flat)](https://github.com/jdorn/json-editor/stargazers) - JSON Schema Based Editor. (jQuery)
* [angular-schema-form](https://github.com/json-schema-form/angular-schema-form) [![GitHub stars](https://img.shields.io/github/stars/json-schema-form/angular-schema-form?style=flat)](https://github.com/json-schema-form/angular-schema-form/stargazers) - Generate forms. (AngularJS)
* [JSON Schema View](https://github.com/mohsen1/json-schema-view) [![GitHub stars](https://img.shields.io/github/stars/mohsen1/json-schema-view?style=flat)](https://github.com/mohsen1/json-schema-view/stargazers) - An AngularJS directive for rendering JSON Schema in HTML (AngularJS)
* [Angular JSON Schema Form](https://github.com/mohsen1/angular-json-schema-form) [![GitHub stars](https://img.shields.io/github/stars/mohsen1/angular-json-schema-form?style=flat)](https://github.com/mohsen1/angular-json-schema-form/stargazers) - Angular directive for making forms out of JSON Schema. (AngularJS)
* [AlpacaJS](http://www.alpacajs.org) - Generates JSON Schema driven forms on top of Bootstrap, jQuery Mobile, jQuery UI and HTML (jQuery)

## JSON Schema Tools
* [JSON Schema CLI](https://github.com/intelligence-ai/jsonschema) [![GitHub stars](https://img.shields.io/github/stars/intelligence-ai/jsonschema?style=flat)](https://github.com/intelligence-ai/jsonschema/stargazers) - Command-line interface for formatting, linting, testing, bundling, and validating schema files for local development and CI/CD pipelines.
* [prmd](https://github.com/interagent/prmd) [![GitHub stars](https://img.shields.io/github/stars/interagent/prmd?style=flat)](https://github.com/interagent/prmd/stargazers) - Tools and doc generation for HTTP APIs.
* [generate-schema](https://github.com/Nijikokun/generate-schema) [![GitHub stars](https://img.shields.io/github/stars/Nijikokun/generate-schema?style=flat)](https://github.com/Nijikokun/generate-schema/stargazers) - Effortlessly convert your JSON Object to JSON Schema, Mongoose Schema, or a Generic template for quick documentation / upstart.
* [Docson](https://github.com/lbovet/docson) [![GitHub stars](https://img.shields.io/github/stars/lbovet/docson?style=flat)](https://github.com/lbovet/docson/stargazers) - Documentation for your types.
* [Orderly JSON](https://github.com/lloyd/orderly) [![GitHub stars](https://img.shields.io/github/stars/lloyd/orderly?style=flat)](https://github.com/lloyd/orderly/stargazers) - A textual format for describing JSON compiled into JSONSchema.
* [jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo) [![GitHub stars](https://img.shields.io/github/stars/joelittlejohn/jsonschema2pojo?style=flat)](https://github.com/joelittlejohn/jsonschema2pojo/stargazers) - Generates Java types and annotates those types for data-binding with Jackson 1.x or 2.x, Gson, etc.
* [Matic](https://github.com/mattyod/matic) [![GitHub stars](https://img.shields.io/github/stars/mattyod/matic?style=flat)](https://github.com/mattyod/matic/stargazers) - Build tool for generating HTML documentation.
* [JSON Schema + Faker](https://github.com/json-schema-faker/json-schema-faker) [![GitHub stars](https://img.shields.io/github/stars/json-schema-faker/json-schema-faker?style=flat)](https://github.com/json-schema-faker/json-schema-faker/stargazers) - Fake your schemas.
* [DLL.js](https://github.com/moll/js-ddl) [![GitHub stars](https://img.shields.io/github/stars/moll/js-ddl?style=flat)](https://github.com/moll/js-ddl/stargazers) - Gets you a JSON Schema from PostgreSQL or SQLite3.
* [js-schema](https://github.com/molnarg/js-schema) [![GitHub stars](https://img.shields.io/github/stars/molnarg/js-schema?style=flat)](https://github.com/molnarg/js-schema/stargazers) - A new way of describing object schemas in JavaScript. It has a clean and simple syntax, and it is capable of serializing to/from the popular JSON Schema format.
* [JSON Schema $Ref Parser](https://github.com/APIDevTools/json-schema-ref-parser) [![GitHub stars](https://img.shields.io/github/stars/APIDevTools/json-schema-ref-parser?style=flat)](https://github.com/APIDevTools/json-schema-ref-parser/stargazers) - Parse, resolve, and dereference JSON Schema $ref pointers

## JSON Schema Resources
* [Learn JSON Schema](https://www.learnjsonschema.com) - Open-source reference documentation for the schema specification.
* [Understanding JSON Schema](https://spacetelescope.github.io/understanding-json-schema/) - A website aiming to provide more accessible documentation for JSON schema.
* [Using JSON Schema](http://usingjsonschema.com/) - a Book and GitHub project, showing how JSON Schema can be used for a variety of tasks and in different programming contexts.
* [Awesome JSON Schema](https://github.com/sourcemeta/awesome-jsonschema) [![GitHub stars](https://img.shields.io/github/stars/sourcemeta/awesome-jsonschema?style=flat)](https://github.com/sourcemeta/awesome-jsonschema/stargazers) - A curated list of awesome JSON Schema resources, tutorials, tools, and more.

## JSON Schema Validators
**Javascript and Node.js**
* [json-schema-benchmark](https://github.com/ebdrup/json-schema-benchmark) [![GitHub stars](https://img.shields.io/github/stars/ebdrup/json-schema-benchmark?style=flat)](https://github.com/ebdrup/json-schema-benchmark/stargazers) - Performance benchmark for Node.js validators.
* [is-my-json-valid](https://github.com/mafintosh/is-my-json-valid) [![GitHub stars](https://img.shields.io/github/stars/mafintosh/is-my-json-valid?style=flat)](https://github.com/mafintosh/is-my-json-valid/stargazers) - A validator that uses code generation to be extremely fast.
* [jsen](https://github.com/bugventure/jsen) [![GitHub stars](https://img.shields.io/github/stars/bugventure/jsen?style=flat)](https://github.com/bugventure/jsen/stargazers) - A validator built for speed.
* [themis](https://github.com/playlyfe/themis) [![GitHub stars](https://img.shields.io/github/stars/playlyfe/themis?style=flat)](https://github.com/playlyfe/themis/stargazers) - A blazing fast validator.
* [jsck](https://github.com/pandastrike/jsck) [![GitHub stars](https://img.shields.io/github/stars/pandastrike/jsck?style=flat)](https://github.com/pandastrike/jsck/stargazers) - JSON Schema Compiled checK.
* [z-schema](https://github.com/zaggino/z-schema) [![GitHub stars](https://img.shields.io/github/stars/zaggino/z-schema?style=flat)](https://github.com/zaggino/z-schema/stargazers) - validator written in JavaScript for NodeJS and Browsers.
* [jjv](https://github.com/acornejo/jjv) [![GitHub stars](https://img.shields.io/github/stars/acornejo/jjv?style=flat)](https://github.com/acornejo/jjv/stargazers) - Javascript Library for Schema Validation.
* [request-validator](https://github.com/bugventure/request-validator) [![GitHub stars](https://img.shields.io/github/stars/bugventure/request-validator?style=flat)](https://github.com/bugventure/request-validator/stargazers) - Flexible request validator middleware for express and connect.
* [tv4](https://github.com/geraintluff/tv4) [![GitHub stars](https://img.shields.io/github/stars/geraintluff/tv4?style=flat)](https://github.com/geraintluff/tv4/stargazers) - Tiny Validator.
* [ajv](https://github.com/ajv-validator/ajv) [![GitHub stars](https://img.shields.io/github/stars/ajv-validator/ajv?style=flat)](https://github.com/ajv-validator/ajv/stargazers) - The fastest schema validator. Supports draft-04/06/07/2019-09/2020-12.

**Java and Kotlin**
* [Medeia Validator](https://github.com/worldturner/medeia-validator) [![GitHub stars](https://img.shields.io/github/stars/worldturner/medeia-validator?style=flat)](https://github.com/worldturner/medeia-validator/stargazers) - Compliant (draft-04/06/07) and fast streaming validator written in Kotlin

**PHP**
* [JSON Schema for PHP](https://github.com/justinrainbow/json-schema) [![GitHub stars](https://img.shields.io/github/stars/justinrainbow/json-schema?style=flat)](https://github.com/justinrainbow/json-schema/stargazers) - PHP implementation of JSON schema.
* [JSON Guard](https://json-guard.thephpleague.com) - A validator for JSON Schema Draft 4.

**Python**
* [jsonschema](https://github.com/python-jsonschema/jsonschema) [![GitHub stars](https://img.shields.io/github/stars/python-jsonschema/jsonschema?style=flat)](https://github.com/python-jsonschema/jsonschema/stargazers) - Python implementation of jsonschema.
* [JSON Schema Toolkit](https://github.com/petrounias/json-schema-toolkit) [![GitHub stars](https://img.shields.io/github/stars/petrounias/json-schema-toolkit?style=flat)](https://github.com/petrounias/json-schema-toolkit/stargazers) - Programmatic building of JSON schemas (recursive field mappings) with validation, a Django JSON Field, and native PostgreSQL JSON type constraints.

**Ruby**
* [Ruby JSON Schema Validator](https://github.com/voxpupuli/json-schema) [![GitHub stars](https://img.shields.io/github/stars/voxpupuli/json-schema?style=flat)](https://github.com/voxpupuli/json-schema/stargazers) - validating against a JSON schema conforming to JSON Schema Draft 4.

## Contribute
Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
