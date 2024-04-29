from django.contrib import admin
from main.models import Items, Themes, ValidCourses, Subtopics, Baskets, OrderItem, Order

admin.site.register(Items)
admin.site.register(Themes)
admin.site.register(Subtopics)
admin.site.register(ValidCourses)
admin.site.register(Baskets)
admin.site.register(Order)
admin.site.register(OrderItem)
