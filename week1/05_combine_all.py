"""
Week 1 - Day 5: Combine everything
Run: python week1/05_combine_all.py

This ties together: env vars, requests, JSON, and functions.
"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_post(post_id: int) -> dict | None:
    """
    Fetch a post from JSONPlaceholder API.
    Returns the post dict or None if request fails.
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return None


def main():
    # Use env var for post ID, or default to 1
    post_id = int(os.getenv("POST_ID", "1"))
    
    post = fetch_post(post_id)
    if post:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body'][:100]}...")
    else:
        print("Failed to fetch post")


if __name__ == "__main__":
    main()
