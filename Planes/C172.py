####################################################################################################
# Description:		Design geometry for a Cessna 172 aircraft
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class C172():

	name = "C172"

	mass = 1000 # kg
	mass_matrix = np.identity(3) * mass

	wingarea = 16.00 # m^2
	wingspan = 11.00 # m
	chord = 1.454545 # m

	CDi = 0.027 # CD due to induced drag
