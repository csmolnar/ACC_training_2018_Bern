# Training: Advanced Cell Classifier for the analysis of HCS data

## Author

Csaba Molnar, BIOMAG Group, Biological Research Centre, Szeged

## Abstract

In this workshop we aim to implement an image-based analysis of a biological system by profiling the phenotipic response of a cancer cell line following perturbation with a small-molecule compound library by using [Advanced Cell Classifier](https://www.cellclassifier.org/), an interactive tool designed to analyse high-throughput experiments on single cell level.

## Software Installation

All the following softwares are recommended to be installed by the time of the training.

Required softwares:

- __CIDRE__
  - Download the ImageJ version of CIDRE illumination correction from [here](https://github.com/smithk/cidre).
  - Download ImageJ from [here](https://imagej.net/Fiji/Downloads). Copy the Cidre_Plugin.jar file to the plugin directory of ImageJ.
- __CellProfiler 2.2.0__
  - Download CellProfiler 2.2.0 release from [here](http://cellprofiler.org/previous_releases/).
  - Be aware of non-English characters in the path of your home directory! If you have those, you have to change the plugin directory by editing registry.
- __Advanced Cell Classifier__
  - Download ACC 3.0 standalone version from [here](http://www.cellclassifier.org/download/). You can use the standalone version after installation of [Matlab Runtime](https://se.mathworks.com/products/compiler/matlab-runtime.html) release R2017a.
  - Download [ExportToACC](http://eucaiorg.ipage.com/ACC/wp-content/uploads/2016/07/ExportToACCmodule.zip) CellProfiler module for saving data in ACC format. Copy exporttoacc.py file into the CellProfiler's plugins directory (File->Preferences->CellProfiler plugins directory).

Optional
  - Download and install Python 2.7 from [here](https://www.python.org/download/releases/2.7/).

Sample datasets:

- __HCS__ input (for flat field correction and focus detection)
  - [Small dataset](https://drive.google.com/open?id=1WEhhCirTY--eyRZ_Siv9R0evXE-nRtN2) (~300MB)
  - [Big dataset](https://drive.google.com/open?id=1qlLCxCqjEl5pOefEH1ktkwZJ2LwgVVg1) (~3GB)
- __Segmentation__ input (after steps flat field correction and focus detection)
  - [Small dataset](https://drive.google.com/open?id=1F5Wa_KCrpnyu8afbAamEp9ac76zesCcg) (~180MB)
  - [Big dataset](https://drive.google.com/open?id=1MPXjDr1qbkkqIhsSDJP3NVbOjHBhqT18) (~1.8GB)
- __ACC__ sample input
  - [Sample dataset](http://acc.ethz.ch/imagecounter/downloadPage.php?fileName=ACC/Test-ProjectFolder01.zip)
