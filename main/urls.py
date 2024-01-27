from django.urls import path

from main.views import courses, matanaliz

app_name = 'main'

urlpatterns = [
    path('', courses, name='index'),
    path('matanaliz/', matanaliz, name='matanaliz')
]
