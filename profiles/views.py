from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'profiles/profile.html', {'profile', profile})