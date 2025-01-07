from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import CustomUser 

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_admin:  # Ensure the user is an admin
            login(request, user)  # Log the user in
            return redirect('admin_home')  # Redirect to the admin dashboard (change to your actual admin dashboard URL name)
        else:
            messages.error(request, 'Invalid username or password or you are not an admin.')

    return render(request, 'admin_login.html')


def home_view(request):
    users = CustomUser.objects.all()  # Fetch all users from the CustomUser model
    message = "Welcome to the Admin Dashboard"  # A sample message to display
    return render(request, 'admin_home.html', {'users': users, 'message': message})
