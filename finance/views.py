from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from finance.models import CustomUser as User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
     return render(request, 'finance/home.html')

def signup_user(request):
    if request.method == 'GET':
        return render(request, 'finance/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save() 
                login(request, user)
                return redirect('current_finance')
            except: IntegrityError
            return render(request, 'finance/signupuser.html', {'form':UserCreationForm(), 'error':'Имя пользователя уже существует, пожалуйста задайте новое'})
        else:
            return render(request, 'finance/signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})

def login_user(request):
    if request.method == 'GET':
        return render(request, 'finance/signupuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'finance/signupuser.html', {'form':AuthenticationForm(), 'error':' Username And Password Did not match'})
        else:
           login(request, user)
           return redirect('current_finance')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def current_finance(request):
   return render(request, 'finance/current_finance.html') 



        