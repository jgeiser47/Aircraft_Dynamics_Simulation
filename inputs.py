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

plane1 = Aircraft()
plane1.forces.net_force = np.array([500, 3000, 0])


SIM = sim_setup.Sim_Parameters()
sim_setup.Run_Sim(SIM, plane1)
