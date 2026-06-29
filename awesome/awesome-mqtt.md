# MQTT

[![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/awesome-mqtt?style=flat)](https://github.com/hobbyquaker/awesome-mqtt/stargazers)

# Awesome MQTT [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

> A curated list of MQTT related stuff.

MQTT is a lightweight client-server publish/subscribe messaging protocol, optimized for high-latency or unreliable networks. This protocol is a good choice for Internet of Things applications, Telemetry, Sensor Networks, Smart Metering, Home Automation, Messaging and Notification Services.

## Contents

<!--lint disable double-link-->
- [Community Resources](#community-resources)
- [Brokers](#brokers)
- [Cloud](#cloud)
- [Platforms](#platforms)
- [Tools](#tools)
- [Clients](#clients)
- [Scripting](#scripting)
- [Interfaces](#interfaces)
    - [Makers](#makers)
    - [Industry](#industry)
    - [Telephony, PBX](#telephony-pbx)
    - [Operating System](#operating-system)
    - [Monitoring](#monitoring)
    - [Location Tracking](#location-tracking)
    - [Logging](#logging)
    - [Smart Home Hardware Interfaces](#smart-home-hardware-interfaces)
    - [Smart Home Integration Software](#smart-home-integration-software)
    - [Lighting](#lighting)
    - [Home Entertainment](#home-entertainment)
    - [Smart Metering](#smart-metering)
    - [Messaging](#messaging)
    - [Misc](#misc)
- [Visualization, Dashboards](#visualization-dashboards)
- [Architecture, Convention](#architecture-convention)
- [Security, Encryption](#security-encryption)
<!--lint enable double-link-->

### Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

## Community Resources

- [mqtt.org](https://mqtt.org/)
- [MQTT community wiki](https://github.com/mqtt/mqtt.org/wiki) [![GitHub stars](https://img.shields.io/github/stars/mqtt/mqtt.org/wiki?style=flat)](https://github.com/mqtt/mqtt.org/wiki/stargazers)
- [Google Groups: MQTT](https://groups.google.com/g/mqtt)
- [IRC channel #mqtt on the freenode network](irc://irc.freenode.net/mqtt)
- [A list of public brokers](https://moxd.io/2015/10/17/public-mqtt-brokers/)

### Blogs

- [Ben Hardill](https://www.hardill.me.uk/wordpress/tag/mqtt/)
- [Jan-Piet Mens](https://jpmens.net/)
- [Nick O'Leary](https://knolleary.net/)
- [HiveMQ](https://www.hivemq.com/blog/)
- [EMQ](https://www.emqx.com/en/blog)
- [Amazon AWS IoT Blog](https://aws.amazon.com/blogs/iot/tag/mqtt/)

### Talks

- [An Introduction to MQTT: Why HTTP isn't the King of the Internet of Things](https://www.youtube.com/watch?v=LKz1jYngpcU) - Shinji Kim, Robert Bird - Akamai, Samsung Developer Conference 2017.
- [Einführung in MQTT](https://www.youtube.com/watch?v=INYG4-xsa9c) - Dominik Obermaier & Jens Deters, [Building IoT](https://www.buildingiot.de/index.php) conference 2016 (German).

## Brokers

- [Ably](https://www.ably.io/documentation/mqtt) - MQTT broker service and protocol adapter.
- [ActiveMQ](https://activemq.apache.org/) - A fast Java multiprotocol messaging and Integration Patterns server.
- [Aedes](https://github.com/moscajs/aedes) [![GitHub stars](https://img.shields.io/github/stars/moscajs/aedes?style=flat)](https://github.com/moscajs/aedes/stargazers) - Barebone MQTT broker that can run on any stream server, the node way.
- [Bevywise MQTTRoute](https://www.bevywise.com/mqtt-broker/) - MQTTRoute is an extendable & Scalable MQTT Broker with customizable UI, flexible storage & security options for all IoT / IIoT Implementation.
- [BifroMQ](https://bifromq.apache.org) - Java-based high-performance MQTT broker with native multi-tenancy for large-scale IoT.
- [comqtt](https://github.com/wind-c/comqtt) [![GitHub stars](https://img.shields.io/github/stars/wind-c/comqtt?style=flat)](https://github.com/wind-c/comqtt/stargazers) - A lightweight, high-performance go mqtt server(v3.0|v3.1.1|v5.0) supporting distributed cluster.
- [Eclipse Amlen](https://github.com/eclipse/amlen) [![GitHub stars](https://img.shields.io/github/stars/eclipse/amlen?style=flat)](https://github.com/eclipse/amlen/stargazers) - A scalable, secure, easy to use message broker that can be used for IoT, web and mobile use-cases. Open-sourced from IBM MessageSight.
- [Emitter](https://github.com/emitter-io/emitter) [![GitHub stars](https://img.shields.io/github/stars/emitter-io/emitter?style=flat)](https://github.com/emitter-io/emitter/stargazers) - A distributed, scalable and fault-tolerant publish-subscribe messaging platform based on MQTT protocol and featuring message storage.
- [EMQ X](https://github.com/emqx/emqx) [![GitHub stars](https://img.shields.io/github/stars/emqx/emqx?style=flat)](https://github.com/emqx/emqx/stargazers) - Scalable and Reliable Real-time MQTT Messaging Engine for IoT in 5G Era.
- [esp_uMQTT_broker](https://github.com/martin-ger/esp_mqtt) [![GitHub stars](https://img.shields.io/github/stars/martin-ger/esp_mqtt?style=flat)](https://github.com/martin-ger/esp_mqtt/stargazers) - A basic MQTT Broker on the ESP8266.
<!--lint disable double-link-->
- [hbmqtt Broker](https://github.com/beerfactory/hbmqtt) [![GitHub stars](https://img.shields.io/github/stars/beerfactory/hbmqtt?style=flat)](https://github.com/beerfactory/hbmqtt/stargazers) - Python MQTT broker using asyncio.
<!--lint enable double-link-->
- [HiveMQ](https://www.hivemq.com/) - Java MQTT Broker that supports MQTT 3.1, 3.1.1 and 5.0. Commercial and open source editions available.
- [hrotti](https://github.com/alsm/hrotti) [![GitHub stars](https://img.shields.io/github/stars/alsm/hrotti?style=flat)](https://github.com/alsm/hrotti/stargazers) - A MQTT broker written in Go.
- [KMQTT](https://github.com/davidepianca98/KMQTT) [![GitHub stars](https://img.shields.io/github/stars/davidepianca98/KMQTT?style=flat)](https://github.com/davidepianca98/KMQTT/stargazers) - Kotlin Multiplatform MQTT broker, both embeddable and standalone.
- [Moquette](https://github.com/moquette-io/moquette) [![GitHub stars](https://img.shields.io/github/stars/moquette-io/moquette?style=flat)](https://github.com/moquette-io/moquette/stargazers) - Java MQTT lightweight broker.
- [Mosca](https://www.mosca.io/) - Node.js MQTT broker, which can be used Standalone or Embedded in another Node.js application.
- [Mosquitto](https://mosquitto.org/) - *"*The"** Open Source MQTT Broker.
- [mqtt5](https://github.com/LabOverWire/mqtt-lib) [![GitHub stars](https://img.shields.io/github/stars/LabOverWire/mqtt-lib?style=flat)](https://github.com/LabOverWire/mqtt-lib/stargazers) - Async MQTT v5.0 broker in Rust with TCP, TLS, WebSocket, and QUIC transport, plus authentication, ACL, bridging, and session persistence.
- [MyQttHub](https://myqtthub.com) - Cloud MQTT broker.
- [Mystique](https://github.com/TheThingsIndustries/mystique) [![GitHub stars](https://img.shields.io/github/stars/TheThingsIndustries/mystique?style=flat)](https://github.com/TheThingsIndustries/mystique/stargazers) - An extendable MQTT broker written in Go, with HTTP capabilities for observability. Implements MQTT v3.1.1.
- [RabbitMQ](https://www.rabbitmq.com/mqtt.html) - High performance messaging broker with MQTT Adapter.
- [RobustMQ](http://robustmq.com) - Multi-protocol brokers written in Rust.
- [SurgeMQ](https://zhen.org/categories/surgemq/) - High Performance MQTT Server and Client Libraries in Go.
- [tbmq](https://github.com/thingsboard/tbmq) [![GitHub stars](https://img.shields.io/github/stars/thingsboard/tbmq?style=flat)](https://github.com/thingsboard/tbmq/stargazers) - Open-source, scalable, fault-tolerant and durable messaging broker for millions of IoT devices.
- [VerneMQ](https://vernemq.com/) - Apache2 licensed distributed MQTT broker, developed in Erlang.
<!--lint disable double-link-->
- [Vert.x MQTT Server](https://github.com/vert-x3/vertx-mqtt) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-mqtt?style=flat)](https://github.com/vert-x3/vertx-mqtt/stargazers) - Vert.x component to handle connections, communication and messages exchange with remote MQTT clients.
<!--lint enable double-link-->
- [Waterstream](https://waterstream.io/) - MQTT broker leveraging Apache Kafka as its own storage and distribution engine.
- [NanoMQ](https://github.com/nanomq/nanomq) [![GitHub stars](https://img.shields.io/github/stars/nanomq/nanomq?style=flat)](https://github.com/nanomq/nanomq/stargazers) - A light-weight and Blazing-fast MQTT Broker for IoT Edge platform.


## Cloud

- [Adafruit IO](https://io.adafruit.com) - Data-oriented IoT framework and libraries.
- [Alibaba Cloud IoT Platform](https://www.alibabacloud.com/product/iot) - Provides secure and reliable communication between devices and the IoT Platform which allows you to manage a large number of devices on a single IoT Platform.
- [AWS IoT Core](https://aws.amazon.com/iot-core/) - Managed cloud broker service supporting MQTT, MQTT over WSS, HTTPS and LoRaWAN.
- [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/) - Enable highly secure and reliable communication between your IoT application and the devices it manages. Azure IoT Hub provides a cloud-hosted solution backend to connect virtually any device. Extend your solution from the cloud to the edge with per-device authentication, built-in device management, and scaled provisioning.
- [CloudMQTT](https://www.cloudmqtt.com/) - Hosted message broker for the Internet of Things. Perfectly configured and optimized message queues for IoT, ready in seconds.
- [CloudAMQP](https://www.cloudamqp.com/docs/mqtt.html) - Hosted AMQP brokers with MQTT support.
- [CrystalMQ](https://www.bevywise.com/hosted-mqtt-server/) - Fully Managed Cloud MQTT Broker for large scale deployments.
- [flespi](https://flespi.com/mqtt-broker) - Free and secure cloud MQTT broker with private namespaces, MQTT 3.1.1 and MQTT 5.0 support and gorgeous limits.
- [Google Cloud IoT](https://cloud.google.com/solutions/iot/) - Cloud managed MQTT service.
- [HiveMQ Cloud](https://www.hivemq.com/cloud/) - Cloud managed MQȚT service.

## Platforms

- [Iotellect](https://iotellect.com/) - Low-code IoT/IIoT platform for industrial automation, SCADA, BMS and remote monitoring. Supports MQTT, OPC-UA, Modbus and 100+ protocols with visual development tools and edge-cloud integration.
- [mainflux](https://www.mainflux.com/) - Device management, data aggregation, data management, data analytics,connectivity and message routing and event management. Supported by Linux Software Foundation.
- [thingsboard](https://thingsboard.io/) - Device management, data collection, processing, event management, and visualization for your IoT projects.
- [ForestHub](https://foresthub.ai) - Edge AI agent platform; its open-source runtime [edge-agents](https://github.com/ForestHubAI/edge-agents) [![GitHub stars](https://img.shields.io/github/stars/ForestHubAI/edge-agents?style=flat)](https://github.com/ForestHubAI/edge-agents/stargazers) orchestrates AI agents on Linux edge gateways with MQTT as a first-class workflow transport, running offline with local SLMs alongside cloud LLMs.


## Tools
- [hivemq-mqtt-web-client](https://github.com/hivemq/hivemq-mqtt-web-client) [![GitHub stars](https://img.shields.io/github/stars/hivemq/hivemq-mqtt-web-client?style=flat)](https://github.com/hivemq/hivemq-mqtt-web-client/stargazers) - Browser-based MQTT client that utilizes MQTT over websockets. [Direct Link](https://www.hivemq.com/demos/websocket-client/)
- [homie-home-assistant-discovery](https://github.com/labodj/homie-home-assistant-discovery) [![GitHub stars](https://img.shields.io/github/stars/labodj/homie-home-assistant-discovery?style=flat)](https://github.com/labodj/homie-home-assistant-discovery/stargazers) - Node.js CLI and library that maps Homie MQTT metadata to Home Assistant MQTT discovery payloads.
- [imqtt](https://github.com/shafreeck/imqtt) [![GitHub stars](https://img.shields.io/github/stars/shafreeck/imqtt?style=flat)](https://github.com/shafreeck/imqtt/stargazers) - Interactive MQTT packet manipulation shell based on IPython.
- [IoT-Testware](https://projects.eclipse.org/projects/technology.iottestware) - The Eclipse IoT-Testware is a collection of conformance test suites for IoT protocols enriched with additional tools for fuzzing and performance testing.
- [LabOverWire](https://laboverwire.com/features) - Visual diagram editor for designing MQTT topologies, built with Rust (WASM) and TypeScript. Features live in-browser simulation, code generation, and AsyncAPI export.
- [Mer-cli](https://github.com/iotmertech/iot-data-generator) [![GitHub stars](https://img.shields.io/github/stars/iotmertech/iot-data-generator?style=flat)](https://github.com/iotmertech/iot-data-generator/stargazers) - A high-performance IoT data generator written in Rust. Supports MQTT, HTTP, and TCP for simulating realistic sensor payloads with Handlebars templates.
- [mockd](https://github.com/getmockd/mockd) [![GitHub stars](https://img.shields.io/github/stars/getmockd/mockd?style=flat)](https://github.com/getmockd/mockd/stargazers) - Multi-protocol mock server with a built-in MQTT broker supporting QoS 0-2, retained messages, topic patterns, and device simulation for IoT development and testing.
- [moxy](https://github.com/jvermillard/moxy) [![GitHub stars](https://img.shields.io/github/stars/jvermillard/moxy?style=flat)](https://github.com/jvermillard/moxy/stargazers) - A Golang MQTT proxy providing useful output traces to monitor and troubleshoot your MQTT communications.
- [MQTT Board](https://github.com/flespi-software/MQTT-Board) [![GitHub stars](https://img.shields.io/github/stars/flespi-software/MQTT-Board?style=flat)](https://github.com/flespi-software/MQTT-Board/stargazers) - Open-source diagnostic-oriented MQTT client tool.
- [mqtt-admin](https://github.com/hobbyquaker/mqtt-admin/) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt-admin/?style=flat)](https://github.com/hobbyquaker/mqtt-admin//stargazers) - Web based MQTT frontend. [Direct Link](https://hobbyquaker.github.io/mqtt-admin/).
- [mqtt-benchmark](https://github.com/chirino/mqtt-benchmark) [![GitHub stars](https://img.shields.io/github/stars/chirino/mqtt-benchmark?style=flat)](https://github.com/chirino/mqtt-benchmark/stargazers) - A benchmarking tool for MQTT Servers.
- [MQTT CLI](https://github.com/hivemq/mqtt-cli) [![GitHub stars](https://img.shields.io/github/stars/hivemq/mqtt-cli?style=flat)](https://github.com/hivemq/mqtt-cli/stargazers) - A command line interface for connecting various MQTT clients supporting MQTT 5.0 and 3.1.1.
- [mqtt-client](https://github.com/sdeancos/mqtt-client) [![GitHub stars](https://img.shields.io/github/stars/sdeancos/mqtt-client?style=flat)](https://github.com/sdeancos/mqtt-client/stargazers) - Simple MQTT Client command line (Python) (use paho lib).
- [mqtt-forget](https://github.com/hobbyquaker/mqtt-forget) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt-forget?style=flat)](https://github.com/hobbyquaker/mqtt-forget/stargazers) - Command line tool to remove retained MQTT topics by wildcard.
- [mqtt-fuzz](https://github.com/F-Secure/mqtt_fuzz) [![GitHub stars](https://img.shields.io/github/stars/F-Secure/mqtt_fuzz?style=flat)](https://github.com/F-Secure/mqtt_fuzz/stargazers) - A simple fuzzer for the MQTT protocol.
- [mqtt-malaria](https://github.com/etactica/mqtt-malaria) [![GitHub stars](https://img.shields.io/github/stars/etactica/mqtt-malaria?style=flat)](https://github.com/etactica/mqtt-malaria/stargazers) - Scalability and load testing utilities for MQTT environments.
- [mqtt-mirror](https://github.com/4nte/mqtt-mirror) [![GitHub stars](https://img.shields.io/github/stars/4nte/mqtt-mirror?style=flat)](https://github.com/4nte/mqtt-mirror/stargazers) - Mirror MQTT traffic from one broker to another. Available as a CLI tool, Helm chart or Docker image.
- [mqtt_recorder](https://github.com/rpdswtk/mqtt_recorder) [![GitHub stars](https://img.shields.io/github/stars/rpdswtk/mqtt_recorder?style=flat)](https://github.com/rpdswtk/mqtt_recorder/stargazers) - Simple cli tool for recording and replaying MQTT messages.
- [mqtt-shell](https://github.com/pidster-dot-org/mqtt-shell) [![GitHub stars](https://img.shields.io/github/stars/pidster-dot-org/mqtt-shell?style=flat)](https://github.com/pidster-dot-org/mqtt-shell/stargazers) - A simple interactive shell for MQTT.
- [mqtt-spy](https://kamilfb.github.io/mqtt-spy/) - Java based MQTT frontend. Supports scripting.
- [mqtt-studio](https://www.mqttstudio.com) - A practical MQTT Tool with an innovative UI, designed for developers to efficiently create, test, and manage MQTT-based applications, enhancing their development and support workflows.
- [mqtt_tree](https://github.com/poggenpower/mqtt_tree) [![GitHub stars](https://img.shields.io/github/stars/poggenpower/mqtt_tree?style=flat)](https://github.com/poggenpower/mqtt_tree/stargazers) - Displays all Topics in an expandable tree, helps to get an overview if you have a lot of clients publishing. (python, tkinter)
- [mqtt-utils](https://github.com/dsell/mqtt-utils) [![GitHub stars](https://img.shields.io/github/stars/dsell/mqtt-utils?style=flat)](https://github.com/dsell/mqtt-utils/stargazers) - A collection of MQTT utilities.
- [mqtt-wall](https://github.com/bastlirna/mqtt-wall) [![GitHub stars](https://img.shields.io/github/stars/bastlirna/mqtt-wall?style=flat)](https://github.com/bastlirna/mqtt-wall/stargazers) - Subscription only web-based client – like Twitter wall for MQTT.
- [mqtt-wildcard](https://github.com/hobbyquaker/mqtt-wildcard) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt-wildcard?style=flat)](https://github.com/hobbyquaker/mqtt-wildcard/stargazers) - Node.js Module to match a MQTT Topic against wildcards.
- [MQTT.fx](https://mqttfx.jensd.de/) - MQTT Client written in Java based on Eclipse Paho. Supports scripting.
- [mqttcli](https://github.com/shirou/mqttcli) [![GitHub stars](https://img.shields.io/github/stars/shirou/mqttcli?style=flat)](https://github.com/shirou/mqttcli/stargazers) - MQTT Client for shell scripting.
- [MQTTInspector](https://github.com/ckrey/MQTTInspector) [![GitHub stars](https://img.shields.io/github/stars/ckrey/MQTTInspector?style=flat)](https://github.com/ckrey/MQTTInspector/stargazers) - A general MQTT testing app for iOS (iPhone and iPad).
- [mqttkit](https://github.com/keyp-dev/mqttkit) [![GitHub stars](https://img.shields.io/github/stars/keyp-dev/mqttkit?style=flat)](https://github.com/keyp-dev/mqttkit/stargazers) - Elysia-style application framework for MQTT on Bun and TypeScript. Compose broker adapters, ordered middleware, typed topic routes, MQTT 5 RPC, and AsyncAPI 3.0 docs with `new MqttApp().use(...)`.
- [MQTTLens](https://chrome.google.com/webstore/detail/mqttlens/hemojaaeigabkbcookmlgmdigohjobjm) - A Google Chrome application, which connects to a MQTT broker and is able to subscribe and publish to MQTT topics.
- [MQTT Explorer](https://mqtt-explorer.com/) - Tool to visualize your MQTT topics in a topic hierarchy, a MQTT swiss-army knife.
- [MQTT TUI](https://github.com/EdJoPaTo/mqttui) [![GitHub stars](https://img.shields.io/github/stars/EdJoPaTo/mqttui?style=flat)](https://github.com/EdJoPaTo/mqttui/stargazers) - Simple lightweight terminal based MQTT monitor and publisher.
- [Python MQTT Client Shell](https://github.com/bapowell/python-mqtt-client-shell) [![GitHub stars](https://img.shields.io/github/stars/bapowell/python-mqtt-client-shell?style=flat)](https://github.com/bapowell/python-mqtt-client-shell/stargazers) - Text console-based, interactive shell for exercising various tasks associated with MQTT client communications.
- [SimpleMQTT](https://simplemqtt.theoi.de/) - A Slack app to send messages from Slack to MQTT brokers with slash commands.
- [Wireshark-MQTT](https://github.com/menudoproblema/Wireshark-MQTT) [![GitHub stars](https://img.shields.io/github/stars/menudoproblema/Wireshark-MQTT?style=flat)](https://github.com/menudoproblema/Wireshark-MQTT/stargazers) - MQTT dissector for Wireshark.
- [VSMQTT](https://github.com/rpdswtk/vsmqtt) [![GitHub stars](https://img.shields.io/github/stars/rpdswtk/vsmqtt?style=flat)](https://github.com/rpdswtk/vsmqtt/stargazers) - Simple MQTT client integrated in Visual Studio Code.
- [MQTTX](https://github.com/emqx/MQTTX) [![GitHub stars](https://img.shields.io/github/stars/emqx/MQTTX?style=flat)](https://github.com/emqx/MQTTX/stargazers) - Cross-platform MQTT desktop client open sourced by EMQ, which supports macOS, Linux, and Windows.
- [MIMIC MQTT Simulator](https://www.gambitcomm.com/site/mqttsimulator.php) - Simulate up to 100,000 MQTT clients per server for development/testing/deployment of IoT applications.
- [mqtt-stats](https://github.com/gambitcomminc/mqtt-stats) [![GitHub stars](https://img.shields.io/github/stars/gambitcomminc/mqtt-stats?style=flat)](https://github.com/gambitcomminc/mqtt-stats/stargazers) - Subscriber client to monitor MQTT Topic Statistics.
- [mqtt_monitor](https://github.com/filipsPL/mqtt-monitor) [![GitHub stars](https://img.shields.io/github/stars/filipsPL/mqtt-monitor?style=flat)](https://github.com/filipsPL/mqtt-monitor/stargazers) - Simple and lightweight console moniotor for mqtt topics, with eye-candies, in python 3.
- [mqttcommander](https://github.com/vroomfondel/mqttcommander) [![GitHub stars](https://img.shields.io/github/stars/vroomfondel/mqttcommander?style=flat)](https://github.com/vroomfondel/mqttcommander/stargazers) - A console-based MQTT client and commander, especially useful for IoT, Tasmota, and Node-RED setups.
- [mqttv5](https://github.com/LabOverWire/mqtt-lib) [![GitHub stars](https://img.shields.io/github/stars/LabOverWire/mqtt-lib?style=flat)](https://github.com/LabOverWire/mqtt-lib/stargazers) - Unified MQTT v5.0 CLI for publishing, subscribing, running a broker, and benchmarking with multi-transport support.

## Clients


### Multi-Platform

- [Paho](https://www.eclipse.org/paho/) - Open source client implementations for C,C++, Java, Python, JavaScript, GoLang, C#, Rust, Android and Embedded (Arduino/mbed).
- [mosquitto-clients](https://mosquitto.org/download/) - [mosquitto_pub](https://mosquitto.org/man/mosquitto_pub-1.html) and [mosquitto_sub](https://mosquitto.org/man/mosquitto_sub-1.html) CLI clients for most operating systems and [libmosquitto](https://mosquitto.org/man/libmosquitto-3.html) for integration.

### Python

- [aiomqtt](https://github.com/empicano/aiomqtt) [![GitHub stars](https://img.shields.io/github/stars/empicano/aiomqtt?style=flat)](https://github.com/empicano/aiomqtt/stargazers) - The idiomatic asyncio MQTT client.
- [gmqtt](https://github.com/wialon/gmqtt) [![GitHub stars](https://img.shields.io/github/stars/wialon/gmqtt?style=flat)](https://github.com/wialon/gmqtt/stargazers) - Python MQTT v5.0 client (asyncio-based).
<!--lint disable double-link-->
- [hbmqtt Client](https://github.com/beerfactory/hbmqtt) [![GitHub stars](https://img.shields.io/github/stars/beerfactory/hbmqtt?style=flat)](https://github.com/beerfactory/hbmqtt/stargazers) - Python MQTT client using asyncio.
<!--lint enable double-link-->
- [MiniMQTT](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT) [![GitHub stars](https://img.shields.io/github/stars/adafruit/Adafruit_CircuitPython_MiniMQTT?style=flat)](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT/stargazers) - MQTT Client Library for CircuitPython.

### JavaScript

- [MQTT.js](https://github.com/mqttjs) [![GitHub stars](https://img.shields.io/github/stars/mqttjs?style=flat)](https://github.com/mqttjs/stargazers) - MQTT client for Node.js.
- [mqtt-elements](https://github.com/mqttjs/mqtt-elements) [![GitHub stars](https://img.shields.io/github/stars/mqttjs/mqtt-elements?style=flat)](https://github.com/mqttjs/mqtt-elements/stargazers) - Polymer elements for MQTT.
- [mqtt-wrapper](https://www.webcomponents.org/element/hobbyquaker/mqtt-wrapper/elements/mqtt-wrapper) - Polymer Element that wraps other Elements and links them to MQTT topics.
<!--lint disable double-link-->
- [Vert.x Client](https://github.com/vert-x3/vertx-mqtt) [![GitHub stars](https://img.shields.io/github/stars/vert-x3/vertx-mqtt?style=flat)](https://github.com/vert-x3/vertx-mqtt/stargazers) - Vert.x component that provides methods for connecting/disconnecting to a broker, publishing messages and subscribing to topics.
<!--lint enable double-link-->

### Java

- [hivemq-mqtt-client](https://github.com/hivemq/hivemq-mqtt-client) [![GitHub stars](https://img.shields.io/github/stars/hivemq/hivemq-mqtt-client?style=flat)](https://github.com/hivemq/hivemq-mqtt-client/stargazers) - High-performance Java MQTT client library with different API flavours for MQTT 5.0 and 3.1.1.

### Erlang or Elixir

- [emqttc](https://github.com/emqx/emqtt) [![GitHub stars](https://img.shields.io/github/stars/emqx/emqtt?style=flat)](https://github.com/emqx/emqtt/stargazers) - Asynchronous Erlang MQTT Client.
- [mqttex](https://github.com/alfert/mqttex) [![GitHub stars](https://img.shields.io/github/stars/alfert/mqttex?style=flat)](https://github.com/alfert/mqttex/stargazers) - MQTT implementation in Elixir.

### Ballerina

- [ballerina-mqtt](https://github.com/ballerina-platform/module-ballerina-mqtt) [![GitHub stars](https://img.shields.io/github/stars/ballerina-platform/module-ballerina-mqtt?style=flat)](https://github.com/ballerina-platform/module-ballerina-mqtt/stargazers) - Ballerina MQTT client based on paho-mqtt.

### C or C++

- [mqtt_cpp](https://github.com/redboltz/mqtt_cpp) [![GitHub stars](https://img.shields.io/github/stars/redboltz/mqtt_cpp?style=flat)](https://github.com/redboltz/mqtt_cpp/stargazers) - MQTT client for C++14 based on Boost.Asio.
- [MQTT-C](https://github.com/LiamBindle/MQTT-C) [![GitHub stars](https://img.shields.io/github/stars/LiamBindle/MQTT-C?style=flat)](https://github.com/LiamBindle/MQTT-C/stargazers) - A portable MQTT C client for embedded systems and PCs alike.
- [wolfMQTT](https://www.wolfssl.com/products/wolfmqtt/) - A client implementation of the MQTT written in C for embedded use. It supports SSL/TLS via the wolfSSL library.

### Clojure

- [Machine Head](https://github.com/clojurewerkz/machine_head) [![GitHub stars](https://img.shields.io/github/stars/clojurewerkz/machine_head?style=flat)](https://github.com/clojurewerkz/machine_head/stargazers) - A Clojure MQTT Client.

### Dart

- [mqtt.dart](https://github.com/jnguillerme/mqtt.dart) [![GitHub stars](https://img.shields.io/github/stars/jnguillerme/mqtt.dart?style=flat)](https://github.com/jnguillerme/mqtt.dart/stargazers) - Dart MQTT client.

### C# / .NET

- [HiveMQtt](https://github.com/hivemq/hivemq-mqtt-client-dotnet) [![GitHub stars](https://img.shields.io/github/stars/hivemq/hivemq-mqtt-client-dotnet?style=flat)](https://github.com/hivemq/hivemq-mqtt-client-dotnet/stargazers) - MQTT 5.0 compliant secure client with automatic back pressure management and TCP & WebSocket transport support.
- [MQTTnet](https://github.com/chkr1011/MQTTnet) [![GitHub stars](https://img.shields.io/github/stars/chkr1011/MQTTnet?style=flat)](https://github.com/chkr1011/MQTTnet/stargazers) - MQTT client and broker .NET implementations.

### Delphi

- [delphi-mqtt](https://github.com/pjde/delphi-mqtt) [![GitHub stars](https://img.shields.io/github/stars/pjde/delphi-mqtt?style=flat)](https://github.com/pjde/delphi-mqtt/stargazers) - MQTT server and client components.
- [TMQTTClient](https://github.com/jamiei/Delphi-TMQTT2) [![GitHub stars](https://img.shields.io/github/stars/jamiei/Delphi-TMQTT2?style=flat)](https://github.com/jamiei/Delphi-TMQTT2/stargazers) - MQTT Client Library for Delphi. Alpha and long term unmaintained.

### GoLang

- [go-mqtt](https://github.com/go-mqtt/mqtt) [![GitHub stars](https://img.shields.io/github/stars/go-mqtt/mqtt?style=flat)](https://github.com/go-mqtt/mqtt/stargazers) - MQTT client.
- [MQTT for Go](https://github.com/jeffallen/mqtt) [![GitHub stars](https://img.shields.io/github/stars/jeffallen/mqtt?style=flat)](https://github.com/jeffallen/mqtt/stargazers) - MQTT Clients, Servers and Load Testers in Go.

### Lua

- [luamqtt](https://github.com/xHasKx/luamqtt/) [![GitHub stars](https://img.shields.io/github/stars/xHasKx/luamqtt/?style=flat)](https://github.com/xHasKx/luamqtt//stargazers) - Pure-lua MQTT v3.1.1 and v5.0 client.
- [mqtt_lua](https://geekscape.github.io/mqtt_lua/) - MQTT Client library for the Lua language.

### Objective-C

- [MQTT-Client-Framework](https://github.com/novastone-media/MQTT-Client-Framework) [![GitHub stars](https://img.shields.io/github/stars/novastone-media/MQTT-Client-Framework?style=flat)](https://github.com/novastone-media/MQTT-Client-Framework/stargazers) - iOS, macOS, tvOS native ObjectiveC MQTT Client Framework.
- [MQTTKit](https://github.com/mobile-web-messaging/MQTTKit) [![GitHub stars](https://img.shields.io/github/stars/mobile-web-messaging/MQTTKit?style=flat)](https://github.com/mobile-web-messaging/MQTTKit/stargazers) - MQTT Objective-C client for iOS.

### PHP

- [Mosquitto-PHP](https://github.com/mgdm/Mosquitto-PHP) [![GitHub stars](https://img.shields.io/github/stars/mgdm/Mosquitto-PHP?style=flat)](https://github.com/mgdm/Mosquitto-PHP/stargazers) - A wrapper for the Mosquitto MQTT client library for PHP.

### Ruby

- [ruby-mqtt](https://github.com/njh/ruby-mqtt) [![GitHub stars](https://img.shields.io/github/stars/njh/ruby-mqtt?style=flat)](https://github.com/njh/ruby-mqtt/stargazers) - Pure Ruby gem that implements the MQTT protocol.

### Rust

- [mqtt-rs](https://github.com/zonyitoo/mqtt-rs) [![GitHub stars](https://img.shields.io/github/stars/zonyitoo/mqtt-rs?style=flat)](https://github.com/zonyitoo/mqtt-rs/stargazers) - MQTT protocol library for Rust.
- [rumqtt](https://github.com/AtherEnergy/rumqtt) [![GitHub stars](https://img.shields.io/github/stars/AtherEnergy/rumqtt?style=flat)](https://github.com/AtherEnergy/rumqtt/stargazers) - A fast, lock free pure Rust MQTT client.
- [mqtt5](https://github.com/LabOverWire/mqtt-lib) [![GitHub stars](https://img.shields.io/github/stars/LabOverWire/mqtt-lib?style=flat)](https://github.com/LabOverWire/mqtt-lib/stargazers) - Complete async MQTT v5.0 client and broker library for Rust with TCP, TLS, WebSocket, and QUIC support.

### Swift

- [CocoaMQTT](https://github.com/emqx/CocoaMQTT) [![GitHub stars](https://img.shields.io/github/stars/emqx/CocoaMQTT?style=flat)](https://github.com/emqx/CocoaMQTT/stargazers) - MQTT for iOS and macOS written with Swift.
- [Moscapsule](https://github.com/flightonary/Moscapsule) [![GitHub stars](https://img.shields.io/github/stars/flightonary/Moscapsule?style=flat)](https://github.com/flightonary/Moscapsule/stargazers) - MQTT Client for iOS written in Swift.

### TCL

- [tcl-mqtt](https://github.com/Tingenek/tcl-mqtt) [![GitHub stars](https://img.shields.io/github/stars/Tingenek/tcl-mqtt?style=flat)](https://github.com/Tingenek/tcl-mqtt/stargazers) - Small library to connect to a MQTT broker. Very, very basic, and not maintained.

## Scripting

- [logic4mqtt](https://github.com/owagner/logic4mqtt) [![GitHub stars](https://img.shields.io/github/stars/owagner/logic4mqtt?style=flat)](https://github.com/owagner/logic4mqtt/stargazers) - Java based Logic and scripting engine for use with MQTT. Uses Java's general scripting interface, so scripts can be written in a multitude of languages like JavaScript, Groovy etc.
- [mqtt-scripts](https://github.com/hobbyquaker/mqtt-scripts/) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt-scripts/?style=flat)](https://github.com/hobbyquaker/mqtt-scripts//stargazers) - Node.js based script runner.
- [Node-RED](https://nodered.org/) - A visual tool for wiring the Internet of Things.

## Interfaces

### Makers

- [arduinoTemps2mqtt](https://github.com/matbor/arduinoTemps2mqtt) [![GitHub stars](https://img.shields.io/github/stars/matbor/arduinoTemps2mqtt?style=flat)](https://github.com/matbor/arduinoTemps2mqtt/stargazers) - Arduino sketch, grab One-wire Temperature's and publish to a MQTT broker.
- [Basecamp](https://github.com/ct-Open-Source/Basecamp) [![GitHub stars](https://img.shields.io/github/stars/ct-Open-Source/Basecamp?style=flat)](https://github.com/ct-Open-Source/Basecamp/stargazers) - An Arduino library to ease the use of the ESP32 in IoT projects. See [c't Magazin 2'2018 (German)](https://www.heise.de/select/ct/2018/2/1515452111258448).
- [deskmate](https://github.com/rbaron/deskmate) [![GitHub stars](https://img.shields.io/github/stars/rbaron/deskmate?style=flat)](https://github.com/rbaron/deskmate/stargazers) - A hackable & portable MQTT-powered mini dashboard and control center.
- [MySensors](https://www.mysensors.org/) - Arduino NRF24L01 based sensor network with support for an MQTT gateway.
- [RFM69-MQTT-client](https://github.com/computourist/RFM69-MQTT-client) [![GitHub stars](https://img.shields.io/github/stars/computourist/RFM69-MQTT-client?style=flat)](https://github.com/computourist/RFM69-MQTT-client/stargazers) - Arduino RFM69 based sensors and MQTT gateway.
- [rpi2mqtt](https://github.com/hobbyquaker/rpi2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/rpi2mqtt?style=flat)](https://github.com/hobbyquaker/rpi2mqtt/stargazers) - Connect a RaspberryPis GPIOs and 1-Wire Temperature Sensors to MQTT.
- [xbee2mqtt](https://github.com/xoseperez/xbee2mqtt) [![GitHub stars](https://img.shields.io/github/stars/xoseperez/xbee2mqtt?style=flat)](https://github.com/xoseperez/xbee2mqtt/stargazers) - XBee to MQTT gateway.

#### ESP
- [pubsubclient](https://github.com/knolleary/pubsubclient) [![GitHub stars](https://img.shields.io/github/stars/knolleary/pubsubclient?style=flat)](https://github.com/knolleary/pubsubclient/stargazers) - A client library for the Arduino Ethernet Shield that provides support for MQTT.
- [ESP32-BLE2MQTT](https://github.com/shmuelzon/esp32-ble2mqtt) [![GitHub stars](https://img.shields.io/github/stars/shmuelzon/esp32-ble2mqtt?style=flat)](https://github.com/shmuelzon/esp32-ble2mqtt/stargazers) - BLE to MQTT bridge, exposes BLE GATT characteristics as MQTT topics for bidirectional communication.
- [ESP8266MQTTMesh](https://github.com/PhracturedBlue/ESP8266MQTTMesh) [![GitHub stars](https://img.shields.io/github/stars/PhracturedBlue/ESP8266MQTTMesh?style=flat)](https://github.com/PhracturedBlue/ESP8266MQTTMesh/stargazers) - MQTT over mesh WiFi integrated library for ESP8266.
- [esp_mqtt](https://github.com/tuanpmt/esp_mqtt) [![GitHub stars](https://img.shields.io/github/stars/tuanpmt/esp_mqtt?style=flat)](https://github.com/tuanpmt/esp_mqtt/stargazers) - MQTT client library for ESP8266.
- [mqtt-ir-transceiver](https://github.com/piotrC4/mqtt-ir-transceiver) [![GitHub stars](https://img.shields.io/github/stars/piotrC4/mqtt-ir-transceiver?style=flat)](https://github.com/piotrC4/mqtt-ir-transceiver/stargazers) - ESP8266 based bidirectional gateway between MQTT and IR. Use with PlatformIO.
- [mqtt-with-micropython](https://docs.pycom.io/tutorials/networkprotocols/mqtt/) - Connect to MQTT with micropython and wipy/others (ESP32 inside).
- [nodemcu-gpiomqtt](https://github.com/hobbyquaker/nodemcu-gpiomqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/nodemcu-gpiomqtt?style=flat)](https://github.com/hobbyquaker/nodemcu-gpiomqtt/stargazers) - Lua script to connect ESP8266 GPIOs to MQTT.


#### Firmwares for ESP based Devices

There are many inexpensive smart home Wi-Fi devices based on inexpensive ESP8266 chip *(see: [1](https://templates.blakadder.com/index.html), [2](https://github.com/xoseperez/espurna/wiki/Hardware) [![GitHub stars](https://img.shields.io/github/stars/xoseperez/espurna/wiki/Hardware?style=flat)](https://github.com/xoseperez/espurna/wiki/Hardware/stargazers), [3](https://www.letscontrolit.com/wiki/index.php?title=ESP_Hardware))*. Most of them can be reflashed with custom firmware.
Here are complete firmwares to turn them into MQTT-controlled smart home nodes:

- [ESPEasy](https://www.letscontrolit.com/wiki/index.php?title=ESPEasy) - Turns ESP into a multifunction sensor device for <abbr title="Home automation">HA</abbr> solutions with web-based configuration.
- [ESPHome](https://esphome.io/) - Builds ESP8266/ESP32 firmware from concise YAML descriptions, uploads to and manages flashed devices.
- [Espurna](https://github.com/xoseperez/espurna) [![GitHub stars](https://img.shields.io/github/stars/xoseperez/espurna?style=flat)](https://github.com/xoseperez/espurna/stargazers) - <abbr title="Home automation">HA</abbr> firmware for ESP8266-based devices with rich web UI and ≈120 devices supported out of the box.
<!--lint disable double-link-->
- [HomeGenie Mini](https://homegenie.it/) - Smart device firmware for ESP8266/ESP32 supporting remote monitoring and controlling via MQTT with end-to-end encryption. The firmware is open source and it can be uploaded to the ESP device directly from the website.
<!--lint enable double-link-->
- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) [![GitHub stars](https://img.shields.io/github/stars/1technophile/OpenMQTTGateway?style=flat)](https://github.com/1technophile/OpenMQTTGateway/stargazers) - MQTT gateway for ESP8266, ESP32, Sonoff RF Bridge or Arduino with bidirectional 433mhz/315mhz/868mhz, Infrared communications, BLE, beacons detection, mi flora, mi jia, LYWSD02, LYWSD03MMC, Mi Scale compatibility, SMS & LORA.
- [Sonoff-Tasmota](https://github.com/arendst/Tasmota) [![GitHub stars](https://img.shields.io/github/stars/arendst/Tasmota?style=flat)](https://github.com/arendst/Tasmota/stargazers) - Firmware for ESP8266 devices with web-based configuration. ≈500 devices supported (not only Sonoffs).
- [WiFi-IoT](https://wifi-iot.com/p/wiki/) - ESP8266/ESP32 firmware builder. Partly in Russian. Free features are limited.


### Industry

- [CODESYS-MQTT](https://github.com/stefandreyer/CODESYS-MQTT) [![GitHub stars](https://img.shields.io/github/stars/stefandreyer/CODESYS-MQTT?style=flat)](https://github.com/stefandreyer/CODESYS-MQTT/stargazers) - A MQTT client for CODESYS PLC.
- [spicierModbus2mqtt](https://github.com/mbs38/spicierModbus2mqtt) [![GitHub stars](https://img.shields.io/github/stars/mbs38/spicierModbus2mqtt?style=flat)](https://github.com/mbs38/spicierModbus2mqtt/stargazers) - Modbus master which publishes register values via MQTT.
- [mqtt2opcua](https://github.com/nzfarmer1/mqtt2opcua) [![GitHub stars](https://img.shields.io/github/stars/nzfarmer1/mqtt2opcua?style=flat)](https://github.com/nzfarmer1/mqtt2opcua/stargazers) - Bi Directional MQTT to OPCUA Bridge.
- [OPC Router](https://www.opc-router.com/4_1-mqtt-client-opc-router-plug-in-en/) - MQTT Gateway (publisher/subscriber) with various plug-ins (OPC UA Bridge, SQL Bridge, REST Bridge, SAP Bridge).


### Telephony, PBX

- [agi-mqtt](https://github.com/zeha/agi-mqtt) [![GitHub stars](https://img.shields.io/github/stars/zeha/agi-mqtt?style=flat)](https://github.com/zeha/agi-mqtt/stargazers) - Interface between Asterisk and MQTT.
- [fritz2mqtt](https://github.com/akentner/fritz2mqtt) [![GitHub stars](https://img.shields.io/github/stars/akentner/fritz2mqtt?style=flat)](https://github.com/akentner/fritz2mqtt/stargazers) - Connect FRITZ!Box to MQTT.
- [sip2mqtt](https://github.com/MartyTremblay/sip2mqtt) [![GitHub stars](https://img.shields.io/github/stars/MartyTremblay/sip2mqtt?style=flat)](https://github.com/MartyTremblay/sip2mqtt/stargazers) - A SIP monitoring script that publishes incoming calls with CallerID to MQTT.
- [sms2mqtt](https://github.com/Domochip/sms2mqtt) [![GitHub stars](https://img.shields.io/github/stars/Domochip/sms2mqtt?style=flat)](https://github.com/Domochip/sms2mqtt/stargazers) - Docker Gateway to send/receive SMS through MQTT using an USB GSM dongle (gammu).


### Operating System

- [updates2mqtt](https://updates2mqtt.rhizomatics.org.uk) - Check for Docker image updates and publish to MQTT, in structure to support Home Assistant's automated Updates and Discovery.
- [mqtt-os-status](https://github.com/oskarhagberg/mqtt-os-status) [![GitHub stars](https://img.shields.io/github/stars/oskarhagberg/mqtt-os-status?style=flat)](https://github.com/oskarhagberg/mqtt-os-status/stargazers) - Operating-system related data, published to an MQTT broker at fixed intervals.
- [mqttlauncher](https://github.com/jpmens/mqtt-launcher) [![GitHub stars](https://img.shields.io/github/stars/jpmens/mqtt-launcher?style=flat)](https://github.com/jpmens/mqtt-launcher/stargazers) - Execute shell commands triggered by published MQTT messages.
- [mqttpc](https://github.com/hobbyquaker/mqttpc) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqttpc?style=flat)](https://github.com/hobbyquaker/mqttpc/stargazers) - Control processes via MQTT. Ability to send signals via MQTT and to publish stdout/stderr or pipe MQTT payloads into stdin.
- [mqttwatchdir](https://github.com/jpmens/mqtt-watchdir) [![GitHub stars](https://img.shields.io/github/stars/jpmens/mqtt-watchdir?style=flat)](https://github.com/jpmens/mqtt-watchdir/stargazers) - Recursively watch a directory for modifications and publish file content to an MQTT broker.
- [psmqtt](https://github.com/eschava/psmqtt) [![GitHub stars](https://img.shields.io/github/stars/eschava/psmqtt?style=flat)](https://github.com/eschava/psmqtt/stargazers) - Utility reporting system health and status via MQTT.
- [WinThing](https://github.com/msiedlarek/winthing) [![GitHub stars](https://img.shields.io/github/stars/msiedlarek/winthing?style=flat)](https://github.com/msiedlarek/winthing/stargazers) - Remotely control Windows through MQTT.


### Monitoring

- [mqttwarn](https://mqttwarn.readthedocs.io/en/latest/) - Route and transform MQTT notifications, with 70+ built-in adapters for databases, messaging and other notification sinks.
- [snmp2mqtt](https://c0d3.sh/andre/snmp2mqtt) - Python based SNMP v2 and v3 bridge to MQTT, active project in late 2025.
- [ccusage-mqtt](https://github.com/george-vice/ccusage-mqtt) [![GitHub stars](https://img.shields.io/github/stars/george-vice/ccusage-mqtt?style=flat)](https://github.com/george-vice/ccusage-mqtt/stargazers) - Publishes Claude Code (Anthropic's AI coding agent) usage telemetry to MQTT with Home Assistant auto-discovery. 15 sensors, mood classifier.
- [check-mqtt](https://github.com/jpmens/check-mqtt) [![GitHub stars](https://img.shields.io/github/stars/jpmens/check-mqtt?style=flat)](https://github.com/jpmens/check-mqtt/stargazers) - A Nagios/Icinga plugin for checking connectivity to an MQTT broker.
- [nag2mqtt](https://github.com/DE-IBH/nag2mqtt) [![GitHub stars](https://img.shields.io/github/stars/DE-IBH/nag2mqtt?style=flat)](https://github.com/DE-IBH/nag2mqtt/stargazers) - Nagios event broker to MQTT gateway.
- [notify-by-mqtt](https://github.com/jpmens/notify-by-mqtt) [![GitHub stars](https://img.shields.io/github/stars/jpmens/notify-by-mqtt?style=flat)](https://github.com/jpmens/notify-by-mqtt/stargazers) - A Nagios/Icinga notification module which wraps data into JSON and fires it off to an MQTT broker.
- [mqtt2notifysend](https://github.com/David-Lor/MQTT2NotifySend) [![GitHub stars](https://img.shields.io/github/stars/David-Lor/MQTT2NotifySend?style=flat)](https://github.com/David-Lor/MQTT2NotifySend/stargazers) - Subscribe to a topic and show notifications from MQTT messages on Ubuntu & other notify-send compatible Linux distros.


### Location Tracking

- [OwnTracks](https://owntracks.org/) - Location tracking and geofencing for MQTT.

### Logging

- [graylog-plugin-mqtt](https://github.com/graylog-labs/graylog-plugin-mqtt) [![GitHub stars](https://img.shields.io/github/stars/graylog-labs/graylog-plugin-mqtt?style=flat)](https://github.com/graylog-labs/graylog-plugin-mqtt/stargazers) - MQTT Input Plugin for Graylog.
- [influx4mqtt](https://github.com/hobbyquaker/influx4mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/influx4mqtt?style=flat)](https://github.com/hobbyquaker/influx4mqtt/stargazers) - Subscribe to MQTT topics and insert into InfluxDB.
- [mqtt2elasticsearch](https://github.com/hobbyquaker/mqtt2elasticsearch) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt2elasticsearch?style=flat)](https://github.com/hobbyquaker/mqtt2elasticsearch/stargazers) - Send MQTT messages to Elasticsearch.
<!--lint disable double-link-->
- [mqttwarn](https://github.com/jpmens/mqttwarn) [![GitHub stars](https://img.shields.io/github/stars/jpmens/mqttwarn?style=flat)](https://github.com/jpmens/mqttwarn/stargazers) - Use with [carbon](https://mqttwarn.readthedocs.io/en/latest/notifier-catalog.html#carbon) plugin.
<!--lint enable double-link-->
- [mqttcollect](https://github.com/jpmens/mqttcollect) [![GitHub stars](https://img.shields.io/github/stars/jpmens/mqttcollect?style=flat)](https://github.com/jpmens/mqttcollect/stargazers) - A collectd "Exec" plugin for MQTT.
- [mqtthandler](https://github.com/changyuheng/MQTTHandler) [![GitHub stars](https://img.shields.io/github/stars/changyuheng/MQTTHandler?style=flat)](https://github.com/changyuheng/MQTTHandler/stargazers) - A Python logging handler module for MQTT.
- [mqtt2mongodb](https://github.com/David-Lor/MQTT2MongoDB) [![GitHub stars](https://img.shields.io/github/stars/David-Lor/MQTT2MongoDB?style=flat)](https://github.com/David-Lor/MQTT2MongoDB/stargazers) - Subscribe to MQTT topics and insert into MongoDB.


### Smart Home Hardware Interfaces

- [airrohr2mqtt](https://c0d3.sh/smarthome/airrohr2mqtt) - Air quality monitoring integration.
- [amcrest2mqtt](https://github.com/dchesterton/amcrest2mqtt) [![GitHub stars](https://img.shields.io/github/stars/dchesterton/amcrest2mqtt?style=flat)](https://github.com/dchesterton/amcrest2mqtt/stargazers) - Amcrest doorbell to MQTT bridge. Uses Home Assistant's MQTT discovery protocol.
- [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync) [![GitHub stars](https://img.shields.io/github/stars/KristianP26/ble-scale-sync?style=flat)](https://github.com/KristianP26/ble-scale-sync/stargazers) - BLE-to-MQTT bridge for smart scales (23 brands) with Home Assistant auto-discovery. Reads weight + impedance, calculates body composition, publishes all 11 metrics with LWT and display precision. [Website](https://blescalesync.dev).
- [aqara-mqtt](https://github.com/monster1025/aqara-mqtt) [![GitHub stars](https://img.shields.io/github/stars/monster1025/aqara-mqtt?style=flat)](https://github.com/monster1025/aqara-mqtt/stargazers) - Aqara (Xiaomi) Gateway to MQTT bridge.
- [aqara2mqtt](https://github.com/hobbyquaker/aqara2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/aqara2mqtt?style=flat)](https://github.com/hobbyquaker/aqara2mqtt/stargazers) - Attach [Aqara](https://www.aqara.com) Smart Hubs to MQTT.
- [Bambuddy](https://github.com/maziggy/bambuddy) [![GitHub stars](https://img.shields.io/github/stars/maziggy/bambuddy?style=flat)](https://github.com/maziggy/bambuddy/stargazers) - Self-hosted management tool for Bambu Lab 3D printers using MQTT, with real-time monitoring, scheduling, and Home Assistant integration.
- [can2mqtt](https://github.com/c3re/can2mqtt) [![GitHub stars](https://img.shields.io/github/stars/c3re/can2mqtt?style=flat)](https://github.com/c3re/can2mqtt/stargazers) - CAN-Bus - MQTT Bridge (also works vice versa).
- [coe2mqtt](https://c0d3.sh/smarthome/coe2mqtt) - Bi-directional CAN Bus to MQTT.
- [cul2mqtt](https://github.com/hobbyquaker/cul2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/cul2mqtt?style=flat)](https://github.com/hobbyquaker/cul2mqtt/stargazers) - Interface between [Busware CUL](https://shop.busware.de/product_info.php/cPath/1/products_id/29) (868MHz RF-Devices like ELV FS20, HMS, EM, etc.) and MQTT.
- [domiqtt](https://github.com/etobi/domiqtt) [![GitHub stars](https://img.shields.io/github/stars/etobi/domiqtt?style=flat)](https://github.com/etobi/domiqtt/stargazers) - Connects to a Domiq Base (LCN) and translate from and to MQTT.
- [eno2mqtt](https://github.com/owagner/eno2mqtt) [![GitHub stars](https://img.shields.io/github/stars/owagner/eno2mqtt?style=flat)](https://github.com/owagner/eno2mqtt/stargazers) - Interface between an Enocean USB300 (TCM310) adapter and MQTT.
- [Evohome2mqtt](https://github.com/svrooij/evohome2mqtt) [![GitHub stars](https://img.shields.io/github/stars/svrooij/evohome2mqtt?style=flat)](https://github.com/svrooij/evohome2mqtt/stargazers) - MQTT Interface for the Honeywell Evohome system.
- [fronius2mqtt](https://c0d3.sh/smarthome/fronius2mqtt) - MQTT integration for Fronius SolarAPI.
- [gardena2mqtt](https://github.com/Domochip/gardena2mqtt) [![GitHub stars](https://img.shields.io/github/stars/Domochip/gardena2mqtt?style=flat)](https://github.com/Domochip/gardena2mqtt/stargazers) - Docker Gateway to control GARDENA Smart system devices (Sileno mower, Irrigation Control, etc.) through MQTT.
- [helios2mqtt](https://github.com/mreschka/helios2mqtt) [![GitHub stars](https://img.shields.io/github/stars/mreschka/helios2mqtt?style=flat)](https://github.com/mreschka/helios2mqtt/stargazers) - A daemon for syncing a helios easy controls system like my KWL EC 220D to MQTT.
- [hm2mqtt.js](https://github.com/hobbyquaker/hm2mqtt.js) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hm2mqtt.js?style=flat)](https://github.com/hobbyquaker/hm2mqtt.js/stargazers) - Interface between EQ-3's Homematic line of smarthome devices and MQTT. Supports Homematic IP.
- [homeeToMqtt](https://github.com/odig/homeeToMqtt) [![GitHub stars](https://img.shields.io/github/stars/odig/homeeToMqtt?style=flat)](https://github.com/odig/homeeToMqtt/stargazers) - Bidirectional Interface between homee and MQTT.
- [HS100toMQTT](https://github.com/dersimn/HS100toMQTT) [![GitHub stars](https://img.shields.io/github/stars/dersimn/HS100toMQTT?style=flat)](https://github.com/dersimn/HS100toMQTT/stargazers) - Gateway between TPLink HS100/HS110 and MQTT.
- [huABus](https://github.com/arboeh/huABus) [![GitHub stars](https://img.shields.io/github/stars/arboeh/huABus?style=flat)](https://github.com/arboeh/huABus/stargazers) - Home Assistant application (Add-on) and MQTT bridge for Huawei solar inverters (SUN2000/3000/5000).
- [ipcam2mqtt](https://github.com/svrooij/ipcam2mqtt) [![GitHub stars](https://img.shields.io/github/stars/svrooij/ipcam2mqtt?style=flat)](https://github.com/svrooij/ipcam2mqtt/stargazers) - A small FTP server to receive movement images from ipcameras and turn them into MQTT alerts.
- [knx-mqtt-bridge](https://github.com/pakerfeldt/knx-mqtt-bridge) [![GitHub stars](https://img.shields.io/github/stars/pakerfeldt/knx-mqtt-bridge?style=flat)](https://github.com/pakerfeldt/knx-mqtt-bridge/stargazers) - Bridges KNX and MQTT using the knx.js library.
- [knx2mqtt](https://github.com/owagner/knx2mqtt) [![GitHub stars](https://img.shields.io/github/stars/owagner/knx2mqtt?style=flat)](https://github.com/owagner/knx2mqtt/stargazers) - Interface between the KNX home automation standard and MQTT.
- [mcsMQTT](https://shop.homeseer.com/products/mcsmqtt-software-plug-in-for-hs3) - Plug-in for HS3 (HomeSeer).
- [mqtt-dss-bridge](https://github.com/cgHome/mqtt-dss-bridge) [![GitHub stars](https://img.shields.io/github/stars/cgHome/mqtt-dss-bridge?style=flat)](https://github.com/cgHome/mqtt-dss-bridge/stargazers) - MQTT digitalSTROM-Server Bridge.
- [mqtt-unifi-protect-bridge](https://github.com/terafin/mqtt-unifi-protect-bridge) [![GitHub stars](https://img.shields.io/github/stars/terafin/mqtt-unifi-protect-bridge?style=flat)](https://github.com/terafin/mqtt-unifi-protect-bridge/stargazers) - Adding motion-status from UniFi Protect Cameras to MQTT.
<!--lint disable double-link-->
- [mqtt2homekit](https://github.com/forty2/mqtt2homekit) [![GitHub stars](https://img.shields.io/github/stars/forty2/mqtt2homekit?style=flat)](https://github.com/forty2/mqtt2homekit/stargazers) - Roughly the opposite of [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homekit2mqtt?style=flat)](https://github.com/hobbyquaker/homekit2mqtt/stargazers): Control your HomeKit-enabled devices with MQTT and without Siri or iPhone.
<!--lint enable double-link-->
- [node-lox-mqtt-gateway](https://github.com/alladdin/node-lox-mqtt-gateway) [![GitHub stars](https://img.shields.io/github/stars/alladdin/node-lox-mqtt-gateway?style=flat)](https://github.com/alladdin/node-lox-mqtt-gateway/stargazers) - Gateway for Loxone™ mini server to communicate with MQTT broker.
- [smartthings-mqtt-bridge](https://github.com/stjohnjohnson/smartthings-mqtt-bridge) [![GitHub stars](https://img.shields.io/github/stars/stjohnjohnson/smartthings-mqtt-bridge?style=flat)](https://github.com/stjohnjohnson/smartthings-mqtt-bridge/stargazers) - Bridge between [SmartThings](https://www.smartthings.com/) and MQTT.
- [xiaomi2mqtt](https://github.com/svrooij/node-xiaomi2mqtt) [![GitHub stars](https://img.shields.io/github/stars/svrooij/node-xiaomi2mqtt?style=flat)](https://github.com/svrooij/node-xiaomi2mqtt/stargazers) - Bridge between the Xiaomi Smart Home Gateway Aquara and a MQTT server.
- [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) [![GitHub stars](https://img.shields.io/github/stars/Koenkk/zigbee2mqtt?style=flat)](https://github.com/Koenkk/zigbee2mqtt/stargazers) - Allows you to use your Zigbee devices without the vendors (Xiaomi/TRADFRI/Hue) bridge/gateway.
- [zwavejs2mqtt](https://github.com/zwave-js/zwavejs2mqtt) [![GitHub stars](https://img.shields.io/github/stars/zwave-js/zwavejs2mqtt?style=flat)](https://github.com/zwave-js/zwavejs2mqtt/stargazers) - Zwave to Mqtt gateway and Control Panel Web UI.


### Smart Home Integration Software

- [Home Assistant](https://www.home-assistant.io) - Home Automation system with native MQTT support, and the world's largest non-commercial Open Source project.
- [Domoticz](https://www.domoticz.com/) - Home Automation system with MQTT support.
- [FHEM](https://fhem.de/fhem.html) - Includes a [MQTT module](https://fhem.de/commandref.html#MQTT) since V5.6.
- [Home.Pi](https://github.com/denschu/home.pi) [![GitHub stars](https://img.shields.io/github/stars/denschu/home.pi?style=flat)](https://github.com/denschu/home.pi/stargazers) - Based on MQTT.
- [Homegear](https://homegear.eu/index.php/Main_Page) - Built in MQTT support.
<!--lint disable double-link-->
- [HomeGenie](https://homegenie.it/) - Supports remote controlling and monitoring via MQTT with end-to-end encryption.
- [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/homekit2mqtt?style=flat)](https://github.com/hobbyquaker/homekit2mqtt/stargazers) - Interface between [HAP-NodeJS](https://github.com/homebridge/HAP-NodeJS) [![GitHub stars](https://img.shields.io/github/stars/homebridge/HAP-NodeJS?style=flat)](https://github.com/homebridge/HAP-NodeJS/stargazers) and MQTT. Control MQTT connected devices with Siri or HomeKit Apps.
<!--lint enable double-link-->
- [ioBroker](https://github.com/ioBroker) [![GitHub stars](https://img.shields.io/github/stars/ioBroker?style=flat)](https://github.com/ioBroker/stargazers) - Includes a [MQTT adapter](https://github.com/ioBroker/ioBroker.mqtt) [![GitHub stars](https://img.shields.io/github/stars/ioBroker/ioBroker.mqtt?style=flat)](https://github.com/ioBroker/ioBroker.mqtt/stargazers).
- [openHAB](https://github.com/openhab) [![GitHub stars](https://img.shields.io/github/stars/openhab?style=flat)](https://github.com/openhab/stargazers) - Includes a [MQTT binding](https://github.com/openhab/openhab1-addons/wiki/MQTT-Binding) [![GitHub stars](https://img.shields.io/github/stars/openhab/openhab1-addons/wiki/MQTT-Binding?style=flat)](https://github.com/openhab/openhab1-addons/wiki/MQTT-Binding/stargazers).
- [openLuup](https://github.com/akbooer/openLuup) [![GitHub stars](https://img.shields.io/github/stars/akbooer/openLuup?style=flat)](https://github.com/akbooer/openLuup/stargazers) - A pure-Lua open-source emulation of the Vera Luup home automation environment with MQTT.
- [pimatic](https://pimatic.org/) - MQTT plugin included.
- [shopsavvy-mqtt](https://github.com/shopsavvy/shopsavvy-mqtt) [![GitHub stars](https://img.shields.io/github/stars/shopsavvy/shopsavvy-mqtt?style=flat)](https://github.com/shopsavvy/shopsavvy-mqtt/stargazers) - MQTT bridge that publishes product price data with Home Assistant MQTT discovery support.
- [knx2mqtt](https://c0d3.sh/smarthome/knx2mqtt) - Telegram bi-directional integration as alternative to HomeAssistant's built-in support.


### Lighting

- [Arilux_AL-LC0X](https://github.com/mertenats/Arilux_AL-LC0X) [![GitHub stars](https://img.shields.io/github/stars/mertenats/Arilux_AL-LC0X?style=flat)](https://github.com/mertenats/Arilux_AL-LC0X/stargazers) - This is an alternative firmware for Arilux LED controllers which uses MQTT.
- [chromoflex2mqtt](https://github.com/owagner/chromoflex2mqtt) [![GitHub stars](https://img.shields.io/github/stars/owagner/chromoflex2mqtt?style=flat)](https://github.com/owagner/chromoflex2mqtt/stargazers) - Control Chromoflex USP3 RGB LED modules via MQTT.
- [hue2mqtt.js](https://github.com/hobbyquaker/hue2mqtt.js) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/hue2mqtt.js?style=flat)](https://github.com/hobbyquaker/hue2mqtt.js/stargazers) - Interface between the Philips Hue bridge and MQTT.
- [MQTT DMX Controller](https://github.com/hobbyquaker/mqtt-dmx-controller) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt-dmx-controller?style=flat)](https://github.com/hobbyquaker/mqtt-dmx-controller/stargazers) - DMX Controller with MQTT support.
- [mqtt-dmx-sequencer](https://github.com/hobbyquaker/mqtt-dmx-sequencer) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqtt-dmx-sequencer?style=flat)](https://github.com/hobbyquaker/mqtt-dmx-sequencer/stargazers) - Headless counterpart to MQTT DMX Controller - use scenes and sequences exported from the MQTT DMX Controller and control them via MQTT.
- [sunricher-wifi-mqtt](https://github.com/magcode/sunricher-wifi-mqtt) [![GitHub stars](https://img.shields.io/github/stars/magcode/sunricher-wifi-mqtt?style=flat)](https://github.com/magcode/sunricher-wifi-mqtt/stargazers) - Control Sunricher LED devices using MQTT.
- [TRADFRI2MQTT](https://github.com/hardillb/TRADFRI2MQTT) [![GitHub stars](https://img.shields.io/github/stars/hardillb/TRADFRI2MQTT?style=flat)](https://github.com/hardillb/TRADFRI2MQTT/stargazers) - MQTT Bridge for IKEA TRÅDFRI Light Gateway.


### Home Entertainment

- [airtunes2mqtt](https://github.com/hobbyquaker/airtunes2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/airtunes2mqtt?style=flat)](https://github.com/hobbyquaker/airtunes2mqtt/stargazers) - MQTT controlled Multi-Room Audio with Airplay/Airtunes Devices.
- [bravia2mqtt](https://github.com/forty2/bravia2mqtt) [![GitHub stars](https://img.shields.io/github/stars/forty2/bravia2mqtt?style=flat)](https://github.com/forty2/bravia2mqtt/stargazers) - Control your Sony Bravia TV with MQTT.
- [broadlink-mqtt](https://github.com/eschava/broadlink-mqtt) [![GitHub stars](https://img.shields.io/github/stars/eschava/broadlink-mqtt?style=flat)](https://github.com/eschava/broadlink-mqtt/stargazers) - MQTT client to control BroadLink RM devices.
- [chromecast-mqtt-connector](https://github.com/nohum/chromecast-mqtt-connector) [![GitHub stars](https://img.shields.io/github/stars/nohum/chromecast-mqtt-connector?style=flat)](https://github.com/nohum/chromecast-mqtt-connector/stargazers) - Control your Google Chromecast devices using MQTT.
- [harmony-api](https://github.com/maddox/harmony-api) [![GitHub stars](https://img.shields.io/github/stars/maddox/harmony-api?style=flat)](https://github.com/maddox/harmony-api/stargazers) - A simple server allowing you to query/control multiple local Harmony Home Hubs over HTTP or MQTT.
- [htd2mqtt](https://github.com/TheOriginalAndrobot/htd2mqtt) [![GitHub stars](https://img.shields.io/github/stars/TheOriginalAndrobot/htd2mqtt?style=flat)](https://github.com/TheOriginalAndrobot/htd2mqtt/stargazers) - Bridge between an HTD Lync audio system and MQTT.
- [kodi2mqtt](https://github.com/owagner/kodi2mqtt) [![GitHub stars](https://img.shields.io/github/stars/owagner/kodi2mqtt?style=flat)](https://github.com/owagner/kodi2mqtt/stargazers) - Interface between a Kodi media center instance and MQTT.
- [lgtv2mqtt](https://github.com/hobbyquaker/lgtv2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/lgtv2mqtt?style=flat)](https://github.com/hobbyquaker/lgtv2mqtt/stargazers) - Interface between LG WebOS Smart TVs and MQTT.
- [lirc2mqtt](https://github.com/hobbyquaker/lirc2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/lirc2mqtt?style=flat)](https://github.com/hobbyquaker/lirc2mqtt/stargazers) - Send and receive infrared via [LIRC](https://www.lirc.org).
- [mopidy-mqtt](https://github.com/magcode/mopidy-mqtt) [![GitHub stars](https://img.shields.io/github/stars/magcode/mopidy-mqtt?style=flat)](https://github.com/magcode/mopidy-mqtt/stargazers) - MQTT features for Mopidy.
- [MQTT-DashCast-Docker](https://github.com/mukowman/MQTT-DashCast-Docker) [![GitHub stars](https://img.shields.io/github/stars/mukowman/MQTT-DashCast-Docker?style=flat)](https://github.com/mukowman/MQTT-DashCast-Docker/stargazers) - MQTT Docker to launch DashCast session on Chromecast.
- [mqtt2atlonamatrix](https://github.com/forty2/mqtt2atlonamatrix) [![GitHub stars](https://img.shields.io/github/stars/forty2/mqtt2atlonamatrix?style=flat)](https://github.com/forty2/mqtt2atlonamatrix/stargazers) - Control Atlona HDMI matrix switches with MQTT.
- [mqtt2tivoremote](https://github.com/forty2/mqtt2tivoremote) [![GitHub stars](https://img.shields.io/github/stars/forty2/mqtt2tivoremote?style=flat)](https://github.com/forty2/mqtt2tivoremote/stargazers) - Make TiVo DVR remote control available through an MQTT smarthome style interface.
- [onkyo2mqtt](https://github.com/owagner/onkyo2mqtt) [![GitHub stars](https://img.shields.io/github/stars/owagner/onkyo2mqtt?style=flat)](https://github.com/owagner/onkyo2mqtt/stargazers) - Interface between Onkyo AVR's EISCP network remote protocol and MQTT. Uses the onkyo-eiscp library.
- [sonos2mqtt](https://github.com/svrooij/sonos2mqtt) [![GitHub stars](https://img.shields.io/github/stars/svrooij/sonos2mqtt?style=flat)](https://github.com/svrooij/sonos2mqtt/stargazers) - A bridge between Sonos and MQTT.
- [VLC MQTT Module](https://wiki.videolan.org/Documentation:Modules/mqtt/) - Control VLC via MQTT.
- [xbmc2mqtt](https://github.com/gordonjcp/xbmc-mqtt) [![GitHub stars](https://img.shields.io/github/stars/gordonjcp/xbmc-mqtt?style=flat)](https://github.com/gordonjcp/xbmc-mqtt/stargazers) - A simple plugin for XBMC to listen for a particular topic on an MQTT broker, and display a popup message.
- [yamaha-avr2mqtt](https://github.com/akentner/yamaha-avr2mqtt) [![GitHub stars](https://img.shields.io/github/stars/akentner/yamaha-avr2mqtt?style=flat)](https://github.com/akentner/yamaha-avr2mqtt/stargazers) - A simple adapter for connection Yamaha AVR to MQTT.


### Smart Metering

- [bcontrol2mqtt](https://github.com/hobbyquaker/bcontrol2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/bcontrol2mqtt?style=flat)](https://github.com/hobbyquaker/bcontrol2mqtt/stargazers) - Publish measurements from TQ Energy Manager / [Busch-Jäger Energy Monitor](https://www.busch-jaeger.de/files/files_ONLINE/Brosch%c3%bcre_EnergyMonitor_druck.pdf) to MQTT.
- [rpi-mqtt-monitor](https://github.com/hjelev/rpi-mqtt-monitor) [![GitHub stars](https://img.shields.io/github/stars/hjelev/rpi-mqtt-monitor?style=flat)](https://github.com/hjelev/rpi-mqtt-monitor/stargazers) - The easiest way to track your Raspberry Pi or Ubuntu computer system health and performance in Home Assistant via MQTT.


### Messaging

- [mqtt-irc-bot](https://github.com/dobermai/mqtt-irc-bot) [![GitHub stars](https://img.shields.io/github/stars/dobermai/mqtt-irc-bot?style=flat)](https://github.com/dobermai/mqtt-irc-bot/stargazers) - A MQTT to IRC / IRC to MQTT bridge or bot.
<!--lint disable double-link-->
- [mqttwarn](https://github.com/jpmens/mqttwarn) [![GitHub stars](https://img.shields.io/github/stars/jpmens/mqttwarn?style=flat)](https://github.com/jpmens/mqttwarn/stargazers) - Subscribe to MQTT topics (with wildcards) and notify pluggable services.
<!--lint enable double-link-->
- [twitter-to-mqtt](https://github.com/knolleary/twitter-to-mqtt) [![GitHub stars](https://img.shields.io/github/stars/knolleary/twitter-to-mqtt?style=flat)](https://github.com/knolleary/twitter-to-mqtt/stargazers) - A python daemon that uses the Twitter Streaming API to access tweets and republishes them to an MQTT topic.


### Misc

- [AlexaMqttBridge](https://github.com/mhdawson/AlexaMqttBridge) [![GitHub stars](https://img.shields.io/github/stars/mhdawson/AlexaMqttBridge?style=flat)](https://github.com/mhdawson/AlexaMqttBridge/stargazers) - Bridge between Amazon Alexa and MQTT.
- [anpr2mqtt](https://anpr2mqtt.rhizomatics.org.uk) - Listen for images on file server, analyze and create Home Assistant entities via MQTT Discovery.
- [bt-mqtt-gateway](https://github.com/zewelor/bt-mqtt-gateway) [![GitHub stars](https://img.shields.io/github/stars/zewelor/bt-mqtt-gateway?style=flat)](https://github.com/zewelor/bt-mqtt-gateway/stargazers) - Easily extensible Bluetooth to MQTT gateway, currently supports: EQ3 smart thermostat, Xiaomi Mi Scale, Linak Desk, MySensors and Xiaomi Mi Flora plant sensor.
- [buderus2mqtt](https://github.com/krambox/buderus2mqtt) [![GitHub stars](https://img.shields.io/github/stars/krambox/buderus2mqtt?style=flat)](https://github.com/krambox/buderus2mqtt/stargazers) - Bridge between Buderus KM200 internet gateway and MQTT.
- [chrome2mqtt](https://github.com/tbowmo/chrome2mqtt) [![GitHub stars](https://img.shields.io/github/stars/tbowmo/chrome2mqtt?style=flat)](https://github.com/tbowmo/chrome2mqtt/stargazers) - Python program to enable MQTT control endpoints for chromecasts (both audio and video).
- [dashbutton2mqtt](https://github.com/hobbyquaker/dashbutton2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/dashbutton2mqtt?style=flat)](https://github.com/hobbyquaker/dashbutton2mqtt/stargazers) - Publish Amazon Dash Button presses to MQTT.
- [flowerpower2mqtt](https://github.com/hobbyquaker/flowerpower2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/flowerpower2mqtt?style=flat)](https://github.com/hobbyquaker/flowerpower2mqtt/stargazers) - Publish measurements from Parrot Flower Power plant sensors to MQTT.
- [gBridge](https://github.com/kservices/gBridge) [![GitHub stars](https://img.shields.io/github/stars/kservices/gBridge?style=flat)](https://github.com/kservices/gBridge/stargazers) - Control (almost) any smart home device, any smart home software, with Google Assistant. Therefore, it transforms actions received from Google by voice commands to MQTT messages.
- [haiku2mqtt](https://github.com/forty2/haiku2mqtt) [![GitHub stars](https://img.shields.io/github/stars/forty2/haiku2mqtt?style=flat)](https://github.com/forty2/haiku2mqtt/stargazers) - A bridge between Haiku smart fans and MQTT.
- [homely](https://github.com/baol/homely) [![GitHub stars](https://img.shields.io/github/stars/baol/homely?style=flat)](https://github.com/baol/homely/stargazers) - Collection of Go daemons for connecting Domoticz and other stuff.
- [kobold2mqtt](https://github.com/krambox/kobold2mqtt) [![GitHub stars](https://img.shields.io/github/stars/krambox/kobold2mqtt?style=flat)](https://github.com/krambox/kobold2mqtt/stargazers) - Bridge between Vorwerk Kobold Vr200 internet gateway and MQTT.
- [leaf-python-mqtt](https://github.com/glynhudson/leaf-python-mqtt) [![GitHub stars](https://img.shields.io/github/stars/glynhudson/leaf-python-mqtt?style=flat)](https://github.com/glynhudson/leaf-python-mqtt/stargazers) - Extract data from Nissan Leaf API and post to MQTT.
- [miflora-mqtt-daemon](https://github.com/ThomDietrich/miflora-mqtt-daemon) [![GitHub stars](https://img.shields.io/github/stars/ThomDietrich/miflora-mqtt-daemon?style=flat)](https://github.com/ThomDietrich/miflora-mqtt-daemon/stargazers) - Linux service to send Xiaomi Mi Flora plant sensor data to an MQTT broker.
- [MQTT.Cool](https://mqtt.cool) - A web gateway that optimizes any MQTT broker when sending real-time data to web clients with automatic throttling.
- [mqtt2ble](https://github.com/hardillb/mqtt2ble) [![GitHub stars](https://img.shields.io/github/stars/hardillb/mqtt2ble?style=flat)](https://github.com/hardillb/mqtt2ble/stargazers) - A way to bridge MQTT topics to BLE Gatt characteristics.
- [mqttclpro](https://github.com/dc297/mqttclpro) [![GitHub stars](https://img.shields.io/github/stars/dc297/mqttclpro?style=flat)](https://github.com/dc297/mqttclpro/stargazers) - MQTT Client with tasker integration Android app.
- [mqttDB](https://github.com/hobbyquaker/mqttDB) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/mqttDB?style=flat)](https://github.com/hobbyquaker/mqttDB/stargazers) - A JSON store with MQTT interface.
- [mqtt-camera-streamer](https://github.com/robmarkcole/mqtt-camera-streamer) [![GitHub stars](https://img.shields.io/github/stars/robmarkcole/mqtt-camera-streamer?style=flat)](https://github.com/robmarkcole/mqtt-camera-streamer/stargazers) - Stream images from a connected camera over MQTT & view using Streamlit.
- [MQTT Joystick Controller](https://github.com/Vincenzo-Petrolo/MQTT-Joystick-Controller) [![GitHub stars](https://img.shields.io/github/stars/Vincenzo-Petrolo/MQTT-Joystick-Controller?style=flat)](https://github.com/Vincenzo-Petrolo/MQTT-Joystick-Controller/stargazers) - Open Source Android app that lets you control everything with your smartphone. Download it from Google Play.
- [mqtt-transformer](https://github.com/tg44/mqtt-transformer) [![GitHub stars](https://img.shields.io/github/stars/tg44/mqtt-transformer?style=flat)](https://github.com/tg44/mqtt-transformer/stargazers) - A simple service which consumes, transforms and periodically republish json messages on MQTT.
- [node-mqtt-for-anki-overdrive](https://github.com/IBM-Cloud/node-mqtt-for-anki-overdrive) [![GitHub stars](https://img.shields.io/github/stars/IBM-Cloud/node-mqtt-for-anki-overdrive?style=flat)](https://github.com/IBM-Cloud/node-mqtt-for-anki-overdrive/stargazers) - Node.js Controller and MQTT API for Anki Overdrive.
- [parrot-sample](https://github.com/IBM-Cloud/parrot-sample) [![GitHub stars](https://img.shields.io/github/stars/IBM-Cloud/parrot-sample?style=flat)](https://github.com/IBM-Cloud/parrot-sample/stargazers) - Sample code which uses MQTT to control a Parrot AR Drone.
- [QuIXI](https://github.com/ixian-platform/QuIXI) [![GitHub stars](https://img.shields.io/github/stars/ixian-platform/QuIXI?style=flat)](https://github.com/ixian-platform/QuIXI/stargazers) - Bridge between the Ixian decentralized P2P network and MQTT/REST. Enables encrypted peer-to-peer messaging for IoT devices with post-quantum security (ML-KEM + AES-256 + ChaCha20).
- [serial2mqtt](https://github.com/vortex314/serial2mqtt) [![GitHub stars](https://img.shields.io/github/stars/vortex314/serial2mqtt?style=flat)](https://github.com/vortex314/serial2mqtt/stargazers) - A Linux gateway to connect low-cost microcontrollers only with a serial port to MQTT.
- [snowboy2mqtt](https://github.com/hobbyquaker/snowboy2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/snowboy2mqtt?style=flat)](https://github.com/hobbyquaker/snowboy2mqtt/stargazers) - Publish MQTT Messages on Snowboy Hotword Detection.
- [speedtest2mqtt](https://github.com/hobbyquaker/speedtest2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/speedtest2mqtt?style=flat)](https://github.com/hobbyquaker/speedtest2mqtt/stargazers) - Run speedtest-cli and publish results via MQTT.
- [unifi2mqtt](https://github.com/hobbyquaker/unifi2mqtt) [![GitHub stars](https://img.shields.io/github/stars/hobbyquaker/unifi2mqtt?style=flat)](https://github.com/hobbyquaker/unifi2mqtt/stargazers) - Publish connected clients from Ubiquiti Unifi to MQTT.
- [Valetudo](https://github.com/Hypfer/Valetudo) [![GitHub stars](https://img.shields.io/github/stars/Hypfer/Valetudo?style=flat)](https://github.com/Hypfer/Valetudo/stargazers) - Xiaomi (Roborock) Vacuum Robots Firmware with MQTT and Webinterface.
- [wlan-thermo-mqtt-addon](https://bitbucket.org/IOcastor/wlan-thermo-mqtt-addon/) - Addon for a popular DIY barbecue thermometer.
- [mqtt-tasker](https://github.com/stesie/TaskerMqtt) [![GitHub stars](https://img.shields.io/github/stars/stesie/TaskerMqtt?style=flat)](https://github.com/stesie/TaskerMqtt/stargazers) - Android Tasker mqtt plugin.
- [MQTT2ETCD](https://github.com/David-Lor/MQTT2ETCD) [![GitHub stars](https://img.shields.io/github/stars/David-Lor/MQTT2ETCD?style=flat)](https://github.com/David-Lor/MQTT2ETCD/stargazers) - MQTT-ETCD gateway: PUT keys on ETCD through MQTT, and watch ETCD key changes on MQTT topics.


## Visualization, Dashboards

- [awtSCADA](https://github.com/larionovavi-stack/awtscada) [![GitHub stars](https://img.shields.io/github/stars/larionovavi-stack/awtscada?style=flat)](https://github.com/larionovavi-stack/awtscada/stargazers) - Industrial SCADA/HMI system with MQTT support (plus IEC 61850, OPC UA, Modbus TCP). Runs from a single HTML file in any browser, zero installation. 53 function blocks, 65 graphic elements, real-time trends.
- [MQTT-Tiles](https://github.com/flespi-software/MQTT-Tiles) [![GitHub stars](https://img.shields.io/github/stars/flespi-software/MQTT-Tiles?style=flat)](https://github.com/flespi-software/MQTT-Tiles/stargazers) - MQTT-based IoT dashboard visualization tool. Allows easy dashboards sharing. Works with any MQTT broker supporting the WSS protocol.
- [Crouton](https://github.com/edfungus/Crouton) [![GitHub stars](https://img.shields.io/github/stars/edfungus/Crouton?style=flat)](https://github.com/edfungus/Crouton/stargazers) - A dashboard that taps into your IOT network, using only MQTT and JSON.
- [d3-MQTT-Topic-Tree](https://github.com/hardillb/d3-MQTT-Topic-Tree) [![GitHub stars](https://img.shields.io/github/stars/hardillb/d3-MQTT-Topic-Tree?style=flat)](https://github.com/hardillb/d3-MQTT-Topic-Tree/stargazers) - A MQTT Topic Tree viewer using the d3 collapsible tree and MQTT over websockets.
- [HelloIoT](https://github.com/adrianromero/helloiot) [![GitHub stars](https://img.shields.io/github/stars/adrianromero/helloiot?style=flat)](https://github.com/adrianromero/helloiot/stargazers) - MQTT client and dashboard application.
- [HOMR-REACT](https://github.com/klauserber/homr-react) [![GitHub stars](https://img.shields.io/github/stars/klauserber/homr-react?style=flat)](https://github.com/klauserber/homr-react/stargazers) - A configurable MQTT Visualization.
- [Linear MQTT Dashboard](https://github.com/ravendmaster/linear-mqtt-dashboard) [![GitHub stars](https://img.shields.io/github/stars/ravendmaster/linear-mqtt-dashboard?style=flat)](https://github.com/ravendmaster/linear-mqtt-dashboard/stargazers) - Easy, customizable control panel - MQTT-client.
- [MMM-mqtt](https://github.com/javiergayala/MMM-mqtt) [![GitHub stars](https://img.shields.io/github/stars/javiergayala/MMM-mqtt?style=flat)](https://github.com/javiergayala/MMM-mqtt/stargazers) - This is an extension for the MagicMirror². It provides the ability to subscribe to MQTT topics and display them.
- [MQTT Dash](https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=de) - Android App: With the app you can create dashboards for your MQTT enabled IoT Smart Home devices and applications.
- [MQTT-Hyperdash](https://github.com/kollokollo/MQTT-Hyperdash) [![GitHub stars](https://img.shields.io/github/stars/kollokollo/MQTT-Hyperdash?style=flat)](https://github.com/kollokollo/MQTT-Hyperdash/stargazers) - A universal independent MQTT Dashboard for Linux/Raspberry Pi.
- [MQTT.Cool Test Client](https://testclient-cloud.mqtt.cool) - A web interface for testing interaction between MQTT.Cool and any MQTT broker.
- [mqtt-panel](https://github.com/fabaff/mqtt-panel) [![GitHub stars](https://img.shields.io/github/stars/fabaff/mqtt-panel?style=flat)](https://github.com/fabaff/mqtt-panel/stargazers) - A web interface for MQTT.
- [mqtt-prometheus-message-exporter](https://github.com/tg44/mqtt-prometheus-message-exporter) [![GitHub stars](https://img.shields.io/github/stars/tg44/mqtt-prometheus-message-exporter?style=flat)](https://github.com/tg44/mqtt-prometheus-message-exporter/stargazers) - A small service which will convert mqtt messages to prometheus metrics.
- [mqtt-svg-dash](https://github.com/jpmens/mqtt-svg-dash) [![GitHub stars](https://img.shields.io/github/stars/jpmens/mqtt-svg-dash?style=flat)](https://github.com/jpmens/mqtt-svg-dash/stargazers) - Subscribe to MQTT, extract JSON from a message and make lights blink on an SVG page.
- [mqtt2highcharts](https://github.com/matbor/mqtt2highcharts) [![GitHub stars](https://img.shields.io/github/stars/matbor/mqtt2highcharts?style=flat)](https://github.com/matbor/mqtt2highcharts/stargazers) - Plotting live numbered data from a subscribed MQTT topic using Highcharts.
- [MYHELLOIOT](https://adrianromero.github.io/myhelloiot/) - MQTT dashboard application.
- [node-red-dashboard](https://github.com/node-red/node-red-dashboard) [![GitHub stars](https://img.shields.io/github/stars/node-red/node-red-dashboard?style=flat)](https://github.com/node-red/node-red-dashboard/stargazers) - A dashboard UI for Node-RED.
- [PlotJuggler](https://github.com/facontidavide/PlotJuggler) [![GitHub stars](https://img.shields.io/github/stars/facontidavide/PlotJuggler?style=flat)](https://github.com/facontidavide/PlotJuggler/stargazers) - Visualize time series (from sources such as: MQTT, Websockets, ZeroMQ, UDP, etc., supports data formats such as JSON, CBOR, BSON, Message Pack, etc.). It is a fast, powerful and intuitive cross-platform tool.


<!--lint disable double-link-->
Other tools that can be used to create Visualization/Dashboards can be found under [Platforms](#platforms) and [Smart Home Integration Software](#smart-home-integration-software).
<!--lint enable double-link-->

## Architecture, Convention

- [mqtt-smarthome](https://github.com/mqtt-smarthome/mqtt-smarthome) [![GitHub stars](https://img.shields.io/github/stars/mqtt-smarthome/mqtt-smarthome?style=flat)](https://github.com/mqtt-smarthome/mqtt-smarthome/stargazers) - Smart home automation with MQTT as the central message bus - Architectural proposal.
- [The Homie Convention](https://github.com/homieiot/convention) [![GitHub stars](https://img.shields.io/github/stars/homieiot/convention?style=flat)](https://github.com/homieiot/convention/stargazers) - A lightweight MQTT convention for the IoT.

## Security, Encryption

- [Let's Encrypt Mosquitto Docker Container](https://hub.docker.com/r/pythonlinks/letsencrypt-mosquitto) - Easier TLS certificate management for brokers.
- [mqttsa](https://github.com/stfbk/mqttsa) [![GitHub stars](https://img.shields.io/github/stars/stfbk/mqttsa?style=flat)](https://github.com/stfbk/mqttsa/stargazers) - Broker mis-configuration detection for cyber protection.
- [MQTT-PWN](https://github.com/akamai-threat-research/mqtt-pwn) [![GitHub stars](https://img.shields.io/github/stars/akamai-threat-research/mqtt-pwn?style=flat)](https://github.com/akamai-threat-research/mqtt-pwn/stargazers) - IoT Broker penetration-testing and security assessment operations.
- [Teserakt E4](https://teserakt.io/) - End-to-end encryption and key management for MQTT and other M2M protocols – Open-source and paid plans.
