from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from database.models import Employee
from django.urls import reverse

def newemployee(request): #create record (c of CRUD)
    res=render(request, 'newemployee.html')
    return res
def saveuser(request): #create record (c of CRUD)
    
    eno=eno=request.POST['eno']
    ename=ename=request.POST['ename']
    esal=esal=request.POST['esal']
    emp=Employee(eno=eno, ename=ename, esal=esal)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url) 

def employeelist(request): #read record (r of CRUD)
    employees=Employee.objects.all() #it returns all the records of Employee table
    res=render(request, 'employeelist.html', {'employees': employees})
    return res

def updateemployee(request):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, id=request.POST['id'])
        employee.eno = request.POST['eno']
        employee.ename = request.POST['ename']
        employee.esal = request.POST['esal']
        employee.save()
        url = reverse('employeelist')
        return HttpResponseRedirect(url)

    employee = get_object_or_404(Employee, id=request.GET.get('id'))
    return render(request, 'updateemployee.html', {'employee': employee})

    #update record (u of CRUD)

def deleteemployee(request):
    id=request.GET.get('id')
    emp=Employee.objects.filter(id=id)
    emp.delete()
    url=reverse('employeelist')
    return HttpResponse('<h1>Record Deleted</h1>')
    #delete record (d of CRUD)
# Create your views here.