from django.urls import path,include
# from shortcuts import render
from . import views
urlpatterns=[
    path('',views.homepage),
    path('index',views.index),
    path('homepage',views.homepage),
    path('login',views.login),
    path('register',views.register),
    path('logindetails',views.logindetails),
    path('registerdetails',views.registerdetails),
    path('logout',views.logout),
    path('destinations',views.BookingPage),
    path('searching',views.searching),
    path('index1',views.BookStatus),
    path('bookeddetails',views.BookedDetails),
    path('serviceshowing',views.serviceshowing)
    
]