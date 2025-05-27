import alpaca_trade_api as tradeapi
from config import ALPACA_KEY_ID, ALPACA_SECRET, ALPACA_API_URL, TRADE_MODE
from sheets_logger import log_trade_to_sheets
from notifier import notify_trade


def execute_trade(ticker, action, qty, reason_list, price):
    print(f"[MODE: {TRADE_MODE}] Executing {action} on {qty} shares of {ticker} @ {price}...")

    if TRADE_MODE == "dry_run":
        print("Dry run mode: trade not sent to Alpaca.")
    else:
        api = tradeapi.REST(
            key_id=ALPACA_KEY_ID,
            secret_key=ALPACA_SECRET,
            base_url=ALPACA_API_URL
        )

        side = action.lower()
        try:
            order = api.submit_order(
                symbol=ticker,
                qty=qty,
                side=side,
                type='market',
                time_in_force='gtc'
            )
            print(f"Order submitted: {order.id}")
        except Exception as e:
            print(f"Trade execution failed: {e}")
            return

    # Log trade to Google Sheets
    log_trade_to_sheets(
        ticker=ticker,
        action=action,
        price=price,
        reasons=reason_list,
        qty=qty,
        status="Executed"
    )

    # Notify via Telegram or other notifier
    notify_trade(
        f"{action} order for {qty}x {ticker} @ {price:.2f} | Reasons: {', '.join(reason_list)}"
    )
