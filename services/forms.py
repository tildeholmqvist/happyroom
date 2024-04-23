from django import forms
from products.widgets import CustomClearableFileInput
from .models import Service, BookService


class ServiceForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'image']


class BookServiceForm(forms.ModelForm):
    class Meta:
        model = BookService
        fields = ['name', 'email', 'phone', 'date_time']
        labels = {
            'date_time': 'Date & Time'
        }
