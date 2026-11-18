from django.urls import path
from .views import (
    AdminDashboardView,
    DashboardRedirectView,
    SecurityDashboardView,
    StaffDashboardView,
    StudentDashboardView,
)

urlpatterns = [
    path("", DashboardRedirectView.as_view(), name="dashboard_redirect"),
    path("student/", StudentDashboardView.as_view(), name="student_dashboard"),
    path("staff/", StaffDashboardView.as_view(), name="staff_dashboard"),
    path("security/", SecurityDashboardView.as_view(), name="security_dashboard"),
    path("admin-dashboard/", AdminDashboardView.as_view(), name="admin_dashboard"),
]