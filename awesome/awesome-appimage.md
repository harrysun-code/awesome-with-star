# AppImage

[![GitHub stars](https://img.shields.io/github/stars/AppImageCommunity/awesome-appimage?style=flat)](https://github.com/AppImageCommunity/awesome-appimage/stargazers)

<!--lint disable double-link-->

<div align="center">
	<div>
		<img width="500" src="media/logo.svg" alt="Awesome AppImage">
	</div>
	<a href="https://awesome.re">
		<!img src="https://awesome.re/badge-flat2.svg" alt="Awesome">
	</a>
	<p>
		<sub>Lovingly crafted AppImage tools and resources. Follow me on <a href="https://twitter.com/probonopd">Twitter</a>.</sub>
	</p>
	<br>
</div>

# Awesome AppImage [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[AppImage](https://appimage.org) is a community-based format to distribute applications to various mainstream Linux distributions without the need for a centralized store. One app = one file! This list contains tools to work with AppImages, such as to create AppImages for applications and to integrate AppImages into the system easily. As the vibrant community around AppImage is growing, so is this list.

## Contents

- [AppImage discovery](#appimage-discovery)
	- [App catalogs](#app-catalogs)
	- [App stores](#app-stores)
	- [App centers](#app-centers)
	- [App scrapers](#app-scrapers)
- [AppImage consumption tools](#appimage-consumption-tools)
	- [Desktop integration](#desktop-integration)
	- [Updaters](#updaters)
	- [Sandboxes](#sandboxes)
	- [Package managers](#package-managers)
	- [Linux distributions](#linux-distributions)
- [AppImage developer tools](#appimage-developer-tools)
	- [Low-level tools](#low-level-tools)
	- [Build systems](#build-systems)
	- [Deployment tools for compiled applications](#deployment-tools-for-compiled-applications)
	- [Deployment tools for Python applications](#deployment-tools-for-python-applications)
	- [Deployment tools for Electron applications](#deployment-tools-for-electron-applications)
	- [Deployment tools for Windows applications](#deployment-tools-for-windows-applications)
	- [Deployment tools for Java applications](#deployment-tools-for-java-applications)
	- [Deployment tools for .NET Core (Mono) applications](#deployment-tools-for-net-core-mono-applications)
	- [Deployment tools for Flash applications](#deployment-tools-for-flash-applications)
	- [Deployment tools for Rust applications](#deployment-tools-for-rust-applications)
	- [Tools to convert from other package formats](#tools-to-convert-from-other-package-formats)
	- [Metadata tools](#metadata-tools)
	- [QC tools](#qc-tools)
	- [Continuous integration](#continuous-integration)
	- [Libraries](#libraries)
	- [Templates](#templates)
- [Resources](#resources)
	- [Specs](#specs)
	- [Documentation](#documentation)
	- [Tutorials](#tutorials)
	- [Articles](#articles)
	- [Videos](#videos)
	- [Books](#books)
	- [Blogs](#blogs)
	- [Courses](#courses)
	- [Community](#community)
	- [Miscellaneous](#miscellaneous)
	- [Related](#related)
	- [Other awesome lists](#other-awesome-lists)
	- [Expired links](#expired-links)

## AppImage discovery

### App catalogs

- [AppImage.GitHub.io](https://appimage.github.io/) - Catalog of AppImages that passed an automated test, links to upstream download pages.

### App stores

- [AppImageHub.com](https://www.appimagehub.com/) - Downloadable AppImages, powered by [Opendesktop.org](https://www.opendesktop.org/).
- [pling.com](https://www.pling.com/) - Open store where creators can publish their libre products and creative content including AppImages.
- [Manjaro Software Discover](https://software.manjaro.org/appimages) - Web-based app store that contains applications in multiple formats, including AppImage.

### App centers

- [NX Software Center](https://github.com/Nitrux/nx-software-center) [![GitHub stars](https://img.shields.io/github/stars/Nitrux/nx-software-center?style=flat)](https://github.com/Nitrux/nx-software-center/stargazers) - Portable Software Center for portable AppImage applications.
- [AppImagePool](https://github.com/prateekmedia/appimagepool) [![GitHub stars](https://img.shields.io/github/stars/prateekmedia/appimagepool?style=flat)](https://github.com/prateekmedia/appimagepool/stargazers) - Simple, modern AppImageHub Client, powered by flutter.

### App scrapers

- [appimages.scraper](https://github.com/azubieta/appimages.scraper) [![GitHub stars](https://img.shields.io/github/stars/azubieta/appimages.scraper?style=flat)](https://github.com/azubieta/appimages.scraper/stargazers) - Search for AppImage releases over the web.
- [AppImageRadar](https://github.com/AppImage/AppImageRadar) [![GitHub stars](https://img.shields.io/github/stars/AppImage/AppImageRadar?style=flat)](https://github.com/AppImage/AppImageRadar/stargazers) - Search for AppImage-related activity on GitHub using Travis CI.

## AppImage consumption tools

### Desktop integration

- [Getting Started Managing Software with AppImage on Ubuntu](https://adamtheautomator.com/appimage-ubuntu/) - Verbosely explains how to manage AppImages without the need for further software.
- [go-appimaged](https://github.com/probonopd/go-appimage/tree/master/src/appimaged) [![GitHub stars](https://img.shields.io/github/stars/probonopd/go-appimage/tree/master/src/appimaged?style=flat)](https://github.com/probonopd/go-appimage/tree/master/src/appimaged/stargazers) - Optional daemon that integrates AppImages into the system (experimental).
- [appimaged](https://github.com/AppImage/appimaged) [![GitHub stars](https://img.shields.io/github/stars/AppImage/appimaged?style=flat)](https://github.com/AppImage/appimaged/stargazers) - Optional daemon that integrates AppImages into the system (deprecated).
- [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher) [![GitHub stars](https://img.shields.io/github/stars/TheAssassin/AppImageLauncher?style=flat)](https://github.com/TheAssassin/AppImageLauncher/stargazers) - Integrates into users' systems and establishes a single `~/Applications` directory, assisting the user to move AppImages into there, with support for updating and removing AppImages through apps launcher.
- [appimagehelper](https://gitlab.com/posktomten/appimagehelper) - Program for creating, deleting, controlling and organizing shortcuts to AppImage.
- [LinuxPA](https://github.com/CalebQ42/LinuxPA) [![GitHub stars](https://img.shields.io/github/stars/CalebQ42/LinuxPA?style=flat)](https://github.com/CalebQ42/LinuxPA/stargazers) - PortableApps.com type launcher for Linux with AppImage support.
- [AppImage Desktop Maker](https://github.com/Alexsussa/AIDM) [![GitHub stars](https://img.shields.io/github/stars/Alexsussa/AIDM?style=flat)](https://github.com/Alexsussa/AIDM/stargazers) - Creates menu entries for AppImages without the need for a daemon.
- [Thumbnailer for AppImages](https://github.com/mttbernardini/appimage-thumbnailer) [![GitHub stars](https://img.shields.io/github/stars/mttbernardini/appimage-thumbnailer?style=flat)](https://github.com/mttbernardini/appimage-thumbnailer/stargazers) - Generates icons for AppImages that are shown in file managers of GNOME and KDE compatible desktop environments.
- [XApp Thumbnailers](https://github.com/linuxmint/xapp-thumbnailers) [![GitHub stars](https://img.shields.io/github/stars/linuxmint/xapp-thumbnailers?style=flat)](https://github.com/linuxmint/xapp-thumbnailers/stargazers) - Thumbnailers for GTK Desktop Environments, including one for the AppImage file format. Makes Gtk based file managers like Caja (MATE), Nautilus (GNOME), Nemo (Cinnamon), PCManFM (LXDE), and Thunar (Xfce) show application icons on AppImages.
- [AppImage To Gnome](https://github.com/DejfCold/ATG) [![GitHub stars](https://img.shields.io/github/stars/DejfCold/ATG?style=flat)](https://github.com/DejfCold/ATG/stargazers) - Monitors and (de)installs AppImages from the Gnome desktop.
- [gnome_appimage_installer](https://github.com/knork-fork/gnome_appimage_installer) [![GitHub stars](https://img.shields.io/github/stars/knork-fork/gnome_appimage_installer?style=flat)](https://github.com/knork-fork/gnome_appimage_installer/stargazers) - Somewhat a misnomer (AppImages don't need to be "installed"), creates a desktop file that follows the freedesktop.org spec for your AppImage files; written in bash.
- [Gear lever](https://github.com/mijorus/gearlever/) [![GitHub stars](https://img.shields.io/github/stars/mijorus/gearlever/?style=flat)](https://github.com/mijorus/gearlever//stargazers) - Integrates AppImages into the Gnome desktop by drag-and-drop onto the Gear lever application.

### Updaters

- [AppImageUpdate](https://github.com/AppImage/AppImageUpdate) [![GitHub stars](https://img.shields.io/github/stars/AppImage/AppImageUpdate?style=flat)](https://github.com/AppImage/AppImageUpdate/stargazers) - Official grapical application to update AppImages; command-line tool to update AppImages.
- [AppImageUpdater](https://github.com/antony-jr/AppImageUpdater) [![GitHub stars](https://img.shields.io/github/stars/antony-jr/AppImageUpdater?style=flat)](https://github.com/antony-jr/AppImageUpdater/stargazers) - Simple updater for humans written in C++ and Qt.
- [appimage-update](https://github.com/AppImageCrafters/appimage-update) [![GitHub stars](https://img.shields.io/github/stars/AppImageCrafters/appimage-update?style=flat)](https://github.com/AppImageCrafters/appimage-update/stargazers) - AppImage Update implementation written in Go.
- [appimage-updater](https://pypi.org/project/appimage-updater/) - AppImage Update implementation written in Python, distributed on PyPi.

### Sandboxes

- [Firejail](https://github.com/netblue30/firejail) [![GitHub stars](https://img.shields.io/github/stars/netblue30/firejail?style=flat)](https://github.com/netblue30/firejail/stargazers) - Optional sandbox with support for AppImage built in.
- [AppImage Sandboxing Project](https://github.com/mgord9518/aisap) [![GitHub stars](https://img.shields.io/github/stars/mgord9518/aisap?style=flat)](https://github.com/mgord9518/aisap/stargazers) - Golang library to help sandbox AppImages with bwrap.

### Package managers

__Note:__ The AppImage format is explicitly designed _not to need any package managers_ or similar tools. Everything can be done in the file manager (and an optional daemon for system integration).

- [appimage-manager](https://github.com/AppImageCrafters/appimage-manager) [![GitHub stars](https://img.shields.io/github/stars/AppImageCrafters/appimage-manager?style=flat)](https://github.com/AppImageCrafters/appimage-manager/stargazers) - Command-line tool for managing AppImages allowing to search, install, remove and update applications.
- [bauh](https://github.com/vinifmor/bauh) [![GitHub stars](https://img.shields.io/github/stars/vinifmor/bauh?style=flat)](https://github.com/vinifmor/bauh/stargazers) - Graphical user interface for managing Linux applications supporting AppImage, Arch (repositories/AUR), Flatpak, Snap and native Web applications.
- [homebrew-appimage](https://github.com/athrunsun/homebrew-appimage) [![GitHub stars](https://img.shields.io/github/stars/athrunsun/homebrew-appimage?style=flat)](https://github.com/athrunsun/homebrew-appimage/stargazers) - Linuxbrew AppImage Formulae.
- [AIPM](https://github.com/michaeldelago/aipm) [![GitHub stars](https://img.shields.io/github/stars/michaeldelago/aipm?style=flat)](https://github.com/michaeldelago/aipm/stargazers) - A Package Manager for AppImages.
- [Zap](https://github.com/srevinsaju/zap) [![GitHub stars](https://img.shields.io/github/stars/srevinsaju/zap?style=flat)](https://github.com/srevinsaju/zap/stargazers) - AppImage package manager. Downloads the AppImage if it does not exist. If it already exists, updates it with AppImageUpdate. Integrates AppImage into the system.
- [RookiePM](https://github.com/18fadly-anthony/rookie) [![GitHub stars](https://img.shields.io/github/stars/18fadly-anthony/rookie?style=flat)](https://github.com/18fadly-anthony/rookie/stargazers) - Package manager for AppImages and Shell Scripts.
- [AppMan](https://github.com/ivan-hc/AppMan) [![GitHub stars](https://img.shields.io/github/stars/ivan-hc/AppMan?style=flat)](https://github.com/ivan-hc/AppMan/stargazers) - AppImage Manager that works like APT or Pacman.
- [jewelrystore](https://rubygems.org/gems/jewelrystore) - Command line AppImage store made in ruby.
- [ayy](https://github.com/lawl/ayy) [![GitHub stars](https://img.shields.io/github/stars/lawl/ayy?style=flat)](https://github.com/lawl/ayy/stargazers) - Package manager for AppImage. Single, static, dependency free binary. Written in Go.
- [leap](https://github.com/lnxcz/leap) [![GitHub stars](https://img.shields.io/github/stars/lnxcz/leap?style=flat)](https://github.com/lnxcz/leap/stargazers) - Fast and simple AppImage manager. Written in Rust.
- [Bread](https://github.com/pegvin/bread) [![GitHub stars](https://img.shields.io/github/stars/pegvin/bread?style=flat)](https://github.com/pegvin/bread/stargazers) - Download, update, remove, and run AppImages from GitHub on the command line, and integrate apps into the desktop.

### Linux distributions

Although the AppImage format was carefully designed not to need any special support from Linux distributions, there are some that offer varying degrees of AppImage friendliness out of the box.

- [Deepin](https://www.deepin.org/en/) - When you double-click an AppImage or any other executable file that lacks execute permissions, a user-friendly dialog explains the situation and asks for your permission to set the execute permission and execute the executable.
- [Nitrux](https://nxos.org/) - Promotes the use of AppImage as the main format for getting applications, has a built in app center featuring AppImages.
- [Linux Mint](https://linuxmint.com/) - Has an [AppImage thumbnailer](https://github.com/linuxmint/xapp-thumbnailers) [![GitHub stars](https://img.shields.io/github/stars/linuxmint/xapp-thumbnailers?style=flat)](https://github.com/linuxmint/xapp-thumbnailers/stargazers) to show application icons on AppImage files.
- [Zenwalk GNU Linux](http://www.zenwalk.org/) - Is "AppImage ready" and distributes some applications in AppImage format.

## AppImage developer tools

### Low-level tools

- [appimagetool](https://github.com/AppImage/AppImageKit/releases/tag/continuous) [![GitHub stars](https://img.shields.io/github/stars/AppImage/AppImageKit/releases/tag/continuous?style=flat)](https://github.com/AppImage/AppImageKit/releases/tag/continuous/stargazers) - Converts AppDirs into AppImages.
- [nix-bundle](https://github.com/matthewbauer/nix-bundle) [![GitHub stars](https://img.shields.io/github/stars/matthewbauer/nix-bundle?style=flat)](https://github.com/matthewbauer/nix-bundle/stargazers) - Converts Nix derivations into AppImages.

### Build systems

- [appimagecraft](https://github.com/TheAssassin/appimagecraft) [![GitHub stars](https://img.shields.io/github/stars/TheAssassin/appimagecraft?style=flat)](https://github.com/TheAssassin/appimagecraft/stargazers) - Recipe based AppImage creation tool working from source.
- [appimage-builder](https://github.com/AppImageCrafters/appimage-builder) [![GitHub stars](https://img.shields.io/github/stars/AppImageCrafters/appimage-builder?style=flat)](https://github.com/AppImageCrafters/appimage-builder/stargazers) - Recipe based AppImage creation tool working from source.
- [KDE Craft](https://invent.kde.org/packaging/craft) - Build system used by KDE that can produce AppImages and other formats.
- [appimage-tooling](https://gitlab.com/sgclarkkde/appimage-tooling) - Ruby tooling to generate Appimages.
- [AppImage.cmake](https://github.com/Ravbug/AppImage.cmake) [![GitHub stars](https://img.shields.io/github/stars/Ravbug/AppImage.cmake?style=flat)](https://github.com/Ravbug/AppImage.cmake/stargazers) - CMake script which facilitates generating AppImage executables for Linux.
- [rules_appimage](https://github.com/lalten/rules_appimage) [![GitHub stars](https://img.shields.io/github/stars/lalten/rules_appimage?style=flat)](https://github.com/lalten/rules_appimage/stargazers) - Bazel rules to package any lang_binary target as AppImage.

### Deployment tools for compiled applications

- [go-appimagetool](https://github.com/probonopd/go-appimage/tree/master/src/appimagetool) [![GitHub stars](https://img.shields.io/github/stars/probonopd/go-appimage/tree/master/src/appimagetool?style=flat)](https://github.com/probonopd/go-appimage/tree/master/src/appimagetool/stargazers) - Tool that deploys dependencies into AppDirs, and converts AppDirs into AppImages (experimental).
- [linuxdeployqt](https://github.com/probonopd/linuxdeployqt) [![GitHub stars](https://img.shields.io/github/stars/probonopd/linuxdeployqt?style=flat)](https://github.com/probonopd/linuxdeployqt/stargazers) - Deploys dependencies into AppDirs and creates AppImages; for Qt and other compiled applications.
- [linuxdeploy](https://github.com/linuxdeploy/linuxdeploy) [![GitHub stars](https://img.shields.io/github/stars/linuxdeploy/linuxdeploy?style=flat)](https://github.com/linuxdeploy/linuxdeploy/stargazers) - AppDir creation and maintenance tool using plugins.
- [XojoToAppImage](https://github.com/AlwaysOfflineSoftware/XojoToAppImage) [![GitHub stars](https://img.shields.io/github/stars/AlwaysOfflineSoftware/XojoToAppImage?style=flat)](https://github.com/AlwaysOfflineSoftware/XojoToAppImage/stargazers) - Graphical tool for packaging compiled Xojo Linux programs into AppImages.

### Deployment tools for Python applications

- [python-appimage](https://github.com/niess/python-appimage) [![GitHub stars](https://img.shields.io/github/stars/niess/python-appimage?style=flat)](https://github.com/niess/python-appimage/stargazers) - Ready to use AppImage distributions of Python (can be modified to include your application).
- [linuxdeploy-plugin-python](https://github.com/niess/linuxdeploy-plugin-python) [![GitHub stars](https://img.shields.io/github/stars/niess/linuxdeploy-plugin-python?style=flat)](https://github.com/niess/linuxdeploy-plugin-python/stargazers) - Bundle Python into an AppDir using a source distribution and linuxdeploy.
- [linuxdeploy-plugin-conda](https://github.com/linuxdeploy/linuxdeploy-plugin-conda) [![GitHub stars](https://img.shields.io/github/stars/linuxdeploy/linuxdeploy-plugin-conda?style=flat)](https://github.com/linuxdeploy/linuxdeploy-plugin-conda/stargazers) - Bundle Python into an AppDir using a source distribution, Conda, and linuxdeploy.
- [Briefcase](https://briefcase.readthedocs.io/) - Convert Python project into a standalone native application, e.g., using AppImage.
- [pycharm-appimage-support](https://gitlab.com/chezmurray/pycharm-appimage-support) - Deploy Python project as an AppImage directly from the PyCharm IDE.
- [PyAppImage](https://github.com/srevinsaju/pyappimage) [![GitHub stars](https://img.shields.io/github/stars/srevinsaju/pyappimage?style=flat)](https://github.com/srevinsaju/pyappimage/stargazers) - Ultimately simple python-to-appimage bundler.

### Deployment tools for Electron applications

- [electron-builder](https://github.com/electron-userland/electron-builder) [![GitHub stars](https://img.shields.io/github/stars/electron-userland/electron-builder?style=flat)](https://github.com/electron-userland/electron-builder/stargazers) - Supports AppImage as an output format.
- [electron-forge-maker-appimage](https://github.com/saleae/electron-forge-maker-appimage) [![GitHub stars](https://img.shields.io/github/stars/saleae/electron-forge-maker-appimage?style=flat)](https://github.com/saleae/electron-forge-maker-appimage/stargazers) - Electron Forge builder for AppImage.
- [Appnativefy](https://github.com/sarweshparajuli/appnativefy) [![GitHub stars](https://img.shields.io/github/stars/sarweshparajuli/appnativefy?style=flat)](https://github.com/sarweshparajuli/appnativefy/stargazers) - Create AppImage with embedded Electron browser from any website.

### Deployment tools for Windows applications

- [wine32-deploy](https://github.com/sudo-give-me-coffee/wine32-deploy) [![GitHub stars](https://img.shields.io/github/stars/sudo-give-me-coffee/wine32-deploy?style=flat)](https://github.com/sudo-give-me-coffee/wine32-deploy/stargazers) - Creates AppImages for 32-bit Windows applications that can run on 64-bit Linux systems without multilib installed.
- [AppImage For WINE](https://github.com/Hackerl/Wine_Appimage) [![GitHub stars](https://img.shields.io/github/stars/Hackerl/Wine_Appimage?style=flat)](https://github.com/Hackerl/Wine_Appimage/stargazers) - WINE-based AppImages and LD_PRELOAD based patches to launch WINE from AppImages.
- [ferion11/Wine_Appimage](https://github.com/ferion11/Wine_Appimage) [![GitHub stars](https://img.shields.io/github/stars/ferion11/Wine_Appimage?style=flat)](https://github.com/ferion11/Wine_Appimage/stargazers) - AppImage for WINE 32bits from PlayOnLinux, an run on no-multilib systems.
- [GameImage](https://gitlab.com/formigoni/gameimage) - Is a way to package up games with either Wine or an Emulator into a portable AppImage that could be useful for the Steam Deck.

### Deployment tools for Java applications

- [nbPackager](https://github.com/trixon/nbPackager) [![GitHub stars](https://img.shields.io/github/stars/trixon/nbPackager?style=flat)](https://github.com/trixon/nbPackager/stargazers) - Packages NetBeans Platform Application with a JRE for AppImage, Linux, macOS and Windows.

### Deployment tools for .NET Core (Mono) applications

- [Publish-AppImage for .NET](https://github.com/kuiperzone/Publish-AppImage) [![GitHub stars](https://img.shields.io/github/stars/kuiperzone/Publish-AppImage?style=flat)](https://github.com/kuiperzone/Publish-AppImage/stargazers) - Publish AppImages for .NET applications.
- [.NET Core AppImage example](https://github.com/ppy/osu-deploy/blob/697a49e9602502a2b7a899c0dff5383f6512d5d2/Program.cs#L207-L243) - Example of how to deploy .NET Core (Mono) applications as an AppImage using `dotnet publish -f netcoreapp3.1 -r linux-x64` from within a `.cs` program.
- [PupNet Deploy](https://github.com/kuiperzone/PupNet-Deploy) [![GitHub stars](https://img.shields.io/github/stars/kuiperzone/PupNet-Deploy?style=flat)](https://github.com/kuiperzone/PupNet-Deploy/stargazers) - Cross-platform deployment utility which publishes your .NET project and packages it as a ready-to-ship installation file in a single step.
- [DotnetPackaging](https://github.com/SuperJMN/DotnetPackaging) [![GitHub stars](https://img.shields.io/github/stars/SuperJMN/DotnetPackaging?style=flat)](https://github.com/SuperJMN/DotnetPackaging/stargazers) - Tool to distribute .NET applications in the AppImage format.

### Deployment tools for Flash applications

- [flash-to-appimage](https://github.com/CredibleOpossum/flash-to-appimage) [![GitHub stars](https://img.shields.io/github/stars/CredibleOpossum/flash-to-appimage?style=flat)](https://github.com/CredibleOpossum/flash-to-appimage/stargazers) - Script to package a Flash game (`.swf`) into an AppImage.

### Deployment tools for Rust applications

- [Cargo AppImage](https://github.com/StratusFearMe21/cargo-appimage) [![GitHub stars](https://img.shields.io/github/stars/StratusFearMe21/cargo-appimage?style=flat)](https://github.com/StratusFearMe21/cargo-appimage/stargazers) - Cargo program that allows you to convert your Rust programs into AppImages.

### Tools to convert from other package formats

- [pkg2appimage](https://github.com/AppImage/pkg2appimage) [![GitHub stars](https://img.shields.io/github/stars/AppImage/pkg2appimage?style=flat)](https://github.com/AppImage/pkg2appimage/stargazers) - Converts from deb, zip, tar.gz and other formats to AppImage using YAML recipes.
- [appimage2pkg](https://gitlab.com/nixtux-packaging/appimage2pkg) - Repack AppImage and make rpm/deb which does not require FUSE.
- [flatpak2appdir](https://github.com/sudo-give-me-coffee/flatpak2appdir) [![GitHub stars](https://img.shields.io/github/stars/sudo-give-me-coffee/flatpak2appdir?style=flat)](https://github.com/sudo-give-me-coffee/flatpak2appdir/stargazers) - Turn Flatpak into AppDir which in turn can be turned into AppImage.
- [make-portable](https://github.com/sudo-give-me-coffee/make-portable) [![GitHub stars](https://img.shields.io/github/stars/sudo-give-me-coffee/make-portable?style=flat)](https://github.com/sudo-give-me-coffee/make-portable/stargazers) - Deploys installed application to AppDir, uses strace to fetch all file system calls and copies all accessed files in to AppDir including glibc.
- [AppImage cobbler](https://gitlab.com/brinkervii/appimage-cobbler) - Python application that takes strace.log and turns it into a directory suited for an AppImage.
- [Elements](https://github.com/s-zeid/elements) [![GitHub stars](https://img.shields.io/github/stars/s-zeid/elements?style=flat)](https://github.com/s-zeid/elements/stargazers) - Tool to generate single-file, runc-based AppImages using a minimal (~3 MB compressed) Alpine Linux rootfs.
- [arch2appimage](https://github.com/hanzala123/arch2appimage) [![GitHub stars](https://img.shields.io/github/stars/hanzala123/arch2appimage?style=flat)](https://github.com/hanzala123/arch2appimage/stargazers) - Python script to convert any Arch Linux package (official/AUR) to an AppImage.
- [appimage-bash](https://github.com/valicm/appimage-bash) [![GitHub stars](https://img.shields.io/github/stars/valicm/appimage-bash?style=flat)](https://github.com/valicm/appimage-bash/stargazers) - GitHub Action for creating AppImage releases from binaries inside `.tar.gz` archives.
- [Package-to-appimage](https://github.com/CausaPrincipalis71/package-to-appimage) [![GitHub stars](https://img.shields.io/github/stars/CausaPrincipalis71/package-to-appimage?style=flat)](https://github.com/CausaPrincipalis71/package-to-appimage/stargazers) - Tool for converting `.deb` and `.rpm` packages into AppImage format by using Docker.
- [GMAppImager](https://github.com/samuelvenable/GMAppImager) [![GitHub stars](https://img.shields.io/github/stars/samuelvenable/GMAppImager?style=flat)](https://github.com/samuelvenable/GMAppImager/stargazers) - Graphically Converts GameMaker Studio 2 games to AppImage bundles.
- [AppImaGen](https://github.com/ivan-hc/AppImaGen) [![GitHub stars](https://img.shields.io/github/stars/ivan-hc/AppImaGen?style=flat)](https://github.com/ivan-hc/AppImaGen/stargazers) - Generates an AppImage from Debian or from a PPA of your choice for the previous (unfortunately not the oldest as recommended) and still supported Ubuntu LTS.

### Metadata tools

- [AppStream MetaInfo Creator](https://www.freedesktop.org/software/appstream/metainfocreator/#/) - More elaborate generator for AppStream MetaInfo files by the author of the AppStream metainfo format.

### QC tools

- [appimage-testsuite](https://github.com/aferrero2707/appimage-testsuite) [![GitHub stars](https://img.shields.io/github/stars/aferrero2707/appimage-testsuite?style=flat)](https://github.com/aferrero2707/appimage-testsuite/stargazers) - AppImage testing environment based on Docker containers for various Linux distributions.
- [appimagelint](https://github.com/TheAssassin/appimagelint) [![GitHub stars](https://img.shields.io/github/stars/TheAssassin/appimagelint?style=flat)](https://github.com/TheAssassin/appimagelint/stargazers) - Tool to check AppImages for compatibility, best practices etc.

### Continuous integration

- [GitHub Actions example](https://github.com/probonopd/Zoom.AppImage/blob/master/.github/workflows/main.yml) [![GitHub stars](https://img.shields.io/github/stars/probonopd/Zoom.AppImage/blob/master/.github/workflows/main.yml?style=flat)](https://github.com/probonopd/Zoom.AppImage/blob/master/.github/workflows/main.yml/stargazers) - Example of how to upload AppImages built using GitHub Actions to GitHub Releases.
- [appimage.yml](https://github.com/iotang/Project_LemonLime/blob/master/.github/workflows/appimage.yml) [![GitHub stars](https://img.shields.io/github/stars/iotang/Project_LemonLime/blob/master/.github/workflows/appimage.yml?style=flat)](https://github.com/iotang/Project_LemonLime/blob/master/.github/workflows/appimage.yml/stargazers) - Bigger, more complex example of how to build and upload AppImages using GitHub Actions.
- [build-appimage-action](https://github.com/AppImageCrafters/build-appimage-action) [![GitHub stars](https://img.shields.io/github/stars/AppImageCrafters/build-appimage-action?style=flat)](https://github.com/AppImageCrafters/build-appimage-action/stargazers) - GitHub Action for producing AppImages using appimage-builder.
- [jniltinho/packages](https://github.com/jniltinho/packages) [![GitHub stars](https://img.shields.io/github/stars/jniltinho/packages?style=flat)](https://github.com/jniltinho/packages/stargazers) - Drone.io example for producing AppImages using go-appimagetool.
- [Link to the latest build artifact on GitLab CI](https://gitlab.com/linuxappimage/element-desktop/-/jobs/artifacts/master/raw/Element.AppImage?job=run-build) - Example of how to directly link to the latest build artifact on GitLab CI (can be tricky).

### Libraries

- [QAppImageUpdate](https://github.com/antony-jr/QAppImageUpdate) [![GitHub stars](https://img.shields.io/github/stars/antony-jr/QAppImageUpdate?style=flat)](https://github.com/antony-jr/QAppImageUpdate/stargazers) - Qt5 library and plugin for updating AppImages, can be embedded into applications.
- [AppImageServices](https://github.com/azubieta/AppImageServices) [![GitHub stars](https://img.shields.io/github/stars/azubieta/AppImageServices?style=flat)](https://github.com/azubieta/AppImageServices/stargazers) - D-Bus services providing a high-level interface over the AppImage manipulation libraries for file managers, software centers and other tools.
- [libappimage](https://github.com/AppImage/libappimage) [![GitHub stars](https://img.shields.io/github/stars/AppImage/libappimage?style=flat)](https://github.com/AppImage/libappimage/stargazers) - Implements functionality for dealing with AppImage files, written in C++ using Boost.
- [libzsync-go](https://github.com/AppImageCrafters/libzsync-go) [![GitHub stars](https://img.shields.io/github/stars/AppImageCrafters/libzsync-go?style=flat)](https://github.com/AppImageCrafters/libzsync-go/stargazers) - Zsync implementation written in Go that can be used to update AppImages.
- [appenv](https://github.com/TheMarlboroMan/appenv) [![GitHub stars](https://img.shields.io/github/stars/TheMarlboroMan/appenv?style=flat)](https://github.com/TheMarlboroMan/appenv/stargazers) - Small C++ library telling where the app data resides and where the user data is by using `readlink("/proc/self/exe")`), thus allowing C++ applications to become relocatable in the filesystem.

### Templates

- [Qt Desktop Template](https://github.com/stemoretti/qt-desktop-template) [![GitHub stars](https://img.shields.io/github/stars/stemoretti/qt-desktop-template?style=flat)](https://github.com/stemoretti/qt-desktop-template/stargazers) - Template for creating Qt Widgets desktop applications with AppImage generation using linuxdeployqt.
- [qt-hello-world](https://github.com/AppImageCrafters/qt-hello-world) [![GitHub stars](https://img.shields.io/github/stars/AppImageCrafters/qt-hello-world?style=flat)](https://github.com/AppImageCrafters/qt-hello-world/stargazers) - Qt Hello World project for AppImage creation using appimage-builder.
- [qt-qml-project-template-with-ci](https://github.com/219-design/qt-qml-project-template-with-ci) [![GitHub stars](https://img.shields.io/github/stars/219-design/qt-qml-project-template-with-ci?style=flat)](https://github.com/219-design/qt-qml-project-template-with-ci/stargazers) - Template for a Qt/QML application with batteries included: GitHub CI, automated GUI testing, automatic code-format checks and more. Compiles for Linux (AppImage), Mac, and Android.
- [mini-qml](https://github.com/patrickelectric/mini-qml) [![GitHub stars](https://img.shields.io/github/stars/patrickelectric/mini-qml?style=flat)](https://github.com/patrickelectric/mini-qml/stargazers) - Minimal Qml application template with deployment for Linux (AppImage), Windows, macOS and WebAssembly.
- [wxWidgetsTemplate](https://github.com/Ravbug/wxWidgetsTemplate) [![GitHub stars](https://img.shields.io/github/stars/Ravbug/wxWidgetsTemplate?style=flat)](https://github.com/Ravbug/wxWidgetsTemplate/stargazers) - Cross-platform application template for wxWidgets C++, with pre-set files and IDE projects, supporting AppImage.
- [Briefcase Linux AppImage Template](https://github.com/beeware/briefcase-linux-appimage-template) [![GitHub stars](https://img.shields.io/github/stars/beeware/briefcase-linux-appimage-template?style=flat)](https://github.com/beeware/briefcase-linux-appimage-template/stargazers) - Cookiecutter template for building Python apps that will run under Linux, packaged as an AppImage.

## Resources

### Specs

- [AppImageSpec](https://github.com/AppImage/AppImageSpec) [![GitHub stars](https://img.shields.io/github/stars/AppImage/AppImageSpec?style=flat)](https://github.com/AppImage/AppImageSpec/stargazers) - Official specification for the AppImage format.
- [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/latest/) - Specification for the matadata used inside AppImages.

### Documentation

- [docs.appimage.org](https://docs.appimage.org/) - Official AppImage documentation.
- [appimage-builder.readthedocs.io](https://appimage-builder.readthedocs.io/) - Documentation of appimage-builder, includes tutorials, examples, and more.

### Tutorials

- [Produce an AppImage that bundles everything with go-appimage](https://www.youtube.com/watch?v=XTGn_JqmDu0) - How to make an AppImage that bundles _all_ required libraries so that it should run not only on newer, but also on _older_ systems than the build system.

### Articles

- [The Background Story of AppImage](https://itsfoss.com/appimage-interview/) - Interview with the creator of AppImage, explaining the key ideas and motivations behind the concept.
- [Flatpak, Snap and AppImage](https://distrowatch.com/weekly.php?issue=20160704#opinion) - Jesse Smith on DistroWatch about AppImage, Flatpak and Snap.
- [Don't Install, Just Copy with klik](https://dot.kde.org/2005/09/16/dont-install-just-copy-klik) - Article from 2005 that gives perspective on how AppImage started, relevant only for historical reasons now.

### Videos

- [AppImage: Portable applications for Linux](https://www.youtube.com/watch?v=nzZ6Ikc7juw) - Official AppImage introduction video by its founder.
- [Comparing Linux Package Formats - Deb, Flatpak, AppImage, etc.](https://www.youtube.com/watch?v=7fPShv-8Z_4) - By Bryan Lunduke.
- [AppImage: Universal Linux Apps, Overview and Thoughts](https://www.youtube.com/watch?v=tMqES2pNxYY) - By Jeremy "Jay" LaCroix, LearnLinuxTV.
- [AppImage system integration on Ubuntu using go-appimaged](https://www.youtube.com/watch?v=L00UjifUEfE) - New appimaged daemon from the go-appimage implementation.
- [Integrate and Manage AppImages with AppImageLauncher](https://www.youtube.com/watch?v=D2WA2zdLvVk) - By Eric Adams.

### Books

- [Mastering Qt 5](https://www.amazon.de/Mastering-Qt-stunning-cross-platform-applications-ebook/dp/B07DH9YK9Q/) - Contains a section on how to package and deploy Qt applications for Linux using linuxdeployqt.

### Blogs

- [Planet AppImage](https://appimage.gitlab.io/planet/) - Blog Aggregator covering all things AppImage.
- [TheAssassin Blog](https://assassinate-you.net/tags/appimage/) - Blog covering AppImage related topics by TheAssassin.
- [AppImage Crafters Blog](https://appimagecrafters.github.io/) - Blog about AppImage creation an usage by azubieta.

### Courses

### Community

- [#AppImage channel on libera.chat](https://web.libera.chat/#AppImage) - Chat where AppImage developers and users hang out, be prepared to stay in the channel for days if you don't get answers immediately.
- [discourse.appimage.org](https://discourse.appimage.org/) - Official AppImage forum for users and application developers.
- [Stack Overflow](https://stackoverflow.com/tags/AppImage) - Questions tagged `[appimage]` on Stack Overflow.
- [r/AppImage/](https://www.reddit.com/r/AppImage/) - AppImage subreddit.

### Miscellaneous

- [AppImage wiki](https://github.com/AppImage/AppImageKit/wiki) [![GitHub stars](https://img.shields.io/github/stars/AppImage/AppImageKit/wiki?style=flat)](https://github.com/AppImage/AppImageKit/wiki/stargazers) - Official AppImage wiki.
- [AppImageZip](https://github.com/sagebind/appimagezip) [![GitHub stars](https://img.shields.io/github/stars/sagebind/appimagezip?style=flat)](https://github.com/sagebind/appimagezip/stargazers) - Experimental pure Rust implementation of the AppImage runtime that uses Zip as the backing file system image.
- [help-wanted](https://github.com/search?q=user%3Aappimage+label%3Ahelp-wanted+state%3Aopen&type=Issues) [![GitHub stars](https://img.shields.io/github/stars/search?q=user%3Aappimage+label%3Ahelp-wanted+state%3Aopen&type=Issues?style=flat)](https://github.com/search?q=user%3Aappimage+label%3Ahelp-wanted+state%3Aopen&type=Issues/stargazers) - AppImage issues that the AppImage team would like your help with. A great way to get started contributing to the project.
- [appdwarf](https://github.com/Phantop/appdwarf) [![GitHub stars](https://img.shields.io/github/stars/Phantop/appdwarf?style=flat)](https://github.com/Phantop/appdwarf/stargazers) - A tool to convert an AppDir or an existing AppImage file, either as a local file or from a URL, into a highly compressed portable image using dwarfs.

### Related

- [Similar projects](https://github.com/AppImage/AppImageKit/wiki/Similar-projects) [![GitHub stars](https://img.shields.io/github/stars/AppImage/AppImageKit/wiki/Similar-projects?style=flat)](https://github.com/AppImage/AppImageKit/wiki/Similar-projects/stargazers) - Comparison to other packaging systems.

### Other awesome lists

- [awesome-linuxdeploy](https://github.com/linuxdeploy/awesome-linuxdeploy) [![GitHub stars](https://img.shields.io/github/stars/linuxdeploy/awesome-linuxdeploy?style=flat)](https://github.com/linuxdeploy/awesome-linuxdeploy/stargazers) - Awesome list on linuxdeploy.
- [All Awesome Lists](https://github.com/topics/awesome) [![GitHub stars](https://img.shields.io/github/stars/topics/awesome?style=flat)](https://github.com/topics/awesome/stargazers) - All the Awesome lists on GitHub.

### Expired links

- [App Outlet](https://app-outlet.github.io/) - Universal app store that works with AppImages, Flatpaks and Snaps.
- [appimage2desktop](https://github.com/me1ting/appimage2desktop) [![GitHub stars](https://img.shields.io/github/stars/me1ting/appimage2desktop?style=flat)](https://github.com/me1ting/appimage2desktop/stargazers) - Creates a desktop file and an icon in the system for an AppImage, nothing else.
- [AppImage-Integrator](https://github.com/w-j-r/AppImage-Integrator) [![GitHub stars](https://img.shields.io/github/stars/w-j-r/AppImage-Integrator?style=flat)](https://github.com/w-j-r/AppImage-Integrator/stargazers) - A simple program to integrate AppImages into the Linux desktop written in Qt6.
- [Get AppImage](https://g.sreve/get-appimage/) - Collection of all AppImages in one website. Great search functionality.
- [AppStream Generator](https://output.jsbin.com/qoqukof) - Very simple generator for AppStream MetaInfo files which application authors can use to add metadata (like descriptions, screenshots, links) to their AppImage.
