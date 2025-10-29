import mysql.connector
try:
    mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "G7v!rX9#pL2@qT5z",
        database = "alx_book_store",
    )
    print("Database 'alx_book_store' created successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")





