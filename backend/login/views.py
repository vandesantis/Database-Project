from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from django.template import loader
from django.db import connection

def logindex(request):

    dbconn = connection.cursor()
    
    template = loader.get_template("mainlogin.html")
    usertemplate = loader.get_template("userdisplay.html")
    context ={}

    name = ""
    email = ""
    password = ""
    
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        search = request.POST.get('search')
        sql = """
        SELECT * FROM Listed_Show WHERE Name = '%s'
        """
        
        sqlAll = """
        SELECT * FROM TV_Show WHERE Name = '%s'
        """
        try:
            dbconn.execute(sql % (search))
            table = list(dbconn)
            
            if len(table) == 0:
                dbconn.execute(sqlAll % (search))
                table = list(dbconn)
                
            print(table)
            context = {'table':table, 'name':name}
            return HttpResponse(usertemplate.render(context,request))
        except Exception as e:
            return HttpResponse(usertemplate.render(context,request))
            pass
        
        sql = """
        SELECT * FROM User WHERE email='%s' and name='%s' and password='%s'
        """
        try:
            dbconn.execute(sql % (email,name,password))
            table = list(dbconn)
            print(table)
            context = {'table':table , 'name':name}
            return HttpResponse(usertemplate.render(context,request))
        except:
            print("Nonexistant")

            
        #Insertion SQL If Login Fails
        sql = """
        INSERT INTO User (Email, Name, Password)
        VALUES ('%s', '%s', '%s')
        """
        try:
            dbconn.execute(sql % (email,name,password))
        except:
            pass


   
    return HttpResponse(template.render(context,request))
