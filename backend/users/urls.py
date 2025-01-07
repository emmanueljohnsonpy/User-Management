from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('home/', views.home_view, name='home'), 
    path('profile/', views.profile_view, name='profile'),  # User profile
    path('logout/', views.logout_view, name='logout'),  # User logout
]
