from django.contrib import admin
from .models import Service, BookService


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'price',
    )

    ordering = ('name',)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('service', 'name', 'date_time', 'user')

    ordering = ('-date_time',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(BookService, BookingAdmin)
