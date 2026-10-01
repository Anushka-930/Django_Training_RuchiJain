from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login,
        name="login"
    ),

    path(
        "evaluation/",
        views.evaluation,
        name="evaluation"
    ),

    path(
        "prediction/",
        views.prediction,
        name="prediction"
    ),

    path(
        "logout/",
        views.logout,
        name="logout"
    ),
]