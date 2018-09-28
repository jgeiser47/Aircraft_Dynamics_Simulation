####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class B737():

	mass = 1500
	mass_matrix = np.identity(3) * mass
