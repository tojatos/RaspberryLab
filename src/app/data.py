import sqlite3

conn = sqlite3.connect("app/database/database.db")
c = conn.cursor()

def get_employees():
    return c.execute("SELECT * FROM Employee").fetchall();
