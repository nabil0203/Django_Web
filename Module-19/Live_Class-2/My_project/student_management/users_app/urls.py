from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    path('register/', views.register_view, name='register'),                    # for register new user
    
    path('login/', views.login_view, name='login'),                           # for user login

    path('logout/', views.logout_view, name='logout'),                           # for logout

]

