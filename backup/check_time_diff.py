from ai import OpenAI

client = OpenAI(api_key="sua_api_key")
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello, what is the market sentiment?"}]
)
print(resp.choices[0].message.content)
