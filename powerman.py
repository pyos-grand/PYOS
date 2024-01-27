import os
import sys
import time
import lib.filestream as fs
import interactiveshell as shell
import fmtest

def maintools():
    ascii = """
    
    """
    print(ascii)
    modes = """
    1. Text editor
    2. Shell
    3. Other tools
    4. Exit powerman
    """
    while (True):
        modechoose = input("Tool: ")
        if (modechoose == "1"):
            text_editor()
        elif (modechoose == "2"):
            interactiveshell.console()
        elif (modechoose == "3"):
            pass
        elif (modechoose == "4"):
            exit()

def text_editor():
    fmtest.function_select()

def powerselect():
    print("Select Mode")
    modes = """
    1. Text editor, shell and tools
    2. Text editor
    """
    modechoose = input("Mode: ")
    if (modechoose == "1"):
        maintools()
    elif (modechoose == "2"):
        pass
    elif (modechoose == "3"):
        pass
    else:
        pass

def powerstart():
    ascii = """
  _____                                             
 |  __ \                                            
 | |__) |____      _____ _ __ _ __ ___   __ _ _ __  
 |  ___/ _ \ \ /\ / / _ \ '__| '_ ` _ \ / _` | '_ \ 
 | |  | (_) \ V  V /  __/ |  | | | | | | (_| | | | |
 |_|   \___/ \_/\_/ \___|_|  |_| |_| |_|\__,_|_| |_|
                                                    
                                                    
"""
    print(ascii)
    print("POWERMAN v. 0.0.1")
    print("(c) 2024 PyOS developers")
    


    
