from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "id_number", "email", "role_code", "account_status", "is_staff"]
    list_filter = ["role_code", "account_status", "is_staff"]
    search_fields = ["username", "id_number", "email", "first_name", "last_name"]

    fieldsets = UserAdmin.fieldsets + (
        (
            "CIT-U Institutional Profile",
            {
                "fields": (
                    "id_number",
                    "role_code",
                    "account_status",
                    "contact_number",
                    "profile_photo",
                )
            },
        ),
    )