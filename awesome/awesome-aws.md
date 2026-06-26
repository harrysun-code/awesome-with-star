# Amazon Web Services

[![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws?style=flat)](https://github.com/donnemartin/awesome-aws/stargazers)

<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/aws.png">
</p>
<br/>

# Awesome AWS [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome AWS libraries, open source repos, guides, blogs, and other resources.

Inspired by the [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) list.

## The Fiery Meter of AWSome

* Repo with 0100+ Stars: :fire:
* Repo with 0200+ Stars: :fire::fire:
* Repo with 0500+ Stars: :fire::fire::fire:
* Repo with 1000+ Stars: :fire::fire::fire::fire:
* Repo with 2000+ Stars: :fire::fire::fire::fire::fire:

Repos not on `The Fiery Meter of AWSome` can still be awesome, see [A Note on Repo AWSomeness](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md#a-note-on-repo-awsomeness).

### `awesome-aws` Python Module

[![Build Status](https://travis-ci.org/donnemartin/awesome-aws.svg?branch=master)](https://travis-ci.org/donnemartin/awesome-aws) [![Codecov](https://img.shields.io/codecov/c/github/donnemartin/awesome-aws.svg)](https://codecov.io/github/donnemartin/awesome-aws) [![PyPI version](https://badge.fury.io/py/awesome-aws.svg)](http://badge.fury.io/py/awesome-aws)

The Python module [`awesome-aws`](https://github.com/donnemartin/awesome-aws/tree/master/awesome) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/tree/master/awesome?style=flat)](https://github.com/donnemartin/awesome-aws/tree/master/awesome/stargazers) regularly scans repos on [Awesome AWS](https://github.com/donnemartin/awesome-aws) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws?style=flat)](https://github.com/donnemartin/awesome-aws/stargazers) to maintain the accuracy of the `Fiery Meter of AWSome`.

## Contributing

Contributions are welcome!

Review the [Contributing Guidelines](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers).

Also check out the [Watch List](https://github.com/donnemartin/awesome-aws/issues/34) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/issues/34?style=flat)](https://github.com/donnemartin/awesome-aws/issues/34/stargazers).

## Index

* [SDKs and Samples](#sdks-and-samples)
    * [Android](#android-sdk)
    * [C++](#c-sdk)
    * [Clojure](#clojure-sdk)
    * [Go](#go-sdk)
    * [iOS](#ios-sdk)
    * [IoT](#iot-sdk)
    * [Java](#java-sdk)
    * [JavaScript](#javascript-sdk)
    * [Haskell](#haskell-sdk)
    * [Perl](#perl-sdk)
    * [PHP](#php-sdk)
    * [Python](#python-sdk)
    * [Ruby](#ruby-sdk)
    * [Rust](#rust-sdk)
    * [Scala](#scala-sdk)
    * [Xamarin](#xamarin-sdk)
    * [Unity](#unity-sdk)
    * [.NET](#net-sdk)
* [Command Line Tools](#command-line-tools)
    * [Universal Command Line Interface](#universal-command-line-interface)
    * [Windows PowerShell](#windows-powershell)
* [IDE Toolkits](#ide-toolkits)
    * [Eclipse Toolkit](#eclipse-toolkit)
    * [Visual Studio Toolkit](#visual-studio-toolkit)
* [Open Source Repos](#open-source-repos)
    * [API Gateway](#api-gateway)
    * [CLI](#cli)
    * [CloudFormation](#cloudformation)
    * [CloudSearch](#cloudsearch)
    * [CloudTrail](#cloudtrail)
    * [CloudWatch](#cloudwatch)
    * [Code Deploy](#code-deploy)
    * [Code Pipeline](#code-pipeline)
    * [Cognito](#cognito)
    * [Data Pipeline](#data-pipeline)
    * [Device Farm](#device-farm)
    * [DynamoDB](#dynamodb)
    * [Elastic Beanstalk](#elastic-beanstalk)
    * [Elastic Container Service](#elastic-container-service)
    * [Elastic File System](#elastic-file-system)
    * [Elastic MapReduce](#elastic-mapreduce)
    * [Elastic Search](#elastic-search)
    * [Elasticache](#elasticache)
    * [Glacier](#glacier)
    * [Kinesis](#kinesis)
    * [Lambda](#lambda)
    * [Machine Learning](#machine-learning)
    * [Mobile Analytics](#mobile-analytics)
    * [OpsWorks](#opsworks)
    * [Redshift](#redshift)
    * [Route 53](#route-53)
    * [S3](#s3)
    * [SNS](#sns)
    * [SQS](#sqs)
    * [Data](#data)
    * [DevOps](#devops)
    * [Security](#security)
    * [Accompanying](#accompanying-repos)
    * [Miscellaneous](#miscellaneous-repos)
* [Guides, Books, Documentation, and Training](#guides-books-documentation-and-training)
    * [Getting Started Guides](#getting-started-guides)
    * [General Guides](#general-guides)
    * [Books](#books)
    * [Whitepapers](#whitepapers)
    * [Documentation](#documentation)
    * [Training](#training)
    * [Case Studies: Powered by AWS](#case-studies-powered-by-aws)
* [Social](#social)
    * [Blogs](#blogs)
    * [Twitter Influencers](#twitter-influencers)
    * [Facebook Pages](#facebook-pages)
    * [YouTube Channels](#youtube-channels)
    * [LinkedIn Groups](#linkedin-groups)
    * [Subreddits](#subreddits)
    * [Conferences](#conferences)
* [Latest KPIs and Stats](#latest-kpis-and-stats)
* [Appendix of Core Services](#appendix-of-core-services)
    * [Services in Plain English](#services-in-plain-english)
    * [Compute](#compute-services)
    * [Networking](#networking-services)
    * [Enterprise Applications](#enterprise-applications)
    * [Analytics](#analytics-services)
    * [Artificial Intelligence](#artificial-intelligence)
    * [Management Tools](#management-tools)
    * [Security and Identity](#security-and-identity-services)
    * [Internet of Things](#internet-of-things-service)
    * [Mobile Services](#mobile-services)
    * [Storage and Content Delivery](#storage-and-content-delivery-services)
    * [Databases](#databases)
    * [Application Services](#application-services)
    * [Developer Tools](#developer-tools)
    * [Miscellaneous Services](#miscellaneous-services)
* [Contributing](#contributing)
* [Credits](#credits)
* [Other Awesome Lists](#other-awesome-lists)
* [Contact Info](#contact-info)
* [License](#license)

## SDKs and Samples

*AWS and community SDKs with samples and docs, grouped by language.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/TK96G8T.png">
</p>
<br/>

### Android SDK

* [Repo :fire::fire::fire:](https://github.com/aws/aws-sdk-android) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-android?style=flat)](https://github.com/aws/aws-sdk-android/stargazers)
* [Repo with Samples :fire::fire::fire:](https://github.com/awslabs/aws-sdk-android-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-android-samples?style=flat)](https://github.com/awslabs/aws-sdk-android-samples/stargazers)
* [Install](http://sdk-for-android.amazonwebservices.com/latest/aws-android-sdk.zip)
* [Docs](https://aws.amazon.com/documentation/sdk-for-android/)
* [Learn More](https://aws.amazon.com/mobile/sdk/)

### C++ SDK

* [Repo :fire::fire::fire::fire:](https://github.com/awslabs/aws-sdk-cpp) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-cpp?style=flat)](https://github.com/awslabs/aws-sdk-cpp/stargazers)
* [Blog with Samples](https://aws.amazon.com/blogs/aws/introducing-the-aws-sdk-for-c/)

*The C++ SDK is a labs project with limited docs and/or samples.*

### Clojure SDK

* [Repo :fire::fire::fire:](https://github.com/mcohen01/amazonica) [![GitHub stars](https://img.shields.io/github/stars/mcohen01/amazonica?style=flat)](https://github.com/mcohen01/amazonica/stargazers)
* [Install](https://github.com/mcohen01/amazonica#installation)
* [Docs](https://github.com/mcohen01/amazonica#documentation)

*The Clojure SDK is a community project with limited docs and/or samples.*)

### Go SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-go) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-go?style=flat)](https://github.com/aws/aws-sdk-go/stargazers)
* [Install](https://github.com/aws/aws-sdk-go/wiki) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-go/wiki?style=flat)](https://github.com/aws/aws-sdk-go/wiki/stargazers)
* [Docs](http://docs.aws.amazon.com/sdk-for-go/api/)
* [Learn More](https://aws.amazon.com/sdk-for-go/)

Related Repos:

* [goamz/goamz :fire::fire:](https://github.com/goamz/goamz) [![GitHub stars](https://img.shields.io/github/stars/goamz/goamz?style=flat)](https://github.com/goamz/goamz/stargazers)

### iOS SDK

* [Repo :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-ios) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-ios?style=flat)](https://github.com/aws/aws-sdk-ios/stargazers)
* [Repo with Samples :fire::fire::fire::fire:](https://github.com/awslabs/aws-sdk-ios-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-ios-samples?style=flat)](https://github.com/awslabs/aws-sdk-ios-samples/stargazers)
* [Install](http://sdk-for-ios.amazonwebservices.com/latest/aws-ios-sdk.zip)
* [Docs](https://aws.amazon.com/documentation/sdk-for-ios/)
* [Learn More](https://aws.amazon.com/mobile/sdk/)

### IoT SDK

* [Repo for Arduino](https://github.com/awslabs/aws-sdk-arduino) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-arduino?style=flat)](https://github.com/awslabs/aws-sdk-arduino/stargazers)
* [Repo for C :fire::fire::fire:](https://github.com/aws/aws-iot-device-sdk-embedded-C) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-iot-device-sdk-embedded-C?style=flat)](https://github.com/aws/aws-iot-device-sdk-embedded-C/stargazers)
* [Repo for JavaScript :fire::fire::fire:](https://github.com/aws/aws-iot-device-sdk-js) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-iot-device-sdk-js?style=flat)](https://github.com/aws/aws-iot-device-sdk-js/stargazers)
* [Repo for Arduino Yun :fire:](https://github.com/aws/aws-iot-device-sdk-arduino-yun/) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-iot-device-sdk-arduino-yun/?style=flat)](https://github.com/aws/aws-iot-device-sdk-arduino-yun//stargazers)
* [Docs](http://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

*The IoT SDK is a labs project with limited docs and/or samples.*

### Java SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-java) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-java?style=flat)](https://github.com/aws/aws-sdk-java/stargazers)
* [Repo with Samples :fire::fire:](https://github.com/awslabs/aws-java-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-java-sample?style=flat)](https://github.com/awslabs/aws-java-sample/stargazers)
* [Install](http://sdk-for-java.amazonwebservices.com/latest/aws-java-sdk.zip)
* [Docs](https://aws.amazon.com/documentation/sdk-for-java/)
* [Learn More](https://aws.amazon.com/sdk-for-java/)

### JavaScript SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-js) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-js?style=flat)](https://github.com/aws/aws-sdk-js/stargazers)
* [Repo with Samples :fire::fire:](https://github.com/awslabs/aws-nodejs-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-nodejs-sample?style=flat)](https://github.com/awslabs/aws-nodejs-sample/stargazers)
* [Install](http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-intro.html)
* [Docs](https://aws.amazon.com/documentation/sdk-for-javascript/)
* [Learn More](https://aws.amazon.com/sdk-for-node-js/)

Related Repos:

* [aws/aws-amplify :fire::fire::fire::fire::fire:](https://github.com/aws/aws-amplify) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-amplify?style=flat)](https://github.com/aws/aws-amplify/stargazers)
* [chilts/awssum :fire::fire:](https://github.com/chilts/awssum) [![GitHub stars](https://img.shields.io/github/stars/chilts/awssum?style=flat)](https://github.com/chilts/awssum/stargazers)
* [mirkokiefer/aws-lib :fire::fire::fire:](https://github.com/mirkokiefer/aws-lib) [![GitHub stars](https://img.shields.io/github/stars/mirkokiefer/aws-lib?style=flat)](https://github.com/mirkokiefer/aws-lib/stargazers)
* [SaltwaterC/aws2js :fire::fire:](https://github.com/SaltwaterC/aws2js) [![GitHub stars](https://img.shields.io/github/stars/SaltwaterC/aws2js?style=flat)](https://github.com/SaltwaterC/aws2js/stargazers)

### Haskell SDK

* [Repo :fire::fire::fire:](https://github.com/brendanhay/amazonka) [![GitHub stars](https://img.shields.io/github/stars/brendanhay/amazonka?style=flat)](https://github.com/brendanhay/amazonka/stargazers)
* [Docs](http://hackage.haskell.org/packages/#cat:AWS)

Related Repos:

* [aristidb/aws :fire::fire:](https://github.com/aristidb/aws) [![GitHub stars](https://img.shields.io/github/stars/aristidb/aws?style=flat)](https://github.com/aristidb/aws/stargazers)

*The Haskell SDK is a community project with limited docs and/or samples.*

### Perl SDK

* [Repo :fire:](https://github.com/pplu/aws-sdk-perl) [![GitHub stars](https://img.shields.io/github/stars/pplu/aws-sdk-perl?style=flat)](https://github.com/pplu/aws-sdk-perl/stargazers)
* [Repo with Samples :fire:](https://github.com/pplu/aws-sdk-perl/tree/master/examples) [![GitHub stars](https://img.shields.io/github/stars/pplu/aws-sdk-perl/tree/master/examples?style=flat)](https://github.com/pplu/aws-sdk-perl/tree/master/examples/stargazers)
* [Install](https://github.com/pplu/aws-sdk-perl#installation)
* [Docs](https://metacpan.org/pod/Paws)
* [Learn More](https://metacpan.org/pod/Paws)

*The Perl SDK is a community project.*

### PHP SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-php) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-php?style=flat)](https://github.com/aws/aws-sdk-php/stargazers)
* [Repo with Samples](https://github.com/awslabs/aws-php-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-php-sample?style=flat)](https://github.com/awslabs/aws-php-sample/stargazers)
* [Install](http://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html)
* [Docs](https://aws.amazon.com/documentation/sdk-for-php/)
* [Learn More](https://aws.amazon.com/sdk-for-php/)

Related Repos:

* [aws-sdk-php-laravel :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-php-laravel) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-php-laravel?style=flat)](https://github.com/aws/aws-sdk-php-laravel/stargazers)
* [aws-sdk-php-silex](https://github.com/aws/aws-sdk-php-silex) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-php-silex?style=flat)](https://github.com/aws/aws-sdk-php-silex/stargazers)
* [aws-sdk-php-zf2 :fire:](https://github.com/aws/aws-sdk-php-zf2) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-php-zf2?style=flat)](https://github.com/aws/aws-sdk-php-zf2/stargazers)

### Python SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/boto/boto3) [![GitHub stars](https://img.shields.io/github/stars/boto/boto3?style=flat)](https://github.com/boto/boto3/stargazers)
* [Repo with Samples :fire:](https://github.com/awslabs/aws-python-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-python-sample?style=flat)](https://github.com/awslabs/aws-python-sample/stargazers)
* [Install](http://github.com/boto/boto#installation)
* [Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [Learn More](http://github.com/boto/boto/blob/develop/README.rst#boto)

Related Repos:

* [boto3 :fire::fire::fire::fire::fire:](https://github.com/boto/boto3) [![GitHub stars](https://img.shields.io/github/stars/boto/boto3?style=flat)](https://github.com/boto/boto3/stargazers)
* [botocore :fire::fire::fire::fire:](https://github.com/boto/botocore) [![GitHub stars](https://img.shields.io/github/stars/boto/botocore?style=flat)](https://github.com/boto/botocore/stargazers)

### Ruby SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-sdk-ruby) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-ruby?style=flat)](https://github.com/aws/aws-sdk-ruby/stargazers)
* [Repo with S3 Sample](https://github.com/awslabs/aws-ruby-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-ruby-sample?style=flat)](https://github.com/awslabs/aws-ruby-sample/stargazers)
* [Install](http://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-install.html)
* [Docs](https://aws.amazon.com/documentation/sdk-for-ruby/)
* [Samples :fire::fire::fire::fire::fire:](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/ruby/example_code/) [![GitHub stars](https://img.shields.io/github/stars/awsdocs/aws-doc-sdk-examples/tree/master/ruby/example_code/?style=flat)](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/ruby/example_code//stargazers)

Related Repos:

* [aws-sdk-rails :fire::fire::fire:](https://github.com/aws/aws-sdk-rails) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-rails?style=flat)](https://github.com/aws/aws-sdk-rails/stargazers)
* [appoxy/aws :fire::fire:](https://github.com/appoxy/aws) [![GitHub stars](https://img.shields.io/github/stars/appoxy/aws?style=flat)](https://github.com/appoxy/aws/stargazers)
* [rightscale/right_aws :fire::fire:](https://github.com/rightscale/right_aws) [![GitHub stars](https://img.shields.io/github/stars/rightscale/right_aws?style=flat)](https://github.com/rightscale/right_aws/stargazers)

### Rust SDK

* [Repo :fire::fire::fire::fire::fire:](https://github.com/rusoto/rusoto) [![GitHub stars](https://img.shields.io/github/stars/rusoto/rusoto?style=flat)](https://github.com/rusoto/rusoto/stargazers)
* [Install](https://github.com/rusoto/rusoto#installation)
* [Docs](https://docs.rs/rusoto_core/)

*The Rust SDK is a community project with limited docs and/or samples.*

### Scala SDK

* [Repo](https://github.com/awslabs/aws-scala-sdk) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-scala-sdk?style=flat)](https://github.com/awslabs/aws-scala-sdk/stargazers)

Related Repos:

* [atlassian/aws-scala](https://bitbucket.org/atlassian/aws-scala)
* [seratch/AWScala :fire::fire::fire:](https://github.com/seratch/AWScala) [![GitHub stars](https://img.shields.io/github/stars/seratch/AWScala?style=flat)](https://github.com/seratch/AWScala/stargazers)

*The Scala SDK is a labs project with limited docs and/or samples.*

### Unity SDK

* [Repo :fire:](https://github.com/aws/aws-sdk-unity) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-unity?style=flat)](https://github.com/aws/aws-sdk-unity/stargazers)
* [Repo with Samples :fire:](https://github.com/awslabs/aws-sdk-unity-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-unity-samples?style=flat)](https://github.com/awslabs/aws-sdk-unity-samples/stargazers)
* [Install](https://s3.amazonaws.com/aws-unity-sdk/latest/aws-unity-sdk.zip)
* [Docs](http://docs.aws.amazon.com/mobile/sdkforunity/developerguide/)

### Xamarin SDK

* [Repo](https://github.com/awslabs/aws-sdk-xamarin) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-xamarin?style=flat)](https://github.com/awslabs/aws-sdk-xamarin/stargazers)
* [Blog with Samples](https://blog.xamarin.com/amazon-web-services-aws-mobile-sdks-for-xamarin-now-available/)

*The Xamarin SDK is a labs project with limited docs and/or samples.*

### .NET SDK

* [Repo :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-net) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-net?style=flat)](https://github.com/aws/aws-sdk-net/stargazers)
* [Repo with Samples](https://github.com/awslabs/aws-auto-scaling-console-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-auto-scaling-console-sample?style=flat)](https://github.com/awslabs/aws-auto-scaling-console-sample/stargazers)
* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* [Docs](https://aws.amazon.com/documentation/sdk-for-net/)
* [Learn More](https://aws.amazon.com/sdk-for-net/)
* [Samples :fire:](https://github.com/awslabs/aws-sdk-net-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-net-samples?style=flat)](https://github.com/awslabs/aws-sdk-net-samples/stargazers)

## Command Line Tools

*AWS and community command line tools with samples and docs.*

<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/commands.png">
</p>
<br/>

### Universal Command Line Interface

* [Repo :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cli) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-cli?style=flat)](https://github.com/aws/aws-cli/stargazers)
* [Install](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)
* [Docs](https://aws.amazon.com/documentation/cli/)
* [Learn More](https://aws.amazon.com/cli/)

Related Repos:

* [awslabs/aws-shell :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-shell) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-shell?style=flat)](https://github.com/awslabs/aws-shell/stargazers)
* [donnemartin/saws :fire::fire::fire::fire::fire:](https://github.com/donnemartin/saws) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/saws?style=flat)](https://github.com/donnemartin/saws/stargazers)

### Windows PowerShell

* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* [Docs](https://aws.amazon.com/documentation/powershell/)
* [Learn More](https://aws.amazon.com/powershell/)

## IDE Toolkits

*Official IDE toolkits with samples and docs.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/x4nu914.png">
</p>
<br/>

### Eclipse Toolkit

* [Install](http://docs.aws.amazon.com/AWSToolkitEclipse/latest/ug/tke_setup.html)
* [Docs](https://aws.amazon.com/documentation/awstoolkiteclipse/)
* [Learn More](https://aws.amazon.com/eclipse/)

### Visual Studio Toolkit

* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* [Docs](https://aws.amazon.com/documentation/aws-toolkit-visual-studio/)
* [Learn More](https://aws.amazon.com/visualstudio/)

## Open Source Repos

*AWS and community open source projects, grouped by service.  See [A Note on Repo AWSomeness](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md#a-note-on-repo-awsomeness) for more details.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/wbhTgga.png">
</p>
<br/>

### API Gateway

AWS Repos:

* [api-gateway-secure-pet-store :fire::fire:](https://github.com/awslabs/api-gateway-secure-pet-store) [![GitHub stars](https://img.shields.io/github/stars/awslabs/api-gateway-secure-pet-store?style=flat)](https://github.com/awslabs/api-gateway-secure-pet-store/stargazers) - Cognito credentials through Lambda.
* [aws-apigateway-sdk-java](https://github.com/awslabs/aws-apigateway-sdk-java) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-apigateway-sdk-java?style=flat)](https://github.com/awslabs/aws-apigateway-sdk-java/stargazers) - SDK for Java.
* [aws-apigateway-swagger-importer :fire::fire::fire:](https://github.com/awslabs/aws-apigateway-importer) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-apigateway-importer?style=flat)](https://github.com/awslabs/aws-apigateway-importer/stargazers) - Tools to work with Swagger.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### CLI

AWS Repos:

* [awscli-aliases :fire::fire:](https://github.com/awslabs/awscli-aliases) [![GitHub stars](https://img.shields.io/github/stars/awslabs/awscli-aliases?style=flat)](https://github.com/awslabs/awscli-aliases/stargazers) - Repository for AWS CLI aliases.
* [amazon-ecs-cli :fire::fire::fire::fire:](https://github.com/aws/amazon-ecs-cli) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-ecs-cli?style=flat)](https://github.com/aws/amazon-ecs-cli/stargazers) - ECS CLI using the same Docker Compose file format and familiar Compose commands.
* [aws-cli :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cli) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-cli?style=flat)](https://github.com/aws/aws-cli/stargazers) - Universal Command Line Interface.
* [aws-shell :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-shell) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-shell?style=flat)](https://github.com/awslabs/aws-shell/stargazers)
* [awscli-cookbook](https://github.com/awslabs/awscli-cookbook) [![GitHub stars](https://img.shields.io/github/stars/awslabs/awscli-cookbook?style=flat)](https://github.com/awslabs/awscli-cookbook/stargazers) - Installs the CLI tools and provides a set of LWRPs for use within chef cookbooks.
* [awsmobile-cli :fire:](https://github.com/aws/awsmobile-cli) [![GitHub stars](https://img.shields.io/github/stars/aws/awsmobile-cli?style=flat)](https://github.com/aws/awsmobile-cli/stargazers) - CLI experience for Frontend developers in the JavaScript ecosystem.

Community Repos:

* [achiku/jungle :fire::fire::fire:](https://github.com/achiku/jungle) [![GitHub stars](https://img.shields.io/github/stars/achiku/jungle?style=flat)](https://github.com/achiku/jungle/stargazers) - Operations by EC2 and ELB cli should be simpler.
* [dbcli/athenacli :fire:](https://github.com/dbcli/athenacli) [![GitHub stars](https://img.shields.io/github/stars/dbcli/athenacli?style=flat)](https://github.com/dbcli/athenacli/stargazers) - a CLI tool for AWS Athena service that can do auto-completion and syntax highlighting.
* [donnemartin/saws :fire::fire::fire::fire::fire:](https://github.com/donnemartin/saws) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/saws?style=flat)](https://github.com/donnemartin/saws/stargazers) - A Supercharged AWS Command Line Interface.
* [timkay/aws :fire::fire:](https://github.com/timkay/aws) [![GitHub stars](https://img.shields.io/github/stars/timkay/aws?style=flat)](https://github.com/timkay/aws/stargazers) - Easy command line access to Amazon EC2, S3, SQS, ELB, and SDB.
* [wallix/awless :fire::fire::fire::fire::fire:](https://github.com/wallix/awless) [![GitHub stars](https://img.shields.io/github/stars/wallix/awless?style=flat)](https://github.com/wallix/awless/stargazers) - a Powerful CLI for EC2, IAM and S3 in Go.
* [99designs/aws-vault :fire::fire::fire::fire::fire:](https://github.com/99designs/aws-vault) [![GitHub stars](https://img.shields.io/github/stars/99designs/aws-vault?style=flat)](https://github.com/99designs/aws-vault/stargazers) - A tool for securely storing AWS credentials, written in Go.

### CloudFormation

AWS Repos:

* [aws-cdk :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cdk) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-cdk?style=flat)](https://github.com/aws/aws-cdk/stargazers) - Framework for defining cloud infrastructure in code.
* [aws-cfn-custom-resource-examples](https://github.com/awslabs/aws-cfn-custom-resource-examples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-cfn-custom-resource-examples?style=flat)](https://github.com/awslabs/aws-cfn-custom-resource-examples/stargazers) - Custom resource examples.
* [aws-cfn-resource-bridge](https://github.com/aws/aws-cfn-resource-bridge) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-cfn-resource-bridge?style=flat)](https://github.com/aws/aws-cfn-resource-bridge/stargazers) - Custom resource framework.
* [cfn-python-lint :fire::fire::fire::fire::fire:](https://github.com/awslabs/cfn-python-lint) [![GitHub stars](https://img.shields.io/github/stars/awslabs/cfn-python-lint?style=flat)](https://github.com/awslabs/cfn-python-lint/stargazers) - A tool for linting/validating CloudFormation.
* [cfncluster-cookbook](https://github.com/awslabs/cfncluster-cookbook) [![GitHub stars](https://img.shields.io/github/stars/awslabs/cfncluster-cookbook?style=flat)](https://github.com/awslabs/cfncluster-cookbook/stargazers) - Sample Cookbook.
* [cfncluster :fire::fire::fire:](https://github.com/awslabs/cfncluster) [![GitHub stars](https://img.shields.io/github/stars/awslabs/cfncluster?style=flat)](https://github.com/awslabs/cfncluster/stargazers) - Framework that deploys and maintains HPC clusters.

Community Repos:

* [Appliscale/perun](https://github.com/Appliscale/perun) [![GitHub stars](https://img.shields.io/github/stars/Appliscale/perun?style=flat)](https://github.com/Appliscale/perun/stargazers) - A CLI tool for linting/validation and managing CloudFormation templates and stacks.
* [bazaarvoice/cloudformation-ruby-dsl :fire::fire:](https://github.com/bazaarvoice/cloudformation-ruby-dsl) [![GitHub stars](https://img.shields.io/github/stars/bazaarvoice/cloudformation-ruby-dsl?style=flat)](https://github.com/bazaarvoice/cloudformation-ruby-dsl/stargazers) - Ruby DSL for creating templates.
* [beaknit/cform :fire:](https://github.com/beaknit/cform) [![GitHub stars](https://img.shields.io/github/stars/beaknit/cform?style=flat)](https://github.com/beaknit/cform/stargazers) - SublimeText plugin.
* [cloudreach/sceptre :fire::fire::fire::fire:](https://github.com/cloudreach/sceptre) [![GitHub stars](https://img.shields.io/github/stars/cloudreach/sceptre?style=flat)](https://github.com/cloudreach/sceptre/stargazers) - A CLI tool for automating CloudFormation.
* [cloudtools/troposphere :fire::fire::fire::fire::fire:](https://github.com/cloudtools/troposphere) [![GitHub stars](https://img.shields.io/github/stars/cloudtools/troposphere?style=flat)](https://github.com/cloudtools/troposphere/stargazers) - Python library to create descriptions.
* [peterkh/cumulus :fire::fire:](https://github.com/peterkh/cumulus) [![GitHub stars](https://img.shields.io/github/stars/peterkh/cumulus?style=flat)](https://github.com/peterkh/cumulus/stargazers) - Manages stacks.
* [envato/stack_master :fire::fire:](https://github.com/envato/stack_master) [![GitHub stars](https://img.shields.io/github/stars/envato/stack_master?style=flat)](https://github.com/envato/stack_master/stargazers) - A CLI tool to manage CloudFormation stacks.
* [sparkleformation/sfn](https://github.com/sparkleformation/sfn) [![GitHub stars](https://img.shields.io/github/stars/sparkleformation/sfn?style=flat)](https://github.com/sparkleformation/sfn/stargazers) - CLI for stack management.
* [sparkleformation/sparkle_formation :fire::fire:](https://github.com/sparkleformation/sparkle_formation) [![GitHub stars](https://img.shields.io/github/stars/sparkleformation/sparkle_formation?style=flat)](https://github.com/sparkleformation/sparkle_formation/stargazers) - Ruby DSL for template creation.
* [Stelligent/cfn_nag :fire::fire::fire::fire:](https://github.com/stelligent/cfn_nag) [![GitHub stars](https://img.shields.io/github/stars/stelligent/cfn_nag?style=flat)](https://github.com/stelligent/cfn_nag/stargazers) - Linting tool for CloudFormation templates

### CloudSearch

AWS Repos:

* [cloudsearchable](https://github.com/awslabs/cloudsearchable) [![GitHub stars](https://img.shields.io/github/stars/awslabs/cloudsearchable?style=flat)](https://github.com/awslabs/cloudsearchable/stargazers) - An ActiveRecord-style ORM query interface.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### CloudTrail

AWS Repos:

* [aws-cloudtrail-processing-library](https://github.com/aws/aws-cloudtrail-processing-library) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-cloudtrail-processing-library?style=flat)](https://github.com/aws/aws-cloudtrail-processing-library/stargazers) - Easily consume and process log files.

Community Repos:

* [AppliedTrust/traildash :fire::fire:](https://github.com/AppliedTrust/traildash) [![GitHub stars](https://img.shields.io/github/stars/AppliedTrust/traildash?style=flat)](https://github.com/AppliedTrust/traildash/stargazers) - Slick dashboard.
* [GorillaStack/auto-tag :fire::fire:](https://github.com/GorillaStack/auto-tag) [![GitHub stars](https://img.shields.io/github/stars/GorillaStack/auto-tag?style=flat)](https://github.com/GorillaStack/auto-tag/stargazers) - Automatically tag AWS resources on creation, for cost assignment.

### CloudWatch

AWS Repos:

* [cloudwatch-logs-subscription-consumer :fire::fire:](https://github.com/awslabs/cloudwatch-logs-subscription-consumer) [![GitHub stars](https://img.shields.io/github/stars/awslabs/cloudwatch-logs-subscription-consumer?style=flat)](https://github.com/awslabs/cloudwatch-logs-subscription-consumer/stargazers) - Kinesis stream reader.
* [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-cloudwatch-logs?style=flat)](https://github.com/awslabs/ecs-cloudwatch-logs/stargazers) - Assets in the blog post on using Amazon ECS and Amazon CloudWatch logs.
* [logstash-output-cloudwatchlogs](https://github.com/awslabs/logstash-output-cloudwatchlogs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/logstash-output-cloudwatchlogs?style=flat)](https://github.com/awslabs/logstash-output-cloudwatchlogs/stargazers) - A logstash plugin that sends logs to CloudWatch.
* [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-cloudwatch-logs-cookbooks?style=flat)](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks/stargazers) - OpsWorks sample cookbook.

Community Repos:

* [jorgebastida/awslogs :fire::fire::fire::fire::fire:](https://github.com/jorgebastida/awslogs) [![GitHub stars](https://img.shields.io/github/stars/jorgebastida/awslogs?style=flat)](https://github.com/jorgebastida/awslogs/stargazers) - Simple CLI for querying groups, streams and events.
* [newrelic-platform/newrelic_aws_cloudwatch_plugin :fire:](https://github.com/newrelic-platform/newrelic_aws_cloudwatch_plugin) [![GitHub stars](https://img.shields.io/github/stars/newrelic-platform/newrelic_aws_cloudwatch_plugin?style=flat)](https://github.com/newrelic-platform/newrelic_aws_cloudwatch_plugin/stargazers) - New Relic plugin.

### Code Deploy

AWS Repos:

* [aws-codedeploy-agent :fire::fire:](https://github.com/aws/aws-codedeploy-agent) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-codedeploy-agent?style=flat)](https://github.com/aws/aws-codedeploy-agent/stargazers) - Sample agent.
* [aws-codedeploy-plugin :fire:](https://github.com/awslabs/aws-codedeploy-plugin) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-codedeploy-plugin?style=flat)](https://github.com/awslabs/aws-codedeploy-plugin/stargazers) - Jenkins plugin.
* [aws-codedeploy-samples :fire::fire::fire:](https://github.com/awslabs/aws-codedeploy-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-codedeploy-samples?style=flat)](https://github.com/awslabs/aws-codedeploy-samples/stargazers) - Samples and template scenarios.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Code Pipeline

AWS Repos:

* [aws-codepipeline-custom-job-worker](https://github.com/awslabs/aws-codepipeline-custom-job-worker) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-codepipeline-custom-job-worker?style=flat)](https://github.com/awslabs/aws-codepipeline-custom-job-worker/stargazers) - Develop your own job worker when creating a custom action.
* [aws-codepipeline-jenkins-aws-codedeploy_linux](https://github.com/awslabs/aws-codepipeline-jenkins-aws-codedeploy_linux) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-codepipeline-jenkins-aws-codedeploy_linux?style=flat)](https://github.com/awslabs/aws-codepipeline-jenkins-aws-codedeploy_linux/stargazers) - Four-stage pipeline for Linux.
* [aws-codepipeline-plugin-for-jenkins](https://github.com/awslabs/aws-codepipeline-plugin-for-jenkins) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-codepipeline-plugin-for-jenkins?style=flat)](https://github.com/awslabs/aws-codepipeline-plugin-for-jenkins/stargazers) - Jenkins plugin.
* [aws-codepipeline-s3-aws-codedeploy_linux :fire:](https://github.com/awslabs/aws-codepipeline-s3-aws-codedeploy_linux) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-codepipeline-s3-aws-codedeploy_linux?style=flat)](https://github.com/awslabs/aws-codepipeline-s3-aws-codedeploy_linux/stargazers) - Simple pipeline for Linux.
* [AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows) [![GitHub stars](https://img.shields.io/github/stars/awslabs/AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows?style=flat)](https://github.com/awslabs/AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows/stargazers) - Four-stage pipeline for Windows.
* [AWSCodePipeline-S3-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-S3-AWSCodeDeploy_Windows) [![GitHub stars](https://img.shields.io/github/stars/awslabs/AWSCodePipeline-S3-AWSCodeDeploy_Windows?style=flat)](https://github.com/awslabs/AWSCodePipeline-S3-AWSCodeDeploy_Windows/stargazers) - Simple pipeline for Windows.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Cognito

AWS Repos:

* [amazon-cognito-android](https://github.com/aws/amazon-cognito-android) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-cognito-android?style=flat)](https://github.com/aws/amazon-cognito-android/stargazers) - Sync SDK for Android.
* [amazon-cognito-developer-authentication-sample](https://github.com/awslabs/amazon-cognito-developer-authentication-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-cognito-developer-authentication-sample?style=flat)](https://github.com/awslabs/amazon-cognito-developer-authentication-sample/stargazers) - Authentication sample.
* [amazon-cognito-dotnet](https://github.com/aws/amazon-cognito-dotnet) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-cognito-dotnet?style=flat)](https://github.com/aws/amazon-cognito-dotnet/stargazers) - Sync SDK for .NET.
* [amazon-cognito-ios](https://github.com/aws/amazon-cognito-ios) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-cognito-ios?style=flat)](https://github.com/aws/amazon-cognito-ios/stargazers) - Sync SDK for iOS.
* [amazon-cognito-js :fire::fire:](https://github.com/aws/amazon-cognito-js) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-cognito-js?style=flat)](https://github.com/aws/amazon-cognito-js/stargazers) - Sync SDK for JavaScript.
* [amazon-cognito-streams-sample](https://github.com/awslabs/amazon-cognito-streams-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-cognito-streams-sample?style=flat)](https://github.com/awslabs/amazon-cognito-streams-sample/stargazers) - Consuming Streams sample.
* [cognito-sample-nodejs :fire:](https://github.com/awslabs/cognito-sample-nodejs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/cognito-sample-nodejs?style=flat)](https://github.com/awslabs/cognito-sample-nodejs/stargazers) - Sample App for Node.js.

Community Repos:

* [capeless/warrant :fire::fire:](https://github.com/capless/warrant) [![GitHub stars](https://img.shields.io/github/stars/capless/warrant?style=flat)](https://github.com/capless/warrant/stargazers) - Python library for using Cognito.
* [rahulpsd18/cognito-backup-restore :fire:](https://github.com/rahulpsd18/cognito-backup-restore) [![GitHub stars](https://img.shields.io/github/stars/rahulpsd18/cognito-backup-restore?style=flat)](https://github.com/rahulpsd18/cognito-backup-restore/stargazers) - Tool for backing up and restoring Cognito user pools.

### Data Pipeline

AWS Repos:

* [data-pipeline-samples :fire::fire:](https://github.com/awslabs/data-pipeline-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/data-pipeline-samples?style=flat)](https://github.com/awslabs/data-pipeline-samples/stargazers) - Sample pipelines.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Device Farm

AWS Repos:

* [aws-device-farm-appium-tests-for-sample-app](https://github.com/awslabs/aws-device-farm-appium-tests-for-sample-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-device-farm-appium-tests-for-sample-app?style=flat)](https://github.com/awslabs/aws-device-farm-appium-tests-for-sample-app/stargazers) - Appium TestNG Android tests.
* [aws-device-farm-calabash-tests-for-sample-app](https://github.com/awslabs/aws-device-farm-calabash-tests-for-sample-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-device-farm-calabash-tests-for-sample-app?style=flat)](https://github.com/awslabs/aws-device-farm-calabash-tests-for-sample-app/stargazers) - Calabash Android tests.
* [aws-device-farm-gradle-plugin](https://github.com/awslabs/aws-device-farm-gradle-plugin) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-device-farm-gradle-plugin?style=flat)](https://github.com/awslabs/aws-device-farm-gradle-plugin/stargazers) - Gradle plugin.
* [aws-device-farm-jenkins-plugin](https://github.com/awslabs/aws-device-farm-jenkins-plugin) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-device-farm-jenkins-plugin?style=flat)](https://github.com/awslabs/aws-device-farm-jenkins-plugin/stargazers) - Jenkins plugin.
* [aws-device-farm-sample-app-for-android :fire:](https://github.com/awslabs/aws-device-farm-sample-app-for-android) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-device-farm-sample-app-for-android?style=flat)](https://github.com/awslabs/aws-device-farm-sample-app-for-android/stargazers) - Sample Android app.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### DynamoDB

AWS Repos:

* [aws-dotnet-session-provider](https://github.com/aws/aws-dotnet-session-provider) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-dotnet-session-provider?style=flat)](https://github.com/aws/aws-dotnet-session-provider/stargazers) - A session state provider for ASP.NET apps.
* [aws-dotnet-trace-listener](https://github.com/aws/aws-dotnet-trace-listener) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-dotnet-trace-listener?style=flat)](https://github.com/aws/aws-dotnet-trace-listener/stargazers) - A trace listener for System.Diagnostics that can be used to log events.
* [aws-dynamodb-encryption-java :fire:](https://github.com/awslabs/aws-dynamodb-encryption-java) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-dynamodb-encryption-java?style=flat)](https://github.com/awslabs/aws-dynamodb-encryption-java/stargazers) - Encryption Client for Java.
* [aws-dynamodb-examples :fire::fire:](https://github.com/awslabs/aws-dynamodb-examples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-dynamodb-examples?style=flat)](https://github.com/awslabs/aws-dynamodb-examples/stargazers) - Samples using the Java SDK.
* [aws-dynamodb-mars-json-demo](https://github.com/awslabs/aws-dynamodb-mars-json-demo) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-dynamodb-mars-json-demo?style=flat)](https://github.com/awslabs/aws-dynamodb-mars-json-demo/stargazers) - Stores and indexes NASA JPL Mars images.
* [aws-dynamodb-session-tomcat](https://github.com/aws/aws-dynamodb-session-tomcat) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-dynamodb-session-tomcat?style=flat)](https://github.com/aws/aws-dynamodb-session-tomcat/stargazers) - Session store for Apache Tomcat.
* [aws-sessionstore-dynamodb-ruby](https://github.com/aws/aws-sessionstore-dynamodb-ruby) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sessionstore-dynamodb-ruby?style=flat)](https://github.com/aws/aws-sessionstore-dynamodb-ruby/stargazers) - Handles sessions for Ruby web apps.
* [dynamodb-cross-region-library :fire::fire:](https://github.com/awslabs/dynamodb-cross-region-library) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-cross-region-library?style=flat)](https://github.com/awslabs/dynamodb-cross-region-library/stargazers) - Cross-region replication.
* [dynamodb-geo :fire::fire:](https://github.com/awslabs/dynamodb-geo) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-geo?style=flat)](https://github.com/awslabs/dynamodb-geo/stargazers) - Library to create and query geospatial data.
* [dynamodb-import-export-tool](https://github.com/awslabs/dynamodb-import-export-tool) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-import-export-tool?style=flat)](https://github.com/awslabs/dynamodb-import-export-tool/stargazers) - Import and export examples.
* [dynamodb-online-index-violation-detector](https://github.com/awslabs/dynamodb-online-index-violation-detector) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-online-index-violation-detector?style=flat)](https://github.com/awslabs/dynamodb-online-index-violation-detector/stargazers) - Finds violations on an online GSI's hash key and range key.
* [dynamodb-streams-kinesis-adapter](https://github.com/awslabs/dynamodb-streams-kinesis-adapter) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-streams-kinesis-adapter?style=flat)](https://github.com/awslabs/dynamodb-streams-kinesis-adapter/stargazers) - Kinesis interface to consume and process data from a DynamoDB stream.
* [dynamodb-tictactoe-example-app](https://github.com/awslabs/dynamodb-tictactoe-example-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-tictactoe-example-app?style=flat)](https://github.com/awslabs/dynamodb-tictactoe-example-app/stargazers) - Lightweight python app.
* [dynamodb-titan-storage-backend :fire::fire:](https://github.com/awslabs/dynamodb-titan-storage-backend) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-titan-storage-backend?style=flat)](https://github.com/awslabs/dynamodb-titan-storage-backend/stargazers) - Storage Backend for Titan.
* [dynamodb-transactions :fire::fire:](https://github.com/awslabs/dynamodb-transactions) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-transactions?style=flat)](https://github.com/awslabs/dynamodb-transactions/stargazers) - Performs atomic writes and isolated reads across multiple items and tables.
* [logstash-input-dynamodb :fire:](https://github.com/awslabs/logstash-input-dynamodb) [![GitHub stars](https://img.shields.io/github/stars/awslabs/logstash-input-dynamodb?style=flat)](https://github.com/awslabs/logstash-input-dynamodb/stargazers) - Logstash input plugin.

Community Repos:

* [channl/dynamodb-lambda-autoscale :fire::fire:](https://github.com/channl/dynamodb-lambda-autoscale) [![GitHub stars](https://img.shields.io/github/stars/channl/dynamodb-lambda-autoscale?style=flat)](https://github.com/channl/dynamodb-lambda-autoscale/stargazers) - Autoscale DynamoDB provisioned capacity using Lambda.
* [lyft/confidant :fire::fire::fire::fire:](https://github.com/lyft/confidant) [![GitHub stars](https://img.shields.io/github/stars/lyft/confidant?style=flat)](https://github.com/lyft/confidant/stargazers) - Stores secrets, encrypted at rest.
* [sebdah/dynamic-dynamodb :fire::fire::fire:](https://github.com/sebdah/dynamic-dynamodb) [![GitHub stars](https://img.shields.io/github/stars/sebdah/dynamic-dynamodb?style=flat)](https://github.com/sebdah/dynamic-dynamodb/stargazers) - Provides auto-scaling.
* [sensedeep/dynamodb-onetable :fire::fire::fire:](https://github.com/sensedeep/dynamodb-onetable) [![GitHub stars](https://img.shields.io/github/stars/sensedeep/dynamodb-onetable?style=flat)](https://github.com/sensedeep/dynamodb-onetable/stargazers) - DynamoDB library for single table designs using NodeJS.

### Elastic Beanstalk

AWS Repos:

* [aws-eb-glassfish-dockerfiles](https://github.com/aws/aws-eb-glassfish-dockerfiles) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-eb-glassfish-dockerfiles?style=flat)](https://github.com/aws/aws-eb-glassfish-dockerfiles/stargazers) - GlassFish docker files.
* [aws-eb-python-dockerfiles](https://github.com/aws/aws-eb-python-dockerfiles) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-eb-python-dockerfiles?style=flat)](https://github.com/aws/aws-eb-python-dockerfiles/stargazers) - Python docker files.
* [eb-demo-php-simple-app :fire:](https://github.com/awslabs/eb-demo-php-simple-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-demo-php-simple-app?style=flat)](https://github.com/awslabs/eb-demo-php-simple-app/stargazers) - Simple PHP app.
* [eb-docker-multiple-ports](https://github.com/awslabs/eb-docker-multiple-ports) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-docker-multiple-ports?style=flat)](https://github.com/awslabs/eb-docker-multiple-ports/stargazers) - Simple Node.js and Tomcat apps using Docker images.
* [eb-docker-nginx-proxy :fire:](https://github.com/awslabs/eb-docker-nginx-proxy) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-docker-nginx-proxy?style=flat)](https://github.com/awslabs/eb-docker-nginx-proxy/stargazers) - Simple PHP app using the PHP-FPM and Nginx Docker images.
* [eb-docker-virtual-hosting](https://github.com/awslabs/eb-docker-virtual-hosting) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-docker-virtual-hosting?style=flat)](https://github.com/awslabs/eb-docker-virtual-hosting/stargazers) - Simple PHP, Tomcat, and Nginx applications using Docker images.
* [eb-node-express-sample :fire::fire:](https://github.com/awslabs/eb-node-express-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-node-express-sample?style=flat)](https://github.com/awslabs/eb-node-express-sample/stargazers) - Sample express app.
* [eb-node-express-signup](https://github.com/awslabs/eb-node-express-signup) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-node-express-signup?style=flat)](https://github.com/awslabs/eb-node-express-signup/stargazers) - Express framework and Bootstrap Node.js sample app.
* [eb-node-express](https://github.com/awslabs/eb-node-express) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-node-express?style=flat)](https://github.com/awslabs/eb-node-express/stargazers) - Sample app referenced in the Developer Guide.
* [eb-py-flask-signup-worker](https://github.com/awslabs/eb-py-flask-signup-worker) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-py-flask-signup-worker?style=flat)](https://github.com/awslabs/eb-py-flask-signup-worker/stargazers) - Python app that illustrates worker roles.
* [eb-py-flask-signup :fire::fire:](https://github.com/awslabs/eb-py-flask-signup) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-py-flask-signup?style=flat)](https://github.com/awslabs/eb-py-flask-signup/stargazers) - Python signup form app with Flask and Bootstrap.
* [eb-python-flask](https://github.com/awslabs/eb-python-flask) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-python-flask?style=flat)](https://github.com/awslabs/eb-python-flask/stargazers) - Simple Python and Flask app.
* [eb-wif-sample](https://github.com/awslabs/eb-wif-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/eb-wif-sample?style=flat)](https://github.com/awslabs/eb-wif-sample/stargazers) - Sample login app with Web Identity Federation.

Community Repos:

* [alienfast/elastic-beanstalk :fire:](https://github.com/alienfast/elastic-beanstalk) [![GitHub stars](https://img.shields.io/github/stars/alienfast/elastic-beanstalk?style=flat)](https://github.com/alienfast/elastic-beanstalk/stargazers) - Gem with rake configuration and deployment for rails apps.
* [ThoughtWorksStudios/eb_deployer :fire::fire:](https://github.com/ThoughtWorksStudios/eb_deployer) [![GitHub stars](https://img.shields.io/github/stars/ThoughtWorksStudios/eb_deployer?style=flat)](https://github.com/ThoughtWorksStudios/eb_deployer/stargazers) - Blue-green deployment automation.

### Elastic Compute Cloud

AWS Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

Community Repos:

* [alestic/ec2-consistent-snapshot :fire::fire:](https://github.com/alestic/ec2-consistent-snapshot) [![GitHub stars](https://img.shields.io/github/stars/alestic/ec2-consistent-snapshot?style=flat)](https://github.com/alestic/ec2-consistent-snapshot/stargazers) - Initiate consistent EBS snapshots in EC2.
* [ConradIrwin/aws-name-server :fire::fire::fire:](https://github.com/ConradIrwin/aws-name-server) [![GitHub stars](https://img.shields.io/github/stars/ConradIrwin/aws-name-server?style=flat)](https://github.com/ConradIrwin/aws-name-server/stargazers) - DNS server that lets you look up instances by name.
* [cristim/autospotting :fire::fire::fire::fire::fire:](https://github.com/autospotting/autospotting) [![GitHub stars](https://img.shields.io/github/stars/autospotting/autospotting?style=flat)](https://github.com/autospotting/autospotting/stargazers) - Automatically rolling-replace on-demand EC2 instances in AutoScaling groups with compatible spot instances.
* [evannuil/aws-snapshot-tool :fire::fire:](https://github.com/evannuil/aws-snapshot-tool) [![GitHub stars](https://img.shields.io/github/stars/evannuil/aws-snapshot-tool?style=flat)](https://github.com/evannuil/aws-snapshot-tool/stargazers) - Automates EBS snapshots and rotation.
* [kelseyhightower/kubernetes-the-hard-way :fire::fire::fire::fire::fire:](https://github.com/kelseyhightower/kubernetes-the-hard-way) [![GitHub stars](https://img.shields.io/github/stars/kelseyhightower/kubernetes-the-hard-way?style=flat)](https://github.com/kelseyhightower/kubernetes-the-hard-way/stargazers) - Bootstrap Kubernetes the hard way on EC2. No scripts.
* [mirakui/ec2ssh :fire::fire:](https://github.com/mirakui/ec2ssh) [![GitHub stars](https://img.shields.io/github/stars/mirakui/ec2ssh?style=flat)](https://github.com/mirakui/ec2ssh/stargazers) - SSH config manager.
* [openebs/openebs :fire::fire::fire::fire::fire:](https://github.com/openebs/openebs) [![GitHub stars](https://img.shields.io/github/stars/openebs/openebs?style=flat)](https://github.com/openebs/openebs/stargazers) - Containerized block storage QoS SLAs, tiering and replica policies across AZs and environments, and predictable and scalable performance.
* [skavanagh/EC2Box :fire::fire:](https://github.com/skavanagh/EC2Box) [![GitHub stars](https://img.shields.io/github/stars/skavanagh/EC2Box?style=flat)](https://github.com/skavanagh/EC2Box/stargazers) - A web-based SSH console to manage multiple instances simultaneously.
* [wbailey/claws :fire:](https://github.com/wbailey/claws) [![GitHub stars](https://img.shields.io/github/stars/wbailey/claws?style=flat)](https://github.com/wbailey/claws/stargazers) - CLI-driven console with capistrano integration.

### Elastic Container Service

AWS Repos:

* [amazon-ecs-agent :fire::fire::fire::fire:](https://github.com/aws/amazon-ecs-agent) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-ecs-agent?style=flat)](https://github.com/aws/amazon-ecs-agent/stargazers) - Agent that runs on and starts containers.
* [amazon-ecs-amazon-efs](https://github.com/awslabs/amazon-ecs-amazon-efs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-ecs-amazon-efs?style=flat)](https://github.com/awslabs/amazon-ecs-amazon-efs/stargazers) - Persists Data from containers.
* [amazon-ecs-init :fire:](https://github.com/aws/amazon-ecs-init) [![GitHub stars](https://img.shields.io/github/stars/aws/amazon-ecs-init?style=flat)](https://github.com/aws/amazon-ecs-init/stargazers) - RPM developed to support the Amazon ECS Container Agent.
* [blox :fire::fire::fire:](https://github.com/blox/blox) [![GitHub stars](https://img.shields.io/github/stars/blox/blox?style=flat)](https://github.com/blox/blox/stargazers) - Open source tools for building custom schedulers on ECS.
* [ecs-blue-green-deployment :fire::fire:](https://github.com/awslabs/ecs-blue-green-deployment) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-blue-green-deployment?style=flat)](https://github.com/awslabs/ecs-blue-green-deployment/stargazers) - Blue-green deployment on ECS.
* [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-cloudwatch-logs?style=flat)](https://github.com/awslabs/ecs-cloudwatch-logs/stargazers) - Assets from the blog using Amazon ECS and Amazon CloudWatch logs.
* [ecs-demo-php-simple-app :fire:](https://github.com/awslabs/ecs-demo-php-simple-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-demo-php-simple-app?style=flat)](https://github.com/awslabs/ecs-demo-php-simple-app/stargazers) - Simple PHP app.
* [ecs-mesos-scheduler-driver :fire:](https://github.com/awslabs/ecs-mesos-scheduler-driver) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-mesos-scheduler-driver?style=flat)](https://github.com/awslabs/ecs-mesos-scheduler-driver/stargazers) - Integrates Apache Mesos.
* [ecs-refarch-continuous-deployment :fire::fire::fire:](https://github.com/awslabs/ecs-refarch-continuous-deployment) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-refarch-continuous-deployment?style=flat)](https://github.com/awslabs/ecs-refarch-continuous-deployment/stargazers) - Reference Architecture for continuous deployment to ECS using CodePipeline.
* [ecs-task-kite](https://github.com/awslabs/ecs-task-kite) [![GitHub stars](https://img.shields.io/github/stars/awslabs/ecs-task-kite?style=flat)](https://github.com/awslabs/ecs-task-kite/stargazers) - Simple ambassador container for inter-task communication.
* [lambda-ecs-worker-pattern :fire::fire:](https://github.com/awslabs/lambda-ecs-worker-pattern) [![GitHub stars](https://img.shields.io/github/stars/awslabs/lambda-ecs-worker-pattern?style=flat)](https://github.com/awslabs/lambda-ecs-worker-pattern/stargazers) - Extends Lambda using SQS and ECS.
* [py-flask-signup-docker](https://github.com/awslabs/py-flask-signup-docker) [![GitHub stars](https://img.shields.io/github/stars/awslabs/py-flask-signup-docker?style=flat)](https://github.com/awslabs/py-flask-signup-docker/stargazers) - Python sample app.
* [service-discovery-ecs-consul :fire:](https://github.com/awslabs/service-discovery-ecs-consul) [![GitHub stars](https://img.shields.io/github/stars/awslabs/service-discovery-ecs-consul?style=flat)](https://github.com/awslabs/service-discovery-ecs-consul/stargazers) - Assets from the blog Service Discovery via Consul with Amazon ECS.

Community Repos:

* [Lumoslabs/broadside](https://github.com/lumoslabs/broadside) [![GitHub stars](https://img.shields.io/github/stars/lumoslabs/broadside?style=flat)](https://github.com/lumoslabs/broadside/stargazers) - Command line tool for deploying revisions of containerized applications.
* [Stelligent/mu :fire::fire::fire:](https://github.com/stelligent/mu) [![GitHub stars](https://img.shields.io/github/stars/stelligent/mu?style=flat)](https://github.com/stelligent/mu/stargazers) - Command line tool to simplify ECS deployments via CodeBuild and CodePipeline.

### Elastic File System

AWS Repos:

* [amazon-ecs-amazon-efs](https://github.com/awslabs/amazon-ecs-amazon-efs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-ecs-amazon-efs?style=flat)](https://github.com/awslabs/amazon-ecs-amazon-efs/stargazers) - Persist data from ECS.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Elastic MapReduce

AWS Repos:

* [emr-bootstrap-actions :fire::fire::fire:](https://github.com/awslabs/emr-bootstrap-actions) [![GitHub stars](https://img.shields.io/github/stars/awslabs/emr-bootstrap-actions?style=flat)](https://github.com/awslabs/emr-bootstrap-actions/stargazers) - Sample bootstrap actions.
* [emr-sample-apps](https://github.com/awslabs/emr-sample-apps) [![GitHub stars](https://img.shields.io/github/stars/awslabs/emr-sample-apps?style=flat)](https://github.com/awslabs/emr-sample-apps/stargazers) - Sample apps.

Community Repos:

* [Yelp/mrjob :fire::fire::fire::fire::fire:](https://github.com/Yelp/mrjob) [![GitHub stars](https://img.shields.io/github/stars/Yelp/mrjob?style=flat)](https://github.com/Yelp/mrjob/stargazers) - Run MapReduce jobs on Hadoop or EMR.

### Elastic Search

AWS Repos:

* [logstash-output-amazon_es :fire::fire:](https://github.com/awslabs/logstash-output-amazon_es) [![GitHub stars](https://img.shields.io/github/stars/awslabs/logstash-output-amazon_es?style=flat)](https://github.com/awslabs/logstash-output-amazon_es/stargazers) - Logstash output plugin to sign and export events.
* [opsworks-elasticsearch-cookbook](https://github.com/awslabs/opsworks-elasticsearch-cookbook) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-elasticsearch-cookbook?style=flat)](https://github.com/awslabs/opsworks-elasticsearch-cookbook/stargazers) - OpsWorks Elasticsearch sample cookbook.

Community Repos:

* [elastic/elasticsearch-cloud-aws :fire::fire::fire:](https://github.com/elastic/elasticsearch-cloud-aws) [![GitHub stars](https://img.shields.io/github/stars/elastic/elasticsearch-cloud-aws?style=flat)](https://github.com/elastic/elasticsearch-cloud-aws/stargazers) - Plugin for Elasticsearch.

### Elasticache

AWS Repos:

* [aws-elasticache-cluster-client-libmemcached](https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-elasticache-cluster-client-libmemcached?style=flat)](https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached/stargazers) - Libmemcached library support.
* [aws-elasticache-cluster-client-memcached-for-java](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-java) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-elasticache-cluster-client-memcached-for-java?style=flat)](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-java/stargazers) - Client for Java.
* [aws-elasticache-cluster-client-memcached-for-php](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-elasticache-cluster-client-memcached-for-php?style=flat)](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php/stargazers) - Enhanced PHP library connecting to ElastiCache.
* [elasticache-cluster-config-net](https://github.com/awslabs/elasticache-cluster-config-net) [![GitHub stars](https://img.shields.io/github/stars/awslabs/elasticache-cluster-config-net?style=flat)](https://github.com/awslabs/elasticache-cluster-config-net/stargazers) - Config object for Enyim's MemcachedClient to enable auto discovery.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Glacier

Community Repos:

* [vsespb/mt-aws-glacier :fire::fire::fire:](https://github.com/vsespb/mt-aws-glacier) [![GitHub stars](https://img.shields.io/github/stars/vsespb/mt-aws-glacier?style=flat)](https://github.com/vsespb/mt-aws-glacier/stargazers) - Perl Multithreaded Multipart sync to Glacier.

### Kinesis

AWS Repos:

* [amazon-kinesis-aggregators :fire:](https://github.com/awslabs/amazon-kinesis-aggregators) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-aggregators?style=flat)](https://github.com/awslabs/amazon-kinesis-aggregators/stargazers) - Provides a simple way to create real time aggregations.
* [amazon-kinesis-client-net](https://github.com/awslabs/amazon-kinesis-client-net) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-client-net?style=flat)](https://github.com/awslabs/amazon-kinesis-client-net/stargazers) - Client Library for .NET.
* [amazon-kinesis-client-nodejs :fire::fire:](https://github.com/awslabs/amazon-kinesis-client-nodejs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-client-nodejs?style=flat)](https://github.com/awslabs/amazon-kinesis-client-nodejs/stargazers) - Client Library for Node.js.
* [amazon-kinesis-client-python :fire::fire:](https://github.com/awslabs/amazon-kinesis-client-python) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-client-python?style=flat)](https://github.com/awslabs/amazon-kinesis-client-python/stargazers) - Client Library for Python.
* [amazon-kinesis-client-ruby :fire:](https://github.com/awslabs/amazon-kinesis-client-ruby) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-client-ruby?style=flat)](https://github.com/awslabs/amazon-kinesis-client-ruby/stargazers) - Client Library for Ruby.
* [amazon-kinesis-client :fire::fire::fire:](https://github.com/awslabs/amazon-kinesis-client) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-client?style=flat)](https://github.com/awslabs/amazon-kinesis-client/stargazers) Client library for Amazon Kinesis.
* [amazon-kinesis-connectors :fire::fire:](https://github.com/awslabs/amazon-kinesis-connectors) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-connectors?style=flat)](https://github.com/awslabs/amazon-kinesis-connectors/stargazers) - Libary to integrate with other AWS and non-AWS services.
* [amazon-kinesis-data-visualization-sample :fire:](https://github.com/awslabs/amazon-kinesis-data-visualization-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-data-visualization-sample?style=flat)](https://github.com/awslabs/amazon-kinesis-data-visualization-sample/stargazers) - Sample data visualization app.
* [amazon-kinesis-learning](https://github.com/awslabs/amazon-kinesis-learning) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-learning?style=flat)](https://github.com/awslabs/amazon-kinesis-learning/stargazers) - Learning Kinesis Development.
* [amazon-kinesis-producer :fire::fire:](https://github.com/awslabs/amazon-kinesis-producer) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-producer?style=flat)](https://github.com/awslabs/amazon-kinesis-producer/stargazers) - Producer Library.
* [amazon-kinesis-scaling-utils :fire::fire:](https://github.com/awslabs/amazon-kinesis-scaling-utils) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-kinesis-scaling-utils?style=flat)](https://github.com/awslabs/amazon-kinesis-scaling-utils/stargazers) - Provides the ability to scale streams.
* [aws-fluent-plugin-kinesis :fire::fire:](https://github.com/awslabs/aws-fluent-plugin-kinesis) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-fluent-plugin-kinesis?style=flat)](https://github.com/awslabs/aws-fluent-plugin-kinesis/stargazers) - Fluent Plugin.
* [dynamodb-streams-kinesis-adapter](https://github.com/awslabs/dynamodb-streams-kinesis-adapter) [![GitHub stars](https://img.shields.io/github/stars/awslabs/dynamodb-streams-kinesis-adapter?style=flat)](https://github.com/awslabs/dynamodb-streams-kinesis-adapter/stargazers) - DynamoDB Streams Adapter.
* [kinesis-log4j-appender](https://github.com/awslabs/kinesis-log4j-appender) [![GitHub stars](https://img.shields.io/github/stars/awslabs/kinesis-log4j-appender?style=flat)](https://github.com/awslabs/kinesis-log4j-appender/stargazers) - Log4J Appender.
* [kinesis-poster-worker](https://github.com/awslabs/kinesis-poster-worker) [![GitHub stars](https://img.shields.io/github/stars/awslabs/kinesis-poster-worker?style=flat)](https://github.com/awslabs/kinesis-poster-worker/stargazers) - Simple multi-threaded Python Poster and Worker.
* [kinesis-storm-spout :fire:](https://github.com/awslabs/kinesis-storm-spout) [![GitHub stars](https://img.shields.io/github/stars/awslabs/kinesis-storm-spout?style=flat)](https://github.com/awslabs/kinesis-storm-spout/stargazers) - Spout for Storm.
* [mqtt-kinesis-bridge](https://github.com/awslabs/mqtt-kinesis-bridge) [![GitHub stars](https://img.shields.io/github/stars/awslabs/mqtt-kinesis-bridge?style=flat)](https://github.com/awslabs/mqtt-kinesis-bridge/stargazers) - Simple MQTT bridge in Python.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Lambda

AWS Repos:

* [amazon-elasticsearch-lambda-samples :fire::fire:](https://github.com/awslabs/amazon-elasticsearch-lambda-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-elasticsearch-lambda-samples?style=flat)](https://github.com/awslabs/amazon-elasticsearch-lambda-samples/stargazers) - Data ingestion for Elasticsearch from S3 and Kinesis.
* [awslabs/aws-sam-local :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-sam-local) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sam-local?style=flat)](https://github.com/awslabs/aws-sam-local/stargazers) - CLI tool for local development and testing of Serverless applications.
* [aws-lambda-go :fire::fire::fire::fire::fire:](https://github.com/aws/aws-lambda-go) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-lambda-go?style=flat)](https://github.com/aws/aws-lambda-go/stargazers) - Libraries, samples and tools to help Go developers develop Lambda functions.
* [aws-lambda-java-libs :fire::fire:](https://github.com/aws/aws-lambda-java-libs) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-lambda-java-libs?style=flat)](https://github.com/aws/aws-lambda-java-libs/stargazers) - Official mirror for interface definitions and helper classes.
* [aws-lambda-redshift-loader :fire::fire::fire:](https://github.com/awslabs/aws-lambda-redshift-loader) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-lambda-redshift-loader?style=flat)](https://github.com/awslabs/aws-lambda-redshift-loader/stargazers) - Redshift loader.
* [chalice :fire::fire::fire::fire::fire:](https://github.com/awslabs/chalice) [![GitHub stars](https://img.shields.io/github/stars/awslabs/chalice?style=flat)](https://github.com/awslabs/chalice/stargazers) - Python Serverless Microframework.
* [create-thumbnails-lambda](https://github.com/awslabs/create-thumbnails-lambda) [![GitHub stars](https://img.shields.io/github/stars/awslabs/create-thumbnails-lambda?style=flat)](https://github.com/awslabs/create-thumbnails-lambda/stargazers) - Uses the grunt-aws-lambda plugin to help you develop and test.
* [lambda-ecs-worker-pattern :fire::fire:](https://github.com/awslabs/lambda-ecs-worker-pattern) [![GitHub stars](https://img.shields.io/github/stars/awslabs/lambda-ecs-worker-pattern?style=flat)](https://github.com/awslabs/lambda-ecs-worker-pattern/stargazers) - Extends Lambda using SQS and ECS.
* [lambda-refarch-fileprocessing :fire::fire:](https://github.com/awslabs/lambda-refarch-fileprocessing) [![GitHub stars](https://img.shields.io/github/stars/awslabs/lambda-refarch-fileprocessing?style=flat)](https://github.com/awslabs/lambda-refarch-fileprocessing/stargazers) - Reference Architecture for Real-time File Processing.
* [lambda-refarch-iotbackend :fire::fire:](https://github.com/awslabs/lambda-refarch-iotbackend) [![GitHub stars](https://img.shields.io/github/stars/awslabs/lambda-refarch-iotbackend?style=flat)](https://github.com/awslabs/lambda-refarch-iotbackend/stargazers) - Reference Architecture for creating an IoT Backend.
* [lambda-refarch-mobilebackend :fire::fire::fire:](https://github.com/awslabs/lambda-refarch-mobilebackend) [![GitHub stars](https://img.shields.io/github/stars/awslabs/lambda-refarch-mobilebackend?style=flat)](https://github.com/awslabs/lambda-refarch-mobilebackend/stargazers) - Reference Architecture for creating a Mobile Backend.
* [lambda-refarch-webapp :fire::fire::fire::fire:](https://github.com/awslabs/lambda-refarch-webapp) [![GitHub stars](https://img.shields.io/github/stars/awslabs/lambda-refarch-webapp?style=flat)](https://github.com/awslabs/lambda-refarch-webapp/stargazers) - Reference Architecture for creating a Web Application.

Community Repos:

* [alestic/lambdash :fire::fire::fire:](https://github.com/alestic/lambdash) [![GitHub stars](https://img.shields.io/github/stars/alestic/lambdash?style=flat)](https://github.com/alestic/lambdash/stargazers) - Lambda shell - Run sh commands inside the Lambda environment.
* [Alephbet/gimel :fire::fire:](https://github.com/Alephbet/gimel) [![GitHub stars](https://img.shields.io/github/stars/Alephbet/gimel?style=flat)](https://github.com/Alephbet/gimel/stargazers) - Run your own A/B testing backend using Lambda.
* [apex/apex ](https://github.com/apex/apex) [![GitHub stars](https://img.shields.io/github/stars/apex/apex?style=flat)](https://github.com/apex/apex/stargazers) - Minimal AWS Lambda function manager with Go support.
* [claudiajs/claudia :fire::fire::fire::fire::fire:](https://github.com/claudiajs/claudia) [![GitHub stars](https://img.shields.io/github/stars/claudiajs/claudia?style=flat)](https://github.com/claudiajs/claudia/stargazers) - Deploy Node.js projects to Lambda and API Gateway easily.
* [cloudnative/lambda-chat :fire::fire:](https://github.com/cloudnative/lambda-chat) [![GitHub stars](https://img.shields.io/github/stars/cloudnative/lambda-chat?style=flat)](https://github.com/cloudnative/lambda-chat/stargazers) - A chat application without servers.
* [danilop/LambdAuth :fire::fire::fire::fire:](https://github.com/danilop/LambdAuth) [![GitHub stars](https://img.shields.io/github/stars/danilop/LambdAuth?style=flat)](https://github.com/danilop/LambdAuth/stargazers) - Sample authentication service.
* [eawsy/aws-lambda-go :fire::fire::fire:](https://github.com/eawsy/aws-lambda-go) [![GitHub stars](https://img.shields.io/github/stars/eawsy/aws-lambda-go?style=flat)](https://github.com/eawsy/aws-lambda-go/stargazers) - A fast and clean way to execute Go on Lambda.
* [garnaat/kappa :fire::fire::fire:](https://github.com/garnaat/kappa) [![GitHub stars](https://img.shields.io/github/stars/garnaat/kappa?style=flat)](https://github.com/garnaat/kappa/stargazers) - Kappa is a CLI tool that makes it easier to deploy, update, and test functions for AWS Lambda.
* [goadapp/goad :fire::fire::fire::fire:](https://github.com/goadapp/goad) [![GitHub stars](https://img.shields.io/github/stars/goadapp/goad?style=flat)](https://github.com/goadapp/goad/stargazers) - Lambda powered, highly distributed, load testing tool.
* [graphcool/chromeless :fire::fire::fire::fire::fire:](https://github.com/graphcool/chromeless) [![GitHub stars](https://img.shields.io/github/stars/graphcool/chromeless?style=flat)](https://github.com/graphcool/chromeless/stargazers) - Automate Chrome through Lambda.
* [grycap/scar :fire::fire::fire:](https://github.com/grycap/scar) [![GitHub stars](https://img.shields.io/github/stars/grycap/scar?style=flat)](https://github.com/grycap/scar/stargazers) - Transparently execute containers out of Docker images in AWS Lambda.
* [jeremydaly/lambda-api :fire::fire::fire::fire:](https://github.com/jeremydaly/lambda-api) [![GitHub stars](https://img.shields.io/github/stars/jeremydaly/lambda-api?style=flat)](https://github.com/jeremydaly/lambda-api/stargazers) - Lightweight web framework for your serverless applications.
* [jimpick/lambda-comments :fire::fire::fire:](https://github.com/jimpick/lambda-comments) [![GitHub stars](https://img.shields.io/github/stars/jimpick/lambda-comments?style=flat)](https://github.com/jimpick/lambda-comments/stargazers) - Blog commenting system built with Lambda.
* [jorgebastida/gordon :fire::fire::fire::fire::fire:](https://github.com/jorgebastida/gordon) [![GitHub stars](https://img.shields.io/github/stars/jorgebastida/gordon?style=flat)](https://github.com/jorgebastida/gordon/stargazers) - λ Gordon is a tool to create, wire and deploy AWS Lambdas using CloudFormation.
* [ks888/LambStatus :fire::fire::fire::fire:](https://github.com/ks888/LambStatus) [![GitHub stars](https://img.shields.io/github/stars/ks888/LambStatus?style=flat)](https://github.com/ks888/LambStatus/stargazers) - A status page system inspired by StatusPage.io, built on AWS Lambda.
* [kubek2k/lambdoku :fire::fire::fire:](https://github.com/kubek2k/lambdoku) [![GitHub stars](https://img.shields.io/github/stars/kubek2k/lambdoku?style=flat)](https://github.com/kubek2k/lambdoku/stargazers) - Heroku-like experience when using Lambda.
* [lambci/lambci :fire::fire::fire::fire::fire:](https://github.com/lambci/lambci) [![GitHub stars](https://img.shields.io/github/stars/lambci/lambci?style=flat)](https://github.com/lambci/lambci/stargazers) - A continuous integration system built on Lambda.
* [littlstar/s3-lambda :fire::fire::fire::fire:](https://github.com/littlstar/s3-lambda) [![GitHub stars](https://img.shields.io/github/stars/littlstar/s3-lambda?style=flat)](https://github.com/littlstar/s3-lambda/stargazers) - Lambda functions over S3 objects with concurrency control (each, map, reduce, filter).
* [mentum/lambdaws :fire::fire::fire::fire:](https://github.com/mentum/lambdaws) [![GitHub stars](https://img.shields.io/github/stars/mentum/lambdaws?style=flat)](https://github.com/mentum/lambdaws/stargazers) - Deploy, run and get results in a breeze.
* [Miserlou/Zappa :fire::fire::fire::fire::fire:](https://github.com/Miserlou/Zappa) [![GitHub stars](https://img.shields.io/github/stars/Miserlou/Zappa?style=flat)](https://github.com/Miserlou/Zappa/stargazers) - Serverless WSGI Python Web Apps with AWS Lambda + API Gateway.
* [nficano/python-lambda :fire::fire::fire::fire:](https://github.com/nficano/python-lambda) [![GitHub stars](https://img.shields.io/github/stars/nficano/python-lambda?style=flat)](https://github.com/nficano/python-lambda/stargazers) - A toolkit for developing and deploying serverless Python code in Lambda.
* [serverless/serverless :fire::fire::fire::fire::fire:](https://github.com/serverless/serverless) [![GitHub stars](https://img.shields.io/github/stars/serverless/serverless?style=flat)](https://github.com/serverless/serverless/stargazers) The Serverless Application Framework (formerly JAWS).
* [Tim-B/grunt-aws-lambda :fire::fire:](https://github.com/Tim-B/grunt-aws-lambda) [![GitHub stars](https://img.shields.io/github/stars/Tim-B/grunt-aws-lambda?style=flat)](https://github.com/Tim-B/grunt-aws-lambda/stargazers) - Grunt plugin.
* [trek10inc/aws-lambda-debugger :fire::fire:](https://github.com/trek10inc/aws-lambda-debugger) [![GitHub stars](https://img.shields.io/github/stars/trek10inc/aws-lambda-debugger?style=flat)](https://github.com/trek10inc/aws-lambda-debugger/stargazers) - Remote debugging tool for Lambda functions running on Node 6.10

### Machine Learning

AWS Repos:

* [machine-learning-samples :fire::fire::fire:](https://github.com/awslabs/machine-learning-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/machine-learning-samples?style=flat)](https://github.com/awslabs/machine-learning-samples/stargazers) - Sample apps.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Mobile Analytics

AWS Repos:

* [aws-sdk-mobile-analytics-js](https://github.com/aws/aws-sdk-mobile-analytics-js) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-sdk-mobile-analytics-js?style=flat)](https://github.com/aws/aws-sdk-mobile-analytics-js/stargazers) - JavaScript SDK.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### OpsWorks

AWS Repos:

* [opsworks-attribute-customization](https://github.com/awslabs/opsworks-attribute-customization) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-attribute-customization?style=flat)](https://github.com/awslabs/opsworks-attribute-customization/stargazers) - Attribute customization example.
* [opsworks-capistrano](https://github.com/awslabs/opsworks-capistrano) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-capistrano?style=flat)](https://github.com/awslabs/opsworks-capistrano/stargazers) - Capistrano with instances.
* [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-cloudwatch-logs-cookbooks?style=flat)](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks/stargazers) - CloudWatch sample cookbook.
* [opsworks-cookbooks :fire::fire::fire::fire:](https://github.com/aws/opsworks-cookbooks) [![GitHub stars](https://img.shields.io/github/stars/aws/opsworks-cookbooks?style=flat)](https://github.com/aws/opsworks-cookbooks/stargazers) - Chef Cookbooks.
* [opsworks-demo-php-photo-share-app](https://github.com/awslabs/opsworks-demo-php-photo-share-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-demo-php-photo-share-app?style=flat)](https://github.com/awslabs/opsworks-demo-php-photo-share-app/stargazers) - Simple PHP photo share app.
* [opsworks-demo-php-simple-app](https://github.com/awslabs/opsworks-demo-php-simple-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-demo-php-simple-app?style=flat)](https://github.com/awslabs/opsworks-demo-php-simple-app/stargazers) - Simple PHP app.
* [opsworks-demo-rails-photo-share-app](https://github.com/awslabs/opsworks-demo-rails-photo-share-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-demo-rails-photo-share-app?style=flat)](https://github.com/awslabs/opsworks-demo-rails-photo-share-app/stargazers) - A sample Rails app.
* [opsworks-elasticsearch-cookbook](https://github.com/awslabs/opsworks-elasticsearch-cookbook) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-elasticsearch-cookbook?style=flat)](https://github.com/awslabs/opsworks-elasticsearch-cookbook/stargazers) - Elasticsearch sample cookbook.
* [opsworks-example-cookbooks :fire:](https://github.com/awslabs/opsworks-example-cookbooks) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-example-cookbooks?style=flat)](https://github.com/awslabs/opsworks-example-cookbooks/stargazers) - Cookbooks used with the sample apps.
* [opsworks-first-cookbook](https://github.com/awslabs/opsworks-first-cookbook) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-first-cookbook?style=flat)](https://github.com/awslabs/opsworks-first-cookbook/stargazers) - Cookbook used to demonstrate simple recipes.
* [opsworks-windows-demo-](https://github.com/awslabs/opsworks-windows-demo-nodejs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-windows-demo-nodejs?style=flat)](https://github.com/awslabs/opsworks-windows-demo-nodejs/stargazers) - A sample Node.JS app.
* [opsworks-windows-demo-cookbooks](https://github.com/awslabs/opsworks-windows-demo-cookbooks) [![GitHub stars](https://img.shields.io/github/stars/awslabs/opsworks-windows-demo-cookbooks?style=flat)](https://github.com/awslabs/opsworks-windows-demo-cookbooks/stargazers) - Cookbooks for Windows.
* [todo-sample-app-cookbooks](https://github.com/awslabs/todo-sample-app-cookbooks) [![GitHub stars](https://img.shields.io/github/stars/awslabs/todo-sample-app-cookbooks?style=flat)](https://github.com/awslabs/todo-sample-app-cookbooks/stargazers) - Custom cookbooks associated with the todo-sample-app.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### Redshift

AWS Repos:

* [aws-lambda-redshift-loader :fire::fire::fire:](https://github.com/awslabs/aws-lambda-redshift-loader) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-lambda-redshift-loader?style=flat)](https://github.com/awslabs/aws-lambda-redshift-loader/stargazers) - Lambda database loader.
* [amazon-redshift-utils :fire::fire::fire::fire::fire:](https://github.com/awslabs/amazon-redshift-utils) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-redshift-utils?style=flat)](https://github.com/awslabs/amazon-redshift-utils/stargazers) - Applies optimal Column Encoding to existing Tables.

Community Repos:

* [Lumoslabs/aleph](https://github.com/lumoslabs/aleph) [![GitHub stars](https://img.shields.io/github/stars/lumoslabs/aleph?style=flat)](https://github.com/lumoslabs/aleph/stargazers) - A full featured web application for writing and running Redshift
queries. Supports revision tracking of queries and has basic visualization support.
* [getredash/redash :fire::fire::fire::fire::fire:](https://github.com/getredash/redash/) [![GitHub stars](https://img.shields.io/github/stars/getredash/redash/?style=flat)](https://github.com/getredash/redash//stargazers) - A web application that allows to easily query an existing database, share the dataset and visualize it in different ways. Initially was developed to work with Redshift, and has great support for it.
* [everythingMe/redshift_console](https://github.com/EverythingMe/redshift_console) [![GitHub stars](https://img.shields.io/github/stars/EverythingMe/redshift_console?style=flat)](https://github.com/EverythingMe/redshift_console/stargazers) -  A simple tool to monitor and manage a Redshift cluster. The first release has basic tools to monitor running queries, WLM queue and your tables/schemas.

### Route 53

AWS Repos:

* [route53-infima :fire::fire:](https://github.com/awslabs/route53-infima) [![GitHub stars](https://img.shields.io/github/stars/awslabs/route53-infima?style=flat)](https://github.com/awslabs/route53-infima/stargazers) - Manages service-level fault isolation.

Community Repos:

* [barnybug/cli53 :fire::fire::fire::fire:](https://github.com/barnybug/cli53) [![GitHub stars](https://img.shields.io/github/stars/barnybug/cli53?style=flat)](https://github.com/barnybug/cli53/stargazers) - cli53 is a command line tool for Amazon Route 53 which provides import and export from BIND format and simple command line management of Route 53 domains.
* [winebarrel/roadworker :fire::fire:](https://github.com/winebarrel/roadworker) [![GitHub stars](https://img.shields.io/github/stars/winebarrel/roadworker?style=flat)](https://github.com/winebarrel/roadworker/stargazers) - Roadworker is a tool to manage Route53. It defines the state of Route53 using DSL, and updates Route53 according to DSL.

### S3

Community Repos:

* [anomalizer/ngx_aws_auth :fire::fire:](https://github.com/anomalizer/ngx_aws_auth) [![GitHub stars](https://img.shields.io/github/stars/anomalizer/ngx_aws_auth?style=flat)](https://github.com/anomalizer/ngx_aws_auth/stargazers) - Implements proxying of authenticated requests.
* [bloomreach/s4cmd :fire::fire::fire::fire:](https://github.com/bloomreach/s4cmd) [![GitHub stars](https://img.shields.io/github/stars/bloomreach/s4cmd?style=flat)](https://github.com/bloomreach/s4cmd/stargazers) - S3 command line tool, faster than S3cmd for large files.
* [CulturalMe/meteor-slingshot :fire::fire::fire:](https://github.com/CulturalMe/meteor-slingshot) [![GitHub stars](https://img.shields.io/github/stars/CulturalMe/meteor-slingshot?style=flat)](https://github.com/CulturalMe/meteor-slingshot/stargazers) - Upload files in meteor.
* [danilop/yas3fs :fire::fire::fire:](https://github.com/danilop/yas3fs) [![GitHub stars](https://img.shields.io/github/stars/danilop/yas3fs?style=flat)](https://github.com/danilop/yas3fs/stargazers) - Yet Another S3-backed File System, inspired by s3fs.
* [grippy/node-s3](https://github.com/grippy/node-s3) [![GitHub stars](https://img.shields.io/github/stars/grippy/node-s3?style=flat)](https://github.com/grippy/node-s3/stargazers) - Node.js app to manage buckets.
* [jubos/fake-s3 :fire::fire::fire::fire::fire:](https://github.com/jubos/fake-s3) [![GitHub stars](https://img.shields.io/github/stars/jubos/fake-s3?style=flat)](https://github.com/jubos/fake-s3/stargazers) - Lightweight S3 clone that simulates most commands.
* [kahing/goofys :fire::fire::fire::fire::fire:](https://github.com/kahing/goofys) [![GitHub stars](https://img.shields.io/github/stars/kahing/goofys?style=flat)](https://github.com/kahing/goofys/stargazers) -  a Filey System for Amazon S3 written in Go.
* [littlstar/s3renity :fire::fire::fire::fire:](https://github.com/littlstar/s3renity) [![GitHub stars](https://img.shields.io/github/stars/littlstar/s3renity?style=flat)](https://github.com/littlstar/s3renity/stargazers) - Batch functions with concurrency control (each, map, reduce, filter, join)
* [marcel/aws-s3 :fire::fire::fire:](https://github.com/marcel/aws-s3) [![GitHub stars](https://img.shields.io/github/stars/marcel/aws-s3?style=flat)](https://github.com/marcel/aws-s3/stargazers) - Ruby implementation of Amazon's S3 REST API.
* [mardix/flask-cloudy :fire::fire:](https://github.com/mardix/flask-cloudy) [![GitHub stars](https://img.shields.io/github/stars/mardix/flask-cloudy?style=flat)](https://github.com/mardix/flask-cloudy/stargazers) - Flask extension.
* [MathieuLoutre/grunt-aws-s3 :fire::fire:](https://github.com/MathieuLoutre/grunt-aws-s3) [![GitHub stars](https://img.shields.io/github/stars/MathieuLoutre/grunt-aws-s3?style=flat)](https://github.com/MathieuLoutre/grunt-aws-s3/stargazers) - Grunt plugin.
* [mickael-kerjean/filestash :fire::fire::fire::fire::fire:](https://github.com/mickael-kerjean/filestash) [![GitHub stars](https://img.shields.io/github/stars/mickael-kerjean/filestash?style=flat)](https://github.com/mickael-kerjean/filestash/stargazers) - A modern web client for S3.
* [minio/mc :fire::fire::fire::fire::fire:](https://github.com/minio/mc) [![GitHub stars](https://img.shields.io/github/stars/minio/mc?style=flat)](https://github.com/minio/mc/stargazers) -  Minio Client for filesystem and cloud storage.
* [minio/minio :fire::fire::fire::fire::fire:](https://github.com/minio/minio) [![GitHub stars](https://img.shields.io/github/stars/minio/minio?style=flat)](https://github.com/minio/minio/stargazers) - Object storage server compatible with S3.
* [mumrah/s3-multipart :fire:](https://github.com/mumrah/s3-multipart) [![GitHub stars](https://img.shields.io/github/stars/mumrah/s3-multipart?style=flat)](https://github.com/mumrah/s3-multipart/stargazers) - Parallel upload/download to S3 via Python.
* [ncw/rclone :fire::fire::fire::fire::fire:](https://github.com/ncw/rclone) [![GitHub stars](https://img.shields.io/github/stars/ncw/rclone?style=flat)](https://github.com/ncw/rclone/stargazers) - Rsync for various cloud storage providers such as S3.
* [owocki/s3_disk_util :fire:](https://github.com/owocki/s3_disk_util) [![GitHub stars](https://img.shields.io/github/stars/owocki/s3_disk_util?style=flat)](https://github.com/owocki/s3_disk_util/stargazers) - S3 Disk usage (du) utility.
* [peak/s5cmd :fire::fire::fire:](https://github.com/peak/s5cmd) [![GitHub stars](https://img.shields.io/github/stars/peak/s5cmd?style=flat)](https://github.com/peak/s5cmd/stargazers) - Fast S3 and local filesystem execution tool with wildcard and batch command support.
* [pgherveou/gulp-awspublish :fire::fire:](https://github.com/pgherveou/gulp-awspublish) [![GitHub stars](https://img.shields.io/github/stars/pgherveou/gulp-awspublish?style=flat)](https://github.com/pgherveou/gulp-awspublish/stargazers) - Gulp plugin.
* [rlmcpherson/s3gof3r :fire::fire::fire::fire:](https://github.com/rlmcpherson/s3gof3r) [![GitHub stars](https://img.shields.io/github/stars/rlmcpherson/s3gof3r?style=flat)](https://github.com/rlmcpherson/s3gof3r/stargazers) - Fast, concurrent, streaming access, includes a CLI.
* [s3git/s3git :fire::fire::fire::fire:](https://github.com/s3git/s3git) [![GitHub stars](https://img.shields.io/github/stars/s3git/s3git?style=flat)](https://github.com/s3git/s3git/stargazers) - CLI tool that allows you to create a distributed, decentralized and versioned repository.
* [s3fs-fuse/s3fs-fuse :fire::fire::fire::fire::fire:](https://github.com/s3fs-fuse/s3fs-fuse) [![GitHub stars](https://img.shields.io/github/stars/s3fs-fuse/s3fs-fuse?style=flat)](https://github.com/s3fs-fuse/s3fs-fuse/stargazers) - Allows Linux and Mac OS X to mount an S3 bucket via FUSE.
* [s3tools/s3cmd :fire::fire::fire::fire::fire:](https://github.com/s3tools/s3cmd) [![GitHub stars](https://img.shields.io/github/stars/s3tools/s3cmd?style=flat)](https://github.com/s3tools/s3cmd/stargazers) - CLI for managing S3 and CloudFront.
* [schickling/git-s3 :fire::fire:](https://github.com/schickling/git-s3) [![GitHub stars](https://img.shields.io/github/stars/schickling/git-s3?style=flat)](https://github.com/schickling/git-s3/stargazers) - Deploy your git repo to a bucket.
* [sorentwo/carrierwave-aws :fire::fire:](https://github.com/sorentwo/carrierwave-aws) [![GitHub stars](https://img.shields.io/github/stars/sorentwo/carrierwave-aws?style=flat)](https://github.com/sorentwo/carrierwave-aws/stargazers) - Adapter for CarrierWave.
* [spring-projects/aws-maven :fire::fire:](https://github.com/spring-projects/aws-maven) [![GitHub stars](https://img.shields.io/github/stars/spring-projects/aws-maven?style=flat)](https://github.com/spring-projects/aws-maven/stargazers) -  Maven Wagon for S3.
* [tongwang/s3fs-c :fire:](https://github.com/tongwang/s3fs-c) [![GitHub stars](https://img.shields.io/github/stars/tongwang/s3fs-c?style=flat)](https://github.com/tongwang/s3fs-c/stargazers) - Mounts buckets for use on a local file system.
* [mishudark/s3-parallel-put :fire::fire:](https://github.com/mishudark/s3-parallel-put) [![GitHub stars](https://img.shields.io/github/stars/mishudark/s3-parallel-put?style=flat)](https://github.com/mishudark/s3-parallel-put/stargazers) - CLI that supports parallel uploads.
* [waynehoover/s3_direct_upload :fire::fire::fire:](https://github.com/waynehoover/s3_direct_upload) [![GitHub stars](https://img.shields.io/github/stars/waynehoover/s3_direct_upload?style=flat)](https://github.com/waynehoover/s3_direct_upload/stargazers) - Direct Upload to Amazon S3 With CORS
* [weavejester/clj-aws-s3 :fire:](https://github.com/weavejester/clj-aws-s3) [![GitHub stars](https://img.shields.io/github/stars/weavejester/clj-aws-s3?style=flat)](https://github.com/weavejester/clj-aws-s3/stargazers) - Client library for Clojure.

### SES

Community Repos:

* [drewblas/aws-ses :fire::fire::fire:](https://github.com/drewblas/aws-ses) [![GitHub stars](https://img.shields.io/github/stars/drewblas/aws-ses?style=flat)](https://github.com/drewblas/aws-ses/stargazers) - Provides an easy ruby DSL & interface.
* [microapps/MoonMail :fire::fire::fire::fire:](https://github.com/microapps/MoonMail) [![GitHub stars](https://img.shields.io/github/stars/microapps/MoonMail?style=flat)](https://github.com/microapps/MoonMail/stargazers) - Shoot billions of emails using SES and Lambda.

### Simple Workflow

AWS Repos:

* [aws-flow-ruby :fire:](https://github.com/aws/aws-flow-ruby) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-flow-ruby?style=flat)](https://github.com/aws/aws-flow-ruby/stargazers) - Creates background jobs and multistep workflows.
* [aws-flow-ruby-samples](https://github.com/awslabs/aws-flow-ruby-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-flow-ruby-samples?style=flat)](https://github.com/awslabs/aws-flow-ruby-samples/stargazers) - AWS Flow Framework for Ruby samples.
* [aws-flow-ruby-opsworks-helloworld](https://github.com/awslabs/aws-flow-ruby-opsworks-helloworld) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-flow-ruby-opsworks-helloworld?style=flat)](https://github.com/awslabs/aws-flow-ruby-opsworks-helloworld/stargazers) - Hello World sample.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### SimpleDB

Community Repos:

* [rjrodger/simpledb :fire:](https://github.com/rjrodger/simpledb) [![GitHub stars](https://img.shields.io/github/stars/rjrodger/simpledb?style=flat)](https://github.com/rjrodger/simpledb/stargazers) - Node.js library.

### SNS

AWS Repos:

* [aws-php-sns-message-validator :fire:](https://github.com/aws/aws-php-sns-message-validator) [![GitHub stars](https://img.shields.io/github/stars/aws/aws-php-sns-message-validator?style=flat)](https://github.com/aws/aws-php-sns-message-validator/stargazers) - Message validation for PHP.

Community Repos:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### SQS

AWS Repos:

* [amazon-sqs-java-messaging-lib :fire:](https://github.com/awslabs/amazon-sqs-java-messaging-lib) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amazon-sqs-java-messaging-lib?style=flat)](https://github.com/awslabs/amazon-sqs-java-messaging-lib/stargazers) - Holds the Java Message Service to communicate with SQS.

Community Repos:

* [phstc/shoryuken :fire::fire::fire::fire:](https://github.com/phstc/shoryuken) [![GitHub stars](https://img.shields.io/github/stars/phstc/shoryuken?style=flat)](https://github.com/phstc/shoryuken/stargazers) - A super efficient SQS thread based message processor for Ruby.

### Data

AWS Repos:

* [aws-data-wrangler :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-data-wrangler) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-data-wrangler?style=flat)](https://github.com/awslabs/aws-data-wrangler/stargazers) - Connects Pandas DataFrames and AWS data related services.

Community Repos:

* [donnemartin/data-science-ipython-notebooks :fire::fire::fire::fire::fire:](https://github.com/donnemartin/data-science-ipython-notebooks) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/data-science-ipython-notebooks?style=flat)](https://github.com/donnemartin/data-science-ipython-notebooks/stargazers) - Big data/data science notebooks.
* [everpeace/vagrant-mesos :fire::fire:](https://github.com/everpeace/vagrant-mesos) [![GitHub stars](https://img.shields.io/github/stars/everpeace/vagrant-mesos?style=flat)](https://github.com/everpeace/vagrant-mesos/stargazers) - Spin up your Mesos Cluster with Vagrant.
* [jhorey/ferry :fire::fire:](https://github.com/jhorey/ferry) [![GitHub stars](https://img.shields.io/github/stars/jhorey/ferry?style=flat)](https://github.com/jhorey/ferry/stargazers) -  Define, run, and deploy big data apps using Docker.
* [nathanmarz/storm-deploy :fire::fire::fire:](https://github.com/nathanmarz/storm-deploy) [![GitHub stars](https://img.shields.io/github/stars/nathanmarz/storm-deploy?style=flat)](https://github.com/nathanmarz/storm-deploy/stargazers) - One click deploy for Storm clusters.

### DevOps

Community Repos:

* [cloud-custodian/cloud-custodian :fire::fire::fire::fire::fire:](https://github.com/cloud-custodian/cloud-custodian) [![GitHub stars](https://img.shields.io/github/stars/cloud-custodian/cloud-custodian?style=flat)](https://github.com/cloud-custodian/cloud-custodian/stargazers) - Rules engine for management, DSL in yaml for query, filter, and actions on resources.
* [chef-cookbooks/aws :fire::fire:](https://github.com/chef-cookbooks/aws) [![GitHub stars](https://img.shields.io/github/stars/chef-cookbooks/aws?style=flat)](https://github.com/chef-cookbooks/aws/stargazers) - Development repository for aws Chef cookbook.
* [colinbjohnson/aws-missing-tools :fire::fire::fire::fire:](https://github.com/colinbjohnson/aws-missing-tools) [![GitHub stars](https://img.shields.io/github/stars/colinbjohnson/aws-missing-tools?style=flat)](https://github.com/colinbjohnson/aws-missing-tools/stargazers) - Tools for managing resources including EC2, EBS, RDS and Route53.
* [k1LoW/awspec :fire::fire::fire::fire:](https://github.com/k1LoW/awspec) [![GitHub stars](https://img.shields.io/github/stars/k1LoW/awspec?style=flat)](https://github.com/k1LoW/awspec/stargazers) - RSpec tests your resources.
* [mitchellh/vagrant-aws :fire::fire::fire::fire::fire:](https://github.com/mitchellh/vagrant-aws) [![GitHub stars](https://img.shields.io/github/stars/mitchellh/vagrant-aws?style=flat)](https://github.com/mitchellh/vagrant-aws/stargazers) - Use Vagrant to manage your EC2 and VPC instances.
* [NixOS/nixops :fire::fire::fire::fire:](https://github.com/NixOS/nixops) [![GitHub stars](https://img.shields.io/github/stars/NixOS/nixops?style=flat)](https://github.com/NixOS/nixops/stargazers) - Use NixOS to provision EC2 instances, S3 buckets, and other resources.

### Security

AWS Repos:

* [aws-sha256-agentcs](https://github.com/awslabs/aws-sha256-agentcs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sha256-agentcs?style=flat)](https://github.com/awslabs/aws-sha256-agentcs/stargazers) - SHA256 Agent Compatibility Ccanner.
* [aws-tvm-anonymous](https://github.com/awslabs/aws-tvm-anonymous) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-tvm-anonymous?style=flat)](https://github.com/awslabs/aws-tvm-anonymous/stargazers) - Token Vending Machine for Anonymous Registration.
* [aws-tvm-identity](https://github.com/awslabs/aws-tvm-identity) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-tvm-identity?style=flat)](https://github.com/awslabs/aws-tvm-identity/stargazers) - Token Vending Machine for Identity Registration.
* [s2n :fire::fire::fire::fire::fire:](https://github.com/awslabs/s2n) [![GitHub stars](https://img.shields.io/github/stars/awslabs/s2n?style=flat)](https://github.com/awslabs/s2n/stargazers) - An implementation of the TLS/SSL protocols.

Community Repos:

* [AdRoll/hologram :fire::fire::fire:](https://github.com/AdRoll/hologram) [![GitHub stars](https://img.shields.io/github/stars/AdRoll/hologram?style=flat)](https://github.com/AdRoll/hologram/stargazers) - Easy, painless credentials on developer laptops.
* [alex/letsencrypt-aws :fire::fire::fire:](https://github.com/alex/letsencrypt-aws) [![GitHub stars](https://img.shields.io/github/stars/alex/letsencrypt-aws?style=flat)](https://github.com/alex/letsencrypt-aws/stargazers) - Automatically provision and update certificates.
* [bridgecrewio/checkov :fire::fire::fire::fire::fire:](https://github.com/bridgecrewio/checkov) [![GitHub stars](https://img.shields.io/github/stars/bridgecrewio/checkov?style=flat)](https://github.com/bridgecrewio/checkov/stargazers) - Terraform static analysis, verifies security best practices.
* [cloudsploit/scans :fire::fire::fire::fire:](https://github.com/cloudsploit/scans) [![GitHub stars](https://img.shields.io/github/stars/cloudsploit/scans?style=flat)](https://github.com/cloudsploit/scans/stargazers) - Detects security risks.
* [iSECPartners/Scout2 :fire::fire::fire::fire:](https://github.com/iSECPartners/Scout2) [![GitHub stars](https://img.shields.io/github/stars/iSECPartners/Scout2?style=flat)](https://github.com/iSECPartners/Scout2/stargazers) - Security auditing tool.
* [jordanpotti/AWSBucketDump :fire::fire::fire::fire:](https://github.com/jordanpotti/AWSBucketDump) [![GitHub stars](https://img.shields.io/github/stars/jordanpotti/AWSBucketDump?style=flat)](https://github.com/jordanpotti/AWSBucketDump/stargazers) - Security Tool to Look For Interesting Files in S3 Buckets.
* [Netflix/bless :fire::fire::fire::fire::fire:](https://github.com/Netflix/bless) [![GitHub stars](https://img.shields.io/github/stars/Netflix/bless?style=flat)](https://github.com/Netflix/bless/stargazers) - SSH Certificate Authority that runs as a Lambda function.
* [Netflix/security_monkey :fire::fire::fire::fire::fire:](https://github.com/Netflix/security_monkey) [![GitHub stars](https://img.shields.io/github/stars/Netflix/security_monkey?style=flat)](https://github.com/Netflix/security_monkey/stargazers) - Monitors policy changes and alerts on insecure configurations.
* [RiotGames/cloud-inquisitor :fire::fire:](https://github.com/RiotGames/cloud-inquisitor) [![GitHub stars](https://img.shields.io/github/stars/RiotGames/cloud-inquisitor?style=flat)](https://github.com/RiotGames/cloud-inquisitor/stargazers) - Tool to enforce ownership and data security.
* [salesforce/policy_sentry :fire::fire::fire::fire:](https://github.com/salesforce/policy_sentry/) [![GitHub stars](https://img.shields.io/github/stars/salesforce/policy_sentry/?style=flat)](https://github.com/salesforce/policy_sentry//stargazers) - IAM Least Privilege Policy Generator.
* [sebsto/AWSVPN :fire:](https://github.com/sebsto/AWSVPN) [![GitHub stars](https://img.shields.io/github/stars/sebsto/AWSVPN?style=flat)](https://github.com/sebsto/AWSVPN/stargazers) - Start a private VPN server in the cloud.
* [trailofbits/algo :fire::fire::fire::fire::fire:](https://github.com/trailofbits/algo) [![GitHub stars](https://img.shields.io/github/stars/trailofbits/algo?style=flat)](https://github.com/trailofbits/algo/stargazers) - Set up a personal IPSEC VPN on EC2 and other cloud services.
* [ttlequals0/autovpn :fire::fire::fire::fire:](https://github.com/ttlequals0/autovpn) [![GitHub stars](https://img.shields.io/github/stars/ttlequals0/autovpn?style=flat)](https://github.com/ttlequals0/autovpn/stargazers) - Create On Demand Disposable OpenVPN Endpoints.

### Accompanying Repos

AWS Repos:

*Repos Accompanying Blogs, Training Events, and Conferences.*

* [aws-arch-backoff-simulator :fire:](https://github.com/awslabs/aws-arch-backoff-simulator) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-arch-backoff-simulator?style=flat)](https://github.com/awslabs/aws-arch-backoff-simulator/stargazers) - Jitter and backoff Simulator for AWS architecture blog.
* [aws-big-data-blog :fire::fire::fire:](https://github.com/awslabs/aws-big-data-blog) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-big-data-blog?style=flat)](https://github.com/awslabs/aws-big-data-blog/stargazers) - Samples from the AWS Big Data Blog.
* [aws-demo-php-simple-app](https://github.com/awslabs/aws-demo-php-simple-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-demo-php-simple-app?style=flat)](https://github.com/awslabs/aws-demo-php-simple-app/stargazers) - PHP apps from the AWS Blogs.
* [aws-mobile-sample-wif](https://github.com/awslabs/aws-mobile-sample-wif) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-mobile-sample-wif?style=flat)](https://github.com/awslabs/aws-mobile-sample-wif/stargazers) - Samples from the AWS Mobile SDK blog.
* [aws-mobile-self-paced-labs-samples](https://github.com/awslabs/aws-mobile-self-paced-labs-samples) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-mobile-self-paced-labs-samples?style=flat)](https://github.com/awslabs/aws-mobile-self-paced-labs-samples/stargazers) - Android Snake Game from a self-paced lab.
* [aws-quickstart](https://github.com/aws-quickstart/) [![GitHub stars](https://img.shields.io/github/stars/aws-quickstart/?style=flat)](https://github.com/aws-quickstart//stargazers) - Official repository for AWS Quick Start.
* [aws-spot-labs :fire::fire::fire:](https://github.com/awslabs/aws-spot-labs) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-spot-labs?style=flat)](https://github.com/awslabs/aws-spot-labs/stargazers) - Best practices using AWS Spot Instances.
* [aws-training-demo :fire:](https://github.com/awslabs/aws-training-demo) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-training-demo?style=flat)](https://github.com/awslabs/aws-training-demo/stargazers) - Demos from the Technical Trainers community.
* [java-meme-generator-sample](https://github.com/awslabs/java-meme-generator-sample) [![GitHub stars](https://img.shields.io/github/stars/awslabs/java-meme-generator-sample?style=flat)](https://github.com/awslabs/java-meme-generator-sample/stargazers) - Meme generation app from re:Invent 2012.
* [railsconf2013-tech-demo :fire:](https://github.com/awslabs/railsconf2013-tech-demo) [![GitHub stars](https://img.shields.io/github/stars/awslabs/railsconf2013-tech-demo?style=flat)](https://github.com/awslabs/railsconf2013-tech-demo/stargazers) - Seahorse demo from RailsConf 2013.
* [reinvent2013-js-blog-demo](https://github.com/awslabs/reinvent2013-js-blog-demo) [![GitHub stars](https://img.shields.io/github/stars/awslabs/reinvent2013-js-blog-demo?style=flat)](https://github.com/awslabs/reinvent2013-js-blog-demo/stargazers) - Demo blogging app from re:Invent 2013.
* [reinvent2013-mobile-photo-share](https://github.com/awslabs/reinvent2013-mobile-photo-share) [![GitHub stars](https://img.shields.io/github/stars/awslabs/reinvent2013-mobile-photo-share?style=flat)](https://github.com/awslabs/reinvent2013-mobile-photo-share/stargazers) - Mobile photo share app from re:Invent 2014.
* [reinvent2014-scalable-site-management](https://github.com/awslabs/reinvent2014-scalable-site-management) [![GitHub stars](https://img.shields.io/github/stars/awslabs/reinvent2014-scalable-site-management?style=flat)](https://github.com/awslabs/reinvent2014-scalable-site-management/stargazers) - Scalable site management sample from re:Invent 2014.
* [reinvent2015-dev309](https://github.com/awslabs/reinvent2015-dev309) [![GitHub stars](https://img.shields.io/github/stars/awslabs/reinvent2015-dev309?style=flat)](https://github.com/awslabs/reinvent2015-dev309/stargazers) - Large Scale Metrics Analysis from re:Invent 2015.
* [timely-security-analytics](https://github.com/awslabs/timely-security-analytics) [![GitHub stars](https://img.shields.io/github/stars/awslabs/timely-security-analytics?style=flat)](https://github.com/awslabs/timely-security-analytics/stargazers) - Security analytics sample from 2015 re:Invent 2015.
* [todo-sample-app](https://github.com/awslabs/todo-sample-app) [![GitHub stars](https://img.shields.io/github/stars/awslabs/todo-sample-app?style=flat)](https://github.com/awslabs/todo-sample-app/stargazers) - Simple "Todo" app from RailsConf 2014.

Community Repos:

* [startup-class/setup :fire::fire:](https://github.com/startup-class/setup) [![GitHub stars](https://img.shields.io/github/stars/startup-class/setup?style=flat)](https://github.com/startup-class/setup/stargazers) -  EC2 setup files for Startup Engineering MOOC.

### Miscellaneous Repos

AWS Repos:

* [amediamanager](https://github.com/awslabs/amediamanager) [![GitHub stars](https://img.shields.io/github/stars/awslabs/amediamanager?style=flat)](https://github.com/awslabs/amediamanager/stargazers) - Media manager.
* [aws-hal-client-java](https://github.com/awslabs/aws-hal-client-java) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-hal-client-java?style=flat)](https://github.com/awslabs/aws-hal-client-java/stargazers) - Java client for the Hypertext Application Language.
* [aws-model-validators](https://github.com/awslabs/aws-model-validators) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-model-validators?style=flat)](https://github.com/awslabs/aws-model-validators/stargazers) - Tools for validating the AWS service JSON model files.
* [aws-sdk-js-sample-video-transcoder](https://github.com/awslabs/aws-sdk-js-sample-video-transcoder) [![GitHub stars](https://img.shields.io/github/stars/awslabs/aws-sdk-js-sample-video-transcoder?style=flat)](https://github.com/awslabs/aws-sdk-js-sample-video-transcoder/stargazers) - Sample cross-platform video transcoder app.
* [simplebeerservice :fire::fire:](https://github.com/awslabs/simplebeerservice) [![GitHub stars](https://img.shields.io/github/stars/awslabs/simplebeerservice?style=flat)](https://github.com/awslabs/simplebeerservice/stargazers) - Cloud-connected kegerator that streams live sensor data to AWS.

Community Repos:

* [bcoe/thumbd :fire::fire:](https://github.com/bcoe/thumbd) [![GitHub stars](https://img.shields.io/github/stars/bcoe/thumbd?style=flat)](https://github.com/bcoe/thumbd/stargazers) - Node.js/ImageMagick-based image thumbnailing service.
* [cdkpatterns/serverless :fire::fire::fire::fire:](https://github.com/cdk-patterns/serverless) [![GitHub stars](https://img.shields.io/github/stars/cdk-patterns/serverless?style=flat)](https://github.com/cdk-patterns/serverless/stargazers) - Deployable serverless architecture patterns built in AWS CDK.
* [Comcast/cmb :fire::fire:](https://github.com/Comcast/cmb) [![GitHub stars](https://img.shields.io/github/stars/Comcast/cmb?style=flat)](https://github.com/Comcast/cmb/stargazers) - Highly available, horizontally scalable queuing and notification service.
* [convox/rack :fire::fire::fire::fire:](https://github.com/convox/rack) [![GitHub stars](https://img.shields.io/github/stars/convox/rack?style=flat)](https://github.com/convox/rack/stargazers) - Open-source PaaS on AWS.
* [devops-israel/aws-inventory :fire::fire:](https://github.com/devops-israel/aws-inventory) [![GitHub stars](https://img.shields.io/github/stars/devops-israel/aws-inventory?style=flat)](https://github.com/devops-israel/aws-inventory/stargazers) - Display all your AWS resources on a single web page.
* [donnemartin/dev-setup :fire::fire::fire::fire:](https://github.com/donnemartin/dev-setup) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/dev-setup?style=flat)](https://github.com/donnemartin/dev-setup/stargazers) - Mac setup of various developer tools and AWS services.
* [dtan4/terraforming :fire::fire::fire::fire::fire:](https://github.com/dtan4/terraforming) [![GitHub stars](https://img.shields.io/github/stars/dtan4/terraforming?style=flat)](https://github.com/dtan4/terraforming/stargazers) - Export existing resources to Terraform style (tf, tfstate).
* [segmentio/stack :fire::fire::fire::fire::fire:](https://github.com/segmentio/stack) [![GitHub stars](https://img.shields.io/github/stars/segmentio/stack?style=flat)](https://github.com/segmentio/stack/stargazers) - A set of Terraform modules for configuring production infrastructure.
* [j2labs/microarmy ](https://github.com/j2labs/microarmy) [![GitHub stars](https://img.shields.io/github/stars/j2labs/microarmy?style=flat)](https://github.com/j2labs/microarmy/stargazers) - Deploy micro instances to launch a coordinated siege.
* [jpillora/grunt-aws :fire:](https://github.com/jpillora/grunt-aws) [![GitHub stars](https://img.shields.io/github/stars/jpillora/grunt-aws?style=flat)](https://github.com/jpillora/grunt-aws/stargazers) - Grunt interface into the Node.JS SDK.
* [jvehent/haproxy-aws :fire::fire:](https://github.com/jvehent/haproxy-aws) [![GitHub stars](https://img.shields.io/github/stars/jvehent/haproxy-aws?style=flat)](https://github.com/jvehent/haproxy-aws/stargazers) - Documentation on building a HTTPS stack with HAProxy.
* [localstack/localstack :fire::fire::fire::fire::fire:](https://github.com/localstack/localstack) [![GitHub stars](https://img.shields.io/github/stars/localstack/localstack?style=flat)](https://github.com/localstack/localstack/stargazers) - A fully functional local AWS cloud stack. Develop and test your cloud apps offline!
* [meducation/propono :fire::fire:](https://github.com/meducation/propono) [![GitHub stars](https://img.shields.io/github/stars/meducation/propono?style=flat)](https://github.com/meducation/propono/stargazers) - Easy-to-use pub/sub in Ruby.
* [mozilla/awsbox :fire::fire::fire:](https://github.com/mozilla/awsbox) [![GitHub stars](https://img.shields.io/github/stars/mozilla/awsbox?style=flat)](https://github.com/mozilla/awsbox/stargazers) - A featherweight PaaS on top of EC2 for deploying node apps.
* [Netflix/aminator :fire::fire::fire:](https://github.com/Netflix/aminator) [![GitHub stars](https://img.shields.io/github/stars/Netflix/aminator?style=flat)](https://github.com/Netflix/aminator/stargazers) - A tool for creating EBS AMIs.
* [Netflix/archaius :fire::fire::fire::fire::fire:](https://github.com/Netflix/archaius) [![GitHub stars](https://img.shields.io/github/stars/Netflix/archaius?style=flat)](https://github.com/Netflix/archaius/stargazers) - Library for configuration management API.
* [Netflix/asgard :fire::fire::fire::fire::fire:](https://github.com/Netflix/asgard) [![GitHub stars](https://img.shields.io/github/stars/Netflix/asgard?style=flat)](https://github.com/Netflix/asgard/stargazers) - Web interface for application deployments and cloud management.
* [Netflix/aws-autoscaling :fire::fire:](https://github.com/Netflix/aws-autoscaling) [![GitHub stars](https://img.shields.io/github/stars/Netflix/aws-autoscaling?style=flat)](https://github.com/Netflix/aws-autoscaling/stargazers) - Tools for using auto scaling and documentation best practices.
* [Netflix/chaosmonkey :fire::fire::fire::fire::fire:](https://github.com/Netflix/chaosmonkey) [![GitHub stars](https://img.shields.io/github/stars/Netflix/chaosmonkey?style=flat)](https://github.com/Netflix/chaosmonkey/stargazers) - Resiliency tool that helps applications tolerate random instance failures.
* [Netflix/eureka :fire::fire::fire::fire::fire:](https://github.com/Netflix/eureka) [![GitHub stars](https://img.shields.io/github/stars/Netflix/eureka?style=flat)](https://github.com/Netflix/eureka/stargazers) - Service registry for resilient mid-tier load balancing and failover.
* [Netflix/EVCache :fire::fire::fire::fire:](https://github.com/Netflix/EVCache) [![GitHub stars](https://img.shields.io/github/stars/Netflix/EVCache?style=flat)](https://github.com/Netflix/EVCache/stargazers) - A distributed in-memory data store.
* [Netflix/Fenzo :fire::fire::fire:](https://github.com/Netflix/Fenzo) [![GitHub stars](https://img.shields.io/github/stars/Netflix/Fenzo?style=flat)](https://github.com/Netflix/Fenzo/stargazers) - Extensible Scheduler for Mesos Frameworks.
* [Netflix/ice :fire::fire::fire::fire::fire:](https://github.com/Netflix/ice) [![GitHub stars](https://img.shields.io/github/stars/Netflix/ice?style=flat)](https://github.com/Netflix/ice/stargazers) - Usage and cost monitoring tool.
* [Netflix/ribbon :fire::fire::fire::fire::fire:](https://github.com/Netflix/ribbon) [![GitHub stars](https://img.shields.io/github/stars/Netflix/ribbon?style=flat)](https://github.com/Netflix/ribbon/stargazers) - Remote procedure call library with built in software load balancers.
* [Netflix/SimianArmy :fire::fire::fire::fire::fire:](https://github.com/Netflix/SimianArmy) [![GitHub stars](https://img.shields.io/github/stars/Netflix/SimianArmy?style=flat)](https://github.com/Netflix/SimianArmy/stargazers) - Tools to keep your cloud operating in top form.
* [Netflix/zuul :fire::fire::fire::fire::fire:](https://github.com/Netflix/zuul) [![GitHub stars](https://img.shields.io/github/stars/Netflix/zuul?style=flat)](https://github.com/Netflix/zuul/stargazers) - Edge service that provides dynamic routing, monitoring, resiliency, security, and more.
* [niftylettuce/gulp-aws-splash :fire::fire:](https://github.com/niftylettuce/gulp-aws-splash) [![GitHub stars](https://img.shields.io/github/stars/niftylettuce/gulp-aws-splash?style=flat)](https://github.com/niftylettuce/gulp-aws-splash/stargazers) - Open-source LaunchRock alternative. Build beautiful splash pages.
* [puppetlabs/puppetlabs-aws :fire:](https://github.com/puppetlabs/puppetlabs-aws) [![GitHub stars](https://img.shields.io/github/stars/puppetlabs/puppetlabs-aws?style=flat)](https://github.com/puppetlabs/puppetlabs-aws/stargazers) - Puppet module for managing resources to build out infrastructure.
* [mhart/react-server-routing-example :fire::fire:](https://github.com/mhart/react-server-routing-example) [![GitHub stars](https://img.shields.io/github/stars/mhart/react-server-routing-example?style=flat)](https://github.com/mhart/react-server-routing-example/stargazers) - Sample universal client/server routing and data in React.
* [Similarweb/finala :fire::fire::fire:](https://github.com/similarweb/finala) [![GitHub stars](https://img.shields.io/github/stars/similarweb/finala?style=flat)](https://github.com/similarweb/finala/stargazers) - A resource cloud scanner that analyzes and reports wasteful and unused resources to cut unwanted expenses.
* [snowplow/snowplow :fire::fire::fire::fire::fire:](https://github.com/snowplow/snowplow) [![GitHub stars](https://img.shields.io/github/stars/snowplow/snowplow?style=flat)](https://github.com/snowplow/snowplow/stargazers) - Enterprise-strength web, mobile and event analytics, powered by Hadoop, Kafka, Kinesis, Redshift and Elasticsearch.
* [Spinnaker/spinnaker :fire::fire::fire::fire::fire:](https://github.com/Spinnaker/spinnaker) [![GitHub stars](https://img.shields.io/github/stars/Spinnaker/spinnaker?style=flat)](https://github.com/Spinnaker/spinnaker/stargazers) - Successor to asgard supporting pipelines and more.
* [spulec/moto :fire::fire::fire::fire::fire:](https://github.com/spulec/moto) [![GitHub stars](https://img.shields.io/github/stars/spulec/moto?style=flat)](https://github.com/spulec/moto/stargazers) - Allows your python tests to easily mock out the boto library.

## Guides, Books, Documentation, and Training

*How-to's, training, whitepapers, docs, and case studies.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/LxYDN5K.png">
</p>
<br/>

### Getting Started Guides

AWS Guides:

* [Getting Started with AWS](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-intro.html)
* [Getting Started Tutorials](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html)
    * [Run a Virtual Server](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2614)
    * [Store Files](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2683)
    * [Share Digital Media](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2755)
    * [Deploy a Website](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2767)
    * [Host a Website (Linux)](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2836)
    * [Host a Website (Windows)](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2908)
    * [Run a Database](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2980)
    * [Analyze Your Data](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e3065)

Community Guides:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### General Guides

AWS Guides:

* [Analyzing Big Data](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
* [Working with the AWS Management Console](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html)
* [Deploying a Web App Using Elastic Beanstalk](http://docs.aws.amazon.com/gettingstarted/latest/deploy/overview.html)
* [Hosting a Web App](http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/web-app-hosting-intro.html)
* [Hosting a .NET Web App](http://docs.aws.amazon.com/gettingstarted/latest/wah/web-app-hosting-intro.html)
* [Hosting a Static Website](http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html)
* [Quick Start Deployment Guides](https://aws.amazon.com/documentation/quickstart/)

Community Guides:

* [Open Guide to AWS :fire::fire::fire::fire::fire:](https://github.com/open-guides/og-aws) [![GitHub stars](https://img.shields.io/github/stars/open-guides/og-aws?style=flat)](https://github.com/open-guides/og-aws/stargazers)

### Books

* Amazon Web Services in Action [Manning](https://www.manning.com/books/amazon-web-services-in-action) or [Amazon.com](http://amzn.com/1617292885)
* AWS Lambda in Action [Manning](https://www.manning.com/books/aws-lambda-in-action) or [Amazon.com](http://amzn.com/1617293717) - [Code Repo :fire::fire:](https://github.com/danilop/AWS_Lambda_in_Action) [![GitHub stars](https://img.shields.io/github/stars/danilop/AWS_Lambda_in_Action?style=flat)](https://github.com/danilop/AWS_Lambda_in_Action/stargazers)

### Whitepapers

* [AWS Well-Architected Framework](https://d0.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)
* [Whitepapers](https://aws.amazon.com/whitepapers/)

### Documentation

* [Documentation](https://aws.amazon.com/documentation/)
* [AWS Billing and Cost Management](https://aws.amazon.com/documentation/account-billing/)
* [AWS Marketplace](https://aws.amazon.com/documentation/marketplace/)
* [AWS Support](https://aws.amazon.com/documentation/aws-support/)
* [AWS General Reference](http://docs.aws.amazon.com/general/latest/gr/)
* [AWS Glossary](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

### Training

* [Training and Certification](https://aws.amazon.com/training/)
* [Webinars](https://aws.amazon.com/about-aws/events/)

### Case Studies: Powered by AWS

* [Adobe](https://aws.amazon.com/solutions/case-studies/adobe/)
* [AdRoll](https://aws.amazon.com/solutions/case-studies/adroll/)
* [Airbnb](https://aws.amazon.com/solutions/case-studies/airbnb/)
* [Autodesk](https://aws.amazon.com/solutions/case-studies/autodesk/)
* [Citrix](https://aws.amazon.com/solutions/case-studies/citrix/)
* [Comcast](https://aws.amazon.com/solutions/case-studies/comcast/)
* [Coursera](https://aws.amazon.com/solutions/case-studies/coursera/)
* [Docker](https://aws.amazon.com/solutions/case-studies/docker/)
* [Dow Jones](https://aws.amazon.com/solutions/case-studies/dow-jones/)
* [Dropbox](https://www.dropbox.com/)
* [Dropcam](https://aws.amazon.com/solutions/case-studies/dropcam/)
* [Expedia](https://aws.amazon.com/solutions/case-studies/expedia/)
* [Foursquare](https://aws.amazon.com/solutions/case-studies/foursquare/)
* [IMDb](https://aws.amazon.com/solutions/case-studies/imdb/)
* [Instrumental](https://instrumentalapp.com/blog/aws-kinesis/)
* [Intuit](https://aws.amazon.com/solutions/case-studies/soasta-intuit/)
* [Johnson & Johnson](https://aws.amazon.com/solutions/case-studies/johnson-and-johnson/)
* [Lionsgate](https://aws.amazon.com/solutions/case-studies/lionsgate/)
* [mlbam](https://aws.amazon.com/solutions/case-studies/major-league-baseball-mlbam/)
* [NASA](https://aws.amazon.com/solutions/case-studies/nasa-jpl-curiosity/)
* [Netflix](https://aws.amazon.com/solutions/case-studies/netflix/)
* [Nike](https://web.archive.org/web/20150910200649/http://aws.amazon.com/solutions/case-studies/nike/)
* [Nokia](https://web.archive.org/web/20161210062336/https://aws.amazon.com/solutions/case-studies/nokia/)
* [PBS](https://aws.amazon.com/solutions/case-studies/pbs/)
* [Pfizer](https://web.archive.org/web/20161210034734/https://aws.amazon.com/solutions/case-studies/pfizer/)
* [Philips](https://aws.amazon.com/solutions/case-studies/philips/)
* [Reddit](https://web.archive.org/web/20150905070945/https://aws.amazon.com/solutions/case-studies/reddit/)
* [Samsung](https://aws.amazon.com/solutions/case-studies/samsung/)
* [Siemens](https://aws.amazon.com/solutions/case-studies/siemens/)
* [Slack](https://aws.amazon.com/solutions/case-studies/slack/)
* [Spotify](https://web.archive.org/web/20180608043124/https://aws.amazon.com/solutions/case-studies/spotify/)
* [Swiftkey](https://web.archive.org/web/20160410051253/https://aws.amazon.com/solutions/case-studies/swiftkey/)
* [The Weather Company](https://aws.amazon.com/solutions/case-studies/the-weather-company/)
* [Ticketmaster](https://aws.amazon.com/solutions/case-studies/ticketmaster/)
* [Time Inc](https://aws.amazon.com/solutions/case-studies/time-inc/)
* [Twilio](https://aws.amazon.com/solutions/case-studies/twilio/)
* [U.S. Department of State](https://aws.amazon.com/solutions/case-studies/exchangesconnect/)
* [Ubisoft](https://aws.amazon.com/solutions/case-studies/ubisoft/)
* [Yelp](https://aws.amazon.com/solutions/case-studies/yelp-docker/)
* [Zillow](https://aws.amazon.com/solutions/case-studies/zillow/)

## Social

*Blogs, discussion groups, conferences, and social media.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/kRRBa1e.png">
</p>
<br/>

### Blogs

AWS Blogs:

* [Official Blog](https://aws.amazon.com/blogs/aws/)
    * [Brasil](https://aws.amazon.com/pt/blogs/aws-brasil/)
    * [China](https://aws.amazon.com/cn/blogs/china/)
    * [Germany](https://aws.amazon.com/de/blogs/germany/)
    * [Japan](https://aws.amazon.com/jp/blogs/news/)
    * [Korea](http://aws.amazon.com/ko/blogs/korea/)
* [DevOps](https://aws.amazon.com/blogs/devops/)
* [Architecture](https://aws.amazon.com/blogs/architecture/)
* [Big Data](https://aws.amazon.com/blogs/big-data/)
* [Compute](https://aws.amazon.com/blogs/compute/)
* [Mobile](https://aws.amazon.com/blogs/mobile/)
* [Messaging](https://aws.amazon.com/blogs/messaging-and-targeting/)
* [Java](https://aws.amazon.com/blogs/developer/category/programing-language/java/)
* [PHP](https://aws.amazon.com/blogs/developer/category/programing-language/php/)
* [Ruby](https://aws.amazon.com/blogs/developer/category/programing-language/ruby/)
* [.NET](https://aws.amazon.com/blogs/developer/category/programing-language/dot-net/)
* [Security](https://aws.amazon.com/blogs/security/)
* [Startup](https://medium.com/aws-activate-startup-blog)
* [Partner Network](https://aws.amazon.com/blogs/apn/)
* [SAP](https://aws.amazon.com/blogs/awsforsap/)

Community Blogs:

* [All Things Distributed](http://www.allthingsdistributed.com/) - Werner Vogels, AWS CTO.
* [Things I Like...](http://jeff-barr.com/) - Jeff Barr, AWS Chief Evangelist.
* [Netflix Tech Blog](http://techblog.netflix.com/)
* [A Curated List of Engineering Blogs](https://github.com/kilimchoi/engineering-blogs) [![GitHub stars](https://img.shields.io/github/stars/kilimchoi/engineering-blogs?style=flat)](https://github.com/kilimchoi/engineering-blogs/stargazers)
* [AWS Geek](https://www.awsgeek.com/)

### Twitter Influencers

AWS Tweeps:

* [@awscloud](https://twitter.com/awscloud) - Official Twitter feed.
* [@AWS_Partners](https://twitter.com/AWS_Partners)
* [@AWSIdentity](https://twitter.com/AWSIdentity)
* [@AWSMarketplace](https://twitter.com/AWSMarketplace)
* [@AWSreInvent](https://twitter.com/AWSreInvent) - Official Twitter account for re:Invent.
* [@AWSStartups](https://twitter.com/AWSStartups)
* [@ajassy](https://twitter.com/ajassy) - Andy Jassy: Senior Vice-President.
* [@Ianmmmm](https://twitter.com/Ianmmmm) - Ian Massingham - Technical Evangelist.
* [@jeffbarr](https://twitter.com/jeffbarr) - Jeff Barr: Chief Evangelist.
* [@mndoci](https://twitter.com/mndoci) - Deepak Singh: GM EC2.
* [@mza](https://twitter.com/mza) - Matt Wood: Product Strategy.
* [@Werner](https://twitter.com/Werner) - Werner Vogels: CTO.
* [Community heroes, Evangelists, etc](https://twitter.com/awscloud/lists)

Community Tweeps:

* [@kennwhite](https://twitter.com/kennwhite)
* [@esh](https://twitter.com/esh)
* [@garnaat](https://twitter.com/garnaat)
* [@quinnypig](https://twitter.com/quinnypig)
* [@awsgeek](https://twitter.com/awsgeek)

### Facebook Pages

AWS Pages:

* [amazonwebservices](https://www.facebook.com/amazonwebservices) - Official Facebook page.
* [awsreinvent](https://www.facebook.com/awsreinvent) - Official Facebook page for re:Invent.

Community Pages:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

### YouTube Channels

AWS Channels:

* [AmazonWebServices](https://www.youtube.com/user/AmazonWebServices)
* [AWSDeutsch](https://www.youtube.com/user/AWSAktuell)
* [AWSJapan](https://www.youtube.com/user/AmazonWebServicesJP)
* [AWSKorea](https://www.youtube.com/user/AWSKorea)
* [AWSLatinAmerica](https://www.youtube.com/channel/UCvaUAVzIIGsRNlUDWkQFCeA)
* [AWSTutorialSeries](https://www.youtube.com/user/awstutorialseries)
* [AWSWebinars](https://www.youtube.com/user/AWSwebinars)

Community Channels:

* [Backspace Academy](https://www.youtube.com/channel/UCav3fsasRc5VOqvZiT5avgw)
* [Cloud Academy](https://www.youtube.com/channel/UCeRY0LppLWdxWAymRANTb0g/videos)
* [Linux Academy](https://www.youtube.com/user/pineheadtv/playlists)

### LinkedIn Groups

AWS Page:

* [Amazon Web Services](https://www.linkedin.com/company/amazon-web-services)

Community Groups:

* [Amazon AWS Architects](https://www.linkedin.com/grp/home?gid=4387417)
* [Amazon AWS Architects, Engineers, Developers, Consultants, Entrepreneurs Experts](https://www.linkedin.com/grps?gid=3748455)
* [Amazon Web Services (AWS) for Business](https://www.linkedin.com/grps?gid=5122002)
* [Amazon Web Services Architects](https://www.linkedin.com/grps?gid=4233997)
* [Amazon Web Services Community Network](https://www.linkedin.com/grp/home?gid=49531)
* [Amazon Web Services Enthusiasts](https://www.linkedin.com/grps?gid=2485626)
* [Amazon Web Services Users](https://www.linkedin.com/grps?gid=86137)

### Subreddits

* [/r/aws/](https://www.reddit.com/r/aws/)
* [/r/AWS_cloud/](https://www.reddit.com/r/AWS_cloud/)

### Conferences

AWS Conferences:

* [re:Invent](https://reinvent.awsevents.com/) - Annual user conference. The event features keynote announcements, training and certification opportunities, over 250 technical sessions, a partner expo, after hours activities, and more.
* [Summits](https://aws.amazon.com/summits/) - Global one-day events that are designed to educate new customers about the AWS platform and offer existing customers deep technical content to be more successful with AWS.
* [AWSome Day](https://aws.amazon.com/events/awsome-day/awsome-day-online/) - Global one-day events are delivered by AWS Education's technical instructors and are ideal for IT pros, developers and technical managers who would like to learn about how to get started in the AWS Cloud.

Community Conferences:

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md/stargazers)

## Latest KPIs and Stats

*Latest key performance indicators and other interesting stats.*

<br/>
<p align="center">
  <img src="http://i.imgur.com/KP2TmJv.png">
</p>
<br/>

* Over 1 million customers active in past 30 days.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* $7B+ annual revenue run-rate business.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
    * 81% year over year revenue growth.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* EC2 usage up 95% year over year.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* S3 data transfer up 120% year over year.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
    * S3 holds trillions of objects and regularly peaks at 1.5 million requests per second.<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>
* Database services usage up 127% year over year.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
    * $1B annual revenue run-rate business.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* 2 million new EBS volumes created per day.<sup>[4](https://www.youtube.com/watch?v=OuyUbvtgfDk)</sup>
* Customers have launched more than 15 million Hadoop clusters.<sup>[3](http://www.forbes.com/sites/benkepes/2014/11/25/scale-beyond-comprehension-some-aws-numbers/)</sup>
* 102Tbps network capacity into a data center.<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>
* 500+ major new features and services launched since 2014.<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* All 14 other cloud providers combined have 1/5th the aggregate capacity of AWS.<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>
* Every day, AWS adds enough new server capacity to support all of Amazon's global infrastructure when it was a $7B annual revenue enterprise (in 2004).<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>

## Appendix of Core Services

*Appendix of official services, grouped by service category.*

### Services in Plain English

* [Amazon Web Services in Plain English](https://www.expeditedssl.com/aws-in-plain-english) - Entertaining and educational, a community contribution.

### Compute Services

* [Auto Scaling](https://aws.amazon.com/autoscaling/) - Launches or terminates EC2 instances based on policies, schedules, and health checks.
* [Batch](https://aws.amazon.com/batch/) - Run batch jobs at scale.
* [Blox](https://blox.github.io/) - Open source projects for building custom schedulers on ECS.
* [EC2 Container Service (ECS)](https://aws.amazon.com/ecs/) - Supports Docker containers on EC2 instances.
* [EC2 Systems Manager](https://aws.amazon.com/ec2/systems-manager/) - Easily configure and manage EC2 and on-premises systems.
* [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) - Provides quick deployment and management of applications in the cloud.
* [Elastic Compute Cloud (EC2)](http://aws.amazon.com/ec2/) - Provides scalable virtual private servers using Xen.
* [Elastic GPUs](https://aws.amazon.com/ec2/Elastic-GPUs/) - Attach low-cost GPUs to EC2 instances for graphics acceleration.
* [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) - Automatically distributes incoming traffic across multiple EC2 instances.
* [Lambda](https://aws.amazon.com/lambda/) - Runs code in response to events and automatically manages EC2 instances.
* [Lightsail](https://amazonlightsail.com/) - Launch and manage simple virtual private servers.
* [Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) - Creates a logically isolated set of EC2 instances which can be connected to an existing network using a VPN connection.

### Networking Services

* [Direct Connect](https://aws.amazon.com/directconnect/) - Provides dedicated connections to AWS for faster and cheaper data throughput.
* [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) - Automatically distributes incoming traffic across multiple EC2 instances.
* [Route 53](https://aws.amazon.com/route53/) - Provides a highly available and scalable Domain Name System (DNS) web service.
* [Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) - Creates a logically isolated set of EC2 instances which can be connected to an existing network using a VPN connection.

### Enterprise Applications

* [WorkDocs](https://aws.amazon.com/workdocs/) - Provides a fully managed, secure enterprise storage and sharing service.
* [WorkMail](https://aws.amazon.com/workmail/) - Provides managed email and calendaring service.
* [WorkSpaces](https://aws.amazon.com/workspaces/) - Provides a cloud-based desktop experience to end-users.
* [Workspaces Application Manager (WAM)](http://aws.amazon.com/workspaces/applicationmanager/) - Simplifies deployment and management of WorkSpaces.

### Analytics Services

* [Athena](https://aws.amazon.com/athena/) - Query data on S3 instantly.
* [Data Pipeline](https://aws.amazon.com/datapipeline/) - Provides workload management by processing and moving data between services.
* [Elastic MapReduce (EMR)](http://aws.amazon.com/elasticmapreduce/) - Hosts a Hadoop and Spark framework running on EC2 and S3.
* [Elasticsearch Service (ES)](https://aws.amazon.com/elasticsearch-service/) - Managed Elasticsearch, a popular open-source search and analytics engine.
* [Glue](https://aws.amazon.com/glue/) - Prepare and load data to data stores.
* [Kinesis](https://aws.amazon.com/kinesis/) - Provides real-time data processing over large, distributed data streams.
* [Kinesis Analytics](https://aws.amazon.com/kinesis/analytics/) - Write standard SQL queries on streaming data without having to learn any new programming skills.
* [Kinesis Firehose](https://aws.amazon.com/kinesis/firehose/) - Captures and automatically loads streaming data into S3 and Redshift.
* [Quicksight](https://aws.amazon.com/quicksight/) - Provides cloud-powered business intelligence for 1/10th the cost of traditional BI solutions.
* [Redshift](https://aws.amazon.com/redshift/) - Provides petabyte-scale data warehousing with columnar storage and multi-node compute.

### Artificial Intelligence

* [Lex](https://aws.amazon.com/lex/) - Build conversational interfaces through voice or text.
* [Machine Learning](https://aws.amazon.com/machine-learning/) - Provides managed machine learning technology.
* [Polly](https://aws.amazon.com/polly/) - Turn text into lifelike speech.
* [Rekognition](https://aws.amazon.com/rekognition/) - Deep learning-based image analysis.

### Management Tools

* [CloudFormation](https://aws.amazon.com/cloudformation/) - Provides a file-based interface for provisioning other resources.
* [CloudTrail](https://aws.amazon.com/cloudtrail/) - Provides logs of all activity.
* [CloudWatch](https://aws.amazon.com/cloudwatch/) - Provides monitoring for AWS cloud resources and applications, starting with EC2.
* [Command Line Interface (CLI)](https://aws.amazon.com/cli/) - Provides a CLI to manage all services.
* [Config](https://aws.amazon.com/config/) - Provides a detailed view of all resources.
* [Management Console (AWS Console)](https://aws.amazon.com/console/) - A web-based interface to manage all services.
* [OpsWorks](https://aws.amazon.com/opsworks/) - Provides configuration of EC2 services using Chef.
* [Personal Health Dashboard](https://aws.amazon.com/premiumsupport/phd/) - Your personalized view of service health.
* [Service Catalog](https://aws.amazon.com/servicecatalog/) - Service Catalog allows IT administrators to create, manage, and distribute portfolios of approved products to end users, who can then access the products they need in a personalized portal.

### Security and Identity Services

* [Certificate Manager](https://aws.amazon.com/certificate-manager/) - Lets you easily provision, manage, and deploy SSL/TLS certificates for use with AWS services.
* [CloudHSM](https://aws.amazon.com/cloudhsm/) - Helps meet corporate, contractual and regulatory compliance requirements for data security by using dedicated Hardware Security Module (HSM) appliances within the AWS cloud.
* [Directory Service](https://aws.amazon.com/directoryservice/) - A managed service that allows you to connect your resources with an existing on-premises Microsoft Active Directory or to set up a new, stand-alone directory in the AWS Cloud.
* [Identity and Access Management (IAM)](https://aws.amazon.com/iam/) - An implicit service, the authentication infrastructure used to authenticate access to the various services.
* [Inspector](https://aws.amazon.com/inspector/) - An automated security assessment service that helps improve the security and compliance of applications deployed on AWS.
* [Key Management Service (KMS)](https://aws.amazon.com/kms/) - A managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
* [Shield](https://aws.amazon.com/shield/) - Managed DDoS Protection.
* [WAF](https://aws.amazon.com/waf/) - A web application firewall service that monitors and manages CloudFront distributions.

### Internet of Things Service

* [IoT](https://aws.amazon.com/iot/) - Enables secure, bi-directional communication between internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the AWS cloud over MQTT and HTTP.

### Mobile Services

* [API Gateway](https://aws.amazon.com/api-gateway/) - Service for publishing, maintaining and securing web service APIs.
* [Cognito](https://aws.amazon.com/cognito/) - Provides user identity and data synchronization.
* [Device Farm](https://aws.amazon.com/device-farm/) - App testing service for iOS, Android and Fire OS apps on physical devices.
* [Mobile Analytics](https://aws.amazon.com/mobileanalytics/) - Service for collecting, visualizing, and understanding app usage data.
* [Mobile Hub](https://aws.amazon.com/mobile/) - Provides an integrated console that helps you build, test, and monitor your mobile apps.
* [Pinpoint](https://aws.amazon.com/pinpoint/) - Targeted push notifications for mobile apps.
* [Simple Notification Service (SNS)](https://aws.amazon.com/sns/) - Provides a hosted multi-protocol "push" messaging for applications.

### Storage and Content Delivery Services

* [CloudFront](https://aws.amazon.com/cloudfront/) - A content delivery network (CDN) for distributing objects to locations near the requester.
* [Elastic Block Store (EBS)](https://aws.amazon.com/ebs/) - Provides persistent block-level storage volumes for EC2.
* [Elastic File System (EFS)](https://aws.amazon.com/efs/) - A file storage service for EC2 instances.
* [Glacier](https://aws.amazon.com/glacier/) - Provides a low-cost, long-term storage option, intended for archiving data.
* [Import/Export](https://aws.amazon.com/importexport/) - Accelerates moving large amounts of data into and out of AWS using portable storage devices for transport.
* [Simple Storage Service (S3)](https://aws.amazon.com/s3/) - Provides Web Service based storage.
* [Storage Gateway](https://aws.amazon.com/storagegateway/) - An iSCSI block storage virtual appliance with cloud-based backup.

### Databases

* [Aurora](https://aws.amazon.com/rds/aurora/) - MySQL and PostgreSQL compatible relational database with improved performance.
* [DynamoDB](https://aws.amazon.com/dynamodb/) - Provides a scalable, low-latency NoSQL online Database Service backed by SSDs.
* [ElastiCache](https://aws.amazon.com/elasticache/) - Provides in-memory caching for web apps (Memcached, Redis).
* [Redshift](https://aws.amazon.com/redshift/) - Provides petabyte-scale data warehousing with columnar storage and multi-node compute.
* [Relational Database Service (RDS)](https://aws.amazon.com/rds/) - Provides a scalable database server with MySQL, Oracle, SQL Server, PostgreSQL, and MariaDB support.
* [Schema Conversion Tool](https://aws.amazon.com/documentation/SchemaConversionTool/) - App that helps you convert your database schema from an Oracle or Microsoft SQL Server database, to an RDS MySQL DB instance or an Aurora DB cluster.
* [SimpleDB](https://aws.amazon.com/simpledb/) - Allows developers to run queries on structured data.

### Application Services

* [API Gateway](https://aws.amazon.com/api-gateway/) - Service for publishing, maintaining and securing web service APIs.
* [AppStream](https://aws.amazon.com/appstream/) - Flexible, low-latency streaming service for apps and games.
* [CloudSearch](https://aws.amazon.com/cloudsearch/) - Provides basic full-text search and indexing of textual content.
* [DevPay](https://aws.amazon.com/devpay/) - Provides billing and account management.
* [Elastic Transcoder (ETS)](https://aws.amazon.com/elastictranscoder/) - Provides video transcoding of S3 hosted videos.
* [Flexible Payments Service (FPS)](https://payments.amazon.com/developer) - Provides an interface for micropayments.
* [Simple Email Service (SES)](https://aws.amazon.com/ses/) - Provides bulk and transactional email sending.
* [Simple Notification Service (SNS)](https://aws.amazon.com/sns/) - Provides a hosted multi-protocol "push" messaging for applications.
* [Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) - Provides a hosted message queue for web applications.
* [Simple Workflow (SWF)](https://aws.amazon.com/swf/) - A workflow service for building scalable, resilient applications.
* [Step Functions](https://aws.amazon.com/step-functions/) - Coordinate components of distributed applications.

### Developer Tools

* [CodeBuild](https://aws.amazon.com/codebuild/) - Build and test code.
* [CodeCommit](https://aws.amazon.com/documentation/codecommit/) - Hosted Git version control service.
* [CodeDeploy](https://aws.amazon.com/codedeploy/) - Provides automated code deployment to EC2 instances.
* [CodePipeline](https://aws.amazon.com/documentation/codepipeline/) - Continuous delivery service.
* [Command Line Interface (CLI)](https://aws.amazon.com/cli/) - Provides a CLI to manage all services.
* [X-Ray](https://aws.amazon.com/xray/) - Analyze and debug your applications.

### Miscellaneous Services

* [Fulfillment Web Service](https://aws.amazon.com/about-aws/whats-new/2008/03/19/announcing-amazon-fulfillment-web-service/) - Provides a programmatic web service for sellers to ship items to and from Amazon using Fulfillment by Amazon.
* [Mechanical Turk](https://www.mturk.com/mturk/welcome) - Manages small units of work distributed among many persons.
* [Partner Network (APN)](https://aws.amazon.com/partners/) - Provides partners with the technical information and sales and marketing support to increase business opportunities.
* [Product Advertising API](http://docs.aws.amazon.com/AWSECommerceService/latest/GSG/Welcome.html) - Provides access to product data and electronic commerce functionality.

## Credits

Check out the [Credits page](https://github.com/donnemartin/awesome-aws/blob/master/CREDITS.md) [![GitHub stars](https://img.shields.io/github/stars/donnemartin/awesome-aws/blob/master/CREDITS.md?style=flat)](https://github.com/donnemartin/awesome-aws/blob/master/CREDITS.md/stargazers).

## Other Awesome Lists

Other awesome lists can be found in [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) and [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) [![GitHub stars](https://img.shields.io/github/stars/bayandin/awesome-awesomeness?style=flat)](https://github.com/bayandin/awesome-awesomeness/stargazers).

## Contact Info

Feel free to contact me to discuss any issues, questions, or comments.

My contact info can be found on my [GitHub page](https://github.com/donnemartin) [![GitHub stars](https://img.shields.io/github/stars/donnemartin?style=flat)](https://github.com/donnemartin/stargazers).

## License

*I am providing code and resources in this repository to you under an open source license.  Because this is my personal repository, the license you receive to my code and resources is from me and not my employer (Facebook).*

    Copyright 2017 Donne Martin

    Creative Commons Attribution 4.0 International License (CC BY 4.0)

    http://creativecommons.org/licenses/by/4.0/
