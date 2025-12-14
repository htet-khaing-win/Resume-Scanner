import PyPDF2
from cleantext import clean

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

def clean_extracted_text(raw_text: str) -> str:
    cleaned_text = clean(raw_text,
    fix_unicode=True,               # fix various unicode errors
    to_ascii=True,                  # transliterate to closest ASCII representation
    lower=True,                     # lowercase text
    no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
    no_urls=False,                  # replace all URLs with a special token
    no_emails=False,                # replace all email addresses with a special token
    no_phone_numbers=False,         # replace all phone numbers with a special token
    no_numbers=False,               # replace all numbers with a special token
    no_digits=False,                # replace all digits with a special token
    no_currency_symbols=False,      # replace all currency symbols with a special token
    no_punct=False,                 # remove punctuations
    replace_with_punct="",          # instead of removing punctuations you may replace them
    replace_with_url="<URL>",
    replace_with_email="<EMAIL>",
    replace_with_phone_number="<PHONE>",
    replace_with_number="<NUMBER>",
    replace_with_digit="0",
    replace_with_currency_symbol="<CUR>",
    lang="en"                       # set to 'de' for German special handling
)
    return cleaned_text
    
def parse_resume_pdf(pdf_path: str) -> str:
    raw_text = extract_text_from_pdf(pdf_path)
    if raw_text:
         clean_text = clean_extracted_text(raw_text)
         return clean_text
    return None