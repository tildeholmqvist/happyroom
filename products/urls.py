from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('all_categories/', views.all_categories, name='all_categories'),
    path('all_categories/<int:selected_category>/', views.all_categories, name='all_categories_selected'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('new_items/', views.new_items, name='new_items'),
    path('last_chance/', views.last_chance, name='last_chance'),
]