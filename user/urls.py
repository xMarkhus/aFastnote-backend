from django.urls import path
from . import views

urlpatterns = [
    path("auth/register/", views.CreateUserView.as_view(), name="register"),
    path("user/profile/", views.get_user_profile, name="user-profile"),

]
