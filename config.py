import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
project = os.getenv('PROJECT_NAME')
log = os.getenv('LOG_LEVEL')
