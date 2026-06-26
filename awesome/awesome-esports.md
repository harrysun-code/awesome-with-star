# Esports

[![GitHub stars](https://img.shields.io/github/stars/strift/awesome-esports?style=flat)](https://github.com/strift/awesome-esports/stargazers)

# Awesome Esports [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open-source projects related to esports.

[Esports](https://en.wikipedia.org/wiki/Esports) (also known as electronic sports or e-sports) is a form of competition using video games. It often takes the form of organized, multiplayer video game competitions, particularly between professional players, individually or as teams.

Unmaintained projects, now only relevant for educational purposes, are in the [Archive](ARCHIVE.md).

## Contents

- [Libraries](#libraries)
  - [APIs & Web Services](#apis--web-services)
  - [Authentication](#authentication)
  - [Data parsing and analysis](#data-parsing-and-analysis)
  - [Team management](#team-management)
  - [Tournaments management](#tournaments-management)
- [Developer tools](#developer-tools)
- [Unofficial documentation](#unofficial-documentation)
- [Applications & Tools](#applications--tools)
- [Education](#education)

## Libraries

> Programming libraries organized per use cases.

### APIs & Web Services

- [Blizzard.js](https://github.com/benweier/blizzard.js) [![GitHub stars](https://img.shields.io/github/stars/benweier/blizzard.js?style=flat)](https://github.com/benweier/blizzard.js/stargazers) - A Node.js library for interacting with the Blizzard Community Platform API.
- [Discord.js](https://github.com/discordjs/discord.js) [![GitHub stars](https://img.shields.io/github/stars/discordjs/discord.js?style=flat)](https://github.com/discordjs/discord.js/stargazers) - A Node.js library for interacting with the Discord API.
- [HLTV](https://github.com/gigobyte/HLTV) [![GitHub stars](https://img.shields.io/github/stars/gigobyte/HLTV?style=flat)](https://github.com/gigobyte/HLTV/stargazers) - A Node.js library for interacting with the HLTV API.
- [liquipediapy](https://github.com/c00kie17/liquipediapy) [![GitHub stars](https://img.shields.io/github/stars/c00kie17/liquipediapy?style=flat)](https://github.com/c00kie17/liquipediapy/stargazers) - A Python library for interacting with the Liquipedia API.
- [steam](https://github.com/ValvePython/steam/) [![GitHub stars](https://img.shields.io/github/stars/ValvePython/steam/?style=flat)](https://github.com/ValvePython/steam//stargazers) - A Python library for interacting with various parts of Steam.
- [Steam Community](https://github.com/DoctorMcKay/node-steamcommunity) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steamcommunity?style=flat)](https://github.com/DoctorMcKay/node-steamcommunity/stargazers) - A Node.js library for interacting with the Steam Community website.
- SteamID - A library for manipulating Steam IDs.
  - [Node.js](https://github.com/DoctorMcKay/node-steamid) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steamid?style=flat)](https://github.com/DoctorMcKay/node-steamid/stargazers)
  - [PHP](https://github.com/DoctorMcKay/php-steamid) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/php-steamid?style=flat)](https://github.com/DoctorMcKay/php-steamid/stargazers)
- [SteamUser](https://github.com/DoctorMcKay/node-steam-user) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-user?style=flat)](https://github.com/DoctorMcKay/node-steam-user/stargazers) - A Node.js library for interacting with the Steam network via the Steam client protocol.
- [Steam TOTP](https://github.com/DoctorMcKay/node-steam-totp) [![GitHub stars](https://img.shields.io/github/stars/DoctorMcKay/node-steam-totp?style=flat)](https://github.com/DoctorMcKay/node-steam-totp/stargazers) - A Node.js library for generating Steam-style 2FA codes.
- [valorant.js](https://github.com/liamcottle/valorant.js) [![GitHub stars](https://img.shields.io/github/stars/liamcottle/valorant.js?style=flat)](https://github.com/liamcottle/valorant.js/stargazers) - A Node.js library for interacting with the VALORANT APIs used in game.

### Authentication

- [Passport-Steam](https://github.com/liamcurry/passport-steam) [![GitHub stars](https://img.shields.io/github/stars/liamcurry/passport-steam?style=flat)](https://github.com/liamcurry/passport-steam/stargazers) - A Node.js passport authentication strategy for Steam.

### Data parsing and analysis

- [awpy](https://github.com/pnxenopoulos/awpy) [![GitHub stars](https://img.shields.io/github/stars/pnxenopoulos/awpy?style=flat)](https://github.com/pnxenopoulos/awpy/stargazers) - A Python library for parsing, analyzing, and visualizing CS:GO data.
- [Boxcars](https://github.com/nickbabcock/boxcars) [![GitHub stars](https://img.shields.io/github/stars/nickbabcock/boxcars?style=flat)](https://github.com/nickbabcock/boxcars/stargazers) - A Rust library for parsing Rocket League replays.
- [Cassiopeia](https://github.com/meraki-analytics/cassiopeia) [![GitHub stars](https://img.shields.io/github/stars/meraki-analytics/cassiopeia?style=flat)](https://github.com/meraki-analytics/cassiopeia/stargazers) - A Python framework for interacting with and analyzing data from the Riot Games League of Legends API.
- [Clarity](https://github.com/skadistats/clarity) [![GitHub stars](https://img.shields.io/github/stars/skadistats/clarity?style=flat)](https://github.com/skadistats/clarity/stargazers) - A Java library for parsing CS:GO and Dota 2 replays.
- [demoinfocs-golang](https://github.com/markus-wa/demoinfocs-golang) [![GitHub stars](https://img.shields.io/github/stars/markus-wa/demoinfocs-golang?style=flat)](https://github.com/markus-wa/demoinfocs-golang/stargazers) - A Go library for parsing and analyzing CS:GO demos (ie. replays.)
- [Rattletrap](https://github.com/tfausak/rattletrap) [![GitHub stars](https://img.shields.io/github/stars/tfausak/rattletrap?style=flat)](https://github.com/tfausak/rattletrap/stargazers) - A Haskell library for parsing and generating Rocket League replays.

### Team management

- [LoL in-house bot](https://github.com/mrtolkien/inhouse_bot) [![GitHub stars](https://img.shields.io/github/stars/mrtolkien/inhouse_bot?style=flat)](https://github.com/mrtolkien/inhouse_bot/stargazers) - A Discord bot handling role queue, matchmaking, and rankings for League of Legends in-house games.

### Tournaments management

- [brackets-manager.js](https://github.com/Drarig29/brackets-manager.js) [![GitHub stars](https://img.shields.io/github/stars/Drarig29/brackets-manager.js?style=flat)](https://github.com/Drarig29/brackets-manager.js/stargazers) - A JavaScript library to manage tournament brackets.
- [brackets-viewer.js](https://github.com/Drarig29/brackets-viewer.js) [![GitHub stars](https://img.shields.io/github/stars/Drarig29/brackets-viewer.js?style=flat)](https://github.com/Drarig29/brackets-viewer.js/stargazers) - A JavaScript library to display tournament brackets.

## Developer tools

> Tooling for developers.

- [Fortnite VSCode Theme](https://github.com/sdras/fortnite-vscode-theme) [![GitHub stars](https://img.shields.io/github/stars/sdras/fortnite-vscode-theme?style=flat)](https://github.com/sdras/fortnite-vscode-theme/stargazers) - A Visual Studio Code theme inspired by Fortnite.

## Unofficial documentation

> Community-maintained documentation of editor APIs.

- [BNETDocs](https://github.com/BNETDocs/bnetdocs-web) [![GitHub stars](https://img.shields.io/github/stars/BNETDocs/bnetdocs-web?style=flat)](https://github.com/BNETDocs/bnetdocs-web/stargazers) - A documentation and discussion website for Blizzard and Battle.net protocols.
- [Rift Explorer](https://github.com/Pupix/rift-explorer) [![GitHub stars](https://img.shields.io/github/stars/Pupix/rift-explorer?style=flat)](https://github.com/Pupix/rift-explorer/stargazers) - An automatically generated documentation of Riot Games LCU API.
- [valorant-api-docs](https://github.com/techchrism/valorant-api-docs) [![GitHub stars](https://img.shields.io/github/stars/techchrism/valorant-api-docs?style=flat)](https://github.com/techchrism/valorant-api-docs/stargazers) - An automatically generated documentation of Valorant internal API.

## Applications & Tools

> Applications and general-purpose tooling.

- [Esport Team Logos](https://github.com/lootmarket/esport-team-logos) [![GitHub stars](https://img.shields.io/github/stars/lootmarket/esport-team-logos?style=flat)](https://github.com/lootmarket/esport-team-logos/stargazers) - A database of Esports teams logos.

**Counter-Strike: Global Offensive**

- [Boltobserv](https://github.com/boltgolt/boltobserv) [![GitHub stars](https://img.shields.io/github/stars/boltgolt/boltobserv?style=flat)](https://github.com/boltgolt/boltobserv/stargazers) - An external Counter-Strike: Global Offensive radar for observers.

**Dota 2**

- [Open Dota](https://github.com/odota/core) [![GitHub stars](https://img.shields.io/github/stars/odota/core?style=flat)](https://github.com/odota/core/stargazers) - A website for Dota 2 esports stats.

**League of Legends**

- [Foldy Sheet](https://github.com/chhopsky/foldysheet) [![GitHub stars](https://img.shields.io/github/stars/chhopsky/foldysheet?style=flat)](https://github.com/chhopsky/foldysheet/stargazers) - A Python script to determine whether teams can make playoffs or not.
- [LeagueDirector](https://github.com/RiotGames/leaguedirector) [![GitHub stars](https://img.shields.io/github/stars/RiotGames/leaguedirector?style=flat)](https://github.com/RiotGames/leaguedirector/stargazers) - A desktop application for staging and recording videos from League of Legends replays.
- [LeagueStats](https://github.com/vkaelin/LeagueStats) [![GitHub stars](https://img.shields.io/github/stars/vkaelin/LeagueStats?style=flat)](https://github.com/vkaelin/LeagueStats/stargazers) - A website for League of Legends summoners' stats.

## Education

- [League of Legends Analytics](https://github.com/FloPrm/lol_analytics) [![GitHub stars](https://img.shields.io/github/stars/FloPrm/lol_analytics?style=flat)](https://github.com/FloPrm/lol_analytics/stargazers) - A collection of League of Legends data-related guides, libraries, and learning materials for Data Analysts.

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
