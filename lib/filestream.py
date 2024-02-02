import os
import shutil
import sys
import time

def show_dircontains(dirname):
    try:
        return os.listdir(dirname)
    except FileNotFoundError:
        return 0

def create_file(filename):
    try:
        with open(filename, "w") as file:
            return 1
    except IOError:
        return 0
    
def edit_file(filename, text):
    try:
        with open(filename, "w") as file:
            file.write(text)
            return 1
    except IOError:
        return 0
    
def delete_file(filename):
    try:
        os.remove(filename)
        return 1
    except IOError:
        return 0

def create_dir(filename):
    try:
        os.mkdir(filename)
        return 1
    except IOError:
        return 0
    
def delete_dir(filename):
    try:
        os.rmdir(filename)
        return 1
    except IOError:
        return 0
    
def rename_file(filename, newname):
    try:
        os.rename(filename,newname)
        return 1
    except IOError:
        return 0
    
def rename_dir(filename, newname):
    try:
        os.rename(filename,newname)
        return 1
    except IOError:
        return 0
    
def copy_file(filename, newname):
    try:
        shutil.copy(filename, newname)
        return 1
    except IOError:
        return 0
    
def copy_dir(filename, newname):
    try:
        shutil.copytree(filename, newname)
        return 1
    except IOError:
        return 0
    
def move_file(filename, newname):
    try:
        shutil.move(filename, newname)
        return 1
    except IOError:
        return 0
    
def move_dir(filename, newname):
    try:
        shutil.move(filename, newname)
        return 1
    except IOError:
        return 0
    
def show_filesize(filename):
    try:
        return os.path.getsize(filename)
    except IOError:
        return 0
    
def show_filestats(filename):
    try:
        return os.stat(filename)
    except IOError:
        return 0
    
def show_filecontents(filename):
    try:
        file = open(filename,"r")
        return file.read()
        file.close()
    except IOError:
        return 0

def show_dirsize(dirname):
    try:
        return os.path.getsize(dirname)
    except IOError:
        return 0
    

    
  