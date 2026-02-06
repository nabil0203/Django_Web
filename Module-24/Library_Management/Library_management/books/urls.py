# router

from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter



router = DefaultRouter()                                # Created a router which will capture incoming CRUD request
                                                        # then is triggers the corresponding views




urlpatterns = [

    path('author/', views.author_list_create, name = 'author_list_create'),

    path('book/', views.book_list_create, name = 'book_list_create')

]