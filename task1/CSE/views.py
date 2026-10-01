from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def About(request):
    s="<h1>CSE</h1>"
    return HttpResponse(s)
