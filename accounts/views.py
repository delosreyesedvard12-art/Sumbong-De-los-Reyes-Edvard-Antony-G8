from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SumbongRegistrationForm, UserProfileUpdateForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = SumbongRegistrationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Account created successfully! Please log in with your credentials.",
        )
        return response


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileUpdateForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        # Ensures a user can only view and edit their own profile
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Your profile details have been updated.")
        return super().form_valid(form)