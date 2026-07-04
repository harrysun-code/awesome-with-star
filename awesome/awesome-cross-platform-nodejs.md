# Cross-Platform

> 来源：[bcoe/awesome-cross-platform-nodejs](https://github.com/bcoe/awesome-cross-platform-nodejs)

[![GitHub stars](https://img.shields.io/github/stars/bcoe/awesome-cross-platform-nodejs?style=flat)](https://github.com/bcoe/awesome-cross-platform-nodejs/stargazers)

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo_dark.svg"/>
    <img alt="awesome-cross-platform-nodejs logo" src="logo.svg" width="500"/>
  </picture>
  <br>
  <a href="https://awesome.re">
	  <img src="https://awesome.re/badge.svg" alt="Awesome">
  </a>
  <p>A curated list of awesome developer tools for writing cross-platform Node.js code.</p>
</div>

## Contents

- [Resources](#resources)
- [Applications](#applications)
  - [Development environment](#development-environment)
  - [Continuous integration](#continuous-integration)
  - [Virtualization](#virtualization)
  - [Compatibility](#compatibility)
  - [Databases](#databases)
- [Libraries](#libraries)
  - [OS identification](#os-identification)
  - [Shell](#shell)
  - [Environment](#environment)
  - [Filesystem](#filesystem)
  - [Signals](#signals)
  - [Processes](#processes)
  - [Streams](#streams)
  - [Desktop UI](#desktop-ui)
  - [Windows registry](#windows-registry)
- [Known issues](#known-issues)
- [Support](#support)

## Resources

- [Core Node.js documentation](https://nodejs.org/en/docs/) - Especially the [`os`](https://nodejs.org/api/os.html), [`path`](https://nodejs.org/api/path.html), [`fs`](https://nodejs.org/api/fs.html), [`process`](https://nodejs.org/api/process.html) and [`child_process`](https://nodejs.org/api/child_process.html) modules.
- [Cross-platform Node.js guide](https://github.com/ehmicky/cross-platform-node-guide) [![GitHub stars](https://img.shields.io/github/stars/ehmicky/cross-platform-node-guide?style=flat)](https://github.com/ehmicky/cross-platform-node-guide/stargazers) - How to write cross-platform Node.js code.
- [Microsoft Node.js Guidelines](https://github.com/Microsoft/nodejs-guidelines) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/nodejs-guidelines?style=flat)](https://github.com/Microsoft/nodejs-guidelines/stargazers) - Tips, tricks, and resources for working with Node.js on Microsoft platforms.
- [Writing Cross-Platform Node.js](http://shapeshed.com/writing-cross-platform-node/) - Great tutorial covering many common issues that arise when writing cross-platform code: path creation, script execution, newline characters.
- [Cross-platform terminal characters](https://github.com/ehmicky/cross-platform-terminal-characters) [![GitHub stars](https://img.shields.io/github/stars/ehmicky/cross-platform-terminal-characters?style=flat)](https://github.com/ehmicky/cross-platform-terminal-characters/stargazers) - All the characters that work on most terminals and most operating systems.

## Applications

### Development environment

- [Node.js](https://nodejs.org/en/download/) - Node.js installer for various platforms.
- [nvm-windows](https://github.com/coreybutler/nvm-windows) [![GitHub stars](https://img.shields.io/github/stars/coreybutler/nvm-windows?style=flat)](https://github.com/coreybutler/nvm-windows/stargazers) - Manage multiple installations of Node.js on a Windows computer.
- [nvm](https://github.com/creationix/nvm) [![GitHub stars](https://img.shields.io/github/stars/creationix/nvm?style=flat)](https://github.com/creationix/nvm/stargazers) / [n](https://github.com/tj/n) [![GitHub stars](https://img.shields.io/github/stars/tj/n?style=flat)](https://github.com/tj/n/stargazers) - Node version manager for macOS/Linux.
- [npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade) [![GitHub stars](https://img.shields.io/github/stars/felixrieseberg/npm-windows-upgrade?style=flat)](https://github.com/felixrieseberg/npm-windows-upgrade/stargazers) - Upgrade npm on Windows.
- [windows-build-tools](https://github.com/felixrieseberg/windows-build-tools) [![GitHub stars](https://img.shields.io/github/stars/felixrieseberg/windows-build-tools?style=flat)](https://github.com/felixrieseberg/windows-build-tools/stargazers) - Install C++ Build Tools for Windows using npm.

### Continuous integration

- [AppVeyor](http://www.appveyor.com/) - Focused on Windows. Free tiers are available for OSS projects.
- [Travis](https://travis-ci.org/) - Windows/macOS/Linux. Free for OSS projects.
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) - Windows/macOS/Linux. Free for OSS projects with 10 parallel jobs.
- [Github Action](https://github.com/features/actions) - Windows/macOS/Linux. GitHub Actions makes it easy to automate all your software workflows.
- [Gitlab CI](https://docs.gitlab.com/ee/ci/) - Windows/macOS/Linux. GitLab CI/CD is a tool built into GitLab for software development.

### Virtualization

- [ievms](https://github.com/amichaelparker/ievms) [![GitHub stars](https://img.shields.io/github/stars/amichaelparker/ievms?style=flat)](https://github.com/amichaelparker/ievms/stargazers) - Automated installer for the free virtual machine images that Microsoft provides for testing on multiple versions of IE. These images can be useful for cross-platform testing various technologies, however make sure you read and understand Microsofts' licensing.
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - General purpose software for running x86 virtual machines.
- [Docker](https://www.docker.com/) - Software platform to create, deploy and manage virtualized application containers on a common operating system, with an ecosystem of allied tools.

### Compatibility

- [Wine](https://www.winehq.org/) - Run Windows API calls on Linux, Mac, BSD and Solaris.
- [Cygwin](https://www.cygwin.com/) - Run POSIX on Windows.
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) - Run the Linux command line on Windows (ELF binary execution, system calls, filesystem, Bash, core utilities, common applications).
- [MinGW](http://www.mingw.org/) - `gcc` on Windows.
- [msys](http://www.mingw.org/wiki/msys) / [Git Bash](https://gitforwindows.org/) - Bash on Windows.

### Databases

- [Redis](https://github.com/tporadowski/redis) [![GitHub stars](https://img.shields.io/github/stars/tporadowski/redis?style=flat)](https://github.com/tporadowski/redis/stargazers) - Native port of Redis for Windows.

## Libraries

### OS identification

- [is-windows](https://github.com/jonschlinkert/is-windows) [![GitHub stars](https://img.shields.io/github/stars/jonschlinkert/is-windows?style=flat)](https://github.com/jonschlinkert/is-windows/stargazers) - Detect whether the current platform is Windows.
- [is-wsl](https://github.com/sindresorhus/is-wsl) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/is-wsl?style=flat)](https://github.com/sindresorhus/is-wsl/stargazers) - Detect whether current platform is WSL (Windows Subsystem for Linux).
- [getos](https://github.com/retrohacker/getos) [![GitHub stars](https://img.shields.io/github/stars/retrohacker/getos?style=flat)](https://github.com/retrohacker/getos/stargazers) - Retrieve the current OS, including Linux distribution.
- [os-name](https://github.com/sindresorhus/os-name) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/os-name?style=flat)](https://github.com/sindresorhus/os-name/stargazers) - Get the name of the current operating system.
- [systeminformation](https://github.com/sebhildebrandt/systeminformation) [![GitHub stars](https://img.shields.io/github/stars/sebhildebrandt/systeminformation?style=flat)](https://github.com/sebhildebrandt/systeminformation/stargazers) - Hardware/software system information.

### Shell

- [execa](https://github.com/sindresorhus/execa) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/execa?style=flat)](https://github.com/sindresorhus/execa/stargazers) - Cross-platform implementation of `child_process.{execFile,exec}`.
- [gulp-execa](https://github.com/ehmicky/gulp-execa) [![GitHub stars](https://img.shields.io/github/stars/ehmicky/gulp-execa?style=flat)](https://github.com/ehmicky/gulp-execa/stargazers) - Cross-platform command execution in Gulp.js.
- [cross-spawn](https://github.com/IndigoUnited/node-cross-spawn) [![GitHub stars](https://img.shields.io/github/stars/IndigoUnited/node-cross-spawn?style=flat)](https://github.com/IndigoUnited/node-cross-spawn/stargazers) - Cross-platform implementation of `child_process.spawn()`.
- [shelljs](https://github.com/shelljs/shelljs) [![GitHub stars](https://img.shields.io/github/stars/shelljs/shelljs?style=flat)](https://github.com/shelljs/shelljs/stargazers) - Cross-platform Unix shell commands.
- [node-windows](https://github.com/coreybutler/node-windows) [![GitHub stars](https://img.shields.io/github/stars/coreybutler/node-windows?style=flat)](https://github.com/coreybutler/node-windows/stargazers) - Windows support for Node.js scripts (daemons, eventlog, UAC, etc).
- [log-symbols](https://github.com/sindresorhus/log-symbols) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/log-symbols?style=flat)](https://github.com/sindresorhus/log-symbols/stargazers) - Colored symbols for various log levels with Windows fallbacks.
- [figures](https://github.com/sindresorhus/figures) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/figures?style=flat)](https://github.com/sindresorhus/figures/stargazers) - Unicode symbols with Windows fallbacks.
- [clipboardy](https://github.com/sindresorhus/clipboardy) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/clipboardy?style=flat)](https://github.com/sindresorhus/clipboardy/stargazers) / [clipboard-cli](https://github.com/sindresorhus/clipboard-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/clipboard-cli?style=flat)](https://github.com/sindresorhus/clipboard-cli/stargazers) - Cross-platform copy/paste.

### Environment

- [cross-env](https://github.com/kentcdodds/cross-env) [![GitHub stars](https://img.shields.io/github/stars/kentcdodds/cross-env?style=flat)](https://github.com/kentcdodds/cross-env/stargazers) - Set environment variables cross-platform.
- [user-home](https://github.com/sindresorhus/user-home) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/user-home?style=flat)](https://github.com/sindresorhus/user-home/stargazers) - Get the path to the user home directory. Cross-platform.
- [username](https://github.com/sindresorhus/username) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/username?style=flat)](https://github.com/sindresorhus/username/stargazers) - Get the current username.
- [osenv](https://github.com/npm/osenv) [![GitHub stars](https://img.shields.io/github/stars/npm/osenv?style=flat)](https://github.com/npm/osenv/stargazers) - Cross-platform environment variables.
- [is-elevated](https://github.com/sindresorhus/is-elevated) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/is-elevated?style=flat)](https://github.com/sindresorhus/is-elevated/stargazers) - Check if the process is running with elevated privileges.
- [which](https://github.com/npm/node-which) [![GitHub stars](https://img.shields.io/github/stars/npm/node-which?style=flat)](https://github.com/npm/node-which/stargazers) - Cross-platform implementation of Unix's `which`.

### Filesystem

- [rimraf](https://github.com/isaacs/rimraf) [![GitHub stars](https://img.shields.io/github/stars/isaacs/rimraf?style=flat)](https://github.com/isaacs/rimraf/stargazers) / [del](https://github.com/sindresorhus/del) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/del?style=flat)](https://github.com/sindresorhus/del/stargazers) - Delete files and folders. Cross-platform.
- [make-dir](https://github.com/sindresorhus/make-dir) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/make-dir?style=flat)](https://github.com/sindresorhus/make-dir/stargazers) - Cross-platform `mkdir -p`.
- [readdirp](https://github.com/paulmillr/readdirp) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/readdirp?style=flat)](https://github.com/paulmillr/readdirp/stargazers) - Recursive version of `fs.readdir()`.
- [cpy](https://github.com/sindresorhus/cpy) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/cpy?style=flat)](https://github.com/sindresorhus/cpy/stargazers) - Copy files. Cross-platform.
- [chokidar](https://github.com/paulmillr/chokidar) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/chokidar?style=flat)](https://github.com/paulmillr/chokidar/stargazers) - Improved cross-platform file watching.
- [graceful-fs](https://github.com/isaacs/node-graceful-fs) [![GitHub stars](https://img.shields.io/github/stars/isaacs/node-graceful-fs?style=flat)](https://github.com/isaacs/node-graceful-fs/stargazers) - Improves the `fs` module, especially on Windows.
- [fs-extra](https://github.com/jprichardson/node-fs-extra) [![GitHub stars](https://img.shields.io/github/stars/jprichardson/node-fs-extra?style=flat)](https://github.com/jprichardson/node-fs-extra/stargazers) - Combines `graceful-fs` with better JSON file reading and promises.
- [any-path](https://github.com/bcoe/any-path) [![GitHub stars](https://img.shields.io/github/stars/bcoe/any-path?style=flat)](https://github.com/bcoe/any-path/stargazers) - Use Windows and POSIX paths interchangeably when fetching values from an object.
- [dev-null-cli](https://github.com/sindresorhus/dev-null-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/dev-null-cli?style=flat)](https://github.com/sindresorhus/dev-null-cli/stargazers) - Cross-platform `/dev/null`.
- [global-cache-dir](https://github.com/ehmicky/global-cache-dir) [![GitHub stars](https://img.shields.io/github/stars/ehmicky/global-cache-dir?style=flat)](https://github.com/ehmicky/global-cache-dir/stargazers) - Get the global OS-specific cache directory.

### Signals

- [fkill](https://github.com/sindresorhus/fkill) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/fkill?style=flat)](https://github.com/sindresorhus/fkill/stargazers) - Kill processes. Cross-platform.
- [signal-exit](https://github.com/tapjs/signal-exit) [![GitHub stars](https://img.shields.io/github/stars/tapjs/signal-exit?style=flat)](https://github.com/tapjs/signal-exit/stargazers) - Cross-platform `exit` handler.
- [human-signals](https://github.com/ehmicky/human-signals) [![GitHub stars](https://img.shields.io/github/stars/ehmicky/human-signals?style=flat)](https://github.com/ehmicky/human-signals/stargazers) - Human-friendly process signals.

### Processes

- [ps-list](https://github.com/sindresorhus/ps-list) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/ps-list?style=flat)](https://github.com/sindresorhus/ps-list/stargazers) - Get running processes.
- [process-exists](https://github.com/sindresorhus/process-exists) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/process-exists?style=flat)](https://github.com/sindresorhus/process-exists/stargazers) - Check if a process exists.

### Streams

- [noop-stream](https://github.com/sindresorhus/noop-stream) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/noop-stream?style=flat)](https://github.com/sindresorhus/noop-stream/stargazers) - Cross-platform `fs.createReadStream('/dev/null')`.
- [random-bytes-readable-stream](https://github.com/sindresorhus/random-bytes-readable-stream) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/random-bytes-readable-stream?style=flat)](https://github.com/sindresorhus/random-bytes-readable-stream/stargazers) - Cross-platform `fs.createReadStream('/dev/urandom')`.

### Desktop UI

- [open](https://github.com/sindresorhus/open) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/open?style=flat)](https://github.com/sindresorhus/open/stargazers) - Opens stuff like websites, files, executables. Cross-platform.
- [node-notifier](https://github.com/mikaelbr/node-notifier) [![GitHub stars](https://img.shields.io/github/stars/mikaelbr/node-notifier?style=flat)](https://github.com/mikaelbr/node-notifier/stargazers) - Cross-platform desktop notifications.

### Windows registry

- [node-winreg](https://github.com/fresc81/node-winreg) [![GitHub stars](https://img.shields.io/github/stars/fresc81/node-winreg?style=flat)](https://github.com/fresc81/node-winreg/stargazers) - Access the Windows registry.
- [rage-edit](https://github.com/MikeKovarik/rage-edit) [![GitHub stars](https://img.shields.io/github/stars/MikeKovarik/rage-edit?style=flat)](https://github.com/MikeKovarik/rage-edit/stargazers) - Access/modify the Windows registry.
- [windows-registry-node](https://github.com/CatalystCode/windows-registry-node) [![GitHub stars](https://img.shields.io/github/stars/CatalystCode/windows-registry-node?style=flat)](https://github.com/CatalystCode/windows-registry-node/stargazers) - Access/modify the Windows registry and set file associations.

## Known issues

- [cmd.exe unicode woes](https://github.com/nodejs/node-v0.x-archive/issues/7940) [![GitHub stars](https://img.shields.io/github/stars/nodejs/node-v0.x-archive/issues/7940?style=flat)](https://github.com/nodejs/node-v0.x-archive/issues/7940/stargazers) - By default, `cmd.exe` does not display Unicode characters on Windows.
- [spawn issues](https://github.com/nodejs/node-v0.x-archive/issues/2318) [![GitHub stars](https://img.shields.io/github/stars/nodejs/node-v0.x-archive/issues/2318?style=flat)](https://github.com/nodejs/node-v0.x-archive/issues/2318/stargazers) - `child_process.spawn()` behavior is not consistent between Windows and Linux.
- [exec() behavior between shells](https://github.com/isaacs/spawn-wrap#contracts-and-caveats) [![GitHub stars](https://img.shields.io/github/stars/isaacs/spawn-wrap?style=flat)](https://github.com/isaacs/spawn-wrap/stargazers) - Depending on the shell being used, e.g., bash vs. dash, `child_process.exec()` has inconsistent exit behavior.

## See also

- [awesome-desktop-js](https://github.com/styfle/awesome-desktop-js) [![GitHub stars](https://img.shields.io/github/stars/styfle/awesome-desktop-js?style=flat)](https://github.com/styfle/awesome-desktop-js/stargazers) - List of tools to build JavaScript applications on the desktop.

## Support

If you found an error or would like to add more information, _don't hesitate_ to
[submit an issue on GitHub](../../issues).

Everyone is welcome regardless of personal background. We enforce a
[Code of conduct](CODE_OF_CONDUCT.md) in order to promote a positive and
inclusive environment.

## Contributing

This project was made with ❤️. The simplest way to give back is by starring and
sharing it online.

If the documentation is unclear or has a typo, please click on the page's `Edit`
button (pencil icon) and suggest a correction.

If you would like to help us fix an error or add more information, please check
our [guidelines](contributing.md). Pull requests are welcome!

Thanks go to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="https://twitter.com/benjamincoe"><img src="https://avatars3.githubusercontent.com/u/194609?v=4" width="100px;" alt="Benjamin E. Coe"/><br /><sub><b>Benjamin E. Coe</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=bcoe" title="Code">💻</a> <a href="#ideas-bcoe" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=bcoe" title="Documentation">📖</a></td><td align="center"><a href="https://twitter.com/ehmicky"><img src="https://avatars2.githubusercontent.com/u/8136211?v=4" width="100px;" alt="ehmicky"/><br /><sub><b>ehmicky</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=ehmicky" title="Code">💻</a> <a href="#ideas-ehmicky" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=ehmicky" title="Documentation">📖</a></td><td align="center"><a href="https://sindresorhus.com"><img src="https://avatars1.githubusercontent.com/u/170270?v=4" width="100px;" alt="Sindre Sorhus"/><br /><sub><b>Sindre Sorhus</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=sindresorhus" title="Code">💻</a> <a href="#ideas-sindresorhus" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=sindresorhus" title="Documentation">📖</a></td><td align="center"><a href="https://fb.com/RemoveU"><img src="https://avatars1.githubusercontent.com/u/19208123?v=4" width="100px;" alt="Hongarc"/><br /><sub><b>Hongarc</b></sub></a><br /><a href="#design-Hongarc" title="Design">🎨</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Hongarc" title="Documentation">📖</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Hongarc" title="Code">💻</a></td><td align="center"><a href="https://kentcdodds.com"><img src="https://avatars0.githubusercontent.com/u/1500684?v=4" width="100px;" alt="Kent C. Dodds"/><br /><sub><b>Kent C. Dodds</b></sub></a><br /><a href="#ideas-kentcdodds" title="Ideas, Planning, & Feedback">🤔</a></td><td align="center"><a href="https://nz.linkedin.com/in/jsonc11"><img src="https://avatars0.githubusercontent.com/u/5185660?v=4" width="100px;" alt="Jason Cooke"/><br /><sub><b>Jason Cooke</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Jason-Cooke" title="Documentation">📖</a></td><td align="center"><a href="http://aronhafner.com"><img src="https://avatars0.githubusercontent.com/u/3322693?v=4" width="100px;" alt="Aron Hafner"/><br /><sub><b>Aron Hafner</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=alonalon" title="Documentation">📖</a></td></tr><tr><td align="center"><a href="https://github.com/ShPelles"><img src="https://avatars0.githubusercontent.com/u/43875468?v=4" width="100px;" alt="ShPelles"/><br /><sub><b>ShPelles</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=ShPelles" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/Frederick-S"><img src="https://avatars1.githubusercontent.com/u/1182395?v=4" width="100px;" alt="Xiaodan Mao"/><br /><sub><b>Xiaodan Mao</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Frederick-S" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/jamestalmage"><img src="https://avatars0.githubusercontent.com/u/4082216?v=4" width="100px;" alt="James Talmage"/><br /><sub><b>James Talmage</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=jamestalmage" title="Documentation">📖</a></td><td align="center"><a href="http://sylvain.pontoreau.com"><img src="https://avatars3.githubusercontent.com/u/3357643?v=4" width="100px;" alt="Sylvain PONTOREAU"/><br /><sub><b>Sylvain PONTOREAU</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=spontoreau" title="Documentation">📖</a></td><td align="center"><a href="https://www.ceriously.com"><img src="https://avatars1.githubusercontent.com/u/229881?v=4" width="100px;" alt="Steven"/><br /><sub><b>Steven</b></sub></a><br /><a href="#ideas-styfle" title="Ideas, Planning, & Feedback">🤔</a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) [![GitHub stars](https://img.shields.io/github/stars/all-contributors/all-contributors?style=flat)](https://github.com/all-contributors/all-contributors/stargazers) specification.

## License

[![License](https://img.shields.io/github/license/bcoe/awesome-cross-platform-nodejs.svg?color=4cc61e&logo=github)](https://creativecommons.org/licenses/by-sa/4.0/)
