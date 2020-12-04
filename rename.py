#imports
import os
import re
import sys
from platform import system
"""I made this script because I was tired of removing some small text
from A long list of filenames.

To use this program correctly, go to the folder where you want to remove text from
files and execute the python file.  Before the program makes changes it will tell
you what it's going to change before it does it.
"""
#Variables
move_cmd = "mv"

if system() == 'Windows':
    move_cmd = "move"

#this raw_input captures the string to remove
text_remove = raw_input('What string would you like to remove (Use "quotes if there is a space".)? ')

#initializing the lists
change = []
nochange = []#I don't use this but it could be useful
commands = []

#This for loop captures all the file names in the dir and fills up the list above.
for filename in os.listdir("."):

    if text_remove in filename:
        new_name = re.sub(text_remove, '', filename)
        change.append(new_name)
        commands.append(("{0} \"{1}\" \"{2}\"").format(move_cmd,filename,new_name))
    else:
        nochange.append(filename)
#Checking for a match and printing a warning to let you know what the script woud do.
if len(commands) > 0:
    print ("")
    print ("")
    print ("Commands to be executed:")
    for command in commands:
        print command
    print ("")
    cont = raw_input('Would you like to continue (y/n)? ')
else:
    print ("No matches found")
    quit()
#if y then we run the commands.
if cont.lower() == 'y':
    for command in commands:
        os.system(command)

#Error capture
else:
    print ("You selected n or an invalid value. Script Stopped")
