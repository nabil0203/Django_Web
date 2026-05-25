from django.urls import path
from . import views


urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('create/', views.create_invoice, name='create_invoice'),
    path('details/<int:id>/', views.invoice_details, name='invoice_details'),
    path("<int:id>/pdf/", views.invoice_pdf, name="invoice_pdf"),

]