"""
Your ROOT url file
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('apps.common.urls')),
    path('first-app/', include('apps.first_app.urls')),
]
