from django.urls import path
from . import views


urlpatterns=[
    path('',views.loginpage,name='loginpage'),#this is the login page
    path('homepage/',views.homepage,name='hpage'),#this is the home page
    path('fogotpassword/',views.fogotpssd,name='fogotp'),#fogot password
    path('newuser/',views.newuser,name='newuser'),#new user
    path('lotp/',views.lotp,name='lotp'),#loginviaotp


    path('switch-bulb-on/', views.Switch_bulb_on, name='sbulbon'),
     path('switch-bulb-off/', views.Switch_bulb_off, name='sbulboff'),

    path('switch-fan-off/', views.Switch_fan_off, name='sfanoff'),
    path('switch-fan-on/', views.Switch_fan_on, name='sfanonn'),

    path('switch-pump-on/', views.Switch_pump_on, name='spumpon'),
    path('switch-pump-off/',views.Switch_pump_off,name='spumpoff')
]

