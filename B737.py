####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class B737():

	mass = 1500 # 41413 # kg
	mass_matrix = np.identity(3) * mass

	wingarea = 124.6 # m^2
	wingspan = 34.32 # m
	chord = 3.630536 # m
