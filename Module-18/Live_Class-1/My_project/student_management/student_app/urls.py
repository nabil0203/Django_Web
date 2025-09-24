from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    path('', views.list_students, name='list_students'),
    path('create/', views.create_students, name='create_students'),
    
]