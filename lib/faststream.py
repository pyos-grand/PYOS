import os
import shutil
def vf(fp):
  print("ViewFast: " + fp)
  file = open(fp, mode='r', encoding='utf-8')
  print(file.read())

def wf(fp,data):
  print("WriteFast: " + fp)
  with open(fp, 'w') as f:
    f.write(data)


def cf(fp):
  print("CreateFast: "+fp)
  with open(fp, 'w') as f:
    f.write("")