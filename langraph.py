# db_agent_coder.py
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
import sqlite3
from langsmith import traceable
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "pr-smug-community-5"

# Tool 1: List all table names
def list_tables():
    """List all table names in the SQLite database."""
    conn = sqlite3.connect("langchain.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

# Tool 2: Describe table schema
def describe_table(table_name):
    """Describe the schema of a given table. Returns (column name, type)."""
    conn = sqlite3.connect("langchain.db")
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    conn.close()
    return [(col[1], col[2]) for col in columns]

# Tool 3: Execute a SQL query
def run_query(query):
    """Run a SQL query. Use only for SELECT or safe queries."""
    conn = sqlite3.connect("langchain.db")
    cursor = conn.cursor()
    cursor.execute(query)
    if query.strip().lower().startswith("select"):
        results = cursor.fetchall()
    else:
        conn.commit()
        results = [["✅ Query executed."]]
    conn.close()
    return results


# Set up the agent
tools = [list_tables, describe_table, run_query]
model = ChatOllama(model="qwen2.5-coder:7b")  # Make sure this model is pulled in Ollama
system_prompt = """You are a helpful assistant that interacts with a store's SQLite database.
You can use tools to:
- list tables
- describe table schemas
- execute SQL queries

Use the tools to gather information before answering.
Only use SELECT queries unless absolutely needed."""

graph = create_react_agent(model, tools, prompt=system_prompt)

@traceable
def chat(question):
    inputs = {"messages": [("user", question)]}
    output = graph.invoke(inputs)
    return output["messages"][-1].content

# Main loop
if __name__ == "__main__":
    print("🧠 AI SQL Agent (Qwen2.5-Coder) - type 'exit' to quit")
    while True:
        question = input("\nYou: ")
        if question.lower() in {"exit", "quit"}:
            break
        answer = chat(question)
        print("Agent:", answer)
