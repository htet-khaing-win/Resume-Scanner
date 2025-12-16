import os
from src.pdf_parser import parse_resume_pdf
from src.text_processor import preprocess_resume, preprocess_job_description

resume_text = parse_resume_pdf("data/raw/Resume.pdf")
jd_text = parse_resume_pdf("data/raw/JD.txt")

resume_data = preprocess_resume(resume_text)
jd_data = preprocess_job_description(jd_text)
print(f" \n From Resume: \n {resume_data}")
print(f" \n From Job Description: \n {jd_data}")

import spacy
from spacy.lang.en.examples import sentences 

nlp = spacy.load("en_core_web_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)
