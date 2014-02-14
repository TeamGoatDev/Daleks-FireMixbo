from Gameboard import Gameboard
from GameObject import *

class Controller(object):
	"""Makes the path between the model and the view"""

	def __init__(self):
		self.reset()

	def initGameboard(self,x,y):
		self.gameboard = Gameboard(x,y)

	def initDalekArmy(self):
		self.daleks = []
		for i in range(self.doctor.level*5)
			self.daleks.append(Dalek())

	def initDoctor(self):
		self.doctor = Doctor()

	def isDoctorSafe(self):
	def canDoctorMove(self):
	def moveDoctor(self):
	def moveDaleks(self):
		for i in range(len(self.daleks)):
			self.daleks[i].move(self.doctor.position)
			
	def reset(self):
		self.initGameboard(20,30)
		self.initDoctor()
		self.initDalekArmy()
