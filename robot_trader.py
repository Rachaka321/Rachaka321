# robot_trader.py
import time
import random
from datetime import datetime

# === CONFIG ===
TRADING_SYMBOL = "BTC-USD"   # Example, can be any symbol
INITIAL_BALANCE = 1000       # USD
POSITION = 0                 # Number of coins held

# Simple trade log
trade_log = []

def log_trade(action, price, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    trade = {"time": timestamp, "action": action, "price": price, "amount": amount}
    trade_log.append(trade)
    print(trade)

def get_market_price():
    # Simulated market price
    return round(random.uniform(30000, 35000), 2)

def decide_trade(price):
    # Random simple logic: buy if price < 31k, sell if price > 34k
    if price < 31000:
        return "BUY"
    elif price > 34000:
        return "SELL"
    else:
        return "HOLD"

def main():
    global POSITION, INITIAL_BALANCE
    print("Paper Trading Bot Started...")

    # Simulate a single trade run (can be looped for more frequent checks)
    price = get_market_price()
    action = decide_trade(price)
    amount = 0

    if action == "BUY":
        amount = INITIAL_BALANCE / price
        POSITION += amount
        INITIAL_BALANCE -= amount * price
        log_trade("BUY", price, round(amount, 4))

    elif action == "SELL" and POSITION > 0:
        amount = POSITION
        INITIAL_BALANCE += amount * price
        POSITION = 0
        log_trade("SELL", price, round(amount, 4))
    
    else:
        print(f"{datetime.now()} - No action. Price: {price}, Position: {POSITION}")

    print(f"Balance: ${round(INITIAL_BALANCE, 2)}, Position: {round(POSITION, 4)} coins")
    print("Run complete.\n")

if __name__ == "__main__":
    main()