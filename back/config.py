import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")