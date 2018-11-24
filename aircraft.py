####################################################################################################
# Description:		Aircraft class which represents a single aircraft in flight
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np
from Planes.B737 import B737
import sim_math as M

class Aircraft():
	def __init__(self):

		self.design = B737() # Default plane if none is input
		self.state = state()
		self.forces = forces()
		self.aero = aero()

	def Calc_Forces(self, CONSTANTS, Atmosphere):
		self.forces.net_force_ENU = np.array([0, 0, 0])
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Lift(Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Drag(Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Thrust(CONSTANTS, Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Weight(CONSTANTS) 

	def Calc_Lift(self, Atmosphere):
		self.aero.CL = M.LUT_Linear_Interpolate_1D('LUTs/' + self.design.name + '_CL_AoA.csv', self.aero.AoA)
		self.forces.lift_mag = 0.5 * Atmosphere.rho * self.design.wingarea * (self.state.vel_ENU[0] ** 2) * self.aero.CL
		self.forces.lift_ENU = np.array([0, 0, self.forces.lift_mag])
		return self.forces.lift_ENU

	def Calc_Drag(self, Atmosphere):
		self.aero.CD = self.design.CDi + M.LUT_Linear_Interpolate_1D('LUTs/' + self.design.name + '_CD_vs_CL.csv', self.aero.CL)
		
		drag_0 = 0.5 * Atmosphere.rho * self.design.wingarea * self.state.vel_ENU[0] * abs(self.state.vel_ENU[0]) * self.aero.CD
		drag_1 = 0.5 * Atmosphere.rho * self.design.wingarea * self.state.vel_ENU[1] * abs(self.state.vel_ENU[1]) * self.aero.CD
		drag_2 = 0.5 * Atmosphere.rho * self.design.wingarea * self.state.vel_ENU[2] * abs(self.state.vel_ENU[2]) * self.aero.CD * 200
	
		self.forces.drag_mag = (drag_0 ** 2 + drag_1 ** 2 + drag_2 ** 2) ** 0.5
		self.forces.drag_ENU = np.array([-1 * drag_0, -1 * drag_1, -1 * drag_2])
		
		return self.forces.drag_ENU

	def Calc_Thrust(self, CONSTANTS, Atmosphere):
		self.forces.thrust_mag = 1500 * self.state.vel_mag * Atmosphere.rho / CONSTANTS.RHO_0 #138000
		self.forces.thrust_ENU = np.array([self.forces.thrust_mag, 0, 0])
		return self.forces.thrust_ENU

	def Calc_Weight(self, CONSTANTS):
		self.forces.weight_mag = self.design.mass * CONSTANTS.GRAVITY
		self.forces.weight_ENU = np.array([0, 0, -1*self.forces.weight_mag])
		return self.forces.weight_ENU


class state():
	def __init__(self):
		self.pos_ENU = np.array([0, 0, 0])
		self.vel_ENU = np.array([0, 0, 0])
		self.acc_ENU = np.array([0, 0, 0])
		self.ang_pos_body = np.array([0, 0, 0])
		self.ang_vel_body = np.array([0, 0, 0])
		self.ang_acc_body = np.array([0, 0, 0])

		self.pos_mag = 0
		self.vel_mag = 0
		self.acc_mag = 0
		self.Mach = 0

class forces():
	def __init__(self): 
		self.lift_ENU = np.array([0, 0, 0])
		self.drag_ENU = np.array([0, 0, 0])
		self.thrust_ENU = np.array([0, 0, 0])
		self.weight_ENU = np.array([0, 0, 0])
		self.net_force_ENU = np.array([0, 0, 0])

		self.lift_mag = 0
		self.drag_mag = 0
		self.thrust_mag = 0
		self.weight_mag = 0
		self.net_force_mag = 0

class aero():
	def __init__(self):
		self.AoA = 0
		self.CL = 0
		self.CD = 0
