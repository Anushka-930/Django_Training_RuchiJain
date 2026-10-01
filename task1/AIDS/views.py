from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def AIDS(request):
    s="<h1>AIDS Department is good</h1>"
    return HttpResponse(s)
