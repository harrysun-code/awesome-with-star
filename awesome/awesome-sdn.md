# Software-Defined Networking

[![GitHub stars](https://img.shields.io/github/stars/sdnds-tw/awesome-sdn?style=flat)](https://github.com/sdnds-tw/awesome-sdn/stargazers)

# Awesome SDN [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://travis-ci.org/sdnds-tw/awesome-sdn.svg?branch=master)](https://travis-ci.org/sdnds-tw/awesome-sdn)

An awesome list about Software Defined Networks (SDN)

- [Awesome SDN](#awesome-sdn)
  - [Introduction](#introduction)
  - [Network Operating System](#network-operating-system)
  - [Install Environment](#install-environment)
  - [Software Switch](#software-switch)
  - [Network Virtualization](#network-virtualization)
  - [Protocol](#protocol)
  - [Controller](#controller)
  - [Simulator/Emulator](#simulatoremulator)
  - [Language](#language)
  - [Library](#library)
  - [Test](#test)
  - [NFV](#nfv)
  - [Overlay Network](#overlay-network)
  - [Router](#router)
  - [Misc](#misc)
  - [High Performacne Network](#high-performance-network)
  - [Userspace Network Stack](#userspace-network-stack)
  - [Analytics](#analytics)
- [Resources](#resources)
  - [Books](#books)
  - [Paper](#paper)

# Introduction
  Software-defined networking (SDN) is an approach to computer networking that allows network administrators to manage network services through abstraction of higher-level functionality.
  Wiki : [Software-Defined Networking](https://en.wikipedia.org/wiki/Software-defined_networking)

# Network Operating System

- [Beluganos](https://github.com/beluganos/beluganos) [![GitHub stars](https://img.shields.io/github/stars/beluganos/beluganos?style=flat)](https://github.com/beluganos/beluganos/stargazers) - Beluganos is a new network OS designed for white-box switches (OF-DPA), which can apply large-scale networks.
- [Cumulus Linux](https://cumulusnetworks.com) - Cumulus Linux is a powerful open network operating system that allows you to automate, customize and scale using web-scale principles like the world's largest data centers.
- [FlexSwitch](https://snaproute.com/) - The first open source network protocol suite offering complete layer2/layer3 functionality for accelerating development and deployment of whitebox networking gear
- [Mion](https://github.com/opencomputeproject/mion) [![GitHub stars](https://img.shields.io/github/stars/opencomputeproject/mion?style=flat)](https://github.com/opencomputeproject/mion/stargazers) - A switch OS based on ONLP API and Yocto project.
- [OcNOS](https://www.ipinfusion.com/) - Extensive switching and routing protocol support with advanced capabilities such as MPLS and SDN
- [Open Network Linux, ONL](https://opennetlinux.org) - A Linux distribution for "bare metal" switches, that is, network forwarding devices built from commodity components.
- [OpenSwitch](http://www.openswitch.net) - A linux network operating system from Dell EMC.
- [OpenWrt](https://openwrt.org/) -  Is a Linux Operating System targeting embedded devices.
- [PicOS](http://www.pica8.com/products/picos) - A SDN OS for white box switches Layer-2/3 feature set with support for OpenFlow, OVSDB, and other protocols.
- [SONiC](https://azure.github.io/SONiC/) - Software for Open Networking in the Cloud SONiC
- [Stratum](https://stratumproject.org/) - An open source, silicon-independent switch operating system for software-defined networks

# Install Environment

- [ONIE](http://onie.org/) - ONIE enables a bare metal network switch ecosystem where end users have a choice among different network operating systems.

# Software Switch

- [BESS](https://github.com/NetSys/bess) [![GitHub stars](https://img.shields.io/github/stars/NetSys/bess?style=flat)](https://github.com/NetSys/bess/stargazers) - Berkeley Extensible Software Switch, BESS is a modular framework for software switches.
- [bmv2](https://github.com/p4lang/behavioral-model) [![GitHub stars](https://img.shields.io/github/stars/p4lang/behavioral-model?style=flat)](https://github.com/p4lang/behavioral-model/stargazers)-  A P4 software switch which is usually used as a tool to verify the funtions the developers describe in P4 language.
- [CPqD](https://github.com/CPqD/ofsoftswitch13) [![GitHub stars](https://img.shields.io/github/stars/CPqD/ofsoftswitch13?style=flat)](https://github.com/CPqD/ofsoftswitch13/stargazers)- An OpenFlow 1.3 compatible user-space software switch implementation
- [FD.IO](https://fd.io/) - Relentlessly focused on data IO speed and efficiency for more flexible and scalable networks and storage
- [Indigo](https://github.com/floodlight/indigo) [![GitHub stars](https://img.shields.io/github/stars/floodlight/indigo?style=flat)](https://github.com/floodlight/indigo/stargazers) - Indigo is an open source project aimed at enabling support for OpenFlow on physical and hypervisor switches.
- [Lagopus](https://lagopus.github.io) - A high-performance software OpenFlow 1.3 switch.
- [LINC-Switch](https://github.com/FlowForwarding/LINC-Switch) [![GitHub stars](https://img.shields.io/github/stars/FlowForwarding/LINC-Switch?style=flat)](https://github.com/FlowForwarding/LINC-Switch/stargazers) - A pure OpenFlow software switch written in Erlang
- [Open vSwitch](http://openvswitch.org/) - Open vSwitch is a production quality, multilayer virtual switch.
- [PISCES](https://www.cs.princeton.edu/~jrex/papers/pisces16.pdf) - A Programmable, Protocol-Independent Software Switch.
- [snabbswitch](https://github.com/SnabbCo/snabbswitch) [![GitHub stars](https://img.shields.io/github/stars/SnabbCo/snabbswitch?style=flat)](https://github.com/SnabbCo/snabbswitch/stargazers) - An open source virtualized Ethernet networking stack.
- [ZeroTier](https://github.com/zerotier/ZeroTierOne) [![GitHub stars](https://img.shields.io/github/stars/zerotier/ZeroTierOne?style=flat)](https://github.com/zerotier/ZeroTierOne/stargazers) - ZeroTier is a software-based managed Ethernet switch for planet Earth.

# Network Virtualization

- [FlowVisor](https://github.com/opennetworkinglab/flowvisor) [![GitHub stars](https://img.shields.io/github/stars/opennetworkinglab/flowvisor?style=flat)](https://github.com/opennetworkinglab/flowvisor/stargazers) - An OpenFlow controller that acts as a hypervisor/proxy between a switch and multiple controllers. Can slice multiple switches in parallel, effectively slicing a network.
- [OpenVirtex](https://github.com/opennetworkinglab/OpenVirteX) [![GitHub stars](https://img.shields.io/github/stars/opennetworkinglab/OpenVirteX?style=flat)](https://github.com/opennetworkinglab/OpenVirteX/stargazers) - A network hypervisor that can create multiple virtual and programmable networks on top of a single physical infrastructure.

# Protocol

- [OpenFlow](https://www.opennetworking.org/sdn-resources/openflow) - A communications protocol that gives access to the forwarding plane of a network switch or router over the network.
- [OF-Config](https://www.opennetworking.org/technical-communities/areas/specification/of-config/) - OpenFlow Management and Configuration Protocol
- [OVSDB](https://tools.ietf.org/html/rfc7047) - A communication protocol which used to manage the OpenvSwitch database.
- [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
- [OpFlex](http://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/white-paper-c11-731302.html)
- [Path Computation Element Protocol, PCEP](https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-pcep-overview.html)
- [Extensible Messaging and Presence Protocol, XMPP](https://en.wikipedia.org/wiki/XMPP)
- [P4 Runtime](https://p4.org/api/p4-runtime-putting-the-control-plane-in-charge-of-the-forwarding-plane.html)
- [gNMI](https://github.com/openconfig/gnmi/) [![GitHub stars](https://img.shields.io/github/stars/openconfig/gnmi/?style=flat)](https://github.com/openconfig/gnmi//stargazers) - gRPC Network Management Interface
- [gNOI](https://github.com/openconfig/gnoi) [![GitHub stars](https://img.shields.io/github/stars/openconfig/gnoi?style=flat)](https://github.com/openconfig/gnoi/stargazers) - gRPC Network Operations Interface

# Controller

- [Beehive Network Controller](https://github.com/kandoo/beehive-netctrl) [![GitHub stars](https://img.shields.io/github/stars/kandoo/beehive-netctrl?style=flat)](https://github.com/kandoo/beehive-netctrl/stargazers) - A distributed SDN controller built on top of Beehive. It supports OpenFlow but can be easily extended for other southbound protocols.
- [Floodlight](https://github.com/floodlight/floodlight) [![GitHub stars](https://img.shields.io/github/stars/floodlight/floodlight?style=flat)](https://github.com/floodlight/floodlight/stargazers) - A java-based OpenFlow controller.
- [IRIS](http://openiris.etri.re.kr/) - A Resursive SDN Openflow Controller created by SDN Research Section, ETRI.
- [lighty.io core](https://github.com/PantheonTechnologies/lighty-core) [![GitHub stars](https://img.shields.io/github/stars/PantheonTechnologies/lighty-core?style=flat)](https://github.com/PantheonTechnologies/lighty-core/stargazers) - lighty.io core components - An open source development framework for building Java-based SDN controllers.
- [Netrack](https://github.com/netrack/openflow) [![GitHub stars](https://img.shields.io/github/stars/netrack/openflow?style=flat)](https://github.com/netrack/openflow/stargazers) - An OpenFlow controller framework in Go.
- [NodeFlow](https://github.com/gaberger/NodeFLow) [![GitHub stars](https://img.shields.io/github/stars/gaberger/NodeFLow?style=flat)](https://github.com/gaberger/NodeFLow/stargazers) - An OpenFlow Controller Node Style.
- [NOX](https://github.com/noxrepo/nox) [![GitHub stars](https://img.shields.io/github/stars/noxrepo/nox?style=flat)](https://github.com/noxrepo/nox/stargazers) - An open source development platform for C++-based software-defined networking (*SDN*) control applications.
- [OESS](https://github.com/globalnoc/oess) [![GitHub stars](https://img.shields.io/github/stars/globalnoc/oess?style=flat)](https://github.com/globalnoc/oess/stargazers) - The Open Exchange Software Suite to configure and control OpenFlow Enabled switches.
- [ONOS](http://onosproject.org) - Open Network Operating System.
- [Open MUL](http://www.openmul.org/openmul-controller.html) - A lightweight SDN/Openflow controller written almost entirely in C from scratch.
- [Open Security Controller](https://www.opensecuritycontroller.org/) - Software-defined security orchestration solution that automates deployment of virtualized network security functions, like next-generation firewall, intrusion prevention systems and application data controllers
- [OpenContrail](https://tungsten.io/opencontrail-is-now-tungsten-fabric/) - A SDN project that utilizes SDN & NFV and provides all the necessary components for network virtualization.
- [OpenDaylight](https://www.opendaylight.org) - OpenDaylight Platform
- [OVN](http://www.openvswitch.org//support/slides/OVN-Vancouver.pdf) - OVN: Open Virtual Network for Open vSwitch
- [POX](https://github.com/noxrepo/pox) [![GitHub stars](https://img.shields.io/github/stars/noxrepo/pox?style=flat)](https://github.com/noxrepo/pox/stargazers) - An open source development platform for Python-based software-defined networking (*SDN*) control applications.
- [Ravel](https://github.com/ravel-net/ravel) [![GitHub stars](https://img.shields.io/github/stars/ravel-net/ravel?style=flat)](https://github.com/ravel-net/ravel/stargazers) - A software-defined networking (SDN) controller that uses a standard SQL database to represent the network.
- [Ryu](https://ryu-sdn.org/) - A component-based software defined networking framework.
- [Trema](https://trema.github.io/trema/) - A full-stack, easy-to-use framework for developing OpenFlow controllers in Ruby and C.
- [Vyatta](https://github.com/BRCDcomm/BVC/) [![GitHub stars](https://img.shields.io/github/stars/BRCDcomm/BVC/?style=flat)](https://github.com/BRCDcomm/BVC//stargazers) - The first commercial Controller built directly from OpenDaylight.

# Simulator/Emulator

- [Containernet](https://github.com/containernet/containernet) [![GitHub stars](https://img.shields.io/github/stars/containernet/containernet?style=flat)](https://github.com/containernet/containernet/stargazers) - Mininet fork that allows to use Docker containers as hosts in emulated networks
- [EstiNet](http://www.estinet.com/products.php?lv1=13&sn=13) - A world-renowned software tool for network planning
- [MaxiNet](http://maxinet.github.io) - MaxiNet extends the famous Mininet emulation environment to span the emulation across several physical machines. This allows to emulate very large software-defined networks.
- [Mininet](http://mininet.org/) - An Instant Virtual Network on your Laptop (or other PC)
- [ns-3](https://www.nsnam.org/) - A discrete-event network simulator that supports OpenFlow environment.
- [OpenNet](http://github.com/dlinknctu/opennet) - A simulator for software-defined wireless local area network
- [Tinynet](https://github.com/John-Lin/tinynet) [![GitHub stars](https://img.shields.io/github/stars/John-Lin/tinynet?style=flat)](https://github.com/John-Lin/tinynet/stargazers) - A lightweight instant virtual network for rapid prototyping SDN

# Language

- [Frenetic](https://github.com/frenetic-lang/frenetic) [![GitHub stars](https://img.shields.io/github/stars/frenetic-lang/frenetic?style=flat)](https://github.com/frenetic-lang/frenetic/stargazers) - The Frenetic Programming Language and Runtime System
- [NEMO](https://wiki.onosproject.org/display/ONOS/NEMO+Language) - A domain specific language (DSL) based on abstraction of network models and conclusion of operation patterns.
- [P4](http://p4.org/) - A declarative language for expressing how packets are processed by the pipeline of a network forwarding element such as a switch, NIC, router or network function appliance.
- [POF](https://dl.acm.org/citation.cfm?id=2491190) - Protocol Oblivious Forwarding
- [Pyretic](http://www.frenetic-lang.org/pyretic/) - Pyretic is one member of the Frenetic family of SDN programming languages.

# Library

- [loxigen](https://github.com/floodlight/loxigen) [![GitHub stars](https://img.shields.io/github/stars/floodlight/loxigen?style=flat)](https://github.com/floodlight/loxigen/stargazers) - LoxiGen is a tool that generates OpenFlow protocol libraries for a number of languages.
- [nettle](https://github.com/AndreasVoellmy/openflow) [![GitHub stars](https://img.shields.io/github/stars/AndreasVoellmy/openflow?style=flat)](https://github.com/AndreasVoellmy/openflow/stargazers) - A Haskell library for working with the OpenFlow protocol.
- [OCaml OpenFlow](https://github.com/frenetic-lang/ocaml-openflow) [![GitHub stars](https://img.shields.io/github/stars/frenetic-lang/ocaml-openflow?style=flat)](https://github.com/frenetic-lang/ocaml-openflow/stargazers) - A serialization and protocol library for OpenFlow.
- [oflib-node](https://github.com/TrafficLab/oflib-node) [![GitHub stars](https://img.shields.io/github/stars/TrafficLab/oflib-node?style=flat)](https://github.com/TrafficLab/oflib-node/stargazers) - Oflib-node is an OpenFlow protocol library for Node. It converts between OpenFlow wire protocol messages and Javascript objects.
- [openfaucet](https://github.com/rlenglet/openfaucet) [![GitHub stars](https://img.shields.io/github/stars/rlenglet/openfaucet?style=flat)](https://github.com/rlenglet/openfaucet/stargazers) - openfaucet is a pure Python implementation of the OpenFlow 1.0.0 protocol, based on Twisted.
- [OpenFlowJ](https://bitbucket.org/openflowj/openflowj) - A Java implementation of low-level OpenFlow packet marshalling/unmarshalling and IO operations.
- [Scapy](http://www.secdev.org/projects/scapy/) - Scapy is a powerful interactive packet manipulation program.

# Test

- [Cbenech](https://github.com/mininet/oflops/tree/master/cbench) [![GitHub stars](https://img.shields.io/github/stars/mininet/oflops/tree/master/cbench?style=flat)](https://github.com/mininet/oflops/tree/master/cbench/stargazers) - Benchmarking tool for controllers
- [nice-of](https://code.google.com/archive/p/nice-of/) - A tool to test OpenFlow controller application for the NOX controller platform.
- [oftest](https://github.com/floodlight/oftest) [![GitHub stars](https://img.shields.io/github/stars/floodlight/oftest?style=flat)](https://github.com/floodlight/oftest/stargazers) - OpenFlow Testing Framework
- [OpenSDNCore](http://www.opensdncore.org/) - Virtualisation Testbed for NFV/SDN Environment.
- [ptf](https://github.com/p4lang/ptf) [![GitHub stars](https://img.shields.io/github/stars/p4lang/ptf?style=flat)](https://github.com/p4lang/ptf/stargazers) - A python based dataplane test framework based on unittest.
- [STS](https://ucb-sts.github.com/sts/) - SDN Troubleshooting System, simulates network devices, allowing programmatically test cases generation.

# NFV

- [OPNFV](https://www.opnfv.org) - Accelerating NFV's evolution through an integrated, open platform.

# Overlay Network

- [GENEVE](https://www.redhat.com/en/blog/what-geneve) - What is GENEVE?
- [NVGRE](https://tools.ietf.org/html/draft-sridharan-virtualization-nvgre-00) - NVGRE-Network-Virtualization-using-Generic-Routing-Encapsulation
- [VXLAN](https://en.wikipedia.org/wiki/Virtual_Extensible_LAN) - Virtual Extensible LAN

# Router

- [bgp4r](https://github.com/jesnault/bgp4r) [![GitHub stars](https://img.shields.io/github/stars/jesnault/bgp4r?style=flat)](https://github.com/jesnault/bgp4r/stargazers) - BGP4R is a ruby library which enables the creation and manipulation of BGP messages. In BGP4R, all well-known BGP constructs are defined in classes.
- [BGPFeeder](https://github.com/BytemarkHosting/bgpfeeder) [![GitHub stars](https://img.shields.io/github/stars/BytemarkHosting/bgpfeeder?style=flat)](https://github.com/BytemarkHosting/bgpfeeder/stargazers)
- [Bird](http://bird.network.cz/) - The BIRD project aims to develop a fully functional dynamic IP routing daemon primarily targeted on (but not limited to) Linux, FreeBSD and other UNIX-like systems and distributed under the GNU General Public License.
- [FreeRouter](http://freerouter.nop.hu/) - Java-based vRouter
- [FRRouting](https://frrouting.org/) - An IP routing protocol suite for Linux and Unix platforms which includes protocol daemons for BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2, RIPng, PIM-SM/MSDP and LDP as well as very early support for IS-IS, EIGRP and NHRP.
- [gobgp](https://github.com/osrg/gobgp) [![GitHub stars](https://img.shields.io/github/stars/osrg/gobgp?style=flat)](https://github.com/osrg/gobgp/stargazers) - GoBGP is an open source BGP implementation designed from scratch for modern environment and implemented in a modern programming language, the Go Programming Language.
- [Quagga](http://www.quagga.net/) - Quagga is a routing software suite, providing implementations of OSPFv2, OSPFv3, RIP v1 and v2, RIPng and BGP-4 for Unix platforms, particularly FreeBSD, Linux, Solaris and NetBSD. Quagga is a fork of GNU Zebra which was developed by Kunihiro Ishiguro.
- [yabgp](https://github.com/smartbgp/yabgp) [![GitHub stars](https://img.shields.io/github/stars/smartbgp/yabgp?style=flat)](https://github.com/smartbgp/yabgp/stargazers) - YABGP is a yet another Python implementation for BGP Protocol. It can be used to establish BGP connections with all kinds of routers (include real Cisco/HuaWei/Juniper routers and some router simulators like GNS3) and receive/parse BGP messages for future analysis.

# Misc

- [Aether Project](https://www.opennetworking.org/aether/) - the first open source Enterprise 5G/LTE Edge-Cloud-as-a-Service platform (ECaaS).
- [Central Office Re-architected as a Datacenter, CORD](http://opencord.org) - Reference Implementation of a Service Delivery Platform that Provides Cloud Economies and Agility.
- [Mininet Spear Narmox](http://mininet.spear.narmox.com) - A online web service provides a visualization of Mininet Topology
- [Open Network Automation Platform, ONAP](https://www.onap.org/) - Alignment of the two projects creates a harmonized and comprehensive framework for real-time, policy-driven software automation of virtual network functions that will enable software, network, IT and cloud providers and developers to rapidly create new services.
- [Open Source MANO Community, OSM](https://osm.etsi.org/welcome/)
- [OPEN-Orchestrator Project, Open-O](https://www.open-o.org)

# High Performance Network

- [ASAP2](http://www.mellanox.com/blog/2016/12/three-ways-asap2-beats-dpdk-for-cloud-and-nfv/) - The ASAP2 accelerator is built on top of eSwitch NIC hardware, and allows either the entire virtual switch, or significant portions of virtual switch or distributed virtual router (DVR) operations to be offloaded to the Mellanox NIC
- [DPDK](http://dpdk.org/) - DPDK is a set of libraries and drivers for fast packet processing.
- [RDMA](https://en.wikipedia.org/wiki/Remote_direct_memory_access) - Remote direct memory access (RDMA) is a direct memory access from the memory of one computer into that of another without involving either one's operating system. This permits high-throughput, low-latency networking
- [XDP](https://www.iovisor.org/technology/xdp) - XDP or eXpress Data Path provides a high performance, programmable network data path in the Linux kernel as part of the IO Visor Project.
It is designed to run on any processors. The first supported CPU was Intel x86 and it is now extended to IBM POWER and ARM.


# Userspace Network Stack

- [drv-netif-dpdk](https://github.com/rumpkernel/drv-netif-dpdk) [![GitHub stars](https://img.shields.io/github/stars/rumpkernel/drv-netif-dpdk?style=flat)](https://github.com/rumpkernel/drv-netif-dpdk/stargazers) - drv-netif-dpdk is a DPDK network interface for rump kernels. The combined result is a userspace TCP/IP stack doing packet I/O via DPDK.
- [f-stack](https://github.com/F-Stack/f-stack) [![GitHub stars](https://img.shields.io/github/stars/F-Stack/f-stack?style=flat)](https://github.com/F-Stack/f-stack/stargazers) - F-Stack is an user space network development kit with high performance based on DPDK, FreeBSD TCP/IP stack and coroutine API.
- [mTCP](https://github.com/eunyoung14/mtcp) [![GitHub stars](https://img.shields.io/github/stars/eunyoung14/mtcp?style=flat)](https://github.com/eunyoung14/mtcp/stargazers) - mTCP is a highly scalable user-level TCP stack for multicore systems. mTCP source code is distributed under the Modified BSD License. For more detail, please refer to the LICENSE. The license term of io_engine driver and ported applications may differ from the mTCP’s.
- [net-next-nuse](https://github.com/libos-nuse/net-next-nuse) [![GitHub stars](https://img.shields.io/github/stars/libos-nuse/net-next-nuse?style=flat)](https://github.com/libos-nuse/net-next-nuse/stargazers) - Network Stack in Userspace (NUSE) NUSE allows us to use Linux network stack as a library which any applications can directory use by linking the library. Each application has its own network stack so, it provides an instant virtualized environment apart from a host operating system.
- [nff-go](https://github.com/intel-go/nff-go) [![GitHub stars](https://img.shields.io/github/stars/intel-go/nff-go?style=flat)](https://github.com/intel-go/nff-go/stargazers) - NFF-Go becomes part of DPDK project umbrella under Linux Foundation! Mirror repo can be found here: http://dpdk.org/browse/apps/nff-go/. We will accept patches through DPDK mail-list and standard DPDK contribution process too.

# Analytics

- [Apache Spot](http://spot.incubator.apache.org/) - Community-driven cybersecurity project, built from the ground up, to bring advanced analytics to all IT Telemetry data on an open, scalable platform
- [PNDA](http://pnda.io/) - The scalable, open source big data analytics platform for networks and services.
- [SNAS](http://www.snas.io/) - Streaming Network Analytics System (project SNAS) is a framework to collect, track and access tens of millions of routing objects (routers, peers, prefixes) in real time.

# Resources
## Books

- [DevOps for Networking](https://www.packtpub.com/networking-and-servers/devops-networking)
- [Network Algorithmics：An Interdisciplinary Approach to Designing Fast Networked Devices](https://doc.lagout.org/network/Network%20Algorithmics%20An%20Interdisciplinary%20Approach%20to%20Designing%20Fast%20Networked%20Devices.pdf)
- [Network Programmability and Automation Skills for the Next-Generation Network Engineer](http://shop.oreilly.com/product/0636920042082.do)
- [SDN: Software Defined Networks: An Authoritative Review of Network Programmability Technologies](https://www.oreilly.com/library/view/sdn-software-defined/9781449342425/)
- [SDN网络指南](https://feisky.gitbooks.io/sdn/)(OpenSource Book in Chinese by Pengfei Ni)
- [SDN核心技术剖析和实战指南](http://www.sdnlab.com/book/9480.html)
- [Software Defined Networking with OpenFlow](https://www.packtpub.com/networking-and-servers/software-defined-networking-openflow)
- [圖解OpenFlow](http://www.books.com.tw/products/CN11301942)
- [重构网络-SDN架构与实现](http://www.sdnlab.com/book/18762.html)
- [深度解析SDN: 利益、战略、技术、实践](http://www.sdnlab.com/book/9470.html)
- [软件定义网络:SDN与OpenFlow解析](http://www.sdnlab.com/book/9473.html)

## Paper

- [A Guided Tour of Data-Center Networking](http://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/40404.pdf)
- [A Survey on the Security of Stateful SDN Data Planes](https://ieeexplore.ieee.org/document/7890396)
- [High Performance Datacenter Networks: Architectures, Algorithms, and Opportunities](https://static.googleusercontent.com/media/research.google.com/zh-TW//pubs/archive/37069.pdf)
- [Re-architecting datacenter networks and stacks for low latency and high performance](http://dl.acm.org/citation.cfm?id=3098825)
- [SDN A Comprehensive Survey](https://arxiv.org/pdf/1406.0440.pdf)

## Awesome Posts
- [VXLAN L3应用EVPN，呈现完整overlay网络](https://www.sdnlab.com/19879.html)
