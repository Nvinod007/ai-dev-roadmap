# Week 2: LLM APIs + Prompt Engineering

**Focus:** Groq API (OpenAI-compatible), message roles, prompt patterns, API params, error handling.

**📚 Learn theory + practice:** For each day, read the theory doc first, then run the Python file.

| Day | Theory | Practice | What you learn |
|-----|--------|----------|----------------|
| 1 | [THEORY_01_system_user_messages.md](THEORY_01_system_user_messages.md) | `01_system_user_messages.py` | System vs user vs assistant, multi-turn |
| 2 | [THEORY_02_prompt_patterns.md](THEORY_02_prompt_patterns.md) | `02_prompt_patterns.py` | Role, task, format, few-shot, chain-of-thought |
| 3 | [THEORY_03_api_params.md](THEORY_03_api_params.md) | `03_api_params.py` | temperature, max_tokens, response_format |
| 4 | [THEORY_04_error_handling.md](THEORY_04_error_handling.md) | `04_error_handling.py` | try/except, retries, rate limits |
| 5 | — | `05_cli_assistant.py` | **Project:** CLI AI assistant |

## Run

```bash
python3 week2/01_system_user_messages.py
python3 week2/02_prompt_patterns.py
# ... etc
```

## Weekend project

`05_cli_assistant.py` — Run with a question or use interactive mode:

```bash
python3 week2/05_cli_assistant.py "Explain React hooks"
# or
python3 week2/05_cli_assistant.py
```
