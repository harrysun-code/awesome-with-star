# Homematic

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
* [Homematic Forum: HomeMatic - Tipps für Anfänger](https://homematic-forum.de/forum/viewtopic.php?f=31&t=22801) - Pflichtlektüre für Einsteiger von Sammy
* [Homematic Guru](https://homematic-guru.de/) - News, Blog, Tutorials und mehr.
* [Homematic Inside](https://www.homematic-inside.de/) - News, Blog, Tutorials und mehr.
* [Homematic Blog Lison](https://homematic-blog.lison.ch/) - Blog, Tutorials und mehr..
* [Technikkram](https://technikkram.net) - News, Blog, Tutorials und mehr.
* [OwnSmartHome](https://ownsmarthome.de/category/homematic/) - News, Blog, Tutorials und mehr.
* [Verdrahtet](https://www.verdrahtet.info/) - News, Blog, Youtube, Tutorials, ...
* [Wikimatic](http://www.wikimatic.de/wiki/Hauptseite) - Community Wiki.


## Documentation

* [Dissecting HomeMatic AES](https://git.zerfleddert.de/hmcfgusb/AES/) - BidCos Protocol AES Handshake description.
* [Direktverknüpfungen im Expertenmodus](https://www.youtube.com/watch?v=1B4iwtK1Rmo) - Vortrag von Frank Grass.
* [Virtuelle Aktorkanäle](https://www.youtube.com/watch?v=Cwxwtig6Q1I) - Vortrag von Frank Grass.
* [Script Documentation](http://www.wikimatic.de/wiki/Script_Dokumentation) - Inoffizielle Homematic Script Referenz.
* [Keymatic Konfiguration](https://homematic-forum.de/forum/viewtopic.php?f=31&t=19196) - Beitrag von rewe0815 im Homematic Forum.

## Mobile Apps

* [@home](https://www.athomeapp.de/) - iOS - (💵 inApp-Purchase um Werbung zu entfernen)
* [HistClient](https://www.sa-com.de/smarthome-special/histclient-handbuch/) - (💵 inApp-Purchase) - CCU-Historian Client mit erweitereten Features für iOS und Android
* [Home-24](http://www.home-24.net/index.php?page=sites/home.php&app=home24) - 💵 Android 
* [HomeControl](http://www.ksquare.de/myhomecontrol/) - 💵 iOS
* [TinyMatic](https://www.tinymatic.de/) - 💵 Android (ehemals: HomeDroid)
* [Pocket Control](https://www.penzler.de) - 💵 iOS
* [Battery Status for HomeMatic](https://zeezide.com/en/products/hmbattery/) - 💵 iOS


## CCU Alternatives

* [debmatic](https://github.com/alexreinert/debmatic) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/debmatic?style=flat)](https://github.com/alexreinert/debmatic/stargazers) - Install the Homematic OCCU on Debian based amd64, armhf and arm64 systems (Debian, Ubuntu, Raspbian, Armbian)
* [docker-ccu](https://github.com/angelnu/docker-ccu) [![GitHub stars](https://img.shields.io/github/stars/angelnu/docker-ccu?style=flat)](https://github.com/angelnu/docker-ccu/stargazers) - Homematic CCU firmware running as [Docker](https://www.docker.com) container on arm and (emulated) x86.
* [Homegear](https://homegear.eu/index.php/Main_Page) - Free and open source program to interface your smart home devices with your home automation software or your own scripts.
* [piVCCU](https://github.com/alexreinert/piVCCU) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/piVCCU?style=flat)](https://github.com/alexreinert/piVCCU/stargazers) - Install the original Homematic CCU firmware inside a virtualized container (lxc) on Raspbian or Armbian.
* [RaspberryMatic](https://github.com/jens-maus/RaspberryMatic) [![GitHub stars](https://img.shields.io/github/stars/jens-maus/RaspberryMatic?style=flat)](https://github.com/jens-maus/RaspberryMatic/stargazers) - Lightweight, OCCU and Linux/buildroot-based distribution for running a HomeMatic CCU on embedded devices like the RaspberryPi.


## Alternative Sensors, Actuators and Hardware Modifications

* [AskSinPPCollection](https://jp112sdl.github.io/AskSinPPCollection/) - Einführung, Dokumentation und Projekte rund um Selbstbau-Komponenten mit AskSinPP
* [Beispiel_AskSinPP](https://github.com/jp112sdl/Beispiel_AskSinPP) [![GitHub stars](https://img.shields.io/github/stars/jp112sdl/Beispiel_AskSinPP?style=flat)](https://github.com/jp112sdl/Beispiel_AskSinPP/stargazers) - Beispiel Sketche für die Verwendung der [AskSinPP](https://github.com/pa-pa/AskSinPP) [![GitHub stars](https://img.shields.io/github/stars/pa-pa/AskSinPP?style=flat)](https://github.com/pa-pa/AskSinPP/stargazers) Bibliothek
* [HAUS-BUS.DE](http://www.haus-bus.de/) - 💵 Homematic Wired kompatible Geräte.
* [Homematic Wired Hombrew Hardware](https://github.com/jfische) [![GitHub stars](https://img.shields.io/github/stars/jfische?style=flat)](https://github.com/jfische/stargazers) - Verschiedene Homebrew Sensoren/Aktoren für Homematic Wired.
* [stall.biz](https://www.stall.biz/) - 💵 Alternative Antennen, Multi Sensor für das Wohnzimmer, Wetterstation, ...


## CCU Addons

* [CCU Historian](https://ccu-historian.de/) - Langzeit Archiv und Graphen.
* [CUxD](https://www.homematic-inside.de/software/tag/Zusatzsoftware ) - Der "Leatherman" für die CCU. Verbindet FS20, ... (💵 EnOcean, ...), stellt virtuelle Geräte und hilfreiche Tools zur Verfügung.
* [Email](https://github.com/jens-maus/hm_email) [![GitHub stars](https://img.shields.io/github/stars/jens-maus/hm_email?style=flat)](https://github.com/jens-maus/hm_email/stargazers) - HomeMatic CCU Addon für den Email Versand.
* [HAP-HomeMatic](https://github.com/thkl/hap-homematic) [![GitHub stars](https://img.shields.io/github/stars/thkl/hap-homematic?style=flat)](https://github.com/thkl/hap-homematic/stargazers) - RaspberryMatic / CCU3 addon to access your HomeMatic devices from HomeKit. Its much like https://github.com/thkl/homebridge-homematic but without homebridge.
* [hm-print](https://github.com/litti/hm-print) [![GitHub stars](https://img.shields.io/github/stars/litti/hm-print?style=flat)](https://github.com/litti/hm-print/stargazers) - CCU Programme drucken.
* [hm-tools](https://github.com/fhetty/hm-tools) [![GitHub stars](https://img.shields.io/github/stars/fhetty/hm-tools?style=flat)](https://github.com/fhetty/hm-tools/stargazers) - Sammlung von Tools für RaspberryMatic.
* [hm_pdetect](https://github.com/jens-maus/hm_pdetect) [![GitHub stars](https://img.shields.io/github/stars/jens-maus/hm_pdetect?style=flat)](https://github.com/jens-maus/hm_pdetect/stargazers) - Anwesenheitserkennung über die FRITZ!-Box
* [Homeputer](https://www.contronics.de/shop/HomeMatic-System/Zentralen-und-Software.html) - 💵
* [Homematic-addon-hue](https://github.com/j-a-n/homematic-addon-hue) [![GitHub stars](https://img.shields.io/github/stars/j-a-n/homematic-addon-hue?style=flat)](https://github.com/j-a-n/homematic-addon-hue/stargazers) - HomeMatic Addon für Philips Hue.
* [homematic_check_mk](https://github.com/alexreinert/homematic_check_mk) [![GitHub stars](https://img.shields.io/github/stars/alexreinert/homematic_check_mk?style=flat)](https://github.com/alexreinert/homematic_check_mk/stargazers) - Addon for the Homematic CCU2 or a Raspberrymatic device which acts as an check_mk_agent.
* [jq](https://github.com/hobbyquaker/ccu-addon-jq) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/ccu-addon-jq?style=flat)](https://github.com/hobbyquaker/ccu-addon-jq/stargazers) - jq packaged as Addon for the Homematic CCU3.
* [Mosquitto](https://github.com/hobbyquaker/ccu-addon-mosquitto) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/ccu-addon-mosquitto?style=flat)](https://github.com/hobbyquaker/ccu-addon-mosquitto/stargazers) - Mosquitto packaged as Addon for the Homematic CCU3 and RaspberryMatic
* [Patcher](https://github.com/hobbyquaker/Patcher) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/Patcher?style=flat)](https://github.com/hobbyquaker/Patcher/stargazers) - CCU3 Addon zur komfortablen Anwendung von Patches.
* [rmupdate](https://github.com/j-a-n/raspberrymatic-addon-rmupdate) [![GitHub stars](https://img.shields.io/github/stars/j-a-n/raspberrymatic-addon-rmupdate?style=flat)](https://github.com/j-a-n/raspberrymatic-addon-rmupdate/stargazers) - RaspberryMatic Addon das RaspberryMatic selbst aktualisieren kann, vereinfacht die WLAN Konfiguration mit GUI und kann andere Addons ohne Zwangsreboot installieren und aktualisieren
* [Redis](https://github.com/hobbyquaker/ccu-addon-redis) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/ccu-addon-redis?style=flat)](https://github.com/hobbyquaker/ccu-addon-redis/stargazers) - Redis packaged as Addon for the Homematic CCU3 and RaspberryMatic
* [RedMatic](https://github.com/rdmtc/RedMatic) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/RedMatic?style=flat)](https://github.com/rdmtc/RedMatic/stargazers) - [Node-RED](https://nodered.org/) als Addon für die Homematic CCU3 und RaspberryMatic. Liefert u.A. komfortable HomeKit-Integration und spezielle Nodes zur Anbindung der CCU an MQTT mit.
* [XML-API](https://github.com/hobbyquaker/xml-api) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/xml-api?style=flat)](https://github.com/hobbyquaker/xml-api/stargazers) - Vereinfachter CCU Zugriff via HTTP/XML.


## Interfacing Software

* [CCU-Jack](https://github.com/mdzio/ccu-jack) [![GitHub stars](https://img.shields.io/github/stars/mdzio/ccu-jack?style=flat)](https://github.com/mdzio/ccu-jack/stargazers) - CCU-Jack bietet einen einfachen und sicheren REST-basierten Zugriff auf die CCU, auch als Addon verfügbar.
* [homebridge-homematic](https://github.com/thkl/homebridge-homematic) [![GitHub stars](https://img.shields.io/github/stars/thkl/homebridge-homematic?style=flat)](https://github.com/thkl/homebridge-homematic/stargazers) - [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) Plugin zur Einbindung von Homematic Geräten in HomeKit.
* [homebridge-homematicip](https://github.com/marcsowen/homebridge-homematicip) [![GitHub stars](https://img.shields.io/github/stars/marcsowen/homebridge-homematicip?style=flat)](https://github.com/marcsowen/homebridge-homematicip/stargazers) - [Homebridge](https://github.com/nfarina/homebridge) [![GitHub stars](https://img.shields.io/github/stars/nfarina/homebridge?style=flat)](https://github.com/nfarina/homebridge/stargazers) Plugin zur Einbindung von Homematic IP mit HmIP-HAP via Cloud.
* [hvl - Homematic Virtual Interface](https://github.com/thkl/Homematic-Virtual-Interface) [![GitHub stars](https://img.shields.io/github/stars/thkl/Homematic-Virtual-Interface?style=flat)](https://github.com/thkl/Homematic-Virtual-Interface/stargazers) - Bindet Fremdgeräte (z.B. Hue, Harmony, Netatmo, Sonos) über Plugins ein, auch als Addon verfügbar.
* [node-red-contrib-ccu](https://github.com/rdmtc/node-red-contrib-ccu) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/node-red-contrib-ccu?style=flat)](https://github.com/rdmtc/node-red-contrib-ccu/stargazers) - [Node-RED](https://nodered.org) Nodes for the Homematic CCU.



## Misc Software

* [check_homematic](https://github.com/hobbyquaker/check_homematic) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/check_homematic?style=flat)](https://github.com/hobbyquaker/check_homematic/stargazers) - Nagios/Icinga Plugin for checking Homematic CCU.
* [hm-simulator](https://github.com/hobbyquaker/hm-simulator) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hm-simulator?style=flat)](https://github.com/hobbyquaker/hm-simulator/stargazers) - Simulates (partly) a Homematic CCU.
* [hmcfgusb](https://git.zerfleddert.de/cgi-bin/gitweb.cgi/hmcfgusb) - Utilities to use the HM-CFG-USB(2) on Linux/Unix.
* [HomeHub](https://github.com/Gerti1972/homehub) [![GitHub stars](https://img.shields.io/github/stars/Gerti1972/homehub?style=flat)](https://github.com/Gerti1972/homehub/stargazers) - PHP/XML-API basiertes Webfrontend. [Forum](https://homematic-forum.de/forum/viewtopic.php?f=41&t=50538)
* [homematic-manager](https://github.com/hobbyquaker/homematic-manager) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homematic-manager?style=flat)](https://github.com/hobbyquaker/homematic-manager/stargazers) - Manage homematic interface processes (rfd/hs485d/homegear).
* [language-homematic](https://github.com/Ayngush/language-homematic) [![GitHub stars](https://img.shields.io/github/stars/Ayngush/language-homematic?style=flat)](https://github.com/Ayngush/language-homematic/stargazers) - Adds syntax highlighting and snippets to HomeMatic Script files in Atom.
* [occu-test](https://github.com/hobbyquaker/occu-test) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/occu-test?style=flat)](https://github.com/hobbyquaker/occu-test/stargazers) - Automated System Tests of ReGaHss - the HomeMatic (O)CCU "Logic Layer".
* [HMScriptEditor](https://zeezide.com/en/products/hmscripteditor/) - A very simple macOS editor and runner for HomeMatic ("Rega") scripts.

## Software Modules

* [binrpc](https://github.com/hobbyquaker/binrpc) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/binrpc?style=flat)](https://github.com/hobbyquaker/binrpc/stargazers) - Xmlrpc_bin protocol client and server Node.js module.
* [hm-discover](https://github.com/hobbyquaker/hm-discover) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hm-discover?style=flat)](https://github.com/hobbyquaker/hm-discover/stargazers) - Node.js module to discover Homematic CCUs and interfaces.
* [homematic-rega](https://github.com/hobbyquaker/homematic-rega) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homematic-rega?style=flat)](https://github.com/hobbyquaker/homematic-rega/stargazers) - Node.js Homematic CCU ReGaHSS Remote Script Interface.
* [homematicip-rest-api](https://github.com/coreGreenberet/homematicip-rest-api) [![GitHub stars](https://img.shields.io/github/stars/coreGreenberet/homematicip-rest-api?style=flat)](https://github.com/coreGreenberet/homematicip-rest-api/stargazers) - Python wrapper for the homematicIP REST API (Cloud / Access Point Based).
* [homematic-gqls](https://github.com/martin-riedl/homematic-gqls) [![GitHub stars](https://img.shields.io/github/stars/martin-riedl/homematic-gqls?style=flat)](https://github.com/martin-riedl/homematic-gqls/stargazers) - A GraphQL service to query Homematic IP components based on [homematicip-rest-api](https://github.com/coreGreenberet/homematicip-rest-api) [![GitHub stars](https://img.shields.io/github/stars/coreGreenberet/homematicip-rest-api?style=flat)](https://github.com/coreGreenberet/homematicip-rest-api/stargazers).
* [homematic-xmlrpc](https://github.com/hobbyquaker/homematic-xmlrpc) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homematic-xmlrpc?style=flat)](https://github.com/hobbyquaker/homematic-xmlrpc/stargazers) - Xmlrpc client and server Node.js module.
* [pmatic](https://github.com/LarsMichelsen/pmatic) [![GitHub stars](https://img.shields.io/github/stars/LarsMichelsen/pmatic?style=flat)](https://github.com/LarsMichelsen/pmatic/stargazers) - Python API for Homematic. Easy to use.
* [pyhomematic](https://github.com/danielperna84/pyhomematic) [![GitHub stars](https://img.shields.io/github/stars/danielperna84/pyhomematic?style=flat)](https://github.com/danielperna84/pyhomematic/stargazers) - Python 3 Interface to interact with Homematic devices.

## Smart Home Software supporting Homematic

* [everHome](https://everhome.de) - 💵
* [FHEM](https://fhem.de/)
* [Home Assistant](https://www.home-assistant.io/)
* [ioBroker](https://www.iobroker.net/?lang=de)
* [IP-Symcon](https://www.symcon.de/) - 💵
* [Mediola](https://www.mediola.com/) - 💵
* [OpenHAB](https://www.openhab.org/)
* [Pimatic](https://pimatic.org/)

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
