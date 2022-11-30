from unicodedata import name
from django.urls import path

from .import views

urlpatterns = [

    path('adminlogin',views.adminlogin, name='adminlogin'),
    path('adminpage',views.adminpage,name='adminpage'),
  
]
