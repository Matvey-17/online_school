from django.shortcuts import render


def index(request):
    content = {'title': 'NSTU-School - Учись с умом'}
    return render(request, 'main/index.html', content)


def courses(request):
    content = {'title': 'NSTU-School - Каталог'}
    return render(request, 'main/catalog.html', content)


def about_us(request):
    content = {'title': 'NSTU-School - О нас'}
    return render(request, 'main/about.html', content)


def matanaliz(request):
    content = {'title': 'NSTU-School - Матанализ'}
    return render(request, 'main/matanaliz.html', content)


def matanaliz_tema(request):
    content = {'title': 'Функции и графики'}
    return render(request, 'main/matanaliz_tema.html', content)
