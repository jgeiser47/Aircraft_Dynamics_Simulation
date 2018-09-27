#!/usr/bin/env python

####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018


import numpy as np

from aircraft import Aircraft
import sim_math
import log_data

class Sim_Parameters():
	# Input simulation start time, stop time, step size

	START_TIME = 0
	END_TIME = 100
	DELTA_T = 0.1 

def Run_Sim(SIM, plane1):
	TIME = SIM.START_TIME
	log_data.Log_Setup()
	log_data.Log_Output(TIME, plane1)
	while (TIME <= SIM.END_TIME):

		# Calculate forces on aircraft at current timestep
		plane1.Calc_Forces()

		# Given forces, update accelerations
		plane1.state.acc_ned = (np.linalg.inv(plane1.mass_matrix)).dot(plane1.forces.net_force)

		# Given accelerations, update velocities
		plane1.state.vel_ned = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.acc_ned, plane1.state.vel_ned)	

		# Given veolocities, update positions
		plane1.state.pos_ned = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.vel_ned, plane1.state.pos_ned)	
	
		# Log output
		log_data.Log_Output(TIME, plane1)

		# Increment time
		TIME += SIM.DELTA_T


