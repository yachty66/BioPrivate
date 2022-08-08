#1. Scrape content
#2. Create pandas dataframe with clickable links and add notes + framework column
#3. Share work with Team
from PyPDF2 import PdfReader

def extractText():
    reader = PdfReader("example.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"