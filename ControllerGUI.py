from Model import *
from UserActions import *
from ReturnCodes import *
import sys


class Controller(object):
        """docstring for Controller"""
        def __init__(self, interface):
                super(Controller, self).__init__()
                self.view = App()
                self.model = Model()
                self.listenEvent=None #will change when user inputs something
                self.view.callback = self.gameLoop #The View will call al the changes here
                if interface == "GUI":
                   self.view.refresh(self.model.gameboard,
                                          self.model.doctor,
                                          self.model.daleks,
                                          self.model.scrapHeaps,
                                          self.model.level
                                          )
                   self.view.run()
                elif interface == "CLI":
                  self.view.getAction()
                  self.gameLoop()

        # Has to be looped by the view manually
        def gameLoop(self, userAction):
                returnCode = ReturnCodes.SUCCESS
                if returnCode != ReturnCodes.DEAD_DOCTOR:
                        returnCode = self.playTurn(userAction)
                        if returnCode == ReturnCodes.END_WAVE:
                                        self.model.changeLevel()

                if returnCode == ReturnCodes.DEAD_DOCTOR:
                        self.view.refresh(self.model.gameboard,
                                          self.model.doctor,
                                          self.model.daleks,
                                          self.model.scrapHeaps,
                                          self.model.level
                                          )
                        self.view.printGameOver()
                self.view.refresh(self.model.gameboard,
                                          self.model.doctor,
                                          self.model.daleks,
                                          self.model.scrapHeaps,
                                          self.model.level
                                          )
                
                




        def playTurn(self, userAction):
                # Everything has been inited in the Views and the Model Constructors
                self.view.refresh(self.model.gameboard,
                                  self.model.doctor,
                                  self.model.daleks,
                                  self.model.scrapHeaps,
                                  self.model.level)


                if userAction == UserAction.ZAP:
                        returnCode = self.model.zap() # ZAP
                elif userAction == UserAction.TELEPORT:
                        returnCode = self.model.teleportDoctor() # TELEPORT
                elif userAction == UserAction.EXIT_GAME:
                        exit(0)
                else:
                        print("IM MOOOVING")
                        returnCode = self.model.moveDoctor(userAction) # MOVE
                if returnCode == ReturnCodes.SUCCESS:
                         returnCode = self.model.moveDaleks()
                return returnCode




if __name__ == '__main__':
        #Get Parametre
        try:
          interface = str(sys.argv[1])
        except IndexError:
            print("interface non specifie, veuillez specifier( GUI, CLI )")
            sys.exit(1)
        if interface == "GUI":
          from dalekGUI import *
        elif interface == "CLI":
          from View import *

        game = Controller(interface)
        #si param = CLI COntroller.vue == CLI()
        #Sinon Controller.vue == GUI

       # if interface == "GUI"
       #  game.gameLoop()
