# admin_panel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Admin login view
    path('home/', views.home_view, name='home'),     # Admin home view
]
