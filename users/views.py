from django.contrib.auth import logout, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RegisterUserForm, LoginUserForm, UpdateProfileForm, UpdateUserForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "users/login_register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_register_page"] = True
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("users:profile", user.pk)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "users/login_register.html"
    next_page = reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect("users:login")


class UserProfileView(DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "user"


# class UpdateProfileView(UpdateView):
#     model = User
#     form_class = UpdateProfileForm
#     template_name = "users/update_profile.html"
#     context_object_name = "user"

def show_user_profile(request, pk):
    user = get_object_or_404(User.objects.select_related("profile"), pk=pk)
    context = {
        "user": user,
    }
    return render(request, "users/profile.html", context)


def update_profile(request):
    user = get_object_or_404(User.objects.select_related("profile"), pk=request.user.id)
    user_form = UpdateUserForm(instance=user)
    profile_form = UpdateProfileForm(instance=user.profile)
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("users:profile", user.pk)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "users/update_profile.html", context)


class ChangePasswordView(PasswordChangeView):
    template_name = "users/change_password.html"
    success_url = reverse_lazy("users:update_profile")




