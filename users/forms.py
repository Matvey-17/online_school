from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Ваше имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Ваша фамилия'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Придумайте логин',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Ваш e-mail',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Придумайте пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control item',
        'placeholder': 'Подтвердите пароль',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput())
    last_name = forms.CharField(required=False, widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
        'class': 'readonly_input'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True,
        'class': 'readonly_input'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
