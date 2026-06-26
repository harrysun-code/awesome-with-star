# Algorand

[![GitHub stars](https://img.shields.io/github/stars/aorumbayev/awesome-algorand?style=flat)](https://github.com/aorumbayev/awesome-algorand/stargazers)

# Awesome Algorand [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
<a href="https://github.com/awesome-algorand/awesome-algorand"><img src="https://dweb.link/ipfs/QmfTGB4EFu1FypcZEWWgs3jCmFw75MrqezVV7oQbnbQPyQ" /></a>
</div>
<br/>
<div align="center">
⚡ A curated list of awesome resources related to the <a href='https://www.algorand.co/'>Algorand</a> Blockchain.
<br />
<br />
Algorand is an open-source, proof of stake Blockchain and smart contract computing platform.
</div>

<p align="center">
    <img  src="https://api.visitorbadge.io/api/visitors?path=aorumbayev%2Fawesome-algorand&countColor=%23000000&style=flat" />
    <a target="_blank" href="https://awesomealgo.com"><img src="https://img.shields.io/badge/url-website-black.svg" /></a>
    <a target="_blank" href="https://github.com/awesome-algorand/awesome-algorand"><img src="https://img.shields.io/badge/url-repository-black.svg" /></a>
    <br />
    <a target="_blank" href="https://rss.com/podcasts/the-awesomealgo-podcast"><img src="https://img.shields.io/badge/podcast-rss-black.svg?color=gold" /></a>
    <a target="_blank" href="https://coinmarketcap.com/currencies/algorand/"><img src="https://img.shields.io/badge/coinmarketcap-price-black.svg?color=teal" /></a>
    <a target="_blank" href="https://github.com/awesome-algorand/awesome-algorand"><img src="https://img.shields.io/github/stars/awesome-algorand/awesome-algorand?color=teal" /></a>
    <a target="_blank" href="https://github.com/awesome-algorand/awesome-algorand/network/members"><img src="https://img.shields.io/github/forks/awesome-algorand/awesome-algorand?color=gold" /></a>
</p>

## Contents

- [Core Resources](#core-resources)
  - [Official Resources](#official-resources)
  - [AlgoKit](#algokit)
  - [AlgoKit Templates](#algokit-templates)
- [Learning Resources](#learning-resources)
  - [Crash Courses](#crash-courses)
  - [General courses](#general-courses)
  - [Tutorials](#tutorials)
  - [Community Resources](#community-resources)
  - [Projects](#projects)
  - [AlgoKit Community Templates](#algokit-community-templates)
- [Development & Tools](#development--tools)
  - [Language SDKs & Tools](#language-sdks--tools)
  - [Smart Contract Development](#smart-contract-development)
  - [CLI](#cli)
  - [IDEs](#ides)
  - [Testing & Debugging](#testing--debugging)
  - [Deployment & Environment](#deployment--environment)
- [Wallets & Asset Interaction](#wallets--asset-interaction)
  - [Wallet Providers](#wallet-providers)
  - [Wallet Development](#wallet-development)
  - [Blockchain Explorers](#blockchain-explorers)
  - [Portfolio Trackers](#portfolio-trackers)
  - [Name Services](#name-services)
- [Infrastructure & Ecosystem Services](#infrastructure--ecosystem-services)
  - [Nodes & Consensus Participation](#nodes--consensus-participation)
  - [Blockchain Bridges](#blockchain-bridges)
  - [Oracles](#oracles)
  - [Security Auditing Services](#security-auditing-services)
  - [Metrics and Analytics Services](#metrics-and-analytics-services)
- [SSI, DID and Verifiable Credentials](#ssi-did-and-verifiable-credentials)
- [AI and Machine Learning](#ai-and-machine-learning)
- [Application Platforms & Examples](#application-platforms--examples)
  - [DeFi Platforms](#defi-platforms)
  - [NFT Marketplaces](#nft-marketplaces)
  - [Prediction Markets](#prediction-markets)
  - [Subscription Management](#subscription-management)
  - [Decentralized voting](#decentralized-voting)
- [Standards](#standards)
  - [Algorand Request for Comments](#algorand-request-for-comments)

## Core Resources

### Official Resources

> Official resources for Algorand.

- [Algorand](https://algorandtechnologies.com/) - Official website.
- [Algorand Foundation](https://algorand.foundation/) - Official website of the Foundation.
- [Algorand FAQ](https://algorand.foundation/faq) - FAQ maintained by the Algorand Foundation.
- [Algorand Governance](https://governance.algorand.foundation/) - Official website of Algorand Governance program.
- [Algorand Developer Portal](https://dev.algorand.co/) - Official Algorand developer portal.
- [Algorand Protocol Specs](https://github.com/algorandfoundation/specs) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/specs?style=flat)](https://github.com/algorandfoundation/specs/stargazers) - Protocol-level specification documents for the Algorand platform.
- [Algorand Discord](https://discord.com/invite/YgPTCVk) - Official Algorand Discord server.

### AlgoKit

> AlgoKit is the official one-stop shop tool for developers building on the Algorand network. Maintained by the Algorand Foundation.

- [algokit-cli](https://github.com/algorandfoundation/algokit-cli) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-cli?style=flat)](https://github.com/algorandfoundation/algokit-cli/stargazers) - The Algorand AlgoKit CLI is the one-stop shop tool for developers building on the Algorand network.
- [algokit-lora](https://lora.algokit.io/mainnet) - Visual local network explorer & app builder for testing Algorand applications (deploy contracts, inspect state, craft transactions).
- [AlgoKit Docs](https://dev.algorand.co/algokit/algokit-intro/) - Official Algorand AlgoKit documentation.
- [algokit-utils-py](https://github.com/algorandfoundation/algokit-utils-py) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-utils-py?style=flat)](https://github.com/algorandfoundation/algokit-utils-py/stargazers) - Algorand AlgoKit Utils for Python.
- [algokit-core](https://github.com/algorandfoundation/algokit-core) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-core?style=flat)](https://github.com/algorandfoundation/algokit-core/stargazers) - Multi-language core primitives (Rust + FFI bindings) powering higher-level AlgoKit tooling (crypto, encoding, protocol logic).
- [algokit-utils-ts](https://github.com/algorandfoundation/algokit-utils-ts) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-utils-ts?style=flat)](https://github.com/algorandfoundation/algokit-utils-ts/stargazers) - Algorand AlgoKit Utils for TypeScript.
- [algokit-client-generator-py](https://github.com/algorandfoundation/algokit-client-generator-py) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-client-generator-py?style=flat)](https://github.com/algorandfoundation/algokit-client-generator-py/stargazers) - Algorand AlgoKit Typed Client Generator for Python.
- [algokit-client-generator-ts](https://github.com/algorandfoundation/algokit-client-generator-ts) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-client-generator-ts?style=flat)](https://github.com/algorandfoundation/algokit-client-generator-ts/stargazers) - Algorand AlgoKit Typed Client Generator for TypeScript.
- [puya](https://github.com/algorandfoundation/puya) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/puya?style=flat)](https://github.com/algorandfoundation/puya/stargazers) - An official Python to TEAL compiler that allows you to write code to execute on the Algorand Virtual Machine (AVM) with Python syntax.
- [puya-ts](https://github.com/algorandfoundation/puya-ts) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/puya-ts?style=flat)](https://github.com/algorandfoundation/puya-ts/stargazers) - An official TypeScript to TEAL compiler frontend, leveraging the core puya compiler, allows you to write code to execute on the Algorand Virtual Machine (AVM) with TypeScript syntax.
- [algorand-python-testing](https://github.com/algorandfoundation/algorand-python-testing) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algorand-python-testing?style=flat)](https://github.com/algorandfoundation/algorand-python-testing/stargazers) - A Python library for unit testing Algorand Python smart contracts without the need to interact with the Algorand Blockchain.
- [algorand-TypeScript-testing](https://github.com/algorandfoundation/algorand-TypeScript-testing) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algorand-TypeScript-testing?style=flat)](https://github.com/algorandfoundation/algorand-TypeScript-testing/stargazers) - A TypeScript library for unit testing Algorand smart contracts without the need to interact with the Algorand Blockchain.
- [algokit-avm-vscode-debugger](https://github.com/algorandfoundation/algokit-avm-vscode-debugger) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-avm-vscode-debugger?style=flat)](https://github.com/algorandfoundation/algokit-avm-vscode-debugger/stargazers) - VSCode extension for line‑by‑line debugging of Algorand Python, TypeScript, TealScript and raw TEAL smart contracts via AVM traces.

### AlgoKit Templates
> AlgoKit templates are a set of starter and production-ready baseline templates for developing and deploying Algorand applications. They are designed to be used as a starting point for developers to quickly bootstrap their projects and focus on the business logic of their applications. Refer to [Creating AlgoKit Templates](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/tutorials/algokit-template.md) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-cli/blob/main/docs/tutorials/algokit-template.md?style=flat)](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/tutorials/algokit-template.md/stargazers) for a general guide on how to create your own AlgoKit templates.

- [algokit-python-template](https://github.com/algorandfoundation/algokit-python-template) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-python-template?style=flat)](https://github.com/algorandfoundation/algokit-python-template/stargazers) - Official AlgoKit's Algorand Python template provides a production-ready baseline for developing and deploying smart contracts in Python.
- [algokit-TypeScript-template](https://github.com/algorandfoundation/algokit-TypeScript-template) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-TypeScript-template?style=flat)](https://github.com/algorandfoundation/algokit-TypeScript-template/stargazers) - Official AlgoKit's Algorand TypeScript template provides a production-ready baseline for developing and deploying smart contracts in TypeScript.
- [algokit-react-frontend-template](https://github.com/algorandfoundation/algokit-react-frontend-template) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-react-frontend-template?style=flat)](https://github.com/algorandfoundation/algokit-react-frontend-template/stargazers) - Official AlgoKit React frontend template provides a production-ready baseline for developing and deploying React frontend applications with Algorand dependencies integrated. Also serves as a reference for template builders on implementing standalone algokit frontend templates.
- [algokit-fullstack-template](https://github.com/algorandfoundation/algokit-fullstack-template) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-fullstack-template?style=flat)](https://github.com/algorandfoundation/algokit-fullstack-template/stargazers) - Official AlgoKit fullstack template provides a production-ready baseline for developing and deploying fullstack applications with Algorand dependencies integrated. Also serves as a reference for template builders on how to combine standalone algokit templates under one full stack template project.

## Learning Resources

> List of learning resources for Algorand. Includes courses, tutorials, and other resources.

### Crash Courses

- [Algorand School](https://github.com/cusma/algorand-school) [![GitHub stars](https://img.shields.io/github/stars/cusma/algorand-school?style=flat)](https://github.com/cusma/algorand-school/stargazers) - Crash course slide deck.
- [Zero to Hero PyTeal](https://www.youtube.com/playlist?list=PLwRyHoehE435ttTjvFZA-DyqHYIYc26K_) - PyTeal crash course video lectures.
- [Algorand, efficient self-sustaining Blockchain](https://prismic-io.s3.amazonaws.com/algorandfoundationv2/d5407f96-8e7d-4465-9656-2abb558850a9_Proof+of+Stake+Blockchain+Efficiency+Framework.pdf) - Proof of Stake Blockchain Efficiency Framework.
- [Algorand Efficiency](https://www.youtube.com/watch?v=e8s8Ui8vDaY) - Understanding Algorand's working principles and its efficiency.
- [Introduction to AVM and Applications](https://www.youtube.com/watch?v=fTAPLiPcj28) - Introduction to the Algorand Virtual Machine architecture and Algorand Smart Contracts (aka Applications).
- [Introduction to PyTeal](https://www.youtube.com/watch?v=zXDqJHK_Bqs) - Walkthrough of PyTeal, the Python framework for developing Algorand smart contracts (with [@matteojug](https://twitter.com/matteojug)).
- [PyTeal ABI Smart Contracts](https://www.youtube.com/watch?v=USLcyfVD_ws) - Using PyTeal to develop _ABI-compliant_ Smart Contracts on Algorand. Final live coding section (with [@deanste](https://twitter.com/_deanste)).
- [Beaker](https://www.youtube.com/watch?v=031VvOxvuxY) - Framework for Algorand Smart Contract development, client and testing based on PyTeal. Live coding session (with [@HGKimChris](https://twitter.com/HGKimChris)).
- [Dissecting Algorand](https://medium.com/coinmonks/dissecting-algorand-e962f48f8c72) - Introduction Algorand and an analysis on Algorand's inner workings.
- [Zero to Hero Blockchain Algorand](https://github.com/VKappaKV/Zero-To-Hero-blockchain-Algorand) [![GitHub stars](https://img.shields.io/github/stars/VKappaKV/Zero-To-Hero-blockchain-Algorand?style=flat)](https://github.com/VKappaKV/Zero-To-Hero-blockchain-Algorand/stargazers) - Curated learning path for Algorand developers.


### General courses

> Please note these are intended for absolute beginners interested in foundational knowledge relatable to all Blockchain systems. Building a theoretical understanding of the domain of Blockchain protocols is an important prerequisite that can significantly amplify your learning about Algorand technology.

- [Foundations of Blockchains](https://www.youtube.com/watch?v=KNJGPI0fuFA&list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA) - A video course by Tim Roughgarden a Professor of Computer Science at Columbia University highlighting the fundamental principles, concepts and properties of Blockchain protocols.

### Tutorials

- [Lending pool using Reach](https://developer.algorand.org/tutorials/building-a-lending-pool-using-reach/) - Tutorial on how to build a lending pool using the Reach language.
- [Creating a License Manager Contract](https://developer.algorand.org/tutorials/creating-a-license-manager-contract-utilizing-pyteal-and-inner-transactions/) - Tutorial on utilizing PyTEAL and Inner Transactions.
- [Stateless session management with the Pera wallet](https://developer.algorand.org/tutorials/stateless-session-management-with-the-pera-wallet/) - Pera Wallet connection example with Next.js and Redux.
- [AlgoMinter](https://developer.algorand.org/tutorials/algominter-a-web-app-for-minting-assets-using-python-algosigner-and-anvil-platform/) - Build your web app for minting assets using Python, AlgoSigner, and Anvil Platform.
- [Getting Started with Django, Python, and Algorand](https://developer.algorand.org/solutions/getting-started-with-python-algorand-sdk-and-django/) - Tutorial from algorand developer portal.
- [MultiSig with Algorand for Co-operative Groups](https://developer.algorand.org/tutorials/decentralised-co-operative-unions-algorand-multisignature-account/) - Decentralised co-operative unions with Algorand Multisignature Account.
- [Adding Notes to Transactions](https://developer.algorand.org/tutorials/v2-read-and-write-transaction-note-field-python/) - Read and Write to the Transaction Note Field with Python.
- [Create Assets with a Stateful Smart Contract](https://developer.algorand.org/solutions/using-stateful-smart-contract-to-create-algorand-standard-asset/) - Using Stateful Smart Contract To Create Algorand Standard Asset.
- [Artificial Intelligence on Algorand](https://developer.algorand.org/solutions/artificial-intelligence-on-algorand/) - Tutorial on using machine learning to predict the transaction volume of the USDC stablecoin on the Algorand Blockchain.

### Community Resources

> The following contains sections related to open source projects, utilities, and news resources.

### Projects

> A list of open source projects, blogs, websites that are built on top of Algorand.

- [arc3.xyz](https://github.com/barnjamin/arc3.xyz) [![GitHub stars](https://img.shields.io/github/stars/barnjamin/arc3.xyz?style=flat)](https://github.com/barnjamin/arc3.xyz/stargazers) - Dapp that can be used to mint ARC3 compliant NFTs.
- [Auction Demo](https://github.com/algorand/auction-demo) [![GitHub stars](https://img.shields.io/github/stars/algorand/auction-demo?style=flat)](https://github.com/algorand/auction-demo/stargazers) - On-chain NFT auction using smart contracts.
- [Algorand Session Wallet](https://github.com/barnjamin/algorand-session-wallet) [![GitHub stars](https://img.shields.io/github/stars/barnjamin/algorand-session-wallet?style=flat)](https://github.com/barnjamin/algorand-session-wallet/stargazers) - Session wallet to allow persisted wallet connections across multiple wallets.
- [AlgoWorld-Contracts](https://github.com/algoworldNFT/algoworld-contracts) [![GitHub stars](https://img.shields.io/github/stars/algoworldNFT/algoworld-contracts?style=flat)](https://github.com/algoworldNFT/algoworld-contracts/stargazers) - Collection of all smart contracts used by AlgoWorld, written in PyTeal.
- [AlgoWorld-Swapper](https://github.com/algoworldNFT/algoworld-swapper) [![GitHub stars](https://img.shields.io/github/stars/algoworldNFT/algoworld-swapper?style=flat)](https://github.com/algoworldNFT/algoworld-swapper/stargazers) - Free and trustless ASA swapper, powered by Algorand Smart Signatures.
- [WalletConnect Example DApp](https://github.com/algorand/walletconnect-example-dapp) [![GitHub stars](https://img.shields.io/github/stars/algorand/walletconnect-example-dapp?style=flat)](https://github.com/algorand/walletconnect-example-dapp/stargazers) - Algorand WalletConnect demo.
- [TinyBar App](https://github.com/aorumbayev/tinybar) [![GitHub stars](https://img.shields.io/github/stars/aorumbayev/tinybar?style=flat)](https://github.com/aorumbayev/tinybar/stargazers) - A tiny macOS menu bar app for tracking ASA prices from TinyMan.
- [algonim](https://github.com/cusma/algonim) [![GitHub stars](https://img.shields.io/github/stars/cusma/algonim?style=flat)](https://github.com/cusma/algonim/stargazers) - First Algorand mini-puzzle-game. Written in Python+PyTEAL by [@cusma](https://twitter.com/cusma_b).
- [algorealm](https://github.com/algorealm/algorealm) [![GitHub stars](https://img.shields.io/github/stars/algorealm/algorealm?style=flat)](https://github.com/algorealm/algorealm/stargazers) - Claim the Crown and the Sceptre of Algorand Realm! Written in Python+PyTEAL by [@cusma](https://github.com/cusma) [![GitHub stars](https://img.shields.io/github/stars/cusma?style=flat)](https://github.com/cusma/stargazers).
- [algorealm-ui](https://github.com/algorealm/algorealm-ui) [![GitHub stars](https://img.shields.io/github/stars/algorealm/algorealm-ui?style=flat)](https://github.com/algorealm/algorealm-ui/stargazers) - A web CLI Emulator version of algorealm cli game by @aorumbayev.
- [minter](https://github.com/algofishexe/minter) [![GitHub stars](https://img.shields.io/github/stars/algofishexe/minter?style=flat)](https://github.com/algofishexe/minter/stargazers) - Bulk mint Algorand NFTs following the ARC-69 community standard. Written in Node.js by [@fish.exe](https://twitter.com/AlgofishExe).
- [algovanity](https://algovanity.com/) - Algorand Vanity Address Generator from [Ripe](https://github.com/Ripe/algovanity) [![GitHub stars](https://img.shields.io/github/stars/Ripe/algovanity?style=flat)](https://github.com/Ripe/algovanity/stargazers).
- [galvanity](https://github.com/shmutalov/galvanity) [![GitHub stars](https://img.shields.io/github/stars/shmutalov/galvanity?style=flat)](https://github.com/shmutalov/galvanity/stargazers) - Go-based Algorand vanity address generator.
- [genpyteal](https://github.com/runvnc/genpyteal) [![GitHub stars](https://img.shields.io/github/stars/runvnc/genpyteal?style=flat)](https://github.com/runvnc/genpyteal/stargazers) - Generate PyTeal from (mostly) normal Python.
- [AgorHash](https://github.com/bafio89/agorhash) [![GitHub stars](https://img.shields.io/github/stars/bafio89/agorhash?style=flat)](https://github.com/bafio89/agorhash/stargazers) - Public, permissionless, decentralized and uncensorable free speech protocol.
- [QRCode Generator](https://github.com/emg110/algorand-qrcode) [![GitHub stars](https://img.shields.io/github/stars/emg110/algorand-qrcode?style=flat)](https://github.com/emg110/algorand-qrcode/stargazers) - Uinversal QRCode generator module for Algorand ARC-26 URIs.
- [algofractals](https://github.com/aorumbayev/algofractals) [![GitHub stars](https://img.shields.io/github/stars/aorumbayev/algofractals?style=flat)](https://github.com/aorumbayev/algofractals/stargazers) - Mint randomly generated mandelbrot fractals with embedded ARC69 tags. (Archived on Dec 31, 2023)
- [algorewards](https://algorewards.github.io/) - Free and unofficial Algorand governance reward calculator. Hosted on GitHub Pages.
- [Pipeline-UI](https://github.com/headline-design/pipeline-ui) [![GitHub stars](https://img.shields.io/github/stars/headline-design/pipeline-ui?style=flat)](https://github.com/headline-design/pipeline-ui/stargazers) - A React.js based component library for rapid deployment of Algorand Dapps.
- [STOI](https://stoi.org/) - Song ownership gone decentralized via microDAOs.
- [AlgoTables](https://algotables.github.io/) - A suite of tools designed to aid everyday hodlers of ALGO who participate in the Algorand ecosystem.
- [AlgoPing](https://github.com/aorumbayev/algoping) [![GitHub stars](https://img.shields.io/github/stars/aorumbayev/algoping?style=flat)](https://github.com/aorumbayev/algoping/stargazers) - A tiny cron job that issues a [tweet](https://twitter.com/algoping) if public Algorand Nodes (AlgoExplorer, AlgoNode and etc) are not healthy.
- [staketaxcsv](https://github.com/hodgerpodger/staketaxcsv) [![GitHub stars](https://img.shields.io/github/stars/hodgerpodger/staketaxcsv?style=flat)](https://github.com/hodgerpodger/staketaxcsv/stargazers) - Python backend for [stake.tax](https://stake.tax) that generates taxable transactions CSVs for Algorand and other Blockchains.
- [Automated Prediction Market Maker on Algorand](https://github.com/dspytdao/Algo_AMM) [![GitHub stars](https://img.shields.io/github/stars/dspytdao/Algo_AMM?style=flat)](https://github.com/dspytdao/Algo_AMM/stargazers) - backend repository with project hosted at [algoAMM.com](https://algoamm.com).
- [AlgoDepo](https://github.com/dspytdao/AlgoDepo) [![GitHub stars](https://img.shields.io/github/stars/dspytdao/AlgoDepo?style=flat)](https://github.com/dspytdao/AlgoDepo/stargazers) - Single Deposit App Algorand.
- [AlgoDeposit](https://github.com/dspytdao/AlgoDeposit) [![GitHub stars](https://img.shields.io/github/stars/dspytdao/AlgoDeposit?style=flat)](https://github.com/dspytdao/AlgoDeposit/stargazers) - AMM Pool App Algorand.
- [txnDuck](https://github.com/No-Cash-7970/txnDuck) [![GitHub stars](https://img.shields.io/github/stars/No-Cash-7970/txnDuck?style=flat)](https://github.com/No-Cash-7970/txnDuck/stargazers) - Transaction building tool for Algorand blockchain.
- [lazylora](https://github.com/aorumbayev/lazylora) [![GitHub stars](https://img.shields.io/github/stars/aorumbayev/lazylora?style=flat)](https://github.com/aorumbayev/lazylora/stargazers) - Terminal UI for exploring Algorand blockchain.
- [wen-tools](https://github.com/LoafPickleWW/wen-tools) [![GitHub stars](https://img.shields.io/github/stars/LoafPickleWW/wen-tools?style=flat)](https://github.com/LoafPickleWW/wen-tools/stargazers) - Bulk operations tool for Algorand.
- [algonoderewards](https://github.com/cryptomalgo/algonoderewards) [![GitHub stars](https://img.shields.io/github/stars/cryptomalgo/algonoderewards?style=flat)](https://github.com/cryptomalgo/algonoderewards/stargazers) - Track and visualize Algorand node rewards using Nodely API.
- [xGov-Guru](https://github.com/SilentRhetoric/xGov-Guru) [![GitHub stars](https://img.shields.io/github/stars/SilentRhetoric/xGov-Guru?style=flat)](https://github.com/SilentRhetoric/xGov-Guru/stargazers) - Tool to browse xGov voting data and proposals.

### AlgoKit Community Templates

> AlgoKit community templates are a set of starter and production-ready baseline templates for developing and deploying Algorand applications created by the projects and individuals in the Algorand community.

- [algokit-tealish-template](https://github.com/aorumbayev/algokit-tealish-template) [![GitHub stars](https://img.shields.io/github/stars/aorumbayev/algokit-tealish-template?style=flat)](https://github.com/aorumbayev/algokit-tealish-template/stargazers) - AlgoKit community template for quick starting a smart contract project with tealish and algojig.
- [algokit-goracle-template](https://github.com/GoracleNetwork/algokit_default_template) [![GitHub stars](https://img.shields.io/github/stars/GoracleNetwork/algokit_default_template?style=flat)](https://github.com/GoracleNetwork/algokit_default_template/stargazers) - Algokit community template for quick starting a smart contract project interacting with goracle.
- [algokit-subtopia-template](https://github.com/subtopia-algo/algokit-subtopia-template) [![GitHub stars](https://img.shields.io/github/stars/subtopia-algo/algokit-subtopia-template?style=flat)](https://github.com/subtopia-algo/algokit-subtopia-template/stargazers) - Algokit community template for quick starting a dapp frontend project interacting with Subtopia platform.

## Development & Tools

> Awesome client libraries, tools, and community utilities for development.

### Language SDKs & Tools

> Awesome client libraries, tools, and community utilities sorted by the language of implementation.

#### C/C++

- [vertices-algorand-sdk](https://github.com/vertices-network/c-vertices-sdk) [![GitHub stars](https://img.shields.io/github/stars/vertices-network/c-vertices-sdk?style=flat)](https://github.com/vertices-network/c-vertices-sdk/stargazers) - The Vertices SDK provides developers with easy device access to interact with Blockchains.
- [unreal-algorand-sdk](https://github.com/Wisdom-Labs/Algorand-Unreal-Engine-SDK) [![GitHub stars](https://img.shields.io/github/stars/Wisdom-Labs/Algorand-Unreal-Engine-SDK?style=flat)](https://github.com/Wisdom-Labs/Algorand-Unreal-Engine-SDK/stargazers) - Official Unreal Engine plugin for Algorand Blockchain Platform.
- [cplusplus-algorand-sdk](https://github.com/Wisdom-Labs/Algorand-CPlusPlus-SDK) [![GitHub stars](https://img.shields.io/github/stars/Wisdom-Labs/Algorand-CPlusPlus-SDK?style=flat)](https://github.com/Wisdom-Labs/Algorand-CPlusPlus-SDK/stargazers) - Algorand C++ SDK: This repo is providing C++ sdk on algorand chain.

#### Dart

- [dart-algorand-sdk](https://pub.dev/packages/algorand_dart) - Dart Algorand SDK.

#### Go

- [go-algorand](https://github.com/algorand/go-algorand) [![GitHub stars](https://img.shields.io/github/stars/algorand/go-algorand?style=flat)](https://github.com/algorand/go-algorand/stargazers) - Algorand's official implementation in Go.
- [go-algorand-sdk](https://github.com/algorand/go-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/algorand/go-algorand-sdk?style=flat)](https://github.com/algorand/go-algorand-sdk/stargazers) - The Algorand Golang SDK.
- [conduit](https://github.com/algorand/conduit) [![GitHub stars](https://img.shields.io/github/stars/algorand/conduit?style=flat)](https://github.com/algorand/conduit/stargazers) - Algorand's data pipeline framework.

#### PHP

- [php-algorand-sdk](https://github.com/ffsolutions/php-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/ffsolutions/php-algorand-sdk?style=flat)](https://github.com/ffsolutions/php-algorand-sdk/stargazers) - Algorand PHP SDK created by [@ffsolutions](https://github.com/ffsolutions) [![GitHub stars](https://img.shields.io/github/stars/ffsolutions?style=flat)](https://github.com/ffsolutions/stargazers).
- [algorand-php](https://github.com/RootSoft/algorand-php) [![GitHub stars](https://img.shields.io/github/stars/RootSoft/algorand-php?style=flat)](https://github.com/RootSoft/algorand-php/stargazers) - Algorand PHP SDK created by [@RootSoft](https://github.com/RootSoft) [![GitHub stars](https://img.shields.io/github/stars/RootSoft?style=flat)](https://github.com/RootSoft/stargazers).

#### Python

- [py-algorand-sdk](https://github.com/algorand/py-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/algorand/py-algorand-sdk?style=flat)](https://github.com/algorand/py-algorand-sdk/stargazers) - The Algorand Python SDK.
- [tinyman-py-sdk](https://github.com/tinymanorg/tinyman-py-sdk) [![GitHub stars](https://img.shields.io/github/stars/tinymanorg/tinyman-py-sdk?style=flat)](https://github.com/tinymanorg/tinyman-py-sdk/stargazers) - Tinyman Python SDK.
- [smart-asa](https://github.com/algorandlabs/smart-asa) [![GitHub stars](https://img.shields.io/github/stars/algorandlabs/smart-asa?style=flat)](https://github.com/algorandlabs/smart-asa/stargazers) - Smart ASA PyTeal reference implementation based on ARC-20.

#### JavaScript & TypeScript

- [js-algorand-sdk](https://github.com/algorand/js-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/algorand/js-algorand-sdk?style=flat)](https://github.com/algorand/js-algorand-sdk/stargazers) - The Algorand JavaScript SDK & Examples.
- [algo-builder](https://github.com/scale-it/algo-builder) [![GitHub stars](https://img.shields.io/github/stars/scale-it/algo-builder?style=flat)](https://github.com/scale-it/algo-builder/stargazers) - Framework to automate development of Algorand Assets and Smart Contracts.
- [algo-builder-templates](https://github.com/scale-it/algo-builder-templates) [![GitHub stars](https://img.shields.io/github/stars/scale-it/algo-builder-templates?style=flat)](https://github.com/scale-it/algo-builder-templates/stargazers) - Dapps templates for Algo Builder.
- [algonaut.js](https://github.com/thencc/algonautjs) [![GitHub stars](https://img.shields.io/github/stars/thencc/algonautjs?style=flat)](https://github.com/thencc/algonautjs/stargazers) - An easier Algo sdk for front-end dapps (TypeScript).
- [perawallet-connect](https://github.com/perawallet/connect) [![GitHub stars](https://img.shields.io/github/stars/perawallet/connect?style=flat)](https://github.com/perawallet/connect/stargazers) - JavaScript SDK for integrating Pera Wallet to web applications.
- [defly-connect](https://github.com/blockshake-io/defly-connect) [![GitHub stars](https://img.shields.io/github/stars/blockshake-io/defly-connect?style=flat)](https://github.com/blockshake-io/defly-connect/stargazers) - JavaScript SDK for integrating Defly Wallet to web applications.
- [subtopia-js](https://github.com/subtopia-algo/subtopia-js) [![GitHub stars](https://img.shields.io/github/stars/subtopia-algo/subtopia-js?style=flat)](https://github.com/subtopia-algo/subtopia-js/stargazers) - Subtopia JavaScript SDK providing convenient interfaces to interact with Subtopia platform.
- [solid-algo-wallets](https://github.com/SilentRhetoric/solid-algo-wallets) [![GitHub stars](https://img.shields.io/github/stars/SilentRhetoric/solid-algo-wallets?style=flat)](https://github.com/SilentRhetoric/solid-algo-wallets/stargazers) - SolidJS wallet integration library for Algorand.

#### Java

- [java-algorand-sdk](https://github.com/algorand/java-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/algorand/java-algorand-sdk?style=flat)](https://github.com/algorand/java-algorand-sdk/stargazers) - The Algorand Java SDK.

#### .NET

- [dotnet-algorand-sdk](https://github.com/RileyGe/dotnet-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/RileyGe/dotnet-algorand-sdk?style=flat)](https://github.com/RileyGe/dotnet-algorand-sdk/stargazers) - Algorand .NET SDK created by [@RileyGe](https://github.com/RileyGe) [![GitHub stars](https://img.shields.io/github/stars/RileyGe?style=flat)](https://github.com/RileyGe/stargazers).
- [unity-algorand-sdk](https://github.com/CareBoo/unity-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/CareBoo/unity-algorand-sdk?style=flat)](https://github.com/CareBoo/unity-algorand-sdk/stargazers) - An Algorand SDK for Unity. Use the Algorand Blockchain in your video game.
- [unity-algorand-sdk-based-on-net-sdk](https://github.com/Vytek/AlgorandUnitySDK) [![GitHub stars](https://img.shields.io/github/stars/Vytek/AlgorandUnitySDK?style=flat)](https://github.com/Vytek/AlgorandUnitySDK/stargazers) - Quick and dirty Unity SDK based on .NET Algorand SDK by RileyGe.
- [dotnet-alogrand-sdk (2)](https://github.com/FrankSzendzielarz/dotnet-algorand-sdk) [![GitHub stars](https://img.shields.io/github/stars/FrankSzendzielarz/dotnet-algorand-sdk?style=flat)](https://github.com/FrankSzendzielarz/dotnet-algorand-sdk/stargazers) - Algorand .NET SDK maintained by [@FrankSzendzielarz](https://github.com/FrankSzendzielarz) [![GitHub stars](https://img.shields.io/github/stars/FrankSzendzielarz?style=flat)](https://github.com/FrankSzendzielarz/stargazers).
- [dotnet-tinyman-sdk](https://github.com/geoffodonnell/dotnet-tinyman-sdk) [![GitHub stars](https://img.shields.io/github/stars/geoffodonnell/dotnet-tinyman-sdk?style=flat)](https://github.com/geoffodonnell/dotnet-tinyman-sdk/stargazers) - Tinyman .NET SDK.
- [dotnet-yieldly-sdk](https://github.com/geoffodonnell/dotnet-yieldly-sdk) [![GitHub stars](https://img.shields.io/github/stars/geoffodonnell/dotnet-yieldly-sdk?style=flat)](https://github.com/geoffodonnell/dotnet-yieldly-sdk/stargazers) - Yieldly .NET SDK.
- [powershell-algorand-module](https://github.com/geoffodonnell/powershell-algorand-module) [![GitHub stars](https://img.shields.io/github/stars/geoffodonnell/powershell-algorand-module?style=flat)](https://github.com/geoffodonnell/powershell-algorand-module/stargazers) - Algorand PowerShell Module.

#### Rust

- [rust-algorand-sdk](https://github.com/manuelmauro/algonaut) [![GitHub stars](https://img.shields.io/github/stars/manuelmauro/algonaut?style=flat)](https://github.com/manuelmauro/algonaut/stargazers) - Rust Algorand SDK.

#### Swift

- [algorand-wallet](https://github.com/algorand/algorand-wallet) [![GitHub stars](https://img.shields.io/github/stars/algorand/algorand-wallet?style=flat)](https://github.com/algorand/algorand-wallet/stargazers) - Algorand wallet official implementation in Swift.
- [swift-algorand](https://github.com/CorvidLabs/swift-algorand) [![GitHub stars](https://img.shields.io/github/stars/CorvidLabs/swift-algorand?style=flat)](https://github.com/CorvidLabs/swift-algorand/stargazers) - Modern Swift SDK for the Algorand Blockchain with async/await and Swift concurrency support.
- [swift-algorand-sdk](https://github.com/Jesulonimi21/Swift-Algorand-Sdk) [![GitHub stars](https://img.shields.io/github/stars/Jesulonimi21/Swift-Algorand-Sdk?style=flat)](https://github.com/Jesulonimi21/Swift-Algorand-Sdk/stargazers) - A Swift SDK for interacting with the Algorand Blockchain.
- [swift-algokit](https://github.com/CorvidLabs/swift-algokit) [![GitHub stars](https://img.shields.io/github/stars/CorvidLabs/swift-algokit?style=flat)](https://github.com/CorvidLabs/swift-algokit/stargazers) - AlgoKit utilities for Swift developers.
- [swift-arc](https://github.com/CorvidLabs/swift-arc) [![GitHub stars](https://img.shields.io/github/stars/CorvidLabs/swift-arc?style=flat)](https://github.com/CorvidLabs/swift-arc/stargazers) - Swift library for working with Algorand ARC metadata standards for NFTs.
- [swift-mint](https://github.com/CorvidLabs/swift-mint) [![GitHub stars](https://img.shields.io/github/stars/CorvidLabs/swift-mint?style=flat)](https://github.com/CorvidLabs/swift-mint/stargazers) - Swift library for minting NFTs on the Algorand Blockchain.
- [swift-algochat](https://github.com/CorvidLabs/swift-algochat) [![GitHub stars](https://img.shields.io/github/stars/CorvidLabs/swift-algochat?style=flat)](https://github.com/CorvidLabs/swift-algochat/stargazers) - End-to-end encrypted messaging on Algorand with hybrid ECDH and PSK ratcheting in Swift.

#### Ruby

- [TEALrb](https://github.com/joe-p/TEALrb) [![GitHub stars](https://img.shields.io/github/stars/joe-p/TEALrb?style=flat)](https://github.com/joe-p/TEALrb/stargazers) - A Ruby DSL for writing Algorand smart contracts. (Archived on Jan 22, 2023)


### Smart Contract Development

#### Languages & Compilers
- [pyteal](https://github.com/algorand/pyteal) [![GitHub stars](https://img.shields.io/github/stars/algorand/pyteal?style=flat)](https://github.com/algorand/pyteal/stargazers) - Algorand Smart Contracts in Python.
- [reach](https://docs.reach.sh) - A domain-specific language for building cross chain decentralized applications (DApps).
- [aqua-compiler](https://github.com/optio-labs/aqua-compiler) [![GitHub stars](https://img.shields.io/github/stars/optio-labs/aqua-compiler?style=flat)](https://github.com/optio-labs/aqua-compiler/stargazers) - An expressive high level language for the Algorand block chain that compiles to TEAL code.
- [algoml](https://github.com/petitnau/algoml) [![GitHub stars](https://img.shields.io/github/stars/petitnau/algoml?style=flat)](https://github.com/petitnau/algoml/stargazers) - A domain-specific language for specifying Algorand smart contracts, which compiles into TEAL scripts.
- [tealang](https://github.com/pzbitskiy/tealang) [![GitHub stars](https://img.shields.io/github/stars/pzbitskiy/tealang?style=flat)](https://github.com/pzbitskiy/tealang/stargazers) - A high level language for Algorand ASC1 and TEAL.
- [tealish](https://tealish.tinyman.org) - Readable Algorand VM language enabling procedural-style TEAL focused on clarity.
- [TEALScript](https://github.com/algorand-devrel/TEALScript) [![GitHub stars](https://img.shields.io/github/stars/algorand-devrel/TEALScript?style=flat)](https://github.com/algorand-devrel/TEALScript/stargazers) - Enables Algorand smart contract development with native TypeScript syntax, tooling, and IDE support.

#### Frameworks & Utilities
- [beaker](https://github.com/algorandfoundation/beaker) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/beaker?style=flat)](https://github.com/algorandfoundation/beaker/stargazers) - Pythonic smart contract framework (PyTEAL DSL wrappers, client + testing utilities). (Canonical repo)
- [pyteal-utils](https://github.com/algorand/pyteal-utils) [![GitHub stars](https://img.shields.io/github/stars/algorand/pyteal-utils?style=flat)](https://github.com/algorand/pyteal-utils/stargazers) - PyTEAL utilities library.
- [avm-semantics](https://github.com/runtimeverification/avm-semantics) [![GitHub stars](https://img.shields.io/github/stars/runtimeverification/avm-semantics?style=flat)](https://github.com/runtimeverification/avm-semantics/stargazers) - Algorand Virtual Machine and TEAL Semantics in K framework. Aids with testing and formal verification of smart contracts.
- [d-asa](https://github.com/cusma/d-asa) [![GitHub stars](https://img.shields.io/github/stars/cusma/d-asa?style=flat)](https://github.com/cusma/d-asa/stargazers) - Debt Algorand Standard Application providing reference implementations and interfaces for tokenizing debt instruments (bonds, loans, commercial papers) that conform to ACTUS standards.


### CLI

- [AlgoRun](https://github.com/algorandfoundation/algorun) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algorun?style=flat)](https://github.com/algorandfoundation/algorun/stargazers) - Simple CLI utility for setting up and starting an Algorand MainNet participation node.


### IDEs

> Awesome client libraries, tools, community plugins and integrations for IDEs.

#### vim

- [vim-algorand-teal](https://github.com/aldur/vim-algorand-teal) [![GitHub stars](https://img.shields.io/github/stars/aldur/vim-algorand-teal?style=flat)](https://github.com/aldur/vim-algorand-teal/stargazers) - Minimalistic syntax highlight for Algorand's TEAL Smart Contract language to vim.

#### IntelliJ

- [algoDEA](https://algodea-docs.bloxbean.com/) - Algorand IntelliJ Plugin.

#### VSCode

- [Obsidian Labs/vscode-algorand](https://github.com/ObsidianLabs/vscode-algorand) [![GitHub stars](https://img.shields.io/github/stars/ObsidianLabs/vscode-algorand?style=flat)](https://github.com/ObsidianLabs/vscode-algorand/stargazers) - Algorand VS Code Extension.
- [optio-labs/teal-debugger-extension](https://github.com/optio-labs/teal-debugger-extension) [![GitHub stars](https://img.shields.io/github/stars/optio-labs/teal-debugger-extension?style=flat)](https://github.com/optio-labs/teal-debugger-extension/stargazers) - Debug teal with minimal AVM configuration inside VSCode.

#### Visual Studio

- [Algorand Visual Studio Extension](https://github.com/FrankSzendzielarz/AlgorandVisualStudio) [![GitHub stars](https://img.shields.io/github/stars/FrankSzendzielarz/AlgorandVisualStudio?style=flat)](https://github.com/FrankSzendzielarz/AlgorandVisualStudio/stargazers) - Visual Studio extensions for C# TEAL compilation and Algorand Smart Contract development.


### Testing & Debugging

- [graviton](https://github.com/algorand/graviton) [![GitHub stars](https://img.shields.io/github/stars/algorand/graviton?style=flat)](https://github.com/algorand/graviton/stargazers) - Algorand's TEAL blackbox testing toolkit.
- [algokit-avm-debugger](https://github.com/algorandfoundation/algokit-avm-debugger) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/algokit-avm-debugger?style=flat)](https://github.com/algorandfoundation/algokit-avm-debugger/stargazers) - Standalone AVM Debug Adapter Protocol implementation powering advanced contract debugging tooling.
- [tealer](https://github.com/crytic/tealer) [![GitHub stars](https://img.shields.io/github/stars/crytic/tealer?style=flat)](https://github.com/crytic/tealer/stargazers) - Static TEAL analyser with a set of vulnerability detectors for quick contracts reviews.
- [irulan](https://irulan.dev/) - Web app for deploying + testing smart contracts ([open source! + PRs welcome](https://github.com/thencc/irulan) [![GitHub stars](https://img.shields.io/github/stars/thencc/irulan?style=flat)](https://github.com/thencc/irulan/stargazers)).
- [algojig](https://github.com/Hipo/algojig) [![GitHub stars](https://img.shields.io/github/stars/Hipo/algojig?style=flat)](https://github.com/Hipo/algojig/stargazers) - A tool for testing Algorand smart contracts.
- [tealinspector](https://github.com/Hipo/tealinspector) [![GitHub stars](https://img.shields.io/github/stars/Hipo/tealinspector?style=flat)](https://github.com/Hipo/tealinspector/stargazers) - Quick and easy TEAL code debugging by Hipo labs.
- [swift-algotest](https://github.com/CorvidLabs/swift-algotest) [![GitHub stars](https://img.shields.io/github/stars/CorvidLabs/swift-algotest?style=flat)](https://github.com/CorvidLabs/swift-algotest/stargazers) - Swift testing framework for Algorand smart contracts with mock chain support.


### Deployment & Environment

- [Algorand Sandbox](https://github.com/algorand/sandbox) [![GitHub stars](https://img.shields.io/github/stars/algorand/sandbox?style=flat)](https://github.com/algorand/sandbox/stargazers) - Fast way to create and configure an Algorand development environment.
- [Algorand Sandbox Dev](https://github.com/MakerXStudio/algorand-sandbox-dev) [![GitHub stars](https://img.shields.io/github/stars/MakerXStudio/algorand-sandbox-dev?style=flat)](https://github.com/MakerXStudio/algorand-sandbox-dev/stargazers) - Docker Hub image for faster local development and CI/CD usage. (Archived on Jan 2, 2024)
- [Official Algod Container](https://hub.docker.com/r/algorand/algod) - Algod Docker Hub image from Algorand Inc.
- [Official Conduit Container](https://hub.docker.com/r/algorand/conduit) - Conduit Docker Hub image from Algorand Inc.


## Wallets & Asset Interaction

### Wallet Providers

> List of wallet providers for Algorand. Please note that this list is not exhaustive and is not an endorsement of any wallet provider.
> ⚠️ Given the [attacks](https://twitter.com/myalgo_/status/1632862464244162560) on MyAlgo wallet users, related sdk has been excluded from the list.

- [Pera Wallet](https://github.com/perawallet) [![GitHub stars](https://img.shields.io/github/stars/perawallet?style=flat)](https://github.com/perawallet/stargazers) - Secure, open source and community driven wallet for both mobile and desktop devices. Maintained by the team behind official Algorand Wallet.
- [Method Wallet](https://methodwallet.app/) - Algorand Wallet you'll love.
- [Defly Wallet](https://defly.app/) - Defly is an Algorand wallet with great suit of integrated DeFi features.
- [Exodus](https://www.exodus.com/) - Multi-cryptocurrency wallet with Algorand support.
- [A-Wallet](https://a-wallet.net/) - AWallet is an open source, HTML only, corporate friendly, and secure Algorand wallet.
- [Liquid Auth](https://github.com/algorandfoundation/liquid-auth) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/liquid-auth?style=flat)](https://github.com/algorandfoundation/liquid-auth/stargazers) - Self-hosted service to bind passkeys to crypto keypairs plus P2P signaling for secure peer connections.
- [Kibisis](https://github.com/kibis-is/web-extension) [![GitHub stars](https://img.shields.io/github/stars/kibis-is/web-extension?style=flat)](https://github.com/kibis-is/web-extension/stargazers) - Open source Algorand wallet web extension built in React and TypeScript.


### Wallet Development

- [use-wallet](https://github.com/txnlab/use-wallet) [![GitHub stars](https://img.shields.io/github/stars/txnlab/use-wallet?style=flat)](https://github.com/txnlab/use-wallet/stargazers) - React hooks for using Algorand compatible wallets with web applications. Developed by [txnlab](https://www.txnlab.dev/).
- [use-wallet-js](https://github.com/TxnLab/use-wallet-js) [![GitHub stars](https://img.shields.io/github/stars/TxnLab/use-wallet-js?style=flat)](https://github.com/TxnLab/use-wallet-js/stargazers) - TypeScript library for integrating Algorand wallets into decentralized applications.
- [rsagg](https://github.com/dragmz/rsagg) [![GitHub stars](https://img.shields.io/github/stars/dragmz/rsagg?style=flat)](https://github.com/dragmz/rsagg/stargazers) - A Rust library for GPU accelerated Algorand 'vanity' address generation.


### Blockchain Explorers

> List of Blockchain explorers for Algorand. Used to view transactions, accounts, assets, etc.

- [Allo](https://allo.info) - Unified Algorand explorer covering all networks by Nodely.
- [Pera Explorer](https://explorer.perawallet.app/) - Algorand Accounts, Standard Asset (ASA) explorer built by [Pera Wallet](https://perawallet.app/)
- [Algorand Ballet](https://akaalias.github.io/algorand-ballet/) - Algorand accounts' 2D graphs.
- [Algorand Multiverse](https://algo3d.live/) - Algorand accounts' 3D graphs.
- [AlgoSurf](https://algo.surf/) - Algorand Network Explorer (supports LocalNet in `localhost`).
- [Algo Explorer](https://github.com/corvid-agent/algo-explorer) [![GitHub stars](https://img.shields.io/github/stars/corvid-agent/algo-explorer?style=flat)](https://github.com/corvid-agent/algo-explorer/stargazers) - Modern Algorand Blockchain explorer with real-time transaction monitoring.


### Portfolio Trackers

> List of portfolio trackers for Algorand. Aids in tracking the value of your assets.

- [CompX](https://app.compx.io/dashboard) - Track or search assets, rewards, yield farming, transactions, and NFTs on the Algorand Blockchain anywhere and anytime. Formerly Algogator.Finance.
- [ASA Stats](https://www.asastats.com/) - One-stop portfolio tracker used to summarize Algorand asset valuations from up to five wallet addresses.


### Name Services

> A list of name services that allow for human-readable addresses.

- [NFDomains](https://nf.domains/) - Algorand name service and marketplace for Non-Fungible Domains (NFDs) — unique, readable aliases for wallet addresses.


## Infrastructure & Ecosystem Services

### Nodes & Consensus Participation

- [Algorand - The Undocumented Docs](https://github.com/AlgoChads/algorand-undoc-docs) [![GitHub stars](https://img.shields.io/github/stars/AlgoChads/algorand-undoc-docs?style=flat)](https://github.com/AlgoChads/algorand-undoc-docs/stargazers) - Dev Notes for Archival Node, Indexer Setup (and more).
- [Nodely](https://nodely.io) - Free Node/Indexer APIs, Node running FAQ, Node/Indexer daily snapshots.
- [Algorand Node UI](https://github.com/algorand/node-ui) [![GitHub stars](https://img.shields.io/github/stars/algorand/node-ui?style=flat)](https://github.com/algorand/node-ui/stargazers) - Terminal UI for remote Algorand node management.
- [nodekit](https://github.com/algorandfoundation/nodekit) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/nodekit?style=flat)](https://github.com/algorandfoundation/nodekit/stargazers) - Terminal user interface for running and managing Algorand nodes locally.
- [SubQuery](https://subquery.network) - Open, fast, flexible, and decentralised cross-chain data indexer for Algorand ([getting started guide](https://academy.subquery.network/quickstart/quickstart_chains/algorand.html)).
- [AlloCTRL](https://github.com/AlgoNode/alloctrl) [![GitHub stars](https://img.shields.io/github/stars/AlgoNode/alloctrl?style=flat)](https://github.com/AlgoNode/alloctrl/stargazers) - A simple, open source, dashboard to help managing your node and participation keys safely, from your local machine.
- [reti](https://github.com/algorandfoundation/reti) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/reti?style=flat)](https://github.com/algorandfoundation/reti/stargazers) - Contracts, Node Daemon, and UI for Algorand 'The Reti' consensus incentives, enabling decentralized staking pools to broaden participation and enhance network security.


### Blockchain Bridges

> This provides a list of bridges that allow for cross-chain transfers of assets between Algorand and other Blockchains.

- [Algomint](https://algomint.io/) - Centralized BTC and ETH bridge to Algorand.
- [Messina](https://messina.one/) - The ALGO — ETH two-way Messina.one's Bridge will open the doors for interoperability between Ethereum and ERC-20 tokens with Algorand.


### Oracles

> A list of oracle solutions that allow for smart contracts to interact with the real world.

- [Gora](https://www.gora.io/) - Decentralized oracle networks that connect the Algorand Blockchain with the real world.


### Security Auditing Services

> This section is not aimed to promote any of the companies below, please do your due diligence when researching on options available for audits. Instead, the following is simply aimed to highlight an expanding variety of companies offering smart contract audits for Algorand ecosystem.

- [Certik](https://www.certik.com/ecosystems/algorand) - Web3 security suite: smart contract audits plus analytics (Skynet, SkyTrace) for Algorand projects.
- [UlamLabs](https://www.ulam.io/software-services/smart-contract-audits) - A Blockchain lab based in Poland, offering auditing services for Algorand smart contracts.
- [Runtime Verification](https://runtimeverification.com/smartcontract) - Smart contract analysis and verification by the team who audited platforms like Algofi, FolksFinance, Yieldly and other prominent DeFi platforms in the ecosystem.
- [Immunebytes](https://www.immunebytes.com) - Secure your Algorand Smart Contract with credible security auditing solutions.
- [KudelskiSecurity](https://kudelskisecurity.com) - Move your Blockchain project securely and successfully into production or onto mainnet. Company can help you assess, design, customize, deploy and manage Blockchain and digital ledger technology systems so you can confidently leverage security as a powerful differentiator in this dynamic market.
- [algorand-ecosystem-audits](https://github.com/blockshake-io/algorand-ecosystem-audits) [![GitHub stars](https://img.shields.io/github/stars/blockshake-io/algorand-ecosystem-audits?style=flat)](https://github.com/blockshake-io/algorand-ecosystem-audits/stargazers) - A growing collection of audit reports in the Algorand ecosystem maintained by [blockshake-io](https://blockshake.io).
- [Vantage Point Blockchain](https://www.vantagepoint.sg/contact-us) - Smart contract audits, crypto wallet audit and other penetration testing services in Algorand ecosystem with clients such as Folks.Finance, Pera, Algorand Foundation, Deflex (Defly/Alammex), GARD, Venue.One and others. Reports are signed by velocity.vantagepoint.algo and published at https://github.com/vantagepointreports/releases.
- [Tenset Security](https://github.com/tenset-security/audits) [![GitHub stars](https://img.shields.io/github/stars/tenset-security/audits?style=flat)](https://github.com/tenset-security/audits/stargazers) - Comprising a team of Web3 Security Researchers, Tenset Security is dedicated to leaving no stone unturned in their pursuit of security excellence. They have a [proven track record of success](https://twitter.com/algoworld_nft/status/1691891473166279042) in discovering high-severity vulnerabilities specifically within Algorand projects, emphasizing their expertise and commitment to the Algorand ecosystem.


### Metrics and Analytics Services

> Metrics and analytics services for Algorand.

- [Algorand MainNet metrics](https://metrics.algorand.org/) - Dashboard that measures the current scale, security, decentralization, and adoption of the open-source Algorand protocol.
- [Metrika](https://app.metrika.co/dashboard/algorand/) - Algorand network performance and account monitor.
- [Allo Metrics](https://metrics.allo.info/) - Algorand MainNet in numbers.

## SSI, DID and Verifiable Credentials

> A list of W3C decentralized identifiers, verifiable credentials and Self sovereign identity service projects.

- [GoPlausible](https://goplausible.com) - Provides [PLAUSIBLE protocol](https://github.com/GoPlausible) [![GitHub stars](https://img.shields.io/github/stars/GoPlausible?style=flat)](https://github.com/GoPlausible/stargazers), A W3C DIDs, Verifiable Credentials and Utility NFTs protocol built on Algorand, as well as [ThisDID](https://thisdid.com) Universal W3C DID/URI resolver.


## AI and Machine Learning

> A list of AI, ML and Data Science projects that leverage Algorand.

- [Algorand-GPT](https://chatgpt.com/g/g-izA6hnC93-algorand-gpt) - An Algorand Assistant Expert with access to all Algorand documentation and chain data built on OpenAI's ChatGPT platform by GoPlausible.
- [DID-GPT](https://chatgpt.com/g/g-rOCQculZQ-did-gpt) - A W3C DID resolver assistant built on OpenAI's ChatGPT platform by GoPlausible.
- [algorand-mcp](https://github.com/GoPlausible/algorand-mcp) [![GitHub stars](https://img.shields.io/github/stars/GoPlausible/algorand-mcp?style=flat)](https://github.com/GoPlausible/algorand-mcp/stargazers) - Algorand Model Context Protocol (Server & Client) by GoPlausible.
- [algorand-remote-mcp](https://github.com/GoPlausible/algorand-remote-mcp) [![GitHub stars](https://img.shields.io/github/stars/GoPlausible/algorand-remote-mcp?style=flat)](https://github.com/GoPlausible/algorand-remote-mcp/stargazers) - Algorand remote SSE MCP Server Cloudflare Worker.
- [arcontextify](https://github.com/aorumbayev/arcontextify) [![GitHub stars](https://img.shields.io/github/stars/aorumbayev/arcontextify?style=flat)](https://github.com/aorumbayev/arcontextify/stargazers) - Algorand ARC-56 to MCP server converter.
- [VibeKit](https://github.com/gabrielkuettel/vibekit) [![GitHub stars](https://img.shields.io/github/stars/gabrielkuettel/vibekit?style=flat)](https://github.com/gabrielkuettel/vibekit/stargazers) - CLI + MCP server that gives AI coding assistants the skills and tools to build on Algorand.
- [corvid-agent](https://github.com/corvid-agent/corvid-agent) [![GitHub stars](https://img.shields.io/github/stars/corvid-agent/corvid-agent?style=flat)](https://github.com/corvid-agent/corvid-agent/stargazers) - An autonomous AI agent platform built on Algorand with encrypted on-chain messaging.
- [AlgoChat](https://github.com/corvid-agent/corvid-agent-chat) [![GitHub stars](https://img.shields.io/github/stars/corvid-agent/corvid-agent-chat?style=flat)](https://github.com/corvid-agent/corvid-agent-chat/stargazers) - Encrypted peer-to-peer chat client using Algorand transactions and PSK ratcheting.
- [algorand-agent-skills](https://github.com/algorand-devrel/algorand-agent-skills) [![GitHub stars](https://img.shields.io/github/stars/algorand-devrel/algorand-agent-skills?style=flat)](https://github.com/algorand-devrel/algorand-agent-skills/stargazers) - Canonical collection of Agent Skills for AI-assisted development on Algorand by Algorand DevRel.


## Application Platforms & Examples

### DeFi Platforms

> Awesome DeFi platforms and protocols on Algorand. Please note that this list is not aimed to promote any specific project, but rather to provide a comprehensive overview of the ecosystem. Do your own research before investing or using any of the projects listed here.

- [Tinyman](https://tinyman.org/) - A decentralized trading protocol, AMM and platform.
- [Pact](https://www.pact.fi/) - Decentralised Automated Market Maker (AMM) built on the Algorand protocol.
- [Lofty.ai](https://www.lofty.ai/) - Tokenized real estate investing platform.
- [Folks.finance](https://folks.finance/) - Decentralized capital markets protocol.
- [Cometa.farm](https://cometa.farm/) - Decentralized liquidity-as-a-service.
- [aramid.finance](https://www.aramid.finance/) - A Decentralized Cross-Chain Protocol supporitng Algorand, Polygon, Ethereum and other EVM chains.
- [stabilitas.finance](https://stabilitas.finance/) - Stable and secure digital assets for various purposes such as purchases, remittances and as a store of value.
- [vestige.fi](https://vestige.fi/) - A decentralized ecosystem of tools primary used as a tool to track and trend Algorand Standard Assets and Liquidity Pools across the ecosystem. The platform also provides a decentralized swap and a launchpad platform.
- [folks-router](https://github.com/Folks-Finance/folks-router) [![GitHub stars](https://img.shields.io/github/stars/Folks-Finance/folks-router?style=flat)](https://github.com/Folks-Finance/folks-router/stargazers) - Efficient swap routing SDK on Algorand by Folks Finance.
- [Folks-Finance/algorand-js-sdk](https://github.com/Folks-Finance/folks-finance-js-sdk) [![GitHub stars](https://img.shields.io/github/stars/Folks-Finance/folks-finance-js-sdk?style=flat)](https://github.com/Folks-Finance/folks-finance-js-sdk/stargazers) - Official Folks Finance Algorand Protocol SDK.
- [DorkFi](https://dork.fi/) - Cross-chain borrow/lend protocol on Algorand and Voi Network. Features overcollateralized lending, WAD stablecoin minting, and UNIT governance token.


### NFT Marketplaces

> Awesome NFT marketplaces and galleries on Algorand.

- [Rand Gallery](https://www.randgallery.com/) - Algorand Standard Asset (ASA) explorer and marketplace developed by [Chris Antaki](https://github.com/ChrisAntaki) [![GitHub stars](https://img.shields.io/github/stars/ChrisAntaki?style=flat)](https://github.com/ChrisAntaki/stargazers).
- [AlgoGems](https://algogems.io/) - Algorand Standard Asset (ASA) markeplace and trading platform for NFT collectors.
- [AlgoMart](https://github.com/deptagency/algomart) [![GitHub stars](https://img.shields.io/github/stars/deptagency/algomart?style=flat)](https://github.com/deptagency/algomart/stargazers) - Opensource NFT marketplace whitelabel solution.
- [Flatter](https://www.flatternft.com/) - NFT art and collectible marketplace.
- [NFT Gallery](https://github.com/corvid-agent/nft-gallery) [![GitHub stars](https://img.shields.io/github/stars/corvid-agent/nft-gallery?style=flat)](https://github.com/corvid-agent/nft-gallery/stargazers) - Algorand NFT gallery browser with ARC-standard support.

### Prediction Markets

> Awesome prediction markets and trading platforms on Algorand.

- [Alpha Arcade](https://www.alphaarcade.com/) - Prediction market platform on Algorand.

### Subscription Management

> Awesome subscription management platforms on Algorand. Please note that this list is not aimed to promote any specific project, but rather to provide a comprehensive overview of the ecosystem. Do your own research before investing or using any of the projects listed here.

- [Subtopia](https://subtopia.io/) - Decentralized subscription management platform for dApp creators and platform on Algorand. Manage and own your subscription infrastructure, setup flexible plans, discounts and get paid in Algo or any ASA token. Created by @aorumbayev.


### Decentralized voting

> Tools for on-chain voting powered by Algorand

- [nft_voting_tool](https://github.com/algorandfoundation/nft_voting_tool) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/nft_voting_tool?style=flat)](https://github.com/algorandfoundation/nft_voting_tool/stargazers) - Official voting tool by Algorand Foundation. The repository contains a voting tool that allows for creation and facilitation of immutable, tamperproof voting using the Algorand Blockchain.


## Standards

### Algorand Request for Comments

> Standards and specs defined in _finalized_ ARCs.
> The list of all the ARCs can be found [here](https://arc.algorand.foundation).

- [ARC3](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0003.md) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/ARCs/blob/main/ARCs/arc-0003.md?style=flat)](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0003.md/stargazers) - Official Algorand Standard Asset Parameters Conventions for Fungible and Non-Fungible Tokens.
- [ARC4](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0004.md) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/ARCs/blob/main/ARCs/arc-0004.md?style=flat)](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0004.md/stargazers) - Application Binary Interface.
- [ARC32](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0032.md) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/ARCs/blob/main/ARCs/arc-0032.md?style=flat)](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0032.md/stargazers) - Application Specification.
- [ARC56](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0056.md) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/ARCs/blob/main/ARCs/arc-0056.md?style=flat)](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0056.md/stargazers) - Extended and improved Application Specification.
- [ARC69](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0069.md) [![GitHub stars](https://img.shields.io/github/stars/algorandfoundation/ARCs/blob/main/ARCs/arc-0069.md?style=flat)](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0069.md/stargazers) - One of several Algorand Standard Asset Parameters Conventions.


## Contributing

Contributions welcome! Read the [contribution guidelines](https://github.com/awesome-algorand/awesome-algorand/blob/main/contributing.md) [![GitHub stars](https://img.shields.io/github/stars/awesome-algorand/awesome-algorand/blob/main/contributing.md?style=flat)](https://github.com/awesome-algorand/awesome-algorand/blob/main/contributing.md/stargazers) first.

Special thanks to everyone who forked or starred the repository ❤️
