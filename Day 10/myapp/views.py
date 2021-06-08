from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student

def homepageview(request):
    return render(request,"home.html",{})

def aboutpageview(request):
    return render(request,"about.html")

def contactpageview(request):
    return render(request,"contact.html")

def myform(request):
    return render(request,"myform.html")

def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    name  = (request.POST['name'])
    email  = (request.POST['Email'])
    age = int(request.POST['age'])
    contact = int(request.POST['contact'])
    city = (request.POST['city'])
    print(name, email, age, contact, city)
    
    return render(request,"ans.html",{
            'myname':name,
            'myemail':email,
            'myage':age,
            'mycontact':contact,
            'mycity':city,})

class studentlist(ListView):
   model = Student
   template_name = 'slist.html'