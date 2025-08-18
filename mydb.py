
import mysql.connector

#Connect to database 

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'Roblox108.'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a  databse 
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
