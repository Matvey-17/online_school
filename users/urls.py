from users.views import login, register, profile, logout
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', register, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')
]
