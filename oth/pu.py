import os
def updpack(list):
  with open('oth/middle/newpackages.txt') as f:
    line = f.readline()
    if (line != ""):
      print("Loading packages")
      print("Running a packages installation, please wait...")
      with open("oth/"+line+"installerpu.py") as f23:
        exec(f23.read())
    else:
      pass    

def grandmost(packname):
  filename = packname+"runpu.py"
  with open(filename) as f2:
    exec(f2.read())