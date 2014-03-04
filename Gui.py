#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Python 3.x
from tkinter import *
from tkinter import ttk
from GuiGoat import *


COLOR_PRIMARY = "#c0392b" #


class GameBoardUI(Frame):
    """docstring for GameBoardUI"""
    def __init__(self, parent, rows,columns, squareSize, background,foreground):
        self.rows = rows
        self.columns = columns
        self.squareSize = squareSize
        self.background = background
        self.foreground = foreground

        self.scrapHeap = []
        self.daleks = []
        self.doctor = None



        canvasWidth = columns * squareSize
        canvasHeight = rows * squareSize

        Frame.__init__(self,parent)
        self.canvas = Canvas(self, width=canvasWidth, height=canvasHeight, background=self.background)
        self.canvas.pack(fill=BOTH, expand=True)
        self.draw()

    def drawDoctor(self, x,y):
        self.img = PhotoImage(file="img/doctor2.gif")
        scale_w = int(self.img.width()/self.squareSize)
        scale_h = int(self.img.height()/self.squareSize)
        print(scale_w, scale_h)
        self.img = self.img.subsample(scale_w,scale_h)
        self.canvas.create_image((x+self.img.width()/2,y+self.img.height()/2), image=self.img)

    def drawDalek(self, x,y):
        self.img = PhotoImage(file="img/dalek.gif")
        scale_w = int(self.img.width()/self.squareSize)
        scale_h = int(self.img.height()/self.squareSize)
        self.img = self.img.subsample(scale_w,scale_h)
        self.canvas.create_image((x+self.img.width()/2,y+self.img.height()/2), image=self.img)


    def drawScrapHeap(self, x,y):
        self.img = PhotoImage(file="img/scrapHeap.gif")
        scale_w = int(self.img.width()/self.squareSize)
        scale_h = int(self.img.height()/self.squareSize)
        self.img = self.img.subsample(scale_w,scale_h)
        self.canvas.create_image((x+self.img.width()/2,y+self.img.height()/2), image=self.img)    


    def draw(self):
        self.canvas.delete()
        for row in range(self.rows):
            for column in range(self.columns):
                x1 = (column * self.squareSize)
                y1 = (row * self.squareSize)
                x2 = x1 + self.squareSize
                y2 = y1 + self.squareSize
                self.canvas.create_rectangle(x1,y1,x2,y2, outline=self.background, width=2,
                    fill=self.foreground, activefill=COLOR_PRIMARY, tags="cell")
                if row == self.rows/2:
                	if column == self.columns/2:
                		self.drawDoctor(x1,y1)
                


        


class App(object):
    """docstring for App"""
    def __init__(self):
        self.parent = Window()
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
  

        self.labelScore = Label(frameStats, text="Crédits cosmiques:", width=35, background=frameStats.color)
        self.labelScore.grid(row=0,column=0, sticky=N+W+E)



        self.labelNbDaleks = Label(frameStats, text="Nombre de Daleks:", width=42, background=frameStats.color)
        self.labelNbDaleks.grid(row=0,column=1)


        self.labelWave = Label(frameStats, text="Vague:",  width=35, background=frameStats.color)
        self.labelWave.grid(row=0,column=2, sticky=E) 

        self.labelZappeur = Label(frameStats, text="Zappeur:",  width=35, background=frameStats.color)
        self.labelZappeur.grid(row=0,column=3, sticky=E) 

        

    def initGameBoard(self):
        self.gameBoardFrame = Frame(self.frame)
        self.gameBoardFrame.grid(row=1,column=0, sticky=N+S+W+E)

        gameBoard = GameBoardUI(self.gameBoardFrame, 20, 30, 32, "#BDC3C7","#ECF0F1")
        gameBoard.pack(side=TOP, fill=BOTH, expand="true", padx=4, pady=4)

        frameButton = Frame(self.frame)
        frameButton.grid(row=1, column=1)

        self.btnTeleport = Button(frameButton, text="Teleporter")
        self.styleButton(self.btnTeleport)
        self.btnTeleport.pack(fill=X)

        self.btnZap = Button(frameButton, text="Zapper")
        self.styleButton(self.btnZap)
        self.btnZap.pack(fill=X, pady=5)


def main():
    app = App()
    app.run()

    
if __name__ == '__main__':
    main()
