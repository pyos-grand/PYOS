import filestream
import ishlib
import os
import sys
import time
import faststream

def ls():
    path = input("Path: ")
    ishlib.listdir(path)

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