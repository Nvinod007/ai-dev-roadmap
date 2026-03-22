# Theory: AI Chat Apps

**Read before:** `01_chat_app.py`

---

## What is an AI Chat App?

A **chat app** is like ChatGPT: you send messages, the AI replies, you send more, it remembers what you said. It's a **conversation**, not a single question-answer.

---

## 🤔 Q&A: Your Doubts Answered

### Q1: "In Week 2 we did single questions. How is chat different?"

**Single question (Week 2):** You send one message → get one reply → done. No memory.

**Chat app:** You send message 1 → reply 1 → message 2 → reply 2 → ... The AI "remembers" because you keep sending the full history each time.

---

### Q2: "Does the API remember my chat? Where is the memory?"

**The API has NO memory.** Every request is independent. The "memory" is **your responsibility** — you store the conversation in a list and send it with each new request.

```
You store:  [user: "Hi", assistant: "Hello!", user: "What's 2+2?"]
You send:   That whole list + your new message
API sees:   Full context → can answer "What's 2+2?" knowing we said hi
```

---

### Q3: "Why can't the API remember? That seems silly."

APIs are designed to be **stateless** — each request stands alone. That makes them:
- Simpler (no server-side sessions)
- Scalable (any server can handle any request)
- Flexible (you decide what to remember, what to forget)

You, the developer, are in control of the "memory."

---

### Q4: "So I send the ENTIRE chat every time? Won't that be huge?"

Yes, you send the full history each time. And yes, it can get big. That's why we learn **context windows** (Week 3–4 Day 3) — to trim old messages when we hit token limits.

---

### Q5: "What format do I send? List of what?"

A **list of message dicts**. Each dict has `role` and `content`:

```python
[
    {"role": "user", "content": "My name is Vinod"},
    {"role": "assistant", "content": "Nice to meet you, Vinod!"},
    {"role": "user", "content": "What's my name?"}  # Your new message
]
```

Order matters. Oldest first, newest last.

---

### Q6: "Do I need a system message for chat?"

Not required, but **very useful**. A system message sets the AI's personality for the whole conversation:

```python
{"role": "system", "content": "You are a helpful coding tutor. Be concise."}
```

Put it once at the start. Include it in every request (it's part of the messages list).

---

### Q7: "How does a chat loop work in code?"

```
1. messages = [system]   # Start with system message
2. Loop:
   a. User types → append {"role": "user", "content": user_input}
   b. Call API with messages
   c. Get reply → append {"role": "assistant", "content": reply}
   d. Print reply
   e. Go back to (a)
```

Each time, `messages` grows. That's your conversation history.

---

## Summary

| Concept | Meaning |
|--------|---------|
| **Stateless** | API doesn't remember — you send full history every time |
| **History** | List of {role, content} — you build and maintain it |
| **Chat loop** | Append user msg → call API → append assistant reply → repeat |

---

## Common Mistakes

1. **Forgetting to append the assistant's reply** — Next turn, the AI has no record of what it said.
2. **Wrong order** — Messages must be chronological.
3. **Losing the system message** — Include it in every request.
