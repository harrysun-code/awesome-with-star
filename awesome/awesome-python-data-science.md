# Data Science

[![GitHub stars](https://img.shields.io/github/stars/krzjoa/awesome-python-data-science?style=flat)](https://github.com/krzjoa/awesome-python-data-science/stargazers)

<div align="center">
    <a href="https://krzjoa.github.io/awesome-python-data-science/"><img width="250" height="250" src="img/py-datascience.png" alt="pyds"></a>
    <br>
    <br>
    <br>
</div>

<h1 align="center">
    Awesome Python Data Science
</h1>
<div align="center"><a href="https://github.com/sindresorhus/awesome">
<img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome" border="0">
</a>
</div>
</br>

> Probably the best curated list of data science software in Python

## Contents
- [Contents](#contents)
- [Machine Learning](#machine-learning)
	- [General Purpose Machine Learning](#general-purpose-machine-learning)
  	- [Gradient Boosting](#gradient-boosting)
	- [Ensemble Methods](#ensemble-methods)
	- [Imbalanced Datasets](#imbalanced-datasets)
	- [Kernel Methods](#kernel-methods)
- [Deep Learning](#deep-learning)
	- [PyTorch](#pytorch)
	- [TensorFlow](#tensorflow)
    - [Keras](#keras)
 	- [JAX](#jax)
	- [Others](#others)
- [Automated Machine Learning](#automated-machine-learning)
- [Natural Language Processing](#natural-language-processing)
- [Computer Audition](#computer-audition)
- [Computer Vision](#computer-vision)
- [Time Series](#time-series)
- [Reinforcement Learning](#reinforcement-learning)
- [Graph Machine Learning](#graph-machine-learning)
- [Graph Manipulation](#graph-manipulation)
- [Learning-to-Rank & Recommender Systems](#learning-to-rank-&-recommender-systems)
- [Probabilistic Graphical Models](#probabilistic-graphical-models)
- [Probabilistic Methods](#probabilistic-methods)
- [Model Explanation](#model-explanation)
- [Optimization](#optimization)
- [Genetic Programming](#genetic-programming)
- [Feature Engineering](#feature-engineering)
	- [General](#general)
	- [Feature Selection](#feature-selection)
- [Visualization](#visualization)
	- [General Purposes](#general-purposes)
	- [Interactive plots](#interactive-plots)
	- [Map](#map)
	- [Automatic Plotting](#automatic-plotting)
	- [NLP](#nlp)
- [Data Manipulation](#data-manipulation)
	- [Data Frames](#data-frames)
	- [Pipelines](#pipelines)
	- [Data-centric AI](#data-centric-ai)
	- [Synthetic Data](#synthetic-data)

- [TabGAN](https://github.com/Diyago/Tabular-data-generation) [![GitHub stars](https://img.shields.io/github/stars/Diyago/Tabular-data-generation?style=flat)](https://github.com/Diyago/Tabular-data-generation/stargazers) - Synthetic tabular data generation using GANs, Diffusion Models, and LLMs. <img height="16" width="16" src="https://github.com/krzjoa/awesome-python-data-science/raw/master/img/sklearn_big.png" alt="sklearn">
- [Deployment](#deployment)
- [Statistics](#statistics)
- [Distributed Computing](#distributed-computing)
- [Experimentation](#experimentation)
- [Data Validation](#data-validation)
- [Evaluation](#evaluation)
- [Computations](#computations)
- [Web Scraping](#web-scraping)
- [Spatial Analysis](#spatial-analysis)
- [Quantum Computing](#quantum-computing)
- [Conversion](#conversion)
- [Contributing](#contributing)
- [License](#license)

## Machine Learning

### General Purpose Machine Learning
* [SciPy](https://scipy.org/) - Fundamental algorithms for scientific computing in Python
* [scikit-learn](https://scikit-learn.org/stable/) - Machine learning in Python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [PyCaret](https://github.com/pycaret/pycaret) [![GitHub stars](https://img.shields.io/github/stars/pycaret/pycaret?style=flat)](https://github.com/pycaret/pycaret/stargazers) - An open-source, low-code machine learning library in Python.  <img height="20" src="img/R_big.png" alt="R inspired lib">
* [Shogun](https://github.com/shogun-toolbox/shogun) [![GitHub stars](https://img.shields.io/github/stars/shogun-toolbox/shogun?style=flat)](https://github.com/shogun-toolbox/shogun/stargazers) - Machine learning toolbox.
* [xLearn](https://github.com/aksnzhy/xlearn) [![GitHub stars](https://img.shields.io/github/stars/aksnzhy/xlearn?style=flat)](https://github.com/aksnzhy/xlearn/stargazers) - High Performance, Easy-to-use, and Scalable Machine Learning Package.
* [cuML](https://github.com/rapidsai/cuml) [![GitHub stars](https://img.shields.io/github/stars/rapidsai/cuml?style=flat)](https://github.com/rapidsai/cuml/stargazers) - RAPIDS Machine Learning Library. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">
* [modAL](https://github.com/cosmic-cortex/modAL) [![GitHub stars](https://img.shields.io/github/stars/cosmic-cortex/modAL?style=flat)](https://github.com/cosmic-cortex/modAL/stargazers) - Modular active learning framework for Python3. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Sparkit-learn](https://github.com/lensacom/sparkit-learn) [![GitHub stars](https://img.shields.io/github/stars/lensacom/sparkit-learn?style=flat)](https://github.com/lensacom/sparkit-learn/stargazers) - PySpark + scikit-learn = Sparkit-learn. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/spark_big.png" alt="Apache Spark based">
* [mlpack](https://github.com/mlpack/mlpack) [![GitHub stars](https://img.shields.io/github/stars/mlpack/mlpack?style=flat)](https://github.com/mlpack/mlpack/stargazers) - A scalable C++ machine learning library (Python bindings).
* [dlib](https://github.com/davisking/dlib) [![GitHub stars](https://img.shields.io/github/stars/davisking/dlib?style=flat)](https://github.com/davisking/dlib/stargazers) - Toolkit for making real-world machine learning and data analysis applications in C++ (Python bindings).
* [MLxtend](https://github.com/rasbt/mlxtend) [![GitHub stars](https://img.shields.io/github/stars/rasbt/mlxtend?style=flat)](https://github.com/rasbt/mlxtend/stargazers) - Extension and helper modules for Python's data analysis and machine learning libraries. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [hyperlearn](https://github.com/danielhanchen/hyperlearn) [![GitHub stars](https://img.shields.io/github/stars/danielhanchen/hyperlearn?style=flat)](https://github.com/danielhanchen/hyperlearn/stargazers) - 50%+ Faster, 50%+ less RAM usage, GPU support re-written Sklearn, Statsmodels. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [Reproducible Experiment Platform (REP)](https://github.com/yandex/rep) [![GitHub stars](https://img.shields.io/github/stars/yandex/rep?style=flat)](https://github.com/yandex/rep/stargazers) - Machine Learning toolbox for Humans. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-multilearn](https://github.com/scikit-multilearn/scikit-multilearn) [![GitHub stars](https://img.shields.io/github/stars/scikit-multilearn/scikit-multilearn?style=flat)](https://github.com/scikit-multilearn/scikit-multilearn/stargazers) - Multi-label classification for python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [seqlearn](https://github.com/larsmans/seqlearn) [![GitHub stars](https://img.shields.io/github/stars/larsmans/seqlearn?style=flat)](https://github.com/larsmans/seqlearn/stargazers) - Sequence classification toolkit for Python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [pystruct](https://github.com/pystruct/pystruct) [![GitHub stars](https://img.shields.io/github/stars/pystruct/pystruct?style=flat)](https://github.com/pystruct/pystruct/stargazers) - Simple structured learning framework for Python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sklearn-expertsys](https://github.com/tmadl/sklearn-expertsys) [![GitHub stars](https://img.shields.io/github/stars/tmadl/sklearn-expertsys?style=flat)](https://github.com/tmadl/sklearn-expertsys/stargazers) - Highly interpretable classifiers for scikit learn. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [RuleFit](https://github.com/christophM/rulefit) [![GitHub stars](https://img.shields.io/github/stars/christophM/rulefit?style=flat)](https://github.com/christophM/rulefit/stargazers) - Implementation of the rulefit. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [metric-learn](https://github.com/all-umass/metric-learn) [![GitHub stars](https://img.shields.io/github/stars/all-umass/metric-learn?style=flat)](https://github.com/all-umass/metric-learn/stargazers) - Metric learning algorithms in Python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [pyGAM](https://github.com/dswah/pyGAM) [![GitHub stars](https://img.shields.io/github/stars/dswah/pyGAM?style=flat)](https://github.com/dswah/pyGAM/stargazers) - Generalized Additive Models in Python.
* [causalml](https://github.com/uber/causalml) [![GitHub stars](https://img.shields.io/github/stars/uber/causalml?style=flat)](https://github.com/uber/causalml/stargazers) - Uplift modeling and causal inference with machine learning algorithms. <img height="20" src="img/sklearn_big.png" alt="sklearn">

### Gradient Boosting
* [XGBoost](https://github.com/dmlc/xgboost) [![GitHub stars](https://img.shields.io/github/stars/dmlc/xgboost?style=flat)](https://github.com/dmlc/xgboost/stargazers) - Scalable, Portable, and Distributed Gradient Boosting. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">
* [LightGBM](https://github.com/Microsoft/LightGBM) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/LightGBM?style=flat)](https://github.com/Microsoft/LightGBM/stargazers) - A fast, distributed, high-performance gradient boosting. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">
* [CatBoost](https://github.com/catboost/catboost) [![GitHub stars](https://img.shields.io/github/stars/catboost/catboost?style=flat)](https://github.com/catboost/catboost/stargazers) - An open-source gradient boosting on decision trees library. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">
* [ThunderGBM](https://github.com/Xtra-Computing/thundergbm) [![GitHub stars](https://img.shields.io/github/stars/Xtra-Computing/thundergbm?style=flat)](https://github.com/Xtra-Computing/thundergbm/stargazers) - Fast GBDTs and Random Forests on GPUs. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">
* [NGBoost](https://github.com/stanfordmlgroup/ngboost) [![GitHub stars](https://img.shields.io/github/stars/stanfordmlgroup/ngboost?style=flat)](https://github.com/stanfordmlgroup/ngboost/stargazers) - Natural Gradient Boosting for Probabilistic Prediction.
* [TensorFlow Decision Forests](https://github.com/tensorflow/decision-forests) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/decision-forests?style=flat)](https://github.com/tensorflow/decision-forests/stargazers) - A collection of state-of-the-art algorithms for the training, serving and interpretation of Decision Forest models in Keras. <img height="20" src="img/keras_big.png" alt="keras"> <img height="20" src="img/tf_big2.png" alt="TensorFlow">

### Ensemble Methods
* [ML-Ensemble](http://ml-ensemble.com/) - High performance ensemble learning. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Stacking](https://github.com/ikki407/stacking) [![GitHub stars](https://img.shields.io/github/stars/ikki407/stacking?style=flat)](https://github.com/ikki407/stacking/stargazers) - Simple and useful stacking library written in Python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [stacked_generalization](https://github.com/fukatani/stacked_generalization) [![GitHub stars](https://img.shields.io/github/stars/fukatani/stacked_generalization?style=flat)](https://github.com/fukatani/stacked_generalization/stargazers) - Library for machine learning stacking generalization. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [vecstack](https://github.com/vecxoz/vecstack) [![GitHub stars](https://img.shields.io/github/stars/vecxoz/vecstack?style=flat)](https://github.com/vecxoz/vecstack/stargazers) - Python package for stacking (machine learning technique). <img height="20" src="img/sklearn_big.png" alt="sklearn">

### Imbalanced Datasets
* [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn) [![GitHub stars](https://img.shields.io/github/stars/scikit-learn-contrib/imbalanced-learn?style=flat)](https://github.com/scikit-learn-contrib/imbalanced-learn/stargazers) - Module to perform under-sampling and over-sampling with various techniques. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [imbalanced-algorithms](https://github.com/dialnd/imbalanced-algorithms) [![GitHub stars](https://img.shields.io/github/stars/dialnd/imbalanced-algorithms?style=flat)](https://github.com/dialnd/imbalanced-algorithms/stargazers) - Python-based implementations of algorithms for learning on imbalanced data. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/tf_big2.png" alt="sklearn">

### Kernel Methods
* [pyFM](https://github.com/coreylynch/pyFM) [![GitHub stars](https://img.shields.io/github/stars/coreylynch/pyFM?style=flat)](https://github.com/coreylynch/pyFM/stargazers) - Factorization machines in python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [fastFM](https://github.com/ibayer/fastFM) [![GitHub stars](https://img.shields.io/github/stars/ibayer/fastFM?style=flat)](https://github.com/ibayer/fastFM/stargazers) - A library for Factorization Machines. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [tffm](https://github.com/geffy/tffm) [![GitHub stars](https://img.shields.io/github/stars/geffy/tffm?style=flat)](https://github.com/geffy/tffm/stargazers) - TensorFlow implementation of an arbitrary order Factorization Machine. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/tf_big2.png" alt="sklearn">
* [liquidSVM](https://github.com/liquidSVM/liquidSVM) [![GitHub stars](https://img.shields.io/github/stars/liquidSVM/liquidSVM?style=flat)](https://github.com/liquidSVM/liquidSVM/stargazers) - An implementation of SVMs.
* [scikit-rvm](https://github.com/JamesRitchie/scikit-rvm) [![GitHub stars](https://img.shields.io/github/stars/JamesRitchie/scikit-rvm?style=flat)](https://github.com/JamesRitchie/scikit-rvm/stargazers) - Relevance Vector Machine implementation using the scikit-learn API. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [ThunderSVM](https://github.com/Xtra-Computing/thundersvm) [![GitHub stars](https://img.shields.io/github/stars/Xtra-Computing/thundersvm?style=flat)](https://github.com/Xtra-Computing/thundersvm/stargazers) - A fast SVM Library on GPUs and CPUs. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">

## Deep Learning

### PyTorch
* [PyTorch](https://github.com/pytorch/pytorch) [![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch?style=flat)](https://github.com/pytorch/pytorch/stargazers) - Tensors and Dynamic neural networks in Python with strong GPU acceleration. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [pytorch-lightning](https://github.com/Lightning-AI/lightning) [![GitHub stars](https://img.shields.io/github/stars/Lightning-AI/lightning?style=flat)](https://github.com/Lightning-AI/lightning/stargazers) - PyTorch Lightning is just organized PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [ignite](https://github.com/pytorch/ignite) [![GitHub stars](https://img.shields.io/github/stars/pytorch/ignite?style=flat)](https://github.com/pytorch/ignite/stargazers) - High-level library to help with training neural networks in PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [skorch](https://github.com/dnouri/skorch) [![GitHub stars](https://img.shields.io/github/stars/dnouri/skorch?style=flat)](https://github.com/dnouri/skorch/stargazers) - A scikit-learn compatible neural network library that wraps PyTorch. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [Catalyst](https://github.com/catalyst-team/catalyst) [![GitHub stars](https://img.shields.io/github/stars/catalyst-team/catalyst?style=flat)](https://github.com/catalyst-team/catalyst/stargazers) - High-level utils for PyTorch DL & RL research. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [ChemicalX](https://github.com/AstraZeneca/chemicalx) [![GitHub stars](https://img.shields.io/github/stars/AstraZeneca/chemicalx?style=flat)](https://github.com/AstraZeneca/chemicalx/stargazers) - A PyTorch-based deep learning library for drug pair scoring. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">

### TensorFlow
* [TensorFlow](https://github.com/tensorflow/tensorflow) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=flat)](https://github.com/tensorflow/tensorflow/stargazers) - Computation using data flow graphs for scalable machine learning by Google. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [TensorLayer](https://github.com/zsdonghao/tensorlayer) [![GitHub stars](https://img.shields.io/github/stars/zsdonghao/tensorlayer?style=flat)](https://github.com/zsdonghao/tensorlayer/stargazers) - Deep Learning and Reinforcement Learning Library for Researcher and Engineer. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [TFLearn](https://github.com/tflearn/tflearn) [![GitHub stars](https://img.shields.io/github/stars/tflearn/tflearn?style=flat)](https://github.com/tflearn/tflearn/stargazers) - Deep learning library featuring a higher-level API for TensorFlow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Sonnet](https://github.com/deepmind/sonnet) [![GitHub stars](https://img.shields.io/github/stars/deepmind/sonnet?style=flat)](https://github.com/deepmind/sonnet/stargazers) - TensorFlow-based neural network library. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [tensorpack](https://github.com/ppwwyyxx/tensorpack) [![GitHub stars](https://img.shields.io/github/stars/ppwwyyxx/tensorpack?style=flat)](https://github.com/ppwwyyxx/tensorpack/stargazers) - A Neural Net Training Interface on TensorFlow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [tfdeploy](https://github.com/riga/tfdeploy) [![GitHub stars](https://img.shields.io/github/stars/riga/tfdeploy?style=flat)](https://github.com/riga/tfdeploy/stargazers) - Deploy TensorFlow graphs for fast evaluation and export to TensorFlow-less environments running numpy. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [tensorflow-upstream](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream) [![GitHub stars](https://img.shields.io/github/stars/ROCmSoftwarePlatform/tensorflow-upstream?style=flat)](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/stargazers) - TensorFlow ROCm port. <img height="20" src="img/tf_big2.png" alt="sklearn"> <img height="20" src="img/amd_big.png" alt="Possible to run on AMD GPU">
* [TensorFlow Fold](https://github.com/tensorflow/fold) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/fold?style=flat)](https://github.com/tensorflow/fold/stargazers) - Deep learning with dynamic computation graphs in TensorFlow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [TensorLight](https://github.com/bsautermeister/tensorlight) [![GitHub stars](https://img.shields.io/github/stars/bsautermeister/tensorlight?style=flat)](https://github.com/bsautermeister/tensorlight/stargazers) - A high-level framework for TensorFlow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Mesh TensorFlow](https://github.com/tensorflow/mesh) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/mesh?style=flat)](https://github.com/tensorflow/mesh/stargazers) - Model Parallelism Made Easier. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Ludwig](https://github.com/uber/ludwig) [![GitHub stars](https://img.shields.io/github/stars/uber/ludwig?style=flat)](https://github.com/uber/ludwig/stargazers) - A toolbox that allows one to train and test deep learning models without the need to write code. <img height="20" src="img/tf_big2.png" alt="sklearn">

### JAX
* [JAX](https://github.com/google/jax) [![GitHub stars](https://img.shields.io/github/stars/google/jax?style=flat)](https://github.com/google/jax/stargazers) - Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more.
* [FLAX](https://github.com/google/flax) [![GitHub stars](https://img.shields.io/github/stars/google/flax?style=flat)](https://github.com/google/flax/stargazers) - A neural network library for JAX that is designed for flexibility.
* [Optax](https://github.com/google-deepmind/optax) [![GitHub stars](https://img.shields.io/github/stars/google-deepmind/optax?style=flat)](https://github.com/google-deepmind/optax/stargazers) - A gradient processing and optimization library for JAX.

### Keras
* [Keras](https://keras.io) - A high-level neural networks API running on top of TensorFlow.  <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [keras-contrib](https://github.com/keras-team/keras-contrib) [![GitHub stars](https://img.shields.io/github/stars/keras-team/keras-contrib?style=flat)](https://github.com/keras-team/keras-contrib/stargazers) - Keras community contributions. <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [Hyperas](https://github.com/maxpumperla/hyperas) [![GitHub stars](https://img.shields.io/github/stars/maxpumperla/hyperas?style=flat)](https://github.com/maxpumperla/hyperas/stargazers) - Keras + Hyperopt: A straightforward wrapper for a convenient hyperparameter. <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [Elephas](https://github.com/maxpumperla/elephas) [![GitHub stars](https://img.shields.io/github/stars/maxpumperla/elephas?style=flat)](https://github.com/maxpumperla/elephas/stargazers) - Distributed Deep learning with Keras & Spark. <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [qkeras](https://github.com/google/qkeras) [![GitHub stars](https://img.shields.io/github/stars/google/qkeras?style=flat)](https://github.com/google/qkeras/stargazers) - A quantization deep learning library. <img height="20" src="img/keras_big.png" alt="Keras compatible">

### Others
* [transformers](https://github.com/huggingface/transformers) [![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=flat)](https://github.com/huggingface/transformers/stargazers) - State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible"> <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Tangent](https://github.com/google/tangent) [![GitHub stars](https://img.shields.io/github/stars/google/tangent?style=flat)](https://github.com/google/tangent/stargazers) - Source-to-Source Debuggable Derivatives in Pure Python.
* [autograd](https://github.com/HIPS/autograd) [![GitHub stars](https://img.shields.io/github/stars/HIPS/autograd?style=flat)](https://github.com/HIPS/autograd/stargazers) - Efficiently computes derivatives of numpy code.
* [Caffe](https://github.com/BVLC/caffe) [![GitHub stars](https://img.shields.io/github/stars/BVLC/caffe?style=flat)](https://github.com/BVLC/caffe/stargazers) - A fast open framework for deep learning.
* [nnabla](https://github.com/sony/nnabla) [![GitHub stars](https://img.shields.io/github/stars/sony/nnabla?style=flat)](https://github.com/sony/nnabla/stargazers) - Neural Network Libraries by Sony.

## Automated Machine Learning
* [auto-sklearn](https://github.com/automl/auto-sklearn) [![GitHub stars](https://img.shields.io/github/stars/automl/auto-sklearn?style=flat)](https://github.com/automl/auto-sklearn/stargazers) - An AutoML toolkit and a drop-in replacement for a scikit-learn estimator. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Auto-PyTorch](https://github.com/automl/Auto-PyTorch) [![GitHub stars](https://img.shields.io/github/stars/automl/Auto-PyTorch?style=flat)](https://github.com/automl/Auto-PyTorch/stargazers) - Automatic architecture search and hyperparameter optimization for PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [AutoKeras](https://github.com/keras-team/autokeras) [![GitHub stars](https://img.shields.io/github/stars/keras-team/autokeras?style=flat)](https://github.com/keras-team/autokeras/stargazers) - AutoML library for deep learning. <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [AutoGluon](https://github.com/awslabs/autogluon) [![GitHub stars](https://img.shields.io/github/stars/awslabs/autogluon?style=flat)](https://github.com/awslabs/autogluon/stargazers) - AutoML for Image, Text, Tabular, Time-Series, and MultiModal Data.
* [TPOT](https://github.com/rhiever/tpot) [![GitHub stars](https://img.shields.io/github/stars/rhiever/tpot?style=flat)](https://github.com/rhiever/tpot/stargazers) - AutoML tool that optimizes machine learning pipelines using genetic programming. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [MLBox](https://github.com/AxeldeRomblay/MLBox) [![GitHub stars](https://img.shields.io/github/stars/AxeldeRomblay/MLBox?style=flat)](https://github.com/AxeldeRomblay/MLBox/stargazers) - A powerful Automated Machine Learning python library.

## Natural Language Processing
* [torchtext](https://github.com/pytorch/text) [![GitHub stars](https://img.shields.io/github/stars/pytorch/text?style=flat)](https://github.com/pytorch/text/stargazers) - Data loaders and abstractions for text and NLP. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [KerasNLP](https://github.com/keras-team/keras-nlp) [![GitHub stars](https://img.shields.io/github/stars/keras-team/keras-nlp?style=flat)](https://github.com/keras-team/keras-nlp/stargazers) - Modular Natural Language Processing workflows with Keras. <img height="20" src="img/keras_big.png" alt="Keras based/compatible">
* [spaCy](https://spacy.io/) - Industrial-Strength Natural Language Processing.
* [NLTK](https://github.com/nltk/nltk) [![GitHub stars](https://img.shields.io/github/stars/nltk/nltk?style=flat)](https://github.com/nltk/nltk/stargazers) -  Modules, data sets, and tutorials supporting research and development in Natural Language Processing.
* [CLTK](https://github.com/cltk/cltk) [![GitHub stars](https://img.shields.io/github/stars/cltk/cltk?style=flat)](https://github.com/cltk/cltk/stargazers) - The Classical Language Toolkik.
* [gensim](https://radimrehurek.com/gensim/) - Topic Modelling for Humans.
* [pyMorfologik](https://github.com/dmirecki/pyMorfologik) [![GitHub stars](https://img.shields.io/github/stars/dmirecki/pyMorfologik?style=flat)](https://github.com/dmirecki/pyMorfologik/stargazers) - Python binding for <a href="https://github.com/morfologik/morfologik-stemming">Morfologik</a>.
* [skift](https://github.com/shaypal5/skift) [![GitHub stars](https://img.shields.io/github/stars/shaypal5/skift?style=flat)](https://github.com/shaypal5/skift/stargazers) - Scikit-learn wrappers for Python fastText. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Phonemizer](https://github.com/bootphon/phonemizer) [![GitHub stars](https://img.shields.io/github/stars/bootphon/phonemizer?style=flat)](https://github.com/bootphon/phonemizer/stargazers) - Simple text-to-phonemes converter for multiple languages.
* [flair](https://github.com/zalandoresearch/flair) [![GitHub stars](https://img.shields.io/github/stars/zalandoresearch/flair?style=flat)](https://github.com/zalandoresearch/flair/stargazers) - Very simple framework for state-of-the-art NLP.

## Computer Audition
* [torchaudio](https://github.com/pytorch/audio) [![GitHub stars](https://img.shields.io/github/stars/pytorch/audio?style=flat)](https://github.com/pytorch/audio/stargazers) - An audio library for PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [librosa](https://github.com/librosa/librosa) [![GitHub stars](https://img.shields.io/github/stars/librosa/librosa?style=flat)](https://github.com/librosa/librosa/stargazers) - Python library for audio and music analysis.
* [Yaafe](https://github.com/Yaafe/Yaafe) [![GitHub stars](https://img.shields.io/github/stars/Yaafe/Yaafe?style=flat)](https://github.com/Yaafe/Yaafe/stargazers) - Audio features extraction.
* [aubio](https://github.com/aubio/aubio) [![GitHub stars](https://img.shields.io/github/stars/aubio/aubio?style=flat)](https://github.com/aubio/aubio/stargazers) - A library for audio and music analysis.
* [Essentia](https://github.com/MTG/essentia) [![GitHub stars](https://img.shields.io/github/stars/MTG/essentia?style=flat)](https://github.com/MTG/essentia/stargazers) - Library for audio and music analysis, description, and synthesis.
* [LibXtract](https://github.com/jamiebullock/LibXtract) [![GitHub stars](https://img.shields.io/github/stars/jamiebullock/LibXtract?style=flat)](https://github.com/jamiebullock/LibXtract/stargazers) - A simple, portable, lightweight library of audio feature extraction functions.
* [Marsyas](https://github.com/marsyas/marsyas) [![GitHub stars](https://img.shields.io/github/stars/marsyas/marsyas?style=flat)](https://github.com/marsyas/marsyas/stargazers) - Music Analysis, Retrieval, and Synthesis for Audio Signals.
* [muda](https://github.com/bmcfee/muda) [![GitHub stars](https://img.shields.io/github/stars/bmcfee/muda?style=flat)](https://github.com/bmcfee/muda/stargazers) - A library for augmenting annotated audio data.
* [madmom](https://github.com/CPJKU/madmom) [![GitHub stars](https://img.shields.io/github/stars/CPJKU/madmom?style=flat)](https://github.com/CPJKU/madmom/stargazers) - Python audio and music signal processing library.

## Computer Vision
* [torchvision](https://github.com/pytorch/vision) [![GitHub stars](https://img.shields.io/github/stars/pytorch/vision?style=flat)](https://github.com/pytorch/vision/stargazers) - Datasets, Transforms, and Models specific to Computer Vision. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [PyTorch3D](https://github.com/facebookresearch/pytorch3d) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/pytorch3d?style=flat)](https://github.com/facebookresearch/pytorch3d/stargazers) - PyTorch3D is FAIR's library of reusable components for deep learning with 3D data. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [KerasCV](https://github.com/keras-team/keras-cv) [![GitHub stars](https://img.shields.io/github/stars/keras-team/keras-cv?style=flat)](https://github.com/keras-team/keras-cv/stargazers) - Industry-strength Computer Vision workflows with Keras. <img height="20" src="img/keras_big.png" alt="MXNet based">
* [OpenCV](https://github.com/opencv/opencv) [![GitHub stars](https://img.shields.io/github/stars/opencv/opencv?style=flat)](https://github.com/opencv/opencv/stargazers) - Open Source Computer Vision Library.
* [Decord](https://github.com/dmlc/decord) [![GitHub stars](https://img.shields.io/github/stars/dmlc/decord?style=flat)](https://github.com/dmlc/decord/stargazers) - An efficient video loader for deep learning with smart shuffling that's super easy to digest.
* [MMEngine](https://github.com/open-mmlab/mmengine) [![GitHub stars](https://img.shields.io/github/stars/open-mmlab/mmengine?style=flat)](https://github.com/open-mmlab/mmengine/stargazers) - OpenMMLab Foundational Library for Training Deep Learning Models. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [scikit-image](https://github.com/scikit-image/scikit-image) [![GitHub stars](https://img.shields.io/github/stars/scikit-image/scikit-image?style=flat)](https://github.com/scikit-image/scikit-image/stargazers) - Image Processing SciKit (Toolbox for SciPy).
* [imgaug](https://github.com/aleju/imgaug) [![GitHub stars](https://img.shields.io/github/stars/aleju/imgaug?style=flat)](https://github.com/aleju/imgaug/stargazers) - Image augmentation for machine learning experiments.
* [imgaug_extension](https://github.com/cadenai/imgaug_extension) [![GitHub stars](https://img.shields.io/github/stars/cadenai/imgaug_extension?style=flat)](https://github.com/cadenai/imgaug_extension/stargazers) - Additional augmentations for imgaug.
* [Augmentor](https://github.com/mdbloice/Augmentor) [![GitHub stars](https://img.shields.io/github/stars/mdbloice/Augmentor?style=flat)](https://github.com/mdbloice/Augmentor/stargazers) - Image augmentation library in Python for machine learning.
* [albumentations](https://github.com/albu/albumentations) [![GitHub stars](https://img.shields.io/github/stars/albu/albumentations?style=flat)](https://github.com/albu/albumentations/stargazers) - Fast image augmentation library and easy-to-use wrapper around other libraries.
* [LAVIS](https://github.com/salesforce/LAVIS) [![GitHub stars](https://img.shields.io/github/stars/salesforce/LAVIS?style=flat)](https://github.com/salesforce/LAVIS/stargazers) - A One-stop Library for Language-Vision Intelligence.

## Time Series
* [sktime](https://github.com/alan-turing-institute/sktime) [![GitHub stars](https://img.shields.io/github/stars/alan-turing-institute/sktime?style=flat)](https://github.com/alan-turing-institute/sktime/stargazers) - A unified framework for machine learning with time series. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [skforecast](https://github.com/JoaquinAmatRodrigo/skforecast) [![GitHub stars](https://img.shields.io/github/stars/JoaquinAmatRodrigo/skforecast?style=flat)](https://github.com/JoaquinAmatRodrigo/skforecast/stargazers) - Time series forecasting with machine learning models
* [darts](https://github.com/unit8co/darts) [![GitHub stars](https://img.shields.io/github/stars/unit8co/darts?style=flat)](https://github.com/unit8co/darts/stargazers) - A python library for easy manipulation and forecasting of time series.
* [statsforecast](https://github.com/Nixtla/statsforecast) [![GitHub stars](https://img.shields.io/github/stars/Nixtla/statsforecast?style=flat)](https://github.com/Nixtla/statsforecast/stargazers) - Lightning fast forecasting with statistical and econometric models.
* [mlforecast](https://github.com/Nixtla/mlforecast) [![GitHub stars](https://img.shields.io/github/stars/Nixtla/mlforecast?style=flat)](https://github.com/Nixtla/mlforecast/stargazers) - Scalable machine learning-based time series forecasting.
* [neuralforecast](https://github.com/Nixtla/neuralforecast) [![GitHub stars](https://img.shields.io/github/stars/Nixtla/neuralforecast?style=flat)](https://github.com/Nixtla/neuralforecast/stargazers) - Scalable machine learning-based time series forecasting.
* [tslearn](https://github.com/rtavenar/tslearn) [![GitHub stars](https://img.shields.io/github/stars/rtavenar/tslearn?style=flat)](https://github.com/rtavenar/tslearn/stargazers) - Machine learning toolkit dedicated to time-series data. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [tick](https://github.com/X-DataInitiative/tick) [![GitHub stars](https://img.shields.io/github/stars/X-DataInitiative/tick?style=flat)](https://github.com/X-DataInitiative/tick/stargazers) - Module for statistical learning, with a particular emphasis on time-dependent modeling.  <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [greykite](https://github.com/linkedin/greykite) [![GitHub stars](https://img.shields.io/github/stars/linkedin/greykite?style=flat)](https://github.com/linkedin/greykite/stargazers) - A flexible, intuitive, and fast forecasting library next.
* [Prophet](https://github.com/facebook/prophet) [![GitHub stars](https://img.shields.io/github/stars/facebook/prophet?style=flat)](https://github.com/facebook/prophet/stargazers) - Automatic Forecasting Procedure.
* [PyFlux](https://github.com/RJT1990/pyflux) [![GitHub stars](https://img.shields.io/github/stars/RJT1990/pyflux?style=flat)](https://github.com/RJT1990/pyflux/stargazers) - Open source time series library for Python.
* [bayesloop](https://github.com/christophmark/bayesloop) [![GitHub stars](https://img.shields.io/github/stars/christophmark/bayesloop?style=flat)](https://github.com/christophmark/bayesloop/stargazers) - Probabilistic programming framework that facilitates objective model selection for time-varying parameter models.
* [luminol](https://github.com/linkedin/luminol) [![GitHub stars](https://img.shields.io/github/stars/linkedin/luminol?style=flat)](https://github.com/linkedin/luminol/stargazers) - Anomaly Detection and Correlation library.
* [dateutil](https://dateutil.readthedocs.io/en/stable/) - Powerful extensions to the standard datetime module
* [maya](https://github.com/timofurrer/maya) [![GitHub stars](https://img.shields.io/github/stars/timofurrer/maya?style=flat)](https://github.com/timofurrer/maya/stargazers) - makes it very easy to parse a string and for changing timezones
* [Chaos Genius](https://github.com/chaos-genius/chaos_genius) [![GitHub stars](https://img.shields.io/github/stars/chaos-genius/chaos_genius?style=flat)](https://github.com/chaos-genius/chaos_genius/stargazers) - ML powered analytics engine for outlier/anomaly detection and root cause analysis

## Reinforcement Learning
* [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) [![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium?style=flat)](https://github.com/Farama-Foundation/Gymnasium/stargazers) - An API standard for single-agent reinforcement learning environments, with popular reference environments and related utilities (formerly [Gym](https://github.com/openai/gym) [![GitHub stars](https://img.shields.io/github/stars/openai/gym?style=flat)](https://github.com/openai/gym/stargazers)).
* [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) [![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/PettingZoo?style=flat)](https://github.com/Farama-Foundation/PettingZoo/stargazers) - An API standard for multi-agent reinforcement learning environments, with popular reference environments and related utilities.
* [MAgent2](https://github.com/Farama-Foundation/MAgent2) [![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/MAgent2?style=flat)](https://github.com/Farama-Foundation/MAgent2/stargazers) - An engine for high performance multi-agent environments with very large numbers of agents, along with a set of reference environments.
* [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3) [![GitHub stars](https://img.shields.io/github/stars/DLR-RM/stable-baselines3?style=flat)](https://github.com/DLR-RM/stable-baselines3/stargazers) - A set of improved implementations of reinforcement learning algorithms based on OpenAI Baselines.
* [Shimmy](https://github.com/Farama-Foundation/Shimmy) [![GitHub stars](https://img.shields.io/github/stars/Farama-Foundation/Shimmy?style=flat)](https://github.com/Farama-Foundation/Shimmy/stargazers) - An API conversion tool for popular external reinforcement learning environments.
* [EnvPool](https://github.com/sail-sg/envpool) [![GitHub stars](https://img.shields.io/github/stars/sail-sg/envpool?style=flat)](https://github.com/sail-sg/envpool/stargazers) - C++-based high-performance parallel environment execution engine (vectorized env) for general RL environments.
* [RLlib](https://ray.readthedocs.io/en/latest/rllib.html) - Scalable Reinforcement Learning.
* [Tianshou](https://github.com/thu-ml/tianshou/#comprehensive-functionality) - An elegant PyTorch deep reinforcement learning library. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [Acme](https://github.com/google-deepmind/acme) [![GitHub stars](https://img.shields.io/github/stars/google-deepmind/acme?style=flat)](https://github.com/google-deepmind/acme/stargazers) - A library of reinforcement learning components and agents.
* [Catalyst-RL](https://github.com/catalyst-team/catalyst-rl) [![GitHub stars](https://img.shields.io/github/stars/catalyst-team/catalyst-rl?style=flat)](https://github.com/catalyst-team/catalyst-rl/stargazers) - PyTorch framework for RL research. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [d3rlpy](https://github.com/takuseno/d3rlpy) [![GitHub stars](https://img.shields.io/github/stars/takuseno/d3rlpy?style=flat)](https://github.com/takuseno/d3rlpy/stargazers) - An offline deep reinforcement learning library.
* [DI-engine](https://github.com/opendilab/DI-engine) [![GitHub stars](https://img.shields.io/github/stars/opendilab/DI-engine?style=flat)](https://github.com/opendilab/DI-engine/stargazers) - OpenDILab Decision AI Engine. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [TF-Agents](https://github.com/tensorflow/agents) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/agents?style=flat)](https://github.com/tensorflow/agents/stargazers) - A library for Reinforcement Learning in TensorFlow. <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [TensorForce](https://github.com/reinforceio/tensorforce) [![GitHub stars](https://img.shields.io/github/stars/reinforceio/tensorforce?style=flat)](https://github.com/reinforceio/tensorforce/stargazers) - A TensorFlow library for applied reinforcement learning. <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [TRFL](https://github.com/deepmind/trfl) [![GitHub stars](https://img.shields.io/github/stars/deepmind/trfl?style=flat)](https://github.com/deepmind/trfl/stargazers) - TensorFlow Reinforcement Learning. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Dopamine](https://github.com/google/dopamine) [![GitHub stars](https://img.shields.io/github/stars/google/dopamine?style=flat)](https://github.com/google/dopamine/stargazers) - A research framework for fast prototyping of reinforcement learning algorithms.
* [keras-rl](https://github.com/keras-rl/keras-rl) [![GitHub stars](https://img.shields.io/github/stars/keras-rl/keras-rl?style=flat)](https://github.com/keras-rl/keras-rl/stargazers) - Deep Reinforcement Learning for Keras. <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [garage](https://github.com/rlworkgroup/garage) [![GitHub stars](https://img.shields.io/github/stars/rlworkgroup/garage?style=flat)](https://github.com/rlworkgroup/garage/stargazers) - A toolkit for reproducible reinforcement learning research.
* [Horizon](https://github.com/facebookresearch/Horizon) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/Horizon?style=flat)](https://github.com/facebookresearch/Horizon/stargazers) - A platform for Applied Reinforcement Learning.
* [rlpyt](https://github.com/astooke/rlpyt) [![GitHub stars](https://img.shields.io/github/stars/astooke/rlpyt?style=flat)](https://github.com/astooke/rlpyt/stargazers) - Reinforcement Learning in PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [cleanrl](https://github.com/vwxyzjn/cleanrl) [![GitHub stars](https://img.shields.io/github/stars/vwxyzjn/cleanrl?style=flat)](https://github.com/vwxyzjn/cleanrl/stargazers) - High-quality single file implementation of Deep Reinforcement Learning algorithms with research-friendly features (PPO, DQN, C51, DDPG, TD3, SAC, PPG).
* [Machin](https://github.com/iffiX/machin) [![GitHub stars](https://img.shields.io/github/stars/iffiX/machin?style=flat)](https://github.com/iffiX/machin/stargazers) -  A reinforcement library designed for pytorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [SKRL](https://github.com/Toni-SM/skrl) [![GitHub stars](https://img.shields.io/github/stars/Toni-SM/skrl?style=flat)](https://github.com/Toni-SM/skrl/stargazers) - Modular reinforcement learning library (on PyTorch and JAX) with support for NVIDIA Isaac Gym, Isaac Orbit and Omniverse Isaac Gym. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [Imitation](https://github.com/HumanCompatibleAI/imitation) [![GitHub stars](https://img.shields.io/github/stars/HumanCompatibleAI/imitation?style=flat)](https://github.com/HumanCompatibleAI/imitation/stargazers) - Clean PyTorch implementations of imitation and reward learning algorithms. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">

## Graph Machine Learning
* [pytorch_geometric](https://github.com/rusty1s/pytorch_geometric) [![GitHub stars](https://img.shields.io/github/stars/rusty1s/pytorch_geometric?style=flat)](https://github.com/rusty1s/pytorch_geometric/stargazers) - Geometric Deep Learning Extension Library for PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [pytorch_geometric_temporal](https://github.com/benedekrozemberczki/pytorch_geometric_temporal) [![GitHub stars](https://img.shields.io/github/stars/benedekrozemberczki/pytorch_geometric_temporal?style=flat)](https://github.com/benedekrozemberczki/pytorch_geometric_temporal/stargazers) - Temporal Extension Library for PyTorch Geometric. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [PyTorch Geometric Signed Directed](https://github.com/SherylHYX/pytorch_geometric_signed_directed) [![GitHub stars](https://img.shields.io/github/stars/SherylHYX/pytorch_geometric_signed_directed?style=flat)](https://github.com/SherylHYX/pytorch_geometric_signed_directed/stargazers) -  A signed/directed graph neural network extension library for PyTorch Geometric. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [dgl](https://github.com/dmlc/dgl) [![GitHub stars](https://img.shields.io/github/stars/dmlc/dgl?style=flat)](https://github.com/dmlc/dgl/stargazers) - Python package built to ease deep learning on graph, on top of existing DL frameworks. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible"> <img height="20" src="img/tf_big2.png" alt="TensorFlow"> <img height="20" src="img/mxnet_big.png" alt="MXNet based">
* [GRAPE](https://github.com/AnacletoLAB/grape/tree/main) [![GitHub stars](https://img.shields.io/github/stars/AnacletoLAB/grape/tree/main?style=flat)](https://github.com/AnacletoLAB/grape/tree/main/stargazers) - GRAPE is a Rust/Python Graph Representation Learning library for Predictions and Evaluations
* [Spektral](https://github.com/danielegrattarola/spektral) [![GitHub stars](https://img.shields.io/github/stars/danielegrattarola/spektral?style=flat)](https://github.com/danielegrattarola/spektral/stargazers) - Deep learning on graphs. <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [StellarGraph](https://github.com/stellargraph/stellargraph) [![GitHub stars](https://img.shields.io/github/stars/stellargraph/stellargraph?style=flat)](https://github.com/stellargraph/stellargraph/stargazers) - Machine Learning on Graphs. <img height="20" src="img/tf_big2.png" alt="TensorFlow">  <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [Graph Nets](https://github.com/google-deepmind/graph_nets) [![GitHub stars](https://img.shields.io/github/stars/google-deepmind/graph_nets?style=flat)](https://github.com/google-deepmind/graph_nets/stargazers) - Build Graph Nets in Tensorflow. <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [TensorFlow GNN](https://github.com/tensorflow/gnn) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/gnn?style=flat)](https://github.com/tensorflow/gnn/stargazers) - A library to build Graph Neural Networks on the TensorFlow platform. <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [Auto Graph Learning](https://github.com/THUMNLab/AutoGL) [![GitHub stars](https://img.shields.io/github/stars/THUMNLab/AutoGL?style=flat)](https://github.com/THUMNLab/AutoGL/stargazers) -An autoML framework & toolkit for machine learning on graphs.
* [PyTorch-BigGraph](https://github.com/facebookresearch/PyTorch-BigGraph) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/PyTorch-BigGraph?style=flat)](https://github.com/facebookresearch/PyTorch-BigGraph/stargazers) - Generate embeddings from large-scale graph-structured data. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [Auto Graph Learning](https://github.com/THUMNLab/AutoGL) [![GitHub stars](https://img.shields.io/github/stars/THUMNLab/AutoGL?style=flat)](https://github.com/THUMNLab/AutoGL/stargazers) - An autoML framework & toolkit for machine learning on graphs.
* [Karate Club](https://github.com/benedekrozemberczki/karateclub) [![GitHub stars](https://img.shields.io/github/stars/benedekrozemberczki/karateclub?style=flat)](https://github.com/benedekrozemberczki/karateclub/stargazers) - An unsupervised machine learning library for graph-structured data.
* [Little Ball of Fur](https://github.com/benedekrozemberczki/littleballoffur) [![GitHub stars](https://img.shields.io/github/stars/benedekrozemberczki/littleballoffur?style=flat)](https://github.com/benedekrozemberczki/littleballoffur/stargazers) - A library for sampling graph structured data.
* [GreatX](https://github.com/EdisonLeeeee/GreatX) [![GitHub stars](https://img.shields.io/github/stars/EdisonLeeeee/GreatX?style=flat)](https://github.com/EdisonLeeeee/GreatX/stargazers) - A graph reliability toolbox based on PyTorch and PyTorch Geometric (PyG). <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [Jraph](https://github.com/google-deepmind/jraph) [![GitHub stars](https://img.shields.io/github/stars/google-deepmind/jraph?style=flat)](https://github.com/google-deepmind/jraph/stargazers) - A Graph Neural Network Library in Jax.
* [TRL](https://github.com/huggingface/trl) [![GitHub stars](https://img.shields.io/github/stars/huggingface/trl?style=flat)](https://github.com/huggingface/trl/stargazers) - Train transformer language models with reinforcement learning.
* [Cleora](https://github.com/BaseModelAI/cleora) [![GitHub stars](https://img.shields.io/github/stars/BaseModelAI/cleora?style=flat)](https://github.com/BaseModelAI/cleora/stargazers) - The Graph Embedding Engine.

## Graph Manipulation
* [Networkx](https://github.com/networkx/networkx) [![GitHub stars](https://img.shields.io/github/stars/networkx/networkx?style=flat)](https://github.com/networkx/networkx/stargazers) - Network Analysis in Python.
* [Rustworkx](https://github.com/Qiskit/rustworkx) [![GitHub stars](https://img.shields.io/github/stars/Qiskit/rustworkx?style=flat)](https://github.com/Qiskit/rustworkx/stargazers) - A high performance Python graph library implemented in Rust.
* [graph-tool](https://graph-tool.skewed.de/) - an efficient Python module for manipulation and statistical analysis of graphs (a.k.a. networks).
* [igraph](https://github.com/igraph/python-igraph) [![GitHub stars](https://img.shields.io/github/stars/igraph/python-igraph?style=flat)](https://github.com/igraph/python-igraph/stargazers) - Python interface for igraph.

## Learning-to-Rank & Recommender Systems
* [LightFM](https://github.com/lyst/lightfm) [![GitHub stars](https://img.shields.io/github/stars/lyst/lightfm?style=flat)](https://github.com/lyst/lightfm/stargazers) - A Python implementation of LightFM, a hybrid recommendation algorithm.
* [Spotlight](https://maciejkula.github.io/spotlight/) - Deep recommender models using PyTorch.
* [Surprise](https://github.com/NicolasHug/Surprise) [![GitHub stars](https://img.shields.io/github/stars/NicolasHug/Surprise?style=flat)](https://github.com/NicolasHug/Surprise/stargazers) - A Python scikit for building and analyzing recommender systems.
* [RecBole](https://github.com/RUCAIBox/RecBole) [![GitHub stars](https://img.shields.io/github/stars/RUCAIBox/RecBole?style=flat)](https://github.com/RUCAIBox/RecBole/stargazers) - A unified, comprehensive and efficient recommendation library. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [allRank](https://github.com/allegro/allRank) [![GitHub stars](https://img.shields.io/github/stars/allegro/allRank?style=flat)](https://github.com/allegro/allRank/stargazers) - allRank is a framework for training learning-to-rank neural models based on PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [TensorFlow Recommenders](https://github.com/tensorflow/recommenders) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/recommenders?style=flat)](https://github.com/tensorflow/recommenders/stargazers) - A library for building recommender system models using TensorFlow. <img height="20" src="img/tf_big2.png" alt="TensorFlow"> <img height="20" src="img/keras_big.png" alt="Keras compatible">
* [TensorFlow Ranking](https://github.com/tensorflow/ranking) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/ranking?style=flat)](https://github.com/tensorflow/ranking/stargazers) - Learning to Rank in TensorFlow. <img height="20" src="img/tf_big2.png" alt="TensorFlow"> 

## Probabilistic Graphical Models
* [pomegranate](https://github.com/jmschrei/pomegranate) [![GitHub stars](https://img.shields.io/github/stars/jmschrei/pomegranate?style=flat)](https://github.com/jmschrei/pomegranate/stargazers) - Probabilistic and graphical models for Python. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [pgmpy](https://github.com/pgmpy/pgmpy) [![GitHub stars](https://img.shields.io/github/stars/pgmpy/pgmpy?style=flat)](https://github.com/pgmpy/pgmpy/stargazers) - A python library for working with Probabilistic Graphical Models.
* [pyAgrum](https://agrum.gitlab.io/) - A GRaphical Universal Modeler.

## Probabilistic Methods
* [pyro](https://github.com/uber/pyro) [![GitHub stars](https://img.shields.io/github/stars/uber/pyro?style=flat)](https://github.com/uber/pyro/stargazers) - A flexible, scalable deep probabilistic programming library built on PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [PyMC](https://github.com/pymc-devs/pymc) [![GitHub stars](https://img.shields.io/github/stars/pymc-devs/pymc?style=flat)](https://github.com/pymc-devs/pymc/stargazers) - Bayesian Stochastic Modelling in Python.
* [ZhuSuan](https://zhusuan.readthedocs.io/en/latest/) - Bayesian Deep Learning. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [GPflow](https://gpflow.readthedocs.io/en/latest/?badge=latest) - Gaussian processes in TensorFlow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [InferPy](https://github.com/PGM-Lab/InferPy) [![GitHub stars](https://img.shields.io/github/stars/PGM-Lab/InferPy?style=flat)](https://github.com/PGM-Lab/InferPy/stargazers) - Deep Probabilistic Modelling Made Easy.  <img height="20" src="img/tf_big2.png" alt="sklearn">
* [PyStan](https://github.com/stan-dev/pystan) [![GitHub stars](https://img.shields.io/github/stars/stan-dev/pystan?style=flat)](https://github.com/stan-dev/pystan/stargazers) - Bayesian inference using the No-U-Turn sampler (Python interface).
* [sklearn-bayes](https://github.com/AmazaspShumik/sklearn-bayes) [![GitHub stars](https://img.shields.io/github/stars/AmazaspShumik/sklearn-bayes?style=flat)](https://github.com/AmazaspShumik/sklearn-bayes/stargazers) - Python package for Bayesian Machine Learning with scikit-learn API. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [skpro](https://github.com/alan-turing-institute/skpro) [![GitHub stars](https://img.shields.io/github/stars/alan-turing-institute/skpro?style=flat)](https://github.com/alan-turing-institute/skpro/stargazers) - Supervised domain-agnostic prediction framework for probabilistic modelling by [The Alan Turing Institute](https://www.turing.ac.uk/). <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [PyVarInf](https://github.com/ctallec/pyvarinf) [![GitHub stars](https://img.shields.io/github/stars/ctallec/pyvarinf?style=flat)](https://github.com/ctallec/pyvarinf/stargazers) - Bayesian Deep Learning methods with Variational Inference for PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [emcee](https://github.com/dfm/emcee) [![GitHub stars](https://img.shields.io/github/stars/dfm/emcee?style=flat)](https://github.com/dfm/emcee/stargazers) - The Python ensemble sampling toolkit for affine-invariant MCMC.
* [hsmmlearn](https://github.com/jvkersch/hsmmlearn) [![GitHub stars](https://img.shields.io/github/stars/jvkersch/hsmmlearn?style=flat)](https://github.com/jvkersch/hsmmlearn/stargazers) - A library for hidden semi-Markov models with explicit durations.
* [pyhsmm](https://github.com/mattjj/pyhsmm) [![GitHub stars](https://img.shields.io/github/stars/mattjj/pyhsmm?style=flat)](https://github.com/mattjj/pyhsmm/stargazers) - Bayesian inference in HSMMs and HMMs.
* [GPyTorch](https://github.com/cornellius-gp/gpytorch) [![GitHub stars](https://img.shields.io/github/stars/cornellius-gp/gpytorch?style=flat)](https://github.com/cornellius-gp/gpytorch/stargazers) - A highly efficient and modular implementation of Gaussian Processes in PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [sklearn-crfsuite](https://github.com/TeamHG-Memex/sklearn-crfsuite) [![GitHub stars](https://img.shields.io/github/stars/TeamHG-Memex/sklearn-crfsuite?style=flat)](https://github.com/TeamHG-Memex/sklearn-crfsuite/stargazers) - A scikit-learn-inspired API for CRFsuite. <img height="20" src="img/sklearn_big.png" alt="sklearn">

## Model Explanation
* [dalex](https://github.com/ModelOriented/DALEX) [![GitHub stars](https://img.shields.io/github/stars/ModelOriented/DALEX?style=flat)](https://github.com/ModelOriented/DALEX/stargazers) - moDel Agnostic Language for Exploration and explanation. <img height="20" src="img/sklearn_big.png" alt="sklearn"><img height="20" src="img/R_big.png" alt="R inspired/ported lib">
* [Shapley](https://github.com/benedekrozemberczki/shapley) [![GitHub stars](https://img.shields.io/github/stars/benedekrozemberczki/shapley?style=flat)](https://github.com/benedekrozemberczki/shapley/stargazers) - A data-driven framework to quantify the value of classifiers in a machine learning ensemble.
* [Alibi](https://github.com/SeldonIO/alibi) [![GitHub stars](https://img.shields.io/github/stars/SeldonIO/alibi?style=flat)](https://github.com/SeldonIO/alibi/stargazers) - Algorithms for monitoring and explaining machine learning models.
* [anchor](https://github.com/marcotcr/anchor) [![GitHub stars](https://img.shields.io/github/stars/marcotcr/anchor?style=flat)](https://github.com/marcotcr/anchor/stargazers) - Code for "High-Precision Model-Agnostic Explanations" paper.
* [aequitas](https://github.com/dssg/aequitas) [![GitHub stars](https://img.shields.io/github/stars/dssg/aequitas?style=flat)](https://github.com/dssg/aequitas/stargazers) - Bias and Fairness Audit Toolkit.
* [Contrastive Explanation](https://github.com/MarcelRobeer/ContrastiveExplanation) [![GitHub stars](https://img.shields.io/github/stars/MarcelRobeer/ContrastiveExplanation?style=flat)](https://github.com/MarcelRobeer/ContrastiveExplanation/stargazers) - Contrastive Explanation (Foil Trees). <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [yellowbrick](https://github.com/DistrictDataLabs/yellowbrick) [![GitHub stars](https://img.shields.io/github/stars/DistrictDataLabs/yellowbrick?style=flat)](https://github.com/DistrictDataLabs/yellowbrick/stargazers) - Visual analysis and diagnostic tools to facilitate machine learning model selection. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-plot](https://github.com/reiinakano/scikit-plot) [![GitHub stars](https://img.shields.io/github/stars/reiinakano/scikit-plot?style=flat)](https://github.com/reiinakano/scikit-plot/stargazers) - An intuitive library to add plotting functionality to scikit-learn objects. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [shap](https://github.com/slundberg/shap) [![GitHub stars](https://img.shields.io/github/stars/slundberg/shap?style=flat)](https://github.com/slundberg/shap/stargazers) - A unified approach to explain the output of any machine learning model. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [InterpretML](https://github.com/interpretml/interpret) [![GitHub stars](https://img.shields.io/github/stars/interpretml/interpret?style=flat)](https://github.com/interpretml/interpret/stargazers) - InterpretML implements the Explainable Boosting Machine (EBM), a modern, fully interpretable machine learning model based on Generalized Additive Models (GAMs). This open-source package also provides visualization tools for EBMs, other glass-box models, and black-box explanations. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [ELI5](https://github.com/TeamHG-Memex/eli5) [![GitHub stars](https://img.shields.io/github/stars/TeamHG-Memex/eli5?style=flat)](https://github.com/TeamHG-Memex/eli5/stargazers) - A library for debugging/inspecting machine learning classifiers and explaining their predictions.
* [Lime](https://github.com/marcotcr/lime) [![GitHub stars](https://img.shields.io/github/stars/marcotcr/lime?style=flat)](https://github.com/marcotcr/lime/stargazers) - Explaining the predictions of any machine learning classifier. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [FairML](https://github.com/adebayoj/fairml) [![GitHub stars](https://img.shields.io/github/stars/adebayoj/fairml?style=flat)](https://github.com/adebayoj/fairml/stargazers) - FairML is a python toolbox auditing the machine learning models for bias. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [L2X](https://github.com/Jianbo-Lab/L2X) [![GitHub stars](https://img.shields.io/github/stars/Jianbo-Lab/L2X?style=flat)](https://github.com/Jianbo-Lab/L2X/stargazers) - Code for replicating the experiments in the paper *Learning to Explain: An Information-Theoretic Perspective on Model Interpretation*.
* [PDPbox](https://github.com/SauceCat/PDPbox) [![GitHub stars](https://img.shields.io/github/stars/SauceCat/PDPbox?style=flat)](https://github.com/SauceCat/PDPbox/stargazers) - Partial dependence plot toolbox.
* [PyCEbox](https://github.com/AustinRochford/PyCEbox) [![GitHub stars](https://img.shields.io/github/stars/AustinRochford/PyCEbox?style=flat)](https://github.com/AustinRochford/PyCEbox/stargazers) - Python Individual Conditional Expectation Plot Toolbox.
* [Skater](https://github.com/datascienceinc/Skater) [![GitHub stars](https://img.shields.io/github/stars/datascienceinc/Skater?style=flat)](https://github.com/datascienceinc/Skater/stargazers) - Python Library for Model Interpretation.
* [model-analysis](https://github.com/tensorflow/model-analysis) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/model-analysis?style=flat)](https://github.com/tensorflow/model-analysis/stargazers) - Model analysis tools for TensorFlow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [themis-ml](https://github.com/cosmicBboy/themis-ml) [![GitHub stars](https://img.shields.io/github/stars/cosmicBboy/themis-ml?style=flat)](https://github.com/cosmicBboy/themis-ml/stargazers) - A library that implements fairness-aware machine learning algorithms. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [treeinterpreter](https://github.com/andosa/treeinterpreter) [![GitHub stars](https://img.shields.io/github/stars/andosa/treeinterpreter?style=flat)](https://github.com/andosa/treeinterpreter/stargazers) - Interpreting scikit-learn's decision tree and random forest predictions. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [AI Explainability 360](https://github.com/IBM/AIX360) [![GitHub stars](https://img.shields.io/github/stars/IBM/AIX360?style=flat)](https://github.com/IBM/AIX360/stargazers) - Interpretability and explainability of data and machine learning models.
* [Auralisation](https://github.com/keunwoochoi/Auralisation) [![GitHub stars](https://img.shields.io/github/stars/keunwoochoi/Auralisation?style=flat)](https://github.com/keunwoochoi/Auralisation/stargazers) - Auralisation of learned features in CNN (for audio).
* [CapsNet-Visualization](https://github.com/bourdakos1/CapsNet-Visualization) [![GitHub stars](https://img.shields.io/github/stars/bourdakos1/CapsNet-Visualization?style=flat)](https://github.com/bourdakos1/CapsNet-Visualization/stargazers) - A visualization of the CapsNet layers to better understand how it works.
* [lucid](https://github.com/tensorflow/lucid) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/lucid?style=flat)](https://github.com/tensorflow/lucid/stargazers) - A collection of infrastructure and tools for research in neural network interpretability.
* [Netron](https://github.com/lutzroeder/Netron) [![GitHub stars](https://img.shields.io/github/stars/lutzroeder/Netron?style=flat)](https://github.com/lutzroeder/Netron/stargazers) - Visualizer for deep learning and machine learning models (no Python code, but visualizes models from most Python Deep Learning frameworks).
* [FlashLight](https://github.com/dlguys/flashlight) [![GitHub stars](https://img.shields.io/github/stars/dlguys/flashlight?style=flat)](https://github.com/dlguys/flashlight/stargazers) - Visualization Tool for your NeuralNetwork.
* [tensorboard-pytorch](https://github.com/lanpa/tensorboard-pytorch) [![GitHub stars](https://img.shields.io/github/stars/lanpa/tensorboard-pytorch?style=flat)](https://github.com/lanpa/tensorboard-pytorch/stargazers) - Tensorboard for PyTorch (and chainer, mxnet, numpy, ...).

## Genetic Programming
* [gplearn](https://github.com/trevorstephens/gplearn) [![GitHub stars](https://img.shields.io/github/stars/trevorstephens/gplearn?style=flat)](https://github.com/trevorstephens/gplearn/stargazers) - Genetic Programming in Python. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [PyGAD](https://github.com/ahmedfgad/GeneticAlgorithmPython) [![GitHub stars](https://img.shields.io/github/stars/ahmedfgad/GeneticAlgorithmPython?style=flat)](https://github.com/ahmedfgad/GeneticAlgorithmPython/stargazers) - Genetic Algorithm in Python. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible"> <img height="20" src="img/keras_big.png" alt="keras">
* [DEAP](https://github.com/DEAP/deap) [![GitHub stars](https://img.shields.io/github/stars/DEAP/deap?style=flat)](https://github.com/DEAP/deap/stargazers) - Distributed Evolutionary Algorithms in Python.
* [karoo_gp](https://github.com/kstaats/karoo_gp) [![GitHub stars](https://img.shields.io/github/stars/kstaats/karoo_gp?style=flat)](https://github.com/kstaats/karoo_gp/stargazers) - A Genetic Programming platform for Python with GPU support. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [monkeys](https://github.com/hchasestevens/monkeys) [![GitHub stars](https://img.shields.io/github/stars/hchasestevens/monkeys?style=flat)](https://github.com/hchasestevens/monkeys/stargazers) - A strongly-typed genetic programming framework for Python.
* [sklearn-genetic](https://github.com/manuel-calzolari/sklearn-genetic) [![GitHub stars](https://img.shields.io/github/stars/manuel-calzolari/sklearn-genetic?style=flat)](https://github.com/manuel-calzolari/sklearn-genetic/stargazers) - Genetic feature selection module for scikit-learn. <img height="20" src="img/sklearn_big.png" alt="sklearn">

<a name="opt"></a>
## Optimization
* [Optuna](https://github.com/optuna/optuna) [![GitHub stars](https://img.shields.io/github/stars/optuna/optuna?style=flat)](https://github.com/optuna/optuna/stargazers) - A hyperparameter optimization framework.
* [pymoo](https://github.com/anyoptimization/pymoo) [![GitHub stars](https://img.shields.io/github/stars/anyoptimization/pymoo?style=flat)](https://github.com/anyoptimization/pymoo/stargazers) - Multi-objective Optimization in Python.
* [pycma](https://github.com/CMA-ES/pycma?tab=readme-ov-file) [![GitHub stars](https://img.shields.io/github/stars/CMA-ES/pycma?tab=readme-ov-file?style=flat)](https://github.com/CMA-ES/pycma?tab=readme-ov-file/stargazers) - Python implementation of CMA-ES.
* [Spearmint](https://github.com/HIPS/Spearmint) [![GitHub stars](https://img.shields.io/github/stars/HIPS/Spearmint?style=flat)](https://github.com/HIPS/Spearmint/stargazers) - Bayesian optimization.
* [BoTorch](https://github.com/pytorch/botorch) [![GitHub stars](https://img.shields.io/github/stars/pytorch/botorch?style=flat)](https://github.com/pytorch/botorch/stargazers) - Bayesian optimization in PyTorch. <img height="20" src="img/pytorch_big2.png" alt="PyTorch based/compatible">
* [scikit-opt](https://github.com/guofei9987/scikit-opt) [![GitHub stars](https://img.shields.io/github/stars/guofei9987/scikit-opt?style=flat)](https://github.com/guofei9987/scikit-opt/stargazers) - Heuristic Algorithms for optimization.
* [sklearn-genetic-opt](https://github.com/rodrigo-arenas/Sklearn-genetic-opt) [![GitHub stars](https://img.shields.io/github/stars/rodrigo-arenas/Sklearn-genetic-opt?style=flat)](https://github.com/rodrigo-arenas/Sklearn-genetic-opt/stargazers) - Hyperparameters tuning and feature selection using evolutionary algorithms. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [SMAC3](https://github.com/automl/SMAC3) [![GitHub stars](https://img.shields.io/github/stars/automl/SMAC3?style=flat)](https://github.com/automl/SMAC3/stargazers) - Sequential Model-based Algorithm Configuration.
* [Optunity](https://github.com/claesenm/optunity) [![GitHub stars](https://img.shields.io/github/stars/claesenm/optunity?style=flat)](https://github.com/claesenm/optunity/stargazers) - Is a library containing various optimizers for hyperparameter tuning.
* [hyperopt](https://github.com/hyperopt/hyperopt) [![GitHub stars](https://img.shields.io/github/stars/hyperopt/hyperopt?style=flat)](https://github.com/hyperopt/hyperopt/stargazers) - Distributed Asynchronous Hyperparameter Optimization in Python.
* [hyperopt-sklearn](https://github.com/hyperopt/hyperopt-sklearn) [![GitHub stars](https://img.shields.io/github/stars/hyperopt/hyperopt-sklearn?style=flat)](https://github.com/hyperopt/hyperopt-sklearn/stargazers) - Hyper-parameter optimization for sklearn. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sklearn-deap](https://github.com/rsteca/sklearn-deap) [![GitHub stars](https://img.shields.io/github/stars/rsteca/sklearn-deap?style=flat)](https://github.com/rsteca/sklearn-deap/stargazers) - Use evolutionary algorithms instead of gridsearch in scikit-learn. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sigopt_sklearn](https://github.com/sigopt/sigopt_sklearn) [![GitHub stars](https://img.shields.io/github/stars/sigopt/sigopt_sklearn?style=flat)](https://github.com/sigopt/sigopt_sklearn/stargazers) - SigOpt wrappers for scikit-learn methods. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Bayesian Optimization](https://github.com/fmfn/BayesianOptimization) [![GitHub stars](https://img.shields.io/github/stars/fmfn/BayesianOptimization?style=flat)](https://github.com/fmfn/BayesianOptimization/stargazers) - A Python implementation of global optimization with gaussian processes.
* [SafeOpt](https://github.com/befelix/SafeOpt) [![GitHub stars](https://img.shields.io/github/stars/befelix/SafeOpt?style=flat)](https://github.com/befelix/SafeOpt/stargazers) - Safe Bayesian Optimization.
* [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize) [![GitHub stars](https://img.shields.io/github/stars/scikit-optimize/scikit-optimize?style=flat)](https://github.com/scikit-optimize/scikit-optimize/stargazers) - Sequential model-based optimization with a `scipy.optimize` interface.
* [Solid](https://github.com/100/Solid) [![GitHub stars](https://img.shields.io/github/stars/100/Solid?style=flat)](https://github.com/100/Solid/stargazers) - A comprehensive gradient-free optimization framework written in Python.
* [PySwarms](https://github.com/ljvmiranda921/pyswarms) [![GitHub stars](https://img.shields.io/github/stars/ljvmiranda921/pyswarms?style=flat)](https://github.com/ljvmiranda921/pyswarms/stargazers) - A research toolkit for particle swarm optimization in Python.
* [Platypus](https://github.com/Project-Platypus/Platypus) [![GitHub stars](https://img.shields.io/github/stars/Project-Platypus/Platypus?style=flat)](https://github.com/Project-Platypus/Platypus/stargazers) - A Free and Open Source Python Library for Multiobjective Optimization.
* [GPflowOpt](https://github.com/GPflow/GPflowOpt) [![GitHub stars](https://img.shields.io/github/stars/GPflow/GPflowOpt?style=flat)](https://github.com/GPflow/GPflowOpt/stargazers) - Bayesian Optimization using GPflow. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [POT](https://github.com/rflamary/POT) [![GitHub stars](https://img.shields.io/github/stars/rflamary/POT?style=flat)](https://github.com/rflamary/POT/stargazers) - Python Optimal Transport library.
* [Talos](https://github.com/autonomio/talos) [![GitHub stars](https://img.shields.io/github/stars/autonomio/talos?style=flat)](https://github.com/autonomio/talos/stargazers) - Hyperparameter Optimization for Keras Models.
* [nlopt](https://github.com/stevengj/nlopt) [![GitHub stars](https://img.shields.io/github/stars/stevengj/nlopt?style=flat)](https://github.com/stevengj/nlopt/stargazers) - Library for nonlinear optimization (global and local, constrained or unconstrained).
* [OR-Tools](https://developers.google.com/optimization) - An open-source software suite for optimization by Google; provides a unified programming interface to a half dozen solvers: SCIP, GLPK, GLOP, CP-SAT, CPLEX, and Gurobi.

## Feature Engineering

### General
* [Featuretools](https://github.com/Featuretools/featuretools) [![GitHub stars](https://img.shields.io/github/stars/Featuretools/featuretools?style=flat)](https://github.com/Featuretools/featuretools/stargazers) - Automated feature engineering.
* [Feature Engine](https://github.com/feature-engine/feature_engine) [![GitHub stars](https://img.shields.io/github/stars/feature-engine/feature_engine?style=flat)](https://github.com/feature-engine/feature_engine/stargazers) - Feature engineering package with sklearn-like functionality. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [OpenFE](https://github.com/IIIS-Li-Group/OpenFE) [![GitHub stars](https://img.shields.io/github/stars/IIIS-Li-Group/OpenFE?style=flat)](https://github.com/IIIS-Li-Group/OpenFE/stargazers) - Automated feature generation with expert-level performance.
* [skl-groups](https://github.com/dougalsutherland/skl-groups) [![GitHub stars](https://img.shields.io/github/stars/dougalsutherland/skl-groups?style=flat)](https://github.com/dougalsutherland/skl-groups/stargazers) - A scikit-learn addon to operate on set/"group"-based features. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Feature Forge](https://github.com/machinalis/featureforge) [![GitHub stars](https://img.shields.io/github/stars/machinalis/featureforge?style=flat)](https://github.com/machinalis/featureforge/stargazers) - A set of tools for creating and testing machine learning features. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [few](https://github.com/lacava/few) [![GitHub stars](https://img.shields.io/github/stars/lacava/few?style=flat)](https://github.com/lacava/few/stargazers) - A feature engineering wrapper for sklearn. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-mdr](https://github.com/EpistasisLab/scikit-mdr) [![GitHub stars](https://img.shields.io/github/stars/EpistasisLab/scikit-mdr?style=flat)](https://github.com/EpistasisLab/scikit-mdr/stargazers) - A sklearn-compatible Python implementation of Multifactor Dimensionality Reduction (MDR) for feature construction. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [tsfresh](https://github.com/blue-yonder/tsfresh) [![GitHub stars](https://img.shields.io/github/stars/blue-yonder/tsfresh?style=flat)](https://github.com/blue-yonder/tsfresh/stargazers) - Automatic extraction of relevant features from time series. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [dirty_cat](https://github.com/dirty-cat/dirty_cat) [![GitHub stars](https://img.shields.io/github/stars/dirty-cat/dirty_cat?style=flat)](https://github.com/dirty-cat/dirty_cat/stargazers) - Machine learning on dirty tabular data (especially: string-based variables for classifcation and regression). <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [NitroFE](https://github.com/NITRO-AI/NitroFE) [![GitHub stars](https://img.shields.io/github/stars/NITRO-AI/NitroFE?style=flat)](https://github.com/NITRO-AI/NitroFE/stargazers) - Moving window features. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sk-transformer](https://github.com/chrislemke/sk-transformers) [![GitHub stars](https://img.shields.io/github/stars/chrislemke/sk-transformers?style=flat)](https://github.com/chrislemke/sk-transformers/stargazers) - A collection of various pandas & scikit-learn compatible transformers for all kinds of preprocessing and feature engineering steps <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [tubular](https://github.com/azukds/tubular) [![GitHub stars](https://img.shields.io/github/stars/azukds/tubular?style=flat)](https://github.com/azukds/tubular/stargazers) - Collection of scikit-learn compatible transformers written in [narwhals]( https://github.com/narwhals-dev/narwhals), which can accept either polars/pandas inputs and utilise the chosen library under the hood. <img height="20" src="img/sklearn_big.png" alt="sklearn"><img height="20" src="img/pandas_big.png" alt="pandas compatible">


### Feature Selection
* [scikit-feature](https://github.com/jundongl/scikit-feature) [![GitHub stars](https://img.shields.io/github/stars/jundongl/scikit-feature?style=flat)](https://github.com/jundongl/scikit-feature/stargazers) - Feature selection repository in Python.
* [boruta_py](https://github.com/scikit-learn-contrib/boruta_py) [![GitHub stars](https://img.shields.io/github/stars/scikit-learn-contrib/boruta_py?style=flat)](https://github.com/scikit-learn-contrib/boruta_py/stargazers) - Implementations of the Boruta all-relevant feature selection method. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [BoostARoota](https://github.com/chasedehan/BoostARoota) [![GitHub stars](https://img.shields.io/github/stars/chasedehan/BoostARoota?style=flat)](https://github.com/chasedehan/BoostARoota/stargazers) - A fast xgboost feature selection algorithm. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-rebate](https://github.com/EpistasisLab/scikit-rebate) [![GitHub stars](https://img.shields.io/github/stars/EpistasisLab/scikit-rebate?style=flat)](https://github.com/EpistasisLab/scikit-rebate/stargazers) - A scikit-learn-compatible Python implementation of ReBATE, a suite of Relief-based feature selection algorithms for Machine Learning. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [zoofs](https://github.com/jaswinder9051998/zoofs) [![GitHub stars](https://img.shields.io/github/stars/jaswinder9051998/zoofs?style=flat)](https://github.com/jaswinder9051998/zoofs/stargazers) - A feature selection library based on evolutionary algorithms.

## Visualization
### General Purposes
* [Matplotlib](https://github.com/matplotlib/matplotlib) [![GitHub stars](https://img.shields.io/github/stars/matplotlib/matplotlib?style=flat)](https://github.com/matplotlib/matplotlib/stargazers) - Plotting with Python.
* [seaborn](https://github.com/mwaskom/seaborn) [![GitHub stars](https://img.shields.io/github/stars/mwaskom/seaborn?style=flat)](https://github.com/mwaskom/seaborn/stargazers) - Statistical data visualization using matplotlib.
* [prettyplotlib](https://github.com/olgabot/prettyplotlib) [![GitHub stars](https://img.shields.io/github/stars/olgabot/prettyplotlib?style=flat)](https://github.com/olgabot/prettyplotlib/stargazers) - Painlessly create beautiful matplotlib plots.
* [python-ternary](https://github.com/marcharper/python-ternary) [![GitHub stars](https://img.shields.io/github/stars/marcharper/python-ternary?style=flat)](https://github.com/marcharper/python-ternary/stargazers) - Ternary plotting library for Python with matplotlib.
* [missingno](https://github.com/ResidentMario/missingno) [![GitHub stars](https://img.shields.io/github/stars/ResidentMario/missingno?style=flat)](https://github.com/ResidentMario/missingno/stargazers) - Missing data visualization module for Python.
* [chartify](https://github.com/spotify/chartify/) [![GitHub stars](https://img.shields.io/github/stars/spotify/chartify/?style=flat)](https://github.com/spotify/chartify//stargazers) - Python library that makes it easy for data scientists to create charts.
* [physt](https://github.com/janpipek/physt) [![GitHub stars](https://img.shields.io/github/stars/janpipek/physt?style=flat)](https://github.com/janpipek/physt/stargazers) - Improved histograms.
### Interactive plots
* [animatplot](https://github.com/t-makaro/animatplot) [![GitHub stars](https://img.shields.io/github/stars/t-makaro/animatplot?style=flat)](https://github.com/t-makaro/animatplot/stargazers) - A python package for animating plots built on matplotlib.
* [plotly](https://plot.ly/python/) - A Python library that makes interactive and publication-quality graphs.
* [Bokeh](https://github.com/bokeh/bokeh) [![GitHub stars](https://img.shields.io/github/stars/bokeh/bokeh?style=flat)](https://github.com/bokeh/bokeh/stargazers) - Interactive Web Plotting for Python.
* [Altair](https://altair-viz.github.io/) - Declarative statistical visualization library for Python. Can easily do many data transformation within the code to create graph
* [bqplot](https://github.com/bqplot/bqplot) [![GitHub stars](https://img.shields.io/github/stars/bqplot/bqplot?style=flat)](https://github.com/bqplot/bqplot/stargazers) - Plotting library for IPython/Jupyter notebooks
* [pyecharts](https://github.com/pyecharts/pyecharts) [![GitHub stars](https://img.shields.io/github/stars/pyecharts/pyecharts?style=flat)](https://github.com/pyecharts/pyecharts/stargazers) - Migrated from [Echarts](https://github.com/apache/echarts) [![GitHub stars](https://img.shields.io/github/stars/apache/echarts?style=flat)](https://github.com/apache/echarts/stargazers), a charting and visualization library, to Python's interactive visual drawing library.<img height="20" src="img/pyecharts.png" alt="pyecharts"> <img height="20" src="img/echarts.png" alt="echarts">
### Map
* [folium](https://python-visualization.github.io/folium/quickstart.html#Getting-Started) - Makes it easy to visualize data on an interactive open street map
* [geemap](https://github.com/giswqs/geemap) [![GitHub stars](https://img.shields.io/github/stars/giswqs/geemap?style=flat)](https://github.com/giswqs/geemap/stargazers) - Python package for interactive mapping with Google Earth Engine (GEE)
### Automatic Plotting
* [HoloViews](https://github.com/ioam/holoviews) [![GitHub stars](https://img.shields.io/github/stars/ioam/holoviews?style=flat)](https://github.com/ioam/holoviews/stargazers) - Stop plotting your data - annotate your data and let it visualize itself.
* [AutoViz](https://github.com/AutoViML/AutoViz) [![GitHub stars](https://img.shields.io/github/stars/AutoViML/AutoViz?style=flat)](https://github.com/AutoViML/AutoViz/stargazers): Visualize data automatically with 1 line of code (ideal for machine learning)
* [SweetViz](https://github.com/fbdesignpro/sweetviz) [![GitHub stars](https://img.shields.io/github/stars/fbdesignpro/sweetviz?style=flat)](https://github.com/fbdesignpro/sweetviz/stargazers): Visualize and compare datasets, target values and associations, with one line of code.

### NLP
* [pyLDAvis](https://github.com/bmabey/pyLDAvis) [![GitHub stars](https://img.shields.io/github/stars/bmabey/pyLDAvis?style=flat)](https://github.com/bmabey/pyLDAvis/stargazers): Visualize interactive topic model

## Deployment
* [fastapi](https://fastapi.tiangolo.com/) - Modern, fast (high-performance), a web framework for building APIs with Python
* [streamlit](https://www.streamlit.io/) - Make it easy to deploy the machine learning model
* [streamsync](https://github.com/streamsync-cloud/streamsync) [![GitHub stars](https://img.shields.io/github/stars/streamsync-cloud/streamsync?style=flat)](https://github.com/streamsync-cloud/streamsync/stargazers) - No-code in the front, Python in the back. An open-source framework for creating data apps.
* [gradio](https://github.com/gradio-app/gradio) [![GitHub stars](https://img.shields.io/github/stars/gradio-app/gradio?style=flat)](https://github.com/gradio-app/gradio/stargazers) - Create UIs for your machine learning model in Python in 3 minutes.
* [Vizro](https://github.com/mckinsey/vizro) [![GitHub stars](https://img.shields.io/github/stars/mckinsey/vizro?style=flat)](https://github.com/mckinsey/vizro/stargazers) - A toolkit for creating modular data visualization applications.
* [datapane](https://datapane.com/) - A collection of APIs to turn scripts and notebooks into interactive reports.
* [binder](https://mybinder.org/) - Enable sharing and execute Jupyter Notebooks
* [Deepnote](https://github.com/deepnote/deepnote) [![GitHub stars](https://img.shields.io/github/stars/deepnote/deepnote?style=flat)](https://github.com/deepnote/deepnote/stargazers) - Deepnote is a drop-in replacement for Jupyter with an AI-first design, sleek UI, new blocks, and native data integrations. Use Python, R, and SQL locally in your favorite IDE, then scale to Deepnote cloud for real-time collaboration, Deepnote agent, and deployable data apps.


## Statistics
* [pandas_summary](https://github.com/mouradmourafiq/pandas-summary) [![GitHub stars](https://img.shields.io/github/stars/mouradmourafiq/pandas-summary?style=flat)](https://github.com/mouradmourafiq/pandas-summary/stargazers) - Extension to pandas dataframes describe function. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) [![GitHub stars](https://img.shields.io/github/stars/pandas-profiling/pandas-profiling?style=flat)](https://github.com/pandas-profiling/pandas-profiling/stargazers) - Create HTML profiling reports from pandas DataFrame objects. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [statsmodels](https://github.com/statsmodels/statsmodels) [![GitHub stars](https://img.shields.io/github/stars/statsmodels/statsmodels?style=flat)](https://github.com/statsmodels/statsmodels/stargazers) - Statistical modeling and econometrics in Python.
* [stockstats](https://github.com/jealous/stockstats) [![GitHub stars](https://img.shields.io/github/stars/jealous/stockstats?style=flat)](https://github.com/jealous/stockstats/stargazers) - Supply a wrapper ``StockDataFrame`` based on the ``pandas.DataFrame`` with inline stock statistics/indicators support.
* [weightedcalcs](https://github.com/jsvine/weightedcalcs) [![GitHub stars](https://img.shields.io/github/stars/jsvine/weightedcalcs?style=flat)](https://github.com/jsvine/weightedcalcs/stargazers) - A pandas-based utility to calculate weighted means, medians, distributions, standard deviations, and more.
* [scikit-posthocs](https://github.com/maximtrp/scikit-posthocs) [![GitHub stars](https://img.shields.io/github/stars/maximtrp/scikit-posthocs?style=flat)](https://github.com/maximtrp/scikit-posthocs/stargazers) - Pairwise Multiple Comparisons Post-hoc Tests.
* [Alphalens](https://github.com/quantopian/alphalens) [![GitHub stars](https://img.shields.io/github/stars/quantopian/alphalens?style=flat)](https://github.com/quantopian/alphalens/stargazers) - Performance analysis of predictive (alpha) stock factors.


## Data Manipulation

### Data Frames
* [pandas](https://pandas.pydata.org/pandas-docs/stable/) - Powerful Python data analysis toolkit.
* [polars](https://github.com/pola-rs/polars) [![GitHub stars](https://img.shields.io/github/stars/pola-rs/polars?style=flat)](https://github.com/pola-rs/polars/stargazers) - A fast multi-threaded, hybrid-out-of-core DataFrame library.
* [Arctic](https://github.com/manahl/arctic) [![GitHub stars](https://img.shields.io/github/stars/manahl/arctic?style=flat)](https://github.com/manahl/arctic/stargazers) - High-performance datastore for time series and tick data.
* [datatable](https://github.com/h2oai/datatable) [![GitHub stars](https://img.shields.io/github/stars/h2oai/datatable?style=flat)](https://github.com/h2oai/datatable/stargazers) - Data.table for Python. <img height="20" src="img/R_big.png" alt="R inspired/ported lib">
* [pandas_profiling](https://github.com/pandas-profiling/pandas-profiling) [![GitHub stars](https://img.shields.io/github/stars/pandas-profiling/pandas-profiling?style=flat)](https://github.com/pandas-profiling/pandas-profiling/stargazers) - Create HTML profiling reports from pandas DataFrame objects
* [cuDF](https://github.com/rapidsai/cudf) [![GitHub stars](https://img.shields.io/github/stars/rapidsai/cudf?style=flat)](https://github.com/rapidsai/cudf/stargazers) - GPU DataFrame Library. <img height="20" src="img/pandas_big.png" alt="pandas compatible"> <img height="20" src="img/gpu_big.png" alt="GPU accelerated">
* [blaze](https://github.com/blaze/blaze) [![GitHub stars](https://img.shields.io/github/stars/blaze/blaze?style=flat)](https://github.com/blaze/blaze/stargazers) - NumPy and pandas interface to Big Data. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [pandasql](https://github.com/yhat/pandasql) [![GitHub stars](https://img.shields.io/github/stars/yhat/pandasql?style=flat)](https://github.com/yhat/pandasql/stargazers) -  Allows you to query pandas DataFrames using SQL syntax. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [pandas-gbq](https://github.com/pydata/pandas-gbq) [![GitHub stars](https://img.shields.io/github/stars/pydata/pandas-gbq?style=flat)](https://github.com/pydata/pandas-gbq/stargazers) - pandas Google Big Query. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [xpandas](https://github.com/alan-turing-institute/xpandas) [![GitHub stars](https://img.shields.io/github/stars/alan-turing-institute/xpandas?style=flat)](https://github.com/alan-turing-institute/xpandas/stargazers) - Universal 1d/2d data containers with Transformers .functionality for data analysis by [The Alan Turing Institute](https://www.turing.ac.uk/).
* [pysparkling](https://github.com/svenkreiss/pysparkling) [![GitHub stars](https://img.shields.io/github/stars/svenkreiss/pysparkling?style=flat)](https://github.com/svenkreiss/pysparkling/stargazers) - A pure Python implementation of Apache Spark's RDD and DStream interfaces. <img height="20" src="img/spark_big.png" alt="Apache Spark based">
* [modin](https://github.com/modin-project/modin) [![GitHub stars](https://img.shields.io/github/stars/modin-project/modin?style=flat)](https://github.com/modin-project/modin/stargazers) - Speed up your pandas workflows by changing a single line of code. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [swifter](https://github.com/jmcarpenter2/swifter) [![GitHub stars](https://img.shields.io/github/stars/jmcarpenter2/swifter?style=flat)](https://github.com/jmcarpenter2/swifter/stargazers) - A package that efficiently applies any function to a pandas dataframe or series in the fastest available manner.
* [pandas-log](https://github.com/eyaltrabelsi/pandas-log) [![GitHub stars](https://img.shields.io/github/stars/eyaltrabelsi/pandas-log?style=flat)](https://github.com/eyaltrabelsi/pandas-log/stargazers) - A package that allows providing feedback about basic pandas operations and finds both business logic and performance issues.
* [vaex](https://github.com/vaexio/vaex) [![GitHub stars](https://img.shields.io/github/stars/vaexio/vaex?style=flat)](https://github.com/vaexio/vaex/stargazers) - Out-of-Core DataFrames for Python, ML, visualize and explore big tabular data at a billion rows per second.
* [xarray](https://github.com/pydata/xarray) [![GitHub stars](https://img.shields.io/github/stars/pydata/xarray?style=flat)](https://github.com/pydata/xarray/stargazers) - Xarray combines the best features of NumPy and pandas for multidimensional data selection by supplementing numerical axis labels with named dimensions for more intuitive, concise, and less error-prone indexing routines.

### Pipelines
* [pdpipe](https://github.com/shaypal5/pdpipe) [![GitHub stars](https://img.shields.io/github/stars/shaypal5/pdpipe?style=flat)](https://github.com/shaypal5/pdpipe/stargazers) - Sasy pipelines for pandas DataFrames.
* [SSPipe](https://sspipe.github.io/) - Python pipe (|) operator with support for DataFrames and Numpy, and Pytorch.
* [pandas-ply](https://github.com/coursera/pandas-ply) [![GitHub stars](https://img.shields.io/github/stars/coursera/pandas-ply?style=flat)](https://github.com/coursera/pandas-ply/stargazers) - Functional data manipulation for pandas. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [Dplython](https://github.com/dodger487/dplython) [![GitHub stars](https://img.shields.io/github/stars/dodger487/dplython?style=flat)](https://github.com/dodger487/dplython/stargazers) - Dplyr for Python. <img height="20" src="img/R_big.png" alt="R inspired/ported lib">
* [sklearn-pandas](https://github.com/scikit-learn-contrib/sklearn-pandas) [![GitHub stars](https://img.shields.io/github/stars/scikit-learn-contrib/sklearn-pandas?style=flat)](https://github.com/scikit-learn-contrib/sklearn-pandas/stargazers) - pandas integration with sklearn. <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [Dataset](https://github.com/analysiscenter/dataset) [![GitHub stars](https://img.shields.io/github/stars/analysiscenter/dataset?style=flat)](https://github.com/analysiscenter/dataset/stargazers) - Helps you conveniently work with random or sequential batches of your data and define data processing.
* [pyjanitor](https://github.com/ericmjl/pyjanitor) [![GitHub stars](https://img.shields.io/github/stars/ericmjl/pyjanitor?style=flat)](https://github.com/ericmjl/pyjanitor/stargazers) - Clean APIs for data cleaning. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [meza](https://github.com/reubano/meza) [![GitHub stars](https://img.shields.io/github/stars/reubano/meza?style=flat)](https://github.com/reubano/meza/stargazers) - A Python toolkit for processing tabular data.
* [Prodmodel](https://github.com/prodmodel/prodmodel) [![GitHub stars](https://img.shields.io/github/stars/prodmodel/prodmodel?style=flat)](https://github.com/prodmodel/prodmodel/stargazers) - Build system for data science pipelines.
* [dopanda](https://github.com/dovpanda-dev/dovpanda) [![GitHub stars](https://img.shields.io/github/stars/dovpanda-dev/dovpanda?style=flat)](https://github.com/dovpanda-dev/dovpanda/stargazers) -  Hints and tips for using pandas in an analysis environment. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [Hamilton](https://github.com/DAGWorks-Inc/hamilton) [![GitHub stars](https://img.shields.io/github/stars/DAGWorks-Inc/hamilton?style=flat)](https://github.com/DAGWorks-Inc/hamilton/stargazers) - A microframework for dataframe generation that applies Directed Acyclic Graphs specified by a flow of lazily evaluated Python functions.

### Data-centric AI
* [cleanlab](https://github.com/cleanlab/cleanlab) [![GitHub stars](https://img.shields.io/github/stars/cleanlab/cleanlab?style=flat)](https://github.com/cleanlab/cleanlab/stargazers) - The standard data-centric AI package for data quality and machine learning with messy, real-world data and labels.
* [snorkel](https://github.com/snorkel-team/snorkel) [![GitHub stars](https://img.shields.io/github/stars/snorkel-team/snorkel?style=flat)](https://github.com/snorkel-team/snorkel/stargazers) - A system for quickly generating training data with weak supervision.
* [dataprep](https://github.com/sfu-db/dataprep) [![GitHub stars](https://img.shields.io/github/stars/sfu-db/dataprep?style=flat)](https://github.com/sfu-db/dataprep/stargazers) - Collect, clean, and visualize your data in Python with a few lines of code.

### Synthetic Data

* [ydata-synthetic](https://github.com/ydataai/ydata-synthetic) [![GitHub stars](https://img.shields.io/github/stars/ydataai/ydata-synthetic?style=flat)](https://github.com/ydataai/ydata-synthetic/stargazers) - A package to generate synthetic tabular and time-series data leveraging the state-of-the-art generative models. <img height="20" src="img/pandas_big.png" alt="pandas compatible">

## Distributed Computing
* [Horovod](https://github.com/uber/horovod) [![GitHub stars](https://img.shields.io/github/stars/uber/horovod?style=flat)](https://github.com/uber/horovod/stargazers) - Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet. <img height="20" src="img/tf_big2.png" alt="sklearn">
* [PySpark](https://spark.apache.org/docs/0.9.0/python-programming-guide.html) - Exposes the Spark programming model to Python. <img height="20" src="img/spark_big.png" alt="Apache Spark based">
* [Veles](https://github.com/Samsung/veles) [![GitHub stars](https://img.shields.io/github/stars/Samsung/veles?style=flat)](https://github.com/Samsung/veles/stargazers) - Distributed machine learning platform.
* [Jubatus](https://github.com/jubatus/jubatus) [![GitHub stars](https://img.shields.io/github/stars/jubatus/jubatus?style=flat)](https://github.com/jubatus/jubatus/stargazers) - Framework and Library for Distributed Online Machine Learning.
* [DMTK](https://github.com/Microsoft/DMTK) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/DMTK?style=flat)](https://github.com/Microsoft/DMTK/stargazers) - Microsoft Distributed Machine Learning Toolkit.
* [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) [![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/Paddle?style=flat)](https://github.com/PaddlePaddle/Paddle/stargazers) - PArallel Distributed Deep LEarning.
* [dask-ml](https://github.com/dask/dask-ml) [![GitHub stars](https://img.shields.io/github/stars/dask/dask-ml?style=flat)](https://github.com/dask/dask-ml/stargazers) - Distributed and parallel machine learning. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Distributed](https://github.com/dask/distributed) [![GitHub stars](https://img.shields.io/github/stars/dask/distributed?style=flat)](https://github.com/dask/distributed/stargazers) - Distributed computation in Python.

## Experimentation
* [mlflow](https://github.com/mlflow/mlflow) [![GitHub stars](https://img.shields.io/github/stars/mlflow/mlflow?style=flat)](https://github.com/mlflow/mlflow/stargazers) - Open source platform for the machine learning lifecycle.
* [Neptune](https://neptune.ai) - A lightweight ML experiment tracking, results visualization, and management tool.
* [dvc](https://github.com/iterative/dvc) [![GitHub stars](https://img.shields.io/github/stars/iterative/dvc?style=flat)](https://github.com/iterative/dvc/stargazers) - Data Version Control | Git for Data & Models | ML Experiments Management.
* [envd](https://github.com/tensorchord/envd) [![GitHub stars](https://img.shields.io/github/stars/tensorchord/envd?style=flat)](https://github.com/tensorchord/envd/stargazers) - 🏕️ machine learning development environment for data science and AI/ML engineering teams.
* [Sacred](https://github.com/IDSIA/sacred) [![GitHub stars](https://img.shields.io/github/stars/IDSIA/sacred?style=flat)](https://github.com/IDSIA/sacred/stargazers) - A tool to help you configure, organize, log, and reproduce experiments.
* [Ax](https://github.com/facebook/Ax) [![GitHub stars](https://img.shields.io/github/stars/facebook/Ax?style=flat)](https://github.com/facebook/Ax/stargazers) - Adaptive Experimentation Platform. <img height="20" src="img/sklearn_big.png" alt="sklearn">

## Data Validation
* [great_expectations](https://github.com/great-expectations/great_expectations) [![GitHub stars](https://img.shields.io/github/stars/great-expectations/great_expectations?style=flat)](https://github.com/great-expectations/great_expectations/stargazers) - Always know what to expect from your data.
* [pandera](https://github.com/unionai-oss/pandera) [![GitHub stars](https://img.shields.io/github/stars/unionai-oss/pandera?style=flat)](https://github.com/unionai-oss/pandera/stargazers) - A lightweight, flexible, and expressive statistical data testing library.
* [deepchecks](https://github.com/deepchecks/deepchecks) [![GitHub stars](https://img.shields.io/github/stars/deepchecks/deepchecks?style=flat)](https://github.com/deepchecks/deepchecks/stargazers) - Validation & testing of ML models and data during model development, deployment, and production. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [evidently](https://github.com/evidentlyai/evidently) [![GitHub stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=flat)](https://github.com/evidentlyai/evidently/stargazers) - Evaluate and monitor ML models from validation to production.
* [TensorFlow Data Validation](https://github.com/tensorflow/data-validation) [![GitHub stars](https://img.shields.io/github/stars/tensorflow/data-validation?style=flat)](https://github.com/tensorflow/data-validation/stargazers) - Library for exploring and validating machine learning data.
* [DataComPy](https://github.com/capitalone/datacompy) [![GitHub stars](https://img.shields.io/github/stars/capitalone/datacompy?style=flat)](https://github.com/capitalone/datacompy/stargazers)- A library to compare Pandas, Polars, and Spark data frames. It provides stats and lets users adjust for match accuracy.

## Evaluation
* [recmetrics](https://github.com/statisticianinstilettos/recmetrics) [![GitHub stars](https://img.shields.io/github/stars/statisticianinstilettos/recmetrics?style=flat)](https://github.com/statisticianinstilettos/recmetrics/stargazers) - Library of useful metrics and plots for evaluating recommender systems.
* [Metrics](https://github.com/benhamner/Metrics) [![GitHub stars](https://img.shields.io/github/stars/benhamner/Metrics?style=flat)](https://github.com/benhamner/Metrics/stargazers) - Machine learning evaluation metric.
* [sklearn-evaluation](https://github.com/edublancas/sklearn-evaluation) [![GitHub stars](https://img.shields.io/github/stars/edublancas/sklearn-evaluation?style=flat)](https://github.com/edublancas/sklearn-evaluation/stargazers) - Model evaluation made easy: plots, tables, and markdown reports. <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [AI Fairness 360](https://github.com/IBM/AIF360) [![GitHub stars](https://img.shields.io/github/stars/IBM/AIF360?style=flat)](https://github.com/IBM/AIF360/stargazers) - Fairness metrics for datasets and ML models, explanations, and algorithms to mitigate bias in datasets and models.
* [alibi-detect](https://github.com/SeldonIO/alibi-detect) [![GitHub stars](https://img.shields.io/github/stars/SeldonIO/alibi-detect?style=flat)](https://github.com/SeldonIO/alibi-detect/stargazers) - Algorithms for outlier, adversarial and drift detection.<img height="20" src="img/alibi-detect.png" alt="sklearn">

## Computations
* [NumPy](https://numpy.org/) - The fundamental package for scientific computing with Python
* [Dask](https://github.com/dask/dask) [![GitHub stars](https://img.shields.io/github/stars/dask/dask?style=flat)](https://github.com/dask/dask/stargazers) - Parallel computing with task scheduling. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [bottleneck](https://github.com/kwgoodman/bottleneck) [![GitHub stars](https://img.shields.io/github/stars/kwgoodman/bottleneck?style=flat)](https://github.com/kwgoodman/bottleneck/stargazers) - Fast NumPy array functions written in C.
* [CuPy](https://github.com/cupy/cupy) [![GitHub stars](https://img.shields.io/github/stars/cupy/cupy?style=flat)](https://github.com/cupy/cupy/stargazers) - NumPy-like API accelerated with CUDA.
* [scikit-tensor](https://github.com/mnick/scikit-tensor) [![GitHub stars](https://img.shields.io/github/stars/mnick/scikit-tensor?style=flat)](https://github.com/mnick/scikit-tensor/stargazers) - Python library for multilinear algebra and tensor factorizations.
* [numdifftools](https://github.com/pbrod/numdifftools) [![GitHub stars](https://img.shields.io/github/stars/pbrod/numdifftools?style=flat)](https://github.com/pbrod/numdifftools/stargazers) - Solve automatic numerical differentiation problems in one or more variables.
* [quaternion](https://github.com/moble/quaternion) [![GitHub stars](https://img.shields.io/github/stars/moble/quaternion?style=flat)](https://github.com/moble/quaternion/stargazers) - Add built-in support for quaternions to numpy.
* [adaptive](https://github.com/python-adaptive/adaptive) [![GitHub stars](https://img.shields.io/github/stars/python-adaptive/adaptive?style=flat)](https://github.com/python-adaptive/adaptive/stargazers) - Tools for adaptive and parallel samping of mathematical functions.
* [NumExpr](https://github.com/pydata/numexpr) [![GitHub stars](https://img.shields.io/github/stars/pydata/numexpr?style=flat)](https://github.com/pydata/numexpr/stargazers) - A fast numerical expression evaluator for NumPy that comes with an integrated computing virtual machine to speed calculations up by avoiding memory allocation for intermediate results.

## Web Scraping
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): The easiest library to scrape static websites for beginners
* [Scrapy](https://scrapy.org/): Fast and extensible scraping library. Can write rules and create customized scraper without touching the core
* [Selenium](https://selenium-python.readthedocs.io/installation.html#introduction): Use Selenium Python API to access all functionalities of Selenium WebDriver in an intuitive way like a real user.
* [Pattern](https://github.com/clips/pattern) [![GitHub stars](https://img.shields.io/github/stars/clips/pattern?style=flat)](https://github.com/clips/pattern/stargazers): High level scraping for well-establish websites such as Google, Twitter, and Wikipedia. Also has NLP, machine learning algorithms, and visualization
* [twitterscraper](https://github.com/taspinar/twitterscraper) [![GitHub stars](https://img.shields.io/github/stars/taspinar/twitterscraper?style=flat)](https://github.com/taspinar/twitterscraper/stargazers): Efficient library to scrape Twitter

## Spatial Analysis
* [GeoPandas](https://github.com/geopandas/geopandas) [![GitHub stars](https://img.shields.io/github/stars/geopandas/geopandas?style=flat)](https://github.com/geopandas/geopandas/stargazers) - Python tools for geographic data. <img height="20" src="img/pandas_big.png" alt="pandas compatible">
* [PySal](https://github.com/pysal/pysal) [![GitHub stars](https://img.shields.io/github/stars/pysal/pysal?style=flat)](https://github.com/pysal/pysal/stargazers) - Python Spatial Analysis Library.

## Quantum Computing
* [qiskit](https://github.com/Qiskit/qiskit) [![GitHub stars](https://img.shields.io/github/stars/Qiskit/qiskit?style=flat)](https://github.com/Qiskit/qiskit/stargazers) - Qiskit is an open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules.
* [cirq](https://github.com/quantumlib/Cirq) [![GitHub stars](https://img.shields.io/github/stars/quantumlib/Cirq?style=flat)](https://github.com/quantumlib/Cirq/stargazers) - A python framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.
* [PennyLane](https://github.com/XanaduAI/pennylane) [![GitHub stars](https://img.shields.io/github/stars/XanaduAI/pennylane?style=flat)](https://github.com/XanaduAI/pennylane/stargazers) - Quantum machine learning, automatic differentiation, and optimization of hybrid quantum-classical computations.
* [QML](https://github.com/qmlcode/qml) [![GitHub stars](https://img.shields.io/github/stars/qmlcode/qml?style=flat)](https://github.com/qmlcode/qml/stargazers) - A Python Toolkit for Quantum Machine Learning.

## Conversion
* [sklearn-porter](https://github.com/nok/sklearn-porter) [![GitHub stars](https://img.shields.io/github/stars/nok/sklearn-porter?style=flat)](https://github.com/nok/sklearn-porter/stargazers) - Transpile trained scikit-learn estimators to C, Java, JavaScript, and others.
* [ONNX](https://github.com/onnx/onnx) [![GitHub stars](https://img.shields.io/github/stars/onnx/onnx?style=flat)](https://github.com/onnx/onnx/stargazers) - Open Neural Network Exchange.
* [MMdnn](https://github.com/Microsoft/MMdnn) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/MMdnn?style=flat)](https://github.com/Microsoft/MMdnn/stargazers) -  A set of tools to help users inter-operate among different deep learning frameworks.
* [treelite](https://github.com/dmlc/treelite) [![GitHub stars](https://img.shields.io/github/stars/dmlc/treelite?style=flat)](https://github.com/dmlc/treelite/stargazers) - Universal model exchange and serialization format for decision tree forests.

## Contributing
Contributions are welcome! :sunglasses: </br>
Read the <a href=https://github.com/krzjoa/awesome-python-datascience/blob/master/CONTRIBUTING.md>contribution guideline</a>.

## License
This work is licensed under the Creative Commons Attribution 4.0 International License - [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
