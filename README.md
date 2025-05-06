# 🧠 AI SQL Agent with LangGraph, Ollama, and LangSmith

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-local--LLM-orange)](https://ollama.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agent--Orchestration-purple)](https://github.com/langchain-ai/langgraph)
[![LangChain](https://img.shields.io/badge/LangChain-tool--integration-yellow)](https://www.langchain.com/)
[![SQLite](https://img.shields.io/badge/SQLite-database-blue)](https://www.sqlite.org/)

An interactive AI-powered SQL assistant that connects to a local SQLite database and answers natural language questions using advanced LLMs. It leverages **LangGraph** for agent orchestration, **LangChain** for tool integration, **Ollama** (with the `Qwen2.5-Coder` model) for language understanding, and **LangSmith** for tracing and debugging.

---

## 🎥 Demo

![AI SQL Agent Demo](https://raw.githubusercontent.com/Tarun553/AI-Agent/main/Screenshot2025-05-06%20052509.png)


*Example: Natural language SQL queries with LLM-powered responses*

> ℹ️ Replace the image URL with your actual demo GIF or video preview hosted on GitHub or an image hosting service.

---

## 🚀 Features

- **Natural Language SQL Agent**: Ask questions about your database in plain English.
- **Automated Tool Use**: List tables, describe schemas, and execute queries.
- **LangSmith Tracing**: Debug and analyze interactions with ease.
- **Extensible Architecture**: Add tools or swap out the LLM with minimal effort.

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Tarun553/AI-Agent.git
cd AI-Agent
