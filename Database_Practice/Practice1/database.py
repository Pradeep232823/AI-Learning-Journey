import sqlite3

def db_connect(db_name):
    connection = sqlite3.connect(db_name)
    print(f"{db_name} Database connected successfully")
    return connection