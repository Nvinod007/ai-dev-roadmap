"""
Week 2 - Day 2: Prompt Patterns (Role, Task, Format, Few-shot)
Run: python3 week2/02_prompt_patterns.py

Structured prompts = better, consistent outputs.
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

# === 1. Role + Task + Format ===
prompt = """
You are a code reviewer.

Task: Review this code for bugs and suggest improvements.

Format: Return JSON with keys "bugs" (list) and "suggestions" (list).

Code:
x = 5
y = "10"
z = x + y
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
)
print("Role+Task+Format:\n", response.choices[0].message.content[:300])

# === 2. Few-shot (examples in prompt) ===
few_shot_prompt = """
Convert product names to slugs.

Examples:
- "Blue Running Shoes" -> blue-running-shoes
- "iPhone 15 Pro Max" -> iphone-15-pro-max
- "Coffee & Tea Set" -> coffee-tea-set

Now convert: "AI Dev Roadmap 2024"
"""

response2 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": few_shot_prompt}],
)
print("\nFew-shot result:", response2.choices[0].message.content.strip())

# === 3. Chain-of-thought (ask for reasoning) ===
cot_prompt = """
A bat and ball cost $1.10. The bat costs $1 more than the ball. What does the ball cost?

Think step by step, then give the final answer.
"""
response3 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": cot_prompt}],
)
print("\nChain-of-thought:", response3.choices[0].message.content[:200])

# === 4. Your exercise ===
# Write a prompt that extracts: name, email, phone from a messy text.
# Use Role + Task + Format. Example input: "Call John at john@mail.com or 555-1234"

your_prompt = """
You are a data extractor.

Task: Extract the name, email, and phone number from the following text:
"Call John at john@mail.com or 555-1234"

Format: Return JSON with keys "name", "email", and "phone".
"""

response4 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": your_prompt}],
)
print("\nYour exercise:", response4.choices[0].message.content)