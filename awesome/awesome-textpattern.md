# Textpattern

> 来源：[drmonkeyninja/awesome-textpattern](https://github.com/drmonkeyninja/awesome-textpattern)

[![GitHub stars](https://img.shields.io/github/stars/drmonkeyninja/awesome-textpattern?style=flat)](https://github.com/drmonkeyninja/awesome-textpattern/stargazers)

h1. Awesome Textpattern <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome" /></a>

A curated list of amazingly awesome "Textpattern CMS":http://textpattern.com plugins, resources and shiny things.

*This list is for the latest version of Textpattern (v4.7.x).* For Textpattern v4.6.x see the "txp-4.6 branch":https://github.com/drmonkeyninja/awesome-textpattern/tree/txp-4.6.

h2. Contributing

This list is for the community and curated by it, so please contribute. See "CONTRIBUTING":https://github.com/drmonkeyninja/awesome-textpattern/blob/master/CONTRIBUTING.textile for details.

h2. Contents

* "Plugins":#plugins
** "Admin":#admin
** "Comments":#comments
** "Content":#content
** "Embedding":#embedding
** "Forms":#forms
** "Images":#images
** "Navigation":#nav
** "Performance":#performance
** "SEO":#seo
** "Social":#social
** "Miscellaneous":#misc
* "Plugin Development":#development
* "Themes":#themes
** "Back-end":#back-end
** "Front-end":#front-end
* "Resources":#resources
** "Official resources":#resources-official
** "Migration":#migration
** "Web development software integration":#software-integration
* "Community":#community
** "Core team":#core-team
** "Plugins developers":#plugins-dev
** "Blogs":#blogs
* "Related":#related
* "License":#license

h2(#plugins). Plugins

h3(#admin). Admin

* "cbe_frontauth":https://github.com/ClaireBrione/cbe_frontauth - Manage backend connections from frontend and protect content from non-logged in users.
* "hak_tinymce":https://github.com/hakjoon/hak_tinymce - TinyMCE integration for Textpattern.
* "jbx_multiple_image_upload":https://github.com/jbach/jbx_multiple_image_upload - Multiple image upload.
* "rah_privileges":https://github.com/gocom/rah_privileges - Configure Textpattern's admin-side user-group privileges through the Preferences panel.
* "spf_codemirror":https://github.com/spiffin/spf_codemirror - CodeMirror syntax-highlighting and Emmet code-completion for Pages, Forms, Styles, etc.
* "spf_js":https://github.com/spiffin/spf_js - JavaScript management (similar to Presentation → Styles).
* "tom_image_grid":https://github.com/Sacripant/tom_image_grid - Provides a more compact grid interface for the image admin panel.
* "yab_copy_to_new":https://github.com/trenc/yab_copy_to_new - Allows for easy copying of articles from the Write panel.

h3(#comments). Comments

* "arc_admin_comment_preview":https://github.com/drmonkeyninja/arc_admin_comment_preview - Adds a comment preview to admin.
* "jnm_recent_comments_unique":https://github.com/juanjonavarro/jnm_recent_comments_unique - Show latest comments.
* "rah_comments":https://github.com/gocom/rah_comments - Paginated article comments.
* "rah_comment_spam":https://github.com/gocom/rah_comment_spam - Comment anti-spam plugin.

h3(#content). Content

* "glz_custom_fields":https://github.com/gerhard/glz_custom_fields - Unlimited custom fields.
* "smd_tags":https://github.com/Bloke/smd_tags - Unlimited, structured taxonomy across content types.

h3(#embedding). Embedding

* "arc_vimeo":https://github.com/drmonkeyninja/arc_vimeo - Easily embed Vimeo videos.
* "arc_youtube":https://github.com/drmonkeyninja/arc_youtube - Easily embed YouTube videos.
* "oui_embed":https://github.com/NicolasGraph/oui_embed - Embed any information from any web page using "Embed":https://github.com/oscarotero/Embed.
* "oui_instagram":https://github.com/NicolasGraph/oui_instagram - Easily embed Instagram recent images galleries.
* "oui_player":https://github.com/NicolasGraph/oui_player - Easily embed customizable players from a growing providers list.

h3(#forms). Forms

* "zem_contact_reborn":https://github.com/Bloke/zem_contact_reborn - Contact forms.

h3(#images). Images

* "smd_imagery":https://github.com/Bloke/smd_imagery - Article images management.
* "smd_thumbnail":https://github.com/Bloke/smd_thumbnail - Multiple image thumbnails of arbitrary dimensions.

h3(#nav). Navigation

* "adi_menu":http://www.greatoceanmedia.com.au/txp/?plugin=adi_menu - Section hierarchy, section menu and breadcrumb trail.
* "etc_pagination":https://github.com/etc-plugins/etc_pagination - Paginate everything.
* "smd_horizon":https://github.com/Bloke/smd_horizon - Advanced next/previous links.

h3(#performance). Performance

* "aks_cache":http://textpattern.org.ua/plugins/aks_cache - Partially cache parts of a Textpattern template via tags.
* "asy_jpcache":https://github.com/netcarver/asy_jpcache - Full page caching.
* "etc_cache":https://github.com/etc-plugins/etc_cache - Events-driven cache solution for Textpattern CMS.
* "rah_cache":https://github.com/gocom/rah_cache - Cache dynamic pages as flat files.
* "rah_cache_minify":https://github.com/gocom/rah_cache_minify - HTML compressor module for rah_cache plugin.
* "rah_memcached":https://github.com/gocom/rah_memcached - Store parts of Textpattern templates in "Memcached":http://memcached.org.
* "rvm_css":https://vanmelick.com/txp/rvm_css.php?help - Static CSS caching.

h3(#seo). SEO

* "arc_meta":https://github.com/drmonkeyninja/arc_meta - Meta tags to improve site SEO and social marketing.
* "arc_redirect":https://github.com/drmonkeyninja/arc_redirect - URL redirect plugin.
* "rah_sitemap":https://github.com/gocom/rah_sitemap - XML sitemap generator.
* "wcz_utf8_url":https://github.com/wcz-txp/Unicode-url-for-Textpattern - UTF-8 permlinks instead of transliterated ones.

h3(#social). Social

Plugins that add social features to Textpattern.

* "arc_social_share":https://github.com/drmonkeyninja/arc_social_share - Social bookmarking.
* "pat_article_social":https://github.com/cara-tm/pat_article_social - Social bookmarking with share counts.
* "TXP Tweet":https://github.com/drmonkeyninja/TXP-Tweet - Twitter-Textpattern integration.

h3(#misc). Miscellaneous

* "fly_excerpt":https://github.com/brachycera/fly_excerpt - Truncate the article excerpt.
* "oui_cookie":https://github.com/NicolasGraph/oui_cookie - Set, read, reset or delete cookies manually or through URL variables.
* "oui_quote":https://github.com/NicolasGraph/oui_quote - Pull and display a quote from "Quotes on design":http://quotesondesign.com/, "They said so":https://theysaidso.com/, "Le figaro":http://evene.lefigaro.fr/citations or "Le Monde":http://dicocitations.lemonde.fr/citations-mot-monde.php.
* "pat_if_amp":https://github.com/cara-tm/pat_if_amp - Serve Google's Accelerated Mobile Pages (AMP) in Textpattern.
* "pat_eu_cookies_law":https://github.com/cara-tm/pat_eu_cookies_law - EU Cookie Law compliance: A Textpattern CMS plugin for third-party cookies.
* "rah_backup":https://github.com/gocom/rah_backup - Takes backups from Textpattern CMS installations.
* "rah_flat":https://github.com/NicolasGraph/rah_flat - Edit Textpattern's database contents and page templates as flat files.
* "rah_terminal":https://github.com/gocom/rah_terminal - Terminal interface emulator.
* "rvm_maintenance":https://vanmelick.com/txp/rvm_maintenance.php?help - Shows a maintenance page to all visitors who are not logged in on the admin side.
* "smd_if":http://stefdawson.com/sw/plugins/smd_if - A generic 'if condition' tester.
* "textpattern-installer":https://github.com/gocom/textpattern-installer - Textpattern plugin and theme installer for Composer.
* "upm_pending_notify":https://github.com/wcz-txp/upm_pending_notify - Pending article notifications.

h2(#development). Plugin Development

* "ied_plugin_composer":https://github.com/Bloke/ied_plugin_composer - Create, publish and edit plugins.
* "MassPlugCompiler":https://github.com/gocom/MassPlugCompiler - Compiles Textpattern's plugin installer packages from separate source files.
* "Plugin template repo":https://github.com/textpattern/textpattern-plugin-template - A starter package for plugin developers.

h2(#themes). Themes

h3(#back-end). Back-end

* "Hive theme design patterns":http://design-patterns.textpattern.io/docs/ - Core designer guidelines for themes and plugins developers.
* "jQuery UI theme repo":https://github.com/textpattern/textpattern-jquery-ui-theme - The jQuery UI theme used within the Textpattern admin-side.

h3(#front-end). Front-end

* "Default theme repo":https://github.com/textpattern/textpattern-default-theme - The theme that ships as standard with Textpattern CMS.

h2(#resources). Resources

Various resources, such as books, websites and articles, for improving your Textpattern skills and knowledge.

h3(#resources-official). Official resources

* "Official website":https://textpattern.com/ - Download link, features description and information.
* "Textpattern Documentation":https://docs.textpattern.com - The Textpattern user guidelines.

h3(#migration). Migration

* "WP to Txp":https://github.com/NicolasGraph/wp-to-txp - WordPress developer helpful references.

h3(#software-integration). Web development software integration

* "Textpattern for Panic Coda":https://github.com/philwareham/Textpattern-for-Panic-Coda - Handy elements for use with Panic Coda 2 on a Mac.

h2(#community). Community

* "@textpattern on Twitter":https://twitter.com/textpattern
* "Google+":https://plus.google.com/u/0/communities/111366418300163664690
* "Textpattern Forum":https://forum.textpattern.com/

h3(#core-team). Core Team

* Stef Dawson aka "Bloke":https://forum.textpattern.com/profile.php?id=8181 on "GitHub":https://github.com/Bloke.
* Oleg Loukianov aka "etc":https://forum.textpattern.com/profile.php?id=96820 on "Github":https://github.com/bloatware.
* Phil Wareham aka "philwareham":https://forum.textpattern.com/profile.php?id=39206 on "GitHub":https://github.com/philwareham.
* Robert Wetzlmayr aka "wet":https://forum.textpattern.com/profile.php?id=5463 on "GitHub":https://github.com/rwetzlmayr.


h3(#plugins-dev). Plugins developers

Alphabetical order by author prefixes

* adi aka "gomedia":https://forum.textpattern.com/profile.php?id=15145 on "GitHub":https://github.com/gomedia-adi
* arc aka "monkeyninja":https://forum.textpattern.com/profile.php?id=18747 (Andy Carter) on "Github":https://github.com/drmonkeyninja.
* bot aka "redbot":https://forum.textpattern.com/profile.php?id=8379 on "Github":https://github.com/redbotxx.
* cbe aka "CeBe":https://forum.textpattern.com/profile.php?id=76735 (Claire Brione) on "Github":https://github.com/ClaireBrione.
* goe aka "goechsler":https://forum.textpattern.com/profile.php?id=173137 on "Github":https://github.com/goechsler.
* jcr aka jools-r on "Github":https://github.com/jools-r.
* mkp aka "michaelkpate":https://forum.textpattern.com/profile.php?id=109 (Michael K Pate) on "Github":https://github.com/michaelkpate.
* oui aka "NicolasGraph":https://forum.textpattern.com/profile.php?id=15445 (Nicolas Morand) on "Github":https://github.com/NicolasGraph.
* pat aka "Pat64":https://forum.textpattern.com/profile.php?id=7660 (Patrick Lefevre) on "Github":https://github.com/cara-tm.
* rah aka "Gocom":https://forum.textpattern.com/profile.php?id=9632 (Jukka Svahn) on "Github":https://github.com/gocom.
* smd aka "Bloke":https://forum.textpattern.com/profile.php?id=8181 (Stef Dawson) on "Github":https://github.com/Bloke.

h3(#blogs). Blogs

* "Textpattern Tips":http://www.textpattern.tips/ - Tips, tutorials and code examples to help build better Textpattern sites.

h2(#related). Related

* "Awesome PHP":https://github.com/ziadoz/awesome-php - A curated list of amazingly awesome PHP libraries, resources and shiny things.

h2(#license). License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Awesome Textpattern</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://andy-carter.com" property="cc:attributionName" rel="cc:attributionURL">Andy Carter</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
