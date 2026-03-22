"""
Week 3-4 - Day 4: Streaming Chat (Combine chat + streaming)
Run: python week3-4/04_streaming_chat.py

Chat that streams the reply word-by-word. Must collect full reply for history!
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

messages = [
    {"role": "system", "content": "You are a helpful assistant. Be concise."},
]

print("Streaming Chat — type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit", "q"):
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})
    print("AI: ", end="", flush=True)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=200,
            stream=True,
        )

        full_reply = ""
        for chunk in response:
            part = chunk.choices[0].delta.content
            if part:
                print(part, end="", flush=True)
                full_reply += part

        print("\n")
        messages.append({"role": "assistant", "content": full_reply})

    except Exception as e:
        print(f"\nError: {e}\n")
        messages.pop()  # Remove the user msg we added, so we can retry

print("Bye!")
