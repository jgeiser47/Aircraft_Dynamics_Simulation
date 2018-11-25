####################################################################################################
# Description:		Setup and control output CSV logging of simulation data
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import os

# Setup of CSV logging
def Log_Setup():

	# If an output.csv file already exists, delete it
	Filepath = "post_processing/output.csv"	
	if os.path.exists(Filepath):
		os.remove(Filepath)
		print("(Note: Old post_processing/output.csv file deleted)\n")

	# Create a new output.csv file and add headers to the first row of the CSV
	fo = open(Filepath, "w")
	headers = [
		"TIME",
		"Aircraft.state.pos_ENU[0]",
		"Aircraft.state.pos_ENU[1]",
		"Aircraft.state.pos_ENU[2]",
		"Aircraft.state.pos_mag",
		"Aircraft.state.vel_ENU[0]",
		"Aircraft.state.vel_ENU[1]",
		"Aircraft.state.vel_ENU[2]",
		"Aircraft.state.vel_mag",
		"Aircraft.state.Mach",
		"Aircraft.state.acc_ENU[0]",
		"Aircraft.state.acc_ENU[1]",
		"Aircraft.state.acc_ENU[2]",
		"Aircraft.state.acc_mag",
		"Aircraft.forces.lift_ENU[0]",
		"Aircraft.forces.lift_ENU[1]",
		"Aircraft.forces.lift_ENU[2]",
		"Aircraft.forces.lift_mag",
		"Aircraft.forces.weight_ENU[0]",
		"Aircraft.forces.weight_ENU[1]",
		"Aircraft.forces.weight_ENU[2]",
		"Aircraft.forces.weight_mag",
		"Aircraft.forces.drag_ENU[0]",
		"Aircraft.forces.drag_ENU[1]",
		"Aircraft.forces.drag_ENU[2]",
		"Aircraft.forces.drag_mag",
		"Aircraft.forces.thrust_ENU[0]",
		"Aircraft.forces.thrust_ENU[1]",
		"Aircraft.forces.thrust_ENU[2]",
		"Aircraft.forces.thrust_mag",
		"Aircraft.forces.net_force_ENU[0]",
		"Aircraft.forces.net_force_ENU[1]",
		"Aircraft.forces.net_force_ENU[2]",
		"Aircraft.forces.net_force_mag",
		"Aircraft.aero.CD",
		"Atmosphere.rho"
	]

	fo.write(",".join(headers) + "\n")
	fo.close()



# Log data to output CSV file
def Log_Output(data, TIME, Atmosphere, Aircraft):

	# Collect data from current timestep
	data_entry = [
		TIME								,
		Aircraft.state.pos_ENU[0]					,
		Aircraft.state.pos_ENU[1]					,
		Aircraft.state.pos_ENU[2]					,
		Aircraft.state.pos_mag						,
		Aircraft.state.vel_ENU[0]					,
		Aircraft.state.vel_ENU[1]					,
		Aircraft.state.vel_ENU[2]					,
		Aircraft.state.vel_mag						,
		Aircraft.state.Mach						,
		Aircraft.state.acc_ENU[0]					,
		Aircraft.state.acc_ENU[1]					,
		Aircraft.state.acc_ENU[2]					,
		Aircraft.state.acc_mag						,
		Aircraft.forces.lift_ENU[0]					,
		Aircraft.forces.lift_ENU[1]					,
		Aircraft.forces.lift_ENU[2]					,
		Aircraft.forces.lift_mag					,
		Aircraft.forces.weight_ENU[0]					,
		Aircraft.forces.weight_ENU[1]					,
		Aircraft.forces.weight_ENU[2]					,
		Aircraft.forces.weight_mag					,
		Aircraft.forces.drag_ENU[0]					,
		Aircraft.forces.drag_ENU[1]					,
		Aircraft.forces.drag_ENU[2]					,
		Aircraft.forces.drag_mag					,
		Aircraft.forces.thrust_ENU[0]					,
		Aircraft.forces.thrust_ENU[1]					,
		Aircraft.forces.thrust_ENU[2]					,
		Aircraft.forces.thrust_mag					,
		Aircraft.forces.net_force_ENU[0]				,
		Aircraft.forces.net_force_ENU[1]				,
		Aircraft.forces.net_force_ENU[2]				,
		Aircraft.forces.net_force_mag					,
		Aircraft.aero.CD						,
		Atmosphere.rho							
	]

	# Add data from current timestep to data variable
	data_entry = ",".join(map(str, data_entry))
	data += data_entry + "\n"

	# Open CSV and add date to file only if data string is sufficently large (improves runtime efficiency)
	if len(data) >= 5000: 
		Log_Output_To_File(data)
		data = ""

	return data

# Actual logging of data to output CSV file
def Log_Output_To_File(data):
	Filepath = "post_processing/output.csv"
	fo = open(Filepath, "a")

	fo.write(data)
	fo.close()
