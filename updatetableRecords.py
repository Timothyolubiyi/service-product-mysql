import mysql.connector

# connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

def selectrecords():
    cursorObject = dataBase.cursor()
    # correct SQL syntax and parameter style
    sql = "SELECT * FROM tbl_service"
    # must be a tuple

    cursorObject.execute(sql)
    # printing all the recoords
   

    #  commit the change to actually save it
    #dataBase.commit()
    for i in cursorObject:
       print(i)
       
       #print(sql)
        #print("Records retrieved from tbl_service successfully")

        # close the connection
        # prepare a cursor object
def updatetables():
    cursorObject = dataBase.cursor()

    records = "UPDATE tbl_service SET Services = 'entry-level training' WHERE Id = 10"
    
    cursorObject.execute(records)
    
    dataBase.commit()
    
    print("Data updated in tbl_service successfully")

selectrecords()
updatetables()


dataBase.close()








