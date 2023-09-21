from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render,redirect
from . models import Service

# Create your views here.
def demo(request):
    ser=Service.objects.all()
    return render(request,"index.html",{'service':ser})
