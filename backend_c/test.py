import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rootroot',
    database='expense_manager'
)
print("Connected successfully")
conn.close()