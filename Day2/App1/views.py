from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):  
    s = "<h1>Welcome to Home</h1>"
    return HttpResponse(s)

def about(request):  
    s = "<h1>Welcome to Home Page</h1>"
    return HttpResponse(s)




