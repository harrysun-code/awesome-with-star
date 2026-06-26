# Jupyter

[![GitHub stars](https://img.shields.io/github/stars/markusschanta/awesome-jupyter?style=flat)](https://github.com/markusschanta/awesome-jupyter/stargazers)

# Awesome Jupyter [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![HitCount](https://hits.dwyl.com/markusschanta/awesome-jupyter.svg?style=flat)](http://hits.dwyl.com/markusschanta/awesome-jupyter)

A curated list of awesome [Jupyter](http://jupyter.org) projects, libraries and resources. Jupyter is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.

<div align="center" style="border-bottom: 0px;">
	<br>
	<img width="400" src="assets/logo.png" alt="Jupyter logo">
	<br>
	<br>
</div>

---

<div align="center" style="border-bottom: 0px;">
	<sub>Awesome Jupyter is proudly supported by our sponsor:</sub>
	<br>
	<br>
	<a href="https://deepnote.com/?utm_source=github&utm_medium=promo&utm_campaign=awesomejupyter"><img width="300" src="assets/deepnote.jpeg" alt="Deepnote logo"></a>
	<br>
	<br>
	<b>Deepnote is a collaborative data science notebook built for teams.</b>
	<div>
	<sub>Explore data with Python & SQL from your browser. Add context with data visualizations and rich text editing. Share your work by simply sending a link. <a href="https://deepnote.com/?utm_source=github&utm_medium=promo&utm_campaign=awesomejupyter">Check it out on the Deepnote free plan.</a></sub>
	</div>
</div>

---

## Contents

<!--lint ignore awesome-toc alphabetize-lists-->
- [Runtimes/Frontends](#runtimesfrontends)
- [Collaboration/Education](#collaborationeducation)
- [Visualization](#visualization)
- [Tables](#Tables)
- [Rendering/Publishing/Conversion](#renderingpublishingconversion)
- [Version Control](#version-control)
- [JupyterLab Extensions](#jupyterlab-extensions)
- [Testing](#testing)
- [Domain-Specific Projects](#domain-specific-projects)
- [Hosted Notebook Solutions](#hosted-notebook-solutions)
- [Official Resources and Documentation](#official-resources-and-documentation)
- [Community Resources](#community-resources)
- [Articles/Guides/Tutorials](#articlesguidestutorials)
- [Contributing](#contributing)

<!--lint disable no-repeat-item-in-description-->

---

## Runtimes/Frontends

- [Beaker](http://beakerx.com/) - Development environment with seamless data transmission from one language to another.
- [docker-stacks](https://github.com/jupyter/docker-stacks) [![GitHub stars](https://img.shields.io/github/stars/jupyter/docker-stacks?style=flat)](https://github.com/jupyter/docker-stacks/stargazers) - Hierarchical stacks of ready-to-run Jupyter applications in Docker.
- [Guild AI](https://my.guild.ai/docs/jupyter-notebook-experiments/) - Execute notebooks as experiments to capture and compare results over time.
- [Hydrogen](https://github.com/nteract/hydrogen) [![GitHub stars](https://img.shields.io/github/stars/nteract/hydrogen?style=flat)](https://github.com/nteract/hydrogen/stargazers) - Run code inline in Atom using Jupyter kernels.
- [Jupyter Notebook](https://github.com/jupyter/notebook) [![GitHub stars](https://img.shields.io/github/stars/jupyter/notebook?style=flat)](https://github.com/jupyter/notebook/stargazers) - Main Jupyter notebook runtime.
- [JupyterHub](https://github.com/jupyterhub/jupyterhub) [![GitHub stars](https://img.shields.io/github/stars/jupyterhub/jupyterhub?style=flat)](https://github.com/jupyterhub/jupyterhub/stargazers) - Multi-user server for Jupyter.
- [JupyterLab](https://github.com/jupyterlab/jupyterlab) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab?style=flat)](https://github.com/jupyterlab/jupyterlab/stargazers) - JupyterLab is the next generation user interface for Jupyter.
- [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-desktop?style=flat)](https://github.com/jupyterlab/jupyterlab-desktop/stargazers) - A desktop application for JupyterLab, based on Electron.
- [JupyterWith](https://github.com/tweag/jupyterWith) [![GitHub stars](https://img.shields.io/github/stars/tweag/jupyterWith?style=flat)](https://github.com/tweag/jupyterWith/stargazers) - Nix-based framework for the definition of declarative and reproducible Jupyter environments.
- [kaggle/docker-python](https://github.com/kaggle/docker-python) [![GitHub stars](https://img.shields.io/github/stars/kaggle/docker-python?style=flat)](https://github.com/kaggle/docker-python/stargazers) - Kaggle Python Docker image that includes datasets and packages.
- [ML Workspace](https://github.com/ml-tooling/ml-workspace) [![GitHub stars](https://img.shields.io/github/stars/ml-tooling/ml-workspace?style=flat)](https://github.com/ml-tooling/ml-workspace/stargazers) - Docker image that includes Jupyter(Lab) and various packages for data science/machine learning.
- [nteract](https://github.com/nteract/nteract) [![GitHub stars](https://img.shields.io/github/stars/nteract/nteract?style=flat)](https://github.com/nteract/nteract/stargazers) - Native desktop notebook frontend. <!--lint disable double-link-->
- [Panel](https://github.com/holoviz/panel) [![GitHub stars](https://img.shields.io/github/stars/holoviz/panel?style=flat)](https://github.com/holoviz/panel/stargazers) - Notebooks as static files or interactive and standalone server-/client-side (via pyodide) apps.
- [PaneLite](https://panelite.holoviz.org) - A distribution of [JupyterLite](https://jupyterlite.readthedocs.io/en/latest/) that works with [Panel](https://panel.holoviz.org) and the [HoloViz](https://holoviz.org) ecosystem. <!--lint enable double-link-->
- [Stencila](https://github.com/stencila/stencila) [![GitHub stars](https://img.shields.io/github/stars/stencila/stencila?style=flat)](https://github.com/stencila/stencila/stargazers) - Native desktop notebook frontend.
- [Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support) - Native desktop notebook frontend.
- [voila](https://github.com/voila-dashboards/voila) [![GitHub stars](https://img.shields.io/github/stars/voila-dashboards/voila?style=flat)](https://github.com/voila-dashboards/voila/stargazers) - Notebooks as interactive standalone web applications.

## Collaboration/Education

- [callgraph](https://github.com/osteele/callgraph) [![GitHub stars](https://img.shields.io/github/stars/osteele/callgraph?style=flat)](https://github.com/osteele/callgraph/stargazers) - Magic to display a function call graph.
- [IllumiDesk](https://github.com/IllumiDesk/illumidesk) [![GitHub stars](https://img.shields.io/github/stars/IllumiDesk/illumidesk?style=flat)](https://github.com/IllumiDesk/illumidesk/stargazers) - Docker-based JupyterHub + LTI + nbgrader distribution for education.
- [ipygame](https://github.com/Kamuyin/ipygame) [![GitHub stars](https://img.shields.io/github/stars/Kamuyin/ipygame?style=flat)](https://github.com/Kamuyin/ipygame/stargazers) - A pygame-compatible reimplementation for Jupyter notebooks.
- [IPythonBlocks](https://github.com/jiffyclub/ipythonblocks) [![GitHub stars](https://img.shields.io/github/stars/jiffyclub/ipythonblocks?style=flat)](https://github.com/jiffyclub/ipythonblocks/stargazers) - Practice Python with colored grids in Jupyter.
- [jupyter-drive](https://github.com/jupyter/jupyter-drive) [![GitHub stars](https://img.shields.io/github/stars/jupyter/jupyter-drive?style=flat)](https://github.com/jupyter/jupyter-drive/stargazers) - Google Drive for Jupyter.
- [jupyter-edx-grader-xblock](https://github.com/ibleducation/jupyter-edx-grader-xblock) [![GitHub stars](https://img.shields.io/github/stars/ibleducation/jupyter-edx-grader-xblock?style=flat)](https://github.com/ibleducation/jupyter-edx-grader-xblock/stargazers) - Auto-grade a student assignment created as a Jupyter notebook and write the score in the Open edX gradebook.
- [jupyter-viewer-xblock](https://github.com/ibleducation/jupyter-viewer-xblock) [![GitHub stars](https://img.shields.io/github/stars/ibleducation/jupyter-viewer-xblock?style=flat)](https://github.com/ibleducation/jupyter-viewer-xblock/stargazers) - Fetch and display part of, or an entire Jupyter Notebook in an Open edX XBlock.
- [jupyterquiz](https://github.com/jmshea/jupyterquiz) [![GitHub stars](https://img.shields.io/github/stars/jmshea/jupyterquiz?style=flat)](https://github.com/jmshea/jupyterquiz/stargazers) - An interactive quiz generator for Jupyter notebooks and Jupyter Book.
- [LTI Launch JupyterHub Authenticator](https://github.com/jupyterhub/ltiauthenticator) [![GitHub stars](https://img.shields.io/github/stars/jupyterhub/ltiauthenticator?style=flat)](https://github.com/jupyterhub/ltiauthenticator/stargazers) - Authentication via Edx.
- [nbautoeval](https://github.com/parmentelat/nbautoeval) [![GitHub stars](https://img.shields.io/github/stars/parmentelat/nbautoeval?style=flat)](https://github.com/parmentelat/nbautoeval/stargazers) - Create auto-evaluated exercises.
- [nbgitpuller](https://github.com/jupyterhub/nbgitpuller) [![GitHub stars](https://img.shields.io/github/stars/jupyterhub/nbgitpuller?style=flat)](https://github.com/jupyterhub/nbgitpuller/stargazers) - Sync a Git repository one-way to a local path.
- [nbgrader](https://github.com/jupyter/nbgrader) [![GitHub stars](https://img.shields.io/github/stars/jupyter/nbgrader?style=flat)](https://github.com/jupyter/nbgrader/stargazers) - Assigning and grading of Jupyter notebooks.
- [nbtutor](https://github.com/lgpage/nbtutor) [![GitHub stars](https://img.shields.io/github/stars/lgpage/nbtutor?style=flat)](https://github.com/lgpage/nbtutor/stargazers) - Visualize Python code execution (line-by-line).

## Visualization

- [Altair](https://github.com/altair-viz/altair) [![GitHub stars](https://img.shields.io/github/stars/altair-viz/altair?style=flat)](https://github.com/altair-viz/altair/stargazers) - Declarative visualization library for Python, based on [Vega](http://vega.github.io/vega) and [Vega-Lite](https://github.com/vega/vega-lite) [![GitHub stars](https://img.shields.io/github/stars/vega/vega-lite?style=flat)](https://github.com/vega/vega-lite/stargazers).
- [anywidget](https://anywidget.dev) - A Python library that simplifies creating and publishing custom Jupyter widgets. 
- [Bokeh](https://bokeh.pydata.org/en/latest/) - Interactive visualization library that targets modern web browsers for presentation.
- [bqplot](https://github.com/bloomberg/bqplot) [![GitHub stars](https://img.shields.io/github/stars/bloomberg/bqplot?style=flat)](https://github.com/bloomberg/bqplot/stargazers) - Grammar of Graphics-based interactive plotting framework for Jupyter.
- [Evidently](https://github.com/evidentlyai/evidently) [![GitHub stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=flat)](https://github.com/evidentlyai/evidently/stargazers) - Interactive reports to analyze machine learning models during validation or production monitoring.
- [hvplot](https://hvplot.holoviz.org/) - A familiar and high-level API for data exploration and visualization in Jupyter.
- [ipychart](https://github.com/nicohlr/ipychart) [![GitHub stars](https://img.shields.io/github/stars/nicohlr/ipychart?style=flat)](https://github.com/nicohlr/ipychart/stargazers) - Interactive Chart.js plots in Jupyter.
- [ipycytoscape](https://github.com/cytoscape/ipycytoscape) [![GitHub stars](https://img.shields.io/github/stars/cytoscape/ipycytoscape?style=flat)](https://github.com/cytoscape/ipycytoscape/stargazers) - Widget for interactive graph visualization in Jupyter using cytoscape.js. <!--lint disable double-link-->
- [ipydagred3](https://github.com/timkpaine/ipydagred3) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/ipydagred3?style=flat)](https://github.com/timkpaine/ipydagred3/stargazers) - [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) [![GitHub stars](https://img.shields.io/github/stars/jupyter-widgets/ipywidgets?style=flat)](https://github.com/jupyter-widgets/ipywidgets/stargazers) library for drawing directed acyclic graphs in jupyterlab using dagre-d3.  <!--lint enable double-link-->
- [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) [![GitHub stars](https://img.shields.io/github/stars/jupyter-widgets/ipyleaflet?style=flat)](https://github.com/jupyter-widgets/ipyleaflet/stargazers) - Interactive visualization library for Leaflet.js maps in Jupyter notebooks.
- [IPySigma](https://github.com/bsnacks000/IPySigma-Demo) [![GitHub stars](https://img.shields.io/github/stars/bsnacks000/IPySigma-Demo?style=flat)](https://github.com/bsnacks000/IPySigma-Demo/stargazers) - Prototype network visualization frontend for Jupyter notebooks.
- [ipytree](https://github.com/QuantStack/ipytree/) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/ipytree/?style=flat)](https://github.com/QuantStack/ipytree//stargazers) - Tree UI element for Jupyter.
- [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) [![GitHub stars](https://img.shields.io/github/stars/vizzuhq/ipyvizzu?style=flat)](https://github.com/vizzuhq/ipyvizzu/stargazers) - Animated data storytelling tool.
- [ipyvolume](https://github.com/maartenbreddels/ipyvolume) [![GitHub stars](https://img.shields.io/github/stars/maartenbreddels/ipyvolume?style=flat)](https://github.com/maartenbreddels/ipyvolume/stargazers) - 3D plotting for Python in Jupyter based on widgets and WebGL.
- [ipywebrtc](https://github.com/maartenbreddels/ipywebrtc) [![GitHub stars](https://img.shields.io/github/stars/maartenbreddels/ipywebrtc?style=flat)](https://github.com/maartenbreddels/ipywebrtc/stargazers) - Video/Audio streaming in Jupyter. <!--lint disable double-link-->
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) [![GitHub stars](https://img.shields.io/github/stars/jupyter-widgets/ipywidgets?style=flat)](https://github.com/jupyter-widgets/ipywidgets/stargazers) - UI widgets for Jupyter.  <!--lint enable double-link-->
- [itk-jupyter-widgets](https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets) [![GitHub stars](https://img.shields.io/github/stars/InsightSoftwareConsortium/itk-jupyter-widgets?style=flat)](https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets/stargazers) - Interactive widgets to visualize images in 2D and 3D.
- [jp_doodle](https://github.com/AaronWatters/jp_doodle) [![GitHub stars](https://img.shields.io/github/stars/AaronWatters/jp_doodle?style=flat)](https://github.com/AaronWatters/jp_doodle/stargazers) - Infrastructure for building special purpose interactive diagrams in 2D and 3D.
- [jupyter-gmaps](https://github.com/pbugnion/gmaps) [![GitHub stars](https://img.shields.io/github/stars/pbugnion/gmaps?style=flat)](https://github.com/pbugnion/gmaps/stargazers) - Interactive visualization library for Google Maps in Jupyter notebooks.
- [jupyter-manim](https://github.com/krassowski/jupyter-manim) [![GitHub stars](https://img.shields.io/github/stars/krassowski/jupyter-manim?style=flat)](https://github.com/krassowski/jupyter-manim/stargazers) - Display [manim](https://github.com/3b1b/manim) [![GitHub stars](https://img.shields.io/github/stars/3b1b/manim?style=flat)](https://github.com/3b1b/manim/stargazers) (Mathematical Animation Engine) videos or GIFs in Jupyter notebooks.
- [lux](https://github.com/lux-org/lux) [![GitHub stars](https://img.shields.io/github/stars/lux-org/lux?style=flat)](https://github.com/lux-org/lux/stargazers) - Recommends a set of visualizations whenever a dataframe is printed in a notebook.
- [mpld3](http://mpld3.github.io) - Combining Matplotlib and D3js for interactive data visualizations.
- [pd-replicator](https://github.com/scwilkinson/pd-replicator) [![GitHub stars](https://img.shields.io/github/stars/scwilkinson/pd-replicator?style=flat)](https://github.com/scwilkinson/pd-replicator/stargazers) - Copy a Pandas DataFrame to the clipboard with one click.
- [Perspective](https://github.com/finos/perspective) [![GitHub stars](https://img.shields.io/github/stars/finos/perspective?style=flat)](https://github.com/finos/perspective/stargazers) - Data visualization and analytics component, especially for large/streaming datasets.
- [pyecharts](https://github.com/pyecharts/pyecharts) [![GitHub stars](https://img.shields.io/github/stars/pyecharts/pyecharts?style=flat)](https://github.com/pyecharts/pyecharts/stargazers) - Python interface for the [ECharts](https://github.com/apache/incubator-echarts) [![GitHub stars](https://img.shields.io/github/stars/apache/incubator-echarts?style=flat)](https://github.com/apache/incubator-echarts/stargazers) visualization library.
- [pythreejs](https://github.com/jovyan/pythreejs) [![GitHub stars](https://img.shields.io/github/stars/jovyan/pythreejs?style=flat)](https://github.com/jovyan/pythreejs/stargazers) - Python / ThreeJS bridge utilizing the Jupyter widget infrastructure.
- [tqdm](https://github.com/tqdm/tqdm) [![GitHub stars](https://img.shields.io/github/stars/tqdm/tqdm?style=flat)](https://github.com/tqdm/tqdm/stargazers) - Fast, extensible progress bar for loops and iterables.
- [tributary](https://github.com/timkpaine/tributary) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/tributary?style=flat)](https://github.com/timkpaine/tributary/stargazers) - Python data streams with Jupyter support.
- [xleaflet](https://github.com/QuantStack/xleaflet) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/xleaflet?style=flat)](https://github.com/QuantStack/xleaflet/stargazers) - C++ Backend for ipyleaflet.
- [xwebrtc](https://github.com/QuantStack/xwebrtc) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/xwebrtc?style=flat)](https://github.com/QuantStack/xwebrtc/stargazers) - C++ Backend for ipywebrtc.
- [xwidgets](https://github.com/QuantStack/xwidgets) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/xwidgets?style=flat)](https://github.com/QuantStack/xwidgets/stargazers) - C++ Backend for ipywidgets.

## Tables

- [buckaroo](https://github.com/paddymul/buckaroo) [![GitHub stars](https://img.shields.io/github/stars/paddymul/buckaroo?style=flat)](https://github.com/paddymul/buckaroo/stargazers) - GUI Data Wrangling tool for Jupyter and pandas.
- [ipyaggrid](https://github.com/widgetti/ipyaggrid) [![GitHub stars](https://img.shields.io/github/stars/widgetti/ipyaggrid?style=flat)](https://github.com/widgetti/ipyaggrid/stargazers) -  The power of ag-Grid in Jupyter.
- [ipydatagrid](https://github.com/bloomberg/ipydatagrid) [![GitHub stars](https://img.shields.io/github/stars/bloomberg/ipydatagrid?style=flat)](https://github.com/bloomberg/ipydatagrid/stargazers) - Fast datagrid widget for Jupyter.
- [ipyregulartable](https://github.com/jpmorganchase/ipyregulartable) [![GitHub stars](https://img.shields.io/github/stars/jpmorganchase/ipyregulartable?style=flat)](https://github.com/jpmorganchase/ipyregulartable/stargazers) - High performance, editable, stylable datagrids in Jupyter.
- [ipysheet](https://github.com/QuantStack/ipysheet/) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/ipysheet/?style=flat)](https://github.com/QuantStack/ipysheet//stargazers) - Interactive spreadsheets in Jupyter.
- [ITables](https://github.com/mwouts/itables) [![GitHub stars](https://img.shields.io/github/stars/mwouts/itables?style=flat)](https://github.com/mwouts/itables/stargazers) - Pandas and Polars DataFrames rendered as interactive [datatables-net](https://datatables.net/) tables.
- [Qgrid](https://github.com/quantopian/qgrid) [![GitHub stars](https://img.shields.io/github/stars/quantopian/qgrid?style=flat)](https://github.com/quantopian/qgrid/stargazers) - Interactive grid for sorting, filtering, and editing DataFrames in Jupyter.

## Rendering/Publishing/Conversion

- [Binder](http://mybinder.org) - Turn a GitHub repo into a collection of interactive notebooks.
- [Bookbook](https://github.com/takluyver/bookbook) [![GitHub stars](https://img.shields.io/github/stars/takluyver/bookbook?style=flat)](https://github.com/takluyver/bookbook/stargazers) - Bookbook converts a set of notebooks in a directory to HTML or PDF, preserving cross references within and between notebooks.
- [ContainDS Dashboards](https://github.com/ideonate/cdsdashboards) [![GitHub stars](https://img.shields.io/github/stars/ideonate/cdsdashboards?style=flat)](https://github.com/ideonate/cdsdashboards/stargazers) - JupyterHub extension to host authenticated scripts or notebooks in any framework (Voilà, Streamlit, Plotly Dash etc).
- [Ganimede](https://github.com/manugraj/ganimede) [![GitHub stars](https://img.shields.io/github/stars/manugraj/ganimede?style=flat)](https://github.com/manugraj/ganimede/stargazers) - Store, version, edit and execute notebooks in sandboxes and integrate them directly via REST interfaces.
- [Jupyter Book](https://github.com/executablebooks/jupyter-book) [![GitHub stars](https://img.shields.io/github/stars/executablebooks/jupyter-book?style=flat)](https://github.com/executablebooks/jupyter-book/stargazers) - Build publication-quality books and documents from computational material.
- [jupyterlab_nbconvert_nocode](https://github.com/timkpaine/jupyterlab_nbconvert_nocode) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/jupyterlab_nbconvert_nocode?style=flat)](https://github.com/timkpaine/jupyterlab_nbconvert_nocode/stargazers) - NBConvert exporters for PDF/HTML export without code cells.
- [Jupytext](https://github.com/mwouts/jupytext) [![GitHub stars](https://img.shields.io/github/stars/mwouts/jupytext?style=flat)](https://github.com/mwouts/jupytext/stargazers) - Convert and synchronize notebooks with text formats (e.g. Python or Markdown files) that work well under version control.
- [jut](https://github.com/kracekumar/jut) [![GitHub stars](https://img.shields.io/github/stars/kracekumar/jut?style=flat)](https://github.com/kracekumar/jut/stargazers) - CLI to nicely display notebooks in the terminal.
- [Kapitsa](https://github.com/gitjeff05/kapitsa) [![GitHub stars](https://img.shields.io/github/stars/gitjeff05/kapitsa?style=flat)](https://github.com/gitjeff05/kapitsa/stargazers) - CLI to search local Jupyter notebooks.
- [Mercury](https://github.com/mljar/mercury) [![GitHub stars](https://img.shields.io/github/stars/mljar/mercury?style=flat)](https://github.com/mljar/mercury/stargazers) - Convert notebooks into web applications.
- [nbconvert](https://nbconvert.readthedocs.io) - Convert notebooks to other formats.
- [nbdev](https://github.com/fastai/nbdev) [![GitHub stars](https://img.shields.io/github/stars/fastai/nbdev?style=flat)](https://github.com/fastai/nbdev/stargazers) - Develop, package and distribute Python packages to PyPI using Jupyter as a [Literate Programing](https://en.wikipedia.org/wiki/Literate_programming) environment.
- [nbflow](https://github.com/jhamrick/nbflow) [![GitHub stars](https://img.shields.io/github/stars/jhamrick/nbflow?style=flat)](https://github.com/jhamrick/nbflow/stargazers) - One-button reproducible workflows with Jupyter and Scons.
- [nbinteract](https://www.nbinteract.com) - Create interactive webpages from Jupyter notebooks.
- [nbscan](https://github.com/conery/nbscan) [![GitHub stars](https://img.shields.io/github/stars/conery/nbscan?style=flat)](https://github.com/conery/nbscan/stargazers) - Search for and print cells contents of Jupyter notebooks.
- [Nikola](https://getnikola.com) - Static Site Generator that converts notebooks into websites.
- [notedown](https://github.com/aaren/notedown/) [![GitHub stars](https://img.shields.io/github/stars/aaren/notedown/?style=flat)](https://github.com/aaren/notedown//stargazers) - Convert Jupyter notebooks to markdown (and back).
- [Papermill](https://github.com/nteract/papermill) [![GitHub stars](https://img.shields.io/github/stars/nteract/papermill?style=flat)](https://github.com/nteract/papermill/stargazers) - Tool for parameterizing, executing, and analyzing Jupyter notebooks.
- [Ploomber](https://github.com/ploomber/ploomber) [![GitHub stars](https://img.shields.io/github/stars/ploomber/ploomber?style=flat)](https://github.com/ploomber/ploomber/stargazers) - Run a collection of notebooks and scripts in a reproducible manner using a `pipeline.yaml` file.
- [pynb](https://github.com/minodes/pynb) [![GitHub stars](https://img.shields.io/github/stars/minodes/pynb?style=flat)](https://github.com/minodes/pynb/stargazers) - Jupyter Notebooks as plain Python code with embedded Markdown text.
- [RISE](https://github.com/damianavila/RISE) [![GitHub stars](https://img.shields.io/github/stars/damianavila/RISE?style=flat)](https://github.com/damianavila/RISE/stargazers) - Reveal.js Jupyter/IPython Slideshow.
- [rst2ipynb](https://github.com/nthiery/rst-to-ipynb) [![GitHub stars](https://img.shields.io/github/stars/nthiery/rst-to-ipynb?style=flat)](https://github.com/nthiery/rst-to-ipynb/stargazers) - Convert standalone reStructuredText files to Jupyter notebook file.
- [Voila](https://github.com/QuantStack/voila) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/voila?style=flat)](https://github.com/QuantStack/voila/stargazers) - Rendering of live Jupyter Notebooks with interactive widgets, allowing dashboarding based on Jupyter Notebooks.

## Version Control

- [databooks](https://github.com/datarootsio/databooks) [![GitHub stars](https://img.shields.io/github/stars/datarootsio/databooks?style=flat)](https://github.com/datarootsio/databooks/stargazers) - A command-line utility that eases versioning and sharing of notebooks.
- [jupyter-nbrequirements](https://github.com/thoth-station/jupyter-nbrequirements/) [![GitHub stars](https://img.shields.io/github/stars/thoth-station/jupyter-nbrequirements/?style=flat)](https://github.com/thoth-station/jupyter-nbrequirements//stargazers) - Dependency management and optimization in Jupyter Notebooks.
- [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-git?style=flat)](https://github.com/jupyterlab/jupyterlab-git/stargazers) - Extension for Git integration.
- [nbdime](https://github.com/jupyter/nbdime) [![GitHub stars](https://img.shields.io/github/stars/jupyter/nbdime?style=flat)](https://github.com/jupyter/nbdime/stargazers) - Tools for diffing and merging of Jupyter notebooks.
- [nbQA](https://github.com/nbQA-dev/nbQA) [![GitHub stars](https://img.shields.io/github/stars/nbQA-dev/nbQA?style=flat)](https://github.com/nbQA-dev/nbQA/stargazers) - Run any standard Python code quality tool on a Jupyter Notebook, from the command-line or via pre-commit.
- [Neptune](https://docs.neptune.ai/integrations-and-supported-tools/ide-and-notebooks/jupyter-lab-and-jupyter-notebook) - Version, manage and share notebook checkpoints in your projects.
- [ReviewNB](https://www.reviewnb.com/) - Code reviews for Jupyter Notebooks.

## JupyterLab Extensions

- [amphi-etl](https://github.com/amphi-ai/amphi-etl) [![GitHub stars](https://img.shields.io/github/stars/amphi-ai/amphi-etl?style=flat)](https://github.com/amphi-ai/amphi-etl/stargazers) - Low-code ETL extension for Jupyterlab.
- [celltags](https://github.com/jupyterlab/jupyterlab-celltags) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-celltags?style=flat)](https://github.com/jupyterlab/jupyterlab-celltags/stargazers) - Extension to organise and execute notebooks using cell tags.
- [code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter) [![GitHub stars](https://img.shields.io/github/stars/ryantam626/jupyterlab_code_formatter?style=flat)](https://github.com/ryantam626/jupyterlab_code_formatter/stargazers) - A universal code formatter.
- [debugger](https://github.com/jupyterlab/debugger) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/debugger?style=flat)](https://github.com/jupyterlab/debugger/stargazers) - A visual debugger for Jupyter notebooks, consoles, and source files.
- [drawio](https://github.com/QuantStack/jupyterlab-drawio) [![GitHub stars](https://img.shields.io/github/stars/QuantStack/jupyterlab-drawio?style=flat)](https://github.com/QuantStack/jupyterlab-drawio/stargazers) - Extension that displays drawio/mxgraph diagrams.
- [elyra](https://github.com/elyra-ai/elyra) [![GitHub stars](https://img.shields.io/github/stars/elyra-ai/elyra?style=flat)](https://github.com/elyra-ai/elyra/stargazers) - A visual editor for creating and running notebook (or Python script) pipelines locally or remotely.
- [genv](https://github.com/run-ai/jupyterlab_genv) [![GitHub stars](https://img.shields.io/github/stars/run-ai/jupyterlab_genv?style=flat)](https://github.com/run-ai/jupyterlab_genv/stargazers) - Extension for managing GPU environments in JupyterLab.
- [go-to-definition](https://github.com/krassowski/jupyterlab-go-to-definition) [![GitHub stars](https://img.shields.io/github/stars/krassowski/jupyterlab-go-to-definition?style=flat)](https://github.com/krassowski/jupyterlab-go-to-definition/stargazers) - Extension for navigating to the definition of a variable or function in JupyterLab.
- [google-drive](https://github.com/jupyterlab/jupyterlab-google-drive) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-google-drive?style=flat)](https://github.com/jupyterlab/jupyterlab-google-drive/stargazers) - Extension for Google Drive integration.
- [jupyter-ai](https://github.com/jupyterlab/jupyter-ai) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=flat)](https://github.com/jupyterlab/jupyter-ai/stargazers) - Work with generative AIs (wide range of models supported) as a conversational assistant in JupyterLab.
- [jupyter-fs](https://github.com/jpmorganchase/jupyter-fs) [![GitHub stars](https://img.shields.io/github/stars/jpmorganchase/jupyter-fs?style=flat)](https://github.com/jpmorganchase/jupyter-fs/stargazers) - A filesystem-like content manager for multiple backends in Jupyter.
- [jupyter-notify](https://github.com/ShopRunner/jupyter-notify) [![GitHub stars](https://img.shields.io/github/stars/ShopRunner/jupyter-notify?style=flat)](https://github.com/ShopRunner/jupyter-notify/stargazers) - Cell magic for browser notification of cell completion. <!--lint disable double-link-->
- [jupyter-panel-proxy](https://github.com/holoviz/jupyter-panel-proxy) [![GitHub stars](https://img.shields.io/github/stars/holoviz/jupyter-panel-proxy?style=flat)](https://github.com/holoviz/jupyter-panel-proxy/stargazers) - Automatically serve notebooks as [Panel](https://panel.holoviz.org) data apps at the `/panel` endpoint of your Jupyter server. <!--lint enable double-link-->
- [jupyter-stack-trace](https://github.com/teticio/jupyter-stack-trace) [![GitHub stars](https://img.shields.io/github/stars/teticio/jupyter-stack-trace?style=flat)](https://github.com/teticio/jupyter-stack-trace/stargazers) - Click on the stack trace to open the respective file or a Google search.
- [jupyterlab-executor](https://github.com/gavincyi/jupyterlab-executor) [![GitHub stars](https://img.shields.io/github/stars/gavincyi/jupyterlab-executor?style=flat)](https://github.com/gavincyi/jupyterlab-executor/stargazers) - Extension to execute scripts from the Jupyterlab file browser. <!--lint disable double-link-->
- [jupyterlab-kyso](https://github.com/kyso-io/jupyterlab-extension) [![GitHub stars](https://img.shields.io/github/stars/kyso-io/jupyterlab-extension?style=flat)](https://github.com/kyso-io/jupyterlab-extension/stargazers) - Extension to publish notebooks to the [Kyso](https://kyso.io) platform from Jupyterlab. <!--lint enable double-link-->
- [jupyterlab-notifications](https://github.com/mwakaba2/jupyterlab-notifications) [![GitHub stars](https://img.shields.io/github/stars/mwakaba2/jupyterlab-notifications?style=flat)](https://github.com/mwakaba2/jupyterlab-notifications/stargazers) - Customizable notebook cell completion browser notifications for JupyterLab.
- [jupyterlab-tensorboard-pro](https://github.com/HFAiLab/jupyterlab_tensorboard_pro) [![GitHub stars](https://img.shields.io/github/stars/HFAiLab/jupyterlab_tensorboard_pro?style=flat)](https://github.com/HFAiLab/jupyterlab_tensorboard_pro/stargazers) - TensorBoard support for JupyterLab.
- [jupyterlab_autoversion](https://github.com/timkpaine/jupyterlab_autoversion) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/jupyterlab_autoversion?style=flat)](https://github.com/timkpaine/jupyterlab_autoversion/stargazers) - Automatically version notebooks in JupyterLab.
- [jupyterlab_commands](https://github.com/timkpaine/jupyterlab_commands) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/jupyterlab_commands?style=flat)](https://github.com/timkpaine/jupyterlab_commands/stargazers) - Add arbitrary python commands to the JupyterLab command palette.
- [jupyterlab_email](https://github.com/timkpaine/jupyterlab_email) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/jupyterlab_email?style=flat)](https://github.com/timkpaine/jupyterlab_email/stargazers) - Email notebooks and their content from within JupyterLab.
- [jupyterlab_iframe](https://github.com/timkpaine/jupyterlab_iframe) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/jupyterlab_iframe?style=flat)](https://github.com/timkpaine/jupyterlab_iframe/stargazers) - View HTML as an embedded iframe in JupyterLab.
- [jupyterlab_miami_nights](https://github.com/timkpaine/jupyterlab_miami_nights) [![GitHub stars](https://img.shields.io/github/stars/timkpaine/jupyterlab_miami_nights?style=flat)](https://github.com/timkpaine/jupyterlab_miami_nights/stargazers) - Combination of VS Code's SynthWave '84 and JupyterLab's Neon Night themes.
- [jupyterlab_templates](https://github.com/jpmorganchase/jupyterlab_templates) [![GitHub stars](https://img.shields.io/github/stars/jpmorganchase/jupyterlab_templates?style=flat)](https://github.com/jpmorganchase/jupyterlab_templates/stargazers) - Notebook templates in JupyterLab.
- [latex](https://github.com/jupyterlab/jupyterlab-latex) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-latex?style=flat)](https://github.com/jupyterlab/jupyterlab-latex/stargazers) - Extension for live editing of LaTeX documents.
- [lineapy](https://github.com/LineaLabs/lineapy) [![GitHub stars](https://img.shields.io/github/stars/LineaLabs/lineapy?style=flat)](https://github.com/LineaLabs/lineapy/stargazers) - Extension for transforming messy Jupyter notebooks to production-ready pipelines with two lines of code.
- [lsp](https://github.com/krassowski/jupyterlab-lsp) [![GitHub stars](https://img.shields.io/github/stars/krassowski/jupyterlab-lsp?style=flat)](https://github.com/krassowski/jupyterlab-lsp/stargazers) - IDE-like features (code navigation, hover suggestions, linters, diagnostics, kernel-less autocompletion etc.)
- [nb_black](https://github.com/dnanhkhoa/nb_black) [![GitHub stars](https://img.shields.io/github/stars/dnanhkhoa/nb_black?style=flat)](https://github.com/dnanhkhoa/nb_black/stargazers) - Extension to keep Python code automatically formatted using [black](https://github.com/psf/black) [![GitHub stars](https://img.shields.io/github/stars/psf/black?style=flat)](https://github.com/psf/black/stargazers).
- [python-bytecode](https://github.com/jtpio/jupyterlab-python-bytecode) [![GitHub stars](https://img.shields.io/github/stars/jtpio/jupyterlab-python-bytecode?style=flat)](https://github.com/jtpio/jupyterlab-python-bytecode/stargazers) - Explore CPython Bytecode in JupyterLab.
- [quickopen](https://github.com/parente/jupyterlab-quickopen) [![GitHub stars](https://img.shields.io/github/stars/parente/jupyterlab-quickopen?style=flat)](https://github.com/parente/jupyterlab-quickopen/stargazers) - Quickly open a file in JupyterLab by typing part of its name.
- [shortcutui](https://github.com/jupyterlab/jupyterlab-shortcutui) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-shortcutui?style=flat)](https://github.com/jupyterlab/jupyterlab-shortcutui/stargazers) - An extension for managing keyboard shortcuts.
- [sidecar](https://github.com/jupyter-widgets/jupyterlab-sidecar) [![GitHub stars](https://img.shields.io/github/stars/jupyter-widgets/jupyterlab-sidecar?style=flat)](https://github.com/jupyter-widgets/jupyterlab-sidecar/stargazers) - A sidecar output widget for JupyterLab.
- [sql](https://github.com/pbugnion/jupyterlab-sql) [![GitHub stars](https://img.shields.io/github/stars/pbugnion/jupyterlab-sql?style=flat)](https://github.com/pbugnion/jupyterlab-sql/stargazers) - SQL GUI for JupyterLab.
- [stickyland](https://github.com/xiaohk/stickyland) [![GitHub stars](https://img.shields.io/github/stars/xiaohk/stickyland?style=flat)](https://github.com/xiaohk/stickyland/stargazers) - Break the linear presentation of notebooks with sticky cells.
- [system-monitor](https://github.com/jtpio/jupyterlab-system-monitor) [![GitHub stars](https://img.shields.io/github/stars/jtpio/jupyterlab-system-monitor?style=flat)](https://github.com/jtpio/jupyterlab-system-monitor/stargazers) - Extension to display system metrics.
- [tabnine](https://github.com/codota/tabnine-jupyterlab) [![GitHub stars](https://img.shields.io/github/stars/codota/tabnine-jupyterlab?style=flat)](https://github.com/codota/tabnine-jupyterlab/stargazers) - Tabnine AI auto completer extension.
- [theme-darcula](https://github.com/telamonian/theme-darcula) [![GitHub stars](https://img.shields.io/github/stars/telamonian/theme-darcula?style=flat)](https://github.com/telamonian/theme-darcula/stargazers) - A handsome Darcula theme for Jupyterlab.
- [toc](https://github.com/jupyterlab/jupyterlab-toc) [![GitHub stars](https://img.shields.io/github/stars/jupyterlab/jupyterlab-toc?style=flat)](https://github.com/jupyterlab/jupyterlab-toc/stargazers) - Extension that provides a table of contents for notebooks.
- [topbar](https://github.com/jtpio/jupyterlab-topbar) [![GitHub stars](https://img.shields.io/github/stars/jtpio/jupyterlab-topbar?style=flat)](https://github.com/jtpio/jupyterlab-topbar/stargazers) - Top Bar extension for JupyterLab.
- [variableinspector](https://github.com/lckr/jupyterlab-variableInspector) [![GitHub stars](https://img.shields.io/github/stars/lckr/jupyterlab-variableInspector?style=flat)](https://github.com/lckr/jupyterlab-variableInspector/stargazers) - Variable inspector extension that shows variables and their values.
- [vim](https://github.com/jwkvam/jupyterlab-vim) [![GitHub stars](https://img.shields.io/github/stars/jwkvam/jupyterlab-vim?style=flat)](https://github.com/jwkvam/jupyterlab-vim/stargazers) - Vim notebook cell bindings.
- [voyager](https://github.com/altair-viz/jupyterlab_voyager) [![GitHub stars](https://img.shields.io/github/stars/altair-viz/jupyterlab_voyager?style=flat)](https://github.com/altair-viz/jupyterlab_voyager/stargazers) - Extension to view CSV and JSON data in [Voyager](http://vega.github.io/voyager/).

## Testing

- [ipytest](https://github.com/chmp/ipytest) [![GitHub stars](https://img.shields.io/github/stars/chmp/ipytest?style=flat)](https://github.com/chmp/ipytest/stargazers) - Test runner for running unit tests from within a notebook.
- [nbcelltests](https://github.com/jpmorganchase/nbcelltests) [![GitHub stars](https://img.shields.io/github/stars/jpmorganchase/nbcelltests?style=flat)](https://github.com/jpmorganchase/nbcelltests/stargazers) - Cell-by-cell testing for notebooks in Jupyter.
- [nbval](https://github.com/computationalmodelling/nbval) [![GitHub stars](https://img.shields.io/github/stars/computationalmodelling/nbval?style=flat)](https://github.com/computationalmodelling/nbval/stargazers) - Py.test plugin for validating Jupyter notebooks.
- [nosebook](https://github.com/bollwyvl/nosebook) [![GitHub stars](https://img.shields.io/github/stars/bollwyvl/nosebook?style=flat)](https://github.com/bollwyvl/nosebook/stargazers) - Nose plugin for finding and running IPython notebooks as nose tests.
- [pointblank](https://github.com/posit-dev/pointblank) [![GitHub stars](https://img.shields.io/github/stars/posit-dev/pointblank?style=flat)](https://github.com/posit-dev/pointblank/stargazers) - Notebook-friendly testing of DataFrames and database tables for data quality purposes.
- [sphinxcontrib-jupyter](https://github.com/QuantEcon/sphinxcontrib-jupyter) [![GitHub stars](https://img.shields.io/github/stars/QuantEcon/sphinxcontrib-jupyter?style=flat)](https://github.com/QuantEcon/sphinxcontrib-jupyter/stargazers) - Sphinx extension for generating Jupyter notebooks.
- [treebeard](https://github.com/treebeardtech/treebeard) [![GitHub stars](https://img.shields.io/github/stars/treebeardtech/treebeard?style=flat)](https://github.com/treebeardtech/treebeard/stargazers) - GitHub Action for testing/scheduling Jupyter notebooks.
- [treon](https://github.com/ReviewNB/treon) [![GitHub stars](https://img.shields.io/github/stars/ReviewNB/treon?style=flat)](https://github.com/ReviewNB/treon/stargazers) - Easy-to-use test framework for Jupyter Notebooks.

## Domain-Specific Projects

- [ArcGIS](https://developers.arcgis.com/python/) - Library for working with maps and geospatial data, powered by web GIS.
- [GenePattern Notebook](http://genepattern-notebook.org) - Integrating Genomic Analysis with Interactive Notebooks.
- [GeoNotebook](https://github.com/OpenGeoscience/geonotebook) [![GitHub stars](https://img.shields.io/github/stars/OpenGeoscience/geonotebook?style=flat)](https://github.com/OpenGeoscience/geonotebook/stargazers) - Extension for exploratory geospatial analysis.
- [Jupylet](https://github.com/nir/jupylet) [![GitHub stars](https://img.shields.io/github/stars/nir/jupylet?style=flat)](https://github.com/nir/jupylet/stargazers) - Create 2D and 3D games, graphics, live music and sound interactively in a Jupyter notebook.
- [keplergl](https://docs.kepler.gl/docs/keplergl-jupyter) - Jupyter extension for visual exploration of large-scale geolocation data sets.
- [lolviz](https://github.com/parrt/lolviz) [![GitHub stars](https://img.shields.io/github/stars/parrt/lolviz?style=flat)](https://github.com/parrt/lolviz/stargazers) - Data-structure visualization tool for lists of lists, lists, dictionaries.
- [Quantopian Notebooks](https://www.quantopian.com/notebooks/survey) - Jupyter-based platform for financial research.
- [vpython-jupyter](https://github.com/BruceSherwood/vpython-jupyter) [![GitHub stars](https://img.shields.io/github/stars/BruceSherwood/vpython-jupyter?style=flat)](https://github.com/BruceSherwood/vpython-jupyter/stargazers) - VPython 3D engine running in a Jupyter notebook.
- [xontrib-jupyter](https://github.com/xonsh/xontrib-jupyter) [![GitHub stars](https://img.shields.io/github/stars/xonsh/xontrib-jupyter?style=flat)](https://github.com/xonsh/xontrib-jupyter/stargazers) - Jupyter kernel for xonsh, a Python-powered, cross-platform, Unix-gazing shell language.

## Hosted Notebook Solutions

- [Anaconda Enterprise](https://www.anaconda.com/enterprise/) - Multi-user collaboration and one-click deployment of models, notebooks, and dashboards.
- [Azure Notebooks](https://notebooks.azure.com) - Jupyter notebooks running in the cloud on Microsoft Azure.
- [CoCalc](https://cocalc.com) - Notebooks with 17 supported kernel types, course management, LaTeX document authoring, simultaneous document editing and integration with the SageMath computer algebra system.
- [DataBlogs](https://www.datablogs.co/) - DataBlogs is an open-source data journalism platform that converts Jupyter notebooks into published articles on the web.
- [DataCamp Workspace](https://www.datacamp.com/workspace) - Jupyter-backed data science notebooks with built-in collaboration and publishing functionality.
- [Datalore](https://www.jetbrains.com/datalore) - Jupyter-compatible data science and analytics notebook solution for team collaboration by JetBrains.
- [Deepnote](https://www.deepnote.com) - Jupyter-compatible data science notebook with real-time collaboration, versioning and easy deployment.
- [Domino Data Lab](https://www.dominodatalab.com) - Data science platform with integrated collaboration tools, environment management and compute grid.
- [Google Cloud AI Platform Notebooks](https://cloud.google.com/ai-platform-notebooks) - Managed JupyterLab notebook instances configured with GPU-enabled machine learning frameworks on Google Cloud Platform.
- [Google Cloud Dataproc Jupyter component](https://cloud.google.com/dataproc/docs/concepts/components/jupyter) - Jupyter and JupyterLab for Apache Spark using Google Cloud Dataproc.
- [Google Colaboratory](https://colab.research.google.com) - Cloud-based Jupyter environment aimed at machine learning education and research.  <!--lint disable double-link-->
- [Kyso](https://kyso.io) - Data science platform to publish and share Jupyter notebooks as data blogs and web applications.  <!--lint enable double-link-->
- [Mineo.app](https://mineo.app) - Data Ops platform with Jupyter-compatible notebooks, no code blocks, and support for creating dashboards.
- [Naas](https://naas.ai) - JupyterLab environment with magic scheduling/notification functionality and assets/dependency/secrets management.
- [Noteable](https://noteable.io/) - Noteable is a collaborative notebook to combine code (SQL, Python & R) and interactive visualizations.
- [Paperspace Gradient](https://gradient.run/) - A Jupyter-backed data science IDE with accelerated hardware (GPUs) and MLOps functionality.
- [PAWS](https://wikitech.wikimedia.org/wiki/PAWS) - Jupyter notebook deployment customized for interacting with Wikimedia wikis.
- [Pinggy](https://pinggy.io) - Create a tunnel to your Jupyter instance even if it is behind a firewall or NAT.
- [qBraid Lab](https://docs.qbraid.com/en/latest/lab/getting_started.html) - JupyterLab deployment providing curated software tools and integrations for quantum computing.
- [Saturn Cloud](https://saturncloud.io/) - Move your data science team into the cloud without having to switch tools.

## Official Resources and Documentation

- [Jupyter documentation](https://docs.jupyter.org/en/latest/index.html)
- [Jupyter kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) [![GitHub stars](https://img.shields.io/github/stars/jupyter/jupyter/wiki/Jupyter-kernels?style=flat)](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels/stargazers) - List of all programming languages available as Jupyter kernels.
- [JupyterLab documentation](http://jupyterlab.readthedocs.io/en/stable/index.html)
- [Making kernels for Jupyter](https://jupyter-client.readthedocs.io/en/latest/kernels.html)
- [Try Jupyter](https://try.jupyter.org) - Try Jupyter in your browser.

## Community Resources

- Conference Talks - [PyVideo.org](http://pyvideo.org/search.html?q=jupyter), [JupyterCon](https://www.youtube.com/playlist?list=PL055Epbe6d5aP6Ru42r7hk68GTSaclYgi)
- GitHub - Search: [Jupyter](https://github.com/search?type=Repositories&q=jupyter) [![GitHub stars](https://img.shields.io/github/stars/search?type=Repositories&q=jupyter?style=flat)](https://github.com/search?type=Repositories&q=jupyter/stargazers)
- GitHub - Topics: [Jupyter](https://github.com/topics/jupyter) [![GitHub stars](https://img.shields.io/github/stars/topics/jupyter?style=flat)](https://github.com/topics/jupyter/stargazers), [jupyter-kernels](https://github.com/topics/jupyter-kernels) [![GitHub stars](https://img.shields.io/github/stars/topics/jupyter-kernels?style=flat)](https://github.com/topics/jupyter-kernels/stargazers), [jupyter-notebook](https://github.com/topics/jupyter-notebook) [![GitHub stars](https://img.shields.io/github/stars/topics/jupyter-notebook?style=flat)](https://github.com/topics/jupyter-notebook/stargazers), [jupyterhub](https://github.com/topics/jupyterhub) [![GitHub stars](https://img.shields.io/github/stars/topics/jupyterhub?style=flat)](https://github.com/topics/jupyterhub/stargazers), [jupyterlab](https://github.com/topics/jupyterlab) [![GitHub stars](https://img.shields.io/github/stars/topics/jupyterlab?style=flat)](https://github.com/topics/jupyterlab/stargazers), [jupyterlab-extension](https://github.com/topics/jupyterlab-extension) [![GitHub stars](https://img.shields.io/github/stars/topics/jupyterlab-extension?style=flat)](https://github.com/topics/jupyterlab-extension/stargazers)
- Gitter - [Jupyter Gitter Chatroom](https://gitter.im/jupyter/jupyter)
- [jupyter-map](https://elc.github.io/jupyter-map/) - Map of university institutions that use Jupyter.
- [kandi Kits Topic](https://kandi.openweaver.com/explore/jupyter) - Discover popular Jupyter libraries, top authors, trending project kits, discussions, tutorials & learning resources.  <!--lint disable double-link-->
- Mailing Lists - [Jupyter General Mailing List](https://groups.google.com/forum/#!forum/jupyter), [Jupyter in Education Mailing List](https://groups.google.com/forum/#!forum/jupyter-education) <!--lint enable double-link-->
- PyPI - [``Framework :: Jupyter``](https://pypi.org/search/?&c=Framework+%3A%3A+Jupyter)
is the PyPI trove classifier for Jupyter projects.
- Reddit - Subreddits: [r/IPython](https://www.reddit.com/r/IPython/), [r/Jupyter/](https://www.reddit.com/r/Jupyter/)
- Stack Overflow - Tags: [Jupyter](https://stackoverflow.com/questions/tagged/jupyter), [jupyter-notebook](https://stackoverflow.com/questions/tagged/jupyter-notebook)


## Articles/Guides/Tutorials

- [Exploratory computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/) - Collection of notebooks covering scientific computing.
- [How to Grow Neat Software Architecture out of Jupyter Notebooks](https://github.com/guillaume-chevalier/How-to-Grow-Neat-Software-Architecture-out-of-Jupyter-Notebooks) [![GitHub stars](https://img.shields.io/github/stars/guillaume-chevalier/How-to-Grow-Neat-Software-Architecture-out-of-Jupyter-Notebooks?style=flat)](https://github.com/guillaume-chevalier/How-to-Grow-Neat-Software-Architecture-out-of-Jupyter-Notebooks/stargazers) - Article and [video](https://www.youtube.com/watch?v=K4QN27IKr0g) about growing a neat software architecture from notebooks.
- [Install and run a Jupyter notebook in a Google Cloud Dataproc cluster](https://cloud.google.com/dataproc/docs/tutorials/jupyter-notebook)
- [Interactive Web Plotting with Bokeh](https://github.com/bokeh/bokeh-notebooks) [![GitHub stars](https://img.shields.io/github/stars/bokeh/bokeh-notebooks?style=flat)](https://github.com/bokeh/bokeh-notebooks/stargazers)
- [Jupyter Notebook Extensions](http://jupyter-contrib-nbextensions.readthedocs.io)
- [Jupyter Notebook Themes](https://github.com/dunovank/jupyter-themes) [![GitHub stars](https://img.shields.io/github/stars/dunovank/jupyter-themes?style=flat)](https://github.com/dunovank/jupyter-themes/stargazers)
- [Jupyter tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- [JupyterLab - Your Personal Data Science Workbench](https://github.com/markusschanta/talks/tree/master/2018-03%20-%20JupyterLab%20-%20Full%20Stack%20Quants) [![GitHub stars](https://img.shields.io/github/stars/markusschanta/talks/tree/master/2018-03%20-%20JupyterLab%20-%20Full%20Stack%20Quants?style=flat)](https://github.com/markusschanta/talks/tree/master/2018-03%20-%20JupyterLab%20-%20Full%20Stack%20Quants/stargazers) - Talk about JupyterLab at Full Stack Quants London.
- [Lectures on scientific computing with Python](https://github.com/jrjohansson/scientific-python-lectures) [![GitHub stars](https://img.shields.io/github/stars/jrjohansson/scientific-python-lectures?style=flat)](https://github.com/jrjohansson/scientific-python-lectures/stargazers)
- [List of Jupyter notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks) [![GitHub stars](https://img.shields.io/github/stars/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks?style=flat)](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks/stargazers)
- [List of Jupyter notebooks II](https://github.com/jupyter-naas/awesome-notebooks) [![GitHub stars](https://img.shields.io/github/stars/jupyter-naas/awesome-notebooks?style=flat)](https://github.com/jupyter-naas/awesome-notebooks/stargazers)
- [pytudes](https://github.com/norvig/pytudes) [![GitHub stars](https://img.shields.io/github/stars/norvig/pytudes?style=flat)](https://github.com/norvig/pytudes/stargazers) - List of Jupyter Notebooks by Peter Norvig.
- [ResGuides: research with Jupyter](https://www.gitbook.com/book/dansand/resguides-research-with-jupyter/details)
- [Sharing Jupyter Notebooks from localhost](https://pinggy.io/blog/share_jupyter_notebook_from_localhost/) - Sharing Jupyter Notebooks from localhost.
- [The Littlest JupyterHub](https://the-littlest-jupyterhub.readthedocs.io/en/latest/) - JupyterHub distribution for 1-50 users on a single server; more lightweight than the Zero to JupyterHub setup.
- [Zero to JupyterHub](http://zero-to-jupyterhub.readthedocs.io/en/latest/) - Tutorial to help install and manage JupyterHub.

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](CONTRIBUTING.md) first.
