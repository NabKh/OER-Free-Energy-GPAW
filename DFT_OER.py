#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author: Nabil Khossossi
Website: https://sustai-nabil.com/
Email: n.khossossi@tudelft.nl

"""

from ase import Atoms
from ase.build import fcc111, molecule
from ase.constraints import FixAtoms
from ase.visualize import view
from ase.optimize import QuasiNewton
from gpaw import GPAW, PW, FermiDirac
import time


"""
Step 1: Calculations to obtain the free energy of the Ni(111) slab
- We create a Ni(111) slab with a lattice constant of 3.52 Å
- 2.0 Å are used for the vacuum, which is a low value, but higher values increased a lot the calculation time
- The slab is then centered with a 2.0 Å vacuum
- We visualize the slab structure
"""

lattice_constant_Ni = 3.52
slab = fcc111("Ni", a=lattice_constant_Ni, size=(2,2,2))
slab.center(vacuum=2.0)
view(slab)

# Step 2: Setting up the GPAW calculator with RPBE exchange-correlation functional
calculator = GPAW(xc='RPBE', mode=PW(350), kpts={'size': (4,4,1), 'gamma': True}, h=0.2, occupations=FermiDirac(0.1))
slab.set_calculator(calculator)

"""Here we fix the position of 7 of 8 atoms of the slab to facilitate the calculation"""
constraint = FixAtoms(indices=[0,1,2,3,5,6,7])
slab.set_constraint(constraint)


# Step 3: Structure optimization using Quasi-Newton algorithm
# - We save the optimized structure in the trajectory file
# - Optimization will stop when force between atoms is lower than fmax: 0.05 eV
# - We can also record the time taken for the calculation
dyn = QuasiNewton(slab, trajectory='Ni.traj')
t = time.time()
dyn.run(fmax=0.05)
print('Calculation time: {} min.'.format((time.time() - t) / 60))

# Step 4: Get the final energy of the optimized slab structure
e_slab = slab.get_potential_energy()
print("Ni(111) energy: ", e_slab, " eV")



"""
Step 5: Calculations to obtain the free energy of the OH adsorbed on the Ni slab
- We create an OH molecule
- We create a new Ni(111) slab
- We place the OH molecule close to a top Ni atom where it would bind
- The slab is centered again with a 2.0 Å vacuum
- We visualize the slab structure with the OH adsorbate
"""

# Creating the OH molecule and a new Ni slab
oh_molecule = Atoms('OH', positions=[(0, 0, 0), (0, -0.763, 0.596)])
slabNi = fcc111("Ni", a=lattice_constant_Ni, size=(2,2,2))

# Placing the molecule close to a top Ni atom, where it would bind
p = slabNi.positions[4]
oh_molecule.translate(p + (0, 0, 1.5))
slabOH = slabNi + oh_molecule
slabOH.center(vacuum=2.0)

# We fix again some atoms of the slab to speed up calculations
constraint = FixAtoms(indices=[0,1,2,3,5,6,7])
slabOH.set_constraint(constraint)
view(slabOH)

# Step 6: Set the calculator and optimize the structure
slabOH.set_calculator(calculator)

dynOH = QuasiNewton(slabOH, trajectory="OH_Ni.traj", )
t = time.time()
dynOH.run(fmax=0.05)
print('Calculation time: {} min.'.format((time.time() - t) / 60))

# Step 7: Get the final energy and bond lengths
e_slabOH = slabOH.get_potential_energy()
print("OH on Ni(111) energy: ", e_slabOH, " eV")
print("bond Ni-O: ", slabOH.get_distance(4,8))
print("bond O-H: ", slabOH.get_distance(8,9))


"""
Step 8: Calculations to get the free energy of the O intermediate adsorbed on the Ni surface
- We create an O atom
- We create a new Ni(111) slab
- We place the O atom close to a top Ni atom where it would bind
- The slab is centered again with a 2.0 Å vacuum
- We visualize the slab structure with the O adsorbate
"""

o_molecule = Atoms('O', positions=[(0, 0, 0)])
slabNi = fcc111("Ni", a=lattice_constant_Ni, size=(2,2,2))
p = slabNi.positions[4]
o_molecule.translate(p + (0, 0, 1.5))
slabO = slabNi + o_molecule
slabO.center(vacuum=2.0)

# Fixing atoms of the slab again
constraint = FixAtoms(indices=[0,1,2,3,5,6,7])
slabO.set_constraint(constraint)
view(slabO)

# Set the calculator and optimize the structure
slabO.set_calculator(calculator)
dynO = QuasiNewton(slabO, trajectory="O_Ni.traj", )
t = time.time()
dynO.run(fmax=0.05)
print('Calculation time: {} min.'.format((time.time() - t) / 60))

# Get the final energy and bond lengths
e_slabO = slabO.get_potential_energy()
print("O on Ni(111) energy: ", e_slabO, " eV")
view(slabO)
print("bond Ni-O: ", slabO.get_distance(4,8))


"""
Step 9: Calculations to get the free energy of the OOH intermediate adsorbed on the Ni surface
- We create an OOH molecule
- We create a new Ni(111) slab
- We place the OOH molecule close to a top Ni atom where it would bind
- The slab is centered again with a 2.0 Å vacuum
- We visualize the slab structure with the OOH adsorbate
"""

ooh_molecule = Atoms('OOH', positions=[(0, 0, 0), (0, 0, 1.4), (0, -0.763, 2.0)])
slabNi = fcc111("Ni", a=lattice_constant_Ni, size=(2,2,2))
p = slabNi.positions[4]
ooh_molecule.translate(p + (0, 0, 1.5))
slabOOH = slabNi + ooh_molecule
slabOOH.center(vacuum=2.0)

# Fixing atoms of the slab again
constraint = FixAtoms(indices=[0,1,2,3,5,6,7])
slabOOH.set_constraint(constraint)
view(slabOOH)

# Set the calculator and optimize the structure
slabOOH.set_calculator(calculator)
dynOOH = QuasiNewton(slabOOH, trajectory="OOH_Ni.traj", )
t = time.time()
dynOOH.run(fmax=0.05)
print('Calculation time: {} min.'.format((time.time() - t) / 60))

# Get the final energy and bond lengths
e_slabO = slabOOH.get_potential_energy()
print("OOH on Ni(111) energy: ", e_slabO, " eV")
view(slabOOH)
print("bond Ni-O: ", slabOOH.get_distance(4,8))




"""
Step 10: Calculations to get the free energy of H2O and H2
These are needed to calculate the free energies of the reaction
"""

# Setting up a new GPAW calculator for isolated molecules
calculator2 = GPAW(xc='RPBE', mode=PW(350), h=0.2, occupations=FermiDirac(0.1))

# Creating and optimizing the H2O molecule
h2o_molecule = molecule("H2O")
h2o_molecule.set_cell(slab.get_cell())
h2o_molecule.center(vacuum=2.0)
h2o_molecule.set_calculator(calculator2)
dynH2O = QuasiNewton(h2o_molecule, trajectory='H2O.traj')
t = time.time()
dynH2O.run(fmax=0.05)
print('Calculation time: {} min.'.format((time.time() - t) / 60))
e_h2o = h2o_molecule.get_potential_energy()
print("H2O energy: ", e_h2o, " eV")
print("O-H bond length: ", h2o_molecule.get_distance(0,1))

# Creating and optimizing the H2 molecule
h2_molecule = molecule("H2")
h2_molecule.set_cell(slab.get_cell())
h2_molecule.center(vacuum=2.0)
h2_molecule.set_calculator(calculator2)
dynH2 = QuasiNewton(h2_molecule, trajectory='H2.traj')
t = time.time()
dynH2.run(fmax=0.05)
print('Calculation time: {} min.'.format((time.time() - t) / 60))
e_h2 = h2_molecule.get_potential_energy()
print("H2 energy: ", e_h2, " eV")
print("H-H bond length: ", h2_molecule.get_distance(0,1))

