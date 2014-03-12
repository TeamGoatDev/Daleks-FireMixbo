#!/usr/bin/python
# -*- coding: utf-8 -*-
#Python 3.x
from tkinter import *
from tkinter import ttk
from GuiGoat import *
from UserActions import *

COLOR_PRIMARY = "#c0392b" #


class GameBoardUI(Frame):
    """docstring for GameBoardUI"""
    def __init__(self, parent, columns, rows, squareSize, background,foreground, app):

        self.parent = parent
        self.app = app
        self.rows = rows
        self.columns = columns
        self.squareSize = squareSize
        self.background = background
        self.foreground = foreground

        self.scrapHeap = []
        self.daleks = []
        self.doctor = None

        self.dalekImage = PhotoImage(file="img/dalekSmall.gif")

        self.doctorImage = PhotoImage(file="img/doctorSmall.gif")


        self.scrapHeapImage = PhotoImage(file="img/scrapHeapSmall.gif")


        canvasWidth = columns * squareSize
        canvasHeight = rows * squareSize

        Frame.__init__(self,parent)
        self.canvas = Canvas(self, width=canvasWidth, height=canvasHeight, background=self.background)
        self.canvas.pack(fill=BOTH, expand=True)
        #Affichage initial
        self.draw(columns,rows)
        # Binding des ÃƒÆ’Ã‚Â©vÃƒÆ’Ã‚Â©nements
        self.canvas.bind("<Button-1>", self.app.notifyMove)




    def drawDoctor(self, x,y):
        self.canvas.create_image((x+self.doctorImage.width()/2,y+self.doctorImage.height()/2), image=self.doctorImage)

    def drawDalek(self, x,y):
        self.canvas.create_image((x+self.dalekImage.width()/2,y+self.dalekImage.height()/2), image=self.dalekImage)


    def drawScrapHeap(self, x,y):
        self.canvas.create_image((x+self.scrapHeapImage.width()/2,y+self.scrapHeapImage.height()/2), image=self.scrapHeapImage)


    def draw(self,  nbCols, nbRows):
        self.rows = nbRows
        self.columns = nbCols
        self.canvas.delete()
        for row in range(0,nbRows):
            for column in range(0,nbCols):
                x1 = (column * self.squareSize)
                y1 = (row * self.squareSize)
                x2 = x1 + self.squareSize
                y2 = y1 + self.squareSize
                self.canvas.create_rectangle(x1,y1,x2,y2, outline=self.background, width=2,
                fill=self.foreground, activefill=COLOR_PRIMARY, tags="cell")

                if self.app.boardData != None:

                    if self.app.boardData[column][row] == self.app.DALEK:
                        self.drawDalek(x1,y1)
                    if self.app.boardData[column][row] == self.app.DOCTOR:
                        self.drawDoctor(x1,y1)
                    if self.app.boardData[column][row] == self.app.SCRAP_HEAP:
                        self.drawScrapHeap(x1,y1)




class App(object):
    """docstring for App"""
    def __init__(self):
        self.parent = Window()

        self.DALEK = "X"
        self.SCRAP_HEAP = "S"
        self.DOCTOR = "D"

        self.initUI()


    def styleButton(self, button):
        button['background'] = COLOR_PRIMARY
        button['borderwidth'] = 0
        button['foreground'] = "#ecf0f1"



    def run(self):
        self.parent.run()

    def initUI(self):
        self.width = 680
        self.height = 500
        self.frame = Frame(self.parent.mainFrame)
        self.frame.grid(row=0,column=0, sticky=N+W+E+S, padx=20,pady=20 )

        self.initStatsBar()
        self.initGameBoard()






    def initStatsBar(self):
        # STATISTIC BAR

        frameStats = Frame(self.frame, height=20,  bg=COLOR_PRIMARY)
        frameStats.grid(row=0,column=0, columnspan=2, sticky=E+W,pady=5)
        frameStats.color = COLOR_PRIMARY


        self.labelScore = Label(frameStats, text="CrÃ©dits cosmiques:", width=35, background=frameStats.color)
        self.labelScore.grid(row=0,column=0, sticky=N+W+E)



        self.labelNbDaleks = Label(frameStats, text="Nombre de Daleks:", width=42, background=frameStats.color)
        self.labelNbDaleks.grid(row=0,column=1)


        self.labelWave = Label(frameStats, text="Vague:",  width=35, background=frameStats.color)
        self.labelWave.grid(row=0,column=2, sticky=E)

        self.labelZappeur = Label(frameStats, text="Zappeur:",  width=35, background=frameStats.color)
        self.labelZappeur.grid(row=0,column=3, sticky=E)



    def initGameBoard(self):
        self.boardData = None


        self.gameBoardFrame = Frame(self.frame)
        self.gameBoardFrame.grid(row=1,column=0, sticky=N+S+W+E)

        self.gameBoard = GameBoardUI(self.gameBoardFrame, 30, 20, 32, "#BDC3C7","#ECF0F1",self)
        self.gameBoard.pack(side=TOP, fill=BOTH, expand="true", padx=4, pady=4)

        frameButton = Frame(self.frame)
        frameButton.grid(row=1, column=1)

        self.btnTeleport = Button(frameButton, text="Teleporter", command=self.notifyTeleport)
        self.styleButton(self.btnTeleport)
        self.btnTeleport.pack(fill=X)

        self.btnZap = Button(frameButton, text="Zapper", command=self.notifyZap)
        self.styleButton(self.btnZap)
        self.btnZap.pack(fill=X, pady=5)




    def refresh(self, gameboard, doctor, daleks, scrapHeaps, level):
        self.doctor = (doctor.position.x, doctor.position.y)
        self.btnTeleport['text'] = "Téléporter"
        self.btnZap['text'] = "Zapper"
        self.labelScore['text'] = "Crédits cosmiques: " + str(doctor.nbPoints)
        self.labelNbDaleks['text'] = "Nombre de Daleks: " + str(len(daleks))
        self.labelZappeur['text'] = "Zappeurs: " + str(doctor.nbZappeurs)
        self.labelWave['text'] = "Vague: " + str(level)
        self.generateMatrix(gameboard, doctor, daleks, scrapHeaps)
        self.gameBoard.draw(gameboard.x,gameboard.y)



    def generateMatrix(self, gameboard, dr, daleks, scrapHeaps):
        #Generate GUI Matrix from position, just for printing purpose
        self.boardData = [["." for i in range(gameboard.y)] for j in range(gameboard.x)]
        self.boardData[dr.position.x][dr.position.y] = self.DOCTOR
        for dalek in daleks:
                self.boardData[dalek.position.x][dalek.position.y] = self.DALEK
        for scrapHeap in scrapHeaps:
                self.boardData[scrapHeap.position.x][scrapHeap.position.y] = self.SCRAP_HEAP
        return self.boardData

    def printGameOver(self):
        self.parent.parent.withdraw()
        window = Window()
        window.mainFrame['background'] = 'red'
        self.doctorDeadImage = PhotoImage(file="img/Doctor.gif")
        self.labelDead = Label(window.mainFrame, compound="top",  text="Docteur! Vous êtes mort!")
        #self.labelDead.image = self.doctorDeadImage
        self.labelDead.pack()
        window.run()
        self.callback(UserAction.EXIT_GAME)


    # CALLBACKS FOR USER INPUT
    def notifyZap(self):
        self.callback(UserAction.ZAP)

    def notifyTeleport(self):
        self.callback(UserAction.TELEPORT)

    # Other events
    def notifyMove(self, event):

        userAction = None
        column = int(event.x/self.gameBoard.squareSize)
        row = int(event.y/self.gameBoard.squareSize)

        #detect direction
        if row < self.doctor[1]: #Move up
            if column < self.doctor[0]: #Move left
                userAction = UserAction.MOVE_NW

            elif column == self.doctor[0]: #Move only up
                userAction = UserAction.MOVE_N

            elif column > self.doctor[0]: #Move right
                userAction = UserAction.MOVE_NE

        elif row == self.doctor[1]: #Move either left or right or not at all
            if column < self.doctor[0]: #Move left
                userAction = UserAction.MOVE_W

            elif column == self.doctor[0]: #Does not move at all
                userAction = UserAction.MOVE_NULL

            elif column > self.doctor[0]: #Move right
                userAction = UserAction.MOVE_E


        elif row > self.doctor[1]: #Move down
            if column < self.doctor[0]: #Move left
                userAction = UserAction.MOVE_SW

            elif column == self.doctor[0]: #Move only down
                userAction = UserAction.MOVE_S

            elif column > self.doctor[0]: #Move right
                userAction = UserAction.MOVE_SE

        self.callback(userAction)










def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
