from django import forms
from .models import Service, BookService


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']


class BookServiceForm(forms.ModelForm):
    class Meta:
        model = BookService
        fields = ['name', 'email', 'phone', 'date_time']