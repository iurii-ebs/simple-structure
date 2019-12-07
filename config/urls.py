"""
Your ROOT url file
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('apps.common.urls')),
    path('first-app/', include('apps.first_app.urls')),
    path('auth-token',  rest_views.obtain_auth_token),  # auth endpoint
]
