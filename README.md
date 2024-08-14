# DFT Calculations for Oxygen Evolution Reaction (OER) using GPAW & ASE

This repository contains a Python script designed to perform Density Functional Theory (DFT) calculations to obtain the Oxygen Evolution Reaction (OER) free energy. The calculations are conducted using **GPAW**, and **ASE** (Atomic Simulation Environment) is used for system design.

**Note**: This script uses simplified models with several approximations to reduce computational cost. Therefore, it is not intended for production use, and the energy values may need to be more accurate. The primary goal of this script is educational, demonstrating how to use DFT calculations for plotting free energy diagrams of an electrochemical reaction.

## Getting Started

### Prerequisites

Make sure you have the following Python packages installed:

- **GPAW**
- **ASE**

You can install these dependencies using pip:

```bash
pip install gpaw ase
```

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/OER-Free-Energy-DFT.git
```

2. Navigate to the project directory:

```bash
cd your-repository-name
```

### Usage

To perform the DFT calculations and generate free energy diagrams for the Oxygen Evolution Reaction:

1. Ensure that your atomic system is properly configured within the script.
2. Run the script using Python:

```bash
python3.7 DFT_OER.py
```

### Input and Output

- **Input**: The script requires configuration of various parameters, such as the atomic structure, exchange-correlation functional, and calculation settings, which can be modified directly in the script.
- **Output**: The script outputs free energy values that can be used to plot a free energy diagram for the electrochemical reaction.

### Example Workflow

1. **System Setup**: Define your atomic system using ASE.
2. **DFT Calculation**: Configure the GPAW calculator parameters within the script.
3. **Execution**: Run the script to perform the DFT calculations.
4. **Plotting**: Use the output data to create free energy diagrams.

## Additional Resources

For more information on using DFT calculations for electrocatalysis, including the Oxygen Evolution Reaction (OER), Oxygen Reduction Reaction (ORR), and Hydrogen Evolution Reaction (HER), please refer to the following article:

1. Vu, Tuan V., Nguyen N. Hieu, Dat D. Vo, A. I. Kartamyshev, Hien D. Tong, Thuat T. Trinh, Vo Khuong Dien, Zakaryae Haman, Poulumi Dey, and Nabil Khossossi. "2D Ge2Se2P4 Monolayer: A Versatile Photocatalyst for Sustainable Water Splitting." The Journal of Physical Chemistry C 128, no. 10 (2024): 4245-4257.

2. Khossossi, N., Banerjee, A., & Dey, P. (2023). Synergistic effect of Fe/Co-doping and electric field in Niobium Diboride for boosting hydrogen production. Surfaces and Interfaces, 39, 102972.

3. Singh, Deobrat, Nabil Khossossi, Abdelmajid Ainane, and Rajeev Ahuja. "Modulation of 2D GaS/BTe vdW heterostructure as an efficient HER catalyst under external electric field influence." Catalysis Today 370 (2021): 14-25.
