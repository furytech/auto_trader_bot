# notifier.py

# 1. Imports
import requests
import os
from dotenv import load_dotenv

# 2. Load environment variables from .env file
load_dotenv()

# 3. Get token and chat ID from environment (corrected variable names)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# 4. Send a message to the Telegram chat
def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise Exception("Telegram token or chat ID not set.")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})

    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
