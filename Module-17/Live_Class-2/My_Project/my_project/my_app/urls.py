from django.contrib import admin
from django.urls import path, include                   # 'include' is imported by me
from . import views                                     # imported the views.py of this app

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
]