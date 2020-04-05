import sqlite3
from time import gmtime, strftime

conn = sqlite3.connect("app/database/database.db", check_same_thread=False)
c = conn.cursor()

def fetchall(sql):
    return c.execute(sql).fetchall()

def get_employees():
    return fetchall("SELECT * FROM Employee")

def get_cards():
    return fetchall("SELECT * FROM Card")

def get_card_readings():
   return fetchall(
"""
SELECT
Employee.id, Employee.name, Terminal.name, readTime
FROM CardReading
INNER JOIN Card ON CardReading.rfid = Card.rfid
INNER JOIN Terminal ON CardReading.terminalId = Terminal.id
LEFT JOIN Employee ON Card.employeeId = Employee.id
""")

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

def delete_terminal(name):
    c.execute("DELETE FROM Terminal WHERE name=?", (name,))
    conn.commit()

def delete_employee(employee_id):
    c.execute("DELETE FROM Employee WHERE id=?", (employee_id,))
    conn.commit()
