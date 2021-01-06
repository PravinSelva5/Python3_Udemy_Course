import csv
import PyPDF2

###########
# Task 1 #
##########

data = open('/Users/PravinSelvarajah/Documents/GitHub/Python_Udemy_Bootcamp/Working with PDFs and Spreadsheets CSV Files/Exercise_Files/find_the_link.csv')

csv_data = csv.reader(data)

# Reformat the csv file as a list of lists
data_lines = list(csv_data)
link = ''


for num in range(len(data_lines)):
    link += data_lines[num][num]

print(link)

##########
# Task 2 #
##########

f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')

pdf_read = PyPDF2.PdfFileReader(f)

# Number of Pages
print(pdf_read.numPages)

import re

pattern = r'\d{3}.\d{3}.\d{4}'

all_text = ' '

for n in range(pdf_read.numPages):

    page = pdf_read.getPage(n)
    page_text = page.extractText()

    all_text = all_text + ' ' + page_text

for match in re.finditer(pattern,all_text ):
    print(match)

# all_text[41809:41808+20]   Looking at the pattern, regualr expression can be adjusted