#################################
# Grep.py
# Author: Shovik Shyamsundar, David Seiavitch, Ignacio Rosas
# CSCI 4760
#################################

import sys
import re
import glob
import os.path

if len(sys.argv) == 3:
    pattern = sys.argv[1]

    fileList = glob.glob(sys.argv[2])
    if not fileList:
            print ("No such file or directory")
    
    for fl in fileList:
        """Opening a file in directory."""

        file = open(fl, "r").readlines()
       
        for line in file:
            """Prints line if pattern is found is line."""
            if re.search(pattern, line):
                print (fl + ": " + line)
    

elif len(sys.argv) == 4:
    if sys.argv[1] == "-v":
        pattern = sys.argv[2]
     

        fileList = glob.glob(sys.argv[3])
        if not fileList:
            print ("No such file or directory")
            
        for fl in fileList:
            """Opening a file in directory."""
            if not os.path.isfile(fl):
                print ("No such file or directory")
            file = open(fl, "r").readlines()
       
            for line in file:
                """Prints line if pattern is not found is line."""
                if not re.search(pattern, line):
                    print (fl + ": " + line)
    
    elif sys.argv[1] == "-x":
        pattern = sys.argv[2]
        
        fileList = glob.glob(sys.argv[3])
        if not fileList:
            print ("No such file or directory")
        
        for fl in fileList:
            """Opening a file in directory."""
            if not os.path.isfile(fl):
                print ("No such file or directory")
            file = open(fl, "r").readlines()
            
            for line in file:
                """Prints line if pattern matches line exactly."""
                if pattern == line:
                    print (sys.argv[2] + ": " + line)

    else:   
        print("Usage: ./Grep.py [option] [string] [filename]")

else:
    print("Usage: ./Grep.py [option] [string] [filename]")
                
