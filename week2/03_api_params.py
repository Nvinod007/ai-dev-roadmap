"""
Week 2 - Day 3: API Parameters (temperature, max_tokens, etc.)
Run: python3 week2/03_api_params.py

Control randomness and output length.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_API_BASE", "https://api.groq.com/openai/v1"),
)
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# === 1. temperature: 0 = deterministic, 1 = creative ===
response_low = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is 2+2? Reply with one word."}],
    temperature=0,
)
print("Low temp (0):", response_low.choices[0].message.content.strip())

# === 2. max_tokens: cap the response length ===
response_capped = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain React in 2 sentences."}],
    max_tokens=50,
)
print("\nMax 50 tokens:", response_capped.choices[0].message.content.strip())

# === 3. JSON output (response_format) ===
response_json = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Return a JSON object with keys 'capital' and 'country' for France."}],
    response_format={"type": "json_object"},
)
print("\nJSON format:", response_json.choices[0].message.content)

# === 4. Usage (token counts) ===
if response_json.usage:
    print("\nTokens used:", response_json.usage)

# === 5. Your exercise ===
# Call with temperature=0.9 and ask "Give me a startup idea"
# Run twice - you'll get different ideas. Then try temperature=0 - more similar.

response_5 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Give me a startup idea"}],
    temperature=0.9,
)
print("\nStartup idea (temperature=0.9):", response_5.choices[0].message.content[:300])

response_6 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Give me a startup idea"}],
    temperature=0,
)
print("\nStartup idea (temperature=0):", response_6.choices[0].message.content[:300])