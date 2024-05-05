from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from main.models import Themes, Subtopics, Baskets, Order, OrderItem, Items
from django.contrib import messages
from django.http import JsonResponse
from main.serializers_views import SubtopicsSerializer


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
    return redirect('auth:basket')


@login_required()
def basket_remove(request, basket_id):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        basket = Baskets.objects.get(id=basket_id)
        basket.delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})


@login_required()
def available_courses(request, theme_name=None):
    page = request.GET.get('page', 1)
    page = int(page)
    per_page = 5

    themes_menu = Items.objects.all().prefetch_related('themes')
    theme_menu = None

    subtopics_list = []
    orders = Order.objects.filter(user=request.user, status_paid=True)
    themes = OrderItem.objects.filter(order__in=orders)
    for theme in themes:
        if theme_name:
            subtopics = Subtopics.objects.filter(Q(name_themes=theme.item) & Q(name_themes__name=theme_name))
            subtopics_list.extend(subtopics)
            theme_menu = theme_name
        else:
            subtopics = Subtopics.objects.filter(name_themes=theme.item)
            subtopics_list.extend(subtopics)
    paginator = Paginator(subtopics_list, per_page)
    subtopics = paginator.get_page(page)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        subtopics_serializer = SubtopicsSerializer(subtopics, many=True)
        data = subtopics_serializer.data
        return JsonResponse(data, safe=False)
    else:
        content = {
            'title': 'NSTU-School | Доступные курсы',
            'subtopics': subtopics,
            'themes_menu': themes_menu,
            'theme_menu': theme_menu
        }
        return render(request, 'main/available_courses.html', content)
