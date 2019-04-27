import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "tvbase"
    )

print(mydb)

mycursor = mydb.cursor()

##############
###TV SHOWS###
##############
try:
    # TV Show Table
    mycursor.execute("""
    CREATE TABLE TV_Show (
    Name varchar(255),
    Genre varchar(255),
    Rating int,
    Seasons int,
    Synopsis varchar(255),
    FCC varchar(255),
    Watching_Status bit,
    PRIMARY KEY (Name)
    )""")
    
except:
    print("TABLE ALREADY EXISTS")

###########
###USERS###
###########
try:
    # User Table
    mycursor.execute("""
    CREATE TABLE User (
    Email varchar(255),
    Name varchar(255),
    Password varchar(255),
    Favorite_Show varchar(255),
    PRIMARY KEY (Email)
    )""")
    
except:
    print("TABLE ALREADY EXISTS")

#################
###LISTED SHOW###
#################
try:
    # Listed Table
    mycursor.execute("""
    CREATE TABLE Listed_Show (
    Email varchar(255),
    Name varchar(255),
    Rating varchar(255),
    Genre varchar(255),
    Rating int,
    Seasons int,
    Synopsis varchar(255),
    FCC varchar(255)
    FOREIGN KEY (Email) REFERNCES User(Email)
    )""")

except:
    print("TABLE ALREADY EXISTS")

############
###STUDIO###
############
try:
    # Studio Table
    mycursor.execute("""
    CREATE TABLE Studio (
    ID int AUTO_INCREMENT,
    Name varchar(255),
    Location varchar(255),
    PRIMARY KEY (ID)
    )""")
      
except:
    print("TABLE ALREADY EXISTS")

###########
###ACTOR###
###########
try:
    # Actor Table
    mycursor.execute("""
    CREATE TABLE Actor (
    ID int AUTO_INCREMENT,
    Name varchar(255),
    Age int,
    PRIMARY KEY (ID)
    )""")
        
except:
    print("TABLE ALREADY EXISTS")

###################
###TV SHOW ACTOR###
###################
try:
    # TV Show Actor Table
    mycursor.execute("""
    CREATE TABLE TV_Show_Actor (
    Show_Name varchar(255),
    Actor_ID varchar(255),
    FOREIGN KEY (Show_Name) REFERENCES TV_Show(Name),
    FOREIGN KEY (Actor_ID) REFERENCES Actor(ID)
    )""")
       
except:
    print("TABLE ALREADY EXISTS")

####################
###TV SHOW STUDIO###
####################
try:
    # TV Show Actor Table
    mycursor.execute("""
    CREATE TABLE TV_Show_Studio (
    Show_Name varchar(255),
    Studio_ID varchar(255),
    FOREIGN KEY (Show_Name) REFERENCES TV_Show(Name),
    FOREIGN KEY (Studio_ID) REFERENCES Studio(ID)
    )""")
       
except:
    print("TABLE ALREADY EXISTS")
    
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
