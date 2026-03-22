# Theory: Error Handling & Retries

**Read this before:** `04_error_handling.py`

---

## Why APIs Fail

When you call an LLM API, things can go wrong:

- **Rate limit (429)** — You sent too many requests too fast
- **Invalid request** — Bad model name, malformed input
- **Timeout** — Server took too long
- **Quota exceeded** — Free tier limit reached
- **Network error** — No internet, DNS failure

Your app should handle these gracefully instead of crashing.

---

## 1. Basic try/except

Wrap API calls in `try/except` so errors don't crash your program.

```python
try:
    response = client.chat.completions.create(...)
    return response.choices[0].message.content
except Exception as e:
    print(f"Error: {e}")
    return None
```

**Why:** Users see a friendly message (or fallback) instead of a stack trace.

---

## 2. Retry with Backoff (Rate Limits)

**429** = "Too Many Requests" — the API says "slow down."

### Strategy: Exponential Backoff

1. Try the request
2. If 429 → wait 30s, try again
3. If 429 again → wait 60s, try again
4. Give up after N retries

### Why Backoff?

- Retrying **immediately** often hits the limit again
- Waiting gives the API time to reset your quota
- Longer wait each retry = more polite to the server

### In Code

```python
for attempt in range(max_retries):
    try:
        return client.chat.completions.create(...)
    except Exception as e:
        if "429" in str(e) or "rate" in str(e).lower():
            wait = 30 * (attempt + 1)  # 30s, 60s, 90s...
            time.sleep(wait)
        else:
            return None  # Different error — don't retry
```

---

## 3. Empty or Invalid Responses

Sometimes the API returns 200 OK but:

- Empty content
- Malformed JSON (when you expected JSON)
- "Refusal" or blocked content

### Defense

- Check `if content and content.strip()` before using
- Provide a fallback: `return content or "[No response]"`
- When expecting JSON, wrap parsing in try/except

---

## 4. User-Friendly Error Messages

Don't show raw API errors to users. Map them:

| Raw error        | User message                          |
|------------------|----------------------------------------|
| Model not found  | "Model not found. Check your model name." |
| 429 rate limit   | "Too many requests. Please wait a moment." |
| Invalid API key  | "Authentication failed. Check your API key." |
| Timeout          | "Request took too long. Try again."    |

---

## Summary

1. **Always** use try/except around API calls
2. **Retry** on 429/rate-limit with increasing waits
3. **Validate** responses (non-empty, valid format)
4. **Translate** technical errors into user-friendly messages
