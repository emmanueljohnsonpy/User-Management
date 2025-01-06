from django.shortcuts import render

def register_view(request):
    return render(request, 'register.html', {'message': 'register'})

def login_view(request):
    return render(request, 'login.html', {'message': 'login'})

def home_view(request):
    return render(request, 'home.html', {'message': 'home'})

def profile_view(request):
    return render(request, 'profile.html', {'message': 'profile'})

