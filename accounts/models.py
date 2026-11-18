from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        FACULTY = "FACULTY", "Faculty / Staff"
        SECURITY = "SECURITY", "Security Personnel"
        ADMIN = "ADMIN", "System Administrator"

    class AccountStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        SUSPENDED = "SUSPENDED", "Suspended"
        PENDING = "PENDING", "Pending"

    id_number = models.CharField(
        max_length=20,
        unique=True,
        help_text="Official CIT-U Student or Employee ID Number (e.g., 21-1234-567)",
    )
    email = models.EmailField(
        unique=True,
        help_text="Must be a valid CIT-U institutional email (@cit.edu)",
    )
    role_code = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )
    account_status = models.CharField(
        max_length=20,
        choices=AccountStatus.choices,
        default=AccountStatus.ACTIVE,
    )
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return f"{self.id_number} - {self.get_full_name()} ({self.get_role_code_display()})"