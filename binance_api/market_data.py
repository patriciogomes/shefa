
from binance_api.binance_client import create_binance_client
import pandas as pd

client = create_binance_client()

def get_latest_price(symbol="BTCUSDT"):
    ticker = client.futures_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

def get_klines(symbol="BTCUSDT", interval="1m", limit=100):
    """
    Fetch recent kline/candle data for a symbol.
    Returns a DataFrame with OHLCV and timestamp.
    """
    klines = client.futures_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
    return df[["timestamp", "open", "high", "low", "close", "volume"]]

def calculate_volatility(df):
    """
    Calculate simple volatility as standard deviation of close returns.
    """
    df["returns"] = df["close"].pct_change()
    return df["returns"].std()
