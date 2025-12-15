import re
from cleantext import clean
from datetime import datetime

contractions_dict = {
    "i'm": "i am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "we're": "we are",
    "they're": "they are",
    "i've": "i have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",
    "i'll": "i will",
    "you'll": "you will",
    "he'll": "he will",
    "she'll": "she will",
    "it'll": "it will",
    "we'll": "we will",
    "they'll": "they will",
    "i'd": "i would",
    "you'd": "you would",
    "he'd": "he would",
    "she'd": "she would",
    "we'd": "we would",
    "they'd": "they would",
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "can't": "cannot",
    "couldn't": "could not",
    "won't": "will not",
    "wouldn't": "would not",
    "shouldn't": "should not",
    "mustn't": "must not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "hasn't": "has not",
    "haven't": "have not",
    "hadn't": "had not",
    "mightn't": "might not",
    "needn't": "need not"
}

COMMON_ABBRS = {

    # Employment Type
    "ft": "full time",
    "f/t": "full time",
    "pt": "part time",
    "p/t": "part time",
    "perm": "permanent",
    "temp": "temporary",
    "contract": "contract",
    "freelance": "freelance",
    "remote": "remote",
    "onsite": "on site",
    "on-site": "on site",
    "hybrid": "hybrid",
    "wfh": "work from home",

    # Experience / Seniority
    "yoe": "years of experience",
    "yrs": "years",
    "yr": "year",
    "exp": "experience",
    "jr": "junior",
    "sr": "senior",
    "mid": "mid level",
    "lead": "team lead",
    "mgr": "manager",
    "dir": "director",
    "vp": "vice president",
    "svp": "senior vice president",
    "cxo": "executive leadership",


    # Education
    "bs": "bachelor of science",
    "bsc": "bachelor of science",
    "ba": "bachelor of arts",
    "be": "bachelor of engineering",
    "ms": "master of science",
    "msc": "master of science",
    "ma": "master of arts",
    "meng": "master of engineering",
    "phd": "doctor of philosophy",
    "mba": "master of business administration",
    "gpa": "grade point average",


    # Core Software / Engineering
    "oop": "object oriented programming",
    "ds": "data structures",
    "dsa": "data structures and algorithms",
    "algo": "algorithms",
    "api": "application programming interface",
    "rest": "representational state transfer",
    "sdk": "software development kit",
    "ci": "continuous integration",
    "cd": "continuous delivery",
    "ci/cd": "continuous integration continuous delivery",
    "ide": "integrated development environment",
    "os": "operating system",
    "db": "database",
    "rdbms": "relational database management system",
    "nosql": "non relational database",
    "etl": "extract transform load",
    "elt": "extract load transform",

    # Data / ML / AI
    "ml": "machine learning",
    "dl": "deep learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "llm": "large language model",
    "rag": "retrieval augmented generation",
    "xgboost": "gradient boosting",
    "rf": "random forest",
    "svm": "support vector machine",
    "pca": "principal component analysis",
    "eda": "exploratory data analysis",
    "mle": "machine learning engineer",

    # Cloud / DevOps
    "aws": "amazon web services",
    "gcp": "google cloud platform",
    "azure": "microsoft azure",
    "ec2": "elastic compute cloud",
    "s3": "simple storage service",
    "iam": "identity and access management",
    "docker": "containerization",
    "k8s": "kubernetes",

    # Business / Product / Process
    "kpi": "key performance indicator",
    "okr": "objectives and key results",
    "sla": "service level agreement",
    "roi": "return on investment",
    "poc": "proof of concept",
    "prd": "product requirements document",
    "brd": "business requirements document",
    "qa": "quality assurance",
    "uat": "user acceptance testing",

    # HR / Hiring / Compensation
    "jd": "job description",
    "cv": "curriculum vitae",
    "tc": "total compensation",
    "ctc": "cost to company",
    "np": "notice period",
    "bgc": "background check",
    "ref": "reference",
    "hc": "headcount"
}


def clean_text(text: str) -> str:
    """
    Performs basic text cleaning
    """
    # Basic cleaning with cleantext
    cleaned_text = clean(
        text,
        fix_unicode=True, 
        to_ascii=True,     
        lower=True,        
        no_line_breaks=False, 
        no_urls=False,     
        no_emails=False,   
        no_numbers=False,  
        no_punct=False,    
    )

    # Remove URLs
    cleaned_text = re.sub(r'https?://\S+', ' ', cleaned_text)
    
    # Remove email addresses
    cleaned_text = re.sub(r'\S+@\S+', ' ', cleaned_text)

    # Remove special characters
    # This is slightly more aggressive than cleantext's no_punct=False
    cleaned_text = re.sub(r'[^a-z0-9.,\-\s]+', ' ', cleaned_text) # changed to ' ' to separate merged words

    # Remove extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # Strip spaces
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def normalize_text(text: str, abbreviation_map: Dict[str, str]) -> str:
    """
    Normalizes text by expanding contractions and common abbreviations.
    """
    # Expand contractions
    for contraction, expansion in contractions_dict.items():
        
        text = re.sub(
            r'\b' + re.escape(contraction) + r'\b', 
            expansion, 
            text, 
            flags=re.IGNORECASE
        )

    # Expand abbreviations
    for abbr, full_form in abbreviation_map.items():
        pattern = r'\b' + re.escape(abbr) + r'\b'
        text = re.sub(pattern, full_form, text, flags=re.IGNORECASE)
    
    # Standardize date formats

    """
    This example finds dates like 01/15/2023 or 1-15-2023 and standardizes to 2023-01-15
    """
 
    def standardize_date(match):
        date_str = match.group(0)
        try:
            dt_obj = datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            try:
                dt_obj = datetime.strptime(date_str, "%m-%d-%Y")
            except ValueError:
                return date_str  

        return dt_obj.strftime("%Y-%m-%d")

    date_pattern = r'\b\d{1,2}[/\-]\d{1,2}[/\-]\d{4}\b'
    text = re.sub(date_pattern, standardize_date, text)

    return text