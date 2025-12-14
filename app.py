import os
from src.pdf_parser import parse_resume_pdf

resume_text = parse_resume_pdf("data/raw/Resume.pdf")

if resume_text:
    print(f"The extracted text is: {resume_text}")
    print(f"The length of text is: {len(resume_text)}")
else:
    print("Extraction Failed.") 


