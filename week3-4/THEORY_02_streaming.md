# Theory: Streaming

**Read before:** `02_streaming.py`

---

## What is Streaming?

**Normal (non-streaming):** Send prompt → wait (5–10 seconds) → get full answer at once.

**Streaming:** Send prompt → get the answer **word by word** as the AI "types" it. Like watching someone type in real time.

---

## 🤔 Q&A: Your Doubts Answered

### Q1: "Why would I want streaming? Isn't waiting the same?"

**UX (User Experience).** Users feel the app is **faster** when they see text appearing immediately. Waiting 8 seconds in silence feels slow; seeing words pop up one by one feels responsive.

Think: ChatGPT — you see it "typing." That's streaming.

---

### Q2: "Does the AI actually type? Or is it an illusion?"

The model generates tokens one at a time. Normally the API waits until it's done, then returns everything. With streaming, the API sends each token as soon as it's ready. So yes — the model really does produce output incrementally.

---

### Q3: "What's a token again?"

A **token** is a chunk of text — roughly 4 characters in English. "Hello" ≈ 1 token. "Streaming" ≈ 2 tokens. The model generates tokens, not whole sentences at once.

---

### Q4: "How do I turn on streaming in code?"

Use `stream=True` in the API call:

```python
response = client.chat.completions.create(
    model=MODEL,
    messages=[...],
    stream=True,   # ← This changes everything
)
```

Now `response` is not a single object — it's an **iterator** (a stream of chunks).

---

### Q5: "What do I get back? A string? A list?"

A **stream of chunks**. Each chunk is a small piece of the response. You **loop** over them:

```python
for chunk in response:
    # Each chunk has a tiny bit of text
    part = chunk.choices[0].delta.content
    if part:
        print(part, end="")
```

`delta.content` = the new text in this chunk. Sometimes it's empty; always check.

---

### Q6: "Why 'delta'? What does that mean?"

**Delta** = change, difference. Each chunk contains only the **new** part since the last chunk. You're getting the "delta" (the change), not the full text so far.

---

### Q7: "Can I still get the full response if I stream?"

Yes. Just collect the chunks:

```python
full = ""
for chunk in response:
    part = chunk.choices[0].delta.content or ""
    full += part
    print(part, end="")  # Show as it arrives
# Now 'full' has the complete response
```

---

### Q8: "Does streaming cost more? Use more tokens?"

**No.** Same tokens, same cost. You're just receiving them in a different way.

---

### Q9: "When should I use streaming?"

| Use streaming when | Don't stream when |
|--------------------|-------------------|
| Chat UI (user watches response) | You need the full text to parse (e.g., JSON) |
| Long responses | Short one-word answers |
| Better UX matters | Running in background, no user watching |

---

## Summary

| Concept | Meaning |
|---------|---------|
| **stream=True** | Get tokens as they're generated, not all at once |
| **Chunks** | Small pieces; loop with `for chunk in response` |
| **delta.content** | The new text in each chunk |
| **Why** | Feels faster, better UX |
