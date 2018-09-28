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

def Run_Sim(SIM, CONSTANTS, Atmosphere, plane1):
	TIME = SIM.START_TIME

	# Update forces on aircraft for current timestep
	plane1.Calc_Forces()

	# Given forces, update accelerations
	plane1.state.acc_ENU = (np.linalg.inv(plane1.design.mass_matrix)).dot(plane1.forces.net_force_ENU)

	# Setup output logging and log output for start time
	log_data.Log_Setup()
	log_data.Log_Output(TIME, plane1)

	# Iterate until simulation stop time
	while (TIME <= SIM.END_TIME):

		# Given accelerations, update velocities
		plane1.state.vel_ENU = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.acc_ENU, plane1.state.vel_ENU)	

		# Given veolocities, update positions
		plane1.state.pos_ENU = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.vel_ENU, plane1.state.pos_ENU)	

		# Update forces on aircraft for current timestep
		plane1.Calc_Forces()

		# Given forces, update accelerations
		plane1.state.acc_ENU = (np.linalg.inv(plane1.design.mass_matrix)).dot(plane1.forces.net_force_ENU)

		# Log output
		log_data.Log_Output(TIME, plane1)

		# Display percentage completion to console
		printProgressBar(TIME, SIM.END_TIME, CONSTANTS.TOLERANCE, prefix = 'Progress:', suffix = 'Complete', length = 50)

		# Increment time
		TIME += SIM.DELTA_T

	print("\n")
	print("\033[92m" + "Simulation Complete - Data output to post_processing/output.csv" + "\033[0m")


# Print iterations progress
def printProgressBar (iteration, total, tolerance, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
	"""
	Call in a loop to create terminal progress bar
	@params:
	    iteration   - Required  : current iteration (Int)
	    total       - Required  : total iterations (Int)
	    prefix      - Optional  : prefix string (Str)
	    suffix      - Optional  : suffix string (Str)
	    decimals    - Optional  : positive number of decimals in percent complete (Int)
	    length      - Optional  : character length of bar (Int)
	    fill        - Optional  : bar fill character (Str)
	"""
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = round(length * iteration / total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

	# Print New Line on Complete
	if iteration >= total - tolerance: 
		print()
