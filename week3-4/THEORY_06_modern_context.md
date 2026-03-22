# Theory: Modern Context Management (Summarize + Retry + Fallback)

**Read before:** `06_modern_chat.py`

---

## Beyond Simple Trimming

Day 3–5 used **trimming**: drop oldest messages when over limit. Simple, but you lose context.

**Modern approach:** **Summarize** old messages into a short context block instead of deleting. Preserves key facts and decisions.

---

## 🤔 Q&A

### Q1: "How does summarization work?"

When over the token limit:
1. Take the **oldest** messages (everything except the last 1–2 turns)
2. Call the LLM: *"Summarize this conversation in 2–4 sentences. Preserve key facts and context."*
3. Replace those messages with **one** message: *"Previous conversation: [summary]"*
4. Keep system + summary + recent turns
5. Send to API

You keep context, use fewer tokens.

---

### Q2: "Why not always summarize? Why trim at all?"

Summarization costs an **extra API call** per summarize. Use it when:
- History is long and context matters
- You want to preserve important details

Trimming is simpler and free. Use it when:
- Speed matters
- Context is less critical
- You want to avoid extra cost

In `06_modern_chat.py` we use **summarize** as the main strategy when over limit.

---

### Q3: "What about retries?"

On API error (network, rate limit, etc.):
1. Retry up to 3 times with **exponential backoff** (wait 2s, 4s, 8s…)
2. On rate limit (429): retry
3. On other errors: retry a few times, then fallback

---

### Q4: "What's the fallback?"

If retries all fail:
- Try **one more time** with **only the user's current question** (no history)
- User still gets an answer, but without conversation context
- Better than showing "Error" and failing completely

---

### Q5: "What else is 'modern' here?"

| Feature | Purpose |
|---------|---------|
| **Summarize vs trim** | Preserve context, not just drop |
| **Retry with backoff** | Handle transient failures |
| **Fallback to single turn** | Graceful degradation |
| **Logging** | See when summarize/retry/fallback happen |

---

## Summary

1. **Over limit** → Summarize old messages instead of trimming
2. **API error** → Retry with backoff (2s, 4s, 8s)
3. **All retries fail** → Fallback: ask with just the user's question
4. **Log** → When we summarize, retry, or fallback
