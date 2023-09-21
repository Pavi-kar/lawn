from django.shortcuts import render

# Create your views here.
def blogpg(request):
    return render(request,"blog-home-1.html")
