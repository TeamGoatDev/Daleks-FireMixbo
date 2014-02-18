# -*- coding: utf8 -*-
from __future__ import unicode_literals
import sys

if sys.version_info < (3, 2):
        input = raw_input

class Vue(object):
        """docstring for Vue"""
        def __init__(self):
                super(Vue, self).__init__()
                self.commands = ["q", "w", "e", "a", "s", "d", "z","x","c"," ", "t"]
                self.DALEK = "X"
                self.SCRAP_HEAP = "X"
                self.DOCTOR = "X"

        def waitForInput(self):
                text = "Entrez votre déplacement: "
                value = "123456789"
                print("---------------------------------------")
                while self.sanitizeInput(value) == False:
                        value = input(text)


        def sanitizeInput(self, userInput):
                return userInput in self.commands


        def displayCosmicPoints(self, nbPoints):
                print("Points cosmiques: %s"%(nbPoints))

        def displayGameBoard(self, gameBoard, dr, daleks, scrapHeap):
                hasPrinted = False #Whether the GUI has printed for this position
                for y in xrange(1,gameBoard.y):
                        for x in xrange(1,gameBoard.x):
                                for dalek in daleks:
                                        if dalek.position.x == x and dalek.position.y == y:
                                                print self.DALEK,
                                                break
                        print("\n")

        def displayGameBoard(self, gameBoard, dr, daleks, scrapHeaps):
                boardUI = self.generateMatirx(gameBoard, dr, daleks, scrapHeaps)
                for y in xrange(1,gameBoard.y):
                         for x in xrange(1,gameBoard.x):
                                print boardUI[x][y]

        def generateMatirx(self, gameBoard, dr, daleks, scrapHeaps):
                #Generate GUI Matrix from position, just for printing purpose
                boardUI = a = [[0 for i in range(gameBoard.x)] for j in range(gameBoard.y)]
                boardUI[dr.x][dr.y] = self.DOCTOR
                for dalek in daleks:
                        boardUI[dalek.position.x][dalek.position.y] = self.DALEK
                for scrapHeap in scrapHeaps:
                        boardUI[scrapHeap.position.x][scrapHeap.position.y] = self.SCRAP_HEAP
                return boardUI



        def refresh(self, gameBoard, dr, daleks, scrapHeap, nbPoints):
                self.displayCosmicPoints(nbPoints)
                self.displayGameBoard(gameBoard, dr, daleks, scrapHeap)
                return self.waitForInput()
               




if __name__ == '__main__':
        vue = Vue()
        vue.refresh(None,None,None,None,None)
                
                
