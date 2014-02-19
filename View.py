# -*- coding: utf8 -*-
from __future__ import unicode_literals
import sys



class View(object):
        """docstring for View"""
        def __init__(self):
                super(View, self).__init__()
                self.commands = ["q", "w", "e", "a", "s", "d", "z","x","c"," ","t"]
                self.DALEK = "X"
                self.SCRAP_HEAP = "S"
                self.DOCTOR = "D"

        def waitForInput(self):
                text = "Entrez votre déplacement: "
                value = "placeholder"
                print("---------------------------------------")
                while self.sanitizeInput(value) == False:
                        value = input(text)
                return value


        def sanitizeInput(self, userInput):
                return userInput in self.commands


        def displayCosmicPoints(self, nbPoints):
                print("Points cosmiques: %s"%(nbPoints))


        def displayGameboard(self, gameboard, dr, daleks, scrapHeaps):
                boardUI = self.generateMatrix(gameboard, dr, daleks, scrapHeaps)
                for y in range(0,gameboard.y-1):
                         for x in range(0,gameboard.x-1):
                                print(boardUI[x][y],end='')
                         print("")

        def generateMatrix(self, gameboard, dr, daleks, scrapHeaps):
                #Generate GUI Matrix from position, just for printing purpose
                boardUI = [["." for i in range(gameboard.y)] for j in range(gameboard.x)]
                boardUI[dr.position.x][dr.position.y] = self.DOCTOR


                for dalek in daleks:
                        boardUI[dalek.position.x][dalek.position.y] = self.DALEK
                for scrapHeap in scrapHeaps:
                        boardUI[scrapHeap.position.x][scrapHeap.position.y] = self.SCRAP_HEAP
                return boardUI



        def refresh(self, gameboard, dr, daleks, scrapHeap):
                self.displayCosmicPoints(dr.nbPoints)
                self.displayGameboard(gameboard, dr, daleks, scrapHeap)
                return self.waitForInput()
               




if __name__ == '__main__':
        view = View()
        view.refresh(None,None,None,None)
                
                
