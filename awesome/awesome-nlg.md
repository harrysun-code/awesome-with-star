# Natural Language Generation

[![GitHub stars](https://img.shields.io/github/stars/accelerated-text/awesome-nlg?style=flat)](https://github.com/accelerated-text/awesome-nlg/stargazers)

# Awesome Natural Language Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Piscis Magnus from BL Harley 647](logo.png)

Natural Language Generation is a broad domain with applications in chat-bots, story generation, and data descriptions. There is a wide spectrum of different technologies addressing parts or the whole of the NLG process. This list aims to represent this deversity of NLG applications and techniques by providing links to various projects, tools, research papers, and learning materials.

## Contents

- [Datasets](#datasets)
- [Dialog](#dialog)
- [Evaluation](#evaluation)
- [Grammar](#grammar)
- [Libraries](#libraries)
- [Narrative Generation](#narrative-generation)
- [Neural Natural Language Generation](#neural-natural-language-generation)
- [Papers and Articles](#papers-and-articles)
- [Products](#products)
- [Realizers](#realizers)
- [Templating Languages](#templating-languages)
- [Videos](#videos)

## Datasets

- [Alex Context NLG Dataset](https://github.com/UFAL-DSG/alex_context_nlg_dataset) [![GitHub stars](https://img.shields.io/github/stars/UFAL-DSG/alex_context_nlg_dataset?style=flat)](https://github.com/UFAL-DSG/alex_context_nlg_dataset/stargazers) - A dataset for NLG in dialogue systems in the public transport information domain.
- [Box-score data](https://github.com/harvardnlp/boxscore-data/) [![GitHub stars](https://img.shields.io/github/stars/harvardnlp/boxscore-data/?style=flat)](https://github.com/harvardnlp/boxscore-data//stargazers) - This dataset consists of (human-written) NBA basketball game summaries aligned with their corresponding box- and line-scores.
- [E2E](http://www.macs.hw.ac.uk/InteractionLab/E2E) - This shared task focuses on recent end-to-end (E2E), data-driven NLG methods, which jointly learn sentence planning and surface realisation from non-aligned data.
- [Neural-Wikipedian](https://github.com/pvougiou/Neural-Wikipedian) [![GitHub stars](https://img.shields.io/github/stars/pvougiou/Neural-Wikipedian?style=flat)](https://github.com/pvougiou/Neural-Wikipedian/stargazers) - The repository contains the code along with the required corpora that were used in order to build a system that "learns" how to generate English biographies for Semantic Web triples.
- [WeatherGov](https://cs.stanford.edu/~pliang/data/weather-data.zip) - Computer-generated weather forecasts from weather.gov (US public forecast), along with corresponding weather data.
- [WebNLG](https://github.com/ThiagoCF05/webnlg) [![GitHub stars](https://img.shields.io/github/stars/ThiagoCF05/webnlg?style=flat)](https://github.com/ThiagoCF05/webnlg/stargazers) - The enriched version of the WebNLG - a resource for evaluating common NLG tasks, including Discourse Ordering, Lexicalization and Referring Expression Generation.
- [WikiBio - wikipedia biography dataset](https://rlebret.github.io/wikipedia-biography-dataset/) - This dataset gathers 728,321 biographies from wikipedia. It aims at evaluating text generation algorithms.
- [The Schema-Guided Dialogue Dataset](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue) [![GitHub stars](https://img.shields.io/github/stars/google-research-datasets/dstc8-schema-guided-dialogue?style=flat)](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue/stargazers) - The Schema-Guided Dialogue (SGD) dataset consists of over 20k annotated multi-domain, task-oriented conversations between a human and a virtual assistant.
- [The Wikipedia company corpus](https://gricad-gitlab.univ-grenoble-alpes.fr/getalp/wikipediacompanycorpus) - Company descriptions collected from Wikipedia. The dataset contains semantic representations, short, and long descriptions for 51K companies in English.
- [YelpNLG](https://nlds.soe.ucsc.edu/yelpnlg) - YelpNLG provides resources for natural language generation of restaurant reviews.

## Dialog

- [Chatito](https://github.com/rodrigopivi/Chatito) [![GitHub stars](https://img.shields.io/github/stars/rodrigopivi/Chatito?style=flat)](https://github.com/rodrigopivi/Chatito/stargazers) - Generate datasets for AI chatbots, NLP tasks, named entity recognition or text classification models using a simple DSL!
- [NNDIAL](https://github.com/shawnwun/NNDIAL) [![GitHub stars](https://img.shields.io/github/stars/shawnwun/NNDIAL?style=flat)](https://github.com/shawnwun/NNDIAL/stargazers) - NNDial is an open source toolkit for building end-to-end trainable task-oriented dialogue models.
- [Plato](https://github.com/uber-research/plato-research-dialogue-system) [![GitHub stars](https://img.shields.io/github/stars/uber-research/plato-research-dialogue-system?style=flat)](https://github.com/uber-research/plato-research-dialogue-system/stargazers) - This is the Plato Research Dialogue System, a flexible platform for developing conversational AI agents. 
- [RNNLG](https://github.com/shawnwun/RNNLG) [![GitHub stars](https://img.shields.io/github/stars/shawnwun/RNNLG?style=flat)](https://github.com/shawnwun/RNNLG/stargazers) - RNNLG is an open source benchmark toolkit for Natural Language Generation (NLG) in spoken dialogue system application domains.
- [TGen](https://github.com/UFAL-DSG/tgen) [![GitHub stars](https://img.shields.io/github/stars/UFAL-DSG/tgen?style=flat)](https://github.com/UFAL-DSG/tgen/stargazers) - Statistical NLG for spoken dialogue systems.

## Evaluation

- [BLEURT: a Transfer Learning-Based Metric for Natural Language Generation](https://github.com/google-research/bleurt) [![GitHub stars](https://img.shields.io/github/stars/google-research/bleurt?style=flat)](https://github.com/google-research/bleurt/stargazers)
- [compare-mt](https://github.com/neulab/compare-mt) [![GitHub stars](https://img.shields.io/github/stars/neulab/compare-mt?style=flat)](https://github.com/neulab/compare-mt/stargazers) - A tool for holistic analysis of language generations systems.
- [GEM](https://gem-benchmark.com/) - a benchmark environment for NLG with a focus on its Evaluation, both through human annotations and automated Metrics.
- [NLG-eval](https://github.com/Maluuba/nlg-eval) [![GitHub stars](https://img.shields.io/github/stars/Maluuba/nlg-eval?style=flat)](https://github.com/Maluuba/nlg-eval/stargazers) - Evaluation code for various unsupervised automated metrics for Natural Language Generation.
- [VizSeq](https://github.com/facebookresearch/vizseq) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/vizseq?style=flat)](https://github.com/facebookresearch/vizseq/stargazers) - A Visual Analysis Toolkit for Text Generation Tasks.

## Grammar

- [OpenCCG](https://github.com/OpenCCG/openccg) [![GitHub stars](https://img.shields.io/github/stars/OpenCCG/openccg?style=flat)](https://github.com/OpenCCG/openccg/stargazers) - OpenCCG library for parsing and realization with CCG.
- [GrammaticalFramework](http://www.grammaticalframework.org/) - A programming language for multilingual grammar applications.
- [EasyCCG](https://github.com/mikelewis0/easyccg) [![GitHub stars](https://img.shields.io/github/stars/mikelewis0/easyccg?style=flat)](https://github.com/mikelewis0/easyccg/stargazers) - CCG: All combinators, common grammar format, parsing to logical form, parameter estimation for probabilistic CCG.
- [CCG Lab](https://github.com/bozsahin/ccglab) [![GitHub stars](https://img.shields.io/github/stars/bozsahin/ccglab?style=flat)](https://github.com/bozsahin/ccglab/stargazers) - All combinators, common grammar format, parsing to logical form, parameter estimation for probabilistic CCG.
- [CCGweb](https://github.com/texttheater/ccgweb) [![GitHub stars](https://img.shields.io/github/stars/texttheater/ccgweb?style=flat)](https://github.com/texttheater/ccgweb/stargazers) - A Web platform for parsing and annotation.

## Libraries

- [Cron Expression Descriptor](https://github.com/bradymholt/cron-expression-descriptor) [![GitHub stars](https://img.shields.io/github/stars/bradymholt/cron-expression-descriptor?style=flat)](https://github.com/bradymholt/cron-expression-descriptor/stargazers) - A .NET library that converts cron expressions into human readable descriptions.
- [Number Words](https://github.com/tokenmill/numberwords) [![GitHub stars](https://img.shields.io/github/stars/tokenmill/numberwords?style=flat)](https://github.com/tokenmill/numberwords/stargazers) - Convert a number to an approximated text expression: from '0.23' to 'less than a quarter'.
- [Writebot](https://docs.writebot.app) - A NodeJS library that makes it easier to use GPT-3 by using presets.

## Narrative Generation

- [Random Story Generator](https://github.com/aherriot/story-generator) [![GitHub stars](https://img.shields.io/github/stars/aherriot/story-generator?style=flat)](https://github.com/aherriot/story-generator/stargazers) - Using Natural Language Generation (NLG) to create a random short story.
- [Tracery](https://github.com/galaxykate/tracery) [![GitHub stars](https://img.shields.io/github/stars/galaxykate/tracery?style=flat)](https://github.com/galaxykate/tracery/stargazers) - A story-grammar generation library for JavaScript.

## Neural Natural Language Generation

- [aitextgen](https://github.com/minimaxir/aitextgen) [![GitHub stars](https://img.shields.io/github/stars/minimaxir/aitextgen?style=flat)](https://github.com/minimaxir/aitextgen/stargazers) - A robust Python tool for text-based AI training and generation using GPT-2.
- [graph-2-text](https://github.com/diegma/graph-2-text) [![GitHub stars](https://img.shields.io/github/stars/diegma/graph-2-text?style=flat)](https://github.com/diegma/graph-2-text/stargazers) - Graph to sequence implemented in Pytorch combining Graph convolutional networks and opennmt-py.
- [Image Caption Generator](https://github.com/neural-nuts/image-caption-generator) [![GitHub stars](https://img.shields.io/github/stars/neural-nuts/image-caption-generator?style=flat)](https://github.com/neural-nuts/image-caption-generator/stargazers) - A Neural Network based generative model for captioning images using Tensorflow.
- [lightnlg](https://github.com/kasnerz/lightnlg) [![GitHub stars](https://img.shields.io/github/stars/kasnerz/lightnlg?style=flat)](https://github.com/kasnerz/lightnlg/stargazers) - A minimalistic codebase for finetuning and interacting with NLG models using PyTorch Lightning.
- [PaperRobot: Incremental Draft Generation of Scientific Ideas](https://github.com/EagleW/PaperRobot) [![GitHub stars](https://img.shields.io/github/stars/EagleW/PaperRobot?style=flat)](https://github.com/EagleW/PaperRobot/stargazers) - We present a PaperRobot who performs as an automatic research assistant.
- [PPLM](https://github.com/uber-research/PPLM) [![GitHub stars](https://img.shields.io/github/stars/uber-research/PPLM?style=flat)](https://github.com/uber-research/PPLM/stargazers) - Plug and Play Language Model implementation. Allows to steer topic and attributes of GPT-2 models.
- [Question Generation using hugstransformers](https://github.com/patil-suraj/question_generation) [![GitHub stars](https://img.shields.io/github/stars/patil-suraj/question_generation?style=flat)](https://github.com/patil-suraj/question_generation/stargazers) - Question generation is the task of automatically generating questions from a text paragraph.
- [Texar](https://github.com/asyml/texar) [![GitHub stars](https://img.shields.io/github/stars/asyml/texar?style=flat)](https://github.com/asyml/texar/stargazers) - Texar is a toolkit aiming to support a broad set of machine learning, especially natural language processing and text generation tasks.
- [textgenrnn](https://github.com/minimaxir/textgenrnn) [![GitHub stars](https://img.shields.io/github/stars/minimaxir/textgenrnn?style=flat)](https://github.com/minimaxir/textgenrnn/stargazers) - Easily train your own text-generating neural network of any size and complexity on any text dataset with a few lines of code.
- [This Word Does Not Exist](https://github.com/turtlesoupy/this-word-does-not-exist) [![GitHub stars](https://img.shields.io/github/stars/turtlesoupy/this-word-does-not-exist?style=flat)](https://github.com/turtlesoupy/this-word-does-not-exist/stargazers) - This is a project allows people to train a variant of GPT-2 that makes up words, definitions and examples from scratch.
- [Transformers](https://github.com/huggingface/transformers) [![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=flat)](https://github.com/huggingface/transformers/stargazers) - State-of-the-art Natural Language Processing for TensorFlow 2.0 and PyTorch.
- [Summary Generation From Structured Data](https://github.com/akanimax/natural-language-summary-generation-from-structured-data) [![GitHub stars](https://img.shields.io/github/stars/akanimax/natural-language-summary-generation-from-structured-data?style=flat)](https://github.com/akanimax/natural-language-summary-generation-from-structured-data/stargazers) - For converting information present in the form of structured data into natural language text.

## Papers and Articles
- [2022: Repairing the Cracked Foundation: A Survey of Obstacles in Evaluation Practices for Generated Text](https://arxiv.org/abs/2202.06935)
- [2021: Vision: NLG Can Help Humanise Data and AI](https://ehudreiter.com/2021/03/17/vision-nlg-can-help-humanise-data-and-ai/)
- [2020: The Curious Case of Neural Text Degeneration](https://openreview.net/forum?id=rygGQyrFvH)
- [2020: A Gold Standard Methodology for Evaluating Accuracy in Data-To-Text Systems](https://arxiv.org/abs/2011.03992)
- [2020: Evaluating the state-of-the-art of End-to-End Natural Language Generation: The E2E NLG challenge](https://www.sciencedirect.com/science/article/pii/S0885230819300919)
- [2020: How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)
- [2020: Natural language generation: The commercial state ofthe art in 2020](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BA2417D73AF29F8073FF5B611CDEB97F/S135132492000025Xa.pdf/natural_language_generation_the_commercial_state_of_the_art_in_2020.pdf)
- [2020: Turing-NLG: A 17-billion-parameter language model by Microsoft](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/)
- [2019: A Closer Look at Recent Results of Verb Selection for Data-to-Text NLG](https://www.inlg2019.com/assets/papers/178_Paper.pdf)
- [2019: A Personalized Data-to-Text Support Tool for Cancer Patients](https://www.inlg2019.com/assets/papers/28_Paper.pdf)
- [2019: Controlling Contents in Data-to-Document Generation with Human-Designed Topic Labels](https://www.inlg2019.com/assets/papers/79_Paper.pdf)
- [2019: Generated Texts Must Be Accurate!](https://ehudreiter.com/2019/09/26/generated-texts-must-be-accurate/)
- [2019: Hotel Scribe: Generating High Variation Hotel Descriptions](https://www.inlg2019.com/assets/papers/44_Paper.pdf)
- [2019: Revisiting Challenges in Data-to-Text Generation with Fact Grounding](https://www.inlg2019.com/assets/papers/32_Paper.pdf)
- [2017: Survey of the State of the Art in NaturalLanguage Generation: Core tasks, applicationsand evaluation](https://arxiv.org/pdf/1703.09902.pdf)
- [2016: Natural Language Generation enhances human decision-making with uncertain information](https://arxiv.org/pdf/1606.03254.pdf)


## Products 

- [Accelerated Text](https://github.com/tokenmill/accelerated-text) [![GitHub stars](https://img.shields.io/github/stars/tokenmill/accelerated-text?style=flat)](https://github.com/tokenmill/accelerated-text/stargazers) - Automatically generate multiple natural language descriptions of your data varying in wording and structure.
- [RosaeNLG](https://rosaenlg.org) - An open-source library for node.js or client side (browser) execution, based on the Pug template engine, to generate texts in English, French, German and Italian.
- [Twine](http://twinery.org/) - An open-source tool for telling interactive, nonlinear stories.

## Realizers

- [Genl](https://github.com/kowey/GenI) [![GitHub stars](https://img.shields.io/github/stars/kowey/GenI?style=flat)](https://github.com/kowey/GenI/stargazers) - Surface realiser (part of a Natural Language Generation system) using Tree Adjoining Grammar.
- [JSrealB](https://github.com/rali-udem/JSrealB) [![GitHub stars](https://img.shields.io/github/stars/rali-udem/JSrealB?style=flat)](https://github.com/rali-udem/JSrealB/stargazers) - A JavaScript bilingual text realizer for web development.
- [SimpleNLG](https://github.com/simplenlg/simplenlg) [![GitHub stars](https://img.shields.io/github/stars/simplenlg/simplenlg?style=flat)](https://github.com/simplenlg/simplenlg/stargazers) - Java API for Natural Language Generation.
- [SimpleNLG DE](https://github.com/sebischair/SimpleNLG-DE) [![GitHub stars](https://img.shields.io/github/stars/sebischair/SimpleNLG-DE?style=flat)](https://github.com/sebischair/SimpleNLG-DE/stargazers) - German version of SimpleNLG 4.
- [SimpleNLG-EnFr](https://github.com/rali-udem/SimpleNLG-EnFr) [![GitHub stars](https://img.shields.io/github/stars/rali-udem/SimpleNLG-EnFr?style=flat)](https://github.com/rali-udem/SimpleNLG-EnFr/stargazers) - SimpleNLG-EnFr 1.1 is a bilingual English/French adaption of SimpleNLG v4.2.

## Templating Languages

- [calyx](https://github.com/maetl/calyx) [![GitHub stars](https://img.shields.io/github/stars/maetl/calyx?style=flat)](https://github.com/maetl/calyx/stargazers) - A Ruby library for generating text with recursive template grammars.
- [nalgene](https://github.com/spro/nalgene) [![GitHub stars](https://img.shields.io/github/stars/spro/nalgene?style=flat)](https://github.com/spro/nalgene/stargazers) - Natural language generation language.
- [StringTemplate](https://www.stringtemplate.org/) - Java template engine (with ports for C##, Objective-C, JavaScript, Scala) for generating source code, web pages, emails, or any other formatted text output. 

## Videos

- [Data-To-Text: Generating Textual Summaries of Complex Data - Ehud Reiter](https://www.youtube.com/watch?v=kFRw-wk5YOA)
- [Imitation Learning and its Application to Natural Language Generation](https://slideslive.com/38922816/imitation-learning-and-its-application-to-natural-language-generation)
- [Natural Language Generation (Introduction)](https://www.youtube.com/watch?v=4fjM72lbJaw)
- [Strata Data Conference | The future of natural language generation: 2017-2027](https://www.youtube.com/watch?v=Ls7elVbN8bI)
- [The Quest for Automated Story Generation - Mark Riedl](https://www.youtube.com/watch?v=wgcDUX_BPpk)

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, [TokenMill](https://www.tokenmill.ai) has waived all copyright and related or neighboring rights to this work.
