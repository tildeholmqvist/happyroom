from django.urls import path
from . import views
from bag import views as bag_views 

urlpatterns = [
    path('', views.services, name='services'),
    path('add_service/', views.add_service, name='add_service'),
    path('services/book_service/<int:service_id>/', views.book_service, name='book_service'),
    path('service_confirmation/<int:booking_id>/', views.service_confirmation, name='service_confirmation'),
    path('edit/<int:service_id>', views.edit_service, name='edit_service'),
    path('delete/<int:service_id>', views.delete_service, name='delete_service'),
]