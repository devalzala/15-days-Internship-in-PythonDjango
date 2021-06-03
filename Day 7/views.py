from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("<h1>Welcome to site</h1>")

def aboutpageview(request):
    return HttpResponse("<h1>About Us</h1>")

def contactpageview(request):
    return HttpResponse("<h1>Contact Us</h1>")

