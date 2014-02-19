# -*- coding: utf8 -*-
from __future__ import unicode_literals
import sys

if sys.version_info < (3, 2):
        input = raw_input

class View(object):
        """docstring for View"""
        def __init__(self):
                super(View, self).__init__()
                self.commands = ["q", "w", "e", "a", "s", "d", "z","x","c"," ","t"]
                self.DALEK = "X"
                self.SCRAP_HEAP = "X"
                self.DOCTOR = "X"

        def waitForInput(self):
                text = "Entrez votre déplacement: "
                value = "placeholder"
                print("---------------------------------------")
                while self.sanitizeInput(value) == False:
                        value = input(text)


        def sanitizeInput(self, userInput):
                return userInput in self.commands


        def displayCosmicPoints(self, nbPoints):
                print("Points cosmiques: %s"%(nbPoints))


        def displayGameboard(self, gameboard, dr, daleks, scrapHeaps):
                boardUI = self.generateMatirx(gameboard, dr, daleks, scrapHeaps)
                for y in xrange(0,gameboard.y-1):
                         for x in xrange(0,gameboard.x-1):
                                print(boardUI[x][y],)
                         print("\n")

        def generateMatirx(self, gameboard, dr, daleks, scrapHeaps):
                #Generate GUI Matrix from position, just for printing purpose
                boardUI = a = [[0 for i in range(gameboard.x)] for j in range(gameboard.y)]
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
                
                
