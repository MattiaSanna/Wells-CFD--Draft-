# Wells Turbine CFD Analysis

## 1. Project Overview

This project focuses on the numerical replication of experimental Wells turbine performance, based on my bachelor thesis *The Effect of Solidity on Wells Turbine Performance*.

A single configuration from the experimental campaign was selected for numerical replication. The same turbine geometry, rotational speed, inlet conditions and fluid properties were implemented in ANSYS Fluent using a steady Multiple Reference Frame (MRF) approach. 


## 2. Project Objectives and Methodology

The numerical investigation was divided into several stages:

1. CAD reconstruction of the experimental turbine.
2. Computational domain development using a Multiple Reference Frame approach.
3. Mesh generation and near-wall refinement.
4. Definition of the physical models and boundary conditions.
5. Numerical quality assessment and mesh independence.
6. Post-processing of aerodynamic quantities.
7. Comparison against experimental performance data.
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
- Target y+ ≈ 1

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
## Model Validation

The numerical model was validated by comparing CFD predictions against the experimental results reported in the reference thesis.

Validation focused on:
- **Torque, pressure drop and efficiency:** comparing simulated and experimental torque across different inlet velocities.
- **Flow behaviour:** examining pressure and velocity distributions around the blades to verify that the simulated aerodynamic behaviour was physically consistent.

A grid independence study was also conducted using four mesh resolutions (1.2M, 3.5M, 7.8M and 12.1M cells). Torque and efficiency were monitored across the mesh levels to assess the influence of cell count on the numerical results.

Residual convergence and the stability of monitored quantities were checked to evaluate numerical convergence.

The comparison highlighted differences between CFD predictions and experimental measurements, providing a basis for assessing the limitations of the numerical setup and identifying areas for further improvement.
## Technologies

- ANSYS Fluent
- ANSYS DesignMdoler
- Python
- MATLAB
- SolidWorks
- HTML, CSS and JavaScript

## Objective

The project combines CAD reconstruction, computational mesh generation, CFD simulation and numerical post-processing to investigate Wells turbine aerodynamics and assess the reliability of numerical predictions against experimental data.
