import re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("./PDFs/Adam_Smith_Private_Loan_Borrower_Form.pdf")
print(text)