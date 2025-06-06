import time
import json
import threading
from dotenv import load_dotenv
load_dotenv()
from binance_api.market_data import get_latest_price, get_klines, calculate_volatility
from ai.decision import get_trade_signal
from engine.alpha import calculate_allocation
from telegram_bot.bot import send_message, setup_bot_commands, ACTIVE_USERS

SYMBOL = "ETH/USDT"
INTERVAL = "1m"
LOOP_INTERVAL = 60  # seconds between executions

def run_shefa():
    send_message("🤖 Shefa Alpha Engine started.")
    print("🟢 Shefa Engine loop running...")

    while not ACTIVE_USERS:
        print("⏳ Aguardando /start no Telegram para iniciar...")
        time.sleep(2)

    while True:
        try:
            print("📈 Fetching market data...")
            price = get_latest_price(SYMBOL)
            candles = get_klines(SYMBOL, interval=INTERVAL, limit=50)
            volatility = calculate_volatility(candles)
            technical_trend = (candles["close"].iloc[-1] - candles["close"].iloc[0]) / candles["close"].iloc[0]
            sentiment_score = 0  # placeholder
            market_summary = f"Current price: {price}, Volatility: {volatility:.4f}, Trend: {technical_trend:.4f}"

            print("🧠 Calling AI decision engine...")
            ai_response = get_trade_signal(
                market_summary=market_summary,
                technical_trend=technical_trend,
                sentiment_score=sentiment_score,
                volatility=volatility
            )

            print(f"🧠 Raw AI response: {ai_response}")

            try:
                if isinstance(ai_response, str):
                    signal = json.loads(ai_response)
                else:
                    signal = ai_response
                print(f"✅ Parsed Signal: {signal}")
            except Exception as e:
                error_msg = f"⚠️ Failed to parse AI response: {str(e)} | Raw: {ai_response}"
                print(error_msg)
                send_message(error_msg)
                time.sleep(LOOP_INTERVAL)
                continue

            R_t = float(signal.get("R_t", 0))
            L_t = float(signal.get("L_t", 0))
            direction = signal.get("Direction", "No Trade")
            confidence = float(signal.get("Confidence", 0.5))

            A_t = calculate_allocation(R_t, sentiment_score, technical_trend, volatility, L_t)

            msg = (
                f"📊 Market: {SYMBOL}\n"
                f"🧠 AI Direction: {direction}\n"
                f"📈 Expected Return (R_t): {R_t}\n"
                f"⚠️ Risk (L_t): {L_t}\n"
                f"🎯 Allocation (A_t): {A_t:.4f}\n"
                f"✅ Confidence: {confidence}"
            )

            print("📤 Sending report...")
            send_message(msg)

        except Exception as e:
            error_msg = f"🔥 Exception: {str(e)}"
            print(error_msg)
            send_message(error_msg)

        time.sleep(LOOP_INTERVAL)

if __name__ == "__main__":
    threading.Thread(target=setup_bot_commands, daemon=True).start()
    send_message("🤖 Shefa Bot iniciado com sucesso.")
    run_shefa()