from Tkinter import *
import Tkinter
import tkMessageBox

class Mainmenu:

  def __init__(self, top):
    print 'menu'
    self.top = top
    self.generate()

  def generate(self):
    menubar = Menu(self.top)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="exit", command=self.top.quit)
    menubar.add_cascade(label="Filer", menu=filemenu)
    self.top.config(menu=menubar)

  def buttons(self, window):
    B = Tkinter.Button(window.top, text ="Select a directory to inspect:", command = window.start)
    B.pack()
    B = Tkinter.Button(window.top, text ="Back", command = window.back)
    B.pack()
