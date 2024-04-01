from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('category', views.main_category, name='category'),
    path('category/<int:category_id>/', views.subcategory_view, name='subcategory'),
]