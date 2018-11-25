####################################################################################################
# Description:		Defines main architecture of simulation and commands to run at each timestep
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import numpy as np

from aircraft import Aircraft
import sim_math
import log_data

# Default values for simulation start time, stop time, and step size
class Sim_Parameters():

	START_TIME = 0
	END_TIME = 100
	DELTA_T = 0.1 

# Main function that defines overall flow of simulation run commands
def Run_Sim(SIM, CONSTANTS, Atmosphere, plane1):

	# Begin at input start time
	TIME = SIM.START_TIME

	# Determine direction of aircraft based on input initial velocity vector
	plane1.state.direction = plane1.state.vel_ENU / np.linalg.norm(plane1.state.vel_ENU)

	# Update atmosphere conditions
	Atmosphere.Update_Atmo(plane1.state.pos_ENU[2])

	# Update forces on aircraft for current timestep
	plane1.Calc_Forces(CONSTANTS, Atmosphere)

	# Given forces, update accelerations
	plane1.state.acc_ENU = (np.linalg.inv(plane1.design.mass_matrix)).dot(plane1.forces.net_force_ENU)
	plane1.state.acc_mag = np.linalg.norm(plane1.state.acc_ENU)

	# Setup output logging and log output for start time
	log_data.Log_Setup()
	data = log_data.Log_Output("", TIME, Atmosphere, plane1)

	# Iterate until simulation stop time or aircraft crashes into ground
	while (TIME < SIM.END_TIME - CONSTANTS.TOLERANCE and plane1.state.pos_ENU[2] >= 0):

		# Update atmosphere conditions
		Atmosphere.Update_Atmo(plane1.state.pos_ENU[2])
		
		# Given accelerations, update velocities
		plane1.state.vel_ENU = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.acc_ENU, plane1.state.vel_ENU)	
		plane1.state.vel_mag = np.linalg.norm(plane1.state.vel_ENU)
		plane1.state.Mach = plane1.state.vel_mag / Atmosphere.speed_of_sound 

		# Given veolocities, update positions
		plane1.state.pos_ENU = sim_math.Integrate_Linear(SIM.DELTA_T, plane1.state.vel_ENU, plane1.state.pos_ENU)	
		plane1.state.pos_mag = np.linalg.norm(plane1.state.pos_ENU)

		# Update forces on aircraft for current timestep
		plane1.Calc_Forces(CONSTANTS, Atmosphere)

		# Given forces, update accelerations
		plane1.state.acc_ENU = (np.linalg.inv(plane1.design.mass_matrix)).dot(plane1.forces.net_force_ENU)
		plane1.state.acc_mag = np.linalg.norm(plane1.state.acc_ENU)

		# Increment time
		TIME += SIM.DELTA_T

		# Log output
		data = log_data.Log_Output(data, TIME, Atmosphere, plane1)

		# Display percentage completion to console
		printProgressBar(TIME, SIM.END_TIME, CONSTANTS.TOLERANCE, prefix = 'Progress:', suffix = 'Complete', length = 50)

	# Final logging of data to output CSV file
	log_data.Log_Output_To_File(data)
	print("\n")

	# Print a success or failure message to terminal based on if the simulation successfully reached the end time
	if (plane1.state.pos_ENU[2] <= 0):
		print("\033[91m" + "Simulation stopped due to aircraft altitude reaching 0 - Data output to post_processing/output.csv" + "\033[0m")	
	else:
		print("\033[92m" + "Simulation Complete - Data output to post_processing/output.csv" + "\033[0m")


# Print iterations progress to terminal
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
