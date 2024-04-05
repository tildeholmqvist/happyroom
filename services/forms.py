from django import forms
from .models import ExpertAppointment

class ExpertAppointmentForm(forms.ModelForm):
    class Meta:
        model = ExpertAppointment
        fields = ['name', 'email', 'phone', 'date_time', 'message']