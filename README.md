# The Jupyter Widget Ecosystem

## Tutorial, JupyterCon 2020

## Installation on your own computer

*You do not have to install the software on your computer to do the tutorial. JupyterCon will provide an environment for going through the materials. Follow these instruction if you want to run it on your computer.*

The code in the tutorial has been written using Python 3; many of the dependencies may not be available for Python 2.7.

We **strongly recommend** using the Anaconda Python distribution. You can install either the full [anaconda distribution](https://www.continuum.io/downloads) (very extensive, but large) or [miniconda](https://conda.io/miniconda.html) (much smaller, only essential packages).

Almost all of the examples will work in either the regular Jupyter notebook or in JupyterLab. The instructions below assume you will be using JupyterLab.

There are also download instructions below for installation using pip, which should work with any Python distribution.

## Download this repository

You can do this with either
`git clone https://github.com/jupytercon/2020-widgets-tutorial` at the command
line or by downloading this repostiory as a [Zip file](https://github.com/jupytercon/2020-widgets-tutorial/archive/master.zip).

## conda installation instructions

The steps below will get you a working environment.

```bash
conda env create -f environment.yml

conda activate widgets-jcon20

# Create a kernel for this environment
ipython kernel install --name widgets-jcon20 --display-name widgets-jcon20 --sys-prefix
```

### Windows users
The installation instructions were tested on an up-to-date version of Windows 10 Professional. If you encounter any issues on Windows please open an issue or contact us through slack.

## pip installation instructions

If you are not using the anaconda python distribution, please use the instructions below.

```bash
pip install -r requirements.txt

# Create a kernel for this environment
ipython kernel install --name widgets-tutorial --display-name widgets-tutorial --sys-prefix
```

## Install JupyterLab extensions

In order to install the JupyterLab extensions, you need `nodejs` to be installed. If you use `conda` it should have been already installed for you when you created your environment.


If you do not use `conda`, see [https://nodejs.org/en/download/](https://nodejs.org/en/download/) or [https://nodejs.org/en/download/package-manager/](https://nodejs.org/en/download/package-manager/) for download and installation instructions.


Now you can install the JupyterLab extensions:

```bash
# This may take several minutes
jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyter-widgets/jupyterlab-sidecar bqplot
```

<!-- **Only if we use them: `ipysheet ipytree`** -->

## Check your installation

To check your installation, please download the script [install_check.py](https://raw.githubusercontent.com/jupytercon/2020-widgets-tutorial/master/install_check.py) and run it:

```bash
python install_check.py
```

## Tutorial materials

To get the tutorial materials, clone this repository. *We anticipate making changes to the tutorial content through the end of October 2, 2020.*

To update your copy of the tutorial materials, navigate in a terminal to folder these materials are in then run `git pull`. An alternative is to download the repository again as a zip file.

## Any ipywidgets or custom widgets library question?

Please join us on the Gitter channel: https://gitter.im/jupyter-widgets/Lobby

## Running into trouble?

Please let us know! You can open an issue on this repository by clicking "Issues" under the repo name on GitHub, then the "New Issue" button in the upper right.
