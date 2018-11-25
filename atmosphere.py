####################################################################################################
# Description:		Atmosphere class which represents atmosphere in which aircraft are flying
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import numpy as np
import sim_math as M

class Atmosphere():

	rho = 1.225 # kg/m^3
	speed_of_sound = 340.294 # m/s

	# Updates atmospheric properties (density, speed of sound, etc.) based on the current height of the aircraft
	def Update_Atmo(self, height):

		self.rho = M.LUT_Linear_Interpolate_1D('LUTs/Atmosphere_Density.csv', height)
		self.speed_of_sound = M.LUT_Linear_Interpolate_1D('LUTs/Atmosphere_SpeedOfSound.csv', height)
