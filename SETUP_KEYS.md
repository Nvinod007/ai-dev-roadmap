# API Key Setup (Groq)

**Free tier — 30 req/min, no credit card required.**

1. **Get your key:** https://console.groq.com/keys
2. Sign up → Create API key
3. Add to `.env` in project root (copy from `.env.example`):

```
GROQ_API_KEY=your-key-here
GROQ_API_BASE=https://api.groq.com/openai/v1
GROQ_MODEL=llama-3.1-8b-instant
```

`GROQ_API_BASE` and `GROQ_MODEL` are optional — defaults are used if not set.

4. Run any Week 2 script:

```bash
pip install -r requirements.txt
python3 week2/01_system_user_messages.py
```

**Model:** `llama-3.1-8b-instant` — fast, good for learning.

## Passing the key in code

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
```
