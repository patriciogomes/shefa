
from client import create_binance_client

client = create_binance_client()

def get_account_balance(asset="USDT"):
    '''
    Get available balance for a given asset in Futures account.
    '''
    balances = client.futures_account_balance()
    for b in balances:
        if b["asset"] == asset:
            return {
                "asset": asset,
                "balance": float(b["balance"]),
                "available": float(b["availableBalance"])
            }
    return {"error": "Asset not found"}

def get_open_positions():
    '''
    Get all open positions with non-zero size.
    '''
    positions = client.futures_position_information()
    open_positions = [
        {
            "symbol": p["symbol"],
            "positionAmt": float(p["positionAmt"]),
            "entryPrice": float(p["entryPrice"]),
            "unrealizedProfit": float(p["unrealizedProfit"]),
            "leverage": int(p["leverage"]),
            "side": "LONG" if float(p["positionAmt"]) > 0 else "SHORT"
        }
        for p in positions if float(p["positionAmt"]) != 0
    ]
    return open_positions
