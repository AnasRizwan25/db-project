import tkinter as tk
from gui.login_register import open_login_window
from gui.utils import center_window, style_button

def open_main_menu():
    win = tk.Tk()
    win.title("Course Registration System")
    center_window(win, 400, 300)
    win.configure(bg="#f0f4f7")

    header = tk.Label(win, text="Select User Type", font=("Segoe UI", 14, "bold"), bg="#f0f4f7")
    header.pack(pady=20)

    btn_admin = tk.Button(win, text="Admin", width=20, command=lambda: open_login_window("admin"))
    style_button(btn_admin)
    btn_admin.pack(pady=10)

    btn_student = tk.Button(win, text="Student", width=20, command=lambda: open_login_window("student"))
    style_button(btn_student)
    btn_student.pack(pady=10)

    win.mainloop()

if __name__ == "__main__":
    open_main_menu()
