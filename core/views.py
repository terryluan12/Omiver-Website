from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, "core/index.html")

def welcome_page(request):
    pages = [
        {
            "heading": "Omiver is a Wellness Technology Company",
            "description": "Thank you for your interest in Omiver! Our demo will provide an overview \
        of our full-scale service, our proprietary model, and reporting \
        platform. You will get the opportunity to try our model through the lens \
        of our three demo profiles: Sofia Rivera, Marcus Thompson, and Jackson \
        Lee. Their lifestyle profiles and metabolic data has already been filed \
        for your convenience.",
            "cartoon_url": "core/welcome/1/cartoon.svg",
            "carton_alt": "Cartoon image of someone checking their phone in front of a giant phone with a profile layout blowup",
            "photo_url": "core/welcome/1/athlete.png",
            "photo_alt": "Athlete taking off phone on their arm"
        }, 
        {
            "heading": "Nutrition & Fitness Management",
            "description": "Omiver integrates biomarker technology and AI  \
        models to provide accessible, scientifically-backed  \
        regimens that are designed for your clients’ specific  \
        nutrition and fitness goals.",
            "cartoon_url": "core/welcome/2/cartoon.svg",
            "carton_alt": "Cartoon image of two people. One person is looking over charts and graphs of indeterminable data, the other is talking to the first, with a speech bubble above their head",
            "photo_url": "core/welcome/2/athlete.png",
            "photo_alt": "An athlete running on the lakeshore"
        },
        {
            "heading": "Exclusively for Wellness Purposes",
            "description": "Omiver cannot diagnose you with any disease or  \
        condition. Omiver tests are intended exclusively for \
        wellness purposes and are not intended as a substitute  \
        for medical advice or advice of a medical professional.",
            "cartoon_url": "core/welcome/3/cartoon.svg",
            "carton_alt": "Cartoon image of three people around a giant phone. The three people are sitting on a chair, on the ground, and walking respectively. On the phone screen is a messaging app. Presumably they are messaging each other. ",
            "photo_url": "core/welcome/3/athlete.png",
            "photo_alt": "An athlete stretching, with his arms above his head"
        }
    ]
    
    return render(request, "core/welcome.html", {"pages": pages})

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