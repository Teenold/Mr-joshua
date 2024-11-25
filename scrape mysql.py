import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password = "190000",
    database = "mybasedata"
)
mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE mybasedata")
mycursor.execute("CREATE TABLE Staff (staffID int PRIMARY KEY AUTO_INCREMENT,name varchar(50), age smallint unsigned)")
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)

