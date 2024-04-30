from django.urls import path

from main.views import courses, matanaliz, matanaliz_tema, basket_add, basket_remove, available_courses

app_name = 'main'

urlpatterns = [
    path('', courses, name='index'),
    path('matanaliz/', matanaliz, name='matanaliz'),
    path('matanaliz/<str:theme_name>/', matanaliz_tema, name='matanaliz_tema'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('available_courses/', available_courses, name='available_courses'),
    path('available_courses/<str:theme_name>/', available_courses, name='available_courses_filter')
]
