"""
Week 2 - Weekend Project: CLI AI Assistant
Run: python3 week2/05_cli_assistant.py "Your question here"

Or run without args for interactive mode:
  python3 week2/05_cli_assistant.py
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


def ask_ai(question: str) -> str:
    """Send question to Groq, return answer."""
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Be concise."},
                {"role": "user", "content": question},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content or "[No response]"
    except Exception as e:
        return f"Error: {e}"


def main():
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        print(ask_ai(question))
    else:
        print("CLI AI Assistant. Type your question (or 'quit' to exit).\n")
        while True:
            question = input("You: ").strip()
            if question.lower() in ("quit", "exit", "q"):
                break
            if not question:
                continue
            print("AI:", ask_ai(question), "\n")


if __name__ == "__main__":
    main()
