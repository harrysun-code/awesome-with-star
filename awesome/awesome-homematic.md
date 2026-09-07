# Homematic

> 来源：[homematic-community/awesome-homematic](https://github.com/homematic-community/awesome-homematic)

[![GitHub stars](https://img.shields.io/github/stars/homematic-community/awesome-homematic?style=flat)](https://github.com/homematic-community/awesome-homematic/stargazers)

# Awesome Homematic [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> A curated list of Homematic related links

[Homematic](https://www.homematic.com/) is a series of Smart Home devices from the manufacturer [eQ-3](https://www.eq-3.de), popular especially in Germany.


## Contents

- [Community](#community)
- [Documentation](#documentation)
- [Mobile Apps](#mobile-apps)
- [CCU Alternatives](#ccu-alternatives)
- [Alternative Sensors and Actuators](#alternative-sensors-and-actuators)
- [CCU Addons](#ccu-addons)
- [Interfacing Software](#interfacing-software)
- [Misc Software](#misc-software)
- [Software Modules](#software-modules)
- [Smart Home Software](#smart-home-software-supporting-homematic)
- [Verschiedenes](#misc)
- [License](License)


## Community Ressources (mostly german language)

* [Haus Automatisierung](https://haus-automatisierung.com/) - News, Blog, Youtube, Tutorials, ...
* [Homematic Forum](https://homematic-forum.de/forum/) - Diskussions-Foren
* [Homematic Forum: Link/Skript-Sammlung](https://homematic-forum.de/forum/viewtopic.php?f=26&t=27907) - Curated link list by AndiN.
* [Homematic Forum: Addons & Tools Übersicht](https://homematic-forum.de/forum/viewtopic.php?t=46890) - Übersicht über Addons und Tools für CCU / OpenCCU.
* [Homematic Forum: HomeMatic - Tipps für Anfänger](https://homematic-forum.de/forum/viewtopic.php?f=31&t=22801) - Pflichtlektüre für Einsteiger von Sammy
* [Homematic Guru](https://homematic-guru.de/) - News, Blog, Tutorials und mehr.
* [Homematic Inside](https://www.homematic-inside.de/) - News, Blog, Tutorials und mehr (wird nicht weitergeführt, bleibt als Archiv online).
* [Homematic Blog Lison](https://homematic-blog.lison.ch/) - Blog, Tutorials und mehr..
* [Technikkram](https://technikkram.net) - News, Blog, Tutorials und mehr.
* [Verdrahtet](https://www.verdrahtet.info/) - News, Blog, Youtube, Tutorials, ...
* [Wikimatic](http://www.wikimatic.de/wiki/Hauptseite) - Community Wiki.


## Documentation

* [ccu-addon-howto](https://github.com/homematic-community/ccu-addon-howto) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/ccu-addon-howto?style=flat)](https://github.com/homematic-community/ccu-addon-howto/stargazers) - Howto für die Entwicklung von Addons für die Homematic CCU und OpenCCU.
* [Direktverknüpfungen im Expertenmodus](https://www.youtube.com/watch?v=1B4iwtK1Rmo) - Vortrag von Frank Grass.
* [Dissecting HomeMatic AES](https://git.zerfleddert.de/hmcfgusb/AES/) - BidCos Protocol AES Handshake description.
* [HomeMatic-Script Dokumentation](https://www.eq-3.de/downloads/download/homematic/hm_web_ui_doku/HM-Skript_Teil_1_Sprachbeschreibung_V2.3.pdf) - Offizielle Dokumentation von eQ-3: [Teil 1 Sprachbeschreibung](https://www.eq-3.de/downloads/download/homematic/hm_web_ui_doku/HM-Skript_Teil_1_Sprachbeschreibung_V2.3.pdf), [Teil 2 Objektmodell](https://www.eq-3.de/Downloads/eq3/download%20bereich/hm_web_ui_doku/HM_Script_Teil_2_Objektmodell_V1.2.pdf), [Teil 3 Beispiele](https://www.eq-3.de/Downloads/eq3/download%20bereich/hm_web_ui_doku/HM_Script_Teil_3_Beispiele_V1.1.pdf), [Teil 4 Datenpunkte](https://www.eq-3.de/Downloads/eq3/download%20bereich/hm_web_ui_doku/HM-Script_4-Datenpunkte.pdf).
* [HomeMatic XML-RPC API](https://www.eq-3.de/Downloads/eq3/download%20bereich/hm_web_ui_doku/HM_XmlRpc_API.pdf) - Offizielle Spezifikation der XML-RPC Schnittstelle der Interface-Prozesse von eQ-3.
* [Keymatic Konfiguration](https://homematic-forum.de/forum/viewtopic.php?f=31&t=19196) - Beitrag von rewe0815 im Homematic Forum.
* [OpenCCU Wiki](https://github.com/OpenCCU/OpenCCU/wiki) - Installation, Administration und Nutzung von OpenCCU.
* [Script Documentation](http://www.wikimatic.de/wiki/Script_Dokumentation) - Inoffizielle Homematic Script Referenz.
* [Virtuelle Aktorkanäle](https://www.youtube.com/watch?v=Cwxwtig6Q1I) - Vortrag von Frank Grass.

## Mobile Apps

* [@home](https://www.athomeapp.de/) - iOS - (💵 inApp-Purchase um Werbung zu entfernen)
* [HistClient](https://www.sa-com.de/smarthome-special/histclient-handbuch/) - (💵 inApp-Purchase) - CCU-Historian Client mit erweitereten Features für iOS und Android
* [TinyMatic](https://www.tinymatic.de/) - 💵 Android (ehemals: HomeDroid)
* [Pocket Control](https://www.penzler.de) - 💵 iOS
* [Battery Status for HomeMatic](https://zeezide.com/en/products/hmbattery/) - 💵 iOS


## CCU Alternatives

* [debmatic](https://github.com/alexreinert/debmatic) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/debmatic?style=flat)](https://github.com/alexreinert/debmatic/stargazers) - Install the Homematic OCCU on Debian based amd64, armhf and arm64 systems (Debian, Ubuntu, Raspbian, Armbian)
* [Homegear](https://homegear.eu/index.php/Main_Page) - Free and open source program to interface your smart home devices with your home automation software or your own scripts.
* [OCCU](https://github.com/eq-3/occu) [![GitHub stars](https://img.shields.io/github/stars/eq-3/occu?style=flat)](https://github.com/eq-3/occu/stargazers) - The HM-OCCU-SDK published by eQ-3, the base of debmatic, piVCCU and OpenCCU.
* [OpenCCU](https://github.com/OpenCCU/OpenCCU) [![GitHub stars](https://img.shields.io/github/stars/OpenCCU/OpenCCU?style=flat)](https://github.com/OpenCCU/OpenCCU/stargazers) - Lightweight, OCCU and Linux/buildroot-based distribution for running a HomeMatic CCU on embedded devices like the RaspberryPi, x86/ARM or as virtual appliance (formerly known as RaspberryMatic).
* [piVCCU](https://github.com/alexreinert/piVCCU) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/piVCCU?style=flat)](https://github.com/alexreinert/piVCCU/stargazers) - Install the original Homematic CCU firmware inside a virtualized container (lxc) on Raspbian or Armbian.


## Alternative Sensors, Actuators and Hardware Modifications

* [AskSin++](https://asksinpp.de/) - Dokumentation, Sketche und Community-Projekte rund um Selbstbau-Komponenten für HomeMatic auf Basis von Arduino/STM32 und CC1101.
* [AskSinPPCollection](https://jp112sdl.github.io/AskSinPPCollection/) - Einführung, Dokumentation und Projekte rund um Selbstbau-Komponenten mit AskSinPP
* [Beispiel_AskSinPP](https://github.com/jp112sdl/Beispiel_AskSinPP) [![GitHub stars](https://img.shields.io/github/stars/jp112sdl/Beispiel_AskSinPP?style=flat)](https://github.com/jp112sdl/Beispiel_AskSinPP/stargazers) - Beispiel Sketche für die Verwendung der [AskSinPP](https://github.com/pa-pa/AskSinPP) [![GitHub stars](https://img.shields.io/github/stars/pa-pa/AskSinPP?style=flat)](https://github.com/pa-pa/AskSinPP/stargazers) Bibliothek
* [HAUS-BUS.DE](http://www.haus-bus.de/) - 💵 Homematic Wired kompatible Geräte.
* [HB-RF-ETH](https://github.com/alexreinert/HB-RF-ETH) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/HB-RF-ETH?style=flat)](https://github.com/alexreinert/HB-RF-ETH/stargazers) - Platine und Firmware um ein Homematic Funkmodul (HM-MOD-RPI-PCB, RPI-RF-MOD) per Netzwerk an debmatic oder piVCCU anzubinden.
* [HB-RF-ETH-ng](https://github.com/Xerolux/HB-RF-ETH-ng) [![GitHub stars](https://img.shields.io/github/stars/Xerolux/HB-RF-ETH-ng?style=flat)](https://github.com/Xerolux/HB-RF-ETH-ng/stargazers) - Modernisierte Next-Generation-Firmware für die HB-RF-ETH Platine mit neuer Weboberfläche und MQTT-Monitoring.
* [HB-UNI-Sen-WEA](https://github.com/jp112sdl/HB-UNI-Sen-WEA) [![GitHub stars](https://img.shields.io/github/stars/jp112sdl/HB-UNI-Sen-WEA?style=flat)](https://github.com/jp112sdl/HB-UNI-Sen-WEA/stargazers) - Selbstbau-Wetterstation für HomeMatic.
* [Homematic Wired Hombrew Hardware](https://github.com/jfische) [![GitHub stars](https://img.shields.io/github/stars/jfische?style=flat)](https://github.com/jfische/stargazers) - Verschiedene Homebrew Sensoren/Aktoren für Homematic Wired.
* [stall.biz](https://www.stall.biz/) - 💵 Alternative Antennen, Multi Sensor für das Wohnzimmer, Wetterstation, ...


## CCU Addons

* [CCU Historian](https://ccu-historian.de/) - Langzeit Archiv und Graphen.
* [ccu-addon-mui](https://github.com/firsttris/ccu-addon-mui) [![GitHub stars](https://img.shields.io/github/stars/firsttris/ccu-addon-mui?style=flat)](https://github.com/firsttris/ccu-addon-mui/stargazers) - Moderne, responsive Progressive Web App (PWA) für die CCU3 mit integriertem WebSocket-Server.
* [CUxD](https://github.com/jens-maus/cuxd) [![GitHub stars](https://img.shields.io/github/stars/jens-maus/cuxd?style=flat)](https://github.com/jens-maus/cuxd/stargazers) - Der "Leatherman" für die CCU. Verbindet FS20, ... (💵 EnOcean, ...), stellt virtuelle Geräte und hilfreiche Tools zur Verfügung.
* [CUxD-Highcharts](https://github.com/homematic-community/CUxD-Highcharts) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/CUxD-Highcharts?style=flat)](https://github.com/homematic-community/CUxD-Highcharts/stargazers) - Visualisiert CUxD DEVLOGS mit Highcharts/Highstock (verwaist, Maintainer gesucht).
* [Email](https://github.com/homematic-community/hm_email) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hm_email?style=flat)](https://github.com/homematic-community/hm_email/stargazers) - HomeMatic CCU Addon für den Email Versand.
* [HAP-HomeMatic](https://github.com/thkl/hap-homematic) [![GitHub stars](https://img.shields.io/github/stars/thkl/hap-homematic?style=flat)](https://github.com/thkl/hap-homematic/stargazers) - OpenCCU / CCU3 addon to access your HomeMatic devices from HomeKit. Its much like https://github.com/thkl/homebridge-homematic but without homebridge (archived).
* [hm-influxdb2](https://github.com/cthil/hm-influxdb2) [![GitHub stars](https://img.shields.io/github/stars/cthil/hm-influxdb2?style=flat)](https://github.com/cthil/hm-influxdb2/stargazers) - Addon for the CCU3/OpenCCU to log data from devices into an InfluxDB2.
* [hm-print](https://github.com/homematic-community/hm-print) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hm-print?style=flat)](https://github.com/homematic-community/hm-print/stargazers) - CCU Programme drucken.
* [hm-sonos](https://github.com/homematic-community/hm-sonos) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hm-sonos?style=flat)](https://github.com/homematic-community/hm-sonos/stargazers) - HomeMatic CCU Addon zur Steuerung von Sonos Playern.
* [hm-tools](https://github.com/fhetty/hm-tools) [![GitHub stars](https://img.shields.io/github/stars/fhetty/hm-tools?style=flat)](https://github.com/fhetty/hm-tools/stargazers) - Sammlung von Tools für OpenCCU.
* [hm_pdetect](https://github.com/homematic-community/hm_pdetect) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hm_pdetect?style=flat)](https://github.com/homematic-community/hm_pdetect/stargazers) - Anwesenheitserkennung über die FRITZ!-Box
* [Homematic-addon-hue](https://github.com/j-a-n/homematic-addon-hue) [![GitHub stars](https://img.shields.io/github/stars/j-a-n/homematic-addon-hue?style=flat)](https://github.com/j-a-n/homematic-addon-hue/stargazers) - HomeMatic Addon für Philips Hue (archiviert).
* [homematic_check_mk](https://github.com/alexreinert/homematic_check_mk) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/homematic_check_mk?style=flat)](https://github.com/alexreinert/homematic_check_mk/stargazers) - Addon for the Homematic CCU2 or an OpenCCU device which acts as an check_mk_agent.
* [homematic-node-exporter](https://github.com/jaroschek/homematic-node-exporter) [![GitHub stars](https://img.shields.io/github/stars/jaroschek/homematic-node-exporter?style=flat)](https://github.com/jaroschek/homematic-node-exporter/stargazers) - Prometheus Node Exporter packaged as Addon for the Homematic CCU3 and OpenCCU.
* [HQ-WebUI](https://github.com/homematic-community/hq-webui) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hq-webui?style=flat)](https://github.com/homematic-community/hq-webui/stargazers) - Schnelles alternatives WebUI für die Homematic CCU mit Skript-Editor (verwaist, Maintainer gesucht).
* [JP-HB-Devices-addon](https://github.com/jp112sdl/JP-HB-Devices-addon) [![GitHub stars](https://img.shields.io/github/stars/jp112sdl/JP-HB-Devices-addon?style=flat)](https://github.com/jp112sdl/JP-HB-Devices-addon/stargazers) - Addon das über 80 Selbstbau-Geräte (AskSinPP HomeBrew) in die CCU/OpenCCU Firmware integriert.
* [jq](https://github.com/hobbyquaker/ccu-addon-jq) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/ccu-addon-jq?style=flat)](https://github.com/hobbyquaker/ccu-addon-jq/stargazers) - jq packaged as Addon for the Homematic CCU3.
* [Mosquitto](https://github.com/homematic-community/ccu-addon-mosquitto) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/ccu-addon-mosquitto?style=flat)](https://github.com/homematic-community/ccu-addon-mosquitto/stargazers) - Mosquitto packaged as Addon for the Homematic CCU3 and OpenCCU
* [Patcher](https://github.com/hobbyquaker/Patcher) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/Patcher?style=flat)](https://github.com/hobbyquaker/Patcher/stargazers) - CCU3 Addon zur komfortablen Anwendung von Patches.
* [Redis](https://github.com/hobbyquaker/ccu-addon-redis) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/ccu-addon-redis?style=flat)](https://github.com/hobbyquaker/ccu-addon-redis/stargazers) - Redis packaged as Addon for the Homematic CCU3 and OpenCCU
* [RedMatic](https://github.com/rdmtc/RedMatic) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/RedMatic?style=flat)](https://github.com/rdmtc/RedMatic/stargazers) - [Node-RED](https://nodered.org/) als Addon für die Homematic CCU3 und OpenCCU. Liefert u.A. komfortable HomeKit-Integration und spezielle Nodes zur Anbindung der CCU an MQTT mit.
* [ScriptParser](https://github.com/homematic-community/scriptparser) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/scriptparser?style=flat)](https://github.com/homematic-community/scriptparser/stargazers) - Addon zur Syntaxprüfung von HomeMatic Skripten.
* [WebMatic](https://github.com/ldittmar81/webmatic) [![GitHub stars](https://img.shields.io/github/stars/ldittmar81/webmatic?style=flat)](https://github.com/ldittmar81/webmatic/stargazers) - Alternative, für Mobilgeräte optimierte Bedienoberfläche, läuft direkt auf der CCU.
* [XML-API](https://github.com/homematic-community/XML-API) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/XML-API?style=flat)](https://github.com/homematic-community/XML-API/stargazers) - Vereinfachter CCU Zugriff via HTTP/XML.


## Interfacing Software

* [CCU-AI-MCP](https://github.com/mdzio/ccu-ai-mcp) [![GitHub stars](https://img.shields.io/github/stars/mdzio/ccu-ai-mcp?style=flat)](https://github.com/mdzio/ccu-ai-mcp/stargazers) - MCP-Server für OpenCCU/CCU, gibt KI-Assistenten (LLMs) über konfigurierbare HM-Skripte Zugriff auf das Smart Home.
* [CCU-Jack](https://github.com/mdzio/ccu-jack) [![GitHub stars](https://img.shields.io/github/stars/mdzio/ccu-jack?style=flat)](https://github.com/mdzio/ccu-jack/stargazers) - CCU-Jack bietet einen einfachen und sicheren REST-basierten Zugriff auf die CCU, auch als Addon verfügbar.
* [ccu-mcp](https://github.com/claymore666/ccu-mcp) [![GitHub stars](https://img.shields.io/github/stars/claymore666/ccu-mcp?style=flat)](https://github.com/claymore666/ccu-mcp/stargazers) - MCP server enabling AI assistants to control Homematic devices via the CCU's JSON-RPC API, no addon required.
* [hm2mqtt.js](https://github.com/hobbyquaker/hm2mqtt.js) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hm2mqtt.js?style=flat)](https://github.com/hobbyquaker/hm2mqtt.js/stargazers) - Node.js based interface between Homematic and MQTT.
* [homebridge-homematic](https://github.com/thkl/homebridge-homematic) [![GitHub stars](https://img.shields.io/github/stars/thkl/homebridge-homematic?style=flat)](https://github.com/thkl/homebridge-homematic/stargazers) - [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) Plugin zur Einbindung von Homematic Geräten in HomeKit.
* [homebridge-homematicip](https://github.com/marcsowen/homebridge-homematicip) [![GitHub stars](https://img.shields.io/github/stars/marcsowen/homebridge-homematicip?style=flat)](https://github.com/marcsowen/homebridge-homematicip/stargazers) - [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) Plugin zur Einbindung von Homematic IP mit HmIP-HAP via Cloud.
* [homematicip-hcu](https://github.com/Ediminator/homematicip-hcu) [![GitHub stars](https://img.shields.io/github/stars/Ediminator/homematicip-hcu?style=flat)](https://github.com/Ediminator/homematicip-hcu/stargazers) - [Home Assistant](https://www.home-assistant.io/) Integration zur lokalen Anbindung der Homematic IP Home Control Unit (HCU) ohne Cloud.
* [homematicip_local](https://github.com/SukramJ/homematicip_local) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/homematicip_local?style=flat)](https://github.com/SukramJ/homematicip_local/stargazers) - [Home Assistant](https://www.home-assistant.io/) Custom Component zur lokalen Anbindung von CCU/OpenCCU (Homematic und Homematic IP), basiert auf aiohomematic.
* [matterbridge-homematic](https://github.com/hobbyquaker/matterbridge-homematic) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/matterbridge-homematic?style=flat)](https://github.com/hobbyquaker/matterbridge-homematic/stargazers) - [Matterbridge](https://github.com/Luligu/matterbridge) [![GitHub stars](https://img.shields.io/github/stars/Luligu/matterbridge?style=flat)](https://github.com/Luligu/matterbridge/stargazers) Plugin to bridge a Homematic CCU's devices to the Matter ecosystem.
* [node-red-contrib-ccu](https://github.com/rdmtc/node-red-contrib-ccu) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/node-red-contrib-ccu?style=flat)](https://github.com/rdmtc/node-red-contrib-ccu/stargazers) - [Node-RED](https://nodered.org) Nodes for the Homematic CCU.
* [OpenCCU-Loom](https://github.com/SukramJ/openccu-loom) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/openccu-loom?style=flat)](https://github.com/SukramJ/openccu-loom/stargazers) - Standalone Go daemon bridging Homematic / Homematic IP CCUs to MQTT (with Home Assistant Discovery), REST + WebSocket, an MCP server and a native Matter bridge.
* [RedMatic-HomeKit](https://github.com/rdmtc/RedMatic-HomeKit) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/RedMatic-HomeKit?style=flat)](https://github.com/rdmtc/RedMatic-HomeKit/stargazers) - HAP-Nodejs basierte Node-RED Nodes um (Homematic-)Geräte in HomeKit einzubinden.
* [RedMatic-Matter](https://github.com/rdmtc/RedMatic-Matter) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/RedMatic-Matter?style=flat)](https://github.com/rdmtc/RedMatic-Matter/stargazers) - Matter.js basierte Node-RED Nodes, die Homematic-Geräte und beliebige Node-RED-Daten als Matter-Bridge bereitstellen.



## Misc Software

* [check_homematic](https://github.com/hobbyquaker/check_homematic) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/check_homematic?style=flat)](https://github.com/hobbyquaker/check_homematic/stargazers) - Nagios/Icinga Plugin for checking Homematic CCU.
* [godevccu](https://github.com/SukramJ/godevccu) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/godevccu?style=flat)](https://github.com/SukramJ/godevccu/stargazers) - Virtual HomeMatic CCU with XML-RPC and JSON-RPC servers written in Go, single static binary for testing integrations.
* [hm-buildroot](https://github.com/homematic-community/hm-buildroot) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hm-buildroot?style=flat)](https://github.com/homematic-community/hm-buildroot/stargazers) - Buildroot environments / cross compiler toolchains to build native applications for the CCU and OpenCCU.
* [HM-Explorer](https://github.com/thkl/HM-Explorer) [![GitHub stars](https://img.shields.io/github/stars/thkl/HM-Explorer?style=flat)](https://github.com/thkl/HM-Explorer/stargazers) - Electron based helper app for the Homematic CCU (macOS/Windows).
* [hm-simulator](https://github.com/hobbyquaker/hm-simulator) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hm-simulator?style=flat)](https://github.com/hobbyquaker/hm-simulator/stargazers) - Simulates (partly) a Homematic CCU.
* [hmcfgusb](https://git.zerfleddert.de/cgi-bin/gitweb.cgi/hmcfgusb) - Utilities to use the HM-CFG-USB(2) on Linux/Unix.
* [HMDeviceFirmware](https://github.com/OpenCCU/HMDeviceFirmware) [![GitHub stars](https://img.shields.io/github/stars/OpenCCU/HMDeviceFirmware?style=flat)](https://github.com/OpenCCU/HMDeviceFirmware/stargazers) - Archive of current and past firmware update files for HomeMatic and Homematic IP devices.
* [hmGetInfo](https://github.com/homematic-community/hmGetInfo) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/hmGetInfo?style=flat)](https://github.com/homematic-community/hmGetInfo/stargazers) - Collect paramsets and paramsetDescriptions from your Homematic CCU as JSON.
* [HMScriptEditor](https://zeezide.com/en/products/hmscripteditor/) - A very simple macOS editor and runner for HomeMatic ("Rega") scripts.
* [HomeHub](https://github.com/homematic-community/homehub) [![GitHub stars](https://img.shields.io/github/stars/homematic-community/homehub?style=flat)](https://github.com/homematic-community/homehub/stargazers) - PHP/XML-API basiertes Webfrontend. [Forum](https://homematic-forum.de/forum/viewtopic.php?f=41&t=50538)
* [Homematic Script Language](https://marketplace.visualstudio.com/items?itemName=HeadCrash.hmscript-language-vscode) - Visual Studio Code extension providing syntax highlighting for HomeMatic Script (.hms) files.
* [homematic-manager](https://github.com/hobbyquaker/homematic-manager) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homematic-manager?style=flat)](https://github.com/hobbyquaker/homematic-manager/stargazers) - Manage homematic interface processes (rfd/hs485d/homegear).
* [language-homematic](https://github.com/Ayngush/language-homematic) [![GitHub stars](https://img.shields.io/github/stars/Ayngush/language-homematic?style=flat)](https://github.com/Ayngush/language-homematic/stargazers) - Adds syntax highlighting and snippets to HomeMatic Script files in Atom.
* [pydevccu](https://github.com/SukramJ/pydevccu) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/pydevccu?style=flat)](https://github.com/SukramJ/pydevccu/stargazers) - Virtual HomeMatic CCU XML-RPC and JSON-RPC server with fake devices for development and testing.
* [ReGaHss-Test](https://github.com/OpenCCU/ReGaHss-Test) [![GitHub stars](https://img.shields.io/github/stars/OpenCCU/ReGaHss-Test?style=flat)](https://github.com/OpenCCU/ReGaHss-Test/stargazers) - Automated System Tests of ReGaHss - the HomeMatic (O)CCU "Logic Layer" (formerly occu-test).

## Software Modules

* [aiohomematic](https://github.com/SukramJ/aiohomematic) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/aiohomematic?style=flat)](https://github.com/SukramJ/aiohomematic/stargazers) - Python 3 interface to interact with Homematic devices via XML-RPC and JSON-RPC, successor of [pyhomematic](https://github.com/danielperna84/pyhomematic) [![GitHub stars](https://img.shields.io/github/stars/danielperna84/pyhomematic?style=flat)](https://github.com/danielperna84/pyhomematic/stargazers) and base of homematicip_local.
* [binrpc](https://github.com/hobbyquaker/binrpc) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/binrpc?style=flat)](https://github.com/hobbyquaker/binrpc/stargazers) - Xmlrpc_bin protocol client and server Node.js module.
* [go-hmccu](https://github.com/mdzio/go-hmccu) [![GitHub stars](https://img.shields.io/github/stars/mdzio/go-hmccu?style=flat)](https://github.com/mdzio/go-hmccu/stargazers) - Go library for interfacing the CCU.
* [hm-discover](https://github.com/hobbyquaker/hm-discover) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hm-discover?style=flat)](https://github.com/hobbyquaker/hm-discover/stargazers) - Node.js module to discover Homematic CCUs and interfaces.
* [Homematic IP Connect API](https://github.com/homematicip/connect-api) [![GitHub stars](https://img.shields.io/github/stars/homematicip/connect-api?style=flat)](https://github.com/homematicip/connect-api/stargazers) - Official WebSocket API and example plugins (Java, Node.js) for developing plugins for the Homematic IP Home Control Unit (HCU).
* [homematic-gqls](https://github.com/martin-riedl/homematic-gqls) [![GitHub stars](https://img.shields.io/github/stars/martin-riedl/homematic-gqls?style=flat)](https://github.com/martin-riedl/homematic-gqls/stargazers) - A GraphQL service to query Homematic IP components based on [homematicip-rest-api](https://github.com/hahn-th/homematicip-rest-api) [![GitHub stars](https://img.shields.io/github/stars/hahn-th/homematicip-rest-api?style=flat)](https://github.com/hahn-th/homematicip-rest-api/stargazers).
* [homematic-rega](https://github.com/hobbyquaker/homematic-rega) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homematic-rega?style=flat)](https://github.com/hobbyquaker/homematic-rega/stargazers) - Node.js Homematic CCU ReGaHSS Remote Script Interface.
* [homematic-xmlrpc](https://github.com/hobbyquaker/homematic-xmlrpc) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homematic-xmlrpc?style=flat)](https://github.com/hobbyquaker/homematic-xmlrpc/stargazers) - Xmlrpc client and server Node.js module.
* [homematicip-rest-api](https://github.com/hahn-th/homematicip-rest-api) [![GitHub stars](https://img.shields.io/github/stars/hahn-th/homematicip-rest-api?style=flat)](https://github.com/hahn-th/homematicip-rest-api/stargazers) - Python wrapper for the homematicIP REST API (Cloud / Access Point Based).
* [openccu-loom-client](https://github.com/SukramJ/openccu-loom-client) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/openccu-loom-client?style=flat)](https://github.com/SukramJ/openccu-loom-client/stargazers) - Async Python REST + WebSocket client for the OpenCCU-Loom daemon.
* [pmatic](https://github.com/LarsMichelsen/pmatic) [![GitHub stars](https://img.shields.io/github/stars/LarsMichelsen/pmatic?style=flat)](https://github.com/LarsMichelsen/pmatic/stargazers) - Python API for Homematic. Easy to use.

## Smart Home Software supporting Homematic

* [FHEM](https://fhem.de/) - via [HMCCU](https://wiki.fhem.de/wiki/HMCCU) Modul.
* [Home Assistant](https://www.home-assistant.io/) - via [homematicip_local](https://github.com/SukramJ/homematicip_local) [![GitHub stars](https://img.shields.io/github/stars/SukramJ/homematicip_local?style=flat)](https://github.com/SukramJ/homematicip_local/stargazers) (CCU/OpenCCU) oder [homematicip-hcu](https://github.com/Ediminator/homematicip-hcu) [![GitHub stars](https://img.shields.io/github/stars/Ediminator/homematicip-hcu?style=flat)](https://github.com/Ediminator/homematicip-hcu/stargazers) (HCU).
* [ioBroker](https://www.iobroker.net/?lang=de) - via [hm-rpc](https://github.com/ioBroker/ioBroker.hm-rpc) [![GitHub stars](https://img.shields.io/github/stars/ioBroker/ioBroker.hm-rpc?style=flat)](https://github.com/ioBroker/ioBroker.hm-rpc/stargazers) (Interface-Prozesse) und [hm-rega](https://github.com/ioBroker/ioBroker.hm-rega) [![GitHub stars](https://img.shields.io/github/stars/ioBroker/ioBroker.hm-rega?style=flat)](https://github.com/ioBroker/ioBroker.hm-rega/stargazers) (ReGaHSS) Adapter, [hmip](https://github.com/iobroker-community-adapters/ioBroker.hmip) [![GitHub stars](https://img.shields.io/github/stars/iobroker-community-adapters/ioBroker.hmip?style=flat)](https://github.com/iobroker-community-adapters/ioBroker.hmip/stargazers) für den Homematic IP Cloud Access Point.
* [IP-Symcon](https://www.symcon.de/) - 💵
* [Mediola](https://www.mediola.com/) - 💵
* [OpenHAB](https://www.openhab.org/) - via [Homematic Binding](https://www.openhab.org/addons/bindings/homematic/).
* [Pimatic](https://pimatic.org/)
* [SmartHomeNG](https://www.smarthomeng.de/) - via [Plugins](https://github.com/smarthomeNG/plugins) [![GitHub stars](https://img.shields.io/github/stars/smarthomeNG/plugins?style=flat)](https://github.com/smarthomeNG/plugins/stargazers).

## Misc

* [AskSinAnalyzer](https://github.com/jp112sdl/AskSinAnalyzer) [![GitHub stars](https://img.shields.io/github/stars/jp112sdl/AskSinAnalyzer?style=flat)](https://github.com/jp112sdl/AskSinAnalyzer/stargazers) - Funktelegramm-Dekodierer für den Einsatz in HomeMatic Umgebungen, hilfreich zur Fehlersuche, z.B. wenn der DutyCycle zu hoch ist.
* [AskSinAnalyzerXS](https://github.com/psi-4ward/AskSinAnalyzerXS) [![GitHub stars](https://img.shields.io/github/stars/psi-4ward/AskSinAnalyzerXS?style=flat)](https://github.com/psi-4ward/AskSinAnalyzerXS/stargazers) - AskSinAnalyzer als Desktop App, verzichtet auf den Einsatz eines ESP.
* [eagle-homematic](https://github.com/dersimn/eagle-homematic) [![GitHub stars](https://img.shields.io/github/stars/dersimn/eagle-homematic?style=flat)](https://github.com/dersimn/eagle-homematic/stargazers) - Homematic Modul Eagle Bibliothek.
* [Tablet Wallmount](https://homematic-forum.de/forum/viewtopic.php?f=18&t=49421) - Rahmen für Unterputzmontage von Tablets.
* [Homematic 3D Druck Collection auf Thingiverse](https://www.thingiverse.com/hobbyquaker/collections/homematic) - Diverse Teile rund um Homematic zum selbst drucken.


## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.


## License

[Public Domain CC0](https://creativecommons.org/publicdomain/zero/1.0/)
