from django.db import models
from users.models import User


class Items(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Предметы'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    photo = models.ImageField(verbose_name='Фотография')
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Цена')
    name_items = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Subtopics(models.Model):
    name = models.CharField(max_length=1024, verbose_name='Название')
    path_video = models.URLField(verbose_name='Ссылка на вебинар')
    path_abstract = models.URLField(verbose_name='Ссылка на конспект')
    name_themes = models.ForeignKey(Themes, on_delete=models.CASCADE, verbose_name='Тема')

    class Meta:
        verbose_name = 'Подтемы'
        verbose_name_plural = 'Подтемы'

    def __str__(self):
        return self.name


class ValidCourses(models.Model):
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, verbose_name='Тема')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Доступные курсы'
        verbose_name_plural = 'Доступные курсы'

    def __str__(self):
        return self.theme.name


class Baskets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, verbose_name='Тема')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.theme.name}'

    def sum(self):
        return self.quantity * self.theme.price
