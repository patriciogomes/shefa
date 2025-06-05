from binance_api.binance_client import create_binance_client
import pandas as pd

client = create_binance_client()

def get_latest_price(symbol):
    ticker = client.fetch_ticker(symbol)
    return ticker['last']

def get_klines(symbol, interval, limit=50):
    ohlcv = client.fetch_ohlcv(symbol, timeframe=interval, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

def calculate_volatility(df):
    returns = df["close"].pct_change().dropna()
    return returns.std()