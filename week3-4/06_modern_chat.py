"""
Week 3-4 - Day 6: Modern Chat (Summarize + Retry + Fallback)
Run: python week3-4/06_modern_chat.py

Instead of trimming: SUMMARIZE old messages. Retry on error. Fallback to single-turn if all fails.
"""

import os
import sys
import time
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
KEEP_LAST_TURNS = 1  # How many recent user messages to keep before summarizing
MAX_RETRIES = 3
RETRY_BASE_WAIT = 2  # seconds


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def count_messages_tokens(messages: list) -> int:
    return sum(estimate_tokens(m.get("content", "")) for m in messages)


def summarise_and_fit(messages: list, max_tokens: int) -> list:
    """
    When over limit: summarize old messages instead of trimming.
    Keeps system + summary of old conv + recent turns.
    """
    current_tokens = count_messages_tokens(messages)
    if current_tokens <= max_tokens:
        return messages

    system = [messages[0]] if messages and messages[0]["role"] == "system" else []
    rest = messages[1:] if system else messages

    # Keep last KEEP_LAST_TURNS user messages (and their assistant replies)
    # For simplicity: keep last 2 messages (user + assistant) or last 1 (user only)
    keep_count = KEEP_LAST_TURNS * 2  # user + assistant per "turn"
    to_keep = rest[-keep_count:] if len(rest) > keep_count else rest
    to_summarise = rest[:-keep_count] if len(rest) > keep_count else []

    if not to_summarise:
        return messages

    print(f"\n[SUMMARISE] Over limit: {current_tokens} tokens. Summarizing {len(to_summarise)} old messages...")

    conv_text = "\n".join(
        f"{m['role']}: {m['content']}" for m in to_summarise
    )
    summarise_prompt = f"""Summarize this conversation in 2-4 sentences. Preserve key facts, decisions, and context.
Keep it concise. Output only the summary, no preamble.

Conversation:
{conv_text}"""

    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": summarise_prompt}],
            max_tokens=150,
            temperature=0.3,
        )
        summary = (r.choices[0].message.content or "").strip()
    except Exception as e:
        print(f"[SUMMARISE] Failed to summarize: {e}. Falling back to trim.")
        summary = "(Previous conversation could not be summarized.)"

    summary_msg = {"role": "user", "content": f"[Previous conversation summary]\n{summary}\n\n[Conversation continues below.]"}
    result = system + [summary_msg] + to_keep
    print(f"[SUMMARISE] Done. Now {len(result)} messages, ~{count_messages_tokens(result)} tokens.\n")
    return result


def chat_with_retry(messages: list, stream: bool = True) -> str:
    """
    Call API with retries. On final failure, fallback to single-turn (user question only).
    """
    last_user = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")

    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_tokens=300,
                stream=stream,
            )
            if stream:
                full = ""
                for chunk in response:
                    part = chunk.choices[0].delta.content
                    if part:
                        full += part
                        print(part, end="", flush=True)
                return full
            return response.choices[0].message.content or "[No response]"
        except Exception as e:
            err_str = str(e).lower()
            is_retryable = "429" in err_str or "rate" in err_str or "timeout" in err_str or "connection" in err_str
            wait = RETRY_BASE_WAIT * (2 ** attempt)
            print(f"\n[RETRY] Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES - 1 and is_retryable:
                print(f"[RETRY] Waiting {wait}s before retry...")
                time.sleep(wait)
            else:
                break

    # Fallback: try with just the user's question
    print(f"\n[FALLBACK] All retries failed. Trying with just your question (no history)...")
    try:
        fallback_msgs = [
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": last_user},
        ]
        r = client.chat.completions.create(model=MODEL, messages=fallback_msgs, max_tokens=300)
        result = r.choices[0].message.content or "[No response]"
        print(result, end="", flush=True)
        return result
    except Exception as e:
        return f"Error (after retries and fallback): {e}"


def chat_loop():
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
    ]
    print("Modern Chat (summarise + retry + fallback) — 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        messages = summarise_and_fit(messages, MAX_HISTORY_TOKENS - RESERVE_FOR_REPLY)
        print("AI: ", end="", flush=True)

        reply = chat_with_retry(messages, stream=True)
        print("\n")
        messages.append({"role": "assistant", "content": reply})

    print("Bye!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        msgs = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": q},
        ]
        msgs = summarise_and_fit(msgs, MAX_HISTORY_TOKENS - RESERVE_FOR_REPLY)
        print(chat_with_retry(msgs, stream=False))
    else:
        chat_loop()
