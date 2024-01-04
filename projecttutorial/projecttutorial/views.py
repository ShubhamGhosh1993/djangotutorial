from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def homepage(req):
    # passing the data mustbe json format of dict
    data={
        "title": "Django tutorials",
        "username": "Django User",
        "clist":["PHP", "JAVA", "Python", "Django"],
        "studentlist":[
            {"name":"Shubham", "phone":"98956565654"},
            {"name":"Sayan", "phone":"89656474974"}]
    }
    return render(req,'index.html',data)

def aboutus(req):
    return HttpResponse("Welcome to django!")

def course(req):
    return HttpResponse("Welcome to Course!")

def dynamicroute1(req, id):
    return HttpResponse(f"Welcome to dynamicroute1! id = {id}")

def dynamicroute2(req, string):
    return HttpResponse(f"Welcome to dynamicroute2! Msg = {string}")

def dynamicroute3(req, data):
    return HttpResponse(f"Welcome to dynamicroute3! Data = {data}")

def userform(req):
    return render(req, 'form.html')

def getdata(req):
    try:
        email=req.GET['email']
        name=req.GET['name']
        print(f"Name : {name}, Email: {email}")
        email2=req.GET.get('email')
        name2=req.GET.get('name')
        
        print(f" {email2} {name2}")
        
        return render(req, 'form.html')

    except:
        return HttpResponse("Something went wrong")
    
def postdata(req):
    try:
        email=req.POST['email']
        name=req.POST['name']
        print(f"Name : {name}, Email: {email}")
        
        email2=req.POST.get('email')
        name2=req.POST.get('name')
        
        print(f" {email2} {name2}")
        
        return render(req, 'form.html')

    except:
        return HttpResponse("Something went wrong")