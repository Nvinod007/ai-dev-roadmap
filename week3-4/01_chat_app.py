"""
Week 3-4 - Day 1: AI Chat App (Multi-turn)
Run: python week3-4/01_chat_app.py

Build a chat that remembers the conversation. API is stateless — we send full history each time.
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

# Start with system message — sets the AI's personality for whole chat
messages = [
    {"role": "system", "content": "You are a helpful assistant. Be concise."},
]

print("Chat App — type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit", "q"):
        break
    if not user_input:
        print("Please enter a message.")
        continue

    # Append user message to history
    messages.append({"role": "user", "content": user_input})

    # Call API with FULL history (that's how the AI "remembers")
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=150,
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {e}"

    # Append assistant reply to history (IMPORTANT: don't forget this!)
    messages.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}\n")

print("Bye!")
