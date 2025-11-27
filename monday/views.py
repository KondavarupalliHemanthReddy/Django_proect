from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# @login_required
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def special(request):
    return render(request,'special.html')
def fresh(request):
    return render(request,'fresh.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created. Please login.")
        return redirect('login')
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to any page you want
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')

