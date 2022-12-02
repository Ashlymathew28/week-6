from unicodedata import name
from django.urls import path

from .import views

urlpatterns = [

    path('adminlogin',views.adminlogin, name='adminlogin'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('user_insert <int:id>',views.user_insert,name='user_insert'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_delete <int:id>',views.admin_delete,name='admin_delete'),
    path('add_user',views.add_user,name='add_user'),
    path('search',views.search,name='search')
  
]
