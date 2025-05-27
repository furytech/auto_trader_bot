#return {
 # "signal": "BUY",
  #"reasons": ["Price > SMA50", "RSI < 30", "Volume > average"]
#}

def generate_signal():
  return {
    "ticker": "UVXY",
    "signal": "BUY",  # 👈 This is the new line you need
    "price": 23.45,  # changed for easy identification
    "qty": 10,
    "reasons": ["entry signal"]
  }



