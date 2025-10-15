from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index_page(request):
    return render(request, "core/index.html")

def information_page(request):
    return render(request, "core/information.html")

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('demo/select')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "core/login.html")