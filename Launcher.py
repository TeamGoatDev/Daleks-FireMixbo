from tkinter import *
import os


def launchCLI():
    os.system('python Controller.py -cli')

def launchGUI():
    os.system('python Controller.py -gui')

def quit():
    exit(0)





class Launcher(Frame):
    """docstring for Launcher"""
    def __init__(self, parent):
        Frame.__init__(self,parent)

        self.parent = parent
        self.initUI()
        self.eventBind()


    def eventBind(self):
        self._drag_data = {"x": 0, "y": 0}
        self.titleText.bind("<ButtonPress-1>", self.OnButtonPress)
        self.titleText.bind("<ButtonRelease-1>", self.OnButtonRelease)
        self.titleText.bind("<B1-Motion>", self.OnMotion)


    def OnButtonPress(self, event):
        '''Being drag of an object'''
        # record the item and its location
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        print("OK")

    def OnButtonRelease(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def OnMotion(self, event):
        '''Handle dragging of an object'''
        # compute how much this object has moved
        delta_x = self._drag_data["x"] #event.x - 
        delta_y = self._drag_data["y"] #event.y - se
        print("X: %s Y: %s"%(delta_x,delta_y))
        # move the object the appropriate amount

        print()
        #self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        if(delta_x < 0):
            operatorX = "-"
        else:
            operatorX = "+"

        if(delta_y < 0):
            operatorY = "-"
        else:
            operatorY = "+"

       # delta_x *= 0.1
       # delta_y *= 0.1
        self.parent.geometry(operatorX + str(delta_x) + operatorY + str(delta_y)) 




        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y



    def initUI(self):
        self.parent.overrideredirect(True)
        SILVER = "#bdc3c7"
        MAIN_COLOR = "#c0392b"
        BACKGROUND_COLOR = "#ecf0f1"
        DARKER_GRAY = "#161b1e"
        DARK_GRAY = "#21262c"

        # TITLE BAR
        self.titleBar = Frame(self, bg=DARKER_GRAY)
        self.titleBar.pack(fill=X)

        self.titleText = Label(self.titleBar, text="O Daleks V.S. Doctor", bg=DARKER_GRAY, fg="#ecf0f1", width=95, anchor=W, justify=LEFT)
        self.titleText.grid(row=0,column=0, columnspan=20)

        btnClose = Button(self.titleBar, text="x", width=5, height=1,  fg="#ecf0f1", bg=MAIN_COLOR, borderwidth=0, command=self.quit)
        btnClose.grid(row=0,column=22, sticky=E)
        btnMinimise = Button(self.titleBar, text="_", width=5, height=1,  fg="#ecf0f1", bg=DARKER_GRAY, relief=SOLID, borderwidth=0)
        btnMinimise.grid(row=0,column=21)


        # LOGO BAR
        logoBar = Label(self, text="", bg=DARK_GRAY, fg="black")
        logoBar.pack(fill=X)


        # Frame Bas
        FrameBas = Frame(self,  bg=BACKGROUND_COLOR)
        FrameBas.pack(fill=X)

        #SIDE BAR
        sideBar = Frame(FrameBas, bg=DARKER_GRAY,  width=20, height=800)
        sideBar.pack(side=LEFT)

        spacer = Label(sideBar, text="", bg=DARKER_GRAY, height=30)
        spacer.grid(row=0, column=0)

        btnQuitter = Button(sideBar, text="Quitter", width=20, height=2, command=self.quit, fg="#ecf0f1", bg=MAIN_COLOR, borderwidth=0)
        btnQuitter.grid(row=1, column=0)


        #CENTER FRAME
        frameCentre = Label(FrameBas, text="Blue", bg=BACKGROUND_COLOR, fg="white")
        frameCentre.pack(side=LEFT)

        #CLI Button
        cliImage = PhotoImage(file="img/terminalBlack.gif")
        btnCLI = Button(frameCentre, text="CLI", width=20, height=2, relief=SOLID,  fg="#ecf0f1", bg=MAIN_COLOR, borderwidth=0)
        btnCLI.pack(side=LEFT, expand=1, padx=100)


        #GUI BUTTON
        btnGUI = Button(frameCentre, text="GUI", width=20, height=2,  fg="#ecf0f1", bg=MAIN_COLOR, borderwidth=0)
        btnGUI.pack(side=LEFT, expand=1)




        self.pack(fill=BOTH)
        

        
def main():
  


    root = Tk()
    root.geometry("750x536+30+30")
    app = Launcher(root)



    root.mainloop()  


if __name__ == '__main__':
    main() 
