from django.shortcuts import render

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    return render(request, 'profile.html')

