# GitHub Actions

[![GitHub stars](https://img.shields.io/github/stars/sdras/awesome-actions?style=flat)](https://github.com/sdras/awesome-actions/stargazers)

<p align="center">
  <br>
    <img src="awesome-actions.png" width="150"/>
  <br>
</p>

# Awesome Actions [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [<!--lint ignore no-dead-urls-->![GitHub Actions status | sdras/awesome-actions](https://github.com/sdras/awesome-actions/workflows/Lint%20Awesome%20List/badge.svg) [![GitHub stars](https://img.shields.io/github/stars/sdras/awesome-actions/workflows/Lint%20Awesome%20List/badge.svg?style=flat)](https://github.com/sdras/awesome-actions/workflows/Lint%20Awesome%20List/badge.svg/stargazers)](https://github.com/sdras/awesome-actions/actions?workflow=Lint+Awesome+List)

> A curated list of awesome things related to GitHub Actions.

Actions are triggered by GitHub platform events directly in a repo and run on-demand workflows either on Linux, Windows or macOS virtual machines or inside a container in response. With GitHub Actions you can automate your workflow from idea to production.

## Contents

- [Official Resources](#official-resources)
  - [Workflow Examples](#workflow-examples)
  - [Official Actions](#official-actions)
  - [Create your Actions](#create-your-actions)
- [Community Resources](#community-resources)
  - [GitHub Tools and Management](#github-tools-and-management)
  - [Collection of Actions](#collection-of-actions)
  - [Utility](#utility)
  - [Static Analysis](#static-analysis)
  - [Dynamic Analysis](#dynamic-analysis)
  - [Monitoring](#monitoring)
  - [Pull Requests](#pull-requests)
  - [GitHub Pages](#github-pages)
  - [Notifications and Messages](#notifications-and-messages)
  - [Deployment](#deployment)
  - [External Services](#external-services)
  - [Frontend Tools](#frontend-tools)
  - [Machine Learning Ops](#machine-learning-ops)
  - [Build](#build)
  - [Database](#database)
  - [Networking](#networking)
  - [Localization](#localization)
  - [Fun](#fun)
  - [Cheat Sheet](#cheat-sheet)
- [Tutorials](#tutorials)

## Official Resources

- [Official Site](https://github.com/features/actions) [![GitHub stars](https://img.shields.io/github/stars/features/actions?style=flat)](https://github.com/features/actions/stargazers)
- [Official Documentation](https://help.github.com/en/actions)
- [Official Actions organization](https://github.com/actions) [![GitHub stars](https://img.shields.io/github/stars/actions?style=flat)](https://github.com/actions/stargazers)
  - [actions/virtual-environments](https://github.com/actions/virtual-environments) [![GitHub stars](https://img.shields.io/github/stars/actions/virtual-environments?style=flat)](https://github.com/actions/virtual-environments/stargazers) - GitHub Actions virtual environments.
  - [actions/runner](https://github.com/actions/runner) [![GitHub stars](https://img.shields.io/github/stars/actions/runner?style=flat)](https://github.com/actions/runner/stargazers) - The Runner for GitHub Actions.
- [GitHub Blog Announcement](https://github.blog/2018-10-17-action-demos/)

### Workflow Examples

- [actions/starter-workflows](https://github.com/actions/starter-workflows) [![GitHub stars](https://img.shields.io/github/stars/actions/starter-workflows?style=flat)](https://github.com/actions/starter-workflows/stargazers) - Starter workflow management.
- [actions/example-services](https://github.com/actions/example-services) [![GitHub stars](https://img.shields.io/github/stars/actions/example-services?style=flat)](https://github.com/actions/example-services/stargazers) - Example workflows using service containers.

### Official Actions

<!--lint disable no-dead-urls-->

#### Workflow Tool Actions

Tool actions for your workflow.

<!--lint ignore awesome-spell-check-->

- [actions/checkout](https://github.com/actions/checkout) [![GitHub stars](https://img.shields.io/github/stars/actions/checkout?style=flat)](https://github.com/actions/checkout/stargazers) - Setup your repository on your workflow.
- [actions/upload-artifact](https://github.com/actions/upload-artifact) [![GitHub stars](https://img.shields.io/github/stars/actions/upload-artifact?style=flat)](https://github.com/actions/upload-artifact/stargazers) - Upload artifacts from your workflow.
- [actions/download-artifact](https://github.com/actions/download-artifact) [![GitHub stars](https://img.shields.io/github/stars/actions/download-artifact?style=flat)](https://github.com/actions/download-artifact/stargazers) - Download artifacts from your build.
- [actions/cache](https://github.com/actions/cache) [![GitHub stars](https://img.shields.io/github/stars/actions/cache?style=flat)](https://github.com/actions/cache/stargazers) - Cache dependencies and build outputs in GitHub Actions.
- [actions/github-script](https://github.com/actions/github-script) [![GitHub stars](https://img.shields.io/github/stars/actions/github-script?style=flat)](https://github.com/actions/github-script/stargazers) - Write a script for GitHub API and the workflow contexts.

#### Actions for GitHub Automation

Automate management for issues, pull requests, and releases.

- [actions/create-release](https://github.com/actions/create-release) [![GitHub stars](https://img.shields.io/github/stars/actions/create-release?style=flat)](https://github.com/actions/create-release/stargazers) - An Action to create releases via the GitHub Release API.
- [actions/upload-release-asset](https://github.com/actions/upload-release-asset) [![GitHub stars](https://img.shields.io/github/stars/actions/upload-release-asset?style=flat)](https://github.com/actions/upload-release-asset/stargazers) - An Action to upload a release asset via the GitHub Release API.
- [actions/first-interaction](https://github.com/actions/first-interaction) [![GitHub stars](https://img.shields.io/github/stars/actions/first-interaction?style=flat)](https://github.com/actions/first-interaction/stargazers) - An action for filtering pull requests and issues from first-time contributors.
- [actions/stale](https://github.com/actions/stale) [![GitHub stars](https://img.shields.io/github/stars/actions/stale?style=flat)](https://github.com/actions/stale/stargazers) - Marks issues and pull requests that have not had recent interaction.
- [actions/labeler](https://github.com/actions/labeler) [![GitHub stars](https://img.shields.io/github/stars/actions/labeler?style=flat)](https://github.com/actions/labeler/stargazers) - An action for automatically labelling pull requests.
- [actions/delete-package-versions](https://github.com/actions/delete-package-versions) [![GitHub stars](https://img.shields.io/github/stars/actions/delete-package-versions?style=flat)](https://github.com/actions/delete-package-versions/stargazers) - Delete versions of a package from GitHub Packages.

#### Setup Actions

Set up your GitHub Actions workflow with a specific version of your programming languages.

- [actions/setup-node: Node.js](https://github.com/actions/setup-node) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-node?style=flat)](https://github.com/actions/setup-node/stargazers)
- [actions/setup-python: Python](https://github.com/actions/setup-python) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-python?style=flat)](https://github.com/actions/setup-python/stargazers)
- [actions/setup-go: Go](https://github.com/actions/setup-go) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-go?style=flat)](https://github.com/actions/setup-go/stargazers)
- [actions/setup-dotnet: .NET core sdk](https://github.com/actions/setup-dotnet) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-dotnet?style=flat)](https://github.com/actions/setup-dotnet/stargazers)
- [actions/setup-haskell: Haskell (GHC and Cabal)](https://github.com/actions/setup-haskell) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-haskell?style=flat)](https://github.com/actions/setup-haskell/stargazers)
- [actions/setup-java: Java](https://github.com/actions/setup-java) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-java?style=flat)](https://github.com/actions/setup-java/stargazers)
- [actions/setup-ruby: Ruby](https://github.com/actions/setup-ruby) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-ruby?style=flat)](https://github.com/actions/setup-ruby/stargazers)
- [actions/setup-elixir: Elixir](https://github.com/actions/setup-elixir) [![GitHub stars](https://img.shields.io/github/stars/actions/setup-elixir?style=flat)](https://github.com/actions/setup-elixir/stargazers)
- [actions/setup-julia: Julia](https://github.com/julia-actions/setup-julia) [![GitHub stars](https://img.shields.io/github/stars/julia-actions/setup-julia?style=flat)](https://github.com/julia-actions/setup-julia/stargazers)

### Create your Actions

#### JavaScript and TypeScript Actions

- [actions/toolkit](https://github.com/actions/toolkit) [![GitHub stars](https://img.shields.io/github/stars/actions/toolkit?style=flat)](https://github.com/actions/toolkit/stargazers) - The GitHub ToolKit for developing GitHub Actions.
- [actions/hello-world-javascript-action](https://github.com/actions/hello-world-javascript-action) [![GitHub stars](https://img.shields.io/github/stars/actions/hello-world-javascript-action?style=flat)](https://github.com/actions/hello-world-javascript-action/stargazers) - A template to demonstrate how to build a JavaScript action.
- [actions/javascript-action](https://github.com/actions/javascript-action) [![GitHub stars](https://img.shields.io/github/stars/actions/javascript-action?style=flat)](https://github.com/actions/javascript-action/stargazers) - Create a JavaScript Action.
- [actions/typescript-action](https://github.com/actions/typescript-action) [![GitHub stars](https://img.shields.io/github/stars/actions/typescript-action?style=flat)](https://github.com/actions/typescript-action/stargazers) - Create a TypeScript Action.
- [actions/http-client](https://github.com/actions/http-client) [![GitHub stars](https://img.shields.io/github/stars/actions/http-client?style=flat)](https://github.com/actions/http-client/stargazers) - A lightweight HTTP client optimized for use with actions, TypeScript with generics and async await.

#### Docker Container Actions

- [actions/hello-world-docker-action](https://github.com/actions/hello-world-docker-action) [![GitHub stars](https://img.shields.io/github/stars/actions/hello-world-docker-action?style=flat)](https://github.com/actions/hello-world-docker-action/stargazers) - A template to demonstrate how to build a Docker action.
- [actions/container-toolkit-action](https://github.com/actions/container-toolkit-action) [![GitHub stars](https://img.shields.io/github/stars/actions/container-toolkit-action?style=flat)](https://github.com/actions/container-toolkit-action/stargazers) - Template repo for creating container actions using actions/toolkit.

## Community Resources

### GitHub Tools and Management

- [Declaratively setup GitHub Labels](https://github.com/lannonbr/issue-label-manager-action) [![GitHub stars](https://img.shields.io/github/stars/lannonbr/issue-label-manager-action?style=flat)](https://github.com/lannonbr/issue-label-manager-action/stargazers)
- [Action to sync GitHub labels in the declarative way](https://github.com/micnncim/action-label-syncer) [![GitHub stars](https://img.shields.io/github/stars/micnncim/action-label-syncer?style=flat)](https://github.com/micnncim/action-label-syncer/stargazers)
- [Add releases to GitHub](https://github.com/elgohr/Github-Release-Action) [![GitHub stars](https://img.shields.io/github/stars/elgohr/Github-Release-Action?style=flat)](https://github.com/elgohr/Github-Release-Action/stargazers)
- [Publish a docker image to Dockerhub](https://github.com/elgohr/Publish-Docker-Github-Action) [![GitHub stars](https://img.shields.io/github/stars/elgohr/Publish-Docker-Github-Action?style=flat)](https://github.com/elgohr/Publish-Docker-Github-Action/stargazers)
- [Create an issue using content from a file](https://github.com/peter-evans/create-issue-from-file) [![GitHub stars](https://img.shields.io/github/stars/peter-evans/create-issue-from-file?style=flat)](https://github.com/peter-evans/create-issue-from-file/stargazers)
- [Publish GitHub Releases with Assets](https://github.com/softprops/action-gh-release) [![GitHub stars](https://img.shields.io/github/stars/softprops/action-gh-release?style=flat)](https://github.com/softprops/action-gh-release/stargazers)
- [GitHub Project Automation+](https://github.com/alex-page/github-project-automation-plus) [![GitHub stars](https://img.shields.io/github/stars/alex-page/github-project-automation-plus?style=flat)](https://github.com/alex-page/github-project-automation-plus/stargazers) - Automate GitHub Project cards with any webhook event.
- [Run GitHub Actions Locally with a web interface](https://github.com/phishy/wflow) [![GitHub stars](https://img.shields.io/github/stars/phishy/wflow?style=flat)](https://github.com/phishy/wflow/stargazers)
- [Run GitHub Actions Locally in Terminal](https://github.com/nektos/act) [![GitHub stars](https://img.shields.io/github/stars/nektos/act?style=flat)](https://github.com/nektos/act/stargazers)
- [Build and Publish Android debug APK](https://github.com/ShaunLWM/action-release-debugapk) [![GitHub stars](https://img.shields.io/github/stars/ShaunLWM/action-release-debugapk?style=flat)](https://github.com/ShaunLWM/action-release-debugapk/stargazers)
- [Generate sequential build numbers for GitHub Actions](https://github.com/einaregilsson/build-number) [![GitHub stars](https://img.shields.io/github/stars/einaregilsson/build-number?style=flat)](https://github.com/einaregilsson/build-number/stargazers)
- [Push Git changes to GitHub repository without authentication difficulties](https://github.com/ad-m/github-push-action) [![GitHub stars](https://img.shields.io/github/stars/ad-m/github-push-action?style=flat)](https://github.com/ad-m/github-push-action/stargazers)
- [Generate release notes based on your events](https://github.com/Decathlon/release-notes-generator-action) [![GitHub stars](https://img.shields.io/github/stars/Decathlon/release-notes-generator-action?style=flat)](https://github.com/Decathlon/release-notes-generator-action/stargazers)
- [Create a GitHub wiki page based on the provided markdown file](https://github.com/Decathlon/wiki-page-creator-action) [![GitHub stars](https://img.shields.io/github/stars/Decathlon/wiki-page-creator-action?style=flat)](https://github.com/Decathlon/wiki-page-creator-action/stargazers)
- [Label your Pull Requests auto-magically (using committed files)](https://github.com/Decathlon/pull-request-labeler-action) [![GitHub stars](https://img.shields.io/github/stars/Decathlon/pull-request-labeler-action?style=flat)](https://github.com/Decathlon/pull-request-labeler-action/stargazers)
- [Add Label to your Pull Requests based on the author team name](https://github.com/JulienKode/team-labeler-action) [![GitHub stars](https://img.shields.io/github/stars/JulienKode/team-labeler-action?style=flat)](https://github.com/JulienKode/team-labeler-action/stargazers)
- [Get a list of file changes with PR/Push](https://github.com/trilom/file-changes-action) [![GitHub stars](https://img.shields.io/github/stars/trilom/file-changes-action?style=flat)](https://github.com/trilom/file-changes-action/stargazers)
- [Use private actions in any workflow](https://github.com/InVisionApp/private-action-loader) [![GitHub stars](https://img.shields.io/github/stars/InVisionApp/private-action-loader?style=flat)](https://github.com/InVisionApp/private-action-loader/stargazers)
- [Label Your Issues Using the Issue's Contents](https://github.com/damccorm/tag-ur-it) [![GitHub stars](https://img.shields.io/github/stars/damccorm/tag-ur-it?style=flat)](https://github.com/damccorm/tag-ur-it/stargazers)
- [Rollback a GitHub Release](https://github.com/author/action-rollback) [![GitHub stars](https://img.shields.io/github/stars/author/action-rollback?style=flat)](https://github.com/author/action-rollback/stargazers)
- [Lock Closed Issues and Pull Requests after a Period of Inactivity](https://github.com/dessant/lock-threads) [![GitHub stars](https://img.shields.io/github/stars/dessant/lock-threads?style=flat)](https://github.com/dessant/lock-threads/stargazers)
- [Get Commit Difference Count Between Two Branches](https://github.com/jessicalostinspace/commit-difference-action) [![GitHub stars](https://img.shields.io/github/stars/jessicalostinspace/commit-difference-action?style=flat)](https://github.com/jessicalostinspace/commit-difference-action/stargazers)
- [Generate Release Notes Based on Git References](https://github.com/metcalfc/changelog-generator) [![GitHub stars](https://img.shields.io/github/stars/metcalfc/changelog-generator?style=flat)](https://github.com/metcalfc/changelog-generator/stargazers)
- [Enforce Policies on GitHub Repositories and Commits](https://github.com/talos-systems/conform) [![GitHub stars](https://img.shields.io/github/stars/talos-systems/conform?style=flat)](https://github.com/talos-systems/conform/stargazers)
- [Auto Label Issue Based on Issue Description](https://github.com/Renato66/auto-label) [![GitHub stars](https://img.shields.io/github/stars/Renato66/auto-label?style=flat)](https://github.com/Renato66/auto-label/stargazers)
- [Update Configured GitHub Actions to the Latest Versions](https://github.com/fabasoad/ghacu) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/ghacu?style=flat)](https://github.com/fabasoad/ghacu/stargazers)
- [Create Issue Branch](https://github.com/robvanderleek/create-issue-branch) [![GitHub stars](https://img.shields.io/github/stars/robvanderleek/create-issue-branch?style=flat)](https://github.com/robvanderleek/create-issue-branch/stargazers)
- [Remove Old Artifacts](https://github.com/c-hive/gha-remove-artifacts) [![GitHub stars](https://img.shields.io/github/stars/c-hive/gha-remove-artifacts?style=flat)](https://github.com/c-hive/gha-remove-artifacts/stargazers)
- [Expose Git Commit Data As Environment Variables](https://github.com/rlespinasse/git-commit-data-action) [![GitHub stars](https://img.shields.io/github/stars/rlespinasse/git-commit-data-action?style=flat)](https://github.com/rlespinasse/git-commit-data-action/stargazers)
- [Sync Defined Files/Binaries to Wiki or External Repositories](https://github.com/kai-tub/external-repo-sync-action) [![GitHub stars](https://img.shields.io/github/stars/kai-tub/external-repo-sync-action?style=flat)](https://github.com/kai-tub/external-repo-sync-action/stargazers)
- [Create/Update/Delete a GitHub Wiki Page Based on Any File](https://github.com/Andrew-Chen-Wang/github-wiki-action) [![GitHub stars](https://img.shields.io/github/stars/Andrew-Chen-Wang/github-wiki-action?style=flat)](https://github.com/Andrew-Chen-Wang/github-wiki-action/stargazers)
- [Prow GitHub Actions](https://github.com/jpmcb/prow-github-actions) [![GitHub stars](https://img.shields.io/github/stars/jpmcb/prow-github-actions?style=flat)](https://github.com/jpmcb/prow-github-actions/stargazers) - Automation of policy enforcement, chat-ops, and automatic PR merging.
- [Check GitHub Status in your Workflow](https://github.com/crazy-max/ghaction-github-status) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-github-status?style=flat)](https://github.com/crazy-max/ghaction-github-status/stargazers)
- [Manage Labels on GitHub (create/rename/update/delete) as Code](https://github.com/crazy-max/ghaction-github-labeler) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-github-labeler?style=flat)](https://github.com/crazy-max/ghaction-github-labeler/stargazers)
- [Continuous Distribution of Funding to your Project Contributors and Dependencies](https://github.com/protontypes/libreselery) [![GitHub stars](https://img.shields.io/github/stars/protontypes/libreselery?style=flat)](https://github.com/protontypes/libreselery/stargazers)
- [Herald Rules for GitHub: Add Subscribers, Assignees, Labels, and More to Your PR](https://github.com/gagoar/use-herald-action) [![GitHub stars](https://img.shields.io/github/stars/gagoar/use-herald-action?style=flat)](https://github.com/gagoar/use-herald-action/stargazers)
- [GitHub Codeowners Validator](https://github.com/mszostok/codeowners-validator) [![GitHub stars](https://img.shields.io/github/stars/mszostok/codeowners-validator?style=flat)](https://github.com/mszostok/codeowners-validator/stargazers) - Ensures the correctness of your GitHub CODEOWNERS file. It supports public and private GitHub repositories and also GitHub Enterprise installations.
- [Copybara Action](https://github.com/olivr/copybara-action) [![GitHub stars](https://img.shields.io/github/stars/olivr/copybara-action?style=flat)](https://github.com/olivr/copybara-action/stargazers) - Move and transform code between repositories (ideal to maintain several repos from one monorepo).

### Collection of Actions

- [Use HashiCorp's Terraform](https://github.com/hashicorp/setup-terraform) [![GitHub stars](https://img.shields.io/github/stars/hashicorp/setup-terraform?style=flat)](https://github.com/hashicorp/setup-terraform/stargazers)
- [GitHub Actions for Yarn 1](https://github.com/Borales/actions-yarn) [![GitHub stars](https://img.shields.io/github/stars/Borales/actions-yarn?style=flat)](https://github.com/Borales/actions-yarn/stargazers)
- [GitHub Actions for Yarn 2](https://github.com/sergioramos/yarn-actions) [![GitHub stars](https://img.shields.io/github/stars/sergioramos/yarn-actions?style=flat)](https://github.com/sergioramos/yarn-actions/stargazers)
- [GitHub Actions for Golang](https://github.com/cedrickring/golang-action) [![GitHub stars](https://img.shields.io/github/stars/cedrickring/golang-action?style=flat)](https://github.com/cedrickring/golang-action/stargazers)
- [GitHub Actions for R and accompanying #rstats package](http://maxheld.de/ghactions/)
- [GitHub Actions for WordPress](https://github.com/10up/actions-wordpress/) [![GitHub stars](https://img.shields.io/github/stars/10up/actions-wordpress/?style=flat)](https://github.com/10up/actions-wordpress//stargazers)
- [GitHub Actions for Composer](https://github.com/MilesChou/composer-action) [![GitHub stars](https://img.shields.io/github/stars/MilesChou/composer-action?style=flat)](https://github.com/MilesChou/composer-action/stargazers)
- [GitHub Actions for Flutter](https://github.com/subosito/flutter-action) [![GitHub stars](https://img.shields.io/github/stars/subosito/flutter-action?style=flat)](https://github.com/subosito/flutter-action/stargazers)
- [GitHub Actions for PHP](https://github.com/shivammathur/setup-php) [![GitHub stars](https://img.shields.io/github/stars/shivammathur/setup-php?style=flat)](https://github.com/shivammathur/setup-php/stargazers)
- [GitHub Actions for Rust](https://github.com/actions-rs) [![GitHub stars](https://img.shields.io/github/stars/actions-rs?style=flat)](https://github.com/actions-rs/stargazers)
- [GitHub Actions for Android](https://github.com/Malinskiy/action-android) [![GitHub stars](https://img.shields.io/github/stars/Malinskiy/action-android?style=flat)](https://github.com/Malinskiy/action-android/stargazers)
- [GitHub Actions for Logtalk and Prolog](https://github.com/logtalk-actions) [![GitHub stars](https://img.shields.io/github/stars/logtalk-actions?style=flat)](https://github.com/logtalk-actions/stargazers)
- [GitHub Actions for Deno](https://github.com/denolib/setup-deno) [![GitHub stars](https://img.shields.io/github/stars/denolib/setup-deno?style=flat)](https://github.com/denolib/setup-deno/stargazers)
- [GitHub Actions for Unity](https://github.com/webbertakken/unity-actions) [![GitHub stars](https://img.shields.io/github/stars/webbertakken/unity-actions?style=flat)](https://github.com/webbertakken/unity-actions/stargazers)
- [Octions - GitHub Actions for GitHub REST API](https://github.com/maxkomarychev/octions) [![GitHub stars](https://img.shields.io/github/stars/maxkomarychev/octions?style=flat)](https://github.com/maxkomarychev/octions/stargazers)
- [GitHub Actions for Docker](https://github.com/docker/github-actions) [![GitHub stars](https://img.shields.io/github/stars/docker/github-actions?style=flat)](https://github.com/docker/github-actions/stargazers)
- [GitHub Actions for AWS](https://github.com/clowdhaus/aws-github-actions) [![GitHub stars](https://img.shields.io/github/stars/clowdhaus/aws-github-actions?style=flat)](https://github.com/clowdhaus/aws-github-actions/stargazers)
- [Actions Hub](https://github.com/actionshub) [![GitHub stars](https://img.shields.io/github/stars/actionshub?style=flat)](https://github.com/actionshub/stargazers)

### Utility

- [Setup `ssh-agent`](https://github.com/webfactory/ssh-agent) [![GitHub stars](https://img.shields.io/github/stars/webfactory/ssh-agent?style=flat)](https://github.com/webfactory/ssh-agent/stargazers) - Run `ssh-agent` with additional SSH keys to access private repositories.
- [GitHub Actions Badges for your README](https://github.com/atrox/github-actions-badge) [![GitHub stars](https://img.shields.io/github/stars/atrox/github-actions-badge?style=flat)](https://github.com/atrox/github-actions-badge/stargazers)
- [GitHub Actions for Python project with poetry](https://github.com/abatilo/actions-poetry) [![GitHub stars](https://img.shields.io/github/stars/abatilo/actions-poetry?style=flat)](https://github.com/abatilo/actions-poetry/stargazers)
- [GitHub Actions for Python project with pyenv](https://github.com/gabrielfalcao/pyenv-action) [![GitHub stars](https://img.shields.io/github/stars/gabrielfalcao/pyenv-action?style=flat)](https://github.com/gabrielfalcao/pyenv-action/stargazers)
- [GitHub Actions to compile LaTeX documents](https://github.com/xu-cheng/latex-action) [![GitHub stars](https://img.shields.io/github/stars/xu-cheng/latex-action?style=flat)](https://github.com/xu-cheng/latex-action/stargazers)
- [Update Maxmind Databases](https://github.com/meetup/maxmind-updater) [![GitHub stars](https://img.shields.io/github/stars/meetup/maxmind-updater?style=flat)](https://github.com/meetup/maxmind-updater/stargazers)
- [Debug with SSH over tmate](https://github.com/mxschmitt/action-tmate) [![GitHub stars](https://img.shields.io/github/stars/mxschmitt/action-tmate?style=flat)](https://github.com/mxschmitt/action-tmate/stargazers) - Debug the Action directly by providing a SSH connection.
- [Unlock git-crypt files](https://github.com/sliteteam/github-action-git-crypt-unlock) [![GitHub stars](https://img.shields.io/github/stars/sliteteam/github-action-git-crypt-unlock?style=flat)](https://github.com/sliteteam/github-action-git-crypt-unlock/stargazers)
- [Golang CGO cross compiler](https://github.com/crazy-max/ghaction-xgo) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-xgo?style=flat)](https://github.com/crazy-max/ghaction-xgo/stargazers)
- [Run your job on another architecture: arm32, aarch64 and others](https://github.com/uraimo/run-on-arch-action) [![GitHub stars](https://img.shields.io/github/stars/uraimo/run-on-arch-action?style=flat)](https://github.com/uraimo/run-on-arch-action/stargazers)
- [Generate a table of contents](https://github.com/technote-space/toc-generator) [![GitHub stars](https://img.shields.io/github/stars/technote-space/toc-generator?style=flat)](https://github.com/technote-space/toc-generator/stargazers)
- [Automatically add Label or Assignee to an Issue](https://github.com/Naturalclar/issue-action) [![GitHub stars](https://img.shields.io/github/stars/Naturalclar/issue-action?style=flat)](https://github.com/Naturalclar/issue-action/stargazers)
- [Action to send LGTM reaction as image or GIF when we say lgtm](https://github.com/micnncim/action-lgtm-reaction) [![GitHub stars](https://img.shields.io/github/stars/micnncim/action-lgtm-reaction?style=flat)](https://github.com/micnncim/action-lgtm-reaction/stargazers)
- [Generate build numbers across multiple scopes](https://github.com/zyborg/gh-action-buildnum) [![GitHub stars](https://img.shields.io/github/stars/zyborg/gh-action-buildnum?style=flat)](https://github.com/zyborg/gh-action-buildnum/stargazers)
- [Publish GitHub release artifacts](https://github.com/skx/github-action-publish-binaries) [![GitHub stars](https://img.shields.io/github/stars/skx/github-action-publish-binaries?style=flat)](https://github.com/skx/github-action-publish-binaries/stargazers)
- [Jekyll Diff Action](https://github.com/David-Byrne/jekyll-diff-action) [![GitHub stars](https://img.shields.io/github/stars/David-Byrne/jekyll-diff-action?style=flat)](https://github.com/David-Byrne/jekyll-diff-action/stargazers) - Diffs the built Jekyll site after a change, and comments the result back to GitHub.
- [Branch Protection Bot](https://github.com/benjefferies/branch-protection-bot) [![GitHub stars](https://img.shields.io/github/stars/benjefferies/branch-protection-bot?style=flat)](https://github.com/benjefferies/branch-protection-bot/stargazers) - Temporarily disable and re-enable "Include administrators" option in branch protection.
- [Wait for commit statuses](https://github.com/WyriHaximus/github-action-wait-for-status) [![GitHub stars](https://img.shields.io/github/stars/WyriHaximus/github-action-wait-for-status?style=flat)](https://github.com/WyriHaximus/github-action-wait-for-status/stargazers) - Wait until all statuses and checks are successful or any of them has failed and set its status output accordingly.
- [Get Latest Tag](https://github.com/WyriHaximus/github-action-get-previous-tag) [![GitHub stars](https://img.shields.io/github/stars/WyriHaximus/github-action-get-previous-tag?style=flat)](https://github.com/WyriHaximus/github-action-get-previous-tag/stargazers) - Get the previous tag from git.
- [Create Milestone](https://github.com/WyriHaximus/github-action-create-milestone) [![GitHub stars](https://img.shields.io/github/stars/WyriHaximus/github-action-create-milestone?style=flat)](https://github.com/WyriHaximus/github-action-create-milestone/stargazers) - Create a new open milestone given the title and description.
- [Close Milestone](https://github.com/WyriHaximus/github-action-close-milestone) [![GitHub stars](https://img.shields.io/github/stars/WyriHaximus/github-action-close-milestone?style=flat)](https://github.com/WyriHaximus/github-action-close-milestone/stargazers) - Close the given milestone.
- [Action to enforce branch naming rules](https://github.com/deepakputhraya/action-branch-name) [![GitHub stars](https://img.shields.io/github/stars/deepakputhraya/action-branch-name?style=flat)](https://github.com/deepakputhraya/action-branch-name/stargazers)
- [Expose slug of some GitHub variables](https://github.com/marketplace/actions/github-slug) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/github-slug?style=flat)](https://github.com/marketplace/actions/github-slug/stargazers)
- [awesome-lint as a GitHub Action](https://github.com/max/awesome-lint) [![GitHub stars](https://img.shields.io/github/stars/max/awesome-lint?style=flat)](https://github.com/max/awesome-lint/stargazers)
- [Edit JSON File](https://github.com/deef0000dragon1/json-edit-action) [![GitHub stars](https://img.shields.io/github/stars/deef0000dragon1/json-edit-action?style=flat)](https://github.com/deef0000dragon1/json-edit-action/stargazers)
- [Build Slate documentation](https://github.com/Decathlon/slate-builder-action) [![GitHub stars](https://img.shields.io/github/stars/Decathlon/slate-builder-action?style=flat)](https://github.com/Decathlon/slate-builder-action/stargazers)
- [Read Properties](https://github.com/christian-draeger/read-properties) [![GitHub stars](https://img.shields.io/github/stars/christian-draeger/read-properties?style=flat)](https://github.com/christian-draeger/read-properties/stargazers) - Read values from `.properties` files.
- [Write Properties](https://github.com/christian-draeger/write-properties) [![GitHub stars](https://img.shields.io/github/stars/christian-draeger/write-properties?style=flat)](https://github.com/christian-draeger/write-properties/stargazers) - Write values to `.properties` files.
- [Autotag](https://github.com/butlerlogic/action-autotag) [![GitHub stars](https://img.shields.io/github/stars/butlerlogic/action-autotag?style=flat)](https://github.com/butlerlogic/action-autotag/stargazers) - Automatically generate a new tag when the manifest file (i.e. `package.json`) version changes.
- [Apply templates with Jinja2](https://github.com/cuchi/jinja2-action) [![GitHub stars](https://img.shields.io/github/stars/cuchi/jinja2-action?style=flat)](https://github.com/cuchi/jinja2-action/stargazers) - Use the Jinja2 template engine to generate files from templates.
- [Has Changes](https://github.com/UnicornGlobal/has-changes-action) [![GitHub stars](https://img.shields.io/github/stars/UnicornGlobal/has-changes-action?style=flat)](https://github.com/UnicornGlobal/has-changes-action/stargazers) - Check if there are code changes from previous steps.
- [Mind Your Language Action](https://github.com/tailaiw/mind-your-language-action) [![GitHub stars](https://img.shields.io/github/stars/tailaiw/mind-your-language-action?style=flat)](https://github.com/tailaiw/mind-your-language-action/stargazers) - Detect offensive comments in issues and pull requests, and warn senders.
- [YAML/JSON/XML Converter](https://github.com/fabasoad/yaml-json-xml-converter-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/yaml-json-xml-converter-action?style=flat)](https://github.com/fabasoad/yaml-json-xml-converter-action/stargazers) - Converts YAML/JSON/XML file formats interchangeably.
- [NSFW Detection](https://github.com/fabasoad/nsfw-detection-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/nsfw-detection-action?style=flat)](https://github.com/fabasoad/nsfw-detection-action/stargazers) - Detect NSFW content in committed files.
- [Has Changed Path](https://github.com/MarceloPrado/has-changed-path) [![GitHub stars](https://img.shields.io/github/stars/MarceloPrado/has-changed-path?style=flat)](https://github.com/MarceloPrado/has-changed-path/stargazers) - Conditionally run actions based on changed paths.
- [Linguist](https://github.com/fabasoad/linguist-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/linguist-action?style=flat)](https://github.com/fabasoad/linguist-action/stargazers) - Checks a repository and produces information about used languages in output.
- [Twilio Voice Call](https://github.com/fabasoad/twilio-voice-call-action/) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/twilio-voice-call-action/?style=flat)](https://github.com/fabasoad/twilio-voice-call-action//stargazers) - Make Twilio voice call with defined text.
- [Setup Xcode](https://github.com/maxim-lobanov/setup-xcode) [![GitHub stars](https://img.shields.io/github/stars/maxim-lobanov/setup-xcode?style=flat)](https://github.com/maxim-lobanov/setup-xcode/stargazers) - Switch between pre-installed versions of Xcode for macOS images.
- [Setup Xamarin](https://github.com/maxim-lobanov/setup-xamarin) [![GitHub stars](https://img.shields.io/github/stars/maxim-lobanov/setup-xamarin?style=flat)](https://github.com/maxim-lobanov/setup-xamarin/stargazers) - Switch between pre-installed versions of Xamarin and Mono for macOS images.
- [Memer Action](https://github.com/Bhupesh-V/memer-action) [![GitHub stars](https://img.shields.io/github/stars/Bhupesh-V/memer-action?style=flat)](https://github.com/Bhupesh-V/memer-action/stargazers) - A GitHub Action for Programmer Memes xD.
- [Setup Cocoapods](https://github.com/maxim-lobanov/setup-cocoapods) [![GitHub stars](https://img.shields.io/github/stars/maxim-lobanov/setup-cocoapods?style=flat)](https://github.com/maxim-lobanov/setup-cocoapods/stargazers) - Setup specific version of Cocoapods.
- [Public IP](https://github.com/haythem/public-ip) [![GitHub stars](https://img.shields.io/github/stars/haythem/public-ip?style=flat)](https://github.com/haythem/public-ip/stargazers) - Queries GitHub actions runner's public IP address.
- [GitHub Actions for Lazarus/FPC](https://github.com/gcarreno/setup-lazarus) [![GitHub stars](https://img.shields.io/github/stars/gcarreno/setup-lazarus?style=flat)](https://github.com/gcarreno/setup-lazarus/stargazers)
- [Twilio Fax](https://github.com/fabasoad/twilio-fax-action/) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/twilio-fax-action/?style=flat)](https://github.com/fabasoad/twilio-fax-action//stargazers) - Sends a document by fax using your Twilio account.
- [Setup Kubernetes tools](https://github.com/yokawasa/action-setup-kube-tools) [![GitHub stars](https://img.shields.io/github/stars/yokawasa/action-setup-kube-tools?style=flat)](https://github.com/yokawasa/action-setup-kube-tools/stargazers) - Install Kubernetes tools (kubectl, kustomize, helm, kubeval, conftest, and yq) on the runner.
- [Setup Elastic Cloud Control Tool](https://github.com/yokawasa/action-setup-ecctl) [![GitHub stars](https://img.shields.io/github/stars/yokawasa/action-setup-ecctl?style=flat)](https://github.com/yokawasa/action-setup-ecctl/stargazers) - Install a specific version of ecctl on the runner.
- [PowerShell Script](https://github.com/Amadevus/pwsh-script) [![GitHub stars](https://img.shields.io/github/stars/Amadevus/pwsh-script?style=flat)](https://github.com/Amadevus/pwsh-script/stargazers) - Run PowerShell scripts with workflow contexts (e.g. `$github.token`) and cmdlets, return value => action output.
- [Upload and Scan Files with VirusTotal](https://github.com/crazy-max/ghaction-virustotal) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-virustotal?style=flat)](https://github.com/crazy-max/ghaction-virustotal/stargazers)
- [Import a GPG Key](https://github.com/crazy-max/ghaction-import-gpg) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-import-gpg?style=flat)](https://github.com/crazy-max/ghaction-import-gpg/stargazers)
- [Compress with UPX](https://github.com/crazy-max/ghaction-upx) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-upx?style=flat)](https://github.com/crazy-max/ghaction-upx/stargazers) - The Ultimate Packer for eXecutables.
- [Pull the New Go Module Version Into the Proxy Cache](https://github.com/andrewslotin/go-proxy-pull-action) [![GitHub stars](https://img.shields.io/github/stars/andrewslotin/go-proxy-pull-action?style=flat)](https://github.com/andrewslotin/go-proxy-pull-action/stargazers) - Ensures the latest version of your Go module is in the proxy cache. Also updates the pkg.go.dev documentation upon release.
- [Delete Run Artifacts](https://github.com/marketplace/actions/delete-run-artifacts) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/delete-run-artifacts?style=flat)](https://github.com/marketplace/actions/delete-run-artifacts/stargazers) - Deletes all artifacts at the end of a workflow run.
- [GitHub Environment Variables Action](https://github.com/FranzDiebold/github-env-vars-action) [![GitHub stars](https://img.shields.io/github/stars/FranzDiebold/github-env-vars-action?style=flat)](https://github.com/FranzDiebold/github-env-vars-action/stargazers) - Expose environment variables such as the branch/tag name, repository slug, and ref slug.
- [GitHub Action Locks](https://github.com/abatilo/github-action-locks/blob/master/README.md) [![GitHub stars](https://img.shields.io/github/stars/abatilo/github-action-locks/blob/master/README.md?style=flat)](https://github.com/abatilo/github-action-locks/blob/master/README.md/stargazers) - Guarantee atomic execution of your GitHub Action workflows.
- [Paths Filter](https://github.com/dorny/paths-filter) [![GitHub stars](https://img.shields.io/github/stars/dorny/paths-filter?style=flat)](https://github.com/dorny/paths-filter/stargazers) - Conditionally run actions based on files modified by PR, feature branch or pushed commits.
- [Minisauras](https://github.com/TeamTigers/minisauras) [![GitHub stars](https://img.shields.io/github/stars/TeamTigers/minisauras?style=flat)](https://github.com/TeamTigers/minisauras/stargazers) -  Pulls all the JavaScript and CSS files from your base branch, minify them and creates a pull-request with a new branch.
- [Website to GIF](https://github.com/PabloLec/website-to-gif) [![GitHub stars](https://img.shields.io/github/stars/PabloLec/website-to-gif?style=flat)](https://github.com/PabloLec/website-to-gif/stargazers) - Turn any webpage into a GIF to display on your README, docs, etc.
- [Interactive Inputs - Runtime workflow inputs](https://github.com/boasiHQ/interactive-inputs) [![GitHub stars](https://img.shields.io/github/stars/boasiHQ/interactive-inputs?style=flat)](https://github.com/boasiHQ/interactive-inputs/stargazers) - Add dynamic inputs at runtime for your GitHub Actions workflows

#### Environments

- [Create an envfile](https://github.com/SpicyPizza/create-envfile) [![GitHub stars](https://img.shields.io/github/stars/SpicyPizza/create-envfile?style=flat)](https://github.com/SpicyPizza/create-envfile/stargazers)
- [Export global environment variables for succeeding build steps](https://github.com/zweitag/github-actions) [![GitHub stars](https://img.shields.io/github/stars/zweitag/github-actions?style=flat)](https://github.com/zweitag/github-actions/stargazers)
- [Programmatically set environment variables for use in subsequent steps](https://github.com/allenevans/set-env) [![GitHub stars](https://img.shields.io/github/stars/allenevans/set-env?style=flat)](https://github.com/allenevans/set-env/stargazers)
- [Install Conda environments for Python](https://github.com/goanpeca/setup-miniconda) [![GitHub stars](https://img.shields.io/github/stars/goanpeca/setup-miniconda?style=flat)](https://github.com/goanpeca/setup-miniconda/stargazers)
- [Setup NativeScript](https://github.com/hrueger/setup-nativescript) [![GitHub stars](https://img.shields.io/github/stars/hrueger/setup-nativescript?style=flat)](https://github.com/hrueger/setup-nativescript/stargazers)
- [Create a JSON Environment File](https://github.com/schdck/create-env-json) [![GitHub stars](https://img.shields.io/github/stars/schdck/create-env-json?style=flat)](https://github.com/schdck/create-env-json/stargazers)

#### Dependencies

- [Install NPM Dependencies with Caching](https://github.com/bahmutov/npm-install) [![GitHub stars](https://img.shields.io/github/stars/bahmutov/npm-install?style=flat)](https://github.com/bahmutov/npm-install/stargazers)
- [Highlight New NPM Dependencies](https://github.com/hiwelo/new-dependencies-action) [![GitHub stars](https://img.shields.io/github/stars/hiwelo/new-dependencies-action?style=flat)](https://github.com/hiwelo/new-dependencies-action/stargazers) - Comments on pull requests newly added NPM dependencies information.
- [Cache NPM Dependencies](https://github.com/c-hive/gha-npm-cache) [![GitHub stars](https://img.shields.io/github/stars/c-hive/gha-npm-cache?style=flat)](https://github.com/c-hive/gha-npm-cache/stargazers)
- [Cache Yarn Dependencies](https://github.com/c-hive/gha-yarn-cache) [![GitHub stars](https://img.shields.io/github/stars/c-hive/gha-yarn-cache?style=flat)](https://github.com/c-hive/gha-yarn-cache/stargazers)

#### Semantic Versioning

- [Next SemVers](https://github.com/WyriHaximus/github-action-next-semvers) [![GitHub stars](https://img.shields.io/github/stars/WyriHaximus/github-action-next-semvers?style=flat)](https://github.com/WyriHaximus/github-action-next-semvers/stargazers) - Output the next version for major, minor, and patch version based on the given semver version.
- [Get latest SemVer and branch name given a search string](https://github.com/jessicalostinspace/github-action-get-regex-branch) [![GitHub stars](https://img.shields.io/github/stars/jessicalostinspace/github-action-get-regex-branch?style=flat)](https://github.com/jessicalostinspace/github-action-get-regex-branch/stargazers)
- [Cut Release Branch](https://github.com/jessicalostinspace/cut-release-action) [![GitHub stars](https://img.shields.io/github/stars/jessicalostinspace/cut-release-action?style=flat)](https://github.com/jessicalostinspace/cut-release-action/stargazers) - Cuts a release branch given a branch prefix and optional semantic version.
- [Increment Semantic Version](https://github.com/christian-draeger/increment-semantic-version) [![GitHub stars](https://img.shields.io/github/stars/christian-draeger/increment-semantic-version?style=flat)](https://github.com/christian-draeger/increment-semantic-version/stargazers) - Bump a given semantic version (SemVer), depending on given release type.

### Static Analysis

- [PHPStan Static code analyzer Action](https://github.com/OskarStark/phpstan-ga) [![GitHub stars](https://img.shields.io/github/stars/OskarStark/phpstan-ga?style=flat)](https://github.com/OskarStark/phpstan-ga/stargazers)
- [GraphQL Inspector Action](https://github.com/kamilkisiela/graphql-inspector) [![GitHub stars](https://img.shields.io/github/stars/kamilkisiela/graphql-inspector?style=flat)](https://github.com/kamilkisiela/graphql-inspector/stargazers)
- [PowerShell static analysis with PSScriptAnalyzer](https://github.com/devblackops/github-action-psscriptanalyzer) [![GitHub stars](https://img.shields.io/github/stars/devblackops/github-action-psscriptanalyzer?style=flat)](https://github.com/devblackops/github-action-psscriptanalyzer/stargazers)
- [Run tfsec, with reviewdog output on the PR](https://github.com/reviewdog/action-tfsec) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-tfsec?style=flat)](https://github.com/reviewdog/action-tfsec/stargazers)

#### Testing

- [Run Tests through Puppeteer, the Headless Chrome Node API](https://github.com/ianwalter/puppeteer) [![GitHub stars](https://img.shields.io/github/stars/ianwalter/puppeteer?style=flat)](https://github.com/ianwalter/puppeteer/stargazers)
- [xUnit Slack Reporter: Sends summary of tests from xUnit reports to a Slack channel](https://github.com/ivanklee86/xunit-slack-reporter) [![GitHub stars](https://img.shields.io/github/stars/ivanklee86/xunit-slack-reporter?style=flat)](https://github.com/ivanklee86/xunit-slack-reporter/stargazers)
- [Run codeception tests](https://github.com/joelwmale/codeception-action) [![GitHub stars](https://img.shields.io/github/stars/joelwmale/codeception-action?style=flat)](https://github.com/joelwmale/codeception-action/stargazers)
- [Run TestCafe tests](https://github.com/DevExpress/testcafe-action) [![GitHub stars](https://img.shields.io/github/stars/DevExpress/testcafe-action?style=flat)](https://github.com/DevExpress/testcafe-action/stargazers)
- [Run Unity tests](https://github.com/webbertakken/unity-test-runner) [![GitHub stars](https://img.shields.io/github/stars/webbertakken/unity-test-runner?style=flat)](https://github.com/webbertakken/unity-test-runner/stargazers)
- [Run Cypress E2E tests](https://github.com/cypress-io/github-action) [![GitHub stars](https://img.shields.io/github/stars/cypress-io/github-action?style=flat)](https://github.com/cypress-io/github-action/stargazers)
- [Test Ansible roles with Molecule](https://github.com/robertdebock/molecule-action) [![GitHub stars](https://img.shields.io/github/stars/robertdebock/molecule-action?style=flat)](https://github.com/robertdebock/molecule-action/stargazers)
- [Run performance testing with artillery.io](https://github.com/kenju/github-actions-artillery) [![GitHub stars](https://img.shields.io/github/stars/kenju/github-actions-artillery?style=flat)](https://github.com/kenju/github-actions-artillery/stargazers)
- [Detect Flaky Tests with BuildPulse](https://github.com/Workshop64/buildpulse-action) [![GitHub stars](https://img.shields.io/github/stars/Workshop64/buildpulse-action?style=flat)](https://github.com/Workshop64/buildpulse-action/stargazers)
- [Display Inline Code Annotations for Jest Tests](https://github.com/IgnusG/jest-report-action) [![GitHub stars](https://img.shields.io/github/stars/IgnusG/jest-report-action?style=flat)](https://github.com/IgnusG/jest-report-action/stargazers)
- [Run Julia tests](https://github.com/julia-actions/julia-runtest) [![GitHub stars](https://img.shields.io/github/stars/julia-actions/julia-runtest?style=flat)](https://github.com/julia-actions/julia-runtest/stargazers)

#### Linting

- [PHP Coding Standards Fixer Action](https://github.com/OskarStark/php-cs-fixer-ga) [![GitHub stars](https://img.shields.io/github/stars/OskarStark/php-cs-fixer-ga?style=flat)](https://github.com/OskarStark/php-cs-fixer-ga/stargazers)
- [Runs Hadolint against a Dockerfile within a repository](https://github.com/burdzwastaken/hadolint-action) [![GitHub stars](https://img.shields.io/github/stars/burdzwastaken/hadolint-action?style=flat)](https://github.com/burdzwastaken/hadolint-action/stargazers)
- [Run ESLint, with reviewdog output on the PR](https://github.com/reviewdog/action-eslint) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-eslint?style=flat)](https://github.com/reviewdog/action-eslint/stargazers)
- [JavaScript-based linter for \*.workflow files](https://github.com/OmarTawfik/github-actions-js) [![GitHub stars](https://img.shields.io/github/stars/OmarTawfik/github-actions-js?style=flat)](https://github.com/OmarTawfik/github-actions-js/stargazers)
- [Lint terraform files using tflint, with reviewdog output on the PR](https://github.com/reviewdog/action-tflint) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-tflint?style=flat)](https://github.com/reviewdog/action-tflint/stargazers)
- [autopep8: Automatically formats Python code to conform to the PEP 8 style guide](https://github.com/peter-evans/autopep8) [![GitHub stars](https://img.shields.io/github/stars/peter-evans/autopep8?style=flat)](https://github.com/peter-evans/autopep8/stargazers)
- [Run `ergebnis/composer-normalize` to ensure your PHP project has a normalized `composer.json`](https://github.com/ergebnis/composer-normalize-action) [![GitHub stars](https://img.shields.io/github/stars/ergebnis/composer-normalize-action?style=flat)](https://github.com/ergebnis/composer-normalize-action/stargazers)
- [Run `stolt/lean-package-validator` to ensure your package has only the required `runtime` artifacts](https://github.com/raphaelstolt/lean-package-validator-action) [![GitHub stars](https://img.shields.io/github/stars/raphaelstolt/lean-package-validator-action?style=flat)](https://github.com/raphaelstolt/lean-package-validator-action/stargazers)
- [Run Go lint checks on PR event](https://github.com/ArangoGutierrez/GoLinty-Action) [![GitHub stars](https://img.shields.io/github/stars/ArangoGutierrez/GoLinty-Action?style=flat)](https://github.com/ArangoGutierrez/GoLinty-Action/stargazers)
- [Node.js - Automatically run the `format` and/or `lint` script used by the package](https://github.com/MarvinJWendt/run-node-formatter) [![GitHub stars](https://img.shields.io/github/stars/MarvinJWendt/run-node-formatter?style=flat)](https://github.com/MarvinJWendt/run-node-formatter/stargazers)
- [Stylelinter - GitHub Action that runs stylelint](https://github.com/exelban/stylelint) [![GitHub stars](https://img.shields.io/github/stars/exelban/stylelint?style=flat)](https://github.com/exelban/stylelint/stargazers)
- [Run stylelint, with reviewdog output on the PR](https://github.com/reviewdog/action-stylelint) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-stylelint?style=flat)](https://github.com/reviewdog/action-stylelint/stargazers)
- [PyCodeStyle Action - A GitHub Action that leaves a comment on your PR with pycodestyle (autopep8) feedback](https://github.com/ankitvgupta/pycodestyle-action) [![GitHub stars](https://img.shields.io/github/stars/ankitvgupta/pycodestyle-action?style=flat)](https://github.com/ankitvgupta/pycodestyle-action/stargazers)
- [wemake-python-styleguide - The strictest and most opinionated python linter ever, with optional reviewdog output on the PR](https://github.com/wemake-services/wemake-python-styleguide) [![GitHub stars](https://img.shields.io/github/stars/wemake-services/wemake-python-styleguide?style=flat)](https://github.com/wemake-services/wemake-python-styleguide/stargazers)
- [Run TSLint with status checks and file diff annotations](https://github.com/mooyoul/tslint-actions) [![GitHub stars](https://img.shields.io/github/stars/mooyoul/tslint-actions?style=flat)](https://github.com/mooyoul/tslint-actions/stargazers)
- [Lint Pull Request commits with commitlint](https://github.com/wagoid/commitlint-github-action) [![GitHub stars](https://img.shields.io/github/stars/wagoid/commitlint-github-action?style=flat)](https://github.com/wagoid/commitlint-github-action/stargazers)
- [Run vint, with reviewdog output on the PR](https://github.com/reviewdog/action-vint) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-vint?style=flat)](https://github.com/reviewdog/action-vint/stargazers)
- [Run mispell, with reviewdog output on the PR](https://github.com/reviewdog/action-misspell) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-misspell?style=flat)](https://github.com/reviewdog/action-misspell/stargazers)
- [Run golangci-lint, with reviewdog output on the PR](https://github.com/reviewdog/action-golangci-lint) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-golangci-lint?style=flat)](https://github.com/reviewdog/action-golangci-lint/stargazers)
- [Run shellcheck, with reviewdog output on the PR](https://github.com/reviewdog/action-shellcheck) [![GitHub stars](https://img.shields.io/github/stars/reviewdog/action-shellcheck?style=flat)](https://github.com/reviewdog/action-shellcheck/stargazers)
- [Catch insensitive, inconsiderate writing in your markdown docs](https://github.com/theashraf/alex-action) [![GitHub stars](https://img.shields.io/github/stars/theashraf/alex-action?style=flat)](https://github.com/theashraf/alex-action/stargazers)
- [Run dotenv-linter - Lints your .env files like a charm, with optional reviewdog output on the PR](https://github.com/wemake-services/dotenv-linter) [![GitHub stars](https://img.shields.io/github/stars/wemake-services/dotenv-linter?style=flat)](https://github.com/wemake-services/dotenv-linter/stargazers)
- [Run dotenv-linter, with reviewdog output on the PR](https://github.com/mgrachev/action-dotenv-linter) [![GitHub stars](https://img.shields.io/github/stars/mgrachev/action-dotenv-linter?style=flat)](https://github.com/mgrachev/action-dotenv-linter/stargazers)
- [Show and auto-fix linting errors for many programming languages](https://github.com/samuelmeuli/lint-action) [![GitHub stars](https://img.shields.io/github/stars/samuelmeuli/lint-action?style=flat)](https://github.com/samuelmeuli/lint-action/stargazers)
- [PHP_CodeSniffer With Annotations](https://github.com/chekalsky/phpcs-action) [![GitHub stars](https://img.shields.io/github/stars/chekalsky/phpcs-action?style=flat)](https://github.com/chekalsky/phpcs-action/stargazers)
- [Linter for markdown (with presets)](https://github.com/avto-dev/markdown-lint) [![GitHub stars](https://img.shields.io/github/stars/avto-dev/markdown-lint?style=flat)](https://github.com/avto-dev/markdown-lint/stargazers)
- [Stylelint problem matcher to create annotations](https://github.com/xt0rted/stylelint-problem-matcher) [![GitHub stars](https://img.shields.io/github/stars/xt0rted/stylelint-problem-matcher?style=flat)](https://github.com/xt0rted/stylelint-problem-matcher/stargazers)
- [Run sqlcheck on the PR to identifies anti-patterns in SQL queries](https://github.com/yokawasa/action-sqlcheck) [![GitHub stars](https://img.shields.io/github/stars/yokawasa/action-sqlcheck?style=flat)](https://github.com/yokawasa/action-sqlcheck/stargazers)
- [Validate Fastlane Supply Metadata Against the Play Store Guidelines](https://github.com/ashutoshgngwr/validate-fastlane-supply-metadata) [![GitHub stars](https://img.shields.io/github/stars/ashutoshgngwr/validate-fastlane-supply-metadata?style=flat)](https://github.com/ashutoshgngwr/validate-fastlane-supply-metadata/stargazers)
- [Run Golint to lint your Golang code](https://github.com/Jerome1337/golint-action) [![GitHub stars](https://img.shields.io/github/stars/Jerome1337/golint-action?style=flat)](https://github.com/Jerome1337/golint-action/stargazers)

#### Security

- [A vulnerability scanner for your docker images](https://github.com/phonito/phonito-scanner-action) [![GitHub stars](https://img.shields.io/github/stars/phonito/phonito-scanner-action?style=flat)](https://github.com/phonito/phonito-scanner-action/stargazers)
- [Automatically approve and merge Dependabot updates](https://github.com/ridedott/dependabot-auto-merge-action) [![GitHub stars](https://img.shields.io/github/stars/ridedott/dependabot-auto-merge-action?style=flat)](https://github.com/ridedott/dependabot-auto-merge-action/stargazers)
- [Run dlint security linter on your Python code](https://github.com/xen0l/dlint-check) [![GitHub stars](https://img.shields.io/github/stars/xen0l/dlint-check?style=flat)](https://github.com/xen0l/dlint-check/stargazers)
- [AWS Secrets Manager Actions](https://github.com/say8425/aws-secrets-manager-actions) [![GitHub stars](https://img.shields.io/github/stars/say8425/aws-secrets-manager-actions?style=flat)](https://github.com/say8425/aws-secrets-manager-actions/stargazers) - Define AWS Secrets Manager secrets to environment values.
- [Linting your AWS IAM policy documents for correctness and security issues](https://github.com/xen0l/iam-lint) [![GitHub stars](https://img.shields.io/github/stars/xen0l/iam-lint?style=flat)](https://github.com/xen0l/iam-lint/stargazers)
- [Secret Spreader](https://github.com/webfactory/secret-spreader) [![GitHub stars](https://img.shields.io/github/stars/webfactory/secret-spreader?style=flat)](https://github.com/webfactory/secret-spreader/stargazers) - Not an action per se, but a tool to manage Actions Secrets across a list of repositories.
- [Secrets Sync Action](https://github.com/google/secrets-sync-action) [![GitHub stars](https://img.shields.io/github/stars/google/secrets-sync-action?style=flat)](https://github.com/google/secrets-sync-action/stargazers) - Action syncs secrets across multiple repositories.
- [Snyk Test Action](https://github.com/snyk/actions) [![GitHub stars](https://img.shields.io/github/stars/snyk/actions?style=flat)](https://github.com/snyk/actions/stargazers)
- [Manage Your GitHub Actions Secrets With A Simple CLI](https://github.com/unfor19/githubsecrets) [![GitHub stars](https://img.shields.io/github/stars/unfor19/githubsecrets?style=flat)](https://github.com/unfor19/githubsecrets/stargazers)
- [SecretHub](https://github.com/secrethub/actions) [![GitHub stars](https://img.shields.io/github/stars/secrethub/actions?style=flat)](https://github.com/secrethub/actions/stargazers) - Have a single source of truth for your secrets and load them into GitHub Actions on demand.

#### Code Coverage

- [Scan code with SonarCloud](https://github.com/sonarsource/sonarcloud-github-action) [![GitHub stars](https://img.shields.io/github/stars/sonarsource/sonarcloud-github-action?style=flat)](https://github.com/sonarsource/sonarcloud-github-action/stargazers)
- [Send your code coverage to codecov.io](https://github.com/codecov/codecov-action) [![GitHub stars](https://img.shields.io/github/stars/codecov/codecov-action?style=flat)](https://github.com/codecov/codecov-action/stargazers)
- [Publishing code coverage to CodeClimate](https://github.com/paambaati/codeclimate-action) [![GitHub stars](https://img.shields.io/github/stars/paambaati/codeclimate-action?style=flat)](https://github.com/paambaati/codeclimate-action/stargazers)
- [Update repository go report card](https://github.com/creekorful/goreportcard-action) [![GitHub stars](https://img.shields.io/github/stars/creekorful/goreportcard-action?style=flat)](https://github.com/creekorful/goreportcard-action/stargazers)

### Dynamic Analysis

- [Run Gofmt to check Golang code formatting](https://github.com/Jerome1337/gofmt-action) [![GitHub stars](https://img.shields.io/github/stars/Jerome1337/gofmt-action?style=flat)](https://github.com/Jerome1337/gofmt-action/stargazers)
- [Run Goimports to check Golang imports order](https://github.com/Jerome1337/goimports-action) [![GitHub stars](https://img.shields.io/github/stars/Jerome1337/goimports-action?style=flat)](https://github.com/Jerome1337/goimports-action/stargazers)

### Monitoring

- [Audit a webpage with Google Chrome's Lighthouse tests](https://github.com/jakejarvis/lighthouse-action) [![GitHub stars](https://img.shields.io/github/stars/jakejarvis/lighthouse-action?style=flat)](https://github.com/jakejarvis/lighthouse-action/stargazers)
- [Runs Lighthouse and posts results to PRs and Slack](https://github.com/foo-software/lighthouse-check-action) [![GitHub stars](https://img.shields.io/github/stars/foo-software/lighthouse-check-action?style=flat)](https://github.com/foo-software/lighthouse-check-action/stargazers)
- [Run Lighthouse in CI using GitHub Actions](https://github.com/treosh/lighthouse-ci-action) [![GitHub stars](https://img.shields.io/github/stars/treosh/lighthouse-ci-action?style=flat)](https://github.com/treosh/lighthouse-ci-action/stargazers)
- [Continuous Benchmarking and Benchmark Visualization for Go](https://github.com/bobheadxi/gobenchdata) [![GitHub stars](https://img.shields.io/github/stars/bobheadxi/gobenchdata?style=flat)](https://github.com/bobheadxi/gobenchdata/stargazers)
- [Size Limit Action](https://github.com/andresz1/size-limit-action) [![GitHub stars](https://img.shields.io/github/stars/andresz1/size-limit-action?style=flat)](https://github.com/andresz1/size-limit-action/stargazers) - Comments cost comparison of your JS in PRs and rejects them if limit is exceeded.
- [Check bundlephobia](https://github.com/carlesnunez/check-my-bundlephobia) [![GitHub stars](https://img.shields.io/github/stars/carlesnunez/check-my-bundlephobia?style=flat)](https://github.com/carlesnunez/check-my-bundlephobia/stargazers) - Comments new and modified package size according to bundlephobia.io website and rejects PR on threshold surpassed.

### Pull Requests

- [Set PR Reviewers Based on Assignees](https://github.com/pullreminders/assignee-to-reviewer-action) [![GitHub stars](https://img.shields.io/github/stars/pullreminders/assignee-to-reviewer-action?style=flat)](https://github.com/pullreminders/assignee-to-reviewer-action/stargazers)
- [Open or Update PR on Branch Push (with Branch Selection)](https://github.com/vsoch/pull-request-action) [![GitHub stars](https://img.shields.io/github/stars/vsoch/pull-request-action?style=flat)](https://github.com/vsoch/pull-request-action/stargazers)
- [Automatically Rebase a PR](https://github.com/cirrus-actions/rebase) [![GitHub stars](https://img.shields.io/github/stars/cirrus-actions/rebase?style=flat)](https://github.com/cirrus-actions/rebase/stargazers)
- [Label PR once it has a Specified Number of Approvals](https://github.com/pullreminders/label-when-approved-action) [![GitHub stars](https://img.shields.io/github/stars/pullreminders/label-when-approved-action?style=flat)](https://github.com/pullreminders/label-when-approved-action/stargazers)
- [Add Labels to a PR based on Matched File Patterns](https://github.com/banyan/auto-label) [![GitHub stars](https://img.shields.io/github/stars/banyan/auto-label?style=flat)](https://github.com/banyan/auto-label/stargazers)
- [Auto-Approve PRs](https://github.com/hmarr/auto-approve-action) [![GitHub stars](https://img.shields.io/github/stars/hmarr/auto-approve-action?style=flat)](https://github.com/hmarr/auto-approve-action/stargazers)
- [Automatically add Reviewers to PR based on the Configuration File](https://github.com/kentaro-m/auto-assign-action) [![GitHub stars](https://img.shields.io/github/stars/kentaro-m/auto-assign-action?style=flat)](https://github.com/kentaro-m/auto-assign-action/stargazers)
- [Add Labels to a PR based on Branch Name Patterns](https://github.com/TimonVS/pr-labeler-action) [![GitHub stars](https://img.shields.io/github/stars/TimonVS/pr-labeler-action?style=flat)](https://github.com/TimonVS/pr-labeler-action/stargazers)
- [Add Labels to a PR based on Total Size of the Diff](https://github.com/pascalgn/size-label-action) [![GitHub stars](https://img.shields.io/github/stars/pascalgn/size-label-action?style=flat)](https://github.com/pascalgn/size-label-action/stargazers)
- [Automatically merge PRs That Are Ready](https://github.com/pascalgn/automerge-action) [![GitHub stars](https://img.shields.io/github/stars/pascalgn/automerge-action?style=flat)](https://github.com/pascalgn/automerge-action/stargazers)
- [Verify That PRs Contain a Ticket Reference](https://github.com/vijaykramesh/pr-lint-action) [![GitHub stars](https://img.shields.io/github/stars/vijaykramesh/pr-lint-action?style=flat)](https://github.com/vijaykramesh/pr-lint-action/stargazers)
- [Create a PR for Changes to your Repository in the Actions Workspace](https://github.com/peter-evans/create-pull-request) [![GitHub stars](https://img.shields.io/github/stars/peter-evans/create-pull-request?style=flat)](https://github.com/peter-evans/create-pull-request/stargazers)
- [Lint a PR](https://github.com/seferov/pr-lint-action) [![GitHub stars](https://img.shields.io/github/stars/seferov/pr-lint-action?style=flat)](https://github.com/seferov/pr-lint-action/stargazers)
- [ChatOps for PRs](https://github.com/machine-learning-apps/actions-chatops) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/actions-chatops?style=flat)](https://github.com/machine-learning-apps/actions-chatops/stargazers)
- [Prefix Title and Body of a PR Based on Text Extracted from Branch Name](https://github.com/tzkhan/pr-update-action) [![GitHub stars](https://img.shields.io/github/stars/tzkhan/pr-update-action?style=flat)](https://github.com/tzkhan/pr-update-action/stargazers)
- [Block Autosquash Commits](https://github.com/xt0rted/block-autosquash-commits-action) [![GitHub stars](https://img.shields.io/github/stars/xt0rted/block-autosquash-commits-action?style=flat)](https://github.com/xt0rted/block-autosquash-commits-action/stargazers)
- [Automatically Bump and Tag on Merge](https://github.com/anothrNick/github-tag-action) [![GitHub stars](https://img.shields.io/github/stars/anothrNick/github-tag-action?style=flat)](https://github.com/anothrNick/github-tag-action/stargazers)
- [Automatically Update PRs with Outdated Checks and Squash and Merge the Ones Matching All Branch Protections](https://github.com/tibdex/autosquash) [![GitHub stars](https://img.shields.io/github/stars/tibdex/autosquash?style=flat)](https://github.com/tibdex/autosquash/stargazers)
- [Merge Pal - Automatically Update and Merge PRs](https://github.com/maxkomarychev/merge-pal-action) [![GitHub stars](https://img.shields.io/github/stars/maxkomarychev/merge-pal-action?style=flat)](https://github.com/maxkomarychev/merge-pal-action/stargazers)
- [Enforce naming convention on pull request title](https://github.com/deepakputhraya/action-pr-title) [![GitHub stars](https://img.shields.io/github/stars/deepakputhraya/action-pr-title?style=flat)](https://github.com/deepakputhraya/action-pr-title/stargazers)
- [Pull Request Stuck Notifier](https://github.com/jrylan/github-action-stuck-pr-notifier) [![GitHub stars](https://img.shields.io/github/stars/jrylan/github-action-stuck-pr-notifier?style=flat)](https://github.com/jrylan/github-action-stuck-pr-notifier/stargazers)
- [Lint pull request name with commitlint (Awesome if you squash merge !)](https://github.com/JulienKode/pull-request-name-linter-action) [![GitHub stars](https://img.shields.io/github/stars/JulienKode/pull-request-name-linter-action?style=flat)](https://github.com/JulienKode/pull-request-name-linter-action/stargazers)
- [Block PR merges when Checks for target branches are failing](https://github.com/cirrus-actions/branch-guard) [![GitHub stars](https://img.shields.io/github/stars/cirrus-actions/branch-guard?style=flat)](https://github.com/cirrus-actions/branch-guard/stargazers)
- [Get generated static site screenshots updated by Pull Request](https://github.com/ssowonny/diff-pages-action) [![GitHub stars](https://img.shields.io/github/stars/ssowonny/diff-pages-action?style=flat)](https://github.com/ssowonny/diff-pages-action/stargazers)
- [Add Labels Depending if the Pull Request Still in Progress](https://github.com/AlbertHernandez/working-label-action) [![GitHub stars](https://img.shields.io/github/stars/AlbertHernandez/working-label-action?style=flat)](https://github.com/AlbertHernandez/working-label-action/stargazers)
- [Ticket Check Action](https://github.com/neofinancial/ticket-check-action) [![GitHub stars](https://img.shields.io/github/stars/neofinancial/ticket-check-action?style=flat)](https://github.com/neofinancial/ticket-check-action/stargazers) - Automatically add a ticket or issue number to the start of all Pull Request titles.
- [Pull Request Lint With Regex](https://github.com/MorrisonCole/pr-lint-action) [![GitHub stars](https://img.shields.io/github/stars/MorrisonCole/pr-lint-action?style=flat)](https://github.com/MorrisonCole/pr-lint-action/stargazers)
- [Pull Request Landmines](https://github.com/tylermurry/github-pr-landmine) [![GitHub stars](https://img.shields.io/github/stars/tylermurry/github-pr-landmine?style=flat)](https://github.com/tylermurry/github-pr-landmine/stargazers)
- [Annotate a GitHub Pull Request Based on a Checkstyle XML-Report](https://github.com/staabm/annotate-pull-request-from-checkstyle) [![GitHub stars](https://img.shields.io/github/stars/staabm/annotate-pull-request-from-checkstyle?style=flat)](https://github.com/staabm/annotate-pull-request-from-checkstyle/stargazers)
- [Pull Request Stats](https://github.com/flowwer-dev/pull-request-stats) [![GitHub stars](https://img.shields.io/github/stars/flowwer-dev/pull-request-stats?style=flat)](https://github.com/flowwer-dev/pull-request-stats/stargazers) -  Print relevant stats about reviewers.
- [Pull Request Description Enforcer](https://github.com/derkinderfietsen/pr-description-enforcer) [![GitHub stars](https://img.shields.io/github/stars/derkinderfietsen/pr-description-enforcer?style=flat)](https://github.com/derkinderfietsen/pr-description-enforcer/stargazers) - Enforces description on pull requests.

### GitHub Pages

- [Deploy a Zola site to GitHub Pages](https://github.com/shalzz/zola-deploy-action) [![GitHub stars](https://img.shields.io/github/stars/shalzz/zola-deploy-action?style=flat)](https://github.com/shalzz/zola-deploy-action/stargazers)
- [Build Hugo static content site and publish it to gh-pages branch](https://github.com/khanhicetea/gh-actions-hugo-deploy-gh-pages) [![GitHub stars](https://img.shields.io/github/stars/khanhicetea/gh-actions-hugo-deploy-gh-pages?style=flat)](https://github.com/khanhicetea/gh-actions-hugo-deploy-gh-pages/stargazers)
- [Build a Jekyll site—with Custom Jekyll Plugins & Build Scripts—and deploy it back to the Gh-Pages Branch](https://github.com/BryanSchuetz/jekyll-deploy-gh-pages) [![GitHub stars](https://img.shields.io/github/stars/BryanSchuetz/jekyll-deploy-gh-pages?style=flat)](https://github.com/BryanSchuetz/jekyll-deploy-gh-pages/stargazers)
- [Google Dataset Search Metadata](https://www.github.com/openschemas/extractors/) - And other schema.org extractors to make datasets discoverable from GitHub pages.
- [GitHub Actions for deploying to GitHub Pages with Static Site Generators](https://github.com/peaceiris/actions-gh-pages) [![GitHub stars](https://img.shields.io/github/stars/peaceiris/actions-gh-pages?style=flat)](https://github.com/peaceiris/actions-gh-pages/stargazers)
- [GitHub Action for Hexo](https://github.com/heowc/action-hexo) [![GitHub stars](https://img.shields.io/github/stars/heowc/action-hexo?style=flat)](https://github.com/heowc/action-hexo/stargazers)
- [Deploy Google Analytics stats to GitHub Pages](https://github.com/cristianpb/analytics-google) [![GitHub stars](https://img.shields.io/github/stars/cristianpb/analytics-google?style=flat)](https://github.com/cristianpb/analytics-google/stargazers)
- [A Jupyter Notebook Blogging Platform Powered by GitHub Actions, Pages and Jekyll](https://github.com/fastai/fastpages) [![GitHub stars](https://img.shields.io/github/stars/fastai/fastpages?style=flat)](https://github.com/fastai/fastpages/stargazers)
- [Deploy A Static Site to GitHub Pages](https://github.com/appleboy/gh-pages-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/gh-pages-action?style=flat)](https://github.com/appleboy/gh-pages-action/stargazers) - Deploy to custom directory and ignore folder/file.
- [Deploy to GitHub Pages with Advanced Settings](https://github.com/crazy-max/ghaction-github-pages) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-github-pages?style=flat)](https://github.com/crazy-max/ghaction-github-pages/stargazers)

### Notifications and Messages

- [Send a Discord notification](https://github.com/Ilshidur/action-discord) [![GitHub stars](https://img.shields.io/github/stars/Ilshidur/action-discord?style=flat)](https://github.com/Ilshidur/action-discord/stargazers)
- [Post a Slack message as a bot](https://github.com/pullreminders/slack-action) [![GitHub stars](https://img.shields.io/github/stars/pullreminders/slack-action?style=flat)](https://github.com/pullreminders/slack-action/stargazers)
- [Send an SMS from GitHub Actions using Nexmo](https://github.com/nexmo-community/nexmo-sms-action) [![GitHub stars](https://img.shields.io/github/stars/nexmo-community/nexmo-sms-action?style=flat)](https://github.com/nexmo-community/nexmo-sms-action/stargazers)
- [Send an SMS from GitHub Actions using Clockworksms](https://github.com/bharathvaj1995/clockwork-sms-action) [![GitHub stars](https://img.shields.io/github/stars/bharathvaj1995/clockwork-sms-action?style=flat)](https://github.com/bharathvaj1995/clockwork-sms-action/stargazers)
- [Send a Telegram Message](https://github.com/appleboy/telegram-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/telegram-action?style=flat)](https://github.com/appleboy/telegram-action/stargazers)
- [Send a File or Text Message to Discord (custom define color, username or avatar)](https://github.com/appleboy/discord-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/discord-action?style=flat)](https://github.com/appleboy/discord-action/stargazers)
- [Collaborate on tweets using pull requests](https://github.com/gr2m/twitter-together) [![GitHub stars](https://img.shields.io/github/stars/gr2m/twitter-together?style=flat)](https://github.com/gr2m/twitter-together/stargazers)
- [Send a Push Notification via Push by Techulus](https://github.com/techulus/push-github-action) [![GitHub stars](https://img.shields.io/github/stars/techulus/push-github-action?style=flat)](https://github.com/techulus/push-github-action/stargazers)
- [Send email with SendGrid](https://github.com/peter-evans/sendgrid-action) [![GitHub stars](https://img.shields.io/github/stars/peter-evans/sendgrid-action?style=flat)](https://github.com/peter-evans/sendgrid-action/stargazers)
- [Send a Push Notification via Join](https://github.com/ShaunLWM/action-join) [![GitHub stars](https://img.shields.io/github/stars/ShaunLWM/action-join?style=flat)](https://github.com/ShaunLWM/action-join/stargazers)
- [New package version checker for npm](https://github.com/MeilCli/npm-update-check-action) [![GitHub stars](https://img.shields.io/github/stars/MeilCli/npm-update-check-action?style=flat)](https://github.com/MeilCli/npm-update-check-action/stargazers)
- [New package version checker for NuGet](https://github.com/MeilCli/nuget-update-check-action) [![GitHub stars](https://img.shields.io/github/stars/MeilCli/nuget-update-check-action?style=flat)](https://github.com/MeilCli/nuget-update-check-action/stargazers)
- [New package version checker for Gradle](https://github.com/MeilCli/gradle-update-check-action) [![GitHub stars](https://img.shields.io/github/stars/MeilCli/gradle-update-check-action?style=flat)](https://github.com/MeilCli/gradle-update-check-action/stargazers)
- [Send a Push Notification via Pushbullet](https://github.com/ShaunLWM/action-pushbullet) [![GitHub stars](https://img.shields.io/github/stars/ShaunLWM/action-pushbullet?style=flat)](https://github.com/ShaunLWM/action-pushbullet/stargazers)
- [Create an Outlook Calendar Event using Microsoft Graph](https://github.com/anoopt/ms-graph-create-event) [![GitHub stars](https://img.shields.io/github/stars/anoopt/ms-graph-create-event?style=flat)](https://github.com/anoopt/ms-graph-create-event/stargazers)
- [Watch for GitHub Wiki page changes and post to Slack](https://github.com/benmatselby/gollum-page-watcher-action) [![GitHub stars](https://img.shields.io/github/stars/benmatselby/gollum-page-watcher-action?style=flat)](https://github.com/benmatselby/gollum-page-watcher-action/stargazers)
- [Send an SMS using MessageBird](https://github.com/nikitasavinov/messagebird-sms-action) [![GitHub stars](https://img.shields.io/github/stars/nikitasavinov/messagebird-sms-action?style=flat)](https://github.com/nikitasavinov/messagebird-sms-action/stargazers)
- [Reply to Stale Bots](https://github.com/c-hive/fresh-bot) [![GitHub stars](https://img.shields.io/github/stars/c-hive/fresh-bot?style=flat)](https://github.com/c-hive/fresh-bot/stargazers)
- [Send an Embed Message to Discord](https://github.com/sarisia/actions-status-discord) [![GitHub stars](https://img.shields.io/github/stars/sarisia/actions-status-discord?style=flat)](https://github.com/sarisia/actions-status-discord/stargazers)
- [Keep Your PRs in Sync With Teamwork Tasks](https://github.com/Teamwork/github-sync) [![GitHub stars](https://img.shields.io/github/stars/Teamwork/github-sync?style=flat)](https://github.com/Teamwork/github-sync/stargazers)
- [Send Microsoft Teams Notification](https://github.com/opsless/ms-teams-github-actions) [![GitHub stars](https://img.shields.io/github/stars/opsless/ms-teams-github-actions?style=flat)](https://github.com/opsless/ms-teams-github-actions/stargazers)

### Deployment

- [Deploy to Netlify](https://github.com/netlify/actions) [![GitHub stars](https://img.shields.io/github/stars/netlify/actions?style=flat)](https://github.com/netlify/actions/stargazers)
- [Deploy a Probot App using Actions](https://probot.github.io/docs/deployment/#github-actions)
- [Deploy a playlist to Spotify](https://github.com/swinton/SpotHub) [![GitHub stars](https://img.shields.io/github/stars/swinton/SpotHub?style=flat)](https://github.com/swinton/SpotHub/stargazers)
- [Deploy VS Code extensions with vsce](https://github.com/lannonbr/vsce-action) [![GitHub stars](https://img.shields.io/github/stars/lannonbr/vsce-action?style=flat)](https://github.com/lannonbr/vsce-action/stargazers)
- [Purge Cloudflare cache after updating a website](https://github.com/jakejarvis/cloudflare-purge-action) [![GitHub stars](https://img.shields.io/github/stars/jakejarvis/cloudflare-purge-action?style=flat)](https://github.com/jakejarvis/cloudflare-purge-action/stargazers)
- [Deploy your DNS configuration using DNS Control](https://github.com/koenrh/dnscontrol-action) [![GitHub stars](https://img.shields.io/github/stars/koenrh/dnscontrol-action?style=flat)](https://github.com/koenrh/dnscontrol-action/stargazers)
- [Deploy a Theme to Shopify](https://github.com/pgrimaud/action-shopify) [![GitHub stars](https://img.shields.io/github/stars/pgrimaud/action-shopify?style=flat)](https://github.com/pgrimaud/action-shopify/stargazers)
- [Trigger multiple GitLab CI Pipeline](https://github.com/appleboy/gitlab-ci-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/gitlab-ci-action?style=flat)](https://github.com/appleboy/gitlab-ci-action/stargazers)
- [Trigger multiple Jenkins Jobs](https://github.com/appleboy/jenkins-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/jenkins-action?style=flat)](https://github.com/appleboy/jenkins-action/stargazers)
- [GitHub Action for Homebrew Tap](https://github.com/izumin5210/action-homebrew-tap) [![GitHub stars](https://img.shields.io/github/stars/izumin5210/action-homebrew-tap?style=flat)](https://github.com/izumin5210/action-homebrew-tap/stargazers)
- [Copy files and artifacts via SSH](https://github.com/appleboy/scp-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/scp-action?style=flat)](https://github.com/appleboy/scp-action/stargazers)
- [Executing remote ssh commands](https://github.com/appleboy/ssh-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/ssh-action?style=flat)](https://github.com/appleboy/ssh-action/stargazers)
- [Publish a Python distribution package to PyPI](https://github.com/pypa/gh-action-pypi-publish) [![GitHub stars](https://img.shields.io/github/stars/pypa/gh-action-pypi-publish?style=flat)](https://github.com/pypa/gh-action-pypi-publish/stargazers)
- [Deploy Static Website to Azure Storage](https://github.com/feeloor/azure-static-website-deploy) [![GitHub stars](https://img.shields.io/github/stars/feeloor/azure-static-website-deploy?style=flat)](https://github.com/feeloor/azure-static-website-deploy/stargazers)
- [Cross platform Chocolatey CLI to build and publish packages](https://github.com/crazy-max/ghaction-chocolatey) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-chocolatey?style=flat)](https://github.com/crazy-max/ghaction-chocolatey/stargazers)
- [Deploy iOS Pod Library to Cocoapods](https://github.com/michaelhenry/deploy-to-cocoapods-github-action) [![GitHub stars](https://img.shields.io/github/stars/michaelhenry/deploy-to-cocoapods-github-action?style=flat)](https://github.com/michaelhenry/deploy-to-cocoapods-github-action/stargazers)
- [GitHub Action for TencentCloud Serverless](https://github.com/Juliiii/action-scf) [![GitHub stars](https://img.shields.io/github/stars/Juliiii/action-scf?style=flat)](https://github.com/Juliiii/action-scf/stargazers)
- [Publish npm (pre)releases](https://github.com/epeli/npm-release/) [![GitHub stars](https://img.shields.io/github/stars/epeli/npm-release/?style=flat)](https://github.com/epeli/npm-release//stargazers)
- [Deploy a static site to Surge.sh](https://github.com/yavisht/deploy-via-surge.sh-github-action-template) [![GitHub stars](https://img.shields.io/github/stars/yavisht/deploy-via-surge.sh-github-action-template?style=flat)](https://github.com/yavisht/deploy-via-surge.sh-github-action-template/stargazers)
- [GitHub Action for GoReleaser, a release automation tool for Go projects](https://github.com/goreleaser/goreleaser-action) [![GitHub stars](https://img.shields.io/github/stars/goreleaser/goreleaser-action?style=flat)](https://github.com/goreleaser/goreleaser-action/stargazers)
- [FTP Deploy Action, Deploys a GitHub project to a FTP server using GitHub actions](https://github.com/SamKirkland/FTP-Deploy-Action) [![GitHub stars](https://img.shields.io/github/stars/SamKirkland/FTP-Deploy-Action?style=flat)](https://github.com/SamKirkland/FTP-Deploy-Action/stargazers)
- [Publish Article to Dev.to](https://github.com/tylerauerbeck/publish-to-dev.to-action) [![GitHub stars](https://img.shields.io/github/stars/tylerauerbeck/publish-to-dev.to-action?style=flat)](https://github.com/tylerauerbeck/publish-to-dev.to-action/stargazers)
- [Action For Semantic Release](https://github.com/cycjimmy/semantic-release-action) [![GitHub stars](https://img.shields.io/github/stars/cycjimmy/semantic-release-action?style=flat)](https://github.com/cycjimmy/semantic-release-action/stargazers)
- [Deploy a Collection to Ansible Galaxy](https://github.com/artis3n/ansible_galaxy_collection) [![GitHub stars](https://img.shields.io/github/stars/artis3n/ansible_galaxy_collection?style=flat)](https://github.com/artis3n/ansible_galaxy_collection/stargazers)
- [Publish module to Puppet Forge](https://github.com/barnumbirr/action-forge-publish) [![GitHub stars](https://img.shields.io/github/stars/barnumbirr/action-forge-publish?style=flat)](https://github.com/barnumbirr/action-forge-publish/stargazers)
- [Build and publish Electron apps](https://github.com/samuelmeuli/action-electron-builder) [![GitHub stars](https://img.shields.io/github/stars/samuelmeuli/action-electron-builder?style=flat)](https://github.com/samuelmeuli/action-electron-builder/stargazers)
- [Publish a Maven package](https://github.com/samuelmeuli/action-maven-publish) [![GitHub stars](https://img.shields.io/github/stars/samuelmeuli/action-maven-publish?style=flat)](https://github.com/samuelmeuli/action-maven-publish/stargazers)
- [Build and deploy a theme to Ghost CMS](https://github.com/TryGhost/action-deploy-theme) [![GitHub stars](https://img.shields.io/github/stars/TryGhost/action-deploy-theme?style=flat)](https://github.com/TryGhost/action-deploy-theme/stargazers)
- [Deploy an Ansible role to Ansible Galaxy](https://github.com/robertdebock/galaxy-action) [![GitHub stars](https://img.shields.io/github/stars/robertdebock/galaxy-action?style=flat)](https://github.com/robertdebock/galaxy-action/stargazers)
- [Publish one or more JS modules to a registry](https://github.com/author/action-publish) [![GitHub stars](https://img.shields.io/github/stars/author/action-publish?style=flat)](https://github.com/author/action-publish/stargazers)
- [Publish a package with 2FA using Slack](https://github.com/erezrokah/2fa-with-slack-action) [![GitHub stars](https://img.shields.io/github/stars/erezrokah/2fa-with-slack-action?style=flat)](https://github.com/erezrokah/2fa-with-slack-action/stargazers)
- [Serialize Workflow Runs in Continuous Deployment Pipelines](https://github.com/softprops/turnstyle) [![GitHub stars](https://img.shields.io/github/stars/softprops/turnstyle?style=flat)](https://github.com/softprops/turnstyle/stargazers)
- [Netlify Deploy GitHub Action for each commit](https://github.com/nwtgck/actions-netlify) [![GitHub stars](https://img.shields.io/github/stars/nwtgck/actions-netlify?style=flat)](https://github.com/nwtgck/actions-netlify/stargazers)
- [Run Ansible Playbooks](https://github.com/arillso/action.playbook) [![GitHub stars](https://img.shields.io/github/stars/arillso/action.playbook?style=flat)](https://github.com/arillso/action.playbook/stargazers)
- [Publish a Python Distribution Package to Anaconda Cloud](https://github.com/fcakyon/conda-publish-action) [![GitHub stars](https://img.shields.io/github/stars/fcakyon/conda-publish-action?style=flat)](https://github.com/fcakyon/conda-publish-action/stargazers)
- [Deploy VS Code Extension to Visual Studio Marketplace or the Open VSX Registry](https://github.com/HaaLeo/publish-vscode-extension) [![GitHub stars](https://img.shields.io/github/stars/HaaLeo/publish-vscode-extension?style=flat)](https://github.com/HaaLeo/publish-vscode-extension/stargazers)
- [Deploy a YouTube Video to Anchor.fm Podcast](https://github.com/Schrodinger-Hat/youtube-to-anchorfm) [![GitHub stars](https://img.shields.io/github/stars/Schrodinger-Hat/youtube-to-anchorfm?style=flat)](https://github.com/Schrodinger-Hat/youtube-to-anchorfm/stargazers)
- [Deploy with AWS CodeDeploy](https://github.com/webfactory/create-aws-codedeploy-deployment) [![GitHub stars](https://img.shields.io/github/stars/webfactory/create-aws-codedeploy-deployment?style=flat)](https://github.com/webfactory/create-aws-codedeploy-deployment/stargazers)

#### Docker

- [Update a Docker Hub repository description from README.md](https://github.com/peter-evans/dockerhub-description) [![GitHub stars](https://img.shields.io/github/stars/peter-evans/dockerhub-description?style=flat)](https://github.com/peter-evans/dockerhub-description/stargazers)
- [Publish Docker Images to the GitHub Package Registry (GPR)](https://github.com/machine-learning-apps/gpr-docker-publish) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/gpr-docker-publish?style=flat)](https://github.com/machine-learning-apps/gpr-docker-publish/stargazers)
- [Update a repository's "Full description" on Docker Hub](https://github.com/mpepping/github-actions/tree/master/docker-hub-metadata) [![GitHub stars](https://img.shields.io/github/stars/mpepping/github-actions/tree/master/docker-hub-metadata?style=flat)](https://github.com/mpepping/github-actions/tree/master/docker-hub-metadata/stargazers)
- [Build and publish docker images to any registry using Kaniko](https://github.com/outillage/kaniko-action) [![GitHub stars](https://img.shields.io/github/stars/outillage/kaniko-action?style=flat)](https://github.com/outillage/kaniko-action/stargazers)
- [Monitor and limit your docker image size](https://github.com/wemake-services/docker-image-size-limit) [![GitHub stars](https://img.shields.io/github/stars/wemake-services/docker-image-size-limit?style=flat)](https://github.com/wemake-services/docker-image-size-limit/stargazers)
- [Publish Docker Images to the Amazon Elastic Container Registry (ECR)](https://github.com/appleboy/docker-ecr-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/docker-ecr-action?style=flat)](https://github.com/appleboy/docker-ecr-action/stargazers)
- [Build And Push Your Docker Images Caching Each Stage To Reduce Build Time](https://github.com/whoan/docker-build-with-cache-action) [![GitHub stars](https://img.shields.io/github/stars/whoan/docker-build-with-cache-action?style=flat)](https://github.com/whoan/docker-build-with-cache-action/stargazers)
- [Set up Docker Buildx](https://github.com/crazy-max/ghaction-docker-buildx) [![GitHub stars](https://img.shields.io/github/stars/crazy-max/ghaction-docker-buildx?style=flat)](https://github.com/crazy-max/ghaction-docker-buildx/stargazers)
- [Convert Branch or Tag Name Into Docker-Compatible Image Tag](https://github.com/ankitvgupta/ref-to-tag-action/) [![GitHub stars](https://img.shields.io/github/stars/ankitvgupta/ref-to-tag-action/?style=flat)](https://github.com/ankitvgupta/ref-to-tag-action//stargazers)
- [Update a Container Repository Description From README.md](https://github.com/marketplace/actions/update-container-description-action) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/update-container-description-action?style=flat)](https://github.com/marketplace/actions/update-container-description-action/stargazers) - Supported Registries: Docker Hub, Quay, Harbor.

#### Kubernetes

- [Deploy to any Cloud or Kubernetes Using Pulumi](https://github.com/pulumi/actions) [![GitHub stars](https://img.shields.io/github/stars/pulumi/actions?style=flat)](https://github.com/pulumi/actions/stargazers)
- [Deploy to Kubernetes with kubectl](https://github.com/steebchen/kubectl) [![GitHub stars](https://img.shields.io/github/stars/steebchen/kubectl?style=flat)](https://github.com/steebchen/kubectl/stargazers)
- [Get Kubeconfig File From Google Kubernetes Engine (GKE)](https://github.com/machine-learning-apps/gke-kubeconfig) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/gke-kubeconfig?style=flat)](https://github.com/machine-learning-apps/gke-kubeconfig/stargazers)
- [Kustomize Kubernetes Config YAMLs](https://github.com/karancode/kustomize-github-action) [![GitHub stars](https://img.shields.io/github/stars/karancode/kustomize-github-action?style=flat)](https://github.com/karancode/kustomize-github-action/stargazers)
- [Create a Kubernetes Cluster for Testing Using Krucible](https://github.com/Krucible/krucible-github-action) [![GitHub stars](https://img.shields.io/github/stars/Krucible/krucible-github-action?style=flat)](https://github.com/Krucible/krucible-github-action/stargazers)

#### AWS

- [Sync/upload a directory to an AWS S3 bucket](https://github.com/jakejarvis/s3-sync-action) [![GitHub stars](https://img.shields.io/github/stars/jakejarvis/s3-sync-action?style=flat)](https://github.com/jakejarvis/s3-sync-action/stargazers)
- [Deploy Lambda code to an existing function](https://github.com/appleboy/lambda-action) [![GitHub stars](https://img.shields.io/github/stars/appleboy/lambda-action?style=flat)](https://github.com/appleboy/lambda-action/stargazers)

#### Terraform

- [Generate terraform documentation](https://github.com/Dirrk/terraform-docs) [![GitHub stars](https://img.shields.io/github/stars/Dirrk/terraform-docs?style=flat)](https://github.com/Dirrk/terraform-docs/stargazers) - Uses terraform-docs to generate docs for terraform modules.
- [An example of using Terraform to validate and apply GitHub administration](https://github.com/asgharlabs/github-terraform/tree/master/.github/workflows) [![GitHub stars](https://img.shields.io/github/stars/asgharlabs/github-terraform/tree/master/.github/workflows?style=flat)](https://github.com/asgharlabs/github-terraform/tree/master/.github/workflows/stargazers)

### External Services

- [Use a Jenkinsfile](https://github.com/jonico/jenkinsfile-runner-github-actions) [![GitHub stars](https://img.shields.io/github/stars/jonico/jenkinsfile-runner-github-actions?style=flat)](https://github.com/jonico/jenkinsfile-runner-github-actions/stargazers)
- [GitHub Action for Firebase](https://github.com/w9jds/firebase-action) [![GitHub stars](https://img.shields.io/github/stars/w9jds/firebase-action?style=flat)](https://github.com/w9jds/firebase-action/stargazers)
- [GitHub Action for Contentful Migration CLI](https://github.com/Shy/contentful-action) [![GitHub stars](https://img.shields.io/github/stars/Shy/contentful-action?style=flat)](https://github.com/Shy/contentful-action/stargazers)
- [GitHub Actions for Pixela (a-know/pi)](https://github.com/peaceiris/actions-pixela) [![GitHub stars](https://img.shields.io/github/stars/peaceiris/actions-pixela?style=flat)](https://github.com/peaceiris/actions-pixela/stargazers)
- [GitHub Action for Google Cloud Platform (GCP)](https://github.com/exelban/gcloud) [![GitHub stars](https://img.shields.io/github/stars/exelban/gcloud?style=flat)](https://github.com/exelban/gcloud/stargazers)
- [Upload files to any OpenStack Swift service provider](https://github.com/iksaku/openstack-swift-action) [![GitHub stars](https://img.shields.io/github/stars/iksaku/openstack-swift-action?style=flat)](https://github.com/iksaku/openstack-swift-action/stargazers)
- [GitHub Action for sending Stack Overflow posts to Slack](https://github.com/logankilpatrick/StackOverflowBot) [![GitHub stars](https://img.shields.io/github/stars/logankilpatrick/StackOverflowBot?style=flat)](https://github.com/logankilpatrick/StackOverflowBot/stargazers)
- [Assume AWS role](https://github.com/nordcloud/aws-assume-role/) [![GitHub stars](https://img.shields.io/github/stars/nordcloud/aws-assume-role/?style=flat)](https://github.com/nordcloud/aws-assume-role//stargazers)
- [Generate Custom Response using JSONbin](https://github.com/fabasoad/jsonbin-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/jsonbin-action?style=flat)](https://github.com/fabasoad/jsonbin-action/stargazers)

### Frontend Tools

- [Execute Gradle task](https://github.com/MrRamych/gradle-actions) [![GitHub stars](https://img.shields.io/github/stars/MrRamych/gradle-actions?style=flat)](https://github.com/MrRamych/gradle-actions/stargazers)
- [JS Build Actions](https://github.com/elstudio/actions-js-build) [![GitHub stars](https://img.shields.io/github/stars/elstudio/actions-js-build?style=flat)](https://github.com/elstudio/actions-js-build/stargazers) - Run Grunt or Gulp build tasks and commit file changes.
- [GitHub Action for Gatsby CLI](https://github.com/jzweifel/gatsby-cli-github-action) [![GitHub stars](https://img.shields.io/github/stars/jzweifel/gatsby-cli-github-action?style=flat)](https://github.com/jzweifel/gatsby-cli-github-action/stargazers)
- [Runs a WebPageTest audit and prints the results as commit comment](https://github.com/JCofman/webPagetestAction) [![GitHub stars](https://img.shields.io/github/stars/JCofman/webPagetestAction?style=flat)](https://github.com/JCofman/webPagetestAction/stargazers)
- [GitHub Actions for Hugo extended](https://github.com/peaceiris/actions-hugo) [![GitHub stars](https://img.shields.io/github/stars/peaceiris/actions-hugo?style=flat)](https://github.com/peaceiris/actions-hugo/stargazers)
- [Generate OG Image](https://github.com/BoyWithSilverWings/generate-og-image) [![GitHub stars](https://img.shields.io/github/stars/BoyWithSilverWings/generate-og-image?style=flat)](https://github.com/BoyWithSilverWings/generate-og-image/stargazers) - Generate customisable open graph images from Markdown files.
- [GitHub Actions for mdBook](https://github.com/peaceiris/actions-mdbook) [![GitHub stars](https://img.shields.io/github/stars/peaceiris/actions-mdbook?style=flat)](https://github.com/peaceiris/actions-mdbook/stargazers)
- [Setup Mint](https://github.com/fabasoad/setup-mint-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/setup-mint-action?style=flat)](https://github.com/fabasoad/setup-mint-action/stargazers) - Setup Mint (programming language for writing single page applications).
- [Gatsby AWS S3 Deployment](https://github.com/jonelantha/gatsby-s3-action) [![GitHub stars](https://img.shields.io/github/stars/jonelantha/gatsby-s3-action?style=flat)](https://github.com/jonelantha/gatsby-s3-action/stargazers) - Deploy Gatsby to S3 (supports CloudFront).

### Machine Learning Ops

- [Submitting Argo Workflows (Cloud Agnostic)](https://github.com/machine-learning-apps/actions-argo) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/actions-argo?style=flat)](https://github.com/machine-learning-apps/actions-argo/stargazers)
- [Submitting Argo Workflows to GKE](https://github.com/machine-learning-apps/gke-argo) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/gke-argo?style=flat)](https://github.com/machine-learning-apps/gke-argo/stargazers)
- [Query Experiment Tracking Results From Weights & Biases](https://github.com/machine-learning-apps/wandb-action) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/wandb-action?style=flat)](https://github.com/machine-learning-apps/wandb-action/stargazers)
- [Run Parameterized Jupyter Notebooks](https://github.com/yaananth/run-notebook) [![GitHub stars](https://img.shields.io/github/stars/yaananth/run-notebook?style=flat)](https://github.com/yaananth/run-notebook/stargazers)
- [Compile, Deploy and Run Kubeflow Pipeline](https://github.com/NikeNano/kubeflow-github-action) [![GitHub stars](https://img.shields.io/github/stars/NikeNano/kubeflow-github-action?style=flat)](https://github.com/NikeNano/kubeflow-github-action/stargazers)
- [Automatically Dockerize A Data-Science Repo As A Jupyter Server](https://github.com/jupyterhub/repo2docker-action) [![GitHub stars](https://img.shields.io/github/stars/jupyterhub/repo2docker-action?style=flat)](https://github.com/jupyterhub/repo2docker-action/stargazers)
- [Azure Machine Learning With GitHub Actions](https://github.com/machine-learning-apps/ml-template-azure) [![GitHub stars](https://img.shields.io/github/stars/machine-learning-apps/ml-template-azure?style=flat)](https://github.com/machine-learning-apps/ml-template-azure/stargazers)

### Build

- [run-cmake](https://github.com/lukka/run-cmake) [![GitHub stars](https://img.shields.io/github/stars/lukka/run-cmake?style=flat)](https://github.com/lukka/run-cmake/stargazers) - Multi platform action to build C/C++ software with [CMake](https://cmake.org) and [Ninja](https://ninja-build.org/).
- [run-vcpkg](https://github.com/lukka/run-vcpkg) [![GitHub stars](https://img.shields.io/github/stars/lukka/run-vcpkg?style=flat)](https://github.com/lukka/run-vcpkg/stargazers) - Multi platform action to build and install C/C++ dependencies with [vcpkg](https://github.com/microsoft/vcpkg) [![GitHub stars](https://img.shields.io/github/stars/microsoft/vcpkg?style=flat)](https://github.com/microsoft/vcpkg/stargazers).
- [Build Go applications for multiplatform](https://github.com/izumin5210/action-go-crossbuild) [![GitHub stars](https://img.shields.io/github/stars/izumin5210/action-go-crossbuild?style=flat)](https://github.com/izumin5210/action-go-crossbuild/stargazers)
- [Generate ~/.m2/settings.xml for Maven builds](https://github.com/whelk-io/maven-settings-xml-action) [![GitHub stars](https://img.shields.io/github/stars/whelk-io/maven-settings-xml-action?style=flat)](https://github.com/whelk-io/maven-settings-xml-action/stargazers)
- [Run Pascal Script](https://github.com/fabasoad/pascal-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/pascal-action?style=flat)](https://github.com/fabasoad/pascal-action/stargazers)
- [Setup Brainfuck](https://github.com/fabasoad/setup-brainfuck-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/setup-brainfuck-action?style=flat)](https://github.com/fabasoad/setup-brainfuck-action/stargazers) - Setup brainfuck interpreter.
- [Publish Go Binaries to GitHub Release Assets](https://github.com/wangyoucao577/go-release-action) [![GitHub stars](https://img.shields.io/github/stars/wangyoucao577/go-release-action?style=flat)](https://github.com/wangyoucao577/go-release-action/stargazers)
- [Setup COBOL](https://github.com/fabasoad/setup-cobol-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/setup-cobol-action?style=flat)](https://github.com/fabasoad/setup-cobol-action/stargazers)
- [Check Gradle version](https://github.com/madhead/check-gradle-version) [![GitHub stars](https://img.shields.io/github/stars/madhead/check-gradle-version?style=flat)](https://github.com/madhead/check-gradle-version/stargazers) - Keep your Gradle version up to date.

### Database

- [Setup Cassandra Schema](https://github.com/fabasoad/setup-cassandra-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/setup-cassandra-action?style=flat)](https://github.com/fabasoad/setup-cassandra-action/stargazers) - Running scripts from the provided folder on top of Cassandra cluster.

### Networking

- [Setup ZeroTier](https://github.com/zerotier/github-action) [![GitHub stars](https://img.shields.io/github/stars/zerotier/github-action?style=flat)](https://github.com/zerotier/github-action/stargazers) - Connect your runner to a ZeroTier network.

### Localization

- [Find and automatically fix typos and grammar issues in your code](https://github.com/sobolevn/misspell-fixer-action) [![GitHub stars](https://img.shields.io/github/stars/sobolevn/misspell-fixer-action?style=flat)](https://github.com/sobolevn/misspell-fixer-action/stargazers)
- [Translation](https://github.com/fabasoad/translation-action) [![GitHub stars](https://img.shields.io/github/stars/fabasoad/translation-action?style=flat)](https://github.com/fabasoad/translation-action/stargazers) - Translate text from any language to any language.

### Fun

- [Add equivalent of a like button in your README](https://github.com/ariary/Readme-Like-Button) [![GitHub stars](https://img.shields.io/github/stars/ariary/Readme-Like-Button?style=flat)](https://github.com/ariary/Readme-Like-Button/stargazers) - Visualize community approval on some part of your readme (can be used as a poll).

### Cheat Sheet

- [GitHub Actions Branding Cheat Sheet](https://haya14busa.github.io/github-action-brandings/)

## Tutorials

- [Continuous deployment of Next.js app with Up](https://medium.com/@romanenko/simple-ci-for-next-js-projects-with-apex-up-github-actions-6f0b1b9a5400)
- [Converting Docker-based Actions to JavaScript/TypeScript](https://httgp.com/converting-github-actions-from-docker-to-javascript/)
- [GitHub Actions CI for Swift/iOS Projects](https://medium.com/rosberryapps/github-actions-ci-for-swift-projects-c129baceed1a)
- [Working with GitHub Actions](https://jeffrafter.com/working-with-github-actions)
- [GitHub Actions for Rails Developers](https://www.youtube.com/watch?v=gGUXydw22zw)
- [GitHub Actions Advent Calendar](https://www.edwardthomson.com/blog/github_actions_advent_calendar.html)
- [Zero Downtime Laravel Deployments with GitHub Actions](https://atymic.dev/blog/github-actions-laravel-ci-cd/)
- [Building Custom GitHub Actions Pluralsight Course](https://www.pluralsight.com/courses/building-custom-github-actions/)
- [Continuously Deploying Django to DigitalOcean with Docker and GitHub Actions](https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-github-actions/)
- [Deploying Self-Hosted GitHub Actions Runners with Docker](https://testdriven.io/blog/github-actions-docker/) - Deploy self-hosted GitHub Actions runners with Docker and Docker Swarm to DigitalOcean.
- [Setup Auto-scaled self-hosted GitHub Actions Runners on AWS Spot-instances](https://040code.github.io/2020/05/25/scaling-selfhosted-action-runners)
- [Getting the Gist of GitHub Actions](https://gist.github.com/br3ndonland/f9c753eb27381f97336aa21b8d932be6)

> Please don't hesitate to make a PR if you have more resources to share. Check out [contributing.md](contributing.md) for more information.
