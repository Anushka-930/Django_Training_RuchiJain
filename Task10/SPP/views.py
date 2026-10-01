import os
import joblib

from django.conf import settings
from django.shortcuts import render, redirect

from .models import Student


def find_model_file(*possible_names):
    for name in possible_names:
        path = os.path.join(settings.BASE_DIR, name)
        if os.path.exists(path):
            return path
    raise FileNotFoundError(
        "No model file found. Checked: " + ", ".join(possible_names)
    )


MODEL_PATH = find_model_file("mlmodel.pkl", "mlmodel (1).pkl")
SCALER_PATH = find_model_file("scalermodel.pkl", "scalermodel (1).pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":

        student_id = request.POST.get("student_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")
        password = request.POST.get("password")

        if not all([student_id, name, email, course, password]):
            return render(
                request,
                "register.html",
                {"error": "Please fill all fields."}
            )

        Student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            course=course,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":

        student_id = request.POST.get("student_id")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not all([student_id, email, password]):
            return render(
                request,
                "login.html",
                {"error": "Please enter Student ID, Email and Password."}
            )

        student = Student.objects.filter(
            student_id=student_id,
            email=email,
            password=password
        ).first()

        if student is not None:
            request.session["student_id"] = student.id
            return redirect("evaluation")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid Student ID, Email or Password"
            }
        )

    return render(request, "login.html")


def evaluation(request):

    if "student_id" not in request.session:
        return redirect("login")

    if request.method == "POST":

        student = Student.objects.get(
            id=request.session["student_id"]
        )

        cgpa_value = request.POST.get("cgpa")
        programming_skills = request.POST.get("programming_skills")
        technical_skills = request.POST.get("technical_skills")
        communication_skills = request.POST.get("communication_skills")

        if not all([cgpa_value, programming_skills, technical_skills, communication_skills]):
            return render(
                request,
                "evaluation.html",
                {"error": "Please fill all evaluation fields."}
            )

        try:
            cgpa = float(cgpa_value)
        except ValueError:
            return render(
                request,
                "evaluation.html",
                {"error": "CGPA must be a valid number."}
            )

        student.cgpa = cgpa
        student.programming_skills = programming_skills
        student.technical_skills = technical_skills
        student.communication_skills = communication_skills

        student.save()

        return redirect("prediction")

    return render(
        request,
        "evaluation.html"
    )


def prediction(request):

    if "student_id" not in request.session:
        return redirect("login")

    student = Student.objects.get(
        id=request.session["student_id"]
    )

    try:

        cgpa = float(student.cgpa or 0)
        programming = float(student.programming_skills or 0)
        technical = float(student.technical_skills or 0)

        data = [[cgpa, programming, technical]]

        scaled_data = scaler.transform(data)

        result = model.predict(scaled_data)

        prediction_result = result[0]

    except Exception as e:

        prediction_result = "Prediction Error"

        print("ML Error:", e)

    return render(
        request,
        "result.html",
        {
            "student": student,
            "prediction": prediction_result
        }
    )


def logout(request):

    request.session.flush()

    return redirect("home")