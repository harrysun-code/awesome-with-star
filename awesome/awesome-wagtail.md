# Wagtail

[![GitHub stars](https://img.shields.io/github/stars/springload/awesome-wagtail?style=flat)](https://github.com/springload/awesome-wagtail/stargazers)

# Awesome Wagtail [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [<img src="https://cdn.jsdelivr.net/gh/wagtail/awesome-wagtail@ac912cc661a7099813f90545adffa6bb3e75216c/logo.svg" width="104" align="right" alt="Wagtail">](https://wagtail.org/)

> A curated list of awesome packages, articles, and other cool resources from the Wagtail community.
> [Wagtail](https://wagtail.org/) is a Python CMS powered by Django, focusing on flexibility and user experience.

_You might also like [Awesome Django](https://github.com/wsvincent/awesome-django) [![GitHub stars](https://img.shields.io/github/stars/wsvincent/awesome-django?style=flat)](https://github.com/wsvincent/awesome-django/stargazers) and [Awesome Python](https://github.com/vinta/awesome-python) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers). :snake:_

## Contents

- [General resources](#general-resources)
- [Apps](#apps)
  - [Blogging/news](#bloggingnews)
  - [Rich text editor extensions](#rich-text-editor-extensions)
  - [Widgets](#widgets)
  - [StreamField](#streamfield)
  - [Static site generation](#static-site-generation)
  - [Settings management](#settings-management)
  - [E-commerce](#e-commerce)
  - [SEO and SMO](#seo-and-smo)
  - [Customer experience](#customer-experience)
  - [Security](#security)
  - [Media](#media)
  - [Translations](#translations)
  - [Forms](#forms)
  - [Testing](#testing)
  - [Modeladmin](#modeladmin)
  - [Content Management](#content-management)
  - [Misc](#misc)
- [Tools](#tools)
  - [Templates & Starter Kits](#templates--starter-kits)
- [Resources](#resources)
  - [Getting started](#getting-started)
  - [Articles](#articles)
  - [Presentations](#presentations)
  - [Podcasts](#podcasts)
  - [Videos](#videos)
  - [Showcases](#showcases)
  - [Package lists](#package-lists)
- [For editors](#for-editors)
- [Community](#community)
- [Open-source sites](#open-source-sites)

## General resources

- [Official site](https://wagtail.org/)
- [GitHub repository](https://github.com/wagtail/wagtail) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail?style=flat)](https://github.com/wagtail/wagtail/stargazers)
- [Project roadmap](https://wagtail.org/roadmap/)

## Apps

### Blogging/news

- [Wagtail CRX (CodeRed Extensions)](https://github.com/coderedcorp/coderedcms) [![GitHub stars](https://img.shields.io/github/stars/coderedcorp/coderedcms?style=flat)](https://github.com/coderedcorp/coderedcms/stargazers) - Wagtail + CodeRed Extensions enabling rapid development of marketing-focused websites.
- [Puput](https://github.com/APSL/puput) [![GitHub stars](https://img.shields.io/github/stars/APSL/puput?style=flat)](https://github.com/APSL/puput/stargazers) - A Django blog app implemented in Wagtail.

### Rich text editor extensions

- [Wagtail EditorJS](https://github.com/Nigel2392/wagtail_editorjs) [![GitHub stars](https://img.shields.io/github/stars/Nigel2392/wagtail_editorjs?style=flat)](https://github.com/Nigel2392/wagtail_editorjs/stargazers) - An [EditorJS](https://editorjs.io/) widget with great support for Wagtail's page, image and document choosers.
- [Wagtail Terms](https://github.com/smark-1/wagtailterms) [![GitHub stars](https://img.shields.io/github/stars/smark-1/wagtailterms?style=flat)](https://github.com/smark-1/wagtailterms/stargazers) - A plugin to add a glossary terms entity to the Draftail editor.
- [wagtailmdx](https://github.com/julinodev/wagtailmdx) [![GitHub stars](https://img.shields.io/github/stars/julinodev/wagtailmdx?style=flat)](https://github.com/julinodev/wagtailmdx/stargazers) - A [MDXEditor](https://github.com/mdx-editor/editor) [![GitHub stars](https://img.shields.io/github/stars/mdx-editor/editor?style=flat)](https://github.com/mdx-editor/editor/stargazers) integration for Wagtail as textfield widget.

### Widgets

- [wagtailgmaps](https://github.com/springload/wagtailgmaps) [![GitHub stars](https://img.shields.io/github/stars/springload/wagtailgmaps?style=flat)](https://github.com/springload/wagtailgmaps/stargazers) - Simple Google Maps address formatter for Wagtail fields.
- [Wagtail-Geo-Widget](https://github.com/Frojd/wagtail-geo-widget) [![GitHub stars](https://img.shields.io/github/stars/Frojd/wagtail-geo-widget?style=flat)](https://github.com/Frojd/wagtail-geo-widget/stargazers) - Google Maps widget for the GeoDjango PointField field in Wagtail.
- [wagtail-markdown](https://github.com/torchbox/wagtail-markdown) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtail-markdown?style=flat)](https://github.com/torchbox/wagtail-markdown/stargazers) - Markdown support for Wagtail.
- [wagtail-autocomplete](https://github.com/wagtail/wagtail-autocomplete) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail-autocomplete?style=flat)](https://github.com/wagtail/wagtail-autocomplete/stargazers) - Autocompleting choosers for `ForeignKey`, `ParentalKey`, and `ManyToMany` fields.
- [wagtail-instance-selector](https://github.com/ixc/wagtail-instance-selector) [![GitHub stars](https://img.shields.io/github/stars/ixc/wagtail-instance-selector?style=flat)](https://github.com/ixc/wagtail-instance-selector/stargazers) - A `ForeignKey` widget to create and select related items. Similar to Django's `raw_id_fields`.
- [wagtail-generic-chooser](https://github.com/wagtail/wagtail-generic-chooser) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail-generic-chooser?style=flat)](https://github.com/wagtail/wagtail-generic-chooser/stargazers) - provides base classes for building chooser popups and form widgets for the Wagtail admin, matching the look and feel of Wagtail's built-in choosers for pages, documents, snippets and images.
- [Wagtail-Color-Panel](https://github.com/marteinn/wagtail-color-panel) [![GitHub stars](https://img.shields.io/github/stars/marteinn/wagtail-color-panel?style=flat)](https://github.com/marteinn/wagtail-color-panel/stargazers) - A package that adds new panels for selecting colors, works both on regular page fields and stream field.
- [Wagtail Ace Editor](https://github.com/Nigel2392/wagtail_ace_editor) [![GitHub stars](https://img.shields.io/github/stars/Nigel2392/wagtail_ace_editor?style=flat)](https://github.com/Nigel2392/wagtail_ace_editor/stargazers) - Ace Editor right in your Wagtail admin.
- [wagtail-html-editor](https://github.com/kkm-horikawa/wagtail-html-editor) [![GitHub stars](https://img.shields.io/github/stars/kkm-horikawa/wagtail-html-editor?style=flat)](https://github.com/kkm-horikawa/wagtail-html-editor/stargazers) - Enhanced HTML editor block for Wagtail CMS with CodeMirror 6, syntax highlighting, Emmet support, and fullscreen mode.

### StreamField

- [wagtail-inventory](https://github.com/cfpb/wagtail-inventory) [![GitHub stars](https://img.shields.io/github/stars/cfpb/wagtail-inventory?style=flat)](https://github.com/cfpb/wagtail-inventory/stargazers) - Search Wagtail pages by the StreamField blocks they contain.
- [Wagtail Code Block](https://github.com/wagtail-nest/wagtailcodeblock) [![GitHub stars](https://img.shields.io/github/stars/wagtail-nest/wagtailcodeblock?style=flat)](https://github.com/wagtail-nest/wagtailcodeblock/stargazers) - StreamField code blocks for the Wagtail CMS with real-time PrismJS Syntax Highlighting.

### Static site generation

- [Wagtail-bakery](https://github.com/wagtail-nest/wagtail-bakery) [![GitHub stars](https://img.shields.io/github/stars/wagtail-nest/wagtail-bakery?style=flat)](https://github.com/wagtail-nest/wagtail-bakery/stargazers) - A set of helpers for baking your Django Wagtail site out as flat files.

### Settings management

- [Wagtail-Flags](https://github.com/cfpb/wagtail-flags) [![GitHub stars](https://img.shields.io/github/stars/cfpb/wagtail-flags?style=flat)](https://github.com/cfpb/wagtail-flags/stargazers) - Feature flags for Wagtail sites.

### E-commerce

- [django-salesman](https://github.com/dinoperovic/django-salesman) [![GitHub stars](https://img.shields.io/github/stars/dinoperovic/django-salesman?style=flat)](https://github.com/dinoperovic/django-salesman/stargazers) - Headless e-commerce framework for Django with Wagtail modeladmin integration.

### SEO and SMO

- [wagtail-meta-preview](https://github.com/Frojd/wagtail-meta-preview) [![GitHub stars](https://img.shields.io/github/stars/Frojd/wagtail-meta-preview?style=flat)](https://github.com/Frojd/wagtail-meta-preview/stargazers) - Wagtail Meta Preview provides panels for previewing Facebook sharing, Twitter sharing and Google search results in the Wagtail admin.
- [Wagtail Yoast](https://github.com/Aleksi44/wagtailyoast) [![GitHub stars](https://img.shields.io/github/stars/Aleksi44/wagtailyoast?style=flat)](https://github.com/Aleksi44/wagtailyoast/stargazers) - A tool to improve readability of your texts with SEO recommendations.
- [Wagtail SEO](https://github.com/coderedcorp/wagtail-seo) [![GitHub stars](https://img.shields.io/github/stars/coderedcorp/wagtail-seo?style=flat)](https://github.com/coderedcorp/wagtail-seo/stargazers) - Search engine and social media optimization for Wagtail.

### Customer experience

- [Wagtail Experiments](https://github.com/torchbox/wagtail-experiments) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtail-experiments?style=flat)](https://github.com/torchbox/wagtail-experiments/stargazers) – A/B testing for Wagtail.
- [Wagtail Personalisation](https://github.com/wagtail-nest/wagtail-personalisation) [![GitHub stars](https://img.shields.io/github/stars/wagtail-nest/wagtail-personalisation?style=flat)](https://github.com/wagtail-nest/wagtail-personalisation/stargazers) - Personalisation module, enabling editors to create customised pages - or parts of pages - based on segments whose rules are configured directly in the admin interface.

### Security

- [wagtail-2fa](https://github.com/labd/wagtail-2fa) [![GitHub stars](https://img.shields.io/github/stars/labd/wagtail-2fa?style=flat)](https://github.com/labd/wagtail-2fa/stargazers) - Add two-factor authentication to Wagtail by integrating it with django-otp.

### Media

- [wagtailmedia](https://github.com/torchbox/wagtailmedia) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtailmedia?style=flat)](https://github.com/torchbox/wagtailmedia/stargazers) - A Wagtail module for managing video and audio files within the admin.
- [Wagtail Transcription](https://github.com/j-bodek/wagtail-transcription) [![GitHub stars](https://img.shields.io/github/stars/j-bodek/wagtail-transcription?style=flat)](https://github.com/j-bodek/wagtail-transcription/stargazers) - Provides a field to automatically creates transcriptions from YouTube videos.

### Translations

- [Wagtail Localize](https://github.com/wagtail/wagtail-localize) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail-localize?style=flat)](https://github.com/wagtail/wagtail-localize/stargazers) - Translation plugin for Wagtail CMS.
- [Wagtail Modeltranslation](https://github.com/infoportugal/wagtail-modeltranslation) [![GitHub stars](https://img.shields.io/github/stars/infoportugal/wagtail-modeltranslation?style=flat)](https://github.com/infoportugal/wagtail-modeltranslation/stargazers) - Simple app containing a mixin model that integrates [django-modeltranslation](https://github.com/deschler/django-modeltranslation) [![GitHub stars](https://img.shields.io/github/stars/deschler/django-modeltranslation?style=flat)](https://github.com/deschler/django-modeltranslation/stargazers) into Wagtail panels system.

### Forms

- [Wagtail's built in Form Builder](https://docs.wagtail.org/en/stable/reference/contrib/forms/) for general use cases.
- [Wagtail ReCaptcha](https://github.com/wagtail-nest/wagtail-django-recaptcha) [![GitHub stars](https://img.shields.io/github/stars/wagtail-nest/wagtail-django-recaptcha?style=flat)](https://github.com/wagtail-nest/wagtail-django-recaptcha/stargazers) - wagtail-django-captcha provides an easy way to integrate the [django-recaptcha](https://github.com/django-recaptcha/django-recaptcha) [![GitHub stars](https://img.shields.io/github/stars/django-recaptcha/django-recaptcha?style=flat)](https://github.com/django-recaptcha/django-recaptcha/stargazers) field when using the Wagtail formbuilder.
- [Wagtail Jotform](https://github.com/torchbox/wagtail-jotform) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtail-jotform?style=flat)](https://github.com/torchbox/wagtail-jotform/stargazers) - A plugin for using jotforms in wagtail.
- [Wagtail Model Forms](https://github.com/vicktornl/wagtail-model-forms) [![GitHub stars](https://img.shields.io/github/stars/vicktornl/wagtail-model-forms?style=flat)](https://github.com/vicktornl/wagtail-model-forms/stargazers) - The Wagtail Form Builder functionalities available for your models/snippets.
- [Wagtail Formation](https://github.com/mwesterhof/wagtail_formation) [![GitHub stars](https://img.shields.io/github/stars/mwesterhof/wagtail_formation?style=flat)](https://github.com/mwesterhof/wagtail_formation/stargazers) - Fully dynamic and easy to use CMS-able forms for wagtail

### Testing

- [wagtail-linkchecker](https://github.com/neon-jungle/wagtail-linkchecker) [![GitHub stars](https://img.shields.io/github/stars/neon-jungle/wagtail-linkchecker?style=flat)](https://github.com/neon-jungle/wagtail-linkchecker/stargazers) - A tool to assist with finding broken links on your Wagtail site.
- [Wagtail Accessibility](https://github.com/wagtail-nest/wagtail-accessibility) [![GitHub stars](https://img.shields.io/github/stars/wagtail-nest/wagtail-accessibility?style=flat)](https://github.com/wagtail-nest/wagtail-accessibility/stargazers) – ✅ Accessibility content checks for Wagtail websites.
- [Wagtail Factories](https://github.com/wagtail/wagtail-factories) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail-factories?style=flat)](https://github.com/wagtail/wagtail-factories/stargazers) - Factory boy classes for Wagtail.

### Modeladmin

- [wagtail-admin-list-controls](https://github.com/ixc/wagtail-admin-list-controls) [![GitHub stars](https://img.shields.io/github/stars/ixc/wagtail-admin-list-controls?style=flat)](https://github.com/ixc/wagtail-admin-list-controls/stargazers) - Adds advanced search, ordering and layout controls to Wagtail's modeladmin list views.
- [Wagtail Rangefilter](https://github.com/wunderweiss/wagtail-rangefilter) [![GitHub stars](https://img.shields.io/github/stars/wunderweiss/wagtail-rangefilter?style=flat)](https://github.com/wunderweiss/wagtail-rangefilter/stargazers) - Integrates django-admin-rangefilter into Wagtail's ModelAdmin.
- [Wagtail-TreeModelAdmin](https://github.com/cfpb/wagtail-treemodeladmin) [![GitHub stars](https://img.shields.io/github/stars/cfpb/wagtail-treemodeladmin?style=flat)](https://github.com/cfpb/wagtail-treemodeladmin/stargazers) - An extension for Wagtail's ModelAdmin for a page explorer-like navigation of Django model relationships.

### Content Management

- [Wagtail Sharing](https://github.com/cfpb/wagtail-sharing) [![GitHub stars](https://img.shields.io/github/stars/cfpb/wagtail-sharing?style=flat)](https://github.com/cfpb/wagtail-sharing/stargazers) – Easier sharing of Wagtail drafts.
- [Wagtail Transfer](https://github.com/wagtail/wagtail-transfer) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail-transfer?style=flat)](https://github.com/wagtail/wagtail-transfer/stargazers) - An official extension for Wagtail allowing content to be transferred between multiple instances of a Wagtail project
- [Wagtail Content Import](https://github.com/torchbox/wagtail-content-import) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtail-content-import?style=flat)](https://github.com/torchbox/wagtail-content-import/stargazers) - Import content from Google Docs or Docx into StreamFields, using a customisable mapping system.
- [Wagtail Headless Preview](https://github.com/torchbox/wagtail-headless-preview) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtail-headless-preview?style=flat)](https://github.com/torchbox/wagtail-headless-preview/stargazers) - Previews for headless Wagtail setups
- [Wagtail-FEdit](https://github.com/Nigel2392/wagtail_fedit) [![GitHub stars](https://img.shields.io/github/stars/Nigel2392/wagtail_fedit?style=flat)](https://github.com/Nigel2392/wagtail_fedit/stargazers) - Add frontend editing to your Wagtail site.

### Misc

- [wagtailmenus](https://github.com/jazzband/wagtailmenus) [![GitHub stars](https://img.shields.io/github/stars/jazzband/wagtailmenus?style=flat)](https://github.com/jazzband/wagtailmenus/stargazers) - An app to help you manage and render menus in your Wagtail projects more effectively.
- [Wagtail Gridder](https://github.com/wharton/wagtailgridder) [![GitHub stars](https://img.shields.io/github/stars/wharton/wagtailgridder?style=flat)](https://github.com/wharton/wagtailgridder/stargazers) - Grid card layout similar to Google image search results, with an expanded area for card details.
- [Wagtail App Pages](https://github.com/mwesterhof/wagtail_app_pages) [![GitHub stars](https://img.shields.io/github/stars/mwesterhof/wagtail_app_pages?style=flat)](https://github.com/mwesterhof/wagtail_app_pages/stargazers) - Extend Wagtail pages using an actual URL config and django views.
- [Wagtail Cache](https://github.com/coderedcorp/wagtail-cache) [![GitHub stars](https://img.shields.io/github/stars/coderedcorp/wagtail-cache?style=flat)](https://github.com/coderedcorp/wagtail-cache/stargazers) - A simple page cache for Wagtail using the Django cache middleware.
- [Wagtail Orderable](https://github.com/elton2048/wagtail-orderable) [![GitHub stars](https://img.shields.io/github/stars/elton2048/wagtail-orderable?style=flat)](https://github.com/elton2048/wagtail-orderable/stargazers) - Mixin support for drag-and-drop ordering in admin panel.
- [Wagtail Resume](https://github.com/adinhodovic/wagtail-resume) [![GitHub stars](https://img.shields.io/github/stars/adinhodovic/wagtail-resume?style=flat)](https://github.com/adinhodovic/wagtail-resume/stargazers) – A Wagtail project made to simplify creation of resumes for developers.
- [Wagtail Trash](https://github.com/Frojd/wagtail-trash) [![GitHub stars](https://img.shields.io/github/stars/Frojd/wagtail-trash?style=flat)](https://github.com/Frojd/wagtail-trash/stargazers) - Instead of deleting pages when pressing delete, pages will get thrown into the "Trash Can".
- [wagtail-pdf-view](https://github.com/donhauser/wagtail-pdf) [![GitHub stars](https://img.shields.io/github/stars/donhauser/wagtail-pdf?style=flat)](https://github.com/donhauser/wagtail-pdf/stargazers) - PDF rendering views for the Wagtail CMS.
- [Wagtail Grapple](https://github.com/torchbox/wagtail-grapple) [![GitHub stars](https://img.shields.io/github/stars/torchbox/wagtail-grapple?style=flat)](https://github.com/torchbox/wagtail-grapple/stargazers) - A Wagtail app that makes building GraphQL endpoints a breeze.
- [Wagtail Cache Invalidator](https://github.com/vicktornl/wagtail-cache-invalidator) [![GitHub stars](https://img.shields.io/github/stars/vicktornl/wagtail-cache-invalidator?style=flat)](https://github.com/vicktornl/wagtail-cache-invalidator/stargazers) - Invalidate and purge (frontend) cache via an user-friendly interface in the Wagtail CMS.

## Tools

### Templates & Starter Kits

- [Pipit](https://github.com/Frojd/Wagtail-Pipit) [![GitHub stars](https://img.shields.io/github/stars/Frojd/Wagtail-Pipit?style=flat)](https://github.com/Frojd/Wagtail-Pipit/stargazers) – Pipit is a Wagtail CMS boilerplate which aims to provide an easy and modern developer workflow with a React-rendered frontend.
- [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) [![GitHub stars](https://img.shields.io/github/stars/wagtail/cookiecutter-wagtail-package?style=flat)](https://github.com/wagtail/cookiecutter-wagtail-package/stargazers) - A cookiecutter template for building Wagtail add-on packages.
- [Wagtail for Platform.sh](https://github.com/platformsh-templates/wagtail) [![GitHub stars](https://img.shields.io/github/stars/platformsh-templates/wagtail?style=flat)](https://github.com/platformsh-templates/wagtail/stargazers) - Wagtail template for Platform.sh.
- [cookiecutter-wagtail-vix](https://github.com/engineervix/cookiecutter-wagtail-vix) [![GitHub stars](https://img.shields.io/github/stars/engineervix/cookiecutter-wagtail-vix?style=flat)](https://github.com/engineervix/cookiecutter-wagtail-vix/stargazers) - a minimal, batteries-included, reusable project skeleton to serve as a starting point for a Wagtail project.
- [Sites Conformes](https://github.com/numerique-gouv/sites-conformes) [![GitHub stars](https://img.shields.io/github/stars/numerique-gouv/sites-conformes?style=flat)](https://github.com/numerique-gouv/sites-conformes/stargazers) - Gestionnaire de contenu permettant de créer et gérer un site internet basé sur le Système de design de l'État, accessible et sécurisé. Basé sur Wagtail CMS.

### Templates (start command)

- [Wagtail template: Your first Wagtail site](https://github.com/thibaudcolas/wagtail-tutorial-template) [![GitHub stars](https://img.shields.io/github/stars/thibaudcolas/wagtail-tutorial-template?style=flat)](https://github.com/thibaudcolas/wagtail-tutorial-template/stargazers) - A Wagtail project starter template – with the solution to Wagtail's official Your first Wagtail site tutorial.
- [Wagtail News Template](https://github.com/wagtail/news-template) [![GitHub stars](https://img.shields.io/github/stars/wagtail/news-template?style=flat)](https://github.com/wagtail/news-template/stargazers) - A Wagtail template for a news site.

## Resources

### Getting started

- [Getting started in Wagtail, a newcomer's perspective](https://wagtail.org/blog/getting-started-wagtail-newcomers-perspective/) - Having used Drupal almost exclusively as my main tool of choice for a while now, I was asked to put together a build using Wagtail.
- [Présentation de Wagtail, le dernier CMS Django](https://makina-corpus.com/django/presentation-de-wagtail-le-dernier-cms-django) - Wagtail est un CMS relativement récent dans l’écosystème Django. Pour autant, son jeune âge ne l’empêche pas de posséder de nombreuses fonctionnalités que nous découvrirons dans cet article.
- [Getting Started With Wagtail](https://vix.digital/insights/getting-started-wagtail/) - Working extensively with Wagtail and the surrounding community, we have discovered a range of common pitfalls developers run into when beginning to deliver with Wagtail.

### Articles

- [Wagtail Tutorials: Build Blog Step by Step](https://saashammer.com/blog/wagtail-tutorials/) - The tutorials teach you how to create a standard blog from scratch step by step.
- [Multi-tenancy with Wagtail](https://cynthiakiser.com/blog/2023/11/01/multitenancy-with-wagtail.html) - Multiple part guide on robust multi-tenancy support in Wagtail.
- [How to Prevent Users from Creating Pages by Type](https://timonweb.com/wagtail/how-to-prevent-users-from-creating-certain-page-types-in-wagtail-cms/)
- [How to Create and Manage Menus of Wagtail application](https://saashammer.com/blog/how-to-create-and-manage-menus-in-wagtail/)

### Presentations

- [An Introduction to Wagtail](https://www.youtube.com/watch?v=glIIF-kBXf0) by Eloise "Ducky" Macdonald-Meyer - This talk is an introduction to Wagtail, a content management system built on the Python web framework, Django.
- [DjangoCon US 2015 - Wagtail - Yet Another Django CMS](https://www.youtube.com/watch?v=6j0NVq6g4FE) by Tom Dyson - Tom will explain why his agency decided to build a new CMS, share some lessons learned in running a growing open source project, and outline Wagtail's roadmap to version 2 and beyond. [Slide deck](https://speakerdeck.com/tomdyson/wagtail-yet-another-cms-djangocon-us-2015).
- [Wellington Wagtail CMS Meetup - Meet Wagtail](https://docs.google.com/presentation/d/19EGWFtfHovHSAvyHCnLbxK50IAR2o7WwKd709cqi9p4/edit) by Josh, Jordi and Rich, from the Springload dev team - An introductory session to Wagtail to showcase the main features it has to offer.
- [DjangoCon US 2016 - Atomic Wagtail](https://www.youtube.com/watch?v=kqAKiouk1lY) by Kurt Wall – Brad Frost's atomic design principles are taking the way we design the web by storm. I'll explain what Wagtail is, how you can use it with atomic design principles, and some hurdles you might run into along the way with suggestions on how to help.
- [PyCon Australia – Comparing Wagtail, Django CMS and Mezzanine](https://www.youtube.com/watch?v=3UC1MNFOjEI) by Adam Brenecki – This talk explores the different approaches, strengths and weaknesses of each CMS, and what they mean for you as a developer and for your content editors.
- [Wagtail — еще одна CMS на Django](https://www.youtube.com/watch?v=yRmZ6WUfoOc) by Mikalai Radchuk - This talk is an introduction to Wagtail in Russian.
- [Wagtail & Agile – Wagtail Space 2017](https://www.youtube.com/watch?t=2m21s&v=-Qii_AyQsxE) by Edd Baldry.
- [Deploy Wagtail to the Divio Cloud – Wagtail Space 2017](https://www.youtube.com/watch?t=38m13s&v=-Qii_AyQsxE) by Daniele Procida.
- [All about Wagtail – Wagtail Space 2017](https://www.youtube.com/watch?v=OedQi5W3Zho) by Robin van der Rijst.
- [Presenting Wagtail Clear StreamField, a modular StreamField app – Wagtail Space 2017](https://www.youtube.com/watch?t=19m1s&v=OedQi5W3Zho) by Edd Baldry.
- [Wagtail Experiments, easy A/B testing for your Wagtail sites – Wagtail Space 2017](https://www.youtube.com/watch?t=34m37s&v=OedQi5W3Zho) by Tom Dyson.
- [Wagtail's preview, a new hope – Wagtail Space 2017](https://www.youtube.com/watch?v=ObM2pUgY-bs) by Bertrand Bordage.
- [The Zen of Wagtail – Wagtail Space 2017](https://www.youtube.com/watch?t=16m38s&v=ObM2pUgY-bs) by Matt Westcott.
- [Plone to Wagtail – Wagtail Space 2017](https://www.youtube.com/watch?t=2m57s&v=hZcuq8WJVew) by Coen van der Kamp.
- [Hundreds of Wagtail in Flight – Wagtail Space 2017](https://www.youtube.com/watch?t=24m9s&v=hZcuq8WJVew) by Simon de Haan.
- [How Google uses Wagtail – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=1937s) by Kevin Chung.
- [Introducing Draft.js in Wagtail – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=2690s) by Thibaud Colas. [Presentation](https://thib.me/introducing-draft-js-in-wagtail).
- [Let It Go – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=3938s) by Matt Wescott.
- [Developing Solutions for Girls, by Men – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=5184s) by Lisa Adams.
- [Wagtail’s first hatch – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=265s) by Bertrand Bordage.
- [The Word Problem – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=2841s) by Tom Dyson.
- [Wagtail on Divio Cloud – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=3856s) by Daniele Procida.
- [Chopping the head off Wagtail and sticking it back on – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=152s) by Tony Yates.
- [StreamField editor at UWKM – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=400s) by Geert jan Hoogeslag.
- [Things i learned at Wagtail Space – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=719s) by Codie Roelf.
- [Fly Wagtail to a PyCon – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=912s) by Daniele Procida.
- [Wagtail Performance – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=1345s) by Michael van Tellingen. [Code](https://gist.github.com/mvantellingen/daebda6abbaa9a5ed0888f886a77fcf0).
- [Mutliple images uploader – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=1661s) by Rajeev J Sebastian.
- [Wagtail Space easter egg team demo – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=2057s) by Lars. [Code](https://github.com/specialunderwear/haunted-wagtail) [![GitHub stars](https://img.shields.io/github/stars/specialunderwear/haunted-wagtail?style=flat)](https://github.com/specialunderwear/haunted-wagtail/stargazers).
- [Wagtail Space 2019 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=2278s) by Maarten Kling.
- [Wagtail in 2018 – Wagtail Space US 2018](https://www.youtube.com/watch?v=ICKYMO0YoFI&index=2&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Tom Dyson.
- [What the Wagtail Docs Don't Tell You – Wagtail Space US 2018](https://www.youtube.com/watch?v=PCkxBNXWM64&index=3&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Lacey Williams Henschel.
- [Django Logging for Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=kkztl9ORUKQ&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=4) by Ryan Sullivan.
- [Scaling Wagtail for 100 Million Girls – Wagtail Space US 2018](https://www.youtube.com/watch?v=AiOJAKE0M0I&index=5&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Lisa Adams and Codie Roelf.
- [Using Wagtail to Fight for Press Freedom – Wagtail Space US 2018](https://www.youtube.com/watch?v=FYqbqsa04T8&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=6) by Harris Lapiroff.
- [Choosing Wagtail for Columbia University – Wagtail Space US 2018](https://www.youtube.com/watch?v=OiZScRcluCo&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=7) by Zarina Mustapha.
- [Running a Multi-Site Newsroom in Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=lMCjInjAz-M&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=8) by Ryan Verner.
- [Wagtail in the Cloud – Wagtail Space US 2018](https://www.youtube.com/watch?v=N1MeTEPRmJA&index=9&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Daniele Procida.
- [Beheading Wagtail: Wagtail as a Headless CMS – Wagtail Space US 2018](https://www.youtube.com/watch?v=HZT14u6WwdY&index=10&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Michael Harrison.
- [Learning Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=C-tXt5fLj_s&index=11&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Dawn Wages.
- [Sharing is Caring – Wagtail Space US 2018](https://www.youtube.com/watch?v=6AXyg6vvMTE&index=12&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Andy Chosak.
- [Lightning Talks – Wagtail Space US 2018](https://www.youtube.com/watch?v=uoxyBIpaXTU&index=13&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)
- [Wagtail: когда хочется чего-то приятнее, чем просто Django – Moscow Python Conf++ 2018](https://www.youtube.com/watch?v=xPPfTvLS7oQ) by Игорь Мосягин
- [The State of Wagtail – Wagtail Space 2019](https://www.youtube.com/watch?t=592&v=MAzZ2lhMhzM) by Tom Dyson.
- [Image rotation feature – Wagtail Space 2019](https://www.youtube.com/watch?t=2057&v=MAzZ2lhMhzM) by Chris Adams. Code.
- [Debug templates – Wagtail Space 2019](https://www.youtube.com/watch?t=2264&v=MAzZ2lhMhzM) by Coen van der Kamp.
- [Wagtail Headless with HATEOAS – Wagtail Space 2019](https://www.youtube.com/watch?t=2567&v=MAzZ2lhMhzM) by Duco Dokter.
- [Building a Planet Friendly Web (with Wagtail) – Wagtail Space 2019](https://www.youtube.com/watch?t=2926&v=MAzZ2lhMhzM) by Chris Adams.
- [\[WIP\] The future of (rich text) authoring experiences in Wagtail – Wagtail Space 2019](https://www.youtube.com/watch?t=4067&v=MAzZ2lhMhzM) by Thibaud Colas.
- [Wagtail & Whatsapp – Wagtail Space 2019](https://www.youtube.com/watch?t=47&v=CSwpj-jyjP4) by Lisa Adams & Codie Roelf.
- [Slack2Wagtail – Wagtail Space 2019](https://www.youtube.com/watch?t=785&v=CSwpj-jyjP4) by Coen van der Kamp & Lucas Moeskops.
- [Wagtail and Oscar – Wagtail Space 2019](https://www.youtube.com/watch?t=1634&v=CSwpj-jyjP4) by Lars van de Kerkhof.
- [wagtail-textract – Wagtail Space 2019](https://www.youtube.com/watch?t=3313&v=CSwpj-jyjP4) by Kees Hink. [Code](https://github.com/fourdigits/wagtail_textract) [![GitHub stars](https://img.shields.io/github/stars/fourdigits/wagtail_textract?style=flat)](https://github.com/fourdigits/wagtail_textract/stargazers).
- [Django 2.2 compatibility – Wagtail Space 2019](https://www.youtube.com/watch?t=3468&v=CSwpj-jyjP4) by Matt Wescott.
- [SEO dashboard – Wagtail Space 2019](https://www.youtube.com/watch?t=3937&v=CSwpj-jyjP4) by Janneke Janssen. [Code](https://github.com/LUKKIEN/wagtail-marketing-addons) [![GitHub stars](https://img.shields.io/github/stars/LUKKIEN/wagtail-marketing-addons?style=flat)](https://github.com/LUKKIEN/wagtail-marketing-addons/stargazers).
- [My First Wagtail Contribution – More formats in RichText Editor – Wagtail Space 2019](https://www.youtube.com/watch?t=4126&v=CSwpj-jyjP4) by Arifin Ibne Matin.
- [Fly, Wagtail, fly! – Wagtail Space 2019](https://www.youtube.com/watch?t=4404&v=CSwpj-jyjP4) by Daniele Procida.
- [Wagtail & GraphQL – Wagtail Space 2019](https://www.youtube.com/watch?t=24&v=YydSbL8gMS4) by Arthur Bayr.
- [Writing (code) for authors – Wagtail Space US 2019](https://www.youtube.com/watch?v=Ihsrki0d1G8&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=1) by Brian Smith & Eric Sherman. [Slides](https://docs.google.com/presentation/d/1z61u0uKwJxmYS4Zawbu4Zgg-kCtInd1VgsEg-rnwzBE/edit).
- [Saving Lives With Wagtail: Recovery Meetings Across the World – Wagtail Space US 2019](https://www.youtube.com/watch?v=QlLWvNT5Wrk&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=2) by Timothy Allen.
- [Why we chose Wagtail for CodeRed CMS – Wagtail Space US 2019](https://www.youtube.com/watch?v=1JUOAAmLQFA&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=3) by Vince Salvino.
- [Building a Wagtail-based site and authoring environment with accessibility in mind – Wagtail Space US 2019](https://www.youtube.com/watch?v=CxjlAI6R7iY&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=4) by Zarina Mustapha.
- [Making Wagtail Accessible – Wagtail Space US 2019](https://www.youtube.com/watch?v=tdB1I_gSCeY&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=5) by Thibaud Colas. [Slides](https://docs.google.com/presentation/d/15y8XIe7SL-RYEO9tEE8n9chx80_X4j4PbczGGM-cEGE/edit).
- [Everyone can fly a flag – Wagtail Space US 2019](https://www.youtube.com/watch?v=ZqwmgsqMTEs&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=6) by Will Barton. [Slides](https://docs.google.com/presentation/d/1-A1doke2ylcqG72oIP-MLiX8SKXKkKNxQeKxddYUGBw/edit).
- [Architecting for a multi-domain site – Wagtail Space US 2019](https://www.youtube.com/watch?v=xMbJmHF7kCw&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=7) by Ben Beecher. [Slides](https://slides.com/benbeecher/mds/).
- [Contributions can be more than code – Wagtail Space US 2019](https://www.youtube.com/watch?v=tK-3kEBbblg&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=8) by Kalob Taulien.
- [Thoughtful Code Review – Wagtail Space US 2019](https://www.youtube.com/watch?v=RY0K1BEV-_U&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=9) by Naomi Morduch Toubman. [Slides](https://docs.google.com/presentation/d/1b_Hda8381G6mMc7uzYDc2EYjocfwSi2TYiRMI7d4e3I/edit).
- [Solving your problems by spelunking the Wagtail code – Wagtail Space US 2019](https://www.youtube.com/watch?v=BMoOhjgirFM&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=10) by Harris Lapiroff. [Slides](https://harrislapiroff.github.io/wagtail-space-us-2019/)
- [The State of Wagtail: 2019 – Wagtail Space US 2019](https://www.youtube.com/watch?v=s29vaGnFcq8&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=11) by Tom Dyson.
- [Wagtail Guide - Getting started - Wagtail Space US 2022](https://www.youtube.com/watch?v=E3-kFY6jPPY) by Coen van der Kamp.
- [A New Approach to Multitenant Wagtail - Wagtail Space US 2022](https://www.youtube.com/watch?v=WN0L4YNrWes) by Stephanie C. Smith and Addison Hardy.
- [The Wagtail Marketplace for Games-based Courses - Wagtail Space 2022](https://www.youtube.com/watch?v=ueou6CxiR3Y) by Sarah Toms.
- [The Wagtail Ecosystem - Wagtail Space US 2022](https://www.youtube.com/watch?v=4Qd43nsxmoc) by Vince Salvino.
- [Wagtail charts and graphs - Wagtail Space US 2022](https://www.youtube.com/watch?v=QK-Vhlpos3Q) by Sævar Öfjörð Magnússon & Arnar Tumi Þorsteinsson.
- [Wagtail as a headless CMS for JavaScript frontends - Wagtail Space US 2022](https://www.youtube.com/watch?v=bYRQ492BED0) by Tommaso Amici.
- [Adding a GraphQL API to Wagtail - Wagtail Space US 2022](https://www.youtube.com/watch?v=_O5isU354vg) by Patrick Arminio.
- [Bringing JSONField into Wagtail Core - Wagtail Space US 2022](https://www.youtube.com/watch?v=XtazMDNdlK8) by Sage Abdullah.
- [Wagtail vs. WordPress - Wagtail Space US 2022](https://www.youtube.com/watch?v=Vl2g7H3aodw) by Kalob Taulien.
- [Designing the new page editor - Wagtail Space US 2022](https://www.youtube.com/watch?v=t2xiPJ91UCE) by Phil Dexter and Ben Enright.
- [5 Things I Learned About Wagtail the Hard Way - Wagtail Space US 2022](https://www.youtube.com/watch?v=LNqVzLkZkig) by Meagen Voss.
- [Tips for Maintaining Wagtail Packages - Wagtail Space US 2022](https://www.youtube.com/watch?v=Zh608nVBrEw) by Tim Allen.
- [Wagtail Guide - Wagtail Space US 2022](https://www.youtube.com/watch?v=W0tL-5V5BWA) by Coen van der Kamp.
- [The state of Wagtail 2022 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=4D49RENHfoM) by Tom Dyson.
- [Choosers - Wagtail Space NL 2022](https://www.youtube.com/watch?v=nSjVAISLr4M) by Matthew Westcott.
- [Working with Image Filters - Wagtail Space NL 2022](https://www.youtube.com/watch?v=gCGT51BcTdM) by Arnar Tumi Þorsteinsson.
- [Things I learned - Wagtail Space NL 2022](https://www.youtube.com/watch?v=xG5-s48TZt8) by Dan Braghis.
- [Wagtail Roadrunner Beep Beep - Wagtail Space NL 2022](https://www.youtube.com/watch?v=ynlFUcutSWQ) by Lars van de Kerkhof.
- [Dockerising wagtail projects in 5 minutes - Wagtail Space NL 2022](https://www.youtube.com/watch?v=PgkpBMoN4UY) by Sævar Öfjörð Magnússon.
- [Wagtail in the News Room - Wagtail Space NL 2022](https://www.youtube.com/watch?v=B85HwmX5uaw) by Sævar Öfjörð Magnússon & Arnar Tumi Þorsteinsson.
- [Digital Nomad - Wagtail Space NL 2022](https://www.youtube.com/watch?v=9Evrwzpg-dw) by Maikel Martens.
- [Unobtrusive internationalisation - Wagtail Space NL 2022](https://www.youtube.com/watch?v=_dhScxTdtjA) by Lars van de Kerkhof.
- [Moving Wagtail pages - Wagtail Space NL 2022](https://www.youtube.com/watch?v=OFqPKffSVWI) by Viggo de Vries.
- [Wagtail architecture options, or should I go headless - Wagtail Space NL 2022](https://www.youtube.com/watch?v=JMULuz6RzjQ) by Dan Braghis.
- [Wagtail headless and NextJS frontend - Wagtail Space NL 2022](https://www.youtube.com/watch?v=s8cJhFtjqZA) by Lucas Moeskops.
- [State of Wagtail - Wagtail Space US 2024](https://www.youtube.com/watch?v=TKLYeKpFbno&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) by Tom Dyson.
- [Pleasant Publishing Patterns - Wagtail Space US 2024](https://www.youtube.com/watch?v=ZXGcqY-OeYk&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) by Michael Trythall.
- [Accessibility for Complex Components and Interfaces - Wagtail Space US 2024](https://www.youtube.com/watch?v=AC1gy9R2Z6c&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) by Kara Gaulrapp.
- [One Thousand and One Wagtail Sites - Wagtail Space US 2024](https://www.youtube.com/watch?v=yciVqzSGWTw&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) by Vince Salvino.
- [3D Files with Wagtail - Wagtail Space US 2024](https://www.youtube.com/watch?v=ccBrb50xRCM&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) by Dawn Wages and Mira Gibson.
- [Wagtail, Reactivated - Headless Without the Headache - Wagtail Space US 2024](https://www.youtube.com/watch?v=mQsI8Ji3_LY&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) by Josh Marantz.
- [Lightning Talks June 20 - Wagtail Space US 2024](https://www.youtube.com/watch?v=UuE3Y15To8Q&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) - lightning talks.
- [LLMs and Wagtail - Wagtail Space US 2024](https://www.youtube.com/watch?v=b-luIDn80bc&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) by Emily Topp-Mugglestone.
- [PudlStack - Building Wagtail Affinity Group Communities That Offer Bot Helpers - Wagtail Space US 2024](https://www.youtube.com/watch?v=SNEeo_ABQ7g&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) by Anthony Garcia.
- [Auditing Wagtail Content - Wagtail Space US 2024](https://www.youtube.com/watch?v=a1O3hKib8Ns&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB&index=2&pp=i) by Will Barton & Chuck Sebian-Lander.
- [What Editors Really Want - Wagtail Space US 2024](https://www.youtube.com/watch?v=1qF5wC4rCY4&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) by Meagen Voss.
- [Improving the Editor Experience through Validation - Wagtail Space US 2024](https://www.youtube.com/watch?v=UVBHciwpgKM&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) by Scott Cranfill.
- [sditail: Extending Wagtail CMS as a Spatial Data Infrastructure - Wagtail Space US 2024](https://www.youtube.com/watch?v=XxdJpYNT4EM&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) by César Benjamin.
- [Packages! Packages! Packages! - Wagtail Space US 2024](https://www.youtube.com/watch?v=r5ovJPWvxL4&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) - panel.
- [Lightning Talks June 21 - Wagtail Space US 2024](https://www.youtube.com/watch?v=vazMp9jTlEU&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) - lightning talks.
- [The State of Wagtail - Wagtail Space NL 2024](https://www.youtube.com/watch?v=P9Ftbu5NVUI&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=1) by Tom Dyson.
- [Headless Wagtail Strategies - Wagtail Space NL 2024](https://www.youtube.com/watch?v=nweVHX5DgWU&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=2) by Rémy Sanchez.
- [Wagging HubSpot's Tail - Wagtail Space NL 2024](https://www.youtube.com/watch?v=VUoOoRxlWrU&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=3) by Simon Blanchard and Joost Meijerink.
- [Wagtail and Caching - Wagtail Space NL 2024](https://www.youtube.com/watch?v=vBdG2GfAZAo&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=4) by Jake Howard.
- [Faster Thumbnails for a Faster Web - Wagtail Space NL 2024](https://www.youtube.com/watch?v=0kHhGBxwzeM&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=5) by Alex Tomkins.
- [The impossible art of making everyone happy - Wagtail Space NL 2024](https://www.youtube.com/watch?v=v3KEaMTfKg0&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=6) by Matthew Westcott.
- [Bringing modern authentication to Wagtail: WebAuthn and Passkeys - Wagtail Space NL 2024](https://www.youtube.com/watch?v=qJwg2kFtFW4&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=7) by Storm Heg.
- [How to abuse Wagtail's StreamFields as much as you want - Wagtail Space NL 2024](https://www.youtube.com/watch?v=tOBGJ0riDRw&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=8) by Rémy Sanchez.
- [Wagtail AI and Wagtail Vector Index - Wagtail Space NL 2024](https://www.youtube.com/watch?v=jHuhX_SNF1s&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=9) by Dan Braghiș.
- [Wagtail Translate - Wagtail Space NL 2024](https://www.youtube.com/watch?v=QxnC70Bwj0k&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=10) by Coen van der Kamp.
- [You've been caching your content website wrong - Wagtail Space NL 2024](https://www.youtube.com/watch?v=bWF06aCjbUM&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=11) by Rémy Sanchez.
- [Universal Listings - Wagtail Space NL 2024](https://www.youtube.com/watch?v=aNto27_lfJ4&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=12) by Sage Abdullah.
- [Recovering deleted Django models - Wagtail Space NL 2024](https://www.youtube.com/watch?v=TB64DtQZeB0&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=13) by Jake Howard.
- [Wagtail Dashboards - Wagtail Space NL 2024](https://www.youtube.com/watch?v=0msxKe0RoNw&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=14) by Judith van Leersum and Emmelien Schiet.
- [Multi-lingual websites in Wagtail - Wagtail Space NL 2024](https://www.youtube.com/watch?v=5rPvOsVeRhA&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=15) by Paul Stevens.
- [State of Wagtail 2025 - Wagtail Space 2025](https://www.youtube.com/watch?v=9Kduqs6NH7Q&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=2) by Thibaud Colas.
- [Wagtail in industry: from farming to finance - Wagtail Space 2025](https://www.youtube.com/watch?v=DH87OzXzj28&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=3) by Vince Salvino.
- [Redesigning and refactoring Wagtail components - Wagtail Space 2025](https://www.youtube.com/watch?v=8h0fxe7b8s8&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=4) by Mariana.
- [Building Better Wagtail Sites: Traits of a Good CMS - Wagtail Space 2025](https://www.youtube.com/watch?v=n5KHTLS22YE&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=5) by Michael Trythall.
- [REX: Building a SaaS from Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=3T-ITKTByH4&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=6) by Sébastien Corbin.
- [Implement the French Government Design System in Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=8_CBltGuv0g&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=7) by Sylvain Boissel and Lucie Laporte.
- [Wagtail Nest: Maintaining Community Packages Together - Wagtail Space 2025](https://www.youtube.com/watch?v=h0kKy4R5kNY&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=8) by Coen van der Kamp.
- [Automated Data Loader: Wagtail for Weather Data Integration - Wagtail Space 2025](https://www.youtube.com/watch?v=iTxcq__Gcr4&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=9) by Erick Otenyo and Grace Amondi.
- [Building Flexible Wagtail CMS Experiences for Editors - Wagtail Space 2025](https://www.youtube.com/watch?v=-azqKJdEivk&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=10) by Annette Lewis and Eric Sherman.
- [Building a little YouTube on Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=hLw3FWb2LfQ&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=11) by Tom Dyson.
- [Creating connections between stories and objects using AI - Wagtail Space 2025](https://www.youtube.com/watch?v=Wkjm8xdV_6c&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=12) by Trish Thomas.
- [AI in Wagtail: responsible innovation for content editors - Wagtail Space 2025](https://www.youtube.com/watch?v=n2fIFJLSH5E&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=16) by Sage Abdullah and Tom Usher.
- [The Bogotá Digital Library: A Wagtail Success Story - Wagtail Space 2025](https://www.youtube.com/watch?v=cbANVWkDIs0&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=17) by Juan Aguayo.
- [Wagtail and AI Agentic Coding - Wagtail Space 2025](https://www.youtube.com/watch?v=pukU8F3ciEM&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=18) by Maciej Baron.
- [The Impact of A Contribution to Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=sW8k4F1DY18&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=19) by Chiemezuo Akujobi.
- [One URL to Rule Them All: Dynamic Landing Pages in Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=UOEvu4Lyj8w&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=20) by Chrissy Wainwright and Doug Harris.
- [Fact checking with Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=Spdt-W5XotM&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=21) by Jon Chittenden and Craig Dawson.
- [Sympa newsletters with Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=n7bM54MAc24&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=22) by Agnès Haasser.
- [Code that creates content - Wagtail Space 2025](https://www.youtube.com/watch?v=XkSX195ssjY&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=23) by Alex Morega.
- [Who's that code snippet? A screen reader guessing game - Wagtail Space 2025](https://www.youtube.com/watch?v=VkPOe_JixTI&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=24) by Laura Wissiak and Pawel Masarczyk.
- [Bird Meets Bot: Using AI Tools to Make Wagtail Smarter - Wagtail Space 2025](https://www.youtube.com/watch?v=SsjXnpuLnL0&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=25) by Alex Tomkins.
- [Where next for Wagtail Search? - Wagtail Space 2025](https://www.youtube.com/watch?v=LglWFsqIu3E&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=26) by Matt Westcott.

### Podcasts

- [Podcast.\_\_init\_\_ Episode 58 - Wagtail with Tom Dyson](https://www.pythonpodcast.com/episodepage/episode-58-wagtail-with-tom-dyson) - In this episode Tom Dyson explains how Wagtail came to be created, what sets it apart from other options, and when you should implement it for your projects.
- [Django Chat E9: Wagtail CMS - Tom Dyson](https://djangochat.com/episodes/wagtail-cms-tom-dyson) - An interview with Tom Dyson on Wagtail, the leading Django-based CMS used by tens of thousands of organizations including Google, NASA, and the British NHS.
- [Django Chat E84: Dawn Wages](https://djangochat.com/episodes/wagtail-react-gatsby-dawn-wages-RaD8k37m) - An interview with Dawn Wages, a core Wagtail team member. Discussion about Wagtail, React and Gatsby.
- [Django Chat E168: Thibaud Colas](https://djangochat.com/episodes/thibaud-colas-2025-dsf-board-nominations) - An interview with a core team member of Wagtail, discussing the current status of Django, upcoming DSF Board elections, Wagtail roadmap & community opportunities.

### Videos

- [Learn Wagtail](https://learnwagtail.com/) - Regular video tutorials about all aspects of Wagtail.
- [Wagtail Wednesdays #01 - Adding Help Text to Improve Wagtail Editor Experience](https://www.youtube.com/watch?v=ciYNMcv3lE0) - Catherine talks you through the steps you can take to add some useful supplementary text fields to the Wagtail admin.
- [Wagtail Wednesdays #02 - Customising Rich Text Features in Wagtail](https://www.youtube.com/watch?v=ei7ot_Wry3o) - Catherine talks you through the steps you can take to customise your rich text editors to control which features are available to your content editors.
- [Wagtail Wednesdays #03 - Using tabs to create a cleaner admin interface](https://www.youtube.com/watch?v=uZc0aZrHtQw) - Chris talks you through using tabs to organise fields.
- [Wagtail Wednesdays #04 - Organising Images and Documents using Wagtail Collections](https://www.youtube.com/watch?v=HGXHtFpLDCA) - Kieran talks you through the process of organising your images and documents into collections.
- [Wagtail Wednesdays #05 - How to organise your fields and streamline the editor experience](https://www.youtube.com/watch?v=CedcZmQ9KHs) - Chelsea talks you through the process of organising your fields to make it easier to manage them and streamline the editor experience.
- [Wagtail Wednesdays #06 - Creating & using custom settings in your wagtail site](https://www.youtube.com/watch?v=KJWCGq3IRNc) - Chris talks you through setting up and using custom site settings.
- [Wagtail Wednesdays #07 - How to Enable the Wagtail Styleguide](https://www.youtube.com/watch?v=_CfU9UivYPI) - It’s a really helpful resource that takes no time at all to enable and it allows you to check your components against the guidelines and shows all the available Wagtail icons.
- [How to Deploy Wagtail to Google App Engine](https://www.youtube.com/watch?v=uD9PTag2-PQ) - Focus is Google Cloud Platform but a great introduction on how to get Wagtail up and running in their PAAS.

### Showcases

- [Offiical showcase - Projects made with Wagtail](https://wagtail.org/showcase/) - Curated list of websites and apps that gives you a taste of the very best projects built with Wagtail.
- [Made with Wagtail](https://madewithwagtail.org/) - A showcase of sites and apps made with Wagtail CMS.

### Package lists

- [Wagtail third-party packages](https://wagtail.org/packages/) - Official list based on PyPI data.
- [Framework: Wagtail on PyPI](https://pypi.org/search/?c=Framework+%3A%3A+Wagtail) - Packages tagged as `Framework: Wagtail`.
- [Wagtail grid - Django Packages](https://djangopackages.org/grids/g/wagtail-cms/) - Wagtail projects and packages on Django Packages.

## For editors

- [Wagtail user guide](https://guide.wagtail.org/) - The official user guide for anyone creating content or managing content production in Wagtail
- [How Do I Wagtail?](https://www.mozillafoundation.org/en/docs/how-do-i-wagtail/) - Mozilla's editor facing guide for how to use Wagtail's admin interface.
- [CCA Wagtail Editor Portal](https://portal.cca.edu/help/wagtail-documentation/) - User facing documentation for Wagtail by California College of the Arts
- [Caltech Wagtail Editor Portal](https://sites.caltech.edu/) - User facing documentation for Wagtail by Caltech

## Community

- [Wagtail Space](https://www.wagtail.space/) - Wagtail training sessions, Wagtail (lightning) talks and a Wagtail sprint. From March 13th until 15th 2019, Wagtail Space takes place in Arnhem, The Netherlands.
- [Wagtail updates on Telegram](https://telegram.me/wagtail) - Unofficial Telegram channel for general Wagtail updates.
- [Wagtail support on Telegram](https://telegram.me/wagtailcms) - Unofficial Telegram channel for support questions and discussions.

## Open-source sites

- [Wagtail demo project](https://github.com/wagtail/bakerydemo) [![GitHub stars](https://img.shields.io/github/stars/wagtail/bakerydemo?style=flat)](https://github.com/wagtail/bakerydemo/stargazers) – Next generation Wagtail demo, born in Reykjavík.
- [Torchbox.com on Wagtail](https://github.com/torchbox/torchbox.com) [![GitHub stars](https://img.shields.io/github/stars/torchbox/torchbox.com?style=flat)](https://github.com/torchbox/torchbox.com/stargazers) – Torchbox website 2024 incarnation.
- [Made with Wagtail](https://github.com/springload/madewithwagtail) [![GitHub stars](https://img.shields.io/github/stars/springload/madewithwagtail?style=flat)](https://github.com/springload/madewithwagtail/stargazers) - A showcase of sites and apps made with Wagtail CMS, the easy to use, open source Django content management system.
- [Federal Election Commission](https://github.com/fecgov/fec-cms) [![GitHub stars](https://img.shields.io/github/stars/fecgov/fec-cms?style=flat)](https://github.com/fecgov/fec-cms/stargazers) – The content management system (CMS) for the new Federal Election Commission website.
- [Bow Valley SPCA Website](https://github.com/nfletton/bvspca) [![GitHub stars](https://img.shields.io/github/stars/nfletton/bvspca?style=flat)](https://github.com/nfletton/bvspca/stargazers) – Wagtail/Django based website of the Bow Valley SPCA.
- [SecureDrop](https://github.com/freedomofpress/securedrop.org) [![GitHub stars](https://img.shields.io/github/stars/freedomofpress/securedrop.org?style=flat)](https://github.com/freedomofpress/securedrop.org/stargazers) – Wagtail-powered website of the SecureDrop whistleblower document submission system.
- [consumerfinance.gov](https://github.com/cfpb/consumerfinance.gov) [![GitHub stars](https://img.shields.io/github/stars/cfpb/consumerfinance.gov?style=flat)](https://github.com/cfpb/consumerfinance.gov/stargazers) – Django project protecting American consumers.
- [Western Friend website](https://github.com/WesternFriend/westernfriend.org) [![GitHub stars](https://img.shields.io/github/stars/WesternFriend/westernfriend.org?style=flat)](https://github.com/WesternFriend/westernfriend.org/stargazers) - A website for Western Friend (westernfriend.org), a Quaker publication that provides resources and support for Quaker communities and individuals seeking to live out their faith in the world. Western Friend is part of the Religious Society of Friends.
- [Outreachy website](https://github.com/outreachy/website) [![GitHub stars](https://img.shields.io/github/stars/outreachy/website?style=flat)](https://github.com/outreachy/website/stargazers) - Code for the Outreachy website, based on Python, Django, and Bootstrap.
- [Wagtail user guide](https://github.com/wagtail/guide) [![GitHub stars](https://img.shields.io/github/stars/wagtail/guide?style=flat)](https://github.com/wagtail/guide/stargazers) - A website to teach Wagtail to content editors, moderators and administrators.
- [Penticon Public Library](https://github.com/danlerche/public-library-wagtailCMS) [![GitHub stars](https://img.shields.io/github/stars/danlerche/public-library-wagtailCMS?style=flat)](https://github.com/danlerche/public-library-wagtailCMS/stargazers) - This is an example public library website using wagtail CMS.

## Contribute

Contributions are always welcome! Please read the [contribution guidelines](docs/CONTRIBUTING.md) first.

## License

This work by [Springload](https://www.springload.co.nz/) and other contributors is marked [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
