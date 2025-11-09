import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Super7898$$#"
)

# Create a cursor object
Cursor = DataBase.cursor()

# Execute command to create the database
Cursor.execute("DROP DATABASE serviceDB")

print("ServiceDB database deleted successfully")
# printing all the databases
for i in Cursor:
    print(i)

Cursor = DataBase.cursor()

# finally closing the database connection
DataBase.close()