import sqlite3

dbconn = sqlite3.connect("tvbase.db")

# DROP EACH POSSIBLE TABLE
sql = "DROP TABLE TV_Show"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE User"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE Listed_Show"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE Studio"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE Actor"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE TV_Show_Actor"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
    
sql = "DROP TABLE TV_Show_Studio"
try:
    dbconn.execute(sql)

except:
    print("TABLE NOT DROPPED")
