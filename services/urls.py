from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.services, name='services'),
    path('add/', views.add_service, name='add_service'),
    path('book_services/', views.book_services, name='book_services'),
    path('inspration/', TemplateView.as_view(template_name='inspiration.html'), name='inspiration'),
]