from django.shortcuts import render
import mysql.connector as sql
fn = ''
ln = ''
s = ''
em =''
pwd = ''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        obj = sql.connect(host="localhost",user = "root",password="Anurag@mysql1",database ="website")
        cur = obj.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln == value
            if key == "sex":
                s == value
            if key == "email":
                em = value
            if key == "password":
                pwd == value
        c = "insert into information Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cur.execute(c)
        obj.commit()
    return render(request,'signup_page.html')
