# Week 1: Python Essentials

**Order to follow:** Do these in sequence. Run each file and understand it before moving on.

**📚 Theory first:** Read [THEORY.md](THEORY.md) to understand *why* we learn each topic for AI development.

| Day | Theory | Practice | What you learn |
|-----|--------|----------|----------------|
| 1 | [THEORY.md](THEORY.md) | `01_variables_types.py` | Variables, functions, loops |
| 2 | [THEORY.md](THEORY.md) | `02_lists_dicts_json.py` | Lists, dicts, JSON (used in API calls!) |
| 3 | [THEORY.md](THEORY.md) | `03_requests_http.py` | HTTP GET with `requests` |
| 4 | [THEORY.md](THEORY.md) | `04_env_variables.py` | `.env` and `python-dotenv` |
| 5 | [THEORY.md](THEORY.md) | `05_combine_all.py` | Put it all together |

## Setup

```bash
cd /Users/vinodkumar.nelanakula/Desktop/projects/ai
pip install -r requirements.txt
```

Create a `.env` file in the project root (copy from `.env.example`):

```
GROQ_API_KEY=your-groq-api-key-here
```

## Run each exercise

```bash
python week1/01_variables_types.py
python week1/02_lists_dicts_json.py
# ... etc
```

## Weekend project

Build a CLI that fetches from `https://jsonplaceholder.typicode.com/users` and prints each user's name and email. Use functions, loops, and env vars.
