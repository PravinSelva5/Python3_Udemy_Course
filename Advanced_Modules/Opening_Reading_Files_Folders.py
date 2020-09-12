'''
# Opening and Reading Files

So far we've discussed how to open files manually, one by one.
 Let's explore how we can open files programatically. 
'''

# Create Practice File

f = open('practice.txt', 'w+')

f.write('test')
f.close()

# Getting Dictionaries

import os 

# get current directory pathway
os.getcwd()

# List directories of the path you provide within the parenthesis
os.listdir()

# MOVE FILES 

import shutil

# move function takes two parameters, source file & path the file should be moved to
shutil.move()

'''
 DELETING FILES

os.unlink(path) which deletes a file at the path your provide
os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. 
All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 
--------------------------------------------
Instead we will use the send2trash module. 
--------------------------------------------
A safer alternative that sends deleted files to the trash bin instead of permanent removal.

'''
import send2trash

# Check everything in your directory
# Create a file name 'filename.txt' before trying this
os.listdir()

send2trash.send2trash('filename.txt')

# Check if file is still in your directory
os.listdir()


'''
WALKING THROUGH A DIRECTORY
'''

os.getcwd()
for folder, sub_folders, files in os.walk("Example_Top_Level"):

    print("Currently looking at folder:"+ folder)
    print("\n")
    print("The subfolders are: ")

    for sub_fold in sub_folders:
        print(f"\tSubfolder: {sub_fold}")
    print('\n')
    print("the files are: ")
    
    for f in files:
        print(f"\tFile: {f}")
    print(\n)





