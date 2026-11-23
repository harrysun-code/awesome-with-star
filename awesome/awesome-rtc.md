# Real-Time Communications

> 来源：[rtckit/awesome-rtc](https://github.com/rtckit/awesome-rtc)

[![GitHub stars](https://img.shields.io/github/stars/rtckit/awesome-rtc?style=flat)](https://github.com/rtckit/awesome-rtc/stargazers)

# Awesome Real Time Communications [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Protocols and methodology for near simultaneous exchange of media and data.


## Contents

- [Server Software](#server-software)
  - [General Purpose](#general-purpose)
  - [SIP Servers](#sip-servers)
  - [Media Servers](#media-servers)
  - [STUN/TURN](#stunturn)
- [Clients](#clients)
- [Operations](#operations)
  - [Monitoring](#monitoring)
  - [Testing](#testing)
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
  - [Media over QUIC](#media-over-quic)
- [Blogs](#blogs)
- [Discussion](#discussion)
- [Events and Talks](#events-and-talks)
- [Contribute](#contribute)


## Server Software

### General Purpose

- [FreeSWITCH](https://github.com/signalwire/freeswitch) [![GitHub stars](https://img.shields.io/github/stars/signalwire/freeswitch?style=flat)](https://github.com/signalwire/freeswitch/stargazers) - Open source communications server for voice, video, messaging and conferencing.
- [Asterisk](https://www.asterisk.org/) - PBX framework supporting multiple protocols and platforms.

### SIP Servers

- [Kamailio](https://www.kamailio.org/w/) - Open source SIP server for routing, registration, presence and large-scale deployments.
- [OpenSIPS](https://opensips.org/) - Open source SIP proxy and application server for VoIP platforms.
- [Routr](https://routr.io) - Cloud-native SIP proxy, registrar and location service.
- [Sippy B2BUA](https://github.com/sippy/b2bua) [![GitHub stars](https://img.shields.io/github/stars/sippy/b2bua?style=flat)](https://github.com/sippy/b2bua/stargazers) - Back-to-back user agent server written in Python.
- [Flexisip](https://github.com/BelledonneCommunications/flexisip) [![GitHub stars](https://img.shields.io/github/stars/BelledonneCommunications/flexisip?style=flat)](https://github.com/BelledonneCommunications/flexisip/stargazers) - SIP server suite comprising proxy, presence and group chat functions.
- [FreeSBC](https://github.com/rasonyang/freesbc) [![GitHub stars](https://img.shields.io/github/stars/rasonyang/freesbc?style=flat)](https://github.com/rasonyang/freesbc/stargazers) - Open source SIP/WebRTC edge proxy with an embedded RTP relay for FreeSWITCH and Asterisk.
- [P-KISS-SBC](https://github.com/mwolff44/pk-sbc) [![GitHub stars](https://img.shields.io/github/stars/mwolff44/pk-sbc?style=flat)](https://github.com/mwolff44/pk-sbc/stargazers) - Kamailio and rtpengine-based session border controller for connecting SIP trunks and PBXs.

### Media Servers

- [Janus](https://janus.conf.meetecho.com) - Lightweight open source, general purpose, WebRTC gateway.
- [LiveKit](https://github.com/livekit/livekit) [![GitHub stars](https://img.shields.io/github/stars/livekit/livekit?style=flat)](https://github.com/livekit/livekit/stargazers) - Open source WebRTC server and SDK ecosystem for real-time audio, video and data.
- [RTPProxy](https://www.rtpproxy.org) - General purpose high performance RTP proxy.
- [rtpengine](https://github.com/sipwise/rtpengine) [![GitHub stars](https://img.shields.io/github/stars/sipwise/rtpengine?style=flat)](https://github.com/sipwise/rtpengine/stargazers) - RTP and UDP based media traffic proxy, usable as a kernel module.
- [mediasoup](https://mediasoup.org) - Specialized WebRTC conferencing system.
- [SEMS](https://github.com/sems-server/sems) [![GitHub stars](https://img.shields.io/github/stars/sems-server/sems?style=flat)](https://github.com/sems-server/sems/stargazers) - Open source media and application server for SIP based VoIP services.
- [Jitsi](https://jitsi.org/projects) - A collection of RTC open source projects, with a focus on conferencing software.
- [MediaMTX](https://github.com/bluenviron/mediamtx) [![GitHub stars](https://img.shields.io/github/stars/bluenviron/mediamtx?style=flat)](https://github.com/bluenviron/mediamtx/stargazers) - Media server and proxy bridging WebRTC, RTSP, RTMP and SRT streams, with recording and playback.
- [go2rtc](https://github.com/AlexxIT/go2rtc) [![GitHub stars](https://img.shields.io/github/stars/AlexxIT/go2rtc?style=flat)](https://github.com/AlexxIT/go2rtc/stargazers) - Camera streaming gateway with WebRTC viewing, RTSP restreaming and two-way audio integrations.

### STUN/TURN

- [coturn](https://github.com/coturn/coturn) [![GitHub stars](https://img.shields.io/github/stars/coturn/coturn?style=flat)](https://github.com/coturn/coturn/stargazers) - Fully featured TURN/STUN server supporting multiple platforms.
- [eturnal](https://eturnal.net/) - Modern and scalable STUN/TURN server written in Erlang.
- [STUNner](https://github.com/l7mp/stunner) [![GitHub stars](https://img.shields.io/github/stars/l7mp/stunner?style=flat)](https://github.com/l7mp/stunner/stargazers) - Kubernetes-native STUN/TURN gateway for WebRTC media.
- [STUNTMAN](https://github.com/jselbie/stunserver) [![GitHub stars](https://img.shields.io/github/stars/jselbie/stunserver?style=flat)](https://github.com/jselbie/stunserver/stargazers) - RFC compliant open source STUN implementation.


## Clients

- [Web SIP Phone](https://github.com/rasonyang/web-sip-phone) [![GitHub stars](https://img.shields.io/github/stars/rasonyang/web-sip-phone?style=flat)](https://github.com/rasonyang/web-sip-phone/stargazers) - Chrome extension maintaining SIP/WebRTC audio for server-controlled call center agents.
- [baresip](https://github.com/baresip/baresip) [![GitHub stars](https://img.shields.io/github/stars/baresip/baresip?style=flat)](https://github.com/baresip/baresip/stargazers) - Modular SIP user agent with command-line controls, audio/video calls and pluggable media modules.


## Operations

### Monitoring

- [sngrep](https://github.com/irontec/sngrep) [![GitHub stars](https://img.shields.io/github/stars/irontec/sngrep?style=flat)](https://github.com/irontec/sngrep/stargazers) - Terminal based SIP flow viewer.
- [sip-exporter](https://github.com/aibudaevv/sip-exporter) [![GitHub stars](https://img.shields.io/github/stars/aibudaevv/sip-exporter?style=flat)](https://github.com/aibudaevv/sip-exporter/stargazers) - Open-source eBPF sensor exporting Prometheus metrics and Grafana dashboards for host-observed IPv4/UDP SIP and correlated RTP/RTCP.
- [sipgrep](https://github.com/sipcapture/sipgrep) [![GitHub stars](https://img.shields.io/github/stars/sipcapture/sipgrep?style=flat)](https://github.com/sipcapture/sipgrep/stargazers) - Console tool for sniffing, capturing and exploring SIP traffic.
- [HOMER](https://github.com/sipcapture/homer) [![GitHub stars](https://img.shields.io/github/stars/sipcapture/homer?style=flat)](https://github.com/sipcapture/homer/stargazers) - Multi-protocol capturing and monitoring framework for RTC.
- [Trickle ICE](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice) - Exposes client-side NAT traversal debug data.
- [rtcStats](https://github.com/rtcstats/rtcstats) [![GitHub stars](https://img.shields.io/github/stars/rtcstats/rtcstats?style=flat)](https://github.com/rtcstats/rtcstats/stargazers) - WebRTC API trace and getStats collection, storage and feature extraction tooling.
- [SIP3 Community Edition](https://sip3.io/docs/InstallationGuide.html) - Open source SIP/RTP capture, analysis and monitoring components with community deployment tooling.

### Testing

- [SIPp](https://github.com/SIPp/sipp) [![GitHub stars](https://img.shields.io/github/stars/SIPp/sipp?style=flat)](https://github.com/SIPp/sipp/stargazers) - Traffic generator and scenario-based test tool for the SIP protocol.
- [SIPVicious](https://github.com/EnableSecurity/sipvicious) [![GitHub stars](https://img.shields.io/github/stars/EnableSecurity/sipvicious?style=flat)](https://github.com/EnableSecurity/sipvicious/stargazers) - Suite of security tools that can be used to audit SIP based VoIP systems.
- [sipsak](https://github.com/nils-ohlmeier/sipsak) [![GitHub stars](https://img.shields.io/github/stars/nils-ohlmeier/sipsak?style=flat)](https://github.com/nils-ohlmeier/sipsak/stargazers) - SIP stress and diagnostics utility.
- [sipexer](https://github.com/miconda/sipexer) [![GitHub stars](https://img.shields.io/github/stars/miconda/sipexer?style=flat)](https://github.com/miconda/sipexer/stargazers) - Modern and flexible SIP command line tool.
- [natcheck](https://github.com/1mb-dev/natcheck) [![GitHub stars](https://img.shields.io/github/stars/1mb-dev/natcheck?style=flat)](https://github.com/1mb-dev/natcheck/stargazers) - NAT diagnosis CLI that probes STUN servers and reports mapping behaviour and a WebRTC P2P forecast.

### Web/API Interfaces

- [Eqivo](https://eqivo.org) - Open source programmable-voice/telephony API platform.
- [Kazoo](https://github.com/2600hz/kazoo/tree/4.3) [![GitHub stars](https://img.shields.io/github/stars/2600hz/kazoo/tree/4.3?style=flat)](https://github.com/2600hz/kazoo/tree/4.3/stargazers) - Legacy open source VoIP API platform built on FreeSWITCH and Kamailio, available in the public 4.3 branch.
- [FusionPBX](https://www.fusionpbx.com) - Multitenant system built on top of FreeSWITCH.
- [FreePBX](https://www.freepbx.org) - Web Manager for Asterisk.
- [Fonoster](https://github.com/fonoster/fonoster) [![GitHub stars](https://img.shields.io/github/stars/fonoster/fonoster?style=flat)](https://github.com/fonoster/fonoster/stargazers) - Open source platform for programmable voice and voice AI applications.
- [Wazo](https://wazo-platform.org) - VoIP API platform built on top of Asterisk, Kamailio and RTPEngine.
- [jambonz](https://www.jambonz.org) - Open source CPaaS built for communications service providers.
- [IVOZ Provider](https://github.com/irontec/ivozprovider) [![GitHub stars](https://img.shields.io/github/stars/irontec/ivozprovider?style=flat)](https://github.com/irontec/ivozprovider/stargazers) - Multitenant solution for VoIP telephony providers.
- [Sayna](https://github.com/SaynaAI/sayna) [![GitHub stars](https://img.shields.io/github/stars/SaynaAI/sayna?style=flat)](https://github.com/SaynaAI/sayna/stargazers) - Real-time speech infrastructure for voice AI with WebSocket streaming, SIP telephony and pluggable STT/TTS providers.
- [AI Native Call Center](https://github.com/rasonyang/ai-native-callcenter) [![GitHub stars](https://img.shields.io/github/stars/rasonyang/ai-native-callcenter?style=flat)](https://github.com/rasonyang/ai-native-callcenter/stargazers) - FreeSWITCH-based call center with speech-to-speech AI, agent queues and a web interface/API.

### Billing

- [CGRateS](https://github.com/cgrates/cgrates) [![GitHub stars](https://img.shields.io/github/stars/cgrates/cgrates?style=flat)](https://github.com/cgrates/cgrates/stargazers) - Open source rating, charging and billing engine for telecom and ISP services.


## Developer Resources

### Tutorials

- [WebRTC.org](https://webrtc.org/) - Official WebRTC guides, APIs and project resources.
- [Getting Started With WebRTC](https://webrtc.org/getting-started/overview) - Official introduction to media capture and peer-to-peer connectivity APIs.
- [WebRTC Samples](https://webrtc.github.io/samples) - Collection of samples demonstrating various parts of the WebRTC APIs.
- [WebRTC for the Curious](https://webrtcforthecurious.com/) - Open book explaining WebRTC protocols, architecture and practical debugging.

### JavaScript Libraries

- [drachtio](https://drachtio.org) - Node.js SIP server framework.
- [adapter.js](https://github.com/webrtcHacks/adapter) [![GitHub stars](https://img.shields.io/github/stars/webrtcHacks/adapter?style=flat)](https://github.com/webrtcHacks/adapter/stargazers) - JavaScript shim for abstracting WebRTC spec changes and inconsistencies.
- [JsSIP](https://jssip.net/) - Open source JavaScript SIP library with WebRTC media support.
- [simple-peer](https://github.com/feross/simple-peer) [![GitHub stars](https://img.shields.io/github/stars/feross/simple-peer?style=flat)](https://github.com/feross/simple-peer/stargazers) - WebRTC wrapper for browser media streams and data channels.
- [Peerix](https://github.com/meefik/peerix) [![GitHub stars](https://img.shields.io/github/stars/meefik/peerix?style=flat)](https://github.com/meefik/peerix/stargazers) - TypeScript WebRTC library for peer-to-peer media and data with pluggable signalling drivers.
- [PeerJS](https://peerjs.com) - Data and media peer-to-peer connection API implemented over WebRTC.
- [werift](https://github.com/shinyoshiaki/werift-webrtc) [![GitHub stars](https://img.shields.io/github/stars/shinyoshiaki/werift-webrtc?style=flat)](https://github.com/shinyoshiaki/werift-webrtc/stargazers) - TypeScript WebRTC implementation for Node.js with media, data channels and RTP/RTCP APIs.
- [Longpipe](https://longpipe.dev) - Real-time video effects for WebRTC streams in the browser: virtual background, background blur, face touch-up and auto-reframe.

### C/C++ Libraries

- [libre](https://github.com/baresip/re) [![GitHub stars](https://img.shields.io/github/stars/baresip/re?style=flat)](https://github.com/baresip/re/stargazers) - Portable SIP, SDP, RTP, SRTP and ICE/STUN/TURN library with asynchronous I/O.
- [PJSIP](https://www.pjsip.org) - Multi-protocol RTC library written in C.
- [eXosip](http://savannah.nongnu.org/projects/exosip) - eXtended osip is a mature C library for abstracting the SIP protocol.
- [libdatachannel](https://github.com/paullouisageneau/libdatachannel) [![GitHub stars](https://img.shields.io/github/stars/paullouisageneau/libdatachannel?style=flat)](https://github.com/paullouisageneau/libdatachannel/stargazers) - Standalone C/C++ library for WebRTC data channels, media transport and WebSockets.
- [icey](https://github.com/auscaster/icey) [![GitHub stars](https://img.shields.io/github/stars/auscaster/icey?style=flat)](https://github.com/auscaster/icey/stargazers) - C++20 media toolkit combining WebRTC, FFmpeg, asynchronous networking and signalling.
- [libSRTP](https://github.com/cisco/libsrtp) [![GitHub stars](https://img.shields.io/github/stars/cisco/libsrtp?style=flat)](https://github.com/cisco/libsrtp/stargazers) - Secure Real-time Transport Protocol (SRTP) library for C.
- [usrsctp](https://github.com/sctplab/usrsctp) [![GitHub stars](https://img.shields.io/github/stars/sctplab/usrsctp?style=flat)](https://github.com/sctplab/usrsctp/stargazers) - Portable Stream Control Transmission Protocol (SCTP) user-land stack.
- [Sofia-SIP](https://github.com/freeswitch/sofia-sip) [![GitHub stars](https://img.shields.io/github/stars/freeswitch/sofia-sip?style=flat)](https://github.com/freeswitch/sofia-sip/stargazers) - Open source SIP library used by FreeSWITCH.
- [GStreamer WebRTC](https://gstreamer.freedesktop.org/documentation/webrtc/) - WebRTC elements for connecting native GStreamer media pipelines to browser peers.

### Go Libraries

- [Pion](https://pion.ly) - Extensive software stack for WebRTC written in Go.
- [go-diameter](https://github.com/fiorix/go-diameter) [![GitHub stars](https://img.shields.io/github/stars/fiorix/go-diameter?style=flat)](https://github.com/fiorix/go-diameter/stargazers) - RFC compliant Diameter protocol library.

### PHP Libraries

- [RTCKit/SIP](https://github.com/rtckit/php-sip) [![GitHub stars](https://img.shields.io/github/stars/rtckit/php-sip?style=flat)](https://github.com/rtckit/php-sip/stargazers) - SIP message parsing and rendering library for PHP.

### Python Libraries

- [aiortc](https://github.com/aiortc/aiortc) [![GitHub stars](https://img.shields.io/github/stars/aiortc/aiortc?style=flat)](https://github.com/aiortc/aiortc/stargazers) - WebRTC and ORTC implementation for Python using asyncio.

### Erlang Libraries

- [ersip](https://github.com/poroh/ersip) [![GitHub stars](https://img.shields.io/github/stars/poroh/ersip?style=flat)](https://github.com/poroh/ersip/stargazers) - Library comprising building blocks for SIP applications.

### Rust Libraries

- [WebRTC.rs](https://github.com/webrtc-rs/webrtc) [![GitHub stars](https://img.shields.io/github/stars/webrtc-rs/webrtc?style=flat)](https://github.com/webrtc-rs/webrtc/stargazers) - Asynchronous WebRTC implementation in Rust with SDP, RTP, RTCP and SRTP support.

### Dart Libraries

- [dart-sip-ua](https://github.com/flutter-webrtc/dart-sip-ua) [![GitHub stars](https://img.shields.io/github/stars/flutter-webrtc/dart-sip-ua?style=flat)](https://github.com/flutter-webrtc/dart-sip-ua/stargazers) - Dart SIP user-agent stack with SIP over WebSocket and WebRTC media support.
- [Flutter WebRTC](https://github.com/flutter-webrtc/flutter-webrtc) [![GitHub stars](https://img.shields.io/github/stars/flutter-webrtc/flutter-webrtc?style=flat)](https://github.com/flutter-webrtc/flutter-webrtc/stargazers) - WebRTC bindings for Flutter applications on mobile, desktop and the web.

### Media over QUIC

Experimental implementations for live media over QUIC and WebTransport. Supported draft versions and protocol variants differ; check compatibility before combining implementations.

- [moq-rs](https://github.com/cloudflare/moq-rs) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/moq-rs?style=flat)](https://github.com/cloudflare/moq-rs/stargazers) - Rust implementation of Media over QUIC Transport with a relay and sample publishers.
- [moq](https://github.com/moq-dev/moq) [![GitHub stars](https://img.shields.io/github/stars/moq-dev/moq?style=flat)](https://github.com/moq-dev/moq/stargazers) - Rust and TypeScript libraries, relay and browser player implementing moq-lite.
- [moqtail](https://github.com/moqtail/moqtail) [![GitHub stars](https://img.shields.io/github/stars/moqtail/moqtail?style=flat)](https://github.com/moqtail/moqtail/stargazers) - Rust and TypeScript Media over QUIC Transport libraries with a relay and example clients.
- [moxygen](https://github.com/facebookexperimental/moxygen) [![GitHub stars](https://img.shields.io/github/stars/facebookexperimental/moxygen?style=flat)](https://github.com/facebookexperimental/moxygen/stargazers) - C++ Media over QUIC Transport library with a relay, sample applications and interoperability tools.
- [libquicr](https://github.com/Quicr/libquicr) [![GitHub stars](https://img.shields.io/github/stars/Quicr/libquicr?style=flat)](https://github.com/Quicr/libquicr/stargazers) - C++ Media over QUIC Transport library with publish, subscribe, capture and replay tools.
- [imquic](https://github.com/meetecho/imquic) [![GitHub stars](https://img.shields.io/github/stars/meetecho/imquic?style=flat)](https://github.com/meetecho/imquic/stargazers) - Experimental C library for QUIC and WebTransport with RTP over QUIC and Media over QUIC Transport support.


## Blogs

- [BlogGeekMe](https://bloggeek.me/blog) - Blog by Tsahi Levent-Levi with a strong focus on WebRTC.
- [WebRTC For Developers](https://www.webrtc-developers.com/) - Articles, examples and tools for WebRTC application developers.
- [WebRTCHacks](https://webrtchacks.com) - WebRTC blog by independent technologists.


## Discussion

- [FreeSWITCH Community](https://signalwire.community) - Discord community for FreeSWITCH and SignalWire users and developers.
- [discuss-webrtc](https://groups.google.com/g/discuss-webrtc) - Developer discussion group for WebRTC APIs, implementations and interoperability.


## Events and Talks

- [ClueCon](https://www.cluecon.com/) - Conference for communications and voice AI developers.
- [Kamailio World](https://www.kamailio.org/w/category/kamailio-world/) - Conference announcements and technical sessions covering Kamailio and open source RTC systems.
- [AstriCon](https://www.asterisk.org/astricon/) - Conference for Asterisk and FreePBX developers and users.
- [CommCon](https://commcon.xyz/) - RTC and open-media community events with a technical talk archive.
- [OpenSIPS Summit](https://www.opensips.org/Community/Summits) - OpenSIPS community conferences with technical presentations and proceedings.
- [FOSDEM](https://fosdem.org) - Free event for software developers, with a RTC component, held every year in Europe.
- [JanusCon](https://www.januscon.it/2024/) - Conference proceedings and technical talks for Janus and WebRTC developers.
- [TADHack](https://blog.tadhack.com/) - Telecom application hackathons, demos and event announcements.


## Related Lists

- [Awesome RTC Hacking](https://github.com/EnableSecurity/awesome-rtc-hacking) [![GitHub stars](https://img.shields.io/github/stars/EnableSecurity/awesome-rtc-hacking?style=flat)](https://github.com/EnableSecurity/awesome-rtc-hacking/stargazers) - Real Time Communications hacking and penetration testing resources.
- [Awesome 5G](https://github.com/calee0219/awesome-5g) [![GitHub stars](https://img.shields.io/github/stars/calee0219/awesome-5g?style=flat)](https://github.com/calee0219/awesome-5g/stargazers) - 5G frameworks, libraries, software and resources.
- [Awesome Cellular Hacking](https://github.com/W00t3k/Awesome-Cellular-Hacking) [![GitHub stars](https://img.shields.io/github/stars/W00t3k/Awesome-Cellular-Hacking?style=flat)](https://github.com/W00t3k/Awesome-Cellular-Hacking/stargazers) - Research resources in the 3G/4G/5G Cellular security space.
- [Awesome Telco](https://github.com/ravens/awesome-telco) [![GitHub stars](https://img.shields.io/github/stars/ravens/awesome-telco?style=flat)](https://github.com/ravens/awesome-telco/stargazers) - Telco resources and projects.
- [Awesome Asterisk](https://github.com/ictinnovations/awesome-asterisk) [![GitHub stars](https://img.shields.io/github/stars/ictinnovations/awesome-asterisk?style=flat)](https://github.com/ictinnovations/awesome-asterisk/stargazers) - Asterisk tooling: ARI, AMI and AGI libraries, call audio streaming, voice AI and testing.
- [Awesome FreeSWITCH](https://github.com/ictinnovations/awesome-freeswitch) [![GitHub stars](https://img.shields.io/github/stars/ictinnovations/awesome-freeswitch?style=flat)](https://github.com/ictinnovations/awesome-freeswitch/stargazers) - FreeSWITCH tooling: Event Socket libraries, call audio streaming, distributions and monitoring.
- [SIP Resources](https://github.com/miconda/sip-resources) [![GitHub stars](https://img.shields.io/github/stars/miconda/sip-resources?style=flat)](https://github.com/miconda/sip-resources/stargazers) - Useful SIP resources curated by Kamailio's head developer.


## Contribute

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.
