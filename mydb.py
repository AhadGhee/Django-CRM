# Import the MySQL Connector module 
# (this lets Python talk to your MySQL server)
import mysql.connector

# Connect to the MySQL server
# host     = where the server is running ('localhost' means your own PC)
# user     = the MySQL username you want to log in with
# passwd   = the password for that user
# NOTE: At this point you are connecting to the server itself, 
#       not to a specific database yet.
dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'Roblox108.'
)

# Prepare a cursor object
# A cursor is like a control structure used to run SQL commands 
# through the Python connection.
cursorObject = dataBase.cursor()

# Execute an SQL command to create a new database named "elderco"
# If the database already exists, this will throw an error.
# To be safe, you could use:
# cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")
cursorObject.execute("CREATE DATABASE elderco")

# Print confirmation that everything ran successfully
print("All Done!")