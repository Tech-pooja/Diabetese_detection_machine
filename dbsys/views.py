from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Hello I am WOrking") 
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def Prediction(request):
    return render(request,"Prediction.html")