from django.shortcuts import render

# Create your views here.
def contactpg(request):
    return render(request,"contact.html")