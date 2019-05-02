from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from django.template import loader
from django.db import connection

# Create your views here.

def index(request):
        
    dbconn = connection.cursor()

    template = loader.get_template("display.html")
    
    #Create Any Tables Needed
    ##############
    ###TV SHOWS###
    ##############
    try:
        # TV Show Table
        dbconn.execute("""
        CREATE TABLE TV_Show (
        Name varchar(255),
        Genre varchar(255),
        Rating int,
        Seasons int,
        Synopsis varchar(255),
        FCC varchar(255),
        Watching_Status bit,
        PRIMARY KEY(Name)
        )""")
        
    except:
        pass

    ###########
    ###USERS###
    ###########
    try:
        # User Table
        dbconn.execute("""
        CREATE TABLE User (
        Email varchar(255),
        Name varchar(255),
        Password varchar(255),
        Favorite_Show varchar(255),
        PRIMARY KEY(Email)
        )""")
        
    except:
        pass

    #################
    ###LISTED SHOW###
    #################
    try:
        # Listed Table
        dbconn.execute("""
        CREATE TABLE Listed_Show (
        Email varchar(255),
        Name varchar(255),
        Rating int,
        Genre varchar(255),
        Seasons int,
        Synopsis varchar(255),
        FCC varchar(255),
        FOREIGN KEY(Email) REFERENCES User(Email)
        )""")

    except:
        pass

    ############
    ###STUDIO###
    ############
    try:
        # Studio Table
        dbconn.execute("""
        CREATE TABLE Studio (
        ID integer PRIMARY KEY,
        Name varchar(255),
        Location varchar(255)
        )""")
          
    except Exception as e:
        print(e)

    ###########
    ###ACTOR###
    ###########
    try:
        # Actor Table
        dbconn.execute("""
        CREATE TABLE Actor (
        ID integer PRIMARY KEY,
        Name varchar(255),
        Age int
        )""")
            
    except:
        pass

    ###################
    ###TV SHOW ACTOR###
    ###################
    try:
        # TV Show Actor Table
        dbconn.execute("""
        CREATE TABLE TV_Show_Actor (
        Show_Name varchar(255),
        Actor_ID integer,
        FOREIGN KEY(Show_Name) REFERENCES TV_Show(Name),
        FOREIGN KEY(Actor_ID) REFERENCES Actor(ID)
        )""")
           
    except:
        pass

    ####################
    ###TV SHOW STUDIO###
    ####################
    try:
        # TV Show Actor Table
        dbconn.execute("""
        CREATE TABLE TV_Show_Studio (
        Show_Name varchar(255),
        Studio_ID integer,
        FOREIGN KEY(Show_Name) REFERENCES TV_Show(Name),
        FOREIGN KEY(Studio_ID) REFERENCES Studio(ID)
        )""")
           
    except:
        pass



    #DISPLAYING TV SHOWS


    # Reading Show Table
    sql = """SELECT name FROM sqlite_master WHERE type='table';"""

    sql = """SELECT * FROM TV_Show
    """
    dbconn.execute(sql)
    badtable = list(dbconn)
    table = []
    for x in badtable:
        try:
            table.append(list(filter(None, x)))
        except:
            pass
    context ={'table': table}

    return HttpResponse(template.render(context,request))

def detail(request, show_name):
    dbconn = connection.cursor()
    sql = """SELECT * FROM TV_Show WHERE name='%s'
    """
    dbconn.execute(sql %(show_name))
    table = list(dbconn)

    html = "<h1>" + str(table[0][0]) + "</h1>"
    html += "\n"
    html += "<p>" + str(table[0][4]) + "</p>"
    return HttpResponse(html)
