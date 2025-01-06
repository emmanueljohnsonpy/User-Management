from django.shortcuts import render

def login_view(request):
    return render(request, 'admin_login.html')

def home_view(request):
    return render(request, 'admin_home.html')
