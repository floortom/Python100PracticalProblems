import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

for row in rows:
    print(row[0])
