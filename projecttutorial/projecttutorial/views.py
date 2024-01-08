from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from services.models import Services

from .forms import UserForm


def homepage(req):
    #service models data
    servicesData = Services.objects.all().order_by("-service_title")[1:2]
    #use - sign in front columns name to ascending or descendending order
    
    # passing the data mustbe json format of dict
    data={
        "title": "Django tutorials",
        "username": "Django User",
        "clist":["PHP", "JAVA", "Python", "Django"],
        "studentlist":[
            {"name":"Shubham", "phone":"98956565654"},
            {"name":"Sayan", "phone":"89656474974"}],
        "services": servicesData
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

def djangoform(req):
    fm = UserForm()
    return render(req, 'form.html', {"form": fm})

def simpleCalculator(req):
    data ={}
    try:
        if req.method == "POST":
            n1=int(req.POST["num1"])
            n2=int(req.POST["num2"])
            opr = req.POST["operator"]
            output=0
            print(n1 , opr, n2)
            if opr == "+":
                output = n1+n2
            elif opr == "-":
                output = n1-n2
            elif opr == "x":
                output = n1*n2
            elif opr == "/":
                output = n1/n2
            else:
                print("Wrong operator!")
                pass
            data={
                "num1":n1,
                "num2":n2,
                "output":output
            }
        pass
    except:
        print("Something Went Wrong!")
        pass
    
    
    return render(req, 'calculator.html', data)

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
    
def marksheet(req):
    data ={}
    try:
        if req.method == "POST":
            s1=int(req.POST["s1"])
            s2=int(req.POST["s2"])
            s3=int(req.POST["s3"])
            s4=int(req.POST["s4"])
            s5=int(req.POST["s5"])
            s6=int(req.POST["s6"])
            
            total = s1+s2+s3+s4+s5+s6
            percentage = round(total/6, 2)
            
            data={
                "s1":s1,
                "s2":s2,
                "s3":s3,
                "s4":s4,
                "s5":s5,
                "s6":s6,
                "total":total,
                "percentage":percentage,
            }
        pass
    except:
        print("Something Went Wrong!")
        pass
    return render(req, 'marksheet.html', data)


