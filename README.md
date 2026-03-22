# AI Dev Roadmap

**Python, LLM APIs, RAG, Agents & Copilots — building AI-powered products from scratch.**

A hands-on learning journey to become an AI / Generative AI application developer. Each week combines **theory** (why) with **practice** (code).

## How to Learn (Theory + Practice)

For every topic:

1. **Read the theory doc** — Understand concepts before coding
2. **Run the Python file** — See it in action
3. **Modify and experiment** — Break things, fix them, learn

Theory files are in each week folder: `week1/THEORY.md`, `week2/THEORY_*.md`

---

## Learning Roadmap

| Phase | Duration | Focus | Status |
|-------|----------|-------|--------|
| **Week 1** | Python Essentials | Variables, functions, HTTP, env vars | ✅ Completed |
| **Week 2** | LLM APIs + Prompt Engineering | System/user messages, prompt patterns, API params, error handling | 🔄 In Progress |
| **Week 3–4** | Chat & Context | AI chat apps, streaming, context windows | ⬜ Upcoming |
| **Week 5–8** | RAG | Vector DBs, embeddings, retrieval-augmented generation | ⬜ Upcoming |
| **Week 9–12** | Agents & Copilots | Tools, function calling, agent patterns | ⬜ Upcoming |
| **Week 13+** | Production & SaaS | Auth, billing, deployment | ⬜ Upcoming |

---

## Tech Stack

- **Language:** Python
- **LLM API:** Groq (free, 30 req/min)
- **Tools:** `requests`, `python-dotenv`, `openai`

---

## Project Structure

```
├── week1/          # Python essentials
│   ├── THEORY.md   # Why we learn each topic
│   └── 01-05_*.py  # Practice files
├── week2/          # LLM APIs + Prompt Engineering
│   ├── THEORY_01_system_user_messages.md
│   ├── THEORY_02_prompt_patterns.md
│   ├── THEORY_03_api_params.md
│   ├── THEORY_04_error_handling.md
│   └── 01-05_*.py  # Practice files
├── .env.example    # Template for API keys (copy to .env)
└── requirements.txt
```

---

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with your `GROQ_API_KEY`. Get one at https://console.groq.com/keys
