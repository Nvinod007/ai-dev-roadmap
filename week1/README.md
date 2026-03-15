# Week 1: Python Essentials

**Order to follow:** Do these in sequence. Run each file and understand it before moving on.

| Day | File | What you learn |
|-----|------|----------------|
| 1 | `01_variables_types.py` | Variables, functions, loops |
| 2 | `02_lists_dicts_json.py` | Lists, dicts, JSON (used in API calls!) |
| 3 | `03_requests_http.py` | HTTP GET with `requests` |
| 4 | `04_env_variables.py` | `.env` and `python-dotenv` |
| 5 | `05_combine_all.py` | Put it all together |

## Setup

```bash
cd /Users/vinodkumar.nelanakula/Desktop/projects/ai
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Run each exercise

```bash
python week1/01_variables_types.py
python week1/02_lists_dicts_json.py
# ... etc
```

## Weekend project

Build a CLI that fetches from `https://jsonplaceholder.typicode.com/users` and prints each user's name and email. Use functions, loops, and env vars.
