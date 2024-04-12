from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    comment = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'placeholder': 'Leave your feedback', 'cols': 50, 'rows': 5}))
    class Meta:
        model = Review
        fields = ['name', 'comment']
