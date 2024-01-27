from django.shortcuts import render
from users.forms import LoginForm, RegisterForm, ProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(password=password, username=username)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы успешно авторизовались!')
                return HttpResponseRedirect(reverse('main'))
    else:
        form = LoginForm()
    content = {
        'title': 'NSTU-School - Вход',
        'form': form
    }
    return render(request, 'users/login.html', content)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = RegisterForm()
    content = {
        'title': 'NSTU-School - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', content)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили свой профиль!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = ProfileForm(instance=request.user)
    content = {
        'title': 'NSTU-School - Проофиль',
        'form': form
    }
    return render(request, 'users/profile.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
