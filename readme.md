# 📚 Course Registration System (Python + Oracle + Tkinter GUI)

A modern university course registration system with a beautiful GUI built using **Python**, **Oracle 11g** and library for Tkinter.

---

## 🖼️ Features

- 🧑‍🎓 Student registration & login  
- 🧑‍💼 Admin login  
- 📋 Add & view courses (Admin)  
- 📝 Enroll in courses (Students — max 5)  
- 📊 View registered courses  

---

## 🏗️ Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| GUI Frontend | Python `Tkinter`    |
| Backend      | Python                   |
| Database     | Oracle 11g               |

---

## 📁 Project Structure
```bash
course_registration_system/
├── db/
│ ├── connection.py # Oracle DB connection
│ └── queries.py # All database queries
├── gui/
│ ├── login_register.py # Login & register interface
│ ├── student_gui.py # Student dashboard
│ ├── admin_gui.py # Admin dashboard
│ └── utils.py # UI helpers (e.g., center_window)
├── main.py # App launcher
├── README.md
└── requirements.txt
```


---

## 💾 Requirements

- Python 3.8+
- Oracle 11g or Oracle XE
- [cx_Oracle](https://pypi.org/project/cx_Oracle/)
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)

---

## 📦 Installation

Install the required Python libraries:

```bash
pip install cx_Oracle ttkbootstrap
⚙️ Oracle Table Setup
Run these SQL commands in Oracle SQL Developer or SQL*Plus:

students 
courses
registrations 


▶️ Running the Application

python main.py