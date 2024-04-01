from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('main_category/', views.main_category, name='main_category'),
]