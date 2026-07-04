# Whisper

> 来源：[sindresorhus/awesome-whisper](https://github.com/sindresorhus/awesome-whisper)

[![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome-whisper?style=flat)](https://github.com/sindresorhus/awesome-whisper/stargazers)

<div align="center">
	<br>
	<br>
	<div>
		<img src="media/logo.png" alt="Awesome Whisper">
		<br>
	</div>
	<br>
	<p>
		<a href="https://openai.com/research/whisper">Whisper</a> is an open-source AI-powered speech recognition system developed by <a href="https://openai.com">OpenAI</a>
	</p>
	<br>
	<a href="https://awesome.re">
		<img src="https://awesome.re/badge-flat2.svg" alt="Awesome">
	</a>
	<br>
	<br>
	<br>
	<br>
	<br>
</div>

## Contents

- [Official](#official)
- [Model variants](#model-variants)
- [Apps](#apps)
- [Web apps](#web-apps)
- [CLI tools](#cli-tools)
- [Playgrounds](#playgrounds)
- [Packages](#packages)
- [Articles](#articles)
- [Videos](#videos)
- [Community](#community)
- [Third-party APIs](#third-party-apis)
- [Related lists](#related-lists)

## Official

- [Introduction](https://openai.com/research/whisper)
- [Source code](https://github.com/openai/whisper) [![GitHub stars](https://img.shields.io/github/stars/openai/whisper?style=flat)](https://github.com/openai/whisper/stargazers)
- [White paper](https://cdn.openai.com/papers/whisper.pdf)

## Model variants

- [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) [![GitHub stars](https://img.shields.io/github/stars/ggerganov/whisper.cpp?style=flat)](https://github.com/ggerganov/whisper.cpp/stargazers) - Port of Whisper in C++.
	- [Bindings for many languages](https://github.com/ggerganov/whisper.cpp#bindings) [![GitHub stars](https://img.shields.io/github/stars/ggerganov/whisper.cpp?style=flat)](https://github.com/ggerganov/whisper.cpp/stargazers)
- [WhisperX](https://github.com/m-bain/whisperX) [![GitHub stars](https://img.shields.io/github/stars/m-bain/whisperX?style=flat)](https://github.com/m-bain/whisperX/stargazers) - Adds fast automatic speaker recognition with word-level timestamps and speaker diarization.
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) [![GitHub stars](https://img.shields.io/github/stars/guillaumekln/faster-whisper?style=flat)](https://github.com/guillaumekln/faster-whisper/stargazers) - Faster reimplementation of Whisper using CTranslate2.
- [Whisper JAX](https://github.com/sanchit-gandhi/whisper-jax) [![GitHub stars](https://img.shields.io/github/stars/sanchit-gandhi/whisper-jax?style=flat)](https://github.com/sanchit-gandhi/whisper-jax/stargazers) - JAX implementation of Whisper for up to 70x speed-up on TPU.
- [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped) [![GitHub stars](https://img.shields.io/github/stars/linto-ai/whisper-timestamped?style=flat)](https://github.com/linto-ai/whisper-timestamped/stargazers) - Adds word-level timestamps and confidence scores.
- [whisper-openvino](https://github.com/zhuzilin/whisper-openvino) [![GitHub stars](https://img.shields.io/github/stars/zhuzilin/whisper-openvino?style=flat)](https://github.com/zhuzilin/whisper-openvino/stargazers) - Whisper running on OpenVINO.
- [whisper.tflite](https://github.com/usefulsensors/openai-whisper) [![GitHub stars](https://img.shields.io/github/stars/usefulsensors/openai-whisper?style=flat)](https://github.com/usefulsensors/openai-whisper/stargazers) - Whisper running on TensorFlow Lite.
- [Whisper variants](https://huggingface.co/models?other=whisper) - Various Whisper variants on Hugging Faces.
- [Whisper-AT](https://github.com/YuanGongND/whisper-at) [![GitHub stars](https://img.shields.io/github/stars/YuanGongND/whisper-at?style=flat)](https://github.com/YuanGongND/whisper-at/stargazers) - Whisper that can recognize non-speech audio events in addition to speech.

## Apps

- [Aiko](https://sindresorhus.com/aiko) - Audio transcription iOS and macOS app.
- [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) - Audio transcription macOS app. (Freemium)
- [Whisper Memos](https://apps.apple.com/app/id6443658039) - Audio transcription iOS app. (Freemium)
- [FourYou](https://apps.apple.com/app/id1671616134) - Audio journal iOS app.
- [Jojo Transcribe](https://apps.apple.com/app/id1659864300) - Audio transcription macOS app.
- [Buzz](https://github.com/chidiwilliams/Buzz) [![GitHub stars](https://img.shields.io/github/stars/chidiwilliams/Buzz?style=flat)](https://github.com/chidiwilliams/Buzz/stargazers) - Audio transcription and translation macOS app.
- [WhisperScript](https://store.getwavery.com/l/whisperscript) - Audio transcription macOS app. (Freemium · Electron)
- [Audio Podium](https://apps.apple.com/app/id6449008295) - Audio/video management macOS app.
- [superwhisper](https://superwhisper.com) - Global audio transcription macOS menu bar app.
- [TypeWhisper](https://github.com/TypeWhisper/typewhisper-mac) [![GitHub stars](https://img.shields.io/github/stars/TypeWhisper/typewhisper-mac?style=flat)](https://github.com/TypeWhisper/typewhisper-mac/stargazers) - Local speech-to-text transcription for macOS and Windows with system-wide dictation.
- [Speech Note](https://github.com/mkiol/dsnote) [![GitHub stars](https://img.shields.io/github/stars/mkiol/dsnote?style=flat)](https://github.com/mkiol/dsnote/stargazers) - Audio transcription Linux app.
- [FridayGPT](https://www.fridaygpt.app) - Dictation macOS app powered by OpenAI API.
- [EasyWhisper](https://easywhisper.io) - Windows and macOS app for audio transcription and speaker diarization. (Freemium)
- [Audio Note](https://audionote.app) - Real-time audio transcription on macOS and Windows. (Freemium · Electron)
- [Whisper](https://github.com/woheller69/whisperIME) [![GitHub stars](https://img.shields.io/github/stars/woheller69/whisperIME?style=flat)](https://github.com/woheller69/whisperIME/stargazers) - Android app for transcription and translation. (FOSS)
- [VoiceInk](https://github.com/Beingpax/VoiceInk) [![GitHub stars](https://img.shields.io/github/stars/Beingpax/VoiceInk?style=flat)](https://github.com/Beingpax/VoiceInk/stargazers) - Dictation and transcription macOS app. (FOSS)
- [Ito AI](https://github.com/heyito/ito) [![GitHub stars](https://img.shields.io/github/stars/heyito/ito?style=flat)](https://github.com/heyito/ito/stargazers) - AI voice dictation for Mac. (FOSS)
- [OpenSuperWhisper](https://github.com/Starmel/OpenSuperWhisper) [![GitHub stars](https://img.shields.io/github/stars/Starmel/OpenSuperWhisper?style=flat)](https://github.com/Starmel/OpenSuperWhisper/stargazers) - Dictation app for macOS. (FOSS)
- [Screenpipe](https://screenpi.pe) - 24/7 local screen and audio recording with AI search. (FOSS)

## Web apps

<!-- ### Hosted and self-hosted -->

### Hosted

- [bigWav](https://bigwav.app) - Audio transcription and annotation tool.
- [Free Podcast Transcription](https://freepodcasttranscription.com) - Runs locally in your browser.
- [Gladia](https://www.gladia.io) - Transcription with real-time processing.
- [Whisper-Web](https://github.com/PierreMesure/whisper-web) [![GitHub stars](https://img.shields.io/github/stars/PierreMesure/whisper-web?style=flat)](https://github.com/PierreMesure/whisper-web/stargazers) - Local transcription using WebGPU, with optimised fine-tuned models for several languages. (FOSS)

### Self-hosted

- [Subs AI](https://github.com/abdeladim-s/subsai) [![GitHub stars](https://img.shields.io/github/stars/abdeladim-s/subsai?style=flat)](https://github.com/abdeladim-s/subsai/stargazers) - Subtitle generation.
- [WaaS](https://github.com/schibsted/WAAS) [![GitHub stars](https://img.shields.io/github/stars/schibsted/WAAS?style=flat)](https://github.com/schibsted/WAAS/stargazers) - GUI and API for Whisper.
- [writeout.ai](https://github.com/beyondcode/writeout.ai) [![GitHub stars](https://img.shields.io/github/stars/beyondcode/writeout.ai?style=flat)](https://github.com/beyondcode/writeout.ai/stargazers) - Laravel app to transcribe and translate audio files.
- [Meeper](https://github.com/pas1ko/meeper) [![GitHub stars](https://img.shields.io/github/stars/pas1ko/meeper?style=flat)](https://github.com/pas1ko/meeper/stargazers) - Transcriptions, summary and more for meetings and any browser tab. (Chrome app)

## CLI tools

- [yt-whisper](https://github.com/m1guelpf/yt-whisper) [![GitHub stars](https://img.shields.io/github/stars/m1guelpf/yt-whisper?style=flat)](https://github.com/m1guelpf/yt-whisper/stargazers) - YouTube subtitle generation.
- [phonix](https://github.com/platisd/phonix) [![GitHub stars](https://img.shields.io/github/stars/platisd/phonix?style=flat)](https://github.com/platisd/phonix/stargazers) - Generate captions for videos.
- [whisper-standalone-win](https://github.com/Purfview/whisper-standalone-win) [![GitHub stars](https://img.shields.io/github/stars/Purfview/whisper-standalone-win?style=flat)](https://github.com/Purfview/whisper-standalone-win/stargazers) - Standalone Windows executable for Whisper and Faster Whisper.
- [whisper-ctranslate2](https://github.com/Softcatala/whisper-ctranslate2) [![GitHub stars](https://img.shields.io/github/stars/Softcatala/whisper-ctranslate2?style=flat)](https://github.com/Softcatala/whisper-ctranslate2/stargazers) - Whisper command-line tool based on CTranslate2, compatible with the original.
- [insanely-fast-whisper-cli](https://github.com/ochen1/insanely-fast-whisper-cli) [![GitHub stars](https://img.shields.io/github/stars/ochen1/insanely-fast-whisper-cli?style=flat)](https://github.com/ochen1/insanely-fast-whisper-cli/stargazers) - Achieve transcription speeds near 30x real-time with several optimizations.
- [whisper-diarization](https://github.com/MahmoudAshraf97/whisper-diarization) [![GitHub stars](https://img.shields.io/github/stars/MahmoudAshraf97/whisper-diarization?style=flat)](https://github.com/MahmoudAshraf97/whisper-diarization/stargazers) - Automatic speech recognition with speaker diarization.
- [hns](https://github.com/primaprashant/hns) [![GitHub stars](https://img.shields.io/github/stars/primaprashant/hns?style=flat)](https://github.com/primaprashant/hns/stargazers) - On-device speech-to-text CLI using faster-whisper with automatic clipboard copy.

## Playgrounds

- [Hugging Faces](https://huggingface.co/spaces/openai/whisper) - Whisper demo running on Hugging Faces. ([Source](https://huggingface.co/spaces/openai/whisper/tree/main))
- [Monster API](https://whisperui.monsterapi.ai) - Whisper demo running on Monster API. ([Source](https://github.com/saharmor/whisper-playground) [![GitHub stars](https://img.shields.io/github/stars/saharmor/whisper-playground?style=flat)](https://github.com/saharmor/whisper-playground/stargazers))
- [Web Whisper](https://whisper.r3d.red) - Whisper demo by Pluja. ([Source](https://codeberg.org/pluja/web-whisper))
- [YouTube Video Transcription](https://github.com/ArthurFDLR/whisper-youtube) [![GitHub stars](https://img.shields.io/github/stars/ArthurFDLR/whisper-youtube?style=flat)](https://github.com/ArthurFDLR/whisper-youtube/stargazers) - Running on Colab.

## Packages

### JavaScript

- [use-whisper](https://github.com/chengsokdara/use-whisper) [![GitHub stars](https://img.shields.io/github/stars/chengsokdara/use-whisper?style=flat)](https://github.com/chengsokdara/use-whisper/stargazers) - React hook.

## Articles

- [Whispers of A.I.'s Modular Future](https://www.newyorker.com/tech/annals-of-technology/whispers-of-ais-modular-future) - The future of machine learning lies in adaptable and accessible open-source speech-transcription programs.
- [How to Run Whisper Speech Recognition Model](https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/) - Explains how to install and run the model, as well as providing a performance analysis comparing Whisper to other models.
- [Create your own speech to text app using Flask](https://blog.paperspace.com/whisper-openai-flask-application-deployment/) - The tutorial demonstrates Whisper's speech-to-text model, with a demo on running it in a Gradient Notebook and a guide for setting up a Flask app with Gradient Deployments.
- [Convert Podcasts to Text](https://betterprogramming.pub/openais-whisper-tutorial-42140dd696ee) - Tutorial on the Whisper API with Python for speech-to-text transcription, showcasing GPU's faster transcription and advanced technology.

## Videos

- [Open AI's Whisper is Amazing!](https://www.youtube.com/watch?v=OCBZtgQGt1I) - Introduction to Whisper.
- [How to do Free Speech-to-Text Transcription Better Than Google Premium API](https://www.youtube.com/watch?v=msj3wuYf3d8) - Tutorial.
- [Multilingual AI Speech Recognition Live App](https://www.youtube.com/watch?v=ywIyc8l1K1Q) - Tutorial.

## Community

- [Discussions](https://github.com/openai/whisper/discussions)
- [Discord](https://discord.com/invite/openai)

## Third-party APIs

*APIs that use Whisper.*

- [Whisper+](https://www.oneai.com/speech-to-text) - Extension of the Whisper model which adds powerful features such as speaker identification custom vocabulary, summarization, and chapter generation.
- [Replicate](https://replicate.com/openai/whisper) - Use Whisper running on Replicate.

## Related lists

- [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome-chatgpt?style=flat)](https://github.com/sindresorhus/awesome-chatgpt/stargazers) - ChatGPT resources.
