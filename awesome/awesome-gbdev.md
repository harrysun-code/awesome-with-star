# Game Boy Development

[![GitHub stars](https://img.shields.io/github/stars/gbdev/awesome-gbdev?style=flat)](https://github.com/gbdev/awesome-gbdev/stargazers)

# ![GameboyIcon](http://i.imgur.com/ROUq7NT.gif) Awesome Game Boy Development

#### [Join us on Discord](https://gbdev.io/chat.html) [![Discord Badge](https://img.shields.io/badge/dynamic/json.svg?label=chat&colorB=green&suffix=%20online&query=presence_count&uri=https://discordapp.com/api/guilds/303217943234215948/widget.json)](https://discord.gg/tKGMPNr)

A curated list of awesome Game Boy (Color) Development resources, tools, docs, related projects and open-source ROMs. Inspired by the [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) list thing.

You can find a (way cooler) web version of this list [here](https://gbdev.github.io/resources).

## Contents

- [Introduction](#introduction)
  - [Disambiguation](#disambiguation)
- [Community](#community)
- [Documentation](#documentation)
  - [Misc](#misc)
  - [Opcodes](#opcodes)
  - [Game Boy Color](#game-boy-color)
  - [Hardware](#hardware)
  - [Peripherals](#peripherals)
  - [Cartridges](#cartridges)
- [Emulator Development](#emulator-development)
  - [Testing](#testing)
- [Software Development](#software-development)
  - [Assemblers](#assemblers)
  - [Compilers](#compilers)
    - [Experimental/Proof of Concepts](#experimentalproof-of-concepts)
  - [Emulators](#emulators)
  - [Tools](#tools)
    - [Engines](#engines)
    - [Development tools](#development-tools)
    - [Graphics utilities](#graphics-utilities)
    - [Hardware and ROM utilities](#hardware-and-rom-utilities)
    - [Music drivers and trackers](#music-drivers-and-trackers)
- [Programming](#programming)
  - [ASM](#asm)
    - [Sources](#sources)
    - [Timings](#timings)
    - [Boilerplates](#boilerplates)
    - [Syntax highlighting packages](#syntax-highlighting-packages)
  - [C](#c)
- [Homebrews](#homebrews)
  - [ASM](#asm-1)
  - [C](#c-1)
  - [GB Studio](#gb-studio) 
  - [Demos](#demos)
- [Reverse Engineering](#reverse-engineering)
  - [Game Disassemblies](#game-disassemblies)
- [Game Boy Camera](#game-boy-camera)
  - [Retrieving Images](#retrieving-images)
  - [Changing the camera's behavior](#changing-the-cameras-behavior)
  - [Post-processing](#post-processing)
- [Related projects](#related-projects)
  - [Directories](#directories)
  - [Websites](#websites)
- [About](#about)
  - [Contribute](#contribute)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Sponsors](#sponsors)

## Introduction

- [The Game Boy, a hardware autopsy](https://www.youtube.com/playlist?list=PLu3xpmdUP-GRDp8tknpXC_Y4RUQtMMqEu)
- [The Ultimate Game Boy Talk](https://media.ccc.de/v/33c3-8029-the_ultimate_game_boy_talk)


> ### Disambiguation
>
> #### Game Boy Advance
>
> Game Boy Advance development is covered by another project, the [awesome-gbadev](https://github.com/gbdev/awesome-gbadev) [![GitHub stars](https://img.shields.io/github/stars/gbdev/awesome-gbadev?style=flat)](https://github.com/gbdev/awesome-gbadev/stargazers) list.
> GBA, however, *can run* GB/GBC games. It does so in a slightly different way compared to native hardware: this is covered in the Emulator Development section of this list.
>
> #### Game Boy Color and Super Game Boy
>
> This list is focused on the original *Game Boy* (GB or DMG, 1989), the *Game Boy Color* (GBC or CGB) and the *Super Game Boy* (SGB) are very similar systems, with a few important distinctions, such as:
>
>- Different hardware specifications;
>- Specific hardware and software features;
>- Specific registers;
>- Specific bugs, quirks and exploitable behaviours.
>
>If you aim to develop your software for SGB or GBC, or you want to know how it runs on the other systems, you may want to take advantage and adapt to these differences, check the [Game Boy Color](#game-boy-color) category and look for specific references to GBC/CGB and SGB.


## Community

- [Chat channels](https://gbdev.io/chat)
- [Forum](https://gbdev.gg8.se/forums/)

## Documentation

- [**Pan Docs**](https://gbdev.github.io/pandocs/) - The single, most comprehensive technical reference to Game Boy available to the public. Corrected, updated and maintained by the community.
- [The Cycle-Accurate Game Boy Docs](https://github.com/AntonioND/giibiiadvance/blob/master/docs/TCAGBD.pdf) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/giibiiadvance/blob/master/docs/TCAGBD.pdf?style=flat)](https://github.com/AntonioND/giibiiadvance/blob/master/docs/TCAGBD.pdf/stargazers) - A precise documentation by AntonioND to make a cycle-accurate Game Boy emulator.
- [Complete Technical Reference](https://gekkio.fi/files/gb-docs/gbctr.pdf) - by Gekkio.
- [Game Boy Architecture: A Practical Analysis](https://www.copetti.org/writings/consoles/game-boy/) - by Rodrigo Copetti.
- [Game Boy Project Report](http://www.cs.columbia.edu/~sedwards/classes/2019/4840-spring/reports/GameBoy.pdf) - Report of an hardware [emulator](https://github.com/kitsuneh/SVGameBoy) [![GitHub stars](https://img.shields.io/github/stars/kitsuneh/SVGameBoy?style=flat)](https://github.com/kitsuneh/SVGameBoy/stargazers) (on a Terasic DE1-SoC Board) developed as final project for the CSEE4840 Embedded Systems Design course at Columbia University.

#### Opcodes

- [gb-opcodes](https://gbdev.github.io/gb-opcodes/optables/) - Opcodes table
- [RGBDS opcodes reference](https://rgbds.gbdev.io/docs/gbz80.7) - A reference of all instructions, including short descriptions, cycle and byte counts, and explanations of flag modifications.

### Game Boy Color

- [Bootstrap ROM](https://tcrf.net/Game_Boy_Color_Bootstrap_ROM)
- [Unused Palettes](https://tcrf.net/Notes:Game_Boy_Color_Bootstrap_ROM)
- [Colorization palettes in the BIOS](https://forums.nesdev.org/viewtopic.php?p=114388#p114388)
- [Boot ROM Disassembly](https://gist.github.com/drhelius/6063265)
- [GBC Hicolour notes](https://romhack.github.io/doc/gbcHiColour/) - A technical note regarding Hicolour mode trick for Game Boy Color and its realization in the GBC game “Crystalis”.

### Hardware

- [DMG Schematics](http://gbdev.gg8.se/wiki/articles/DMG_Schematics) - Hardware schematics.
- [The Game Boy Project](http://marc.rawer.de/Gameboy/Docs/GBProject.pdf) - Provides a study on the hardware and detailed constructional information for the implementation of three 8-bit bidirectional parallel ports.
- [Related custom hardware](https://github.com/Gekkio/gb-hardware) [![GitHub stars](https://img.shields.io/github/stars/Gekkio/gb-hardware?style=flat)](https://github.com/Gekkio/gb-hardware/stargazers) - by Gekkio.
- [ESP8266 GB Dev Board](https://github.com/applefreak/esp8266-gameboy-dev-board) [![GitHub stars](https://img.shields.io/github/stars/applefreak/esp8266-gameboy-dev-board?style=flat)](https://github.com/applefreak/esp8266-gameboy-dev-board/stargazers) - Dev board for Game Boy accessories development, powered by ESP8266.
- [ESP8266 GB Printer](https://github.com/applefreak/esp8266-gameboy-printer) [![GitHub stars](https://img.shields.io/github/stars/applefreak/esp8266-gameboy-printer?style=flat)](https://github.com/applefreak/esp8266-gameboy-printer/stargazers) - A device that emulates the GB Printer and lets you retrieve images using WiFi.
- [fruttenboel](https://web.archive.org/web/20220628023315/https://verhoeven272.nl/fruttenboel/Gameboy/index.html) - Page with loads of information on the hardware, custom boards to interface with the console and other related projects.
- [Game Boy hardware database](https://gbhwdb.gekkio.fi/) - Data and photos of various types of Game Boy consoles.
- [dmg-schematics](https://github.com/msinger/dmg-schematics) [![GitHub stars](https://img.shields.io/github/stars/msinger/dmg-schematics?style=flat)](https://github.com/msinger/dmg-schematics/stargazers) - Schematics and annotated overlay for the DMG-CPU B chip, extracted from die photos, made with KiCad. Also contains Electric VLSI library with layouts for some of the cells and memories.

### Peripherals

- [Dan Docs](https://shonumi.github.io/dandocs.html) - Obscure Game Boy hardware documentation.
- [Edge of Emulation](https://shonumi.github.io/articles.html), a series of articles about emulating and investigating Game Boy accessories. Also available as [technical documents](https://github.com/shonumi/gbe-plus/tree/master/src/docs/technical) [![GitHub stars](https://img.shields.io/github/stars/shonumi/gbe-plus/tree/master/src/docs/technical?style=flat)](https://github.com/shonumi/gbe-plus/tree/master/src/docs/technical/stargazers) in the GBE- emulator documentation.
  - [Mobile Adapter GB](https://shonumi.github.io/articles/art14.html) - Internet connectivity and DLC on the Game Boy Color.
  - [The Game Boy Printer](https://shonumi.github.io/articles/art2.html)
  - [Pocket Sonar](https://shonumi.github.io/articles/art13.html) - A blue cart with built-in sonar hardware.
  - [Zok Zok Heroes](https://shonumi.github.io/articles/art8.html)  - Zok Zok Heroes' Full Changer, a motion-activated accessory.
  - [Infrared Madness](https://shonumi.github.io/articles/art11.html) - Infrared communication on the Game Boy Color.
  - [Game Boy 4-Player Adapter](https://shonumi.github.io/articles/art9.html) - DMG-07.
  - [Barcode Boy](https://shonumi.github.io/articles/art7.html) - The first Game Boy card-scanner.
  - [Barcode Taisen Bardigun](https://shonumi.github.io/articles/art6.html) - A late 90s DMG-GBC barcode reader.
- [DMG-07 Technical Documentation](https://raw.githubusercontent.com/shonumi/gbe-plus/master/src/docs/technical/DMG_07.txt)
- [Game Boy Camera RE](https://github.com/AntonioND/gbcam-rev-engineer) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/gbcam-rev-engineer?style=flat)](https://github.com/AntonioND/gbcam-rev-engineer/stargazers) - Documentation about GB Camera and tools used to reverse engineer it by using Arduino.
- [Creating photo realistic images with neural networks and a Gameboy Camera](http://www.pinchofintelligence.com/photorealistic-neural-network-gameboy/)
- [The Game Boy Printer](https://shonumi.github.io/articles/art2.html) - An in-depth technical document about the printer hardware, the communication protocol and the usual routine that games used for implementing the print feature.
- [Ben Heck Reverse Engineers Game Boy Printer](https://www.youtube.com/watch?v=43FfJvd-YP4) (Errata: the used thermal paper is expired, 4 colors are actually printable).
- [Arduino Game Boy Printer Emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator) [![GitHub stars](https://img.shields.io/github/stars/mofosyne/arduino-gameboy-printer-emulator?style=flat)](https://github.com/mofosyne/arduino-gameboy-printer-emulator/stargazers) - Emulating a Game Boy Printer via the Game Boy Link cable with an Arduino.
- [Mobile Game Boy Adapter](https://bulbapedia.bulbagarden.net/wiki/Mobile_Game_Boy_Adapter)
- [GB KISS LINK MODEM](http://nectaris.tg-16.com/GB-KISS-LINK-FAQ-hudson-gameboy-nectaris.html)

### Cartridges

- [GB Flash Cartridges for Sale](https://bbbbbr.github.io/GameBoy-Flash-Carts/) - A List of available, ready-made Game Boy Flash Cartridges.
- [AntonioND's docs](https://github.com/AntonioND/giibiiadvance/tree/master/docs) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/giibiiadvance/tree/master/docs?style=flat)](https://github.com/AntonioND/giibiiadvance/tree/master/docs/stargazers) - Corrected schematics and infos on cartridge header data.
- [Gekkio's Game Boy cartridge types](http://gekkio.fi/blog/2015-02-14-mooneye-gb-gameboy-cartridge-types.html) - An overview on existing cartridge types.
- Gekkio's cartridge analysis:
  - [DMG-BEAN-02](http://gekkio.fi/blog/2015-05-18-mooneye-gb-cartridge-analysis-dmg-bean-02.html);
  - [MBC1](http://gekkio.fi/blog/2015-05-17-mooneye-gb-cartridge-analysis-fortress-of-fear.html);
  - [no MBC](http://gekkio.fi/blog/2015-02-28-mooneye-gb-cartridge-analysis-tetris.html).
- Pinout, registers descriptions and VHDL code of some cartridge types on Tauwasser's wiki:
  - [MBC1](https://wiki.tauwasser.eu/view/MBC1)
  - [MBC2](https://wiki.tauwasser.eu/view/MBC2)
  - [MMM01](https://wiki.tauwasser.eu/view/MMM01)
- [Game Boy Cartridges Schematics](http://www.devrs.com/gb/files/gb.html) - Schematics for MBC2 and MBC3 types.
- [Cartridges PCB photos](https://imgur.com/a/D5bpC)
- [MBC1+RAM+Battery cartridge Schematic](http://www.devrs.com/gb/files/mbc1.gif) - First schematics by Jeff Frohwein.
- [MBC1 and MBC2 cartridges circuits](http://fms.komkon.org/GameBoy/Tech/Carts.html) - and explanation on how these MBC bank switch and control RAM.
- [GB Rom List](CartridgeList.csv) - Navigable table of every game released with details on their cartridges.
- [Game Boy cartridge PCB photos](http://gekkio.fi/blog/2016-03-19-game-boy-cartridge-pcb-photos.html)


#### Custom cartridges

- [Emulating a GameBoy Cartridge](https://dhole.github.io/post/gameboy_cartridge_emu_1/) - Emulating the functionality of a Game Boy cartridge with the development board STM32F4.
- [Wolf](http://www.happydaze.se/wolf/) - Game Boy cartridge with co-processor.
- [Homebrew-Gameboy-Cartridge](https://github.com/dwaq/Homebrew-Gameboy-Cartridge) [![GitHub stars](https://img.shields.io/github/stars/dwaq/Homebrew-Gameboy-Cartridge?style=flat)](https://github.com/dwaq/Homebrew-Gameboy-Cartridge/stargazers) - Eagle library, schematic, and board files for a cartridge PCB using an Atmel AT49F040 as ROM.
- [Homebrew Gameboy Color Cartridge](https://github.com/Xyl2k/Gameboy-Color-Cartridge) [![GitHub stars](https://img.shields.io/github/stars/Xyl2k/Gameboy-Color-Cartridge?style=flat)](https://github.com/Xyl2k/Gameboy-Color-Cartridge/stargazers) - Board layout for an EEPROM powered cartridge.
- [Nekocart](https://github.com/zephray/NekoCart-GB) [![GitHub stars](https://img.shields.io/github/stars/zephray/NekoCart-GB?style=flat)](https://github.com/zephray/NekoCart-GB/stargazers) - Open-source flash cartridge using an Xilinx CPLD as MBC5 ([Post](https://hackaday.io/project/41160-nekocart-cpld-gameboy-cartridge)).
- [Reiner Ziegler's Game Boy page](http://reinerziegler.de.mirrors.gg8.se/) - Commercial and homemade programmable cartridges and programming systems. Tutorials, wiring and schematics provided.
- [Gameboy-MBC5-MBC1-Hybrid](https://github.com/insidegadgets/Gameboy-MBC5-MBC1-Hybrid) [![GitHub stars](https://img.shields.io/github/stars/insidegadgets/Gameboy-MBC5-MBC1-Hybrid?style=flat)](https://github.com/insidegadgets/Gameboy-MBC5-MBC1-Hybrid/stargazers) - CPLD implementation of a MBC5/MBC1 Hybrid cartridge.

#### Misc

- [Introduction to Game Boy Hacking](http://pepijndevos.nl/sha2017/workshop.pdf) - Workshop introducing basic assembly, debugging and reverse engineering.
- [GBSOUND.txt](https://github.com/bwhitman/pushpin/blob/master/src/gbsound.txt) [![GitHub stars](https://img.shields.io/github/stars/bwhitman/pushpin/blob/master/src/gbsound.txt?style=flat)](https://github.com/bwhitman/pushpin/blob/master/src/gbsound.txt/stargazers) - A document detailing the Game Boy sound engine.
- [gbdev FAQs](http://www.devrs.com/gb/files/faqs.html) - Must read by Jeff Frohwein.
- [Game Boy Bootrom](http://www.neviksti.com/DMG/DMG_ROM.asm) - Commented dump of the DMG bootrom.
- [Differences between the Z80 and the gameboy's processor](http://www.z80.info/z80gboy.txt)
- [Gameboy 2BPP Graphics Format](http://www.huderlem.com/demos/gameboy2bpp.html) - Information on how the Game Boy interprets VRAM tile data to color pixels.

## Emulator Development

- [Reverse Engineering fine details of Game Boy hardware](https://www.youtube.com/watch?v=GBYwjch6oEE) - 43 minutes talk by Gekkio given at Disobey 2018 ([errata](https://gekkio.fi/blog/2018-02-05-errata-for-reverse-engineering-fine-details-of-game-boy-hardware.html)).
- [Emulation of Nintendo Game Boy](https://github.com/Baekalfen/PyBoy/blob/master/extras/PyBoy.pdf) [![GitHub stars](https://img.shields.io/github/stars/Baekalfen/PyBoy/blob/master/extras/PyBoy.pdf?style=flat)](https://github.com/Baekalfen/PyBoy/blob/master/extras/PyBoy.pdf/stargazers) - Overview of the Game Boy hardware with the perspective of building an emulator.
- [DMG-01](https://rylev.github.io/DMG-01/public/book/) - An educational Gameboy Emulator in Rust and a companion book explaining its development. *[Oh Boy! Creating a Game Boy Emulator in Rust](https://media.ccc.de/v/rustfest-rome-3-gameboy-emulator)- is a talk given at Rust Fest 18 about this.
- [Building a Game Boy emulator in JavaScript](http://imrannazar.com/gameboy-Emulation-in-JavaScript) - Step by step tutorial.
- [Writing a Game Boy emulator, Cinoop](https://cturt.github.io/cinoop.html)
- [0dmg](https://jeremybanks.github.io/0dmg/2018/05/23/getting-started.html) - Learning Rust by building a partial Game Boy emulator.
- [RealBoy Emulator](https://realboyemulator.wordpress.com/posts/) - A series of posts about the design and implementation of the RealBoy Emulator.
- [Codeslinger](http://www.codeslinger.co.uk/pages/projects/gameboy.html) - Another series of posts documenting the building of an emulator.
- [Why did I spend 1.5 months creating a Gameboy emulator?](http://blog.rekawek.eu/2017/02/09/coffee-gb/) - Blog post.
- [binjgb rewind](https://binji.github.io/2017/12/31/binjgb-rewind.html) - Implementing a *rewind- feature.
- [binjgb on the web](https://binji.github.io/2017/02/26/binjgb-on-the-web-part-1.html) - Porting of the binjgb emulator to Web Assembly. [(Part 2)](https://binji.github.io/2017/02/27/binjgb-on-the-web-part-2.html)
- [binjgb debugging hangs](https://binji.github.io/2017/05/03/debugging-hangs.html) - Investigations on emulations quirks.
- [Decoding Gameboy Z80 opcodes](https://gb-archive.github.io/salvage/decoding_gbz80_opcodes/Decoding%20Gamboy%20Z80%20Opcodes.html) - How to algorithmically decode Game Boy instructions (as opposed to writing one huge switch-case statement).
- [Porting a GO Game Boy emulator to WebAssembly](https://djhworld.github.io/post/2018/09/21/i-ported-my-gameboy-color-emulator-to-webassembly/)
- [About swotGB](https://mitxela.com/projects/swotgb/about) - Notes about the development of a Game Boy emulator in JavaScript.
- [List of open source emulators](EMULATORS.md)
- [Game Boy Doctor](https://github.com/robert/gameboy-doctor) [![GitHub stars](https://img.shields.io/github/stars/robert/gameboy-doctor?style=flat)](https://github.com/robert/gameboy-doctor/stargazers) - A command line tool for comparing logs from your emulator to those from a known-correct one. Useful for line-by-line debugging of Blargg's test ROMs.

### Testing

- [Blargg's test roms](http://gbdev.gg8.se/files/roms/blargg-gb-tests/)
- [Gekkio's test roms](https://gekkio.fi/files/mooneye-gb/latest/)
- [SameSuite](https://github.com/LIJI32/SameSuite) [![GitHub stars](https://img.shields.io/github/stars/LIJI32/SameSuite?style=flat)](https://github.com/LIJI32/SameSuite/stargazers)
- [Mealybug Tearoom Tests](https://github.com/mattcurrie/mealybug-tearoom-tests) [![GitHub stars](https://img.shields.io/github/stars/mattcurrie/mealybug-tearoom-tests?style=flat)](https://github.com/mattcurrie/mealybug-tearoom-tests/stargazers)
- [GB Accuracy Tests](http://tasvideos.org/EmulatorResources/GBAccuracyTests.html)
- [144p Test Suite](https://github.com/pinobatch/240p-test-mini/tree/master/gameboy) [![GitHub stars](https://img.shields.io/github/stars/pinobatch/240p-test-mini/tree/master/gameboy?style=flat)](https://github.com/pinobatch/240p-test-mini/tree/master/gameboy/stargazers) - Port of Artemio Urbina's 240p Test Suite to the Game Boy.
- [MBC3 RTC test ROM](https://github.com/aaaaaa123456789/rtc3test) [![GitHub stars](https://img.shields.io/github/stars/aaaaaa123456789/rtc3test?style=flat)](https://github.com/aaaaaa123456789/rtc3test/stargazers)
- [dmg-acid2](https://github.com/mattcurrie/dmg-acid2) [![GitHub stars](https://img.shields.io/github/stars/mattcurrie/dmg-acid2?style=flat)](https://github.com/mattcurrie/dmg-acid2/stargazers) and [cgb-acid2](https://github.com/mattcurrie/cgb-acid2) [![GitHub stars](https://img.shields.io/github/stars/mattcurrie/cgb-acid2?style=flat)](https://github.com/mattcurrie/cgb-acid2/stargazers) - Basic PPU rendering tests.

## Software Development

The [Choosing tools for Game Boy development](https://gbdev.io/guides/tools.html) essay provides an overview of the available development tools for Game Boy.

### Assemblers

- [RGBDS](https://github.com/gbdev/rgbds) [![GitHub stars](https://img.shields.io/github/stars/gbdev/rgbds?style=flat)](https://github.com/gbdev/rgbds/stargazers) - Assembler and linker package. [Documentation](https://rgbds.gbdev.io).
- [ASMotor](https://github.com/csoren/asmotor) [![GitHub stars](https://img.shields.io/github/stars/csoren/asmotor?style=flat)](https://github.com/csoren/asmotor/stargazers) - Assembler engine and development system targeting Game Boy, among other CPUs. Written by the original RGBDS author. [Documentation](https://github.com/asmotor/asmotor/tree/develop#further-reading).
- [wla-dx](https://github.com/vhelin/wla-dx) [![GitHub stars](https://img.shields.io/github/stars/vhelin/wla-dx?style=flat)](https://github.com/vhelin/wla-dx/stargazers) - Yet Another GB-Z80/Z80/... Multi Platform Cross Assembler Package. [Documentation](http://www.villehelin.com/wla.txt).

### Compilers

- [GBDK](https://github.com/gbdk-2020/gbdk-2020/) [![GitHub stars](https://img.shields.io/github/stars/gbdk-2020/gbdk-2020/?style=flat)](https://github.com/gbdk-2020/gbdk-2020//stargazers) - Maintained and modernized GBDK (Game Boy Development Kit) powered by an updated version of the SDCC toolchain. Provides a C compiler, assembler, linker and a set of libraries. 
  - [API docs: Getting Started](https://gbdk-2020.github.io/gbdk-2020/docs/api/docs_getting_started.html)
  - [Examples](https://github.com/mrombout/gbdk_playground) [![GitHub stars](https://img.shields.io/github/stars/mrombout/gbdk_playground?style=flat)](https://github.com/mrombout/gbdk_playground/stargazers)
  - [Documentation, links and tools](https://gbdk-2020.github.io/gbdk-2020/docs/api/docs_links_and_tools.html)
- [Turbo Rascal Syntax Error](https://lemonspawn.com/turbo-rascal-syntax-error-expected-but-begin/) - Complete suite (IDE, compiler, programming language, resource editor) intended for developing games/demos for 8 / 16-bit line of computers, including the Game Boy and Game Boy Color.

#### Experimental/Proof of Concepts

- [RGBDS-Live](https://gbdev.io/rgbds-live) - In-browser coding environment to try out RGBDS.
- [Wiz](https://github.com/wiz-lang/wiz) [![GitHub stars](https://img.shields.io/github/stars/wiz-lang/wiz?style=flat)](https://github.com/wiz-lang/wiz/stargazers) - A high-level assembly language for writing homebrew on retro console platforms (Game Boy, NES, Atari 2600, and more).
- [gbforth](https://github.com/ams-hackers/gbforth) [![GitHub stars](https://img.shields.io/github/stars/ams-hackers/gbforth?style=flat)](https://github.com/ams-hackers/gbforth/stargazers) - A Forth-based Game Boy development kit.
- [gbasm-rs](https://gitlab.com/BonsaiDen/gbasm-rs) - An opinionated Rust based compiler for Game Boy z80 assembly code.
- [gbasm](https://github.com/BonsaiDen/gbasm) [![GitHub stars](https://img.shields.io/github/stars/BonsaiDen/gbasm?style=flat)](https://github.com/BonsaiDen/gbasm/stargazers) - A JavaScript based compiler for Game Boy z80 assembly code.
- [tniASM](http://www.tni.nl/products/tniasm.html) - Macro Assembler.
- [Assembler](https://github.com/ulrikdamm/Assembler) [![GitHub stars](https://img.shields.io/github/stars/ulrikdamm/Assembler?style=flat)](https://github.com/ulrikdamm/Assembler/stargazers) - Assembler written in Swift.
- [llvm-gbz80](https://github.com/Bevinsky/llvm-gbz80) [![GitHub stars](https://img.shields.io/github/stars/Bevinsky/llvm-gbz80?style=flat)](https://github.com/Bevinsky/llvm-gbz80/stargazers) / [clang-gbz80](https://github.com/Bevinsky/clang-gbz80) [![GitHub stars](https://img.shields.io/github/stars/Bevinsky/clang-gbz80?style=flat)](https://github.com/Bevinsky/clang-gbz80/stargazers) - Clang/LLVM port to the GBZ80 CPU (similar to the deprecated [euclio/llvm-gbz80](https://github.com/euclio/llvm-gbz80) [![GitHub stars](https://img.shields.io/github/stars/euclio/llvm-gbz80?style=flat)](https://github.com/euclio/llvm-gbz80/stargazers)).
- [gbdk-go](https://github.com/pokemium/gbdk-go) [![GitHub stars](https://img.shields.io/github/stars/pokemium/gbdk-go?style=flat)](https://github.com/pokemium/gbdk-go/stargazers) - A compiler translates Go programs to C code. The output C code is built into GB ROM by GBDK.
- [Rust-GB](https://github.com/zlfn/rust-gb) [![GitHub stars](https://img.shields.io/github/stars/zlfn/rust-gb?style=flat)](https://github.com/zlfn/rust-gb/stargazers) - A compiler and library that enable the development of GB ROMs using Rust.

### Emulators

- [BGB](https://bgb.bircd.org/) - Powerful emulator and debugger. Provides an accurate hardware emulation.
- [SameBoy](https://github.com/LIJI32/SameBoy) [![GitHub stars](https://img.shields.io/github/stars/LIJI32/SameBoy?style=flat)](https://github.com/LIJI32/SameBoy/stargazers) - Accurate emulator with a wide range of powerful debugging features.
- [Mooneye GB](https://github.com/Gekkio/mooneye-gb) [![GitHub stars](https://img.shields.io/github/stars/Gekkio/mooneye-gb?style=flat)](https://github.com/Gekkio/mooneye-gb/stargazers) - Research project and emulator in Rust.
- [mGBA](https://github.com/mgba-emu/mgba) [![GitHub stars](https://img.shields.io/github/stars/mgba-emu/mgba?style=flat)](https://github.com/mgba-emu/mgba/stargazers) - Modern cross platform GBA emulator which also runs GB/GBC games.
- [Binjgb](https://github.com/binji/binjgb) [![GitHub stars](https://img.shields.io/github/stars/binji/binjgb?style=flat)](https://github.com/binji/binjgb/stargazers) - 5Kloc emulator that passes most of the tests. *Rewind- feature. Runs in the browser using WebAssembly.
- [Gambatte](https://github.com/gb-archive/gambatte) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/gambatte?style=flat)](https://github.com/gb-archive/gambatte/stargazers) - Cross-platform and accurate emulator.

- [MetroBoy](https://github.com/aappleby/MetroBoy) [![GitHub stars](https://img.shields.io/github/stars/aappleby/MetroBoy?style=flat)](https://github.com/aappleby/MetroBoy/stargazers) - A playable, circuit-level simulation of an entire Game Boy.
- [gbe-plus](https://github.com/shonumi/gbe-plus) [![GitHub stars](https://img.shields.io/github/stars/shonumi/gbe-plus?style=flat)](https://github.com/shonumi/gbe-plus/stargazers) - A recently rewritten emulator that has a large effort in preserving the functions of obscure accessories (such as IR link, Mobile Network GB, Barcode Boy, GB Printer, local and online GB Serial Link Cable, ... )
- [Emulicious](https://emulicious.net/) - Provides accurate emulation and includes powerful tools such as a profiler and source-level debugging for ASM and C via a [VS Code debug adapter](https://marketplace.visualstudio.com/items?itemName=emulicious.emulicious-debugger).

[Complete list of open source emulators](EMULATORS.md)

### Tools

#### Engines

- [ZGB](https://github.com/Zal0/ZGB) [![GitHub stars](https://img.shields.io/github/stars/Zal0/ZGB?style=flat)](https://github.com/Zal0/ZGB/stargazers) - A little engine for creating games for the original Game Boy (expands gbdk, more info [here](http://zalods.blogspot.com/2017/01/zgb-little-engine-for-game-boy.html)).
- [Retr0 GB](https://bitbucket.org/HellSuffering/retr0-gb/) - An engine for creating games (expands GBDK).

#### Development tools

- [GBExtended](https://www.tensi.eu/thomas/programming/utilities/gbx_library/gbx_library.html) - C library extending gbdk.
- [gbdk-lib-extension](https://github.com/ProGM/gbdk-lib-extension) [![GitHub stars](https://img.shields.io/github/stars/ProGM/gbdk-lib-extension?style=flat)](https://github.com/ProGM/gbdk-lib-extension/stargazers) - A small set of sources and tools for the Game Boy Development Kit by Michael Hope.
- [mgbdis](https://github.com/mattcurrie/mgbdis) [![GitHub stars](https://img.shields.io/github/stars/mattcurrie/mgbdis?style=flat)](https://github.com/mattcurrie/mgbdis/stargazers) - Game Boy ROM disassembler with RGBDS compatible output.
- [ROM Header Utility](http://catskull.net/GB-Logo-Generator/) - An online tool to inspect and modify a ROM's header data, including the logo.
- [romusage](https://github.com/bbbbbr/romusage) [![GitHub stars](https://img.shields.io/github/stars/bbbbbr/romusage?style=flat)](https://github.com/bbbbbr/romusage/stargazers) - Command line tool for estimating usage (free space) of Game Boy ROMs from a .map, .noi or ihx file. Works with GBDK-2020 and RGBDS.
- [awake](https://github.com/devdri/awake) [![GitHub stars](https://img.shields.io/github/stars/devdri/awake?style=flat)](https://github.com/devdri/awake/stargazers) - Game Boy decompiler.
- [Game Boy Text Tools](https://github.com/raphaklaus/gameboy-text-tools) [![GitHub stars](https://img.shields.io/github/stars/raphaklaus/gameboy-text-tools?style=flat)](https://github.com/raphaklaus/gameboy-text-tools/stargazers) - Set of tools for text manipulation and translation of Game Boy ROMs written in Node.js.
- [evscript](https://github.com/eievui5/evscript) [![GitHub stars](https://img.shields.io/github/stars/eievui5/evscript?style=flat)](https://github.com/eievui5/evscript/stargazers) - A scripting language for the Game Boy, useful for enemy AI, dialogue, animations, and coroutines.
- [evunit](https://github.com/eievui5/evunit) [![GitHub stars](https://img.shields.io/github/stars/eievui5/evunit?style=flat)](https://github.com/eievui5/evunit/stargazers) - A unit testing program for assembly code.
- [opcode_count](https://github.com/rondnelson99/opcode_count) [![GitHub stars](https://img.shields.io/github/stars/rondnelson99/opcode_count?style=flat)](https://github.com/rondnelson99/opcode_count/stargazers) - Generates statistics on which CPU instructions are run the most often using Python and Emulicious

#### Graphics utilities

- [Game Boy Tile Data Generator](https://github.com/chrisantonellis/gbtdg) [![GitHub stars](https://img.shields.io/github/stars/chrisantonellis/gbtdg?style=flat)](https://github.com/chrisantonellis/gbtdg/stargazers) - HTML5 / JS web application that will convert bitmap images to hexadecimal data appropriate for use in tile based graphical applications, specifically GB.
- [Harry Mulder's GB Development](http://www.devrs.com/gb/hmgd/intro.html) - Some sources and home of Game Boy Tile Designer (GBTD) and Game Boy Map Builder (GBMB) tools.
- [GBTiles](https://github.com/bashaus/gbtiles) [![GitHub stars](https://img.shields.io/github/stars/bashaus/gbtiles?style=flat)](https://github.com/bashaus/gbtiles/stargazers) - Converts .GBR files created with Harry Mulder's Tile Designer (GBTD) and .GBM files created with Harry Mulder's Map Builder (GBMB) to different formats for use with the Game Boy and GBDK.
- [bmp2cgb](https://github.com/gitendo/bmp2cgb) [![GitHub stars](https://img.shields.io/github/stars/gitendo/bmp2cgb?style=flat)](https://github.com/gitendo/bmp2cgb/stargazers) - Graphics converter for Game Boy Color development providing real time palette adjustments.
- [png2gb](https://github.com/LuckyLights/png2gb) [![GitHub stars](https://img.shields.io/github/stars/LuckyLights/png2gb?style=flat)](https://github.com/LuckyLights/png2gb/stargazers) - CLI tool to convert image file to game boy .c array.
- [GB-convert](https://github.com/gb-archive/gb-convert) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/gb-convert?style=flat)](https://github.com/gb-archive/gb-convert/stargazers) - Game Boy tile conversion and map editor tool (converts to assembly).
- [brewtool](http://make.vg/brewtool/) - A collection of primitive editor/converter tools for making assets used with homebrew ROM development.
- [vtGBte](https://github.com/paul-arutyunov/vtGBte) [![GitHub stars](https://img.shields.io/github/stars/paul-arutyunov/vtGBte?style=flat)](https://github.com/paul-arutyunov/vtGBte/stargazers) - A minimalistic ncurses tile editor.
- [tpp1](https://github.com/TwitchPlaysPokemon/tpp1) [![GitHub stars](https://img.shields.io/github/stars/TwitchPlaysPokemon/tpp1?style=flat)](https://github.com/TwitchPlaysPokemon/tpp1/stargazers) - Definition and specification of a custom GB/GBC memory/hardware mapper, as a functional superset of MBC.
- [libstdgb](https://github.com/delwink/libstdgb) [![GitHub stars](https://img.shields.io/github/stars/delwink/libstdgb?style=flat)](https://github.com/delwink/libstdgb/stargazers) - A C library of useful Game Boy operations (SDCC).
- [Tilemap GB](https://github.com/bbbbbr/gimp-tilemap-gb) [![GitHub stars](https://img.shields.io/github/stars/bbbbbr/gimp-tilemap-gb?style=flat)](https://github.com/bbbbbr/gimp-tilemap-gb/stargazers) - GIMP image editor plug-in for importing & exporting GBMB and GBTD tilemaps and tilesets (as bitmap images or .GBM/.GBR files).
- [Tilemap Helper](https://github.com/bbbbbr/gimp-tilemap-helper) [![GitHub stars](https://img.shields.io/github/stars/bbbbbr/gimp-tilemap-helper?style=flat)](https://github.com/bbbbbr/gimp-tilemap-helper/stargazers) - GIMP image editor plug-in for optimizing tile maps and tile sets.
- [Tilemap Studio](https://github.com/Rangi42/tilemap-studio) [![GitHub stars](https://img.shields.io/github/stars/Rangi42/tilemap-studio?style=flat)](https://github.com/Rangi42/tilemap-studio/stargazers) - A tilemap editor for Game Boy, Color, Advance, and SNES projects. Written in C++ with FLTK. 
- [Superfamiconv](https://github.com/Optiroc/SuperFamiconv) [![GitHub stars](https://img.shields.io/github/stars/Optiroc/SuperFamiconv?style=flat)](https://github.com/Optiroc/SuperFamiconv/stargazers) - Flexible and composable tile graphics converter supporting Super Nintendo, Game Boy, Game Boy Color, Game Boy Advance, Mega Drive and PC Engine formats.

#### Hardware and ROM utilities

- [cart-dumper](https://github.com/Palmr/cart-dumper) [![GitHub stars](https://img.shields.io/github/stars/Palmr/cart-dumper?style=flat)](https://github.com/Palmr/cart-dumper/stargazers) - Game Boy Cartridge Dumper ROM.
- [gbcamextract](https://github.com/jkbenaim/gbcamextract) [![GitHub stars](https://img.shields.io/github/stars/jkbenaim/gbcamextract?style=flat)](https://github.com/jkbenaim/gbcamextract/stargazers) - Extracts photos from Game Boy Camera saves.
- [Game Boy LCD sniffing](https://github.com/svendahlstrand/game-boy-lcd-sniffing) [![GitHub stars](https://img.shields.io/github/stars/svendahlstrand/game-boy-lcd-sniffing?style=flat)](https://github.com/svendahlstrand/game-boy-lcd-sniffing/stargazers) - Sniff your Game Boy's LCD using a logic analyzer.
- [swapdump](https://github.com/sanqui/swapdump) [![GitHub stars](https://img.shields.io/github/stars/sanqui/swapdump?style=flat)](https://github.com/sanqui/swapdump/stargazers) - Diagnostic utility for Game Boy flashcarts.
- [Gameboy-LinkUp](https://github.com/JustinLloyd/Gameboy-LinkUp) [![GitHub stars](https://img.shields.io/github/stars/JustinLloyd/Gameboy-LinkUp?style=flat)](https://github.com/JustinLloyd/Gameboy-LinkUp/stargazers) - Game Boy LinkUp serial cable networking project.

#### Music drivers and trackers

- [DevSoundX](https://github.com/DevEd2/DevSoundX) [![GitHub stars](https://img.shields.io/github/stars/DevEd2/DevSoundX?style=flat)](https://github.com/DevEd2/DevSoundX/stargazers) - Sound driver embeddable in homebrews which supports pulse width manipulation, arpeggios, and multiple waveforms.
- [Carillon Player](http://gbdev.gg8.se/files/musictools/Aleksi%20Eeben/Carillon%20Editor.zip) - Music Engine.
- [GBT PLAYER](https://github.com/AntonioND/gbt-player) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/gbt-player?style=flat)](https://github.com/AntonioND/gbt-player/stargazers) - A music player library and converter kit.
- [mmlgb](https://github.com/SimonLarsen/mmlgb) [![GitHub stars](https://img.shields.io/github/stars/SimonLarsen/mmlgb?style=flat)](https://github.com/SimonLarsen/mmlgb/stargazers) - A MML parser and GBDK sound driver for the Nintendo Game Boy.
- [XPMCK](https://github.com/bazzinotti/XPMCK) [![GitHub stars](https://img.shields.io/github/stars/bazzinotti/XPMCK?style=flat)](https://github.com/bazzinotti/XPMCK/stargazers) - An MML based music compiler with support for Game Boy & Game Boy Color.
- [GBSoundSystem](https://github.com/gbdev/GBSoundSystem) [![GitHub stars](https://img.shields.io/github/stars/gbdev/GBSoundSystem?style=flat)](https://github.com/gbdev/GBSoundSystem/stargazers) - A modernized audio driver for GameBoy Tracker (aka the Paragon 5 music player).
- [hUGETracker](https://github.com/SuperDisk/hUGETracker) [![GitHub stars](https://img.shields.io/github/stars/SuperDisk/hUGETracker?style=flat)](https://github.com/SuperDisk/hUGETracker/stargazers) - A music tracker based on OpenMPT, focused on ease of use, compact output, and embeddability in homebrew games.
- [CBT-FX](https://github.com/datguywitha3ds/CBT-FX) [![GitHub stars](https://img.shields.io/github/stars/datguywitha3ds/CBT-FX?style=flat)](https://github.com/datguywitha3ds/CBT-FX/stargazers) - A GBDK-2020 sound effect driver compatible with FX-Hammer sound effects.

## Programming

Guides, tutorials and tools to develop software for Game Boy using the development toolchains described in the [Software Development](#software-development) chapter.

### ASM

- **[gb asm tutorial](https://gbdev.io/gb-asm-tutorial)** - Step by step tutorial, building several ROMs to accompany its explanations.
- [hardware.inc](https://github.com/tobiasvl/hardware.inc) [![GitHub stars](https://img.shields.io/github/stars/tobiasvl/hardware.inc?style=flat)](https://github.com/tobiasvl/hardware.inc/stargazers) - Standard include file containing Game Boy hardware definitions for use in RGBDS projects.
- [Assembly tutorial by David Pello](https://gb-archive.github.io/salvage/tutorial_de_ensamblador/tutorial_de_ensamblador_la_decadence.html) - Good document to learn to produce working asm code for gb. Brief explanations of many important topics. Many examples with commented source code.
- [assemblydigest](https://github.com/assemblydigest/gameboy) [![GitHub stars](https://img.shields.io/github/stars/assemblydigest/gameboy?style=flat)](https://github.com/assemblydigest/gameboy/stargazers) - Exploring Game Boy programming techniques:
  - [Making an Empty Game Boy ROM (in Wiz)](https://assemblydigest.tumblr.com/post/77203696711/tutorial-making-an-empty-game-boy-rom-in-wiz)
  - [Making Art for the Game Boy](https://assemblydigest.tumblr.com/post/77404621743/tutorial-making-art-for-the-game-boy)
- [Beginner's Guide to Reverse Engineering GB](http://web.archive.org/web/20150511145100/http://www.bennvenn.com/Beginners_Guide_To_Reverse_Engineering.htm) - Some starting tips on disassembling and reverse engineering.
- [FlappyBoy: Making a simple Game Boy Game](http://voidptr.io/blog/2017/01/21/GameBoy.html)
- [Super Game Boy development](https://imanoleasgames.blogspot.no/2016/12/games-aside-1-super-game-boy.html) - Step by step tutorial to implement Super Game Boy features (frame and palettes).
- [GameBoy programming tutorial: Hello World!](https://peterwynroberts.wordpress.com/2014/05/11/gameboy-programming-tutorial-hello-world/) - Step by step tutorial.
- [DMGreport](https://github.com/lancekindle/DMGreport) [![GitHub stars](https://img.shields.io/github/stars/lancekindle/DMGreport?style=flat)](https://github.com/lancekindle/DMGreport/stargazers) - Game programming tutorials in assembly.
- [OAM DMA tutorial](https://gbdev.gg8.se/wiki/articles/OAM_DMA_tutorial) - Example of how to use OAM DMA in assembly.
- [Game Boy Assembly Programming for the Modern Game Developer](https://github.com/ahrnbom/gbapfomgd) [![GitHub stars](https://img.shields.io/github/stars/ahrnbom/gbapfomgd?style=flat)](https://github.com/ahrnbom/gbapfomgd/stargazers) - An e-book about making Game Boy games in Assembly.

#### Sources

Fragments of code, effects, proof of concepts and generally non complete games.

- [dev'rs ASM section](https://web.archive.org/web/20250329180046/http://www.devrs.com/gb/asmcode.php) - A lot of working demos and sources.
- [EmmaEwert's experiments](https://github.com/EmmaEwert/gameboy) [![GitHub stars](https://img.shields.io/github/stars/EmmaEwert/gameboy?style=flat)](https://github.com/EmmaEwert/gameboy/stargazers) - A collection of prototype programs, mostly just toying around. Among others, a daylight effect, transparency and a weather effect.
- [DeadCScroll](https://github.com/gb-archive/DeadCScroll) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/DeadCScroll?style=flat)](https://github.com/gb-archive/DeadCScroll/stargazers) - A detailed tutorial on how to make the screen wobble, among other "raster effects"

#### Timings

- [Nitty Gritty Gameboy Cycle Timing](http://blog.kevtris.org/blogfiles/Nitty%20Gritty%20Gameboy%20VRAM%20Timing.txt)
- [Mode3 Sprite Timing](https://old.reddit.com/r/EmuDev/comments/59pawp/gb_mode3_sprite_timing/)
- [GameBoy Color DMA-Transfers v0.0.1](http://gameboy.mongenel.com/dmg/gbc_dma_transfers.txt)
- [STAT interrupt timings](http://gameboy.mongenel.com/dmg/istat98.txt)
- [Video Timing](https://github.com/jdeblese/gbcpu/wiki/Video-Timing) [![GitHub stars](https://img.shields.io/github/stars/jdeblese/gbcpu/wiki/Video-Timing?style=flat)](https://github.com/jdeblese/gbcpu/wiki/Video-Timing/stargazers)

#### Boilerplates and libraries

- [rgbds-template](https://github.com/nezticle/rgbds-template) [![GitHub stars](https://img.shields.io/github/stars/nezticle/rgbds-template?style=flat)](https://github.com/nezticle/rgbds-template/stargazers) - Basic hello-world example for Game Boy using RGBDS.
- [Game Boy Assembly Language Primer](http://www.devrs.com/gb/files/galp.zip) - Simple template code with memory defines, copy routines and IBM font tilemap.
- [bootstrap.gb](https://github.com/yenatch/bootstrap.gb) [![GitHub stars](https://img.shields.io/github/stars/yenatch/bootstrap.gb?style=flat)](https://github.com/yenatch/bootstrap.gb/stargazers) - An example Game Boy project.
- [Gameboy Boilerplate](https://github.com/junebug12851/GameboyBoilerplateProj) [![GitHub stars](https://img.shields.io/github/stars/junebug12851/GameboyBoilerplateProj?style=flat)](https://github.com/junebug12851/GameboyBoilerplateProj/stargazers) - Boilerplate project to move quicker into the actual assembly code for your game.
- [GingerBread](https://github.com/ahrnbom/gingerbread) [![GitHub stars](https://img.shields.io/github/stars/ahrnbom/gingerbread?style=flat)](https://github.com/ahrnbom/gingerbread/stargazers) - A software library for making your own Game Boy games. It is made to be used alongside the book [Game Boy Assembly Programming for the Modern Game Developer](https://github.com/ahrnbom/gbapfomgd) [![GitHub stars](https://img.shields.io/github/stars/ahrnbom/gbapfomgd?style=flat)](https://github.com/ahrnbom/gbapfomgd/stargazers) which also doubles as documentation.
- [gb-vwf](https://github.com/ISSOtm/gb-vwf) [![GitHub stars](https://img.shields.io/github/stars/ISSOtm/gb-vwf?style=flat)](https://github.com/ISSOtm/gb-vwf/stargazers) - Library to print variable-width text, comes with a demo.
- [gb-boilerplate](https://github.com/ISSOtm/gb-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/ISSOtm/gb-boilerplate?style=flat)](https://github.com/ISSOtm/gb-boilerplate/stargazers) - A template for starting Game Boy projects, providing a Makefile for infrastructure.
- [gb-starter-kit](https://github.com/ISSOtm/gb-starter-kit) [![GitHub stars](https://img.shields.io/github/stars/ISSOtm/gb-starter-kit?style=flat)](https://github.com/ISSOtm/gb-starter-kit/stargazers) - An expansion on the above, including base library code as well to get started faster.
- [gb-template](https://github.com/gb-archive/gb-template) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/gb-template?style=flat)](https://github.com/gb-archive/gb-template/stargazers) - A template with basic functions such as joypad input, DMA transfers, and map/tile data loading.

#### Syntax highlighting packages

- [gbz80-highlight](https://github.com/ISSOtm/gbz80-highlight) [![GitHub stars](https://img.shields.io/github/stars/ISSOtm/gbz80-highlight?style=flat)](https://github.com/ISSOtm/gbz80-highlight/stargazers) - Notepad+- and gedit syntax highlighting files for RGBDS assembly.
- [Vim syntax file for the Game Boy assembler RGBASM](http://www.vim.org/scripts/script.php?script_id=819) - Vim syntax highlighting for RGBDS assembly.
- [Vim syntax file for RGBDS](https://github.com/Leandros/dotfiles/blob/master/.vim/syntax/rgbds.vim) [![GitHub stars](https://img.shields.io/github/stars/Leandros/dotfiles/blob/master/.vim/syntax/rgbds.vim?style=flat)](https://github.com/Leandros/dotfiles/blob/master/.vim/syntax/rgbds.vim/stargazers) - Another Vim syntax highlighting file for RGBDS assembly.
- [sublime-rgbds](https://packagecontrol.io/packages/RGBDS) - A Sublime Text 3 package for RGBDS, including syntax highlighting and some completion snippets.
- [Z80 Assembly support for Visual Studio Code](https://github.com/Imanolea/z80asm-vscode) [![GitHub stars](https://img.shields.io/github/stars/Imanolea/z80asm-vscode?style=flat)](https://github.com/Imanolea/z80asm-vscode/stargazers)
- [rgbds-vscode](https://github.com/DonaldHays/rgbds-vscode) [![GitHub stars](https://img.shields.io/github/stars/DonaldHays/rgbds-vscode?style=flat)](https://github.com/DonaldHays/rgbds-vscode/stargazers) - Visual Studio Code language extension for RGBDS GBZ80 Assembly.
- [rgbds-mode](https://github.com/japanoise/rgbds-mode) [![GitHub stars](https://img.shields.io/github/stars/japanoise/rgbds-mode?style=flat)](https://github.com/japanoise/rgbds-mode/stargazers) - Emacs major mode for RGBDS assembly.

### C

- [8-Bit Wonderland](https://github.com/gb-archive/salvage/blob/master/misc/8bit_wonderland.pdf) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/salvage/blob/master/misc/8bit_wonderland.pdf?style=flat)](https://github.com/gb-archive/salvage/blob/master/misc/8bit_wonderland.pdf/stargazers) - Well-written introductory document about how the Game Boy works and how to start developing working code for it.
- [Grooves Game Boy Programming](https://github.com/gbdk-salvage/grooves-game-boy-programming) [![GitHub stars](https://img.shields.io/github/stars/gbdk-salvage/grooves-game-boy-programming?style=flat)](https://github.com/gbdk-salvage/grooves-game-boy-programming/stargazers) - A complete set of lessons about implementing various game mechanics in a Game Boy game.
- [How to Write a Simple Side Scrolling Game](http://pastebin.com/F3tHLj68) - Old (but still relevant) tutorial.
- [Just another simple tutorial](http://web.archive.org/web/20230327070526/http://pastebin.com/gzT47MPJ)
- [GBDK Tutorial](https://refreshgames.co.uk/2016/04/18/gameboy-tutorial-rom/) - Fairly minimal game demo for getting started with GBDK.
- [GBDK Sprite](http://gbdev.gg8.se/wiki/articles/GBDK_Sprite_Tutorial) - Presents a workflow for getting multiple sprites to display and animate.
- [GBDK Color](http://gbdev.gg8.se/wiki/articles/GBDK_Color_Tutorial) - Extends your knowledge of basic spriting on the Game Boy by adding colors to sprites, backgrounds and the window layer.
- [GBDK Joypad](http://gbdev.gg8.se/wiki/articles/GBDK_Joypad_Tutorial) - Details the use of the joypad with GBDK.
- [Game Boy home of Flavor](https://web.archive.org/web/20210427064949/www.personal.triticom.com/~erm/GameBoy/) - Some full games and sources.
- [GBDK Configuring and Programming Tutorial](https://videlais.com/2016/07/03/programming-game-boy-games-using-gbdk-part-1-configuring-programming-and-compiling/) - Configuring GBDK, Using Tiles, Colliding Sprites, GBTD, GBMB, Memory Management and ROM Banking.
- [Simplified GBDK examples](https://github.com/mrombout/gbdk_playground) [![GitHub stars](https://img.shields.io/github/stars/mrombout/gbdk_playground?style=flat)](https://github.com/mrombout/gbdk_playground/stargazers)
- [GBDK Programming Video Tutorials](https://www.youtube.com/playlist?list=PLeEj4c2zF7PaFv5MPYhNAkBGrkx4iPGJo) - A series of video tutorials introducing beginners to programming with GBDK.
- [Larold's Retro Gameyard](https://laroldsretrogameyard.com/category/tutorials/gb/) - A collection of detailed GBDK-2020 based tutorials.

## Homebrews

Complete and open source games.

- [Homebrew Hub](https://hh.gbdev.io) - A community-led attempt to collect, archive and preserve every unlicensed and homebrew game released for Game Boy. Entries are playable online.

### ASM

- [Tuff](https://github.com/BonsaiDen/Tuff.gb) [![GitHub stars](https://img.shields.io/github/stars/BonsaiDen/Tuff.gb?style=flat)](https://github.com/BonsaiDen/Tuff.gb/stargazers)
- [2048-gb](https://github.com/Sanqui/2048-gb) [![GitHub stars](https://img.shields.io/github/stars/Sanqui/2048-gb?style=flat)](https://github.com/Sanqui/2048-gb/stargazers)
- [Snake](https://bitbucket.org/Sanqui/snake/src/?at=master)
- [Lazerpong](https://github.com/huderlem/lazerpong) [![GitHub stars](https://img.shields.io/github/stars/huderlem/lazerpong?style=flat)](https://github.com/huderlem/lazerpong/stargazers)
- [Geometrix](https://github.com/AntonioND/geometrix) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/geometrix?style=flat)](https://github.com/AntonioND/geometrix/stargazers)
- [µCity](https://github.com/AntonioND/ucity) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/ucity?style=flat)](https://github.com/AntonioND/ucity/stargazers)
- [Carazu](https://github.com/mholtkamp/carazu) [![GitHub stars](https://img.shields.io/github/stars/mholtkamp/carazu?style=flat)](https://github.com/mholtkamp/carazu/stargazers)
- [Snake-gb](https://github.com/DonaldHays/snake-gb) [![GitHub stars](https://img.shields.io/github/stars/DonaldHays/snake-gb?style=flat)](https://github.com/DonaldHays/snake-gb/stargazers)
- [GB303](https://github.com/furrtek/GB303) [![GitHub stars](https://img.shields.io/github/stars/furrtek/GB303?style=flat)](https://github.com/furrtek/GB303/stargazers) - GB303 wavetable-based TB-303 style synthesizer for the Nintendo Game Boy.
- [Sushi](https://github.com/JustSid/Sushi) [![GitHub stars](https://img.shields.io/github/stars/JustSid/Sushi?style=flat)](https://github.com/JustSid/Sushi/stargazers)
- [Flappy-boy-asm](https://github.com/bitnenfer/flappy-boy-asm) [![GitHub stars](https://img.shields.io/github/stars/bitnenfer/flappy-boy-asm?style=flat)](https://github.com/bitnenfer/flappy-boy-asm/stargazers)
- [kupman](https://github.com/dubvulture/gbdev) [![GitHub stars](https://img.shields.io/github/stars/dubvulture/gbdev?style=flat)](https://github.com/dubvulture/gbdev/stargazers) and some other projects.
- [Adjustris](https://github.com/tbsp/Adjustris) [![GitHub stars](https://img.shields.io/github/stars/tbsp/Adjustris?style=flat)](https://github.com/tbsp/Adjustris/stargazers)
- [exeman](https://github.com/gb-archive/exeman) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/exeman?style=flat)](https://github.com/gb-archive/exeman/stargazers)
- [Aevilia](https://github.com/ISSOtm/Aevilia-GB) [![GitHub stars](https://img.shields.io/github/stars/ISSOtm/Aevilia-GB?style=flat)](https://github.com/ISSOtm/Aevilia-GB/stargazers)
- [GBSlides](https://github.com/Kartones/gameboy) [![GitHub stars](https://img.shields.io/github/stars/Kartones/gameboy?style=flat)](https://github.com/Kartones/gameboy/stargazers) - A simple Game Boy Powerpoint-like slides viewer.
- [Pokered-gbc](https://github.com/dannye/pokered-gbc) [![GitHub stars](https://img.shields.io/github/stars/dannye/pokered-gbc?style=flat)](https://github.com/dannye/pokered-gbc/stargazers) - Pokémon Red remade with full GBC support.
- [ToyToy](https://github.com/tslanina/Retro-GameBoyColor-ToyToy) [![GitHub stars](https://img.shields.io/github/stars/tslanina/Retro-GameBoyColor-ToyToy?style=flat)](https://github.com/tslanina/Retro-GameBoyColor-ToyToy/stargazers)
- [StefaN](https://github.com/tslanina/Retro-GameBoyColor-StefaN) [![GitHub stars](https://img.shields.io/github/stars/tslanina/Retro-GameBoyColor-StefaN?style=flat)](https://github.com/tslanina/Retro-GameBoyColor-StefaN/stargazers) - Fourway Breakout clone.
- [Galaxia](https://github.com/tslanina/Retro-GameBoyColor-Galaxia) [![GitHub stars](https://img.shields.io/github/stars/tslanina/Retro-GameBoyColor-Galaxia?style=flat)](https://github.com/tslanina/Retro-GameBoyColor-Galaxia/stargazers)
- [desgb](https://github.com/sanqui/desgb) [![GitHub stars](https://img.shields.io/github/stars/sanqui/desgb?style=flat)](https://github.com/sanqui/desgb/stargazers) - DES encryption.
- [superhappyfunbubbletime](https://github.com/l0k1/superhappyfunbubbletime) [![GitHub stars](https://img.shields.io/github/stars/l0k1/superhappyfunbubbletime?style=flat)](https://github.com/l0k1/superhappyfunbubbletime/stargazers)
- [minesweepGB](https://github.com/lancekindle/minesweepGB) [![GitHub stars](https://img.shields.io/github/stars/lancekindle/minesweepGB?style=flat)](https://github.com/lancekindle/minesweepGB/stargazers)
- [Libbet and the Magic Floor](https://github.com/pinobatch/libbet) [![GitHub stars](https://img.shields.io/github/stars/pinobatch/libbet?style=flat)](https://github.com/pinobatch/libbet/stargazers)
- [waveform-gb](https://github.com/dannye/waveform-gb) [![GitHub stars](https://img.shields.io/github/stars/dannye/waveform-gb?style=flat)](https://github.com/dannye/waveform-gb/stargazers) - Program visualizing the wave form used by the wave channel. The wave form can be edited freely and playback of the wave is updated immediately.
- [vectroid.gb](https://gitlab.com/BonsaiDen/vectroid.gb) - Developed with gbasm.
- [PlantBoy](https://github.com/gb-archive/plantboy) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/plantboy?style=flat)](https://github.com/gb-archive/plantboy/stargazers)
- [Death Planet](https://makrill.itch.io/death-planet)
- [Quartet](https://makrill.itch.io/quartet) - Puzzle game for the Game Boy (Color) and Super Game Boy.
- [Dangan](https://snorpung.itch.io/dangan-gb)

### C

- [FlappyBoy](https://github.com/bitnenfer/FlappyBoy) [![GitHub stars](https://img.shields.io/github/stars/bitnenfer/FlappyBoy?style=flat)](https://github.com/bitnenfer/FlappyBoy/stargazers)
- [flappybird-gameboy](https://github.com/pashutk/flappybird-gameboy) [![GitHub stars](https://img.shields.io/github/stars/pashutk/flappybird-gameboy?style=flat)](https://github.com/pashutk/flappybird-gameboy/stargazers)
- [fbgb](https://github.com/gb-archive/fbgb) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/fbgb?style=flat)](https://github.com/gb-archive/fbgb/stargazers)
- [Novascape](https://web.archive.org/web/20171002042716/http://ludumdare.com/compo/ludum-dare-34/?action=preview&uid=6823)
- [Squishy the Turtle](https://github.com/cppchriscpp/SquishyTheTurtle) [![GitHub stars](https://img.shields.io/github/stars/cppchriscpp/SquishyTheTurtle?style=flat)](https://github.com/cppchriscpp/SquishyTheTurtle/stargazers)
- [Quadratino](https://github.com/avivace/quadratino) [![GitHub stars](https://img.shields.io/github/stars/avivace/quadratino?style=flat)](https://github.com/avivace/quadratino/stargazers)
- [Doctor How](https://github.com/elfgames/doctorhow) [![GitHub stars](https://img.shields.io/github/stars/elfgames/doctorhow?style=flat)](https://github.com/elfgames/doctorhow/stargazers)
- [Super Princess' 2092 Exodus](https://github.com/Zal0/gbjam2016) [![GitHub stars](https://img.shields.io/github/stars/Zal0/gbjam2016?style=flat)](https://github.com/Zal0/gbjam2016/stargazers) - ([ZGB engine](https://github.com/Zal0/ZGB/) [![GitHub stars](https://img.shields.io/github/stars/Zal0/ZGB/?style=flat)](https://github.com/Zal0/ZGB//stargazers)).
- [GBsnake](https://github.com/brovador/GBsnake) [![GitHub stars](https://img.shields.io/github/stars/brovador/GBsnake?style=flat)](https://github.com/brovador/GBsnake/stargazers)
- [gb-mines](https://github.com/andreasjhkarlsson/gb-mines) [![GitHub stars](https://img.shields.io/github/stars/andreasjhkarlsson/gb-mines?style=flat)](https://github.com/andreasjhkarlsson/gb-mines/stargazers)
- [oranges](http://www.atari2600land.com/gameboy/oranges.html)
- [red hot princess carnage](https://github.com/Imanolea/bitbitjam3_red_hot_princess_carnage) [![GitHub stars](https://img.shields.io/github/stars/Imanolea/bitbitjam3_red_hot_princess_carnage?style=flat)](https://github.com/Imanolea/bitbitjam3_red_hot_princess_carnage/stargazers)
- [loderunner](https://www.tensi.eu/thomas/programming/games/loderunner/loderunner.html)
- [Hives](https://refreshgames.co.uk/2017/04/24/ludum-dare-38-entry-hives/)
- [Bubble Factory](https://github.com/DonaldHays/bubblefactory) [![GitHub stars](https://img.shields.io/github/stars/DonaldHays/bubblefactory?style=flat)](https://github.com/DonaldHays/bubblefactory/stargazers) - *Vanilla- SDCC (no gbdk).
- [GBC Atari Boxing](https://github.com/rubfi/gbc-atari-boxing) [![GitHub stars](https://img.shields.io/github/stars/rubfi/gbc-atari-boxing?style=flat)](https://github.com/rubfi/gbc-atari-boxing/stargazers) - Atari 2600 Boxing clone for the Game Boy (Color).
- [GB raycaster, Vision-8](https://github.com/haroldo-ok/really-old-stuff/tree/master/gameboy) [![GitHub stars](https://img.shields.io/github/stars/haroldo-ok/really-old-stuff/tree/master/gameboy?style=flat)](https://github.com/haroldo-ok/really-old-stuff/tree/master/gameboy/stargazers) - and some other projects.
- [Tobu Tobu Girl Deluxe](https://github.com/SimonLarsen/tobutobugirl-dx) [![GitHub stars](https://img.shields.io/github/stars/SimonLarsen/tobutobugirl-dx?style=flat)](https://github.com/SimonLarsen/tobutobugirl-dx/stargazers) - An arcade platformer for the Game Boy (Color).
- [Burly Bear vs. The Mean Foxes](http://sebastianmihai.com/gameboy-burly-bear.html) ([GBC](http://sebastianmihai.com/gameboy-color-burly-bear.html) port)
- [PostBot](https://github.com/MasterIV/PostBot) [![GitHub stars](https://img.shields.io/github/stars/MasterIV/PostBot?style=flat)](https://github.com/MasterIV/PostBot/stargazers)
- [Guns & Riders](https://github.com/kanfor/gunsridersgameboy) [![GitHub stars](https://img.shields.io/github/stars/kanfor/gunsridersgameboy?style=flat)](https://github.com/kanfor/gunsridersgameboy/stargazers)
- [Dino's Offline Adventure](https://github.com/gingemonster/DinosOfflineAdventure) [![GitHub stars](https://img.shields.io/github/stars/gingemonster/DinosOfflineAdventure?style=flat)](https://github.com/gingemonster/DinosOfflineAdventure/stargazers) - A clone of the Google Chrome offline game.
- [dino-gb](https://github.com/rnegron/dino-gb) [![GitHub stars](https://img.shields.io/github/stars/rnegron/dino-gb?style=flat)](https://github.com/rnegron/dino-gb/stargazers) - Another clone of the Chrome game.
- [Evoland.gb](https://github.com/flozz/evoland.gb) [![GitHub stars](https://img.shields.io/github/stars/flozz/evoland.gb?style=flat)](https://github.com/flozz/evoland.gb/stargazers) - A port of the first level of Evoland.
- [Petris](https://github.com/bbbbbr/Petris) [![GitHub stars](https://img.shields.io/github/stars/bbbbbr/Petris?style=flat)](https://github.com/bbbbbr/Petris/stargazers) - A puzzle game of shapely pets for the Game Boy Color ([itch.io](https://bbbbbr.itch.io/petris)).
- [Infinity](https://github.com/gb-archive/infinity-gbc) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/infinity-gbc?style=flat)](https://github.com/gb-archive/infinity-gbc/stargazers) - RPG developed by Affinix Software primarily between the years 1999 and 2001. The game never found a publisher and was eventually canceled. Got recently released with the full source, development tools and workflows.
- [Black Castle](https://gbdev.gg8.se/forums/viewtopic.php?id=743) - Side scrolling platformer for the Game Boy ([itch.io](https://user0x7f.itch.io/black-castle)).
- [Genesis](https://gbdev.gg8.se/forums/viewtopic.php?id=674) - Shmup for the Game Boy ([itch.io](https://user0x7f.itch.io/genesis)).
- [Indestructo Tank!](https://antonylavelle.itch.io/indestructotank-gb)
- [Super JetPak DX](https://asobitech.itch.io/super-jetpak-dx)
- [Powa!](https://aiguanachein.itch.io/powa) - Side scrolling platformer for the Game Boy (Color)  ([ZGB engine](https://github.com/Zal0/ZGB/) [![GitHub stars](https://img.shields.io/github/stars/Zal0/ZGB/?style=flat)](https://github.com/Zal0/ZGB//stargazers)).
- [Cavern](https://thegreatgallus.itch.io/cavern-mvm-9) - ([ZGB engine](https://github.com/Zal0/ZGB/) [![GitHub stars](https://img.shields.io/github/stars/Zal0/ZGB/?style=flat)](https://github.com/Zal0/ZGB//stargazers)).
- [Mona and the Witch's Hat Deluxe](https://ctneptune.itch.io/mona-and-the-witchs-hat-dx) - ([ZGB engine](https://github.com/Zal0/ZGB/) [![GitHub stars](https://img.shields.io/github/stars/Zal0/ZGB/?style=flat)](https://github.com/Zal0/ZGB//stargazers)).
- [The Bouncing Ball](https://gamejolt.com/games/the-bouncing-ball-gb/86699)
- [DMG Deals Damage](https://drludos.itch.io/dmg-deals-damage)
- [totp-gb](https://github.com/dmang-dev/totp-gb) [![GitHub stars](https://img.shields.io/github/stars/dmang-dev/totp-gb?style=flat)](https://github.com/dmang-dev/totp-gb/stargazers) - TOTP (RFC 6238) two-factor authenticator with SGB border, GBC palettes and an MBC3 RTC clock.

### GB Studio

- [Soul Void](https://kadabura.itch.io/soul-void) - Interactive horror fiction.
- [Deadeus](https://izma.itch.io/deadeus)
- [SUPER IMPOSTOR BROS.](https://lumpytouch.itch.io/super-impostor-bros)

### Demos

- [Back to Color](https://github.com/AntonioND/back-to-color) [![GitHub stars](https://img.shields.io/github/stars/AntonioND/back-to-color?style=flat)](https://github.com/AntonioND/back-to-color/stargazers)
- [beach-gbc](https://github.com/vegard/beach-gbc) [![GitHub stars](https://img.shields.io/github/stars/vegard/beach-gbc?style=flat)](https://github.com/vegard/beach-gbc/stargazers)
- [CUTE DEMO](https://github.com/mills32/CUTE_DEMO) [![GitHub stars](https://img.shields.io/github/stars/mills32/CUTE_DEMO?style=flat)](https://github.com/mills32/CUTE_DEMO/stargazers)
- [`10 PRINT` Game Boy](https://github.com/svendahlstrand/10-print-game-boy) [![GitHub stars](https://img.shields.io/github/stars/svendahlstrand/10-print-game-boy?style=flat)](https://github.com/svendahlstrand/10-print-game-boy/stargazers)
- [Roboto Demo](https://github.com/naavis/roboto-demo) [![GitHub stars](https://img.shields.io/github/stars/naavis/roboto-demo?style=flat)](https://github.com/naavis/roboto-demo/stargazers)
- [matrix-rain-gb](https://github.com/wtjones/matrix-rain-gb) [![GitHub stars](https://img.shields.io/github/stars/wtjones/matrix-rain-gb?style=flat)](https://github.com/wtjones/matrix-rain-gb/stargazers) - A Matrix digital rain effect in assembler.
- [GBVideoPlayer](https://github.com/LIJI32/GBVideoPlayer) [![GitHub stars](https://img.shields.io/github/stars/LIJI32/GBVideoPlayer?style=flat)](https://github.com/LIJI32/GBVideoPlayer/stargazers) - A technical demo demonstrating how the Game Boy LCD controller can be hacked to make a Game Boy Color play a full motion video in color, together with music.
- [GBVideoPlayer2](https://github.com/LIJI32/GBVideoPlayer2) [![GitHub stars](https://img.shields.io/github/stars/LIJI32/GBVideoPlayer2?style=flat)](https://github.com/LIJI32/GBVideoPlayer2/stargazers) - The second iteration of the above demo, which increases the resolution, adds *stereo- PCM audio, and introduces video compression*.

## Reverse Engineering

- [Reverse engineering Kirby's Dreamland 2](http://ecc-comp.blogspot.it/2016/03/reverse-engineering-kirbys-dreamland-2.html)
- [pokemontools](https://github.com/pret/pokemon-reverse-engineering-tools) [![GitHub stars](https://img.shields.io/github/stars/pret/pokemon-reverse-engineering-tools?style=flat)](https://github.com/pret/pokemon-reverse-engineering-tools/stargazers) - a python module that provides various reverse engineering components for various Pokémon games.
- [Reverse Engineering a Gameboy ROM with radare2](https://www.megabeets.net/reverse-engineering-a-gameboy-rom-with-radare2) - A walkthrough to reverse engineer a Game Boy ROM challenge using radare2.
- [Disassembling Link's Awakening](http://kemenaran.winosx.com/posts/category-disassembling-links-awakening/) - A series of blog posts about disassembling Link's Awakening DX.
- [Reverse Engineering the GameBoy Tetris](https://github.com/h3nnn4n/Reverse-Engineering-the-GameBoy-Tetris) [![GitHub stars](https://img.shields.io/github/stars/h3nnn4n/Reverse-Engineering-the-GameBoy-Tetris?style=flat)](https://github.com/h3nnn4n/Reverse-Engineering-the-GameBoy-Tetris/stargazers)
- [DMA hijacking](https://gbdev.io/guides/dma_hijacking) - A simple technique that allows you to run custom code in most GB/SGB/CGB games, provided you have an ACE exploit.

### Game Disassemblies

- [Pokémon Red/Blue](https://github.com/pret/pokered) [![GitHub stars](https://img.shields.io/github/stars/pret/pokered?style=flat)](https://github.com/pret/pokered/stargazers)
- [Pokémon Crystal](https://github.com/pret/pokecrystal) [![GitHub stars](https://img.shields.io/github/stars/pret/pokecrystal?style=flat)](https://github.com/pret/pokecrystal/stargazers)
- [Pokémon Yellow](https://github.com/pret/pokeyellow) [![GitHub stars](https://img.shields.io/github/stars/pret/pokeyellow?style=flat)](https://github.com/pret/pokeyellow/stargazers)
- [Pokémon Gold and Silver](https://github.com/pret/pokegold) [![GitHub stars](https://img.shields.io/github/stars/pret/pokegold?style=flat)](https://github.com/pret/pokegold/stargazers)
- [Pokémon Pinball](https://github.com/pret/pokepinball) [![GitHub stars](https://img.shields.io/github/stars/pret/pokepinball?style=flat)](https://github.com/pret/pokepinball/stargazers)
- [Pokémon TCG](https://github.com/pret/poketcg) [![GitHub stars](https://img.shields.io/github/stars/pret/poketcg?style=flat)](https://github.com/pret/poketcg/stargazers)
- [pokegold-spaceworld](https://github.com/pret/pokegold-spaceworld) [![GitHub stars](https://img.shields.io/github/stars/pret/pokegold-spaceworld?style=flat)](https://github.com/pret/pokegold-spaceworld/stargazers) - Pokémon Gold and Silver 1997 Space World demo.
- [Link's Awakening DX](https://github.com/mojobojo/LADX-Disassembly) [![GitHub stars](https://img.shields.io/github/stars/mojobojo/LADX-Disassembly?style=flat)](https://github.com/mojobojo/LADX-Disassembly/stargazers)
- [Oracle of Ages](https://github.com/drenn1/ages-disasm) [![GitHub stars](https://img.shields.io/github/stars/drenn1/ages-disasm?style=flat)](https://github.com/drenn1/ages-disasm/stargazers)
- [Tetris](https://github.com/vinheim3/tetris-gb-disasm) [![GitHub stars](https://img.shields.io/github/stars/vinheim3/tetris-gb-disasm?style=flat)](https://github.com/vinheim3/tetris-gb-disasm/stargazers) - Complete Tetris disassembly.
- [FX Hammer](https://github.com/DevEd2/FXHammer-Disasm) [![GitHub stars](https://img.shields.io/github/stars/DevEd2/FXHammer-Disasm?style=flat)](https://github.com/DevEd2/FXHammer-Disasm/stargazers)
- [Harvest Moon 3](https://github.com/sanqui/hm3) [![GitHub stars](https://img.shields.io/github/stars/sanqui/hm3?style=flat)](https://github.com/sanqui/hm3/stargazers)
- [Final Fantasy Adventure](https://daid.github.io/FFA-Disassembly/)
- [The Jungle Book](https://github.com/not-chciken/jungle-book-gb-disassembly) [![GitHub stars](https://img.shields.io/github/stars/not-chciken/jungle-book-gb-disassembly?style=flat)](https://github.com/not-chciken/jungle-book-gb-disassembly/stargazers)

## Game Boy Camera

### Retrieving images

Game Boy Printer emulation (e.g. to retrieve images from the camera):

- [Arduino Gameboy Printer Emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator) [![GitHub stars](https://img.shields.io/github/stars/mofosyne/arduino-gameboy-printer-emulator?style=flat)](https://github.com/mofosyne/arduino-gameboy-printer-emulator/stargazers) - Emulate a gameboy printer via the gameboy link cable. 
- [ESP8266 Game Boy Printer](https://github.com/applefreak/esp8266-gameboy-printer) [![GitHub stars](https://img.shields.io/github/stars/applefreak/esp8266-gameboy-printer?style=flat)](https://github.com/applefreak/esp8266-gameboy-printer/stargazers) -  A device that emulates the Gameboy Printer and lets you retrieve images using WiFi powered by an ESP8266.
- [WiFi GBP Emulator](https://github.com/HerrZatacke/wifi-gbp-emulator) [![GitHub stars](https://img.shields.io/github/stars/HerrZatacke/wifi-gbp-emulator?style=flat)](https://github.com/HerrZatacke/wifi-gbp-emulator/stargazers) - A GameBoy printer emulator which provides the received data over a WiFi connection.
- [Game Boy WiFi Printer - D1 Mini Shield](https://github.com/cristofercruz/gbp-esp-shield-pcb) [![GitHub stars](https://img.shields.io/github/stars/cristofercruz/gbp-esp-shield-pcb?style=flat)](https://github.com/cristofercruz/gbp-esp-shield-pcb/stargazers) - Game Boy Printer interface shield for D1 mini/mini Pro ESP8266 boards. 
- [Game Boy Printer Sniffer](https://github.com/mofosyne/GameboyPrinterSniffer) [![GitHub stars](https://img.shields.io/github/stars/mofosyne/GameboyPrinterSniffer?style=flat)](https://github.com/mofosyne/GameboyPrinterSniffer/stargazers) - Sniff packet communications between a Game Boy and the Printer.

### Changing the camera's behavior

Methods to improve and/or manipulate the camera's quality and behavior:

- [Game Boy Camera Canon EF Lens Mount](http://ekeler.com/game-boy-camera-canon-ef-mount)
- [Game Boy Camera to Canon Lens mount](https://www.thingiverse.com/thing:4337362) - based on the above.
- [game-boy-camera-frame-replacer](https://github.com/cristofercruz/game-boy-camera-frame-replacer) [![GitHub stars](https://img.shields.io/github/stars/cristofercruz/game-boy-camera-frame-replacer?style=flat)](https://github.com/cristofercruz/game-boy-camera-frame-replacer/stargazers) - Manipulate the ROM of a camera to include custom frames

### Post processing

- [Game Boy Printer Paper Simulation](https://github.com/mofosyne/GameboyPrinterPaperSimulation) [![GitHub stars](https://img.shields.io/github/stars/mofosyne/GameboyPrinterPaperSimulation?style=flat)](https://github.com/mofosyne/GameboyPrinterPaperSimulation/stargazers) - Generate as-if-printed images of digital printed images.
- [Game Boy Printer Web](https://github.com/HerrZatacke/gb-printer-web) [![GitHub stars](https://img.shields.io/github/stars/HerrZatacke/gb-printer-web?style=flat)](https://github.com/HerrZatacke/gb-printer-web/stargazers) - Gallery app for to the Game Boy camera: import pictures from exports or cartridge dumps and choose color palettes.

## Related projects

- [GB Studio](https://www.gbstudio.dev/) - Drag and drop game creator with simple, no knowledge required, visual scripting.
  - [Resources to get started](https://gbstudiocentral.com/resources/)
  - [Dedicated Discord](https://discord.gg/knRryZWGcm)
  - [Lets Build a Platformer Game!](https://gumpyfunction.itch.io/lets-build-a-platformer) - A course designed to teach anyone how to create a platformer game using GB Studio 4+.
- [ArduinoBoy](https://github.com/trash80/Arduinoboy) [![GitHub stars](https://img.shields.io/github/stars/trash80/Arduinoboy?style=flat)](https://github.com/trash80/Arduinoboy/stargazers) - Serial communication (MIDI) from an Arduino to the Game Boy for music applications such as LittleSoundDJ, Nanoloop, and mGB.
- [papiGB](https://github.com/diegovalverde/papiGB) [![GitHub stars](https://img.shields.io/github/stars/diegovalverde/papiGB?style=flat)](https://github.com/diegovalverde/papiGB/stargazers) - Game Boy Classic fully functional FPGA implementation from scratch.
- [fpgaboy](https://github.com/trun/fpgaboy) [![GitHub stars](https://img.shields.io/github/stars/trun/fpgaboy?style=flat)](https://github.com/trun/fpgaboy/stargazers) - Implementation Nintendo's Game Boy console on an FPGA.
- [Piglet](https://github.com/danShumway/Piglet) [![GitHub stars](https://img.shields.io/github/stars/danShumway/Piglet?style=flat)](https://github.com/danShumway/Piglet/stargazers) - A LUA-driven AI that plays classic Game Boy color games using experimentation. In active development.
- [Ostrich](https://github.com/PumpMagic/ostrich) [![GitHub stars](https://img.shields.io/github/stars/PumpMagic/ostrich?style=flat)](https://github.com/PumpMagic/ostrich/stargazers) - A Game Boy Sound System player written in Swift.
- [mGB](https://github.com/trash80/mGB) [![GitHub stars](https://img.shields.io/github/stars/trash80/mGB?style=flat)](https://github.com/trash80/mGB/stargazers) - A Game Boy cartridge program that enables the Game Boy to act as a full MIDI supported sound module.
- [GBVisualizer](https://github.com/LIJI32/GBVisualizer) [![GitHub stars](https://img.shields.io/github/stars/LIJI32/GBVisualizer?style=flat)](https://github.com/LIJI32/GBVisualizer/stargazers) - Demonstrating the use of two undocumented Game Boy Color registers, nicknamed PCM12 (FF76) and PCM34 (FF77), which can be used to read the current PCM amplitude of the 4 APU channels.
- [ArduinoGameBoy](https://github.com/drhelius/arduinogameboy) [![GitHub stars](https://img.shields.io/github/stars/drhelius/arduinogameboy?style=flat)](https://github.com/drhelius/arduinogameboy/stargazers) - Arduino based Game Boy cartridge reader and writer.
- [gameboy-brainfuck](https://github.com/bitnenfer/gameboy-brainfuck) [![GitHub stars](https://img.shields.io/github/stars/bitnenfer/gameboy-brainfuck?style=flat)](https://github.com/bitnenfer/gameboy-brainfuck/stargazers) - Brainf*ck interpreter.
- [gbfk](https://github.com/elseyf/gbfk) [![GitHub stars](https://img.shields.io/github/stars/elseyf/gbfk?style=flat)](https://github.com/elseyf/gbfk/stargazers) - Brainf*ck interpreter, with input.
- [gb-save-states](https://github.com/mattcurrie/gb-save-states) [![GitHub stars](https://img.shields.io/github/stars/mattcurrie/gb-save-states?style=flat)](https://github.com/mattcurrie/gb-save-states/stargazers) - Patches to add save state support to Game Boy games when playing on the original hardware.
- [gbcpu](https://github.com/jdeblese/gbcpu) [![GitHub stars](https://img.shields.io/github/stars/jdeblese/gbcpu?style=flat)](https://github.com/jdeblese/gbcpu/stargazers) - A CPU and peripherals implementing the Game Boy instruction set and functionality.
- [Digitized Speech in Game Boy Games](https://youtube.com/watch?v=1lzHfLYzyRM)
- [Sniffing Game Boy serial traffic with an STM32F4](https://dhole.github.io/post/gameboy_serial_1/)
- [Virtual Game Boy Printer with an STM32F4](https://dhole.github.io/post/gameboy_serial_2/)
- [Printing on the Game Boy Printer using an STM32F4](https://dhole.github.io/post/gameboy_serial_3/)
- [Programming Game Boy Chinese cartridges with an STM32F4](https://dhole.github.io/post/gameboy_cartridge_rw_1/)
- [Pokemon Pocket Computer:](https://tilde.town/~minerobber/techwriteups/pokemonpc.html) - What is it and how to use it to make cheat codes.
- [Booting the Game Boy with a custom logo](https://dhole.github.io/post/gameboy_custom_logo/) - Bypassing the Nintendo logo check.
- Making a Game Boy game in 2017: A "Sheep It Up!" Post-Mortem ([part 1](https://www.gamasutra.com/blogs/DoctorLudos/20171207/311143/), [part 2](https://www.gamasutra.com/blogs/DoctorLudos/20180213/314554/))
- [Nintendo's fake logos](http://fuji.drillspirits.net/?post=87) - Every cartridge has to show the authentic logo to be considered valid and be run, but obviously some companies managed to exploit the check system.
- [liblsdj](https://github.com/stijnfrishert/liblsdj) [![GitHub stars](https://img.shields.io/github/stars/stijnfrishert/liblsdj?style=flat)](https://github.com/stijnfrishert/liblsdj/stargazers) - Utility library for interacting with the LSDj save format (.sav), song files (.lsdsng) and more.
- [lsdpatch](https://github.com/jkotlinski/lsdpatch) [![GitHub stars](https://img.shields.io/github/stars/jkotlinski/lsdpatch?style=flat)](https://github.com/jkotlinski/lsdpatch/stargazers) - Tool for modifying samples, fonts and palettes on LSDj ROM images.
- [Game Boy video effects](https://github.com/ChaosCabbage/crazy-gameboy-video-experiments) [![GitHub stars](https://img.shields.io/github/stars/ChaosCabbage/crazy-gameboy-video-experiments?style=flat)](https://github.com/ChaosCabbage/crazy-gameboy-video-experiments/stargazers) - Some little experiments using the STAT interrupt to do funny video manipulations.
- [gbos](https://github.com/ekimekim/gbos) [![GitHub stars](https://img.shields.io/github/stars/ekimekim/gbos?style=flat)](https://github.com/ekimekim/gbos/stargazers) - A basic operating system for the Game Boy.
- [Work Master OS](https://translate.google.com/translate?hl=&sl=ru&tl=en&u=https%3A%2F%2Fweb.archive.org%2Fweb%2F20081226145726%2Fhttp%3A%2F%2Fworkmaster.ru%2Findex.php%3Fp%3D8&sandbox=1) - Russian multi tasking operating system.
- [Game Boy Link Cable Breakout Board](https://github.com/Palmr/gb-link-cable) [![GitHub stars](https://img.shields.io/github/stars/Palmr/gb-link-cable?style=flat)](https://github.com/Palmr/gb-link-cable/stargazers)
- [GBCartFlasher firmware](https://github.com/Tauwasser/GBCartFlasher) [![GitHub stars](https://img.shields.io/github/stars/Tauwasser/GBCartFlasher?style=flat)](https://github.com/Tauwasser/GBCartFlasher/stargazers)
- [VerilogBoy](https://github.com/zephray/VerilogBoy/) [![GitHub stars](https://img.shields.io/github/stars/zephray/VerilogBoy/?style=flat)](https://github.com/zephray/VerilogBoy//stargazers) - Game Boy compatible console Verilog RTL implementation.
- [GBCamcorder](https://github.com/furrtek/GBCamcorder) [![GitHub stars](https://img.shields.io/github/stars/furrtek/GBCamcorder?style=flat)](https://github.com/furrtek/GBCamcorder/stargazers) - Lo-Fi portable video recorder using a GameBoy Camera cartridge.
- [GBCartRead](https://github.com/insidegadgets/GBCartRead) [![GitHub stars](https://img.shields.io/github/stars/insidegadgets/GBCartRead?style=flat)](https://github.com/insidegadgets/GBCartRead/stargazers) - Read ROM, Read RAM or Write RAM from/to a GameBoy Cartridge.
- [GBxCart-RW](https://github.com/insidegadgets/GBxCart-RW) [![GitHub stars](https://img.shields.io/github/stars/insidegadgets/GBxCart-RW?style=flat)](https://github.com/insidegadgets/GBxCart-RW/stargazers) - A device for reading game ROMs, save games and restoring saves for GB, GBC and GBA carts from your PC via USB.
- [Dumping the Super Game Boy Boot ROM](https://www.its.caltech.edu/~costis/sgb_hack/)
- [sm83-render](https://github.com/msinger/sm83-render) [![GitHub stars](https://img.shields.io/github/stars/msinger/sm83-render?style=flat)](https://github.com/msinger/sm83-render/stargazers) - A 3D model of the Game Boy CPU layout in Blender.
- [visual-sm83](https://iceboy.a-singer.de/visual6502/expert-sm83.html) - A visual transistor level simulation of the Game Boy CPU core in JavaScript, running in a browser.

### Directories

- [Archive of related files](http://gbdev.gg8.se/files/)
- [The Game Boy Archive](https://github.com/gb-archive) [![GitHub stars](https://img.shields.io/github/stars/gb-archive?style=flat)](https://github.com/gb-archive/stargazers) - A library of Game Boy related software, hardware and literature. Aimed to mirror and preserve old and fragmented contributions from the last three decades.
- [The Game Boy Archive - Salvage](https://github.com/gb-archive/salvage) [![GitHub stars](https://img.shields.io/github/stars/gb-archive/salvage?style=flat)](https://github.com/gb-archive/salvage/stargazers) - Historical archive of software, old articles, FAQs and various documents.

### Websites

- [devrs.com/gb](http://devrs.com/gb) - Old home of the scene: examples, sources, complete documentation, guides, tutorials and various tools.
- [pdroms.de](http://pdroms.de/news/gameboy/) - Game Boy releases.
- [Handheld Underground](http://hhug.me) - Unlicensed games, blog posts about Game Boy, home of the hhugboy emulator.


## About

### Contribute

Take a look at [Contribution Guidelines](CONTRIBUTING.md).

### License

Licensed under **GPLv3**.
See [LICENSE](LICENSE) for more information.

### Acknowledgements

Thanks to [every](https://github.com/avivace/awesome-gbdev/graphs/contributors) [![GitHub stars](https://img.shields.io/github/stars/avivace/awesome-gbdev/graphs/contributors?style=flat)](https://github.com/avivace/awesome-gbdev/graphs/contributors/stargazers) contributor of this project, Jeff Frohwein, Pascal Felber, KOOPa, Pan of Anthrox, GABY, Marat Fayzullin, Paul Robson, BOWSER, neviksti, Martin "nocash" Korth, Nitro2k01, Duo, Chris Antonellis, Michael Hope, Beware, Jonathan “Lord Nightmare” Gevaryahu, Carsten Sorense, Sindre Aamås, Otaku No Zoku, GeeBee.

### Sponsors

Special thanks to our friends at [DigitalOcean](https://www.digitalocean.com/) and [Incube8 Games](https://incube8games.com/), sponsoring the open source activites of our Game Boy Development community.

