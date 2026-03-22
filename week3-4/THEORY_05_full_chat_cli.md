# Theory: Full Chat CLI — The Capstone

**Read before:** `05_full_chat_cli.py`

---

## What We're Building

A **production-style** chat CLI that uses everything you learned:

| Feature | From |
|---------|------|
| Multi-turn history | Day 1 (chat app) |
| Streaming replies | Day 2 + 4 |
| Context trimming | Day 3 |

This is the "weekend project" — the final piece that ties Chat & Context together.

---

## 🤔 Q&A: Design Choices

### Q1: "When do I trim the context?"

**Before** each API call. Check token count; if over your limit, trim oldest messages, then send.

---

### Q2: "What limit should I use?"

Depends on the model. Llama 3.1 8B has ~128K. For a CLI, 4000–8000 tokens for history is plenty. Leave room for the new reply (e.g., reserve 500 tokens).

---

### Q3: "Should I add error handling?"

Yes. Use try/except (Week 2). On failure, don't append a broken assistant message. Optionally retry on rate limit.

---

### Q4: "What about the system message?"

Keep it. Trim **conversation pairs** (user + assistant) first. Only trim the system message if you're desperate — it's usually short.

---

### Q5: "How do I structure the code?"

```
main loop:
  - get user input
  - append user msg to messages
  - trim messages to fit (use Day 3's trim_to_fit)
  - call API with stream=True
  - collect chunks, print as they arrive
  - append full reply to messages
```

Reuse functions from 01, 02, 03: `trim_to_fit`, `estimate_tokens`, streaming loop.

---

## What You'll Learn by Building

1. **Composition** — combining small pieces into one app
2. **Real constraints** — token limits, errors, UX
3. **Patterns** — how chat apps are built in the real world

---

## Checklist Before You Run

- [ ] Messages list with system message
- [ ] Append user, call API, append assistant (full reply)
- [ ] stream=True, collect chunks for history
- [ ] Trim before each call when over limit
- [ ] try/except for API errors
