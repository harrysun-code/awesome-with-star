# Real-Time Communications

[![GitHub stars](https://img.shields.io/github/stars/rtckit/awesome-rtc?style=flat)](https://github.com/rtckit/awesome-rtc/stargazers)

# Awesome Real Time Communications [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Protocols and methodology for near simultaneous exchange of media and data.


## Contents

- [Server Software](#server-software)
  - [General Purpose](#general-purpose)
  - [SIP Servers](#sip-servers)
  - [Media Servers](#media-servers)
  - [STUN/TURN](#stunturn)
- [Operations](#operations)
  - [Monitoring](#monitoring)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Web/API Interfaces](#webapi-interfaces)
  - [Billing](#billing)
- [Developer Resources](#developer-resources)
  - [Tutorials](#tutorials)
  - [JavaScript Libraries](#javascript-libraries)
  - [C/C++ Libraries](#cc-libraries)
  - [Go Libraries](#go-libraries)
  - [PHP Libraries](#php-libraries)
  - [Python Libraries](#python-libraries)
  - [Erlang Libraries](#erlang-libraries)
  - [Rust Libraries](#rust-libraries)
  - [Dart Libraries](#dart-libraries)
- [Blogs](#blogs)
- [Discussion](#discussion)
- [Events](#events)
- [Related Lists](#related-lists)
- [Contribute](#contribute)


## Server Software

### General Purpose

- [FreeSWITCH](http://freeswitch.org) - Open source multi-protocol, cross-platform and software switch.
- [Asterisk](http://asterisk.org) - PBX framework supporting multiple protocols and platforms.

### SIP Servers

- [Kamailio](http://www.kamailio.org) - Open source SIP server widely deployed by carriers and providers. Formerly known as OpenSER.
- [OpenSIPS](http://www.opensips.org) - Open source SIP server, tracing its roots in OpenSER (presently Kamailio).
- [Routr](https://routr.io) - Lightweight SIP proxy, location server, and registrar written in Node.js.
- [Sippy B2BUA](https://github.com/sippy/b2bua) [![GitHub stars](https://img.shields.io/github/stars/sippy/b2bua?style=flat)](https://github.com/sippy/b2bua/stargazers) - Back-to-back user agent server written in Python.
- [Flexisip](https://github.com/BelledonneCommunications/flexisip) [![GitHub stars](https://img.shields.io/github/stars/BelledonneCommunications/flexisip?style=flat)](https://github.com/BelledonneCommunications/flexisip/stargazers) - SIP server suite comprising proxy, presence and group chat functions.

### Media Servers

- [Janus](https://janus.conf.meetecho.com) - Lightweight open source, general purpose, WebRTC gateway.
- [LiveKit](https://livekit.io) - Open-source WebRTC infrastructure for building scalable real-time audio and video applications.
- [RTPProxy](https://www.rtpproxy.org) - General purpose high performance RTP proxy.
- [RTP:Engine](https://github.com/sipwise/rtpengine) [![GitHub stars](https://img.shields.io/github/stars/sipwise/rtpengine?style=flat)](https://github.com/sipwise/rtpengine/stargazers) - RTP and UDP based media traffic proxy, usable as a kernel module.
- [mediasoup](https://mediasoup.org) - Specialized WebRTC conferencing system.
- [SEMS](https://github.com/sems-server/sems) [![GitHub stars](https://img.shields.io/github/stars/sems-server/sems?style=flat)](https://github.com/sems-server/sems/stargazers) - Open source media and application server for SIP based VoIP services.
- [Jitsi](https://jitsi.org/projects) - A collection of RTC open source projects, with a focus on conferencing software.

### STUN/TURN

- [coturn](https://github.com/coturn/coturn) [![GitHub stars](https://img.shields.io/github/stars/coturn/coturn?style=flat)](https://github.com/coturn/coturn/stargazers) - Fully featured TURN/STUN server supporting multiple platforms.
- [eturnal](https://eturnal.net/) - Modern and scalable STUN/TURN server written in Erlang.
- [natcheck](https://github.com/1mb-dev/natcheck) [![GitHub stars](https://img.shields.io/github/stars/1mb-dev/natcheck?style=flat)](https://github.com/1mb-dev/natcheck/stargazers) - NAT type diagnosis CLI. Probes STUN servers, classifies mapping behaviour per RFC 5780, and reports a WebRTC direct-P2P forecast.
- [STUNTMAN](https://github.com/jselbie/stunserver) [![GitHub stars](https://img.shields.io/github/stars/jselbie/stunserver?style=flat)](https://github.com/jselbie/stunserver/stargazers) - RFC compliant open source STUN implementation.


	## Operations

### Monitoring

- [sngrep](https://github.com/irontec/sngrep) [![GitHub stars](https://img.shields.io/github/stars/irontec/sngrep?style=flat)](https://github.com/irontec/sngrep/stargazers) - Terminal based SIP flow viewer.
- [sipgrep](https://github.com/sipcapture/sipgrep) [![GitHub stars](https://img.shields.io/github/stars/sipcapture/sipgrep?style=flat)](https://github.com/sipcapture/sipgrep/stargazers) - Console tool for sniffing, capturing and exploring SIP traffic.
- [rtpbreak](https://github.com/Naishy/rtpsplit) [![GitHub stars](https://img.shields.io/github/stars/Naishy/rtpsplit?style=flat)](https://github.com/Naishy/rtpsplit/stargazers) - Detect, reconstruct and analyze RTP sessions.
- [HOMER](https://github.com/sipcapture/homer) [![GitHub stars](https://img.shields.io/github/stars/sipcapture/homer?style=flat)](https://github.com/sipcapture/homer/stargazers) - Multi-protocol capturing and monitoring framework for RTC.
- [WebRTC Troubleshooter](https://github.com/webrtc/testrtc) [![GitHub stars](https://img.shields.io/github/stars/webrtc/testrtc?style=flat)](https://github.com/webrtc/testrtc/stargazers) - Self-hosted one stop client-side WebRTC troubleshooter.
- [Trickle ICE](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice) - Exposes client-side NAT traversal debug data.
- [SIP3](https://sip3.io) - VoIP & RTC traffic monitoring and analysis platform.

### Testing

- [SIPp](http://sipp.sourceforge.net) - Traffic generator for the SIP protocol.
- [SIPVicious](https://github.com/EnableSecurity/sipvicious) [![GitHub stars](https://img.shields.io/github/stars/EnableSecurity/sipvicious?style=flat)](https://github.com/EnableSecurity/sipvicious/stargazers) - Suite of security tools that can be used to audit SIP based VoIP systems.
- [sipsak](https://github.com/nils-ohlmeier/sipsak) [![GitHub stars](https://img.shields.io/github/stars/nils-ohlmeier/sipsak?style=flat)](https://github.com/nils-ohlmeier/sipsak/stargazers) - SIP stress and diagnostics utility.
- [sipexer](https://github.com/miconda/sipexer) [![GitHub stars](https://img.shields.io/github/stars/miconda/sipexer?style=flat)](https://github.com/miconda/sipexer/stargazers) - Modern and flexible SIP command line tool.

### Deployment

- [slimswitch](https://github.com/rtckit/slimswitch) [![GitHub stars](https://img.shields.io/github/stars/rtckit/slimswitch?style=flat)](https://github.com/rtckit/slimswitch/stargazers) - Tooling for creating lean secure FreeSWITCH Docker images.

### Web/API Interfaces

- [Eqivo](https://eqivo.org) - Open source programmable-voice/telephony API platform.
- [Kazoo](https://www.2600hz.org) - Carrier-grade VoIP API platform using FreeSWITCH and Kamailio.
- [FusionPBX](https://www.fusionpbx.com) - Multitenant system built on top of FreeSWITCH.
- [FreePBX](https://www.freepbx.org) - Web Manager for Asterisk.
- [Fonoster](https://github.com/fonoster/fonoster) [![GitHub stars](https://img.shields.io/github/stars/fonoster/fonoster?style=flat)](https://github.com/fonoster/fonoster/stargazers) - Telecommunication stack built with Node.js.
- [Wazo](https://wazo-platform.org) - VoIP API platform built on top of Asterisk, Kamailio and RTPEngine.
- [jambonz](https://www.jambonz.org) - Open source CPaaS built for communications service providers.
- [IVOZ Provider](https://github.com/irontec/ivozprovider) [![GitHub stars](https://img.shields.io/github/stars/irontec/ivozprovider?style=flat)](https://github.com/irontec/ivozprovider/stargazers) - Multitenant solution for VoIP telephony providers.
- [Sayna](https://github.com/SaynaAI/sayna) [![GitHub stars](https://img.shields.io/github/stars/SaynaAI/sayna?style=flat)](https://github.com/SaynaAI/sayna/stargazers) - Real-time speech infrastructure for voice AI with WebSocket streaming, SIP telephony and pluggable STT/TTS providers.

### Billing

- [CGRateS](http://cgrates.org) - Carrier grade open source billing/rating server.
- [A2Billing](http://www.asterisk2billing.org) - Billing system for Asterisk for multiple applications.
- [PyFreeBilling](https://github.com/mwolff44/pyfreebilling) [![GitHub stars](https://img.shields.io/github/stars/mwolff44/pyfreebilling?style=flat)](https://github.com/mwolff44/pyfreebilling/stargazers) - Wholesale billing platform for Kamailio and FreeSWITCH.


## Developer Resources

### Tutorials

- [Official Website](https://webrtc.org) - Entry level WebRTC resources.
- [Getting Started With WebRTC](https://www.html5rocks.com/en/tutorials/webrtc/basics) - WebRTC tutorial by HTML5 Rocks.
- [WebRTC Samples](https://webrtc.github.io/samples) - Collection of samples demonstrating various parts of the WebRTC APIs.
- [WebRTC Experiments](https://www.webrtc-experiment.com) - Comprehensive list of samples by Muaz Khan.
- [Interactive Codelab](https://codelabs.developers.google.com/codelabs/webrtc-web) - 30 minutes step by step live tutorial by Google.

### JavaScript Libraries

- [drachtio](https://drachtio.org) - Node.js SIP server framework.
- [adapter.js](https://github.com/webrtcHacks/adapter) [![GitHub stars](https://img.shields.io/github/stars/webrtcHacks/adapter?style=flat)](https://github.com/webrtcHacks/adapter/stargazers) - JavaScript shim for abstracting WebRTC spec changes and inconsistencies.
- [JsSIP](http://jssip.net) - Lightweight open source JavaScript SIP library.
- [sipML5](https://www.doubango.org/sipml5) - Open source JavaScript SIP client with WebRTC media stack.
- [simple-peer](https://github.com/feross/simple-peer) [![GitHub stars](https://img.shields.io/github/stars/feross/simple-peer?style=flat)](https://github.com/feross/simple-peer/stargazers) - WebRTC video, voice, and data channels abstraction for Node.js and the browser.
- [Netflux](https://github.com/coast-team/netflux) [![GitHub stars](https://img.shields.io/github/stars/coast-team/netflux?style=flat)](https://github.com/coast-team/netflux/stargazers) - Isomorphic JavaScript peer to peer transport API for client and server.
- [PeerJS](https://peerjs.com) - Data and media peer-to-peer connection API implemented over WebRTC.
- [Socio](https://github.com/Rolands-Laucis/Socio) [![GitHub stars](https://img.shields.io/github/stars/Rolands-Laucis/Socio?style=flat)](https://github.com/Rolands-Laucis/Socio/stargazers) - A WebSocket Real-Time Communication (RTC) API framework. Realtime Front-end, Back-end reactivity.

### C/C++ Libraries

- [libre](https://github.com/creytiv/re) [![GitHub stars](https://img.shields.io/github/stars/creytiv/re?style=flat)](https://github.com/creytiv/re/stargazers) - Portable SIP Stack along with companion libraries for media handling, STUN/TURN and a modular user agent.
- [PJSIP](https://www.pjsip.org) - Multi-protocol RTC library written in C.
- [eXosip](http://savannah.nongnu.org/projects/exosip) - eXtended osip is a mature C library for abstracting the SIP protocol.
- [libdatachannel](https://github.com/paullouisageneau/libdatachannel) [![GitHub stars](https://img.shields.io/github/stars/paullouisageneau/libdatachannel?style=flat)](https://github.com/paullouisageneau/libdatachannel/stargazers) - Standalone WebRTC DataChannels C++ implementation.
- [icey](https://github.com/nilstate/icey) [![GitHub stars](https://img.shields.io/github/stars/nilstate/icey?style=flat)](https://github.com/nilstate/icey/stargazers) - C++20 WebRTC media runtime with FFmpeg pipeline, Symple signalling, and RFC 5766 TURN.
- [libSRTP](https://github.com/cisco/libsrtp) [![GitHub stars](https://img.shields.io/github/stars/cisco/libsrtp?style=flat)](https://github.com/cisco/libsrtp/stargazers) - Secure Real-time Transport Protocol (SRTP) library for C.
- [usrsctp](https://github.com/sctplab/usrsctp) [![GitHub stars](https://img.shields.io/github/stars/sctplab/usrsctp?style=flat)](https://github.com/sctplab/usrsctp/stargazers) - Portable Stream Control Transmission Protocol (SCTP) user-land stack.
- [rawrtc](https://github.com/rawrtc/rawrtc) [![GitHub stars](https://img.shields.io/github/stars/rawrtc/rawrtc?style=flat)](https://github.com/rawrtc/rawrtc/stargazers) - WebRTC and ORTC library with a small footprint.
- [OSS Core](https://github.com/joegen/oss_core) [![GitHub stars](https://img.shields.io/github/stars/joegen/oss_core?style=flat)](https://github.com/joegen/oss_core/stargazers) - General purpose C++ library for Real Time Communications.
- [Open WebRTC Toolkit](https://01.org/open-webrtc-toolkit) - WebRTC development toolkit with bindings for multiple platforms.
- [Sofia-SIP](https://github.com/freeswitch/sofia-sip) [![GitHub stars](https://img.shields.io/github/stars/freeswitch/sofia-sip?style=flat)](https://github.com/freeswitch/sofia-sip/stargazers) - Open source SIP library used by FreeSWITCH.

### Go Libraries

- [Pion](https://pion.ly) - Extensive software stack for WebRTC written in Go.
- [gossip](https://github.com/StefanKopieczek/gossip) [![GitHub stars](https://img.shields.io/github/stars/StefanKopieczek/gossip?style=flat)](https://github.com/StefanKopieczek/gossip/stargazers) - SIP stack for stateful user agents written in Go.
- [siprocket](https://github.com/marv2097/siprocket) [![GitHub stars](https://img.shields.io/github/stars/marv2097/siprocket?style=flat)](https://github.com/marv2097/siprocket/stargazers) - Fast SIP and SDP packet parser.
- [go-diameter](https://github.com/fiorix/go-diameter) [![GitHub stars](https://img.shields.io/github/stars/fiorix/go-diameter?style=flat)](https://github.com/fiorix/go-diameter/stargazers) - RFC compliant Diameter protocol library.

### PHP Libraries

- [RTCKit/SIP](https://github.com/rtckit/php-sip) [![GitHub stars](https://img.shields.io/github/stars/rtckit/php-sip?style=flat)](https://github.com/rtckit/php-sip/stargazers) - RFC 3261 compliant SIP parsing and rendering library for PHP 7.4+.

### Python Libraries

- [aiortc](https://github.com/aiortc/aiortc) [![GitHub stars](https://img.shields.io/github/stars/aiortc/aiortc?style=flat)](https://github.com/aiortc/aiortc/stargazers) - WebRTC and ORTC implementation for Python using asyncio.
- [Katari](https://github.com/hyperioxx/Katari) [![GitHub stars](https://img.shields.io/github/stars/hyperioxx/Katari?style=flat)](https://github.com/hyperioxx/Katari/stargazers) - SIP stack application framework.
- [peerjs-python](https://github.com/ambianic/peerjs-python) [![GitHub stars](https://img.shields.io/github/stars/ambianic/peerjs-python?style=flat)](https://github.com/ambianic/peerjs-python/stargazers) - Python port of the PeerJS peer-to-peer connection library.

### Erlang Libraries

- [NkSIP](https://github.com/NetComposer/nksip) [![GitHub stars](https://img.shields.io/github/stars/NetComposer/nksip?style=flat)](https://github.com/NetComposer/nksip/stargazers) - Extendable SIP server framework.
- [ersip](https://github.com/poroh/ersip) [![GitHub stars](https://img.shields.io/github/stars/poroh/ersip?style=flat)](https://github.com/poroh/ersip/stargazers) - Library comprising building blocks for SIP applications.

### Rust Libraries

- [libsip](https://docs.rs/libsip/0.2.4/libsip) - SIP implementation, with a focus towards softphone clients.
- [sipcore](https://github.com/armatusmiles/sipcore) [![GitHub stars](https://img.shields.io/github/stars/armatusmiles/sipcore?style=flat)](https://github.com/armatusmiles/sipcore/stargazers) - Rust framework for creating SIP applications.
- [rtcrs/webrtc](https://github.com/rtcrs/webrtc) [![GitHub stars](https://img.shields.io/github/stars/rtcrs/webrtc?style=flat)](https://github.com/rtcrs/webrtc/stargazers) - WebRTC stack, supporting SDP, RTP, RTCP and SRTP.

### Dart Libraries

- [dart-sip-ua](https://github.com/cloudwebrtc/dart-sip-ua) [![GitHub stars](https://img.shields.io/github/stars/cloudwebrtc/dart-sip-ua?style=flat)](https://github.com/cloudwebrtc/dart-sip-ua/stargazers) - Dart-lang port of JsSIP, capable of SIP over WebSocket.


## Blogs

- [BlogGeekMe](https://bloggeek.me/blog) - Blog by Tsahi Levent-Levi with a strong focus on WebRTC.
- [SIP Adventures](https://andrewjprokop.wordpress.com) - Unified communications blog by Andrew Prokop.
- [WebRTCHacks](https://webrtchacks.com) - WebRTC blog by independent technologists.


## Discussion

- [FreeSWITCH Slack](https://signalwire.community) - Join #freeswitch and #freeswitch-dev for user and developer support.
- [discuss-webrtc](https://groups.google.com/forum/?fromgroups#!forum/discuss-webrtc) - Developer oriented Google Group for WebRTC discussions.


## Events

- [ClueCon](http://cluecon.com) - Annual conference held in Chicago for telecommunications developers. Birthplace of FreeSWITCH.
- [Kamailio World](https://www.kamailioworld.com) - Berlin hosted annual event focused on Kamailio as well as VoIP, WebRTC, IMS, VoLTE and more.
- [AstriCon](https://www.asterisk.org/community/astricon-user-conference) - Asterisk focus event held every year across the US.
- [CommCon](https://commcon.xyz) - Annual conference held in the UK focused on telecommunications in general and WebRTC in particular.
- [OpenSIPS Summit](https://www.opensips.org/events) - Meeting place for the OpenSIPS community.
- [Kranky Geek](https://krankygeek.com) - AI and RTC event in San Francisco.
- [FOSDEM](https://fosdem.org) - Free event for software developers, with a RTC component, held every year in Europe.
- [JanusCon](https://www.januscon.it) - JanusCon is a live event for Janus and RTC implementers.
- [TADHack](https://tadhack.com) - Global hackathon focused on programmable communications.


## Related Lists

- [Awesome RIPT](https://github.com/rtckit/awesome-ript) [![GitHub stars](https://img.shields.io/github/stars/rtckit/awesome-ript?style=flat)](https://github.com/rtckit/awesome-ript/stargazers) - Real Time Internet Peering for Telephony.
- [Awesome RTC Hacking](https://github.com/EnableSecurity/awesome-rtc-hacking) [![GitHub stars](https://img.shields.io/github/stars/EnableSecurity/awesome-rtc-hacking?style=flat)](https://github.com/EnableSecurity/awesome-rtc-hacking/stargazers) - Real Time Communications hacking and penetration testing resources.
- [Awesome 5G](https://github.com/calee0219/awesome-5g) [![GitHub stars](https://img.shields.io/github/stars/calee0219/awesome-5g?style=flat)](https://github.com/calee0219/awesome-5g/stargazers) - 5G frameworks, libraries, software and resources.
- [Awesome Cellular Hacking](https://github.com/W00t3k/Awesome-Cellular-Hacking) [![GitHub stars](https://img.shields.io/github/stars/W00t3k/Awesome-Cellular-Hacking?style=flat)](https://github.com/W00t3k/Awesome-Cellular-Hacking/stargazers) - Research resources in the 3G/4G/5G Cellular security space.
- [Awesome Telco](https://github.com/ravens/awesome-telco) [![GitHub stars](https://img.shields.io/github/stars/ravens/awesome-telco?style=flat)](https://github.com/ravens/awesome-telco/stargazers) - Telco resources and projects.
- [SIP Resources](https://github.com/miconda/sip-resources) [![GitHub stars](https://img.shields.io/github/stars/miconda/sip-resources?style=flat)](https://github.com/miconda/sip-resources/stargazers) - Useful SIP resources curated by Kamailio's head developer.


## Contribute

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
