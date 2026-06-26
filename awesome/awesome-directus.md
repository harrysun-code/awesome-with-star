# Directus

[![GitHub stars](https://img.shields.io/github/stars/directus-community/awesome-directus?style=flat)](https://github.com/directus-community/awesome-directus/stargazers)

<p align="center"><a href="https://directus.io"><img alt="Directus Logo" src="https://user-images.githubusercontent.com/522079/158864859-0fbeae62-9d7a-4619-b35e-f8fa5f68e0c8.png" width="1000px"></a></p>

# Awesome Directus [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome things related to Directus

[Directus](https://directus.io) is a real-time API and App dashboard for managing SQL database content.

## Contents

- [Resources](#resources)
  - [Official](#official)
  - [Community](#community)
- [Integration](#integration)
- [Extensions](#extensions)
  - [Extension Scripts](#extension-scripts)
  - [Tools](#tools)
- [Articles](#articles)
  - [Educational](#educational)
  - [Personal](#personal)
- [Examples / Showcases](#examples--showcases)

## Resources

### Official

- [Documentation](https://docs.directus.io/getting-started/introduction/)
- [GitHub Repository](https://github.com/directus/directus) [![GitHub stars](https://img.shields.io/github/stars/directus/directus?style=flat)](https://github.com/directus/directus/stargazers)
- [Live Discussions on Discord](https://directus.chat)
- [Community Help Board](https://github.com/directus/directus/discussions/categories/q-a) [![GitHub stars](https://img.shields.io/github/stars/directus/directus/discussions/categories/q-a?style=flat)](https://github.com/directus/directus/discussions/categories/q-a/stargazers)
- [Video Tutorials on YouTube](https://www.youtube.com/c/DirectusVideos/featured)
- [Community Repositories](https://github.com/directus-community) [![GitHub stars](https://img.shields.io/github/stars/directus-community?style=flat)](https://github.com/directus-community/stargazers)

### Community

- [Directus Extensions](https://directusextensions.com) - A searchable index of Directus extensions, themes, OSes, and more.
- [Portuguese YouTube Channel](https://www.youtube.com/c/DirectusBR)

## Integration

- [Official JS SDK](https://www.npmjs.com/package/@directus/sdk) - The JS SDK provides an intuitive interface for the Directus API from within a JavaScript-powered project (Browsers and Node.js).
- [Official Gatsby Source Plugin](https://www.npmjs.com/package/@directus/gatsby-source-directus) - Source plugin for pulling data into Gatsby from a Directus API.
- [react-directus](https://github.com/gremo/react-directus) [![GitHub stars](https://img.shields.io/github/stars/gremo/react-directus?style=flat)](https://github.com/gremo/react-directus/stargazers) - A set of React components and utilities for Directus Headless CMS.
- [Flutter SDK](https://pub.dev/packages/directus) - Flutter SDK to provide interface for Directus API.
- [PHP SDK](https://github.com/alantiller/directus-php-sdk) [![GitHub stars](https://img.shields.io/github/stars/alantiller/directus-php-sdk?style=flat)](https://github.com/alantiller/directus-php-sdk/stargazers) - PHP SDK to provide easy access to the Directus API.
- [Lite SDK (TypeScript)](https://github.com/jacoborus/directus-lite-sdk) [![GitHub stars](https://img.shields.io/github/stars/jacoborus/directus-lite-sdk?style=flat)](https://github.com/jacoborus/directus-lite-sdk/stargazers) - Query builder for the Directus API (Browser, Deno, Node.js). Bring your own fetch.
- [Nuxt Directus](https://github.com/directus-community/nuxt-directus) [![GitHub stars](https://img.shields.io/github/stars/directus-community/nuxt-directus?style=flat)](https://github.com/directus-community/nuxt-directus/stargazers) - First-Class Nuxt 3 Module for connecting with an Directus instance.
- [Nuxtus](https://nuxtus.com) - Provides a Nuxt boilerplate and set of tools to automatically create Nuxt pages from Directus Collections.
- [cool-stack](https://github.com/tdsoftpl/cool-stack) [![GitHub stars](https://img.shields.io/github/stars/tdsoftpl/cool-stack?style=flat)](https://github.com/tdsoftpl/cool-stack/stargazers) - Template repository integrating Directus & Remix into a full-stack monorepo.

## Extensions

- [Image Scout](https://github.com/resauce-dev/directus-image-scout?ref=awesome-directus) [![GitHub stars](https://img.shields.io/github/stars/resauce-dev/directus-image-scout?ref=awesome-directus?style=flat)](https://github.com/resauce-dev/directus-image-scout?ref=awesome-directus/stargazers) - Search and select images found on a variety of royalty free image sites (Pexels, Pixabay, Unsplash & Giphy!).
- [Editor.js Interface](https://github.com/dimitrov-adrian/directus-extension-editorjs-interface) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-editorjs-interface?style=flat)](https://github.com/dimitrov-adrian/directus-extension-editorjs-interface/stargazers) - Block editor (Editor.js) interface for Directus 9.
- [Draw Interface](https://github.com/jesusgp22/directus-draw-interface) [![GitHub stars](https://img.shields.io/github/stars/jesusgp22/directus-draw-interface?style=flat)](https://github.com/jesusgp22/directus-draw-interface/stargazers) - Free draw interface for Directus app.
- [User-friendly file paths](https://gist.github.com/ToJans/fa18e2a7363edd24be6ad8dda2dd0232) - Use the folder and file module structure to reference to assets.
- [Date Picker Interface](https://github.com/u12206050/directus-9-date-picker-interface) [![GitHub stars](https://img.shields.io/github/stars/u12206050/directus-9-date-picker-interface?style=flat)](https://github.com/u12206050/directus-9-date-picker-interface/stargazers) - An alternative Date Picker Interface to the original Directus DateTime interface.
- [Search Sync](https://github.com/dimitrov-adrian/directus-extension-searchsync) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-searchsync?style=flat)](https://github.com/dimitrov-adrian/directus-extension-searchsync/stargazers) - Sync data into a search engine index, supports Algolia, ElasticSearch & MeiliSearch.
- [Dictionary](https://github.com/georgexchelebiev/directus-dictionary) [![GitHub stars](https://img.shields.io/github/stars/georgexchelebiev/directus-dictionary?style=flat)](https://github.com/georgexchelebiev/directus-dictionary/stargazers) - Save key-value pairs as JSON blobs with a progress indicator for completeness.
- [WordPress-like Slug](https://github.com/dimitrov-adrian/directus-extension-wpslug-interface) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-wpslug-interface?style=flat)](https://github.com/dimitrov-adrian/directus-extension-wpslug-interface/stargazers) - Slug/Permalink interface with support for pre- and suffixes.
- [Link Meta](https://github.com/dimitrov-adrian/directus-extension-linkmeta) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-linkmeta?style=flat)](https://github.com/dimitrov-adrian/directus-extension-linkmeta/stargazers) - Stores hyperlink metadata into Directus.
- [Group Modal](https://github.com/dimitrov-adrian/directus-extension-group-modal-interface) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-group-modal-interface?style=flat)](https://github.com/dimitrov-adrian/directus-extension-group-modal-interface/stargazers) - Group interface fields into a modal that can be opened with a button.
- [Display Link](https://github.com/jacoborus/directus-extension-display-link) [![GitHub stars](https://img.shields.io/github/stars/jacoborus/directus-extension-display-link?style=flat)](https://github.com/jacoborus/directus-extension-display-link/stargazers) - Display URLs with an "open in new tab" button.
- [SQL Panel](https://github.com/harish2704/directus-sql-panel) [![GitHub stars](https://img.shields.io/github/stars/harish2704/directus-sql-panel?style=flat)](https://github.com/harish2704/directus-sql-panel/stargazers) - Panel component which shows result of stored SQL query as a table.
- [SVG Map Picker Interface](https://github.com/dimitrov-adrian/directus-extension-svgmap-picker-interface) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-svgmap-picker-interface?style=flat)](https://github.com/dimitrov-adrian/directus-extension-svgmap-picker-interface/stargazers) - Select a value from a SVG Map box.
- [Directus Mailer](https://github.com/ryntab/Directus-Mailer) [![GitHub stars](https://img.shields.io/github/stars/ryntab/Directus-Mailer?style=flat)](https://github.com/ryntab/Directus-Mailer/stargazers) - An endpoint for sending emails with the Directus Nodemailer service.
- [Data Grid Interface](https://github.com/seymoe/directus-extension-vgrid-interface) [![GitHub stars](https://img.shields.io/github/stars/seymoe/directus-extension-vgrid-interface?style=flat)](https://github.com/seymoe/directus-extension-vgrid-interface/stargazers) - A data grid interface width `@revolist/vue3-datagrid` for Directus 9.
- [SparkLine Display](https://github.com/seymoe/directus-extension-sparkline-display) [![GitHub stars](https://img.shields.io/github/stars/seymoe/directus-extension-sparkline-display?style=flat)](https://github.com/seymoe/directus-extension-sparkline-display/stargazers) - A sparkline display with `apexcharts` for Directus 9.
- [Tags M2M](https://github.com/dimitrov-adrian/directus-extension-tags-m2m-interface) [![GitHub stars](https://img.shields.io/github/stars/dimitrov-adrian/directus-extension-tags-m2m-interface?style=flat)](https://github.com/dimitrov-adrian/directus-extension-tags-m2m-interface/stargazers) - M2M driven tags interface.
- [Sanitize HTML](https://github.com/licitdev/directus-extension-sanitize-html) [![GitHub stars](https://img.shields.io/github/stars/licitdev/directus-extension-sanitize-html?style=flat)](https://github.com/licitdev/directus-extension-sanitize-html/stargazers) - Sanitize HTML inputs to Directus.
- [Directus LogSnag](https://github.com/Intevel/directus-logsnag) [![GitHub stars](https://img.shields.io/github/stars/Intevel/directus-logsnag?style=flat)](https://github.com/Intevel/directus-logsnag/stargazers) - Sending your events from Directus directly to your phone using LogSnag.
- [Field Actions](https://github.com/utomic-media/directus-extension-field-actions) [![GitHub stars](https://img.shields.io/github/stars/utomic-media/directus-extension-field-actions?style=flat)](https://github.com/utomic-media/directus-extension-field-actions/stargazers) - Adds copy to clipboard and open URL's action-buttons to fields (interface + display).
- [Generate Types](https://github.com/maltejur/directus-extension-generate-types) [![GitHub stars](https://img.shields.io/github/stars/maltejur/directus-extension-generate-types?style=flat)](https://github.com/maltejur/directus-extension-generate-types/stargazers) - Adds a module for generating typescript types for a Directus JS-SDK connected to that Directus database. Also can generate Python or OpenAPI types.
- [Computed Interface](https://github.com/rezo-labs/directus-extension-computed-interface) [![GitHub stars](https://img.shields.io/github/stars/rezo-labs/directus-extension-computed-interface?style=flat)](https://github.com/rezo-labs/directus-extension-computed-interface/stargazers) - Perform computed value based on other fields.
- [Inline Form Interface](https://github.com/hanneskuettner/directus-extension-inline-form-interface) [![GitHub stars](https://img.shields.io/github/stars/hanneskuettner/directus-extension-inline-form-interface?style=flat)](https://github.com/hanneskuettner/directus-extension-inline-form-interface/stargazers) - Edit M2O relations in an inline form contained in the parent record.
- [Tab Group Interface](https://github.com/hanneskuettner/directus-extension-group-tabs-interface) [![GitHub stars](https://img.shields.io/github/stars/hanneskuettner/directus-extension-group-tabs-interface?style=flat)](https://github.com/hanneskuettner/directus-extension-group-tabs-interface/stargazers) - Display groups as tab panels, as a pretty, space saving alternative to the accordion group.
- [Woodpecker Build Status](https://github.com/sguter90/directus-extension-woodpecker-build-status) [![GitHub stars](https://img.shields.io/github/stars/sguter90/directus-extension-woodpecker-build-status?style=flat)](https://github.com/sguter90/directus-extension-woodpecker-build-status/stargazers) - Adds status bar for [Woodpecker](https://woodpecker-ci.org/) pipeline build status to Directus UI.
- [Imagga Hook](https://github.com/gbicou/directus-extension-imagga) [![GitHub stars](https://img.shields.io/github/stars/gbicou/directus-extension-imagga?style=flat)](https://github.com/gbicou/directus-extension-imagga/stargazers) - Hook for file uploads to automatically tag images with [Imagga API](https://imagga.com/).
- [Tiptap Interface & Display](https://github.com/gbicou/directus-extension-tiptap) [![GitHub stars](https://img.shields.io/github/stars/gbicou/directus-extension-tiptap?style=flat)](https://github.com/gbicou/directus-extension-tiptap/stargazers) - Tiptap rich text editor interface and display.
- [API Viewer](https://github.com/u12206050/directus-extension-api-viewer-module) [![GitHub stars](https://img.shields.io/github/stars/u12206050/directus-extension-api-viewer-module?style=flat)](https://github.com/u12206050/directus-extension-api-viewer-module/stargazers) - View and run API queries directly from a Module.
- [Flexible Editor](https://github.com/formfcw/directus-extension-flexible-editor) [![GitHub stars](https://img.shields.io/github/stars/formfcw/directus-extension-flexible-editor?style=flat)](https://github.com/formfcw/directus-extension-flexible-editor/stargazers) - A Rich Text Editor (WYSIWYG) with JSON output, that allows to integrate M2A relations to make it extremely flexible.
- [BlurHash](https://github.com/pixielabs/directus-extension-blurhash/) [![GitHub stars](https://img.shields.io/github/stars/pixielabs/directus-extension-blurhash/?style=flat)](https://github.com/pixielabs/directus-extension-blurhash//stargazers) - A Directus extension that generates blurhashes for uploaded images.
- [Media AI Bundle](https://github.com/Arood/directus-extension-media-ai-bundle) [![GitHub stars](https://img.shields.io/github/stars/Arood/directus-extension-media-ai-bundle?style=flat)](https://github.com/Arood/directus-extension-media-ai-bundle/stargazers) - Two operations to perform image description and OCR.
- [Directus Copilot](https://github.com/programmarchy/directus-extension-copilot/) [![GitHub stars](https://img.shields.io/github/stars/programmarchy/directus-extension-copilot/?style=flat)](https://github.com/programmarchy/directus-extension-copilot//stargazers) - A bundle including a panel to ask data-aware questions in a chat interface.
- [OpenAI Automatic Translation](https://github.com/timio23/directus-operation-auto-translate/) [![GitHub stars](https://img.shields.io/github/stars/timio23/directus-operation-auto-translate/?style=flat)](https://github.com/timio23/directus-operation-auto-translate//stargazers) - An operaiton to automatically translate new items via OpenAI.
- [Machine Learning Operations](https://github.com/karamokoisrael/directus-hackathon-submission/) [![GitHub stars](https://img.shields.io/github/stars/karamokoisrael/directus-hackathon-submission/?style=flat)](https://github.com/karamokoisrael/directus-hackathon-submission//stargazers) - A set of extensions to train, test and use machine learning models.
- [Tab Group](https://github.com/formfcw/directus-extension-tab-group) [![GitHub stars](https://img.shields.io/github/stars/formfcw/directus-extension-tab-group?style=flat)](https://github.com/formfcw/directus-extension-tab-group/stargazers) - A group interface with a tab menu for toggling the visibility of fields within the group.
- [Drawer Notice](https://github.com/formfcw/directus-extension-drawer-notice) [![GitHub stars](https://img.shields.io/github/stars/formfcw/directus-extension-drawer-notice?style=flat)](https://github.com/formfcw/directus-extension-drawer-notice/stargazers) - A notice field that is only visible in the drawer.
- [Classified Group](https://github.com/formfcw/directus-extension-classified-group) [![GitHub stars](https://img.shields.io/github/stars/formfcw/directus-extension-classified-group?style=flat)](https://github.com/formfcw/directus-extension-classified-group/stargazers) - A group to which a class can be assigned for custom styling.
- [Tokenized Preview](https://github.com/formfcw/directus-extension-tokenized-preview) [![GitHub stars](https://img.shields.io/github/stars/formfcw/directus-extension-tokenized-preview?style=flat)](https://github.com/formfcw/directus-extension-tokenized-preview/stargazers) - An endpoint that adds an active auth token to your preview URL.
- [Umami Analytics](https://github.com/egidiusmengelberg/directus-extension-umami) [![GitHub stars](https://img.shields.io/github/stars/egidiusmengelberg/directus-extension-umami?style=flat)](https://github.com/egidiusmengelberg/directus-extension-umami/stargazers) - Add Umami analytics to Directus.
- [Auto generate file transformations](https://github.com/utomic-media/directus-extension-auto-generate-file-transformations) [![GitHub stars](https://img.shields.io/github/stars/utomic-media/directus-extension-auto-generate-file-transformations?style=flat)](https://github.com/utomic-media/directus-extension-auto-generate-file-transformations/stargazers) - Automatically generate selected file transformations on upload 

### Extension Scripts

- [Directus Hook Library](https://github.com/formfcw/directus-hook-library) [![GitHub stars](https://img.shields.io/github/stars/formfcw/directus-hook-library?style=flat)](https://github.com/formfcw/directus-hook-library/stargazers) - A collection of customizable hooks for Directus.

### Tools

- [Directus Sync](https://github.com/tractr/directus-sync) [![GitHub stars](https://img.shields.io/github/stars/tractr/directus-sync?style=flat)](https://github.com/tractr/directus-sync/stargazers) - A CLI tool for synchronizing the schema and configuration of Directus across various environments.

## Articles

### Educational

- [Directus Guides (Official)](https://directus.io/guides/)
- [Learn Directus](https://learndirectus.com/)
- [How to Work With Many to Many Relationships (M2M) On Directus](https://medium.com/@bianperotti/how-i-made-a-many-to-many-relationship-on-directus-b158ff55de7e)
- [Creating a Custom Panel in Directus With Chart.js](https://blog.eperedo.com/2023/02/14/custom-panel-directus-chart-js)

### Personal

- [Get Started With Directus](https://medium.com/7span/no-code-backend-get-started-with-directus-7876bffdbd1d)

## Examples / Showcases

If you're using Directus in an open source project, you're very welcome to link this project here.

- [Official Examples](https://github.com/directus/examples) [![GitHub stars](https://img.shields.io/github/stars/directus/examples?style=flat)](https://github.com/directus/examples/stargazers) - Integration examples with Directus.
- [Nuxt 3 Demo](https://github.com/bryantgillespie/nuxt3-directus-starter) [![GitHub stars](https://img.shields.io/github/stars/bryantgillespie/nuxt3-directus-starter?style=flat)](https://github.com/bryantgillespie/nuxt3-directus-starter/stargazers) - Opinionated Nuxt 3 / Directus Starter with Tailwind CSS.
- [Agency OS](https://github.com/directus-community/agency-os) [![GitHub stars](https://img.shields.io/github/stars/directus-community/agency-os?style=flat)](https://github.com/directus-community/agency-os/stargazers) - Fully complete, opinionated agency website template featuring Nuxt and Directus. View [Demo](https://www.agencyos.dev/).
- [Nextus](https://github.com/luochuanyuewu/nextus) [![GitHub stars](https://img.shields.io/github/stars/luochuanyuewu/nextus?style=flat)](https://github.com/luochuanyuewu/nextus/stargazers) - A comprehensive, versatile and modern website template based on Nextjs and Directus technologies. It helps you build various types of websites more quickly. View [Demo](https://nextus.vercel.app/en).

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
