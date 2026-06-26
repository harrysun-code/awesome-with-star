# CMake

[![GitHub stars](https://img.shields.io/github/stars/onqtam/awesome-cmake?style=flat)](https://github.com/onqtam/awesome-cmake/stargazers)

# Awesome CMake [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://rawgit.com/onqtam/awesome-cmake/master/cmake-logo.svg" align="right" width="100">](https://cmake.org/)

> A curated list of awesome [CMake](https://cmake.org/) scripts, modules, examples and others

Your contributions are highly welcome (first see [CONTRIBUTING.md](CONTRIBUTING.md)).

There is another file [`NonModernCMake.md`](NonModernCMake.md) with other links worth taking a look, but they use obsolete practices which are considered non-modern - like not using `target_*`-based dependency management - see [`#16`](https://github.com/onqtam/awesome-cmake/issues/16) [![GitHub stars](https://img.shields.io/github/stars/onqtam/awesome-cmake/issues/16?style=flat)](https://github.com/onqtam/awesome-cmake/issues/16/stargazers) and [`#42`](https://github.com/onqtam/awesome-cmake/pull/42) [![GitHub stars](https://img.shields.io/github/stars/onqtam/awesome-cmake/pull/42?style=flat)](https://github.com/onqtam/awesome-cmake/pull/42/stargazers) for more details.

## Contents

- [Community](#community)
- [Resources](#resources)
- [Package Management / Build Systems](#package-management--build-systems)
- [Modules](#modules)
- [Utility Scripts](#utility-scripts)
- [Toolchains](#toolchains)
- [Examples / Templates](#examples--templates)
- [Other](#other)

## Community

* [```#cmake``` on Freenode](http://webchat.freenode.net/?channels=cmake)
* [```/r/cmake``` on Reddit](https://www.reddit.com/r/cmake/)
* [```/r/cpp``` on Reddit](https://www.reddit.com/r/cpp/)
* [Official Discourse Forum](https://discourse.cmake.org/)
* [Stack Overflow](http://stackoverflow.com/questions/tagged/cmake)

## Resources

* [Latest Documentation](https://cmake.org/cmake/help/latest/)
* [FAQ](https://gitlab.kitware.com/cmake/community/-/wikis/FAQ)
* [Wiki](https://gitlab.kitware.com/cmake/community/-/wikis/home)
* [Webinars](https://cmake.org/webinars/)
* [Web Book](https://github.com/ruslo/CGold) [![GitHub stars](https://img.shields.io/github/stars/ruslo/CGold?style=flat)](https://github.com/ruslo/CGold/stargazers) - CGold: The Hitchhiker’s [Guide](https://cgold.readthedocs.io) to the CMake. [```[BSD2]```][BSD-2-Clause]
* [Modern CMake](https://github.com/toeb/moderncmake) [![GitHub stars](https://img.shields.io/github/stars/toeb/moderncmake?style=flat)](https://github.com/toeb/moderncmake/stargazers) - Modern CMake **PDF** and samples by the creator of [cmakepp](https://github.com/toeb/cmakepp) [![GitHub stars](https://img.shields.io/github/stars/toeb/cmakepp?style=flat)](https://github.com/toeb/cmakepp/stargazers). [```[MIT]```][MIT]
* [Tutorial](https://www.siliceum.com/en/blog/post/cmake_01_cmake-basics) - Modern CMake tutorials part1: CMake basics
* [Article](http://foonathan.net/blog/2016/03/03/cmake-install.html) - Easily supporting CMake install and find_package().
* [Article](http://foonathan.net/blog/2016/07/07/cmake-dependency-handling.html) - Easy dependency management for C++ with CMake and Git.
* [Article](https://steveire.wordpress.com/2016/08/09/opt-in-header-only-libraries-with-cmake/) - Opt-in header-only libraries with CMake.
* [Article](https://rix0r.nl/blog/2015/08/13/cmake-guide/) - Ultimate Guide to Modern CMake.
* [Article](https://web.archive.org/web/20190116071957/http://voices.canonical.com/jussi.pakkanen/2013/03/26/a-list-of-common-cmake-antipatterns/) - A list of common CMake antipatterns (from 2013 but still relevant).
* [Article](http://preshing.com/20170511/how-to-build-a-cmake-based-project/) - How to Build a CMake-Based Project.
* [Article](http://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) - Learn CMake's Scripting Language in 15 Minutes.
* [Article](http://aosabook.org/en/cmake.html) - The architecture of CMake.
* [Lecture](https://www.youtube.com/watch?v=bsXLMQ6WgIk) - Effective CMake - by Daniel Pfeifer, C++Now 2017.
* [Article](https://devblogs.nvidia.com/parallelforall/building-cuda-applications-cmake/) - Building Cross-Platform CUDA Applications with CMake.
* [Tutorial](https://github.com/Wigner-GPU-Lab/Teaching/tree/master/CMake) [![GitHub stars](https://img.shields.io/github/stars/Wigner-GPU-Lab/Teaching/tree/master/CMake?style=flat)](https://github.com/Wigner-GPU-Lab/Teaching/tree/master/CMake/stargazers) - A step-by-step guide for understanding CMake.
* [Article + Lecture](https://steveire.wordpress.com/2017/11/05/embracing-modern-cmake/) - Embracing Modern CMake - by Stephen Kelly.
* [Lecture](https://www.youtube.com/watch?v=eC9-iRN2b04) - Modern CMake for Modular Design - by Mathieu Ropert, CppCon 2017.
* [Article](https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/) - It's Time To Do CMake Right (one of the best articles about CMake).
* Articles - A series on CMake - by Martin Hořeňovský
    * [Basic CMake usage](https://codingnest.com/basic-cmake/).
    * [Basic CMake, part 2: libraries](https://codingnest.com/basic-cmake-part-2/).
* [Lecture](https://www.youtube.com/watch?v=jt3meXdP-QI) - Introduction to CMake - by Florent Castelli, C++ Sweden 2018.
* [Article](http://bastian.rieck.me/blog/posts/2018/cmake_tips/) - Some nice and accurate CMake tips.
* [Article](http://unclejimbo.github.io/2018/06/08/Modern-CMake-for-Library-Developers/) - Modern CMake for Library Developers.
* [Article](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1) - Effective Modern CMake: a great summary of most good practices - by Manuel Binna.
* [Book](https://crascit.com/professional-cmake/) - Professional CMake: A Practical Guide (paid).
* [Book](https://leanpub.com/effective-cmake) - Effective CMake: Practical Advice to Write Better CMake (not fully written yet).
* [Web Book](https://cliutils.gitlab.io/modern-cmake/) - An Introduction to Modern CMake.
* [YouTube Series](https://vector-of-bool.github.io/2018/08/12/cmake-good.html) - How to CMake Good. [```[CC0-1.0]```][CC0-1.0]
* [Lecture](https://www.youtube.com/watch?v=y7ndUhdQuU8) - More Modern CMake ([slides & examples](https://github.com/Bagira80/More-Modern-CMake) [![GitHub stars](https://img.shields.io/github/stars/Bagira80/More-Modern-CMake?style=flat)](https://github.com/Bagira80/More-Modern-CMake/stargazers))- by Deniz Bahadir, Meeting C++ 2018.
* [Lecture](https://www.youtube.com/watch?v=y9kSr5enrSk) - Oh No! More Modern CMake ([slides](https://github.com/Bagira80/More-Modern-CMake/raw/master/OhNoMoreModernCMake.pdf) [![GitHub stars](https://img.shields.io/github/stars/Bagira80/More-Modern-CMake/raw/master/OhNoMoreModernCMake.pdf?style=flat)](https://github.com/Bagira80/More-Modern-CMake/raw/master/OhNoMoreModernCMake.pdf/stargazers))- by Deniz Bahadir, Meeting C++ 2019.
* [Article](https://cristianadam.eu/20190223/modifying-the-default-cmake-build-types/) - Modifying the default CMake build types/flags, toolchains and patches - Oh my! - by Cristian Adam.
* [Tutorial](https://github.com/schweitzer/modern-cmake-tutorial) [![GitHub stars](https://img.shields.io/github/stars/schweitzer/modern-cmake-tutorial?style=flat)](https://github.com/schweitzer/modern-cmake-tutorial/stargazers) - Tutorial and Example on How to Properly Use Modern CMake.

## Package Management / Build Systems

* [hunter](https://github.com/ruslo/hunter) [![GitHub stars](https://img.shields.io/github/stars/ruslo/hunter?style=flat)](https://github.com/ruslo/hunter/stargazers) - Cross-platform package manager for C++ (based on CMake ExternalProject). [```[BSD2]```][BSD-2-Clause]
* [cget](https://github.com/pfultz2/cget) [![GitHub stars](https://img.shields.io/github/stars/pfultz2/cget?style=flat)](https://github.com/pfultz2/cget/stargazers) - CMake package retrieval. This can be used to download and install CMake packages. [```[BOOST]```][BOOST]
* [cppan](https://cppan.org/) - C++ Archive Network - C++ Package Manager based on CMake, implemented in C++14. [```[APACHE2]```][APACHE2]
* [cpm](https://github.com/iauns/cpm) [![GitHub stars](https://img.shields.io/github/stars/iauns/cpm?style=flat)](https://github.com/iauns/cpm/stargazers) - C++ Package Manager based on CMake and Git. [```[MIT]```][MIT]
* [conan](https://github.com/conan-io/conan) [![GitHub stars](https://img.shields.io/github/stars/conan-io/conan?style=flat)](https://github.com/conan-io/conan/stargazers) - Conan C++ Package Manager, implemented in Python and has a CMake integration backend. [```[MIT]```][MIT]
* [fips](https://github.com/floooh/fips) [![GitHub stars](https://img.shields.io/github/stars/floooh/fips?style=flat)](https://github.com/floooh/fips/stargazers) - High-level build system/dependency management for distributed, multi-platform C/C++ projects. [```[MIT]```][MIT]
* [Ninja](https://github.com/ninja-build/ninja) [![GitHub stars](https://img.shields.io/github/stars/ninja-build/ninja?style=flat)](https://github.com/ninja-build/ninja/stargazers) - Build system that differs from others in two major respects: it is designed to have its input files generated by a higher-level build system (like CMake), and it is designed to run builds as fast as possible. [```[APACHE2]```][APACHE2]
* [vcpkg](https://github.com/Microsoft/vcpkg) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/vcpkg?style=flat)](https://github.com/Microsoft/vcpkg/stargazers) - A tool to acquire and build C++ open source libraries. Uses CMake internally as a build script language. [```[MIT]```][MIT]
* [pmm](https://github.com/AnotherFoxGuy/pmm) [![GitHub stars](https://img.shields.io/github/stars/AnotherFoxGuy/pmm?style=flat)](https://github.com/AnotherFoxGuy/pmm/stargazers) - PMM is a module for CMake that manages... package managers. [```[MIT]```][MIT]
* [cpm](https://github.com/TheLartians/CPM) [![GitHub stars](https://img.shields.io/github/stars/TheLartians/CPM?style=flat)](https://github.com/TheLartians/CPM/stargazers) - A setup-free CMake + git dependency manager. [```[MIT]```][MIT]
* [FetchDependency](https://github.com/jpetrie/fetch-dependency) [![GitHub stars](https://img.shields.io/github/stars/jpetrie/fetch-dependency?style=flat)](https://github.com/jpetrie/fetch-dependency/stargazers) - Configuration-time retrieval, configuration and building of dependencies. [```[MIT]```][MIT]

## Modules

* [cmake-modules](https://github.com/rpavlik/cmake-modules) [![GitHub stars](https://img.shields.io/github/stars/rpavlik/cmake-modules?style=flat)](https://github.com/rpavlik/cmake-modules/stargazers) - [Ryan Pavlik](https://github.com/rpavlik) [![GitHub stars](https://img.shields.io/github/stars/rpavlik?style=flat)](https://github.com/rpavlik/stargazers)'s collection of CMake modules. There are a number of find modules, especially for virtual reality and physical simulation, some utility modules, and some patches or workarounds for CMake itself. [```[BOOST]```][BOOST]
* [cmake-modules](https://github.com/bilke/cmake-modules) [![GitHub stars](https://img.shields.io/github/stars/bilke/cmake-modules?style=flat)](https://github.com/bilke/cmake-modules/stargazers) - This is a collection of additional CMake modules. Most of them are from Ryan Pavlik. [```[BOOST]```][BOOST]
* [CMake](https://github.com/Eyescale/CMake) [![GitHub stars](https://img.shields.io/github/stars/Eyescale/CMake?style=flat)](https://github.com/Eyescale/CMake/stargazers) - [Eyescale](https://github.com/Eyescale) [![GitHub stars](https://img.shields.io/github/stars/Eyescale?style=flat)](https://github.com/Eyescale/stargazers)'s common CMake modules. [```[BSD3]```][BSD-3-Clause]
* [cmake-modules](https://github.com/jedbrown/cmake-modules) [![GitHub stars](https://img.shields.io/github/stars/jedbrown/cmake-modules?style=flat)](https://github.com/jedbrown/cmake-modules/stargazers) - CMake modules for some scientific libraries. [```[BSD2]```][BSD-2-Clause]
* [cgcmake](https://github.com/chadmv/cgcmake) [![GitHub stars](https://img.shields.io/github/stars/chadmv/cgcmake?style=flat)](https://github.com/chadmv/cgcmake/stargazers) - CMake modules for common applications related to computer graphics. [```[MIT]```][MIT]
* [FindMathematica](https://github.com/sakra/FindMathematica) [![GitHub stars](https://img.shields.io/github/stars/sakra/FindMathematica?style=flat)](https://github.com/sakra/FindMathematica/stargazers) - CMake module for Mathematica. [```[MIT]```][MIT]
* [extra-cmake-modules](https://github.com/KDE/extra-cmake-modules) [![GitHub stars](https://img.shields.io/github/stars/KDE/extra-cmake-modules?style=flat)](https://github.com/KDE/extra-cmake-modules/stargazers) - [KDE](https://github.com/KDE) [![GitHub stars](https://img.shields.io/github/stars/KDE?style=flat)](https://github.com/KDE/stargazers)'s extra modules and scripts for CMake. [```[BSD3]```][BSD-3-Clause]
* [FindICU.cmake](https://github.com/julp/FindICU.cmake) [![GitHub stars](https://img.shields.io/github/stars/julp/FindICU.cmake?style=flat)](https://github.com/julp/FindICU.cmake/stargazers) - CMake module to find International Components for Unicode (ICU) Library. [```[BSD2]```][BSD-2-Clause]
* [FindTBB](https://github.com/justusc/FindTBB) [![GitHub stars](https://img.shields.io/github/stars/justusc/FindTBB?style=flat)](https://github.com/justusc/FindTBB/stargazers) - CMake find module for Intel Threading Building Blocks. [```[MIT]```][MIT]
* [FindWiX](https://github.com/apriorit/FindWiX) [![GitHub stars](https://img.shields.io/github/stars/apriorit/FindWiX?style=flat)](https://github.com/apriorit/FindWiX/stargazers) - CMake module for building [Windows Installer](https://en.wikipedia.org/wiki/Windows_Installer) packages with [WiX toolset](http://wixtoolset.org). [```[BSD3]```][BSD-3-Clause]
* [FindIDL](https://github.com/apriorit/FindIDL) [![GitHub stars](https://img.shields.io/github/stars/apriorit/FindIDL?style=flat)](https://github.com/apriorit/FindIDL/stargazers) - CMake module for building [IDL](https://docs.microsoft.com/en-us/windows/win32/midl/interface-definition-idl-file) files with MIDL and generating CLR DLL using [Tlbimp](https://docs.microsoft.com/en-us/dotnet/framework/tools/tlbimp-exe-type-library-importer). [```[MIT]```][MIT]
* [cmake-modules](https://github.com/hanjianwei/cmake-modules) [![GitHub stars](https://img.shields.io/github/stars/hanjianwei/cmake-modules?style=flat)](https://github.com/hanjianwei/cmake-modules/stargazers) - [hanjianwei](https://github.com/hanjianwei) [![GitHub stars](https://img.shields.io/github/stars/hanjianwei?style=flat)](https://github.com/hanjianwei/stargazers)'s CMake module collection. [```[MIT]```][MIT]
* [YCM](https://github.com/robotology/ycm) [![GitHub stars](https://img.shields.io/github/stars/robotology/ycm?style=flat)](https://github.com/robotology/ycm/stargazers) - Extra CMake Modules for [Yet Another Robot Platform](https://github.com/robotology/yarp) [![GitHub stars](https://img.shields.io/github/stars/robotology/yarp?style=flat)](https://github.com/robotology/yarp/stargazers) and friends. [```[BSD3]```][BSD-3-Clause]
* [CMakeCM](https://github.com/AnotherFoxGuy/CMakeCM) [![GitHub stars](https://img.shields.io/github/stars/AnotherFoxGuy/CMakeCM?style=flat)](https://github.com/AnotherFoxGuy/CMakeCM/stargazers) - CMake Community Modules. ```[NO LICENSE]```
* [Metabench](https://github.com/ldionne/metabench) [![GitHub stars](https://img.shields.io/github/stars/ldionne/metabench?style=flat)](https://github.com/ldionne/metabench/stargazers) - CMake module for compile-time microbenchmarks. [```[BOOST]```][BOOST]
* [Oranges](https://github.com/benthevining/Oranges) [![GitHub stars](https://img.shields.io/github/stars/benthevining/Oranges?style=flat)](https://github.com/benthevining/Oranges/stargazers) - [Ben Vining](https://github.com/benthevining) [![GitHub stars](https://img.shields.io/github/stars/benthevining?style=flat)](https://github.com/benthevining/stargazers)'s library of CMake modules and toolchains [```[GPL]```][GPL]

## Utility Scripts

These provide a wide range of functionality - from dealing with compiler flags to using tools. Some also contain modules.

* [cotire](https://github.com/sakra/cotire) [![GitHub stars](https://img.shields.io/github/stars/sakra/cotire?style=flat)](https://github.com/sakra/cotire/stargazers) - Cotire (compile time reducer) is a CMake module that speeds up the build process of CMake based build systems by fully automating techniques as precompiled headers and unity builds for C and C++. [```[MIT]```][MIT]
* [ucm](https://github.com/onqtam/ucm) [![GitHub stars](https://img.shields.io/github/stars/onqtam/ucm?style=flat)](https://github.com/onqtam/ucm/stargazers) - For managing compiler/linker flags, collecting sources, precompiled headers, unity builds and others. [```[MIT]```][MIT]
* [cmakepp](https://github.com/toeb/cmakepp) [![GitHub stars](https://img.shields.io/github/stars/toeb/cmakepp?style=flat)](https://github.com/toeb/cmakepp/stargazers) - Enhancement Suite for the CMake Build System. [```[MIT]```][MIT]
* [sugar](https://github.com/ruslo/sugar) [![GitHub stars](https://img.shields.io/github/stars/ruslo/sugar?style=flat)](https://github.com/ruslo/sugar/stargazers) - CMake tools and examples: collecting source files, warnings suppression, etc. [```[BSD2]```][BSD-2-Clause]
* [DownloadProject](https://github.com/Crascit/DownloadProject) [![GitHub stars](https://img.shields.io/github/stars/Crascit/DownloadProject?style=flat)](https://github.com/Crascit/DownloadProject/stargazers) - CMake module for downloading an external project's source at configure time. [```[MIT]```][MIT]
* [buildem](https://github.com/janelia-flyem/buildem) [![GitHub stars](https://img.shields.io/github/stars/janelia-flyem/buildem?style=flat)](https://github.com/janelia-flyem/buildem/stargazers) - Modular CMake-based system that leverages ExternalProject to simplify builds. [```[LICENSE]```](https://github.com/janelia-flyem/buildem/blob/master/LICENSE.txt)
* [coveralls-cmake](https://github.com/JoakimSoderberg/coveralls-cmake) [![GitHub stars](https://img.shields.io/github/stars/JoakimSoderberg/coveralls-cmake?style=flat)](https://github.com/JoakimSoderberg/coveralls-cmake/stargazers) - Coveralls JSON coverage generator and uploader for CMake. [```[MIT]```][MIT]
* [compatibility](https://github.com/foonathan/compatibility) [![GitHub stars](https://img.shields.io/github/stars/foonathan/compatibility?style=flat)](https://github.com/foonathan/compatibility/stargazers) - Improved version of cmake-compile-features. [```[LICENSE]```](https://github.com/foonathan/compatibility/blob/master/LICENSE)
* [cmake-modules](https://github.com/Tronic/cmake-modules) [![GitHub stars](https://img.shields.io/github/stars/Tronic/cmake-modules?style=flat)](https://github.com/Tronic/cmake-modules/stargazers) - LibFindMacros development repository and other cool CMake stuff. [```[LICENSE]```](https://github.com/Tronic/cmake-modules/blob/master/LibFindMacros.cmake#L2)
* [GreatCMakeCookOff](https://github.com/UCL/GreatCMakeCookOff) [![GitHub stars](https://img.shields.io/github/stars/UCL/GreatCMakeCookOff?style=flat)](https://github.com/UCL/GreatCMakeCookOff/stargazers) - This is a repository of useful and less than useful CMake recipes. [```[MIT]```][MIT]
* [cppcheck-target-cmake](https://github.com/polysquare/cppcheck-target-cmake) [![GitHub stars](https://img.shields.io/github/stars/polysquare/cppcheck-target-cmake?style=flat)](https://github.com/polysquare/cppcheck-target-cmake/stargazers) - Per-target CPPCheck for CMake. [```[MIT]```][MIT]
* [clang-tidy-target-cmake](https://github.com/polysquare/clang-tidy-target-cmake) [![GitHub stars](https://img.shields.io/github/stars/polysquare/clang-tidy-target-cmake?style=flat)](https://github.com/polysquare/clang-tidy-target-cmake/stargazers) - Add clang-tidy checks to a target using CMake. [```[MIT]```][MIT]
* [cmake-unit](https://github.com/polysquare/cmake-unit) [![GitHub stars](https://img.shields.io/github/stars/polysquare/cmake-unit?style=flat)](https://github.com/polysquare/cmake-unit/stargazers) - Unit testing framework for CMake. [```[MIT]```][MIT]
* [cmake-header-language](https://github.com/polysquare/cmake-header-language) [![GitHub stars](https://img.shields.io/github/stars/polysquare/cmake-header-language?style=flat)](https://github.com/polysquare/cmake-header-language/stargazers) - CMake macro to determine the language of a header file. [```[MIT]```][MIT]
* [tooling-cmake-util](https://github.com/polysquare/tooling-cmake-util) [![GitHub stars](https://img.shields.io/github/stars/polysquare/tooling-cmake-util?style=flat)](https://github.com/polysquare/tooling-cmake-util/stargazers) - Utility and common library for all polysquare CMake tools. [```[MIT]```][MIT]
* [iwyu-target-cmake](https://github.com/polysquare/iwyu-target-cmake) [![GitHub stars](https://img.shields.io/github/stars/polysquare/iwyu-target-cmake?style=flat)](https://github.com/polysquare/iwyu-target-cmake/stargazers) - CMake integration for include-what-you-use. [```[MIT]```][MIT]
* [sanitizers-cmake](https://github.com/arsenm/sanitizers-cmake) [![GitHub stars](https://img.shields.io/github/stars/arsenm/sanitizers-cmake?style=flat)](https://github.com/arsenm/sanitizers-cmake/stargazers) - CMake module to enable sanitizers for binary targets. [```[MIT]```][MIT]
* [cmake-precompiled-header](https://github.com/larsch/cmake-precompiled-header) [![GitHub stars](https://img.shields.io/github/stars/larsch/cmake-precompiled-header?style=flat)](https://github.com/larsch/cmake-precompiled-header/stargazers) - Visual Studio and GCC precompiled header macro. [```[LICENSE]```](https://github.com/larsch/cmake-precompiled-header/blob/master/PrecompiledHeader.cmake#L31)
* [CMakePCHCompiler](https://github.com/nanoant/CMakePCHCompiler) [![GitHub stars](https://img.shields.io/github/stars/nanoant/CMakePCHCompiler?style=flat)](https://github.com/nanoant/CMakePCHCompiler/stargazers) - CMake precompiled headers via custom compiler extension - with reuse support! [```[MIT]```][MIT]
* [CMake-codecov](https://github.com/RWTH-ELP/CMake-codecov) [![GitHub stars](https://img.shields.io/github/stars/RWTH-ELP/CMake-codecov?style=flat)](https://github.com/RWTH-ELP/CMake-codecov/stargazers) - Enables code coverage and generates coverage reports with CMake targets. [```[GPL]```][GPL]
* [cmake-get](https://github.com/pfultz2/cmake-get) [![GitHub stars](https://img.shields.io/github/stars/pfultz2/cmake-get?style=flat)](https://github.com/pfultz2/cmake-get/stargazers) - Get dependencies in config or script mode. ```[NO LICENSE]```
* [ixm](https://github.com/slurps-mad-rips/ixm) [![GitHub stars](https://img.shields.io/github/stars/slurps-mad-rips/ixm?style=flat)](https://github.com/slurps-mad-rips/ixm/stargazers) - Make CMake less painful when trying to write Modern Flexible CMake.  [```[MIT]```][MIT]
* [CMakeCooking](https://github.com/hakuch/CMakeCooking) [![GitHub stars](https://img.shields.io/github/stars/hakuch/CMakeCooking?style=flat)](https://github.com/hakuch/CMakeCooking/stargazers) - Flexible development environments for CMake projects with external dependencies
. [```[APACHE2]```][APACHE2]
* [fetch_paths.cmake](https://github.com/XiaoLey/fetch_paths.cmake) [![GitHub stars](https://img.shields.io/github/stars/XiaoLey/fetch_paths.cmake?style=flat)](https://github.com/XiaoLey/fetch_paths.cmake/stargazers) - Lightweight utility to simplify file/directory path retrieval in CMake, supporting dynamic searches and flexible output formats. [```[MIT]```](https://github.com/XiaoLey/fetch_paths.cmake/blob/main/LICENSE)

## Toolchains

* [dockcross](https://github.com/dockcross/dockcross) [![GitHub stars](https://img.shields.io/github/stars/dockcross/dockcross?style=flat)](https://github.com/dockcross/dockcross/stargazers) - Cross compiling toolchains in Docker images. [```[MIT]```][MIT]
* [android-cmake](https://github.com/taka-no-me/android-cmake) [![GitHub stars](https://img.shields.io/github/stars/taka-no-me/android-cmake?style=flat)](https://github.com/taka-no-me/android-cmake/stargazers) - CMake toolchain file and other scripts for the Android NDK. [```[BSD3]```][BSD-3-Clause]
* [ios-cmake](https://github.com/cristeab/ios-cmake) [![GitHub stars](https://img.shields.io/github/stars/cristeab/ios-cmake?style=flat)](https://github.com/cristeab/ios-cmake/stargazers) - Toolchain file and examples using CMake for iOS development. [```[BSD3]```][BSD-3-Clause]
* [qt-android-cmake](https://github.com/LaurentGomila/qt-android-cmake) [![GitHub stars](https://img.shields.io/github/stars/LaurentGomila/qt-android-cmake?style=flat)](https://github.com/LaurentGomila/qt-android-cmake/stargazers) - For building and deploying Qt based apps on Android without QtCreator. [```[LICENSE]```](https://github.com/LaurentGomila/qt-android-cmake/blob/master/license.txt)
* [mingw-w64-cmake](https://github.com/lachs0r/mingw-w64-cmake) [![GitHub stars](https://img.shields.io/github/stars/lachs0r/mingw-w64-cmake?style=flat)](https://github.com/lachs0r/mingw-w64-cmake/stargazers) - CMake-based MinGW-w64 Cross Toolchain - to build Windows binaries of mpv. [```[ISC]```][ISC]
* [cmake-avr](https://github.com/mkleemann/cmake-avr) [![GitHub stars](https://img.shields.io/github/stars/mkleemann/cmake-avr?style=flat)](https://github.com/mkleemann/cmake-avr/stargazers) - CMake toolchain for AVR. [```[LICENSE]```](https://github.com/mkleemann/cmake-avr/blob/master/LICENSE)
* [arduino-cmake](https://github.com/francoiscampbell/arduino-cmake) [![GitHub stars](https://img.shields.io/github/stars/francoiscampbell/arduino-cmake?style=flat)](https://github.com/francoiscampbell/arduino-cmake/stargazers) - This is the CMake project settings for the Arduino platform. [```[MPL]```][MPL]
* [polly](https://github.com/ruslo/polly) [![GitHub stars](https://img.shields.io/github/stars/ruslo/polly?style=flat)](https://github.com/ruslo/polly/stargazers) - Collection of CMake toolchain files and scripts for cross-platform build and CI testing. [```[BSD2]```][BSD-2-Clause]
* [toolchains](https://github.com/mosra/toolchains) [![GitHub stars](https://img.shields.io/github/stars/mosra/toolchains?style=flat)](https://github.com/mosra/toolchains/stargazers) - For cross-compiling with CMake. They are meant to be mainly used on ArchLinux. ```[NO LICENSE]```
* [cmake](https://github.com/staticlibs/cmake/tree/master/toolchains) [![GitHub stars](https://img.shields.io/github/stars/staticlibs/cmake/tree/master/toolchains?style=flat)](https://github.com/staticlibs/cmake/tree/master/toolchains/stargazers) - Collection of CMake toolchain files, mostly for static linking. [```[APACHE2]```][APACHE2]
* [Arduino-CMake-Toolchain](https://github.com/a9183756-gh/Arduino-CMake-Toolchain) [![GitHub stars](https://img.shields.io/github/stars/a9183756-gh/Arduino-CMake-Toolchain?style=flat)](https://github.com/a9183756-gh/Arduino-CMake-Toolchain/stargazers) - CMake toolchain for all official and 3rd party Arduino platforms. [```[MIT]```][MIT]

## Examples / Templates

* [cmake-init](https://github.com/cginternals/cmake-init) [![GitHub stars](https://img.shields.io/github/stars/cginternals/cmake-init?style=flat)](https://github.com/cginternals/cmake-init/stargazers) - Template for reliable, cross-platform C++ project setup using CMake. [```[LICENSE]```](https://github.com/cginternals/cmake-init/blob/master/LICENSE)
* [android-cmake](https://github.com/forexample/android-cmake) [![GitHub stars](https://img.shields.io/github/stars/forexample/android-cmake?style=flat)](https://github.com/forexample/android-cmake/stargazers) - Examples of using [ruslo/hunter](https://github.com/ruslo/hunter) [![GitHub stars](https://img.shields.io/github/stars/ruslo/hunter?style=flat)](https://github.com/ruslo/hunter/stargazers) package manager for an Android application. [```[BSD2]```][BSD-2-Clause]
* [hunter-simple](https://github.com/forexample/hunter-simple) [![GitHub stars](https://img.shields.io/github/stars/forexample/hunter-simple?style=flat)](https://github.com/forexample/hunter-simple/stargazers) - Example of downloading/installing dependencies using [ruslo/hunter](https://github.com/ruslo/hunter) [![GitHub stars](https://img.shields.io/github/stars/ruslo/hunter?style=flat)](https://github.com/ruslo/hunter/stargazers) package manager. [```[BSD2]```][BSD-2-Clause]
* [package-example](https://github.com/forexample/package-example) [![GitHub stars](https://img.shields.io/github/stars/forexample/package-example?style=flat)](https://github.com/forexample/package-example/stargazers) - Config mode of find_package (examples for [this](http://stackoverflow.com/questions/20746936/cmake-of-what-use-is-find-package-if-you-need-to-specify-cmake-module-path-an) Stack Overflow question). ```[NO LICENSE]```
* [minimal_cmake_example](https://github.com/krux02/minimal_cmake_example) [![GitHub stars](https://img.shields.io/github/stars/krux02/minimal_cmake_example?style=flat)](https://github.com/krux02/minimal_cmake_example/stargazers) - Minimal CMake example, that covers dependencies and packaging. [```[CC0-1.0]```][CC0-1.0]
* [cmake-example](https://github.com/bast/cmake-example) [![GitHub stars](https://img.shields.io/github/stars/bast/cmake-example?style=flat)](https://github.com/bast/cmake-example/stargazers) - Example project which demonstrates various CMake features. [```[BSD3]```][BSD-3-Clause]
* [cmake-examples](https://github.com/ttroy50/cmake-examples) [![GitHub stars](https://img.shields.io/github/stars/ttroy50/cmake-examples?style=flat)](https://github.com/ttroy50/cmake-examples/stargazers) - Useful CMake examples in a tutorial format. [```[MIT]```][MIT]
* [mini-cmake-qt](https://github.com/euler0/mini-cmake-qt) [![GitHub stars](https://img.shields.io/github/stars/euler0/mini-cmake-qt?style=flat)](https://github.com/euler0/mini-cmake-qt/stargazers) - Minimal CMake template for Qt 5 projects. [```[LICENSE]```](https://github.com/euler0/mini-cmake-qt/blob/master/LICENSE)
* [BASIS](https://github.com/cmake-basis/BASIS) [![GitHub stars](https://img.shields.io/github/stars/cmake-basis/BASIS?style=flat)](https://github.com/cmake-basis/BASIS/stargazers) - CMake [BASIS](https://cmake-basis.github.io) makes it easy to create sharable software and libraries that work together. [```[BSD2]```][BSD-2-Clause]
* [cpp-boilerplate](https://github.com/Lectem/cpp-boilerplate) [![GitHub stars](https://img.shields.io/github/stars/Lectem/cpp-boilerplate?style=flat)](https://github.com/Lectem/cpp-boilerplate/stargazers) - Template that aims to be a reference for modern CMake and CI. [```[MIT]```][MIT]
* [how-to-export-cpp-library](https://github.com/robotology/how-to-export-cpp-library) [![GitHub stars](https://img.shields.io/github/stars/robotology/how-to-export-cpp-library?style=flat)](https://github.com/robotology/how-to-export-cpp-library/stargazers) - An OS-agnostic template project for exporting either shared, static or header-only C++ library, sporting ctest and CI support, written in plain CMake with line-by-line tutorial comments. [```[MIT]```][MIT]
* [modern-cmake-sample](https://github.com/pabloariasal/modern-cmake-sample) [![GitHub stars](https://img.shields.io/github/stars/pabloariasal/modern-cmake-sample?style=flat)](https://github.com/pabloariasal/modern-cmake-sample/stargazers) - Best practices and proper usage of CMake by using targets. ```[NO LICENSE]```
* [CMakeInstallExample](https://github.com/DeveloperPaul123/CMakeInstallExample) [![GitHub stars](https://img.shields.io/github/stars/DeveloperPaul123/CMakeInstallExample?style=flat)](https://github.com/DeveloperPaul123/CMakeInstallExample/stargazers) - Installation example for a C++ project (Windows) with Cmake. ```[NO LICENSE]```
* [cpp14-project-template](https://github.com/arnavb/cpp14-project-template) [![GitHub stars](https://img.shields.io/github/stars/arnavb/cpp14-project-template?style=flat)](https://github.com/arnavb/cpp14-project-template/stargazers) - A C++14 template with CI, tests, code coverage, docs and static analysis integration. [```[CC0-1.0]```][CC0-1.0]
* [cmake_templates](https://github.com/acdemiralp/cmake_templates) [![GitHub stars](https://img.shields.io/github/stars/acdemiralp/cmake_templates?style=flat)](https://github.com/acdemiralp/cmake_templates/stargazers) - Templates for creating C++ libraries and executables (including conan). ```[NO LICENSE]```
* [cmake_snippets](https://github.com/adishavit/cmake_snippets) [![GitHub stars](https://img.shields.io/github/stars/adishavit/cmake_snippets?style=flat)](https://github.com/adishavit/cmake_snippets/stargazers) - Short copy-pasteable CMake snippets. [```[BSD3]```][BSD-3-Clause]
* [cmake-cookbook](https://github.com/dev-cafe/cmake-cookbook) [![GitHub stars](https://img.shields.io/github/stars/dev-cafe/cmake-cookbook?style=flat)](https://github.com/dev-cafe/cmake-cookbook/stargazers) - A huge CMake cookbook full of recipes. [```[MIT]```][MIT]
* [cpp-template](https://github.com/joshpeterson/cpp-template) [![GitHub stars](https://img.shields.io/github/stars/joshpeterson/cpp-template?style=flat)](https://github.com/joshpeterson/cpp-template/stargazers) - A template C++ repository, using CMake and Catch. ```[NO LICENSE]```
* [pitchfork](https://github.com/vector-of-bool/pitchfork) [![GitHub stars](https://img.shields.io/github/stars/vector-of-bool/pitchfork?style=flat)](https://github.com/vector-of-bool/pitchfork/stargazers) - A set of conventions for native C and C++ projects. [```[MIT]```][MIT]
* [cmake-examples](https://github.com/pr0g/cmake-examples) [![GitHub stars](https://img.shields.io/github/stars/pr0g/cmake-examples?style=flat)](https://github.com/pr0g/cmake-examples/stargazers) - A collection of as simple as possible, modern CMake projects. [```[MIT]```][MIT]
* [cpp-project](https://github.com/bsamseth/cpp-project) [![GitHub stars](https://img.shields.io/github/stars/bsamseth/cpp-project?style=flat)](https://github.com/bsamseth/cpp-project/stargazers) - Boiler plate for C++ projects - tests, CI, coverage, docs. [```[UNLICENSE]```][UNLICENSE]
* [ModernCppStarter](https://github.com/TheLartians/ModernCppStarter) [![GitHub stars](https://img.shields.io/github/stars/TheLartians/ModernCppStarter?style=flat)](https://github.com/TheLartians/ModernCppStarter/stargazers) - A template for modern C++ projects using CMake, CI, code coverage, clang-format, reproducible dependency management, tests using [doctest](https://github.com/onqtam/doctest) [![GitHub stars](https://img.shields.io/github/stars/onqtam/doctest?style=flat)](https://github.com/onqtam/doctest/stargazers) and much more. [```[UNLICENSE]```][UNLICENSE]
* [SeeMake](https://github.com/MhmRhm/SeeMake) [![GitHub stars](https://img.shields.io/github/stars/MhmRhm/SeeMake?style=flat)](https://github.com/MhmRhm/SeeMake/stargazers) - A feature-packed, ready-to-use CMake template with testing, static and dynamic checks, coverage reports, and more. [```[MIT]```][MIT]

## Other

* [autocmake](https://github.com/coderefinery/autocmake) [![GitHub stars](https://img.shields.io/github/stars/coderefinery/autocmake?style=flat)](https://github.com/coderefinery/autocmake/stargazers) - Using a autocmake.yml file [Autocmake](http://autocmake.readthedocs.io/en/latest/) composes CMake building blocks into a CMake project and generates CMakeLists.txt as well as a setup script, which serves as a front-end to CMakeLists.txt. [```[BSD3]```][BSD-3-Clause]
* [UseLATEX](https://gitlab.kitware.com/kmorel/UseLATEX) - Collection of CMake macros to simplify building LaTeX files. [```[BSD3]```][BSD-3-Clause]
* [scikit-build](https://github.com/scikit-build/scikit-build) [![GitHub stars](https://img.shields.io/github/stars/scikit-build/scikit-build?style=flat)](https://github.com/scikit-build/scikit-build/stargazers) - Improved build system generator for CPython C extensions. [```[MIT]```][MIT]
* [node-cmake](https://github.com/cjntaylor/node-cmake) [![GitHub stars](https://img.shields.io/github/stars/cjntaylor/node-cmake?style=flat)](https://github.com/cjntaylor/node-cmake/stargazers) - CMake-based build system for node.js native modules. [```[ISC]```][ISC]
* [cmake-font-lock](https://github.com/Lindydancer/cmake-font-lock) [![GitHub stars](https://img.shields.io/github/stars/Lindydancer/cmake-font-lock?style=flat)](https://github.com/Lindydancer/cmake-font-lock/stargazers) - Advanced syntax coloring support for CMake scripts inside Emacs. [```[GPL]```][GPL]
* [autovala](https://github.com/rastersoft/autovala) [![GitHub stars](https://img.shields.io/github/stars/rastersoft/autovala?style=flat)](https://github.com/rastersoft/autovala/stargazers) - Program that automatically generates CMake configuration files for your Vala project. [```[GPL]```][GPL]
* [catkin](https://github.com/ros/catkin) [![GitHub stars](https://img.shields.io/github/stars/ros/catkin?style=flat)](https://github.com/ros/catkin/stargazers) - CMake-based build system that is used to build all packages in Robot Operating System (ROS). [```[BSD3]```][BSD-3-Clause]
* [suitesparse-metis-for-windows](https://github.com/jlblancoc/suitesparse-metis-for-windows) [![GitHub stars](https://img.shields.io/github/stars/jlblancoc/suitesparse-metis-for-windows?style=flat)](https://github.com/jlblancoc/suitesparse-metis-for-windows/stargazers) - CMake scripts for painless usage of SuiteSparse+METIS. [```[BSD3]```][BSD-3-Clause]
* [osg-3rdparty-cmake](https://github.com/bjornblissing/osg-3rdparty-cmake) [![GitHub stars](https://img.shields.io/github/stars/bjornblissing/osg-3rdparty-cmake?style=flat)](https://github.com/bjornblissing/osg-3rdparty-cmake/stargazers) - CMake scripts for building OpenSceneGraph third party libraries. ```[MIXED LICENSE]```
* [cmake-d](https://github.com/dcarp/cmake-d) [![GitHub stars](https://img.shields.io/github/stars/dcarp/cmake-d?style=flat)](https://github.com/dcarp/cmake-d/stargazers) - CMake for D2. [```[MIT]```][MIT]
* [cmakeprojectmanager2](https://github.com/h4tr3d/cmakeprojectmanager2) [![GitHub stars](https://img.shields.io/github/stars/h4tr3d/cmakeprojectmanager2?style=flat)](https://github.com/h4tr3d/cmakeprojectmanager2/stargazers) - Enhanced CMake Project Manager plugin for Qt Creator. ```[NO LICENSE]```
* [cmake-lint](https://github.com/richq/cmake-lint) [![GitHub stars](https://img.shields.io/github/stars/richq/cmake-lint?style=flat)](https://github.com/richq/cmake-lint/stargazers) - Check for coding style issues in CMake files. cmakelint requires Python. [```[APACHE2]```][APACHE2]
* [git-cmake-format](https://github.com/kbenzie/git-cmake-format) [![GitHub stars](https://img.shields.io/github/stars/kbenzie/git-cmake-format?style=flat)](https://github.com/kbenzie/git-cmake-format/stargazers) - Integrate clang-format into your CMake project hosted in a git repository. [```[LICENSE]```](https://github.com/kbenzie/git-cmake-format/blob/master/license.txt)
* [cmakefmt](https://github.com/cmakefmt/cmakefmt) [![GitHub stars](https://img.shields.io/github/stars/cmakefmt/cmakefmt?style=flat)](https://github.com/cmakefmt/cmakefmt/stargazers) - Fast, native CMake formatter written in Rust with format-on-save editor support and a first-party GitHub Action. [```[MIT]```][MIT]
* [configure-cmake](https://github.com/nemequ/configure-cmake) [![GitHub stars](https://img.shields.io/github/stars/nemequ/configure-cmake?style=flat)](https://github.com/nemequ/configure-cmake/stargazers) - configure-cmake is an autotools-style configure script for CMake-based projects. [```[CC0-1.0]```][CC0-1.0]
* [cmake-ast](https://github.com/polysquare/cmake-ast) [![GitHub stars](https://img.shields.io/github/stars/polysquare/cmake-ast?style=flat)](https://github.com/polysquare/cmake-ast/stargazers) - Python module to reduce a CMake file to an AST. [```[MIT]```][MIT]
* [cmake-checks-cache](https://github.com/cristianadam/cmake-checks-cache) [![GitHub stars](https://img.shields.io/github/stars/cristianadam/cmake-checks-cache?style=flat)](https://github.com/cristianadam/cmake-checks-cache/stargazers) - CMake checks cache helper modules. [```[MIT]```][MIT]
* [cmake_check](https://github.com/DaelDe/cmake_check) [![GitHub stars](https://img.shields.io/github/stars/DaelDe/cmake_check?style=flat)](https://github.com/DaelDe/cmake_check/stargazers) - Static analysis (linter) for the CMake language (e.g. to enforce modern CMake rules). [```[MIT]```][MIT]
* [cmake-language-server](https://github.com/regen100/cmake-language-server) [![GitHub stars](https://img.shields.io/github/stars/regen100/cmake-language-server?style=flat)](https://github.com/regen100/cmake-language-server/stargazers) - CMake Language Server Protocol Implementation. [```[MIT]```][MIT]
* [cmake-xray](https://github.com/pt9912/cmake-xray) [![GitHub stars](https://img.shields.io/github/stars/pt9912/cmake-xray?style=flat)](https://github.com/pt9912/cmake-xray/stargazers) - Analyze and diagnose CMake-based C++ builds from compile databases and CMake File API data. [```[MIT]```][MIT]
* [cmake-maven-plugin](https://github.com/cmake-maven-project/cmake-maven-project) [![GitHub stars](https://img.shields.io/github/stars/cmake-maven-project/cmake-maven-project?style=flat)](https://github.com/cmake-maven-project/cmake-maven-project/stargazers) - CMake integration for Maven builds. [```[APACHE2]```][APACHE2]
* [version-from-git](https://github.com/MhmRhm/version-from-git) [![GitHub stars](https://img.shields.io/github/stars/MhmRhm/version-from-git?style=flat)](https://github.com/MhmRhm/version-from-git/stargazers) - Bake git information into your binary. [```[MIT]```][MIT]
* [SoCMake](https://github.com/HEP-SoC/SoCMake) [![GitHub stars](https://img.shields.io/github/stars/HEP-SoC/SoCMake?style=flat)](https://github.com/HEP-SoC/SoCMake/stargazers) - CMake based build system for hardware (ASIC, FPGA) and System-on-Chip build automation. [```[LGPL]```][LGPL]

## License

This is released under the [**```Creative Commons Attribution 4.0 International```**](http://creativecommons.org/licenses/by/4.0/) License ```(CC BY 4.0)```.

[ISC]: https://opensource.org/licenses/ISC
[GPL]: https://www.gnu.org/licenses/gpl-3.0.html
[GPL2]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
[LGPL]: https://www.gnu.org/licenses/lgpl-3.0.en.html
[MIT]: https://opensource.org/licenses/MIT
[BOOST]: http://www.boost.org/LICENSE_1_0.txt
[BSD-2-Clause]: https://opensource.org/licenses/BSD-2-Clause
[BSD-3-Clause]: https://opensource.org/licenses/BSD-3-Clause
[APACHE2]: http://www.apache.org/licenses/LICENSE-2.0
[CC0-1.0]: https://creativecommons.org/publicdomain/zero/1.0/
[MPL]: https://www.mozilla.org/en-US/MPL/2.0/
[UNLICENSE]: https://unlicense.org/
