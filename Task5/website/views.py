from django.shortcuts import render


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def cities(request):
    return render(request, "website/cities.html")
