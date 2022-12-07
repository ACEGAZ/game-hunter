
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('<int:review_id>/', views.index, name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('add_review_success/', views.add_review_success,
         name='add_review_success'),
]
