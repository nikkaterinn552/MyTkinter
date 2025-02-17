import sqlite3

def create_db():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()

    # Create products, customers, and sales tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price REAL,
                        stock INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        phone TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                        id INTEGER PRIMARY KEY,
                        product_id INTEGER,
                        quantity INTEGER,
                        total REAL,
                        date TEXT,
                        customer_id INTEGER,
                        FOREIGN KEY (product_id) REFERENCES products(id),
                        FOREIGN KEY (customer_id) REFERENCES customers(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS staffs (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        password TEXT,
                        email TEXT,
                        workingHour TEXT,
                        wage INTEGER)''')
    
    '''cursor.execute("PRAGMA table_info(staffs);")
    columns = cursor.fetchall()
    for column in columns:
        print(column)'''        #checking columns in staffs table
    
    '''cursor.execute("""CREATE TABLE IF NOT EXISTS sold_products (
                    id INTEGER PRIMARY KEY
                    product_id)""")'''
    
    conn.commit()
    conn.close()

# Create the database when the program starts
create_db()

