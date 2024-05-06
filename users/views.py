import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.forms import LoginForm, RegisterForm, ProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from main.models import Baskets, OrderItem, Order
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from yookassa import Configuration, Payment
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import transaction
import os
from dotenv import load_dotenv

load_dotenv()


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(password=password, username=username)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                messages.error(request, 'Неверный логин или пароль. Пожалуйста, попробуйте еще раз.')
        else:
            messages.error(request, 'Неверный логин или пароль. Пожалуйста, попробуйте еще раз.')
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
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            mail_subject = 'Активируйте свой аккаунт'
            message = render_to_string('users/acc_active_email.html', {
                'user': user.username,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
                'protocol': 'http'
            })
            send_mail(mail_subject, message, 'Moty017@yandex.ru', [user.email])
            content = {'title': 'NSTU-School - Подтверждение пароля'}
            return render(request, 'users/email_active.html', content)
    else:
        form = RegisterForm()
    content = {
        'title': 'NSTU-School - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', content)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Вы успешно зарегистрировались.')
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            return render(request, 'activation_invalid.html')
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        return render(request, 'activation_invalid.html')


@login_required()
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили свой профиль.')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = ProfileForm(instance=request.user)
    content = {
        'title': 'NSTU-School - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html', content)


@login_required()
def basket(request):
    baskets = Baskets.objects.filter(user=request.user)
    total_sum = 0
    for bask in baskets:
        total_sum += bask.sum()
    content = {
        'title': 'NSTU-School - Корзина',
        'baskets': baskets,
        'total_sum': total_sum
    }
    return render(request, 'users/basket.html', content)


@login_required()
def payment_view(request):
    Configuration.account_id = os.getenv('ACCOUNT_ID')
    Configuration.secret_key = os.getenv('SECRET_KEY_PAYMENT')

    baskets = Baskets.objects.filter(user=request.user)
    total_sum = 0
    for bask in baskets:
        total_sum += bask.sum()

    payment = Payment.create({
        "amount": {
            "value": f"{total_sum}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://127.0.0.1:8000/"
        },
        "capture": True,
        "description": "Тестовый платеж",
    }, uuid.uuid4())

    payment_url = payment.confirmation.confirmation_url

    order = Order(user=request.user, id_order=payment.id, summa=total_sum)
    order.save()

    return HttpResponseRedirect(payment_url)


@csrf_exempt
def message(request):
    event = json.loads(request.body)
    if event['object']['status'] == 'succeeded':
        with transaction.atomic():
            order = Order.objects.get(id_order=event['object']['id'])
            order.status_paid = True
            order.save()

            baskets = Baskets.objects.filter(user=order.user)
            if baskets.exists():
                for bask in baskets:
                    order_item = OrderItem(order=order, item=bask.theme)
                    order_item.save()
                baskets.delete()
    return HttpResponse(200)


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth:login'))
