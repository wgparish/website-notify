import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TEXTBELT_API_KEY = os.getenv("TEXTBELT_API_KEY")
SEND_SMS_TO = os.getenv("SEND_SMS_TO")