from dotenv import load_dotenv
import os

load_dotenv()

print("BINANCE_API_KEY =", os.getenv("BINANCE_API_KEY"))
print("BINANCE_SECRET_KEY =", os.getenv("BINANCE_SECRET_KEY"))
