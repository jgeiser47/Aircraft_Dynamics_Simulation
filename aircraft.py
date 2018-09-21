#!/usr/bin/env python

####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np

class Aircraft():
	def __init__(self, initial_state, initial_forces):

		self.Design = "B747"
		self.state = initial_state
		self.forces = initial_forces

	mass = 1500;
	mass_matrix = np.identity(3) * mass

	def Calc_Forces(self):
		self.forces.net_force = np.array([0, 0, 0])
		self.forces.net_force = self.forces.net_force + self.Calc_Lift() 
		self.forces.net_force = self.forces.net_force + self.Calc_Drag() 
		self.forces.net_force = self.forces.net_force + self.Calc_Thrust() 
		self.forces.net_force = self.forces.net_force + self.Calc_Weight() 


	def Calc_Lift(self):
		self.forces.lift_ned = np.array([0, 0, -1300])
		return self.forces.lift_ned

	def Calc_Drag(self):
		drag_mag = 0.1 * np.linalg.norm(self.state.vel_ned) 
		self.forces.drag_ned = -1 * drag_mag * self.state.vel_ned
		
		#print(self.forces.drag_ned)
		return self.forces.drag_ned

	def Calc_Thrust(self):
		self.forces.thrust_ned = np.array([0, 60000, 0])
		return self.forces.thrust_ned

	def Calc_Weight(self):
		self.forces.weight_ned = np.array([0, 0, 1300])
		return self.forces.weight_ned



class state():
	def __init__(self):
		self.pos_ned = np.array([0, 0, 0])
		self.vel_ned = np.array([0, 300, 0])
		self.acc_ned = np.array([0, 0, 0])
		self.ang_pos_body = np.array([0, 0, 0])
		self.ang_vel_body = np.array([0, 0, 0])
		self.ang_acc_body = np.array([0, 0, 0])

class forces():
	def __init__(self): 
		self.lift_ned = np.array([0, 0, -1300])
		self.drag_ned = np.array([0, -12000, 0])
		self.thrust_ned = np.array([0, 60000, 0])
		self.weight_ned = np.array([0, 0, 1300])
		self.net_force = np.array([0, 1000, 0])
