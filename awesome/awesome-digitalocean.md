# DigitalOcean

[![GitHub stars](https://img.shields.io/github/stars/jonleibowitz/awesome-digitalocean?style=flat)](https://github.com/jonleibowitz/awesome-digitalocean/stargazers)

# Awesome DigitalOcean [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://raw.githubusercontent.com/jonleibowitz/awesome-digitalocean/master/media/DO_Logo.png" align="right" width="100">](https://www.digitalocean.com/)

> A curated list of awesome [DigitalOcean](https://www.digitalocean.com) guides, blogs, and other resources.

DigitalOcean's tagline is it is a simple and robust cloud computing platform, designed for developers. With DigitalOcean you can easily spin up cloud compute and storage resources either indivdually or with a team. 

Contributions welcome. Add links through pull requests or create an issue to start a discussion.


## Contents

- [Community](#community)
- [Configuration management](#configuration-management)
- [Developer documentation](#developer-documentation)
- [Open source projects](#open-source-projects)
- [Commercial integrations](#commercial-integrations)
- [Community OSS projects](#community-oss-projects)
- [Clients](#clients)
- [Video tutorials](#video-tutorials)
- [Other](#other)


## Community

- [Tutorial Search and Index](https://www.digitalocean.com/community/tutorials)
- [Community articles by tag](https://www.digitalocean.com/community/tags)
- [Questions](https://www.digitalocean.com/community/questions)
- [Projects](https://www.digitalocean.com/community/projects)
- [Meetups](https://www.meetup.com/pro/digitalocean/)
- [DigitalOcean Lovers](https://www.linkedin.com/groups/8876623/) - A LinkedIn group for users and lovers of DigitalOcean.
- 

## Configuration management

- [Using Ansible with DigitalOcean](https://the.binbashtheory.com/using-ansible-with-digitalocean/)
- [Ansible Cloud Modules - DigitalOcean](https://docs.ansible.com/ansible/latest/collections/community/digitalocean/index.html#plugins-in-community-digitalocean)
- [Terraform - DigitalOcean Provider](https://www.terraform.io/docs/providers/do/)
- [DigitalOcean in Action!](https://github.com/keinohguchi/do-in-action) [![GitHub stars](https://img.shields.io/github/stars/keinohguchi/do-in-action?style=flat)](https://github.com/keinohguchi/do-in-action/stargazers) - Example repo for using DigitalOcean with Terraform and Ansible.
- [Use DigitalOcean as Dynamic DNS](https://surdu.me/2019/07/28/digital-ocean-ddns.html)

## Developer documentation

- [API](https://developers.digitalocean.com/documentation/v2/)
- [Spaces API](https://developers.digitalocean.com/documentation/spaces/)
- [OAuth](https://developers.digitalocean.com/documentation/oauth/)
- [Droplet Metadata](https://developers.digitalocean.com/documentation/metadata/)
- [Official DO Release Notes](https://www.digitalocean.com/docs/release-notes/) - Notes tracking incremental improvements and major releases for the DigitalOcean cloud platform.
- [DigitalOcean API Slugs](https://slugs.do-api.dev/)

## Open source projects

- [Open Source @ DigitalOcean](https://developers.digitalocean.com/opensource/)
- [Netbox](https://github.com/digitalocean/netbox) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/netbox?style=flat)](https://github.com/digitalocean/netbox/stargazers)
- [Doctl](https://github.com/digitalocean/doctl) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/doctl?style=flat)](https://github.com/digitalocean/doctl/stargazers) - Official command-line interface for the DigitalOcean API.
- [go-libvirt](https://github.com/digitalocean/go-libvirt) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/go-libvirt?style=flat)](https://github.com/digitalocean/go-libvirt/stargazers)
- [go-qemu](https://github.com/digitalocean/go-qemu) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/go-qemu?style=flat)](https://github.com/digitalocean/go-qemu/stargazers)

## Commercial integrations

- [Bill.do](https://bill.do) - Free DigitalOcean billing monitoring and insights tool
- [HostLaunch](https://hostlaunch.io) - Launch a hosting company based on DigitalOcean and ServerPilot.
- [SimpleBackups](https://simplebackups.io) - Tool for scheduling DigitalOcean backups (files & databases) on auto-pilot.
- [SnapShooter](https://snapshooter.io/digitalocean) - Tool for taking Daily to Hourly backups of Droplets and Volumes
- [Weap.io](https://weap.io) - Hourly to Daily DigitalOcean backups. Tool for scheduling more frequent DigitalOcean backups

## Community OSS projects

- [do-sshuttle](https://github.com/f/do-sshuttle) [![GitHub stars](https://img.shields.io/github/stars/f/do-sshuttle?style=flat)](https://github.com/f/do-sshuttle/stargazers) - Transparent Proxying via sshuttle to DigitalOcean Droplet.
- [drophosts](https://github.com/qmx/drophosts) [![GitHub stars](https://img.shields.io/github/stars/qmx/drophosts?style=flat)](https://github.com/qmx/drophosts/stargazers) - Update `/etc/hosts` with peer droplets.
- [droplan](https://github.com/tam7t/droplan) [![GitHub stars](https://img.shields.io/github/stars/tam7t/droplan?style=flat)](https://github.com/tam7t/droplan/stargazers) - Manage iptable rules for the private interface on DigitalOcean droplets.
- [foreman-digitalocean](https://github.com/theforeman/foreman-digitalocean) [![GitHub stars](https://img.shields.io/github/stars/theforeman/foreman-digitalocean?style=flat)](https://github.com/theforeman/foreman-digitalocean/stargazers) - Plugin to enable management of DigitalOcean droplets in Foreman.
- [ghost-digitalocean](https://github.com/shiva-hack/ghost-digitalocean) [![GitHub stars](https://img.shields.io/github/stars/shiva-hack/ghost-digitalocean?style=flat)](https://github.com/shiva-hack/ghost-digitalocean/stargazers) - A DigitalOcean Storage adapter for Ghost.
- [lita-digitalocean](https://github.com/jimmycuadra/lita-digitalocean) [![GitHub stars](https://img.shields.io/github/stars/jimmycuadra/lita-digitalocean?style=flat)](https://github.com/jimmycuadra/lita-digitalocean/stargazers) - Lita handler for managing DigitalOcean services.
- [hostpool](https://github.com/progrium/hostpool) [![GitHub stars](https://img.shields.io/github/stars/progrium/hostpool?style=flat)](https://github.com/progrium/hostpool/stargazers) - Worker pool manager for DigitalOcean hosts.
- [DDNS](https://github.com/skibish/ddns) [![GitHub stars](https://img.shields.io/github/stars/skibish/ddns?style=flat)](https://github.com/skibish/ddns/stargazers) - Personal DDNS client with DigitalOcean Networking DNS as backend.
- [Less Confusing Menus](https://github.com/addpipe/Less-Confusing-Digital-Ocean-Menus) [![GitHub stars](https://img.shields.io/github/stars/addpipe/Less-Confusing-Digital-Ocean-Menus?style=flat)](https://github.com/addpipe/Less-Confusing-Digital-Ocean-Menus/stargazers) - A Chrome extension that makes account menus less confusing.
- [DigitalOcean Droplet creator](https://github.com/NicholasPCole/dodc) [![GitHub stars](https://img.shields.io/github/stars/NicholasPCole/dodc?style=flat)](https://github.com/NicholasPCole/dodc/stargazers) - A dialog-based shell script to quickly create a single DigitalOcean Droplet.
- [do-upgrade-plans](https://github.com/bjornjohansen/do-upgrade-plans) [![GitHub stars](https://img.shields.io/github/stars/bjornjohansen/do-upgrade-plans?style=flat)](https://github.com/bjornjohansen/do-upgrade-plans/stargazers) - A script to upgrade your DigitalOcean Droplets to better plans with the same cost.

## Clients

- [doctl](https://github.com/digitalocean/doctl) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/doctl?style=flat)](https://github.com/digitalocean/doctl/stargazers) - Command-line tool for DigitalOcean services.
- [digitalocean-indicator](https://github.com/andrewsomething/digitalocean-indicator) [![GitHub stars](https://img.shields.io/github/stars/andrewsomething/digitalocean-indicator?style=flat)](https://github.com/andrewsomething/digitalocean-indicator/stargazers) - Debian Gnome panel client.
- [domanager](https://github.com/itohnobue/domanager) [![GitHub stars](https://img.shields.io/github/stars/itohnobue/domanager?style=flat)](https://github.com/itohnobue/domanager/stargazers) - Linux and Windows System Tray Client.
- [OceanBar](https://github.com/terhechte/OceanBar) [![GitHub stars](https://img.shields.io/github/stars/terhechte/OceanBar?style=flat)](https://github.com/terhechte/OceanBar/stargazers) - macOS menu bar client.
- [Tugboat](https://github.com/pearkes/tugboat) [![GitHub stars](https://img.shields.io/github/stars/pearkes/tugboat?style=flat)](https://github.com/pearkes/tugboat/stargazers) - Ruby command-line tool for DigitalOcean services, focusing on a more guided UX.

## Video tutorials

- [Building a Kubernetes cluster on DigitalOcean using Kubicorn](https://www.youtube.com/watch?v=XpxgSZ3dspE)

## Other

- [Reddit community](https://www.reddit.com/r/digital_ocean/)
- [`##digitalocean` on freenode](https://webchat.freenode.net/)
- [Engineering Code of Conduct](https://github.com/digitalocean/engineering-code-of-conduct) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/engineering-code-of-conduct?style=flat)](https://github.com/digitalocean/engineering-code-of-conduct/stargazers)
- [User Scripts](https://github.com/digitalocean/do_user_scripts) [![GitHub stars](https://img.shields.io/github/stars/digitalocean/do_user_scripts?style=flat)](https://github.com/digitalocean/do_user_scripts/stargazers) - User data scripts to help provision apps on a Droplet.
- [Hacktoberfest](https://hacktoberfest.digitalocean.com/) - Month-long celebration of open source software in partnership with GitHub.

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Jon Leibowitz](https://github.com/jonleibowitz) [![GitHub stars](https://img.shields.io/github/stars/jonleibowitz?style=flat)](https://github.com/jonleibowitz/stargazers) has waived all copyright and related or neighboring rights to this work.
