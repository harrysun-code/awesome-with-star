# FFmpeg

> 来源：[transitive-bullshit/awesome-ffmpeg](https://github.com/transitive-bullshit/awesome-ffmpeg)

[![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/awesome-ffmpeg?style=flat)](https://github.com/transitive-bullshit/awesome-ffmpeg/stargazers)

# Awesome FFmpeg [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [FFmpeg](http://ffmpeg.org) is a cross-platform solution to record, convert and stream audio and video.

<p align="center">
  <img width="400" src="https://cdn.rawgit.com/transitive-bullshit/awesome-ffmpeg/master/ffmpeg-logo.svg">
</p>


## Contents

- [Docs](#docs)
- [JavaScript](#javascript)
- [Native](#native)
- [Mobile](#mobile)
- [Tutorials](#tutorials)
- [Community](#community)


## Docs

FFmpeg's official docs are notoriously difficult for beginners to understand due to the scope and complexity of FFmpeg's capabilities. With that being said, they're still very useful as a reference.

- [FFmpeg.org](http://ffmpeg.org) - Where it all starts.
- [Filters](https://ffmpeg.org/ffmpeg-filters.html) - Docs for FFmpeg's powerful filter chains (scaling, cropping, concatenating, merging, etc.). This is one of my most visited links when working with FFmpeg.
- [Man page](https://man.cx/ffmpeg) - Official FFmpeg man page.
- [Wiki & Bug Tracker](https://trac.ffmpeg.org) - Lots of great info on here.
- [CLI flags](https://github.com/transitive-bullshit/ffmpeg-cli-flags/blob/master/readme.md) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-cli-flags/blob/master/readme.md?style=flat)](https://github.com/transitive-bullshit/ffmpeg-cli-flags/blob/master/readme.md/stargazers) - A comprehensive list of all FFmpeg commandline flags. Really useful for searching random flags that you come across in the wild.


## JavaScript

- [fluent-ffmpeg](https://github.com/fluent-ffmpeg/node-fluent-ffmpeg) [![GitHub stars](https://img.shields.io/github/stars/fluent-ffmpeg/node-fluent-ffmpeg?style=flat)](https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/stargazers) - A fluent API to [FFmpeg](http://www.ffmpeg.org). If you only use one tool from this list, it should be this one.
- [ffmpeg-probe](https://github.com/transitive-bullshit/ffmpeg-probe) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-probe?style=flat)](https://github.com/transitive-bullshit/ffmpeg-probe/stargazers) - Wrapper around ffprobe for getting info about media files.
- [ffmpeg-concat](https://github.com/transitive-bullshit/ffmpeg-concat) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-concat?style=flat)](https://github.com/transitive-bullshit/ffmpeg-concat/stargazers) - Concats a list of videos together using FFmpeg with sexy OpenGL transitions.
- [editly](https://github.com/mifi/editly) [![GitHub stars](https://img.shields.io/github/stars/mifi/editly?style=flat)](https://github.com/mifi/editly/stargazers) - Declarative video editing tool and library with slick animations and transitions.
- [ffmpeg-generate-video-preview](https://github.com/transitive-bullshit/ffmpeg-generate-video-preview) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-generate-video-preview?style=flat)](https://github.com/transitive-bullshit/ffmpeg-generate-video-preview/stargazers) - Generates an attractive image strip or GIF preview from a video.
- [ffmpeg-extract-frame](https://github.com/transitive-bullshit/ffmpeg-extract-frame) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-extract-frame?style=flat)](https://github.com/transitive-bullshit/ffmpeg-extract-frame/stargazers) - Extracts a single frame from a video.
- [ffmpeg-extract-frames](https://github.com/transitive-bullshit/ffmpeg-extract-frames) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-extract-frames?style=flat)](https://github.com/transitive-bullshit/ffmpeg-extract-frames/stargazers) - Extracts screenshots from a video using FFmpeg.
- [gif-extract-frames](https://github.com/transitive-bullshit/gif-extract-frames) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/gif-extract-frames?style=flat)](https://github.com/transitive-bullshit/gif-extract-frames/stargazers) - Extracts frames from GIFs including inter-frame coalescing.
- [ffmpeg-extract-audio](https://github.com/transitive-bullshit/ffmpeg-extract-audio) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-extract-audio?style=flat)](https://github.com/transitive-bullshit/ffmpeg-extract-audio/stargazers) - Extracts an audio stream from a media file.
- [ffmpeg-on-progress](https://github.com/transitive-bullshit/ffmpeg-on-progress) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-on-progress?style=flat)](https://github.com/transitive-bullshit/ffmpeg-on-progress/stargazers) - Utility for robustly reporting progress with fluent-ffmpeg.
- [ffmpeg.js](https://github.com/Kagami/ffmpeg.js) [![GitHub stars](https://img.shields.io/github/stars/Kagami/ffmpeg.js?style=flat)](https://github.com/Kagami/ffmpeg.js/stargazers) - Port of FFmpeg to JavaScript via Emscripten. Allows for limited FFmpeg use on the client-side.
- [ffmpeg-static](https://github.com/eugeneware/ffmpeg-static) [![GitHub stars](https://img.shields.io/github/stars/eugeneware/ffmpeg-static?style=flat)](https://github.com/eugeneware/ffmpeg-static/stargazers) - Provides static FFmpeg binaries for macOS, Linux, and Windows. Very useful for CI testing.
- [tangerine](https://github.com/niftylettuce/tangerine) [![GitHub stars](https://img.shields.io/github/stars/niftylettuce/tangerine?style=flat)](https://github.com/niftylettuce/tangerine/stargazers) - Webcam streaming service using Node.js, FFmpeg, WebSockets, and Lad.
- [ffparser](https://github.com/NiKlimenko/FFParser) [![GitHub stars](https://img.shields.io/github/stars/NiKlimenko/FFParser?style=flat)](https://github.com/NiKlimenko/FFParser/stargazers) - Parse input stream by frames directly into your code as a buffer.


## Native

- [ffmpeg-gl-transition](https://github.com/transitive-bullshit/ffmpeg-gl-transition) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit/ffmpeg-gl-transition?style=flat)](https://github.com/transitive-bullshit/ffmpeg-gl-transition/stargazers) - FFmpeg filter for applying GLSL transitions between video streams ([gl-transitions](https://gl-transitions.com/)).


## Mobile

- [simplest ffmpeg mobile](https://github.com/leixiaohua1020/simplest_ffmpeg_mobile) [![GitHub stars](https://img.shields.io/github/stars/leixiaohua1020/simplest_ffmpeg_mobile?style=flat)](https://github.com/leixiaohua1020/simplest_ffmpeg_mobile/stargazers) - FFmpeg examples for Android and iOS.
- [ijkplayer](https://github.com/Bilibili/ijkplayer) [![GitHub stars](https://img.shields.io/github/stars/Bilibili/ijkplayer?style=flat)](https://github.com/Bilibili/ijkplayer/stargazers) - Android / iOS video player based on FFmpeg.


## Tutorials

- [How to Write a Video Player in Less Than 1k Lines](http://dranger.com/ffmpeg)
- [Learn FFmpeg libav the Hard Way](https://github.com/leandromoreira/ffmpeg-libav-tutorial) [![GitHub stars](https://img.shields.io/github/stars/leandromoreira/ffmpeg-libav-tutorial?style=flat)](https://github.com/leandromoreira/ffmpeg-libav-tutorial/stargazers)
- [Applying OpenGL Shaders with FFmpeg](https://nervous.io/ffmpeg/opengl/2017/01/31/ffmpeg-opengl) - And [follow-up](https://nervous.io/ffmpeg/opengl/2017/05/15/ffmpeg-pbo-yuv).
- [A Beginner's FFmpeg Cookbook](https://github.com/talwrii/ffmpeg-cookbook) [![GitHub stars](https://img.shields.io/github/stars/talwrii/ffmpeg-cookbook?style=flat)](https://github.com/talwrii/ffmpeg-cookbook/stargazers)
- [FFmpeg Cookbook](https://ghassan-gaidi.github.io/ffmpeg-cookbook/?ref=specD2) - Task-first cookbook of tested ffmpeg one-liners (compress, trim, GIF, audio extraction).
- [FFmpeg Cheatsheet for Video Automation](https://github.com/rendi-api/ffmpeg-cheatsheet) [![GitHub stars](https://img.shields.io/github/stars/rendi-api/ffmpeg-cheatsheet?style=flat)](https://github.com/rendi-api/ffmpeg-cheatsheet/stargazers)


## Community

- [Stack Overflow](https://superuser.com/questions/tagged/ffmpeg)
- [Mailing Lists](https://www.ffmpeg.org/contact.html#MailingLists)
- [IRC](https://www.ffmpeg.org/contact.html#IRCChannels)


## Contribute

Contributions welcome! Please read the [contributing guideline](contributing.md) first.


## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, [Travis Fischer](https://github.com/transitive-bullshit) [![GitHub stars](https://img.shields.io/github/stars/transitive-bullshit?style=flat)](https://github.com/transitive-bullshit/stargazers) has waived all copyright and related or neighboring rights to this work.

Support my OSS work by <a href="https://twitter.com/transitive_bs">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>
