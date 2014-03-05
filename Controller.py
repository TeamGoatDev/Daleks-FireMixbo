from Model import *
from View import *
from UserActions import *

from dalekGUI import *
import sys


class Controller(object):
        """docstring for Controller"""
        def __init__(self):
                super(Controller, self).__init__()
                self.view = View()
                self.model = Model()
                self.listenEvent=None #will change when user inputs something
                self.view.callback = self.listenInput #The View will call al the changes here
                self.view.run()

        # Has to be looped by the view manually
        def gameLoop(self):
                returnCode = ReturnCodes.SUCCESS
                if returnCode != ReturnCodes.DEAD_DOCTOR:
                        returnCode = self.startGame()
                        if returnCode == ReturnCodes.END_WAVE:
<<<<<<< HEAD
                                        self.model.level += 1
                                        self.model.reset()
=======
                          self.model.level += 1
                          self.model.reset()
>>>>>>> e08d610b4bafe9953cccf45b64c66b805e512c06

                if returnCode == ReturnCodes.DEAD_DOCTOR:
                        self.view.refresh(self.model.gameboard,
                                          self.model.doctor,
                                          self.model.daleks,
                                          self.model.scrapHeaps,
                                          self.model.level
                                          )
                        self.view.printGameOver()
                
                
        def listenInput(self, returnCode=None):
            self.listenEvent = returnCode
            #Wait for change
            while(returnCode == None):
              pass
            #Something changed
            returnCode = self.listenEvent
            self.listenEvent = None; #Reset
            return returnCode



        def startGame(self):
                # Everything has been inited in the Views and the Model Constructors
                self.view.refresh(self.model.gameboard,
                                  self.model.doctor,
                                  self.model.daleks,
                                  self.model.scrapHeaps,
                                  self.model.level)

                userAction = self.ListenInput()

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
        #Get Parametre
        print(str(sys.argv))
        if str(sys.argv[0]) == "CLI":
          print("CLI")



        game = Controller()
        #si param = CLI COntroller.vue == CLI()
        #Sinon Controller.vue == GUI
        game.gameLoop()
