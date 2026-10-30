# Wells Turbine CFD Analysis

## Project Overview

This project focuses on the numerical replication of experimental Wells turbine performance, based on the thesis *The Effect of Solidity on Wells Turbine Performance*.

The objective was to investigate the aerodynamic behaviour of a six-blade Wells turbine using ANSYS Fluent and compare numerical results with experimental data.

## CAD Model and Airfoil Generation

The turbine geometry was reconstructed using a **NACA 0015 symmetrical airfoil**, with six blades arranged around the hub.

Python was used to generate the right airfoil profile mathematically starting from the NACA_0015 coordinates, later  exported for CAD reconstruction.

This approach ensured an accurate airfoil geometry instead of relying on manually drawn profiles.

## Computational Domain

The computational domain was divided into three regions:
- Upstream stationary duct
- Rotating region containing the turbine
- Downstream stationary duct

A **60° periodic sector** was used to model a single blade passage, reducing computational cost while preserving the turbine's rotational symmetry.

## Mesh Generation

An unstructured hybrid mesh was generated, with local refinement around the blades and inflation layers to resolve the boundary layer.

The mesh included:
- 15 inflation layers
- Growth rate of 1.2
- Target \(y^+ \approx 1\)

A grid independence study was also performed using four mesh resolutions, ranging from 1.2 to 12.1 million cells.

## CFD Setup

The simulations were performed in **ANSYS Fluent** using:
- Pressure-based, steady-state solver
- SST \(k-\omega\) turbulence model
- Multiple Reference Frame (MRF)
- Velocity inlet and pressure outlet
- No-slip blade walls
- Second-order spatial discretisation

The MRF approach allowed the rotating turbine to be simulated within a stationary computational domain.

## Post-Processing and MATLAB Analysis

Fluent results were exported for further analysis in MATLAB.

The post-processing workflow calculated:
- Flow coefficient
- Pressure coefficient
- Torque coefficient
- Aerodynamic efficiency

Numerical results were then compared with experimental measurements to evaluate the accuracy of the CFD model.

## Technologies

- ANSYS Fluent
- ANSYS SpaceClaim
- Python
- MATLAB
- SolidWorks
- HTML, CSS and JavaScript

## Objective

The project combines CAD reconstruction, computational mesh generation, CFD simulation and numerical post-processing to investigate Wells turbine aerodynamics and assess the reliability of numerical predictions against experimental data.
