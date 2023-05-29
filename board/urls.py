from django.contrib import admin
from django.urls import path, include
from board import views

urlpatterns = [
    # board/
    path('', views.index),
    path('create/', views.create),
    path('update/<id>/', views.update),
    path('delete/', views.delete),
    path('<id>/', views.read),
]
