#!/usr/bin/python
# -*- coding: utf-8 -*-
#Python 3.x
from tkinter import *
from tkinter import ttk
from GuiGoat import *

from Controller import *



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
        btnCLI = Button(frameButtons, compound="top", image=cliImage, text="CLI", command=self.launchCLI)
        btnCLI.image = cliImage
        self.styleButton(btnCLI)
        btnCLI.grid(row=0,column=0, pady=25, padx=25)

        #GUI BUTTON

        guiImage = PhotoImage(file="img/gui.gif")
        guiImage = guiImage.subsample(2, 2)
        btnGUI = Button(frameButtons, compound="top", image=guiImage, text="GUI", command=self.launchGUI)
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

    def launchCLI(self):
        launchCLI(self)

    def launchGUI(self):
        launchGUI(self)


def main():
    app = Launcher()
    app.run()

def launchCLI(app):
    app.parent.quit()
    game = Controller("CLI")
   
    

def launchGUI(app):
    app.parent.quit()
    game = Controller("GUI")



def quit():
    exit(0)

if __name__ == '__main__':
    main()
