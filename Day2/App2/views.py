from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def facebook(request):  
    s = "<h1>Welcome to Home Page</h1>"
    return HttpResponse(s)

def instagram(request):  
    s = "<h1>Welcome to Home Page</h1>"
    return HttpResponse(s)