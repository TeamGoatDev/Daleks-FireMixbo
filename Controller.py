from Model import *
from View import *
from UserActions import *

class Controller(object):
        """docstring for Controller"""
        def __init__(self):
                super(Controller, self).__init__()
                self.view = View()
                self.model = Model()

        def gameLoop(self):
                returnCode = ReturnCodes.SUCCESS
                while returnCode != ReturnCodes.DEAD_DOCTOR:
                        returnCode = self.startGame()
                if returnCode == ReturnCodes.DEAD_DOCTOR:
                        self.view.refresh(self.model.gameboard,
                                                                          self.model.doctor,
                                                                          self.model.daleks,
                                                                          self.model.scrapHeaps)
                        self.view.printGameOver()


        def startGame(self):
                # Everything has been inited in the Views and the Model Constructors
                self.view.refresh(self.model.gameboard,
                                                                          self.model.doctor,
                                                                          self.model.daleks,
                                                                          self.model.scrapHeaps)
                userAction = self.view.getAction()

                if userAction == UserAction.ZAP:
                        returnCode = self.model.zap() # ZAP
                elif userAction == UserAction.TELEPORT:
                        returnCode = self.model.teleportDoctor() # TELEPORT
                elif userAction == UserAction.EXIT_GAME:
                        exit()
                else:
                         returnCode = self.model.moveDoctor(userAction) # MOVE
                if returnCode == ReturnCodes.SUCCESS:
                         returnCode = self.model.moveDaleks()
                return returnCode





if __name__ == '__main__':
        game = Controller()
        game.gameLoop()
