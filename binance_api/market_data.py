from binance_api.binance_client import create_binance_client
import pandas as pd

client = create_binance_client()

def get_latest_price(symbol="ETH/USDT"):
    ticker = client.fetch_ticker(symbol)
    return ticker['last']

def get_klines(symbol="ETH/USDT", timeframe="1m", limit=100):
    ohlcv = client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

def calculate_volatility(df):
    df["returns"] = df["close"].pct_change()
    return df["returns"].std()