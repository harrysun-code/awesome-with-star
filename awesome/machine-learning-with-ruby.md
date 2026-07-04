# ML with Ruby

> 来源：[arbox/machine-learning-with-ruby](https://github.com/arbox/machine-learning-with-ruby)

[![GitHub stars](https://img.shields.io/github/stars/arbox/machine-learning-with-ruby?style=flat)](https://github.com/arbox/machine-learning-with-ruby/stargazers)

<img title="Awesome Machine Learning with Ruby" alt="Awesome Machine Learning with Ruby" src="header.png" align="center">

[![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome#readme) [![Support Me](https://img.shields.io/badge/%F0%9F%92%97-Support%20Me-blue.svg?style=flat-square)](https://www.patreon.com/arbox)

[[RubyNLP](https://github.com/arbox/nlp-with-ruby) [![GitHub stars](https://img.shields.io/github/stars/arbox/nlp-with-ruby?style=flat)](https://github.com/arbox/nlp-with-ruby/stargazers) |
 [RubyDataScience](https://github.com/arbox/data-science-with-ruby) [![GitHub stars](https://img.shields.io/github/stars/arbox/data-science-with-ruby?style=flat)](https://github.com/arbox/data-science-with-ruby/stargazers) |
 [RubyInterop](https://github.com/arbox/ruby-interoperability) [![GitHub stars](https://img.shields.io/github/stars/arbox/ruby-interoperability?style=flat)](https://github.com/arbox/ruby-interoperability/stargazers)]

# Awesome Machine Learning with Ruby [<img src="ruby.jpg" align="left" width="30px" height="30px" />][ruby]

> Curated List of Ruby Machine Learning Links and Resources

[Machine Learning][ml] is a field of [Computational Science][cs] -
often nested under [AI][ai] research - with many practical
applications due to the ability of resulting algorithms to
systematically implement a specific solution without explicit
programmer's instructions. Obviously many algorithms need a definition
of [features][fe] to look at or a biggish [training set][ts] of data to derive the
solution from.

This curated list comprises [_awesome_][awesome] libraries,
data sources, tutorials and presentations about [Machine Learning][ml]
utilizing the [Ruby][ruby] programming language.

A lot of useful resources on this list come from the development by
[The Ruby Science Foundation][sciruby], our [contributors][contributors] and
our own day to day work on various ML applications.

:sparkles: Every [contribution](contributing.md) is welcome! Add links through pull
requests or create an issue to start a discussion.

Follow us on [Twitter](https://twitter.com/NonWebRuby) and please spread
the word using the `#RubyML` hash tag!

<!-- nodoc -->
## Contents

<!-- toc -->

- [:sparkles: Tutorials](#sparkles-tutorials)
- [Machine Learning Libraries](#machine-learning-libraries)
  * [Frameworks](#frameworks)
  * [Neural networks](#neural-networks)
  * [Deep Learning](#deep-learning)
  * [Kernel methods](#kernel-methods)
  * [Evolutionary algorithms](#evolutionary-algorithms)
  * [Bayesian methods](#bayesian-methods)
  * [Decision trees](#decision-trees)
  * [Clustering](#clustering)
  * [Linear classifiers](#linear-classifiers)
  * [Statistical models](#statistical-models)
  * [Gradient boosting](#gradient-boosting)
  * [Vector search](#vector-search)
- [Applications of machine learning](#applications-of-machine-learning)
- [Data structures](#data-structures)
- [Data visualization](#data-visualization)
- [Articles, Posts, Talks, and Presentations](#articles-posts-talks-and-presentations)
- [Projects and Code Examples](#projects-and-code-examples)
- [Heroku buildpacks](#heroku-buildpacks)
- [Books, Blogs, Channels](#books-blogs-channels)
- [Community](#community)
- [Related Resources](#related-resources)
- [License](#license)

<!-- tocstop -->

<!-- doc -->

## :sparkles: Tutorials

Please help us to fill out this section! :smiley:
- [Ruby neural networks](https://www.honeybadger.io/blog/ruby-neural-networks/)
- [How to implement linear regression in Ruby](https://www.practicalai.io/implementing-linear-regression-using-ruby/)
  <sup>[[code](https://github.com/daugaard/example-linear-regression) [![GitHub stars](https://img.shields.io/github/stars/daugaard/example-linear-regression?style=flat)](https://github.com/daugaard/example-linear-regression/stargazers)]</sup>
- [How to implement classification using logistic regression in Ruby](https://www.practicalai.io/implementing-classification-using-logistic-regression-in-ruby/)
- [How to implement simple binary classification using a Neural Network in Ruby](https://www.practicalai.io/implementing-simple-classification-using-neural-network-in-ruby/)
  <sup>[[code](https://github.com/daugaard/example-neural-network) [![GitHub stars](https://img.shields.io/github/stars/daugaard/example-neural-network?style=flat)](https://github.com/daugaard/example-neural-network/stargazers)]</sup>
- [How to implement classification using a SVM in Ruby](https://www.practicalai.io/implementing-classification-using-a-svm-in-ruby/)
  <sup>[[code](https://github.com/daugaard/example-svm) [![GitHub stars](https://img.shields.io/github/stars/daugaard/example-svm?style=flat)](https://github.com/daugaard/example-svm/stargazers)]</sup>
- [Unsupervised learning using k-means clustering in Ruby](https://www.practicalai.io/unsupervised-learning-using-k-means-clustering-in-ruby/)
  <sup>[[code](https://github.com/daugaard/example-kmeans-clustering) [![GitHub stars](https://img.shields.io/github/stars/daugaard/example-kmeans-clustering?style=flat)](https://github.com/daugaard/example-kmeans-clustering/stargazers)]</sup>
- [Teaching an AI to play a simple game using Q-Learning in Ruby](https://www.practicalai.io/teaching-ai-play-simple-game-using-q-learning/)
  <sup>[[code](https://github.com/daugaard/q-learning-simple-game) [![GitHub stars](https://img.shields.io/github/stars/daugaard/q-learning-simple-game?style=flat)](https://github.com/daugaard/q-learning-simple-game/stargazers)]</sup>
- [Teaching a Neural Network to play a game using Q-Learning in Ruby](https://www.practicalai.io/teaching-a-neural-network-to-play-a-game-with-q-learning/)
  <sup>[[code](https://github.com/daugaard/q-learning-simple-game/tree/neuralnetwork) [![GitHub stars](https://img.shields.io/github/stars/daugaard/q-learning-simple-game/tree/neuralnetwork?style=flat)](https://github.com/daugaard/q-learning-simple-game/tree/neuralnetwork/stargazers)]</sup>
- [Using the Python scikit-learn machine learning library in Ruby using PyCall](https://www.practicalai.io/using-scikit-learn-machine-learning-library-in-ruby-using-pycall/)
  <sup>[[code](https://github.com/daugaard/scikit-learn-from-ruby) [![GitHub stars](https://img.shields.io/github/stars/daugaard/scikit-learn-from-ruby?style=flat)](https://github.com/daugaard/scikit-learn-from-ruby/stargazers)]</sup>
- [How to _evolve_ neural networks in Ruby using the Machine Learning Workbench](https://github.com/giuse/machine_learning_workbench/blob/master/examples/neuroevolution.rb) [![GitHub stars](https://img.shields.io/github/stars/giuse/machine_learning_workbench/blob/master/examples/neuroevolution.rb?style=flat)](https://github.com/giuse/machine_learning_workbench/blob/master/examples/neuroevolution.rb/stargazers)

## Machine Learning Libraries

[Machine Learning][ml] algorithms in pure Ruby or written in other
programming languages with appropriate bindings for Ruby.

### Frameworks

- [LangChain.rb](https://github.com/andreibondarev/langchainrb) [![GitHub stars](https://img.shields.io/github/stars/andreibondarev/langchainrb?style=flat)](https://github.com/andreibondarev/langchainrb/stargazers) -
  Build ML/AI-supercharged applications with Ruby's LangChain.
- [weka](https://github.com/paulgoetze/weka-jruby) [![GitHub stars](https://img.shields.io/github/stars/paulgoetze/weka-jruby?style=flat)](https://github.com/paulgoetze/weka-jruby/stargazers) -
  JRuby bindings for Weka, different ML algorithms implemented through Weka.
- [ai4r](https://github.com/SergioFierens/ai4r) [![GitHub stars](https://img.shields.io/github/stars/SergioFierens/ai4r?style=flat)](https://github.com/SergioFierens/ai4r/stargazers) -
  Artificial Intelligence for Ruby.
- [classifier-reborn](https://github.com/jekyll/classifier-reborn) [![GitHub stars](https://img.shields.io/github/stars/jekyll/classifier-reborn?style=flat)](https://github.com/jekyll/classifier-reborn/stargazers) -
  General classifier module to allow Bayesian and other types of classifications.
  <sup>[[dep: GLS](#gls)]</sup>
- [scoruby](https://github.com/asafschers/scoruby) [![GitHub stars](https://img.shields.io/github/stars/asafschers/scoruby?style=flat)](https://github.com/asafschers/scoruby/stargazers) -
  Ruby scoring API for [PMML](http://dmg.org/pmml/v4-3/GeneralStructure.html) (Predictive Model Markup Language).
- [rblearn](https://github.com/himkt/rblearn) [![GitHub stars](https://img.shields.io/github/stars/himkt/rblearn?style=flat)](https://github.com/himkt/rblearn/stargazers) - Feature Extraction and Crossvalidation library.
- [data_modeler](https://github.com/giuse/data_modeler) [![GitHub stars](https://img.shields.io/github/stars/giuse/data_modeler?style=flat)](https://github.com/giuse/data_modeler/stargazers) -
  Model your data with machine learning. Ample test coverage, examples to start fast, complete documentation. Production ready since 1.0.0.
- [shogun](https://github.com/shogun-toolbox/shogun) [![GitHub stars](https://img.shields.io/github/stars/shogun-toolbox/shogun?style=flat)](https://github.com/shogun-toolbox/shogun/stargazers) - Polyfunctional and mature
  machine learning toolbox with [Ruby bindings](https://github.com/shogun-toolbox/shogun/tree/develop/src/interfaces/ruby) [![GitHub stars](https://img.shields.io/github/stars/shogun-toolbox/shogun/tree/develop/src/interfaces/ruby?style=flat)](https://github.com/shogun-toolbox/shogun/tree/develop/src/interfaces/ruby/stargazers).
- [aws-sdk-machinelearning](https://github.com/aws/aws-sdk-ruby) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-ruby?style=flat)](https://github.com/aws/aws-sdk-ruby/stargazers) -
  Machine Learning API of the Amazon Web Services.
- [azure_mgmt_machine_learning](https://github.com/Azure/azure-sdk-for-ruby) [![GitHub stars](https://img.shields.io/github/stars/Azure/azure-sdk-for-ruby?style=flat)](https://github.com/Azure/azure-sdk-for-ruby/stargazers) -
  Machine Learning API of the Microsoft Azure.
- [machine_learning_workbench](https://github.com/giuse/machine_learning_workbench) [![GitHub stars](https://img.shields.io/github/stars/giuse/machine_learning_workbench?style=flat)](https://github.com/giuse/machine_learning_workbench/stargazers) -
  Growing machine learning framework written in pure Ruby, high performance computing using
  [Numo](https://github.com/ruby-numo/) [![GitHub stars](https://img.shields.io/github/stars/ruby-numo/?style=flat)](https://github.com/ruby-numo//stargazers), CUDA bindings through [Cumo](https://github.com/sonots/cumo) [![GitHub stars](https://img.shields.io/github/stars/sonots/cumo?style=flat)](https://github.com/sonots/cumo/stargazers).
  Currently implementating neural networks, evolutionary strategies, vector quantization, and plenty of
  examples and utilities.
- [Deep NeuroEvolution](https://github.com/giuse/DNE) [![GitHub stars](https://img.shields.io/github/stars/giuse/DNE?style=flat)](https://github.com/giuse/DNE/stargazers) -
  Experimental setup based on the [machine_learning_workbench](https://github.com/giuse/machine_learning_workbench) [![GitHub stars](https://img.shields.io/github/stars/giuse/machine_learning_workbench?style=flat)](https://github.com/giuse/machine_learning_workbench/stargazers)
  towards searching for deep neural networks (rather than training) using evolutionary algorithms. Applications to the
  [OpenAI Gym](https://github.com/openai/gym) [![GitHub stars](https://img.shields.io/github/stars/openai/gym?style=flat)](https://github.com/openai/gym/stargazers) using [PyCall](https://github.com/mrkn/pycall.rb) [![GitHub stars](https://img.shields.io/github/stars/mrkn/pycall.rb?style=flat)](https://github.com/mrkn/pycall.rb/stargazers).
- [rumale](https://github.com/yoshoku/rumale) [![GitHub stars](https://img.shields.io/github/stars/yoshoku/rumale?style=flat)](https://github.com/yoshoku/rumale/stargazers) -
  Machine Learninig toolkit in Ruby with wide range of implemented algorithms
  (SVM, Logistic Regression, Linear Regression, Random Forest etc.) and
  interfaces similar to [Scikit-Learn][scikit] in Python.
- [eps](https://github.com/ankane/eps) [![GitHub stars](https://img.shields.io/github/stars/ankane/eps?style=flat)](https://github.com/ankane/eps/stargazers) - Bayesian Classification and Linear Regression with exports
  using [PMML](http://dmg.org/pmml/v4-3/GeneralStructure.html) and an alternative backend using [GSL][gsl].
- [ruby-openai](https://github.com/alexrudall/ruby-openai) [![GitHub stars](https://img.shields.io/github/stars/alexrudall/ruby-openai?style=flat)](https://github.com/alexrudall/ruby-openai/stargazers) - OpenAI API wrapper
- [Instruct](https://github.com/instruct-rb/instruct) [![GitHub stars](https://img.shields.io/github/stars/instruct-rb/instruct?style=flat)](https://github.com/instruct-rb/instruct/stargazers) - Inspired by Guidance; weave code, prompts and completions together to instruct LLMs to do what you want.
  
### Neural networks

- [neural-net-ruby](https://github.com/gbuesing/neural-net-ruby) [![GitHub stars](https://img.shields.io/github/stars/gbuesing/neural-net-ruby?style=flat)](https://github.com/gbuesing/neural-net-ruby/stargazers) -
  Neural network written in Ruby.
- [ruby-fann](https://github.com/tangledpath/ruby-fann) [![GitHub stars](https://img.shields.io/github/stars/tangledpath/ruby-fann?style=flat)](https://github.com/tangledpath/ruby-fann/stargazers) -
  Ruby bindings to the [Fast Artificial Neural Network Library (FANN)](http://leenissen.dk/fann/wp/).
- [cerebrum](https://github.com/irfansharif/cerebrum) [![GitHub stars](https://img.shields.io/github/stars/irfansharif/cerebrum?style=flat)](https://github.com/irfansharif/cerebrum/stargazers) -
  Experimental implementation for Artificial Neural Networks in Ruby.
- [tlearn-rb](https://github.com/josephwilk/tlearn-rb) [![GitHub stars](https://img.shields.io/github/stars/josephwilk/tlearn-rb?style=flat)](https://github.com/josephwilk/tlearn-rb/stargazers) -
  Recurrent Neural Network library for Ruby.
- [brains](https://github.com/jedld/brains-jruby) [![GitHub stars](https://img.shields.io/github/stars/jedld/brains-jruby?style=flat)](https://github.com/jedld/brains-jruby/stargazers) -
  Feed-forward neural networks for JRuby based on
  [brains](https://github.com/jedld/brains) [![GitHub stars](https://img.shields.io/github/stars/jedld/brains?style=flat)](https://github.com/jedld/brains/stargazers).
- [machine_learning_workbench](https://github.com/giuse/machine_learning_workbench/tree/master/lib/machine_learning_workbench/neural_network) [![GitHub stars](https://img.shields.io/github/stars/giuse/machine_learning_workbench/tree/master/lib/machine_learning_workbench/neural_network?style=flat)](https://github.com/giuse/machine_learning_workbench/tree/master/lib/machine_learning_workbench/neural_network/stargazers) -
  Framework including pure-Ruby implementation of both feed-forward and recurrent neural networks
  (fully connected). Training available using neuroevolution (Natural Evolution Strategies algorithms).
- [rann](https://github.com/mikecmpbll/rann) [![GitHub stars](https://img.shields.io/github/stars/mikecmpbll/rann?style=flat)](https://github.com/mikecmpbll/rann/stargazers) -
  Flexible Ruby ANN implementation with backprop (through-time, for recurrent
  nets), gradient checking, adagrad, and parallel batch execution.

### Deep learning

- [tensor_stream](https://github.com/jedld/tensor_stream) [![GitHub stars](https://img.shields.io/github/stars/jedld/tensor_stream?style=flat)](https://github.com/jedld/tensor_stream/stargazers) -
  Ground-up and standalone reimplementation of TensorFlow for Ruby.
- [red-chainer](https://github.com/red-data-tools/red-chainer) [![GitHub stars](https://img.shields.io/github/stars/red-data-tools/red-chainer?style=flat)](https://github.com/red-data-tools/red-chainer/stargazers) - Deep learning framework for Ruby.
- [tensorflow](https://github.com/somaticio/tensorflow.rb) [![GitHub stars](https://img.shields.io/github/stars/somaticio/tensorflow.rb?style=flat)](https://github.com/somaticio/tensorflow.rb/stargazers) - Ruby bindings for [TensorFlow](https://www.tensorflow.org/).
- [ruby-dnn](https://github.com/unagiootoro/ruby-dnn) [![GitHub stars](https://img.shields.io/github/stars/unagiootoro/ruby-dnn?style=flat)](https://github.com/unagiootoro/ruby-dnn/stargazers) - Simple deep learning for Ruby.
- [torch-rb](https://github.com/ankane/torch-rb) [![GitHub stars](https://img.shields.io/github/stars/ankane/torch-rb?style=flat)](https://github.com/ankane/torch-rb/stargazers) - Ruby bindings for [LibTorch](https://github.com/pytorch/pytorch) [![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch?style=flat)](https://github.com/pytorch/pytorch/stargazers)
  using [rice](https://github.com/jasonroelofs/rice) [![GitHub stars](https://img.shields.io/github/stars/jasonroelofs/rice?style=flat)](https://github.com/jasonroelofs/rice/stargazers).
- [mxnet](https://github.com/mrkn/mxnet.rb) [![GitHub stars](https://img.shields.io/github/stars/mrkn/mxnet.rb?style=flat)](https://github.com/mrkn/mxnet.rb/stargazers) - Ruby bindings for [mxnet](https://mxnet.apache.org/).

### Kernel methods

- [rb-libsvm](https://github.com/febeling/rb-libsvm) [![GitHub stars](https://img.shields.io/github/stars/febeling/rb-libsvm?style=flat)](https://github.com/febeling/rb-libsvm/stargazers) -
  Support Vector Machines with Ruby and the [LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) library.
  <sup>[[dep: bundled](#bundled)]</sup>

### Evolutionary algorithms

- [machine_learning_workbench](https://github.com/giuse/machine_learning_workbench/tree/master/lib/machine_learning_workbench/optimizer/natural_evolution_strategies) [![GitHub stars](https://img.shields.io/github/stars/giuse/machine_learning_workbench/tree/master/lib/machine_learning_workbench/optimizer/natural_evolution_strategies?style=flat)](https://github.com/giuse/machine_learning_workbench/tree/master/lib/machine_learning_workbench/optimizer/natural_evolution_strategies/stargazers) -
  Framework including pure-Ruby implementations of Natural Evolution Strategy algorithms
  (black-box optimization), specifically Exponential NES (XNES),
  Separable NES (sNES), Block-Diagonal NES (BDNES) and more.
  Applications include neural network search/training (neuroevolution).
- [simple_ga](https://github.com/giuse/simple_ga) [![GitHub stars](https://img.shields.io/github/stars/giuse/simple_ga?style=flat)](https://github.com/giuse/simple_ga/stargazers) -
  Simplest Genetic Algorithms implementation in Ruby.

### Bayesian methods

- [linnaeus](https://github.com/djcp/linnaeus) [![GitHub stars](https://img.shields.io/github/stars/djcp/linnaeus?style=flat)](https://github.com/djcp/linnaeus/stargazers) -
  Redis-backed Bayesian classifier.
- [naive_bayes](https://github.com/reddavis/Naive-Bayes) [![GitHub stars](https://img.shields.io/github/stars/reddavis/Naive-Bayes?style=flat)](https://github.com/reddavis/Naive-Bayes/stargazers) -
  Simple Naive Bayes classifier.
- [nbayes](https://github.com/oasic/nbayes) [![GitHub stars](https://img.shields.io/github/stars/oasic/nbayes?style=flat)](https://github.com/oasic/nbayes/stargazers) -
  Full-featured, Ruby implementation of Naive Bayes.

### Decision trees

- [decisiontree](https://github.com/igrigorik/decisiontree) [![GitHub stars](https://img.shields.io/github/stars/igrigorik/decisiontree?style=flat)](https://github.com/igrigorik/decisiontree/stargazers) -
  Decision Tree ID3 Algorithm in pure Ruby.
  <sup>[[dep: GraphViz](#graphviz) |
        [post](https://www.igvita.com/2007/04/16/decision-tree-learning-in-ruby/)]</sup>.

### Clustering

- [kmeans-clusterer](https://github.com/gbuesing/kmeans-clusterer) [![GitHub stars](https://img.shields.io/github/stars/gbuesing/kmeans-clusterer?style=flat)](https://github.com/gbuesing/kmeans-clusterer/stargazers) -
  k-means clustering in Ruby.
- [k_means](https://github.com/reddavis/K-Means) [![GitHub stars](https://img.shields.io/github/stars/reddavis/K-Means?style=flat)](https://github.com/reddavis/K-Means/stargazers) -
  Attempting to build a fast, memory efficient K-Means program.
- [knn](https://github.com/reddavis/knn) [![GitHub stars](https://img.shields.io/github/stars/reddavis/knn?style=flat)](https://github.com/reddavis/knn/stargazers) -
  Simple K Nearest Neighbour Algorithm.

### Linear classifiers

- [liblinear-ruby-swig](https://github.com/tomz/liblinear-ruby-swig) [![GitHub stars](https://img.shields.io/github/stars/tomz/liblinear-ruby-swig?style=flat)](https://github.com/tomz/liblinear-ruby-swig/stargazers) -
  Ruby interface to LIBLINEAR (much more efficient than LIBSVM for text classification).
- [liblinear-ruby](https://github.com/kei500/liblinear-ruby) [![GitHub stars](https://img.shields.io/github/stars/kei500/liblinear-ruby?style=flat)](https://github.com/kei500/liblinear-ruby/stargazers) -
  Ruby interface to LIBLINEAR using SWIG.

### Statistical models

- [rtimbl](https://github.com/maspwr/rtimbl) [![GitHub stars](https://img.shields.io/github/stars/maspwr/rtimbl?style=flat)](https://github.com/maspwr/rtimbl/stargazers) -
  Memory based learners from the Timbl framework.
- [lda-ruby](https://github.com/ealdent/lda-ruby) [![GitHub stars](https://img.shields.io/github/stars/ealdent/lda-ruby?style=flat)](https://github.com/ealdent/lda-ruby/stargazers) -
  Ruby implementation of the [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
  (Latent Dirichlet Allocation) for automatic Topic Modelling and Document Clustering.
- [maxent_string_classifier](https://github.com/mccraigmccraig/maxent_string_classifier) [![GitHub stars](https://img.shields.io/github/stars/mccraigmccraig/maxent_string_classifier?style=flat)](https://github.com/mccraigmccraig/maxent_string_classifier/stargazers) -
  JRuby maximum entropy classifier for string data, based on the OpenNLP Maxent framework.
- [omnicat](https://github.com/mustafaturan/omnicat) [![GitHub stars](https://img.shields.io/github/stars/mustafaturan/omnicat?style=flat)](https://github.com/mustafaturan/omnicat/stargazers) -
  Generalized rack framework for text classifications.
- [omnicat-bayes](https://github.com/mustafaturan/omnicat-bayes) [![GitHub stars](https://img.shields.io/github/stars/mustafaturan/omnicat-bayes?style=flat)](https://github.com/mustafaturan/omnicat-bayes/stargazers) -
  Naive Bayes text classification implementation as an OmniCat classifier strategy.
  <sup>[[dep: bundled](#bundled)]</sup>

### Gradient boosting

- [xgboost](https://github.com/PairOnAir/xgboost-ruby) [![GitHub stars](https://img.shields.io/github/stars/PairOnAir/xgboost-ruby?style=flat)](https://github.com/PairOnAir/xgboost-ruby/stargazers) &mdash;
  Ruby bindings for XGBoost.
  <sup>[[dep: XGBoost](#xgboost)]</sup>
- [xgb](https://github.com/ankane/xgb) [![GitHub stars](https://img.shields.io/github/stars/ankane/xgb?style=flat)](https://github.com/ankane/xgb/stargazers) &mdash;
  Ruby bindings for XGBoost.
  <sup>[[dep: XGBoost](#xgboost)]</sup>
- [lightgbm](https://github.com/ankane/lightgbm) [![GitHub stars](https://img.shields.io/github/stars/ankane/lightgbm?style=flat)](https://github.com/ankane/lightgbm/stargazers) &mdash;
  Ruby bindings for LightGBM.
  <sup>[[dep: LightGBM](#lightgbm)]</sup>

### Vector search

- [flann](https://github.com/mariusmuja/flann) [![GitHub stars](https://img.shields.io/github/stars/mariusmuja/flann?style=flat)](https://github.com/mariusmuja/flann/stargazers) -
  Ruby bindings for the [FLANN](https://github.com/flann-lib/flann) [![GitHub stars](https://img.shields.io/github/stars/flann-lib/flann?style=flat)](https://github.com/flann-lib/flann/stargazers) (Fast Library for Approximate Nearest Neighbors).
  <sup>[[flann](#flann)]</sup>
- [annoy-rb](https://github.com/yoshoku/annoy.rb) [![GitHub stars](https://img.shields.io/github/stars/yoshoku/annoy.rb?style=flat)](https://github.com/yoshoku/annoy.rb/stargazers) -
  Ruby bindings for the [Annoy](https://github.com/spotify/annoy) [![GitHub stars](https://img.shields.io/github/stars/spotify/annoy?style=flat)](https://github.com/spotify/annoy/stargazers) (Approximate Nearest Neighbors Oh Yeah).
- [hnswlib.rb](https://github.com/yoshoku/hnswlib.rb) [![GitHub stars](https://img.shields.io/github/stars/yoshoku/hnswlib.rb?style=flat)](https://github.com/yoshoku/hnswlib.rb/stargazers) -
  Ruby bindings for the [Hnswlib](https://github.com/nmslib/hnswlib) [![GitHub stars](https://img.shields.io/github/stars/nmslib/hnswlib?style=flat)](https://github.com/nmslib/hnswlib/stargazers) that implements approximate nearest neighbor search with Hierarchical Navigable Small World graphs.
- [ngt-ruby](https://github.com/ankane/ngt-ruby) [![GitHub stars](https://img.shields.io/github/stars/ankane/ngt-ruby?style=flat)](https://github.com/ankane/ngt-ruby/stargazers) -
  Ruby bindings for the [NGT](https://github.com/yahoojapan/NGT) [![GitHub stars](https://img.shields.io/github/stars/yahoojapan/NGT?style=flat)](https://github.com/yahoojapan/NGT/stargazers) (Neighborhood Graph and Tree for Indexing High-dimensional data).
- [milvus](https://github.com/andreibondarev/milvus) [![GitHub stars](https://img.shields.io/github/stars/andreibondarev/milvus?style=flat)](https://github.com/andreibondarev/milvus/stargazers) &mdash;
  Ruby client for Milvus Vector DB.
- [pinecone](https://github.com/ScotterC/pinecone) [![GitHub stars](https://img.shields.io/github/stars/ScotterC/pinecone?style=flat)](https://github.com/ScotterC/pinecone/stargazers) &mdash;
  Ruby client for Pinecone Vector DB.
- [qdrant-ruby](https://github.com/andreibondarev/qdrant-ruby) [![GitHub stars](https://img.shields.io/github/stars/andreibondarev/qdrant-ruby?style=flat)](https://github.com/andreibondarev/qdrant-ruby/stargazers) &mdash;
  Ruby wrapper for the Qdrant vector search database API.
- [weaviate-ruby](https://github.com/andreibondarev/weaviate-ruby) [![GitHub stars](https://img.shields.io/github/stars/andreibondarev/weaviate-ruby?style=flat)](https://github.com/andreibondarev/weaviate-ruby/stargazers) &mdash;
  Ruby wrapper for the Weaviate vector search database API.

## Applications of machine learning

- [phashion](https://github.com/westonplatter/phashion) [![GitHub stars](https://img.shields.io/github/stars/westonplatter/phashion?style=flat)](https://github.com/westonplatter/phashion/stargazers) -
  Ruby wrapper around pHash, the perceptual hash library for detecting duplicate multimedia files.
  <sup>[[ImageMagick](#imagemagick) | [libjpeg](#libjpeg)]</sup>

## Data structures

If you're going to implement your own ML algorithms you're probably interested
in storing your feature sets efficiently. Look for appropriate
[data structures](https://github.com/arbox/data-science-with-ruby#data-structures) [![GitHub stars](https://img.shields.io/github/stars/arbox/data-science-with-ruby?style=flat)](https://github.com/arbox/data-science-with-ruby/stargazers)
in our [Data Science with Ruby][ds-with-ruby] list.

## Data visualization

Please refer to the [Data Visualization](https://github.com/arbox/data-science-with-ruby#visualization) [![GitHub stars](https://img.shields.io/github/stars/arbox/data-science-with-ruby?style=flat)](https://github.com/arbox/data-science-with-ruby/stargazers)
section on the [Data Science with Ruby][ds-with-ruby] list.

## Articles, Posts, Talks, and Presentations

- 2022
  - _Discover Machine Learning in Ruby_ by [Justin Bowen](https://twitter.com/TonsOfFun111)
   <sup>[[video](https://www.youtube.com/watch?v=HPbizNgcyFk)]</sup>
- 2019
  - _TensorStream: Bringing Machine Learning to Ruby_ by [Joseph Emmanuel Dayo](https://www.linkedin.com/in/jdayo/)
    <sup>[[post](https://medium.com/@joseph.dayo/tensorstream-bringing-machine-learning-to-ruby-114582060e3d)]</sup>
  - _Easy machine learning with Ruby using SVMKit_ by [@kojix](https://twitter.com/kojix2dayo)
    <sup>[[post](https://dev.to/kojix2/easy-machine-learning-with-ruby-using-svmkit-4n86)]</sup>
- 2018
  - _Deep Learning Programming on Ruby_ by [Kenta Murata](https://twitter.com/mrkn)
    &amp; [Yusaku Hatanaka ](https://twitter.com/hatappi)
    <sup>[[slides](https://speakerdeck.com/mrkn/deep-learning-programming-on-ruby) |
          [page](https://rubykaigi.org/2018/presentations/mrkn.html)]</sup>
  - _How to use trained Keras and TensorFlow machine learning models within Ruby on Rails_ by [Denis Sellu](https://twitter.com/denis_sellu)
    <sup>[[post](https://www.cookieshq.co.uk/posts/how-to-use-trained-keras-and-tensorflow-machine-learning-models-within-ruby-on-rails)]</sup>
- 2017
  - _Scientific Computing on JRuby_ by [Prasun Anand](https://twitter.com/prasun_anand)
    <sup>[[slides](https://www.slideshare.net/PrasunAnand2/fosdem2017-scientific-computing-on-jruby) |
    [video](https://ftp.fau.de/fosdem/2017/K.4.201/ruby_scientific_computing_on_jruby.mp4) |
    [slides](https://www.slideshare.net/PrasunAnand2/scientific-computing-on-jruby) |
    [slides](https://www.slideshare.net/PrasunAnand2/scientific-computation-on-jruby)]</sup>
  - _Is it Food? An Introduction to Machine Learning_ by [Matthew Mongeau](https://twitter.com/halogenandtoast)
    <sup>[[video](https://www.youtube.com/watch?v=8G709hKkthY) |
          [slides](https://www.slideshare.net/halogenandtoast/is-it-food)]</sup>
  - _Bayes is BAE_ by [Richard Schneeman](https://twitter.com/schneems)
    <sup>[[video](https://www.youtube.com/watch?v=bQSzZrDDV80) |
          [slides](https://speakerdeck.com/schneems/bayes-is-bae)]</sup>
  - _Ruby Roundtable: Machine Learning in Ruby_ by [RubyThursday](https://rubythursday.com/)
    <sup>[[video](https://www.youtube.com/watch?v=ScIFARN0jCo)]</sup>
- 2016
  - _Practical Machine Learning with Ruby_ by [Jordan Hudgens](https://twitter.com/jordanhudgens)
    <sup>[[tutorial](https://www.crondose.com/2016/12/practical-machine-learning-ruby/)]</sup>
  - _Deep Learning: An Introduction for Ruby Developers_ by [Geoffrey Litt](https://twitter.com/geoffreylitt)
    <sup>[[slides](https://speakerdeck.com/geoffreylitt/deep-learning-an-introduction-for-ruby-developers)]</sup>
  - _How I made a pure-Ruby word2vec program more than 3x faster_ by [Kei Sawada](https://twitter.com/remore)
    <sup>[[slides](https://speakerdeck.com/remore/how-i-made-a-pure-ruby-word2vec-program-more-than-3x-faster)]</sup>
  - _Dōmo arigatō, Mr. Roboto: Machine Learning with Ruby_ by [Eric Weinstein](https://twitter.com/ericqweinstein)
    <sup>[[slides](https://speakerdeck.com/ericqweinstein/domo-arigato-mr-roboto-machine-learning-with-ruby) |
          [video](https://www.youtube.com/watch?v=T1nFQ49TyeA)]</sup>
  - _Building a Recommendation Engine with Machine Learning Techniques_ by [Brian Sam-Bodden](https://twitter.com/bsbodden)
    <sup>[[video](https://www.youtube.com/watch?v=SRnM_P_ygqI)]</sup>
  - :sparkles: _SciRuby Machine Learning: Current Status and Future_ by [Kenta Murata](https://twitter.com/mrkn)
    <sup>[[slides](https://speakerdeck.com/mrkn/sciruby-machine-learning-current-status-and-future) |
          [video: jp](https://www.youtube.com/watch?v=gfQ8XEy7vO4)]</sup>
  - _Ruby Roundtable: Intro to Tensorflow_ by [RubyThursday](https://rubythursday.com/)
    <sup>[[video](https://www.youtube.com/watch?v=pYC5mXHUWkc)]</sup>
- 2015
  - _Machine Learning made simple with Ruby_ by [Lorenzo Masini](https://twitter.com/rugginoso)
    <sup>[[post](https://www.leanpanda.com/blog/2015-08-24-machine-learning-automatic-classification/)]</sup>
  - _Using Ruby Machine Learning to Find Paris Hilton Quotes_ by [Rick Carlino](https://github.com/RickCarlino) [![GitHub stars](https://img.shields.io/github/stars/RickCarlino?style=flat)](https://github.com/RickCarlino/stargazers)
    <sup>[[tutorial](https://web.archive.org/web/20160414072324/http://datamelon.io/blog/2015/using-ruby-machine-learning-id-paris-hilton-quotes.html)]</sup>
- 2014
  - _Test Driven Neural Networks_ by [Matthew Kirk](https://twitter.com/mjkirk)
    <sup>[[video](https://www.youtube.com/watch?v=ppf8m-3uXvU&t=36s)]</sup>
  - _Five machine learning techniques that you can use in your Ruby apps today_ by [Benjamin Curtis](https://twitter.com/stympy)
    <sup>[[video](https://www.youtube.com/watch?v=crziu7dk6Vw) |
          [slides](https://speakerdeck.com/stympy/machine-learning-techniques)]</sup>
  - _Machine Learning for Fun and Profit_ by [John Paul Ashenfelter](https://twitter.com/johnashenfelter)
    <sup>[[video](https://www.youtube.com/watch?v=KC5MtKHm1O4)]</sup>
- 2013
  - _Sentiment Analysis using Support Vector Machines in Ruby_ by [Matthew Kirk](https://twitter.com/mjkirk)
    <sup>[[video](https://www.youtube.com/watch?v=iSug6CgxWxc) |
          [code](https://github.com/hexgnu/sentiment_analyzer) [![GitHub stars](https://img.shields.io/github/stars/hexgnu/sentiment_analyzer?style=flat)](https://github.com/hexgnu/sentiment_analyzer/stargazers)]</sup>
  - _Recommender Systems with Ruby_ by [Marcel Caraciolo](https://twitter.com/marcelcaraciolo)
    <sup>[[slides](https://www.slideshare.net/marcelcaraciolo/recommender-systems-with-ruby-adding-machine-learning-statistics-etc)]</sup>
  - _Detecting Faces with Ruby: FFI in a Nutshell_ by [Marc Berszick]()
    <sup>[[post](https://www.sitepoint.com/detecting-faces-with-ruby-ffi-in-a-nutshell/)]</sup>
- 2012
  - _Machine Learning with Ruby, Part One_ by [Vasily Vasinov](https://twitter.com/vasinov)
    <sup>[[tutorial](https://www.vasinov.com/blog/machine-learning-with-ruby-part-one/)]</sup>
  - _Recurrent Neural Networks in Ruby_ by [Joseph Wilk](https://twitter.com/josephwilk)
    <sup>[[post](http://blog.josephwilk.net/ruby/recurrent-neural-networks-in-ruby.html)]</sup>
  - _Recommendation Engines using Machine Learning, and JRuby_ by [Matthew Kirk](https://twitter.com/mjkirk)
    <sup>[[video](https://www.youtube.com/watch?v=hsZcrlbBg_0)]</sup>
  - _Practical Machine Learning and Rails_ by [Andrew Cantino](https://twitter.com/tectonic)
    and [Ryan Stout](https://twitter.com/ryanstout)
    <sup>[[video](https://www.youtube.com/watch?v=vy_zQ1-F0JI)]</sup>

- 2011
  - _Clustering in Ruby_ by [Colin Drake](https://twitter.com/colinfdrake)
    <sup>[[post](https://colindrake.me/post/k-means-clustering-in-ruby/)]</sup>
  - _Text Classification using Support Vector Machines in Ruby_ by [Rimas Silkaitis](https://twitter.com/neovintage)
    <sup>[[post](http://neovintage.org/2011/11/14/text-classification-using-support/)]</sup>
- 2010
  - _bayes_motel – Bayesian classification for Ruby_ by [Mike Perham](https://twitter.com/mperham)
    <sup>[[post](http://www.mikeperham.com/2010/04/28/bayes_motel-bayesian-classification-for-ruby/)]</sup>
  - _Intelligent Ruby: Getting Started with Machine Learning_ by [Ilya Grigorik](https://twitter.com/igrigorik)
    <sup>[[video](https://vimeo.com/22513786)]</sup>
- 2009

- 2008
  - _Support Vector Machines (SVM) in Ruby_ by [Ilya Grigorik](https://twitter.com/igrigorik)
    <sup>[[post](https://www.igvita.com/2008/01/07/support-vector-machines-svm-in-ruby/)]</sup>
- 2007
  - _Decision Tree Learning in Ruby_ by [Ilya Grigorik](https://twitter.com/igrigorik)
    <sup>[[post](https://www.igvita.com/2007/04/16/decision-tree-learning-in-ruby/)]</sup>

## Projects and Code Examples

- [Wine Clustering](https://github.com/hexgnu/wine_clustering) [![GitHub stars](https://img.shields.io/github/stars/hexgnu/wine_clustering?style=flat)](https://github.com/hexgnu/wine_clustering/stargazers) -
  Wine quality estimations clustered with different algorithms.
- [simple_ga](https://github.com/giuse/simple_ga) [![GitHub stars](https://img.shields.io/github/stars/giuse/simple_ga?style=flat)](https://github.com/giuse/simple_ga/stargazers) -
  Basic (working) demo of Genetic Algorithms in Ruby.
- [Handwritten Digits Recognition](https://github.com/jdrzj/handwritten-digits-recognition) [![GitHub stars](https://img.shields.io/github/stars/jdrzj/handwritten-digits-recognition?style=flat)](https://github.com/jdrzj/handwritten-digits-recognition/stargazers) -
  Handwritten digits recognition using Neural Networks and Ruby.

## Heroku buildpacks

- [GSL and Ruby buildpack](https://github.com/tomwolfe/heroku-buildpack-gsl-ruby) [![GitHub stars](https://img.shields.io/github/stars/tomwolfe/heroku-buildpack-gsl-ruby?style=flat)](https://github.com/tomwolfe/heroku-buildpack-gsl-ruby/stargazers)
- [OpenCV and Ruby buildpack](https://github.com/lilibethdlc/heroku-buildpack-ruby-opencv) [![GitHub stars](https://img.shields.io/github/stars/lilibethdlc/heroku-buildpack-ruby-opencv?style=flat)](https://github.com/lilibethdlc/heroku-buildpack-ruby-opencv/stargazers)
- [ImageMagick buildpack](https://github.com/mcollina/heroku-buildpack-imagemagick) [![GitHub stars](https://img.shields.io/github/stars/mcollina/heroku-buildpack-imagemagick?style=flat)](https://github.com/mcollina/heroku-buildpack-imagemagick/stargazers)

## Books, Blogs, Channels

-  [Kirk, Matthew](https://twitter.com/mjkirk).
   _Thoughtful Machine Learning: A Test-Driven Approach_. O'Reilly, 2014.
   <sup>[[Amazon](https://www.amazon.com/Thoughtful-Machine-Learning-Test-Driven-Approach/dp/1449374069) |
         [code](https://github.com/thoughtfulml/examples) [![GitHub stars](https://img.shields.io/github/stars/thoughtfulml/examples?style=flat)](https://github.com/thoughtfulml/examples/stargazers)]</sup>
- [Practical Artificial Intelligence](https://www.practicalai.io/) -
  Blog about Artificial Intelligence and Machine Learning with tutorials and code samples in Ruby.

## Community

- [SciRuby Mailing List](https://groups.google.com/forum/#!forum/sciruby-dev)
- [SciRuby Slack](https://sciruby.slack.com/)
- [Red Data Gitter](https://gitter.im/red-data-tools/)
- [Reddit](https://www.reddit.com/r/MachineLearning/search?q=Ruby&restrict_sr=on)
- [Stack Overflow](https://stackoverflow.com/search?q=machine+learning+ruby)
- [Twitter](https://twitter.com/search?q=Machine%20Learning%20Ruby&src=typd)
- [NonWebRuby](https://twitter.com/NonWebRuby)
- [Ruby AI Builders Discord](https://discord.gg/zDyFJFBTGB)
- [X Ruby AI group](https://twitter.com/i/communities/1709211359039078677)
- [Mastodon Ruby AI and Data group](https://ruby.social/@Ruby_AI_and_Data@chirp.social)

## Related Resources

- <a name="lightgbm"></a>
  [LightGBM](https://github.com/microsoft/LightGBM) [![GitHub stars](https://img.shields.io/github/stars/microsoft/LightGBM?style=flat)](https://github.com/microsoft/LightGBM/stargazers)
- <a name="xgboost"></a>
  [XGBoost](https://github.com/dmlc/xgboost) [![GitHub stars](https://img.shields.io/github/stars/dmlc/xgboost?style=flat)](https://github.com/dmlc/xgboost/stargazers)
- <a name="gls"></a>
  [GSL (GNU Scientific Library)][gls]
- <a name="opencv"></a>
  [OpenCV](https://opencv.org/)
- <a name="empty-lines-around-access-modifier"></a>
  [Graphviz](http://www.graphviz.org/)
- <a name="gnuplot"></a>
  [Gnuplot](http://www.gnuplot.info/)
- <a name="xquartz"></a>
  [X11/XQuartz](https://www.xquartz.org/)
- <a name="imagemagic"></a>
  [ImageMagick](https://www.imagemagick.org/script/index.php)
- <a name="r"></a>
  [R](http://www.r-project.org/)
- <a name="octave"></a>
  [Octave](https://www.gnu.org/software/octave/)
- [scikit-learn algorithm cheatsheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/)
- [Awesome Ruby](https://github.com/markets/awesome-ruby#natural-language-processing) [![GitHub stars](https://img.shields.io/github/stars/markets/awesome-ruby?style=flat)](https://github.com/markets/awesome-ruby/stargazers) -
  Among other awesome items a short list of NLP related projects.
- [Ruby NLP](https://github.com/diasks2/ruby-nlp) [![GitHub stars](https://img.shields.io/github/stars/diasks2/ruby-nlp?style=flat)](https://github.com/diasks2/ruby-nlp/stargazers) -
  State-of-Art collection of Ruby libraries for NLP.
- [Speech and Natural Language Processing](https://github.com/edobashira/speech-language-processing) [![GitHub stars](https://img.shields.io/github/stars/edobashira/speech-language-processing?style=flat)](https://github.com/edobashira/speech-language-processing/stargazers) -
  General List of NLP related resources (mostly not for Ruby programmers).
- [Scientific Ruby](http://sciruby.com/) -
  Linear Algebra, Visualization and Scientific Computing for Ruby.
- [iRuby](https://github.com/SciRuby/iruby) [![GitHub stars](https://img.shields.io/github/stars/SciRuby/iruby?style=flat)](https://github.com/SciRuby/iruby/stargazers) - IRuby kernel for Jupyter (formerly IPython).
- [Kiba](https://github.com/thbar/kiba) [![GitHub stars](https://img.shields.io/github/stars/thbar/kiba?style=flat)](https://github.com/thbar/kiba/stargazers) -
  Lightweight [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) (Extract, Transform, Load) pipeline.
- [Awesome OCR](https://github.com/kba/awesome-ocr) [![GitHub stars](https://img.shields.io/github/stars/kba/awesome-ocr?style=flat)](https://github.com/kba/awesome-ocr/stargazers) -
  Multitude of OCR (Optical Character Recognition) resources.
- [Awesome TensorFlow](https://github.com/jtoy/awesome-tensorflow) [![GitHub stars](https://img.shields.io/github/stars/jtoy/awesome-tensorflow?style=flat)](https://github.com/jtoy/awesome-tensorflow/stargazers) -
  Machine Learning with TensorFlow libraries.
- [rb-gsl](https://github.com/SciRuby/rb-gsl) [![GitHub stars](https://img.shields.io/github/stars/SciRuby/rb-gsl?style=flat)](https://github.com/SciRuby/rb-gsl/stargazers) -
  Ruby interface to the [GNU Scientific Library](https://www.gnu.org/software/gsl/).
- [The Definitive Guide to Ruby's C API](https://silverhammermba.github.io/emberb/) -
  Modern Reference and Tutorial on Embedding and Extending Ruby using C programming language.

## License

[![Creative Commons Zero 1.0](http://mirrors.creativecommons.org/presskit/buttons/80x15/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
`Awesome ML with Ruby` by [Andrei Beliankou](https://github.com/arbox) [![GitHub stars](https://img.shields.io/github/stars/arbox?style=flat)](https://github.com/arbox/stargazers) and
[Contributors][contributors].

To the extent possible under law, the person who associated CC0 with
`Awesome ML with Ruby` has waived all copyright and related or neighboring rights
to `Awesome ML with Ruby`.

You should have received a copy of the CC0 legalcode along with this
work. If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.

<!--- Links --->
[ruby]: https://www.ruby-lang.org/en/
[awesome]: https://github.com/sindresorhus/awesome/blob/master/awesome.md
[change-pr]: https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md
[ml]: https://en.wikipedia.org/wiki/Machine_learning
[ds-with-ruby]: https://github.com/arbox/data-science-with-ruby
[contributors]: https://github.com/arbox/machine-learning-with-ruby/graphs/contributors
[sciruby]: https://github.com/sciruby
[ai]: https://en.wikipedia.org/wiki/Artificial_intelligence
[cs]: https://en.wikipedia.org/wiki/Computational_science
[fe]: https://en.wikipedia.org/wiki/Feature_engineering
[ts]: https://en.wikipedia.org/wiki/Test_set
[gsl]: https://www.gnu.org/software/gsl/
[scikit]: https://scikit-learn.org/stable/index.html
