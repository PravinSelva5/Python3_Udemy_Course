'''
Libraries to consider when working with CSV files:
   - built-in csv module in Python
   - Pandas
        - Full data analysis library, can work with almost any tabular data type.
        - Runs visualizations and analysis
   - Openpyxl
        - specifically designed for excel files
        - retains a lot of Excel specific functionality
        - Supports Excel formulas
   - Google Sheets Python API
        - allows you to directly make changes to the spreadsheets hosted online

   - CSV 
        - Comma Separated Variables
        - csv only contains the raw data from spreadsheet

Other Libraries to consider is Pandas, openpyxl, google sheets python api

'''

import csv 

# Open File
data = open('example.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# print(data_lines)

for line in data_lines[:5]:
     print(line)

# At index 3, is where all the emails are. So to get all the emails in the list
all_emails = []

for line in data_lines[1:]:
     all_emails.append(line[3])

# print(all_emails)

