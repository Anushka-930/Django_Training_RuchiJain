"""
URL configuration for task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from SISTEC import views as v1
from CSE import views as v2 
from AIDS import views as v3


urlpatterns = [
    path("Home",v1.Home),
    path("About",v2.About),
    path("AIDS",v3.AIDS),
    path("admin/", admin.site.urls),
]
