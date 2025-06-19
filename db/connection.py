import cx_Oracle

def get_connection():
    dsn = cx_Oracle.makedsn("localhost", "--", service_name="--")
    conn = cx_Oracle.connect(user="--", password="--", dsn=dsn)
    return conn