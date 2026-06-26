# JMeter

[![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-jmeter?style=flat)](https://github.com/aliesbelik/awesome-jmeter/stargazers)

# Awesome JMeter [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
A curated collection of resources covering [Apache JMeter](https://jmeter.apache.org/) and related stuff and shiny things: plugins, integrations, testing techniques, DevOps practices, etc.

<!--lint ignore double-link match-punctuation -->
[<img src="assets/images/jmeter-logo.svg" align="right" width="260" alt="Apache JMeter">](https://jmeter.apache.org/)

<!--lint ignore double-link-->
> [Apache JMeter](https://jmeter.apache.org/) is open source, pure Java application designed to load test functional behavior and measure performance.

<!--lint ignore double-link-->
This list grew up from [an occasional answer](https://sqa.stackexchange.com/a/2552/1842) on Stack Exchange and personal JMeter-related links collection, got further inspiration from [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers) project and improved by these [amazing contributors](CONTRIBUTORS.md).

## Contents

<!--lint ignore double-link-->
- [Official Resources](#official-resources)
- [Distributions](#distributions)
- [Getting Started](#getting-started)
- [Tutorials](#tutorials)
- [Best Practices](#best-practices)
- [Scripting](#scripting)
- [Automation](#automation)
  - [DSL](#dsl)
  - [Packages](#packages)
  - [Frameworks](#frameworks)
  - [Conversion](#conversion)
- [CI](#ci)
  - [Tools & Plugins](#tools--plugins)
  - [Tutorials & Demo](#tutorials--demo)
- [Distributed Testing](#distributed-testing)
- [Cloud Services / SaaS](#cloud-services--saas)
- [Results Processing](#results-processing)
  - [Results Analysis](#results-analysis)
  - [Reporting & Visualization](#reporting--visualization)
- [Performance Testing](#performance-testing)
  - [Streaming Protocols](#streaming-protocols)
  - [Mobile Apps](#mobile-apps)
  - [Mainframe Environments](#mainframe-environments)
  - [RPC Frameworks](#rpc-frameworks)
  - [RESTful API](#restful-api)
- [Tools](#tools)
  - [Plugins](#plugins)
  - [Correlation](#correlation)
  - [Extending JMeter](#extending-jmeter)
  - [IDE Integration](#ide-integration)
  - [Editors](#editors)
  - [Utilities](#utilities)
  - [AI](#ai)
- [APM Integration](#apm-integration)
- [JMeter Performance](#jmeter-performance)
- [Tips & Tricks](#tips--tricks)
- [Books](#books)
- [Trainings & Courses](#trainings--courses)
- [Videos](#videos)
- [Community](#community)
  - [Blogs](#blogs)
  - [Forums](#forums)
  - [Twitter](#twitter)
  - [Q&A](#qa)
- [Related](#related)
  - [Awesome Lists](#awesome-lists)
  - [Other](#other)

## Official Resources

<!--lint ignore double-link-->
- [Apache JMeter Project](https://jmeter.apache.org/) - Apache JMeter official website.
- [GitHub Repository](https://github.com/apache/jmeter) [![GitHub stars](https://img.shields.io/github/stars/apache/jmeter?style=flat)](https://github.com/apache/jmeter/stargazers) - Apache JMeter source code repository.
- [JMeter Wiki](https://cwiki.apache.org/confluence/display/jmeter) - Apache JMeter official documentation.
- [Issue Tracking](https://jmeter.apache.org/issues.html) - Apache JMeter issue tracking system.
- [Mailing Lists](https://jmeter.apache.org/mail2.html) - Apache JMeter mailing lists.

## Distributions

- [Download Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) - Apache JMeter: Official downloads.
- [JMeter for Windows](https://sourceforge.net/projects/jmeterforwindows/) - Package for installation JMeter with plugins.
- [JMeter Bootstrap](https://github.com/cfpb/jmeter-bootstrap) [![GitHub stars](https://img.shields.io/github/stars/cfpb/jmeter-bootstrap?style=flat)](https://github.com/cfpb/jmeter-bootstrap/stargazers) - Solution to setup JMeter and JMeter plugins, suitable to be used as a submodule.

## Getting Started

- [Getting Started with Apache JMeter](https://dzone.com/refcardz/getting-started-with-apache-jmeter)
- [The Beginner's Guide to Performance Testing with Apache JMeter](https://medium.com/better-programming/the-beginners-guide-to-performance-testing-with-apache-jmeter-5cc52c327ff6)
- JMeter — Performance and Load Testing: Beginner's Guide: [part 1](https://ekremkurt1907.medium.com/jmeter-performance-and-load-testing-beginners-guide-part-i-5121604bf97a), [part 2](https://ekremkurt1907.medium.com/jmeter-performance-and-load-testing-beginners-guide-part-ii-7edb98b0d2c3)

## Tutorials

- [JMeter Tutorial](https://artoftesting.com/jmeter-tutorial) - By ArtOfTesting.
- Load Testing with JMeter: [part 1](https://lincolnloop.com/blog/load-testing-jmeter-part-1-getting-started/), [part 2](https://lincolnloop.com/blog/load-testing-jmeter-part-2-headless-testing-and-je/), [part 3](https://lincolnloop.com/blog/load-testing-jmeter-part-3-replaying-apache-logs/) - By Brandon Konkle.
- [JMeter Tutorial](https://www.tutorialspoint.com/jmeter/) - By Tutorials Point.
- [JMeter Tutorial for Load Testing: The Ultimate Guide](https://www.javacodegeeks.com/2014/11/jmeter-tutorial-load-testing.html) - By Daniel Gutierrez Diez.
- [JMeter: Load Development Lifecycle](https://datacadamia.com/jmeter/lifecycle) - By DataCadamia.
- [Load Testing with Apache JMeter](https://www.digitalocean.com/community/tutorial-series/load-testing-with-apache-jmeter) - By Mitchell Anicas @ DigitalOcean.
- [JMeter Tutorial for Beginners](https://www.guru99.com/jmeter-tutorials.html) - By Guru99.
- [JMeter Tutorials](https://qaautomation.expert/2023/12/07/jmeter-tutorials/) - By QA Automation Expert.
- [Web App Load Testing Using Maven Plugins for Apache JMeter, and Analyzing the Results](https://dzone.com/articles/running-load-test-web-app-using-maven-plugins) - By Vincent DABURON.

## Best Practices

- [JMeter Official Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
- [Optimize JMeter for Large Scale Tests](https://blog.octoperf.com/optimize-jmeter-for-large-scale-tests/)
- [Concurrent, High Throughput Performance Testing with JMeter](https://howtojboss.wordpress.com/2012/07/31/concurrent-high-throughput-performance-testing-with-jmeter/)

## Scripting

- [Beanshell vs JSR223 vs Java JMeter Scripting](https://www.blazemeter.com/blog/beanshell-vs-jsr223-vs-jmeter) - Most popular scripting mechanisms performance comparison.
- [Testing with Groovy](https://static.packt-cdn.com/downloads/Testingwithgroovy.pdf) - Using JMeter and Groovy for load testing.

## Automation

### DSL

- [jmeter-java-dsl](https://abstracta.github.io/jmeter-java-dsl/) - Simple Java API to run JMeter performance tests in an VCS and programmers friendly way.
- [jmeter-dotnet-dsl](https://abstracta.github.io/jmeter-dotnet-dsl/) - Simple .Net API to run JMeter performance tests in an VCS and programmers friendly way.
- [jmeter-groovy-dsl](https://github.com/smicyk/groovy-jmeter) [![GitHub stars](https://img.shields.io/github/stars/smicyk/groovy-jmeter?style=flat)](https://github.com/smicyk/groovy-jmeter/stargazers) - The Groovy-JMeter project is simple DSL to write JMeter test plans.
- [jmeter-as-code](https://github.com/anasoid/jmeter-as-code) [![GitHub stars](https://img.shields.io/github/stars/anasoid/jmeter-as-code?style=flat)](https://github.com/anasoid/jmeter-as-code/stargazers) - Simple wrapper for JMeter to write and execute JMeter tests with Java.
- [pymeter](https://github.com/eldaduzman/pymeter) [![GitHub stars](https://img.shields.io/github/stars/eldaduzman/pymeter?style=flat)](https://github.com/eldaduzman/pymeter/stargazers) - Simple JMeter performance tests API for Python.

### Packages

- [loadtest](https://github.com/tmobile/loadtest) [![GitHub stars](https://img.shields.io/github/stars/tmobile/loadtest?style=flat)](https://github.com/tmobile/loadtest/stargazers) - An R package for load testing using JMeter.

### Frameworks

- [Taurus](https://gettaurus.org/) - Automation-friendly framework for Continuous Testing.
- [Performance testing framework](https://github.com/serputko/performance-testing-framework) [![GitHub stars](https://img.shields.io/github/stars/serputko/performance-testing-framework?style=flat)](https://github.com/serputko/performance-testing-framework/stargazers) - Framework both for backend load testing with Apache JMeter and frontend load testing with sitespeed.io + webpagetest private instance.
- [JMeter Load Testing Center](https://github.com/innogames/ltc) [![GitHub stars](https://img.shields.io/github/stars/innogames/ltc?style=flat)](https://github.com/innogames/ltc/stargazers) - Online web-application/dashboard to run, monitor and analyze results of load tests using JMeter.
- [MeterSphere](https://github.com/metersphere/metersphere) [![GitHub stars](https://img.shields.io/github/stars/metersphere/metersphere?style=flat)](https://github.com/metersphere/metersphere/stargazers) - One-stop open-source enterprise-class continuous testing platform, compatible with open-source standards such as JMeter :cn:.
- [Carrier](https://github.com/carrier-io) [![GitHub stars](https://img.shields.io/github/stars/carrier-io?style=flat)](https://github.com/carrier-io/stargazers) - Continuous test execution platform with ability to perform load testing using customized JMeter and Gatling containers.

### Conversion

- [swaggerjmx](https://github.com/Pactortester/swaggerjmx) [![GitHub stars](https://img.shields.io/github/stars/Pactortester/swaggerjmx?style=flat)](https://github.com/Pactortester/swaggerjmx/stargazers) - Tool to convert Swagger UI specification into JMeter test plans.
- [postman2jmx](https://github.com/Loadium/postman2jmx) [![GitHub stars](https://img.shields.io/github/stars/Loadium/postman2jmx?style=flat)](https://github.com/Loadium/postman2jmx/stargazers) - Postman collection to JMeter jmx file converter.
- [convert-postman-jmeter](https://github.com/sercheo87/convert-postman-jmeter) [![GitHub stars](https://img.shields.io/github/stars/sercheo87/convert-postman-jmeter?style=flat)](https://github.com/sercheo87/convert-postman-jmeter/stargazers) - Convert Postman projects to JMeter.
- [fiddler2jmeter](https://github.com/dperfly/fiddler2jmeter) [![GitHub stars](https://img.shields.io/github/stars/dperfly/fiddler2jmeter?style=flat)](https://github.com/dperfly/fiddler2jmeter/stargazers) - Fiddler or Charles to JMeter script convertor.
- [har-convertor-jmeter-tool](https://github.com/vdaburon/har-convertor-jmeter-plugin) [![GitHub stars](https://img.shields.io/github/stars/vdaburon/har-convertor-jmeter-plugin?style=flat)](https://github.com/vdaburon/har-convertor-jmeter-plugin/stargazers) - Apache JMeter Plugin to convert a HAR file to a JMeter script and Record XML file.
- [JMeter HAR Importer Plugin](https://github.com/Qytera-Gmbh/JMeterHARImporterPlugin) [![GitHub stars](https://img.shields.io/github/stars/Qytera-Gmbh/JMeterHARImporterPlugin?style=flat)](https://github.com/Qytera-Gmbh/JMeterHARImporterPlugin/stargazers) - JMeter plugin to import HTTP Archive (HAR) files into Apache JMeter.

## CI

### Tools & Plugins

- [JMeter Ant Task](https://github.com/jfifield/ant-jmeter) [![GitHub stars](https://img.shields.io/github/stars/jfifield/ant-jmeter?style=flat)](https://github.com/jfifield/ant-jmeter/stargazers) - Ant task to automate running JMeter test plans.
- [JMeter Maven Plugin](https://github.com/jmeter-maven-plugin/jmeter-maven-plugin) [![GitHub stars](https://img.shields.io/github/stars/jmeter-maven-plugin/jmeter-maven-plugin?style=flat)](https://github.com/jmeter-maven-plugin/jmeter-maven-plugin/stargazers) - Maven plugin that provides the ability to run JMeter tests as part of the build.
- [JMeter Gradle Plugin](https://github.com/jmeter-gradle-plugin/jmeter-gradle-plugin) [![GitHub stars](https://img.shields.io/github/stars/jmeter-gradle-plugin/jmeter-gradle-plugin?style=flat)](https://github.com/jmeter-gradle-plugin/jmeter-gradle-plugin/stargazers) - Gradle plugin to execute JMeter tests.
- [Jenkins Performance Plugin](https://plugins.jenkins.io/performance/) - Jenkins plugin to capture reports from JMeter and generate graphic charts with the trend report of performance and robustness.
- [TeamCity Performance Tests Analysis Plugin](https://github.com/jtorgan/jmeter_plugin) [![GitHub stars](https://img.shields.io/github/stars/jtorgan/jmeter_plugin?style=flat)](https://github.com/jtorgan/jmeter_plugin/stargazers) - TeamCity plugin to organize simplest performance testing in CI 💀.
- [Bamboo JMeter Aggregator Plugin](https://marketplace.atlassian.com/apps/5902/jmeter-aggregator-for-bamboo) - Bamboo plugin to collect, assert and graph JMeter test results.
- [Sonar JMeter Plugin](https://github.com/SonarQubeCommunity/sonar-jmeter) [![GitHub stars](https://img.shields.io/github/stars/SonarQubeCommunity/sonar-jmeter?style=flat)](https://github.com/SonarQubeCommunity/sonar-jmeter/stargazers) - Plugin to collect JMeter performance tests results and display in Sonar dashboard 💀.
- [Lightning](https://deliverymind.github.io/lightning/) - Framework to integrate JMeter non-functional tests with CI/CD server.
- [Taurus JMeter Executor](https://gettaurus.org/docs/JMeter/) - JMeter Executor in Taurus automation framework.
- [PerfAction for JMeter](https://github.com/marketplace/actions/perfaction-for-jmeter) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/perfaction-for-jmeter?style=flat)](https://github.com/marketplace/actions/perfaction-for-jmeter/stargazers) - GitHub Action to run performance tests using Apache JMeter and its plugins.
- [Apache JMeter GitHub Action](https://github.com/marketplace/actions/apache-jmeter) [![GitHub stars](https://img.shields.io/github/stars/marketplace/actions/apache-jmeter?style=flat)](https://github.com/marketplace/actions/apache-jmeter/stargazers) - A GitHub Action for carrying out Apache JMeter performance tests.

### Tutorials & Demo

- Jenkins
  - [Performance Tests with JMeter, Maven and Hudson](https://medium.com/the-server-labs/performance-tests-with-jmeter-maven-and-hudson-d1cbdb3ffad8)
  - [CI with Jenkins, Git, Maven, Grunt, and JMeter](https://github.com/dzuluagaapigee/apigee-ci-jenkins-git-maven-jmeter) [![GitHub stars](https://img.shields.io/github/stars/dzuluagaapigee/apigee-ci-jenkins-git-maven-jmeter?style=flat)](https://github.com/dzuluagaapigee/apigee-ci-jenkins-git-maven-jmeter/stargazers)
  - [Continuous automated web tests using Jenkins and JMeter](https://www.linkedin.com/pulse/continuous-automated-web-tests-using-jenkins-jmeter-mahanta)
  - [Automating JMeter tests with Maven and Jenkins](https://www.codecentric.de/en/knowledge-hub/blog/automating-jmeter-tests-maven-jenkins)
  - How to automate JMeter tests with Maven and Jenkins: [part 1](https://ribblescode.wordpress.com/2012/04/16/how-to-run-jmeter-tests-with-maven/), [part 2](https://ribblescode.wordpress.com/2012/04/16/how-to-automate-jmeter-tests-with-maven-and-jenkins-hudson-8/)
  - JMeter Continuous Performance Testing (JMeter + Ant + Jenkins): [part 1](https://www.testautomationguru.com/jmeter-continuous-performance-testing-part1/), [part 2](https://www.testautomationguru.com/jmeter-continuous-performance-testing-part2/)
  - [Continuous Integration 101: How to Run JMeter with Jenkins](https://dzone.com/articles/continuous-integration-101-how-to-run-jmeter-with)
- Bamboo
  - [How to Run JMeter in a Continuous Integration Environment with Bamboo](https://dzone.com/articles/how-to-run-jmeter-in-a-continuous-integration-envi)
- TeamCity
  - [How to Run JMeter Tests with TeamCity for Continuous Integration](https://web.archive.org/web/20211204112944/https://www.blazemeter.com/blog/how-run-jmeter-tests-teamcity-continuous-integration/)
- CircleCI
  - [How to integrate JMeter into CircleCI](https://www.blazemeter.com/blog/circleci-jmeter)
- SonarQube
  - [JMeter with Sonar](https://testersinaction.blogspot.com/2013/05/v-behaviorurldefaultvmlo_24.html)

## Distributed Testing

- [JMeter Distributed Testing Step-by-step](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.pdf)
- [JMeter Remote Testing](https://jmeter.apache.org/usermanual/remote-test.html)
- [Setting up a JMeter Cluster for web server load testing](https://www.howtoforge.com/setting-up-jmeter-cluster-for-load-testing/)
- Dockerized
  - [Dockerized JMeter](https://gist.github.com/hhcordero/abd1dcaf6654cfe51d0b) - Distributed load testing workflow with Docker and JMeter.
  - [JMeter Docker Images](https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=jmeter&starCount=0)
  - [Distributed JMeter testing using Docker](https://srivaths.blogspot.com/2014/08/distrubuted-jmeter-testing-using-docker.html)
  - [A Docker solution to JMeter + InfluxDB + Grafana performance testing](https://medium.com/@ellenhuang523/a-docker-solution-to-jmeter-influxdb-grafana-performance-testing-568848de7a0f)
  - [AutoMeter](https://github.com/intuit/autometer) [![GitHub stars](https://img.shields.io/github/stars/intuit/autometer?style=flat)](https://github.com/intuit/autometer/stargazers) - An automation tool for scaling load tests using distributed slaves, based on JMeter master-slave architecture.
  - [JMeter Docker Extension](https://hub.docker.com/extensions/qainsights/jmeter-docker-extension) - Docker extension to run JMeter tests from Docker Desktop.
- Testing in Cloud
  - Kubernetes
    - [jmeter-kubernetes](https://github.com/kubernauts/jmeter-kubernetes) [![GitHub stars](https://img.shields.io/github/stars/kubernauts/jmeter-kubernetes?style=flat)](https://github.com/kubernauts/jmeter-kubernetes/stargazers) - JMeter cluster support for Kubernetes and OpenShift.
    - [jmeter-k8s-starterkit](https://github.com/Rbillon59/jmeter-k8s-starterkit) [![GitHub stars](https://img.shields.io/github/stars/Rbillon59/jmeter-k8s-starterkit?style=flat)](https://github.com/Rbillon59/jmeter-k8s-starterkit/stargazers) - JMeter Kubernetes starter kit, with live test reporting, JMeter monitoring, Kubernetes monitoring and mock as a service.
    - [kangal](https://github.com/hellofresh/kangal) [![GitHub stars](https://img.shields.io/github/stars/hellofresh/kangal?style=flat)](https://github.com/hellofresh/kangal/stargazers) - Kubernetes and Go Automatic Loader solution to run performance tests in Kubernetes cluster using multiple load generators.
    - [aks_testing_fwk](https://github.com/petegrimsdale/aks_testing_fwk) [![GitHub stars](https://img.shields.io/github/stars/petegrimsdale/aks_testing_fwk?style=flat)](https://github.com/petegrimsdale/aks_testing_fwk/stargazers) - AKS-based scalable JMeter test framework with Grafana reporting.
  - Amazon Web Services
    - [jmeter-ec2](https://github.com/oliverlloyd/jmeter-ec2/) [![GitHub stars](https://img.shields.io/github/stars/oliverlloyd/jmeter-ec2/?style=flat)](https://github.com/oliverlloyd/jmeter-ec2//stargazers) - Automates running Apache JMeter on Amazon EC2.
    - [gee](https://github.com/kowalcj0/gee) [![GitHub stars](https://img.shields.io/github/stars/kowalcj0/gee?style=flat)](https://github.com/kowalcj0/gee/stargazers) - A modified version of JMeter-EC2 project.
    - [os-jmeter-aws](https://github.com/Aptimyze/os-jmeter-aws) [![GitHub stars](https://img.shields.io/github/stars/Aptimyze/os-jmeter-aws?style=flat)](https://github.com/Aptimyze/os-jmeter-aws/stargazers) - Run JMeter on multiple Amazon EC2 instances, view results in ELK.
    - [Load Testing with JMeter and Amazon EC2](https://medium.com/@alttaf/load-testing-with-jmeter-and-amazon-ec2-e143a7350596)
    - [Performance Testing in the Cloud with JMeter & AWS](https://web.archive.org/web/20190526033436/http://www.artofsoftwaredevelopment.com/performance/performance-testing-in-the-cloud-with-jmeter-aws)
    - [JMeter distributed testing with Amazon EC2](https://vedovini.net/2009/08/17/jmeter-distributed-testing-with-amazon-ec2/)
    - [jmeter-ecs](https://github.com/smithmicro/jmeter-ecs) [![GitHub stars](https://img.shields.io/github/stars/smithmicro/jmeter-ecs?style=flat)](https://github.com/smithmicro/jmeter-ecs/stargazers) - JMeter Docker image for distributed testing on EC2 Container Service (ECS).
  - DigitalOcean
    - [Lightweight JMeter Cloud](https://docs.google.com/presentation/d/1Yi5C27C3Q0AnT-uw9SRnMeEqXSKLQ8h9O9Jqo1gQiyI/) - Building your own JMeter Cloud using DigitalOcean, JMeter and Docker.
  - Microsoft Azure
    - [Load Testing Pipeline with JMeter, ACI and Terraform](https://github.com/Azure-Samples/jmeter-aci-terraform) [![GitHub stars](https://img.shields.io/github/stars/Azure-Samples/jmeter-aci-terraform?style=flat)](https://github.com/Azure-Samples/jmeter-aci-terraform/stargazers) - Scalable cloud load/stress testing pipeline solution with Apache JMeter and Terraform to dynamically provision and destroy the required infrastructure on Azure.

## Cloud Services / SaaS

*List of cloud-based load testing services with support of JMeter test plans execution.*

- [Perforce BlazeMeter](https://www.blazemeter.com/) - Performance engineering platform with JMeter and Selenium support.
- [OctoPerf](https://octoperf.com/) - SaaS and On-Premise Load Testing Tool with JMeter and Selenium support.
- [RedLine13](https://redline13.com/) - AWS-based load testing service with JMeter, Gatling and Selenium scenarios support.
- [OpenText Core Performance Engineering](https://www.opentext.com/products/saas/core-performance-engineering) - OpenText cloud-based solution for web and mobile performance testing with JMeter and Gatling support (formerly Micro Focus LoadRunner Cloud, formerly HP StormRunner Load).
- [Loadium](https://loadium.com/) - AWS-based load testing service with JMeter and Selenium support.
- [Azure Microsoft](https://azure.microsoft.com/en-us/products/app-testing/) - Azure Load Testing Service use Apache JMeter.

## Results Processing

- [JMeter Report Dashboard](https://jmeter.apache.org/usermanual/generating-dashboard.html) - JMeter supports dashboard report generation to get graphs and statistics from a test plan.
- [Latency Lingo](https://latencylingo.com) - Publish test results to generate hosted, interactive dashboards containing insights.

### Results Analysis

<!--lint ignore double-link-->
- [JMeter Log Analysis](https://cwiki.apache.org/confluence/display/jmeter/LogAnalysis) - Suggestions and recipes for JMeter log analysis.
- [Analyzing JMeter Results](https://www.datazoo.de/articles/158/performance-testing-analyzing-jmeter-results)
- [JMeter Result Analysis: The Ultimate Guide](https://blog.octoperf.com/jmeter-result-analysis-the-ultimate-guide/)
- [JtlReporter](https://github.com/ludeknovy/jtl-reporter) [![GitHub stars](https://img.shields.io/github/stars/ludeknovy/jtl-reporter?style=flat)](https://github.com/ludeknovy/jtl-reporter/stargazers) - Online reporting application to generate reports by uploading JTL file.
- [JMeter Result Analysis Plugin](https://github.com/afranken/jmeter-analysis-maven-plugin) [![GitHub stars](https://img.shields.io/github/stars/afranken/jmeter-analysis-maven-plugin?style=flat)](https://github.com/afranken/jmeter-analysis-maven-plugin/stargazers) - Maven plugin that parses JMeter test results and generates detailed reports with charts.
- [JMeter Results Analyser](https://sourceforge.net/projects/jmstats/) - Web-based application for collating, analysing and reporting JMeter test results.
- [JMeter Graph Tool Maven Plugin](https://github.com/vdaburon/jmeter-graph-tool-maven-plugin) [![GitHub stars](https://img.shields.io/github/stars/vdaburon/jmeter-graph-tool-maven-plugin?style=flat)](https://github.com/vdaburon/jmeter-graph-tool-maven-plugin/stargazers) - Maven plugin to create graphs and filter results using CMDRunner and Filter Results Tools from [JMeter Plugins](#plugins); usually used along with the [JMeter Maven Plugin](#tools--plugins) and  set of [companion plugins](https://github.com/vdaburon/jmeter-graph-tool-maven-plugin#compagnion-tools).
- DB Results Collectors
  - [JMeter DBCollector Plugin](https://sourceforge.net/projects/jmeterdbcollect/) - Plugin to enable results logging into a database for more effective reporting.
  - [JMeter MySQLCollector Plugin](https://cwiki.apache.org/confluence/display/jmeter/MysqlCollectorPlugin) - Patch to configure listener to log into MySQL database.
- SLA and KPIs
  - [JMeter SLA Report](https://github.com/sgoeschl/jmeter-sla-report) [![GitHub stars](https://img.shields.io/github/stars/sgoeschl/jmeter-sla-report?style=flat)](https://github.com/sgoeschl/jmeter-sla-report/stargazers) - JMeter HTML report generator based on JAMon.
  - [JMeter JUnit Reporter](https://github.com/tilln/jmeter-junit-reporter) [![GitHub stars](https://img.shields.io/github/stars/tilln/jmeter-junit-reporter?style=flat)](https://github.com/tilln/jmeter-junit-reporter/stargazers) - Apache JMeter plugin for generating JUnit Reports in XML format, based on custom KPIs (Key Performance Indicators).
  - Tools to validate results from KPIs:
    - [JUnit KPI Reporter from JMeter CSV Report](https://github.com/vdaburon/JUnitReportKpiJMeterReportCsv) [![GitHub stars](https://img.shields.io/github/stars/vdaburon/JUnitReportKpiJMeterReportCsv?style=flat)](https://github.com/vdaburon/JUnitReportKpiJMeterReportCsv/stargazers) - Tool to generate JUnit Report based on custom KPIs applied to the JMeter Report CSV file.
    - [JUnit KPI Reporter from JMeter Dashboard Statistics JSON File](https://github.com/vdaburon/JUnitReportKpiJMeterDashboardStats) [![GitHub stars](https://img.shields.io/github/stars/vdaburon/JUnitReportKpiJMeterDashboardStats?style=flat)](https://github.com/vdaburon/JUnitReportKpiJMeterDashboardStats/stargazers) - Tool to generate JUnit Report based on custom KPIs applied to the JMeter Dashboard Statistics JSON file.
    - [JUnit Report Compare 2 JMeter Report CSV Files](https://github.com/vdaburon/JUnitReportKpiCompareJMeterReportCsv) [![GitHub stars](https://img.shields.io/github/stars/vdaburon/JUnitReportKpiCompareJMeterReportCsv?style=flat)](https://github.com/vdaburon/JUnitReportKpiCompareJMeterReportCsv/stargazers) - Tool to compare 2 load tests using JMeter Report CSV files and create a JUnit Report based on custom KPIs.

### Reporting & Visualization

<!--lint ignore double-link-->
- InfluxDB & Grafana
  - [Using JMeter with InfluxDB & Grafana](https://blog.vinsguru.com/category/influxdb/) - Collection of guides to collect and visualize real-time test results and server monitoring stats using InfluxDB & Grafana.
  - [How to Use Grafana to Monitor JMeter Non-GUI Results](https://dzone.com/articles/how-to-use-grafana-to-monitor-jmeter-non-gui-resul)
  - [jmeterReports](https://github.com/kirillyu/jmeterReports) [![GitHub stars](https://img.shields.io/github/stars/kirillyu/jmeterReports?style=flat)](https://github.com/kirillyu/jmeterReports/stargazers) - Autogenerated JMeter test-run results reported into Confluence, using Grafana custom dashboards :ru:.
  - [InfluxDB Community Template for JMeter](https://github.com/influxdata/community-templates/tree/master/apache_jmeter) [![GitHub stars](https://img.shields.io/github/stars/influxdata/community-templates/tree/master/apache_jmeter?style=flat)](https://github.com/influxdata/community-templates/tree/master/apache_jmeter/stargazers) - Prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts in a single manifest file.
  - Grafana Dashboards
    - [JMeter Load Test Dashboard](https://grafana.com/grafana/dashboards/1152-jmeter-load-test/) - Grafana dashboard shows live load test metrics provided by JMeter (by NovaTec-APM).
    - [JMeter Dashboard using Core InfluxdbBackendListenerClient](https://grafana.com/grafana/dashboards/5496-apache-jmeter-dashboard-by-ubikloadpack/) - Monitor your Apache JMeter load test in real time with InfluxDB and Grafana (by Philippe M).
    - [JMeter Dashboard (3.2 and up)](https://grafana.com/grafana/dashboards/3351-jmeter-3-3/) - Monitor JMeter load test in real time with InfluxDB and Grafana (by adrianbanu).
    - [JMeter (via prometheus exporter)](https://grafana.com/grafana/dashboards/2492-jmeter/) - A Grafana dashboard to inspect JMeter metrics via Prometheus exporter (by chiabre).
  - [JMeter-InfluxBD-Writer Plugin](https://github.com/NovatecConsulting/JMeter-InfluxDB-Writer) [![GitHub stars](https://img.shields.io/github/stars/NovatecConsulting/JMeter-InfluxDB-Writer?style=flat)](https://github.com/NovatecConsulting/JMeter-InfluxDB-Writer/stargazers) - JMeter plugin to write load test data on-the-fly into InfluxDB.
  - [JMeter Results to InfluxDB](https://github.com/soprasteria/jmeter2influxdb) [![GitHub stars](https://img.shields.io/github/stars/soprasteria/jmeter2influxdb?style=flat)](https://github.com/soprasteria/jmeter2influxdb/stargazers) - Read JMeter results from csv file and put into InfluxDB database.
- ELK Stack
  - [Using ELK](https://ecmarchitect.com/archives/2014/09/09/3932) - Using Elasticsearch, Logstash, and Kibana to visualize JMeter test results.
  - [JMeter + Elasticsearch Live Monitoring](https://medium.com/@anthony.gauthier325/jmeter-elasticsearch-live-monitoring-c895c843c51e) - Using the Elasticsearch Backend listener and Grafana/Kibana to monitor results in real time.
  - [jmeter-logstash](https://github.com/anasoid/jmeter-logstash) [![GitHub stars](https://img.shields.io/github/stars/anasoid/jmeter-logstash?style=flat)](https://github.com/anasoid/jmeter-logstash/stargazers) - Parse JTL result with Docker and Logstash in real time or after test end, and send data to Elasticsearch or InfluxDB, to have a nice dashboard and compare different tests.
- Prometheus
  - [jmeter-prometheus-plugin](https://github.com/johrstrom/jmeter-prometheus-plugin) [![GitHub stars](https://img.shields.io/github/stars/johrstrom/jmeter-prometheus-plugin?style=flat)](https://github.com/johrstrom/jmeter-prometheus-plugin/stargazers) - A Prometheus Listener for Apache JMeter that exposes results in HTTP API.
  - [jmeter-prometheus-listener](https://github.com/kolesnikovm/jmeter-prometheus-listener) [![GitHub stars](https://img.shields.io/github/stars/kolesnikovm/jmeter-prometheus-listener?style=flat)](https://github.com/kolesnikovm/jmeter-prometheus-listener/stargazers) - Apache JMeter Backend Listener implementation for Prometheus metrics exporting.
  - [ulp-observability-plugin](https://github.com/ubikingenierie/ulp-observability-plugin) [![GitHub stars](https://img.shields.io/github/stars/ubikingenierie/ulp-observability-plugin?style=flat)](https://github.com/ubikingenierie/ulp-observability-plugin/stargazers) - Allows you to monitor your JMeter CLI performance test from your favorite browser without having to start JMeter in GUI mode.
- ClickHouse
  - [JMeter Results from ClickHouse](https://grafana.com/grafana/dashboards/9561-jmeter-results-from-clickhouse-eng/) - Using the [JMeter Listener pack](https://gitlab.com/testload/jmeter-listener/-/wikis/3.3-ClickHouse-usage), ClickHouse and Grafana to collect and monitor test results.
  - [jmeter-clickhouse-listener](https://gitlab.com/testload-group/jmeter-clickhouse-listener) - JMeter plugin allows to write load test data on-the-fly to ClickHouse.
- Backend Listener Implementations
  - [jmeter-elasticsearch-backend-listener](https://github.com/anthonygauthier/jmeter-elasticsearch-backend-listener) [![GitHub stars](https://img.shields.io/github/stars/anthonygauthier/jmeter-elasticsearch-backend-listener?style=flat)](https://github.com/anthonygauthier/jmeter-elasticsearch-backend-listener/stargazers) - JMeter plugin to send test results to an Elasticsearch engine.
  - [jmeter-backend-azure](https://github.com/adrianmo/jmeter-backend-azure) [![GitHub stars](https://img.shields.io/github/stars/adrianmo/jmeter-backend-azure?style=flat)](https://github.com/adrianmo/jmeter-backend-azure/stargazers) - JMeter plugin to send test results to Azure Application Insights.
  - [jmeter-backend-listener-kafka](https://github.com/veeranalyticsltd/jmeter-backend-listener-kafka) [![GitHub stars](https://img.shields.io/github/stars/veeranalyticsltd/jmeter-backend-listener-kafka?style=flat)](https://github.com/veeranalyticsltd/jmeter-backend-listener-kafka/stargazers) - JMeter plugin to send test results to a Kafka server.
  - [jmeter-listener](https://gitlab.com/testload/jmeter-listener) - JMeter plugin to write load test data on-the-fly to ClickHouse, InfluxDB, Elasticsearch.
  - [jmeter-influxdb2-listener-plugin](https://github.com/mderevyankoaqa/jmeter-influxdb2-listener-plugin) [![GitHub stars](https://img.shields.io/github/stars/mderevyankoaqa/jmeter-influxdb2-listener-plugin?style=flat)](https://github.com/mderevyankoaqa/jmeter-influxdb2-listener-plugin/stargazers) - InfluxDB v2.0 listener plugin for Apache JMeter.
  - [jmeter-datadog-backend-listener](https://github.com/DataDog/jmeter-datadog-backend-listener) [![GitHub stars](https://img.shields.io/github/stars/DataDog/jmeter-datadog-backend-listener?style=flat)](https://github.com/DataDog/jmeter-datadog-backend-listener/stargazers) - Send JMeter test results to Datadog.
  - [jmeter-dynatrace-plugin](https://github.com/dynatrace-oss/jmeter-dynatrace-plugin) [![GitHub stars](https://img.shields.io/github/stars/dynatrace-oss/jmeter-dynatrace-plugin?style=flat)](https://github.com/dynatrace-oss/jmeter-dynatrace-plugin/stargazers) - A JMeter Backend listener implementation to send the recorded load test metrics via the Dynatrace MINT metric ingest to the configured Dynatrace monitoring environment.
  - [jmeter-backend-newrelic](https://github.com/darrensmithwtc/jmeter-backend-newrelic) [![GitHub stars](https://img.shields.io/github/stars/darrensmithwtc/jmeter-backend-newrelic?style=flat)](https://github.com/darrensmithwtc/jmeter-backend-newrelic/stargazers) - A JMeter plugin to send test results to New Relic Metrics API.
- AWS CloudWatch
  - [jmeter-cw-logs](https://github.com/concurrencylabs/jmeter-cw-logs) [![GitHub stars](https://img.shields.io/github/stars/concurrencylabs/jmeter-cw-logs?style=flat)](https://github.com/concurrencylabs/jmeter-cw-logs/stargazers) - CloudFormation template for publishing JMeter test results to AWS CloudWatch Logs.
- Custom & Deprecated
  - [Using Matplotlib & Python](https://www.metaltoad.com/blog/plotting-your-load-test-jmeter) - Plotting JMeter load test results with Matplotlib plotting tool and Python.
  - [Statistical Aggregate Report](https://rubenlaguna.com/post/2007-01-02-better-jmeter-graphs/) - Custom Statistical Aggregate Report listener for enhanced results visualization.
  - [JChav](https://github.com/d6y/jchav) [![GitHub stars](https://img.shields.io/github/stars/d6y/jchav?style=flat)](https://github.com/d6y/jchav/stargazers) - JMeter Chart History and Visualization library.
  - JMeter Dashboard: [howto](https://seangkuan.blogspot.com/2015/06/jmeter-dashboard-realtime-monitoring-of.html), [sources](https://github.com/vincentskooi/JMeterDashboard) [![GitHub stars](https://img.shields.io/github/stars/vincentskooi/JMeterDashboard?style=flat)](https://github.com/vincentskooi/JMeterDashboard/stargazers) - Real-time monitoring of JMeter load test.
  - [Using CMDRunner & Powershell](https://performancewebautoamtionother.blogspot.com/2015/12/jmeter-create-graphs-with-cmdrunner.html) - Create JMeter graphs with CMDRunner with powershell parallel execution.

## Performance Testing

### Streaming Protocols

- [Easy and realistic Load Testing of HTTP Live Streaming (HLS) with Apache JMeter](https://ubik-ingenierie.com/blog/easy-and-realistic-load-testing-of-http-live-streaming-hls-with-apache-jmeter/)
- [Using JMeter to Load Test Live HLS Concurrency of Wowza Streaming Engine](https://web.archive.org/web/20210918113142/https://www.realeyes.com/blog/wowza-streaming/)
- [How to Test Video Streaming with JMeter](https://www.blazemeter.com/blog/video-streaming-testing)
- [HLS JMeter Plugin](https://github.com/Blazemeter/HLSPlugin) [![GitHub stars](https://img.shields.io/github/stars/Blazemeter/HLSPlugin?style=flat)](https://github.com/Blazemeter/HLSPlugin/stargazers)

### Mobile Apps

- [Record iOS application HTTP requests](https://www.testautomationguru.com/jmeter-record-ios-application-http-requests/)
- [Load Testing Mobile Apps Made Easy](https://www.blazemeter.com/blog/mobile-app-load-testing)

### Mainframe Environments

- [JMeter RTE Plugin](https://github.com/Blazemeter/RTEPlugin) [![GitHub stars](https://img.shields.io/github/stars/Blazemeter/RTEPlugin?style=flat)](https://github.com/Blazemeter/RTEPlugin/stargazers) - JMeter RTE (Remote Terminal Emulator protocol) plugin for testing Mainframe applications.

### RPC Frameworks

- [JMeter gRPC Plugin](https://github.com/zalopay-oss/jmeter-grpc-plugin) [![GitHub stars](https://img.shields.io/github/stars/zalopay-oss/jmeter-grpc-plugin?style=flat)](https://github.com/zalopay-oss/jmeter-grpc-plugin/stargazers) - JMeter plugin supports load test gRPC.
- [JMeter gRPC Request](https://github.com/zalopay-oss/jmeter-grpc-request) [![GitHub stars](https://img.shields.io/github/stars/zalopay-oss/jmeter-grpc-request?style=flat)](https://github.com/zalopay-oss/jmeter-grpc-request/stargazers) - JMeter sampler to send an gRPC request to a server.
- [JMeter Dubbo Plugin](https://github.com/thubbo/jmeter-plugins-for-apache-dubbo) [![GitHub stars](https://img.shields.io/github/stars/thubbo/jmeter-plugins-for-apache-dubbo?style=flat)](https://github.com/thubbo/jmeter-plugins-for-apache-dubbo/stargazers) - JMeter plugin for Apache Dubbo.

### RESTful API

- [REST API Testing with JMeter. Step by Step Guide](https://blog.octoperf.com/rest-api-testing-with-jmeter-step-by-step-guide/)

## Tools

### Plugins

- [JMeter Plugins](https://jmeter-plugins.org/) - Independent set of plugins for Apache JMeter, with plugin manager references many plugins and simplifies installation.
- [Ubik Load Pack](https://ubikloadpack.com/) - Productivity extensions for Apache JMeter.
- GitHub Topics: [jmeter-plugin](https://github.com/topics/jmeter-plugin) [![GitHub stars](https://img.shields.io/github/stars/topics/jmeter-plugin?style=flat)](https://github.com/topics/jmeter-plugin/stargazers), [jmeter-plugins](https://github.com/topics/jmeter-plugins) [![GitHub stars](https://img.shields.io/github/stars/topics/jmeter-plugins?style=flat)](https://github.com/topics/jmeter-plugins/stargazers) - Explore JMeter plugins tagged with the `jmeter-plugin` or `jmeter-plugins` labels.

### Correlation

<!--lint ignore double-link-->
- [Correlation Recorder Plugin](https://github.com/Blazemeter/CorrelationRecorder) [![GitHub stars](https://img.shields.io/github/stars/Blazemeter/CorrelationRecorder?style=flat)](https://github.com/Blazemeter/CorrelationRecorder/stargazers) - JMeter plugin that simplifies the process of recording for applications with Dynamic Variables by providing automatic correlations of variables at recording time.
- [Siebel CRM Plugin](https://github.com/Blazemeter/SiebelPlugin) [![GitHub stars](https://img.shields.io/github/stars/Blazemeter/SiebelPlugin?style=flat)](https://github.com/Blazemeter/SiebelPlugin/stargazers) - JMeter plugin to simplify the scripting of Siebel CRM applications by providing automatic correlations of variables at recording time ❄️.
- [ULP Auto-correlator Plugin](https://ubik-ingenierie.com/blog/ubikloadpack-autocorrelator-plugin-help/) - Commercial plugin for Oracle and Vaadin-based applications from [Ubik Load Pack](#plugins).

### Extending JMeter

- [JMeter Developer Manual](https://cwiki.apache.org/confluence/display/jmeter/DeveloperManual)
- [How to write a plugin for JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)
- [How to build a JMeter plugin utilizing Groovy](https://web.archive.org/web/20180225144718/http://artur.ejsmont.org/blog/content/how-to-build-a-jmeter-plugin-utilising-groovy)
- [How to create a plugin in JMeter](https://stackoverflow.com/questions/20422640/how-to-create-a-plugin-in-jmeter)
- [Custom JMeter Samplers and Config Elements](https://codyaray.com/2014/07/custom-jmeter-samplers-and-config-elements)
- [Implement Custom JMeter Samplers](https://dzone.com/articles/implement-custom-jmeter-samplers)
- [Hello JMeter plugin](https://github.com/Bugazelle/hello-jmeter-plugin) [![GitHub stars](https://img.shields.io/github/stars/Bugazelle/hello-jmeter-plugin?style=flat)](https://github.com/Bugazelle/hello-jmeter-plugin/stargazers) - A brief, clear & fast guide to create your first JMeter plugin.

### IDE Integration

- [IntelliJ IDEA IDE Plugin](https://plugins.jetbrains.com/plugin/7013-jmeter-plugin) - Create run configurations and run JMeter tests from IntelliJ IDEA.
- [JMeter Viewer](https://github.com/anboralabs/intellij-jmeter) [![GitHub stars](https://img.shields.io/github/stars/anboralabs/intellij-jmeter?style=flat)](https://github.com/anboralabs/intellij-jmeter/stargazers) - Open JMeter test plans inside IntelliJ IDE.
- [JMeter + Eclipse HOWTO](https://cwiki.apache.org/confluence/display/jmeter/JMeterAndEclipseHowTo) - Develop the JMeter project with Eclipse IDE.
- [Using a Load Generator in NetBeans IDE](https://netbeans.apache.org/tutorial/main/kb/docs/java/profile-loadgenerator/)

### Editors

*Alternative editors for JMX files, in addition to standard JMeter GUI and XML editors.*

<!--lint ignore double-link-->
- [BlocklyJMX Editor](https://jmeter-plugins.org/editor/) - A web-based viewer and editor for JMeter test plan files (part of [JMeter Plugins](#plugins) project).
- [JEval](https://github.com/QAInsights/JEval) [![GitHub stars](https://img.shields.io/github/stars/QAInsights/JEval?style=flat)](https://github.com/QAInsights/JEval/stargazers) - A Python-based utility which evaluates JMeter test plan and provides recommendations and best practices by analyzing each element.
- [JMX Enhancer](https://www.jmxenhancer.com/) - A solution to expedite preparation of JMeter test plans.
- [jmx.js](https://www.vinodkd.org/jmx.js/) - Web-based editor for JMeter JMX files 💀.

### Utilities

- [Hamster](https://github.com/QAInsights/hamster) [![GitHub stars](https://img.shields.io/github/stars/QAInsights/hamster?style=flat)](https://github.com/QAInsights/hamster/stargazers) - Swiftly launch your JMeter test plans from Mac menubar.

### AI

- [Feather Wand](https://jmeter.ai) - An AI agent in JMeter with Claude Code, Codex, OpenCode, and Gemini integration.

## APM Integration

*Integration with Application Performance Monitoring (APM) tools to analyze the performance of application servers, database servers, and web services.*

<!--lint ignore double-link-->
- [Servers Performance Monitoring Plugin](https://jmeter-plugins.org/wiki/PerfMon/) - Server monitoring plugin from [JMeter Plugins](#plugins) project.
- [DX App Synthetic Monitor](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/app-synthetic-monitor/SaaS/using/use-jmeter-scripts-to-test-web-servers.html) - Transaction monitoring & testing solution with JMeter support.
- Performance Remediation using New Relic and JMeter: [part 1](https://web.archive.org/web/20250811141928/https://moduscreate.com/blog/performance-remediation-using-new-relic-jmeter-part-1-3/), [part 2](https://web.archive.org/web/20250809025316/https://moduscreate.com/blog/performance-remediation-using-new-relic-jmeter-part-2-3/), [part 3](https://web.archive.org/web/20250719013947/https://moduscreate.com/blog/performance-remediation-using-new-relic-jmeter-part-3-of-3/)
- [Elastic APM integration](https://github.com/vdaburon/jmeter-elastic-apm) [![GitHub stars](https://img.shields.io/github/stars/vdaburon/jmeter-elastic-apm?style=flat)](https://github.com/vdaburon/jmeter-elastic-apm/stargazers) - Manages the integration of Elastic Application Performance Monitoring API in Apache JMeter script.

## JMeter Performance

- [JMeter Performance](https://cwiki.apache.org/confluence/display/jmeter/JMeterPerformance) - Evolution of JMeter performance across versions.
- [JMeter Performance and Tuning Tips](https://ubik-ingenierie.com/blog/jmeter_performance_tuning_tips/) - By Ubik Ingenierie.
- How to speed up JMeter: [part 1](https://pflb.us/blog/how-to-speed-up-jmeter-part-1/), [part 2](https://pflb.us/blog/how-to-speed-up-jmeter-part-2/)

## Tips & Tricks

- [JMeter tips](https://web.archive.org/web/20221126233834/https://www.webwob.com/html/jmeter_tips.html) - Scratchpad for JMeter tips and tricks.

## Books

<!--lint ignore double-link-->
- [Apache JMeter: A Practical Beginner's Guide to Automated Testing and Performance Measurement for Your Websites](https://books.google.com/books?id=nX8oKIEvUcYC) - By Emily H. Halili (Packt Publishing).
- [Performance Testing with JMeter 2.9](https://books.google.com/books?id=fpWmv3wPT64C) - By Bayo Erinle ([Packt Publishing](https://www.packtpub.com/product/performance-testing-with-jmeter-29/9781782165842)); guide to test web applications using Apache JMeter with practical, hands-on examples.
- [Performance Testing with JMeter, 2nd Edition](https://books.google.com/books?id=6ditCAAAQBAJ) - By Bayo Erinle ([Packt Publishing](https://www.packtpub.com/product/performance-testing-with-jmeter/9781784394813)).
- [Performance Testing with JMeter 3, 3rd Edition](https://books.google.com/books?id=BedDDwAAQBAJ) - By Bayo Erinle ([Packt Publishing](https://www.packtpub.com/product/performance-testing-with-jmeter-3-third-edition/9781787285774)).
- [JMeter Cookbook](https://books.google.com/books?id=gJUeBQAAQBAJ) - By Bayo Erinle ([Packt Publishing](https://www.packtpub.com/product/jmeter-cookbook/9781783988280)); 70 insightful and practical recipes to help successfully use Apache JMeter.
- [JMeter by Example](https://books.google.com/books?id=iWeJDAEACAAJ) - By Sai Matam and Jagdeep Jain ([Leanpub](https://leanpub.com/jmeterbyexample)); a simple, practical, step-by-step tutorial to measure the performance of websites.
- [Pro Apache JMeter: Web Application Performance Testing](https://books.google.com/books?id=YJ4xDwAAQBAJ) - By Sai Matam and Jagdeep Jain ([Apress](https://link.springer.com/book/10.1007/978-1-4842-2961-3)).
- [Master Apache JMeter: From load testing to DevOps](https://books.google.com/books?id=D_amDwAAQBAJ) - By Antonio Gomes Rodrigues, Bruno Demion (Milamber) and Philippe Mouawad ([Leanpub](https://leanpub.com/master-jmeter-from-load-test-to-devops), [Packt Publishing](https://www.packtpub.com/product/master-apache-jmeter-from-load-testing-to-devops/9781839217647)).
- [Advanced JMeter Testing](https://leanpub.com/advanced_jmeter_testing) - By Penny Curich ([Leanpub](https://leanpub.com/advanced_jmeter_testing)), guide to write custom components for Apache JMeter 5.0.

## Trainings & Courses

- [JMeter: Performance and Load Testing (Feb 2019)](https://www.linkedin.com/learning/jmeter-performance-and-load-testing) - By LinkedIn Learning.
- [Advanced JMeter (Jul 2020)](https://www.linkedin.com/learning/advanced-jmeter) - By LinkedIn Learning.
- [JMeter Training Courses](https://www.nobleprog.co.uk/cc/apachejmetertesting) - By NobleProg.
- [BlazeMeter University](https://www.blazemeter.com/university) - By BlazeMeter.
- [JMeter Courses collection](https://www.udemy.com/topic/jmeter/) - By Udemy.
- [Web Applications (and Mobile Apps) Performance Testing with JMeter](http://pragmatictestlabs.com/web-applications-mobile-apps-performance-testing-jmeter/) - By Pragmatic Test Labs.
- [Training courses on Load Testing with Apache JMeter](https://ubik-ingenierie.com/blog/jmeter-trainings-by-contributors-and-committers/) - By Ubik Ingenierie.
- [Apache JMeter Training](https://qainsights.com/apache-jmeter-training/) - By QAInsights.
- [JMeter Getting Started Course (Apr 2019)](https://www.pluralsight.com/courses/jmeter-getting-started) - By Pluralsight.

## Videos

- [JMeter Tutorials](https://www.youtube.com/c/AutomationStepByStep/search?query=jmeter) - By Automation Step by Step.
- [Learn Apache JMeter Series](https://www.youtube.com/playlist?list=PLJ9A48W0kpRIjLkZ32Do9yDZXnnm7_uj_) - By QAInsights.
- [JMeter / Devops/ CI-CD / Cloud](https://www.youtube.com/c/xavki-linux/search?query=jmeter) - By xavki :fr:.

## Community

### Blogs

- [BlazeMeter Blog](https://www.blazemeter.com/blog) - BlazeMeter's blog about JMeter and performance testing.
- [Ubik Load Pack Blog](https://ubik-ingenierie.com/blog/category/jmeter/) - Ubik Ingenierie blog.
- [TestAutomationGuru Blog](https://www.testautomationguru.com/category/jmeter/) - Technical blog on test automation.
- [RedLine13 Blog](https://www.redline13.com/blog/tag/jmeter/) - JMeter articles in RedLine13 blog.
- [JMeter Blog](https://shantonusarker.blogspot.com/p/jmeter.html) - Another blog for performance & automation testing using JMeter.
- [OctoPerf Blog](https://blog.octoperf.com/categories/jmeter/) - OctoPerf's blog about JMeter and load testing.
- [Abstracta JMeter Archives](https://abstracta.us/blog/tag/jmeter/) - Abstracta blog about JMeter.
- [JMeter Basics](https://thatsabug.com/tags/#jmeter-series) - By João Farias.

### Forums

<!--lint ignore double-link-->
- [JMeterPlugins Google Group](https://groups.google.com/g/jmeter-plugins)

### Twitter

<!--lint ignore double-link-->
- [@ApacheJMeter](https://x.com/apachejmeter) - Official Twitter account of the Apache JMeter load testing tool.
- [@jmeter_plugins](https://x.com/jmeter_plugins) - Twitter account of custom plugins project for JMeter load testing tool.
- [@BlazeMeter](https://x.com/BlazeMeter) - Official Twitter account of Blazemeter, performance engineering platform for DevOps, based on JMeter.
- [@masterjmeter](https://x.com/masterjmeter) - Official account of the [Master Apache JMeter from Load Testing to DevOps](#books) book.
- [@ubikloadpack](https://x.com/ubikloadpack) - Twitter account of [Ubik Load Pack](#plugins), custom JMeter plugins for Video Streaming & complex protocols load testing.

### Q&A

- [`jmeter` on Stack Overflow](https://stackoverflow.com/questions/tagged/jmeter)
- [`jmeter` on Gitter](https://app.gitter.im/#/room/#aliesbelik_jmeter-chat:gitter.im)
- [`#jmeter` on Slack](https://jmeterusers.slack.com/)
- [`r/jmeter` on Reddit](https://www.reddit.com/r/jmeter/)

## Related

### Awesome Lists

- [Awesome Software Quality](https://github.com/ligurio/sqa-wiki) [![GitHub stars](https://img.shields.io/github/stars/ligurio/sqa-wiki?style=flat)](https://github.com/ligurio/sqa-wiki/stargazers) - A list of free software testing and verification resources.
- [Awesome Testing](https://github.com/TheJambo/awesome-testing) [![GitHub stars](https://img.shields.io/github/stars/TheJambo/awesome-testing?style=flat)](https://github.com/TheJambo/awesome-testing/stargazers) - A curated list of testing resources.
- [Awesome Tsung](https://github.com/aliesbelik/awesome-tsung) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-tsung?style=flat)](https://github.com/aliesbelik/awesome-tsung/stargazers) - Open-source multi-protocol distributed load testing tool, developed in Erlang.
- [Awesome Gatling](https://github.com/aliesbelik/awesome-gatling) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-gatling?style=flat)](https://github.com/aliesbelik/awesome-gatling/stargazers) - Open-source load and performance testing framework based on Scala, Akka and Netty.
- [Awesome k6](https://github.com/grafana/awesome-k6) [![GitHub stars](https://img.shields.io/github/stars/grafana/awesome-k6?style=flat)](https://github.com/grafana/awesome-k6/stargazers) - Open-source, developer-centric performance monitoring and load testing solution.
- [Awesome Locust](https://github.com/aliesbelik/awesome-locust) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-locust?style=flat)](https://github.com/aliesbelik/awesome-locust/stargazers) - Open-source scalable load testing framework written in Python.

### Other

- [How They Load Test](https://github.com/aliesbelik/how-they-load) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/how-they-load?style=flat)](https://github.com/aliesbelik/how-they-load/stargazers) - A curated collection of publicly available resources on how companies around the world perform load testing.
- [Load Testing Toolkit](https://github.com/aliesbelik/load-testing-toolkit) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/load-testing-toolkit?style=flat)](https://github.com/aliesbelik/load-testing-toolkit/stargazers) - Collection of open-source tools for debugging, benchmarking, load and stress testing your code or services.

## Contributing

Please take a look at the [CONTRIBUTING](CONTRIBUTING.md) guidelines first.
