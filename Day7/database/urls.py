from django.urls import path
from .views import deleteemployee, employeelist, newemployee, saveuser, updateemployee

urlpatterns = [
    path('newemployee/', newemployee,name='newemployee'),
    path('deleteemployee/', deleteemployee,name='deleteemployee'),
    path('updateemployee/', updateemployee,name='updateemployee'),
    path('employeelist/', employeelist,name='employeelist'),
    path('saveuser/', saveuser,name='saveuser'),
]
