import Tkinter
import tkMessageBox
from commander import Commander
from Tkinter import *

class Window:

  def __init__(self):
    top = Tkinter.Tk()
    self.set_top(top)
    self.set_text()
    top.geometry('{}x{}'.format(600, 600))
    B = Tkinter.Button(top, text ="Select a directory to inspect:", command = self.start)
    self.var.set('Select a directory to inspect...')

    B.pack()
    top.mainloop()

  def set_top(self, top):
    self.top = top

  def set_text(self):
    self.var = StringVar()
    self.label = Message(self.top, textvariable=self.var, width=600)
    self.label.pack(fill='x')

  def start(self):
    commander = Commander()
    text = commander.examine()
    self.var.set(text)

app = Window()

