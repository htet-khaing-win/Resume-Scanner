import PyPDF2

def extract_text_from_pdf(filepath: str) -> str:
    file_path = filepath

    try: 
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            raw_text = ""
            for page in reader.pages:
                text = page.extract_text()
                raw_text += text + "\n"
                
        return raw_text
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' is not found")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    
def parse_resume_pdf(pdf_path: str) -> str:
    raw_text = extract_text_from_pdf(pdf_path)
    return raw_text
