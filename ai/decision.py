import os
from dotenv import load_dotenv
load_dotenv()

try:
    from ai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    USE_OPENAI = True
except:
    client = None
    USE_OPENAI = False

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
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return {"error": str(e)}

    # fallback mock
    return {
        "R_t": 0.018,
        "L_t": 0.004,
        "Direction": "Long",
        "Confidence": 0.91
    }