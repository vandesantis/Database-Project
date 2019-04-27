import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "tvbase"
    )

print(mydb)

mycursor = mydb.cursor()

# DROP EACH POSSIBLE TABLE
sql = "DROP TABLE TV_Show"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE User"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE Listed_Show"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE Studio"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE Actor"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE TV_Show_Actor"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE TV_Show_Studio"
try:
    mycursor.execute(sql)

except:
    print("TABLE NOT DROPPED")
