"""
Week 1 - Day 3: HTTP calls with requests
Run: python week1/03_requests_http.py

Install first: pip install requests
"""

import requests

# === 1. Simple GET request (no API key needed) ===
# JSONPlaceholder - free fake API for testing
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("Status code:", response.status_code)
print("Response (dict):", response.json())

# === 2. Extract data from response ===
data = response.json()
print("Post title:", data["title"])
print("Post body:", data["body"][:50] + "...")

# === 3. GET with query params ===
response2 = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}  # ?userId=1
)
posts = response2.json()
print(f"\nGot {len(posts)} posts for user 1")

# === 4. Error handling ===
bad_response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
if bad_response.status_code == 200:
    print(bad_response.json())
else:
    print("Request failed:", bad_response.status_code)

# === 5. Your exercise ===
# Call https://jsonplaceholder.typicode.com/users/1
# Print the user's name and email.

response_user = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
)
user = response_user.json()
print(f"User name: {user['name']}")
print(f"User email: {user['email']}")