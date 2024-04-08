from django import forms
from .models import Service, ExpertAppointment


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

        
class ExpertAppointmentForm(forms.ModelForm):
    class Meta:
        model = ExpertAppointment
        fields = ['name', 'email', 'phone',]