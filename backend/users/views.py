from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create the user
        CustomUser.objects.create_user(username=username, password=password)
        return redirect('login')  # Redirect to login after successful registration

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return render(request, 'login.html', {"error": "Invalid username or password"})

    return render(request, 'login.html')


def home_view(request):
    """
    Displays the home page for authenticated users.
    """
    return render(request, 'home.html', {'user': request.user})


def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page after logging out

