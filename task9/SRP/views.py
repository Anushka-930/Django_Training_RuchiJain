from django.shortcuts import render, redirect
from SRP.models import user
from django.contrib.auth.hashers import check_password, make_password


def home(request):
    return render(request, "home.html", {"student_name": request.session.get("student_name")})


def signup(request):
    return render(request, "signup.html")


def saveuser(request):
    if request.method != "POST":
        return redirect("signup")

    name = request.POST.get("name", "").strip()
    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    if not name or not username or not password:
        return render(request, "signup.html", {"errormsg": "Please complete every field."})
    if user.objects.filter(username=username).exists():
        return render(request, "signup.html", {"errormsg": "That username is already registered."})

    user.objects.create(username=username, password=make_password(password), name=name)
    return redirect("login")


def login(request):
    return render(request,'login.html')


def loginvalidation(request):
    if request.method != "POST":
        return redirect("login")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    try:
        student = user.objects.get(username=username)
    except user.DoesNotExist:
        student = None

    if student and check_password(password, student.password):
        request.session["student_name"] = student.name
        return redirect("home")
    return render(request, "login.html", {"erg": "Invalid username or password."})


def logout(request):
    request.session.flush()
    return redirect("home")

# Create your views here.
