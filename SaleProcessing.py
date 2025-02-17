import sqlite3
from datetime import datetime

def process_sale(product_id, quantity, customer_id=None):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()

    # Check stock and price of the product
    cursor.execute("SELECT price, stock FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    if product and product[1] >= quantity:
        total = product[0] * quantity
        new_stock = product[1] - quantity
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))

        # Insert sale into sales table
        cursor.execute("INSERT INTO sales (product_id, quantity, total, date, customer_id) VALUES (?, ?, ?, ?, ?)",
                        (product_id, quantity, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), customer_id))
        
        conn.commit()
        conn.close()
        return f"Sale successful! Total: ${total:.2f}"
    else:
        conn.close()
        return "Error: Not enough stock or product does not exist."
