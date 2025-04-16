import pyodbc

def get_db_connection():
    server = 'DESKTOP-9IBBKL9\\SQLEXPRESS'
    database = 'order_management'
    driver = '{SQL Server}'

    conn = pyodbc.connect(
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        'Trusted_Connection=yes;'
    )
    return conn
