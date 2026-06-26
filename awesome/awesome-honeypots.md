# Honeypots

[![GitHub stars](https://img.shields.io/github/stars/paralax/awesome-honeypots?style=flat)](https://github.com/paralax/awesome-honeypots/stargazers)

# Awesome Honeypots [![Awesome Honeypots](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome honeypots, plus related components and much more, divided into categories such as Web, services, and others, with a focus on free and open source projects.

There is no pre-established order of items in each category, the order is for contribution. If you want to contribute, please read the [guide](CONTRIBUTING.md).

Discover more awesome lists at [sindresorhus/awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers).

# Contents

- [Awesome Honeypots ](#awesome-honeypots-)
- [Contents](#contents)
  - [Related Lists](#related-lists)
  - [Honeypots](#honeypots)
  - [Honeyd Tools](#honeyd-tools)
  - [Network and Artifact Analysis](#network-and-artifact-analysis)
  - [Data Tools](#data-tools)
  - [Guides](#guides)

## Related Lists

## Commercial Honepots 
- [honerix](https://www.honerix.com) - Honerix is a distributed system for capturing web-based attacks. Honerix works by simulating vulnerable applications, with the goal of pushing attackers into deploying their malicious payload.

## <a name="honeypots"></a> Honeypots
- [awesome-pcaptools](https://github.com/caesar0301/awesome-pcaptools) [![GitHub stars](https://img.shields.io/github/stars/caesar0301/awesome-pcaptools?style=flat)](https://github.com/caesar0301/awesome-pcaptools/stargazers) - Useful in network traffic analysis.
- [awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) [![GitHub stars](https://img.shields.io/github/stars/rshipp/awesome-malware-analysis?style=flat)](https://github.com/rshipp/awesome-malware-analysis/stargazers) - Some overlap here for artifact analysis.
- [CyberBriefing IOC Feeds API](https://cyberbriefing.info) - REST API with 63K+ active IOCs from 20+ feeds. Useful for cross-referencing honeypot-captured IPs and domains against known malicious indicators. Free tier available.

## Honeypots

- Database Honeypots
    - [Acra](https://github.com/cossacklabs/acra) [![GitHub stars](https://img.shields.io/github/stars/cossacklabs/acra?style=flat)](https://github.com/cossacklabs/acra/stargazers) - Effective SQL database protection suite: strong selective encryption, SQL injections prevention, intrusion detection system based on using honeypots/poison records in the database.
    - [Delilah](https://github.com/Novetta/delilah) [![GitHub stars](https://img.shields.io/github/stars/Novetta/delilah?style=flat)](https://github.com/Novetta/delilah/stargazers) - An Elasticsearch Honeypot written in Python.
    - [ESPot](https://github.com/mycert/ESPot) [![GitHub stars](https://img.shields.io/github/stars/mycert/ESPot?style=flat)](https://github.com/mycert/ESPot/stargazers) - An Elasticsearch honeypot written in NodeJS, to capture every attempts to exploit CVE-2014-3120.
    - [Elastic honey](https://github.com/jordan-wright/elastichoney) [![GitHub stars](https://img.shields.io/github/stars/jordan-wright/elastichoney?style=flat)](https://github.com/jordan-wright/elastichoney/stargazers) - A Simple Elasticsearch Honeypot.
    - [HoneyMysql](https://github.com/xiaoxiaoleo/HoneyMysql) [![GitHub stars](https://img.shields.io/github/stars/xiaoxiaoleo/HoneyMysql?style=flat)](https://github.com/xiaoxiaoleo/HoneyMysql/stargazers) - A simple Mysql honeypot project.
    - [MongoDB-HoneyProxy](https://github.com/Plazmaz/MongoDB-HoneyProxy) [![GitHub stars](https://img.shields.io/github/stars/Plazmaz/MongoDB-HoneyProxy?style=flat)](https://github.com/Plazmaz/MongoDB-HoneyProxy/stargazers) - A MongoDB honeypot proxy.
    - [NoSQLpot](https://github.com/torque59/nosqlpot) [![GitHub stars](https://img.shields.io/github/stars/torque59/nosqlpot?style=flat)](https://github.com/torque59/nosqlpot/stargazers) - The NoSQL Honeypot Framework.
    - [mysql-honeypotd](https://github.com/sjinks/mysql-honeypotd) [![GitHub stars](https://img.shields.io/github/stars/sjinks/mysql-honeypotd?style=flat)](https://github.com/sjinks/mysql-honeypotd/stargazers) - Low interaction MySQL honeypot written in C.
    - [MysqlPot](https://github.com/schmalle/MysqlPot) [![GitHub stars](https://img.shields.io/github/stars/schmalle/MysqlPot?style=flat)](https://github.com/schmalle/MysqlPot/stargazers) - A mysql honeypot, still very very early stage.
    - [pghoney](https://github.com/betheroot/pghoney) [![GitHub stars](https://img.shields.io/github/stars/betheroot/pghoney?style=flat)](https://github.com/betheroot/pghoney/stargazers) - Low-interaction Postgres Honeypot.
    - [sticky_elephant](https://github.com/betheroot/sticky_elephant) [![GitHub stars](https://img.shields.io/github/stars/betheroot/sticky_elephant?style=flat)](https://github.com/betheroot/sticky_elephant/stargazers) - medium interaction postgresql honeypot.

  - [Delilah](https://github.com/SecurityTW/delilah) [![GitHub stars](https://img.shields.io/github/stars/SecurityTW/delilah?style=flat)](https://github.com/SecurityTW/delilah/stargazers) - Elasticsearch Honeypot written in Python (originally from Novetta).
  - [ESPot](https://github.com/mycert/ESPot) [![GitHub stars](https://img.shields.io/github/stars/mycert/ESPot?style=flat)](https://github.com/mycert/ESPot/stargazers) - Elasticsearch honeypot written in NodeJS, to capture every attempts to exploit CVE-2014-3120.
  - [ElasticPot](https://gitlab.com/bontchev/elasticpot) - An Elasticsearch Honeypot.
  - [Elastic honey](https://github.com/jordan-wright/elastichoney) [![GitHub stars](https://img.shields.io/github/stars/jordan-wright/elastichoney?style=flat)](https://github.com/jordan-wright/elastichoney/stargazers) - Simple Elasticsearch Honeypot.
  - [MongoDB-HoneyProxy](https://github.com/Plazmaz/MongoDB-HoneyProxy) [![GitHub stars](https://img.shields.io/github/stars/Plazmaz/MongoDB-HoneyProxy?style=flat)](https://github.com/Plazmaz/MongoDB-HoneyProxy/stargazers) - MongoDB honeypot proxy.
  - [NoSQLpot](https://github.com/torque59/nosqlpot) [![GitHub stars](https://img.shields.io/github/stars/torque59/nosqlpot?style=flat)](https://github.com/torque59/nosqlpot/stargazers) - Honeypot framework built on a NoSQL-style database.
  - [mysql-honeypotd](https://github.com/sjinks/mysql-honeypotd) [![GitHub stars](https://img.shields.io/github/stars/sjinks/mysql-honeypotd?style=flat)](https://github.com/sjinks/mysql-honeypotd/stargazers) - Low interaction MySQL honeypot written in C.
  - [MysqlPot](https://github.com/schmalle/MysqlPot) [![GitHub stars](https://img.shields.io/github/stars/schmalle/MysqlPot?style=flat)](https://github.com/schmalle/MysqlPot/stargazers) - MySQL honeypot, still very early stage.
  - [pghoney](https://github.com/betheroot/pghoney) [![GitHub stars](https://img.shields.io/github/stars/betheroot/pghoney?style=flat)](https://github.com/betheroot/pghoney/stargazers) - Low-interaction Postgres Honeypot.
  - [sticky_elephant](https://github.com/betheroot/sticky_elephant) [![GitHub stars](https://img.shields.io/github/stars/betheroot/sticky_elephant?style=flat)](https://github.com/betheroot/sticky_elephant/stargazers) - Medium interaction postgresql honeypot.
  - [RedisHoneyPot](https://github.com/cypwnpwnsocute/RedisHoneyPot) [![GitHub stars](https://img.shields.io/github/stars/cypwnpwnsocute/RedisHoneyPot?style=flat)](https://github.com/cypwnpwnsocute/RedisHoneyPot/stargazers) - High Interaction Honeypot Solution for Redis protocol.

- Blockchain honeypots
    - [Ethereum-honey-pot](https://github.com/jeremyfritzen/Ethereum-honey-pot) [![GitHub stars](https://img.shields.io/github/stars/jeremyfritzen/Ethereum-honey-pot?style=flat)](https://github.com/jeremyfritzen/Ethereum-honey-pot/stargazers) - Tool hacking-back hackers who tried to steal tokens.

- Web honeypots

  - [Krawl](https://github.com/BlessedRebuS/Krawl) [![GitHub stars](https://img.shields.io/github/stars/BlessedRebuS/Krawl?style=flat)](https://github.com/BlessedRebuS/Krawl/stargazers) - Lightweight deception server and anti‑crawler that deploys realistic fake web applications with low‑hanging vulnerabilities and randomly generated decoy data.
  - [Cloud Active Defense](https://github.com/SAP/cloud-active-defense?tab=readme-ov-file) [![GitHub stars](https://img.shields.io/github/stars/SAP/cloud-active-defense?tab=readme-ov-file?style=flat)](https://github.com/SAP/cloud-active-defense?tab=readme-ov-file/stargazers) - Cloud active defense lets you deploy decoys right into your cloud applications, putting adversaries into a dilemma: to hack or not to hack?
  - [Express honeypot](https://github.com/christophe77/express-honeypot) [![GitHub stars](https://img.shields.io/github/stars/christophe77/express-honeypot?style=flat)](https://github.com/christophe77/express-honeypot/stargazers) - RFI & LFI honeypot using nodeJS and express.
  - [EoHoneypotBundle](https://github.com/eymengunay/EoHoneypotBundle) [![GitHub stars](https://img.shields.io/github/stars/eymengunay/EoHoneypotBundle?style=flat)](https://github.com/eymengunay/EoHoneypotBundle/stargazers) - Honeypot type for Symfony2 forms.
  - [FCaptcha](https://github.com/WebDecoy/FCaptcha) [![GitHub stars](https://img.shields.io/github/stars/WebDecoy/FCaptcha?style=flat)](https://github.com/WebDecoy/FCaptcha/stargazers) - Self-hosted CAPTCHA that acts as an inline honeypot, detecting bots and vision AI agents through 40+ behavioral signals, headless browser fingerprinting, and SHA-256 proof of work.
  - [Glastopf](https://github.com/mushorg/glastopf) [![GitHub stars](https://img.shields.io/github/stars/mushorg/glastopf?style=flat)](https://github.com/mushorg/glastopf/stargazers) - Web Application Honeypot.
  - [Google Hack Honeypot](http://ghh.sourceforge.net) - Designed to provide reconnaissance against attackers that use search engines as a hacking tool against your resources.
  - [HellPot](https://github.com/yunginnanet/HellPot) [![GitHub stars](https://img.shields.io/github/stars/yunginnanet/HellPot?style=flat)](https://github.com/yunginnanet/HellPot/stargazers) - Honeypot that tries to crash the bots and clients that visit it's location.
  - [Laravel Application Honeypot](https://github.com/msurguy/Honeypot) [![GitHub stars](https://img.shields.io/github/stars/msurguy/Honeypot?style=flat)](https://github.com/msurguy/Honeypot/stargazers) - Simple spam prevention package for Laravel applications.
  - [Lophiid](https://github.com/mrheinen/lophiid/) [![GitHub stars](https://img.shields.io/github/stars/mrheinen/lophiid/?style=flat)](https://github.com/mrheinen/lophiid//stargazers) - Distributed web application honeypot to interact with large scale exploitation attempts.
  - [Nodepot](https://github.com/schmalle/Nodepot) [![GitHub stars](https://img.shields.io/github/stars/schmalle/Nodepot?style=flat)](https://github.com/schmalle/Nodepot/stargazers) - NodeJS web application honeypot.
  - [PasitheaHoneypot](https://github.com/Marist-Innovation-Lab/PasitheaHoneypot) [![GitHub stars](https://img.shields.io/github/stars/Marist-Innovation-Lab/PasitheaHoneypot?style=flat)](https://github.com/Marist-Innovation-Lab/PasitheaHoneypot/stargazers) - RestAPI honeypot.
  - [Servletpot](https://github.com/schmalle/servletpot) [![GitHub stars](https://img.shields.io/github/stars/schmalle/servletpot?style=flat)](https://github.com/schmalle/servletpot/stargazers) - Web application Honeypot.
  - [Shadow Daemon](https://shadowd.zecure.org/overview/introduction/) - Modular Web Application Firewall / High-Interaction Honeypot for PHP, Perl, and Python apps.
  - [StrutsHoneypot](https://github.com/Cymmetria/StrutsHoneypot) [![GitHub stars](https://img.shields.io/github/stars/Cymmetria/StrutsHoneypot?style=flat)](https://github.com/Cymmetria/StrutsHoneypot/stargazers) - Struts Apache 2 based honeypot as well as a detection module for Apache 2 servers.
  - [WebTrap](https://github.com/IllusiveNetworks-Labs/WebTrap) [![GitHub stars](https://img.shields.io/github/stars/IllusiveNetworks-Labs/WebTrap?style=flat)](https://github.com/IllusiveNetworks-Labs/WebTrap/stargazers) - Designed to create deceptive webpages to deceive and redirect attackers away from real websites.
  - [basic-auth-pot (bap)](https://github.com/bjeborn/basic-auth-pot) [![GitHub stars](https://img.shields.io/github/stars/bjeborn/basic-auth-pot?style=flat)](https://github.com/bjeborn/basic-auth-pot/stargazers) - HTTP Basic Authentication honeypot.
  - [bwpot](https://github.com/graneed/bwpot) [![GitHub stars](https://img.shields.io/github/stars/graneed/bwpot?style=flat)](https://github.com/graneed/bwpot/stargazers) - Breakable Web applications honeyPot.
  - [django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot) [![GitHub stars](https://img.shields.io/github/stars/dmpayton/django-admin-honeypot?style=flat)](https://github.com/dmpayton/django-admin-honeypot/stargazers) - Fake Django admin login screen to notify admins of attempted unauthorized access.
  - [drupo](https://github.com/d1str0/drupot) [![GitHub stars](https://img.shields.io/github/stars/d1str0/drupot?style=flat)](https://github.com/d1str0/drupot/stargazers) - Drupal Honeypot.
  - [flux](https://github.com/andrewmichaelsmith/flux) [![GitHub stars](https://img.shields.io/github/stars/andrewmichaelsmith/flux?style=flat)](https://github.com/andrewmichaelsmith/flux/stargazers) - Dynamic Web Honeypot with Canary Token Integration that is being actively maintained by LLMs.
  - [galah](https://github.com/0x4D31/galah) [![GitHub stars](https://img.shields.io/github/stars/0x4D31/galah?style=flat)](https://github.com/0x4D31/galah/stargazers) - an LLM-powered web honeypot using the OpenAI API.
  - [honeyhttpd](https://github.com/bocajspear1/honeyhttpd) [![GitHub stars](https://img.shields.io/github/stars/bocajspear1/honeyhttpd?style=flat)](https://github.com/bocajspear1/honeyhttpd/stargazers) - Python-based web server honeypot builder.
  - [honeyup](https://github.com/LogoiLab/honeyup) [![GitHub stars](https://img.shields.io/github/stars/LogoiLab/honeyup?style=flat)](https://github.com/LogoiLab/honeyup/stargazers) - An uploader honeypot designed to look like poor website security.
  - [modpot](https://github.com/referefref/modpot) [![GitHub stars](https://img.shields.io/github/stars/referefref/modpot?style=flat)](https://github.com/referefref/modpot/stargazers) - Modpot is a modular web application honeypot framework and management application written in Golang and making use of gin framework.
  - [nginx-honeypot](https://github.com/GetPageSpeed/nginx-honeypot) [![GitHub stars](https://img.shields.io/github/stars/GetPageSpeed/nginx-honeypot?style=flat)](https://github.com/GetPageSpeed/nginx-honeypot/stargazers) - A simple honeypot based on NGINX configuration that logs and blocks bots scanning for vulnerabilities.
  - [owa-honeypot](https://github.com/joda32/owa-honeypot) [![GitHub stars](https://img.shields.io/github/stars/joda32/owa-honeypot?style=flat)](https://github.com/joda32/owa-honeypot/stargazers) - A basic flask based Outlook Web Honey pot.
  - [phpmyadmin_honeypot](https://github.com/gfoss/phpmyadmin_honeypot) [![GitHub stars](https://img.shields.io/github/stars/gfoss/phpmyadmin_honeypot?style=flat)](https://github.com/gfoss/phpmyadmin_honeypot/stargazers) - Simple and effective phpMyAdmin honeypot.
  - [shockpot](https://github.com/threatstream/shockpot) [![GitHub stars](https://img.shields.io/github/stars/threatstream/shockpot?style=flat)](https://github.com/threatstream/shockpot/stargazers) - WebApp Honeypot for detecting Shell Shock exploit attempts.
  - [smart-honeypot](https://github.com/freak3dot/smart-honeypot) [![GitHub stars](https://img.shields.io/github/stars/freak3dot/smart-honeypot?style=flat)](https://github.com/freak3dot/smart-honeypot/stargazers) - PHP Script demonstrating a smart honey pot.
  - Snare/Tanner - successors to Glastopf
    - [Snare](https://github.com/mushorg/snare) [![GitHub stars](https://img.shields.io/github/stars/mushorg/snare?style=flat)](https://github.com/mushorg/snare/stargazers) - Super Next generation Advanced Reactive honeypot.
    - [Tanner](https://github.com/mushorg/tanner) [![GitHub stars](https://img.shields.io/github/stars/mushorg/tanner?style=flat)](https://github.com/mushorg/tanner/stargazers) - Evaluating SNARE events.
  - [stack-honeypot](https://github.com/CHH/stack-honeypot) [![GitHub stars](https://img.shields.io/github/stars/CHH/stack-honeypot?style=flat)](https://github.com/CHH/stack-honeypot/stargazers) - Inserts a trap for spam bots into responses.
  - [tomcat-manager-honeypot](https://github.com/helospark/tomcat-manager-honeypot) [![GitHub stars](https://img.shields.io/github/stars/helospark/tomcat-manager-honeypot?style=flat)](https://github.com/helospark/tomcat-manager-honeypot/stargazers) - Honeypot that mimics Tomcat manager endpoints. Logs requests and saves attacker's WAR file for later study.
  - WordPress honeypots
    - [HonnyPotter](https://github.com/MartinIngesen/HonnyPotter) [![GitHub stars](https://img.shields.io/github/stars/MartinIngesen/HonnyPotter?style=flat)](https://github.com/MartinIngesen/HonnyPotter/stargazers) - WordPress login honeypot for collection and analysis of failed login attempts.
    - [HoneyPress](https://github.com/kungfuguapo/HoneyPress) [![GitHub stars](https://img.shields.io/github/stars/kungfuguapo/HoneyPress?style=flat)](https://github.com/kungfuguapo/HoneyPress/stargazers) - Python based WordPress honeypot in a Docker container.
    - [wp-smart-honeypot](https://github.com/freak3dot/wp-smart-honeypot) [![GitHub stars](https://img.shields.io/github/stars/freak3dot/wp-smart-honeypot?style=flat)](https://github.com/freak3dot/wp-smart-honeypot/stargazers) - WordPress plugin to reduce comment spam with a smarter honeypot.
    - [WebDecoy](https://github.com/WebDecoy/wordpress-plugin) [![GitHub stars](https://img.shields.io/github/stars/WebDecoy/wordpress-plugin?style=flat)](https://github.com/WebDecoy/wordpress-plugin/stargazers) - Zero-configuration WordPress plugin with invisible honeypot fields, behavioral analysis, and SHA-256 proof-of-work challenges to detect bots, headless browsers, and automation frameworks.
    - [wordpot](https://github.com/gbrindisi/wordpot) [![GitHub stars](https://img.shields.io/github/stars/gbrindisi/wordpot?style=flat)](https://github.com/gbrindisi/wordpot/stargazers) - WordPress Honeypot.
  - [Python-Honeypot](https://github.com/OWASP/Python-Honeypot) [![GitHub stars](https://img.shields.io/github/stars/OWASP/Python-Honeypot?style=flat)](https://github.com/OWASP/Python-Honeypot/stargazers) - OWASP Honeypot, Automated Deception Framework.

- Service Honeypots
  - [ADBHoney](https://github.com/huuck/ADBHoney) [![GitHub stars](https://img.shields.io/github/stars/huuck/ADBHoney?style=flat)](https://github.com/huuck/ADBHoney/stargazers) - Low interaction honeypot that simulates an Android device running Android Debug Bridge (ADB) server process.
  - [AMTHoneypot](https://github.com/packetflare/amthoneypot) [![GitHub stars](https://img.shields.io/github/stars/packetflare/amthoneypot?style=flat)](https://github.com/packetflare/amthoneypot/stargazers) - Honeypot for Intel's AMT Firmware Vulnerability CVE-2017-5689.
  - [ddospot](https://github.com/aelth/ddospot) [![GitHub stars](https://img.shields.io/github/stars/aelth/ddospot?style=flat)](https://github.com/aelth/ddospot/stargazers) - NTP, DNS, SSDP, Chargen and generic UDP-based amplification DDoS honeypot.
  - [dionaea](https://github.com/DinoTools/dionaea) [![GitHub stars](https://img.shields.io/github/stars/DinoTools/dionaea?style=flat)](https://github.com/DinoTools/dionaea/stargazers) - Home of the dionaea honeypot.
  - [dhp](https://github.com/ciscocsirt/dhp) [![GitHub stars](https://img.shields.io/github/stars/ciscocsirt/dhp?style=flat)](https://github.com/ciscocsirt/dhp/stargazers) - Simple Docker Honeypot server emulating small snippets of the Docker HTTP API.
  - [DolosHoneypot](https://github.com/Marist-Innovation-Lab/DolosHoneypot) [![GitHub stars](https://img.shields.io/github/stars/Marist-Innovation-Lab/DolosHoneypot?style=flat)](https://github.com/Marist-Innovation-Lab/DolosHoneypot/stargazers) - SDN (software defined networking) honeypot.
  - [Ensnare](https://github.com/ahoernecke/ensnare) [![GitHub stars](https://img.shields.io/github/stars/ahoernecke/ensnare?style=flat)](https://github.com/ahoernecke/ensnare/stargazers) - Easy to deploy Ruby honeypot.
  - [GenAIPot](https://github.com/ls1911/GenAIPot) [![GitHub stars](https://img.shields.io/github/stars/ls1911/GenAIPot?style=flat)](https://github.com/ls1911/GenAIPot/stargazers) - The first A.I based open source honeypot. supports POP3 and SMTP protocols and generates content using A.I based on user description.
  - [Helix](https://github.com/Zeerg/helix-honeypot) [![GitHub stars](https://img.shields.io/github/stars/Zeerg/helix-honeypot?style=flat)](https://github.com/Zeerg/helix-honeypot/stargazers) - K8s API Honeypot with Active Defense Capabilities.
  - [honeycomb_plugins](https://github.com/Cymmetria/honeycomb_plugins) [![GitHub stars](https://img.shields.io/github/stars/Cymmetria/honeycomb_plugins?style=flat)](https://github.com/Cymmetria/honeycomb_plugins/stargazers) - Plugin repository for Honeycomb, the honeypot framework by Cymmetria.
  - [honeydb] (https://honeydb.io/downloads) - Multi-service honeypot that is easy to deploy and configure. Can be configured to send interaction data to to HoneyDB's centralized collectors for access via REST API.
  - [honeyntp](https://github.com/fygrave/honeyntp) [![GitHub stars](https://img.shields.io/github/stars/fygrave/honeyntp?style=flat)](https://github.com/fygrave/honeyntp/stargazers) - NTP logger/honeypot.
  - [honeypot-camera](https://github.com/alexbredo/honeypot-camera) [![GitHub stars](https://img.shields.io/github/stars/alexbredo/honeypot-camera?style=flat)](https://github.com/alexbredo/honeypot-camera/stargazers) - Observation camera honeypot.
  - [honeypot-ftp](https://github.com/alexbredo/honeypot-ftp) [![GitHub stars](https://img.shields.io/github/stars/alexbredo/honeypot-ftp?style=flat)](https://github.com/alexbredo/honeypot-ftp/stargazers) - FTP Honeypot.
  - [honeypots](https://github.com/qeeqbox/honeypots) [![GitHub stars](https://img.shields.io/github/stars/qeeqbox/honeypots?style=flat)](https://github.com/qeeqbox/honeypots/stargazers) - 25 different honeypots in a single pypi package! (dns, ftp, httpproxy, http, https, imap, mysql, pop3, postgres, redis, smb, smtp, socks5, ssh, telnet, vnc, mssql, elastic, ldap, ntp, memcache, snmp, oracle, sip and irc).
  - [honeytrap](https://github.com/honeytrap/honeytrap) [![GitHub stars](https://img.shields.io/github/stars/honeytrap/honeytrap?style=flat)](https://github.com/honeytrap/honeytrap/stargazers) - Advanced Honeypot framework written in Go that can be connected with other honeypot software.
  - [HoneyPy](https://github.com/foospidy/HoneyPy) [![GitHub stars](https://img.shields.io/github/stars/foospidy/HoneyPy?style=flat)](https://github.com/foospidy/HoneyPy/stargazers) - Low interaction honeypot.
  - [Honeygrove](https://github.com/UHH-ISS/honeygrove) [![GitHub stars](https://img.shields.io/github/stars/UHH-ISS/honeygrove?style=flat)](https://github.com/UHH-ISS/honeygrove/stargazers) - Multi-purpose modular honeypot based on Twisted.
  - [Honeyport](https://github.com/securitygeneration/Honeyport) [![GitHub stars](https://img.shields.io/github/stars/securitygeneration/Honeyport?style=flat)](https://github.com/securitygeneration/Honeyport/stargazers) - Simple honeyport written in Bash and Python.
  - [Honeyprint](https://github.com/glaslos/honeyprint) [![GitHub stars](https://img.shields.io/github/stars/glaslos/honeyprint?style=flat)](https://github.com/glaslos/honeyprint/stargazers) - Printer honeypot.
  - [Lyrebird](https://hub.docker.com/r/lyrebird/honeypot-base/) - Modern high-interaction honeypot framework.
  - [MICROS honeypot](https://github.com/Cymmetria/micros_honeypot) [![GitHub stars](https://img.shields.io/github/stars/Cymmetria/micros_honeypot?style=flat)](https://github.com/Cymmetria/micros_honeypot/stargazers) - Low interaction honeypot to detect CVE-2018-2636 in the Oracle Hospitality Simphony component of Oracle Hospitality Applications (MICROS).
  - [node-ftp-honeypot](https://github.com/christophe77/node-ftp-honeypot) [![GitHub stars](https://img.shields.io/github/stars/christophe77/node-ftp-honeypot?style=flat)](https://github.com/christophe77/node-ftp-honeypot/stargazers) - FTP server honeypot in JS.
  - [pyrdp](https://github.com/gosecure/pyrdp) [![GitHub stars](https://img.shields.io/github/stars/gosecure/pyrdp?style=flat)](https://github.com/gosecure/pyrdp/stargazers) - RDP man-in-the-middle and library for Python 3 with the ability to watch connections live or after the fact.
  - [rdppot](https://github.com/kryptoslogic/rdppot) [![GitHub stars](https://img.shields.io/github/stars/kryptoslogic/rdppot?style=flat)](https://github.com/kryptoslogic/rdppot/stargazers) - RDP honeypot
  - [RDPy](https://github.com/citronneur/rdpy) [![GitHub stars](https://img.shields.io/github/stars/citronneur/rdpy?style=flat)](https://github.com/citronneur/rdpy/stargazers) - Microsoft Remote Desktop Protocol (RDP) honeypot implemented in Python.
  - [SMB Honeypot](https://github.com/r0hi7/HoneySMB) [![GitHub stars](https://img.shields.io/github/stars/r0hi7/HoneySMB?style=flat)](https://github.com/r0hi7/HoneySMB/stargazers) - High interaction SMB service honeypot capable of capturing wannacry-like Malware.
  - [Tom's Honeypot](https://github.com/inguardians/toms_honeypot) [![GitHub stars](https://img.shields.io/github/stars/inguardians/toms_honeypot?style=flat)](https://github.com/inguardians/toms_honeypot/stargazers) - Low interaction Python honeypot.
  - [Trapster Commmunity](https://github.com/0xBallpoint/trapster-community) [![GitHub stars](https://img.shields.io/github/stars/0xBallpoint/trapster-community?style=flat)](https://github.com/0xBallpoint/trapster-community/stargazers) - Modural and easy to install Python Honeypot, with comprehensive alerting
  - [troje](https://github.com/dutchcoders/troje/) [![GitHub stars](https://img.shields.io/github/stars/dutchcoders/troje/?style=flat)](https://github.com/dutchcoders/troje//stargazers) - Honeypot that runs each connection with the service within a separate LXC container.
  - [WebLogic honeypot](https://github.com/Cymmetria/weblogic_honeypot) [![GitHub stars](https://img.shields.io/github/stars/Cymmetria/weblogic_honeypot?style=flat)](https://github.com/Cymmetria/weblogic_honeypot/stargazers) - Low interaction honeypot to detect CVE-2017-10271 in the Oracle WebLogic Server component of Oracle Fusion Middleware.
  - [WhiteFace Honeypot](https://github.com/csirtgadgets/csirtg-honeypot) [![GitHub stars](https://img.shields.io/github/stars/csirtgadgets/csirtg-honeypot?style=flat)](https://github.com/csirtgadgets/csirtg-honeypot/stargazers) - Twisted based honeypot for WhiteFace.
 
- Distributed Honeypots

  - [DemonHunter](https://github.com/RevengeComing/DemonHunter) [![GitHub stars](https://img.shields.io/github/stars/RevengeComing/DemonHunter?style=flat)](https://github.com/RevengeComing/DemonHunter/stargazers) - Low interaction honeypot server.

- Anti-honeypot stuff

  - [canarytokendetector](https://github.com/referefref/canarytokendetector) [![GitHub stars](https://img.shields.io/github/stars/referefref/canarytokendetector?style=flat)](https://github.com/referefref/canarytokendetector/stargazers) - Tool for detection and nullification of Thinkst CanaryTokens
  - [honeydet](https://github.com/referefref/honeydet) [![GitHub stars](https://img.shields.io/github/stars/referefref/honeydet?style=flat)](https://github.com/referefref/honeydet/stargazers) - Signature based honeypot detector tool written in Golang
  - [kippo_detect](https://github.com/andrew-morris/kippo_detect) [![GitHub stars](https://img.shields.io/github/stars/andrew-morris/kippo_detect?style=flat)](https://github.com/andrew-morris/kippo_detect/stargazers) - Offensive component that detects the presence of the kippo honeypot.
  - [potsnitch](https://github.com/f0rw4rd/potsnitch) [![GitHub stars](https://img.shields.io/github/stars/f0rw4rd/potsnitch?style=flat)](https://github.com/f0rw4rd/potsnitch/stargazers) - Honeypot detection toolkit with protocol fingerprinting for 25+ honeypot types.

- ICS/SCADA honeypots

  - [Conpot](https://github.com/mushorg/conpot) [![GitHub stars](https://img.shields.io/github/stars/mushorg/conpot?style=flat)](https://github.com/mushorg/conpot/stargazers) - ICS/SCADA honeypot.
  - [GasPot](https://github.com/sjhilt/GasPot) [![GitHub stars](https://img.shields.io/github/stars/sjhilt/GasPot?style=flat)](https://github.com/sjhilt/GasPot/stargazers) - Veeder Root Gaurdian AST, common in the oil and gas industry.
  - [SCADA honeynet](http://scadahoneynet.sourceforge.net) - Building Honeypots for Industrial Networks.
  - [gridpot](https://github.com/sk4ld/gridpot) [![GitHub stars](https://img.shields.io/github/stars/sk4ld/gridpot?style=flat)](https://github.com/sk4ld/gridpot/stargazers) - Open source tools for realistic-behaving electric grid honeynets.
  - [scada-honeynet](http://www.digitalbond.com/blog/2007/07/24/scada-honeynet-article-in-infragard-publication/) - Mimics many of the services from a popular PLC and better helps SCADA researchers understand potential risks of exposed control system devices.
  - [HoneyPLC](https://github.com/sefcom/honeyplc) [![GitHub stars](https://img.shields.io/github/stars/sefcom/honeyplc?style=flat)](https://github.com/sefcom/honeyplc/stargazers) - Mimics multiple PLC devices, including Siemenens and Rockewell

- Space/Satellite honeypots

  - [HoneySat](https://github.com/HoneySat/honeysat-deploy) [![GitHub stars](https://img.shields.io/github/stars/HoneySat/honeysat-deploy?style=flat)](https://github.com/HoneySat/honeysat-deploy/stargazers) - Mimics multiple satellite missions
   

- Other/random

  - [CitrixHoneypot](https://github.com/MalwareTech/CitrixHoneypot) [![GitHub stars](https://img.shields.io/github/stars/MalwareTech/CitrixHoneypot?style=flat)](https://github.com/MalwareTech/CitrixHoneypot/stargazers) - Detect and log CVE-2019-19781 scan and exploitation attempts.
  - [Damn Simple Honeypot (DSHP)](https://github.com/naorlivne/dshp) [![GitHub stars](https://img.shields.io/github/stars/naorlivne/dshp?style=flat)](https://github.com/naorlivne/dshp/stargazers) - Honeypot framework with pluggable handlers.
  - [dicompot](https://github.com/nsmfoo/dicompot) [![GitHub stars](https://img.shields.io/github/stars/nsmfoo/dicompot?style=flat)](https://github.com/nsmfoo/dicompot/stargazers) - DICOM Honeypot.
  - [IPP Honey](https://gitlab.com/bontchev/ipphoney) - A honeypot for the Internet Printing Protocol.
  - [Log4Pot](https://github.com/thomaspatzke/Log4Pot) [![GitHub stars](https://img.shields.io/github/stars/thomaspatzke/Log4Pot?style=flat)](https://github.com/thomaspatzke/Log4Pot/stargazers) - A honeypot for the Log4Shell vulnerability (CVE-2021-44228).
  - [Masscanned](https://github.com/ivre/masscanned) [![GitHub stars](https://img.shields.io/github/stars/ivre/masscanned?style=flat)](https://github.com/ivre/masscanned/stargazers) - Let's be scanned. A low-interaction honeypot focused on network scanners and bots. It integrates very well with IVRE to build a self-hosted alternative to GreyNoise.
  - [medpot](https://github.com/schmalle/medpot) [![GitHub stars](https://img.shields.io/github/stars/schmalle/medpot?style=flat)](https://github.com/schmalle/medpot/stargazers) -  HL7 / FHIR honeypot.
  - [NOVA](https://github.com/DataSoft/Nova) [![GitHub stars](https://img.shields.io/github/stars/DataSoft/Nova?style=flat)](https://github.com/DataSoft/Nova/stargazers) - Uses honeypots as detectors, looks like a complete system.
  - [OpenFlow Honeypot (OFPot)](https://github.com/upa/ofpot) [![GitHub stars](https://img.shields.io/github/stars/upa/ofpot?style=flat)](https://github.com/upa/ofpot/stargazers) - Redirects traffic for unused IPs to a honeypot, built on POX.
  - [OpenCanary](https://github.com/thinkst/opencanary) [![GitHub stars](https://img.shields.io/github/stars/thinkst/opencanary?style=flat)](https://github.com/thinkst/opencanary/stargazers) - Modular and decentralised honeypot daemon that runs several canary versions of services that alerts when a service is (ab)used.
  - [ciscoasa_honeypot](https://github.com/cymmetria/ciscoasa_honeypot) [![GitHub stars](https://img.shields.io/github/stars/cymmetria/ciscoasa_honeypot?style=flat)](https://github.com/cymmetria/ciscoasa_honeypot/stargazers) A low interaction honeypot for the Cisco ASA component capable of detecting CVE-2018-0101, a DoS and remote code execution vulnerability.
  - [miniprint](https://github.com/sa7mon/miniprint) [![GitHub stars](https://img.shields.io/github/stars/sa7mon/miniprint?style=flat)](https://github.com/sa7mon/miniprint/stargazers) - A medium interaction printer honeypot.
  - [FortiGate SSL-VPN Honeypot](https://github.com/PeterGabaldon/Fortigate.VPN-SSL.Honeypot) [![GitHub stars](https://img.shields.io/github/stars/PeterGabaldon/Fortigate.VPN-SSL.Honeypot?style=flat)](https://github.com/PeterGabaldon/Fortigate.VPN-SSL.Honeypot/stargazers) - Mimics FortiGate SSL-VPN devices to capture brute-force attempts, symlink exploit probes, and malicious IP telemetry.

- Botnet C2 tools

  - [Hale](https://github.com/pjlantz/Hale) [![GitHub stars](https://img.shields.io/github/stars/pjlantz/Hale?style=flat)](https://github.com/pjlantz/Hale/stargazers) - Botnet command and control monitor.
  - [dnsMole](https://code.google.com/archive/p/dns-mole/) - Analyses DNS traffic and potentionaly detect botnet command and control server activity, along with infected hosts.

- IPv6 attack detection tool

  - [ipv6-attack-detector](https://github.com/mzweilin/ipv6-attack-detector/) [![GitHub stars](https://img.shields.io/github/stars/mzweilin/ipv6-attack-detector/?style=flat)](https://github.com/mzweilin/ipv6-attack-detector//stargazers) - Google Summer of Code 2012 project, supported by The Honeynet Project organization.

- Dynamic code instrumentation toolkit

  - [Frida](https://www.frida.re) - Inject JavaScript to explore native apps on Windows, Mac, Linux, iOS and Android.

- Tool to convert website to server honeypots

  - [HIHAT](http://hihat.sourceforge.net/) - Transform arbitrary PHP applications into web-based high-interaction Honeypots.

- Malware collector

  - [Kippo-Malware](https://bruteforcelab.com/kippo-malware) - Python script that will download all malicious files stored as URLs in a Kippo SSH honeypot database.

- Distributed sensor deployment

  - [Community Honey Network](https://communityhoneynetwork.readthedocs.io/en/stable/) - CHN aims to make deployments honeypots and honeypot management tools easy and flexible. The default deployment method uses Docker Compose and Docker to deploy with a few simple commands.
  - [Modern Honey Network](https://github.com/threatstream/mhn) [![GitHub stars](https://img.shields.io/github/stars/threatstream/mhn?style=flat)](https://github.com/threatstream/mhn/stargazers) - Multi-snort and honeypot sensor management, uses a network of VMs, small footprint SNORT installations, stealthy dionaeas, and a centralized server for management.

- Network Analysis Tool

  - [Tracexploit](https://code.google.com/archive/p/tracexploit/) - Replay network packets.

- Log anonymizer

  - [LogAnon](http://code.google.com/archive/p/loganon/) - Log anonymization library that helps having anonymous logs consistent between logs and network captures.

- Dynamic Deception Tool

  - [Mimicry](https://github.com/chaitin/mimicry) [![GitHub stars](https://img.shields.io/github/stars/chaitin/mimicry?style=flat)](https://github.com/chaitin/mimicry/stargazers) - Mimicry is a dynamic deception tool that actively deceives an attacker during exploitation and post-exploitation.

- Low interaction honeypot (router back door)

  - [Honeypot-32764](https://github.com/knalli/honeypot-for-tcp-32764) [![GitHub stars](https://img.shields.io/github/stars/knalli/honeypot-for-tcp-32764?style=flat)](https://github.com/knalli/honeypot-for-tcp-32764/stargazers) - Honeypot for router backdoor (TCP 32764).
  - [WAPot](https://github.com/lcashdol/WAPot) [![GitHub stars](https://img.shields.io/github/stars/lcashdol/WAPot?style=flat)](https://github.com/lcashdol/WAPot/stargazers) - Honeypot that can be used to observe traffic directed at home routers.

- honeynet farm traffic redirector

  - [Honeymole](https://web.archive.org/web/20100326040550/http://www.honeynet.org.pt:80/index.php/HoneyMole) - Deploy multiple sensors that redirect traffic to a centralized collection of honeypots.

- HTTPS Proxy

  - [mitmproxy](https://mitmproxy.org/) - Allows traffic flows to be intercepted, inspected, modified, and replayed.

- System instrumentation

  - [Sysdig](https://sysdig.com/opensource/) - Open source, system-level exploration allows one to capture system state and activity from a running GNU/Linux instance, then save, filter, and analyze the results.
  - [Fibratus](https://github.com/rabbitstack/fibratus) [![GitHub stars](https://img.shields.io/github/stars/rabbitstack/fibratus?style=flat)](https://github.com/rabbitstack/fibratus/stargazers) - Tool for exploration and tracing of the Windows kernel.

- Honeypot for USB-spreading malware

  - [Ghost-usb](https://github.com/honeynet/ghost-usb-honeypot) [![GitHub stars](https://img.shields.io/github/stars/honeynet/ghost-usb-honeypot?style=flat)](https://github.com/honeynet/ghost-usb-honeypot/stargazers) - Honeypot for malware that propagates via USB storage devices.

- Data Collection

  - [Kippo2MySQL](https://bruteforcelab.com/kippo2mysql) - Extracts some very basic stats from Kippo’s text-based log files and inserts them in a MySQL database.
  - [Kippo2ElasticSearch](https://bruteforcelab.com/kippo2elasticsearch) - Python script to transfer data from a Kippo SSH honeypot MySQL database to an ElasticSearch instance (server or cluster).

- Passive network audit framework parser

  - [Passive Network Audit Framework (pnaf)](https://github.com/jusafing/pnaf) [![GitHub stars](https://img.shields.io/github/stars/jusafing/pnaf?style=flat)](https://github.com/jusafing/pnaf/stargazers) - Framework that combines multiple passive and automated analysis techniques in order to provide a security assessment of network platforms.

- VM monitoring and tools

  - [Antivmdetect](https://github.com/nsmfoo/antivmdetection) [![GitHub stars](https://img.shields.io/github/stars/nsmfoo/antivmdetection?style=flat)](https://github.com/nsmfoo/antivmdetection/stargazers) - Script to create templates to use with VirtualBox to make VM detection harder.
  - [VMCloak](https://github.com/hatching/vmcloak) [![GitHub stars](https://img.shields.io/github/stars/hatching/vmcloak?style=flat)](https://github.com/hatching/vmcloak/stargazers) - Automated Virtual Machine Generation and Cloaking for Cuckoo Sandbox.
  - [vmitools](http://libvmi.com/) - C library with Python bindings that makes it easy to monitor the low-level details of a running virtual machine.

- Binary debugger

  - [Hexgolems - Pint Debugger Backend](https://github.com/hexgolems/pint) [![GitHub stars](https://img.shields.io/github/stars/hexgolems/pint?style=flat)](https://github.com/hexgolems/pint/stargazers) - Debugger backend and LUA wrapper for PIN.
  - [Hexgolems - Schem Debugger Frontend](https://github.com/hexgolems/schem) [![GitHub stars](https://img.shields.io/github/stars/hexgolems/schem?style=flat)](https://github.com/hexgolems/schem/stargazers) - Debugger frontend.

- Mobile Analysis Tool

  - [Androguard](https://github.com/androguard/androguard) [![GitHub stars](https://img.shields.io/github/stars/androguard/androguard?style=flat)](https://github.com/androguard/androguard/stargazers) - Reverse engineering, Malware and goodware analysis of Android applications and more.
  - [APKinspector](https://github.com/honeynet/apkinspector/) [![GitHub stars](https://img.shields.io/github/stars/honeynet/apkinspector/?style=flat)](https://github.com/honeynet/apkinspector//stargazers) - Powerful GUI tool for analysts to analyze the Android applications.

- Low interaction honeypot

  - [Honeyperl](https://sourceforge.net/projects/honeyperl/) - Honeypot software based in Perl with plugins developed for many functions like : wingates, telnet, squid, smtp, etc.
  - [T-Pot](https://github.com/dtag-dev-sec/tpotce) [![GitHub stars](https://img.shields.io/github/stars/dtag-dev-sec/tpotce?style=flat)](https://github.com/dtag-dev-sec/tpotce/stargazers) - All in one honeypot appliance from telecom provider T-Mobile
  - [beelzebub](https://github.com/mariocandela/beelzebub) [![GitHub stars](https://img.shields.io/github/stars/mariocandela/beelzebub?style=flat)](https://github.com/mariocandela/beelzebub/stargazers) - A secure honeypot framework, extremely easy to configure by yaml 🚀

- Honeynet data fusion

  - [HFlow2](https://projects.honeynet.org/hflow) - Data coalesing tool for honeynet/network analysis.

- Server

  - [Amun](http://amunhoney.sourceforge.net) - Vulnerability emulation honeypot.
  - [Artillery](https://github.com/BinaryDefense/artillery) [![GitHub stars](https://img.shields.io/github/stars/BinaryDefense/artillery?style=flat)](https://github.com/BinaryDefense/artillery/stargazers) - Open-source blue team tool designed to protect Linux and Windows operating systems through multiple methods.
  - [Bait and Switch](http://baitnswitch.sourceforge.net) - Redirects all hostile traffic to a honeypot that is partially mirroring your production system.
  - [Bifrozt](https://github.com/Ziemeck/bifrozt-ansible) [![GitHub stars](https://img.shields.io/github/stars/Ziemeck/bifrozt-ansible?style=flat)](https://github.com/Ziemeck/bifrozt-ansible/stargazers) - Automatic deploy bifrozt with ansible.
  - [Conpot](http://conpot.org/) - Low interactive server side Industrial Control Systems honeypot.
  - [Heralding](https://github.com/johnnykv/heralding) [![GitHub stars](https://img.shields.io/github/stars/johnnykv/heralding?style=flat)](https://github.com/johnnykv/heralding/stargazers) - Credentials catching honeypot.
  - [HoneyWRT](https://github.com/CanadianJeff/honeywrt) [![GitHub stars](https://img.shields.io/github/stars/CanadianJeff/honeywrt?style=flat)](https://github.com/CanadianJeff/honeywrt/stargazers) - Low interaction Python honeypot designed to mimic services or ports that might get targeted by attackers.
  - [Honeyd](https://github.com/provos/honeyd) [![GitHub stars](https://img.shields.io/github/stars/provos/honeyd?style=flat)](https://github.com/provos/honeyd/stargazers) - See [honeyd tools](#honeyd-tools).
  - [Honeysink](http://www.honeynet.org/node/773) - Open source network sinkhole that provides a mechanism for detection and prevention of malicious traffic on a given network.
  - [Hontel](https://github.com/stamparm/hontel) [![GitHub stars](https://img.shields.io/github/stars/stamparm/hontel?style=flat)](https://github.com/stamparm/hontel/stargazers) - Telnet Honeypot.
  - [KFSensor](http://www.keyfocus.net/kfsensor/) - Windows based honeypot Intrusion Detection System (IDS).
  - [LaBrea](http://labrea.sourceforge.net/labrea-info.html) - Takes over unused IP addresses, and creates virtual servers that are attractive to worms, hackers, and other denizens of the Internet.
  - [MTPot](https://github.com/Cymmetria/MTPot) [![GitHub stars](https://img.shields.io/github/stars/Cymmetria/MTPot?style=flat)](https://github.com/Cymmetria/MTPot/stargazers) - Open Source Telnet Honeypot, focused on Mirai malware.
  - [SIREN](https://github.com/blaverick62/SIREN) [![GitHub stars](https://img.shields.io/github/stars/blaverick62/SIREN?style=flat)](https://github.com/blaverick62/SIREN/stargazers) - Semi-Intelligent HoneyPot Network - HoneyNet Intelligent Virtual Environment.
  - [TelnetHoney](https://github.com/balte/TelnetHoney) [![GitHub stars](https://img.shields.io/github/stars/balte/TelnetHoney?style=flat)](https://github.com/balte/TelnetHoney/stargazers) - Simple telnet honeypot.
  - [UDPot Honeypot](https://github.com/jekil/UDPot) [![GitHub stars](https://img.shields.io/github/stars/jekil/UDPot?style=flat)](https://github.com/jekil/UDPot/stargazers) - Simple UDP/DNS honeypot scripts.
  - [Yet Another Fake Honeypot (YAFH)](https://github.com/fnzv/YAFH) [![GitHub stars](https://img.shields.io/github/stars/fnzv/YAFH?style=flat)](https://github.com/fnzv/YAFH/stargazers) - Simple honeypot written in Go.
  - [arctic-swallow](https://github.com/ajackal/arctic-swallow) [![GitHub stars](https://img.shields.io/github/stars/ajackal/arctic-swallow?style=flat)](https://github.com/ajackal/arctic-swallow/stargazers) - Low interaction honeypot.
  - [fapro](https://github.com/fofapro/fapro) [![GitHub stars](https://img.shields.io/github/stars/fofapro/fapro?style=flat)](https://github.com/fofapro/fapro/stargazers) - Fake Protocol Server.
  - [glutton](https://github.com/mushorg/glutton) [![GitHub stars](https://img.shields.io/github/stars/mushorg/glutton?style=flat)](https://github.com/mushorg/glutton/stargazers) - All eating honeypot.
  - [go-HoneyPot](https://github.com/Mojachieee/go-HoneyPot) [![GitHub stars](https://img.shields.io/github/stars/Mojachieee/go-HoneyPot?style=flat)](https://github.com/Mojachieee/go-HoneyPot/stargazers) - Honeypot server written in Go.
  - [go-emulators](https://github.com/kingtuna/go-emulators) [![GitHub stars](https://img.shields.io/github/stars/kingtuna/go-emulators?style=flat)](https://github.com/kingtuna/go-emulators/stargazers) - Honeypot Golang emulators.
  - [honeymail](https://github.com/sec51/honeymail) [![GitHub stars](https://img.shields.io/github/stars/sec51/honeymail?style=flat)](https://github.com/sec51/honeymail/stargazers) - SMTP honeypot written in Golang.
  - [honeytrap](https://github.com/tillmannw/honeytrap) [![GitHub stars](https://img.shields.io/github/stars/tillmannw/honeytrap?style=flat)](https://github.com/tillmannw/honeytrap/stargazers) - Low-interaction honeypot and network security tool written to catch attacks against TCP and UDP services.
  - [imap-honey](https://github.com/yvesago/imap-honey) [![GitHub stars](https://img.shields.io/github/stars/yvesago/imap-honey?style=flat)](https://github.com/yvesago/imap-honey/stargazers) - IMAP honeypot written in Golang.
  - [mwcollectd](https://www.openhub.net/p/mwcollectd) - Versatile malware collection daemon, uniting the best features of nepenthes and honeytrap.
  - [potd](https://github.com/lnslbrty/potd) [![GitHub stars](https://img.shields.io/github/stars/lnslbrty/potd?style=flat)](https://github.com/lnslbrty/potd/stargazers) - Highly scalable low- to medium-interaction SSH/TCP honeypot designed for OpenWrt/IoT devices leveraging several Linux kernel features, such as namespaces, seccomp and thread capabilities.
  - [portlurker](https://github.com/bartnv/portlurker) [![GitHub stars](https://img.shields.io/github/stars/bartnv/portlurker?style=flat)](https://github.com/bartnv/portlurker/stargazers) - Port listener in Rust with protocol guessing and safe string display.
  - [slipm-honeypot](https://github.com/rshipp/slipm-honeypot) [![GitHub stars](https://img.shields.io/github/stars/rshipp/slipm-honeypot?style=flat)](https://github.com/rshipp/slipm-honeypot/stargazers) - Simple low-interaction port monitoring honeypot.
  - [telnet-iot-honeypot](https://github.com/Phype/telnet-iot-honeypot) [![GitHub stars](https://img.shields.io/github/stars/Phype/telnet-iot-honeypot?style=flat)](https://github.com/Phype/telnet-iot-honeypot/stargazers) - Python telnet honeypot for catching botnet binaries.
  - [telnetlogger](https://github.com/robertdavidgraham/telnetlogger) [![GitHub stars](https://img.shields.io/github/stars/robertdavidgraham/telnetlogger?style=flat)](https://github.com/robertdavidgraham/telnetlogger/stargazers) - Telnet honeypot designed to track the Mirai botnet.
  - [vnclowpot](https://github.com/magisterquis/vnclowpot) [![GitHub stars](https://img.shields.io/github/stars/magisterquis/vnclowpot?style=flat)](https://github.com/magisterquis/vnclowpot/stargazers) - Low interaction VNC honeypot.

- IDS signature generation

  - [Honeycomb](http://www.icir.org/christian/honeycomb/) - Automated signature creation using honeypots.

- Lookup service for AS-numbers and prefixes

  - [CC2ASN](http://www.cc2asn.com/) - Simple lookup service for AS-numbers and prefixes belonging to any given country in the world.

- Data Collection / Data Sharing

  - [HPfriends](http://hpfriends.honeycloud.net/#/home) - Honeypot data-sharing platform.
    - [hpfriends - real-time social data-sharing](https://heipei.io/sigint-hpfriends/) - Presentation about HPFriends feed system
  - [HPFeeds](https://github.com/rep/hpfeeds/) [![GitHub stars](https://img.shields.io/github/stars/rep/hpfeeds/?style=flat)](https://github.com/rep/hpfeeds//stargazers) - Lightweight authenticated publish-subscribe protocol.

- Central management tool

  - [PHARM](http://www.nepenthespharm.com/) - Manage, report, and analyze your distributed Nepenthes instances.

- Network connection analyzer

  - [Impost](http://impost.sourceforge.net/) - Network security auditing tool designed to analyze the forensics behind compromised and/or vulnerable daemons.

- Honeypot deployment

  - [honeyfs](https://github.com/referefref/honeyfs) [![GitHub stars](https://img.shields.io/github/stars/referefref/honeyfs?style=flat)](https://github.com/referefref/honeyfs/stargazers) - Tool to create artificial file systems for medium/high interaction honeypots.
  - [Modern Honeynet Network](http://threatstream.github.io/mhn/) - Streamlines deployment and management of secure honeypots.

- Honeypot extensions to Wireshark

  - [Wireshark Extensions](https://www.honeynet.org/project/WiresharkExtensions) - Apply Snort IDS rules and signatures against packet capture files using Wireshark.

- Client

  - [CWSandbox / GFI Sandbox](https://www.gfi.com/products-and-solutions/all-products)
  - [Capture-HPC-Linux](https://redmine.honeynet.org/projects/linux-capture-hpc/wiki)
  - [Capture-HPC-NG](https://github.com/CERT-Polska/HSN-Capture-HPC-NG) [![GitHub stars](https://img.shields.io/github/stars/CERT-Polska/HSN-Capture-HPC-NG?style=flat)](https://github.com/CERT-Polska/HSN-Capture-HPC-NG/stargazers)
  - [Capture-HPC](https://projects.honeynet.org/capture-hpc) - High interaction client honeypot (also called honeyclient).
  - [HoneyBOT](http://www.atomicsoftwaresolutions.com/)
  - [HoneyC](https://projects.honeynet.org/honeyc)
  - [HoneySpider Network](https://github.com/CERT-Polska/hsn2-bundle) [![GitHub stars](https://img.shields.io/github/stars/CERT-Polska/hsn2-bundle?style=flat)](https://github.com/CERT-Polska/hsn2-bundle/stargazers) - Highly-scalable system integrating multiple client honeypots to detect malicious websites.
  - [HoneyWeb](https://code.google.com/archive/p/gsoc-honeyweb/) - Web interface created to manage and remotely share Honeyclients resources.
  - [Jsunpack-n](https://github.com/urule99/jsunpack-n) [![GitHub stars](https://img.shields.io/github/stars/urule99/jsunpack-n?style=flat)](https://github.com/urule99/jsunpack-n/stargazers)
  - [MonkeySpider](http://monkeyspider.sourceforge.net)
  - [PhoneyC](https://github.com/honeynet/phoneyc) [![GitHub stars](https://img.shields.io/github/stars/honeynet/phoneyc?style=flat)](https://github.com/honeynet/phoneyc/stargazers) - Python honeyclient (later replaced by Thug).
  - [Pwnypot](https://github.com/shjalayeri/pwnypot) [![GitHub stars](https://img.shields.io/github/stars/shjalayeri/pwnypot?style=flat)](https://github.com/shjalayeri/pwnypot/stargazers) - High Interaction Client Honeypot.
  - [Rumal](https://github.com/thugs-rumal/) [![GitHub stars](https://img.shields.io/github/stars/thugs-rumal/?style=flat)](https://github.com/thugs-rumal//stargazers) - Thug's Rumāl: a Thug's dress and weapon.
  - [Shelia](https://www.cs.vu.nl/~herbertb/misc/shelia/) - Client-side honeypot for attack detection.
  - [Thug](https://buffer.github.io/thug/) - Python-based low-interaction honeyclient.
  - [Thug Distributed Task Queuing](https://thug-distributed.readthedocs.io/en/latest/index.html)
  - [Trigona](https://www.honeynet.org/project/Trigona)
  - [URLQuery](https://urlquery.net/)
  - [YALIH (Yet Another Low Interaction Honeyclient)](https://github.com/Masood-M/yalih) [![GitHub stars](https://img.shields.io/github/stars/Masood-M/yalih?style=flat)](https://github.com/Masood-M/yalih/stargazers) - Low-interaction client honeypot designed to detect malicious websites through signature, anomaly, and pattern matching techniques.

- Honeypot

  - [Deception Toolkit](http://www.all.net/dtk/dtk.html)
  - [IMHoneypot](https://github.com/mushorg/imhoneypot) [![GitHub stars](https://img.shields.io/github/stars/mushorg/imhoneypot?style=flat)](https://github.com/mushorg/imhoneypot/stargazers)

- PDF document inspector

  - [peepdf](https://github.com/jesparza/peepdf) [![GitHub stars](https://img.shields.io/github/stars/jesparza/peepdf?style=flat)](https://github.com/jesparza/peepdf/stargazers) - Powerful Python tool to analyze PDF documents.

- Hybrid low/high interaction honeypot

  - [HoneyBrid](http://honeybrid.sourceforge.net)

- SSH Honeypots

  - [Blacknet](https://github.com/morian/blacknet) [![GitHub stars](https://img.shields.io/github/stars/morian/blacknet?style=flat)](https://github.com/morian/blacknet/stargazers) - Multi-head SSH honeypot system.
  - [Cowrie](https://github.com/cowrie/cowrie) [![GitHub stars](https://img.shields.io/github/stars/cowrie/cowrie?style=flat)](https://github.com/cowrie/cowrie/stargazers) - Cowrie SSH Honeypot (based on kippo).
  - [DShield docker](https://github.com/xme/dshield-docker) [![GitHub stars](https://img.shields.io/github/stars/xme/dshield-docker?style=flat)](https://github.com/xme/dshield-docker/stargazers) - Docker container running cowrie with DShield output enabled.
  - [endlessh](https://github.com/skeeto/endlessh) [![GitHub stars](https://img.shields.io/github/stars/skeeto/endlessh?style=flat)](https://github.com/skeeto/endlessh/stargazers) - SSH tarpit that slowly sends an endless banner. ([docker image](https://hub.docker.com/r/linuxserver/endlessh))
  - [HonSSH](https://github.com/tnich/honssh) [![GitHub stars](https://img.shields.io/github/stars/tnich/honssh?style=flat)](https://github.com/tnich/honssh/stargazers) - Logs all SSH communications between a client and server.
  - [HUDINX](https://github.com/Cryptix720/HUDINX) [![GitHub stars](https://img.shields.io/github/stars/Cryptix720/HUDINX?style=flat)](https://github.com/Cryptix720/HUDINX/stargazers) - Tiny interaction SSH honeypot engineered in Python to log brute force attacks and, most importantly, the entire shell interaction performed by the attacker.
  - [InnerWarden](https://github.com/InnerWarden/innerwarden) [![GitHub stars](https://img.shields.io/github/stars/InnerWarden/innerwarden?style=flat)](https://github.com/InnerWarden/innerwarden/stargazers) - Security agent with built-in SSH and HTTP honeypots featuring an LLM-powered interactive fake shell that captures credentials and attacker commands.
  - [Kippo](https://github.com/desaster/kippo) [![GitHub stars](https://img.shields.io/github/stars/desaster/kippo?style=flat)](https://github.com/desaster/kippo/stargazers) - Medium interaction SSH honeypot.
  - [Kippo_JunOS](https://github.com/gregcmartin/Kippo_JunOS) [![GitHub stars](https://img.shields.io/github/stars/gregcmartin/Kippo_JunOS?style=flat)](https://github.com/gregcmartin/Kippo_JunOS/stargazers) - Kippo configured to be a backdoored netscreen.
  - [Kojoney2](https://github.com/madirish/kojoney2) [![GitHub stars](https://img.shields.io/github/stars/madirish/kojoney2?style=flat)](https://github.com/madirish/kojoney2/stargazers) - Low interaction SSH honeypot written in Python and based on Kojoney by Jose Antonio Coret.
  - [Kojoney](http://kojoney.sourceforge.net/) - Python-based Low interaction honeypot that emulates an SSH server implemented with Twisted Conch.
  - [Longitudinal Analysis of SSH Cowrie Honeypot Logs](https://github.com/deroux/longitudinal-analysis-cowrie) [![GitHub stars](https://img.shields.io/github/stars/deroux/longitudinal-analysis-cowrie?style=flat)](https://github.com/deroux/longitudinal-analysis-cowrie/stargazers) - Python based command line tool to analyze cowrie logs over time.
  - [LongTail Log Analysis @ Marist College](http://longtail.it.marist.edu/honey/) - Analyzed SSH honeypot logs.
  - [Malbait](https://github.com/batchmcnulty/Malbait) [![GitHub stars](https://img.shields.io/github/stars/batchmcnulty/Malbait?style=flat)](https://github.com/batchmcnulty/Malbait/stargazers) - Simple TCP/UDP honeypot implemented in Perl.
  - [MockSSH](https://github.com/ncouture/MockSSH) [![GitHub stars](https://img.shields.io/github/stars/ncouture/MockSSH?style=flat)](https://github.com/ncouture/MockSSH/stargazers) - Mock an SSH server and define all commands it supports (Python, Twisted).
  - [cowrie2neo](https://github.com/xlfe/cowrie2neo) [![GitHub stars](https://img.shields.io/github/stars/xlfe/cowrie2neo?style=flat)](https://github.com/xlfe/cowrie2neo/stargazers) - Parse cowrie honeypot logs into a neo4j database.
  - [go-sshoney](https://github.com/ashmckenzie/go-sshoney) [![GitHub stars](https://img.shields.io/github/stars/ashmckenzie/go-sshoney?style=flat)](https://github.com/ashmckenzie/go-sshoney/stargazers) - SSH Honeypot.
  - [go0r](https://github.com/fzerorubigd/go0r) [![GitHub stars](https://img.shields.io/github/stars/fzerorubigd/go0r?style=flat)](https://github.com/fzerorubigd/go0r/stargazers) - Simple ssh honeypot in Golang.
  - [gohoney](https://github.com/PaulMaddox/gohoney) [![GitHub stars](https://img.shields.io/github/stars/PaulMaddox/gohoney?style=flat)](https://github.com/PaulMaddox/gohoney/stargazers) - SSH honeypot written in Go.
  - [hived](https://github.com/sahilm/hived) [![GitHub stars](https://img.shields.io/github/stars/sahilm/hived?style=flat)](https://github.com/sahilm/hived/stargazers) - Golang-based honeypot.
  - [hnypots-agent)](https://github.com/joshrendek/hnypots-agent) [![GitHub stars](https://img.shields.io/github/stars/joshrendek/hnypots-agent?style=flat)](https://github.com/joshrendek/hnypots-agent/stargazers) - SSH Server in Go that logs username and password combinations.
  - [honeypot.go](https://github.com/mdp/honeypot.go) [![GitHub stars](https://img.shields.io/github/stars/mdp/honeypot.go?style=flat)](https://github.com/mdp/honeypot.go/stargazers) - SSH Honeypot written in Go.
  - [honeyssh](https://github.com/ppacher/honeyssh) [![GitHub stars](https://img.shields.io/github/stars/ppacher/honeyssh?style=flat)](https://github.com/ppacher/honeyssh/stargazers) - Credential dumping SSH honeypot with statistics.
  - [hornet](https://github.com/czardoz/hornet) [![GitHub stars](https://img.shields.io/github/stars/czardoz/hornet?style=flat)](https://github.com/czardoz/hornet/stargazers) - Medium interaction SSH honeypot that supports multiple virtual hosts.
  - [ssh-auth-logger](https://github.com/JustinAzoff/ssh-auth-logger) [![GitHub stars](https://img.shields.io/github/stars/JustinAzoff/ssh-auth-logger?style=flat)](https://github.com/JustinAzoff/ssh-auth-logger/stargazers) - Low/zero interaction SSH authentication logging honeypot.
  - [ssh-honeypot](https://github.com/droberson/ssh-honeypot) [![GitHub stars](https://img.shields.io/github/stars/droberson/ssh-honeypot?style=flat)](https://github.com/droberson/ssh-honeypot/stargazers) - Fake sshd that logs IP addresses, usernames, and passwords.
  - [ssh-honeypot](https://github.com/amv42/sshd-honeypot) [![GitHub stars](https://img.shields.io/github/stars/amv42/sshd-honeypot?style=flat)](https://github.com/amv42/sshd-honeypot/stargazers) - Modified version of the OpenSSH deamon that forwards commands to Cowrie where all commands are interpreted and returned.
  - [ssh-honeypotd](https://github.com/sjinks/ssh-honeypotd) [![GitHub stars](https://img.shields.io/github/stars/sjinks/ssh-honeypotd?style=flat)](https://github.com/sjinks/ssh-honeypotd/stargazers) - Low-interaction SSH honeypot written in C.
  - [sshForShits](https://github.com/traetox/sshForShits) [![GitHub stars](https://img.shields.io/github/stars/traetox/sshForShits?style=flat)](https://github.com/traetox/sshForShits/stargazers) - Framework for a high interaction SSH honeypot.
  - [sshesame](https://github.com/jaksi/sshesame) [![GitHub stars](https://img.shields.io/github/stars/jaksi/sshesame?style=flat)](https://github.com/jaksi/sshesame/stargazers) - Fake SSH server that lets everyone in and logs their activity.
  - [sshhipot](https://github.com/magisterquis/sshhipot) [![GitHub stars](https://img.shields.io/github/stars/magisterquis/sshhipot?style=flat)](https://github.com/magisterquis/sshhipot/stargazers) - High-interaction MitM SSH honeypot.
  - [sshlowpot](https://github.com/magisterquis/sshlowpot) [![GitHub stars](https://img.shields.io/github/stars/magisterquis/sshlowpot?style=flat)](https://github.com/magisterquis/sshlowpot/stargazers) - Yet another no-frills low-interaction SSH honeypot in Go.
  - [sshsyrup](https://github.com/mkishere/sshsyrup) [![GitHub stars](https://img.shields.io/github/stars/mkishere/sshsyrup?style=flat)](https://github.com/mkishere/sshsyrup/stargazers) - Simple SSH Honeypot with features to capture terminal activity and upload to asciinema.org.
  - [twisted-honeypots](https://github.com/lanjelot/twisted-honeypots) [![GitHub stars](https://img.shields.io/github/stars/lanjelot/twisted-honeypots?style=flat)](https://github.com/lanjelot/twisted-honeypots/stargazers) - SSH, FTP and Telnet honeypots based on Twisted.

- Distributed sensor project

  - [DShield Web Honeypot Project](https://sites.google.com/site/webhoneypotsite/)

- A pcap analyzer

  - [Honeysnap](https://projects.honeynet.org/honeysnap/)

- Network traffic redirector

  - [Honeywall](https://projects.honeynet.org/honeywall/)

- Honeypot Distribution with mixed content

  - [HoneyDrive](https://www.honeynet.org/tags/honeydrive/)

- Honeypot sensor

  - [Honeeepi](https://redmine.honeynet.org/projects/honeeepi/wiki) - Honeypot sensor on a Raspberry Pi based on a customized Raspbian OS.

- File carving

  - [TestDisk & PhotoRec](https://www.cgsecurity.org/)

- Behavioral analysis tool for win32

  - [Capture BAT](https://www.honeynet.org/node/315)

- Live CD

  - [DAVIX](https://www.secviz.org/node/89) - The DAVIX Live CD.

- Spamtrap

  - [Mail::SMTP::Honeypot](https://metacpan.org/pod/release/MIKER/Mail-SMTP-Honeypot-0.11/Honeypot.pm) - Perl module that appears to provide the functionality of a standard SMTP server.
  - [Mailoney](https://github.com/phin3has/mailoney) [![GitHub stars](https://img.shields.io/github/stars/phin3has/mailoney?style=flat)](https://github.com/phin3has/mailoney/stargazers) - SMTP honeypot written in python.
  - [SendMeSpamIDS.py](https://github.com/johestephan/VerySimpleHoneypot) [![GitHub stars](https://img.shields.io/github/stars/johestephan/VerySimpleHoneypot?style=flat)](https://github.com/johestephan/VerySimpleHoneypot/stargazers) - Simple SMTP fetch all IDS and analyzer.
  - [Shiva](https://github.com/shiva-spampot/shiva) [![GitHub stars](https://img.shields.io/github/stars/shiva-spampot/shiva?style=flat)](https://github.com/shiva-spampot/shiva/stargazers) - Spam Honeypot with Intelligent Virtual Analyzer.
    - [Shiva The Spam Honeypot Tips And Tricks For Getting It Up And Running](https://www.pentestpartners.com/security-blog/shiva-the-spam-honeypot-tips-and-tricks-for-getting-it-up-and-running/)
  - [SMTPLLMPot](https://github.com/referefref/SMTPLLMPot) [![GitHub stars](https://img.shields.io/github/stars/referefref/SMTPLLMPot?style=flat)](https://github.com/referefref/SMTPLLMPot/stargazers) - A super simple SMTP Honeypot built using GPT3.5
  - [SpamHAT](https://github.com/miguelraulb/spamhat) [![GitHub stars](https://img.shields.io/github/stars/miguelraulb/spamhat?style=flat)](https://github.com/miguelraulb/spamhat/stargazers) - Spam Honeypot Tool.
  - [Spamhole](http://www.spamhole.net/)
  - [honeypot](https://github.com/jadb/honeypot) [![GitHub stars](https://img.shields.io/github/stars/jadb/honeypot?style=flat)](https://github.com/jadb/honeypot/stargazers) - The Project Honey Pot un-official PHP SDK.
  - [spamd](http://man.openbsd.org/cgi-bin/man.cgi?query=spamd%26apropos=0%26sektion=0%26manpath=OpenBSD+Current%26arch=i386%26format=html)

- Commercial honeynet

  - [Cymmetria Mazerunner](ttps://cymmetria.com/products/mazerunner/) - Leads attackers away from real targets and creates a footprint of the attack.

- Server (Bluetooth)

  - [Bluepot](https://github.com/andrewmichaelsmith/bluepot) [![GitHub stars](https://img.shields.io/github/stars/andrewmichaelsmith/bluepot?style=flat)](https://github.com/andrewmichaelsmith/bluepot/stargazers)

- Dynamic analysis of Android apps

  - [Droidbox](https://code.google.com/archive/p/droidbox/)

- Dockerized Low Interaction packaging

  - [Docker honeynet](https://github.com/sreinhardt/Docker-Honeynet) [![GitHub stars](https://img.shields.io/github/stars/sreinhardt/Docker-Honeynet?style=flat)](https://github.com/sreinhardt/Docker-Honeynet/stargazers) - Several Honeynet tools set up for Docker containers.
  - [Dockerized Thug](https://hub.docker.com/r/honeynet/thug/) - Dockerized [Thug](https://github.com/buffer/thug) [![GitHub stars](https://img.shields.io/github/stars/buffer/thug?style=flat)](https://github.com/buffer/thug/stargazers) to analyze malicious web content.
  - [Dockerpot](https://github.com/mrschyte/dockerpot) [![GitHub stars](https://img.shields.io/github/stars/mrschyte/dockerpot?style=flat)](https://github.com/mrschyte/dockerpot/stargazers) - Docker based honeypot.
  - [Manuka](https://github.com/andrewmichaelsmith/manuka) [![GitHub stars](https://img.shields.io/github/stars/andrewmichaelsmith/manuka?style=flat)](https://github.com/andrewmichaelsmith/manuka/stargazers) - Docker based honeypot (Dionaea and Kippo).
  - [honey_ports](https://github.com/run41/honey_ports) [![GitHub stars](https://img.shields.io/github/stars/run41/honey_ports?style=flat)](https://github.com/run41/honey_ports/stargazers) - Very simple but effective docker deployed honeypot to detect port scanning in your environment.
  - [mhn-core-docker](https://github.com/MattCarothers/mhn-core-docker) [![GitHub stars](https://img.shields.io/github/stars/MattCarothers/mhn-core-docker?style=flat)](https://github.com/MattCarothers/mhn-core-docker/stargazers) - Core elements of the Modern Honey Network implemented in Docker.

- Network analysis

  - [Quechua](https://bitbucket.org/zaccone/quechua)

- SIP Server

  - [Artemnesia VoIP](http://artemisa.sourceforge.net)

- SIP

  - [SentryPeer](https://github.com/SentryPeer/SentryPeer) [![GitHub stars](https://img.shields.io/github/stars/SentryPeer/SentryPeer?style=flat)](https://github.com/SentryPeer/SentryPeer/stargazers) - Protect your SIP Servers from bad actors.

- IOT Honeypot

  - [HoneyThing](https://github.com/omererdem/honeything) [![GitHub stars](https://img.shields.io/github/stars/omererdem/honeything?style=flat)](https://github.com/omererdem/honeything/stargazers) - TR-069 Honeypot.
  - [Kako](https://github.com/darkarnium/kako) [![GitHub stars](https://img.shields.io/github/stars/darkarnium/kako?style=flat)](https://github.com/darkarnium/kako/stargazers) - Honeypots for a number of well known and deployed embedded device vulnerabilities.

- Honeytokens
  - [CanaryTokens](https://github.com/thinkst/canarytokens) [![GitHub stars](https://img.shields.io/github/stars/thinkst/canarytokens?style=flat)](https://github.com/thinkst/canarytokens/stargazers) - Self-hostable honeytoken generator and reporting dashboard; demo version available at [CanaryTokens.org](https://canarytokens.org/generate).
  - [Honeybits](https://github.com/0x4D31/honeybits) [![GitHub stars](https://img.shields.io/github/stars/0x4D31/honeybits?style=flat)](https://github.com/0x4D31/honeybits/stargazers) - Simple tool designed to enhance the effectiveness of your traps by spreading breadcrumbs and honeytokens across your production servers and workstations to lure the attacker toward your honeypots.
  - [Honeyλ (HoneyLambda)](https://github.com/0x4D31/honeylambda) [![GitHub stars](https://img.shields.io/github/stars/0x4D31/honeylambda?style=flat)](https://github.com/0x4D31/honeylambda/stargazers) - Simple, serverless application designed to create and monitor URL honeytokens, on top of AWS Lambda and Amazon API Gateway.
  - [dcept](https://github.com/secureworks/dcept) [![GitHub stars](https://img.shields.io/github/stars/secureworks/dcept?style=flat)](https://github.com/secureworks/dcept/stargazers) - Tool for deploying and detecting use of Active Directory honeytokens.
  - [honeyku](https://github.com/0x4D31/honeyku) [![GitHub stars](https://img.shields.io/github/stars/0x4D31/honeyku?style=flat)](https://github.com/0x4D31/honeyku/stargazers) - Heroku-based web honeypot that can be used to create and monitor fake HTTP endpoints (i.e. honeytokens).
  - [Tracebit Community Edition](https://community.tracebit.com) - online free canary tokens (AWS, SSH, Email, Web)
    
## Honeyd Tools

- Honeyd plugin

  - [Honeycomb](http://www.honeyd.org/tools.php)

- Honeyd viewer

  - [Honeyview](http://honeyview.sourceforge.net/)

- Honeyd to MySQL connector

  - [Honeyd2MySQL](https://bruteforcelab.com/honeyd2mysql)

- A script to visualize statistics from honeyd

  - [Honeyd-Viz](https://bruteforcelab.com/honeyd-viz)

- Honeyd stats
  - [Honeydsum.pl](https://github.com/DataSoft/Honeyd/blob/master/scripts/misc/honeydsum-v0.3/honeydsum.pl) [![GitHub stars](https://img.shields.io/github/stars/DataSoft/Honeyd/blob/master/scripts/misc/honeydsum-v0.3/honeydsum.pl?style=flat)](https://github.com/DataSoft/Honeyd/blob/master/scripts/misc/honeydsum-v0.3/honeydsum.pl/stargazers)

## Network and Artifact Analysis

- Sandbox

  - [Argos](http://www.few.vu.nl/argos/) - Emulator for capturing zero-day attacks.
  - [COMODO automated sandbox](https://help.comodo.com/topic-72-1-451-4768-.html)
  - [Cuckoo](https://cuckoosandbox.org/) - Leading open source automated malware analysis system.
  - [Pylibemu](https://github.com/buffer/pylibemu) [![GitHub stars](https://img.shields.io/github/stars/buffer/pylibemu?style=flat)](https://github.com/buffer/pylibemu/stargazers) - Libemu Cython wrapper.
  - [RFISandbox](https://monkey.org/~jose/software/rfi-sandbox/) - PHP 5.x script sandbox built on top of [funcall](https://pecl.php.net/package/funcall).
  - [dorothy2](https://github.com/m4rco-/dorothy2) [![GitHub stars](https://img.shields.io/github/stars/m4rco-/dorothy2?style=flat)](https://github.com/m4rco-/dorothy2/stargazers) - Malware/botnet analysis framework written in Ruby.
  - [imalse](https://github.com/hbhzwj/imalse) [![GitHub stars](https://img.shields.io/github/stars/hbhzwj/imalse?style=flat)](https://github.com/hbhzwj/imalse/stargazers) - Integrated MALware Simulator and Emulator.
  - [libemu](https://github.com/buffer/libemu) [![GitHub stars](https://img.shields.io/github/stars/buffer/libemu?style=flat)](https://github.com/buffer/libemu/stargazers) - Shellcode emulation library, useful for shellcode detection.

- Sandbox-as-a-Service

  - [Hybrid Analysis](https://www.hybrid-analysis.com) - Free malware analysis service powered by Payload Security that detects and analyzes unknown threats using a unique Hybrid Analysis technology.
  - [Joebox Cloud](https://jbxcloud.joesecurity.org/login) - Analyzes the behavior of malicious files including PEs, PDFs, DOCs, PPTs, XLSs, APKs, URLs and MachOs on Windows, Android and Mac OS X for suspicious activities.
  - [VirusTotal](https://www.virustotal.com/) - Analyze suspicious files and URLs to detect types of malware, and automatically share them with the security community.
  - [malwr.com](https://malwr.com/) - Free malware analysis service and community.

## Data Tools

- Front Ends

  - [DionaeaFR](https://github.com/rubenespadas/DionaeaFR) [![GitHub stars](https://img.shields.io/github/stars/rubenespadas/DionaeaFR?style=flat)](https://github.com/rubenespadas/DionaeaFR/stargazers) - Front Web to Dionaea low-interaction honeypot.
  - [Django-kippo](https://github.com/jedie/django-kippo) [![GitHub stars](https://img.shields.io/github/stars/jedie/django-kippo?style=flat)](https://github.com/jedie/django-kippo/stargazers) - Django App for kippo SSH Honeypot.
  - [Shockpot-Frontend](https://github.com/GovCERT-CZ/Shockpot-Frontend) [![GitHub stars](https://img.shields.io/github/stars/GovCERT-CZ/Shockpot-Frontend?style=flat)](https://github.com/GovCERT-CZ/Shockpot-Frontend/stargazers) - Full featured script to visualize statistics from a Shockpot honeypot.
  - [Tango](https://github.com/aplura/Tango) [![GitHub stars](https://img.shields.io/github/stars/aplura/Tango?style=flat)](https://github.com/aplura/Tango/stargazers) - Honeypot Intelligence with Splunk.
  - [Wordpot-Frontend](https://github.com/GovCERT-CZ/Wordpot-Frontend) [![GitHub stars](https://img.shields.io/github/stars/GovCERT-CZ/Wordpot-Frontend?style=flat)](https://github.com/GovCERT-CZ/Wordpot-Frontend/stargazers) - Full featured script to visualize statistics from a Wordpot honeypot.
  - [honeyalarmg2](https://github.com/schmalle/honeyalarmg2) [![GitHub stars](https://img.shields.io/github/stars/schmalle/honeyalarmg2?style=flat)](https://github.com/schmalle/honeyalarmg2/stargazers) - Simplified UI for showing honeypot alarms.
  - [honeypotDisplay](https://github.com/Joss-Steward/honeypotDisplay) [![GitHub stars](https://img.shields.io/github/stars/Joss-Steward/honeypotDisplay?style=flat)](https://github.com/Joss-Steward/honeypotDisplay/stargazers) - Flask website which displays data gathered from an SSH Honeypot.

- Visualization

  - [Acapulco](https://github.com/hgascon/acapulco) [![GitHub stars](https://img.shields.io/github/stars/hgascon/acapulco?style=flat)](https://github.com/hgascon/acapulco/stargazers) - Automated Attack Community Graph Construction.
  - [Afterglow Cloud](https://github.com/ayrus/afterglow-cloud) [![GitHub stars](https://img.shields.io/github/stars/ayrus/afterglow-cloud?style=flat)](https://github.com/ayrus/afterglow-cloud/stargazers)
  - [Afterglow](http://afterglow.sourceforge.net/)
  - [Glastopf Analytics](https://github.com/katkad/Glastopf-Analytics) [![GitHub stars](https://img.shields.io/github/stars/katkad/Glastopf-Analytics?style=flat)](https://github.com/katkad/Glastopf-Analytics/stargazers) - Easy honeypot statistics.
  - [HoneyMalt](https://github.com/SneakersInc/HoneyMalt) [![GitHub stars](https://img.shields.io/github/stars/SneakersInc/HoneyMalt?style=flat)](https://github.com/SneakersInc/HoneyMalt/stargazers) - Maltego tranforms for mapping Honeypot systems.
  - [HoneyMap](https://github.com/fw42/honeymap) [![GitHub stars](https://img.shields.io/github/stars/fw42/honeymap?style=flat)](https://github.com/fw42/honeymap/stargazers) - Real-time websocket stream of GPS events on a fancy SVG world map.
  - [HoneyStats](https://sourceforge.net/projects/honeystats/) - Statistical view of the recorded activity on a Honeynet.
  - [HpfeedsHoneyGraph](https://github.com/yuchincheng/HpfeedsHoneyGraph) [![GitHub stars](https://img.shields.io/github/stars/yuchincheng/HpfeedsHoneyGraph?style=flat)](https://github.com/yuchincheng/HpfeedsHoneyGraph/stargazers) - Visualization app to visualize hpfeeds logs.
  - [IVRE](https://github.com/ivre/ivre) [![GitHub stars](https://img.shields.io/github/stars/ivre/ivre?style=flat)](https://github.com/ivre/ivre/stargazers) - Network recon framework, published by @cea-sec & @ANSSI-FR. Build your own, self-hosted and fully-controlled alternatives to Criminalip / Shodan / ZoomEye / Censys and GreyNoise, run your Passive DNS service, collect and analyse network intelligence from your sensors, and much more!
  - [Kippo stats](https://github.com/mfontani/kippo-stats) [![GitHub stars](https://img.shields.io/github/stars/mfontani/kippo-stats?style=flat)](https://github.com/mfontani/kippo-stats/stargazers) - Mojolicious app to display statistics for your kippo SSH honeypot.
  - [Kippo-Graph](https://bruteforcelab.com/kippo-graph) - Full featured script to visualize statistics from a Kippo SSH honeypot.
  - [The Intelligent HoneyNet](https://github.com/jpyorre/IntelligentHoneyNet) [![GitHub stars](https://img.shields.io/github/stars/jpyorre/IntelligentHoneyNet?style=flat)](https://github.com/jpyorre/IntelligentHoneyNet/stargazers) - Create actionable information from honeypots.
  - [ovizart](https://github.com/oguzy/ovizart) [![GitHub stars](https://img.shields.io/github/stars/oguzy/ovizart?style=flat)](https://github.com/oguzy/ovizart/stargazers) - Visual analysis for network traffic.
  - [SSH-Radar](https://github.com/antonsatt/ssh-radar) [![GitHub stars](https://img.shields.io/github/stars/antonsatt/ssh-radar?style=flat)](https://github.com/antonsatt/ssh-radar/stargazers) - Real-time monitoring and visualization of failed SSH login attempts with geolocation and Grafana dashboards.

## Guides

- [T-Pot: A Multi-Honeypot Platform](https://dtag-dev-sec.github.io/mediator/feature/2015/03/17/concept.html)
- [Honeypot (Dionaea and kippo) setup script](https://github.com/andrewmichaelsmith/honeypot-setup-script/) [![GitHub stars](https://img.shields.io/github/stars/andrewmichaelsmith/honeypot-setup-script/?style=flat)](https://github.com/andrewmichaelsmith/honeypot-setup-script//stargazers)
- [The Security Canary Maturity Model](https://tracebit.com/blog/the-security-canary-maturity-model)

- Deployment

  - [Dionaea and EC2 in 20 Minutes](http://andrewmichaelsmith.com/2012/03/dionaea-honeypot-on-ec2-in-20-minutes/) - Tutorial on setting up Dionaea on an EC2 instance.
  - [Using a Raspberry Pi honeypot to contribute data to DShield/ISC](https://isc.sans.edu/diary/22680) - The Raspberry Pi based system will allow us to maintain one code base that will make it easier to collect rich logs beyond firewall logs.
  - [honeypotpi](https://github.com/free5ty1e/honeypotpi) [![GitHub stars](https://img.shields.io/github/stars/free5ty1e/honeypotpi?style=flat)](https://github.com/free5ty1e/honeypotpi/stargazers) - Script for turning a Raspberry Pi into a HoneyPot Pi.

- Research Papers

  - [Honeypot research papers](https://github.com/shbhmsingh72/Honeypot-Research-Papers) [![GitHub stars](https://img.shields.io/github/stars/shbhmsingh72/Honeypot-Research-Papers?style=flat)](https://github.com/shbhmsingh72/Honeypot-Research-Papers/stargazers) - PDFs of research papers on honeypots.
  - [vEYE](https://link.springer.com/article/10.1007%2Fs10115-008-0137-3) - Behavioral footprinting for self-propagating worm detection and profiling.
  - [The Tularosa Study: An Experimental Design and Implementation to Quantify the Effectiveness of Cyber Deception](https://www.osti.gov/servlets/purl/1524844)
  - ['It's Not Paranoia If They're Really After You': When Announcing Deception Technology Can Change Attacker Decisions](https://scholarspace.manoa.hawaii.edu/items/88cd00a5-914f-456e-a322-01c22fd5b7d7)
  - [When to Deceive: A Cross-Layer Stackelberg Game Framework for Strategic Timing of Cyber Deception](https://arxiv.org/pdf/2505.21244)
