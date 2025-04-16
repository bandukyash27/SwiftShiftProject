from django.shortcuts import render,redirect
from app.models import *
from django.http import *
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,'index.html')

def Services(request):
    return render(request,'Services.html')

def LocalMoving(request):
    return render(request,'LocalMoving.html')

def Longdistance(request):
    return render(request,'Longdistance.html')

def Contactus(request):
    return render(request,'Contactus.html')

def CommercialMoving(request):
    return render(request,'CommercialMoving.html')

def Storage(request):
    return render(request,'Storage.html')
def Packunpacking(request):
    return render(request,'PackUnpack.html')
def Petreloctaion(request):
    return render(request,'Petrelocation.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            auth_login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request,'login.html')

    

def aboutus(request):
    return render(request,'aboutus.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect(signup)
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect(login)
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('/signup')
    else:
        return render(request, 'signup.html')

def Contactus(request):
    if request.method=='POST':
        na=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        message=request.POST['message']
        LCO=ContactDetails.objects.get_or_create(name=na,mobileno=mobile,email=email,message=message)
        messages.success(request,"Your message is submitted")
    return render(request,'Contactus.html')
        