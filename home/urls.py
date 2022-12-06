
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_review/', views.add_review, name='add_review'),
]
