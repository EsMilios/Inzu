from django.shortcuts import render
from django.http import HttpRequest

def Estadisticas_app(request):
    return render(request,'Estadisticas_app.html')
