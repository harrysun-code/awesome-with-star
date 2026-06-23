# Composer

[![GitHub stars](https://img.shields.io/github/stars/jakoch/awesome-composer?style=flat)](https://github.com/jakoch/awesome-composer/stargazers)

<!--lint disable double-link awesome-toc-->
# Awesome Composer [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome) [![Build on Windows](https://github.com/jakoch/awesome-composer/actions/workflows/awesome-bot.yml/badge.svg?branch=main)](https://github.com/jakoch/awesome-composer/actions/workflows/awesome-bot.yml) [![license](https://img.shields.io/github/license/jakoch/awesome-composer.svg?maxAge=2592000)]()

[<img src="https://raw.githubusercontent.com/jakoch/awesome-composer/master/logo-composer-transparent.png" align="right" width="150">](https://getcomposer.org/)

> A curated list of resources for Composer, Packagist, Satis, Plugins, Scripts, Videos, Tutorials.

You might also like [awesome-php](https://github.com/ziadoz/awesome-php) [![GitHub stars](https://img.shields.io/github/stars/ziadoz/awesome-php?style=flat)](https://github.com/ziadoz/awesome-php/stargazers).

*Please read the [contribution guidelines](https://github.com/jakoch/awesome-composer/blob/main/.github/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/jakoch/awesome-composer/blob/main/.github/CONTRIBUTING.md?style=flat)](https://github.com/jakoch/awesome-composer/blob/main/.github/CONTRIBUTING.md/stargazers) before contributing.*

## Composer

- [Official Website](https://getcomposer.org/)
- [GitHub](https://github.com/composer/composer) [![GitHub stars](https://img.shields.io/github/stars/composer/composer?style=flat)](https://github.com/composer/composer/stargazers)
- [Issues](https://github.com/composer/composer/issues) [![GitHub stars](https://img.shields.io/github/stars/composer/composer/issues?style=flat)](https://github.com/composer/composer/issues/stargazers)
- [Source](https://github.com/composer/composer/tree/HEAD/src/Composer) [![GitHub stars](https://img.shields.io/github/stars/composer/composer/tree/HEAD/src/Composer?style=flat)](https://github.com/composer/composer/tree/HEAD/src/Composer/stargazers)
- [Documentation](https://getcomposer.org/doc/)
- [Getting Started Guide and Installation Instructions](https://getcomposer.org/doc/00-intro.md)
- [Find Packages on Packagist](https://packagist.org/)
- [CheatSheet](https://composer.json.jolicode.com/) - Overview of CLI commands and `composer.json` schema.
- [Composer Installers](https://github.com/composer/installers) [![GitHub stars](https://img.shields.io/github/stars/composer/installers?style=flat)](https://github.com/composer/installers/stargazers) - Composer installers for multiple frameworks.

### Support

#### Stack Overflow

- You might use the following tags: `composer-php`, `packagist`, `satis` + `php`.
- [Ask a new question](https://stackoverflow.com/questions/ask?tags=composer-php+php)
- [Find questions tagged `composer-php`](https://stackoverflow.com/questions/tagged/composer-php)

#### IRC

- IRC channels are on `irc.freenode.org`: [#composer](https://irc.com/#composer) for users and [#composer-dev](https://irc.com/#composer-dev) for development.

---

## Plugins

- [Documentation for Plugins](https://getcomposer.org/doc/articles/plugins.md) - This offical documentation is good starting point, when writing a Composer plugin.
- [Composer-Asset-Plugin](https://github.com/fxpio/composer-asset-plugin) [![GitHub stars](https://img.shields.io/github/stars/fxpio/composer-asset-plugin?style=flat)](https://github.com/fxpio/composer-asset-plugin/stargazers) - A npm/Bower Dependencies Manager for Composer.
- [Composer-AWS](https://github.com/naderman/composer-aws) [![GitHub stars](https://img.shields.io/github/stars/naderman/composer-aws?style=flat)](https://github.com/naderman/composer-aws/stargazers) - The plugin loads repository data and downloads packages from Amazon S3 (with authentication support for private repositories).
- [Composer-Composition](https://github.com/bamarni/composition) [![GitHub stars](https://img.shields.io/github/stars/bamarni/composition?style=flat)](https://github.com/bamarni/composition/stargazers) - Provides an API, for checking your environment at runtime.
- [Composer-Suggest](https://github.com/nfreear/composer-suggest) [![GitHub stars](https://img.shields.io/github/stars/nfreear/composer-suggest?style=flat)](https://github.com/nfreear/composer-suggest/stargazers) - Enables you to install a custom group of suggested packages, based on keyword patterns.
- [Composer-Versions-Check](https://github.com/Soullivaneuh/composer-versions-check) [![GitHub stars](https://img.shields.io/github/stars/Soullivaneuh/composer-versions-check?style=flat)](https://github.com/Soullivaneuh/composer-versions-check/stargazers) - Shows outdated packages from last major versions after using the update command (showing "Latest is vX.Y.Z").
- [Composer-Changelogs](https://github.com/pyrech/composer-changelogs) [![GitHub stars](https://img.shields.io/github/stars/pyrech/composer-changelogs?style=flat)](https://github.com/pyrech/composer-changelogs/stargazers) - Provides a summary of the updates with links to changelog/releasenote/tag. The output is ready to be pasted into the commit message when updating the composer.lock file.
- [Composer-Merge-Plugin](https://github.com/wikimedia/composer-merge-plugin) [![GitHub stars](https://img.shields.io/github/stars/wikimedia/composer-merge-plugin?style=flat)](https://github.com/wikimedia/composer-merge-plugin/stargazers) - Merges multiple `composer.json` files at Composer runtime.
- [Composer-Bin-Plugin](https://github.com/bamarni/composer-bin-plugin) [![GitHub stars](https://img.shields.io/github/stars/bamarni/composer-bin-plugin?style=flat)](https://github.com/bamarni/composer-bin-plugin/stargazers) - Adds support for managing dependencies for multiple packages in a single repository or isolate bin dependencies.
- [Composer-Inheritance-Plugin](https://github.com/theofidry/composer-inheritance-plugin) [![GitHub stars](https://img.shields.io/github/stars/theofidry/composer-inheritance-plugin?style=flat)](https://github.com/theofidry/composer-inheritance-plugin/stargazers) - Opinionated version of Wikimedia composer-merge-plugin to work in pair with Bamarni composer-bin-plugin.
- [Composer-MonoRepo-Plugin](https://github.com/beberlei/composer-monorepo-plugin) [![GitHub stars](https://img.shields.io/github/stars/beberlei/composer-monorepo-plugin?style=flat)](https://github.com/beberlei/composer-monorepo-plugin/stargazers) - The plugin helps to manage dependencies for multiple packages in a single repository.
- [Composer-Patches-Plugin](https://github.com/netresearch/composer-patches-plugin) [![GitHub stars](https://img.shields.io/github/stars/netresearch/composer-patches-plugin?style=flat)](https://github.com/netresearch/composer-patches-plugin/stargazers) - Enables you to provide patches for any package from any package. When the dependency is fetched, the patch is applied on top.
- [Composer-Patches](https://github.com/cweagans/composer-patches) [![GitHub stars](https://img.shields.io/github/stars/cweagans/composer-patches?style=flat)](https://github.com/cweagans/composer-patches/stargazers) - The plugin applies a patch from a local or remote file to any required package.
- [Composer-Patches](https://github.com/vaimo/composer-patches) [![GitHub stars](https://img.shields.io/github/stars/vaimo/composer-patches?style=flat)](https://github.com/vaimo/composer-patches/stargazers) - Applies a patch from a local or remote file to any package that is part of a given composer project.
- [Composer-Patchset](https://github.com/mageops/php-composer-plugin-patchset) [![GitHub stars](https://img.shields.io/github/stars/mageops/php-composer-plugin-patchset?style=flat)](https://github.com/mageops/php-composer-plugin-patchset/stargazers) - Automatically fetch, update and apply patches to any composer package with a twist - store the patchset as a composer package itself.
- [Composer-Plugin-QA](https://github.com/Webysther/composer-plugin-qa) [![GitHub stars](https://img.shields.io/github/stars/Webysther/composer-plugin-qa?style=flat)](https://github.com/Webysther/composer-plugin-qa/stargazers) - Comprehensive Plugin for composer to execute PHP Quality assurance Tools.
- [Composer-Cleanup-Plugin](https://github.com/barryvdh/composer-cleanup-plugin) [![GitHub stars](https://img.shields.io/github/stars/barryvdh/composer-cleanup-plugin?style=flat)](https://github.com/barryvdh/composer-cleanup-plugin/stargazers) - Removes tests & documentation folders from the vendor dir.
- [Composer-Cleaner](https://github.com/dg/composer-cleaner) [![GitHub stars](https://img.shields.io/github/stars/dg/composer-cleaner?style=flat)](https://github.com/dg/composer-cleaner/stargazers) - The tool removes unnecessary files and directories from the vendor directory.
- [Composer-Ignore-Plugin](https://github.com/lichunqiang/composer-ignore-plugin) [![GitHub stars](https://img.shields.io/github/stars/lichunqiang/composer-ignore-plugin?style=flat)](https://github.com/lichunqiang/composer-ignore-plugin/stargazers) - Enables you to remove files and folders from the vendor folder (to make a cleaner and smaller deployment to production). It's an alternative to `.gitattributes`.
- [Composer-Vendor-Cleaner](https://github.com/liborm85/composer-vendor-cleaner) [![GitHub stars](https://img.shields.io/github/stars/liborm85/composer-vendor-cleaner?style=flat)](https://github.com/liborm85/composer-vendor-cleaner/stargazers) - Plugin removes unnecessary development files and directories from `vendor` directory by glob pattern syntax.
- [Composer-Skrub](https://github.com/ssx/skrub) [![GitHub stars](https://img.shields.io/github/stars/ssx/skrub?style=flat)](https://github.com/ssx/skrub/stargazers) - The plugin helps to remove junk from Composer installations and trim build sizes.
- [Drupal Vendor Hardening Composer Plugin](https://github.com/drupal/core-vendor-hardening) [![GitHub stars](https://img.shields.io/github/stars/drupal/core-vendor-hardening?style=flat)](https://github.com/drupal/core-vendor-hardening/stargazers) - Removes extraneous directories from the project's vendor directory & adds .htaccess and web.config files to the root of the project's vendor directory.
- [Composer-Shared-Package-Plugin](https://github.com/Letudiant/composer-shared-package-plugin) [![GitHub stars](https://img.shields.io/github/stars/Letudiant/composer-shared-package-plugin?style=flat)](https://github.com/Letudiant/composer-shared-package-plugin/stargazers) - Allows you to share selected packages between your projects by creating symlinks.
- [Composer-Symlinker](https://github.com/e-picas/composer-symlinker) [![GitHub stars](https://img.shields.io/github/stars/e-picas/composer-symlinker?style=flat)](https://github.com/e-picas/composer-symlinker/stargazers) - Enables you to load packages from different directories (instead of loading them from /vendor).
- [Prestissimo](https://github.com/hirak/prestissimo) [![GitHub stars](https://img.shields.io/github/stars/hirak/prestissimo?style=flat)](https://github.com/hirak/prestissimo/stargazers) - A parallel downloader using `phpext_curl`.
- [Composer-Curl-Plugin](https://github.com/ngyuki/composer-curl-plugin) [![GitHub stars](https://img.shields.io/github/stars/ngyuki/composer-curl-plugin?style=flat)](https://github.com/ngyuki/composer-curl-plugin/stargazers) - The plugin uses `phpext_curl` for downloading packages.
- [Composer-Custom-Directory-Installer](https://github.com/mnsami/composer-custom-directory-installer) [![GitHub stars](https://img.shields.io/github/stars/mnsami/composer-custom-directory-installer?style=flat)](https://github.com/mnsami/composer-custom-directory-installer/stargazers) - A composer plugin, to install different types of composer packages in custom directories outside the default composer installation path (vendor folder).
- [Composer-Dependency-Analyzer](https://github.com/shipmonk-rnd/composer-dependency-analyser) [![GitHub stars](https://img.shields.io/github/stars/shipmonk-rnd/composer-dependency-analyser?style=flat)](https://github.com/shipmonk-rnd/composer-dependency-analyser/stargazers) - The plugin helps to find dependency issues, including dead, unused, shadow and misplaced dependencies.
- [Composer-Dependency-Analyzer](https://packagist.org/packages/jms/composer-deps-analyzer) - Allows you to build a dependency graph for an installed composer project.
- [Graph-Composer](https://github.com/clue/graph-composer) [![GitHub stars](https://img.shields.io/github/stars/clue/graph-composer?style=flat)](https://github.com/clue/graph-composer/stargazers) - Provides a graph visualization for your project's `composer.json` and its dependencies.
- [PackageVersions](https://github.com/Ocramius/PackageVersions) [![GitHub stars](https://img.shields.io/github/stars/Ocramius/PackageVersions?style=flat)](https://github.com/Ocramius/PackageVersions/stargazers) - Provides a very quick and easy access to installed composer dependency versions.
- [PackageVersions Deprecated](https://github.com/composer/package-versions-deprecated) [![GitHub stars](https://img.shields.io/github/stars/composer/package-versions-deprecated?style=flat)](https://github.com/composer/package-versions-deprecated/stargazers) - Is a fork of Ocramius/PackageVersions providing compatibility with Composer 1 and 2 on PHP 7+.
- [Composer-Locator](https://github.com/mindplay-dk/composer-locator) [![GitHub stars](https://img.shields.io/github/stars/mindplay-dk/composer-locator?style=flat)](https://github.com/mindplay-dk/composer-locator/stargazers) - Provides a means of locating the installation path for a given Composer package name.
- [PackageInfo](https://github.com/ThaDafinser/PackageInfo) [![GitHub stars](https://img.shields.io/github/stars/ThaDafinser/PackageInfo?style=flat)](https://github.com/ThaDafinser/PackageInfo/stargazers) - Enables you to retrieve all package informations (like version, tag, release date, description).
- [Composer-Git-Hooks](https://github.com/BrainMaestro/composer-git-hooks) [![GitHub stars](https://img.shields.io/github/stars/BrainMaestro/composer-git-hooks?style=flat)](https://github.com/BrainMaestro/composer-git-hooks/stargazers) - A library for easily managing git hooks in your composer config.
- [Symfony-Flex](https://github.com/symfony/flex) [![GitHub stars](https://img.shields.io/github/stars/symfony/flex?style=flat)](https://github.com/symfony/flex/stargazers) - Provides [recipe-based](https://github.com/symfony/recipes) [![GitHub stars](https://img.shields.io/github/stars/symfony/recipes?style=flat)](https://github.com/symfony/recipes/stargazers) installation and configuration management for Symfony packages.
- [Narrowspark-Automatic](https://github.com/narrowspark/automatic) [![GitHub stars](https://img.shields.io/github/stars/narrowspark/automatic?style=flat)](https://github.com/narrowspark/automatic/stargazers) - Automates the most common tasks of applications, boost package downloads, adds a composer security audit and more.
- [PHPCodeSniffer-Composer-Installer](https://github.com/PHPCSStandards/composer-installer) [![GitHub stars](https://img.shields.io/github/stars/PHPCSStandards/composer-installer?style=flat)](https://github.com/PHPCSStandards/composer-installer/stargazers) - The plugin enables you to install [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) [![GitHub stars](https://img.shields.io/github/stars/squizlabs/PHP_CodeSniffer?style=flat)](https://github.com/squizlabs/PHP_CodeSniffer/stargazers) coding standards (rulesets).
- [Composer-Warmup](https://github.com/jderusse/composer-warmup) [![GitHub stars](https://img.shields.io/github/stars/jderusse/composer-warmup?style=flat)](https://github.com/jderusse/composer-warmup/stargazers) - The plugin adds the command `warmup-opcode` to Composer, which triggers the compilation of all PHP files discovered in your project into the Opcache.
- [Foxy](https://github.com/fxpio/foxy) [![GitHub stars](https://img.shields.io/github/stars/fxpio/foxy?style=flat)](https://github.com/fxpio/foxy/stargazers) - Composer plugin that executes npm/yarn packages installation operations, when composer package is installed or updated.
- [NodeJS-Installer](https://github.com/thecodingmachine/nodejs-installer) [![GitHub stars](https://img.shields.io/github/stars/thecodingmachine/nodejs-installer?style=flat)](https://github.com/thecodingmachine/nodejs-installer/stargazers) - Installer for Node.js and npm.
- [Node-Composer](https://github.com/mariusbuescher/node-composer) [![GitHub stars](https://img.shields.io/github/stars/mariusbuescher/node-composer?style=flat)](https://github.com/mariusbuescher/node-composer/stargazers) - Installer for Node.js, npm and yarn.
- [Imposter-Plugin](https://github.com/typisttech/imposter-plugin) [![GitHub stars](https://img.shields.io/github/stars/typisttech/imposter-plugin?style=flat)](https://github.com/typisttech/imposter-plugin/stargazers) - Wrapping all composer vendor packages inside your own namespace. Intended for WordPress plugins.
- [Composer Preload](https://github.com/Ayesh/Composer-Preload) [![GitHub stars](https://img.shields.io/github/stars/Ayesh/Composer-Preload?style=flat)](https://github.com/Ayesh/Composer-Preload/stargazers) - The plugin generates a `vendor/preload.php` file to warm up the Opcache.
- [PHP Inc](https://github.com/krakphp/php-inc) [![GitHub stars](https://img.shields.io/github/stars/krakphp/php-inc?style=flat)](https://github.com/krakphp/php-inc/stargazers) - Automatically includes files for autoload and autoload-dev to facilitate using functions and grouped definitions within composer loaded applications.
- [Composer Registry Manager](https://github.com/slince/composer-registry-manager) [![GitHub stars](https://img.shields.io/github/stars/slince/composer-registry-manager?style=flat)](https://github.com/slince/composer-registry-manager/stargazers) - Enables you to switch between different composer repositories.
- [Production-Dependencies-Guard](https://github.com/kalessil/production-dependencies-guard) [![GitHub stars](https://img.shields.io/github/stars/kalessil/production-dependencies-guard?style=flat)](https://github.com/kalessil/production-dependencies-guard/stargazers) - Prevents development packages from being added into require and getting into production environment.
- [Composer-Plugin-Exclude-Files](https://github.com/mcaskill/composer-plugin-exclude-files) [![GitHub stars](https://img.shields.io/github/stars/mcaskill/composer-plugin-exclude-files?style=flat)](https://github.com/mcaskill/composer-plugin-exclude-files/stargazers) - A plugin for excluding files required by packages using the 'files' autoloading mechanism.
- [Composer-Downloads-Plugin](https://github.com/civicrm/composer-downloads-plugin) [![GitHub stars](https://img.shields.io/github/stars/civicrm/composer-downloads-plugin?style=flat)](https://github.com/civicrm/composer-downloads-plugin/stargazers) - Lightweight mechanism to download external resources (ZIP/TAR files) with only a `url` and `path`.
- [Private-Composer-Installer](https://github.com/ffraenz/private-composer-installer) [![GitHub stars](https://img.shields.io/github/stars/ffraenz/private-composer-installer?style=flat)](https://github.com/ffraenz/private-composer-installer/stargazers) - Install helper outsourcing sensitive keys from the package URL into environment variables.
- [CycloneDX-PHP-Composer](https://github.com/CycloneDX/cyclonedx-php-composer) [![GitHub stars](https://img.shields.io/github/stars/CycloneDX/cyclonedx-php-composer?style=flat)](https://github.com/CycloneDX/cyclonedx-php-composer/stargazers) - Creates a [CycloneDX](https://cyclonedx.org/) "Software Bill-of-Materials" (SBOM) for the dependencies of a project. The SBOM enables dependency monitoring and risk analysis by [OWASP DependencyTrack](https://dependencytrack.org/).
- [Composer-Compile-Plugin](https://github.com/civicrm/composer-compile-plugin) [![GitHub stars](https://img.shields.io/github/stars/civicrm/composer-compile-plugin?style=flat)](https://github.com/civicrm/composer-compile-plugin/stargazers) - Allow PHP libraries to define simple, freeform compilation tasks. Support post-install hooks in any package.
- [Composer-Link](https://github.com/SanderSander/composer-link) [![GitHub stars](https://img.shields.io/github/stars/SanderSander/composer-link?style=flat)](https://github.com/SanderSander/composer-link/stargazers) - Adds the ability to link local packages for development.
- [Composer-REPL](https://github.com/ramsey/composer-repl) [![GitHub stars](https://img.shields.io/github/stars/ramsey/composer-repl?style=flat)](https://github.com/ramsey/composer-repl/stargazers) - The plugin provides the `composer repl` command, which gives you a PHP language shell (read-eval-print loop).
- [Composer-Diff](https://github.com/IonBazan/composer-diff) [![GitHub stars](https://img.shields.io/github/stars/IonBazan/composer-diff?style=flat)](https://github.com/IonBazan/composer-diff/stargazers) - Compares `composer.lock` changes and generates a Markdown report for usage in a pull request description.
- [Composer-Velocita](https://github.com/isaaceindhoven/composer-velocita) [![GitHub stars](https://img.shields.io/github/stars/isaaceindhoven/composer-velocita?style=flat)](https://github.com/isaaceindhoven/composer-velocita/stargazers) - Fast and reliable Composer package downloads using [Velocita](https://github.com/isaaceindhoven/velocita-proxy) [![GitHub stars](https://img.shields.io/github/stars/isaaceindhoven/velocita-proxy?style=flat)](https://github.com/isaaceindhoven/velocita-proxy/stargazers): a caching reverse proxy that does not require you to modify your projects.
- [Composer Translation Validator](https://github.com/move-elevator/composer-translation-validator) [![GitHub stars](https://img.shields.io/github/stars/move-elevator/composer-translation-validator?style=flat)](https://github.com/move-elevator/composer-translation-validator/stargazers) - Validates translation files in your project, supports several file formats (regarding different frameworks) and provides useful validators for comparison, consistency and syntax checks.

## Tools

- [Composer SemVer Checker](https://semver.madewithlove.com/) - Enables you identify constraint to version resolution issues, by doing a semantic version check for Packagist hosted packages.
- [Composer-Yaml](https://github.com/igorw/composer-yaml) [![GitHub stars](https://img.shields.io/github/stars/igorw/composer-yaml?style=flat)](https://github.com/igorw/composer-yaml/stargazers) - This tool converts `composer.yml` to `composer.json`.
- [Studio](https://github.com/franzliedke/studio) [![GitHub stars](https://img.shields.io/github/stars/franzliedke/studio?style=flat)](https://github.com/franzliedke/studio/stargazers) - A workbench for developing Composer packages. Its an alternative to editing dependencies in the vendor folder or using [PathRepositories](https://getcomposer.org/doc/05-repositories.md#path) to load a local clone of your dependency into your project.
- [OctoLinker Browser Extension](https://github.com/OctoLinker/OctoLinker) [![GitHub stars](https://img.shields.io/github/stars/OctoLinker/OctoLinker?style=flat)](https://github.com/OctoLinker/OctoLinker/stargazers) - Enables you to navigate Composer/NPM dependencies on GitHub.
- [ComposerRequireChecker](https://github.com/maglnet/ComposerRequireChecker) [![GitHub stars](https://img.shields.io/github/stars/maglnet/ComposerRequireChecker?style=flat)](https://github.com/maglnet/ComposerRequireChecker/stargazers) - A CLI tool to analyze dependencies and verify that no unknown imported symbols are used in the sources of a package.
- [Composer-Unused](https://github.com/composer-unused/composer-unused) [![GitHub stars](https://img.shields.io/github/stars/composer-unused/composer-unused?style=flat)](https://github.com/composer-unused/composer-unused/stargazers) - A CLI tool, which scans your code and shows unused Composer dependencies.
- [Composer-Normalize](https://github.com/ergebnis/composer-normalize) [![GitHub stars](https://img.shields.io/github/stars/ergebnis/composer-normalize?style=flat)](https://github.com/ergebnis/composer-normalize/stargazers) - The plugin helps to keep your `composer.json` file(s) consistent by restructuring and sorting entries (normalizing).
- [Composer-Service](https://github.com/pborreli/composer-service) [![GitHub stars](https://img.shields.io/github/stars/pborreli/composer-service?style=flat)](https://github.com/pborreli/composer-service/stargazers) - Enables you to run Composer as a service on a remote server.
- [Composer PreferLowest Checker](https://github.com/dereuromark/composer-prefer-lowest) [![GitHub stars](https://img.shields.io/github/stars/dereuromark/composer-prefer-lowest?style=flat)](https://github.com/dereuromark/composer-prefer-lowest/stargazers) - Strictly compare the specified minimum versions of your composer.json with the ones actually used by the prefer-lowest composer update command option.
- [Bramus/Composer-Autocomplete](https://github.com/bramus/composer-autocomplete) [![GitHub stars](https://img.shields.io/github/stars/bramus/composer-autocomplete?style=flat)](https://github.com/bramus/composer-autocomplete/stargazers) - A Bash/Shell autocompletion script for Composer.
- [Composer/Xdebug-Handler](https://github.com/composer/xdebug-handler) [![GitHub stars](https://img.shields.io/github/stars/composer/xdebug-handler?style=flat)](https://github.com/composer/xdebug-handler/stargazers) - Helps you to restart a CLI process without loading the xdebug extension.
- [Composer Semver Range Checker](https://gitlab.com/MattyRad/composer.guru) - A tool to help check the satisfiable ranges of a composer constraint.

## Scripts

- [ParameterHandler](https://github.com/Incenteev/ParameterHandler) [![GitHub stars](https://img.shields.io/github/stars/Incenteev/ParameterHandler?style=flat)](https://github.com/Incenteev/ParameterHandler/stargazers) - Allows you to manage your ignored parameters when running a composer install or update.
- [Tooly](https://github.com/tommy-muehle/tooly-composer-script) [![GitHub stars](https://img.shields.io/github/stars/tommy-muehle/tooly-composer-script?style=flat)](https://github.com/tommy-muehle/tooly-composer-script/stargazers) - Manage needed PHAR files in your project `composer.json`. Every PHAR file will be saved in the composer binary directory. Optional with GPG verification for every PHAR.
- [Melody](https://github.com/sensiolabs/melody) [![GitHub stars](https://img.shields.io/github/stars/sensiolabs/melody?style=flat)](https://github.com/sensiolabs/melody/stargazers) - One-file composer scripts.
- [Composer-Travis-Lint](https://github.com/raphaelstolt/composer-travis-lint) [![GitHub stars](https://img.shields.io/github/stars/raphaelstolt/composer-travis-lint?style=flat)](https://github.com/raphaelstolt/composer-travis-lint/stargazers) - Allows you to lint the Travis CI configuration file (`.travis.yml`).
- [Composer-Multitest](https://github.com/raphaelstolt/composer-multitest) [![GitHub stars](https://img.shields.io/github/stars/raphaelstolt/composer-multitest?style=flat)](https://github.com/raphaelstolt/composer-multitest/stargazers) - Enables you to run a Composer script against multiple, locally installed PHP versions, which are managed by PHPBrew or phpenv.
- [ScriptsDev](https://github.com/neronmoon/scriptsdev) [![GitHub stars](https://img.shields.io/github/stars/neronmoon/scriptsdev?style=flat)](https://github.com/neronmoon/scriptsdev/stargazers) - Enables you to use a `scripts-dev` section, which triggers scripts only in dev mode.
- [PhantomJS-Installer](https://github.com/jakoch/phantomjs-installer) [![GitHub stars](https://img.shields.io/github/stars/jakoch/phantomjs-installer?style=flat)](https://github.com/jakoch/phantomjs-installer/stargazers) - A Composer Package which installs the PhantomJS binary (Linux, Windows, Mac) into /bin of your project.
- [Composer-Vendor-Cleanup](https://github.com/0xch/composer-vendor-cleanup) [![GitHub stars](https://img.shields.io/github/stars/0xch/composer-vendor-cleanup?style=flat)](https://github.com/0xch/composer-vendor-cleanup/stargazers) - A script which removes whitelisted unnecessary files (like tests/docs etc.) from the vendor directory.
- [Composer-Substitution-Plugin](https://github.com/villfa/composer-substitution-plugin) [![GitHub stars](https://img.shields.io/github/stars/villfa/composer-substitution-plugin?style=flat)](https://github.com/villfa/composer-substitution-plugin/stargazers) - A Composer plugin replacing placeholders in the `scripts` section by dynamic values.

## Services

- [Dependabot](https://github.com/security/advanced-security) [![GitHub stars](https://img.shields.io/github/stars/security/advanced-security?style=flat)](https://github.com/security/advanced-security/stargazers) - Dependabot is a dependency update service. It monitors and updates your dependencies by sending a pull-request. The service is free for public repos and personal account repos.

---

## Tutorials

- [A beginners guide to Composer](https://www.digitalocean.com/community/tutorials/a-beginners-guide-to-composer)
- [A short & simple Composer tutorial](https://www.dev-metal.com/composer-tutorial/)
- [Easy package management with Composer](https://code.tutsplus.com/easy-package-management-with-composer--net-25530t)
- [PHP Dependency Management with Composer](https://www.sitepoint.com/re-introducing-composer/)
- [Composer Primer](https://daylerees.com/composer-primer/)
- [PHP Composer Magento Tutorial by Alan Storm](https://alanastorm.com/php_composer_magento_tutorial/)
- [Creating and Using Composer Packages](https://www.packtpub.com/en-us/learning/how-to-tutorials/creating-and-using-composer-packages/)

## Blogs

- [Jordi Boggiano (seldaek)](https://seld.be/)
- [Nils Adermann (naderman)](https://naderman.de/)
- [Composer Stability Flags](https://igor.io/2013/02/07/composer-stability-flags.html)
- [Composer Versioning](https://igor.io/2013/01/07/composer-versioning.html)
- [The long journey of making PHPs Composer memory-efficient and fast (toflar)](https://medium.com/@yanick.witschi/the-long-journey-of-making-phps-composer-memory-efficient-and-fast-63d12944aaa8)

## Videos

- [Composer Best Practices 2018 - Nils Adermann @ scotphp18](https://www.youtube.com/watch?v=eQkFjMfyqFY)
- [Composer Best Practices 2018 - Nils Adermann @ phpday 2018](https://www.youtube.com/watch?v=EpvihKaQyLs)
- [Managing dependencies is more than running "composer update" -  Nils Adermann @ phpsrb17](https://www.youtube.com/watch?v=QL6w8H2eHQE)
- [Composer Best Practices — Jordi Boggiano @ phptek 2015](https://www.youtube.com/watch?v=uNlYpSTiAcA)
- [Wonderful World of Composer](https://symfonycasts.com/screencast/composer)
- [PHP Composer Quickstart](https://www.youtube.com/watch?v=Ejr4Xqs9V2I)
- [How Composer helped shape the new way of writing PHP - Nils Adermann @ Drupal Camp Frankfurt](https://www.youtube.com/watch?v=C2jfLM-Egvg)
- [Composer Package Management - Nils Adermann @ T3CON12DE](https://www.youtube.com/watch?v=P4Qnp90TG0g)
- [Composer 2 - Jordi Boggiano @ Symfony UK usergroup 2020](https://www.youtube.com/watch?v=BAgwWhRo82w)
- [Lessons learned building the Composer internals - Jordi Boggiano @ CODEiD Odessa PHP Conference 2017](https://www.youtube.com/watch?v=pjvbn6TBZqM)

## Slides

- Slides by Nils Adermann
  - Source: https://naderman.de/slippy/src/
  - [PHP Reinvented - How Composer helped shape the new way of writing PHP](https://naderman.de/slippy/src/?file=2014-04-13-PHP-Reinvented.html)
  - [Composer Update](https://naderman.de/slippy/src/?file=2015-02-03-Composer-Update.html)
  - [Dependency Management with Composer PHP Reinvented](https://naderman.de/slippy/src/?file=2015-02-01-Dependency-Management-with-Composer-PHP-Reinvented.html)
  - [Managing dependencies is
more than running
"composer update"](https://naderman.de/slippy/slides/2017-06-30-DPC-Dependency-Management-is-more-than-composer-update.pdf)
  - [Composer
Best Practices @ T3DD17](https://naderman.de/slippy/slides/2017-07-13-T3DD17-Composer-Best-Practices.pdf)
  - [Gain Control over your
Dependencies with
Private Packagist](https://naderman.de/slippy/slides/2017-07-14-T3DD17-Gain-control-over-your-dependencies-with-private-packagist.pdf)
  - [Composer.lock demystified](https://naderman.de/slippy/slides/2018-01-26-composer-lock-demystified.pdf)
  - [Compoer In-Depth @ Contao Konferenz 2018](https://naderman.de/slippy/slides/2018-06-08-Contao-Konferenz-2018-Composer-In-Depth.pdf)
  - [Composer Best Practices 2018](https://naderman.de/slippy/slides/2018-06-27-Composer-Best-Practices-2018.pdf)
  - [Developing and Deploying Magento with Composer Best Practices](https://naderman.de/slippy/slides/2018-06-18-Developing-and-Deploying-Magento-with-Composer-Best-Practices.pdf)
  - [Composer Platform Config (check-platform-reqs) @ SymfonCon 2018](https://naderman.de/slippy/slides/2018-12-07-SymfonCon-Composer-Platform-Config.pdf)
- Slides by Jordi Boggiano
  - Source: http://slides.seld.be/
  - [Dependency Management with Composer (2013)](http://slides.seld.be/?file=2013-10-04+Dependency+Management+with+Composer.html)
  - [In Depth with Composer (2013)](http://slides.seld.be/?file=2013-10-05+In-Depth+with+Composer.html)
  - [Composer Best Practices (2015)](http://slides.seld.be/?file=2015-07-25+Composer+Best+Practices.html)
  - [Introduction to Composer (2015)](http://slides.seld.be/?file=2015-06-30+Introduction+to+Composer.html)
  - [Composer in 2016](http://slides.seld.be/?file=2016-07-22+Composer+in+2016.html)
  - [Lessons Learned Building the Composer Internals (2018)](http://slides.seld.be/?file=2018-04-20+Lessons+Learned+Building+the+Composer+Internals.html)

---

## Packagist

[Packagist](https://packagist.org) is the PHP Package Repository.

### Setup a Packagist Mirror

- [Packagist Mirror](https://github.com/Webysther/packagist-mirror) [![GitHub stars](https://img.shields.io/github/stars/Webysther/packagist-mirror?style=flat)](https://github.com/Webysther/packagist-mirror/stargazers) - This script helps to setup a packagist mirror. It is the maintained and stable version of [Packagist Crawler](https://github.com/hirak/packagist-crawler) [![GitHub stars](https://img.shields.io/github/stars/hirak/packagist-crawler?style=flat)](https://github.com/hirak/packagist-crawler/stargazers).
- [Docker Image](https://github.com/Webysther/packagist-mirror-docker) [![GitHub stars](https://img.shields.io/github/stars/Webysther/packagist-mirror-docker?style=flat)](https://github.com/Webysther/packagist-mirror-docker/stargazers) - This Docker image helps to create a customized packagist mirror.
- [Packagist Mirror from Indonesia](https://github.com/IndraGunawan/packagist-mirror) [![GitHub stars](https://img.shields.io/github/stars/IndraGunawan/packagist-mirror?style=flat)](https://github.com/IndraGunawan/packagist-mirror/stargazers) - Another implementation for creating a packagist mirror.

### Packagist Mirrors

About metadata mirrors: https://packagist.org/mirrors

- Global, CloudFlare - [packagist.pages.dev](https://packagist.pages.dev/)
- North America
  - Canada - [packagist.org](https://packagist.org) *Main mirror*
- Africa
  - South Africa - [packagist.co.za](https://packagist.co.za)
- Asia
  - China - [https://pkg.xyz/](https://pkg.xyz/), [https://developer.aliyun.com/composer](https://developer.aliyun.com/composer)
  - India - [https://packagist.in/](https://packagist.in/)
  - Japan - [packagist.jp](https://packagist.jp)
  - Korea - [https://packagist.kr/](https://packagist.kr/)

## Composer Repositories

### Registry Manager
- https://github.com/slince/composer-registry-manager - The plugin helps you to switch between different composer repositories.

### Private repositories
- [fxpio/tug](https://github.com/fxpio/tug) [![GitHub stars](https://img.shields.io/github/stars/fxpio/tug?style=flat)](https://github.com/fxpio/tug/stargazers) - Enables you to host a private Composer registry on AWS Serverless serving your private PHP packages, which are hosted on GitHub or GitLab services.

### Private Packagist
- [Private Packagist Cloud](https://packagist.com) - A Composer Repository as a Service for private packages and to mirror packages from other repositories.
- [Private Packagist Enterprise](https://packagist.com) - On-premise self-hosted version of Private Packagist.
- [Private Packagist API Client](https://github.com/packagist/private-packagist-api-client) [![GitHub stars](https://img.shields.io/github/stars/packagist/private-packagist-api-client?style=flat)](https://github.com/packagist/private-packagist-api-client/stargazers) - A PHP client for the Private Packagist API. The client handles authentication, signature generation and access to all endpoints.

### Repman

- [repman.io](https://repman.io) & [repman-io/repman](https://github.com/repman-io/repman) [![GitHub stars](https://img.shields.io/github/stars/repman-io/repman?style=flat)](https://github.com/repman-io/repman/stargazers) - A Private PHP Package Repository Manager & Packagist Proxy.
- [repman-io/composer-plugin](https://github.com/repman-io/composer-plugin) [![GitHub stars](https://img.shields.io/github/stars/repman-io/composer-plugin?style=flat)](https://github.com/repman-io/composer-plugin/stargazers) - This plugin enables downloading via Repman by adding a distribution mirror URL for all your dependencies (without need to update the `composer.lock` file).

## Packagist-compatible repositories

- [WordPress Packagist](https://wpackagist.org/) - Mirrors the WordPress plugin and theme directories as a Composer repository.
- [Asset Packagist](https://asset-packagist.org/) - Enables installation of Bower and NPM packages as native Composer packages.
- [Firegento](https://packages.firegento.com/) - A Composer Repository providing Magento Modules.
- [Drupal Packagist](https://www.drupal.org/node/2822344) - Composer repositories for Drupal 7 and 8 core, modules, and themes.
- [Satis Server](https://github.com/lukaszlach/satis-server) [![GitHub stars](https://img.shields.io/github/stars/lukaszlach/satis-server?style=flat)](https://github.com/lukaszlach/satis-server/stargazers) - This docker container provides a Satis Server and enables you to run a private, self-hosted Composer repository with support for Git, Mercurial, and Subversion, HTTP API, HTTPs support, webhook handler and scheduled builds.
- [Cloudsmith](https://cloudsmith.com/) - A fully managed package management SaaS with PHP/Composer support (and many others).
- [Release Belt](https://github.com/Rarst/release-belt) [![GitHub stars](https://img.shields.io/github/stars/Rarst/release-belt?style=flat)](https://github.com/Rarst/release-belt/stargazers) - Self–hosted Composer repository implementation to quickly integrate ZIP files of third party non–Composer releases.
- [Packeton](https://github.com/vtsykun/packeton) [![GitHub stars](https://img.shields.io/github/stars/vtsykun/packeton?style=flat)](https://github.com/vtsykun/packeton/stargazers) - Private self-hosted Composer repository for vendors. Fork of packagist with adding support for authorization, customer users, groups, webhooks.
- [RepoFlow](https://www.repoflow.io) - Simple and fast platform for hosting private Composer registries. Also supports Docker, npm, PyPI, Maven, and RubyGems. Offers free options for both cloud and self-hosted setups.

### Satis

- [GitLab-Composer](https://github.com/wemakecustom/gitlab-composer) [![GitHub stars](https://img.shields.io/github/stars/wemakecustom/gitlab-composer?style=flat)](https://github.com/wemakecustom/gitlab-composer/stargazers) - This is a branch/tag indexer for GitLab repositories.
- [Satisfy](https://github.com/project-satisfy/satisfy) [![GitHub stars](https://img.shields.io/github/stars/project-satisfy/satisfy?style=flat)](https://github.com/project-satisfy/satisfy/stargazers) - Satis composer repository manager with a Web UI.
- [Satis Control Panel](https://github.com/realshadow/satis-control-panel) [![GitHub stars](https://img.shields.io/github/stars/realshadow/satis-control-panel?style=flat)](https://github.com/realshadow/satis-control-panel/stargazers) - A simple web UI for managing your Satis Repository with optional CI integration.
- [Satis Go](https://github.com/benschw/satis-go) [![GitHub stars](https://img.shields.io/github/stars/benschw/satis-go?style=flat)](https://github.com/benschw/satis-go/stargazers) - A web server for managing Satis configuration and hosting the generated Composer repository.

### Toran Proxy

- [ToranProxy](https://toranproxy.com/) (deprecated) - In addition to providing a composer repository ToranProxy acts as a proxy server for Packagist and GitHub.

---

## Copyright

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Jens A. Koch](https://github.com/jakoch) [![GitHub stars](https://img.shields.io/github/stars/jakoch?style=flat)](https://github.com/jakoch/stargazers) has waived all copyright and related or neighboring rights to this work.
