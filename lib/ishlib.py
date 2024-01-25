import os
import shutil
import sys

def print_working_directory():
    print(os.getcwd())

def listdir(path):
    listdir = os.listdir(path)
    for i in listdir:
        print(listdir[i])