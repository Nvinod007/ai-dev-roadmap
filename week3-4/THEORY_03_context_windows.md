# Theory: Context Windows

**Read before:** `03_context_window.py`

---

## What is a Context Window?

The **context window** is how much text the model can "see" at once — your prompt + the model's response. It's measured in **tokens**.

Think of it as the model's **short-term memory limit**. Too much text → it forgets the beginning or errors out.

---

## 🤔 Q&A: Your Doubts Answered

### Q1: "What's the limit? How many tokens?"

Depends on the model. Examples (approximate):

| Model | Context window |
|-------|----------------|
| Llama 3.1 8B (Groq) | ~128,000 tokens |
| Older models | 4,000–8,000 tokens |
| GPT-4 | 128,000 tokens |

Check the provider's docs for your model.

---

### Q2: "What counts toward the limit?"

**Everything you send + everything the model generates.**

- Your system message
- All user messages
- All assistant messages (history)
- The new reply the model is generating

All of that must fit inside the window.

---

### Q3: "What happens if I exceed the limit?"

The API may:
- **Reject** the request (error)
- **Truncate** (cut off old messages)
- **Fail** mid-response

Better to **trim yourself** before sending.

---

### Q4: "How do I count tokens?"

You don't have to count by hand. Use a library:

```python
import tiktoken  # OpenAI's tokenizer
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("Your text here")
print(len(tokens))  # Token count
```

Or estimate: ~4 characters per token for English.

---

### Q5: "So in a long chat, I keep appending messages. When do I trim?"

When you're **getting close** to the limit. For example, if the limit is 8,000 tokens:

- Keep a **buffer** (e.g., 1,000 tokens) for the reply
- Use ~7,000 for your messages
- When history exceeds that, **remove the oldest** messages

---

### Q6: "Which messages do I remove first?"

**Oldest first.** The model needs recent context most. Keep:
- System message (important, usually short)
- Recent user + assistant exchanges
- Drop the oldest back-and-forth

---

### Q7: "Can I summarize old messages instead of deleting?"

Yes! Advanced approach: when trimming, send old messages to the API and ask "Summarize this conversation in 2 sentences." Use that summary as context. More work, but preserves more history.

For learning, **simple trimming** (drop oldest) is enough.

---

### Q8: "What's a good strategy for a chat app?"

1. Set a **max history tokens** (e.g., 4000 for 8K model)
2. Before each API call, **count** tokens in your messages
3. If over limit: remove oldest (user + assistant) pair
4. Repeat until under limit
5. Send to API

---

### Q9: "Does the system message count? Should I trim it?"

Yes, it counts. Usually the system message is short (one paragraph) — keep it. Trim **conversation turns** (user/assistant pairs) first.

---

## Summary

| Concept | Meaning |
|---------|---------|
| **Context window** | Max tokens the model can process (input + output) |
| **Token limit** | Check model docs; e.g., 8K, 32K, 128K |
| **Trim strategy** | Remove oldest messages when approaching limit |
| **Keep** | System message + recent conversation |

---

## Rough Token Estimates

| Content | Approx tokens |
|---------|---------------|
| 1 word | 1–2 |
| 1 sentence | 10–20 |
| 1 paragraph | 50–100 |
| 1 page | 200–400 |
