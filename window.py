import Tkinter
import tkMessageBox
from commander import Commander
from mainmenu import Mainmenu
from Tkinter import *

class Window:

  def __init__(self):
    self.labels = []
    top = Tkinter.Tk()
    self.commander = Commander()
    self.set_top(top)
    self.menu()
    top.geometry('{}x{}'.format(600, 600))
    top.configure(bg='#445566')
    top.mainloop()

  def menu(self):
    mainmenu = Mainmenu(self.top)
    mainmenu.buttons(self);
  def set_top(self, top):
    self.top = top
    self.scrollbar = Scrollbar(self.top)
    self.scrollbar.pack( side = RIGHT, fill=Y )
    self.mylist = Listbox(self.top, yscrollcommand = self.scrollbar.set, width=600 )

  def clean_labels(self):
    index = 0
    for i in self.fileArray:
      self.fileArray.delete(index)
      index += 1
    self.mylist.delete(0, END)

  def generate(self, files):
    self.fileArray = []
    self.clean_labels()
    for index, i in enumerate(files):
       self.mylist.insert(END, files[index])
       self.fileArray.append(files[index])
    self.mylist.bind('<<ListboxSelect>>', lambda event, a=self.mylist: self.text_callback(a))
    self.mylist.pack( side = LEFT, fill = BOTH )
    self.scrollbar.config( command = self.mylist.yview )

  def text_callback(self, fileCombo):
    fileCombo = self.fileArray[int(fileCombo.curselection()[0])]
    path = fileCombo
    if fileCombo.split('\t').count > 2:
      path = fileCombo.split('\t')[1]
    
    text = self.commander.examine_by_path(path)
    files = text.split('\n')
    self.generate(files)

  def start(self):
    text = self.commander.examine()
    files = text.split('\n')
    self.generate(files)

  def back(self):
    text = self.commander.back()
    files = text.split('\n')
    self.generate(files)

app = Window()

