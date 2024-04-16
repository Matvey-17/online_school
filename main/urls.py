from django.urls import path

from main.views import courses, matanaliz, matanaliz_tema

app_name = 'main'

urlpatterns = [
    path('', courses, name='index'),
    path('matanaliz/', matanaliz, name='matanaliz'),
    path('matanaliz/function', matanaliz_tema, name='matanaliz_tema')
]
