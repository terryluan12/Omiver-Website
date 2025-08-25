from django.shortcuts import render
from django.conf import settings
import os, json

def select_page(request):
    DATA_FILE = os.path.join(settings.BASE_DIR, "demo", "data", "profiles.json")
    with open(DATA_FILE) as f:
        profile_data = json.load(f)
    return render(request, "demo/select.html", {"profiles": profile_data})