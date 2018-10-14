####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np
from B737 import B737

class Aircraft():
	def __init__(self):

		self.design = B737()
		self.state = state()
		self.forces = forces()

	def Calc_Forces(self):
		self.forces.net_force_ENU = np.array([0, 0, 0])
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Lift() 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Drag() 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Thrust() 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Weight() 

	def Calc_Lift(self):
		self.forces.lift_ENU = np.array([0, 0, 1400])
		return self.forces.lift_ENU

	def Calc_Drag(self):
		drag_mag = 0.1 * np.linalg.norm(self.state.vel_ENU) 
		self.forces.drag_ENU = -1 * drag_mag * self.state.vel_ENU
		return self.forces.drag_ENU

	def Calc_Thrust(self):
		self.forces.thrust_ENU = np.array([0, 60000, 0])
		return self.forces.thrust_ENU

	def Calc_Weight(self):
		self.forces.weight_ENU = np.array([0, 0, -1300])
		return self.forces.weight_ENU


class state():
	def __init__(self):
		self.pos_ENU = np.array([0, 0, 0])
		self.vel_ENU = np.array([0, 0, 0])
		self.acc_ENU = np.array([0, 0, 0])
		self.ang_pos_body = np.array([0, 0, 0])
		self.ang_vel_body = np.array([0, 0, 0])
		self.ang_acc_body = np.array([0, 0, 0])
		self.AoA = 0

class forces():
	def __init__(self): 
		self.lift_ENU = np.array([0, 0, 0])
		self.drag_ENU = np.array([0, 0, 0])
		self.thrust_ENU = np.array([0, 0, 0])
		self.weight_ENU = np.array([0, 0, 0])
		self.net_force_ENU = np.array([0, 0, 0])
