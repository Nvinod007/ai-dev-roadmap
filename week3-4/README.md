# Week 3–4: Chat & Context

**Focus:** AI chat apps, streaming responses, and context window management.

**📚 Learn theory + practice:** Read each theory doc first, then run the Python file.

| Day | Theory | Practice | What you learn |
|-----|--------|----------|----------------|
| 1 | [THEORY_01_chat_apps.md](THEORY_01_chat_apps.md) | `01_chat_app.py` | Multi-turn chat, conversation history |
| 2 | [THEORY_02_streaming.md](THEORY_02_streaming.md) | `02_streaming.py` | Token-by-token streaming, UX |
| 3 | [THEORY_03_context_windows.md](THEORY_03_context_windows.md) | `03_context_window.py` | Token limits, trimming history |
| 4 | [THEORY_04_streaming_chat.md](THEORY_04_streaming_chat.md) | `04_streaming_chat.py` | Chat + streaming combined |
| 5 | [THEORY_05_full_chat_cli.md](THEORY_05_full_chat_cli.md) | `05_full_chat_cli.py` | **Capstone:** Full chat with streaming + context trim |
| 6 | [THEORY_06_modern_context.md](THEORY_06_modern_context.md) | `06_modern_chat.py` | **Modern:** Summarize instead of trim, retry, fallback |

## Run

```bash
python week3-4/01_chat_app.py
python week3-4/02_streaming.py
python week3-4/03_context_window.py
python week3-4/04_streaming_chat.py
python week3-4/05_full_chat_cli.py
python week3-4/06_modern_chat.py
```

## Day 5: Full Chat CLI

Run interactive mode:
```bash
python week3-4/05_full_chat_cli.py
```

Or ask a single question:
```bash
python week3-4/05_full_chat_cli.py "Explain recursion"
```
