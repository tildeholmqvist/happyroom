from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'price',
    )

    ordering = ('name',)


admin.site.register(Service, ServiceAdmin)