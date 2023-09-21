from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        e_mail=request.POST['email']
        passwd=request.POST['password']
        passwd1=request.POST['password1']
        if passwd == passwd1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"User name already taken!")
                return redirect('credentials:register')
            elif User.objects.filter(email=e_mail).exists():
                messages.info(request,"Email already registered!")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=uname,
                                              password=passwd,
                                              first_name=fname,
                                              last_name=lname,
                                              email=e_mail)
                user.save();
                print("User created")
                return redirect('credentials:login')
        else:
            messages.info(request,"Password not matched!")
            return redirect('credentials:register')
        return redirect('/')
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        passwd=request.POST['password']
        user=auth.authenticate(username=uname,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('credentials:login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


