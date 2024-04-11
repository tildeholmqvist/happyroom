from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.customer_review, name='review'),
    path('review_list/', views.review_list, name='review_list'),
]