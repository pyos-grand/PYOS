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
def loadmod():
    modpath = input("Please, enter mod path.")
    with open(modpath) as f2:
        exec(f2.read())

def help():
    print("ls - Show directory entries")
    print("cf - Create file")
    print("m - Load mod")
    print("help - Show this help message")
    print("exit - Exit PyOS")

def exit():
    sys.exit()