from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.customer_review, name='review'),
]