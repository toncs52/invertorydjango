from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.product_detail, name='product_detail'),
    path('create', views.product_create, name='product_create'),
    path('delete/<int:id>', views.product_delete, name='product_delete')
]
