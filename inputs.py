#!/usr/bin/env python

####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

from aircraft import Aircraft
import sim_setup
import sim_math
import log_data


SIM = sim_setup.Sim_Parameters()

SIM.START_TIME = 0.0
SIM.END_TIME = 200.0
SIM.DELTA_T = 0.25


plane1 = Aircraft()
plane1.forces.net_force = np.array([500, 3000, 0])


sim_setup.Run_Sim(SIM, plane1)
