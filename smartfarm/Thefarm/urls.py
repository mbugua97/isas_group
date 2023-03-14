from django.urls import path
from . import views


urlpatterns=[
    path('',views.loginpage,name='loginpage'),#this is the login page
    path('homepage/',views.homepage,name='hpage'),#this is the home page
    path('fogotpassword/',views.fogotpssd,name='fogotp'),#fogot password
    path('newuser/',views.newuser,name='newuser'),#new user
    path('lotp/',views.lotp,name='lotp')#loginviaotp

]

