import os
import ccxt
from dotenv import load_dotenv

load_dotenv()

def create_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not api_secret:
        raise ValueError("API key and secret must be set in environment variables.")

    binance = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True
    })

    # Ajuste manual de timestamp com o servidor Binance
    server_time = binance.fetch_time()
    local_time = binance.milliseconds()
    time_diff = server_time - local_time
    binance.time_difference = time_diff

    print(f"⚙️ Binance client criado com ajuste manual de tempo: {time_diff} ms")

    return binance