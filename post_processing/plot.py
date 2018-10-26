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
plt.plot(data["Aircraft.state.pos_ENU[0]"], data["Aircraft.state.pos_ENU[2]"])
plt.xlabel('Distance east')
plt.ylabel('Altitude (m)')
plt.title('Position Graph')

plt.figure()
plt.plot(data["TIME"], -1*data["Aircraft.forces.drag_ENU[0]"])
plt.plot(data["TIME"], data["Aircraft.forces.thrust_ENU[0]"])
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.title('Thrust and Drag vs time')
plt.legend()

plt.figure()
plt.plot(data["TIME"], data["Aircraft.forces.lift_mag"])
plt.plot(data["TIME"], data["Aircraft.forces.weight_mag"])
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.title('Lift vs Weight vs time')
plt.legend()

plt.show()
