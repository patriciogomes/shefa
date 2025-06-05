import ccxt
import os
exchange = ccxt.binance({
    "enableRateLimit": True,
    "options": {
        "adjustForTimeDifference": True
    }
})

exchange.load_markets()
print("✅ Conexão com Binance está OK e ajustada.")


print(os.getenv("BINANCE_API_KEY"))
