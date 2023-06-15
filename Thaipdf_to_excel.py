# from PyPDF2 import PdfReader
# from openpyxl import Workbook

# def extract_table_data(page_text):
#     # Implement your custom logic to extract table data from the page text
#     # This could involve using regular expressions or specific string operations

#     # Here's a dummy implementation that splits the text by newline and space
#     table_data = [row.split(' ') for row in page_text.split('\n')]

#     return table_data

# pdf_file = 'table.pdf'
# pdf = PdfReader(pdf_file)

# total_pages = len(pdf.pages)

# workbook = Workbook()
# sheet = workbook.active

# for page_number in range(total_pages):
#     page = pdf.pages[page_number]
#     text = page.extract_text()

#     table_data = extract_table_data(text)

#     for row in table_data:
#         sheet.append(row)

# excel_file = 'table.xlsx'
# workbook.save(excel_file)

import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('table.pdf')

import pandas as pd

# Assuming you have extracted the content using Tika and stored it in the 'content' variable
content = parsed['content']

# Split the content into rows based on newlines
rows = content.strip().split('\n')

# Split each row into columns based on a delimiter (e.g., tab, comma, etc.)
data = [row.split('\t') for row in rows]

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)
df1 = df.applymap(str)
df1.to_csv('table.csv', index=False)