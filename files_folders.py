#!/usr/bin/python3 

# Let us practice the creation of files, folders and adding content

import os 

os.system("touch kenya.txt")

os.system("exit")

os.remove("kenya.txt")

os.system(" echo =================================================================")

file_name = "configuration.sh"
file = open(file_name,"w")
content = "\n this file will be used to configure the system"
file.write(content)
file.close()


# Let open another file and edit the content

file_name = "mango.txt"
file = open(file_name,"w")
content = "\n today is staurday"
file.write(content)
file.close()

# Let create folder

import os 
folder_name = "mango"
os.mkdir(folder_name)

print ("====================================================")

import os
# We start by defining the folder and file name

folder_name = "Apple"
file_name = "file.txt"

# Let us now create the folder 

os.mkdir(folder_name)

# Create a file inside the folder
# Let us now define the path 

file_path = os.path.join(folder_name,file_name)

file = open(file_path, "w")
content = "\n Tylor swift is a great musician and commanded a huge crowd in the last concert"
file.write(content)
file.close()



