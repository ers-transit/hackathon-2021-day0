# ERS Pre-launch Data Hackathon | Day 0
This repository contains a tutorial [notebook](hackathon-day0-tutorial.ipynb) and some helpful data files for getting started.

Day 0 is an optional day that is particularly designed for new community members and those who want help getting their coding environments set up. You can use this tutorial whether or not you attend the Day 0 zoom session.

## If you plan to attend Day 0 on zoom:
We will walk step-by-step through a Guided Tutorial on the process of setting up a convenient coding environment to work with JWST data.

Please be aware there are a few things you'll need to download. Some of them include large files, so it's probably a good idea to start downloading them *before* the start of the tutorial session.

Those downloads are:
1. **This tutorial repository.** If you're new to GitHub, click the green *Code* button in the upper right corner of this window and select *Download ZIP*. (Check out Christina Hedges' Day 1 GitHub tutorial tomorrow for more advanced GitHub concepts!)
2. **Anaconda Python Distribution.** If do not yet have `conda` installed on your computer yet, download an installer for [Anaconda Individual Edition](https://www.anaconda.com/products/individual) for your computer.
3. **Some simulated data.** [ZKBT wonders, do we want to include a tiny sample file in this repository directly, or have them download a real file from the Box?]

## If you do not plan to attend Day 0 on zoom:
If you plan to participate in the Guided Tutorials on Days 1, 2, and 3, there are some coding ingredients you will need. The `environment.yml` file in this repository defines an `ers-transit` conda environment with everything we expect to be needed for the Guided Tutorials. Please create this environment on your computer using `conda env create -f environment.yml` (more detailed instructions are available in the tutorial [notebook](hackathon-day0-tutorial.ipynb)).