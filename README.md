
# Wells Turbine CFD — Numerical Replication of Experimental Performance


## 1. Project Overview

This project investigates the ability of Computational Fluid Dynamics (CFD) to reproduce the experimental performance of a Wells turbine.

The work is based on my Bachelor's thesis, *The Effect of Solidity on Wells Turbine Performance*, which experimentally investigated how blade solidity influences the aerodynamic characteristics of a Wells turbine.

A Wells turbine is a self-rectifying air turbine commonly used in Oscillating Water Column (OWC) wave-energy converters. Its symmetrical blade profiles allow the rotor to maintain the same rotational direction despite periodic reversals in airflow.

The original experimental investigation evaluated different rotor configurations, varying the number of blades from four to eight, and measured parameters including aerodynamic torque, pressure drop and efficiency.

The objective of this project was to reconstruct one of the experimental configurations, reproduce its operating conditions numerically and compare the CFD predictions against the experimental measurements.

Rather than developing a completely new turbine design, the focus was on reproducing an existing experimental setup and evaluating the reliability of the numerical model.

---

## 2. Project Objectives and Methodology

The numerical investigation was divided into several stages:

1. CAD reconstruction of the experimental turbine.
2. Computational domain development using a Multiple Reference Frame approach.
3. Mesh generation and near-wall refinement.
4. Definition of the physical models and boundary conditions.
5. Numerical quality assessment and mesh independence.
6. Post-processing of aerodynamic quantities.
7. Comparison against experimental performance data.

Each stage was developed to minimize differences between the numerical model and the original experimental configuration.

The main performance quantities used for comparison were:

- Aerodynamic torque.
- Pressure drop.
- Non-dimensional pressure coefficient.
- Non-dimensional torque coefficient.
- Turbine efficiency.

---

## 3. CAD Reconstruction

### 3.1 Turbine Geometry

The turbine geometry was reconstructed using the dimensions and geometric characteristics reported in the experimental investigation.

The selected configuration uses six symmetrical blades with a NACA 0015 profile.

The main geometric parameters considered during reconstruction were:

| Parameter | Value |
|---|---:|
| Airfoil | NACA 0015 |
| Blade count | 6 |
| Chord length | 72 mm |
| Solidity | 0.625 |
| Tip radius | 125 mm* |
| Hub radius | 95 mm* |
| Hub-to-tip ratio | 0.76* |

*The radii above should be checked against the final CAD model and original experimental reference before publication.*

### 3.2 Python-Based NACA 0015 Profile Generation

A particularly important part of the CAD reconstruction was obtaining an accurate NACA 0015 airfoil profile.

Instead of approximating the blade section manually using CAD splines, Python was used to generate the airfoil coordinates mathematically.

The NACA four-digit airfoil designation defines three geometric characteristics:

- First digit: maximum camber as a percentage of chord.
- Second digit: position of maximum camber along the chord.
- Last two digits: maximum thickness as a percentage of chord.

For NACA 0015:

- Maximum camber: 0%.
- Camber position: 0% of chord.
- Maximum thickness: 15% of chord.

This produces a symmetrical airfoil with identical upper and lower surface geometry.

The standard NACA four-digit thickness distribution was implemented in Python:

\[
\frac{y_t}{c}=5t\left[
0.2969\sqrt{\frac{x}{c}}
-0.1260\frac{x}{c}
-0.3516\left(\frac{x}{c}\right)^2
+0.2843\left(\frac{x}{c}\right)^3
-0.1015\left(\frac{x}{c}\right)^4
\right]
\]

Where:

- \(x/c\) is the normalized chordwise coordinate.
- \(y_t\) is the local half-thickness.
- \(t=0.15\) represents the maximum thickness ratio.
- \(c\) is the blade chord.

Python generated the upper and lower surface coordinates along the chord, producing a continuous airfoil geometry.

The resulting coordinate set could then be exported as a point distribution and imported into the CAD environment to construct the actual blade profile.

**Why Python was used:**

Generating the profile mathematically ensured that the reconstructed geometry followed the standard NACA definition rather than relying on manually positioned control points.

It also provided:

- Reproducible geometry generation.
- Accurate control over chord length and thickness.
- Consistent coordinates for CAD reconstruction.
- The possibility of generating alternative NACA profiles by changing the defining parameters.

This approach was particularly important because small geometric inaccuracies in the blade profile can influence pressure distribution, boundary-layer development and aerodynamic torque.

### 3.3 Blade Arrangement and Solidity

Six blades were arranged around the rotor axis with equal angular spacing.

The solidity was defined as:

\[
\sigma=\frac{Zc}{2\pi R}
\]

Where:

- \(Z\) is the number of blades.
- \(c\) is the blade chord.
- \(R\) is the reference radius used in the experimental definition.

The blade arrangement was reconstructed to preserve the original rotor configuration and its aerodynamic characteristics.

---

## 4. Computational Domain — Multiple Reference Frame

### 4.1 Domain Architecture

The computational domain was divided into three separate regions:

1. Upstream stationary duct.
2. Rotating region containing the turbine.
3. Downstream stationary duct.

This architecture allows the rotating turbine to be represented without requiring the entire computational domain to rotate.

The upstream region establishes the incoming flow before it reaches the rotor, while the downstream region provides space for the wake and flow disturbances to develop.

The rotating region contains the blade geometry and is assigned the appropriate rotational speed.

### 4.2 Multiple Reference Frame (MRF)

A steady Multiple Reference Frame formulation was selected to represent the rotating turbine.

In this approach, the governing equations are solved in different reference frames within the same computational domain.

The rotor region is assigned a rotating reference frame, while the inlet and outlet regions remain stationary.

This allows rotational effects to be included in a steady-state simulation without explicitly moving the mesh at every time step.

The main advantages of this approach are:

- Lower computational cost compared with transient sliding-mesh simulations.
- Ability to obtain steady aerodynamic performance predictions.
- Compatibility with stationary inlet and outlet boundaries.
- Simplified modelling of rotating turbomachinery.

The approach is particularly suitable when the objective is to investigate mean performance characteristics rather than transient blade-passing phenomena.

### 4.3 Rotational Periodicity

To reduce computational requirements, the complete rotor was not simulated.

Instead, a single-blade sector was considered.

For a six-blade rotor, the angular sector is:

\[
\theta=\frac{360^\circ}{Z}=60^\circ
\]

Periodic boundary conditions were applied to the two circumferential faces of the sector.

This allows the numerical model to represent the complete rotor under the assumption of rotational periodicity.

The resulting reduction in computational domain size significantly decreases the number of mesh elements and computational resources required.

---

## 5. Mesh Generation

### 5.1 Mesh Strategy

The computational domain was discretized using an unstructured hybrid mesh.

Although specialized turbomachinery meshing tools such as ANSYS TurboGrid would provide an alternative approach, the available ANSYS Student licensing capabilities influenced the choice of meshing methodology.

The selected strategy used unstructured elements throughout the domain, with additional refinement around the turbine blades.

The objective was to obtain sufficient spatial resolution in the regions where strong velocity and pressure gradients were expected.

Particular attention was given to:

- Blade leading and trailing edges.
- Blade suction and pressure surfaces.
- Near-wall boundary layers.
- Regions expected to experience flow separation.

### 5.2 Boundary-Layer Inflation

Inflation layers were generated along the blade surfaces to resolve the near-wall velocity gradients.

The selected configuration included:

| Parameter | Value |
|---|---:|
| Number of inflation layers | 15 |
| Growth rate | 1.2 |
| Target y+ | Approximately 1 |

The relatively small growth rate was selected to provide a gradual transition between the near-wall mesh and the surrounding volume mesh.

A target y+ close to unity was adopted to support the near-wall resolution requirements of the SST k-ω turbulence model.

This is particularly relevant for Wells turbine blades, where adverse pressure gradients and flow separation can strongly influence aerodynamic performance.

---

## 6. CFD Setup — ANSYS Fluent

### 6.1 Solver Configuration

The numerical simulations were performed using ANSYS Fluent with a pressure-based steady-state formulation.

The governing equations were discretized using the finite-volume method.

The main physical and numerical settings were:

| Parameter | Configuration |
|---|---|
| Solver | ANSYS Fluent |
| Formulation | Pressure-based |
| Simulation type | Steady-state |
| Rotating region | Multiple Reference Frame |
| Turbulence model | SST k-ω |
| Inlet | Velocity inlet |
| Inlet velocity range | 0–14 m/s |
| Outlet | Pressure outlet |
| Outlet gauge pressure | 0 Pa |
| Blade walls | No-slip |
| Frame interface | Frozen Frame |
| Pressure-velocity coupling | Verify final Fluent case |
| Spatial discretization | Second-order upwind |

### 6.2 Turbulence Model — SST k-ω

The Shear Stress Transport (SST) k-ω model was selected to simulate the turbulent flow around the turbine blades.

This model combines the near-wall accuracy of the k-ω formulation with the free-stream behaviour of the k-ε formulation.

Its use is particularly relevant for aerodynamic applications involving:

- Adverse pressure gradients.
- Boundary-layer development.
- Flow separation.
- Strong velocity gradients near solid surfaces.

Since the Wells turbine operates under aerodynamic conditions where blade loading and flow separation directly affect torque production, the SST k-ω model was considered an appropriate choice.

### 6.3 Boundary Conditions

A velocity inlet was defined upstream of the turbine.

The inlet velocity was varied between 0 and 14 m/s to investigate the turbine response under different operating conditions.

A pressure outlet was defined downstream with zero gauge static pressure.

The blade surfaces were assigned no-slip wall conditions.

The rotating reference frame was applied to the turbine region, allowing the solver to account for the rotational effects on the flow field.

### 6.4 Spatial Discretization

Second-order upwind discretization was selected for the momentum and turbulence transport equations.

Compared with first-order schemes, second-order discretization reduces numerical diffusion and provides improved spatial accuracy.

This is important when evaluating aerodynamic quantities such as pressure distribution, boundary-layer behaviour and blade loading.

---

## 7. Numerical Quality Assessment

Obtaining a converged solution is not sufficient to guarantee that a CFD result is physically reliable.

For this reason, several numerical quality indicators were considered.

### 7.1 Residual Convergence

The residuals of the governing equations were monitored during the iterative solution process.

Their evolution provides information about how well the numerical equations are being satisfied.

However, residual reduction alone cannot guarantee physical convergence.

For this reason, aerodynamic quantities such as torque and pressure drop must also be monitored throughout the iterations.

### 7.2 Near-Wall Resolution

The y+ distribution was evaluated to assess the quality of the mesh close to the blade surfaces.

This provides an indication of whether the first mesh cell is positioned appropriately for the selected turbulence model.

A target y+ around unity was adopted during mesh design.

### 7.3 Physical Consistency

The predicted aerodynamic quantities were evaluated to identify possible inconsistencies.

Particular attention was given to:

- Torque generation.
- Pressure drop across the turbine.
- Blade pressure distribution.
- Flow separation.
- Overall aerodynamic efficiency.

These quantities provide additional information about the physical behaviour of the simulated turbine.

---

## 8. Grid Independence Study

A mesh independence study was performed using the six-blade configuration at the peak-efficiency operating point.

The selected operating condition was:

\[
\lambda^*=0.15
\]

Four mesh densities were considered to investigate the sensitivity of the numerical solution to spatial discretization.

| Mesh | Elements |
|---|---:|
| Coarse | 1.2 million |
| Medium | 3.5 million |
| Fine | 7.8 million |
| Very Fine | 12.1 million |

The aerodynamic torque and turbine efficiency were selected as the primary comparison parameters.

The purpose of the study was to identify whether increasing mesh density produced significant changes in the predicted performance.

Once the variations between successive mesh levels became sufficiently small, additional refinement was considered to provide limited improvement relative to its computational cost.

The fine mesh was selected as the intended production configuration, subject to verification of the final torque and efficiency values.

---

## 9. Post-Processing and MATLAB Data Analysis

### 9.1 CFD Data Extraction

After completing the simulations, the relevant aerodynamic quantities were exported from ANSYS Fluent.

The extracted data included:

- Blade pressure distributions.
- Wall shear stress.
- Axial force.
- Aerodynamic torque.
- Pressure drop across the turbine.

These quantities were used to reconstruct the performance characteristics of the simulated turbine.

### 9.2 MATLAB Processing

A custom MATLAB workflow was developed to organize and process the exported simulation data.

The scripts were used to calculate the non-dimensional performance parameters required for comparison against the experimental investigation.

This separation between CFD simulation and performance analysis made it possible to process the numerical results consistently across different operating conditions.

### 9.3 Non-Dimensional Performance Parameters

The principal performance quantities were calculated using the following expressions.

**Flow coefficient**

\[
\phi=\frac{C_z}{\omega R}
\]

**Pressure coefficient**

\[
C_p=\frac{\Delta p}{\rho\omega^2R^2}
\]

**Torque coefficient**

\[
C_T=\frac{T}{\rho\omega^2R^5}
\]

**Aerodynamic efficiency**

\[
\eta=\frac{T\omega}{\Delta p Q}
\]

Where:

- \(C_z\) is the axial flow velocity.
- \(\omega\) is angular velocity.
- \(R\) is the reference radius.
- \(\Delta p\) is the pressure drop.
- \(\rho\) is air density.
- \(T\) is aerodynamic torque.
- \(Q\) is volumetric flow rate.

The reference radius and coefficient definitions must follow the original experimental thesis to ensure a consistent comparison.

### 9.4 Experimental Validation

The final objective was to compare the numerical predictions against the original experimental measurements.

Three main performance relationships were considered:

1. Torque coefficient versus flow coefficient.
2. Pressure coefficient versus flow coefficient.
3. Efficiency versus flow coefficient.

These comparisons provide insight into how accurately the numerical model reproduces the experimental aerodynamic behaviour.

The results also help identify potential limitations associated with the turbulence model, mesh resolution, rotating reference frame and boundary conditions.

---

## 10. Technologies and Tools

| Technology | Application |
|---|---|
| ANSYS Fluent | CFD simulations |
| ANSYS Meshing | Computational mesh generation |
| Python | Mathematical NACA airfoil coordinate generation |
| MATLAB | CFD data processing and performance analysis |
| SolidWorks | CAD reconstruction |
| Three.js | Interactive 3D turbine visualization |
| Chart.js | Experimental and numerical performance plots |
| HTML / CSS / JavaScript | Interactive project presentation |

---

## 11. Project Structure

The repository contains the resources associated with the numerical investigation and its presentation.

A possible organization is:

```text
Wells-CFD/
│
├── CAD/
│   ├── Geometry/
│   └── NACA_Profile/
│
├── CFD/
│   ├── Fluent_Cases/
│   ├── Mesh/
│   └── Results/
│
├── MATLAB/
│   ├── Post_Processing/
│   └── Performance_Analysis/
│
├── Python/
│   └── NACA_Generator/
│
├── images/
│
├── js/
│   └── main.js
│
├── index.html
│
└── README.md
```

---

## 12. Conclusion

This project combines CAD reconstruction, computational fluid dynamics and numerical data analysis to investigate the performance of a Wells turbine.

Starting from an existing experimental investigation, the turbine geometry was reconstructed, the computational domain was developed using a Multiple Reference Frame approach, and an unstructured hybrid mesh was generated to resolve the aerodynamic flow around the blades.

The numerical model was implemented in ANSYS Fluent using the SST k-ω turbulence model, with particular attention to near-wall resolution and numerical discretization.

Finally, a MATLAB post-processing workflow was developed to calculate the relevant non-dimensional performance parameters and compare the numerical predictions against experimental measurements.

The project provided practical experience in the complete CFD workflow, from mathematical geometry generation and CAD modelling to numerical simulation, mesh assessment and aerodynamic performance analysis.

---

**Author:** Mattia Sanna  
**Repository:** [Wells-CFD](https://github.com/MattiaSanna/Wells-CFD)
