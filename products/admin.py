from django.contrib import admin
from .models import Product, Category, SubCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'display_categories',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

    def display_categories(self, obj):
        return ', '.join(category.name for category in obj.category.all())


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'is_filterable',
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.exclude(name__in=['bestsellers', 'new_items', 'last_chance'])


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
