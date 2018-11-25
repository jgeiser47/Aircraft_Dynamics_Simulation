####################################################################################################
# Description:		Design geometry for a T-38 aircraft
#	
# Cruise Velocity:	362 m/s
# Cruise Altitude: 	16700 m
#
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class T38():

	name = "T38"

	mass = 4000 # kg
	mass_matrix = np.identity(3) * mass

	wingarea = 15.79 # m^2
	wingspan = 7.600 # m
	chord = 2.077632 # m

	max_thrust = 25800 # N

	CDi = 0.10 # CD due to induced drag

