####################################################################################################
# Description:		Run simulation by executing Driver.py script
# Author(s):		Joshua Geiser
# Last Modified:	10/2018

import numpy as np
from B737 import B737
import sim_math as M

class Aircraft():
	def __init__(self):

		self.design = B737()
		self.state = state()
		self.forces = forces()
		self.aero = aero()

	def Calc_Forces(self, CONSTANTS, Atmosphere):
		self.forces.net_force_ENU = np.array([0, 0, 0])
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Lift(Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Drag(Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Thrust() 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Weight(CONSTANTS) 

	def Calc_Lift(self, Atmosphere):
		self.aero.CL = M.LUT_Linear_Interpolate_1D('LUTs/B737_CL_AoA.csv', self.aero.AoA)
		lift_mag = 0.5 * Atmosphere.rho * self.design.wingarea * (np.linalg.norm(self.state.vel_ENU) ** 2) * self.aero.CL
		self.forces.lift_ENU = np.array([0, 0, lift_mag])
		return self.forces.lift_ENU

	def Calc_Drag(self, Atmosphere):
		self.aero.CD = self.design.CDi + M.LUT_Linear_Interpolate_1D('LUTs/B737_CD_vs_CL.csv', self.aero.CL)
		
		drag_mag = 0.5 * Atmosphere.rho * self.design.wingarea * np.linalg.norm(self.state.vel_ENU) * self.aero.CD
		self.forces.drag_ENU = -1 * drag_mag * self.state.vel_ENU
		return self.forces.drag_ENU

	def Calc_Thrust(self):
		thrust_mag = 242800
		self.forces.thrust_ENU = np.array([thrust_mag, 0, 0])
		return self.forces.thrust_ENU

	def Calc_Weight(self, CONSTANTS):
		weight_mag = self.design.mass * CONSTANTS.GRAVITY
		self.forces.weight_ENU = np.array([0, 0, -1*weight_mag])
		return self.forces.weight_ENU


class state():
	def __init__(self):
		self.pos_ENU = np.array([0, 0, 0])
		self.vel_ENU = np.array([0, 0, 0])
		self.acc_ENU = np.array([0, 0, 0])
		self.ang_pos_body = np.array([0, 0, 0])
		self.ang_vel_body = np.array([0, 0, 0])
		self.ang_acc_body = np.array([0, 0, 0])

class forces():
	def __init__(self): 
		self.lift_ENU = np.array([0, 0, 0])
		self.drag_ENU = np.array([0, 0, 0])
		self.thrust_ENU = np.array([0, 0, 0])
		self.weight_ENU = np.array([0, 0, 0])
		self.net_force_ENU = np.array([0, 0, 0])

class aero():
	def __init__(self):
		self.AoA = 0
		self.CL = 0
		self.CD = 0
