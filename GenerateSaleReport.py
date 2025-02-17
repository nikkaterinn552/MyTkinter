import sqlite3


def generate_sales_report():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
        
    # Get sales data
    cursor.execute('''SELECT sales.id, products.name, sales.quantity, sales.total, sales.date, customers.name 
                    FROM sales
                    JOIN products ON sales.product_id = products.id
                    LEFT JOIN customers ON sales.customer_id = customers.id''')
    sales = cursor.fetchall()

    # Format the report
    report = "Sales Report\n"
    report += "ID | Product | Quantity | Total | Date | Customer\n"
    report += "-" * 60 + "\n"
    for sale in sales:
        report += f"{sale[0]} | {sale[1]} | {sale[2]} | {sale[3]:.2f} | {sale[4]} | {sale[5] if sale[5] else 'N/A'}\n"

    conn.close()
    return report

def taste_report():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT products.id, products.name, MAX(sales.quantity) AS total_amount FROM sales
                    JOIN products on sales.product_id = product_id
                    GROUP BY products.id, products.name
                    ORDER BY total_amount DESC
                    LIMIT 5''')
    
    sales = cursor.fetchall()
    report = "Popular Products\n"
    report += "ID | Product | Quantity sold\n"
    report += "-" * 30 + "\n"
    for sale in sales:
        report += f"{sale[0]} | {sale[1]} | {sale[2]}\n"
    conn.close()
    return report
