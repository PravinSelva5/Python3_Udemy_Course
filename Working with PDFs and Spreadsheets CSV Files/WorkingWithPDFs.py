'''
- PyPDF2 is an open-source library
- Images, tables, format adjustment can render a PDF unreadable by Python
'''
import PyPDF2

f = open('Working_Business_Proposal.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)

pdf_reader.numPages

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extract_text()

print(page_one_text)

# You can't go into a PDF page and write in the middle of the document with this open source library.
