####################################################################################################
# Description:		Aircraft class which represents a single aircraft in flight
# Author(s):		Joshua Geiser
# Last Modified:	12/2018

import numpy as np
from Planes.B737 import B737
import sim_math as M

class Aircraft():

	# Initialization of an aircraft
	def __init__(self):
		self.design = B737() # Default plane if none is input
		self.state = state() # Defaults to all zero state
		self.forces = forces() # Defaults to all zero forces
		self.aero = aero() # Defaults to all zeros

	# Calculates and sums all forces on aircraft at a given timestep
	def Calc_Forces(self, CONSTANTS, Atmosphere):
		self.forces.net_force_ENU = np.array([0, 0, 0])
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Lift(Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Drag(Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Thrust(CONSTANTS, Atmosphere) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Weight(CONSTANTS) 
		self.forces.net_force_ENU = self.forces.net_force_ENU + self.Calc_Wind(Atmosphere)

	# Calculates lift force on aircraft at a given timestep
	def Calc_Lift(self, Atmosphere):
		self.aero.CL = M.LUT_Linear_Interpolate_1D('LUTs/' + self.design.name + '_CL_vs_AoA.csv', self.aero.AoA)
		planar_velocity = (self.state.vel_ENU[0] ** 2 + self.state.vel_ENU[1] ** 2) ** 0.5
		self.forces.lift_mag = 0.5 * Atmosphere.rho * self.design.wingarea * (planar_velocity ** 2) * self.aero.CL
		self.forces.lift_ENU = np.array([0, 0, self.forces.lift_mag])
		return self.forces.lift_ENU

	# Calculates drag force on aircraft at a given timestep
	def Calc_Drag(self, Atmosphere):
		
		# Calculate CD as the sum of induced drag (assumed to be constant) and CD due to angle of attack
		self.aero.CD = self.design.CDi + M.LUT_Linear_Interpolate_1D('LUTs/' + self.design.name + '_CD_vs_AoA.csv', self.aero.AoA)
		
		# Calculate drag in each ENU component direction, Z component multiplied by 200 to increase damping 
		drag_0 = 0.5 * Atmosphere.rho * self.design.wingarea * self.state.vel_ENU[0] * abs(self.state.vel_ENU[0]) * self.aero.CD
		drag_1 = 0.5 * Atmosphere.rho * self.design.wingarea * self.state.vel_ENU[1] * abs(self.state.vel_ENU[1]) * self.aero.CD
		drag_2 = 0.5 * Atmosphere.rho * self.design.wingarea * self.state.vel_ENU[2] * abs(self.state.vel_ENU[2]) * self.aero.CD * 200 
	
		self.forces.drag_mag = (drag_0 ** 2 + drag_1 ** 2 + drag_2 ** 2) ** 0.5
		self.forces.drag_ENU = np.array([-1 * drag_0, -1 * drag_1, -1 * drag_2])
		
		return self.forces.drag_ENU

	# Calculates thrust force on aircraft at a given timestep
	def Calc_Thrust(self, CONSTANTS, Atmosphere):

		# For simplicity, thrust assumed to vary only as a function of atmospheric density
		self.forces.thrust_mag = self.design.max_thrust * Atmosphere.rho / CONSTANTS.RHO_0

		# Calculates thrust components based on direction of travel
		thrust_0 = self.forces.thrust_mag * self.state.direction[0]
		thrust_1 = self.forces.thrust_mag * self.state.direction[1]
		thrust_2 = self.forces.thrust_mag * self.state.direction[2]

		self.forces.thrust_ENU = np.array([thrust_0, thrust_1, thrust_2])
		return self.forces.thrust_ENU

	# Calculates weight force on aircraft at a given timestep (mass/weight assumed to be constant)
	def Calc_Weight(self, CONSTANTS):
		self.forces.weight_mag = self.design.mass * CONSTANTS.GRAVITY
		self.forces.weight_ENU = np.array([0, 0, -1*self.forces.weight_mag])
		return self.forces.weight_ENU

	# Calculates wind force on aircraft at a given timestep based on input wind gusts
	def Calc_Wind(self, Atmosphere):
		self.forces.wind_ENU = np.array([0, 0, 0])

		# Sum wind forces that are active at the current timestep
		for wind_gust in Atmosphere.wind:
			if (wind_gust.active):
				self.forces.wind_ENU = self.forces.wind_ENU + wind_gust.wind_force

		self.forces.wind_mag = (np.linalg.norm(self.forces.wind_ENU))
		return self.forces.wind_ENU


# State subclass of aircraft class - contains information about the current state of the aircraft
class state():
	def __init__(self):
		self.pos_ENU = np.array([0, 0, 0])
		self.vel_ENU = np.array([0, 0, 0])
		self.acc_ENU = np.array([0, 0, 0])
		self.ang_pos_body = np.array([0, 0, 0])
		self.ang_vel_body = np.array([0, 0, 0])
		self.ang_acc_body = np.array([0, 0, 0])
		self.direction = np.array([0, 0, 0])

		self.pos_mag = 0
		self.vel_mag = 0
		self.acc_mag = 0
		self.Mach = 0

# Forces subclass of aircraft class - contains information about the forces acting on the aircraft
class forces():
	def __init__(self): 
		self.lift_ENU = np.array([0, 0, 0])
		self.drag_ENU = np.array([0, 0, 0])
		self.thrust_ENU = np.array([0, 0, 0])
		self.weight_ENU = np.array([0, 0, 0])
		self.wind_ENU = np.array([0, 0, 0])
		self.net_force_ENU = np.array([0, 0, 0])

		self.lift_mag = 0
		self.drag_mag = 0
		self.thrust_mag = 0
		self.weight_mag = 0
		self.wind_mag = 0
		self.net_force_mag = 0

# Aero subclass of aircraft class - contains information about aerodynamic properties of the aircraft
class aero():
	def __init__(self):
		self.AoA = 0
		self.CL = 0
		self.CD = 0
