# Cybersecurity Blue Team

[![GitHub stars](https://img.shields.io/github/stars/fabacab/awesome-cybersecurity-blueteam?style=flat)](https://github.com/fabacab/awesome-cybersecurity-blueteam/stargazers)

# Awesome Cybersecurity Blue Team [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> A collection of awesome resources, tools, and other shiny things for cybersecurity blue teams.

[Cybersecurity blue teams](https://en.wikipedia.org/wiki/Blue_team_(computer_security)) are groups of individuals who identify security flaws in information technology systems, verify the effectiveness of security measures, and monitor the systems to ensure that implemented defensive measures remain effective in the future. While not exclusive, this list is heavily biased towards [Free Software](https://www.gnu.org/philosophy/free-sw.html) projects and against proprietary products or corporate services. For offensive TTPs, please see [awesome-pentest](https://github.com/fabacab/awesome-pentest) [![GitHub stars](https://img.shields.io/github/stars/fabacab/awesome-pentest?style=flat)](https://github.com/fabacab/awesome-pentest/stargazers).

Your contributions and suggestions are heartily ♥ welcome. (✿◕‿◕). Please check the [Contributing Guidelines](CONTRIBUTING.md) for more details. This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

Many cybersecurity professionals enable racist state violence, wittingly or unwittingly, by providing services to local, state, and federal policing agencies or otherwise cooperating with similar institutions who do so. This evil most often happens through the coercive mechanism of employment under threat of lack of access to food, shelter, or healthcare. Despite this list's public availability, it is the maintainer's intention and hope that this list supports the people and organizations who work to counter such massive albeit banal evil.

![Image of a raised fist composed of the names of Black people murdered by taxpayer-funded racist police violence.](https://web.archive.org/web/20201028021653if_/https://lauerrealtygroup.com/wp-content/uploads/2020/06/BLM-FIST-scaled.jpg)

![Image of a "Blue Lives Matter" flag with the thin blue line being peeled away to reveal a Nazi swastika underneath.](https://web.archive.org/web/20201123181815if_/https://i.redd.it/86pl28p0dl631.jpg)

**[DEFUND THE POLICE.](https://defundthepolice.org/)**

## Contents

- [Automation and Convention](#automation-and-convention)
  - [Code libraries and bindings](#code-libraries-and-bindings)
  - [Security Orchestration, Automation, and Response (SOAR)](#security-orchestration-automation-and-response-soar)
- [Cloud platform security](#cloud-platform-security)
  - [Distributed monitoring](#distributed-monitoring)
  - [Kubernetes](#kubernetes)
  - [Service meshes](#service-meshes)
- [Communications security (COMSEC)](#communications-security-comsec)
- [DevSecOps](#devsecops)
  - [Application or Binary Hardening](#application-or-binary-hardening)
  - [Compliance testing and reporting](#compliance-testing-and-reporting)
  - [Dependency confusion](#dependency-confusion)
  - [Fuzzing](#fuzzing)
  - [Policy enforcement](#policy-enforcement)
  - [Supply chain security](#supply-chain-security)
- [Honeypots](#honeypots)
  - [Tarpits](#tarpits)
- [Host-based tools](#host-based-tools)
  - [Sandboxes](#sandboxes)
- [Identity and AuthN/AuthZ](#identity-and-authnauthz)
- [Incident Response tools](#incident-response-tools)
  - [IR management consoles](#ir-management-consoles)
  - [Evidence collection](#evidence-collection)
- [Network perimeter defenses](#network-perimeter-defenses)
  - [Firewall appliances or distributions](#firewall-appliances-or-distributions)
- [Operating System distributions](#operating-system-distributions)
- [Phishing awareness and reporting](#phishing-awareness-and-reporting)
- [Preparedness training and wargaming](#preparedness-training-and-wargaming)
  - [Post-engagement analysis and reporting](#post-engagement-analysis-and-reporting)
- [Security configurations](#security-configurations)
- [Security monitoring](#security-monitoring)
  - [Endpoint Detection and Response (EDR)](#endpoint-detection-and-response-edr)
  - [Network Security Monitoring (NSM)](#network-security-monitoring-nsm)
  - [Security Information and Event Management (SIEM)](#security-information-and-event-management-siem)
  - [Service and performance monitoring](#service-and-performance-monitoring)
  - [Threat hunting](#threat-hunting)
- [Threat intelligence](#threat-intelligence)
  - [Fingerprinting](#fingerprinting)
  - [Threat signature packages and collections](#threat-signature-packages-and-collections)
- [Tor Onion service defenses](#tor-onion-service-defenses)
- [Transport-layer defenses](#transport-layer-defenses)
  - [Overlay and Virtual Private Networks (VPNs)](#overlay-and-virtual-private-networks-vpns)
- [macOS-based defenses](#macos-based-defenses)
- [Windows-based defenses](#windows-based-defenses)
  - [Active Directory](#active-directory)

## Automation and Convention

- [Ansible Lockdown](https://ansiblelockdown.io/) - Curated collection of information security themed Ansible roles that are both vetted and actively maintained.
- [Clevis](https://github.com/latchset/clevis) [![GitHub stars](https://img.shields.io/github/stars/latchset/clevis?style=flat)](https://github.com/latchset/clevis/stargazers) - Plugable framework for automated decryption, often used as a Tang client.
- [DShell](https://github.com/USArmyResearchLab/Dshell) [![GitHub stars](https://img.shields.io/github/stars/USArmyResearchLab/Dshell?style=flat)](https://github.com/USArmyResearchLab/Dshell/stargazers) - Extensible network forensic analysis framework written in Python that enables rapid development of plugins to support the dissection of network packet captures.
- [Dev-Sec.io](https://dev-sec.io/) - Server hardening framework providing Ansible, Chef, and Puppet implementations of various baseline security configurations.
- [Password Manager Resources](https://github.com/apple/password-manager-resources) [![GitHub stars](https://img.shields.io/github/stars/apple/password-manager-resources?style=flat)](https://github.com/apple/password-manager-resources/stargazers) - Collaborative, crowd-sourced data and code to make password management better.
- [peepdf](https://eternal-todo.com/tools/peepdf-pdf-analysis-tool) - Scriptable PDF file analyzer.
- [PyREBox](https://talosintelligence.com/pyrebox) - Python-scriptable reverse engineering sandbox, based on QEMU.
- [Watchtower](https://containrrr.dev/watchtower/) - Container-based solution for automating Docker container base image updates, providing an unattended upgrade experience.

### Code libraries and bindings

- [MultiScanner](https://github.com/mitre/multiscanner) [![GitHub stars](https://img.shields.io/github/stars/mitre/multiscanner?style=flat)](https://github.com/mitre/multiscanner/stargazers) - File analysis framework written in Python that assists in evaluating a set of files by automatically running a suite of tools against them and aggregating the output.
- [Posh-VirusTotal](https://github.com/darkoperator/Posh-VirusTotal) [![GitHub stars](https://img.shields.io/github/stars/darkoperator/Posh-VirusTotal?style=flat)](https://github.com/darkoperator/Posh-VirusTotal/stargazers) - PowerShell interface to VirusTotal.com APIs.
- [censys-python](https://github.com/censys/censys-python) [![GitHub stars](https://img.shields.io/github/stars/censys/censys-python?style=flat)](https://github.com/censys/censys-python/stargazers) - Python wrapper to the Censys REST API.
- [libcrafter](https://github.com/pellegre/libcrafter) [![GitHub stars](https://img.shields.io/github/stars/pellegre/libcrafter?style=flat)](https://github.com/pellegre/libcrafter/stargazers) - High level C++ network packet sniffing and crafting library.
- [python-dshield](https://github.com/rshipp/python-dshield) [![GitHub stars](https://img.shields.io/github/stars/rshipp/python-dshield?style=flat)](https://github.com/rshipp/python-dshield/stargazers) - Pythonic interface to the Internet Storm Center/DShield API.
- [python-sandboxapi](https://github.com/InQuest/python-sandboxapi) [![GitHub stars](https://img.shields.io/github/stars/InQuest/python-sandboxapi?style=flat)](https://github.com/InQuest/python-sandboxapi/stargazers) - Minimal, consistent Python API for building integrations with malware sandboxes.
- [python-stix2](https://github.com/oasis-open/cti-python-stix2) [![GitHub stars](https://img.shields.io/github/stars/oasis-open/cti-python-stix2?style=flat)](https://github.com/oasis-open/cti-python-stix2/stargazers) - Python APIs for serializing and de-serializing Structured Threat Information eXpression (STIX) JSON content, plus higher-level APIs for common tasks.

### Security Orchestration, Automation, and Response (SOAR)

See also [Security Information and Event Management (SIEM)](#security-information-and-event-management-siem), and [IR management consoles](#ir-management-consoles).

- [Shuffle](https://shuffler.io/) - Graphical generalized workflow (automation) builder for IT professionals and blue teamers.

## Cloud platform security

See also [asecure.cloud/tools](https://asecure.cloud/tools/).

- [Aaia](https://github.com/rams3sh/Aaia) [![GitHub stars](https://img.shields.io/github/stars/rams3sh/Aaia?style=flat)](https://github.com/rams3sh/Aaia/stargazers) - Helps in visualizing AWS IAM and Organizations in a graph format with help of Neo4j.
- [Falco](https://falco.org/) - Behavioral activity monitor designed to detect anomalous activity in containerized applications, hosts, and network packet flows by auditing the Linux kernel and enriched by runtime data such as Kubernetes metrics.
- [Kata Containers](https://katacontainers.io/) - Secure container runtime with lightweight virtual machines that feel and perform like containers, but provide stronger workload isolation using hardware virtualization technology as a second layer of defense.
- [Principal Mapper (PMapper)](https://github.com/nccgroup/PMapper) [![GitHub stars](https://img.shields.io/github/stars/nccgroup/PMapper?style=flat)](https://github.com/nccgroup/PMapper/stargazers) - Quickly evaluate IAM permissions in AWS via script and library capable of identifying risks in the configuration of AWS Identity and Access Management (IAM) for an AWS account or an AWS organization.
- [Prowler](https://github.com/toniblyx/prowler) [![GitHub stars](https://img.shields.io/github/stars/toniblyx/prowler?style=flat)](https://github.com/toniblyx/prowler/stargazers) - Tool based on AWS-CLI commands for Amazon Web Services account security assessment and hardening.
- [Scout Suite](https://github.com/nccgroup/ScoutSuite) [![GitHub stars](https://img.shields.io/github/stars/nccgroup/ScoutSuite?style=flat)](https://github.com/nccgroup/ScoutSuite/stargazers) - Open source multi-cloud security-auditing tool, which enables security posture assessment of cloud environments.
- [gVisor](https://github.com/google/gvisor) [![GitHub stars](https://img.shields.io/github/stars/google/gvisor?style=flat)](https://github.com/google/gvisor/stargazers) - Application kernel, written in Go, that implements a substantial portion of the Linux system surface to provide an isolation boundary between the application and the host kernel.

### Distributed monitoring

See also [§ Service and performance monitoring](#service-and-performance-monitoring).

- [Cortex](https://cortexmetrics.io/) - Provides horizontally scalable, highly available, multi-tenant, long term storage for Prometheus.
- [Jaeger](https://www.jaegertracing.io/) - Distributed tracing platform backend used for monitoring and troubleshooting microservices-based distributed systems.
- [OpenTelemetry](https://opentelemetry.io/) - Observability framework for cloud-native software, comprising a collection of tools, APIs, and SDKs for exporting application performance metrics to a tracing backend (formerly maintained by the OpenTracing and OpenCensus projects).
- [Prometheus](https://prometheus.io/) - Open-source systems monitoring and alerting toolkit originally built at SoundCloud.
- [Zipkin](https://zipkin.io/) - Distributed tracing system backend that helps gather timing data needed to troubleshoot latency problems in service architectures.

### Kubernetes

See also [Kubernetes-Security.info](https://kubernetes-security.info/).

- [KubeSec](https://kubesec.io/) - Static analyzer of Kubernetes manifests that can be run locally, as a Kuberenetes admission controller, or as its own cloud service.
- [Kyverno](https://kyverno.io/) - Policy engine designed for Kubernetes.
- [Linkerd](https://linkerd.io/) - Ultra light Kubernetes-specific service mesh that adds observability, reliability, and security to Kubernetes applications without requiring any modification of the application itself.
- [Managed Kubernetes Inspection Tool (MKIT)](https://github.com/darkbitio/mkit) [![GitHub stars](https://img.shields.io/github/stars/darkbitio/mkit?style=flat)](https://github.com/darkbitio/mkit/stargazers) - Query and validate several common security-related configuration settings of managed Kubernetes cluster objects and the workloads/resources running inside the cluster.
- [Polaris](https://polaris.docs.fairwinds.com/) - Validates Kubernetes best practices by running tests against code commits, a Kubernetes admission request, or live resources already running in a cluster. 
- [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets) [![GitHub stars](https://img.shields.io/github/stars/bitnami-labs/sealed-secrets?style=flat)](https://github.com/bitnami-labs/sealed-secrets/stargazers) - Kubernetes controller and tool for one-way encrypted Secrets.
- [certificate-expiry-monitor](https://github.com/muxinc/certificate-expiry-monitor) [![GitHub stars](https://img.shields.io/github/stars/muxinc/certificate-expiry-monitor?style=flat)](https://github.com/muxinc/certificate-expiry-monitor/stargazers) - Utility that exposes the expiry of TLS certificates as Prometheus metrics.
- [k-rail](https://github.com/cruise-automation/k-rail) [![GitHub stars](https://img.shields.io/github/stars/cruise-automation/k-rail?style=flat)](https://github.com/cruise-automation/k-rail/stargazers) - Workload policy enforcement tool for Kubernetes.
- [kube-forensics](https://github.com/keikoproj/kube-forensics) [![GitHub stars](https://img.shields.io/github/stars/keikoproj/kube-forensics?style=flat)](https://github.com/keikoproj/kube-forensics/stargazers) - Allows a cluster administrator to dump the current state of a running pod and all its containers so that security professionals can perform off-line forensic analysis.
- [kube-hunter](https://kube-hunter.aquasec.com/) - Open-source tool that runs a set of tests ("hunters") for security issues in Kubernetes clusters from either outside ("attacker's view") or inside a cluster.
- [kubernetes-event-exporter](https://github.com/opsgenie/kubernetes-event-exporter) [![GitHub stars](https://img.shields.io/github/stars/opsgenie/kubernetes-event-exporter?style=flat)](https://github.com/opsgenie/kubernetes-event-exporter/stargazers) - Allows exporting the often missed Kubernetes events to various outputs so that they can be used for observability or alerting purposes.

### Service meshes

See also [ServiceMesh.es](https://servicemesh.es/).

- [Consul](https://consul.io/) - Solution to connect and configure applications across dynamic, distributed infrastructure and, with Consul Connect, enabling secure service-to-service communication with automatic TLS encryption and identity-based authorization.
- [Istio](https://istio.io/) - Open platform for providing a uniform way to integrate microservices, manage traffic flow across microservices, enforce policies and aggregate telemetry data.

## Communications security (COMSEC)

See also [Transport-layer defenses](#transport-layer-defenses).

- [GPG Sync](https://github.com/firstlookmedia/gpgsync) [![GitHub stars](https://img.shields.io/github/stars/firstlookmedia/gpgsync?style=flat)](https://github.com/firstlookmedia/gpgsync/stargazers) - Centralize and automate OpenPGP public key distribution, revocation, and updates amongst all members of an organization or team.
- [Geneva (Genetic Evasion)](https://censorship.ai/) - Novel experimental genetic algorithm that evolves packet-manipulation-based censorship evasion strategies against nation-state level censors to increase availability of otherwise blocked content.
- [GlobaLeaks](https://www.globaleaks.org/) - Free, open source software enabling anyone to easily set up and maintain a secure whistleblowing platform.
- [SecureDrop](https://securedrop.org/) - Open source whistleblower submission system that media organizations and NGOs can install to securely accept documents from anonymous sources.
- [Teleport](https://goteleport.com/) - Allows engineers and security professionals to unify access for SSH servers, Kubernetes clusters, web applications, and databases across all environments.

## DevSecOps

See also [awesome-devsecops](https://github.com/devsecops/awesome-devsecops) [![GitHub stars](https://img.shields.io/github/stars/devsecops/awesome-devsecops?style=flat)](https://github.com/devsecops/awesome-devsecops/stargazers).

- [Bane](https://github.com/genuinetools/bane) [![GitHub stars](https://img.shields.io/github/stars/genuinetools/bane?style=flat)](https://github.com/genuinetools/bane/stargazers) - Custom and better AppArmor profile generator for Docker containers.
- [BlackBox](https://github.com/StackExchange/blackbox) [![GitHub stars](https://img.shields.io/github/stars/StackExchange/blackbox?style=flat)](https://github.com/StackExchange/blackbox/stargazers) - Safely store secrets in Git/Mercurial/Subversion by encrypting them "at rest" using GnuPG.
- [Checkov](https://www.checkov.io/) - Static analysis for Terraform (infrastructure as code) to help detect CIS policy violations and prevent cloud security misconfiguration.
- [Cilium](https://cilium.io/) - Open source software for transparently securing the network connectivity between application services deployed using Linux container management platforms like Docker and Kubernetes.
- [Clair](https://github.com/coreos/clair) [![GitHub stars](https://img.shields.io/github/stars/coreos/clair?style=flat)](https://github.com/coreos/clair/stargazers) - Static analysis tool to probe for vulnerabilities introduced via application container (e.g., Docker) images.
- [CodeQL](https://securitylab.github.com/tools/codeql) - Discover vulnerabilities across a codebase by performing queries against code as though it were data.
- [DefectDojo](https://www.defectdojo.org/) - Application vulnerability management tool built for DevOps and continuous security integration.
- [Gauntlt](http://gauntlt.org/) - Pentest applications during routine continuous integration build pipelines.
- [Git Secrets](https://github.com/awslabs/git-secrets) [![GitHub stars](https://img.shields.io/github/stars/awslabs/git-secrets?style=flat)](https://github.com/awslabs/git-secrets/stargazers) - Prevents you from committing passwords and other sensitive information to a git repository.
- [SOPS](https://github.com/mozilla/sops) [![GitHub stars](https://img.shields.io/github/stars/mozilla/sops?style=flat)](https://github.com/mozilla/sops/stargazers) - Editor of encrypted files that supports YAML, JSON, ENV, INI and binary formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, and PGP.
- [Snyk](https://snyk.io/) - Finds and fixes vulnerabilities and license violations in open source dependencies and container images.
- [SonarQube](https://sonarqube.org) - Continuous inspection tool that provides detailed reports during automated testing and alerts on newly introduced security vulnerabilities.
- [Trivy](https://github.com/aquasecurity/trivy) [![GitHub stars](https://img.shields.io/github/stars/aquasecurity/trivy?style=flat)](https://github.com/aquasecurity/trivy/stargazers) - Simple and comprehensive vulnerability scanner for containers and other artifacts, suitable for use in continuous integration pipelines.
- [Vault](https://www.vaultproject.io/) - Tool for securely accessing secrets such as API keys, passwords, or certificates through a unified interface.
- [git-crypt](https://www.agwa.name/projects/git-crypt/) - Transparent file encryption in git; files which you choose to protect are encrypted when committed, and decrypted when checked out.
- [helm-secrets](https://github.com/jkroepke/helm-secrets) [![GitHub stars](https://img.shields.io/github/stars/jkroepke/helm-secrets?style=flat)](https://github.com/jkroepke/helm-secrets/stargazers) - Helm plugin that helps manage secrets with Git workflow and stores them anywhere, backed by SOPS.
- [terrascan](https://runterrascan.io/) - Static code analyzer for Infrastructure as Code tools that helps detect compliance and security violations to mitigate risk before provisioning cloud native resources.
- [tfsec](https://aquasecurity.github.io/tfsec/) - Static analysis security scanner for your Terraform code designed to run locally and in CI pipelines.

### Application or Binary Hardening

- [DynInst](https://dyninst.org/dyninst) - Tools for binary instrumentation, analysis, and modification, useful for binary patching.
- [DynamoRIO](https://dynamorio.org/) - Runtime code manipulation system that supports code transformations on any part of a program, while it executes, implemented as a process-level virtual machine.
- [Egalito](https://egalito.org/) - Binary recompiler and instrumentation framework that can fully disassemble, transform, and regenerate ordinary Linux binaries designed for binary hardening and security research.
- [Valgrind](https://www.valgrind.org/) - Instrumentation framework for building dynamic analysis tools.

### Compliance testing and reporting

- [Chef InSpec](https://www.chef.io/products/chef-inspec) - Language for describing security and compliance rules, which become automated tests that can be run against IT infrastructures to discover and report on non-compliance.
- [OpenSCAP Base](https://www.open-scap.org/tools/openscap-base/) - Both a library and a command line tool (`oscap`) used to evaluate a system against SCAP baseline profiles to report on the security posture of the scanned system(s). 

### Dependency confusion

See also [§ Supply chain security](#supply-chain-security).

- [Dependency Combobulator](https://github.com/apiiro/combobulator) [![GitHub stars](https://img.shields.io/github/stars/apiiro/combobulator?style=flat)](https://github.com/apiiro/combobulator/stargazers) - Open source, modular and extensible framework to detect and prevent dependency confusion leakage and potential attacks.
- [Confusion checker](https://github.com/sonatype-nexus-community/repo-diff) [![GitHub stars](https://img.shields.io/github/stars/sonatype-nexus-community/repo-diff?style=flat)](https://github.com/sonatype-nexus-community/repo-diff/stargazers) - Script to check if you have artifacts containing the same name between your repositories.
- [snync](https://github.com/snyk-labs/snync) [![GitHub stars](https://img.shields.io/github/stars/snyk-labs/snync?style=flat)](https://github.com/snyk-labs/snync/stargazers) - Prevent and detect if you're vulnerable to dependency confusion supply chain security attacks.

### Fuzzing

See also [Awesome-Fuzzing](https://github.com/secfigo/Awesome-Fuzzing) [![GitHub stars](https://img.shields.io/github/stars/secfigo/Awesome-Fuzzing?style=flat)](https://github.com/secfigo/Awesome-Fuzzing/stargazers).

* [Atheris](https://pypi.org/project/atheris/) - Coverage-guided Python fuzzing engine based off of libFuzzer that supports fuzzing of Python code but also native extensions written for CPython.
* [FuzzBench](https://google.github.io/fuzzbench/) - Free service that evaluates fuzzers on a wide variety of real-world benchmarks, at Google scale.
* [OneFuzz](https://github.com/microsoft/onefuzz) [![GitHub stars](https://img.shields.io/github/stars/microsoft/onefuzz?style=flat)](https://github.com/microsoft/onefuzz/stargazers) - Self-hosted Fuzzing-as-a-Service (FaaS) platform.

### Policy enforcement

- [AllStar](https://github.com/ossf/allstar) [![GitHub stars](https://img.shields.io/github/stars/ossf/allstar?style=flat)](https://github.com/ossf/allstar/stargazers) - GitHub App installed on organizations or repositories to set and enforce security policies.
- [Conftest](https://conftest.dev/) - Utility to help you write tests against structured configuration data.
- [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) - Unified toolset and framework for policy across the cloud native stack.
- [Regula](https://regula.dev/) - Checks infrastructure as code templates (Terraform, CloudFormation, K8s manifests) for AWS, Azure, Google Cloud, and Kubernetes security and compliance using Open Policy Agent/Rego.
- [Tang](https://github.com/latchset/tang) [![GitHub stars](https://img.shields.io/github/stars/latchset/tang?style=flat)](https://github.com/latchset/tang/stargazers) - Server for binding data to network presence; provides data to clients only when they are on a certain (secured) network.

### Supply chain security

See also [§ Dependency confusion](#dependency-confusion).

- [Grafeas](https://grafeas.io/) - Open artifact metadata API to audit and govern your software supply chain.
- [Helm GPG (GnuPG) Plugin](https://github.com/technosophos/helm-gpg) [![GitHub stars](https://img.shields.io/github/stars/technosophos/helm-gpg?style=flat)](https://github.com/technosophos/helm-gpg/stargazers) - Chart signing and verification with GnuPG for Helm.
- [Notary](https://github.com/theupdateframework/notary) [![GitHub stars](https://img.shields.io/github/stars/theupdateframework/notary?style=flat)](https://github.com/theupdateframework/notary/stargazers) - Aims to make the internet more secure by making it easy for people to publish and verify content.
- [in-toto](https://in-toto.io/) - Framework to secure the integrity of software supply chains.

## Honeypots

See also [awesome-honeypots](https://github.com/paralax/awesome-honeypots) [![GitHub stars](https://img.shields.io/github/stars/paralax/awesome-honeypots?style=flat)](https://github.com/paralax/awesome-honeypots/stargazers).

- [CanaryTokens](https://github.com/thinkst/canarytokens) [![GitHub stars](https://img.shields.io/github/stars/thinkst/canarytokens?style=flat)](https://github.com/thinkst/canarytokens/stargazers) - Self-hostable honeytoken generator and reporting dashboard; demo version available at [CanaryTokens.org](https://canarytokens.org/).
- [Kushtaka](https://kushtaka.org) - Sustainable all-in-one honeypot and honeytoken orchestrator for under-resourced blue teams.
- [Manuka](https://github.com/spaceraccoon/manuka) [![GitHub stars](https://img.shields.io/github/stars/spaceraccoon/manuka?style=flat)](https://github.com/spaceraccoon/manuka/stargazers) - Open-sources intelligence (OSINT) honeypot that monitors reconnaissance attempts by threat actors and generates actionable intelligence for Blue Teamers.

### Tarpits

- [Endlessh](https://github.com/skeeto/endlessh) [![GitHub stars](https://img.shields.io/github/stars/skeeto/endlessh?style=flat)](https://github.com/skeeto/endlessh/stargazers) - SSH tarpit that slowly sends an endless banner.
- [LaBrea](http://labrea.sourceforge.net/labrea-info.html) - Program that answers ARP requests for unused IP space, creating the appearance of fake machines that answer further requests very slowly in order to slow down scanners, worms, etcetera.

## Host-based tools

- [Artillery](https://github.com/BinaryDefense/artillery) [![GitHub stars](https://img.shields.io/github/stars/BinaryDefense/artillery?style=flat)](https://github.com/BinaryDefense/artillery/stargazers) - Combination honeypot, filesystem monitor, and alerting system designed to protect Linux and Windows operating systems.
- [Crowd Inspect](https://www.crowdstrike.com/resources/community-tools/crowdinspect-tool/) - Free tool for Windows systems aimed to alert you to the presence of malware that may be communicating over the network.
- [Fail2ban](https://www.fail2ban.org/) - Intrusion prevention software framework that protects computer servers from brute-force attacks.
- [Open Source HIDS SECurity (OSSEC)](https://www.ossec.net/) - Fully open source and free, feature-rich, Host-based Instrusion Detection System (HIDS).
- [Rootkit Hunter (rkhunter)](http://rkhunter.sourceforge.net/) - POSIX-compliant Bash script that scans a host for various signs of malware.
- [Shufflecake](https://shufflecake.net/) - Plausible deniability for multiple hidden filesystems on Linux.
- [USB Keystroke Injection Protection](https://github.com/google/ukip) [![GitHub stars](https://img.shields.io/github/stars/google/ukip?style=flat)](https://github.com/google/ukip/stargazers) - Daemon for blocking USB keystroke injection devices on Linux systems.
- [chkrootkit](http://chkrootkit.org/) - Locally checks for signs of a rootkit on GNU/Linux systems.

### Sandboxes

- [Bubblewrap](https://github.com/containers/bubblewrap) [![GitHub stars](https://img.shields.io/github/stars/containers/bubblewrap?style=flat)](https://github.com/containers/bubblewrap/stargazers) - Sandboxing tool for use by unprivileged Linux users capable of restricting access to parts of the operating system or user data.
- [Dangerzone](https://dangerzone.rocks/) - Take potentially dangerous PDFs, office documents, or images and convert them to a safe PDF.
- [Firejail](https://firejail.wordpress.com/) - SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf.

## Identity and AuthN/AuthZ

- [Gluu Server](https://gluu.org/) - Central authentication and authorization for Web and mobile applications with a Free and Open Source Software cloud-native community distribution.

## Incident Response tools

See also [awesome-incident-response](https://github.com/meirwah/awesome-incident-response) [![GitHub stars](https://img.shields.io/github/stars/meirwah/awesome-incident-response?style=flat)](https://github.com/meirwah/awesome-incident-response/stargazers).

- [LogonTracer](https://github.com/JPCERTCC/LogonTracer) [![GitHub stars](https://img.shields.io/github/stars/JPCERTCC/LogonTracer?style=flat)](https://github.com/JPCERTCC/LogonTracer/stargazers) - Investigate malicious Windows logon by visualizing and analyzing Windows event log.
- [Volatility](https://www.volatilityfoundation.org/) - Advanced memory forensics framework.
- [aws_ir](https://github.com/ThreatResponse/aws_ir) [![GitHub stars](https://img.shields.io/github/stars/ThreatResponse/aws_ir?style=flat)](https://github.com/ThreatResponse/aws_ir/stargazers) - Automates your incident response with zero security preparedness assumptions.

### IR management consoles

See also [Security Orchestration, Automation, and Response (SOAR)](#security-orchestration-automation-and-response-soar).

- [CIRTKit](https://github.com/opensourcesec/CIRTKit) [![GitHub stars](https://img.shields.io/github/stars/opensourcesec/CIRTKit?style=flat)](https://github.com/opensourcesec/CIRTKit/stargazers) - Scriptable Digital Forensics and Incident Response (DFIR) toolkit built on Viper.
- [Fast Incident Response (FIR)](https://github.com/certsocietegenerale/FIR) [![GitHub stars](https://img.shields.io/github/stars/certsocietegenerale/FIR?style=flat)](https://github.com/certsocietegenerale/FIR/stargazers) - Cybersecurity incident management platform allowing for easy creation, tracking, and reporting of cybersecurity incidents.
- [Rekall](http://www.rekall-forensic.com/) - Advanced forensic and incident response framework.
- [TheHive](https://thehive-project.org/) - Scalable, free Security Incident Response Platform designed to make life easier for SOCs, CSIRTs, and CERTs, featuring tight integration with MISP.
- [threat_note](https://github.com/defpoint/threat_note) [![GitHub stars](https://img.shields.io/github/stars/defpoint/threat_note?style=flat)](https://github.com/defpoint/threat_note/stargazers) - Web application built by Defense Point Security to allow security researchers the ability to add and retrieve indicators related to their research.

### Evidence collection

- [AutoMacTC](https://github.com/CrowdStrike/automactc) [![GitHub stars](https://img.shields.io/github/stars/CrowdStrike/automactc?style=flat)](https://github.com/CrowdStrike/automactc/stargazers) - Modular, automated forensic triage collection framework designed to access various forensic artifacts on macOS, parse them, and present them in formats viable for analysis.
- [OSXAuditor](https://github.com/jipegit/OSXAuditor) [![GitHub stars](https://img.shields.io/github/stars/jipegit/OSXAuditor?style=flat)](https://github.com/jipegit/OSXAuditor/stargazers) - Free macOS computer forensics tool.
- [OSXCollector](https://github.com/Yelp/osxcollector) [![GitHub stars](https://img.shields.io/github/stars/Yelp/osxcollector?style=flat)](https://github.com/Yelp/osxcollector/stargazers) - Forensic evidence collection & analysis toolkit for macOS.
- [ir-rescue](https://github.com/diogo-fernan/ir-rescue) [![GitHub stars](https://img.shields.io/github/stars/diogo-fernan/ir-rescue?style=flat)](https://github.com/diogo-fernan/ir-rescue/stargazers) - Windows Batch script and a Unix Bash script to comprehensively collect host forensic data during incident response.
- [Margarita Shotgun](https://github.com/ThreatResponse/margaritashotgun) [![GitHub stars](https://img.shields.io/github/stars/ThreatResponse/margaritashotgun?style=flat)](https://github.com/ThreatResponse/margaritashotgun/stargazers) - Command line utility (that works with or without Amazon EC2 instances) to parallelize remote memory acquisition.
- [Untitled Goose Tool](https://github.com/cisagov/untitledgoosetool) [![GitHub stars](https://img.shields.io/github/stars/cisagov/untitledgoosetool?style=flat)](https://github.com/cisagov/untitledgoosetool/stargazers) - Assists incident response teams by exporting cloud artifacts from Azure/AzureAD/M365 environments in order to run a full investigation despite lacking in logs ingested by a SIEM.

## Network perimeter defenses

- [Gatekeeper](https://github.com/AltraMayor/gatekeeper) [![GitHub stars](https://img.shields.io/github/stars/AltraMayor/gatekeeper?style=flat)](https://github.com/AltraMayor/gatekeeper/stargazers) - First open source Distributed Denial of Service (DDoS) protection system.
- [fwknop](https://www.cipherdyne.org/fwknop/) - Protects ports via Single Packet Authorization in your firewall.
- [ssh-audit](https://github.com/jtesta/ssh-audit) [![GitHub stars](https://img.shields.io/github/stars/jtesta/ssh-audit?style=flat)](https://github.com/jtesta/ssh-audit/stargazers) - Simple tool that makes quick recommendations for improving an SSH server's security posture.

### Firewall appliances or distributions

See also [Wikipedia: List of router and firewall distributions](https://en.wikipedia.org/wiki/List_of_router_and_firewall_distributions).

- [IPFire](https://www.ipfire.org/) - Hardened GNU/Linux based router and firewall distribution forked from IPCop.
- [OPNsense](https://opnsense.org/) - Hardened FreeBSD based firewall and routing platform forked from pfSense.
- [pfSense](https://www.pfsense.org/) - FreeBSD firewall and router distribution forked from m0n0wall.

## Operating System distributions

- [Computer Aided Investigative Environment (CAINE)](https://caine-live.net/) - Italian GNU/Linux live distribution that pre-packages numerous digital forensics and evidence collection tools.
- [Security Onion](https://securityonionsolutions.com/) - Free and open source GNU/Linux distribution for intrusion detection, enterprise security monitoring, and log management.
- [Qubes OS](https://qubes-os.org/) - Desktop environment built atop the Xen hypervisor project that runs each end-user program in its own virtual machine intended to provide strict security controls to constrain the reach of any successful malware exploit.

## Phishing awareness and reporting

See also [awesome-pentest § Social Engineering Tools](https://github.com/fabacab/awesome-pentest#social-engineering-tools).

- [CertSpotter](https://github.com/SSLMate/certspotter) [![GitHub stars](https://img.shields.io/github/stars/SSLMate/certspotter?style=flat)](https://github.com/SSLMate/certspotter/stargazers) - Certificate Transparency log monitor from SSLMate that alerts you when a SSL/TLS certificate is issued for one of your domains.
- [Gophish](https://getgophish.com/) - Powerful, open-source phishing framework that makes it easy to test your organization's exposure to phishing.
- [King Phisher](https://github.com/securestate/king-phisher) [![GitHub stars](https://img.shields.io/github/stars/securestate/king-phisher?style=flat)](https://github.com/securestate/king-phisher/stargazers) - Tool for testing and promoting user awareness by simulating real world phishing attacks.
- [NotifySecurity](https://github.com/certsocietegenerale/NotifySecurity) [![GitHub stars](https://img.shields.io/github/stars/certsocietegenerale/NotifySecurity?style=flat)](https://github.com/certsocietegenerale/NotifySecurity/stargazers) - Outlook add-in used to help your users to report suspicious e-mails to security teams.
- [Phishing Intelligence Engine (PIE)](https://github.com/LogRhythm-Labs/PIE) [![GitHub stars](https://img.shields.io/github/stars/LogRhythm-Labs/PIE?style=flat)](https://github.com/LogRhythm-Labs/PIE/stargazers) - Framework that will assist with the detection and response to phishing attacks.
- [Swordphish](https://github.com/certsocietegenerale/swordphish-awareness) [![GitHub stars](https://img.shields.io/github/stars/certsocietegenerale/swordphish-awareness?style=flat)](https://github.com/certsocietegenerale/swordphish-awareness/stargazers) - Platform allowing to create and manage (fake) phishing campaigns intended to train people in identifying suspicious mails. 
- [mailspoof](https://github.com/serain/mailspoof) [![GitHub stars](https://img.shields.io/github/stars/serain/mailspoof?style=flat)](https://github.com/serain/mailspoof/stargazers) - Scans SPF and DMARC records for issues that could allow email spoofing.
- [phishing_catcher](https://github.com/x0rz/phishing_catcher) [![GitHub stars](https://img.shields.io/github/stars/x0rz/phishing_catcher?style=flat)](https://github.com/x0rz/phishing_catcher/stargazers) - Configurable script to watch for issuances of suspicious TLS certificates by domain name in the Certificate Transparency Log (CTL) using the [CertStream](https://certstream.calidog.io/) service.

## Preparedness training and wargaming

(Also known as *adversary emulation*, *threat simulation*, or similar.)

- [APTSimulator](https://github.com/NextronSystems/APTSimulator) [![GitHub stars](https://img.shields.io/github/stars/NextronSystems/APTSimulator?style=flat)](https://github.com/NextronSystems/APTSimulator/stargazers) - Toolset to make a system look as if it was the victim of an APT attack.
- [Atomic Red Team](https://atomicredteam.io/) - Library of simple, automatable tests to execute for testing security controls.
- [BadBlood](https://www.secframe.com/badblood/) - Fills a test (non-production) Windows Domain with data that enables security analysts and engineers to practice using tools to gain an understanding and prescribe to securing Active Directory.
- [Caldera](https://caldera.mitre.org/) - Scalable, automated, and extensible adversary emulation platform developed by MITRE.
- [Drool](https://www.dns-oarc.net/tools/drool) - Replay DNS traffic from packet capture files and send it to a specified server, such as for simulating DDoS attacks on the DNS and measuring normal DNS querying.
- [DumpsterFire](https://github.com/TryCatchHCF/DumpsterFire) [![GitHub stars](https://img.shields.io/github/stars/TryCatchHCF/DumpsterFire?style=flat)](https://github.com/TryCatchHCF/DumpsterFire/stargazers) - Modular, menu-driven, cross-platform tool for building repeatable, time-delayed, distributed security events for Blue Team drills and sensor/alert mapping.
- [Infection Monkey](https://www.guardicore.com/infectionmonkey/) - Open-source breach and attack simulation (BAS) platform that helps you validate existing controls and identify how attackers might exploit your current network security gaps.
- [Metta](https://github.com/uber-common/metta) [![GitHub stars](https://img.shields.io/github/stars/uber-common/metta?style=flat)](https://github.com/uber-common/metta/stargazers) - Automated information security preparedness tool to do adversarial simulation.
- [Network Flight Simulator (`flightsim`)](https://github.com/alphasoc/flightsim) [![GitHub stars](https://img.shields.io/github/stars/alphasoc/flightsim?style=flat)](https://github.com/alphasoc/flightsim/stargazers) - Utility to generate malicious network traffic and help security teams evaluate security controls and audit their network visibility.
- [RedHunt OS](https://github.com/redhuntlabs/RedHunt-OS) [![GitHub stars](https://img.shields.io/github/stars/redhuntlabs/RedHunt-OS?style=flat)](https://github.com/redhuntlabs/RedHunt-OS/stargazers) - Ubuntu-based Open Virtual Appliance (`.ova`) preconfigured with several threat emulation tools as well as a defender's toolkit.
- [Stratus Red Team](https://stratus-red-team.cloud/) - Emulate offensive attack techniques in a granular and self-contained manner against a cloud environment; think "Atomic Red Team™ for the cloud."
- [tcpreplay](https://tcpreplay.appneta.com/) - Suite of free Open Source utilities for editing and replaying previously captured network traffic originally designed to replay malicious traffic patterns to Intrusion Detection/Prevention Systems.

### Post-engagement analysis and reporting

- [RedEye](https://cisagov.github.io/RedEye/) - Analytic tool to assist both Red and Blue teams with visualizing and reporting command and control activities, replay and demonstrate attack paths, and more clearly communicate remediation recommendations to stakeholders.

## Security configurations

(Also known as *secure-by-default baselines* and *implemented best practices*.)

- [Bunkerized-nginx](https://github.com/bunkerity/bunkerized-nginx) [![GitHub stars](https://img.shields.io/github/stars/bunkerity/bunkerized-nginx?style=flat)](https://github.com/bunkerity/bunkerized-nginx/stargazers) - Docker image of an NginX configuration and scripts implementing many defensive techniques for Web sites.

## Security monitoring

- [Crossfeed](https://docs.crossfeed.cyber.dhs.gov/) - Continuously enumerates and monitors an organization’s public-facing attack surface in order to discover assets and flag potential security flaws.
- [Starbase](https://github.com/JupiterOne/starbase) [![GitHub stars](https://img.shields.io/github/stars/JupiterOne/starbase?style=flat)](https://github.com/JupiterOne/starbase/stargazers) - Collects assets and relationships from services and systems into an intuitive graph view to offer graph-based security analysis for everyone.

### Endpoint Detection and Response (EDR)

- [Wazuh](https://wazuh.com/) - Open source, multiplatform agent-based security monitoring based on a fork of OSSEC HIDS.

### Network Security Monitoring (NSM)

See also [awesome-pcaptools](https://github.com/caesar0301/awesome-pcaptools) [![GitHub stars](https://img.shields.io/github/stars/caesar0301/awesome-pcaptools?style=flat)](https://github.com/caesar0301/awesome-pcaptools/stargazers).

- [Arkime](https://github.com/arkime/arkime) [![GitHub stars](https://img.shields.io/github/stars/arkime/arkime?style=flat)](https://github.com/arkime/arkime/stargazers) - Augments your current security infrastructure to store and index network traffic in standard PCAP format, providing fast, indexed access.
- [ChopShop](https://github.com/MITRECND/chopshop) [![GitHub stars](https://img.shields.io/github/stars/MITRECND/chopshop?style=flat)](https://github.com/MITRECND/chopshop/stargazers) - Framework to aid analysts in the creation and execution of pynids-based decoders and detectors of APT tradecraft.
- [Maltrail](https://github.com/stamparm/maltrail) [![GitHub stars](https://img.shields.io/github/stars/stamparm/maltrail?style=flat)](https://github.com/stamparm/maltrail/stargazers) - Malicious network traffic detection system.
- [OwlH](https://www.owlh.net/) - Helps manage network IDS at scale by visualizing Suricata, Zeek, and Moloch life cycles.
- [Real Intelligence Threat Analysis (RITA)](https://github.com/activecm/rita) [![GitHub stars](https://img.shields.io/github/stars/activecm/rita?style=flat)](https://github.com/activecm/rita/stargazers) - Open source framework for network traffic analysis that ingests Zeek logs and detects beaconing, DNS tunneling, and more.
- [Respounder](https://github.com/codeexpress/respounder) [![GitHub stars](https://img.shields.io/github/stars/codeexpress/respounder?style=flat)](https://github.com/codeexpress/respounder/stargazers) - Detects the presence of the Responder LLMNR/NBT-NS/MDNS poisoner on a network.
- [Snort](https://snort.org/) - Widely-deployed, Free Software IPS capable of real-time packet analysis, traffic logging, and custom rule-based triggers.
- [SpoofSpotter](https://github.com/NetSPI/SpoofSpotter) [![GitHub stars](https://img.shields.io/github/stars/NetSPI/SpoofSpotter?style=flat)](https://github.com/NetSPI/SpoofSpotter/stargazers) - Catch spoofed NetBIOS Name Service (NBNS) responses and alert to an email or log file.
- [Stenographer](https://github.com/google/stenographer) [![GitHub stars](https://img.shields.io/github/stars/google/stenographer?style=flat)](https://github.com/google/stenographer/stargazers) - Full-packet-capture utility for buffering packets to disk for intrusion detection and incident response purposes.
- [Suricata](https://suricata-ids.org/) - Free, cross-platform, IDS/IPS with on- and off-line analysis modes and deep packet inspection capabilities that is also scriptable with Lua.
- [Tsunami](https://github.com/google/tsunami-security-scanner) [![GitHub stars](https://img.shields.io/github/stars/google/tsunami-security-scanner?style=flat)](https://github.com/google/tsunami-security-scanner/stargazers) - General purpose network security scanner with an extensible plugin system for detecting high severity vulnerabilities with high confidence. 
- [VAST](https://github.com/tenzir/vast) [![GitHub stars](https://img.shields.io/github/stars/tenzir/vast?style=flat)](https://github.com/tenzir/vast/stargazers) - Free and open-source network telemetry engine for data-driven security investigations.
- [Wireshark](https://www.wireshark.org) - Free and open-source packet analyzer useful for network troubleshooting or forensic netflow analysis.
- [Zeek](https://zeek.org/) - Powerful network analysis framework focused on security monitoring, formerly known as Bro.
- [netsniff-ng](http://netsniff-ng.org/) -  Free and fast GNU/Linux networking toolkit with numerous utilities such as a connection tracking tool (`flowtop`), traffic generator (`trafgen`), and autonomous system (AS) trace route utility (`astraceroute`).

### Security Information and Event Management (SIEM)

- [AlienVault OSSIM](https://www.alienvault.com/open-threat-exchange/projects) - Single-server open source SIEM platform featuring asset discovery, asset inventorying, behavioral monitoring, and event correlation, driven by AlienVault Open Threat Exchange (OTX).
- [Prelude SIEM OSS](https://www.prelude-siem.org/) - Open source, agentless SIEM with a long history and several commercial variants featuring security event collection, normalization, and alerting from arbitrary log input and numerous popular monitoring tools.

### Service and performance monitoring

See also [awesome-sysadmin#monitoring](https://github.com/n1trux/awesome-sysadmin#monitoring).

- [Icinga](https://icinga.com/) - Modular redesign of Nagios with pluggable user interfaces and an expanded set of data connectors, collectors, and reporting tools.
- [Locust](https://locust.io/) - Open source load testing tool in which you can define user behaviour with Python code and swarm your system with millions of simultaneous users.
- [Nagios](https://nagios.org) - Popular network and service monitoring solution and reporting platform.
- [OpenNMS](https://opennms.org/) - Free and feature-rich networking monitoring system supporting multiple configurations, a variety of alerting mechanisms (email, XMPP, SMS), and numerous data collection methods (SNMP, HTTP, JDBC, etc).
- [osquery](https://github.com/facebook/osquery) [![GitHub stars](https://img.shields.io/github/stars/facebook/osquery?style=flat)](https://github.com/facebook/osquery/stargazers) - Operating system instrumentation framework for macOS, Windows, and Linux, exposing the OS as a high-performance relational database that can be queried with a SQL-like syntax.
- [Zabbix](https://www.zabbix.com/) - Mature, enterprise-level platform to monitor large-scale IT environments.

### Threat hunting

(Also known as *hunt teaming* and *threat detection*.)

See also [awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) [![GitHub stars](https://img.shields.io/github/stars/0x4D31/awesome-threat-detection?style=flat)](https://github.com/0x4D31/awesome-threat-detection/stargazers).

- [CimSweep](https://github.com/PowerShellMafia/CimSweep) [![GitHub stars](https://img.shields.io/github/stars/PowerShellMafia/CimSweep?style=flat)](https://github.com/PowerShellMafia/CimSweep/stargazers) - Suite of CIM/WMI-based tools enabling remote incident response and hunting operations across all versions of Windows.
- [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI) [![GitHub stars](https://img.shields.io/github/stars/sans-blue-team/DeepBlueCLI?style=flat)](https://github.com/sans-blue-team/DeepBlueCLI/stargazers) - PowerShell module for hunt teaming via Windows Event logs.
- [GRR Rapid Response](https://github.com/google/grr) [![GitHub stars](https://img.shields.io/github/stars/google/grr?style=flat)](https://github.com/google/grr/stargazers) - Incident response framework focused on remote live forensics consisting of a Python agent installed on assets and Python-based server infrastructure enabling analysts to quickly triage attacks and perform analysis remotely.
- [Hunting ELK (HELK)](https://github.com/Cyb3rWard0g/HELK) [![GitHub stars](https://img.shields.io/github/stars/Cyb3rWard0g/HELK?style=flat)](https://github.com/Cyb3rWard0g/HELK/stargazers) - All-in-one Free Software threat hunting stack based on Elasticsearch, Logstash, Kafka, and Kibana with various built-in integrations for analytics including Jupyter Notebook.
- [Logging Made Easy (LME)](https://www.cisa.gov/resources-tools/services/logging-made-easy) - Free and open logging and protective monitoring solution serving.
- [MozDef](https://github.com/mozilla/MozDef) [![GitHub stars](https://img.shields.io/github/stars/mozilla/MozDef?style=flat)](https://github.com/mozilla/MozDef/stargazers) - Automate the security incident handling process and facilitate the real-time activities of incident handlers.
- [PSHunt](https://github.com/Infocyte/PSHunt) [![GitHub stars](https://img.shields.io/github/stars/Infocyte/PSHunt?style=flat)](https://github.com/Infocyte/PSHunt/stargazers) - PowerShell module designed to scan remote endpoints for indicators of compromise or survey them for more comprehensive information related to state of those systems.
- [PSRecon](https://github.com/gfoss/PSRecon) [![GitHub stars](https://img.shields.io/github/stars/gfoss/PSRecon?style=flat)](https://github.com/gfoss/PSRecon/stargazers) - PSHunt-like tool for analyzing remote Windows systems that also produces a self-contained HTML report of its findings.
- [PowerForensics](https://github.com/Invoke-IR/PowerForensics) [![GitHub stars](https://img.shields.io/github/stars/Invoke-IR/PowerForensics?style=flat)](https://github.com/Invoke-IR/PowerForensics/stargazers) - All in one PowerShell-based platform to perform live hard disk forensic analysis.
- [Redline](https://www.fireeye.com/services/freeware/redline.html) - Freeware endpoint auditing and analysis tool that provides host-based investigative capabilities, offered by FireEye, Inc.
- [rastrea2r](https://github.com/rastrea2r/rastrea2r) [![GitHub stars](https://img.shields.io/github/stars/rastrea2r/rastrea2r?style=flat)](https://github.com/rastrea2r/rastrea2r/stargazers) - Multi-platform tool for triaging suspected IOCs on many endpoints simultaneously and that integrates with antivirus consoles.

## Threat intelligence

See also [awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) [![GitHub stars](https://img.shields.io/github/stars/hslatman/awesome-threat-intelligence?style=flat)](https://github.com/hslatman/awesome-threat-intelligence/stargazers).

- [AttackerKB](https://attackerkb.com/) - Free and public crowdsourced vulnerability assessment platform to help prioritize high-risk patch application and combat vulnerability fatigue.
- [DATA](https://github.com/hadojae/DATA) [![GitHub stars](https://img.shields.io/github/stars/hadojae/DATA?style=flat)](https://github.com/hadojae/DATA/stargazers) - Credential phish analysis and automation tool that can accept suspected phishing URLs directly or trigger on observed network traffic containing such a URL.
- [Forager](https://github.com/opensourcesec/Forager) [![GitHub stars](https://img.shields.io/github/stars/opensourcesec/Forager?style=flat)](https://github.com/opensourcesec/Forager/stargazers) - Multi-threaded threat intelligence gathering built with Python3 featuring simple text-based configuration and data storage for ease of use and data portability.
- [GRASSMARLIN](https://github.com/nsacyber/GRASSMARLIN) [![GitHub stars](https://img.shields.io/github/stars/nsacyber/GRASSMARLIN?style=flat)](https://github.com/nsacyber/GRASSMARLIN/stargazers) - Provides IP network situational awareness of industrial control systems (ICS) and Supervisory Control and Data Acquisition (SCADA) by passively mapping, accounting for, and reporting on your ICS/SCADA network topology and endpoints.
- [MLSec Combine](https://github.com/mlsecproject/combine) [![GitHub stars](https://img.shields.io/github/stars/mlsecproject/combine?style=flat)](https://github.com/mlsecproject/combine/stargazers) - Gather and combine multiple threat intelligence feed sources into one customizable, standardized CSV-based format.
- [Malware Information Sharing Platform and Threat Sharing (MISP)](https://misp-project.org/) - Open source software solution for collecting, storing, distributing and sharing cyber security indicators.
- [Open Source Vulnerabilities (OSV)](https://osv.dev/) - Vulnerability database and triage infrastructure for open source projects aimed at helping both open source maintainers and consumers of open source.
- [Sigma](https://github.com/Neo23x0/sigma) [![GitHub stars](https://img.shields.io/github/stars/Neo23x0/sigma?style=flat)](https://github.com/Neo23x0/sigma/stargazers) - Generic signature format for SIEM systems, offering an open signature format that allows you to describe relevant log events in a straightforward manner.
- [Threat Bus](https://github.com/tenzir/threatbus) [![GitHub stars](https://img.shields.io/github/stars/tenzir/threatbus?style=flat)](https://github.com/tenzir/threatbus/stargazers) - Threat intelligence dissemination layer to connect security tools through a distributed publish/subscribe message broker.
- [ThreatIngestor](https://github.com/InQuest/ThreatIngestor) [![GitHub stars](https://img.shields.io/github/stars/InQuest/ThreatIngestor?style=flat)](https://github.com/InQuest/ThreatIngestor/stargazers) - Extendable tool to extract and aggregate IOCs from threat feeds including Twitter, RSS feeds, or other sources.
- [Unfetter](https://nsacyber.github.io/unfetter/) - Identifies defensive gaps in security posture by leveraging Mitre's ATT&CK framework.
- [Viper](https://github.com/viper-framework/viper) [![GitHub stars](https://img.shields.io/github/stars/viper-framework/viper?style=flat)](https://github.com/viper-framework/viper/stargazers) - Binary analysis and management framework enabling easy organization of malware and exploit samples.
- [YARA](https://github.com/VirusTotal/yara) [![GitHub stars](https://img.shields.io/github/stars/VirusTotal/yara?style=flat)](https://github.com/VirusTotal/yara/stargazers) - Tool aimed at (but not limited to) helping malware researchers to identify and classify malware samples, described as "the pattern matching swiss army knife" for file patterns and signatures.

### Fingerprinting

- [HASSH](https://github.com/salesforce/hassh) [![GitHub stars](https://img.shields.io/github/stars/salesforce/hassh?style=flat)](https://github.com/salesforce/hassh/stargazers) - Network fingerprinting standard which can be used to identify specific client and server SSH implementations.
- [JA3](https://ja3er.com/) - Extracts SSL/TLS handshake settings for fingerprinting and communicating about a given TLS implementation.

### Threat signature packages and collections

- [ESET's Malware IoCs](https://github.com/eset/malware-ioc) [![GitHub stars](https://img.shields.io/github/stars/eset/malware-ioc?style=flat)](https://github.com/eset/malware-ioc/stargazers) - Indicators of Compromises (IOCs) derived from ESET's various investigations.
- [FireEye's Red Team Tool Countermeasures](https://github.com/fireeye/red_team_tool_countermeasures) [![GitHub stars](https://img.shields.io/github/stars/fireeye/red_team_tool_countermeasures?style=flat)](https://github.com/fireeye/red_team_tool_countermeasures/stargazers) - Collection of Snort and YARA rules to detect attacks carried out with FireEye's own Red Team tools, first released after FireEye disclosed a breach in December 2020.
- [FireEye's Sunburst Countermeasures](https://github.com/fireeye/sunburst_countermeasures) [![GitHub stars](https://img.shields.io/github/stars/fireeye/sunburst_countermeasures?style=flat)](https://github.com/fireeye/sunburst_countermeasures/stargazers) - Collection of IoC in various languages for detecting backdoored SolarWinds Orion NMS activities and related vulnerabilities.
- [YARA Rules](https://github.com/Yara-Rules/rules) [![GitHub stars](https://img.shields.io/github/stars/Yara-Rules/rules?style=flat)](https://github.com/Yara-Rules/rules/stargazers) - Project covering the need for IT security researchers to have a single repository where different Yara signatures are compiled, classified and kept as up to date as possible.

## Tor Onion service defenses

See also [awesome-tor](https://github.com/ajvb/awesome-tor) [![GitHub stars](https://img.shields.io/github/stars/ajvb/awesome-tor?style=flat)](https://github.com/ajvb/awesome-tor/stargazers).

- [OnionBalance](https://onionbalance.readthedocs.io/) - Provides load-balancing while also making Onion services more resilient and reliable by eliminating single points-of-failure.
- [Vanguards](https://github.com/mikeperry-tor/vanguards) [![GitHub stars](https://img.shields.io/github/stars/mikeperry-tor/vanguards?style=flat)](https://github.com/mikeperry-tor/vanguards/stargazers) - Version 3 Onion service guard discovery attack mitigation script (intended for eventual inclusion in Tor core).

## Transport-layer defenses

- [Certbot](https://certbot.eff.org/) - Free tool to automate the issuance and renewal of TLS certificates from the [LetsEncrypt Root CA](https://letsencrypt.org/) with plugins that configure various Web and e-mail server software.
- [MITMEngine](https://github.com/cloudflare/mitmengine) [![GitHub stars](https://img.shields.io/github/stars/cloudflare/mitmengine?style=flat)](https://github.com/cloudflare/mitmengine/stargazers) - Golang library for server-side detection of TLS interception events.
- [Tor](https://torproject.org/) - Censorship circumvention and anonymizing overlay network providing distributed, cryptographically verified name services (`.onion` domains) to enhance publisher privacy and service availability.

### Overlay and Virtual Private Networks (VPNs)

- [Firezone](https://www.firezone.dev/) - Self-hosted VPN server built on WireGuard that supports MFA and SSO.
- [Headscale](https://github.com/juanfont/headscale) [![GitHub stars](https://img.shields.io/github/stars/juanfont/headscale?style=flat)](https://github.com/juanfont/headscale/stargazers) - Open source, self-hosted implementation of the Tailscale control server.
- [IPsec VPN Server Auto Setup Scripts](https://github.com/hwdsl2/setup-ipsec-vpn) [![GitHub stars](https://img.shields.io/github/stars/hwdsl2/setup-ipsec-vpn?style=flat)](https://github.com/hwdsl2/setup-ipsec-vpn/stargazers) - Scripts to build your own IPsec VPN server, with IPsec/L2TP, Cisco IPsec and IKEv2.
- [Innernet](https://github.com/tonarino/innernet) [![GitHub stars](https://img.shields.io/github/stars/tonarino/innernet?style=flat)](https://github.com/tonarino/innernet/stargazers) - Free Software private network system that uses WireGuard under the hood, made to be self-hosted.
- [Nebula](https://github.com/slackhq/nebula) [![GitHub stars](https://img.shields.io/github/stars/slackhq/nebula?style=flat)](https://github.com/slackhq/nebula/stargazers) - Completely open source and self-hosted, scalable overlay networking tool with a focus on performance, simplicity, and security, inspired by tinc.
- [OpenVPN](https://openvpn.net/) - Longstanding Free Software traditional SSL/TLS-based virtual private network.
- [OpenZITI](https://openziti.github.io/) - Open source initiative focused on bringing Zero Trust to any application via an overlay network, tunelling applications, and numerous SDKs.
- [Tailscale](https://tailscale.com/) - Managed freemium mesh VPN service built on top of WireGuard.
- [WireGuard](https://www.wireguard.com/) - Extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.
- [tinc](https://tinc-vpn.org/) - Free Software mesh VPN implemented entirely in userspace that supports expandable network space, bridged ethernet segments, and more.

## macOS-based defenses

See also [drduh/macOS-Security-and-Privacy-Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide) [![GitHub stars](https://img.shields.io/github/stars/drduh/macOS-Security-and-Privacy-Guide?style=flat)](https://github.com/drduh/macOS-Security-and-Privacy-Guide/stargazers).

- [BlockBlock](https://objective-see.com/products/blockblock.html) - Monitors common persistence locations and alerts whenever a persistent component is added, which helps to detect and prevent malware installation.
- [LuLu](https://objective-see.com/products/lulu.html) - Free macOS firewall.
- [Santa](https://github.com/google/santa) [![GitHub stars](https://img.shields.io/github/stars/google/santa?style=flat)](https://github.com/google/santa/stargazers) - Keep track of binaries that are naughty or nice in an allow/deny-listing system for macOS.
- [Stronghold](https://github.com/alichtman/stronghold) [![GitHub stars](https://img.shields.io/github/stars/alichtman/stronghold?style=flat)](https://github.com/alichtman/stronghold/stargazers) - Easily configure macOS security settings from the terminal.
- [macOS Fortress](https://github.com/essandess/macOS-Fortress) [![GitHub stars](https://img.shields.io/github/stars/essandess/macOS-Fortress?style=flat)](https://github.com/essandess/macOS-Fortress/stargazers) - Automated configuration of kernel-level, OS-level, and client-level security features including privatizing proxying and anti-virus scanning for macOS.

## Windows-based defenses

See also [awesome-windows#security](https://github.com/Awesome-Windows/Awesome#security) and [awesome-windows-domain-hardening](https://github.com/PaulSec/awesome-windows-domain-hardening) [![GitHub stars](https://img.shields.io/github/stars/PaulSec/awesome-windows-domain-hardening?style=flat)](https://github.com/PaulSec/awesome-windows-domain-hardening/stargazers).

- [CobaltStrikeScan](https://github.com/Apr4h/CobaltStrikeScan) [![GitHub stars](https://img.shields.io/github/stars/Apr4h/CobaltStrikeScan?style=flat)](https://github.com/Apr4h/CobaltStrikeScan/stargazers) - Scan files or process memory for Cobalt Strike beacons and parse their configuration.
- [HardenTools](https://github.com/securitywithoutborders/hardentools) [![GitHub stars](https://img.shields.io/github/stars/securitywithoutborders/hardentools?style=flat)](https://github.com/securitywithoutborders/hardentools/stargazers) - Utility that disables a number of risky Windows features.
- [NotRuler](https://github.com/sensepost/notruler) [![GitHub stars](https://img.shields.io/github/stars/sensepost/notruler?style=flat)](https://github.com/sensepost/notruler/stargazers) - Detect both client-side rules and VBScript enabled forms used by the [Ruler](https://github.com/sensepost/ruler) [![GitHub stars](https://img.shields.io/github/stars/sensepost/ruler?style=flat)](https://github.com/sensepost/ruler/stargazers) attack tool when attempting to compromise a Microsoft Exchange server.
- [Sandboxie](https://www.sandboxie.com/) - Free and open source general purpose Windows application sandboxing utility.
- [Sigcheck](https://docs.microsoft.com/en-us/sysinternals/downloads/sigcheck) - Audit a Windows host's root certificate store against Microsoft's [Certificate Trust List (CTL)](https://docs.microsoft.com/en-us/windows/desktop/SecCrypto/certificate-trust-list-overview).
- [Sticky Keys Slayer](https://github.com/linuz/Sticky-Keys-Slayer) [![GitHub stars](https://img.shields.io/github/stars/linuz/Sticky-Keys-Slayer?style=flat)](https://github.com/linuz/Sticky-Keys-Slayer/stargazers) - Establishes a Windows RDP session from a list of hostnames and scans for accessibility tools backdoors, alerting if one is discovered.
- [Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline) [![GitHub stars](https://img.shields.io/github/stars/nsacyber/Windows-Secure-Host-Baseline?style=flat)](https://github.com/nsacyber/Windows-Secure-Host-Baseline/stargazers) - Group Policy objects, compliance checks, and configuration tools that provide an automated and flexible approach for securely deploying and maintaining the latest releases of Windows 10.
- [WMI Monitor](https://github.com/realparisi/WMI_Monitor) [![GitHub stars](https://img.shields.io/github/stars/realparisi/WMI_Monitor?style=flat)](https://github.com/realparisi/WMI_Monitor/stargazers) - Log newly created WMI consumers and processes to the Windows Application event log.

### Active Directory

- [Active Directory Control Paths](https://github.com/ANSSI-FR/AD-control-paths) [![GitHub stars](https://img.shields.io/github/stars/ANSSI-FR/AD-control-paths?style=flat)](https://github.com/ANSSI-FR/AD-control-paths/stargazers) - Visualize and graph Active Directory permission configs ("control relations") to audit questions such as "Who can read the CEO's email?" and similar.
- [PingCastle](https://www.pingcastle.com/) - Active Directory vulnerability detection and reporting tool.
- [PlumHound](https://github.com/PlumHound/PlumHound) [![GitHub stars](https://img.shields.io/github/stars/PlumHound/PlumHound?style=flat)](https://github.com/PlumHound/PlumHound/stargazers) - More effectively use BloodHoundAD in continual security life-cycles by utilizing its pathfinding engine to identify Active Directory security vulnerabilities.

## License

[![CC-BY](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
