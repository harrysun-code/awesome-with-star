# Scientific Computing

[![GitHub stars](https://img.shields.io/github/stars/nschloe/awesome-scientific-computing?style=flat)](https://github.com/nschloe/awesome-scientific-computing/stargazers)

# Awesome Scientific Computing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://nschloe.github.io/awesome-scientific-computing/sunglasses.svg" align="right" width="30%">](#readme)

> Useful resources for scientific computing and numerical analysis.

Scientific computing and numerical analysis are research fields that aim to provide
methods for solving large-scale problems from various areas of science with the help of
computers. Typical problems are ordinary and partial differential equations (ODEs,
PDEs), their discretizations, and the solution of linear algebra problems arising from
them.

## Contents

- [Basic linear algebra](#basic-linear-algebra)
- [Multi-purpose toolkits](#multi-purpose-toolkits)
- [Finite Elements](#finite-elements)
- [Meshing](#meshing)
- [Data formats](#data-formats)
- [Sparse linear solvers](#sparse-linear-solvers)
- [Visualization](#visualization)
- [Other libraries and tools](#other-libraries-and-tools)
- [Community](#community)

## Basic linear algebra

- [BLAS](https://netlib.org/blas/) - Standard building blocks for performing basic vector and matrix operations.
  (Fortran, public domain, [GitHub](https://github.com/Reference-LAPACK/lapack/tree/master/BLAS) [![GitHub stars](https://img.shields.io/github/stars/Reference-LAPACK/lapack/tree/master/BLAS?style=flat)](https://github.com/Reference-LAPACK/lapack/tree/master/BLAS/stargazers))
- [OpenBLAS](https://www.openblas.net) - Optimized BLAS library based on GotoBLAS2.
  (C and Assembly, BSD, [GitHub](https://github.com/OpenMathLib/OpenBLAS) [![GitHub stars](https://img.shields.io/github/stars/OpenMathLib/OpenBLAS?style=flat)](https://github.com/OpenMathLib/OpenBLAS/stargazers))
- [BLIS](https://github.com/flame/blis) [![GitHub stars](https://img.shields.io/github/stars/flame/blis?style=flat)](https://github.com/flame/blis/stargazers) - High-performance BLAS-like dense linear algebra libraries.
  (C, BSD, GitHub)
- [LAPACK](https://netlib.org/lapack/) - Routines for solving systems of linear equations, linear least-squares, eigenvalue problems, etc.
  (Fortran, BSD, [GitHub](https://github.com/Reference-LAPACK/lapack) [![GitHub stars](https://img.shields.io/github/stars/Reference-LAPACK/lapack?style=flat)](https://github.com/Reference-LAPACK/lapack/stargazers))
- [Eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) - C++ template library for linear algebra.
  (C++, MPL 2, [GitLab](https://gitlab.com/libeigen/eigen))
- [Ginkgo](https://ginkgo-project.github.io/) - High-performance manycore linear algebra library, focus on sparse systems.
  (C++, BSD, [GitHub](https://github.com/ginkgo-project/ginkgo) [![GitHub stars](https://img.shields.io/github/stars/ginkgo-project/ginkgo?style=flat)](https://github.com/ginkgo-project/ginkgo/stargazers))
- [blaze](https://bitbucket.org/blaze-lib/blaze) - High-performance C++ math library for dense and sparse arithmetic.
  (C++, BSD, Bitbucket)

## Multi-purpose toolkits

- [PETSc](https://petsc.org/release/) - Parallel solution of scientific applications modeled by PDEs.
  (C, 2-clause BSD, [GitLab](https://gitlab.com/petsc/petsc))
- [DUNE Numerics](https://www.dune-project.org) - Toolbox for solving PDEs with grid-based methods.
  (C++, GPL 2, [GitLab](https://gitlab.dune-project.org/core/))
- [SciPy](https://scipy.org) - Python modules for statistics, optimization, integration, linear algebra, etc.
  (Python, mostly BSD, [GitHub](https://github.com/scipy/scipy/) [![GitHub stars](https://img.shields.io/github/stars/scipy/scipy/?style=flat)](https://github.com/scipy/scipy//stargazers))
- [NumPy](https://numpy.org/) - Fundamental package needed for scientific computing with Python.
  (Python, BSD, [GitHub](https://github.com/numpy/numpy) [![GitHub stars](https://img.shields.io/github/stars/numpy/numpy?style=flat)](https://github.com/numpy/numpy/stargazers))
- [DifferentialEquations.jl](https://docs.sciml.ai/DiffEqDocs/stable/) - Toolbox for solving different types of differential equations numerically. (Julia, MIT, [GitHub](https://github.com/SciML/DifferentialEquations.jl) [![GitHub stars](https://img.shields.io/github/stars/SciML/DifferentialEquations.jl?style=flat)](https://github.com/SciML/DifferentialEquations.jl/stargazers))

## Finite Elements

- [FEniCS](https://fenicsproject.org) - Computing platform for solving PDEs in Python and C++.
  (C++/Python, LGPL 3, [GitHub](https://github.com/FEniCS) [![GitHub stars](https://img.shields.io/github/stars/FEniCS?style=flat)](https://github.com/FEniCS/stargazers)/[Bitbucket](https://bitbucket.org/fenics-project/))
- [libMesh](https://libmesh.github.io) - Framework for the numerical simulation of PDEs using unstructured discretizations.
  (C++, LGPL 2.1, [GitHub](https://github.com/libMesh/libmesh) [![GitHub stars](https://img.shields.io/github/stars/libMesh/libmesh?style=flat)](https://github.com/libMesh/libmesh/stargazers))
- [deal.II](https://dealii.org) - Software library supporting the creation of finite element codes.
  (C++, LGPL 2.1, [GitHub](https://github.com/dealii/dealii) [![GitHub stars](https://img.shields.io/github/stars/dealii/dealii?style=flat)](https://github.com/dealii/dealii/stargazers))
- [Netgen/NGSolve](https://ngsolve.org) - High performance multiphysics finite element software.
  (C++, LGPL 2.1, [GitHub](https://github.com/NGSolve/netgen) [![GitHub stars](https://img.shields.io/github/stars/NGSolve/netgen?style=flat)](https://github.com/NGSolve/netgen/stargazers))
- [Firedrake](https://www.firedrakeproject.org) - Automated system for the solution of PDEs using the finite element method.
  (Python, LGPL 3, [GitHub](https://github.com/firedrakeproject/firedrake) [![GitHub stars](https://img.shields.io/github/stars/firedrakeproject/firedrake?style=flat)](https://github.com/firedrakeproject/firedrake/stargazers))
- [MOOSE](https://mooseframework.inl.gov/) - Multiphysics Object Oriented Simulation Environment.
  (C++, LGPL 2.1, [GitHub](https://github.com/idaholab/moose) [![GitHub stars](https://img.shields.io/github/stars/idaholab/moose?style=flat)](https://github.com/idaholab/moose/stargazers))
- [MFEM](https://mfem.org) - Free, lightweight, scalable C++ library for finite element methods.
  (C++, BSD-3-Clause, [GitHub](https://github.com/mfem/mfem) [![GitHub stars](https://img.shields.io/github/stars/mfem/mfem?style=flat)](https://github.com/mfem/mfem/stargazers))
- [SfePy](https://sfepy.org) - Simple Finite Elements in Python.
  (Python, BSD, [GitHub](https://github.com/sfepy/sfepy) [![GitHub stars](https://img.shields.io/github/stars/sfepy/sfepy?style=flat)](https://github.com/sfepy/sfepy/stargazers))
- [FreeFEM](https://freefem.org) - High level multiphysics-multimesh finite element language.
  (C++, LGPL, [GitHub](https://github.com/FreeFem) [![GitHub stars](https://img.shields.io/github/stars/FreeFem?style=flat)](https://github.com/FreeFem/stargazers))
- [libceed](https://libceed.readthedocs.io/en/latest/index.html) - Code for Efficient Extensible Discretizations.
  (C, 2-clause BSD, [GitHub](https://github.com/CEED/libCEED) [![GitHub stars](https://img.shields.io/github/stars/CEED/libCEED?style=flat)](https://github.com/CEED/libCEED/stargazers))
- [scikit-fem](https://github.com/kinnala/scikit-fem) [![GitHub stars](https://img.shields.io/github/stars/kinnala/scikit-fem?style=flat)](https://github.com/kinnala/scikit-fem/stargazers) - Simple finite element assemblers.
  (Python, BSD/GPL, GitHub)

## Meshing

### Triangular and tetrahedral meshing

- [Gmsh](https://gmsh.info) - Three-dimensional finite element mesh generator with pre- and post-processing facilities.
  (C++, GPL, [GitLab](https://gitlab.onelab.info/gmsh/gmsh))
- [pygmsh](https://github.com/nschloe/pygmsh) [![GitHub stars](https://img.shields.io/github/stars/nschloe/pygmsh?style=flat)](https://github.com/nschloe/pygmsh/stargazers) - Python interface for Gmsh.
  (Python, GPL 3, GitHub)
- [MeshPy](https://mathema.tician.de/software/meshpy/) - Quality triangular and tetrahedral mesh generation.
  (Python, MIT, [GitHub](https://github.com/inducer/meshpy) [![GitHub stars](https://img.shields.io/github/stars/inducer/meshpy?style=flat)](https://github.com/inducer/meshpy/stargazers))
- [CGAL](https://www.cgal.org) - Algorithms for computational geometry.
  (C++, mixed LGPL/GPL, [GitHub](https://github.com/CGAL/cgal) [![GitHub stars](https://img.shields.io/github/stars/CGAL/cgal?style=flat)](https://github.com/CGAL/cgal/stargazers))
- [pygalmesh](https://github.com/meshpro/pygalmesh) [![GitHub stars](https://img.shields.io/github/stars/meshpro/pygalmesh?style=flat)](https://github.com/meshpro/pygalmesh/stargazers) - Python interface for CGAL's 3D meshing capabilities.
  (Python, GPL 3, GitHub)
- [TetGen](https://www.wias-berlin.de/software/index.jsp?id=TetGen) - Quality tetrahedral mesh generator and 3D Delaunay triangulator.
  (C++, AGPLv3)
- [Triangle](https://www.cs.cmu.edu/~quake/triangle.html) - Two-dimensional quality mesh generator and Delaunay triangulator.
  (C, _nonfree software_)
- [distmesh](https://persson.berkeley.edu/distmesh/) - Simple generator for unstructured triangular and tetrahedral meshes.
  (MATLAB, GPL 3)
- [trimesh](https://trimesh.org) - Loading and using triangular meshes with an emphasis on watertight surfaces.
  (Python, MIT, [GitHub](https://github.com/mikedh/trimesh) [![GitHub stars](https://img.shields.io/github/stars/mikedh/trimesh?style=flat)](https://github.com/mikedh/trimesh/stargazers))
- [dmsh](https://github.com/meshpro/dmsh) [![GitHub stars](https://img.shields.io/github/stars/meshpro/dmsh?style=flat)](https://github.com/meshpro/dmsh/stargazers) - Simple generator for unstructured triangular meshes, inspired by distmesh.
  (Python, proprietary, GitHub)
- [TetWild](https://arxiv.org/abs/1908.03581) - Generate tetrahedral meshes for triangular surface meshes.
  (C++, GPL 3, [GitHub](https://github.com/Yixin-Hu/TetWild) [![GitHub stars](https://img.shields.io/github/stars/Yixin-Hu/TetWild?style=flat)](https://github.com/Yixin-Hu/TetWild/stargazers))
- [TriWild](https://cims.nyu.edu/gcl/papers/2019-TriWild.pdf) - Robust triangulation with curve constraints.
  (C++, MPL 2, [GitHub](https://github.com/wildmeshing/TriWild) [![GitHub stars](https://img.shields.io/github/stars/wildmeshing/TriWild?style=flat)](https://github.com/wildmeshing/TriWild/stargazers))
- [fTetWild](https://arxiv.org/abs/1908.03581) - Same as TetWild, but faster.
  (C++, MPL 2, [GitHub](https://github.com/wildmeshing/fTetWild) [![GitHub stars](https://img.shields.io/github/stars/wildmeshing/fTetWild?style=flat)](https://github.com/wildmeshing/fTetWild/stargazers))
- [SeismicMesh](https://github.com/krober10nd/SeismicMesh) [![GitHub stars](https://img.shields.io/github/stars/krober10nd/SeismicMesh?style=flat)](https://github.com/krober10nd/SeismicMesh/stargazers) - Parallel 2D/3D triangle/tetrahedral mesh generation with sliver removal.
  (Python and C++, GPL 3, GitHub)

### Quadrilateral and hexahedral meshing

- [QuadriFlow](https://stanford.edu/~jingweih/papers/quadriflow/) - Scalable and robust quadrangulation from triangulation.
  (C++, BSD, [GitHub](https://github.com/hjwdzh/QuadriFlow) [![GitHub stars](https://img.shields.io/github/stars/hjwdzh/QuadriFlow?style=flat)](https://github.com/hjwdzh/QuadriFlow/stargazers))

### Mesh tools

- [meshio](https://github.com/nschloe/meshio) [![GitHub stars](https://img.shields.io/github/stars/nschloe/meshio?style=flat)](https://github.com/nschloe/meshio/stargazers) - I/O for various mesh formats, file conversion.
  (Python, MIT, GitHub)
- [MOAB](https://sigma.mcs.anl.gov/moab-library/) - Representing and evaluating mesh data.
  (C++, mostly LGPL 3, [Bitbucket](https://bitbucket.org/fathomteam/moab/))
- [optimesh](https://github.com/meshpro/optimesh) [![GitHub stars](https://img.shields.io/github/stars/meshpro/optimesh?style=flat)](https://github.com/meshpro/optimesh/stargazers) - Triangular mesh smoothing.
  (Python, proprietary, GitHub)
- [pmp-library](https://www.pmp-library.org/) - Polygon mesh processing library.
  (C++, MIT with Employer Disclaimer, [GitHub](https://github.com/pmp-library/pmp-library/) [![GitHub stars](https://img.shields.io/github/stars/pmp-library/pmp-library/?style=flat)](https://github.com/pmp-library/pmp-library//stargazers))
- [Mmg](https://www.mmgtools.org/) - Robust, open-source & multidisciplinary software for remeshing.
  (C, LGPL 3, [GitHub](https://github.com/MmgTools/mmg) [![GitHub stars](https://img.shields.io/github/stars/MmgTools/mmg?style=flat)](https://github.com/MmgTools/mmg/stargazers))
- [meshplex](https://github.com/meshpro/meshplex) [![GitHub stars](https://img.shields.io/github/stars/meshpro/meshplex?style=flat)](https://github.com/meshpro/meshplex/stargazers) - Fast tools for simplex meshes.
  (Python, proprietary, GitHub)

## Data formats

- [NetCDF](https://www.unidata.ucar.edu/software/netcdf) - Software libraries and data formats for array-oriented scientific data.
  (C/C++/Fortran/Java/Python, [custom open-source
  license](https://www.unidata.ucar.edu/software/netcdf/licensing),
  [GitHub](https://github.com/Unidata/netcdf-c/) [![GitHub stars](https://img.shields.io/github/stars/Unidata/netcdf-c/?style=flat)](https://github.com/Unidata/netcdf-c//stargazers))
- [HDF5](https://www.hdfgroup.org/solutions/hdf5/) - Data model, library, and file format for storing and managing data.
  (C/Fortran, BSD, [GitHub](https://github.com/HDFGroup/hdf5) [![GitHub stars](https://img.shields.io/github/stars/HDFGroup/hdf5?style=flat)](https://github.com/HDFGroup/hdf5/stargazers))
- [XDMF](https://xdmf.org/) - eXtensible Data Model and Format for data from High Performance Computing codes.
  (C++, [GitLab](https://gitlab.kitware.com/xdmf/xdmf))
- [Zarr](https://zarr.readthedocs.io/en/stable/) - Format for the storage of chunked, compressed, N-dimensional arrays.
  (Python, MIT, [GitHub](https://github.com/zarr-developers/zarr-python) [![GitHub stars](https://img.shields.io/github/stars/zarr-developers/zarr-python?style=flat)](https://github.com/zarr-developers/zarr-python/stargazers))

## Sparse linear solvers

- [SuperLU](https://portal.nersc.gov/project/sparse/superlu/) - Direct solution of large, sparse, nonsymmetric systems of linear equations.
  (C, mostly BSD, [GitHub](https://github.com/xiaoyeli/superlu) [![GitHub stars](https://img.shields.io/github/stars/xiaoyeli/superlu?style=flat)](https://github.com/xiaoyeli/superlu/stargazers))
- [PyAMG](https://pyamg.readthedocs.io/en/latest/) - Algebraic Multigrid Solvers in Python.
  (Python, MIT, [GitHub](https://github.com/pyamg/pyamg) [![GitHub stars](https://img.shields.io/github/stars/pyamg/pyamg?style=flat)](https://github.com/pyamg/pyamg/stargazers))
- [hypre](https://computing.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods) - Library of high-performance preconditioners and solvers.
  (C, Apache 2.0/MIT, [GitHub](https://github.com/hypre-space/hypre) [![GitHub stars](https://img.shields.io/github/stars/hypre-space/hypre?style=flat)](https://github.com/hypre-space/hypre/stargazers))

## Visualization

- [ParaView](https://www.paraview.org) - Multi-platform data analysis and visualization application based on VTK.
  (C++, BSD, [GitLab](https://gitlab.kitware.com/paraview/paraview))
- [VTK](https://vtk.org/) - Process images and create 3D computer graphics.
  (C++, BSD, [GitLab](https://gitlab.kitware.com/vtk/vtk))
- [Mayavi](https://docs.enthought.com/mayavi/mayavi/) - 3D scientific data visualization and plotting in Python.
  (Python, BSD, [GitHub](https://github.com/enthought/mayavi) [![GitHub stars](https://img.shields.io/github/stars/enthought/mayavi?style=flat)](https://github.com/enthought/mayavi/stargazers))
- [Polyscope](https://polyscope.run/) - Viewer and user interface for 3D geometry processing.
  (C++, MIT, [GitHub](https://github.com/nmwsharp/polyscope) [![GitHub stars](https://img.shields.io/github/stars/nmwsharp/polyscope?style=flat)](https://github.com/nmwsharp/polyscope/stargazers))
- [PyVista](https://docs.pyvista.org/) - 3D plotting and mesh analysis through a streamlined interface for VTK.
  (Python, MIT, [GitHub](https://github.com/pyvista/pyvista) [![GitHub stars](https://img.shields.io/github/stars/pyvista/pyvista?style=flat)](https://github.com/pyvista/pyvista/stargazers))
- [vedo](https://vedo.embl.es) - Library for scientific analysis and visualization of 3D objects based on VTK.
  (Python, MIT, [GitHub](https://github.com/marcomusy/vedo) [![GitHub stars](https://img.shields.io/github/stars/marcomusy/vedo?style=flat)](https://github.com/marcomusy/vedo/stargazers))
- [yt](https://yt-project.org/) - Toolkit for analysis and visualization of volumetric data.
  (Python, BSD, [GitHub](https://github.com/yt-project/yt) [![GitHub stars](https://img.shields.io/github/stars/yt-project/yt?style=flat)](https://github.com/yt-project/yt/stargazers))
- [F3D](https://f3d.app/) - Cross-platform, fast, and minimalist 3D viewer with scientific visualization tools.
  (C++, BSD, [GitHub](https://github.com/f3d-app/f3d) [![GitHub stars](https://img.shields.io/github/stars/f3d-app/f3d?style=flat)](https://github.com/f3d-app/f3d/stargazers))
- [TTK](https://topology-tool-kit.github.io/) - Topological data analysis and visualization.
  (C++/Python, BSD, [GitHub](https://github.com/topology-tool-kit/ttk) [![GitHub stars](https://img.shields.io/github/stars/topology-tool-kit/ttk?style=flat)](https://github.com/topology-tool-kit/ttk/stargazers))
- [morphologica](https://github.com/ABRG-Models/morphologica) [![GitHub stars](https://img.shields.io/github/stars/ABRG-Models/morphologica?style=flat)](https://github.com/ABRG-Models/morphologica/stargazers) - Header-only, modern OpenGL code to visualize numerical simulations at runtime. (C++, Apache 2.0, GitHub)

## Other libraries and tools

- [FFTW](http://www.fftw.org) - Discrete Fourier transforms in one or more dimensions, of arbitrary input size, real and complex.
  (C, GPL2, [GitHub](https://github.com/FFTW/fftw3) [![GitHub stars](https://img.shields.io/github/stars/FFTW/fftw3?style=flat)](https://github.com/FFTW/fftw3/stargazers))
- [Qhull](http://www.qhull.org) - Convex hull, Delaunay triangulation, Voronoi diagram, halfspace intersection about a point, etc.
  (C/C++, [custom open source license](http://www.qhull.org/COPYING.txt),
  [GitHub](https://github.com/qhull/qhull/) [![GitHub stars](https://img.shields.io/github/stars/qhull/qhull/?style=flat)](https://github.com/qhull/qhull//stargazers))
- [GSL](https://www.gnu.org/software/gsl/) - Random number generators, special functions, and least-squares fitting etc.
  (C/C++, GPL 3, [Savannah](https://savannah.gnu.org/projects/gsl))
- [OpenFOAM](https://www.openfoam.com) - Free, open source CFD (computational fluid dynamics) software.
  (C++, GPL 3, [GitHub](https://github.com/OpenFOAM/OpenFOAM-dev) [![GitHub stars](https://img.shields.io/github/stars/OpenFOAM/OpenFOAM-dev?style=flat)](https://github.com/OpenFOAM/OpenFOAM-dev/stargazers))
- [quadpy](https://github.com/sigma-py/quadpy) [![GitHub stars](https://img.shields.io/github/stars/sigma-py/quadpy?style=flat)](https://github.com/sigma-py/quadpy/stargazers) - Numerical integration (quadrature, cubature) in Python.
  (Python, proprietary, GitHub)
- [FiPy](https://www.ctcms.nist.gov/fipy/) - Finite-volume PDE solver.
  (Python, [custom open-source
  license](https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications),
  [GitHub](https://github.com/usnistgov/fipy) [![GitHub stars](https://img.shields.io/github/stars/usnistgov/fipy?style=flat)](https://github.com/usnistgov/fipy/stargazers))
- [accupy](https://github.com/sigma-py/accupy) [![GitHub stars](https://img.shields.io/github/stars/sigma-py/accupy?style=flat)](https://github.com/sigma-py/accupy/stargazers) - Accurate sums and dot products for Python.
  (Python, GPL 3, GitHub)
- [SLEPc](https://slepc.upv.es) - Scalable Library for Eigenvalue Problem Computations.
  (C, 2-clause BSD, [GitLab](https://gitlab.com/slepc/slepc))
- [Chebfun](https://www.chebfun.org/) - Computing with functions to about 15-digit accuracy.
  (MATLAB, BSD, [GitHub](https://github.com/chebfun/chebfun) [![GitHub stars](https://img.shields.io/github/stars/chebfun/chebfun?style=flat)](https://github.com/chebfun/chebfun/stargazers))
- [pyMOR](https://pymor.org/) - Model Order Reduction with Python.
  (Python, 2-clause BSD, [GitHub](https://github.com/pymor/pymor/) [![GitHub stars](https://img.shields.io/github/stars/pymor/pymor/?style=flat)](https://github.com/pymor/pymor//stargazers))
- [cvxpy](https://www.cvxpy.org/) - Modeling language for convex optimization problems.
  (Python, Apache 2.0, [GitHub](https://github.com/cvxpy/cvxpy) [![GitHub stars](https://img.shields.io/github/stars/cvxpy/cvxpy?style=flat)](https://github.com/cvxpy/cvxpy/stargazers))
- [PyWavelets](https://pywavelets.readthedocs.io/en/latest/) - Wavelet transforms in Python.
  (Python, MIT, [GitHub](https://github.com/PyWavelets/pywt) [![GitHub stars](https://img.shields.io/github/stars/PyWavelets/pywt?style=flat)](https://github.com/PyWavelets/pywt/stargazers))
- [NFFT](https://www-user.tu-chemnitz.de/~potts/nfft/) - Nonequispaced fast Fourier transform.
  (C/MATLAB, GPL 2, [GitHub](https://github.com/NFFT/nfft) [![GitHub stars](https://img.shields.io/github/stars/NFFT/nfft?style=flat)](https://github.com/NFFT/nfft/stargazers))
- [preCICE](https://precice.org/) - Coupling library for partitioned multi-physics simulations (FSI, CHT, and more).
  (C++, LGPL 3, [GitHub](https://github.com/precice/) [![GitHub stars](https://img.shields.io/github/stars/precice/?style=flat)](https://github.com/precice//stargazers))
- [orthopy](https://github.com/sigma-py/orthopy) [![GitHub stars](https://img.shields.io/github/stars/sigma-py/orthopy?style=flat)](https://github.com/sigma-py/orthopy/stargazers) - Compute orthogonal polynomials efficiently.
  (Python, proprietary, GitHub)
- [pyGAM](https://pygam.readthedocs.io/en/latest/) - Generalized Additive Models in Python.
  (Python, Apache 2.0, [GitHub](https://github.com/dswah/pyGAM) [![GitHub stars](https://img.shields.io/github/stars/dswah/pyGAM?style=flat)](https://github.com/dswah/pyGAM/stargazers))
- [Dedalus](https://dedalus-project.org/) - Solve partial differential equations with spectral methods.
  (Python, GPL 3, [GitHub](https://github.com/DedalusProject/dedalus) [![GitHub stars](https://img.shields.io/github/stars/DedalusProject/dedalus?style=flat)](https://github.com/DedalusProject/dedalus/stargazers))
- [PyGMO](https://esa.github.io/pygmo/) - Massively parallel optimization.
  (Python/C++, MPL 2, [GitHub](https://github.com/esa/pygmo2) [![GitHub stars](https://img.shields.io/github/stars/esa/pygmo2?style=flat)](https://github.com/esa/pygmo2/stargazers))
- [shenfun](https://shenfun.readthedocs.io/en/latest/) - High-performance Python library for the spectral Galerkin method.
  (Python, BSD-2, [GitHub](https://github.com/spectralDNS/shenfun) [![GitHub stars](https://img.shields.io/github/stars/spectralDNS/shenfun?style=flat)](https://github.com/spectralDNS/shenfun/stargazers))
- [PyDMD](https://github.com/mathLab/PyDMD) [![GitHub stars](https://img.shields.io/github/stars/mathLab/PyDMD?style=flat)](https://github.com/mathLab/PyDMD/stargazers) - Dynamic Mode Decomposition (DMD) in Python.
  (Python, MIT, GitHub)
- [HPDDM](https://github.com/hpddm/hpddm) [![GitHub stars](https://img.shields.io/github/stars/hpddm/hpddm?style=flat)](https://github.com/hpddm/hpddm/stargazers) - High-performance unified framework for domain decomposition methods.
  (C++, LGPL 3, GitHub)

## Community

- [SciComp StackExchange](https://scicomp.stackexchange.com/) - Computational Science on the StackExchange network.
- [Wolfgang Bangerth's video class](https://www.math.colostate.edu/~bangerth/videos.html) - MATH 676: Finite element methods in scientific computing.
- [Nick Higham's blog](https://nhigham.com/) - Mostly on MATLAB, general computing advice.
- [Nick Trefethen's Video Lectures](https://people.maths.ox.ac.uk/trefethen/videos.html) - 36 video lectures on approximation theory/practice and scientific computing.
- [John D. Cook's blog](https://www.johndcook.com/blog/) - Feats of scientific computing.
- [Jack Dongarra's software list](https://netlib.org/utk/people/JackDongarra/la-sw.html) - List of freely available software for the solution of linear algebra problems.
- [NA Digest](https://netlib.org/na-digest-html/) - Collection of articles on topics related to numerical analysis and those who practice it.
- [Gabriel Peyré on Bluesky](https://bsky.app/profile/gabrielpeyre.bsky.social) - One post a day on computational mathematics.
- [Discord: Numerical Software](https://discord.com/invite/hnTJ5MRX2Y) - Discord messaging server on numerical software.
