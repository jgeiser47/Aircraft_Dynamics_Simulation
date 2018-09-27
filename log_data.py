#!/usr/bin/env python

####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import os
	
def Log_Setup():
	Filepath = "post_processing/output.csv"	
	if os.path.exists(Filepath):
		os.remove(Filepath)
		print("(Note: Old post_processing/output.csv file deleted)\n")

	fo = open(Filepath, "w")
	headers = [
		"TIME",
		"Aircraft.state.pos_ned[0]",
		"Aircraft.state.pos_ned[1]",
		"Aircraft.state.pos_ned[2]",
		"Aircraft.state.vel_ned[0]",
		"Aircraft.state.vel_ned[1]",
		"Aircraft.state.vel_ned[2]",
		"Aircraft.state.acc_ned[0]",
		"Aircraft.state.acc_ned[1]",
		"Aircraft.state.acc_ned[2]",
		"Aircraft.forces.net_force[0]",
		"Aircraft.forces.net_force[1]",
		"Aircraft.forces.net_force[2]"
	]

	fo.write(",".join(headers) + "\n")
	fo.close()



# Log data from the current time step to output.csv
def Log_Output(TIME, Aircraft):
	# Log data from the current time step to output.csv

	Filepath = "post_processing/output.csv"	
	fo = open(Filepath, "a")

	data = [
		TIME,
		Aircraft.state.pos_ned[0],
		Aircraft.state.pos_ned[1],
		Aircraft.state.pos_ned[2],
		Aircraft.state.vel_ned[0],
		Aircraft.state.vel_ned[1],
		Aircraft.state.vel_ned[2],
		Aircraft.state.acc_ned[0],
		Aircraft.state.acc_ned[1],
		Aircraft.state.acc_ned[2],
		Aircraft.forces.net_force[0],
		Aircraft.forces.net_force[1],
		Aircraft.forces.net_force[2]
	]

	data = ",".join(map(str, data))

	fo.write(data + "\n")
	fo.close()


