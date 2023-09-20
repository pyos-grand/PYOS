import os


def hfmstart():
  print("Please, use hfmi instead of hfm. 'hfm' support will end in 2024.")
  print("Humanity FileManager 0.0.4")
  print("1. Create file")
  print("2. Open file and write")
  print("3. Show file entries")
  print("4. Delete file")
  print("5. Make directory")
  print("6. Copy file")
  a = input(":")
  if (a == "1"):
    print("Type path")
    b = input(":")
    createFile(b)
  if (a == "2"):
    print("Type path")
    b = input(":")
    print("Type data")
    c = input(":")
    openFileandwrite(b, c)
  if (a == "3"):
    print("Type path")
    path = input(":")

    ffile = open(path, mode='r', encoding='utf-8')
    print(ffile.read())
  if (a == "4"):
    print("Type path")
    b = input(":")
    os.remove(b)
    print("Ok")
  if (a == "5"):
    print("Type 1st part of path")
    b = input(":")
    print("Type 2st part of path")
    c = input(":")
    print("Type name of directory")
    d = input(":")
    dir = os.path.join(b, c, d)
    if not os.path.exists(dir):
      os.mkdir(dir)
    print("Ok")
  if (a == "6"):
    print("Type original file")
    of = input(":")
    print("Type copied file path")
    cf = input(":")
    with open(of, 'r') as off:
      ofd = off.read()
    with open(cf, 'w') as cff:
      cff.write(ofd)

def createFile(filepath):
  with open(filepath, 'w') as f:
    f.write("")
  print("Ok")


def openFileandwrite(filepath, data):
  with open(filepath, 'w') as f:
    f.write(data)
  print("Ok")
