import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Access the values
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Bot Token:", TELEGRAM_BOT_TOKEN)
print("Chat ID:", TELEGRAM_CHAT_ID)

# Construct the message
message = "Test message from auto_trader system."

# Send message
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message
}

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print("[SUCCESS] Message sent to Telegram.")
except requests.exceptions.RequestException as e:
    print("[ERROR] Telegram send failed:", e)
