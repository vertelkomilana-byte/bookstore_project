import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT title, amount
FROM book
WHERE amount < 5;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()