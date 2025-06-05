import ccxt
from dotenv import load_dotenv
import os

load_dotenv()

client = ccxt.binance({
    'apiKey': os.getenv("BINANCE_API_KEY"),
    'secret': os.getenv("BINANCE_SECRET_KEY"),
    'enableRateLimit': True
})

balance = client.fetch_balance()
print(balance)
