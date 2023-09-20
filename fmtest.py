import os
import sys

def function_select():
    print("Humanity FileManagerIMROVED 0.0.1")
    print("(c) 2023 PyOS develiopers and Roman Zeldinov (aka) WowInceptionGood")
    print("1. Show directory contents")
    print("2. Create file")
    print("3. Edit file")
    print("4. Delete file")
    print("5. Create directory")
    print("6. Delete directory")
    print("7. Rename file")
    print("8. Rename directory")
    print("9. Copy file")
    print("10. Copy directory")
    print("11. Move file")
    print("12. Move directory")
    print("13. Show file contents")
    print("14. Show file size")
    print("15. Show file stats")
    print("16. Show directory size")
    choice = input("Enter choice: ")
    if choice == "1":
        show_dircontains()
    elif choice == "2":
        create_file()
    elif choice == "3":
        edit_file()
    elif choice == "4":
        delete_file()
    elif choice == "5":
        create_dir()
    elif choice == "6":
        delete_dir()
    elif choice == "7":
        rename_file()
    elif choice == "8":
        rename_dir()
    elif choice == "9":
        copy_file()
    elif choice == "10":
        copy_dir()
    elif choice == "11":
        move_file()
    elif choice == "12":
        move_dir()
    elif choice == "13":
        show_filecontents()
    elif choice == "14":
        show_filesize()
    elif choice == "15":
        show_filestats()
    elif choice == "16":
        show_dirsize()
    else:
        print("Invalid choice!")
def show_dircontains():
  direname = input("Enter dirname: ")
  print(os.listdir(direname))

def create_file():
  filename = input("Enter filename: ")
  file = open(filename,"w")
  file.close()
  print("File created!")

def edit_file():
  filename = input("Enter filename: ")
  file = open(filename,"w")
  file.write(input("Enter text: "))
  file.close()
  print("File edited!")

def delete_file():
  filename = input("Enter filename: ")
  os.remove(filename)
  print("File deleted!")

def create_dir():
  dirname = input("Enter dirname: ")
  os.mkdir(dirname)
  print("Directory created!")

def delete_dir():
    dirname = input("Enter dirname: ")
    os.rmdir(dirname)
    print("Directory deleted!")

def rename_file():
  filename = input("Enter filename: ")
  newname = input("Enter new filename: ")
  os.rename(filename,newname)
  print("File renamed!")

def rename_dir():
  dirname = input("Enter dirname: ")
  newname = input("Enter new dirname: ")
  os.rename(dirname,newname)
  print("Directory renamed!")

def copy_file():
  filename = input("Enter filename: ")
  newname = input("Enter new filename: ")
  os.system("cp "+filename+" "+newname)
  print("File copied!")

def copy_dir():
  dirname = input("Enter dirname: ")
  newname = input("Enter new dirname: ")
  os.system("cp -r "+dirname+" "+newname)
  print("Directory copied!")    

def move_file():
  filename = input("Enter filename: ")
  newname = input("Enter new filename: ")
  os.system("mv "+filename+" "+newname)
  print("File moved!")  

def move_dir():
    dirname = input("Enter dirname: ")
    newname = input("Enter new dirname: ")
    os.system("mv "+dirname+" "+newname)
    print("Directory moved!")

def show_filecontents():
  filename = input("Enter filename: ")
  file = open(filename,"r")
  print(file.read())
  file.close()

def show_filesize():
  filename = input("Enter filename: ")
  print(os.path.getsize(filename))

def show_filestats():
  filename = input("Enter filename: ")
  print(os.stat(filename))

def show_dirsize():
  dirname = input("Enter dirname: ")
  print(os.path.getsize(dirname))
