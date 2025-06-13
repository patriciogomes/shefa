
import time
import json
import threading
import math

from binance_api.market_data import get_latest_price, get_klines, calculate_volatility
from ai.decision import get_trade_signal
from engine.filters import is_valid_signal
from telegram_bot.bot import send_message, setup_bot_commands, ACTIVE_USERS

SYMBOL = "RESOLVUSDT"
INTERVAL = "1m"
LOOP_INTERVAL = 20

capital = 48.00
total_pnl = 0
trade_history = []

def explain_direction(direction):
    if direction.lower() == "long":
        return "📈 Long (comprar esperando alta)"
    elif direction.lower() == "short":
        return "📉 Short (vender esperando queda)"
    else:
        return "🧘 No Trade (sem ação recomendada)"

def run_shefa():
    global total_pnl

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
            sentiment_score = 0
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

            if confidence < 0.85 or abs(R_t) < 0.01:
                msg = f"⛔ Sinal ignorado (baixa confiança {confidence:.2f} ou retorno {R_t:.4f})"
                print(msg)
                send_message(msg)
                time.sleep(LOOP_INTERVAL)
                continue

            if not is_valid_signal(R_t, L_t, sentiment_score, technical_trend, confidence, volatility):
                msg = "⛔ Sinal bloqueado pelo filtro antifake-sinal (sinal fraco, incoerente ou arriscado)"
                print(msg)
                send_message(msg)
                time.sleep(LOOP_INTERVAL)
                continue

            # Alocação
            A_t = R_t / (volatility + L_t + 1e-6)
            A_t = max(min(A_t, 1.0), -1.0)
            expected_gain = capital * A_t * R_t
            total_pnl += expected_gain
            trade_history.append(expected_gain)

            msg = (
                f"📊 Market: {SYMBOL}"
                f"🧠 AI Direction: {explain_direction(direction)}"
                f"📈 Expected Return (R_t): {R_t * 100:.2f}%"
                f"⚠️ Risk (L_t): {L_t * 100:.2f}%"
                f"🎯 Allocation (A_t): {A_t * 100:.2f}%"
                f"💸 Gain Estimado: ${expected_gain:.2f}"
                f"📊 PnL Total: ${total_pnl:.2f}"
                f"✅ Confidence: {confidence:.2f}"
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
