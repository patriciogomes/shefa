
from binance_client import create_binance_client

client = create_binance_client()

def place_market_order(symbol="ETHUSDT", side="BUY", quantity=0.001):
    '''
    Place a market order (BUY or SELL) on Binance Futures.
    '''
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        return order
    except Exception as e:
        return {"error": str(e)}

def close_position(symbol="ETHUSDT"):
    '''
    Attempts to close an open position by placing a market order in the opposite direction.
    '''
    position_info = client.futures_position_information(symbol=symbol)[0]
    position_amt = float(position_info['positionAmt'])

    if position_amt == 0:
        return {"status": "No open position to close"}

    side = "SELL" if position_amt > 0 else "BUY"
    quantity = abs(position_amt)

    return place_market_order(symbol=symbol, side=side, quantity=quantity)
