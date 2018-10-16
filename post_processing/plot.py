#!/usr/bin/env python

####################################################################################################
# Description:		Executable plotting script for analyzing output data
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import pandas as pd
from numpy import genfromtxt
from matplotlib import pyplot as plt

data = pd.read_csv("output.csv", sep=',')

plt.plot(data["TIME"], data["Aircraft.state.vel_ENU[0]"])
plt.xlabel('Time (s)')
plt.ylabel('Eastward Velocity (m/s)')
plt.title('Aircraft velocity component vs time')

plt.figure()
plt.plot(data["TIME"], data["Aircraft.state.pos_ENU[0]"])
plt.xlabel('Time (s)')
plt.ylabel('Distance east (m)')
plt.title('Position component vs time')

plt.show()
