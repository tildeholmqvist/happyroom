from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('expertise/', views.expertise, name='expertise'),
    path('inspration/', TemplateView.as_view(template_name='inspiration.html'), name='inspiration'),
]