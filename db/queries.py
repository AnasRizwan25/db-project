from .connection import get_connection


def register_student(name, email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, email, password) VALUES (:1, :2, :3)", (name, email, password))
    conn.commit()
    cur.close()
    conn.close()

def login_student(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE email=:1 AND password=:2", (email, password))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def get_all_courses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    courses = cur.fetchall()
    cur.close()
    conn.close()
    return courses

def register_course(student_id, course_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO registrations (student_id, course_id) VALUES (:1, :2)", (student_id, course_id))
    conn.commit()
    cur.close()
    conn.close()

def get_student_courses(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT c.course_name FROM courses c JOIN registrations r ON c.course_id = r.course_id WHERE r.student_id = :1", (student_id,))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def add_course(course_name, instructor, capacity):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (course_name, instructor, capacity) VALUES (:1, :2, :3)", (course_name, instructor, capacity))
    conn.commit()
    cur.close()
    conn.close()

def get_course_enrollments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT c.course_name, COUNT(r.student_id) FROM courses c LEFT JOIN registrations r ON c.course_id = r.course_id GROUP BY c.course_name")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
