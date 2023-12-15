from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from accounts.models import User


class SignUpForm(UserCreationForm):
    """Form for signing up/creating new account."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже существует.')
        return email


class AdminUserChangeForm(UserChangeForm):
    """Form for editing `User` (used on the admin panel)."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
        )


class UserInfoForm(forms.ModelForm):
    """Form for editing user info."""

    patronymic = forms.CharField(
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
        )
