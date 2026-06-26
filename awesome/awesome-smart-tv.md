# Smart TV

[![GitHub stars](https://img.shields.io/github/stars/vitalets/awesome-smart-tv?style=flat)](https://github.com/vitalets/awesome-smart-tv/stargazers)

# Awesome Smart TV [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of awesome resources for building Smart TV apps

<a href="https://github.com/vitalets/awesome-smart-tv"><img align="right" width="150" src="https://user-images.githubusercontent.com/1473072/27913047-7c3a5e60-6267-11e7-8bd1-bef2bf3cd753.png"/></a>

[Smart TV](https://en.wikipedia.org/wiki/Smart_TV) is a growing platform of TVs having access to the internet and allowing to browse web-sites and install applications. It has own ecosystem with main players like Samsung, LG, Android TV and Apple TV. In this list you will find official and third-party resources for developing Smart TV apps and communicating with TV from remote devices.

## Contents
* [Platforms](#platforms)
  * [Samsung Tizen](#samsung-tizen)
  * [LG webOS](#lg-webos)
  * [Android TV](#android-tv)
  * [Apple tvOS](#apple-tvos)
  * [Google Chromecast](#google-chromecast)
* [Cross-platform frameworks](#cross-platform-frameworks)
* [Remote control protocols](#remote-control-protocols)
* [Cross-platform tools](#cross-platform-tools)
* [Navigation libraries](#navigation-libraries)
* [Testing](#testing)
* [Misc](#misc)
* [Community](#community)

## Platforms
Below are the most popular platforms for Smart TV. The full list is [here](https://en.wikipedia.org/wiki/List_of_smart_TV_platforms_and_middleware_software).

### Samsung Tizen
#### Official resources
* [Samsung TV Developers site](http://developer.samsung.com/tv) - News, documentation and SDK downloads.
* [Tizen TV Developers site](https://developer.tizen.org/tizen/tv) - Full API documentation and guides for developing Tizen TV apps.
* [Tizen Studio](https://developer.tizen.org/development/tizen-studio/download) - IDE for TV apps development including Tizen TV Emulator.
* [Smart View SDK](http://developer.samsung.com/tv/develop/extension-libraries/smart-view-sdk/download/) - Official Android, IOS and JavaScript SDK for communication between remote device and Samsung Smart TV.
* [Samsung TV Developers Forum](http://developer.samsung.com/forum/?topCtgy=06) - Ask questions and share tips when developing apps with Samsung SDKs.
* [Samsung Smart TV Bug Bounty](https://samsungtvbounty.com) - If you find bug in Samsung TV, submit it here and get a reward $1000+.
* [vscode-extension-tizentv](https://marketplace.visualstudio.com/items?itemName=tizensdk.tizentv) - A Visual Studio Code extension that provides a lightweight IDE for Tizen application developers.
* [Wits](https://github.com/Samsung/Wits) [![GitHub stars](https://img.shields.io/github/stars/Samsung/Wits?style=flat)](https://github.com/Samsung/Wits/stargazers) - A tool for reloading tv app's JavaScript/CSS without reinstalling the app every time you make a change.

#### Third-party remote control libraries
* [samsungctl](https://github.com/Ape/samsungctl) [![GitHub stars](https://img.shields.io/github/stars/Ape/samsungctl?style=flat)](https://github.com/Ape/samsungctl/stargazers) - Library and command line tool for remote controlling Samsung televisions via a TCP/IP connection. It currently supports both pre-2016 TVs as well most of the modern Tizen-OS TVs with Ethernet or Wi-Fi connectivity (Python).
* [samsung-tv-remote](https://github.com/Badisi/samsung-tv-remote) [![GitHub stars](https://img.shields.io/github/stars/Badisi/samsung-tv-remote?style=flat)](https://github.com/Badisi/samsung-tv-remote/stargazers) - Node.js module to remotely control Samsung Smart TV starting from 2016 (JavaScript).
* [homebridge-samsungtv2016](https://github.com/kyleaa/homebridge-samsungtv2016) [![GitHub stars](https://img.shields.io/github/stars/kyleaa/homebridge-samsungtv2016?style=flat)](https://github.com/kyleaa/homebridge-samsungtv2016/stargazers) - A plugin for [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) that allows you to control your 2016 Samsung TV with HomeKit and Siri (JavaScript).
* [homebridge-samsung-tizen](https://github.com/tavicu/homebridge-samsung-tizen) [![GitHub stars](https://img.shields.io/github/stars/tavicu/homebridge-samsung-tizen?style=flat)](https://github.com/tavicu/homebridge-samsung-tizen/stargazers) - A plugin for [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) that allows you to control your Samsung Tizen TV with HomeKit and Siri (JavaScript).
* [samsung-remote-models-2014-and-newer](https://github.com/tdudek/samsung-remote-models-2014-and-newer) [![GitHub stars](https://img.shields.io/github/stars/tdudek/samsung-remote-models-2014-and-newer?style=flat)](https://github.com/tdudek/samsung-remote-models-2014-and-newer/stargazers) - Encrypted communication with the internal web service of Samsung TV models 2014+.
* [SmartCrypto](https://github.com/sectroyer/SmartCrypto) [![GitHub stars](https://img.shields.io/github/stars/sectroyer/SmartCrypto?style=flat)](https://github.com/sectroyer/SmartCrypto/stargazers) - SmartView2 encrypted handshake API implementation in C/Python.
* [samsung-messagebox](https://github.com/shantanugoel/samsung-messagebox) [![GitHub stars](https://img.shields.io/github/stars/shantanugoel/samsung-messagebox?style=flat)](https://github.com/shantanugoel/samsung-messagebox/stargazers) - Python script to show notifications on Samsung TVs.
* [samsung-tv-control](https://github.com/Toxblh/samsung-tv-control) [![GitHub stars](https://img.shields.io/github/stars/Toxblh/samsung-tv-control?style=flat)](https://github.com/Toxblh/samsung-tv-control/stargazers) - Library for remote control Samsung TV in your Node.js

#### Other
* [Identification of Samsung TV models 2008-2017](http://en.tab-tv.com/?page_id=7123) - How to get screen size, matrix type, year of development, series and other parameters from Samsung TV model name.
* [Tizen Studio development references](https://github.com/claromes/tizenstudio) [![GitHub stars](https://img.shields.io/github/stars/claromes/tizenstudio?style=flat)](https://github.com/claromes/tizenstudio/stargazers) - Documents focused on web apps for Smart TVs e Professional Monitors, based in personal researches.
* [TizenBrew] (https://github.com/reisxd/TizenBrew) - A way to experience modded websites and you can install newer apps without fighting with Tizen Studio
* [TizenTube] (https://github.com/reisxd/TizenTube) - A TizenBrew module that enhances your favourite streaming websites viewing experience by removing ads and adding support for Sponsorblock.

### LG webOS
#### Official resources
* [webOS TV Developers Site](http://webostv.developer.lge.com) - WebOS TV apps development principles, tutorials, API documentation and packaging tools.
* [webOS TV IDE + SDK](http://webostv.developer.lge.com/sdk/download/download-sdk/) - IDE for apps development including a Command Line Interface and emulator.
* [Connect SDK](http://www.svlconnectsdk.com/) - Open source framework developed by LG that connects your mobile apps with multiple media device platforms. Currently supports 8 platforms. But seems [abandoned](https://github.com/ConnectSDK/Connect-SDK-Android/issues/364) [![GitHub stars](https://img.shields.io/github/stars/ConnectSDK/Connect-SDK-Android/issues/364?style=flat)](https://github.com/ConnectSDK/Connect-SDK-Android/issues/364/stargazers).
* [webOS TV Developers Forum](http://developer.lge.com/community/forums/RetrieveForumList.dev?prodTypeCode=TV) - Ask questions, share information and learn about Smart TV app development with other developers.

#### Third-party remote control libraries
* [lgtv2](https://github.com/hobbyquaker/lgtv2) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/lgtv2?style=flat)](https://github.com/hobbyquaker/lgtv2/stargazers) - Node.js module for remote control of LG webOS TV via WebSocket messages (JavaScript).
* [node-red-contrib-lgtv](https://github.com/hobbyquaker/node-red-contrib-lgtv) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/node-red-contrib-lgtv?style=flat)](https://github.com/hobbyquaker/node-red-contrib-lgtv/stargazers) - Module for [Node-RED](https://nodered.org) allowing  remote control of LG webOS Smart TVs (JavaScript).
* [node-webos](https://github.com/WeeJeWel/node-webos) [![GitHub stars](https://img.shields.io/github/stars/WeeJeWel/node-webos?style=flat)](https://github.com/WeeJeWel/node-webos/stargazers) - Node.js module to discover and control webOS TVs (JavaScript).
* [lgtv2mqtt](https://github.com/hobbyquaker/lgtv2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/lgtv2mqtt?style=flat)](https://github.com/hobbyquaker/lgtv2mqtt/stargazers) - Interface between LG WebOS Smart TVs and MQTT (JavaScript).
* [ares-webos-sdk](https://github.com/stevenvong/ares-webos-sdk) [![GitHub stars](https://img.shields.io/github/stars/stevenvong/ares-webos-sdk?style=flat)](https://github.com/stevenvong/ares-webos-sdk/stargazers) - webOS [CLI](http://webostv.developer.lge.com/sdk/using-webos-tv-cli/) as separate NPM module (JavaScript).
* [pylgtv](https://github.com/TheRealLink/pylgtv) [![GitHub stars](https://img.shields.io/github/stars/TheRealLink/pylgtv?style=flat)](https://github.com/TheRealLink/pylgtv/stargazers) - Library to control webOS based LG Tv devices (Python).
* [LGWebOSRemote](https://github.com/klattimer/LGWebOSRemote) [![GitHub stars](https://img.shields.io/github/stars/klattimer/LGWebOSRemote?style=flat)](https://github.com/klattimer/LGWebOSRemote/stargazers) - Command line tool for webOS remote control of LG TVs (Python).
* [homebridge-webos-tv](https://github.com/merdok/homebridge-webos-tv) [![GitHub stars](https://img.shields.io/github/stars/merdok/homebridge-webos-tv?style=flat)](https://github.com/merdok/homebridge-webos-tv/stargazers) - A plugin for [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) which allows you to control your webOS TV.
* [PyWebOSTV](https://github.com/supersaiyanmode/PyWebOSTV) [![GitHub stars](https://img.shields.io/github/stars/supersaiyanmode/PyWebOSTV?style=flat)](https://github.com/supersaiyanmode/PyWebOSTV/stargazers) - A generic & entensible WebOS 3.0 Client Library (Python2, Python3).
* [go-webos](github.com/kaperys/go-webos) - A small Go library for interaction with webOS TVs (golang).

#### Videos
* [LG Magic Motion Remote - Point, Click, and Control](https://youtu.be/yxu0G7jM_us) - Operate TV like a computer mouse.

#### Other
* [openlgtv.org.ru](http://openlgtv.org.ru) - A non-commercial project for legal reverse engineering and research on LG Television firmware. Seems a bit outdated but contains a lot of information.
* [Identification of LG TV models 2011-2017](http://en.tab-tv.com/?page_id=7111) - How to get screen size, matrix type, year of development, series and ohter parameters from LG TV model name.

### Android TV
#### Official resources
* [Android TV Developers site](https://developer.android.com/training/tv/start/start.html) - Documentation, tutorials and best practises for building Android TV apps.

#### Articles
* [How to develop Android TV App?](https://medium.com/@halilozel1903/how-to-develop-android-tv-app-5e251f3aa56b) - An article about developing apps for Android TV.

### Apple tvOS
#### Official resources
* [tvOS Developers Site](https://developer.apple.com/tvos/) - SDK, documentation and tutorials for developing tvOS apps.
* [TVML](https://developer.apple.com/documentation/tvml) -  Apple TV Markup Language for creating tvOS apps.

### Google Chromecast
#### Official resources
* [Google Cast SDK](https://developers.google.com/cast/) - Official Google Cast SDK documentation and tutorials.
* [TVs with Chromecast built-in](https://www.google.com/chromecast/built-in/tv/) - List of vendors supporting built-in Chromecast and advantages over traditional TV remote controller.

## Cross-platform frameworks
* [react-tv](https://github.com/raphamorim/react-tv) [![GitHub stars](https://img.shields.io/github/stars/raphamorim/react-tv?style=flat)](https://github.com/raphamorim/react-tv/stargazers) - React development for TV: renderer for low memory applications and Packager for WebOS, Tizen, Orsay.
* [TOAST](http://developer.samsung.com/tv/develop/extension-libraries/toast/) - Samsung open-source framework for multi-platform TV apps developemnt.
* [Enyo](http://enyojs.com) - LG framework for development apps for all major platforms, from phones and tablets to PCs and TVs.
* [Smartbox](https://github.com/immosmart/smartbox) [![GitHub stars](https://img.shields.io/github/stars/immosmart/smartbox?style=flat)](https://github.com/immosmart/smartbox/stargazers) - Smart TV universal library for Samsung, LG, Philips, SmartTV Aliance, STB Mag app development.
* [Mautilus Smart TV SDK](https://github.com/mautilus/sdk) [![GitHub stars](https://img.shields.io/github/stars/mautilus/sdk?style=flat)](https://github.com/mautilus/sdk/stargazers) - A platform-agnostic framework for developing TV Apps. Supports Samsung, LG, Philips, Sony, Panasonic and VESTEL Smart TVs.
* [BBC TAL](https://bbc.github.io/tal/) - An open source library for building applications for Smart TV developed by BBC engineers.
* [PureQML TV](https://github.com/pureqml/qmlcore-tv) [![GitHub stars](https://img.shields.io/github/stars/pureqml/qmlcore-tv?style=flat)](https://github.com/pureqml/qmlcore-tv/stargazers) - A declarative front-end framework for web-based SmartTV/STB platforms. Has experimental support of Android TV.
* [ZombieBox](https://github.com/interfaced/zombiebox) [![GitHub stars](https://img.shields.io/github/stars/interfaced/zombiebox?style=flat)](https://github.com/interfaced/zombiebox/stargazers) - An open source Smart TV framework. Strongly typed JavaScript, component based, built-in D-PAD navigation management, abstract video API with DRM for all platforms. Supports many platforms like Tizen, webOS, Android TV, etc. 

## Remote control protocols
* [DLNA](https://en.wikipedia.org/wiki/Digital_Living_Network_Alliance) - Industry-wide standard for sharing data over a home network. Depending on the DLNA-compatible devices you own, you might be able to stream films from your laptop to your TV, play an MP3 stored on your phone over your hi-fi system, or print a photo from your tablet on your home printer.
* [DIAL](http://www.dial-multiscreen.org/) - Developed by Netflix and Google, this protocol alows client devices (like smartphone, tablet, or computer) to discover apps on server devices (like a smart TV or streaming box) and launch content on them.
* [Wi-Fi Direct](https://en.wikipedia.org/wiki/Wi-Fi_Direct) - Standard enabling devices to easily connect with each other without requiring a wireless access point.
* [Miracast](https://en.wikipedia.org/wiki/Miracast) - Standard for wireless connections from devices (such as laptops, tablets, or smartphones) to displays (such as TVs, monitors or projectors). Works over Wi-Fi Direct.

## Cross-platform tools
* [smartest-tv](https://github.com/Hybirdss/smartest-tv) [![GitHub stars](https://img.shields.io/github/stars/Hybirdss/smartest-tv?style=flat)](https://github.com/Hybirdss/smartest-tv/stargazers) - CLI and MCP server for playing Netflix, YouTube, and Spotify on any smart TV by name. Deep links content across LG, Samsung, Android TV, and Roku — say "Frieren S2E8" and it plays (Python).
* [Fluxcast](https://github.com/IlyaP358/fluxcast) [![GitHub stars](https://img.shields.io/github/stars/IlyaP358/fluxcast?style=flat)](https://github.com/IlyaP358/fluxcast/stargazers) - A user-friendly Python utility for mirroring Linux desktops to Smart TVs via Miracast and DLNA, supporting GNOME, KDE, and wlroots/Wayland.

## Navigation libraries
* [lrud](https://github.com/stuart-williams/lrud) [![GitHub stars](https://img.shields.io/github/stars/stuart-williams/lrud?style=flat)](https://github.com/stuart-williams/lrud/stargazers) - Left, Right, Up, Down. A spatial navigation library for devices with input via directional controls.
* [js-spatial-navigation](https://github.com/luke-chang/js-spatial-navigation) [![GitHub stars](https://img.shields.io/github/stars/luke-chang/js-spatial-navigation?style=flat)](https://github.com/luke-chang/js-spatial-navigation/stargazers) - A javascript-based implementation of Spatial Navigation.
* [react-js-spatial-navigation](https://github.com/dead/react-js-spatial-navigation) [![GitHub stars](https://img.shields.io/github/stars/dead/react-js-spatial-navigation?style=flat)](https://github.com/dead/react-js-spatial-navigation/stargazers) - A wrapper of js-spatial-navigation to react components.
* [react-key-navigation](https://github.com/dead/react-key-navigation) [![GitHub stars](https://img.shields.io/github/stars/dead/react-key-navigation?style=flat)](https://github.com/dead/react-key-navigation/stargazers) - Spatial Navigation components for React. Similar to the ["Focus Management"](http://bbc.github.io/tal/widgets/focus-management.html) of the [BBC TAL](https://bbc.github.io/tal/).
* [react-spatial-navigation](https://github.com/NoriginMedia/react-spatial-navigation) [![GitHub stars](https://img.shields.io/github/stars/NoriginMedia/react-spatial-navigation?style=flat)](https://github.com/NoriginMedia/react-spatial-navigation/stargazers) - HOC-based Spatial Navigation (key navigation) solution for React.

## Testing
* [Suitest](https://suite.st) - Test automation solution for Smart TVs, gaming consoles, streaming sticks etc.
* [stb-tester](https://github.com/stb-tester/stb-tester) [![GitHub stars](https://img.shields.io/github/stars/stb-tester/stb-tester?style=flat)](https://github.com/stb-tester/stb-tester/stargazers) - Automated User Interface Testing for Set-Top Boxes & Smart TVs (python).

## Misc
* [LIRC](http://lirc.org) - A package that allows you to decode and send infra-red signals of many (but not all) commonly used remote controls.
* [awesome-smarttv](https://github.com/linuxenko/awesome-smarttv) [![GitHub stars](https://img.shields.io/github/stars/linuxenko/awesome-smarttv?style=flat)](https://github.com/linuxenko/awesome-smarttv/stargazers) - Another list of Smart TV resources. Discovered after this one was already done :roll_eyes:.
* [docker-tizen-webos-sdk](https://github.com/vitalets/docker-tizen-webos-sdk) [![GitHub stars](https://img.shields.io/github/stars/vitalets/docker-tizen-webos-sdk?style=flat)](https://github.com/vitalets/docker-tizen-webos-sdk/stargazers) - Docker image with Samsung Tizen CLI and LG webOS CLI. Allows to develop, build, launch and debug Smart TV apps without installing Tizen Studio and webOS SDK.

## Community
* [Stack Overflow](http://stackoverflow.com/questions/tagged/smart-tv)
* [Reddit](https://www.reddit.com/r/smarttv)

## Contribute
Feel free to share your experience and contribute useful extension resources by creating [new issue](https://github.com/vitalets/awesome-smart-tv/issues) [![GitHub stars](https://img.shields.io/github/stars/vitalets/awesome-smart-tv/issues?style=flat)](https://github.com/vitalets/awesome-smart-tv/issues/stargazers) or [pull request](https://github.com/vitalets/awesome-smart-tv/pulls) [![GitHub stars](https://img.shields.io/github/stars/vitalets/awesome-smart-tv/pulls?style=flat)](https://github.com/vitalets/awesome-smart-tv/pulls/stargazers).
Please read the [contribution guidelines](CONTRIBUTING.md) first. Thanks!

## License
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
