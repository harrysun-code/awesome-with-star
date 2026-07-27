# Quick Look Plugins

> 来源：[sindresorhus/quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins)

[![GitHub stars](https://img.shields.io/github/stars/sindresorhus/quick-look-plugins?style=flat)](https://github.com/sindresorhus/quick-look-plugins/stargazers)

# Quick Look plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> List of useful [Quick Look](https://en.wikipedia.org/wiki/Quick_Look) plugins for developers

## Install

### Using [Homebrew](https://brew.sh)

- Run `brew install <package>`

##### Catalina notes

To get many plugins working in Catalina and later, you will need to remove the quarantine attribute.

Run this to see the attributes:

```
xattr -r ~/Library/QuickLook
```

And run this to remove the attributes:

```
xattr -d -r com.apple.quarantine ~/Library/QuickLook
```

### Manually

- Click "download manually"
- Move the downloaded .qlgenerator file to `~/Library/QuickLook`
- Run `qlmanage -r`

## Plugins

### [QLStephen](https://github.com/whomwah/qlstephen) [![GitHub stars](https://img.shields.io/github/stars/whomwah/qlstephen?style=flat)](https://github.com/whomwah/qlstephen/stargazers)

> Preview plain text files without or with unknown file extension. Example: README, CHANGELOG, index.styl, etc.

Run `brew install qlstephen` or [download manually](https://github.com/whomwah/qlstephen/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/whomwah/qlstephen/releases/latest?style=flat)](https://github.com/whomwah/qlstephen/releases/latest/stargazers)

[![](screenshots/QLStephen.png)](https://github.com/whomwah/qlstephen)

### [QLMarkdown](https://github.com/sbarex/QLMarkdown) [![GitHub stars](https://img.shields.io/github/stars/sbarex/QLMarkdown?style=flat)](https://github.com/sbarex/QLMarkdown/stargazers)

> Preview Markdown files

Run `brew install --cask qlmarkdown` or [download manually](https://github.com/sbarex/QLMarkdown/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/sbarex/QLMarkdown/releases/latest?style=flat)](https://github.com/sbarex/QLMarkdown/releases/latest/stargazers)

[![](screenshots/QLMarkdown.png)](https://github.com/sbarex/QLMarkdown)

### [QuickLookJSON](http://www.sagtau.com/quicklookjson.html)

> Preview JSON files

[Download manually](http://www.sagtau.com/media/QuickLookJSON.qlgenerator.zip)

[![](screenshots/QuickLookJSON.png)](http://www.sagtau.com/quicklookjson.html)

### [BetterZipQL](https://macitbetter.com/downloads/)

> Preview archives

> Note: The BetterZipQL plugin was integrated with the BetterZip app.

Run `brew install betterzip` to install the BetterZip app and its Quick Look plugin or [download manually](https://macitbetter.com/BetterZip.zip)

The legacy BetterZipQL plugin can be [downloaded here](https://macitbetter.com/dl/BetterZipQL-1.5.zip).

[![](screenshots/BetterZipQL.png)](https://macitbetter.com/BetterZip-Quick-Look-Generator/)

### [Suspicious Package](https://www.mothersruin.com/software/SuspiciousPackage/)

> Preview the contents of a standard Apple installer package

Run `brew install suspicious-package` or [download manually](https://www.mothersruin.com/software/downloads/SuspiciousPackage.xip)

[![](screenshots/SuspiciousPackage.png)](https://www.mothersruin.com/software/SuspiciousPackage/)

### [Apparency](https://www.mothersruin.com/software/Apparency/)

> Preview the contents of a macOS app

Run `brew install apparency` or [download manually](https://mothersruin.com/software/downloads/Apparency.dmg)

[![](screenshots/Apparency.png)](https://mothersruin.com/software/Apparency/)

### [QLVideo](https://github.com/Marginal/QLVideo) [![GitHub stars](https://img.shields.io/github/stars/Marginal/QLVideo?style=flat)](https://github.com/Marginal/QLVideo/stargazers)

> Preview most types of video files, as well as their thumbnails, cover art and metadata

Run `brew install qlvideo` or [download manually](https://github.com/Marginal/QLVideo/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/Marginal/QLVideo/releases/latest?style=flat)](https://github.com/Marginal/QLVideo/releases/latest/stargazers)

[![](screenshots/QLVideo.png)](https://github.com/Marginal/QLVideo)

### [Source Code Preview](https://anybox.ltd/source-code-preview) 💰

> Includes 10+ color themes and syntax highlighting for 50+ languages, including JavaScript, Python, Java, CSS, and JSON.

Purchase on the [App Store](https://apps.apple.com/app/source-code-preview/id6759270528).

[![](screenshots/SourceCodePreview.png)](https://anybox.ltd/source-code-preview)

### [Peek](https://bigzlabs.com/peek) 💰

> Peek allows you to copy and find text, jump to line numbers, render Github-flavored Markdown with a generated table of contents, restore scroll positions, highlight syntax, & more in the Quick Look previews of over 300 file extensions.

Purchase on the [App Store](https://apps.apple.com/app/peek-quick-look-extension/id1554235898).

*The app is abandoned and buggy, but still functional.*

[![](screenshots/Peek.png)](https://bigzlabs.com/peek)

### [Folder Preview](https://anybox.ltd/folder-preview) 💰

> Quick look inside folders and archives.

Purchase on the [App Store](https://apps.apple.com/app/folder-preview/id6698876601).

[![](screenshots/FolderPreview.png)](https://anybox.ltd/folder-preview)

### [Folder Quick Look](https://apps.apple.com/app/id6753110395) 💰

> Preview folder and archive contents (ZIP, RAR, and more).

Purchase on the [App Store](https://apps.apple.com/app/id6753110395).

[![](screenshots/FolderQuickLook.png)](https://apps.apple.com/app/id6753110395)

### [FluxMarkdown](https://github.com/xykong/flux-markdown) [![GitHub stars](https://img.shields.io/github/stars/xykong/flux-markdown?style=flat)](https://github.com/xykong/flux-markdown/stargazers)

> Preview Markdown files with Mermaid diagrams, KaTeX math, GFM support, and interactive table of contents.

Run `brew tap xykong/tap && brew install --cask flux-markdown` or [download manually](https://github.com/xykong/flux-markdown/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/xykong/flux-markdown/releases/latest?style=flat)](https://github.com/xykong/flux-markdown/releases/latest/stargazers)

[![](screenshots/FluxMarkdown.png)](https://github.com/xykong/flux-markdown)

### [Markdown Preview](https://anybox.ltd/markdown-preview) 💰

> Quick look Markdown files with KaTex and Mermaid support.

Purchase on the [App Store](https://apps.apple.com/app/markdown-preview-quick-look/id6739955340).

[![](screenshots/MarkdownPreview.png)](https://anybox.ltd/markdown-preview)

### [EPS Preview](https://anybox.ltd/eps-preview) 💰

> EPS Preview adds Quick Look and thumbnails of EPS files to Finder.

Purchase on the [website](https://anybox.ltd/eps-preview).

[![](screenshots/EPSPreview.png)](https://anybox.ltd/eps-preview)

### [ProvisionQL](https://github.com/ealeksandrov/ProvisionQL) [![GitHub stars](https://img.shields.io/github/stars/ealeksandrov/ProvisionQL?style=flat)](https://github.com/ealeksandrov/ProvisionQL/stargazers)

> Preview iOS / macOS app and provision information

Run `brew install provisionql` or [download manually](https://github.com/ealeksandrov/ProvisionQL/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/ealeksandrov/ProvisionQL/releases/latest?style=flat)](https://github.com/ealeksandrov/ProvisionQL/releases/latest/stargazers)

[![](screenshots/ProvisionQL.png)](https://github.com/ealeksandrov/ProvisionQL)

### [WebP](https://github.com/dchest/webp-quicklook) [![GitHub stars](https://img.shields.io/github/stars/dchest/webp-quicklook?style=flat)](https://github.com/dchest/webp-quicklook/stargazers)

> Preview WebP images

> NOTE: This is already covered by `qlImageSize`, so this plugin is listed here only in case you do not like `qlImageSize`.

Run `brew install webpquicklook` or [download manually](https://github.com/dchest/webp-quicklook/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/dchest/webp-quicklook/releases/latest?style=flat)](https://github.com/dchest/webp-quicklook/releases/latest/stargazers)

[![](screenshots/WebP.png)](https://github.com/dchest/webp-quicklook)

### [SourceCodeSyntaxHighlight](https://github.com/sbarex/SourceCodeSyntaxHighlight) [![GitHub stars](https://img.shields.io/github/stars/sbarex/SourceCodeSyntaxHighlight?style=flat)](https://github.com/sbarex/SourceCodeSyntaxHighlight/stargazers)

> Preview many different source code files

Run `brew install --cask --no-quarantine syntax-highlight` or [download manually](https://github.com/sbarex/SourceCodeSyntaxHighlight/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/sbarex/SourceCodeSyntaxHighlight/releases/latest?style=flat)](https://github.com/sbarex/SourceCodeSyntaxHighlight/releases/latest/stargazers)

[![](https://user-images.githubusercontent.com/8471055/118415204-5f53fc80-b6a9-11eb-93d8-b88c442c5744.png)](https://github.com/sbarex/SourceCodeSyntaxHighlight)

**Note:** This might overwrite some other Quick Look plugins.

### [Burrete](https://github.com/SergeiNikolenko/Burrete) [![GitHub stars](https://img.shields.io/github/stars/SergeiNikolenko/Burrete?style=flat)](https://github.com/SergeiNikolenko/Burrete/stargazers)

> Preview PDB, mmCIF, SDF, XYZ, trajectories, and chemistry tables in Finder

[Download manually](https://github.com/SergeiNikolenko/Burrete/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/SergeiNikolenko/Burrete/releases/latest?style=flat)](https://github.com/SergeiNikolenko/Burrete/releases/latest/stargazers)

[![](screenshots/Burrete.png)](https://github.com/SergeiNikolenko/Burrete)

### [Preview3MF](https://github.com/cavoco/Preview3MF) [![GitHub stars](https://img.shields.io/github/stars/cavoco/Preview3MF?style=flat)](https://github.com/cavoco/Preview3MF/stargazers)

> Preview 3MF 3D-printing models — real 3D rendering plus Finder thumbnails

Run `brew install --cask cavoco/tap/preview3mf` or [download manually](https://github.com/cavoco/Preview3MF/releases/latest) [![GitHub stars](https://img.shields.io/github/stars/cavoco/Preview3MF/releases/latest?style=flat)](https://github.com/cavoco/Preview3MF/releases/latest/stargazers)

[![](screenshots/Preview3MF.png)](https://github.com/cavoco/Preview3MF)

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Sindre Sorhus](https://sindresorhus.com) has waived all copyright and related or neighboring rights to this work.
