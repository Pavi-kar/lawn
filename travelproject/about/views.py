from django.shortcuts import render

# Create your views here.
def aboutpg(request):
    return render(request,"about.html")