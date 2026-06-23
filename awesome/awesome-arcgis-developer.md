# ArcGIS Developer

[![GitHub stars](https://img.shields.io/github/stars/Esri/awesome-arcgis-developer?style=flat)](https://github.com/Esri/awesome-arcgis-developer/stargazers)

<!--lint disable double-link-->
# Awesome ArcGIS Developers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable match-punctuation-->
<img src="esri-logo.png" align="right" width="100">

> An awesome set of resources to help you [develop with ArcGIS Products](https://www.esri.com/en-us/arcgis/products/develop-with-arcgis/overview).

ArcGIS products give you access to APIs, location services, and tools to develop your own mapping and spatial analysis applications. Use mapping products to help developers build web, native, offline, desktop, or integrated solutions for yourself, your organization, or other organizations. Access a full suite of location services to provide basemap layers, geocoding and routing capabilities, and other geospatial functionalities. Securely host and manage your data in the ArcGIS cloud.

---

## Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [APIs and SDKs](#apis-and-sdks)
- [Application generators and CLIs](#application-generators-and-clis)
- [ArcGIS location services](#arcgis-location-services)
- [Code samples and snippets](#code-samples-and-snippets)
- [Data conversion tools](#data-conversion-tools)
- [Data integration tools](#data-integration-tools)
- [Debugging tools](#debugging-tools)
- [Design and styling](#design-and-styling)
- [Developer guides](#developer-guides)
- [Helpers](#helpers)
- [Map and data exploration](#map-and-data-exploration)
- [Playgrounds](#playgrounds)
- [Spatial Analysis](#spatial-analysis)
- [Specifications](#specifications)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

## APIs and SDKs

- ArcGIS Core APIs & Libraries:
	- [ArcGIS API for Python](https://developers.arcgis.com/python/) - Guides, sample notebooks, and API reference to do mapping, spatial analysis, data science, geospatial AI, and automation using Python.
	- [ArcGIS REST APIs](https://developers.arcgis.com/rest/) - General documentation about ArcGIS REST APIs: location services, content management, portal administration, and more.
	- [ArcGIS REST APIs collections](https://github.com/esri-es/ArcGIS-REST-API) [![GitHub stars](https://img.shields.io/github/stars/esri-es/ArcGIS-REST-API?style=flat)](https://github.com/esri-es/ArcGIS-REST-API/stargazers) - Postman collections to work with some of the REST APIs: location services, hosted feature layers, ArcGIS Online, ArcGIS Hub, etc.
	- [ArcGIS REST JS](https://developers.arcgis.com/arcgis-rest-js/) - Key concepts, tutorials, and API reference of a collection of JavaScript modules for accessing location services, ArcGIS Online, and ArcGIS Enterprise REST APIs.
	- [ArcGIS Urban API](https://developers.arcgis.com/arcgis-urban-api/) - Public GraphQL web service that can be used to interact with ArcGIS Urban data directly.
	- [ArcPy](https://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm) - Documentation about the Python package to perform geographic data analysis, data conversion, data management, and map automation in ArcGIS Desktop or ArcGIS Enterprise environments.

- Esri Client-side SDKs:
	- [ArcGIS Maps SDK for .NET](https://developers.arcgis.com/net/) - Guides, sample codes, and API reference to build desktop and mobile apps using .NET.
	- [ArcGIS Maps SDK for Flutter](https://developers.arcgis.com/flutter/) - Guides, sample codes, and API reference to build desktop and mobile apps using Flutter.
	- [ArcGIS Maps SDK for JavaScript](https://developers.arcgis.com/javascript/latest/) - Guides, sample code, API references, and showcase to build 2D and 3D interactive web apps unlocking geospatial data.
	- [ArcGIS Maps SDK for Kotlin](https://developers.arcgis.com/kotlin/) - Guides, sample codes, and API reference to build mobile apps using Kotlin.
	- [ArcGIS Maps SDK for Qt](https://developers.arcgis.com/qt/) - Guides, sample codes, and API reference to build mobile and desktop apps.
	- [ArcGIS Maps SDK for Swift](https://developers.arcgis.com/swift/) - Guides, sample codes, and API reference to build mobile apps using Swift.
	- [ArcGIS Maps SDK for Unity](https://developers.arcgis.com/unity/) - Guides, API reference, and sample code to use ArcGIS data and services to develop for Unity.
	- [ArcGIS Maps SDK for Unreal Engine](https://developers.arcgis.com/unreal-engine/) - Guides, API reference, and sample code to use ArcGIS data and services to develop for Unreal Engine.

- Integrations & Plugins (third-party libraries):
	- [ArcGIS integrations with CesiumJS](https://developers.arcgis.com/cesiumjs/) - Guide and tutorials to help you start build mapping applications with CesiumJS and ArcGIS.
	- [ArcGIS integrations with MapLibre GL JS](https://developers.arcgis.com/maplibre-gl-js/maplibre-arcgis-plugin/) - Learn how to connect MapLibre GL JS apps with ArcGIS services using the Esri-maintained ArcGIS MapLibre plugin and ArcGIS REST JS, including tutorials, API references, and sample code.
	- [ArcGIS integrations with OpenLayers](https://developers.arcgis.com/openlayers/) - Guide and tutorials to help you start building web apps with OpenLayers and ArcGIS location services.
	- [ArcGIS integrations with Leaflet](https://developers.arcgis.com/esri-leaflet/) - Learn how to connect Leaflet apps with ArcGIS services using the Esri-maintained Esri Leaflet plugin and ArcGIS REST JS, including tutorials, API references, and sample code.
	- [Esri-gl](https://github.com/muimsd/esri-gl) [![GitHub stars](https://img.shields.io/github/stars/muimsd/esri-gl?style=flat)](https://github.com/muimsd/esri-gl/stargazers) - A community-maintained plugin that enables the use of ArcGIS services in Mapbox GL JS and MapLibre GL JS applications.

- SDKs for Extending ArcGIS Products:
	- [ArcGIS CityEngine SDKs (C++)](https://github.com/esri/cityengine-sdk) [![GitHub stars](https://img.shields.io/github/stars/esri/cityengine-sdk?style=flat)](https://github.com/esri/cityengine-sdk/stargazers) - C++ APIs, documentation, and examples for the Procedural Runtime (PRT).
	- [ArcGIS CityEngine SDKs (Python)](https://github.com/Esri/pyprt) [![GitHub stars](https://img.shields.io/github/stars/Esri/pyprt?style=flat)](https://github.com/Esri/pyprt/stargazers) - Python bindings for the *Procedural Runtime* (PRT) of CityEngine.
	- [ArcGIS Earth Automation API](https://doc.arcgis.com/en/arcgis-earth/automation-api/get-started.htm) - Guide, API reference, and samples to communicate with ArcGIS Earth.
	- [ArcGIS Enterprise SDK](https://developers.arcgis.com/enterprise-sdk/) - Guides, API reference, and sample code to extend ArcGIS Enterprise.
	- [ArcGIS Pro SDK for Microsoft .NET](https://pro.arcgis.com/en/pro-app/latest/sdk/) - Documentation, tutorials, API reference, FAQ, etc. to extend ArcGIS Pro Desktop.

- Legacy SDKs:
	- [ArcGIS Maps SDK for Java](https://developers.arcgis.com/java/) - Guides, sample codes, and API reference to build desktop apps.
	- [ArcObjects SDK for .NET](https://desktop.arcgis.com/en/arcobjects/latest/net/webframe.htm#RoadmapToExtendingArcObjects.htm) - Documentation about the .NET SDK for the library of Component Object Model (COM) components that make up the foundation of ArcGIS.
	- [ArcObjects SDK for Java](https://desktop.arcgis.com/en/arcobjects/latest/java/#80146cac-6b50-4c82-a9f5-7a5be3406c5b.htm) - Documentation about the Java SDK for the library of Component Object Model (COM) components that make up the foundation of ArcGIS.

## Application generators and CLIs

- [@arcgis/cli](https://github.com/Esri/arcgis-js-cli) [![GitHub stars](https://img.shields.io/github/stars/Esri/arcgis-js-cli?style=flat)](https://github.com/Esri/arcgis-js-cli/stargazers) - Quickly scaffold various applications for the ArcGIS API for JavaScript.
- [generator-esri-appbuilder-js](https://github.com/Esri/generator-esri-appbuilder-js) [![GitHub stars](https://img.shields.io/github/stars/Esri/generator-esri-appbuilder-js?style=flat)](https://github.com/Esri/generator-esri-appbuilder-js/stargazers) - Yeoman generator to help customize Esri's Web AppBuilder.
- [koop-cli](https://github.com/koopjs/koop-cli) [![GitHub stars](https://img.shields.io/github/stars/koopjs/koop-cli?style=flat)](https://github.com/koopjs/koop-cli/stargazers) - Tool to scaffold Koop applications and plugins.

## ArcGIS location services

- [ArcGIS location services Postman Workspace](https://www.postman.com/esridevs/workspace/arcgis-location-services) - Postman collections to facilitate work with many of the location services.
- [Basemap styles service (v1)](https://developers.arcgis.com/documentation/mapping-apis-and-services/maps/services/basemap-layer-service/) - Access streets, satellite, and other basemap styles for maps and scenes.
- [Basemap styles service (v2)](https://developers.arcgis.com/rest/basemap-styles/) - Access multiple map styles, add places of interest, set label languages, word views, and more.
- [Places service](https://developers.arcgis.com/rest/places/) - Search for businesses and geographic locations around the world with detailed information about each place.
- [Elevation service](https://developers.arcgis.com/documentation/mapping-and-location-services/elevation/) - Get the vertical distance (height) of a location above or below the mean sea level or ground level.
- [Hydrology analysis service](https://developers.arcgis.com/rest/elevation-analysis/hydrology-analysis-service/) - Trace water flow and generate watersheds.
- [Geocoding service](https://developers.arcgis.com/documentation/mapping-apis-and-services/search/services/geocoding-service/) - Search for addresses, businesses, and places around the world.
- [GeoEnrichment service](https://developers.arcgis.com/documentation/mapping-apis-and-services/demographics/services/geoenrichment-service/) - Find facts and demographic information about a location or area.
- [Routing service](https://developers.arcgis.com/documentation/mapping-apis-and-services/routing/services/routing-service/) - Get turn-by-turn directions and solve advanced routing problems.
- [Printing tools service](https://developers.arcgis.com/rest/services-reference/enterprise/export-web-map-task.htm) - Generate static maps (png, jpg, pdf, etc.) from advanced web maps.
<!--lint disable double-link-->
- [Spatial analysis service](https://developers.arcgis.com/rest/analysis/) - Process spatial datasets to discover relationships and patterns.
- [Offline packaging service](https://developers.arcgis.com/rest/packaging/api-reference/create-map-area.htm) - Create and manage preplanned map areas for generating offline maps.

## Code samples and snippets

- [ArcGIS Code Sharing](http://codesharing.arcgis.com/) - Search, browse, and use code, scripts, models, add-ins, widgets, and more.
- [Esri/developer-support](https://github.com/Esri/developer-support) [![GitHub stars](https://img.shields.io/github/stars/Esri/developer-support?style=flat)](https://github.com/Esri/developer-support/stargazers) - Community samples to help be successful with all ArcGIS developer products (Python, .NET, JavaScript, Android…).
- [esrinederland/CoolScripts](https://github.com/esrinederland/CoolScripts) [![GitHub stars](https://img.shields.io/github/stars/esrinederland/CoolScripts?style=flat)](https://github.com/esrinederland/CoolScripts/stargazers) - Esri Netherlands scripts and snippets for reuse.
- [Esri Germany Github organization](https://github.com/EsriDE) [![GitHub stars](https://img.shields.io/github/stars/EsriDE?style=flat)](https://github.com/EsriDE/stargazers): code samples, tools and more by Esri Deutschland.
- [EsriJapan/arcgis-dev-resources](https://github.com/EsriJapan/arcgis-dev-resources) [![GitHub stars](https://img.shields.io/github/stars/EsriJapan/arcgis-dev-resources?style=flat)](https://github.com/EsriJapan/arcgis-dev-resources/stargazers) - ArcGIS Developers 開発リソース集 (by Esri Japan).
- .NET:
  	- [ArcGIS Maps SDK for .NET MAUI samples](https://developers.arcgis.com/net/maui/sample-code/) - Esri's official ArcGIS Maps SDK MAUI product team samples.
	- [ArcGIS Maps SDK for .NET UWP samples](https://developers.arcgis.com/net/uwp/sample-code/) - Esri's official ArcGIS Maps SDK for .NET product team samples.
 	- [ArcGIS Maps SDK for .NET WinUI samples](https://developers.arcgis.com/net/winui/sample-code/) - Esri's official ArcGIS Maps SDK for .NET product team samples.
	- [ArcGIS Maps SDK for .NET WPF samples](https://developers.arcgis.com/net/wpf/sample-code/) - Esri's official ArcGIS Maps SDK for .NET product team samples.
- Android:
	- [ArcGIS Maps SDK for Kotlin samples](https://developers.arcgis.com/kotlin/sample-code/) - Esri's official ArcGIS Maps SDK for Kotlin product team samples for Kotlin.
- Arcade:
  - [ArcGIS Arcade Expression Templates](https://github.com/Esri/arcade-expressions) [![GitHub stars](https://img.shields.io/github/stars/Esri/arcade-expressions?style=flat)](https://github.com/Esri/arcade-expressions/stargazers) - Collection of reusable Arcade expressions across all supported profiles.
- iOS:
	- [ArcGIS Maps SDK for iOS sample code](https://developers.arcgis.com/ios/swift/sample-code/) - Esri's official ArcGIS Maps SDK for iOS product team samples.
- JavaScript:
	- [ArcGIS API for JavaScript Sample Code](https://developers.arcgis.com/javascript/latest/sample-code/) - Esri's official JavaScript API product team samples.
	- [ArcGIS REST JS demos](https://github.com/Esri/arcgis-rest-js/tree/master/demos) [![GitHub stars](https://img.shields.io/github/stars/Esri/arcgis-rest-js/tree/master/demos?style=flat)](https://github.com/Esri/arcgis-rest-js/tree/master/demos/stargazers) - Demo apps built by Esri's REST JS maintainers.
	- [arcgis-js-api-starter-apps](https://github.com/hhkaos/arcgis-js-api-starter-apps) [![GitHub stars](https://img.shields.io/github/stars/hhkaos/arcgis-js-api-starter-apps?style=flat)](https://github.com/hhkaos/arcgis-js-api-starter-apps/stargazers) - Collection of boilerplates to get started with the ArcGIS API for JavaScript 4.x.
	- [Esri/arcgis-js-vscode-snippets](https://github.com/Esri/arcgis-js-vscode-snippets) [![GitHub stars](https://img.shields.io/github/stars/Esri/arcgis-js-vscode-snippets?style=flat)](https://github.com/Esri/arcgis-js-vscode-snippets/stargazers) - Collection of Visual Studio Code snippets for common code patterns for the ArcGIS API for JavaScript.
	- [Esri/jsapi-resources](https://github.com/Esri/jsapi-resources) [![GitHub stars](https://img.shields.io/github/stars/Esri/jsapi-resources?style=flat)](https://github.com/Esri/jsapi-resources/stargazers) - A collection of resources for developers using the ArcGIS API for JavaScript.
	- [RalucaNicola/code-snippets-arcgis-api-js](https://github.com/RalucaNicola/code-snippets-arcgis-api-js) [![GitHub stars](https://img.shields.io/github/stars/RalucaNicola/code-snippets-arcgis-api-js?style=flat)](https://github.com/RalucaNicola/code-snippets-arcgis-api-js/stargazers) - A collection of code snippets for ArcGIS API for JavaScript.
- Python:
	- [ArcGIS API for Python Sample Notebooks](https://developers.arcgis.com/python/sample-notebooks/) - Esri's official Python API product team samples.
	- [esrinederland/CoolMaps](https://github.com/esrinederland/CoolMaps) [![GitHub stars](https://img.shields.io/github/stars/esrinederland/CoolMaps?style=flat)](https://github.com/esrinederland/CoolMaps/stargazers) - Shows cool example maps you can use.
- Qt:
	- [ArcGIS Maps SDK for Qt C++ sample code](https://developers.arcgis.com/qt/cpp/sample-code/) - Esri's official ArcGIS Maps SDK for Qt product team samples for C++.
- Unity:
  - [ArcGIS Maps SDK for Unity samples](https://developers.arcgis.com/unity/sample-code/) - Esri's official ArcGIS Maps SDK for Unity product team samples.
- Unreal:
  - [ArcGIS Maps SDK for Unreal Engine samples](https://developers.arcgis.com/unreal-engine/sample-code/) - Esri's official ArcGIS Maps SDK for Unreal Engine product team samples.

## Data conversion tools

- Core geospatial processing libraries:
  - [ArcPy](https://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm) - Python interface to the ArcGIS geoprocessing framework for automating spatial analysis, data management, and mapping.
  - [gdal](https://github.com/OSGeo/gdal) [![GitHub stars](https://img.shields.io/github/stars/OSGeo/gdal?style=flat)](https://github.com/OSGeo/gdal/stargazers) - Translator library for raster and vector geospatial data formats.
  - [loam](https://github.com/azavea/loam) [![GitHub stars](https://img.shields.io/github/stars/azavea/loam?style=flat)](https://github.com/azavea/loam/stargazers) - JavaScript wrapper for GDAL in the browser.
- Format conversion:
  - [arcgis-json-to-geojson](https://github.com/gavinr/arcgis-json-to-geojson) [![GitHub stars](https://img.shields.io/github/stars/gavinr/arcgis-json-to-geojson?style=flat)](https://github.com/gavinr/arcgis-json-to-geojson/stargazers) - Convert layer in ArcGIS JSON spec to GeoJSON spec.
  - [csv2geojson](https://viglino.github.io/ol-ext/examples/misc/csv2geojson.html) - Convert points from CSV format to GeoJSON.
  - [geojson2svg](https://github.com/w8r/geojson2svg) [![GitHub stars](https://img.shields.io/github/stars/w8r/geojson2svg?style=flat)](https://github.com/w8r/geojson2svg/stargazers) - Render GeoJSON into SVG using an inline or external stylesheet.
  - [geojsonio](https://github.com/ropensci/geojsonio) [![GitHub stars](https://img.shields.io/github/stars/ropensci/geojsonio?style=flat)](https://github.com/ropensci/geojsonio/stargazers) - Convert many data formats to and from GeoJSON and TopoJSON.
  - [gtfs2geojson](https://github.com/node-geojson/gtfs2geojson) [![GitHub stars](https://img.shields.io/github/stars/node-geojson/gtfs2geojson?style=flat)](https://github.com/node-geojson/gtfs2geojson/stargazers) - Convert GTFS data into GeoJSON.
  - [img2geojson](https://github.com/caseymm/img2geojson/) [![GitHub stars](https://img.shields.io/github/stars/caseymm/img2geojson/?style=flat)](https://github.com/caseymm/img2geojson//stargazers) - Drag an image onto a map, trace the paths you need, and export as GeoJSON.
  - [terraformer](https://github.com/terraformer-js/terraformer) [![GitHub stars](https://img.shields.io/github/stars/terraformer-js/terraformer?style=flat)](https://github.com/terraformer-js/terraformer/stargazers) - Convert ArcGIS JSON to and from GeoJSON, convert WKT geometries to and from GeoJSON geometries, and other formats.
  - [togeojson](https://mapbox.github.io/togeojson/) - Convert KML and GPX to GeoJSON, without the fuss.
  - [tokml](https://github.com/mapbox/tokml) [![GitHub stars](https://img.shields.io/github/stars/mapbox/tokml?style=flat)](https://github.com/mapbox/tokml/stargazers) - Convert GeoJSON to KML.
- Simplification and generalization:
  - [Distillery](http://shancarter.github.io/distillery/) - Web application to simplify and project TopoJSON.
  - [Feature Service Layer](https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer-.htm) - Use the `maxAllowableOffset` parameter to return generalized geometries with the `query` operation.
  - [Generalize method](https://esri-es.github.io/arcgis-search/?search=geometryEngine.generalize#gsc.tab=0&gsc.q=%22generalize%22%20site:developers.arcgis.com&gsc.sort=) - GeometryEngine can produce a geometry with fewer vertices programmatically. Several APIs support it: JavaScript, iOS, Android, .NET, Qt, and Java.
  - [PostGIS ST_Simplify](https://postgis.net/docs/ST_Simplify.html) - This operation returns a *simplified* version of the given geometry using the Douglas-Peucker algorithm.
  - [Mapshaper](https://github.com/mbloch/mapshaper) [![GitHub stars](https://img.shields.io/github/stars/mbloch/mapshaper?style=flat)](https://github.com/mbloch/mapshaper/stargazers) - Web application to simplify shapes, edit attribute data, clip, erase, dissolve, filter, etc. Supported file formats: Shapefile, GeoJSON, TopoJSON, and CSV files.

## Data integration tools

- [ArcGIS Data Interoperability Extension](https://esri-es.github.io/awesome-arcgis/arcgis/products/extensions/data-interoperability/) - Desktop tool to transform +400 data formats. 
- [FME Server](https://www.safe.com/integrate/) - ETL allowing to easily transform almost any dataset into an ArcGIS compatible format and vice-versa. Support for 500+ formats and technologies.
- [Koop](https://koopjs.github.io) - JavaScript toolkit for connecting spatial APIs. Transform geospatial data on the fly and serve as GeoJSON, vector tiles, feature services, and more.
- [Make.com](https://www.make.com/en/integrations/survey123) - iPaaS to automate repetitive tasks involved in using Survey123 and make your work easier.
- [node-red-contrib-arcgis-rest](https://flows.nodered.org/node/node-red-contrib-arcgis-rest) - Query, delete, update, or insert data with low-code programming for event-driven applications of the JS Foundation.
- [Zapier for ArcGIS](https://marketplace.arcgis.com/listing.html?id=5ab7936269f8449b82b0f5c78695ab38) - iPaaS to automate integrations without writing any code.
- [Tray.io](https://tray.io/connectors/arcgis-integrations) - Manual, scheduled, and webhook triggers to apply edits, get features, layers, etc. using Tray Platform's ArcGIS connector.

## Debugging tools

- [cors-test.codehappy.dev](https://cors-test.codehappy.dev/) - App to test CORS requests.
- [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic) - Windows tool that logs HTTP(s) network traffic.
- [GeoJSONLint](https://geojsonlint.com/) - Validate and view your GeoJSON.
- [json-schema.org](https://json-schema.org/) - Vocabulary that allows you to annotate and validate JSON documents (including multiple validators).
- [mapbox/geojson-vt/debug](http://mapbox.github.io/geojson-vt/debug/) - Validate GeoJSON or TopoJSON.
- [Postman interceptor](https://www.postman.com/product/postman-interceptor/) - Interceptor enables you to sync cookies from your browser and capture network requests directly from Chrome.
- [netbalancer.com](https://netbalancer.com/) - Windows application for local network traffic control and monitoring.

## Design and styling

- Best practices, books, videos, and training:
	- [Cartography and Making Stunning Maps](https://www.youtube.com/watch?v=AGf_DjZZwXc) - Short video showing some examples of what can be achieved using different blend modes effects.
	- [How to style using ArcGIS Online](https://www.youtube.com/watch?v=6vy-kVkIcRg&list=PLPjPOZQjCWEn6ezKrwN11L8NWhZ2JdpYd) - Playlist with a collection of short videos showcasing some ArcGIS styling capabilities.
	- [Photoshop-style Graphics Effects for Your Layers and Data](https://www.youtube.com/watch?v=crmWm80hwKI) - Video explaining how to use blend modes as well as layer and feature effects to create unique and stunning web maps using the ArcGIS API for JavaScript 4.x. 
	- [MapUIPatterns](https://www.mapuipatterns.com/) - Best practices & design principles. UI Patterns describe solutions to observed and recurring design problems.
- Developer tools:
	- [Calcite Design System](https://developers.arcgis.com/calcite-design-system/) - Collection of mapping icons, web components, and good practices.
  - [Calcite Intellisense Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=K-Dev.calcite-intellisense) - Injects HTML IntelliSense (completion, hover, documentation) for Esri Calcite Design System web components, using Esri's official custom-data JSON.
	- [Calcite Snippets Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=K-Dev.calcite-snippets) - A collection of handy code snippets for the Calcite Design System components, designed to boost your productivity when building web applications with Calcite in Visual Studio Code.
	<!--lint disable double-link-->
	- [geojson2svg](https://github.com/w8r/geojson2svg) [![GitHub stars](https://img.shields.io/github/stars/w8r/geojson2svg?style=flat)](https://github.com/w8r/geojson2svg/stargazers) - Render GeoJSON into SVG using an inline or external stylesheet.
- GUIs:
	- [ArcGIS Vector Tile Style Editor](https://developers.arcgis.com/documentation/mapping-apis-and-services/tools/vector-tile-style-editor/) - Style vector tile basemap layers for applications.
	- [arcgis-vectortile-style-editor](https://github.com/Esri/arcgis-vectortile-style-editor) [![GitHub stars](https://img.shields.io/github/stars/Esri/arcgis-vectortile-style-editor?style=flat)](https://github.com/Esri/arcgis-vectortile-style-editor/stargazers) - Minimalistic tool to update the styles of Esri Vector Basemaps through JSON.
	- [EsriUK mapstyler](https://github.com/EsriUK/mapstyler) [![GitHub stars](https://img.shields.io/github/stars/EsriUK/mapstyler?style=flat)](https://github.com/EsriUK/mapstyler/stargazers) - Quickly style an Esri vector tile layer using an image.

## Developer guides

- [Content management](https://developers.arcgis.com/documentation/mapping-apis-and-services/content-management/) - Store, manage, and access private and public content.
- [Data hosting](https://developers.arcgis.com/documentation/mapping-apis-and-services/data-hosting/) - Store, manage, and access your data as data services.
- [Demographics](https://developers.arcgis.com/documentation/mapping-apis-and-services/demographics/) - Discover local facts and demographic information with the GeoEnrichment service.
- [Geocoding](https://developers.arcgis.com/documentation/mapping-apis-and-services/search/) - Search for addresses, businesses, and places of interest (POIs) with the geocoding service.
- [Maps](https://developers.arcgis.com/documentation/mapping-apis-and-services/maps/) - Display 2D maps and 3D scenes using the basemap layer service and data services.
- [Offline](https://developers.arcgis.com/documentation/mapping-apis-and-services/offline/) - Display, analyze, and edit data while disconnected.
- [Routing](https://developers.arcgis.com/documentation/mapping-apis-and-services/routing/) - Find routes and directions with the routing service.
- [Security and authentication](https://developers.arcgis.com/documentation/mapping-apis-and-services/security/) - Access services and content using API keys and OAuth 2.0.
- [Visualization](https://developers.arcgis.com/documentation/mapping-apis-and-services/visualization/) - Style layers to visualize data in 2D and 3D.

## Helpers

- [arcgis-geometry-calculations](https://github.com/hhkaos/arcgis-geometry-calculations) [![GitHub stars](https://img.shields.io/github/stars/hhkaos/arcgis-geometry-calculations?style=flat)](https://github.com/hhkaos/arcgis-geometry-calculations/stargazers) - Web application to create and grab ArcGIS geometry calculations.
- [arcgis-js-api-camera-helper](https://github.com/pjmclaughlin1979/arcgis-js-api-camera-helper) [![GitHub stars](https://img.shields.io/github/stars/pjmclaughlin1979/arcgis-js-api-camera-helper?style=flat)](https://github.com/pjmclaughlin1979/arcgis-js-api-camera-helper/stargazers) - Web application to get the camera position JSON object for 3D web apps in the ArcGIS API for JavaScript 4.x.
- [arcgis-js-api-extent-helper](https://arcgis-js-api-extent-helper.gavinr.com/) -  Web application to get the map extent JSON object for web apps in the ArcGIS API for JavaScript 4.x.
- [ArcGIS JS API Module Butler](https://marketplace.visualstudio.com/items?itemName=ScottDavis.vscode-arcgis-js-api-module-butler&ssr=false#overview) - VSCode extension for quickly adding ES import statements for the @arcgis/core package without leaving your current code context.
- [epsg.io](https://github.com/maptiler/) [![GitHub stars](https://img.shields.io/github/stars/maptiler/?style=flat)](https://github.com/maptiler//stargazers) - Website to discover and transform coordinate systems from all over the world.
- [esri-loader](https://github.com/Esri/esri-loader) [![GitHub stars](https://img.shields.io/github/stars/Esri/esri-loader?style=flat)](https://github.com/Esri/esri-loader/stargazers) - A tiny library to help you lazy-load the ArcGIS API for JavaScript (i.e., from the CDN) in applications built with popular JavaScript frameworks and bundlers.
- [esri-loader-hooks](https://github.com/tomwayson/esri-loader-hooks) [![GitHub stars](https://img.shields.io/github/stars/tomwayson/esri-loader-hooks?style=flat)](https://github.com/tomwayson/esri-loader-hooks/stargazers) - Custom React hooks for using the ArcGIS API for JavaScript with esri-loader.
- [geojson-random-generator](https://github.com/erick-otenyo/geojson-random-generator) [![GitHub stars](https://img.shields.io/github/stars/erick-otenyo/geojson-random-generator?style=flat)](https://github.com/erick-otenyo/geojson-random-generator/stargazers) - Generate and download random GeoJSON quickly for testing.
- [reducegeojson](https://github.com/radical-data/reducegeojson) [![GitHub stars](https://img.shields.io/github/stars/radical-data/reducegeojson?style=flat)](https://github.com/radical-data/reducegeojson/stargazers) - A tool to reduce the file size of GeoJSON files for web optimization.
- [histogrand](https://github.com/hhkaos/histogrand) [![GitHub stars](https://img.shields.io/github/stars/hhkaos/histogrand?style=flat)](https://github.com/hhkaos/histogrand/stargazers) - Random value generator according to customized histograms.
- [mercator-geographic-converter](https://github.com/hhkaos/mercator-geographic-converter/) [![GitHub stars](https://img.shields.io/github/stars/hhkaos/mercator-geographic-converter/?style=flat)](https://github.com/hhkaos/mercator-geographic-converter//stargazers) - Simple coordinate converter between Geographic units (latitude, longitude) and Mercator units (x, y).
- [react-sceneview](https://github.com/Esri/react-sceneview) [![GitHub stars](https://img.shields.io/github/stars/Esri/react-sceneview?style=flat)](https://github.com/Esri/react-sceneview/stargazers) - A simple Esri SceneView React component that builds on the ArcGIS API for JavaScript.
- [bboxfinder](http://bboxfinder.com/) - Simple web application to get the coordinates of a bounding box drawn on the map.
- [snippets client side raster functions](https://ubatsukh.github.io/arcgis-js-api-demos/clientside-rasterfunctions/index.html) - The client-side raster functions are operations that apply processing directly to the source image pixels.

## Map and data exploration

- [ArcGIS Map Viewer](https://www.arcgis.com/apps/mapviewer/index.html) - Web application to create, explore, and share web maps for 2D applications.
- [ArcGIS Map Viewer (classic version)](https://arcgis.com/home/webmap/viewer.html) - Web application to create, explore, and share web maps for 2D applications.
- [ArcGIS Scene Viewer](https://www.arcgis.com/home/webscene/viewer.html) - Web application to create, explore, and share web maps for 3D applications.
- [Geo Data Viewer](https://marketplace.visualstudio.com/items?itemName=RandomFractalsInc.geo-data-viewer) - VSCode extension for Geo Data Analytics. Support to generate and view maps.
- [geojson.io](https://github.com/mapbox/geojson.io) [![GitHub stars](https://img.shields.io/github/stars/mapbox/geojson.io?style=flat)](https://github.com/mapbox/geojson.io/stargazers) - Web application to visualize, generate, and edit geospatial vector data. Supports GeoJSON, TopoJSON, CSV, KML, WKT, and Shapefile.
- [gpxstudio](https://github.com/gpxstudio/gpxstudio.github.io) [![GitHub stars](https://img.shields.io/github/stars/gpxstudio/gpxstudio.github.io?style=flat)](https://github.com/gpxstudio/gpxstudio.github.io/stargazers) - Online and open source GPX file editor.
- [Mapshaper](https://github.com/mbloch/mapshaper) [![GitHub stars](https://img.shields.io/github/stars/mbloch/mapshaper?style=flat)](https://github.com/mbloch/mapshaper/stargazers) - Web application to simplify shapes, edit attribute data, clip, erase, dissolve, filter, etc. Supported file formats: Shapefile, GeoJSON, TopoJSON, and CSV files. 
- [Smart Mapping](https://www.esri.com/en-us/smart-mapping) - It is built into the Map and Scene viewer, but some APIs like JavaScript and Python also provide utilities to help build data exploration tools.
- [VSCode Map Preview](https://marketplace.visualstudio.com/items?itemName=jumpinjackie.vscode-map-preview) - Extension for visually previewing geospatial file content (GeoJSON, KML, etc) on a map.

## Playgrounds

- [arcgis-arcade-playground](https://developers.arcgis.com/arcade/playground/) - Try the portable scripting language for creating ArcGIS custom visualizations and labeling expressions.
- [cim-symbol-builder](https://github.com/Esri/cim-symbol-builder-js) [![GitHub stars](https://img.shields.io/github/stars/Esri/cim-symbol-builder-js?style=flat)](https://github.com/Esri/cim-symbol-builder-js/stargazers) - Generate CIM symbols to work with ArcGIS client APIs and feature services.
- [geometry-inspector](http://brianbunker.github.io/geometry-inspector/) - Quickly show EsriJSON, GeoJSON, or WKT on a map, or draw on a map to get EsriJSON, GeoJSON, or WKT.
- [js-symbol-playground 3.x](https://developers.arcgis.com/javascript/3/samples/playground/index.html) - Generate symbols to work with the ArcGIS API for JavaScript 3.x.
- [js-symbol-playground 4.x](https://developers.arcgis.com/javascript/latest/sample-code/playground/live/) - Generate symbols to work with the ArcGIS API for JavaScript 4.x.
- [Postman workspaces](https://www.postman.com/esridevs) - Postman collections to experiment with location services and authentication.
- [Firefly Symbols Generator](https://vannizhang.github.io/firefly-symbols-generator/dist/) - Firefly symbol generation.

## Spatial Analysis

<!--lint disable double-link-->
- [ArcGIS Analysis services](https://developers.arcgis.com/rest/analysis-services/) - Spatial, raster, elevation, hydrology, and utility network analysis.
- [Esri/gis-tools-for-hadoop](https://github.com/Esri/gis-tools-for-hadoop) [![GitHub stars](https://img.shields.io/github/stars/Esri/gis-tools-for-hadoop?style=flat)](https://github.com/Esri/gis-tools-for-hadoop/stargazers) - Collection of GIS tools for spatial analysis of big data.
- [Esri/spatial-framework-for-hadoop](https://github.com/Esri/spatial-framework-for-hadoop) [![GitHub stars](https://img.shields.io/github/stars/Esri/spatial-framework-for-hadoop?style=flat)](https://github.com/Esri/spatial-framework-for-hadoop/stargazers) - Allows developers and data scientists to use the Hadoop data processing system for spatial data analysis.
- [Client-side Geometry Engine](https://esri-es.github.io/arcgis-search/?search=geometry+engine&utm_source=chrome-extension#gsc.tab=0&gsc.q=geometry%20engine%20site:developers.arcgis.com&gsc.sort=) - Allows you to test spatial relationships, calculate new geometries, and measure lengths, areas, distances, etc.
	- [ArcGIS API for JavaScript `geometryEngine`](https://developers.arcgis.com/javascript/latest/api-reference/esri-geometry-geometryEngine.html) - Works for browsers and Node.js.
	- [ArcGIS API for Python `arcgis.geometry`](https://developers.arcgis.com/python/api-reference/arcgis.geometry.html)
	- [ArcGIS Maps SDK for .NET `GeometryEngine`](https://developers.arcgis.com/net/api-reference/api/netwin/Esri.ArcGISRuntime/Esri.ArcGISRuntime.Geometry.GeometryEngine.html)
	- [ArcGIS Maps SDK for Android `GeometryEngine`](https://developers.arcgis.com/android/api-reference/reference/com/esri/arcgisruntime/geometry/GeometryEngine.html)
	- [ArcGIS Maps SDK for iOS `AGSGeometryEngine`](https://developers.arcgis.com/ios/api-reference/interface_a_g_s_geometry_engine.html)
	- [ArcGIS Maps SDK for Qt `GeometryEngine`](https://developers.arcgis.com/qt/cpp/api-reference/esri-arcgisruntime-geometryengine.html)
- [Turf.js](https://github.com/Turfjs/turf) [![GitHub stars](https://img.shields.io/github/stars/Turfjs/turf?style=flat)](https://github.com/Turfjs/turf/stargazers) - Geospatial analysis for browsers and Node.js.

## Specifications

- [Cartographic Information Model spec](https://github.com/Esri/cim-spec) [![GitHub stars](https://img.shields.io/github/stars/Esri/cim-spec?style=flat)](https://github.com/Esri/cim-spec/stargazers) - Map content specification used to persist and transfer cartographic descriptions of GIS datasets represented in JSON.
- [Common data types](https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm) - JSON formats of the geometry and spatial reference objects as returned by ArcGIS REST API: Point, Multipoint, Polyline, Polygon and Envelope.
- [GeoServices spec](https://github.com/koopjs/FeatureServer) [![GitHub stars](https://img.shields.io/github/stars/koopjs/FeatureServer?style=flat)](https://github.com/koopjs/FeatureServer/stargazers) - Open Web Foundation REST-based API that provides complete access to structured geospatial data used by Esri.
- [Indexed 3D Scene Layers](https://github.com/Esri/i3s-spec) [![GitHub stars](https://img.shields.io/github/stars/Esri/i3s-spec?style=flat)](https://github.com/Esri/i3s-spec/stargazers) - Service and package standard of containers for arbitrarily large amounts of geographic data.
- [Shapefile Format](https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf) - Spec for the geospatial vector data format for GIS software.
- [Spatial reference specifications](https://developers.arcgis.com/documentation/spatial-references/#spatial-reference-specifications) - List of  Well-Known ID (WKID) integer value or a text string definition referred to as Well-Known Text (WKT) to define a spatial reference.
- [Tile Package Specification](https://github.com/Esri/tile-package-spec) [![GitHub stars](https://img.shields.io/github/stars/Esri/tile-package-spec?style=flat)](https://github.com/Esri/tile-package-spec/stargazers) - Compressed file containing a set of tiles and a tiling scheme, which can be used as a basemap in ArcGIS applications.
- [Web Map spec](https://developers.arcgis.com/web-map-specification/) - Sharable 2D maps. It describes the JSON object that defines a web map.
- [Web Scene spec](https://developers.arcgis.com/web-scene-specification/) - A JSON structure that defines the contents (viewpoint, camera, basemap layer, layers, styles, etc.) for a shareable 3D scene.

---

<!--lint disable no-emphasis-as-heading-->
**Related awesome lists**

- [awesome-arcgis](https://github.com/esri-es/awesome-arcgis/) [![GitHub stars](https://img.shields.io/github/stars/esri-es/awesome-arcgis/?style=flat)](https://github.com/esri-es/awesome-arcgis//stargazers) - Awesome list with a wiki flavor with resources about Esri and ArcGIS, organized by: products, industries, file formats, content providers, etc.
- [awesome-earthobservation-code](https://github.com/acgeospatial/awesome-earthobservation-code) [![GitHub stars](https://img.shields.io/github/stars/acgeospatial/awesome-earthobservation-code?style=flat)](https://github.com/acgeospatial/awesome-earthobservation-code/stargazers) - Tools, tutorials, code, helpful projects, and links about Earth Observation and Geospatial stuff.
- [awesome-geojson](https://github.com/tmcw/awesome-geojson) [![GitHub stars](https://img.shields.io/github/stars/tmcw/awesome-geojson?style=flat)](https://github.com/tmcw/awesome-geojson/stargazers) - GeoJSON utilities: operations,editors & viewers, validation, services, conversion, etc.
- [awesome-geospatial](https://github.com/sacridini/Awesome-Geospatial) [![GitHub stars](https://img.shields.io/github/stars/sacridini/Awesome-Geospatial?style=flat)](https://github.com/sacridini/Awesome-Geospatial/stargazers) - Databases, radar, lidar, web map development, etc.
- [awesome-gis](https://github.com/sshuair/awesome-gis) [![GitHub stars](https://img.shields.io/github/stars/sshuair/awesome-gis?style=flat)](https://github.com/sshuair/awesome-gis/stargazers) - GIS, remote sensing, 3D apps, Web Map Servers, Geospatial libraries, Open Standards, data, etc.
- [awesome-json-datasets](https://github.com/jdorfman/awesome-json-datasets) [![GitHub stars](https://img.shields.io/github/stars/jdorfman/awesome-json-datasets?style=flat)](https://github.com/jdorfman/awesome-json-datasets/stargazers) - JSON datasets that don't require authentication about: climate, crime, government, NASA, travel, etc.
- [awesome-open-geoscience](https://github.com/softwareunderground/awesome-open-geoscience) [![GitHub stars](https://img.shields.io/github/stars/softwareunderground/awesome-open-geoscience?style=flat)](https://github.com/softwareunderground/awesome-open-geoscience/stargazers) - Curated from repositories that make our lives as geoscientists, hackers, and data wranglers easier or just more awesome.
- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) [![GitHub stars](https://img.shields.io/github/stars/awesomedata/awesome-public-datasets?style=flat)](https://github.com/awesomedata/awesome-public-datasets/stargazers) - A topic-centric list of high-quality open datasets.
- [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) [![GitHub stars](https://img.shields.io/github/stars/wenhwu/awesome-remote-sensing-change-detection?style=flat)](https://github.com/wenhwu/awesome-remote-sensing-change-detection/stargazers) - List of datasets, codes, and contests related to remote sensing change detection.
- [awesome-satellite-imagery-datasets](https://github.com/chrieke/awesome-satellite-imagery-datasets) [![GitHub stars](https://img.shields.io/github/stars/chrieke/awesome-satellite-imagery-datasets?style=flat)](https://github.com/chrieke/awesome-satellite-imagery-datasets/stargazers) - List of satellite image training datasets with annotations for computer vision and deep learning.
- [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) [![GitHub stars](https://img.shields.io/github/stars/mrgloom/awesome-semantic-segmentation?style=flat)](https://github.com/mrgloom/awesome-semantic-segmentation/stargazers) - Networks by architecture (semantic segmentation, instance aware segmentation, etc.), RNN, GANS, datasets, and more.
- [awesome-vector-tiles](https://github.com/mapbox/awesome-vector-tiles) [![GitHub stars](https://img.shields.io/github/stars/mapbox/awesome-vector-tiles?style=flat)](https://github.com/mapbox/awesome-vector-tiles/stargazers) - Implementations of the Mapbox Vector Tile specification: parsers & generators, clients, apps, and command line tools, CLI utilities, servers, etc.

<!--lint disable no-emphasis-as-heading-->
**Issues**

Any open issues are fair game. Even just telling us what you want to see would be extremely helpful!

You can [file an issue](https://github.com/ArcGIS/awesome-arcgis-developer/issues/new) [![GitHub stars](https://img.shields.io/github/stars/ArcGIS/awesome-arcgis-developer/issues/new?style=flat)](https://github.com/ArcGIS/awesome-arcgis-developer/issues/new/stargazers) to request or suggest a specific resource.

<!--lint disable no-emphasis-as-heading-->
**Contributing**

Esri welcomes contributions from anyone and everyone. You can [issue a pull request](https://github.com/ArcGIS/awesome-arcgis-developer/pulls) [![GitHub stars](https://img.shields.io/github/stars/ArcGIS/awesome-arcgis-developer/pulls?style=flat)](https://github.com/ArcGIS/awesome-arcgis-developer/pulls/stargazers) to propose an update, but before doing it, please:

- Check the [contributing guidelines for this repo](./CONTRIBUTING.md).
- Take a look at [previously logged issues](https://github.com/ArcGIS/awesome-arcgis-developer/issues) [![GitHub stars](https://img.shields.io/github/stars/ArcGIS/awesome-arcgis-developer/issues?style=flat)](https://github.com/ArcGIS/awesome-arcgis-developer/issues/stargazers). 

For more information, please see Esri's [guidelines for contributing](https://github.com/esri/contributing) [![GitHub stars](https://img.shields.io/github/stars/esri/contributing?style=flat)](https://github.com/esri/contributing/stargazers).

<!--lint disable no-emphasis-as-heading-->

**Footnotes**

Copyright 2025 Esri
