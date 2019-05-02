from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from django.template import loader
from django.db import connection

# Create your views here.

def index(request):
        
    dbconn = connection.cursor()
    
    template = loader.get_template("login.html")
    template_add = loader.get_template("add.html")

    context ={}

    name = ""
    password = ""
    
    if request.method == 'POST':
        table = request.POST.get('table')
        
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        if name == "DyVa" and password == "root":
            return HttpResponse(template_add.render(context,request))
        # Add Show To Table
        elif table == 'Show':
            print("SHOW")
            name = request.POST.get('name')
            genre = request.POST.get('genre')
            seasons = int(request.POST.get('seasons'))
            synopsis = request.POST.get('sysnopsis')
            fcc = request.POST.get('fcc')

            
            #Insertion SQL
            sql = """
            INSERT INTO TV_Show (Name, Genre, Seasons, Synopsis, FCC)
            VALUES ('%s', '%s', '%d', '%s', '%s')
            """
            try:
                dbconn.execute(sql % (name,genre,seasons,synopsis,fcc))
            except:
                pass

            
        # Add Studio To Table
        elif table == 'Studio':
            print("STUDIO")
            name = request.POST.get('name')
            location = request.POST.get('location')
            show = request.POST.get('show')

            sql = """
            SELECT * FROM TV_Show_Studio WHERE Show_Name = '%s'
            """
            try:
                dbconn.execute(sql %(show))
            except:
                pass

            table = list(dbconn)
            if len(table) > 0:
                print("DUPLICATE")
                print(table)
                return HttpResponse(template.render({},request))

            #Insertion SQL
            sql = """
            INSERT INTO Studio (Name, Location)
            VALUES ('%s', '%s')
            """
            try:
                dbconn.execute(sql % (name,location))
            except:
                pass

            #Foreign Key Handling
            studioID = len(table)+1
            sql = """
            INSERT INTO TV_Show_Studio (Show_Name, Studio_ID)
            VALUES ('%s', '%d')
            """
            try:
                dbconn.execute(sql % (name,studioID))
            except:
                pass

        # Add Actor To Table
        elif table == 'Actor':
            print("Actor")
            name = request.POST.get('name')
            age = int(request.POST.get('age'))
            show = request.POST.get('show')

            sql = """
            SELECT * FROM Actor
            """
            try:
                dbconn.execute(sql)
            except:
                pass

            table = list(dbconn)
            print(table)

            #Insertion SQL
            sql = """
            INSERT INTO Actor (Name, Age)
            VALUES ('%s', '%d')
            """
            try:
                dbconn.execute(sql % (name,age))
            except:
                pass

            #Foreign Key Handling
            actorID = len(table)+1
            sql = """
            INSERT INTO TV_Show_Actor (Show_Name, Actor_ID)
            VALUES ('%s', '%d')
            """
            try:
                dbconn.execute(sql % (show,actorID))
            except Exception as e:
                print(e)
                pass

   
    return HttpResponse(template.render(context,request))
