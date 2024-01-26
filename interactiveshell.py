import lib.filestream as fs
import lib.ishlib as ishlib
import lib.ishtools as ishtools
import os
import sys
import time
import fmtest

commands = {
    "ls":ishtools.ls,
    "apparto":ishtools.ls_legacy,
    "mkdir":ishtools.mkdir,
    "cf":ishtools.cf,
    "vf":ishtools.vf,
    "wf":ishtools.wf,
    "m":ishtools.loadmod,
    "fm":fmtest.function_select,
    "hfmi":fmtest.function_select,
    "help":ishtools.help,
    "exit":ishtools.exit
}

def console():
    print(r"""
 ______   __  __     ______     ______    
/\  == \ /\ \_\ \   /\  __ \   /\  ___\   
\ \  _-/ \ \____ \  \ \ \/\ \  \ \___  \  
 \ \_\    \/\_____\  \ \_____\  \/\_____\ 
  \/_/     \/_____/   \/_____/   \/_____/ 
                                          
""")
            print("Welcome to PyOS Oxygen Alpha (BUILD 250124)")
        elif logininfo == "false":
            pass
        else:
            print("Welcome to PyOS Oxygen Alpha (BUILD 250124)")
        
    while True:
        command = input("PyOS: ")
        if command in commands:
            commands[command]()
        else:
            print("Command not found. Type 'help' for a list of commands.")
