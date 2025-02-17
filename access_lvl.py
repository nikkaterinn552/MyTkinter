import tkinter as tk
from tkinter import messagebox, ttk
from SetDatabase import create_db
import sqlite3

create_db()
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("pos_system.db")
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return connection


def front():
    window = tk.Tk()
    window.title("Login")
    window.geometry("300x200")
    
    frame = tk.LabelFrame(window, text="Login", width=300, height=150, borderwidth=3, font=("Arial", 14, 'bold'))
    frame.pack()
    
    tk.Label(frame, text="Username", font=(14)).grid(row=0, column=0)
    tk.Label(frame, text="Password", font=(14)).grid(row=1, column=0)
    
    username_entry = tk.Entry(frame, font=(14))
    username_entry.grid(row=0, column=1)
    
    global pw_entry
    pw_entry = tk.Entry(frame, show="*",font=(14))
    pw_entry.grid(row=1, column=1)
    
    login_label = tk.Label(frame, text="Log in as:", font=(14))
    login_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    
    admin_btn = tk.Button(frame, text="Admin", font=(14), command= adminLogin)
    admin_btn.grid(row=3, column=0, pady=10, ipadx=10)
    
    staff_btn = tk.Button(frame, text="Staff", font=(14))
    staff_btn.grid(row=3, column=1, pady=10, ipadx=20)
            
    window.mainloop()
    
    def adminLogin():
        pw = "sugarrush"
        user_pw = pw_entry.get()
        if pw == user_pw:
            messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
            access = True
            return access
            window.destroy()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
            access = False
            return access

front()
