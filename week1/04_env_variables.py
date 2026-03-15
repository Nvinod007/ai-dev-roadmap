"""
Week 1 - Day 4: Environment variables with python-dotenv
Run: python week1/04_env_variables.py

Install first: pip install python-dotenv

Why: Never hardcode API keys! Store them in .env (and add .env to .gitignore)
"""

import os
from dotenv import load_dotenv

# Load variables from .env file into os.environ
load_dotenv()

# === 1. Read env vars ===
api_key = os.getenv("OPENAI_API_KEY")
# Returns None if not set - that's why we use .env

# === 2. With default value ===
api_base = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
print("API base (or default):", api_base)

# === 3. Check if key exists (important for API keys!) ===
if api_key:
    print("API key is set (length:", len(api_key), ")")
else:
    print("OPENAI_API_KEY not found in .env - add it for index.py to work!")

# === 4. Your .env file should look like: ===
# OPENAI_API_KEY=sk-your-key-here
#
# Create .env in project root (same folder as index.py)
# Add .env to .gitignore so you never commit secrets!
