from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *

def index(request):

    return render(request, 'index.html', {'message': 'Listado de Productos',
    'title':'Productos',
    'products':[
        {'title':'Playera', 'price':5, 'stock':True},
        {'title':'Camisa', 'price':7, 'stock':True},
        {'title':'Mochila', 'price':20, 'stock':False},
        {'title':'Laptop', 'price':500, 'stock':True},


    ]
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(username))
            return redirect('index')
        else:
            messages.error(request, "Username or Password not valid")
    return render(request, 'users/login.html',locals())

def logout_view(request):

    logout(request)
    
    messages.success(request, 'Logout Succesfully')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)

            messages.success(request, 'User created succesfully')

            return redirect('index')

    return render(request, 'users/register.html', locals())


