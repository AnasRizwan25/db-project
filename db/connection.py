import cx_Oracle

def get_connection():
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
    conn = cx_Oracle.connect(user="taha", password="123", dsn=dsn)
    return conn