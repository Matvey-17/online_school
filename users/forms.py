from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваша фамилия'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Придумайте логин',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш e-mail',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Придумайте пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'class': 'readonly_input, form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True,
        'class': 'readonly_input, form-control'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class PassResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=False,
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'class': 'form-control',
            'style': 'width: 50%;',
            'placeholder': 'Введите e-mail',
        }),
    )


class SetPassForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            'class': 'form-control',
            'style': 'width: 50%;',
            'placeholder': 'Введите новый пароль'
        }),
    )
    new_password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            'class': 'form-control',
            'style': 'width: 50%;',
            'placeholder': 'Подтвердите новый пароль'
        }),
    )
