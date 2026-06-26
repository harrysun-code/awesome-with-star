# Dev Env

[![GitHub stars](https://img.shields.io/github/stars/jondot/awesome-devenv?style=flat)](https://github.com/jondot/awesome-devenv/stargazers)

# Awesome Dev Env [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome tools, resources and workflow tips making an awesome development environment.

Inspired by [awesome-go](https://github.com/avelino/awesome-go) [![GitHub stars](https://img.shields.io/github/stars/avelino/awesome-go?style=flat)](https://github.com/avelino/awesome-go/stargazers), which was in turn inspired by [awesome-python](https://github.com/vinta/awesome-python) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers).

### Contributing

[Guidelines](https://github.com/jondot/awesome-devenv/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/jondot/awesome-devenv/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/jondot/awesome-devenv/blob/master/CONTRIBUTING.md/stargazers) tweaked and adapted from `awesome-go` - thanks!

But in short:

* List is alphabetically sorted
* If you think an item shouldn't be here [open an issue](https://github.com/jondot/awesome-devenv/issues/new) [![GitHub stars](https://img.shields.io/github/stars/jondot/awesome-devenv/issues/new?style=flat)](https://github.com/jondot/awesome-devenv/issues/new/stargazers)


Many thanks to everyone on the [contributor list](https://github.com/jondot/awesome-devenv/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/jondot/awesome-devenv/graphs/contributors?style=flat)](https://github.com/jondot/awesome-devenv/graphs/contributors/stargazers) :)


# Content

_Note: for an OS specific tool, please do your best to mark with `OSX/WIN/*NIX/LIN`_



- [Admins](#admins)
- [Benchmarking](#benchmarking)
- [Data](#data)
- [Diagnostics](#diagnostics)
- [Desktop](#desktop)
- [Documentation](#documentation)
- [Dotfiles](#dotfiles)
- [Editors](#editors)
  - [Atom](#atom)
  - [Sublime Text](#sublime-text-3)
  - [Vim](#vim)
  - [IntelliJ](#intellij)
  - [VSCode](#visual-studio-code)
- [Git](#git)
- [Misc](#misc)
- [Notifications](#notifications)
- [Orchestration](#orchestration)
- [Presentation](#presentation)
- [Shell](#shell)
- [Text](#text)
- [Terminal](#terminal)
- [Workflow](#workflow)


## Admins
*Tools to manage databases, permissions, etc.*

* [hss](https://github.com/six-ddc/hss) [![GitHub stars](https://img.shields.io/github/stars/six-ddc/hss?style=flat)](https://github.com/six-ddc/hss/stargazers) - Never type the annoying ssh commands again.
* [MongoHub](https://github.com/fotonauts/MongoHub-Mac/releases) [![GitHub stars](https://img.shields.io/github/stars/fotonauts/MongoHub-Mac/releases?style=flat)](https://github.com/fotonauts/MongoHub-Mac/releases/stargazers) - Native OSx client for mongo
* [Robomongo](http://robomongo.org/) - a cross platform Admin for MongoDB


## Benchmarking
*Tools to benchmark your code or services*

* [apachebench (ab)](http://httpd.apache.org/docs/2.2/programs/ab.html)
* [boom](https://github.com/rakyll/boom) [![GitHub stars](https://img.shields.io/github/stars/rakyll/boom?style=flat)](https://github.com/rakyll/boom/stargazers)
* [httperf](http://www.hpl.hp.com/research/linux/httperf/)
* [phantomas](https://github.com/macbre/phantomas) [![GitHub stars](https://img.shields.io/github/stars/macbre/phantomas?style=flat)](https://github.com/macbre/phantomas/stargazers) - website perf evaluation tool
* [siege](http://www.joedog.org/siege-home/)
* [Vegeta](https://github.com/tsenart/vegeta) [![GitHub stars](https://img.shields.io/github/stars/tsenart/vegeta?style=flat)](https://github.com/tsenart/vegeta/stargazers)
* [wrk](https://github.com/wg/wrk) [![GitHub stars](https://img.shields.io/github/stars/wg/wrk?style=flat)](https://github.com/wg/wrk/stargazers)
* [redis-faina](https://github.com/Instagram/redis-faina) [![GitHub stars](https://img.shields.io/github/stars/Instagram/redis-faina?style=flat)](https://github.com/Instagram/redis-faina/stargazers) Instagram's Redis counter/timing stats based on the MONITOR command


## Data
*Tools for handling online and offline data*

* [s3cmd](https://github.com/s3tools/s3cmd) [![GitHub stars](https://img.shields.io/github/stars/s3tools/s3cmd?style=flat)](https://github.com/s3tools/s3cmd/stargazers) - the S3 CLI tool for Amazon


## Diagnostics
*Tools for checking diagnosing your system while you work*

* [glances](https://github.com/nicolargo/glances) [![GitHub stars](https://img.shields.io/github/stars/nicolargo/glances?style=flat)](https://github.com/nicolargo/glances/stargazers)
* [nmon](http://nmon.sourceforge.net/pmwiki.php)
* [gtop](https://github.com/aksakalli/gtop) [![GitHub stars](https://img.shields.io/github/stars/aksakalli/gtop?style=flat)](https://github.com/aksakalli/gtop/stargazers)


## Desktop
*Tools for improving and hacking around with your vanilla desktop*

* [Alfred](http://www.alfredapp.com/) - OSX productivity app `/OSX/`
* [hydra](https://github.com/sdegutis/hydra) [![GitHub stars](https://img.shields.io/github/stars/sdegutis/hydra?style=flat)](https://github.com/sdegutis/hydra/stargazers) - script your desktop
  `/OSX/`
* [Keycastr](https://github.com/sdeken/keycastr) [![GitHub stars](https://img.shields.io/github/stars/sdeken/keycastr?style=flat)](https://github.com/sdeken/keycastr/stargazers) - show your keys while
  presenting/casting `/OSX/`

## Documentation
*Tools to document your project*

* [Log4brains](https://github.com/thomvaill/log4brains) [![GitHub stars](https://img.shields.io/github/stars/thomvaill/log4brains?style=flat)](https://github.com/thomvaill/log4brains/stargazers) - Docs-as-code knowledge base to manage Architecture Decision Records (ADR) for your project and publish them automatically as a static website.


## Dotfiles

* [dotfiles.github.io](https://dotfiles.github.io/) - Collected dotfile resources. Has sections with dotfile bootstraps and lists of frameworks for various shells and editors.
* [Zach Holman's](https://github.com/holman/dotfiles) [![GitHub stars](https://img.shields.io/github/stars/holman/dotfiles?style=flat)](https://github.com/holman/dotfiles/stargazers) - oh-my-zsh, osx, Zsh, vi, Ruby, Git, and more
* [Mathias Bynens's](https://github.com/mathiasbynens/dotfiles) [![GitHub stars](https://img.shields.io/github/stars/mathiasbynens/dotfiles?style=flat)](https://github.com/mathiasbynens/dotfiles/stargazers) - .files, including ~/.osx — sensible hacker defaults for OS X
* [Thoughtbot's](https://github.com/thoughtbot/dotfiles) [![GitHub stars](https://img.shields.io/github/stars/thoughtbot/dotfiles?style=flat)](https://github.com/thoughtbot/dotfiles/stargazers) - A set of vim, zsh, git, and tmux configuration files
* [Paul Miller's](https://github.com/paulmillr/dotfiles) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/dotfiles?style=flat)](https://github.com/paulmillr/dotfiles/stargazers) - Colourful & robust OS X configuration files and utilities


## Editors
*Only awesome tools and addons for your favorite editor*

### Atom

* [atom-beautify](https://github.com/Glavin001/atom-beautify) [![GitHub stars](https://img.shields.io/github/stars/Glavin001/atom-beautify?style=flat)](https://github.com/Glavin001/atom-beautify/stargazers) - Beautify HTML (including Handlebars), CSS (including Sass and Less), JavaScript, and much more in Atom.
* [file-icons](https://github.com/DanBrooker/file-icons) [![GitHub stars](https://img.shields.io/github/stars/DanBrooker/file-icons?style=flat)](https://github.com/DanBrooker/file-icons/stargazers) - Adds file specific icons to atom for improved visual grepping.
* [highlight-selected](https://github.com/richrace/highlight-selected) [![GitHub stars](https://img.shields.io/github/stars/richrace/highlight-selected?style=flat)](https://github.com/richrace/highlight-selected/stargazers) - Double click on a word to highlight it throughout the open file.
* [minimap](https://github.com/atom-minimap/minimap) [![GitHub stars](https://img.shields.io/github/stars/atom-minimap/minimap?style=flat)](https://github.com/atom-minimap/minimap/stargazers) - A graphical map (preview) of the full source code.
* [minimap-git-diff](https://github.com/atom-minimap/minimap-git-diff) [![GitHub stars](https://img.shields.io/github/stars/atom-minimap/minimap-git-diff?style=flat)](https://github.com/atom-minimap/minimap-git-diff/stargazers) - A minimap binding for the Atom git-diff package.
* [minimap-highlight-selected](https://github.com/atom-minimap/minimap-highlight-selected) [![GitHub stars](https://img.shields.io/github/stars/atom-minimap/minimap-highlight-selected?style=flat)](https://github.com/atom-minimap/minimap-highlight-selected/stargazers) - A minimap binding for the highlight-selected package.
* [atom-project-manager](https://github.com/danielbrodin/atom-project-manager) [![GitHub stars](https://img.shields.io/github/stars/danielbrodin/atom-project-manager?style=flat)](https://github.com/danielbrodin/atom-project-manager/stargazers) - Get easy access to all your projects and manage them with project specific settings and options.
* [atom-tree-view-git-status](https://github.com/subesokun/atom-tree-view-git-status) [![GitHub stars](https://img.shields.io/github/stars/subesokun/atom-tree-view-git-status?style=flat)](https://github.com/subesokun/atom-tree-view-git-status/stargazers) - Show the Git repository status in the Atom tree-view.
* [atom-pigments](https://github.com/abe33/atom-pigments) [![GitHub stars](https://img.shields.io/github/stars/abe33/atom-pigments?style=flat)](https://github.com/abe33/atom-pigments/stargazers) - An Atom package to display colors in project and files.

### Vim

* [Completor](https://github.com/maralla/completor.vim) [![GitHub stars](https://img.shields.io/github/stars/maralla/completor.vim?style=flat)](https://github.com/maralla/completor.vim/stargazers) - async autocomplete with support for omni and semantic completion.
* [Powerline](https://github.com/Lokaltog/powerline) [![GitHub stars](https://img.shields.io/github/stars/Lokaltog/powerline?style=flat)](https://github.com/Lokaltog/powerline/stargazers) - improved status bar for your buffers.
* [snipmate](https://github.com/garbas/vim-snipmate) [![GitHub stars](https://img.shields.io/github/stars/garbas/vim-snipmate?style=flat)](https://github.com/garbas/vim-snipmate/stargazers) - textual snippets compatiable with Textmate snippets.
* [The Ultimate Vim Distribution](http://vim.spf13.com/) - spf13-vim is a distribution of vim plugins and resources for Vim, GVim and MacVim.

### Sublime Text 3

* [AdvancedNewFile](https://github.com/skuroda/Sublime-AdvancedNewFile) [![GitHub stars](https://img.shields.io/github/stars/skuroda/Sublime-AdvancedNewFile?style=flat)](https://github.com/skuroda/Sublime-AdvancedNewFile/stargazers) - File creation plugin.
* [Emmet](https://github.com/sergeche/emmet-sublime) [![GitHub stars](https://img.shields.io/github/stars/sergeche/emmet-sublime?style=flat)](https://github.com/sergeche/emmet-sublime/stargazers)
* [Git Gutter](https://github.com/jisaacks/GitGutter) [![GitHub stars](https://img.shields.io/github/stars/jisaacks/GitGutter?style=flat)](https://github.com/jisaacks/GitGutter/stargazers) - display changed/added lines in the margin of the editor window.
* [jsFormat](https://github.com/jdc0589/JsFormat) [![GitHub stars](https://img.shields.io/github/stars/jdc0589/JsFormat?style=flat)](https://github.com/jdc0589/JsFormat/stargazers) - Javascript formatting.
* [LiveReload](https://github.com/dz0ny/LiveReload-sublimetext2) [![GitHub stars](https://img.shields.io/github/stars/dz0ny/LiveReload-sublimetext2?style=flat)](https://github.com/dz0ny/LiveReload-sublimetext2/stargazers) - LiveReload plugin.
* [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) [![GitHub stars](https://img.shields.io/github/stars/SublimeText-Markdown/MarkdownEditing?style=flat)](https://github.com/SublimeText-Markdown/MarkdownEditing/stargazers) - Markdown syntax understanding and good color schemes.
* [Package Control](https://sublime.wbond.net/installation) - The Sublime Text package manager.
* [RubyTest](https://github.com/maltize/sublime-text-2-ruby-tests) [![GitHub stars](https://img.shields.io/github/stars/maltize/sublime-text-2-ruby-tests?style=flat)](https://github.com/maltize/sublime-text-2-ruby-tests/stargazers) - Plugin for running Ruby tests.
* [Side Bar Enhancments](https://github.com/titoBouzout/SideBarEnhancements) [![GitHub stars](https://img.shields.io/github/stars/titoBouzout/SideBarEnhancements?style=flat)](https://github.com/titoBouzout/SideBarEnhancements/stargazers) - Enhancements to Sublime Text sidebar. Files and folders.
* [Sublime Git](https://github.com/kemayo/sublime-text-git) [![GitHub stars](https://img.shields.io/github/stars/kemayo/sublime-text-git?style=flat)](https://github.com/kemayo/sublime-text-git/stargazers) - Git Integration for Sublime.
* [Sublime Linter](https://github.com/SublimeLinter/SublimeLinter3/) [![GitHub stars](https://img.shields.io/github/stars/SublimeLinter/SublimeLinter3/?style=flat)](https://github.com/SublimeLinter/SublimeLinter3//stargazers) - Interactive code linting.
* [TrailingSpaces](https://github.com/SublimeText/TrailingSpaces) [![GitHub stars](https://img.shields.io/github/stars/SublimeText/TrailingSpaces?style=flat)](https://github.com/SublimeText/TrailingSpaces/stargazers) - Highlight trailing spaces and delete them in a flash.

### Intellij

* [keymap](https://github.com/jondot/keymaps/) [![GitHub stars](https://img.shields.io/github/stars/jondot/keymaps/?style=flat)](https://github.com/jondot/keymaps//stargazers) - a hybrid Vim/ReSharper/Intellij keymap

### Visual Studio Code

* [Dev Git Repo](https://github.com/Microsoft/vscode) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/vscode?style=flat)](https://github.com/Microsoft/vscode/stargazers) - Github code repository for VS Code 
* [Monaco Editor Git Repo](https://github.com/microsoft/monaco-editor) [![GitHub stars](https://img.shields.io/github/stars/microsoft/monaco-editor?style=flat)](https://github.com/microsoft/monaco-editor/stargazers) - Github code repository for underlying browser-based editor

#### Extensions
* [VS Code Extension Marketplace](https://marketplace.visualstudio.com/search?target=VSCode&category=All%20categories) - Official website for extensions
* [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Official Python extension
* [Sync settings](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) - Excellent extension for settings and extension sync of your VS code setup

## Git
*Tools and addons for making an awesome Git experience*

* [awesome-github](https://github.com/fffaraz/awesome-github) [![GitHub stars](https://img.shields.io/github/stars/fffaraz/awesome-github?style=flat)](https://github.com/fffaraz/awesome-github/stargazers) - Faraz Fallahi maintains a curated list of GitHub & Git resources.
* [gh](https://github.com/jingweno/gh) [![GitHub stars](https://img.shields.io/github/stars/jingweno/gh?style=flat)](https://github.com/jingweno/gh/stargazers) - Fast GitHub command line client (hub port to Go)
* [git-extra-commands](https://github.com/unixorn/git-extra-commands) [![GitHub stars](https://img.shields.io/github/stars/unixorn/git-extra-commands?style=flat)](https://github.com/unixorn/git-extra-commands/stargazers) - collected git helper scripts
* [git-extras](https://github.com/visionmedia/git-extras) [![GitHub stars](https://img.shields.io/github/stars/visionmedia/git-extras?style=flat)](https://github.com/visionmedia/git-extras/stargazers) - GIT utilities -- repo summary, repl, changelog population, author commit percentages and more
* [git-it-on](https://github.com/peterhurford/git-it-on.zsh) [![GitHub stars](https://img.shields.io/github/stars/peterhurford/git-it-on.zsh?style=flat)](https://github.com/peterhurford/git-it-on.zsh/stargazers) - ZSH plugin, adds a gitit command that opens the current directory on github in your current branch
* [git-secret](https://github.com/sobolevn/git-secret) [![GitHub stars](https://img.shields.io/github/stars/sobolevn/git-secret?style=flat)](https://github.com/sobolevn/git-secret/stargazers) - A bash-tool to store your private data inside a git repository.
* [git-semver](https://github.com/markchalloner/git-semver) [![GitHub stars](https://img.shields.io/github/stars/markchalloner/git-semver?style=flat)](https://github.com/markchalloner/git-semver/stargazers) - A git plugin to make Semantic Versioning 2.0.0 and Change Log management easier.
* [git-sweep](https://github.com/arc90/git-sweep) [![GitHub stars](https://img.shields.io/github/stars/arc90/git-sweep?style=flat)](https://github.com/arc90/git-sweep/stargazers) - safely removes branches that have been merged into the master
* [git-up](https://github.com/aanand/git-up) [![GitHub stars](https://img.shields.io/github/stars/aanand/git-up?style=flat)](https://github.com/aanand/git-up/stargazers) - a better 'git pull'
* [hub](https://hub.github.com/) - git CLI wrapper which makes working with GitHub easier
* [scm_breeze](https://github.com/ndbroadbent/scm_breeze) [![GitHub stars](https://img.shields.io/github/stars/ndbroadbent/scm_breeze?style=flat)](https://github.com/ndbroadbent/scm_breeze/stargazers) Streamline your git workflow
* [tig](http://jonas.nitro.dk/tig/) - an ncurses-based text-mode interface for git

## Misc
*Useful tools that cannot find a home in other categories*

* [Fenix Web Server](https://fenixwebserver.com) - A multi-host local static web server with push-button sharing (desktop app).
* [ML Workspace](hhttps://github.com/ml-tooling/ml-workspace) - All-in-one web-based development environment for machine learning and data science.
* [Mockoon](https://mockoon.com) - an API / HTTP REST mocking desktop application
* [HTTP Toolkit](https://httptoolkit.tech) - an HTTP inspection & debugging desktop application

## Notifications
*Tools that notify developers about changes in their work environment*

* [CatLight](https://catlight.io) - status notifier for developers. Checks the status of continuous delivery builds and shows desktop notifications.

## Orchestration
*Tools for orchestrating awesome development environments*

* [azk](https://github.com/azukiapp/azk) [![GitHub stars](https://img.shields.io/github/stars/azukiapp/azk?style=flat)](https://github.com/azukiapp/azk/stargazers) - a lightweight open source engine to orchestrate development environments
* [Nanobox](https://github.com/nanobox-io/nanobox) [![GitHub stars](https://img.shields.io/github/stars/nanobox-io/nanobox?style=flat)](https://github.com/nanobox-io/nanobox/stargazers) - A micro-PaaS (μPaaS) for creating consistent, isolated, development environments deployable anywhere https://nanobox.io.

## Presentation
*Tools for presenting your work*

* [bespoke.js](https://github.com/markdalgleish/bespoke.js) [![GitHub stars](https://img.shields.io/github/stars/markdalgleish/bespoke.js?style=flat)](https://github.com/markdalgleish/bespoke.js/stargazers) - DIY Presentation Micro-Framework
* [hacker-slides](https://github.com/msoedov/hacker-slides) [![GitHub stars](https://img.shields.io/github/stars/msoedov/hacker-slides?style=flat)](https://github.com/msoedov/hacker-slides/stargazers) - Reveal.js based presentation tool
* [impress.js](https://github.com/impress/impress.js) [![GitHub stars](https://img.shields.io/github/stars/impress/impress.js?style=flat)](https://github.com/impress/impress.js/stargazers) - presentation framework based on the power of CSS3 transforms and transitions
* [mithril-slides](https://github.com/wulab/mithril-slides) [![GitHub stars](https://img.shields.io/github/stars/wulab/mithril-slides?style=flat)](https://github.com/wulab/mithril-slides/stargazers) - A Keynote-inspired presentation app written with Mithril
* [remark](https://github.com/gnab/remark) [![GitHub stars](https://img.shields.io/github/stars/gnab/remark?style=flat)](https://github.com/gnab/remark/stargazers) - markdown based presentation on your browser
* [reveal.js](https://github.com/hakimel/reveal.js/) [![GitHub stars](https://img.shields.io/github/stars/hakimel/reveal.js/?style=flat)](https://github.com/hakimel/reveal.js//stargazers) - markdown based presentation on your browser
* [deck.js](https://github.com/imakewebthings/deck.js) [![GitHub stars](https://img.shields.io/github/stars/imakewebthings/deck.js?style=flat)](https://github.com/imakewebthings/deck.js/stargazers) - markdown based presentation on your browser
* [vimdeck](https://github.com/tybenz/vimdeck) [![GitHub stars](https://img.shields.io/github/stars/tybenz/vimdeck?style=flat)](https://github.com/tybenz/vimdeck/stargazers) - present inside your Vim
* [WebSlides](https://github.com/jlantunez/webslides) [![GitHub stars](https://img.shields.io/github/stars/jlantunez/webslides?style=flat)](https://github.com/jlantunez/webslides/stargazers) - Making HTML presentations easy

## Shell
*Tools for having an awesome shell environment*

* [awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins) [![GitHub stars](https://img.shields.io/github/stars/unixorn/awesome-zsh-plugins?style=flat)](https://github.com/unixorn/awesome-zsh-plugins/stargazers) - List of zsh plugins usable with [zgen](https://github.com/tarjoilija/zgen) [![GitHub stars](https://img.shields.io/github/stars/tarjoilija/zgen?style=flat)](https://github.com/tarjoilija/zgen/stargazers) and other [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/) [![GitHub stars](https://img.shields.io/github/stars/robbyrussell/oh-my-zsh/?style=flat)](https://github.com/robbyrussell/oh-my-zsh//stargazers) compatible zsh frameworks
* [fish-shell](https://github.com/fish-shell/fish-shell) [![GitHub stars](https://img.shields.io/github/stars/fish-shell/fish-shell?style=flat)](https://github.com/fish-shell/fish-shell/stargazers) - The user-friendly command line shell
* [hss](https://github.com/six-ddc/hss) [![GitHub stars](https://img.shields.io/github/stars/six-ddc/hss?style=flat)](https://github.com/six-ddc/hss/stargazers) - Never type the annoying ssh commands again.
* [oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) [![GitHub stars](https://img.shields.io/github/stars/oh-my-fish/oh-my-fish?style=flat)](https://github.com/oh-my-fish/oh-my-fish/stargazers) - Framework for managing your fish shell configuration inspired by oh-my-zsh.
* [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/) [![GitHub stars](https://img.shields.io/github/stars/robbyrussell/oh-my-zsh/?style=flat)](https://github.com/robbyrussell/oh-my-zsh//stargazers) - A community driven framework for managing zsh configuration.
* [zgen](https://github.com/tarjoilija/zgen) [![GitHub stars](https://img.shields.io/github/stars/tarjoilija/zgen?style=flat)](https://github.com/tarjoilija/zgen/stargazers) - Faster framework for managing your zsh configuration, backward compatible with oh-my-zsh plugins
* [zsh](http://www.zsh.org/) - A shell designed for interactive use, although it is also a powerful scripting language.
* [shellcheck](https://github.com/koalaman/shellcheck) [![GitHub stars](https://img.shields.io/github/stars/koalaman/shellcheck?style=flat)](https://github.com/koalaman/shellcheck/stargazers) - Lint for shell. Will find deprecated and/or dangerous usage in shell scripts
* [zsh quickstart kit](https://github.com/unixorn/zsh-quickstart-kit) [![GitHub stars](https://img.shields.io/github/stars/unixorn/zsh-quickstart-kit?style=flat)](https://github.com/unixorn/zsh-quickstart-kit/stargazers) - Quick intro for getting set up with zsh and zgen

## Text
*Tools for working with text files - search, replace, processing*

* [ack](https://github.com/petdance/ack2) [![GitHub stars](https://img.shields.io/github/stars/petdance/ack2?style=flat)](https://github.com/petdance/ack2/stargazers) - the Perl based
  better-than-grep tool.
* [ag](https://github.com/ggreer/the_silver_searcher) [![GitHub stars](https://img.shields.io/github/stars/ggreer/the_silver_searcher?style=flat)](https://github.com/ggreer/the_silver_searcher/stargazers) - A C based code-searching tool similar to ack, but faster
* [peco](https://github.com/peco/peco) [![GitHub stars](https://img.shields.io/github/stars/peco/peco?style=flat)](https://github.com/peco/peco/stargazers) - interactive filtering, like interactive Grep
* [ripgrep](https://github.com/BurntSushi/ripgrep) [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/ripgrep?style=flat)](https://github.com/BurntSushi/ripgrep/stargazers) - Faster than grep, written in Rust


## Terminal
*Tools and addons for terminal and terminal work*

* [autojump](https://github.com/joelthelion/autojump) [![GitHub stars](https://img.shields.io/github/stars/joelthelion/autojump?style=flat)](https://github.com/joelthelion/autojump/stargazers) - remembers your
  folders and jump to them based on partial recall (e.g. `j proj` will jump
to `/home/Users/yourself/projects`.
* [fasd](https://github.com/clvv/fasd) [![GitHub stars](https://img.shields.io/github/stars/clvv/fasd?style=flat)](https://github.com/clvv/fasd/stargazers) Command-line productivity booster, offers quick access to files and directories.
* [freshenv](https://github.com/raiyanyahya/freshenv) [![GitHub stars](https://img.shields.io/github/stars/raiyanyahya/freshenv?style=flat)](https://github.com/raiyanyahya/freshenv/stargazers) - Provision, share, manage local and cloud developer environments.
* [homebrew](http://brew.sh) - Makes it easy to install open source packages on an `OS X` system with a single command.
* [hss](https://github.com/six-ddc/hss) [![GitHub stars](https://img.shields.io/github/stars/six-ddc/hss?style=flat)](https://github.com/six-ddc/hss/stargazers) - Never type the annoying ssh commands again.
* [httpie](http://httpie.org/) A command line HTTP client, a user-friendly cURL replacement.
* [iTerm2](http://www.iterm2.com/) - a great terminal replacement `/OSX/`
* [jq](https://stedolan.github.io/jq/) - a lightweight and flexible command-line JSON processor
* [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) [![GitHub stars](https://img.shields.io/github/stars/robbyrussell/oh-my-zsh?style=flat)](https://github.com/robbyrussell/oh-my-zsh/stargazers) - the
  incredible ZSH addon.
* [Pipe Viewer](http://www.ivarch.com/programs/pv.shtml) - a tool for monitoring the progress of data through a pipeline
* [tmux](https://tmux.github.io/) the awesome terminal multiplexer.
* [zoxide](https://github.com/ajeetdsouza/zoxide) [![GitHub stars](https://img.shields.io/github/stars/ajeetdsouza/zoxide?style=flat)](https://github.com/ajeetdsouza/zoxide/stargazers) - A better way to navigate your filesystem. Written in Rust, cross-shell, and much faster than other autojumpers.


## Workflow
*Tools and addons which improve your daily workflow with code*

* [fswatch](https://github.com/alandipert/fswatch) [![GitHub stars](https://img.shields.io/github/stars/alandipert/fswatch?style=flat)](https://github.com/alandipert/fswatch/stargazers) - a watch tool which
  will emit FS events and you can run commands on demand with. Note -
`fswatch-run` too.
* [guard](https://github.com/guard/guard) [![GitHub stars](https://img.shields.io/github/stars/guard/guard?style=flat)](https://github.com/guard/guard/stargazers) - FS watch tool with a huge ecosystem of plugins
* [just](https://github/casey/just) - A task runner for conveniently saving and running project-specific commands. Similar to make, but much nicer
* [LiveReload](http://livereload.com/) - FS watch and preprocessor as a desktop app for `/OSX/` and `/WIN/` with complementary browser extensions
  * [guard-livereload](https://github.com/guard/guard-livereload) [![GitHub stars](https://img.shields.io/github/stars/guard/guard-livereload?style=flat)](https://github.com/guard/guard-livereload/stargazers) - Guard plugin compatible with LiveReload's browser extensions
  * [simplehttp](https://github.com/snwfdhmp/simplehttp) [![GitHub stars](https://img.shields.io/github/stars/snwfdhmp/simplehttp?style=flat)](https://github.com/snwfdhmp/simplehttp/stargazers) Fastest and simplest way to start serving a local directory over http.
* [watchman](https://github.com/facebook/watchman) [![GitHub stars](https://img.shields.io/github/stars/facebook/watchman?style=flat)](https://github.com/facebook/watchman/stargazers) - Facebook's better
  `watch` - note it works as a service.
* [Zappr](https://github.com/zalando/zappr) [![GitHub stars](https://img.shields.io/github/stars/zalando/zappr?style=flat)](https://github.com/zalando/zappr/stargazers) - GitHub integration built to enhance your project workflow via enable/disable pull request approval checks.
* [ergo](https://github.com/cristianoliveira/ergo) [![GitHub stars](https://img.shields.io/github/stars/cristianoliveira/ergo?style=flat)](https://github.com/cristianoliveira/ergo/stargazers) - The management of multiple local services running over different ports made easy.
* [Prodmodel](https://github.com/prodmodel/prodmodel) [![GitHub stars](https://img.shields.io/github/stars/prodmodel/prodmodel?style=flat)](https://github.com/prodmodel/prodmodel/stargazers) - Build tool for data science pipelines.
* [Gebug](https://github.com/moshebe/gebug) [![GitHub stars](https://img.shields.io/github/stars/moshebe/gebug?style=flat)](https://github.com/moshebe/gebug/stargazers) - A tool that makes debugging of Dockerized Go applications super easy by enabling Debugger and Hot-Reload features, seamlessly.
