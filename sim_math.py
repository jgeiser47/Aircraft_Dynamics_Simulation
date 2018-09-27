####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np


def Integrate_Linear(DELTA_T, integrand, initial_condition):
	return (integrand * DELTA_T + initial_condition)
	
