"""
Week 2 - Day 4: Error Handling & Retries
Run: python3 week2/04_error_handling.py

APIs fail. Handle rate limits, timeouts, and invalid requests.
"""

import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_API_BASE", "https://api.groq.com/openai/v1"),
)
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# === 1. Basic try/except ===
def safe_completion(prompt: str) -> str | None:
    """Call API, return content or None on error."""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

result = safe_completion("Say hello in one word.")
print("Result:", result)
print()

# === 2. Retry with backoff (for rate limits) ===
def completion_with_retry(prompt: str, max_retries: int = 3) -> str | None:
    """Retry on rate limit (429) or quota errors."""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=20,
            )
            return response.choices[0].message.content
        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "rate" in err_str or "quota" in err_str:
                wait = 30 * (attempt + 1)
                print(f"Rate limited. Waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"Error: {e}")
                return None
    return None

result_retry = completion_with_retry("Reply with one word: yes or no.")
print("completion_with_retry result:", result_retry)
print()

# === 3. Check for empty/invalid response ===
def robust_completion(prompt: str) -> str:
    content = safe_completion(prompt)
    if content and content.strip():
        return content.strip()
    return "[No response]"

result_robust = robust_completion("What is 1+1? One word only.")
print("robust_completion result:", result_robust)
print()

# === 4. Your exercise ===
# Trigger an error: use model="invalid-model" and catch the error.
# Print a user-friendly message like "Model not found. Check your model name."
