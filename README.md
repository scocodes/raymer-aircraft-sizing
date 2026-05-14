Raymer Aircraft Sizing

Overview

This project implements a Class II aircraft weight estimation and mission sizing framework based on empirical methods presented in Raymer aircraft design methodology.

The repository combines:

* Raymer component weight estimation equations
* Mission fuel burn analysis
* Breguet range and endurance calculations
* MTOW convergence iteration
* Aerodynamic interpolation from imported datasets
* Modular object-oriented Python architecture

The project is intended for conceptual aircraft design and preliminary sizing studies.

⸻

Features

* Class II Raymer weight estimation
* Wing, fuselage, tail, landing gear and systems weight calculations
* Mission fuel burn estimation
* Breguet range and loiter analysis
* MTOW iterative convergence solver
* Aerodynamic data interpolation
* Convergence plotting and visualisation
* Modular Python repository structure

⸻

Repository Structure

raymer-aircraft-sizing/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   └── optimum clld.xlsx
│
└── src/
    ├── __init__.py
    ├── conversions.py
    ├── data_import.py
    ├── mission_analysis.py
    ├── raymer_equations.py
    └── raymer_variables.py

⸻

Methodology

1. Raymer Weight Estimation

The project implements empirical Class II weight estimation equations for major aircraft components including:

* Wing
* Horizontal tail
* Vertical tail
* Fuselage
* Landing gear
* Fuel systems
* Flight controls
* Electrical systems
* Avionics
* Hydraulic systems

Aircraft component weights are combined to estimate operating empty weight (OEW).

⸻

2. Mission Analysis

Mission fuel burn is estimated using:

* Mission fuel fractions
* Breguet range equation
* Breguet endurance equation
* Cruise and loiter aerodynamic conditions

Aerodynamic performance is interpolated from imported aerodynamic datasets.

⸻

3. MTOW Iteration

The sizing loop iteratively updates:

* Empty weight
* Fuel weight
* Total aircraft weight

until convergence is achieved below a specified error threshold.

Convergence behaviour is visualised using error-history plots.

⸻

Running the Project

Run the project from the repository root:

python main.py

⸻

Dependencies

Install required packages using:

pip install -r requirements.txt

⸻

Example Output

The project outputs:

* Component weight breakdowns
* Fuel weight estimates
* MTOW convergence histories
* Error convergence plots

⸻

Future Work

Potential future improvements include:

* Constraint analysis integration
* Drag polar modelling
* Multi-mission optimisation
* Sensitivity analysis
* Parametric aircraft studies
* GUI/dashboard integration
* Machine learning surrogate sizing models

⸻

Author

Scott Collins
University of Southampton
Aeronautics and Astronautics