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
     
                        
        def startGame(self):
                # Everything has been inited in the Views and the Model Constructors
                userAction = self.view.refresh(self.model.gameboard, 
                                                                          self.model.doctor, 
                                                                          self.model.daleks, 
                                                                          self.model.scrapHeaps)

                if userAction == UserAction.ZAP:
                        self.model.zap() # ZAP
                elif userAction == UserAction.TELEPORT:
                        self.model.teleportDoctor() # TELEPORT
                else:
                         returnCode = self.model.moveDoctor(userAction) # MOVE
                if returnCode == ReturnCodes.SUCCESS:
                        self.model.moveDaleks()
                        return ReturnCodes.SUCCESS
                return returnCode
                
       

                

if __name__ == '__main__':
        game = Controller()
        game.gameLoop()
