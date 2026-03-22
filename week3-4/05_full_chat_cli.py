"""
Week 3-4 - Day 5: Full Chat CLI (Capstone)
Run: python week3-4/05_full_chat_cli.py

Or with a question: python week3-4/05_full_chat_cli.py "Explain recursion"

Combines: multi-turn chat + streaming + context trimming.
"""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_API_BASE", "https://api.groq.com/openai/v1"),
)
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

MAX_HISTORY_TOKENS = 4000
RESERVE_FOR_REPLY = 500


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def count_messages_tokens(messages: list) -> int:
    return sum(estimate_tokens(m.get("content", "")) for m in messages)


def trim_to_fit(messages: list, max_tokens: int) -> list:
    current_tokens = count_messages_tokens(messages)
    if current_tokens <= max_tokens:
        return messages

    print(f"\n[TRIM] Over limit: {current_tokens} tokens (max {max_tokens}). Trimming oldest messages...")
    before_count = len(messages)
    result = [messages[0]] if messages and messages[0]["role"] == "system" else []
    rest = messages[1:] if result else messages
    while rest and count_messages_tokens(result + rest) > max_tokens:
        if len(rest) >= 2 and rest[0]["role"] == "user" and rest[1]["role"] == "assistant":
            rest = rest[2:]
        else:
            rest = rest[1:]
    after = result + rest
    removed = before_count - len(after)
    print(f"[TRIM] Removed {removed} message(s). Kept {len(after)} messages, {count_messages_tokens(after)} tokens.\n")
    return after


def ask(prompt: str, messages: list) -> str:
    """Single question mode (no streaming, for argv)."""
    msgs = messages + [{"role": "user", "content": prompt}]
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=trim_to_fit(msgs, MAX_HISTORY_TOKENS - RESERVE_FOR_REPLY),
            max_tokens=300,
        )
        return r.choices[0].message.content or "[No response]"
    except Exception as e:
        return f"Error: {e}"


def chat_loop():
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
    ]
    print("Full Chat CLI (streaming + context trim) — 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        messages = trim_to_fit(messages, MAX_HISTORY_TOKENS - RESERVE_FOR_REPLY)
        print("AI: ", end="", flush=True)

        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_tokens=300,
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
            messages.pop()

    print("Bye!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        msgs = [{"role": "system", "content": "You are a helpful assistant."}]
        print(ask(q, msgs))
    else:
        chat_loop()
