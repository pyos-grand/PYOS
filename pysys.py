import os
import htxe
import husr
import hfm


def md(path):
  if not os.path.exists(path):
    os.mkdir(path)


def UpdateLog(path, logdata):
  with open(path, 'w') as f:
    f.write(logdata)

def loadmod(pathe):
  with open(pathe) as f2:
    exec(f2.read())