#!/usr/bin/env python

####################################################################################################
# Description:		Executable plotting script for analyzing output data
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("output.csv", sep=',')

plt.plot(data["TIME"], data["Aircraft.state.Mach"])
plt.xlabel('Time (s)')
plt.ylabel('Mach Number')
plt.title('Mach Number vs time')
plt.grid(True)

plt.figure()
plt.plot(data["TIME"], data["Aircraft.state.vel_ENU[1]"])
plt.xlabel('Time (s)')
plt.ylabel('Northward Velocity (m/s)')
plt.title('Northward Velocity vs time')
plt.grid(True)

plt.figure()
plt.plot(data["TIME"], data["Aircraft.state.vel_ENU[0]"])
plt.xlabel('Time (s)')
plt.ylabel('Eastward Velocity (m/s)')
plt.title('Eastward Velocity vs time')
plt.grid(True)

plt.figure()
plt.plot(data["TIME"], data["Aircraft.state.vel_ENU[2]"])
plt.xlabel('Time (s)')
plt.ylabel('Upwardd Velocity (m/s)')
plt.title('Upward Velocity vs time')
plt.grid(True)

plt.figure()
plt.plot(data["Aircraft.state.pos_ENU[0]"], data["Aircraft.state.pos_ENU[2]"])
plt.xlabel('Distance east')
plt.ylabel('Altitude (m)')
plt.title('Position Graph')
plt.grid(True)

plt.figure()
plt.plot(data["TIME"], -1*data["Aircraft.forces.drag_ENU[0]"])
plt.plot(data["TIME"], data["Aircraft.forces.thrust_ENU[0]"])
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.title('Thrust and Drag vs time')
plt.legend(loc=4)
plt.grid(True)

plt.figure()
plt.plot(data["TIME"], data["Aircraft.forces.lift_mag"])
plt.plot(data["TIME"], data["Aircraft.forces.weight_mag"])
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.title('Lift and Weight vs time')
plt.legend(loc=4)
plt.grid(True)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(data["Aircraft.state.pos_ENU[0]"], data["Aircraft.state.pos_ENU[1]"], data["Aircraft.state.pos_ENU[2]"])
ax.set_xlabel('Distance East (m)')
ax.set_ylabel('Distance North (m)')
ax.set_zlabel('Altitude (m)')
ax.set_title('Aircraft Position vs Time')



plt.show()
