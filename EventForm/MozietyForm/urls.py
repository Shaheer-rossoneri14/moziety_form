from django.contrib import admin
from django.urls import path,include
from .views import register_view

urlpatterns = [
    path('form',register_view)
]