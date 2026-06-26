# Vulkan

[![GitHub stars](https://img.shields.io/github/stars/vinjn/awesome-vulkan?style=flat)](https://github.com/vinjn/awesome-vulkan/stargazers)

# Awesome Vulkan [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<img src="https://raw.githubusercontent.com/SaschaWillems/Vulkan/master/images/vulkanlogoscene.png" alt="Vulkan demo scene" height="256px">

A curated list of awesome Vulkan libraries, debuggers and resources. Inspired by [awesome-opengl](https://github.com/eug/awesome-opengl) [![GitHub stars](https://img.shields.io/github/stars/eug/awesome-opengl?style=flat)](https://github.com/eug/awesome-opengl/stargazers) and other awesome-... stuff.

* **[Hardware Support](#hardware-support)**
* **[SDK](#sdk)**
* **[IHV Document](#document)**
* **[Tutorial](#tutorial)**
* **[Apps](#apps)**
* **[Samples](#samples)**
* **[Libraries](#libraries)**
* **[Bindings](#bindings)**
* **[Tools](#tools)**
* **[Books](#books)**
* **[Papers](#papers)**
* **[Khronos](#khronos)**
* **[Community](#community)**

## Hardware Support
*  [gpuinfo](http://vulkan.gpuinfo.org/) - Vulkan Hardware Database by Sascha Willems
*  [Khronos](https://www.khronos.org/vulkan)
*  [NVIDIA](https://developer.nvidia.com/Vulkan)
    *  [Driver for Desktop](https://developer.nvidia.com/vulkan-driver)
    *  [Driver for Android](https://developer.nvidia.com/vulkan-android)
    *  [Driver for Linux for Tegra (L4T)](https://developer.nvidia.com/embedded/vulkan)
*  [AMD](http://www.amd.com/en-gb/innovations/software-technologies/technologies-gaming/vulkan)
    *  [Open-source Driver](https://github.com/GPUOpen-Drivers/AMDVLK) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-Drivers/AMDVLK?style=flat)](https://github.com/GPUOpen-Drivers/AMDVLK/stargazers)
*  [Imagination](https://www.imgtec.com/developers/powervr-sdk-tools/)
*  Intel
    *  [Open-source Driver](https://01.org/linuxgraphics/blogs/jekstrand/2016/open-source-vulkan-drivers-intel-hardware/)
    *  [Driver for Windows](https://software.intel.com/en-us/blogs/2016/03/14/new-intel-vulkan-beta-1540204404-graphics-driver-for-windows-78110-1540)
*  [Qualcomm](https://developer.qualcomm.com/software/adreno-gpu-sdk/gpu)
*  Arm
    *  [Mali GPU Best Practices](https://developer.arm.com/solutions/graphics/developer-guides/mali-gpu-best-practices)

## SDK
*  [For Windows & Linux](https://vulkan.lunarg.com/signin)
*  [For Android](https://developer.android.com/ndk/guides/graphics/index.html)

## Document
*  [AMD](http://gpuopen.com/tag/vulkan/)
    *  [Vulkan barriers explained](http://gpuopen.com/vulkan-barriers-explained/)
    *  [Vulkan Fast Paths](https://gpuopen.com/wp-content/uploads/2016/03/VulkanFastPaths.pdf)
    *  [Let Your Game Shine – Optimizing DirectX 12 and Vulkan Performance with AMD CodeXL	](https://gpuopen.com/wp-content/uploads/2016/03/Let_your_game_shine_optimizing_DirectX-12_and_Vulkan-performance_with_AMD_CodeXL.pdf)
    *  [D3D12 & Vulkan: Lessons Learned	 ](https://gpuopen.com/wp-content/uploads/2016/03/d3d12_vulkan_lessons_learned.pdf)
    *  [Say Hello to a New Rendering API in Town!](http://gpuopen.com/say-hello/)
    *  [Vulkan Renderpasses](http://gpuopen.com/vulkan-renderpasses/)
    *  [Performance tweets series: Barriers, fences, synchronization](http://gpuopen.com/performance-tweets-series-barriers-fences-synchronization/)
    *  [Using the Vulkan™ Validation Layers](http://gpuopen.com/using-the-vulkan-validation-layers/)
    *  [Most common mistakes in Vulkan apps](https://gpuopen.com/wp-content/uploads/2016/05/Most-common-mistakes-in-Vulkan-apps.pdf)
	*  [Vulkan Device Memory](http://gpuopen.com/vulkan-device-memory/)
*  [NVIDIA](https://developer.nvidia.com/taxonomy/term/586)
    * [Vulkan Device-Generated Commands](https://developer.nvidia.com/device-generated-commands-vulkan)
    * [Getting Vulkan Ready For VR](https://developer.nvidia.com/getting-vulkan-ready-vr)
    * [GPU-Driven Rendering](http://on-demand.gputechconf.com/gtc/2016/presentation/s6138-christoph-kubisch-pierre-boudier-gpu-driven-rendering.pdf)
    * [GDC 16 - High-performance, Low-Overhead Rendering with OpenGL and Vulkan](http://developer.download.nvidia.com/gameworks/events/GDC2016/mschott_lbishop_gl_vulkan.pdf)
    * [GDC 16 - Vulkan and NVIDIA – The Essentials](http://developer.download.nvidia.com/gameworks/events/GDC2016/Vulkan_Essentials_GDC16_tlorach.pdf)
    * [Engaging the Voyage to Vulkan](https://developer.nvidia.com/engaging-voyage-vulkan)
    * [Vulkan Shader Resource Binding](https://developer.nvidia.com/vulkan-shader-resource-binding)
    * [Vulkan Memory Management](https://developer.nvidia.com/vulkan-memory-management)
    * [OpenGL like Vulkan](https://developer.nvidia.com/opengl-vulkan)
    * [Transitioning from OpenGL to Vulkan](https://developer.nvidia.com/transitioning-opengl-vulkan)
    * [Siggraph 15 talk - Vulkan on NVIDIA GPUs](http://on-demand.gputechconf.com/siggraph/2015/presentation/SIG1501-Piers-Daniell.pdf)
*  [Arm](https://developer.arm.com/solutions/graphics/apis/vulkan)
    * [Vulkan Best Practice for Mobile Developers Tutorials](https://github.com/ARM-software/vulkan_best_practice_for_mobile_developers) [![GitHub stars](https://img.shields.io/github/stars/ARM-software/vulkan_best_practice_for_mobile_developers?style=flat)](https://github.com/ARM-software/vulkan_best_practice_for_mobile_developers/stargazers)
    * [Vulkan's Key Features on Arm Architecture](https://developer.arm.com/-/media/Files/pdf/graphics-and-multimedia/Vulkan%20API%20key%20features%20on%20ARM%20architecture.pdf)
    * [Porting a Graphics Engine to the Vulkan API](https://community.arm.com/groups/arm-mali-graphics/blog/2016/02/16/porting-a-graphics-engine-to-the-vulkan-api)
    * [Get Your Engine Ready for Vulkan on Mobile](https://developer.arm.com/-/media/Files/pdf/graphics-and-multimedia/Get%20Your%20Engine%20Ready%20for%20Vulkan%20on%20Mobile.pdf)
    * [Multi-Threading in Vulkan](https://community.arm.com/groups/arm-mali-graphics/blog/2016/04/19/massively-multi-thread-for-vulkan)
    * [Mali Vulkan SDK Tutorials](https://developer.arm.com/products/software/mali-sdks/vulkan) and [Slides](https://developer.arm.com/graphics/vulkan/vulkan-tutorials)
* Intel
    * [API without Secrets: Introduction to Vulkan](https://github.com/GameTechDev/IntroductionToVulkan) [![GitHub stars](https://img.shields.io/github/stars/GameTechDev/IntroductionToVulkan?style=flat)](https://github.com/GameTechDev/IntroductionToVulkan/stargazers) [[LICENSE](https://github.com/GameTechDev/IntroductionToVulkan/blob/master/license.txt) [![GitHub stars](https://img.shields.io/github/stars/GameTechDev/IntroductionToVulkan/blob/master/license.txt?style=flat)](https://github.com/GameTechDev/IntroductionToVulkan/blob/master/license.txt/stargazers)]
        * [Part 1: The Beginning](https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-1)
        * [Part 2: Swap Chain](https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-2)
        * [Part 3: First Triangle](https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-3)
        * [Part 4: Vertex Attributes](https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-4)
* [Imagination](http://blog.imgtec.com/tag/vulkan)
    * [Efficient Rendering with Vulkan on PowerVR](https://imagination-technologies-cloudfront-assets.s3.amazonaws.com/idc-docs/gdc16/6_Efficient%20rendering%20with%20Vulkan%20on%20PowerVR.pdf)
    * [Migrating to Vulkan with the New PowerVR Graphics Framework](https://www.imgtec.com/webinar/migrating-to-vulkan-with-the-powervr-framework/)
    * [Migrating from OpenGLES to Vulkan](https://www.imgtec.com/downloads/download-info/migrating-from-opengl-es-to-vulkan/)
* Samsung
    * [Siggraph 2016 - Best Practices for Mobile](https://community.arm.com/cfs-file/__key/telligent-evolution-extensions-calendar-calendarfiles/00-00-00-00-05/2_2D00_mmg_2D00_siggraph2016_2D00_best_2D00_practice_2D00_andrew.pdf)
    * [Vulkan Usage Recommencation](https://developer.samsung.com/game/usage) (for mobile)
* Epic
    * [Efficient use of Vulkan on UE4 Mobile](https://community.arm.com/cfs-file/__key/telligent-evolution-extensions-calendar-calendarfiles/00-00-00-00-05/6_2D00_mmg_2D00_siggraph2016_2D00_vulkan_2D00_smedis.pdf)
* Khronos
   * [Vulkan Guide](https://github.com/KhronosGroup/Vulkan-Guide) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/Vulkan-Guide?style=flat)](https://github.com/KhronosGroup/Vulkan-Guide/stargazers)
* [LunarG](https://lunarg.com)
    * [Vulkan SDK](https://vulkan.lunarg.com/)
    * [Vulkan SDK Version Compatibility](https://www.lunarg.com/news-insights/white-papers/vulkan-sdk-version-compatibility/)
    * [Introducing the New Vulkan Configurator](https://www.lunarg.com/news-insights/white-papers/vulkan-validation-layers/)
    * [Unified Validation Layer for Vulkan](https://www.lunarg.com/news-insights/white-papers/unified-validation-layer-for-vulkan/)
    * [Vulkan Synchronization Validation Quick Start Guide](https://www.lunarg.com/news-insights/white-papers/vulkan-synchronization-validation-quick-start-guide/)
    * [Guide to Vulkan Synchronization Validation](https://www.lunarg.com/news-insights/white-papers/guide-to-vulkan-synchronization-validation/)
    * [Vulkan GPU-Assisted Validation](https://www.lunarg.com/news-insights/white-papers/vulkan-gpu-assisted-validation/)
    * [Automatic RelaxedPrecision Decoration and Conversion in Spirv-Opt](https://www.lunarg.com/news-insights/white-papers/automatic-relaxedprecision-decoration-and-conversion-in-spirv-opt/)
    * [SPIR-V Legalization and Size Reduction with spirv-opt](https://www.lunarg.com/news-insights/white-papers/spir-v-legalization-and-size-reduction-with-spirv-opt/)
    * [All White Papers](https://www.lunarg.com/vulkan-white-papers/)
* Community
    * [VulkanHub](https://vkdoc.net) 

## Tutorial
*  [How to Learn Vulkan](https://www.jeremyong.com/c++/vulkan/graphics/rendering/2018/03/26/how-to-learn-vulkan.html) - Meta post on how to learn Vulkan
*  [I Am Graphics And So Can You](https://www.fasterthan.life/blog/2017/7/11/i-am-graphics-and-so-can-you-part-1) - Blog post style tutorial for those new to graphics learning Vulkan.
*  [Vulkan Game Engine Tutorial](https://www.youtube.com/watch?v=Y9U9IE0gVHA) - Tutorial series on making a vulkan game engine by Brendan Galea on YouTube.
*  [Kohi Game Engine Series](https://www.youtube.com/watch?v=dHPuU-DJoBM&list=PLv8Ddw9K0JPg1BEO-RS-0MYs423cvLVtj) - "Vulkan Game Engine series, where we make a game engine from the ground up using C and Vulkan".
*  [Moving to Vulkan (Khronos UK May16)](https://www.khronos.org/assets/uploads/developers/library/2016-uk-chapter-moving-to-vulkan/Moving-to-Vulkan_Khronos-UK_May16.pdf)
*  [jhenriques's tutorial](http://jhenriques.net/development.html)
*  [Lunarg's tutorial](https://vulkan.lunarg.com/doc/sdk/1.0.26.0/windows/tutorial.html)
*  [Mike Bailey's Vulkan Page](http://web.engr.oregonstate.edu/~mjb/vulkan/) - Provides extensive Vulkan course slides. [CC BY-NC-ND 4.0]
*  [Qualcomm Video Tutorial Series](https://developer.qualcomm.com/software/adreno-gpu-sdk/tutorial-videos) - Leans more towards Vulkan for mobile devices.
*  [Raw Vulkan](https://alain.xyz/blog/raw-vulkan) - Overview on how to program a Vulkan application from the ground up.
* Siggraph
    * [An overview of next-generation graphics APIs](http://nextgenapis.realtimerendering.com/) - covers Vulkan, D3D12 etc.
*  [Tutorial by Overv](https://vulkan-tutorial.com/) and [its github repository](https://github.com/Overv/VulkanTutorial) [![GitHub stars](https://img.shields.io/github/stars/Overv/VulkanTutorial?style=flat)](https://github.com/Overv/VulkanTutorial/stargazers). [CC BY-SA 4.0]
*  [vulkan-sxs](https://github.com/philiptaylor/vulkan-sxs) [![GitHub stars](https://img.shields.io/github/stars/philiptaylor/vulkan-sxs?style=flat)](https://github.com/philiptaylor/vulkan-sxs/stargazers) - explain the Vulkan API step by step and [vulkan-sync](https://github.com/philiptaylor/vulkan-sync) [![GitHub stars](https://img.shields.io/github/stars/philiptaylor/vulkan-sync?style=flat)](https://github.com/philiptaylor/vulkan-sync/stargazers) - rephrase Vulkan's requirements on execution dependencies in a more precise form. [MIT]
*  [Vulkan in 30 minutes](https://renderdoc.org/vulkan-in-30-minutes.html) - by baldurk.
*  [Vulkan Demos and Tutorials](https://github.com/Z80Fan/VulkanDemos) [![GitHub stars](https://img.shields.io/github/stars/Z80Fan/VulkanDemos?style=flat)](https://github.com/Z80Fan/VulkanDemos/stargazers). [MIT]
*  [Vulkan Guide](https://vkguide.dev). [MIT]
*  [Vulkan Lecture Series](https://www.youtube.com/playlist?list=PLmIqTlJ6KsE1Jx5HV4sd2jOe3V1KMHHgn) - University lectures by Johannes Unterguggenberger from the Research Unit of Computer Graphics, TU Wien. Covers basic and advanced topics like: Vulkan essentials, the swap chain, resources and descriptors, commands and command buffers, pipelines and stages, real-time ray tracing, and synchronization.

## Apps
*  [The Talos Principle](http://www.croteam.com/talos-principle-will-support-vulkan-first-screenshot-released/) - by Croteam.
*  [Dota2](https://github.com/ValveSoftware/Dota-2-Vulkan/) [![GitHub stars](https://img.shields.io/github/stars/ValveSoftware/Dota-2-Vulkan/?style=flat)](https://github.com/ValveSoftware/Dota-2-Vulkan//stargazers) - by Valve.
*  [Basemark](https://www.basemark.com/blog/basemark-extends-its-benchmarking-lead-with-a-vulkan-performance-test/) - by Basemark.
*  [GFXBench 5](https://kishonti.net/news_single.jsp?id=31133884) - by Kishonti.
*  [ProtoStar](https://www.unrealengine.com/blog/epic-games-unveils-protostar-at-samsung-galaxy-unpacked) - by Epic, built with Unreal Engine 4 technology.
*  [DDraceNetwork](https://github.com/ddnet/ddnet/) [![GitHub stars](https://img.shields.io/github/stars/ddnet/ddnet/?style=flat)](https://github.com/ddnet/ddnet//stargazers) - Cooperative 2D platformer with optional [Vulkan backend](https://github.com/ddnet/ddnet/blob/master/src/engine/client/backend/vulkan/backend_vulkan.cpp) [![GitHub stars](https://img.shields.io/github/stars/ddnet/ddnet/blob/master/src/engine/client/backend/vulkan/backend_vulkan.cpp?style=flat)](https://github.com/ddnet/ddnet/blob/master/src/engine/client/backend/vulkan/backend_vulkan.cpp/stargazers). - [zlib](https://github.com/ddnet/ddnet/blob/master/license.txt) [![GitHub stars](https://img.shields.io/github/stars/ddnet/ddnet/blob/master/license.txt?style=flat)](https://github.com/ddnet/ddnet/blob/master/license.txt/stargazers) [website](https://ddnet.tw/)
*  [Doom](https://en.wikipedia.org/wiki/Doom_(2016_video_game)) - by id Software.
*  [vkQuake](https://github.com/Novum/vkQuake) [![GitHub stars](https://img.shields.io/github/stars/Novum/vkQuake?style=flat)](https://github.com/Novum/vkQuake/stargazers) - Vulkan Quake port based on QuakeSpasm. [GPL]
*  [vkQuake2](https://github.com/kondrak/vkQuake2) [![GitHub stars](https://img.shields.io/github/stars/kondrak/vkQuake2?style=flat)](https://github.com/kondrak/vkQuake2/stargazers) - id Software's Quake 2 v3.21 with Vulkan support (Windows and Linux). [GPL]
*  [q2vkpt](https://github.com/cschied/q2vkpt/) [![GitHub stars](https://img.shields.io/github/stars/cschied/q2vkpt/?style=flat)](https://github.com/cschied/q2vkpt//stargazers) - Real-time path tracer VKPT integrated into q2pro Quake 2 client. [gpl]
*  [Linux port of SteamVR](https://github.com/ValveSoftware/SteamVR-for-Linux) [![GitHub stars](https://img.shields.io/github/stars/ValveSoftware/SteamVR-for-Linux?style=flat)](https://github.com/ValveSoftware/SteamVR-for-Linux/stargazers) - SteamVR is built on top of the Vulkan API.
*  [3DMark](https://www.futuremark.com/pressreleases/compare-vulkan-and-directx-12-performance-with-3dmark) - 3DMark API Overhead test.
*  [Q2RTX](https://github.com/NVIDIA/Q2RTX) [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/Q2RTX?style=flat)](https://github.com/NVIDIA/Q2RTX/stargazers) - NVIDIA’s implementation of RTX ray-tracing in Quake II. [[LICENSE](https://github.com/NVIDIA/Q2RTX/blob/master/license.txt) [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/Q2RTX/blob/master/license.txt?style=flat)](https://github.com/NVIDIA/Q2RTX/blob/master/license.txt/stargazers)]

## Samples
*  Khronos [Vulkan samples](https://github.com/KhronosGroup/Vulkan-Samples) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/Vulkan-Samples?style=flat)](https://github.com/KhronosGroup/Vulkan-Samples/stargazers) [[LICENSE](https://github.com/KhronosGroup/Vulkan-Samples/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/Vulkan-Samples/blob/master/LICENSE?style=flat)](https://github.com/KhronosGroup/Vulkan-Samples/blob/master/LICENSE/stargazers)]
*  Sascha Willems's [samples](https://github.com/SaschaWillems/Vulkan) [![GitHub stars](https://img.shields.io/github/stars/SaschaWillems/Vulkan?style=flat)](https://github.com/SaschaWillems/Vulkan/stargazers) and [Deferred rendering of Sponza](https://github.com/SaschaWillems/VulkanSponza) [![GitHub stars](https://img.shields.io/github/stars/SaschaWillems/VulkanSponza?style=flat)](https://github.com/SaschaWillems/VulkanSponza/stargazers) and his talk of [Khronos_meetup_munich](https://www.saschawillems.de/blog/2016/04/11/khronos-chapter-munich-vulkan-slides/).
*  (Incomplete) Sascha Willems's [samples port](https://github.com/jvm-graphics-labs/Vulkan) [![GitHub stars](https://img.shields.io/github/stars/jvm-graphics-labs/Vulkan?style=flat)](https://github.com/jvm-graphics-labs/Vulkan/stargazers) to Kotlin
*  Sascha Willems's [Vulkan-glTF-PBR](https://github.com/SaschaWillems/Vulkan-glTF-PBR) [![GitHub stars](https://img.shields.io/github/stars/SaschaWillems/Vulkan-glTF-PBR?style=flat)](https://github.com/SaschaWillems/Vulkan-glTF-PBR/stargazers) - physical based rendering with Vulkan using glTF 2.0 models. [MIT]
*  [Vulkan Best Practice for Mobile Developers Samples](https://github.com/ARM-software/vulkan_best_practice_for_mobile_developers) [![GitHub stars](https://img.shields.io/github/stars/ARM-software/vulkan_best_practice_for_mobile_developers?style=flat)](https://github.com/ARM-software/vulkan_best_practice_for_mobile_developers/stargazers)
*  Google
    *  [Android port of LunarG samples](https://github.com/googlesamples/vulkan-basic-samples) [![GitHub stars](https://img.shields.io/github/stars/googlesamples/vulkan-basic-samples?style=flat)](https://github.com/googlesamples/vulkan-basic-samples/stargazers).
    *  [android tutorials](https://github.com/googlesamples/android-vulkan-tutorials) [![GitHub stars](https://img.shields.io/github/stars/googlesamples/android-vulkan-tutorials?style=flat)](https://github.com/googlesamples/android-vulkan-tutorials/stargazers).
*  [nvpro-samples](https://github.com/nvpro-samples) [![GitHub stars](https://img.shields.io/github/stars/nvpro-samples?style=flat)](https://github.com/nvpro-samples/stargazers) - NVIDIA DesignWorks Samples. [[LICENSE](https://github.com/nvpro-samples/gl_vk_threaded_cadscene/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/nvpro-samples/gl_vk_threaded_cadscene/blob/master/LICENSE?style=flat)](https://github.com/nvpro-samples/gl_vk_threaded_cadscene/blob/master/LICENSE/stargazers)]
    *  [gl_vk_chopper](https://github.com/nvpro-samples/gl_vk_chopper) [![GitHub stars](https://img.shields.io/github/stars/nvpro-samples/gl_vk_chopper?style=flat)](https://github.com/nvpro-samples/gl_vk_chopper/stargazers) - Simple vulkan rendering example.
    *  [gl_vk_threaded_cadscene](https://github.com/nvpro-samples/gl_vk_threaded_cadscene) [![GitHub stars](https://img.shields.io/github/stars/nvpro-samples/gl_vk_threaded_cadscene?style=flat)](https://github.com/nvpro-samples/gl_vk_threaded_cadscene/stargazers) - OpenGL and Vulkan comparison on rendering a CAD scene using various techniques and [the blog](https://developer.nvidia.com/vulkan-opengl-threaded-cad-scene-sample) about it.
    *  [gl_vk_bk3dthreaded](https://github.com/nvpro-samples/gl_vk_bk3dthreaded) [![GitHub stars](https://img.shields.io/github/stars/nvpro-samples/gl_vk_bk3dthreaded?style=flat)](https://github.com/nvpro-samples/gl_vk_bk3dthreaded/stargazers) - Vulkan sample rendering 3D with 'worker-threads'.
    *  [gl_vk_supersampled](https://github.com/nvpro-samples/gl_vk_supersampled) [![GitHub stars](https://img.shields.io/github/stars/nvpro-samples/gl_vk_supersampled?style=flat)](https://github.com/nvpro-samples/gl_vk_supersampled/stargazers) - Vulkan sample showing a high quality super-sampled rendering.
*  [NVIDIA GameWorks Samples](https://github.com/NVIDIAGameWorks/GraphicsSamples) [![GitHub stars](https://img.shields.io/github/stars/NVIDIAGameWorks/GraphicsSamples?style=flat)](https://github.com/NVIDIAGameWorks/GraphicsSamples/stargazers) - GameWorks cross-platform graphics API samples. [[LICENSE](https://github.com/NVIDIAGameWorks/GraphicsSamples/blob/master/license.txt) [![GitHub stars](https://img.shields.io/github/stars/NVIDIAGameWorks/GraphicsSamples/blob/master/license.txt?style=flat)](https://github.com/NVIDIAGameWorks/GraphicsSamples/blob/master/license.txt/stargazers)]
*  [LunarG's Samples](https://github.com/LunarG/VulkanSamples) [![GitHub stars](https://img.shields.io/github/stars/LunarG/VulkanSamples?style=flat)](https://github.com/LunarG/VulkanSamples/stargazers)
*  [vkcube](https://github.com/krh/vkcube) [![GitHub stars](https://img.shields.io/github/stars/krh/vkcube?style=flat)](https://github.com/krh/vkcube/stargazers) - 'vkcube' sample from krh, works under X, wayland and VT console with
drm/kms.
*  [Stardust from Intel](https://github.com/GameTechDev/stardust_vulkan) [![GitHub stars](https://img.shields.io/github/stars/GameTechDev/stardust_vulkan?style=flat)](https://github.com/GameTechDev/stardust_vulkan/stargazers) - The Stardust sample application uses the Vulkan graphics API to efficiently render a cloud of animated particles. [[LICENSE](https://github.com/GameTechDev/stardust_vulkan/blob/master/license.txt) [![GitHub stars](https://img.shields.io/github/stars/GameTechDev/stardust_vulkan/blob/master/license.txt?style=flat)](https://github.com/GameTechDev/stardust_vulkan/blob/master/license.txt/stargazers)]
*  [Vulkan Quake port based on QuakeSpasm](https://github.com/Novum/vkQuake) [![GitHub stars](https://img.shields.io/github/stars/Novum/vkQuake?style=flat)](https://github.com/Novum/vkQuake/stargazers).
*  [C# Samples](https://github.com/FacticiusVir/SharpVk-Samples) [![GitHub stars](https://img.shields.io/github/stars/FacticiusVir/SharpVk-Samples?style=flat)](https://github.com/FacticiusVir/SharpVk-Samples/stargazers) - Port of Overv's tutorials to [SharpVk](https://github.com/FacticiusVir/SharpVk) [![GitHub stars](https://img.shields.io/github/stars/FacticiusVir/SharpVk?style=flat)](https://github.com/FacticiusVir/SharpVk/stargazers) [MIT]
*  [Vulkan-Forward-Plus-Renderer](https://github.com/WindyDarian/Vulkan-Forward-Plus-Renderer) [![GitHub stars](https://img.shields.io/github/stars/WindyDarian/Vulkan-Forward-Plus-Renderer?style=flat)](https://github.com/WindyDarian/Vulkan-Forward-Plus-Renderer/stargazers) - VFPR - a Vulkan Forward Plus Renderer. [MIT]
*  [Laugh Engine](https://github.com/jian-ru/laugh_engine) [![GitHub stars](https://img.shields.io/github/stars/jian-ru/laugh_engine?style=flat)](https://github.com/jian-ru/laugh_engine/stargazers) - Vulkan implementation of real-time PBR renderer.
*  [tinyrenderers](https://github.com/chaoticbob/tinyrenderers) [![GitHub stars](https://img.shields.io/github/stars/chaoticbob/tinyrenderers?style=flat)](https://github.com/chaoticbob/tinyrenderers/stargazers) - Single header implemenations of Vulkan and D3D12 renderers.
*  [TLVulkanRenderer](https://github.com/trungtle/TLVulkanRenderer) [![GitHub stars](https://img.shields.io/github/stars/trungtle/TLVulkanRenderer?style=flat)](https://github.com/trungtle/TLVulkanRenderer/stargazers) - Simple Vulkan-based renderer for my master thesis on real-time transparency. [CC BY-SA 4.0]
*  [Vulkan-Hpp Samples](https://github.com/jherico/Vulkan) [![GitHub stars](https://img.shields.io/github/stars/jherico/Vulkan?style=flat)](https://github.com/jherico/Vulkan/stargazers) - Fork of Sascha Willems excellent Vulkan examples that uses Vulkan-Hpp.
*  [SDF Font Demo](https://github.com/kocsis1david/font-demo) [![GitHub stars](https://img.shields.io/github/stars/kocsis1david/font-demo?style=flat)](https://github.com/kocsis1david/font-demo/stargazers) - Text rendering in Vulkan by estimating signed distance. [MIT]
*  [vulkantoy](https://github.com/jpystynen/vulkantoy) [![GitHub stars](https://img.shields.io/github/stars/jpystynen/vulkantoy?style=flat)](https://github.com/jpystynen/vulkantoy/stargazers) - Shadertoy image shader test app with Vulkan. [MIT]
*  [GL_vs_VK](https://github.com/RippeR37/GL_vs_VK) [![GitHub stars](https://img.shields.io/github/stars/RippeR37/GL_vs_VK?style=flat)](https://github.com/RippeR37/GL_vs_VK/stargazers) - Comparison of OpenGL and Vulkan API in terms of performance. [MIT]
*  [Vulkan Basic Graphics Samples](https://github.com/vcoda/basic-graphics-samples) [![GitHub stars](https://img.shields.io/github/stars/vcoda/basic-graphics-samples?style=flat)](https://github.com/vcoda/basic-graphics-samples/stargazers) - Collection of simple graphics samples that are written using Magma library.
*  [Simple RTX Vulkan raytracing tutorials](https://github.com/iOrange/rtxON) [![GitHub stars](https://img.shields.io/github/stars/iOrange/rtxON?style=flat)](https://github.com/iOrange/rtxON/stargazers). [MIT]
*  [Ray Tracing In One Weekend (Vulkan RTX)](https://github.com/GPSnoopy/RayTracingInVulkan) [![GitHub stars](https://img.shields.io/github/stars/GPSnoopy/RayTracingInVulkan?style=flat)](https://github.com/GPSnoopy/RayTracingInVulkan/stargazers) - Implementation of Peter Shirley's Ray Tracing In One Weekend book using Vulkan and NVIDIA's RTX extension.
*  [Gears VK](https://github.com/jeffboody/gearsvk) [![GitHub stars](https://img.shields.io/github/stars/jeffboody/gearsvk?style=flat)](https://github.com/jeffboody/gearsvk/stargazers) - Gears VK is a heavily modified port of the famous "gears" demo to Vulkan/Android/Linux. [MIT]
*  [Hello triangle,](https://github.com/maierfelix/VK_KHR_ray_tracing) [![GitHub stars](https://img.shields.io/github/stars/maierfelix/VK_KHR_ray_tracing?style=flat)](https://github.com/maierfelix/VK_KHR_ray_tracing/stargazers) based on Vulkan Ray Tracing extensions. [MIT]
*  [Simple Animation Blender](https://github.com/Red1C3/Simple-Animation-Blender) [![GitHub stars](https://img.shields.io/github/stars/Red1C3/Simple-Animation-Blender?style=flat)](https://github.com/Red1C3/Simple-Animation-Blender/stargazers) - A real-time 1D animation blender and player using Vulkan as graphical back end and ImGui for GUI. [MIT]

## Libraries
* 2D
   *  [imgui](https://github.com/ocornut/imgui) [![GitHub stars](https://img.shields.io/github/stars/ocornut/imgui?style=flat)](https://github.com/ocornut/imgui/stargazers) - Immediate Mode Graphical User interface. [MIT]
   *  [Skia](https://skia.googlesource.com/skia) - Google's 2D graphics library has a [Vulkan](https://skia.org/user/special/vulkan) [backend](https://github.com/google/skia/tree/master/src/gpu/vk) [![GitHub stars](https://img.shields.io/github/stars/google/skia/tree/master/src/gpu/vk?style=flat)](https://github.com/google/skia/tree/master/src/gpu/vk/stargazers), demonstrated in a cross-platform [sample application](https://skia.org/user/sample/viewer) with its own [window library](https://github.com/google/skia/tree/master/tools/viewer) [![GitHub stars](https://img.shields.io/github/stars/google/skia/tree/master/tools/viewer?style=flat)](https://github.com/google/skia/tree/master/tools/viewer/stargazers). [BSD 3-clause] [website](https://skia.org)
   *  [VKVG](https://github.com/jpbruyere/vkvg) [![GitHub stars](https://img.shields.io/github/stars/jpbruyere/vkvg?style=flat)](https://github.com/jpbruyere/vkvg/stargazers) - Vulkan 2D graphics library, API follows the same pattern as Cairo graphics lib, but with new functions.

* Compute
   *  [libvc](https://github.com/alexhultman/libvc) [![GitHub stars](https://img.shields.io/github/stars/alexhultman/libvc?style=flat)](https://github.com/alexhultman/libvc/stargazers) - Vulkan Compute for C++.  [[LICENSE](https://github.com/alexhultman/libvc/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/alexhultman/libvc/blob/master/LICENSE?style=flat)](https://github.com/alexhultman/libvc/blob/master/LICENSE/stargazers)]
   *  [Vulkan Kompute](https://github.com/axsaucedo/vulkan-kompute) [![GitHub stars](https://img.shields.io/github/stars/axsaucedo/vulkan-kompute?style=flat)](https://github.com/axsaucedo/vulkan-kompute/stargazers) - Blazing fast and lightweight Vulkan Compute Framework optimized for advanced GPU processing usecases. [Apache License 2.0]
   *  [ncnn](https://github.com/Tencent/ncnn) [![GitHub stars](https://img.shields.io/github/stars/Tencent/ncnn?style=flat)](https://github.com/Tencent/ncnn/stargazers) - High-performance neural network inference framework with Vulkan based GPU inference. [BSD 3-clause]
   *  [vuh](https://github.com/Glavnokoman/vuh) [![GitHub stars](https://img.shields.io/github/stars/Glavnokoman/vuh?style=flat)](https://github.com/Glavnokoman/vuh/stargazers) - Vulkan-based C++ GPGPU computing framework. [MIT]
   *  [VkFFT](https://github.com/DTolm/VkFFT) [![GitHub stars](https://img.shields.io/github/stars/DTolm/VkFFT?style=flat)](https://github.com/DTolm/VkFFT/stargazers) - Efficient Vulkan FFT library [MPL-2.0 License]

* Low Level
   *  [Vulkan Memory Allocator](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator?style=flat)](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/stargazers) - Easy to integrate Vulkan memory allocation library from AMD. [MIT]
      *  [VulkanMemoryAllocator-Hpp] (https://github.com/malte-v/VulkanMemoryAllocator-Hpp) - C++ Bindings for VMA, like Vulkan-HPP
   *  [Fossilize](https://github.com/Themaister/Fossilize) [![GitHub stars](https://img.shields.io/github/stars/Themaister/Fossilize?style=flat)](https://github.com/Themaister/Fossilize/stargazers) - serialization format for various persistent Vulkan object types. [MIT]
   *  [vk-bootstrap](https://github.com/charles-lunarg/vk-bootstrap) [![GitHub stars](https://img.shields.io/github/stars/charles-lunarg/vk-bootstrap?style=flat)](https://github.com/charles-lunarg/vk-bootstrap/stargazers) - C++ utility library to jump start Vulkan development by automating instance, physical device, device, and swapchain creation. [MIT]
   *  [Google's vulkan-cpp-library](https://github.com/google/vulkan-cpp-library) [![GitHub stars](https://img.shields.io/github/stars/google/vulkan-cpp-library?style=flat)](https://github.com/google/vulkan-cpp-library/stargazers) - Vulkan abstraction library using C++11 for memory, resource management, type and thread safety as well as system independency. [Apache]
   *  [FrameGraph](https://github.com/azhirnov/FrameGraph) [![GitHub stars](https://img.shields.io/github/stars/azhirnov/FrameGraph?style=flat)](https://github.com/azhirnov/FrameGraph/stargazers) - Vulkan abstraction layer that represent frame as a task graph. [BSD 2-clause]
   *  [V-EZ](https://github.com/GPUOpen-LibrariesAndSDKs/V-EZ) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-LibrariesAndSDKs/V-EZ?style=flat)](https://github.com/GPUOpen-LibrariesAndSDKs/V-EZ/stargazers) - light-weight middleware layer for the Vulkan API targeting Professional Workstation ISVs. [MIT]
   *  [Vookoo](https://github.com/andy-thomason/Vookoo) [![GitHub stars](https://img.shields.io/github/stars/andy-thomason/Vookoo?style=flat)](https://github.com/andy-thomason/Vookoo/stargazers) - Vookoo is a set of dependency-free utilities to assist in the construction and updating of Vulkan graphics data structres. [MIT]
   *  [vpp](https://github.com/nyorain/vpp) [![GitHub stars](https://img.shields.io/github/stars/nyorain/vpp?style=flat)](https://github.com/nyorain/vpp/stargazers) - Modern C++ Vulkan Abstraction focused on performance and a straightforward interface. [MIT]
   *  [VulkanSceneGraph](https://github.com/vsg-dev) [![GitHub stars](https://img.shields.io/github/stars/vsg-dev?style=flat)](https://github.com/vsg-dev/stargazers) - Vulkan/C++17 scene graph project, successor to [OpenSceneGraph](http://www.openscenegraph.org).
   *  [Vulkan-WSIWindow](https://github.com/renelindsay/Vulkan-WSIWindow) [![GitHub stars](https://img.shields.io/github/stars/renelindsay/Vulkan-WSIWindow?style=flat)](https://github.com/renelindsay/Vulkan-WSIWindow/stargazers) - Multi-platform library to create a Vulkan window, and handle input events. [Apache License 2.0]
   *  [Screen 13](https://github.com/attackgoat/screen-13) [![GitHub stars](https://img.shields.io/github/stars/attackgoat/screen-13?style=flat)](https://github.com/attackgoat/screen-13/stargazers) - An easy-to-use Vulkan render graph for Rust. [MIT]

* Frameworks, Engines, Higher Level Rendering
   *  [Acid](https://github.com/Equilibrium-Games/Acid) [![GitHub stars](https://img.shields.io/github/stars/Equilibrium-Games/Acid?style=flat)](https://github.com/Equilibrium-Games/Acid/stargazers) - A high speed C++17 Vulkan game engine. [MIT]
   *  [AMD's Anvil](https://github.com/GPUOpen-LibrariesAndSDKs/Anvil) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-LibrariesAndSDKs/Anvil?style=flat)](https://github.com/GPUOpen-LibrariesAndSDKs/Anvil/stargazers) - cross-platform framework for Vulkan. [[LICENSE](https://github.com/GPUOpen-LibrariesAndSDKs/Anvil/blob/master/LICENSE.txt) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-LibrariesAndSDKs/Anvil/blob/master/LICENSE.txt?style=flat)](https://github.com/GPUOpen-LibrariesAndSDKs/Anvil/blob/master/LICENSE.txt/stargazers)]
   *  [Auto-Vk](https://github.com/cg-tuwien/Auto-Vk) [![GitHub stars](https://img.shields.io/github/stars/cg-tuwien/Auto-Vk?style=flat)](https://github.com/cg-tuwien/Auto-Vk/stargazers) - Vulkan convenience and productivity layer for modern C++, atop Vulkan-Hpp, by the Research Unit of Computer Graphics, TU Wien. [MIT]
   *  [Auto-Vk-Toolkit](https://github.com/cg-tuwien/Auto-Vk-Toolkit) [![GitHub stars](https://img.shields.io/github/stars/cg-tuwien/Auto-Vk-Toolkit?style=flat)](https://github.com/cg-tuwien/Auto-Vk-Toolkit/stargazers) - C++ framework around [Auto-Vk](https://github.com/cg-tuwien/Auto-Vk) [![GitHub stars](https://img.shields.io/github/stars/cg-tuwien/Auto-Vk?style=flat)](https://github.com/cg-tuwien/Auto-Vk/stargazers) for rapid prototyping, research, and teaching, by the Research Unit of Computer Graphics, TU Wien. [MIT for the framework's code]
   *  [bgfx](https://github.com/bkaradzic/bgfx#bgfx---cross-platform-rendering-library) - Cross-platform, graphics API agnostic, "Bring Your Own Engine/Framework" style rendering library. [[BSD-2-clause](https://github.com/bkaradzic/bgfx/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/bkaradzic/bgfx/blob/master/LICENSE?style=flat)](https://github.com/bkaradzic/bgfx/blob/master/LICENSE/stargazers)]
   *  [bsf](https://github.com/GameFoundry/bsf) [![GitHub stars](https://img.shields.io/github/stars/GameFoundry/bsf?style=flat)](https://github.com/GameFoundry/bsf/stargazers) - Modern C++14 library for the development of real-time graphical applications. [MIT]
   *  [Cinder](https://github.com/cinder/Cinder) [![GitHub stars](https://img.shields.io/github/stars/cinder/Cinder?style=flat)](https://github.com/cinder/Cinder/stargazers) and [the story](https://libcinder.org/notes/vulkan) [behind](https://forum.libcinder.org/#Topic/23286000002614007). [BSD]
   *  [DemoFramework](https://github.com/NXPmicro/gtec-demo-framework) [![GitHub stars](https://img.shields.io/github/stars/NXPmicro/gtec-demo-framework?style=flat)](https://github.com/NXPmicro/gtec-demo-framework/stargazers) - NXP GTEC C++11 cross-platform demo framework including lots of samples for Vulkan, OpenGL ES, OpenVX, OpenCL, OpenVG and OpenCV. [[BSD-3-clause](https://github.com/NXPmicro/gtec-demo-framework/blob/master/License.md) [![GitHub stars](https://img.shields.io/github/stars/NXPmicro/gtec-demo-framework/blob/master/License.md?style=flat)](https://github.com/NXPmicro/gtec-demo-framework/blob/master/License.md/stargazers)]
   *  [Diligent Engine](https://github.com/DiligentGraphics/DiligentEngine) [![GitHub stars](https://img.shields.io/github/stars/DiligentGraphics/DiligentEngine?style=flat)](https://github.com/DiligentGraphics/DiligentEngine/stargazers) - a modern cross-platform low-level graphics library that supports OpenGL/GLES, Direct3D11/12 and Vulkan. [Apache License 2.0]
   *  [Falcor](https://github.com/NVIDIAGameWorks/Falcor) [![GitHub stars](https://img.shields.io/github/stars/NVIDIAGameWorks/Falcor?style=flat)](https://github.com/NVIDIAGameWorks/Falcor/stargazers) - Real-time rendering framework from NVIDIA, supporting mainly DX12, with experimental Vulkan support. [BSD 3-clause]
   *  [glfw](https://github.com/glfw/glfw) [![GitHub stars](https://img.shields.io/github/stars/glfw/glfw?style=flat)](https://github.com/glfw/glfw/stargazers) and [the guide](http://www.glfw.org/docs/3.2/vulkan.html).  [[LICENSE](https://github.com/glfw/glfw/blob/master/LICENSE.md) [![GitHub stars](https://img.shields.io/github/stars/glfw/glfw/blob/master/LICENSE.md?style=flat)](https://github.com/glfw/glfw/blob/master/LICENSE.md/stargazers)]
   *  [Intrinsic Engine](https://github.com/begla/Intrinsic) [![GitHub stars](https://img.shields.io/github/stars/begla/Intrinsic?style=flat)](https://github.com/begla/Intrinsic/stargazers) - Intrinsic is a Vulkan based cross-platform graphics and game engine. [Apache License 2.0]
   *  [Introductory Vulkan sample by GPUOpen](https://github.com/GPUOpen-LibrariesAndSDKs/HelloVulkan) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-LibrariesAndSDKs/HelloVulkan?style=flat)](https://github.com/GPUOpen-LibrariesAndSDKs/HelloVulkan/stargazers). [MIT]
   *  [liblava](https://github.com/liblava/liblava) [![GitHub stars](https://img.shields.io/github/stars/liblava/liblava?style=flat)](https://github.com/liblava/liblava/stargazers) - A modern C++ and easy-to-use framework. [MIT]
   *  [Logi](https://github.com/UL-FRI-LGM/Logi) [![GitHub stars](https://img.shields.io/github/stars/UL-FRI-LGM/Logi?style=flat)](https://github.com/UL-FRI-LGM/Logi/stargazers) - Light-weight object oriented Vulkan abstraction framework. [BSD 2-clause]
   *  [Lugdunum](https://github.com/Lugdunum3D/Lugdunum) [![GitHub stars](https://img.shields.io/github/stars/Lugdunum3D/Lugdunum?style=flat)](https://github.com/Lugdunum3D/Lugdunum/stargazers) - Modern cross-platform 3D rendering engine built with Vulkan and modern C++14. [MIT]
   *  [Nabla](https://github.com/Devsh-Graphics-Programming/Nabla) [![GitHub stars](https://img.shields.io/github/stars/Devsh-Graphics-Programming/Nabla?style=flat)](https://github.com/Devsh-Graphics-Programming/Nabla/stargazers) - Vulkan, OptiX and CUDA Interoperation Modular Rendering Library and Framework for PC/Linux/Android. [Apache License 2.0]
   *  [openFrameworks](https://github.com/openframeworks-vk/openFrameworks) [![GitHub stars](https://img.shields.io/github/stars/openframeworks-vk/openFrameworks?style=flat)](https://github.com/openframeworks-vk/openFrameworks/stargazers) - the most famouse C++ creative coding framework. [MIT]
   *  [PowerVR SDK](https://github.com/powervr-graphics/Native_SDK) [![GitHub stars](https://img.shields.io/github/stars/powervr-graphics/Native_SDK?style=flat)](https://github.com/powervr-graphics/Native_SDK/stargazers) - C++ cross-platform 3D graphics SDK to speed up development of Vulkan and GLES. [[LICENSE](https://github.com/powervr-graphics/Native_SDK/blob/4.1/LICENSE_POWERVR_SDK.txt) [![GitHub stars](https://img.shields.io/github/stars/powervr-graphics/Native_SDK/blob/4.1/LICENSE_POWERVR_SDK.txt?style=flat)](https://github.com/powervr-graphics/Native_SDK/blob/4.1/LICENSE_POWERVR_SDK.txt/stargazers)]
   *  [Pumex](https://github.com/pumexx/pumex) [![GitHub stars](https://img.shields.io/github/stars/pumexx/pumex?style=flat)](https://github.com/pumexx/pumex/stargazers) - cross-platform Vulkan renderer implementing frame graph and simple scene graph. Able to render on many surfaces at once [MIT]
   *  [SDL](https://discourse.libsdl.org/t/sdl-2-0-6-released/23109) - added cross-platform Vulkan graphics support in SDL_vulkan.h. [zlib]
   *  [small3d](https://www.gamedev.net/projects/515-small3d/), Tiny Vulkan based C++ cross-platform game development framework [BSD 3-clause]
   *  [Spectrum](https://github.com/mwalczyk/spectrum_core) [![GitHub stars](https://img.shields.io/github/stars/mwalczyk/spectrum_core?style=flat)](https://github.com/mwalczyk/spectrum_core/stargazers) - Work-in-progress framework and abstraction layer around Vulkan.
   *  [Tephra](https://github.com/Dolkar/Tephra) [![GitHub stars](https://img.shields.io/github/stars/Dolkar/Tephra?style=flat)](https://github.com/Dolkar/Tephra/stargazers) - A modern C++17 graphics and compute library filling the gap between Vulkan and high-level APIs like OpenGL. [MIT]
   *  [The-Forge](https://github.com/ConfettiFX/The-Forge) [![GitHub stars](https://img.shields.io/github/stars/ConfettiFX/The-Forge?style=flat)](https://github.com/ConfettiFX/The-Forge/stargazers) - DirectX 12, Vulkan, macOS Metal 2 rendering framework. [Apache License 2.0]
   *  [VKFS](https://github.com/MHDtA-dev/VKFS) [![GitHub stars](https://img.shields.io/github/stars/MHDtA-dev/VKFS?style=flat)](https://github.com/MHDtA-dev/VKFS/stargazers) - Cross-platform easy-to-use C++ framework that allows you to quickly initialize Vulkan and get a ready-made environment. Provides high-level abstraction over basic Vulkan objects.
   *  [Vulkan Launchpad](https://github.com/cg-tuwien/VulkanLaunchpad) [![GitHub stars](https://img.shields.io/github/stars/cg-tuwien/VulkanLaunchpad?style=flat)](https://github.com/cg-tuwien/VulkanLaunchpad/stargazers) - Vulkan framework for Windows, macOS, and Linux. Especially well-suited for Vulkan beginners, used in university education, by the Research Unit of Computer Graphics, TU Wien. [MIT]
       * [Vulkan Launchpad Starter](https://github.com/cg-tuwien/VulkanLaunchpadStarter) [![GitHub stars](https://img.shields.io/github/stars/cg-tuwien/VulkanLaunchpadStarter?style=flat)](https://github.com/cg-tuwien/VulkanLaunchpadStarter/stargazers) - Starter template containing additional functionality and assets. [[LICENSE]](https://github.com/cg-tuwien/VulkanLaunchpadStarter/blob/main/LICENSE)

* Other API Interop and Implementations
   *  [visor](https://github.com/baldurk/visor) [![GitHub stars](https://img.shields.io/github/stars/baldurk/visor?style=flat)](https://github.com/baldurk/visor/stargazers) - Vulkan Ignoble Software Rasterizer. [MIT]
   *  [VulkanOnD3D12](https://github.com/Chabloom/VulkanOnD3D12) [![GitHub stars](https://img.shields.io/github/stars/Chabloom/VulkanOnD3D12?style=flat)](https://github.com/Chabloom/VulkanOnD3D12/stargazers) - Vulkan API for D3D12. [Apache License 2.0]
   *  [rostkatze](https://github.com/msiglreith/rostkatze) [![GitHub stars](https://img.shields.io/github/stars/msiglreith/rostkatze?style=flat)](https://github.com/msiglreith/rostkatze/stargazers) - C++ implementation of Vulkan sitting on D3D12 🐈[Apache License 2.0]
   *  [VK9](https://github.com/disks86/VK9) [![GitHub stars](https://img.shields.io/github/stars/disks86/VK9?style=flat)](https://github.com/disks86/VK9/stargazers) - Direct3D 9 compatibility layer using Vulkan
   *  [VUDA](https://github.com/jgbit/vuda) [![GitHub stars](https://img.shields.io/github/stars/jgbit/vuda?style=flat)](https://github.com/jgbit/vuda/stargazers) - header-only lib that provides a CUDA Runtime API interface. [MIT]
   *  [clspv](https://github.com/google/clspv) [![GitHub stars](https://img.shields.io/github/stars/google/clspv?style=flat)](https://github.com/google/clspv/stargazers) - prototype compiler for a subset of OpenCL C to Vulkan compute shaders. [Apache License 2.0]
   *  [MoltenVK](https://github.com/KhronosGroup/MoltenVK/) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/MoltenVK/?style=flat)](https://github.com/KhronosGroup/MoltenVK//stargazers) - run Vulkan on iOS and macOS. [Apache-2.0]
   *  [Zink](https://gitlab.freedesktop.org/kusma/mesa/tree/zink) - OpenGL implementation on top of Vulkan, part of Mesa project. [MIT]
   *  [glo / OpenGL Overload](https://github.com/g-truc/glo) [![GitHub stars](https://img.shields.io/github/stars/g-truc/glo?style=flat)](https://github.com/g-truc/glo/stargazers) - OpenGL implementation on top of Vulkan.
   *  [gfx-portability](https://github.com/gfx-rs/portability) [![GitHub stars](https://img.shields.io/github/stars/gfx-rs/portability?style=flat)](https://github.com/gfx-rs/portability/stargazers) - Vulkan Portability implementation on Metal and D3D12, based on [gfx-rs](https://github.com/gfx-rs/gfx/) [![GitHub stars](https://img.shields.io/github/stars/gfx-rs/gfx/?style=flat)](https://github.com/gfx-rs/gfx//stargazers).

* Raytracing
   *  [Quartz](https://github.com/Nadrin/Quartz) [![GitHub stars](https://img.shields.io/github/stars/Nadrin/Quartz?style=flat)](https://github.com/Nadrin/Quartz/stargazers) - Physically based Vulkan RTX path tracer with a declarative ES7-like scene description language. [LGPL-3.0]

* Scientific
   *  [datoviz](https://github.com/datoviz/datoviz) [![GitHub stars](https://img.shields.io/github/stars/datoviz/datoviz?style=flat)](https://github.com/datoviz/datoviz/stargazers) - High-performance GPU interactive scientific data visualization with Vulkan. [MIT]
   *  [iMSTK](https://gitlab.kitware.com/iMSTK/iMSTK) - C++ toolkit for building surgical simulations with Vulkan and VTK backends. [Apache License 2.0]
  
* Shaders
   *  [glslang](https://github.com/KhronosGroup/glslang) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/glslang?style=flat)](https://github.com/KhronosGroup/glslang/stargazers) - Library for compiling glsl to spirv [BSD 3-Clause]
   *  [SPIRV-Cross](https://github.com/KhronosGroup/SPIRV-Cross) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/SPIRV-Cross?style=flat)](https://github.com/KhronosGroup/SPIRV-Cross/stargazers) - Library for reflection of spirv, simplify the creation of Vulkan pipeline layouts [ Apache-2.0 License]

* Outdated ⚠️
   *  [VkHLF](https://github.com/nvpro-pipeline/VkHLF) [![GitHub stars](https://img.shields.io/github/stars/nvpro-pipeline/VkHLF?style=flat)](https://github.com/nvpro-pipeline/VkHLF/stargazers) - Vulkan High Level Framework. [[LICENSE]](https://github.com/nvpro-pipeline/VkHLF/blob/master/LICENSE.txt)

## Bindings
*  [ash](https://github.com/MaikKlein/ash) [![GitHub stars](https://img.shields.io/github/stars/MaikKlein/ash?style=flat)](https://github.com/MaikKlein/ash/stargazers) - Vulkan bindings for Rust. [MIT]
*  [gfx-rs](https://github.com/gfx-rs/gfx) [![GitHub stars](https://img.shields.io/github/stars/gfx-rs/gfx?style=flat)](https://github.com/gfx-rs/gfx/stargazers) - A low-overhead Vulkan-like GPU API for Rust. [Apache License 2.0]
*  [libvulkan.lua](https://github.com/CapsAdmin/ffibuild/blob/master/vulkan/vulkan.lua) [![GitHub stars](https://img.shields.io/github/stars/CapsAdmin/ffibuild/blob/master/vulkan/vulkan.lua?style=flat)](https://github.com/CapsAdmin/ffibuild/blob/master/vulkan/vulkan.lua/stargazers) - Lua bindings for Vulkan.
*  [dvulkan](https://github.com/ColonelThirtyTwo/dvulkan) [![GitHub stars](https://img.shields.io/github/stars/ColonelThirtyTwo/dvulkan?style=flat)](https://github.com/ColonelThirtyTwo/dvulkan/stargazers) - Auto-generated D bindings for Vulkan.
*  [ErupteD](https://github.com/ParticlePeter/ErupteD) [![GitHub stars](https://img.shields.io/github/stars/ParticlePeter/ErupteD?style=flat)](https://github.com/ParticlePeter/ErupteD/stargazers) - Another Auto-generated D bindings for Vulkan.
*  [flextGL](https://github.com/mosra/flextgl) [![GitHub stars](https://img.shields.io/github/stars/mosra/flextgl?style=flat)](https://github.com/mosra/flextgl/stargazers) - Minimal Vulkan header/loader generator and [the blog post](http://blog.magnum.graphics/hacking/simple-efficient-vulkan-loading-with-flextgl/) about it.
*  [Silk.NET](https://github.com/dotnet/Silk.NET) [![GitHub stars](https://img.shields.io/github/stars/dotnet/Silk.NET?style=flat)](https://github.com/dotnet/Silk.NET/stargazers) - C# bindings for Vulkan and others. [MIT]
*  [vulkan](https://github.com/expipiplus1/vulkan) [![GitHub stars](https://img.shields.io/github/stars/expipiplus1/vulkan?style=flat)](https://github.com/expipiplus1/vulkan/stargazers) - Haskell bindings for Vulkan and Vulkan Memory Allocator [BSD-3-Clause]
*  [nvk](https://github.com/maierfelix/nvk) [![GitHub stars](https://img.shields.io/github/stars/maierfelix/nvk?style=flat)](https://github.com/maierfelix/nvk/stargazers) - JavaScript bindings for Vulkan. [MIT]
*  [racket-vulkan](https://github.com/zyrolasting/racket-vulkan) [![GitHub stars](https://img.shields.io/github/stars/zyrolasting/racket-vulkan?style=flat)](https://github.com/zyrolasting/racket-vulkan/stargazers) - Racket bindings for Vulkan with [detailed implementation notes](https://sagegerard.com/racket-vulkan-notes-index.html). [MIT]
*  [Vulkan-hpp](https://github.com/KhronosGroup/Vulkan-Hpp) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/Vulkan-Hpp?style=flat)](https://github.com/KhronosGroup/Vulkan-Hpp/stargazers) Open-Source Vulkan C++ API originated from NVIDIA and [the blog](https://developer.nvidia.com/open-source-vulkan-c-api) about it.
*  [VulkanSharp](https://github.com/mono/VulkanSharp) [![GitHub stars](https://img.shields.io/github/stars/mono/VulkanSharp?style=flat)](https://github.com/mono/VulkanSharp/stargazers) - C# bindings for Vulkan. [MIT]
*  [Vulkano](https://github.com/vulkano-rs/vulkano) [![GitHub stars](https://img.shields.io/github/stars/vulkano-rs/vulkano?style=flat)](https://github.com/vulkano-rs/vulkano/stargazers) - Safe and rich Rust wrapper around the Vulkan API. [MIT]
*  [LWJGL](https://www.lwjgl.org/) - Lightweight Java Game Library 3 has Vulkan bindings. [BSD]
*  [SharpVk](https://github.com/FacticiusVir/SharpVk) [![GitHub stars](https://img.shields.io/github/stars/FacticiusVir/SharpVk?style=flat)](https://github.com/FacticiusVir/SharpVk/stargazers) - C# bindings for Vulkan with Linq-to-SPIR-V & [NuGet package](https://www.nuget.org/packages/SharpVk). [MIT]
*  [vulkan](https://github.com/realitix/vulkan) [![GitHub stars](https://img.shields.io/github/stars/realitix/vulkan?style=flat)](https://github.com/realitix/vulkan/stargazers) - Ultimate Python bindings for Vulkan generated with CFFI. [Apache Licence 2.0]
*  [vulkan-go](https://github.com/vulkan-go/vulkan) [![GitHub stars](https://img.shields.io/github/stars/vulkan-go/vulkan?style=flat)](https://github.com/vulkan-go/vulkan/stargazers) - Go bindings for Vulkan. [MIT]
*  [PasVulkan](https://github.com/BeRo1985/pasvulkan) [![GitHub stars](https://img.shields.io/github/stars/BeRo1985/pasvulkan?style=flat)](https://github.com/BeRo1985/pasvulkan/stargazers) - Vulkan bindings plus high-level wrapper library for Object Pascal [Zlib]
*  [vulkan-zig](https://github.com/Snektron/vulkan-zig) [![GitHub stars](https://img.shields.io/github/stars/Snektron/vulkan-zig?style=flat)](https://github.com/Snektron/vulkan-zig/stargazers) - Vulkan binding generator for Zig [MIT]
*  [VK²](https://github.com/kotlin-graphics/vkk) [![GitHub stars](https://img.shields.io/github/stars/kotlin-graphics/vkk?style=flat)](https://github.com/kotlin-graphics/vkk/stargazers), Kotlin Wrapper for Vulkan: code expressiveness and safety meet graphic power [Apache License 2.0]
*  [Vortice.Vulkan](https://github.com/amerkoleci/Vortice.Vulkan) [![GitHub stars](https://img.shields.io/github/stars/amerkoleci/Vortice.Vulkan?style=flat)](https://github.com/amerkoleci/Vortice.Vulkan/stargazers) - .NET Standard 2.0 and .NET5 C# bindings [MIT]
*  [Raw Node.js Vulkan API](https://github.com/hydra2s/node-vulkan-api) [![GitHub stars](https://img.shields.io/github/stars/hydra2s/node-vulkan-api?style=flat)](https://github.com/hydra2s/node-vulkan-api/stargazers) - A new Vulkan bindings for Node.JS, similar with LWJGL-3 or NVK.
*  [Deno Vulkan](https://github.com/deno-windowing/vulkan) [![GitHub stars](https://img.shields.io/github/stars/deno-windowing/vulkan?style=flat)](https://github.com/deno-windowing/vulkan/stargazers) - Vulkan API bindings for Deno. [Apache Licence 2.0]

## Tools
*  [Nsight™ Visual Studio Edition 5.2+](https://developer.nvidia.com/nvidia-nsight-visual-studio-edition).
*  [LoaderAndValidationLayers](https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/Vulkan-LoaderAndValidationLayers?style=flat)](https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/stargazers) - from KhronosGroup. [Apache Licence 2.0]
*  [renderdoc](https://github.com/baldurk/renderdoc) [![GitHub stars](https://img.shields.io/github/stars/baldurk/renderdoc?style=flat)](https://github.com/baldurk/renderdoc/stargazers) - by baldurk, a stand-alone graphics debugging tool. [MIT]
    * [RDCtoVkCpp](https://github.com/azhirnov/RDCtoVkCpp) [![GitHub stars](https://img.shields.io/github/stars/azhirnov/RDCtoVkCpp?style=flat)](https://github.com/azhirnov/RDCtoVkCpp/stargazers) - converts RenderDoc Vulkan capture to compilable and executable C++ code. [MIT]
*  [VulkanTools](https://github.com/LunarG/VulkanTools) [![GitHub stars](https://img.shields.io/github/stars/LunarG/VulkanTools?style=flat)](https://github.com/LunarG/VulkanTools/stargazers) - LunarG's tools including layers and configurator. [Apache Licence 2.0]
*  [VKtracer](https://www.vktracer.com) - universal and easy-to-use profiler for Vulkan.
*  [CodeXL](https://github.com/GPUOpen-Tools/CodeXL) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-Tools/CodeXL?style=flat)](https://github.com/GPUOpen-Tools/CodeXL/stargazers) - CodeXL goes open source. [MIT]
*  [Qualcomm Adreno GPU Tools](https://developer.qualcomm.com/software/adreno-gpu-sdk/tools) - samples, Adreno recommendation layer, best practice docs for Adreno GPU.
*  [Qualcomm Snapdragon Profiler](https://developer.qualcomm.com/software/snapdragon-profiler) - includes Vulkan traces and frame captures for Adreno GPU.
*  [Arm Mobile Studio](https://www.arm.com/products/development-tools/graphics/arm-mobile-studio) - includes the Arm Graphics Analyzer to trace graphics performance issues easily, and Arm Streamline performance analyzer, for a whole-system view of performance to determine bottlenecks quickly across both the CPU and GPU.
*  [Open Capture and Analytics Tool (OCAT)](https://github.com/GPUOpen-Tools/OCAT) [![GitHub stars](https://img.shields.io/github/stars/GPUOpen-Tools/OCAT?style=flat)](https://github.com/GPUOpen-Tools/OCAT/stargazers) - provides an FPS overlay and performance measurement for D3D11, D3D12, and Vulkan. [MIT]
*  [gapid](https://github.com/google/gapid) [![GitHub stars](https://img.shields.io/github/stars/google/gapid?style=flat)](https://github.com/google/gapid/stargazers) - Graphics API Debugger, can trace and replay Android OpenGL ES and Vulkan applications. [Apache License 2.0]
*  [Arm - PerfDoc](https://github.com/ARM-software/perfdoc) [![GitHub stars](https://img.shields.io/github/stars/ARM-software/perfdoc?style=flat)](https://github.com/ARM-software/perfdoc/stargazers) - a validation layer against the Mali Application Developer Best Practices document. [MIT]
*  [glsl_trace](https://github.com/azhirnov/glsl_trace) [![GitHub stars](https://img.shields.io/github/stars/azhirnov/glsl_trace?style=flat)](https://github.com/azhirnov/glsl_trace/stargazers) - library for shader debugging and profiling for Vulkan and OpenGL. [MIT]
*  [MangoHud](https://github.com/flightlessmango/MangoHud) [![GitHub stars](https://img.shields.io/github/stars/flightlessmango/MangoHud?style=flat)](https://github.com/flightlessmango/MangoHud/stargazers) - Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load. [MIT]

## Books
* [Introduction to Computer Graphics and the Vulkan API](https://www.amazon.com/Introduction-Computer-Graphics-Vulkan-API/dp/1548616176) by **Kenwright** - Introduce the reader to the exciting topic of computer graphics from a grounds-up practical perspective with the Vulkan API.
* [Learning Vulkan](https://www.amazon.com/Learning-Vulkan-Parminder-Singh/dp/1786469804) - by **Parminder Singh** - Get started with the Vulkan API and its programming techniques using the easy-to-follow examples.
  * [Book's Examples](https://github.com/PacktPublishing/Learning-Vulkan) [![GitHub stars](https://img.shields.io/github/stars/PacktPublishing/Learning-Vulkan?style=flat)](https://github.com/PacktPublishing/Learning-Vulkan/stargazers)
* [Vulkan Cookbook](https://www.amazon.com/Vulkan-Cookbook-Pawel-Lapinski/dp/1786468158)- by **Pawel Lapinski** - Explores a wide range of graphics programming and GPU compute methods to make the best use of the Vulkan API.
  * [Book's Examples](https://github.com/PacktPublishing/Vulkan-Cookbook) [![GitHub stars](https://img.shields.io/github/stars/PacktPublishing/Vulkan-Cookbook?style=flat)](https://github.com/PacktPublishing/Vulkan-Cookbook/stargazers)
* [Vulkan Programming Guide](https://www.amazon.com/Vulkan-Programming-Guide-Official-Learning/dp/0134464540) - by **Graham Sellers** and **John Kessenich** - Introduces powerful 3D development techniques for many fields.
* [Mastering Graphics Programming with Vulkan](https://www.amazon.com/Mastering-Graphics-Programming-Vulkan-state/dp/1803244798/ref=sr_1_1?keywords=mastering+graphics+programming+with+vulkan&qid=1678290788&sprefix=mastering+graphics+%2Caps%2C255&sr=8-1) - Develop a modern rendering engine from first principles to state-of-the-art techniques, by **Marco Castorina** and **Gabriel Sassone**.

## Papers
*  [The Road to Vulkan: Teaching Modern Low-Level APIs in Introductory Graphics Courses](https://www.cg.tuwien.ac.at/research/publications/2022/unterguggenberger-2022-vulkan) by **Johannes Unterguggenberger**, **Bernhard Kerbl**, and **Michael Wimmer**, Eurographics 2022 - Education Papers
    *  Direct link to the [paper](https://www.cg.tuwien.ac.at/research/publications/2022/unterguggenberger-2022-vulkan/unterguggenberger-2022-vulkan-paper.pdf).
    *  Pre-recorded presentation on [YouTube](https://youtu.be/ZG0ct4V6c0k).

## Khronos
*  Specification
    *  Vulkan 1.0 Core API ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.0/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.0/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.0/html/vkspec.html))
    *  Vulkan 1.0 Core API + Khronos-defined Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.0-wsi_extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.0-wsi_extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.0-wsi_extensions/html/vkspec.html))
    *  Vulkan 1.0 Core API + all registered Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.0-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.0-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.0-extensions/html/vkspec.html)) 
    *  Vulkan 1.1 Core API ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.1/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.1/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.1/html/vkspec.html))
    *  Vulkan 1.1 Core API + Khronos-defined Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.1-khr-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.1-khr-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.1-khr-extensions/html/vkspec.html))
    *  Vulkan 1.1 Core API + all registered Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.1-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/vkspec.html)) 
    *  Vulkan 1.2 Core API ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.2/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.2/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.2/html/vkspec.html))
    *  Vulkan 1.2 Core API + Khronos-defined Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.2-khr-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.2-khr-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.2-khr-extensions/html/vkspec.html))
    *  Vulkan 1.2 Core API + all registered Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.2-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.2-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.2-extensions/html/vkspec.html)) 
    *  Vulkan 1.3 Core API ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.3/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.3/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.3/html/vkspec.html))
    *  Vulkan 1.3 Core API + Khronos-defined Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.3-khr-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.3-khr-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.3-khr-extensions/html/vkspec.html))
    *  Vulkan 1.3 Core API + all registered Extensions ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.3-extensions/pdf/vkspec.pdf)) ([Single-file HTML](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html)) 
*  Quick Reference Sheets
    *  [Vulkan 1.0 Quick Reference Sheets](https://www.khronos.org/registry/vulkan/specs/1.0/refguide/Vulkan-1.0-web.pdf)
    *  [Vulkan 1.1 Quick Reference Sheets](https://www.khronos.org/registry/vulkan/specs/1.1/refguide/Vulkan-1.1-web.pdf)
*  [Conformance Tests (CTS)](https://github.com/KhronosGroup/Vulkan-CTS) [![GitHub stars](https://img.shields.io/github/stars/KhronosGroup/Vulkan-CTS?style=flat)](https://github.com/KhronosGroup/Vulkan-CTS/stargazers)
*  Conferences and Presentations
    *  [GDC 2016 Presentations](https://www.khronos.org/developers/library/2016-gdc)
    *  [2016 UK Chapter: Moving to Vulkan](https://www.khronos.org/developers/library/2016-uk-chapter-moving-to-vulkan)
    *  [SIGGRAPH 2016 BOF - Vulkan](https://www.youtube.com/watch?v=CsHMiEQgrLA)
    *  [SIGGRPAH 2016 Best Practices Roundtable](https://www.youtube.com/watch?v=owuJRPKIUAg)
    *  [2016 Vulkan DevDay UK](https://www.khronos.org/developers/library/2016-vulkan-devday-uk)
    *  [2016 Vulkan DevDay Seoul](https://www.khronos.org/developers/library/2016-Vulkan-DevU-Seoul)
    *  [2017 Vulkan DevU Vancouver](https://www.khronos.org/developers/library/2017-vulkan-devu-vancouver)
    *  [2017 Vulkan Loader Webinar](https://www.khronos.org/developers/library/2017-vulkan-loader-webinar)
    *  [SIGGRAPH 2017 BOF - Vulkan](https://www.youtube.com/watch?v=Nx0u-9ZwrmQ)
    *  [2018 Vulkan Montreal Dev Day](https://www.khronos.org/developers/library/2018-vulkan-montreal-dev-day)
    *  [2018 Vulkanised!](https://www.khronos.org/developers/library/2018-vulkanised)
    *  [SIGGRAPH 2018 BOF - Vulkan](https://www.youtube.com/watch?v=FCAM-3aAzXg&t=18350s)

## Community
*  [Freenode IRC](http://webchat.freenode.net/?channels=Vulkan)
*  [Google Plus](https://plus.google.com/communities/108983304183191634377)
*  [Khronos Forum](https://forums.khronos.org/forumdisplay.php/114-Vulkan)
*  [Reddit](https://www.reddit.com/r/vulkan/)
*  [Stack Overflow](http://stackoverflow.com/questions/tagged/vulkan)
*  [Discord](https://discord.com/invite/tFdvbEj)

## Related lists
*  [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) - Curated list of awesome lists.
*  [awesome-opengl](https://github.com/eug/awesome-opengl) [![GitHub stars](https://img.shields.io/github/stars/eug/awesome-opengl?style=flat)](https://github.com/eug/awesome-opengl/stargazers) - Curated list of awesome OpenGL libraries, debuggers and resources.
*  [gamedev](https://github.com/ellisonleao/magictools) [![GitHub stars](https://img.shields.io/github/stars/ellisonleao/magictools?style=flat)](https://github.com/ellisonleao/magictools/stargazers) - Awesome list about game development.
*  [graphics-resources](https://github.com/mattdesl/graphics-resources) [![GitHub stars](https://img.shields.io/github/stars/mattdesl/graphics-resources?style=flat)](https://github.com/mattdesl/graphics-resources/stargazers) - List of graphic programming resources.
*  [awesome-d3d12](https://github.com/vinjn/awesome-d3d12) [![GitHub stars](https://img.shields.io/github/stars/vinjn/awesome-d3d12?style=flat)](https://github.com/vinjn/awesome-d3d12/stargazers) - Curated list of awesome D3D12 libraries, debuggers and resources.

## License

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

## Contributing
Please see [CONTRIBUTING](https://github.com/vinjn/awesome-vulkan/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/vinjn/awesome-vulkan/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/vinjn/awesome-vulkan/blob/master/CONTRIBUTING.md/stargazers) for details.
