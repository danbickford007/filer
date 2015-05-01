import subprocess
import tkFileDialog

class Commander:

  def __init__(self):
    print "Commanding..." 
    self.history = []

  def ls(self):
    bashCommand = "ls"
    return self.run(bashCommand)

  def examine(self):
    path = tkFileDialog.askdirectory()
    self.history.append(path)
    return self.run("du -h -d1 " + path)

  def examine_by_path(self, path):
    self.history.append(path)
    text = self.run("du -h -d1 " + path)
    if len(text.split('\n')) <= 2:
      return self.run("ls -hal " + path)
    else: 
      return self.run("du -h -d1 " + path)

  def back(self):
    del self.history[-1]
    path = self.history[len(self.history) - 1]
    return self.run("du -h -d1 " + path)

  def run(self, command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return process.communicate()[0]
