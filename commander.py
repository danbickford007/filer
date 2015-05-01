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
    text = self.run("du -h -d1 " + path)
    if len(text.split('\n')) <= 2:
      return self.run("ls -hal " + path)
    else: 
      return self.run("du -h -d1 " + path)

  def run(self, command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return process.communicate()[0]
