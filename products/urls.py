from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('all_categories/', views.all_categories, name='all_categories'),
    path('all_categories/<int:selected_category>/', views.all_categories, name='all_categories_selected'),
]