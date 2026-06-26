# Cosmos SDK

[![GitHub stars](https://img.shields.io/github/stars/cosmos/awesome-cosmos?style=flat)](https://github.com/cosmos/awesome-cosmos/stargazers)

<!--lint disable double-link-->
# Awesome Cosmos [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A community curated list of awesome projects related to the Cosmos ecosystem

The Cosmos SDK is a modular framework for building blockchain applications in Go.
Gaia, the implementation of the Cosmos Hub, is built with the Cosmos SDK.

**Contributing:**
Please read the [Contributing guide](./CONTRIBUTING.md). Thank you to all our [contributors](https://github.com/cosmos/awesome/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/cosmos/awesome/graphs/contributors?style=flat)](https://github.com/cosmos/awesome/graphs/contributors/stargazers).

**Disclaimer: This community-maintained repo does not reflect the views of any official entity.**

## Contents

* [Core Components](#core-components)
* [Documentation](#documentation)
* [Client Libraries](#client-libraries)
    * [Go](#go)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Rust](#rust)
* [Block Explorers](#block-explorers)
    * [Visual Block Explorers](#visual-block-explorers)
    * [Terminal Block Explorers](#terminal-block-explorers)
* [Chain Registry](#chain-registry)
* [Validators](#validators)
* [Cosmos SDK Modules](#cosmos-sdk-modules)
* [Monitoring](#monitoring)
* [Indexers](#indexers)
* [Frameworks](#frameworks)
* [Virtual Machines](#virtual-machines)
* [IBC](#ibc)
* [Testing](#testing)
* [Templates](#templates)
* [Tools](#tools)
    * [CLI](#cli)
    * [GUI](#gui)
    * [Bots](#bots)
* [Node Operations](#node-operations)
    * [Utilities](#utilities)
* [Ecosystem](#ecosystem)
* [Wallets](#wallets)
* [Blogs](#blogs)
    * [Articles](#articles)
* [Related](#related)

## Core Components

* [Cosmos Hub](https://github.com/cosmos/gaia) [![GitHub stars](https://img.shields.io/github/stars/cosmos/gaia?style=flat)](https://github.com/cosmos/gaia/stargazers)
<!-- -->
* [Cosmos SDK](https://github.com/cosmos/cosmos-sdk/) [![GitHub stars](https://img.shields.io/github/stars/cosmos/cosmos-sdk/?style=flat)](https://github.com/cosmos/cosmos-sdk//stargazers)
* [IBC Go](https://github.com/cosmos/ibc-go) [![GitHub stars](https://img.shields.io/github/stars/cosmos/ibc-go?style=flat)](https://github.com/cosmos/ibc-go/stargazers)
* [CometBFT](https://github.com/cometbft/cometbft) [![GitHub stars](https://img.shields.io/github/stars/cometbft/cometbft?style=flat)](https://github.com/cometbft/cometbft/stargazers)
* [CosmWasm](https://github.com/CosmWasm/cosmwasm) [![GitHub stars](https://img.shields.io/github/stars/CosmWasm/cosmwasm?style=flat)](https://github.com/CosmWasm/cosmwasm/stargazers)
* [CosmJS](https://github.com/cosmos/cosmjs) [![GitHub stars](https://img.shields.io/github/stars/cosmos/cosmjs?style=flat)](https://github.com/cosmos/cosmjs/stargazers)
<!-- -->
* [Protobuf](https://buf.build/cosmos)
* [IAVL](https://github.com/cosmos/iavl) [![GitHub stars](https://img.shields.io/github/stars/cosmos/iavl?style=flat)](https://github.com/cosmos/iavl/stargazers)
* [ICS23](https://github.com/cosmos/ics23) [![GitHub stars](https://img.shields.io/github/stars/cosmos/ics23?style=flat)](https://github.com/cosmos/ics23/stargazers)

## Documentation

* [Cosmos Developer Portal](https://tutorials.cosmos.network)
* [Interchain Developer Academy](https://ida.interchain.io/)
* [Cosmos SDK](https://docs.cosmos.network/)
* [IBC](https://ibc.cosmos.com/)
* [CometBFT](https://docs.cometbft.com/)
* [Cosmos Hub](https://hub.cosmos.network/)
* [CosmWasm](https://docs.cosmwasm.com/docs/1.0/)
* [Cosmology](https://cosmology.tech/learn)

## Client Libraries

### Go

* [Ignite CLI](https://github.com/ignite/cli) [![GitHub stars](https://img.shields.io/github/stars/ignite/cli?style=flat)](https://github.com/ignite/cli/stargazers) - All-in-one platform to build, launch, and maintain any crypto application on a sovereign and secured blockchain. Quickly bootstraps a new Cosmos SDK blockchain with UI and support to create new and work conveniently with existing Cosmos SDK modules.

### JavaScript

* [cosmos/cosmjs](https://github.com/cosmos/cosmjs) [![GitHub stars](https://img.shields.io/github/stars/cosmos/cosmjs?style=flat)](https://github.com/cosmos/cosmjs/stargazers) - The Cosmos JavaScript library.
* [telescope](https://github.com/osmosis-labs/telescope) [![GitHub stars](https://img.shields.io/github/stars/osmosis-labs/telescope?style=flat)](https://github.com/osmosis-labs/telescope/stargazers) - Typescript library generator built on top of CosmJS.
* [chainapsis/cosmosjs](https://github.com/chainapsis/cosmosjs) [![GitHub stars](https://img.shields.io/github/stars/chainapsis/cosmosjs?style=flat)](https://github.com/chainapsis/cosmosjs/stargazers) - Chainapsis Signing & API Library.
* [cosmos-client/cosmos-client-ts](https://github.com/cosmos-client/cosmos-client-ts) [![GitHub stars](https://img.shields.io/github/stars/cosmos-client/cosmos-client-ts?style=flat)](https://github.com/cosmos-client/cosmos-client-ts/stargazers) - JavaScript / TypeScript client for Cosmos SDK blockchains.
* [cosmology-tech/chain-registry](https://github.com/cosmology-tech/chain-registry) [![GitHub stars](https://img.shields.io/github/stars/cosmology-tech/chain-registry?style=flat)](https://github.com/cosmology-tech/chain-registry/stargazers) - A npm package for the official Cosmos Chain Registry.
* [strangelove-ventures/graz](https://github.com/strangelove-ventures/graz) [![GitHub stars](https://img.shields.io/github/stars/strangelove-ventures/graz?style=flat)](https://github.com/strangelove-ventures/graz/stargazers) - Collection of React hooks to interact with wallets, signers, signing clients, etc.
* [cosmology-tech/create-cosmos-app](https://github.com/cosmology-tech/create-cosmos-app) [![GitHub stars](https://img.shields.io/github/stars/cosmology-tech/create-cosmos-app?style=flat)](https://github.com/cosmology-tech/create-cosmos-app/stargazers) - A npm package to bootstrap a Cosmos Web UI.
* [cosmology-tech/cosmos-kit](https://github.com/cosmology-tech/cosmos-kit) [![GitHub stars](https://img.shields.io/github/stars/cosmology-tech/cosmos-kit?style=flat)](https://github.com/cosmology-tech/cosmos-kit/stargazers) - A wallet connector for the Cosmos.
* [nabla-studio/quirks](https://github.com/nabla-studio/quirks) [![GitHub stars](https://img.shields.io/github/stars/nabla-studio/quirks?style=flat)](https://github.com/nabla-studio/quirks/stargazers) - A universal wallet adapter for your Cosmos dApps, that works on both mobile and browser.
* [toschdev/bip44](https://github.com/toschdev/cosmos-bip44) [![GitHub stars](https://img.shields.io/github/stars/toschdev/cosmos-bip44?style=flat)](https://github.com/toschdev/cosmos-bip44/stargazers) - Cosmos BIP44 implementation in JavaScript for development and education learning.

### Python

* [cosmpy](https://github.com/fetchai/cosmpy) [![GitHub stars](https://img.shields.io/github/stars/fetchai/cosmpy?style=flat)](https://github.com/fetchai/cosmpy/stargazers) - A Python client library for interacting with blockchains based on the Cosmos SDK.
* [pyCosmicWrap](https://github.com/ChihuahuaChain/pyCosmicWrap/) [![GitHub stars](https://img.shields.io/github/stars/ChihuahuaChain/pyCosmicWrap/?style=flat)](https://github.com/ChihuahuaChain/pyCosmicWrap//stargazers) - A python3 wrapper around Cosmos API/RPC.
* [mospy](https://github.com/ctrl-Felix/mospy) [![GitHub stars](https://img.shields.io/github/stars/ctrl-Felix/mospy?style=flat)](https://github.com/ctrl-Felix/mospy/stargazers) - A Python library to create and sign transactions for Cosmos SDK based coins.
* [cosmospy-protobuf](https://github.com/ctrl-Felix/cosmospy-protobuf) [![GitHub stars](https://img.shields.io/github/stars/ctrl-Felix/cosmospy-protobuf?style=flat)](https://github.com/ctrl-Felix/cosmospy-protobuf/stargazers) - A Python library containing all compiled protobuf files (works very good for grpc).
* [fx-py-sdk](https://github.com/functionx/fx-py-sdk) [![GitHub stars](https://img.shields.io/github/stars/functionx/fx-py-sdk?style=flat)](https://github.com/functionx/fx-py-sdk/stargazers) - The Cosmos Python client library.

### Rust

* [CosmWasm/cosmwasm](https://github.com/CosmWasm/cosmwasm) [![GitHub stars](https://img.shields.io/github/stars/CosmWasm/cosmwasm?style=flat)](https://github.com/CosmWasm/cosmwasm/stargazers) - WebAssembly Smart Contracts for the Cosmos SDK.
* [iqlusioninc/stdtx](https://github.com/iqlusioninc/crates) [![GitHub stars](https://img.shields.io/github/stars/iqlusioninc/crates?style=flat)](https://github.com/iqlusioninc/crates/stargazers) - A collection of open source Rust crates from iqlusion.
* [peggyjv/ocular](https://github.com/peggyjv/ocular) [![GitHub stars](https://img.shields.io/github/stars/peggyjv/ocular?style=flat)](https://github.com/peggyjv/ocular/stargazers) - A client library for Cosmos SDK chains focusing on pleasant UX.

## Block Explorers

* [ATOMScan](https://atomscan.com)
* [Big Dipper](https://bigdipper.live) - [Source](https://github.com/forbole/big-dipper-2.0-cosmos) [![GitHub stars](https://img.shields.io/github/stars/forbole/big-dipper-2.0-cosmos?style=flat)](https://github.com/forbole/big-dipper-2.0-cosmos/stargazers)
* [IOBScan](https://ibc.iobscan.io/)
* [Mintscan](https://www.mintscan.io)
    * [Mintscan for Cosmos Hub Testnet](https://cosmoshub-testnet.mintscan.io/cosmoshub-testnet)
* [NG Explorers](https://explorers.guru/)
* [Ping.pub](https://ping.pub) - [Source](https://github.com/ping-pub/explorer) [![GitHub stars](https://img.shields.io/github/stars/ping-pub/explorer?style=flat)](https://github.com/ping-pub/explorer/stargazers)
* [Stake ID](https://stake.id)

### Visual Block Explorers

View Inter-Blockchain Communication (IBC) transfer activity. The map traces IBC transactions between different blockchains (called zones in the Cosmos Hub) to display accurate aggregate information about the pulse of the entire Cosmos ecosystem.

* [Map of Zones](https://mapofzones.com/?period=24) - [Source](https://github.com/mapofzones) [![GitHub stars](https://img.shields.io/github/stars/mapofzones?style=flat)](https://github.com/mapofzones/stargazers)
* [Mintscan](https://hub.mintscan.io) - Interchain Explorer by Cosmostation.

### Terminal Block Explorers

Explore Cosmos SDK blockchains via a terminal.

* [gex](https://github.com/cosmos/gex) [![GitHub stars](https://img.shields.io/github/stars/cosmos/gex?style=flat)](https://github.com/cosmos/gex/stargazers) - GEX In-Terminal Explorer.
* [cshtop](https://github.com/gsk967/cshtop) [![GitHub stars](https://img.shields.io/github/stars/gsk967/cshtop?style=flat)](https://github.com/gsk967/cshtop/stargazers) - Cosmos htop , Blocks visualizer on terminal.
* [pvtop](https://github.com/blockpane/pvtop) [![GitHub stars](https://img.shields.io/github/stars/blockpane/pvtop?style=flat)](https://github.com/blockpane/pvtop/stargazers) - Consensus visualizer on terminal.
* [tmtop](https://github.com/quokkastake/tmtop) [![GitHub stars](https://img.shields.io/github/stars/quokkastake/tmtop?style=flat)](https://github.com/quokkastake/tmtop/stargazers) - Htop-like visualiser of consensus inspired by pvtop that allows showing upgrade info, working with consumer chains and non-Cosmos chains and way more.

## Chain Registry

A registry containing standardized metadata from most Cosmos chains.

* [cosmos/chain-registry](https://github.com/cosmos/chain-registry/) [![GitHub stars](https://img.shields.io/github/stars/cosmos/chain-registry/?style=flat)](https://github.com/cosmos/chain-registry//stargazers)
* [Cosmos directory](https://cosmos.directory) - [Source](https://github.com/eco-stake/cosmos-directory) [![GitHub stars](https://img.shields.io/github/stars/eco-stake/cosmos-directory?style=flat)](https://github.com/eco-stake/cosmos-directory/stargazers)
* [cosmology-tech/chain-registry](https://github.com/cosmology-tech/chain-registry) [![GitHub stars](https://img.shields.io/github/stars/cosmology-tech/chain-registry?style=flat)](https://github.com/cosmology-tech/chain-registry/stargazers) - A npm package for the official Cosmos Chain Registry.

## Validators

Popular block explorers provide a list of active validators. The easiest entry point to view validator profiles is from a block explorer:

* [List on Mintscan](https://www.mintscan.io/cosmos/validators)
* [List on ATOMScan](https://atomscan.com/validators)
* [List on BigDipper](https://cosmos.bigdipper.live/validators)
* [List on Kujira POD](https://pod.kujira.app/cosmoshub-4)

DYOR when choosing a validator. Consider delegating your tokens to validators outside of the top 20 to increase the decentralization of the network.
This is also a good practice to avoid 0% commission validators and exchange validators.

## Cosmos SDK Modules

The best place to find an accurate list of the Cosmos SDK modules is the project repository:

* For a list of production-grade modules, see the [List of Modules](https://docs.cosmos.network/main/modules/).
* For a list of well-known third-party modules, see [Cosmod.xyz](https://cosmod.xyz)

## Monitoring
* [PANIC Monitoring and Alerting For Blockchains](https://github.com/SimplyVC/panic) [![GitHub stars](https://img.shields.io/github/stars/SimplyVC/panic?style=flat)](https://github.com/SimplyVC/panic/stargazers) - An open source monitoring and alerting solution for Cosmos SDK, Substrate, and Chainlink-based nodes.
* [Prometheus Exporter](https://github.com/node-a-team/Cosmos-IE) [![GitHub stars](https://img.shields.io/github/stars/node-a-team/Cosmos-IE?style=flat)](https://github.com/node-a-team/Cosmos-IE/stargazers) - An integrated Prometheus exporter for the Cosmos SDK.
* [Cosmos Chains Dashboard](https://github.com/zhangyelong/cosmos-dashboard) [![GitHub stars](https://img.shields.io/github/stars/zhangyelong/cosmos-dashboard?style=flat)](https://github.com/zhangyelong/cosmos-dashboard/stargazers) - A Grafana dashboard to monitor Cosmos SDK and Tendermint-based blockchain nodes.
* [Chain Pulse](https://github.com/informalsystems/chainpulse) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/chainpulse?style=flat)](https://github.com/informalsystems/chainpulse/stargazers) - Relayed IBC packets monitor with Prometheus exporter.
* [missed-blocks-checker](https://github.com/QuokkaStake/missed-blocks-checker) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/missed-blocks-checker?style=flat)](https://github.com/QuokkaStake/missed-blocks-checker/stargazers) - Monitor validators' missed blocks on multiple Cosmos chains and send its notifications to Telegram.
* [Nodes Checker](https://t.me/NodesGuru_bot) - Check your nodes status online, receive instant notification if something is wrong with your validator node.
* [Cosmon](https://github.com/iqlusioninc/cosmon) [![GitHub stars](https://img.shields.io/github/stars/iqlusioninc/cosmon?style=flat)](https://github.com/iqlusioninc/cosmon/stargazers) - Observability tool for Cosmos and other Tendermint applications.
* [Tenderduty](https://github.com/blockpane/tenderduty) [![GitHub stars](https://img.shields.io/github/stars/blockpane/tenderduty?style=flat)](https://github.com/blockpane/tenderduty/stargazers) - Comprehensive monitoring tool for Tendermint chains. Its primary function is to alert a validator if they are missing blocks, and more.
* [UpgradesWatchdog](https://github.com/ChihuahuaChain/UpgradesWatchdog) [![GitHub stars](https://img.shields.io/github/stars/ChihuahuaChain/UpgradesWatchdog?style=flat)](https://github.com/ChihuahuaChain/UpgradesWatchdog/stargazers) - SoftwareUpgradeProposal & GitHub Releases telegram monitoring tool.
* [cosmos-node-exporter](https://github.com/QuokkaStake/cosmos-node-exporter.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-node-exporter.git?style=flat)](https://github.com/QuokkaStake/cosmos-node-exporter.git/stargazers) - A Prometheus exporter to scrape data on your node sync status, Cosmovisor upgrades and GitHub version mismatches, useful for node operators and validators.
* [cosmos-wallets-exporter](https://github.com/QuokkaStake/cosmos-wallets-exporter.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-wallets-exporter.git?style=flat)](https://github.com/QuokkaStake/cosmos-wallets-exporter.git/stargazers) - A Prometheus exporter to scrape data on wallets balance, useful to get notified if your wallet balance is too low.
* [cosmos-validators-exporter](https://github.com/QuokkaStake/cosmos-validators-exporter.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-validators-exporter.git?style=flat)](https://github.com/QuokkaStake/cosmos-validators-exporter.git/stargazers) - A Prometheus exporter to scrape data about a validator (missed blocks, delegators count, total staked amount, rankings, etc.)
* [cosmos-validator-monitoring-service(CVMS)](https://github.com/cosmostation/cvms) [![GitHub stars](https://img.shields.io/github/stars/cosmostation/cvms?style=flat)](https://github.com/cosmostation/cvms/stargazers) - Integrated monitoring system for validators in the Cosmos app chain ecosystem.
* [cosmos-proposals-checker](https://github.com/QuokkaStake/cosmos-proposals-checker.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-proposals-checker.git?style=flat)](https://github.com/QuokkaStake/cosmos-proposals-checker.git/stargazers) - A bot that sends you a notification on multiple Cosmos chains if your wallet hasn't voted on any proposal.
* [cosmos-transactions-bot](https://github.com/QuokkaStake/cosmos-transactions-bot.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-transactions-bot.git?style=flat)](https://github.com/QuokkaStake/cosmos-transactions-bot.git/stargazers) - A bot that sends you notifications on any transactions you want to be subscribed to on multiple Cosmos chains.

## Indexers

* [Cosmscan](https://github.com/cosmscan/cosmscan-go) [![GitHub stars](https://img.shields.io/github/stars/cosmscan/cosmscan-go?style=flat)](https://github.com/cosmscan/cosmscan-go/stargazers) - An indexer engine for Cosmos chains.
* [interchain-indexer](https://github.com/Reecepbcups/interchain-indexer) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/interchain-indexer?style=flat)](https://github.com/Reecepbcups/interchain-indexer/stargazers) - A cosmos blockchain indexer in Python.
* [Cosmos Indexer](https://github.com/DefiantLabs/cosmos-indexer) [![GitHub stars](https://img.shields.io/github/stars/DefiantLabs/cosmos-indexer?style=flat)](https://github.com/DefiantLabs/cosmos-indexer/stargazers) - A generalized DB schema indexer with correlation and direct database indexing in Go.
* [BDJuno](https://github.com/forbole/bdjuno) [![GitHub stars](https://img.shields.io/github/stars/forbole/bdjuno?style=flat)](https://github.com/forbole/bdjuno/stargazers) - All the chains' data that are queried from the RPC and gRPC endpoints are stored inside a PostgreSQL database on top of which GraphQL APIs can then be created using Hasura.

## Frameworks

* [Cosmos SDK](https://github.com/cosmos/cosmos-sdk/) [![GitHub stars](https://img.shields.io/github/stars/cosmos/cosmos-sdk/?style=flat)](https://github.com/cosmos/cosmos-sdk//stargazers) - A Framework for Building High Value Public Blockchains in Go.
* [Orga](https://github.com/nomic-io/orga) [![GitHub stars](https://img.shields.io/github/stars/nomic-io/orga?style=flat)](https://github.com/nomic-io/orga/stargazers) - ABCI framework for state machine transitions in Rust.
* [CosmosSwift](https://github.com/CosmosSwift) [![GitHub stars](https://img.shields.io/github/stars/CosmosSwift?style=flat)](https://github.com/CosmosSwift/stargazers) - Build blockchain applications in Swift on top of the Tendermint consensus.
* [ABCI-RS](https://github.com/devashishdxt/abci-rs) [![GitHub stars](https://img.shields.io/github/stars/devashishdxt/abci-rs?style=flat)](https://github.com/devashishdxt/abci-rs/stargazers) - Rust crate for creating ABCI applications.
* [CosmRS](https://github.com/cosmos/cosmos-rust/tree/main/cosmrs) [![GitHub stars](https://img.shields.io/github/stars/cosmos/cosmos-rust/tree/main/cosmrs?style=flat)](https://github.com/cosmos/cosmos-rust/tree/main/cosmrs/stargazers) - Framework for building Cosmos blockchain applications in Rust.

## Virtual Machines

Modules or frameworks for virtual machines that run in the Cosmos SDK

* [Agoric SDK](https://github.com/Agoric/agoric-sdk) [![GitHub stars](https://img.shields.io/github/stars/Agoric/agoric-sdk?style=flat)](https://github.com/Agoric/agoric-sdk/stargazers) - Agoric JavaScript Smart Contract Platform.
* [CosmWasm](https://github.com/CosmWasm/cosmwasm) [![GitHub stars](https://img.shields.io/github/stars/CosmWasm/cosmwasm?style=flat)](https://github.com/CosmWasm/cosmwasm/stargazers) - WASM Virtual Machine & Rust Smart Contracts.
* [Ethermint](https://github.com/evmos/ethermint) [![GitHub stars](https://img.shields.io/github/stars/evmos/ethermint?style=flat)](https://github.com/evmos/ethermint/stargazers) - Ethereum Virtual Machine.
* [Polaris](https://github.com/berachain/polaris) [![GitHub stars](https://img.shields.io/github/stars/berachain/polaris?style=flat)](https://github.com/berachain/polaris/stargazers) - Modular Ethereum Virtual Machine.

## IBC

* [IBCprotocol.dev](https://ibcprotocol.dev/) - IBC Protocol website.
* [Interchain Standards](https://github.com/cosmos/ibc/) [![GitHub stars](https://img.shields.io/github/stars/cosmos/ibc/?style=flat)](https://github.com/cosmos/ibc//stargazers) - Interchain Standards (ICS) for the Cosmos network & interchain ecosystem.
* [cosmos/ibc-go](https://github.com/cosmos/ibc-go) [![GitHub stars](https://img.shields.io/github/stars/cosmos/ibc-go?style=flat)](https://github.com/cosmos/ibc-go/stargazers) - Inter-Blockchain Communication protocol (IBC) implementation in Go.
* [cosmos/ibc-rs](https://github.com/cosmos/ibc-rs) [![GitHub stars](https://img.shields.io/github/stars/cosmos/ibc-rs?style=flat)](https://github.com/cosmos/ibc-rs/stargazers) - Rust implementation of the Inter-Blockchain Communication (IBC) protocol.
* [interchaintest](https://github.com/strangelove-ventures/interchaintest) [![GitHub stars](https://img.shields.io/github/stars/strangelove-ventures/interchaintest?style=flat)](https://github.com/strangelove-ventures/interchaintest/stargazers) - E2E testing framework for IBC Chains.
* [cosmos/relayer](https://github.com/cosmos/relayer) [![GitHub stars](https://img.shields.io/github/stars/cosmos/relayer?style=flat)](https://github.com/cosmos/relayer/stargazers) - IBC Relayer in Go.
* [informalsystems/hermes](https://github.com/informalsystems/hermes) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/hermes?style=flat)](https://github.com/informalsystems/hermes/stargazers) - IBC Relayer in Rust.
* [confio/ts-relayer](https://github.com/confio/ts-relayer) [![GitHub stars](https://img.shields.io/github/stars/confio/ts-relayer?style=flat)](https://github.com/confio/ts-relayer/stargazers) - IBC Relayer in TypeScript.
* [local-interchain](https://github.com/Reecepbcups/local-interchain) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/local-interchain?style=flat)](https://github.com/Reecepbcups/local-interchain/stargazers) - Quickly spin up a local IBC development environment on any operating system.
* [IBC-escrow-auditor](https://github.com/Cordtus/ibc-escrow) [![GitHub stars](https://img.shields.io/github/stars/Cordtus/ibc-escrow?style=flat)](https://github.com/Cordtus/ibc-escrow/stargazers) - Standalone tool to check and report on-chain token amounts against the IBC lockup account on counterparty chain.

## Testing

* [interchaintest](https://github.com/strangelove-ventures/interchaintest) [![GitHub stars](https://img.shields.io/github/stars/strangelove-ventures/interchaintest?style=flat)](https://github.com/strangelove-ventures/interchaintest/stargazers) - E2E testing framework for IBC Chains.
* [atomkraft](https://github.com/informalsystems/atomkraft-cosmos) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/atomkraft-cosmos?style=flat)](https://github.com/informalsystems/atomkraft-cosmos/stargazers) - E2E testing framework of Cosmos SDK blockchains.
* [python-iavl](https://github.com/crypto-com/python-iavl) [![GitHub stars](https://img.shields.io/github/stars/crypto-com/python-iavl?style=flat)](https://github.com/crypto-com/python-iavl/stargazers) - IAVL inspection tool implemented in Python.
* [cosmos-sdk-codeql](https://github.com/crypto-com/cosmos-sdk-codeql) [![GitHub stars](https://img.shields.io/github/stars/crypto-com/cosmos-sdk-codeql?style=flat)](https://github.com/crypto-com/cosmos-sdk-codeql/stargazers) - CodeQL queries for common Cosmos SDK bugs.
* [tm-load-test](https://github.com/informalsystems/tm-load-test) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/tm-load-test?style=flat)](https://github.com/informalsystems/tm-load-test/stargazers) - CometBFT load test application.
* [cosmosloadtester](https://github.com/orijtech/cosmosloadtester) [![GitHub stars](https://img.shields.io/github/stars/orijtech/cosmosloadtester?style=flat)](https://github.com/orijtech/cosmosloadtester/stargazers) - Load tester for Cosmos SDK blockchains.
* [CometMock](https://github.com/informalsystems/CometMock) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/CometMock?style=flat)](https://github.com/informalsystems/CometMock/stargazers) - Drop-in replacement for CometBFT in end-to-end tests.
* [quint](https://github.com/informalsystems/quint) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/quint?style=flat)](https://github.com/informalsystems/quint/stargazers) - Executable specification language with delightful tooling.
* [apalache](https://github.com/informalsystems/apalache) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/apalache?style=flat)](https://github.com/informalsystems/apalache/stargazers) - APALACHE: symbolic model checker for TLA+ and Quint.

## Templates

Templates to help you get started with building a Cosmos SDK blockchain.

* [ignite](https://github.com/cli) [![GitHub stars](https://img.shields.io/github/stars/cli?style=flat)](https://github.com/cli/stargazers) - Quickly bootstrap a new Cosmos SDK blockchain with UI and support to create new and work conveniently with existing Cosmos SDK modules.
* [cosmosregistry/example](https://github.com/cosmosregistry/example) [![GitHub stars](https://img.shields.io/github/stars/cosmosregistry/example?style=flat)](https://github.com/cosmosregistry/example/stargazers) - Template and example repository of a Cosmos SDK module.
* [cosmosregistry/chain-minimal](https://github.com/cosmosregistry/chain-minimal) [![GitHub stars](https://img.shields.io/github/stars/cosmosregistry/chain-minimal?style=flat)](https://github.com/cosmosregistry/chain-minimal/stargazers) -  Template and example of a minimal Cosmos SDK blockchain.
* [spawn](https://github.com/rollchains/spawn) [![GitHub stars](https://img.shields.io/github/stars/rollchains/spawn?style=flat)](https://github.com/rollchains/spawn/stargazers) -  Generate a new Cosmos SDK blockchain with testing, GitHub integrations, and easy instant testnets.

## Tools

### CLI

* [tmkms](https://github.com/iqlusioninc/tmkms) [![GitHub stars](https://img.shields.io/github/stars/iqlusioninc/tmkms?style=flat)](https://github.com/iqlusioninc/tmkms/stargazers) - Key Management System for Tendermint validators.
* [cosmosvisor](https://github.com/cosmos/cosmos-sdk/tree/main/cosmovisor#readme) - Automates Cosmos SDK application binary upgrades.
* [cosmosvanity](https://github.com/hukkinj1/cosmosvanity) [![GitHub stars](https://img.shields.io/github/stars/hukkinj1/cosmosvanity?style=flat)](https://github.com/hukkinj1/cosmosvanity/stargazers) - CLI tool for generating Cosmos vanity addresses.
* [findaccount](https://github.com/blockpane/findaccount) [![GitHub stars](https://img.shields.io/github/stars/blockpane/findaccount?style=flat)](https://github.com/blockpane/findaccount/stargazers) - Helps identify if an account exists on multiple Cosmos chains with the same address.
* [lens](https://github.com/strangelove-ventures/lens) [![GitHub stars](https://img.shields.io/github/stars/strangelove-ventures/lens?style=flat)](https://github.com/strangelove-ventures/lens/stargazers) - CLI tool to interact with any Cosmos chain supporting the core Cosmos-SDK modules.
* [cosmology](https://github.com/cosmology-tech/cosmology) [![GitHub stars](https://img.shields.io/github/stars/cosmology-tech/cosmology?style=flat)](https://github.com/cosmology-tech/cosmology/stargazers) - CLI tool for making cryptocurrency trades, joining liquidity pools, and stake rewards on Osmosis.
* [multisig](https://github.com/informalsystems/multisig) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/multisig?style=flat)](https://github.com/informalsystems/multisig/stargazers) - CLI tool for managing multisig accounts on Cosmos SDK chains.
* [cosmos-genesis-tinkerer](https://github.com/hyphacoop/cosmos-genesis-tinkerer) [![GitHub stars](https://img.shields.io/github/stars/hyphacoop/cosmos-genesis-tinkerer?style=flat)](https://github.com/hyphacoop/cosmos-genesis-tinkerer/stargazers) - CLI tool for modifying Cosmos genesis files.
* [airdrop-tools](https://github.com/Reecepbcups/airdrop-tools) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/airdrop-tools?style=flat)](https://github.com/Reecepbcups/airdrop-tools/stargazers) - CLI scripts to help distribute a variety of tokens from multiple formats.
* [cosmos.nix](https://github.com/informalsystems/cosmos.nix) [![GitHub stars](https://img.shields.io/github/stars/informalsystems/cosmos.nix?style=flat)](https://github.com/informalsystems/cosmos.nix/stargazers) - [Nix](https://nixos.org/) support for Cosmos and CosmWasm.

### GUI

* [REStake](https://restake.app) - Auto-compounder app for Cosmos blockchains using Authz ([source](https://github.com/eco-stake/restake) [![GitHub stars](https://img.shields.io/github/stars/eco-stake/restake?style=flat)](https://github.com/eco-stake/restake/stargazers)).
* [Cosmfaucet](https://github.com/scalalang2/cosmfaucet) [![GitHub stars](https://img.shields.io/github/stars/scalalang2/cosmfaucet?style=flat)](https://github.com/scalalang2/cosmfaucet/stargazers) - Self-hosted faucet service for Cosmos based blockchain.
* [Cosmos Notifier](https://cosmos-notifier.decrypto.online) - Governance notification tool for Telegram and Discord ([source](https://github.com/shifty11/cosmos-notifier) [![GitHub stars](https://img.shields.io/github/stars/shifty11/cosmos-notifier?style=flat)](https://github.com/shifty11/cosmos-notifier/stargazers)).
* [Skip:Go](https://go.skip.build) - IBC token transfers, automated swapping and multi-hop routing ([source](https://github.com/skip-mev/skip-go-app) [![GitHub stars](https://img.shields.io/github/stars/skip-mev/skip-go-app?style=flat)](https://github.com/skip-mev/skip-go-app/stargazers)).

### Bots

* [Cosmos Discord Faucet](https://github.com/0x4139/cosmos-discord-faucet) [![GitHub stars](https://img.shields.io/github/stars/0x4139/cosmos-discord-faucet?style=flat)](https://github.com/0x4139/cosmos-discord-faucet/stargazers) - A configurable Discord faucet for Cosmos SDK blockchains.
* [Cosmos Discord Bot](https://github.com/okp4/discord-bot) [![GitHub stars](https://img.shields.io/github/stars/okp4/discord-bot?style=flat)](https://github.com/okp4/discord-bot/stargazers) - A general-purpose Discord bot for Cosmos SDK blockchains.
* [cosmos-proposals-checker](https://github.com/QuokkaStake/cosmos-proposals-checker.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-proposals-checker.git?style=flat)](https://github.com/QuokkaStake/cosmos-proposals-checker.git/stargazers) - A bot to notify you if your wallets didn't vote on proposal on multiple Cosmos SDK chains.
* [cosmos-transactions-bot](https://github.com/QuokkaStake/cosmos-transactions-bot.git) [![GitHub stars](https://img.shields.io/github/stars/QuokkaStake/cosmos-transactions-bot.git?style=flat)](https://github.com/QuokkaStake/cosmos-transactions-bot.git/stargazers) - Get notified about transactions matching the filters you want on multiple Cosmos SDK chains.
* [cosmos-balance-bot](https://github.com/Reecepbcups/cosmos-balance-bot) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/cosmos-balance-bot?style=flat)](https://github.com/Reecepbcups/cosmos-balance-bot/stargazers) - Get notified about your wallet balance on multiple Cosmos SDK chains at a set interval.
* [validator-stats-notifications](https://github.com/Reecepbcups/validator-stats-notifs) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/validator-stats-notifs?style=flat)](https://github.com/Reecepbcups/validator-stats-notifs/stargazers) - Discord announcements including ranking, delegations over time, and unique delegators.
* [Secret Stashh NFT Bot](https://github.com/Reecepbcups/stashh-bot) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/stashh-bot?style=flat)](https://github.com/Reecepbcups/stashh-bot/stargazers) - A discord bot to get notified of sales, auctions, and purchases for a Secret Network NFT collection.
* [DAODAO Treasury Bot](https://github.com/Reecepbcups/dao-treasury-bot) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/dao-treasury-bot?style=flat)](https://github.com/Reecepbcups/dao-treasury-bot/stargazers) - A discord bot that keeps up with a DAO's treasury fiat value.
* [Cosmos Price Bot](https://github.com/Reecepbcups/cosmos-price-bot) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/cosmos-price-bot?style=flat)](https://github.com/Reecepbcups/cosmos-price-bot/stargazers) - A discord bot that nicknames to the USD price of any cosmos token via a DEX.

## Node Operations

### Utilities

* [Cosmos Cache](https://github.com/Reecepbcups/cosmos-endpoint-cache) [![GitHub stars](https://img.shields.io/github/stars/Reecepbcups/cosmos-endpoint-cache?style=flat)](https://github.com/Reecepbcups/cosmos-endpoint-cache/stargazers) - Optimize Cosmos queries by caching responses for predefined sets of time (regex).
* [cosmos-operator](https://github.com/strangelove-ventures/cosmos-operator) [![GitHub stars](https://img.shields.io/github/stars/strangelove-ventures/cosmos-operator?style=flat)](https://github.com/strangelove-ventures/cosmos-operator/stargazers) - Cosmos Operator is a kubernetes operator for managing cosmos nodes.
* [Wallet-generator](https://github.com/Cordtus/wallet_generator) [![GitHub stars](https://img.shields.io/github/stars/Cordtus/wallet_generator?style=flat)](https://github.com/Cordtus/wallet_generator/stargazers) - Manually generate a keypair + wallet addresses from mnemonic, pubkey + wallet addresses from privkey, or wallet addresses from pubkey. Accepts arbitrary HDpath (incl. cointype)

## Ecosystem

The most up-to-date list of projects built using Cosmos SDK can be found on the [Cosmos Directory](https://cosmos.directory).

## Wallets

A list of wallets supporting Cosmos chains is <https://cosmos.network/ecosystem/wallets>.

## Blogs

As the ecosystem grows, so does the content. DYOR and follow the projects you find interesting.

**Disclaimer: This community-maintained repo does not reflect the views of any official entity.**

* [What is Cosmos?](https://cosmos.network/intro/)
* [Cosmos Blog](https://blog.cosmos.network/)
* [Interchain Foundation Blog](https://interchain-io.medium.com)

### Articles

* [Cosmos Dev Series: Cosmos Blockchain Upgrade](https://zerofruit.medium.com/cosmos-dev-series-cosmos-sdk-based-blockchain-upgrade-b5e99181554c)
* [Hardening guides](https://cyber.orijtech.com/scsec/cosmos-hardening)
* [How to connect your frontend to Cosmos blockchain](https://dev.to/kikiding/how-to-connect-your-frontend-to-cosmos-blockchain-5fcn)
* [(Not So) Smart Cosmos, examples of common Cosmos app vulnerabilities](https://github.com/crytic/building-secure-contracts/tree/master/not-so-smart-contracts/cosmos) [![GitHub stars](https://img.shields.io/github/stars/crytic/building-secure-contracts/tree/master/not-so-smart-contracts/cosmos?style=flat)](https://github.com/crytic/building-secure-contracts/tree/master/not-so-smart-contracts/cosmos/stargazers)
* [Go coding guide](https://cyber.orijtech.com/scsec/cosmos-go-coding-guide)
* [The Cosmos Security Handbook - Part 1](https://www.faulttolerant.xyz/2024-01-16-cosmos-security-1)

## Related

* [Awesome CosmWasm](https://github.com/InterWasm/cw-awesome) [![GitHub stars](https://img.shields.io/github/stars/InterWasm/cw-awesome?style=flat)](https://github.com/InterWasm/cw-awesome/stargazers)
