from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # User login
    path('register/', views.register_view, name='register'),  # User registration
    path('home/', views.home_view, name='home'), 
    path('profile/', views.profile_view, name='profile'),  # User profile
    # path('logout/', views.logout_view, name='logout'),  # User logout
]
