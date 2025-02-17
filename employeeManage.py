import sqlite3

def add_employee(name, password, email, workingHour, wage):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO staffs (name, password, email, workingHour, wage) VALUES (?, ?, ?, ?, ?)", (name, password, email, workingHour, wage))
    conn.commit()
    conn.close()
    
def update_employee(name, password, email, workingHour, wage):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE staffs SET name = ?, password = ?, email = ? , workingHour = ?, wage = ? WHERE id = ?", (name, password, email, workingHour, wage, id))
    conn.commit()
    conn.close()
    
def remove_employee(id):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM staffs WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
def fetch_employee():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staffs")
    employees = cursor.fetchall()
    conn.close()
    return employees

def validateLogin(name, password):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staffs WHERE name = ? AND password =?", (name, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

    