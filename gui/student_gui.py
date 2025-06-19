import tkinter as tk
from tkinter import messagebox
from db.queries import get_all_courses, register_course, get_student_courses
from gui.utils import center_window, style_button

def open_student_dashboard(student_id, student_name):
    win = tk.Tk()
    win.title(f"Student Dashboard - {student_name}")
    center_window(win, 600, 500)
    win.configure(bg="#f0f4f7")

    tk.Label(win, text=f"Welcome {student_name}!", font=("Segoe UI", 14, "bold"), bg="#f0f4f7").pack(pady=10)

    def load_courses():
        for widget in course_frame.winfo_children():
            widget.destroy()
        courses = get_all_courses()
        for course in courses:
            cid, cname, instructor, capacity = course
            frame = tk.Frame(course_frame, bg="#ffffff", bd=1, relief="solid")
            frame.pack(fill="x", padx=10, pady=5)
            tk.Label(frame, text=f"{cname} by {instructor} (Cap: {capacity})", bg="#ffffff").pack(side="left", padx=5)
            btn = tk.Button(frame, text="Register", command=lambda cid=cid: handle_register(cid))
            style_button(btn)
            btn.pack(side="right", padx=10)

    def handle_register(course_id):
        try:
            register_course(student_id, course_id)
            messagebox.showinfo("Success", "Course registered!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_registered():
        courses = get_student_courses(student_id)
        msg = "\n".join([c[0] for c in courses]) or "No courses registered"
        messagebox.showinfo("Registered Courses", msg)

    btn_refresh = tk.Button(win, text="Refresh Courses", command=load_courses)
    style_button(btn_refresh)
    btn_refresh.pack(pady=5)

    btn_view = tk.Button(win, text="View Registered Courses", command=show_registered)
    style_button(btn_view)
    btn_view.pack(pady=5)

    course_frame = tk.Frame(win, bg="#f0f4f7")
    course_frame.pack(fill="both", expand=True, padx=10)

    load_courses()
    win.mainloop()
