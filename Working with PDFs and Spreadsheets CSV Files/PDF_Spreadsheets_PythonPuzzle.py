import csv
import PyPDF2

# Task 1

data = open('/Users/PravinSelvarajah/Documents/GitHub/Python_Udemy_Bootcamp/Working with PDFs and Spreadsheets CSV Files/Exercise_Files/find_the_link.csv')

csv_data = csv.reader(data)

# Reformat the csv file as a list of lists
data_lines = list(csv_data)

print(data_lines)