from django.contrib import admin

from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
    )
    list_filter = ('category',)
    search_fields = (
        'title',
        'category',
    )
