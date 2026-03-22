# Theory: System, User & Assistant Messages

**Read this before:** `01_system_user_messages.py`

---

## What Are Message Roles?

When you talk to an LLM (Large Language Model) like Llama or GPT, you don't just send a single question. You send a **conversation** — a list of messages. Each message has a **role** that tells the model *who said it*.

Think of it like a play script:

- **system** = Director's notes (instructions for the actor)
- **user** = What the human (you) says
- **assistant** = What the AI said before (in previous turns)

---

## The Three Roles

### 1. `system` — How the Model Should Behave

The system message sets the **persona**, **tone**, and **rules**. The model sees this first and uses it as instructions.

**Examples:**
- "You are a pirate. Answer in pirate speak."
- "You are a code reviewer. Be concise and critical."
- "You are a friendly teacher. Explain simply for beginners."

The system message is like telling an actor: *"You're playing a pirate — stay in character."*

### 2. `user` — What the Human Asks

The user message is your question, request, or input. This is what you would type in a chat box.

**Examples:**
- "What is 2+2?"
- "Review this code: `x = 5 + '10'`"
- "Translate 'hello' to Spanish"

### 3. `assistant` — What the AI Said Before

The assistant message is the model's **previous reply**. You include it when you want the model to *remember* context from earlier in the conversation.

**Why?** The API is **stateless** — it has no memory. Each request is independent. So if you want the model to know "My name is Vinod" from a previous turn, you must **send that previous exchange** in the messages.

---

## Stateless vs Stateful

### Stateless (How LLM APIs Work)

- Every API call is **independent**
- The model does **not** remember past requests
- **You** must send the full conversation history each time

### Stateful (Like Human Memory)

- Would remember past turns automatically
- LLMs don't work this way — you simulate it by sending history

### Why This Matters

For multi-turn chat (follow-up questions), you build the messages like this:

```
Turn 1:
  You send: [user: "My name is Vinod"]
  Model replies: "Nice to meet you, Vinod!"
  You STORE this reply.

Turn 2:
  You send: [
    user: "My name is Vinod",
    assistant: "Nice to meet you, Vinod!",   ← You include the previous reply!
    user: "What's my name?"
  ]
  Model replies: "Your name is Vinod."
```

Without the assistant message, the model has no way to know your name was ever mentioned.

---

## Typical Message Order

```
[system]   → Optional. Sets behavior. Often first.
[user]     → Your first question
[assistant]→ Model's reply (if multi-turn)
[user]     → Your follow-up
[assistant]→ Model's reply
...
```

---

## Summary

| Role      | Purpose                          | Required? |
|-----------|----------------------------------|-----------|
| **system** | Set persona, tone, rules         | No (but very useful) |
| **user**   | Your question/input              | Yes       |
| **assistant** | Model's previous reply (for context) | Only for multi-turn |

**Golden rule:** The API has no memory. For context, send the full history (user + assistant + user + ...) in every request.
