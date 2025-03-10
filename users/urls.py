from django.urls import path 
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='register'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh')
]


# Register with POST /api/users/register/
# log in with POST /api/users/login/
# refresh the token using POST /api/users/token/refresh/