# admin_panel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='admin_login'),  # Admin login view
    path('home/', views.home_view, name='admin_home'),     # Admin home view
]
