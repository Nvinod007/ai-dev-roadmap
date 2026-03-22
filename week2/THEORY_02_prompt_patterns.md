# Theory: Prompt Patterns (Role, Task, Format, Few-Shot, Chain-of-Thought)

**Read this before:** `02_prompt_patterns.py`

---

## What is a "Prompt"?

A **prompt** is the text you send to the AI model. It's your instruction or question. The way you write it dramatically affects the quality and consistency of the answer.

- **Vague:** "Review this code" → Model might do anything
- **Structured:** "You are a code reviewer. Task: Find bugs. Format: JSON with keys bugs and suggestions." → Clear, predictable output

---

## Pattern 1: Role + Task + Format

These three ingredients shape the model's behavior and output.

### Role — WHO the model should act as

You tell the model its **persona** or expertise:

- "You are a code reviewer"
- "You are a friendly teacher explaining to a 10-year-old"
- "You are a pirate"

This changes tone, focus, and style. A code reviewer thinks about bugs; a pirate talks differently.

### Task — WHAT to do

Be explicit about the goal:

- "Review this code for bugs and suggest improvements"
- "Translate this to French"
- "Summarize in 3 bullet points"

Without a clear task, the model guesses what you want.

### Format — HOW to respond

Specify the structure of the answer:

- "Return JSON with keys 'bugs' (list) and 'suggestions' (list)"
- "Answer in exactly 2 sentences"
- "Use bullet points only"

This is crucial when your app needs to **parse** the output (e.g., JSON for code).

### Example

```
Role: You are a code reviewer.
Task: Review this code for bugs and suggest improvements.
Format: Return JSON with keys "bugs" (list) and "suggestions" (list).
Code: x = 5, y = "10", z = x + y
```

---

## Pattern 2: Few-Shot

**Few-shot** = Show the model **examples** of input → output, then ask it to do the same for a new input.

Instead of explaining rules in words, you demonstrate the pattern:

```
Examples:
- "Blue Running Shoes" -> blue-running-shoes
- "iPhone 15 Pro Max" -> iphone-15-pro-max
- "Coffee & Tea Set" -> coffee-tea-set

Now convert: "AI Dev Roadmap 2024"
```

The model learns the pattern from examples (lowercase, hyphens, special characters). Works better than long explanations for format/transformation tasks.

### Zero-Shot vs Few-Shot

- **Zero-shot:** No examples — just instructions
- **Few-shot:** A few examples before the new input

Few-shot often improves accuracy and consistency.

---

## Pattern 3: Chain-of-Thought (CoT)

**Chain-of-thought** = Ask the model to "think step by step" before giving the final answer.

For math or logic, models sometimes jump to wrong answers. Explicit reasoning reduces errors.

**Example problem:**  
A bat and ball cost $1.10. The bat costs $1 more than the ball. What does the ball cost?

- **Without CoT:** Model might blurt "0.10" (wrong)
- **With CoT:** "Let total = bat + ball = 1.10. Bat = ball + 1. So (ball+1) + ball = 1.10 → 2×ball = 0.10 → ball = 0.05"

Phrases like *"Think step by step"* or *"Show your work"* trigger this behavior.

---

## When to Use Which

| Pattern              | Use when                          |
|----------------------|-----------------------------------|
| **Role + Task + Format** | Reviews, summaries, structured data, any task needing clear output shape |
| **Few-shot**         | Formatting, conversions, pattern tasks where examples are easier than rules |
| **Chain-of-thought** | Math, logic, debugging, complex reasoning |

---

## Summary

1. **Role** = Who the model pretends to be  
2. **Task** = What you want done  
3. **Format** = How the answer should look  
4. **Few-shot** = Show examples instead of (or in addition to) explaining  
5. **Chain-of-thought** = Ask for step-by-step reasoning before the answer  

These patterns are reusable building blocks for any LLM application.
