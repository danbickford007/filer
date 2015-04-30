import Tkinter
import tkMessageBox
from commander import Commander
from Tkinter import *

class Window:

  def __init__(self):
    self.labels = []
    top = Tkinter.Tk()
    self.set_top(top)
    self.set_text()
    self.menu()
    top.geometry('{}x{}'.format(600, 600))
    B = Tkinter.Button(top, text ="Select a directory to inspect:", command = self.start)
    self.var.set('Select a directory to inspect...')
    self.set_scroll()
    B.pack()
    top.mainloop()

  def menu(self):
    menubar = Menu(self.top)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="todo", command="")
    filemenu.add_command(label="exit", command=self.top.quit)
    menubar.add_cascade(label="Filer", menu=filemenu)
    self.top.config(menu=menubar)


  def set_scroll(self):
    scrollbar = Scrollbar(self.top)
    scrollbar.pack( side = RIGHT, fill=Y )

  def set_top(self, top):
    self.top = top

  def set_text(self):
    self.var = StringVar()
    self.label = Message(self.top, textvariable=self.var, width=600)
    self.label.pack(fill='x')

  def clean_labels(self):
    if self.labels:
      for index, i in enumerate(self.labels):
        i.destroy()

  def generate(self, files):
    self.clean_labels()
    for index, i in enumerate(files):
      label=Label(self.top, text=files[index])
      self.labels.append(label)
      if files[index]:
        label.bind("<Button-1>", lambda event, a=files[index]: self.text_callback(a))
        label.pack()

  def text_callback(self, fileCombo):
    commander = Commander()
    path = fileCombo
    if fileCombo.split('\t').count > 2:
      path = fileCombo.split('\t')[1]
    
    text = commander.examine_by_path(path)
    files = text.split('\n')
    self.generate(files)

  def start(self):
    commander = Commander()
    text = commander.examine()
    files = text.split('\n')
    self.generate(files)
    self.set_scroll()

app = Window()

