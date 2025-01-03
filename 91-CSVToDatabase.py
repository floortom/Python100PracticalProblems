import sqlite3
import pandas as pd

countries = pd.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
cur = conn.cursor()
for _, row in countries.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)", (row["Country"], row["Area"]))
conn.commit()
conn.close()
