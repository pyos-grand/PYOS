import husr
import hfm
import htxe
import os
import pysys
import hetools
import oth.pu

def apparto():
  appartoz()


def info_username(logginguser):
  print(logginguser)


def husrc():
  print("Humanity UserManager 0.0.4")


def hsrm():
  print("Humanity ServiceManager 0.0.4")


def husr_create_user(logginguser):
  husr.FirstCreating()
  logginguser = husr.user2


def husr_reset_user(logginguser):
  husr.ResetUser()
  logginguser = husr.user2


def sys_set_username(logginguser,husr_user2):
  logginguser = husr_user2


def hfmc():
  hfm.hfmstart()

def cf():
  pathff = input("")
  hetools.cf(pathff)

def info_sys_systemdirectory():
  cwd = os.getcwd()
  print(cwd)

def vfe():
  filep = input()
  hetools.vf(filep)
  
def htxec():
  htxe.starthtxe()

def wfx():
  filepc = input(" :Filepath")
  datac = input(" :Data")
  hetools.wf(filepc,datac)
def make_directory():
  directory_name = input("Enter directory name: ")
  pysys.md(directory_name)

def infop():
  print("GRAND System Information Program version 0.0.5")

def loadmod():
  print("WARNING! This feature is in beta!")
  modpath = input()
  pysys.loadmod(modpath)

def help():
  print("listdir - Show directory entries")
  print("husr - Humanity UserManager")
  print("hsrm - Humanity ServiceManager")
  print("hfm - Humanity FileManager")
  print("htxe - Humanity TextEditor")
  print("info - Information Programm")

def dellog():
  print("Deleting log")
  print(".")
  os.remove("logs/log.psdf")
  print("..")
  os.remove("logs/pyos-log.log")
  print("...")

def ip():
  package = input(":")
  print("Adding package to newpackages file...")
  with open("oth/middle/newpackages.txt", 'w') as cff:
      cff.write(package)
  print("Done! Now restart, to start package installation")  

def ipm():
  package = input(":")
  print("Running a package installation, please wait...")
  with open("oth/"+package+"installerpu.py") as f23:
    exec(f23.read())
commands = {
  "dir": apparto,
  "info husr.username": info_username,
  "husr": husrc,
  "hsrm": hsrm,
  "hsrm husr.createuser": husr_create_user,
  "hsrm husr.resetuser": husr_reset_user,
  "hsrm sys.SetUsername\husr.user2": sys_set_username,
  "hfm": hfmc,
  "info sys.systemdirectory": info_sys_systemdirectory,
  "htxe": htxec,
  "mkdir": make_directory,
  "help": help,
  "info": infop,
  "vf": vfe,
  "wf": wfx,
  "cf": cf,
  "sysutil dellog": dellog,
  "sysutil loadmod": loadmod,
  "sut lm": loadmod,
  "m": loadmod,
  "insp": ip,
  "inspm": ipm,
}


def console(logginguser):
  while True:
    user_input = input(":")
    if user_input in commands:
      commands[user_input]()
    else:
      print("Invalid command. Type 'help' for a list of commands.")


def run():
  if not os.path.exists("logs"):
    os.mkdir("logs")
  print("   ___ __  __ ____   ____")
  print("  / _ \\ \/ // __ \ / __/")
  print(" / ___/ \  // /_/ /_\ \  ")
  print("/_/     /_/ \____//___/  ")
  oth.pu.updpack(commands)
  print("PYOS PC Olivia 0.1 - PYOS BUILD 19042023, GRAND 0.0.5")
  print("User Creation System: Create user")
  logginguser = input("USERNAME : ")
  isUserLoggedOn = False
  husr.user2 = logginguser
  logginguser = husr.user2
  print("Log on:")
  while (isUserLoggedOn != True):
    inputuser = input()
    logginguser = inputuser
    pastlogvalue = ""
    newlogvalue = "PYOS-PC-0.0.5-Log:"
    pysys.UpdateLog("logs/log.psdf", newlogvalue)
    pastlogvalue = newlogvalue
    if (inputuser == husr.user2 or inputuser == husr.user1
        or inputuser == husr.user3):
      newlogvalue = f"USERNAME REGISTERED: {inputuser}"
      sod = pastlogvalue, "END", newlogvalue
      pysys.UpdateLog("logs/pyos-log.log", str(sod))
      isUserLoggedOn = True
      console(logginguser)

    else:

      print("INVALID USERNAME")
      print("Log into your user")
      inputuser = input()
      logginguser = inputuser
      if (inputuser == husr.user2 or inputuser == husr.user1
          or inputuser == husr.user3):
        newlogvalue = "USERNAME REGISTERED:", inputuser
        sod = pastlogvalue, "END", newlogvalue
        pysys.UpdateLog("logs/log.psdf", str(sod))
        isUserLoggedOn = True
        console(logginguser)


def appartoz():
  print("Path: ")
  path = input()
  print(os.listdir(path))
