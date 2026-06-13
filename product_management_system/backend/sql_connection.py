import mysql.connector
import os

def get_sql_connection():
    print("Opening mysql connection")

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "product_db")
    )

    return connection