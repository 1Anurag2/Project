from django.shortcuts import render
import mysql.connector as sql
em =''
pwd = ''

# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        obj = sql.connect(host="localhost",user = "root",password="Anurag@mysql1",database ="website")
        cur = obj.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd == value
        c="select * from information where email='{}' and password='{}'".format(em,pwd)
        cur.execute(c)
        t=tuple(cur.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')