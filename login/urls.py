from unicodedata import name
from django.urls import path

from .import views

urlpatterns = [

    path('',views.userlogin, name='userlogin'),
    path('registration',views.registration,name='registration'),
    path('homepage',views.homepage, name='homepage'),
    path('userlogout',views.userlogout,name='userlogout')
]
