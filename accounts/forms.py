from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SumbongRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address.",
    )
    id_number = forms.CharField(
        max_length=20,
        required=True,
        label="ID Number",
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "id_number",
            "first_name",
            "last_name",
            "email",
            "contact_number",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "contact_number",
            "profile_photo",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email address is already in use by another account.")
        return email