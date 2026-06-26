# Computational Biology

[![GitHub stars](https://img.shields.io/github/stars/inoue0426/awesome-computational-biology?style=flat)](https://github.com/inoue0426/awesome-computational-biology/stargazers)

# Awesome Computational Biology [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated collection of databases, software, and papers related to computational biology.

> Computational biology involves the development and application of data-analytical and theoretical methods, mathematical modelling and computational simulation techniques to the study of biological, ecological, behavioural, and social systems. — [Wikipedia](https://en.wikipedia.org/wiki/Computational_biology)

---

## Overview

[![Resource Landscape Overview](docs/overview.png)](https://inoue0426.github.io/awesome-computational-biology/overview.html)

> Interactive version: [Resource Overview page](https://inoue0426.github.io/awesome-computational-biology/overview.html)  
> Regenerate the figure: `python scripts/generate_overview.py`

---

## GitHub Pages UI

Browse and search the resources via the [GitHub Pages UI](https://inoue0426.github.io/awesome-computational-biology/).

- Search matches `name`, `description`, `tasks`, `modalities`, and `tags`.
- The **Task**, **Modality**, and **Type** filters map directly to `tasks`, `modalities`, and `type` in `docs/data/resources.json`.
- Clicking badges on cards applies the corresponding filter.

---

## Table of Contents

- [Awesome Computational Biology](#awesome-computational-biology-)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [GitHub Pages UI](#github-pages-ui)
  - [Citation](#citation)
  - [Curation Criteria (Strict)](#curation-criteria-strict)
  - [Update & Link Rot Policy](#update--link-rot-policy)
  - [Data Schema & Contribution Workflow](#data-schema--contribution-workflow)
  - [Databases](#databases)
    - [scRNA](#scrna)
    - [Compound](#compound)
    - [Pathway](#pathway)
    - [Mass Spectra](#mass-spectra)
    - [Protein](#protein)
    - [Genome](#genome)
    - [Disease](#disease)
    - [Interaction](#interaction)
      - [Drug-Gene Interaction](#drug-gene-interaction)
      - [Drug (Cell Line) Response](#drug-cell-line-response)
      - [Chemical-Protein Interaction](#chemical-protein-interaction)
      - [Protein-Protein Interaction](#protein-protein-interaction)
      - [Knowledge Graph](#knowledge-graph)
      - [Gene Regulatory Network](#gene-regulatory-network)
    - [Clinical Trial](#clinical-trial)
  - [Benchmarks & Datasets](#benchmarks--datasets)
  - [API](#api)
  - [Preprocessing Tools](#preprocessing-tools)
  - [Machine Learning Tasks and Models](#machine-learning-tasks-and-models)
    - [Drug Discovery](#drug-discovery)
      - [Drug Response Prediction](#drug-response-prediction)
      - [Drug Repurposing](#drug-repurposing)
      - [Drug Target Interaction](#drug-target-interaction)
      - [Compound-Protein Interaction](#compound-protein-interaction)
      - [Molecular Generation](#molecular-generation)
    - [LLM for Biology](#llm-for-biology)
    - [Foundation Models](#foundation-models)
      - [Single-cell Foundation Models](#single-cell-foundation-models)
        - [Transcriptomics Foundation Models](#transcriptomics-foundation-models)
        - [Spatial Foundation Models](#spatial-foundation-models)
        - [Multi-Omics Foundation Models](#multi-omics-foundation-models)
        - [Domain Alignment](#domain-alignment)
      - [Compound Foundation Models](#compound-foundation-models)
        - [Compound Embedding](#compound-embedding)
      - [Protein Foundation Models](#protein-foundation-models)
        - [Pre-trained Embedding](#pre-trained-embedding)
        - [Protein Structure Prediction and Design](#protein-structure-prediction-and-design)
      - [Multi-Modal Foundation Models](#multi-modal-foundation-models)
      - [Genomics Foundation Models](#genomics-foundation-models)

---

## Databases

### scRNA

- [CZ CELLxGENE](https://cellxgene.cziscience.com/) — Single-cell dataset repository and interactive explorer from the Chan Zuckerberg Initiative.
- [Gene Expression Omnibus](https://www.ncbi.nlm.nih.gov/geo/) — Public functional genomics database.
- [Human Cell Atlas](https://www.humancellatlas.org/) — Open global atlas of all cells in the human body.
- [Single Cell PORTAL](https://singlecell.broadinstitute.org/single_cell) — Public database for single-cell RNA.
- [Single Cell Expression Atlas](https://www.ebi.ac.uk/gxa/sc/home) — Public database for single-cell RNA.

### Compound

- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) — One of the largest chemical databases (compounds, genes, and proteins).
- [ChEBI](https://www.ebi.ac.uk/chebi/) — Database focused on small chemical compounds.
- [ChEMBL](https://www.ebi.ac.uk/chembl/) — Bioactive molecules with drug-like properties.
- [ChemSpider](http://www.chemspider.com/) — Chemical structure database.
- [DrugTargetCommons](https://drugtargetcommons.fimm.fi/) — Community platform for curating and integrating experimental bioactivity data across drugs and targets.
- [HMDB (Human Metabolome Database)](https://hmdb.ca/) — Comprehensive database of small molecule metabolites found in the human body.
- [KEGG COMPOUND](https://www.genome.jp/kegg/compound/) — Collection of small molecules and biopolymers.
- [LIPID MAPS](https://www.lipidmaps.org/databases/lmsd/overview) — Database of lipids.
- [Rhea](https://www.rhea-db.org/) — Database of chemical reactions.
- [DrugCentral](http://drugcentral.org/) — Online drug compendium with drug mode of action and indication information.
- [Drug Repurposing Hub](https://repo-hub.broadinstitute.org/repurposing#download-data) — Collections of drug repurposing data (drug, MoA, target, etc).
- [Therapeutic Target Database](https://idrblab.net/ttd/full-data-download) — Drug-target, target-disease, and drug-disease datasets.
- [ZINC ligand discovery database](https://zinc.docking.org/) — Free database of commercially-available compounds for virtual screening.

### Pathway

- [PathwayCommons](https://www.pathwaycommons.org/) — Database of pathways and interactions.
- [KEGG PATHWAY](https://www.genome.jp/kegg/pathway.html) — Collection of pathway maps.
- [WikiPathways](https://wikipathways.org/) — Database of biological pathways.
- [Reactome](https://reactome.org/) — Expert-curated, peer-reviewed pathway database with detailed reaction mechanisms.
- [BioCyc](https://biocyc.org/) — Collection of pathway/genome databases across thousands of organisms.
- [OmniPath](https://omnipathdb.org/) — Comprehensive resource integrating protein interactions, signaling pathways, gene regulatory networks, and miRNA targets from over 100 databases.
- [SIGNOR 2.0](https://signor.uniroma2.it/) — Database of causal signaling interactions and pathways, with signed and directed relationships between proteins.
- [MSigDB (Molecular Signatures Database)](https://www.gsea-msigdb.org/gsea/msigdb) — Curated gene sets derived from pathways and biological processes.

### Mass Spectra

- [MassBank](http://www.massbank.jp/) — Open source databases and tools for mass spectrometry reference spectra.
- [MoNA MassBank of North America](https://mona.fiehnlab.ucdavis.edu/) — Meta-database of metabolite mass spectra, metadata, and associated compounds.

### Protein

- [THE HUMAN PROTEIN ATLAS](https://www.proteinatlas.org/) — Comprehensive human protein database (cells, tissues, organs).
- [PROTEIN DATA BANK (PDB)](https://www.rcsb.org/) — 3D structures of proteins, nucleic acids, complexes.
- [UniProt](https://www.uniprot.org/) — Functional information on proteins.
- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/api-docs) — 3D protein structure predictions.
- [RCSB Protein Data Bank](https://www.rcsb.org/) — Repository for structural data of biological molecules.
- [Critical Assessment of Structure Prediction (CASP)](https://predictioncenter.org/) — Assessing methods for protein structure prediction.
- [Uniclust](https://uniclust.mmseqs.com/) — Clustered protein sequence databases.
- [UniRef](https://www.uniprot.org/uniref/) — Non-redundant sequence database clustering UniProtKB entries at multiple sequence identity thresholds.
- [CATH database](https://www.cathdb.info/) — Hierarchical classification of protein domain structures.
- [SAbDab](https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/sabdab) — Structural Antibody Database containing all antibody structures in the PDB.
- [OADB (Observed Antibody Space Database)](http://opig.stats.ox.ac.uk/webapps/oas/) — Database of antibody sequences from immune repertoire sequencing.
- [InterPro](https://www.ebi.ac.uk/interpro/) — Protein families, domains, and functional sites database integrating 14 member databases including Pfam and PROSITE.
- [Pfam](https://www.ebi.ac.uk/interpro/entry/pfam/) — Database of protein families described by multiple sequence alignments and hidden Markov models.
- [NeXtProt](https://www.nextprot.org/) — Expert knowledge base on human proteins with deep functional annotation, complementary to UniProt.

### Genome

- [ENCODE](https://www.encodeproject.org/) — Encyclopedia of DNA Elements; regulatory and functional genomic elements across the genome.
- [Ensembl](https://www.ensembl.org/) — Genome browser and annotation database for vertebrate and other eukaryotic genomes.
- [Human Genome Resources at NCBI](https://www.ncbi.nlm.nih.gov/projects/genome/guide/human/index.shtml) — Database for genomics, proteomics, transcriptomics, and systems biology.
- [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) — NCBI's database of genetic sequences.
- [UCSC Genome Browser](https://genome.ucsc.edu/) — UCSC's genome browser.
- [cBioPortal](https://www.cbioportal.org/) — Cancer genomics database; aggregating many patient datasets.
- [10x Genomics Dataset](https://www.10xgenomics.com/resources/datasets) — Collection of single-cell datasets.
- [The Genotype-Tissue Expression (GTEx)](https://gtexportal.org/home/) — Human gene expression and regulation resource.
- [Dependency Map (DepMap)](https://depmap.org/portal/) — CRISPR-Cas9 screens in cancer cell lines.
- [Catalogue Of Somatic Mutations In Cancer (COSMIC)](https://cancer.sanger.ac.uk/cosmic) — Resource on somatic mutations in cancers.
- [MGnify](https://www.ebi.ac.uk/metagenomics/) — Resource for metagenomic and metatranscriptomic data.
- [JASPAR](http://jaspar.genereg.net/) — Database of transcription factor binding profiles.
- [gnomAD](https://gnomad.broadinstitute.org/) — Genome Aggregation Database; genetic variation from large-scale sequencing projects.
- [Rfam](https://rfam.org/) — Database of RNA families with sequence alignments and consensus structures.
- [ROADMAP Epigenomics](http://www.roadmapepigenomics.org/) — Reference epigenome maps for 111 primary human cell types and tissues, including histone modifications, chromatin accessibility, and DNA methylation.
- [FANTOM5](https://fantom.gsc.riken.jp/5/) — Functional annotation of mammalian genome; comprehensive atlas of active enhancers, promoters, and transcription start sites across human and mouse cell types.

### Disease

- [KEGG DRUG](https://www.genome.jp/kegg/drug/) — Comprehensive, approved drug information.
- [DrugBank](https://go.drugbank.com/) — Database of drugs and targets (University of Alberta).
- [DisGeNET](https://www.disgenet.org/) — Database of gene-disease associations integrating expert-curated and GWAS data.
- [OMIM (Online Mendelian Inheritance in Man)](https://www.omim.org/) — Comprehensive database of human genes and genetic disorders.
- [Open Targets Platform](https://platform.opentargets.org/) — Systematic target identification and prioritization platform integrating genetics, genomics, and drug data for drug discovery.
- [Human Phenotype Ontology (HPO)](https://hpo.jax.org/) — Standardized vocabulary of phenotypic abnormalities in human disease, linking genes, variants, and clinical features.
- [DISEASES](https://diseases.jensenlab.org/) — Gene–disease association database integrating evidence from text mining, curated databases, and experimental data.

### Interaction

#### Drug-Gene Interaction

- [DGIdb](https://www.dgidb.org/) — Drug-gene interactions and the druggable genome.
- [Comparative Toxicogenomics Database](http://ctdbase.org/) — Chemical-gene interactions, chemical-disease and gene-disease associations, chemical-phenotype associations.
- [SNAP](https://snap.stanford.edu/biodata/datasets/10002/10002-ChG-Miner.html) — Dataset of drug-gene interactions.

#### Drug (Cell Line) Response

- [NCI60](https://dtp.cancer.gov/discovery_development/nci-60/) — Focuses on 60 cancer cell lines and many drugs.
- [Genomics of Drug Sensitivity in Cancer (GDSC)](https://www.cancerrxgene.org/) — Drug sensitivity for ~1000 human cancer cell lines and hundreds of compounds.
- [Cancer Cell Line Encyclopedia](https://sites.broadinstitute.org/ccle/) — Database of ~1000 cancer cell lines.
- [CellMiner Cross Database (CellMinerCDB)](https://discover.nci.nih.gov/cellminercdb/) — Integrates multiple cancer cell line databases.

#### Chemical-Protein Interaction

- [STITCH](http://stitch.embl.de/) — Chemical-protein interactions.
- [BindingDB](https://www.bindingdb.org/rwd/bind/index.jsp) — Compounds and target database.
- [Davis kinase inhibitors DB](http://staff.cs.utu.fi/~aijrinas/dti/) — Experimental kinase inhibitor binding affinity dataset for protein–ligand interaction research.
- [Kinase Inhibitor Bioactivity Data (KIBA)](https://janeliascicomp.github.io/KIBA/) — Integrated bioactivity scores for kinase inhibitors combining Ki, Kd, and IC50 measurements.
- [PDBBind](https://www.pdbbind-plus.org.cn/) — Binding affinity data for biomolecular complexes.

#### Protein-Protein Interaction

- [STRING](https://string-db.org/) — PPI networks for multiple organisms.
- [BioGRID](https://thebiogrid.org/) — Protein, genetic, and chemical interactions.
- [HIPPIE](http://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/) — Human protein-protein interaction database.
- [IntAct](https://www.ebi.ac.uk/intact/home) — Open-source molecular interaction database and analysis system from EMBL-EBI.

#### Knowledge Graph

- [Drug Mechanism Database (DrugMechDB)](https://github.com/SuLab/DrugMechDB/tree/2.0.1) [![GitHub stars](https://img.shields.io/github/stars/SuLab/DrugMechDB/tree/2.0.1?style=flat)](https://github.com/SuLab/DrugMechDB/tree/2.0.1/stargazers) — Mechanisms of action from drug to disease.
- [DRKG](https://github.com/gnn4dr/DRKG) [![GitHub stars](https://img.shields.io/github/stars/gnn4dr/DRKG?style=flat)](https://github.com/gnn4dr/DRKG/stargazers) — Large-scale biological knowledge graph for drug discovery.
- [Hetionet](https://github.com/hetio/hetionet) [![GitHub stars](https://img.shields.io/github/stars/hetio/hetionet?style=flat)](https://github.com/hetio/hetionet/stargazers) — Heterogeneous network integrating genes, diseases, drugs, pathways, and more.
- [PrimeKG](https://github.com/mims-harvard/PrimeKG) [![GitHub stars](https://img.shields.io/github/stars/mims-harvard/PrimeKG?style=flat)](https://github.com/mims-harvard/PrimeKG/stargazers) — Multi-modal precision medicine knowledge graph integrating clinical, genetic, and drug data.

#### Gene Regulatory Network

- [TRRUST v2](https://www.grnpedia.org/trrust/) — Manually curated database of human and mouse transcriptional regulatory interactions between transcription factors and their target genes, expanded with literature-derived evidence.
- [RegNetwork](http://www.regnetworkweb.org/) — Database of gene regulatory networks covering transcription factor–target gene and miRNA–gene interaction data across multiple species.
- [miRBase](https://www.mirbase.org/) — Reference repository for microRNA gene annotations, sequences, and experimentally validated targets.

### Clinical Trial

- [ClinicalTrials.gov](https://clinicaltrials.gov/) — Privately and publicly funded clinical studies.
- [ICD10](https://icd.who.int/browse10/2019/en) — International Classification of Diseases, 10th revision.
- [EU Drug Regulating Authorities Clinical Trials DB (EudraCT)](https://eudract.ema.europa.eu/) — European clinical trial database.
- [MIMIC-IV](https://mimic.mit.edu/) — Freely accessible critical care database.

---

## Benchmarks & Datasets

- [1000 Genomes Project](https://www.internationalgenome.org/) — Reference panel of human genetic variation from 2,504 individuals across 26 populations.
- [BACE](https://www.kaggle.com/datasets/gokturkkoch/bace) — Binary classification and regression dataset for β-secretase 1 (BACE-1) inhibitor binding affinity.
- [BEAT AML](https://biodev.github.io/BeatAML2/) — Functional ex vivo drug sensitivity measurements paired with genomics for acute myeloid leukemia.
- [Bento](https://github.com/LigandPro/Bento) [![GitHub stars](https://img.shields.io/github/stars/LigandPro/Bento?style=flat)](https://github.com/LigandPro/Bento/stargazers) — Protein-ligand docking benchmark covering rigid, flexible, de novo, blind, induced-fit, and covalent docking tasks.
- [BindingDB Curated Sets](https://www.bindingdb.org/rwd/bind/chemsearch/marvin/SDFdownload.jsp?all_download=yes) — Curated binding affinity datasets for protein–ligand interaction benchmarking.
- [Cancer Therapeutics Response Portal (CTRP)](https://portals.broadinstitute.org/ctrp/) — Drug sensitivity profiles across ~900 cancer cell lines for >400 compounds.
- [ClinTox](https://tdcommons.ai/single_pred_tasks/tox/#clintox) — Clinical toxicity dataset contrasting FDA-approved drugs with those that failed clinical trials due to toxicity.
- [CPTAC (Clinical Proteomic Tumor Analysis Consortium)](https://proteomics.cancer.gov/programs/cptac) — Multi-omic proteogenomic datasets for multiple cancer types linking proteomics with genomics.
- [CrossDocked2020](https://arxiv.org/abs/2001.01037) — Large-scale dataset for structure-based virtual screening.
- [DUD-E (Directory of Useful Decoys, Enhanced)](http://dude.docking.org/) — Structure-based virtual screening benchmark with active ligands and challenging decoy sets across diverse protein targets.
- [FLIP (Fitness Landscape Inference for Proteins)](https://github.com/J-SNACKKB/FLIP) [![GitHub stars](https://img.shields.io/github/stars/J-SNACKKB/FLIP?style=flat)](https://github.com/J-SNACKKB/FLIP/stargazers) — Benchmark collection of protein fitness landscape datasets for evaluating protein ML models.
- [Genomics of Drug Sensitivity in Cancer (GDSC)](https://www.cancerrxgene.org/) — Drug sensitivity for ~1000 human cancer cell lines and hundreds of compounds.
- [GuacaMol](https://github.com/BenevolentAI/guacamol) [![GitHub stars](https://img.shields.io/github/stars/BenevolentAI/guacamol?style=flat)](https://github.com/BenevolentAI/guacamol/stargazers) — Benchmark suite for generative molecular design models.
- [JUMP Cell Painting Datasets](https://github.com/jump-cellpainting/datasets) [![GitHub stars](https://img.shields.io/github/stars/jump-cellpainting/datasets?style=flat)](https://github.com/jump-cellpainting/datasets/stargazers) — Consortium-scale cell imaging perturbation datasets (chemical and genetic) for phenotypic profiling and drug discovery research.
- [LINCS L1000](https://lincsproject.org/LINCS/tools/workflows/find-the-best-place-to-obtain-the-lincs-l1000-data) — Gene expression profiles (978 landmark genes) for >20,000 chemical and genetic perturbations across cell lines.
- [MoleculeNet](http://moleculenet.ai/) — Benchmark datasets for molecular machine learning.
- [MOSES](https://github.com/molecularsets/moses) [![GitHub stars](https://img.shields.io/github/stars/molecularsets/moses?style=flat)](https://github.com/molecularsets/moses/stargazers) — Benchmarking platform for molecular generation models.
- [NCI60](https://dtp.cancer.gov/discovery_development/nci-60/) — Drug sensitivity benchmark across 60 diverse human cancer cell lines.
- [OGB (Open Graph Benchmark)](https://ogb.stanford.edu/) — Large-scale graph ML benchmark suite including biological datasets such as ogbl-ppa (protein-protein associations) and ogbg-molhiv.
- [OpenBioLink](https://github.com/OpenBioLink/OpenBioLink) [![GitHub stars](https://img.shields.io/github/stars/OpenBioLink/OpenBioLink?style=flat)](https://github.com/OpenBioLink/OpenBioLink/stargazers) — Benchmark datasets for biological knowledge graph completion.
- [PharmGKB](https://www.pharmgkb.org/) — Curated pharmacogenomics dataset linking genetic variants to drug response phenotypes across thousands of drugs.
- [PK-DB](https://pk-db.com/) — Open database of experimental pharmacokinetics (PK) and ADME data from clinical and preclinical studies.
- [PRISM](https://depmap.org/portal/prism/) — Cancer drug sensitivity profiling of >4,500 drugs across >900 cancer cell lines using pooled-cell-line barcoding.
- [ProteinGym](https://github.com/OATML-Markslab/ProteinGym) [![GitHub stars](https://img.shields.io/github/stars/OATML-Markslab/ProteinGym?style=flat)](https://github.com/OATML-Markslab/ProteinGym/stargazers) — Large-scale benchmark of deep mutational scanning assays for evaluating protein fitness landscape models.
- [QM9](https://figshare.com/collections/Quantum_chemistry_structures_and_properties_of_134_kilo_molecules/978904) — Quantum chemistry properties for 134K stable small organic molecules computed at DFT level.
- [scIB (Single-cell Integration Benchmarks)](https://github.com/theislab/scib) [![GitHub stars](https://img.shields.io/github/stars/theislab/scib?style=flat)](https://github.com/theislab/scib/stargazers) — Comprehensive benchmarking framework for single-cell data integration methods.
- [scPerturb](https://github.com/sanderlab/scPerturb) [![GitHub stars](https://img.shields.io/github/stars/sanderlab/scPerturb?style=flat)](https://github.com/sanderlab/scPerturb/stargazers) — Curated and continuously updated single-cell perturbation data resource spanning CRISPR and drug perturbation studies.
- [SIDER (Side Effect Resource)](http://sideeffects.embl.de/) — Database of 1,430 approved drugs with their recorded adverse drug reactions across 27 system-organ classes.
- [Tabula Muris](https://tabula-muris.ds.czbiohub.org/) — Comprehensive single-cell atlas of 20 mouse organs and tissues, enabling cross-tissue and cross-species comparisons.
- [Tabula Sapiens](https://tabula-sapiens-portal.ds.czbiohub.org/) — Comprehensive human single-cell atlas of ~500K cells from 24 organs and tissues across multiple donors.
- [TAPE (Tasks Assessing Protein Embeddings)](https://github.com/songlab-cal/tape) [![GitHub stars](https://img.shields.io/github/stars/songlab-cal/tape?style=flat)](https://github.com/songlab-cal/tape/stargazers) — Benchmark suite of five biologically meaningful semi-supervised learning tasks for evaluating protein representations.
- [The Cancer Genome Atlas (TCGA)](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga) — Comprehensive multi-omics (genomics, transcriptomics, proteomics, methylation) dataset for 33 cancer types across ~11,000 patients.
- [Therapeutics Data Commons (TDC)](https://tdcommons.ai/) — Unified benchmark suite covering ADMET, drug-target interaction, drug response, and more.
- [Tox21](https://tripod.nih.gov/tox21/challenge/) — 12,707 compounds tested in 12 nuclear receptor and stress-response pathway biochemical assays for toxicity prediction.
- [UK Biobank](https://www.ukbiobank.ac.uk/) — Large-scale biomedical database of ~500K participants with genetic, imaging, and health data for population genetics and disease studies.

---

## API

- [PubMed E-utilities (esearch/efetch)](https://www.nlm.nih.gov/dataguide/edirect/esearch.html) — APIs for searching and retrieving biomedical literature from PubMed.
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) — Unified APIs for accessing NCBI databases (Gene, GEO, SRA, PubChem, etc).
- [UniProt REST API](https://www.uniprot.org/help/api) — Programmatic access to protein sequence and functional annotation data.
- [Ensembl REST API](https://rest.ensembl.org/) — API for genomic annotations, variants, genes, and comparative genomics.
- [KEGG REST API](https://www.kegg.jp/kegg/rest/keggapi.html) — API for accessing KEGG pathways, compounds, genes, and reactions.
- [ChEMBL Web Services](https://www.ebi.ac.uk/chembl/ws) — REST API for bioactive molecules, targets, and bioassays.
- [Open Targets Platform API](https://platform.opentargets.org/api) — API for target–disease associations integrating genetics, genomics, and drug data.
- [ClinicalTrials.gov API](https://clinicaltrials.gov/api/gui) — API for querying clinical trial metadata and results.

---

## Preprocessing Tools

- [Chemistry Development Kit](https://github.com/cdk/cdk) [![GitHub stars](https://img.shields.io/github/stars/cdk/cdk?style=flat)](https://github.com/cdk/cdk/stargazers) — Cheminformatics software & machine learning tools.
- [Biopython](https://biopython.org/) — Collection of Python tools for biological computation including sequence analysis, structure parsing, and database access.
- [FlashDeconv](https://github.com/cafferychen777/flashdeconv) [![GitHub stars](https://img.shields.io/github/stars/cafferychen777/flashdeconv?style=flat)](https://github.com/cafferychen777/flashdeconv/stargazers) — High-performance spatial transcriptomics deconvolution (~1M spots in ~3 min).
- [RDKit](https://github.com/rdkit/rdkit) [![GitHub stars](https://img.shields.io/github/stars/rdkit/rdkit?style=flat)](https://github.com/rdkit/rdkit/stargazers) — Cheminformatics software & machine learning toolkit.
- [DeepChem](https://github.com/deepchem/deepchem) [![GitHub stars](https://img.shields.io/github/stars/deepchem/deepchem?style=flat)](https://github.com/deepchem/deepchem/stargazers) — Deep learning library for drug discovery, quantum chemistry, and materials science.
- [ChatSpatial](https://github.com/cafferychen777/ChatSpatial) [![GitHub stars](https://img.shields.io/github/stars/cafferychen777/ChatSpatial?style=flat)](https://github.com/cafferychen777/ChatSpatial/stargazers) — MCP server for spatial transcriptomics analysis via natural language.
- [Scanpy](https://scanpy.readthedocs.io/en/stable/) — Python library for scRNA-seq analysis.
- [Seurat](https://satijalab.org/seurat/) — R library for scRNA-seq analysis.
- [scvi-tools](https://scvi-tools.org/) — Probabilistic models for single-cell omics data analysis.
- [CellTypist](https://github.com/Teichlab/celltypist) [![GitHub stars](https://img.shields.io/github/stars/Teichlab/celltypist?style=flat)](https://github.com/Teichlab/celltypist/stargazers) — Automated cell type annotation for scRNA-seq.
- [Squidpy](https://squidpy.readthedocs.io/) — Python library for spatial single-cell analysis.
- [GROMACS](https://www.gromacs.org/) — Molecular dynamics simulation package for biochemical molecules.
- [MDAnalysis](https://www.mdanalysis.org/) — Python library for analyzing and altering molecular dynamics simulation trajectories.
- [OpenMM](https://openmm.org/) — High-performance toolkit for molecular simulation and GPU-accelerated MD.
- [scVelo](https://github.com/theislab/scvelo) [![GitHub stars](https://img.shields.io/github/stars/theislab/scvelo?style=flat)](https://github.com/theislab/scvelo/stargazers) — RNA velocity estimation for single-cell transcriptomics, inferring the direction and speed of cell differentiation.
- [STAR](https://github.com/alexdobin/STAR) [![GitHub stars](https://img.shields.io/github/stars/alexdobin/STAR?style=flat)](https://github.com/alexdobin/STAR/stargazers) — Ultrafast universal RNA-seq aligner with support for spliced alignment and single-cell quantification via STARsolo.
- [kallisto](https://pachterlab.github.io/kallisto/) — Near-optimal RNA-seq quantification using pseudoalignment for fast transcript abundance estimation.
- [Harmony](https://github.com/immunogenomics/harmony) [![GitHub stars](https://img.shields.io/github/stars/immunogenomics/harmony?style=flat)](https://github.com/immunogenomics/harmony/stargazers) — Fast and scalable integration of single-cell data across datasets, conditions, technologies, and species.
- [Monocle3](https://cole-trapnell-lab.github.io/monocle3/) — Single-cell trajectory analysis tool for learning developmental trajectories and ordering cells in pseudotime.
- [CellChat](https://github.com/sqjin/CellChat) [![GitHub stars](https://img.shields.io/github/stars/sqjin/CellChat?style=flat)](https://github.com/sqjin/CellChat/stargazers) — Inference and analysis of cell-cell communication ligand-receptor networks from single-cell transcriptomics data.
- [SCENIC](https://github.com/aertslab/SCENIC) [![GitHub stars](https://img.shields.io/github/stars/aertslab/SCENIC?style=flat)](https://github.com/aertslab/SCENIC/stargazers) — Single-cell regulatory network inference and clustering linking transcription factors to co-expressed gene modules.
- [DoubletFinder](https://github.com/chris-mcginnis-ucsf/DoubletFinder) [![GitHub stars](https://img.shields.io/github/stars/chris-mcginnis-ucsf/DoubletFinder?style=flat)](https://github.com/chris-mcginnis-ucsf/DoubletFinder/stargazers) — Machine learning approach for detecting multiplet (doublet) artifacts in single-cell RNA-seq data.
- [Numbat](https://github.com/kharchenkolab/numbat) [![GitHub stars](https://img.shields.io/github/stars/kharchenkolab/numbat?style=flat)](https://github.com/kharchenkolab/numbat/stargazers) — Haplotype-aware copy number variation inference from single-cell RNA-seq using hidden Markov models.
- [CaSpER](https://github.com/akdess/CaSpER) [![GitHub stars](https://img.shields.io/github/stars/akdess/CaSpER?style=flat)](https://github.com/akdess/CaSpER/stargazers) — CNV identification and visualization by integrative analysis of single-cell or bulk RNA-seq data.
- [CellCharter](https://github.com/CSOgroup/cellcharter) [![GitHub stars](https://img.shields.io/github/stars/CSOgroup/cellcharter?style=flat)](https://github.com/CSOgroup/cellcharter/stargazers) — Identification and characterization of spatial cell niches from spatial transcriptomics using VAEs and Gaussian mixture models.
- [STAGATE](https://github.com/RucDongLab/STAGATE) [![GitHub stars](https://img.shields.io/github/stars/RucDongLab/STAGATE?style=flat)](https://github.com/RucDongLab/STAGATE/stargazers) — Adaptive graph attention auto-encoder for spatial domain identification in spatial transcriptomics.
- [NCEM](https://github.com/theislab/ncem) [![GitHub stars](https://img.shields.io/github/stars/theislab/ncem?style=flat)](https://github.com/theislab/ncem/stargazers) — GNN-based model for learning intercellular communication from spatial graphs of cells.
- [DeepTalk](https://github.com/JiangBioLab/DeepTalk) [![GitHub stars](https://img.shields.io/github/stars/JiangBioLab/DeepTalk?style=flat)](https://github.com/JiangBioLab/DeepTalk/stargazers) — Graph attention network for deciphering cell-cell communication from spatial transcriptomics data.
- [COMMOT](https://github.com/zcang/COMMOT) [![GitHub stars](https://img.shields.io/github/stars/zcang/COMMOT?style=flat)](https://github.com/zcang/COMMOT/stargazers) — Optimal transport-based framework for screening cell-cell communication in spatial transcriptomics.
- [TIGON](https://github.com/yutongo/TIGON) [![GitHub stars](https://img.shields.io/github/stars/yutongo/TIGON?style=flat)](https://github.com/yutongo/TIGON/stargazers) — Neural optimal transport method for reconstructing growth and dynamic trajectories from single-cell transcriptomics.
- [LINGER](https://github.com/Durenlab/LINGER) [![GitHub stars](https://img.shields.io/github/stars/Durenlab/LINGER?style=flat)](https://github.com/Durenlab/LINGER/stargazers) — Neural network for gene regulatory network inference from single-cell multiome (RNA+ATAC-seq) data with bulk data pretraining.
- [sciPENN](https://github.com/jlakkis/sciPENN) [![GitHub stars](https://img.shields.io/github/stars/jlakkis/sciPENN?style=flat)](https://github.com/jlakkis/sciPENN/stargazers) — RNN-based method for simultaneous protein expression prediction, uncertainty estimation, and cell-type label transfer from CITE-seq and scRNA-seq data.
- [MOGONET](https://github.com/txWang/MOGONET) [![GitHub stars](https://img.shields.io/github/stars/txWang/MOGONET?style=flat)](https://github.com/txWang/MOGONET/stargazers) — Multi-omics graph convolutional network framework for patient classification and biomarker identification.
- [AutoZyme](https://github.com/ElliotXie/autozyme) [![GitHub stars](https://img.shields.io/github/stars/ElliotXie/autozyme?style=flat)](https://github.com/ElliotXie/autozyme/stargazers) — Autonomous agentic framework that speeds up bioinformatics software (e.g. Scanpy, Seurat) on CPUs while preserving the original results.

---

## Machine Learning Tasks and Models

### Drug Discovery

#### Drug Response Prediction

- [drGAT](https://github.com/inoue0426/drGAT) [![GitHub stars](https://img.shields.io/github/stars/inoue0426/drGAT?style=flat)](https://github.com/inoue0426/drGAT/stargazers) — Attention-based model for drug response prediction with gene explainability.
- [MOFGCN](https://github.com/weiba/MOFGCN/tree/main) [![GitHub stars](https://img.shields.io/github/stars/weiba/MOFGCN/tree/main?style=flat)](https://github.com/weiba/MOFGCN/tree/main/stargazers) — GCN + heterogeneous network.
- [DeepDSC](https://ieeexplore-ieee-org.ezp2.lib.umn.edu/stamp/stamp.jsp?tp=&arnumber=8723620&tag=1) — Autoencoder + fully connected NN.
- [DGDRP](https://github.com/minwoopak/heteronet) [![GitHub stars](https://img.shields.io/github/stars/minwoopak/heteronet?style=flat)](https://github.com/minwoopak/heteronet/stargazers) — Multi-view embedding neural network.
- [DeepAEG](https://github.com/zhejiangzhuque/DeepAEG) [![GitHub stars](https://img.shields.io/github/stars/zhejiangzhuque/DeepAEG?style=flat)](https://github.com/zhejiangzhuque/DeepAEG/stargazers) — GNN embedding + attention mechanism.
- [RECOVER](https://github.com/RECOVERcoalition/Recover) [![GitHub stars](https://img.shields.io/github/stars/RECOVERcoalition/Recover?style=flat)](https://github.com/RECOVERcoalition/Recover/stargazers) — Machine learning framework for predicting synergistic drug combination responses across cell lines.
- [TGSA](https://github.com/violet-sto/TGSA) [![GitHub stars](https://img.shields.io/github/stars/violet-sto/TGSA?style=flat)](https://github.com/violet-sto/TGSA/stargazers) — Tumor gene set and attention-based model leveraging biological pathway knowledge for drug response prediction.
- [HiDRA](https://github.com/bsml320/HiDRA) [![GitHub stars](https://img.shields.io/github/stars/bsml320/HiDRA?style=flat)](https://github.com/bsml320/HiDRA/stargazers) — Hierarchical network model incorporating gene and pathway-level information for cancer drug response prediction.
- [PRNet](https://github.com/Perturbation-Response-Prediction/PRnet) [![GitHub stars](https://img.shields.io/github/stars/Perturbation-Response-Prediction/PRnet?style=flat)](https://github.com/Perturbation-Response-Prediction/PRnet/stargazers) — Deep generative model for predicting transcriptional responses to novel chemical perturbations for drug discovery.
- [chemCPA](https://github.com/theislab/chemCPA) [![GitHub stars](https://img.shields.io/github/stars/theislab/chemCPA?style=flat)](https://github.com/theislab/chemCPA/stargazers) — Compositional perturbation autoencoder for predicting single-cell transcriptional responses to unseen drug perturbations and dose combinations.
- [cycleCDR](https://github.com/hliulab/cycleCDR) [![GitHub stars](https://img.shields.io/github/stars/hliulab/cycleCDR?style=flat)](https://github.com/hliulab/cycleCDR/stargazers) — Interpretable cycle-consistency framework for modeling cellular responses to drug perturbations.
- [DRUML](https://github.com/CutillasLab/DRUMLR) [![GitHub stars](https://img.shields.io/github/stars/CutillasLab/DRUMLR?style=flat)](https://github.com/CutillasLab/DRUMLR/stargazers) — Ensemble machine learning framework combining standard ML with deep learning to systematically rank anti-cancer drugs from proteomics and RNA-seq data.

#### Drug Repurposing

- [DeepPurpose](https://github.com/kexinhuang12345/DeepPurpose) [![GitHub stars](https://img.shields.io/github/stars/kexinhuang12345/DeepPurpose?style=flat)](https://github.com/kexinhuang12345/DeepPurpose/stargazers) — Deep learning library for drug repurposing.
- [TranSiGen](https://github.com/myzhengSIMM/TranSiGen) [![GitHub stars](https://img.shields.io/github/stars/myzhengSIMM/TranSiGen?style=flat)](https://github.com/myzhengSIMM/TranSiGen/stargazers) — Dual-VAE architecture for ligand-based virtual screening, drug response prediction, and drug repurposing using chemical-induced transcriptional profiles.

#### Drug Target Interaction

- [NeoDTI](https://github.com/FangpingWan/NeoDTI) [![GitHub stars](https://img.shields.io/github/stars/FangpingWan/NeoDTI?style=flat)](https://github.com/FangpingWan/NeoDTI/stargazers) — Library for drug-target interaction prediction.
- [DTINet](https://github.com/luoyunan/DTINet) [![GitHub stars](https://img.shields.io/github/stars/luoyunan/DTINet?style=flat)](https://github.com/luoyunan/DTINet/stargazers) — Network-based framework integrating heterogeneous biological data for DTI prediction.
- [DeepDTA](https://github.com/hkmztrk/DeepDTA) [![GitHub stars](https://img.shields.io/github/stars/hkmztrk/DeepDTA?style=flat)](https://github.com/hkmztrk/DeepDTA/stargazers) — Deep learning model using CNNs on protein sequences and drug SMILES.
- [GraphDTA](https://github.com/thinng/GraphDTA) [![GitHub stars](https://img.shields.io/github/stars/thinng/GraphDTA?style=flat)](https://github.com/thinng/GraphDTA/stargazers) — Graph neural network–based DTI prediction using molecular graphs.
- [MolTrans](https://github.com/kexinhuang12345/MolTrans) [![GitHub stars](https://img.shields.io/github/stars/kexinhuang12345/MolTrans?style=flat)](https://github.com/kexinhuang12345/MolTrans/stargazers) — Transformer-based DTI model leveraging molecular substructures.
- [DrugBAN](https://github.com/peizhenbai/DrugBAN) [![GitHub stars](https://img.shields.io/github/stars/peizhenbai/DrugBAN?style=flat)](https://github.com/peizhenbai/DrugBAN/stargazers) — Bilinear attention network for interpretable DTI prediction.

#### Compound-Protein Interaction

- [MCPINN](https://github.com/mhlee0903/multi_channels_PINN) [![GitHub stars](https://img.shields.io/github/stars/mhlee0903/multi_channels_PINN?style=flat)](https://github.com/mhlee0903/multi_channels_PINN/stargazers) — Drug discovery via compound-protein interaction and machine learning.
- [TransformerCPI](https://github.com/lifanchen-simm/transformerCPI) [![GitHub stars](https://img.shields.io/github/stars/lifanchen-simm/transformerCPI?style=flat)](https://github.com/lifanchen-simm/transformerCPI/stargazers) — CPI prediction using Transformer.

#### Molecular Generation

- [REINVENT](https://github.com/MolecularAI/Reinvent) [![GitHub stars](https://img.shields.io/github/stars/MolecularAI/Reinvent?style=flat)](https://github.com/MolecularAI/Reinvent/stargazers) — Reinforcement learning for de novo drug design.
- [MolGPT](https://github.com/devalab/molgpt) [![GitHub stars](https://img.shields.io/github/stars/devalab/molgpt?style=flat)](https://github.com/devalab/molgpt/stargazers) — Transformer-based model for molecular generation.
- [Molecular Transformer](https://github.com/pschwllr/MolecularTransformer) [![GitHub stars](https://img.shields.io/github/stars/pschwllr/MolecularTransformer?style=flat)](https://github.com/pschwllr/MolecularTransformer/stargazers) — Sequence-to-sequence model for retrosynthesis prediction.
- [Matcha](https://github.com/LigandPro/Matcha) [![GitHub stars](https://img.shields.io/github/stars/LigandPro/Matcha?style=flat)](https://github.com/LigandPro/Matcha/stargazers) — Multi-stage Riemannian flow matching model for physically valid molecular docking with scoring, pose filtering, and benchmarks.
- [TargetDiff](https://github.com/guanjq/targetdiff) [![GitHub stars](https://img.shields.io/github/stars/guanjq/targetdiff?style=flat)](https://github.com/guanjq/targetdiff/stargazers) — 3D equivariant diffusion model for structure-based drug design.
- [DiffDock](https://github.com/gcorso/DiffDock) [![GitHub stars](https://img.shields.io/github/stars/gcorso/DiffDock?style=flat)](https://github.com/gcorso/DiffDock/stargazers) — Diffusion generative model for molecular docking, predicting the binding pose of small molecules to protein targets.
- [JTVAE](https://github.com/wengong-jin/icml18-jtnn) [![GitHub stars](https://img.shields.io/github/stars/wengong-jin/icml18-jtnn?style=flat)](https://github.com/wengong-jin/icml18-jtnn/stargazers) — Junction tree variational autoencoder for molecular graph generation that guarantees chemical validity via a hierarchical tree decomposition.
- [DiffSBDD](https://github.com/arneschneuing/DiffSBDD) [![GitHub stars](https://img.shields.io/github/stars/arneschneuing/DiffSBDD?style=flat)](https://github.com/arneschneuing/DiffSBDD/stargazers) — Equivariant diffusion model for structure-based drug design that generates molecules and binding conformations for protein targets.
- [ReLeaSE](https://github.com/isayev/ReLeaSE) [![GitHub stars](https://img.shields.io/github/stars/isayev/ReLeaSE?style=flat)](https://github.com/isayev/ReLeaSE/stargazers) — Deep reinforcement learning framework for de novo drug design combining a generative and predictive model.
- [PaccMannRL](https://github.com/PaccMann/paccmann_generator) [![GitHub stars](https://img.shields.io/github/stars/PaccMann/paccmann_generator?style=flat)](https://github.com/PaccMann/paccmann_generator/stargazers) — Reinforcement learning-based generative model for de novo hit-like anticancer molecule design from transcriptomic data.

### LLM for Biology

- [AI4Chem/ChemLLM-7B-Chat](https://huggingface.co/AI4Chem/ChemLLM-7B-Chat) — LLM for chemical & molecular science.
- [BioGPT](https://github.com/microsoft/BioGPT) [![GitHub stars](https://img.shields.io/github/stars/microsoft/BioGPT?style=flat)](https://github.com/microsoft/BioGPT/stargazers) — LLM for biomedical text generation.
- [GeneGPT](https://github.com/ncbi/GeneGPT) [![GitHub stars](https://img.shields.io/github/stars/ncbi/GeneGPT?style=flat)](https://github.com/ncbi/GeneGPT/stargazers) — LLM for biomedical information, integrated with various APIs.
- [GenePT](https://github.com/yiqunchen/GenePT) [![GitHub stars](https://img.shields.io/github/stars/yiqunchen/GenePT?style=flat)](https://github.com/yiqunchen/GenePT/stargazers) — Foundation LLM for single-cell data.
- [scPRINT](https://github.com/cantinilab/scPRINT) [![GitHub stars](https://img.shields.io/github/stars/cantinilab/scPRINT?style=flat)](https://github.com/cantinilab/scPRINT/stargazers) — Pretrained on 50M cells for scRNA-seq denoising & zero imputation.
- [ClawBio](https://github.com/ClawBio/ClawBio) [![GitHub stars](https://img.shields.io/github/stars/ClawBio/ClawBio?style=flat)](https://github.com/ClawBio/ClawBio/stargazers) — Bioinformatics-native AI agent skill library with local-first pharmacogenomics, ancestry PCA, semantic similarity, nutrigenomics, and metagenomics skills.
- [BioMedLM](https://huggingface.co/stanford-crfm/BioMedLM) — 2.7B parameter GPT-2-style language model trained exclusively on biomedical literature from PubMed for biomedical question answering and text generation.
- [MolT5](https://github.com/blender-nlp/MolT5) [![GitHub stars](https://img.shields.io/github/stars/blender-nlp/MolT5?style=flat)](https://github.com/blender-nlp/MolT5/stargazers) — Language model for molecular tasks bridging text and SMILES, enabling molecule captioning and text-driven molecule generation.
- [ChatDrug](https://github.com/chao1224/ChatDrug) [![GitHub stars](https://img.shields.io/github/stars/chao1224/ChatDrug?style=flat)](https://github.com/chao1224/ChatDrug/stargazers) — LLM-based conversational pipeline for drug discovery, using natural language prompts for iterative drug editing and optimization.
- [CASSIA](https://github.com/ElliotXie/CASSIA) [![GitHub stars](https://img.shields.io/github/stars/ElliotXie/CASSIA?style=flat)](https://github.com/ElliotXie/CASSIA/stargazers) — Multi-agent LLM for reference-free, interpretable cell-type annotation of single-cell RNA-seq data, with dedicated annotation, validation, scoring, and reporting agents.

### Foundation Models

#### Single-cell Foundation Models

##### Transcriptomics Foundation Models

- [scFoundation](https://github.com/biomap-research/scFoundation) [![GitHub stars](https://img.shields.io/github/stars/biomap-research/scFoundation?style=flat)](https://github.com/biomap-research/scFoundation/stargazers) — Large-scale foundation model for single-cell gene expression, enabling multiple downstream tasks.
- [scGPT](https://github.com/bowang-lab/scGPT) [![GitHub stars](https://img.shields.io/github/stars/bowang-lab/scGPT?style=flat)](https://github.com/bowang-lab/scGPT/stargazers) — Transformer-based foundation model pretrained on millions of single-cell profiles.
- [Geneformer](https://huggingface.co/ctheodoris/Geneformer) — Context-aware, attention-based deep learning model pretrained on a large corpus of single-cell transcriptomes.
- [BulkFormer](https://github.com/KangBoming/BulkFormer) [![GitHub stars](https://img.shields.io/github/stars/KangBoming/BulkFormer?style=flat)](https://github.com/KangBoming/BulkFormer/stargazers) — Foundation model for bulk RNA-seq data; learns general transcriptomic representations.
- [scBERT](https://github.com/TencentAILabHealthcare/scBERT) [![GitHub stars](https://img.shields.io/github/stars/TencentAILabHealthcare/scBERT?style=flat)](https://github.com/TencentAILabHealthcare/scBERT/stargazers) — BERT-based foundation model pretrained on large-scale scRNA-seq data for cell type annotation.
- [CellPLM](https://github.com/OmicsML/CellPLM) [![GitHub stars](https://img.shields.io/github/stars/OmicsML/CellPLM?style=flat)](https://github.com/OmicsML/CellPLM/stargazers) — Cell pre-trained language model with inter-cell transformer architecture for diverse single-cell analysis tasks.
- [UCE](https://github.com/snap-stanford/UCE) [![GitHub stars](https://img.shields.io/github/stars/snap-stanford/UCE?style=flat)](https://github.com/snap-stanford/UCE/stargazers) — Universal Cell Embeddings: zero-shot single-cell embedding model trained on 36M cells across species, tissues, and assays without fine-tuning.
- [GEARS](https://github.com/snap-stanford/GEARS) [![GitHub stars](https://img.shields.io/github/stars/snap-stanford/GEARS?style=flat)](https://github.com/snap-stanford/GEARS/stargazers) — Graph-based model for predicting transcriptional responses to single and combinatorial genetic perturbations using biological priors.
- [SATURN](https://github.com/snap-stanford/SATURN) [![GitHub stars](https://img.shields.io/github/stars/snap-stanford/SATURN?style=flat)](https://github.com/snap-stanford/SATURN/stargazers) — Transformer-based model integrating gene expression and protein sequences via a protein language model to learn unified multi-species cell embeddings.
- [CancerFoundation](https://github.com/BoevaLab/CancerFoundation) [![GitHub stars](https://img.shields.io/github/stars/BoevaLab/CancerFoundation?style=flat)](https://github.com/BoevaLab/CancerFoundation/stargazers) — Single-cell RNA-seq foundation model trained exclusively on a curated dataset of malignant cells to learn cancer-specific embeddings.

##### Spatial Foundation Models

- [GigaPath](https://github.com/prov-gigapath/prov-gigapath) [![GitHub stars](https://img.shields.io/github/stars/prov-gigapath/prov-gigapath?style=flat)](https://github.com/prov-gigapath/prov-gigapath/stargazers) — Slide-level digital pathology foundation model pretrained on 1.3 billion pathology image tokens from whole-slide images.
- [UNI](https://github.com/mahmoodlab/UNI) [![GitHub stars](https://img.shields.io/github/stars/mahmoodlab/UNI?style=flat)](https://github.com/mahmoodlab/UNI/stargazers) — General-purpose self-supervised pathology foundation model trained on 100K+ whole-slide images for diverse computational pathology tasks.
- [CONCH](https://github.com/mahmoodlab/CONCH) [![GitHub stars](https://img.shields.io/github/stars/mahmoodlab/CONCH?style=flat)](https://github.com/mahmoodlab/CONCH/stargazers) — Vision-language foundation model for computational pathology trained with contrastive captioning on pathology image–text pairs.
- [Phikon](https://huggingface.co/owkin/phikon) — ViT-based pathology foundation model pretrained with iBOT self-supervision on TCGA whole-slide images.
- [Nicheformer](https://github.com/theislab/nicheformer) [![GitHub stars](https://img.shields.io/github/stars/theislab/nicheformer?style=flat)](https://github.com/theislab/nicheformer/stargazers) — Foundation model for single-cell and spatial omics using a transformer architecture with positional embeddings to encode spatial cell information.
- [scGPT-spatial](https://github.com/bowang-lab/scGPT-spatial) [![GitHub stars](https://img.shields.io/github/stars/bowang-lab/scGPT-spatial?style=flat)](https://github.com/bowang-lab/scGPT-spatial/stargazers) — Extension of scGPT for spatial transcriptomics with continual pretraining and a mixture-of-experts decoder for spatial gene expression analysis.

##### Multi-Omics Foundation Models

- [scMulan](https://github.com/SuperBianC/scMulan) [![GitHub stars](https://img.shields.io/github/stars/SuperBianC/scMulan?style=flat)](https://github.com/SuperBianC/scMulan/stargazers) — Single-cell multi-omic language model pretrained on ~10M cells spanning transcriptomics, epigenomics, and proteomics for cross-omics transfer tasks.
- [totalVI](https://github.com/scverse/scvi-tools) [![GitHub stars](https://img.shields.io/github/stars/scverse/scvi-tools?style=flat)](https://github.com/scverse/scvi-tools/stargazers) — Probabilistic framework for joint analysis of paired scRNA-seq and protein (CITE-seq) data enabling multi-modal cell state representation across single-cell datasets.
- [MultiVI](https://github.com/scverse/scvi-tools) [![GitHub stars](https://img.shields.io/github/stars/scverse/scvi-tools?style=flat)](https://github.com/scverse/scvi-tools/stargazers) — Multi-modal variational autoencoder for integrating paired and unpaired single-cell RNA-seq and ATAC-seq measurements into a unified latent space.
- [MIRA](https://github.com/cistrome/MIRA) [![GitHub stars](https://img.shields.io/github/stars/cistrome/MIRA?style=flat)](https://github.com/cistrome/MIRA/stargazers) — Probabilistic multimodal topic model jointly modeling single-cell transcriptomics and chromatin accessibility for regulatory network inference.
- [GLUE](https://github.com/gao-lab/GLUE) [![GitHub stars](https://img.shields.io/github/stars/gao-lab/GLUE?style=flat)](https://github.com/gao-lab/GLUE/stargazers) — Graph-Linked Unified Embedding framework for unpaired single-cell multi-omics data integration across RNA, ATAC, methylation, and protein modalities.
- [BABEL](https://github.com/wukevin/babel) [![GitHub stars](https://img.shields.io/github/stars/wukevin/babel?style=flat)](https://github.com/wukevin/babel/stargazers) — Cross-modality translation model enabling prediction between scRNA-seq and scATAC-seq profiles without requiring paired single-cell measurements.
- [Multigrate](https://github.com/theislab/multigrate) [![GitHub stars](https://img.shields.io/github/stars/theislab/multigrate?style=flat)](https://github.com/theislab/multigrate/stargazers) — Asymmetric multi-omics variational autoencoder for integrating single-cell data across RNA, ATAC, and protein modalities with missing-modality support.
- [MOFA+](https://github.com/bioFAM/MOFA2) [![GitHub stars](https://img.shields.io/github/stars/bioFAM/MOFA2?style=flat)](https://github.com/bioFAM/MOFA2/stargazers) — Multi-Omics Factor Analysis framework identifying shared axes of variation across bulk and single-cell datasets including RNA, ATAC, proteomics, methylation, and copy number.
- [GeneCompass](https://github.com/xCompass-AI/GeneCompass) [![GitHub stars](https://img.shields.io/github/stars/xCompass-AI/GeneCompass?style=flat)](https://github.com/xCompass-AI/GeneCompass/stargazers) — Large-scale foundation model integrating DNA regulatory sequences and single-cell transcriptomics from 120M+ cells across multiple species for gene regulation prediction.
- [UnitedNet](https://github.com/LiuLab-Bioelectronics-Harvard/UnitedNet) [![GitHub stars](https://img.shields.io/github/stars/LiuLab-Bioelectronics-Harvard/UnitedNet?style=flat)](https://github.com/LiuLab-Bioelectronics-Harvard/UnitedNet/stargazers) — Interpretable multi-task deep neural network for single-cell multi-omics integration spanning transcriptomics, chromatin accessibility, and proteomics.
- [SpatialGlue](https://github.com/zhanglabtools/SpatialGlue) [![GitHub stars](https://img.shields.io/github/stars/zhanglabtools/SpatialGlue?style=flat)](https://github.com/zhanglabtools/SpatialGlue/stargazers) — Graph attention network for spatial multi-omics integration jointly embedding spatial transcriptomics with chromatin accessibility or proteomics.
- [MIDAS](https://github.com/labomics/midas) [![GitHub stars](https://img.shields.io/github/stars/labomics/midas?style=flat)](https://github.com/labomics/midas/stargazers) — Mosaic integration and differential accessibility model for single-cell multi-omics data that handles arbitrary missing-modality combinations across transcriptomics, chromatin accessibility, and proteomics.
- [Concerto](https://github.com/melobio/Concerto-reproducibility) [![GitHub stars](https://img.shields.io/github/stars/melobio/Concerto-reproducibility?style=flat)](https://github.com/melobio/Concerto-reproducibility/stargazers) — Contrastive self-supervised learning framework for single-cell multimodal data integration, batch correction, and reference-query mapping.
- [scButterfly](https://github.com/BioX-NKU/scButterfly) [![GitHub stars](https://img.shields.io/github/stars/BioX-NKU/scButterfly?style=flat)](https://github.com/BioX-NKU/scButterfly/stargazers) — Dual-aligned variational autoencoder for single-cell cross-modality translation between paired and unpaired multiomics data.
- [JAMIE](https://github.com/Oafish1/JAMIE) [![GitHub stars](https://img.shields.io/github/stars/Oafish1/JAMIE?style=flat)](https://github.com/Oafish1/JAMIE/stargazers) — Joint variational autoencoder for multimodal single-cell data imputation and embedding.
- [scPair](https://github.com/quon-titative-biology/scPair) [![GitHub stars](https://img.shields.io/github/stars/quon-titative-biology/scPair?style=flat)](https://github.com/quon-titative-biology/scPair/stargazers) — Bidirectional feedforward network for single-cell multimodal analysis with cross-modality prediction leveraging single-cell atlases.

##### Domain Alignment

- [scArches](https://github.com/theislab/scarches) [![GitHub stars](https://img.shields.io/github/stars/theislab/scarches?style=flat)](https://github.com/theislab/scarches/stargazers) — Transfer learning framework for mapping new single-cell datasets onto pre-trained reference atlases across batches, conditions, and modalities.
- [TOSICA](https://github.com/JackieHanlaopo/TOSICA) [![GitHub stars](https://img.shields.io/github/stars/JackieHanlaopo/TOSICA?style=flat)](https://github.com/JackieHanlaopo/TOSICA/stargazers) — Transformer-based framework for one-stop interpretable cell-type annotation supporting cross-dataset and cross-species transfer.

#### Compound Foundation Models

##### Compound Embedding

- [ChemBERTa-2](https://github.com/seyonechithrananda/bert-loves-chemistry) [![GitHub stars](https://img.shields.io/github/stars/seyonechithrananda/bert-loves-chemistry?style=flat)](https://github.com/seyonechithrananda/bert-loves-chemistry/stargazers) — RoBERTa-based molecular language model pretrained on SMILES for small-molecule representation learning.
- [GROVER](https://github.com/tencent-ailab/grover) [![GitHub stars](https://img.shields.io/github/stars/tencent-ailab/grover?style=flat)](https://github.com/tencent-ailab/grover/stargazers) — Self-supervised graph transformer for large-scale molecular representation learning from unlabeled compounds.
- [Mol2Vec](https://github.com/samoturk/mol2vec) [![GitHub stars](https://img.shields.io/github/stars/samoturk/mol2vec?style=flat)](https://github.com/samoturk/mol2vec/stargazers) — Unsupervised molecular embedding method inspired by Word2Vec for learning vector representations of chemical substructures.
- [MolFormer](https://github.com/IBM/molformer) [![GitHub stars](https://img.shields.io/github/stars/IBM/molformer?style=flat)](https://github.com/IBM/molformer/stargazers) — Linear attention transformer pretrained on millions of SMILES strings for efficient molecular embeddings.
- [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) [![GitHub stars](https://img.shields.io/github/stars/deepmodeling/Uni-Mol?style=flat)](https://github.com/deepmodeling/Uni-Mol/stargazers) — 3D molecular pretraining framework for universal representation learning on molecules and protein pockets.

#### Protein Foundation Models

##### Pre-trained Embedding

- [Evolutionary Scale Modeling (ESM)](https://github.com/facebookresearch/esm) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/esm?style=flat)](https://github.com/facebookresearch/esm/stargazers) — Protein embeddings.
- [ProtTrans](https://github.com/agemagician/ProtTrans) [![GitHub stars](https://img.shields.io/github/stars/agemagician/ProtTrans?style=flat)](https://github.com/agemagician/ProtTrans/stargazers) — Suite of protein language models (ProtBERT, ProtT5, ProtXLNet) trained on billions of protein sequences from UniRef and BFD.
- [ProGen2](https://github.com/salesforce/progen) [![GitHub stars](https://img.shields.io/github/stars/salesforce/progen?style=flat)](https://github.com/salesforce/progen/stargazers) — Protein language model trained on diverse protein families for sequence generation and fitness prediction.
- [Ankh](https://github.com/agemagician/Ankh) [![GitHub stars](https://img.shields.io/github/stars/agemagician/Ankh?style=flat)](https://github.com/agemagician/Ankh/stargazers) — Efficient protein language model optimized for downstream prediction tasks including secondary structure, localization, and function annotation.

##### Protein Structure Prediction and Design

- [AlphaFold3](https://github.com/google-deepmind/alphafold3) [![GitHub stars](https://img.shields.io/github/stars/google-deepmind/alphafold3?style=flat)](https://github.com/google-deepmind/alphafold3/stargazers) — Predicts structures of proteins, nucleic acids, small molecules, and their complexes.
- [Boltz-1](https://github.com/jwohlwend/boltz) [![GitHub stars](https://img.shields.io/github/stars/jwohlwend/boltz?style=flat)](https://github.com/jwohlwend/boltz/stargazers) — Open-source all-atom biomolecular structure prediction model for proteins, nucleic acids, small molecules, and their complexes achieving AlphaFold3-level accuracy.
- [Chai-1](https://github.com/chaidiscovery/chai-lab) [![GitHub stars](https://img.shields.io/github/stars/chaidiscovery/chai-lab?style=flat)](https://github.com/chaidiscovery/chai-lab/stargazers) — Unified molecular structure prediction model covering proteins, nucleic acids, small molecules, and complexes.
- [ESM3](https://github.com/evolutionaryscale/esm) [![GitHub stars](https://img.shields.io/github/stars/evolutionaryscale/esm?style=flat)](https://github.com/evolutionaryscale/esm/stargazers) — Multimodal protein language model that jointly reasons over sequence, structure, and function for generative protein design and engineering.
- [ESMFold](https://github.com/facebookresearch/esm) [![GitHub stars](https://img.shields.io/github/stars/facebookresearch/esm?style=flat)](https://github.com/facebookresearch/esm/stargazers) — Fast protein structure prediction using language model embeddings.
- [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) [![GitHub stars](https://img.shields.io/github/stars/RosettaCommons/RFdiffusion?style=flat)](https://github.com/RosettaCommons/RFdiffusion/stargazers) — Generative model for protein backbone design using diffusion.
- [ProteinMPNN](https://github.com/dauparas/ProteinMPNN) [![GitHub stars](https://img.shields.io/github/stars/dauparas/ProteinMPNN?style=flat)](https://github.com/dauparas/ProteinMPNN/stargazers) — Deep learning model for protein sequence design given backbone structure.
- [OmegaFold](https://github.com/HeliXonProtein/OmegaFold) [![GitHub stars](https://img.shields.io/github/stars/HeliXonProtein/OmegaFold?style=flat)](https://github.com/HeliXonProtein/OmegaFold/stargazers) — High-resolution de novo protein structure prediction from sequence.
- [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold) [![GitHub stars](https://img.shields.io/github/stars/RosettaCommons/RoseTTAFold?style=flat)](https://github.com/RosettaCommons/RoseTTAFold/stargazers) — Three-track neural network for protein structure prediction.
- [OpenFold](https://github.com/aqlaboratory/openfold) [![GitHub stars](https://img.shields.io/github/stars/aqlaboratory/openfold?style=flat)](https://github.com/aqlaboratory/openfold/stargazers) — Trainable, memory-efficient open-source reproduction of AlphaFold2 enabling custom protein structure prediction workflows.
- [SaProt](https://github.com/westlake-reup/SaProt) [![GitHub stars](https://img.shields.io/github/stars/westlake-reup/SaProt?style=flat)](https://github.com/westlake-reup/SaProt/stargazers) — Structure-aware protein language model using structure-aware tokens that encode both sequence and backbone geometry for improved function prediction.
- [EvoDiff](https://github.com/microsoft/evodiff) [![GitHub stars](https://img.shields.io/github/stars/microsoft/evodiff?style=flat)](https://github.com/microsoft/evodiff/stargazers) — Discrete diffusion framework for protein sequence generation trained on evolutionary-scale data, supporting unconditional generation, disordered region design, and functional motif scaffolding. [ [paper-2023](https://www.biorxiv.org/content/10.1101/2023.09.11.556673v1) ]

#### Multi-Modal Foundation Models

- [CHIEF](https://github.com/hms-dbmi/CHIEF) [![GitHub stars](https://img.shields.io/github/stars/hms-dbmi/CHIEF?style=flat)](https://github.com/hms-dbmi/CHIEF/stargazers) — Clinical Histopathology Imaging Evaluation Foundation model integrating histology images and clinical context for pan-cancer analysis.
- [BiomedCLIP](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_g_14) — CLIP-based vision-language foundation model for biomedical images and text trained on PubMed figure–caption pairs.
- [PORPOISE](https://github.com/mahmoodlab/PORPOISE) [![GitHub stars](https://img.shields.io/github/stars/mahmoodlab/PORPOISE?style=flat)](https://github.com/mahmoodlab/PORPOISE/stargazers) — Pan-cancer integrative histology-genomic analysis framework using multimodal deep learning for patient stratification.
- [PathomicFusion](https://github.com/mahmoodlab/PathomicFusion) [![GitHub stars](https://img.shields.io/github/stars/mahmoodlab/PathomicFusion?style=flat)](https://github.com/mahmoodlab/PathomicFusion/stargazers) — Integrated framework fusing histopathology and genomic features via CNN, GNN, and attention gating for cancer diagnosis and prognosis.
- [Virchow](https://huggingface.co/paige-ai/Virchow) — Million-slide digital pathology foundation model using a vision transformer and self-supervised distillation for tile-level pathology image representation.
- [TOAD](https://github.com/mahmoodlab/TOAD) [![GitHub stars](https://img.shields.io/github/stars/mahmoodlab/TOAD?style=flat)](https://github.com/mahmoodlab/TOAD/stargazers) — Tumor Origin Assessment via Deep-learning; weakly-supervised multi-task model predicting cancer primary origin from H&E whole-slide images.
- [PLIP](https://github.com/PathologyFoundation/plip) [![GitHub stars](https://img.shields.io/github/stars/PathologyFoundation/plip?style=flat)](https://github.com/PathologyFoundation/plip/stargazers) — Vision-language foundation model for pathology trained with contrastive learning on pathology image–text pairs for image classification and text-to-image retrieval.
- [MUSK](https://github.com/lilab-stanford/MUSK) [![GitHub stars](https://img.shields.io/github/stars/lilab-stanford/MUSK?style=flat)](https://github.com/lilab-stanford/MUSK/stargazers) — Vision-language foundation model for precision oncology analyzing multimodal paired text and pathology image data for biomarker prediction and retrieval.

#### Genomics Foundation Models

- [Nucleotide Transformer](https://github.com/instadeepai/nucleotide-transformer) [![GitHub stars](https://img.shields.io/github/stars/instadeepai/nucleotide-transformer?style=flat)](https://github.com/instadeepai/nucleotide-transformer/stargazers) — Foundation model for genomic sequences across multiple species.
- [DNABERT](https://github.com/jerryji1993/DNABERT) [![GitHub stars](https://img.shields.io/github/stars/jerryji1993/DNABERT?style=flat)](https://github.com/jerryji1993/DNABERT/stargazers) — Pre-trained bidirectional encoder for DNA sequence analysis.
- [DNABERT-2](https://github.com/Zhihan1996/DNABERT_2) [![GitHub stars](https://img.shields.io/github/stars/Zhihan1996/DNABERT_2?style=flat)](https://github.com/Zhihan1996/DNABERT_2/stargazers) — Improved genome foundation model with efficient tokenization.
- [Enformer](https://github.com/deepmind/deepmind-research/tree/master/enformer) [![GitHub stars](https://img.shields.io/github/stars/deepmind/deepmind-research/tree/master/enformer?style=flat)](https://github.com/deepmind/deepmind-research/tree/master/enformer/stargazers) — Transformer model predicting gene expression from DNA sequence.
- [Basenji](https://github.com/calico/basenji) [![GitHub stars](https://img.shields.io/github/stars/calico/basenji?style=flat)](https://github.com/calico/basenji/stargazers) — Sequential regulatory activity prediction from DNA sequences.
- [Caduceus](https://github.com/kuleshov-group/caduceus) [![GitHub stars](https://img.shields.io/github/stars/kuleshov-group/caduceus?style=flat)](https://github.com/kuleshov-group/caduceus/stargazers) — Bidirectional equivariant long-range DNA sequence model based on Mamba.
- [Evo](https://github.com/evo-design/evo) [![GitHub stars](https://img.shields.io/github/stars/evo-design/evo?style=flat)](https://github.com/evo-design/evo/stargazers) — Long-context genomic foundation model (up to 1M tokens).
- [HyenaDNA](https://github.com/HazyResearch/hyena-dna) [![GitHub stars](https://img.shields.io/github/stars/HazyResearch/hyena-dna?style=flat)](https://github.com/HazyResearch/hyena-dna/stargazers) — Long-range genomic foundation model handling sequences up to 1M tokens with sub-quadratic attention.
- [Borzoi](https://github.com/calico/borzoi) [![GitHub stars](https://img.shields.io/github/stars/calico/borzoi?style=flat)](https://github.com/calico/borzoi/stargazers) — Extended successor to Enformer for predicting RNA-seq coverage from long genomic sequence windows (524 kb) with improved resolution.
- [DeepSEA](http://deepsea.princeton.edu/) — Deep learning framework for predicting chromatin effects of sequence alterations with single-nucleotide sensitivity across thousands of chromatin features.
- [Sei](https://github.com/FunctionLab/sei-framework) [![GitHub stars](https://img.shields.io/github/stars/FunctionLab/sei-framework?style=flat)](https://github.com/FunctionLab/sei-framework/stargazers) — Sequence-to-function framework learning a genome-wide regulatory activity code from DNA sequences for variant effect prediction.
- [GPN (Genomic Pre-trained Network)](https://github.com/songlab-cal/gpn) [![GitHub stars](https://img.shields.io/github/stars/songlab-cal/gpn?style=flat)](https://github.com/songlab-cal/gpn/stargazers) — Masked language model for DNA sequences enabling zero-shot variant effect prediction without requiring functional annotations.

---

## Citation

If you use this list in papers, slides, or documentation, please cite this repository via [`CITATION.cff`](./CITATION.cff) (also available through GitHub's **Cite this repository** button).

## Curation Criteria (Strict)

To keep quality high, additions should meet all of the following:

- The resource is trustworthy and relevant to computational biology.
- The primary link points to an official source (official docs, organization site, maintained repository, or official dataset page).
- The resource has evidence of technical substance: ideally a peer-reviewed paper; at minimum a preprint or official technical documentation.
- The description is factual and concise (no marketing copy).
- Duplicate or near-duplicate entries should be avoided.

We generally do **not** accept entries that are only promotional pages, personal opinion posts, or generic blog posts without technical references.

## Update & Link Rot Policy

- Link validity is monitored by the [Link Check workflow](./.github/workflows/link-check.yml).
- If a link repeatedly fails, maintainers may replace it with an official mirror/canonical URL or remove the entry until a stable URL is available.
- Contributions fixing broken links are welcome and encouraged.

## Data Schema & Contribution Workflow

- Data schema reference: [`docs/data/SCHEMA.md`](./docs/data/SCHEMA.md).
- Source-of-truth workflow:
  1. Edit/add resources in `README.md`.
  2. Regenerate machine-readable artifacts:
     - `python scripts/sync_resources_from_readme.py`
     - `python scripts/build_resources.py`
  3. Commit updated data files (`data/resources.yml`, `data/resources.json`, `data/resources.csv`, `docs/data/resources.json`) with your README change.
- Contribution guide: [`contributing.md`](./contributing.md).
