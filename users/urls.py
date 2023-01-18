from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/<int:pk>", views.show_user_profile, name="profile"),
    path("update-profile/", views.update_profile, name="update_profile"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change_password"),
]
