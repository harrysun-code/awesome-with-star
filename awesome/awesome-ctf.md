# CTF

[![GitHub stars](https://img.shields.io/github/stars/apsdehal/awesome-ctf?style=flat)](https://github.com/apsdehal/awesome-ctf/stargazers)

# Awesome CTF [![Build Status](https://travis-ci.org/apsdehal/awesome-ctf.svg?branch=master)](https://travis-ci.org/apsdehal/awesome-ctf) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of [Capture The Flag](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security) (CTF) frameworks, libraries, resources, softwares and tutorials. This list aims to help starters as well as seasoned CTF players to find everything related to CTFs at one place.

### Contributing

Please take a quick look at the [contribution guidelines](https://github.com/apsdehal/ctf-tools/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/apsdehal/ctf-tools/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/apsdehal/ctf-tools/blob/master/CONTRIBUTING.md/stargazers) first.

#### _If you know a tool that isn't present here, feel free to open a pull request._

### Why?

It takes time to build up collection of tools used in CTF and remember them all. This repo helps to keep all these scattered tools at one place.

### Contents

- [Awesome CTF](#awesome-ctf)
  - [Create](#create)
    - [Forensics](#forensics)
    - [Platforms](#platforms)
    - [Steganography](#steganography)
    - [Web](#web)
  - [Solve](#solve)
    - [Attacks](#attacks)
    - [Bruteforcers](#bruteforcers)
    - [Cryptography](#crypto)
    - [Exploits](#exploits)
    - [Forensics](#forensics-1)
    - [Networking](#networking)
    - [Reversing](#reversing)
    - [Services](#services)
    - [Steganography](#steganography-1)
    - [Web](#web-1)

- [Resources](#resources)
  - [Operating Systems](#operating-systems)
  - [Starter Packs](#starter-packs)
  - [Tutorials](#tutorials)
  - [Wargames](#wargames)
  - [Websites](#websites)
  - [Wikis](#wikis)
  - [Writeups Collections](#writeups-collections)


# Create

*Tools used for creating CTF challenges*

- [Kali Linux CTF Blueprints](https://www.packtpub.com/eu/networking-and-servers/kali-linux-ctf-blueprints) - Online book on building, testing, and customizing your own Capture the Flag challenges.


## Forensics

*Tools used for creating Forensics challenges*

- [Dnscat2](https://github.com/iagox86/dnscat2) [![GitHub stars](https://img.shields.io/github/stars/iagox86/dnscat2?style=flat)](https://github.com/iagox86/dnscat2/stargazers) - Hosts communication through DNS.
- [Kroll Artifact Parser and Extractor (KAPE)](https://learn.duffandphelps.com/kape) - Triage program.
- [Magnet AXIOM](https://www.magnetforensics.com/downloadaxiom) - Artifact-centric DFIR tool.
- [Registry Dumper](http://www.kahusecurity.com/posts/registry_dumper_find_and_dump_hidden_registry_keys.html) - Dump your registry.

## Platforms

*Projects that can be used to host a CTF*

- [CTFd](https://github.com/isislab/CTFd) [![GitHub stars](https://img.shields.io/github/stars/isislab/CTFd?style=flat)](https://github.com/isislab/CTFd/stargazers) - Platform to host jeopardy style CTFs from ISISLab, NYU Tandon.
- [echoCTF.RED](https://github.com/echoCTF/echoCTF.RED) [![GitHub stars](https://img.shields.io/github/stars/echoCTF/echoCTF.RED?style=flat)](https://github.com/echoCTF/echoCTF.RED/stargazers) - Develop, deploy and maintain your own CTF infrastructure.
- [FBCTF](https://github.com/facebook/fbctf) [![GitHub stars](https://img.shields.io/github/stars/facebook/fbctf?style=flat)](https://github.com/facebook/fbctf/stargazers) - Platform to host Capture the Flag competitions from Facebook.
- [Haaukins](https://github.com/aau-network-security/haaukins) [![GitHub stars](https://img.shields.io/github/stars/aau-network-security/haaukins?style=flat)](https://github.com/aau-network-security/haaukins/stargazers)- A Highly Accessible and Automated Virtualization Platform for Security Education.
- [HackTheArch](https://github.com/mcpa-stlouis/hack-the-arch) [![GitHub stars](https://img.shields.io/github/stars/mcpa-stlouis/hack-the-arch?style=flat)](https://github.com/mcpa-stlouis/hack-the-arch/stargazers) - CTF scoring platform.
- [Mellivora](https://github.com/Nakiami/mellivora) [![GitHub stars](https://img.shields.io/github/stars/Nakiami/mellivora?style=flat)](https://github.com/Nakiami/mellivora/stargazers) - A CTF engine written in PHP.
- [MotherFucking-CTF](https://github.com/andreafioraldi/motherfucking-ctf) [![GitHub stars](https://img.shields.io/github/stars/andreafioraldi/motherfucking-ctf?style=flat)](https://github.com/andreafioraldi/motherfucking-ctf/stargazers) - Badass lightweight plaform to host CTFs. No JS involved.
- [NightShade](https://github.com/UnrealAkama/NightShade) [![GitHub stars](https://img.shields.io/github/stars/UnrealAkama/NightShade?style=flat)](https://github.com/UnrealAkama/NightShade/stargazers) - A simple security CTF framework.
- [OpenCTF](https://github.com/easyctf/openctf) [![GitHub stars](https://img.shields.io/github/stars/easyctf/openctf?style=flat)](https://github.com/easyctf/openctf/stargazers) - CTF in a box. Minimal setup required.
- [PicoCTF](https://github.com/picoCTF/picoCTF) [![GitHub stars](https://img.shields.io/github/stars/picoCTF/picoCTF?style=flat)](https://github.com/picoCTF/picoCTF/stargazers) - The platform used to run picoCTF. A great framework to host any CTF.
- [PyChallFactory](https://github.com/pdautry/py_chall_factory) [![GitHub stars](https://img.shields.io/github/stars/pdautry/py_chall_factory?style=flat)](https://github.com/pdautry/py_chall_factory/stargazers) - Small framework to create/manage/package jeopardy CTF challenges.
- [RootTheBox](https://github.com/moloch--/RootTheBox) [![GitHub stars](https://img.shields.io/github/stars/moloch--/RootTheBox?style=flat)](https://github.com/moloch--/RootTheBox/stargazers) - A Game of Hackers (CTF Scoreboard & Game Manager).
- [Scorebot](https://github.com/legitbs/scorebot) [![GitHub stars](https://img.shields.io/github/stars/legitbs/scorebot?style=flat)](https://github.com/legitbs/scorebot/stargazers) - Platform for CTFs by Legitbs (Defcon).
- [SecGen](https://github.com/cliffe/SecGen) [![GitHub stars](https://img.shields.io/github/stars/cliffe/SecGen?style=flat)](https://github.com/cliffe/SecGen/stargazers) - Security Scenario Generator. Creates randomly vulnerable virtual machines.

## Steganography

*Tools used to create stego challenges*

Check solve section for steganography.

## Web

*Tools used for creating Web challenges*

*JavaScript Obfustcators*

- [Metasploit JavaScript Obfuscator](https://github.com/rapid7/metasploit-framework/wiki/How-to-obfuscate-JavaScript-in-Metasploit) [![GitHub stars](https://img.shields.io/github/stars/rapid7/metasploit-framework/wiki/How-to-obfuscate-JavaScript-in-Metasploit?style=flat)](https://github.com/rapid7/metasploit-framework/wiki/How-to-obfuscate-JavaScript-in-Metasploit/stargazers)
- [Uglify](https://github.com/mishoo/UglifyJS) [![GitHub stars](https://img.shields.io/github/stars/mishoo/UglifyJS?style=flat)](https://github.com/mishoo/UglifyJS/stargazers)


# Solve

*Tools used for solving CTF challenges*

## Attacks

*Tools used for performing various kinds of attacks*

- [Bettercap](https://github.com/bettercap/bettercap) [![GitHub stars](https://img.shields.io/github/stars/bettercap/bettercap?style=flat)](https://github.com/bettercap/bettercap/stargazers) - Framework to perform MITM (Man in the Middle) attacks.
- [Yersinia](https://github.com/tomac/yersinia) [![GitHub stars](https://img.shields.io/github/stars/tomac/yersinia?style=flat)](https://github.com/tomac/yersinia/stargazers) - Attack various protocols on layer 2.

## Crypto

*Tools used for solving Crypto challenges*

- [CyberChef](https://gchq.github.io/CyberChef) - Web app for analysing and decoding data.
- [FeatherDuster](https://github.com/nccgroup/featherduster) [![GitHub stars](https://img.shields.io/github/stars/nccgroup/featherduster?style=flat)](https://github.com/nccgroup/featherduster/stargazers) - An automated, modular cryptanalysis tool.
- [Hash Extender](https://github.com/iagox86/hash_extender) [![GitHub stars](https://img.shields.io/github/stars/iagox86/hash_extender?style=flat)](https://github.com/iagox86/hash_extender/stargazers) - A utility tool for performing hash length extension attacks.
- [padding-oracle-attacker](https://github.com/KishanBagaria/padding-oracle-attacker) [![GitHub stars](https://img.shields.io/github/stars/KishanBagaria/padding-oracle-attacker?style=flat)](https://github.com/KishanBagaria/padding-oracle-attacker/stargazers) - A CLI tool to execute padding oracle attacks.
- [PkCrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html) - A tool for Breaking PkZip-encryption.
- [QuipQuip](https://quipqiup.com) - An online tool for breaking substitution ciphers or vigenere ciphers (without key).
- [RSACTFTool](https://github.com/Ganapati/RsaCtfTool) [![GitHub stars](https://img.shields.io/github/stars/Ganapati/RsaCtfTool?style=flat)](https://github.com/Ganapati/RsaCtfTool/stargazers) - A tool for recovering RSA private key with various attack.
- [RSATool](https://github.com/ius/rsatool) [![GitHub stars](https://img.shields.io/github/stars/ius/rsatool?style=flat)](https://github.com/ius/rsatool/stargazers) - Generate private key with knowledge of p and q.
- [XORTool](https://github.com/hellman/xortool) [![GitHub stars](https://img.shields.io/github/stars/hellman/xortool?style=flat)](https://github.com/hellman/xortool/stargazers) - A tool to analyze multi-byte xor cipher.

## Bruteforcers

*Tools used for various kind of bruteforcing (passwords etc.)*

- [Hashcat](https://hashcat.net/hashcat/) - Password Cracker
- [Hydra](https://tools.kali.org/password-attacks/hydra) - A parallelized login cracker which supports numerous protocols to attack
- [John The Jumbo](https://github.com/magnumripper/JohnTheRipper) [![GitHub stars](https://img.shields.io/github/stars/magnumripper/JohnTheRipper?style=flat)](https://github.com/magnumripper/JohnTheRipper/stargazers) - Community enhanced version of John the Ripper.
- [John The Ripper](http://www.openwall.com/john/) - Password Cracker.
- [Nozzlr](https://github.com/intrd/nozzlr) [![GitHub stars](https://img.shields.io/github/stars/intrd/nozzlr?style=flat)](https://github.com/intrd/nozzlr/stargazers) - Nozzlr is a bruteforce framework, trully modular and script-friendly.
- [Ophcrack](http://ophcrack.sourceforge.net/) - Windows password cracker based on rainbow tables.
- [Patator](https://github.com/lanjelot/patator) [![GitHub stars](https://img.shields.io/github/stars/lanjelot/patator?style=flat)](https://github.com/lanjelot/patator/stargazers) - Patator is a multi-purpose brute-forcer, with a modular design.
- [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) - Burp Suite extension for sending large numbers of HTTP requests 

## Exploits

*Tools used for solving Exploits challenges*

- [DLLInjector](https://github.com/OpenSecurityResearch/dllinjector) [![GitHub stars](https://img.shields.io/github/stars/OpenSecurityResearch/dllinjector?style=flat)](https://github.com/OpenSecurityResearch/dllinjector/stargazers) - Inject dlls in processes.
- [libformatstr](https://github.com/hellman/libformatstr) [![GitHub stars](https://img.shields.io/github/stars/hellman/libformatstr?style=flat)](https://github.com/hellman/libformatstr/stargazers) - Simplify format string exploitation.
- [Metasploit](http://www.metasploit.com/) - Penetration testing software.
  - [Cheatsheet](https://www.comparitech.com/net-admin/metasploit-cheat-sheet/)
- [one_gadget](https://github.com/david942j/one_gadget) [![GitHub stars](https://img.shields.io/github/stars/david942j/one_gadget?style=flat)](https://github.com/david942j/one_gadget/stargazers) -  A tool to find the one gadget `execve('/bin/sh', NULL, NULL)` call.
  - `gem install one_gadget`
- [Pwntools](https://github.com/Gallopsled/pwntools) [![GitHub stars](https://img.shields.io/github/stars/Gallopsled/pwntools?style=flat)](https://github.com/Gallopsled/pwntools/stargazers) - CTF Framework for writing exploits.
- [Qira](https://github.com/BinaryAnalysisPlatform/qira) [![GitHub stars](https://img.shields.io/github/stars/BinaryAnalysisPlatform/qira?style=flat)](https://github.com/BinaryAnalysisPlatform/qira/stargazers) - QEMU Interactive Runtime Analyser.
- [ROP Gadget](https://github.com/JonathanSalwan/ROPgadget) [![GitHub stars](https://img.shields.io/github/stars/JonathanSalwan/ROPgadget?style=flat)](https://github.com/JonathanSalwan/ROPgadget/stargazers) - Framework for ROP exploitation.
- [V0lt](https://github.com/P1kachu/v0lt) [![GitHub stars](https://img.shields.io/github/stars/P1kachu/v0lt?style=flat)](https://github.com/P1kachu/v0lt/stargazers) - Security CTF Toolkit.

## Forensics

*Tools used for solving Forensics challenges*

- [Aircrack-Ng](http://www.aircrack-ng.org/) - Crack 802.11 WEP and WPA-PSK keys.
  - `apt-get install aircrack-ng`
- [Audacity](http://sourceforge.net/projects/audacity/) - Analyze sound files (mp3, m4a, whatever).
  - `apt-get install audacity`
- [Bkhive and Samdump2](http://sourceforge.net/projects/ophcrack/files/samdump2/) - Dump SYSTEM and SAM files.
  - `apt-get install samdump2 bkhive`
- [CFF Explorer](http://www.ntcore.com/exsuite.php) - PE Editor.
- [Creddump](https://github.com/moyix/creddump) [![GitHub stars](https://img.shields.io/github/stars/moyix/creddump?style=flat)](https://github.com/moyix/creddump/stargazers) - Dump windows credentials.
- [DVCS Ripper](https://github.com/kost/dvcs-ripper) [![GitHub stars](https://img.shields.io/github/stars/kost/dvcs-ripper?style=flat)](https://github.com/kost/dvcs-ripper/stargazers) - Rips web accessible (distributed) version control systems.
- [Exif Tool](http://www.sno.phy.queensu.ca/~phil/exiftool/) - Read, write and edit file metadata.
- [Extundelete](http://extundelete.sourceforge.net/) - Used for recovering lost data from mountable images.
- [Fibratus](https://github.com/rabbitstack/fibratus) [![GitHub stars](https://img.shields.io/github/stars/rabbitstack/fibratus?style=flat)](https://github.com/rabbitstack/fibratus/stargazers) - Tool for exploration and tracing of the Windows kernel.
- [Foremost](http://foremost.sourceforge.net/) - Extract particular kind of files using headers.
  - `apt-get install foremost`
- [Fsck.ext4](http://linux.die.net/man/8/fsck.ext3) - Used to fix corrupt filesystems.
- [Malzilla](http://malzilla.sourceforge.net/) - Malware hunting tool.
- [NetworkMiner](http://www.netresec.com/?page=NetworkMiner) - Network Forensic Analysis Tool.
- [PDF Streams Inflater](http://malzilla.sourceforge.net/downloads.html) - Find and extract zlib files compressed in PDF files.
- [Pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html) - Verifies the integrity of PNG and dump all of the chunk-level information in human-readable form.
  - `apt-get install pngcheck`
- [ResourcesExtract](http://www.nirsoft.net/utils/resources_extract.html) - Extract various filetypes from exes.
- [Shellbags](https://github.com/williballenthin/shellbags) [![GitHub stars](https://img.shields.io/github/stars/williballenthin/shellbags?style=flat)](https://github.com/williballenthin/shellbags/stargazers) - Investigate NT\_USER.dat files.
- [Snow](https://sbmlabs.com/notes/snow_whitespace_steganography_tool) - A Whitespace Steganography Tool.
- [USBRip](https://github.com/snovvcrash/usbrip) [![GitHub stars](https://img.shields.io/github/stars/snovvcrash/usbrip?style=flat)](https://github.com/snovvcrash/usbrip/stargazers) - Simple CLI forensics tool for tracking USB device artifacts (history of USB events) on GNU/Linux.
- [Volatility](https://github.com/volatilityfoundation/volatility) [![GitHub stars](https://img.shields.io/github/stars/volatilityfoundation/volatility?style=flat)](https://github.com/volatilityfoundation/volatility/stargazers) - To investigate memory dumps.
- [Wireshark](https://www.wireshark.org) - Used to analyze pcap or pcapng files

*Registry Viewers*
- [OfflineRegistryView](https://www.nirsoft.net/utils/offline_registry_view.html) - Simple tool for Windows that allows you to read offline Registry files from external drive and view the desired Registry key in .reg file format.
- [Registry Viewer®](https://accessdata.com/product-download/registry-viewer-2-0-0) - Used to view Windows registries.

## Networking

*Tools used for solving Networking challenges*

- [Masscan](https://github.com/robertdavidgraham/masscan) [![GitHub stars](https://img.shields.io/github/stars/robertdavidgraham/masscan?style=flat)](https://github.com/robertdavidgraham/masscan/stargazers) - Mass IP port scanner, TCP port scanner.
- [Monit](https://linoxide.com/monitoring-2/monit-linux/) - A linux tool to check a host on the network (and other non-network activities).
- [Nipe](https://github.com/GouveaHeitor/nipe) [![GitHub stars](https://img.shields.io/github/stars/GouveaHeitor/nipe?style=flat)](https://github.com/GouveaHeitor/nipe/stargazers) - Nipe is a script to make Tor Network your default gateway.
- [Nmap](https://nmap.org/) - An open source utility for network discovery and security auditing.
- [Wireshark](https://www.wireshark.org/) - Analyze the network dumps.
  - `apt-get install wireshark`
- [Zeek](https://www.zeek.org) - An open-source network security monitor.
- [Zmap](https://zmap.io/) - An open-source network scanner.

## Reversing

*Tools used for solving Reversing challenges*

- [Androguard](https://github.com/androguard/androguard) [![GitHub stars](https://img.shields.io/github/stars/androguard/androguard?style=flat)](https://github.com/androguard/androguard/stargazers) - Reverse engineer Android applications.
- [Angr](https://github.com/angr/angr) [![GitHub stars](https://img.shields.io/github/stars/angr/angr?style=flat)](https://github.com/angr/angr/stargazers) - platform-agnostic binary analysis framework.
- [Apk2Gold](https://github.com/lxdvs/apk2gold) [![GitHub stars](https://img.shields.io/github/stars/lxdvs/apk2gold?style=flat)](https://github.com/lxdvs/apk2gold/stargazers) - Yet another Android decompiler.
- [ApkTool](http://ibotpeaches.github.io/Apktool/) - Android Decompiler.
- [Barf](https://github.com/programa-stic/barf-project) [![GitHub stars](https://img.shields.io/github/stars/programa-stic/barf-project?style=flat)](https://github.com/programa-stic/barf-project/stargazers) - Binary Analysis and Reverse engineering Framework.
- [Binary Ninja](https://binary.ninja/) - Binary analysis framework.
- [BinUtils](http://www.gnu.org/software/binutils/binutils.html) - Collection of binary tools.
- [BinWalk](https://github.com/devttys0/binwalk) [![GitHub stars](https://img.shields.io/github/stars/devttys0/binwalk?style=flat)](https://github.com/devttys0/binwalk/stargazers) - Analyze, reverse engineer, and extract firmware images.
- [Boomerang](https://github.com/BoomerangDecompiler/boomerang) [![GitHub stars](https://img.shields.io/github/stars/BoomerangDecompiler/boomerang?style=flat)](https://github.com/BoomerangDecompiler/boomerang/stargazers) - Decompile x86/SPARC/PowerPC/ST-20 binaries to C.
- [ctf_import](https://github.com/docileninja/ctf_import) [![GitHub stars](https://img.shields.io/github/stars/docileninja/ctf_import?style=flat)](https://github.com/docileninja/ctf_import/stargazers) – run basic functions from stripped binaries cross platform.
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) [![GitHub stars](https://img.shields.io/github/stars/fkie-cad/cwe_checker?style=flat)](https://github.com/fkie-cad/cwe_checker/stargazers) - cwe_checker finds vulnerable patterns in binary executables.
- [demovfuscator](https://github.com/kirschju/demovfuscator) [![GitHub stars](https://img.shields.io/github/stars/kirschju/demovfuscator?style=flat)](https://github.com/kirschju/demovfuscator/stargazers) - A work-in-progress deobfuscator for movfuscated binaries.
- [Frida](https://github.com/frida/) [![GitHub stars](https://img.shields.io/github/stars/frida/?style=flat)](https://github.com/frida//stargazers) - Dynamic Code Injection.
- [GDB](https://www.gnu.org/software/gdb/) - The GNU project debugger.
- [GEF](https://github.com/hugsy/gef) [![GitHub stars](https://img.shields.io/github/stars/hugsy/gef?style=flat)](https://github.com/hugsy/gef/stargazers) - GDB plugin.
- [Ghidra](https://ghidra-sre.org/) - Open Source suite of reverse engineering tools.  Similar to IDA Pro.
- [Hopper](http://www.hopperapp.com/) - Reverse engineering tool (disassembler) for OSX and Linux.
- [IDA Pro](https://www.hex-rays.com/products/ida/) - Most used Reversing software.
- [Jadx](https://github.com/skylot/jadx) [![GitHub stars](https://img.shields.io/github/stars/skylot/jadx?style=flat)](https://github.com/skylot/jadx/stargazers) - Decompile Android files.
- [Java Decompilers](http://www.javadecompilers.com) - An online decompiler for Java and Android APKs.
- [Krakatau](https://github.com/Storyyeller/Krakatau) [![GitHub stars](https://img.shields.io/github/stars/Storyyeller/Krakatau?style=flat)](https://github.com/Storyyeller/Krakatau/stargazers) - Java decompiler and disassembler.
- [Objection](https://github.com/sensepost/objection) [![GitHub stars](https://img.shields.io/github/stars/sensepost/objection?style=flat)](https://github.com/sensepost/objection/stargazers) - Runtime Mobile Exploration.
- [PEDA](https://github.com/longld/peda) [![GitHub stars](https://img.shields.io/github/stars/longld/peda?style=flat)](https://github.com/longld/peda/stargazers) - GDB plugin (only python2.7).
- [Pin](https://software.intel.com/en-us/articles/pin-a-dynamic-binary-instrumentation-tool) - A dynamic binary instrumentaion tool by Intel.
- [PINCE](https://github.com/korcankaraokcu/PINCE) [![GitHub stars](https://img.shields.io/github/stars/korcankaraokcu/PINCE?style=flat)](https://github.com/korcankaraokcu/PINCE/stargazers) - GDB front-end/reverse engineering tool, focused on game-hacking and automation.
- [PinCTF](https://github.com/ChrisTheCoolHut/PinCTF) [![GitHub stars](https://img.shields.io/github/stars/ChrisTheCoolHut/PinCTF?style=flat)](https://github.com/ChrisTheCoolHut/PinCTF/stargazers) - A tool which uses intel pin for Side Channel Analysis.
- [Plasma](https://github.com/joelpx/plasma) [![GitHub stars](https://img.shields.io/github/stars/joelpx/plasma?style=flat)](https://github.com/joelpx/plasma/stargazers) - An interactive disassembler for x86/ARM/MIPS which can generate indented pseudo-code with colored syntax.
- [Pwndbg](https://github.com/pwndbg/pwndbg) [![GitHub stars](https://img.shields.io/github/stars/pwndbg/pwndbg?style=flat)](https://github.com/pwndbg/pwndbg/stargazers) - A GDB plugin that provides a suite of utilities to hack around GDB easily.
- [radare2](https://github.com/radare/radare2) [![GitHub stars](https://img.shields.io/github/stars/radare/radare2?style=flat)](https://github.com/radare/radare2/stargazers) - A portable reversing framework.
- [Triton](https://github.com/JonathanSalwan/Triton/) [![GitHub stars](https://img.shields.io/github/stars/JonathanSalwan/Triton/?style=flat)](https://github.com/JonathanSalwan/Triton//stargazers) - Dynamic Binary Analysis (DBA) framework.
- [Uncompyle](https://github.com/gstarnberger/uncompyle) [![GitHub stars](https://img.shields.io/github/stars/gstarnberger/uncompyle?style=flat)](https://github.com/gstarnberger/uncompyle/stargazers) - Decompile Python 2.7 binaries (.pyc).
- [WinDbg](http://www.windbg.org/) - Windows debugger distributed by Microsoft.
- [Xocopy](http://reverse.lostrealm.com/tools/xocopy.html) - Program that can copy executables with execute, but no read permission.
- [Z3](https://github.com/Z3Prover/z3) [![GitHub stars](https://img.shields.io/github/stars/Z3Prover/z3?style=flat)](https://github.com/Z3Prover/z3/stargazers) - A theorem prover from Microsoft Research.

*JavaScript Deobfuscators*

- [Detox](http://relentless-coding.org/projects/jsdetox/install) - A Javascript malware analysis tool.
- [Revelo](http://www.kahusecurity.com/posts/revelo_javascript_deobfuscator.html) - Analyze obfuscated Javascript code.

*SWF Analyzers*
- [RABCDAsm](https://github.com/CyberShadow/RABCDAsm) [![GitHub stars](https://img.shields.io/github/stars/CyberShadow/RABCDAsm?style=flat)](https://github.com/CyberShadow/RABCDAsm/stargazers) - Collection of utilities including an ActionScript 3 assembler/disassembler.
- [Swftools](http://www.swftools.org/) - Collection of utilities to work with SWF files.
- [Xxxswf](https://bitbucket.org/Alexander_Hanel/xxxswf) -  A Python script for analyzing Flash files.

## Services

*Various kind of useful services available around the internet*

- [CSWSH](http://cow.cat/cswsh.html) - Cross-Site WebSocket Hijacking Tester.
- [Request Bin](https://requestbin.com/) - Lets you inspect http requests to a particular url.

## Steganography

*Tools used for solving Steganography challenges*

- [AperiSolve](https://aperisolve.fr/) - Aperi'Solve is a platform which performs layer analysis on image (open-source).
- [Convert](http://www.imagemagick.org/script/convert.php) - Convert images b/w formats and apply filters.
- [Exif](http://manpages.ubuntu.com/manpages/trusty/man1/exif.1.html) - Shows EXIF information in JPEG files.
- [Exiftool](https://linux.die.net/man/1/exiftool) - Read and write meta information in files.
- [Exiv2](http://www.exiv2.org/manpage.html) - Image metadata manipulation tool.
- [Image Steganography](https://sourceforge.net/projects/image-steg/) - Embeds text and files in images with optional encryption. Easy-to-use UI.
- [Image Steganography Online](https://incoherency.co.uk/image-steganography) - This is a client-side Javascript tool to steganographically hide images inside the lower "bits" of other images
- [ImageMagick](http://www.imagemagick.org/script/index.php) - Tool for manipulating images.
- [Outguess](https://www.freebsd.org/cgi/man.cgi?query=outguess+&apropos=0&sektion=0&manpath=FreeBSD+Ports+5.1-RELEASE&format=html) - Universal steganographic tool.
- [Pngtools](https://packages.debian.org/sid/pngtools) - For various analysis related to PNGs.
  - `apt-get install pngtools`
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) [![GitHub stars](https://img.shields.io/github/stars/Y-Vladimir/SmartDeblur?style=flat)](https://github.com/Y-Vladimir/SmartDeblur/stargazers) - Used to deblur and fix defocused images.
- [Steganabara](https://www.openhub.net/p/steganabara) -  Tool for stegano analysis written in Java.
- [SteganographyOnline](https://stylesuxx.github.io/steganography/) - Online steganography encoder and decoder.
- [Stegbreak](https://linux.die.net/man/1/stegbreak) - Launches brute-force dictionary attacks on JPG image.
- [StegCracker](https://github.com/Paradoxis/StegCracker) [![GitHub stars](https://img.shields.io/github/stars/Paradoxis/StegCracker?style=flat)](https://github.com/Paradoxis/StegCracker/stargazers) - Steganography brute-force utility to uncover hidden data inside files.
- [stegextract](https://github.com/evyatarmeged/stegextract) [![GitHub stars](https://img.shields.io/github/stars/evyatarmeged/stegextract?style=flat)](https://github.com/evyatarmeged/stegextract/stargazers) - Detect hidden files and text in images.
- [Steghide](http://steghide.sourceforge.net/) - Hide data in various kind of images.
- [StegOnline](https://georgeom.net/StegOnline/upload) - Conduct a wide range of image steganography operations, such as concealing/revealing files hidden within bits (open-source).
- [Stegsolve](http://www.caesum.com/handbook/Stegsolve.jar) - Apply various steganography techniques to images.
- [Zsteg](https://github.com/zed-0xff/zsteg/) [![GitHub stars](https://img.shields.io/github/stars/zed-0xff/zsteg/?style=flat)](https://github.com/zed-0xff/zsteg//stargazers) - PNG/BMP analysis.

## Web

*Tools used for solving Web challenges*

- [BurpSuite](https://portswigger.net/burp) - A graphical tool to testing website security.
- [Commix](https://github.com/commixproject/commix) [![GitHub stars](https://img.shields.io/github/stars/commixproject/commix?style=flat)](https://github.com/commixproject/commix/stargazers) - Automated All-in-One OS Command Injection and Exploitation Tool.
- [Hackbar](https://addons.mozilla.org/en-US/firefox/addon/hackbartool/) - Firefox addon for easy web exploitation.
- [OWASP ZAP](https://www.owasp.org/index.php/Projects/OWASP_Zed_Attack_Proxy_Project) - Intercepting proxy to replay, debug, and fuzz HTTP requests and responses
- [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) - Add on for chrome for debugging network requests.
- [Raccoon](https://github.com/evyatarmeged/Raccoon) [![GitHub stars](https://img.shields.io/github/stars/evyatarmeged/Raccoon?style=flat)](https://github.com/evyatarmeged/Raccoon/stargazers) - A high performance offensive security tool for reconnaissance and vulnerability scanning.
- [SQLMap](https://github.com/sqlmapproject/sqlmap) [![GitHub stars](https://img.shields.io/github/stars/sqlmapproject/sqlmap?style=flat)](https://github.com/sqlmapproject/sqlmap/stargazers) - Automatic SQL injection and database takeover tool.
  ```pip install sqlmap```
- [W3af](https://github.com/andresriancho/w3af) [![GitHub stars](https://img.shields.io/github/stars/andresriancho/w3af?style=flat)](https://github.com/andresriancho/w3af/stargazers) -  Web Application Attack and Audit Framework.
- [XSSer](http://xsser.sourceforge.net/) - Automated XSS testor.


# Resources

*Where to discover about CTF*

## Operating Systems

*Penetration testing and security lab Operating Systems*

- [Android Tamer](https://androidtamer.com/) - Based on Debian.
- [BackBox](https://backbox.org/) - Based on Ubuntu.
- [BlackArch Linux](https://blackarch.org/) - Based on Arch Linux.
- [Fedora Security Lab](https://labs.fedoraproject.org/security/) - Based on Fedora.
- [Kali Linux](https://www.kali.org/) - Based on Debian.
- [Parrot Security OS](https://www.parrotsec.org/) - Based on Debian.
- [Pentoo](http://www.pentoo.ch/) - Based on Gentoo.
- [URIX OS](http://urix.us/) - Based on openSUSE.
- [Wifislax](http://www.wifislax.com/) - Based on Slackware.

*Malware analysts and reverse-engineering*

- [Flare VM](https://github.com/fireeye/flare-vm/) [![GitHub stars](https://img.shields.io/github/stars/fireeye/flare-vm/?style=flat)](https://github.com/fireeye/flare-vm//stargazers) - Based on Windows.
- [REMnux](https://remnux.org/) - Based on Debian.

## Starter Packs

*Collections of installer scripts, useful tools*

- [CTF Tools](https://github.com/zardus/ctf-tools) [![GitHub stars](https://img.shields.io/github/stars/zardus/ctf-tools?style=flat)](https://github.com/zardus/ctf-tools/stargazers) - Collection of setup scripts to install various security research tools.
- [LazyKali](https://github.com/jlevitsk/lazykali) [![GitHub stars](https://img.shields.io/github/stars/jlevitsk/lazykali?style=flat)](https://github.com/jlevitsk/lazykali/stargazers) - A 2016 refresh of LazyKali which simplifies install of tools and configuration.

## Tutorials

*Tutorials to learn how to play CTFs*

- [CTF Field Guide](https://trailofbits.github.io/ctf/) - Field Guide by Trails of Bits.
- [CTF Resources](http://ctfs.github.io/resources/) -  Start Guide maintained by community.
- [How to Get Started in CTF](https://www.endgame.com/blog/how-get-started-ctf) - Short guideline for CTF beginners by Endgame
- [Intro. to CTF Course](https://www.hoppersroppers.org/courseCTF.html) - A free course that teaches beginners the basics of forensics, crypto, and web-ex.
- [IppSec](https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA) - Video tutorials and walkthroughs of popular CTF platforms.
- [LiveOverFlow](https://www.youtube.com/channel/UClcE-kVhqyiHCcjYwcpfj9w) - Video tutorials on Exploitation.
- [MIPT CTF](https://github.com/xairy/mipt-ctf) [![GitHub stars](https://img.shields.io/github/stars/xairy/mipt-ctf?style=flat)](https://github.com/xairy/mipt-ctf/stargazers) - A small course for beginners in CTFs (in Russian).


## Wargames

*Always online CTFs*

- [Backdoor](https://backdoor.sdslabs.co/) - Security Platform by SDSLabs.
- [Crackmes](https://crackmes.one/) - Reverse Engineering Challenges.
- [CryptoHack](https://cryptohack.org/) - Fun cryptography challenges.
- [echoCTF.RED](https://echoctf.red/) - Online CTF with a variety of targets to attack.
- [Exploit Exercises](https://exploit-exercises.lains.space/) - Variety of VMs to learn variety of computer security issues.
- [Exploit.Education](http://exploit.education) - Variety of VMs to learn variety of computer security issues.
- [Gracker](https://github.com/Samuirai/gracker) [![GitHub stars](https://img.shields.io/github/stars/Samuirai/gracker?style=flat)](https://github.com/Samuirai/gracker/stargazers) - Binary challenges having a slow learning curve, and write-ups for each level.
- [Hack The Box](https://www.hackthebox.eu) - Weekly CTFs for all types of security enthusiasts.
- [Hack This Site](https://www.hackthissite.org/) - Training ground for hackers.
- [Hacker101](https://www.hacker101.com/) - CTF from HackerOne
- [Hacking-Lab](https://hacking-lab.com/) - Ethical hacking, computer network and security challenge platform.
- [Hone Your Ninja Skills](https://honeyourskills.ninja/) - Web challenges starting from basic ones.
- [IO](http://io.netgarage.org/) - Wargame for binary challenges.
- [Microcorruption](https://microcorruption.com) - Embedded security CTF.
- [Over The Wire](http://overthewire.org/wargames/) - Wargame maintained by OvertheWire Community.
- [PentesterLab](https://pentesterlab.com/) - Variety of VM and online challenges (paid).
- [PicoCTF](https://2019game.picoctf.com) - All year round ctf game. Questions from the yearly picoCTF competition.
- [PWN Challenge](http://pwn.eonew.cn/) - Binary Exploitation Wargame.
- [Pwnable.kr](http://pwnable.kr/) - Pwn Game.
- [Pwnable.tw](https://pwnable.tw/) - Binary wargame.
- [Pwnable.xyz](https://pwnable.xyz/) - Binary Exploitation Wargame.
- [Reversin.kr](http://reversing.kr/) - Reversing challenge.
- [Ringzer0Team](https://ringzer0team.com/) - Ringzer0 Team Online CTF.
- [Root-Me](https://www.root-me.org/) - Hacking and Information Security learning platform.
- [ROP Wargames](https://github.com/xelenonz/game) [![GitHub stars](https://img.shields.io/github/stars/xelenonz/game?style=flat)](https://github.com/xelenonz/game/stargazers) - ROP Wargames.
- [SANS HHC](https://holidayhackchallenge.com/past-challenges/) - Challenges with a holiday theme
  released annually and maintained by SANS.
- [SmashTheStack](http://smashthestack.org/) - A variety of wargames maintained by the SmashTheStack Community.
- [Viblo CTF](https://ctf.viblo.asia) - Various amazing CTF challenges, in many different categories. Has both Practice mode and Contest mode.
- [VulnHub](https://www.vulnhub.com/) - VM-based for practical in digital security, computer application & network administration.
- [W3Challs](https://w3challs.com) - A penetration testing training platform, which offers various computer challenges, in various categories.
- [WebHacking](http://webhacking.kr) - Hacking challenges for web.


*Self-hosted CTFs*
- [Damn Vulnerable Web Application](http://www.dvwa.co.uk/) - PHP/MySQL web application that is damn vulnerable.
- [Juice Shop CTF](https://github.com/bkimminich/juice-shop-ctf) [![GitHub stars](https://img.shields.io/github/stars/bkimminich/juice-shop-ctf?style=flat)](https://github.com/bkimminich/juice-shop-ctf/stargazers) - Scripts and tools for hosting a CTF on [OWASP Juice Shop](https://www.owasp.org/index.php/OWASP_Juice_Shop_Project) easily.

## Websites

*Various general websites about and on CTF*

- [Awesome CTF Cheatsheet](https://github.com/uppusaikiran/awesome-ctf-cheatsheet#awesome-ctf-cheatsheet-) - CTF Cheatsheet.
- [CTF Time](https://ctftime.org/) - General information on CTF occuring around the worlds.
- [Reddit Security CTF](http://www.reddit.com/r/securityctf) - Reddit CTF category.

## Wikis

*Various Wikis available for learning about CTFs*

- [Bamboofox](https://bamboofox.github.io/) - Chinese resources to learn CTF.
- [bi0s Wiki](https://teambi0s.gitlab.io/bi0s-wiki/) - Wiki from team bi0s.
- [CTF Cheatsheet](https://uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/) - CTF tips and tricks.
- [ISIS Lab](https://github.com/isislab/Project-Ideas/wiki) [![GitHub stars](https://img.shields.io/github/stars/isislab/Project-Ideas/wiki?style=flat)](https://github.com/isislab/Project-Ideas/wiki/stargazers) - CTF Wiki by Isis lab.
- [OpenToAll](https://github.com/OpenToAllCTF/Tips) [![GitHub stars](https://img.shields.io/github/stars/OpenToAllCTF/Tips?style=flat)](https://github.com/OpenToAllCTF/Tips/stargazers) - CTF tips by OTA CTF team members.

## Writeups Collections

*Collections of CTF write-ups*

- [0e85dc6eaf](https://github.com/0e85dc6eaf/CTF-Writeups) [![GitHub stars](https://img.shields.io/github/stars/0e85dc6eaf/CTF-Writeups?style=flat)](https://github.com/0e85dc6eaf/CTF-Writeups/stargazers) - Write-ups for CTF challenges by 0e85dc6eaf
- [Captf](http://captf.com/) - Dumped CTF challenges and materials by psifertex.
- [CTF write-ups (community)](https://github.com/ctfs/) [![GitHub stars](https://img.shields.io/github/stars/ctfs/?style=flat)](https://github.com/ctfs//stargazers) - CTF challenges + write-ups archive maintained by the community.
- [CTFTime Scrapper](https://github.com/abdilahrf/CTFWriteupScrapper) [![GitHub stars](https://img.shields.io/github/stars/abdilahrf/CTFWriteupScrapper?style=flat)](https://github.com/abdilahrf/CTFWriteupScrapper/stargazers) - Scraps all writeup from CTF Time and organize which to read first.
- [HackThisSite](https://github.com/HackThisSite/CTF-Writeups) [![GitHub stars](https://img.shields.io/github/stars/HackThisSite/CTF-Writeups?style=flat)](https://github.com/HackThisSite/CTF-Writeups/stargazers) - CTF write-ups repo maintained by HackThisSite team.
- [Mzfr](https://github.com/mzfr/ctf-writeups/) [![GitHub stars](https://img.shields.io/github/stars/mzfr/ctf-writeups/?style=flat)](https://github.com/mzfr/ctf-writeups//stargazers) - CTF competition write-ups by mzfr
- [pwntools writeups](https://github.com/Gallopsled/pwntools-write-ups) [![GitHub stars](https://img.shields.io/github/stars/Gallopsled/pwntools-write-ups?style=flat)](https://github.com/Gallopsled/pwntools-write-ups/stargazers) - A collection of CTF write-ups all using pwntools.
- [SababaSec](https://github.com/SababaSec/ctf-writeups) [![GitHub stars](https://img.shields.io/github/stars/SababaSec/ctf-writeups?style=flat)](https://github.com/SababaSec/ctf-writeups/stargazers) - A collection of CTF write-ups by the SababaSec team
- [Shell Storm](http://shell-storm.org/repo/CTF/) - CTF challenge archive maintained by Jonathan Salwan.
- [Smoke Leet Everyday](https://github.com/smokeleeteveryday/CTF_WRITEUPS) [![GitHub stars](https://img.shields.io/github/stars/smokeleeteveryday/CTF_WRITEUPS?style=flat)](https://github.com/smokeleeteveryday/CTF_WRITEUPS/stargazers) - CTF write-ups repo maintained by SmokeLeetEveryday team.

### LICENSE

CC0 :)
