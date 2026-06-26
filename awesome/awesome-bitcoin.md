# Bitcoin

[![GitHub stars](https://img.shields.io/github/stars/igorbarinov/awesome-bitcoin?style=flat)](https://github.com/igorbarinov/awesome-bitcoin/stargazers)

Awesome Bitcoin
===============
A curated list of bitcoin services and tools for software developers
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

## List of content

- [Utilities](#utilities)
- [Blockchain API and Web services](#blockchain-api-and-web-services)
- [Wallets API](#wallets-api)
- [Open Source wallets](#open-source-wallets)
- [Blockchain Explorers](#blockchain-explorers)
- [C Libraries](#c-libraries)
- [C++ Libraries](#c-libraries-1)
- [JavaScript Libraries](#javascript-libraries)
- [PHP Libraries](#php-libraries)
- [Ruby Libraries](#ruby-libraries)
- [Python Libraries](#python-libraries)
- [Java Libraries](#java-libraries)
- [Scala Libraries](#scala-libraries)
- [Swift Libraries](#swift-libraries)
- [.Net Libraries](#net-libraries)
- [Haskell Libraries](#haskell-libraries)
- [Playgrounds](#playgrounds)
- [Blockchain dump](#blockchain-dump)
- [Full nodes](#full-nodes)
- [Read](#read)
- [Course](#course)
- [Additional Resources](#additional-resources)


## Utilities
* [Nigiri](https://github.com/vulpemventures/nigiri/) [![GitHub stars](https://img.shields.io/github/stars/vulpemventures/nigiri/?style=flat)](https://github.com/vulpemventures/nigiri//stargazers) - CLI to quickly fire up a a Bitcoin regtest box along with Electrs and Esplora. Includes faucet and push commands.
* [hal](https://github.com/stevenroose/hal) [![GitHub stars](https://img.shields.io/github/stars/stevenroose/hal?style=flat)](https://github.com/stevenroose/hal/stargazers) - Bitcoin CLI swiss-army-knife (based on rust-bitcoin).
* [BitKey](https://bitkey.io) - Live USB for airgapped transactions and Bitcoin swiss army knife.
* [PaperVault](https://github.com/boazeb/papervault) [![GitHub stars](https://img.shields.io/github/stars/boazeb/papervault?style=flat)](https://github.com/boazeb/papervault/stargazers) - Offline paper-based secret storage using AES-256-GCM and Shamir's Secret Sharing. Create printable encrypted backups of seed phrases with threshold key splitting.
* [Pycoin](https://github.com/richardkiss/pycoin) [![GitHub stars](https://img.shields.io/github/stars/richardkiss/pycoin?style=flat)](https://github.com/richardkiss/pycoin/stargazers) - Python-based Bitcoin and alt-coin utility library.
* [bx](https://github.com/libbitcoin/libbitcoin-explorer) [![GitHub stars](https://img.shields.io/github/stars/libbitcoin/libbitcoin-explorer?style=flat)](https://github.com/libbitcoin/libbitcoin-explorer/stargazers) - Bitcoin Command Line Tool.
* [Deadhand Protocol](https://deadhandprotocol.com) - Dead man's switch for crypto using Shamir's Secret Sharing to protect seed phrases and ensure inheritance.
* [txwatcher](https://github.com/tsileo/txwatcher) [![GitHub stars](https://img.shields.io/github/stars/tsileo/txwatcher?style=flat)](https://github.com/tsileo/txwatcher/stargazers) - A little Python utility that lets you monitor Bitcoin addresses through Blockchain Websocket API and perform custom callbacks.
* [hellobitcoin](https://github.com/prettymuchbryce/hellobitcoin) [![GitHub stars](https://img.shields.io/github/stars/prettymuchbryce/hellobitcoin?style=flat)](https://github.com/prettymuchbryce/hellobitcoin/stargazers) - A collection of simple programs which can generate bitcoin wallets, create and sign transactions, and send transactions over the bitcoin network.
* [Mining visualization](https://yogh.io/landing/)
* [HD Wallet Scanner](https://github.com/alexk111/HD-Wallet-Scanner) [![GitHub stars](https://img.shields.io/github/stars/alexk111/HD-Wallet-Scanner?style=flat)](https://github.com/alexk111/HD-Wallet-Scanner/stargazers) - Find all used addresses in your Bitcoin HD wallets bypassing gap limits.
* [`<qr-code>`](https://github.com/bitjson/qr-code) [![GitHub stars](https://img.shields.io/github/stars/bitjson/qr-code?style=flat)](https://github.com/bitjson/qr-code/stargazers) – A no-framework, no-dependencies, customizable, animate-able, SVG-based `<qr-code>` web component.
* [Bitcoin Serverless Donations](https://github.com/tombennet/bitcoin-serverless-donations) [![GitHub stars](https://img.shields.io/github/stars/tombennet/bitcoin-serverless-donations?style=flat)](https://github.com/tombennet/bitcoin-serverless-donations/stargazers) - Self-custodial serverless donation widget with address rotation derived from an XPUB.
* [BTC Tooling](https://github.com/douvy/btc-tooling) [![GitHub stars](https://img.shields.io/github/stars/douvy/btc-tooling?style=flat)](https://github.com/douvy/btc-tooling/stargazers) - Bitcoin dashboard with real-time price data, a chart, orderbook, market summary, Twitter/X insights, and halving countdown data. [Live Demo](https://www.btctooling.com/)
* [Chartscout](https://chartscout.io) - Real-time BTC chart pattern detection and trading alerts across multiple exchanges.
* [Bitcoin Bottom Score](https://bitcoinbottom.app) - Real-time Bitcoin cycle bottom probability tracker. Aggregates 25 on-chain and macro signals (MVRV Z-Score, Puell Multiple, Hash Ribbon, ETF flows) into a daily P(bottom) score. Free, updated twice daily.
* [BTC Airgap Bridge](https://github.com/paranoid-qrypto/btc-airgap-bridge) [![GitHub stars](https://img.shields.io/github/stars/paranoid-qrypto/btc-airgap-bridge?style=flat)](https://github.com/paranoid-qrypto/btc-airgap-bridge/stargazers) - 100% client-side tool for broadcasting signed Bitcoin transactions from air-gapped wallets.
* [SuperScalar MCP](https://github.com/8144225309/superscalar-mcp) [![GitHub stars](https://img.shields.io/github/stars/8144225309/superscalar-mcp?style=flat)](https://github.com/8144225309/superscalar-mcp/stargazers) - MCP server for SuperScalar Bitcoin Lightning channel factories — onboard N users in one shared UTXO, no soft fork required.
* [Lightning Memory](https://github.com/singularityjason/lightning-memory) [![GitHub stars](https://img.shields.io/github/stars/singularityjason/lightning-memory?style=flat)](https://github.com/singularityjason/lightning-memory/stargazers) - Open-source memory layer for AI agents in the Bitcoin/Lightning economy. L402 payment gateway, vendor reputation, spending anomaly detection.
* [CryptoCalk](https://cryptocalk.com) - Bitcoin profitability and on-chain calculators: ASIC/GPU mining ROI, hash rate converter, halving countdown, Mayer Multiple, Stock-to-Flow (S2F), Rainbow chart, profit/loss, DCA simulator, tax estimator, liquidation price. Client-side, no signup, available in 6 languages.
* [dont-trust-verify](https://dont-trust-verify.com) - Bitcoin-only client-side tools and self-custody education: 22 calculators, validators and decoders (BIP-39 validator, tx-stuck checker, fee estimator, wallet installer SHA-256 verifier, self-custody score quiz), plus primary-sourced guides and hardware wallet reviews. No signup, no tracking, EN + TH.

## Blockchain API and Web services
* [3xpl.com](https://3xpl.com/) - Fastest ad-free universal block explorer.
* [Bitquery.io](https://bitquery.io/) - Bitquery provides blockchain data, offering real-time streaming APIs for 40+ chains, NFT APIs, and a money flow investigation tool.
* [block.io](https://block.io)
* [blockchair.com](https://blockchair.com/) - Universal blockchain explorer and search engine.
* [BlockCypher](https://www.blockcypher.com)
* [Esplora](https://github.com/Blockstream/esplora) [![GitHub stars](https://img.shields.io/github/stars/Blockstream/esplora?style=flat)](https://github.com/Blockstream/esplora/stargazers) - Self-hosted blockchain explorer.
* [Insight](https://insight.is)
* [Chain.com](https://chain.com)
* [Coinbase Wallet](https://wallet.coinbase.com/)
* [Chainradar API](https://github.com/yasaricli/chainradar-api) [![GitHub stars](https://img.shields.io/github/stars/yasaricli/chainradar-api?style=flat)](https://github.com/yasaricli/chainradar-api/stargazers) - Blockchain Explorer API for Chainradar.
* [One-Time Address](https://github.com/alexk111/One-Time-Address) [![GitHub stars](https://img.shields.io/github/stars/alexk111/One-Time-Address?style=flat)](https://github.com/alexk111/One-Time-Address/stargazers) A better way to share your Bitcoin address.
* [Cryptocurrency Alerting](https://cryptocurrencyalerting.com/blockchain-alerts.html) - Bitcoin wallet monitoring and blockchain alerts.
* [BTC Connect](https://developers.particle.network/reference/introduction-to-btc-connect) - Unified Bitcoin Layer-1 and Layer-2 wallet connection and account abstraction.
* [Tatum](https://tatum.io/blockchain-api) - The blockchain development platform to build Web3 application. The go-to blockchain data API for Web3 developers.
* [mempool.space](https://mempool.space/docs/api/rest) - Open source and self hostable REST, WebSocket and Electrum RPC API
* [Bitview](https://bitview.space/) - An open source Bitcoin Core data extractor and visualizer (aka FOSS Glassnode)
* [Maestro](https://www.gomaestro.org/) - A high-performance Bitcoin RPC and UTXO indexer API that powers applications with real-time blockchain data, mempool monitoring, and event notifications.

## Market Data API
* [CoinGapRadar](https://coingapradar.com) - Real-time crypto premium tracker across 9 countries. Monitor kimchi premium and regional price gaps. Free, no signup.
* [CoinMetrics.io](https://docs.coinmetrics.io/) JSON REST API (free as well as paid) with access to market data. Also CSV data file download available.
* [CoinPaprika](https://api.coinpaprika.com) Free crypto market data API. 12,000+ coins, 350+ exchanges, tickers, OHLCV, historical prices. No API key for free tier.
* [Messari.io](https://messari.io/api) JSON REST API (free as well as paid) with access to market data, news, metrics, profile, etc.
* [PreReason](https://www.prereason.com) - Pre-analyzed Bitcoin market briefings via REST API. Covers BTC price, hash rate, difficulty, mining production costs, treasury holdings (30 public companies), and macro signals that move Bitcoin (Fed balance sheet, M2, Treasury yields). Returns trend direction, confidence scores, and regime classification instead of raw numbers. Free tier available.

## Wallets API
* [BitGo](https://developers.bitgo.com)
* [Coinbase](https://developers.coinbase.com)
* [Blockchain.com](https://www.blockchain.com/api)
* [BIP32](http://bip32.org)
* [walletOS](https://www.pinestreetlabs.com/walletos/)

## Open Source Wallets
* [Blue Wallet](https://bluewallet.io/)
* [CoPay by BitPay](https://copay.io/)
* [Coinb.in](https://coinb.in)
* [Coin Wallet](https://coin.space/)
* [Electrum](https://electrum.org/)
* [Green](https://blockstream.com/green/)
* [Sparrow](https://sparrowwallet.com/)
* [Wasabi Wallet](https://wasabiwallet.io/)

## Privacy projects
* [Joinmarket](https://github.com/JoinMarket-Org/joinmarket-clientserver) [![GitHub stars](https://img.shields.io/github/stars/JoinMarket-Org/joinmarket-clientserver?style=flat)](https://github.com/JoinMarket-Org/joinmarket-clientserver/stargazers) - Decentralized CoinJoin implementation
* [Jam](https://jamapp.org/) - User friendly frontend for Joinmarket

## Blockchain Explorers
* [3xpl.com](https://3xpl.com/bitcoin) - Fastest ad-free universal block explorer.
* [Chain.so](http://chain.so)
* [Blockchain.com](https://blockchain.com)
* [Blockchair.com](https://blockchair.com/bitcoin) - Universal blockchain explorer and search engine.
* [Blockstream.info](https://blockstream.info) - Blockchain explorer with API (mainnet, testnet and Liquid).
* [Bitcoin Transaction Explorer](https://github.com/JornC/bitcoin-transaction-explorer) [![GitHub stars](https://img.shields.io/github/stars/JornC/bitcoin-transaction-explorer?style=flat)](https://github.com/JornC/bitcoin-transaction-explorer/stargazers)
* [Blockexplorer.com](https://blockexplorer.com)
* [Smartbit](https://www.smartbit.com.au)
* [mempool.space](https://mempool.space/) - Open source, self hostable blockchain, mempool and lightning network explorer

## C Libraries
* [libsecp256k1](https://github.com/bitcoin-core/secp256k1) [![GitHub stars](https://img.shields.io/github/stars/bitcoin-core/secp256k1?style=flat)](https://github.com/bitcoin-core/secp256k1/stargazers)
* [UltrafastSecp256k1](https://github.com/shrec/UltrafastSecp256k1) [![GitHub stars](https://img.shields.io/github/stars/shrec/UltrafastSecp256k1?style=flat)](https://github.com/shrec/UltrafastSecp256k1/stargazers) - High-performance `secp256k1` engine with a stable C ABI, CPU, CUDA, OpenCL, embedded, and WebAssembly targets.

## C++ Libraries
* [Libbitcoin](https://libbitcoin.org/)
* [Libbitcoin](https://libbitcoin.info/) - A set of cross platform C++ libraries for building bitcoin applications
* [libwally-core](https://github.com/ElementsProject/libwally-core) [![GitHub stars](https://img.shields.io/github/stars/ElementsProject/libwally-core?style=flat)](https://github.com/ElementsProject/libwally-core/stargazers)

## JavaScript Libraries
* [Awesome CryptoCoinJS](https://github.com/cryptocoinjs/awesome-cryptocoinjs) [![GitHub stars](https://img.shields.io/github/stars/cryptocoinjs/awesome-cryptocoinjs?style=flat)](https://github.com/cryptocoinjs/awesome-cryptocoinjs/stargazers)
* [Bitcore Library](https://github.com/bitpay/bitcore/tree/v8.0.0/packages/bitcore-lib) [![GitHub stars](https://img.shields.io/github/stars/bitpay/bitcore/tree/v8.0.0/packages/bitcore-lib?style=flat)](https://github.com/bitpay/bitcore/tree/v8.0.0/packages/bitcore-lib/stargazers)
* [Bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib) [![GitHub stars](https://img.shields.io/github/stars/bitcoinjs/bitcoinjs-lib?style=flat)](https://github.com/bitcoinjs/bitcoinjs-lib/stargazers)
* [Cryptocoin](http://cryptocoinjs.com/#modules)
* [BlockTrail SDK NodeJS](https://github.com/blocktrail/blocktrail-sdk-nodejs) [![GitHub stars](https://img.shields.io/github/stars/blocktrail/blocktrail-sdk-nodejs?style=flat)](https://github.com/blocktrail/blocktrail-sdk-nodejs/stargazers)
* [bcoin](https://github.com/bcoin-org/bcoin) [![GitHub stars](https://img.shields.io/github/stars/bcoin-org/bcoin?style=flat)](https://github.com/bcoin-org/bcoin/stargazers) - Javascript bitcoin library for node.js and browsers.
* [Libauth](https://libauth.org/) – A lightweight, zero-dependency, JavaScript/TypeScript bitcoin library.
* [noble-curves](https://github.com/paulmillr/noble-curves) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/noble-curves?style=flat)](https://github.com/paulmillr/noble-curves/stargazers) — audited implementation of secp256k1 + schnorr in pure typescript
* [noble-secp256k1](https://github.com/paulmillr/noble-secp256k1) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/noble-secp256k1?style=flat)](https://github.com/paulmillr/noble-secp256k1/stargazers) — alternative implementation of secp256k1: size is only 4KB gzipped; lots of comments, very valuable for learning how algorithms work
* [scure-btc-signer](https://github.com/paulmillr/scure-btc-signer) [![GitHub stars](https://img.shields.io/github/stars/paulmillr/scure-btc-signer?style=flat)](https://github.com/paulmillr/scure-btc-signer/stargazers) — audited & minimal library for creating, signing & decoding Bitcoin transactions. With Schnorr, Taproot, UTXO & PSBT.
* [bitcoin-sdk-js](https://github.com/ChrisCho-H/bitcoin-sdk-js) [![GitHub stars](https://img.shields.io/github/stars/ChrisCho-H/bitcoin-sdk-js?style=flat)](https://github.com/ChrisCho-H/bitcoin-sdk-js/stargazers) — Bitcoin TypeScript/JavaScript Library for NodeJS, Browser and Mobile. Segwit & Taproot support.
* [toll-booth](https://github.com/forgesworn/toll-booth) [![GitHub stars](https://img.shields.io/github/stars/forgesworn/toll-booth?style=flat)](https://github.com/forgesworn/toll-booth/stargazers) - HTTP 402 payment middleware for Node.js; gates any API behind Lightning, Cashu, or stablecoin payments with five backend options.
## PHP Libraries
* [PHP-OP_RETURN](https://github.com/coinspark/php-OP_RETURN) [![GitHub stars](https://img.shields.io/github/stars/coinspark/php-OP_RETURN?style=flat)](https://github.com/coinspark/php-OP_RETURN/stargazers)
* [BlockTrail PHP SDK](https://github.com/blocktrail/blocktrail-sdk-php) [![GitHub stars](https://img.shields.io/github/stars/blocktrail/blocktrail-sdk-php?style=flat)](https://github.com/blocktrail/blocktrail-sdk-php/stargazers)

## Ruby Libraries
* [Bitcoin-ruby](https://github.com/lian/bitcoin-ruby) [![GitHub stars](https://img.shields.io/github/stars/lian/bitcoin-ruby?style=flat)](https://github.com/lian/bitcoin-ruby/stargazers)
* [bitcoinrb](https://github.com/chaintope/bitcoinrb) [![GitHub stars](https://img.shields.io/github/stars/chaintope/bitcoinrb?style=flat)](https://github.com/chaintope/bitcoinrb/stargazers) - Ruby bitcoin library including script interpreter.
* [bech32rb](https://github.com/azuchi/bech32rb) [![GitHub stars](https://img.shields.io/github/stars/azuchi/bech32rb?style=flat)](https://github.com/azuchi/bech32rb/stargazers) - Bech32 and Bech32m encode/decode library.
* [bip-schnorrrb](https://github.com/chaintope/bip-schnorrrb) [![GitHub stars](https://img.shields.io/github/stars/chaintope/bip-schnorrrb?style=flat)](https://github.com/chaintope/bip-schnorrrb/stargazers) - Schnorr signature library for Bitcoin.

## Rust Libraries
* [Bitcoin Dev Kit (BDK)](https://bitcoindevkit.org/) - With BDK, you can seamlessly build cross platform mobile wallets
* [Rust Bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) [![GitHub stars](https://img.shields.io/github/stars/rust-bitcoin/rust-bitcoin?style=flat)](https://github.com/rust-bitcoin/rust-bitcoin/stargazers) - support for de/serialization, parsing and executing on data-structures and network messages.
* [Lightning Dev Kit (LDK)](https://lightningdevkit.org/) -  Complete Lightning implementation packaged as an SDK
* [Bithoven](https://github.com/ChrisCho-H/bithoven) [![GitHub stars](https://img.shields.io/github/stars/ChrisCho-H/bithoven?style=flat)](https://github.com/ChrisCho-H/bithoven/stargazers) -  A High-Level, Imperative Language for Bitcoin Smart Contracts, featuring an LR(1) parser with static analysis for compile-time safety.

## Python Libraries
* [BlockTrail SDK Python](https://github.com/blocktrail/blocktrail-sdk-python) [![GitHub stars](https://img.shields.io/github/stars/blocktrail/blocktrail-sdk-python?style=flat)](https://github.com/blocktrail/blocktrail-sdk-python/stargazers)
* [btctxstore](https://github.com/F483/btctxstore) [![GitHub stars](https://img.shields.io/github/stars/F483/btctxstore?style=flat)](https://github.com/F483/btctxstore/stargazers) - Simple library to store/retrieve information in bitcoin transactions using OP_RETURN.
* [pybitcointools](https://github.com/vbuterin/pybitcointools) [![GitHub stars](https://img.shields.io/github/stars/vbuterin/pybitcointools?style=flat)](https://github.com/vbuterin/pybitcointools/stargazers) - Python library for Bitcoin signatures and transactions from Vitalik Buterin. Project discontinued.
* [pycoin](https://github.com/richardkiss/pycoin) [![GitHub stars](https://img.shields.io/github/stars/richardkiss/pycoin?style=flat)](https://github.com/richardkiss/pycoin/stargazers) - Python library for Bitcoin keys, signatures, transactions. Includes full VM implementation and tools for manipulating keys (ku) and transactions (tx).
* [bitcoin_tools](https://github.com/sr-gi/bitcoin_tools) [![GitHub stars](https://img.shields.io/github/stars/sr-gi/bitcoin_tools?style=flat)](https://github.com/sr-gi/bitcoin_tools/stargazers) - Python library for building and analyzing transactions and scripts (both standard and custom). Comes along with a UTXO set analysis tool. Includes several examples and exhaustive documentation.
* [pybtc](https://github.com/mohanson/pybtc) [![GitHub stars](https://img.shields.io/github/stars/mohanson/pybtc?style=flat)](https://github.com/mohanson/pybtc/stargazers) - Python BTC is an experimental project that aims to provide human-friendly interfaces for common BTC operations.

## Java Libraries
> Note that you can also use [Scala libraries](#scala-libraries) in Java.
* [BitcoinJ](https://bitcoinj.github.io)
* [XChange](https://github.com/knowm/XChange) [![GitHub stars](https://img.shields.io/github/stars/knowm/XChange?style=flat)](https://github.com/knowm/XChange/stargazers) - Library that provides a simple and consistent API for interacting with 50+ Bitcoin currency exchanges.
* [Bitcoin Spring Boot Starter](https://github.com/theborakompanioni/bitcoin-spring-boot-starter) [![GitHub stars](https://img.shields.io/github/stars/theborakompanioni/bitcoin-spring-boot-starter?style=flat)](https://github.com/theborakompanioni/bitcoin-spring-boot-starter/stargazers) - Bitcoin integration for Spring Boot applications.
* [bech32](https://github.com/NostrGameEngine/bech32) [![GitHub stars](https://img.shields.io/github/stars/NostrGameEngine/bech32?style=flat)](https://github.com/NostrGameEngine/bech32/stargazers) - Bech32 and Bech32m encode/decode library.

## Scala libraries
> Note that you can also use [Java libraries](#java-libraries) in Scala.
* [Bitcoin-S](https://bitcoin-s.org) - Scala/JVM toolkit for Bitcoin applications, includes Bitcoin data structures, transaction signing, strongly typed `bitcoind`/Eclair RPC clients, and more.

## Swift libraries
* [secp256k1.swift](https://github.com/GigaBitcoin/secp256k1.swift) [![GitHub stars](https://img.shields.io/github/stars/GigaBitcoin/secp256k1.swift?style=flat)](https://github.com/GigaBitcoin/secp256k1.swift/stargazers) - Swift package for secp256k1 applications, includes Elliptic Curve operations, Schnorr, ZKP and more for Bitcoin.

## .Net Libraries
* [NBitcoin](https://github.com/MetacoSA/NBitcoin) [![GitHub stars](https://img.shields.io/github/stars/MetacoSA/NBitcoin?style=flat)](https://github.com/MetacoSA/NBitcoin/stargazers) - Comprehensive Bitcoin library for the .NET framework.
* [BitcoinLib](https://github.com/cryptean/bitcoinlib) [![GitHub stars](https://img.shields.io/github/stars/cryptean/bitcoinlib?style=flat)](https://github.com/cryptean/bitcoinlib/stargazers) - The most complete, up-to-date, battle-tested .net Library and RPC Wrapper for Bitcoin and Altcoins in C#.

## Haskell Libraries
* [Haskoin-core](https://github.com/haskoin/haskoin-core) [![GitHub stars](https://img.shields.io/github/stars/haskoin/haskoin-core?style=flat)](https://github.com/haskoin/haskoin-core/stargazers) - Haskoin Core is a library of Bitcoin and Bitcoin Cash functions written in Haskell.

## Playgrounds
* [Script Playground](https://www.crmarsh.com/script-playground/)
* [Bitcoin IDE](https://github.com/siminchen/bitcoinIDE) [![GitHub stars](https://img.shields.io/github/stars/siminchen/bitcoinIDE?style=flat)](https://github.com/siminchen/bitcoinIDE/stargazers) - Bitcoin Script for dummies.
* [Script Debugger](https://github.com/kallewoof/btcdeb) [![GitHub stars](https://img.shields.io/github/stars/kallewoof/btcdeb?style=flat)](https://github.com/kallewoof/btcdeb/stargazers)
* [Bitcore Playground](https://bitcore.io/playground/)
* [Mnemonic Code generator](https://iancoleman.io/bip39/)
* [blockchain-demo](https://github.com/anders94/blockchain-demo/) [![GitHub stars](https://img.shields.io/github/stars/anders94/blockchain-demo/?style=flat)](https://github.com/anders94/blockchain-demo//stargazers) - A web-based demonstration of blockchain concepts.
* [Bitcoin Script Debugger](https://github.com/liuhongchao/bitcoin4s) [![GitHub stars](https://img.shields.io/github/stars/liuhongchao/bitcoin4s?style=flat)](https://github.com/liuhongchao/bitcoin4s/stargazers) - Visualize Bitcoin script execution for real transactions.
* [Bitauth IDE](https://ide.bitauth.com/) – An interactive development environment for Bitcoin contracts.
* [ChainQuery Bitcoin RPC](https://chainquery.com) - Run select bitcoin RPC API calls and read full RPC docs in your browser.
* [Bithoven IDE](https://bithoven-lang.github.io/bithoven/ide/) -  Web IDE for Bithoven, A High-Level, Imperative Language for Bitcoin Smart Contracts.

## Blockchain dump
* [BitcoinDatabaseGenerator](https://github.com/ladimolnar/BitcoinDatabaseGenerator) [![GitHub stars](https://img.shields.io/github/stars/ladimolnar/BitcoinDatabaseGenerator?style=flat)](https://github.com/ladimolnar/BitcoinDatabaseGenerator/stargazers) - A high performance data transfer tool that can be used to copy data from Bitcoin Core blockchain files to a SQL Server database.
* [Blockparser+SQL](https://github.com/mcdee/blockparser) [![GitHub stars](https://img.shields.io/github/stars/mcdee/blockparser?style=flat)](https://github.com/mcdee/blockparser/stargazers) - Fast, quick and dirty bitcoin blockchain parser.
* [BitcoinABE](https://github.com/bitcoin-abe/bitcoin-abe) [![GitHub stars](https://img.shields.io/github/stars/bitcoin-abe/bitcoin-abe?style=flat)](https://github.com/bitcoin-abe/bitcoin-abe/stargazers) - Abe: block browser for Bitcoin and similar currencies.
* [Chaingraph](https://github.com/bitauth/chaingraph/) [![GitHub stars](https://img.shields.io/github/stars/bitauth/chaingraph/?style=flat)](https://github.com/bitauth/chaingraph//stargazers) – A multi-node blockchain indexer and GraphQL API.

## Full nodes
* [btcd](https://github.com/btcsuite/btcd/) [![GitHub stars](https://img.shields.io/github/stars/btcsuite/btcd/?style=flat)](https://github.com/btcsuite/btcd//stargazers) - Go-based full node since 2013.
* [Bitcoin-ruby-node](https://github.com/mhanne/bitcoin-ruby-node) [![GitHub stars](https://img.shields.io/github/stars/mhanne/bitcoin-ruby-node?style=flat)](https://github.com/mhanne/bitcoin-ruby-node/stargazers) - bitcoin node based on bitcoin-ruby-blockchain.
* [Fullnode](https://github.com/moneybutton/yours-bitcoin) [![GitHub stars](https://img.shields.io/github/stars/moneybutton/yours-bitcoin?style=flat)](https://github.com/moneybutton/yours-bitcoin/stargazers) - Javascript implementation of bitcoin.
* [Bitcore Node](https://github.com/bitpay/bitcore-node) [![GitHub stars](https://img.shields.io/github/stars/bitpay/bitcore-node?style=flat)](https://github.com/bitpay/bitcore-node/stargazers) - bitcoind linked to node.js by BitPay.
* [Bitcore](https://github.com/bitpay/bitcore) [![GitHub stars](https://img.shields.io/github/stars/bitpay/bitcore?style=flat)](https://github.com/bitpay/bitcore/stargazers) - Formerly just a Nodejs library, now a full node.
* [Bitcoin Core](https://bitcoincore.org/) - direct descendant of the original Bitcoin implementation in C++

## Read
* [A Gentle Introduction to Bitcoin Core Development](https://medium.com/bitcoin-tech-talk/a-gentle-introduction-to-bitcoin-core-development-fdc95eaee6b8)
* [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook) [![GitHub stars](https://img.shields.io/github/stars/bitcoinbook/bitcoinbook?style=flat)](https://github.com/bitcoinbook/bitcoinbook/stargazers)
* [Grokking Bitcoin](https://www.manning.com/books/grokking-bitcoin) - An in-depth technical book with rich illustrations.
* [Bitcoin Stackexchange](https://bitcoin.stackexchange.com)
* [Elliptic Curve Cryptography A Gentle Introduction](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/).
* [Bitcoin Programming with BitcoinJS and Bitcoin Core CLI](https://github.com/bitcoin-studio/Bitcoin-Programming-with-BitcoinJS) [![GitHub stars](https://img.shields.io/github/stars/bitcoin-studio/Bitcoin-Programming-with-BitcoinJS?style=flat)](https://github.com/bitcoin-studio/Bitcoin-Programming-with-BitcoinJS/stargazers).
* [Bitcoin Protocol Development Curriculum - Chaincode Labs](https://github.com/chaincodelabs/bitcoin-curriculum) [![GitHub stars](https://img.shields.io/github/stars/chaincodelabs/bitcoin-curriculum?style=flat)](https://github.com/chaincodelabs/bitcoin-curriculum/stargazers).
* [Lightning Network Protocol Development Curriculum - Chaincode Labs](https://github.com/chaincodelabs/lightning-curriculum) [![GitHub stars](https://img.shields.io/github/stars/chaincodelabs/lightning-curriculum?style=flat)](https://github.com/chaincodelabs/lightning-curriculum/stargazers).
* [btcinformation.org / Developer Documentation](https://btcinformation.org/en/developer-documentation) - Find useful resources, guides and reference material for developers.

## Course
* [Bitcoin & Cryptocurrency](http://bitcoinbook.cs.princeton.edu/).

## Additional Resources
* [@lopp / Bitcoin Developers](https://twitter.com/lopp/lists/bitcoin-developers) - Software developers who have experience working on Bitcoin implementations or applications.
* [@lopp / Lightning Developers](https://twitter.com/i/lists/981976067551490048) - Software developers with experience working on LN implementations / applications.
* [Practical Bitcoin Info - Google Sheets](https://docs.google.com/spreadsheets/d/1Z3Ofa4P8097VWV70Z_bMqIMladngvm-Ck24ot9TDNmw/).
* [A brief history of Bitcoin development...](https://www.youtube.com/watch?v=ZfFNce6CVsE)
* [bitcoin-resources.com](https://bitcoin-resources.com/) Meta-list of Bitcoin resources, from books, articles, to podcasts.
* [Jameson Lopp Bitcoin Resource List](https://www.lopp.net/bitcoin-information.html) Very detailed curated Bitcoin resource list and meta-list by J. Lopp
* [Svrgnty.com: Everything Bitcoin](https://svrgnty.com/) A curated list of the best Bitcoin resources.
* [River Learn](https://river.com/learn) A collection of educational resources to learn about Bitcoin basics, investing, technology, and more.
* [BitcoinCompanies](https://bitcoincompanies.co/) - Corporate Bitcoin treasury map and leaderboard with claimed vs verified holdings.
* [Learn me a Bitcoin - Greg Walker](https://learnmeabitcoin.com/) - extensive learning resource for bitcoin developers
* [Bennet.org](https://bennet.org/) - Interactive technical guides for bitcoiners.
* [Knowing Bitcoin](https://knowingbitcoin.com/) - Comprehensive Bitcoin education with 214+ in-depth guides on Lightning Network, wallets, security, privacy, and nodes.
* [Bitcoin.diy](https://bitcoin.diy) - Bitcoin-only education and hardware wallet reviews, focused on self-custody for beginners and intermediate users.
* [Bitcoin Institute](https://bitcoin-institute.pages.dev) - Bilingual (EN/JP) archive of Satoshi Nakamoto primary sources: forum posts, emails, and mailing-list messages, each linked to its original source.
---

Inspired by the [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) list thing.
Created by BlockchainU fellows.

---

### License

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Igor Barinov](https://github.com/igorbarinov/) [![GitHub stars](https://img.shields.io/github/stars/igorbarinov/?style=flat)](https://github.com/igorbarinov//stargazers) has waived all copyright and related or neighboring rights to this work.
