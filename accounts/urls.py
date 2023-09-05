from django.shortcuts import render, redirect
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('logout/', views.logout_user, name='logout'),
    path('contact/', views.contact, name='contact'),
]
