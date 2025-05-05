# create a database use sqlite3
import sqlite3

with open("sample.sql", "r") as f:
    sql_script = f.read()

conn = sqlite3.connect("langchain.db")
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()
print("Database created successfully")