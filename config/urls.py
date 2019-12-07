"""
Your ROOT url file
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('apps.common.urls')),
    path('first-app/', include('apps.first_app.urls')),
    path('auth-token', jwt_views.TokenObtainPairView.as_view()),  # auth endpoint
    path('auth-token/refresh', jwt_views.TokenRefreshView.as_view()),  # token refresh endpoint
]
