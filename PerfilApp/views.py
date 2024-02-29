from django.shortcuts import render
from django.http import HttpRequest

def perfil_app(request):
    return render(request,'perfil_app.html')

# Create your views here.
