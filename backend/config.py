import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))
# Ensure this matches the name in your .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "", 
    "database": "ai_cooking"
}