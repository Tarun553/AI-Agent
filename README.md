# 🧠 Private AI SQL Assistant with LangGraph + Ollama + Qwen2.5-Coder

This project is a command-line AI assistant that can interact with a local SQLite database using natural language. It uses:

- [LangGraph](https://github.com/langchain-ai/langgraph) for creating ReAct-based agents
- [Ollama](https://ollama.com/) to run local LLMs like `qwen2.5-coder:7b`
- [LangChain](https://www.langchain.com/) tools integration
- A local SQLite database (`langchain.db`) for executing SQL queries

---

## 📦 Requirements

- Python 3.10+
- [Ollama installed](https://ollama.com/download)
- SQLite (comes with Python)
- Required Python libraries (see below)

---

## 🧠 LLM Used

This project uses the [Qwen2.5-Coder:7B](https://huggingface.co/Qwen/Qwen2.5-7B-Chat) model via Ollama:

```bash
ollama pull qwen2.5-coder:7b
