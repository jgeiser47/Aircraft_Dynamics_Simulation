#!/usr/bin/env python

####################################################################################################
# Description:		Executable input deck to vary inputs and run simulation
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

from aircraft import Aircraft
from atmosphere import Atmosphere
from constants import Constants
import sim_setup

from Planes.B737 import B737
from Planes.C172 import C172
from Planes.T38 import T38


SIM = sim_setup.Sim_Parameters()

SIM.START_TIME = 0.0
SIM.END_TIME = 2000.0
SIM.DELTA_T = 2

CONSTANTS = Constants()

Atmosphere = Atmosphere()

plane1 = Aircraft()

plane1.design = B737()
plane1.state.pos_ENU = np.array([0, 0, 10000])
plane1.state.vel_ENU = np.array([260, 0, 0])
plane1.aero.AoA = 0.02
	

sim_setup.Run_Sim(SIM, CONSTANTS, Atmosphere, plane1)
