from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    s="<h1>About SISTec</h1>"
    return HttpResponse(s)