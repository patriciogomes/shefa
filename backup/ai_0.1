import os
import re
import json
from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    USE_OPENAI = True
except:
    client = None
    USE_OPENAI = False

def clean_response(content):
    return re.sub(r"```json|```", "", content, flags=re.IGNORECASE).strip()

def map_signal_keys(signal_raw):
    try:
        signal = json.loads(signal_raw)
    except Exception as e:
        return {"error": f"Parse failed: {str(e)}", "raw": signal_raw}

    # Mapeamento dos campos esperados
    return {
        "R_t": signal.get("R_t", signal.get("Expected return (R_t)", 0)),
        "L_t": signal.get("L_t", signal.get("Predicted risk (L_t)", 0)),
        "Direction": signal.get("Direction", signal.get("Recommended direction", "No Trade")),
        "Confidence": signal.get("Confidence", signal.get("Confidence score", 0.5))
    }

def get_trade_signal(market_summary, technical_trend, sentiment_score, volatility):
    prompt = f"""
You are a trading assistant AI specialized in crypto futures.

Market Summary:
{market_summary}

Technical Trend Indicator (T_t): {technical_trend}
Sentiment Score (S_t): {sentiment_score}
Volatility (V_t): {volatility}

Based on the information above, return:
1. Expected return (R_t) between -1 and 1
2. Predicted risk (L_t) between 0 and 1
3. Recommended direction (Long / Short / No Trade)
4. Confidence score (0 to 1)

Format the response as JSON.
"""

    if USE_OPENAI:
        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            raw = response.choices[0].message.content
            cleaned = clean_response(raw)
            return map_signal_keys(cleaned)
        except Exception as e:
            return {"error": str(e)}

    # fallback mock
    return {
        "R_t": 0.02,
        "L_t": 0.004,
        "Direction": "Long",
        "Confidence": 0.91
    }
