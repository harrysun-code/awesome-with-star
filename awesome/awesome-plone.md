# Plone

[![GitHub stars](https://img.shields.io/github/stars/collective/awesome-plone?style=flat)](https://github.com/collective/awesome-plone/stargazers)

# Awesome Plone [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
[<img align="right" src="logo.png" height="64">](https://plone.org)

> A community-curated list of _awesome_ Plone add-ons.

<!--lint ignore double-link-->
[Plone](https://plone.org) is a open source CMS written in Python with a focus on functionality, customizability and security out of the box.

<!--lint ignore double-link-->
There are over 3000 add-ons for [Plone on PyPi](https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Plone) and over 1500 repositories in the [Collective](https://github.com/collective) [![GitHub stars](https://img.shields.io/github/stars/collective?style=flat)](https://github.com/collective/stargazers) organization on GitHub. If you want to know if there is already a add-on for Plone that fits your needs, searching for it on GitHub or PyPi can be hard. It's hard to understand which one could be a good solution or not.

This list is intended to fill that gap, and create a shared knowledge about common products and techniques.

For a filterable list of addons aggreating all Plone related packages from PyPi see https://pag.derico.tech.

This list only covers add-ons that work with the latest major versions of Plone (currently 5.2 and 6) and only those that support Python 3.

Plone 6 comes with a new default frontend called Volto, which is written in React and uses `plone.restapi` to communicate with Plone. Volto is very extendable in itself. Checkout the [awesome-volto list](https://github.com/collective/awesome-volto) [![GitHub stars](https://img.shields.io/github/stars/collective/awesome-volto?style=flat)](https://github.com/collective/awesome-volto/stargazers) for add-ons to Volto.


## Contents

* [Content and utilities for content](#content-and-utilities-for-content)
* [Editing](#editing)
* [Searching and Categorizing](#searching-and-categorizing)
* [Layout](#layout)
* [Tiles](#tiles)
* [Events](#events)
* [Forms](#forms)
* [Multilingual](#multilingual)
* [Media](#media)
* [Security](#security)
* [SEO](#seo)
* [Authentication](#authentication)
* [Shop](#shop)
* [Export, Import and Migrations](#export-import-and-migrations)
* [Themes](#themes)
* [Develop](#develop)
* [Sysadmin](#sysadmin)
* [Finding more add-ons](#finding-more-add-ons)
* [Official resources](#official-resources)

---

## Content and utilities for content

_Add-ons that provide content-types or additional functionality for content_

* [collective.consent](https://github.com/collective/collective.consent) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.consent?style=flat)](https://github.com/collective/collective.consent/stargazers) - Ask users for consent to different topics, before they can continue.
* [collective.dexteritytextindexer](https://github.com/collective/collective.dexteritytextindexer) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.dexteritytextindexer?style=flat)](https://github.com/collective/collective.dexteritytextindexer/stargazers) - Dynamic SearchableText index for dexterity content types. For Plone 6 this was merged into Plone core.
* [collective.documentgenerator](https://github.com/collective/collective.documentgenerator) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.documentgenerator?style=flat)](https://github.com/collective/collective.documentgenerator/stargazers) - Generate Documents (.odt, .pdf, .doc) from content based on appy framework (https://appyframe.work/) and OpenOffice/LibreOffice.
* [collective.documentviewer](https://github.com/collective/collective.documentviewer) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.documentviewer?style=flat)](https://github.com/collective/collective.documentviewer/stargazers) - Very nice document viewer that integrates DocumentCloud viewer and PDF processing into Plone.
* [collective.easyformplugin.createdx](https://github.com/collective/collective.easyformplugin.createdx) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.easyformplugin.createdx?style=flat)](https://github.com/collective/collective.easyformplugin.createdx/stargazers) - Creates Plone content objects from EasyForm submissions.
* [collective.embeddedpage](https://github.com/collective/collective.embeddedpage) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.embeddedpage?style=flat)](https://github.com/collective/collective.embeddedpage/stargazers) - A content type to embed remote HTML pages in Plone Classic and Volto.
* [collective.folderishtraverse](https://github.com/collective/collective.folderishtraverse) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.folderishtraverse?style=flat)](https://github.com/collective/collective.folderishtraverse/stargazers) - Traverse to first item in folder.
* [collective.folderishtypes](https://github.com/collective/collective.folderishtypes) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.folderishtypes?style=flat)](https://github.com/collective/collective.folderishtypes/stargazers) - Provides the types "Folderish Event", "Folderish News Item" and "Folderish Document" as replacements for default types. Those types are able to hold any other content, like a Folder.
* [collective.geolocationbehavior](https://github.com/collective/collective.geolocationbehavior) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.geolocationbehavior?style=flat)](https://github.com/collective/collective.geolocationbehavior/stargazers) - Geotagging for Plone content using LeafletJS.
* [collective.glossary](https://github.com/collective/collective.glossary) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.glossary?style=flat)](https://github.com/collective/collective.glossary/stargazers) - Content type to define a glossary and its terms.
* [collective.immediatecreate](https://github.com/collective/collective.immediatecreate) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.immediatecreate?style=flat)](https://github.com/collective/collective.immediatecreate/stargazers) - Create content immediatly and skip the add form.
* [collective.lineage](https://github.com/collective/collective.lineage) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.lineage?style=flat)](https://github.com/collective/collective.lineage/stargazers) - Subsites: Turns subfolders of a Plone site to appear as autonomous Plone sites. There is also a whole ecosystem off addons specific to subsites.
* [collective.mailchimp](https://github.com/collective/collective.mailchimp) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.mailchimp?style=flat)](https://github.com/collective/collective.mailchimp/stargazers) - MailChimp newsletter integration for Plone.
* [collective.mirror](https://github.com/collective/collective.mirror) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.mirror?style=flat)](https://github.com/collective/collective.mirror/stargazers) - A content type that mirrors the content of any other container.
* [collective.mustread](https://github.com/collective/collective.mustread) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.mustread?style=flat)](https://github.com/collective/collective.mustread/stargazers) - Tracking user views on content that are marked as must-read.
* [collective.person](https://github.com/collective/collective.person) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.person?style=flat)](https://github.com/collective/collective.person/stargazers) - A content type to represent a person, with an optional behavior to connect it to a Plone user.
* [collective.pdfjs](https://github.com/collective/collective.pdfjs) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.pdfjs?style=flat)](https://github.com/collective/collective.pdfjs/stargazers) - Plone integration for Mozilla's JavaScript PDF reader.
* [collective.remoteproxy](https://github.com/collective/collective.remoteproxy) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.remoteproxy?style=flat)](https://github.com/collective/collective.remoteproxy/stargazers) - Proxy for remote content. All remote URLs for which a local proxy was created are replaced in the resulting content.
* [collective.restrictportlets](https://github.com/collective/collective.restrictportlets) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.restrictportlets?style=flat)](https://github.com/collective/collective.restrictportlets/stargazers) - Allows you to restrict the available portlets that non-Managers can add.
* [collective.workspace](https://github.com/collective/collective.workspace) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.workspace?style=flat)](https://github.com/collective/collective.workspace/stargazers) - Easily manage 'membership' in specific areas of a Plone Site. It allows to grant people access to areas of content using a membership group rather than local roles for each user, and to delegate control over that group to people who don't have access to the site-wide user/group control panel.
* [dexterity.membrane](https://github.com/collective/dexterity.membrane) [![GitHub stars](https://img.shields.io/github/stars/collective/dexterity.membrane?style=flat)](https://github.com/collective/dexterity.membrane/stargazers) - Enables content to be used as users and groups in Plone sites.
* [plone.pdfexport](https://github.com/plone/plone.pdfexport) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.pdfexport?style=flat)](https://github.com/plone/plone.pdfexport/stargazers) - Generic PDF export functionality for Plone content.
* [Products.EasyNewsletter](https://github.com/collective/Products.EasyNewsletter) [![GitHub stars](https://img.shields.io/github/stars/collective/Products.EasyNewsletter?style=flat)](https://github.com/collective/Products.EasyNewsletter/stargazers) - Powerful newsletter/mailing product for Plone.
* [zopyx.ipsumplone](https://github.com/zopyx/zopyx.ipsumplone) [![GitHub stars](https://img.shields.io/github/stars/zopyx/zopyx.ipsumplone?style=flat)](https://github.com/zopyx/zopyx.ipsumplone/stargazers) - Creates demo content and demo images for Plone.
* [collective.folderorder](https://github.com/collective/collective.folderorder) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.folderorder?style=flat)](https://github.com/collective/collective.folderorder/stargazers) - Allows alternative ordering on plone folders.


## Editing

* [collective.a11ycheck](https://github.com/collective/collective.a11ycheck) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.a11ycheck?style=flat)](https://github.com/collective/collective.a11ycheck/stargazers) - Reports accessibility issues to your site editors when a page is saved.
* [collective.collabora](https://github.com/collective/collective.collabora) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.collabora?style=flat)](https://github.com/collective/collective.collabora/stargazers) - Collabora Online integration for Plone to provide collaborative document editing.
* [collective.bbcodesnippets](https://github.com/collective/collective.bbcodesnippets) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.bbcodesnippets?style=flat)](https://github.com/collective/collective.bbcodesnippets/stargazers) - Provides generic and extensible BBCode markup integration for Plone.
* [collective.richdescription](https://github.com/collective/collective.richdescription) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.richdescription?style=flat)](https://github.com/collective/collective.richdescription/stargazers) - Formatable description field for Plone.


## Searching and Categorizing

* [cioppino.twothumbs](https://github.com/collective/cioppino.twothumbs) [![GitHub stars](https://img.shields.io/github/stars/collective/cioppino.twothumbs?style=flat)](https://github.com/collective/cioppino.twothumbs/stargazers) - Rate content using up- and down-thumbs.
* [collective.bookmarks](https://github.com/collective/collective.bookmarks) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.bookmarks?style=flat)](https://github.com/collective/collective.bookmarks/stargazers) - Bookmarks/ favorites/ wish-list for Plone.
* [collective.collectionfilter](https://github.com/collective/collective.collectionfilter) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.collectionfilter?style=flat)](https://github.com/collective/collective.collectionfilter/stargazers) - Faceted navigation filter for collection or contentlisting tiles.
* [collective.elasticsearch](https://github.com/collective/collective.elasticsearch) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.elasticsearch?style=flat)](https://github.com/collective/collective.elasticsearch/stargazers) - Use Elasticsearch as the search backend for Plone.
* [collective.elastic.plone](https://github.com/collective/collective.elastic.plone) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.elastic.plone?style=flat)](https://github.com/collective/collective.elastic.plone/stargazers) - Elasticsearch Integration for Plone content.
* [collective.searchandreplace](https://github.com/collective/collective.searchandreplace) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.searchandreplace?style=flat)](https://github.com/collective/collective.searchandreplace/stargazers) - Find and replace text in Plone content objects.
* [collective.solr](https://github.com/collective/collective.solr) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.solr?style=flat)](https://github.com/collective/collective.solr/stargazers) - Solr search engine integration for Plone.
* [collective.taxonomy](https://github.com/collective/collective.taxonomy) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.taxonomy?style=flat)](https://github.com/collective/collective.taxonomy/stargazers) - Create, edit and use hierarchical taxonomies to categorize content.
* [eea.facetednavigation](https://github.com/collective/eea.facetednavigation) [![GitHub stars](https://img.shields.io/github/stars/collective/eea.facetednavigation?style=flat)](https://github.com/collective/eea.facetednavigation/stargazers) - Very powerful interface to improve search without programming skills. Configuration is done through-the-web and lets you gradually select and explore different facets (metadata/properties) of the content and narrow down you search quickly and dynamically.
* [Products.PloneKeywordManager](https://github.com/collective/Products.PloneKeywordManager) [![GitHub stars](https://img.shields.io/github/stars/collective/Products.PloneKeywordManager?style=flat)](https://github.com/collective/Products.PloneKeywordManager/stargazers) - Change, merge and delete keywords/tags/subjects).
* [zopyx.typesense](https://github.com/zopyx/zopyx.typesense) [![GitHub stars](https://img.shields.io/github/stars/zopyx/zopyx.typesense?style=flat)](https://github.com/zopyx/zopyx.typesense/stargazers) - Plone integration with the external Typesense search server (open-source). This is an alternative to collective.solr or Elasticsearch.


## Layout

_Products and resources that help developers and users to create and manage site layouts._

* [plone.app.mosaic](https://github.com/plone/plone.app.mosaic) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.app.mosaic?style=flat)](https://github.com/plone/plone.app.mosaic/stargazers) - Powerful and extendable editor that allows users to compose the content of a page with different tiles.
* [collective.cover](https://github.com/collective/collective.cover) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.cover?style=flat)](https://github.com/collective/collective.cover/stargazers) - Cover allows the creation of elaborate covers built around a drag-and-drop interface. Uses the same blocks/tiles ecosystem as plone.app.mosaic but a different approach to editing.
* [collective.contentsections](https://github.com/collective/collective.contentsections) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.contentsections?style=flat)](https://github.com/collective/collective.contentsections/stargazers) - Offers a block approach for Plone 6 Classic based entirely on Dexterity content types.
* [collective.gridlisting](https://github.com/collective/collective.gridlisting) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.gridlisting?style=flat)](https://github.com/collective/collective.gridlisting/stargazers) - Adds a dexterity behavior and a browser template to manipulate folder and collection listings by adding Bootstrap 5 CSS classes and `pat-masonry` from patternslib. 


## Tiles

_Add-ons that extend the layout editor plone.app.mosaic._

* [plone.app.standardtiles](https://github.com/plone/plone.app.standardtiles) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.app.standardtiles?style=flat)](https://github.com/plone/plone.app.standardtiles/stargazers) - A set of standard tiles used by Mosaic, but can be used from any other tile manager.
* [collective.tiles.carousel](https://github.com/collective/collective.tiles.carousel) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.tiles.carousel?style=flat)](https://github.com/collective/collective.tiles.carousel/stargazers) - A slider tile for plone.app.mosaic based on the carousel component of Bootstrap 5.
* [collective.tiles.advancedstatic](https://github.com/collective/collective.tiles.advancedstatic) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.tiles.advancedstatic?style=flat)](https://github.com/collective/collective.tiles.advancedstatic/stargazers) - A tile that shows html text (similar to the static text portlet), with some additional configuration like the possibility to add custom css classes.
* [collective.tiles.collection](https://github.com/collective/collective.tiles.collection) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.tiles.collection?style=flat)](https://github.com/collective/collective.tiles.collection/stargazers) - A tile that shows a set of collection results with possibility to choose (and develop) custom layouts.


## Events

_Add-ons that handle events and calendars._

* [collective.easyformplugin.registration](https://github.com/collective/collective.easyformplugin.registration) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.easyformplugin.registration?style=flat)](https://github.com/collective/collective.easyformplugin.registration/stargazers) - Add a behavior to collective.easyform to manage registration forms for events.
* [collective.fullcalendar](https://github.com/collective/collective.fullcalendar) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.fullcalendar?style=flat)](https://github.com/collective/collective.fullcalendar/stargazers) - Display events in a nice calendar UI using https://fullcalendar.io.
* [collective.venue](https://github.com/collective/collective.venue) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.venue?style=flat)](https://github.com/collective/collective.venue/stargazers) - Venue type with geolocation support for use with events or any other location specific content.


## Forms

_Add-ons that allow generating and using forms._

* [collective.easyform](https://github.com/collective/collective.easyform) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.easyform?style=flat)](https://github.com/collective/collective.easyform/stargazers) - EasyForm provides a Plone form builder through-the-web using fields, widgets, actions and validators. Form input can be saved or emailed. A simple and user-friendly interface allows non-programmers to create custom forms.
* [collective.fieldedit](https://github.com/collective/collective.fieldedit) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.fieldedit?style=flat)](https://github.com/collective/collective.fieldedit/stargazers) - A flexible form to edit selected fields of a content type.
* [collective.honeypot](https://github.com/collective/collective.honeypot) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.honeypot?style=flat)](https://github.com/collective/collective.honeypot/stargazers) - Honeypot protection for forms.
* [collective.z3cform.datagridfield](https://github.com/collective/collective.z3cform.datagridfield) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.z3cform.datagridfield?style=flat)](https://github.com/collective/collective.z3cform.datagridfield/stargazers) - A field with a datagrid (table), where each row is a sub form.
* [collective.z3cform.norobots](https://github.com/collective/collective.z3cform.norobots) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.z3cform.norobots?style=flat)](https://github.com/collective/collective.z3cform.norobots/stargazers) - A "human" captcha widget based on a list of questions/answers.
* [plone.formwidgets.hcaptcha](https://github.com/plone/plone.formwidget.hcaptcha) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.formwidget.hcaptcha?style=flat)](https://github.com/plone/plone.formwidget.hcaptcha/stargazers) - HCaptcha widget to protect Plone from bots, spam, and other forms of automated abuse.
* [yafowil.plone](https://github.com/bluedynamics/yafowil.plone) [![GitHub stars](https://img.shields.io/github/stars/bluedynamics/yafowil.plone?style=flat)](https://github.com/bluedynamics/yafowil.plone/stargazers) - Yafowil is a form library for Python. This is its Plone Integration package.


## Multilingual

_Add-ons to help manage multilingual sites._

* [collective.linguatags](https://github.com/collective/collective.linguatags) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.linguatags?style=flat)](https://github.com/collective/collective.linguatags/stargazers) - Multilingual Tags for Plone.
* [plone.app.multilingualindexes](https://github.com/plone/plone.app.multilingualindexes) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.app.multilingualindexes?style=flat)](https://github.com/plone/plone.app.multilingualindexes/stargazers) - Indexes optimized to query multilingual content made with plone.app.multilingual.
* [cs.adminlanguage](https://github.com/codesyntax/cs.adminlanguage) [![GitHub stars](https://img.shields.io/github/stars/codesyntax/cs.adminlanguage?style=flat)](https://github.com/codesyntax/cs.adminlanguage/stargazers) - Configure a language to be used when editing your Plone site, independent to the site language.
* [collective.multilingual](https://github.com/collective/collective.multilingual/tree/fix-tests) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.multilingual/tree/fix-tests?style=flat)](https://github.com/collective/collective.multilingual/tree/fix-tests/stargazers) - This add-on provides support for content in multiple languages (multilingual).


## Media

_Add-ons that handle image, video and audio content._

* [collective.autoscaling](https://github.com/collective/collective.autoscaling) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.autoscaling?style=flat)](https://github.com/collective/collective.autoscaling/stargazers) - Automatic scaling of large images. Useful to reduce your database size when editors upload too large images.
* [collective.behavior.banner](https://github.com/collective/collective.behavior.banner) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.behavior.banner?style=flat)](https://github.com/collective/collective.behavior.banner/stargazers) - A behavior to create banners and sliders from banners.
* [collective.behavior.relatedmedia](https://github.com/collective/collective.behavior.relatedmedia) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.behavior.relatedmedia?style=flat)](https://github.com/collective/collective.behavior.relatedmedia/stargazers) - A behavior to create/upload/manage media relations (Image, File) for content types.
* [collective.lazysizes](https://github.com/collective/collective.lazysizes) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.lazysizes?style=flat)](https://github.com/collective/collective.lazysizes/stargazers) - Integration of lazysizes, a lightweight lazy loader, into Plone.
* [collective.wavesurfer](https://github.com/collective/collective.wavesurfer) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.wavesurfer?style=flat)](https://github.com/collective/collective.wavesurfer/stargazers) - Implementation of https://wavesurfer-js.org audio player for Plone.
* [plone.app.imagecropping](https://github.com/collective/plone.app.imagecropping) [![GitHub stars](https://img.shields.io/github/stars/collective/plone.app.imagecropping?style=flat)](https://github.com/collective/plone.app.imagecropping/stargazers) - Crops Images in Plone manually using cropper JS library.
* [plone.gallery](https://github.com/plone/plone.gallery) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.gallery?style=flat)](https://github.com/plone/plone.gallery/stargazers) - Photo gallery view for Plone.
* [redturtle.gallery](https://github.com/RedTurtle/redturtle.gallery) [![GitHub stars](https://img.shields.io/github/stars/RedTurtle/redturtle.gallery?style=flat)](https://github.com/RedTurtle/redturtle.gallery/stargazers) - Adds a gallery view with a carousel made with slick.
* [wildcard.media](https://github.com/collective/wildcard.media) [![GitHub stars](https://img.shields.io/github/stars/collective/wildcard.media?style=flat)](https://github.com/collective/wildcard.media/stargazers) - Provides audio and video content types and behaviors.
* [cs_flickrgallery](https://github.com/codesyntax/cs_flickrgallery) [![GitHub stars](https://img.shields.io/github/stars/codesyntax/cs_flickrgallery?style=flat)](https://github.com/codesyntax/cs_flickrgallery/stargazers) - Flickr photo gallery support for Plone.


## Security

* [collective.explicitacquisition](https://github.com/collective/collective.explicitacquisition) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.explicitacquisition?style=flat)](https://github.com/collective/collective.explicitacquisition/stargazers) - Disallow access to acquired content outside the current path.
* [collective.geotransform](https://github.com/collective/collective.geotransform) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.geotransform?style=flat)](https://github.com/collective/collective.geotransform/stargazers) - Graceful E-mail Obfuscation for Plone.
* [collective.contactformprotection](https://github.com/collective/collective.contactformprotection) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.contactformprotection?style=flat)](https://github.com/collective/collective.contactformprotection/stargazers) - Disables the default `contact-info` form or protect it with `plone.formwidget.[h|re]captcha`.
* [collective.lockdown](https://github.com/collective/collective.lockdown) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.lockdown?style=flat)](https://github.com/collective/collective.lockdown/stargazers) - Protect Plone sites against site administrators from reconfiguring the site or making layout changes.


## SEO

_Add-ons for search engine optimization._

* [bda.plone.gtm](https://github.com/bluedynamics/bda.plone.gtm) [![GitHub stars](https://img.shields.io/github/stars/bluedynamics/bda.plone.gtm?style=flat)](https://github.com/bluedynamics/bda.plone.gtm/stargazers) - Google Tag Manager Integration.
* [collective.behavior.seo](https://github.com/collective/collective.behavior.seo) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.behavior.seo?style=flat)](https://github.com/collective/collective.behavior.seo/stargazers) - Adds extra fields used for SEO optimisation.
* [collective.splitsitemap](https://github.com/collective/collective.splitsitemap) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.splitsitemap?style=flat)](https://github.com/collective/collective.splitsitemap/stargazers) - Provides a cached split sitemap on big public sites.
* [kitconcept.seo](https://github.com/kitconcept/kitconcept.seo) [![GitHub stars](https://img.shields.io/github/stars/kitconcept/kitconcept.seo?style=flat)](https://github.com/kitconcept/kitconcept.seo/stargazers) - Adds extra fields used for SEO optimisation for sites using Volto.


## Authentication

_A list of authentication plugins, to integrate Plone with external user , Importsources and Migrations.import_

* [pas.plugins.ldap](https://github.com/collective/pas.plugins.ldap) [![GitHub stars](https://img.shields.io/github/stars/collective/pas.plugins.ldap?style=flat)](https://github.com/collective/pas.plugins.ldap/stargazers) - Provides users and groups from a LDAP directory.
* [pas.plugins.authomatic](https://github.com/collective/pas.plugins.authomatic) [![GitHub stars](https://img.shields.io/github/stars/collective/pas.plugins.authomatic?style=flat)](https://github.com/collective/pas.plugins.authomatic/stargazers) - Authomatic OAuth1/OAuth2/OpenID Login Integration with Plone.
* [pas.plugins.eea](https://github.com/collective/pas.plugins.eea) [![GitHub stars](https://img.shields.io/github/stars/collective/pas.plugins.eea?style=flat)](https://github.com/collective/pas.plugins.eea/stargazers) - Provides user and group enumeration on top of pas.plugins.authomatic, with support for Microsoft Entra ID. Includes user and group synchronization.
* [iw.rejectanonymous](https://github.com/collective/iw.rejectanonymous) [![GitHub stars](https://img.shields.io/github/stars/collective/iw.rejectanonymous?style=flat)](https://github.com/collective/iw.rejectanonymous/stargazers) - Reject unconditionnally anonymous users from a Plone site, without any change in your security policy matrix or workflows. The basic use case is an extranet, where all visitors must be authenticated.
* [pas.plugins.headers](https://github.com/collective/pas.plugins.headers) [![GitHub stars](https://img.shields.io/github/stars/collective/pas.plugins.headers?style=flat)](https://github.com/collective/pas.plugins.headers/stargazers) - Reads request headers and uses them for authentication. Think SAML headers that are set by a front web server like Apache or nginx.
* [dm.zope.saml2](https://pypi.org/project/dm.zope.saml2/) - Supports SAML2 based Single Sign-On.
* [collective.impersonate](https://github.com/collective/collective.impersonate) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.impersonate?style=flat)](https://github.com/collective/collective.impersonate/stargazers) - Allow administrators to impersonate another user. Useful for verifying workflow/permission set up on real content.
* [collective.pwexpiry](https://github.com/collective/collective.pwexpiry) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.pwexpiry?style=flat)](https://github.com/collective/collective.pwexpiry/stargazers) - Provideds methods for stronger user passwords in Plone and password attack protection.
* [pas.plugins.oidc](https://github.com/collective/pas.plugins.oidc) [![GitHub stars](https://img.shields.io/github/stars/collective/pas.plugins.oidc?style=flat)](https://github.com/collective/pas.plugins.oidc/stargazers) - Login using OIDC providers.
* [wcs.samlauth](https://github.com/collective/wcs.samlauth) [![GitHub stars](https://img.shields.io/github/stars/collective/wcs.samlauth?style=flat)](https://github.com/collective/wcs.samlauth/stargazers) - Login using SAML providers.


## Shop

* [bda.plone.productshop](https://github.com/bluedynamics/bda.plone.productshop) [![GitHub stars](https://img.shields.io/github/stars/bluedynamics/bda.plone.productshop?style=flat)](https://github.com/bluedynamics/bda.plone.productshop/stargazers) - Flexible and modular e-commerce solution for Plone.


## Export, Import and Migrations

* [collective.exportimport](https://github.com/collective/collective.exportimport) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.exportimport?style=flat)](https://github.com/collective/collective.exportimport/stargazers) - Export and import content and a lot of other data from and to Plone. The main solution for all kinds of migrations based on plone.restapi.
* [collective.migrationhelpers](https://github.com/collective/collective.migrationhelpers) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.migrationhelpers?style=flat)](https://github.com/collective/collective.migrationhelpers/stargazers) - Helpers and examples to use during migrations.
* [collective.jsonify](https://github.com/collective/collective.jsonify) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.jsonify?style=flat)](https://github.com/collective/collective.jsonify/stargazers) - Export Plone content to JSON.
* [collective.transmogrifier](https://github.com/collective/collective.transmogrifier) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.transmogrifier?style=flat)](https://github.com/collective/collective.transmogrifier/stargazers) - A configurable pipeline, aimed at transforming content for import and export.


## Themes

* [plonetheme.tokyo](https://github.com/collective/plonetheme.tokyo) [![GitHub stars](https://img.shields.io/github/stars/collective/plonetheme.tokyo?style=flat)](https://github.com/collective/plonetheme.tokyo/stargazers) - A alternative theme for Plone using Bootstrap 5.
* [plonetheme.grueezibuesi](https://github.com/collective/plonetheme.grueezibuesi) [![GitHub stars](https://img.shields.io/github/stars/collective/plonetheme.grueezibuesi?style=flat)](https://github.com/collective/plonetheme.grueezibuesi/stargazers) - A kitten inspired theme for Plone 6.
* [collective.sidebar](https://github.com/collective/collective.sidebar) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.sidebar?style=flat)](https://github.com/collective/collective.sidebar/stargazers) - A sidebar that consolidates toolbar and navigation.
* [collective.editablemenu](https://github.com/RedTurtle/collective.editablemenu) [![GitHub stars](https://img.shields.io/github/stars/RedTurtle/collective.editablemenu?style=flat)](https://github.com/RedTurtle/collective.editablemenu/stargazers) - A customizable navigation menu for Plone.
* [collective.localstyles](https://github.com/collective/collective.localstyles) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.localstyles?style=flat)](https://github.com/collective/collective.localstyles/stargazers) - Add local styles within any subsection of a Plone site by adding a css-file.


## Develop

_Add-ons that help developing Plone_

* [Products.PDBDebugMode](https://github.com/collective/Products.PDBDebugMode) [![GitHub stars](https://img.shields.io/github/stars/collective/Products.PDBDebugMode?style=flat)](https://github.com/collective/Products.PDBDebugMode/stargazers) - Post-mortem debugging: open a pdb session whenever an exception occurs so you you can find out what is going wrong. Plus: By adding /pdb to a url you end up you in a pdb session on the current context. A killer tool for developers.
* [plone.app.debugtoolbar](https://github.com/plone/plone.app.debugtoolbar) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.app.debugtoolbar?style=flat)](https://github.com/plone/plone.app.debugtoolbar/stargazers) - A toolbar that shows a wealth of debug information about a running Plone site and the content you are inspecting. Also includes a interactive python-shell, a TALES-expression evaluator and and code-reload.
* [plone.reload](https://github.com/plone/plone.reload) [![GitHub stars](https://img.shields.io/github/stars/plone/plone.reload?style=flat)](https://github.com/plone/plone.reload/stargazers) - Code and configuration reload without server restarts.
* [Products.PrintingMailHost](https://github.com/collective/Products.PrintingMailHost) [![GitHub stars](https://img.shields.io/github/stars/collective/Products.PrintingMailHost?style=flat)](https://github.com/collective/Products.PrintingMailHost/stargazers) - Log mail messages instead of sending mail.
* [experimental.gracefulblobmissing](https://github.com/collective/experimental.gracefulblobmissing/) [![GitHub stars](https://img.shields.io/github/stars/collective/experimental.gracefulblobmissing/?style=flat)](https://github.com/collective/experimental.gracefulblobmissing//stargazers) - Gracefully handle missing binary files in Plone.
* [collective.debugtools](https://github.com/collective/collective.debugtools) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.debugtools?style=flat)](https://github.com/collective/collective.debugtools/stargazers) - Add remote debugging via debugpy for debugpy-compatible clients like VSCode or PyCharm.
* [collective.icecream](https://github.com/collective/collective.icecream) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.icecream?style=flat)](https://github.com/collective/collective.icecream/stargazers) - Debug and inspect Plone using the icecream package. 
* [collective.patchwatcher](https://github.com/collective/collective.patchwatcher) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.patchwatcher?style=flat)](https://github.com/collective/collective.patchwatcher/stargazers) - A companion for keeping track of patched or overridden files.
* [collective.pdbpp](https://github.com/collective/collective.pdbpp) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.pdbpp?style=flat)](https://github.com/collective/collective.pdbpp/stargazers) - Allows you to use the pdbpp package.
* [collective.relationhelpers](https://github.com/collective/collective.relationhelpers) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.relationhelpers?style=flat)](https://github.com/collective/collective.relationhelpers/stargazers) - Helpers to manage, create, export and rebuild relations in Plone 5.x. For Plone 6 this was merged into Plone core.


## Sysadmin

_Add-ons that help admins deploying and maintaining Plone_

* [collective.catalogcleanup](https://github.com/collective/collective.catalogcleanup) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.catalogcleanup?style=flat)](https://github.com/collective/collective.catalogcleanup/stargazers) - Removes data from the catalog that no longer belong to an actual object.
* [collective.fingerpointing](https://github.com/collective/collective.fingerpointing) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.fingerpointing?style=flat)](https://github.com/collective/collective.fingerpointing/stargazers) - Keeps track of different events and write them down to an audit log.
* [collective.ftw.upgrade](https://github.com/collective/collective.ftw.upgrade) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.ftw.upgrade?style=flat)](https://github.com/collective/collective.ftw.upgrade/stargazers) - Simplifies writing and running upgrade steps for Plone add-ons and projects.
* [collective.ifttt](https://github.com/collective/collective.ifttt) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.ifttt?style=flat)](https://github.com/collective/collective.ifttt/stargazers) - Enables any Plone site to play in the IFTTT ecosystem. For example when a news item is published, then tweet about it or post it on Facebook.
* [collective.purgebyid](https://github.com/collective/collective.purgebyid) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.purgebyid?style=flat)](https://github.com/collective/collective.purgebyid/stargazers) - Use tag-based cache invalidation in Plone (e.g. with Varnish's xkey module).
* [collective.recipe.backup](https://github.com/collective/collective.recipe.backup) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.recipe.backup?style=flat)](https://github.com/collective/collective.recipe.backup/stargazers) - Powerful and flexible backup/restore solution for Plone.
* [collective.regenv](https://github.com/collective/collective.regenv) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.regenv?style=flat)](https://github.com/collective/collective.regenv/stargazers) - Override registry settings using environment variables stored in a file.
* [plone-registryfromenviron](https://github.com/bluedynamics/plone-registryfromenviron) [![GitHub stars](https://img.shields.io/github/stars/bluedynamics/plone-registryfromenviron?style=flat)](https://github.com/bluedynamics/plone-registryfromenviron/stargazers) - Override plone.registry settings from environment variables.
* [collective.revisionmanager](https://github.com/collective/collective.revisionmanager) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.revisionmanager?style=flat)](https://github.com/collective/collective.revisionmanager/stargazers) - Manage Products.CMFEditions histories that can bloat your database.
* [collective.sentry](https://github.com/collective/collective.sentry) [![GitHub stars](https://img.shields.io/github/stars/collective/collective.sentry?style=flat)](https://github.com/collective/collective.sentry/stargazers) - Sentry integration to aggregate errors and help finding their causes.
* [dm.historical](https://pypi.org/project/dm.historical) - Access any historical state of your database. Can be useful to find out what happened to objects in the past and to restore accidentally deleted or modified objects.
* [haufe.requestmonitoring](https://github.com/collective/haufe.requestmonitoring) [![GitHub stars](https://img.shields.io/github/stars/collective/haufe.requestmonitoring?style=flat)](https://github.com/collective/haufe.requestmonitoring/stargazers) - Detailed request logging functionality on top of the publication events. Useful to find out what takes longer than it should.
* [Cloudbrine](https://bluedynamics.github.io/zodb-pgjsonb/ecosystem.html) - A set of add-ons that replace the ZODB and the catalog with PostgreSQL and stores objects as queryable JSONB and can delegate image scaling to Thumbor.


## Finding more add-ons

Finding the right add-on for your needs can sometimes be challenging.
Here are a few tips to help you:

<!--lint ignore double-link-->
* Start by making a list of the features you require.
* Check this list first to see if any existing add-ons meet your needs.
* Search for Plone add-ons on [PyPi](https://pypi.org/search/?c=Framework+%3A%3A+Plone).
* Browse the [Collective](https://github.com/collective) [![GitHub stars](https://img.shields.io/github/stars/collective?style=flat)](https://github.com/collective/stargazers) organization on GitHub.
* Browse the [Plone](https://github.com/plone) [![GitHub stars](https://img.shields.io/github/stars/plone?style=flat)](https://github.com/plone/stargazers) organization on GitHub.
* Or simply Google for your requirements.

Once you have a shortlist, test these add-ons. Here are the main issues you need to test before you install an add-on on a production site:

* Test all required features. Read but do not trust the documentation
* Check if the add-on runs on your required version
* Check if it is maintained
* Does it have i18n-support, i.e. is the user-interface translated to your language?
* Does it uninstall cleanly?
* Check for unwanted dependencies

Once you found an add-on you like, you can ask the community if you made a good choice or if you missed something:

<!--lint ignore double-link-->
* Message Board: [community.plone.org](https://community.plone.org)

If you can't find something that fits your requirements 100% you can:

* Adapt your requirements to what is available.
* Invest the time & money to customize an existing add-ons to better fit your needs.
* Create a new add-on that does exactly what you need.

## Official resources

_Because Plone also has a lot of good official info resources_

<!--lint ignore double-link-->
* [plone.org](https://plone.org) - Official website for developers and community.
* [community.plone.org](https://community.plone.org) - Official community forum, the best place to get help.
* [Discord chat](https://discord.gg/zFY3EBbjaj) - Discord is the best way to chat with members of the Plone community.
* [Plone support](https://plone.org/support) - Where to find help.
* [docs.plone.org](https://docs.plone.org) - Official documentation for developers/integrators.
* [Plone 6 Documentation](https://6.dev-docs.plone.org) - Official documentation for the upcoming Plone 6 (work on progress).
* [training.plone.org](https://training.plone.org) - Training classes for developers/integrators/users/designers.
* [plone.api](https://6.dev-docs.plone.org/plone.api/index.html) - Documentation for plone.api.


## Contributing

Contributions are welcome! Read the [contribution guidelines](contributing.md).
