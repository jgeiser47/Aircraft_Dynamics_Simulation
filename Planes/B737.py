####################################################################################################
# Description:		Design geometry for a Boeing 737 aircraft
#	
# Cruise Velocity:	260 m/s
# Cruise Altitude: 	9145 m
#
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import numpy as np

class B737():

	name = "B737"

	mass = 50000 # kg
	mass_matrix = np.identity(3) * mass

	wingarea = 124.6 # m^2
	wingspan = 34.32 # m
	chord = 3.630536 # m

	max_thrust = 242800 # N

	CDi = 0.043 # CD due to induced drag

