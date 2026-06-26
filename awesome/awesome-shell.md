# Shell

[![GitHub stars](https://img.shields.io/github/stars/alebcay/awesome-shell?style=flat)](https://github.com/alebcay/awesome-shell/stargazers)

```
 █████╗ ██╗    ██╗███████╗███████╗ ██████╗ ███╗   ███╗███████╗
██╔══██╗██║    ██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔════╝
███████║██║ █╗ ██║█████╗  ███████╗██║   ██║██╔████╔██║█████╗
██╔══██║██║███╗██║██╔══╝  ╚════██║██║   ██║██║╚██╔╝██║██╔══╝
██║  ██║╚███╔███╔╝███████╗███████║╚██████╔╝██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
███████╗██╗  ██╗███████╗██╗     ██╗
██╔════╝██║  ██║██╔════╝██║     ██║
███████╗███████║█████╗  ██║     ██║
╚════██║██╔══██║██╔══╝  ██║     ██║
███████║██║  ██║███████╗███████╗███████╗
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
```

# Awesome Shell [![Awesome][awesome-badge]][awesome-link]

A curated list of awesome command-line frameworks, toolkits, guides and gizmos. Inspired by awesome-php. This awesome collection is also available on [Unix-Shell.ZEEF.com](https://unix-shell.zeef.com/caleb.xu).
- [Shells](#shells)
- [Command-Line Productivity](#command-line-productivity)
  - [Directory Navigation](#directory-navigation)
- [Customization](#customization)
- [For Developers](#for-developers)
- [System Utilities](#system-utilities)
- [Downloading and Serving](#downloading-and-serving)
- [Multimedia and File Formats](#multimedia-and-file-formats)
- [Applications](#applications)
- [Games](#games)
- [Shell Package Management](#shell-package-management)
- [Shell Script Development](#shell-script-development)
- [Guides](#guides)
- [**Awesome Zsh**][awesome-zsh]&nbsp; [![Awesome][awesome-badge]][awesome-zsh]
- [**Awesome Fish**][awesome-fish] [![Awesome][awesome-badge]][awesome-fish]
- [**Awesome Bash**][awesome-bash] [![Awesome][awesome-badge]][awesome-bash]
- [Other Awesome Lists](#other-awesome-lists)

## Shells

*Choose your base shell.*

* [bash](https://www.gnu.org/software/bash/) - GNU Project's shell (Bourne Again SHell)
* [elvish](https://elv.sh/) - Friendly, expressive shell features like anonymous functions and data structures
* [es](https://wryun.github.io/es-shell/) - The extensible shell, based on Plan 9's [rc](https://github.com/rakitzis/rc) [![GitHub stars](https://img.shields.io/github/stars/rakitzis/rc?style=flat)](https://github.com/rakitzis/rc/stargazers) shell
* [fish](https://fishshell.com) - Smart and user-friendly command line shell
* [ion](https://github.com/redox-os/ion) [![GitHub stars](https://img.shields.io/github/stars/redox-os/ion?style=flat)](https://github.com/redox-os/ion/stargazers) - A modern system shell that features a simple, yet powerful, syntax. It is written entirely in Rust.
* [ksh93](https://github.com/att/ast) [![GitHub stars](https://img.shields.io/github/stars/att/ast?style=flat)](https://github.com/att/ast/stargazers) - Korn Shell
* [mksh](https://github.com/MirBSD/mksh) [![GitHub stars](https://img.shields.io/github/stars/MirBSD/mksh?style=flat)](https://github.com/MirBSD/mksh/stargazers) - MirBSD Korn Shell
* [murex](https://github.com/lmorg/murex) [![GitHub stars](https://img.shields.io/github/stars/lmorg/murex?style=flat)](https://github.com/lmorg/murex/stargazers) - A smarter shell and scripting environment with advanced features designed for usability, safety and productivity (eg smarter DevOps tooling)
* [ngs](https://github.com/ngs-lang/ngs) [![GitHub stars](https://img.shields.io/github/stars/ngs-lang/ngs?style=flat)](https://github.com/ngs-lang/ngs/stargazers) - Fully featured scripting language created specifically for Ops. REPL is being developed.
* [nushell](https://github.com/nushell/nushell) [![GitHub stars](https://img.shields.io/github/stars/nushell/nushell?style=flat)](https://github.com/nushell/nushell/stargazers) - A modern shell written in Rust
* [oksh](https://github.com/ibara/oksh) [![GitHub stars](https://img.shields.io/github/stars/ibara/oksh?style=flat)](https://github.com/ibara/oksh/stargazers) - Portable OpenBSD ksh
* [osh](https://www.oilshell.org) - Bash compatible, with new/modern Unix shell language called Oil
* [pdksh](https://cvsweb.openbsd.org/cgi-bin/cvsweb/src/bin/ksh/) - Public domain Korn shell
* [powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview) a cross-platform task automation and configuration management framework, consisting of a command-line shell and scripting language
* [shell++](https://github.com/alexst07/shell-plus-plus) [![GitHub stars](https://img.shields.io/github/stars/alexst07/shell-plus-plus?style=flat)](https://github.com/alexst07/shell-plus-plus/stargazers) - Friendly and modern functional and object oriented shell script language
* [shenv](https://github.com/shenv/shenv) [![GitHub stars](https://img.shields.io/github/stars/shenv/shenv?style=flat)](https://github.com/shenv/shenv/stargazers) - Simple shell version management
* [tcsh](https://www.tcsh.org/) - C shell with file name completion and command line editing
* [xonsh](https://xon.sh) - Python-ish, BASHwards-looking shell language and command prompt
* [yash](https://github.com/magicant/yash) [![GitHub stars](https://img.shields.io/github/stars/magicant/yash?style=flat)](https://github.com/magicant/yash/stargazers) - A POSIX-compliant command line shell with built-in support for completion and prediction based on command history
* [zsh](https://www.zsh.org) - Powerful shell with scripting language

## Command-Line Productivity

*Search, bookmarks, multiplexing, and other tools that make your terminal experience more productive.*

* [AdvancedNewFile](https://github.com/tanrax/terminal-AdvancedNewFile) [![GitHub stars](https://img.shields.io/github/stars/tanrax/terminal-AdvancedNewFile?style=flat)](https://github.com/tanrax/terminal-AdvancedNewFile/stargazers) - Fast creation of files and directories in a recursive way. Inspired by the Vim plugin.
* [ag](https://github.com/ggreer/the_silver_searcher) [![GitHub stars](https://img.shields.io/github/stars/ggreer/the_silver_searcher?style=flat)](https://github.com/ggreer/the_silver_searcher/stargazers) - Super fast string search through a directory hierarchy
* [aliases](https://github.com/sebglazebrook/aliases) [![GitHub stars](https://img.shields.io/github/stars/sebglazebrook/aliases?style=flat)](https://github.com/sebglazebrook/aliases/stargazers) - Contextual, dynamic, organized aliases for bash
* [arttime](https://github.com/reportaman/arttime) [![GitHub stars](https://img.shields.io/github/stars/reportaman/arttime?style=flat)](https://github.com/reportaman/arttime/stargazers) - Beauty of text art meets functionality of clock, timer, pomodoro++ time manager
* [autoenv](https://github.com/hyperupcall/autoenv) [![GitHub stars](https://img.shields.io/github/stars/hyperupcall/autoenv?style=flat)](https://github.com/hyperupcall/autoenv/stargazers) - Directory-based environments.
* [await](https://github.com/slavaGanzin/await) [![GitHub stars](https://img.shields.io/github/stars/slavaGanzin/await?style=flat)](https://github.com/slavaGanzin/await/stargazers) - single binary that run list of commands in parallel and waits for their termination
* [bartib](https://github.com/nikolassv/bartib) [![GitHub stars](https://img.shields.io/github/stars/nikolassv/bartib?style=flat)](https://github.com/nikolassv/bartib/stargazers) - A simple timetracker for the command line. It saves a log of all tracked activities as a plaintext file and allows you to create flexible reports.
* [bashhub](https://github.com/rcaloras/bashhub-client) [![GitHub stars](https://img.shields.io/github/stars/rcaloras/bashhub-client?style=flat)](https://github.com/rcaloras/bashhub-client/stargazers) - :cloud: Bash history in the cloud. Indexed and searchable.
* [boilr](https://github.com/tmrts/boilr) [![GitHub stars](https://img.shields.io/github/stars/tmrts/boilr?style=flat)](https://github.com/tmrts/boilr/stargazers) - A blazingly fast CLI tool for creating projects from boilerplate templates.
* [boom](https://github.com/holman/boom) [![GitHub stars](https://img.shields.io/github/stars/holman/boom?style=flat)](https://github.com/holman/boom/stargazers) - Store links and snippets in the command line
* [borg](https://github.com/ok-borg/borg) [![GitHub stars](https://img.shields.io/github/stars/ok-borg/borg?style=flat)](https://github.com/ok-borg/borg/stargazers) - A terminal based search engine for bash commands
* [broot](https://github.com/Canop/broot) [![GitHub stars](https://img.shields.io/github/stars/Canop/broot?style=flat)](https://github.com/Canop/broot/stargazers) - A better way to navigate directories
* [browsh](https://github.com/browsh-org/browsh) [![GitHub stars](https://img.shields.io/github/stars/browsh-org/browsh?style=flat)](https://github.com/browsh-org/browsh/stargazers) - The modern text-based browser
* [Buku](https://github.com/jarun/Buku) [![GitHub stars](https://img.shields.io/github/stars/jarun/Buku?style=flat)](https://github.com/jarun/Buku/stargazers) - Powerful command-line bookmark manager
* [byobu](https://www.byobu.org) - Text-based window manager and terminal multiplexer
* [cod](https://github.com/dim-an/cod) [![GitHub stars](https://img.shields.io/github/stars/dim-an/cod?style=flat)](https://github.com/dim-an/cod/stargazers) — A completion daemon for shell that learns when you invoke `--help` commands
* [CloudClip](https://github.com/skywind3000/CloudClip) [![GitHub stars](https://img.shields.io/github/stars/skywind3000/CloudClip?style=flat)](https://github.com/skywind3000/CloudClip/stargazers) - Your own clipboard in the cloud, copy and paste text with gist between different systems
* [ddgr](https://github.com/jarun/ddgr) [![GitHub stars](https://img.shields.io/github/stars/jarun/ddgr?style=flat)](https://github.com/jarun/ddgr/stargazers) - DuckDuckGo from the terminal
* [desk](https://github.com/jamesob/desk) [![GitHub stars](https://img.shields.io/github/stars/jamesob/desk?style=flat)](https://github.com/jamesob/desk/stargazers) - A lightweight workspace manager for the shell
* [direnv](https://github.com/direnv/direnv) [![GitHub stars](https://img.shields.io/github/stars/direnv/direnv?style=flat)](https://github.com/direnv/direnv/stargazers) - An environment switcher for the shell, compare with autoenv
* [dnote](https://github.com/dnote/dnote) [![GitHub stars](https://img.shields.io/github/stars/dnote/dnote?style=flat)](https://github.com/dnote/dnote/stargazers) - A simple command line notebook with multi-device sync and web interface
* [eureka](https://github.com/simeg/eureka/) [![GitHub stars](https://img.shields.io/github/stars/simeg/eureka/?style=flat)](https://github.com/simeg/eureka//stargazers) - :bulb: CLI tool to input and store your ideas without leaving the terminal
* [fasd](https://github.com/clvv/fasd) [![GitHub stars](https://img.shields.io/github/stars/clvv/fasd?style=flat)](https://github.com/clvv/fasd/stargazers) - Command-line productivity booster, offers quick access to files and directories
* [fd](https://github.com/sharkdp/fd) [![GitHub stars](https://img.shields.io/github/stars/sharkdp/fd?style=flat)](https://github.com/sharkdp/fd/stargazers) - A simple, fast and user-friendly alternative to find.
* [foxy](https://github.com/s-p-k/foxy) [![GitHub stars](https://img.shields.io/github/stars/s-p-k/foxy?style=flat)](https://github.com/s-p-k/foxy/stargazers) - Plain text bookmarks for Firefox and surf browsers.
* [fselect](https://github.com/jhspetersson/fselect) [![GitHub stars](https://img.shields.io/github/stars/jhspetersson/fselect?style=flat)](https://github.com/jhspetersson/fselect/stargazers) - Find files with SQL-like queries.
* [funky](https://github.com/bbugyi200/funky) [![GitHub stars](https://img.shields.io/github/stars/bbugyi200/funky?style=flat)](https://github.com/bbugyi200/funky/stargazers) - Extends functionality of shell functions making them more powerful and flexible.
* [fz](https://github.com/changyuheng/fz) [![GitHub stars](https://img.shields.io/github/stars/changyuheng/fz?style=flat)](https://github.com/changyuheng/fz/stargazers) - Seamless fuzzy tab completion for z
* [fzf](https://github.com/junegunn/fzf) [![GitHub stars](https://img.shields.io/github/stars/junegunn/fzf?style=flat)](https://github.com/junegunn/fzf/stargazers) - A command-line fuzzy finder
* [gitmux](https://github.com/arl/gitmux) [![GitHub stars](https://img.shields.io/github/stars/arl/gitmux?style=flat)](https://github.com/arl/gitmux/stargazers) - Show Git status in Tmux status bar
* [googler](https://github.com/jarun/googler) [![GitHub stars](https://img.shields.io/github/stars/jarun/googler?style=flat)](https://github.com/jarun/googler/stargazers) - Google Search, Google Site Search, Google News from the terminal
* [googlr](https://github.com/Astranno/googlr) [![GitHub stars](https://img.shields.io/github/stars/Astranno/googlr?style=flat)](https://github.com/Astranno/googlr/stargazers) - Command line tool that lets you search Google from your terminal.
* [has](https://github.com/kdabir/has) [![GitHub stars](https://img.shields.io/github/stars/kdabir/has?style=flat)](https://github.com/kdabir/has/stargazers) - `has` helps you check presence of various command line tools and their versions on path
* [how2](https://github.com/santinic/how2) [![GitHub stars](https://img.shields.io/github/stars/santinic/how2?style=flat)](https://github.com/santinic/how2/stargazers) - `how2` finds the simplest way to do something in a unix shell. It's like `man`, but you can query it in natural language.
* [navi](https://github.com/denisidoro/navi) [![GitHub stars](https://img.shields.io/github/stars/denisidoro/navi?style=flat)](https://github.com/denisidoro/navi/stargazers) - An interactive cheatsheet tool for the command-line
* [hhighlighter](https://github.com/paoloantinori/hhighlighter) [![GitHub stars](https://img.shields.io/github/stars/paoloantinori/hhighlighter?style=flat)](https://github.com/paoloantinori/hhighlighter/stargazers) - Colorize words in a command output
* [hr](https://github.com/LuRsT/hr) [![GitHub stars](https://img.shields.io/github/stars/LuRsT/hr?style=flat)](https://github.com/LuRsT/hr/stargazers) - `<hr />` for your terminal
* [hss](https://github.com/six-ddc/hss) [![GitHub stars](https://img.shields.io/github/stars/six-ddc/hss?style=flat)](https://github.com/six-ddc/hss/stargazers) - An interactive parallel ssh client featuring autocomplete and asynchronous execution
* [hstr](https://github.com/dvorka/hstr) [![GitHub stars](https://img.shields.io/github/stars/dvorka/hstr?style=flat)](https://github.com/dvorka/hstr/stargazers) - Bash History Suggest Box
* [k](https://github.com/supercrabtree/k) [![GitHub stars](https://img.shields.io/github/stars/supercrabtree/k?style=flat)](https://github.com/supercrabtree/k/stargazers) - k is a Zsh script to make directory listings more readable, adding Git status, fileweight colors and rotting dates
* [k alias](https://github.com/lingtalfi/k) [![GitHub stars](https://img.shields.io/github/stars/lingtalfi/k?style=flat)](https://github.com/lingtalfi/k/stargazers) - get kool aliases (and more) working with a simple one-liner
* [lf](https://github.com/gokcehan/lf) [![GitHub stars](https://img.shields.io/github/stars/gokcehan/lf?style=flat)](https://github.com/gokcehan/lf/stargazers) - Terminal file manager written in Go, inspired by ranger
* [lf.sh](https://github.com/suewonjp/lf.sh) [![GitHub stars](https://img.shields.io/github/stars/suewonjp/lf.sh?style=flat)](https://github.com/suewonjp/lf.sh/stargazers) - Quickly search files with fewer typings and do many more (grepping, copying path to clipboard, etc)
* [lowcharts](https://github.com/juan-leon/lowcharts) [![GitHub stars](https://img.shields.io/github/stars/juan-leon/lowcharts?style=flat)](https://github.com/juan-leon/lowcharts/stargazers) - Draw low-resolution graphs in terminal
* [Lmod](https://lmod.readthedocs.io/en/latest/) - Lua-based Environment Modules that enhances Tcl-based modules while being backward compatible (compare to modules)
* [loop](https://github.com/Miserlou/Loop) [![GitHub stars](https://img.shields.io/github/stars/Miserlou/Loop?style=flat)](https://github.com/Miserlou/Loop/stargazers) - Write and control complex loops with as one-liners
* [marker](https://github.com/pindexis/marker) [![GitHub stars](https://img.shields.io/github/stars/pindexis/marker?style=flat)](https://github.com/pindexis/marker/stargazers) - Bookmark your shell commands
* [mackup](https://github.com/lra/mackup/) [![GitHub stars](https://img.shields.io/github/stars/lra/mackup/?style=flat)](https://github.com/lra/mackup//stargazers) - Keep your application settings in sync (OS X/Linux)
* [mcfly](https://github.com/cantino/mcfly) [![GitHub stars](https://img.shields.io/github/stars/cantino/mcfly?style=flat)](https://github.com/cantino/mcfly/stargazers) - Fly through your shell history. Great Scot!
* [modules](http://modules.sourceforge.net/) - Classical Tcl-based Environment Modules managing the shell environment (compare to Lmod, direnv, and autoenv)
* [nnn](https://github.com/jarun/nnn) [![GitHub stars](https://img.shields.io/github/stars/jarun/nnn?style=flat)](https://github.com/jarun/nnn/stargazers) - File browser and disk usage analyzer with excellent desktop integration
* [ok-sh](https://github.com/secretGeek/ok-bash) [![GitHub stars](https://img.shields.io/github/stars/secretGeek/ok-bash?style=flat)](https://github.com/secretGeek/ok-bash/stargazers) - Do you work on many different projects? And in each project, are there commands you use that are specific to that project? You need a .ok file.
* [parallel](https://www.gnu.org/software/parallel/) - Build and execute shell command lines from standard input in parallel
* [pass](https://www.passwordstore.org/) - Manage passwords from the command line with GPG encryption and optional git integration.
* [pathpicker](https://github.com/facebook/PathPicker) [![GitHub stars](https://img.shields.io/github/stars/facebook/PathPicker?style=flat)](https://github.com/facebook/PathPicker/stargazers) - Accepts inputs like grep, searches, git etc; allows selecting files from the result of the input, which you can then open or provide as argument to a command.
* [pdd](https://github.com/jarun/pdd) [![GitHub stars](https://img.shields.io/github/stars/jarun/pdd?style=flat)](https://github.com/jarun/pdd/stargazers) - Tiny date, time diff calculator with timers
* [percol](https://github.com/mooz/percol) [![GitHub stars](https://img.shields.io/github/stars/mooz/percol?style=flat)](https://github.com/mooz/percol/stargazers) - Adds flavor of interactive filtering to the traditional pipe concept of UNIX shell
* [q](https://github.com/cal2195/q) [![GitHub stars](https://img.shields.io/github/stars/cal2195/q?style=flat)](https://github.com/cal2195/q/stargazers) - Vim like macro registers for your Bash and Zsh Shell
* [qfc](https://github.com/pindexis/qfc) [![GitHub stars](https://img.shields.io/github/stars/pindexis/qfc?style=flat)](https://github.com/pindexis/qfc/stargazers) - File-completion widget for Bash and Zsh
* [resh](https://github.com/curusarn/resh) [![GitHub stars](https://img.shields.io/github/stars/curusarn/resh?style=flat)](https://github.com/curusarn/resh/stargazers) - Contextual shell history for Zsh and Bash
* [rg](https://github.com/BurntSushi/ripgrep) [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/ripgrep?style=flat)](https://github.com/BurntSushi/ripgrep/stargazers) - ripgrep is a line oriented search tool that combines the usability of The Silver Searcher with the raw speed of GNU grep
* [screen](https://www.gnu.org/software/screen/) - GNU terminal multiplexer
* [shell-history](https://github.com/pawamoy/shell-history) [![GitHub stars](https://img.shields.io/github/stars/pawamoy/shell-history?style=flat)](https://github.com/pawamoy/shell-history/stargazers) - Visualize your shell usage with Highcharts
* [SHML](https://github.com/odb/shml) [![GitHub stars](https://img.shields.io/github/stars/odb/shml?style=flat)](https://github.com/odb/shml/stargazers) - Style framework for the terminal (Shell Markup Language)
* [slugify](https://github.com/benlinton/slugify) [![GitHub stars](https://img.shields.io/github/stars/benlinton/slugify?style=flat)](https://github.com/benlinton/slugify/stargazers) - Command that converts filenames and directories to a web friendly format
* [sman](https://github.com/tokozedg/sman) [![GitHub stars](https://img.shields.io/github/stars/tokozedg/sman?style=flat)](https://github.com/tokozedg/sman/stargazers) - :bug: A command-line snippet manager
* [spark](https://github.com/holman/spark) [![GitHub stars](https://img.shields.io/github/stars/holman/spark?style=flat)](https://github.com/holman/spark/stargazers) - ▁▂▃▅▂▇ in your shell
* [spark.fish](https://github.com/jorgebucaran/spark.fish) [![GitHub stars](https://img.shields.io/github/stars/jorgebucaran/spark.fish?style=flat)](https://github.com/jorgebucaran/spark.fish/stargazers) - ▁▂▃▅ Sparkline Generator
* [sheet](https://github.com/oscardelben/sheet) [![GitHub stars](https://img.shields.io/github/stars/oscardelben/sheet?style=flat)](https://github.com/oscardelben/sheet/stargazers) -  Text snippets for the command line
* [spot](https://github.com/rauchg/spot) [![GitHub stars](https://img.shields.io/github/stars/rauchg/spot?style=flat)](https://github.com/rauchg/spot/stargazers) - Tiny file search utility
- [snips](https://github.com/srijanshetty/snips) [![GitHub stars](https://img.shields.io/github/stars/srijanshetty/snips?style=flat)](https://github.com/srijanshetty/snips/stargazers) - Command line tool to manage snippets of code.
* [sqlline](https://github.com/julianhyde/sqlline) [![GitHub stars](https://img.shields.io/github/stars/julianhyde/sqlline?style=flat)](https://github.com/julianhyde/sqlline/stargazers) - Shell for issuing SQL to relational databases via JDBC (multiline, completion, highlighting, dialect support)
* [sshfs](https://github.com/osxfuse/sshfs) [![GitHub stars](https://img.shields.io/github/stars/osxfuse/sshfs?style=flat)](https://github.com/osxfuse/sshfs/stargazers) - A tool for mounting remote file systems over SSH
* [sudocabulary](https://github.com/badarsh2/Sudocabulary) [![GitHub stars](https://img.shields.io/github/stars/badarsh2/Sudocabulary?style=flat)](https://github.com/badarsh2/Sudocabulary/stargazers) - Learn English Vocabulary from your terminal
* [surfraw](https://gitlab.com/surfraw/Surfraw) - browse specific site and search the web from your terminal without browser.
* [task-manager](https://github.com/lingtalfi/task-manager) [![GitHub stars](https://img.shields.io/github/stars/lingtalfi/task-manager?style=flat)](https://github.com/lingtalfi/task-manager/stargazers) - Execute all your scripts with just two or three keystrokes.
* [td-cli](https://github.com/darrikonn/td-cli) [![GitHub stars](https://img.shields.io/github/stars/darrikonn/td-cli?style=flat)](https://github.com/darrikonn/td-cli/stargazers) - A todo command line manager to organize and manage your todos across multiple projects.
* [tere](https://github.com/mgunyho/tere) [![GitHub stars](https://img.shields.io/github/stars/mgunyho/tere?style=flat)](https://github.com/mgunyho/tere/stargazers) - A faster alternative to cd + ls
* [thefuck](https://github.com/nvbn/thefuck) [![GitHub stars](https://img.shields.io/github/stars/nvbn/thefuck?style=flat)](https://github.com/nvbn/thefuck/stargazers) - Fix common shell mistakes by using an easy to remember command
* [tldr](https://github.com/raylee/tldr-sh-client) [![GitHub stars](https://img.shields.io/github/stars/raylee/tldr-sh-client?style=flat)](https://github.com/raylee/tldr-sh-client/stargazers) - A fully-functional bash client for tldr, simplified and community-driven man pages
* [tmux](https://tmux.github.io/) - Amazing terminal multiplexer
* [undollar](https://github.com/xtyrrell/undollar) [![GitHub stars](https://img.shields.io/github/stars/xtyrrell/undollar?style=flat)](https://github.com/xtyrrell/undollar/stargazers) - undollar bites the dollar sign off the tip of the command you just pasted into your terminal
* [usql](https://github.com/xo/usql) [![GitHub stars](https://img.shields.io/github/stars/xo/usql?style=flat)](https://github.com/xo/usql/stargazers) - Universal command-line interface for SQL databases.
* [v](https://github.com/rupa/v) [![GitHub stars](https://img.shields.io/github/stars/rupa/v?style=flat)](https://github.com/rupa/v/stargazers) - z for vim.
* [wemux](https://github.com/zolrath/wemux) [![GitHub stars](https://img.shields.io/github/stars/zolrath/wemux?style=flat)](https://github.com/zolrath/wemux/stargazers) - Multi-User Tmux Made Easy
* [xiki](https://github.com/trogdoro/xiki) [![GitHub stars](https://img.shields.io/github/stars/trogdoro/xiki?style=flat)](https://github.com/trogdoro/xiki/stargazers) - Makes the shell console more friendly and powerful
* [xplr](https://github.com/sayanarijit/xplr) [![GitHub stars](https://img.shields.io/github/stars/sayanarijit/xplr?style=flat)](https://github.com/sayanarijit/xplr/stargazers) -  A hackable, minimal, fast TUI file explorer
* [xsv](https://github.com/BurntSushi/xsv) [![GitHub stars](https://img.shields.io/github/stars/BurntSushi/xsv?style=flat)](https://github.com/BurntSushi/xsv/stargazers) - a fast CSV command line toolkit written in Rust
* [xxh](https://github.com/xxh/xxh) [![GitHub stars](https://img.shields.io/github/stars/xxh/xxh?style=flat)](https://github.com/xxh/xxh/stargazers) - Bring your favorite shell wherever you go through the SSH.

### Directory Navigation

* [aliasme](https://github.com/Jintin/aliasme) [![GitHub stars](https://img.shields.io/github/stars/Jintin/aliasme?style=flat)](https://github.com/Jintin/aliasme/stargazers) - alias helper to change directory quickly
* [autojump](https://github.com/wting/autojump) [![GitHub stars](https://img.shields.io/github/stars/wting/autojump?style=flat)](https://github.com/wting/autojump/stargazers) - A cd command that learns - easily navigate directories from the command line
* [bashmarks](https://github.com/huyng/bashmarks) [![GitHub stars](https://img.shields.io/github/stars/huyng/bashmarks?style=flat)](https://github.com/huyng/bashmarks/stargazers) - Directory bookmarks for the shell
* [bd](https://github.com/vigneshwaranr/bd) [![GitHub stars](https://img.shields.io/github/stars/vigneshwaranr/bd?style=flat)](https://github.com/vigneshwaranr/bd/stargazers) - Quickly go back to a parent directory
* [commacd](https://github.com/shyiko/commacd) [![GitHub stars](https://img.shields.io/github/stars/shyiko/commacd?style=flat)](https://github.com/shyiko/commacd/stargazers) - A faster way to move around in Bash
* [enhancd](https://github.com/b4b4r07/enhancd) [![GitHub stars](https://img.shields.io/github/stars/b4b4r07/enhancd?style=flat)](https://github.com/b4b4r07/enhancd/stargazers) - :rocket: A next-generation cd command with an interactive filter
* [goto](https://github.com/iridakos/goto) [![GitHub stars](https://img.shields.io/github/stars/iridakos/goto?style=flat)](https://github.com/iridakos/goto/stargazers) - A shell utility for navigation to aliased directories supporting auto-completion
* [jump](https://github.com/gsamokovarov/jump) [![GitHub stars](https://img.shields.io/github/stars/gsamokovarov/jump?style=flat)](https://github.com/gsamokovarov/jump/stargazers) - Jump helps you navigate your file system faster by learning your habits.
* [lazy-cd](https://github.com/pedramamini/lazy-cd) [![GitHub stars](https://img.shields.io/github/stars/pedramamini/lazy-cd?style=flat)](https://github.com/pedramamini/lazy-cd/stargazers) - Simple bash commands for bookmarked navigation of the file system, complete with bash-completion.
* [up](https://github.com/shannonmoeller/up) [![GitHub stars](https://img.shields.io/github/stars/shannonmoeller/up?style=flat)](https://github.com/shannonmoeller/up/stargazers) - Ascend directories by name or count; for bash, zsh, and fish.
* [z](https://github.com/rupa/z) [![GitHub stars](https://img.shields.io/github/stars/rupa/z?style=flat)](https://github.com/rupa/z/stargazers) - z is the new j, yo
* [z.lua](https://github.com/skywind3000/z.lua) [![GitHub stars](https://img.shields.io/github/stars/skywind3000/z.lua?style=flat)](https://github.com/skywind3000/z.lua/stargazers) - A new cd command that helps you navigate faster by learning your habits
* [zoxide](https://github.com/ajeetdsouza/zoxide) [![GitHub stars](https://img.shields.io/github/stars/ajeetdsouza/zoxide?style=flat)](https://github.com/ajeetdsouza/zoxide/stargazers) - A faster way to navigate your filesystem, written in Rust
* [zpyi](https://github.com/sakshamsharma/zpyi) [![GitHub stars](https://img.shields.io/github/stars/sakshamsharma/zpyi?style=flat)](https://github.com/sakshamsharma/zpyi/stargazers) - Python in Zsh - Easy python scripting in shell

## Customization

*Custom prompts, color themes, etc.*

* [aphrodite-terminal-theme](https://github.com/win0err/aphrodite-terminal-theme) [![GitHub stars](https://img.shields.io/github/stars/win0err/aphrodite-terminal-theme?style=flat)](https://github.com/win0err/aphrodite-terminal-theme/stargazers) — Minimalistic Aphrodite theme (prompt) for sexy terminals that works in bash, fish and zsh
* [base16-builder](https://github.com/base16-builder/base16-builder) [![GitHub stars](https://img.shields.io/github/stars/base16-builder/base16-builder?style=flat)](https://github.com/base16-builder/base16-builder/stargazers) - Base16-Builder
* [bash-full-of-colors](https://github.com/slomkowski/bash-full-of-colors) [![GitHub stars](https://img.shields.io/github/stars/slomkowski/bash-full-of-colors?style=flat)](https://github.com/slomkowski/bash-full-of-colors/stargazers) - Powerful prompt with screen, tmux, git support and many more
* [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt) [![GitHub stars](https://img.shields.io/github/stars/magicmonty/bash-git-prompt?style=flat)](https://github.com/magicmonty/bash-git-prompt/stargazers) - An informative and fancy Bash prompt for Git users
* [bash-powerline](https://github.com/riobard/bash-powerline) [![GitHub stars](https://img.shields.io/github/stars/riobard/bash-powerline?style=flat)](https://github.com/riobard/bash-powerline/stargazers) - Powerline-style Bash prompt in pure Bash script
* [bashstrap](https://github.com/barryclark/bashstrap) [![GitHub stars](https://img.shields.io/github/stars/barryclark/bashstrap?style=flat)](https://github.com/barryclark/bashstrap/stargazers) - A quick way to spruce up OSX terminal
* [bullet-train-oh-my-zsh-theme](https://github.com/caiogondim/bullet-train.zsh) [![GitHub stars](https://img.shields.io/github/stars/caiogondim/bullet-train.zsh?style=flat)](https://github.com/caiogondim/bullet-train.zsh/stargazers) - :bullettrain_side: An oh-my-zsh shell theme based on the Powerline Vim plugin
* [emojify](https://github.com/mrowa44/emojify) [![GitHub stars](https://img.shields.io/github/stars/mrowa44/emojify?style=flat)](https://github.com/mrowa44/emojify/stargazers) Emoji on the command line :scream:
* [flatui-terminal-theme](https://dribbble.com/shots/1021755-Flat-UI-Terminal-Theme) - Nicer colors for terminal
* [geometry](https://github.com/geometry-zsh/geometry) [![GitHub stars](https://img.shields.io/github/stars/geometry-zsh/geometry?style=flat)](https://github.com/geometry-zsh/geometry/stargazers) - A minimal ZSH theme where any function can be added to the left prompt or (async) right prompt on the fly.
* [git-prompt](https://github.com/lvv/git-prompt) [![GitHub stars](https://img.shields.io/github/stars/lvv/git-prompt?style=flat)](https://github.com/lvv/git-prompt/stargazers) - Bash prompt with Git, SVN and HG modules
* [gittify](https://github.com/momeni/gittify) [![GitHub stars](https://img.shields.io/github/stars/momeni/gittify?style=flat)](https://github.com/momeni/gittify/stargazers) - A colorful Bash prompt + customized Git aliases
* [Gogh - Color Scheme](https://github.com/Mayccoll/Gogh) [![GitHub stars](https://img.shields.io/github/stars/Mayccoll/Gogh?style=flat)](https://github.com/Mayccoll/Gogh/stargazers) - Color Scheme for Gnome Terminal
* [liquidprompt](https://github.com/nojhan/liquidprompt) [![GitHub stars](https://img.shields.io/github/stars/nojhan/liquidprompt?style=flat)](https://github.com/nojhan/liquidprompt/stargazers) - A full-featured & carefully designed adaptive prompt for Bash & Zsh
* [mysql-colorize](https://github.com/zpm-zsh/mysql-colorize) [![GitHub stars](https://img.shields.io/github/stars/zpm-zsh/mysql-colorize?style=flat)](https://github.com/zpm-zsh/mysql-colorize/stargazers) -  Colorization for mysql comand-line client
* [oh-my-git](https://github.com/arialdomartini/oh-my-git) [![GitHub stars](https://img.shields.io/github/stars/arialdomartini/oh-my-git?style=flat)](https://github.com/arialdomartini/oh-my-git/stargazers) - An opinionated git prompt for bash and zsh
* [oh-my-posh](https://ohmyposh.dev) - Prompt theme engine for any shell and platform written in go.
* [polyglot](https://github.com/agkozak/polyglot) [![GitHub stars](https://img.shields.io/github/stars/agkozak/polyglot?style=flat)](https://github.com/agkozak/polyglot/stargazers) - An informative Git prompt that works in bash, zsh, ksh, mksh, pdksh, oksh, dash, yash, busybox sh, and osh
* [powerlevel10k](https://github.com/romkatv/powerlevel10k) [![GitHub stars](https://img.shields.io/github/stars/romkatv/powerlevel10k?style=flat)](https://github.com/romkatv/powerlevel10k/stargazers) - Super flexible awesome powerline ZSH theme
* [sexy-bash-prompt](https://github.com/twolfson/sexy-bash-prompt) [![GitHub stars](https://img.shields.io/github/stars/twolfson/sexy-bash-prompt?style=flat)](https://github.com/twolfson/sexy-bash-prompt/stargazers) - Bash prompt with colors, Git statuses, and Git branches
* [starship](https://starship.rs/) - Fast, customisable, cross-shell prompt written in rust
* [synth-shell](https://github.com/andresgongora/synth-shell) [![GitHub stars](https://img.shields.io/github/stars/andresgongora/synth-shell?style=flat)](https://github.com/andresgongora/synth-shell/stargazers) - Greeter with a customizable status report and a fancy bash prompt

## For Developers

*Command-line development, version control, and deployment.*

* [1Password SSH Agent](https://developer.1password.com/docs/ssh/) - Authenticate Git and SSH workflows with biometric unlock using 1Password
* [ack](https://beyondgrep.com/) - A grep-like search tool optimized for source code.
* [add-gitignore](https://github.com/TejasQ/add-gitignore) [![GitHub stars](https://img.shields.io/github/stars/TejasQ/add-gitignore?style=flat)](https://github.com/TejasQ/add-gitignore/stargazers) - Interactive CLI that generates a .gitignore for your project based on your needs.
* [bcal](https://github.com/jarun/bcal) [![GitHub stars](https://img.shields.io/github/stars/jarun/bcal?style=flat)](https://github.com/jarun/bcal/stargazers) - Byte CALculator for storage conversions and calculations
* [bitwise](https://github.com/mellowcandle/bitwise) [![GitHub stars](https://img.shields.io/github/stars/mellowcandle/bitwise?style=flat)](https://github.com/mellowcandle/bitwise/stargazers) - Terminal based interactive bit manipulator in curses.
* [bocker](https://github.com/p8952/bocker) [![GitHub stars](https://img.shields.io/github/stars/p8952/bocker?style=flat)](https://github.com/p8952/bocker/stargazers) - Docker implemented in 100 lines of bash
* [cloc](https://github.com/AlDanial/cloc) [![GitHub stars](https://img.shields.io/github/stars/AlDanial/cloc?style=flat)](https://github.com/AlDanial/cloc/stargazers) - Count Lines of Code
* [doclt](https://github.com/omgimanerd/doclt) [![GitHub stars](https://img.shields.io/github/stars/omgimanerd/doclt?style=flat)](https://github.com/omgimanerd/doclt/stargazers) - A command line interface to Digital Ocean
* [dokku](https://github.com/dokku/dokku) [![GitHub stars](https://img.shields.io/github/stars/dokku/dokku?style=flat)](https://github.com/dokku/dokku/stargazers) - Docker powered mini-Heroku. The smallest PaaS implementation you've ever seen.
* [forgit](https://github.com/wfxr/forgit) [![GitHub stars](https://img.shields.io/github/stars/wfxr/forgit?style=flat)](https://github.com/wfxr/forgit/stargazers) - Utility tool for `git` taking advantage of fuzzy finder fzf.
* [git-extra-commands](https://github.com/unixorn/git-extra-commands) [![GitHub stars](https://img.shields.io/github/stars/unixorn/git-extra-commands?style=flat)](https://github.com/unixorn/git-extra-commands/stargazers) - Many Git extra utilities. Churn, cut-branch, improved-merge and many more.
* [git-extras](https://github.com/tj/git-extras) [![GitHub stars](https://img.shields.io/github/stars/tj/git-extras?style=flat)](https://github.com/tj/git-extras/stargazers) - Git utilities -- repo summary, repl, changelog population, author commit percentages and more
* [git-open](https://github.com/paulirish/git-open) [![GitHub stars](https://img.shields.io/github/stars/paulirish/git-open?style=flat)](https://github.com/paulirish/git-open/stargazers) - Type `git open` to open the GitHub page or website for a repository in your browser
* [git-quick-stats](https://github.com/arzzen/git-quick-stats) [![GitHub stars](https://img.shields.io/github/stars/arzzen/git-quick-stats?style=flat)](https://github.com/arzzen/git-quick-stats/stargazers) - Git quick statistics is a simple and efficient way to access various statistics in git repository.
* [git-semver](https://github.com/markchalloner/git-semver) [![GitHub stars](https://img.shields.io/github/stars/markchalloner/git-semver?style=flat)](https://github.com/markchalloner/git-semver/stargazers) - Git plugin for easing semantic versioning and changelog validation
* [git-sh](https://github.com/rtomayko/git-sh) [![GitHub stars](https://img.shields.io/github/stars/rtomayko/git-sh?style=flat)](https://github.com/rtomayko/git-sh/stargazers) - A customized Bash environment suitable for Git work
* [gita](https://github.com/nosarthur/gita) [![GitHub stars](https://img.shields.io/github/stars/nosarthur/gita?style=flat)](https://github.com/nosarthur/gita/stargazers) - A command-line tool to manage multiple git repos.
* [hub](https://github.com/github/hub) [![GitHub stars](https://img.shields.io/github/stars/github/hub?style=flat)](https://github.com/github/hub/stargazers) - hub helps you win at git.
* [just](https://github.com/casey/just) [![GitHub stars](https://img.shields.io/github/stars/casey/just?style=flat)](https://github.com/casey/just/stargazers) - Task runner for saving and running project-specific commands.
* [licins](https://github.com/dogoncouch/licins) [![GitHub stars](https://img.shields.io/github/stars/dogoncouch/licins?style=flat)](https://github.com/dogoncouch/licins/stargazers) - Insert commented software licenses into source code.
* [mkdkr](https://github.com/rosineygp/mkdkr) [![GitHub stars](https://img.shields.io/github/stars/rosineygp/mkdkr?style=flat)](https://github.com/rosineygp/mkdkr/stargazers) - Makefile + Docker = CI Pipeline
* [mr](https://myrepos.branchable.com) - Multiple Repository management tool
* [nve](https://github.com/ehmicky/nve) [![GitHub stars](https://img.shields.io/github/stars/ehmicky/nve?style=flat)](https://github.com/ehmicky/nve/stargazers) - Run any command on specific Node.js versions.
* [overcommit](https://github.com/sds/overcommit) [![GitHub stars](https://img.shields.io/github/stars/sds/overcommit?style=flat)](https://github.com/sds/overcommit/stargazers) - A fully configurable and extendable Git hook manager
* [pre-commit](https://pre-commit.com) - A framework for managing and maintaining multi-language pre-commit hooks
* [rebound](https://github.com/shobrook/rebound) [![GitHub stars](https://img.shields.io/github/stars/shobrook/rebound?style=flat)](https://github.com/shobrook/rebound/stargazers) - Instantly browse Stack Overflow results in your terminal when you get a compiler error
* [repren](https://github.com/jlevy/repren) [![GitHub stars](https://img.shields.io/github/stars/jlevy/repren?style=flat)](https://github.com/jlevy/repren/stargazers) - Command-line search-and-replace and file-renaming swiss army knife
* [slap](https://github.com/slap-editor/slap) [![GitHub stars](https://img.shields.io/github/stars/slap-editor/slap?style=flat)](https://github.com/slap-editor/slap/stargazers) - Sublime-like terminal-based text editor that runs on Node.js
* [shipit](https://github.com/sapegin/shipit) [![GitHub stars](https://img.shields.io/github/stars/sapegin/shipit?style=flat)](https://github.com/sapegin/shipit/stargazers) - Minimalistic SSH deployment
* [starring](https://github.com/ritz078/starring) [![GitHub stars](https://img.shields.io/github/stars/ritz078/starring?style=flat)](https://github.com/ritz078/starring/stargazers) - Automatically star the npm-packages that you are using on GitHub.
* [tag](https://github.com/aykamko/tag) [![GitHub stars](https://img.shields.io/github/stars/aykamko/tag?style=flat)](https://github.com/aykamko/tag/stargazers) - Instantly jump to your ag matches.
* [trunk](https://www.npmjs.com/package/@trunkio/launcher) - Blazingly fast meta code checker and formatter
* [vmn](https://github.com/final-israel/vmn) [![GitHub stars](https://img.shields.io/github/stars/final-israel/vmn?style=flat)](https://github.com/final-israel/vmn/stargazers) - git-based automatic versioning and state recovery solution agnostic to language or architecture
* [wipe-modules](https://github.com/bntzio/wipe-modules) [![GitHub stars](https://img.shields.io/github/stars/bntzio/wipe-modules?style=flat)](https://github.com/bntzio/wipe-modules/stargazers) - A little agent that removes the node_modules folder of non-active projects

## System Utilities

*OS-related tools, including system administration, system debugging, and file and process management.*

* [atop](https://www.atoptool.nl) - ASCII full-screen performance monitor that is capable of reporting the activity of all processes
* [bat](https://github.com/sharkdp/bat) [![GitHub stars](https://img.shields.io/github/stars/sharkdp/bat?style=flat)](https://github.com/sharkdp/bat/stargazers) - A `cat` clone with wings
* [bmon](https://github.com/tgraf/bmon) [![GitHub stars](https://img.shields.io/github/stars/tgraf/bmon?style=flat)](https://github.com/tgraf/bmon/stargazers) - Real-time network bandwidth monitor and rate estimator with human-friendly visual output
* [btop](https://github.com/aristocratos/btop) [![GitHub stars](https://img.shields.io/github/stars/aristocratos/btop?style=flat)](https://github.com/aristocratos/btop/stargazers) - Linux/OSX/FreeBSD resource monitor
* [catcli](https://github.com/deadc0de6/catcli) [![GitHub stars](https://img.shields.io/github/stars/deadc0de6/catcli?style=flat)](https://github.com/deadc0de6/catcli/stargazers) -  The command line catalog tool for your offline data
* [ccat](https://github.com/owenthereal/ccat) [![GitHub stars](https://img.shields.io/github/stars/owenthereal/ccat?style=flat)](https://github.com/owenthereal/ccat/stargazers) - ccat is the colorizing cat. It works similar to cat but displays content with syntax highlighting.
* [exa](https://github.com/ogham/exa) [![GitHub stars](https://img.shields.io/github/stars/ogham/exa?style=flat)](https://github.com/ogham/exa/stargazers) - A modern version of `ls`.
* [progress](https://github.com/Xfennec/progress) [![GitHub stars](https://img.shields.io/github/stars/Xfennec/progress?style=flat)](https://github.com/Xfennec/progress/stargazers) - Linux tool to show progress for `cp`, `rm`, `dd`, and more...
* [stronghold](https://github.com/alichtman/stronghold) [![GitHub stars](https://img.shields.io/github/stars/alichtman/stronghold?style=flat)](https://github.com/alichtman/stronghold/stargazers) - Easily configure MacOS security settings from the terminal.
* [glances](https://github.com/nicolargo/glances) [![GitHub stars](https://img.shields.io/github/stars/nicolargo/glances?style=flat)](https://github.com/nicolargo/glances/stargazers) - Glances an Eye on your system
* [goaccess](https://github.com/allinurl/goaccess) [![GitHub stars](https://img.shields.io/github/stars/allinurl/goaccess?style=flat)](https://github.com/allinurl/goaccess/stargazers) - GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in \*nix systems.
* [hblock](https://github.com/hectorm/hblock) [![GitHub stars](https://img.shields.io/github/stars/hectorm/hblock?style=flat)](https://github.com/hectorm/hblock/stargazers) - Hosts-file based adblocker
* [histstat](https://github.com/vesche/histstat) [![GitHub stars](https://img.shields.io/github/stars/vesche/histstat?style=flat)](https://github.com/vesche/histstat/stargazers) - History for netstat
* [htop](https://github.com/hishamhm/htop) [![GitHub stars](https://img.shields.io/github/stars/hishamhm/htop?style=flat)](https://github.com/hishamhm/htop/stargazers) - A ncurses based interactive process viewer which aims to be a better `top`
* [lnav](https://lnav.org) - An advanced log file viewer for the small-scale
* [logdissect](https://github.com/dogoncouch/logdissect) [![GitHub stars](https://img.shields.io/github/stars/dogoncouch/logdissect?style=flat)](https://github.com/dogoncouch/logdissect/stargazers) - CLI utility and Python API for analyzing log files and other data.
* [ls++](https://github.com/trapd00r/ls--) [![GitHub stars](https://img.shields.io/github/stars/trapd00r/ls--?style=flat)](https://github.com/trapd00r/ls--/stargazers) - Colorized ls on steroids
* [lsd](https://github.com/Peltoche/lsd) [![GitHub stars](https://img.shields.io/github/stars/Peltoche/lsd?style=flat)](https://github.com/Peltoche/lsd/stargazers) - LSDeluxe, rewrite of GNU ls with lot of added features like colors, icons, tree-view and more formatting options.
* [lsp](https://github.com/dborzov/lsp) [![GitHub stars](https://img.shields.io/github/stars/dborzov/lsp?style=flat)](https://github.com/dborzov/lsp/stargazers) - An improved `ls`, with file descriptions in plain language and intelligent file grouping
* [maza](https://github.com/tanrax/maza-ad-blocking) [![GitHub stars](https://img.shields.io/github/stars/tanrax/maza-ad-blocking?style=flat)](https://github.com/tanrax/maza-ad-blocking/stargazers) - Local ad blocker. Like Pi-hole but local and using your operating system.
* [mtr](https://github.com/traviscross/mtr) [![GitHub stars](https://img.shields.io/github/stars/traviscross/mtr?style=flat)](https://github.com/traviscross/mtr/stargazers) - The functionality of the 'traceroute' and 'ping' programs in a single network diagnostic tool.
* [ncdu](https://dev.yorhel.nl/ncdu) - NCurses Disk Usage
* [nmtui](https://github.com/NetworkManager/NetworkManager) [![GitHub stars](https://img.shields.io/github/stars/NetworkManager/NetworkManager?style=flat)](https://github.com/NetworkManager/NetworkManager/stargazers) - Text User Interface for controlling NetworkManager
* [powertop](https://github.com/fenrus75/powertop) [![GitHub stars](https://img.shields.io/github/stars/fenrus75/powertop?style=flat)](https://github.com/fenrus75/powertop/stargazers) - Battery/Power usage and device stats monitoring command-line tool, with tune-up options.
* [prettyping](https://github.com/denilsonsa/prettyping) [![GitHub stars](https://img.shields.io/github/stars/denilsonsa/prettyping?style=flat)](https://github.com/denilsonsa/prettyping/stargazers) - Making the output of `ping` prettier, more colorful, more compact, and easier to read.
* [procdog](https://github.com/jlevy/procdog) [![GitHub stars](https://img.shields.io/github/stars/jlevy/procdog?style=flat)](https://github.com/jlevy/procdog/stargazers) - Lightweight command-line control of long-lived processes like servers
* [quick-secure](https://github.com/marshyski/quick-secure) [![GitHub stars](https://img.shields.io/github/stars/marshyski/quick-secure?style=flat)](https://github.com/marshyski/quick-secure/stargazers) - Quickly secure and harden UNIX/Linux systems
* [rng](https://github.com/nickolasburr/rng) [![GitHub stars](https://img.shields.io/github/stars/nickolasburr/rng?style=flat)](https://github.com/nickolasburr/rng/stargazers) - Copy range of lines from file or stdin to stdout.
* [tiptop](https://github.com/nschloe/tiptop) [![GitHub stars](https://img.shields.io/github/stars/nschloe/tiptop?style=flat)](https://github.com/nschloe/tiptop/stargazers) - Graphical command-line system monitor.
* [wifi-wand](https://github.com/keithrbennett/wifiwand) [![GitHub stars](https://img.shields.io/github/stars/keithrbennett/wifiwand?style=flat)](https://github.com/keithrbennett/wifiwand/stargazers) - a Ruby command line application for managing WiFi on MacOS (install by `gem install wifi-wand`)
* [xiringuito](https://github.com/ivanilves/xiringuito) [![GitHub stars](https://img.shields.io/github/stars/ivanilves/xiringuito?style=flat)](https://github.com/ivanilves/xiringuito/stargazers) - SSH-based "VPN for poors"

## Downloading and Serving

*Self-hosted, lightweight servers and networking tools written in shell scripts.*

* [aria2](https://github.com/aria2/aria2) [![GitHub stars](https://img.shields.io/github/stars/aria2/aria2?style=flat)](https://github.com/aria2/aria2/stargazers) - aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. It supports HTTP/HTTPS, FTP, BitTorrent and Metalink
* [balls](https://github.com/jneen/balls) [![GitHub stars](https://img.shields.io/github/stars/jneen/balls?style=flat)](https://github.com/jneen/balls/stargazers) - Bash on Balls
* [bashttpd](https://github.com/avleen/bashttpd) [![GitHub stars](https://img.shields.io/github/stars/avleen/bashttpd?style=flat)](https://github.com/avleen/bashttpd/stargazers) - A web server written in Bash
* [bashhub-server](https://github.com/nicksherron/bashhub-server) [![GitHub stars](https://img.shields.io/github/stars/nicksherron/bashhub-server?style=flat)](https://github.com/nicksherron/bashhub-server/stargazers) - Private cloud shell history. Open source server for bashhub
* [bitpocket](https://github.com/sickill/bitpocket) [![GitHub stars](https://img.shields.io/github/stars/sickill/bitpocket?style=flat)](https://github.com/sickill/bitpocket/stargazers) - "DIY Dropbox" or "2-way directory (r)sync with proper deletion"
* [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) [![GitHub stars](https://img.shields.io/github/stars/andreafabrizi/Dropbox-Uploader?style=flat)](https://github.com/andreafabrizi/Dropbox-Uploader/stargazers) - Dropbox Uploader is a Bash script which can be used to upload, download, list or delete files from Dropbox
* [httpie](https://github.com/httpie/httpie) [![GitHub stars](https://img.shields.io/github/stars/httpie/httpie?style=flat)](https://github.com/httpie/httpie/stargazers) - HTTPie is a command line HTTP client, a user-friendly cURL replacement
* [HTTPLab](https://github.com/gchaincl/httplab) [![GitHub stars](https://img.shields.io/github/stars/gchaincl/httplab?style=flat)](https://github.com/gchaincl/httplab/stargazers) - The interactive web server, let you inspect HTTP requests and forge responses.
* [Kapow!](https://github.com/BBVA/kapow) [![GitHub stars](https://img.shields.io/github/stars/BBVA/kapow?style=flat)](https://github.com/BBVA/kapow/stargazers) - If you can script it, you can HTTP it.
* [ngincat](https://github.com/jaburns/ngincat) [![GitHub stars](https://img.shields.io/github/stars/jaburns/ngincat?style=flat)](https://github.com/jaburns/ngincat/stargazers) - Tiny Bash HTTP server using netcat
* [resty](https://github.com/micha/resty) [![GitHub stars](https://img.shields.io/github/stars/micha/resty?style=flat)](https://github.com/micha/resty/stargazers) - Little command line REST client that you can use in pipelines
* [shell2http](https://github.com/msoap/shell2http) [![GitHub stars](https://img.shields.io/github/stars/msoap/shell2http?style=flat)](https://github.com/msoap/shell2http/stargazers) - HTTP-server to execute shell commands. Designed for development, prototyping or remote control
* [tshare](https://github.com/trikko/tshare) [![GitHub stars](https://img.shields.io/github/stars/trikko/tshare?style=flat)](https://github.com/trikko/tshare/stargazers) - File sharing from commandline.
* [vesper](https://github.com/chris-rock/vesper) [![GitHub stars](https://img.shields.io/github/stars/chris-rock/vesper?style=flat)](https://github.com/chris-rock/vesper/stargazers) - 🍸Vesper is a HTTP framework for Bash/Unix Shell
* [xh](https://github.com/ducaale/xh) [![GitHub stars](https://img.shields.io/github/stars/ducaale/xh?style=flat)](https://github.com/ducaale/xh/stargazers) - Friendly and fast tool for sending HTTP requests
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) [![GitHub stars](https://img.shields.io/github/stars/yt-dlp/yt-dlp?style=flat)](https://github.com/yt-dlp/yt-dlp/stargazers) - Command-line program to download videos from YouTube.com and other video sites

## Multimedia and File Formats

*Tools for handling video and audio files.*

* [adb-export](https://github.com/sromku/adb-export) [![GitHub stars](https://img.shields.io/github/stars/sromku/adb-export?style=flat)](https://github.com/sromku/adb-export/stargazers) - Export Android content providers to CSV format
* [Android-Kitchen](https://github.com/dsixda/Android-Kitchen) [![GitHub stars](https://img.shields.io/github/stars/dsixda/Android-Kitchen?style=flat)](https://github.com/dsixda/Android-Kitchen/stargazers) - A text-based kitchen for Android ROM customization. Uses shell scripts and works with Cygwin/OS X/Linux
* [Beets](https://github.com/beetbox/beets) [![GitHub stars](https://img.shields.io/github/stars/beetbox/beets?style=flat)](https://github.com/beetbox/beets/stargazers) - Music library manager and MusicBrainz tagger
* [cmus](https://github.com/cmus/cmus) [![GitHub stars](https://img.shields.io/github/stars/cmus/cmus?style=flat)](https://github.com/cmus/cmus/stargazers) - Cross-platform cli audio player.
* [dasel](https://github.com/tomwright/dasel) [![GitHub stars](https://img.shields.io/github/stars/tomwright/dasel?style=flat)](https://github.com/tomwright/dasel/stargazers) - Query and update data structures using selectors from the command line. Comparable to [jq](https://github.com/stedolan/jq) [![GitHub stars](https://img.shields.io/github/stars/stedolan/jq?style=flat)](https://github.com/stedolan/jq/stargazers) / [yq](https://github.com/kislyuk/yq) [![GitHub stars](https://img.shields.io/github/stars/kislyuk/yq?style=flat)](https://github.com/kislyuk/yq/stargazers) but supports JSON, YAML, TOML and XML with zero runtime dependencies.
* [dzr](https://github.com/yne/dzr) [![GitHub stars](https://img.shields.io/github/stars/yne/dzr?style=flat)](https://github.com/yne/dzr/stargazers) - Cross-platform Deezer.com audio player.
* [fx](https://github.com/antonmedv/fx) [![GitHub stars](https://img.shields.io/github/stars/antonmedv/fx?style=flat)](https://github.com/antonmedv/fx/stargazers) - Command-line JSON processing tool by anononymus JavaScript functions
* [gifgen](https://github.com/lukechilds/gifgen) [![GitHub stars](https://img.shields.io/github/stars/lukechilds/gifgen?style=flat)](https://github.com/lukechilds/gifgen/stargazers) - Simple high quality GIF encoding
* [image-scraper](https://github.com/sananth12/ImageScraper) [![GitHub stars](https://img.shields.io/github/stars/sananth12/ImageScraper?style=flat)](https://github.com/sananth12/ImageScraper/stargazers) - A cool command line image scraper with a lot of features.
* [imgp](https://github.com/jarun/imgp) [![GitHub stars](https://img.shields.io/github/stars/jarun/imgp?style=flat)](https://github.com/jarun/imgp/stargazers) - Blazing fast batch image resizer and rotator
* [jc](https://github.com/kellyjonbrazil/jc) [![GitHub stars](https://img.shields.io/github/stars/kellyjonbrazil/jc?style=flat)](https://github.com/kellyjonbrazil/jc/stargazers) - Convert command output, file-types, and common strings to JSON or YAML for easier use in scripts.
* [jo](https://github.com/jpmens/jo) [![GitHub stars](https://img.shields.io/github/stars/jpmens/jo?style=flat)](https://github.com/jpmens/jo/stargazers) - A small utility to create JSON objects from command-line arguments.
* [jq](https://github.com/stedolan/jq) [![GitHub stars](https://img.shields.io/github/stars/stedolan/jq?style=flat)](https://github.com/stedolan/jq/stargazers) - Sed for json data. You can use it to slice and filter and map and transform structured data
* [korkut](https://github.com/oguzhaninan/korkut) [![GitHub stars](https://img.shields.io/github/stars/oguzhaninan/korkut?style=flat)](https://github.com/oguzhaninan/korkut/stargazers) - Quick and simple image processing at the command line.
* [library](https://github.com/chapmanjacobd/library) [![GitHub stars](https://img.shields.io/github/stars/chapmanjacobd/library?style=flat)](https://github.com/chapmanjacobd/library/stargazers) - Create SQLITE databases for folders of music, video, images, or online media. Play and track media like Plex but a CLI-only interface with many sorting options.
* [mpv](https://mpv.io/) - Lets you play most audio and video formats (using ASCII characters) in the shell as well as in a GUI.
* [nehm](https://github.com/bogem/nehm) [![GitHub stars](https://img.shields.io/github/stars/bogem/nehm?style=flat)](https://github.com/bogem/nehm/stargazers) - Console tool, which downloads, sets IDv3 tags and adds to your iTunes (if you use it) your SoundCloud likes in convenient way
* [PiCAST](https://github.com/lanceseidman/PiCAST) [![GitHub stars](https://img.shields.io/github/stars/lanceseidman/PiCAST?style=flat)](https://github.com/lanceseidman/PiCAST/stargazers) - PiCAST turns your $35 Raspberry Pi in to a Chromecast like Device
* [sejda](https://github.com/torakiki/sejda/) [![GitHub stars](https://img.shields.io/github/stars/torakiki/sejda/?style=flat)](https://github.com/torakiki/sejda//stargazers) - Command line manipulation of PDF documents (split, merge, rotate, convert to jpg, extract text, etc)
* [visidata](https://github.com/saulpw/visidata) [![GitHub stars](https://img.shields.io/github/stars/saulpw/visidata?style=flat)](https://github.com/saulpw/visidata/stargazers) - A terminal spreadsheet multitool for exploring and arranging data (csv/json/xml/xls/yaml/etc)
* [xidel](https://github.com/benibela/xidel/) [![GitHub stars](https://img.shields.io/github/stars/benibela/xidel/?style=flat)](https://github.com/benibela/xidel//stargazers) - Cli tool to filter, map and create HTML/XML/JSON data with (Turing-complete) XPath and XQuery.
* [xmlstarlet](http://xmlstar.sourceforge.net/) - Old but powerful tool for command-line XML formatting, filtering, and manipulation.
* [yq](https://github.com/mikefarah/yq) [![GitHub stars](https://img.shields.io/github/stars/mikefarah/yq?style=flat)](https://github.com/mikefarah/yq/stargazers) - yq is a portable command-line YAML processor

## Applications

*Command line-based applications or command line access to existing services.*

* [ansiweather](https://github.com/fcambus/ansiweather) [![GitHub stars](https://img.shields.io/github/stars/fcambus/ansiweather?style=flat)](https://github.com/fcambus/ansiweather/stargazers) - Weather in your terminal, with ANSI colors and Unicode symbols
* [awless](https://github.com/wallix/awless) [![GitHub stars](https://img.shields.io/github/stars/wallix/awless?style=flat)](https://github.com/wallix/awless/stargazers) - A powerful, innovative and small surface CLI to manage AWS.
* [bashblog](https://github.com/cfenollosa/bashblog) [![GitHub stars](https://img.shields.io/github/stars/cfenollosa/bashblog?style=flat)](https://github.com/cfenollosa/bashblog/stargazers) - A Bash script that handles blog posting
* [carbon-now-cli](https://github.com/mixn/carbon-now-cli) [![GitHub stars](https://img.shields.io/github/stars/mixn/carbon-now-cli?style=flat)](https://github.com/mixn/carbon-now-cli/stargazers) - 🎨 Beautiful images of your code — from right inside your terminal.
* [choosealicense-cli](https://github.com/lord63/choosealicense-cli) [![GitHub stars](https://img.shields.io/github/stars/lord63/choosealicense-cli?style=flat)](https://github.com/lord63/choosealicense-cli/stargazers) - Choose an OSS license from the comfort of your terminal
* [cointop](https://github.com/miguelmota/cointop) [![GitHub stars](https://img.shields.io/github/stars/miguelmota/cointop?style=flat)](https://github.com/miguelmota/cointop/stargazers) - The fastest and most interactive terminal based UI application for tracking cryptocurrencies
* [dstask](https://github.com/naggie/dstask) [![GitHub stars](https://img.shields.io/github/stars/naggie/dstask?style=flat)](https://github.com/naggie/dstask/stargazers) - Single binary terminal-based TODO manager with git-based sync + markdown notes per task
* [editly](https://github.com/mifi/editly) [![GitHub stars](https://img.shields.io/github/stars/mifi/editly?style=flat)](https://github.com/mifi/editly/stargazers) - Command line video editor
* [facebook-cli](https://github.com/specious/facebook-cli) [![GitHub stars](https://img.shields.io/github/stars/specious/facebook-cli?style=flat)](https://github.com/specious/facebook-cli/stargazers) - Facebook command line tool
* [fanyi](https://github.com/afc163/fanyi) [![GitHub stars](https://img.shields.io/github/stars/afc163/fanyi?style=flat)](https://github.com/afc163/fanyi/stargazers) - Translate English to Chinese in terminal
* [gcalcli](https://github.com/insanum/gcalcli) [![GitHub stars](https://img.shields.io/github/stars/insanum/gcalcli?style=flat)](https://github.com/insanum/gcalcli/stargazers) - Google Calendar command line interface
* [geeknote](https://github.com/VitaliyRodnenko/geeknote) [![GitHub stars](https://img.shields.io/github/stars/VitaliyRodnenko/geeknote?style=flat)](https://github.com/VitaliyRodnenko/geeknote/stargazers) - Command line evernote client
* [haxor-news](https://github.com/donnemartin/haxor-news) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/haxor-news?style=flat)](https://github.com/donnemartin/haxor-news/stargazers) - Browse Hacker News like a haxor
* [hn-cli](https://github.com/rafaelrinaldi/hn-cli) [![GitHub stars](https://img.shields.io/github/stars/rafaelrinaldi/hn-cli?style=flat)](https://github.com/rafaelrinaldi/hn-cli/stargazers) - Browse Hacker News from the comfort of your Terminal
* [iponmap](https://github.com/nogizhopaboroda/iponmap) [![GitHub stars](https://img.shields.io/github/stars/nogizhopaboroda/iponmap?style=flat)](https://github.com/nogizhopaboroda/iponmap/stargazers) - Draw point on world map using ip address
* [isitup](https://github.com/lord63/isitup) [![GitHub stars](https://img.shields.io/github/stars/lord63/isitup?style=flat)](https://github.com/lord63/isitup/stargazers) - Check whether a website is up or down
* [jrnl](https://github.com/jrnl-org/jrnl) [![GitHub stars](https://img.shields.io/github/stars/jrnl-org/jrnl?style=flat)](https://github.com/jrnl-org/jrnl/stargazers) - A simple command line journal application that stores your journal in a plain text file
* [kanban.bash](https://github.com/coderofsalvation/kanban.bash) [![GitHub stars](https://img.shields.io/github/stars/coderofsalvation/kanban.bash?style=flat)](https://github.com/coderofsalvation/kanban.bash/stargazers) - commandline asciii kanban board for minimalist productivity bash hackers (csv-based)
* [ledger](https://github.com/ledger/ledger) [![GitHub stars](https://img.shields.io/github/stars/ledger/ledger?style=flat)](https://github.com/ledger/ledger/stargazers) - Command line accounting
* [licen](https://github.com/lord63/licen) [![GitHub stars](https://img.shields.io/github/stars/lord63/licen?style=flat)](https://github.com/lord63/licen/stargazers) - Generate your license. Yet another lice, but implement with Jinja2 and docopt
* [md2png](https://github.com/weaming/md2png) [![GitHub stars](https://img.shields.io/github/stars/weaming/md2png?style=flat)](https://github.com/weaming/md2png/stargazers) - Convert markdown to PNG image
* [moviemon](https://github.com/iCHAIT/moviemon) [![GitHub stars](https://img.shields.io/github/stars/iCHAIT/moviemon?style=flat)](https://github.com/iCHAIT/moviemon/stargazers) - Everything about your movies within the command line.
* [nomino](https://github.com/yaa110/nomino) [![GitHub stars](https://img.shields.io/github/stars/yaa110/nomino?style=flat)](https://github.com/yaa110/nomino/stargazers) - Batch rename utility using regex, sort and map file options.
* [pcalc](https://github.com/alt-romes/programmer-calculator) [![GitHub stars](https://img.shields.io/github/stars/alt-romes/programmer-calculator?style=flat)](https://github.com/alt-romes/programmer-calculator/stargazers) - Calculator made for programmers working with multiple number representations, sizes, and overall close to the bits.
* [pockyt](https://github.com/achembarpu/pockyt) [![GitHub stars](https://img.shields.io/github/stars/achembarpu/pockyt?style=flat)](https://github.com/achembarpu/pockyt/stargazers) - Read, Manage, and Automate your [Pocket](https://getpocket.com) collection.
* [pushblast](https://github.com/alebcay/pushblast) [![GitHub stars](https://img.shields.io/github/stars/alebcay/pushblast?style=flat)](https://github.com/alebcay/pushblast/stargazers) - Get PushBullet notifications when a shell program exits
* [pushbullet-bash](https://github.com/Red5d/pushbullet-bash) [![GitHub stars](https://img.shields.io/github/stars/Red5d/pushbullet-bash?style=flat)](https://github.com/Red5d/pushbullet-bash/stargazers) - Bash interface to the PushBullet API
* [ranger](https://github.com/ranger/ranger) [![GitHub stars](https://img.shields.io/github/stars/ranger/ranger?style=flat)](https://github.com/ranger/ranger/stargazers) - A console file manager with VI key bindings.
* [Reddit Terminal Viewer](https://github.com/michael-lazar/rtv) [![GitHub stars](https://img.shields.io/github/stars/michael-lazar/rtv?style=flat)](https://github.com/michael-lazar/rtv/stargazers) - Browse Reddit from your terminal
* [SAWS](https://github.com/donnemartin/saws) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/saws?style=flat)](https://github.com/donnemartin/saws/stargazers) - A Supercharged AWS CLI
* [taskbook](https://github.com/klaussinani/taskbook) [![GitHub stars](https://img.shields.io/github/stars/klaussinani/taskbook?style=flat)](https://github.com/klaussinani/taskbook/stargazers) - Tasks, boards & notes for the command-line habitat
* [taskwarrior](https://taskwarrior.org/) - A command-line TODO list manager
* [terjira](https://github.com/keepcosmos/terjira) [![GitHub stars](https://img.shields.io/github/stars/keepcosmos/terjira?style=flat)](https://github.com/keepcosmos/terjira/stargazers) - Command line power tool for Jira
* [ticker](https://github.com/achannarasappa/ticker) [![GitHub stars](https://img.shields.io/github/stars/achannarasappa/ticker?style=flat)](https://github.com/achannarasappa/ticker/stargazers) — Terminal stock ticker with live updates and position tracking
* [vl](https://github.com/ellisonleao/vl) [![GitHub stars](https://img.shields.io/github/stars/ellisonleao/vl?style=flat)](https://github.com/ellisonleao/vl/stargazers) - URL link checker on text documents
* [wego](https://github.com/schachmat/wego) [![GitHub stars](https://img.shields.io/github/stars/schachmat/wego?style=flat)](https://github.com/schachmat/wego/stargazers) - Weather app for the terminal
* [whales](https://github.com/Gueils/whales) [![GitHub stars](https://img.shields.io/github/stars/Gueils/whales?style=flat)](https://github.com/Gueils/whales/stargazers) - A tool to automatically dockerize your applications
* [whereami](https://github.com/rafaelrinaldi/whereami) [![GitHub stars](https://img.shields.io/github/stars/rafaelrinaldi/whereami?style=flat)](https://github.com/rafaelrinaldi/whereami/stargazers) - Get your geolocation information from the CLI
* [wttr.in](https://github.com/chubin/wttr.in) [![GitHub stars](https://img.shields.io/github/stars/chubin/wttr.in?style=flat)](https://github.com/chubin/wttr.in/stargazers) - :partly_sunny: The right way to check the weather (curl wttr.in)

## Games

*All work and no play is a cruddy way to spend your day.*

* [bash2048](https://github.com/mydzor/bash2048) [![GitHub stars](https://img.shields.io/github/stars/mydzor/bash2048?style=flat)](https://github.com/mydzor/bash2048/stargazers) - Bash implementation of 2048 game
* [minesweeper](https://github.com/feherke/Bash-script/tree/master/minesweeper) [![GitHub stars](https://img.shields.io/github/stars/feherke/Bash-script/tree/master/minesweeper?style=flat)](https://github.com/feherke/Bash-script/tree/master/minesweeper/stargazers) - Bash implementation of minesweeper
* [nudoku](https://github.com/jubalh/nudoku) [![GitHub stars](https://img.shields.io/github/stars/jubalh/nudoku?style=flat)](https://github.com/jubalh/nudoku/stargazers) - ncurses based sudoku game written in C
* [piu-piu](https://github.com/vaniacer/piu-piu-SH) [![GitHub stars](https://img.shields.io/github/stars/vaniacer/piu-piu-SH?style=flat)](https://github.com/vaniacer/piu-piu-SH/stargazers) - Horizontal scroller game in bash with multiplayer mode!
* [sedtris](https://github.com/uuner/sedtris) [![GitHub stars](https://img.shields.io/github/stars/uuner/sedtris?style=flat)](https://github.com/uuner/sedtris/stargazers) - Tetris in sed
* [sed-scripts](https://github.com/aureliojargas/sed-scripts) [![GitHub stars](https://img.shields.io/github/stars/aureliojargas/sed-scripts?style=flat)](https://github.com/aureliojargas/sed-scripts/stargazers) - Arkanoid and Sokoban written using sed
* [SHTAP](https://notimetoplay.org/engines/shtap/) - Reusable text adventure engine for Bash 4
* [tty-solitaire](https://github.com/mpereira/tty-solitaire) [![GitHub stars](https://img.shields.io/github/stars/mpereira/tty-solitaire?style=flat)](https://github.com/mpereira/tty-solitaire/stargazers) - Play solitaire in your terminal!

## Shell Package Management

*Tools for managing multiple shell configurations. For zsh-specific tools, see the Zsh section.*

* [bash-it](https://github.com/Bash-it/bash-it) [![GitHub stars](https://img.shields.io/github/stars/Bash-it/bash-it?style=flat)](https://github.com/Bash-it/bash-it/stargazers) - A community Bash framework
* [basher](https://github.com/basherpm/basher) [![GitHub stars](https://img.shields.io/github/stars/basherpm/basher?style=flat)](https://github.com/basherpm/basher/stargazers) - A package manager for shell scripts
* [bashing](https://github.com/xsc/bashing) [![GitHub stars](https://img.shields.io/github/stars/xsc/bashing?style=flat)](https://github.com/xsc/bashing/stargazers) - Smashing Bash into Pieces
* [bpkg](https://www.bpkg.sh/) - JavaScript has npm, Ruby has Gems, Python has pip and now Shell has bpkg
* [dotdrop](https://github.com/deadc0de6/dotdrop) [![GitHub stars](https://img.shields.io/github/stars/deadc0de6/dotdrop?style=flat)](https://github.com/deadc0de6/dotdrop/stargazers) - Save your dotfiles once, deploy them everywhere
* [dotfiler](https://github.com/svetlyak40wt/dotfiler) [![GitHub stars](https://img.shields.io/github/stars/svetlyak40wt/dotfiler?style=flat)](https://github.com/svetlyak40wt/dotfiler/stargazers) – Shell agnostic git based dotfiles package manager, written in Python.
* [fresh](https://github.com/freshshell/fresh) [![GitHub stars](https://img.shields.io/github/stars/freshshell/fresh?style=flat)](https://github.com/freshshell/fresh/stargazers) - Keep your dotfiles fresh
* [homeshick](https://github.com/andsens/homeshick) [![GitHub stars](https://img.shields.io/github/stars/andsens/homeshick?style=flat)](https://github.com/andsens/homeshick/stargazers) - Git dotfile synchronizer written in Bash
* [shallow-backup](https://github.com/alichtman/shallow-backup) [![GitHub stars](https://img.shields.io/github/stars/alichtman/shallow-backup?style=flat)](https://github.com/alichtman/shallow-backup/stargazers) - Easily create lightweight documentation of installed packages, dotfiles, and more
* [shundle](https://github.com/javier-lopez/shundle) [![GitHub stars](https://img.shields.io/github/stars/javier-lopez/shundle?style=flat)](https://github.com/javier-lopez/shundle/stargazers) - Plugin manager for shell scripts
* [vcsh](https://github.com/RichiH/vcsh) [![GitHub stars](https://img.shields.io/github/stars/RichiH/vcsh?style=flat)](https://github.com/RichiH/vcsh/stargazers) - Config manager based on Git
* [yadm](https://yadm.io/) - Git-based dotfiles manager supporting encryption, alternates, and bootstrapping

## Shell Script Development

*Tools for writing, improving, or organizing Bash or other shell scripts*

* [ansi](https://github.com/fidian/ansi) [![GitHub stars](https://img.shields.io/github/stars/fidian/ansi?style=flat)](https://github.com/fidian/ansi/stargazers) - ANSI escape codes in pure bash - change text color, position the cursor, much more
* [assert.sh](https://github.com/lehmannro/assert.sh) [![GitHub stars](https://img.shields.io/github/stars/lehmannro/assert.sh?style=flat)](https://github.com/lehmannro/assert.sh/stargazers) - Bash unit testing framework
* [bashew](https://github.com/pforret/bashew) [![GitHub stars](https://img.shields.io/github/stars/pforret/bashew?style=flat)](https://github.com/pforret/bashew/stargazers) - bash script creator - from small stand-alone script to complex projects with CI/CD and testing
* [bashful](https://github.com/jmcantrell/bashful) [![GitHub stars](https://img.shields.io/github/stars/jmcantrell/bashful?style=flat)](https://github.com/jmcantrell/bashful/stargazers) - A collection of libraries to simplify writing Bash scripts
* [Bashlets](https://github.com/reale/bashlets) [![GitHub stars](https://img.shields.io/github/stars/reale/bashlets?style=flat)](https://github.com/reale/bashlets/stargazers) - A modular extensible toolbox for Bash
* [bashly](https://bashly.dannyb.co/) - Bash command line framework and CLI generator
* [bashmanager](https://github.com/lingtalfi/bashmanager) [![GitHub stars](https://img.shields.io/github/stars/lingtalfi/bashmanager?style=flat)](https://github.com/lingtalfi/bashmanager/stargazers) - mini bash framework for creating command line tools
* [bashwithnails](https://github.com/mindaugasbarysas/bashwithnails) [![GitHub stars](https://img.shields.io/github/stars/mindaugasbarysas/bashwithnails?style=flat)](https://github.com/mindaugasbarysas/bashwithnails/stargazers) - a Bash framework written just for fun with testing, dependency management & packaging
* [bash-language-server](https://github.com/bash-lsp/bash-language-server) [![GitHub stars](https://img.shields.io/github/stars/bash-lsp/bash-language-server?style=flat)](https://github.com/bash-lsp/bash-language-server/stargazers) - [LSP](https://microsoft.github.io/language-server-protocol/)-based Bash language server
* [bash-modules](https://github.com/vlisivka/bash-modules) [![GitHub stars](https://img.shields.io/github/stars/vlisivka/bash-modules?style=flat)](https://github.com/vlisivka/bash-modules/stargazers) - functions for developing with [unofficial strict mode](http://redsymbol.net/articles/unofficial-bash-strict-mode/) enabled.
* [bats](https://github.com/bats-core/bats-core) [![GitHub stars](https://img.shields.io/github/stars/bats-core/bats-core?style=flat)](https://github.com/bats-core/bats-core/stargazers) - Bash Automated Testing System
* [composure](https://github.com/erichs/composure) [![GitHub stars](https://img.shields.io/github/stars/erichs/composure?style=flat)](https://github.com/erichs/composure/stargazers) - Compose, document, version and organize your shell functions
* [crash](https://github.com/molovo/crash) [![GitHub stars](https://img.shields.io/github/stars/molovo/crash?style=flat)](https://github.com/molovo/crash/stargazers) - Proper error handling, exceptions and try/catch for ZSH
* [critic.sh](https://github.com/Checksum/critic.sh) [![GitHub stars](https://img.shields.io/github/stars/Checksum/critic.sh?style=flat)](https://github.com/Checksum/critic.sh/stargazers) - Dead simple testing framework for Bash with coverage reporting
* [dispatch](https://github.com/Mosai/workshop/blob/master/doc/dispatch.md) [![GitHub stars](https://img.shields.io/github/stars/Mosai/workshop/blob/master/doc/dispatch.md?style=flat)](https://github.com/Mosai/workshop/blob/master/doc/dispatch.md/stargazers) - A command line argument parser in 50 lines of portable shell script.
* [esh](https://github.com/jirutka/esh) [![GitHub stars](https://img.shields.io/github/stars/jirutka/esh?style=flat)](https://github.com/jirutka/esh/stargazers) - A simple templating engine based on shell, implemented in ~290 lines of POSIX shell and awk.
* [Fishtape](https://github.com/jorgebucaran/fishtape) [![GitHub stars](https://img.shields.io/github/stars/jorgebucaran/fishtape?style=flat)](https://github.com/jorgebucaran/fishtape/stargazers) - TAP producer and test harness for fish
* [getoptions](https://github.com/ko1nksm/getoptions) [![GitHub stars](https://img.shields.io/github/stars/ko1nksm/getoptions?style=flat)](https://github.com/ko1nksm/getoptions/stargazers) - An elegant option parser for shell scripts (sh, bash and all POSIX shells)
* [getopts.fish](https://github.com/jorgebucaran/getopts.fish) [![GitHub stars](https://img.shields.io/github/stars/jorgebucaran/getopts.fish?style=flat)](https://github.com/jorgebucaran/getopts.fish/stargazers) - CLI parser for fish
* [is.sh](https://github.com/qzb/is.sh) [![GitHub stars](https://img.shields.io/github/stars/qzb/is.sh?style=flat)](https://github.com/qzb/is.sh/stargazers) - An alternative for builtin test command, it will make your "if" statements pretty
* [lumberjack](https://github.com/molovo/lumberjack) [![GitHub stars](https://img.shields.io/github/stars/molovo/lumberjack?style=flat)](https://github.com/molovo/lumberjack/stargazers) - A logging interface for shell scripts
* [mo](https://github.com/tests-always-included/mo) [![GitHub stars](https://img.shields.io/github/stars/tests-always-included/mo?style=flat)](https://github.com/tests-always-included/mo/stargazers) - Mustache templates in pure bash
* [optparse](https://github.com/nk412/optparse) [![GitHub stars](https://img.shields.io/github/stars/nk412/optparse?style=flat)](https://github.com/nk412/optparse/stargazers) - A BASH wrapper for getopts, for simple command line arguments.
* [rerun](https://github.com/rerun/rerun) [![GitHub stars](https://img.shields.io/github/stars/rerun/rerun?style=flat)](https://github.com/rerun/rerun/stargazers) - A modular shell automation framework to organize your keeper scripts
* [revolver](https://github.com/molovo/revolver) [![GitHub stars](https://img.shields.io/github/stars/molovo/revolver?style=flat)](https://github.com/molovo/revolver/stargazers) - A reusable progress spinner for shell scripts
* [phases](https://github.com/sorokine/phases) [![GitHub stars](https://img.shields.io/github/stars/sorokine/phases?style=flat)](https://github.com/sorokine/phases/stargazers) - Minimally invasive bash preprocessor, select sections of your script to run
* [powscript](https://github.com/coderofsalvation/powscript) [![GitHub stars](https://img.shields.io/github/stars/coderofsalvation/powscript?style=flat)](https://github.com/coderofsalvation/powscript/stargazers) - bash transpiler written in bash (coffeescript for bash)
* [semver_bash](https://github.com/cloudflare/semver_bash) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/semver_bash?style=flat)](https://github.com/cloudflare/semver_bash/stargazers) - Semantic Versioning in Bash
* [sh-semver](https://github.com/qzb/sh-semver) [![GitHub stars](https://img.shields.io/github/stars/qzb/sh-semver?style=flat)](https://github.com/qzb/sh-semver/stargazers) - Semver tool for bash - finds versions matching to specified rules
* [shellcheck](https://github.com/koalaman/shellcheck) [![GitHub stars](https://img.shields.io/github/stars/koalaman/shellcheck?style=flat)](https://github.com/koalaman/shellcheck/stargazers) - Static analysis tool for shell scripts
* [shellfire](https://github.com/shellfire-dev/shellfire) [![GitHub stars](https://img.shields.io/github/stars/shellfire-dev/shellfire?style=flat)](https://github.com/shellfire-dev/shellfire/stargazers) -  A repository of namespaced, composable shell (bash, sh and dash) function libraries
* [shellspec](https://github.com/shellspec/shellspec) [![GitHub stars](https://img.shields.io/github/stars/shellspec/shellspec?style=flat)](https://github.com/shellspec/shellspec/stargazers) - A full-featured BDD unit testing framework for dash, bash, ksh, zsh and all POSIX shells
* [shfmt](https://github.com/mvdan/sh) [![GitHub stars](https://img.shields.io/github/stars/mvdan/sh?style=flat)](https://github.com/mvdan/sh/stargazers) - A shell parser, formatter, and interpreter with bash support; includes shfmt
* [shpec](https://github.com/rylnd/shpec) [![GitHub stars](https://img.shields.io/github/stars/rylnd/shpec?style=flat)](https://github.com/rylnd/shpec/stargazers) - A shell testing framework
* [shutit](https://ianmiell.github.io/shutit/) - Automation framework based on bash and pexpect
* [sub](https://github.com/basecamp/sub) [![GitHub stars](https://img.shields.io/github/stars/basecamp/sub?style=flat)](https://github.com/basecamp/sub/stargazers) - A delicious way to organize programs
* [ts](https://github.com/thinkerbot/ts) [![GitHub stars](https://img.shields.io/github/stars/thinkerbot/ts?style=flat)](https://github.com/thinkerbot/ts/stargazers) - A shell test script
* [urchin](https://github.com/tlevine/urchin) [![GitHub stars](https://img.shields.io/github/stars/tlevine/urchin?style=flat)](https://github.com/tlevine/urchin/stargazers) - An idiomatic shell testing framework that uses only shell commands
* [shunit2](https://github.com/kward/shunit2) [![GitHub stars](https://img.shields.io/github/stars/kward/shunit2?style=flat)](https://github.com/kward/shunit2/stargazers) - A unit test framework for Bash scripts with a flavour of JUnit/PyUnit.
* [rebash](https://github.com/jandob/rebash) [![GitHub stars](https://img.shields.io/github/stars/jandob/rebash?style=flat)](https://github.com/jandob/rebash/stargazers) - Scripting library/framework. Features: imports, exceptions, doc-tests ...
* [zunit](https://github.com/zunit-zsh/zunit) [![GitHub stars](https://img.shields.io/github/stars/zunit-zsh/zunit?style=flat)](https://github.com/zunit-zsh/zunit/stargazers) - A powerful unit testing framework for ZSH

# Guides

* [Bash Official Reference Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
* [Bash Hackers Wiki](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/)
* [Greg Wooledge's (aka "greycat") wiki](https://mywiki.wooledge.org).
  Specifically [Bash Guide](https://mywiki.wooledge.org/BashGuide), [Bash FAQ](https://mywiki.wooledge.org/BashFAQ) and [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls)
* [Google's Shell Style Guide](https://google.github.io/styleguide/shell.xml)
* [The Linux Documentation Project: Bash Programming - Intro/How-to](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
* [The Linux Documentation Project: Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/)
* [WikiBooks: Bash Shell Scripting](https://en.wikibooks.org/wiki/Bash_Shell_Scripting)
* [Use the Unofficial Bash Strict Mode (Unless You Looove Debugging)](http://redsymbol.net/articles/unofficial-bash-strict-mode/)
* [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) [![GitHub stars](https://img.shields.io/github/stars/jlevy/the-art-of-command-line?style=flat)](https://github.com/jlevy/the-art-of-command-line/stargazers)
* [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics)
* [A guide to learn bash](https://github.com/Idnan/bash-guide) [![GitHub stars](https://img.shields.io/github/stars/Idnan/bash-guide?style=flat)](https://github.com/Idnan/bash-guide/stargazers)
* [Shell Field Guide](https://raimonster.com/scripting-field-guide/)

# Other Awesome Lists

Other amazingly awesome lists can be found in [awesome-awesome](https://github.com/emijrp/awesome-awesome) [![GitHub stars](https://img.shields.io/github/stars/emijrp/awesome-awesome?style=flat)](https://github.com/emijrp/awesome-awesome/stargazers) and [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers).

### See also

* [awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps) [![GitHub stars](https://img.shields.io/github/stars/agarrharr/awesome-cli-apps?style=flat)](https://github.com/agarrharr/awesome-cli-apps/stargazers)
* [awesome-fish][awesome-fish]
* [awesome-zsh][awesome-zsh]
* [awesome-bash][awesome-bash]
* [terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy) [![GitHub stars](https://img.shields.io/github/stars/k4m4/terminals-are-sexy?style=flat)](https://github.com/k4m4/terminals-are-sexy/stargazers)

[awesome-badge]: https://raw.githubusercontent.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg
[awesome-fish]: https://github.com/jorgebucaran/awsm.fish
[awesome-link]: https://github.com/sindresorhus/awesome
[awesome-zsh]: https://github.com/unixorn/awesome-zsh-plugins
[awesome-bash]: https://github.com/awesome-lists/awesome-bash
