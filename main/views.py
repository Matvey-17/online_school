from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from main.models import Themes, Subtopics, Baskets
from django.contrib import messages


def index(request):
    content = {'title': 'NSTU-School - Учись с умом'}
    return render(request, 'main/index.html', content)


@login_required()
def courses(request):
    content = {'title': 'NSTU-School - Каталог'}
    return render(request, 'main/catalog.html', content)


@login_required()
def matanaliz(request):
    themes = Themes.objects.all()
    content = {'title': 'NSTU-School - Матанализ', 'themes': themes}
    return render(request, 'main/matanaliz.html', content)


@login_required()
def matanaliz_tema(request, theme_name):
    theme = Themes.objects.get(name=theme_name)
    subtopics = Subtopics.objects.filter(name_themes=theme)
    content = {
        'title': theme.name,
        'subtopics': subtopics,
        'theme': theme
    }
    return render(request, 'main/matanaliz_tema.html', content)


@login_required()
def basket_add(request, product_id):
    product = Themes.objects.get(id=product_id)
    baskets = Baskets.objects.filter(user=request.user, theme=product)
    if not baskets.exists():
        Baskets.objects.create(user=request.user, theme=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    messages.success(request, 'Товар добавлен в корзину.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required()
def basket_remove(request, basket_id):
    basket = Baskets.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
