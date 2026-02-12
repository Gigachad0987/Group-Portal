from typing import Any
from django import forms
from django.contrib.auth.models import User
from django .contrib.auth.forms import UserCreationForm
from .models import UserProfile
class UserRegisterform(UserCreationForm):
    bio = forms.CharField(label="Bio", required=False)
    avatar = forms.ImageField(label="Avatar", required=False)
    class Meta():
        model = User
        fields = ["username", "email", "password1", "password2", "bio", "avatar"]
    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit)
        if commit == True:
            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(user=user,bio=self.cleaned_data['bio'], avatar=self.cleaned_data['avatar'])
            else:
                pass
        return user