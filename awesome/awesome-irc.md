# IRC

> 来源：[davisonio/awesome-irc](https://github.com/davisonio/awesome-irc)

[![GitHub stars](https://img.shields.io/github/stars/davisonio/awesome-irc?style=flat)](https://github.com/davisonio/awesome-irc/stargazers)

# Awesome IRC [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> A curated list of awesome [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) resources.

A list of tools, software & other resources related to the Internet Relay Chat (IRC) protocol.

IRC (Internet Relay Chat) is an open source protocol that can be used for multi-user text based communication through channels.

## Contents

<!--lint disable awesome-list-item-->
<!--lint ignore awesome-toc double-link-->
- [Clients](#clients)
- [Bouncers](#bouncers)
  - [Hosted](#hosted)
  - [Self-hosted](#self-hosted)
- [Daemons](#daemons)
- [Services](#services)
- [Bots](#bots)
- [Encryption](#encryption)
- [Frameworks](#frameworks)
  - [Bridges](#bridges)
- [Channels](#channels)
  - [Discovery](#discovery)
  - [Platforms](#platforms)
- [Networks](#networks)
- [Articles](#articles)
- [Guides](#guides)
- [Protocol](#protocol)
- [Miscellaneous](#miscellaneous)

## Clients

*You use these to connect to IRC.*

- [![Textual-icon](https://user-images.githubusercontent.com/15098724/56874954-680a0500-69f2-11e9-87ec-d4015ce54af5.png) Textual](https://www.codeux.com/textual/) - Very customizable, ZNC integration, iCloud sync ($4.99). ([source](https://github.com/Codeux-Software/Textual) [![GitHub stars](https://img.shields.io/github/stars/Codeux-Software/Textual?style=flat)](https://github.com/Codeux-Software/Textual/stargazers)) `macOS`
- [![LimeChat-icon](https://user-images.githubusercontent.com/15098724/56875043-04cca280-69f3-11e9-8e1f-285e54784fe4.png) LimeChat](http://limechat.net/mac/) - One window for multiple servers, keyboard shortcuts, fast & stable. ([source](https://github.com/psychs/limechat) [![GitHub stars](https://img.shields.io/github/stars/psychs/limechat?style=flat)](https://github.com/psychs/limechat/stargazers)) `macOS` `iOS`
- [![HexChat-icon](https://user-images.githubusercontent.com/15098724/56874706-b28a8200-69f0-11e9-9ca7-27c8779134e0.png) HexChat](https://hexchat.github.io) - Based on XChat, easy to use, spell check & multiple languages. ([source](https://github.com/hexchat/hexchat) [![GitHub stars](https://img.shields.io/github/stars/hexchat/hexchat?style=flat)](https://github.com/hexchat/hexchat/stargazers)) `Windows` `macOS` `Linux`
- [gamja](https://sr.ht/~emersion/gamja/) - A simple IRC web client. ([source](https://git.sr.ht/~emersion/gamja)) `Web`
- [![KiwiIRC-icon](https://user-images.githubusercontent.com/15098724/56875143-a7852100-69f3-11e9-8b33-2035c156c016.png) Kiwi IRC](https://kiwiirc.com) - Powerful modern IRC messenger for the web. ([source](https://github.com/kiwiirc/kiwiirc) [![GitHub stars](https://img.shields.io/github/stars/kiwiirc/kiwiirc?style=flat)](https://github.com/kiwiirc/kiwiirc/stargazers), [demo](https://kiwiirc.com/nextclient/)) `Web`
- [![CIRC-icon](https://user-images.githubusercontent.com/15098724/56875201-1498b680-69f4-11e9-91ff-ae3b674c82be.png) CIRC](https://flackr.github.io/circ/) - Uses the chrome.sockets APIs to connect directly to IRC servers without needing a proxy. ([source](https://github.com/flackr/circ) [![GitHub stars](https://img.shields.io/github/stars/flackr/circ?style=flat)](https://github.com/flackr/circ/stargazers)) `Chrome`
- [![Quassel-icon](https://user-images.githubusercontent.com/15098724/56875264-84a73c80-69f4-11e9-807c-75db09db0ec5.png) Quassel](https://quassel-irc.org) - Distributed (clients can attach to and detach from a central core that stays permanently online. ([source](https://github.com/quassel/quassel) [![GitHub stars](https://img.shields.io/github/stars/quassel/quassel?style=flat)](https://github.com/quassel/quassel/stargazers)) `Linux` `macOS` `Windows`
- [![Circe-icon](https://user-images.githubusercontent.com/15098724/56875558-a3a6ce00-69f6-11e9-92da-2e4d8c7b4a53.png) Circe](https://github.com/emacs-circe/circe) - For use in Emacs, sane defaults. `Emacs`
- [![Smuxi-icon](https://user-images.githubusercontent.com/15098724/56875672-2f205f00-69f7-11e9-8cac-5721602234bb.png) Smuxi](https://smuxi.im) - User-friendly, based on GNOME / GTK+. ([source](https://github.com/meebey/smuxi) [![GitHub stars](https://img.shields.io/github/stars/meebey/smuxi?style=flat)](https://github.com/meebey/smuxi/stargazers)) `Linux` `Windows` `macOS`
- [![KvIRC-icon](https://user-images.githubusercontent.com/15098724/56874636-1d878900-69f0-11e9-856e-719c4c822e25.png) KvIRC](https://www.kvirc.net) - Free, portable, based on Qt GUI toolkit. ([source](https://github.com/kvirc/KVIrc) [![GitHub stars](https://img.shields.io/github/stars/kvirc/KVIrc?style=flat)](https://github.com/kvirc/KVIrc/stargazers)) `Linux` `macOS` `Windows`
- [![Konversation-icon](https://user-images.githubusercontent.com/15098724/56876024-609a2a00-69f9-11e9-91dd-196f310776d7.png) Konversation](https://konversation.kde.org) - User-friendly client built on the KDE Platform. ([source](https://github.com/KDE/konversation) [![GitHub stars](https://img.shields.io/github/stars/KDE/konversation?style=flat)](https://github.com/KDE/konversation/stargazers)) `Linux`
- [![sic-icon](https://user-images.githubusercontent.com/15098724/56876157-457bea00-69fa-11e9-94f5-11dcd0bfb00c.png) sic](https://tools.suckless.org/sic/) - **S**imple **I**RC **c**lient - a terminal client in less than 250 lines of C. `Linux` `macOS`
- [![irssi-icon](https://user-images.githubusercontent.com/15098724/56876266-0c904500-69fb-11e9-85a9-00796373cf88.png) irssi](https://irssi.org) - Terminal client, multi-protocol friendly for module authors, GPLv2. `Linux` `macOS` `Cygwin` `BSD`
- [![RevolutionIRC-icon](https://user-images.githubusercontent.com/15098724/56876444-4f065180-69fc-11e9-8200-b244b6a86e94.png) Revolution IRC](https://github.com/MCMrARM/revolution-irc) - Feature-full, actively maintained Android IRC client. `Android`
- [![AdiIRC-icon](https://user-images.githubusercontent.com/15098724/56632956-0e2fc680-6611-11e9-949e-c79c21f465a0.png) AdiIRC](https://adiirc.com) - Never has a client offered such granular settings for every aspect of the IRC experience. `Windows` `WINE`
- [![IRCforAndroid-icon](https://user-images.githubusercontent.com/15098724/56655816-b3b25c80-6648-11e9-92e1-12ca4587d9eb.png) IRC for Android™](https://www.countercultured.net/android/) - Android/Chrome OS client for power users, with ZNC built-ins, notification logic, reliable DCC, keybinds for hardware keyboards, etc. `Android` `ChromeOS`
- [Iridium](https://appcenter.elementary.io/com.github.avojak.iridium/) - Friendly IRC client built in Vala and GTK, designed for elementary OS. ([source](https://github.com/avojak/iridium) [![GitHub stars](https://img.shields.io/github/stars/avojak/iridium?style=flat)](https://github.com/avojak/iridium/stargazers)) `Linux`
- [MERK](https://github.com/nutjob-laboratories/merk) [![GitHub stars](https://img.shields.io/github/stars/nutjob-laboratories/merk?style=flat)](https://github.com/nutjob-laboratories/merk/stargazers) - Open source, multiple-document interface GUI client with a rich plugin framework supporting 40+ events; plugins created directly inside the app. `Windows` `macOS` `Linux` `Python`
- [mIRC](https://www.mirc.co.uk) - One of the most popular IRC clients for Windows, with a built-in scripting language. `Windows`
- [ObsidianIRC](https://hello.obby.world/) - Modern WebSocket IRC client with Discord-like UI. ([source](https://github.com/obbyworld/obby) [![GitHub stars](https://img.shields.io/github/stars/obbyworld/obby?style=flat)](https://github.com/obbyworld/obby/stargazers)) `Linux` `Windows` `macOS` `Android` `iOS` `Web`
- [XChat](https://xchat.org) - Precursor to HexChat, multi-platform graphical IRC client. `Windows` `Linux`
- [ircII](http://www.eterna23.net/ircii/) - One of the oldest IRC clients, initially released in 1989. `Linux` `macOS`
- [BitchX](https://bitchx.sourceforge.net/) - Terminal-based client popular on Unix-like systems. ([screenshots](https://bitchx.sourceforge.net/category/screenshots.html)) `Linux` `macOS` `Windows`
- [Goguma](https://sr.ht/~emersion/goguma/) - An IRC client for mobile devices, from the creator of soju. `Android` `Linux`

<!--lint ignore double-link-->
*More? Clients that include bouncers are found [below](#bouncers).*

## Bouncers

*Useful for disconnecting and reconnecting without losing the chat session.*

### Hosted

- [![IRCCloud-icon](https://user-images.githubusercontent.com/15098724/56879253-ba581f80-6a0c-11e9-8f6b-8461c10ed149.png) IRCCloud](https://www.irccloud.com) - Group chat for teams, friends, and communities. stay connected, chat from anywhere, and never miss a message (+client) (£0-£3.50/month).
  - [iOS App](https://github.com/irccloud/ios) [![GitHub stars](https://img.shields.io/github/stars/irccloud/ios?style=flat)](https://github.com/irccloud/ios/stargazers) - Official. `Objective-C`
  - [Android App](https://github.com/irccloud/android) [![GitHub stars](https://img.shields.io/github/stars/irccloud/android?style=flat)](https://github.com/irccloud/android/stargazers) - Official. `Java`
  - [Nimbus](https://github.com/jnordberg/irccloudapp) [![GitHub stars](https://img.shields.io/github/stars/jnordberg/irccloudapp?style=flat)](https://github.com/jnordberg/irccloudapp/stargazers) - Standalone client. `macOS` `Objective-C`

### Self-hosted

- [![Convos-icon](https://user-images.githubusercontent.com/15098724/56879497-d8724f80-6a0d-11e9-844d-7a5380b4524b.png) Convos](https://convos.chat) - Always online web IRC client. ([source](https://github.com/convos-chat/convos) [![GitHub stars](https://img.shields.io/github/stars/convos-chat/convos?style=flat)](https://github.com/convos-chat/convos/stargazers)) `Perl` `JavaScript` `Web`
- [![ZNC-icon](https://user-images.githubusercontent.com/15098724/56879721-d8268400-6a0e-11e9-8b74-c2c748d15c4a.png) ZNC](https://wiki.znc.in/ZNC) - Most popular. many different plugins. ([source](https://github.com/znc/znc) [![GitHub stars](https://img.shields.io/github/stars/znc/znc?style=flat)](https://github.com/znc/znc/stargazers)) `C++`
- [![BIP-icon](https://user-images.githubusercontent.com/15098724/56899123-89491080-6a47-11e9-8513-4c8d09be32d9.png) BIP IRC Proxy](https://packages.debian.org/sid/bip) - Always online, lightweight and secure Open Source IRC proxying with backlogging. ([source](https://salsa.debian.org/debian/bip)) `C`
- [![TheLounge-icon](https://user-images.githubusercontent.com/15098724/56899491-6b2fe000-6a48-11e9-9f01-1ed2cfb86b09.png) TheLounge](https://thelounge.chat) - Responsive, self-hosted & support for multiple users. ([source](https://github.com/thelounge/thelounge) [![GitHub stars](https://img.shields.io/github/stars/thelounge/thelounge?style=flat)](https://github.com/thelounge/thelounge/stargazers), [demo](https://demo.thelounge.chat/)) `JavaScript` `Node.js` `Web`
- [![WeeChat-icon](https://user-images.githubusercontent.com/15098724/56876389-e028f880-69fb-11e9-82d6-8084e17f2f04.png) WeeChat](https://weechat.org) - A fast, light and extensible chat client. ([source](https://github.com/weechat/weechat) [![GitHub stars](https://img.shields.io/github/stars/weechat/weechat?style=flat)](https://github.com/weechat/weechat/stargazers)) `Linux` `macOS`
- [soju](https://codeberg.org/emersion/soju) - A user-friendly IRC bouncer. `Go`
- [sms-webhook](https://github.com/terminaldweller/sms-webhook) [![GitHub stars](https://img.shields.io/github/stars/terminaldweller/sms-webhook?style=flat)](https://github.com/terminaldweller/sms-webhook/stargazers) - A simple webhook to receive SMS messages on IRC. `Go`
- [psyBNC](https://psybnc.org/) - Multi-user, permanent IRC bouncer with encryption support. `Linux`

## Daemons

*Used for running your own IRC server or network.*

- [ircd.js](https://github.com/alexyoung/ircd.js) [![GitHub stars](https://img.shields.io/github/stars/alexyoung/ircd.js?style=flat)](https://github.com/alexyoung/ircd.js/stargazers) - Server will allow clients to connect, join channels, change topics; basic stuff.
- [InspIRCd](https://www.inspircd.org) - Modular, stable, written from scratch. ([source](https://github.com/inspircd/inspircd) [![GitHub stars](https://img.shields.io/github/stars/inspircd/inspircd?style=flat)](https://github.com/inspircd/inspircd/stargazers))
- [miniircd](https://github.com/jrosdahl/miniircd) [![GitHub stars](https://img.shields.io/github/stars/jrosdahl/miniircd?style=flat)](https://github.com/jrosdahl/miniircd/stargazers) - Very simple and limited.
- [ngIRCd](https://ngircd.barton.de) - Portable and lightweight for small or private networks. ([source](https://github.com/ngircd/ngircd) [![GitHub stars](https://img.shields.io/github/stars/ngircd/ngircd?style=flat)](https://github.com/ngircd/ngircd/stargazers))
- [Ergo](https://ergo.chat/) - Modern server that's portable and designed around specifications (bleeding-edge IRCv3 support). ([source](https://github.com/ergochat/ergo) [![GitHub stars](https://img.shields.io/github/stars/ergochat/ergo?style=flat)](https://github.com/ergochat/ergo/stargazers))
- [UnrealIRCd](https://www.unrealircd.org) - Modular, advanced IRCd serving thousands of networks since 1999. ([source](https://github.com/unrealircd/unrealircd) [![GitHub stars](https://img.shields.io/github/stars/unrealircd/unrealircd?style=flat)](https://github.com/unrealircd/unrealircd/stargazers))
- [RobustIRC](https://robustirc.net) - IRC server without netsplits. ([source](https://github.com/robustirc/robustirc/) [![GitHub stars](https://img.shields.io/github/stars/robustirc/robustirc/?style=flat)](https://github.com/robustirc/robustirc//stargazers))

## Services

*Used to provide user accounts and bots like NickServ/ChanServ to your network.*

- [Atheme](https://atheme.github.io) - Designed for large networks with high scalability requirements. ([source](https://github.com/atheme/atheme) [![GitHub stars](https://img.shields.io/github/stars/atheme/atheme?style=flat)](https://github.com/atheme/atheme/stargazers))
- [anope](https://www.anope.org) - Designed for flexibility and ease of use. ([source](https://github.com/anope/anope) [![GitHub stars](https://img.shields.io/github/stars/anope/anope?style=flat)](https://github.com/anope/anope/stargazers))

## Bots

*IRC users which provide services for humans, e.g. integrations or information.*

- [Eggdrop](https://www.eggheads.org) - Oldest IRC bot still in active development. Feature rich, uses Tcl scripting. ([source](https://github.com/eggheads/eggdrop) [![GitHub stars](https://img.shields.io/github/stars/eggheads/eggdrop?style=flat)](https://github.com/eggheads/eggdrop/stargazers)) `C`
- [Sopel](https://sopel.chat) - Tonnes of ready made features, tutorial, fully documented. ([source](https://github.com/sopel-irc/sopel) [![GitHub stars](https://img.shields.io/github/stars/sopel-irc/sopel?style=flat)](https://github.com/sopel-irc/sopel/stargazers)) `Python`
- [Limnoria](https://github.com/ProgVal/Limnoria) [![GitHub stars](https://img.shields.io/github/stars/ProgVal/Limnoria?style=flat)](https://github.com/ProgVal/Limnoria/stargazers) - Robust, user friendly, developer friendly. `Python`
- [Twitch Plays](https://github.com/aidanrwt/twitch-plays ) [![GitHub stars](https://img.shields.io/github/stars/aidanrwt/twitch-plays?style=flat)](https://github.com/aidanrwt/twitch-plays/stargazers) - Takes input from the chat and presses the corresponding key. `Python`
- [Skybot](https://github.com/rmmh/skybot) [![GitHub stars](https://img.shields.io/github/stars/rmmh/skybot?style=flat)](https://github.com/rmmh/skybot/stargazers) - Main goals are simplicity and power. `Python`
- [lazybot](https://github.com/Raynes/lazybot) [![GitHub stars](https://img.shields.io/github/stars/Raynes/lazybot?style=flat)](https://github.com/Raynes/lazybot/stargazers) - User-friendly and powerful. `Clojure`
- [IRC-BF](https://gitlab.com/ddevault/bf-irc-bot) - `Brainfuck`
- [geordi](https://github.com/Eelis/geordi) [![GitHub stars](https://img.shields.io/github/stars/Eelis/geordi?style=flat)](https://github.com/Eelis/geordi/stargazers) - Compiles and runs C++ code snippets. `C++`
- [CloudBot](https://github.com/TotallyNotRobots/CloudBot) [![GitHub stars](https://img.shields.io/github/stars/TotallyNotRobots/CloudBot?style=flat)](https://github.com/TotallyNotRobots/CloudBot/stargazers) - Simple, fast, expandable. `Python`
- [yossarian-bot](https://github.com/woodruffw/yossarian-bot) [![GitHub stars](https://img.shields.io/github/stars/woodruffw/yossarian-bot?style=flat)](https://github.com/woodruffw/yossarian-bot/stargazers) - Large default plugin set, Cinch-based. `Ruby`
- [helga](https://github.com/shaunduncan/helga) [![GitHub stars](https://img.shields.io/github/stars/shaunduncan/helga?style=flat)](https://github.com/shaunduncan/helga/stargazers) - Pluggable chat bot supporting multiple protocols. `Python`
- [EveIRC](https://github.com/Inspyre-Technologies/EveIRC) [![GitHub stars](https://img.shields.io/github/stars/Inspyre-Technologies/EveIRC?style=flat)](https://github.com/Inspyre-Technologies/EveIRC/stargazers) - Extendable chat/channel/server-managenent service-providing bot. Using the [Cinch Framework](https://github.com/cinchrb/cinch) [![GitHub stars](https://img.shields.io/github/stars/cinchrb/cinch?style=flat)](https://github.com/cinchrb/cinch/stargazers). `Ruby`
- [BitBot](https://github.com/bitbot-irc/bitbot) [![GitHub stars](https://img.shields.io/github/stars/bitbot-irc/bitbot?style=flat)](https://github.com/bitbot-irc/bitbot/stargazers) - Modular, event-driven bot featuring a REST API, individual user settings and much more. ([bitbot.dev](https://bitbot.dev)) `Python`
- [Cardinal](https://github.com/JohnMaguire/Cardinal) [![GitHub stars](https://img.shields.io/github/stars/JohnMaguire/Cardinal?style=flat)](https://github.com/JohnMaguire/Cardinal/stargazers) - Python Twisted IRC bot with a focus on ease of plugin development. `Python`
- [pyHoneybot](https://pyhoneybot.github.io/honeybot-store/) - Python Twisted IRC bot with a focus on ease of plugin development. ([source](https://github.com/pyhoneybot/honeybot) [![GitHub stars](https://img.shields.io/github/stars/pyhoneybot/honeybot?style=flat)](https://github.com/pyhoneybot/honeybot/stargazers)) `Python`
- [wayback](https://github.com/wabarc/wayback) [![GitHub stars](https://img.shields.io/github/stars/wabarc/wayback?style=flat)](https://github.com/wabarc/wayback/stargazers) - An archiving tool with an IRC interface integrated with various archiving services.
- [milla](https://github.com/terminaldweller/milla) [![GitHub stars](https://img.shields.io/github/stars/terminaldweller/milla?style=flat)](https://github.com/terminaldweller/milla/stargazers) - New generation LLM-powered bot with lua scripting support. `Go`
- [MansionNET Bot Suite](https://github.com/MansionNET) [![GitHub stars](https://img.shields.io/github/stars/MansionNET?style=flat)](https://github.com/MansionNET/stargazers) - Collection of self-hostable IRC bots: AI chat assistant, real-time weather, privacy-focused search, YouTube metadata, and AI-powered trivia. `Python`

## Encryption

*Plugins and tools for encrypting IRC messages.*

- [irssi-otr](https://github.com/cryptodotis/irssi-otr) [![GitHub stars](https://img.shields.io/github/stars/cryptodotis/irssi-otr?style=flat)](https://github.com/cryptodotis/irssi-otr/stargazers) - Off-the-Record (OTR) messaging plugin for irssi. `C`
- [weechat-otr](https://github.com/mmb/weechat-otr) [![GitHub stars](https://img.shields.io/github/stars/mmb/weechat-otr?style=flat)](https://github.com/mmb/weechat-otr/stargazers) - Off-the-Record (OTR) messaging plugin for WeeChat. `Python`
- [FiSH-irssi](https://github.com/falsovsky/FiSH-irssi) [![GitHub stars](https://img.shields.io/github/stars/falsovsky/FiSH-irssi?style=flat)](https://github.com/falsovsky/FiSH-irssi/stargazers) - Blowfish encryption in ECB/CBC modes with Diffie-Hellman key exchange for irssi. `C`

## Frameworks

*Helpful to write bots or integrate IRC with applications.*

- [node-irc](https://github.com/Throne3d/node-irc) [![GitHub stars](https://img.shields.io/github/stars/Throne3d/node-irc?style=flat)](https://github.com/Throne3d/node-irc/stargazers) `JavaScript`
- [goirc](https://github.com/fluffle/goirc) [![GitHub stars](https://img.shields.io/github/stars/fluffle/goirc?style=flat)](https://github.com/fluffle/goirc/stargazers) - Event-based, stateful, lacking documentation. `Go`
- [Hubot IRC Adapter](https://github.com/nandub/hubot-irc) [![GitHub stars](https://img.shields.io/github/stars/nandub/hubot-irc?style=flat)](https://github.com/nandub/hubot-irc/stargazers) - The IRC adapter for hubot. `JavaScript`
- [go-ircevent](https://github.com/thoj/go-ircevent) [![GitHub stars](https://img.shields.io/github/stars/thoj/go-ircevent?style=flat)](https://github.com/thoj/go-ircevent/stargazers) - Event-based. `Go`
- [slate-irc](https://github.com/slate/slate-irc) [![GitHub stars](https://img.shields.io/github/stars/slate/slate-irc?style=flat)](https://github.com/slate/slate-irc/stargazers) - Plugin system, simple api, arbitrary input stream, debug support. `JavaScript`
- [PircBotX](https://github.com/pircbotx/pircbotx) [![GitHub stars](https://img.shields.io/github/stars/pircbotx/pircbotx?style=flat)](https://github.com/pircbotx/pircbotx/stargazers) - Event based IRC Library with a straightforward API (updated fork of [PircBot](https://www.jibble.org/pircbot.php)). `Java`
- [IRC::Client](https://github.com/lizmat/IRC-Client) [![GitHub stars](https://img.shields.io/github/stars/lizmat/IRC-Client?style=flat)](https://github.com/lizmat/IRC-Client/stargazers) - `Perl6` based extendable IRC client framework.
- [irccd](https://projects.malikania.fr/irccd/index.html) - Flexible IRC bot customizable with JavaScript. `C++`.

### Bridges

*Sends messages back and forth.*

- [discord-irc](https://github.com/reactiflux/discord-irc) [![GitHub stars](https://img.shields.io/github/stars/reactiflux/discord-irc?style=flat)](https://github.com/reactiflux/discord-irc/stargazers) - Discord ↔ IRC. `JavaScript`
- [dibridge](https://github.com/OpenTTD/dibridge) [![GitHub stars](https://img.shields.io/github/stars/OpenTTD/dibridge?style=flat)](https://github.com/OpenTTD/dibridge/stargazers) - Discord ↔ IRC (with puppets) `Python`
- [Dis4IRC](https://github.com/zachbr/Dis4IRC) [![GitHub stars](https://img.shields.io/github/stars/zachbr/Dis4IRC?style=flat)](https://github.com/zachbr/Dis4IRC/stargazers) - Discord ↔ IRC. `Kotlin`
- [slack-irc](https://github.com/ekmartin/slack-irc) [![GitHub stars](https://img.shields.io/github/stars/ekmartin/slack-irc?style=flat)](https://github.com/ekmartin/slack-irc/stargazers) - Slack ↔ IRC. `JavaScript`
- [irc-slack](https://github.com/insomniacslk/irc-slack) [![GitHub stars](https://img.shields.io/github/stars/insomniacslk/irc-slack?style=flat)](https://github.com/insomniacslk/irc-slack/stargazers) - Slack ↔ IRC. `Go`
- [BitlBee](https://www.bitlbee.org/main.php/news.r.html) - XMPP, Jabber, Google Talk, MSN Messenger, Yahoo! Messenger, AIM, ICQ, Twitter API, HipChat ↔ IRC. `C`
- [teleirc](https://github.com/RITlug/teleirc) [![GitHub stars](https://img.shields.io/github/stars/RITlug/teleirc?style=flat)](https://github.com/RITlug/teleirc/stargazers) - Telegram ↔ IRC. `JavaScript`
- [toxirc](https://github.com/e0ff/toxirc) [![GitHub stars](https://img.shields.io/github/stars/e0ff/toxirc?style=flat)](https://github.com/e0ff/toxirc/stargazers) - Tox ↔ IRC. `C`
- [skyweb2irc](https://github.com/ProgVal/skyweb2irc) [![GitHub stars](https://img.shields.io/github/stars/ProgVal/skyweb2irc?style=flat)](https://github.com/ProgVal/skyweb2irc/stargazers) - Skype (webclient API) ↔ IRC. `Javascript`
- [matterbridge](https://github.com/42wim/matterbridge) [![GitHub stars](https://img.shields.io/github/stars/42wim/matterbridge?style=flat)](https://github.com/42wim/matterbridge/stargazers) - IRC ↔ Mattermost ↔ Discord ↔ XMPP ↔ Gitter ↔ Slack ↔ Discord ↔ Telegram ↔ etc. `Go`
- [Heisenbridge](https://github.com/hifi/heisenbridge) [![GitHub stars](https://img.shields.io/github/stars/hifi/heisenbridge?style=flat)](https://github.com/hifi/heisenbridge/stargazers) - Bouncer-style Matrix IRC bridge `Python`
- [Appservice-IRC](https://github.com/matrix-org/matrix-appservice-irc) [![GitHub stars](https://img.shields.io/github/stars/matrix-org/matrix-appservice-irc?style=flat)](https://github.com/matrix-org/matrix-appservice-irc/stargazers) - Gateway and bridge Matrix ↔ IRC `Javascript`
- [matterircd](https://github.com/42wim/matterircd) [![GitHub stars](https://img.shields.io/github/stars/42wim/matterircd?style=flat)](https://github.com/42wim/matterircd/stargazers) - Matterbridge ↔ IRC, Slack ↔ IRC, Mastodon ↔ IRC. `Go`

## Channels

*IRC channels.*

### Discovery

- [netsplit.de Search](https://netsplit.de/channels/ ) - Searches 563 different networks.
- [KiwiIRC Search](https://kiwiirc.com/search) - Searches 318 different networks.

### Platforms

- [#Ubuntu](https://wiki.ubuntu.com/IRC/ChannelList)@Libera.Chat - Official Ubuntu support channel. ([rules](https://wiki.ubuntu.com/IRC/Guidelines))

## Networks

*A collection of IRC servers is known as a network.*

- [Libera.Chat](https://libera.chat) - Network mostly focused on free and open source projects, run by former freenode staff.
- [MansionNET](https://inthemansion.com) - Privacy-focused community network running UnrealIRCd with Anope services; open to all, no tracking, no ads. (`irc.inthemansion.com:6697`, webchat at `webirc.inthemansion.com`)
- [Snoonet](https://snoonet.org) - Community of redditors and subreddits. ([rules](https://snoonet.org/rules/))
- [OFTC](https://oftc.net) - Community for free and open source software communities.
- [LibertaCasa](https://liberta.casa) - Privacy endorsing community serving as a safe and open space for the discussion of various topics.

## Articles

*Articles and blog posts about IRC.*

- [Please don't use Slack for FOSS projects](https://drewdevault.com/2015/11/01/Please-stop-using-slack.html) - Drew DeVault's Blog.
- [IRC is dead, long live IRC](https://www.pingdom.com/blog/irc-is-dead-long-live-irc/) - Pingdom.
- [IRC Has Lost 60% Of Its Users Since 2003, But Life As A Robot Is Just Beginning](https://techcrunch.com/2013/01/06/irc-has-lost-60-of-its-users-since-2003-but-life-as-a-robot-is-just-beginning/) - Alex Williams (TechCrunch).

## Guides

*How-to's, documentation and books.*

- [#irchelp](https://www.irchelp.org) - A vast amount of reasonably up-to-date information.

## Protocol

*Information and resources about the IRC protocol itself.*

- [IRCv3 Working Group](https://ircv3.net) - A group of IRC software authors working to enhance, improve, maintain and standardize the IRC protocol. ([source](https://github.com/ircv3/ircv3.github.io) [![GitHub stars](https://img.shields.io/github/stars/ircv3/ircv3.github.io?style=flat)](https://github.com/ircv3/ircv3.github.io/stargazers))
- [Modern IRC Documents](https://modern.ircdocs.horse) - An attempt to write an update to the original IRC protocol. documentation ([source](https://github.com/ircdocs/modern-irc) [![GitHub stars](https://img.shields.io/github/stars/ircdocs/modern-irc?style=flat)](https://github.com/ircdocs/modern-irc/stargazers))
- [IRC Definition Files](https://defs.ircdocs.horse) - Lists of numerics, modes, ISUPPORT tokens and other protocol details. ([source](https://github.com/ircdocs/irc-defs) [![GitHub stars](https://img.shields.io/github/stars/ircdocs/irc-defs?style=flat)](https://github.com/ircdocs/irc-defs/stargazers))
- [grawity's IRC docs](https://github.com/grawity/irc-docs) [![GitHub stars](https://img.shields.io/github/stars/grawity/irc-docs?style=flat)](https://github.com/grawity/irc-docs/stargazers) - Collection of misc IRC protocol documentation.
- [Protocol Statistics](https://stats.ircdocs.horse) - Statistics around the server software in use on networks today. ([source](https://github.com/ircdocs/irc-stats) [![GitHub stars](https://img.shields.io/github/stars/ircdocs/irc-stats?style=flat)](https://github.com/ircdocs/irc-stats/stargazers))
- [IRC Parser Tests](https://github.com/ircdocs/parser-tests) [![GitHub stars](https://img.shields.io/github/stars/ircdocs/parser-tests?style=flat)](https://github.com/ircdocs/parser-tests/stargazers) - A CC0 set of test suites, to ensure IRC message parsers are consistent.

## Miscellaneous

*Items that belong on the list but defy classification.*

- [superseriousstats](https://github.com/tommyrot/superseriousstats) [![GitHub stars](https://img.shields.io/github/stars/tommyrot/superseriousstats?style=flat)](https://github.com/tommyrot/superseriousstats/stargazers) - Fast and efficient program to create statistics out of various types of chat logs. `PHP` `Web`
- [img2src](https://github.com/waveplate/img2irc) [![GitHub stars](https://img.shields.io/github/stars/waveplate/img2irc?style=flat)](https://github.com/waveplate/img2irc/stargazers) - Convert images to halfblock ANSI or IRC, with a bunch of post-processing filters. `Rust`

## Use

The best ways to use this list are:

- By browsing the [contents](#contents)
- By using <kbd>command</kbd> + <kbd>F</kbd> to search the contents

This list also uses tags to help when searching the contents:
- **Language** - `Python`, `Java`, `C++`, `Go`, `JavaScript`, `Ruby`, `C` etc.
- **Platform** - `Web`, `macOS`, `Windows`, `Linux`, `Chrome` etc.

## Credits

By [Craig Davison](https://davison.io) and contributors.
