from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    path('', views.list_students, name='list_students'),
    path('create/', views.create_students, name='create_students'),
    path('edit/<int:id>', views.update_students, name='update_students'),
    path('delete/<int:id>', views.delete_students, name='delete_students')
]






# path('', ..........)----->    here, 'blank' means if we visit "127.0.0.1" then the "list_student"-function of view.py will execute. And that is designed to run student_list.html
# path('create/', ..........)----->     here, 'create/' means if we visit "127.0.0.1/create" then the "create_student"-function of view.py will execute. And that is designed to run student_create.html
# path('edit/<int:id>', ..........)----->    here, 'edit/<int:id>' means if we click on any 'edit' button, then the "update_student"-function of view.py will execute. It will take to that specific object's page

