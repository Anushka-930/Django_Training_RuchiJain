from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

def home(request):
    res=render(request, 'home.html')
    return res
def result(request):
    scaler=joblib.load('scalermodel.pkl')
    mlmodel=joblib.load('mlmodel.pkl')
    lis=[]
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])
    scaled_input=scaler.transform([lis])
    ans=mlmodel.predict(scaled_input)[0]

    res=render(request,'result.html',{'ans':ans,'lis':lis})
    return res
    

# Create your views here.
