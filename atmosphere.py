####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np
import sim_math as M

class Atmosphere():

	rho = 1.225 # kg/m^3

	def Update_Atmo(self, height):
		self.rho = M.LUT_Linear_Interpolate_1D('LUTs/Atmosphere_Density.csv', height)
