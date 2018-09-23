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

		plane1.Calc_Forces()

		plane1.state.acc_ned = (np.linalg.inv(plane1.mass_matrix)).dot(plane1.forces.net_force)

		plane1.state.vel_ned = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.acc_ned, plane1.state.vel_ned)	
		plane1.state.pos_ned = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.vel_ned, plane1.state.pos_ned)	
	

		log_data.Log_Output(TIME, plane1)
		TIME += SIM.DELTA_T


	# Given forces, calculate accelerations
	# Given accelerations, update velocities
	# Given velocities, update positions
	# Update forces	
	# Log output


plane1 = Aircraft()
plane1.forces.net_force = np.array([500, 3000, 0])


SIM = Sim_Parameters()
Run_Sim(SIM, plane1)
