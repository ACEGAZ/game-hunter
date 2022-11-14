from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.bag_view, name='bag_view'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<str:item_id>/', views.adjust_bag, name="adjust_bag"),
]