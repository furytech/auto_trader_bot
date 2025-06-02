# 1. Imports
import time
import schedule
from signals import generate_signal
from trade_executor import execute_trade
from notifier import send_telegram
from sheets_logger import log_trade_to_sheets

# 2. Define the main strategy function
def run_strategy():
    print("Running strategy...")

    try:
        # 3. Generate signal from technical + sentiment logic
        result = generate_signal()

        # 4. If signal is BUY or SELL, proceed with execution
        if result["signal"] in ["BUY", "SELL"]:
            ticker = result["ticker"]
            action = result["signal"]
            reasons = result["reasons"]
            qty = result.get("qty", result.get("quantity", 1))

            # 5. Execute trade and get execution price
            price = execute_trade(ticker, action, qty, reasons)

            # 6. Send notification via Telegram
            msg = f"Trade Executed: {action} {ticker} @ ${price:.2f}\nReasons: {', '.join(reasons)}"
            send_telegram(msg)

            # 7. Log trade to Google Sheets
            log_trade_to_sheets(ticker, action, price, reasons, qty, status="DRY_RUN")
            print(f"Trade logged: {ticker} {action} x{qty} @ ${price:.2f}")

        else:
            # 8. No trade condition met
            print("No trade signal today.")

    except Exception as e:
        # 9. Handle and notify on errors
        error_msg = f"Error running strategy: {str(e)}"
        print(error_msg)
        send_telegram(error_msg)

# 10. Schedule the strategy to run before market close
run_strategy()  # Immediate test run
schedule.every().day.at("15:55").do(run_strategy)

# 11. Main runtime loop
if __name__ == "__main__":
    print("Scheduler now started.")
    while True:
        schedule.run_pending()
        time.sleep(30)

