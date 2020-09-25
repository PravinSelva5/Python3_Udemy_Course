'''
Unzipping and Zipping Files

As you are probably aware, files can be compressed to a zip format. 
Often people use special programs on their computer to unzip these files, luckily for us, Python can do the same task with just a few simple lines of code.

'''


f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()


f = open('filetwo.txt', 'w+')
f.write('SECOND FILE')
f.close()

import zipfile

# Step 1: Create a compressed file

comp_file = zipfile.ZipFile('comp_file.zip', 'w')

comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()


# NOW HOW DO YOU UNZIP THE FILE?

zip_obj = zipfile.ZipFile('comp_file.zip')