from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    return render(request, "core/index.html")

def welcome_page(request):
    return render(request, "core/welcome_page.html")