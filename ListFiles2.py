#!/usr/bin/env python3
#The OS module  built-in library within Python makes available different functions that are used to communicate with the operating system. 
# This module is part of Python’s standard utility modules.

#os module to collect information about the files in our current working directory.
# The os.getcwd() method is one of the functions which the OS module provides.
import os
import json
import datetime

# get current working dir (same as pwd in linux but) in python it is function getcwd() of OS module
mydir = str(input("enter the directory full path: "))
#print (mydir)

if mydir == '':
    print ("you have not entered dir path, thus we will take current dir as selected.")
    mydir = os.getcwd()
    print ("my dir is : ",mydir)

else:
    print ("you have selected directory : ",mydir)
    #sys.exit()

# Create an empty list which we will later be using to add file related info
list_files = []

# os.scandir() function – a better and faster directory iterator/current working dir
for file in os.scandir(mydir):
        
# Get the file path, file name, and size
        file_path = str(file.path)
        file_name = str(file.name)
        file_size = str(file.stat().st_size)
        #file_date = convertDate(file.stat().st_date)

# file info is a veriable which will have the file information
        file_details = {"file name is - "+ file_name + " , file size is - "+ file_size + " bytes, and file path is - "+file_path}
                                    
# Append/add list of files in to the empty dictionary
        list_files.extend(file_details)

# Print the list of files, printed onto separate lines
print ("you have total : " + str(len(list_files)) + " files.")
#print(*list_files, sep="\n")

# print the list of file in Json format and save the output into a filelist.json
filedata = json.dumps(list_files, indent=4)
print()
print("now printing filedata in JSON: ")
print(filedata)
