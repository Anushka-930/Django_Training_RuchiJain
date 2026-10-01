from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("register/", views.saveuser, name="saveuser"),
    path("login/", views.login, name="login"),
    path("login/validate/", views.loginvalidation, name="loginvalidation"),
    path("logout/", views.logout, name="logout"),
]