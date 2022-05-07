from django.contrib import admin
from django.urls import path,include
from .views import register_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
    path('',register_view)
]

urlpatterns += staticfiles_urlpatterns()