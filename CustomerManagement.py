import sqlite3

def add_customer(name, phone):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()

def fetch_customers():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return customers
