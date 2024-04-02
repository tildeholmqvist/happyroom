from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('categories/', views.all_categories, name='categories'),  
    path('category/<int:category_id>/', views.main_category, name='category'),
    path('sub_category/<int:subcategory_id>/', views.subcategory_view, name='subcategory'),
]