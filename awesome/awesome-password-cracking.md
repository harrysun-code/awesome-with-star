# Password Cracking

[![GitHub stars](https://img.shields.io/github/stars/n0kovo/awesome-password-cracking?style=flat)](https://github.com/n0kovo/awesome-password-cracking/stargazers)

# Awesome Password Cracking  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

In cryptanalysis and computer security, password cracking is the process of recovering passwords from data that has been stored in or transmitted by a computer system in scrambled form. A common approach ([brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack)) is to repeatedly try guesses for the password and to check them against an available cryptographic hash of the password.

This is a curated list of awesome tools, research, papers and other projects related to password cracking and password security by [@n0kovo@infosec.exchange](https://infosec.exchange/@n0kovo/?l).

Read [CONTRIBUTING.md](https://github.com/narkopolo/awesome-password-cracking/blob/main/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/narkopolo/awesome-password-cracking/blob/main/CONTRIBUTING.md?style=flat)](https://github.com/narkopolo/awesome-password-cracking/blob/main/CONTRIBUTING.md/stargazers) before contributing! In short:

- List is alphabetically sorted
- If in doubt, use [awesome-lint](https://github.com/sindresorhus/awesome-lint) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome-lint?style=flat)](https://github.com/sindresorhus/awesome-lint/stargazers)
- If you think an item shouldn't be here [open an issue](https://github.com/narkopolo/awesome-password-cracking/issues/new) [![GitHub stars](https://img.shields.io/github/stars/narkopolo/awesome-password-cracking/issues/new?style=flat)](https://github.com/narkopolo/awesome-password-cracking/issues/new/stargazers)

## Contents

- [Awesome Password Cracking  ](#awesome-password-cracking--)
  - [Contents](#contents)
  - [Books](#books)
  - [Cloud](#cloud)
  - [Conversion](#conversion)
  - [Hashcat](#hashcat)
    - [Automation](#automation)
    - [Distributed cracking](#distributed-cracking)
    - [Rules](#rules)
    - [Rule tools](#rule-tools)
    - [Web interfaces](#web-interfaces)
  - [John the Ripper](#john-the-ripper)
  - [Misc](#misc)
    - [Notable People](#notable-people)
  - [Websites](#websites)
    - [Communities](#communities)
    - [Lookup services](#lookup-services)
  - [Wordlist tools](#wordlist-tools)
    - [Analysis](#analysis)
    - [Generation/Manipulation](#generationmanipulation)
  - [Wordlists](#wordlists)
    - [Laguage specific](#laguage-specific)
    - [Other](#other)
  - [Specific file formats](#specific-file-formats)
    - [PDF](#pdf)
    - [JKS](#jks)
    - [ZIP](#zip)
  - [Machine Learning / AI](#machine-learning--ai)
  - [Research](#research)
    - [Articles and Blog Posts](#articles-and-blog-posts)
    - [Papers](#papers)
    - [Talks](#talks)

## Books

- [Hash Crack: Password Cracking Manual (v3)](https://www.amazon.com/-/en/Joshua-Picolet/dp/1793458618) - Password Cracking Manual v3 is an expanded reference guide for password recovery (cracking) methods, tools, and analysis techniques.

## Cloud

- [Cloud_crack](https://github.com/lordsaibat/Cloud_crack) [![GitHub stars](https://img.shields.io/github/stars/lordsaibat/Cloud_crack?style=flat)](https://github.com/lordsaibat/Cloud_crack/stargazers) - Crack passwords using Terraform and AWS.
- [Cloudcat](https://github.com/stormfleet/cloudcat) [![GitHub stars](https://img.shields.io/github/stars/stormfleet/cloudcat?style=flat)](https://github.com/stormfleet/cloudcat/stargazers) - A script to automate the creation of cloud infrastructure for hash cracking.
- [Cloudstomp](https://github.com/Fmstrat/cloudstomp) [![GitHub stars](https://img.shields.io/github/stars/Fmstrat/cloudstomp?style=flat)](https://github.com/Fmstrat/cloudstomp/stargazers) - Automated deployment of instances on EC2 via plugin for high CPU/GPU applications at the lowest price.
- [Cloudtopolis](https://github.com/JoelGMSec/Cloudtopolis) [![GitHub stars](https://img.shields.io/github/stars/JoelGMSec/Cloudtopolis?style=flat)](https://github.com/JoelGMSec/Cloudtopolis/stargazers) - A tool that facilitates the installation and provisioning of Hashtopolis on the Google Cloud Shell platform, quickly and completely unattended (and also, free!).
- [NPK](https://github.com/c6fc/npk) [![GitHub stars](https://img.shields.io/github/stars/c6fc/npk?style=flat)](https://github.com/c6fc/npk/stargazers) - NPK is a distributed hash-cracking platform built entirely of serverless components in AWS including Cognito, DynamoDB, and S3.
- [Penglab](https://github.com/mxrch/penglab) [![GitHub stars](https://img.shields.io/github/stars/mxrch/penglab?style=flat)](https://github.com/mxrch/penglab/stargazers) - Abuse of Google Colab for cracking hashes.
- [Rook](https://github.com/JumpsecLabs/Rook) [![GitHub stars](https://img.shields.io/github/stars/JumpsecLabs/Rook?style=flat)](https://github.com/JumpsecLabs/Rook/stargazers) - Automates the creation of AWS p3 instances for use in GPU-based password cracking.

## Conversion

- [7z2hashcat](https://github.com/philsmd/7z2hashcat) [![GitHub stars](https://img.shields.io/github/stars/philsmd/7z2hashcat?style=flat)](https://github.com/philsmd/7z2hashcat/stargazers) - Extract information from password-protected .7z archives (and .sfx files) such that you can crack these "hashes" with hashcat.
- [MacinHash](https://github.com/jmagers/MacinHash) [![GitHub stars](https://img.shields.io/github/stars/jmagers/MacinHash?style=flat)](https://github.com/jmagers/MacinHash/stargazers) - Convert macOS plist password file to hash file for password crackers.
- [NetNTLM-Hashcat](https://github.com/ins1gn1a/NetNTLM-Hashcat) [![GitHub stars](https://img.shields.io/github/stars/ins1gn1a/NetNTLM-Hashcat?style=flat)](https://github.com/ins1gn1a/NetNTLM-Hashcat/stargazers) - Converts John The Ripper/Cain format hashes (singular, or in bulk) to HashCat compatible hash format.
- [Rubeus-to-Hashcat](https://github.com/PwnDexter/Rubeus-to-Hashcat) [![GitHub stars](https://img.shields.io/github/stars/PwnDexter/Rubeus-to-Hashcat?style=flat)](https://github.com/PwnDexter/Rubeus-to-Hashcat/stargazers) - Converts / formats Rubeus kerberoasting output into hashcat readable format.
- [WINHELLO2hashcat](https://github.com/Banaanhangwagen/WINHELLO2hashcat) [![GitHub stars](https://img.shields.io/github/stars/Banaanhangwagen/WINHELLO2hashcat?style=flat)](https://github.com/Banaanhangwagen/WINHELLO2hashcat/stargazers) - With this tool one can extract the "hash" from a WINDOWS HELLO PIN. This hash can be cracked with Hashcat.
- [bitwarden2hashcat](https://github.com/0x6470/bitwarden2hashcat) [![GitHub stars](https://img.shields.io/github/stars/0x6470/bitwarden2hashcat?style=flat)](https://github.com/0x6470/bitwarden2hashcat/stargazers) - A tool that converts Bitwarden's data into a hashcat-suitable hash.
- [hc\_to\_7z](https://github.com/philsmd/hc_to_7z) [![GitHub stars](https://img.shields.io/github/stars/philsmd/hc_to_7z?style=flat)](https://github.com/philsmd/hc_to_7z/stargazers) - Convert 7-Zip hashcat hashes back to 7z archives.
- [hcxtools](https://github.com/ZerBea/hcxtools) [![GitHub stars](https://img.shields.io/github/stars/ZerBea/hcxtools?style=flat)](https://github.com/ZerBea/hcxtools/stargazers) - Portable solution for conversion of cap/pcap/pcapng (gz compressed) WiFi dump files to hashcat formats.
- [itunes_backup2hashcat](https://github.com/philsmd/itunes_backup2hashcat) [![GitHub stars](https://img.shields.io/github/stars/philsmd/itunes_backup2hashcat?style=flat)](https://github.com/philsmd/itunes_backup2hashcat/stargazers) - Extract the information needed from the Manifest.plist files to convert it to hashes compatible with hashcat. 
- [mongodb2hashcat](https://github.com/philsmd/mongodb2hashcat) [![GitHub stars](https://img.shields.io/github/stars/philsmd/mongodb2hashcat?style=flat)](https://github.com/philsmd/mongodb2hashcat/stargazers) - Extract hashes from the MongoDB database server to a hash format that hashcat accepts: -m 24100 (SCRAM-SHA-1) or -m 24200 (SCRAM-SHA-256).

## Hashcat

*[Hashcat](https://github.com/hashcat/hashcat) [![GitHub stars](https://img.shields.io/github/stars/hashcat/hashcat?style=flat)](https://github.com/hashcat/hashcat/stargazers) is the "World's fastest and most advanced password recovery utility." The following are projects directly related to Hashcat in one way or another.*

- [Autocrack](https://github.com/pry0cc/autocrack) [![GitHub stars](https://img.shields.io/github/stars/pry0cc/autocrack?style=flat)](https://github.com/pry0cc/autocrack/stargazers) - A set of client and server tools for automatically, and lightly automatically cracking hashes.
- [docker-hashcat](https://github.com/dizcza/docker-hashcat) [![GitHub stars](https://img.shields.io/github/stars/dizcza/docker-hashcat?style=flat)](https://github.com/dizcza/docker-hashcat/stargazers) - Latest hashcat docker for Ubuntu 18.04 CUDA, OpenCL, and POCL.
- [Hashcat-Stuffs](https://github.com/xfox64x/Hashcat-Stuffs) [![GitHub stars](https://img.shields.io/github/stars/xfox64x/Hashcat-Stuffs?style=flat)](https://github.com/xfox64x/Hashcat-Stuffs/stargazers) - Collection of hashcat lists and things.
- [hashcat-utils](https://github.com/hashcat/hashcat-utils/) [![GitHub stars](https://img.shields.io/github/stars/hashcat/hashcat-utils/?style=flat)](https://github.com/hashcat/hashcat-utils//stargazers) - Small utilities that are useful in advanced password cracking.
- [Hashfilter](https://github.com/bharshbarger/Hashfilter) [![GitHub stars](https://img.shields.io/github/stars/bharshbarger/Hashfilter?style=flat)](https://github.com/bharshbarger/Hashfilter/stargazers) - Read a hashcat potfile and parse different types into a sqlite database.
- [known_hosts-hashcat](https://github.com/chris408/known_hosts-hashcat) [![GitHub stars](https://img.shields.io/github/stars/chris408/known_hosts-hashcat?style=flat)](https://github.com/chris408/known_hosts-hashcat/stargazers) - A guide and tool for cracking ssh known_hosts files with hashcat.
- [pyhashcat](https://github.com/f0cker/pyhashcat) [![GitHub stars](https://img.shields.io/github/stars/f0cker/pyhashcat?style=flat)](https://github.com/f0cker/pyhashcat/stargazers) - Python C API binding to libhashcat.

### Automation

- [autocrack](https://github.com/timbo05sec/autocrack) [![GitHub stars](https://img.shields.io/github/stars/timbo05sec/autocrack?style=flat)](https://github.com/timbo05sec/autocrack/stargazers) - Hashcat wrapper to help automate the cracking process.
- [hat](https://github.com/sp00ks-git/hat) [![GitHub stars](https://img.shields.io/github/stars/sp00ks-git/hat?style=flat)](https://github.com/sp00ks-git/hat/stargazers) - An Automated Hashcat Tool for common wordlists and rules to speed up the process of cracking hashes during engagements.
- [hate_crack](https://github.com/trustedsec/hate_crack) [![GitHub stars](https://img.shields.io/github/stars/trustedsec/hate_crack?style=flat)](https://github.com/trustedsec/hate_crack/stargazers) - A tool for automating cracking methodologies through Hashcat from the TrustedSec team.
- [Naive hashcat](https://github.com/brannondorsey/naive-hashcat) [![GitHub stars](https://img.shields.io/github/stars/brannondorsey/naive-hashcat?style=flat)](https://github.com/brannondorsey/naive-hashcat/stargazers) - Naive hashcat is a plug-and-play script that is pre-configured with naive, emperically-tested, "good enough" parameters/attack types.

### Distributed cracking

- [CrackLord](https://github.com/jmmcatee/cracklord) [![GitHub stars](https://img.shields.io/github/stars/jmmcatee/cracklord?style=flat)](https://github.com/jmmcatee/cracklord/stargazers) - Queue and resource system for cracking passwords.
- [fitcrack](https://github.com/nesfit/fitcrack) [![GitHub stars](https://img.shields.io/github/stars/nesfit/fitcrack?style=flat)](https://github.com/nesfit/fitcrack/stargazers) - A hashcat-based distributed password cracking system.
- [Hashstation](https://github.com/hashstation/hashstation) [![GitHub stars](https://img.shields.io/github/stars/hashstation/hashstation?style=flat)](https://github.com/hashstation/hashstation/stargazers) - Hashstation is a BOINC-based distributed password cracking system with a built-in web interface.
- [Hashtopolis](https://github.com/hashtopolis/server) [![GitHub stars](https://img.shields.io/github/stars/hashtopolis/server?style=flat)](https://github.com/hashtopolis/server/stargazers) - A multi-platform client-server tool for distributing hashcat tasks to multiple computers.
- [Kraken](https://github.com/arcaneiceman/kraken) [![GitHub stars](https://img.shields.io/github/stars/arcaneiceman/kraken?style=flat)](https://github.com/arcaneiceman/kraken/stargazers) - A multi-platform distributed brute-force password cracking system.

### Rules

- [clem9669 rules](https://github.com/clem9669/hashcat-rule) [![GitHub stars](https://img.shields.io/github/stars/clem9669/hashcat-rule?style=flat)](https://github.com/clem9669/hashcat-rule/stargazers) - Rule for hashcat or john.
- [hashcat rules collection](https://github.com/narkopolo/hashcat-rules-collection) [![GitHub stars](https://img.shields.io/github/stars/narkopolo/hashcat-rules-collection?style=flat)](https://github.com/narkopolo/hashcat-rules-collection/stargazers) - Probably the largest collection of hashcat rules out there.
- [Hob0Rules](https://github.com/praetorian-inc/Hob0Rules) [![GitHub stars](https://img.shields.io/github/stars/praetorian-inc/Hob0Rules?style=flat)](https://github.com/praetorian-inc/Hob0Rules/stargazers) - Password cracking rules for Hashcat based on statistics and industry patterns.
- [Kaonashi](https://github.com/kaonashi-passwords/Kaonashi) [![GitHub stars](https://img.shields.io/github/stars/kaonashi-passwords/Kaonashi?style=flat)](https://github.com/kaonashi-passwords/Kaonashi/stargazers) - Wordlist, rules and masks from Kaonashi project (RootedCON 2019).
- [nsa-rules](https://github.com/NSAKEY/nsa-rules) [![GitHub stars](https://img.shields.io/github/stars/NSAKEY/nsa-rules?style=flat)](https://github.com/NSAKEY/nsa-rules/stargazers) - Password cracking rules and masks for hashcat generated from cracked passwords.
- [nyxgeek-rules](https://github.com/nyxgeek/nyxgeek-rules) [![GitHub stars](https://img.shields.io/github/stars/nyxgeek/nyxgeek-rules?style=flat)](https://github.com/nyxgeek/nyxgeek-rules/stargazers) - Custom password cracking rules for Hashcat and John the Ripper.
- [OneRuleToRuleThemAll](https://github.com/NotSoSecure/password_cracking_rules) [![GitHub stars](https://img.shields.io/github/stars/NotSoSecure/password_cracking_rules?style=flat)](https://github.com/NotSoSecure/password_cracking_rules/stargazers) - "One rule to crack all passwords. or atleast we hope so."
- [OneRuleToRuleThemStill](https://github.com/stealthsploit/OneRuleToRuleThemStill) [![GitHub stars](https://img.shields.io/github/stars/stealthsploit/OneRuleToRuleThemStill?style=flat)](https://github.com/stealthsploit/OneRuleToRuleThemStill/stargazers) - "A revamped and updated version of my original OneRuleToRuleThemAll hashcat rule."
- [pantagrule](https://github.com/rarecoil/pantagrule) [![GitHub stars](https://img.shields.io/github/stars/rarecoil/pantagrule?style=flat)](https://github.com/rarecoil/pantagrule/stargazers) - Large hashcat rulesets generated from real-world compromised passwords.

### Rule tools

- [duprule](https://github.com/mhasbini/duprule) [![GitHub stars](https://img.shields.io/github/stars/mhasbini/duprule?style=flat)](https://github.com/mhasbini/duprule/stargazers) - Detect & filter duplicate hashcat rules.
- [ruleprocessorY](https://github.com/TheWorkingDeveloper/ruleprocessorY) [![GitHub stars](https://img.shields.io/github/stars/TheWorkingDeveloper/ruleprocessorY?style=flat)](https://github.com/TheWorkingDeveloper/ruleprocessorY/stargazers) - A next-gen Rule processor with complex multibyte character support built to support Hashcat.

### Web interfaces

- [crackerjack](https://github.com/ctxis/crackerjack) [![GitHub stars](https://img.shields.io/github/stars/ctxis/crackerjack?style=flat)](https://github.com/ctxis/crackerjack/stargazers) - CrackerJack is a Web GUI for Hashcat developed in Python.
- [CrackQ](https://github.com/f0cker/crackq) [![GitHub stars](https://img.shields.io/github/stars/f0cker/crackq?style=flat)](https://github.com/f0cker/crackq/stargazers) - A Python Hashcat cracking queue system.
- [hashpass](https://github.com/dj-zombie/hashpass) [![GitHub stars](https://img.shields.io/github/stars/dj-zombie/hashpass?style=flat)](https://github.com/dj-zombie/hashpass/stargazers) - Hash cracking WebApp & Server for hashcat.
- [Hashview](https://github.com/hashview/hashview) [![GitHub stars](https://img.shields.io/github/stars/hashview/hashview?style=flat)](https://github.com/hashview/hashview/stargazers) - A web front-end for password cracking and analytics.
- [Wavecrack](https://github.com/wavestone-cdt/wavecrack) [![GitHub stars](https://img.shields.io/github/stars/wavestone-cdt/wavecrack?style=flat)](https://github.com/wavestone-cdt/wavecrack/stargazers) - Wavestone's web interface for password cracking with hashcat.
- [WebHashCat](https://github.com/hegusung/WebHashcat) [![GitHub stars](https://img.shields.io/github/stars/hegusung/WebHashcat?style=flat)](https://github.com/hegusung/WebHashcat/stargazers) - WebHashcat is a very simple but efficient web interface for hashcat password cracking tool.

## John the Ripper

*[John the Ripper](https://github.com/openwall/john) [![GitHub stars](https://img.shields.io/github/stars/openwall/john?style=flat)](https://github.com/openwall/john/stargazers) is "an Open Source password security auditing and password recovery tool available for many operating systems." The following are projects directly related to John the Ripper in one way or another.*

- [BitCracker](https://github.com/e-ago/bitcracker) [![GitHub stars](https://img.shields.io/github/stars/e-ago/bitcracker?style=flat)](https://github.com/e-ago/bitcracker/stargazers) - BitCracker is the first open source password cracking tool for memory units encrypted with BitLocker.
- [johnny](https://github.com/openwall/johnny) [![GitHub stars](https://img.shields.io/github/stars/openwall/johnny?style=flat)](https://github.com/openwall/johnny/stargazers) - GUI frontend to John the Ripper.

## Misc

- [Hashes](https://github.com/zefr0x/hashes) [![GitHub stars](https://img.shields.io/github/stars/zefr0x/hashes?style=flat)](https://github.com/zefr0x/hashes/stargazers) - Identify hashing algorithms (GUI frontend for Name That Hash).
- [hashgen](https://github.com/cyclone-github/hashgen) [![GitHub stars](https://img.shields.io/github/stars/cyclone-github/hashgen?style=flat)](https://github.com/cyclone-github/hashgen/stargazers) - Hashgen is a simple yet very fast CLI hash generator written in Go and cross compiled for Linux, Windows & Mac.
- [Name That Hash](https://github.com/HashPals/Name-That-Hash) [![GitHub stars](https://img.shields.io/github/stars/HashPals/Name-That-Hash?style=flat)](https://github.com/HashPals/Name-That-Hash/stargazers) - Don't know what type of hash it is? Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other hashes. Comes with a neat web app.

### Notable People

- Alotdv - [Twitter](https://twitter.com/AlongExc).
- Clem9669 - [GitHub](https://github.com/clem9669) [![GitHub stars](https://img.shields.io/github/stars/clem9669?style=flat)](https://github.com/clem9669/stargazers).
- Coolbry95 - [GitHub](https://github.com/coolbry95) [![GitHub stars](https://img.shields.io/github/stars/coolbry95?style=flat)](https://github.com/coolbry95/stargazers) / [Twitter](https://twitter.com/coolbry95).
- Dakykilla - [GitHub](https://github.com/dakykilla) [![GitHub stars](https://img.shields.io/github/stars/dakykilla?style=flat)](https://github.com/dakykilla/stargazers) / [Twitter](https://twitter.com/dakykilla).
- Dropdeadfu - [GitHub](https://github.com/dropdeadfu) [![GitHub stars](https://img.shields.io/github/stars/dropdeadfu?style=flat)](https://github.com/dropdeadfu/stargazers) / [Twitter](https://twitter.com/dropdeadfu).
- Epixoip - [GitHub](https://github.com/epixoip) [![GitHub stars](https://img.shields.io/github/stars/epixoip?style=flat)](https://github.com/epixoip/stargazers) / [Mastodon](https://infosec.exchange/@epixoip) / [Twitter](https://twitter.com/jmgosney).
- Evilmog - [GitHub](https://github.com/evilmog/) [![GitHub stars](https://img.shields.io/github/stars/evilmog/?style=flat)](https://github.com/evilmog//stargazers) / [Mastodon](https://infosec.exchange/@evilmog) / [Twitter](https://twitter.com/Evil_Mog).
- Hydraze - [GitHub](https://github.com/Hydraze) [![GitHub stars](https://img.shields.io/github/stars/Hydraze?style=flat)](https://github.com/Hydraze/stargazers) / [Mastodon](https://infosec.exchange/@hydraze) / [Twitter](https://twitter.com/Hydraze).
- JakeWnuk - [GitHub](https://github.com/jakewnuk) [![GitHub stars](https://img.shields.io/github/stars/jakewnuk?style=flat)](https://github.com/jakewnuk/stargazers).
- Kontrast23 - [GitHub](https://github.com/kontrast23) [![GitHub stars](https://img.shields.io/github/stars/kontrast23?style=flat)](https://github.com/kontrast23/stargazers) / [Twitter](https://twitter.com/marco_preuss).
- M3g9tr0n - [GitHub](https://github.com/m3g9tr0n) [![GitHub stars](https://img.shields.io/github/stars/m3g9tr0n?style=flat)](https://github.com/m3g9tr0n/stargazers) / [Twitter](https://twitter.com/m3g9tr0n).
- Matrix - [GitHub](https://github.com/matrix) [![GitHub stars](https://img.shields.io/github/stars/matrix?style=flat)](https://github.com/matrix/stargazers) / [Twitter](https://twitter.com/gm4tr1x).
- Minga - [Twitter](https://twitter.com/mingadotcom).
- N0kovo - [GitHub](https://github.com/n0kovo) [![GitHub stars](https://img.shields.io/github/stars/n0kovo?style=flat)](https://github.com/n0kovo/stargazers) / [Mastodon](https://infosec.exchange/@n0kovo) / [Twitter](https://twitter.com/n0kovos).
- NSAKEY - [GitHub](https://github.com/NSAKEY) [![GitHub stars](https://img.shields.io/github/stars/NSAKEY?style=flat)](https://github.com/NSAKEY/stargazers) / [Twitter](https://twitter.com/_NSAKEY) / [Website](https://abigisp.com/).
- NullMode - [GitHub](https://github.com/NullMode) [![GitHub stars](https://img.shields.io/github/stars/NullMode?style=flat)](https://github.com/NullMode/stargazers) / [Mastodon](https://infosec.exchange/@nullmode_@twtr.plus) / [Twitter](https://twitter.com/nullmode_).
- Paule965 - [Twitter](https://twitter.com/paule965).
- Philsmd - [GitHub](https://github.com/philsmd) [![GitHub stars](https://img.shields.io/github/stars/philsmd?style=flat)](https://github.com/philsmd/stargazers) / [Twitter](https://twitter.com/philsmd).
- Roycewilliams - [GitHub](https://github.com/roycewilliams) [![GitHub stars](https://img.shields.io/github/stars/roycewilliams?style=flat)](https://github.com/roycewilliams/stargazers) / [Mastodon](https://infosec.exchange/@tychotithonus) / [Twitter](https://twitter.com/TychoTithonus).
- RuraPenthe - [GitHub](https://github.com/bitcrackcyber) [![GitHub stars](https://img.shields.io/github/stars/bitcrackcyber?style=flat)](https://github.com/bitcrackcyber/stargazers) / [Mastodon](https://infosec.exchange/@rurapenthe) / [Twitter](https://twitter.com/RuraPenthe0).
- S3in!c - [GitHub](https://github.com/s3inlc) [![GitHub stars](https://img.shields.io/github/stars/s3inlc?style=flat)](https://github.com/s3inlc/stargazers) / [Mastodon](https://infosec.exchange/@s3inlc) / [Twitter](https://twitter.com/s3inlc).
- Tehnlulz - [GitHub](https://github.com/tehnlulz) [![GitHub stars](https://img.shields.io/github/stars/tehnlulz?style=flat)](https://github.com/tehnlulz/stargazers) / [Twitter](https://twitter.com/tehnlulz).
- The_Mechanic - [GitHub](https://github.com/th3mechanic) [![GitHub stars](https://img.shields.io/github/stars/th3mechanic?style=flat)](https://github.com/th3mechanic/stargazers) / [Twitter](https://twitter.com/th3_m3chan1c).
- ToXiC - [Twitter](https://twitter.com/yiannistox).
- Undeath - [GitHub](https://github.com/undeath) [![GitHub stars](https://img.shields.io/github/stars/undeath?style=flat)](https://github.com/undeath/stargazers).
- Unix-ninja - [GitHub](https://github.com/unix-ninja) [![GitHub stars](https://img.shields.io/github/stars/unix-ninja?style=flat)](https://github.com/unix-ninja/stargazers) / [Mastodon](https://infosec.exchange/@unix_ninja@twitterbridge.jannis.rocks) / [Twitter](https://twitter.com/unix_ninja).
- Xan - [GitHub](https://github.com/Xanadrel) [![GitHub stars](https://img.shields.io/github/stars/Xanadrel?style=flat)](https://github.com/Xanadrel/stargazers) / [Mastodon](https://infosec.exchange/@Xanadrel) / [Twitter](https://twitter.com/Xanadrel).

## Websites

### Communities

- [hashcat Forum](https://hashcat.net/forum/) - Forum by the developers of hashcat.
- [Hashmob](https://hashmob.net/) - A growing password recovery community aimed towards being a center point of collaboration for cryptography enthusiasts. Huge wordlist collection and a lookup service too.
- [Hashkiller Forum](https://forum.hashkiller.io/) - A password cracking forum with over 20,000 registered users.

### Lookup services

- [CMD5](https://www.cmd5.org/) - Provides online MD5 / sha1/ mysql / sha256 encryption and decryption services.
- [CrackStation](https://crackstation.net/) - Free hash lookup service supplying wordlists as well.
- [gohashmob](https://github.com/n0kovo/gohashmob) [![GitHub stars](https://img.shields.io/github/stars/n0kovo/gohashmob?style=flat)](https://github.com/n0kovo/gohashmob/stargazers) - Go CLI app to quickly lookup hashes using the HashMob API.
- [Hashes.com](https://hashes.com/) - A hash lookup service with paid features.
- [Hashkiller](https://hashkiller.io/) - A hash lookup service with a forum.
- [Online Hash Crack](https://www.onlinehashcrack.com/) - Cloud password recovery service.

## Wordlist tools

*Tools for analyzing, generating and manipulating wordlists.*

### Analysis

- [PACK](https://github.com/iphelix/pack) [![GitHub stars](https://img.shields.io/github/stars/iphelix/pack?style=flat)](https://github.com/iphelix/pack/stargazers) - A collection of utilities developed to aid in analysis of password lists in order to enhance password cracking through pattern detection of masks, rules, character-sets and other password characteristics.
- [password-smelter](https://github.com/TheTechromancer/password-smelter) [![GitHub stars](https://img.shields.io/github/stars/TheTechromancer/password-smelter?style=flat)](https://github.com/TheTechromancer/password-smelter/stargazers) - Ingests passwords from hashcat, etc. and outputs to HTML, Markdown, XLSX, PNG, JSON. Dark and light themes supported. Compliments password-stretcher.
- [password-stretcher](https://github.com/thetechromancer/password-stretcher) [![GitHub stars](https://img.shields.io/github/stars/thetechromancer/password-stretcher?style=flat)](https://github.com/thetechromancer/password-stretcher/stargazers) - Generate "disgusting quantities" of passwords from websites, files, or stdin. Compliments password-smelter.
- [pcfg_cracker](https://github.com/lakiw/pcfg_cracker) [![GitHub stars](https://img.shields.io/github/stars/lakiw/pcfg_cracker?style=flat)](https://github.com/lakiw/pcfg_cracker/stargazers) - This project uses machine learning to identify password creation habits of users.
- [Pipal](https://github.com/digininja/pipal) [![GitHub stars](https://img.shields.io/github/stars/digininja/pipal?style=flat)](https://github.com/digininja/pipal/stargazers) - THE password analyser.
- [Graphcat](https://github.com/Orange-Cyberdefense/graphcat) [![GitHub stars](https://img.shields.io/github/stars/Orange-Cyberdefense/graphcat?style=flat)](https://github.com/Orange-Cyberdefense/graphcat/stargazers) - Generate graphs and charts based on password cracking result.

### Generation/Manipulation

- [accent_permutator](https://github.com/cyclone-github/accent_permutator) [![GitHub stars](https://img.shields.io/github/stars/cyclone-github/accent_permutator?style=flat)](https://github.com/cyclone-github/accent_permutator/stargazers) - A tool to transform characters from ASCII / UTF-8 to accented characters such as "o" to "ò".
- [anew](https://github.com/tomnomnom/anew) [![GitHub stars](https://img.shields.io/github/stars/tomnomnom/anew?style=flat)](https://github.com/tomnomnom/anew/stargazers) - Append lines from stdin to a file, but only if they don't already appear in the file. Outputs new lines to stdout too, making it a bit like a tee -a that removes duplicates.
- [bopscrk](https://github.com/r3nt0n/bopscrk) [![GitHub stars](https://img.shields.io/github/stars/r3nt0n/bopscrk?style=flat)](https://github.com/r3nt0n/bopscrk/stargazers) - Generate smart and powerful wordlists for targeted attacks. Includes song lyrics fetching and different transforms.
- [common-substr](https://github.com/sensepost/common-substr) [![GitHub stars](https://img.shields.io/github/stars/sensepost/common-substr?style=flat)](https://github.com/sensepost/common-substr/stargazers) - Simple tool to extract the most common substrings from an input text. Built for password cracking.
- [Crunch](https://sourceforge.net/projects/crunch-wordlist/) - Crunch is a wordlist generator where you can specify a standard character set or a character set you specify. Crunch can generate all possible combinations and permutations.
- [CUPP](https://github.com/Mebus/cupp) [![GitHub stars](https://img.shields.io/github/stars/Mebus/cupp?style=flat)](https://github.com/Mebus/cupp/stargazers) - A tool that lets you generate wordlists by user profiling data such as birthday, nickname, address, name of a pet or relative etc.
- [duplicut](https://github.com/nil0x42/duplicut) [![GitHub stars](https://img.shields.io/github/stars/nil0x42/duplicut?style=flat)](https://github.com/nil0x42/duplicut/stargazers) - Remove duplicates from MASSIVE wordlist, without sorting it (for dictionary-based password cracking).
- [Gorilla](https://github.com/d4rckh/gorilla) [![GitHub stars](https://img.shields.io/github/stars/d4rckh/gorilla?style=flat)](https://github.com/d4rckh/gorilla/stargazers) - Tool for generating wordlists or extending an existing one using mutations.
- [Gramify](https://github.com/TheWorkingDeveloper/gramify) [![GitHub stars](https://img.shields.io/github/stars/TheWorkingDeveloper/gramify?style=flat)](https://github.com/TheWorkingDeveloper/gramify/stargazers) - Create n-grams of wordlists based on words, characters, or charsets to use in offline password attacks and data analysis.
- [Elpscrk](https://github.com/D4Vinci/elpscrk) [![GitHub stars](https://img.shields.io/github/stars/D4Vinci/elpscrk?style=flat)](https://github.com/D4Vinci/elpscrk/stargazers) - Elpscrk is like cupp, but it's based on permutations and statistics while being memory efficient.
- [Keyboard-Walk-Generators](https://github.com/Rich5/Keyboard-Walk-Generators) [![GitHub stars](https://img.shields.io/github/stars/Rich5/Keyboard-Walk-Generators?style=flat)](https://github.com/Rich5/Keyboard-Walk-Generators/stargazers) - Generate Keyboard Walk Dictionaries for cracking.
- [kwprocessor](https://github.com/hashcat/kwprocessor) [![GitHub stars](https://img.shields.io/github/stars/hashcat/kwprocessor?style=flat)](https://github.com/hashcat/kwprocessor/stargazers) - Advanced keyboard-walk generator with configureable basechars, keymap and routes.
- [maskprocessor](https://github.com/hashcat/maskprocessor/) [![GitHub stars](https://img.shields.io/github/stars/hashcat/maskprocessor/?style=flat)](https://github.com/hashcat/maskprocessor//stargazers) - High-performance word generator with a per-position configureable charset.
- [maskuni](https://github.com/flbdx/maskuni) [![GitHub stars](https://img.shields.io/github/stars/flbdx/maskuni?style=flat)](https://github.com/flbdx/maskuni/stargazers) - A standalone fast word generator in the spirit of hashcat's mask generator with unicode support.
- [Mentalist](https://github.com/sc0tfree/mentalist) [![GitHub stars](https://img.shields.io/github/stars/sc0tfree/mentalist?style=flat)](https://github.com/sc0tfree/mentalist/stargazers) - Mentalist is a graphical tool for custom wordlist generation. It utilizes common human paradigms for constructing passwords and can output the full wordlist as well as rules compatible with Hashcat and John the Ripper.
- [PTT](https://github.com/JakeWnuk/ptt) [![GitHub stars](https://img.shields.io/github/stars/JakeWnuk/ptt?style=flat)](https://github.com/JakeWnuk/ptt/stargazers) - The Password Transformation Tool (ptt) is a versatile utility designed for password cracking. It facilitates the creation of custom rules and transformations, as well as the generation of wordlists. This tool supports processing data from files, URLs, and standard input, streamlining cracking workflows.
- [Phraser](https://github.com/Sparell/Phraser) [![GitHub stars](https://img.shields.io/github/stars/Sparell/Phraser?style=flat)](https://github.com/Sparell/Phraser/stargazers) - Phraser is a phrase generator using n-grams and Markov chains to generate phrases for passphrase cracking.
- [princeprocessor](https://github.com/hashcat/princeprocessor) [![GitHub stars](https://img.shields.io/github/stars/hashcat/princeprocessor?style=flat)](https://github.com/hashcat/princeprocessor/stargazers) - Standalone password candidate generator using the PRINCE algorithm.
- [Rephraser](https://github.com/travco/rephraser) [![GitHub stars](https://img.shields.io/github/stars/travco/rephraser?style=flat)](https://github.com/travco/rephraser/stargazers) - A Python-based reimagining of Phraser using Markov-chains for linguistically-correct password cracking.
- [Rling](https://github.com/Cynosureprime/rling) [![GitHub stars](https://img.shields.io/github/stars/Cynosureprime/rling?style=flat)](https://github.com/Cynosureprime/rling/stargazers) - RLI Next Gen (Rling), a faster multi-threaded, feature rich alternative to rli found in hashcat utilities.
- [statsprocessor](https://github.com/hashcat/statsprocessor/) [![GitHub stars](https://img.shields.io/github/stars/hashcat/statsprocessor/?style=flat)](https://github.com/hashcat/statsprocessor//stargazers) - Word generator based on per-position markov-chains.
- [StringZilla](https://github.com/ashvardanian/StringZilla) [![GitHub stars](https://img.shields.io/github/stars/ashvardanian/StringZilla?style=flat)](https://github.com/ashvardanian/StringZilla/stargazers) - Fastest string sort, search, split, and shuffle for long strings and multi-gigabyte files in Python and C.
- [TTPassGen](https://github.com/tp7309/TTPassGen) [![GitHub stars](https://img.shields.io/github/stars/tp7309/TTPassGen?style=flat)](https://github.com/tp7309/TTPassGen/stargazers) - Flexible and scriptable password dictionary generator which supportss brute-force, combination, complex rule modes etc.
- [token-reverser](https://github.com/dariusztytko/token-reverser) [![GitHub stars](https://img.shields.io/github/stars/dariusztytko/token-reverser?style=flat)](https://github.com/dariusztytko/token-reverser/stargazers) - Words list generator to crack security tokens.
- [WikiRaider](https://github.com/NorthwaveSecurity/wikiraider) [![GitHub stars](https://img.shields.io/github/stars/NorthwaveSecurity/wikiraider?style=flat)](https://github.com/NorthwaveSecurity/wikiraider/stargazers) - WikiRaider enables you to generate wordlists based on country specific databases of Wikipedia.

## Wordlists

### Laguage specific

- [Albanian wordlist](https://github.com/its0x08/albanian-wordlist) [![GitHub stars](https://img.shields.io/github/stars/its0x08/albanian-wordlist?style=flat)](https://github.com/its0x08/albanian-wordlist/stargazers) - A mix of names, last names and some albanian literature.
- [Danish Phone Wordlist Generator](https://github.com/narkopolo/danish_phone_wordlist_generator) [![GitHub stars](https://img.shields.io/github/stars/narkopolo/danish_phone_wordlist_generator?style=flat)](https://github.com/narkopolo/danish_phone_wordlist_generator/stargazers) - This tool can generate wordlists of Danish phone numbers by area and/or usage (Mobile, landline etc.) Useful for password cracking or fuzzing Danish targets.
- [Danish Wordlists](https://github.com/narkopolo/danish-wordlists) [![GitHub stars](https://img.shields.io/github/stars/narkopolo/danish-wordlists?style=flat)](https://github.com/narkopolo/danish-wordlists/stargazers) - Collection of danish wordlists for cracking danish passwords.
- [French Wordlists](https://github.com/clem9669/wordlists) [![GitHub stars](https://img.shields.io/github/stars/clem9669/wordlists?style=flat)](https://github.com/clem9669/wordlists/stargazers) - This project aim to provide french word list about everything a person could use as a base password.

### Other

- [Packet Storm Wordlists](https://packetstormsecurity.com/Crackers/wordlists/page1/) - A substantial collection of different wordlists in multiple languages.
- [Rocktastic](https://labs.nettitude.com/tools/rocktastic/) - Includes many permutations of passwords and patterns that have been observed in the wild.
- [RockYou2021](https://github.com/ohmybahgosh/RockYou2021.txt) [![GitHub stars](https://img.shields.io/github/stars/ohmybahgosh/RockYou2021.txt?style=flat)](https://github.com/ohmybahgosh/RockYou2021.txt/stargazers) -  RockYou2021.txt is a MASSIVE WORDLIST compiled of various other wordlists.
- [WeakPass](https://weakpass.com/) - Collection of large wordlists.

## Specific file formats

### PDF

- [pdfrip](https://github.com/mufeedvh/pdfrip) [![GitHub stars](https://img.shields.io/github/stars/mufeedvh/pdfrip?style=flat)](https://github.com/mufeedvh/pdfrip/stargazers) - A multi-threaded PDF password cracking utility equipped with commonly encountered password format builders and dictionary attacks.

### JKS

- [JKS private key cracker](https://github.com/floyd-fuh/JKS-private-key-cracker-hashcat) [![GitHub stars](https://img.shields.io/github/stars/floyd-fuh/JKS-private-key-cracker-hashcat?style=flat)](https://github.com/floyd-fuh/JKS-private-key-cracker-hashcat/stargazers) - Cracking passwords of private key entries in a JKS file.

### ZIP

- [bkcrack](https://github.com/kimci86/bkcrack) [![GitHub stars](https://img.shields.io/github/stars/kimci86/bkcrack?style=flat)](https://github.com/kimci86/bkcrack/stargazers) - Crack legacy zip encryption with Biham and Kocher's known plaintext attack.
- [frackzip](https://github.com/hyc/fcrackzip) [![GitHub stars](https://img.shields.io/github/stars/hyc/fcrackzip?style=flat)](https://github.com/hyc/fcrackzip/stargazers) - Small tool for cracking encrypted ZIP archives.

## Machine Learning / AI

- [adams](https://github.com/TheAdamProject/adams) [![GitHub stars](https://img.shields.io/github/stars/TheAdamProject/adams?style=flat)](https://github.com/TheAdamProject/adams/stargazers) - Reducing Bias in Modeling Real-world Password Strength via Deep Learning and Dynamic Dictionaries.
- [neural network cracking](https://github.com/cupslab/neural_network_cracking) [![GitHub stars](https://img.shields.io/github/stars/cupslab/neural_network_cracking?style=flat)](https://github.com/cupslab/neural_network_cracking/stargazers) - Code for cracking passwords with neural networks.
- [RNN-Passwords](https://github.com/gehaxelt/RNN-Passwords) [![GitHub stars](https://img.shields.io/github/stars/gehaxelt/RNN-Passwords?style=flat)](https://github.com/gehaxelt/RNN-Passwords/stargazers) - Using the char-rnn to learn and guess passwords.
- [rulesfinder](https://github.com/synacktiv/rulesfinder) [![GitHub stars](https://img.shields.io/github/stars/synacktiv/rulesfinder?style=flat)](https://github.com/synacktiv/rulesfinder/stargazers) - This tool finds efficient password mangling rules (for John the Ripper or Hashcat) for a given dictionary and a list of passwords.
- [PassGPT](https://github.com/javirandor/passgpt) [![GitHub stars](https://img.shields.io/github/stars/javirandor/passgpt?style=flat)](https://github.com/javirandor/passgpt/stargazers) - PassGPT is a GPT-2 model trained from scratch on password leaks.
- [SePass: Semantic Password Guessing using k-nn Similarity Search in Word Embeddings](https://github.com/Knuust/SePass) [![GitHub stars](https://img.shields.io/github/stars/Knuust/SePass?style=flat)](https://github.com/Knuust/SePass/stargazers) - A password guessing method that utilizes word embeddings to discover and exploit semantic correlations in password lists.

## Research

### Articles and Blog Posts

- [Optimizing Wordlists with Masks](https://jakewnuk.com/posts/optimizing-wordlists-w-masks/)
- [Purple Rain Attack - Password Cracking With Random Generation](https://www.netmux.com/blog/purple-rain-attack)
- [Smashing Hashes with Token Swapping Attacks](https://jakewnuk.com/posts/token-swapping-attack/)
- [Bcrypt at 25: A Retrospective on Password Security](https://www.usenix.org/publications/loginonline/bcrypt-25-retrospective-password-security)

### Papers

- [PassGPT: Password Modeling and (Guided) Generation with LLMs](https://arxiv.org/abs/2306.01545)
- [Password Cracking Using Probabilistic Context-Free Grammars (2009)](https://www.researchgate.net/publication/220713709_Password_Cracking_Using_Probabilistic_Context-Free_Grammars)
- [Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks (2016)](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/melicher)
- [PassGAN: A Deep Learning Approach for Password Guessing (2017)](https://arxiv.org/pdf/1709.00440)
- [GENPass: A General Deep Learning Model for Password Guessing with PCFG Rules and Adversarial Generation (2018)](https://ieeexplore.ieee.org/document/8422243)
- [Generating Optimized Guessing Candidates toward Better Password Cracking from Multi-Dictionaries Using Relativistic GAN (2020)](https://www.mdpi.com/2076-3417/10/20/7306/htm)
- [Reducing Bias in Modeling Real-world Password Strength via Deep Learning and Dynamic Dictionaries (2020)](https://arxiv.org/abs/2010.12269)
- [PassFlow: Guessing Passwords with Generative Flows (2021)](https://arxiv.org/abs/2105.06165)
- [GNPassGAN: Improved Generative Adversarial Networks For Trawling Offline Password Guessing (2022)](https://arxiv.org/pdf/2208.06943)
- [The Revenge of Password Crackers: Automated Training of Password Cracking Tools (2022)](https://doi.org/10.1007/978-3-031-17146-8_16)
- [A Systematic Review on Password Guessing Tasks (2023)](https://doi.org/10.3390/e25091303)
- [Harder, better, faster, stronger: Optimising the performance of context-based password cracking dictionaries (2023)](https://doi.org/10.1016/j.fsidi.2023.301507)
- [Confident Monte Carlo: Rigorous Analysis of Guessing Curves for Probabilistic Password Models (2023)](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10179365)
- [Improving Real-world Password Guessing Attacks via Bi-directional Transformers (2023)](https://www.usenix.org/conference/usenixsecurity23/presentation/xu-ming)
- [Mangling Rules Generation With Density-Based Clustering for Password Guessing (2023)](https://annas-archive.pk/scidb/10.1109/tdsc.2022.3217002/)
- [No Single Silver Bullet: Measuring the Accuracy of Password Strength Meters (2023)](https://www.usenix.org/system/files/usenixsecurity23-wang-ding-silver-bullet.pdf)
- [Optimizing The Computation Of Password Hashes (2023)](https://helda.helsinki.fi/server/api/core/bitstreams/23a37f74-a162-4473-b894-5da77f0627d1/content)
- [PGTCN: A Novel Password-Guessing Model Based On Temporal Convolution Network (2023)](https://annas-archive.pk/scidb/10.1016/j.jnca.2023.103592/)
- [Towards a Rigorous Statistical Analysis of Empirical Password Datasets (2023)](https://ieeexplore.ieee.org/document/10179431)
- [Enhancing The Resistance Of Password Hashing Using Binary Randomization Through Logical Gates (2024)](http://doi.org/10.11591/ijece.v14i5.pp5400-5407)
- [GuessFuse: Hybrid Password Guessing With Multi-View (2024)](https://ieeexplore.ieee.org/document/10466588)
- [PassRVAE: Improved Trawling Attacks via Recurrent Variational Autoencoder (2024)](https://dl.acm.org/doi/10.1145/3673277.3673295)
- [Prob-Hashcat: Accelerating Probabilistic PasswordGuessing with Hashcat by Hundreds of Times (2024)](https://dl.acm.org/doi/epdf/10.1145/3678890.3678919)
- [Reinforcing Cybersecurity With Bloom Filters: A Novel Approach To Password Cracking Efficiency (2024)](https://doi.org/10.1186/s13635-024-00183-2)
- [Beyond The Dictionary Attack: Enhancing Password Cracking Efficiency Through Machine Learning-Induced Mangling Rules (2025)](https://doi.org/10.1016/j.fsidi.2025.301865)
- [MAYA: Addressing Inconsistencies in Generative Password Guessing through a Unified Benchmark (2025)](https://arxiv.org/abs/2504.16651)
- [Password Guessing Using Large Language Models (2025)](https://www.usenix.org/system/files/usenixsecurity25-zou-yunkai.pdf)
- [PassRecover: A Multi-FPGA System for End-to-End Offline Password Recovery Acceleration (2025)](https://doi.org/10.3390/electronics14071415)
- [When Intelligence Fails: An Empirical Study on Why LLMs Struggle with Password Cracking (2025)](https://arxiv.org/abs/2510.17884)
- [Success Rates Doubled with Only One Character: Mask Password Guessing (2025)](https://doi.org/10.14722/ndss.2026.241059)
- [PGMaP: Password Generation Based On Mask Prediction (2026)](https://linkinghub.elsevier.com/retrieve/pii/S0957417426002319)
- [Improving targeted password guessing attacks by using personally identifiable information and old password (2026)](https://doi.org/10.1186/s42400-025-00430-0)

### Talks

- [BSides Cayman Islands 2024 - No Cap Cracking: Improving Offline Hash Recovery Methodologies](https://jakewnuk.com/static/No%20Cap%20Cracking%20Improving%20Offline%20Hash%20Recovery%20Methodologies.pdf)
- [BSides Cayman Islands 2023 - Leveling Up Password Attacks with Breach Data](https://jakewnuk.com/static/Leveling%20Up%20Password%20Attacks%20with%20Breach%20Data.pdf)
- [DEF CON Safe Mode Password Village - Getting Started with Hashcat](https://www.youtube.com/watch?v=MBTJ8f6Fsmg)
- [DEF CON Safe Mode Password Village - Jeremi Gosney - Cracking at Extreme Scale](https://www.youtube.com/watch?v=4Ell1Tt23NI)
- [DEF CON 28 Safe Mode Password Village – 'Let's Crack RockYou Without Using rockyou txt'](https://www.youtube.com/watch?v=8FtXntEsZdU)
- [SecTor 2019 - Will Hunt - Hashes, Hashes Everywhere, But All I See Is Plaintext](https://sector.ca/sessions/hashes-hashes-everywhere-but-all-i-see-is-plaintext/)
- [Tailored, Machine Learning-driven Password Guessing Attacks and Mitigation at DefCamp](https://www.youtube.com/watch?v=iK6ZbD6v9Gg)
- [UNHash - Methods for better password cracking](https://media.ccc.de/v/31c3_-_5966_-_en_-_saal_1_-_201412292245_-_unhash_-_methods_for_better_password_cracking_-_tonimir_kisasondi)
- [USENIX Security '23 - No Single Silver Bullet: Measuring the Accuracy of Password Strength Meters](https://www.youtube.com/watch?v=0vhoAaqGYV8)
- [USENIX Security '23 - Improving Real-World Password Guessing Attacks via Bi-Directional Transformers](https://www.youtube.com/watch?v=kE7dEUcPtU0)
- [USENIX Security '21 - Reducing Bias in Modeling Real-world Password Strength via Deep Learning and Dynamic Dictionaries](https://www.youtube.com/watch?v=Jvp3UTdCeag)
- [USENIX Security '16 - Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks](https://www.youtube.com/watch?v=GgaZ_LxsL_8)
