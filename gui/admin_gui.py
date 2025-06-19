import tkinter as tk
from tkinter import messagebox
from db.queries import add_course, get_course_enrollments
from gui.utils import center_window, style_button, style_label

def open_admin_dashboard():
    win = tk.Tk()
    win.title("Admin Dashboard")
    center_window(win, 500, 400)
    win.configure(bg="#f0f4f7")

    tk.Label(win, text="Admin Panel", font=("Segoe UI", 14, "bold"), bg="#f0f4f7").pack(pady=10)

    frame = tk.Frame(win, bg="#f0f4f7")
    frame.pack()

    lbl1 = tk.Label(frame, text="Course Name:")
    style_label(lbl1)
    lbl1.grid(row=0, column=0, sticky="e")
    course_name = tk.Entry(frame, width=40)
    course_name.grid(row=0, column=1, pady=5)

    lbl2 = tk.Label(frame, text="Instructor:")
    style_label(lbl2)
    lbl2.grid(row=1, column=0, sticky="e")
    instructor = tk.Entry(frame, width=40)
    instructor.grid(row=1, column=1, pady=5)

    lbl3 = tk.Label(frame, text="Capacity:")
    style_label(lbl3)
    lbl3.grid(row=2, column=0, sticky="e")
    capacity = tk.Entry(frame, width=40)
    capacity.grid(row=2, column=1, pady=5)

    def submit():
        try:
            add_course(course_name.get(), instructor.get(), int(capacity.get()))
            messagebox.showinfo("Success", "Course added!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_enrollments():
        stats = get_course_enrollments()
        result = "\n".join([f"{name}: {count} students" for name, count in stats])
        messagebox.showinfo("Enrollments", result)

    btn_add = tk.Button(win, text="Add Course", command=submit)
    style_button(btn_add)
    btn_add.pack(pady=10)

    btn_view = tk.Button(win, text="View Enrollments", command=view_enrollments)
    style_button(btn_view)
    btn_view.pack()

    win.mainloop()
