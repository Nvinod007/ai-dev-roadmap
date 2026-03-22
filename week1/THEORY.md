# Theory: Week 1 — Why We Learn These Topics

**Purpose:** Week 1 teaches Python basics that are **essential** for AI development. Here's the *why* behind each topic.

---

## 1. Variables, Functions, Loops

**Files:** `01_variables_types.py`

### Why for AI Dev?

- You store API keys, model names, and config in **variables**
- You wrap API calls in **functions** for reuse and clarity
- You loop over lists of prompts, messages, or results

Everything you build in AI is structured with these basics.

---

## 2. Lists, Dicts, JSON

**Files:** `02_lists_dicts_json.py`

### Why for AI Dev?

LLM APIs send and receive **JSON**. Understanding dicts and lists is critical because:

- **Messages** are a list of dicts: `[{"role": "user", "content": "Hello"}]`
- **API responses** are nested dicts: `response.choices[0].message.content`
- You parse JSON with `json.loads()` and build it with `json.dumps()`

Without dicts and JSON, you can't talk to any AI API.

---

## 3. HTTP with requests

**Files:** `03_requests_http.py`

### Why for AI Dev?

LLM APIs are **HTTP APIs**. You send POST requests with your prompt and get back JSON.

- `requests.get()` / `requests.post()` — how you call any API
- Status codes (200, 429, 401) — success, rate limit, auth failure
- `response.json()` — parse the response

We use the `openai` library (which uses `requests` under the hood), but the same concepts apply.

---

## 4. Environment Variables (.env)

**Files:** `04_env_variables.py`

### Why for AI Dev?

**Never hardcode API keys.** They go in `.env` and you load them with `python-dotenv`.

- `GROQ_API_KEY`, `OPENAI_API_KEY` — secrets stay out of code
- `.env` in `.gitignore` — never commit keys to Git
- `os.getenv("KEY")` — read in code

This is standard practice for any production app.

---

## 5. Combine All

**Files:** `05_combine_all.py`

### Why for AI Dev?

Real apps use everything together: env vars for config, HTTP for APIs, JSON for data, functions for structure. Week 1's capstone ties these together before you move to LLM APIs in Week 2.

---

## Flow: Week 1 → Week 2

```
Week 1: Variables, dicts, JSON, HTTP, .env
         ↓
Week 2: Use all of the above to call Groq API
        - Messages = list of dicts (Week 1)
        - API key from .env (Week 1)
        - Parse JSON response (Week 1)
```
