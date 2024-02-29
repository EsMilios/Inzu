from django.shortcuts import render
from django.http import HttpRequest

def inicioApp_inicio(request):
    return render(request,'inicioApp.html')

# Create your views here.
