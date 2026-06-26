# Web Archiving

[![GitHub stars](https://img.shields.io/github/stars/iipc/awesome-web-archiving?style=flat)](https://github.com/iipc/awesome-web-archiving/stargazers)

<!--lint ignore awesome-github-->
# Awesome Web Archiving [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Web archiving is the process of collecting portions of the World Wide Web to ensure the information is preserved in an archive for future researchers, historians, and the public. Web archivists typically employ Web crawlers for automated capture due to the massive scale of the Web. Ever-evolving Web standards require continuous evolution of archiving tools to keep up with the changes in Web technologies to ensure reliable and meaningful capture and replay of archived web pages.


## Contents

* [Training/Documentation](#trainingdocumentation)
  * [Introductions to Web Archiving Concepts](#introductions-to-web-archiving-concepts)
  * [Training Materials](#training-materials)
  * [The WARC Standard](#the-warc-standard)
  * [For Researchers using Web Archives](#for-researchers-using-web-archives)
* [Resources for Web Publishers](#resources-for-web-publishers)
* [Tools & Software](#tools--software)
  * [Acquisition](#acquisition)
  * [Replay](#replay)
  * [Search & Discovery](#search--discovery)
  * [Utilities](#utilities)
  * [WARC I/O Libraries](#warc-io-libraries)
  * [Analysis](#analysis)
  * [Quality Assurance](#quality-assurance)
  * [Curation](#curation)
* [Community Resources](#community-resources)
  * [Other Awesome Lists](#other-awesome-lists)
  * [Blogs and Scholarship](#blogs-and-scholarship)
  * [Mailing Lists](#mailing-lists)
  * [Slack](#slack)
  * [Discord](#discord)
  * [Twitter](#twitter)
* [Web Archiving Service Providers](#web-archiving-service-providers)
  * [Self-hostable, Open Source](#self-hostable-open-source)
  * [Hosted, Closed Source](#hosted-closed-source)
* [Public Data](#public-data)

## Training/Documentation

This section provides a curated list of training materials, documentation, and educational resources for those interested in learning about web archiving practices, methodologies, and tools.

### Introductions to Web Archiving Concepts

* [What is a web archive?](https://youtu.be/ubDHY-ynWi0) - A video from [the UK Web Archive YouTube Channel](https://www.youtube.com/channel/UCJukhTSw8VRj-VNTpBcqWkw)
* [Wikipedia's List of Web Archiving Initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)
* [Glossary of Archive-It and Web Archiving Terms](https://support.archive-it.org/hc/en-us/articles/208111686-Glossary-of-Archive-It-and-Web-Archiving-Terms)
* [The Web Archiving Lifecycle Model](https://archive-it.org/blog/post/announcing-the-web-archiving-life-cycle-model/) - An attempt to incorporate the technological and programmatic arms of the web archiving into a framework that will be relevant to any organization seeking to archive content from the web. Archive-It, the web archiving service from the Internet Archive, developed the model based on its work with memory institutions around the world.
* [Retrieving and Archiving Information from Websites by Wael Eskandar and Brad Murray](https://kit.exposingtheinvisible.org/en/web-archive.html/)

### Training Materials

* [IIPC and DPC Training materials: module for beginners (8 sessions)](https://netpreserve.org/web-archiving/training-materials/)
* [UNT Web Archiving Course](https://github.com/vphill/web-archiving-course) [![GitHub stars](https://img.shields.io/github/stars/vphill/web-archiving-course?style=flat)](https://github.com/vphill/web-archiving-course/stargazers)
* [Continuing Education to Advance Web Archiving (CEDWARC)](https://cedwarc.github.io/)
* [A Whirlwind Tour of Common Crawl's Datasets using Python](https://github.com/commoncrawl/whirlwind-python/) [![GitHub stars](https://img.shields.io/github/stars/commoncrawl/whirlwind-python/?style=flat)](https://github.com/commoncrawl/whirlwind-python//stargazers)
* [A Whirlwind Tour of Common Crawl's Datasets as a Python notebook](https://github.com/commoncrawl/whirlwind-python-notebook) [![GitHub stars](https://img.shields.io/github/stars/commoncrawl/whirlwind-python-notebook?style=flat)](https://github.com/commoncrawl/whirlwind-python-notebook/stargazers)
* [A Whirlwind Tour of Common Crawl's Datasets using Java](https://github.com/commoncrawl/whirlwind-java/) [![GitHub stars](https://img.shields.io/github/stars/commoncrawl/whirlwind-java/?style=flat)](https://github.com/commoncrawl/whirlwind-java//stargazers)

### The WARC Standard

* [The warc-specifications](https://iipc.github.io/warc-specifications/) - A community HTML version of the official specification and hub for new proposals.
* [Offical ISO 28500 WARC specification homepage](http://bibnum.bnf.fr/WARC/)

### For Researchers using Web Archives

* [GLAM Workbench: Web Archives](https://glam-workbench.github.io/web-archives/) - See also [this related blog post on 'Asking questions with web archives'](https://netpreserveblog.wordpress.com/2020/05/28/asking-questions-with-web-archives/).
* [Archives Unleashed Toolkit documentation](https://aut.docs.archivesunleashed.org/)
* [Tutorial for Humanities researchers about how to explore Arquivo.pt](https://sobre.arquivo.pt/en/tutorial-for-humanities-researchers-about-how-to-use-arquivo-pt/)

## Resources for Web Publishers

These resources can help when working with individuals or organisations who publish on the web, and who want to make sure their site can be archived.

* [Definition of Web Archivability](https://nullhandle.org/web-archivability/index.html) - This describes the ease with which web content can be preserved. ([Archived version from the Stanford Libraries](https://web.archive.org/web/20230728211501/https://library.stanford.edu/projects/web-archiving/archivability))
* The [Archive Ready](http://archiveready.com/) tool, for estimating how likely a web page will be archived successfully.


## Tools & Software

This list of tools and software is intended to briefly describe some of the most important and widely-used tools related to web archiving. For more details, we recommend you refer to (and contribute to!) these excellent resources from other groups:

* [Comparison of web archiving software](https://github.com/archivers-space/research/tree/master/web_archiving) [![GitHub stars](https://img.shields.io/github/stars/archivers-space/research/tree/master/web_archiving?style=flat)](https://github.com/archivers-space/research/tree/master/web_archiving/stargazers)
* [Awesome Website Change Monitoring](https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring) [![GitHub stars](https://img.shields.io/github/stars/edgi-govdata-archiving/awesome-website-change-monitoring?style=flat)](https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring/stargazers)

### Acquisition

* [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) [![GitHub stars](https://img.shields.io/github/stars/ArchiveBox/ArchiveBox?style=flat)](https://github.com/ArchiveBox/ArchiveBox/stargazers) - A tool which maintains an additive archive from RSS feeds, bookmarks, and links using wget, Chrome headless, and other methods (formerly `Bookmark Archiver`). *(In Development)*
* [archivenow](https://github.com/oduwsdl/archivenow) [![GitHub stars](https://img.shields.io/github/stars/oduwsdl/archivenow?style=flat)](https://github.com/oduwsdl/archivenow/stargazers) - A [Python library](http://ws-dl.blogspot.com/2017/02/2017-02-22-archive-now-archivenow.html) to push web resources into on-demand web archives. *(Stable)*
* [ArchiveWeb.Page](https://webrecorder.net/archivewebpage/) - A plugin for Chrome and other Chromium based browsers that lets you interactively archive web pages, replay them, and export them as WARC & WACZ files. Also available as an Electron based desktop application.
* [Auto Archiver](https://github.com/bellingcat/auto-archiver) [![GitHub stars](https://img.shields.io/github/stars/bellingcat/auto-archiver?style=flat)](https://github.com/bellingcat/auto-archiver/stargazers) - Python script to automatically archive social media posts, videos, and images from a Google Sheets document. Read the [article about Auto Archiver on bellingcat.com](https://www.bellingcat.com/resources/2022/09/22/preserve-vital-online-content-with-bellingcats-auto-archiver-tool/).
* [Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler) [![GitHub stars](https://img.shields.io/github/stars/webrecorder/browsertrix-crawler?style=flat)](https://github.com/webrecorder/browsertrix-crawler/stargazers) - A Chromium based high-fidelity crawling system, designed to run a complex, customizable browser-based crawl in a single Docker container. *(Stable)*
* [Brozzler](https://github.com/internetarchive/brozzler) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/brozzler?style=flat)](https://github.com/internetarchive/brozzler/stargazers) - A distributed web crawler (爬虫) that uses a real browser (Chrome or Chromium) to fetch pages and embedded urls and to extract links. *(Stable)*
* [Cairn](https://github.com/wabarc/cairn) [![GitHub stars](https://img.shields.io/github/stars/wabarc/cairn?style=flat)](https://github.com/wabarc/cairn/stargazers) - A npm package and CLI tool for saving webpages. *(Stable)*
* [Chronicler](https://github.com/CGamesPlay/chronicler) [![GitHub stars](https://img.shields.io/github/stars/CGamesPlay/chronicler?style=flat)](https://github.com/CGamesPlay/chronicler/stargazers) - Web browser with record and replay functionality. *(In Development)*
* [Community Archive](https://www.community-archive.org/) - Open Twitter Database and API with tools and resources for building on archived Twitter data.
* [crau](https://github.com/turicas/crau) [![GitHub stars](https://img.shields.io/github/stars/turicas/crau?style=flat)](https://github.com/turicas/crau/stargazers) - crau is the way (most) Brazilians pronounce crawl, it's the easiest command-line tool for archiving the Web and playing archives: you just need a list of URLs. *(Stable)*
* [Crawl](https://git.autistici.org/ale/crawl) - A simple web crawler in Golang. *(Stable)*
* [crocoite](https://github.com/PromyLOPh/crocoite) [![GitHub stars](https://img.shields.io/github/stars/PromyLOPh/crocoite?style=flat)](https://github.com/PromyLOPh/crocoite/stargazers) - Crawl websites using headless Google Chrome/Chromium and save resources, static DOM snapshot and page screenshots to WARC files. *(In Development)*
* [DiskerNet](https://github.com/DO-SAY-GO/dn) [![GitHub stars](https://img.shields.io/github/stars/DO-SAY-GO/dn?style=flat)](https://github.com/DO-SAY-GO/dn/stargazers) - A non-WARC-based tool which hooks into the Chrome browser and archives everything you browse making it available for offline replay. *(In Development)*
* [F(b)arc](https://github.com/justinlittman/fbarc) [![GitHub stars](https://img.shields.io/github/stars/justinlittman/fbarc?style=flat)](https://github.com/justinlittman/fbarc/stargazers) - A commandline tool and Python library for archiving data from [Facebook](https://www.facebook.com/) using the [Graph API](https://developers.facebook.com/docs/graph-api). *(Stable)*
* [freeze-dry](https://github.com/WebMemex/freeze-dry) [![GitHub stars](https://img.shields.io/github/stars/WebMemex/freeze-dry?style=flat)](https://github.com/WebMemex/freeze-dry/stargazers) - JavaScript library to turn page into static, self-contained HTML document; useful for browser extensions. *(In Development)*
* [grab-site](https://github.com/ArchiveTeam/grab-site) [![GitHub stars](https://img.shields.io/github/stars/ArchiveTeam/grab-site?style=flat)](https://github.com/ArchiveTeam/grab-site/stargazers) - The archivist's web crawler: WARC output, dashboard for all crawls, dynamic ignore patterns. *(Stable)*
* [Heritrix](https://github.com/internetarchive/heritrix3/wiki) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/heritrix3/wiki?style=flat)](https://github.com/internetarchive/heritrix3/wiki/stargazers) - An open source, extensible, web-scale, archival quality web crawler. *(Stable)*
  * [Heritrix Q&A](https://github.com/internetarchive/heritrix3/discussions/categories/q-a) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/heritrix3/discussions/categories/q-a?style=flat)](https://github.com/internetarchive/heritrix3/discussions/categories/q-a/stargazers) - A discussion forum for asking questions and getting answers about using Heritrix.
  * [Heritrix Walkthrough](https://github.com/web-archive-group/heritrix-walkthrough) [![GitHub stars](https://img.shields.io/github/stars/web-archive-group/heritrix-walkthrough?style=flat)](https://github.com/web-archive-group/heritrix-walkthrough/stargazers) *(In Development)*
* [html2warc](https://github.com/steffenfritz/html2warc) [![GitHub stars](https://img.shields.io/github/stars/steffenfritz/html2warc?style=flat)](https://github.com/steffenfritz/html2warc/stargazers) - A simple script to convert offline data into a single WARC file. *(Stable)*
* [HTTrack](http://www.httrack.com/) - An open source website copying utility. *(Stable)*
* [monolith](https://github.com/Y2Z/monolith) [![GitHub stars](https://img.shields.io/github/stars/Y2Z/monolith?style=flat)](https://github.com/Y2Z/monolith/stargazers) - CLI tool to save a web page as a single HTML file. *(Stable)*
* [Obelisk](https://github.com/go-shiori/obelisk) [![GitHub stars](https://img.shields.io/github/stars/go-shiori/obelisk?style=flat)](https://github.com/go-shiori/obelisk/stargazers) - Go package and CLI tool for saving web page as single HTML file. *(Stable)*
* [Scoop](https://github.com/harvard-lil/scoop) [![GitHub stars](https://img.shields.io/github/stars/harvard-lil/scoop?style=flat)](https://github.com/harvard-lil/scoop/stargazers) - High-fidelity, browser-based, single-page web archiving library and CLI for witnessing the web. *(Stable)*
* [SingleFile](https://github.com/gildas-lormeau/SingleFile) [![GitHub stars](https://img.shields.io/github/stars/gildas-lormeau/SingleFile?style=flat)](https://github.com/gildas-lormeau/SingleFile/stargazers) - Browser extension for Firefox/Chrome and CLI tool to save a faithful copy of a complete page as a single HTML file. *(Stable)*
* [SiteStory](http://mementoweb.github.io/SiteStory/) - A transactional archive that selectively captures and stores transactions that take place between a web client (browser) and a web server. *(Stable)*
* [Social Feed Manager](https://gwu-libraries.github.io/sfm-ui/) - Open source software that enables users to create social media collections from Twitter, Tumblr, Flickr, and Sina Weibo public APIs. *(Stable)*
* [Squidwarc](https://github.com/N0taN3rd/Squidwarc) [![GitHub stars](https://img.shields.io/github/stars/N0taN3rd/Squidwarc?style=flat)](https://github.com/N0taN3rd/Squidwarc/stargazers) - An [open source, high-fidelity, page interacting](http://ws-dl.blogspot.com/2017/07/2017-07-24-replacing-heritrix-with.html) archival crawler that uses Chrome or Chrome Headless directly. *(In Development)*
* [StormCrawler](http://stormcrawler.net/) - A collection of resources for building low-latency, scalable web crawlers on Apache Storm. *(Stable)*
* [twarc](https://github.com/DocNow/twarc) [![GitHub stars](https://img.shields.io/github/stars/DocNow/twarc?style=flat)](https://github.com/DocNow/twarc/stargazers) - A command line tool and Python library for archiving Twitter JSON data. *(Stable)*
* [WAIL](https://github.com/machawk1/wail) [![GitHub stars](https://img.shields.io/github/stars/machawk1/wail?style=flat)](https://github.com/machawk1/wail/stargazers) - A graphical user interface (GUI) atop multiple web archiving tools intended to be used as an easy way for anyone to preserve and replay web pages; [Python](https://machawk1.github.io/wail/), [Electron](https://github.com/n0tan3rd/wail) [![GitHub stars](https://img.shields.io/github/stars/n0tan3rd/wail?style=flat)](https://github.com/n0tan3rd/wail/stargazers). *(Stable)*
* [Warcprox](https://github.com/internetarchive/warcprox) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/warcprox?style=flat)](https://github.com/internetarchive/warcprox/stargazers) - WARC-writing MITM HTTP/S proxy. *(Stable)*
* [WARCreate](http://matkelly.com/warcreate/) - A [Google Chrome](https://www.google.com/intl/en/chrome/browser/) extension for archiving an individual webpage or website to a WARC file. *(Stable)*
* [Warcworker](https://github.com/peterk/warcworker) [![GitHub stars](https://img.shields.io/github/stars/peterk/warcworker?style=flat)](https://github.com/peterk/warcworker/stargazers) - An open source, dockerized, queued, high fidelity web archiver based on Squidwarc with a simple web GUI. *(Stable)*
* [Wayback](https://github.com/wabarc/wayback) [![GitHub stars](https://img.shields.io/github/stars/wabarc/wayback?style=flat)](https://github.com/wabarc/wayback/stargazers) - A toolkit for snapshot webpage to Internet Archive, archive.today, IPFS and beyond. *(Stable)*
* [Waybackpy](https://github.com/akamhy/waybackpy) [![GitHub stars](https://img.shields.io/github/stars/akamhy/waybackpy?style=flat)](https://github.com/akamhy/waybackpy/stargazers) -  Wayback Machine Save, CDX and availability API interface in Python and a command-line tool  *(Stable)*
* [Web2Warc](https://github.com/helgeho/Web2Warc) [![GitHub stars](https://img.shields.io/github/stars/helgeho/Web2Warc?style=flat)](https://github.com/helgeho/Web2Warc/stargazers) - An easy-to-use and highly customizable crawler that enables anyone to create their own little Web archives (WARC/CDX). *(Stable)*
* [Web Curator Tool](https://webcuratortool.org) - Open-source workflow management for selective web archiving. *(Stable)*
* [WebMemex](https://github.com/WebMemex) [![GitHub stars](https://img.shields.io/github/stars/WebMemex?style=flat)](https://github.com/WebMemex/stargazers) - Browser extension for Firefox and Chrome which lets you archive web pages you visit. *(In Development)*
* [Wget](http://www.gnu.org/software/wget/) - An open source file retrieval utility that of [version 1.14 supports writing warcs](http://www.archiveteam.org/index.php?title=Wget_with_WARC_output). *(Stable)*
* [Wget-lua](https://github.com/alard/wget-lua) [![GitHub stars](https://img.shields.io/github/stars/alard/wget-lua?style=flat)](https://github.com/alard/wget-lua/stargazers) - Wget with Lua extension. *(Stable)*
* [Wpull](https://github.com/ArchiveTeam/wpull) [![GitHub stars](https://img.shields.io/github/stars/ArchiveTeam/wpull?style=flat)](https://github.com/ArchiveTeam/wpull/stargazers) - A Wget-compatible (or remake/clone/replacement/alternative) web downloader and crawler. *(Stable)*

### Replay

* [InterPlanetary Wayback (ipwb)](https://github.com/oduwsdl/ipwb) [![GitHub stars](https://img.shields.io/github/stars/oduwsdl/ipwb?style=flat)](https://github.com/oduwsdl/ipwb/stargazers) - Web Archive (WARC) indexing and replay using [IPFS](https://ipfs.io/).
* [OpenWayback](https://github.com/iipc/openwayback/) [![GitHub stars](https://img.shields.io/github/stars/iipc/openwayback/?style=flat)](https://github.com/iipc/openwayback//stargazers) - The open source project aimed to develop Wayback Machine, the key software used by web archives worldwide to play back archived websites in the user's browser. *(Stable)*
* [PYWB](https://github.com/webrecorder/pywb) [![GitHub stars](https://img.shields.io/github/stars/webrecorder/pywb?style=flat)](https://github.com/webrecorder/pywb/stargazers) - A Python 3 implementation of web archival replay tools, sometimes also known as 'Wayback Machine'. *(Stable)*
* [Reconstructive](https://oduwsdl.github.io/Reconstructive/) - Reconstructive is a ServiceWorker module for client-side reconstruction of composite mementos by rerouting resource requests to corresponding archived copies (JavaScript).
* [ReplayWeb.page](https://webrecorder.net/replaywebpage/) - A browser-based, fully client-side replay engine for both local and remote WARC & WACZ files. Also available as an Electron based desktop application. *(Stable)*
* [warc2html](https://github.com/iipc/warc2html) [![GitHub stars](https://img.shields.io/github/stars/iipc/warc2html?style=flat)](https://github.com/iipc/warc2html/stargazers) - Converts WARC files to static HTML suitable for browsing offline or rehosting.

### Search & Discovery

* [hyphe](https://github.com/medialab/hyphe) [![GitHub stars](https://img.shields.io/github/stars/medialab/hyphe?style=flat)](https://github.com/medialab/hyphe/stargazers) - A webcrawler built for research uses with a graphical user interface in order to build web corpuses made of lists of web actors and maps of links between them. *(Stable)*
* [Mink](https://github.com/machawk1/Mink) [![GitHub stars](https://img.shields.io/github/stars/machawk1/Mink?style=flat)](https://github.com/machawk1/Mink/stargazers) - A [Google Chrome](https://www.google.com/intl/en/chrome/) extension for querying Memento aggregators while browsing and integrating live-archived web navigation. *(Stable)*
* [PANDORÆ](https://github.com/Guillaume-Levrier/PANDORAE) [![GitHub stars](https://img.shields.io/github/stars/Guillaume-Levrier/PANDORAE?style=flat)](https://github.com/Guillaume-Levrier/PANDORAE/stargazers) - A desktop research software to be plugged on a Solr endpoint to query, retrieve, normalize and visually explore web archives. *(Stable)*
* [playback](https://github.com/wabarc/playback) [![GitHub stars](https://img.shields.io/github/stars/wabarc/playback?style=flat)](https://github.com/wabarc/playback/stargazers) - A toolkit for searching archived webpages from <!--lint ignore double-link-->[Internet Archive](https://web.archive.org), [archive.today](https://archive.today), [Memento](http://timetravel.mementoweb.org) and beyond. *(In Development)*
* [SecurityTrails](https://securitytrails.com/) - Web based archive for WHOIS and DNS records. REST API available free of charge.
* [Tempas v1](http://tempas.L3S.de/v1) - Temporal web archive search based on [Delicious](https://en.wikipedia.org/wiki/Delicious_(website)) tags. *(Stable)*
* [Tempas v2](http://tempas.L3S.de/v2) - Temporal web archive search based on links and anchor texts extracted from the German web from 1996 to 2013 (results are not limited to German pages, e.g., [Obama@2005-2009 in Tempas](http://tempas.l3s.de/v2/query?q=obama&from=2005&to=2009)). *(Stable)*
* [webarchive-discovery](https://github.com/ukwa/webarchive-discovery) [![GitHub stars](https://img.shields.io/github/stars/ukwa/webarchive-discovery?style=flat)](https://github.com/ukwa/webarchive-discovery/stargazers) - WARC and ARC full-text indexing and discovery tools, with a number of associated tools capable of using the index shown below. *(Stable)*
* [Shine](https://github.com/ukwa/shine) [![GitHub stars](https://img.shields.io/github/stars/ukwa/shine?style=flat)](https://github.com/ukwa/shine/stargazers) - A prototype web archives exploration UI, developed with researchers as part of the [Big UK Domain Data for the Arts and Humanities project](https://buddah.projects.history.ac.uk/). *(Stable)*
* [SolrWayback](https://github.com/netarchivesuite/solrwayback) [![GitHub stars](https://img.shields.io/github/stars/netarchivesuite/solrwayback?style=flat)](https://github.com/netarchivesuite/solrwayback/stargazers) - A backend Java and frontend VUE JS project with freetext search and a build in playback engine. Require Warc files has been index with the Warc-Indexer. The web application also has a wide range of data visualization tools and data export tools that can be used on the whole webarchive. [SolrWayback 4 Bundle release](https://github.com/netarchivesuite/solrwayback/releases) [![GitHub stars](https://img.shields.io/github/stars/netarchivesuite/solrwayback/releases?style=flat)](https://github.com/netarchivesuite/solrwayback/releases/stargazers) contains all the software and dependencies in an out-of-the box solution that is easy to install.
* [Warclight](https://github.com/archivesunleashed/warclight) [![GitHub stars](https://img.shields.io/github/stars/archivesunleashed/warclight?style=flat)](https://github.com/archivesunleashed/warclight/stargazers) - A Project Blacklight based Rails engine that supports the discovery of web archives held in the WARC and ARC formats. *(In Development)*
* [Wasp](https://github.com/webis-de/wasp) [![GitHub stars](https://img.shields.io/github/stars/webis-de/wasp?style=flat)](https://github.com/webis-de/wasp/stargazers) - A fully functional prototype of a personal [web archive and search system](http://ceur-ws.org/Vol-2167/paper6.pdf). *(In Development)*
* Other possible options for builting a front-end are listed on in the `webarchive-discovery` wiki, [here](https://github.com/ukwa/webarchive-discovery/wiki/Front-ends) [![GitHub stars](https://img.shields.io/github/stars/ukwa/webarchive-discovery/wiki/Front-ends?style=flat)](https://github.com/ukwa/webarchive-discovery/wiki/Front-ends/stargazers).

### Utilities

* [ArchiveTools](https://github.com/recrm/ArchiveTools) [![GitHub stars](https://img.shields.io/github/stars/recrm/ArchiveTools?style=flat)](https://github.com/recrm/ArchiveTools/stargazers) - Collection of tools to extract and interact with WARC files (Python).
* [bagnabit2warc](https://github.com/internetarchive/bagnabit2warc) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/bagnabit2warc?style=flat)](https://github.com/internetarchive/bagnabit2warc/stargazers) - Convert a [bag-nabit](https://github.com/harvard-lil/bag-nabit) [![GitHub stars](https://img.shields.io/github/stars/harvard-lil/bag-nabit?style=flat)](https://github.com/harvard-lil/bag-nabit/stargazers) dataset stored in a ZIP into a full-content WARC.
* [cdx-toolkit](https://pypi.org/project/cdx-toolkit/) - Library and CLI to consult cdx indexes and create WARC extractions of subsets. Abstracts away Common Crawl's unusual crawl structure. *(Stable)*
* [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) [![GitHub stars](https://img.shields.io/github/stars/midwork-finds-jobs/duckdb_warc?style=flat)](https://github.com/midwork-finds-jobs/duckdb_warc/stargazers) - DuckDB extension to query WARC files. *(In Development)*
* [duckdb-web-archive-cdx](https://github.com/midwork-finds-jobs/duckdb-web-archive) [![GitHub stars](https://img.shields.io/github/stars/midwork-finds-jobs/duckdb-web-archive?style=flat)](https://github.com/midwork-finds-jobs/duckdb-web-archive/stargazers) - DuckDB extension to query the Internet Archive and CommonCrawl CDX APIs directly from SQL. *(In Development)*
* [Go Get Crawl](https://github.com/karust/gogetcrawl) [![GitHub stars](https://img.shields.io/github/stars/karust/gogetcrawl?style=flat)](https://github.com/karust/gogetcrawl/stargazers) - Extract web archive data using <!--lint ignore double-link-->[Wayback Machine](https://web.archive.org/) and [Common Crawl](https://commoncrawl.org/). *(Stable)*
* [gowarcserver](https://github.com/nlnwa/gowarcserver) [![GitHub stars](https://img.shields.io/github/stars/nlnwa/gowarcserver?style=flat)](https://github.com/nlnwa/gowarcserver/stargazers) - [BadgerDB](https://github.com/dgraph-io/badger) [![GitHub stars](https://img.shields.io/github/stars/dgraph-io/badger?style=flat)](https://github.com/dgraph-io/badger/stargazers)-based capture index (CDX) and WARC record server, used to index and serve WARC files (Go).
* [har2warc](https://github.com/webrecorder/har2warc) [![GitHub stars](https://img.shields.io/github/stars/webrecorder/har2warc?style=flat)](https://github.com/webrecorder/har2warc/stargazers) - Convert HTTP Archive (HAR) -> Web Archive (WARC) format (Python).
<!--lint ignore double-link-->
* [httpreserve.info](https://httpreserve.info) - Service to return the status of a web page or save it to the Internet Archive. HTTPreserve includes disambiguation of well-known short link services. It returns JSON via the browser or command line via CURL using GET. Describes web sites using earliest and latest dates in the Internet Archive and demonstrates the construction of Robust Links in its output using that range. (Golang). *(Stable)*
* [HTTPreserve linkstat](https://github.com/httpreserve/linkstat) [![GitHub stars](https://img.shields.io/github/stars/httpreserve/linkstat?style=flat)](https://github.com/httpreserve/linkstat/stargazers) - Command line implementation of <!--lint ignore double-link-->[httpreserve.info](https://httpreserve.info) to describe the status of a web page. Can be easily scripted and provides JSON output to enable querying through tools like JQ. HTTPreserve Linkstat describes current status, and earliest and latest links on <!--lint ignore double-link-->[archive.org](https://archive.org/). (Golang). *(Stable)*
* [Internet Archive Library](https://github.com/jjjake/internetarchive) [![GitHub stars](https://img.shields.io/github/stars/jjjake/internetarchive?style=flat)](https://github.com/jjjake/internetarchive/stargazers) - A command line tool and Python library for interacting directly with <!--lint ignore double-link-->[archive.org](https://archive.org). (Python). *(Stable)*
* [httrack2warc](https://github.com/nla/httrack2warc) [![GitHub stars](https://img.shields.io/github/stars/nla/httrack2warc?style=flat)](https://github.com/nla/httrack2warc/stargazers) - Convert HTTrack archives to WARC format (Java).
* [MementoMap](https://github.com/oduwsdl/MementoMap) [![GitHub stars](https://img.shields.io/github/stars/oduwsdl/MementoMap?style=flat)](https://github.com/oduwsdl/MementoMap/stargazers) - A Tool to Summarize Web Archive Holdings (Python). *(In Development)*
* [MemGator](https://github.com/oduwsdl/MemGator) [![GitHub stars](https://img.shields.io/github/stars/oduwsdl/MemGator?style=flat)](https://github.com/oduwsdl/MemGator/stargazers) - A Memento Aggregator CLI and Server (Golang). *(Stable)*
* [node-cdxj](https://github.com/N0taN3rd/node-cdxj) [![GitHub stars](https://img.shields.io/github/stars/N0taN3rd/node-cdxj?style=flat)](https://github.com/N0taN3rd/node-cdxj/stargazers) - [CDXJ](https://github.com/oduwsdl/ORS/wiki/CDXJ) [![GitHub stars](https://img.shields.io/github/stars/oduwsdl/ORS/wiki/CDXJ?style=flat)](https://github.com/oduwsdl/ORS/wiki/CDXJ/stargazers) file parser (Node.js). *(Stable)*
* [OutbackCDX](https://github.com/nla/outbackcdx) [![GitHub stars](https://img.shields.io/github/stars/nla/outbackcdx?style=flat)](https://github.com/nla/outbackcdx/stargazers) - RocksDB-based capture index (CDX) server supporting incremental updates and compression. Can be used as backend for OpenWayback, PyWb and [Heritrix](https://github.com/ukwa/ukwa-heritrix/blob/master/src/main/java/uk/bl/wap/modules/uriuniqfilters/OutbackCDXRecentlySeenUriUniqFilter.java) [![GitHub stars](https://img.shields.io/github/stars/ukwa/ukwa-heritrix/blob/master/src/main/java/uk/bl/wap/modules/uriuniqfilters/OutbackCDXRecentlySeenUriUniqFilter.java?style=flat)](https://github.com/ukwa/ukwa-heritrix/blob/master/src/main/java/uk/bl/wap/modules/uriuniqfilters/OutbackCDXRecentlySeenUriUniqFilter.java/stargazers). *(Stable)*
* [py-wasapi-client](https://github.com/unt-libraries/py-wasapi-client) [![GitHub stars](https://img.shields.io/github/stars/unt-libraries/py-wasapi-client?style=flat)](https://github.com/unt-libraries/py-wasapi-client/stargazers) - Command line application to download crawls from WASAPI (Python). *(Stable)*
* [The Unarchiver](https://theunarchiver.com/) - Program to extract the contents of many archive formats, inclusive of WARC, to a file system. Free variant of The Archive Browser (macOS only, Proprietary app).
* [tikalinkextract](https://github.com/httpreserve/tikalinkextract) [![GitHub stars](https://img.shields.io/github/stars/httpreserve/tikalinkextract?style=flat)](https://github.com/httpreserve/tikalinkextract/stargazers) - Extract hyperlinks as a seed for web archiving from folders of document types that can be parsed by Apache Tika (Golang, Apache Tika Server). *(In Development)*
* [wasapi-downloader](https://github.com/sul-dlss/wasapi-downloader) [![GitHub stars](https://img.shields.io/github/stars/sul-dlss/wasapi-downloader?style=flat)](https://github.com/sul-dlss/wasapi-downloader/stargazers) - Java command line application to download crawls from WASAPI. *(Stable)*
* [Warchaeology](https://nlnwa.github.io/warchaeology/) - Warchaeology is a collection of tools for inspecting, manipulating, deduplicating and validating WARC-files. *(Stable)*
* [warcdb](https://github.com/florents-Tselai/warcdb) [![GitHub stars](https://img.shields.io/github/stars/florents-Tselai/warcdb?style=flat)](https://github.com/florents-Tselai/warcdb/stargazers) - A command line utility (Python) for importing WARC files into a SQLite database. *(Stable)*
* [warcbench](https://github.com/harvard-lil/warcbench) [![GitHub stars](https://img.shields.io/github/stars/harvard-lil/warcbench?style=flat)](https://github.com/harvard-lil/warcbench/stargazers) - A tool for exploring, analyzing, transforming, recombining, and extracting data from WARC (Web ARChive) files.
* [warcdedupe](https://gitlab.com/taricorp/warcdedupe) - WARC deduplication tool (and WARC library) written in Rust. *(In Development)*
* [warc-safe](https://github.com/natliblux/warc-safe) [![GitHub stars](https://img.shields.io/github/stars/natliblux/warc-safe?style=flat)](https://github.com/natliblux/warc-safe/stargazers) - Automatic detection of viruses and NSFW content in WARC files.
* [WarcPartitioner](https://github.com/helgeho/WarcPartitioner) [![GitHub stars](https://img.shields.io/github/stars/helgeho/WarcPartitioner?style=flat)](https://github.com/helgeho/WarcPartitioner/stargazers) - Partition (W)ARC Files by MIME Type and Year. *(Stable)*
* [warcrefs](https://github.com/arcalex/warcrefs) [![GitHub stars](https://img.shields.io/github/stars/arcalex/warcrefs?style=flat)](https://github.com/arcalex/warcrefs/stargazers) - Web archive deduplication tools. *(Stable)*
* [webarchive-indexing](https://github.com/ikreymer/webarchive-indexing) [![GitHub stars](https://img.shields.io/github/stars/ikreymer/webarchive-indexing?style=flat)](https://github.com/ikreymer/webarchive-indexing/stargazers) - Tools for bulk indexing of WARC/ARC files on Hadoop, EMR or local file system.
* [wikiteam](https://github.com/WikiTeam/wikiteam) [![GitHub stars](https://img.shields.io/github/stars/WikiTeam/wikiteam?style=flat)](https://github.com/WikiTeam/wikiteam/stargazers) - Tools for downloading and preserving wikis. *(Stable)*

### WARC I/O Libraries

* [FastWARC](https://github.com/chatnoir-eu/chatnoir-resiliparse) [![GitHub stars](https://img.shields.io/github/stars/chatnoir-eu/chatnoir-resiliparse?style=flat)](https://github.com/chatnoir-eu/chatnoir-resiliparse/stargazers) - A high-performance WARC parsing library (Python).
* [HadoopConcatGz](https://github.com/helgeho/HadoopConcatGz) [![GitHub stars](https://img.shields.io/github/stars/helgeho/HadoopConcatGz?style=flat)](https://github.com/helgeho/HadoopConcatGz/stargazers) - A Splitable Hadoop InputFormat for Concatenated GZIP Files (and `*.warc.gz`). *(Stable)*
* [jwarc](https://github.com/iipc/jwarc) [![GitHub stars](https://img.shields.io/github/stars/iipc/jwarc?style=flat)](https://github.com/iipc/jwarc/stargazers) - Read and write WARC files with a type safe API (Java).
* [Jwat](https://github.com/netarchivesuite/jwat) [![GitHub stars](https://img.shields.io/github/stars/netarchivesuite/jwat?style=flat)](https://github.com/netarchivesuite/jwat/stargazers) - Libraries for reading/writing/validating WARC/ARC/GZIP files (Java). *(Stable)*
* [Jwat-Tools](https://github.com/netarchivesuite/jwat-tools) [![GitHub stars](https://img.shields.io/github/stars/netarchivesuite/jwat-tools?style=flat)](https://github.com/netarchivesuite/jwat-tools/stargazers) - Tools for reading/writing/validating WARC/ARC/GZIP files (Java). *(Stable)*
* [node-warc](https://github.com/N0taN3rd/node-warc) [![GitHub stars](https://img.shields.io/github/stars/N0taN3rd/node-warc?style=flat)](https://github.com/N0taN3rd/node-warc/stargazers) - Parse WARC files or create WARC files using either [Electron](https://electron.atom.io/) or [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) [![GitHub stars](https://img.shields.io/github/stars/cyrus-and/chrome-remote-interface?style=flat)](https://github.com/cyrus-and/chrome-remote-interface/stargazers) (Node.js). *(Stable)*
* [Sparkling](https://github.com/internetarchive/Sparkling) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/Sparkling?style=flat)](https://github.com/internetarchive/Sparkling/stargazers) - Internet Archive's Sparkling Data Processing Library. *(Stable)*
* [Unwarcit](https://github.com/emmadickson/unwarcit) [![GitHub stars](https://img.shields.io/github/stars/emmadickson/unwarcit?style=flat)](https://github.com/emmadickson/unwarcit/stargazers) - Command line interface to unzip WARC and WACZ files (Python).
* [warc](https://github.com/jedireza/warc) [![GitHub stars](https://img.shields.io/github/stars/jedireza/warc?style=flat)](https://github.com/jedireza/warc/stargazers) - A Rust library for reading and writing WARC files. *(Stable)*
* [Warcat](https://github.com/chfoo/warcat) [![GitHub stars](https://img.shields.io/github/stars/chfoo/warcat?style=flat)](https://github.com/chfoo/warcat/stargazers) - Tool and library for handling Web ARChive (WARC) files (Python). *(Stable)*
* [Warcat-rs](https://github.com/chfoo/warcat-rs) [![GitHub stars](https://img.shields.io/github/stars/chfoo/warcat-rs?style=flat)](https://github.com/chfoo/warcat-rs/stargazers) - Command-line tool and Rust library for handling Web ARChive (WARC) files. *(In Development)*
* [warcio](https://github.com/webrecorder/warcio) [![GitHub stars](https://img.shields.io/github/stars/webrecorder/warcio?style=flat)](https://github.com/webrecorder/warcio/stargazers) - Streaming WARC/ARC library for fast web archive IO (Python). *(Stable)*
* [warctools](https://github.com/internetarchive/warctools) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/warctools?style=flat)](https://github.com/internetarchive/warctools/stargazers) - Library to work with ARC and WARC files (Python).
* [webarchive](https://github.com/richardlehane/webarchive) [![GitHub stars](https://img.shields.io/github/stars/richardlehane/webarchive?style=flat)](https://github.com/richardlehane/webarchive/stargazers) - Golang readers for ARC and WARC webarchive formats (Golang).

### Analysis

* [Archives Research Compute Hub](https://github.com/internetarchive/arch) [![GitHub stars](https://img.shields.io/github/stars/internetarchive/arch?style=flat)](https://github.com/internetarchive/arch/stargazers) - Web application for distributed compute analysis of Archive-It web archive collections. *(Stable)*
* [ArchiveSpark](https://github.com/helgeho/ArchiveSpark) [![GitHub stars](https://img.shields.io/github/stars/helgeho/ArchiveSpark?style=flat)](https://github.com/helgeho/ArchiveSpark/stargazers) - An Apache Spark framework (not only) for Web Archives that enables easy data processing, extraction as well as derivation. *(Stable)*
* [Archives Unleashed Notebooks](https://github.com/archivesunleashed/notebooks) [![GitHub stars](https://img.shields.io/github/stars/archivesunleashed/notebooks?style=flat)](https://github.com/archivesunleashed/notebooks/stargazers) - Notebooks for working with web archives with the Archives Unleashed Toolkit, and derivatives generated by the Archives Unleashed Toolkit. *(Stable)*
* [Archives Unleashed Toolkit](https://github.com/archivesunleashed/aut) [![GitHub stars](https://img.shields.io/github/stars/archivesunleashed/aut?style=flat)](https://github.com/archivesunleashed/aut/stargazers) - Archives Unleashed Toolkit (AUT) is an open-source platform for analyzing web archives with Apache Spark. *(Stable)*
* [Common Crawl Columnar Index](https://commoncrawl.org/tag/columnar-index/) - SQL-queryable index, with CDX info plus language classification. *(Stable)*
* [Common Crawl Web Graph](https://commoncrawl.org/category/web-graph/) - A host or domain-level graph of the web, with ranking information. *(Stable)*
* [Common Crawl Jupyter notebooks](https://github.com/commoncrawl/cc-notebooks) [![GitHub stars](https://img.shields.io/github/stars/commoncrawl/cc-notebooks?style=flat)](https://github.com/commoncrawl/cc-notebooks/stargazers) - A collection of notebooks using Common Crawl's various datasets. *(Stable)*
* [Tweet Archvies Unleashed Toolkit](https://github.com/archivesunleashed/twut) [![GitHub stars](https://img.shields.io/github/stars/archivesunleashed/twut?style=flat)](https://github.com/archivesunleashed/twut/stargazers) - An open-source toolkit for analyzing line-oriented JSON Twitter archives with Apache Spark. *(In Development)*
* [Web Data Commons](http://webdatacommons.org/) - Structured data extracted from Common Crawl. *(Stable)*

### Quality Assurance

* [Chrome Check My Links](https://chromewebstore.google.com/detail/check-my-links/ojkcdipcgfaekbeaelaapakgnjflfglf) - Browser extension: a link checker with more options.
* [Chrome link checker](https://chromewebstore.google.com/detail/link-checker/aibjbgmpmnidnmagaefhmcjhadpffaoi) - Browser extension: basic link checker.
* [Chrome link gopher](https://chromewebstore.google.com/detail/bpjdkodgnbfalgghnbeggfbfjpcfamkf/publish-accepted?hl=en-US&gl=US) - Browser extension: link harvester on a page.
* [Chrome Open Multiple URLs](https://chromewebstore.google.com/detail/open-multiple-urls/oifijhaokejakekmnjmphonojcfkpbbh?hl=de) - Browser extension: opens multiple URLs and also extracts URLs from text.
* [Chrome Revolver](https://chromewebstore.google.com/detail/revolver-tabs/dlknooajieciikpedpldejhhijacnbda) - Browser extension: switches between browser tabs.
* [FlameShot](https://github.com/flameshot-org/flameshot) [![GitHub stars](https://img.shields.io/github/stars/flameshot-org/flameshot?style=flat)](https://github.com/flameshot-org/flameshot/stargazers) - Screen capture and annotation on Ubuntu.
* [PlayOnLinux](https://www.playonlinux.com/en/) - For running Xenu and Notepad++ on Ubuntu.
* [PlayOnMac](https://www.playonmac.com/en/) - For running Xenu and Notepad++ on macOS.
* [Windows Snipping Tool](https://support.microsoft.com/en-gb/help/13776/windows-use-snipping-tool-to-capture-screenshots) - Windows built-in for partial screen capture and annotation. On macOS you can use Command + Shift + 4 (keyboard shortcut for taking partial screen capture).
* [WineBottler](http://winebottler.kronenberg.org/) - For running Xenu and Notepad++ on macOS.
* [xDoTool](https://github.com/jordansissel/xdotool) [![GitHub stars](https://img.shields.io/github/stars/jordansissel/xdotool?style=flat)](https://github.com/jordansissel/xdotool/stargazers) - Click automation on Ubuntu.
* [Xenu](http://home.snafu.de/tilman/xenulink.html) - Desktop link checker for Windows.

### Curation

* [Zotero Robust Links Extension](https://robustlinks.mementoweb.org/zotero/) - A [Zotero](https://www.zotero.org/) extension that submits to and reads from web archives. Source [on GitHub](https://github.com/lanl/Zotero-Robust-Links-Extension) [![GitHub stars](https://img.shields.io/github/stars/lanl/Zotero-Robust-Links-Extension?style=flat)](https://github.com/lanl/Zotero-Robust-Links-Extension/stargazers). Supercedes [leonkt/zotero-memento](https://github.com/leonkt/zotero-memento) [![GitHub stars](https://img.shields.io/github/stars/leonkt/zotero-memento?style=flat)](https://github.com/leonkt/zotero-memento/stargazers).

## Community Resources

### Other Awesome Lists

* [Web Archiving Community](https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community) [![GitHub stars](https://img.shields.io/github/stars/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community?style=flat)](https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community/stargazers)
* [Awesome Memento](https://github.com/machawk1/awesome-memento) [![GitHub stars](https://img.shields.io/github/stars/machawk1/awesome-memento?style=flat)](https://github.com/machawk1/awesome-memento/stargazers)
* [The WARC Ecosystem](http://www.archiveteam.org/index.php?title=The_WARC_Ecosystem)
* [The Web Crawl section of COPTR](http://coptr.digipres.org/Category:Web_Crawl)

### Blogs and Scholarship

* [IIPC Blog](https://netpreserveblog.wordpress.com/)
* [Web Archiving Roundtable](https://webarchivingrt.wordpress.com/) - Unofficial blog of the Web Archiving Roundtable of the [Society of American Archivists](https://www2.archivists.org/) maintained by the members of the Web Archiving Roundtable.
* [The Web as History](https://www.uclpress.co.uk/products/84010) - An open-source book that provides a conceptual overview to web archiving research, as well as several case studies.
* [WS-DL Blog](https://ws-dl.blogspot.com/) - Web Science and Digital Libraries Research Group blogs about various Web archiving related topics, scholarly work, and academic trip reports.
* [DSHR's Blog](https://blog.dshr.org/) - David Rosenthal regularly reviews and summarizes work done in the Digital Preservation field.
* [UK Web Archive Blog](https://blogs.bl.uk/webarchive/)
* [Common Crawl Foundation Blog](https://commoncrawl.org/blog) - [rss](http://commoncrawl.org/blog/rss.xml)

### Mailing Lists

* [Common Crawl](https://groups.google.com/g/common-crawl)
* [IIPC](http://netpreserve.org/about-us/iipc-mailing-list/)
* [OpenWayback](https://groups.google.com/g/openwayback-dev)
* [WASAPI](https://groups.google.com/g/wasapi-community)

### Slack

* [IIPC Slack](https://iipc.slack.com/) - Ask [@netpreserve](https://twitter.com/NetPreserve?s=20) for access.
* [Archives Unleashed Slack](https://archivesunleashed.slack.com/) - [Fill out this request form](http://slack.archivesunleashed.org/) for access to a researcher group of people working with web archives.
* [Archivers Slack](https://archivers.slack.com) - [Invite yourself](https://archivers-slack.herokuapp.com/) to a multi-disciplinary effort for archiving projects run in affiliation with [EDGI](https://envirodatagov.org/archiving/) and [Data Together](http://datatogether.org/).
* [Common Crawl Foundation Partners](https://ccfpartners.slack.com/) (ask greg zat commoncrawl zot org for an invite)

### Discord

* [Common Crawl Foundation](https://discord.gg/njaVFh7avF)

### Twitter

* [@commoncrawl](https://twitter.com/commoncrawl) - Official Common Crawl Foundation handle.
* [@NetPreserve](https://twitter.com/NetPreserve) - Official IIPC handle.
* [@WebSciDL](https://twitter.com/WebSciDL) - ODU Web Science and Digital Libraries Research Group.
* [#WebArchiving](https://twitter.com/search?q=%23webarchiving)
* [#WebArchiveWednesday](https://twitter.com/hashtag/webarchivewednesday)

## Web Archiving Service Providers

The intention is that we only list services that allow web archives to be exported in standard formats (WARC or WACZ). But this is not an endorsement of these services, and readers should check and evaluate these options based on their needs.

### Self-hostable, Open Source

*	[Browsertrix](https://webrecorder.net/browsertrix/) - From [Webrecorder](https://webrecorder.net/), source available at <https://github.com/webrecorder/browsertrix>.
*	[Conifer](https://conifer.rhizome.org/) - From [Rhizome](https://rhizome.org/), source available at <https://github.com/Rhizome-Conifer>.

### Hosted, Closed Source

* [Archive-It](https://archive-it.org/) - From the Internet Archive.
* [Arkiwera](https://arkiwera.se/wp/websites/)
*	[Hanzo](https://www.hanzo.co/chronicle)
*	[MirrorWeb](https://www.mirrorweb.com/solutions/capabilities/website-archiving)
*	[PageFreezer](https://www.pagefreezer.com/)
*	[Smarsh](https://www.smarsh.com/platform/compliance-management/web-archive)

## Public Data

This is a list of publicly available WARCs, Wayback Machines, CDX API endpoints, other indexes, and so on.

* [Common Crawl files](https://data.commoncrawl.org/) - WARCs, CDX files, parquet url index, parquet host index, etc.
* [Common Crawl CDX API](https://index.commoncrawl.org/)
* [End of Term Archive](https://eotarchive.org/) - WARCs, CDX files, parquet url index
* [Internet Archive Wayback](https://web.archive.org/)
* [Webrecorder US GovArchive](https://govarchive.us/) - high-fidelity replay
* [UK Government Web Archive](https://www.nationalarchives.gov.uk/webarchive/) - Wayback
