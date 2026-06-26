# OpenTofu

[![GitHub stars](https://img.shields.io/github/stars/virtualroot/awesome-opentofu?style=flat)](https://github.com/virtualroot/awesome-opentofu/stargazers)

# Awesome OpenTofu [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <!-- omit in toc -->

> A curated and collaborative list of awesome OpenTofu resources and tools.

[OpenTofu](https://opentofu.org/) allows you to declaratively manage your infrastructure. It's an open-source, community-driven alternative to Terraform.

## Contents <!-- omit in toc -->

- [Official](#official)
- [Community](#community)
- [Features](#features)
- [Tools](#tools)
  - [Environment managers](#environment-managers)
  - [Wrappers](#wrappers)
  - [CI](#ci)
  - [Tests](#tests)
  - [State](#state)
  - [Providers](#providers)
  - [Platforms](#platforms)
  - [Registry](#registry)
  - [Helpers](#helpers)
- [Learning](#learning)
- [Media](#media)
- [Podcasts](#podcasts)

## Official

- [OpenTofu repository](https://github.com/opentofu/opentofu) [![GitHub stars](https://img.shields.io/github/stars/opentofu/opentofu?style=flat)](https://github.com/opentofu/opentofu/stargazers) 🎉
- [Fork announcement](https://opentofu.org/announcement)
- [Registry](https://github.com/opentofu/registry) [![GitHub stars](https://img.shields.io/github/stars/opentofu/registry?style=flat)](https://github.com/opentofu/registry/stargazers)
- [Registry MCP Server](https://github.com/opentofu/opentofu-mcp-server#opentofu-mcp-server)
- [Weekly updates](https://github.com/opentofu/opentofu/discussions/categories/weekly-updates) [![GitHub stars](https://img.shields.io/github/stars/opentofu/opentofu/discussions/categories/weekly-updates?style=flat)](https://github.com/opentofu/opentofu/discussions/categories/weekly-updates/stargazers)
- [Office hours](https://www.youtube.com/watch?v=aEoMzUza6Ok&list=PLnVotLM2QsyhCc1_8PA7fbVF-ixt4_XAY)
- [Technical Steering Committee updates](https://github.com/opentofu/org/tree/main/TSC) [![GitHub stars](https://img.shields.io/github/stars/opentofu/org/tree/main/TSC?style=flat)](https://github.com/opentofu/org/tree/main/TSC/stargazers)

## Community

*Communication channels, meetups, newsletters, and forums.*

- [OpenTofu GitHub Discussion](https://github.com/orgs/opentofu/discussions) [![GitHub stars](https://img.shields.io/github/stars/orgs/opentofu/discussions?style=flat)](https://github.com/orgs/opentofu/discussions/stargazers)
- [OpenTofu LinkedIn](https://www.linkedin.com/company/opentofuorg/)
- [OpenTofu Slack](https://opentofu.org/slack)
- [OpenTofu Twitter](https://twitter.com/opentofuorg)

## Features

<!--lint disable double-link-->

- [1.10 - Enhanced moved and removed blocks](https://opentofu.org/docs/v1.10/intro/whats-new/#enhanced-moved-and-removed-blocks)
- [1.10 - External key providers](https://opentofu.org/docs/v1.10/intro/whats-new/#external-key-providers)
- [1.10 - OCI registry support](https://opentofu.org/docs/cli/oci_registries/)
- [1.10 - S3 native state locking](https://opentofu.org/docs/v1.10/intro/whats-new/#native-s3-state-locking)
- [1.10 - Target and exclude files](https://opentofu.org/docs/v1.10/intro/whats-new/#target-and-exclude-files)
- [1.9 - Provider iteration with for_each](https://opentofu.org/docs/v1.9/intro/whats-new/#provider-iteration-for_each)
- [1.9 - The -exclude flag](https://opentofu.org/docs/v1.9/intro/whats-new/#the--exclude-flag)
- [1.8 - Early variable and locals evaluation](https://opentofu.org/docs/v1.8/intro/whats-new/#early-variablelocals-evaluation)
- [1.8 - Override files for OpenTofu (.tofu)](https://opentofu.org/docs/v1.8/intro/whats-new/#override-files-for-opentofu-keeping-compatibility)
- [1.7 - End-to-end encryption for state files](https://opentofu.org/docs/v1.7/intro/whats-new/#state-encryption)
- [1.7 - Loopable import blocks](https://opentofu.org/docs/v1.7/intro/whats-new/#loopable-import-blocks)
- [1.7 - Provider-defined functions](https://opentofu.org/docs/v1.7/intro/whats-new/#provider-defined-functions)
- [1.7 - Removed block](https://opentofu.org/docs/v1.7/intro/whats-new/#removed-block)
- [CanI.TF - Feature parity between Terraform and OpenTofu](https://cani.tf/)

<!--lint enable double-link-->

## Tools

### Environment managers

- [arkade](https://github.com/alexellis/arkade) [![GitHub stars](https://img.shields.io/github/stars/alexellis/arkade?style=flat)](https://github.com/alexellis/arkade/stargazers) - CLI and Kubernetes app installer.
- [asdf-opentofu](https://github.com/virtualroot/asdf-opentofu) [![GitHub stars](https://img.shields.io/github/stars/virtualroot/asdf-opentofu?style=flat)](https://github.com/virtualroot/asdf-opentofu/stargazers) - OpenTofu plugin for asdf version manager.
- [tenv](https://github.com/tofuutils/tenv) [![GitHub stars](https://img.shields.io/github/stars/tofuutils/tenv?style=flat)](https://github.com/tofuutils/tenv/stargazers) - Terraform and OpenTofu version manager written in Go.
- [tfswitcher](https://github.com/ASleepyCat/tfswitcher) [![GitHub stars](https://img.shields.io/github/stars/ASleepyCat/tfswitcher?style=flat)](https://github.com/ASleepyCat/tfswitcher/stargazers) - Terraform and OpenTofu version switcher written in Rust.
- [tofuenv](https://github.com/tofuutils/tofuenv) [![GitHub stars](https://img.shields.io/github/stars/tofuutils/tofuenv?style=flat)](https://github.com/tofuutils/tofuenv/stargazers) - OpenTofu version manager inspired by tfenv.

### Wrappers

*Simplify your OpenTofu workflows with a thin wrapper.*

- [Atmos](https://github.com/cloudposse/atmos) [![GitHub stars](https://img.shields.io/github/stars/cloudposse/atmos?style=flat)](https://github.com/cloudposse/atmos/stargazers) - Orchestration tool that keeps environment configuration DRY.
- [Terragrunt](https://github.com/gruntwork-io/terragrunt) [![GitHub stars](https://img.shields.io/github/stars/gruntwork-io/terragrunt?style=flat)](https://github.com/gruntwork-io/terragrunt/stargazers) - Keep your configurations DRY, work with multiple modules, and manage remote state.
- [Terramate](https://github.com/terramate-io/terramate) [![GitHub stars](https://img.shields.io/github/stars/terramate-io/terramate?style=flat)](https://github.com/terramate-io/terramate/stargazers) - Automation, orchestration, and code generation for OpenTofu, Terraform, Kubernetes, and others.
- [easy_infra](https://github.com/SeisoLLC/easy_infra) [![GitHub stars](https://img.shields.io/github/stars/SeisoLLC/easy_infra?style=flat)](https://github.com/SeisoLLC/easy_infra/stargazers) - Docker container to simplify and secure the use of infrastructure as code.
- [pug](https://github.com/leg100/pug) [![GitHub stars](https://img.shields.io/github/stars/leg100/pug?style=flat)](https://github.com/leg100/pug/stargazers) - A terminal user interface for power users.
- [tf](https://github.com/dex4er/tf) [![GitHub stars](https://img.shields.io/github/stars/dex4er/tf?style=flat)](https://github.com/dex4er/tf/stargazers) - Less verbose and more friendly command outputs.
- [tfam](https://github.com/Ant0wan/tfam) [![GitHub stars](https://img.shields.io/github/stars/Ant0wan/tfam?style=flat)](https://github.com/Ant0wan/tfam/stargazers) - Rust-powered wrapper for concurrent Terraform/OpenTofu apply, enabling multi-deployment support.
- [tfexe](https://github.com/Ant0wan/tfexe) [![GitHub stars](https://img.shields.io/github/stars/Ant0wan/tfexe?style=flat)](https://github.com/Ant0wan/tfexe/stargazers) - Rust-powered wrapper for seamless execution of tfswitch and Terraform/OpenTofu with version control.
- [tfwrapper](https://github.com/claranet/tfwrapper) [![GitHub stars](https://img.shields.io/github/stars/claranet/tfwrapper?style=flat)](https://github.com/claranet/tfwrapper/stargazers) - Python wrapper that simplifies OpenTofu usage and enforces best practices.

### CI

- [Atlantis](https://www.runatlantis.io/) - Automating workflows via pull requests.
- [Burrito](https://docs.burrito.tf/latest/overview/) - A TACoS (Terraform Automation and Collaboration Software) that works inside Kubernetes.
- [drifthound](https://github.com/treezio/drifthound) [![GitHub stars](https://img.shields.io/github/stars/treezio/drifthound?style=flat)](https://github.com/treezio/drifthound/stargazers) - Continuous infrastructure drift detection with historical tracking and notifications.
- [TF-via-PR](https://github.com/OP5dev/TF-via-PR) [![GitHub stars](https://img.shields.io/github/stars/OP5dev/TF-via-PR?style=flat)](https://github.com/OP5dev/TF-via-PR/stargazers) - GitHub Action to init, plan and apply Terraform/OpenTofu via PR automation.
- [pre-commit-opentofu](https://github.com/tofuutils/pre-commit-opentofu) [![GitHub stars](https://img.shields.io/github/stars/tofuutils/pre-commit-opentofu?style=flat)](https://github.com/tofuutils/pre-commit-opentofu/stargazers) - Git pre-commit hooks plugin.
- [setup-opentofu](https://github.com/opentofu/setup-opentofu) [![GitHub stars](https://img.shields.io/github/stars/opentofu/setup-opentofu?style=flat)](https://github.com/opentofu/setup-opentofu/stargazers) - Set up OpenTofu CLI in your GitHub Actions workflow.
- [terraform-github-actions](https://github.com/dflook/terraform-github-actions) [![GitHub stars](https://img.shields.io/github/stars/dflook/terraform-github-actions?style=flat)](https://github.com/dflook/terraform-github-actions/stargazers) - GitHub Actions for OpenTofu.
- [tofu-controller](https://github.com/flux-iac/tofu-controller) [![GitHub stars](https://img.shields.io/github/stars/flux-iac/tofu-controller?style=flat)](https://github.com/flux-iac/tofu-controller/stargazers) - GitOps OpenTofu and Terraform controller for Flux.
- [tofUI](https://github.com/65156/tofUI) [![GitHub stars](https://img.shields.io/github/stars/65156/tofUI?style=flat)](https://github.com/65156/tofUI/stargazers) - Easily export OpenTofu and Terraform plans in HTML for better readability.

### Tests

- [Terratest](https://github.com/gruntwork-io/terratest) [![GitHub stars](https://img.shields.io/github/stars/gruntwork-io/terratest?style=flat)](https://github.com/gruntwork-io/terratest/stargazers) - Go library that makes writing automated tests for your infrastructure code easier.

### State

*Analyze and manipulate OpenTofu's state.*

- [tfmigrate](https://github.com/minamijoyo/tfmigrate) [![GitHub stars](https://img.shields.io/github/stars/minamijoyo/tfmigrate?style=flat)](https://github.com/minamijoyo/tfmigrate/stargazers) - State migration tool.
- [tfimport](https://github.com/coolapso/tfimport) [![GitHub stars](https://img.shields.io/github/stars/coolapso/tfimport?style=flat)](https://github.com/coolapso/tfimport/stargazers) - Tool to automate state imports.

### Providers

*Inspect and interact with OpenTofu providers.*

- [tfschema](https://github.com/minamijoyo/tfschema) [![GitHub stars](https://img.shields.io/github/stars/minamijoyo/tfschema?style=flat)](https://github.com/minamijoyo/tfschema/stargazers) - Schema inspector for providers.

### Platforms

*Alternatives to Terraform Cloud.*

- [digger](https://github.com/diggerhq/digger) [![GitHub stars](https://img.shields.io/github/stars/diggerhq/digger?style=flat)](https://github.com/diggerhq/digger/stargazers) - Open-source IaC orchestration tool. Digger allows you to run IaC in your existing CI pipeline.
- [Stategraph](https://stategraph.com) - State backend that eliminates the state file bottleneck. Teams plan in parallel with resource-level locking, and state is queryable via SQL.
- [terrakube](https://github.com/AzBuilder/terrakube) [![GitHub stars](https://img.shields.io/github/stars/AzBuilder/terrakube?style=flat)](https://github.com/AzBuilder/terrakube/stargazers) - Open-source platform with a private registry, remote state, custom flows, scheduled workspaces, and visual states.
- [tofutf](https://github.com/tofutf/tofutf) [![GitHub stars](https://img.shields.io/github/stars/tofutf/tofutf?style=flat)](https://github.com/tofutf/tofutf/stargazers) - Open-source alternative to Terraform Enterprise with SSO, team management, agents, etc.
- [Terrateam](https://github.com/terrateamio/terrateam) [![GitHub stars](https://img.shields.io/github/stars/terrateamio/terrateam?style=flat)](https://github.com/terrateamio/terrateam/stargazers) - Open-source alternative to Terraform Cloud/Enterprise. GitOps-first and built for scale, security, and reliability across modern VCS providers.

### Registry

- [library.tf](https://library.tf/) - An indexer of registries for providers and modules with insights and documentation.
- [boring-registry](https://github.com/boring-registry/boring-registry) [![GitHub stars](https://img.shields.io/github/stars/boring-registry/boring-registry?style=flat)](https://github.com/boring-registry/boring-registry/stargazers) - An open-source module and provider registry compatible with OpenTofu.
- [hermitcrab](https://github.com/seal-io/hermitcrab) [![GitHub stars](https://img.shields.io/github/stars/seal-io/hermitcrab?style=flat)](https://github.com/seal-io/hermitcrab/stargazers) - Registry network mirroring service compatible with OpenTofu.
- [terrac](https://github.com/haoliangyu/terrac) [![GitHub stars](https://img.shields.io/github/stars/haoliangyu/terrac?style=flat)](https://github.com/haoliangyu/terrac/stargazers) - Minimal private module registry compatible with OpenTofu.
- [GitLab Module Registry](https://docs.gitlab.com/ee/user/packages/terraform_module_registry/) - Use GitLab projects as a private registry for Terraform modules.
- [terralist](https://github.com/terralist/terralist) [![GitHub stars](https://img.shields.io/github/stars/terralist/terralist?style=flat)](https://github.com/terralist/terralist/stargazers) - Private registry for providers and modules.
- [citizen](https://github.com/outsideris/citizen) [![GitHub stars](https://img.shields.io/github/stars/outsideris/citizen?style=flat)](https://github.com/outsideris/citizen/stargazers) - Private registry for modules and providers with support for multiple databases and storages.
- [petra](https://github.com/devoteamgcloud/petra) [![GitHub stars](https://img.shields.io/github/stars/devoteamgcloud/petra?style=flat)](https://github.com/devoteamgcloud/petra/stargazers) - Private registry manager using Google Cloud Storage.
- [tapir](https://github.com/PacoVK/tapir) [![GitHub stars](https://img.shields.io/github/stars/PacoVK/tapir?style=flat)](https://github.com/PacoVK/tapir/stargazers) - Private registry for modules and providers with a UI.
- [terraform-registry](https://github.com/nrkno/terraform-registry) [![GitHub stars](https://img.shields.io/github/stars/nrkno/terraform-registry?style=flat)](https://github.com/nrkno/terraform-registry/stargazers) - Modules registry with authentication and support for multiple backends.
- [terrareg](https://github.com/MatthewJohn/terrareg) [![GitHub stars](https://img.shields.io/github/stars/MatthewJohn/terrareg?style=flat)](https://github.com/MatthewJohn/terrareg/stargazers) - Open-source modules registry with UI, optional Git integration and deep analysis.
- [terustry](https://github.com/veepee-oss/terustry) [![GitHub stars](https://img.shields.io/github/stars/veepee-oss/terustry?style=flat)](https://github.com/veepee-oss/terustry/stargazers) - Proxy registry for providers.
- [tofuref](https://github.com/djetelina/tofuref) [![GitHub stars](https://img.shields.io/github/stars/djetelina/tofuref?style=flat)](https://github.com/djetelina/tofuref/stargazers) - TUI for OpenTofu provider registry.

### Helpers

- [OpenTofu Language Server](https://github.com/opentofu/tofu-ls) [![GitHub stars](https://img.shields.io/github/stars/opentofu/tofu-ls?style=flat)](https://github.com/opentofu/tofu-ls/stargazers) - The OpenTofu Language Server.
- [VS Code Extension](https://open-vsx.org/extension/OpenTofu/vscode-opentofu) - Extension for Visual Studio Code with the OpenTofu Language Server adds editing features for OpenTofu files such as syntax highlighting, IntelliSense, code navigation, code formatting, module explorer.
- [zed Extension](https://github.com/ashpool37/zed-extension-opentofu) [![GitHub stars](https://img.shields.io/github/stars/ashpool37/zed-extension-opentofu?style=flat)](https://github.com/ashpool37/zed-extension-opentofu/stargazers) - Extension for the Zed Editor.
- [terratag](https://github.com/env0/terratag) [![GitHub stars](https://img.shields.io/github/stars/env0/terratag?style=flat)](https://github.com/env0/terratag/stargazers) - CLI tool allowing for tags or labels to be applied across an entire set of OpenTofu/Terraform files.
- [tfupdate](https://github.com/minamijoyo/tfupdate) [![GitHub stars](https://img.shields.io/github/stars/minamijoyo/tfupdate?style=flat)](https://github.com/minamijoyo/tfupdate/stargazers) - Update version constraints in your Terraform / OpenTofu configurations.

## Learning

- [OpenTofu Course](https://killercoda.com/quincycheng/course/course_opentofu) - Interactive tutorials.
- [Terraform in Depth](https://www.manning.com/books/terraform-in-depth) - Book with OpenTofu sections.
- [Infrastructure automation with OpenTofu](https://www.udemy.com/course/infrastructure-automation-with-opentofu-hands-on-devops/?couponCode=1D97F4D8FFE62E296BE1) - Learn infrastructure provisioning with lectures, quizzes, hands-on demos and coding exercises.
- [Migrating From Terraform To OpenTofu](https://www.youtube.com/watch?v=v9rJgtHzxUk) - Introduction to OpenTofu history and how to migrate.
- [Terraform Academy OpenTofu Practitioner Path](https://www.terraformacademy.app/max/labs/opentofu-basics.html) - Interactive browser-based lab covering native state and plan encryption with PBKDF2 and AES-GCM, plus a full practitioner readiness path that reuses HCL fundamentals applicable to OpenTofu 1.6 and later.

## Media

- [OSS EU 2023 - Announcement](https://www.youtube.com/watch?v=Ha77rpusEDM&t=1190s)
- [OSS EU 2023 - Project Overview](https://www.youtube.com/watch?v=-8sOE9-icmY&t=15116s)
- [Code To Cloud - Getting Started With OpenTofu](https://www.youtube.com/watch?v=HeUz6TMg82U)
- [CNCF - OpenTofu Day Europe 2024](https://www.youtube.com/playlist?list=PLnVotLM2Qsyiw_6Pd_9WxRRLdrUAs3c1c)
- [CNCF - OpenTofu Day North America 2024](https://www.youtube.com/playlist?list=PLnVotLM2QsyhhCO5TgEUsAip601j3NUlm)
- [CNCF - OpenTofu Day Europe 2025](https://www.youtube.com/playlist?list=PLj6h78yzYM2P1WUOx9Ny6Q3JJxiAs1A3M)
- [CNCF - OpenTofu Day North America 2025](https://www.youtube.com/playlist?list=PLj6h78yzYM2MATqCH0Tux6phUq9o4-lnG)

## Podcasts

<!-- DESC, from most recent to oldest. -->
- [SE Radio: Christian Mesh on OpenTofu](https://se-radio.net/2025/01/se-radio-652-christian-mesh-on-opentofu/)
- [Kubernetes Podcast - OpenTofu, with Ohad Maislish](https://kubernetespodcast.com/episode/232-opentofu/)
- [TheIaCPodcast - Expert Panel on OpenTofu GA Release, Licensing, and OSS Future](https://www.theiacpodcast.com/episode/expert-panel-on-opentofu-ga-release-licensing-and-oss-future)
- [Contributor - Community-Driven IaC](https://www.contributor.fyi/opentofu)
- [Ned in the Cloud - IaC Live Stream](https://www.youtube.com/watch?v=p0vDydkUWB4)
- [Arrested DevOps - What's Up With Open Terraform?](https://www.arresteddevops.com/open-tofu/)
- [OpenObservability - Terraform is no longer open source. Is OpenTF the successor?](https://www.youtube.com/watch?v=5QdUs9VKq5g)
- [TheCloudGambit - The Future of OpenTF](https://www.thecloudgambit.com/2236725/13576531-the-future-of-opentf-with-ohad-maislish)
- [Oxide and Friends - Fork in the road for Terraform?](https://www.youtube.com/watch?v=QaU94LY891M)
- [Changelog -  OpenTF for an open Terraform](https://changelog.com/podcast/556)
