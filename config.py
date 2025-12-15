import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

api_key = os.getenv('API_KEY')
project = os.getenv('PROJECT_NAME')
log = os.getenv('LOG_LEVEL')
