import os, shutil, re

# Open file with the instructions 
with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)


pattern = r'\d{3}-\d{3}-\d{4}'


# Search function that takes in a file and a pattern. Returns empty string if pattern not found
def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r' )
    text = f.read()
    
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ' '

# Empty list to hold numbers
results = []


# Go through files and append results of search function to results list

for folder, sub_folders, files in os.walk(os.getcwd()+'/extracted_content'):
    
    for f in files:
        full_path = folder + '/' + f
        
        results.append(search(full_path))


# Print out the phone number(s)
for r in results:
    if r != ' ':
        print(r.group())

