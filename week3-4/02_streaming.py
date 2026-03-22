"""
Week 3-4 - Day 2: Streaming Responses
Run: python week3-4/02_streaming.py

Stream = get tokens one by one as the AI "types". Better UX.
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

print("Streaming demo — watch the text appear word by word.\n")
print("AI: ", end="", flush=True)

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "Explain what Python is in 2 sentences."}],
        max_tokens=100,
        stream=True,  # This enables streaming!
    )

    # response is an iterator when stream=True — not printable directly
    # Uncomment to see: print("Response type:", type(response).__name__)
    full_reply = ""
    for chunk in response:
        part = chunk.choices[0].delta.content
        if part:
            print(part, end="", flush=True)
            full_reply += part
    print("\n")

    # We also have the full reply if needed
    print(f"(Full length: {len(full_reply)} chars)")

except Exception as e:
    print(f"\nError: {e}")
