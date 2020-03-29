import sqlite3
from time import gmtime, strftime

conn = sqlite3.connect("app/database/database.db")
c = conn.cursor()

def fetchall(sql):
    return c.execute(sql).fetchall()

def get_employees():
    return fetchall("SELECT * FROM Employee")

def get_cards():
    return fetchall("SELECT * FROM Card")

def get_card_readings():
    return fetchall("SELECT * FROM CardReading")

def get_terminals():
    return fetchall("SELECT * FROM Terminal")

def insert_employee(name):
    c.execute("INSERT INTO Employee (name) VALUES (?)", (name,))
    conn.commit()

def insert_card(rfid):
    c.execute("INSERT INTO Card (rfid) VALUES (?)", (rfid,))
    conn.commit()

def insert_terminal(name):
    c.execute("INSERT INTO Terminal (name) VALUES (?)", (name,))
    conn.commit()

def update_card_employee(rfid, employee_id=None):
    c.execute("UPDATE Card SET employeeId = ? WHERE rfid = ?", (employee_id, rfid))
    conn.commit()

def insert_card_reading(terminal_id, rfid):
    c.execute("INSERT INTO CardReading (terminalId, rfid, readTime) VALUES (?, ?, ?)",
              (terminal_id, rfid, strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    conn.commit()
