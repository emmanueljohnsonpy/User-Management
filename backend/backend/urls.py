from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('admin/', include('admin_panel.urls')), 
]