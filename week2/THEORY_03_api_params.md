# Theory: API Parameters (temperature, max_tokens, response_format)

**Read this before:** `03_api_params.py`

---

## Why Parameters Matter

The LLM API doesn't just take your prompt. It also accepts **parameters** that control:

- **Randomness** — How creative vs predictable the output is
- **Length** — How long the response can be
- **Format** — Whether to force JSON, etc.

These knobs help you tune the model for your use case.

---

## 1. Temperature (Randomness)

**Range:** 0.0 to 2.0 (typically 0.0 to 1.0)

Controls how "random" or "creative" the model is when picking the next word.

### Low Temperature (0.0 – 0.3)

- **Deterministic** — Same prompt → very similar output each time
- Model picks the **most likely** next word
- Use for: factual answers, code, translations, math

### High Temperature (0.7 – 1.0+)

- **Creative** — Same prompt → different output each run
- Model explores less likely options
- Use for: brainstorming, creative writing, varied ideas

### Analogy

Think of it like a multiple-choice exam:

- **Temp = 0:** Always pick the answer you're 90% sure about
- **Temp = 0.7:** Sometimes pick the 60% option, the 40% option — more variety

### When to Use

| Task                 | Suggested temp |
|----------------------|----------------|
| Math, facts, code   | 0 – 0.3        |
| Summarization       | 0.3 – 0.5      |
| Chat, Q&A            | 0.5 – 0.7      |
| Brainstorming, ideas| 0.7 – 1.0      |

---

## 2. max_tokens (Response Length)

**What it is:** Maximum number of **tokens** the model can generate. 1 token ≈ 4 characters for English (roughly).

### Why It Matters

- **Too low:** Response gets cut off mid-sentence
- **Too high:** Wastes tokens (you often pay per token) and time
- **Rule of thumb:** Set slightly above what you expect. For "2 sentences", 50–100 tokens is fine.

### Example

```
max_tokens=50   → Short, concise answer
max_tokens=500  → Longer explanation
max_tokens=2048 → Long-form content
```

---

## 3. response_format (Structured Output)

Some APIs (including Groq/OpenAI) support `response_format` to **force** a structure.

### `{"type": "json_object"}`

Tells the model: *"Return valid JSON only."*

Useful when your app needs to **parse** the response (e.g., `json.loads(response)`). Without this, the model might wrap JSON in extra text like "Here's the result: {...}".

### When to Use

- Extracting structured data (name, email, phone)
- Code generation that returns objects
- Any downstream parsing

---

## 4. Usage / Token Counts

The API often returns `usage` with:

- **prompt_tokens** — How many tokens in your input
- **completion_tokens** — How many in the model's output
- **total_tokens** — Sum of both

Use this to:

- Monitor cost (many APIs charge per token)
- Debug when responses are cut off (hit max_tokens?)
- Optimize prompt length

---

## Summary

| Parameter         | Controls           | Typical use                          |
|------------------|--------------------|--------------------------------------|
| **temperature**   | Creativity         | 0 = deterministic, 1 = creative      |
| **max_tokens**    | Output length      | Cap to avoid runaway or save cost    |
| **response_format** | Output structure | Force JSON when parsing needed       |
| **usage**         | (returned) Token counts | Cost tracking, debugging           |
