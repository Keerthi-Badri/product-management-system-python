import mysql.connector

def get_sql_connection():
    print("Opening mysql connection")

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Hanuma@18',
        database='product_db'
    )

    return connection