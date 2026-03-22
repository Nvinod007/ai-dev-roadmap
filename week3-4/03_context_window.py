"""
Week 3-4 - Day 3: Context Window Management
Run: python week3-4/03_context_window.py

Models have token limits. Trim old messages when history gets too long.

No API call here — this file teaches the LOGIC you use BEFORE calling the API.
"""

# Rough estimate: ~4 chars per token for English
def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def count_messages_tokens(messages: list) -> int:
    total = 0
    for msg in messages:
        total += estimate_tokens(msg.get("content", ""))
    return total


def trim_to_fit(messages: list, max_tokens: int = 2000) -> list:
    """
    Remove oldest user+assistant pairs until under max_tokens.
    Keep system message + recent turns.
    """
    if count_messages_tokens(messages) <= max_tokens:
        return messages

    # Keep system (index 0) and trim from the rest
    result = [messages[0]] if messages and messages[0]["role"] == "system" else []
    rest = messages[1:] if result else messages

    # Remove oldest pairs from the end of 'rest' (we'll reverse logic: keep newest)
    while rest and count_messages_tokens(result + rest) > max_tokens:
        # Remove oldest pair (first two if user+assistant, else first one)
        if len(rest) >= 2 and rest[0]["role"] == "user" and rest[1]["role"] == "assistant":
            rest = rest[2:]
        else:
            rest = rest[1:]

    return result + rest


# Demo: build a long conversation and trim it
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there! How can I help?"},
    {"role": "user", "content": "What is 2+2?"},
    {"role": "assistant", "content": "2+2 equals 4."},
    {"role": "user", "content": "And 3+3?"},
    {"role": "assistant", "content": "3+3 equals 6."},
]

print(f"Original messages: {len(messages)}")
print(f"Estimated tokens: {count_messages_tokens(messages)}")

trimmed = trim_to_fit(messages, max_tokens=50)
print(f"\nAfter trim (max 50 tokens): {len(trimmed)} messages")
print(f"Estimated tokens: {count_messages_tokens(trimmed)}")
print("\nKept messages:")
for m in trimmed:
    content = m["content"][:40] + "..." if len(m["content"]) > 40 else m["content"]
    print(f"  {m['role']}: {content}")
