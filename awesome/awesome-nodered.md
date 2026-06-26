# Node-RED

[![GitHub stars](https://img.shields.io/github/stars/naimo84/awesome-nodered?style=flat)](https://github.com/naimo84/awesome-nodered/stargazers)

# Awesome Node-RED [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <a href="https://nodered.org/"><img src="https://nodered.org/about/resources/media/node-red-hexagon.png" width="200" align="right" alt="Node-RED"></a>

> Curated list of useful resources for Node-RED.

[Node-RED](https://nodered.org/) is a programming tool for wiring together hardware devices, APIs and online services in new and interesting ways.

It provides a browser-based editor that makes it easy to wire together flows using the wide range of nodes in the palette that can be deployed to its runtime in a single-click.

## Contents

- [Installation](#installation)
- [Documentation](#documentation)
- [Nodes](#nodes)
    - [Analysis](#analysis)
    - [Database](#database)
    - [Development](#development)
    - [Function](#function)
    - [Hardware](#hardware)
    - [I/O](#io)
    - [Image processing](#image-processing)
    - [Parsers](#parsers)
    - [Smarthome](#smarthome)
    - [Social](#social)
    - [System](#system)
    - [Time](#time)
    - [Utility](#utility)
    - [UI](#ui)
- [Community](#community)

## Installation

- [Running locally](https://nodered.org/docs/getting-started/local)
- [Running under Docker](https://github.com/node-red/node-red-docker) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-docker?style=flat)](https://github.com/node-red/node-red-docker/stargazers)
- [c't-Smart-Home](https://github.com/ct-Open-Source/ct-Smart-Home) [![GitHub stars](https://img.shields.io/github/stars/ct-Open-Source/ct-Smart-Home?style=flat)](https://github.com/ct-Open-Source/ct-Smart-Home/stargazers) - A ready-to-use setup for home automation maintained by [german computer magazine c't](https://www.ct.de/smarthome).
- [Home Assistant Community Add-on](https://community.home-assistant.io/t/home-assistant-community-add-on-node-red/55023) - Starts an instance within Home Assistant and communicates with it.
- [ioBroker node-red Adapter](https://github.com/ioBroker/ioBroker.node-red) [![GitHub stars](https://img.shields.io/github/stars/ioBroker/ioBroker.node-red?style=flat)](https://github.com/ioBroker/ioBroker.node-red/stargazers) - Starts an instance within ioBroker and communicates with it.
- [openHAB running on openHABian](https://www.openhab.org/docs/installation/openhabian.html#optional-components) - Install Node-RED using openhab-config from command line, choose it from "Optional Components".
- [RedMatic](https://github.com/rdmtc/RedMatic/wiki/Installation) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/RedMatic/wiki/Installation?style=flat)](https://github.com/rdmtc/RedMatic/wiki/Installation/stargazers) - Install Node-RED on a CCU3, smart home automation hardware from the manufacturer eQ-3, popular especially in Germany.

## Documentation

- [Getting Started](https://nodered.org/docs/getting-started/)
- [FAQ](https://nodered.org/docs/faq/)
- [Tutorials](https://nodered.org/docs/tutorials/)
- [User Guide](https://nodered.org/docs/user-guide/)
## Nodes

### Analysis

- [badwords](https://github.com/node-red/node-red-nodes/tree/master/analysis/swearfilter) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/analysis/swearfilter?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/analysis/swearfilter/stargazers) - Analyses the payload and tries to filter out any messages containing bad swear words. This only operates on payloads of type string. Everything else is blocked.
- [wordpos](https://github.com/node-red/node-red-nodes/tree/master/analysis/wordpos) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/analysis/wordpos?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/analysis/wordpos/stargazers) - Analyses the payload and classifies the part-of-speech of each word. The resulting message has msg.pos added with the results. A word may appear in multiple categories (eg, 'great' is both a noun and an adjective).

### Database

- [influxdb](https://github.com/mblackstock/node-red-contrib-influxdb) [![GitHub stars](https://img.shields.io/github/stars/mblackstock/node-red-contrib-influxdb?style=flat)](https://github.com/mblackstock/node-red-contrib-influxdb/stargazers) - Save and query data from an InfluxDB time series database.
- [mssql-plus](https://github.com/bestlong/node-red-contrib-mssql-plus) [![GitHub stars](https://img.shields.io/github/stars/bestlong/node-red-contrib-mssql-plus?style=flat)](https://github.com/bestlong/node-red-contrib-mssql-plus/stargazers) - Execute queries, stored procedures and bulk inserts in Microsoft SQL Server and Azure Databases SQL2000 ~ SQL2019.
- [stackhero-influxdb-v2](https://github.com/stackhero-io/node-red-contrib-stackhero-influxdb-v2) [![GitHub stars](https://img.shields.io/github/stars/stackhero-io/node-red-contrib-stackhero-influxdb-v2?style=flat)](https://github.com/stackhero-io/node-red-contrib-stackhero-influxdb-v2/stargazers) - Save and query data from an InfluxDB v2 time series database.
- [stackhero-mysql](https://github.com/stackhero-io/node-red-contrib-stackhero-mysql) [![GitHub stars](https://img.shields.io/github/stars/stackhero-io/node-red-contrib-stackhero-mysql?style=flat)](https://github.com/stackhero-io/node-red-contrib-stackhero-mysql/stargazers) - Connect to a MySQL or a MariaDB database, using TLS (SSL) and compatible with "Caching SHA2 password" authentication method (MySQL >= 8).
- [leveldb](https://github.com/node-red/node-red-nodes/tree/master/storage/leveldb) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/storage/leveldb?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/storage/leveldb/stargazers) - Uses LevelDB for a simple key value pair database.
- [mysql](https://github.com/node-red/node-red-nodes/tree/master/storage/mysql) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/storage/mysql?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/storage/mysql/stargazers) - Allows basic access to a MySQL database. 
- [sqlite](https://github.com/node-red/node-red-nodes/tree/master/storage/sqlite) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/storage/sqlite?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/storage/sqlite/stargazers) - Supports read and write to a local sqlite database.

### Development

- [typescript-starter](https://github.com/alexk111/node-red-node-typescript-starter) [![GitHub stars](https://img.shields.io/github/stars/alexk111/node-red-node-typescript-starter?style=flat)](https://github.com/alexk111/node-red-node-typescript-starter/stargazers) - Quick-start template repository for creating new node sets in TypeScript.

### Function

- [datagenerater](https://github.com/node-red/node-red-nodes/tree/master/function/datagenerator) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/function/datagenerator?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/function/datagenerator/stargazers) - Generate dummy data in various formats, names, addresses, emails, numbers, words, etc.
- [pidcontrol](https://github.com/node-red/node-red-nodes/tree/master/function/PID) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/function/PID?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/function/PID/stargazers) - A PID control node for numeric inputs - provides simple controll loop feedback capability.
- [random](https://github.com/node-red/node-red-nodes/tree/master/function/random) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/function/random?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/function/random/stargazers) - Random number generator - can generate integers for x to y - or floats between x and y.
- [rbe](https://github.com/node-red/node-red-nodes/tree/master/function/rbe) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/function/rbe?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/function/rbe/stargazers) - Provide report by exception and deadband / bandgap capability for simple inputs.
- [smooth](https://github.com/node-red/node-red-nodes/tree/master/function/smooth) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/function/smooth?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/function/smooth/stargazers) - Provide various functions across several previous values, including max, min, mean, high and low pass filters.

### Hardware

- [arduino](https://github.com/node-red/node-red-nodes/tree/master/hardware/Arduino) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/Arduino?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/Arduino/stargazers) - Uses firmata protocol to talk to the board.
- [beaglebone](https://github.com/node-red/node-red-nodes/tree/master/hardware/BBB) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/BBB?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/BBB/stargazers) - Nodes for the [Beaglebone Black](https://beagleboard.org/black).
- [blink1](https://github.com/node-red/node-red-nodes/tree/master/hardware/blink1) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/blink1?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/blink1/stargazers) - [Blink1](https://blink1.thingm.com/) USB LED from ThingM.
- [blinkstick](https://github.com/node-red/node-red-nodes/tree/master/hardware/blinkstick) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/blinkstick?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/blinkstick/stargazers) - [BlinkStick](https://www.blinkstick.com/) USB LED device.
- [digirgb](https://github.com/node-red/node-red-nodes/tree/master/hardware/digiRGB) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/digiRGB?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/digiRGB/stargazers) - DigiSpark RGB USB LED.
- [heatmiser](https://github.com/node-red/node-red-nodes/tree/master/hardware/heatmiser) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/heatmiser?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/heatmiser/stargazers) - Temperature and frost protection for Heatmiser thermostats.
- [intel-galileo](https://github.com/node-red/node-red-nodes/tree/master/hardware/intel) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/intel?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/intel/stargazers) - A collection for the Intel Galileo and Edison.
- [ledborg](https://github.com/node-red/node-red-nodes/tree/master/hardware/LEDborg) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/LEDborg?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/LEDborg/stargazers) - [LEDborg](https://www.piborg.org/ledborg) plug on module.
- [makeymakey](https://github.com/node-red/node-red-nodes/tree/master/hardware/makey) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/makey?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/makey/stargazers) - Read from a [MakeyMakey](http://www.makeymakey.com/) input device.
- [pi-gpiod](https://github.com/node-red/node-red-nodes/tree/master/hardware/pigpiod) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/pigpiod?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/pigpiod/stargazers) - An alternative to the default PI GPIO nodes that allows remote access.
- [pi-mcp3008](https://github.com/node-red/node-red-nodes/tree/master/hardware/mcp3008) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/mcp3008?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/mcp3008/stargazers) - Read from MCP300x series Analogue to Digital Converter chips via the SPI bus.
- [pi-neopixel](https://github.com/node-red/node-red-nodes/tree/master/hardware/neopixel) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/neopixel?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/neopixel/stargazers) - Drive a strip of NeoPixels directly.
- [pi-unicorn-hat](https://github.com/node-red/node-red-nodes/tree/master/hardware/unicorn) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/unicorn?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/unicorn/stargazers) - Controls a Pimorini Unicorn HAT 8x8 LED display.
- [pibrella](https://github.com/node-red/node-red-nodes/tree/master/hardware/Pibrella) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/Pibrella?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/Pibrella/stargazers) - Controls a [Pibrella](https://pibrella.com/) add-on board.
- [piface](https://github.com/node-red/node-red-nodes/tree/master/hardware/PiFace) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/PiFace?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/PiFace/stargazers) - [PiFace](https://www.piface.org.uk/) interface module.
- [piliter](https://github.com/node-red/node-red-nodes/tree/master/hardware/PiLiter) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/PiLiter?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/PiLiter/stargazers) - Controls a Pimorini Pi-LITEr 8 LED add-on board.
- [sensortag](https://github.com/node-red/node-red-nodes/tree/master/hardware/sensorTag) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/sensorTag?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/sensorTag/stargazers) - Reads data from the Ti Bluetooth Low Energy SensorTag device.
- [wemo](https://github.com/node-red/node-red-nodes/tree/master/hardware/wemo) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/wemo?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/wemo/stargazers) - Drive a [WeMo](https://www.belkin.com/us/Products/home-automation/c/wemo-home-automation/) socket and switch.
- [scanBLE](https://github.com/node-red/node-red-nodes/tree/master/hardware/scanBLE) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/hardware/scanBLE?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/hardware/scanBLE/stargazers) - Scans for a particular Bluetooth Low Energy device.

### I/O

- [discovery](https://github.com/node-red/node-red-nodes/tree/master/io/mdns) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/mdns?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/mdns/stargazers) - Discovers other Avahi/Bonjour services on the network.
- [emoncms](https://github.com/node-red/node-red-nodes/tree/master/io/emoncms) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/emoncms?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/emoncms/stargazers) - Post to an [Emoncms](https://emoncms.org/) server.
- [noble-bluetooth](https://github.com/clausbroch/node-red-contrib-noble-bluetooth) [![GitHub stars](https://img.shields.io/github/stars/clausbroch/node-red-contrib-noble-bluetooth?style=flat)](https://github.com/clausbroch/node-red-contrib-noble-bluetooth/stargazers) - Based on noble for interaction with Bluetooth Low Energy devices.
- [mindconnect](https://github.com/mindsphere/node-red-contrib-mindconnect) [![GitHub stars](https://img.shields.io/github/stars/mindsphere/node-red-contrib-mindconnect?style=flat)](https://github.com/mindsphere/node-red-contrib-mindconnect/stargazers) - Upload timeseries, files and events to MindSphere.
- [modbus](https://github.com/biancoroyal/node-red-contrib-modbus) [![GitHub stars](https://img.shields.io/github/stars/biancoroyal/node-red-contrib-modbus?style=flat)](https://github.com/biancoroyal/node-red-contrib-modbus/stargazers) - All in one Modbus TCP and Serial package.
- [mqlight](https://github.com/node-red/node-red-nodes/tree/master/io/mqlight) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/mqlight?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/mqlight/stargazers) - Adds nodes to send and receive using MQlight.
- [ping](https://github.com/node-red/node-red-nodes/tree/master/io/ping) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/ping?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/ping/stargazers) - Pings a machine and returns the trip time in mS.
- [s7](https://github.com/st-one-io/node-red-contrib-s7) [![GitHub stars](https://img.shields.io/github/stars/st-one-io/node-red-contrib-s7?style=flat)](https://github.com/st-one-io/node-red-contrib-s7/stargazers) - Interact with Siemens S7 PLCs.
- [serialport](https://github.com/node-red/node-red-nodes/tree/master/io/serialport) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/serialport?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/serialport/stargazers) - Send messages to and receive messages from a physical serial port.
- [snmp](https://github.com/node-red/node-red-nodes/tree/master/io/snmp) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/snmp?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/snmp/stargazers) - SNMP receivers for single OIDs or OID tables.
- [stomp](https://github.com/node-red/node-red-nodes/tree/master/io/stomp) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/stomp?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/stomp/stargazers) - Publish and subscribe to and from a [STOMP server](https://stomp.github.io/implementations.html#STOMP_Servers).
- [wol](https://github.com/node-red/node-red-nodes/tree/master/io/wol) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/io/wol?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/io/wol/stargazers) - Sends a Wake-On-LAN magic packet to the mac address specified.
- [xiaomi-ble](https://github.com/eschava/node-red-contrib-xiaomi-ble) [![GitHub stars](https://img.shields.io/github/stars/eschava/node-red-contrib-xiaomi-ble?style=flat)](https://github.com/eschava/node-red-contrib-xiaomi-ble/stargazers) - Single "Xiaomi BLE" node that gets all known data from Xiaomi BLE (Bluetooth 4).

### Image processing

- [image-output](https://github.com/rikukissa/node-red-contrib-image-output) [![GitHub stars](https://img.shields.io/github/stars/rikukissa/node-red-contrib-image-output?style=flat)](https://github.com/rikukissa/node-red-contrib-image-output/stargazers) - Simple image output node. Useful for previewing images (of face detecting, object recognition etc.) inside the flow editor.
- [image-tools](https://flows.nodered.org/node/node-red-contrib-image-tools) - Editing images, building and decoding 2D and 3D barcodes.

### Parsers

- [base64](https://github.com/node-red/node-red-nodes/tree/master/parsers/base64) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/parsers/base64?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/parsers/base64/stargazers) - Converts a payload to/from base64 encoded format.
- [buffer-parser](https://flows.nodered.org/node/node-red-contrib-buffer-parser) - Converts values to and from buffer/array. Supports Big/Little Endian, BCD, byte swapping and much more.
- [geohash](https://github.com/node-red/node-red-nodes/tree/master/parsers/geohash) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/parsers/geohash?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/parsers/geohash/stargazers) - Converts a lat, lon payload to/from geohash format.
- [msgpack](https://github.com/node-red/node-red-nodes/tree/master/parsers/msgpack) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/parsers/msgpack?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/parsers/msgpack/stargazers) - Converts a payload to/from msgpack binary packed format.
- [what3words](https://github.com/node-red/node-red-nodes/tree/master/parsers/what3words) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/parsers/what3words?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/parsers/what3words/stargazers) - Encodes or Decodes a lat, lon position into what3words text format.

### Smarthome

- [alexa-home](https://github.com/mabunixda/node-red-contrib-alexa-home) [![GitHub stars](https://img.shields.io/github/stars/mabunixda/node-red-contrib-alexa-home?style=flat)](https://github.com/mabunixda/node-red-contrib-alexa-home/stargazers) - Connect with Alexa just wihtin the local network - no extra cloud stuff is required.
- [alexa-home-skill-v3](https://github.com/coldfire84/node-red-contrib-alexa-home-skill-v3) [![GitHub stars](https://img.shields.io/github/stars/coldfire84/node-red-contrib-alexa-home-skill-v3?style=flat)](https://github.com/coldfire84/node-red-contrib-alexa-home-skill-v3/stargazers) - Controls things via Alexa and Google Home.
    - [alexa-home-skill-v3-web](https://github.com/coldfire84/node-red-alexa-home-skill-v3-web) [![GitHub stars](https://img.shields.io/github/stars/coldfire84/node-red-alexa-home-skill-v3-web?style=flat)](https://github.com/coldfire84/node-red-alexa-home-skill-v3-web/stargazers) - Web Service for Alexa and Google Home.
    - [alexa-home-skill-v3-lambda](https://github.com/coldfire84/node-red-alexa-home-skill-v3-lambda) [![GitHub stars](https://img.shields.io/github/stars/coldfire84/node-red-alexa-home-skill-v3-lambda?style=flat)](https://github.com/coldfire84/node-red-alexa-home-skill-v3-lambda/stargazers) - Lambda function for node-red-alexa-home-skill-v3-web.
- [alexa-remote2-applestrudel](https://github.com/bbindreiter/node-red-contrib-alexa-remote2-applestrudel) [![GitHub stars](https://img.shields.io/github/stars/bbindreiter/node-red-contrib-alexa-remote2-applestrudel?style=flat)](https://github.com/bbindreiter/node-red-contrib-alexa-remote2-applestrudel/stargazers) - Interacting with the Alexa API. Emulates routine behaviour, control and query your devices.
- [avr-yamaha](https://github.com/krauskopf/node-red-contrib-avr-yamaha) [![GitHub stars](https://img.shields.io/github/stars/krauskopf/node-red-contrib-avr-yamaha?style=flat)](https://github.com/krauskopf/node-red-contrib-avr-yamaha/stargazers) - Integrate and control YAMAHA™ audio/video receiver via YNCA protocol.
- [ccu](https://github.com/rdmtc/node-red-contrib-ccu) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/node-red-contrib-ccu?style=flat)](https://github.com/rdmtc/node-red-contrib-ccu/stargazers) - Connect with Homematic, a series of smart home automation hardware from the manufacturer eQ-3, popular especially in Germany.
- [deconz](https://github.com/deconz-community/node-red-contrib-deconz) [![GitHub stars](https://img.shields.io/github/stars/deconz-community/node-red-contrib-deconz?style=flat)](https://github.com/deconz-community/node-red-contrib-deconz/stargazers) - Access Zigbee 3.0 (Z30), Zigbee Home Automation (ZHA) and Zigbee Light Link (ZLL) lights via deCONZ.
- [fritz](https://github.com/bashgroup/node-red-contrib-fritz) [![GitHub stars](https://img.shields.io/github/stars/bashgroup/node-red-contrib-fritz?style=flat)](https://github.com/bashgroup/node-red-contrib-fritz/stargazers) - Provides easy access to your AVM Fritz!Box. Read and write the configuration including the VoIP and Dect configuration.
- [fritzapi](https://github.com/dnknth/node-red-contrib-fritzapi) [![GitHub stars](https://img.shields.io/github/stars/dnknth/node-red-contrib-fritzapi?style=flat)](https://github.com/dnknth/node-red-contrib-fritzapi/stargazers) - Controls smart home DECT devices and guest wifi through an AVM Fritz!Box.
- [harmony](https://github.com/Aietes/node-red-contrib-harmony) [![GitHub stars](https://img.shields.io/github/stars/Aietes/node-red-contrib-harmony?style=flat)](https://github.com/Aietes/node-red-contrib-harmony/stargazers) - Controls devices connected to a Logitech™ Harmony Hub.
- [home-assistant](https://github.com/AYapejian/node-red-contrib-home-assistant) [![GitHub stars](https://img.shields.io/github/stars/AYapejian/node-red-contrib-home-assistant?style=flat)](https://github.com/AYapejian/node-red-contrib-home-assistant/stargazers) - Connect with Home Assistant.
- [home-assistant-websocket](https://github.com/zachowj/node-red-contrib-home-assistant-websocket) [![GitHub stars](https://img.shields.io/github/stars/zachowj/node-red-contrib-home-assistant-websocket?style=flat)](https://github.com/zachowj/node-red-contrib-home-assistant-websocket/stargazers) - Various nodes using websockets to assist in setting up communication with Home Assistant.
- [homebridge-automation](https://github.com/NorthernMan54/node-red-contrib-homebridge-automation) [![GitHub stars](https://img.shields.io/github/stars/NorthernMan54/node-red-contrib-homebridge-automation?style=flat)](https://github.com/NorthernMan54/node-red-contrib-homebridge-automation/stargazers) - Integrate Homebridge Accessories into flows.
- [homee](https://github.com/stfnhmplr/node-red-contrib-homee) [![GitHub stars](https://img.shields.io/github/stars/stfnhmplr/node-red-contrib-homee?style=flat)](https://github.com/stfnhmplr/node-red-contrib-homee/stargazers) - Access the homee api and create virtual devices for homee.
- [homekit-bridged](https://github.com/NRCHKB/node-red-contrib-homekit-bridged) [![GitHub stars](https://img.shields.io/github/stars/NRCHKB/node-red-contrib-homekit-bridged?style=flat)](https://github.com/NRCHKB/node-red-contrib-homekit-bridged/stargazers) - Imitate HomeKit devices.
- [hubitat](https://github.com/fblackburn1/node-red-contrib-hubitat) [![GitHub stars](https://img.shields.io/github/stars/fblackburn1/node-red-contrib-hubitat?style=flat)](https://github.com/fblackburn1/node-red-contrib-hubitat/stargazers) - Connect with Hubitat.
- [huemagic](https://github.com/Foddy/node-red-contrib-huemagic) [![GitHub stars](https://img.shields.io/github/stars/Foddy/node-red-contrib-huemagic?style=flat)](https://github.com/Foddy/node-red-contrib-huemagic/stargazers) - Controls Philips Hue bridges, lights, groups, scenes, rules, taps, switches, buttons, motion sensors, temperature sensors and Lux sensors.
- [lgtv](https://github.com/hobbyquaker/node-red-contrib-lgtv) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/node-red-contrib-lgtv?style=flat)](https://github.com/hobbyquaker/node-red-contrib-lgtv/stargazers) - Controls LG webOS Smart TVs.
- [loxone](https://github.com/codmpm/node-red-contrib-loxone) [![GitHub stars](https://img.shields.io/github/stars/codmpm/node-red-contrib-loxone?style=flat)](https://github.com/codmpm/node-red-contrib-loxone/stargazers) - Connect to the Loxone Miniserver.
- [knx-ultimate](https://github.com/Supergiovane/node-red-contrib-knx-ultimate) [![GitHub stars](https://img.shields.io/github/stars/Supergiovane/node-red-contrib-knx-ultimate?style=flat)](https://github.com/Supergiovane/node-red-contrib-knx-ultimate/stargazers) - Controls KNX intallation. With optional ETS group address importer and gateway simulation. 
- [openhab3](https://github.com/jeroenhendricksen/node-red-contrib-openhab3) [![GitHub stars](https://img.shields.io/github/stars/jeroenhendricksen/node-red-contrib-openhab3?style=flat)](https://github.com/jeroenhendricksen/node-red-contrib-openhab3/stargazers) - Integration of openHAB item states and commands.
- [power-saver](https://power-saver.smoky.no/) - Automatically save money on variable electricity prices.
- [smartnora](https://github.com/andrei-tatar/node-red-contrib-smartnora) [![GitHub stars](https://img.shields.io/github/stars/andrei-tatar/node-red-contrib-smartnora?style=flat)](https://github.com/andrei-tatar/node-red-contrib-smartnora/stargazers) - Google smart home Action integration via Smart NORA.
- [sonos-plus](https://github.com/hklages/node-red-contrib-sonos-plus) [![GitHub stars](https://img.shields.io/github/stars/hklages/node-red-contrib-sonos-plus?style=flat)](https://github.com/hklages/node-red-contrib-sonos-plus/stargazers) - Controls Sonos player in your local network.
- [tado-client](https://github.com/mattdavis90/node-red-contrib-tado-client) [![GitHub stars](https://img.shields.io/github/stars/mattdavis90/node-red-contrib-tado-client?style=flat)](https://github.com/mattdavis90/node-red-contrib-tado-client/stargazers) - Connect to the Tado Web API.
- [tahoma](https://github.com/nikkow/node-red-contrib-tahoma) [![GitHub stars](https://img.shields.io/github/stars/nikkow/node-red-contrib-tahoma?style=flat)](https://github.com/nikkow/node-red-contrib-tahoma/stargazers) - Controls a Somfy Tahoma box (Roller shutters, etc.). 
- [tasmota](https://github.com/DaveMDS/node-red-contrib-tasmota) [![GitHub stars](https://img.shields.io/github/stars/DaveMDS/node-red-contrib-tasmota?style=flat)](https://github.com/DaveMDS/node-red-contrib-tasmota/stargazers) - Tasmota devices integration for building automation.
- [tuya-smart](https://github.com/hgross/node-red-contrib-tuya-smart) [![GitHub stars](https://img.shields.io/github/stars/hgross/node-red-contrib-tuya-smart?style=flat)](https://github.com/hgross/node-red-contrib-tuya-smart/stargazers) - Interface with smart plugs, bulbs, etc. from tuya.
- [zigbee](https://github.com/hobbyquaker/node-red-contrib-zigbee) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/node-red-contrib-zigbee?style=flat)](https://github.com/hobbyquaker/node-red-contrib-zigbee/stargazers) - Controls Zigbee Devices via a CC253x Module.
- [zigbee2mqtt](https://github.com/andreypopov/node-red-contrib-zigbee2mqtt) [![GitHub stars](https://img.shields.io/github/stars/andreypopov/node-red-contrib-zigbee2mqtt?style=flat)](https://github.com/andreypopov/node-red-contrib-zigbee2mqtt/stargazers) - Zigbee2mqtt connectivity.
- [zwave-js](https://github.com/zwave-js/node-red-contrib-zwave-js) [![GitHub stars](https://img.shields.io/github/stars/zwave-js/node-red-contrib-zwave-js?style=flat)](https://github.com/zwave-js/node-red-contrib-zwave-js/stargazers) - Integrates Z-Wave node based on Z-Wave JS.

### Social

- [chatbot](https://github.com/guidone/node-red-contrib-chatbot) [![GitHub stars](https://img.shields.io/github/stars/guidone/node-red-contrib-chatbot?style=flat)](https://github.com/guidone/node-red-contrib-chatbot/stargazers) - Full featured chat bot for Telegram, Facebook Messenger, Viber, Twilio and Slack.
- [discord-advanced](https://github.com/Markoudstaal/node-red-contrib-discord-advanced) [![GitHub stars](https://img.shields.io/github/stars/Markoudstaal/node-red-contrib-discord-advanced?style=flat)](https://github.com/Markoudstaal/node-red-contrib-discord-advanced/stargazers) - Interact with Discord, via Discord.js.
- [dweetio](https://github.com/node-red/node-red-nodes/tree/master/social/dweetio) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/dweetio?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/dweetio/stargazers) - Uses [dweetio](https://dweet.io/) to send/receive messages.
- [email](https://github.com/node-red/node-red-nodes/tree/master/social/email) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/email?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/email/stargazers) - Sends and receives simple emails from services like gmail or smtp or imap servers.
- [feedparser](https://github.com/node-red/node-red-nodes/tree/master/social/feedparser) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/feedparser?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/feedparser/stargazers) - Reads messages from an atom or rss feed.
- [irc](https://github.com/node-red/node-red-nodes/tree/master/social/irc) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/irc?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/irc/stargazers) - Connect to an IRC server to send and receive messages.
- [notify](https://github.com/node-red/node-red-nodes/tree/master/social/notify) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/notify?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/notify/stargazers) - Uses [Growl](https://growl.info/) to provide a desktop popup. Only useful on the local Apple machine.
- [prowl](https://github.com/node-red/node-red-nodes/tree/master/social/prowl) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/prowl?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/prowl/stargazers) - Uses [Prowl](https://www.prowlapp.com/) to push to an Apple device that has the Prowl app installed.
- [pushbullet](https://github.com/node-red/node-red-nodes/tree/master/social/pushbullet) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/pushbullet?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/pushbullet/stargazers) - Uses [PushBullet](https://www.pushbullet.com/) to push an Android device that has the app installed.
- [pusher](https://github.com/node-red/node-red-nodes/tree/master/social/pusher) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/pusher?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/pusher/stargazers) - Publish-Subscribe to a [Pusher](https://pusher.com/) channel/event.
- [pushover](https://github.com/node-red/node-red-nodes/tree/master/social/pushover) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/pushover?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/pushover/stargazers) - Sends alerts via [Pushover](https://pushover.net/).
- [PushStaq](https://github.com/pantchox/node-red-contrib-pushstaq) [![GitHub stars](https://img.shields.io/github/stars/pantchox/node-red-contrib-pushstaq?style=flat)](https://github.com/pantchox/node-red-contrib-pushstaq/stargazers) - Send real time alerts using Push Notifications from your Node-Red flows to any device with [PushStaq](https://www.pushstaq.com).
- [slack](https://github.com/yayadrian/node-red-slack) [![GitHub stars](https://img.shields.io/github/stars/yayadrian/node-red-slack?style=flat)](https://github.com/yayadrian/node-red-slack/stargazers) - Interact with the Slack API.
- [sms77](https://github.com/sms77io/nodered-contrib-sms77) [![GitHub stars](https://img.shields.io/github/stars/sms77io/nodered-contrib-sms77?style=flat)](https://github.com/sms77io/nodered-contrib-sms77/stargazers) - Uses [sms77](https://www.sms77.io/) service for SMS, text-to-speech calls and number lookups.
- [telegrambot](https://github.com/windkh/node-red-contrib-telegrambot) [![GitHub stars](https://img.shields.io/github/stars/windkh/node-red-contrib-telegrambot?style=flat)](https://github.com/windkh/node-red-contrib-telegrambot/stargazers) - Contains a receiver and a sender node which act as a Telegram Bot.
- [twilio](https://github.com/node-red/node-red-nodes/tree/master/social/twilio) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/twilio?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/twilio/stargazers) - Uses [Twilio](https://www.twilio.com/) service to send/receive text messages.
- [whin](https://github.com/inUtil-info/node-red-contrib-whin) [![GitHub stars](https://img.shields.io/github/stars/inUtil-info/node-red-contrib-whin?style=flat)](https://github.com/inUtil-info/node-red-contrib-whin/stargazers) - Send and receive whatsapps from within a nodered flow.
- [xmpp](https://github.com/node-red/node-red-nodes/tree/master/social/xmpp) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/social/xmpp?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/social/xmpp/stargazers) - Connect to an XMPP server to send and receive messages.
- [open-wa (whatsapp)](https://github.com/open-wa/node-red-contrib-wa-automate) [![GitHub stars](https://img.shields.io/github/stars/open-wa/node-red-contrib-wa-automate?style=flat)](https://github.com/open-wa/node-red-contrib-wa-automate/stargazers) - Efficiently connect to remote instances of your open-wa whatsapp automate servers.

### System

- [aedes](https://github.com/martin-doyle/node-red-contrib-aedes) [![GitHub stars](https://img.shields.io/github/stars/martin-doyle/node-red-contrib-aedes?style=flat)](https://github.com/martin-doyle/node-red-contrib-aedes/stargazers) - MQTT Broker based on Aedes.
- [dockerode](https://github.com/naimo84/node-red-contrib-dockerode) [![GitHub stars](https://img.shields.io/github/stars/naimo84/node-red-contrib-dockerode?style=flat)](https://github.com/naimo84/node-red-contrib-dockerode/stargazers) - Connect to Docker daemon.
- [os](https://github.com/Argonne-National-Laboratory/node-red-contrib-os) [![GitHub stars](https://img.shields.io/github/stars/Argonne-National-Laboratory/node-red-contrib-os?style=flat)](https://github.com/Argonne-National-Laboratory/node-red-contrib-os/stargazers) - Obtain system information.

### Time

- [blindcontroller](https://github.com/alisdairjsmyth/node-red-contrib-blindcontroller) [![GitHub stars](https://img.shields.io/github/stars/alisdairjsmyth/node-red-contrib-blindcontroller?style=flat)](https://github.com/alisdairjsmyth/node-red-contrib-blindcontroller/stargazers) - Automate the control of household roller blinds based on the current position of the sun.
- [bigtimer](https://github.com/scargill/node-red-contrib-bigtimer) [![GitHub stars](https://img.shields.io/github/stars/scargill/node-red-contrib-bigtimer?style=flat)](https://github.com/scargill/node-red-contrib-bigtimer/stargazers) - Timing node with support for dusk/sunset dawn/sunrise and variations also day/week/month (and special days) control. The node offers outputs suitable for MQTT, speech and databases.
- [cron-plus](https://flows.nodered.org/node/node-red-contrib-cron-plus) - A flexible scheduler (cron, solar events, simple dates) node with full dynamic control and Timezone support.
- [suncalc](https://github.com/node-red/node-red-nodes/tree/master/time/suncalc) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/time/suncalc?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/time/suncalc/stargazers) - Uses the suncalc module to generate an output at sunrise and sunset based on a specified location. 
- [simpletime](https://github.com/Paul-Reed/node-red-contrib-simpletime) [![GitHub stars](https://img.shields.io/github/stars/Paul-Reed/node-red-contrib-simpletime?style=flat)](https://github.com/Paul-Reed/node-red-contrib-simpletime/stargazers) - Adds time and date payloads with various formatting options, which can be retreived and used later in the flow.
- [sun-position](https://github.com/rdmtc/node-red-contrib-sun-position) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/node-red-contrib-sun-position?style=flat)](https://github.com/rdmtc/node-red-contrib-sun-position/stargazers) - Timer based flow control with dusk, dawn (and variations) and much more. Additional you can get sun and moon position or to control a flow by sun or moon position.
- [timeswitch](https://github.com/node-red/node-red-nodes/tree/master/time/timeswitch) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/time/timeswitch?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/time/timeswitch/stargazers) - Lets the user set simple repeating timers for example for simple heating control, etc.

### Utility

- [actionflows](https://github.com/Steveorevo/node-red-contrib-actionflows) [![GitHub stars](https://img.shields.io/github/stars/Steveorevo/node-red-contrib-actionflows?style=flat)](https://github.com/Steveorevo/node-red-contrib-actionflows/stargazers) - Brings easy to use loops and OOP (object oriented programming) features.
- [alarm](https://github.com/Anamico/node-red-contrib-alarm) [![GitHub stars](https://img.shields.io/github/stars/Anamico/node-red-contrib-alarm?style=flat)](https://github.com/Anamico/node-red-contrib-alarm/stargazers) - Build your own home alarm system with any number of panels, zones, sensors, triggers and automations.
- [bool-gate](https://flows.nodered.org/node/node-red-contrib-bool-gate) - Boolean logic gates.
- [daemon](https://github.com/node-red/node-red-nodes/tree/master/utility/daemon) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/utility/daemon?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/utility/daemon/stargazers) - Starts up (calls) a long running system program and pipes STDIN, STDOUT and STDERR to and from that process. 
- [exif](https://github.com/node-red/node-red-nodes/tree/master/utility/exif) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-nodes/tree/master/utility/exif?style=flat)](https://github.com/node-red/node-red-nodes/tree/master/utility/exif/stargazers) - Extracts GPS and other EXIF information from a passed in jpeg image.
- [german-holidays](https://github.com/rdmtc/node-red-contrib-german-holidays) [![GitHub stars](https://img.shields.io/github/stars/rdmtc/node-red-contrib-german-holidays?style=flat)](https://github.com/rdmtc/node-red-contrib-german-holidays/stargazers) - Getting german holidays or information if today/tomorrow is a holiday.
- [ical-events](https://github.com/naimo84/node-red-contrib-ical-events) [![GitHub stars](https://img.shields.io/github/stars/naimo84/node-red-contrib-ical-events?style=flat)](https://github.com/naimo84/node-red-contrib-ical-events/stargazers) - Get events from an ical-URL, a caldav-server or from iCloud via [kalender-events](https://github.com/naimo84/kalender-events) [![GitHub stars](https://img.shields.io/github/stars/naimo84/kalender-events?style=flat)](https://github.com/naimo84/kalender-events/stargazers).
- [interval-length](https://github.com/bartbutenaers/node-red-contrib-interval-length) [![GitHub stars](https://img.shields.io/github/stars/bartbutenaers/node-red-contrib-interval-length?style=flat)](https://github.com/bartbutenaers/node-red-contrib-interval-length/stargazers) - Measure the (time) interval length between successive messages.
- [moment](https://github.com/totallyinformation/node-red-contrib-moment) [![GitHub stars](https://img.shields.io/github/stars/totallyinformation/node-red-contrib-moment?style=flat)](https://github.com/totallyinformation/node-red-contrib-moment/stargazers) - Produces a nicely formatted Date/Time string using the Moment.js library. 
- [owntracks](https://github.com/hardillb/node-red-contrib-owntracks) [![GitHub stars](https://img.shields.io/github/stars/hardillb/node-red-contrib-owntracks?style=flat)](https://github.com/hardillb/node-red-contrib-owntracks/stargazers) - Converts Owntrack Messages into standard geo message and deals with encrypted locations.
- [persist](https://github.com/DeanCording/node-red-contrib-persist) [![GitHub stars](https://img.shields.io/github/stars/DeanCording/node-red-contrib-persist?style=flat)](https://github.com/DeanCording/node-red-contrib-persist/stargazers) - Persist data over Node-RED restarts and deploys.
- [self-healing](https://github.com/jpdias/node-red-contrib-self-healing) [![GitHub stars](https://img.shields.io/github/stars/jpdias/node-red-contrib-self-healing?style=flat)](https://github.com/jpdias/node-red-contrib-self-healing/stargazers) - Making Node-RED more resilient by adding self-healing capabilities.
- [state-machine](https://github.com/DeanCording/node-red-contrib-state-machine) [![GitHub stars](https://img.shields.io/github/stars/DeanCording/node-red-contrib-state-machine?style=flat)](https://github.com/DeanCording/node-red-contrib-state-machine/stargazers) - Wraps around the JavaScript State Machine to implement a finite state machine.
- [string](https://github.com/steveorevo/node-red-contrib-string) [![GitHub stars](https://img.shields.io/github/stars/steveorevo/node-red-contrib-string?style=flat)](https://github.com/steveorevo/node-red-contrib-string/stargazers) - Provides native and extended chainable JavaScript string parsing and manipulation methods.
- [twc-weather](https://github.com/johnwalicki/node-red-contrib-twc-weather) [![GitHub stars](https://img.shields.io/github/stars/johnwalicki/node-red-contrib-twc-weather?style=flat)](https://github.com/johnwalicki/node-red-contrib-twc-weather/stargazers) - The Weather Company and Weather Underground Personal Weather Station APIs.
- [users](https://github.com/SenseTecnic/node-red-contrib-users) [![GitHub stars](https://img.shields.io/github/stars/SenseTecnic/node-red-contrib-users?style=flat)](https://github.com/SenseTecnic/node-red-contrib-users/stargazers) - Quickly build a very simple user access control for HTTP-based flows.
- [watson](https://github.com/watson-developer-cloud/node-red-node-watson) [![GitHub stars](https://img.shields.io/github/stars/watson-developer-cloud/node-red-node-watson?style=flat)](https://github.com/watson-developer-cloud/node-red-node-watson/stargazers) - Interact with the IBM Watson services in IBM Cloud.

### UI

- [browser-utils](https://github.com/ibm-early-programs/node-red-contrib-browser-utils) [![GitHub stars](https://img.shields.io/github/stars/ibm-early-programs/node-red-contrib-browser-utils?style=flat)](https://github.com/ibm-early-programs/node-red-contrib-browser-utils/stargazers) - Add browser functionality such as file upload, camera & microphone.
- [node-red-dashboard](https://github.com/node-red/node-red-dashboard) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-dashboard?style=flat)](https://github.com/node-red/node-red-dashboard/stargazers) - Create a live data dashboard.
    - [https://flows.nodered.org/collection](https://flows.nodered.org/collection/590bc13ff3a5f005c7d2189bbb563976) - Dashboard extra nodes.
    - [ui-svg](https://flows.nodered.org/node/node-red-contrib-ui-svg) - Show interactive SVG (vector graphics) in the dashboard.
    - [ui-contextmenu](https://flows.nodered.org/node/node-red-contrib-ui-contextmenu) - Show a popup contextmenu in the dashboard.
- [flow-manager](https://flows.nodered.org/node/node-red-contrib-flow-manager) - Separates flow json to multiple files.
- [iglass](https://www.npmjs.com/package/iglass-nodes) - Interaction with [iGlass Automation](https://iglass.international) blocks.
- [uibuilder](https://github.com/TotallyInformation/node-red-contrib-uibuilder) [![GitHub stars](https://img.shields.io/github/stars/TotallyInformation/node-red-contrib-uibuilder?style=flat)](https://github.com/TotallyInformation/node-red-contrib-uibuilder/stargazers) - Create dynamic web interfaces using any (or no) front end libraries for convenience.
- [web-worldmap](https://github.com/dceejay/RedMap) [![GitHub stars](https://img.shields.io/github/stars/dceejay/RedMap?style=flat)](https://github.com/dceejay/RedMap/stargazers) - Provide a world map web page for plotting "things" on.

## Community

- [HomeAssistant Forum](https://community.home-assistant.io/c/third-party/node-red/31)
- [Node-RED Forum](https://discourse.nodered.org/)
- [Node-RED Blog](https://nodered.org/blog/)
- [Node-RED User Group Japan](https://nodered.jp/)
- [Reddit](https://www.reddit.com/r/nodered/)
- [Redmatic Forum](https://homematic-forum.de/forum/viewforum.php?f=77)
- [Slack](https://nodered.org/about/community/slack)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/node-red)
- [Steves Node-RED Guide](https://stevesnoderedguide.com/)
- [Twitter](https://twitter.com/NodeRED)
- [YouTube](https://www.youtube.com/channel/UCQaB8NXBEPod7Ab8PPCLLAA)

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
