from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use the custom user model
        fields = ("username", "email", "password1", "password2")  # Add any custom fields
