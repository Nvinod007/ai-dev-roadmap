"""
Week 2 - Day 1: System, User, and Assistant Messages
Run: python3 week2/01_system_user_messages.py

Uses Groq API (free, 30 req/min). Get key: https://console.groq.com/keys

=== THEORY ===
  • SYSTEM = how the model should behave (persona, tone)
  • USER = what the human asks
  • ASSISTANT = what the model said before (for multi-turn)
  • API is STATELESS — you send full history each time
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


def section(title, emoji="📌"):
    print(f"\n{emoji} {'─' * 40}")
    print(f"   {title}")
    print(f"   {'─' * 40}")


def show(user_msg, ai_reply, note=""):
    print(f"   You:  {user_msg}")
    print(f"   AI:   {ai_reply[:150]}{'...' if len(ai_reply) > 150 else ''}")
    if note:
        print(f"   💡 {note}")
    print()


# ═══════════════════════════════════════════════════════════
#  Demo 1: User only (simplest)
# ═══════════════════════════════════════════════════════════
section("Demo 1: User message only", "1️⃣")

response1 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is 2+2?"}],
)
show("What is 2+2?", response1.choices[0].message.content, "Just 1 message: role=user")

# ═══════════════════════════════════════════════════════════
#  Demo 2: System + User (set the persona)
# ═══════════════════════════════════════════════════════════
section("Demo 2: System + User (persona)", "2️⃣")

response2 = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a pirate. Answer in pirate speak."},
        {"role": "user", "content": "What is 2+2?"},
    ],
)
show("What is 2+2?", response2.choices[0].message.content, "System sets HOW to answer")

# ═══════════════════════════════════════════════════════════
#  Demo 3: Multi-turn (stateless — send full history)
# ═══════════════════════════════════════════════════════════
section("Demo 3: Multi-turn chat (remembers context)", "3️⃣")

# Turn 1: User says name
r1 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "My name is Vinod."}],
)
reply1 = r1.choices[0].message.content
show("My name is Vinod.", reply1, "API has no memory — we store this reply")

# Turn 2: User asks follow-up — we MUST send previous exchange
r2 = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "My name is Vinod."},
        {"role": "assistant", "content": reply1},
        {"role": "user", "content": "What's my name?"},
    ],
)
show("What's my name?", r2.choices[0].message.content, "We sent full history: user + assistant + user")

print("   ✅ Done! 3 demos learned.\n")
