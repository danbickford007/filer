import Tkinter
import tkMessageBox
from commander import Commander
from Tkinter import *

class Window:

  def __init__(self):
    top = Tkinter.Tk()
    self.set_top(top)
    self.set_text()
    self.menu()
    top.geometry('{}x{}'.format(600, 600))
    B = Tkinter.Button(top, text ="Select a directory to inspect:", command = self.start)
    self.var.set('Select a directory to inspect...')

    B.pack()
    top.mainloop()

  def menu(self):
    menubar = Menu(self.top)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="todo", command="")
    filemenu.add_command(label="exit", command=self.top.quit)
    menubar.add_cascade(label="Filer", menu=filemenu)
    self.top.config(menu=menubar)
#     mb=  Menubutton ( self.top, text="menu", relief=RAISED )
#     mb.grid()
#     mb.menu  =  Menu ( mb, tearoff = 0 )
#     mb["menu"]  =  mb.menu
#     mb.pack()
#
#     mb.add_command(label="Quit", command="sys.exit(0)")   

#  
#     mb.menu.add_checkbutton ( label="look for offenders",
#                           variable=1 )
#     mb.menu.add_checkbutton ( label="exit",
#                               variable="exit()" )


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

