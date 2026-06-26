# HPC

[![GitHub stars](https://img.shields.io/github/stars/dstdev/awesome-hpc?style=flat)](https://github.com/dstdev/awesome-hpc/stargazers)

<!--lint ignore-->
# Awesome HPC [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

High Performance Computing tools and resources for engineers and administrators.

[High Performance Computing (HPC)](https://en.wikipedia.org/wiki/Supercomputer) most generally refers to the practice of aggregating computing power in a way that delivers much higher performance than one could get out of a typical desktop computer or workstation in order to solve large problems in science, engineering, or business.


## Contents
<details>
  <summary><b>(click to expand)</b></summary>
  
- [Provisioning](#provisioning)
- [Workload Managers](#workload-managers)
- [Pipelines](#pipelines)
- [Applications](#applications)
- [Compilers](#compilers)
- [MPI](#mpi)
- [Parallel Computing](#parallel-computing)
- [Benchmarking](#benchmarking)
- [Miscellaneous](#miscellaneous)
- [Performance](#performance)
- [Parallel Shells](#parallel-shells)
- [Containers](#containers)
- [Environment Management](#environment-management)
- [Visualization](#visualization)
- [Parallel Filesystems](#parallel-filesystems)
- [Programming Languages](#programming-languages)
- [Monitoring](#monitoring)
- [Journals](#journals)
- [Podcasts](#podcasts)
- [Blogs](#blogs)
- [Conferences](#conferences)
- [Websites](#websites)
- [User Groups](#user-groups)

</details>

## Provisioning
- [Grendel](https://grendel.readthedocs.io/) - Bare Metal Provisioning system for HPC Linux clusters ([Source Code](https://github.com`ubccr/grendel)) `GPL-3`.
- [XCat](https://xcat.org/) - xCAT is a toolkit for deployment and administration of clusters of all sizes ([Source Code](https://github.com/xcat2/xcat-core) [![GitHub stars](https://img.shields.io/github/stars/xcat2/xcat-core?style=flat)](https://github.com/xcat2/xcat-core/stargazers)) `EPL-1.0`.
- [Warewulf](https://warewulf.hpcng.org/) - Warewulf is a stateless and diskless container operating system provisioning system for large clusters of bare metal and/or virtual systems ([Source Code](https://github.com/hpcng/warewulf) [![GitHub stars](https://img.shields.io/github/stars/hpcng/warewulf?style=flat)](https://github.com/hpcng/warewulf/stargazers)) `BSD-3`.
- [Rocks](http://www.rocksclusters.org/) - A Linux distribution for developing Linux clusters `other`.
- [Cobbler](https://cobbler.github.io/) - Cobbler is a Linux installation server that allows for rapid setup of network installation environments ([Source Code](https://github.com/cobbler/cobbler) [![GitHub stars](https://img.shields.io/github/stars/cobbler/cobbler?style=flat)](https://github.com/cobbler/cobbler/stargazers)) `GPL-2.0`.
- [Base Command Manager](https://docs.nvidia.com/base-command-manager/index.html) - Base Command Manager allows administrator to quickly build and manage heterogeneous clusters `Proprietary`.
- [Scyld](https://www.penguinsolutions.com/computing/products/software/scyld-clusterware/) - Scyld Clusterware Scyld ClusterWare is developed based on the continuing evolution of Beowulf clusters first developed at NASA in the 1990s `Proprietary`.
- [BlueBanquise](https://bluebanquise.com) - BlueBanquise is an open source cluster deployment and management stack built on Python and Ansible ([Source Code](https://github.com/bluebanquise/bluebanquise) [![GitHub stars](https://img.shields.io/github/stars/bluebanquise/bluebanquise?style=flat)](https://github.com/bluebanquise/bluebanquise/stargazers)) `MIT`.

## Workload Managers
- [Slurm](https://slurm.schedmd.com/documentation.html) - A free and open source job scheduler ([Source Code](https://github.com/SchedMD/slurm) [![GitHub stars](https://img.shields.io/github/stars/SchedMD/slurm?style=flat)](https://github.com/SchedMD/slurm/stargazers)) `OSS`.
- [LSF](https://www.ibm.com/products/hpc-workload-management) - A job scheduler and workload management software developed by IBM `Proprietary`.
- [Moab](https://adaptivecomputing.com/moab-hpc-suite/) - Moab is a workload management and job scheduler `other`.
- [Torque](https://en.wikipedia.org/wiki/TORQUE) - Torque is a workload management and job scheduler `other`.
- [OpenLava](https://en.wikipedia.org/wiki/OpenLava) - OpenLava is a workload management and job scheduler `other`.
- [UGE/SGE](https://en.wikipedia.org/wiki/Univa_Grid_Engine) - Univa Grid Engine is a workload management engine for HPC `Proprietary`.
- [Volcano](https://volcano.sh/) - Volcano is a batch system built on Kubernetes `Apache-2.0`.
- [Maui](https://www.mhpcc.hpc.mil/) - Maui is a workload management and job scheduler `other`.
- [Kube Batch](https://github.com/kubernetes-sigs/kube-batch) [![GitHub stars](https://img.shields.io/github/stars/kubernetes-sigs/kube-batch?style=flat)](https://github.com/kubernetes-sigs/kube-batch/stargazers) - A batch scheduler of kubernetes for high performance workload, e.g. AI/ML, BigData, HPC `Apache-2.0`.
- [OpenPBS](https://www.openpbs.org/) - OpenPBS® software optimizes job scheduling and workload management in high-performance computing (HPC) environments ([Source Code](https://github.com/openpbs/openpbs) [![GitHub stars](https://img.shields.io/github/stars/openpbs/openpbs?style=flat)](https://github.com/openpbs/openpbs/stargazers)) `other`.

## Pipelines
- [Nextflow](https://nextflow.io) - Data drive computational pipelines `Apache-2.0`.
- [Cromwell](https://cromwell.readthedocs.io/en/stable/) - Scientific workflow engine designed for simplicity & scalability ([Source Code](https://github.com/broadinstitute/cromwell) [![GitHub stars](https://img.shields.io/github/stars/broadinstitute/cromwell?style=flat)](https://github.com/broadinstitute/cromwell/stargazers)) `BSD-3`.
- [Pegasus](https://pegasus.isi.edu/) - A configurable system for mapping and executing scientific workflows over a wide range of computational infrastructure ([Source Code](https://github.com/pegasus-isi/pegasus) [![GitHub stars](https://img.shields.io/github/stars/pegasus-isi/pegasus?style=flat)](https://github.com/pegasus-isi/pegasus/stargazers))`Apache-2.0`.

## Applications
- [Spack](https://spack.io) - A flexible package manager that supports multiple versions, configurations, platforms, and compilers ([Source Code](https://github.com/spack/spack) [![GitHub stars](https://img.shields.io/github/stars/spack/spack?style=flat)](https://github.com/spack/spack/stargazers)) `other`.
- [EasyBuild](https://easybuild.io/) -  EasyBuild - building software with ease ([Source Code](https://github.com/easybuilders/easybuild) [![GitHub stars](https://img.shields.io/github/stars/easybuilders/easybuild?style=flat)](https://github.com/easybuilders/easybuild/stargazers)) `GPL-2`.

## Compilers
- [Nvidia](https://developer.nvidia.com/hpc-compilers) - NVIDIA HPC compiler suite for Fortran, C/C++ with OpenACC `Proprietary`.
- [Portland Group](https://www.pgroup.com/index.htm) - The Portland Group compilers were Fortran, C/C++ compilers now integrated into NVIDIA HPC SDK `Proprietary`.
- [Intel](https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html#hpc-kit) - The Intel compiler suite offers many language compilers for use in the HPC space `Proprietary`.
- [Cray](https://bluewaters.ncsa.illinois.edu/cray-compiler) - A suite of compilers designed and optimized to target the AMD interlagos instruction set `Proprietary`.
- [GNU](https://gcc.gnu.org/) - The GNU Compiler Collection is a suite of compilers targeting many languages ([Source Code](https://gcc.gnu.org/git.html)) `GPL-3`.
- [LLVM](https://llvm.org/) - The LLVM project is a collection of modular compilers and toolchains ([Source Code](https://github.com/llvm/llvm-project) [![GitHub stars](https://img.shields.io/github/stars/llvm/llvm-project?style=flat)](https://github.com/llvm/llvm-project/stargazers)) `OSS`.

## MPI
- [OpenMPI](https://www.open-mpi.org/) - OpenMPI is an open source implementation of the MPI-3.1 standard ([Source Code](https://github.com/open-mpi/ompi) [![GitHub stars](https://img.shields.io/github/stars/open-mpi/ompi?style=flat)](https://github.com/open-mpi/ompi/stargazers)) `BSD`.
- [MPICH](https://www.mpich.org/) - MPICH is a high-performance and widely portable implementation of the MPI-3.1 standard ([Source Code](https://github.com/pmodels/mpich) [![GitHub stars](https://img.shields.io/github/stars/pmodels/mpich?style=flat)](https://github.com/pmodels/mpich/stargazers)) `other`.
- [MVAPICH](https://mvapich.cse.ohio-state.edu/) - MVAPICH is an open source implementation of the MPI-3.1 standard developed by Ohio State University `BSD`.
- [Intel-MPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html) - Intel-MPI is Intel's MPI-3.1 implementation included in their compiler suite `other`.

## Parallel Computing
- [ArrayFire](https://arrayfire.org/docs/index.htm) - A general purpose tensor library that simplifies the process of software development for parallel architectures `other`.
- [OpenMP](https://www.openmp.org/) - OpenMP is an application programming interface that supports multi-platform shared-memory multiprocessing programming `other`.

## Benchmarking
- [OSU Benchmarks](https://mvapich.cse.ohio-state.edu/benchmarks/) - A collection of benchmarking tools for MPI developed by Ohio State University `other`.
- [Intel MPI Benchmarks](https://software.intel.com/content/www/us/en/develop/articles/intel-mpi-benchmarks.html) - A set of benchmarks developed by Intel for use with their Intel MPI `other`.
- [HPCC Systems](https://hpccsystems.com/) - HPCC Systems (High Performance Computing Cluster) is an open source, massive parallel-processing computing platform for big data processing and analytics ([Source Code](https://github.com/hpcc-systems/HPCC-Platform) [![GitHub stars](https://img.shields.io/github/stars/hpcc-systems/HPCC-Platform?style=flat)](https://github.com/hpcc-systems/HPCC-Platform/stargazers)) `other`.
- [LINPACK](https://www.netlib.org/linpack/) - LINPACK is a set of efficient fortran subroutines for solving linear systems which benchmarks are useful for HPC `other`.
- [IOzone](https://www.iozone.org/) - IOzone is a filesystem benchmark tool `OSS`.
- [IOR](https://www.vi4io.org/tools/benchmarks/ior) - Interleaved or Random is a useful benchmarking tool for testing parallel filesystems `other`.
- [MDtest](https://www.vi4io.org/tools/benchmarks/mdtest) - MDtest is an MPI-based application for evaluating the metadata performance of a file system `other`.
- [FIO](https://fio.readthedocs.io/en/latest/fio_doc.html) - Flexible I/O is an advanced disk benchmark that depends upon the kernel's AIO access library ([Source Code](https://git.kernel.dk/cgit/fio/)) `GPL-2`.
- [elbencho](https://github.com/breuner/elbencho) [![GitHub stars](https://img.shields.io/github/stars/breuner/elbencho?style=flat)](https://github.com/breuner/elbencho/stargazers) - A distributed storage benchmark for files, objects & blocks with support for GPUs `GPL-3`.

## Miscellaneous
- [OpenOnDemand](https://openondemand.org/) - Open OnDemand helps computational researchers and students efficiently utilize remote computing resources by making them easy to access from any device ([Source Code](https://github.com/OSC/openondemand.org) [![GitHub stars](https://img.shields.io/github/stars/OSC/openondemand.org?style=flat)](https://github.com/OSC/openondemand.org/stargazers)) `MIT`.
- [Open XDMod](https://open.xdmod.org) - Open XDMoD is an open source tool to facilitate the management of high performance computing resources ([Source Code](https://github.com/ubccr/xdmod/) [![GitHub stars](https://img.shields.io/github/stars/ubccr/xdmod/?style=flat)](https://github.com/ubccr/xdmod//stargazers)) `LGPL-3`.
- [Coldfront](https://coldfront.readthedocs.io/en/latest/) - ColdFront is an open source resource allocation system designed to provide a central portal for administration, reporting, and measuring scientific impact of HPC resources ([Source Code](https://github.com/ubccr/coldfront) [![GitHub stars](https://img.shields.io/github/stars/ubccr/coldfront?style=flat)](https://github.com/ubccr/coldfront/stargazers)) `GPL-3`.
- [Pavilion2](https://pavilion2.readthedocs.io/) - Pavilion is a Python 3 (3.6+) based framework for running and analyzing tests targeting HPC systems ([Source Code](https://github.com/hpc/pavilion2) [![GitHub stars](https://img.shields.io/github/stars/hpc/pavilion2?style=flat)](https://github.com/hpc/pavilion2/stargazers)) `other`.
- [Reframe](https://reframe-hpc.readthedocs.io/en/stable/) - A powerful Python framework for writing and running portable regression tests and benchmarks for HPC systems. ([Source Code](https://github.com/reframe-hpc/reframe) [![GitHub stars](https://img.shields.io/github/stars/reframe-hpc/reframe?style=flat)](https://github.com/reframe-hpc/reframe/stargazers)) `BSD-3`.
- [OLCF Test Harness](https://olcf.github.io/olcf-test-harness/) - The OLCF Test Harness (OTH) helps automate the testing of applications, tools, and other system software ([Source Code](https://github.com/olcf/olcf-test-harness) [![GitHub stars](https://img.shields.io/github/stars/olcf/olcf-test-harness?style=flat)](https://github.com/olcf/olcf-test-harness/stargazers)) `other`. 
- [GoSlmailer](https://github.com/CLIP-HPC/goslmailer) [![GitHub stars](https://img.shields.io/github/stars/CLIP-HPC/goslmailer?style=flat)](https://github.com/CLIP-HPC/goslmailer/stargazers) - Goslmailer is a drop-in notification delivery solution for slurm that can do slack, mattermost, teams, and more.

## Performance
- [TotalView](https://totalview.io/products/totalview) - TotalView is a debugging tool for HPC applications `Proprietary`.
- [Tau](https://www.cs.uoregon.edu/research/tau/home.php) - TAU Performance System® is a portable profiling and tracing toolkit for performance analysis of parallel programs written in Fortran, C, C++, UPC, Java, Python `other`.
- [Valgrind](https://www.valgrind.org/) - Valgrind is a tool designed to profile programs to determine memory leaks ([Source Code](https://sourceware.org/git/?p=valgrind.git)) `GPL-2`.
- [Paraver](https://tools.bsc.es/paraver) - Paraver is a very flexible data browser that is part of the CEPBA-Tools toolkit `other`.
- [PAPI](http://icl.cs.utk.edu/papi) - Performance Application Programming Interface (PAPI) is a performance analysis tool ([Source Code](https://bitbucket.org/icl/papi/src/master/)) `other`.

## Parallel Shells
- [pdsh](https://linux.die.net/man/1/pdsh) - pdsh runs terminal commands across multiple hosts in parallel ([Source Code](https://github.com/chaos/pdsh) [![GitHub stars](https://img.shields.io/github/stars/chaos/pdsh?style=flat)](https://github.com/chaos/pdsh/stargazers)) `GPL-2`.
- [ClusterShell](https://clustershell.readthedocs.io/en/latest/intro.html) - Scalable cluster administration Python framework ([Source Code](https://github.com/cea-hpc/clustershell) [![GitHub stars](https://img.shields.io/github/stars/cea-hpc/clustershell?style=flat)](https://github.com/cea-hpc/clustershell/stargazers)) `LGPL-2.1` .

## Containers
- [Apptainer](https://apptainer.org) - Apptainer is an open source container system ([Source Code](https://github.com/apptainer/apptainer) [![GitHub stars](https://img.shields.io/github/stars/apptainer/apptainer?style=flat)](https://github.com/apptainer/apptainer/stargazers)) `BSD`.
- [Charliecloud](https://hpc.github.io/charliecloud/) - Charliecloud provides user-defined software stacks (UDSS) for high-performance computing (HPC) centers ([Source Code](https://github.com/hpc/charliecloud) [![GitHub stars](https://img.shields.io/github/stars/hpc/charliecloud?style=flat)](https://github.com/hpc/charliecloud/stargazers)) `Apache-2.0`.
- [Docker](https://www.docker.com/) - Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers `other`.
- [uDocker](https://indigo-dc.github.io/udocker/) - A basic user tool to execute simple docker containers in batch or interactive systems without root privileges ([Source Code](https://github.com/indigo-dc/udocker) [![GitHub stars](https://img.shields.io/github/stars/indigo-dc/udocker?style=flat)](https://github.com/indigo-dc/udocker/stargazers)) `Apache-2.0`.
- [Shifter](https://www.nersc.gov/research-and-development/user-defined-images/) -  Shifter is Linux containers for HPC ([Source Code](https://github.com/NERSC/shifter) [![GitHub stars](https://img.shields.io/github/stars/NERSC/shifter?style=flat)](https://github.com/NERSC/shifter/stargazers)) `other`.
- [HPC Container Maker](https://github.com/NVIDIA/hpc-container-maker) [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/hpc-container-maker?style=flat)](https://github.com/NVIDIA/hpc-container-maker/stargazers) - HPC Container Maker is an open source tool to make it easier to generate container specification files. `Apache-2.0`.
- [Scarus](https://github.com/eth-cscs/sarus) [![GitHub stars](https://img.shields.io/github/stars/eth-cscs/sarus?style=flat)](https://github.com/eth-cscs/sarus/stargazers) - An OCI-compatible container engine for HPC `BSD`.
- [Singularity HPC](https://singularity-hpc.readthedocs.io) - Singularity Registry HPC (shpc) allows you to install containers as modules ([Source Code](https://github.com/singularityhub/singularity-hpc) [![GitHub stars](https://img.shields.io/github/stars/singularityhub/singularity-hpc?style=flat)](https://github.com/singularityhub/singularity-hpc/stargazers)) `MPL 2.0`.

## Environment Management
- [Lmod](https://lmod.readthedocs.io/en/latest/) - Lmod: An Environment Module System based on Lua, Reads TCL Modules, Supports a Software Hierarchy ([Source Code](https://github.com/TACC/Lmod) [![GitHub stars](https://img.shields.io/github/stars/TACC/Lmod?style=flat)](https://github.com/TACC/Lmod/stargazers)) `other`.
- [Environment Modules](https://modules.readthedocs.io/en/latest/) - Environment Modules: provides dynamic modification of a user's environment  ([Source Code](https://github.com/cea-hpc/modules) [![GitHub stars](https://img.shields.io/github/stars/cea-hpc/modules?style=flat)](https://github.com/cea-hpc/modules/stargazers)) `GPL-2`.
- [Anaconda](https://www.anaconda.com/) - Anaconda is a Python and R distribution for use in computational science `other`.
- [Mamba](https://mamba.readthedocs.io/en/latest/) - Mamba is a reimplementation of the conda package manager in C++ ([Source Code](https://github.com/mamba-org/mamba) [![GitHub stars](https://img.shields.io/github/stars/mamba-org/mamba?style=flat)](https://github.com/mamba-org/mamba/stargazers)) `BSD`.

## Visualization
- [Visit](https://visit-dav.github.io/visit-website/) - VisIt - Visualization and Data Analysis for Mesh-based Scientific Data ([Source Code](https://github.com/visit-dav/visit) [![GitHub stars](https://img.shields.io/github/stars/visit-dav/visit?style=flat)](https://github.com/visit-dav/visit/stargazers)) `BSD-3`.
- [Paraview](https://www.paraview.org/) - ParaView is an open-source, multi-platform data analysis and visualization application based on Visualization Toolkit (VTK) ([Source Code](https://github.com/Kitware/ParaView) [![GitHub stars](https://img.shields.io/github/stars/Kitware/ParaView?style=flat)](https://github.com/Kitware/ParaView/stargazers)) `BSD-3`.

## Parallel Filesystems
- [GPFS](https://www.ibm.com/docs/en/gpfs/4.1.0.4?topic=guide-introducing-general-parallel-file-system) - GPFS is a high-performance clustered file system software developed by IBM `Proprietary`.
- [Quobyte](https://www.quobyte.com/storage-for/high-performance-computing-hpc?gclid=EAIaIQobChMI-fv1pfKG8wIV5x6tBh367Q5CEAAYASABEgJTgPD_BwE) - A high performance filesystem `Proprietary`.
- [Ceph](https://ceph.io/en/) - Ceph is a distributed object, block, and file storage platform ([Source Code](https://github.com/ceph/ceph) [![GitHub stars](https://img.shields.io/github/stars/ceph/ceph?style=flat)](https://github.com/ceph/ceph/stargazers)) `other`.
- [Weka](https://www.weka.io/) - A file system designed for HPC `Proprietary` .
- [Lustre/Exascaler](https://www.lustre.org/) - Lustre is an open-source, distributed parallel file system software platform designed for scalability, high-performance, and high-availability ([Source Code](https://git.whamcloud.com/fs/lustre-release.git)) `other`.
- [BeeGFS](https://www.beegfs.io/c/) - BeeGFS is a hardware-independent POSIX parallel file system developed with a strong focus on performance and designed for ease of use, simple installation, and management `Proprietary`.
- [OrangeFS](http://www.orangefs.org/) - OrangeFS is a next generation parallel file system for Linux clusters ([Source Code](https://github.com/waltligon/orangefs) [![GitHub stars](https://img.shields.io/github/stars/waltligon/orangefs?style=flat)](https://github.com/waltligon/orangefs/stargazers)) `other`.
- [MooseFS](https://moosefs.com/) - Moose File System is an Open-source, POSIX-compliant distributed file system developed by Core Technology ([Source Code](https://github.com/moosefs/moosefs) [![GitHub stars](https://img.shields.io/github/stars/moosefs/moosefs?style=flat)](https://github.com/moosefs/moosefs/stargazers)) `GPL-2.0`.

## Programming Languages
- [Julia](https://julialang.org/) - Julia is a high-level, high-performance dynamic language for technical computing `MIT`.
- [Futhark](https://futhark-lang.org/) - Futhark is a purely functional data-parallel programming language in the ML family `isc`.
- [Chapel](https://chapel-lang.org/) - Chapel is a programming language designed for productive parallel computing at scale `Apache-2.0`.

## Monitoring
### Prometheus Based
- [Slurm Exporter](https://github.com/treydock/prometheus-slurm-exporter) [![GitHub stars](https://img.shields.io/github/stars/treydock/prometheus-slurm-exporter?style=flat)](https://github.com/treydock/prometheus-slurm-exporter/stargazers) - Prometheus exporter for performance metrics from Slurm `GPL-3.0`. 
- [Slurm Exporter](https://github.com/ubccr/slurm-exporter) [![GitHub stars](https://img.shields.io/github/stars/ubccr/slurm-exporter?style=flat)](https://github.com/ubccr/slurm-exporter/stargazers) - Slurm Exporter for Prometheus using Rest API `GPL-3.0`.
- [Infiniband Exporter](https://github.com/treydock/infiniband_exporter) [![GitHub stars](https://img.shields.io/github/stars/treydock/infiniband_exporter?style=flat)](https://github.com/treydock/infiniband_exporter/stargazers) - The InfiniBand exporter collects counters from InfiniBand switches and HCAs `Apache-2.0`.
- [Cgroup Exporter](https://github.com/treydock/cgroup_exporter) [![GitHub stars](https://img.shields.io/github/stars/treydock/cgroup_exporter?style=flat)](https://github.com/treydock/cgroup_exporter/stargazers) - Produces metrics from cgroups `Apache-2.0`.
- [Cgroup Exporter](https://github.com/phpHavok/cgroups_exporter) [![GitHub stars](https://img.shields.io/github/stars/phpHavok/cgroups_exporter?style=flat)](https://github.com/phpHavok/cgroups_exporter/stargazers) - A Prometheus exporter for cgroup-level metrics `unknown`.
- [GPFS Exporter](https://github.com/treydock/gpfs_exporter) [![GitHub stars](https://img.shields.io/github/stars/treydock/gpfs_exporter?style=flat)](https://github.com/treydock/gpfs_exporter/stargazers) - The GPFS exporter collects metrics from the GPFS filesystem `Apache-2.0`.
- [Lustre Exporter](https://github.com/GSI-HPC/lustre_exporter) [![GitHub stars](https://img.shields.io/github/stars/GSI-HPC/lustre_exporter?style=flat)](https://github.com/GSI-HPC/lustre_exporter/stargazers) - Prometheus exporter for use with the Lustre parallel filesystem `GPL-3.0`.
- [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) [![GitHub stars](https://img.shields.io/github/stars/NVIDIA/dcgm-exporter?style=flat)](https://github.com/NVIDIA/dcgm-exporter/stargazers) - NVIDIA GPU metrics exporter for Prometheus leveraging DCGM `Apache-2.0`.

## Journals
- [Journal of Super Computing](https://www.springer.com/journal/11227) - An International Journal of High-Performance Computer Design, Analysis, and Use.

## Podcasts
- [This week in HPC](https://www.intersect360.com/media/podcasts/) - Each week, Intersect360 Research CEO Addison Snell and HPCwire editor Tiffany Trader dissect the week's top HPC stories. 
- [Exascaler Project](https://www.exascaleproject.org/podcast/) - ECP's Let's Talk Exascale podcast goes behind the scenes to chat with some of the people who are bringing a capable and sustainable exascale computing ecosystem to fruition.
- [@HPCpodcast](https://insidehpc.com/category/resources/hpc-podcast/) - Join Shahin Khan and Doug Black as they discuss Supercomputing technologies and the applications, markets, and policies that shape them.


## Blogs
- [HPCWire](https://www.hpcwire.com/) - Since 1987 covering the fastest computers in the world and the people who run them.
- [InsideHPC](https://insidehpc.com/) - insideHPC is a global publication recognized for its comprehensive and insightful coverage of the HPC-AI community, linking vendors, end-users and HPC strategists. 
- [The Next Platform](https://www.nextplatform.com/category/hpc/) - Offers in-depth coverage of high-end computing at large enterprises, supercomputing centers, hyperscale data centers, and public clouds.
- [The Register HPC](http://www.theregister.co.uk/data_centre/hpc/) - The Register is a leading and trusted global online enterprise technology news publication, reaching roughly 40 million readers worldwide.
- [HPC at Dell](http://hpcatdell.com) - High-Performance Computing knowledge base articles from Dell.

## Conferences

- [Pearc](https://pearc.acm.org/) - Practice & Experience in Advanced Research Computing.
- [Supercomputing (SC)](https://supercomputing.org/) - The International Conference for High Performance Computing, Networking, Storage, and Analysis.
- [Supercomputing International (ISC)](https://www.isc-hpc.com/) - The International Conference for High Performance Computing, Networking, Storage, and Analysis.
- [CCGrid](https://dl.acm.org/conference/ccgrid) - IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing.
- [IEEE-HPEC](https://ieee-hpec.org/) - IEEE High Performance Embedded Computing.
- [Hot Chips](https://hotchips.org) - Semiconductor industry's leading conference on high-performance microprocessors and related circuits.
- [Hot Interconnects](https://hoti.org) - IEEE conference on software architectures and implementations for interconnection networks of all scales.
- [ESSA](https://sites.google.com/view/essa-2024/) - Workshop on Extreme-Scale Storage and Analysis.
- [IEEE-IPDPS](https://www.ipdps.org/) - IEEE International Parallel & Distributed Processing Symposium.
- [ESPM2 Workshop](http://nowlab.cse.ohio-state.edu/espm2/) - International Workshop on Extreme Scale Programming Models and Middleware.
- [LCI Workshops](https://linuxclustersinstitute.org/workshops/) - The Linux Clusters Institute (LCI) is providing education and advanced technical training for the deployment and use of computing clusters to the high performance computing community worldwide.
- [HPC Carpentry](https://www.hpc-carpentry.org/) - Teaching basic skills for high-performance computing.

## Websites

- [Top500](https://top500.org) - The TOP500 project ranks and details the 500 most powerful non-distributed computer systems in the world.

## User Groups
- [MVAPICH](https://mug.mvapich.cse.ohio-state.edu/) - The MUG conference provides an open forum for all attendees (users, system administrators, researchers, engineers, and students) to discuss and share their knowledge on using MVAPICH libraries.
- [Slurm](https://slurm.schedmd.com/slurm_ug_agenda.html) - The annual Slurm user group meeting.

## Contributing

Contributing guidelines can be found in [contributing.md](contributing.md).
