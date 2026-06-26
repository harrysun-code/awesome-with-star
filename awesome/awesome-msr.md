# Empirical Software Engineering

[![GitHub stars](https://img.shields.io/github/stars/dspinellis/awesome-msr?style=flat)](https://github.com/dspinellis/awesome-msr/stargazers)

# Awesome Empirical Software Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
A curated repository of data sets and tools that can be used for conducting evidence-based, data-driven research on software systems.
This research approach is often termed [experimental, or empirical software engineering](https://en.wikipedia.org/wiki/Experimental_software_engineering).
Many of the data sets can also be useful in research using [search-based software engineering](https://en.wikipedia.org/wiki/Search-based_software_engineering) methods.
The repository is named after the [Mining Software Repositories (MSR)](https://www.msrconf.org/) conference series.
For examples of such work see the MSR conference's [Hall of Fame](http://2016.msrconf.org/#/hall-of-fame).


- This list requires your input for its continuous improvement.
  Read the [contribution guide](contributing.md) for instructions on how
  you can contribute.
  Alternatively, you can send me an [email](mailto:dds@aueb.gr)
  if you find the process too cumbersome or confusing.
- For more awesome lists, see [awesome](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/sindresorhus/awesome?style=flat)](https://github.com/sindresorhus/awesome/stargazers).

## Contents
- [Repositories](#repositories)
- [Data Sets](#data-sets)
- [Tools](#tools)
- [Research Outlets](#research-outlets)

## Repositories

- [ESEUR](https://github.com/Derek-Jones/ESEUR-code-data) [![GitHub stars](https://img.shields.io/github/stars/Derek-Jones/ESEUR-code-data?style=flat)](https://github.com/Derek-Jones/ESEUR-code-data/stargazers) All data used in the openly available book [Evidence-based Software Engineering](http://www.knosof.co.uk/ESEUR/index.html)
- [Directory of MSR Datasets](https://authecesofteng.github.io/directory-msr-datasets/)
- [FLOSSmole](https://flossmole.org/collection_details) - Collaborative collection and analysis of free/libre/open source project data.
- [PROMISE](http://promise.site.uottawa.ca/SERepository/datasets-page.html) - About 20 datasets related to software engineering research.
- [SIR](http://sir.unl.edu/portal/index.php) - Software-artifact infrastructure repository; Java, C, C++, and C# software together with test suites and fault data.
- [Zenodo](http://zenodo.org/) - Software data collections in CERN's open-access repository.
  - [Software Engineering Artifacts Can Really Assist Future Tasks](http://zenodo.org/communities/seacraft)
  - [Empirical Software Engineering](https://zenodo.org/communities/empirical-software-engineering/)
  - [Mining Software Repositories](https://zenodo.org/communities/msr/)

## Data Sets

- [AndroidTimeMachine](https://androidtimemachine.github.io) - Graph-based dataset of commit history of 8,431 real-world Android apps.
- [AndroZoo](https://androzoo.uni.lu/) - Collection of Android Applications.
- [Bug Prediction Dataset](http://bug.inf.usi.ch/index.php) - Collection of models and metrics from Eclipse JDT Core, PDE UI, Equinox Framework, Lucene, Mylyn, and their histories.
- [Code Reviews](http://kin-y.github.io/miningReviewRepo/) - Code reviews of OpenStack, LibreOffice, AOSP, Qt, Eclipse.
- [CoREBench](http://www.comp.nus.edu.sg/%7Erelease/corebench/) - Collection of 70 realistically Complex Regression Errors that were systematically extracted from the repositories and bug reports of four open-source software projects: Make, Grep, Findutils, and Coreutils.
- [Cryptocurrency GitHub Activity and Market Cap Dataset](https://rvantonder.github.io/CryptOSS/) - Activity such as commits, stars, prices, and market cap of over 200 cryptocurrency projects on GitHub over time. Raw, historic data is also [available](https://zenodo.org/record/2595588#.XRuzuBNKhSM).
- [Defects4J](https://github.com/rjust/defects4j) [![GitHub stars](https://img.shields.io/github/stars/rjust/defects4j?style=flat)](https://github.com/rjust/defects4j/stargazers) - Collection of 395 reproducible bugs collected with the goal of advancing software testing research.
- [Eclipse AERI stacktraces](http://download.eclipse.org/scava/datasets/aeri_stacktraces/aeri_stacktraces.html) - Collection of stacktraces of Exceptions encountered by users of the Eclipse IDE, as retrieved by the AERI reporting system.
- [Enron Spreadsheets and Emails](https://figshare.com/articles/Enron_Spreadsheets_and_Emails/1221767) - All the spreadsheets and emails used in the paper 'Enron's Spreadsheets and Related Emails: A Dataset and Analysis'.
- [Findbugs-maven](https://github.com/istlab/maven_bug_catalog) [![GitHub stars](https://img.shields.io/github/stars/istlab/maven_bug_catalog?style=flat)](https://github.com/istlab/maven_bug_catalog/stargazers) - Set of FindBugs reports for the Java projects of the [Maven repository](https://maven.apache.org).
- [GHTorrent](http://ghtorrent.org/) - Scalable, queriable, offline mirror of data offered through the GitHub REST API.
- [GitHub Bug Dataset](http://www.inf.u-szeged.hu/~ferenc/papers/GitHubBugDataSet/) - Bug Dataset of 15 Java open-source projects characterized by static source code metrics.
- [GitHub on Google BigQuery](https://cloud.google.com/bigquery/public-data/github) - GitHub data accessible through Google's BigQuery platform.
- [Grammar Zoo](http://slebok.github.io/zoo/) - Collection of grammars of DSLs and GPLs, some extracted from metamodels and document schemata.
- [KaVE](http://www.kave.cc/datasets) - Developer tool interaction data.
- [Linux Kernel 4.21 Call Graphs](https://zenodo.org/record/2652487#.XRnvomUzb0o) - The Linux Kernel 4.21 Call Graphs produced using [CScout](https://github.com/dspinellis/cscout/) [![GitHub stars](https://img.shields.io/github/stars/dspinellis/cscout/?style=flat)](https://github.com/dspinellis/cscout//stargazers). 
- [Maven metrics](https://github.com/bkarak/data_msr2015) [![GitHub stars](https://img.shields.io/github/stars/bkarak/data_msr2015?style=flat)](https://github.com/bkarak/data_msr2015/stargazers) - Collection of software complexity & sizing metrics for the [Maven Repository](https://maven.apache.org).
- [Maven Dependency Graph](https://zenodo.org/record/1489120) - Snapshot of the whole Maven Central taken on September 6, 2018, stored in a graph database.
- [mzdata](https://github.com/jxshin/mzdata) [![GitHub stars](https://img.shields.io/github/stars/jxshin/mzdata?style=flat)](https://github.com/jxshin/mzdata/stargazers) - Multi-extract and multi-level dataset of Mozilla issue tracking history.
- [npm-miner](https://github.com/AuthEceSoftEng/msr-2018-npm-miner) [![GitHub stars](https://img.shields.io/github/stars/AuthEceSoftEng/msr-2018-npm-miner?style=flat)](https://github.com/AuthEceSoftEng/msr-2018-npm-miner/stargazers) - The dataset contains the analysis results of 5 open source software quality tools eslint, escomplex, nsp, jsinspect and sonarjs for 2000 popular (in terms of stars and downloads) npm packages.
- [OCL Expressions on GitHub](https://github.com/tue-mdse/ocl-dataset) [![GitHub stars](https://img.shields.io/github/stars/tue-mdse/ocl-dataset?style=flat)](https://github.com/tue-mdse/ocl-dataset/stargazers) - Data set of 9188 OCL expressions originating from 504 EMF meta-models in 245 systematically selected GitHub repositories.
- [RepoReapers Data Set](https://reporeapers.github.io) - Data set containing a collection of _engineered software projects_ from GHTorrent.
- [Software Heritage Graph Dataset](https://doi.org/10.5281/zenodo.2583978) - Graph of the development history and file metadata of >80 million software projects from various forges (GitHub, Gitlab, Debian, PyPI, Google Code, etc) in a deduplicated and unified representation ([paper here](https://dl.acm.org/citation.cfm?id=3341907)).
- [STAMINA](http://stamina.chefbe.net/download) - (STAte Machine INference Approaches) data are used to benchmark techniques for learning deterministic finite state machines (FSMs).
- [Stack Exchange](https://archive.org/details/stackexchange) - Anonymized dump of all user-contributed content on the Stack Exchange network.
- [SWE-bench](https://www.swebench.com) - SWE-bench is a benchmark designed to evaluate the ability of AI models to solve real-world software engineering problems by generating fixes for issues found in open-source code repositories.
- [TravisTorrent](http://travistorrent.testroots.org) - Provides free and easy-to-use Traivs CI build analyses.
- [Ultimate Debian Database (UDD)](https://wiki.debian.org/UltimateDebianDatabase) - Data about various aspects of Debian (e.g. packages, bugs, mainteners) in the same SQL database.
- [Unified Bug Dataset](http://www.inf.u-szeged.hu/~ferenc/papers/UnifiedBugDataSet/) - Static source code based datasets which includes the Bugcatchers Bug Dataset, the [Bug Prediction Dataset](http://bug.inf.usi.ch/index.php), the [Eclipse Bug Dataset](https://www.st.cs.uni-saarland.de/softevo/bug-data/eclipse/), the [GitHub Bug Dataset](http://www.inf.u-szeged.hu/~ferenc/papers/GitHubBugDataSet/), some datasets from the [PROMISE](http://promise.site.uottawa.ca/SERepository/datasets-page.html) repository.
- [Unix history](https://github.com/dspinellis/unix-history-repo) [![GitHub stars](https://img.shields.io/github/stars/dspinellis/unix-history-repo?style=flat)](https://github.com/dspinellis/unix-history-repo/stargazers) - Git repository with 46 years of Unix history evolution.

## Tools
- [astminer](https://github.com/JetBrains-Research/astminer) [![GitHub stars](https://img.shields.io/github/stars/JetBrains-Research/astminer?style=flat)](https://github.com/JetBrains-Research/astminer/stargazers) - Library and tool for mining of path-based representations of code and other data derived from ASTs.
- [Boa](http://boa.cs.iastate.edu/) - Domain-specific language and infrastructure that eases mining software repositories.
- [buckwheat](https://github.com/JetBrains-Research/buckwheat) [![GitHub stars](https://img.shields.io/github/stars/JetBrains-Research/buckwheat?style=flat)](https://github.com/JetBrains-Research/buckwheat/stargazers) - Multi-language tokenizer for extracting identifiers from source code.
- [ckjm](http://www.spinellis.gr/sw/ckjm/) - Chidamber and Kemerer Java Metrics.
- [Coming](https://github.com/SpoonLabs/coming/) [![GitHub stars](https://img.shields.io/github/stars/SpoonLabs/coming/?style=flat)](https://github.com/SpoonLabs/coming//stargazers) - A Java framework for analyzing code changes and mining instances of change patterns from Git repositories.
- [CryptOSS](https://github.com/rvantonder/CryptOSS) [![GitHub stars](https://img.shields.io/github/stars/rvantonder/CryptOSS?style=flat)](https://github.com/rvantonder/CryptOSS/stargazers) - Mine GitHub activity and market cap data for cryptocurrency projects.
- [DbDeo](https://github.com/tushartushar/DbDeo) [![GitHub stars](https://img.shields.io/github/stars/tushartushar/DbDeo?style=flat)](https://github.com/tushartushar/DbDeo/stargazers) - Extract embedded SQL statements and detect database schema smells.
- [Designite](http://www.designite-tools.com) - Compute source code metrics and detect a variety of implementation, design, and architecture smells for C#.
- [DesigniteJava](https://github.com/tushartushar/DesigniteJava) [![GitHub stars](https://img.shields.io/github/stars/tushartushar/DesigniteJava?style=flat)](https://github.com/tushartushar/DesigniteJava/stargazers) - Compute source code metrics and detect a variety of implementation and design smells for Java.
- [Diggit](https://github.com/jrfaller/diggit) [![GitHub stars](https://img.shields.io/github/stars/jrfaller/diggit?style=flat)](https://github.com/jrfaller/diggit/stargazers) - Agile Ruby Tool to analyze Git repositories.
- [GitEvo](https://github.com/andrehora/gitevo) [![GitHub stars](https://img.shields.io/github/stars/andrehora/gitevo?style=flat)](https://github.com/andrehora/gitevo/stargazers) - Code evolution analysis for Git repositories.
- [GrimoireLab](http://grimoirelab.github.io/) - Free/Libre/Open Source tools for Software Development Analytics.
- [MetricMiner](http://www.github.com/mauricioaniche/metricminer2) - Lean Java DSL to mine and extract data (e.g. commits, developers, modifications, diffs) from Git and SVN repositories.
- [Maven-miner](https://github.com/diverse-project/maven-miner) [![GitHub stars](https://img.shields.io/github/stars/diverse-project/maven-miner?style=flat)](https://github.com/diverse-project/maven-miner/stargazers) - Java tools and infrastructure to resolve the whole Maven dependency graph, hosted in Maven Central, in the form of a [Neo4j](https://neo4j.com/) Graph.
- [Perceval](https://github.com/chaoss/grimoirelab-perceval) [![GitHub stars](https://img.shields.io/github/stars/chaoss/grimoirelab-perceval?style=flat)](https://github.com/chaoss/grimoirelab-perceval/stargazers) - Fetch repository data from tens of back-ends.
- [Puppeteer](https://github.com/tushartushar/Puppeteer) [![GitHub stars](https://img.shields.io/github/stars/tushartushar/Puppeteer?style=flat)](https://github.com/tushartushar/Puppeteer/stargazers) - Detect configuration smells in Puppet code.
- [PyDriller](https://github.com/ishepard/pydriller) [![GitHub stars](https://img.shields.io/github/stars/ishepard/pydriller?style=flat)](https://github.com/ishepard/pydriller/stargazers) - Python Framework to analyse Git repositories.
- [qmcalc](https://github.com/dspinellis/cqmetrics) [![GitHub stars](https://img.shields.io/github/stars/dspinellis/cqmetrics?style=flat)](https://github.com/dspinellis/cqmetrics/stargazers) - Calculate quality metrics from C source code.
- [reaper](https://github.com/RepoReapers/reaper) [![GitHub stars](https://img.shields.io/github/stars/RepoReapers/reaper?style=flat)](https://github.com/RepoReapers/reaper/stargazers) - Python tool to compute a score for a repository from GHTorrent. The score quantifies the extent to which the project contained within the repository is _engineered_.
- [RefactoringMiner](https://github.com/tsantalis/RefactoringMiner) [![GitHub stars](https://img.shields.io/github/stars/tsantalis/RefactoringMiner?style=flat)](https://github.com/tsantalis/RefactoringMiner/stargazers) - Library/API for detection of refactorings in changes of Java code.
- [TestMiner](https://andrehora.github.io/testminer) - Software testing analysis for GitHub repositories.
- [VulData7](https://github.com/electricalwind/data7) [![GitHub stars](https://img.shields.io/github/stars/electricalwind/data7?style=flat)](https://github.com/electricalwind/data7/stargazers) - Java framework enabling the automated collection of commits fixing vulnerabilities that are reported in NVD (links NVD with Git).

## Research Outlets
- Outlets exclusively devoted to empirical software engineering research
  - [Empirical Software Engineering journal](https://link.springer.com/journal/10664)
  - [MSR: Mining Software Repositories conference](https://www.msrconf.org/)
  - [PROMISE: Predictive Models and Data Analytics in Software Engineering conference](http://promise.site.uottawa.ca/SERepository/)
- Outlets that publish empirical software engineering research
  - [ACM Transactions on Software Engineering and Methodology (TOSEM)](https://dl.acm.org/citation.cfm?id=J790)
  - [ESEC/FSE: ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering](https://www.esec-fse.org/)
  - [ICSE: International Conference on Software Engineering](http://www.icse-conferences.org/)
  - [IEEE Software magazine](https://publications.computer.org/software-magazine/)
  - [IEEE Transactions on Software Engineering](https://www.computer.org/csdl/journal/ts)
  - [Journal of Systems and Software](https://www.journals.elsevier.com/journal-of-systems-and-software)
  - [SANER: IEEE International Conference on Software Analysis, Evolution and Reengineering](https://ieeexplore.ieee.org/xpl/conhome.jsp?punumber=1000695)


## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Diomidis Spinellis](http://www.spinellis.gr) has waived all copyright and related or neighboring rights to this work.
