#!/usr/bin/env python

####################################################################################################
# Description:		Executable input deck to vary inputs and run simulation
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import numpy as np

from aircraft import Aircraft
from atmosphere import Atmosphere, Wind
from constants import Constants
import sim_setup

from Planes.B737 import B737
from Planes.C172 import C172
from Planes.T38 import T38

# Initialization of objects used in overall sim architecture
SIM = sim_setup.Sim_Parameters()
CONSTANTS = Constants()
Atmosphere = Atmosphere()
plane1 = Aircraft()

####################################################################################################
# BEGIN INPUT FIELDS
####################################################################################################

# Modify simulation parameters
SIM.START_TIME = 0.0
SIM.END_TIME = 2000.0
SIM.DELTA_T = 2

# Modify aircraft inital conditions 

# Choose airplane type - B737, C172, T38
plane1.design = B737()

# Input initial position vector (ex: [0, 0, 10000] to begin at 10000 m altitude)
plane1.state.pos_ENU = np.array([0, 0, 10000])

# Input initial velocity vector (ex: [260, 0, 0] for an initial velocity of 260 m/s eastward
plane1.state.vel_ENU = np.array([260, 0, 0])

# Input angle of attack (in radians)
plane1.aero.AoA = 0.02

Wind_Gust_1 = Wind()
Wind_Gust_1.start_time = 10
Wind_Gust_1.end_time = 200
Wind_Gust_1.wind_force = np.array([0, 1000, 0])
Atmosphere.add_wind(Wind_Gust_1)

Wind_Gust_2 = Wind()
Wind_Gust_2.start_time = 150
Wind_Gust_2.end_time = 1000
Wind_Gust_2.wind_force = np.array([750, 4000, 0])
Atmosphere.add_wind(Wind_Gust_2)
	
####################################################################################################
# END INPUT FIELDS
####################################################################################################

# Command to begin running of simulation after input deck
sim_setup.Run_Sim(SIM, CONSTANTS, Atmosphere, plane1)

