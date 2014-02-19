from ReturnCodes import *
from Gameboard import *
from GameObjects import *
from UserActions import *
class Model(object):
	""" """

	def __init__(self):
		super(Model, self).__init__()
		self.level = 1
		self.daleks = []
		self.scrapHeap = []

		self.reset()


	def reset(self):
		self.initGameboard(20+self.level,30+self.level)
		self.initDoctor()
		self.initDalekArmy()


	def initGameboard(self,x,y):
		self.gameboard = Gameboard(x,y)

	def initDalekArmy(self):
		self.daleks = []
		for i in range(self.level*5):
			self.daleks.append(Dalek())


	def initDoctor(self):
		self.doctor = Doctor()
		self.doctor.position.x = self.gameboard.x/2
		self.doctor.position.y = self.gameboard.y/2

	def isDoctorSafe(self):
		pass



	def zap(self):
		pass

	def teleportDoctor(self):
		pass

	def moveDoctor(self, direction):
		""" the direction parameter is a UserAction MOVE_* """
		targetPosition = self.detTargetDoctorPos(direction)
		if self.canDoctorMove(targtePosition):
			self.doctor.position = targetPosition
			return ReturnCodes.SUCCESS
		else:
			return ReturnCodes.INVALID_MOVE

		
		



	def detTargetDoctorPos(self, direction):
		targetPosition = None
		if direction == UserAction.MOVE_N:
			targetPosition = Position(0,1)
		if direction == UserAction.MOVE_S:
			targetPosition = Position(0,-1)
		if direction == UserAction.MOVE_E:
			targetPosition = Position(1,0)
		if direction == UserAction.MOVE_W:
			targetPosition = Position(-1,0)

		if direction == UserAction.MOVE_NW:
			targetPosition = Position(-1,1)
		if direction == UserAction.MOVE_NE:
			targetPosition = Position(1,1)
		if direction == UserAction.MOVE_SW:
			targetPosition = Position(-1,-1) 
		if direction == UserAction.MOVE_SE:
			targetPosition = Position(1,-1)
		if direction == UserAction.MOVE_NULL:
			targetPosition = Position(0,0)
		targetPosition.add(self.doctor.position)
		return targetPosition

	

	def canDoctorMove(self, position):
		if position.x < 1 or position.x > self.gameboard.x:
			return False
		if position.y < 1 or position.y > self.gameboard.y:
			return False
		if isDoctorDead(position): #Test whether or not the doctor is commiting suicide
			return False
		return True



	def moveDaleks(self):
		for i in range(len(self.daleks)):
			self.daleks[i].move(self.doctor.position)

	def detectCollision(self):
                pass
	
			
	def isDoctorDead(self, doctorPosition):
		for dalek in self.daleks:
			if dalek.position.x == doctorPosition.position.x and  dalek.position.y == doctorPosition.position.y:
				return True
		for scrapHeap in self.scrapHeaps:
			if scrapHeap.position.x == doctorPosition.position.x and  scrapHeap.position.y == doctorPosition.position.y:
				return True 
