# Gatling

[![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-gatling?style=flat)](https://github.com/aliesbelik/awesome-gatling/stargazers)

# Awesome Gatling [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint ignore double-link match-punctuation -->
[<img src="assets/images/gatling-logo.svg" align="right" width="260" alt="Gatling">](https://gatling.io/)
<!--lint ignore double-link-->
A curated collection of resources covering all aspects of load testing using [Gatling](https://gatling.io/) and related stuff: plugins, integrations, testing techniques, DevOps practices, etc.
<!--lint ignore double-link-->
> [Gatling](https://gatling.io/) is an open-source load and performance testing framework based on Scala, Akka and Netty.

## Contents

- [Official Resources](#official-resources)
- [Getting Started](#getting-started)
- [Tutorials](#tutorials)
- [Distributed Testing](#distributed-testing)
- [Tools](#tools)
  - [Plugins](#plugins)
  - [Frameworks](#frameworks)
  - [Reporting](#reporting)
  - [Sandbox](#sandbox)
  - [Miscellaneous](#miscellaneous)
- [CI](#ci)
- [Test Management](#test-management)
- [Trainings & Courses](#trainings--courses)
- [Videos](#videos)
  - [Talks](#talks)
  - [Video Tutorials](#video-tutorials)
- [Community](#community)
- [Related](#related)
  - [Awesome Lists](#awesome-lists)
  - [Other](#other)

## Official Resources
<!--lint ignore double-link-->
- [Homepage](https://gatling.io/)
- [Documentation](https://docs.gatling.io/)
- [Source code](https://github.com/gatling/gatling) [![GitHub stars](https://img.shields.io/github/stars/gatling/gatling?style=flat)](https://github.com/gatling/gatling/stargazers)

## Getting Started

- [A first look at Gatling, a DSL based load test tool](https://callistaenterprise.se/blogg/teknik/2014/04/16/a-first-look-at-gatling-a-dsl-based-load-test-tool/)
- [Gatling: Take your performance tests to the next level](https://www.thoughtworks.com/insights/blog/gatling-take-your-performance-tests-next-level)
- [Load Testing with Gatling. The Complete Guide](https://www.james-willett.com/gatling-load-testing-complete-guide/)

## Tutorials

- [Load testing gRPC services with Gatling](https://medium.com/@georgeleung_7777/load-testing-grpc-services-with-gatling-990025c77055)
- [Creating a custom Gatling protocol for AWS Lambda](https://callistaenterprise.se/blogg/teknik/2016/11/26/gatling-custom-protocol/)
- [Load testing ZeroMQ with a custom DSL for Gatling](https://mintbeans.com/load-testing-zeromq-with-gatling/)

## Distributed Testing

- [Distributed load testing with Gatling and Kubernetes](https://debijenkorf.tech/https-medium-com-annashepeleva-distributed-load-testing-with-gatling-and-kubernetes-93ebce26edbe)
- [Gatling – Scaling Out Your Load Tests](https://web.archive.org/web/20210625094528/http://www.nimrodstech.com/gatling-cluster-load-testing/)
- [Distributed Gatling](https://github.com/Abiy/distGatling) [![GitHub stars](https://img.shields.io/github/stars/Abiy/distGatling?style=flat)](https://github.com/Abiy/distGatling/stargazers) - Solution to run Gatling simulation tests in a distributed/cluster environment.
- [gatling-operator](https://github.com/st-tech/gatling-operator) [![GitHub stars](https://img.shields.io/github/stars/st-tech/gatling-operator?style=flat)](https://github.com/st-tech/gatling-operator/stargazers) - Automating distributed Gatling load testing using Kubernetes operator.

## Tools

### Plugins

- [gatling-sbt-plugin](https://github.com/gatling/gatling-sbt-plugin) [![GitHub stars](https://img.shields.io/github/stars/gatling/gatling-sbt-plugin?style=flat)](https://github.com/gatling/gatling-sbt-plugin/stargazers) - Gatling SBT plugin to integrate Gatling with SBT, allowing to use Gatling as a testing framework.
- [gatling-build-plugin](https://github.com/gatling/gatling-build-plugin) [![GitHub stars](https://img.shields.io/github/stars/gatling/gatling-build-plugin?style=flat)](https://github.com/gatling/gatling-build-plugin/stargazers) - An SBT plugin to share common settings across Gatling's projects' builds.
- [gatling-maven-plugin](https://github.com/gatling/gatling-maven-plugin) [![GitHub stars](https://img.shields.io/github/stars/gatling/gatling-maven-plugin?style=flat)](https://github.com/gatling/gatling-maven-plugin/stargazers) - Gatling Maven Extensions.
- [gatling-gradle-plugin](https://github.com/gatling/gatling-gradle-plugin) [![GitHub stars](https://img.shields.io/github/stars/gatling/gatling-gradle-plugin?style=flat)](https://github.com/gatling/gatling-gradle-plugin/stargazers) - Gatling plugin for Gradle.
- [gatling-remote-sbt](https://github.com/Pravoru/gatling-remote-sbt) [![GitHub stars](https://img.shields.io/github/stars/Pravoru/gatling-remote-sbt?style=flat)](https://github.com/Pravoru/gatling-remote-sbt/stargazers) - Remote execution plugin for Gatling load tests.
- [gatling-junitrunner](https://github.com/Pravoru/gatling-junitrunner) [![GitHub stars](https://img.shields.io/github/stars/Pravoru/gatling-junitrunner?style=flat)](https://github.com/Pravoru/gatling-junitrunner/stargazers) - JUnit wrapper around Gatling simulations.
- [gatling-grpc](https://github.com/phiSgr/gatling-grpc) [![GitHub stars](https://img.shields.io/github/stars/phiSgr/gatling-grpc?style=flat)](https://github.com/phiSgr/gatling-grpc/stargazers) - Gatling load test plugin for gRPC.
- [gatling-aws](https://github.com/callistaenterprise/gatling-aws) [![GitHub stars](https://img.shields.io/github/stars/callistaenterprise/gatling-aws?style=flat)](https://github.com/callistaenterprise/gatling-aws/stargazers) - Gatling custom protocol for AWS Lambda.
- [gatling-xmpp-protocol](https://github.com/TLmaK0/gatling-xmpp-protocol) [![GitHub stars](https://img.shields.io/github/stars/TLmaK0/gatling-xmpp-protocol?style=flat)](https://github.com/TLmaK0/gatling-xmpp-protocol/stargazers) - XMPP protocol for stress test XMPP servers with Gatling.
- [gatling-jwt](https://bitbucket.org/atlassianlabs/gatling-jwt/) - An extension to Gatling 2.0 to help make JWT-signed requests.
- [gatling-mqtt](https://github.com/mnogu/gatling-mqtt) [![GitHub stars](https://img.shields.io/github/stars/mnogu/gatling-mqtt?style=flat)](https://github.com/mnogu/gatling-mqtt/stargazers) - A Gatling plugin for stress testing MQTT.
- [gatling-kafka](https://github.com/mnogu/gatling-kafka) [![GitHub stars](https://img.shields.io/github/stars/mnogu/gatling-kafka?style=flat)](https://github.com/mnogu/gatling-kafka/stargazers) - A Gatling plugin for stress testing Apache Kafka protocol.
- [gatling-kafka](https://github.com/Amerousful/gatling-kafka) [![GitHub stars](https://img.shields.io/github/stars/Amerousful/gatling-kafka?style=flat)](https://github.com/Amerousful/gatling-kafka/stargazers) - Gatling plugin for Kafka.
- [gatling-kafka-plugin](https://github.com/galax-io/gatling-kafka-plugin) [![GitHub stars](https://img.shields.io/github/stars/galax-io/gatling-kafka-plugin?style=flat)](https://github.com/galax-io/gatling-kafka-plugin/stargazers) - Plugin for support Kafka in Gatling.
- [gatling-amqp-plugin](https://github.com/galax-io/gatling-amqp-plugin) [![GitHub stars](https://img.shields.io/github/stars/galax-io/gatling-amqp-plugin?style=flat)](https://github.com/galax-io/gatling-amqp-plugin/stargazers) - Plugin for support performance testing with AMQP in Gatling (3.2.x).
- [gatling-jdbc-plugin](https://github.com/galax-io/gatling-jdbc-plugin) [![GitHub stars](https://img.shields.io/github/stars/galax-io/gatling-jdbc-plugin?style=flat)](https://github.com/galax-io/gatling-jdbc-plugin/stargazers) - Simple Gatling plugin for JDBC support.
- [gatling-picatinny](https://github.com/galax-io/gatling-picatinny) [![GitHub stars](https://img.shields.io/github/stars/galax-io/gatling-picatinny?style=flat)](https://github.com/galax-io/gatling-picatinny/stargazers) - Library with a bunch of useful functions that extend Gatling DSL.
- [gatling-sql](https://github.com/tmcgrath/gatling-sql) [![GitHub stars](https://img.shields.io/github/stars/tmcgrath/gatling-sql?style=flat)](https://github.com/tmcgrath/gatling-sql/stargazers) - Gatling extension for JDBC or Spark Thrift Server stress testing.
- [gatling-tcp-extensions](https://github.com/scalecube/gatling-tcp-extensions) [![GitHub stars](https://img.shields.io/github/stars/scalecube/gatling-tcp-extensions?style=flat)](https://github.com/scalecube/gatling-tcp-extensions/stargazers) - TCP extensions for Gatling.
- [gatling-thrift](https://github.com/3tty0n/gatling-thrift) [![GitHub stars](https://img.shields.io/github/stars/3tty0n/gatling-thrift?style=flat)](https://github.com/3tty0n/gatling-thrift/stargazers) - Gatling third party plugin for Apache Thrift.
- [gatling-bolt](https://github.com/sarmbruster/gatling-bolt) [![GitHub stars](https://img.shields.io/github/stars/sarmbruster/gatling-bolt?style=flat)](https://github.com/sarmbruster/gatling-bolt/stargazers) - Support Neo4j Bolt protocol for Gatling.
- [gatling-zeromq](https://github.com/softwaremill/gatling-zeromq) [![GitHub stars](https://img.shields.io/github/stars/softwaremill/gatling-zeromq?style=flat)](https://github.com/softwaremill/gatling-zeromq/stargazers) - A Gatling stress test plugin for ZeroMQ protocol.
- [gatling-dubbo](https://github.com/youzan/gatling-dubbo) [![GitHub stars](https://img.shields.io/github/stars/youzan/gatling-dubbo?style=flat)](https://github.com/youzan/gatling-dubbo/stargazers) - A Gatling plugin for running load tests on Apache Dubbo.
- [gatling-wait](https://github.com/Amerousful/gatling-wait) [![GitHub stars](https://img.shields.io/github/stars/Amerousful/gatling-wait?style=flat)](https://github.com/Amerousful/gatling-wait/stargazers) - Plugin that simplifies waiting for specific events allowing customizable conditions, attempt management, and error handling.

### Frameworks

- [Kraken](https://github.com/OctoPerf/kraken) [![GitHub stars](https://img.shields.io/github/stars/OctoPerf/kraken?style=flat)](https://github.com/OctoPerf/kraken/stargazers) - Load testing IDE based on Gatling by OctoPerf.
- [Karate Gatling](https://docs.karatelabs.io/extensions/performance-testing/) - Re-use Karate API-tests as performance tests executed by Gatling.
- [Taurus](https://gettaurus.org/docs/Gatling/) - Gatling Executor in Taurus framework.
- [Carrier](https://github.com/carrier-io) [![GitHub stars](https://img.shields.io/github/stars/carrier-io?style=flat)](https://github.com/carrier-io/stargazers) - Continuous test execution platform with ability to perform load testing using customized JMeter and Gatling containers.
- [Gatlytron](https://github.com/Performetriks/Gatlytron) [![GitHub stars](https://img.shields.io/github/stars/Performetriks/Gatlytron?style=flat)](https://github.com/Performetriks/Gatlytron/stargazers) - Gatling Base Framework for easy onboarding.

### Reporting

- [gatling-report](https://github.com/nuxeo/gatling-report) [![GitHub stars](https://img.shields.io/github/stars/nuxeo/gatling-report?style=flat)](https://github.com/nuxeo/gatling-report/stargazers) - Parse Gatling simulation.log files to output CSV stats or build HTML reports with Plotly charts.
- [gatling2allure](https://github.com/biski/gatling2allure) [![GitHub stars](https://img.shields.io/github/stars/biski/gatling2allure?style=flat)](https://github.com/biski/gatling2allure/stargazers) - Convert Gatling log to Allure report.
- [gatling-elasticsearch](https://github.com/Amerousful/gatling-elasticsearch-logs) [![GitHub stars](https://img.shields.io/github/stars/Amerousful/gatling-elasticsearch-logs?style=flat)](https://github.com/Amerousful/gatling-elasticsearch-logs/stargazers) - Logger which parses raw Gatling logs and sends them to the Elasticsearch.

### Sandbox

- [gatling-scaffold](https://github.com/robsonbittencourt/gatling-scaffold) [![GitHub stars](https://img.shields.io/github/stars/robsonbittencourt/gatling-scaffold?style=flat)](https://github.com/robsonbittencourt/gatling-scaffold/stargazers) - Base for load test project using Gatling, InfluxDB and Grafana.
- [perfiz](https://github.com/znsio/perfiz) [![GitHub stars](https://img.shields.io/github/stars/znsio/perfiz?style=flat)](https://github.com/znsio/perfiz/stargazers) - A dockerised API performance test setup based on Gatling with Grafana dashboards and Prometheus monitoring.

### Miscellaneous

- [dakiya](https://github.com/rupeshmore/dakiya) [![GitHub stars](https://img.shields.io/github/stars/rupeshmore/dakiya?style=flat)](https://github.com/rupeshmore/dakiya/stargazers) - Convert Postman collections to Gatling scripts.
- [gatling-template.g8](https://github.com/galax-io/gatling-template.g8) [![GitHub stars](https://img.shields.io/github/stars/galax-io/gatling-template.g8?style=flat)](https://github.com/galax-io/gatling-template.g8/stargazers) - A Giter8 template for Gatling performance test project.

## CI

- [Gatling Jenkins Plugin](https://github.com/jenkinsci/gatling-plugin) [![GitHub stars](https://img.shields.io/github/stars/jenkinsci/gatling-plugin?style=flat)](https://github.com/jenkinsci/gatling-plugin/stargazers) - [Jenkins plugin](https://plugins.jenkins.io/gatling/) for Gatling.
- [run-gatling](https://github.com/liatrio/run-gatling) [![GitHub stars](https://img.shields.io/github/stars/liatrio/run-gatling?style=flat)](https://github.com/liatrio/run-gatling/stargazers) - GitHub Action to easily integrate Gatling performance tests to GitHub workflows.

## Test Management

- [Performance and load testing with Gatling](https://docs.getxray.app/space/XRAYCLOUD/44565472/Performance+and+load+testing+with+Gatling) - Integrating with Xray Test Management on Jira and Gatling.

## Trainings & Courses

- [Gatling Courses](https://www.udemy.com/topic/gatling/) - By Udemy.
- [Performance Test Automation 101: Gatling, Lighthouse, & Jenkins](https://www.educative.io/courses/performance-test-automation-101-gatling-lighthouse-jenkins) - By Educative.

## Videos

### Talks

- [Load Testing Done Right with Gatling](https://www.youtube.com/watch?v=VUPTaPms210) - Stéphane Landelle @ Voxxed Days Belgrade 2015.
- [Load Testing Crash Course with Gatling](https://www.youtube.com/watch?v=RiM1GsVSbzM) - Stéphane Landelle @ Devoxx Belgium 2022.
- [Load Testing Made Easy with Gatling](https://www.youtube.com/watch?v=8Eplj8BvugA) - Rafał Piotrowski @ Scala Days 2023 Madrid.

### Video Tutorials

- [Performance Testing with Gatling](https://www.youtube.com/playlist?list=PLd4gvNaNZ4T3NCWsv3zwHYlLGtr9s1-Fz) - Tutorial series by Tomi Tiihonen.
- [Gatling Tutorials for Beginners](https://www.youtube.com/playlist?list=PLw_jGKXm9lIYpTotIJ-R31pXS7qqwXstt) - Tutorial series by James Willett.

## Community

- [Gatling Community](https://community.gatling.io/)
- [`gatling` on Stack Overflow](https://stackoverflow.com/questions/tagged/gatling+or+scala-gatling+or+gatling-java+or+gatling-plugin)
- [`@GatlingTool` on Twitter](https://x.com/gatlingtool)

## Related

### Awesome Lists

- [Awesome Software Quality](https://github.com/ligurio/sqa-wiki) [![GitHub stars](https://img.shields.io/github/stars/ligurio/sqa-wiki?style=flat)](https://github.com/ligurio/sqa-wiki/stargazers) - A list of free software testing and verification resources.
- [Awesome Testing](https://github.com/TheJambo/awesome-testing) [![GitHub stars](https://img.shields.io/github/stars/TheJambo/awesome-testing?style=flat)](https://github.com/TheJambo/awesome-testing/stargazers) - A curated list of testing resources.
- [Awesome JMeter](https://github.com/aliesbelik/awesome-jmeter) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-jmeter?style=flat)](https://github.com/aliesbelik/awesome-jmeter/stargazers) - Open-source load testing and performance measurement tool, written in Java.
- [Awesome Tsung](https://github.com/aliesbelik/awesome-tsung) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-tsung?style=flat)](https://github.com/aliesbelik/awesome-tsung/stargazers) - Open-source multi-protocol distributed load testing tool, developed in Erlang.
- [Awesome k6](https://github.com/grafana/awesome-k6) [![GitHub stars](https://img.shields.io/github/stars/grafana/awesome-k6?style=flat)](https://github.com/grafana/awesome-k6/stargazers) - Open-source, developer-centric performance monitoring and load testing solution.
- [Awesome Locust](https://github.com/aliesbelik/awesome-locust) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/awesome-locust?style=flat)](https://github.com/aliesbelik/awesome-locust/stargazers) - Open-source scalable load testing framework written in Python.

### Other

- [How They Load Test](https://github.com/aliesbelik/how-they-load) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/how-they-load?style=flat)](https://github.com/aliesbelik/how-they-load/stargazers) - A curated collection of publicly available resources on how companies around the world perform load testing.
- [Load Testing Toolkit](https://github.com/aliesbelik/load-testing-toolkit) [![GitHub stars](https://img.shields.io/github/stars/aliesbelik/load-testing-toolkit?style=flat)](https://github.com/aliesbelik/load-testing-toolkit/stargazers) - Collection of open-source tools for debugging, benchmarking, load and stress testing your code or services.

## Contributing

Contributions are welcome!<br>
Please take a look at the [CONTRIBUTING](CONTRIBUTING.md) guidelines first.
