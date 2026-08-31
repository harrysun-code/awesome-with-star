# Python

> 来源：[vinta/awesome-python](https://github.com/vinta/awesome-python)

[![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers)

# [Awesome Python](https://awesome-python.com/)

An opinionated guide to the best Python frameworks, libraries, and tools.

**Visit the [website](https://awesome-python.com/) to search and filter projects more easily.**

## **Sponsors**

> The **#10 most-starred repo on GitHub**. Put your product in front of Python developers. [Become a sponsor](SPONSORSHIP.md).

## Categories

**AI & ML**

- [AI and Agents](#ai-and-agents)
- [Deep Learning](#deep-learning)
- [Machine Learning](#machine-learning)
- [Natural Language Processing](#natural-language-processing)
- [Computer Vision](#computer-vision)
- [Recommender Systems](#recommender-systems)

**Web Development**

- [Web Frameworks](#web-frameworks)
- [Web APIs](#web-apis)
- [Web Servers](#web-servers)
- [WebSocket](#websocket)
- [Template Engines](#template-engines)
- [Web Asset Management](#web-asset-management)
- [Authentication](#authentication)
- [Admin Panels](#admin-panels)
- [CMS](#cms)
- [ERP](#erp)
- [Static Site Generators](#static-site-generators)

**HTTP & Scraping**

- [HTTP Clients](#http-clients)
- [Web Scraping](#web-scraping)
- [Email](#email)

**Database & Storage**

- [ORM](#orm)
- [Database Drivers](#database-drivers)
- [Database](#database)
- [Caching](#caching)
- [Search](#search)
- [Serialization](#serialization)

**Data & Science**

- [Data Analysis](#data-analysis)
- [Data Ingestion / ETL](#data-ingestion--etl)
- [Data Validation](#data-validation)
- [Data Visualization](#data-visualization)
- [Geolocation](#geolocation)
- [Science](#science)
- [Quantum Computing](#quantum-computing)

**Developer Tools**

- [Algorithms and Design Patterns](#algorithms-and-design-patterns)
- [Interactive Interpreter](#interactive-interpreter)
- [Code Analysis](#code-analysis)
- [Testing](#testing)
- [Debugging Tools](#debugging-tools)
- [Build Tools](#build-tools)
- [Documentation](#documentation)

**DevOps**

- [DevOps Tools](#devops-tools)
- [Distributed Computing](#distributed-computing)
- [Task Queues](#task-queues)
- [Messaging](#messaging)
- [Job Schedulers](#job-schedulers)
- [Logging](#logging)
- [Network Virtualization](#network-virtualization)

**CLI & GUI**

- [CLI Development](#cli-development)
- [CLI Tools](#cli-tools)
- [GUI Development](#gui-development)

**Text & Documents**

- [Text Processing](#text-processing)
- [HTML Manipulation](#html-manipulation)
- [File Format Processing](#file-format-processing)
- [File Manipulation](#file-manipulation)

**Media**

- [Image Processing](#image-processing)
- [Audio & Video Processing](#audio--video-processing)
- [Game Development](#game-development)

**Python Language**

- [Implementations](#implementations)
- [Built-in Classes Enhancement](#built-in-classes-enhancement)
- [Functional Programming](#functional-programming)
- [Asynchronous Programming](#asynchronous-programming)
- [Date and Time](#date-and-time)

**Python Toolchain**

- [Environment Management](#environment-management)
- [Package Management](#package-management)
- [Package Repositories](#package-repositories)
- [Distribution](#distribution)
- [Configuration Files](#configuration-files)

**Security**

- [Cryptography](#cryptography)
- [Penetration Testing](#penetration-testing)
- [Supply Chain Security](#supply-chain-security)
- [Web Security](#web-security)

**Other**

- [Hardware](#hardware)
- [Microsoft Windows](#microsoft-windows)
- [Miscellaneous](#miscellaneous)

## Projects

**AI & ML**

### AI and Agents

_Libraries for building AI applications, LLM integrations, and autonomous agents._

- Agent Skills
  - [django-ai-plugins](https://github.com/vintasoftware/django-ai-plugins) [![GitHub stars](https://img.shields.io/github/stars/vintasoftware/django-ai-plugins?style=flat)](https://github.com/vintasoftware/django-ai-plugins/stargazers) - Django backend agent skills for Django, DRF, Celery, and Django-specific code review.
  - [sentry-skills](https://github.com/getsentry/skills) [![GitHub stars](https://img.shields.io/github/stars/getsentry/skills?style=flat)](https://github.com/getsentry/skills/stargazers) - Python-focused engineering skills for code review, debugging, and backend workflows.
  - [trailofbits-skills](https://github.com/trailofbits/skills) [![GitHub stars](https://img.shields.io/github/stars/trailofbits/skills?style=flat)](https://github.com/trailofbits/skills/stargazers) - Python-friendly security skills for auditing, testing, and safer backend development.
- Orchestration
  - [langchain](https://github.com/langchain-ai/langchain) [![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat)](https://github.com/langchain-ai/langchain/stargazers) - Building applications with LLMs through composability.
  - [langgraph](https://github.com/langchain-ai/langgraph) [![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat)](https://github.com/langchain-ai/langgraph/stargazers) - Low-level orchestration framework for building stateful, long-running LLM agents.
  - [crewai](https://github.com/crewAIInc/crewAI) [![GitHub stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat)](https://github.com/crewAIInc/crewAI/stargazers) - A framework for orchestrating role-playing autonomous AI agents for collaborative task solving.
  - [pydantic-ai](https://github.com/pydantic/pydantic-ai) [![GitHub stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat)](https://github.com/pydantic/pydantic-ai/stargazers) - A Python agent framework for building generative AI applications with structured schemas.
- Vendor Agent SDKs
  - [openai-agents](https://github.com/openai/openai-agents-python) [![GitHub stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat)](https://github.com/openai/openai-agents-python/stargazers) - OpenAI's framework for building and managing AI agents.
  - [claude-agent-sdk](https://github.com/anthropics/claude-agent-sdk-python) [![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-agent-sdk-python?style=flat)](https://github.com/anthropics/claude-agent-sdk-python/stargazers) - Anthropic's Python SDK for building AI agents on Claude Code's harness — custom tools, in-process MCP servers, hooks.
- Personal Assistants
  - [hermes-agent](https://github.com/nousresearch/hermes-agent) [![GitHub stars](https://img.shields.io/github/stars/nousresearch/hermes-agent?style=flat)](https://github.com/nousresearch/hermes-agent/stargazers) - An adaptive personal AI assistant that grows with you.
- Prompt Optimization
  - [dspy](https://github.com/stanfordnlp/dspy) [![GitHub stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat)](https://github.com/stanfordnlp/dspy/stargazers) - A framework for programming, not prompting, language models.
- Data Layer
  - [instructor](https://github.com/567-labs/instructor) [![GitHub stars](https://img.shields.io/github/stars/567-labs/instructor?style=flat)](https://github.com/567-labs/instructor/stargazers) - A library for extracting structured data from LLMs, powered by Pydantic.
  - [llama-index](https://github.com/run-llama/llama_index) [![GitHub stars](https://img.shields.io/github/stars/run-llama/llama_index?style=flat)](https://github.com/run-llama/llama_index/stargazers) - A data framework for your LLM application.
  - [mem0](https://github.com/mem0ai/mem0) [![GitHub stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat)](https://github.com/mem0ai/mem0/stargazers) - An intelligent memory layer for AI agents enabling personalized interactions.
  - [openviking](https://github.com/volcengine/OpenViking) [![GitHub stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=flat)](https://github.com/volcengine/OpenViking/stargazers) - A context database for AI agents that unifies memory, resources, and skills.
  - [semantica](https://github.com/semantica-agi/semantica) [![GitHub stars](https://img.shields.io/github/stars/semantica-agi/semantica?style=flat)](https://github.com/semantica-agi/semantica/stargazers) - A graph-native context and knowledge layer for AI agents with reasoning, provenance, and governance.
- Pre-trained Models
  - [transformers](https://github.com/huggingface/transformers) [![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=flat)](https://github.com/huggingface/transformers/stargazers) - A framework that lets you easily use pre-trained transformer models for NLP, vision, and audio tasks.
- LLM Inference and Serving
  - [sglang](https://github.com/sgl-project/sglang) [![GitHub stars](https://img.shields.io/github/stars/sgl-project/sglang?style=flat)](https://github.com/sgl-project/sglang/stargazers) - A high-performance serving framework for large language models and multimodal models.
  - [vllm](https://github.com/vllm-project/vllm) [![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat)](https://github.com/vllm-project/vllm/stargazers) - A high-throughput and memory-efficient inference and serving engine for LLMs.
  - [mlx-lm](https://github.com/ml-explore/mlx-lm) [![GitHub stars](https://img.shields.io/github/stars/ml-explore/mlx-lm?style=flat)](https://github.com/ml-explore/mlx-lm/stargazers) - Run and fine-tune large language models on Apple Silicon with MLX.
- LLM Gateways
  - [LiteLLM](https://github.com/BerriAI/litellm) [![GitHub stars](https://img.shields.io/github/stars/BerriAI/litellm?style=flat)](https://github.com/BerriAI/litellm/stargazers) - Call 100+ LLMs using OpenAI format.
- Image and Video Generation
  - [diffusers](https://github.com/huggingface/diffusers) [![GitHub stars](https://img.shields.io/github/stars/huggingface/diffusers?style=flat)](https://github.com/huggingface/diffusers/stargazers) - A library that provides pre-trained diffusion models for generating and editing images, audio, and video.
- Fine-tuning
  - [unsloth](https://github.com/unslothai/unsloth) [![GitHub stars](https://img.shields.io/github/stars/unslothai/unsloth?style=flat)](https://github.com/unslothai/unsloth/stargazers) - A library for faster LLM fine-tuning and training with reduced memory usage.
- Speech
  - [openai-whisper](https://github.com/openai/whisper) [![GitHub stars](https://img.shields.io/github/stars/openai/whisper?style=flat)](https://github.com/openai/whisper/stargazers) - A general-purpose automatic speech recognition model trained on 680k hours of multilingual and multitask supervised data.
  - [funasr](https://github.com/modelscope/FunASR) [![GitHub stars](https://img.shields.io/github/stars/modelscope/FunASR?style=flat)](https://github.com/modelscope/FunASR/stargazers) - Industrial-grade speech recognition toolkit with 170x realtime speed, 50+ languages, speaker diarization, and emotion detection.
  - [vibevoice](https://github.com/microsoft/VibeVoice) [![GitHub stars](https://img.shields.io/github/stars/microsoft/VibeVoice?style=flat)](https://github.com/microsoft/VibeVoice/stargazers) - A family of open-source voice AI models from Microsoft for text-to-speech and long-form speech recognition.
  - [gTTS](https://github.com/pndurette/gTTS) [![GitHub stars](https://img.shields.io/github/stars/pndurette/gTTS?style=flat)](https://github.com/pndurette/gTTS/stargazers) - Python library and CLI tool for converting text to speech using Google Translate TTS.
  - [kittentts](https://github.com/KittenML/KittenTTS) [![GitHub stars](https://img.shields.io/github/stars/KittenML/KittenTTS?style=flat)](https://github.com/KittenML/KittenTTS/stargazers) - Lightweight ONNX text-to-speech library with small CPU-friendly models.

### Deep Learning

_Frameworks for Neural Networks and Deep Learning. Also see [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) [![GitHub stars](https://img.shields.io/github/stars/ChristosChristofidis/awesome-deep-learning?style=flat)](https://github.com/ChristosChristofidis/awesome-deep-learning/stargazers)._

- Frameworks
  - [pytorch](https://github.com/pytorch/pytorch) [![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch?style=flat)](https://github.com/pytorch/pytorch/stargazers) - Tensors and Dynamic neural networks in Python with strong GPU acceleration.
  - [tensorflow](https://github.com/tensorflow/tensorflow) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=flat)](https://github.com/tensorflow/tensorflow/stargazers) - The most popular Deep Learning framework created by Google.
  - [keras](https://github.com/keras-team/keras) [![GitHub stars](https://img.shields.io/github/stars/keras-team/keras?style=flat)](https://github.com/keras-team/keras/stargazers) - A high-level deep learning library with support for JAX, TensorFlow, and PyTorch backends.
  - [jax](https://github.com/jax-ml/jax) [![GitHub stars](https://img.shields.io/github/stars/jax-ml/jax?style=flat)](https://github.com/jax-ml/jax/stargazers) - A library for high-performance numerical computing with automatic differentiation and JIT compilation.
  - [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) [![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/pytorch-lightning?style=flat)](https://github.com/Lightning-AI/pytorch-lightning/stargazers) - Deep learning framework to train, deploy, and ship AI products Lightning fast.
- Reinforcement Learning
  - [gymnasium](https://github.com/Farama-Foundation/Gymnasium) [![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium?style=flat)](https://github.com/Farama-Foundation/Gymnasium/stargazers) - A standard API for reinforcement learning environments with popular reference environments ([gym](https://github.com/openai/gym) [![GitHub stars](https://img.shields.io/github/stars/openai/gym?style=flat)](https://github.com/openai/gym/stargazers) successor).
  - [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) [![GitHub stars](https://img.shields.io/github/stars/DLR-RM/stable-baselines3?style=flat)](https://github.com/DLR-RM/stable-baselines3/stargazers) - PyTorch implementations of Stable Baselines (deep) reinforcement learning algorithms.

### Machine Learning

_Libraries for Machine Learning. Also see [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python) [![GitHub stars](https://img.shields.io/github/stars/josephmisiti/awesome-machine-learning?style=flat)](https://github.com/josephmisiti/awesome-machine-learning/stargazers)._

- General
  - [scikit-learn](https://github.com/scikit-learn/scikit-learn) [![GitHub stars](https://img.shields.io/github/stars/scikit-learn/scikit-learn?style=flat)](https://github.com/scikit-learn/scikit-learn/stargazers) - The most popular Python library for Machine Learning with extensive documentation and community support.
  - [pgmpy](https://github.com/pgmpy/pgmpy) [![GitHub stars](https://img.shields.io/github/stars/pgmpy/pgmpy?style=flat)](https://github.com/pgmpy/pgmpy/stargazers) - A Python library for probabilistic graphical models and Bayesian networks.
  - [feature-engine](https://github.com/feature-engine/feature_engine) [![GitHub stars](https://img.shields.io/github/stars/feature-engine/feature_engine?style=flat)](https://github.com/feature-engine/feature_engine/stargazers) - sklearn compatible API with the widest toolset for feature engineering and selection.
- Gradient Boosting
  - [xgboost](https://github.com/dmlc/xgboost) [![GitHub stars](https://img.shields.io/github/stars/dmlc/xgboost?style=flat)](https://github.com/dmlc/xgboost/stargazers) - A scalable, portable, and distributed gradient boosting library.
  - [lightgbm](https://github.com/lightgbm-org/LightGBM) [![GitHub stars](https://img.shields.io/github/stars/lightgbm-org/LightGBM?style=flat)](https://github.com/lightgbm-org/LightGBM/stargazers) - A fast, distributed, high performance gradient boosting framework.
  - [catboost](https://github.com/catboost/catboost) [![GitHub stars](https://img.shields.io/github/stars/catboost/catboost?style=flat)](https://github.com/catboost/catboost/stargazers) - A fast, scalable, high performance gradient boosting on decision trees library.
- Time Series Forecasting
  - [timesfm](https://github.com/google-research/timesfm) [![GitHub stars](https://img.shields.io/github/stars/google-research/timesfm?style=flat)](https://github.com/google-research/timesfm/stargazers) - A pretrained foundation model from Google Research for time-series forecasting.

### Natural Language Processing

_Libraries for working with human languages._

- General
  - [nltk](https://github.com/nltk/nltk) [![GitHub stars](https://img.shields.io/github/stars/nltk/nltk?style=flat)](https://github.com/nltk/nltk/stargazers) - A leading platform for building Python programs to work with human language data.
  - [spacy](https://github.com/explosion/spaCy) [![GitHub stars](https://img.shields.io/github/stars/explosion/spaCy?style=flat)](https://github.com/explosion/spaCy/stargazers) - A library for industrial-strength natural language processing in Python and Cython.
  - [gensim](https://github.com/piskvorky/gensim) [![GitHub stars](https://img.shields.io/github/stars/piskvorky/gensim?style=flat)](https://github.com/piskvorky/gensim/stargazers) - Topic Modeling for Humans.
  - [stanza](https://github.com/stanfordnlp/stanza) [![GitHub stars](https://img.shields.io/github/stars/stanfordnlp/stanza?style=flat)](https://github.com/stanfordnlp/stanza/stargazers) - The Stanford NLP Group's official Python library, supporting 60+ languages.
- Chinese
  - [jieba](https://github.com/fxsjy/jieba) [![GitHub stars](https://img.shields.io/github/stars/fxsjy/jieba?style=flat)](https://github.com/fxsjy/jieba/stargazers) - The most popular Chinese text segmentation library.
  - [pypinyin](https://github.com/mozillazg/python-pinyin) [![GitHub stars](https://img.shields.io/github/stars/mozillazg/python-pinyin?style=flat)](https://github.com/mozillazg/python-pinyin/stargazers) - Convert Chinese hanzi (漢字) to pinyin (拼音).
  - [pangu.py](https://github.com/vinta/pangu.py) [![GitHub stars](https://img.shields.io/github/stars/vinta/pangu.py?style=flat)](https://github.com/vinta/pangu.py/stargazers) - Paranoid text spacing.

### Computer Vision

_Libraries for Computer Vision._

- General
  - [opencv-python](https://github.com/opencv/opencv-python) [![GitHub stars](https://img.shields.io/github/stars/opencv/opencv-python?style=flat)](https://github.com/opencv/opencv-python/stargazers) - Open Source Computer Vision Library.
  - [ultralytics](https://github.com/ultralytics/ultralytics) [![GitHub stars](https://img.shields.io/github/stars/ultralytics/ultralytics?style=flat)](https://github.com/ultralytics/ultralytics/stargazers) - Ultralytics YOLO for object detection, segmentation, pose estimation, and classification with state-of-the-art accuracy and speed.
  - [kornia](https://github.com/kornia/kornia/) [![GitHub stars](https://img.shields.io/github/stars/kornia/kornia/?style=flat)](https://github.com/kornia/kornia//stargazers) - Open Source Differentiable Computer Vision Library for PyTorch.
  - [fiftyone](https://github.com/voxel51/fiftyone) [![GitHub stars](https://img.shields.io/github/stars/voxel51/fiftyone?style=flat)](https://github.com/voxel51/fiftyone/stargazers) - The open-source tool for building high-quality datasets and computer vision models.
- OCR
  - [pytesseract](https://github.com/madmaze/pytesseract) [![GitHub stars](https://img.shields.io/github/stars/madmaze/pytesseract?style=flat)](https://github.com/madmaze/pytesseract/stargazers) - A wrapper for [Google Tesseract OCR](https://github.com/tesseract-ocr) [![GitHub stars](https://img.shields.io/github/stars/tesseract-ocr?style=flat)](https://github.com/tesseract-ocr/stargazers).
  - [easyocr](https://github.com/JaidedAI/EasyOCR) [![GitHub stars](https://img.shields.io/github/stars/JaidedAI/EasyOCR?style=flat)](https://github.com/JaidedAI/EasyOCR/stargazers) - Ready-to-use OCR with 40+ languages supported.

### Recommender Systems

_Libraries for building recommender systems._

- [annoy](https://github.com/spotify/annoy) [![GitHub stars](https://img.shields.io/github/stars/spotify/annoy?style=flat)](https://github.com/spotify/annoy/stargazers) - Approximate Nearest Neighbors in C++/Python optimized for memory usage.
- [implicit](https://github.com/benfred/implicit) [![GitHub stars](https://img.shields.io/github/stars/benfred/implicit?style=flat)](https://github.com/benfred/implicit/stargazers) - A fast Python implementation of collaborative filtering for implicit datasets.
- [scikit-surprise](https://github.com/NicolasHug/Surprise) [![GitHub stars](https://img.shields.io/github/stars/NicolasHug/Surprise?style=flat)](https://github.com/NicolasHug/Surprise/stargazers) - A scikit for building and analyzing recommender systems.

**Web Development**

### Web Frameworks

_Traditional full stack web frameworks. Also see [Web APIs](#web-apis)._

- Synchronous
  - [flask](https://github.com/pallets/flask) [![GitHub stars](https://img.shields.io/github/stars/pallets/flask?style=flat)](https://github.com/pallets/flask/stargazers) - A microframework for Python.
    - [awesome-flask](https://github.com/humiaozuzu/awesome-flask) [![GitHub stars](https://img.shields.io/github/stars/humiaozuzu/awesome-flask?style=flat)](https://github.com/humiaozuzu/awesome-flask/stargazers)
  - [django](https://github.com/django/django) [![GitHub stars](https://img.shields.io/github/stars/django/django?style=flat)](https://github.com/django/django/stargazers) - The most popular web framework in Python.
    - [awesome-django](https://github.com/wsvincent/awesome-django) [![GitHub stars](https://img.shields.io/github/stars/wsvincent/awesome-django?style=flat)](https://github.com/wsvincent/awesome-django/stargazers)
  - [bottle](https://github.com/bottlepy/bottle) [![GitHub stars](https://img.shields.io/github/stars/bottlepy/bottle?style=flat)](https://github.com/bottlepy/bottle/stargazers) - A fast and simple micro-framework distributed as a single file with no dependencies.
  - [pyramid](https://github.com/Pylons/pyramid) [![GitHub stars](https://img.shields.io/github/stars/Pylons/pyramid?style=flat)](https://github.com/Pylons/pyramid/stargazers) - A small, fast, down-to-earth, open source Python web framework.
    - [awesome-pyramid](https://github.com/uralbash/awesome-pyramid) [![GitHub stars](https://img.shields.io/github/stars/uralbash/awesome-pyramid?style=flat)](https://github.com/uralbash/awesome-pyramid/stargazers)
  - [fasthtml](https://github.com/AnswerDotAI/fasthtml) [![GitHub stars](https://img.shields.io/github/stars/AnswerDotAI/fasthtml?style=flat)](https://github.com/AnswerDotAI/fasthtml/stargazers) - The fastest way to create an HTML app.
    - [awesome-fasthtml](https://github.com/amosgyamfi/awesome-fasthtml) [![GitHub stars](https://img.shields.io/github/stars/amosgyamfi/awesome-fasthtml?style=flat)](https://github.com/amosgyamfi/awesome-fasthtml/stargazers)
- Asynchronous
  - [starlette](https://github.com/Kludex/starlette) [![GitHub stars](https://img.shields.io/github/stars/Kludex/starlette?style=flat)](https://github.com/Kludex/starlette/stargazers) - A lightweight ASGI framework and toolkit for building high-performance async services.
  - [tornado](https://github.com/tornadoweb/tornado) [![GitHub stars](https://img.shields.io/github/stars/tornadoweb/tornado?style=flat)](https://github.com/tornadoweb/tornado/stargazers) - A web framework and asynchronous networking library.
  - [litestar](https://github.com/litestar-org/litestar) [![GitHub stars](https://img.shields.io/github/stars/litestar-org/litestar?style=flat)](https://github.com/litestar-org/litestar/stargazers) - Production-ready, capable and extensible ASGI Web framework.
  - [reflex](https://github.com/reflex-dev/reflex) [![GitHub stars](https://img.shields.io/github/stars/reflex-dev/reflex?style=flat)](https://github.com/reflex-dev/reflex/stargazers) - A framework for building reactive, full-stack web applications entirely with Python.

### Web APIs

_Libraries for building RESTful, GraphQL, and RPC APIs._

- Django
  - [django-rest-framework](https://github.com/encode/django-rest-framework) [![GitHub stars](https://img.shields.io/github/stars/encode/django-rest-framework?style=flat)](https://github.com/encode/django-rest-framework/stargazers) - A powerful and flexible toolkit to build web APIs.
  - [django-ninja](https://github.com/vitalik/django-ninja) [![GitHub stars](https://img.shields.io/github/stars/vitalik/django-ninja?style=flat)](https://github.com/vitalik/django-ninja/stargazers) - Fast, Django REST framework based on type hints and Pydantic.
  - [strawberry-django](https://github.com/strawberry-graphql/strawberry-django) [![GitHub stars](https://img.shields.io/github/stars/strawberry-graphql/strawberry-django?style=flat)](https://github.com/strawberry-graphql/strawberry-django/stargazers) - Strawberry GraphQL integration with Django.
  - [django-modern-rest](https://github.com/wemake-services/django-modern-rest) [![GitHub stars](https://img.shields.io/github/stars/wemake-services/django-modern-rest?style=flat)](https://github.com/wemake-services/django-modern-rest/stargazers) - Modern REST with speed, types, async, `msgspec`, `pydantic` and other goodies!
- Flask
  - [apiflask](https://github.com/apiflask/apiflask) [![GitHub stars](https://img.shields.io/github/stars/apiflask/apiflask?style=flat)](https://github.com/apiflask/apiflask/stargazers) - A lightweight Python web API framework based on Flask and Marshmallow.
- Framework Agnostic
  - [fastapi](https://github.com/fastapi/fastapi) [![GitHub stars](https://img.shields.io/github/stars/fastapi/fastapi?style=flat)](https://github.com/fastapi/fastapi/stargazers) - A modern, fast, web framework for building APIs with standard Python type hints.
  - [connexion](https://github.com/spec-first/connexion) [![GitHub stars](https://img.shields.io/github/stars/spec-first/connexion?style=flat)](https://github.com/spec-first/connexion/stargazers) - A spec-first framework that automatically handles requests based on your OpenAPI specification.
  - [strawberry](https://github.com/strawberry-graphql/strawberry) [![GitHub stars](https://img.shields.io/github/stars/strawberry-graphql/strawberry?style=flat)](https://github.com/strawberry-graphql/strawberry/stargazers) - A GraphQL library that leverages Python type annotations for schema definition.
- RPC
  - [grpcio](https://github.com/grpc/grpc) [![GitHub stars](https://img.shields.io/github/stars/grpc/grpc?style=flat)](https://github.com/grpc/grpc/stargazers) - HTTP/2-based RPC framework with Python bindings, built by Google.

### Web Servers

_ASGI and WSGI compatible web servers._

- ASGI
  - [uvicorn](https://github.com/Kludex/uvicorn) [![GitHub stars](https://img.shields.io/github/stars/Kludex/uvicorn?style=flat)](https://github.com/Kludex/uvicorn/stargazers) - A lightning-fast ASGI server implementation, using uvloop and httptools.
  - [granian](https://github.com/emmett-framework/granian) [![GitHub stars](https://img.shields.io/github/stars/emmett-framework/granian?style=flat)](https://github.com/emmett-framework/granian/stargazers) - A Rust HTTP server for Python applications built on top of Hyper and Tokio, supporting WSGI/ASGI/RSGI.
  - [hypercorn](https://github.com/pgjones/hypercorn) [![GitHub stars](https://img.shields.io/github/stars/pgjones/hypercorn?style=flat)](https://github.com/pgjones/hypercorn/stargazers) - An ASGI and WSGI Server based on Hyper libraries and inspired by Gunicorn.
- WSGI
  - [gunicorn](https://github.com/benoitc/gunicorn) [![GitHub stars](https://img.shields.io/github/stars/benoitc/gunicorn?style=flat)](https://github.com/benoitc/gunicorn/stargazers) - Pre-forked, ported from Ruby's Unicorn project.
  - [waitress](https://github.com/Pylons/waitress) [![GitHub stars](https://img.shields.io/github/stars/Pylons/waitress?style=flat)](https://github.com/Pylons/waitress/stargazers) - Multi-threaded, powers Pyramid.

### WebSocket

_Libraries for working with WebSocket._

- [websockets](https://github.com/python-websockets/websockets) [![GitHub stars](https://img.shields.io/github/stars/python-websockets/websockets?style=flat)](https://github.com/python-websockets/websockets/stargazers) - A library for building WebSocket servers and clients with a focus on correctness and simplicity.
- [channels](https://github.com/django/channels) [![GitHub stars](https://img.shields.io/github/stars/django/channels?style=flat)](https://github.com/django/channels/stargazers) - Developer-friendly asynchrony for Django.
- [flask-socketio](https://github.com/miguelgrinberg/Flask-SocketIO) [![GitHub stars](https://img.shields.io/github/stars/miguelgrinberg/Flask-SocketIO?style=flat)](https://github.com/miguelgrinberg/Flask-SocketIO/stargazers) - Socket.IO integration for Flask applications.
- [autobahn-python](https://github.com/crossbario/autobahn-python) [![GitHub stars](https://img.shields.io/github/stars/crossbario/autobahn-python?style=flat)](https://github.com/crossbario/autobahn-python/stargazers) - WebSocket & WAMP for Python on Twisted and [asyncio](https://docs.python.org/3/library/asyncio.html).

### Template Engines

_Libraries and tools for templating and lexing._

- [jinja](https://github.com/pallets/jinja) [![GitHub stars](https://img.shields.io/github/stars/pallets/jinja?style=flat)](https://github.com/pallets/jinja/stargazers) - A modern and designer friendly templating language.
- [mako](https://github.com/sqlalchemy/mako) [![GitHub stars](https://img.shields.io/github/stars/sqlalchemy/mako?style=flat)](https://github.com/sqlalchemy/mako/stargazers) - Hyperfast and lightweight templating for the Python platform.

### Web Asset Management

_Tools for managing, storing, compressing and minifying website assets._

- [django-storages](https://github.com/jschneier/django-storages) [![GitHub stars](https://img.shields.io/github/stars/jschneier/django-storages?style=flat)](https://github.com/jschneier/django-storages/stargazers) - A collection of custom storage back ends for Django.
- [django-compressor](https://github.com/django-compressor/django-compressor) [![GitHub stars](https://img.shields.io/github/stars/django-compressor/django-compressor?style=flat)](https://github.com/django-compressor/django-compressor/stargazers) - Compresses linked and inline JavaScript or CSS into a single cached file.

### Authentication

_Libraries for implementing authentication schemes._

- OAuth
  - [oauthlib](https://github.com/oauthlib/oauthlib) [![GitHub stars](https://img.shields.io/github/stars/oauthlib/oauthlib?style=flat)](https://github.com/oauthlib/oauthlib/stargazers) - A generic and thorough implementation of the OAuth request-signing logic.
  - [authlib](https://github.com/authlib/authlib) [![GitHub stars](https://img.shields.io/github/stars/authlib/authlib?style=flat)](https://github.com/authlib/authlib/stargazers) - A comprehensive library for building OAuth, OpenID Connect, and JWT/JWS/JWE/JWK/JWA.
  - [django-allauth](https://github.com/pennersr/django-allauth) [![GitHub stars](https://img.shields.io/github/stars/pennersr/django-allauth?style=flat)](https://github.com/pennersr/django-allauth/stargazers) - Authentication app for Django that "just works."
  - [django-oauth-toolkit](https://github.com/django-oauth/django-oauth-toolkit) [![GitHub stars](https://img.shields.io/github/stars/django-oauth/django-oauth-toolkit?style=flat)](https://github.com/django-oauth/django-oauth-toolkit/stargazers) - OAuth 2 goodies for Django.
- JWT
  - [pyjwt](https://github.com/jpadilla/pyjwt) [![GitHub stars](https://img.shields.io/github/stars/jpadilla/pyjwt?style=flat)](https://github.com/jpadilla/pyjwt/stargazers) - JSON Web Token implementation in Python.
- Permissions
  - [django-guardian](https://github.com/django-guardian/django-guardian) [![GitHub stars](https://img.shields.io/github/stars/django-guardian/django-guardian?style=flat)](https://github.com/django-guardian/django-guardian/stargazers) - Implementation of per-object permissions for Django.
  - [django-rules](https://github.com/dfunckt/django-rules) [![GitHub stars](https://img.shields.io/github/stars/dfunckt/django-rules?style=flat)](https://github.com/dfunckt/django-rules/stargazers) - A tiny but powerful app providing object-level permissions to Django, without requiring a database.

### Admin Panels

_Libraries for administrative interfaces._

- [flask-admin](https://github.com/pallets-eco/flask-admin) [![GitHub stars](https://img.shields.io/github/stars/pallets-eco/flask-admin?style=flat)](https://github.com/pallets-eco/flask-admin/stargazers) - Simple and extensible administrative interface framework for Flask.
- [django-unfold](https://github.com/unfoldadmin/django-unfold) [![GitHub stars](https://img.shields.io/github/stars/unfoldadmin/django-unfold?style=flat)](https://github.com/unfoldadmin/django-unfold/stargazers) - Elevate your Django admin with a stunning modern interface, powerful features, and seamless user experience.
- [django-grappelli](https://github.com/sehmaschine/django-grappelli) [![GitHub stars](https://img.shields.io/github/stars/sehmaschine/django-grappelli?style=flat)](https://github.com/sehmaschine/django-grappelli/stargazers) - A jazzy skin for the Django Admin-Interface.

### CMS

_Content Management Systems._

- [wagtail](https://github.com/wagtail/wagtail) [![GitHub stars](https://img.shields.io/github/stars/wagtail/wagtail?style=flat)](https://github.com/wagtail/wagtail/stargazers) - A Django content management system.
- [django-cms](https://github.com/django-cms/django-cms) [![GitHub stars](https://img.shields.io/github/stars/django-cms/django-cms?style=flat)](https://github.com/django-cms/django-cms/stargazers) - The easy-to-use and developer-friendly enterprise CMS powered by Django.

### ERP

_Enterprise resource planning frameworks._

- [odoo](https://github.com/odoo/odoo) [![GitHub stars](https://img.shields.io/github/stars/odoo/odoo?style=flat)](https://github.com/odoo/odoo/stargazers) - A suite of open source business apps: CRM, e-commerce, accounting, inventory, and thousands of community modules.

### Static Site Generators

_Static site generator is a software that takes some text + templates as input and produces HTML files on the output._

- [pelican](https://github.com/getpelican/pelican) [![GitHub stars](https://img.shields.io/github/stars/getpelican/pelican?style=flat)](https://github.com/getpelican/pelican/stargazers) - Static site generator that supports Markdown and reST syntax.
- [nikola](https://github.com/getnikola/nikola) [![GitHub stars](https://img.shields.io/github/stars/getnikola/nikola?style=flat)](https://github.com/getnikola/nikola/stargazers) - A static website and blog generator.

**HTTP & Scraping**

### HTTP Clients

_Libraries for working with HTTP._

- Clients
  - [requests](https://github.com/psf/requests) [![GitHub stars](https://img.shields.io/github/stars/psf/requests?style=flat)](https://github.com/psf/requests/stargazers) - HTTP Requests for Humans.
  - [httpx](https://github.com/encode/httpx) [![GitHub stars](https://img.shields.io/github/stars/encode/httpx?style=flat)](https://github.com/encode/httpx/stargazers) - A next generation HTTP client for Python.
  - [aiohttp](https://github.com/aio-libs/aiohttp) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiohttp?style=flat)](https://github.com/aio-libs/aiohttp/stargazers) - Asynchronous HTTP client/server framework for asyncio and Python.
  - [urllib3](https://github.com/urllib3/urllib3) [![GitHub stars](https://img.shields.io/github/stars/urllib3/urllib3?style=flat)](https://github.com/urllib3/urllib3/stargazers) - A HTTP library with thread-safe connection pooling, file post support, sanity friendly.
  - [httpx2](https://github.com/pydantic/httpx2) [![GitHub stars](https://img.shields.io/github/stars/pydantic/httpx2?style=flat)](https://github.com/pydantic/httpx2/stargazers) - HTTP/1.1 and HTTP/2 client with sync and async APIs, maintained by Pydantic ([httpx](https://github.com/encode/httpx) [![GitHub stars](https://img.shields.io/github/stars/encode/httpx?style=flat)](https://github.com/encode/httpx/stargazers) fork).
- URL Manipulation
  - [yarl](https://github.com/aio-libs/yarl) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/yarl?style=flat)](https://github.com/aio-libs/yarl/stargazers) - Yet another URL library.

### Web Scraping

_Libraries to automate web scraping and extract web content._

- Frameworks
  - [browser-use](https://github.com/browser-use/browser-use) [![GitHub stars](https://img.shields.io/github/stars/browser-use/browser-use?style=flat)](https://github.com/browser-use/browser-use/stargazers) - Make websites accessible for AI agents with easy browser automation.
  - [scrapy](https://github.com/scrapy/scrapy) [![GitHub stars](https://img.shields.io/github/stars/scrapy/scrapy?style=flat)](https://github.com/scrapy/scrapy/stargazers) - A fast high-level screen scraping and web crawling framework.
  - [crawl4ai](https://github.com/unclecode/crawl4ai) [![GitHub stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=flat)](https://github.com/unclecode/crawl4ai/stargazers) - An open-source, LLM-friendly web crawler that provides lightning-fast, structured data extraction specifically designed for AI agents.
- Content Extraction
  - [feedparser](https://github.com/kurtmckee/feedparser) [![GitHub stars](https://img.shields.io/github/stars/kurtmckee/feedparser?style=flat)](https://github.com/kurtmckee/feedparser/stargazers) - Universal feed parser.
  - [html2text](https://github.com/Alir3z4/html2text) [![GitHub stars](https://img.shields.io/github/stars/Alir3z4/html2text?style=flat)](https://github.com/Alir3z4/html2text/stargazers) - Convert HTML to Markdown-formatted text.
  - [trafilatura](https://github.com/adbar/trafilatura) [![GitHub stars](https://img.shields.io/github/stars/adbar/trafilatura?style=flat)](https://github.com/adbar/trafilatura/stargazers) - A tool for gathering text and metadata from the web, with built-in content filtering.

### Email

_Libraries for sending and parsing email, and mail server management._

- [yagmail](https://github.com/kootenpv/yagmail) [![GitHub stars](https://img.shields.io/github/stars/kootenpv/yagmail?style=flat)](https://github.com/kootenpv/yagmail/stargazers) - Yet another Gmail/SMTP client.

**Database & Storage**

### ORM

_Libraries that implement Object-Relational Mapping or data mapping techniques._

- Relational Databases
  - [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/sqlalchemy/sqlalchemy?style=flat)](https://github.com/sqlalchemy/sqlalchemy/stargazers) - The Python SQL Toolkit and Object Relational Mapper.
    - [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/dahlia/awesome-sqlalchemy?style=flat)](https://github.com/dahlia/awesome-sqlalchemy/stargazers)
  - [django.db.models](https://github.com/django/django) [![GitHub stars](https://img.shields.io/github/stars/django/django?style=flat)](https://github.com/django/django/stargazers) - (part of Django) The Django [ORM](https://docs.djangoproject.com/en/dev/topics/db/models/).
  - [peewee](https://github.com/coleifer/peewee) [![GitHub stars](https://img.shields.io/github/stars/coleifer/peewee?style=flat)](https://github.com/coleifer/peewee/stargazers) - A small, expressive ORM.
  - [sqlmodel](https://github.com/fastapi/sqlmodel) [![GitHub stars](https://img.shields.io/github/stars/fastapi/sqlmodel?style=flat)](https://github.com/fastapi/sqlmodel/stargazers) - SQLModel is based on Python type annotations, and powered by Pydantic and SQLAlchemy.
- NoSQL Databases
  - [pynamodb](https://github.com/pynamodb/PynamoDB) [![GitHub stars](https://img.shields.io/github/stars/pynamodb/PynamoDB?style=flat)](https://github.com/pynamodb/PynamoDB/stargazers) - A Pythonic interface for [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).
  - [mongoengine](https://github.com/MongoEngine/mongoengine) [![GitHub stars](https://img.shields.io/github/stars/MongoEngine/mongoengine?style=flat)](https://github.com/MongoEngine/mongoengine/stargazers) - A Python Object-Document-Mapper for working with MongoDB.
  - [beanie](https://github.com/BeanieODM/beanie) [![GitHub stars](https://img.shields.io/github/stars/BeanieODM/beanie?style=flat)](https://github.com/BeanieODM/beanie/stargazers) - An asynchronous Python object-document mapper (ODM) for MongoDB.

### Database Drivers

_Libraries for connecting and operating databases._

- MySQL - [awesome-mysql](https://github.com/shlomi-noach/awesome-mysql) [![GitHub stars](https://img.shields.io/github/stars/shlomi-noach/awesome-mysql?style=flat)](https://github.com/shlomi-noach/awesome-mysql/stargazers)
  - [pymysql](https://github.com/PyMySQL/PyMySQL) [![GitHub stars](https://img.shields.io/github/stars/PyMySQL/PyMySQL?style=flat)](https://github.com/PyMySQL/PyMySQL/stargazers) - A pure Python MySQL driver compatible to mysql-python.
  - [mysqlclient](https://github.com/PyMySQL/mysqlclient) [![GitHub stars](https://img.shields.io/github/stars/PyMySQL/mysqlclient?style=flat)](https://github.com/PyMySQL/mysqlclient/stargazers) - MySQL connector with Python 3 support ([mysql-python](https://sourceforge.net/projects/mysql-python/) fork).
- PostgreSQL - [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres) [![GitHub stars](https://img.shields.io/github/stars/dhamaniasad/awesome-postgres?style=flat)](https://github.com/dhamaniasad/awesome-postgres/stargazers)
  - [psycopg](https://github.com/psycopg/psycopg) [![GitHub stars](https://img.shields.io/github/stars/psycopg/psycopg?style=flat)](https://github.com/psycopg/psycopg/stargazers) - The most popular PostgreSQL adapter for Python.
  - [asyncpg](https://github.com/MagicStack/asyncpg) [![GitHub stars](https://img.shields.io/github/stars/MagicStack/asyncpg?style=flat)](https://github.com/MagicStack/asyncpg/stargazers) - A fast PostgreSQL Database Client Library for Python/asyncio.
- SQLite - [awesome-sqlite](https://github.com/planetopendata/awesome-sqlite) [![GitHub stars](https://img.shields.io/github/stars/planetopendata/awesome-sqlite?style=flat)](https://github.com/planetopendata/awesome-sqlite/stargazers)
  - [sqlite3](https://docs.python.org/3/library/sqlite3.html) - (Python standard library) SQLite interface compliant with DB-API 2.0.
  - [sqlite-utils](https://github.com/simonw/sqlite-utils) [![GitHub stars](https://img.shields.io/github/stars/simonw/sqlite-utils?style=flat)](https://github.com/simonw/sqlite-utils/stargazers) - Python CLI utility and library for manipulating SQLite databases.
- ClickHouse
  - [clickhouse-connect](https://github.com/ClickHouse/clickhouse-connect) [![GitHub stars](https://img.shields.io/github/stars/ClickHouse/clickhouse-connect?style=flat)](https://github.com/ClickHouse/clickhouse-connect/stargazers) - The official ClickHouse client, with SQLAlchemy and Superset connectors.
  - [clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver) [![GitHub stars](https://img.shields.io/github/stars/mymarilyn/clickhouse-driver?style=flat)](https://github.com/mymarilyn/clickhouse-driver/stargazers) - Python driver with native interface for ClickHouse.
- Other Relational Databases
  - [pyodbc](https://github.com/mkleehammer/pyodbc) [![GitHub stars](https://img.shields.io/github/stars/mkleehammer/pyodbc?style=flat)](https://github.com/mkleehammer/pyodbc/stargazers) - An ODBC bridge for connecting to SQL Server and any other ODBC-accessible database.
  - [oracledb](https://github.com/oracle/python-oracledb) [![GitHub stars](https://img.shields.io/github/stars/oracle/python-oracledb?style=flat)](https://github.com/oracle/python-oracledb/stargazers) - The official Python driver for Oracle Database, successor to cx_Oracle.
  - [mssql-python](https://github.com/microsoft/mssql-python) [![GitHub stars](https://img.shields.io/github/stars/microsoft/mssql-python?style=flat)](https://github.com/microsoft/mssql-python/stargazers) - Official Microsoft driver for SQL Server and Azure SQL, built on ODBC for high performance and low memory usage.
- NoSQL Databases
  - [redis](https://github.com/redis/redis-py) [![GitHub stars](https://img.shields.io/github/stars/redis/redis-py?style=flat)](https://github.com/redis/redis-py/stargazers) - The Python client for Redis.
  - [pymongo](https://github.com/mongodb/mongo-python-driver) [![GitHub stars](https://img.shields.io/github/stars/mongodb/mongo-python-driver?style=flat)](https://github.com/mongodb/mongo-python-driver/stargazers) - The official Python client for MongoDB.
  - [cassandra-driver](https://github.com/apache/cassandra-python-driver) [![GitHub stars](https://img.shields.io/github/stars/apache/cassandra-python-driver?style=flat)](https://github.com/apache/cassandra-python-driver/stargazers) - The Python Driver for Apache Cassandra.
  - [django-mongodb-backend](https://github.com/mongodb/django-mongodb-backend) [![GitHub stars](https://img.shields.io/github/stars/mongodb/django-mongodb-backend?style=flat)](https://github.com/mongodb/django-mongodb-backend/stargazers) - Official MongoDB database backend for Django.

### Database

_In-process databases usable directly from Python._

- Analytical
  - [duckdb](https://github.com/duckdb/duckdb) [![GitHub stars](https://img.shields.io/github/stars/duckdb/duckdb?style=flat)](https://github.com/duckdb/duckdb/stargazers) - An in-process SQL OLAP database management system; optimized for analytics and fast queries, similar to SQLite but for analytical workloads.
  - [chdb](https://github.com/chdb-io/chdb) [![GitHub stars](https://img.shields.io/github/stars/chdb-io/chdb?style=flat)](https://github.com/chdb-io/chdb/stargazers) - In-process OLAP SQL engine with the full ClickHouse dialect, zero-copy pandas/Arrow interop, and federation to remote ClickHouse clusters via `remoteSecure()`.
- Vector
  - [chromadb](https://github.com/chroma-core/chroma) [![GitHub stars](https://img.shields.io/github/stars/chroma-core/chroma?style=flat)](https://github.com/chroma-core/chroma/stargazers) - An open-source embedding database for building AI applications with embeddings and semantic search.
  - [lancedb](https://github.com/lancedb/lancedb) [![GitHub stars](https://img.shields.io/github/stars/lancedb/lancedb?style=flat)](https://github.com/lancedb/lancedb/stargazers) - A developer-friendly embedded retrieval database for multimodal AI.
  - [zvec](https://github.com/alibaba/zvec) [![GitHub stars](https://img.shields.io/github/stars/alibaba/zvec?style=flat)](https://github.com/alibaba/zvec/stargazers) - An embedded vector database for on-device RAG and edge AI, the SQLite of vector databases.
- Key-Value & Document
  - [tinydb](https://github.com/msiemens/tinydb) [![GitHub stars](https://img.shields.io/github/stars/msiemens/tinydb?style=flat)](https://github.com/msiemens/tinydb/stargazers) - A tiny, document-oriented database.

### Caching

_Libraries for caching data._

- [cachetools](https://github.com/tkem/cachetools) [![GitHub stars](https://img.shields.io/github/stars/tkem/cachetools?style=flat)](https://github.com/tkem/cachetools/stargazers) - Extensible memoizing collections and decorators.
- [diskcache](https://github.com/grantjenks/python-diskcache) [![GitHub stars](https://img.shields.io/github/stars/grantjenks/python-diskcache?style=flat)](https://github.com/grantjenks/python-diskcache/stargazers) - SQLite and file backed cache backend with faster lookups than memcached and redis.
- [hishel](https://github.com/karpetrosyan/hishel) [![GitHub stars](https://img.shields.io/github/stars/karpetrosyan/hishel?style=flat)](https://github.com/karpetrosyan/hishel/stargazers) - RFC 9111 compliant HTTP caching for httpx and requests, with sync and async support.
- [dogpile.cache](https://github.com/sqlalchemy/dogpile.cache) [![GitHub stars](https://img.shields.io/github/stars/sqlalchemy/dogpile.cache?style=flat)](https://github.com/sqlalchemy/dogpile.cache/stargazers) - dogpile.cache is a next generation replacement for Beaker made by the same authors.
- [django-cacheops](https://github.com/Suor/django-cacheops) [![GitHub stars](https://img.shields.io/github/stars/Suor/django-cacheops?style=flat)](https://github.com/Suor/django-cacheops/stargazers) - A slick ORM cache with automatic granular event-driven invalidation.

### Search

_Libraries and software for indexing and performing search queries on data._

- [elasticsearch](https://github.com/elastic/elasticsearch-py) [![GitHub stars](https://img.shields.io/github/stars/elastic/elasticsearch-py?style=flat)](https://github.com/elastic/elasticsearch-py/stargazers) - The official low-level Python client for [Elasticsearch](https://www.elastic.co/products/elasticsearch).
- [opensearch-py](https://github.com/opensearch-project/opensearch-py) [![GitHub stars](https://img.shields.io/github/stars/opensearch-project/opensearch-py?style=flat)](https://github.com/opensearch-project/opensearch-py/stargazers) - The official low-level Python client for [OpenSearch](https://opensearch.org/).
- [meilisearch](https://github.com/meilisearch/meilisearch-python) [![GitHub stars](https://img.shields.io/github/stars/meilisearch/meilisearch-python?style=flat)](https://github.com/meilisearch/meilisearch-python/stargazers) - The official Python client for the [Meilisearch](https://www.meilisearch.com/) search engine.
- [django-haystack](https://github.com/django-haystack/django-haystack) [![GitHub stars](https://img.shields.io/github/stars/django-haystack/django-haystack?style=flat)](https://github.com/django-haystack/django-haystack/stargazers) - Modular search for Django.

### Serialization

_Libraries for serializing complex data types._

- [msgpack](https://github.com/msgpack/msgpack-python) [![GitHub stars](https://img.shields.io/github/stars/msgpack/msgpack-python?style=flat)](https://github.com/msgpack/msgpack-python/stargazers) - MessagePack serializer implementation for Python.
- [orjson](https://github.com/ijl/orjson) [![GitHub stars](https://img.shields.io/github/stars/ijl/orjson?style=flat)](https://github.com/ijl/orjson/stargazers) - Fast, correct JSON library.
- [marshmallow](https://github.com/marshmallow-code/marshmallow) [![GitHub stars](https://img.shields.io/github/stars/marshmallow-code/marshmallow?style=flat)](https://github.com/marshmallow-code/marshmallow/stargazers) - A lightweight library for converting complex objects to and from simple Python datatypes.
- [msgspec](https://github.com/msgspec/msgspec) [![GitHub stars](https://img.shields.io/github/stars/msgspec/msgspec?style=flat)](https://github.com/msgspec/msgspec/stargazers) - A fast serialization and validation library with built-in support for JSON, MessagePack, YAML, and TOML.

**Data & Science**

### Data Analysis

_Libraries for data analysis._

- [pandas](https://github.com/pandas-dev/pandas) [![GitHub stars](https://img.shields.io/github/stars/pandas-dev/pandas?style=flat)](https://github.com/pandas-dev/pandas/stargazers) - A library providing high-performance, easy-to-use data structures and data analysis tools.
- [polars](https://github.com/pola-rs/polars) [![GitHub stars](https://img.shields.io/github/stars/pola-rs/polars?style=flat)](https://github.com/pola-rs/polars/stargazers) - A fast DataFrame library implemented in Rust with a Python API.
- [ibis-framework](https://github.com/ibis-project/ibis) [![GitHub stars](https://img.shields.io/github/stars/ibis-project/ibis?style=flat)](https://github.com/ibis-project/ibis/stargazers) - A portable Python dataframe library with a single API for 20+ backends.

### Data Ingestion / ETL

_Libraries for data extraction, transformation, and loading pipelines across multiple sources and destinations._

- General
  - [awswrangler](https://github.com/aws/aws-sdk-pandas) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-pandas?style=flat)](https://github.com/aws/aws-sdk-pandas/stargazers) - Pandas integration with AWS services like Athena, Glue, Redshift, S3, and DynamoDB.
  - [dlt](https://github.com/dlt-hub/dlt) [![GitHub stars](https://img.shields.io/github/stars/dlt-hub/dlt?style=flat)](https://github.com/dlt-hub/dlt/stargazers) - A Python library for building data pipelines with automatic schema inference, incremental loading, and support for multiple sources and destinations.
  - [pathway](https://github.com/pathwaycom/pathway) [![GitHub stars](https://img.shields.io/github/stars/pathwaycom/pathway?style=flat)](https://github.com/pathwaycom/pathway/stargazers) - Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.
- Financial Data
  - [yfinance](https://github.com/ranaroussi/yfinance) [![GitHub stars](https://img.shields.io/github/stars/ranaroussi/yfinance?style=flat)](https://github.com/ranaroussi/yfinance/stargazers) - Easy Pythonic way to download market and financial data from Yahoo Finance.
  - [akshare](https://github.com/akfamily/akshare) [![GitHub stars](https://img.shields.io/github/stars/akfamily/akshare?style=flat)](https://github.com/akfamily/akshare/stargazers) - A financial data interface library, built for human beings!
  - [edgartools](https://github.com/dgunning/edgartools) [![GitHub stars](https://img.shields.io/github/stars/dgunning/edgartools?style=flat)](https://github.com/dgunning/edgartools/stargazers) - Library for downloading structured data from SEC EDGAR filings and XBRL financial statements.
  - [openbb](https://github.com/OpenBB-finance/OpenBB) [![GitHub stars](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=flat)](https://github.com/OpenBB-finance/OpenBB/stargazers) - A financial data platform for analysts, quants and AI agents.

### Data Validation

_Libraries for validating data. Used for forms in many cases._

- [pydantic](https://github.com/pydantic/pydantic) [![GitHub stars](https://img.shields.io/github/stars/pydantic/pydantic?style=flat)](https://github.com/pydantic/pydantic/stargazers) - Data validation using Python type hints.
- [jsonschema](https://github.com/python-jsonschema/jsonschema) [![GitHub stars](https://img.shields.io/github/stars/python-jsonschema/jsonschema?style=flat)](https://github.com/python-jsonschema/jsonschema/stargazers) - An implementation of [JSON Schema](https://json-schema.org/) for Python.
- [pandera](https://github.com/unionai-oss/pandera) [![GitHub stars](https://img.shields.io/github/stars/unionai-oss/pandera?style=flat)](https://github.com/unionai-oss/pandera/stargazers) - A data validation library for dataframes, with support for pandas, polars, and Spark.

### Data Visualization

_Libraries for visualizing data. Also see [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization) [![GitHub stars](https://img.shields.io/github/stars/sorrycc/awesome-javascript?style=flat)](https://github.com/sorrycc/awesome-javascript/stargazers)._

- Plotting
  - [matplotlib](https://github.com/matplotlib/matplotlib) [![GitHub stars](https://img.shields.io/github/stars/matplotlib/matplotlib?style=flat)](https://github.com/matplotlib/matplotlib/stargazers) - A Python 2D plotting library.
  - [plotly](https://github.com/plotly/plotly.py) [![GitHub stars](https://img.shields.io/github/stars/plotly/plotly.py?style=flat)](https://github.com/plotly/plotly.py/stargazers) - Interactive graphing library for Python.
  - [seaborn](https://github.com/mwaskom/seaborn) [![GitHub stars](https://img.shields.io/github/stars/mwaskom/seaborn?style=flat)](https://github.com/mwaskom/seaborn/stargazers) - Statistical data visualization using Matplotlib.
  - [altair](https://github.com/vega/altair) [![GitHub stars](https://img.shields.io/github/stars/vega/altair?style=flat)](https://github.com/vega/altair/stargazers) - Declarative statistical visualization library for Python.
  - [bokeh](https://github.com/bokeh/bokeh) [![GitHub stars](https://img.shields.io/github/stars/bokeh/bokeh?style=flat)](https://github.com/bokeh/bokeh/stargazers) - Interactive Web Plotting for Python.
- Specialized
  - [cartopy](https://github.com/SciTools/cartopy) [![GitHub stars](https://img.shields.io/github/stars/SciTools/cartopy?style=flat)](https://github.com/SciTools/cartopy/stargazers) - A cartographic python library with matplotlib support.
  - [pygraphviz](https://github.com/pygraphviz/pygraphviz/) [![GitHub stars](https://img.shields.io/github/stars/pygraphviz/pygraphviz/?style=flat)](https://github.com/pygraphviz/pygraphviz//stargazers) - Python interface to [Graphviz](https://www.graphviz.org/).
  - [graphify](https://github.com/Graphify-Labs/graphify) [![GitHub stars](https://img.shields.io/github/stars/Graphify-Labs/graphify?style=flat)](https://github.com/Graphify-Labs/graphify/stargazers) - Turn any folder of code, SQL schemas, docs, papers, images, or videos into a queryable knowledge graph.
- Dashboards and Apps
  - [streamlit](https://github.com/streamlit/streamlit) [![GitHub stars](https://img.shields.io/github/stars/streamlit/streamlit?style=flat)](https://github.com/streamlit/streamlit/stargazers) - A framework which lets you build dashboards, generate reports, or create chat apps in minutes.
  - [gradio](https://github.com/gradio-app/gradio) [![GitHub stars](https://img.shields.io/github/stars/gradio-app/gradio?style=flat)](https://github.com/gradio-app/gradio/stargazers) - Build and share machine learning apps, all in Python.

### Geolocation

_Libraries for geocoding addresses and working with latitudes and longitudes._

- [geopandas](https://github.com/geopandas/geopandas) [![GitHub stars](https://img.shields.io/github/stars/geopandas/geopandas?style=flat)](https://github.com/geopandas/geopandas/stargazers) - Python tools for geographic data (GeoSeries/GeoDataFrame) built on pandas.
- [geopy](https://github.com/geopy/geopy) [![GitHub stars](https://img.shields.io/github/stars/geopy/geopy?style=flat)](https://github.com/geopy/geopy/stargazers) - Python Geocoding Toolbox.
- [geojson](https://github.com/jazzband/geojson) [![GitHub stars](https://img.shields.io/github/stars/jazzband/geojson?style=flat)](https://github.com/jazzband/geojson/stargazers) - Python bindings and utilities for GeoJSON.
- [geodjango](https://github.com/django/django) [![GitHub stars](https://img.shields.io/github/stars/django/django?style=flat)](https://github.com/django/django/stargazers) - (part of Django) A world-class [geographic web framework](https://docs.djangoproject.com/en/dev/ref/contrib/gis/).

### Science

_Libraries for scientific computing. Also see [Python-for-Scientists](https://github.com/TomNicholas/Python-for-Scientists) [![GitHub stars](https://img.shields.io/github/stars/TomNicholas/Python-for-Scientists?style=flat)](https://github.com/TomNicholas/Python-for-Scientists/stargazers)._

- Core
  - [numpy](https://github.com/numpy/numpy) [![GitHub stars](https://img.shields.io/github/stars/numpy/numpy?style=flat)](https://github.com/numpy/numpy/stargazers) - A fundamental package for scientific computing with Python.
  - [scipy](https://github.com/scipy/scipy) [![GitHub stars](https://img.shields.io/github/stars/scipy/scipy?style=flat)](https://github.com/scipy/scipy/stargazers) - A Python-based ecosystem of open-source software for mathematics, science, and engineering.
  - [numba](https://github.com/numba/numba) [![GitHub stars](https://img.shields.io/github/stars/numba/numba?style=flat)](https://github.com/numba/numba/stargazers) - Python JIT compiler to LLVM aimed at scientific Python.
- Symbolic Mathematics
  - [sympy](https://github.com/sympy/sympy) [![GitHub stars](https://img.shields.io/github/stars/sympy/sympy?style=flat)](https://github.com/sympy/sympy/stargazers) - A Python library for symbolic mathematics.
- Statistics
  - [statsmodels](https://github.com/statsmodels/statsmodels) [![GitHub stars](https://img.shields.io/github/stars/statsmodels/statsmodels?style=flat)](https://github.com/statsmodels/statsmodels/stargazers) - Statistical modeling and econometrics in Python.
- Biology and Chemistry
  - [biopython](https://github.com/biopython/biopython) [![GitHub stars](https://img.shields.io/github/stars/biopython/biopython?style=flat)](https://github.com/biopython/biopython/stargazers) - Biopython is a set of freely available tools for biological computation.
  - [rdkit](https://github.com/rdkit/rdkit) [![GitHub stars](https://img.shields.io/github/stars/rdkit/rdkit?style=flat)](https://github.com/rdkit/rdkit/stargazers) - Cheminformatics and Machine Learning Software.
- Physics and Engineering
  - [pint](https://github.com/hgrecco/pint) [![GitHub stars](https://img.shields.io/github/stars/hgrecco/pint?style=flat)](https://github.com/hgrecco/pint/stargazers) - Operate and manipulate physical quantities with units and dimensional analysis.
  - [astropy](https://github.com/astropy/astropy) [![GitHub stars](https://img.shields.io/github/stars/astropy/astropy?style=flat)](https://github.com/astropy/astropy/stargazers) - A community Python library for Astronomy.
  - [obspy](https://github.com/obspy/obspy) [![GitHub stars](https://img.shields.io/github/stars/obspy/obspy?style=flat)](https://github.com/obspy/obspy/stargazers) - A Python toolbox for seismology.
- Simulation and Modeling
  - [pymc](https://github.com/pymc-devs/pymc) [![GitHub stars](https://img.shields.io/github/stars/pymc-devs/pymc?style=flat)](https://github.com/pymc-devs/pymc/stargazers) - Probabilistic programming and Bayesian modeling in Python.
  - [simpy](https://gitlab.com/team-simpy/simpy) - A process-based discrete-event simulation framework.
  - [mesa](https://github.com/mesa/mesa) [![GitHub stars](https://img.shields.io/github/stars/mesa/mesa?style=flat)](https://github.com/mesa/mesa/stargazers) - An agent-based modeling framework for building, analyzing, and visualizing complex system simulations.
- Graphs and Networks
  - [networkx](https://github.com/networkx/networkx) [![GitHub stars](https://img.shields.io/github/stars/networkx/networkx?style=flat)](https://github.com/networkx/networkx/stargazers) - A high-productivity software for complex networks.
- Computational Geometry
  - [shapely](https://github.com/shapely/shapely) [![GitHub stars](https://img.shields.io/github/stars/shapely/shapely?style=flat)](https://github.com/shapely/shapely/stargazers) - Manipulation and analysis of geometric objects in the Cartesian plane.
- Other
  - [colour-science](https://github.com/colour-science/colour) [![GitHub stars](https://img.shields.io/github/stars/colour-science/colour?style=flat)](https://github.com/colour-science/colour/stargazers) - Implementing a comprehensive number of colour theory transformations and algorithms.
  - [manim](https://github.com/ManimCommunity/manim) [![GitHub stars](https://img.shields.io/github/stars/ManimCommunity/manim?style=flat)](https://github.com/ManimCommunity/manim/stargazers) - An animation engine for explanatory math videos.

### Quantum Computing

_Libraries for quantum computing._

- [qiskit](https://github.com/Qiskit/qiskit) [![GitHub stars](https://img.shields.io/github/stars/Qiskit/qiskit?style=flat)](https://github.com/Qiskit/qiskit/stargazers) - An IBM-backed quantum SDK for building, simulating, and running circuits on real quantum hardware.
- [qutip](https://github.com/qutip/qutip) [![GitHub stars](https://img.shields.io/github/stars/qutip/qutip?style=flat)](https://github.com/qutip/qutip/stargazers) - Quantum Toolbox in Python.
- [pennylane](https://github.com/PennyLaneAI/pennylane) [![GitHub stars](https://img.shields.io/github/stars/PennyLaneAI/pennylane?style=flat)](https://github.com/PennyLaneAI/pennylane/stargazers) - A hybrid quantum-classical machine learning library with automatic differentiation support.
- [cirq](https://github.com/quantumlib/Cirq) [![GitHub stars](https://img.shields.io/github/stars/quantumlib/Cirq?style=flat)](https://github.com/quantumlib/Cirq/stargazers) - A Google-developed framework focused on hardware-aware quantum circuit design for NISQ devices.

**Developer Tools**

### Algorithms and Design Patterns

_Python implementation of data structures, algorithms and design patterns. Also see [awesome-algorithms](https://github.com/tayllan/awesome-algorithms) [![GitHub stars](https://img.shields.io/github/stars/tayllan/awesome-algorithms?style=flat)](https://github.com/tayllan/awesome-algorithms/stargazers)._

- Algorithms
  - [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) [![GitHub stars](https://img.shields.io/github/stars/grantjenks/python-sortedcontainers?style=flat)](https://github.com/grantjenks/python-sortedcontainers/stargazers) - Fast and pure-Python implementation of sorted collections.
  - [algorithms](https://github.com/keon/algorithms) [![GitHub stars](https://img.shields.io/github/stars/keon/algorithms?style=flat)](https://github.com/keon/algorithms/stargazers) - Minimal examples of data structures and algorithms.
  - [thealgorithms](https://github.com/TheAlgorithms/Python) [![GitHub stars](https://img.shields.io/github/stars/TheAlgorithms/Python?style=flat)](https://github.com/TheAlgorithms/Python/stargazers) - All Algorithms implemented in Python.
- Design Patterns
  - [transitions](https://github.com/pytransitions/transitions) [![GitHub stars](https://img.shields.io/github/stars/pytransitions/transitions?style=flat)](https://github.com/pytransitions/transitions/stargazers) - A lightweight, object-oriented finite state machine implementation.
  - [python-patterns](https://github.com/faif/python-patterns) [![GitHub stars](https://img.shields.io/github/stars/faif/python-patterns?style=flat)](https://github.com/faif/python-patterns/stargazers) - A collection of design patterns in Python.
  - [python-statemachine](https://github.com/fgmacedo/python-statemachine) [![GitHub stars](https://img.shields.io/github/stars/fgmacedo/python-statemachine?style=flat)](https://github.com/fgmacedo/python-statemachine/stargazers) - Expressive statecharts and finite state machines with a declarative API, in sync and async codebases.

### Interactive Interpreter

_Interactive Python interpreters (REPL)._

- [ipython](https://github.com/ipython/ipython) [![GitHub stars](https://img.shields.io/github/stars/ipython/ipython?style=flat)](https://github.com/ipython/ipython/stargazers) - A powerful interactive Python shell, and the kernel behind Jupyter notebooks.
- [jupyter](https://github.com/jupyter/notebook) [![GitHub stars](https://img.shields.io/github/stars/jupyter/notebook?style=flat)](https://github.com/jupyter/notebook/stargazers) - A rich toolkit to help you make the most out of using Python interactively.
  - [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter) [![GitHub stars](https://img.shields.io/github/stars/markusschanta/awesome-jupyter?style=flat)](https://github.com/markusschanta/awesome-jupyter/stargazers)
- [marimo](https://github.com/marimo-team/marimo) [![GitHub stars](https://img.shields.io/github/stars/marimo-team/marimo?style=flat)](https://github.com/marimo-team/marimo/stargazers) - Transform data and train models, feels like a next-gen notebook, stored as Git-friendly Python.
- [ptpython](https://github.com/prompt-toolkit/ptpython) [![GitHub stars](https://img.shields.io/github/stars/prompt-toolkit/ptpython?style=flat)](https://github.com/prompt-toolkit/ptpython/stargazers) - Advanced Python REPL built on top of the [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) [![GitHub stars](https://img.shields.io/github/stars/prompt-toolkit/python-prompt-toolkit?style=flat)](https://github.com/prompt-toolkit/python-prompt-toolkit/stargazers).

### Code Analysis

_Tools of static analysis, linters and code quality checkers. Also see [awesome-static-analysis](https://github.com/analysis-tools-dev/static-analysis) [![GitHub stars](https://img.shields.io/github/stars/analysis-tools-dev/static-analysis?style=flat)](https://github.com/analysis-tools-dev/static-analysis/stargazers)._

- Code Analysis
  - [vulture](https://github.com/jendrikseipp/vulture) [![GitHub stars](https://img.shields.io/github/stars/jendrikseipp/vulture?style=flat)](https://github.com/jendrikseipp/vulture/stargazers) - A tool for finding and analyzing dead Python code.
  - [prospector](https://github.com/prospector-dev/prospector) [![GitHub stars](https://img.shields.io/github/stars/prospector-dev/prospector?style=flat)](https://github.com/prospector-dev/prospector/stargazers) - A tool to analyze Python code.
  - [repowise](https://github.com/repowise-dev/repowise) [![GitHub stars](https://img.shields.io/github/stars/repowise-dev/repowise?style=flat)](https://github.com/repowise-dev/repowise/stargazers) - Codebase intelligence that indexes repos into dependency graphs, git history, and auto-generated docs with dead code detection.
  - [complexipy](https://github.com/rohaquinlop/complexipy) [![GitHub stars](https://img.shields.io/github/stars/rohaquinlop/complexipy?style=flat)](https://github.com/rohaquinlop/complexipy/stargazers) - Cognitive complexity analysis for Python code, written in Rust.
- Git Hooks
  - [pre-commit](https://github.com/pre-commit/pre-commit) [![GitHub stars](https://img.shields.io/github/stars/pre-commit/pre-commit?style=flat)](https://github.com/pre-commit/pre-commit/stargazers) - A framework for managing and maintaining multi-language pre-commit hooks.
- Linters and Formatters
  - [ruff](https://github.com/astral-sh/ruff) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/ruff?style=flat)](https://github.com/astral-sh/ruff/stargazers) - An extremely fast Python linter and code formatter.
  - [black](https://github.com/psf/black) [![GitHub stars](https://img.shields.io/github/stars/psf/black?style=flat)](https://github.com/psf/black/stargazers) - The uncompromising Python code formatter.
  - [isort](https://github.com/PyCQA/isort) [![GitHub stars](https://img.shields.io/github/stars/PyCQA/isort?style=flat)](https://github.com/PyCQA/isort/stargazers) - A Python utility / library to sort imports.
  - [pylint](https://github.com/pylint-dev/pylint) [![GitHub stars](https://img.shields.io/github/stars/pylint-dev/pylint?style=flat)](https://github.com/pylint-dev/pylint/stargazers) - A fully customizable source code analyzer.
  - [flake8](https://github.com/PyCQA/flake8) [![GitHub stars](https://img.shields.io/github/stars/PyCQA/flake8?style=flat)](https://github.com/PyCQA/flake8/stargazers) - A wrapper around `pycodestyle`, `pyflakes` and McCabe.
    - [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions) [![GitHub stars](https://img.shields.io/github/stars/DmytroLitvinov/awesome-flake8-extensions?style=flat)](https://github.com/DmytroLitvinov/awesome-flake8-extensions/stargazers)
  - [bandit](https://github.com/PyCQA/bandit) [![GitHub stars](https://img.shields.io/github/stars/PyCQA/bandit?style=flat)](https://github.com/PyCQA/bandit/stargazers) - A tool designed to find common security issues in Python code.
- Refactoring
  - [rope](https://github.com/python-rope/rope) [![GitHub stars](https://img.shields.io/github/stars/python-rope/rope?style=flat)](https://github.com/python-rope/rope/stargazers) - Rope is a python refactoring library.
- Type Checkers - [awesome-python-typing](https://github.com/typeddjango/awesome-python-typing) [![GitHub stars](https://img.shields.io/github/stars/typeddjango/awesome-python-typing?style=flat)](https://github.com/typeddjango/awesome-python-typing/stargazers)
  - [mypy](https://github.com/python/mypy) [![GitHub stars](https://img.shields.io/github/stars/python/mypy?style=flat)](https://github.com/python/mypy/stargazers) - Check variable types during compile time.
  - [ty](https://github.com/astral-sh/ty) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/ty?style=flat)](https://github.com/astral-sh/ty/stargazers) - An extremely fast Python type checker and language server.
  - [pyright](https://github.com/microsoft/pyright) [![GitHub stars](https://img.shields.io/github/stars/microsoft/pyright?style=flat)](https://github.com/microsoft/pyright/stargazers) - Full-featured static type checker for Python from Microsoft, the engine behind Pylance.
  - [pyrefly](https://github.com/facebook/pyrefly) [![GitHub stars](https://img.shields.io/github/stars/facebook/pyrefly?style=flat)](https://github.com/facebook/pyrefly/stargazers) - A fast type checker and language server for Python.
- Type Annotations Generators
  - [monkeytype](https://github.com/Instagram/MonkeyType) [![GitHub stars](https://img.shields.io/github/stars/Instagram/MonkeyType?style=flat)](https://github.com/Instagram/MonkeyType/stargazers) - A system for Python that generates static type annotations by collecting runtime types.

### Testing

_Libraries for testing codebases and generating test data. Also see [awesome-python-testing](https://github.com/cleder/awesome-python-testing) [![GitHub stars](https://img.shields.io/github/stars/cleder/awesome-python-testing?style=flat)](https://github.com/cleder/awesome-python-testing/stargazers)._

- Frameworks
  - [pytest](https://github.com/pytest-dev/pytest) [![GitHub stars](https://img.shields.io/github/stars/pytest-dev/pytest?style=flat)](https://github.com/pytest-dev/pytest/stargazers) - A mature full-featured Python testing tool.
    - [awesome-pytest](https://github.com/augustogoulart/awesome-pytest) [![GitHub stars](https://img.shields.io/github/stars/augustogoulart/awesome-pytest?style=flat)](https://github.com/augustogoulart/awesome-pytest/stargazers)
  - [hypothesis](https://github.com/HypothesisWorks/hypothesis) [![GitHub stars](https://img.shields.io/github/stars/HypothesisWorks/hypothesis?style=flat)](https://github.com/HypothesisWorks/hypothesis/stargazers) - Hypothesis is an advanced Quickcheck style property based testing library.
  - [robotframework](https://github.com/robotframework/robotframework) [![GitHub stars](https://img.shields.io/github/stars/robotframework/robotframework?style=flat)](https://github.com/robotframework/robotframework/stargazers) - A generic test automation framework.
- Test Runners
  - [tox](https://github.com/tox-dev/tox) [![GitHub stars](https://img.shields.io/github/stars/tox-dev/tox?style=flat)](https://github.com/tox-dev/tox/stargazers) - Auto builds and tests distributions in multiple Python versions
  - [nox](https://github.com/wntrblm/nox) [![GitHub stars](https://img.shields.io/github/stars/wntrblm/nox?style=flat)](https://github.com/wntrblm/nox/stargazers) - Flexible test automation for Python.
- Browser Automation
  - [playwright-python](https://github.com/microsoft/playwright-python) [![GitHub stars](https://img.shields.io/github/stars/microsoft/playwright-python?style=flat)](https://github.com/microsoft/playwright-python/stargazers) - Python version of the Playwright testing and automation library.
  - [selenium](https://github.com/SeleniumHQ/selenium) [![GitHub stars](https://img.shields.io/github/stars/SeleniumHQ/selenium?style=flat)](https://github.com/SeleniumHQ/selenium/stargazers) - Python bindings for [Selenium](https://selenium.dev/) [WebDriver](https://selenium.dev/documentation/webdriver/).
  - [seleniumbase](https://github.com/seleniumbase/SeleniumBase) [![GitHub stars](https://img.shields.io/github/stars/seleniumbase/SeleniumBase?style=flat)](https://github.com/seleniumbase/SeleniumBase/stargazers) - Python framework for web automation & testing, with stealth options.
- Load Testing
  - [locust](https://github.com/locustio/locust) [![GitHub stars](https://img.shields.io/github/stars/locustio/locust?style=flat)](https://github.com/locustio/locust/stargazers) - Scalable user load testing tool written in Python.
- API Testing
  - [schemathesis](https://github.com/schemathesis/schemathesis) [![GitHub stars](https://img.shields.io/github/stars/schemathesis/schemathesis?style=flat)](https://github.com/schemathesis/schemathesis/stargazers) - A tool for automatic property-based testing of web applications built with Open API / Swagger specifications.
- Mock
  - [mock](https://docs.python.org/3/library/unittest.mock.html) - (Python standard library) A mocking and patching library.
  - [responses](https://github.com/getsentry/responses) [![GitHub stars](https://img.shields.io/github/stars/getsentry/responses?style=flat)](https://github.com/getsentry/responses/stargazers) - A utility library for mocking out the requests Python library.
  - [freezegun](https://github.com/spulec/freezegun) [![GitHub stars](https://img.shields.io/github/stars/spulec/freezegun?style=flat)](https://github.com/spulec/freezegun/stargazers) - Travel through time by mocking the datetime module.
  - [vcrpy](https://github.com/kevin1024/vcrpy) [![GitHub stars](https://img.shields.io/github/stars/kevin1024/vcrpy?style=flat)](https://github.com/kevin1024/vcrpy/stargazers) - Record and replay HTTP interactions on your tests.
  - [respx](https://github.com/lundberg/respx) [![GitHub stars](https://img.shields.io/github/stars/lundberg/respx?style=flat)](https://github.com/lundberg/respx/stargazers) - Mock HTTPX with awesome request patterns and response side effects.
- Object Factories
  - [factory_boy](https://github.com/FactoryBoy/factory_boy) [![GitHub stars](https://img.shields.io/github/stars/FactoryBoy/factory_boy?style=flat)](https://github.com/FactoryBoy/factory_boy/stargazers) - A test fixtures replacement for Python.
  - [polyfactory](https://github.com/litestar-org/polyfactory) [![GitHub stars](https://img.shields.io/github/stars/litestar-org/polyfactory?style=flat)](https://github.com/litestar-org/polyfactory/stargazers) - mock data generation library with support to classes (continuation of `pydantic-factories`)
- Code Coverage
  - [coverage](https://github.com/coveragepy/coveragepy) [![GitHub stars](https://img.shields.io/github/stars/coveragepy/coveragepy?style=flat)](https://github.com/coveragepy/coveragepy/stargazers) - Code coverage measurement.
- Fake Data
  - [faker](https://github.com/joke2k/faker) [![GitHub stars](https://img.shields.io/github/stars/joke2k/faker?style=flat)](https://github.com/joke2k/faker/stargazers) - A Python package that generates fake data.
  - [mimesis](https://github.com/lk-geimfari/mimesis) [![GitHub stars](https://img.shields.io/github/stars/lk-geimfari/mimesis?style=flat)](https://github.com/lk-geimfari/mimesis/stargazers) - is a Python library that help you generate fake data.

### Debugging Tools

_Libraries for debugging code._

- pdb-like Debugger
  - [ipdb](https://github.com/gotcha/ipdb) [![GitHub stars](https://img.shields.io/github/stars/gotcha/ipdb?style=flat)](https://github.com/gotcha/ipdb/stargazers) - IPython-enabled [pdb](https://docs.python.org/3/library/pdb.html).
  - [pudb](https://github.com/inducer/pudb) [![GitHub stars](https://img.shields.io/github/stars/inducer/pudb?style=flat)](https://github.com/inducer/pudb/stargazers) - A full-screen, console-based Python debugger.
- Tracing
  - [hunter](https://github.com/ionelmc/python-hunter) [![GitHub stars](https://img.shields.io/github/stars/ionelmc/python-hunter?style=flat)](https://github.com/ionelmc/python-hunter/stargazers) - A flexible code tracing toolkit.
- Profiler
  - [py-spy](https://github.com/benfred/py-spy) [![GitHub stars](https://img.shields.io/github/stars/benfred/py-spy?style=flat)](https://github.com/benfred/py-spy/stargazers) - A sampling profiler for Python programs. Written in Rust.
  - [memray](https://github.com/bloomberg/memray) [![GitHub stars](https://img.shields.io/github/stars/bloomberg/memray?style=flat)](https://github.com/bloomberg/memray/stargazers) - A memory profiler that tracks allocations in Python code, native extensions, and the interpreter itself.
  - [pyinstrument](https://github.com/joerick/pyinstrument) [![GitHub stars](https://img.shields.io/github/stars/joerick/pyinstrument?style=flat)](https://github.com/joerick/pyinstrument/stargazers) - A statistical wall-clock profiler with low overhead and readable call-tree output.
  - [scalene](https://github.com/plasma-umass/scalene) [![GitHub stars](https://img.shields.io/github/stars/plasma-umass/scalene?style=flat)](https://github.com/plasma-umass/scalene/stargazers) - A high-performance, high-precision CPU, GPU, and memory profiler for Python.
- Others
  - [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar) [![GitHub stars](https://img.shields.io/github/stars/django-commons/django-debug-toolbar?style=flat)](https://github.com/django-commons/django-debug-toolbar/stargazers) - Display various debug information for Django.
  - [icecream](https://github.com/gruns/icecream) [![GitHub stars](https://img.shields.io/github/stars/gruns/icecream?style=flat)](https://github.com/gruns/icecream/stargazers) - Inspect variables, expressions, and program execution with a single, simple function call.
  - [flask-debugtoolbar](https://github.com/pallets-eco/flask-debugtoolbar) [![GitHub stars](https://img.shields.io/github/stars/pallets-eco/flask-debugtoolbar?style=flat)](https://github.com/pallets-eco/flask-debugtoolbar/stargazers) - A port of the django-debug-toolbar to flask.

### Build Tools

_Compile software from source code. If you're looking for Python packaging/build tools, see [Package Management](#package-management)._

- [invoke](https://github.com/pyinvoke/invoke) [![GitHub stars](https://img.shields.io/github/stars/pyinvoke/invoke?style=flat)](https://github.com/pyinvoke/invoke/stargazers) - A tool for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks.
- [scons](https://github.com/SCons/scons) [![GitHub stars](https://img.shields.io/github/stars/SCons/scons?style=flat)](https://github.com/SCons/scons/stargazers) - A software construction tool.
- [doit](https://github.com/pydoit/doit) [![GitHub stars](https://img.shields.io/github/stars/pydoit/doit?style=flat)](https://github.com/pydoit/doit/stargazers) - A task runner and build tool.

### Documentation

_Libraries for generating project documentation._

- [sphinx](https://github.com/sphinx-doc/sphinx/) [![GitHub stars](https://img.shields.io/github/stars/sphinx-doc/sphinx/?style=flat)](https://github.com/sphinx-doc/sphinx//stargazers) - Python Documentation generator.
  - [awesome-sphinxdoc](https://github.com/ygzgxyz/awesome-sphinxdoc) [![GitHub stars](https://img.shields.io/github/stars/ygzgxyz/awesome-sphinxdoc?style=flat)](https://github.com/ygzgxyz/awesome-sphinxdoc/stargazers)
- [mkdocs-material](https://github.com/squidfunk/mkdocs-material) [![GitHub stars](https://img.shields.io/github/stars/squidfunk/mkdocs-material?style=flat)](https://github.com/squidfunk/mkdocs-material/stargazers) - A documentation framework and Material Design theme built on MkDocs.
- [diagrams](https://github.com/mingrammer/diagrams) [![GitHub stars](https://img.shields.io/github/stars/mingrammer/diagrams?style=flat)](https://github.com/mingrammer/diagrams/stargazers) - Diagram as Code.
- [pdoc](https://github.com/mitmproxy/pdoc) [![GitHub stars](https://img.shields.io/github/stars/mitmproxy/pdoc?style=flat)](https://github.com/mitmproxy/pdoc/stargazers) - Epydoc replacement to auto generate API documentation for Python libraries.
- [zensical](https://github.com/zensical/zensical) [![GitHub stars](https://img.shields.io/github/stars/zensical/zensical?style=flat)](https://github.com/zensical/zensical/stargazers) - A modern static site generator for technical documentation.

**DevOps**

### DevOps Tools

_Software and libraries for DevOps._

- Cloud Providers
  - [boto3](https://github.com/boto/boto3) [![GitHub stars](https://img.shields.io/github/stars/boto/boto3?style=flat)](https://github.com/boto/boto3/stargazers) - Python interface to Amazon Web Services.
  - [awscli](https://github.com/aws/aws-cli) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-cli?style=flat)](https://github.com/aws/aws-cli/stargazers) - Universal Command Line Interface for Amazon Web Services.
  - [azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) [![GitHub stars](https://img.shields.io/github/stars/Azure/azure-sdk-for-python?style=flat)](https://github.com/Azure/azure-sdk-for-python/stargazers) - Microsoft Azure SDK for Python, published as per-service packages.
  - [google-cloud-python](https://github.com/googleapis/google-cloud-python) [![GitHub stars](https://img.shields.io/github/stars/googleapis/google-cloud-python?style=flat)](https://github.com/googleapis/google-cloud-python/stargazers) - Google Cloud client libraries for Python, published as per-service packages.
- Configuration Management
  - [ansible](https://github.com/ansible/ansible) [![GitHub stars](https://img.shields.io/github/stars/ansible/ansible?style=flat)](https://github.com/ansible/ansible/stargazers) - A radically simple IT automation platform.
  - [cloud-init](https://github.com/canonical/cloud-init) [![GitHub stars](https://img.shields.io/github/stars/canonical/cloud-init?style=flat)](https://github.com/canonical/cloud-init/stargazers) - A multi-distribution package that handles early initialization of a cloud instance.
  - [pyinfra](https://github.com/pyinfra-dev/pyinfra) [![GitHub stars](https://img.shields.io/github/stars/pyinfra-dev/pyinfra?style=flat)](https://github.com/pyinfra-dev/pyinfra/stargazers) - A versatile CLI tools and python libraries to automate infrastructure.
  - [salt](https://github.com/saltstack/salt) [![GitHub stars](https://img.shields.io/github/stars/saltstack/salt?style=flat)](https://github.com/saltstack/salt/stargazers) - Infrastructure automation and management system.
- Deployment
  - [fabric](https://github.com/fabric/fabric) [![GitHub stars](https://img.shields.io/github/stars/fabric/fabric?style=flat)](https://github.com/fabric/fabric/stargazers) - A simple, Pythonic tool for remote execution and deployment.
  - [chalice](https://github.com/aws/chalice) [![GitHub stars](https://img.shields.io/github/stars/aws/chalice?style=flat)](https://github.com/aws/chalice/stargazers) - A Python serverless microframework for AWS.
- Monitoring and Processes
  - [psutil](https://github.com/giampaolo/psutil) [![GitHub stars](https://img.shields.io/github/stars/giampaolo/psutil?style=flat)](https://github.com/giampaolo/psutil/stargazers) - A cross-platform process and system utilities module.
  - [sentry-sdk](https://github.com/getsentry/sentry-python) [![GitHub stars](https://img.shields.io/github/stars/getsentry/sentry-python?style=flat)](https://github.com/getsentry/sentry-python/stargazers) - Sentry SDK for Python.
  - [supervisor](https://github.com/Supervisor/supervisor) [![GitHub stars](https://img.shields.io/github/stars/Supervisor/supervisor?style=flat)](https://github.com/Supervisor/supervisor/stargazers) - Supervisor process control system for UNIX.
  - [flower](https://github.com/mher/flower) [![GitHub stars](https://img.shields.io/github/stars/mher/flower?style=flat)](https://github.com/mher/flower/stargazers) - A real-time monitor and web admin for Celery task queues.
  - [sh](https://github.com/amoffat/sh) [![GitHub stars](https://img.shields.io/github/stars/amoffat/sh?style=flat)](https://github.com/amoffat/sh/stargazers) - A full-fledged subprocess replacement for Python.
- Other
  - [borgbackup](https://github.com/borgbackup/borg) [![GitHub stars](https://img.shields.io/github/stars/borgbackup/borg?style=flat)](https://github.com/borgbackup/borg/stargazers) - A deduplicating archiver with compression and encryption.
  - [chaostoolkit](https://github.com/chaostoolkit/chaostoolkit) [![GitHub stars](https://img.shields.io/github/stars/chaostoolkit/chaostoolkit?style=flat)](https://github.com/chaostoolkit/chaostoolkit/stargazers) - A Chaos Engineering toolkit & Orchestration for Developers.

### Distributed Computing

_Frameworks and libraries for Distributed Computing._

- [ray](https://github.com/ray-project/ray/) [![GitHub stars](https://img.shields.io/github/stars/ray-project/ray/?style=flat)](https://github.com/ray-project/ray//stargazers) - A system for parallel and distributed Python that unifies the machine learning ecosystem.
- [pyspark](https://github.com/apache/spark) [![GitHub stars](https://img.shields.io/github/stars/apache/spark?style=flat)](https://github.com/apache/spark/stargazers) - [Apache Spark](https://spark.apache.org/) Python API.
- [dask](https://github.com/dask/dask) [![GitHub stars](https://img.shields.io/github/stars/dask/dask?style=flat)](https://github.com/dask/dask/stargazers) - A flexible parallel computing library for analytic computing.
- [joblib](https://github.com/joblib/joblib) [![GitHub stars](https://img.shields.io/github/stars/joblib/joblib?style=flat)](https://github.com/joblib/joblib/stargazers) - A set of tools to provide lightweight pipelining in Python.
- [mpi4py](https://github.com/mpi4py/mpi4py) [![GitHub stars](https://img.shields.io/github/stars/mpi4py/mpi4py?style=flat)](https://github.com/mpi4py/mpi4py/stargazers) - Python bindings for MPI.

### Task Queues

_Libraries for working with task queues._

- [celery](https://github.com/celery/celery) [![GitHub stars](https://img.shields.io/github/stars/celery/celery?style=flat)](https://github.com/celery/celery/stargazers) - An asynchronous task queue/job queue based on distributed message passing.
- [rq](https://github.com/rq/rq) [![GitHub stars](https://img.shields.io/github/stars/rq/rq?style=flat)](https://github.com/rq/rq/stargazers) - Simple job queues for Python.
- [dramatiq](https://github.com/Bogdanp/dramatiq) [![GitHub stars](https://img.shields.io/github/stars/Bogdanp/dramatiq?style=flat)](https://github.com/Bogdanp/dramatiq/stargazers) - A fast and reliable background task processing library for Python 3.
- [huey](https://github.com/coleifer/huey) [![GitHub stars](https://img.shields.io/github/stars/coleifer/huey?style=flat)](https://github.com/coleifer/huey/stargazers) - Little multi-threaded task queue.
- [taskiq](https://github.com/taskiq-python/taskiq) [![GitHub stars](https://img.shields.io/github/stars/taskiq-python/taskiq?style=flat)](https://github.com/taskiq-python/taskiq/stargazers) - Distributed task queue with native asyncio support and pluggable brokers.

### Messaging

_Libraries for working with message brokers and event streaming._

- [confluent-kafka](https://github.com/confluentinc/confluent-kafka-python) [![GitHub stars](https://img.shields.io/github/stars/confluentinc/confluent-kafka-python?style=flat)](https://github.com/confluentinc/confluent-kafka-python/stargazers) - Confluent's Python client for Apache Kafka, built on librdkafka.
- [pika](https://github.com/pika/pika) [![GitHub stars](https://img.shields.io/github/stars/pika/pika?style=flat)](https://github.com/pika/pika/stargazers) - Pure-Python RabbitMQ/AMQP 0-9-1 client library.
- [paho-mqtt](https://github.com/eclipse-paho/paho.mqtt.python) [![GitHub stars](https://img.shields.io/github/stars/eclipse-paho/paho.mqtt.python?style=flat)](https://github.com/eclipse-paho/paho.mqtt.python/stargazers) - The Eclipse Paho MQTT client for Python.
- [faststream](https://github.com/ag2ai/faststream) [![GitHub stars](https://img.shields.io/github/stars/ag2ai/faststream?style=flat)](https://github.com/ag2ai/faststream/stargazers) - A framework for building asynchronous services over Apache Kafka, RabbitMQ, NATS, MQTT and Redis.

### Job Schedulers

_Libraries for scheduling jobs._

- Task Scheduling
  - [apscheduler](https://github.com/agronholm/apscheduler) [![GitHub stars](https://img.shields.io/github/stars/agronholm/apscheduler?style=flat)](https://github.com/agronholm/apscheduler/stargazers) - A light but powerful in-process task scheduler that lets you schedule functions.
  - [schedule](https://github.com/dbader/schedule) [![GitHub stars](https://img.shields.io/github/stars/dbader/schedule?style=flat)](https://github.com/dbader/schedule/stargazers) - Python job scheduling for humans.
- Workflow Orchestration
  - [apache-airflow](https://github.com/apache/airflow) [![GitHub stars](https://img.shields.io/github/stars/apache/airflow?style=flat)](https://github.com/apache/airflow/stargazers) - Airflow is a platform to programmatically author, schedule and monitor workflows.
  - [prefect](https://github.com/PrefectHQ/prefect) [![GitHub stars](https://img.shields.io/github/stars/PrefectHQ/prefect?style=flat)](https://github.com/PrefectHQ/prefect/stargazers) - A modern workflow orchestration framework that makes it easy to build, schedule and monitor robust data pipelines.
  - [dagster](https://github.com/dagster-io/dagster) [![GitHub stars](https://img.shields.io/github/stars/dagster-io/dagster?style=flat)](https://github.com/dagster-io/dagster/stargazers) - An orchestration platform for the development, production, and observation of data assets.

### Logging

_Libraries for generating and working with logs._

- [logging](https://docs.python.org/3/library/logging.html) - (Python standard library) Logging facility for Python.
- [structlog](https://github.com/hynek/structlog) [![GitHub stars](https://img.shields.io/github/stars/hynek/structlog?style=flat)](https://github.com/hynek/structlog/stargazers) - Structured logging made easy.
- [loguru](https://github.com/Delgan/loguru) [![GitHub stars](https://img.shields.io/github/stars/Delgan/loguru?style=flat)](https://github.com/Delgan/loguru/stargazers) - Library which aims to bring enjoyable logging in Python.

### Network Virtualization

_Tools and libraries for Virtual Networking and SDN (Software Defined Networking)._

- [scapy](https://github.com/secdev/scapy) [![GitHub stars](https://img.shields.io/github/stars/secdev/scapy?style=flat)](https://github.com/secdev/scapy/stargazers) - A brilliant packet manipulation library.
- [napalm](https://github.com/napalm-automation/napalm) [![GitHub stars](https://img.shields.io/github/stars/napalm-automation/napalm?style=flat)](https://github.com/napalm-automation/napalm/stargazers) - Cross-vendor API to manipulate network devices.

**CLI & GUI**

### CLI Development

_Libraries for building command-line applications._

- CLI Development
  - [argparse](https://docs.python.org/3/library/argparse.html) - (Python standard library) Command-line option and argument parsing.
  - [click](https://github.com/pallets/click/) [![GitHub stars](https://img.shields.io/github/stars/pallets/click/?style=flat)](https://github.com/pallets/click//stargazers) - A package for creating beautiful command line interfaces in a composable way.
  - [typer](https://github.com/fastapi/typer) [![GitHub stars](https://img.shields.io/github/stars/fastapi/typer?style=flat)](https://github.com/fastapi/typer/stargazers) - Modern CLI framework that uses Python type hints. Built on Click and Pydantic.
  - [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) [![GitHub stars](https://img.shields.io/github/stars/prompt-toolkit/python-prompt-toolkit?style=flat)](https://github.com/prompt-toolkit/python-prompt-toolkit/stargazers) - A library for building powerful interactive command lines.
  - [fire](https://github.com/google/python-fire) [![GitHub stars](https://img.shields.io/github/stars/google/python-fire?style=flat)](https://github.com/google/python-fire/stargazers) - A library for creating command line interfaces from absolutely any Python object.
- Terminal Rendering
  - [tqdm](https://github.com/tqdm/tqdm) [![GitHub stars](https://img.shields.io/github/stars/tqdm/tqdm?style=flat)](https://github.com/tqdm/tqdm/stargazers) - Fast, extensible progress bar for loops and CLI.
  - [rich](https://github.com/Textualize/rich) [![GitHub stars](https://img.shields.io/github/stars/Textualize/rich?style=flat)](https://github.com/Textualize/rich/stargazers) - Python library for rich text and beautiful formatting in the terminal. Also provides a great `RichHandler` log handler.
  - [colorama](https://github.com/tartley/colorama) [![GitHub stars](https://img.shields.io/github/stars/tartley/colorama?style=flat)](https://github.com/tartley/colorama/stargazers) - Cross-platform colored terminal text.
  - [alive-progress](https://github.com/rsalmei/alive-progress) [![GitHub stars](https://img.shields.io/github/stars/rsalmei/alive-progress?style=flat)](https://github.com/rsalmei/alive-progress/stargazers) - A new kind of Progress Bar, with real-time throughput, eta and very cool animations.
- TUI Frameworks
  - [textual](https://github.com/Textualize/textual) [![GitHub stars](https://img.shields.io/github/stars/Textualize/textual?style=flat)](https://github.com/Textualize/textual/stargazers) - A framework for building interactive user interfaces that run in the terminal and the browser.
  - [urwid](https://github.com/urwid/urwid) [![GitHub stars](https://img.shields.io/github/stars/urwid/urwid?style=flat)](https://github.com/urwid/urwid/stargazers) - A library for creating terminal GUI applications with strong support for widgets, events, rich colors, etc.
  - [asciimatics](https://github.com/peterbrittain/asciimatics) [![GitHub stars](https://img.shields.io/github/stars/peterbrittain/asciimatics?style=flat)](https://github.com/peterbrittain/asciimatics/stargazers) - A package to create full-screen text UIs (from interactive forms to ASCII animations).

### CLI Tools

_Useful CLI-based tools._

- Database CLIs
  - [pgcli](https://github.com/dbcli/pgcli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/pgcli?style=flat)](https://github.com/dbcli/pgcli/stargazers) - PostgreSQL CLI with autocompletion and syntax highlighting.
  - [mycli](https://github.com/dbcli/mycli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/mycli?style=flat)](https://github.com/dbcli/mycli/stargazers) - MySQL CLI with autocompletion and syntax highlighting.
  - [litecli](https://github.com/dbcli/litecli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/litecli?style=flat)](https://github.com/dbcli/litecli/stargazers) - SQLite CLI with autocompletion and syntax highlighting.
  - [iredis](https://github.com/laixintao/iredis) [![GitHub stars](https://img.shields.io/github/stars/laixintao/iredis?style=flat)](https://github.com/laixintao/iredis/stargazers) - Redis CLI with autocompletion and syntax highlighting.
- Downloaders
  - [yt-dlp](https://github.com/yt-dlp/yt-dlp) [![GitHub stars](https://img.shields.io/github/stars/yt-dlp/yt-dlp?style=flat)](https://github.com/yt-dlp/yt-dlp/stargazers) - A command-line program to download videos from YouTube and other video sites, a fork of youtube-dl.
- HTTP Clients
  - [httpie](https://github.com/httpie/cli) [![GitHub stars](https://img.shields.io/github/stars/httpie/cli?style=flat)](https://github.com/httpie/cli/stargazers) - A command line HTTP client, a user-friendly cURL replacement.
- Project Scaffolding
  - [cookiecutter](https://github.com/cookiecutter/cookiecutter) [![GitHub stars](https://img.shields.io/github/stars/cookiecutter/cookiecutter?style=flat)](https://github.com/cookiecutter/cookiecutter/stargazers) - A command-line utility that creates projects from cookiecutters (project templates).
  - [copier](https://github.com/copier-org/copier) [![GitHub stars](https://img.shields.io/github/stars/copier-org/copier?style=flat)](https://github.com/copier-org/copier/stargazers) - A library and command-line utility for rendering projects templates.
- Shells
  - [xonsh](https://github.com/xonsh/xonsh/) [![GitHub stars](https://img.shields.io/github/stars/xonsh/xonsh/?style=flat)](https://github.com/xonsh/xonsh//stargazers) - A Python-powered shell. Full-featured and cross-platform.
- Terminal Workflow
  - [tmuxp](https://github.com/tmux-python/tmuxp) [![GitHub stars](https://img.shields.io/github/stars/tmux-python/tmuxp?style=flat)](https://github.com/tmux-python/tmuxp/stargazers) - A [tmux](https://github.com/tmux/tmux) [![GitHub stars](https://img.shields.io/github/stars/tmux/tmux?style=flat)](https://github.com/tmux/tmux/stargazers) session manager.

### GUI Development

_Libraries for working with graphical user interface applications._

- Desktop
  - [pygobject](https://github.com/GNOME/pygobject) [![GitHub stars](https://img.shields.io/github/stars/GNOME/pygobject?style=flat)](https://github.com/GNOME/pygobject/stargazers) - Python Bindings for GLib/GObject/GIO/GTK+ (GTK+3).
  - [wxPython](https://github.com/wxWidgets/Phoenix) [![GitHub stars](https://img.shields.io/github/stars/wxWidgets/Phoenix?style=flat)](https://github.com/wxWidgets/Phoenix/stargazers) - A blending of the wxWidgets C++ class library with the Python.
  - [kivy](https://github.com/kivy/kivy) [![GitHub stars](https://img.shields.io/github/stars/kivy/kivy?style=flat)](https://github.com/kivy/kivy/stargazers) - A library for creating NUI applications, running on Windows, Linux, Mac OS X, Android and iOS.
  - [dearpygui](https://github.com/hoffstadt/DearPyGui) [![GitHub stars](https://img.shields.io/github/stars/hoffstadt/DearPyGui?style=flat)](https://github.com/hoffstadt/DearPyGui/stargazers) - A Simple GPU accelerated Python GUI framework
  - [toga](https://github.com/beeware/toga) [![GitHub stars](https://img.shields.io/github/stars/beeware/toga?style=flat)](https://github.com/beeware/toga/stargazers) - A Python native, OS native GUI toolkit.
- Qt
  - [PySide6](https://github.com/pyside/pyside-setup) [![GitHub stars](https://img.shields.io/github/stars/pyside/pyside-setup?style=flat)](https://github.com/pyside/pyside-setup/stargazers) - Qt for Python offers the official Python bindings for [Qt](https://www.qt.io/), same as PyQt6 but it's the official binding with different licensing.
  - [PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/) - Python bindings for the [Qt](https://www.qt.io/) cross-platform application and UI framework.
- Tkinter
  - [tkinter](https://docs.python.org/3/library/tkinter.html) - (Python standard library) The standard Python interface to the Tcl/Tk GUI toolkit.
  - [customtkinter](https://github.com/tomschimansky/customtkinter) [![GitHub stars](https://img.shields.io/github/stars/tomschimansky/customtkinter?style=flat)](https://github.com/tomschimansky/customtkinter/stargazers) - A modern and customizable python UI-library based on Tkinter.
  - [tkdesigner](https://github.com/ParthJadhav/Tkinter-Designer) [![GitHub stars](https://img.shields.io/github/stars/ParthJadhav/Tkinter-Designer?style=flat)](https://github.com/ParthJadhav/Tkinter-Designer/stargazers) - Generates Tkinter interfaces from Figma designs using the Figma API.
- Web-based
  - [pywebview](https://github.com/r0x0r/pywebview/) [![GitHub stars](https://img.shields.io/github/stars/r0x0r/pywebview/?style=flat)](https://github.com/r0x0r/pywebview//stargazers) - A lightweight cross-platform native wrapper around a webview component.
  - [nicegui](https://github.com/zauberzeug/nicegui) [![GitHub stars](https://img.shields.io/github/stars/zauberzeug/nicegui?style=flat)](https://github.com/zauberzeug/nicegui/stargazers) - An easy-to-use, Python-based UI framework, which shows up in your web browser.
  - [flet](https://github.com/flet-dev/flet) [![GitHub stars](https://img.shields.io/github/stars/flet-dev/flet?style=flat)](https://github.com/flet-dev/flet/stargazers) - Cross-platform GUI framework for building modern apps in pure Python.
- Wrappers
  - [gooey](https://github.com/chriskiehl/Gooey) [![GitHub stars](https://img.shields.io/github/stars/chriskiehl/Gooey?style=flat)](https://github.com/chriskiehl/Gooey/stargazers) - Turn command line programs into a full GUI application with one line.

**Text & Documents**

### Text Processing

_Libraries for parsing and manipulating plain texts._

- Encoding and Unicode
  - [charset-normalizer](https://github.com/jawah/charset_normalizer) [![GitHub stars](https://img.shields.io/github/stars/jawah/charset_normalizer?style=flat)](https://github.com/jawah/charset_normalizer/stargazers) - Universal character encoding detector, the default of the requests ecosystem.
  - [chardet](https://github.com/chardet/chardet) [![GitHub stars](https://img.shields.io/github/stars/chardet/chardet?style=flat)](https://github.com/chardet/chardet/stargazers) - Python character encoding detector.
  - [ftfy](https://github.com/rspeer/python-ftfy) [![GitHub stars](https://img.shields.io/github/stars/rspeer/python-ftfy?style=flat)](https://github.com/rspeer/python-ftfy/stargazers) - Makes Unicode text less broken and more consistent automagically.
- Fuzzy Matching
  - [rapidfuzz](https://github.com/rapidfuzz/RapidFuzz) [![GitHub stars](https://img.shields.io/github/stars/rapidfuzz/RapidFuzz?style=flat)](https://github.com/rapidfuzz/RapidFuzz/stargazers) - Rapid fuzzy string matching using various string metrics, with a C++ core.
- General
  - [difflib](https://docs.python.org/3/library/difflib.html) - (Python standard library) Helpers for computing deltas.
  - [pyfiglet](https://github.com/pwaller/pyfiglet) [![GitHub stars](https://img.shields.io/github/stars/pwaller/pyfiglet?style=flat)](https://github.com/pwaller/pyfiglet/stargazers) - An implementation of figlet written in Python.
- Internationalization
  - [babel](https://github.com/python-babel/babel) [![GitHub stars](https://img.shields.io/github/stars/python-babel/babel?style=flat)](https://github.com/python-babel/babel/stargazers) - An internationalization library for Python.
- Parser
  - [pygments](https://github.com/pygments/pygments) [![GitHub stars](https://img.shields.io/github/stars/pygments/pygments?style=flat)](https://github.com/pygments/pygments/stargazers) - A generic syntax highlighter.
  - [pyparsing](https://github.com/pyparsing/pyparsing) [![GitHub stars](https://img.shields.io/github/stars/pyparsing/pyparsing?style=flat)](https://github.com/pyparsing/pyparsing/stargazers) - A general purpose framework for generating parsers.
  - [sqlparse](https://github.com/andialbrecht/sqlparse) [![GitHub stars](https://img.shields.io/github/stars/andialbrecht/sqlparse?style=flat)](https://github.com/andialbrecht/sqlparse/stargazers) - A non-validating SQL parser.
  - [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) [![GitHub stars](https://img.shields.io/github/stars/daviddrysdale/python-phonenumbers?style=flat)](https://github.com/daviddrysdale/python-phonenumbers/stargazers) - Parsing, formatting, storing and validating international phone numbers.
  - [parsy](https://github.com/python-parsy/parsy) [![GitHub stars](https://img.shields.io/github/stars/python-parsy/parsy?style=flat)](https://github.com/python-parsy/parsy/stargazers) - Easy, generic parser combinator library for creating parsers.
- Transliteration and Slugs
  - [python-slugify](https://github.com/un33k/python-slugify) [![GitHub stars](https://img.shields.io/github/stars/un33k/python-slugify?style=flat)](https://github.com/un33k/python-slugify/stargazers) - A Python slugify library that translates unicode to ASCII.
  - [unidecode](https://github.com/avian2/unidecode) [![GitHub stars](https://img.shields.io/github/stars/avian2/unidecode?style=flat)](https://github.com/avian2/unidecode/stargazers) - ASCII transliterations of Unicode text.
- Unique identifiers
  - [shortuuid](https://github.com/skorokithakis/shortuuid) [![GitHub stars](https://img.shields.io/github/stars/skorokithakis/shortuuid?style=flat)](https://github.com/skorokithakis/shortuuid/stargazers) - A generator library for concise, unambiguous and URL-safe UUIDs.
  - [sqids](https://github.com/sqids/sqids-python) [![GitHub stars](https://img.shields.io/github/stars/sqids/sqids-python?style=flat)](https://github.com/sqids/sqids-python/stargazers) - A library for generating short unique IDs from numbers.

### HTML Manipulation

_Libraries for working with HTML and XML._

- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Providing Pythonic idioms for iterating, searching, and modifying HTML or XML.
- [lxml](https://github.com/lxml/lxml) [![GitHub stars](https://img.shields.io/github/stars/lxml/lxml?style=flat)](https://github.com/lxml/lxml/stargazers) - A very fast, easy-to-use and versatile library for handling HTML and XML.
- [xmltodict](https://github.com/martinblech/xmltodict) [![GitHub stars](https://img.shields.io/github/stars/martinblech/xmltodict?style=flat)](https://github.com/martinblech/xmltodict/stargazers) - Working with XML feel like you are working with JSON.
- [markupsafe](https://github.com/pallets/markupsafe) [![GitHub stars](https://img.shields.io/github/stars/pallets/markupsafe?style=flat)](https://github.com/pallets/markupsafe/stargazers) - Implements a XML/HTML/XHTML Markup safe string for Python.
- [justhtml](https://github.com/EmilStenstrom/justhtml/) [![GitHub stars](https://img.shields.io/github/stars/EmilStenstrom/justhtml/?style=flat)](https://github.com/EmilStenstrom/justhtml//stargazers) - A pure Python HTML5 parser that just works.

### File Format Processing

_Libraries for parsing and manipulating specific text formats._

- General
  - [pyelftools](https://github.com/eliben/pyelftools) [![GitHub stars](https://img.shields.io/github/stars/eliben/pyelftools?style=flat)](https://github.com/eliben/pyelftools/stargazers) - Parsing and analyzing ELF files and DWARF debugging information.
  - [tablib](https://github.com/jazzband/tablib) [![GitHub stars](https://img.shields.io/github/stars/jazzband/tablib?style=flat)](https://github.com/jazzband/tablib/stargazers) - A module for Tabular Datasets in XLS, CSV, JSON, YAML.
- File Conversion
  - [markitdown](https://github.com/microsoft/markitdown) [![GitHub stars](https://img.shields.io/github/stars/microsoft/markitdown?style=flat)](https://github.com/microsoft/markitdown/stargazers) - Python tool for converting files and office documents to Markdown.
  - [docling](https://github.com/docling-project/docling) [![GitHub stars](https://img.shields.io/github/stars/docling-project/docling?style=flat)](https://github.com/docling-project/docling/stargazers) - Library for converting documents into structured data.
- Excel
  - [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.
  - [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) [![GitHub stars](https://img.shields.io/github/stars/jmcnamara/XlsxWriter?style=flat)](https://github.com/jmcnamara/XlsxWriter/stargazers) - A Python module for creating Excel .xlsx files.
- Word
  - [python-docx](https://github.com/python-openxml/python-docx) [![GitHub stars](https://img.shields.io/github/stars/python-openxml/python-docx?style=flat)](https://github.com/python-openxml/python-docx/stargazers) - Reads, queries and modifies Microsoft Word 2007/2008 docx files.
- PowerPoint
  - [python-pptx](https://github.com/scanny/python-pptx) [![GitHub stars](https://img.shields.io/github/stars/scanny/python-pptx?style=flat)](https://github.com/scanny/python-pptx/stargazers) - Python library for creating and updating PowerPoint (.pptx) files.
- PDF
  - [pypdf](https://github.com/py-pdf/pypdf) [![GitHub stars](https://img.shields.io/github/stars/py-pdf/pypdf?style=flat)](https://github.com/py-pdf/pypdf/stargazers) - A library capable of splitting, merging, cropping, and transforming PDF pages.
  - [reportlab](https://www.reportlab.com/opensource/) - Allowing Rapid creation of rich PDF documents.
  - [pdfminer.six](https://github.com/pdfminer/pdfminer.six) [![GitHub stars](https://img.shields.io/github/stars/pdfminer/pdfminer.six?style=flat)](https://github.com/pdfminer/pdfminer.six/stargazers) - Pdfminer.six is a community maintained fork of the original PDFMiner.
- HTML-to-PDF
  - [weasyprint](https://github.com/Kozea/WeasyPrint) [![GitHub stars](https://img.shields.io/github/stars/Kozea/WeasyPrint?style=flat)](https://github.com/Kozea/WeasyPrint/stargazers) - A visual rendering engine for HTML and CSS that can export to PDF.
- Markdown
  - [markdown-it-py](https://github.com/executablebooks/markdown-it-py) [![GitHub stars](https://img.shields.io/github/stars/executablebooks/markdown-it-py?style=flat)](https://github.com/executablebooks/markdown-it-py/stargazers) - Markdown parser with 100% CommonMark support, extensions, and syntax plugins.
  - [markdown](https://github.com/Python-Markdown/markdown) [![GitHub stars](https://img.shields.io/github/stars/Python-Markdown/markdown?style=flat)](https://github.com/Python-Markdown/markdown/stargazers) - A Python implementation of John Gruber’s Markdown.
  - [mistune](https://github.com/lepture/mistune) [![GitHub stars](https://img.shields.io/github/stars/lepture/mistune?style=flat)](https://github.com/lepture/mistune/stargazers) - Fastest and full featured pure Python parsers of Markdown.
- Data Formats
  - [tomllib](https://docs.python.org/3/library/tomllib.html) - (Python standard library) Parse TOML files.
  - [pyyaml](https://github.com/yaml/pyyaml) [![GitHub stars](https://img.shields.io/github/stars/yaml/pyyaml?style=flat)](https://github.com/yaml/pyyaml/stargazers) - YAML implementations for Python.

### File Manipulation

_Libraries for file manipulation._

- [mimetypes](https://docs.python.org/3/library/mimetypes.html) - (Python standard library) Map filenames to MIME types.
- [pathlib](https://docs.python.org/3/library/pathlib.html) - (Python standard library) A cross-platform, object-oriented path library.
- [watchfiles](https://github.com/samuelcolvin/watchfiles) [![GitHub stars](https://img.shields.io/github/stars/samuelcolvin/watchfiles?style=flat)](https://github.com/samuelcolvin/watchfiles/stargazers) - Simple, modern and fast file watching and code reload in python.
- [watchdog](https://github.com/gorakhargosh/watchdog) [![GitHub stars](https://img.shields.io/github/stars/gorakhargosh/watchdog?style=flat)](https://github.com/gorakhargosh/watchdog/stargazers) - API and shell utilities to monitor file system events.
- [python-magic](https://github.com/ahupp/python-magic) [![GitHub stars](https://img.shields.io/github/stars/ahupp/python-magic?style=flat)](https://github.com/ahupp/python-magic/stargazers) - A Python interface to the libmagic file type identification library.

**Media**

### Image Processing

_Libraries for manipulating images._

- Barcodes and QR Codes
  - [qrcode](https://github.com/lincolnloop/python-qrcode) [![GitHub stars](https://img.shields.io/github/stars/lincolnloop/python-qrcode?style=flat)](https://github.com/lincolnloop/python-qrcode/stargazers) - A pure Python QR Code generator.
  - [python-barcode](https://github.com/WhyNotHugo/python-barcode) [![GitHub stars](https://img.shields.io/github/stars/WhyNotHugo/python-barcode?style=flat)](https://github.com/WhyNotHugo/python-barcode/stargazers) - Create barcodes in Python with no extra dependencies.
- General
  - [pillow](https://github.com/python-pillow/Pillow) [![GitHub stars](https://img.shields.io/github/stars/python-pillow/Pillow?style=flat)](https://github.com/python-pillow/Pillow/stargazers) - Pillow is the friendly [PIL](https://www.pythonware.com/products/pil/) fork.
  - [scikit-image](https://github.com/scikit-image/scikit-image) [![GitHub stars](https://img.shields.io/github/stars/scikit-image/scikit-image?style=flat)](https://github.com/scikit-image/scikit-image/stargazers) - A Python library for (scientific) image processing.
  - [rembg](https://github.com/danielgatis/rembg) [![GitHub stars](https://img.shields.io/github/stars/danielgatis/rembg?style=flat)](https://github.com/danielgatis/rembg/stargazers) - A tool to remove image backgrounds.
  - [wand](https://github.com/emcconville/wand) [![GitHub stars](https://img.shields.io/github/stars/emcconville/wand?style=flat)](https://github.com/emcconville/wand/stargazers) - Python bindings for [MagickWand](https://www.imagemagick.org/script/magick-wand.php), C API for ImageMagick.
  - [pyvips](https://github.com/libvips/pyvips) [![GitHub stars](https://img.shields.io/github/stars/libvips/pyvips?style=flat)](https://github.com/libvips/pyvips/stargazers) - A fast image processing library with low memory needs.
- Image Serving
  - [thumbor](https://github.com/thumbor/thumbor) [![GitHub stars](https://img.shields.io/github/stars/thumbor/thumbor?style=flat)](https://github.com/thumbor/thumbor/stargazers) - A smart imaging service. It enables on-demand crop, re-sizing and flipping of images.

### Audio & Video Processing

_Libraries for manipulating audio, video, and their metadata._

- Audio
  - [pydub](https://github.com/jiaaro/pydub) [![GitHub stars](https://img.shields.io/github/stars/jiaaro/pydub?style=flat)](https://github.com/jiaaro/pydub/stargazers) - Manipulate audio with a simple and easy high level interface.
  - [librosa](https://github.com/librosa/librosa) [![GitHub stars](https://img.shields.io/github/stars/librosa/librosa?style=flat)](https://github.com/librosa/librosa/stargazers) - Python library for audio and music analysis.
- Video
  - [moviepy](https://github.com/Zulko/moviepy) [![GitHub stars](https://img.shields.io/github/stars/Zulko/moviepy?style=flat)](https://github.com/Zulko/moviepy/stargazers) - A module for script-based movie editing with many formats, including animated GIFs.
  - [vidgear](https://github.com/abhiTronix/vidgear) [![GitHub stars](https://img.shields.io/github/stars/abhiTronix/vidgear?style=flat)](https://github.com/abhiTronix/vidgear/stargazers) - Most Powerful multi-threaded Video Processing framework.
- Metadata
  - [mutagen](https://github.com/quodlibet/mutagen) [![GitHub stars](https://img.shields.io/github/stars/quodlibet/mutagen?style=flat)](https://github.com/quodlibet/mutagen/stargazers) - A Python module to handle audio metadata.
  - [tinytag](https://github.com/tinytag/tinytag) [![GitHub stars](https://img.shields.io/github/stars/tinytag/tinytag?style=flat)](https://github.com/tinytag/tinytag/stargazers) - A library for reading music meta data of MP3, OGG, FLAC and Wave files.
  - [beets](https://github.com/beetbox/beets) [![GitHub stars](https://img.shields.io/github/stars/beetbox/beets?style=flat)](https://github.com/beetbox/beets/stargazers) - A music library manager and [MusicBrainz](https://musicbrainz.org/) tagger.

### Game Development

_Awesome game development libraries._

- 3D Engines
  - [panda3d](https://github.com/panda3d/panda3d) [![GitHub stars](https://img.shields.io/github/stars/panda3d/panda3d?style=flat)](https://github.com/panda3d/panda3d/stargazers) - 3D game engine developed by Disney.
- Game Frameworks
  - [pygame](https://github.com/pygame/pygame) [![GitHub stars](https://img.shields.io/github/stars/pygame/pygame?style=flat)](https://github.com/pygame/pygame/stargazers) - Pygame is a set of Python modules designed for writing games.
  - [pyglet](https://github.com/pyglet/pyglet) [![GitHub stars](https://img.shields.io/github/stars/pyglet/pyglet?style=flat)](https://github.com/pyglet/pyglet/stargazers) - A cross-platform windowing and multimedia library for Python.
  - [pygame-ce](https://github.com/pygame-community/pygame-ce) [![GitHub stars](https://img.shields.io/github/stars/pygame-community/pygame-ce?style=flat)](https://github.com/pygame-community/pygame-ce/stargazers) - An actively developed drop-in replacement with new features and performance improvements ([pygame](https://github.com/pygame/pygame) [![GitHub stars](https://img.shields.io/github/stars/pygame/pygame?style=flat)](https://github.com/pygame/pygame/stargazers) fork).
  - [arcade](https://github.com/pythonarcade/arcade) [![GitHub stars](https://img.shields.io/github/stars/pythonarcade/arcade?style=flat)](https://github.com/pythonarcade/arcade/stargazers) - Arcade is a modern Python framework for crafting games with compelling graphics and sound.
- Visual Novels
  - [renpy](https://github.com/renpy/renpy) [![GitHub stars](https://img.shields.io/github/stars/renpy/renpy?style=flat)](https://github.com/renpy/renpy/stargazers) - A Visual Novel engine.

**Python Language**

### Implementations

_Implementations of Python._

- [cpython](https://github.com/python/cpython) [![GitHub stars](https://img.shields.io/github/stars/python/cpython?style=flat)](https://github.com/python/cpython/stargazers) - Default, most widely used implementation of the Python programming language written in C.
- [micropython](https://github.com/micropython/micropython) [![GitHub stars](https://img.shields.io/github/stars/micropython/micropython?style=flat)](https://github.com/micropython/micropython/stargazers) - A lean and efficient Python programming language implementation.
- [pypy](https://github.com/pypy/pypy) [![GitHub stars](https://img.shields.io/github/stars/pypy/pypy?style=flat)](https://github.com/pypy/pypy/stargazers) - A very fast and compliant implementation of the Python language.
- [Cython](https://github.com/cython/cython) [![GitHub stars](https://img.shields.io/github/stars/cython/cython?style=flat)](https://github.com/cython/cython/stargazers) - Optimizing Static Compiler for Python.
- [pyodide](https://github.com/pyodide/pyodide) [![GitHub stars](https://img.shields.io/github/stars/pyodide/pyodide?style=flat)](https://github.com/pyodide/pyodide/stargazers) - Python distribution for the browser and Node.js based on WebAssembly.

### Built-in Classes Enhancement

_Libraries for enhancing Python built-in classes._

- [attrs](https://github.com/python-attrs/attrs) [![GitHub stars](https://img.shields.io/github/stars/python-attrs/attrs?style=flat)](https://github.com/python-attrs/attrs/stargazers) - Replacement for `__init__`, `__eq__`, `__repr__`, etc. boilerplate in class definitions.
- [bidict](https://github.com/jab/bidict) [![GitHub stars](https://img.shields.io/github/stars/jab/bidict?style=flat)](https://github.com/jab/bidict/stargazers) - Efficient, Pythonic bidirectional map data structures and related functionality.
- [uuid-utils](https://github.com/aminalaee/uuid-utils) [![GitHub stars](https://img.shields.io/github/stars/aminalaee/uuid-utils?style=flat)](https://github.com/aminalaee/uuid-utils/stargazers) - A fast, Rust-backed drop-in replacement for Python's built-in `uuid` module, supporting RFC 9562 (UUIDv6, UUIDv7, and UUIDv8).
- [python-box](https://github.com/cdgriffith/Box) [![GitHub stars](https://img.shields.io/github/stars/cdgriffith/Box?style=flat)](https://github.com/cdgriffith/Box/stargazers) - Python dictionaries with advanced dot notation access.

### Functional Programming

_Functional Programming with Python._

- [functools](https://docs.python.org/3/library/functools.html) - (Python standard library) Higher-order functions and operations on callable objects.
- [more-itertools](https://github.com/more-itertools/more-itertools) [![GitHub stars](https://img.shields.io/github/stars/more-itertools/more-itertools?style=flat)](https://github.com/more-itertools/more-itertools/stargazers) - More routines for operating on iterables, beyond `itertools`.
- [toolz](https://github.com/pytoolz/toolz) [![GitHub stars](https://img.shields.io/github/stars/pytoolz/toolz?style=flat)](https://github.com/pytoolz/toolz/stargazers) - A collection of functional utilities for iterators, functions, and dictionaries. Also available as [cytoolz](https://github.com/pytoolz/cytoolz/) [![GitHub stars](https://img.shields.io/github/stars/pytoolz/cytoolz/?style=flat)](https://github.com/pytoolz/cytoolz//stargazers) for Cython-accelerated performance.
- [funcy](https://github.com/Suor/funcy) [![GitHub stars](https://img.shields.io/github/stars/Suor/funcy?style=flat)](https://github.com/Suor/funcy/stargazers) - A fancy and practical functional tools.
- [returns](https://github.com/dry-python/returns) [![GitHub stars](https://img.shields.io/github/stars/dry-python/returns?style=flat)](https://github.com/dry-python/returns/stargazers) - A set of type-safe monads, transformers, and composition utilities.

### Asynchronous Programming

_Libraries for asynchronous, concurrent and parallel execution. Also see [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio) [![GitHub stars](https://img.shields.io/github/stars/timofurrer/awesome-asyncio?style=flat)](https://github.com/timofurrer/awesome-asyncio/stargazers)._

- Async I/O
  - [asyncio](https://docs.python.org/3/library/asyncio.html) - (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
    - [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio) [![GitHub stars](https://img.shields.io/github/stars/timofurrer/awesome-asyncio?style=flat)](https://github.com/timofurrer/awesome-asyncio/stargazers)
  - [anyio](https://github.com/agronholm/anyio) [![GitHub stars](https://img.shields.io/github/stars/agronholm/anyio?style=flat)](https://github.com/agronholm/anyio/stargazers) - A high-level async concurrency and networking framework that works on top of asyncio or trio.
  - [uvloop](https://github.com/MagicStack/uvloop) [![GitHub stars](https://img.shields.io/github/stars/MagicStack/uvloop?style=flat)](https://github.com/MagicStack/uvloop/stargazers) - Ultra fast asyncio event loop.
  - [trio](https://github.com/python-trio/trio) [![GitHub stars](https://img.shields.io/github/stars/python-trio/trio?style=flat)](https://github.com/python-trio/trio/stargazers) - A friendly library for async concurrency and I/O.
  - [gevent](https://github.com/gevent/gevent) [![GitHub stars](https://img.shields.io/github/stars/gevent/gevent?style=flat)](https://github.com/gevent/gevent/stargazers) - A coroutine-based Python networking library that uses [greenlet](https://github.com/python-greenlet/greenlet) [![GitHub stars](https://img.shields.io/github/stars/python-greenlet/greenlet?style=flat)](https://github.com/python-greenlet/greenlet/stargazers).
  - [Twisted](https://github.com/twisted/twisted) [![GitHub stars](https://img.shields.io/github/stars/twisted/twisted?style=flat)](https://github.com/twisted/twisted/stargazers) - An event-driven networking engine.
- Parallelism
  - [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) - (Python standard library) A high-level interface for asynchronously executing callables.
  - [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - (Python standard library) Process-based parallelism.

### Date and Time

_Libraries for working with dates and times._

- [zoneinfo](https://docs.python.org/3/library/zoneinfo.html) - (Python standard library) IANA time zone support. Brings the [tz database](https://en.wikipedia.org/wiki/Tz_database) into Python.
- [python-dateutil](https://github.com/dateutil/dateutil) [![GitHub stars](https://img.shields.io/github/stars/dateutil/dateutil?style=flat)](https://github.com/dateutil/dateutil/stargazers) - Extensions to the standard Python [datetime](https://docs.python.org/3/library/datetime.html) module.
- [dateparser](https://github.com/scrapinghub/dateparser) [![GitHub stars](https://img.shields.io/github/stars/scrapinghub/dateparser?style=flat)](https://github.com/scrapinghub/dateparser/stargazers) - A Python parser for human-readable dates in dozens of languages.
- [pendulum](https://github.com/python-pendulum/pendulum) [![GitHub stars](https://img.shields.io/github/stars/python-pendulum/pendulum?style=flat)](https://github.com/python-pendulum/pendulum/stargazers) - Python datetimes made easy.
- [whenever](https://github.com/ariebovenberg/whenever) [![GitHub stars](https://img.shields.io/github/stars/ariebovenberg/whenever?style=flat)](https://github.com/ariebovenberg/whenever/stargazers) - A modern datetime library, type-safe and DST-safe, backed by Rust.

**Python Toolchain**

### Environment Management

_Libraries for Python version and virtual environment management._

- [virtualenv](https://github.com/pypa/virtualenv) [![GitHub stars](https://img.shields.io/github/stars/pypa/virtualenv?style=flat)](https://github.com/pypa/virtualenv/stargazers) - A tool to create isolated Python environments.
- [uv](https://github.com/astral-sh/uv) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/uv?style=flat)](https://github.com/astral-sh/uv/stargazers) - An extremely fast Python version, package and project manager, written in Rust.
- [pyenv](https://github.com/pyenv/pyenv) [![GitHub stars](https://img.shields.io/github/stars/pyenv/pyenv?style=flat)](https://github.com/pyenv/pyenv/stargazers) - Simple Python version management.

### Package Management

_Libraries for package and dependency management._

- Package Managers
  - [pip](https://github.com/pypa/pip) [![GitHub stars](https://img.shields.io/github/stars/pypa/pip?style=flat)](https://github.com/pypa/pip/stargazers) - The package installer for Python.
  - [uv](https://github.com/astral-sh/uv) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/uv?style=flat)](https://github.com/astral-sh/uv/stargazers) - An extremely fast Python version, package and project manager, written in Rust.
  - [poetry](https://github.com/python-poetry/poetry) [![GitHub stars](https://img.shields.io/github/stars/python-poetry/poetry?style=flat)](https://github.com/python-poetry/poetry/stargazers) - Python dependency management and packaging made easy.
  - [hatch](https://github.com/pypa/hatch) [![GitHub stars](https://img.shields.io/github/stars/pypa/hatch?style=flat)](https://github.com/pypa/hatch/stargazers) - Modern, extensible Python project manager for environments, builds, and publishing.
  - [pipx](https://github.com/pypa/pipx) [![GitHub stars](https://img.shields.io/github/stars/pypa/pipx?style=flat)](https://github.com/pypa/pipx/stargazers) - Install and Run Python Applications in Isolated Environments. Like `npx` in Node.js.
  - [conda](https://github.com/conda/conda/) [![GitHub stars](https://img.shields.io/github/stars/conda/conda/?style=flat)](https://github.com/conda/conda//stargazers) - Cross-platform, Python-agnostic binary package manager.
- Build Backends
  - [setuptools](https://github.com/pypa/setuptools) [![GitHub stars](https://img.shields.io/github/stars/pypa/setuptools?style=flat)](https://github.com/pypa/setuptools/stargazers) - The historical and still most widely used pyproject build backend.
  - [hatchling](https://github.com/pypa/hatch) [![GitHub stars](https://img.shields.io/github/stars/pypa/hatch?style=flat)](https://github.com/pypa/hatch/stargazers) - Modern, extensible build backend from the hatch project.
  - [uv-build](https://github.com/astral-sh/uv) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/uv?style=flat)](https://github.com/astral-sh/uv/stargazers) - uv's fast, minimal build backend for pure-Python projects.

### Package Repositories

_Local PyPI repository server and proxies._

- [bandersnatch](https://github.com/pypa/bandersnatch/) [![GitHub stars](https://img.shields.io/github/stars/pypa/bandersnatch/?style=flat)](https://github.com/pypa/bandersnatch//stargazers) - PyPI mirroring tool provided by Python Packaging Authority (PyPA).
- [devpi](https://github.com/devpi/devpi) [![GitHub stars](https://img.shields.io/github/stars/devpi/devpi?style=flat)](https://github.com/devpi/devpi/stargazers) - PyPI server and packaging/testing/release tool.
- [warehouse](https://github.com/pypi/warehouse) [![GitHub stars](https://img.shields.io/github/stars/pypi/warehouse?style=flat)](https://github.com/pypi/warehouse/stargazers) - Next generation Python Package Repository (PyPI).

### Distribution

_Libraries to create packaged executables for release distribution._

- Executables
  - [pyinstaller](https://github.com/pyinstaller/pyinstaller) [![GitHub stars](https://img.shields.io/github/stars/pyinstaller/pyinstaller?style=flat)](https://github.com/pyinstaller/pyinstaller/stargazers) - Converts Python programs into stand-alone executables (cross-platform).
  - [Nuitka](https://github.com/Nuitka/Nuitka) [![GitHub stars](https://img.shields.io/github/stars/Nuitka/Nuitka?style=flat)](https://github.com/Nuitka/Nuitka/stargazers) - Compiles Python programs into high-performance standalone executables (cross-platform, supports all Python versions).
  - [shiv](https://github.com/linkedin/shiv) [![GitHub stars](https://img.shields.io/github/stars/linkedin/shiv?style=flat)](https://github.com/linkedin/shiv/stargazers) - A command line utility for building fully self-contained zipapps (PEP 441), but with all their dependencies included.
  - [cx-Freeze](https://github.com/marcelotduarte/cx_Freeze) [![GitHub stars](https://img.shields.io/github/stars/marcelotduarte/cx_Freeze?style=flat)](https://github.com/marcelotduarte/cx_Freeze/stargazers) - It is a Python tool that converts Python scripts into standalone executables and installers for Windows, macOS, and Linux.
- Obfuscation
  - [pyarmor](https://github.com/dashingsoft/pyarmor) [![GitHub stars](https://img.shields.io/github/stars/dashingsoft/pyarmor?style=flat)](https://github.com/dashingsoft/pyarmor/stargazers) - A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

### Configuration Files

_Libraries for storing and parsing configuration options._

- [configparser](https://docs.python.org/3/library/configparser.html) - (Python standard library) INI file parser.
- [python-dotenv](https://github.com/theskumar/python-dotenv) [![GitHub stars](https://img.shields.io/github/stars/theskumar/python-dotenv?style=flat)](https://github.com/theskumar/python-dotenv/stargazers) - Reads key-value pairs from a `.env` file and sets them as environment variables.
- [pydantic-settings](https://github.com/pydantic/pydantic-settings) [![GitHub stars](https://img.shields.io/github/stars/pydantic/pydantic-settings?style=flat)](https://github.com/pydantic/pydantic-settings/stargazers) - Settings management using Pydantic models with validation, loading from environment variables and secrets files.
- [hydra-core](https://github.com/facebookresearch/hydra) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/hydra?style=flat)](https://github.com/facebookresearch/hydra/stargazers) - Hydra is a framework for elegantly configuring complex applications.
- [dynaconf](https://github.com/dynaconf/dynaconf) [![GitHub stars](https://img.shields.io/github/stars/dynaconf/dynaconf?style=flat)](https://github.com/dynaconf/dynaconf/stargazers) - Dynaconf is a configuration manager with plugins for Django, Flask and FastAPI.

**Security**

### Cryptography

_Libraries for cryptographic primitives and secure protocols._

- [cryptography](https://github.com/pyca/cryptography) [![GitHub stars](https://img.shields.io/github/stars/pyca/cryptography?style=flat)](https://github.com/pyca/cryptography/stargazers) - A package designed to expose cryptographic primitives and recipes to Python developers.
- [pynacl](https://github.com/pyca/pynacl) [![GitHub stars](https://img.shields.io/github/stars/pyca/pynacl?style=flat)](https://github.com/pyca/pynacl/stargazers) - Python binding to the Networking and Cryptography (NaCl) library.
- [paramiko](https://github.com/paramiko/paramiko) [![GitHub stars](https://img.shields.io/github/stars/paramiko/paramiko?style=flat)](https://github.com/paramiko/paramiko/stargazers) - The leading native Python SSHv2 protocol library.
- [itsdangerous](https://github.com/pallets/itsdangerous) [![GitHub stars](https://img.shields.io/github/stars/pallets/itsdangerous?style=flat)](https://github.com/pallets/itsdangerous/stargazers) - Various helpers to pass trusted data to untrusted environments.

### Penetration Testing

_Frameworks and tools for penetration testing._

- [mitmproxy](https://github.com/mitmproxy/mitmproxy) [![GitHub stars](https://img.shields.io/github/stars/mitmproxy/mitmproxy?style=flat)](https://github.com/mitmproxy/mitmproxy/stargazers) - An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.
- [sqlmap](https://github.com/sqlmapproject/sqlmap) [![GitHub stars](https://img.shields.io/github/stars/sqlmapproject/sqlmap?style=flat)](https://github.com/sqlmapproject/sqlmap/stargazers) - Automatic SQL injection and database takeover tool.
- [sherlock-project](https://github.com/sherlock-project/sherlock) [![GitHub stars](https://img.shields.io/github/stars/sherlock-project/sherlock?style=flat)](https://github.com/sherlock-project/sherlock/stargazers) - Hunt down social media accounts by username across social networks.
- [social-engineer-toolkit](https://github.com/trustedsec/social-engineer-toolkit) [![GitHub stars](https://img.shields.io/github/stars/trustedsec/social-engineer-toolkit?style=flat)](https://github.com/trustedsec/social-engineer-toolkit/stargazers) - A toolkit for social engineering.

### Supply Chain Security

_Tools for auditing dependencies against known vulnerabilities._

- [pip-audit](https://github.com/pypa/pip-audit) [![GitHub stars](https://img.shields.io/github/stars/pypa/pip-audit?style=flat)](https://github.com/pypa/pip-audit/stargazers) - Audits Python environments and dependency trees for known vulnerabilities, using the PyPI Advisory Database and OSV.
- [uv-audit](https://github.com/astral-sh/uv) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/uv?style=flat)](https://github.com/astral-sh/uv/stargazers) - (part of uv) uv's [dependency vulnerability and malware scanning](https://docs.astral.sh/uv/reference/cli/#uv-audit) backed by OSV.

### Web Security

_Libraries for application-layer web security._

- [secure](https://github.com/TypeError/secure) [![GitHub stars](https://img.shields.io/github/stars/TypeError/secure?style=flat)](https://github.com/TypeError/secure/stargazers) - HTTP security headers for Python web applications with ASGI and WSGI middleware.

**Other**

### Hardware

_Libraries for programming with hardware._

- [bleak](https://github.com/hbldh/bleak) [![GitHub stars](https://img.shields.io/github/stars/hbldh/bleak?style=flat)](https://github.com/hbldh/bleak/stargazers) - A cross platform Bluetooth Low Energy Client for Python using asyncio.
- [pynput](https://github.com/moses-palmer/pynput) [![GitHub stars](https://img.shields.io/github/stars/moses-palmer/pynput?style=flat)](https://github.com/moses-palmer/pynput/stargazers) - A library to control and monitor input devices.
- [jumpstarter](https://github.com/jumpstarter-dev/jumpstarter) [![GitHub stars](https://img.shields.io/github/stars/jumpstarter-dev/jumpstarter?style=flat)](https://github.com/jumpstarter-dev/jumpstarter/stargazers) - A hardware-in-the-loop testing framework with a Python client library for automated testing on real and virtual hardware.

### Microsoft Windows

_Python programming on Microsoft Windows._

- [pythonnet](https://github.com/pythonnet/pythonnet) [![GitHub stars](https://img.shields.io/github/stars/pythonnet/pythonnet?style=flat)](https://github.com/pythonnet/pythonnet/stargazers) - Python Integration with the .NET Common Language Runtime (CLR).
- [pywin32](https://github.com/mhammond/pywin32) [![GitHub stars](https://img.shields.io/github/stars/mhammond/pywin32?style=flat)](https://github.com/mhammond/pywin32/stargazers) - Python Extensions for Windows.
- [pyenv-win](https://github.com/pyenv-win/pyenv-win) [![GitHub stars](https://img.shields.io/github/stars/pyenv-win/pyenv-win?style=flat)](https://github.com/pyenv-win/pyenv-win/stargazers) - A Python version manager for Windows ([pyenv](https://github.com/pyenv/pyenv) [![GitHub stars](https://img.shields.io/github/stars/pyenv/pyenv?style=flat)](https://github.com/pyenv/pyenv/stargazers) fork).
- [winpython](https://github.com/winpython/winpython) [![GitHub stars](https://img.shields.io/github/stars/winpython/winpython?style=flat)](https://github.com/winpython/winpython/stargazers) - Portable development environment for Windows 10/11.

### Miscellaneous

_Useful libraries or tools that don't fit in the categories above._

- [blinker](https://github.com/pallets-eco/blinker) [![GitHub stars](https://img.shields.io/github/stars/pallets-eco/blinker?style=flat)](https://github.com/pallets-eco/blinker/stargazers) - A fast Python in-process signal/event dispatching system.
- [boltons](https://github.com/mahmoud/boltons) [![GitHub stars](https://img.shields.io/github/stars/mahmoud/boltons?style=flat)](https://github.com/mahmoud/boltons/stargazers) - A set of pure-Python utilities.

## Resources

Where to discover learning resources or new Python libraries.

### Newsletters

- [Awesome Python Newsletter](https://python.libhunt.com/newsletter)
- [Pycoder's Weekly](https://pycoders.com/)
- [Python Tricks](https://realpython.com/python-tricks/)
- [Python Weekly](https://www.pythonweekly.com/)

### Podcasts

- [Django Chat](https://djangochat.com/)
- [PyPodcats](https://pypodcats.live)
- [Python Bytes](https://pythonbytes.fm)
- [Talk Python To Me](https://talkpython.fm/)
- [The Real Python Podcast](https://realpython.com/podcasts/rpp/)

### Websites

- [Python Developer Tooling Handbook](https://pydevtools.com/) - Comprehensive guide to modern Python developer tools covering package management, linting, type checking, testing, and more.

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](https://github.com/vinta/awesome-python/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/vinta/awesome-python/blob/master/CONTRIBUTING.md/stargazers) first.

---

If you have any question about this opinionated list, do not hesitate to contact [@vinta](https://x.com/vinta) on X (Twitter).
