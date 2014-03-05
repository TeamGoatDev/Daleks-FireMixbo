<<<<<<< HEAD
#Python 3.x
from tkinter import *
from tkinter import ttk
from GuiGoat import *

class Launcher(object):
    """A simple launcher to start the Game either in Graphical Mode or in a Command Line Interface"""
    def __init__(self):
        self.parent = Window()
        self.initUI()


    def styleButton(self, button):
        BTN_PRIMARY = "#c0392b"
        button['background'] = BTN_PRIMARY
        button['borderwidth'] = 0
        button['foreground'] = "#ecf0f1"


    def run(self):
        self.parent.run()

    def initUI(self):
        self.height = 600
        self.width = 500

        #SIDE BAR
        sideBar_width = 160
        frameSideBar = Frame(self.parent.mainFrame, width=sideBar_width, height=self.height)
        frameSideBar['background'] = "#161B1E"
        frameSideBar.grid(row=2,column=0)


        #CENTER AREA    
        frameCenter = ttk.Frame(self.parent.mainFrame, width=self.width-sideBar_width, height=self.height)
        frameCenter.grid(row=2, column=1, rowspan=2, columnspan=2, sticky=N+S )

        frameButtons = Frame(frameCenter)
        frameButtons.grid(column=0, row=0, sticky=(N, W, E, S))
        frameButtons.columnconfigure(0, weight=1)
        frameButtons.rowconfigure(0, weight=1)

        #CLI Button
        cliImage = PhotoImage(file="img/terminal.gif")
        cliImage = cliImage.subsample(2, 2)
        btnCLI = Button(frameButtons, compound="top", image=cliImage, text="CLI")
        btnCLI.image = cliImage
        self.styleButton(btnCLI)
        btnCLI.grid(row=0,column=0, pady=25, padx=25)

        #GUI BUTTON

        guiImage = PhotoImage(file="img/gui.gif")
        guiImage = guiImage.subsample(2, 2)
        btnGUI = Button(frameButtons, compound="top", image=guiImage, text="GUI")
        btnGUI.image = guiImage
        self.styleButton(btnGUI)
        btnGUI.grid(row=0,column=1, pady=25, padx=25)

        texte = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse bibendum, mauris in varius dictum, justo quam convallis urna, in ultricies sapien augue non lectus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 
        Ut fringilla diam a diam ultrices sodales. Maecenas adipiscing ante elementum congue pharetra. 
        Morbi aliquet lacus et elementum auctor. Etiam vitae interdum lacus. Maecenas euismod blandit leo, 
        quis facilisis nisl auctor in. """
        labelDescription = Label(frameButtons, justify=LEFT, text=texte, wraplength=500, foreground="#21262C")
        labelDescription.grid(row=1,column=0, sticky=N+W, columnspan=2, padx=25 )

        #QUIT BUTTON  
        btnQuit = Button(self.parent.mainFrame, text="Quitter", command=self.parent.quit, height=2)
        self.styleButton(btnQuit)
        btnQuit.grid(row=3, column=0, sticky=E+W)



def main():
    app = Launcher()
    app.run()

if __name__ == '__main__':
    main()
=======
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
>>>>>>> e08d610b4bafe9953cccf45b64c66b805e512c06
