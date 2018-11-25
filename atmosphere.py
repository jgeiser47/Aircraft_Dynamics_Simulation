####################################################################################################
# Description:		Atmosphere class which represents atmosphere in which aircraft are flying
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import numpy as np
import sim_math as M

class Atmosphere():

	rho = 1.225 # kg/m^3
	speed_of_sound = 340.294 # m/s

	# Array of wind gusts
	wind = []

	# Add a wind object to array of wind
	def add_wind(self, wind_gust):
		self.wind.append(wind_gust)


	# Updates atmospheric properties (density, speed of sound, etc.) based on the current height of the aircraft
	def Update_Atmo(self, height, TIME):

		self.rho = M.LUT_Linear_Interpolate_1D('LUTs/Atmosphere_Density.csv', height)
		self.speed_of_sound = M.LUT_Linear_Interpolate_1D('LUTs/Atmosphere_SpeedOfSound.csv', height)

		# Determine if a wind gust is currently active based on the current timestep
		for wind_gust in self.wind:
			if (TIME >= wind_gust.start_time and TIME <= wind_gust.end_time):
				wind_gust.active = True
			else:
				wind_gust.active = False
			
# Wind class represents a single gust of wind with an input start/stop time and force in each component direction
class Wind():
	def __init__(self): 
		self.active = False
		self.start_time = 0
		self.end_time = 0
		self.wind_force = np.array([0, 0, 0])
