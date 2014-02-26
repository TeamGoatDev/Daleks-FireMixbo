#!/usr/bin/python
# -*- encoding: utf-8 -*-



from tkinter import *

class GoatCanvas(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent)

    def create_triangle(self, x,y, width, height, outlineColor,fillColor):
        points = [0+x, height+y,     int(width/2)+x, 0+y,     width+x,height+y ]
        self.create_polygon(points, outline=outlineColor, fill=fillColor, width=1)

    def create_square(self, x,y,width):
        self.create_rectangle(x,y,x+width,y+width)


class View(Frame):
    def __init__(self, parent=Tk()):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("DALEK vs DR. WHO")
        self.width  = 800
        self.height = 600
        self.parent.geometry(str(self.width)+"x"+str(self.height) )
        self.pack(fill=BOTH, expand=1)

        self.initCanvas()




    def initCanvas(self):
        canvas = GoatCanvas(self)
        #Stats bar


        # Gameboard

        gameboardWidth = self.width-50
        gameboardHeight = self.height-50
        gameboardPos = ((self.width-gameboardWidth)/2, (self.height-gameboardHeight)/2)


        canvas.create_rectangle(gameboardPos[0],gameboardPos[1],gameboardPos[0]+gameboardWidth,gameboardPos[1]+gameboardHeight, outline="#bdc3c7", fill="#ecf0f1")


        nbRows = 20
        nbCells = 30

        for j in range(nbCells):
            for i in range(nbRows):
                sizeX = gameboardWidth/nbRows
                sizeY = gameboardHeight/nbCells
                x1 = (i*sizeX)+gameboardPos[0]
                y1 = (j*sizeY)+gameboardPos[1]
                x2 = x1+sizeX
                y2 = y1+sizeY
                canvas.create_rectangle(x1,y1,x2,y2)
                # Dalek Test
                canvas.create_triangle(x1,y1,sizeX,sizeY,"#27ae60","#2ecc71")

        canvas.pack(fill=BOTH, expand=1)







if __name__ == '__main__':
    view = View()

    view.mainloop()