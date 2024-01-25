from lib import ishlib
import os
import sys
import time
from lib import faststream

def ls():
    listdir = os.listdir(input("Path: "))
    for i in listdir:
        print(i)

def cf():
    pathff = input("Path: ")
    faststream.cf(pathff)

def vf():
    pathff = input("Path: ")
    faststream.vf(pathff)

def wf():
    pathff = input("Path: ")
    datac = input("Data: ")
    faststream.wf(pathff,datac)

def loadmod():
    modpath = input("Please, enter mod path.")
    with open(modpath) as f2:
        exec(f2.read())

def help():
    print("ls - Show directory entries")
    print("hfmi - Humanity FileManager Improved")
    print("cf - Create file")
    print("vf - View file")
    print("wf - Write file")
    print("m - Load mod")
    print("help - Show this help message")
    print("exit - Exit PyOS")

def exit():
    sys.exit()