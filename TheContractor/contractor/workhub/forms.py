from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser  # Import your custom user model
from django.contrib.auth.forms import UserChangeForm
from .models import JobApplication



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use the custom user model
        fields = ("username", "email", "password1", "password2")  # Add any custom fields


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_picture']  # add other fields if needed

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['job', 'submitted_at']
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'rows': 5,
                'maxlength': 1000,
                'placeholder': 'Write your cover letter here...'
            }),
            'experience_details': forms.Textarea(attrs={'rows': 4}),
        }