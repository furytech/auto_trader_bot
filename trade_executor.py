# trade_executor.py
# Handles actual trade execution or simulates it based on TRADE_MODE.
# Also logs the trade and sends Telegram notifications.

import os
from alpaca_trade_api.rest import REST
from config import ALPACA_KEY_ID, ALPACA_SECRET, ALPACA_API_URL, TRADE_MODE
from sheets_logger import log_trade_to_sheets
from notifier import send_telegram

# Function to execute a trade
def execute_trade(ticker, action, qty, reasons, price=None):
    # Log the mode and action
    print(f"🚦 Mode: {TRADE_MODE.upper()} | Action: {action} {qty} {ticker}")

    # DRY RUN mode — simulate trade, do not connect to Alpaca
    if TRADE_MODE == "dry_run":
        print(f"[DRY RUN] Would {action} {qty} shares of {ticker}")
        return 123.45  # Simulated price

    # PAPER or LIVE mode — send real trade to Alpaca
    else:
        try:
            # Connect to Alpaca with dynamic URL based on mode
            api = REST(ALPACA_KEY_ID, ALPACA_SECRET, base_url=ALPACA_API_URL)

            # Submit market order
            order = api.submit_order(
                symbol=ticker,
                qty=qty,
                side=action.lower(),  # "buy" or "sell"
                type="market",
                time_in_force="gtc"
            )

            print(f"✅ Order submitted: {order.id}")
            send_telegram(f"✅ Executed {action} {qty} {ticker} (order ID: {order.id})")

            # Optionally fetch the last trade price for logging
            last_trade = api.get_last_trade(ticker)
            price = float(last_trade.price)

        except Exception as e:
            error_msg = f"❌ Alpaca order failed: {str(e)}"
            print(error_msg)
            send_telegram(error_msg)
            return

    # Ensure price is set even in dry run mode
    price = price or 0.00
    #added last - check to see if we keep
    if __name__ == "__main__":
        execute_trade(
            ticker="UVXY",
            action="BUY",
            qty=10,
            reasons=["test signal"],
            price=12.34  # Optional for dry run
        )

    # Log the trade to Google Sheets
    log_trade_to_sheets(ticker, action, price, reasons, qty)
