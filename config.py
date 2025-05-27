import os
from dotenv import load_dotenv

load_dotenv()

# Trading mode: "dry_run", "paper", or "live"
TRADE_MODE = os.getenv("TRADE_MODE", "paper")

# Alpaca credentials
ALPACA_KEY_ID = os.getenv("ALPACA_KEY_ID")
ALPACA_SECRET = os.getenv("ALPACA_SECRET")

# Automatically determine the API URL based on the trade mode
if TRADE_MODE == "paper":
    ALPACA_API_URL = "https://paper-api.alpaca.markets"
elif TRADE_MODE == "live":
    ALPACA_API_URL = "https://api.alpaca.markets"
else:
    ALPACA_API_URL = None  # or a local mock server if needed
