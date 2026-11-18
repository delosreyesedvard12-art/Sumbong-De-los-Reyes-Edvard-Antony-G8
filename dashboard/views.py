from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from accounts.models import CustomUser


class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    allowed_roles = []

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and self.request.user.role_code in self.allowed_roles
        )


class DashboardRedirectView(LoginRequiredMixin, View):
    """Redirects authenticated users to their role-specific dashboard."""

    def get(self, request, *args, **kwargs):
        role = request.user.role_code
        if role == CustomUser.Role.STUDENT:
            return redirect("student_dashboard")
        elif role == CustomUser.Role.FACULTY:
            return redirect("staff_dashboard")
        elif role == CustomUser.Role.SECURITY:
            return redirect("security_dashboard")
        elif role == CustomUser.Role.ADMIN:
            return redirect("admin_dashboard")
        return redirect("profile")


class StudentDashboardView(RoleRequiredMixin, TemplateView):
    template_name = "dashboard/student_dashboard.html"
    allowed_roles = [CustomUser.Role.STUDENT]


class StaffDashboardView(RoleRequiredMixin, TemplateView):
    template_name = "dashboard/staff_dashboard.html"
    allowed_roles = [CustomUser.Role.FACULTY]


class SecurityDashboardView(RoleRequiredMixin, TemplateView):
    template_name = "dashboard/security_dashboard.html"
    allowed_roles = [CustomUser.Role.SECURITY]


class AdminDashboardView(RoleRequiredMixin, TemplateView):
    template_name = "dashboard/admin_dashboard.html"
    allowed_roles = [CustomUser.Role.ADMIN]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_users"] = CustomUser.objects.count()
        context["student_count"] = CustomUser.objects.filter(role_code=CustomUser.Role.STUDENT).count()
        context["staff_count"] = CustomUser.objects.filter(role_code=CustomUser.Role.FACULTY).count()
        context["security_count"] = CustomUser.objects.filter(role_code=CustomUser.Role.SECURITY).count()
        return context