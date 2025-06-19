def center_window(win, width=400, height=300):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")

def style_button(btn):
    btn.configure(bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), bd=0, padx=10, pady=5, activebackground="#005f99")

def style_label(lbl):
    lbl.configure(bg="#f0f4f7", font=("Segoe UI", 10))
