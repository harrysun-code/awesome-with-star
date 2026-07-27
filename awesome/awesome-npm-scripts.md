# npm scripts

> 来源：[RyanZim/awesome-npm-scripts](https://github.com/RyanZim/awesome-npm-scripts)

[![GitHub stars](https://img.shields.io/github/stars/RyanZim/awesome-npm-scripts?style=flat)](https://github.com/RyanZim/awesome-npm-scripts/stargazers)

<!--lint ignore awesome-heading-->
# Awesome npm Scripts [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="npm-logo.png" align="right" width="150">](https://www.npmjs.com)

> Everything awesome for using npm as a build tool.

You might also like [awesome-npm](https://github.com/sindresorhus/awesome-npm) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome-npm?style=flat)](https://github.com/sindresorhus/awesome-npm/stargazers).

**Notice: I'm currently too busy to actively expand this list; therefore, I've decided to make this an [OPEN Open Source Project](http://openopensource.github.io/). Individuals making significant and valuable contributions are given commit-access to the project to contribute as they see fit.**

## Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Articles](#articles)
- [Videos/Talks](#videostalks)
- [Task Runners](#task-runners)
- [File Watchers](#file-watchers)
- [Dev Servers](#dev-servers)
- [Cross-platform Utilities](#cross-platform-utilities)
  - [Utility Packs](#utility-packs)
- [Other Utilities](#other-utilities)
- [Miscellaneous](#miscellaneous)
- [Cross-platform Shell Reference](#cross-platform-shell-reference)
- [`npm run` Reference](#npm-run-reference)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Articles

- [Why we should stop using Grunt & Gulp](https://www.keithcirkel.co.uk/why-we-should-stop-using-grunt/) - Blog post by Keith Cirkel.
- [How to Use npm as a Build Tool](https://www.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/) - Sequel to »Why we should stop using Grunt & Gulp«.
- [Why I Left Gulp and Grunt for npm Scripts](https://medium.freecodecamp.com/why-i-left-gulp-and-grunt-for-npm-scripts-3d6853dd22b8) -  Article by Cory House.
- [Helpers and tips for npm run scripts](http://michael-kuehnel.de/tooling/2018/03/22/helpers-and-tips-for-npm-run-scripts.html) - Blog post by Michael Kühnel covering advanced topics.
- [Running cross-platform tasks via npm package scripts](https://exploringjs.com/nodejs-shell-scripting/ch_package-scripts.html) - The most comprehensive guide to using npm Scripts by Dr. Axel Rauschmayer.

## Videos/Talks

- [Advanced front-end automation with npm scripts](https://www.youtube.com/watch?v=0RYETb9YVrk) - Talk at Nordic.js 2015 by Kate Hudson.
- [How to create a build system with npm scripts](http://www.penta-code.com/how-to-create-a-build-system-with-npm-scripts/) - Video tutorial series on setting up a front-end build system.

## Task Runners

Tools for running multiple commands or npm scripts in parallel or sequentially.

- [script-runner](https://github.com/paulpflug/script-runner) [![GitHub stars](https://img.shields.io/github/stars/paulpflug/script-runner?style=flat)](https://github.com/paulpflug/script-runner/stargazers) - Simple task runner with a terse syntax.
- [npm-run-all2](https://github.com/bcomnes/npm-run-all2) [![GitHub stars](https://img.shields.io/github/stars/bcomnes/npm-run-all2?style=flat)](https://github.com/bcomnes/npm-run-all2/stargazers) - Fully featured task runner.
- [redrun](https://github.com/coderaiser/redrun) [![GitHub stars](https://img.shields.io/github/stars/coderaiser/redrun?style=flat)](https://github.com/coderaiser/redrun/stargazers) - Expand scripts from package.json to improve execution speed.

## File Watchers

Tools to watch your source files and run a build command whenever any of the files change.

- [onchange](https://github.com/Qard/onchange) [![GitHub stars](https://img.shields.io/github/stars/Qard/onchange?style=flat)](https://github.com/Qard/onchange/stargazers) - `onchange <glob> -- <command>`.
- [watch](https://github.com/mikeal/watch) [![GitHub stars](https://img.shields.io/github/stars/mikeal/watch?style=flat)](https://github.com/mikeal/watch/stargazers) - `watch <command> <directory>`.

## Dev Servers

- [http-server](https://github.com/indexzero/http-server) [![GitHub stars](https://img.shields.io/github/stars/indexzero/http-server?style=flat)](https://github.com/indexzero/http-server/stargazers) - Simple zero-configuration command-line http server.
- [live-server](https://github.com/tapio/live-server) [![GitHub stars](https://img.shields.io/github/stars/tapio/live-server?style=flat)](https://github.com/tapio/live-server/stargazers) - Simple development http server with live reload capability.

## Cross-platform Utilities

Utilities to perform common command-line tasks without worrying about cross-platform compatibility.

- [rimraf](https://github.com/isaacs/rimraf) [![GitHub stars](https://img.shields.io/github/stars/isaacs/rimraf?style=flat)](https://github.com/isaacs/rimraf/stargazers) - Delete files or directories; like `rm -rf`.
- [del-cli](https://github.com/sindresorhus/del-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/del-cli?style=flat)](https://github.com/sindresorhus/del-cli/stargazers) - Safer file and folder deletion.
- [mkdirp](https://github.com/substack/node-mkdirp) [![GitHub stars](https://img.shields.io/github/stars/substack/node-mkdirp?style=flat)](https://github.com/substack/node-mkdirp/stargazers) - Create a directory, creating parent directories if needed; like `mkdir -p`.
- [cpr](https://github.com/davglass/cpr) [![GitHub stars](https://img.shields.io/github/stars/davglass/cpr?style=flat)](https://github.com/davglass/cpr/stargazers) - `cp -r` for Node.js.
- [cpy-cli](https://github.com/sindresorhus/cpy-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/cpy-cli?style=flat)](https://github.com/sindresorhus/cpy-cli/stargazers) - File/directory copying/renaming.
- [copyfiles](https://github.com/calvinmetcalf/copyfiles) [![GitHub stars](https://img.shields.io/github/stars/calvinmetcalf/copyfiles?style=flat)](https://github.com/calvinmetcalf/copyfiles/stargazers) - Copy a list of files into a directory.
- [sync-files](https://github.com/byteclubfr/node-sync-files) [![GitHub stars](https://img.shields.io/github/stars/byteclubfr/node-sync-files?style=flat)](https://github.com/byteclubfr/node-sync-files/stargazers) - `rsync`-like directory syncing with watch mode.
- [echo-cli](https://github.com/iamakulov/echo-cli) [![GitHub stars](https://img.shields.io/github/stars/iamakulov/echo-cli?style=flat)](https://github.com/iamakulov/echo-cli/stargazers) - Cross-platform `echo` with JS escape sequence support.
- [clear-cli](https://github.com/sindresorhus/clear-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/clear-cli?style=flat)](https://github.com/sindresorhus/clear-cli/stargazers) - Clear the terminal.
- [cross-env](https://github.com/kentcdodds/cross-env) [![GitHub stars](https://img.shields.io/github/stars/kentcdodds/cross-env?style=flat)](https://github.com/kentcdodds/cross-env/stargazers) - Set environment variables for scripts, unix-style.
- [cross-os](https://github.com/milewski/cross-os) [![GitHub stars](https://img.shields.io/github/stars/milewski/cross-os?style=flat)](https://github.com/milewski/cross-os/stargazers) - Run platform-specific npm scripts.
- [ntee](https://github.com/stefanmaric/ntee) [![GitHub stars](https://img.shields.io/github/stars/stefanmaric/ntee?style=flat)](https://github.com/stefanmaric/ntee/stargazers) - Utility that reads from standard input and writes to standard output and files; like Unix `tee`.
- [catw](https://github.com/substack/catw) [![GitHub stars](https://img.shields.io/github/stars/substack/catw?style=flat)](https://github.com/substack/catw/stargazers) - Print a file to stdout, with optional watch mode; sorta like Unix `cat`.

### Utility Packs

- [shx](https://github.com/shelljs/shx) [![GitHub stars](https://img.shields.io/github/stars/shelljs/shx?style=flat)](https://github.com/shelljs/shx/stargazers) - Collection of common Unix utilities implemented in Node.js; example usage: `shx rm somefile`.

## Other Utilities

- [hashmark](https://github.com/keithamus/hashmark) [![GitHub stars](https://img.shields.io/github/stars/keithamus/hashmark?style=flat)](https://github.com/keithamus/hashmark/stargazers) -  Take contents of a file and output as new file with a hash in the name.
- [gzip-size-cli](https://github.com/sindresorhus/gzip-size-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/gzip-size-cli?style=flat)](https://github.com/sindresorhus/gzip-size-cli/stargazers) - Get the gzipped size of a file or stdin.
- [opn-cli](https://github.com/sindresorhus/opn-cli) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/opn-cli?style=flat)](https://github.com/sindresorhus/opn-cli/stargazers) - Open websites, files, executables, etc. with the user's preferred application.
- [headr](https://github.com/heldr/headr) [![GitHub stars](https://img.shields.io/github/stars/heldr/headr?style=flat)](https://github.com/heldr/headr/stargazers) - Add header / banner info to a file.
- [Bower files CLI](https://github.com/thompsonemerson/bower-files-cli) [![GitHub stars](https://img.shields.io/github/stars/thompsonemerson/bower-files-cli?style=flat)](https://github.com/thompsonemerson/bower-files-cli/stargazers) - Get main bower files on the command line.
- [cli-error-notifier](https://github.com/micromata/cli-error-notifier) [![GitHub stars](https://img.shields.io/github/stars/micromata/cli-error-notifier?style=flat)](https://github.com/micromata/cli-error-notifier/stargazers) - Send native desktop notifications when npm scripts fail.

## Miscellaneous

- [screwy](https://github.com/samueleaton/screwy) [![GitHub stars](https://img.shields.io/github/stars/samueleaton/screwy?style=flat)](https://github.com/samueleaton/screwy/stargazers) - The npm scripts GUI.
- [Forrest](https://github.com/stefanjudis/forrest) [![GitHub stars](https://img.shields.io/github/stars/stefanjudis/forrest?style=flat)](https://github.com/stefanjudis/forrest/stargazers) - npm scripts desktop client.
- [run-npm](https://github.com/timoxley/npm-run) [![GitHub stars](https://img.shields.io/github/stars/timoxley/npm-run?style=flat)](https://github.com/timoxley/npm-run/stargazers) - Run locally-installed node module executables. Useful for debugging npm scripts.
- [npm-quick-run](https://github.com/bahmutov/npm-quick-run) [![GitHub stars](https://img.shields.io/github/stars/bahmutov/npm-quick-run?style=flat)](https://github.com/bahmutov/npm-quick-run/stargazers) - Quickly run npm scripts by prefix without typing the full name.
- [edit-script](https://github.com/RyanZim/edit-script) [![GitHub stars](https://img.shields.io/github/stars/RyanZim/edit-script?style=flat)](https://github.com/RyanZim/edit-script/stargazers) - Edit npm scripts from the command line without worrying about JSON escaping.
- [ntl](https://github.com/ruyadorno/ntl) [![GitHub stars](https://img.shields.io/github/stars/ruyadorno/ntl?style=flat)](https://github.com/ruyadorno/ntl/stargazers) - Interactive cli menu to list and run npm scripts.

## Cross-platform Shell Reference

A quick reference of the shell operators & commands that work the same on Unix and Windows.

- Use `&&` to run commands in sequence. If a command fails, the script exits.
- Use `|` to pipe the stdout of one command into the stdin of the next. (`do-something | something else`)
- Use `>` to write the stdout of a command to a file. (`do-something > file`)
- Use `<` to send the contents of a file to a command's stdin. (`command < file`)
- Use `cd <dir>` to change the current working directory to `<dir>`. Note that `cd` alone prints the current working directory on windows, but changes the working directory to `~` on \*nix.

## `npm run` Reference

You can use `npm run-script` or `npm run`; they both do the same thing, but `npm run` is shorter.

- Run just `npm run` to print a list of scripts.
- Running `npm run script` (where `script` is the name of your script) will run `prescript`, `script`, and `postscript`; in that order.
  - You can't nest `pre` and `post` hooks (i.e. `preprescript` won't work).
- You can pass arguments to your scripts by passing `--` to `npm run`, followed by the arguments. Example: Given the script `"mocha": "mocha"`, you can run `npm run mocha -- --reporter xunit`. This effectively runs `mocha --reporter xunit`.
- Running `npm test` is the same as running `npm run test`. The same applies to `npm start` and `npm stop`.
- You can run `npm run <script> -s` to silence the default npm output (useful for calling a script within another script).

## Contributing

See [CONTRIBUTING.md](https://github.com/RyanZim/awesome-npm-scripts/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/RyanZim/awesome-npm-scripts/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/RyanZim/awesome-npm-scripts/blob/master/CONTRIBUTING.md/stargazers).
