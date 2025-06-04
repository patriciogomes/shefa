
import os
import time
import json

from binance.market_data import get_latest_price, get_klines, calculate_volatility
from openai.decision import get_trade_signal
from engine.alpha import calculate_allocation
from telegram_bot.bot import send_message

SYMBOL = "ETHUSDT"
INTERVAL = "1m"
LOOP_INTERVAL = 60  # seconds between executions

def run_shefa():
    send_message("🤖 Shefa Alpha Engine started.")

    while True:
        try:
            # Step 1: Fetch Market Data
            price = get_latest_price(SYMBOL)
            candles = get_klines(SYMBOL, interval=INTERVAL, limit=50)
            volatility = calculate_volatility(candles)
            technical_trend = (candles["close"].iloc[-1] - candles["close"].iloc[0]) / candles["close"].iloc[0]
            sentiment_score = 0  # placeholder — could be calculated externally or via OpenAI later
            market_summary = f"Current price: {price}, Volatility: {volatility:.4f}, Trend: {technical_trend:.4f}"

            # Step 2: Get AI Decision
            ai_response = get_trade_signal(
                market_summary=market_summary,
                technical_trend=technical_trend,
                sentiment_score=sentiment_score,
                volatility=volatility
            )

            try:
                signal = json.loads(ai_response)
            except:
                send_message(f"⚠️ Failed to parse AI response: {ai_response}")
                time.sleep(LOOP_INTERVAL)
                continue

            R_t = float(signal.get("R_t", 0))
            L_t = float(signal.get("L_t", 0))
            direction = signal.get("Direction", "No Trade")
            confidence = float(signal.get("Confidence", 0.5))

            # Step 3: Compute Allocation
            A_t = calculate_allocation(R_t, sentiment_score, technical_trend, volatility, L_t)

            # Step 4: Report
            msg = (
                f"📊 Market: {SYMBOL}"
                f"🧠 AI Direction: {direction}"
                f"📈 Expected Return (R_t): {R_t}"
                f"⚠️ Risk (L_t): {L_t}"
                f"🎯 Allocation (A_t): {A_t:.4f}"
                f"✅ Confidence: {confidence}"
            )
            send_message(msg)

        except Exception as e:
            send_message(f"🔥 Exception: {str(e)}")

        time.sleep(LOOP_INTERVAL)

if __name__ == "__main__":
    run_shefa()
