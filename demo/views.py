from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
import os, json


def welcome_page(request, index=0):
    pages = [
        {
            "heading": "Omiver is a Wellness Technology Company",
            "description": "Thank you for your interest in Omiver! Our demo will provide an overview \
        of our full-scale service, our proprietary model, and reporting \
        platform. You will get the opportunity to try our model through the lens \
        of our three demo profiles: Sofia Rivera, Marcus Thompson, and Jackson \
        Lee. Their lifestyle profiles and metabolic data has already been filed \
        for your convenience.",
            "cartoon_url": "demo/welcome/1/cartoon.svg",
            "carton_alt": "Cartoon image of someone checking their phone in front of a giant phone with a profile layout blowup",
            "photo_url": "demo/welcome/1/athlete.png",
            "photo_alt": "Athlete taking off phone on their arm"
        }, 
        {
            "heading": "Nutrition & Fitness Management",
            "description": "Omiver integrates biomarker technology and AI  \
        models to provide accessible, scientifically-backed  \
        regimens that are designed for your clients’ specific  \
        nutrition and fitness goals.",
            "cartoon_url": "demo/welcome/2/cartoon.svg",
            "carton_alt": "Cartoon image of two people. One person is looking over charts and graphs of indeterminable data, the other is talking to the first, with a speech bubble above their head",
            "photo_url": "demo/welcome/2/athlete.png",
            "photo_alt": "An athlete running on the lakeshore"
        },
        {
            "heading": "Exclusively for Wellness Purposes",
            "description": "Omiver cannot diagnose you with any disease or  \
        condition. Omiver tests are intended exclusively for \
        wellness purposes and are not intended as a substitute  \
        for medical advice or advice of a medical professional.",
            "cartoon_url": "demo/welcome/3/cartoon.svg",
            "carton_alt": "Cartoon image of three people around a giant phone. The three people are sitting on a chair, on the ground, and walking respectively. On the phone screen is a messaging app. Presumably they are messaging each other. ",
            "photo_url": "demo/welcome/3/athlete.png",
            "photo_alt": "An athlete stretching, with his arms above his head"
        }
    ]
    index = int(index)
    if index > len(pages) - 1:
        response = HttpResponse()
        response['HX-Redirect'] = '/login'
        return response
    
    if index < 0:
        response = HttpResponse()
        response['HX-Redirect'] = '/'
        return response
    
    return render(request, "demo/welcome.html", {"page": pages[index], "next_index": index+1, "prev_index": index - 1})


@login_required
def select_page(request):
    DATA_FILE = os.path.join(settings.BASE_DIR, "demo", "data", "profiles.json")
    with open(DATA_FILE) as f:
        profile_data = json.load(f)
    return render(request, "demo/select.html", {"profiles": profile_data})

def profile_detail(request, id):
    DATA_FILE = os.path.join(settings.BASE_DIR, "demo", "data", "profiles.json")
    with open(DATA_FILE) as f:
        all_profiles = json.load(f)
    profile_data = all_profiles[id]
    
    return render(request, "demo/profile_detail.html", profile_data)

def process(request):
    return render(request, "demo/process.html")

def layout(request):
    return render(request, "demo/two_column_layout.html")