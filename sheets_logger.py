# 1. Imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# 2. Function to log trade to Google Sheets
def log_trade_to_sheets(ticker, action, price, reasons, qty, status="Executed"):
    # 3. Auth scopes for Sheets and Drive
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # 4. Authenticate with Google
    creds = ServiceAccountCredentials.from_json_keyfile_name("google-credentials.json", scope)
    client = gspread.authorize(creds)

    # 5. Open your spreadsheet and sheet
    sheet = client.open("TradeLogs").sheet1

    # 6. Get timestamp and append the new row
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, ticker, action, qty, price, ", ".join(reasons), status])


# 7. Example usage
if __name__ == "__main__":
    log_trade_to_sheets(
        ticker="UVXY",
        action="BUY",
        price=12.34,
        reasons=["test", "entry signal"],
        qty=10,
        status="Executed"
    )
