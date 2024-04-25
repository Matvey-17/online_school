from django.urls import path

from main.views import courses, matanaliz, matanaliz_tema, basket_add, basket_remove

app_name = 'main'

urlpatterns = [
    path('', courses, name='index'),
    path('matanaliz/', matanaliz, name='matanaliz'),
    path('matanaliz/<str:theme_name>', matanaliz_tema, name='matanaliz_tema'),
    path('add/<int:product_id>', basket_add, name='basket_add'),
    path('remove/<int:basket_id>', basket_remove, name='basket_remove')
]
