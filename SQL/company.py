import sqlite3

conn = sqlite3.connect("company.db")   # this creates company.db automatically
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary INTEGER
)
""")

conn.commit()
conn.close()
print("Table created successfully")