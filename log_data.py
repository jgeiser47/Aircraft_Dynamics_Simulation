#!/usr/bin/env python

####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import os
	
def Log_Setup():
	if os.path.exists("post_processing/output.csv"):
		os.remove("post_processing/output.csv")
		print("File output.csv deleted")

	fo = open("post_processing/output.csv", "w")
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

	fo = open("post_processing/output.csv", "a")

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


