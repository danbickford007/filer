import Tkinter
import tkMessageBox
from commander import Commander
from Tkinter import *

class Window:

  def __init__(self):
    top = Tkinter.Tk()
    self.set_top(top)
    self.set_text()
    top.geometry('{}x{}'.format(800, 800))
    B = Tkinter.Button(top, text ="Select a directory to start:", command = self.start)
    self.var.set('Select a directory to inspect...')

    B.pack()
    top.mainloop()

  def set_top(self, top):
    self.top = top

  def set_text(self):
    self.var = StringVar()
    self.frame = Frame(self.top, width=500)
    self.frame.pack_propagate(0) 
    self.label = Message(self.top, textvariable=self.var, relief=RAISED)
    self.label.pack(expand=YES)

  def start(self):
    commander = Commander()
    text = commander.examine()
    self.var.set(text)

app = Window()

