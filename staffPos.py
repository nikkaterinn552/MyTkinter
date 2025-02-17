import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from SetDatabase import create_db
from ProductManagement import add_product, update_product, remove_product, fetch_products
from SaleProcessing import process_sale
from GenerateSaleReport import generate_sales_report


# Create the root window
def staff_Pos():
    root = tk.Tk()
    root.title("POS System")
    root.geometry("600x550")

    bg_image = tk.PhotoImage(file="D:\CS\Python\kinterGUI\paint.png")
    label = tk.Label(root, image=bg_image)
    label.config(width=600, height=600)
    label.pack()

    #database creation
    create_db()
    def create_connection():
        connection = None
        try:
            connection = sqlite3.connect("pos_system.db")
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection

    #access level


    # Product Management

    
        

    #view products
    connection = create_connection()
    def view_product_gui():
        def view_products(connection):
            try:
                cursor = connection.cursor()
                
                product_info = "SELECT * FROM products"
                cursor.execute(product_info)
                products = cursor.fetchall()
                
                connection.commit()
                return products
            except sqlite3.Error as e:
                print(f"Error '{e}' occurred")
                messagebox.showerror("Error", f"An error occurred: {e}")
                return []
            
        
        
        view_product_window = tk.Toplevel(root)
        view_product_window.title("View Product")
        
        
        items = view_products(connection)
        tk.Label(view_product_window, text="Products").grid(row=0, column= 1, columnspan=4)
        tk.Label(view_product_window, text="ID", font="bold").grid(row=1, column=1, padx=10, pady=5)
        tk.Label(view_product_window, text="Product", font="bold").grid(row=1, column=2, padx=10, pady=5)
        tk.Label(view_product_window, text="Price", font="bold").grid(row=1, column=3, padx=10, pady=5)
        tk.Label(view_product_window, text="Stock", font="bold").grid(row=1, column=4, padx=10, pady=5)
        row = 2
        for item in items:
            tk.Label(view_product_window, text=f"{item[0]}").grid(row=row, column=1, padx=10, pady=5)
            tk.Label(view_product_window, text=f"{item[1]}").grid(row=row, column=2, padx=10, pady=5)
            tk.Label(view_product_window, text=f"{item[2]}").grid(row=row, column=3, padx=10, pady=5)
            tk.Label(view_product_window, text=f"{item[3]}").grid(row=row, column=4, padx=10, pady=5)
            row += 1
        
    


    # Sales Processing
    def process_sale_gui():
        def process_sale_button():
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            customer_id = int(customer_id_entry.get()) if customer_id_entry.get() else None
            result = process_sale(product_id, quantity, customer_id)
            messagebox.showinfo("Sale", result)

        sale_window = tk.Toplevel(root)
        sale_window.title("Process Sale")

        tk.Label(sale_window, text="Product ID:").pack()
        product_id_entry = tk.Entry(sale_window)
        product_id_entry.pack()

        tk.Label(sale_window, text="Quantity:").pack()
        quantity_entry = tk.Entry(sale_window)
        quantity_entry.pack()

        tk.Label(sale_window, text="Customer ID (optional):").pack()
        customer_id_entry = tk.Entry(sale_window)
        customer_id_entry.pack()

        tk.Button(sale_window, text="Process Sale", command=process_sale_button).pack()

    # Report Generation
    def show_sales_report():
        report = generate_sales_report()
        report_window = tk.Toplevel(root)
        report_window.title("Sales Report")
        report_text = tk.Text(report_window, width=80, height=20)
        report_text.pack()
        report_text.insert(tk.END, report)



    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Add Product Menu
    product_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Product", menu=product_menu)
    product_menu.add_command(label="View Products", command=view_product_gui)

    # Sale Menu
    sale_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Sale", menu=sale_menu)
    sale_menu.add_command(label="Process Sale", command=process_sale_gui)


    # Report Menu
    report_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Report", menu=report_menu)
    report_menu.add_command(label="Generate Sales Report", command=show_sales_report)

    # Run the app
    root.mainloop()
