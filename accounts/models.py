from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        FACULTY = 'FACULTY', 'Faculty / Staff'
        SECURITY = 'SECURITY', 'Security Personnel'
        ADMIN = 'ADMIN', 'System Administrator'

    class AccountStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        SUSPENDED = 'SUSPENDED', 'Suspended'
        PENDING = 'PENDING', 'Pending'

    id_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    role_code = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    account_status = models.CharField(max_length=20, choices=AccountStatus.choices, default=AccountStatus.ACTIVE)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role_code})"