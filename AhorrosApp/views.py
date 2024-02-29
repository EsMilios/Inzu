from django.shortcuts import render
from django.http import HttpRequest

def ahorros_app(request):
    return render(request,'ahorros_app.html')