from django.contrib import admin

from .models import Manager, Category, Size, Product

admin.site.register(Manager)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)