from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("authentication/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("authentication/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("authentication/", include("rest_framework.urls")),
]
