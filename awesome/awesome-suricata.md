# Suricata

[![GitHub stars](https://img.shields.io/github/stars/satta/awesome-suricata?style=flat)](https://github.com/satta/awesome-suricata/stargazers)

# Awesome Suricata [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

[<img src="https://suricata.io/wp-content/uploads/2022/01/Logo-SuricataFinal-1-translucent.png" align="right" width="120">](https://suricata.io)

> Curated list of awesome things related to Suricata.

[Suricata](https://suricata.io/features) is a free intrusion detection/prevention system (IDS/IPS) and network security monitoring engine.

## Contents

- [Input Tools](#input-tools)
- [Output Tools](#output-tools)
- [Operations, Monitoring and Troubleshooting](#operations-monitoring-and-troubleshooting)
- [Programming Libraries and Toolkits](#programming-libraries-and-toolkits)
- [Dashboards and Templates](#dashboards-and-templates)
- [Development Tools](#development-tools)
- [Documentation and Guides](#documentation-and-guides)
- [Analysis Tools](#analysis-tools)
- [Rule Sets](#rule-sets)
- [Rule/Security Content Management and Handling](#rulesecurity-content-management-and-handling)
- [Plugins and Extensions](#plugins-and-extensions)
- [Systems Using Suricata](#systems-using-suricata)
- [Training](#training)
- [Simulation and Testing](#simulation-and-testing)
- [Data Sets](#data-sets)
- [Misc](#misc)


## Input Tools

- [PacketStreamer](https://github.com/deepfence/PacketStreamer) [![GitHub stars](https://img.shields.io/github/stars/deepfence/PacketStreamer?style=flat)](https://github.com/deepfence/PacketStreamer/stargazers) - Distributed tcpdump for cloud native environments.


## Output Tools

- [suricata-kafka-output](https://github.com/Center-Sun/suricata-kafka-output) [![GitHub stars](https://img.shields.io/github/stars/Center-Sun/suricata-kafka-output?style=flat)](https://github.com/Center-Sun/suricata-kafka-output/stargazers) - Suricata Eve Kafka Output Plugin for Suricata 6.
- [suricata-redis-output](https://github.com/jasonish/suricata-redis-output) [![GitHub stars](https://img.shields.io/github/stars/jasonish/suricata-redis-output?style=flat)](https://github.com/jasonish/suricata-redis-output/stargazers) - Suricata Eve Redis Output Plugin for Suricata 7.
- [Meer](https://github.com/quadrantsec/meer) [![GitHub stars](https://img.shields.io/github/stars/quadrantsec/meer?style=flat)](https://github.com/quadrantsec/meer/stargazers) - A "spooler" for Suricata / Sagan.
- [FEVER](https://github.com/DCSO/fever) [![GitHub stars](https://img.shields.io/github/stars/DCSO/fever?style=flat)](https://github.com/DCSO/fever/stargazers) - Fast, extensible, versatile event router for Suricata's EVE-JSON format.
- [Suricata-Logstash-Templates](https://github.com/pevma/Suricata-Logstash-Templates) [![GitHub stars](https://img.shields.io/github/stars/pevma/Suricata-Logstash-Templates?style=flat)](https://github.com/pevma/Suricata-Logstash-Templates/stargazers) - Templates for Kibana/Logstash to use with Suricata IDPS.
- [Lilith](https://github.com/VVelox/Lilith) [![GitHub stars](https://img.shields.io/github/stars/VVelox/Lilith?style=flat)](https://github.com/VVelox/Lilith/stargazers) - Reads EVE files into SQL as well as search stored data.


## Operations, Monitoring and Troubleshooting

- [slinkwatch](https://github.com/DCSO/slinkwatch) [![GitHub stars](https://img.shields.io/github/stars/DCSO/slinkwatch?style=flat)](https://github.com/DCSO/slinkwatch/stargazers) - Automatic enumeration and maintenance of Suricata monitoring interfaces.
- [suri-stats](https://github.com/regit/suri-stats) [![GitHub stars](https://img.shields.io/github/stars/regit/suri-stats?style=flat)](https://github.com/regit/suri-stats/stargazers) - A tool to work on suricata `stats.log` file.
- [Mauerspecht](https://github.com/DCSO/mauerspecht) [![GitHub stars](https://img.shields.io/github/stars/DCSO/mauerspecht?style=flat)](https://github.com/DCSO/mauerspecht/stargazers) - Simple Probing Tool for Corporate Walled Garden Networks.
- [ansible-suricata](https://github.com/GitMirar/ansible-suricata) [![GitHub stars](https://img.shields.io/github/stars/GitMirar/ansible-suricata?style=flat)](https://github.com/GitMirar/ansible-suricata/stargazers) - Suricata Ansible role (slightly outdated).
- [MassDeploySuricata](https://github.com/pevma/MassDeploySuricata) [![GitHub stars](https://img.shields.io/github/stars/pevma/MassDeploySuricata?style=flat)](https://github.com/pevma/MassDeploySuricata/stargazers) - Mass deploy and update Suricata IDPS using Ansible IT automation platform.
- [docker-suricata](https://github.com/jasonish/docker-suricata) [![GitHub stars](https://img.shields.io/github/stars/jasonish/docker-suricata?style=flat)](https://github.com/jasonish/docker-suricata/stargazers) - Suricata Docker image.
- [Suricata-Monitoring](https://github.com/VVelox/Suricata-Monitoring) [![GitHub stars](https://img.shields.io/github/stars/VVelox/Suricata-Monitoring?style=flat)](https://github.com/VVelox/Suricata-Monitoring/stargazers) - LibreNMS JSON / Nagios monitor for Suricata stats.
- [Terraform Module for Suricata](https://github.com/onetwopunch/terraform-google-suricata) [![GitHub stars](https://img.shields.io/github/stars/onetwopunch/terraform-google-suricata?style=flat)](https://github.com/onetwopunch/terraform-google-suricata/stargazers) - Terraform module to setup Google Cloud packet mirroring and send packets to Suricata.
- [InfluxDB Suricata Input Plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/suricata) [![GitHub stars](https://img.shields.io/github/stars/influxdata/telegraf/tree/master/plugins/inputs/suricata?style=flat)](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/suricata/stargazers) - Input Plugin for Telegraf to collect and forward Suricata `stats` logs (included out of the box in recent Telegraf releases).
- [suricata_exporter](https://github.com/corelight/suricata_exporter) [![GitHub stars](https://img.shields.io/github/stars/corelight/suricata_exporter?style=flat)](https://github.com/corelight/suricata_exporter/stargazers) - Simple Prometheus exporter written in Go exporting stats metrics scraped from Suricata socket.
- [Triagewall](https://github.com/aaronphifer/triagewall) [![GitHub stars](https://img.shields.io/github/stars/aaronphifer/triagewall?style=flat)](https://github.com/aaronphifer/triagewall/stargazers) - Local-LLM triage layer for Suricata alerts, using a tunable prefilter and Ollama classifier to reduce alert volume.


## Programming Libraries and Toolkits

- [rust-suricatax-rule-parser](https://github.com/jasonish/rust-suricatax-rule-parser) [![GitHub stars](https://img.shields.io/github/stars/jasonish/rust-suricatax-rule-parser?style=flat)](https://github.com/jasonish/rust-suricatax-rule-parser/stargazers) - Experimental Suricata Rule Parser in Rust.
- [go-suricata](https://github.com/ks2211/go-suricata) [![GitHub stars](https://img.shields.io/github/stars/ks2211/go-suricata?style=flat)](https://github.com/ks2211/go-suricata/stargazers) - Go Client for Suricata (Interacting via Socket).
- [gonids](https://github.com/google/gonids) [![GitHub stars](https://img.shields.io/github/stars/google/gonids?style=flat)](https://github.com/google/gonids/stargazers) - Go library to parse intrusion detection rules for engines like Snort and Suricata.
- [surevego](https://github.com/rhaist/surevego) [![GitHub stars](https://img.shields.io/github/stars/rhaist/surevego?style=flat)](https://github.com/rhaist/surevego/stargazers) - Suricata EVE-JSON parser in Go.
- [suricataparser](https://github.com/m-chrome/py-suricataparser) [![GitHub stars](https://img.shields.io/github/stars/m-chrome/py-suricataparser?style=flat)](https://github.com/m-chrome/py-suricataparser/stargazers) - Pure python parser for Snort/Suricata rules.
- [py-idstools](https://github.com/jasonish/py-idstools) [![GitHub stars](https://img.shields.io/github/stars/jasonish/py-idstools?style=flat)](https://github.com/jasonish/py-idstools/stargazers) - Snort and Suricata Rule and Event Utilities in Python (Including a Rule Update Tool).


## Dashboards and Templates

- [KTS](https://github.com/StamusNetworks/KTS) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/KTS?style=flat)](https://github.com/StamusNetworks/KTS/stargazers) - Kibana 4 Templates for Suricata IDPS Threat Hunting.
- [KTS5](https://github.com/StamusNetworks/KTS5) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/KTS5?style=flat)](https://github.com/StamusNetworks/KTS5/stargazers) - Kibana 5 Templates for Suricata IDPS Threat Hunting.
- [KTS6](https://github.com/StamusNetworks/KTS6) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/KTS6?style=flat)](https://github.com/StamusNetworks/KTS6/stargazers) - Kibana 6 Templates for Suricata IDPS Threat Hunting.
- [KTS7](https://github.com/StamusNetworks/KTS7) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/KTS7?style=flat)](https://github.com/StamusNetworks/KTS7/stargazers) - Kibana 7 Templates for Suricata IDPS Threat Hunting.


## Development Tools

- [Suricata Language Server](https://github.com/StamusNetworks/suricata-language-server) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/suricata-language-server?style=flat)](https://github.com/StamusNetworks/suricata-language-server/stargazers) - An implementation of the Language Server Protocol for Suricata signatures. It adds syntax check, hints and auto-completion to your preferred editor once it is configured.
- [suricata-ls-vscode](https://github.com/StamusNetworks/suricata-ls-vscode) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/suricata-ls-vscode?style=flat)](https://github.com/StamusNetworks/suricata-ls-vscode/stargazers) - Suricata IntelliSense Extension using the Suricata Language Server.
- [suricata-highlight-vscode](https://github.com/dgenzer/suricata-highlight-vscode) [![GitHub stars](https://img.shields.io/github/stars/dgenzer/suricata-highlight-vscode?style=flat)](https://github.com/dgenzer/suricata-highlight-vscode/stargazers) - Suricata Rules Support for Visual Studio Code (syntax highlighting, etc).
- [SublimeSuricata](https://github.com/ozuriexv/SublimeSuricata) [![GitHub stars](https://img.shields.io/github/stars/ozuriexv/SublimeSuricata?style=flat)](https://github.com/ozuriexv/SublimeSuricata/stargazers) - Basic Suricata syntax highlighter for Sublime Text.
- [Suricata-Check](https://suricata-check.teuwen.net/readme.html) - A command-line utility to provide feedback on Suricata rules. It can detect issues such as covering syntax validity, interpretability, rule specificity, rule coverage, and efficiency.

## Documentation and Guides

- [SEPTun](https://github.com/pevma/SEPTun) [![GitHub stars](https://img.shields.io/github/stars/pevma/SEPTun?style=flat)](https://github.com/pevma/SEPTun/stargazers) - Suricata Extreme Performance Tuning guide.
- [SEPTun-Mark-II](https://github.com/pevma/SEPTun-Mark-II) [![GitHub stars](https://img.shields.io/github/stars/pevma/SEPTun-Mark-II?style=flat)](https://github.com/pevma/SEPTun-Mark-II/stargazers) - Suricata Extreme Performance Tuning guide - Mark II.
- [suricata-4-analysts](https://github.com/StamusNetworks/suricata-4-analysts) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/suricata-4-analysts?style=flat)](https://github.com/StamusNetworks/suricata-4-analysts/stargazers) - The Security Analyst's Guide to Suricata.
- [Suricata Community Style Guide](https://github.com/sidallocation/suricata-style-guide) [![GitHub stars](https://img.shields.io/github/stars/sidallocation/suricata-style-guide?style=flat)](https://github.com/sidallocation/suricata-style-guide/stargazers) - A collaborative document to collect style guidelines from the community of rule writers.


## Analysis Tools

- [Suricata Analytics](https://github.com/StamusNetworks/suricata-analytics) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/suricata-analytics?style=flat)](https://github.com/StamusNetworks/suricata-analytics/stargazers) - Various resources that are useful when interacting with Suricata data.
- [Malcolm](https://github.com/cisagov/Malcolm) [![GitHub stars](https://img.shields.io/github/stars/cisagov/Malcolm?style=flat)](https://github.com/cisagov/Malcolm/stargazers) - A powerful, easily deployable network traffic analysis tool suite for full packet capture artifacts (PCAP files), Zeek logs and Suricata alerts.
- [Evebox](https://github.com/jasonish/evebox) [![GitHub stars](https://img.shields.io/github/stars/jasonish/evebox?style=flat)](https://github.com/jasonish/evebox/stargazers) - Web Based Event Viewer (GUI) for Suricata EVE Events in Elastic Search.


## Rule Sets

- [nids-rule-library](https://github.com/klingerko/nids-rule-library#readme) - Collection of various open-source and commercial rulesets.
- [Stamus Lateral Movement Detection Rules](https://www.stamus-networks.com/blog/new-open-ruleset-for-detecting-lateral-movement-with-suricata) - Suricata ruleset to detect lateral movement.
- [QuadrantSec Suricata Rules](https://github.com/quadrantsec/suricata-rules) [![GitHub stars](https://img.shields.io/github/stars/quadrantsec/suricata-rules?style=flat)](https://github.com/quadrantsec/suricata-rules/stargazers) - Set of Suricata rules published by QuadrantSec.
- [Cluster25/detection](https://github.com/Cluster25/detection) [![GitHub stars](https://img.shields.io/github/stars/Cluster25/detection?style=flat)](https://github.com/Cluster25/detection/stargazers) - Cluster25's detection rules.
- Networkforensic.dk (NF) rules sets: 
  - [NF IDS rules](https://networkforensic.dk/SNORT/NF-local.zip)
  - [NF SCADA IDS Rules](https://networkforensic.dk/SNORT/NF-SCADA.zip)
  - [NF Scanners IDS Rules](https://networkforensic.dk/SNORT/NF-Scanners.zip)
- [Quantum Insert detection for Suricata](https://github.com/fox-it/quantuminsert/blob/master/detection/suricata/README.md) [![GitHub stars](https://img.shields.io/github/stars/fox-it/quantuminsert/blob/master/detection/suricata/README.md?style=flat)](https://github.com/fox-it/quantuminsert/blob/master/detection/suricata/README.md/stargazers) - Suricata rules accompanying Fox-IT's QUANTUM 2015 blog/BroCon talk.
- [Hunting rules](https://github.com/travisbgreen/hunting-rules) [![GitHub stars](https://img.shields.io/github/stars/travisbgreen/hunting-rules?style=flat)](https://github.com/travisbgreen/hunting-rules/stargazers) - Suricata IDS alert rules for network anomaly detection from Travis Green.
- [3CORESec NIDS - Lateral Movement](https://dtection.io/ruleset/3cs_lateral) - Suricata ruleset focusing on lateral movement techniques (paid).
- [3CORESec NIDS - Sinkholes](https://dtection.io/ruleset/3cs_sinkholes) - Suricata ruleset focused on a curated list of public malware sinkholes (free).
- [PAW Patrules](https://pawpatrules.fr) - Another free (CC BY-NC-SA) collection of rules for the Suricata engine.
- [opnsense-suricata-nmaps](https://github.com/aleksibovellan/opnsense-suricata-nmaps) [![GitHub stars](https://img.shields.io/github/stars/aleksibovellan/opnsense-suricata-nmaps?style=flat)](https://github.com/aleksibovellan/opnsense-suricata-nmaps/stargazers) - OPNSense's Suricata IDS/IPS Detection Rules Against NMAP Scans.
- [Antiphishing](https://github.com/julioliraup/Antiphishing) [![GitHub stars](https://img.shields.io/github/stars/julioliraup/Antiphishing?style=flat)](https://github.com/julioliraup/Antiphishing/stargazers) - Suricata rules and datasets to detect phishing attacks.


## Rule/Security Content Management and Handling

- [sidallocation.org](https://sidallocation.org/) - Sid Allocation working group, list of SID ranges.
- [Scirius](https://github.com/StamusNetworks/scirius) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/scirius?style=flat)](https://github.com/StamusNetworks/scirius/stargazers) - Web application for Suricata ruleset management and threat hunting.
- [IOCmite](https://github.com/sebdraven/IOCmite) [![GitHub stars](https://img.shields.io/github/stars/sebdraven/IOCmite?style=flat)](https://github.com/sebdraven/IOCmite/stargazers) - Tool to create dataset for suricata with indicators of MISP instances and add sightings in MISP if an indicator of dataset generates an alert.
- [luaevilbit](https://github.com/regit/luaevilbit) [![GitHub stars](https://img.shields.io/github/stars/regit/luaevilbit?style=flat)](https://github.com/regit/luaevilbit/stargazers) - An Evil bit implementation in luajit for Suricata.
- [Lawmaker](https://www.3coresec.com/solutions/lawmaker) - Suricata IDS rule and fleet management system.
- [surify-cli](https://github.com/dgenzer/surify-cli) [![GitHub stars](https://img.shields.io/github/stars/dgenzer/surify-cli?style=flat)](https://github.com/dgenzer/surify-cli/stargazers) - Generate suricata-rules from collection of IOCs (JSON, CSV or flags) based on your suricata template.
- [suricata-prettifier](https://github.com/theY4Kman/suricata-prettifier) [![GitHub stars](https://img.shields.io/github/stars/theY4Kman/suricata-prettifier?style=flat)](https://github.com/theY4Kman/suricata-prettifier/stargazers) - Command-line tool to format and syntax highlight Suricata rules.
- [OTX-Suricata](https://github.com/AlienVault-OTX/OTX-Suricata) [![GitHub stars](https://img.shields.io/github/stars/AlienVault-OTX/OTX-Suricata?style=flat)](https://github.com/AlienVault-OTX/OTX-Suricata/stargazers) - Create rules and configuration for Suricata to alert on indicators from an OTX account.
- [Aristotle](https://github.com/secureworks/aristotle) [![GitHub stars](https://img.shields.io/github/stars/secureworks/aristotle?style=flat)](https://github.com/secureworks/aristotle/stargazers) - Simple Python program that allows for the filtering and modifying of Suricata and Snort rulesets based on interpreted key-value pairs present in the metadata keyword within each rule.


## Plugins and Extensions

- [suricata-zabbix](https://github.com/catenacyber/suricata-zabbix) [![GitHub stars](https://img.shields.io/github/stars/catenacyber/suricata-zabbix?style=flat)](https://github.com/catenacyber/suricata-zabbix/stargazers) - Zabbix application layer plugin for Suricata.


## Systems Using Suricata

- [SELKS](https://github.com/StamusNetworks/SELKS) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/SELKS?style=flat)](https://github.com/StamusNetworks/SELKS/stargazers) - A Suricata-based intrusion detection system/intrusion prevention system/network security monitoring distribution.
- [Amsterdam](https://github.com/StamusNetworks/Amsterdam) [![GitHub stars](https://img.shields.io/github/stars/StamusNetworks/Amsterdam?style=flat)](https://github.com/StamusNetworks/Amsterdam/stargazers) - Docker based Suricata, Elasticsearch, Logstash, Kibana, Scirius aka SELKS.
- [pfSense](https://www.pfsense.org) - A free network firewall distribution, based on the FreeBSD operating system with a custom kernel and including third party free software packages for additional functionality.
- [OPNsense](https://opnsense.org) - An open source, easy-to-use and easy-to-build FreeBSD based firewall and routing platform.
- [Artica](https://github.com/dtouzeau/artica-suricata) [![GitHub stars](https://img.shields.io/github/stars/dtouzeau/artica-suricata?style=flat)](https://github.com/dtouzeau/artica-suricata/stargazers) - Suricata IDS integration for the [Artica](https://artica.systems) gateway appliance.
- [Shovel](https://github.com/FCSC-FR/shovel) [![GitHub stars](https://img.shields.io/github/stars/FCSC-FR/shovel?style=flat)](https://github.com/FCSC-FR/shovel/stargazers) - Web interface to explore Suricata EVE outputs, with a primary focus on network analysis in CTF competitions.


## Training

- [Experimental Suricata Training Environment](https://github.com/jasonish/experimental-suricata-training) [![GitHub stars](https://img.shields.io/github/stars/jasonish/experimental-suricata-training?style=flat)](https://github.com/jasonish/experimental-suricata-training/stargazers) - Suricata Training Environment based on Docker(-Compose).
- [CDMCS](https://github.com/ccdcoe/CDMCS/tree/master) [![GitHub stars](https://img.shields.io/github/stars/ccdcoe/CDMCS/tree/master?style=flat)](https://github.com/ccdcoe/CDMCS/tree/master/stargazers) - Cyber Defence Monitoring Course: Rule-based Threat Detection.


## Simulation and Testing

- [Leonidas](https://github.com/WithSecureLabs/leonidas) [![GitHub stars](https://img.shields.io/github/stars/WithSecureLabs/leonidas?style=flat)](https://github.com/WithSecureLabs/leonidas/stargazers) - Automated Attack Simulation in the Cloud, complete with detection use cases.
- [speeve](https://github.com/satta/speeve) [![GitHub stars](https://img.shields.io/github/stars/satta/speeve?style=flat)](https://github.com/satta/speeve/stargazers) - Fast, probabilistic EVE-JSON generator for testing and benchmarking of EVE-consuming applications.
- [Dalton](https://github.com/secureworks/dalton) [![GitHub stars](https://img.shields.io/github/stars/secureworks/dalton?style=flat)](https://github.com/secureworks/dalton/stargazers) - Suricata and Snort IDS rule and pcap testing system.


## Data Sets

- [suricata-sample-data](https://github.com/FrankHassanabad/suricata-sample-data) [![GitHub stars](https://img.shields.io/github/stars/FrankHassanabad/suricata-sample-data?style=flat)](https://github.com/FrankHassanabad/suricata-sample-data/stargazers) - Repository of creating different example suricata data sets.


## Misc

- [Suriwire](https://github.com/regit/suriwire) [![GitHub stars](https://img.shields.io/github/stars/regit/suriwire?style=flat)](https://github.com/regit/suriwire/stargazers) - Wireshark plugin to display Suricata analysis info.
- [bash_cata](https://github.com/isMTv/bash_cata) [![GitHub stars](https://img.shields.io/github/stars/isMTv/bash_cata?style=flat)](https://github.com/isMTv/bash_cata/stargazers) - A simple script that processes the generated Suricata eve-log in real time and, based on alerts, adds an ip-address to the MikroTik Address Lists for a specified time for subsequent blocking.
- [suriGUI](https://github.com/control-owl/suriGUI) [![GitHub stars](https://img.shields.io/github/stars/control-owl/suriGUI?style=flat)](https://github.com/control-owl/suriGUI/stargazers) - GUI for Suricata + Qubes OS.
- [SuriGuard](https://github.com/SEc-123/SuriGuard1) [![GitHub stars](https://img.shields.io/github/stars/SEc-123/SuriGuard1?style=flat)](https://github.com/SEc-123/SuriGuard1/stargazers) - Web-based management system for Suricata IDS/IPS, featuring advanced analytics and visualization capabilities.
