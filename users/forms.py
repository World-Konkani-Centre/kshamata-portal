from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.functions import Lower
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'batch', 'gender', 'name', 'image', 'date_of_birth', 'college_name', 'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'batch', 'gender', 'name', 'image', 'date_of_birth', 'college_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['team']
