####################################################################################################
# Description:		Design geometry for a Boeing 737 aircraft
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class B737():

	name = "B737"

	mass = 35000 # kg
	mass_matrix = np.identity(3) * mass

	wingarea = 124.6 # m^2
	wingspan = 34.32 # m
	chord = 3.630536 # m

	max_thrust = 242800 # N

	CDi = 0.043 # CD due to induced drag


	# Specs found online
	# 
	# Cruise velocity - 260 m/s
	# Cruis Altitude - 9145 m
	# Max Mach Number - 0.82
