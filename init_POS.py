import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from SetDatabase import create_db
from ProductManagement import add_product, update_product, remove_product, fetch_products, restock_products
from SaleProcessing import process_sale
from GenerateSaleReport import generate_sales_report, taste_report
from employeeManage import add_employee, update_employee, remove_employee, fetch_employee, validateLogin
from staffPos import staff_Pos

# Create the root window
def pos_System():
    root = tk.Tk()
    root.title("POS System")
    root.geometry("600x550")

    bg_image = tk.PhotoImage(file="D:\CS\Python\kinterGUI\paint.png")
    label = tk.Label(root, image=bg_image)
    label.config(width=600, height=600)
    label.place(relwidth=1, relheight=1)

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

    def add_product_gui():
        def add_product_to_db():
            name = name_entry.get()
            price = float(price_entry.get())
            stock = int(stock_entry.get())
            add_product(name, price, stock)
            messagebox.showinfo("Success", "Product added successfully!")
            add_product_window.destroy()
        
        

        add_product_window = tk.Toplevel(root)
        add_product_window.title("Add Product")

        tk.Label(add_product_window, text="Product Name:").pack()
        name_entry = tk.Entry(add_product_window)
        name_entry.pack()

        tk.Label(add_product_window, text="Price:").pack()
        price_entry = tk.Entry(add_product_window)
        price_entry.pack()

        tk.Label(add_product_window, text="Stock:").pack()
        stock_entry = tk.Entry(add_product_window)
        stock_entry.pack()

        tk.Button(add_product_window, text="Add Product", command=add_product_to_db).pack()
        
    #Update products
    def update_product_gui():
        def update_product_to_db():
            Id = int(id_entry.get())
            name = name_entry.get()
            price = float(price_entry.get())
            stock = int(stock_entry.get())
            update_product(Id, name, price, stock)
            messagebox.showinfo("Success", "Product updated successfully!")
            update_product_window.destroy()
        
        

        update_product_window = tk.Toplevel(root)
        update_product_window.title("Update Product")
        
        tk.Label(update_product_window, text="Enter product ID").pack()
        id_entry = tk.Entry(update_product_window)
        id_entry.pack()

        tk.Label(update_product_window, text="Product Name:").pack()
        name_entry = tk.Entry(update_product_window)
        name_entry.pack()

        tk.Label(update_product_window, text="Price:").pack()
        price_entry = tk.Entry(update_product_window)
        price_entry.pack()

        tk.Label(update_product_window, text="Stock:").pack()
        stock_entry = tk.Entry(update_product_window)
        stock_entry.pack()

        tk.Button(update_product_window, text="Update Product", command=update_product_to_db).pack()  

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
    
    #update stocks
    def update_stockGui():
        def update_stock_in_db():
            user_id = int(id_entry.get())
            quantity = int(quantity_entry.get())
            if not user_id or not quantity.is_integer():
                messagebox.showerror("Input Error", message="Please provide valid product name and quantity.")
            else:
                restock_products(user_id, quantity)
                messagebox.showinfo("Success", "Stock added")
                update_stock_window.destroy()
    
        update_stock_window = tk.Toplevel(root)
        update_stock_window.title("Restock")
        
        tk.Label(update_stock_window, text="Enter product ID").pack()
        id_entry = tk.Entry(update_stock_window)
        id_entry.pack()
        
        tk.Label(update_stock_window, text="Quantity to restock").pack()
        quantity_entry = tk.Entry(update_stock_window)
        quantity_entry.pack()
        
        tk.Button(update_stock_window, text="Restock", command=update_stock_in_db).pack()
    
    #remove products func

    def remove_gui():
        def remove_item():
            id_data = int(id_entry.get())
            remove_product(id_data)
            messagebox.showinfo("Success", "Product removed")
            remove_window.destroy()
        
        remove_window = tk.Toplevel(root)
        remove_window.title("Remove Product")
        tk.Label(remove_window, text="Enter product ID").pack()
        id_entry = tk.Entry(remove_window)
        id_entry.pack()
        remove = tk.Button(remove_window, text="Remove", command=remove_item)
        remove.pack()


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
    
    #displaying the most sold items
    def show_taste_report():
        report = taste_report()
        report_window = tk.Toplevel(root)
        report_window.title("Popular Products")
        report_text = tk.Text(report_window, width=80, height=20)
        report_text.pack()
        report_text.insert(tk.END, report)
        
    def add_em_gui():
        def add_em_to_db():
            name = name_entry.get()
            password = pw_entry.get()
            email = email_entry.get()
            workHour = workHour_entry.get()
            wage = int(wage_entry.get())
            add_employee(name, password, email, workHour, wage)
            messagebox.showinfo("Success", "Employee added successfully!")
            add_em_window.destroy()
            
        add_em_window = tk.Toplevel(root)
        add_em_window.title("Add Employee")

        tk.Label(add_em_window, text="Name:").pack()
        name_entry = tk.Entry(add_em_window)
        name_entry.pack()

        tk.Label(add_em_window, text="Password:").pack()
        pw_entry = tk.Entry(add_em_window)
        pw_entry.pack()

        tk.Label(add_em_window, text="Email:").pack()
        email_entry = tk.Entry(add_em_window)
        email_entry.pack()
        
        tk.Label(add_em_window, text="Work Hours:").pack()
        workHour_entry = tk.Entry(add_em_window)
        workHour_entry.pack()
        
        tk.Label(add_em_window, text="Wage:").pack()
        wage_entry = tk.Entry(add_em_window)
        wage_entry.pack()

        tk.Button(add_em_window, text="Add Employee", command=add_em_to_db).pack(pady=10)
        
    def view_employees():
        view_em_window = tk.Toplevel(root)
        view_em_window.title("Staff")
        items = fetch_employee()
        tk.Label(view_em_window, text="Staff", font="bold").grid(row=0, column= 1, columnspan=6)
        tk.Label(view_em_window, text="ID", font="bold").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(view_em_window, text="Name", font="bold").grid(row=1, column=1, padx=10, pady=5)
        tk.Label(view_em_window, text="Password", font="bold").grid(row=1, column=2, padx=10, pady=5)
        tk.Label(view_em_window, text="Email", font="bold").grid(row=1, column=3, padx=10, pady=5)
        tk.Label(view_em_window, text="Work Hours", font="bold").grid(row=1, column=4, padx=10, pady=5)
        tk.Label(view_em_window, text="Wage(per hour)", font="bold").grid(row=1, column=5, padx=10, pady=5)
        row = 2
        for item in items:
            tk.Label(view_em_window, text=f"{item[0]}").grid(row=row, column=0, padx=10, pady=5)
            tk.Label(view_em_window, text=f"{item[1]}").grid(row=row, column=1, padx=10, pady=5)
            tk.Label(view_em_window, text=f"{item[2]}").grid(row=row, column=2, padx=10, pady=5)
            tk.Label(view_em_window, text=f"{item[3]}").grid(row=row, column=3, padx=10, pady=5)
            tk.Label(view_em_window, text=f"{item[4]}").grid(row=row, column=4, padx=10, pady=5)
            tk.Label(view_em_window, text=f"{item[5]}").grid(row=row, column=5, padx=10, pady=5)
            row += 1
        
    def manage_em_gui():
        def update_staff_to_db():
            staff_id = int(id_entry.get())
            name = name_entry.get()
            pw = pw_entry.get()
            email = email_entry.get()
            workHour = workHour_entry.get()
            wage = int(wage_entry.get())
            update_employee(staff_id, name, pw, email, workHour, wage)
            messagebox.showinfo("Success", "Employee updated successfully!")
            update_em_window.destroy()
                
        update_em_window = tk.Toplevel(root)
        update_em_window.title("Update Staff Info")
        
        tk.Label(update_em_window, text="Enter employee ID").pack()
        id_entry = tk.Entry(update_em_window)
        id_entry.pack()
        
        tk.Label(update_em_window, text="Employee Name:").pack()
        name_entry = tk.Entry(update_em_window)
        name_entry.pack()

        tk.Label(update_em_window, text="Password:").pack()
        pw_entry = tk.Entry(update_em_window)
        pw_entry.pack()

        tk.Label(update_em_window, text="Email:").pack()
        email_entry = tk.Entry(update_em_window)
        email_entry.pack()
        
        tk.Label(update_em_window, text="Working hours:").pack()
        workHour_entry = tk.Entry(update_em_window)
        workHour_entry.pack()
        
        tk.Label(update_em_window, text="Wage:").pack()
        wage_entry = tk.Entry(update_em_window)
        wage_entry.pack()
        
        def remove_staff():
            id_data = int(id_entry.get())
            remove_employee(id_data)
            messagebox.showinfo("Success", "Employee dismissed")
            update_em_window.destroy()

        tk.Button(update_em_window, text="Save", command=update_staff_to_db).pack(pady=5, ipadx = 35)
        tk.Button(update_em_window, text="Dismiss Employee", command=remove_staff).pack(pady=5)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Add Product Menu
    product_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Product", menu=product_menu)
    product_menu.add_command(label="Add Product", command=add_product_gui)
    product_menu.add_command(label="View Products", command=view_product_gui)
    product_menu.add_command(label="Update Products", command=update_product_gui)
    product_menu.add_command(label="Remove Products", command=remove_gui)
    product_menu.add_command(label="Restock", command=update_stockGui)

    # Sale Menu
    sale_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Sale", menu=sale_menu)
    sale_menu.add_command(label="Process Sale", command=process_sale_gui)


    # Report Menu
    report_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Report", menu=report_menu)
    report_menu.add_command(label="Generate Sales Report", command=show_sales_report)
    report_menu.add_command(label="Taste Report", command=show_taste_report)
    
    #Employee Menu
    employee_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Employees", menu=employee_menu)
    employee_menu.add_command(label="Add employees", command=add_em_gui)
    employee_menu.add_command(label="View employees", command=view_employees)
    employee_menu.add_command(label="Manage employees", command=manage_em_gui)

    # Run the app
    root.mainloop()

def adminLogin():
        pw = "sugarrush"
        user_pw = pw_entry.get()
        if pw == user_pw:
            messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
            window.destroy()
            pos_System()
        else:
            messagebox.showerror(title="Error", message="Incorrect username or password")
            
def staffLogin():
    username = username_entry.get()
    password = pw_entry.get()
    
    if validateLogin(username, password):
        messagebox.showinfo("Login Successful", message="You successfully logged in.")
        window.destroy()
        staff_Pos()
    else:
        messagebox.showerror(title="Error", message="Incorrect username or password")

window = tk.Tk()
window.title("Login")
window.geometry("300x200")

frame = tk.LabelFrame(window, text="Login", width=300, height=150, borderwidth=3, font=("Arial", 14, 'bold'))
frame.pack()

tk.Label(frame, text="Username", font=(14)).grid(row=0, column=0)
tk.Label(frame, text="Password", font=(14)).grid(row=1, column=0)

username_entry = tk.Entry(frame, font=(14))
username_entry.grid(row=0, column=1)

pw_entry = tk.Entry(frame, show="*",font=(14))
pw_entry.grid(row=1, column=1)

login_label = tk.Label(frame, text="Log in as:", font=(14))
login_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


admin_btn = tk.Button(frame, text="Admin", font=(14), command= adminLogin)
admin_btn.grid(row=3, column=0, pady=10, ipadx=10)

staff_btn = tk.Button(frame, text="Staff", font=(14), command=staffLogin)
staff_btn.grid(row=3, column=1, pady=10, ipadx=20)
        
window.mainloop()
