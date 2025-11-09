import mysql.connector as SQLC

# Connect to MySQL
DataBase = SQLC.connect(
  host="localhost",
  user="root",
  password="Super7898$$#",
  database = "serviceDB"
)
def showtables():
  
  Cursor = DataBase.cursor()
  Cursor.execute("SHOW TABLES")
  for i in Cursor:
    if len(i)>0:
      
      print(i)
    else:
      print("no tables to display")   
# Create a cursor object
Cursor = DataBase.cursor()

# Execute command to create the database
Cursor.execute("DROP TABLE IF EXISTS shift")

print("table shift dropped successfully")
# printing all the tables
showtables()

# finally closing the database connection
DataBase.close()