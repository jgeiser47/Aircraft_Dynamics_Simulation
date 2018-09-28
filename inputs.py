#!/usr/bin/env python

####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

from aircraft import Aircraft
from atmosphere import Atmosphere
from constants import Constants
from B737 import B737
import sim_setup



SIM = sim_setup.Sim_Parameters()

SIM.START_TIME = 0.0
SIM.END_TIME = 200.0
SIM.DELTA_T = 0.1

CONSTANTS = Constants()

Atmosphere = Atmosphere()

plane1 = Aircraft()

plane1.design = B737()
plane1.state.pos_ENU = np.array([0, 0, 0])
plane1.state.vel_ENU = np.array([0, 300, 0])
	

sim_setup.Run_Sim(SIM, CONSTANTS, Atmosphere, plane1)
