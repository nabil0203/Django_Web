# router

from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter



router = DefaultRouter()                                # Created a router which will capture incoming CRUD request
                                                        # then is triggers the corresponding views

router.register('authors', views.AuthorViewSet)                 # this will handle all the 4 Request (get, post, put/patch, delete)




urlpatterns = [

    # path('author/', views.author_list_create, name = 'author_list_create'),                # old function based author list

    path('', include(router.urls)),                                                          # new class based                     

    path('book/', views.book_list_create, name = 'book_list_create')

]

