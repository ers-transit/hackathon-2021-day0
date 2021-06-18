# ERS Pre-launch Data Hackathon | Day 0
This repository contains a tutorial [notebook](hackathon-day0-tutorial.ipynb) and some helpful data files for getting started.

Day 0 is an optional day that is particularly designed for new community members and those who want help getting their coding environments set up. You can use this tutorial whether or not you attend the Day 0 zoom session.

## If you plan to attend Day 0 on zoom:
We will walk step-by-step through a Guided Tutorial on the process of setting up a convenient coding environment to work with JWST data. It is not a complete introduction to the Python language, but it shares some tips to help get started.

### Before you attend:
Please be aware there are a few things you'll need to download. Some of them include large files, so it's probably a good idea to start downloading them *before* the start of the tutorial session. Those downloads are:
1. **Anaconda Python Distribution.** If do not yet have `conda` installed on your computer yet, download an installer for [Anaconda Individual Edition](https://www.anaconda.com/products/individual) for your computer. Try running that installer; it should be pretty straightforward.
2. **This tutorial repository.** You can download everything you need by clicking the green *Code* button in the upper right corner of this window and selecting *Download ZIP*. (If you're new to GitHub, consider Christina Hedges' Day 1 GitHub tutorial tomorrow for a great introduction!)

## If you do not plan to attend Day 0 on zoom:
If you plan to participate in the Guided Tutorials on Days 1, 2, and 3, there are some coding ingredients you will need.

If you're using Python 3.6 or greater, you should be able to get pretty much everything by running `pip install git+https://github.com/ers-transit/ers-transit-tutorial-requirements.git --upgrade`.

If that doesn't work, or if you want to follow our suggestion of working in a clean `conda` environment, the `environment.yml` file in this repository defines an `ers-transit` conda environment with everything we expect to be needed for the Guided Tutorials. You can create this environment on your computer using `conda env create -f environment.yml` (more detailed instructions are available in the tutorial [notebook](hackathon-day0-tutorial.ipynb)).

## If you can't get Python working on your computer:
You can still (mostly) run this notebook using Google Colaboratory. Simply click [this link](https://colab.research.google.com/github/ers-transit/hackathon-2021-day0/blob/main/hackathon-day0-tutorial-colab-version.ipynb) to open and run it with your google account.
