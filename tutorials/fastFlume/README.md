# This tutorial for SOWFA is for model of hydrokinetic turbines.

* full-scale axial-flow tidal turbine, rated power of 550kW, diameter of 20-m
* created by US DOE to standardize experimental and numerical studies
* foils are NACA 4 and 6 series chosen for cavitation prevention and well known performance characteristics at low and high Reynolds numbers
* laboratory scale turbine 45:1 scaling -- diameter of 45-cm
* attempt to match power extraction and wake characteristics at lab-scale
* lab-scale rotor was re-designed to minimize Reynolds scaling effects

Two turbine models are included in this tutorial the full-scale and laboratory-scale re-design.  This repository uses seperate branches for different OpenFOAM cases (like when changing meshes, turbine configurations and layouts).


## Some additional scripts have also been added:
* session files for visualization using VisIt
* spreadsheet to estimate values for actuator-line settings, timestepping, mesh size, etc...


## Running on HPC ...
These simulations were test to run up to hundreds of CPUs. and checkpointing is working properly now.
Further improvements to the LES model would be ... local mesh
refinement, improve distribution of body forces (like
elliptical wing or disk/sector method), add background turbulence,
change wall boundary conditions, add a controller for the rotor drivetrain ...

![turbine-photo-stitch](https://raw.githubusercontent.com/nnmrec/fastFlume/master/docs/figures/turbine-photostitch-63-79-93-resized.png)

