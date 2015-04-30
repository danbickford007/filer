import subprocess
import tkFileDialog

class Commander:

  def __init__(self):
    print "Commanding..." 

  def ls(self):
    bashCommand = "ls"
    return self.run(bashCommand)

  def examine(self):
    path = tkFileDialog.askdirectory()
    return self.run("du -h -d1 " + path)

  def examine_by_path(self, path):
    return self.run("du -h -d1 " + path)

  def run(self, command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return process.communicate()[0]
