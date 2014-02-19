from Model import *
from View import *


class Controller(object):
	"""docstring for Controller"""
	def __init__(self):
		super(Controller, self).__init__()
		self.view = View()
		self.model = Model()

	
	def startGame(self):
		# Everything has been inited in the Views and the Model Constructors
		userInput = self.view.refresh(self.model.gameboard, 
									  self.model.doctor, 
									  self.model.daleks, 
									  self.model.scrapHeap)
		userAction = self.actionFromInput(userInput)

		if userAction == UserAction.ZAP:
			self.model.zap() # ZAP
		elif userAction == UserAction.TELEPORT:
			self.model.teleportDoctor() # TELEPORT
		else:
			return self.model.moveDoctor(userAction) # MOVE 



	def actionFromInput(self, userInput):
		if userInput == "q":
			return UserAction.MOVE_NW
		if userInput == "w":
			return UserAction.MOVE_N
		if userInput == "e":
			return UserAction.MOVE_NE
		if userInput == "a":
			return UserAction.MOVE_W
		if userInput == "s":
			return UserAction.MOVE_NULL
		if userInput == "d":
			return UserAction.MOVE_E
		if userInput == "z":
			return UserAction.MOVE_SW
		if userInput == "x":
			return UserAction.MOVE_S
		if userInput == "c":
			return UserAction.MOVE_SE
		if userInput == " ":
			return UserAction.ZAP
		if userInput == "t":
			return UserAction.TELEPORT

		

if __name__ == '__main__':
	game = Controller()
	game.startGame()