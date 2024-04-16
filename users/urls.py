from users.forms import PassResetForm, SetPassForm
from users.views import login, register, profile, logout
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', register, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
                                              email_template_name='users/password_reset_email.html',
                                              success_url=reverse_lazy('auth:password_reset_done'),
                                              form_class=PassResetForm),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                     success_url=reverse_lazy('auth:password_reset_complete'),
                                                     form_class=SetPassForm,
                                                     title='Придумайте новый пароль'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
