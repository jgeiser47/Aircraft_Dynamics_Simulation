####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class Constants():

	GRAVITY = 9.81;
	GRAVITY_ENU = np.array([0, 0, GRAVITY])
	TOLERANCE = 1e-06;

