import os
from binance.client import Client  # <-- Correto

def create_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API key and secret must be set in environment variables.")

    client = Client(api_key, api_secret)
    client.API_URL = "https://fapi.binance.com"  # For Binance Futures
    return client
