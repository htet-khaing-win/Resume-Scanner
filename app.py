import os
from src.pdf_parser import parse_resume_pdf
from src.text_processor import preprocess_resume, preprocess_job_description

# Process Resume
resume_path = "data/raw/Resume.pdf"
resume_text = parse_resume_pdf(resume_path)
resume_data = preprocess_resume(resume_text)

# Process Job Description
jd_path = "data/raw/JD.txt"
if os.path.exists(jd_path):
    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text = f.read() 
else:
    jd_text = ""
    print("Error: JD.txt not found")
    
jd_data = preprocess_job_description(jd_text)

print(f" \n From Resume: \n {resume_data}")
print(f" \n From Job Description: \n {jd_data}")