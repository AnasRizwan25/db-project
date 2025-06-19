import tkinter as tk
from tkinter import messagebox
from db.queries import register_student, login_student
from gui.student_gui import open_student_dashboard
from gui.admin_gui import open_admin_dashboard
from gui.utils import center_window, style_button, style_label

def open_login_window(user_type):
    def login():
        user = login_student(email.get(), password.get())
        if user:
            if user_type == "admin":
                if email.get() == "admin@admin.com":
                    open_admin_dashboard()
                else:
                    messagebox.showerror("Error", "Only admin@admin.com allowed")
            else:
                open_student_dashboard(user[0], user[1])
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register():
        try:
            register_student(name.get(), email.get(), password.get())
            messagebox.showinfo("Success", "Registered successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    win = tk.Tk()
    win.title(f"{user_type.capitalize()} Login")
    center_window(win, 400, 300)
    win.configure(bg="#f0f4f7")

    header = tk.Label(win, text=f"{user_type.capitalize()} Login", font=("Segoe UI", 14, "bold"), bg="#f0f4f7")
    header.grid(row=0, column=0, columnspan=2, pady=10)

    if user_type == "student":
        lbl_name = tk.Label(win, text="Name:")
        style_label(lbl_name)
        lbl_name.grid(row=1, column=0)
        name = tk.Entry(win, width=30)
        name.grid(row=1, column=1, padx=5, pady=5)
    else:
        name = tk.Entry(win)

    lbl_email = tk.Label(win, text="Email:")
    style_label(lbl_email)
    lbl_email.grid(row=2, column=0)
    email = tk.Entry(win, width=30)
    email.grid(row=2, column=1, padx=5, pady=5)

    lbl_pass = tk.Label(win, text="Password:")
    style_label(lbl_pass)
    lbl_pass.grid(row=3, column=0)
    password = tk.Entry(win, show="*", width=30)
    password.grid(row=3, column=1, padx=5, pady=5)

    btn_login = tk.Button(win, text="Login", command=login)
    style_button(btn_login)
    btn_login.grid(row=4, column=0, pady=10)

    if user_type == "student":
        btn_register = tk.Button(win, text="Register", command=register)
        style_button(btn_register)
        btn_register.grid(row=4, column=1, pady=10)

    win.mainloop()
