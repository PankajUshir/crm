import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Techladd@123'
)

#prepare a cursor Object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE crmdatabase")

print("Database Done !!")