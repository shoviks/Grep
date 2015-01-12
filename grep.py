#################################
# Grep.py
# Author: Shovik Shyamsundar
# CSCI 4760
#################################

import sys
import re

if len(sys.argv) == 3:
    pattern = sys.argv[1]

    file = open( sys.argv[2], "r" ).readlines()

    for line in file:
        """Prints line if pattern is found is line."""
        if re.search(pattern, line):
            print (line)

elif len(sys.argv) == 4:
    if sys.argv[1] == "-v":
        pattern = sys.argv[2]
        file = open( sys.argv[3], "r" ).readlines()

        for line in file:
            """Prints line if pattern is not found in line."""
            if not re.search(pattern, line):
                print (line)
    
    elif sys.argv[1] == "-x":
        pattern = sys.argv[2]
        file = open( sys.argv[3], "r" ).readlines()

        for line in file:
            """Prints line if pattern matches line exactly."""
            if pattern == line:
                print (line)

 
