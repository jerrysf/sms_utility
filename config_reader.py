#Usage:
#1st: import this module
#2nd: using config['variable_name']

import sys

#Define global variable
#Using Dictionary to store parameter from config file
global config

config = {}
    
def reader(file_name):
    
    file = open(file_name, 'r')
    
    for line in file:
        if line == "\n":
            continue
        elif "[" in line:
            continue
        elif "#" in line:
            continue
        else:
            config[line.split("=")[0]]=line.split("=")[1].rstrip()
        
if __name__ == "__main__":
    reader(sys.argv[1])
    #self testing code here
    #e.g., print config['test']