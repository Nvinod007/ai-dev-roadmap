"""
Week 1 - Day 2: Lists, Dicts, and JSON
Run: python week1/02_lists_dicts_json.py

These are essential for working with API responses (like OpenAI returns).
"""

# === 1. Lists ===
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"},
]
print("First message:", messages[0])
print("Role of first:", messages[0]["role"])

# === 2. Dicts (dictionaries) ===
# This is what OpenAI API expects!
message_dict = {
    "role": "user",
    "content": "Explain React hooks"
}
print("Dict:", message_dict)
print("Content:", message_dict["content"])

# === 3. JSON - Python's json module ===
import json

# Convert Python dict to JSON string (what APIs send over the wire)
json_string = json.dumps(message_dict)
print("As JSON string:", json_string)

# Convert JSON string back to Python dict (what you get from API responses)
parsed = json.loads(json_string)
print("Parsed back:", parsed)

# === 4. Simulating an API response ===
fake_api_response = {
    "choices": [
        {"message": {"content": "React hooks let you use state in function components."}}
    ]
}
content = fake_api_response["choices"][0]["message"]["content"]
print("Extracted content:", content)

# === 5. Your exercise ===
# Create a list of 2 message dicts (user + assistant).
# Use json.dumps() to print it as a JSON string.
