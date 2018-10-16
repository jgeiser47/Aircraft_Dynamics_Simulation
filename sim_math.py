####################################################################################################
# Description:		Various math functions used throughout simulation
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np
import csv

def Integrate_Linear(DELTA_T, integrand, initial_condition):
	return (integrand * DELTA_T + initial_condition)
	
def LUT_Linear_Interpolate_1D(LUT, val):
	with open(LUT) as csvfile:
		CSV_data = list(csv.reader(csvfile, delimiter=','))
		if val <= float(CSV_data[0][0]):
			return float(CSV_data[0][1])
		elif val >= float(CSV_data[len(CSV_data) - 1][0]):
			return float(CSV_data[len(CSV_data) - 1][1])
		else:
			for row in range(len(CSV_data)):
				if val < float(CSV_data[row+1][0]):
					m = (float(CSV_data[row+1][1]) - float(CSV_data[row][1])) \
						/(float(CSV_data[row+1][0]) - float(CSV_data[row][0]))
					dx = val - float(CSV_data[row][0])
					b = float(CSV_data[row][1])
					LU_val = m*dx + b
					return LU_val
				else:
					continue
