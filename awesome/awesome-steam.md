# Steam

[![GitHub stars](https://img.shields.io/github/stars/scholtzm/awesome-steam?style=flat)](https://github.com/scholtzm/awesome-steam/stargazers)

# Awesome Steam [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of [packages](#packages) and [resources](#resources) regarding [Steam](http://store.steampowered.com/) development.

*Please read the [contribution guidelines](CONTRIBUTING.md) before contributing.*

The purpose of this document is to provide a quick overview over existing packages (libraries, modules etc.) and resources available regarding Steam client automation and WebAPI usage. Whenever you need to start a new project, have a look at the list of packages and see if there is anything useful for your use case. If you need technical details or tutorials, check out the resources section.

## Table of Contents

- [Packages](#packages)
  - [Node.js](#nodejs)
  - [C#](#c)
  - [PHP](#php)
  - [Go](#go)
  - [Python](#python)
  - [C++](#c-1)
  - [Java](#java)
  - [Objective-C](#objective-c)
  - [Ruby](#ruby)
  - [Rust](#rust)

- [Resources](#resources)
  - [General](#general-3)
  - [Tutorials](#tutorials)
  - [Posts](#posts)
  - [Standalone Tools](#standalone-tools)
  - [Discussion Boards](#discussion-boards)
  - [Third-Party Services](#third-party-services)

## Packages

> 💡 Many of these package repositories provide helpful READMEs and wiki pages, which explain the usage and/or provide examples. Do not forget to check them out when using particular package.

### Node.js

#### General

- [steam](https://github.com/seishun/node-steam) [![GitHub stars](https://img.shields.io/github/stars/seishun/node-steam?style=flat)](https://github.com/seishun/node-steam/stargazers) - Interface directly with Steam servers from Node.js.
- [steam-client](https://github.com/DoctorMcKay/node-steam-client) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-client?style=flat)](https://github.com/DoctorMcKay/node-steam-client/stargazers) - API-compatible fork of node-steam's SteamClient.
- [steam-user](https://github.com/DoctorMcKay/node-steam-user) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-user?style=flat)](https://github.com/DoctorMcKay/node-steam-user/stargazers) - Feature-rich easy-to-use Steam client.
- [vapor](https://github.com/scholtzm/vapor) [![GitHub stars](https://img.shields.io/github/stars/scholtzm/vapor?style=flat)](https://github.com/scholtzm/vapor/stargazers) - Lightweight Steam client framework.
- [steam-parentbot](https://github.com/dragonbanshee/node-steam-parentbot) [![GitHub stars](https://img.shields.io/github/stars/dragonbanshee/node-steam-parentbot?style=flat)](https://github.com/dragonbanshee/node-steam-parentbot/stargazers) - Simple base class for a Steam bot.
- [steamworks-ffi-node](https://github.com/ArtyProf/steamworks-ffi-node) [![GitHub stars](https://img.shields.io/github/stars/ArtyProf/steamworks-ffi-node?style=flat)](https://github.com/ArtyProf/steamworks-ffi-node/stargazers) - A Node.js wrapper for Steamworks SDK.

#### WebAPI

- [steam-webapi](https://github.com/DoctorMcKay/node-steam-webapi) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-webapi?style=flat)](https://github.com/DoctorMcKay/node-steam-webapi/stargazers) - Complete WebAPI wrapper with support for extra HTTP headers sent by Steam.
- [steamapi](https://github.com/lloti/node-steamapi) [![GitHub stars](https://img.shields.io/github/stars/lloti/node-steamapi?style=flat)](https://github.com/lloti/node-steamapi/stargazers) - A nice Steam API wrapper.

#### Trading

- [steam-trade](https://github.com/seishun/node-steam-trade) [![GitHub stars](https://img.shields.io/github/stars/seishun/node-steam-trade?style=flat)](https://github.com/seishun/node-steam-trade/stargazers) - Node.js wrapper around Steam live trading.
- [steam-tradeoffers](https://github.com/Alex7Kom/node-steam-tradeoffers) [![GitHub stars](https://img.shields.io/github/stars/Alex7Kom/node-steam-tradeoffers?style=flat)](https://github.com/Alex7Kom/node-steam-tradeoffers/stargazers) - Steam Trade Offers for Node.js.
- [steam-tradeoffer-manager](https://github.com/DoctorMcKay/node-steam-tradeoffer-manager) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-tradeoffer-manager?style=flat)](https://github.com/DoctorMcKay/node-steam-tradeoffer-manager/stargazers) - Simple and sane Steam trade offer management.
- [steam-inventory-stream](https://github.com/timvandam/steam-inventory-stream) [![GitHub stars](https://img.shields.io/github/stars/timvandam/steam-inventory-stream?style=flat)](https://github.com/timvandam/steam-inventory-stream/stargazers) - Fetch inventories as readable streams.
- [steam-inventory-api-ng](https://github.com/itsjfx/node-steam-inventory-api-ng) [![GitHub stars](https://img.shields.io/github/stars/itsjfx/node-steam-inventory-api-ng?style=flat)](https://github.com/itsjfx/node-steam-inventory-api-ng/stargazers) - A Steam Inventory API wrapper with advanced features such as retries and proxy support.

#### Game Interaction

- [steam-gameserver](https://github.com/DoctorMcKay/node-steam-gameserver) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-gameserver?style=flat)](https://github.com/DoctorMcKay/node-steam-gameserver/stargazers) - Steam client handler for Gameserver and AnonGameserver account types.
- [tf2](https://github.com/DoctorMcKay/node-tf2) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-tf2?style=flat)](https://github.com/DoctorMcKay/node-tf2/stargazers) - Interact directly with TF2 game coordinator.
- [csgo](https://github.com/joshuaferrara/node-csgo) [![GitHub stars](https://img.shields.io/github/stars/joshuaferrara/node-csgo?style=flat)](https://github.com/joshuaferrara/node-csgo/stargazers) - Interact directly with CS:GO game coordinator.
- [dota2](https://github.com/RJacksonm1/node-dota2) [![GitHub stars](https://img.shields.io/github/stars/RJacksonm1/node-dota2?style=flat)](https://github.com/RJacksonm1/node-dota2/stargazers) - Interact directly with Dota 2 game coordinator.

#### Community & Store Automation

- [steamcommunity](https://github.com/DoctorMcKay/node-steamcommunity) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steamcommunity?style=flat)](https://github.com/DoctorMcKay/node-steamcommunity/stargazers) - Interact with steamcommunity.com. Also allows to confirm trade offers.
- [steamstore](https://github.com/DoctorMcKay/node-steamstore) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steamstore?style=flat)](https://github.com/DoctorMcKay/node-steamstore/stargazers) - Interact with store.steampowered.com.
- [steam-weblogon](https://github.com/Alex7Kom/node-steam-weblogon) [![GitHub stars](https://img.shields.io/github/stars/Alex7Kom/node-steam-weblogon?style=flat)](https://github.com/Alex7Kom/node-steam-weblogon/stargazers) - Retrieve SteamCommunity cookies if you are running Steam network client.
- [steam-web-api-key](https://github.com/Alex7Kom/node-steam-web-api-key) [![GitHub stars](https://img.shields.io/github/stars/Alex7Kom/node-steam-web-api-key?style=flat)](https://github.com/Alex7Kom/node-steam-web-api-key/stargazers) - Automatically registers and retrieves Steam API key.
- [steam-parental](https://github.com/Alex7Kom/node-steam-parental) [![GitHub stars](https://img.shields.io/github/stars/Alex7Kom/node-steam-parental?style=flat)](https://github.com/Alex7Kom/node-steam-parental/stargazers) - Disable parental lock.

#### Authentication

- [steam-login](https://github.com/cpancake/steam-login) [![GitHub stars](https://img.shields.io/github/stars/cpancake/steam-login?style=flat)](https://github.com/cpancake/steam-login/stargazers) - Simple Connect / Express Steam authentication library.
- [passport-steam](https://github.com/liamcurry/passport-steam) [![GitHub stars](https://img.shields.io/github/stars/liamcurry/passport-steam?style=flat)](https://github.com/liamcurry/passport-steam/stargazers) - Steam (OpenID) authentication strategy for Passport and Node.js.
- [meteor-accounts-steam](https://github.com/scholtzm/meteor-accounts-steam) [![GitHub stars](https://img.shields.io/github/stars/scholtzm/meteor-accounts-steam?style=flat)](https://github.com/scholtzm/meteor-accounts-steam/stargazers) - Steam OpenID integration for Meteor Accounts.

#### Misc

- [steam-resources](https://github.com/seishun/node-steam-resources) [![GitHub stars](https://img.shields.io/github/stars/seishun/node-steam-resources?style=flat)](https://github.com/seishun/node-steam-resources/stargazers) - Steam's enums, protobufs and structs.
- [steam-crypto](https://github.com/seishun/node-steam-crypto) [![GitHub stars](https://img.shields.io/github/stars/seishun/node-steam-crypto?style=flat)](https://github.com/seishun/node-steam-crypto/stargazers) - Node.js implementation of Steam crypto.
- [steam-groups](https://github.com/scholtzm/node-steam-groups) [![GitHub stars](https://img.shields.io/github/stars/scholtzm/node-steam-groups?style=flat)](https://github.com/scholtzm/node-steam-groups/stargazers) - Custom node-steam handler which provides group functions.
- [steamid](https://github.com/DoctorMcKay/node-steamid) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steamid?style=flat)](https://github.com/DoctorMcKay/node-steamid/stargazers) - SteamID usage and conversion made easy.
- [steam-totp](https://github.com/DoctorMcKay/node-steam-totp) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-totp?style=flat)](https://github.com/DoctorMcKay/node-steam-totp/stargazers) - Easily generate 2FA codes used by Steam.
- [steam-chat-bot](https://github.com/Steam-Chat-Bot/node-steam-chat-bot) [![GitHub stars](https://img.shields.io/github/stars/Steam-Chat-Bot/node-steam-chat-bot?style=flat)](https://github.com/Steam-Chat-Bot/node-steam-chat-bot/stargazers) - Simplified interface for a steam chat bot.
- [vdf](https://github.com/RJacksonm1/node-vdf) [![GitHub stars](https://img.shields.io/github/stars/RJacksonm1/node-vdf?style=flat)](https://github.com/RJacksonm1/node-vdf/stargazers) - vdf to object and vice versa.
- [steamrep](https://github.com/scholtzm/node-steamrep) [![GitHub stars](https://img.shields.io/github/stars/scholtzm/node-steamrep?style=flat)](https://github.com/scholtzm/node-steamrep/stargazers) - Check user's SteamRep reputation.
- [reptf](https://github.com/scholtzm/node-reptf) [![GitHub stars](https://img.shields.io/github/stars/scholtzm/node-reptf?style=flat)](https://github.com/scholtzm/node-reptf/stargazers) - Check user's rep.tf reputation.
- [steamapis](https://github.com/itsjfx/node-steamapis) [![GitHub stars](https://img.shields.io/github/stars/itsjfx/node-steamapis?style=flat)](https://github.com/itsjfx/node-steamapis/stargazers) - Module to use the API of [steamapis.com](https://steamapis.com).

### C&#35;

#### General

- [SteamKit2](https://github.com/SteamRE/SteamKit) [![GitHub stars](https://img.shields.io/github/stars/SteamRE/SteamKit?style=flat)](https://github.com/SteamRE/SteamKit/stargazers) - .NET library designed to interoperate with Valve's Steam network.
- [SteamAuth](https://github.com/geel9/SteamAuth) [![GitHub stars](https://img.shields.io/github/stars/geel9/SteamAuth?style=flat)](https://github.com/geel9/SteamAuth/stargazers) - A C# library that provides vital Steam Mobile Authenticator functionality.
- [SteamBot](https://github.com/Jessecar96/SteamBot) [![GitHub stars](https://img.shields.io/github/stars/Jessecar96/SteamBot?style=flat)](https://github.com/Jessecar96/SteamBot/stargazers) - Automated bot software for interacting with steam trade.
- [SteamTradeOffersBot](https://github.com/waylaidwanderer/SteamTradeOffersBot) [![GitHub stars](https://img.shields.io/github/stars/waylaidwanderer/SteamTradeOffersBot?style=flat)](https://github.com/waylaidwanderer/SteamTradeOffersBot/stargazers) - SteamBot fork which focuses on trade offers.
- [SteamStandardProject](https://github.com/ObsidianMinor/SteamStandardProject) [![GitHub stars](https://img.shields.io/github/stars/ObsidianMinor/SteamStandardProject?style=flat)](https://github.com/ObsidianMinor/SteamStandardProject/stargazers) - A collection of .NET Standard libraries using common types that provide functionality in one or more parts of Steam.

#### Misc

- [BackpackLogin](https://github.com/igeligel/BackpackLogin) [![GitHub stars](https://img.shields.io/github/stars/igeligel/BackpackLogin?style=flat)](https://github.com/igeligel/BackpackLogin/stargazers) - A .NET Standard library for logging into backpack.tf using Steam credentials.
- [TeamFortressOutpostApi](https://github.com/igeligel/TeamFortressOutpostApi) [![GitHub stars](https://img.shields.io/github/stars/igeligel/TeamFortressOutpostApi?style=flat)](https://github.com/igeligel/TeamFortressOutpostApi/stargazers) - A .NET Standard class library which allows user to interact with TF2Outpost.

### PHP

- [SteamCommunity](https://github.com/waylaidwanderer/PHP-SteamCommunity) [![GitHub stars](https://img.shields.io/github/stars/waylaidwanderer/PHP-SteamCommunity?style=flat)](https://github.com/waylaidwanderer/PHP-SteamCommunity/stargazers) - A PHP library for interacting with the Steam Community website.
- [SteamAuthentication](https://github.com/SmItH197/SteamAuthentication) [![GitHub stars](https://img.shields.io/github/stars/SmItH197/SteamAuthentication?style=flat)](https://github.com/SmItH197/SteamAuthentication/stargazers) - Steam OpenID authentication with PHP.
- [SteamAuthOOP](https://github.com/BlackCetha/SteamAuthOOP) [![GitHub stars](https://img.shields.io/github/stars/BlackCetha/SteamAuthOOP?style=flat)](https://github.com/BlackCetha/SteamAuthOOP/stargazers) - An object-oriented alternative to SteamAuthentication.
- [steam-api](https://github.com/DaMitchell/steam-api-php) [![GitHub stars](https://img.shields.io/github/stars/DaMitchell/steam-api-php?style=flat)](https://github.com/DaMitchell/steam-api-php/stargazers) - A PHP wrapper for the Steam API.
- [steamid](https://github.com/DoctorMcKay/php-steamid) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/php-steamid?style=flat)](https://github.com/DoctorMcKay/php-steamid/stargazers) - SteamID class for PHP.
- [steam-totp](https://github.com/DoctorMcKay/php-steam-totp) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/php-steam-totp?style=flat)](https://github.com/DoctorMcKay/php-steam-totp/stargazers) - PHP library to deal with Steam's proprietary TOTP algorithm.
- [steam-auth](https://github.com/vikas5914/steam-auth) [![GitHub stars](https://img.shields.io/github/stars/vikas5914/steam-auth?style=flat)](https://github.com/vikas5914/steam-auth/stargazers) - An alternative Steam authentication library with Composer support.

### Go

- [steam](https://github.com/0xAozora/steam) [![GitHub stars](https://img.shields.io/github/stars/0xAozora/steam?style=flat)](https://github.com/0xAozora/steam/stargazers) - Simple steam library for trading in Go.
- [go-steam](https://github.com/Philipp15b/go-steam) [![GitHub stars](https://img.shields.io/github/stars/Philipp15b/go-steam?style=flat)](https://github.com/Philipp15b/go-steam/stargazers) - Steam's protocol in Go.
- [steam-mobileauth](https://github.com/YellowOrWhite/go-steam-mobileauth) [![GitHub stars](https://img.shields.io/github/stars/YellowOrWhite/go-steam-mobileauth?style=flat)](https://github.com/YellowOrWhite/go-steam-mobileauth/stargazers) - Port of SteamAuth in Go.

### Python

#### General

- [steam](https://github.com/ValvePython/steam) [![GitHub stars](https://img.shields.io/github/stars/ValvePython/steam?style=flat)](https://github.com/ValvePython/steam/stargazers) - Module for various interactions with Steam.
- [steamodd](https://github.com/Lagg/steamodd) [![GitHub stars](https://img.shields.io/github/stars/Lagg/steamodd?style=flat)](https://github.com/Lagg/steamodd/stargazers) - Steam tools library.
- [steampy](https://github.com/bukson/steampy) [![GitHub stars](https://img.shields.io/github/stars/bukson/steampy?style=flat)](https://github.com/bukson/steampy/stargazers) - Fully automated Steam trade offers library with SteamGuard support.
- [SteamAPI](https://github.com/smiley/steamapi) [![GitHub stars](https://img.shields.io/github/stars/smiley/steamapi?style=flat)](https://github.com/smiley/steamapi/stargazers) - An object-oriented Python 2.7+ library for accessing the Steam Web API.
- [Steam-Trade](https://github.com/Zwork101/steam-trade) [![GitHub stars](https://img.shields.io/github/stars/Zwork101/steam-trade?style=flat)](https://github.com/Zwork101/steam-trade/stargazers) - An asynchronous, event-based trade library.
- [aiosteampy](https://github.com/somespecialone/aiosteampy) [![GitHub stars](https://img.shields.io/github/stars/somespecialone/aiosteampy?style=flat)](https://github.com/somespecialone/aiosteampy/stargazers) - Trade and interact with Steam market, WebAPI, SteamGuard.

#### Game Interaction

- [csgo](https://github.com/ValvePython/csgo) [![GitHub stars](https://img.shields.io/github/stars/ValvePython/csgo?style=flat)](https://github.com/ValvePython/csgo/stargazers) - Python module for interacting with CSGO's Game Coordinator.
- [dota2](https://github.com/ValvePython/dota2) [![GitHub stars](https://img.shields.io/github/stars/ValvePython/dota2?style=flat)](https://github.com/ValvePython/dota2/stargazers) - Python module for interacting with Dota 2's Game Coordinator.

#### Misc

- [vpk](https://github.com/ValvePython/vpk) [![GitHub stars](https://img.shields.io/github/stars/ValvePython/vpk?style=flat)](https://github.com/ValvePython/vpk/stargazers) - Python module for working with Valve's Pack format.
- [vdf](https://github.com/ValvePython/vdf) [![GitHub stars](https://img.shields.io/github/stars/ValvePython/vdf?style=flat)](https://github.com/ValvePython/vdf/stargazers) - Python module for working with Valve's KeyValue format.

### C++

- [SteamPP](https://github.com/seishun/SteamPP) [![GitHub stars](https://img.shields.io/github/stars/seishun/SteamPP?style=flat)](https://github.com/seishun/SteamPP/stargazers) - C++ library to interoperate with Steam servers.

### Java

- [SteamKit-Java](https://github.com/Top-Cat/SteamKit-Java) [![GitHub stars](https://img.shields.io/github/stars/Top-Cat/SteamKit-Java?style=flat)](https://github.com/Top-Cat/SteamKit-Java/stargazers) - Java port of SteamKit.
- [JavaSteam](https://github.com/Longi94/JavaSteam) [![GitHub stars](https://img.shields.io/github/stars/Longi94/JavaSteam?style=flat)](https://github.com/Longi94/JavaSteam/stargazers) - Java library that provides an interface to directly interact with Valve's Steam servers.

### Objective-C

- [SteamAuth](https://github.com/michaelchum/SteamAuth) [![GitHub stars](https://img.shields.io/github/stars/michaelchum/SteamAuth?style=flat)](https://github.com/michaelchum/SteamAuth/stargazers) - An iOS wrapper around Steam's OpenID login.

### Ruby

- [steam-trade](https://github.com/OmG3r/steam-trade) [![GitHub stars](https://img.shields.io/github/stars/OmG3r/steam-trade?style=flat)](https://github.com/OmG3r/steam-trade/stargazers) - Ruby gem for sending trade offers.

### Rust

- [steamguard-cli](https://github.com/dyc3/steamguard-cli) [![GitHub stars](https://img.shields.io/github/stars/dyc3/steamguard-cli?style=flat)](https://github.com/dyc3/steamguard-cli/stargazers) - Command-line utility for generating Steam 2FA codes and managing Steam confirmations.

## Resources

### General

- [Steam WebAPI @ ValveSoftware](https://developer.valvesoftware.com/wiki/Steam_Web_API)
- [Steam WebAPI @ TF2 Wiki](https://wiki.teamfortress.com/wiki/WebAPI)
- [Steam WebAPI Documentation by xPaw](https://lab.xpaw.me/steam_api_documentation.html)
- [Steam Internal WebAPI Documentation by Revadike](https://github.com/Revadike/UnofficialSteamWebAPI) [![GitHub stars](https://img.shields.io/github/stars/Revadike/UnofficialSteamWebAPI?style=flat)](https://github.com/Revadike/UnofficialSteamWebAPI/stargazers)
- [Steam as OpenID Provider](http://steamcommunity.com/dev)
- [Steam API Key Registration](http://steamcommunity.com/dev/apikey)
- [Steam Error Codes](https://steamerrors.com/) - List of `EResult` codes with possible explanations.

### Tutorials

- [Creating a Steam Trade Bot with Node.js](https://firepowered.org/developer/create-a-steam-trade-bot-with-nodejs-iojs-updated-for-node-steam-v1-0/)
- [Charred's node.js Guide to Steam Bots](https://github.com/charredgrass/nodejs-bot-guide) [![GitHub stars](https://img.shields.io/github/stars/charredgrass/nodejs-bot-guide?style=flat)](https://github.com/charredgrass/nodejs-bot-guide/stargazers)
- [In-depth Steam Bot Guide with Node.js](https://github.com/andrewda/node-steam-guide) [![GitHub stars](https://img.shields.io/github/stars/andrewda/node-steam-guide?style=flat)](https://github.com/andrewda/node-steam-guide/stargazers)
- [Retrieving 2FA Keys from iOS Device](http://forums.backpack.tf/index.php?/topic/45995-guide-how-to-get-your-shared-secret-from-ios-device-steam-mobile/)

### Posts

- [Item IDs Explained](https://dev.doctormckay.com/topic/332-identifying-steam-items/)
- [Everything Related to Escrow](https://www.reddit.com/r/SteamBot/comments/3udhkd/everything_related_to_escrow/)
- [Understanding Avatar Hash](https://www.reddit.com/r/SteamBot/comments/3cv6k7/problem_downloading_an_avatar_using/)

### Standalone Tools

- [NetHook2](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHook2) [![GitHub stars](https://img.shields.io/github/stars/SteamRE/SteamKit/tree/master/Resources/NetHook2?style=flat)](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHook2/stargazers) - Intercept Steam client's network messages.
- [NetHook2 Analyzer](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHookAnalyzer2) [![GitHub stars](https://img.shields.io/github/stars/SteamRE/SteamKit/tree/master/Resources/NetHookAnalyzer2?style=flat)](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHookAnalyzer2/stargazers) - Inspect messages dumped by NetHook2.
- [steam-auth-web-util](http://scholtzm.github.io/steam-auth-web-util/) - Generate 2FA codes directly in your web browser.
- [SteamDesktopAuthenticator](https://github.com/Jessecar96/SteamDesktopAuthenticator) [![GitHub stars](https://img.shields.io/github/stars/Jessecar96/SteamDesktopAuthenticator?style=flat)](https://github.com/Jessecar96/SteamDesktopAuthenticator/stargazers) - Desktop implementation of Steam's mobile authenticator app.
- [protonenv](https://github.com/rizkiarm/protonenv) [![GitHub stars](https://img.shields.io/github/stars/rizkiarm/protonenv?style=flat)](https://github.com/rizkiarm/protonenv/stargazers) - Simple Proton version and prefix management.
- [steam-desktop-authenticator-multiplatform](https://github.com/tre3p/steam-desktop-authenticator-multiplatform) [![GitHub stars](https://img.shields.io/github/stars/tre3p/steam-desktop-authenticator-multiplatform?style=flat)](https://github.com/tre3p/steam-desktop-authenticator-multiplatform/stargazers) - Steam desktop authenticator.

### Discussion Boards

- [/r/SteamBot](https://www.reddit.com/r/SteamBot)
- [/r/SteamBot Discord](https://discord.gg/0i5X3oDHJbDUsiGC)
- [/r/nodesteam](https://www.reddit.com/r/nodesteam)
- [DoctorMcKay's Dev Forum](https://dev.doctormckay.com/)
- [node-steam-forum](https://github.com/steam-forward/node-steam-forum) [![GitHub stars](https://img.shields.io/github/stars/steam-forward/node-steam-forum?style=flat)](https://github.com/steam-forward/node-steam-forum/stargazers)

### Third-Party Services

Websites listed below may provide free and/or paid services and are listed alphabetically according to their domain name.

- [backpack.tf](https://backpack.tf/developer) - Provides TF2 prices and Steam market/inventory related services.
- [steamanalyst.com](https://steamanalyst.com/) - Provides CS:GO prices.
- [hexa.one](https://hexa.one/) - Provides prices for several games and Steam market/inventory related services.
- [steamapis.com](https://steamapis.com/) - Provides prices for several games and Steam market/inventory related services.

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the author and contributors of this text have waived all copyright and related or neighboring rights to this work.
